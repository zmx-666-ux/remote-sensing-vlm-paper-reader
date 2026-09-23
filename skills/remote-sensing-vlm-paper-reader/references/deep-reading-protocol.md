# Deep-reading protocol

Select the least expensive mode that answers the user's decision. Upgrade modes when the paper becomes central; do not downgrade a requested full read into an abstract summary.

## Evidence contract shared by every mode

- Identify the exact title, authors, year, venue or preprint version, and PDF page-number convention.
- Distinguish author claims, experimental evidence, and analysis/inference.
- Cite PDF pages for method definitions, figures, quantitative results, ablations, and stated limitations.
- Inspect decisive figures and tables visually when rendering is available.
- Report inaccessible pages, extraction warnings, missing code, and missing training details.
- Do not infer novelty, superiority, or reproducibility from the abstract alone.

## Quick screening

Return: task and modality; central idea; evidence available; relevance to remote-sensing VLM/change detection; code/data availability; likely reading value; and a `精读`, `选读`, or `暂不读` recommendation. Read enough method and experiment content to support that decision.

## Beginner deep reading

Start with prerequisites and a plain-language problem statement. Then explain the input-output contract, method pipeline, decisive figure, objectives, evidence, and limitations. Introduce each unfamiliar term before using it technically.

For every central equation, use this order:

1. symbol table and units or semantic meaning;
2. tensor shapes before and after the operation;
3. computation in words;
4. why the operation may help;
5. one small numerical or shape example;
6. assumptions and failure conditions.

End with five active-recall questions. Keep answers separate so the user can attempt retrieval first.

## Reproduction analysis

Extract: official code and license; datasets and splits; preprocessing; architecture versions; frozen/trainable modules; training stages; objectives and weights; optimizer/schedule; batch size; precision; epochs; augmentation; inference; seed/reporting protocol; hardware; parameter/FLOP/memory evidence; missing details; and the smallest credible reproduction.

Estimate A800 80GB feasibility only when the paper or code provides enough dimensions. Label calculated estimates and list assumptions. Separate exact reproduction from an affordable diagnostic reproduction.

## Innovation analysis

Express each candidate as a falsifiable hypothesis, not a novelty claim. Record the nearest known work, apparent difference, why the difference could matter, required public data, implementation burden, failure risk, and the minimum experiment that would change the decision. Mark literature search coverage and unresolved uncertainty.

## Cross-paper comparison

Normalize task definition, datasets, metrics, backbones, training resources, and evaluation protocols before comparing results. Explain when metrics are not directly comparable. Update the ledger with relationships such as `extends`, `contradicts`, `replaces`, `combines`, or `uses under different conditions`.

## Completion report

Summarize five deltas: knowledge added, prior judgment revised, idea or module downgraded, item archived, and question left unresolved. Omit empty categories rather than inventing activity.
