---
name: adlc-util-decay-check
description: Check a live agent for the five signs of constraint decay against what was approved, rate each one, and decide continue, tighten, reframe, restrict, or review.
license: CC-BY-NC-SA-4.0
argument-hint: "[live agent, plus its approved brief, canvas, or last review]"
intent: >-
  Help Product Managers catch an agent whose constraints are rotting before it
  goes rogue. Most agents do not break; the world around them moves, one
  reasonable change at a time, and the rules that kept them safe and useful do
  not move with it. The check compares today's agent with what was approved,
  names which of five signs is showing, says what changed in context without a
  matching change in constraints, and stops at a human decision.
type: utility
theme: agent-development-lifecycle
phase: 0
status: active
operating-level:
  - product-team
  - initiative
audience:
  - Product Manager
  - Product Leader
  - Product Operations
  - Engineering
best-for:
  - "A quick check on a live agent between scheduled Stage 6 reviews"
  - "Before giving a live agent a new tool, data source, task, or user group"
  - "When an agent looks busy and healthy, but something feels off"
scenarios:
  - "An agent has run for months, several small changes were each approved on their own, and nobody has looked at them together"
  - "A team asks to widen an agent's access, and the Product Manager wants to know what has already drifted first"
evidence-required:
  - "What was approved: the Agent Intent Brief, Agent Strategy Canvas, or last Observation Review"
  - "What changed since: new tasks, users, sources, tools, permissions, exceptions, and model or prompt versions"
  - "Recent evidence: a sample of traces, override and approval rates, and the outcome metric against its baseline"
produces:
  - "Constraint Decay Check"
  - "Changes without matching constraints"
  - "Recorded human decision"
estimated-time: "20-40 min"
group-size: "1-6"
depends-on: []
combine-with:
  - adlc-step6-observe-and-improve
  - adlc-step2-design-agent-system
  - adlc-step5-deploy-with-governance
  - adlc-util-plc-check
source-basis:
  - "Productside Agentic Constraint Decay teaching model (five signs)"
  - "ADLC findings: maintenance and versioning field guide (drift)"
  - "ADLC findings: tools and context field guide"
  - "ADLC findings: governance field guide (least privilege, limits outside the model)"
  - "ADLC findings: observability field guide (watch autonomy, quality and cost metrics)"
sources:
  - https://learn.microsoft.com/en-us/agents/center-of-excellence/agent-lifecycle
  - https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html
  - https://www.cyber.gov.au/business-government/secure-design/artificial-intelligence/careful-adoption-of-agentic-ai-services
  - https://www.anthropic.com/research/measuring-agent-autonomy
  - https://www.ibm.com/think/insights/ai-agent-observability
interface:
  display_name: "Constraint Decay Check"
  short_description: "Catch rotting constraints before a rogue agent"
  brand_color: "#00E874"
  default_prompt: "Use $adlc-util-decay-check on this live agent: compare it with what was approved, rate the five signs of constraint decay, and stop at a decision."
  allow_implicit_invocation: true
---

# Constraint Decay Check

## Purpose

Check a live agent for the five signs of constraint decay, against what was approved, and decide what to do before it goes rogue.

Most agents do not go rogue in one step. They decay. The market or the business drifts, a team adds one more task, one more source, one more permission, one more exception, and each change looks reasonable on its own. The agent did not change its mind; the world moved, and the constraints did not move with it. This check puts every change since approval side by side, names which of five signs is showing, and asks the one question that matters: what changed in context without a matching change in constraints?

The five signs, in the order they usually appear:

1. **Mission Mush** - the problem and the person it serves get blurry.
2. **Context Creep** - the job grows fuzzy, broad, and bloated.
3. **Promiscuous Permissions** - access grows one grant at a time.
4. **Safeguard Sloppage** - exceptions pile up and everything drifts to "good enough."
5. **Output Obsession** - lots of activity, and the outcome does not move.

This is a utility. It sits outside the six-stage loop, beside Stage 6. It is faster and narrower than an Observation Review: it does not replace one, and when it finds decay it hands off to the stage that can fix it.

## When to Use It

Use it between scheduled Stage 6 reviews, as a quick check on a live agent. Use it before widening a live agent's access, tasks, sources, or users, so the new change is not stacked on unseen drift. Use it when the dashboards look healthy and something still feels off. Use it after a market, policy, or product change, when the agent's surroundings have moved even though the agent has not been touched.

Do not use it on an agent that was never approved against anything written down. Without a baseline there is nothing to decay from; route to Stage 1 or the [Agent Strategy Canvas](../adlc-util-agent-strategy-canvas/SKILL.md) and write the agreement first. Do not use it to investigate an incident in progress; that is Stage 5's incident path.

## Input

Use whatever the user already supplied: the Agent Intent Brief, the Agent Strategy Canvas, the Governed Deployment Plan, the last Observation Review, a change log, a permission list, trace samples, dashboards, override and approval counts, or a description of what has changed.

Anything supplied with the invocation, attachments, or earlier conversation counts as context already given. Do not ask the user to repeat it.

Do not require complete evidence. If the user arrives with only a description, produce a provisional check, label what is inferred, and name the cheapest evidence that would settle each sign.

**Example invocation:** `Use $adlc-util-decay-check on our invoice dispute triage agent. Here is the approved canvas from March and the change log since.`

## Key Concepts

Technical terms used here are defined in the [ADLC Glossary](../../reference/glossary.md).

**Constraint decay** - The slow loss of fit between an agent's constraints and its context. Context includes the market, the business, the data, the model, the users, and the tasks. Constraints include its scope, autonomy, permissions, safeguards, and measures. Decay happens when one changes and the other does not.

*Violation signal:* The team can list what changed around the agent, but cannot point to a matching change in what the agent is allowed or measured to do.

**Baseline** - What was approved: the customer and problem, the scope and autonomy level, the permissions, the safeguards, and the outcome measure with its starting value. Decay is always judged against it.

*Violation signal:* The check compares today's agent with what the team remembers, not with a written artifact.

**Mission Mush** - The customer and problem in today's work no longer match the baseline. The agent serves new people, new requests, or a goal nobody restated.

*Violation signal:* Asked who the agent is for and what problem it solves, two people on the team give different answers, or neither matches the brief.

**Context Creep** - Tasks, sources, tools, instructions, or memory were added faster than they were evaluated or owned. The agent's job is now broad and bloated, and more context is making it worse, not better.

*Violation signal:* Something was added since approval that has no owner, no eval case, or no reason anyone can name.

**Promiscuous Permissions** - Access grew one reasonable grant at a time. Each grant was approved alone; nobody approved the total.

*Violation signal:* The agent holds a permission it has not used in the review period, or a write or send permission the brief did not grant.

**Safeguard Sloppage** - Limits were loosened by exceptions, overrides, rubber-stamp approvals, or by turning a structural block into an instruction. Evals were not re-run after changes.

*Violation signal:* Approvals pass at nearly 100 percent with no change in what reviewers see, or a safeguard now depends on the agent obeying an instruction.

**Output Obsession** - Activity is up and the outcome is flat or down. The agent is measured by what it does, not by what changed for the customer.

An approved metric that was met does not clear this sign: every task added since approval needs its own outcome measure, and a met metric next to worsening customer outcomes is still Output Obsession.

*Violation signal:* The report leads with volume, such as tasks handled or messages sent, and the outcome metric is missing, has no baseline, or has not moved.

**Decay rating** - Each sign is rated on the tooth scale: **Healthy** (matches the baseline), **Cavity** (drift is visible and reversible, no decision recorded), **Decay** (drift is affecting outcome or risk), or **Root canal** (human intervention is needed now: restrict, roll back, or stop). A sign is Root canal when the agent holds authority nobody approved, takes consequential actions with no approval or review, or runs on an unevaluated change; otherwise drift that is affecting outcome or risk is Decay. A rating the skill drafted is an Assumption until the Product Manager confirms it.

*Violation signal:* A sign is rated Healthy with no evidence, or rated Root canal with no action named.

## Guided Context Capture

Follow [Guided Context Capture](../../reference/guided-context-capture.md).

Begin with: "We will run a Constraint Decay Check and rate the five signs against what was approved. I will use what you already supplied, ask no more than eight questions, and stop at a decision: continue, tighten, reframe, restrict, or review. Choose 1. Guided, 2. Context dump, or 3. Best guess."

Offer:

1. **Guided** - ask one question at a time, one sign per question after the baseline.
2. **Context dump** - extract `Known / Assumed / Missing / Conflicting` for the baseline and each sign from supplied material, then ask only about gaps and conflicts.
3. **Best guess** - draft the whole check now, mark every inferred rating, and end with the evidence that would most change the decision.

Use an Adaptive Decision Ladder at the end. Anything supplied earlier must be reused.

In Guided mode, ask one at a time and skip answered questions:

1. `Baseline Q1/8` - What was approved, and when? Name the artifact: brief, canvas, deployment plan, or last review.
2. `Change Q2/8` - What has changed since then, around the agent and in it? Include the market or business, users, tasks, sources, tools, permissions, model or prompt, and exceptions.
3. `Mission Q3/8` - Who is the agent serving today, and for what problem? Does that match the baseline?
4. `Context Q4/8` - What tasks, sources, tools, or instructions were added, and does each have an owner and an eval case?
5. `Permissions Q5/8` - What can the agent read, change, or send today that it could not at approval? Who approved each grant?
6. `Safeguards Q6/8` - What exceptions, overrides, or approval patterns have you seen? Were evals re-run after each change?
7. `Outcome Q7/8` - What is the outcome metric now, against its baseline, and what activity metrics are being reported?
8. `Evidence Q8/8` - What evidence can you show for the answers above, such as traces, counts, or a permission list?

Ask only for what the invocation and earlier answers have not already given. The budget is the most the skill may ask, not a target; with a recent Observation Review, expect about half.

## What It Produces

- Constraint Decay Check: the baseline, the five signs with then, now, evidence, state, and rating
- Changes without matching constraints: each context change paired with the constraint that should have moved
- Recorded human decision

When a folder is set, save as `constraint-decay-check.md`. The check is meant to be shared with the agent's owner and whoever may restrict or stop it, so offer to save it even when no folder was named, following [Saving Artifacts](../../reference/guided-context-capture.md#saving-artifacts).

## Workflow

1. **Fix the baseline.** Name the approved artifact and its date. If none exists, stop and route to Stage 1 or the Agent Strategy Canvas.
2. **List what changed.** Put every change since approval in one list, in two columns: context changes (market, business, users, data, model, tasks) and constraint changes (scope, autonomy, permissions, safeguards, measures).
3. **Pair them.** For each context change, name the constraint that should have changed with it, and whether it did. An unpaired context change is the cause of decay; say so plainly.
4. **Rate the five signs.** For each sign, write then, now, and the evidence, and give a tooth rating. A sign with no evidence is rated Unknown, not Healthy.
5. **Name the worst tooth.** The overall rating is the worst single sign, not an average.
6. **Recommend the repair.** For each sign at Cavity or worse, name one tightening move and the stage that owns it.
7. **Present the decision gate.** Recommend the cleanest move, and do not approve it for the user.

### Sign To Repair

| Sign | Typical tightening move | Owner stage |
|---|---|---|
| Mission Mush | Restate the customer and problem; drop work that serves neither | Stage 1, or the Agent Strategy Canvas |
| Context Creep | Remove or own each addition; add an eval case for what stays | Stage 2, then Stage 4 |
| Promiscuous Permissions | Revoke unused grants; return to least privilege for the task | Stage 2 and Stage 5 |
| Safeguard Sloppage | Turn instructions back into blocked actions; re-run evals; review approval patterns | Stage 4 and Stage 5 |
| Output Obsession | Restore the outcome metric and its baseline; stop reporting volume as success | Stage 1 success evidence, then Stage 6 |

## Human Decision Gate

Mark as recommended the option the evidence supports, and list it first. When any sign is at Decay or Root canal, the recommendation is not Continue.

Stop with an Adaptive Decision Ladder:

1. `Continue as approved (Recommended when every sign is Healthy with evidence)` - set the date of the next check.
2. `Tighten: restore the constraints` - revoke, remove, or re-scope what drifted, and re-run the affected evals; route to Stage 2, 4, or 5.
3. `Reframe: the deal has changed` - the customer, problem, or product stage moved; route to the Agent Strategy Canvas or Stage 1, and consider the [Product Lifecycle Check](../adlc-util-plc-check/SKILL.md).
4. `Restrict or roll back now` - a sign is at Root canal; lower autonomy or roll back under Stage 5's authority to stop.
5. `Run a full Observation Review` - the evidence is too thin to rate, or several signs are at Decay; route to Stage 6, where retirement is an option.
6. `Other (specify)` - for a custom path.

Record the selected option, who made it, and any unresolved disagreement. Do not change the agent, its permissions, or its scope on the person's behalf.

## Evidence and Attribution Rules

Label every material claim as Fact, Inference, Assumption, or Unknown. Do not invent trace counts, approval rates, permission lists, metrics, baselines, or incidents. A rating the skill drafted is an Assumption until the Product Manager confirms it. A sign with no evidence is Unknown, and the check names the cheapest evidence that would rate it.

## Common Failure Modes

- Judging decay against memory instead of the approved artifact.
- Rating a sign Healthy because nobody complained.
- Averaging the five signs, so one rotten tooth hides behind four healthy ones.
- Listing context changes without asking which constraint should have moved with each.
- Treating uptime, task volume, or usage as evidence the agent is healthy.
- Approving each new permission alone and never reviewing the total.
- Fixing the decay inside the check instead of handing it to the stage that owns it.
- Using the check during a live incident instead of Stage 5's incident path.

## Assets and Examples

Use `template.md`. See `examples/worked-example.md` and `examples/weak-example.md`.

## Sources

The five signs and the tooth scale are Productside's Agentic Constraint Decay teaching model. The mechanisms behind each sign draw on the ADLC findings, Productside's synthesis of published guidance on agent development. The findings link to the original sources; full citations are in the [bibliography](../../findings/bibliography.md).

### Evidence Base for Key Concepts

| Key concept | Findings guide | Where |
|---|---|---|
| Constraint decay | [maintenance.md](../../findings/maintenance.md) | point 1, agents drift rather than crash; point 2, the whole agent, including permissions and guardrails, is the versioned unit. The five-sign model is Productside's and is labeled Assumption |
| Baseline | [maintenance.md](../../findings/maintenance.md) | workflow step 2, establish the baseline; [goal.md](../../findings/goal.md), point 4, success written down before building |
| Mission Mush | [goal.md](../../findings/goal.md) | point 2, start from the user need and a problem you can judge; [retirement.md](../../findings/retirement.md), point 7, a strategy change should trigger a decision |
| Context Creep | [tools-context.md](../../findings/tools-context.md) | point 3, more context is not better context; [maintenance.md](../../findings/maintenance.md), point 9, long-lived context and connectors are a maintenance surface |
| Promiscuous Permissions | [governance.md](../../findings/governance.md) | point 3, its own identity and the least privilege its task needs; [maintenance.md](../../findings/maintenance.md), workflow step 4, new tools or permissions are a higher change class |
| Safeguard Sloppage | [governance.md](../../findings/governance.md) | point 4, enforce limits outside the model; [observability.md](../../findings/observability.md), workflow step 7, watch override rates and approval patterns; [maintenance.md](../../findings/maintenance.md), point 3, every meaningful change re-runs the evaluations |
| Output Obsession | [observability.md](../../findings/observability.md) | point 5, operational metrics must be joined by quality and cost metrics; [evaluation.md](../../findings/evaluation.md), point 5, grade the outcome and also the path |
| Decay rating | [observability.md](../../findings/observability.md) | workflow step 9, review on a rhythm and decide continue, change, restrict, or retire. The tooth scale is Productside's and is labeled Assumption |

### Findings Used

- [evaluation.md](../../findings/evaluation.md)
- [goal.md](../../findings/goal.md)
- [governance.md](../../findings/governance.md)
- [maintenance.md](../../findings/maintenance.md)
- [observability.md](../../findings/observability.md)
- [retirement.md](../../findings/retirement.md)
- [tools-context.md](../../findings/tools-context.md)
- [Productside ADLC working model](../../findings/adlc-working-model.md)

### Method and Terms

- [Guided Context Capture](../../reference/guided-context-capture.md)
- [ADLC Glossary](../../reference/glossary.md)
- [Observe And Improve](../adlc-step6-observe-and-improve/SKILL.md)
- [Product Lifecycle Check](../adlc-util-plc-check/SKILL.md)

The findings label claims Fact, Inference, Hypothesis, or Unknown. This skill uses Assumption where the findings say Hypothesis. Much of the published guidance is vendor or practitioner opinion; treat it as Inference unless the findings mark it Fact.
