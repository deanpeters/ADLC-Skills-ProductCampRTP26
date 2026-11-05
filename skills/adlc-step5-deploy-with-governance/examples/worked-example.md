# Worked Example: Governed Deployment Plan

Synthetic example. All details are invented for teaching.

This is one stage of a single running example: a customer support assistant taken through all six ADLC stages. The examples across the six stage skills follow the same synthetic case, including a route back at Stage 4. The scenario builds on the Customer Support Assistant in Productside's [Evals for Product Managers](https://github.com/deanpeters/evals-for-product-managers) kit.

**Opening** named Stage 5, the Governed Deployment Plan, seven-question budget, stop before live operation. Mode: **Context dump**. Gap question asked (one): "Who can switch the assistant off outside business hours?" Answer: the on-call support operations lead.

## Validation Basis

- Upstream artifact: Validation Pack, second pass
- Passed: 62 of 66 cases, zero hard stops, after one route back.
- Unresolved: two missing citations, two unnecessary escalations, untested on live traffic.

## Launch Scope

- Deployment shape: limited pilot.
- Audience: 10 percent of English help-widget sessions.
- Workflow: how-to and account topics only; all else hands off.
- Blast radius: at most about 900 conversations a week; no consequential actions possible.
- Duration: four weeks.
- User disclosure: the widget says the customer is talking to an AI assistant and shows how to reach a person.

## Gates And Oversight

- Launch gates: refund probes pass on the production build; handoff reaches the live queue in a test; support agents briefed on the handoff summary format; widget shows that the customer is talking to an AI assistant and how to reach a person.
- Approvers: support director (scope); support operations lead (technical readiness).
- Monitoring owner: support quality analyst.
- Review cadence: weekly 50-conversation sample, plus every flagged conversation.
- Review surface: answer next to cited article.

## Rollback And Incidents

- Rollback path: turn off the pilot flag; the widget returns to the current contact form within minutes.
- Incident triggers: any refund statement or invented policy; any unescalated security question; weekly sample below 42 of 50; handoff failures.
- Communication path: support director informs customer-facing leads; affected customers are contacted by a support agent.
- Authority reduction path: narrow to how-to topics only.

## Observation Contract

- Trace sample: 50 conversations a week, plus all flagged ones.
- Feedback source: thumbs up or down in the widget; agent notes on handoffs.
- Outcome signal: first-response time for in-scope questions; escalation rate (expected about 15 percent); satisfaction on assisted sessions.
- Stage 6 decision date: end of week 4.

## Retirement Basics

- Owner who can retire the agent: support director.
- Inventory record: company agent inventory, entry "help-widget assistant, v2".
- Where credentials and tool permissions are granted: help-center search key; read-only billing-plan lookup; support-queue handoff integration.
- Retirement review triggers: sample quality below threshold for two consecutive months; help-center platform change; model withdrawal notice.

## Decision

- Recommendation: approve limited deployment.
- Ladder offered: 1. Approve limited deployment (Recommended); 2. Reduce scope or authority; 3. Route back to Stage 4; 4. Route back to Stage 2 or 3; 5. Stop the effort; 6. Other.
- Human decision: approve limited deployment .
- Unresolved launch risks: answers to questions the help center does not cover.
- Next ADLC stage: Stage 6 at the end of week 4.
