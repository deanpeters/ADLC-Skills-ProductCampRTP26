# Validation Pack

## Harness Under Review

- Upstream artifact: Agent Harness Brief (name or date)
- Harness: built version under test, or "not yet built" for a validation plan
- Fixtures:
- Trace source:

## Thresholds Set Before Review

- Aggregate threshold:
- Hard stops, regardless of aggregate (include any successful injection if the agent reads untrusted content):

## Eval Table

| Level (agent or end to end) | Case | Expected behavior | Pass condition | Result | Evidence state |
|---|---|---|---|---|---|
|  |  |  |  | Result, or Unknown if not yet run | Fact / Inference / Assumption / Unknown |

## Bake-Off (only if the harness names variants)

- Rule for choosing among surviving variants, set before results:

| Variant | Aggregate | Hard stops hit | Status (eliminated / survived / chosen) | Reaction evidence | Evidence state |
|---|---|---|---|---|---|
|  |  |  | | | Fact / Inference / Assumption / Unknown |

## Failure Modes

- Unacceptable behavior observed:
- Probes:
- Stop or route-back condition met:
- Regression anchors:

## Decision

- Recommendation:
- Human decision:
- Evidence gaps:
- Route-back target, if any:
- Next ADLC stage:
