# Weak Example: Deployment Anti-Pattern

Synthetic anti-pattern. All details are invented for teaching.

## Artifact

Launch the agent to the whole support team next week. We will monitor feedback and pause if something goes wrong.

## Why It Passes

It sounds cautious because it mentions monitoring and pausing.

## Why It Fails

It has no launch gate, no blast-radius limit, no oversight owner, no rollback path, and no incident trigger. "Something goes wrong" is not an operating condition.

## Repair

Start with a limited audience, define gates, assign oversight, specify rollback, and name incident triggers before launch.
