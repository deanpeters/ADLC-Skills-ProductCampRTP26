---
name: adlc-step5-deploy-with-governance
description: Prepare a governed deployment plan with launch gates, oversight, rollback, incident response, and authority to stop.
license: CC-BY-NC-SA-4.0
argument-hint: "[Validation Pack and proposed launch context]"
intent: >-
  Help Product Managers convert validation evidence into a deployment plan that
  names oversight, rollout scope, policy gates, rollback, incident handling, and
  human authority before a live agent reaches users or operations.
type: interactive
theme: agent-development-lifecycle
phase: 5
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
  - "Turning validation evidence into a launch decision"
  - "Defining oversight, rollback, and stop authority"
  - "Planning limited rollout before broader exposure"
scenarios:
  - "An agent passed evals and stakeholders want to pilot it"
  - "The team has a launch plan but no rollback or incident path"
evidence-required:
  - "Validation Pack and unresolved failures"
  - "Launch audience, workflow, and operational owners"
  - "Policy, privacy, security, and support constraints"
produces:
  - "Governed Deployment Plan"
  - "Launch gate checklist"
  - "Deployment decision record"
estimated-time: "45-90 min"
group-size: "1-8"
depends-on:
  - adlc-step4-validate-agent-behavior
combine-with:
  - adlc-step6-observe-and-improve
source-basis:
  - "ADLC findings: deployment field guide"
  - "ADLC findings: governance field guide"
  - "ADLC findings: retirement field guide (planning before launch)"
sources:
  - https://www.nist.gov/itl/ai-risk-management-framework
  - https://www.imda.gov.sg/-/media/imda/files/about/emerging-tech-and-research/artificial-intelligence/mgf-for-agentic-ai.pdf
  - https://www.cyber.gov.au/business-government/secure-design/artificial-intelligence/careful-adoption-of-agentic-ai-services
  - https://learn.microsoft.com/en-us/agents/center-of-excellence/govern-agents-risk
interface:
  display_name: "Deploy With Governance"
  short_description: "Plan launch gates and rollback"
  brand_color: "#00E874"
  default_prompt: "Use $adlc-step5-deploy-with-governance to create a Governed Deployment Plan from this validation evidence and stop before live operation."
  allow_implicit_invocation: true
---

# Deploy With Governance

## Purpose

Turn validation evidence into a Governed Deployment Plan. This stage defines launch scope, oversight, policy gates, rollback, incident response, communications, and authority to stop.

Governance is not the paperwork after the fun part. This stage turns validation evidence into a controlled exposure plan: who sees the agent, what the agent may do, who watches, what stops it, and how the team will learn without pretending a pilot is a full launch.

## When to Use It

Use this skill after validation and before pilot or production exposure. Use it when a stakeholder says the agent is ready to launch.

Do not use it to paper over failed validation. Unresolved unacceptable failures route backward.

## Input

Use the Validation Pack, proposed rollout audience, operational owners, policies, incident paths, support model, rollback options, and launch constraints.

Anything supplied with the invocation, attachments, or earlier conversation counts as context already given. Do not ask the user to repeat it.

If validation has hard-stop failures, do not proceed by adding monitoring language. Route backward. Monitoring does not make an unsafe behavior acceptable.

**Example invocation:** `Use $adlc-step5-deploy-with-governance with this Validation Pack for a five-person internal pilot.`

## Key Concepts

Technical terms used here are defined in the [ADLC Glossary](../../reference/glossary.md).

**Launch gate** - A condition that must be true before exposure. It protects the decision from enthusiasm.

*Violation signal:* The plan lists tasks but no condition that could block launch.

**Blast radius** - The number and importance of users, workflows, data, or decisions affected. It should be small enough to learn safely.

*Violation signal:* The first live release affects everyone the eventual system might serve.

**Oversight model** - Who watches, reviews, approves, and responds during deployment. Oversight is an operating responsibility, not a slogan.

*Violation signal:* The plan says "monitored closely" but no person, cadence, or action is named.

**Rollback path** - The mechanism to remove, disable, or reduce agent authority. It must be possible before it is needed.

*Violation signal:* Stopping requires improvised engineering work during an incident.

**Incident trigger** - A condition that starts response, communication, rollback, or review. It turns vague risk into action.

*Violation signal:* The plan lists risks but not what happens when one occurs.

**Observation contract** - The evidence the deployment must produce for Stage 6. A pilot that cannot teach the next decision is just exposure.

*Violation signal:* The plan says "monitor feedback" without naming traces, samples, cadence, or decision use.

## Guided Context Capture

Follow [Guided Context Capture](../../reference/guided-context-capture.md).

Begin with: "We will run ADLC Stage 5 and produce a Governed Deployment Plan. I will preserve the validation evidence, ask no more than seven context questions, and stop before live operation. Choose 1. Guided, 2. Context dump, or 3. Best guess."

Offer Guided, Context dump, and Best guess modes. Use an Adaptive Decision Ladder at the deployment gate. Anything supplied earlier must be reused.

In Guided mode, ask one at a time and skip answered questions:

1. `Deployment Q1/7` - What validation result authorizes deployment planning, and what remains unresolved?
2. `Deployment Q2/7` - Who is in the first exposure group, and what is the blast radius?
3. `Deployment Q3/7` - What launch gates must be true before exposure?
4. `Deployment Q4/7` - Who owns oversight, review cadence, and response?
5. `Deployment Q5/7` - What incident triggers require rollback, escalation, or communication?
6. `Deployment Q6/7` - How can the agent be disabled, reduced, or reverted?
7. `Deployment Q7/7` - What evidence must this deployment produce for Stage 6?

In Context dump mode, extract `Validation basis / Scope / Gates / Oversight / Rollback / Incidents / Observation`. In Best guess mode, draft a conservative limited deployment and mark all approvals or operating capacity as assumptions unless supplied.

## What It Produces

- Governed Deployment Plan
- Launch gate checklist
- Rollback and incident plan
- Deployment decision record

When a folder is set, save as `stage-5-governed-deployment-plan.md`, following [Saving Artifacts](../../reference/guided-context-capture.md#saving-artifacts).

The plan must be specific enough for operations to run the deployment without inventing oversight or rollback under pressure. It must also define what Stage 6 will inspect.

## Workflow

1. **Confirm validation evidence.** State which cases passed, which failed, and which gaps remain.
2. **Define deployment shape.** Pilot, limited release, staged rollout, shadow mode, or no launch.
3. **Set blast radius.** Name audience, workflow, data, authority, and duration.
4. **Set launch gates.** Include validation, policy, support, training, and technical gates as applicable. Include how users will know they are dealing with an AI agent and how they can reach a person. For agents that read untrusted content, include a check that injection probes pass on the production build, and consider starting in shadow mode.
5. **Define oversight.** Name owner, cadence, sample size, review surface, and escalation path.
6. **Define rollback.** Say how to disable, reduce authority, revert workflow, and communicate.
7. **Define incident triggers.** Use concrete conditions, not "if something goes wrong." For agents that read untrusted content, include any action traced to instructions inside that content.
8. **Define observation contract.** Name the traces, feedback, outcomes, and review schedule Stage 6 will use.
9. **Name the retirement basics.** Record the owner who can retire the agent, where it appears in the agent inventory, every place its credentials are granted, and what would trigger a retirement review. Stage 6 uses these if the agent is later retired.
10. **Present the deployment gate.**

## Human Decision Gate

Mark as recommended the option the evidence supports, and list it first. When the artifact is weak, that is a revise, route-back, or stop option, not approval.

Stop with an Adaptive Decision Ladder:

1. `Approve limited deployment (Recommended when gates are clear)` - expose the agent only within the named blast radius and oversight model.
2. `Reduce scope or authority` - useful when validation supports learning but not the proposed exposure.
3. `Route back to Stage 4` - needed when readiness evidence is insufficient.
4. `Route back to Stage 2 or 3` - needed when governance reveals a system or harness gap.
5. `Stop the effort` - appropriate when risks cannot be governed at an acceptable scope.
6. `Other (specify)`.

Record who approved what, what remains unresolved, and what would trigger rollback. Do not treat a deployment plan as live approval unless the user explicitly grants it.

## Evidence and Attribution Rules

Label claims as Fact, Inference, Assumption, or Unknown. Do not invent approvals, legal clearance, support capacity, security review, or operational readiness.

## Common Failure Modes

- Treating governance as documentation after launch.
- Launching to the full audience first.
- Naming no owner for oversight.
- Lacking rollback.
- Failing to define incident triggers.
- Treating a pilot as a soft launch to everyone.
- Asking Stage 6 to learn from evidence Stage 5 never planned to collect.

## Assets and Examples

Use `template.md`. See `examples/worked-example.md` and `examples/weak-example.md`.

## Sources

This skill draws on the ADLC findings, Productside's synthesis of published guidance on agent development. The findings link to the original sources; full citations are in the [bibliography](../../findings/bibliography.md).

### Evidence Base for Key Concepts

| Key concept | Findings guide | Where |
|---|---|---|
| Launch gate | [deployment.md](../../findings/deployment.md) | points 2 and 4, approval before production; an evaluation result can stop a release |
| Blast radius | [governance.md](../../findings/governance.md) | point 1, govern by risk tier; deployment.md, point 3, roll out gradually |
| Oversight model | [governance.md](../../findings/governance.md) | point 5, human oversight must be designed to work; fleet-ops.md, point 6 |
| Rollback path | [deployment.md](../../findings/deployment.md) | points 1 and 3, versioned units; rollback as a routing change |
| Incident trigger | [governance.md](../../findings/governance.md) | point 8, plan for the first incident before it happens |
| Observation contract | [observability.md](../../findings/observability.md) | points 5 and 9, quality and cost metrics; monitoring needs an owner; retirement.md, point 2, inventory with owners |

### Findings Used

- [deployment.md](../../findings/deployment.md)
- [fleet-ops.md](../../findings/fleet-ops.md)
- [governance.md](../../findings/governance.md)
- [observability.md](../../findings/observability.md)
- [retirement.md](../../findings/retirement.md)
- [Productside ADLC working model](../../findings/adlc-working-model.md)

### Method and Terms

- [Guided Context Capture](../../reference/guided-context-capture.md)
- [ADLC Glossary](../../reference/glossary.md)

The findings label claims Fact, Inference, Hypothesis, or Unknown. This skill uses Assumption where the findings say Hypothesis. Much of the published guidance is vendor or practitioner opinion; treat it as Inference unless the findings mark it Fact.
