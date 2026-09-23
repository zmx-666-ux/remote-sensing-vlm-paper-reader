# Knowledge update policy

The current active view should be concise; the underlying history should remain traceable. Update status and relationships instead of deleting inconvenient evidence.

## Compare before creating

For each proposed idea or module, compare problem, input/output, mechanism, supervision, training stage, datasets, and claimed benefit against existing active and archived rows.

| Finding | Action |
|---|---|
| Same substance | Link the new paper as additional evidence; do not create a duplicate row. |
| Partial overlap | Keep the row, narrow the claimed difference, and record the overlap. |
| Fully proposed earlier | Mark `被已有工作覆盖`; identify the covering paper and residual difference. |
| Evidence contradicts the benefit | Mark the idea `已否定` or module `效果存疑`; record conditions and evidence. |
| Better successor exists | Mark the old module `被替代` and link the successor; preserve reusable parts. |
| Promising after search | Move the idea toward `候选` or `值得实验`; record search coverage and uncertainty. |
| Adopted in experiments | Mark `实验中` or `已采用` and link the experiment record. |

## Novelty discipline

`未在当前检索中发现` is not equivalent to `首次提出`. Record databases, query concepts, date, and inaccessible literature. Treat novelty as unresolved until the search and mechanism comparison are adequate for the decision.

## File safety

- Resolve the intended private-library root before any write.
- Check destination existence and Office lock files before creating or replacing artifacts.
- If provenance is unclear, stop and report the exact path; do not create an alternate file that silently forks the source of truth.
- Archive independent Word files under the designated archive directory and keep their ledger rows and paths.
- Never move, rename, or delete a PDF solely because its reading status changed.

## Report every update batch

Return a compact change report with: rows created, rows revised, status changes with reasons, documents archived, relationships added, and questions left unresolved. If no change was justified, say so.
