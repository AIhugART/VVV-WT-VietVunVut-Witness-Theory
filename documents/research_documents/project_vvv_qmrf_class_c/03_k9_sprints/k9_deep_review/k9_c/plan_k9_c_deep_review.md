Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# Plan — K9_C Deep Review (Provenance + 4-Layer RCA)

**Target candidate:** K9_C — Registration Latency Weighting (FAIL-FIXABLE)
**Phase:** P3 (executes this plan)
**Method:** AHP-driven component provenance audit + 4-layer Root Cause Analysis
**Parent program:** [K9 Deep Review Master Index](../index.md)
**Pre-existing sources:** [K9S2_candidate_C.md](../../k9_analysis/K9S2_candidate_C.md), [VVV_QMRF_K9_Analysis_Plan.md](../../VVV_QMRF_K9_Analysis_Plan.md)
**Status:** EXECUTED ✅ (2026-05-27). K9_C FAIL-FIXABLE confirmed. 12 components, mean H=5.0, Cluster C-C1 (No-τ_reg), 2 orphans [AH-DEFER] (C-09, C-11), PS-1 (K2 kṣaṇabhaṅga boundary). See deliverables in §8.

---

## §1. Objective

Run a **provenance audit** on K9_C components **AND** a **4-layer RCA** focused on the outcome-dependence circularity. K9_C's core issue: τ_reg(o) (registration latency for outcome o) appears in probability formula but requires knowing outcome o—a circular definition. This audit will:
- Inventory K9_C's ~10–12 components
- Classify τ_reg as outcome-dependent or outcome-independent
- Identify the logical circularity (Layer 0 RCA)
- Propose resolution: (A) τ_reg outcome-independent (cancels, FAIL) or (B) τ_reg outcome-dependent (requires K-state extension)
- Determine whether K9_C can be fixed within frozen K1-K8

---

## §2. K9_C Definition (Reference)

```
K9_C — Registration Latency Weighting:

  P(o|k,H) = Tr(E_o ρ) · g(τ_reg(o)) / Z_C

  g(τ_reg) = exp(−τ_reg / τ_0)
  τ_0 ∈ (0,∞) = characteristic registration time [free parameter]
  Z_C = Σ_o Tr(E_o ρ) · g(τ_reg(o))  [normalization]
  τ_reg(o) = registration latency for outcome o under Hamiltonian H

  K-side interpretation: outcomes registering faster (kṣaṇabhaṅga —
  momentariness) get higher probability weight.

CRITICAL AMBIGUITY:
  τ_reg(o) DEPENDS ON OUTCOME o.
  But probability formula assigns P TO outcome o before it's known.
  Circular: how evaluate τ_reg(o) before o is known?

POSSIBLE RESOLUTIONS:
  (A) Outcome-Independent: τ_reg = system-level constant
      → Cancels in normalization (like K9_B) → FAIL
  (B) Outcome-Dependent (Requires Extension):
      → τ_reg(o) pre-computed as latency each outcome WOULD have
      → Requires K-state field not currently axiomatized
```

---

## §3. Methodology — 5 Phases

**Phase 0:** Layer 0 RCA — The Temporal Latency Circularity.
**Phase 1–3:** Inventory τ_reg, g(), Z_C, τ_0, interpretations.
**Phase 4:** Layer 1–3 RCA (per-component 5-Whys, resolution paths cluster).
**Phase 5:** Verdict — Can K9_C be fixed within frozen K1-K8?

---

## §4. Expected Component Inventory (~10–12 items)

| ID | Component | Type | Expected H-Score |
|----|-----------|------|------------------|
| C-01 | P(o\|k,H) formula | Operation | BLUE (3–4) |
| C-02 | τ_reg(o) outcome-dependent? | Assumption | YELLOW (5–6) |
| C-03 | g(τ_reg) = exp(−τ_reg / τ_0) | Symbol | BLUE (3–4) |
| C-04 | τ_0 free parameter | Symbol | GREEN (0–2) |
| C-05 | Z_C normalization | Operation | BLUE (3–4) |
| C-06 | kṣaṇabhaṅga interpretation | Term (BE) | YELLOW (5–6) |
| C-07 | arthakriyā mapping | Term (BE) | YELLOW (5–6) |
| C-08 | τ_reg depends on Hamiltonian H | Assumption | YELLOW (5–6) |
| C-09 | Circularity: τ_reg requires knowing o | Logical issue | ORANGE (7–8) |
| C-10 | Resolution (A): outcome-independent τ_reg | Assumption | YELLOW (5–6) |
| C-11 | Resolution (B): outcome-dependent τ_reg | Layer 2 proposal | ORANGE (7–8) |
| C-12 | Extend K-state with τ_reg vector? | Frozen K1-K8 question | ORANGE (7–8) |

---

## §5. Expected Metrics (Post-Execution)

- **Total components:** ~12
- **Mean H-score:** ~4.5 (mixed BLUE/YELLOW/ORANGE)
- **Orphans:** 1–2 (τ_reg circularity, Resolution B K-state field)
- **Primary RCA:** Layer 0 (circularity) + Layer 2 (resolution paths)
- **Actions:** 2–3 (AC-C1 outcome-independent => FAIL, AC-C2 resolution B proposal)

---

## §6. Sources to Read (Before Execution)

1. **K9S2_candidate_C.md** (PRIORITY 1) — Full circularity analysis
2. **K_Space_Axiomatization.md §K2** — Temporal order definition
3. **SYSTEM_Buddhist_Epistemology/system_be_full.md** — kṣaṇabhaṅga, arthakriyā
4. **PP2_K9B_locked.md** — Compare outcome-independence proof for K9_B

---

## §7. Pre-Execution Checklist

- [x] K9_A, K9_B audits complete
- [x] K9S2_candidate_C.md read
- [x] Circularity understood
- [x] Component inventory drafted
- [x] Estimated 4–5 hours

---

## §8. Expected Deliverables

**report_k9_c_traceability_matrix.md:**
- 12-row component matrix
- Outcome-dependence classification columns
- Resolution path options (A vs B)
- Mean H ≈ 4.5

**rca_k9_c_chains.md:**
- Layer 0 RCA: Temporal Latency Circularity (5-Why chain)
- Layer 1: Per-component chains (τ_reg, g(), τ_0, interpretation)
- Layer 2: Resolution Paths cluster
- Layer 3: Post-v31 verdict confirmation

---

## §9. Change Log

| Date | Version | Notes |
|------|---------|-------|
| 2026-05-27 | v0.1 | Initial plan for P3 K9_C audit. Circularity diagnosis + resolution paths. |
| 2026-05-27 | v1.0 | P3 executed. FAIL-FIXABLE confirmed. 12 components (C-01…C-12), mean H=5.0. Cluster C-C1 (No-τ_reg, 5 components). 2 orphans [AH-DEFER] (C-09, C-11). PS-1 (K2 boundary). |

*Plan K9_C Deep Review v1.0 (2026-05-27). P3 EXECUTED — FAIL-FIXABLE confirmed. Deliverables: report_k9_c_traceability_matrix.md + rca_k9_c_chains.md.*
