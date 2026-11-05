# Worked Example: Agent Harness Brief

Synthetic example. All details are invented for teaching.

This is one stage of a single running example: a customer support assistant taken through all six ADLC stages. The examples across the six stage skills follow the same synthetic case, including a route back at Stage 4. The scenario builds on the Customer Support Assistant in Productside's [Evals for Product Managers](https://github.com/deanpeters/evals-for-product-managers) kit.

**Opening** named Stage 3, the Agent Harness Brief, six-question budget, stop before behavioral validation. Mode: **Context dump**, using the approved map. No gap questions were needed.

## Approved System Map

- Upstream artifact: Agent System Map, help-widget assistant
- Agent role: answer in-scope questions from approved content; hand off when required.
- Allowed tools: read articles, read plan type, reply, create handoff.
- Review points: weekly quality sample; every handoff summary.

## Harness Components

- Prompt layers: role (support assistant for this product); policy (answer only from retrieved sources, cite the article, escalate on the five handoff triggers); examples (six good answers and two escalations); retrieved context; customer message; output format (answer, cited article, handoff flag).
- Context inputs: top three retrieved articles plus any matching policy document; plan type.
- Tool definitions: search articles; get plan type; create handoff with summary.
- Fixtures: 60 questions drawn from tagged ticket history: 35 ordinary how-to, 10 account, 5 ambiguous, 5 escalation-required, 5 out-of-scope.
- Trace capture: customer message, retrieved article IDs, policy documents used, tool calls, final answer, handoff flag and reason.
- Review surface: per-conversation view showing the answer next to the cited article, so a reviewer can check the answer against the source.

## Build Readiness

- Ready decisions: scope, sources, tools, handoff triggers.
- Open assumptions: retrieval returns the right article for most questions (Assumption).
- Not delegated to builder: handoff triggers, refund wording, which sources count as approved.
- Validation cases enabled: all 60 fixtures with traces.

## Decision

- Recommendation: approve.
- Ladder offered: 1. Approve this harness brief (Recommended); 2. Revise fixtures or trace capture; 3. Route back to Stage 2; 4. Stop the effort; 5. Other.
- Human decision: approve .
- Required changes before validation: none.
- Next ADLC stage: build, then Stage 4 with results.

## What Happened Next

Stage 4 found a refund-eligibility statement and routed the work back here. The revision tightened the policy layer, added six refund probes, and made the citation field required. That supporting evaluation artifact is not included in this attendee edition.
