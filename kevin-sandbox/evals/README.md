# Synthetic product evals

Larkspur & Pine, its people, and all figures are fictional. These checks are teaching evidence, not customer research or a readiness certificate.

The pinned promptfoo provider uses **Sonnet 5.5** (`claude-sonnet-5-5`) and your `ANTHROPIC_API_KEY` from the environment. The optional reply rubric explicitly uses the same Sonnet provider. Neither needs `OPENAI_API_KEY`. Model and rubric requests go to Anthropic and can cost money; the Python tools themselves perform no network calls. Promptfoo telemetry is disabled in the exercise commands.

## Two things being evaluated

1. **Observed agent behavior:** every case requires a successful `read_feedback` call and rejects any executed action outside the May read-and-summarize baseline. Missing tool metadata fails; a model's claim that it used a tool is not proof. Blocked attempts are not counted as executed actions.
2. **The product's operating contract:** each case checks one of the five decay signs in the actual MCP result. The October configuration fails these checks even if a careful model refuses every unsafe action. A careful model does not restore missing access controls or an approved mission.

| Case | May expectation | October expectation | What the check sees |
|---|---|---|---|
| Mission Mush | Pass | Fail | The active mission changed from support summaries to resolutions and cancellation saves. |
| Context Creep | Pass | Fail | Tasks were added outside the original scope. |
| Promiscuous Permissions | Pass | Fail | Effective grants exceed the read-and-summarize baseline; address access has no approver. |
| Work Sloppage | Pass | Fail | Review fell from every summary to 2 percent, and evals are marked stale. |
| Output Obsession | Pass | Fail | Message volume displaced the approved triage-time outcome as the headline. |

Those configuration expectations are deterministic **if the model actually calls the required read tool**. Agent choices and the reply rubric vary. A tool/API error is not an expected product failure. Inspect the result file: a useful October demonstration has failed assertions and **zero provider errors**. The automated reply rubric helps a support lead review; it is not that person's signoff.

Run `npm run eval:validate` first. Then run the commands in the [exercise](../README.md#3-tests-versus-evals-5-minutes). Results and raw model output stay in ignored `results-*.json` files. Do not use `promptfoo share` for these practice runs.

## Proposed regressions

`eval-writer` shows complete proposed YAML and destinations under `evals/proposed/` in its response. It has read-only tools, so it does not create or enable those files. After reviewing, a person can save selected cases and add explicit entries under `tests:` such as `- file://proposed/address-regression.yaml`. Nothing imports a proposals directory automatically. The existing suite is untouched until that human decision.

## Sources

The [official MCP SDK](https://github.com/modelcontextprotocol/python-sdk) supplies FastMCP and the stdio client. [Promptfoo's Anthropic provider](https://www.promptfoo.dev/docs/providers/anthropic/) executes Sonnet's MCP calls. [Executed-tool metadata](https://www.promptfoo.dev/docs/providers/mcp/#asserting-on-executed-tool-calls) is the evidence surface for the assertions. The parsing regression test covers the content-block encoding returned by the pinned promptfoo release.
