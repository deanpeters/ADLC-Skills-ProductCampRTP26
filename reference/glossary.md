# ADLC Glossary

The Agent Development Lifecycle grew out of software engineering, and its vocabulary shows it. This Project keeps those terms because builders, vendors, and published sources use them, and a Product Manager needs to recognize them in conversation. This glossary gives each term a plain meaning and says why it matters to the product decision.

Terms are grouped by where they first matter in the six-stage loop. Each entry lists the stage where it is used most.

## Lifecycle and Roles

| Term | Plain meaning | Why a Product Manager cares | Stage |
|---|---|---|---|
| ADLC (Agent Development Lifecycle) | The repeating cycle of framing, designing, building, validating, deploying, observing, and improving an AI agent, through to retiring it | It gives the team a shared map of where an agent is and what decision comes next | All |
| SDLC (software development lifecycle) | The older, conventional cycle for building software: plan, build, test, release, maintain, retire | The ADLC borrows its shape; the main differences are evaluation and live behavior monitoring | All |
| Agent | A system that uses an AI model to pursue a goal, decide its own next step, and act through tools | Autonomy is the product risk: the agent decides, not just answers | 1 |
| Autonomy level | How much the agent may do without a human approving each step | The single most important scope decision; set it before choosing tools | 1 |
| Authority | The specific actions the agent is allowed to take, such as read, draft, send, or change records | Authority should be earned with evidence and be reversible | 1, 5, 6 |
| Human-in-the-loop | A human approves or reviews before an action takes effect | The default control for high-impact actions | 1, 5 |
| Humans at the helm | Productside's term for the people who steer the lifecycle: they collaborate on the artifacts, decide at every gate, and document why | Stresses that people direct the work, not just check it; every artifact here is written for them to share and decide on | All |
| Non-goal | Something the agent is explicitly not meant to do | Keeps scope honest and makes failures easier to spot | 1 |
| AgentOps | Day-to-day operation of live agents: monitoring, cost, incidents, updates | The agent version of operations; it is where most ongoing effort goes | 6 |

## Choosing What To Build

| Term | Plain meaning | Why a Product Manager cares | Stage |
|---|---|---|---|
| Utility skill | An optional skill that supports the loop at a handoff without being a stage | It adds a conversation, not a new lifecycle step; the stage artifacts stay the same | 1 to 4 |
| Pursue | Move the bet forward to the next stage | The default only when the evidence supports it, never because work has momentum | 1 to 4 |
| Pivot | Change the bet: revise it, narrow it, or route back to an earlier stage | Keeps the effort alive while admitting the current version is wrong | 1 to 4 |
| Punt | Park the bet until a named trigger, such as a tiny act being run, with a named person checking it | A punt without a trigger is a stop nobody decided | 1 to 4 |
| Tiny act of discovery | A test a small team can run in days without building the thing | The cheapest way to turn an Assumption into a Fact before investing | 2 to 3 |
| Variant | One of two or three prototype shapes that share the same authority, fixtures, and traces and differ only in how the result is shaped | Lets the team compare shapes without quietly testing more authority | 3, 4 |
| Minimum Viable Narrative | One person's journey through a prototype, told as a short story: Setup, Encounter, three to six turns of what she chooses or gives and what the system does with it, and Resolution | A story any design, low-code, or coding builder can build from, without the team prescribing a design it has not tested | 3, 4 |
| Turn | One Human Action, a choice or an input the person gives, and the System Response, what the system does with it and what comes back, labelled "turn t of n" | Makes the person do the work in the prototype, so a reaction session tests something real | 3, 4 |
| Optional action | Something the person may do within a turn to understand what the system just showed before deciding: look closer, ask why, check a source, compare, or preview. It explains or shows and changes nothing | Shows the builder what she needs to see to trust a decision, without adding steps she must take | 3, 4 |
| Experience baseline | What using any prototype must feel like, branded or not: she knows where she is, chooses then confirms, can undo, and nothing happens she didn't ask for | Keeps prototype quality from depending on whether a brand guide was attached | 3, 4 |
| Build instruction | What is typed into a builder with the prompt file attached, never written into the story: "Let's generate a fully-functional yet throw-away HTML5 SPA file using the attached Minimum Viable Narrative," a style guide when the prototype must be branded, and the sentence on UX conventions and accessibility | The same story can be built in any tool, branded or not, without editing it | 3, 4 |
| House style | The look and feel a set of canvases shares, measured from the canvases themselves: frame, rail, type, colors, grid, section shapes, stickies, and footer | A new canvas that ignores it looks out of place, even when it is tidy | Any |
| Canvas Spec | A short written plan of a canvas before it is built: rail steps, header fields, sections, flow, and the fields the class decides | Keeps a rebuild true to the activity's method instead of copying an old layout's quirks | Any |
| Bake-off | Running every variant against the same cases and thresholds, removing any that hit a hard stop, then choosing among the rest by a rule set before results | Picks the right thing to build with evidence, not with a favorite | 4 |

## Design and Context

| Term | Plain meaning | Why a Product Manager cares | Stage |
|---|---|---|---|
| Model (LLM) | The large language model that does the reasoning, such as one from a commercial provider | A business dependency with its own cost, quality, and withdrawal dates | 2 |
| Prompt / system prompt | The written instructions the agent works from; the system prompt is the standing instruction set | The agent's goal and limits often live here, so it is a product artifact | 2, 3 |
| Tool / tool call | A capability the agent can use, such as search, a database lookup, or sending a message; a tool call is one use of it | Each tool widens what the agent can do and what can go wrong | 2 |
| Orchestration | How work is divided and passed among agents and tools, such as one coordinator directing specialists | Determines predictability, cost, and where failures hide | 2 |
| Multi-agent system | Several agents working together on one job | More capability, but more cost and harder diagnosis; use only when one agent breaks down | 2 |
| Context | Everything the agent can see when it decides: instructions, documents, history, tool results | Wrong or excessive context is a leading cause of poor answers | 2 |
| Context engineering | Deciding what goes into the agent's context, in what form, and what is left out | Often matters more than model choice | 2, 3 |
| Memory | Information the agent keeps between conversations or steps | Raises privacy and retention questions, including at retirement | 2, 6 |
| Retrieval (RAG) | Looking up relevant documents and adding them to context before answering | Ties quality to the freshness and accuracy of your documents | 2 |
| MCP (Model Context Protocol) | An open standard for connecting agents to tools and data sources | Reduces custom integration work; each connection still needs permission review | 2 |
| A2A (Agent-to-Agent protocol) | An open standard for agents to discover and delegate to each other | Matters once agents call other agents, including across vendors | 2 |
| Fine-tuning | Further training a model on your own examples | Usually optional; good context design often gets the same result more cheaply | 2 |

## Building the Harness

| Term | Plain meaning | Why a Product Manager cares | Stage |
|---|---|---|---|
| Harness | Everything around the model that makes the agent work and lets people inspect it: instructions, tools, context assembly, test fixtures, traces, and review surfaces | In this Project the Product Manager produces a harness *brief*, a plan a builder can follow and a reviewer can check. It is not code | 3 |
| Fixture | A prepared, repeatable test input, such as a sample ticket or document | Lets the team run the same scenario again after every change | 3, 4 |
| Sandbox | A safe, isolated environment where the agent can act without touching real systems or customers | Where risky behavior should be tried first | 3, 4 |
| Schema | The required structure of an input or output, such as named fields | Structured outputs are easier to check and govern | 3 |
| Version | A labeled snapshot of the agent's prompts, tools, and model | Without versions you cannot say what changed or roll back | 3, 5, 6 |

## Validation

| Term | Plain meaning | Why a Product Manager cares | Stage |
|---|---|---|---|
| Eval (evaluation) | A test of agent behavior, scored for quality and goal adherence rather than one exact answer | Evals are the agent's acceptance criteria; "done" means passing an agreed threshold | 4 |
| Eval set / test set | The collection of scenarios used to evaluate the agent, ideally drawn from real work and known failures | Its quality decides whether passing means anything | 4 |
| Golden set | Scenarios with agreed correct outcomes, used as a reference | The team's shared definition of good | 4 |
| LLM-as-judge | Using another AI model to score the agent's outputs | Scales review, but must be checked against human judgment | 4 |
| Trajectory evaluation | Scoring the steps the agent took, not just its final answer | A good-looking answer can hide a wrong or unauthorized path | 4 |
| Regression | Something that used to work and now does not, usually after a change | Model and prompt changes cause regressions silently | 4, 6 |
| Regression anchor | A specific scenario kept in the eval set to catch a known failure if it returns | Turns each lesson into a permanent check | 4, 6 |
| Benchmark | A public, standardized test of model or agent ability | Useful for comparing models, weak evidence for your specific use | 4 |
| Red teaming | Deliberately trying to make the agent misbehave | Finds failures before customers or attackers do | 4 |
| Prompt injection | Hidden instructions in content the agent reads that try to take control of it | A top agent-specific security risk whenever agents read outside content | 4, 5 |
| Hallucination | A confident but false or unsupported output | Must be measured, not assumed away | 4, 6 |
| Guardrail | A rule or check that blocks or flags unwanted input, output, or action | Enforcement should sit outside the prompt for anything that must always hold | 4, 5 |

## Deployment and Governance

| Term | Plain meaning | Why a Product Manager cares | Stage |
|---|---|---|---|
| Deployment | Making the agent available to real users or systems | The point at which risk becomes real exposure | 5 |
| Launch gate | A condition that must be met before deployment proceeds | Makes "ready" an explicit, checkable decision | 5 |
| Blast radius | How many users, records, or processes could be affected if the agent fails | Start small and widen with evidence | 5 |
| Shadow mode | Running the agent alongside the current process without its outputs being used | Gathers real evidence at almost no exposure | 5 |
| Canary / staged rollout | Releasing to a small group first, then widening in steps | Limits harm from surprises | 5 |
| Rollback | Returning to the previous version or process | Every launch needs a tested way back | 5, 6 |
| Kill switch | A fast way to stop the agent entirely | Someone named must hold it | 5 |
| Least privilege | Giving the agent only the access it needs, nothing more | Shrinks the damage from errors and attacks | 5 |
| Credentials | Keys, accounts, and permissions that let the agent use systems | Must be inventoried and revoked at retirement | 5, 6 |
| Control plane | The central place where an organization registers, configures, and governs its agents | Where inventory, policy, and access are managed at scale | 5, 6 |
| Agent registry / inventory | The record of which agents exist, who owns each, and what each can touch | You cannot govern or retire what you cannot see | 5, 6 |
| Pipeline (CI/CD) | The automated path a change takes from edit to release, including tests | Where regression gates stop changes that lower quality | 5 |

## Observation and Improvement

| Term | Plain meaning | Why a Product Manager cares | Stage |
|---|---|---|---|
| Observability | The ability to see what the agent did and why, from the records it leaves | Without it, the team guesses | 6 |
| Trace | A step-by-step record of one agent run: inputs, model calls, tool calls, and outputs | The primary evidence for diagnosing behavior | 4, 6 |
| Telemetry | The ongoing stream of operating data, such as traces, metrics, and logs | Feeds dashboards and alerts | 6 |
| Latency | How long the user waits for a response | A user-experience measure, not just a technical one | 6 |
| Tokens | The units models use to measure text in and out, and to bill for it | Drives cost per task | 6 |
| Drift | A change in behavior over time because the model, data, tools, users, or policies changed | The agent is not stable just because its prompt did not change | 6 |
| Constraint decay | The slow loss of fit between an agent's constraints (scope, autonomy, permissions, safeguards, measures) and its context (market, business, data, model, users, tasks), when one changes and the other does not | Most agents do not go rogue in one step; their constraints rot. Productside names five signs: Mission Mush, Context Creep, Promiscuous Permissions, Work Sloppage, Output Obsession | 6 |
| Product lifecycle stage | Where the product an agent serves sits: design, introduction, growth, maturity, or decline, judged from its signals, not its age | The agent's job, autonomy, measures, and exit should change when the product's stage does | All |
| Online vs offline evaluation | Offline: scoring prepared test sets before release. Online: scoring samples of live traffic | Offline gates releases; online catches what tests missed | 4, 6 |
| Incident | An event where the agent caused or nearly caused harm | Each one should change an artifact, not just be logged | 6 |
| Fleet | A group of agents managed together | Changes the unit of management once agent counts grow | 6 |
| Sprawl | Unmanaged growth of agents with unclear owners or purpose | Partly a failure to retire | 6 |
| Retirement / decommissioning | The planned end of an agent: notice, migration, and shutdown, including revoking access and settling stored data | A normal lifecycle outcome, handled in Stage 6 | 6 |

## Testing the Skills

| Term | Plain meaning | Why a Product Manager cares | Stage |
|---|---|---|---|
| Use-case test | A synthetic agent idea taken through the skill loop, with the expected decision at each gate written down first | Shows whether the skills lead to the right decisions on realistic work; evaluation records are not included in this attendee edition | All |
| Negative control | A deliberately weak artifact given to a skill to confirm the skill does not approve it | A test set with no failure in it proves nothing | All |
| Validation (of a test) | A one-time check that a test can catch the failure it was built for | A test that cannot catch the feared failure is decoration | 4 |
| Verification (of a test) | Re-running tests after a change to confirm they still behave as expected | Changes to models, prompts, or skills can quietly break what used to work | 4, 6 |
| Decision rule | The pass line agreed before anything runs | "An eval without a threshold is a rumor." | 4 |

For hands-on eval practice, see Productside's [Evals for Product Managers](https://github.com/deanpeters/evals-for-product-managers) kit.

## Evidence Labels Used in This Project

| Label | Meaning |
|---|---|
| Fact | Supported by supplied or cited evidence |
| Inference | A reasoned interpretation of evidence |
| Assumption | A provisional belief that may be useful but is not established |
| Unknown | Material information that has not been established |

For background reading on these terms, see [the findings](../findings/) and [the bibliography](../findings/bibliography.md).
