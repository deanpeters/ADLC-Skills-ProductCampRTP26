# Weak Example: Harness Anti-Pattern

Synthetic anti-pattern. All details are invented for teaching.

## Artifact

Build a support triage agent with a good system prompt and connect it to the support tool. Try several tickets and adjust until it works.

## Why It Passes

It sounds pragmatic and fast. Teams often accept this because it feels like useful prototyping.

## Why It Fails

It has no stable fixtures, no trace surface, no prompt boundary, no review schema, and no build-readiness line. Validation would become a memory of good demos.

## Repair

Define fixture scenarios, prompt layers, allowed tool calls, captured traces, and reviewer outputs before anyone evaluates behavior.
