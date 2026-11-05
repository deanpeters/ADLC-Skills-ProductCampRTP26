# Worked Example: Agent Intent Brief

Synthetic example. All details are invented for teaching.

This is one stage of a single running example: a customer support assistant taken through all six ADLC stages. The examples across the six stage skills follow the same synthetic case, including a route back at Stage 4. The scenario builds on the Customer Support Assistant in Productside's [Evals for Product Managers](https://github.com/deanpeters/evals-for-product-managers) kit.

**Opening:** "We will run ADLC Stage 1 and produce an Agent Intent Brief. I will use what you already supplied, ask no more than seven context questions, and stop before system design. Choose 1. Guided, 2. Context dump, or 3. Best guess." Mode chosen: **Context dump**.

**Extraction**

- Known: ticket volume up 30 percent and first-response time doubled since the spring release (director statement); most tickets are how-to and account questions; 400-article help center owned by support content; refunds only through billing specialists.
- Assumed: help-center articles are current enough to answer from.
- Missing: what share of tickets the help center fully answers; who reviews escalations.
- Conflicting: none.

Gap question asked (one): "What share of last quarter's tickets were tagged how-to or account?" Answer supplied by the case owner: about 55 percent.

## Context

- Decision this brief serves: design a pilot.
- Actor: customer using the in-product help widget; support agents receive escalations.
- Workflow: first response to how-to and account questions.
- Trigger: a customer opens the help widget and asks a question.

## Intent

- Desired human outcome: customers with how-to and account questions get a correct answer in under a minute, and support agents spend their time on billing, security, and cancellation cases.
- Agent job: answer how-to and account questions from approved help-center content, cite the article used, and hand off to a person when required.
- Non-goals: refunds, credits, account changes, plan changes, troubleshooting outside the help center.
- First version boundary: English sessions; how-to and account topics only.

## Autonomy And Authority

- Autonomy level: act within limits. The assistant answers directly, but only from approved content.
- Allowed actions: read approved help-center articles and policy documents; reply in the widget; create a handoff to the human queue with a summary.
- Human approvals: none for answering within scope; all refunds and credits go to billing specialists.
- Stop conditions: any answer that invents a policy or promises a refund halts expansion and routes back; escalation that fails to reach a person.
- Unacceptable failures: promising or implying refund eligibility; inventing policy, prices, or steps; failing to escalate a security issue.

## Success Evidence

- Behavior evidence: at least 90 percent of sampled answers judged good against the support scenario rules, and zero invented policies.
- Product and workflow evidence: median first response for in-scope questions under one minute; how-to tickets reaching agents fall; customer satisfaction on assisted sessions no worse than today.

## Evidence Ledger

| Claim | State | Basis |
|---|---|---|
| Volume up 30 percent, response time doubled | Fact | Director statement with ticket history supplied |
| About 55 percent of tickets are how-to or account | Fact | Case owner answer from tagged history |
| Help center answers those questions accurately | Assumption | Not yet checked; articles may be stale |
| An assistant will cut first-response time | Assumption | Plausible; no evidence yet |
| Refunds require a billing specialist | Fact | Supplied refund policy |

## Decision

- Recommendation: approve this brief.
- Ladder offered: 1. Approve this Agent Intent Brief (Recommended); 2. Revise the intent; 3. Return to discovery; 4. Stop the agent effort; 5. Other.
- Human decision: approve .
- Unresolved disagreements: none recorded.
- Next ADLC stage: Stage 2, only when asked.
