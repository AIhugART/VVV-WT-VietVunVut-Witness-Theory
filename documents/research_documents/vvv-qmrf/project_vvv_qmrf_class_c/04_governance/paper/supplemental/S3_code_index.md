# Supplemental S3: Reproducible Code Index

All numerical predictions reproducible via `07_fits/` scripts.

## Scripts

| Script | Purpose | Paper Section |
|--------|---------|---------------|
| K9S12_proposal.py | Full protocol: angle optimization, correlator table, K9_E predictions | 4-5 |
| statistical_significance.py | FOM scan, Monte Carlo, sigma computations | 6 |
| universal_theorem_lf_check.py | Sympy verification of Equatorial Cancellation Theorem | 3 |

## Reproducing key numbers

```bash
cd 07_fits
python K9S12_proposal.py
# Gen LF 1 = +0.0891 +- 0.0103 (8.6sigma)
# delta<A1B2> = -0.0355 (20.8sigma at beta=0.3)
```

## Requirements

Python 3.9+, numpy, scipy. No external data files needed (parameters inline).

## Two K9_E models

- Additive (k9e_predictor.py): E = E_QM*(1 - beta*n_BSM*g_ctx), g_ctx=0.039
- Multiplicative (proietti_raw_fit.py): E = E_QM*(1 - beta*g_eff)^n_BSM, g_eff=0.146
Both predict suppression ratio ~2. See T1B_model_comparison_RCA.md for full analysis.

## Model parameters

N=91,000 (Bong 2020), lambda=810 nm SPDC, mu=0.95 (nominal), mu_threshold=0.86
