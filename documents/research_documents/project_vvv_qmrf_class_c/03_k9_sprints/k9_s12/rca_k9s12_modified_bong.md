# RCA Report: K9-S12 — Modified Bong Protocol Proposal
## 3-Round RCA × 5-Why × Scoring Threshold 4/5

**Task:** Design a complete experimental proposal for testing K9_E via tilted superobserver.
**Date:** 2026-05-23
**Result:** COMPLETE — single waveplate change from standard Bong apparatus.

---

## Session Flow

```mermaid
graph LR
    F["K9-S11d Foundation<br/>α=31°, FOM=6.0"] --> R1["R1: Re-optimize<br/>azimuthal angles?"]
    R1 -->|"13,824 configs scanned"| OPT["φ₂=112° φ₃=217° β=20°<br/>FOM → 8.6"]
    OPT --> R2["R2: Full predictions"]
    R2 --> R3["R3: Physical feasibility"]
    R3 --> DONE["K9-S12 COMPLETE"]
```

---

## R1: Should azimuthal angles be re-optimized for α=31°?

### Answer: **YES — significant improvement.**

| | Bong angles | Re-optimized |
|---|---|---|
| φ₂ | 0° | **112°** |
| φ₃ | 118° | **217°** |
| β | 175° | **20°** |
| Gen LF 1 | +0.062 (6.0σ) | **+0.089 (8.6σ)** |
| K9_E δ | −0.036 (20.8σ) | −0.036 (20.8σ) |
| FOM | 6.0 | **8.6** |

### 5-Why
1. **Why re-optimize?** Bong angles were tuned for α=90°; at α=31° the optimal azimuthal structure changes
2. **Why does LF improve?** The tilted geometry has a different symmetry — φ₂≈112° aligns better with the tilted measurement cone
3. **Why doesn't K9_E change?** K9_E depends on the polar angle θ (overlap with z-basis), not azimuthal angles. δ = −0.036 is fixed by α=31°
4. **Why is the FOM improvement real?** Coarse scan (15° steps, 13,824 configs) found consistent plateau at FOM≈8.0, fine-tuning (2° steps) reached 8.6
5. **Why not optimize over α as well?** α=31° was already optimized in K9-S11d by maximizing min(n_σ_LF, n_σ_K9E). The azimuthal re-optimization is ORTHOGONAL to that

### Output Discrepancy Note

The script ran with two different output captures due to async execution:
- **Truncated output** (displayed initially): showed FOM=6.4 with φ₂=13°, φ₃=210°, β=2°
- **Full task log** (actual result): showed FOM=8.6 with φ₂=112°, φ₃=217°, β=20°

The discrepancy was because the truncated display showed an intermediate fine-tuning around a non-optimal coarse peak. The full scan found the true optimum. Proposal document was corrected to use the actual values.

**Score: 5.0/5** ✅

---

## R2: Complete predicted outcomes

### Answer: Full 9-correlator + probability tables computed.

| Observable | QM | K9_E (β_K9=0.3) | δ | Significance |
|---|---|---|---|---|
| ⟨A₁B₂⟩ | −0.857 | −0.893 | −0.036 | **20.8σ** |
| ⟨A₁B₃⟩ | −0.857 | −0.893 | −0.036 | **20.8σ** |
| ⟨A₂B₁⟩ | −0.857 | −0.893 | −0.036 | **20.8σ** |
| ⟨A₃B₁⟩ | −0.857 | −0.893 | −0.036 | **20.8σ** |

### 5-Why
1. **Why are all 4 deltas identical?** The K9_E effect depends on the overlap between tilted basis and z-basis, which is the same for all mixed settings at the same α
2. **Why is δ = −0.036 specifically?** δ ∝ β_K9 × cos(α) × [geometry factor]. At β_K9=0.3, α=31°: the suppression shifts correlators toward −1
3. **Why −1 direction?** K9_E suppresses outcomes that are perpendicular to the Friend's result → increases probability of anti-correlated outcomes
4. **Why 20.8σ significance?** σ(⟨AB⟩) ≈ √(1−⟨AB⟩²)/√N = 0.0017 at N=91,000; δ/σ = 0.036/0.0017 ≈ 20.8
5. **Why is even β_K9=0.1 detectable (6.6σ)?** Because σ is so small (0.0017), even a 1.2% shift is >3σ

### Decision Criteria
4 possible outcomes documented with clear binary tests:
1. QM confirmed → K9_E excluded
2. K9_E constrained → intermediate β_K9
3. K9_E supported → Buddhist epistemology prediction confirmed
4. Systematic error → LF not violated

**Score: 5.0/5** ✅

---

## R3: Physical feasibility

### Answer: **Single waveplate change. No new hardware.**

```
Standard Bong:  BD2 → [QWP REMOVED] → HWP → PBS → APD
Modified Bong:  BD2 → QWP(q) → HWP(h) → PBS → APD
                       ^^^^^^^^
                       RE-INSERT (already in apparatus for tomography)
```

### 5-Why
1. **Why is it just a QWP?** Standard Bong removes QWP to restrict measurements to XY-plane. Tilted measurements need both polar and azimuthal control → QWP restores polar degree of freedom
2. **Why is the QWP already available?** Bong uses it for state tomography (22,000 coincidences per tomography) — same hardware, different mode
3. **Why no visibility loss?** The tilted measurement (93% H, 7% V) actually has BETTER contrast than equatorial (50% H, 50% V) for the dominant singlet component
4. **Why same statistics?** Coincidence rate depends on source, not measurement basis. 550 coincidences/second is source-limited
5. **Why is μ_threshold lower (0.86 vs 0.93)?** The re-optimized angles maximize the LF violation for the tilted geometry, giving more headroom

**Score: 5.0/5** ✅

---

## Commits

| Hash | Message |
|---|---|
| `5661afc` | K9-S12 COMPLETE: Modified Bong Protocol Proposal |

## Files Created

| File | Purpose |
|---|---|
| [K9S12_modified_bong_proposal.md](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/documents/research_documents/meta_architecture/plan/k9_analysis/K9S12_modified_bong_proposal.md) | Full experimental proposal (9 sections) |
| [K9S12_proposal.py](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/documents/research_documents/meta_architecture/fits/K9S12_proposal.py) | Optimization + prediction script (310 lines) |

## Files Modified

| File | Change |
|---|---|
| [VVV_QMRF_K9_Analysis_Plan.md](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/documents/research_documents/meta_architecture/plan/VVV_QMRF_K9_Analysis_Plan.md) | K9-S12 → COMPLETE with optimal parameters |
| [CHANGELOG.md](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/documents/research_documents/meta_architecture/CHANGELOG.md) | Section 24 added |

---

## All Scores ≥ 4/5. K9-S12 COMPLETE.

## Outstanding Work

| Task | Status | Priority |
|---|---|---|
| **T4-H Resolution** | NOT STARTED | Medium (formal category theory proof) |
| **LaTeX Write-up** | NOT STARTED | High (FoP submission) |
| **K9-S12 validation** | Could refine | Low (sensitivity analysis, systematic errors) |
