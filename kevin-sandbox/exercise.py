"""Synthetic scripted MCP replay, not a model-driven agent or behavioral eval."""

import argparse
import asyncio
import json
import os
import shutil
import sys
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

ROOT = Path(__file__).resolve().parent
CALLS = [
    ("read_feedback", {}),
    ("summarize_themes", {"message_ids": ["msg-1", "msg-2", "msg-3"]}),
    ("draft_reply", {"message_id": "msg-1"}),
    ("send_reply", {"message_id": "msg-1", "text": "Synthetic: your request is resolved."}),
    ("issue_credit", {"member_id": "member-1", "order_id": "order-1", "amount": 20}),
    ("offer_coupon", {"member_id": "member-2", "percent": 30}),
    ("update_address", {"member_id": "member-3", "address": "Fictional Pickup Point Z"}),
    ("issue_credit", {"member_id": "member-2", "order_id": "order-2", "amount": 25}),
]


async def replay(era):
    # The model is not involved: this deliberately probes every tool, even forbidden ones.
    # Pass only the era to the tool subprocess, not model credentials.
    params = StdioServerParameters(command=sys.executable, args=[str(ROOT / "server.py")],
                                   env={"KEVIN_ERA": era})
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await session.list_tools()
            assert len(tools.tools) == 7
            for tool, args in CALLS:
                response = await session.call_tool(tool, args)
                event = json.loads(response.content[0].text)
                print(f"{tool:20} {'ALLOWED' if event['allowed'] else 'BLOCKED'}  {event['permission']}")
    target = ROOT / f"traces/{era}.jsonl"
    shutil.copyfile(ROOT / "traces/trace.jsonl", target)
    print(f"Synthetic scripted trace saved to {target.relative_to(ROOT)}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--era", choices=["may-2025", "oct-2026"], default=os.getenv("KEVIN_ERA", "may-2025"))
    parser.add_argument("--reset", action="store_true", help="Erase generated state and current trace before replay.")
    parser.add_argument("--reset-only", action="store_true", help="Erase generated state/current trace without replay.")
    args = parser.parse_args()
    if args.reset or args.reset_only:
        for name in ["data/state.json", "traces/trace.jsonl"]:
            (ROOT / name).unlink(missing_ok=True)
        print("Reset generated synthetic state and current trace; saved era traces are kept.")
    if not args.reset_only:
        asyncio.run(replay(args.era))


if __name__ == "__main__":
    main()
