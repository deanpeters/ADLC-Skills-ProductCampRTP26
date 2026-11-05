# Weak Example: Minimum Viable Narrative Anti-Pattern

Synthetic anti-pattern. All details are invented for teaching.

## Artifact

**Audience:** CSMs.

**Setup:** The CSM needs to manage renewals more efficiently.

**Encounter:** A modern dashboard with a left navigation bar, three tabs (Plan, Risks, Pricing), and a blue header.

**Loop:**

1. The CSM opens the dashboard → the AI shows the best renewal plan with a confidence score.
2. The CSM clicks "Generate" → the agent writes the plan, recommends a discount, and emails it to the customer for approval.

**Resolution:** Renewals go up 20 percent.

**Prompt:** "Create a React HTML5 app in our brand colors for the ADLC Stage 3 review surface per the harness brief (see docs/harness.md). Use our real customer list for realism."

## Why It Passes

It has every beat, a loop, a prompt, and a clear outcome. It reads like a confident product vision, and the dashboard sounds buildable.

## Why It Fails

- The audience is a role with no person and no moment, and the Setup is a goal, not a starting point: nothing about what is at stake, what the CSM already knows, or what they don't know yet, so a builder cannot tell what the prototype must help them work out.
- The Encounter prescribes a design (navigation, tabs, colors), so the prototype tests nothing about the experience.
- The loop is two arrow lines, not labelled turns, and it is too short to be a story. Neither Action is a choice or an input: "opens" and "clicks Generate" give the system nothing, so a person reacting to the prototype never does the work. There is no checking a claim, no handback, and no edit, and no chance to look closer or ask why before a consequential choice.
- Turn 1 names one "best" plan with a confidence score, so the story itself contains the failure a bake-off would test for: a single confident answer where the CSM should decide.
- Turn 2 proposes a discount and emails the customer, both beyond a draft-only ceiling. The story widened the authority because the ceiling was never stated beside it.
- The Resolution is a business metric no single prototype session could show.
- The prompt names a medium and a brand, which belong in the build instruction, so the same story cannot go to a design tool or be built unbranded. It also uses lifecycle vocabulary, links to a file the builder cannot open, asks for real customer data, and has no experience baseline, so even a good builder has no reason to show progress, ask before acting, or let the CSM undo a choice.

## Repair

Name one person in one moment, and give the Setup a real starting point: what is at stake, what they know, and what they don't. Describe what they see and experience, not the layout. Decide the number of turns, then tell three to six labelled turns, each a Human Action that is a choice or an input ("Sam flags the usage claim that looks wrong") and a System Response that answers it, from the first draft to taking the plan into the call, with the unconfirmed contract term as a whole turn where it hands the decision back, and up to two optional actions where Sam would hesitate ("Sam asks why the CRM date wasn't used") that explain without changing anything. State the ceiling beside the story: draft only, nothing sent, no pricing. End on what success feels like for that person. Rewrite the prompt in the metaprompt's shape so a stranger can use it: no medium, no jargon, no links, an "It Must Never" section, a "How It Should Feel To Use" section with the experience baseline, and invented data only. Move the medium and the brand guide into the build instruction.
