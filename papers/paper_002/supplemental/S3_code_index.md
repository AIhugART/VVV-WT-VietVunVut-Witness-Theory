# Supplemental S3: Reproducible Code Index

All numerical predictions reproducible via `papers/paper_002/supplemental/` scripts.

## Scripts

| Script | Purpose | Paper Section |
|--------|---------|---------------|
| K9S12_proposal.py | Full protocol: angle optimization, correlator table, K9_E predictions | 4-5 |
| statistical_significance.py | FOM scan, Monte Carlo, sigma computations | 6 |
| RCA_full_verification_v93.py | Complete RCA verification of all manuscript v93 claims | All |

## Reproducing key numbers

```bash
cd papers/paper_002/supplemental
python K9S12_proposal.py
# Gen LF 1 = +0.0891 +- 0.0103 (8.6sigma)
# delta<A1B2> = -0.0355 (20.8sigma at beta=0.3)
```

## Requirements

Python 3.9+, numpy, scipy. No external data files needed (parameters inline).

## K9_E deformation model

The manuscript (Eq. 2-3) uses the overlap-dependent form:

  P_K9E(a,b|x,y) = P_QM(a,b|x,y) * (1 - beta * f_perp(b,d)) / Z

where f_perp(b,d) = 1 - |<b|d>|^2 and Z normalizes. This acts at the
probability level, modifying outcome weights by the geometric overlap
between Superobserver outcome b and Friend outcome d.

## Model parameters

N=91,000 (Bong 2020), lambda=810 nm SPDC, mu=0.95 (nominal), mu_threshold=0.86
