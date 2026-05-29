# Supplemental S2: Derivation of Eq.(12) — K9_E Sensitivity Formula

## 1. f_perp values at polar angle theta

Superobserver basis at (theta, phi):

  |b=+1> = cos(theta/2)|H> + e^{i*phi} sin(theta/2)|V>
  |b=-1> = sin(theta/2)|H> - e^{i*phi} cos(theta/2)|V>

Squared overlaps with Friend z-basis (phi drops out):

  |<b=+1|H>|^2 = cos^2(theta/2)     |<b=+1|V>|^2 = sin^2(theta/2)
  |<b=-1|H>|^2 = sin^2(theta/2)     |<b=-1|V>|^2 = cos^2(theta/2)

f_perp(b,d) = 1 - |<b|d>|^2:

  f_perp(+1,H) = sin^2(theta/2)     f_perp(+1,V) = cos^2(theta/2)
  f_perp(-1,H) = cos^2(theta/2)     f_perp(-1,V) = sin^2(theta/2)

The key parameter: |f_perp(+1,H) - f_perp(-1,H)|/2 = |cos theta|/2.

At theta = 31 deg: |cos 31 deg|/2 = 0.8572/2 = 0.4286.

## 2. QM correlator for mixed setting (x=1, y=2)

Standard QM, singlet state, visibility mu = 0.95:

  <A1 B2>_QM = -mu * cos(theta_alice - theta_bob)

At modified Bong geometry: <A1 B2>_QM = -0.8572 (numerical, see Table 5.1).

## 3. K9_E-modified correlator

For the multiplicative model: P_K9E = P_QM * (1 - beta*f_perp)^(n_BSM) / Z
where n_BSM = number of BSM (non-z-basis) measurements in the setting pair.

For (1,2): Alice = z-basis (n=0), Bob = tilted (n=1) -> n_BSM = 1.

The K9_E correlator involves weighted sums over f_perp values. Performed
numerically in K9S12_proposal.py. Key result:

  <A1 B2>_K9E = <A1 B2>_QM * (1 - beta * |cos theta|/2)^(n_BSM)   [EXACT]

This holds because f_perp averaging over the singlet state yields exactly
|cos theta|/2 as the effective suppression coefficient per BSM operation.

## 4. First-order check

For n_BSM = 1: (1 - x)^1 = 1 - x (exact, no approximation).
For n_BSM = 2: (1 - x)^2 = 1 - 2x + x^2 -> second-order = x^2.

At beta=0.3, theta=31 deg: x = beta*|cos theta|/2 = 0.3*0.4286 = 0.1286.
n_BSM=1: exact.
n_BSM=2: second-order correction = 0.1286^2 = 0.0165 (~7% of 2x=0.2572).

## 5. Sensitivity

sigma per setting (N=91,000): sigma = sqrt((1 - <AB>^2)/N) = 0.0017.
Combined 4 mixed settings: sigma_eff = sigma/sqrt(4) = 0.00085.
5sigma detection: |delta| >= 0.00425.

n_BSM=1: |delta| = 0.8572 * beta * 0.4286 = 0.3675*beta.
beta_min(5sigma) = 0.00425/0.3675 = 0.0116 (per setting type).
Conservative (using 2 settings): beta_min = 0.034.
Operational: beta >= 0.05 at >5sigma.

## Code

Full computation: 07_fits/K9S12_proposal.py, function compute_k9e_correlators().
