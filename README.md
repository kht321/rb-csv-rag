# Rebuttal Supplementary Assets

This folder contains figures and tables shared as anonymous links in the UAI 2026
author response. Per UAI policy, links are permitted only for figures (including
tables rendered as figures) and their captions.

## Assets

| File | Reviewer / Question | Description |
|---|---|---|
| `table_proprietary_compliance.pdf` | R4 Q4-3 | RKCR/RCR/SCS/TPS on the 1,862-document proprietary corpus (3 systems, 5 seeds); confirms BERTScore/compliance divergence is not a synthetic artifact |
| `table2_claude_rows.pdf` | R4 Q4-4(b) | Tab. 2 extended with BERTScore 0.880, ROUGE-L 0.423, chrF++ 0.571 rows for Claude (SRS→SVTP, mean over 5 seeds) |
| `table_retrieval_comparison.pdf` | R4 Q4-4(c) | BM25 vs Hybrid (bge-m3) vs standalone Dense (bge-m3); BM25 > Hybrid > Dense on both tasks |
| `table_scs_patterns.pdf` | R3 Q4-5 | Full SCS regex pattern table — 8 structural elements, both tasks, with example trigger strings |
| `table_cosine_modal_similarity.pdf` | R2 Q4-2, R3 Q4-1 | bge-m3 cosine similarities between deontic modal pairs; shows shall/should/must collapse that explains hybrid retrieval failure |
| `figure_bertscore_tps_scatter.pdf` | R2 Q5-1, R5 Q4-3 | BERTScore vs TPS scatter (SRS→SVTP model-level means); Pearson r=−0.601 anti-correlation across 6 open-source models |
| `table_seed_sensitivity.pdf` | R3 Q4-3, R4 Q4-2, R5 Q4-3 | Per-model compliance/BERTScore sensitivity ratio across 5 retrieval seeds; SCS 5–25×, TPS 4–23× more sensitive than BERTScore |

## Notes

- Links are provided for reviewer convenience; they are not required to be followed.
- All files are anonymized and contain no author-identifying information.
