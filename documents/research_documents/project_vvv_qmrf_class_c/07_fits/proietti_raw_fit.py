"""
Genuine Non-Circular Fit: K9_E vs Raw Proietti Figure 3 Correlator Data
=======================================================================
3-Round RCA x 5-Why x Scoring Threshold 4/5
VVV-QMRF scope, VVV-QMRF-EX as compass

DATA SOURCE: Proietti et al. 2019, arXiv:1902.05080v2, Figure 3
  Values extracted from Wigner_figure_3.md (this directory's SOT)
  Verified against main.tex L146 (CHSH formula) and L196 (S_exp)

CONTRAST WITH CIRCULAR FIT:
  OLD (d1_blk1_4point_fit.py): E_exp = V_exp * E_QM  [CIRCULAR — tautology]
  NEW (this script):          E_exp = raw Figure 3 values [GENUINE — empirical]

MODEL:
  E_pred(A_x,B_y; V, beta) = V * E_QM(x,y) * (1 - beta*g)^(n_BSM)
  where n_BSM = x + y (number of BSM measurements in setting pair)
  g = 0.146 (effective f_perp per observer, from PP-4 calibration)
  Free parameters: V (visibility), beta (K9_E suppression)
  DOF = N_data - N_params = 4 - 2 = 2
"""

import numpy as np
from scipy.optimize import minimize, minimize_scalar
from scipy import stats

# ============================================================
# SECTION 1: RAW EXPERIMENTAL DATA (Proietti Figure 3)
# ============================================================

# Extracted from Wigner_figure_3.md — verified against main.tex
RAW_DATA = {
    'A0B0': {'E_exp': -0.678, 'sigma': 0.033, 'x': 0, 'y': 0},
    'A0B1': {'E_exp':  0.570, 'sigma': 0.040, 'x': 0, 'y': 1},
    'A1B0': {'E_exp':  0.595, 'sigma': 0.041, 'x': 1, 'y': 0},
    'A1B1': {'E_exp':  0.571, 'sigma': 0.034, 'x': 1, 'y': 1},
}

# Theoretical QM predictions (singlet state, CHSH optimal angles)
E_QM = {
    'A0B0': -1.0 / np.sqrt(2),
    'A0B1': +1.0 / np.sqrt(2),
    'A1B0': +1.0 / np.sqrt(2),
    'A1B1': +1.0 / np.sqrt(2),
}

# CHSH formula from main.tex L146: S = E(A1B1) + E(A1B0) + E(A0B1) - E(A0B0)
CHSH_SIGNS = {'A0B0': -1, 'A0B1': +1, 'A1B0': +1, 'A1B1': +1}

# Verify S from raw data
S_raw = sum(CHSH_SIGNS[k] * RAW_DATA[k]['E_exp'] for k in RAW_DATA)
S_paper = 2.416
print(f"S_raw (from Figure 3) = {S_raw:.4f}")
print(f"S_exp (paper L196)    = {S_paper:.3f}")
print(f"Delta = {abs(S_raw - S_paper):.4f} (rounding error from 3-decimal Figure 3 values)")
print()

# ============================================================
# SECTION 2: K9_E MODEL
# ============================================================

G_EFF = 0.146  # effective f_perp per observer (PP-4 calibration)

def k9e_suppression_factor(n_bsm, beta):
    """K9_E suppression: (1 - beta*g)^(n_BSM) per observer with BSM."""
    return (1.0 - beta * G_EFF) ** n_bsm

def predict_E(key, V, beta):
    """K9_E predicted expectation value for setting key."""
    d = RAW_DATA[key]
    n_bsm = d['x'] + d['y']
    return V * E_QM[key] * k9e_suppression_factor(n_bsm, beta)

def predict_all(V, beta):
    """Return dict of predictions for all settings."""
    return {k: predict_E(k, V, beta) for k in RAW_DATA}

def predict_S(V, beta):
    """Predicted CHSH S value."""
    preds = predict_all(V, beta)
    return sum(CHSH_SIGNS[k] * preds[k] for k in preds)

# ============================================================
# SECTION 3: CHI-SQUARED FIT
# ============================================================

def chi2(params):
    """chi^2 for (V, beta) parameters against raw data."""
    V, beta = params
    total = 0.0
    for key in RAW_DATA:
        d = RAW_DATA[key]
        pred = predict_E(key, V, beta)
        total += (d['E_exp'] - pred)**2 / d['sigma']**2
    return total

# Fit: minimize chi^2 over V in [0.8, 1.0], beta in [0, 0.99]
initial_guess = [0.95, 0.1]
bounds = [(0.8, 1.0), (0.0, 0.99)]
result = minimize(chi2, initial_guess, bounds=bounds, method='L-BFGS-B')

V_fit, beta_fit = result.x
chi2_min = result.fun
dof = 4 - 2  # N_data - N_params
chi2_per_dof = chi2_min / dof
p_value = 1.0 - stats.chi2.cdf(chi2_min, dof)

print("=" * 60)
print("GENUINE FIT RESULTS (Raw Figure 3 Data)")
print("=" * 60)
print(f"  Best-fit V     = {V_fit:.4f}")
print(f"  Best-fit beta  = {beta_fit:.6f}")
print(f"  chi2_min       = {chi2_min:.4f}")
print(f"  chi2/DOF       = {chi2_per_dof:.4f}  (DOF = {dof})")
print(f"  p-value        = {p_value:.4f}")
print()

# ============================================================
# SECTION 4: PREDICTIONS AT BEST-FIT
# ============================================================

preds_best = predict_all(V_fit, beta_fit)
print("--- Per-setting comparison at best-fit ---")
print(f"{'Setting':<8s} {'n_BSM':<6s} {'E_raw':>10s} {'E_pred':>10s} {'Residual':>10s} {'Res/sigma':>10s}")
for key in ['A0B0', 'A0B1', 'A1B0', 'A1B1']:
    d = RAW_DATA[key]
    n_bsm = d['x'] + d['y']
    pred = preds_best[key]
    residual = d['E_exp'] - pred
    res_sigma = residual / d['sigma']
    print(f"  {key:<8s} {n_bsm:<6d} {d['E_exp']:>+10.4f} {pred:>+10.4f} {residual:>+10.4f} {res_sigma:>+10.2f}")

S_pred = predict_S(V_fit, beta_fit)
print(f"\n  S_pred = {S_pred:.4f}  (S_raw = {S_raw:.4f}, S_paper = {S_paper:.3f})")
print()

# ============================================================
# SECTION 5: QM-ONLY COMPARISON (beta=0, V free)
# ============================================================

result_qm = minimize_scalar(lambda v: chi2([v, 0.0]), bounds=(0.8, 1.0), method='bounded')
V_qm = result_qm.x
chi2_qm = result_qm.fun

print("=" * 60)
print("QM-ONLY MODEL (beta=0) vs K9_E MODEL")
print("=" * 60)
print(f"  QM-only:   V = {V_qm:.4f},  chi2 = {chi2_qm:.4f},  chi2/DOF(QM) = {chi2_qm/3:.4f}  (DOF=3)")
print(f"  K9_E:      V = {V_fit:.4f},  beta = {beta_fit:.6f},  chi2 = {chi2_min:.4f},  chi2/DOF = {chi2_per_dof:.4f}  (DOF=2)")

delta_chi2 = chi2_qm - chi2_min
print(f"\n  Delta_chi2 (QM - K9_E) = {delta_chi2:.4f}")
print(f"  Significance = {np.sqrt(max(0, delta_chi2)):.2f} sigma")
print()

# ============================================================
# SECTION 6: BETA CONFIDENCE INTERVALS (from raw data)
# ============================================================
# NOTE: The profile chi^2(beta) is NON-MONOTONIC — it is high at beta=0
# (chi2=6.687), decreases to chi2_min=1.340 at beta=0.598, then increases.
# Beta=0 is excluded at >2sigma (Delta_chi2=5.35). Confidence intervals
# are computed by scanning outward from the minimum in both directions.

print("=" * 60)
print("BETA CONFIDENCE INTERVALS (from raw Figure 3 data)")
print("=" * 60)

def profile_chi2_beta(beta_val):
    """Profile chi^2: minimize over V at fixed beta."""
    res = minimize_scalar(lambda v: chi2([v, beta_val]), bounds=(0.8, 1.0), method='bounded')
    return res.fun

# Scan beta grid for profile chi^2
beta_grid = np.linspace(0, 0.99, 5000)
beta_scan = np.array([profile_chi2_beta(b) for b in beta_grid])

for nsigma, dchi2 in [(1, 1.0), (2, 4.0), (3, 9.0)]:
    chi2_target = chi2_min + dchi2
    inside = beta_grid[beta_scan <= chi2_target]
    if len(inside) > 0:
        beta_low = inside[0]
        beta_high = inside[-1]
        print(f"  {nsigma}sigma CI: beta in [{beta_low:.4f}, {beta_high:.4f}]")
    else:
        print(f"  {nsigma}sigma CI: no beta values within threshold (unconstrained)")

print()

# ============================================================
# SECTION 7: SETTING-DEPENDENT RESIDUAL ANALYSIS
# ============================================================

print("=" * 60)
print("SETTING-DEPENDENT RESIDUAL ANALYSIS (K9_E Signature Test)")
print("=" * 60)

print("\nQM with uniform visibility predicts: ALL residuals ~ 0")
print("K9_E with beta > 0 predicts: BSM settings have LARGER negative residuals")
print()

print("--- QM-only residuals (beta=0, V fitted) ---")
preds_qm = predict_all(V_qm, 0.0)
for key in ['A0B0', 'A0B1', 'A1B0', 'A1B1']:
    d = RAW_DATA[key]
    n_bsm = d['x'] + d['y']
    res = d['E_exp'] - preds_qm[key]
    print(f"  {key} ({n_bsm} BSM): res = {res:+.4f} ({res/d['sigma']:+.2f}sigma)")

print("\n--- K9_E residuals (beta and V fitted) ---")
for key in ['A0B0', 'A0B1', 'A1B0', 'A1B1']:
    d = RAW_DATA[key]
    n_bsm = d['x'] + d['y']
    res = d['E_exp'] - preds_best[key]
    print(f"  {key} ({n_bsm} BSM): res = {res:+.4f} ({res/d['sigma']:+.2f}sigma)")

print("\n--- K9_E PATTERN CHECK ---")
print("K9_E predicts: residual(2 BSM) approx 2 * residual(1 BSM) in negative direction")
res_0bsm = RAW_DATA['A0B0']['E_exp'] - preds_best['A0B0']
res_1bsm_avg = ((RAW_DATA['A0B1']['E_exp'] - preds_best['A0B1']) +
                (RAW_DATA['A1B0']['E_exp'] - preds_best['A1B0'])) / 2
res_2bsm = RAW_DATA['A1B1']['E_exp'] - preds_best['A1B1']
print(f"  Residual 0 BSM: {res_0bsm:+.4f}")
print(f"  Residual 1 BSM (avg): {res_1bsm_avg:+.4f}")
print(f"  Residual 2 BSM: {res_2bsm:+.4f}")
if abs(res_1bsm_avg) > 1e-10:
    print(f"  Ratio 2BSM/1BSM: {res_2bsm/res_1bsm_avg:.3f}")
else:
    print(f"  Ratio 2BSM/1BSM: N/A (1 BSM residual ~ 0)")
print()

# ============================================================
# SECTION 8: COMPARISON WITH CIRCULAR FIT
# ============================================================

print("=" * 60)
print("COMPARISON: GENUINE FIT vs CIRCULAR FIT")
print("=" * 60)

V_circular = 2.416 / (2 * np.sqrt(2))
print(f"\n  Circular fit:  V = {V_circular:.4f} (from S_exp/S_QM), beta = 0.000 (forced)")
print(f"                   Used E_exp = V * E_QM = +/-{V_circular * 1/np.sqrt(2):.4f} for all settings")
print(f"  Genuine fit:   V = {V_fit:.4f} (fitted), beta = {beta_fit:.6f} (fitted)")
print(f"                   Used E_exp = raw Figure 3 values")
print()

# ============================================================
# SECTION 9: SENSITIVITY SCAN
# ============================================================

print("=" * 60)
print("SENSITIVITY: Minimum Detectable beta")
print("=" * 60)

for beta_test in [0.0, 0.05, 0.10, 0.20, 0.30, 0.50]:
    chi2_test = profile_chi2_beta(beta_test)
    dchi2_test = chi2_test - chi2_min
    sigma_test = np.sqrt(max(0, dchi2_test))
    print(f"  beta = {beta_test:.2f}: Delta_chi2 = {dchi2_test:.4f}, significance = {sigma_test:.2f}sigma")
print()

# ============================================================
# SECTION 10: SUMMARY
# ============================================================

print("=" * 60)
print("GENUINE FIT SUMMARY")
print("=" * 60)
print(f"""
  DATA: 4 raw correlator values from Proietti Figure 3
        Extracted from Wigner_figure_3.md (SOT verified against main.tex)
        S_raw = {S_raw:.4f} approx S_paper = {S_paper:.3f} (confirmed)

  MODEL: K9_E with visibility: E_pred = V * E_QM * (1 - beta*{G_EFF})^(n_BSM)
        Free parameters: V (visibility), beta (K9_E suppression)
        DOF = 2

  RESULTS:
        Best-fit beta = {beta_fit:.6f}
        Best-fit V    = {V_fit:.4f}
        chi2/DOF      = {chi2_per_dof:.4f}
        p-value       = {p_value:.4f}

  COMPARISON:
        QM-only (beta=0):  chi2 = {chi2_qm:.4f} (DOF=3)
        K9_E (beta free):  chi2 = {chi2_min:.4f} (DOF=2)
        Delta_chi2        = {delta_chi2:.4f} ({np.sqrt(max(0,delta_chi2)):.2f}sigma)

  VERDICT: {'K9_E does NOT significantly improve over QM at current precision' if delta_chi2 < 1 else 'K9_E marginally improves over QM' if delta_chi2 < 4 else 'K9_E shows evidence of suppression'}
""")
