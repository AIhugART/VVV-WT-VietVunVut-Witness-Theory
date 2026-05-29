# Quantum Nonlocality

In theoretical physics, quantum nonlocality refers to the phenomenon by which the measurement statistics of a multipartite quantum system do not allow an interpretation with local hidden variables. Quantum nonlocality has been experimentally verified under a variety of physical assumptions,[1][2][3][4][5] with a notable exception being the many-worlds interpretation which violates an assumption of Bell's theorem.[6][7]

Quantum nonlocality does not allow for faster-than-light communication,[8] and hence is compatible with special relativity and its universal speed limit of objects. Thus, quantum theory is local in the strict sense defined by special relativity and, as such, the term "quantum nonlocality" is sometimes considered a misnomer.[9] Still, it prompts many of the foundational discussions concerning quantum theory.[9]

## History

### Einstein, Podolsky and Rosen

In the 1935 EPR paper,[10] Albert Einstein, Boris Podolsky and Nathan Rosen described "two spatially separated particles which have both perfectly correlated positions and momenta"[11] as a direct consequence of quantum theory. They intended to use the classical principle of locality to challenge the idea that the quantum wavefunction was a complete description of reality, but instead they sparked a debate on the nature of reality.[12]

Afterwards, Einstein presented a variant of these ideas in a letter to Erwin Schrödinger,[13] which is the version that is presented here. The state and notation used here are more modern, and akin to David Bohm's take on EPR.[14] The quantum state of the two particles prior to measurement can be written as:

```math
|\psi_{AB}\rangle = \frac{1}{\sqrt{2}}\left(|0\rangle_A|1\rangle_B - |1\rangle_A|0\rangle_B\right) = \frac{1}{\sqrt{2}}\left(|-\rangle_A|+\rangle_B - |+\rangle_A|-\rangle_B\right)
```

where:

```math
|\pm\rangle = \frac{1}{\sqrt{2}}\left(|0\rangle \pm |1\rangle\right)
```

Here, subscripts "A" and "B" distinguish the two particles, though it is more convenient and usual to refer to these particles as being in the possession of two experimentalists called Alice and Bob. The rules of quantum theory give predictions for the outcomes of measurements performed by the experimentalists. Alice, for example, will measure her particle to be spin-up in an average of fifty percent of measurements.

However, according to textbook quantum mechanics, Alice's measurement causes the state of the two particles to collapse, so that if Alice performs a measurement of spin in the z-direction, that is with respect to the basis `{|0>, |1>}`, then Bob's system will be left in one of the states `|0>` or `|1>`. Likewise, if Alice performs a measurement of spin in the x-direction, that is, with respect to the basis `{|+>, |->}`, then Bob's system will be left in one of the states `|+>` or `|->`. Schrödinger referred to this phenomenon as "steering".[16]

This steering occurs in such a way that no signal can be sent by performing such a state update; quantum nonlocality cannot be used to send messages instantaneously and is therefore not in direct conflict with causality concerns in special relativity.[15]

In the orthodox view of this experiment, Alice's measurement, and particularly her measurement choice, has a direct effect on Bob's state. However, under the assumption of locality, actions on Alice's system do not affect the "true", or "ontic", state of Bob's system. The ontic state of Bob's system must be compatible with one of the quantum states `|0>` or `|1>`, since Alice can make a measurement that concludes with one of those states being the quantum description of his system. At the same time, it must also be compatible with one of the quantum states `|+>` or `|->` for the same reason. Therefore, the ontic state of Bob's system must be compatible with at least two quantum states; the quantum state is therefore not a complete descriptor of his system.

Einstein, Podolsky and Rosen saw this as evidence of the incompleteness of quantum theory, since the wavefunction is explicitly not a complete description of a quantum system under this assumption of locality. Their paper concludes:[10]

> While we have thus shown that the wave function does not provide a complete description of the physical reality, we left open the question of whether or not such a description exists. We believe, however, that such a theory is possible.

Although various authors, most notably Niels Bohr, criticised the ambiguous terminology of the EPR paper,[17][18] the thought experiment nevertheless generated a great deal of interest. Their notion of a "complete description" was later formalised by the suggestion of hidden variables that determine the statistics of measurement results, but to which an observer does not have access.[19]

Bohmian mechanics provides such a completion of quantum mechanics, with the introduction of hidden variables; however the theory is explicitly nonlocal.[20] The interpretation therefore does not give an answer to Einstein's question, which was whether or not a complete description of quantum mechanics could be given in terms of local hidden variables in keeping with the "Principle of Local Action".[21]

### Bell Inequality

In 1964 John Bell answered Einstein's question by showing that such local hidden variables can never reproduce the full range of statistical outcomes predicted by quantum theory.[22] Bell showed that a local hidden variable hypothesis leads to restrictions on the strength of correlations of measurement results. If the Bell inequalities are violated experimentally as predicted by quantum mechanics, then reality cannot be described by local hidden variables and the mystery of quantum nonlocal causation remains. However, Bell notes that the non-local hidden variable model of Bohm is different:[22]

> This [grossly nonlocal structure] is characteristic ... of any such theory which reproduces exactly the quantum mechanical predictions.

Clauser, Horne, Shimony and Holt (CHSH) reformulated these inequalities in a manner that was more conducive to experimental testing; see CHSH inequality.[23]

In the scenario proposed by Bell, a Bell scenario, two experimentalists, Alice and Bob, conduct experiments in separate labs. At each run, Alice conducts an experiment `x` in her lab, obtaining outcome `a`; Bob conducts an experiment `y` in his lab, obtaining outcome `b`. If Alice and Bob repeat their experiments several times, then they can estimate the probabilities:

```math
P(a,b|x,y)
```

namely, the probability that Alice and Bob respectively observe the results `a,b` when they respectively conduct the experiments `x,y`. In the following, each such set of probabilities will be denoted by just `P`. In the quantum nonlocality slang, `P` is termed a box.[24]

Bell formalized the idea of a hidden variable by introducing the parameter `λ` to locally characterize measurement results on each system:[22] "It is a matter of indifference ... whether λ denotes a single variable or a set ... and whether the variables are discrete or continuous". However, it is equivalent, and more intuitive, to think of `λ` as a local "strategy" or "message" that occurs with some probability when Alice and Bob reboot their experimental setup.

Bell's assumption of local causality then stipulates that each local strategy defines the distributions of independent outcomes if Alice conducts experiment `x` and Bob conducts experiment `y`:

```math
P(a,b|x,y,\lambda_A,\lambda_B) = P_A(a|x,\lambda_A)P_B(b|y,\lambda_B)
```

Here `P_A(a|x,λ_A)` denotes the probability that Alice obtains result `a` when she conducts experiment `x` and the local variable describing her experiment has value `λ_A`. Likewise, `P_B(b|y,λ_B)` denotes the probability that Bob obtains result `b` when he conducts experiment `y` and the local variable describing his experiment has value `λ_B`.

Suppose that `λ_A,λ_B` can take values from some set `Λ`. If each pair of values has an associated probability `ρ(λ_A,λ_B)` of being selected, shared randomness is allowed, then one can average over this distribution to obtain a formula for the joint probability of each measurement result:

```math
P(a,b|x,y) = \sum_{\lambda_A,\lambda_B \in \Lambda} \rho(\lambda_A,\lambda_B)P_A(a|x,\lambda_A)P_B(b|y,\lambda_B)
```

A box admitting such a decomposition is called a Bell local or a classical box. Fixing the number of possible values which `a,b,x,y` can each take, one can represent each box `P` as a finite vector with entries `P(a,b|x,y)`. In that representation, the set of all classical boxes forms a convex polytope.

In the Bell scenario studied by CHSH, where `a,b,x,y` can take values within `{0,1}`, any Bell local box `P` must satisfy the CHSH inequality:

```math
S_{CHSH}(P) \leq 2
```

where:

```math
S_{CHSH}(P) = E(0,0) + E(1,0) + E(0,1) - E(1,1)
```

and:

```math
E(x,y) = \sum_{a,b=0}^{1}(-1)^{a+b}P(a,b|x,y)
```

The above considerations apply to model a quantum experiment. Consider two parties conducting local polarization measurements on a bipartite photonic state. The measurement result for the polarization of a photon can take one of two values, informally, whether the photon is polarized in that direction, or in the orthogonal direction. If each party is allowed to choose between just two different polarization directions, the experiment fits within the CHSH scenario. As noted by CHSH, there exist a quantum state and polarization directions which generate a box `P` with:

```math
S_{CHSH}(P)=2\sqrt{2}
```

This demonstrates an explicit way in which a theory with ontological states that are local, with local measurements and only local actions cannot match the probabilistic predictions of quantum theory, disproving Einstein's hypothesis. Experimentalists such as Alain Aspect have verified the quantum violation of the CHSH inequality[1] as well as other formulations of Bell's inequality, to invalidate the local hidden variables hypothesis and confirm that reality is indeed nonlocal in the EPR sense.

### Possibilistic Nonlocality

Bell's demonstration is probabilistic in the sense that it shows that the precise probabilities predicted by quantum mechanics for some entangled scenarios cannot be met by a local hidden variable theory. For brevity, here and henceforth "local theory" means "local hidden variables theory". However, quantum mechanics permits an even stronger violation of local theories: a possibilistic one, in which local theories cannot even agree with quantum mechanics on which events are possible or impossible in an entangled scenario.

The first proof of this kind was due to Daniel Greenberger, Michael Horne, and Anton Zeilinger in 1993.[25] The state involved is often called the GHZ state.

In 1993, Lucien Hardy demonstrated a logical proof of quantum nonlocality that, like the GHZ proof, is a possibilistic proof.[26][27][28] It starts with the observation that the state `|ψ>` defined below can be written in a few suggestive ways:

```math
|\psi\rangle = \frac{1}{\sqrt{3}}\left(|00\rangle + |01\rangle + |10\rangle\right)
```

```math
|\psi\rangle = \frac{1}{\sqrt{3}}\left(\sqrt{2}|+0\rangle + \frac{1}{\sqrt{2}}|+1\rangle + \frac{1}{\sqrt{2}}|-1\rangle\right)
```

```math
|\psi\rangle = \frac{1}{\sqrt{3}}\left(\sqrt{2}|0+\rangle + \frac{1}{\sqrt{2}}|1+\rangle + \frac{1}{\sqrt{2}}|1-\rangle\right)
```

where, as above:

```math
|\pm\rangle = \frac{1}{\sqrt{2}}\left(|0\rangle \pm |1\rangle\right)
```

The experiment consists of this entangled state being shared between two experimenters, each of whom has the ability to measure either with respect to the basis `{|0>, |1>}` or `{|+>, |->}`. If they each measure with respect to `{|0>, |1>}`, then they never see the outcome `|11>`. If one measures with respect to `{|+>, |->}` and the other `{|0>, |1>}`, they never see the outcomes `|-0>` or `|0->`. However, sometimes they see the outcome `|-->` when measuring with respect to `{|+>, |->}`, since:

```math
\langle --|\psi\rangle = -\frac{1}{2\sqrt{3}} \neq 0
```

This leads to the paradox: having the outcome `|-->`, one concludes that if one of the experimenters had measured with respect to the `{|0>, |1>}` basis instead, the outcome must have been `|1>`, since `|-0>` and `|0->` are impossible. But then, if they had both measured with respect to the `{|0>, |1>}` basis, by locality the result must have been `|11>`, which is also impossible.

### Nonlocal Hidden Variable Models with a Finite Propagation Speed

The work of Bancal et al.[29] studies whether influences that propagate at a finite speed, possibly superluminal, can explain quantum correlations. In the case of a bipartite experiment, even if no signalling is allowed, the correlations can always be explained by a finite, but superluminal, hidden influence. In this scenario, any bipartite experiment revealing Bell nonlocality can just provide lower bounds on the hidden influence's propagation speed. However, certain experiments with three or more parties will either result in signalling, meaning the influences cannot be hidden anymore, or rule out all finite speed causal influences explaining quantum correlations.

### Analogs of Bell's Theorem in More Complicated Causal Structures

The random variables measured in a general experiment can depend on each other in complicated ways. In the field of causal inference, such dependencies are represented via Bayesian networks: directed acyclic graphs where each node represents a variable and an edge from a variable to another signifies that the former influences the latter and not otherwise.

In a standard bipartite Bell experiment, Alice's setting `x`, together with her local variable `λ_A`, influences her local outcome `a`. Bob's setting `y`, together with his local variable `λ_B`, influences his local outcome `b`. Bell's theorem can thus be interpreted as a separation between the quantum and classical predictions in a type of causal structure with just one hidden node `λ`.

Similar separations have been established in other types of causal structures.[30] The characterization of the boundaries for classical correlations in such extended Bell scenarios is challenging, but there exist complete practical computational methods to achieve it.[31][32]

## Entanglement and Nonlocality

Quantum nonlocality is sometimes understood as being equivalent to entanglement. However, this is not the case. Quantum entanglement can be defined only within the formalism of quantum mechanics, that is, it is a model-dependent property. In contrast, nonlocality refers to the impossibility of a description of observed statistics in terms of a local hidden variable model, so it is independent of the physical model used to describe the experiment.

It is true that for any pure entangled state there exists a choice of measurements that produce Bell nonlocal correlations, but the situation is more complex for mixed states. While any Bell nonlocal state must be entangled, there exist mixed entangled states which do not produce Bell nonlocal correlations[33], although, operating on several copies of some of such states,[34] or carrying out local post-selections,[35] it is possible to witness nonlocal effects.

Moreover, while there are catalysts for entanglement,[36] there are none for nonlocality.[37] Finally, reasonably simple examples of Bell inequalities have been found for which the quantum state giving the largest violation is never a maximally entangled state, showing that entanglement is, in some sense, not even proportional to nonlocality.[38][39][40]

## Quantum Correlations

As shown, the statistics achievable by two or more parties conducting experiments in a classical system are constrained in a non-trivial way. Analogously, the statistics achievable by separate observers in a quantum theory also happen to be restricted. The first derivation of a non-trivial statistical limit on the set of quantum correlations, due to B. Tsirelson,[41] is known as Tsirelson's bound. Consider the CHSH Bell scenario detailed before, but this time assume that, in their experiments, Alice and Bob are preparing and measuring quantum systems. In that case, the CHSH parameter can be shown to be bounded by:

```math
-2\sqrt{2} \leq S_{CHSH} \leq 2\sqrt{2}
```

### The Sets of Quantum Correlations and Tsirelson's Problem

Mathematically, a box `P` admits a quantum realization if and only if there exists a pair of Hilbert spaces `H_A,H_B`, a normalized vector `|ψ> ∈ H_A ⊗ H_B`, and projection operators `E_a^x, F_b^y` such that:

1. For all `x,y`, the sets `{E_a^x}_a` and `{F_b^y}_b` represent complete measurements. Namely:

```math
\sum_a E_a^x = I_A, \qquad \sum_b F_b^y = I_B
```

2. The box probabilities are given by:

```math
P(a,b|x,y)=\langle\psi|E_a^x\otimes F_b^y|\psi\rangle
```

In the following, the set of such boxes will be called `Q`. Contrary to the classical set of correlations, when viewed in probability space, `Q` is not a polytope. On the contrary, it contains both straight and curved boundaries.[42] In addition, `Q` is not closed:[43] this means that there exist boxes which can be arbitrarily well approximated by quantum systems but are themselves not quantum.

In the above definition, the space-like separation of the two parties conducting the Bell experiment was modeled by imposing that their associated operator algebras act on different factors `H_A,H_B` of the overall Hilbert space `H_A ⊗ H_B` describing the experiment. Alternatively, one could model space-like separation by imposing that these two algebras commute. This leads to a different definition: `P` admits a field quantum realization if and only if there exists a Hilbert space `H`, a normalized vector `|ψ>`, and projection operators `E_a^x,F_b^y` such that:

1. For all `x,y`, the sets `{E_a^x}_a` and `{F_b^y}_b` represent complete measurements. Namely:

```math
\sum_a E_a^x = I, \qquad \sum_b F_b^y = I
```

2. The box probabilities are given by:

```math
P(a,b|x,y)=\langle\psi|E_a^xF_b^y|\psi\rangle
```

3. Alice's and Bob's operators commute:

```math
[E_a^x,F_b^y]=0
```

Call `Q_c` the set of all such correlations. How does this new set relate to the more conventional `Q` defined above? It can be proven that `Q_c` is closed. Moreover:

```math
\overline{Q} \subseteq Q_c
```

where `\overline{Q}` denotes the closure of `Q`. Tsirelson's problem[44] consists in deciding whether the inclusion relation is strict, i.e., whether or not:

```math
\overline{Q}=Q_c
```

This problem only appears in infinite dimensions: when the Hilbert space `H` in the definition of `Q_c` is constrained to be finite-dimensional, the closure of the corresponding set equals `Q`.[44]

In January 2020, Ji, Natarajan, Vidick, Wright, and Yuen claimed a result in quantum complexity theory[45] that would imply that:

```math
\overline{Q} \neq Q_c
```

thus solving Tsirelson's problem.[46][47][48][49][50][51][52] Tsirelson's problem can be shown equivalent to Connes embedding problem,[53][54][55] a famous conjecture in the theory of operator algebras.

### Characterization of Quantum Correlations

Since the dimensions of `H_A,H_B` are, in principle, unbounded, determining whether a given box `P` admits a quantum realization is a complicated problem. In fact, the dual problem of establishing whether a quantum box can have a perfect score at a non-local game is known to be undecidable.[43] Moreover, the problem of deciding whether `P` can be approximated by a quantum system with precision `ε` is NP-hard.[56] Characterizing quantum boxes is equivalent to characterizing the cone of completely positive semidefinite matrices under a set of linear constraints.[57]

For small fixed dimensions `d_A,d_B`, one can explore, using variational methods, whether `P` can be realized in a bipartite quantum system `H_A ⊗ H_B`, with `dim(H_A)=d_A` and `dim(H_B)=d_B`. That method, however, can just be used to prove the realizability of `P`, and not its unrealizability with quantum systems.

To prove unrealizability, the most known method is the Navascués-Pironio-Acín (NPA) hierarchy.[58] This is an infinite decreasing sequence of sets of correlations:

```math
Q^1 \supseteq Q^2 \supseteq Q^3 \supseteq \cdots
```

with the properties:

1. If `P ∈ Q_c`, then `P ∈ Q^k` for all `k`.
2. If `P ∉ Q_c`, then there exists `k` such that `P ∉ Q^k`.
3. For any `k`, deciding whether `P ∈ Q^k` can be cast as a semidefinite program.

The NPA hierarchy thus provides a computational characterization, not of `Q`, but of `Q_c`. If `Q ≠ Q_c`, as claimed by Ji, Natarajan, Vidick, Wright, and Yuen, then a new method to detect the non-realizability of the correlations in `Q_c` is needed. If Tsirelson's problem was solved in the affirmative, namely `Q = Q_c`, then the above two methods would provide a practical characterization of `Q`.

### The Physics of Supra-Quantum Correlations

The works listed above describe what the quantum set of correlations looks like, but they do not explain why. Are quantum correlations unavoidable, even in post-quantum physical theories, or on the contrary, could there exist correlations outside `Q` which nonetheless do not lead to any unphysical operational behavior?

In their seminal 1994 paper, Popescu and Rohrlich explore whether quantum correlations can be explained by appealing to relativistic causality alone.[59] Namely, whether any hypothetical box `P` outside `Q` would allow building a device capable of transmitting information faster than the speed of light. At the level of correlations between two parties, Einstein's causality translates in the requirement that Alice's measurement choice should not affect Bob's statistics, and vice versa. Otherwise, Alice or Bob could signal the other instantaneously by choosing her or his measurement setting appropriately. Mathematically, Popescu and Rohrlich's no-signalling conditions are:

```math
\sum_a P(a,b|x,y)=\sum_a P(a,b|x',y) := P_B(b|y)
```

```math
\sum_b P(a,b|x,y)=\sum_b P(a,b|x,y') := P_A(a|x)
```

Like the set of classical boxes, when represented in probability space, the set of no-signalling boxes forms a polytope. Popescu and Rohrlich identified a box `P` that, while complying with the no-signalling conditions, violates Tsirelson's bound, and is thus unrealizable in quantum physics. Dubbed the PR-box, it can be written as:

```math
P(a,b|x,y)=\frac{1}{2}\delta_{xy,a\oplus b}
```

Here `a,b,x,y` take values in `{0,1}`, and `⊕` denotes the sum modulo two. It can be verified that the CHSH value of this box is 4, as opposed to the Tsirelson bound of `2√2`. This box had been identified earlier, by Rastall[60] and Khalfin and Tsirelson.[61]

In view of this mismatch, Popescu and Rohrlich pose the problem of identifying a physical principle, stronger than the no-signalling conditions, that allows deriving the set of quantum correlations. Several proposals followed:

1. **Non-trivial communication complexity (NTCC).[62]** This principle stipulates that nonlocal correlations should not be so strong as to allow two parties to solve all one-way communication problems with some probability `p > 1/2` using just one bit of communication. It can be proven that any box violating Tsirelson's bound by more than `4√(2/3)` is incompatible with NTCC.
2. **No Advantage for Nonlocal Computation (NANLC).[63]** The following scenario is considered: given a function `f`, two parties are distributed the strings of `n` bits `x,y` and asked to output the bits `a,b` so that `a ⊕ b` is a good guess for `f(x,y)`. The principle of NANLC states that non-local boxes should not give the two parties any advantage to play this game. It is proven that any box violating Tsirelson's bound would provide such an advantage.
3. **Information Causality (IC).[64]** The starting point is a bipartite communication scenario where one of the parts, Alice, is handed a random string `x` of `n` bits. The second part, Bob, receives a random number `k`. Their goal is to transmit Bob the bit `x_k`, for which purpose Alice is allowed to transmit Bob `m` bits. The principle of IC states that the sum over `k` of the mutual information between Alice's bit and Bob's guess cannot exceed the number `m` of bits transmitted by Alice. It is shown that any box violating Tsirelson's bound would allow two parties to violate IC.
4. **Macroscopic Locality (ML).[65]** In the considered setup, two separate parties conduct extensive low-resolution measurements over a large number of independently prepared pairs of correlated particles. ML states that any such "macroscopic" experiment must admit a local hidden variable model. It is proven that any microscopic experiment capable of violating Tsirelson's bound would also violate standard Bell nonlocality when brought to the macroscopic scale. Besides Tsirelson's bound, the principle of ML fully recovers the set of all two-point quantum correlators.
5. **Local Orthogonality (LO).[66]** This principle applies to multipartite Bell scenarios, where `n` parties respectively conduct experiments `x_1,...,x_n` in their local labs. They respectively obtain the outcomes `a_1,...,a_n`. The pair of vectors `(a|x)` is called an event. Two events `(a|x)` and `(a'|x')` are said to be locally orthogonal if there exists `i` such that `x_i=x'_i` and `a_i≠a'_i`. The principle of LO states that, for any multipartite box, the sum of the probabilities of any set of pair-wise locally orthogonal events cannot exceed 1. It is proven that any bipartite box violating Tsirelson's bound by an amount of `0.052` violates LO.

All these principles can be experimentally falsified under the assumption that we can decide if two or more events are space-like separated. This sets this research program aside from the axiomatic reconstruction of quantum mechanics via Generalized Probabilistic Theories.

The works above rely on the implicit assumption that any physical set of correlations must be closed under wirings.[67] This means that any effective box built by combining the inputs and outputs of a number of boxes within the considered set must also belong to the set. Closure under wirings does not seem to enforce any limit on the maximum value of CHSH. However, it is not a void principle: on the contrary, in [67] it is shown that many simple, intuitive families of sets of correlations in probability space happen to violate it.

Originally, it was unknown whether any of these principles, or a subset thereof, was strong enough to derive all the constraints defining `Q`. This state of affairs continued for some years until the construction of the almost quantum set `\tilde{Q}`.[68] `\tilde{Q}` is a set of correlations that is closed under wirings and can be characterized via semidefinite programming. It contains all correlations in `Q`, but also some non-quantum boxes. Remarkably, all boxes within the almost quantum set are shown to be compatible with the principles of NTCC, NANLC, ML and LO. There is also numerical evidence that almost-quantum boxes also comply with IC. It seems, therefore, that, even when the above principles are taken together, they do not suffice to single out the quantum set in the simplest Bell scenario of two parties, two inputs and two outputs.[68]

## Device Independent Protocols

Nonlocality can be exploited to conduct quantum information tasks which do not rely on the knowledge of the inner workings of the prepare-and-measurement apparatuses involved in the experiment. The security or reliability of any such protocol just depends on the strength of the experimentally measured correlations `P`. These protocols are termed device-independent.

### Device-Independent Quantum Key Distribution

The first device-independent protocol proposed was device-independent quantum key distribution (QKD).[69] In this primitive, two distant parties, Alice and Bob, are distributed an entangled quantum state, that they probe, thus obtaining the statistics `P`. Based on how non-local the box `P` happens to be, Alice and Bob estimate how much knowledge an external quantum adversary Eve, the eavesdropper, could possess on the value of Alice and Bob's outputs. This estimation allows them to devise a reconciliation protocol at the end of which Alice and Bob share a perfectly correlated one-time pad of which Eve has no information whatsoever. The one-time pad can then be used to transmit a secret message through a public channel. Although the first security analyses on device-independent QKD relied on Eve carrying out a specific family of attacks,[70] all such protocols have been recently proven unconditionally secure.[71]

### Device-Independent Randomness Certification, Expansion and Amplification

Nonlocality can be used to certify that the outcomes of one of the parties in a Bell experiment are partially unknown to an external adversary. By feeding a partially random seed to several non-local boxes, and, after processing the outputs, one can end up with a longer, potentially unbounded, string of comparable randomness[72] or with a shorter but more random string.[73] This last primitive can be proven impossible in a classical setting.[74]

Device-independent (DI) randomness certification, expansion, and amplification are techniques used to generate high-quality random numbers that are secure against any potential attacks on the underlying devices used to generate random numbers. These techniques have critical applications in cryptography, where high-quality random numbers are essential for ensuring the security of cryptographic protocols.

Randomness certification is the process of verifying that the output of a random number generator is truly random and has not been tampered with by an adversary. DI randomness certification does this verification without making assumptions about the underlying devices that generate random numbers. Instead, randomness is certified by observing correlations between the outputs of different devices that are generated using the same physical process. Recent research has demonstrated the feasibility of DI randomness certification using entangled quantum systems, such as photons or electrons.

Randomness expansion is taking a small amount of initial random seed and expanding it into a much larger sequence of random numbers. In DI randomness expansion, the expansion is done using measurements of quantum systems that are prepared in a highly entangled state. The security of the expansion is guaranteed by the laws of quantum mechanics, which make it impossible for an adversary to predict the expansion output. Recent research has shown that DI randomness expansion can be achieved using entangled photon pairs and measurement devices that violate a Bell inequality.[75]

Randomness amplification is the process of taking a small amount of initial random seed and increasing its randomness by using a cryptographic algorithm. In DI randomness amplification, this process is done using entanglement properties and quantum mechanics. The security of the amplification is guaranteed by the fact that any attempt by an adversary to manipulate the algorithm's output will inevitably introduce errors that can be detected and corrected. Recent research has demonstrated the feasibility of DI randomness amplification using quantum entanglement and the violation of a Bell inequality.[76]

DI randomness certification, expansion, and amplification are powerful techniques for generating high-quality random numbers that are secure against any potential attacks on the underlying devices used to generate random numbers. These techniques have critical applications in cryptography and are likely to become increasingly crucial as quantum computing technology advances. In addition, a milder approach called semi-DI exists where random numbers can be generated with some assumptions on the working principle of the devices, environment, dimension, energy, etc., in which it benefits from ease-of-implementation and high generation rate.[77]

### Self-Testing

Sometimes, the box `P` shared by Alice and Bob is such that it only admits a unique quantum realization. This means that there exist measurement operators and a quantum state giving rise to `P` such that any other physical realization of `P` is connected to it via local unitary transformations. This phenomenon, that can be interpreted as an instance of device-independent quantum tomography, was first pointed out by Tsirelson[42] and named self-testing by Mayers and Yao.[69]

Self-testing is known to be robust against systematic noise, i.e., if the experimentally measured statistics are close enough to `P`, one can still determine the underlying state and measurement operators up to error bars.[69]

### Dimension Witnesses

The degree of non-locality of a quantum box `P` can also provide lower bounds on the Hilbert space dimension of the local systems accessible to Alice and Bob.[78] This problem is equivalent to deciding the existence of a matrix with low completely positive semidefinite rank.[79] Finding lower bounds on the Hilbert space dimension based on statistics happens to be a hard task, and current general methods only provide very low estimates.[80] However, a Bell scenario with five inputs and three outputs suffices to provide arbitrarily high lower bounds on the underlying Hilbert space dimension.[81]

Quantum communication protocols which assume a knowledge of the local dimension of Alice and Bob's systems, but otherwise do not make claims on the mathematical description of the preparation and measuring devices involved are termed semi-device independent protocols. Currently, there exist semi-device independent protocols for quantum key distribution[82] and randomness expansion.[83]

## See Also

- Action at a distance
- Buscemi nonlocality
- Popper's experiment
- Quantum pseudo-telepathy
- Quantum contextuality
- Quantum foundations

## References

1. Aspect, Alain; Dalibard, Jean; Roger, Gérard (1982-12-20). "Experimental Test of Bell's Inequalities Using Time-Varying Analyzers". *Physical Review Letters*. 49 (25): 1804-1807. Bibcode:1982PhRvL..49.1804A. doi:10.1103/PhysRevLett.49.1804.
2. Rowe MA, et al. (February 2001). "Experimental violation of a Bell's Inequality with efficient detection". *Nature*. 409 (6822): 791-794. Bibcode:2001Natur.409..791R. doi:10.1038/35057215. hdl:2027.42/62731. PMID 11236986. S2CID 205014115.
3. Hensen, B, et al. (October 2015). "Loophole-free Bell inequality violation using electron spins separated by 1.3 kilometres". *Nature*. 526 (7575): 682-686. arXiv:1508.05949. Bibcode:2015Natur.526..682H. doi:10.1038/nature15759. PMID 26503041. S2CID 205246446.
4. Giustina, M, et al. (December 2015). "Significant-Loophole-Free Test of Bell's Theorem with Entangled Photons". *Physical Review Letters*. 115 (25) 250401. arXiv:1511.03190. Bibcode:2015PhRvL.115y0401G. doi:10.1103/PhysRevLett.115.250401. PMID 26722905. S2CID 13789503.
5. Shalm, LK, et al. (December 2015). "Strong Loophole-Free Test of Local Realism". *Physical Review Letters*. 115 (25) 250402. arXiv:1511.03189. Bibcode:2015PhRvL.115y0402S. doi:10.1103/PhysRevLett.115.250402. PMC 5815856. PMID 26722906.
6. Bell, Mary; Gao, Shan, eds. (2016). *Quantum nonlocality and reality: 50 years of Bell's theorem*. Cambridge: Cambridge University Press. ISBN 978-1-316-21939-3.
7. Deutsch, David; Hayden, Patrick (1999-06-04), "Information flow in entangled quantum systems", *Proceedings of the Royal Society of London. Series A: Mathematical, Physical and Engineering Sciences*, 456 (1999): 1759-1774, arXiv:quant-ph/9906007, doi:10.1098/rspa.2000.0585.
8. Ghirardi, G.C.; Rimini, A.; Weber, T. (March 1980). "A general argument against superluminal transmission through the quantum mechanical measurement process". *Lettere al Nuovo Cimento*. 27 (10): 293-298. doi:10.1007/BF02817189. S2CID 121145494.
9. Chang, Lay Nam; Lewis, Zachary; Minic, Djordje; Takeuchi, Tatsu; Tze, Chia-Hsiung (2011). "Bell's Inequalities, Superquantum Correlations, and String Theory". *Advances in High Energy Physics*. 2011: 1-11. arXiv:1104.3359. doi:10.1155/2011/593423. hdl:10919/48902. ISSN 1687-7357.
10. Einstein, A.; Podolsky, B.; Rosen, N. (1935-05-15). "Can Quantum-Mechanical Description of Physical Reality Be Considered Complete?" *Physical Review*. 47 (10): 777-780. Bibcode:1935PhRv...47..777E. doi:10.1103/PhysRev.47.777. ISSN 0031-899X.
11. Reid, M. D.; Drummond, P. D.; Bowen, W. P.; Cavalcanti, E. G.; Lam, P. K.; Bachor, H. A.; Andersen, U. L.; Leuchs, G. (2009-12-10). "Colloquium: The Einstein-Podolsky-Rosen paradox: From concepts to applications". *Reviews of Modern Physics*. 81 (4): 1727-1751. arXiv:0806.0270. Bibcode:2009RvMP...81.1727R. doi:10.1103/RevModPhys.81.1727. hdl:10072/37941. ISSN 0034-6861.
12. Clauser, John F.; Shimony, Abner. "Bell's theorem. Experimental tests and implications." *Reports on Progress in Physics*. 41.12 (1978): 1881.
13. Einstein, Albert. "Letter to E. Schrödinger" [Letter]. Einstein Archives, ID: Call Number 22-47. Hebrew University of Jerusalem.
14. Jevtic, S.; Rudolph, T. (2015). "How Einstein and/or Schrödinger should have discovered Bell's theorem in 1936". *Journal of the Optical Society of America B*. 32 (4): 50-55. arXiv:1411.4387. Bibcode:2015JOSAB..32A..50J. doi:10.1364/JOSAB.32.000A50. S2CID 55579565.
15. Nielsen, Michael A.; Chuang, Isaac L. (2000). *Quantum Computation and Quantum Information*. Cambridge University Press. pp. 112-113. ISBN 978-0-521-63503-5.
16. Wiseman, H.M.; Jones, S.J.; Doherty, A.C. (April 2007). "Steering, Entanglement, Nonlocality, and the Einstein-Podolsky-Rosen Paradox". *Physical Review Letters*. 98 (14) 140402. arXiv:quant-ph/0612147. Bibcode:2007PhRvL..98n0402W. doi:10.1103/physrevlett.98.140402. PMID 17501251. S2CID 30078867.
17. Bohr, N. (July 1935). "Can Quantum-Mechanical Description of Physical Reality Be Considered Complete?" *Physical Review*. 48 (8): 696-702. Bibcode:1935PhRv...48..696B. doi:10.1103/PhysRev.48.696.
18. Furry, W.H. (March 1936). "Remarks on Measurements in Quantum Theory". *Physical Review*. 49 (6): 476. Bibcode:1936PhRv...49..476F. doi:10.1103/PhysRev.49.476.
19. von Neumann, J. (1932/1955). In *Mathematische Grundlagen der Quantenmechanik*, Springer, Berlin, translated into English by Beyer, R.T., Princeton University Press, Princeton, cited by Baggott, J. (2004), *Beyond Measure: Modern physics, philosophy, and the meaning of quantum theory*, Oxford University Press, Oxford, ISBN 0-19-852927-9, pages 144-145.
20. Maudlin, Tim (2011). *Quantum Non-Locality and Relativity: Metaphysical Intimations of Modern Physics* (3rd ed.). John Wiley & Sons. p. 111. ISBN 978-1-4443-3126-4.
21. Fine, Arthur (Winter 2017). "The Einstein-Podolsky-Rosen Argument in Quantum Theory". In Zalta, Edward N. (ed.). *The Stanford Encyclopedia of Philosophy*. Metaphysics Research Lab, Stanford University. Retrieved 6 December 2018.
22. Bell, John (1964). "On the Einstein Podolsky Rosen paradox". *Physics Physique Физика*. 1 (3): 195-200. Bibcode:1964PhyNY...1..195B. doi:10.1103/PhysicsPhysiqueFizika.1.195.
23. Clauser, John F.; Horne, Michael A.; Shimony, Abner; Holt, Richard A. (October 1969). "Proposed Experiment to Test Local Hidden-Variable Theories". *Physical Review Letters*. 23 (15): 880-884. Bibcode:1969PhRvL..23..880C. doi:10.1103/PhysRevLett.23.880. S2CID 18467053.
24. Barrett, J.; Linden, N.; Massar, S.; Pironio, S.; Popescu, S.; Roberts, D. (2005). "Non-local correlations as an information theoretic resource". *Physical Review A*. 71 (2) 022101. arXiv:quant-ph/0404097. Bibcode:2005PhRvA..71b2101B. doi:10.1103/PhysRevA.71.022101. S2CID 13373771.
25. Greenberger, Daniel M.; Horne, Michael A.; Zeilinger, Anton (2007). *Going beyond Bell's Theorem*. arXiv:0712.0921. Bibcode:2007arXiv0712.0921G.
26. Hardy, Lucien (1993). "Nonlocality for two particles without inequalities for almost all entangled states". *Physical Review Letters*. 71 (11): 1665-1668. Bibcode:1993PhRvL..71.1665H. doi:10.1103/PhysRevLett.71.1665. PMID 10054467. S2CID 11839894.
27. Braun, D.; Choi, M.-S. (2008). "Hardy's test versus the Clauser-Horne-Shimony-Holt test of quantum nonlocality: Fundamental and practical aspects". *Physical Review A*. 78 (3) 032114. arXiv:0808.0052. Bibcode:2008PhRvA..78c2114B. doi:10.1103/physreva.78.032114. S2CID 119267461.
28. Nikolić, Hrvoje (2007). "Quantum Mechanics: Myths and Facts". *Foundations of Physics*. 37 (11): 1563-1611. arXiv:quant-ph/0609163. Bibcode:2007FoPh...37.1563N. doi:10.1007/s10701-007-9176-y. S2CID 9613836.
29. Bancal, Jean-Daniel; Pironio, Stefano; Acin, Antonio; Liang, Yeong-Cherng; Scarani, Valerio; Gisin, Nicolas (2012). "Quantum nonlocality based on finite-speed causal influences leads to superluminal signaling". *Nature Physics*. 8 (867): 867-870. arXiv:1110.3795. Bibcode:2012NatPh...8..867B. doi:10.1038/nphys2460. S2CID 13922531.
30. Fritz, Tobias (2012). "Beyond Bell's Theorem: Correlation Scenarios". *New Journal of Physics*. 14 (10) 103001. arXiv:1206.5115. Bibcode:2012NJPh...14j3001F. doi:10.1088/1367-2630/14/10/103001. S2CID 4847110.
31. Wolfe, Elie; Spekkens, R. W.; Fritz, T. (2019). "The Inflation Technique for Causal Inference with Latent Variables". *Causal Inference*. 7 (2) 20170020. arXiv:1609.00672. doi:10.1515/jci-2017-0020. S2CID 52476882.
32. Navascués, Miguel; Wolfe, Elie (2020). "The Inflation Technique Completely Solves the Causal Compatibility Problem". *Journal of Causal Inference*. 8: 70-91. arXiv:1707.06476. doi:10.1515/jci-2018-0008. S2CID 155100141.
33. Werner, R.F. (1989). "Quantum States with Einstein-Podolsky-Rosen correlations admitting a hidden-variable model". *Physical Review A*. 40 (8): 4277-4281. Bibcode:1989PhRvA..40.4277W. doi:10.1103/PhysRevA.40.4277. PMID 9902666.
34. Palazuelos, Carlos (2012). "Super-activation of quantum non-locality". *Physical Review Letters*. 109 (19) 190401. arXiv:1205.3118. Bibcode:2012PhRvL.109s0401P. doi:10.1103/PhysRevLett.109.190401. PMID 23215363. S2CID 4613963.
35. Popescu, Sandu (1995). "Bell's Inequalities and Density Matrices: Revealing 'Hidden' Nonlocality". *Physical Review Letters*. 74 (14): 2619-2622. arXiv:quant-ph/9502005. Bibcode:1995PhRvL..74.2619P. doi:10.1103/PhysRevLett.74.2619. PMID 10057976. S2CID 35478562.
36. Jonathan, Daniel; Plenio, Martin B. (1999-10-25). "Entanglement-Assisted Local Manipulation of Pure Quantum States". *Physical Review Letters*. 83 (17): 3566-3569. arXiv:quant-ph/9905071. Bibcode:1999PhRvL..83.3566J. doi:10.1103/PhysRevLett.83.3566. hdl:10044/1/245. ISSN 0031-9007. S2CID 392419.
37. Karvonen, Martti (2021-10-13). "Neither Contextuality nor Nonlocality Admits Catalysts". *Physical Review Letters*. 127 (16) 160402. arXiv:2102.07637. Bibcode:2021PhRvL.127p0402K. doi:10.1103/PhysRevLett.127.160402. ISSN 0031-9007. PMID 34723585. S2CID 231924967.
38. Junge, Marius; Palazuelos, C. (2011). "Large violation of Bell inequalities with low entanglement". *Communications in Mathematical Physics*. 306 (3): 695-746. arXiv:1007.3043. Bibcode:2011CMaPh.306..695J. doi:10.1007/s00220-011-1296-8. S2CID 673737.
39. Vidick, Thomas; Wehner, Stephanie (2011). "More Non-locality with less Entanglement". *Physical Review A*. 83 (5) 052310. arXiv:1011.5206. Bibcode:2011PhRvA..83e2310V. doi:10.1103/PhysRevA.83.052310. S2CID 6589783.
40. Liang, Yeong-Cherng; Vértesi, Tamás; Brunner, Nicolas (2010). "Semi-device-independent bounds on entanglement". *Physical Review A*. 83 (2) 022108. arXiv:1012.1513. Bibcode:2011PhRvA..83b2108L. doi:10.1103/PhysRevA.83.022108. S2CID 73571969.
41. Cirel'son, B.S. (1980). "Quantum generalizations of Bell's inequality". *Letters in Mathematical Physics*. 4 (2): 93-100. Bibcode:1980LMaPh...4...93C. doi:10.1007/bf00417500. S2CID 120680226.
42. Tsirel'son, B.S. (1987). "Quantum analogues of the Bell inequalities. The case of two spatially separated domains". *Journal of Soviet Mathematics*. 36 (4): 557-570. doi:10.1007/BF01663472. S2CID 119363229.
43. Slofstra, William (2017). "The set of quantum correlations is not closed". arXiv:1703.08618 [quant-ph].
44. "Bell inequalities and operator algebras". *Open quantum problems*. Archived from the original on 2019-12-06. Retrieved 2019-12-05.
45. Ji, Zhengfeng; Natarajan, Anand; Vidick, Thomas; Wright, John; Yuen, Henry (2020). "MIP*=RE". arXiv:2001.04383 [quant-ph].
46. Castelvecchi, Davide (2020). "How 'spooky' is quantum physics? The answer could be incalculable". *Nature*. 577 (7791): 461-462. Bibcode:2020Natur.577..461C. doi:10.1038/d41586-020-00120-6. PMID 31965099.
47. Kalai, Gil (2020-01-17). "Amazing: Zhengfeng Ji, Anand Natarajan, Thomas Vidick, John Wright, and Henry Yuen proved that MIP* = RE and thus disproved Connes 1976 Embedding Conjecture, and provided a negative answer to Tsirelson's problem". *Combinatorics and More*. Retrieved 2020-03-06.
48. Barak, Boaz (2020-01-14). "MIP*=RE, disproving Connes embedding conjecture". *Windows On Theory*. Retrieved 2020-03-06.
49. Aaronson, Scott (16 January 2020). "MIP*=RE". *Shtetl-Optimized*. Retrieved 2020-03-06.
50. Regan, Kenneth W. (2020-01-15). "Halting Is Poly-Time Quantum Provable". *Gödel's Lost Letter and P=NP*. Retrieved 2020-03-06.
51. Vidick, Thomas (2020-01-14). "A Masters project". *MyCQstate*. Retrieved 2020-03-06.
52. Hartnett, Kevin (4 March 2020). "Landmark Computer Science Proof Cascades Through Physics and Math". *Quanta Magazine*. Retrieved 2020-03-09.
53. Junge, M.; Navascués, M.; Palazuelos, C.; Pérez-García, D.; Scholz, V.B.; Werner, R.F. (2011). "Connes' embedding problem and Tsirelson's problem". *Journal of Mathematical Physics*. 52 (1): 012102. arXiv:1008.1142. Bibcode:2011JMP....52a2102J. doi:10.1063/1.3514538. S2CID 12321570.
54. Fritz, Tobias (2012). "Tsirelson's problem and Kirchberg's conjecture". *Reviews in Mathematical Physics*. 24 (5): 1250012. arXiv:1008.1168. Bibcode:2012RvMaP..2450012F. doi:10.1142/S0129055X12500122. S2CID 17162262.
55. Ozawa, Narutaka (2013). "About the Connes Embedding Conjecture---Algebraic approaches---". *Japanese Journal of Mathematics*. 8: 147-183. doi:10.1007/s11537-013-1280-5. hdl:2433/173118. S2CID 121154563.
56. Ito, T.; Kobayashi, H.; Matsumoto, K. (2008). "Oracularization and two-prover one-round interactive proofs against nonlocal strategies". arXiv:0810.0693 [quant-ph].
57. Sikora, Jamie; Varvitsiotis, Antonios (2017). "Linear conic formulations for two-party correlations and values of nonlocal games". *Mathematical Programming*. 162 (1-2): 431-463. arXiv:1506.07297. doi:10.1007/s10107-016-1049-8. S2CID 8234910.
58. Navascués, Miguel; Pironio, S.; Acín, A. (2007). "Bounding the Set of Quantum Correlations". *Physical Review Letters*. 98 (1) 010401. arXiv:quant-ph/0607119. Bibcode:2007PhRvL..98a0401N. doi:10.1103/physrevlett.98.010401. PMID 17358458. S2CID 41742170.
59. Popescu, Sandu; Rohrlich, Daniel (1994). "Nonlocality as an axiom". *Foundations of Physics*. 24 (3): 379-385. Bibcode:1994FoPh...24..379P. CiteSeerX 10.1.1.508.4193. doi:10.1007/BF02058098. S2CID 120333148.
60. Rastall, Peter (1985). "Locality, Bell's theorem, and quantum mechanics". *Foundations of Physics*. 15 (9): 963-972. Bibcode:1985FoPh...15..963R. doi:10.1007/bf00739036. S2CID 122298281.
61. Khalfin, L.A.; Tsirelson, B.S. (1985). Lahti; et al. (eds.). "Quantum and quasi-classical analogs of Bell inequalities". *Symposium on the Foundations of Modern Physics*. World Scientific Publishing. pp. 441-460.
62. Brassard, G.; Buhrman, H.; Linden, N.; Methot, A.A.; Tapp, A.; Unger, F. (2006). "Limit on Nonlocality in Any World in Which Communication Complexity Is Not Trivial". *Physical Review Letters*. 96 (25) 250401. arXiv:quant-ph/0508042. Bibcode:2006PhRvL..96y0401B. doi:10.1103/PhysRevLett.96.250401. PMID 16907289. S2CID 6135971.
63. Linden, N.; Popescu, S.; Short, A. J.; Winter, A. (2007). "Quantum Nonlocality and Beyond: Limits from Nonlocal Computation". *Physical Review Letters*. 99 (18) 180502. arXiv:quant-ph/0610097. Bibcode:2007PhRvL..99r0502L. doi:10.1103/PhysRevLett.99.180502. PMID 17995388.
64. Pawlowski, M.; Paterek, T.; Kaszlikowski, D.; Scarani, V.; Winter, A.; Zukowski, M. (October 2009). "Information Causality as a Physical Principle". *Nature*. 461 (7267): 1101-1104. arXiv:0905.2292. Bibcode:2009Natur.461.1101P. doi:10.1038/nature08400. PMID 19847260. S2CID 4428663.
65. Navascués, M.; Wunderlich, H. (2009). "A Glance Beyond the Quantum Model". *Proceedings of the Royal Society A*. 466 (2115): 881-890. arXiv:0907.0372. doi:10.1098/rspa.2009.0453.
66. Fritz, T.; Sainz, A. B.; Augusiak, R.; Brask, J. B.; Chaves, R.; Leverrier, A.; Acín, A. (2013). "Local orthogonality as a multipartite principle for quantum correlations". *Nature Communications*. 4 2263. arXiv:1210.3018. Bibcode:2013NatCo...4.2263F. doi:10.1038/ncomms3263. PMID 23948952. S2CID 14759956.
67. Allcock, Jonathan; Brunner, Nicolas; Linden, Noah; Popescu, Sandu; Skrzypczyk, Paul; Vértesi, Tamás (2009). "Closed sets of non-local correlations". *Physical Review A*. 80 (6) 062107. arXiv:0908.1496. Bibcode:2009PhRvA..80f2107A. doi:10.1103/PhysRevA.80.062107. S2CID 118677048.
68. Navascués, M.; Guryanova, Y.; Hoban, M. J.; Acín, A. (2015). "Almost Quantum Correlations". *Nature Communications*. 6 6288. arXiv:1403.4621. Bibcode:2015NatCo...6.6288N. doi:10.1038/ncomms7288. PMID 25697645. S2CID 12810715.
69. Mayers, Dominic; Yao, Andrew C.-C. (1998). *Quantum Cryptography with Imperfect Apparatus*. IEEE Symposium on Foundations of Computer Science (FOCS).
70. Acín, Antonio; Gisin, Nicolas; Masanes, Lluis (2006). "From Bell's Theorem to Secure Quantum Key Distribution". *Physical Review Letters*. 97 (12) 120405. arXiv:quant-ph/0510094. Bibcode:2006PhRvL..97l0405A. doi:10.1103/PhysRevLett.97.120405. PMID 17025944. S2CID 3315286.
71. Vazirani, Umesh; Vidick, Thomas (2014). "Fully Device-Independent Quantum Key Distribution". *Physical Review Letters*. 113 (14) 140501. arXiv:1210.1810. Bibcode:2014PhRvL.113n0501V. doi:10.1103/physrevlett.113.140501. PMID 25325625. S2CID 119299119.
72. Colbeck, Roger (December 2006). Chapter 5. *Quantum And Relativistic Protocols For Secure Multi-Party Computation* (Thesis), University of Cambridge. arXiv:0911.3814.
73. Colbeck, Roger; Renner, Renato (2012). "Free randomness can be amplified". *Nature Physics*. 8 (6): 450-453. arXiv:1105.3195. Bibcode:2012NatPh...8..450C. doi:10.1038/nphys2300. S2CID 118309394.
74. Santha, Miklos; Vazirani, Umesh V. (1984-10-24). *Generating quasi-random sequences from slightly-random sources*. Proceedings of the 25th IEEE Symposium on Foundations of Computer Science. University of California. pp. 434-440.
75. Colbeck, R.; Kent, A. (2011). "Private randomness expansion with untrusted devices". *Journal of Physics A: Mathematical and Theoretical*. 44(9), 095305. doi:10.1088/1751-8113/44/9/095305.
76. Pironio, S, et al. (2010). "Random numbers certified by Bell's theorem". *Nature*. 464 (7291): 1021-1024. arXiv:0911.3427. Bibcode:2010Natur.464.1021P. doi:10.1038/nature09008. PMID 20393558. S2CID 4300790.
77. Tebyanian, H.; Zahidy, M.; Avesani, M.; Stanco, A.; Villoresi, P.; Vallone, G. (2021). "Semi-device independent randomness generation based on quantum state's indistinguishability". *Quantum Science and Technology*. 6(4), 045026. doi:10.1088/2058-9565/ac2047.
78. Brunner, Nicolas; Pironio, Stefano; Acín, Antonio; Gisin, Nicolas; Methot, Andre Allan; Scarani, Valerio (2008). "Testing the Hilbert space dimension". *Physical Review Letters*. 100 (21) 210503. arXiv:0802.0760. Bibcode:2008arXiv0802.0760B. doi:10.1103/PhysRevLett.100.210503. PMID 18518591. S2CID 119256543.
79. Prakash, Anupam; Sikora, Jamie; Varvitsiotis, Antonios; Wei Zhaohui (2018). "Completely positive semidefinite rank". *Mathematical Programming*. 171 (1-2): 397-431. arXiv:1604.07199. doi:10.1007/s10107-017-1198-4. S2CID 17885968.
80. Navascués, Miguel; Vértesi, Tamás (2015). "Bounding the set of finite dimensional quantum correlations". *Physical Review Letters*. 115 (2) 020501. arXiv:1412.0924. Bibcode:2015PhRvL.115b0501N. doi:10.1103/PhysRevLett.115.020501. PMID 26207454. S2CID 12226163.
81. Coladangelo, Andrea; Stark, Jalex (2018). "Unconditional separation of finite and infinite-dimensional quantum correlations". arXiv:1804.05116 [quant-ph].
82. Pawlowski, Marcin; Brunner, Nicolas (2011). "Semi-device-independent security of one-way quantum key distribution". *Physical Review A*. 84 (1): 010302(R). arXiv:1103.4105. Bibcode:2011PhRvA..84a0302P. doi:10.1103/PhysRevA.84.010302. S2CID 119300029.
83. Li, Hong-Wei; Yin, Zhen-Qiang; Wu, Yu-Chun; Zou, Xu-Bo; Wang, Shuang; Chen, Wei; Guo, Guang-Can; Han, Zheng-Fu (2011). "Semi-device-independent random-number expansion without entanglement". *Physical Review A*. 84 (3) 034301. arXiv:1108.1480. Bibcode:2011PhRvA..84c4301L. doi:10.1103/PhysRevA.84.034301. S2CID 118407749.

## Further Reading

- Grib, AA; Rodrigues, WA (1999). *Nonlocality in Quantum Physics*. Springer Verlag. ISBN 978-0-306-46182-8.
- Cramer, JG (2015). *The Quantum Handshake: Entanglement, Nonlocality and Transactions*. Springer Verlag. ISBN 978-3-319-24642-0.
- Duarte, FJ (2019). *Fundamentals of Quantum Entanglement*. Institute of Physics (UK). ISBN 978-0-7503-2226-3.

Retrieved from: https://en.wikipedia.org/w/index.php?title=Quantum_nonlocality&oldid=1351218549
