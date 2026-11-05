---
name: adlc-step1-frame-intent
description: Frame an agent idea as a clear intent brief with autonomy, success, non-goals, and stop boundaries before design begins.
license: CC-BY-NC-SA-4.0
argument-hint: "[agent idea, mandate, workflow, or opportunity]"
intent: >-
  Help Product Managers turn a vague agent request into an evidence-aware intent
  brief that names the human outcome, autonomy level, success criteria,
  boundaries, risks, and decision needed before system design.
type: interactive
theme: agent-development-lifecycle
phase: 1
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
  - "Turning a build-an-agent request into a product intent"
  - "Separating human outcome from model or workflow enthusiasm"
  - "Choosing an initial autonomy level before architecture"
scenarios:
  - "Leadership asks for an agent without naming the human job it should improve"
  - "A prototype exists but nobody can state what good behavior means"
evidence-required:
  - "Initial agent request or opportunity"
  - "Affected human workflow and actors"
  - "Desired outcome, constraints, and unacceptable failure modes"
produces:
  - "Agent Intent Brief"
  - "Evidence and assumption ledger"
  - "Recorded human decision"
estimated-time: "20-40 min"
group-size: "1-8"
depends-on: []
combine-with:
  - adlc-step2-design-agent-system
source-basis:
  - "ADLC findings: goal and charter field guide"
  - "ADLC findings: governance field guide (ownership and authority)"
  - "Productside ADLC working model"
sources:
  - https://www.ibm.com/think/topics/agent-development-lifecycle-adlc
  - https://www.anthropic.com/engineering/building-effective-agents
  - https://pair.withgoogle.com/chapter/user-needs/
  - https://learn.microsoft.com/en-us/agents/center-of-excellence/agent-lifecycle
interface:
  display_name: "Frame Agent Intent"
  short_description: "Define agent purpose and boundaries"
  brand_color: "#00E874"
  default_prompt: "Use $adlc-step1-frame-intent to turn this agent idea into an Agent Intent Brief and stop before system design."
  allow_implicit_invocation: true
---

# Frame Agent Intent

## Purpose

Turn an agent idea, mandate, workflow pain, or prototype into an Agent Intent Brief. This stage keeps the team from designing machinery before it can explain the product job, the user, the authority granted to the agent, and the evidence that would justify continuing.

This is not a naming exercise. "Build an agent for onboarding" sounds concrete, but it has not said whose work changes, which decisions the agent may make, what a responsible failure looks like, or what evidence would justify the next stage. The Product Manager job in this stage is to make those choices visible before the conversation becomes a tooling conversation.

## When to Use It

Use this skill before architecture, tool selection, vendor evaluation, or prompt design. Use it when the request says "agent," "copilot," "automation," or "AI teammate" before it names the human outcome.

Do not use it to rationalize a solution that has already been approved without evidence. If the decision is already irreversible, record that constraint and name which lifecycle questions remain unanswered.

## Input

Use whatever the user already supplied: notes, research, product goals, stakeholder mandate, workflow description, prototype behavior, support tickets, discovery findings, constraints, or risks.

Anything supplied with the invocation, attachments, or earlier conversation counts as context already given. Do not ask the user to repeat it.

Do not require a perfect brief. If the user arrives with only a sentence, produce a useful provisional brief and label its assumptions. If the user arrives with a pile of notes, extract the intent candidates rather than flattening them into one vague agent.

**Example invocation:** `Use $adlc-step1-frame-intent on this idea: we want an agent to help customer success managers prepare renewal plans.`

## Key Concepts

Technical terms used here are defined in the [ADLC Glossary](../../reference/glossary.md).

**Human outcome** - The observable improvement in a person's work. It is not the presence of an agent. It is the change the agent may help create.

*Violation signal:* The brief would still sound successful if no user's work improved.

**Agent job** - The bounded work the agent is being asked to perform. A good agent job fits inside the human workflow rather than replacing the entire workflow in one theatrical sentence.

*Violation signal:* The brief says the agent will "own onboarding," "handle renewals," or "manage support" without naming the narrower work unit.

**Autonomy level** - The degree to which the agent can suggest, draft, act, escalate, or decide. Naming autonomy prevents an assistant from becoming an unauthorized operator by drift.

*Violation signal:* The same sentence says the agent will "recommend" and "handle" the work without distinguishing approval.

**Authority boundary** - The limit on tools, data, actions, spend, messages, or decisions. A boundary is a product control, not a legal appendix.

*Violation signal:* The agent can affect customers, money, records, or commitments without a named approval path.

**Success evidence** - The behavior or outcome that would show the agent is useful. Success must be inspectable before the team debates launch.

*Violation signal:* Success is stated as adoption, efficiency, or delight with no observable measure.

**Stop condition** - The failure, uncertainty, or policy concern that halts the work or routes it backward. A stop condition protects the team from momentum.

*Violation signal:* The brief lists risks but no condition under which the team would stop.

## Guided Context Capture

Follow [Guided Context Capture](../../reference/guided-context-capture.md).

Begin with: "We will run ADLC Stage 1 and produce an Agent Intent Brief. I will use what you already supplied, ask no more than seven context questions, and stop before system design. Choose 1. Guided, 2. Context dump, or 3. Best guess."

Offer:

1. **Guided** - ask one question at a time.
2. **Context dump** - extract Known / Assumed / Missing / Conflicting from supplied material.
3. **Best guess** - draft a provisional brief with assumptions labeled.

Use an Adaptive Decision Ladder at the end. Anything supplied earlier must be reused.

After the brief is approved, the [Agent Strategy Canvas](../adlc-util-agent-strategy-canvas/SKILL.md) utility can sum it up as nine boxes and hold a pivot, punt, or pursue conversation before Stage 2. Offer it when a sponsor must decide whether to fund design. It does not change this stage's questions, budget, or gate.

In Guided mode, ask one at a time and skip answered questions:

1. `Intent Q1/7` - What decision should this brief support: explore, design, pilot, fund, or stop?
2. `Intent Q2/7` - What human workflow should improve first?
3. `Intent Q3/7` - Who does this work today, and who is affected if the agent gets it wrong?
4. `Intent Q4/7` - In the first version, should the agent suggest, draft, act with approval, act within limits, or decide?
5. `Intent Q5/7` - What must the agent not do without human approval?
6. `Intent Q6/7` - What evidence would show the agent is worth building?
7. `Intent Q7/7` - What failure would make you stop or route the effort back?

Ask only for what the invocation and earlier answers have not already given. If an answer to Q4 is vague, such as "handle it," ask one follow-up before setting autonomy.

In Context dump mode, extract `Known / Assumed / Missing / Conflicting`, then ask only about material gaps. When the dump contains several agent ideas, name each candidate and ask the user to choose one rather than blending them.

In Best guess mode, draft the brief immediately, mark assumptions inline, and rank `Assumptions to Validate` by how much they could change autonomy or whether the agent should exist.

## What It Produces

- Agent Intent Brief
- Evidence and assumption ledger
- Autonomy and authority statement
- Human decision record

When a folder is set, save as `stage-1-agent-intent-brief.md`, following [Saving Artifacts](../../reference/guided-context-capture.md#saving-artifacts).

The brief must be specific enough for Stage 2 to design a system without inventing product intent. If a builder would still have to decide the user, job, autonomy, or stop condition, the Stage 1 artifact is not done.

## Workflow

1. **Name the decision this brief serves.** State whether the decision is to explore, design, pilot, fund, or stop an agent effort.
2. **Name the human workflow and actor.** Keep the actor concrete: "renewal manager preparing account risks" beats "sales team productivity."
3. **Separate requested solution from intended outcome.** Mark "agent," "copilot," "automation," or a vendor name as proposed means unless already approved as a constraint.
4. **Define the agent job.** Name the narrow work unit the agent may perform in the first version.
5. **Set autonomy.** Use plain levels: suggest, draft, act with approval, act within limits, or decide.
6. **Name authority boundaries.** State blocked actions and approvals needed for customer, money, record, policy, or message impact.
7. **Define success evidence.** Include behavior evidence and product/workflow evidence where possible.
8. **Define stop conditions.** Name failures or unknowns that route backward or halt the effort.
9. **Present the decision gate.** Recommend the cleanest intent brief, but do not approve it for the user.

## Human Decision Gate

Mark as recommended the option the evidence supports, and list it first. When the artifact is weak, that is a revise, route-back, or stop option, not approval.

Stop with a choice. Use an Adaptive Decision Ladder:

1. `Approve this Agent Intent Brief (Recommended when the brief is complete)` - ready to design the system because actor, job, autonomy, evidence, and stop conditions are explicit.
2. `Revise the intent` - useful when the actor, job, or autonomy is close but not yet clean.
3. `Return to discovery` - needed when the human problem or evidence is too thin.
4. `Stop the agent effort` - appropriate when the request is a solution in search of a problem or the authority boundary is unacceptable.
5. `Other (specify)` - for a custom path.

Record the selected option and any unresolved disagreement. Do not continue into Stage 2 unless the user explicitly asks.

## Evidence and Attribution Rules

Label every material claim as Fact, Inference, Assumption, or Unknown. Do not invent customer evidence, approvals, benchmarks, legal requirements, or performance claims.

## Common Failure Modes

- Treating "agent" as the outcome.
- Choosing tools before autonomy.
- Hiding approval boundaries.
- Describing risks without stop conditions.
- Measuring demo success instead of product behavior.
- Turning several agent ideas into one blurry intent.
- Writing for leadership excitement instead of downstream design usefulness.

## Assets and Examples

Use `template.md`. See `examples/worked-example.md` and `examples/weak-example.md`.

## Sources

This skill draws on the ADLC findings, Productside's synthesis of published guidance on agent development. The findings link to the original sources; full citations are in the [bibliography](../../findings/bibliography.md).

### Evidence Base for Key Concepts

| Key concept | Findings guide | Where |
|---|---|---|
| Human outcome | [goal.md](../../findings/goal.md) | point 2, start from the user need and a problem you can judge |
| Agent job | [goal.md](../../findings/goal.md) | point 1, ask first whether an agent is needed; also architecture.md, point 2, workflow versus agent |
| Autonomy level | [goal.md](../../findings/goal.md) | point 3, autonomy is a choice made per use case, in steps |
| Authority boundary | [governance.md](../../findings/governance.md) | point 3, own identity and least privilege; architecture.md, point 9, authority belongs in structure |
| Success evidence | [goal.md](../../findings/goal.md) | point 4, success written down before building; evaluation.md, point 1, evals as acceptance criteria |
| Stop condition | [goal.md](../../findings/goal.md) | point 7, ownership and decision rights belong in the charter; retirement.md, point 1 |

### Findings Used

- [architecture.md](../../findings/architecture.md)
- [evaluation.md](../../findings/evaluation.md)
- [goal.md](../../findings/goal.md)
- [governance.md](../../findings/governance.md)
- [retirement.md](../../findings/retirement.md)
- [Productside ADLC working model](../../findings/adlc-working-model.md)

### Method and Terms

- [Guided Context Capture](../../reference/guided-context-capture.md)
- [ADLC Glossary](../../reference/glossary.md)

The findings label claims Fact, Inference, Hypothesis, or Unknown. This skill uses Assumption where the findings say Hypothesis. Much of the published guidance is vendor or practitioner opinion; treat it as Inference unless the findings mark it Fact.
