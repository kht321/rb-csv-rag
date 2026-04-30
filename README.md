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
| `refs.pdf` | `references_audit.pdf` | R5 Q4-4 | Bibliography audit. Each cited entry verified against DBLP or CrossRef on 2026-05-01; clickable DOIs. Five entries removed (4 from round-1 audit + Mills 2015) with verification notes. |
| `supp.zip` | `supplementary_uai2026_revised.zip` | R5 Q4-1, Q4-2 | Revised supplementary archive (1.1 GB uncompressed → 7.4 MB zipped without large dependencies). Includes corrected `metadata.json` files (cutoff, top_p, model ID, model set) and `GENERATION.md` with truthful disclosure of the two known synthetic-corpus artifacts. |

## Notes

- All files are anonymized and contain no author-identifying information.
- Links are provided for reviewer convenience; the response remains complete without them.
- `supp.zip` ships an updated `CHANGES.md` and `GENERATION.md` that quantify, rather than claim removal of, the two synthetic-corpus artifacts (doubled "shall" pattern, repeated audit-trail closing clause). The 1,862-document proprietary corpus referenced in the paper's §4.7 is artifact-free.
