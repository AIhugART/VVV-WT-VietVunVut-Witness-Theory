# Paper QC Checklist -- K9-S12 Single-Waveplate Test

**Date:** 2026-05-24 | **Paper:** draft_v1.md (v3) | **QC:** 15/15 PASS

## Quality Gates

| # | Criterion | Status | Notes |
|---|-----------|--------|-------|
| 1 | Every symbol defined at first use | PASS | K9_E, f_perp, beta, Gen LF 1: Sections 2-3 |
| 2 | Every number has uncertainty | PASS | All correlators: sigma column. Gen LF 1: +-0.0103 |
| 3 | Every figure has self-contained caption | PASS | Figs 3-5: captions + embedded images |
| 4 | All 5 loopholes (Section 8) | PASS | Locality, Detection, Freedom, Superobserver, K9_E scope |
| 5 | Decision criteria: 4 outcomes (Section 5.5) | PASS | Joint/LF-only/calibration/null |
| 6 | Code runnable by third party | PASS | K9S12_proposal.py self-contained |
| 7 | Abstract: no undefined acronyms | PASS | EWF, LF, QWP expanded |
| 8 | References complete + consistent | PASS | 11 refs, consistent format |
| 9 | FOM consistent across Sections 5-7 | PASS | FOM=8.6 throughout |
| 10 | Section 7.5: actual values, not placeholders | PASS | mu>=0.86, eta>=0.91, dtheta<=+-5 deg |

## Content Gates

| # | Criterion | Status | Notes |
|---|-----------|--------|-------|
| 11 | v31 status accurate | PASS | Section 2.3: qualified, P10-NOISE, K9E-PAT |
| 12 | "First test" framing | PASS | Sections 1, 9.4, 10 |
| 13 | Theorem proof complete | PASS | Section 3.2 |
| 14 | K9_E model clearly defined | PASS | Section 2.3: P9, f_perp, beta |
| 15 | No overclaim about empirical status | PASS | "empirically UNCONFIRMED" |

## Remaining

| Item | Priority | Notes |
|------|----------|-------|
| Fig 1 (EWF schematic) | MEDIUM | TikZ/Inkscape |
| Fig 2 (Optical path) | MEDIUM | TikZ/Inkscape |
| Supplemental S1-S6 | LOW | Content mostly in main text |
| LaTeX conversion | MEDIUM | arXiv format |

**Verdict: 15/15 PASS. Ready for Figs 1-2 + LaTeX + arXiv.**
