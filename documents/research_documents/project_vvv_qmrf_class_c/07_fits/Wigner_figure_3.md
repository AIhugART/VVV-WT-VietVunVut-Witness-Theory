# Proietti et al. 2019 — Figure 3 Raw Correlator Data (SOT)

**Source:** Proietti, M. et al. "Experimental test of local observer-independence."
Science Advances 5, eaaw9832 (2019). arXiv:1902.05080v2.

**Data location:** Figure 3 (all four panels: A0B0, A0B1, A1B0, A1B1).

**Extraction method:** Visual reading from Figure 3 bar charts (3 decimal places).

**Verification:** S_raw = sum(CHSH_signs × E_raw) = 2.414 ≈ 2.416 (paper L196).
Delta = 0.002 from rounding at 3 decimal places — consistent with extraction precision.

---

## Raw Correlator Values

| Setting | E_exp   | sigma | x (Alice) | y (Bob)  | n_BSM | CHSH sign |
|---------|---------|-------|-----------|----------|-------|-----------|
| A0B0    | -0.678  | 0.033 | 0 (proj)  | 0 (proj) | 0     | -1        |
| A0B1    | +0.570  | 0.040 | 0 (proj)  | 1 (BSM)  | 1     | +1        |
| A1B0    | +0.595  | 0.041 | 1 (BSM)   | 0 (proj) | 1     | +1        |
| A1B1    | +0.571  | 0.034 | 1 (BSM)   | 1 (BSM)  | 2     | +1        |

### Setting Key

- **x=0 (projective):** Alice/Bob measures Friend's lab in the computational basis.
  No BSM performed → no K-space incommensurability (bot_K does not fire).
- **x=1 (BSM):** Alice/Bob performs Bell-State Measurement on Friend's lab.
  BSM creates K-space incommensurability with Friend's prior projective measurement.

---

## Derived Quantities

| Quantity | Value          | Formula / Source                                    |
|----------|----------------|-----------------------------------------------------|
| S_raw    | 2.414          | -E(A0B0) + E(A0B1) + E(A1B0) + E(A1B1)            |
| S_paper  | 2.416 ± 0.075  | main.tex L196                                       |
| S_QM     | 2.828          | 2√2 (Tsirelson bound)                               |
| Delta    | 0.002          | |S_raw - S_paper| — rounding from 3-decimal Figure 3 |
| N_total  | 1794           | Total coincidences, main.tex L195                   |

---

## Error Bar Source

Error bars estimated from Poissonian statistics on coincidence counts:
- N_total = 1794 coincidences (main.tex L195)
- Per-setting events ≈ N_total / 4 ≈ 449
- sigma_E ≈ 1/√(N_per_setting) per setting pair
- Actual sigma values read from Figure 3 error bars

The sigma values are NOT uniform across settings — this reflects the
asymmetric event distribution inherent to BSM vs projective measurements.

---

## Contrast with Reconstructed Data (CIRCULAR — superseded)

The reconstructed data used in `d1_blk1_4point_fit.py` assumed uniform visibility:

    E_reconstructed = V_exp × E_QM = (S_exp / S_QM) × E_QM

| Setting | E_reconstructed | E_raw  | Delta   | Note                    |
|---------|----------------|--------|---------|-------------------------|
| A0B0    | -0.604         | -0.678 | -0.074  | Raw MORE negative       |
| A0B1    | +0.604         | +0.570 | -0.034  | Raw LESS positive       |
| A1B0    | +0.604         | +0.595 | -0.009  | Nearly identical        |
| A1B1    | +0.604         | +0.571 | -0.033  | Raw LESS positive       |

**Key observation:** The raw data is significantly NON-UNIFORM — visibility
differs per setting. The 0-BSM setting (A0B0) has the largest deviation from
QM prediction, while the 1-BSM setting (A1B0) is closest. This non-uniformity
is why the genuine fit (proietti_raw_fit.py) yields beta=0.598 (not 0).

> **CAUTION:** The non-uniform pattern does NOT confirm K9_E multiplicative
> suppression. The pattern check (2BSM/1BSM residual ratio = -0.78, expected ~2)
> shows the K9_E-specific signature is NOT present. Non-uniform experimental
> noise remains a viable alternative explanation.

---

## Citation

```
Proietti, M., Pickston, A., Graffitti, F., Barrow, P., Kundys, D.,
Branciard, C., Ringbauer, M., & Fedrizzi, A. (2019).
Experimental test of local observer-independence.
Science Advances, 5(9), eaaw9832.
arXiv:1902.05080v2
```

---

*SOT document for `07_fits/proietti_raw_fit.py`. Created 2026-05-23.*
