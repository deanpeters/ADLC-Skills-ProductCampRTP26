---
name: adlc-step6-observe-and-improve
description: Review live agent traces, incidents, feedback, drift, and outcomes to decide whether to continue, change, rollback, or retire.
license: CC-BY-NC-SA-4.0
argument-hint: "[live traces, feedback, incidents, or monitoring notes]"
intent: >-
  Help Product Managers turn operational evidence from a live or piloted agent
  into lifecycle decisions: continue, change, reduce authority, roll back, retire,
  or reframe the agent intent.
type: interactive
theme: agent-development-lifecycle
phase: 6
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
  - "Reviewing live agent traces and feedback"
  - "Deciding what to improve, reduce, rollback, or retire"
  - "Closing the learning loop back into intent, design, harness, or evals"
scenarios:
  - "A pilot has run and the team needs to decide what changes"
  - "An incident or drift signal suggests the agent should be revised or stopped"
evidence-required:
  - "Deployment plan and launch gates"
  - "Traces, incidents, feedback, and outcome signals"
  - "Known changes to users, tools, policies, or context"
produces:
  - "Observation Review"
  - "Learning and change ledger"
  - "Lifecycle decision record"
estimated-time: "45-90 min"
group-size: "1-8"
depends-on:
  - adlc-step5-deploy-with-governance
combine-with:
  - adlc-step1-frame-intent
source-basis:
  - "ADLC findings: observability field guide"
  - "ADLC findings: feedback and maintenance field guides"
  - "ADLC findings: retirement field guide, including Productside's approach to agent retirement"
  - "ADLC findings: fleet operations field guide"
sources:
  - https://learn.microsoft.com/en-us/agents/center-of-excellence/agent-lifecycle
  - https://www.ibm.com/think/topics/agent-lifecycle-management
  - https://www.ibm.com/think/topics/ai-agent-sprawl
  - https://www.gov.uk/government/publications/ai-cyber-security-code-of-practice/code-of-practice-for-the-cyber-security-of-ai
interface:
  display_name: "Observe And Improve"
  short_description: "Review traces and decide changes"
  brand_color: "#00E874"
  default_prompt: "Use $adlc-step6-observe-and-improve to turn these live traces and feedback into an Observation Review and stop at the lifecycle decision."
  allow_implicit_invocation: true
---

# Observe And Improve

## Purpose

Turn live traces, feedback, incidents, drift signals, and outcome evidence into an Observation Review. This stage decides whether to continue, improve, reduce authority, rollback, retire, or reframe the agent.

Observation is not a dashboard ritual. The Product Manager job is to turn operational evidence into a lifecycle decision and update the artifact that should change. If nothing changes, the team should be able to say why continuing is still responsible.

## When to Use It

Use this skill after a pilot or live deployment. Use it when monitoring produces evidence, when a model or tool changes, when incidents occur, or when stakeholders want to expand the agent.

Do not use it to rubber-stamp expansion without evidence. If observation is missing, report the gap.

It also works for a fleet: several agents reviewed together because of a shared event, such as a platform shutdown, a sprawl review, or a model withdrawal that affects many agents. In a fleet review, work from the agent inventory and give a decision for each agent, not one decision for all.

## Input

Use the Governed Deployment Plan, launch gates, traces, incidents, user feedback, operator review notes, outcome measures, drift signals, and known context changes.

Anything supplied with the invocation, attachments, or earlier conversation counts as context already given. Do not ask the user to repeat it.

If the deployment did not collect usable evidence, say that plainly. Do not replace missing traces or outcome signals with general sentiment.

**Example invocation:** `Use $adlc-step6-observe-and-improve with these pilot traces, coordinator notes, and two incident reports.`

## Key Concepts

Technical terms used here are defined in the [ADLC Glossary](../../reference/glossary.md).

**Operational evidence** - What happened in real use: traces, incidents, feedback, outcomes, and workarounds. It is stronger than expectation but still needs interpretation.

*Violation signal:* The review relies on stakeholder impressions while ignoring available traces or incidents.

**Drift signal** - A change in model, tools, policies, users, data, or workflow that may alter behavior.

*Violation signal:* The agent is treated as stable even though its context changed.

**Learning ledger** - A record of what the team learned and which artifact should change. Learning must land somewhere.

*Violation signal:* The review lists observations but no change to intent, design, harness, evals, deployment, or retirement.

**Authority adjustment** - Increasing, reducing, or freezing what the agent may do based on evidence. Authority should be earned and reversible.

*Violation signal:* Expansion is proposed because the pilot was popular, not because behavior evidence supports more authority.

**Retirement path** - A plan to stop or replace the agent when it no longer serves the intent or cannot be governed. Retirement is lifecycle work.

*Violation signal:* The only choices are continue or improve, even when evidence shows the agent should stop.

**Staged retirement** - Retiring an agent is a managed transition for the people and systems that depend on it, not a switch-off. The aim is to lose the legacy agent without losing the legacy users. It runs in stages: notice, stop onboarding, freeze, cutover, shutdown.

*Violation signal:* The plan says "turn it off on Friday" with no notice, no successor or human fallback, and no step to revoke credentials or settle stored data.

**Fleet decision** - When several agents are reviewed together, each agent gets its own decision (continue, improve, migrate, retire), its own evidence, and an owner. The fleet plan then orders the work so that no agent loses something it still depends on.

*Violation signal:* One decision covers every agent, or a plan shuts down an agent that another agent still calls, or revokes a credential other agents still use.

**Artifact update** - The specific upstream artifact that changes because of learning: intent, system map, harness, validation pack, deployment plan, or retirement plan.

*Violation signal:* The review says "improve the agent" without naming which lifecycle artifact becomes false or incomplete.

## Guided Context Capture

Follow [Guided Context Capture](../../reference/guided-context-capture.md).

Begin with: "We will run ADLC Stage 6 and produce an Observation Review. I will use the deployment plan and observed evidence, ask no more than seven context questions, and stop at the lifecycle decision. Choose 1. Guided, 2. Context dump, or 3. Best guess."

Offer Guided, Context dump, and Best guess modes. Use an Adaptive Decision Ladder at the lifecycle gate. Anything supplied earlier must be reused.

If an approved Solution Hypothesis exists, check each of its validation measures against what was observed, as described in the [Solution Hypothesis](../adlc-util-solution-hypothesis/SKILL.md) utility. A measure that held is evidence about value, not a reason to expand authority.

In Guided mode, ask one at a time and skip answered questions:

1. `Observation Q1/7` - What deployment window, audience, and authority level are under review?
2. `Observation Q2/7` - Which traces, incidents, feedback, and outcomes are available?
3. `Observation Q3/7` - What changed in users, workflow, tools, model, data, or policy?
4. `Observation Q4/7` - Which expected behaviors held up, and which failed?
5. `Observation Q5/7` - What authority change is being considered, if any?
6. `Observation Q6/7` - Which lifecycle artifact must be updated based on the evidence?
7. `Observation Q7/7` - What condition would justify continuing, reducing, rolling back, retiring, or reframing?

In Context dump mode, extract `Evidence / Incidents / Drift / Outcomes / Learning / Artifact updates / Decision`. In Best guess mode, draft the review and mark all unavailable monitoring evidence as Unknown.

## What It Produces

- Observation Review
- Learning and change ledger
- Authority adjustment recommendation
- Lifecycle decision record
- Retirement Plan, when the human chooses retire, replace, or migrate

When a folder is set, save as `stage-6-observation-review.md`, plus `stage-6-retirement-plan.md` when retiring, following [Saving Artifacts](../../reference/guided-context-capture.md#saving-artifacts).

The review must land learning somewhere. A list of observations without a change, explicit continue rationale, or retirement decision is incomplete.

## Workflow

1. **Confirm the deployment under review.** State scope, dates, authority level, and observation contract from Stage 5.
2. **Inventory evidence.** Separate traces, incidents, feedback, outcomes, and missing evidence.
3. **Separate facts from interpretations.** Treat sentiment and anecdotes as signals, not verdicts.
4. **Identify drift.** Name changes in model, tools, data, users, policy, workflow, or context.
5. **Compare behavior to validation.** Say which regression anchors held, failed, or need revision.
6. **Map learning to artifacts.** Intent, system map, harness, validation pack, deployment plan, or retirement path.
7. **Recommend a lifecycle decision.** Continue, improve, reduce authority, rollback, retire, or reframe.
8. **Present the lifecycle gate.**
9. **If the human chooses retire, replace, or migrate, draft the Retirement Plan.** Use the procedure below. Do not start it before the gate decision.

### Retirement Procedure

Use this only after the human has chosen retire, replace, or migrate at the lifecycle gate. Product practice for ending products is well established; applying it to agents is an Inference, so label the plan's assumptions.

1. **Confirm the reason.** Name which applies: financial viability (cost exceeds value), strategic alignment (the workflow or market is no longer a priority), replacement (a better agent, platform feature, simpler automation, or a withdrawn underlying model), or irrelevance (the need changed or usage went dormant).
2. **Confirm the path.** Keep and extend, migrate to a successor, or retire with no successor. If the path is keep, return to the improvement workflow.
3. **Map dependents before announcing.** Human users, teams, other agents that call this one, integrations, reports, and partners. Use call and access logs, not memory.
   - **Ownerless agents:** name an interim owner before any notice. No owner means no one can approve the retirement. Check usage first: an agent without an owner may still be in daily use.
   - **Dormant agents:** retire them only after checking logs for remaining callers and report reads.
4. **Set the stages and dates.**

   | Stage | What happens |
   |---|---|
   | Notice | Announce the plan and dates; name the successor or human fallback; review contract, privacy, and retention duties |
   | Stop onboarding | No new users or use cases; redirect new demand to the successor |
   | Freeze | No feature or prompt changes; security fixes only |
   | Cutover | Move traffic to the successor; run old and new side by side where feasible; keep a human fallback and a rollback route |
   | Shutdown | Revoke credentials and tool access everywhere they were granted; archive or delete memory and stored data under retention rules; close the inventory record |

   Stage durations for agents are Unknown. Do not copy product timelines unchanged. If a model provider sets the deadline, compress the stages and say so.

   **For a fleet, order the work across agents:**
   - Shut down an agent only after nothing still calls it. Move a coordinator and the specialists it calls together, or keep the specialists until the coordinator no longer calls them.
   - Revoke a shared credential only after the last agent using it is off. Find out which agents share it before planning. Give each successor agent its own identity.
   - For an agent with write access, set up the replacement source for anything that reads its output first, and revoke the old write access last, after the new path is accepted.
   - Group the work into waves with dates, and finish before any hard deadline with a buffer.
5. **Name an owner per function for each stage.** Agent owner, Product Manager, legal and compliance, finance, security and IT, support or customer success, the dependent teams, and whoever maintains training material.
6. **Put the human fallback in place at notice, not at cutover.** Users should see it before they need it.
7. **Preserve what the next agent needs.** Evaluation sets, regression anchors, failure logs, and decision records, subject to data-handling rules.
8. **Check the rules of the road.** Do not surprise users, strand users, ignore contracts or service commitments, silently break dependent work, or leave credentials or data exposed. Do communicate early and often, align stakeholders before announcing, offer a migration path, and keep support in place through the transition.
9. **Return the Retirement Plan for human approval.** The skill drafts the plan. It does not announce, revoke, or shut down anything.

## Human Decision Gate

Mark as recommended the option the evidence supports, and list it first. When the artifact is weak, that is a revise, route-back, or stop option, not approval.

Stop with an Adaptive Decision Ladder:

1. `Continue with targeted improvements (Recommended when evidence supports it)` - update named artifacts without expanding authority.
2. `Expand or increase authority` - only when behavior evidence and governance support it.
3. `Reduce authority or rollback` - appropriate when failures are manageable but exposure should shrink.
4. `Retire or replace` - appropriate when the agent no longer serves the intent or cannot be governed.
5. `Reframe by returning to Stage 1` - needed when the original intent was wrong.
6. `Other (specify)`.

Record the human lifecycle decision and the artifact updates it requires. Do not silently restart the loop.

## Evidence and Attribution Rules

Label claims as Fact, Inference, Assumption, or Unknown. Do not invent incident counts, outcome gains, user sentiment, trace findings, or approvals.

## Common Failure Modes

- Monitoring without decisions.
- Expanding authority because the pilot feels successful.
- Ignoring drift.
- Fixing symptoms without updating evals.
- Treating retirement as failure rather than responsible lifecycle management.
- Retiring abruptly: no notice, no fallback, no dependent map.
- Shutting down without revoking credentials or deciding what happens to stored data.
- Making one decision for a whole fleet instead of one per agent.
- Revoking a shared credential while agents still use it.
- Deleting an ownerless agent without checking whether anyone uses it.
- Expanding authority from popularity rather than evidence.
- Producing a monitoring summary with no lifecycle decision.

## Assets and Examples

Use `template.md`. See `examples/worked-example.md` and `examples/weak-example.md`.

## Sources

This skill draws on the ADLC findings, Productside's synthesis of published guidance on agent development. The findings link to the original sources; full citations are in the [bibliography](../../findings/bibliography.md).

### Evidence Base for Key Concepts

| Key concept | Findings guide | Where |
|---|---|---|
| Operational evidence | [observability.md](../../findings/observability.md) | points 1 and 2, healthy infrastructure is not a healthy agent; the trace is the basic unit |
| Drift signal | [maintenance.md](../../findings/maintenance.md) | points 1 and 4, agents drift rather than crash; sample production too |
| Learning ledger | [feedback.md](../../findings/feedback.md) | points 1 and 3, production traces as raw material; reviewed failures become permanent tests |
| Authority adjustment | [maintenance.md](../../findings/maintenance.md) | point 6, roll out gradually and keep a way back; governance.md, point 1 |
| Retirement path | [retirement.md](../../findings/retirement.md) | points 4 and 7, retirement is a normal outcome and a decision, not drift |
| Staged retirement | [retirement.md](../../findings/retirement.md) | section "Productside's approach to agent retirement"; points 5 and 6, shutdown duties and dependents as stakeholders |
| Fleet decision | [fleet-ops.md](../../findings/fleet-ops.md) | points 1, 2 and 8, inventory first; every agent needs a named owner and its own identity; retirement belongs to fleet operations |
| Artifact update | [maintenance.md](../../findings/maintenance.md) | points 3 and 5, every meaningful change re-runs evaluations; record which version produced which behavior |

### Findings Used

- [feedback.md](../../findings/feedback.md)
- [governance.md](../../findings/governance.md)
- [maintenance.md](../../findings/maintenance.md)
- [observability.md](../../findings/observability.md)
- [retirement.md](../../findings/retirement.md)
- [Productside ADLC working model](../../findings/adlc-working-model.md)

### Method and Terms

- [Guided Context Capture](../../reference/guided-context-capture.md)
- [ADLC Glossary](../../reference/glossary.md)

The findings label claims Fact, Inference, Hypothesis, or Unknown. This skill uses Assumption where the findings say Hypothesis. Much of the published guidance is vendor or practitioner opinion; treat it as Inference unless the findings mark it Fact.
