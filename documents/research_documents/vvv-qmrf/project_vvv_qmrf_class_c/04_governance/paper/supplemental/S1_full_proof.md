# Supplemental S1: Full Proof of Equatorial Cancellation Theorem

## Theorem

Let Friend F measure in z-basis and Superobserver W at Bloch angles (theta, phi).
With f_perp(b,d) = 1 - |<b|d>|^2:
  f_perp(+1, H) - f_perp(-1, H) = -cos(theta)

Vanishes iff theta = pi/2. K9_E = 0 for all equatorial measurements.

## Proof

### Step 1: W's measurement basis

|b=+1> = cos(theta/2)|H> + e^(i*phi)*sin(theta/2)|V>
|b=-1> = sin(theta/2)|H> - e^(i*phi)*cos(theta/2)|V>

### Step 2: Overlaps with F's outcomes

|<b=+1|H>|^2 = cos^2(theta/2)     |<b=+1|V>|^2 = sin^2(theta/2)
|<b=-1|H>|^2 = sin^2(theta/2)     |<b=-1|V>|^2 = cos^2(theta/2)

phi drops out: |e^(i*phi)|^2 = 1. Overlaps depend ONLY on theta.

### Step 3: f_perp values

f_perp(+1,H) = 1 - cos^2(theta/2) = sin^2(theta/2)
f_perp(-1,H) = 1 - sin^2(theta/2) = cos^2(theta/2)
f_perp(+1,V) = 1 - sin^2(theta/2) = cos^2(theta/2)
f_perp(-1,V) = 1 - cos^2(theta/2) = sin^2(theta/2)

### Step 4: Outcome-dependence

f_perp(+1,H) - f_perp(-1,H) = sin^2(theta/2) - cos^2(theta/2) = -cos(theta)

### Step 5: Equatorial cancellation

-cos(theta) = 0 iff theta = pi/2. At theta = pi/2: all f_perp = 1/2.

### Step 6: K9_E reduction

When f_perp is outcome-independent:
  P(o|K) = Tr(E_o rho) * [1 - beta*constant] / [1 - beta*constant] = Tr(E_o rho)
K9_E = 0 for all equatorial measurements. QED.

## Sympy verification

```python
import sympy as sp
theta = sp.Symbol('theta', real=True)
assert sp.simplify(sp.sin(theta/2)**2 - sp.cos(theta/2)**2 + sp.cos(theta)) == 0
```
