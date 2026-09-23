# Installation

The repository can be used as a local development Skill now. The public Plugin commands below become usable only after the repository is published and its marketplace entry has been verified.

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

The intended public identity is `zmx-666-ux/remote-sensing-vlm-paper-reader`. Do not run these commands until that repository is public and the README, release files, and owner have been verified.

```powershell
codex plugin marketplace add zmx-666-ux/remote-sensing-vlm-paper-reader
codex plugin marketplace list
codex plugin list --available --json
codex plugin add remote-sensing-vlm-paper-reader@remote-sensing-vlm-paper-reader
```

The first command accepts an `owner/repository` Git marketplace source. The listing steps let you verify the marketplace and Plugin identity before installation. If the published marketplace name differs, use the exact selector shown by `codex plugin list --available --json` instead of guessing. Restart Codex after installing or upgrading the source.

## Verify behavior

Use the [synthetic request](../examples/synthetic-example/example-request.md) before touching private research data. Confirm that the response:

- asks for or respects a private library outside the Plugin;
- uses the selected reading mode;
- cites PDF pages rather than viewer counters;
- labels author claim, evidence, and inference separately;
- updates an existing idea row instead of deleting it.

Keep PDFs, populated notes, and populated ledgers out of the cloned repository. See the [privacy policy](../README.md#privacy-and-evidence-policy).
