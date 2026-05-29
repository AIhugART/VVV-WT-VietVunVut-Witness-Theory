"""
Analysis of Discussion Table (line 632) claim:
    delta<AB> at theta=31 = beta*cos(31) ~ 0.857*beta
"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
import numpy as np

cos31 = np.cos(np.radians(31))

# Numerical deltas from our computation
deltas = {
    0.03: 0.0034,
    0.05: 0.0057,
    0.07: 0.0080,
    0.10: 0.0115,
    0.30: 0.0355,
}

print("DISCUSSION TABLE (line 632) ANALYSIS")
print("=" * 70)
print()
print("Manuscript Discussion Table claims:")
print("  delta<AB> at theta=31 | Overlap-only: beta*cos(31) = 0.857*beta")
print()
print(f"cos(31) = {cos31:.6f}")
print()
print(f"  {'beta':>6s}  {'beta*cos31':>12s}  {'num_delta':>12s}  {'ratio':>8s}")
print(f"  {'-'*45}")
for beta in [0.03, 0.05, 0.07, 0.10, 0.30]:
    approx = beta * cos31
    actual = deltas[beta]
    ratio = actual / approx
    print(f"  {beta:6.2f}  {approx:12.4f}  {actual:12.4f}  {ratio:8.4f}")

print()
print("FINDING: numerical delta is only ~13% of beta*cos(31)")
print()
print("However, reading the table more carefully:")
print("  The table shows 'beta*cos(31) ~ 0.857*beta' as the")
print("  FUNCTIONAL FORM, not the exact value.")
print("  The proportionality constant is implicit (absorbed into beta).")
print()
print("The manuscript text (lines 42, 183, 527) explicitly says:")
print("  'delta<AB> PROPORTIONAL TO cos(theta) (at LEADING ORDER in beta)'")
print("  This is correct: delta ~ C(beta)*cos(theta)")
print()
print("delta/beta for each beta:")
for beta in [0.03, 0.05, 0.07, 0.10, 0.30]:
    actual = deltas[beta]
    print(f"  beta={beta}: delta/beta = {actual/beta:.4f}")

print()
print("The proportionality is NOT exactly linear in beta either,")
print("because Z(beta) depends on beta. delta/beta ~ 0.113-0.118.")
print()
print("VERDICT:")
print("  The Discussion Table entry 'beta*cos(31) ~ 0.857*beta' is")
print("  MISLEADING as written. It could be interpreted as the exact")
print("  numerical value, but the actual delta is ~7x smaller.")
print()
print("  HOWEVER, it IS consistent if interpreted as:")
print("  'The leading-order SCALING of delta with theta goes as cos(theta),")
print("   so delta(theta=31) / delta(theta_ref) = cos(31) = 0.857.'")
print()
print("  The numerical values in Table 5.3 are correct and authoritative.")
print("  The Discussion Table should ideally read:")
print("    delta<AB> ~ 0.115*beta (numerical, at theta=31, mu=0.95)")
print("  or")
print("    delta<AB> = f(beta)*cos(theta), f depends on model parameters")
