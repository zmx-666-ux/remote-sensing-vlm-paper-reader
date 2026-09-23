# Remote Sensing VLM Paper Reader

[简体中文](README_zh-CN.md)

A Codex Plugin for researchers who need to understand remote-sensing vision-language models (VLMs) and multimodal change-detection papers, preserve page-grounded evidence, and maintain an evolving research knowledge base.

## Scope

The Skill is intentionally narrow: remote-sensing VLMs, bi-temporal vision-language reasoning, change captioning, semantic change detection, and closely related multimodal change-detection work. It is not a generic PDF summarizer.

Choose one of five reading modes:

1. quick screening;
2. beginner deep reading;
3. reproduction analysis;
4. innovation analysis;
5. cross-paper comparison.

## What it produces

- A twelve-section Word note based on [`paper-note-template.docx`](skills/remote-sensing-vlm-paper-reader/assets/paper-note-template.docx).
- An evolving six-sheet Excel ledger based on [`research-ledger-template.xlsx`](skills/remote-sensing-vlm-paper-reader/assets/research-ledger-template.xlsx).
- Explicit separation of **author claim**, **evidence supports**, and **analysis/inference**.
- PDF-page citations for methods, figures, equations, results, and limitations.
- Status transitions for ideas and modules. A later paper changes the existing row instead of erasing research history.

See the copyright-safe [synthetic example](examples/synthetic-example/example-request.md) for the expected workflow.

## Quick start

1. Follow the [installation guide](docs/installation.md), then restart Codex.
2. Put research PDFs and generated notes in a private library outside this repository.
3. Start with a request such as:

   > Use beginner deep-reading mode on this local PDF. Explain prerequisites for an image-processing student, cite PDF pages, create the twelve-section note, and propose evidence-backed ledger updates.

[Paper Pilot](docs/paper-pilot-setup.md) is optional and independently maintained. When available, it can help with paper search, retrieval, consecutive full-text reading, and decisive-page rendering. Without it, the Skill uses a user-provided local PDF and states that online retrieval was not performed.

## Privacy and evidence policy

The repository contains reusable instructions and blank templates only. Do **not** place private PDFs, notes, unpublished ideas, personal paths, credentials, or a populated ledger in the Plugin repository. The automated privacy gate blocks PDFs and known private markers from the release set.

An abstract is not a full-paper read. Missing details are reported as `not found`, `not reported`, or `requires code verification`; they are never guessed. The Skill paraphrases rather than copying long passages.

## Known limitations

- Online search and retrieval depend on Paper Pilot, network access, and an accessible paper version.
- Scanned PDFs may require OCR before reliable page-grounded reading.
- A novelty hypothesis is not validated by one paper; it needs a separate search and comparable evidence.
- Word and Excel generation depends on the document/spreadsheet tooling available in the current Codex environment.

## Contributing

Open an issue with a minimal synthetic example, expected behavior, and observed behavior. Keep all private research material out of issues and pull requests. Changes to the workflow should preserve stable IDs, evidence links, and historical status transitions.

See [installation](docs/installation.md) and [Paper Pilot setup](docs/paper-pilot-setup.md) for details.

Released under the [MIT License](LICENSE).
