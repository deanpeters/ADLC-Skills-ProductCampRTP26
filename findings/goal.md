---
title: Goal and charter field guide
adlc_phase: goal
sources_used: 49
status: draft for Productside review
---

# Goal and charter field guide

A digital takeaway supporting Productside's teaching and advisory services on the Agentic Development Lifecycle (ADLC). It synthesizes 50 sources; it is not a standard and carries no endorsement of any vendor.

## What this phase is for

The goal phase decides what an agent is for, how far it may act on its own, how you will know it works, and whether an agent is the right answer at all. The decision it supports is a go, no-go or "use something simpler" call, recorded in a short charter before anyone builds. Every later phase (design, tools, evaluation, governance, retirement) inherits the charter, so vagueness here becomes cost later.

## What the sources agree on

1. **Ask first whether an agent is needed. (Fact that vendors say so; Inference that it is sound.)** Anthropic, OpenAI, Google Cloud, IBM, Databricks and Microsoft all tell teams to prefer the simplest approach that works, and treat rules, retrieval, a single prompted call or a fixed workflow as the default. See [Anthropic](https://www.anthropic.com/engineering/building-effective-agents), [OpenAI](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf), [Google Cloud](https://cloud.google.com/architecture/choose-design-pattern-agentic-ai-system), [IBM lifecycle](https://www.ibm.com/think/topics/agent-development-lifecycle-adlc), [Databricks](https://learn.microsoft.com/en-us/azure/databricks/agents/agents-dev-lifecycle), [Microsoft lifecycle](https://learn.microsoft.com/en-us/agents/architecture/deployment-lifecycle). Independent practitioners echo it: [Vanlightly](https://jack-vanlightly.com/blog/2025/1/16/ai-agents-in-2025), [Bowne-Anderson](https://hugobowne.substack.com/p/stop-building-agents) (signpost only), [Mind the Product](https://www.mindtheproduct.com/product-management-for-agentic-ai-when-to-build-agents-and-wow-to-do-it-well/).

2. **Start from the user need and a problem you can judge. (Fact: shared guidance; no controlled evidence.)** [Google PAIR](https://pair.withgoogle.com/chapter/user-needs/) asks whether AI adds unique value over a rule. [Product Talk](https://www.producttalk.org/ai-playbook/), [Product School](https://productschool.com/blog/artificial-intelligence/how-build-an-ai-agent) and [Saar, chapter 7](https://www.adlc.io/product-management/read/finding-your-way-into-the-work) favor frequent, familiar, low-consequence problems where the team can recognize a wrong answer.

3. **Autonomy is a choice made per use case, in steps. (Fact for the vocabulary; Hypothesis that stepwise rollout reduces harm.)** Mind the Product's ladder (suggest, act with approval, act alone), [Bessemer's L0 to L6 scale](https://www.bvp.com/atlas/bessemers-ai-agent-autonomy-scale), [AWS's four autonomy modes](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-economics/measuring-success.html), [Microsoft's three agent types](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/), [Deloitte's graduated autonomy](https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html) and [Product School's "read widely, draft, publish only after proof"](https://productschool.com/blog/artificial-intelligence/how-build-an-ai-agent) are variants of one idea.

4. **Success must be written down before building, in business terms. (Fact that sources require it; evidence of effect is Unknown.)** [CRISP-ML(Q) (Studer et al.)](https://arxiv.org/abs/2003.05155) and [INNOQ's summary](https://ml-ops.org/content/crisp-ml) set business, technical and economic criteria and a simple non-AI baseline. [AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-economics/measuring-success.html) adds a cost baseline and an explicit stop point; [Databricks](https://learn.microsoft.com/en-us/azure/databricks/agents/agents-dev-lifecycle) adds named release sign-off; [Productside's agent guide](https://productside.com/building-ai-agents-for-product-managers/) says to baseline task time, quality and owner.



7. **Ownership and decision rights belong in the charter. (Inference.)** [Broda](https://agenticmesh.substack.com/p/agents-are-about-to-rewrite-the-enterprise) proposes granting decision authority only with a clear task boundary, limited harm, recorded evidence and a controlled release path; [McKinsey](https://www.mckinsey.com/capabilities/people-and-organizational-performance/our-insights/the-agentic-organization-contours-of-the-next-paradigm-for-the-ai-era), [KPMG](https://kpmg.com/us/en/articles/2025/the-agentic-ai-advantage.html) and [swyx](https://www.latent.space/p/agent) (authority and trust as a design element) point the same way, as does Productside's own [friend-or-foe article](https://productside.com/agentic-ai-in-product-management-friend-or-foe/) on keeping accountability human.

8. **Real data, early. (Vendor guidance; plausible, unquantified.)** [Microsoft](https://learn.microsoft.com/en-us/agents/architecture/deployment-lifecycle) advises testing on real data and keeping experiment-to-build gaps short.

## Where they disagree or differ

- **What counts as an agent.** OpenAI treats a system that does not steer its own workflow as not an agent; Anthropic separates workflows from agents; Bessemer excludes plain prompting and automation from L1 upward; Microsoft's lowest type still retrieves and synthesizes. [swyx](https://www.latent.space/p/agent) says no agreed definition exists. Expect stakeholders to argue about words; fix a working definition in the charter.
- **Autonomy vocabularies do not map one-to-one.** Bessemer has seven levels, AWS four, Microsoft three, Mind the Product three. None is validated, and the upper Bessemer levels and [Deloitte's 2028 projection](https://www.deloitte.com/us/en/what-we-do/capabilities/applied-artificial-intelligence/articles/agentic-ai-enterprise-2028.html) are forecasts.
- **Retrofit or redesign.** [MIT Sloan/BCG](https://mitsloan.mit.edu/ideas-made-to-matter/how-to-navigate-age-agentic-ai) and [Deloitte's transformation study](https://www.deloitte.com/us/en/insights/industry/technology/path-to-agentic-transformation.html) describe layering agents on existing workflows as faster and cheaper but limited; [Deloitte's strategy chapter](https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html) urges end-to-end redesign. All three sell advisory services.
- **Start narrow or start with a target state.** Snowflake and Product School favor one narrow agent; [Mind the Product's reverse-waterfall essay](https://www.mindtheproduct.com/why-agentic-ai-forces-a-reverse-waterfall-in-product-management/) says define the target capability first, then build only the context it needs. These are compatible if the narrow agent is the first slice of a stated target.
- **Where the PM sits.** [Saar](https://www.adlc.io/product-management) argues PMs increasingly take part in building; [Cagan](https://www.svpg.com/ai-product-management-2-years-in/) is skeptical that speed yields better outcomes and worries about weak product foundations. Both are opinion.
- **Probabilistic behavior.** [Cagan's essay](https://www.svpg.com/creating-intelligent-products/) argues uncertainty is not disqualifying even in demanding domains; PAIR and the [SVPG risk article](https://www.svpg.com/ai-product-management/) say error tolerance should decide fit. Reconcile by stating tolerance per use case.
- **Vendor slant.** Platform guides ([Snowflake](https://www.snowflake.com/en/developers/guides/best-practices-to-building-cortex-agents/), [Foundry](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/development-lifecycle), [AWS patterns](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/introduction.html), [IBM](https://www.ibm.com/think/topics/agentic-engineering)) route steps to their products and claim benefits without data. [KPMG](https://kpmg.com/us/en/articles/2025/the-agentic-ai-advantage.html) and [Reforge](https://www.reforge.com/blog/how-ai-changes-product-management) are marketing-adjacent.

## What to do in this phase

1. **Name the opportunity.** Product lead with a domain expert. Write one sentence: the agent does X, using data Y, to produce Z, improving outcome W. Evidence: current volume, frequency, who does it today.
2. **Run the "is an agent needed" screen.** Product, engineering lead. Is the task multi-step or variable, does it need tools or memory, could rules or a fixed workflow do it? Record the simpler alternative you rejected and why.
3. **Check the product risks.** Value, usability, feasibility (error tolerance, data availability), viability (unit economics, legal, data provenance), per the [SVPG risk frame](https://www.svpg.com/ai-product-management/) and [PAIR](https://pair.withgoogle.com/chapter/user-needs/). Evidence: a baseline cost and quality measurement.
4. **Choose a target autonomy level.** Product, risk or compliance, the business owner. Decide the level now, and the conditions for moving up. Weigh false positives and false negatives by consequence, not equally.
5. **Write boundaries and failure behavior.** What it may read, draft, change or publish; when it stops and hands back; what it must never touch.
6. **Define success and "done".** Business outcome, quality rubric, cost and latency limits, and a starter set of 20 to 50 realistic cases including awkward ones. Product and risk own the rubric.
7. **Assign owners and decision rights.** One accountable owner, an escalation path, a reviewer of false positives, and who may stop it.
8. **Set stop and review points.** Break-even horizon, a date to decide continue, change or stop, and a note on what retirement would require (identity, stored data, dependents).
9. **Hold a short readiness review** with data and platform owners, since [Deloitte's survey](https://www.deloitte.com/us/en/insights/industry/technology/path-to-agentic-transformation.html) reports data foundations, governance trust and integration as the main barriers (self-reported).

## Artifacts this phase should produce

| Artifact | Purpose | Minimum contents |
|---|---|---|
| Agent charter | One page of record that later phases inherit | Opportunity sentence, users, outcome, owner, out-of-scope list, autonomy level, stop date |
| Agent-or-not decision note | Show simpler options were weighed | Alternatives, screening answers, cost and latency rationale |
| Autonomy and authority statement | Set what it may do alone | Level, allowed actions, approval triggers, escalation path |
| Success and "done" definition | Turn goals into tests | Baseline, metrics, rubric, thresholds (provisional), starter case list |
| Risk and tolerance register | Make error tolerance explicit | Four product risks, error types and cost, data and legal limits |
| Business case with exit criteria | Tie spend to results | Cost baseline, break-even, decision points, retirement note |

## Questions a product leader should ask

1. What would we use if agents did not exist, and why is it not enough?
2. Who does this work today, how often, and what does it cost and produce?
3. At what autonomy level are we starting, and what evidence moves it up?
4. What is the worst plausible error, and who bears it?
5. What is the agent forbidden from doing, and how do we know the prohibition holds?
6. Who is the one named owner, and who can stop it?
7. What does "good enough" mean as a number or a rubric, and who signed it?
8. Do we have real data and a baseline, or only a demo?
9. Which system, data owner or team must change for this to work?
10. What happens if the underlying model, vendor or data source changes?
11. When do we decide to continue, change or stop, and what would trigger that early?
12. Are we layering onto a process we have not understood?

## Failure modes

- **Agent as the answer looking for a question.** Warning sign: the charter names a technology but no user outcome.
- **Agent washing.** Automation relabeled as agentic ([Deloitte](https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html)). Warning sign: no step needs judgment.
- **Unbounded scope.** Warning sign: the out-of-scope list is empty.
- **Autonomy by default.** Writes or sends before quality is shown. Warning sign: no approval triggers.
- **Success defined after the demo.** Warning sign: criteria written to fit existing output.
- **Orphaned ownership.** Warning sign: production release with no escalation path ([Broda](https://agenticmesh.substack.com/p/agents-are-about-to-rewrite-the-enterprise)).
- **Knowledge layer built for coverage, not need.** Warning sign: platform team measures breadth.
- **Compounding error ignored.** Warning sign: long step chains with no per-step reliability estimate; Vanlightly's arithmetic shows 95 percent per step falls near 60 percent over ten.
- **No exit.** Warning sign: no break-even date or stop condition.

## Productside working notes

Productside's own consolidated lifecycle notes, including graceful-retirement practice and goal framing, are in [the ADLC working model](adlc-working-model.md). They are synthesis, not a cited source.

## Gaps in the evidence

Fifty sources are tagged to this phase, but most are practitioner opinion, vendor guidance or consultancy material; few are research. The two research papers ([MetaGPT](https://arxiv.org/abs/2308.00352), [Xi et al. survey](https://arxiv.org/abs/2309.07864)) predate current tooling and say little about charters. Treat as unverified or Unknown:

- Whether any screening heuristic or autonomy ladder improves outcomes; none is tested.
- Numeric suggestions (20 to 100 test cases, cost ranges, 10 percent model and 90 percent harness) are rules of thumb or vendor claims.
- Survey percentages (Deloitte, MIT Sloan/BCG) are self-reported; the 40 to 70 percent automation estimate in a Productside article is an unverified secondary citation.
- Several captures are partial: Bowne-Anderson (signpost), AWS patterns and Deloitte 2028 (landing pages), the book table of contents (headings only), and the AWS measuring page (summary of fuller sections).
- Many publication dates are unknown, and several sources are from 2024 or early 2025. Check currency.
- Nothing here covers regulated sectors or legal duties in depth. The CRISP-ML(Q) material predates agents.
- Productside's own articles are included but promote its training; weigh them like other vendor sources.

## Sources

Licence is "not verified" for all sources unless stated (PAIR's mental-models chapter is non-commercial and share-alike). Do not reuse wording from the originals without checking terms.

**Standards-style and research**
- [Studer et al., CRISP-ML(Q), 2020](https://arxiv.org/abs/2003.05155): success criteria on three levels
- [INNOQ, CRISP-ML(Q) overview](https://ml-ops.org/content/crisp-ml): feasibility gate, non-ML baseline
- [Hong et al., MetaGPT, 2023](https://arxiv.org/abs/2308.00352): structured hand-offs between roles
- [Xi et al., LLM agent survey, 2023](https://arxiv.org/abs/2309.07864): brain, perception, action model

**Vendor guidance**
- [Anthropic, Building effective agents, 2024](https://www.anthropic.com/engineering/building-effective-agents): simplest-first, workflow versus agent
- [OpenAI, Practical guide to building agents](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf): use-case screen, layered guardrails
- [Google Cloud, Choose a design pattern, 2026](https://cloud.google.com/architecture/choose-design-pattern-agentic-ai-system): non-agentic option first
- [Databricks, Agent development lifecycle](https://learn.microsoft.com/en-us/azure/databricks/agents/agents-dev-lifecycle): success criteria and sign-off
- [Snowflake, Cortex agent practices, 2025](https://www.snowflake.com/en/developers/guides/best-practices-to-building-cortex-agents/): narrow scope, top questions
- [AWS, Agentic patterns introduction](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/introduction.html): thin orientation page
- [AWS, Measuring success and ROI](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-economics/measuring-success.html): baseline, autonomy modes, stop points
- [Google PAIR, User needs and defining success](https://pair.withgoogle.com/chapter/user-needs/): need first, reward function
- [Google PAIR, Mental models](https://pair.withgoogle.com/chapter/mental-models/): setting honest expectations
- [Microsoft, Agent development lifecycle, 2026](https://learn.microsoft.com/en-us/agents/architecture/deployment-lifecycle): discovery and real data
- [Microsoft, Foundry lifecycle, 2026](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/development-lifecycle): platform steps
- [Microsoft, Adoption guidance, 2025](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/): three agent types
- [Microsoft, Derive quality signals, 2026](https://learn.microsoft.com/en-us/agents/agent-evaluation/evaluation-define-quality): specific quality definitions
- [IBM, What is the agent development lifecycle](https://www.ibm.com/think/topics/agent-development-lifecycle-adlc): plan-first go or no-go
- [IBM, What is AI agent development](https://www.ibm.com/think/topics/ai-agent-development): scoping questions
- [IBM, What is agentic engineering, 2026](https://www.ibm.com/think/topics/agentic-engineering): human review in delivery

**Analysts and consultancies**
- [McKinsey, The agentic organization, 2025](https://www.mckinsey.com/capabilities/people-and-organizational-performance/our-insights/the-agentic-organization-contours-of-the-next-paradigm-for-the-ai-era): outcome teams, governance
- [Deloitte, Agentic AI strategy, 2025](https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html): agent washing, redesign
- [Deloitte, Path to agentic transformation, 2026](https://www.deloitte.com/us/en/insights/industry/technology/path-to-agentic-transformation.html): readiness survey
- [Deloitte, Agentic enterprise 2028](https://www.deloitte.com/us/en/what-we-do/capabilities/applied-artificial-intelligence/articles/agentic-ai-enterprise-2028.html): autonomy forecast
- [KPMG, Agentic AI advantage](https://kpmg.com/us/en/articles/2025/the-agentic-ai-advantage.html): pilot selection, marketing slant
- [MIT Sloan on MIT SMR and BCG report, 2026](https://mitsloan.mit.edu/ideas-made-to-matter/how-to-navigate-age-agentic-ai): four leadership tensions
- [Bessemer, Agent autonomy scale, 2025](https://www.bvp.com/atlas/bessemers-ai-agent-autonomy-scale): L0 to L6

**Practitioners and product voices**
- [SVPG, AI Product Management, 2024](https://www.svpg.com/ai-product-management/): four risks for AI
- [SVPG, 2 years in, 2024](https://www.svpg.com/ai-product-management-2-years-in/): skeptical open questions
- [SVPG, Creating intelligent products, 2025](https://www.svpg.com/creating-intelligent-products/): probabilistic design
- [Mind the Product, When to build agents, 2025](https://www.mindtheproduct.com/product-management-for-agentic-ai-when-to-build-agents-and-wow-to-do-it-well/): screen and autonomy ladder
- [Mind the Product, Reverse-waterfall, 2026](https://www.mindtheproduct.com/why-agentic-ai-forces-a-reverse-waterfall-in-product-management/): capability-first context
- [Product Talk, Building my first AI product, 2025](https://www.producttalk.org/ai-playbook/): choosing AI-shaped problems
- [Product School, How to create an AI agent](https://productschool.com/blog/artificial-intelligence/how-build-an-ai-agent): goal template
- [Pollick, Evals as acceptance criteria, 2026](https://rickpollick.com/blog/evals-are-the-new-acceptance-criteria): definition of done
- [Reforge, How AI changes PM, 2025](https://www.reforge.com/blog/how-ai-changes-product-management): prioritization questions
- [Vanlightly, AI agents in 2025](https://jack-vanlightly.com/blog/2025/1/16/ai-agents-in-2025): compounding error, start simple
- [swyx, Agent engineering, 2025](https://www.latent.space/p/agent): definitions, authority
- [Bowne-Anderson, Stop building agents, 2025](https://hugobowne.substack.com/p/stop-building-agents): partial capture
- [Osmani, The new software lifecycle, 2026](https://www.oreilly.com/radar/the-new-software-lifecycle/): specification and verification
- [Broda, Agents rewrite the operating model, 2026](https://agenticmesh.substack.com/p/agents-are-about-to-rewrite-the-enterprise): decision rights

**Courses, books and Productside material**
- [Saar, chapter 7](https://www.adlc.io/product-management/read/finding-your-way-into-the-work): first-project advice
- [Saar, free sample page](https://www.adlc.io/product-management/sample): duplicate of chapter 7
- [Saar, book landing page](https://www.adlc.io/product-management): PM loop, marketing copy
- [Saar, table of contents](https://www.adlc.io/product-management/read): headings only
- [adlc.io home](https://www.adlc.io/): manifesto, single author
- [Productside, Future of AI PM roles, 2025](https://productside.com/the-future-of-ai-product-management-roles/): evals as product work
- [Productside, Friend or foe, 2025](https://productside.com/agentic-ai-in-product-management-friend-or-foe/): human accountability
- [Productside, AI agents for PMs, 2026](https://productside.com/building-ai-agents-for-product-managers/): first pilots, baselines
