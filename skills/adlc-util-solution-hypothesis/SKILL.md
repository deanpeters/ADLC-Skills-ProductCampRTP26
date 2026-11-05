---
name: adlc-util-solution-hypothesis
description: Turn an approved system design into a falsifiable If/Then bet with two tiny acts of discovery and two measures, then decide pivot, punt, or pursue before building a harness.
license: CC-BY-NC-SA-4.0
argument-hint: "[approved Agent System Map, plus any canvas or tiny-act results]"
intent: >-
  Help Product Managers state the bet a design is making in terms a cheap test
  could prove wrong, run or plan the cheapest tests first, and hold a pivot,
  punt, or pursue conversation before the team invests in a harness and
  prototypes. It also gives Stage 6 the measures to check whether the bet held.
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
  - "Deciding whether a designed agent system is worth a harness and prototypes"
  - "Turning an unmeasured baseline into a Fact with a cheap test before building"
  - "Writing the measures Stage 6 will later check"
scenarios:
  - "Stage 2 approved a design and the team is about to commission prototypes"
  - "A stakeholder asks why this solution, and the team has only enthusiasm to show"
evidence-required:
  - "Approved Agent System Map"
  - "Approved Agent Intent Brief or Agent Strategy Canvas"
  - "Any results from tiny acts of discovery already run"
produces:
  - "Solution Hypothesis statement"
  - "Tiny-act plan and results"
  - "Evidence and assumption ledger"
  - "Recorded human decision"
estimated-time: "20-40 min"
group-size: "1-8"
depends-on: []
combine-with:
  - adlc-step2-design-agent-system
  - adlc-step3-generate-agent-harness
  - adlc-step6-observe-and-improve
source-basis:
  - "Productside Epic-Level Solution Hypothesis canvas, AI PM course"
  - "ADLC findings: goal and charter field guide"
  - "ADLC findings: evaluation field guide"
sources:
  - https://www.anthropic.com/engineering/building-effective-agents
  - https://pair.withgoogle.com/chapter/user-needs/
interface:
  display_name: "Solution Hypothesis"
  short_description: "Pivot, punt, or pursue before the harness"
  brand_color: "#00E874"
  default_prompt: "Use $adlc-util-solution-hypothesis to turn this approved system map into an If/Then bet with two tiny acts and two measures, and stop at a pivot, punt, or pursue decision before Stage 3."
  allow_implicit_invocation: true
---

# Solution Hypothesis

## Purpose

Turn an approved system design into a bet a cheap test could prove wrong, before the team spends on a harness and prototypes. The statement has three parts: an If/Then sentence, two tiny acts of discovery that test its assumptions, and one quantitative and one qualitative measure with a timeframe.

This is a utility. It sits outside the six-stage loop, between Stage 2 and Stage 3. It does not replace the Agent System Map. It asks the question the design alone cannot answer: now that we know what we could build, is it still the bet worth making? It ends in a pivot, punt, or pursue decision.

Stage 1 already named success evidence, and the Agent Strategy Canvas may have named metrics. This skill sharpens them into a statement about the designed solution, and adds the cheapest tests that could change the answer before anything is built.

## When to Use It

Use it after Stage 2 is approved and before Stage 3, when the team is about to commission a harness or prototypes. Use it when a baseline in the brief is an Assumption and a few days of work could make it a Fact. Use it when a stakeholder asks "why this solution?" and the honest answer is a hunch.

Do not use it before the design exists: at Stage 1, use the [Agent Strategy Canvas](../adlc-util-agent-strategy-canvas/SKILL.md) instead. Do not use it to re-open the authority decisions Stage 2 made.

## Input

Use whatever the user already supplied: the approved Agent System Map, the Agent Intent Brief, an Agent Strategy Canvas, notes from conversations with users, and results of any tiny acts already run.

Anything supplied with the invocation, attachments, or earlier conversation counts as context already given. Do not ask the user to repeat it.

Do not require a finished statement. If the user arrives with only an approved map, draft the statement from it and label what is assumed.

**Example invocation:** `Use $adlc-util-solution-hypothesis on our approved system map for the payroll tax notice capability.`

## Key Concepts

Technical terms used here are defined in the [ADLC Glossary](../../reference/glossary.md).

**If/Then statement** - "If we [action or solution, on behalf of a person] for [that person], then we will [the outcome or job the person gets done]." The If clause names the designed solution, not the idea.

*Violation signal:* The If clause would read the same before Stage 2 ran, or names a technology instead of what the person gets.

**Tiny act of discovery** - A test a small team can run in days without building the thing: time a few people doing the work today, hand-assemble a sample result and watch someone review it, ask the owner of an adjoining system how a call would be approved. One tiny act tests one assumption.

*Violation signal:* The "tiny act" is a pilot, a build, or anything that needs the harness.

**Validation measure** - An outcome someone other than the builder can observe within a stated timeframe: one quantitative, one qualitative.

*Violation signal:* A measure has no timeframe, no baseline state, or could only be judged by the team that built it.

**Falsifiable bet** - A statement that a plausible result could prove wrong. If no observable result would change the team's mind, it is a slogan.

*Violation signal:* Every imaginable outcome would be read as support.

**Autonomy ceiling** - The autonomy level and blocked actions Stage 1 and Stage 2 approved. The statement must fit inside it.

*Violation signal:* The If clause says "file," "decide," "send," or anything above the approved level.

**Value evidence and safety evidence** - A measure that holds shows the bet was worth making. It says nothing about whether the agent is safe at more authority. Safety evidence comes from evals and traces.

*Violation signal:* A held measure is cited as the reason to widen authority.

**Pivot, punt, or pursue** - The three ways this conversation can end, defined in the [ADLC Glossary](../../reference/glossary.md). Pursue moves to Stage 3. Pivot changes the bet or routes back. Punt parks it with a named trigger for revisiting.

*Violation signal:* A punt has no revisit trigger, so it quietly becomes a stop nobody decided.

## Guided Context Capture

Follow [Guided Context Capture](../../reference/guided-context-capture.md).

Begin with: "We will write a Solution Hypothesis for the approved design and decide pivot, punt, or pursue before Stage 3. I will use the system map and anything earlier, ask no more than seven context questions, and stop at that decision. Choose 1. Guided, 2. Context dump, or 3. Best guess."

Offer:

1. **Guided** - ask one question at a time.
2. **Context dump** - extract `If / For / Then / Tiny acts / Measures / Results / Gaps` from supplied material, then ask only about gaps.
3. **Best guess** - draft the full statement now, mark every inferred detail, and rank the assumptions by how much they could change the decision.

Use an Adaptive Decision Ladder at the end. Anything supplied earlier must be reused.

In Guided mode, ask one at a time and skip answered questions:

1. `Hypothesis Q1/7` - If we: what does the designed solution do for the person, in one clause?
2. `Hypothesis Q2/7` - For: which person is it for?
3. `Hypothesis Q3/7` - Then we will: what outcome or job does that person get done?
4. `Hypothesis Q4/7` - What is the first tiny act, and has it been run? If so, what did it show?
5. `Hypothesis Q5/7` - What is the second tiny act, and has it been run? If so, what did it show?
6. `Hypothesis Q6/7` - What quantitative measure, with a timeframe, would show the bet is valid?
7. `Hypothesis Q7/7` - What qualitative measure, with a timeframe, would show the bet is valid?

The brief, the canvas, and the map usually answer Q1 to Q3 and seed Q6 and Q7. Say what you already have in one line and ask only for what is missing. If a baseline is an Assumption, propose a tiny act that would measure it as the first tiny act.

## What It Produces

- Solution Hypothesis statement: the If/Then sentence, "We will test our assumptions by" with two tiny acts, and "We know our hypothesis is valid if within [timeframe] we observe" with two measures
- Tiny-act plan and results, each marked not yet run or run, with what it showed
- Evidence and assumption ledger
- Recorded human decision

When a folder is set, save as `solution-hypothesis.md`. This statement is meant to be shared with the people who decide pivot, punt, or pursue, and Stage 6 checks it later, so offer to save it even when no folder was named, following [Saving Artifacts](../../reference/guided-context-capture.md#saving-artifacts).

The statement must be specific enough that the [Minimum Viable Narrative](../adlc-util-minimum-viable-narrative/SKILL.md) utility can carry it into each story as written, and Stage 6 can check each measure.

## Workflow

1. **Confirm the approved design and ceiling.** Quote the autonomy level and blocked actions from the map. The statement must fit inside them.
2. **Write the If/Then sentence.** Name the designed solution, the person, and the outcome.
3. **Name two tiny acts.** Put the one that turns the biggest Assumption into a Fact first, usually the baseline. A baseline must time the same span the target measures.
4. **Record what each tiny act showed, if it was run.** Label an observed result Fact and any generalization from a small sample Inference. A tiny act not yet run is Unknown, not evidence.
5. **Write the two measures with a timeframe and baseline state.**
6. **Read the results for shape questions.** If a tiny act showed that people want the result shaped differently, say so and suggest comparing variants at Stage 3. Do not decide the shape here.
7. **Present the decision gate.** Recommend, do not decide.

### Stage 6: Did The Bet Hold

When Stage 6 reviews a deployment that had a Solution Hypothesis, check each measure: the target, the timeframe, what was observed, and whether it held, partly held, or did not hold. A held measure is value evidence, not safety evidence. A measure nobody collected is Unknown, and the review names which artifact must change so it is collected next time. If the bet did not hold, say whether the cause is the intent (Stage 1), the system (Stage 2), or the harness (Stage 3).

## Human Decision Gate

Mark as recommended the option the evidence supports, and list it first. When the bet is weak, that is a pivot, punt, or stop option, not pursue.

Stop with an Adaptive Decision Ladder:

1. `Pursue into Stage 3 (Recommended when the statement is falsifiable, fits the ceiling, and at least one tiny act has been run)` - build the harness and prototypes against this bet.
2. `Pivot: revise the bet` - useful when a tiny act showed the outcome or the person is different from what the statement says.
3. `Pivot: route back to Stage 2` - needed when the bet needs a design the map does not support.
4. `Punt: park the bet until a named trigger` - appropriate when a tiny act must run first, or a dependency is not ready. Name the trigger and who checks it.
5. `Stop the effort` - appropriate when a tiny act showed the problem is not worth solving this way.
6. `Other (specify)`.

When neither tiny act has been run, recommend `Punt` with running the first tiny act as the trigger, unless the person chooses to pursue and records that as an accepted risk. Record the selected option and any unresolved disagreement. Do not continue into Stage 3 unless the user explicitly asks.

## Evidence and Attribution Rules

Label every material claim as Fact, Inference, Assumption, or Unknown. Do not invent tiny-act results, baselines, user statements, benchmarks, or performance claims. Numbers in a statement are targets. A target stays an Assumption until it is observed, even after the baseline is measured: the baseline becomes a Fact, the target is still the bet.

## Common Failure Modes

- Writing the If clause about the idea instead of the designed solution.
- Calling a pilot a tiny act.
- Treating an unrun tiny act as evidence.
- Measures with no timeframe or no baseline state.
- An If clause that outruns the approved autonomy.
- Deciding the shape of the result here instead of carrying the question to Stage 3.
- A punt with no revisit trigger.
- Citing a held measure as a reason to widen authority at Stage 6.

## Assets and Examples

Use `template.md`. See `examples/worked-example.md` and `examples/weak-example.md`.

## Sources

This skill draws on Productside's Epic-Level Solution Hypothesis canvas from the AI PM course and on the ADLC findings, Productside's synthesis of published guidance on agent development. The findings link to the original sources; full citations are in the [bibliography](../../findings/bibliography.md).

### Evidence Base for Key Concepts

| Key concept | Findings guide | Where |
|---|---|---|
| If/Then statement | [goal.md](../../findings/goal.md) | point 2, start from the user need and a problem you can judge |
| Tiny act of discovery | [goal.md](../../findings/goal.md) | point 8, real data, early |
| Validation measure | [goal.md](../../findings/goal.md) | point 4, success written down before building |
| Falsifiable bet | [evaluation.md](../../findings/evaluation.md) | point 1, evals as acceptance criteria |
| Autonomy ceiling | [goal.md](../../findings/goal.md) | point 3, autonomy is a choice made per use case, in steps |
| Value evidence and safety evidence | [evaluation.md](../../findings/evaluation.md) | point 9, safety evaluation reported per risk; governance.md, point 5, oversight designed to work |

### Findings Used

- [evaluation.md](../../findings/evaluation.md)
- [goal.md](../../findings/goal.md)
- [governance.md](../../findings/governance.md)
- [Productside ADLC working model](../../findings/adlc-working-model.md)

### Method and Terms

- [Guided Context Capture](../../reference/guided-context-capture.md)
- [ADLC Glossary](../../reference/glossary.md)
- [Agent Strategy Canvas](../adlc-util-agent-strategy-canvas/SKILL.md)
- [Minimum Viable Narrative](../adlc-util-minimum-viable-narrative/SKILL.md)

The findings label claims Fact, Inference, Hypothesis, or Unknown. This skill uses Assumption where the findings say Hypothesis. Much of the published guidance is vendor or practitioner opinion; treat it as Inference unless the findings mark it Fact.
