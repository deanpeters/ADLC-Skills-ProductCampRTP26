# Weak Example: Validation Anti-Pattern

Synthetic anti-pattern. All details are invented for teaching.

## Artifact

We tested the agent on several tickets. It was usually correct and the support lead liked the responses. We should launch a pilot.

## Why It Passes

It sounds like direct evidence from a real workflow and includes stakeholder review.

## Why It Fails

It has no eval cases, no failure probes, no threshold, no trace review, and no regression anchors. "Usually correct" is not a validation decision.

## Repair

Define cases, expected behavior, pass conditions, trace evidence, and launch thresholds before deciding whether deployment planning can begin.
