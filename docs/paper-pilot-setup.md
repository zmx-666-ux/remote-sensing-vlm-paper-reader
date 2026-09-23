# Paper Pilot setup

Paper Pilot is optional, independently maintained software. This Skill can use it when its MCP tools are available, but the Plugin does not install, bundle, or guarantee Paper Pilot.

## Add the MCP server on Windows

Install `uv`/`uvx`, then run:

```powershell
codex mcp add paper_pilot -- uvx --from git+https://github.com/aytzey/paper-pilot paper-pilot
```

Restart Codex completely after adding the server. The first launch can take longer because `uvx` may download and prepare dependencies. In a new task, confirm that Paper Pilot tools are present before relying on online search or retrieval.

## Enhanced workflow

When Paper Pilot is available, the Skill may use it to search scholarly sources, retrieve an accessible paper, read consecutive full-text pages, and render decisive pages containing central figures or tables. Paper identity and version still need to be checked, and evidence should point to PDF pages.

Paper Pilot availability does not guarantee that every paywalled or withdrawn paper can be downloaded. Do not treat a search snippet or abstract as full-text evidence.

## local PDF fallback

When Paper Pilot is unavailable, attach or provide the path to a local PDF. The Skill will:

1. state that online search and retrieval were not performed;
2. read the relevant full-paper sections and decisive pages locally;
3. preserve PDF-page citations;
4. mark unresolved identity, code, data, or novelty claims as unverified.

An abstract is not a full-paper read. If only an abstract is available, use quick screening or obtain the full paper before requesting deep reading.

Scanned PDFs may contain images without a usable text layer. Run OCR first or provide a searchable version; otherwise page extraction, equations, and citations may be unreliable.

## Troubleshooting

- If tools are missing, verify the MCP entry, fully exit Codex, and restart it.
- If the first launch stalls, allow `uvx` to finish dependency installation and retry in a new task.
- If retrieval fails, use the local PDF fallback rather than inferring content from metadata.
- Keep downloaded papers and generated notes in your private research library, never in the Plugin repository.
