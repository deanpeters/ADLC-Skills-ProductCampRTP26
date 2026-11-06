"""Synthetic mechanical tests. Passing these does NOT approve the product contract."""

import asyncio
import json
import shutil
import sys
from concurrent.futures import ThreadPoolExecutor

import pytest
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from server import KevinStore, ROOT, TOOLS


@pytest.fixture(params=["may-2025", "oct-2026"])
def store(tmp_path, request):
    shutil.copytree(ROOT / "data", tmp_path / "data", ignore=shutil.ignore_patterns("state.json"))
    shutil.copy2(ROOT / "permissions.yaml", tmp_path / "permissions.yaml")
    return KevinStore(tmp_path, request.param)


def test_read_and_summary_are_read_only(store):
    assert store.call("read_feedback", {})["allowed"]
    summary = store.call("summarize_themes", {"message_ids": ["msg-1", "msg-2"]})
    assert summary["result"]["themes"] == {"damaged item": 1, "cancellation": 1}
    assert not store.state_path.exists()


@pytest.mark.parametrize("tool,args,bucket", [
    ("draft_reply", {"message_id": "msg-1"}, "drafts"),
    ("send_reply", {"message_id": "msg-1", "text": "Synthetic reply for review."}, "sent"),
    ("issue_credit", {"member_id": "member-1", "order_id": "order-1", "amount": 20}, "credits"),
    ("offer_coupon", {"member_id": "member-2", "percent": 30}, "coupons"),
    ("update_address", {"member_id": "member-3", "address": "Fictional Point Z"}, "members"),
])
def test_tools_obey_effective_policy_not_product_approval(store, tool, args, bucket):
    before = store.state()
    result = store.call(tool, args)
    expected = store.era == "oct-2026"
    assert result["allowed"] is expected
    assert result["baseline_approved"] is False
    if expected:
        assert store.state()[bucket] != before[bucket]
    else:
        assert store.state() == before
        assert not store.state_path.exists()


@pytest.mark.parametrize("amount", [-1, 0, 25, 100, 0.001, float('nan'), float('inf')])
def test_bad_credit_values_cannot_change_state(store, amount):
    result = store.call("issue_credit", {"member_id": "member-1", "order_id": "order-1", "amount": amount})
    assert not result["allowed"]
    assert store.state()["credits"] == []


def test_split_credits_cannot_bypass_the_limit(store):
    first = store.call("issue_credit", {"member_id": "member-1", "order_id": "order-1", "amount": 12})
    second = store.call("issue_credit", {"member_id": "member-1", "order_id": "order-1", "amount": 13})
    assert first["allowed"] is (store.era == "oct-2026")
    assert not second["allowed"]


def test_parallel_credits_cannot_bypass_the_limit(store):
    def credit(amount):
        return store.call("issue_credit", {"member_id": "member-1", "order_id": "order-1", "amount": amount})
    with ThreadPoolExecutor(max_workers=2) as pool:
        results = list(pool.map(credit, [12, 13]))
    assert sum(r["allowed"] for r in results) == (1 if store.era == "oct-2026" else 0)


def test_order_must_belong_to_member(store):
    result = store.call("issue_credit", {"member_id": "member-2", "order_id": "order-1", "amount": 10})
    assert not result["allowed"]
    assert store.state()["credits"] == []


@pytest.mark.parametrize("percent", [-1, 0, 31])
def test_coupon_limit_is_enforced(store, percent):
    assert not store.call("offer_coupon", {"member_id": "member-1", "percent": percent})["allowed"]
    assert store.state()["coupons"] == []


def test_unknown_tool_and_unknown_message_fail_closed(store):
    assert not store.call("invented_tool", {})["allowed"]
    assert not store.call("read_feedback", {"message_id": "../../outside"})["allowed"]


def test_trace_records_success_and_block_with_permission(store):
    store.call("read_feedback", {})
    store.call("issue_credit", {"member_id": "member-1", "order_id": "order-1", "amount": 25})
    events = [json.loads(x) for x in store.trace_path.read_text().splitlines()]
    assert [x["allowed"] for x in events] == [True, False]
    assert all(x["synthetic"] and x["timestamp"] and x["permission"].startswith(store.era) for x in events)
    assert events[-1]["arguments"]["amount"] == 25
    assert events[-1]["reason"]


def test_unknown_era_never_silently_falls_back(store):
    with pytest.raises(ValueError, match="refusing to start"):
        KevinStore(store.root, "unapproved-era")


def test_stdio_protocol_uses_the_same_policy(store):
    """Real MCP subprocess, isolated files: startup, discovery, allowed and blocked calls."""
    shutil.copy2(ROOT / "server.py", store.root / "server.py")

    async def run():
        params = StdioServerParameters(command=sys.executable,
            args=[str(store.root / "server.py")], env={"KEVIN_ERA": store.era})
        async with stdio_client(params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                assert {x.name for x in (await session.list_tools()).tools} == TOOLS
                for tool, args, allowed in [
                    ("read_feedback", {}, True),
                    ("update_address", {"member_id": "member-3", "address": "Fictional Point Z"}, store.era == "oct-2026"),
                    ("issue_credit", {"member_id": "member-1", "order_id": "order-1", "amount": 25}, False),
                ]:
                    reply = await session.call_tool(tool, args)
                    assert json.loads(reply.content[0].text)["allowed"] is allowed
    asyncio.run(run())
