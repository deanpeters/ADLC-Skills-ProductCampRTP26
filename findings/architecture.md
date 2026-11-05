---
title: Architecture and design field guide
adlc_phase: architecture
sources_used: 61
status: draft for Productside review
---

This page is one of the digital takeaways and examples that support Productside's teaching and advisory services on the Agentic Development Lifecycle (ADLC). It synthesizes published sources so a reader does not need to open each one. Evidence labels: Fact (stated by a source as established or documented), Inference (our reading across sources), Hypothesis (a claim without demonstrated support), Unknown.

## What this phase is for

Architecture is where a team turns an agreed goal into a shape it can build, test and govern. The decision it supports is concrete: should this capability be a single model call, a fixed workflow, one agent, or several agents; which model and framework sit underneath; and where do people stay in control? Choices made here set the ceiling on cost, latency, debuggability and risk for every later phase, so they deserve a written rationale, not a default.

## What the sources agree on

1. **Start with the simplest design that could work.** Vendors with different products converge on this: [Anthropic](https://www.anthropic.com/engineering/building-effective-agents), [OpenAI](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf), [Google Cloud](https://cloud.google.com/architecture/choose-design-pattern-agentic-ai-system), [Databricks](https://docs.databricks.com/aws/en/agents/agent-system-design-patterns), [Salesforce](https://architect.salesforce.com/docs/architect/fundamentals/guide/enterprise-agentic-architecture.html), [IBM](https://www.ibm.com/think/topics/agent-development-lifecycle-adlc) and [Microsoft](https://learn.microsoft.com/en-us/agents/architecture/deployment-lifecycle) all advise testing whether a plain call, retrieval or deterministic automation is enough before adding autonomy. Reasons given are cost, latency and error compounding. Fact that the advice is consistent; Inference that it is sound, since none offers controlled comparisons.
2. **Workflow versus agent is the primary fork.** A workflow follows paths the team wrote; an agent chooses its own steps ([Anthropic](https://www.anthropic.com/engineering/building-effective-agents), [Vanlightly](https://jack-vanlightly.com/blog/2025/1/16/ai-agents-in-2025)). Named workflow patterns include chaining, routing, parallel work, orchestrator-workers and evaluator-optimizer. Agents suit open-ended work where the number of steps cannot be predicted ([Google Cloud](https://cloud.google.com/architecture/choose-design-pattern-agentic-ai-system), [Bain](https://www.bain.com/insights/building-the-foundation-for-agentic-ai-technology-report-2025/)). Fact (vendor and practitioner framing).
3. **Move to multiple agents only when one breaks down.** [OpenAI](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf) and [Google Cloud](https://cloud.google.com/architecture/choose-design-pattern-agentic-ai-system) say to split when instructions or tool selection degrade. A survey of agent architectures ([Masterman et al.](https://arxiv.org/abs/2404.11584)) ties multi-agent designs to work that benefits from several perspectives or parallel effort. Inference: choose by the shape of the work, not by ambition.
4. **Multi-agent value is real but narrow and expensive.** [Anthropic's research system](https://www.anthropic.com/engineering/multi-agent-research-system) reports roughly 90 percent better results than a single agent on its internal research evaluation, at about fifteen times the tokens of a chat; the account says it fits breadth-first, parallelizable work and fits poorly where agents share heavy context ([relayed by Willison](https://simonwillison.net/2025/Jun/14/multi-agent-research-system/)). Vendor claim, internal evaluation, not independently verified.
5. **Failures are often structural.** A study of failed multi-agent traces ([Cemri et al.](https://arxiv.org/abs/2503.13657)) grouped 14 failure modes into design flaws, inter-agent misalignment and weak verification, and concluded that better prompts alone will not fix them. Cognition's early argument ([Yan, 2025](https://cognition.ai/blog/dont-build-multi-agents)) is that parallel agents make conflicting implicit decisions; its later note ([Yan, 2026](https://cognition.com/blog/multi-agents-working)) keeps writes single-threaded while letting extra agents review or advise. Fact for the study's data; Inference for generalizing.
6. **Context is a finite design resource.** [Anthropic](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents), [LangChain](https://www.langchain.com/blog/context-engineering-for-agents) and the [smolagents guidance](https://huggingface.co/docs/smolagents/en/tutorials/building_good_agents) agree that tools should be few and distinct, descriptions plain, and information loaded when needed. Long-run techniques are compaction, external notes and sub-agents that return summaries. Fact as practice reports; effect sizes Unknown.
7. **Long-running work needs durable state outside the model.** [Anthropic's harness note](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents), [Osmani](https://www.oreilly.com/radar/long-running-agents/), [LangGraph](https://docs.langchain.com/oss/python/langgraph/durable-execution), [Microsoft](https://devblogs.microsoft.com/dotnet/durable-workflows-in-microsoft-agent-framework/), [Pydantic](https://pydantic.dev/articles/pydantic-ai-dbos) and [CrewAI](https://docs.crewai.com/en/concepts/production-architecture) all describe checkpointing, progress logs or event logs so a crash resumes instead of restarting. [Anthropic's managed-agents post](https://anthropic.com/engineering/managed-agents) separates the session log, the loop and the execution sandbox so each can be replaced. Inference: persistence is an architecture decision, not an operations afterthought.
8. **Human oversight must be designed in, and made real.** Approval steps, escalation and pause points appear in [Microsoft's workflow guidance](https://devblogs.microsoft.com/dotnet/durable-workflows-in-microsoft-agent-framework/), [AutoGen](https://arxiv.org/abs/2308.08155), [Google's CLI example](https://developers.googleblog.com/agents-cli-in-agent-platform-create-to-production-in-one-cli/) and [A2A's task model](https://a2a-protocol.org/latest/specification/). Standards go further: [Singapore's framework](https://www.imda.gov.sg/-/media/imda/files/about/emerging-tech-and-research/artificial-intelligence/mgf-for-agentic-ai.pdf) warns about automation bias and suggests tracking override rates; the [joint guidance led by Australia's cyber agency](https://www.cyber.gov.au/business-government/secure-design/artificial-intelligence/careful-adoption-of-agentic-ai-services) asks for human control points, reversibility and bounded control flows. Fact (documented guidance).
9. **Authority belongs in structure, not in the prompt.** [OpenAI](https://platform.openai.com/docs/guides/agent-builder-safety), [Willison](https://simonwillison.net/2025/Sep/30/designing-agentic-loops/), [Hugging Face](https://huggingface.co/docs/smolagents/en/tutorials/secure_code_execution) and [Broda](https://agenticmesh.substack.com/p/secure-agent-authorization-tasks) agree that least privilege, sandboxes, scoped credentials and per-agent identity limit damage from injection and error. [Anthropic](https://anthropic.com/engineering/managed-agents) describes keeping credentials outside the sandbox, and [one O'Reilly analysis](https://www.oreilly.com/radar/the-ai-agents-stack-2026-edition/) argues guardrails belong at the tool layer, because filtering output is too late once an action has run. Fact as recommended controls; effectiveness is not measured.
10. **Evaluation is a precondition for architecture choices.** [Anthropic](https://www.anthropic.com/engineering/building-effective-agents) says to add complexity only when measurement shows benefit; [Databricks](https://learn.microsoft.com/en-us/azure/databricks/agents/agents-dev-lifecycle), [Snowflake](https://www.snowflake.com/en/developers/guides/best-practices-to-building-cortex-agents/), [Torres](https://www.producttalk.org/customer-interview-coach/) and [Applied LLMs](https://applied-llms.org/) describe small realistic test sets drawn from real traces. Inference: a design without a baseline cannot be compared with a simpler one.
11. **Open protocols are becoming the connective layer.** MCP for tools and A2A for agent-to-agent communication are treated as complementary in the [A2A project's own documents](https://a2a-protocol.org/latest/topics/what-is-a2a/), [Salesforce](https://architect.salesforce.com/docs/architect/fundamentals/guide/enterprise-agentic-architecture.html), [Microsoft](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/governance-security-across-organization) and [Deloitte](https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html). Fact that they are cited widely; neither is shown here to be sufficient for authorization ([Broda and Shreedhar](https://agenticmesh.substack.com/p/building-the-agentic-platform-avoiding)).

## Where they disagree or differ

- **Single versus multi-agent.** [IBM](https://www.ibm.com/think/topics/multiagent-system) and [IBM on orchestration](https://www.ibm.com/think/topics/ai-agent-orchestration) lean toward specialist agents and assert advantages without evidence; Cognition's 2025 essay says to avoid them ([Yan](https://cognition.ai/blog/dont-build-multi-agents)); [Anthropic](https://www.anthropic.com/engineering/multi-agent-research-system) shows a gain for research tasks. The conflict is partly about task type: research versus interdependent coding. Salesforce and Databricks sit in between with staged advice.
- **Frameworks.** [Anthropic](https://www.anthropic.com/engineering/building-effective-agents) warns that frameworks can hide prompts; [IBM](https://www.ibm.com/think/topics/ai-agent-development) presents them as the faster route; [CrewAI](https://docs.crewai.com/en/concepts/production-architecture), [Microsoft](https://devblogs.microsoft.com/dotnet/durable-workflows-in-microsoft-agent-framework/) and [Pydantic](https://pydantic.dev/articles/pydantic-ai-dbos) each recommend their own. Treat framework advice as slanted by product.
- **Is the harness permanent?** [Osmani](https://www.oreilly.com/radar/the-new-software-lifecycle/) says the harness is most of the system; Anthropic's own notes ([harness](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents), [managed agents](https://anthropic.com/engineering/managed-agents)) say harness assumptions go stale as models improve. Inference: keep scaffolding removable.
- **Approval granularity.** [OpenAI](https://platform.openai.com/docs/guides/agent-builder-safety) recommends approving every tool operation; [Willison](https://simonwillison.net/2025/Sep/30/designing-agentic-loops/) notes this slows agents sharply and favors sandboxing; [Google's example](https://developers.googleblog.com/agents-cli-in-agent-platform-create-to-production-in-one-cli/) uses a threshold. No source tests which works best.
- **Platform scope.** Analysts ([McKinsey](https://www.mckinsey.com/capabilities/mckinsey-technology/our-insights/building-the-foundations-for-agentic-ai-at-scale), [BCG](https://www.bcg.com/publications/2026/building-enterprise-ai-agents-in-regulated-industries), [Bain](https://www.bain.com/insights/building-the-foundation-for-agentic-ai-technology-report-2025/)) and [Salesforce](https://architect.salesforce.com/docs/architect/well-architected/guide/agentic-enterprise.html) push shared platforms and registries early; [Wulveryck](https://blog.owulveryck.info/2026/06/24/who-does-what-team-topologies-for-the-agentic-platform.html) suggests a platform pays off at around three to five product teams (author's rule of thumb); [Applied LLMs](https://applied-llms.org/) advises not building what you can buy. Small teams should scale these down.
- **Vocabulary.** Salesforce names five agent types ([patterns](https://architect.salesforce.com/docs/architect/fundamentals/guide/agentic-patterns.html)); Microsoft names three ([adoption](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/)); Databricks uses a ladder; Google separates deterministic from dynamic multi-agent patterns. Names do not map one-to-one, so define terms in your own design record.

## What to do in this phase

1. **Restate the task and its risk.** Product lead, engineering lead and risk owner confirm how reversible actions are, what data is touched and how much autonomy is acceptable ([Singapore framework](https://www.imda.gov.sg/-/media/imda/files/about/emerging-tech-and-research/artificial-intelligence/mgf-for-agentic-ai.pdf)). Evidence: a one-page task profile.
2. **Build the baseline first.** Try a single call with retrieval and a fixed workflow. Collect 20 to 50 realistic cases and score them ([Anthropic](https://www.anthropic.com/engineering/multi-agent-research-system), [Product School](https://productschool.com/blog/artificial-intelligence/how-build-an-ai-agent)). Decide whether an agent earns its added cost.
3. **Choose the structure by climbing the ladder.** Fixed chain, one agent, then specialists ([Databricks](https://docs.databricks.com/aws/en/agents/agent-system-design-patterns), [Google Cloud](https://cloud.google.com/architecture/choose-design-pattern-agentic-ai-system)). For each step up, record the measured benefit and the added cost, latency and debugging burden.
4. **Select model and framework separately from hosting.** Prototype on a strong model, then test smaller ones ([OpenAI](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf)); keep hosting a separate decision ([Microsoft](https://learn.microsoft.com/en-us/agents/architecture/host-platform)). Note switching costs, since changing closed models means retuning and re-evaluating ([O'Reilly stack](https://www.oreilly.com/radar/the-ai-agents-stack-2026-edition/)). Pin versions.
5. **Design context, memory and state.** Decide what is loaded up front, what is retrieved on demand, what persists and who can delete it ([Anthropic](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents), [LangGraph](https://docs.langchain.com/oss/python/langgraph/durable-execution)).
6. **Design authority and human control points.** Define identity, scoped credentials, sandbox boundaries, approval thresholds, escalation, pause and kill switches ([ACSC](https://www.cyber.gov.au/business-government/secure-design/artificial-intelligence/careful-adoption-of-agentic-ai-services), [Microsoft](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/governance-security-across-organization)). Involve security and the accountable business owner.
7. **Plan for observation and change.** Specify traces, cost envelopes, versioning, rollout and rollback ([Salesforce](https://architect.salesforce.com/docs/architect/well-architected/guide/agentic-enterprise.html), [OpenTelemetry conventions](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-agent-spans.md)), plus how the agent will eventually be decommissioned.
8. **Hold an architecture review.** Record the decision, rejected alternatives and revisit triggers.

## Artifacts this phase should produce

| Artifact | Purpose | Minimum contents |
|---|---|---|
| Architecture decision record | Justify structure and model choices | Options, baseline results, cost and latency, rejected alternatives, revisit triggers |
| Task and risk profile | Fix autonomy limits | Actions, reversibility, data touched, autonomy level, owner |
| Control-point map | Show where people intervene | Approval thresholds, escalation paths, override tracking, pause method |
| Authority and identity plan | Limit blast radius | Agent identity, scoped credentials, sandbox, tool permissions |
| Context and state plan | Keep runs reliable | What is loaded, retrieved, stored; retention and deletion |
| Evaluation baseline | Make comparisons possible | Test set, rubric, simple-design scores, pass threshold |
| Cost envelope | Bound spend | Model tier, token and retry budgets, escalation rule |

## Questions a product leader should ask

1. What did the simplest non-agent design score, and why is it not enough?
2. Is the step count predictable? If so, why is the path not fixed?
3. What measured gain justifies each added agent, and at what cost multiple?
4. Can any two agents make conflicting decisions that nobody reconciles?
5. Which actions are irreversible, and who approves them?
6. How will we know approvals are real and not rubber stamps?
7. What can this agent reach if it is fooled by untrusted text?
8. Where does state live, and what happens after a crash mid-task?
9. What would it cost to switch model or framework, and which choices are pinned?
10. Who owns this agent, and how will it be retired?
11. What would make us remove scaffolding when models improve?
12. Which claims in our design rest on vendor marketing?

## Failure modes

- **Agent by default.** Early warning: no baseline from a simpler design exists.
- **Framework hides the system.** Early warning: nobody can show the actual prompts and tool calls.
- **Agent sprawl inside one product.** Early warning: roles overlap and agents repeat each other's work ([MAST study](https://arxiv.org/abs/2503.13657)).
- **Parallel writers without coordination.** Early warning: contradictory outputs that nobody reconciles.
- **Ambient authority.** Early warning: the agent holds broad credentials "to be safe" ([Broda](https://agenticmesh.substack.com/p/secure-agent-authorization-tasks)).
- **Approval fatigue.** Early warning: near-zero override rate with fast responses ([Singapore framework](https://www.imda.gov.sg/-/media/imda/files/about/emerging-tech-and-research/artificial-intelligence/mgf-for-agentic-ai.pdf)).
- **Context bloat.** Early warning: quality drops as runs lengthen while costs climb ([Anthropic](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)).
- **No durable state.** Early warning: failed runs restart from scratch and repeat side effects ([Pydantic](https://pydantic.dev/articles/pydantic-ai-dbos)).
- **Platform before product.** Early warning: a registry and gateway exist but no agent has a measured result.

## Gaps in the evidence

Coverage here is broad, but breadth is not strength. Most multi-agent evidence is vendor-reported on internal evaluations or comes from research prototypes on benchmarks such as code generation ([MetaGPT](https://arxiv.org/abs/2308.00352), [AutoGen](https://arxiv.org/abs/2308.08155)); there are no independent head-to-head comparisons of single and multi-agent designs on production work. Cost multiples come from one vendor and one task type. Standards bodies ([Singapore](https://www.imda.gov.sg/-/media/imda/files/about/emerging-tech-and-research/artificial-intelligence/mgf-for-agentic-ai.pdf), [ACSC](https://www.cyber.gov.au/business-government/secure-design/artificial-intelligence/careful-adoption-of-agentic-ai-services), [OWASP](https://genai.owasp.org/2025/12/09/owasp-genai-security-project-releases-top-10-risks-and-mitigations-for-agentic-ai-security/)) are voluntary and thin on how to choose a pattern; the OWASP item is an announcement without the full list. Analyst content ([McKinsey](https://www.mckinsey.com/capabilities/quantumblack/our-insights/seizing-the-agentic-ai-advantage), [PwC](https://www.pwc.com/us/en/about-us/newsroom/press-releases/pwc-launches-ai-agent-operating-system-enterprises.html), [EY](https://www.ey.com/en_gl/insights/ai/building-an-enterprise-scale-agentic-ai-operating-system)) mixes survey self-report with marketing; headline savings and agent counts are Hypothesis. Several vendor pages are undated and tied to products that change quickly. Little is available on small-team architectures, on model-selection method beyond "test smaller models," or on how often the harness-removal advice holds. Treat all numbers here as illustrations.

## Sources

Licenses are "not verified" unless stated; the Google Cloud pattern page states CC BY 4.0 for page content.

- [Bain, Building the foundation for agentic AI (2025-09-23)](https://www.bain.com/insights/building-the-foundation-for-agentic-ai-technology-report-2025/): orchestrator and task agents
- [BCG, Enterprise AI agents in regulated industries (2026-07-20)](https://www.bcg.com/publications/2026/building-enterprise-ai-agents-in-regulated-industries): shared platform, reuse before build
- [Deloitte, Agentic AI strategy, Tech Trends 2026 (2025-12-10)](https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html): protocols and graduated autonomy
- [EY case study (2026-03-26)](https://www.ey.com/en_gl/insights/ai/building-an-enterprise-scale-agentic-ai-operating-system): self-reported marketing
- [McKinsey, Foundations for agentic AI at scale (2026-04-02)](https://www.mckinsey.com/capabilities/mckinsey-technology/our-insights/building-the-foundations-for-agentic-ai-at-scale): data and governance foundations
- [McKinsey, Seizing the agentic AI advantage (2025-06-13)](https://www.mckinsey.com/capabilities/quantumblack/our-insights/seizing-the-agentic-ai-advantage): agentic mesh concept
- [PwC press release (2025-03-27)](https://www.pwc.com/us/en/about-us/newsroom/press-releases/pwc-launches-ai-agent-operating-system-enterprises.html): vendor marketing
- [Broda and Shreedhar, Avoiding accidental architecture (2026-06-23)](https://agenticmesh.substack.com/p/building-the-agentic-platform-avoiding): MCP is not full authorization
- [Eric Broda, Tasks as the authorization boundary (2026-06-29)](https://agenticmesh.substack.com/p/secure-agent-authorization-tasks): task-scoped grants
- [Addy Osmani, Long-Running Agents, O'Reilly Radar (2026-06-08)](https://www.oreilly.com/radar/long-running-agents/): state outside the model
- [Paolo Perrone, The AI Agents Stack 2026, O'Reilly Radar (2026-06-08)](https://www.oreilly.com/radar/the-ai-agents-stack-2026-edition/): layer choices, tool-layer guardrails
- [Addy Osmani, The New Software Lifecycle, O'Reilly Radar (2026-07-15)](https://www.oreilly.com/radar/the-new-software-lifecycle/): model plus harness
- [Olivier Wulveryck, Team topologies for the agentic platform (2026-06-24)](https://blog.owulveryck.info/2026/06/24/who-does-what-team-topologies-for-the-agentic-platform.html): platform team rule of thumb
- [OpenAI, A practical guide to building agents (undated)](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf): single-agent-first guidance
- [Product School, PM-friendly guide to creating an agent (undated)](https://productschool.com/blog/artificial-intelligence/how-build-an-ai-agent): small test sets, default autonomy
- [Teresa Torres, Building the Interview Coach (2025-08-06)](https://www.producttalk.org/customer-interview-coach/): single-builder evals and cost
- [Yan et al., A Year of Building with LLMs (2024-06-08)](https://applied-llms.org/): smallest model, buy not build
- [Jack Vanlightly, AI Agents in 2025 (2025-01-16)](https://jack-vanlightly.com/blog/2025/1/16/ai-agents-in-2025): compounding error arithmetic
- [Simon Willison annotation (2025-06-14)](https://simonwillison.net/2025/Jun/14/multi-agent-research-system/): secondhand summary
- [Simon Willison, Designing agentic loops (2025-09-30)](https://simonwillison.net/2025/Sep/30/designing-agentic-loops/): sandboxing versus approvals
- [Walden Yan, Cognition, Don't build multi-agents (2025-06-12)](https://cognition.ai/blog/dont-build-multi-agents): single-threaded default
- [Walden Yan, Cognition, Multi-agents: what's working (2026-04-22)](https://cognition.com/blog/multi-agents-working): single-writer, clean-context review
- [Hong et al., MetaGPT (arXiv, 2023-08-01)](https://arxiv.org/abs/2308.00352): structured hand-offs; self-reported
- [Wu et al., AutoGen (arXiv, 2023-08-16)](https://arxiv.org/abs/2308.08155): configurable human involvement
- [Masterman et al., agent architectures survey (arXiv, 2024-04-17)](https://arxiv.org/abs/2404.11584): single versus multi-agent fit
- [Cemri et al., Why do multi-agent LLM systems fail (arXiv, 2025-03-17)](https://arxiv.org/abs/2503.13657): failure taxonomy
- [IBM, What is a multi-agent system (undated)](https://www.ibm.com/think/topics/multiagent-system): multi-agent claims without evidence
- [IBM, What is AI agent development (undated)](https://www.ibm.com/think/topics/ai-agent-development): frameworks as faster route
- [IBM, What is AI agent orchestration (undated)](https://www.ibm.com/think/topics/ai-agent-orchestration): four orchestration styles
- [IBM, What is the ADLC (undated)](https://www.ibm.com/think/topics/agent-development-lifecycle-adlc): plan-first, simplest solution
- [Microsoft Learn, Agent development lifecycle (2026-07-06)](https://learn.microsoft.com/en-us/agents/architecture/deployment-lifecycle): test value before adding complexity
- [Microsoft, AI agent adoption guidance (2025-12-01)](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/): three agent types
- [Microsoft Learn, Choice of agent host (2026-06-23)](https://learn.microsoft.com/en-us/agents/architecture/host-platform): hosting separate from authoring
- [Microsoft Learn, Govern and secure AI agents (2026-04-09)](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/governance-security-across-organization): registry, identity, kill switch
- [A2A Project, Specification 1.0.0 (undated)](https://a2a-protocol.org/latest/specification/): task lifecycle, human-in-the-loop support
- [A2A Project, What is A2A (undated)](https://a2a-protocol.org/latest/topics/what-is-a2a/): MCP and A2A as complements
- [ACSC with CISA, NSA and partner agencies, Careful adoption (2026-05-01)](https://www.cyber.gov.au/business-government/secure-design/artificial-intelligence/careful-adoption-of-agentic-ai-services): risk groups, control points
- [Singapore IMDA, Model AI Governance Framework for Agentic AI v1.5 (2026-05-20)](https://www.imda.gov.sg/-/media/imda/files/about/emerging-tech-and-research/artificial-intelligence/mgf-for-agentic-ai.pdf): risk factors, automation bias
- [OWASP GenAI Security Project, Agentic Top 10 announcement (2025-12-09)](https://genai.owasp.org/2025/12/09/owasp-genai-security-project-releases-top-10-risks-and-mitigations-for-agentic-ai-security/): announcement only
- [OpenTelemetry, GenAI agent span conventions (undated)](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-agent-spans.md): trace vocabulary; development status
- [Anthropic, Building effective agents (2024-12-19)](https://www.anthropic.com/engineering/building-effective-agents): workflow versus agent and five patterns
- [Anthropic, Effective context engineering (2025-09-29)](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents): context as finite resource
- [Anthropic, Effective harnesses for long-running agents (2025-11-26)](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents): progress logs and requirement lists
- [Anthropic, Scaling Managed Agents (2026-04-08)](https://anthropic.com/engineering/managed-agents): session, harness, sandbox split
- [Anthropic, How we built our multi-agent research system (2025-06-13)](https://www.anthropic.com/engineering/multi-agent-research-system): lead plus subagents, cost multiples
- [CrewAI, Production architecture (undated)](https://docs.crewai.com/en/concepts/production-architecture): flow-first, saved state
- [Databricks on Microsoft Learn, Agent development lifecycle (undated)](https://learn.microsoft.com/en-us/azure/databricks/agents/agents-dev-lifecycle): scope and evaluation first
- [Databricks, Agent system design patterns (undated)](https://docs.databricks.com/aws/en/agents/agent-system-design-patterns): complexity ladder
- [Google Cloud, Choose a design pattern (2026-05-28)](https://cloud.google.com/architecture/choose-design-pattern-agentic-ai-system): pattern menu, CC BY 4.0 stated
- [Google Cloud, Agents CLI (2026-04-22)](https://developers.googleblog.com/agents-cli-in-agent-platform-create-to-production-in-one-cli/): approval threshold example; marketing
- [Hugging Face, Building good agents (undated)](https://huggingface.co/docs/smolagents/en/tutorials/building_good_agents): simplest design, clear tools
- [Hugging Face, Secure code execution (undated)](https://huggingface.co/docs/smolagents/en/tutorials/secure_code_execution): sandbox practices
- [LangChain, Context engineering for agents (2025-07-02)](https://www.langchain.com/blog/context-engineering-for-agents): write, select, compress, isolate
- [LangChain, LangGraph persistence (undated)](https://docs.langchain.com/oss/python/langgraph/durable-execution): checkpointers and stores
- [Microsoft, Durable workflows in Agent Framework (undated)](https://devblogs.microsoft.com/dotnet/durable-workflows-in-microsoft-agent-framework/): checkpointing, approval step
- [OpenAI, Safety in building agents (undated)](https://platform.openai.com/docs/guides/agent-builder-safety): injection and approvals
- [Pydantic, Reliable agents with DBOS (2026-02-19)](https://pydantic.dev/articles/pydantic-ai-dbos): durable execution; vendor marketing
- [Salesforce, Agentic patterns with Agentforce (undated)](https://architect.salesforce.com/docs/architect/fundamentals/guide/agentic-patterns.html): five agent types
- [Salesforce Architects, Enterprise agentic architecture (undated)](https://architect.salesforce.com/docs/architect/fundamentals/guide/enterprise-agentic-architecture.html): single-first, multi-agent roles
- [Salesforce, Well-Architected agentic enterprise (undated)](https://architect.salesforce.com/docs/architect/well-architected/guide/agentic-enterprise.html): versioning, rollback, observability
- [Snowflake, Best practices for Cortex agents (2025-11-20)](https://www.snowflake.com/en/developers/guides/best-practices-to-building-cortex-agents/): narrow agents, golden set
