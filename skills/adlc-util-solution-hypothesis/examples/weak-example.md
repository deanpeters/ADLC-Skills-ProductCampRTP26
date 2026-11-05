# Weak Example: Solution Hypothesis Anti-Pattern

Synthetic anti-pattern. All details are invented for teaching.

## Artifact

**If we** build an AI agent that automates payroll tax notices
**for** our clients
**then we will** save them time and keep them compliant.

**We will test our assumptions by:**
1. Running a 90-day pilot with ten clients.
2. Building a prototype and demoing it to leadership.

**We know our hypothesis is valid if we observe:**
1. 80 percent time savings.
2. Clients love it.

Decision: Pursue.

## Why It Passes

It uses the canvas shape exactly, names a real pain, and has two tests and two measures. It reads like a confident plan, and leadership would recognize the ambition.

## Why It Fails

- The If clause names a technology ("an AI agent that automates"), not the designed solution, and "automates" outruns a draft-only ceiling.
- "Our clients" is an organization, not the person whose work changes.
- "Keep them compliant" is a claim about legal outcomes the capability is not allowed to make.
- Neither test is tiny: a 90-day pilot and a built prototype are the investment the hypothesis is meant to protect.
- Neither test has been run, yet the decision is pursue.
- "80 percent time savings" has no baseline and no timeframe; "clients love it" cannot be observed by anyone in particular.
- No result could prove it wrong.

## Repair

Rewrite the If clause around the approved design at draft autonomy and name the specialist as the person. Replace the tests with a timing of a few real past notices and a hand-assembled packet review, and run at least one before deciding. Give each measure a timeframe and a baseline state, and make the qualitative one something a named person says. If neither test can run yet, punt with running the first one as the trigger.
