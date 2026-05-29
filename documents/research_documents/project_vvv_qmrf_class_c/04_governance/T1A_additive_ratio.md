Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# Track 1A — Additive Model 2BSM/1BSM Ratio

**Date:** 2026-05-24
**Plan:** Post-v30 Execution Plan, Track 1

## Computed Values

| Setting | n_BSM | E_QM | E_K9E_add (beta=0.598) | delta |
|---------|-------|------|------------------------|-------|
| A0B0 | 0 | -0.7071 | -0.7071 | 0.0000 |
| A0B1 | 1 | +0.7071 | +0.6907 | -0.0164 |
| A1B0 | 1 | +0.7071 | +0.6907 | -0.0164 |
| A1B1 | 2 | +0.7071 | +0.6742 | -0.0329 |

## Ratio

- delta_1BSM (avg A0B1 + A1B0) = -0.016445
- delta_2BSM (A1B1) = -0.032889
- **ratio_additive = 2.000**

Ly do: additive model la tuyen tinh theo n_BSM: delta = -beta * n_BSM * g_ctx * E_QM.
Tai Proietti geometry, E_QM co cung magnitude cho tat ca BSM settings (~0.7071),
nen ratio = 2*g_ctx / 1*g_ctx = 2.000 chinh xac.

## Model Characteristics

- Suppression per BSM: delta/n_BSM = -0.0164 tai beta=0.598
- Nho hon multiplicative model ~3.5x (multiplicative: -0.0580 per BSM)
- Su dung g_ctx = 0.03889 (calibrated tu delta_S(beta=0.5) = -0.055)
