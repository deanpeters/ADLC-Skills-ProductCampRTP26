---
name: adlc-util-agent-strategy-canvas
description: Sum up an agent intent as nine boxes, three each for problem, solution, and value, then decide pivot, punt, or pursue before system design.
license: CC-BY-NC-SA-4.0
argument-hint: "[use case, workflow, or area where an agent might help]"
intent: >-
  Help Product Managers prove the discussions an agent strategy needs have
  happened: who has the problem and why, what the agent may and may not do and
  in what steps, and how success and failure will be seen. It sums up the
  intent on one page and ends in a gut-check and a pivot, punt, or pursue
  decision before the team invests in system design.
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
  - Design
  - Engineering
best-for:
  - "Summing up an approved intent on one page for a pivot, punt, or pursue conversation"
  - "Making sure the team has discussed the problem, the boundaries, and the measures before design"
  - "Choosing one narrow, governable piece of work when several ideas compete"
scenarios:
  - "Stage 1 produced a brief and leadership wants one page to decide whether to fund design"
  - "Leadership names an area where AI should help, and nobody has picked the narrow part"
evidence-required:
  - "An approved Agent Intent Brief, or a use case or workflow area, however rough"
  - "What is known about who has the problem and how often"
  - "Any boundaries, policies, or past incidents that limit what an agent may do"
produces:
  - "Agent Strategy Canvas"
  - "Gut-check result"
  - "Evidence and assumption ledger"
  - "Recorded human decision"
estimated-time: "30-60 min"
group-size: "1-8"
depends-on: []
combine-with:
  - adlc-step1-frame-intent
  - adlc-step2-design-agent-system
source-basis:
  - "Productside Agent Strategy Canvas, AI PM course"
  - "ADLC findings: goal and charter field guide"
  - "ADLC findings: governance field guide (ownership and authority)"
  - "ADLC findings: observability field guide"
sources:
  - https://www.anthropic.com/engineering/building-effective-agents
  - https://pair.withgoogle.com/chapter/user-needs/
interface:
  display_name: "Agent Strategy Canvas"
  short_description: "Pivot, punt, or pursue before design"
  brand_color: "#00E874"
  default_prompt: "Use $adlc-util-agent-strategy-canvas to sum up this agent intent as a nine-box canvas, run the gut-check, and stop at a pivot, punt, or pursue decision before Stage 2."
  allow_implicit_invocation: true
---

# Agent Strategy Canvas

## Purpose

Sum up an agent intent on one page, and prove three conversations have happened before the team invests in design: the problem space (who has the problem, what sets it off, what makes it worse), the solution space (what the agent is allowed to do, what is off-limits, in what steps), and value validation (how success is measured, how failure is spotted early, what good looks like at each step). Each space has three boxes, so the canvas holds nine boxes in all.

This is a utility. It sits outside the six-stage loop, at the handoff from Stage 1 to Stage 2. It does not replace the Agent Intent Brief. It turns the brief into a page a leadership group can argue with, fills what the brief left open, and ends in a gut-check and a pivot, punt, or pursue decision. It asks the two questions design would otherwise discover too late: is the scope governable, and can success be measured without ambiguity?

It can also run before Stage 1, when several ideas compete and the team needs to choose one narrow candidate. In that position its first question picks the candidate.

The canvas was written for an agent that runs periodically with relatively little human involvement. This skill keeps its structure and adds one adaptation: the Scope box names an autonomy level, and every step is marked as done by the agent, approved by a person, or handed back. That lets the same canvas serve a draft-only capability inside a client's own agent platform as well as a more autonomous agent.

## When to Use It

Use it after Stage 1 is approved, when the team or a sponsor must decide whether the intent deserves system design. Use it when the brief is complete but nobody has said out loud what makes the problem worse, what the steps are, or how failure would show early. Use it before Stage 1 when someone says "AI should help with X" and X is still an area, not a piece of work.

Do not use it to justify a solution already chosen. If the agent is already built or approved, record that constraint and use the canvas to find what was never discussed. Do not use it as a brief: the Agent Intent Brief is Stage 1's artifact, and the canvas never overrides it.

## Input

Use whatever the user already supplied: the approved Agent Intent Brief, notes from a workshop, research, a stakeholder mandate, a workflow description, support tickets, past incidents, policies, or a rough list of ideas.

Anything supplied with the invocation, attachments, or earlier conversation counts as context already given. Do not ask the user to repeat it. When an approved brief is supplied, most boxes come from it, and the skill asks only for what the brief left open.

Do not require a complete picture. If the user arrives with one sentence, produce a provisional canvas and label its assumptions. If the user arrives with a pile of notes, extract candidates and ask the user to choose one rather than blending them into one blurry agent.

**Example invocation:** `Use $adlc-util-agent-strategy-canvas on our approved intent brief for the payroll tax notice capability.`

## Key Concepts

Technical terms used here are defined in the [ADLC Glossary](../../reference/glossary.md).

**Narrow candidate** - One bounded piece of work, small enough that a person can say what the agent does and what it never does. "Prepare the first draft of a response to one kind of notice" is narrow. "Handle our tax work" is an area.

*Violation signal:* The candidate would still sound right if you replaced the agent with the whole department.

**Problem space** - The three boxes that say who has the problem and how often (Customer), what the problem is and what sets it off (Context), and under what conditions it occurs or gets worse (Cause). This space is about people and conditions, not about the agent.

*Violation signal:* A problem-space box mentions the agent, a model, or a tool.

**Solution space** - The three boxes that say what the agent is authorized to do (Scope), what it must never do (Safeguards), and the high-level sequence of its actions (Steps). This space is where autonomy is chosen.

*Violation signal:* Scope says "handle" or "manage" without naming an autonomy level, or Safeguards is empty because "the agent will be careful."

**Value validation** - The three boxes that say how success is measured (Metrics), how failure is detected early (Monitor), and what good looks like at each step (Milestones). It is about evidence someone other than the builder can observe.

*Violation signal:* Metrics are adoption, usage, or satisfaction with no baseline and no way to tell whether the work improved.

**Governable scope** - A scope where each safeguard can be enforced by how the system is built, such as read-only access or a blocked action, and not only by an instruction to the agent. The gut-check asks whether this holds.

*Violation signal:* Every safeguard would be broken by the agent simply deciding to ignore an instruction.

**Measurable without ambiguity** - Each metric and milestone is something an observer other than the builder could see happen, with a stated baseline or a stated way to get one.

*Violation signal:* Two reasonable people could disagree about whether a milestone was reached.

**Early failure signal** - A sign that the agent is going wrong before a person is harmed: a rate that moves, a mismatch, a handback pattern, an override. It is not the incident itself.

*Violation signal:* Monitor lists "complaints" or "incidents," which only appear after the harm.

## Guided Context Capture

Follow [Guided Context Capture](../../reference/guided-context-capture.md).

Begin with: "We will run the Agent Strategy Canvas and produce a nine-box canvas with a gut-check. I will use what you already supplied, ask no more than ten context questions (one to choose a candidate, then three for each space), and stop at a pivot, punt, or pursue decision before system design. Choose 1. Guided, 2. Context dump, or 3. Best guess."

Offer:

1. **Guided** - ask one question at a time, one box per question.
2. **Context dump** - extract `Known / Assumed / Missing / Conflicting` for each box from supplied material, then ask only about empty boxes and conflicts.
3. **Best guess** - draft all nine boxes now, mark every inferred detail, and end with the assumptions that most change the scope or whether the agent should exist.

Use an Adaptive Decision Ladder at the end. Anything supplied earlier must be reused.

In Guided mode, ask one at a time and skip answered questions:

1. `Canvas Q1/10` - Which one narrow piece of work should the agent take on? Skip this when an approved brief names it. If the user has not named one, offer three candidates, each a sentence of no more than 20 words with a reason of no more than 20 words, and ask the user to choose one. Do not blend them.
2. `Problem Q2/10` - Customer: who has this problem, and how often?
3. `Problem Q3/10` - Context: what is the problem, and what sets it off?
4. `Problem Q4/10` - Cause: under what conditions does it occur or get worse?
5. `Solution Q5/10` - Scope: what is the agent authorized to do, and at what level: suggest, draft, act with approval, act within limits, or decide?
6. `Solution Q6/10` - Safeguards: what is off-limits? What must it never do?
7. `Solution Q7/10` - Steps: what is the high-level sequence of actions?
8. `Value Q8/10` - Metrics: how will you measure success?
9. `Value Q9/10` - Monitor: how will you know early that it is failing?
10. `Value Q10/10` - Milestones: what does good look like at each step?

Ask only for what the invocation and earlier answers have not already given. Keep each box to one to three bullets, in plain language. If an answer to Q5 is vague, such as "handle it," ask one follow-up, labeled `Q5/10 follow-up`, before setting the autonomy level. Do not start a space until the previous space has all three boxes filled or marked Unknown, and say in one line what the space captured before moving on.

Progress labels keep their fixed numbers when questions are skipped, so a run that starts at `Problem Q2/10` and jumps to `Problem Q4/10` is expected. The budget is the most the skill may ask, not a target; with an approved brief, expect about half.

After Q7, mark each step as done by the agent, approved by a person, or handed back, using what Scope and Safeguards already said, and show the user the marking without asking a new question. After Q10, check that every step has a milestone.

In Context dump mode, extract per box and name each box's state. When the dump holds several candidate ideas, name each and ask the user to choose one. In Best guess mode, draft all nine boxes. A box the skill drafted is an Assumption until the Product Manager confirms it, even when it reads well.

## What It Produces

- Agent Strategy Canvas: the agent name and description line, then nine boxes in three spaces
- Gut-check result
- Evidence and assumption ledger
- Recorded human decision

When a folder is set, save as `agent-strategy-canvas.md`. This canvas is meant to be shared with the people who decide pivot, punt, or pursue, so offer to save it even when no folder was named, following [Saving Artifacts](../../reference/guided-context-capture.md#saving-artifacts).

The canvas must be specific enough that Stage 2 does not have to rediscover the customer, the trigger, the autonomy level, the steps, or the early failure signals. If design would still have to decide any of them, the canvas is not done.

## Workflow

1. **Name the one narrow candidate.** Take it from the approved brief when there is one. Otherwise state it in a sentence, and if several were supplied, offer three and ask the user to choose one.
2. **Run the "is an agent needed" screen.** Judge, from what you already have, whether a fixed rule or a fixed workflow would do the job. This is the skill's own check, not a question, and it does not count against the budget. If so, say so plainly. It does not block the canvas, but the answer is recorded and the gate notes it.
3. **Fill the problem space.** Customer, Context, Cause. Frequency and conditions that were never measured are Unknown, not guesses.
4. **Fill the solution space.** Scope with an autonomy level, Safeguards stated as blocked actions and approvals, and Steps in sequence. Mark each step as agent, person, or handback.
5. **Fill value validation.** Metrics with a baseline or a way to get one, Monitor signals that appear before harm, and one milestone for each step.
6. **Run the gut-check.** Ask the two canvas questions: is the scope governable, and can success be measured without ambiguity? Then run the cross-checks below.
7. **Present the decision gate.** Recommend the cleanest next move, but do not approve it for the user.

### Gut-Check Cross-Checks

| Check | Passes when | If it fails |
|---|---|---|
| Customer is a person | Customer names a role or a person doing the work, not "the team" or "the business" | Punt until discovery |
| Cause is observable | At least one condition in Cause can be seen in a real case | Punt until discovery |
| Scope names autonomy | Scope states one of the five levels | Revise; ask the Q5 follow-up |
| Safeguards are structural | At least one safeguard can be enforced by access or a blocked action, and none relies only on an instruction | Pivot: revise, or choose a narrower candidate |
| Safeguards do not contradict Scope | Nothing is both authorized and blocked | Revise |
| Every step is marked | Each step is agent, person, or handback | Revise |
| Every step has a milestone | One milestone per step, observable by someone other than the builder | Revise |
| Metrics have a baseline state | Each metric has a baseline stated as Fact, or is marked Assumption with the way to measure it | Revise; name the cheap test that would get the baseline |
| Monitor appears before harm | Each signal moves before a person is hurt | Revise |
| Scope is small enough | One person can say what the agent does and does not do in two sentences | Choose a narrower candidate |

### Hand-Off To The Lifecycle

The canvas feeds the stages that follow. It does not decide for them.

| Canvas box | Feeds |
|---|---|
| Customer | Stage 1 actors and who is affected; the "for" in the [Solution Hypothesis](../adlc-util-solution-hypothesis/SKILL.md) |
| Context | Stage 1 workflow and trigger |
| Cause | Stage 1 assumptions; Stage 4 edge cases |
| Scope | Stage 1 agent job, autonomy, and allowed actions; the "If we" in the Solution Hypothesis |
| Safeguards | Stage 1 blocked actions, approvals, and stop conditions; Stage 2 control boundaries and blocked tools |
| Steps | Stage 2 handoffs; the order of the Human Action and System Response turns in the [Minimum Viable Narrative](../adlc-util-minimum-viable-narrative/SKILL.md) |
| Metrics | Stage 1 success evidence; the validation measures in the Solution Hypothesis |
| Monitor | Stage 1 stop conditions; Stage 5 incident triggers and observation contract; Stage 6 |
| Milestones | Stage 4 pass conditions, one per step |

The order when all three canvases are used: Stage 1, then this canvas and its pivot, punt, or pursue decision, then Stage 2, then the Solution Hypothesis and its decision, then Stage 3, which names the prototype variants, then the Minimum Viable Narrative and its decision, which gives each variant a story and a portable prompt, then a Stage 4 bake-off. That path takes a Product Manager from intent to the right thing to build before investing at scale. When a canvas item is missing from the brief, the canvas adds it as an Assumption; it never changes an approved brief field. If a box contradicts the brief, recommend pivoting back to Stage 1.

## Human Decision Gate

Mark as recommended the option the evidence supports, and list it first. When the artifact is weak, that is a pivot, punt, or stop option, not pursue.

Stop with an Adaptive Decision Ladder:

1. `Pursue into Stage 2 (Recommended when all nine boxes are filled and the gut-check passes)` - the candidate is narrow, the scope is governable, and success can be measured.
2. `Pivot: revise the canvas` - useful when boxes are close but a cross-check failed.
3. `Pivot: choose a narrower candidate, or route back to Stage 1` - needed when the scope is too big to govern or measure, or a box contradicts the approved brief.
4. `Punt: park until a named trigger` - appropriate when who has the problem is Unknown, when Cause is Unknown, or when the problem has not been seen in real work. An Unknown frequency alone does not call for a punt; record it, and name the cheapest way to measure it. Name the trigger, such as a discovery interview or a measured baseline, and who checks it.
5. `Stop the agent effort` - appropriate when a fixed rule or workflow does the job, or no governable scope exists.
6. `Other (specify)` - for a custom path.

When the canvas ran before Stage 1, read "Stage 2" in option 1 as "Stage 1." Record the selected option and any unresolved disagreement. Do not continue into the next stage unless the user explicitly asks.

## Evidence and Attribution Rules

Label every material claim as Fact, Inference, Assumption, or Unknown. Do not invent customer evidence, frequencies, baselines, incidents, benchmarks, legal requirements, or performance claims. A canvas box drafted by the skill is an Assumption until the Product Manager confirms it. A frequency or baseline nobody measured is Unknown, and the Metrics box names the cheapest way to measure it.

## Common Failure Modes

- Filling the boxes with a solution, then calling it a problem space.
- Treating the agent as the customer.
- Writing Scope as "handle" or "manage" with no autonomy level.
- Leaving Safeguards empty, or listing only instructions the agent could ignore.
- Choosing metrics that measure adoption instead of whether the work improved.
- Monitoring incidents that only appear after harm.
- Letting Steps and Milestones drift apart so some steps have no definition of good.
- Blending several candidate ideas into one canvas.
- Counting a skill-drafted box as confirmed.
- Skipping the gut-check because every box has text in it.

## Assets and Examples

Use `template.md`. See `examples/worked-example.md` and `examples/weak-example.md`.

## Sources

This skill draws on Productside's Agent Strategy Canvas from the AI PM course and on the ADLC findings, Productside's synthesis of published guidance on agent development. The findings link to the original sources; full citations are in the [bibliography](../../findings/bibliography.md).

### Evidence Base for Key Concepts

| Key concept | Findings guide | Where |
|---|---|---|
| Narrow candidate | [goal.md](../../findings/goal.md) | point 1, ask first whether an agent is needed; also architecture.md, point 1, start with the simplest design that could work |
| Problem space | [goal.md](../../findings/goal.md) | point 2, start from the user need and a problem you can judge |
| Solution space | [goal.md](../../findings/goal.md) | point 3, autonomy is a choice made per use case, in steps |
| Value validation | [goal.md](../../findings/goal.md) | point 4, success written down before building; evaluation.md, point 1, evals as acceptance criteria |
| Governable scope | [governance.md](../../findings/governance.md) | point 4, enforce limits outside the model; architecture.md, point 9, authority belongs in structure |
| Measurable without ambiguity | [evaluation.md](../../findings/evaluation.md) | point 1, evals as acceptance criteria; point 5, grade the outcome and also the path |
| Early failure signal | [observability.md](../../findings/observability.md) | point 1, healthy infrastructure does not mean a healthy agent; point 9, monitoring needs an owner who gets alerted |

### Findings Used

- [architecture.md](../../findings/architecture.md)
- [evaluation.md](../../findings/evaluation.md)
- [goal.md](../../findings/goal.md)
- [governance.md](../../findings/governance.md)
- [observability.md](../../findings/observability.md)
- [Productside ADLC working model](../../findings/adlc-working-model.md)

### Method and Terms

- [Guided Context Capture](../../reference/guided-context-capture.md)
- [ADLC Glossary](../../reference/glossary.md)
- [Solution Hypothesis](../adlc-util-solution-hypothesis/SKILL.md)
- [Minimum Viable Narrative](../adlc-util-minimum-viable-narrative/SKILL.md)

The findings label claims Fact, Inference, Hypothesis, or Unknown. This skill uses Assumption where the findings say Hypothesis. Much of the published guidance is vendor or practitioner opinion; treat it as Inference unless the findings mark it Fact.
