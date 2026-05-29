"""
Noise Sensitivity Analysis — P10-NOISE Resolution
==================================================
3-Round RCA x 5-Why x Scoring Threshold 4/5
VVV-QMRF scope, VVV-QMRF-EX as compass

Implements: noise_sensitivity_analysis_spec.md (2026-05-24)
Methodology: RCA_P10_NOISE_methodology_decision_2026_05_24.md (aggregate 4.77/5)

Answer: "How large must non-uniform noise be to produce Delta_chi2 = 5.35?"

B1: Delta_chi2 decomposition per setting
B2: Single-setting perturbation — fragility of each setting
B3: Worst-case noise pattern — random search
B4: Multi-setting noise threshold — Monte Carlo + g_eff sensitivity
"""
import numpy as np
from scipy.optimize import minimize_scalar

np.random.seed(42)

# ============================================================
# SECTION 0: RAW DATA (Proietti Figure 3, via Wigner_figure_3.md)
# ============================================================
SETTINGS = ['A0B0', 'A0B1', 'A1B0', 'A1B1']

RAW_DATA = {
    'A0B0': {'E_exp': -0.678, 'sigma': 0.033, 'x': 0, 'y': 0},
    'A0B1': {'E_exp':  0.570, 'sigma': 0.040, 'x': 0, 'y': 1},
    'A1B0': {'E_exp':  0.595, 'sigma': 0.041, 'x': 1, 'y': 0},
    'A1B1': {'E_exp':  0.571, 'sigma': 0.034, 'x': 1, 'y': 1},
}

E_QM_VAL = 1.0 / np.sqrt(2)
E_QM = {
    'A0B0': -E_QM_VAL,
    'A0B1': +E_QM_VAL,
    'A1B0': +E_QM_VAL,
    'A1B1': +E_QM_VAL,
}

G_EFF_NOMINAL = 0.146
V_FIT = 0.939
BETA_FIT = 0.598
CHI2_K9E = 1.340
CHI2_QM = 6.687
DELTA_CHI2_TARGET = 5.347
SIGMA_TARGET = np.sqrt(DELTA_CHI2_TARGET)


# ============================================================
# SECTION 1: MODEL FUNCTIONS (closed-form V_opt for speed)
# ============================================================

def v_opt_closed_form(data_dict, beta, g_eff=G_EFF_NOMINAL):
    """Closed-form optimal V for given beta.

    V_opt = sum(a_i * E_exp_i / sigma_i^2) / sum(a_i^2 / sigma_i^2)
    where a_i = E_QM_i * (1 - beta*g)^n_i
    """
    num = 0.0
    den = 0.0
    for key in SETTINGS:
        d = data_dict[key]
        n_bsm = d['x'] + d['y']
        a_i = E_QM[key] * (1.0 - beta * g_eff) ** n_bsm
        w = 1.0 / d['sigma'] ** 2
        num += a_i * d['E_exp'] * w
        den += a_i * a_i * w
    return num / den if den > 1e-15 else 0.9


def compute_chi2(data_dict, V, beta, g_eff=G_EFF_NOMINAL):
    """Full chi^2 for given V, beta."""
    total = 0.0
    for key in SETTINGS:
        d = data_dict[key]
        n_bsm = d['x'] + d['y']
        pred = V * E_QM[key] * (1.0 - beta * g_eff) ** n_bsm
        total += (d['E_exp'] - pred) ** 2 / d['sigma'] ** 2
    return total


def profile_chi2(data_dict, beta, g_eff=G_EFF_NOMINAL):
    """min_V chi2(V, beta) using closed-form V_opt."""
    V_opt = v_opt_closed_form(data_dict, beta, g_eff)
    return compute_chi2(data_dict, V_opt, beta, g_eff)


def fit_qm_only(data_dict):
    """Fit QM-only: beta=0, optimize V via closed form."""
    V_qm = v_opt_closed_form(data_dict, 0.0)
    chi2_qm = compute_chi2(data_dict, V_qm, 0.0)
    return V_qm, chi2_qm


def fit_k9e_full(data_dict, g_eff=G_EFF_NOMINAL):
    """Fit K9_E: optimize V (closed form) and beta (1D minimization)."""
    res = minimize_scalar(
        lambda b: profile_chi2(data_dict, b, g_eff),
        bounds=(0.0, 0.99),
        method='bounded',
    )
    beta_opt = res.x
    V_opt = v_opt_closed_form(data_dict, beta_opt, g_eff)
    chi2_opt = res.fun
    return V_opt, beta_opt, chi2_opt


def delta_chi2_compute(data_dict, g_eff=G_EFF_NOMINAL):
    """Compute Delta_chi2 for a dataset."""
    _, chi2_qm = fit_qm_only(data_dict)
    _, _, chi2_k9e = fit_k9e_full(data_dict, g_eff)
    return chi2_qm - chi2_k9e, chi2_qm, chi2_k9e


# ============================================================
# SECTION 2: VERIFY BASELINE
# ============================================================

print("=" * 65)
print("BASELINE VERIFICATION (genuine fit reproduction)")
print("=" * 65)

V_qm_base, chi2_qm_base = fit_qm_only(RAW_DATA)
V_k9e_base, beta_k9e_base, chi2_k9e_base = fit_k9e_full(RAW_DATA)
delta_chi2_base = chi2_qm_base - chi2_k9e_base

print(f"  QM-only:      V = {V_qm_base:.4f},  chi2 = {chi2_qm_base:.4f}")
print(f"  K9_E:         V = {V_k9e_base:.4f},  beta = {beta_k9e_base:.6f},  chi2 = {chi2_k9e_base:.4f}")
print(f"  Delta_chi2  = {delta_chi2_base:.4f}")
print(f"  Significance = {np.sqrt(max(0, delta_chi2_base)):.2f} sigma")
print(f"  Expected:      V=0.939, beta=0.598, chi2_qm=6.687, chi2_k9e=1.340")
print(f"  Match:         {'OK' if abs(V_k9e_base - V_FIT) < 0.01 and abs(beta_k9e_base - BETA_FIT) < 0.01 else 'CHECK - minor diff from closed-form vs L-BFGS-B'}")
print()

# ============================================================
# SECTION 3: B1 - DELTA_CHI2 DECOMPOSITION
# ============================================================

print("=" * 65)
print("B1: DELTA_CHI2 DECOMPOSITION")
print("=" * 65)
print("Which setting(s) drive the K9_E advantage over QM?")
print()

print(f"{'Setting':<8s} {'n_BSM':<6s} {'chi2_QM':>10s} {'chi2_K9E':>10s} {'delta_chi2':>10s} {'%':>8s}")
print("-" * 58)

b1_deltas = {}
total_delta = 0.0
for key in SETTINGS:
    d = RAW_DATA[key]
    n_bsm = d['x'] + d['y']
    chi2_qm_i = (d['E_exp'] - V_qm_base * E_QM[key]) ** 2 / d['sigma'] ** 2
    pred_k9e = V_k9e_base * E_QM[key] * (1.0 - beta_k9e_base * G_EFF_NOMINAL) ** n_bsm
    chi2_k9e_i = (d['E_exp'] - pred_k9e) ** 2 / d['sigma'] ** 2
    delta_i = chi2_qm_i - chi2_k9e_i
    b1_deltas[key] = {'chi2_qm': chi2_qm_i, 'chi2_k9e': chi2_k9e_i, 'delta': delta_i}
    total_delta += delta_i

for key in SETTINGS:
    d = b1_deltas[key]
    pct = 100.0 * d['delta'] / total_delta if abs(total_delta) > 1e-10 else 0.0
    print(f"  {key:<8s} {RAW_DATA[key]['x']+RAW_DATA[key]['y']:<6d} {d['chi2_qm']:>10.4f} {d['chi2_k9e']:>10.4f} {d['delta']:>+10.4f} {pct:>7.1f}%")
print(f"  {'Total':<14s} {chi2_qm_base:>10.4f} {chi2_k9e_base:>10.4f} {total_delta:>+10.4f} {'100.0%':>8s}")
print()

max_key = max(b1_deltas, key=lambda k: abs(b1_deltas[k]['delta']))
print(f"  >> Setting {max_key} contributes the MOST to K9_E advantage")
print(f"     ({b1_deltas[max_key]['delta']:+.4f} out of {total_delta:.4f} total, {100*abs(b1_deltas[max_key]['delta'])/abs(total_delta):.0f}%)")
print()

# ============================================================
# SECTION 4: B2 - SINGLE-SETTING PERTURBATION
# ============================================================

print("=" * 65)
print("B2: SINGLE-SETTING PERTURBATION ANALYSIS")
print("=" * 65)
print("How many sigma must each setting shift to eliminate K9_E advantage?")
print("(Delta_chi2 < 1.0 = no significant K9_E advantage)")
print()

print(f"{'Setting':<8s} {'delta_threshold':>18s} {'direction':>12s}")
print("-" * 42)

b2_thresholds = {}
for key in SETTINGS:
    sigma_i = RAW_DATA[key]['sigma']
    threshold_pos = None
    threshold_neg = None

    # Scan positive direction
    for delta in np.arange(0.0, 8.0, 0.05):
        data_pert = {k: dict(RAW_DATA[k]) for k in SETTINGS}
        data_pert[key] = dict(RAW_DATA[key])
        data_pert[key]['E_exp'] = RAW_DATA[key]['E_exp'] + delta * sigma_i
        dc, _, _ = delta_chi2_compute(data_pert)
        if dc < 1.0:
            threshold_pos = delta
            break

    # Scan negative direction
    for delta in np.arange(0.0, -8.0, -0.05):
        data_pert = {k: dict(RAW_DATA[k]) for k in SETTINGS}
        data_pert[key] = dict(RAW_DATA[key])
        data_pert[key]['E_exp'] = RAW_DATA[key]['E_exp'] + delta * sigma_i
        dc, _, _ = delta_chi2_compute(data_pert)
        if dc < 1.0:
            threshold_neg = abs(delta)
            break

    if threshold_pos is not None and threshold_neg is not None:
        min_thresh = min(threshold_pos, threshold_neg)
        direction = "+sigma" if min_thresh == threshold_pos else "-sigma"
    elif threshold_pos is not None:
        min_thresh = threshold_pos
        direction = "+sigma"
    elif threshold_neg is not None:
        min_thresh = threshold_neg
        direction = "-sigma"
    else:
        min_thresh = float('inf')
        direction = "N/A"

    b2_thresholds[key] = min_thresh
    print(f"  {key:<8s} {min_thresh:>14.2f} sigma  {direction:>12s}")

min_key = min(b2_thresholds, key=lambda k: b2_thresholds[k])
print()
print(f"  >> Most fragile setting: {min_key} ({b2_thresholds[min_key]:.2f} sigma)")
print(f"     Only {b2_thresholds[min_key]:.1f} sigma shift at {min_key} eliminates K9_E advantage.")
print()

# ============================================================
# SECTION 5: B3 - WORST-CASE NOISE PATTERN
# ============================================================

print("=" * 65)
print("B3: WORST-CASE NOISE PATTERN SEARCH")
print("=" * 65)
print("What noise pattern most efficiently mimics K9_E suppression?")
print()

N_RANDOM_B3 = 100000
best_delta_chi2 = -1.0
best_noise = None
best_chi2_qm = None
best_chi2_k9e = None

print(f"  Searching {N_RANDOM_B3:,} random noise vectors in [-3, 3]^4 ...")
for _ in range(N_RANDOM_B3):
    eps = np.random.uniform(-3.0, 3.0, 4)
    data_noisy = {}
    for j, key in enumerate(SETTINGS):
        data_noisy[key] = dict(RAW_DATA[key])
        data_noisy[key]['E_exp'] = RAW_DATA[key]['E_exp'] + eps[j] * RAW_DATA[key]['sigma']
    dc, c2_qm, c2_k9e = delta_chi2_compute(data_noisy)
    if dc > best_delta_chi2:
        best_delta_chi2 = dc
        best_noise = eps.copy()
        best_chi2_qm = c2_qm
        best_chi2_k9e = c2_k9e

print("  Done.\n")

eps_map = {key: best_noise[i] for i, key in enumerate(SETTINGS)}
print("  Worst-case noise vector (sigma units):")
for key in SETTINGS:
    print(f"    eps({key}) = {eps_map[key]:+.2f}")
print(f"  Delta_chi2 with this noise: {best_delta_chi2:.4f}")
print(f"  (chi2_QM = {best_chi2_qm:.4f}, chi2_K9E = {best_chi2_k9e:.4f})")
print()

# Pattern check
V_qm_noisy, _ = fit_qm_only(data_noisy)
print(f"  Pattern analysis (V_QM = {V_qm_noisy:.4f}):")
print(f"  {'Setting':<8s} {'n_BSM':<6s} {'E_noisy':>10s} {'E_QM_vis':>10s} {'residual':>10s} {'res/sigma':>10s}")

residuals_bsm = {}
for key in SETTINGS:
    d = RAW_DATA[key]
    eps_val = eps_map[key]
    e_noisy = d['E_exp'] + eps_val * d['sigma']
    e_qm_vis = V_qm_noisy * E_QM[key]
    residual = e_noisy - e_qm_vis
    n_bsm = d['x'] + d['y']
    if n_bsm == 1:
        residuals_bsm.setdefault('1bsm', []).append(residual)
    elif n_bsm == 2:
        residuals_bsm['2bsm'] = residual
    print(f"  {key:<8s} {n_bsm:<6d} {e_noisy:>+10.4f} {e_qm_vis:>+10.4f} {residual:>+10.4f} {residual/d['sigma']:>+10.2f}")

if '1bsm' in residuals_bsm and '2bsm' in residuals_bsm:
    avg_1bsm = np.mean(residuals_bsm['1bsm'])
    ratio = residuals_bsm['2bsm'] / avg_1bsm if abs(avg_1bsm) > 1e-10 else float('inf')
    print(f"\n  2BSM residual: {residuals_bsm['2bsm']:+.4f}")
    print(f"  1BSM residual (avg): {avg_1bsm:+.4f}")
    print(f"  2BSM/1BSM ratio: {ratio:.3f}  (K9_E predicts ~2)")
    print(f"  Pattern matches K9_E signature? ", end="")
    if 1.0 < ratio < 4.0:
        print("YES - noise can mimic K9_E multiplicative pattern")
    else:
        print("PARTIAL - noise achieves Delta_chi2 but different residual pattern")
print()

# ============================================================
# SECTION 6: B4 - MULTI-SETTING NOISE THRESHOLD (Monte Carlo)
# ============================================================

print("=" * 65)
print("B4: MULTI-SETTING NOISE THRESHOLD (Monte Carlo)")
print("=" * 65)
print("What RMS noise is needed to produce Delta_chi2 >= 5.35?")
print()

N_RANDOM = 3000
rms_values = np.arange(0.1, 5.05, 0.1)
print(f"  Testing noise_RMS in [{rms_values[0]:.1f}, {rms_values[-1]:.1f}]")
print(f"  N_random = {N_RANDOM} per RMS value")
print(f"  Total fits: {len(rms_values)} x {N_RANDOM} = {len(rms_values) * N_RANDOM:,}")
print()

fraction_ge_target = []

for rms_val in rms_values:
    count_target = 0
    for _ in range(N_RANDOM):
        eps = np.random.normal(0, rms_val, 4)
        data_noisy = {}
        for j, key in enumerate(SETTINGS):
            data_noisy[key] = dict(RAW_DATA[key])
            data_noisy[key]['E_exp'] = RAW_DATA[key]['E_exp'] + eps[j] * RAW_DATA[key]['sigma']
        dc, _, _ = delta_chi2_compute(data_noisy)
        if dc >= DELTA_CHI2_TARGET:
            count_target += 1
    fraction_ge_target.append(count_target / N_RANDOM)

fraction_ge_target = np.array(fraction_ge_target)

# Find thresholds
threshold_2sigma = None
threshold_median = None
for i, rms_val in enumerate(rms_values):
    if threshold_2sigma is None and fraction_ge_target[i] >= 0.05:
        threshold_2sigma = rms_val
    if threshold_median is None and fraction_ge_target[i] >= 0.50:
        threshold_median = rms_val

print(f"  --- Delta_chi2 >= {DELTA_CHI2_TARGET:.2f} ({SIGMA_TARGET:.2f} sigma) ---")
print(f"  Noise threshold (2-sigma confidence, P>=0.05): ", end="")
if threshold_2sigma is not None:
    print(f"{threshold_2sigma:.2f} sigma RMS")
else:
    print("> 5.0 sigma RMS (not reached)")
print(f"  Noise threshold (median, P>=0.50):             ", end="")
if threshold_median is not None:
    print(f"{threshold_median:.2f} sigma RMS")
else:
    print("> 5.0 sigma RMS (not reached)")
print()

print("  --- Fraction exceeding Delta_chi2 target at key RMS ---")
for rms_check in [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]:
    idx = np.argmin(np.abs(rms_values - rms_check))
    print(f"    RMS = {rms_values[idx]:.1f} sigma: P = {fraction_ge_target[idx]:.4f}  ({fraction_ge_target[idx]*100:.1f}%)")
print()

# ============================================================
# SECTION 7: g_eff SENSITIVITY SCAN
# ============================================================

print("=" * 65)
print("B4-EXT: g_eff SENSITIVITY SCAN")
print("=" * 65)
print("How does the noise threshold depend on PP-4 calibration g_eff?")
print()

g_eff_values = np.arange(0.05, 0.31, 0.02)
N_RANDOM_G = 1000
rms_values_g = np.arange(0.2, 5.2, 0.2)

print(f"  g_eff in [{g_eff_values[0]:.2f}, {g_eff_values[-1]:.2f}]")
print(f"  N_random = {N_RANDOM_G} per (g_eff, RMS) pair")
print(f"  Total: {len(g_eff_values)} x {len(rms_values_g)} x {N_RANDOM_G} = {len(g_eff_values)*len(rms_values_g)*N_RANDOM_G:,} fits")
print()

g_thresholds = {}
for g_eff in g_eff_values:
    _, _, chi2_k9e_g = fit_k9e_full(RAW_DATA, g_eff)
    _, chi2_qm_g = fit_qm_only(RAW_DATA)
    dc_target_g = chi2_qm_g - chi2_k9e_g
    sigma_target_g = np.sqrt(max(0, dc_target_g))

    threshold_g = None
    for rms_val in rms_values_g:
        count = 0
        for _ in range(N_RANDOM_G):
            eps = np.random.normal(0, rms_val, 4)
            data_noisy = {}
            for j, key in enumerate(SETTINGS):
                data_noisy[key] = dict(RAW_DATA[key])
                data_noisy[key]['E_exp'] = RAW_DATA[key]['E_exp'] + eps[j] * RAW_DATA[key]['sigma']
            dc, _, _ = delta_chi2_compute(data_noisy, g_eff)
            if dc >= dc_target_g:
                count += 1
        if count / N_RANDOM_G >= 0.05:
            threshold_g = rms_val
            break

    g_thresholds[g_eff] = threshold_g
    thresh_str = f"{threshold_g:.2f}" if threshold_g is not None else ">5.0"
    print(f"  g_eff = {g_eff:.3f}: target = {dc_target_g:.3f} ({sigma_target_g:.2f}sigma), threshold = {thresh_str} sigma RMS")

print()

# ============================================================
# SECTION 8: FINAL VERDICT
# ============================================================

print("=" * 65)
print("FINAL VERDICT")
print("=" * 65)

noise_threshold = threshold_2sigma if threshold_2sigma is not None else float('inf')

print(f"  Noise threshold (2-sigma): {threshold_2sigma if threshold_2sigma else '>5.0'} sigma RMS")
print(f"  Most fragile setting:     {min_key} ({b2_thresholds[min_key]:.2f} sigma)")
print(f"  Worst-case pattern:       Delta_chi2 = {best_delta_chi2:.4f}")
print()

if noise_threshold > 3.0:
    verdict = "PASS"
    action = ("Close P10-NOISE: H=5->3, Risk=18.0->10.8. "
              "Remove [AH-NOISE] label.")
elif noise_threshold >= 1.0:
    verdict = "AMBIGUOUS"
    action = ("Keep P10-NOISE OPEN. Add boundary statement to index.md: "
              "\"'Genuine' claim is conditional on uniform noise assumption.\"")
else:
    verdict = "FAIL"
    action = ("Downgrade Class C (genuine) -> (qualified). "
              "Add boundary statement. Published error bars alone "
              "can explain non-uniform pattern.")

print(f"  VERDICT: {verdict}")
print(f"  Action:  {action}")
print()
print("  LIMITATIONS (explicit):")
print("    1. Error bars are Poissonian - systematic noise NOT characterized.")
print("    2. 4 data points carry no noise correlation information.")
print("    3. This analysis does NOT replace 3-observer experiment.")
print()
print("=" * 65)
print("ANALYSIS COMPLETE")
print("=" * 65)
print(f"  Methodology:  Delta_chi2 Decomposition + Noise Budget Analysis")
print(f"  RCA ref:      RCA_P10_NOISE_methodology_decision_2026_05_24.md (4.77/5)")
print(f"  Spec ref:     noise_sensitivity_analysis_spec.md")
