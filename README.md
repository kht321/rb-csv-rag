# File legend

| File | Contents |
|---|---|
| [`t1.pdf`](t1.pdf) | Tab. 2 extended with Claude SRS→SVTP rows (BERTScore, ROUGE-L, chrF++). |
| [`t2.pdf`](t2.pdf) | bge-m3 cosine similarities between deontic modal pairs. |
| [`t3.pdf`](t3.pdf) | Compliance metrics on the 1,862-document proprietary corpus. |
| [`t4.pdf`](t4.pdf) | BM25 vs hybrid vs dense retrieval comparison. |
| [`t5.pdf`](t5.pdf) | Full SCS regex pattern table. |
| [`t6.pdf`](t6.pdf) | Per-model compliance/BERTScore sensitivity ratio across seeds. |
| [`f1.pdf`](f1.pdf) | BERTScore vs TPS scatter, Pearson r = −0.601. |
| [`refs.pdf`](refs.pdf) | Bibliography audit (verified against DBLP, CrossRef, Zotero). |
| [`supp.zip`](supp.zip) | Revised supplementary archive (original + `CHANGES.md` + `GENERATION.md`; metadata.json fields corrected per `CHANGES.md`). |
| [`clean_r.csv`](clean_r.csv) | Per-model BERTScore vs TPS on full SRS→SVTP corpus vs the artifact-free 80.15% subset (rows where neither SRS source nor SVTP reference contains the doubled-`shall` or audit-trail substrings). Pearson r = −0.598 full / −0.571 clean. |
| [`clean_r.py`](clean_r.py) | Reproducer script for `clean_r.csv` (uses the paper's TPS implementation in `src/evaluation/compliance_metrics.py`). |
