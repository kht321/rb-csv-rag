# Rebuttal Supplementary Assets

Anonymous links shared in the UAI 2026 author response. Files are renamed to
short codes (`t1`–`t6`, `f1`, `refs`, `supp`) so each URL fits within the
2,500-character official-comment limit; this `README.md` is the legend.

## File legend

| Short | Original filename | Reviewer / Question | Description |
|---|---|---|---|
| `t1.pdf` | `table2_claude_rows.pdf` | R4 Q4-4(b) | Tab. 2 extended with BERTScore 0.880, ROUGE-L 0.423, chrF++ 0.571 rows for Claude (SRS→SVTP, mean over 5 seeds). |
| `t2.pdf` | `table_cosine_modal_similarity.pdf` | R2 Q4-2, R3 Q4-1 | bge-m3 cosine similarities between deontic modal pairs (`shall`/`should`/`must`); shows the modal collapse that explains hybrid retrieval failure on URS→SRS. |
| `t3.pdf` | `table_proprietary_compliance.pdf` | R4 Q4-3 | RKCR/RCR/SCS/TPS on the 1,862-document proprietary corpus (3 systems, 5 seeds, 6 OSS models); confirms BERTScore/compliance divergence is not a synthetic artifact. |
| `t4.pdf` | `table_retrieval_comparison.pdf` | R4 Q4-4(c) | BM25 vs Hybrid (bge-m3) vs standalone Dense (bge-m3); BM25 > Hybrid > Dense on both tasks. |
| `t5.pdf` | `table_scs_patterns.pdf` | R3 Q4-5 | Full SCS regex pattern table — 8 structural elements, both tasks, with example trigger strings. |
| `t6.pdf` | `table_seed_sensitivity.pdf` | R3 Q4-3, R4 Q4-2, R5 Q4-3 | Per-model compliance/BERTScore sensitivity ratio across 5 retrieval seeds; SCS 5–25×, TPS 4–23× more sensitive than BERTScore on SRS→SVTP. |
| `f1.pdf` | `figure_bertscore_tps_scatter.pdf` | R2 Q5-1, R5 Q4-3 | BERTScore vs TPS scatter (SRS→SVTP, 6 OSS models + Claude); Pearson r = −0.601. |
| `refs.pdf` | `references_audit.pdf` | R5 Q4-4 | **Rebuttal-time addendum (not part of the supplementary archive).** Bibliography audit for the paper's `references.bib`: each cited entry verified against DBLP, CrossRef, and the authors' Zotero library on 2026-05-01, with clickable DOIs. Five entries listed at the end as verification-failed (4 from round-1 audit + Mills 2015). |
| `supp.zip` | `supplementary_uai2026_revised.zip` | R5 Q4-1, Q4-2 | Revised supplementary archive. Identical to the originally submitted archive except for: (i) `metadata.json` corrections (cutoff, top_p, Claude model ID, model set), (ii) added `GENERATION.md` with truthful disclosure of the two known synthetic-corpus artifacts, (iii) added `CHANGES.md`. No expansion of the experiment-reproducibility footprint. |

## Notes

- All files are anonymized and contain no author-identifying information.
- Links are provided for reviewer convenience; the response remains complete without them.
- `supp.zip` adds only what is needed to address R5's Q4-1 (paper↔supp metadata mismatches) and Q4-2 (synthetic-corpus disclosure) — the experiment-reproducibility content is otherwise unchanged from the originally submitted archive. `GENERATION.md` quantifies, rather than claims removal of, the two known synthetic-corpus artifacts (doubled "shall" pattern, repeated audit-trail closing clause); the 1,862-document proprietary corpus used in §4.7 is artifact-free.
- `refs.pdf` is a rebuttal-time bibliography audit of the *paper's* `references.bib`. It is provided here for reviewer convenience and is not packaged inside `supp.zip`.
