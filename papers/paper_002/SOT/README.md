Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# paper_002 SOT (Source of Truth) Directory

**Purpose:** Internal reference -- K9_E completeness and provenance for Paper 002.
**Created:** 2026-05-25
**Audience:** Internal (VietVunVut + collaborators). NOT for publication.

---

## File Inventory

| File | Type | Purpose |
|------|------|---------|
| `paper_002_SOT.md` | Synthesis | **PRIMARY SOT** -- synthesizes best content from all versions (v4-v21). Full K9_E context, VVV-QMRF language, corrected numbers (v12+), academic depth (v17-v21). Use this when revising the paper. |
| `draft_v1.md` | Provenance document | **HISTORICAL ORIGIN** -- K9-S12 proposal draft v4 (2026-05-24). Contains the original experimental design, angle optimization, and K9_E postulate as first formulated. NUMBERS ARE PRE-FIX (v12 corrected Eq.(12) thresholds). Use this only for tracing the origin of concepts. |
| `README.md` | Index | This file. |

---

## Relationship Between Files

```
draft_v1.md (v4)                   manuscript.md (v21)
  K9-S12 proposal                      Public-facing academic paper
  K9_E = central identity              K9_E = sanitized to Eq.2-3
  Numbers: analytical (BUG)            Numbers: corrected (v12+)
       \                                    /
        \                                  /
         \                                /
          paper_002_SOT.md (synthesis)
            K9_E = central identity
            Numbers = corrected (v12+)
            Academic depth = v17-v21
            VVV-QMRF language = preserved
```

---

## When to Use Which File

| If you want to... | Read... |
|-------------------|---------|
| Understand K9_E completely (postulate, architecture, predictions, history) | `paper_002_SOT.md` |
| Trace the original K9-S12 experimental design | `draft_v1.md` |
| Write/revise the public-facing paper | `manuscript.md` (v21) + `paper_002_SOT.md` for K9_E context |
| Check K9_E numbers (beta thresholds, deltas, FOM) | `paper_002_SOT.md` Section 16 |
| Understand what changed across versions | `paper_002_SOT.md` Section 14 + `../CHANGELOG.md` |
| Map SOT content to manuscript sections | `paper_002_SOT.md` Section 15 |
| Reproduce numerical predictions | `../supplemental/K9S12_proposal.py` |
| Verify novelty claim | `../supplemental/S1_search_audit.md` |

---

## Key Warnings

1. **draft_v1.md has WRONG numbers.** The analytical |cos theta|/2 approximation was corrected in v12. Always use `paper_002_SOT.md` or `manuscript.md` v21 for numerical values.
2. **paper_002_SOT.md uses VVV-QMRF language.** This is intentional -- the SOT preserves framework context removed from the public manuscript. Do NOT copy VVV-QMRF sections directly into the manuscript without translation.
3. **SOT is internal only.** Do not include this directory in arXiv submission or share with external reviewers.

---

*Created 2026-05-25. Update when new synthesis versions are added.*
