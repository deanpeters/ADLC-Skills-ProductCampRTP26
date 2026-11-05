# Plugin packages

Version **0.6.0** contains eleven instructional skills for ProductCamp RTP 2026 attendees.

| Download | Intended application | Contents |
|---|---|---|
| [claude.plugin](claude.plugin) | Claude Code / Claude Cowork | Claude manifest, skills, reference, findings, root README, and license. |
| [codex.plugin](codex.plugin) | Codex | Codex compatibility manifest, skills, reference, findings, root README, and license. |

These are ZIP archives with a `.plugin` extension. Download the raw file rather than saving GitHub's preview page. Rename a local copy to `.zip` if your file picker requires that extension. Application support and installation options vary; see the [installation guidance](../README.md#install).

The Claude marketplace is named `adlc-productcamp-rtp26`; its plugin is `adlc`. The marketplace catalog stays in the repository and is not bundled inside either archive.

## Rebuild

From the repository root, with the `zip` command installed:

```bash
zip -qrFS plugins/claude.plugin .claude-plugin/plugin.json skills reference findings README.md LICENSE -x "*.DS_Store"
zip -qrFS plugins/codex.plugin .codex-plugin skills reference findings README.md LICENSE -x "*.DS_Store"
```

Keep the manifests and marketplace at the same version, and rebuild both archives after changing a bundled file. The archives preserve relative paths. They include no deck files, raw research, private working notes, or evaluation transcripts.

Packaging checks establish archive contents and metadata, not behavioral validation or a successful installation in every application.
