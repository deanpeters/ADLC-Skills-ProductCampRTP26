# ADLC Skills · ProductCamp RTP 2026

From the ProductCamp RTP 2026 talk 'ADLC: What It Is & What It Ain't' by Dean Peters.

Instructional skills that help Product Managers shape, secure, and ship AI agents with humans at the helm. Each skill helps you make an artifact, name the evidence, and stop at a human decision.

This is Dean's personal attendee edition of instructional material developed with Productside. It is a set of digital takeaways, not a software product or a certification that an agent is ready to ship.

**Start here:** [Try Kevin: three skills in ten minutes](https://github.com/deanpeters/ADLC-Skills-ProductCampRTP26/blob/main/examples/try-it-kevin/TRY-IT.md).

## The six-stage loop

Enter where your current work needs help. Evidence can send you back to an earlier stage.

| Stage | Skill | What you leave with |
|---|---|---|
| Intent | [Frame Intent](skills/adlc-step1-frame-intent/SKILL.md) | An Agent Intent Brief: whose work changes, why, and within what limits. |
| Design | [Design Agent System](skills/adlc-step2-design-agent-system/SKILL.md) | An Agent System Map: tools, context, memory, and control boundaries. |
| Harness | [Generate Agent Harness](skills/adlc-step3-generate-agent-harness/SKILL.md) | An Agent Harness Brief: an inspectable build plan and test surface. |
| Validate | [Validate Agent Behavior](skills/adlc-step4-validate-agent-behavior/SKILL.md) | A Validation Pack: expected behavior, failure cases, and evidence. |
| Deploy | [Deploy With Governance](skills/adlc-step5-deploy-with-governance/SKILL.md) | A Governed Deployment Plan: launch gates, oversight, rollback, and stop authority. |
| Observe | [Observe And Improve](skills/adlc-step6-observe-and-improve/SKILL.md) | An Observation Review: improve, reframe, restrict, or retire. |

## Five utilities

| Skill | What it helps you decide |
|---|---|
| [Agent Strategy Canvas](skills/adlc-util-agent-strategy-canvas/SKILL.md) | Is the agent's problem, scope, and value worth pursuing? |
| [Solution Hypothesis](skills/adlc-util-solution-hypothesis/SKILL.md) | What must be true, and what small tests could change the decision? |
| [Minimum Viable Narrative](skills/adlc-util-minimum-viable-narrative/SKILL.md) | What human journey should a prototype let us test? |
| [Constraint Decay Check](skills/adlc-util-decay-check/SKILL.md) | What changed without a matching change in constraints? |
| [Product Lifecycle Check](skills/adlc-util-plc-check/SKILL.md) | Has the product changed enough that the agent's job should change too? |

## Install or read

You need access to the application you choose. These files do not supply an account, model, or API key.

### Claude Code

In a Claude Code session, run these commands one at a time:

```text
/plugin marketplace add deanpeters/ADLC-Skills-ProductCampRTP26
/plugin install adlc@adlc-productcamp-rtp26
```

Start a new session after installation. Invoke a skill by its namespaced command, for example:

```text
/adlc:adlc-util-agent-strategy-canvas
```

### Claude Cowork

Download [claude.plugin](https://github.com/deanpeters/ADLC-Skills-ProductCampRTP26/blob/main/plugins/claude.plugin) using GitHub's download button. Upload it through Cowork's plugin interface. If the file picker requires a `.zip` extension, rename the downloaded copy to `claude.zip`; its contents are already a ZIP archive. Start a new session after enabling it.

### Codex

Download [codex.plugin](https://github.com/deanpeters/ADLC-Skills-ProductCampRTP26/blob/main/plugins/codex.plugin). It contains the Codex compatibility manifest, all eleven skills, and their supporting material. Plugin installation options vary by Codex surface: use a local plugin or marketplace workflow supported by your version. See [OpenAI's plugin documentation](https://developers.openai.com/plugins/build/plugins).

For a route that does not need plugin installation, download this repository with **Code → Download ZIP**, extract it, and open the folder as your project. Ask Codex to read the chosen `skills/<skill-name>/SKILL.md`, follow its linked references, and run it in your chosen mode. This uses the files directly; it does not register the plugin.

### Any chatbot that accepts files

Download and extract this repository. Provide the chosen skill's `SKILL.md`, `template.md`, and the supporting references it requests. Ask it to follow those instructions in Guided, Context dump, or Best guess mode. If it cannot read a linked file, supply that file before proceeding.

## What to expect

- **Guided** asks one question at a time and reuses what you already supplied.
- **Context dump** organizes the context you give it and identifies gaps.
- **Best guess** drafts with labeled assumptions and unknowns.
- Every mode stops for a human decision. A generated artifact does not approve an agent, authorize access, or establish readiness.

Every example is synthetic and invented for teaching. Start with fictional inputs; keep customer records, credentials, and confidential material out of your practice session.

These are instructional takeaways. They have structural checks and synthetic examples; they are not a claim of completed real-world usability testing or production effectiveness. Review the output before using it to make decisions.

ADLC is not a settled standard, and nobody owns it. These skills express one practical approach. Other organizations use the term differently.

## Sources and license

The [glossary](reference/glossary.md) explains the terms. The [findings](findings/adlc-working-model.md) and [bibliography](findings/bibliography.md) credit the guidance behind the skills. Linked third-party works retain their own rights and terms.

Credit: Dean Peters and Productside. This attendee edition preserves the source material's [CC BY-NC-SA 4.0 license](LICENSE): share and adapt it, give credit, keep use non-commercial, identify your changes, and distribute adaptations under the same license. This license does not grant rights to third-party works or trademarks.

Package version: **0.6.0**. [Package contents and rebuild commands](https://github.com/deanpeters/ADLC-Skills-ProductCampRTP26/blob/main/plugins/README.md).
