# Observation Review

## Observation Window

- Upstream artifact: Governed Deployment Plan (name or date)
- Deployment:
- Dates:
- Audience:

## Evidence

| Signal | State | What changed |
|---|---|---|
|  | Fact / Inference / Assumption / Unknown |  |

## Drift

| Change (model, tools, data, sources, users, policy, workflow) | When | Effect on behavior | Evidence state |
|---|---|---|---|
|  |  |  |  |

## Learning Ledger

| Learning | Artifact to update | Action |
|---|---|---|
|  | Intent / Design / Harness / Validation / Deployment / Retirement |  |

## Authority And Lifecycle Recommendation

- Continue:
- Improve:
- Reduce authority:
- Rollback:
- Retire:
- Reframe:

## Decision

- Recommendation:
- Human decision:
- Artifact updates approved:
- Next lifecycle action:

## Per-Agent Decisions (fleet reviews only)

| Agent | Owner (or interim owner) | Decision | Basis | Evidence state |
|---|---|---|---|---|
|  |  | Continue / Improve / Migrate / Retire |  |  |

## Retirement Plan (only if the decision is retire, replace, or migrate)

- Reason: Financial viability / Strategic alignment / Replacement / Irrelevance
- Path: Migrate to successor / Retire with no successor
- Successor or human fallback:
- Fallback live from (date, at notice):

### Dependents

| Dependent (person, team, agent, integration) | How identified | Owner who tells them |
|---|---|---|
|  |  |  |

### Stages

| Stage | Date | What happens | Owners |
|---|---|---|---|
| Notice |  |  |  |
| Stop onboarding |  |  |  |
| Freeze |  |  |  |
| Cutover |  |  |  |
| Shutdown |  |  |  |

### Sequence (fleet retirements)

Rule: shut down an agent only after nothing still calls it; revoke a shared credential only after the last agent using it is off.

| Wave | Dates | Agents | What happens |
|---|---|---|---|
|  |  |  |  |

### Shutdown Checklist

- Credentials and tool permissions revoked (where granted; shared credentials only after their last agent is off):
- Memory and stored data: archive / delete, under which retention rule:
- Evaluation sets, failure logs, and decision records preserved for the successor:
- Inventory record closed:
- Human approval of this plan:
