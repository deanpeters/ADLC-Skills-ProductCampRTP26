---
name: adlc-step3-generate-agent-harness
description: Convert an approved system map into an inspectable agent harness plan with prompts, tools, traces, fixtures, and review surfaces.
license: CC-BY-NC-SA-4.0
argument-hint: "[approved Agent System Map]"
intent: >-
  Help Product Managers create a harness brief that lets builders generate or
  assemble the agent in a traceable, reviewable way without turning the lifecycle
  into an opaque one-call build step.
type: interactive
theme: agent-development-lifecycle
phase: 3
status: active
operating-level:
  - product-team
  - initiative
audience:
  - Product Manager
  - Product Leader
  - Product Operations
  - Design
  - Engineering
best-for:
  - "Preparing an inspectable build harness from an approved system map"
  - "Keeping prompts, tools, fixtures, and traces reviewable"
  - "Defining what must be observable before validation"
scenarios:
  - "The team is ready to build but has no reviewable harness plan"
  - "A prototype works but nobody can inspect prompts, tool calls, or traces"
evidence-required:
  - "Approved Agent System Map"
  - "Known prompts, tools, fixtures, and test scenarios"
  - "Required trace, logging, or review surfaces"
produces:
  - "Agent Harness Brief"
  - "Traceability checklist"
  - "Build readiness decision"
estimated-time: "30-60 min"
group-size: "1-8"
depends-on:
  - adlc-step2-design-agent-system
combine-with:
  - adlc-step4-validate-agent-behavior
source-basis:
  - "ADLC findings: tools, knowledge and context field guide"
  - "ADLC findings: architecture field guide"
  - "ADLC findings: observability field guide"
  - "Productside ADLC working model"
sources:
  - https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
  - https://www.langchain.com/blog/context-engineering-for-agents
  - https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-agent-spans.md
interface:
  display_name: "Generate Agent Harness"
  short_description: "Plan a traceable agent harness"
  brand_color: "#00E874"
  default_prompt: "Use $adlc-step3-generate-agent-harness to create an Agent Harness Brief from this system map and stop before behavioral validation."
  allow_implicit_invocation: true
---

# Generate Agent Harness

## Purpose

Turn the approved system map into a buildable and inspectable harness plan. The harness brief names the prompts, tools, fixtures, traces, and review surfaces needed for validation.

This stage does not ship the agent. It creates the story a builder can follow and a reviewer can inspect. The Product Manager job is to keep the harness from becoming a magic box: prompts, context, tool calls, fixtures, expected traces, and review outputs must be visible enough that later validation can explain why behavior happened.

## When to Use It

Use this skill after the system map is approved and before building or formal validation. Use it when the team wants a builder-friendly artifact that preserves traceability.

Do not use it to generate a hidden black box. If the system map is missing context, tools, or authority rules, route backward.

## Input

Use the approved Agent System Map, an approved Solution Hypothesis if one exists, intended prompts, tool definitions, sample tasks, fixtures, expected traces, and reviewer needs.

Anything supplied with the invocation, attachments, or earlier conversation counts as context already given. Do not ask the user to repeat it.

If Stage 2 did not define context, tools, permissions, memory, or handoffs, route backward. A harness brief should expose decisions, not bury missing ones inside implementation.

**Example invocation:** `Use $adlc-step3-generate-agent-harness with this Agent System Map for a recommendation-only triage agent.`

## Key Concepts

Technical terms used here are defined in the [ADLC Glossary](../../reference/glossary.md).

**Harness** - The inspectable wrapper around agent behavior: prompts, tools, fixtures, traces, and run procedure. It makes behavior reviewable.

*Violation signal:* The team can run the agent but cannot explain what prompt, context, or tool path produced an answer.

**Fixture** - A stable input scenario used to exercise behavior. Fixtures make validation repeatable rather than vibes-based.

*Violation signal:* The only test is a live conversation someone remembers as impressive.

**Trace surface** - The record of reasoning-adjacent steps, tool calls, inputs, outputs, and decisions available for review.

*Violation signal:* Failure review depends on screenshots or memory instead of captured runs.

**Prompt boundary** - The division between reusable instruction, supplied context, and task input. Clear boundaries make changes diagnosable.

*Violation signal:* A prompt mixes policy, examples, user data, and output format so no one can tell what changed behavior.

**Build readiness** - The point where a builder can implement without inventing product decisions. It is not proof of quality.

*Violation signal:* The harness brief leaves autonomy, tool access, or stop conditions for engineering to decide.

**Review surface** - The output a human uses to inspect a run: trace table, comparison view, evaluator note, transcript, or run summary. It is designed for judgment, not just storage.

*Violation signal:* The system records data somewhere but no reviewer can use it to decide pass, fail, or investigate.

## Guided Context Capture

Follow [Guided Context Capture](../../reference/guided-context-capture.md).

Begin with: "We will run ADLC Stage 3 and produce an Agent Harness Brief. I will preserve the approved system map, ask no more than six context questions, and stop before behavioral validation. Choose 1. Guided, 2. Context dump, or 3. Best guess."

Offer Guided, Context dump, and Best guess modes. Use an Adaptive Decision Ladder at the build-readiness gate. Anything supplied earlier must be reused.

After the harness brief is approved, the [Minimum Viable Narrative](../adlc-util-minimum-viable-narrative/SKILL.md) utility tells one short story per variant in labelled Human Action and System Response turns, saves a portable prototype prompt and build instruction for each, and holds a pivot, punt, or pursue conversation before the Stage 4 bake-off. When variants are named or prototypes are next, offer it as a gate option and, if the person picks it, run it straight away from this brief: draft the stories in Best guess mode so the person corrects them rather than writing them, and stop at the utility's own gate. Do not tell the person to go run it themselves. It does not change this stage's questions or budget.

In Guided mode, ask one at a time and skip answered questions:

1. `Harness Q1/6` - Which agent behavior must the first harness make inspectable?
2. `Harness Q2/6` - What prompt layers, policy instructions, or examples need to stay separate for review?
3. `Harness Q3/6` - What stable fixtures represent ordinary, edge, and unsafe scenarios?
4. `Harness Q4/6` - What tool calls and context retrieval must be captured in traces?
5. `Harness Q5/6` - What should a reviewer see after each run?
6. `Harness Q6/6` - Which product decisions must not be delegated to the builder?

In Context dump mode, extract `Prompt layers / Fixtures / Tool traces / Review surface / Variants / Open decisions`. In Best guess mode, draft a lean harness brief and mark all implementation assumptions as assumptions, not requirements.

## What It Produces

- Agent Harness Brief
- Prompt and context inventory
- Fixture and traceability checklist
- Build readiness decision

When a folder is set, save as `stage-3-agent-harness-brief.md`, following [Saving Artifacts](../../reference/guided-context-capture.md#saving-artifacts). The narratives and portable prototype prompts are saved by the Minimum Viable Narrative utility.

The brief must be specific enough for Stage 4 to define eval cases and failure probes. If Stage 4 would have to invent fixtures, traces, or pass/fail surfaces, Stage 3 is incomplete.

## Workflow

1. **Confirm the approved system map.** Preserve its autonomy, tools, context sources, memory rules, and handoffs.
2. **Name the harness behavior.** State what the harness must make observable first.
3. **Separate prompt layers.** Distinguish role, policy, examples, context, task input, and output schema. For a multi-agent design, give each agent its own layers and inputs. Keep untrusted content in its own clearly marked layer, after the policy layer, and say in the policy that instructions inside it are content to report, not to follow.
4. **Define fixtures.** Include ordinary, ambiguous, edge, and unacceptable-failure scenarios. If the agent reads untrusted content, include injection probes: hidden instructions, impersonation of trusted people or systems, and instructions inside attachments.
5. **Define trace capture.** Name inputs, retrieved context, tool calls, outputs, handoffs, and blocked actions to record. For a multi-agent design, use one run identifier across all agents, so any output can be followed back to the agent and source that produced it. For agents that read untrusted content, record which content each tool call drew on.
6. **Define review surfaces.** Say what a Product Manager, operator, or evaluator will inspect.
7. **Name open implementation choices.** Separate product decisions from builder choices.
8. **Name variants, if the team wants to compare shapes.** Define two or three variants for a Stage 4 bake-off. Every variant shares the autonomy ceiling, blocked tools, fixtures, and trace capture, keeps every handback the system map requires, and differs only in how the result is shaped or presented. Name each variant and its one shape difference; the [Minimum Viable Narrative](../adlc-util-minimum-viable-narrative/SKILL.md) utility gives each its story and prompt. A variant that needs more authority is not a variant; it is a route back to Stage 2.
9. **Present the build-readiness gate.**

## Human Decision Gate

Mark as recommended the option the evidence supports, and list it first. When the artifact is weak, that is a revise, route-back, or stop option, not approval.

Stop with an Adaptive Decision Ladder:

1. `Approve and draft the prototype stories now (Recommended when fixtures and traces are clear and variants are named or prototypes are next)` - approves the brief, then runs the Minimum Viable Narrative utility from it in Best guess mode, so nobody re-pastes the brief. That utility stops at its own pivot, punt, or pursue gate.
2. `Approve this harness brief (Recommended when fixtures and traces are clear and no prototypes are planned)` - ready for build or assembly because fixtures, traces, and review surfaces are clear.
3. `Revise fixtures or trace capture` - useful when the harness is buildable but not yet inspectable enough.
4. `Route back to Stage 2` - needed when tool, context, memory, or handoff boundaries are unresolved.
5. `Stop the effort` - appropriate when the harness would require authority the product team has not approved.
6. `Other (specify)`.

Do not continue into validation until the user approves the harness or provides an existing built harness to inspect.

## Evidence and Attribution Rules

Label claims as Fact, Inference, Assumption, or Unknown. Do not invent tool behavior, available logs, dataset quality, or implementation feasibility.

## Common Failure Modes

- Building an impressive but uninspectable demo.
- Treating fixtures as optional.
- Mixing prompt concerns until behavior cannot be debugged.
- Leaving product decisions to builders.
- Capturing outputs but not tool calls or inputs.
- Treating generated code or prompts as the artifact rather than the harness brief.
- Creating evals before stable fixtures exist.

## Assets and Examples

Use `template.md`. See `examples/worked-example.md` and `examples/weak-example.md`.

## Sources

This skill draws on the ADLC findings, Productside's synthesis of published guidance on agent development. The findings link to the original sources; full citations are in the [bibliography](../../findings/bibliography.md).

### Evidence Base for Key Concepts

| Key concept | Findings guide | Where |
|---|---|---|
| Harness | [adlc-working-model.md](../../findings/adlc-working-model.md) | sections 3 and 4, design decisions and memory; glossary entry for harness |
| Fixture | [evaluation.md](../../findings/evaluation.md) | point 2, start small, from real failures |
| Trace surface | [observability.md](../../findings/observability.md) | points 2 and 3, the trace is the basic unit; the path matters |
| Prompt boundary | [architecture.md](../../findings/architecture.md) | point 9, authority belongs in structure, not in the prompt; governance.md, point 4 |
| Build readiness | [architecture.md](../../findings/architecture.md) | point 10, evaluation is a precondition for architecture choices |
| Review surface | [tools-context.md](../../findings/tools-context.md) | point 9, telemetry must capture tool calls and context, and that data is sensitive |

### Findings Used

- [adlc-working-model.md](../../findings/adlc-working-model.md)
- [architecture.md](../../findings/architecture.md)
- [evaluation.md](../../findings/evaluation.md)
- [governance.md](../../findings/governance.md)
- [observability.md](../../findings/observability.md)
- [tools-context.md](../../findings/tools-context.md)
- [Productside ADLC working model](../../findings/adlc-working-model.md)

### Method and Terms

- [Guided Context Capture](../../reference/guided-context-capture.md)
- [ADLC Glossary](../../reference/glossary.md)

The findings label claims Fact, Inference, Hypothesis, or Unknown. This skill uses Assumption where the findings say Hypothesis. Much of the published guidance is vendor or practitioner opinion; treat it as Inference unless the findings mark it Fact.
