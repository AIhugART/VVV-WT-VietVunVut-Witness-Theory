Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# VVV-QMRF Thought Experiment 1: Wigner's Friend as Registration-Layer Mapping

**Framework:** VietVunVut Quantum Measurement Registration Framework (VVV-QMRF)
**Phase:** Experimental Design Phase
**Status:** Initial Draft (v0.1)

## Legacy terminology cross-reference / Bảng đối chiếu thuật ngữ cũ

| Legacy term | Current VVV-QMRF term | Decision score | Reason |
|---|---|---:|---|
| VVV-EQM | VVV-QMRF | 5/5 | Current public name uses registration framing; legacy retained for traceability. |
| formal epistemic operators | registration-layer operators | 5/5 | The Wigner's Friend mapping concerns K-side registration, not a new physical collapse law. |
| Epistemic Space | K-side registration space | 5/5 | The current model separates physical `ρ` from registration state `K`. |
| Observer-as-Process | Registering-System-as-Process | 5/5 | Current E6 framework terminology avoids human-only observer framing. |
| `VVV_EQM_Wigners_Friend.md` | VVV-QMRF Wigner's Friend registration-layer mapping (legacy filename retained) | 4/5 | File name is not changed; document title and framework line use current VVV-QMRF naming. |
| observer (canonical Wigner's Friend role) | registering system when used in VVV-QMRF analysis | 4/5 | Keep `observer` only inside the classic thought experiment; use `registering system` for the framework layer. |
| subjective consciousness | local K-side registration status | 4/5 | The mapping avoids making collapse depend on human consciousness. |

## 1. The Wigner's Friend Paradox in Standard QM
In the classic "Wigner's Friend" thought experiment, an observer (the Friend) inside a sealed laboratory measures a quantum system in a superposition, such as a spin state:
$$ |\psi\rangle_S = \alpha|\uparrow\rangle + \beta|\downarrow\rangle $$

**The Friend's Perspective:** The Friend measures the spin. According to Postulate 3 (Collapse), the superposition breaks, and the Friend records a definite result (e.g., "up").
**Wigner's Perspective:** Wigner stands outside the sealed laboratory. Since Wigner has not interacted with the lab, he treats the entire lab (System + Friend) as a closed quantum system evolving unitarily according to Postulate 4. To Wigner, the lab is in a macroscopic superposition:
$$ |\Psi\rangle_W = \alpha|\uparrow\rangle_S |\text{saw up}\rangle_F + \beta|\downarrow\rangle_S |\text{saw down}\rangle_F $$

**The Paradox:** When does the collapse actually happen? Is it an objective physical event (which would mean Wigner is wrong to use unitary evolution), or is it only relative to the Friend's local perspective? Standard QM provides no registration-layer definition of the registering role to settle this.

---

## 2. Registration-Layer Mapping using VVV-QMRF

Using the registration-layer operators of VVV-QMRF, we can separate the physical description in $\mathcal{H}$ from the K-side registration state. Measurement is treated here not as a universal physical collapse law, but as localized registration certification.

### 2.1 The Friend's Measurement ($M_F$)
When the Friend interacts with the spin system, an interaction $I_F$ occurs.
1.  **E1 (Self-Certifying Registration):** The interaction triggers the intrinsic operator $\sigma(I_F) = 1$. The interaction is self-certifying as a measurement act $M_F$.
2.  **E3 (Registration Lock):** The operator $C(I_F)$ irreversibly fixes the physical correlation into the Friend's K-side registration space $\mathcal{K}_F$.
3.  **E2 (Registration Self-Completion):** The Friend immediately registers the result $r_F$ because $M_F \equiv^K r_F$.
4.  **E7 (Validity Location):** The validity of this measurement $V(M_F) = 1$ is local to $\mathcal{K}_F$. It requires no external certification from Wigner.

### 2.2 Wigner's Pre-Observation State
While standing outside, Wigner has not yet interacted with the system or the Friend.
1.  For Wigner, interaction $I_W = \emptyset$.
2.  Therefore, $\sigma(I_W) = 0$. No measurement act $M_W$ has occurred.
3.  Because no Registration Lock $C(I_W)$ has been made in Wigner's K-side registration space $\mathcal{K}_W$, Wigner may still represent the system + lab by the physical Hilbert-space model $|\Psi\rangle_W$.

### 2.3 Wigner Opens the Door ($M_W$)
When Wigner opens the door and asks the Friend for the result:
1.  Wigner makes a physical interaction $I_W$ with the Friend.
2.  **E1 (Self-Certifying Registration):** $\sigma(I_W) = 1$, creating Wigner's measurement act $M_W$.
3.  **E3 (Registration Lock):** Wigner applies $C(I_W)$ and obtains the classical information. At this point, Wigner's K-side registration state updates to a definite registered result.

---

## 3. Structural Conclusion

The apparent paradox arises from treating "wavefunction collapse" as an objective ontological event that is globally broadcast across the universe, rather than separating the physical model from local K-side registration.

VVV-QMRF Postulate **E6 (Registering-System-as-Process)** states that a registering system is not a substance, but a causal chain of measurement acts: $R = \{M_1, M_2, \dots\}$.
Because the Friend and Wigner are two distinct registering-system processes ($R_F \neq R_W$), their K-side registration spaces are distinct ($\mathcal{K}_F \neq \mathcal{K}_W$).

**Registration-layer resolution:**
There is no contradiction at the registration layer.
*   In $\mathcal{K}_F$, the result is registered at $t_1$ when $\sigma(I_F) = 1$.
*   In $\mathcal{K}_W$, the result is registered at $t_2$ when $\sigma(I_W) = 1$.

This is a K-side registration mapping, not a new physical collapse law. It reframes the location of registration validity and does not claim to solve the $\rho$-side physical superposition problem.
