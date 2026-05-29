"""
Focused FOM investigation at theta=20 and theta=58 (beta=0.30).
Ultra-fine grid search to check if higher FOM values are achievable.
"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
import numpy as np

def make_rho(mu):
    phi_minus = np.array([0, 1, -1, 0], dtype=complex) / np.sqrt(2)
    hv = np.array([0, 1, 0, 0], dtype=complex)
    vh = np.array([0, 0, 1, 0], dtype=complex)
    return mu * np.outer(phi_minus, phi_minus.conj()) + (1-mu)/2 * (
        np.outer(hv, hv.conj()) + np.outer(vh, vh.conj()))

H = np.array([1,0], dtype=complex)
V = np.array([0,1], dtype=complex)
I2 = np.eye(2, dtype=complex)

def z_proj(o):
    return np.array([[1,0],[0,0]], dtype=complex) if o==+1 else np.array([[0,0],[0,1]], dtype=complex)

def bloch_state(theta, phi, o):
    ct, st = np.cos(theta/2), np.sin(theta/2)
    ep = np.exp(1j*phi)
    return np.array([ct, ep*st]) if o==+1 else np.array([st, -ep*ct])

def tilted_proj(az, theta, o):
    s = bloch_state(theta, az, o)
    return np.outer(s, s.conj())

def compute_gen_lf1_and_fom(rho, theta, phi2, phi3, beta_bob, beta_k9=0.30, N=91000):
    aa = {2: phi2, 3: phi3}
    ba = {2: beta_bob - phi2, 3: beta_bob - phi3}
    
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
        if s==1: Pp, Pm = z_proj(+1), z_proj(-1)
        else: Pp, Pm = tilted_proj(aa[s], theta, +1), tilted_proj(aa[s], theta, -1)
        mA[s] = np.real(np.trace(np.kron(Pp-Pm, I2)@rho))
        if s==1: Pp, Pm = z_proj(+1), z_proj(-1)
        else: Pp, Pm = tilted_proj(ba[s], theta, +1), tilted_proj(ba[s], theta, -1)
        mB[s] = np.real(np.trace(np.kron(I2, Pp-Pm)@rho))
    
    S = (-mA[1]-mA[2]-mB[1]-mB[2]-corrs[(1,1)]-2*corrs[(1,2)]-2*corrs[(2,1)]
         +2*corrs[(2,2)]-corrs[(2,3)]-corrs[(3,2)]-corrs[(3,3)]-6)
    
    ts = [(-1,mA[1]),(-1,mA[2]),(-1,mB[1]),(-1,mB[2]),(-1,corrs[(1,1)]),
          (-2,corrs[(1,2)]),(-2,corrs[(2,1)]),(2,corrs[(2,2)]),
          (-1,corrs[(2,3)]),(-1,corrs[(3,2)]),(-1,corrs[(3,3)])]
    sig_lf = np.sqrt(sum(c**2*max(0,1-v**2)/N for c,v in ts))
    n_lf = S/sig_lf if S>0 and sig_lf>0 else 0
    
    # Signal
    f_perp = {(+1,+1): np.sin(theta/2)**2, (-1,+1): np.cos(theta/2)**2,
              (+1,-1): np.cos(theta/2)**2, (-1,-1): np.sin(theta/2)**2}
    P_cd = {}
    for c in [+1,-1]:
        for d in [+1,-1]:
            P_cd[(c,d)] = max(0, np.real(np.trace(np.kron(z_proj(c),z_proj(d))@rho)))
    
    best_nsig = 0
    for y_set in [2, 3]:
        az_y = ba[y_set]
        P_bd = {}
        for b in [+1,-1]:
            for d in [+1,-1]:
                Pb = tilted_proj(az_y, theta, b)
                ds = H if d==+1 else V
                P_bd[(b,d)] = max(0, np.real(ds.conj()@Pb@ds))
        Pk = {}; Z = 0
        for c in [+1,-1]:
            for b in [+1,-1]:
                val = sum(P_cd[(c,d)]*P_bd[(b,d)]*(1-beta_k9*f_perp[(b,d)]) for d in [+1,-1])
                Pk[(c,b)] = val; Z += val
        ck9e = sum(c*b*Pk[(c,b)]/Z for c in [+1,-1] for b in [+1,-1])
        delta = abs(ck9e - corrs[(1,y_set)])
        sig_ab = np.sqrt(max(0,1-corrs[(1,y_set)]**2)/N)
        ns = delta/sig_ab if sig_ab>0 else 0
        if ns > best_nsig: best_nsig = ns
    
    fom = min(n_lf, best_nsig) if S>0 else 0
    return S, n_lf, best_nsig, fom

mu = 0.95
rho = make_rho(mu)

print("="*80)
print("FOCUSED INVESTIGATION: theta=20 and theta=58 (beta_k9=0.30)")
print("="*80)

for theta_deg in [20, 45, 50, 55, 58]:
    theta = np.radians(theta_deg)
    print(f"\n--- theta = {theta_deg} deg ---")
    
    best_fom = 0
    best_nlf = 0
    best_params = None
    best_S = 0
    
    # Fine grid: 10-deg steps for all three angles
    for p2 in range(0, 360, 10):
        for p3 in range(0, 360, 10):
            for bb in range(0, 360, 10):
                try:
                    S, nlf, nsig, fom = compute_gen_lf1_and_fom(
                        rho, theta, np.radians(p2), np.radians(p3), np.radians(bb))
                    if fom > best_fom:
                        best_fom = fom
                        best_nlf = nlf
                        best_params = (p2, p3, bb)
                        best_S = S
                except:
                    pass
                # Also track best n_LF
                if nlf > best_nlf:
                    best_nlf_only = nlf
    
    if best_params:
        bp2, bp3, bbb = best_params
        # Ultra-fine grid around best: 2-deg steps
        for dp2 in range(-8, 9, 2):
            for dp3 in range(-8, 9, 2):
                for db in range(-8, 9, 2):
                    try:
                        S, nlf, nsig, fom = compute_gen_lf1_and_fom(
                            rho, theta, np.radians(bp2+dp2), np.radians(bp3+dp3), np.radians(bbb+db))
                        if fom > best_fom:
                            best_fom = fom
                            best_params = (bp2+dp2, bp3+dp3, bbb+db)
                            best_S = S
                    except:
                        pass
    
    if best_params:
        S, nlf, nsig, fom = compute_gen_lf1_and_fom(
            rho, theta, np.radians(best_params[0]), np.radians(best_params[1]), np.radians(best_params[2]))
        print(f"  Best FOM = {fom:.2f}  (n_LF={nlf:.2f}, n_sig={nsig:.2f})")
        print(f"  Gen LF 1 = {S:+.4f}")
        print(f"  Angles: phi2={best_params[0]}, phi3={best_params[1]}, beta={best_params[2]}")
    else:
        print(f"  No positive FOM found")
    
    # Also find max n_LF achievable (even if FOM=0 because signal=0)
    max_nlf = 0
    max_nlf_S = 0
    max_nlf_params = None
    for p2 in range(0, 360, 10):
        for p3 in range(0, 360, 10):
            for bb in range(0, 360, 10):
                try:
                    S, nlf, _, _ = compute_gen_lf1_and_fom(
                        rho, theta, np.radians(p2), np.radians(p3), np.radians(bb))
                    if nlf > max_nlf:
                        max_nlf = nlf
                        max_nlf_S = S
                        max_nlf_params = (p2, p3, bb)
                except:
                    pass
    print(f"  Max n_LF achievable = {max_nlf:.2f}  (Gen LF 1 = {max_nlf_S:+.4f})")
    if max_nlf_params:
        print(f"  Angles: phi2={max_nlf_params[0]}, phi3={max_nlf_params[1]}, beta={max_nlf_params[2]}")

print()
print("="*80)
print("MANUSCRIPT v94 claims for FOM at beta=0.30:")
print("  theta=20: FOM=5.8")
print("  theta=31: FOM=8.6 (near-optimal, plateau 31-35)")
print("  theta=35: FOM=8.8")
print("  theta=45: FOM=6.0")
print("  theta=58: FOM=0 (Gen LF 1 negative)")
print("  FOM > 5sigma for theta in [20, 45]")
print("=" * 80)
