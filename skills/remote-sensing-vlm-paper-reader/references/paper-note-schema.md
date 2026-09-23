# Word paper-note schema

Create one note per stable paper ID. Name it `Pxxx_年份_论文简称_精读笔记.docx`. Use PDF page numbers, not viewer counters, and state the mapping when they differ.

## Required sections

1. **论文身份信息** — stable ID, title, authors, year, venue/version, DOI/arXiv, PDF path, code/data links, reading mode and date.
2. **一句话问题与核心结论** — problem, claimed answer, and where the paper sits in the field.
3. **阅读前置知识** — only concepts required to understand this paper, explained before formal use.
4. **方法流程** — input, encoders, temporal interaction, cross-modal fusion, prediction head, outputs, and training stages.
5. **关键图表** — figure/table purpose, how to read it, supported conclusion, and PDF page.
6. **关键公式** — symbols, tensor shapes, computation, motivation, example, assumptions, and page.
7. **实验与证据** — datasets, splits, metrics, comparable baselines, main results, ablations, robustness, efficiency, and missing evidence.
8. **主张、证据与推断** — a three-column table separating `作者主张`, `证据支持范围`, and `分析/推断`.
9. **局限与失败条件** — stated limitations plus evidence-grounded risks; label which source each limitation comes from.
10. **对研究台账的影响** — paper rows, idea IDs, method IDs, comparison changes, and unresolved questions to update.
11. **主动回忆** — five questions first, followed by a visually separated answer section.
12. **PDF页码索引** — claim/topic, PDF page, figure/table/equation, and note section.

## Writing quality

- Start each technical section with a short plain-language verdict.
- Prefer diagrams, tables, or short sequences when they clarify relationships; avoid decorative structure.
- Preserve uncertainty. Use `未找到`, `论文未报告`, or `需要代码验证` instead of guessing.
- Do not copy long paper passages. Paraphrase and retain the page evidence.
- Do not turn every tentative inspiration into a separate Word file; send it to the Excel innovation ledger first.
