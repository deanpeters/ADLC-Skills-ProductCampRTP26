# Worked Example: Agent System Map

Synthetic example. All details are invented for teaching.

This is one stage of a single running example: a customer support assistant taken through all six ADLC stages. The examples across the six stage skills follow the same synthetic case, including a route back at Stage 4. The scenario builds on the Customer Support Assistant in Productside's [Evals for Product Managers](https://github.com/deanpeters/evals-for-product-managers) kit.

**Opening** named Stage 2, the Agent System Map, six-question budget, stop before harness generation. Mode chosen: **Context dump**, using the approved Stage 1 brief.

**Extraction:** Actors, context, tools, and handoffs are clear from Stage 1. Unknown: how long conversation transcripts are kept. Gap question asked (one): "What retention rule applies to help-widget transcripts today?" Answer: 90 days, per the existing privacy policy.

## Approved Intent

- Upstream artifact: Agent Intent Brief, help-widget assistant
- Outcome: correct answers in under a minute for how-to and account questions; agents focus on billing, security, and cancellations.
- Agent job: answer from approved help content, cite the article, hand off when required.
- Autonomy: act within limits.
- Stop condition: invented policy or refund promise; failed escalation.

## Actors And Handoffs

- User: customer in the help widget.
- Operator: support operations lead, who owns the assistant's configuration.
- Approver: support director approves scope changes; billing specialists alone approve refunds.
- Reviewer: support quality analyst, weekly samples.
- Affected party: customers who receive answers; support agents who receive handoffs.
- Escalation path: handoff to the existing human support queue with a conversation summary.

## Context, Tools, And Memory

| Surface | Purpose | Owner | Authority | Freshness / retention | Privacy concern |
|---|---|---|---|---|---|
| Help-center articles | Answer source | Support content team | Authoritative for how-to | Updated continuously; retired articles excluded | None |
| Policy documents | Answer source for account rules | Support operations | Authoritative when they conflict with articles | Reviewed quarterly | None |
| Customer's account plan (read) | Tailor answers to plan | Billing systems | Read only | Live | Account data; show only to that customer |
| Conversation transcript | Context and review | Support operations | Record only | 90 days, existing policy | Customer messages |

Tools: read articles; read plan type; reply; create handoff. Blocked: issue refunds or credits, change plan or account, send email.

Memory rule: no memory across conversations in v1. Transcripts kept 90 days for review, then deleted.

## Control Boundaries

- Allowed: answer in-scope questions from approved sources; create handoffs.
- Not allowed: refunds, credits, account or plan changes, statements of refund eligibility, answers from unapproved sources.
- Requires approval: none in v1, because the agent has no consequential actions.
- Handoff points: billing disputes, security, cancellations, upset customers, no confident source.
- Escalation owner: support operations lead.

## Decision

- Recommended design: single assistant with retrieval over approved content and a handoff tool. Simplest viable system.
- Alternative considered: a router plus separate billing and how-to agents. Rejected for v1: more cost and harder diagnosis, with no evidence that one assistant breaks down.
- Ladder offered: 1. Approve the simplest viable system map (Recommended); 2. Revise controls or handoffs; 3. Reduce autonomy; 4. Return to Stage 1; 5. Other.
- Human decision: approve .
- Next ADLC stage: Stage 3, only when asked.
