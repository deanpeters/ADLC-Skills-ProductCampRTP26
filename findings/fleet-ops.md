---
title: Fleet operations field guide
adlc_phase: fleet-ops
sources_used: 37
status: draft for Productside review
---

This page is one of the digital takeaways and examples that support Productside's teaching and advisory services on the Agentic Development Lifecycle (ADLC). It is written so you can use it without opening the sources.

## What this phase is for

Fleet operations begins when you stop managing one agent and start managing many. The questions change from "does this agent work?" to "what agents do we have, who owns each, what can each one touch, how do they coordinate, what do they cost, and which should we switch off?"

The decision it supports: how much structure to put around a growing set of agents, and when. Too little and you get sprawl. Too much and you slow simple agents and push people toward unsanctioned ones. Product leaders usually own the outcome and the owner assignments. Platform, security and finance colleagues own the machinery.

## What the sources agree on

1. **You cannot govern what you cannot see, so an inventory comes first.** Nearly every source that discusses scale starts here: [IBM on sprawl](https://www.ibm.com/think/topics/ai-agent-sprawl), [Microsoft's governance guidance](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/governance-security-across-organization), [BCG](https://www.bcg.com/publications/2026/the-four-pillars-cios-can-use-to-scale-agentic-ai), [SAP](https://learning.sap.com/courses/boosting-ai-driven-business-transformation-with-joule-agents/managing-ai-agents-using-ai-agent-hub) and [ServiceNow](https://www.servicenow.com/community/servicenow-ai-platform-forum/ai-without-chaos-a-deep-dive-into-ai-control-tower/m-p/3455272). *Inference*: the agreement is strong, but almost all of it is vendor or consultancy advice, not measured outcomes.

2. **Every agent needs a named human owner and its own identity.** See [Accenture](https://www.accenture.com/en/insights/consulting/operating-model-age-of-ai), [Microsoft](https://learn.microsoft.com/en-us/agents/center-of-excellence/agent-lifecycle), [Broda on operating models](https://agenticmesh.substack.com/p/agents-are-about-to-rewrite-the-enterprise) and Singapore's [IMDA framework](https://www.imda.gov.sg/-/media/imda/files/about/emerging-tech-and-research/artificial-intelligence/mgf-for-agentic-ai.pdf), which also admits that robust agent identity is still an evolving gap. *Fact* that these sources recommend it; *Unknown* how widely it is practiced.

3. **Oversight should sit apart from the agents it oversees and be enforced at run time.** [Forrester](https://www.forrester.com/blogs/announcing-our-evaluation-of-the-agent-control-plane-market/) argues governance should be independent of build and orchestration; [IBM](https://www.ibm.com/think/topics/agent-control-plane) says policies must be evaluated during execution; [AWS](https://aws.amazon.com/blogs/machine-learning/agentops-operationalize-agentic-ai-at-scale-with-amazon-bedrock-agentcore/) and [Wulveryck](https://blog.owulveryck.info/2026/06/24/who-does-what-team-topologies-for-the-agentic-platform.html) put guardrails in deterministic controls rather than prompts. *Inference*: a design consensus, not a tested result.

4. **Governance should scale with risk, not apply one checklist.** [Microsoft's tiering](https://learn.microsoft.com/en-us/agents/center-of-excellence/govern-agents-risk) uses the line between assisting a person and executing actions. IMDA lists action reversibility, autonomy and data sensitivity as risk drivers, and [KPMG](https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2025/ai-governance-for-agentic-ai-era.pdf) sorts agents into four types. *Fact* that each proposes tiers; the tier counts themselves are design choices.

5. **Fleet telemetry is a precondition, not an add-on.** [Microsoft's fleet monitoring](https://learn.microsoft.com/en-us/azure/foundry/control-plane/monitoring-across-fleet) states that an agent without connected telemetry has no health or cost view. The research agrees on the principle: [AgentOps](https://arxiv.org/abs/2411.05285) proposes tracing across the whole lifecycle, and [Wang et al.](https://arxiv.org/abs/2606.01581) argue that log-based operations miss semantic failures. *Fact* for the Microsoft statement; *Inference* that it generalizes.

6. **Human review, not agent output, is often the bottleneck.** [Orosz](https://newsletter.pragmaticengineer.com/p/new-trend-programming-by-kicking) reports engineers landing only one significant change at a time; [Cognition](https://cognition.com/blog/multi-agents-working) keeps writes single-threaded; [Hands-on Architects](https://handsonarchitects.com/blog/2026/team-topologies-ai-harness-cognitive-load/) say cognitive load is relocated, not removed. *Inference*, from anecdote.

7. **Interoperability standards are immature but converging.** The [A2A specification](https://a2a-protocol.org/latest/specification/) positions itself as complementary to MCP: tools versus peer agents. [NIST](https://www.nist.gov/artificial-intelligence/ai-agent-standards-initiative) is pursuing voluntary guidelines, yet [Forrester's follow-up](https://www.forrester.com/blogs/agent-control-planes-still-need-a-robust-standards-stack/) says portable identity and policy propagation are still missing. *Fact* for the specification and the NIST intent.

8. **Retirement belongs to fleet operations.** IBM frames sprawl partly as a decommissioning failure; [McKinsey](https://www.mckinsey.com/capabilities/quantumblack/our-insights/seizing-the-agentic-ai-advantage) lists who decides what to retire as a sprawl challenge; Microsoft's seven-stage lifecycle ends in retire.

## Where they disagree or differ

- **Vocabulary.** "Control plane" (IBM, Forrester, Microsoft), "control tower" (ServiceNow), "agent hub" (SAP) and "mesh" ([McKinsey](https://www.mckinsey.com/capabilities/quantumblack/our-insights/seizing-the-agentic-ai-advantage), [Broda](https://agenticmesh.substack.com/p/building-the-agentic-platform-avoiding)) overlap heavily. IBM itself notes the control plane has no formal standard. Treat the names as marketing categories and compare capabilities instead.
- **Orchestration shape.** [IBM](https://www.ibm.com/think/topics/ai-agent-orchestration) lists centralized, decentralized, hierarchical and federated styles, with trade-offs between predictability and resilience. [Salesforce](https://architect.salesforce.com/docs/architect/fundamentals/guide/agentic-enterprise-it-architecture.html) prefers blended: local coordination plus a central layer for process and compliance. [Bessemer's scale](https://www.bvp.com/atlas/bessemers-ai-agent-autonomy-scale) treats agents that direct other agents as its top level, which is speculative.
- **Swarms versus single writers.** IBM's multi-agent explainers lean toward multi-agent benefits ([system](https://www.ibm.com/think/topics/multiagent-system), [collaboration](https://www.ibm.com/think/topics/multi-agent-collaboration)), while Cognition reports that parallel writer swarms are mostly unproven. Both are vendors with products to sell.
- **Central versus federated ownership.** [McKinsey](https://www.mckinsey.com/capabilities/mckinsey-technology/our-insights/building-the-foundations-for-agentic-ai-at-scale) and BCG favor a federated split (domains own workflows, a center owns platforms); Broda leans toward centrally governed agents; Wulveryck suggests a shared platform pays off at roughly three to five product teams, an untested rule of thumb.
- **Per-task or persistent agents.** Salesforce describes instances created per task and then decommissioned; Microsoft says to treat an agent as a product with a lasting owner. These suit different designs.
- **Adoption numbers.** [Deloitte](https://www.deloitte.com/us/en/insights/industry/technology/path-to-agentic-transformation.html) reports 15 percent at scaled, orchestrated use; McKinsey says under 10 percent have scaled; [EY](https://www.ey.com/en_gl/insights/ai/building-an-enterprise-scale-agentic-ai-operating-system) cites more than 50,000 agents built in nine months. These use different definitions and are self-reported.

## What to do in this phase

1. **Declare what counts as an agent and take a census.** Involve security, IT, business-unit leads and low-code owners. Collect owner, purpose, platform, data and tool access, identity, version, status and cost. Evidence: a first inventory with its known blind spots listed.
2. **Assign owners and close orphans.** Decide who is accountable for each agent; flag those with none. Evidence: percentage of agents with a named owner.
3. **Tier by risk.** Decide which agents act versus assist, which touch regulated data, and which are external-facing. Apply lighter controls to low tiers and gates to high ones. Evidence: tier assignments with the reasoning.
4. **Set the minimum telemetry standard.** Decide the fields every agent must emit before it joins the fleet, and the audiences for each view (managers, administrators, finance, security). Evidence: coverage rate and cost per outcome, not agent count.
5. **Decide the coordination pattern for multi-agent work.** Choose single-writer, manager and child, or peer designs deliberately, and record the human review points. Evidence: review load and error rates in a pilot.
6. **Define the stop and retire paths.** Establish the kill switch, what stopping does to in-flight work, dormancy rules, and a retire, migrate or keep decision. Evidence: a tested stop on a low-risk agent.
7. **Review on a rhythm.** Hold quarterly reviews for high-tier agents and track drift, spend and incidents, feeding findings back to earlier phases.

## Artifacts this phase should produce

| Artifact | Purpose | Minimum contents |
|---|---|---|
| Agent inventory | One source of truth for the fleet | ID, owner, purpose, platform, version, status, data and tool access, identity, cost, last review |
| Risk tier policy | Match controls to consequence | Tier definitions, classification questions, required controls per tier |
| Ownership and decision-rights map | Make accountability explicit | Owner, backup, escalation path, what the agent may decide alone |
| Telemetry standard | Make the fleet observable | Required fields, audiences, alert owners, retention |
| Coordination design note | Record how agents hand off | Pattern chosen, write rules, human review points, failure handling |
| Retirement and dormancy rules | Prevent zombie agents | Triggers, notice, credential revocation, data disposition, successor |
| Fleet review pack | Support recurring decisions | Counts by tier, spend, incidents, drift signals, retire or keep list |

## Questions a product leader should ask

1. Can we list every agent running on our behalf, including those built in low-code tools? How do we know the list is complete?
2. Who is the named owner of each, and what happens when that person leaves?
3. Which agents act on records, money or customers, and which only draft?
4. What identity and permissions does each hold, and who can revoke them?
5. What would we see if one agent began failing quietly tomorrow?
6. Which agents have no telemetry, and therefore no cost or health view?
7. Where do multiple agents write to the same thing, and who reviews the result?
8. Is human review keeping pace with agent output, or are we rubber-stamping?
9. What does it cost per completed outcome, and who sees it?
10. Which agents are dormant or duplicated, and who decides they go?
11. If we pause an agent, what happens to runs already in progress?
12. Which parts of our setup depend on one vendor's control plane, and how would we move?

## Failure modes

- **Counting agents as success.** Warning sign: dashboards show agents created, not outcomes or cost per outcome. Microsoft's measurement guidance warns against it.
- **Orphaned agents.** Warning sign: no owner field, or owners who changed roles.
- **One checklist for everything.** Warning sign: simple agents wait weeks for review, so teams route around it ([Microsoft](https://learn.microsoft.com/en-us/agents/center-of-excellence/govern-agents-risk), [IBM](https://www.ibm.com/think/topics/ai-agent-sprawl) on shadow AI).
- **Governance by prompt.** Warning sign: constraints exist only as instructions inside the agent, not as enforced controls.
- **Blind spots in telemetry.** Warning sign: cost or error charts blank for some agents.
- **Swarming without review capacity.** Warning sign: queues of unreviewed changes, or reviewers approving at speed.
- **Stop that does not stop.** Warning sign: no one has tested what a stop or block does ([Microsoft](https://learn.microsoft.com/en-us/azure/foundry/control-plane/how-to-manage-agents) notes some agents can only be blocked, not halted).
- **Never retiring.** Warning sign: inventory only grows.
- **Platform lock-in by default.** Warning sign: inventory and policies live only in one vendor's tool.

## Gaps in the evidence

The corpus has many sources for this phase, but they are weaker than the count suggests.

- **Mostly vendor and consultancy.** Few independent studies measure whether inventories, control planes or tiering reduce incidents or cost. Treat every benefit claim as *Hypothesis*.
- **Statistics are second-hand.** Survey figures on sprawl, readiness and observability are largely vendor-reported and unverified. Treat as *Unknown* until checked against originals.
- **Standards are early.** NIST has announced intent rather than finished guidance; agent identity and cross-system policy propagation lack portable standards. The IMDA framework is voluntary and Singapore-anchored.
- **Multi-agent evidence is anecdotal.** The practitioner sources are small, early-adopter accounts focused on software engineering, so applicability to product-management work is an extension.
- **Retirement is thin.** Few sources say how retirement criteria should be set.
- **Scale thresholds are unsupported.** No source gives a defensible fleet size at which a given control becomes necessary.
- **Tooling will date.** Product names and features in Microsoft, AWS, IBM, SAP, ServiceNow and Google material change quickly.

## Sources

Licenses are "not verified" unless stated. Dates are as shown by each source.

- [IBM, What is AI Agent Sprawl](https://www.ibm.com/think/topics/ai-agent-sprawl): sprawl, discover/govern/standardize (2026-04-28)
- [IBM, What is an Agent Control Plane](https://www.ibm.com/think/topics/agent-control-plane): control versus data plane (undated)
- [IBM, What is AI Agent Orchestration](https://www.ibm.com/think/topics/ai-agent-orchestration): four orchestration styles (undated)
- [IBM, What is a Multi-Agent System](https://www.ibm.com/think/topics/multiagent-system): network shapes and risks (undated)
- [IBM, What is Multi-Agent Collaboration](https://www.ibm.com/think/topics/multi-agent-collaboration): collaboration strategies (undated)
- [Microsoft, Govern agents by risk](https://learn.microsoft.com/en-us/agents/center-of-excellence/govern-agents-risk): three-tier model (2026-07-13)
- [Microsoft, Govern and secure AI agents](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/governance-security-across-organization): registry, identity, baseline (2026-04-09)
- [Microsoft, Manage the agent lifecycle](https://learn.microsoft.com/en-us/agents/center-of-excellence/agent-lifecycle): owner, drift, retire (2026-07-13)
- [Microsoft, Monitor fleet health](https://learn.microsoft.com/en-us/azure/foundry/control-plane/monitoring-across-fleet): telemetry prerequisite (2026-05-12)
- [Microsoft, Manage agents at scale](https://learn.microsoft.com/en-us/azure/foundry/control-plane/how-to-manage-agents): inventory columns, stop limits (2026-07-15)
- [Accenture, Operating Model in the Age of AI](https://www.accenture.com/en/insights/consulting/operating-model-age-of-ai): owner for every agent (2026-09-24)
- [BCG, Scaling Agents Without Creating Your Next Tech Legacy](https://www.bcg.com/publications/2026/the-four-pillars-cios-can-use-to-scale-agentic-ai): graduation pathways (2026-07-14)
- [Deloitte, The path to agentic transformation](https://www.deloitte.com/us/en/insights/industry/technology/path-to-agentic-transformation.html): adoption stages survey (2026-08-12)
- [EY, enterprise agentic operating system case study](https://www.ey.com/en_gl/insights/ai/building-an-enterprise-scale-agentic-ai-operating-system): self-reported scale (2026-03-26)
- [Forrester, Evaluation of the agent control plane market](https://www.forrester.com/blogs/announcing-our-evaluation-of-the-agent-control-plane-market/): three planes (2025-12-04)
- [Forrester, Control planes need a standards stack](https://www.forrester.com/blogs/agent-control-planes-still-need-a-robust-standards-stack/): standards gaps (2026-03-20)
- [KPMG, AI governance for the agentic era](https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2025/ai-governance-for-agentic-ai-era.pdf): agent types and controls (2025-07-01)
- [McKinsey, Building the foundations for agentic AI at scale](https://www.mckinsey.com/capabilities/mckinsey-technology/our-insights/building-the-foundations-for-agentic-ai-at-scale): federated model (2026-04-02)
- [McKinsey, Seizing the agentic AI advantage](https://www.mckinsey.com/capabilities/quantumblack/our-insights/seizing-the-agentic-ai-advantage): agentic mesh, sprawl (2025-06-13)
- [Bain, Building the Foundation for Agentic AI](https://www.bain.com/insights/building-the-foundation-for-agentic-ai-technology-report-2025/): orchestrator and task agents (2025-09-23)
- [Bessemer, AI agent autonomy scale](https://www.bvp.com/atlas/bessemers-ai-agent-autonomy-scale): L0 to L6 framework (2025-04-09)
- [Broda, Agents Are About to Rewrite the Enterprise Operating Model](https://agenticmesh.substack.com/p/agents-are-about-to-rewrite-the-enterprise): authority conditions (2026-07-28)
- [Broda and Shreedhar, Avoiding Accidental Architecture](https://agenticmesh.substack.com/p/building-the-agentic-platform-avoiding): open decisions, deprecation registry (2026-06-23)
- [Wulveryck, Team Topologies for the Agentic Platform](https://blog.owulveryck.info/2026/06/24/who-does-what-team-topologies-for-the-agentic-platform.html): platform ownership split (2026-06-24)
- [Hands-on Architects, Team Topologies in the AI Era](https://handsonarchitects.com/blog/2026/team-topologies-ai-harness-cognitive-load/): cognitive load (2026-06-30)
- [Wang et al., Agent System Operations](https://arxiv.org/abs/2606.01581): anomaly taxonomy, preprint (2026-06-01)
- [Orosz, Programming by kicking off parallel agents](https://newsletter.pragmaticengineer.com/p/new-trend-programming-by-kicking): review bottleneck (2025-10-30)
- [Yan, Multi-Agents: What's Actually Working](https://cognition.com/blog/multi-agents-working): single-writer pattern, vendor view (2026-04-22)
- [Dong et al., AgentOps observability](https://arxiv.org/abs/2411.05285): tracing taxonomy, preprint (2024-11-08)
- [Chan et al., Visibility into AI Agents](https://arxiv.org/abs/2401.13138): identifiers, monitoring, logging, preprint (2024-01-23)
- [A2A Protocol Specification 1.0.0](https://a2a-protocol.org/latest/specification/): agent-to-agent standard (undated)
- [IMDA, Model AI Governance Framework for Agentic AI](https://www.imda.gov.sg/-/media/imda/files/about/emerging-tech-and-research/artificial-intelligence/mgf-for-agentic-ai.pdf): risk-based guidance (2026-05-20)
- [NIST CAISI, AI Agent Standards Initiative](https://www.nist.gov/artificial-intelligence/ai-agent-standards-initiative): three pillars (2026-02-17)
- [AWS, AgentOps with Bedrock AgentCore](https://aws.amazon.com/blogs/machine-learning/agentops-operationalize-agentic-ai-at-scale-with-amazon-bedrock-agentcore/): versioned, deterministic controls (2026-06-01)
- [Salesforce Architects, The Agentic Enterprise](https://architect.salesforce.com/docs/architect/fundamentals/guide/agentic-enterprise-it-architecture.html): blended orchestration (undated)
- [SAP, Managing AI Agents using AI Agent Hub](https://learning.sap.com/courses/boosting-ai-driven-business-transformation-with-joule-agents/managing-ai-agents-using-ai-agent-hub): registry mapped to capabilities (undated)
- [ServiceNow Community, AI Without Chaos](https://www.servicenow.com/community/servicenow-ai-platform-forum/ai-without-chaos-a-deep-dive-into-ai-control-tower/m-p/3455272): known, approved, monitored (2025-12-23)
