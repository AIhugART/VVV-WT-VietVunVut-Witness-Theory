"""
Verify FOM with beta_k9=0.30 and per-theta angle optimization
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

def z_proj(o):
    return np.array([[1,0],[0,0]], dtype=complex) if o==+1 else np.array([[0,0],[0,1]], dtype=complex)

def bloch_state(theta, phi, o):
    ct, st = np.cos(theta/2), np.sin(theta/2)
    ep = np.exp(1j*phi)
    return np.array([ct, ep*st]) if o==+1 else np.array([st, -ep*ct])

def tilted_proj(az, theta, o):
    s = bloch_state(theta, az, o)
    return np.outer(s, s.conj())

def compute_fom(rho, theta, phi2, phi3, beta_bob, beta_k9, N=91000):
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
    
    f_perp = {(+1,+1): np.sin(theta/2)**2, (-1,+1): np.cos(theta/2)**2,
              (+1,-1): np.cos(theta/2)**2, (-1,-1): np.sin(theta/2)**2}
    P_cd = {}
    for c in [+1,-1]:
        for d in [+1,-1]:
            P_cd[(c,d)] = max(0, np.real(np.trace(np.kron(z_proj(c),z_proj(d))@rho)))
    
    best_nsig = 0
    for y_set in [2,3]:
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
    return fom, n_lf, best_nsig

mu = 0.95
rho = make_rho(mu)
N = 91000

# Quick sanity: theta=31, optimized angles, beta_k9=0.30
phi2, phi3, bb = np.radians(112), np.radians(217), np.radians(20)
fom, nlf, nsig = compute_fom(rho, np.radians(31), phi2, phi3, bb, 0.30)
print(f"theta=31, beta=0.30, optimized angles:")
print(f"  n_LF={nlf:.1f}, n_sig={nsig:.1f}, FOM={fom:.1f}")
print(f"  Manuscript claims FOM=8.6 -> {'MATCH' if abs(fom-8.6)<0.5 else 'MISMATCH'}")
print()

# Per-theta optimization
claimed = {20: 5.8, 31: 8.6, 45: 6.0, 58: 0, 90: 0}
print("Per-theta angle optimization (beta_k9=0.30, grid 30deg+fine 5deg):")
header = f"{'theta':>6s}  {'FOM':>8s}  {'n_LF':>8s}  {'n_sig':>8s}  {'claimed':>8s}"
print(header)
print("-"*45)

for td in [20, 25, 31, 35, 40, 45, 50, 55, 58, 60, 70, 80, 90]:
    tr = np.radians(td)
    best_fom = 0
    best_p = (0, 0, 0)
    
    for p2 in range(0, 360, 30):
        for p3 in range(0, 360, 30):
            for bbd in range(0, 360, 30):
                try:
                    f, _, _ = compute_fom(rho, tr, np.radians(p2), np.radians(p3), np.radians(bbd), 0.30)
                    if f > best_fom:
                        best_fom = f
                        best_p = (p2, p3, bbd)
                except: pass
    
    bp2, bp3, bbb = best_p
    for dp2 in range(-20, 21, 5):
        for dp3 in range(-20, 21, 5):
            for db in range(-20, 21, 5):
                try:
                    f, _, _ = compute_fom(rho, tr, np.radians(bp2+dp2), np.radians(bp3+dp3), np.radians(bbb+db), 0.30)
                    if f > best_fom:
                        best_fom = f
                        best_p = (bp2+dp2, bp3+dp3, bbb+db)
                except: pass
    
    fom_f, nlf_f, nsig_f = compute_fom(rho, tr, np.radians(best_p[0]), np.radians(best_p[1]), np.radians(best_p[2]), 0.30)
    cl = claimed.get(td, "?")
    print(f"{td:6d}  {fom_f:8.1f}  {nlf_f:8.1f}  {nsig_f:8.1f}  {str(cl):>8s}")
