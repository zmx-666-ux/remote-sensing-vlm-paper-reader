# Installation

Install the public Plugin from its GitHub marketplace, or copy only the Skill directory for local development.

## Requirements

- Codex Desktop or a current Codex CLI with Skills support.
- A local research-library directory outside this repository.
- A readable paper PDF for the fallback workflow.
- Optional: Paper Pilot; see [Paper Pilot setup](paper-pilot-setup.md).

## Local development installation

Clone or download the repository, open PowerShell in its root, and copy only the Skill directory into your personal Codex Skills directory. The following command deliberately stops if a directory with the same name already exists so it cannot silently overwrite your customizations.

```powershell
$source = (Resolve-Path '.\skills\remote-sensing-vlm-paper-reader').Path
$destination = Join-Path $env:USERPROFILE '.codex\skills\remote-sensing-vlm-paper-reader'
if (Test-Path -LiteralPath $destination) {
    throw "Destination already exists: $destination. Back it up or remove it intentionally before upgrading."
}
Copy-Item -LiteralPath $source -Destination $destination -Recurse
```

Restart Codex, start a new task, and ask it to use “Remote Sensing VLM Paper Reader” on a local PDF. If the Skill does not activate, confirm that this file exists:

```text
%USERPROFILE%\.codex\skills\remote-sensing-vlm-paper-reader\SKILL.md
```

For an upgrade, compare your installed copy with the new release first. Back up personal edits, replace the installed Skill intentionally, then restart Codex.

## Public GitHub Plugin installation

The verified public identity is `zmx-666-ux/remote-sensing-vlm-paper-reader`.

```powershell
codex plugin marketplace add zmx-666-ux/remote-sensing-vlm-paper-reader
codex plugin marketplace list
codex plugin list --available --json
codex plugin add remote-sensing-vlm-paper-reader@remote-sensing-vlm-paper-reader
```

The first command adds the public Git marketplace. The listing steps let you inspect its resolved name and Plugin entry before installation. Restart Codex and start a new task after installing or upgrading so the Skill is loaded into the new task.

## Verify behavior

Use the [synthetic request](../examples/synthetic-example/example-request.md) before touching private research data. Confirm that the response:

- asks for or respects a private library outside the Plugin;
- uses the selected reading mode;
- cites PDF pages rather than viewer counters;
- labels author claim, evidence, and inference separately;
- updates an existing idea row instead of deleting it.

Keep PDFs, populated notes, and populated ledgers out of the cloned repository. See the [privacy policy](../README.md#privacy-and-evidence-policy).
