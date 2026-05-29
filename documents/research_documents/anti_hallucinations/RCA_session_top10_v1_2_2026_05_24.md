Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# RCA Session Report — Top 10 v1.2: [A-E3] Removal

**Date:** 2026-05-24
**Session:** Anti-Hallucination Pipeline — Task 4 (RCA: Why [A-E3] is #1)
**Method:** Full AHP Pipeline (9-file) + 5-Whys RCA x scoring threshold 4/5
**Commit:** `c6e53c6`

---

## Task Summary

RCA dieu tra tai sao [A-E3] (beta universal) dang la #1 trong Top 10 Hallucination Risk Ranking. Ap dung toan bo AHP pipeline (01→06) de truy vet nguyen nhan goc.

## Key Finding

**[A-E3] dang la #1 vi STALE DATA.** RCA A-E3 Final Verdict (commit `897028b`, truoc khi AHP duoc tao) da RECLASSIFY [A-E3] tu "assumption" → "FREE PARAMETER (MEASUREMENT TARGET)". AHP duoc tao SAU verdict nhung khong reflect verdict do — documentation cascade chua den cac file AHP.

## 5-Whys Root Cause

```
W1: [A-E3] #1? -> Risk=22.5
W2: Risk=22.5? -> H=5 x W=3 x (1+0.5) = 22.5
W3: H=5, A=0.5? -> Top 10 phan loai [A-E3] la "assumption"
W4: Chua update? -> AHP tao SAU verdict, doc cascade incomplete
W5: ROOT CAUSE -> STALE DATA + incomplete documentation cascade
```

## Actions Taken

| Action | Detail |
|--------|--------|
| [A-E3] removed khoi Top 10 | Reclassified: FREE PARAMETER. H=5→2, Risk=22.5→6.0 |
| Free Parameter Registry | Them FP-1 (beta) + FP-2 (beta_universal) |
| Top 10 re-rank | phi-map #1, P10-NOISE #2, T5 #3, T4-H #4 |
| New #10 | BE↔QM cross-domain mapping (Risk=9.6) |
| Label update | [A-E3]: [AH-WARN] [RS-CRIT] → [AH-OK] [RS-LOW] [AH-EX] |

## Key Metrics

| Metric | v1.1 | v1.2 | Delta |
|--------|------|------|-------|
| CRITICAL (20+) | 1 ([A-E3]) | **0** | -1 |
| HIGH (15-20) | 4 | 4 | — |
| K9_E assumptions | "1 remaining" | **0** | -1 |
| Free parameters | 0 (unlisted) | **1 (β)** | +1 |

## Files Changed

| File | Change | Lines |
|------|--------|-------|
| `RCA_why_A_E3_is_top1_2026_05_24.md` | **NEW** — Full AHP pipeline analysis + 5-Whys | +270 |
| `00_top_10_hallucinations_record.md` | v1.1→v1.2: [A-E3] removed, re-rank, BE↔QM #10, Free Param Registry | +220 / -170 |
| `label_system.md` | [A-E3] label updated, Top 10 table synced | ~20 |
| `RCA_FINAL_VERDICT_Anti_Hallucination_Pipeline.md` | Section 4 synced | ~5 |
| `index.md` | v1.3→v1.4, version history | ~3 |

## 3-Round RCA Verification

| Round | Focus | Score |
|-------|-------|-------|
| R1 | [A-E3] reclassification — verdict binding? | 5.0/5 |
| R2 | H=2 for FREE PARAMETER — correct? | 4.5/5 |
| R3 | Top 10 stability after removal | 5.0/5 |
| **Aggregate** | | **4.83/5** PASS |

---

*RCA Session Report — Top 10 v1.2: [A-E3] Removal. 2026-05-24. 3-Round RCA: 4.83/5. Commit: c6e53c6.*
