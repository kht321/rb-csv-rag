"""Print the file legend with SHA-256 fingerprints so reviewers can verify the
bundled rebuttal artifacts are exactly what the comment text refers to.

Usage:
    python verify.py
"""

import hashlib
import pathlib


LEGEND = {
    "f1.pdf":   "BERTScore vs TPS scatter, Pearson r = -0.601",
    "t1.pdf":   "Tab. 2 extended with Claude SRS->SVTP rows",
    "t2.pdf":   "bge-m3 cosine similarities between deontic modal pairs",
    "t3.pdf":   "Compliance metrics on the 1,862-doc proprietary corpus",
    "t4.pdf":   "BM25 vs hybrid vs dense retrieval comparison",
    "t5.pdf":   "Full SCS regex pattern table",
    "t6.pdf":   "Per-model compliance/BERTScore sensitivity ratios",
    "refs.pdf": "Bibliography audit (DBLP, CrossRef, Zotero verified)",
    "supp.zip": "Revised supplementary archive",
}


def main() -> None:
    here = pathlib.Path(__file__).parent
    for name, desc in LEGEND.items():
        p = here / name
        if not p.exists():
            print(f"  MISSING            {name:<10s}              {desc}")
            continue
        h = hashlib.sha256(p.read_bytes()).hexdigest()[:16]
        size_kb = p.stat().st_size // 1024
        print(f"  {h}  {name:<10s}  ({size_kb:>5d} KB)  {desc}")


if __name__ == "__main__":
    main()
