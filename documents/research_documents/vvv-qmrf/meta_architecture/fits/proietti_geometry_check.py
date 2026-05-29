"""
Proietti Geometry Check: Does f_perp cancel?
=============================================
Binary question: Is the superobserver measurement in Proietti
maximally incompatible with the Friend's z-basis?

If YES (constant f_perp) -> cancellation -> K9-S12
If NO  (varies f_perp)  -> no cancellation -> Phase 10a

Proietti 2019 (arXiv:1902.05080):
  N=2 settings per party, CHSH test
  x=0: Alice reads Friend (a=c, z-basis)
  x=1: Alice does BSM (reverses Friend + measures at angle)
  
  Mixed settings: (x=0,y=1) and (x=1,y=0) -- same structure as Bong

Key: WHAT BASIS does the superobserver effectively measure in
after reversing the Friend's z-measurement?

Answer: For CHSH-optimal violation with singlet, ALL measurements
are in the equatorial (XY) plane of the Bloch sphere.
"""

import numpy as np

print("=" * 70)
print("PROIETTI GEOMETRY CHECK: f_perp constant or varies?")
print("=" * 70)
print()

# ============================================================
# PART 1: What basis does Proietti's superobserver use?
# ============================================================

print("PART 1: Proietti's Measurement Structure")
print("-" * 45)
print()
print("Proietti 2019: 6-photon CHSH experiment")
print("  Friend measures: z-basis (|H>, |V>)")
print("  Superobserver x=0: reads Friend (a=c)")
print("  Superobserver x=1: BSM (reverses Friend + measures photon)")
print()
print("The BSM effectively measures the photon in the XY-plane")
print("after undoing the Friend-photon entanglement.")
print()
print("For CHSH optimization with singlet |Psi->:")
print("  Standard optimal angles (Bloch sphere equator):")
print("    Alice x=1: theta_A = 0 deg (or pi/4 = 45 deg)")  
print("    Bob   y=1: theta_B = pi/8 = 22.5 deg (or -22.5 deg)")
print("  ALL are in the XY-plane (theta_Bloch = pi/2)")
print()

# ============================================================
# PART 2: Compute |<b|d>|^2 for equatorial measurements
# ============================================================

print("PART 2: Overlap Computation")
print("-" * 45)
print()

def compute_overlap(theta_bloch, phi_angle, d_label):
    """
    Compute |<b(theta,phi) | d_z>|^2
    
    Superobserver state on Bloch sphere:
      |b=+1> = cos(theta/2)|H> + exp(i*phi)*sin(theta/2)|V>
      |b=-1> = sin(theta/2)|H> - exp(i*phi)*cos(theta/2)|V>
    
    Friend's z-basis:
      d=+1 -> |H> = [1, 0]
      d=-1 -> |V> = [0, 1]
    """
    if d_label == "H":
        d_state = np.array([1, 0], dtype=complex)
    else:
        d_state = np.array([0, 1], dtype=complex)
    
    b_plus = np.array([
        np.cos(theta_bloch / 2),
        np.exp(1j * phi_angle) * np.sin(theta_bloch / 2)
    ], dtype=complex)
    
    b_minus = np.array([
        np.sin(theta_bloch / 2),
        -np.exp(1j * phi_angle) * np.cos(theta_bloch / 2)
    ], dtype=complex)
    
    overlap_plus = np.abs(np.vdot(b_plus, d_state))**2
    overlap_minus = np.abs(np.vdot(b_minus, d_state))**2
    
    return overlap_plus, overlap_minus


# Test 1: Standard CHSH angles (ALL equatorial: theta_Bloch = pi/2)
print("Test 1: Standard CHSH-optimal angles")
print("  (All equatorial: theta_Bloch = pi/2)")
print()

chsh_angles = {
    "Alice x=1 (a1=0 deg)":    (np.pi/2, np.radians(0)),
    "Alice x=1 (a1=45 deg)":   (np.pi/2, np.radians(45)),
    "Bob y=1 (b1=22.5 deg)":   (np.pi/2, np.radians(22.5)),
    "Bob y=1 (b1=-22.5 deg)":  (np.pi/2, np.radians(-22.5)),
}

print(f"{'Setting':>28s}  {'|<b+|H>|^2':>12s}  {'|<b-|H>|^2':>12s}  "
      f"{'|<b+|V>|^2':>12s}  {'|<b-|V>|^2':>12s}  {'Constant?':>10s}")
print("-" * 95)

all_constant = True
for label, (theta, phi) in chsh_angles.items():
    op_H, om_H = compute_overlap(theta, phi, "H")
    op_V, om_V = compute_overlap(theta, phi, "V")
    
    is_const = (abs(op_H - om_H) < 1e-10 and 
                abs(op_V - om_V) < 1e-10 and
                abs(op_H - op_V) < 1e-10)
    if not is_const:
        all_constant = False
    
    print(f"{label:>28s}  {op_H:12.6f}  {om_H:12.6f}  "
          f"{op_V:12.6f}  {om_V:12.6f}  {'YES' if is_const else '** NO **':>10s}")

print()
print(f"  All overlaps = 0.5? {'YES' if all_constant else 'NO'}")
print()

# Test 2: Bong angles (also equatorial: theta_Bloch = pi/2)
print("Test 2: Bong angles (user-specified, also equatorial)")
print()

bong_angles = {
    "phi_1=168 deg":  (np.pi/2, np.radians(168)),
    "phi_2=0 deg":    (np.pi/2, np.radians(0)),
    "phi_3=118 deg":  (np.pi/2, np.radians(118)),
    "beta-phi_2=175": (np.pi/2, np.radians(175)),
    "beta-phi_3=57":  (np.pi/2, np.radians(57)),
}

print(f"{'Setting':>28s}  {'|<b+|H>|^2':>12s}  {'|<b-|H>|^2':>12s}  "
      f"{'|<b+|V>|^2':>12s}  {'|<b-|V>|^2':>12s}  {'Constant?':>10s}")
print("-" * 95)

all_const_bong = True
for label, (theta, phi) in bong_angles.items():
    op_H, om_H = compute_overlap(theta, phi, "H")
    op_V, om_V = compute_overlap(theta, phi, "V")
    
    is_const = (abs(op_H - om_H) < 1e-10 and 
                abs(op_V - om_V) < 1e-10 and
                abs(op_H - op_V) < 1e-10)
    if not is_const:
        all_const_bong = False
    
    print(f"{label:>28s}  {op_H:12.6f}  {om_H:12.6f}  "
          f"{op_V:12.6f}  {om_V:12.6f}  {'YES' if is_const else '** NO **':>10s}")

print()
print(f"  All overlaps = 0.5? {'YES' if all_const_bong else 'NO'}")
print()

# ============================================================
# PART 3: PROOF that ANY equatorial measurement gives constant
# ============================================================

print("PART 3: General Proof")
print("-" * 45)
print()
print("THEOREM: For ANY measurement in the XY-plane (theta_Bloch = pi/2),")
print("  |<b(pi/2, phi) | d_z>|^2 = 1/2 for ALL (b, d, phi).")
print()
print("PROOF:")
print("  |b=+1> = (|H> + e^{i*phi}|V>) / sqrt(2)")
print("  |<b=+1 | H>|^2 = |1/sqrt(2)|^2 = 1/2")
print("  |<b=+1 | V>|^2 = |e^{i*phi}/sqrt(2)|^2 = 1/2")
print("  |<b=-1 | H>|^2 = |1/sqrt(2)|^2 = 1/2")
print("  |<b=-1 | V>|^2 = |-e^{i*phi}/sqrt(2)|^2 = 1/2")
print()
print("  This is INDEPENDENT of phi. QED.")
print()
print("  CONSEQUENCE: ANY experiment where:")
print("    Friend measures in z-basis (poles)")
print("    Superobserver measures in XY-plane (equator)")
print("  will have f_perp = 1/2 (constant) => CANCELLATION.")
print()

# ============================================================
# PART 4: Verify with random angles
# ============================================================

print("PART 4: Monte Carlo Verification (1000 random equatorial angles)")
print("-" * 45)
print()

rng = np.random.default_rng(42)
max_deviation = 0.0
for _ in range(1000):
    phi_rand = rng.uniform(0, 2 * np.pi)
    theta_rand = np.pi / 2  # equatorial
    
    op_H, om_H = compute_overlap(theta_rand, phi_rand, "H")
    op_V, om_V = compute_overlap(theta_rand, phi_rand, "V")
    
    dev = max(abs(op_H - 0.5), abs(om_H - 0.5), 
              abs(op_V - 0.5), abs(om_V - 0.5))
    max_deviation = max(max_deviation, dev)

print(f"  Max deviation from 0.5 across 1000 random angles: {max_deviation:.2e}")
print(f"  (Machine epsilon ~ {np.finfo(float).eps:.2e})")
print()

# ============================================================
# PART 5: Check if Proietti COULD have non-equatorial settings
# ============================================================

print("PART 5: Could Proietti Use Non-Equatorial Settings?")
print("-" * 45)
print()
print("Proietti's BSM involves:")
print("  1. Friend measures photon in z-basis (|H>, |V>)")
print("  2. Superobserver reverses Friend's measurement (U_z^dag)")
print("  3. Superobserver measures photon at some angle")
print()
print("Step 3's angle determines theta_Bloch.")
print("For CHSH optimization with singlet, step 3 is ALWAYS equatorial")
print("because sin(2*alpha) is maximized at alpha=pi/4 (equatorial).")
print()
print("However: a non-standard implementation COULD use tilted angles.")
print("This would sacrifice CHSH violation strength but enable K9_E testing.")
print()

# ============================================================
# PART 6: What about the BSM itself? Is it truly equatorial?
# ============================================================

print("PART 6: BSM as Effective Single-Qubit Measurement")
print("-" * 45)
print()
print("The BSM on (Friend_memory, Photon) projects onto Bell basis.")
print("After the Friend measured z-basis and recorded outcome c:")
print("  Post-Friend state: |c>_F |c>_S")
print()
print("  BSM outcomes and overlaps with |c>_F |c>_S:")
print("    |Phi+> = (|HH> + |VV>)/sqrt(2)")
print("    |Phi-> = (|HH> - |VV>)/sqrt(2)")
print("    |Psi+> = (|HV> + |VH>)/sqrt(2)")
print("    |Psi-> = (|HV> - |VH>)/sqrt(2)")
print()

for c_label in ["H", "V"]:
    c_state = np.array([1, 0], dtype=complex) if c_label == "H" else np.array([0, 1], dtype=complex)
    cc_state = np.kron(c_state, c_state)  # |cc> in 4D
    
    # Bell states
    phi_plus = np.array([1, 0, 0, 1], dtype=complex) / np.sqrt(2)
    phi_minus = np.array([1, 0, 0, -1], dtype=complex) / np.sqrt(2)
    psi_plus = np.array([0, 1, 1, 0], dtype=complex) / np.sqrt(2)
    psi_minus = np.array([0, 1, -1, 0], dtype=complex) / np.sqrt(2)
    
    print(f"  c={c_label} (state = |{c_label}{c_label}>):")
    for bell_label, bell_state in [("Phi+", phi_plus), ("Phi-", phi_minus),
                                     ("Psi+", psi_plus), ("Psi-", psi_minus)]:
        overlap = np.abs(np.vdot(bell_state, cc_state))**2
        print(f"    |<{bell_label}|{c_label}{c_label}>|^2 = {overlap:.4f}")
    print()

print("  KEY: For c=H, BSM gives 50/50 between Phi+ and Phi-.")
print("       For c=V, BSM gives 50/50 between Phi+ and Phi-.")
print("       Psi+/Psi- have ZERO overlap with |cc>.")
print()
print("  If BSM is binned as a={+1,-1}:")
print("    Grouping 1: a=+1 -> {Phi+,Psi+}, a=-1 -> {Phi-,Psi-}")
print("      P(a=+1|c=H) = 1/2, P(a=+1|c=V) = 1/2  => CONSTANT")
print("    Grouping 2: a=+1 -> {Phi+,Psi-}, a=-1 -> {Phi-,Psi+}")
print("      P(a=+1|c=H) = 1/2, P(a=+1|c=V) = 1/2  => CONSTANT")
print("    ANY binary grouping of Bell states gives constant overlap!")
print()

# ============================================================
# BINARY ANSWER
# ============================================================

print("=" * 70)
print()
print("  +-------------------------------------------------+")
print("  |                                                   |")
print("  |   BINARY ANSWER: CONSTANT                        |")
print("  |                                                   |")
print("  |   f_perp = 1/2 for ALL Proietti settings.        |")
print("  |   Marginalization cancellation applies.           |")
print("  |   K9_E = QM for the standard Proietti protocol.  |")
print("  |                                                   |")
print("  |   DECISION: GO TO K9-S12                          |")
print("  |   (Design modified experiment with tilted basis)  |")
print("  |                                                   |")
print("  +-------------------------------------------------+")
print()
print("=" * 70)
print()

# ============================================================
# UNIVERSAL THEOREM
# ============================================================

print("UNIVERSAL THEOREM:")
print()
print("  For ANY Extended Wigner's Friend experiment where:")
print("    (a) Friend measures in z-basis ({|H>, |V>})")
print("    (b) Superobserver's effective measurement is equatorial")
print("        (theta_Bloch = pi/2, ANY azimuthal angle phi)")
print()
print("  Then: f_perp = 1/2 (constant, outcome-independent)")
print("        => Marginalization cancellation applies")
print("        => K9_E is INDISTINGUISHABLE from QM")
print()
print("  This covers:")
print("    - Proietti 2019 (CHSH, N=2)")
print("    - Bong 2020 (LF, N=3)")  
print("    - ANY future experiment with z-Friend + equatorial-Superobserver")
print()
print("  To test K9_E, one MUST use a TILTED superobserver basis")
print("  (0 < theta_Bloch < pi/2).")
