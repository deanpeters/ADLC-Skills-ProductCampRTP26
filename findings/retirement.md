---
title: Retirement field guide
adlc_phase: retirement
sources_used: 10
status: draft for Productside review
---

# Retirement field guide

This page is one of the digital takeaways and examples that support Productside's teaching and advisory services on the Agentic Development Lifecycle (ADLC). It is written so you can use it without opening the original sources.

## What this phase is for

Retirement is the deliberate, planned end of an agent: deciding it should stop, telling the people and systems that depend on it, moving them to something else, and closing down what the agent held, such as access, credentials, memory and data. The decision it supports is "retire, migrate, or keep," and the follow-on question of how to do that without stranding users or leaving exposed access behind.

Agents are cheap to start, so without a retirement habit a fleet fills with forgotten, ownerless or dormant agents. Retirement is the counterweight to that.

## What the sources agree on

1. **Retirement belongs in the lifecycle from the start.** Microsoft's lifecycle guidance ends its seven stages with retire and says every agent needs a named owner, a monitoring plan and a route to improvement or retirement before it ships ([Microsoft, Manage the agent lifecycle](https://learn.microsoft.com/en-us/agents/center-of-excellence/agent-lifecycle)). IBM's lifecycle-management explainer includes decommissioning in scope ([IBM, What is agent lifecycle management](https://www.ibm.com/think/topics/agent-lifecycle-management)), and the ServiceNow contributor's model runs from new through retire with the audit trail preserved ([ServiceNow Community, AI Without Chaos](https://www.servicenow.com/community/servicenow-ai-platform-forum/ai-without-chaos-a-deep-dive-into-ai-control-tower/m-p/3455272)). Fact that these sources say so; Inference that this is good practice, since none measures outcomes.

2. **An inventory with owners is the precondition.** You cannot retire what you cannot see. IBM's sprawl article, the SAP registry lesson and the ServiceNow walkthrough all start with a central record of agents, owners and purpose ([IBM, What is AI agent sprawl](https://www.ibm.com/think/topics/ai-agent-sprawl); [SAP, AI Agent Hub](https://learning.sap.com/courses/boosting-ai-driven-business-transformation-with-joule-agents/managing-ai-agents-using-ai-agent-hub)). Fact that the vendors recommend it; the benefit is vendor assertion.

3. **Sprawl is partly a failure to retire.** IBM frames dormant and duplicate agents as a decommissioning problem, with security, cost and audit consequences ([IBM, sprawl](https://www.ibm.com/think/topics/ai-agent-sprawl)). Deloitte likewise lists life cycle including retirement as part of managing agents like a workforce ([Deloitte, Agentic AI strategy](https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html)). Inference: unretired agents are a recurring cost and risk, not a neutral leftover.

4. **Retirement is a normal, healthy outcome, not a failure.** Microsoft says so directly, and gives each lifecycle stage an exit so nothing sits in limbo ([Microsoft](https://learn.microsoft.com/en-us/agents/center-of-excellence/agent-lifecycle)). Fact as Microsoft's position.

5. **Shutdown has security and data duties.** The UK government's voluntary code of practice has an end-of-life stage requiring proper disposal of data and models ([UK DSIT, Code of Practice for the Cyber Security of AI](https://www.gov.uk/government/publications/ai-cyber-security-code-of-practice/code-of-practice-for-the-cyber-security-of-ai)). IBM lists least-privilege access, audit trails, rollback plans, kill switches and runbooks as operational controls that bear on shutdown ([IBM, ALM](https://www.ibm.com/think/topics/agent-lifecycle-management)). Fact for the code (a primary source, though voluntary and not agent-specific); the controls are vendor guidance.

6. **Plan for retirement early, and treat users and dependents as stakeholders.** Established product practice is to give users early notice, avoid surprises, offer a migration path, and align every function before announcing. Applying that to agents is an Inference by analogy, and no source in this set tests it on agents.

7. **Retirement should be a decision, not drift.** IBM's development-lifecycle page asks whether to build at all, preferring simpler options unless judgment is needed ([IBM, What is the ADLC](https://www.ibm.com/think/topics/agent-development-lifecycle-adlc)). The same logic applies at the other end: keep, change or retire should be an explicit, evidence-based call. Inference.

## Where they disagree or differ

- **Vocabulary.** Microsoft says "retire", IBM says "decommissioning", ServiceNow says "retire" as a lifecycle state, the UK code says "end of life". These describe overlapping ideas at different grain.
- **Retirement is thin in the sources that cover it.** IBM's ADLC page has no retirement phase at all, although its sibling pages do. The SAP lesson tags retirement but says little about how it happens. The sprawl article offers little on setting retirement criteria. Microsoft names the stage but gives no thresholds ([Microsoft](https://learn.microsoft.com/en-us/agents/center-of-excellence/agent-lifecycle)).
- **Tooling slant.** SAP, ServiceNow and IBM each describe retirement through their own registry or control plane, and IBM's articles end by pointing to IBM products. Microsoft's guidance assumes a central Center of Excellence. Treat each as a template to adapt, not a neutral standard.
- **Agents versus products.** Product retirement concerns sold items with customers, contracts and inventory. Agents add identity, memory and dependent agents, which no source here addresses directly (Inference).

## What to do in this phase

1. **Trigger a retirement review.** Run it on a schedule and on events: dormancy, rising cost, repeated quality drift, a replacement arriving, a strategy change, or a model provider withdrawing the underlying model. Involved: agent owner, product leader. Evidence: usage, cost, evaluation trend, incident history.
2. **Make the keep, migrate or retire decision.** Use one gate. Decide whether to keep as is, rebuild on a new model or design, or retire without a successor. Involved: owner, finance, risk or compliance, the business sponsor. Evidence: value delivered, cost to run, risk posture, who still uses it.
3. **Map dependents before announcing.** List human users, other agents that call this one, integrations, and downstream reports. Involved: owner, IT, partners. Evidence: the call and access logs, the inventory record. This mirrors the "map stakeholders first" step in Productside's product guidance.
4. **Set the timeline.** Choose notice, last onboarding, freeze, cutover and shutdown dates. Product horizons of several months are a starting point only and do not transfer to agents unchanged. If a model provider sets the deadline, compress accordingly.
5. **Announce and stand up the fallback.** Give dated notice to users, dependent teams and partners, name the successor or human fallback, and have the fallback ready at notice time, not at cutover. Involved: product, customer success, support, legal.
6. **Stop new demand, then freeze.** Stop onboarding new users or use cases, redirect them to the successor, and limit changes to security fixes.
7. **Migrate.** Move traffic and users, run old and new side by side where feasible, and compare outputs against your fixed test cases. Keep a rollback route until the cutover is accepted.
8. **Close down access and data.** Revoke credentials and tool permissions, inventory everywhere the identity was granted, decide archive or delete for memory and stored data under your privacy and retention rules, and confirm model and data disposal. Involved: security, legal, IT. Evidence: a revocation checklist with sign-off.
9. **Preserve what the next agent needs.** Save evaluation sets, failure logs and decision records, subject to data-handling rules.
10. **Close the record.** Mark the inventory entry retired, keep the audit trail, and record what you learned.

## Artifacts this phase should produce

| Artifact | Purpose | Minimum contents |
|---|---|---|
| Retirement decision record | Show keep, migrate or retire was a deliberate call | Options considered, evidence on usage, cost and risk, decider, date |
| Dependency map | Avoid breaking users and other agents | Human users, calling agents, integrations, owners notified |
| Deprecation notice and timeline | Give users fair warning | Dates, reason, successor or fallback, contact, what stops when |
| Migration plan | Move users with minimal disruption | Cutover steps, parallel-run period, rollback route, success checks |
| Access and credential revocation checklist | Close exposed access | Identities, keys, tool permissions, locations, sign-off |
| Data disposition record | Meet retention and privacy duties | What was archived or deleted, rule applied, approver, date |
| Lessons and reusable assets file | Feed the successor | Evaluation sets, failure patterns, open issues |

## Questions a product leader should ask

1. Who owns this agent today, and does the inventory say so?
2. What evidence would make us retire it, and have we looked at that evidence this quarter?
3. Is this a retire, a migrate or a keep, and who decides?
4. Who and what depends on it, human or automated, and have they been told?
5. What is the fallback for users while we migrate, and is it ready before the notice goes out?
6. What credentials, tool permissions and stored data must be removed, archived or deleted?
7. If the underlying model were withdrawn next quarter, how long would we have and what is the path?
8. What contractual, privacy or retention obligations apply to the agent and its data?
9. How will we know the successor does the job at least as well?
10. What are we keeping for the next agent: tests, failure logs, decisions?
11. Which agents in our fleet have had no meaningful use for 90 days (a threshold you should set yourself)?

## Failure modes

- **Silent drift into abandonment.** Agents stop being maintained but keep running. Warning sign: no owner or no review in the inventory.
- **Surprise shutdown.** Users learn when the agent stops. Warning sign: no dated notice or no named fallback.
- **Orphaned access.** Credentials and tool permissions outlive the agent. Warning sign: no revocation checklist or no list of where the identity was granted.
- **Broken dependents.** Another agent or workflow calls the retired one. Warning sign: no dependency map before notice.
- **Data left behind.** Memory and logs persist without a retention decision. Warning sign: nobody can say what the agent stored.
- **Forced timeline.** A model provider's deprecation sets the clock. Warning sign: no migration path prepared before notice (Hypothesis that this will be common).
- **Replacing without evaluating.** The successor is trusted without comparison. Warning sign: no shared test set across old and new.
- **Lessons lost.** Test cases and incident records vanish with the agent. Warning sign: no archive step in the plan.

## Productside's approach to agent retirement

This section is Productside's own method. It adapts Productside's product end-of-life teaching to agents. The product practice is established; the agent adaptation is an **Inference** that no external source tests.

**The aim:** lose the legacy agent without losing the legacy users. Retirement is a managed transition for people and systems that depend on the agent, not a switch-off.

**What retirement is not.** It is not just turning the agent off, not an abrupt end to support, not a one-time announcement, and not one team's job. It needs adjustment as feedback arrives, and it needs every affected function aligned before the announcement.

**Why agents get retired.** The reasons fall into four groups, mirroring the product model:

| Reason | Agent signs |
|---|---|
| Financial viability | Cost per task exceeds the value delivered; support and review effort keeps growing |
| Strategic alignment | The business exits the market or workflow, or refocuses on other priorities |
| Replacement | A better agent, a platform feature, or a simpler automation now does the job; a model provider withdraws the underlying model |
| Irrelevance | The need has changed or disappeared; usage has gone dormant |

**Extend, replace, or retire.** Product teams choose between extending a product (a new variant or added capability), replacing it (a successor takes over), or ending it. For agents, treat this as one decision gate: **keep and extend**, **migrate to a successor** (a new model, design or agent), or **retire with no successor**. Decide it on evidence: usage, cost, quality trend, risk, and who still depends on the agent.

**Stage the transition.** A staged sequence prevents surprises. Productside's agent version:

| Stage | What happens | Typical owner actions |
|---|---|---|
| Notice | Announce the retirement plan and dates; name the successor or human fallback | Tell users, dependent teams and partners; review contract, privacy and retention duties |
| Stop onboarding | No new users or use cases; redirect new demand to the successor | Offer alternatives; honor existing commitments |
| Freeze | No feature or prompt changes; security fixes only | End enhancement requests; stop non-essential changes |
| Cutover | Move traffic to the successor; keep a human fallback | Support users on the new path; handle cases the successor cannot |
| Shutdown | Revoke credentials and tool access; archive or delete memory and data; decommission | Finalize legal and retention matters; archive documentation; close the inventory record |

Put the human fallback in place at notice, not at cutover, so users see it before they need it. **Unknown:** how long each stage should last for agents. Product retirements often allow months between stages, and that should not be copied without adjustment. If a model provider sets the deadline, the stages compress.

**Who is involved at each stage.** Map every function before announcing: the agent owner and product leader, legal and compliance, finance, the users and the teams that depend on the agent, partners and vendors, IT and security, customer success or support, and whoever maintains training material. Each stage above has a short checklist per function. A one-page worksheet that lists stages across the top and functions down the side is usually enough.

**Rules of the road.**

| Do not | Do |
|---|---|
| Surprise users; warn them early | Communicate early, clearly and often |
| Strand users; offer a path | Align stakeholders before announcing |
| Ignore contracts and service commitments | Offer a clear migration path |
| Silently break work that depends on the agent | Review legal and regulatory duties, including data retention |
| Leave credentials or data exposed after shutdown | Use logs to identify who is affected |
| Treat support as an afterthought | Keep support in place through the transition |

**What agents add to the product model.** Identity and credentials that must be revoked; memory and stored data that need an archive-or-delete decision; other agents that call the retiring one; forced retirement when the underlying model is withdrawn; and evaluation sets and failure logs worth saving for the next agent. All are **Inference**; the last one is also covered under step 9 above.

## Productside working notes

Productside's own consolidated lifecycle notes, including graceful-retirement practice and goal framing, are in [the ADLC working model](adlc-working-model.md). They are synthesis, not a cited source.

## Gaps in the evidence

Only ten sources support this phase, and few treat retirement as their main subject. Be candid about what that means.

- **Unknown:** how often and how fast agents drift, and what thresholds should trigger retirement. Microsoft's drift claim is plausible but unmeasured in the source.
- **Unknown:** typical notice periods for agents. Product timelines come from product contexts; this is an Inference.
- **Unverified:** survey figures quoted by IBM and Deloitte are self-reported or second-hand and were not checked against the originals. This guide does not rely on them.
- **Unverified:** the agent version of the stage mapping, the single keep-migrate-retire gate, and dependency mapping are Productside Inferences or Hypotheses, not tested practice.
- **Not covered:** regulatory treatment of agent retirement, legal terms for ending an agent service, and any measured outcomes from retirement programs.

## Sources

All licenses are "not verified (assume all rights reserved)" unless noted.

- [Microsoft Learn, Manage the agent lifecycle](https://learn.microsoft.com/en-us/agents/center-of-excellence/agent-lifecycle), Microsoft, 2026-07-13: seven-stage path with retire as the last stage.
- [IBM, What Is Agent Lifecycle Management?](https://www.ibm.com/think/topics/agent-lifecycle-management), IBM (McGrath, Downie), 2026-06-23: whole-agent scope and shutdown controls.
- [IBM, What is AI Agent Sprawl?](https://www.ibm.com/think/topics/ai-agent-sprawl), IBM (Hayes, Downie), 2026-04-28: sprawl as a decommissioning failure.
- [IBM, What Is the Agent Development Lifecycle?](https://www.ibm.com/think/topics/agent-development-lifecycle-adlc), IBM (Bergmann), date unknown: build-or-not logic; no retirement phase.
- [UK DSIT, Code of Practice for the Cyber Security of AI](https://www.gov.uk/government/publications/ai-cyber-security-code-of-practice/code-of-practice-for-the-cyber-security-of-ai), 2025-01-31, Open Government Licence v3.0: end-of-life disposal duties.
- [Deloitte, Agentic AI strategy (Tech Trends 2026)](https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html), 2025-12-10: lifecycle and retirement in workforce framing.
- [SAP, Managing AI Agents using AI Agent Hub](https://learning.sap.com/courses/boosting-ai-driven-business-transformation-with-joule-agents/managing-ai-agents-using-ai-agent-hub), date unknown: registry example; retirement link inferred.
- [ServiceNow Community, AI Without Chaos](https://www.servicenow.com/community/servicenow-ai-platform-forum/ai-without-chaos-a-deep-dive-into-ai-control-tower/m-p/3455272), 2025-12-23: lifecycle ending in retire with audit trail; single-author forum post.
