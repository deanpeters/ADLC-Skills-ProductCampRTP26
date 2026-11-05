---
name: adlc-util-plc-check
description: Ask whether the product's lifecycle stage has changed since an agent was approved, and whether the agent's job, autonomy, measures, and exit should change with it.
license: CC-BY-NC-SA-4.0
argument-hint: "[product, the agent that serves it, and the approved brief or canvas]"
intent: >-
  Help Product Managers keep an agent's job matched to the product it serves.
  The same build loops do a different job at every stage of the product
  lifecycle: an agent approved to help a product launch is not the agent a
  mature or declining product needs. The check names the product's stage then
  and now, asks the question the product team owns at this stage, tests
  whether the agent's job and the stage's biggest risk still fit, and stops at
  a decision: keep the deal, change the deal, scale, or plan the exit.
type: utility
theme: agent-development-lifecycle
phase: 0
status: active
operating-level:
  - product-team
  - initiative
  - portfolio
audience:
  - Product Manager
  - Product Leader
  - Product Operations
best-for:
  - "A strategy or portfolio review where the product has moved stage since its agents were approved"
  - "Deciding whether to scale, re-scope, or retire an agent when the product's numbers change direction"
  - "Planning an agent's exit alongside the product's end of life"
scenarios:
  - "An onboarding agent approved at launch is still running unchanged two years later, and the product's growth has flattened"
  - "Leadership asks to expand agents across a product that is entering decline"
evidence-required:
  - "The approved Agent Intent Brief or Agent Strategy Canvas, and the date it was approved"
  - "Signals of the product's stage then and now: revenue and profit direction, customer growth, competitive moves, or a roadmap decision"
  - "What the agent does today, and how it is measured"
produces:
  - "Product Lifecycle Check"
  - "Stage fit and stage risk"
  - "Recorded human decision"
estimated-time: "20-40 min"
group-size: "1-8"
depends-on: []
combine-with:
  - adlc-util-agent-strategy-canvas
  - adlc-step1-frame-intent
  - adlc-step6-observe-and-improve
  - adlc-util-decay-check
source-basis:
  - "Productside Product Lifecycle × Build Loops teaching model"
  - "ADLC findings: goal and charter field guide (autonomy chosen per use case, in steps)"
  - "ADLC findings: retirement field guide"
  - "ADLC findings: maintenance and versioning field guide (periodic continue, change, migrate, or retire)"
sources:
  - https://learn.microsoft.com/en-us/agents/center-of-excellence/agent-lifecycle
  - https://www.ibm.com/think/topics/agent-lifecycle-management
  - https://www.ibm.com/think/topics/agent-development-lifecycle-adlc
  - https://www.bvp.com/atlas/bessemers-ai-agent-autonomy-scale
interface:
  display_name: "Product Lifecycle Check"
  short_description: "Has the product's stage changed the deal?"
  brand_color: "#00E874"
  default_prompt: "Use $adlc-util-plc-check on this product and its agent: name the lifecycle stage then and now, test whether the agent's job still fits, and stop at a decision."
  allow_implicit_invocation: true
---

# Product Lifecycle Check

## Purpose

Ask whether the product an agent serves has moved to a new lifecycle stage since the agent was approved, and whether the agent's job should move with it.

Same loops, a different job at every stage. A product moves through design, introduction, growth, maturity, and decline, and at each stage the product team owns a different question. An agent approved for one stage keeps doing that stage's job unless someone changes the deal. That is how a launch-era agent ends up optimizing a decline, or how a dying product is kept alive cheaply by agents nobody re-examined. This check names the stage then and now, asks this stage's question, tests the agent's job and risk against it, and stops at a decision.

| Stage | The product team owns | A typical agent job | The biggest AI risk |
|---|---|---|---|
| Design | Is the problem real? | Research and synthesis | Building before validating |
| Introduction | Is this the right value? | Onboarding and support | Shipping volume, not value |
| Growth | Where do we differentiate? | Scaling the work, with real governance | Feature sprawl at machine speed |
| Maturity | Defend or reinvent? | Tuning customer experience and operations | Optimizing a decline |
| Decline | When do we let go? | Retiring with the product | Zombie products kept alive cheaply |

The agent jobs in the table are typical, not rules. The questions and risks are what the check tests.

This is a utility. It sits outside the six-stage loop. It does not decide strategy for the product; it makes sure the agent's deal is re-asked when the product's strategy changes, and hands off to the canvas, Stage 1, or Stage 6.

## When to Use It

Use it at a strategy, portfolio, or quarterly review. Use it when the product's numbers change direction: growth flattens, profit peaks, a competitor reshapes the market, or a sunset date is set. Use it before scaling an agent across a product, so the scale matches the stage. Use it when an agent has run unchanged for a long time and nobody can say which stage it was built for.

Do not use it to choose a product strategy; that belongs to the product team and leadership. Do not use it to diagnose drift inside the agent; that is the [Constraint Decay Check](../adlc-util-decay-check/SKILL.md). The two often run together: this one asks whether the deal changed, the decay check asks whether the constraints kept up.

## Input

Use whatever the user already supplied: the Agent Intent Brief, the Agent Strategy Canvas, the last Observation Review, a strategy or roadmap document, revenue and profit trends, customer growth, competitive notes, or a description of what the agent does today.

Anything supplied with the invocation, attachments, or earlier conversation counts as context already given. Do not ask the user to repeat it.

Do not require exact figures. A direction of travel, such as "growth flattened over three quarters," is enough to place a stage as Inference. If nobody knows the direction, the stage is Unknown, and the check names the cheapest way to find out.

**Example invocation:** `Use $adlc-util-plc-check on our meal-kit app's onboarding agent. It was approved at launch; here is the canvas and this year's subscriber numbers.`

## Key Concepts

Technical terms used here are defined in the [ADLC Glossary](../../reference/glossary.md).

**Product lifecycle stage** - Where the product sits now: design, introduction, growth, maturity, or decline, judged from the direction of revenue, profit, customer growth, and competitive position, not from age.

*Violation signal:* The stage is named from how long the product has existed, or from what the team hopes, with no signal behind it.

**Stage question** - The question the product team owns at this stage: is the problem real, is this the right value, where do we differentiate, defend or reinvent, when do we let go. The agent's job should help answer it.

*Violation signal:* Nobody can say how the agent's work helps answer this stage's question.

**Stage fit** - Whether the agent's current job, autonomy, and measures match the stage. A job that fitted an earlier stage is not wrong; it may simply be the wrong job now.

*Violation signal:* The agent's success measure is still the one chosen at approval, even though the product's goal has changed, such as activation at launch while the product now needs retention or cost to serve.

**Stage risk** - The biggest AI risk for the stage: building before validating, shipping volume over value, feature sprawl, optimizing a decline, or keeping a zombie product alive. The check asks whether that risk is showing.

*Violation signal:* The stage risk is present and is being reported as a success, for example more features shipped while differentiation falls.

**Autonomy follows the stage** - How much the agent may do alone is chosen per use case and raised in steps with evidence, not raised because the product grew. Scaling an agent is a governance decision, not a growth reflex.

*Violation signal:* Autonomy or reach was expanded because the product is growing, with no new evidence and no Stage 5 decision.

**Exit tied to the product** - An agent's retirement trigger is linked to the product's end of life, so the agent does not outlive the product or keep a declining product running out of habit.

*Violation signal:* The product has a sunset date and the agent has no retirement plan, or the agent has no retirement trigger at all.

## Guided Context Capture

Follow [Guided Context Capture](../../reference/guided-context-capture.md).

Begin with: "We will run a Product Lifecycle Check: name the product's stage then and now, test whether the agent's job still fits, and stop at a decision. I will use what you already supplied, ask no more than seven questions, and recommend keeping the deal, changing it, scaling, or planning the exit. Choose 1. Guided, 2. Context dump, or 3. Best guess."

Offer:

1. **Guided** - ask one question at a time.
2. **Context dump** - extract `Known / Assumed / Missing / Conflicting` for each part of the check from supplied material, then ask only about gaps and conflicts.
3. **Best guess** - draft the whole check now, mark every inferred stage and fit, and end with the signal that would most change the decision.

Use an Adaptive Decision Ladder at the end. Anything supplied earlier must be reused.

In Guided mode, ask one at a time and skip answered questions:

1. `Agent Q1/7` - Which product, and which agent serving it? What was it approved to do, and when?
2. `Then Q2/7` - What stage was the product in when the agent was approved, and what told you so?
3. `Now Q3/7` - What stage is it in now? Which way are revenue, profit, and customer growth moving, and what are competitors doing?
4. `Question Q4/7` - What question does the product team own now, and how does the agent's work help answer it?
5. `Job Q5/7` - What does the agent do today, at what autonomy level, and how is it measured?
6. `Risk Q6/7` - Is this stage's biggest AI risk showing? What would you see if it were?
7. `Exit Q7/7` - Is there a plan for the product's end of life, and is the agent's retirement tied to it?

Ask only for what the invocation and earlier answers have not already given. The budget is the most the skill may ask, not a target.

## What It Produces

- Product Lifecycle Check: the stage then and now with the signals behind each, the stage question, and the agent's job, autonomy, and measure
- Stage fit and stage risk: what still fits, what fitted an earlier stage, and whether the stage risk is showing
- Recorded human decision

When a folder is set, save as `product-lifecycle-check.md`. It is meant for the product leader and the agent's owner, so offer to save it even when no folder was named, following [Saving Artifacts](../../reference/guided-context-capture.md#saving-artifacts).

## Workflow

1. **Name the agent and its deal.** Take the approved brief or canvas and its date. If there is none, say so; the check can still run, but its first hand-off is the Agent Strategy Canvas.
2. **Place the stage then and now.** Use signals, not age. Label each stage Fact, Inference, or Unknown. If the stage has not changed, say so; the check may end at Keep.
3. **Ask the stage question.** Write the question the product team owns now, and how the agent's work helps answer it, or does not.
4. **Test stage fit.** Compare the agent's job, autonomy, and success measure with what this stage needs. Mark each Fits, Fitted an earlier stage, or Unknown.
5. **Test stage risk.** Name this stage's biggest AI risk and the evidence for or against it.
6. **Check the exit.** Confirm the agent's retirement trigger is tied to the product's end of life.
7. **Present the decision gate.** Recommend the cleanest move, and do not approve it for the user.

### Stage Change To Agent Change

| When the product moves to | Re-ask in the canvas | Watch for |
|---|---|---|
| Introduction | Is the agent creating the right value, or just activity? | Volume reported as success |
| Growth | Which work differentiates us, and which is sprawl? | Autonomy or reach raised without evidence |
| Maturity | Is the agent defending, reinventing, or just cutting cost? | Optimizing a measure that no longer matters |
| Decline | What is the agent's exit, and who decides when? | Agents keeping the product alive by habit |

## Human Decision Gate

Mark as recommended the option the evidence supports, and list it first. When the stage has changed and the agent's job fitted an earlier stage, the recommendation is not Keep.

Stop with an Adaptive Decision Ladder:

1. `Keep the deal (Recommended when the stage has not changed, or the agent's job still fits)` - set the date of the next check.
2. `Change the deal` - re-run the [Agent Strategy Canvas](../adlc-util-agent-strategy-canvas/SKILL.md) for this stage, then Stage 1 for the brief; consider a [Constraint Decay Check](../adlc-util-decay-check/SKILL.md) first.
3. `Scale with evidence` - the stage supports more reach; take it to Stage 5 as a governed change, not an automatic expansion.
4. `Plan the exit` - the product is in decline or the agent's job has ended; route to Stage 6 for a Retirement Plan tied to the product's end of life.
5. `Punt: re-check at a named trigger` - the stage is Unknown; name the signal, such as two more quarters of numbers, and who checks it.
6. `Other (specify)` - for a custom path.

Record the selected option, who made it, and any unresolved disagreement. Do not change the agent, its scope, or the product strategy on the person's behalf.

## Evidence and Attribution Rules

Label every material claim as Fact, Inference, Assumption, or Unknown. Do not invent revenue, profit, growth, market, or competitive figures. A stage placed from a direction of travel is Inference; a stage placed from hope or age is an Assumption and is marked as one. A stage nobody can place is Unknown, and the check names the cheapest way to find out.

## Common Failure Modes

- Naming the stage from the product's age instead of its signals.
- Treating the stage table's agent jobs as rules instead of starting points.
- Raising autonomy or reach because the product is growing.
- Keeping the success measure chosen at launch after the product's goal changed.
- Reporting the stage's biggest risk as success, such as more features shipped in a maturing market.
- Letting the agent outlive the product, or keep a declining product alive by habit.
- Deciding product strategy inside the check instead of handing the deal back to the people who own it.

## Assets and Examples

Use `template.md`. See `examples/worked-example.md` and `examples/weak-example.md`.

## Sources

The stage table is Productside's Product Lifecycle × Build Loops teaching model. The agent practices behind each concept draw on the ADLC findings, Productside's synthesis of published guidance on agent development. The findings link to the original sources; full citations are in the [bibliography](../../findings/bibliography.md).

### Evidence Base for Key Concepts

| Key concept | Findings guide | Where |
|---|---|---|
| Product lifecycle stage | none | Productside's Product Lifecycle × Build Loops teaching model; labeled Assumption. No finding covers product lifecycle stages |
| Stage question | [goal.md](../../findings/goal.md) | point 2, start from the user need and a problem you can judge; the stage questions themselves are Productside's and labeled Assumption |
| Stage fit | [goal.md](../../findings/goal.md) | point 4, success written down before building, in business terms; [maintenance.md](../../findings/maintenance.md), workflow step 10, review periodically and decide continue, change, migrate, or retire |
| Stage risk | [retirement.md](../../findings/retirement.md) | point 3, sprawl is partly a failure to retire; the stage risks are Productside's and labeled Assumption |
| Autonomy follows the stage | [goal.md](../../findings/goal.md) | point 3, autonomy is a choice made per use case, in steps; workflow step 4, decide the level and the conditions for moving up |
| Exit tied to the product | [retirement.md](../../findings/retirement.md) | point 1, retirement belongs in the lifecycle from the start; point 7, retirement should be a decision, not drift; workflow step 1, a strategy change triggers a retirement review |

### Findings Used

- [goal.md](../../findings/goal.md)
- [maintenance.md](../../findings/maintenance.md)
- [retirement.md](../../findings/retirement.md)
- [Productside ADLC working model](../../findings/adlc-working-model.md)

### Method and Terms

- [Guided Context Capture](../../reference/guided-context-capture.md)
- [ADLC Glossary](../../reference/glossary.md)
- [Agent Strategy Canvas](../adlc-util-agent-strategy-canvas/SKILL.md)
- [Constraint Decay Check](../adlc-util-decay-check/SKILL.md)

The findings label claims Fact, Inference, Hypothesis, or Unknown. This skill uses Assumption where the findings say Hypothesis. Much of the published guidance is vendor or practitioner opinion; treat it as Inference unless the findings mark it Fact.
