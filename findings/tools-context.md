---
title: Tools, knowledge and context field guide
adlc_phase: tools-context
sources_used: 48
status: draft for Productside review
---

This field guide is a digital takeaway that supports Productside's teaching and advisory services on the Agentic Development Lifecycle (ADLC). It synthesizes published sources; it is not a specification, and it makes no commitment about anything Productside will build.

## What this phase is for

An agent is only as capable, and as risky, as what it can reach and what it can see. This phase decides three things: which tools the agent may call (including connections to business systems), which knowledge it may draw on (retrieval, memory, notes, shared skills), and how that information is curated at each step (context engineering).

The decision it supports is a product decision as much as a technical one: what is the smallest set of actions and information that lets the agent do its job, and who is accountable for each? Teams that treat this as "wire up everything available" tend to meet cost, accuracy and security problems later. Teams that treat it as scope design usually find the later phases, evaluation, governance and operations, easier.

## What the sources agree on

1. **Start simple, then add tools and structure only when measurement justifies it.** Several vendors and practitioners converge here: a single model call or fixed workflow often suffices, a single agent with tools is the usual next step, and multiple agents come last. ([Anthropic, Building effective agents](https://www.anthropic.com/engineering/building-effective-agents); [Databricks, Agent system design patterns](https://docs.databricks.com/aws/en/agents/agent-system-design-patterns); [Google Cloud, Choose a design pattern](https://cloud.google.com/architecture/choose-design-pattern-agentic-ai-system); [OpenAI, Practical guide](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf); [Hugging Face, Building good agents](https://huggingface.co/docs/smolagents/en/tutorials/building_good_agents)). Evidence label: Inference. It is consistent advice from interested vendors, with no controlled comparison behind it.

2. **Tools are an interface designed for a model, not a copy of a developer API.** Fewer, distinct tools with clear names, descriptions and readable errors perform better than sprawling toolsets. ([Anthropic, Writing effective tools](https://www.anthropic.com/engineering/writing-tools-for-agents); [Anthropic, Effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents); [MCP Specification, Tools](https://modelcontextprotocol.io/specification/2025-11-25/server/tools); [Chip Huyen, Agents](https://huyenchip.com/2025/01/07/agents.html)). Fact that the protocol treats descriptions as model-readable content; Inference that quality of description drives behavior, supported mainly by vendor-reported results.

3. **More context is not better context.** Long windows degrade: stale, duplicated, irrelevant or contradictory material reduces quality, and too many tool definitions confuse selection. ([Drew Breunig, How long contexts fail](https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html); [Drew Breunig, How to fix your context](https://www.dbreunig.com/2025/06/26/how-to-fix-your-context.html); [LangChain, Context engineering](https://www.langchain.com/blog/context-engineering-for-agents); [nilenso, Context observability](https://blog.nilenso.com/blog/2025/10/29/fight-context-rot-with-context-observability/)). Label: Inference. The thresholds quoted are anecdotal or from small-model tests and should not be treated as current limits.

4. **A common toolkit exists for managing context.** The vocabulary differs, but the moves repeat: retrieve selectively, load tools per task, summarize or compact, keep notes outside the window, and isolate work in separate threads. ([Anthropic, Effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents); [LangChain](https://www.langchain.com/blog/context-engineering-for-agents); [Breunig, How to fix your context](https://www.dbreunig.com/2025/06/26/how-to-fix-your-context.html); [Claude Agent SDK post](https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk)). Fact that these techniques are widely described; Unknown which works best for a given task.

5. **Long-running work needs durable, inspectable state.** Agents that start each session with no memory need progress logs, requirement lists and checkpoints so work resumes cleanly. ([Anthropic, Effective harnesses](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents); [Microsoft, Durable workflows](https://devblogs.microsoft.com/dotnet/durable-workflows-in-microsoft-agent-framework/); [Microsoft, Scale agents with shared skills and tools](https://learn.microsoft.com/en-us/agents/architecture/scaling-agents-shared-skills-tools); [Thorsten Ball, How to build an agent](https://ampcode.com/notes/how-to-build-an-agent), which shows the application, not the provider, holds conversation history). Fact for the mechanics; Inference for generality beyond the narrow experiments described.

6. **Protocols standardize connection, not authority.** MCP connects an agent to tools and data; A2A connects agents to each other. Both specifications say access control must be enforced by the server side, and neither decides what an agent should be allowed to do. ([MCP, Authorization](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization); [MCP, Security best practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices); [A2A, What is A2A](https://a2a-protocol.org/latest/topics/what-is-a2a/); [A2A, Specification](https://a2a-protocol.org/latest/specification/)). Fact, from the project specifications. Adoption levels are not established by these sources.

7. **Least privilege, separate identity and human approval for consequential actions are the shared security baseline.** ([ACSC and partner agencies, Careful adoption](https://www.cyber.gov.au/business-government/secure-design/artificial-intelligence/careful-adoption-of-agentic-ai-services); [OWASP, Agentic Top 10 announcement](https://genai.owasp.org/2025/12/09/owasp-genai-security-project-releases-top-10-risks-and-mitigations-for-agentic-ai-security/); [Microsoft, Secure agents](https://learn.microsoft.com/en-us/agents/center-of-excellence/secure-agents); [IBM, Deploy agents across the enterprise](https://www.ibm.com/think/topics/ai-agent-deployment); [Simon Willison, Designing agentic loops](https://simonwillison.net/2025/Sep/30/designing-agentic-loops/)). Fact that government and standards bodies recommend it; Inference that it suffices for any particular product.

8. **Knowledge access inherits existing data problems.** Agents act with the asking user's permissions, so oversharing, stale documents and undocumented business terms surface fast once an agent can retrieve them. ([Microsoft, Secure agents](https://learn.microsoft.com/en-us/agents/center-of-excellence/secure-agents); [McKinsey, Foundations for agentic AI at scale](https://www.mckinsey.com/capabilities/mckinsey-technology/our-insights/building-the-foundations-for-agentic-ai-at-scale); [Mind the Product, Reverse-waterfall](https://www.mindtheproduct.com/why-agentic-ai-forces-a-reverse-waterfall-in-product-management/); [Deloitte, Agentic AI strategy](https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html)). Inference, consistent across consultancy and practitioner sources but lightly evidenced.

9. **Telemetry must capture tool calls and context, and that data is itself sensitive.** ([OpenTelemetry, Agent spans](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-agent-spans.md); [OpenAI Agents SDK, Tracing](https://openai.github.io/openai-agents-python/tracing/); [CrewAI, Tracing](https://docs.crewai.com/en/observability/tracing)). Fact: these documents say prompts, tool arguments and results can contain personal data, and that capture defaults differ by product.

## Where they disagree or differ

- **Single agent versus multiple agents.** Cognition's 2025 essay argues for a single linear thread with shared context ([Walden Yan, Don't build multi-agents](https://cognition.ai/blog/dont-build-multi-agents)); the same author's 2026 follow-up describes narrow multi-agent uses where extra agents contribute judgment but writes stay single-threaded ([Multi-agents: what's actually working](https://cognition.com/blog/multi-agents-working)). Anthropic's research system reports gains from parallel subagents, at roughly fifteen times the tokens of chat, as relayed secondhand ([ByteByteGo summary](https://blog.bytebytego.com/p/how-anthropic-built-a-multi-agent)). Salesforce and AWS lean toward modular multi-agent platforms ([Salesforce, Enterprise agentic architecture](https://architect.salesforce.com/docs/architect/fundamentals/guide/enterprise-agentic-architecture.html); [AWS, AgentCore overview](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html)). The reconciling pattern is that parallelism helps breadth-heavy reading and hurts tightly coupled writing. This is an Inference; every source here has a commercial or personal stake.

- **Retrieval method.** Anthropic's SDK guidance prefers searching an organized file structure first and adding vector search only when needed, citing transparency and maintenance cost. Microsoft's operations guidance treats embedding and index upkeep as normal RAG work to be governed ([Microsoft, GenAIOps](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/genaiops-for-mlops)). Neither compares the two on measured results.

- **Who owns authorization.** MCP's own specification makes authorization optional and leaves action-level limits to implementers. Eric Broda argues for short-lived grants bound to a single task ([Tasks as the authorization boundary](https://agenticmesh.substack.com/p/secure-agent-authorization-tasks); [Avoiding accidental architecture](https://agenticmesh.substack.com/p/building-the-agentic-platform-avoiding)); AWS describes gateway-side policy checks ([AWS, AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html)). These are proposals and product claims, not tested standards.

- **Vocabulary.** "Context engineering" (Anthropic, LangChain), "harness" (Birgitta Bockeler on [harness engineering](https://martinfowler.com/articles/harness-engineering.html)), "agent computer interface" and "augmented model" overlap heavily. Treat them as labels for the same design surface, not as distinct methods. Failure names also vary: poisoning, distraction, confusion and clash come from Breunig; Huyen uses invalid tool, wrong parameters and false completion.

- **Skills as a context mechanism.** Anthropic's progressive-disclosure approach loads only a short description until needed ([Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)); Microsoft's shared catalog serves consistency across many instances. One optimizes the window, the other fleet behavior.

- **Vendor slant.** Platform pages (AWS, Salesforce, Snowflake, Databricks, IBM) tend to present their component list as a checklist of needs. The useful content is the list of concerns, not the product mapping. Consultancies (McKinsey, Bain) quote spend and savings estimates that are hypotheses, not measurements ([Bain, Foundation for agentic AI](https://www.bain.com/insights/building-the-foundation-for-agentic-ai-technology-report-2025/)).

## What to do in this phase

1. **Name the actions and the knowledge.** With the product manager, domain owner and an engineer, list every action the agent must perform and every fact it needs. Classify each tool as knowledge access, capability extension or write action (the split Huyen uses). Evidence: a one-page inventory with an owner per item.

2. **Decide the autonomy default per tool.** Read freely, draft with logging, require approval for irreversible or external-facing actions. Include security and, where data is sensitive, legal. Evidence: a permission table and the rationale for each approval gate.

3. **Choose the connection method.** Direct integration, an MCP server, or a gateway; decide whether other agents need to call this one. Check how credentials are issued: scoped, short-lived and bound to the specific server, as the MCP authorization text requires. Evidence: an architecture note and a credential plan.

4. **Design the tools for the model.** Prototype, write realistic multi-step tasks with checkable answers, read transcripts, revise names, descriptions and error messages. Evidence: a tool test set and a change log.

5. **Set the knowledge boundary.** Specify allowed sources, freshness rules, how references appear in outputs, and what is excluded. Audit permissions on those sources first. Evidence: source register and an oversharing check.

6. **Plan the context budget.** Decide what is always present, what is retrieved, what is summarized, and what is stored outside the window. Name the trigger for compaction or a fresh session. Evidence: a context map with rough token shares and a measurement method.

7. **Instrument before scaling.** Capture tool calls, retrieved content and outcomes, with a decision on retention and redaction. Evidence: a sample trace reviewed by a person who did not build the agent.

8. **Hand off to evaluation.** Pass the tool test set and context map to the evaluation phase, and keep the credential and memory inventory for retirement.

## Artifacts this phase should produce

| Artifact | Purpose | Minimum contents |
|---|---|---|
| Tool and permission register | Single view of what the agent can do | Tool, action type, data touched, autonomy level, approver, credential scope, owner |
| Knowledge source register | Control what the agent can know | Source, owner, freshness, access rule, citation requirement, exclusions |
| Context map | Make context a managed resource | Always-loaded items, retrieved items, compaction rule, external notes, token budget |
| Tool test set | Evidence tools work for the agent | Realistic tasks, expected end state, transcripts, revision history |
| Integration and protocol decision note | Record connection choices | Method (direct, MCP, A2A), authorization model, version, rejected options |
| Telemetry and retention plan | Support review and audit | Events captured, sensitive fields, retention, who reviews |
| Credential and memory inventory | Feed retirement and review | Identities, tokens, stores, retention rule, revocation steps |

## Questions a product leader should ask

1. What is the narrowest set of tools that completes the job, and who removed the others?
2. Which tools can change something outside the agent, and what gates each one?
3. Does the agent have its own identity, or does it borrow a person's or a shared account?
4. If the user can see a document, can the agent retrieve and summarize it? Have we checked whether they should?
5. How do we know a tool works for an agent, as opposed to a person calling the API?
6. What fills the context window by the tenth step, and can anyone show us?
7. What happens when a source is stale, contradictory or wrong? Does the agent say so?
8. Which connectors, tokens or schemas will break when a vendor changes something, and who is told?
9. Is the multi-agent design justified by a measured result, or by an architecture preference?
10. What do our traces store, who can read them, and for how long?
11. Which tool descriptions or skills came from outside our organization, and who reviewed them?
12. If we retired this agent tomorrow, could we list every credential and memory store to remove?

## Failure modes

- **Tool sprawl.** The agent is given every available integration. Early warning: tool-selection errors, rising token cost per task, and engineers unable to say which tool should have been used.
- **Context stuffing.** Teams add documents and history instead of curating. Early warning: quality falls in long sessions, repeated actions, outputs that contradict earlier turns.
- **Breadth-first knowledge layer.** The data team indexes everything while the agent needs depth on a few questions (Mind the Product's hypothesis). Early warning: correct documents exist but answers stay shallow or wrong.
- **Ambient authority.** Valid credentials stand in for permission. Early warning: approvals described as "the agent has access" rather than "this task is allowed".
- **Trusting protocol compliance.** The team assumes using MCP or A2A means secure. Early warning: no one can state how tokens are scoped or validated.
- **Unvetted third-party additions.** Servers, skills and descriptions are installed without review. Early warning: no inventory of what the agent loads.
- **Silent connector drift.** Schemas change or credentials expire without alerting. Early warning: intermittent failures that get blamed on the model.
- **Trace as liability.** Prompts and customer data stored by default. Early warning: nobody can say where traces go.
- **Premature multi-agent design.** Parallel writers make conflicting assumptions. Early warning: rework at merge points and coordination chatter outweighing output.

## Gaps in the evidence

Nothing in this corpus provides independent, controlled evidence on tool or context design. Most of the guidance (about two thirds of the sources used) is vendor guidance or practitioner opinion, and the quantitative claims (tool-count thresholds, token shares, gains from subagents or compaction) are vendor-reported, anecdotal or relayed secondhand. Treat them as Hypothesis.

Specific gaps:

- **Retrieval and memory are thinly covered.** RAG operations appear in one operations guide, and long-term agent memory (what to store, how to expire, how to correct it) has no dedicated source. Memory governance, such as privacy rights and deletion, is Unknown from this corpus.
- **Protocol evidence is specification-only.** The MCP and A2A documents state what the protocols require; none shows adoption, interoperability in practice or security outcomes. The MCP security text is the project's own guidance, not an independent audit, and versions change quickly.
- **Dated research.** The academic papers on agent architecture predate current models and native tool calling, so they inform vocabulary more than practice. See, for example, [Weng, LLM powered autonomous agents](https://lilianweng.github.io/posts/2023-06-23-agent/) and [ReAct](https://arxiv.org/abs/2210.03629).
- **Model-generation drift.** Several vendor essays note that scaffolding useful for one model generation can become dead weight later. Re-test any tool or context workaround when the model changes.
- **Cost and latency.** Few sources quantify the cost of tool and context choices.
- **License status.** Licenses for nearly all sources are not verified; one Breunig post states a CC BY-NC license in its footer. Read the original before reusing wording.

## Sources

Links go to the original sources; read the original for full detail.

- [Anthropic, Building effective agents](https://www.anthropic.com/engineering/building-effective-agents): Anthropic, 2024-12-19, workflow versus agent patterns; license not verified.
- [Anthropic, Writing effective tools for AI agents](https://www.anthropic.com/engineering/writing-tools-for-agents): Anthropic, 2025-09-11, tool design and evaluation.
- [Anthropic, Effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents): Anthropic, 2025-09-29, context as a finite resource.
- [Anthropic, Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents): Anthropic, 2025-11-26, session handoff.
- [Anthropic, Equipping agents with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills): Anthropic, 2025-10-16, progressive disclosure.
- [Anthropic, Building agents with the Claude Agent SDK](https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk): Anthropic, undated, context gathering and verification.
- [OpenAI, A practical guide to building agents](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf): OpenAI, undated, definitions and guardrails.
- [OpenAI Agents SDK, Tracing](https://openai.github.io/openai-agents-python/tracing/): OpenAI, undated, trace contents and defaults.
- [Databricks, Agent system design patterns](https://docs.databricks.com/aws/en/agents/agent-system-design-patterns): Databricks, undated, complexity ladder.
- [Google Cloud, Choose a design pattern](https://cloud.google.com/architecture/choose-design-pattern-agentic-ai-system): Google Cloud, reviewed 2026-05-28.
- [Snowflake, Best practices for Cortex agents](https://www.snowflake.com/en/developers/guides/best-practices-to-building-cortex-agents/): Snowflake, 2025-11-20, scoped agents and golden sets.
- [Salesforce, Enterprise agentic architecture](https://architect.salesforce.com/docs/architect/fundamentals/guide/enterprise-agentic-architecture.html): Salesforce Architects, undated, multi-agent patterns.
- [AWS, What is Amazon Bedrock AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html): AWS, undated, platform concern map.
- [AWS, Policy in AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html): AWS, undated, gateway policy checks.
- [LangChain, Context engineering for agents](https://www.langchain.com/blog/context-engineering-for-agents): LangChain, 2025-07-02, write/select/compress/isolate.
- [Hugging Face, Building good agents](https://huggingface.co/docs/smolagents/en/tutorials/building_good_agents): Hugging Face, undated, simplicity and tool errors.
- [Microsoft, Durable workflows in Agent Framework](https://devblogs.microsoft.com/dotnet/durable-workflows-in-microsoft-agent-framework/): Microsoft, undated, checkpointing.
- [CrewAI, Built-in tracing](https://docs.crewai.com/en/observability/tracing): CrewAI, undated, trace privacy design.
- [Microsoft, Scale agents with shared skills and tools](https://learn.microsoft.com/en-us/agents/architecture/scaling-agents-shared-skills-tools): Microsoft Learn, 2026-07-06.
- [Microsoft, Secure agents](https://learn.microsoft.com/en-us/agents/center-of-excellence/secure-agents): Microsoft Learn, 2026-07-13.
- [Microsoft, GenAIOps for organizations with MLOps](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/genaiops-for-mlops): Microsoft Azure Architecture Center, undated, RAG operations.
- [IBM, How to deploy AI agents across the enterprise](https://www.ibm.com/think/topics/ai-agent-deployment): IBM, 2026-06-25.
- [MCP Specification, Tools](https://modelcontextprotocol.io/specification/2025-11-25/server/tools): Model Context Protocol project, 2025-11-25.
- [MCP Specification, Authorization](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization): Model Context Protocol project, 2025-11-25.
- [MCP, Security best practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices): Model Context Protocol project, 2026-07-28.
- [A2A, What is A2A](https://a2a-protocol.org/latest/topics/what-is-a2a/): A2A Project (Linux Foundation), undated.
- [A2A, Protocol Specification 1.0.0](https://a2a-protocol.org/latest/specification/): A2A Project (Linux Foundation), undated.
- [ACSC and partners, Careful adoption of agentic AI services](https://www.cyber.gov.au/business-government/secure-design/artificial-intelligence/careful-adoption-of-agentic-ai-services): joint national cyber agency guidance, 2026-05-01.
- [OWASP, Agentic Top 10 announcement](https://genai.owasp.org/2025/12/09/owasp-genai-security-project-releases-top-10-risks-and-mitigations-for-agentic-ai-security/): OWASP GenAI Security Project, 2025-12-09.
- [OpenTelemetry, GenAI agent spans](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-agent-spans.md): OpenTelemetry community, undated, development-status convention.
- [Drew Breunig, How long contexts fail](https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html): 2025-06-22.
- [Drew Breunig, How to fix your context](https://www.dbreunig.com/2025/06/26/how-to-fix-your-context.html): 2025-06-26, CC BY-NC 4.0 stated in site footer.
- [nilenso, Fight context rot with context observability](https://blog.nilenso.com/blog/2025/10/29/fight-context-rot-with-context-observability/): 2025-10-29.
- [Walden Yan, Don't build multi-agents](https://cognition.ai/blog/dont-build-multi-agents): Cognition, 2025-06-12.
- [Walden Yan, Multi-agents: what's actually working](https://cognition.com/blog/multi-agents-working): Cognition, 2026-04-22.
- [ByteByteGo, How Anthropic built a multi-agent research system](https://blog.bytebytego.com/p/how-anthropic-built-a-multi-agent): secondary account, 2025-09-16.
- [Birgitta Bockeler, Harness engineering](https://martinfowler.com/articles/harness-engineering.html): Thoughtworks via martinfowler.com, 2026-04-02.
- [Simon Willison, Designing agentic loops](https://simonwillison.net/2025/Sep/30/designing-agentic-loops/): 2025-09-30.
- [Thorsten Ball, How to build an agent](https://ampcode.com/notes/how-to-build-an-agent): Amp, 2025-04-15.
- [Chip Huyen, Agents](https://huyenchip.com/2025/01/07/agents.html): 2025-01-07.
- [Lilian Weng, LLM powered autonomous agents](https://lilianweng.github.io/posts/2023-06-23-agent/): 2023-06-23.
- [ReAct (arXiv 2210.03629)](https://arxiv.org/abs/2210.03629): Yao and colleagues, preprint, 2022-10.
- [Mind the Product, Reverse-waterfall](https://www.mindtheproduct.com/why-agentic-ai-forces-a-reverse-waterfall-in-product-management/): 2026-03-24, author not captured.
- [Eric Broda, Tasks as the authorization boundary](https://agenticmesh.substack.com/p/secure-agent-authorization-tasks): AgenticMesh Substack, 2026-06-29.
- [Broda and Shreedhar, Avoiding accidental architecture](https://agenticmesh.substack.com/p/building-the-agentic-platform-avoiding): AgenticMesh Substack, 2026-06-23.
- [McKinsey, Building the foundations for agentic AI at scale](https://www.mckinsey.com/capabilities/mckinsey-technology/our-insights/building-the-foundations-for-agentic-ai-at-scale): 2026-04-02.
- [Bain, Building the foundation for agentic AI](https://www.bain.com/insights/building-the-foundation-for-agentic-ai-technology-report-2025/): 2025-09-23.
- [Deloitte, Agentic AI strategy](https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html): Tech Trends 2026, 2025-12-10.

