"""
RCA Supplemental: Verify FOM with per-theta angle re-optimization
=================================================================
The manuscript says (Section 4.1):
  "A grid search over (theta, phi2, phi3, beta_Bob) maximizing
   min(n_sig_LF, n_sig_signal) yields theta=31 as optimal"

This means the azimuthal angles are RE-OPTIMIZED at each theta.
Let's verify this.
"""

import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
import numpy as np

# === Core functions ===
def make_rho(mu):
    phi_minus = np.array([0, 1, -1, 0], dtype=complex) / np.sqrt(2)
    hv = np.array([0, 1, 0, 0], dtype=complex)
    vh = np.array([0, 0, 1, 0], dtype=complex)
    return mu * np.outer(phi_minus, phi_minus.conj()) + (1-mu)/2 * (
        np.outer(hv, hv.conj()) + np.outer(vh, vh.conj()))

H = np.array([1,0], dtype=complex)
V = np.array([0,1], dtype=complex)

def z_proj(o):
    return np.array([[1,0],[0,0]], dtype=complex) if o==+1 else np.array([[0,0],[0,1]], dtype=complex)

def bloch_state(theta, phi, o):
    ct, st = np.cos(theta/2), np.sin(theta/2)
    ep = np.exp(1j*phi)
    return np.array([ct, ep*st]) if o==+1 else np.array([st, -ep*ct])

def tilted_proj(az, theta, o):
    s = bloch_state(theta, az, o)
    return np.outer(s, s.conj())

def compute_all_vals(rho, theta, phi2, phi3, beta_bob, N=91000):
    aa = {2: phi2, 3: phi3}
    ba = {2: beta_bob - phi2, 3: beta_bob - phi3}
    I2 = np.eye(2, dtype=complex)
    
    corrs = {}
    for x in [1,2,3]:
        for y in [1,2,3]:
            r = 0.0
            for a in [+1,-1]:
                for b in [+1,-1]:
                    Pa = z_proj(a) if x==1 else tilted_proj(aa[x], theta, a)
                    Pb = z_proj(b) if y==1 else tilted_proj(ba[y], theta, b)
                    r += a*b*max(0, np.real(np.trace(np.kron(Pa,Pb)@rho)))
            corrs[(x,y)] = r
    
    mA, mB = {}, {}
    for s in [1,2,3]:
        if s==1:
            Pp, Pm = z_proj(+1), z_proj(-1)
        else:
            Pp = tilted_proj(aa[s], theta, +1)
            Pm = tilted_proj(aa[s], theta, -1)
        mA[s] = np.real(np.trace(np.kron(Pp-Pm, I2)@rho))
        if s==1:
            Pp, Pm = z_proj(+1), z_proj(-1)
        else:
            Pp = tilted_proj(ba[s], theta, +1)
            Pm = tilted_proj(ba[s], theta, -1)
        mB[s] = np.real(np.trace(np.kron(I2, Pp-Pm)@rho))
    
    S = (-mA[1]-mA[2]-mB[1]-mB[2]
         -corrs[(1,1)]-2*corrs[(1,2)]-2*corrs[(2,1)]+2*corrs[(2,2)]
         -corrs[(2,3)]-corrs[(3,2)]-corrs[(3,3)]-6)
    
    ts = [(-1,mA[1]),(-1,mA[2]),(-1,mB[1]),(-1,mB[2]),
          (-1,corrs[(1,1)]),(-2,corrs[(1,2)]),(-2,corrs[(2,1)]),
          (2,corrs[(2,2)]),(-1,corrs[(2,3)]),(-1,corrs[(3,2)]),(-1,corrs[(3,3)])]
    sig_lf = np.sqrt(sum(c**2*max(0,1-v**2)/N for c,v in ts))
    n_lf = S/sig_lf if S>0 and sig_lf>0 else 0
    
    # K9E delta (beta=0.07, setting (1,2))
    f_perp = {(+1,+1): np.sin(theta/2)**2, (-1,+1): np.cos(theta/2)**2,
              (+1,-1): np.cos(theta/2)**2, (-1,-1): np.sin(theta/2)**2}
    P_cd = {}
    for c in [+1,-1]:
        for d in [+1,-1]:
            P_cd[(c,d)] = max(0, np.real(np.trace(np.kron(z_proj(c),z_proj(d))@rho)))
    az_y = ba[2]
    P_bd = {}
    for b in [+1,-1]:
        for d in [+1,-1]:
            Pb = tilted_proj(az_y, theta, b)
            ds = H if d==+1 else V
            P_bd[(b,d)] = max(0, np.real(ds.conj()@Pb@ds))
    Pk = {}
    Z = 0
    beta_k9 = 0.07
    for c in [+1,-1]:
        for b in [+1,-1]:
            val = sum(P_cd[(c,d)]*P_bd[(b,d)]*(1-beta_k9*f_perp[(b,d)]) for d in [+1,-1])
            Pk[(c,b)] = val
            Z += val
    corr_k9e = sum(c*b*Pk[(c,b)]/Z for c in [+1,-1] for b in [+1,-1])
    delta = abs(corr_k9e - corrs[(1,2)])
    sig_ab = np.sqrt(max(0,1-corrs[(1,2)]**2)/N)
    n_sig = delta/sig_ab if sig_ab>0 else 0
    
    fom = min(n_lf, n_sig) if S>0 else 0
    return S, n_lf, delta, n_sig, fom

mu = 0.95
rho = make_rho(mu)
N = 91000

print("="*80)
print("FOM with PER-THETA angle re-optimization")
print("  Grid search: phi2 in [0,360,20), phi3 in [0,360,20), beta in [0,360,20)")
print("  mu=0.95, N=91,000, beta_K9E=0.07")
print("="*80)
print()

fom_results = []

for theta_deg in range(15, 91, 1):
    theta = np.radians(theta_deg)
    best_fom = 0
    best_params = (0, 0, 0)
    
    # Coarse grid (20-deg steps for speed)
    for p2 in range(0, 360, 20):
        for p3 in range(0, 360, 20):
            for bb in range(0, 360, 20):
                try:
                    _, _, _, _, fom = compute_all_vals(
                        rho, theta, np.radians(p2), np.radians(p3), np.radians(bb), N)
                    if fom > best_fom:
                        best_fom = fom
                        best_params = (p2, p3, bb)
                except:
                    pass
    
    # Fine grid around best (5-deg steps)
    bp2, bp3, bbb = best_params
    for dp2 in range(-15, 16, 5):
        for dp3 in range(-15, 16, 5):
            for db in range(-15, 16, 5):
                try:
                    _, _, _, _, fom = compute_all_vals(
                        rho, theta, np.radians(bp2+dp2), np.radians(bp3+dp3),
                        np.radians(bbb+db), N)
                    if fom > best_fom:
                        best_fom = fom
                        best_params = (bp2+dp2, bp3+dp3, bbb+db)
                except:
                    pass
    
    S, n_lf, delta, n_sig, fom_final = compute_all_vals(
        rho, theta, np.radians(best_params[0]), np.radians(best_params[1]),
        np.radians(best_params[2]), N)
    
    fom_results.append((theta_deg, best_fom, S, n_lf, delta, n_sig, best_params))

# Print table
print(f"  {'theta':>6s}  {'FOM':>8s}  {'GenLF1':>8s}  {'n_LF':>8s}  {'|delta|':>10s}  {'n_sig':>8s}  {'phi2':>6s}  {'phi3':>6s}  {'beta':>6s}")
print("  "+"-"*80)
for r in fom_results:
    td = r[0]
    if td in [15,20,25,30,31,35,40,45,50,55,58,60,70,80,90] or td == max(fom_results, key=lambda x:x[1])[0]:
        marker = " <<<" if r[1] == max(fom_results, key=lambda x:x[1])[1] else ""
        print(f"  {td:6d}  {r[1]:8.1f}  {r[2]:8.4f}  {r[3]:8.1f}  {r[4]:10.6f}  {r[5]:8.1f}  "
              f"{r[6][0]:6d}  {r[6][1]:6d}  {r[6][2]:6d}{marker}")

best_overall = max(fom_results, key=lambda x: x[1])
print(f"\n  OPTIMAL: theta={best_overall[0]} deg, FOM={best_overall[1]:.1f}")
print(f"  Angles: phi2={best_overall[6][0]}, phi3={best_overall[6][1]}, beta={best_overall[6][2]}")
print()

# Manuscript claims
print("Manuscript claims:")
claimed_fom = {20: 9.6, 31: 8.6, 45: 7.1, 58: 5.0, 90: 0}
for td, cf in claimed_fom.items():
    r = next(x for x in fom_results if x[0]==td)
    match = "MATCH" if abs(r[1]-cf) < 1.5 else "MISMATCH"
    print(f"  theta={td}: computed={r[1]:.1f}, claimed={cf}, [{match}]")

# Check 5sigma plateau
above_5 = [r for r in fom_results if r[1] >= 5.0]
if above_5:
    theta_range = (min(r[0] for r in above_5), max(r[0] for r in above_5))
    print(f"\n  FOM >= 5sigma range: theta in [{theta_range[0]}, {theta_range[1]}] deg")
    print(f"  Manuscript claims: [20, 55] deg")
