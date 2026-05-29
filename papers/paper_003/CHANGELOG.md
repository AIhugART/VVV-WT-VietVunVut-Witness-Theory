Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# CHANGELOG — Working Paper v3.0
# Nhật ký thay đổi — Bài báo Làm việc v3.0

**Project:** VVV-QMRF (VietVunVut Quantum Measurement Registration Framework)
**Transition:** v2.0 → v3.0
**Date:** 2026-05-28
**Base document:** `papers/Testable_Prediction_Section/extended_wigners_friend_k_side_incommensurability/VVV-QMRF_Working_Paper_v2.0.md`
**New draft:** `papers/paper_003/VVV-QMRF_Working_Paper_v3.0_draft.md`
**Plan:** `papers/paper_003/VVV-QMRF_Working_Paper_v3.0_plan.md`

---

## Summary / Tóm tắt

Working Paper v3.0 is a substantial update of v2.0. The central claim shifts from "K-side incommensurability in EWF" (v2.0 focus) to the full framework stack: K-space architecture (K1–K8 + Layer 2) + K9_E testable hypothesis (Class C qualified) + K9-S12 experimental specification (arXiv submitted 2026-05-27). The φ-map conjecture (Class D) is demoted from potential central claim to supporting material in §11.

**3-Round RCA decision (aggregate 4.6/5 PASS):** Plan approved by `papers/paper_003/VVV-QMRF_Working_Paper_v3.0_plan.md` §1.

---

## Delta Map — 13 Changes (D1–D13)

| ID | Delta | v2.0 state | v3.0 state | Priority |
|---|---|---|---|---|
| **D1** | Project A/B/C separation (one-way motivation, not derivational) | Not explicit | Abstract para 7 + §12.3 | HIGH |
| **D2** | Abstract update: K9_E, Class C qualified, 3 projects, K9-S12 arXiv | 4-paragraph abstract | 8-paragraph abstract | HIGH |
| **D3** | New §4 K-Space Architecture: K1–K8 + Layer 2 (T1–T9, K7_trace, D_enc) | Deferred item v2.0 §7.2 | §4 (~1,300w) | HIGH |
| **D4** | New §5 K9_E Probability Postulate (P9): equation, 8-term provenance, Born limit | Not in v2.0 | §5 (~1,500w) | HIGH |
| **D5** | New §7 Empirical Status: D1 Proietti genuine fit, v30 noise FAIL, K9E-PAT closed | Not in v2.0 | §7 (~900w) | HIGH |
| **D6** | New §8 K9-S12 Modified Bong Protocol: equatorial cancellation, predictions, IBM-Q rejected | Not in v2.0 | §8 (~900w) | HIGH |
| **D7** | Update §6 EWF + §6.7: requires_K_joint = K5 precondition; Bridge_EWF = K5_prospective | v2.0 §4 standalone | §6 carry + §6.7 (~300w new) | MEDIUM |
| **D8** | New §9 BB (2024) + FR (2018) fits: T_BB Class C conditional, V_FR2 PASS, K7_trace 4 consumers | Not in v2.0 | §9 (~900w) | MEDIUM |
| **D9** | New §10 T4-H THEOREM (4/4) + 3-OBS Class C upgrade: δ_M3 dependency chain | T4-H deferred item | §10 (~800w) | MEDIUM |
| **D10** | §11 φ conjecture: Class D SUPPORTING (demoted, conditions φ-1 through φ-7') | v2.0 §6.1 addendum | §11 (~1,000w) | MEDIUM |
| **D11** | Update §12: §12.2 references §11; §12.3 new 3-project independence | v2.0 §6 + §6.1 addendum | §12 carry + §12.3 (~300w new) | MEDIUM |
| **D12** | Update §13: 4 new bullets + resolved items table + K9-S12 falsification explicit | v2.0 §7 | §13 carry + updates | LOW |
| **D13** | AHP audit footprint (Appendix C link to anti_hallucinations/) | Not in v2.0 | Appendix C | LOW |

---

## Structural Comparison

| v2.0 section | v3.0 section | Change |
|---|---|---|
| §1 Registration Layer Gap | §1 | Carry-over + §4 forward-ref |
| §2 K-side Registration Space | §2 | Carry-over + §4 forward-ref |
| §3 Six Conditions | §3 | Carry-over + §4 forward-ref |
| *(not in v2.0)* | **§4 K-Space Architecture** | NEW (~1,300w) |
| *(not in v2.0)* | **§5 K9_E Postulate** | NEW (~1,500w) |
| §4 EWF Incommensurability | §6 EWF Incommensurability | Carry-over + §6.7 new |
| *(not in v2.0)* | **§7 Empirical Status** | NEW (~900w) |
| *(not in v2.0)* | **§8 K9-S12 Protocol** | NEW (~900w) |
| *(not in v2.0)* | **§9 BB + FR fits** | NEW (~900w) |
| *(not in v2.0)* | **§10 T4-H + 3-OBS** | NEW (~800w) |
| §6.1 φ-conditional addendum | §11 φ conjecture (§11, first-class) | Restructured, demoted from central (~1,000w) |
| §6 Positioning | §12 Positioning | Carry-over + §12.3 new |
| §7 Scope/Limitations | §13 Scope/Limitations | Carry-over + 4 new bullets + resolved table |

**Word count:** v2.0 ~12,000w → v3.0 ~14,500w (+~2,500w net, includes replaced/restructured content).

---

## What Did NOT Change

| Item | Reason |
|---|---|
| Title: "When Does a Physical Interaction Become a Valid Registered Measurement?" | User-locked; research question, not claim |
| Six-condition test (Conditions 1–6) | Core contribution of v2.0; unchanged |
| requires_K_joint formal definitions | Class D complete; unchanged |
| ODC_K criterion | Class C conjecture; unchanged |
| §13.4 Architectural constraints (K ≠ H) | Structural; verbatim carry |

---

## Phase Completion Log

| Phase | Sections | Date | mini-RCA |
|---|---|---|---|
| P1 | Skeleton + Abstract (8 para) + §4 | 2026-05-28 | 4.57/5 PASS |
| P2 | §5 K9_E + §7 Empirical Status | 2026-05-28 | 4.6/5 PASS |
| P3 | §8 K9-S12 + §10 T4-H | 2026-05-28 | 4.57/5 PASS |
| P4 | §9 BB+FR + §11 φ-map | 2026-05-28 | 4.6/5 PASS |
| P5 | §6 EWF carry + §12 + §13 | 2026-05-28 | 4.6/5 PASS |
| P6 | Header + abstract finalization | 2026-05-28 | 4.57/5 PASS |
| P7 | CHANGELOG + README + AHP | 2026-05-28 | 4.57/5 PASS |

**Average mini-RCA: 4.58/5.**

---

## Publication Record

| Event | Date | Details |
|---|---|---|
| Draft complete (all phases P1–P7) | 2026-05-28 | `papers/paper_003/VVV-QMRF_Working_Paper_v3.0.md` + PDF 447 KB |
| **Zenodo publish** | **2026-05-28** | **DOI: [10.5281/zenodo.20431310](https://zenodo.org/records/20431310)** — PUBLISHED |
| E-postulate anchoring (post-publish) | 2026-05-29 | E7/E1/E6 §3d/3e/3f K-axiom anchors added (v36); does not affect published PDF |

---

## Superseded Legacy Plan

`papers/Testable_Prediction_Section/.../plan/VVV-QMRF_Working_Paper_v3.0_structure.md` (2026-05-23) — φ-centric plan, outdated relative to index v35. **Superseded** by `papers/paper_003/VVV-QMRF_Working_Paper_v3.0_plan.md`.

---

---

## Zenodo Export — 2026-05-28

| Item | Detail |
|---|---|
| **PDF generated** | `zenodo/VVV-QMRF_Working_Paper_v3.0.pdf` — 447 KB, pdflatex |
| **latex_header.tex** | `zenodo/latex_header.tex` — pdflatex Unicode header (70+ char mappings: Greek, math, subscripts, Sanskrit diacritics) |
| **RCA** | 3 root causes resolved: (1) `unicode-math` XeLaTeX-only → replaced with `inputenc`+`fontenc`; (2) 70+ Unicode chars unmapped → comprehensive `newunicodechar` suite; (3) U+0302 combining circumflex → `\^{}` fallback |
| **Upload target** | Zenodo record `10.5281/zenodo.20289260` → New version v3.0 |
| **DOI (v3.0)** | **`10.5281/zenodo.20431310`** — Published 2026-05-28 |
| **Record URL** | https://zenodo.org/records/20431310 |

*CHANGELOG v1.2 — 2026-05-28. Zenodo v3.0 published. DOI: 10.5281/zenodo.20431310.*
