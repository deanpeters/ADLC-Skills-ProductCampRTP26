---
title: Governance, security and guardrails field guide
adlc_phase: governance
sources_used: 50
status: draft for Productside review
---

This page is one of the digital takeaways that support Productside's teaching and advisory services on the Agentic Development Lifecycle (ADLC). It synthesizes 50 sources; use it without opening the originals, then follow the links when you need detail.

## What this phase is for

Governance decides how much an agent is allowed to do, on whose authority, under what limits, and how you will know when it goes wrong. It turns "can we build this?" into "should this act on its own, what can it reach, who answers for it, and who can stop it?"

The decision it supports is a release and autonomy decision: which tier of oversight an agent gets, whether it may ship, and what evidence keeps it running. Governance is not a gate at the end. The sources treat it as a loop that runs from intake through retirement.

## What the sources agree on

1. **Govern by risk tier, not one checklist.** Risk follows what an agent can do, how reversible its actions are, how autonomous it is and what data it touches. A uniform process slows simple agents and under-protects consequential ones. *Fact (convergent guidance):* [IMDA framework](https://www.imda.gov.sg/-/media/imda/files/about/emerging-tech-and-research/artificial-intelligence/mgf-for-agentic-ai.pdf), [Microsoft, Govern agents by risk](https://learn.microsoft.com/en-us/agents/center-of-excellence/govern-agents-risk), [EY, Six steps](https://www.ey.com/en_ca/insights/assurance/technology-risk/six-steps-to-enhance-agentic-ai-governance), [KPMG](https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2025/ai-governance-for-agentic-ai-era.pdf), [NIST AI RMF](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf).
2. **Keep an inventory with a named owner.** You cannot review, monitor or retire what you do not know exists. *Fact (all vendor or consultancy guidance, so the practice is consistent but not independently tested):* [Microsoft, Govern and secure](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/governance-security-across-organization), [IBM, agent sprawl](https://www.ibm.com/think/topics/ai-agent-sprawl), [Forrester, control plane](https://www.forrester.com/blogs/announcing-our-evaluation-of-the-agent-control-plane-market/), [Accenture](https://www.accenture.com/en/insights/consulting/operating-model-age-of-ai).
3. **Give each agent its own identity and the least privilege its task needs.** Inheriting a user's full permissions or sharing a generic service account makes errors and attacks larger and untraceable. *Fact:* [ACSC and partner agencies](https://www.cyber.gov.au/business-government/secure-design/artificial-intelligence/careful-adoption-of-agentic-ai-services), [CSA on NIST work](https://labs.cloudsecurityalliance.org/research/csa-research-note-nist-ai-agent-red-teaming-standards-202603/), [Microsoft, Secure agents](https://learn.microsoft.com/en-us/agents/center-of-excellence/secure-agents), [MCP authorization](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization), [MCP security](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices).
4. **Enforce limits outside the model.** Prompt instructions are weak controls; deterministic checks at a gateway, sandbox or service hold up better. *Fact (design position):* [AWS AgentCore policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html), [Anthropic, Securely deploying](https://platform.claude.com/docs/en/agent-sdk/secure-deployment), [Broda, task grants](https://agenticmesh.substack.com/p/secure-agent-authorization-tasks), [AISI incident report](https://www.aisi.gov.uk/blog/incident-report-unsanctioned-agent-behaviour-during-cyber-testing). *Inference:* the benchmark evidence below supports this, because prompt-only defenses underperformed. See [Agent-SafetyBench](https://arxiv.org/abs/2412.14470) and [AgentHarm](https://arxiv.org/abs/2410.09024).
5. **Human oversight must be designed to work.** Name competent overseers, give them authority and a stop control, require approval at significant or irreversible steps, and measure whether approvals are real, for example override rates. *Fact:* [EU AI Act Art. 14](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14), [Art. 26](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26), [IMDA](https://www.imda.gov.sg/-/media/imda/files/about/emerging-tech-and-research/artificial-intelligence/mgf-for-agentic-ai.pdf). Evidence of how oversight changes in practice: [Anthropic, autonomy in practice](https://www.anthropic.com/research/measuring-agent-autonomy) (vendor data, coding-heavy).
6. **Agents are attacked through content they read.** Prompt injection, tool misuse, memory poisoning and privilege abuse are the named threat classes. *Fact:* [OWASP agentic top 10](https://genai.owasp.org/2025/12/09/owasp-genai-security-project-releases-top-10-risks-and-mitigations-for-agentic-ai-security/), [NIST hijacking evaluations](https://www.nist.gov/news-events/news/2025/01/technical-blog-strengthening-ai-agent-hijacking-evaluations), [NIST red-teaming competition](https://www.nist.gov/blogs/caisi-research-blog/insights-ai-agent-security-large-scale-red-teaming-competition). NIST reported that every model tested was broken at least once, and that adaptive attacks raised success from 11% to 81% in one experiment. *Inference:* a single benchmark score is not evidence of safety.
7. **Record what agents do, and keep the records.** Logs, traces and audit trails support incident work, regulation and learning. *Fact:* [EU Art. 12](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12), [Art. 73](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-73), [Visibility into AI Agents](https://arxiv.org/abs/2401.13138), [O'Reilly Radar](https://www.oreilly.com/radar/ai-agents-need-guardrails/).
8. **Plan for the first incident before it happens.** Learn from failures without blame and track whether fixes close. *Fact (practice) and Inference (fit for agents):* [Google SRE postmortems](https://sre.google/sre-book/postmortem-culture/), [Agent Incident Registry](https://arxiv.org/abs/2609.11030).

## Where they disagree or differ

- **Standards versus selling.** Regulators and standards bodies describe duties; IBM, Microsoft, ServiceNow-style vendors and consultancies describe a "control plane" product category. [Forrester](https://www.forrester.com/blogs/agent-control-planes-still-need-a-robust-standards-stack/) itself says the standards stack is immature, and its vendor poll is small. Treat product claims such as [IBM's governance marketing](https://www.ibm.com/think/insights/ai-agent-governance) as options, not proof.
- **Where governance lives.** Forrester argues it should sit outside both build and orchestration for independence. [Microsoft](https://learn.microsoft.com/en-us/agents/center-of-excellence/govern-agents-risk) stresses connecting to existing security and risk bodies, and accountability with the domain owner. These are compatible but imply different org charts.
- **Guardrails as agents.** [McKinsey-style and IBM-style](https://www.ibm.com/think/insights/ai-agent-governance) proposals use "governance agents" to watch other agents. No source here tests that; [R-Judge-type findings](https://arxiv.org/abs/2401.10019) suggest automated judges miss many risks (Hypothesis that this applies to monitors).
- **Approval stance.** [OpenAI](https://platform.openai.com/docs/guides/agent-builder-safety) advises approval on every tool operation; [Anthropic's data](https://www.anthropic.com/research/measuring-agent-autonomy) shows experienced users move to auto-approve with active monitoring. Which is right depends on reversibility and scale.
- **Vocabulary.** Autonomy tiers, "agenticness" and agent types are named differently by [KPMG](https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2025/ai-governance-for-agentic-ai-era.pdf), [EY](https://www.ey.com/en_ca/insights/assurance/technology-risk/six-steps-to-enhance-agentic-ai-governance) and [Microsoft](https://learn.microsoft.com/en-us/agents/center-of-excellence/govern-agents-risk). Pick one and map to it.
- **Governance as a phase or a mode.** [adlc.io](https://www.adlc.io/) presents Govern as a continuous mode that checks alignment with intent; this is the author's hypothesis, and the library's phase structure is a simplification of it.

## What to do in this phase

1. **Classify the agent (product lead, risk, security).** Decide on the assist-versus-execute line, data touched, reversibility and external exposure. Evidence: a one-page risk record using a tier scheme you choose.
2. **Assign accountability (executive sponsor, product owner).** Name a business owner, a technical owner and an overseer. Evidence: names recorded in the inventory before build proceeds.
3. **Bound access by design (engineering, security).** Decide identity, scoped credentials, tool allowlist, network egress, memory scope and sandboxing. Evidence: a permissions map reviewed by someone outside the build team.
4. **Set decision rights and approval points (product, legal, operations).** Specify what the agent may do alone, what needs approval, and what it must never do. Include the stop control.
5. **Test adversarially (security, evaluation lead).** Run red-team and misuse tests, with repeated attempts and per-attack-type reporting, not one average. Evidence: results tied to a version.
6. **Check compliance obligations (legal, compliance).** Map the use case to applicable rules, for example EU high-risk duties for deployers, logging, worker notification and incident reporting deadlines.
7. **Release gradually (product, operations).** Limited users first, with monitoring thresholds and rollback agreed in advance.
8. **Run the loop (owner, overseer).** Review logs, overrides, incidents and drift on a schedule; rerun tests when the model, prompt or tool changes.
9. **Close or retire (owner, IT, legal).** Revoke credentials, archive or delete memory, tell dependents.

## Artifacts this phase should produce

| Artifact | Purpose | Minimum contents |
|---|---|---|
| Agent inventory entry | Make the agent visible | Owner, purpose, tools, data, identity, tier, version, status |
| Risk and tier record | Justify oversight level | Autonomy, reversibility, data, exposure, residual risk accepted by whom |
| Permissions map | Show least privilege | Identity, scopes, allowed tools, egress, memory scope |
| Decision-rights sheet | Define autonomy limits | Allowed alone, needs approval, prohibited, stop procedure |
| Red-team and misuse report | Show adversarial testing | Attack types, attempts, success per type, agent version |
| Oversight evidence | Show oversight is real | Approval counts, override rates, response times |
| Incident and escalation plan | Prepare for failure | Triggers, contacts, reporting duties, postmortem template |
| Retirement checklist | Prevent orphaned access | Credential revocation, data disposition, dependents notified |

## Questions a product leader should ask

1. Who is the named owner of this agent, and can they stop it today?
2. What is the worst action it can take with the access it holds, and is that reversible?
3. Does it act as itself or inherit someone's permissions?
4. Which limits are enforced outside the model, and which rely on instructions?
5. Where do approvals sit, and what do override rates say about whether anyone is really checking?
6. What untrusted content does it read, and what could that content make it do?
7. How were the tests designed, with repeated attempts and attacks tuned to this system?
8. What do we log, for how long, and could we reconstruct an incident?
9. What regulation or contract obligation applies, and who has confirmed that?
10. What changes trigger a re-review: model, prompt, tool, data, user group?
11. What would we do in the first hour of an incident?
12. How does this agent get retired, and who finds out?

## Failure modes

- **Governance theater:** policies exist but nothing enforces them. Warning sign: no measure of actions logged or violations blocked ([O'Reilly Radar](https://www.oreilly.com/radar/ai-agents-need-guardrails/)).
- **Ambient authority:** the agent can reach more than its task needs. Warning sign: it runs under an employee's or shared account ([Broda](https://agenticmesh.substack.com/p/secure-agent-authorization-tasks)).
- **Rubber-stamp oversight:** approvals become habit. Warning sign: near-zero overrides ([IMDA](https://www.imda.gov.sg/-/media/imda/files/about/emerging-tech-and-research/artificial-intelligence/mgf-for-agentic-ai.pdf)).
- **Sprawl and shadow agents:** teams build outside review. Warning sign: nobody can say how many agents exist ([IBM](https://www.ibm.com/think/topics/ai-agent-sprawl)).
- **Retrofitted controls:** governance added after launch. Warning sign: identity and data decisions left to "later" ([BCG](https://www.bcg.com/publications/2026/building-enterprise-ai-agents-in-regulated-industries), [Deloitte](https://www.deloitte.com/us/en/insights/topics/emerging-technologies/ai-agents-scaling-faster.html)).
- **Silent configuration gaps:** a setting weakens a protection. Warning sign: agent-level guardrails replace model-level ones unnoticed ([Microsoft Foundry](https://learn.microsoft.com/en-us/azure/foundry/guardrails/guardrails-overview)).
- **Permissive test conditions reaching production:** [AISI's report](https://www.aisi.gov.uk/blog/incident-report-unsanctioned-agent-behaviour-during-cyber-testing) describes out-of-scope actions when internet access was open and classifiers were off.
- **Opaque disclosure:** relying on vendors' safety claims. Warning sign: no third-party evaluation ([MIT AI Agent Index](https://aiagentindex.mit.edu/)).

## Gaps in the evidence

This phase has strong coverage (50 sources used from 148 tagged), but quality is uneven.

- **Unknown:** how well any of these controls reduce real incidents. Most controls come from vendor guidance or standards that prescribe, not measure. The incident registry counts events in its own collection, not deployment risk.
- **Unverified:** survey figures from consultancies and vendors (adoption, readiness, sprawl). They are self-reported and often second-hand.
- **Gap:** the EU AI Act articles apply to high-risk systems; whether your agent qualifies is a legal question the corpus does not answer. Summaries are explanatory, not legally binding.
- **Gap:** NIST agent overlays and identity guidance are drafts; treat as Unknown until final. The RMF predates agents.
- **Gap:** benchmark results (2023 to 2024) are dated; current models differ.
- **Gap:** little on cost of governance, small-team practice, or product-management-specific governance.
- Licenses are "not verified" throughout except where stated: UK DSIT Code of Practice (Open Government Licence v3.0) and Google PAIR (CC BY-NC-SA 4.0). Read the original before reusing text.

## Sources

Publisher and date shown; see the bibliography for details.

- [NIST AI RMF 1.0](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf), NIST, 2023-01, risk functions
- [NIST generative AI profile](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf), NIST, 2024-07, risk areas
- [EU AI Act Art. 9](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-9), EC Service Desk, 2024-06, risk management
- [EU AI Act Art. 12](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12), same, record-keeping
- [EU AI Act Art. 14](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14), same, oversight
- [EU AI Act Art. 26](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26), same, deployer duties
- [EU AI Act Art. 73](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-73), same, incident reporting
- [IMDA agentic framework v1.5](https://www.imda.gov.sg/-/media/imda/files/about/emerging-tech-and-research/artificial-intelligence/mgf-for-agentic-ai.pdf), IMDA Singapore, 2026-05, agent governance
- [ACSC agentic adoption](https://www.cyber.gov.au/business-government/secure-design/artificial-intelligence/careful-adoption-of-agentic-ai-services), ACSC and partners, 2026-05, risk groups
- [OWASP agentic top 10](https://genai.owasp.org/2025/12/09/owasp-genai-security-project-releases-top-10-risks-and-mitigations-for-agentic-ai-security/), OWASP, 2025-12, threats
- [NIST hijacking evaluations](https://www.nist.gov/news-events/news/2025/01/technical-blog-strengthening-ai-agent-hijacking-evaluations), NIST CAISI, 2025-01, adaptive attacks
- [NIST red-teaming competition](https://www.nist.gov/blogs/caisi-research-blog/insights-ai-agent-security-large-scale-red-teaming-competition), NIST CAISI, 2026-03, attack results
- [NIST agent standards initiative](https://www.nist.gov/artificial-intelligence/ai-agent-standards-initiative), NIST CAISI, 2026-02, identity work
- [CSA on NIST guidance](https://labs.cloudsecurityalliance.org/research/csa-research-note-nist-ai-agent-red-teaming-standards-202603/), CSA, 2026-03, secondary summary
- [MCP authorization](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization), MCP project, 2025-11, tokens and scopes
- [MCP security practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices), MCP project, 2026-07, confused deputy
- [AISI incident report](https://www.aisi.gov.uk/blog/incident-report-unsanctioned-agent-behaviour-during-cyber-testing), UK AISI, 2026-08, out-of-scope actions
- [UK Code of Practice](https://www.gov.uk/government/publications/ai-cyber-security-code-of-practice/code-of-practice-for-the-cyber-security-of-ai), UK DSIT, 2025-01, lifecycle security
- [Microsoft, Govern agents by risk](https://learn.microsoft.com/en-us/agents/center-of-excellence/govern-agents-risk), Microsoft, 2026-07, tiers
- [Microsoft, Govern and secure](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/governance-security-across-organization), Microsoft, 2026-04, baseline
- [Microsoft, Secure agents](https://learn.microsoft.com/en-us/agents/center-of-excellence/secure-agents), Microsoft, 2026-07, identity
- [Microsoft Foundry guardrails](https://learn.microsoft.com/en-us/azure/foundry/guardrails/guardrails-overview), Microsoft, 2026-07, guardrail points
- [Microsoft Foundry control plane](https://learn.microsoft.com/en-us/azure/foundry/control-plane/how-to-manage-agents), Microsoft, 2026-07, fleet inventory
- [Microsoft, Manage the lifecycle](https://learn.microsoft.com/en-us/agents/center-of-excellence/agent-lifecycle), Microsoft, 2026-07, ownership
- [IBM, agent sprawl](https://www.ibm.com/think/topics/ai-agent-sprawl), IBM, 2026-04, sprawl
- [IBM, control plane](https://www.ibm.com/think/topics/agent-control-plane), IBM, undated, control concept
- [IBM, agent governance](https://www.ibm.com/think/insights/ai-agent-governance), IBM, undated, marketing
- [adlc.io home](https://www.adlc.io/), adlc.io, undated, Govern mode
- [Forrester, market evaluation](https://www.forrester.com/blogs/announcing-our-evaluation-of-the-agent-control-plane-market/), Forrester, 2025-12, three planes
- [Forrester, standards stack](https://www.forrester.com/blogs/agent-control-planes-still-need-a-robust-standards-stack/), Forrester, 2026-03, standards gaps
- [KPMG, AI governance](https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2025/ai-governance-for-agentic-ai-era.pdf), KPMG, 2025-07, ten controls
- [EY, Six steps](https://www.ey.com/en_ca/insights/assurance/technology-risk/six-steps-to-enhance-agentic-ai-governance), EY, 2026-01, risk-matched governance
- [Deloitte, guardrails](https://www.deloitte.com/us/en/insights/topics/emerging-technologies/ai-agents-scaling-faster.html), Deloitte, 2026-04, survey
- [BCG, regulated industries](https://www.bcg.com/publications/2026/building-enterprise-ai-agents-in-regulated-industries), BCG, 2026-07, decide early
- [Accenture, operating model](https://www.accenture.com/en/insights/consulting/operating-model-age-of-ai), Accenture, 2026-09, owners
- [Broda, task grants](https://agenticmesh.substack.com/p/secure-agent-authorization-tasks), Broda, 2026-06, authorization
- [MIT AI Agent Index 2025](https://aiagentindex.mit.edu/), MIT project, undated, disclosure gaps
- [AI Agent Index 2024](https://arxiv.org/abs/2502.01635), Casper et al., 2025-02, safety disclosure
- [O'Reilly, guardrails](https://www.oreilly.com/radar/ai-agents-need-guardrails/), O'Reilly Radar, 2025-12, governance engineering
- [Google SRE, postmortems](https://sre.google/sre-book/postmortem-culture/), Google SRE, undated, blameless review
- [Agent Incident Registry](https://arxiv.org/abs/2609.11030), Kumar et al., 2026-09, incident coding
- [Anthropic, Securely deploying](https://platform.claude.com/docs/en/agent-sdk/secure-deployment), Anthropic, undated, isolation
- [OpenAI, Safety in building agents](https://platform.openai.com/docs/guides/agent-builder-safety), OpenAI, undated, injection
- [AWS AgentCore policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html), AWS, undated, gateway policy
- [Agent-SafetyBench](https://arxiv.org/abs/2412.14470), Zhang et al., 2024-12, safety scores
- [AgentHarm](https://arxiv.org/abs/2410.09024), Andriushchenko et al., 2024-10, harmful tasks
- [R-Judge](https://arxiv.org/abs/2401.10019), Yuan et al., 2024-01, risk awareness
- [Visibility into AI Agents](https://arxiv.org/abs/2401.13138), Chan et al., 2024-01, logging and monitoring
- [Anthropic, autonomy in practice](https://www.anthropic.com/research/measuring-agent-autonomy), Anthropic, 2026-02, approval behavior
