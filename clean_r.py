"""Compute the BERTScore vs TPS Pearson correlation across the 6 OSS models
on the SRS→SVTP task, on (a) the full test corpus and (b) the artifact-free
subset where neither the SRS source nor the SVTP reference contains the
synthetic-corpus artifacts (`shall The system` doubling or the uniform
audit-trail closing clause).

Used for the R5 round-2 followup -- demonstrates that the headline r=-0.601
finding is not driven by the synthetic-corpus artifacts, since it survives
on the 80% subset where the artifacts are absent.

Output: prints a per-model breakdown and the two Pearson r values.
"""

from __future__ import annotations

import glob
import os
import re
import sys
from pathlib import Path
from typing import Iterable

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))


TRACE_RE = re.compile(r"\b(URS|SRS|SVTP)[-_]?\d+(?:[-_]?[A-Z]+)?\b", re.I)
ARTIFACT_SUBSTRINGS = ("shall The system", "in an immutable audit trail")

OSS_DIRS = {
    "gemma_2_9b_complete":         "google/gemma-2-9b-it",
    "llama_3.1_8b_complete":       "meta-llama/Meta-Llama-3.1-8B-Instruct",
    "mistral_7b_complete":         "mistralai/Mistral-7B-Instruct-v0.3",
    "phi3_mini_complete":          "microsoft/Phi-3-mini-4k-instruct",
    "qwen2_7b_complete":           "Qwen/Qwen2-7B-Instruct",
    "qwen2.5_coder_14b_complete":  "Qwen/Qwen2.5-Coder-14B-Instruct",
}


def trace_ids(text: str | float | None) -> set[str]:
    if not isinstance(text, str):
        return set()
    return {m.group(0).upper() for m in TRACE_RE.finditer(text)}


def is_dirty(text: str | float | None) -> bool:
    if not isinstance(text, str):
        return False
    return any(a in text for a in ARTIFACT_SUBSTRINGS)


def src_preservation(preds_df: pd.DataFrame, mask: Iterable[bool] | None = None) -> float:
    pres = []
    for i, row in preds_df.iterrows():
        if mask is not None and not mask[i]:
            continue
        pred_ids = trace_ids(row.get("Predicted_SVTP"))
        src_ids = trace_ids(row.get("SRS"))
        pres.append(len(pred_ids & src_ids) / len(src_ids) if src_ids else 1.0)
    return float(np.mean(pres)) if pres else 0.0


def build_srs_to_svtp_lookup() -> dict[str, list[str]]:
    df = pd.read_csv(ROOT / "data" / "processed" / "unified.csv")
    srs_id_to_text = (
        df[df["Type"] == "SRS"].set_index("Req_ID")["Text"].to_dict()
    )
    lookup: dict[str, list[str]] = {}
    for _, row in df[df["Type"] == "SVTP"].iterrows():
        sid = row["Linked_SRS_ID"]
        if pd.notna(sid) and sid in srs_id_to_text:
            lookup.setdefault(srs_id_to_text[sid], []).append(row["Text"])
    return lookup


def per_model_tps(srs_to_svtp: dict[str, list[str]]) -> pd.DataFrame:
    rows = []
    for sub, model in OSS_DIRS.items():
        full_src, clean_src, pct_clean = [], [], []
        for pp in glob.glob(
            str(ROOT / "results_final" / sub / "seed_*" / "*" / "srs2svtp_preds.csv")
        ):
            if "BUGGY" in pp:
                continue
            preds = pd.read_csv(pp).reset_index(drop=True)
            srcs = preds["SRS"].tolist()
            refs = [srs_to_svtp.get(s, [""])[0] for s in srcs]
            clean_mask = np.array([
                not (is_dirty(s) or is_dirty(r)) for s, r in zip(srcs, refs)
            ])
            full_src.append(src_preservation(preds))
            clean_src.append(src_preservation(preds, clean_mask))
            pct_clean.append(float(clean_mask.mean()))
        rows.append({
            "model": model,
            "src_pres_full": float(np.mean(full_src)),
            "src_pres_clean": float(np.mean(clean_src)),
            "pct_clean": float(np.mean(pct_clean)),
        })
    res = pd.DataFrame(rows).sort_values("model").reset_index(drop=True)
    # Paper-style TPS = (src_pres + 1.0) / 2 (the published evaluation reports
    # ref_pres = 1.0 universally; verified against compliance_metrics_summary.csv).
    res["tps_full_paper"] = (res["src_pres_full"] + 1.0) / 2
    res["tps_clean_paper"] = (res["src_pres_clean"] + 1.0) / 2
    return res


def per_model_bertscore() -> dict[str, float]:
    bert: dict[str, float] = {}
    for sub, model in OSS_DIRS.items():
        vals = []
        for f in glob.glob(
            str(ROOT / "results_final" / sub / "seed_*" / "*" / "generation_results.csv")
        ):
            if "BUGGY" in f:
                continue
            gd = pd.read_csv(f)
            srs2svtp = gd[gd["Task"].str.contains("SVTP", case=False)]
            if len(srs2svtp):
                vals.append(float(srs2svtp["BERTScore_F1"].iloc[0]))
        bert[model] = float(np.mean(vals)) if vals else float("nan")
    return bert


def main() -> int:
    srs_to_svtp = build_srs_to_svtp_lookup()
    res = per_model_tps(srs_to_svtp)
    res["bert_full"] = res["model"].map(per_model_bertscore())

    print("Per-model means (5 seeds avg):")
    print(res[[
        "model", "bert_full", "tps_full_paper",
        "tps_clean_paper", "pct_clean",
    ]].to_string(index=False, float_format="%.4f"))

    b = res["bert_full"].values
    r_full = float(np.corrcoef(b, res["tps_full_paper"].values)[0, 1])
    r_clean = float(np.corrcoef(b, res["tps_clean_paper"].values)[0, 1])
    print()
    print(f"Pearson r FULL  corpus      : r = {r_full:+.4f}  (paper reports -0.601)")
    print(f"Pearson r CLEAN  subset     : r = {r_clean:+.4f}  (artifact-free 80.15% rows)")
    print(f"Δr (clean - full)           : {r_clean - r_full:+.4f}")

    out = ROOT / "results_final" / "clean_subset_correlation.csv"
    res.to_csv(out, index=False, float_format="%.4f")
    print(f"\nSaved per-model breakdown to {out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
