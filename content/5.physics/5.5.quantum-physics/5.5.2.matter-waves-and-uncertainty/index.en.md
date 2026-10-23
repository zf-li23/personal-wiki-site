---
title: Matter Waves and the Uncertainty Relation
description: The de Broglie hypothesis and matter waves, electron diffraction experiments, phase and group velocities of matter waves, calculation of the de Broglie wavelength; the single-electron double-slit experiment, the wave function and Born's statistical interpretation, superposition of probability amplitudes and the superposition principle of states, plane waves of a free particle; the position–momentum and energy–time uncertainty relations and order-of-magnitude estimates.
source_hash: 892b096040a0
---

The previous chapter ([5.5.1](/5.5.1)) showed that light is both a wave and a particle: the energy and momentum of a **photon**, $\varepsilon=h\nu$ and $p=h/\lambda$, connect its particle nature with its wave nature. This chapter asks the converse question: do massive particles such as electrons and protons also have a wave nature? De Broglie answered yes in 1924, and electron diffraction experiments confirmed it three years later (Section 2.1). What kind of wave is a matter wave? The single-electron double-slit experiment and Born's statistical interpretation show that it is a probability wave describing the probability of finding the particle at each point in space, and that the essence of the wave nature is the coherent superposition of probability amplitudes (Section 2.2). The coexistence of particle and wave nature invalidates the classical concept of a "trajectory", and its quantitative expression is Heisenberg's uncertainty relation (Section 2.3).

The mathematics and physics used in this chapter are the **phase velocity**, **group velocity** and **dispersion** of waves ([5.1.7](/5.1.7#sec-7.10)), the energy and momentum of special relativity ([5.1.8](/5.1.8#sec-8.9)), the **probability density function** and **standard deviation** from probability theory ([3.1](/3.1)), and the **Fourier transform** with its **uncertainty principle** ([2.5.6](/2.5.6#sec-6.3.4)). The next chapter, [5.5.3](/5.5.3), writes down the Schrödinger equation satisfied by the wave function.

## 2.1. The Wave Nature of Massive Particles

### 2.1.1. The de Broglie Hypothesis

Since light has a particle nature, do massive particles have a wave nature? Guided by the symmetry of nature, de Broglie concluded that they do. In his doctoral thesis "Researches on the Quantum Theory", submitted to the University of Paris in November 1924, he proposed:

**Definition 2.1.1 (Matter Wave)** A massive particle of energy $E$ and momentum $\boldsymbol{p}$ also has a wave nature, and the wave associated with it is called a **matter wave** (de Broglie wave). Its frequency $\nu$ and wavelength $\lambda$ are related to the energy and momentum of the particle in the same way as for the photon:

$$
E=h\nu=\hbar\omega,\qquad p=\frac{h}{\lambda}=\hbar k,\tag{2.1}
$$
where $\hbar=h/(2\pi)$, $\omega=2\pi\nu$ and $k=2\pi/\lambda$. Equation (2.1) is called the Einstein–de Broglie relations, and $\lambda=h/p$ is called the **de Broglie wavelength** of the particle.

The quantity $\hbar$ is called the *reduced Planck constant*,

$$
\hbar=\frac{h}{2\pi}=1.055\times10^{-34}\,\mathrm{J\,s}=6.582\times10^{-16}\,\mathrm{eV\,s}.
$$
In vector form $\boldsymbol{p}=\hbar\boldsymbol{k}$, where $\boldsymbol{k}$ is the **wave vector**.

The concept of matter waves immediately explains the puzzling quantization condition of **angular momentum** in Bohr's atomic model ([5.5.4](/5.5.4)). If the electron in a hydrogen atom moves stably on a circular orbit of radius $r$, the matter wave associated with it must be in phase with itself after one trip around the orbit, that is, it forms a **standing wave** along the circumference: $2\pi r=n\lambda$, $n=1,2,\dots$. Substituting $\lambda=h/p$ gives $L=rp=n\frac{h}{2\pi}=n\hbar$, which is exactly Bohr's quantization condition.

De Broglie's supervisor Langevin sent the thesis to Einstein, who said that it "lifted a corner of the great veil", and the theory of matter waves began to receive attention. At the thesis defense Perrin asked how such waves could be confirmed experimentally, and de Broglie answered: by the diffraction of electrons by crystals.

### 2.1.2. Electron Diffraction Experiments

Why use a crystal? An electron accelerated from rest through a voltage $U$ has kinetic energy $E_{\mathrm{k}}=eU$. For $eU\ll m_{\mathrm{e}}c^2$ the nonrelativistic relation $p=\sqrt{2m_{\mathrm{e}}eU}$ can be used, so

$$
\lambda=\frac{h}{\sqrt{2m_{\mathrm{e}}eU}}=\frac{1.226}{\sqrt{U/\mathrm{V}}}\,\mathrm{nm}.\tag{2.2}
$$
For $U=100\,\mathrm{V}$, $\lambda=0.123\,\mathrm{nm}$, of the same order as the wavelength of **X-rays** and the spacing of atoms in a crystal, so a crystal can serve as a diffraction **grating** for electron waves, just as it does for X-rays ([5.4.2](/5.4.2)).

**Example 2.1.1 (The Davisson–Germer Experiment)** In 1927 Davisson and Germer directed an electron beam at normal incidence onto the surface of a nickel single crystal and measured the reflected electron current $I$ as a function of direction and accelerating voltage $U$. At $U=54\,\mathrm{V}$ a pronounced maximum of the electron current appeared in the direction at $50^\circ$ to the incident beam. The spacing of the rows of atoms on the nickel surface is $d=0.215\,\mathrm{nm}$. Treating the surface as a reflection grating, the first-order maximum satisfies $d\sin\varphi=\lambda$, giving $\lambda=0.215\times\sin50^\circ\,\mathrm{nm}=0.165\,\mathrm{nm}$; by Eq. (2.2), $\lambda=1.226/\sqrt{54}\,\mathrm{nm}=0.167\,\mathrm{nm}$, and the two agree.

In another version of the experiment, the directions of incidence and detection are fixed and the accelerating voltage is varied. If the electrons are reflected from a set of crystal planes of spacing $d$ at glancing angle $\varphi$, the condition for constructive interference of the waves reflected from adjacent planes is Bragg's formula $2d\sin\varphi=k\lambda$ ($k=1,2,\dots$). By Eq. (2.2),

$$
\sqrt{U}=k\,\frac{h}{2d\sin\varphi\sqrt{2em_{\mathrm{e}}}},
$$
so the electron current $I$ shows a series of equally spaced maxima as a function of $\sqrt{U}$, exactly as observed.

In the same year G. P. Thomson sent a high-energy electron beam (about $10$–$60\,\mathrm{keV}$) through thin polycrystalline films of gold, aluminum and other metals and obtained on a photographic plate concentric rings exactly analogous to those of X-ray powder diffraction. In 1961 Jönsson performed single-, double-, triple- and four-slit diffraction experiments with electrons and obtained patterns identical to those of multiple-slit diffraction of light. De Broglie received the 1929 Nobel Prize in Physics for the discovery of the wave nature of electrons; Davisson and G. P. Thomson shared the 1937 Nobel Prize in Physics (his father J. J. Thomson had received the 1906 prize for discovering the electron as a particle).

Subsequently, diffraction was observed for protons, neutrons, helium atoms (Estermann and Stern, 1930) and even $\ce{C60}$ molecules (Arndt, Zeilinger and others, 1999): all massive particles have a wave nature. Electron diffraction and neutron diffraction, like X-ray diffraction, are now routine means of studying the structure of crystals and molecules; the electron microscope exploits the extremely short wavelength of electrons, and its resolving power is far higher than that of the optical microscope ([5.4.2](/5.4.2)).

**Example 2.1.2 (De Broglie Wavelength of a Macroscopic Object)** For a bullet of mass $m=0.01\,\mathrm{kg}$ and speed $v=300\,\mathrm{m/s}$,

$$
\lambda=\frac{h}{mv}=\frac{6.63\times10^{-34}}{0.01\times300}\,\mathrm{m}=2.2\times10^{-34}\,\mathrm{m},
$$
which is $10^{19}$ times smaller than an atomic nucleus. No apparatus could reveal its diffraction, so macroscopic objects show only their particle nature.

Nature has two yardsticks: the speed of light $c$ and the **Planck constant** $h$. For $v\ll c$ (formally $c\to\infty$) relativity reduces to Newtonian mechanics; when the action is much larger than $h$ (formally $h\to0$) the wavelength tends to zero and quantum physics reduces to classical physics.

### 2.1.3. Phase Velocity and Group Velocity of Matter Waves

What is the speed of a matter wave? For a particle of mass $m$ and velocity $v$, special relativity gives $E=\gamma mc^2$ and $p=\gamma mv$ ([5.1.8](/5.1.8#sec-8.9)), and by Eq. (2.1) the **phase velocity** of the matter wave is

$$
u=\nu\lambda=\frac{\omega}{k}=\frac{E}{p}=\frac{\gamma mc^2}{\gamma mv}=\frac{c^2}{v}.\tag{2.3}
$$
Since $v<c$, the phase velocity $u>c$, and it is not equal to the speed of the particle. This does not violate relativity: the phase velocity is only the speed at which surfaces of constant phase move, and it transmits neither energy nor information. The **dispersion relation** of matter waves follows from the energy–momentum relation $E^2=p^2c^2+m^2c^4$, namely $\omega(k)=\sqrt{c^2k^2+m^2c^4/\hbar^2}$, so matter waves are dispersive even in vacuum. The particle is represented by a wave packet formed by the superposition of a group of waves with nearby frequencies, and the packet moves with the **group velocity**:

$$
v_{\mathrm{g}}=\frac{\mathrm{d}\omega}{\mathrm{d}k}=\frac{\mathrm{d}E}{\mathrm{d}p}=\frac{pc^2}{E}=\frac{\gamma mvc^2}{\gamma mc^2}=v.
$$
The group velocity equals the speed of the particle, and $uv_{\mathrm{g}}=c^2$.

**Remark 2.1.1** Many textbooks use the "relativistic mass" $m=\gamma m_0$ and $E=mc^2$ to write $uv=c^2$ and call $u$ the "speed of the matter wave". With the convention used here (the invariant mass $m$, [Remark 8.7.1](/5.1.8#rem-8.7.1)) the result $u=c^2/v$ is unchanged, but it should be made clear that $u$ is the phase velocity, and that the quantity corresponding to the motion of the particle is the group velocity $v_{\mathrm{g}}=v$. The phase velocity itself has no direct physical meaning: in the nonrelativistic case one often takes $E=p^2/(2m)$ (dropping the rest energy), whereupon $u=\frac{E}{p}=\frac{v}{2}$, completely different from Eq. (2.3), while the group velocity $\frac{\mathrm{d}E}{\mathrm{d}p}=\frac{p}{m}=v$ is unaffected by the choice of the zero of energy.

For a photon, $m=0$ and $u=v_{\mathrm{g}}=c$, and either the momentum or the energy alone determines the wavelength and frequency: $\lambda=h/p$, $\nu=pc/h$. For a massive particle, $u\ne v$: the wavelength must be found from the momentum, $\lambda=h/p$, and the frequency from the energy, $\nu=E/h$, and both formulas are indispensable.

### 2.1.4. Calculating the de Broglie Wavelength

In practical problems the de Broglie wavelength is usually found from the kinetic energy $E_{\mathrm{k}}$ of the particle. From $E=E_{\mathrm{k}}+mc^2$ and $E^2=p^2c^2+m^2c^4$ we get $pc=\sqrt{E_{\mathrm{k}}^2+2E_{\mathrm{k}}mc^2}$, so

$$
\lambda=\frac{h}{p}=\frac{hc}{\sqrt{E_{\mathrm{k}}^2+2E_{\mathrm{k}}mc^2}}.\tag{2.4}
$$

- Nonrelativistic case $E_{\mathrm{k}}\ll mc^2$: $\lambda\approx\dfrac{h}{\sqrt{2mE_{\mathrm{k}}}}$; for an electron accelerated from rest through a voltage $U$, $E_{\mathrm{k}}=eU$, which gives Eq. (2.2).
- Extreme relativistic case $E_{\mathrm{k}}\gg mc^2$: $\lambda\approx\dfrac{hc}{E_{\mathrm{k}}}\approx\dfrac{hc}{E}$, the same as the wavelength of a photon of the same energy.

![De Broglie wavelength of electrons and neutrons versus kinetic energy (log–log scale). Solid lines: relativistic formula (2.4); dashed lines: nonrelativistic approximation; the two begin to separate when the kinetic energy approaches the rest energy mc², and for kinetic energies far above the rest energy they coincide with λ = hc/E for a photon of the same energy. The gray band marks the order of magnitude of interatomic spacings in crystals](./plots/de-broglie-wavelength.py)

**Example 2.1.3 (Electrons in a Transmission Electron Microscope)** In a transmission electron microscope the electrons are accelerated through a voltage $U=100\,\mathrm{kV}$. Find their de Broglie wavelength.

**Solution** Here $E_{\mathrm{k}}=100\,\mathrm{keV}$ and $m_{\mathrm{e}}c^2=511\,\mathrm{keV}$ are comparable, so the relativistic formula (2.4) must be used:

$$
pc=\sqrt{100^2+2\times100\times511}\,\mathrm{keV}=335\,\mathrm{keV},\qquad\lambda=\frac{hc}{pc}=\frac{1239.8\,\mathrm{eV\,nm}}{3.35\times10^5\,\mathrm{eV}}=3.70\times10^{-3}\,\mathrm{nm}.
$$
The nonrelativistic formula would give $3.88\times10^{-3}\,\mathrm{nm}$, about $5\%$ too large. Such a short wavelength allows the electron microscope to resolve individual atoms (the actual resolving power is limited by the aberrations of the electromagnetic lenses to about $0.05$–$0.1\,\mathrm{nm}$).

## 2.2. Probability Waves and Probability Amplitudes

### 2.2.1. The Single-Electron Double-Slit Experiment

What is the nature of matter waves? Several views were held early on. De Broglie regarded the wave as a "pilot wave" guiding the motion of the particle, without specifying its nature; Schrödinger held that the wave is fundamental and the electron is a wave packet of the matter wave, but under dispersion a wave packet spreads, whereas the electron is stable; a third view held that the particle is fundamental and the matter wave is a collective phenomenon arising from the interaction of many electrons. The last view is ruled out by the following experiment.

Let electrons pass through a double slit one at a time, with each electron emitted only after the previous one has reached the screen, so that the electrons cannot interact with each other. The results of the experiment (Tonomura et al., 1989) are:

- Each electron leaves only a single dot on the screen, and where it appears is random; this shows that the electron has a particle nature and is always detected as a whole.
- As the number of electrons grows, the dots gradually build up a double-slit **interference** pattern; this shows that a single electron already has a wave nature, and the interference is each electron interfering "with itself" rather than the result of interactions between electrons.

Where a single electron appears on the screen is a matter of probability; but under given conditions (for example a double slit) the probability distribution obeys a definite law, namely the law embodied in the diffraction pattern.

![Simulation of the single-electron double-slit experiment: landing points of electrons drawn one by one according to the probability density |ψ1 + ψ2|². With few electrons the points look disordered; as their number grows, interference fringes emerge. Bottom: the distribution |ψ1 + ψ2|² with both slits open compared with |ψ1|² + |ψ2|², which has no interference](./plots/double-slit-buildup.py)

### 2.2.2. The Wave Function and Born's Statistical Interpretation

Quantum mechanics postulates that the state of a microscopic particle is described by a complex function. A classical plane **harmonic wave** propagating in the positive $x$ direction can be written $y=A\cos(\omega t-kx)$, or, using **complex numbers**, $y=A\mathrm{e}^{-\mathrm{i}(\omega t-kx)}$ (taking the real part); the wave function describing a particle is essentially complex.

**Definition 2.2.1 (Wave Function)** The complex function $\Psi(\boldsymbol{r},t)$ (or $\Psi(x,t)$ in one dimension) that describes the state of a microscopic particle is called the **wave function** of the particle, also called the **probability amplitude**.

**Property 2.2.1 (Born Interpretation)** Born (1926): a matter wave does not represent the oscillation of some real physical quantity, as a classical wave does, but is a probability wave describing the probability distribution of the particle in space. The squared modulus of the wave function

$$
\lvert\Psi(\boldsymbol{r},t)\rvert^2=\Psi^*(\boldsymbol{r},t)\Psi(\boldsymbol{r},t)
$$
is the **probability density function** of the position of the particle at time $t$: the probability of finding the particle at time $t$ in a volume element $\mathrm{d}V$ near $\boldsymbol{r}$ is $\lvert\Psi(\boldsymbol{r},t)\rvert^2\,\mathrm{d}V$.

Thus the wave function itself has no direct physical meaning; what is meaningful is $\lvert\Psi\rvert^2$. Multiplying $\Psi$ by a constant factor $\mathrm{e}^{\mathrm{i}\alpha}$ of modulus 1 leaves the state described unchanged. For a single particle, $\lvert\Psi\rvert^2$ gives the probability density of finding it at each point; for a large number $N$ of particles in the same state, $N\lvert\Psi\rvert^2$ gives the distribution of particle number, which is the intensity distribution of the diffraction pattern. The concept of matter waves (probability waves) unifies the particle nature and the wave nature: the particle nature shows in the fact that a particle always appears as a whole at one place, and the wave nature in the fact that the probabilities of appearing are distributed and superposed according to the laws of waves. Born received the 1954 Nobel Prize in Physics for the statistical interpretation of the wave function.

The statistical interpretation provoked fierce debate at the time. Born held that the motion of particles obeys probabilistic laws while the evolution of the probability itself is still governed by causality (the Schrödinger equation of [5.5.3](/5.5.3) is deterministic). Einstein was never satisfied; he wrote to Born that quantum mechanics is certainly impressive, but "I, at any rate, am convinced that He does not throw dice." Schrödinger and de Broglie did not accept it either. The debate continued as the long dispute between Einstein and Bohr over the completeness of quantum mechanics ([5.5.4](/5.5.4)), and was settled experimentally only by the tests of Bell's inequalities (2022 Nobel Prize in Physics).

### 2.2.3. Standard Conditions for the Wave Function

The statistical interpretation imposes the following requirements on the wave function.

1. Finiteness: the probability $\int_{\Delta V}\lvert\Psi\rvert^2\,\mathrm{d}V$ of finding the particle in any finite volume $\Delta V$ of space must be finite.
2. Normalization: the probabilities of finding the particle, summed over all space, add up to 1,

   $$
   \int_{\Omega}\lvert\Psi(\boldsymbol{r},t)\rvert^2\,\mathrm{d}V=1,\tag{2.5}
   $$
   where $\Omega$ is all of space. Equation (2.5) is called the *normalization condition*. If $\int_\Omega\lvert\Psi\rvert^2\,\mathrm{d}V=A$ is finite, then $\frac{1}{\sqrt A}\Psi$ satisfies Eq. (2.5), and $\frac{1}{\sqrt A}$ is called the normalization factor.
3. Single-valuedness: the wave function has only one value at each time and each position, so that the probability density is well defined.
4. Continuity: in regions where the potential energy is finite, the wave function and its first derivative are continuous (the first derivative determines the probability current, [5.5.3](/5.5.3)).

Conditions 1–4 are together called the standard conditions of the wave function. In solving the Schrödinger equation they act as boundary conditions, and it is precisely they that restrict the energies of bound states to discrete values.

### 2.2.4. Superposition of Probability Amplitudes

Comparing three situations in the double-slit experiment shows how a probability wave differs from a classical particle and from a classical wave.

| | Only slit 1 open | Only slit 2 open | Both slits open | Interference? |
|---|---|---|---|---|
| Bullets | Distribution $P_1$ | Distribution $P_2$ | $P_{12}=P_1+P_2$ | No: the landing point of each bullet is random, but the probabilities simply add |
| Classical waves (water waves, light) | Intensity $I_1=\lvert A_1\rvert^2$ | $I_2=\lvert A_2\rvert^2$ | $I_{12}=\lvert A_1+A_2\rvert^2\ne I_1+I_2$ | Yes: amplitudes add |
| Electrons (incident one at a time) | $P_1=\lvert\Psi_1\rvert^2$ | $P_2=\lvert\Psi_2\rvert^2$ | $P_{12}=\lvert\Psi_1+\Psi_2\rvert^2\ne P_1+P_2$ | Yes: probability amplitudes add |

For classical waves, the complex amplitudes on the screen of the waves passing through slits 1 and 2 are $A_1(x)\mathrm{e}^{-\mathrm{i}\omega t}$ and $A_2(x)\mathrm{e}^{-\mathrm{i}\omega t}$; with both slits open the resultant amplitude is $(A_1+A_2)\mathrm{e}^{-\mathrm{i}\omega t}$, and the intensity is

$$
I_{12}=\lvert A_1+A_2\rvert^2=I_1+I_2+A_1^*A_2+A_1A_2^*,
$$
the last two terms being the **interference** terms ([5.4.1](/5.4.1)). The case of electrons is completely analogous. With only slit 1 open, the electron passes through slit 1 and its state is $\Psi_1$; with only slit 2 open its state is $\Psi_2$. With both slits open the electron can pass through slit 1 or through slit 2, its state is a superposition of the two, the total probability amplitude is $\Psi_{12}=\Psi_1+\Psi_2$, and the probability distribution is

$$
P_{12}=\lvert\Psi_1+\Psi_2\rvert^2=\lvert\Psi_1\rvert^2+\lvert\Psi_2\rvert^2+2\operatorname{Re}(\Psi_1^*\Psi_2)\ne P_1+P_2.
$$
Even with a single electron, its state with both slits open must be described by $\Psi_1+\Psi_2$, and the superposition of probability amplitudes produces the interference. The essence of the wave nature of microscopic particles is the coherent superposition of probability amplitudes, and the diffraction pattern is the result of the interference of probability waves. Feynman summarized this as follows: if an event can occur in several indistinguishable ways, its probability amplitude is the sum of the probability amplitudes of the individual ways. Conversely, if some means is used to determine through which slit each electron passes, the two ways become distinguishable, the probability amplitudes no longer add, the interference fringes disappear, and the distribution becomes $P_1+P_2$.

### 2.2.5. The Superposition Principle of States

The superposition $\Psi_1+\Psi_2$ in the double-slit experiment is a special case of a general principle.

**Property 2.2.2 (Superposition Principle of States)** If $\Psi_1,\Psi_2,\dots$ are possible states of a particle, then any linear combination of them

$$
\Psi=\sum_nC_n\Psi_n\qquad(C_n\text{ arbitrary complex constants})
$$
is also a possible state of the particle. If the $\Psi_n$ are the states in which some physical quantity takes different definite values, and are normalized and mutually orthogonal ($\int\Psi_m^*\Psi_n\,\mathrm{d}V=\delta_{mn}$) with $\sum_n\lvert C_n\rvert^2=1$, then a measurement of that quantity on a particle in the state $\Psi$ gives the $n$th value (after which the particle is in the state $\Psi_n$) with probability $\lvert C_n\rvert^2$.

In the language of linear algebra, the state of a particle is a vector in a complex linear space, $\{\Psi_n\}$ is an **orthonormal basis**, and $C_n=\int\Psi_n^*\Psi\,\mathrm{d}V$ is the coordinate of $\Psi$ in this basis (an **inner product**). The superposition principle requires the equation of motion satisfied by the wave function to be linear, and this is the Schrödinger equation ([5.5.3](/5.5.3)). A superposed state differs from a classical probabilistic mixture: a particle in the state $\Psi_1+\Psi_2$ is not "either in $\Psi_1$ or in $\Psi_2$", for otherwise there would be no interference term. Schrödinger's cat (1935) links a microscopic superposed state to the life and death of a macroscopic cat, highlighting the conflict between the microscopic superposition principle and macroscopic experience; this raises the problems of measurement and decoherence.

### 2.2.6. The Wave Function of a Free Particle

A particle subject to no force has constant momentum $\boldsymbol{p}$ and energy $E$, so by Eq. (2.1) its matter wave is a monochromatic plane wave with definite frequency and wavelength. Replacing $\omega$ and $k$, which describe the wave nature, in the complex plane **harmonic wave** $A\mathrm{e}^{-\mathrm{i}(\omega t-kx)}$ by $E/\hbar$ and $p/\hbar$, which describe the particle nature, gives the wave function of a free particle moving in the $x$ direction:

$$
\Psi(x,t)=A\,\mathrm{e}^{-\frac{\mathrm{i}}{\hbar}(Et-px)}=\psi(x)\,\mathrm{e}^{-\mathrm{i}Et/\hbar},\qquad\psi(x)=A\,\mathrm{e}^{\mathrm{i}px/\hbar}.\tag{2.6}
$$
The function $\psi(x)$ is called the spatial wave function; the particle moves to the right for $p>0$ and to the left for $p<0$. In three dimensions $\psi(\boldsymbol{r})=A\,\mathrm{e}^{\mathrm{i}\boldsymbol{p}\cdot\boldsymbol{r}/\hbar}$.

The probability density of a free particle, $\lvert\Psi\rvert^2=\lvert A\rvert^2$, is the same everywhere: the momentum of the particle is completely definite, while its position is completely undetermined. Such a wave function cannot be normalized over all space and is an idealization. A real particle is always confined to a finite region, and its wave function is a wave packet formed by the superposition of many plane waves; by the **Fourier transform**, the more concentrated the packet is in space, the more spread out are the required momentum (wave number) components, and this is the uncertainty relation of the next section.

### 2.2.7. Understanding Wave–Particle Duality

A microscopic particle is neither a classical particle nor a classical wave.

- Particle nature means "atomicity" or "wholeness": a particle has concentrated energy $E$ and momentum $\boldsymbol{p}$ and is always produced, absorbed and detected as a whole; but it has no definite trajectory, and the classical concept of a "trajectory" is abandoned.
- Wave nature means "diffuseness" and "superposability": it shows itself in interference, diffraction and **polarization**, and is characterized by a wavelength $\lambda$ and a **wave vector** $\boldsymbol{k}=\frac{2\pi}{\lambda}\boldsymbol{e}_k$; but it does not represent the oscillation in space of any real physical quantity, only the oscillation of the probability amplitude.

Under some conditions a microscopic particle shows its particle nature and under others its wave nature; the two properties reside in the same object, but they do not both show up completely in the same experiment (for example, once we determine through which slit the electron passes, no interference is seen). It is like the ambiguous picture of a "young woman and an old woman": the two images never appear in the visual field at the same time. Bohr summarized this as the principle of complementarity ([5.5.4](/5.5.4)).

## 2.3. The Uncertainty Relation

### 2.3.1. The Position–Momentum Uncertainty Relation

To what extent does the classical concept of a trajectory apply to the microscopic world? In 1927 Heisenberg analyzed several thought experiments (for example, measuring the position of an electron with a $\gamma$-ray microscope) and, combining them with the de Broglie relation, concluded that the coordinate and the momentum of a particle along the same direction cannot be determined simultaneously. In the same year Kennard stated it rigorously as an inequality for standard deviations.

**Theorem 2.3.1 (Heisenberg Uncertainty Relation)** In any state, the **standard deviations** of the coordinate of a particle and of the momentum along the same direction satisfy

$$
\Delta x\,\Delta p_x\ge\frac{\hbar}{2},\qquad\Delta y\,\Delta p_y\ge\frac{\hbar}{2},\qquad\Delta z\,\Delta p_z\ge\frac{\hbar}{2}.\tag{2.7}
$$
Here $\Delta x$ is the standard deviation of $x$ computed with the probability density $\lvert\psi(x)\rvert^2$, and $\Delta p_x$ is the standard deviation of the momentum in the same state.

Mathematically, Eq. (2.7) is the **uncertainty principle** of Fourier analysis ([Theorem 6.3.3](/2.5.6#thm-6.3.3)). In quantum mechanics, the momentum probability amplitude $\varphi(p)$ of a particle is the **Fourier transform** of the coordinate wave function $\psi(x)$ in the variable $\xi=p/\hbar$ (times a normalization constant):

$$
\varphi(p)=\frac{1}{\sqrt{2\pi\hbar}}\int_{-\infty}^{\infty}\psi(x)\,\mathrm{e}^{-\mathrm{i}px/\hbar}\,\mathrm{d}x,
$$
that is, $\psi$ is a superposition of plane waves (2.6) of various momenta, and $\lvert\varphi(p)\rvert^2$ is the probability density of momentum. Section [2.5.6](/2.5.6#sec-6.3.4) proves that $\sigma_x\sigma_\xi\ge\frac12$ (valid for any center of the distribution), and since $\Delta p_x=\hbar\sigma_\xi$, it follows that $\Delta x\,\Delta p_x\ge\frac{\hbar}{2}$. Equality holds if and only if $\psi$ is a Gaussian function, in which case both position and momentum follow **normal distributions**.

![Gaussian wave packets (with ħ = 1 and mean momentum p0 = 4). Left: real part and probability density |ψ(x)|² of two packets of different widths; right: the corresponding momentum probability densities |φ(p)|². The narrower the position distribution, the wider the momentum distribution; the product σ_x σ_p is always equal to ħ/2, the lower bound of the uncertainty relation](./plots/gaussian-wave-packet.py)

The uncertainty relation is an inevitable consequence of the **wave–particle duality** of microscopic particles and has nothing to do with the precision of measuring instruments or the imperfection of measurement methods: there is no state in which the coordinate and the momentum both have definite values. It deprives the motion of microscopic particles of the concept of a "trajectory", because a trajectory requires both position and velocity to be definite at every instant. A pair of physical quantities such as $x$ and $p_x$ that satisfy an uncertainty relation is called conjugate quantities; there is no such restriction between a coordinate and the momentum along a different direction (such as $x$ and $p_y$).

### 2.3.2. Estimate from Single-Slit Electron Diffraction

Single-slit diffraction gives a rough picture of where the uncertainty relation comes from. An electron beam of momentum $p$ is directed along the $y$ direction at a slit of width $a$. As an electron passes the slit, the uncertainty of its position in the $x$ direction is $\Delta x\approx a$. After the slit the electrons are diffracted, and most of them fall within the central bright fringe; the diffraction angle $\theta_1$ at the edge of the central fringe satisfies $a\sin\theta_1=\lambda$ ([5.4.2](/5.4.2)). Considering only the central fringe, the $x$ component of the electron momentum lies between $0$ and $p\sin\theta_1$, so

$$
\Delta p_x\approx p\sin\theta_1=\frac{h}{\lambda}\cdot\frac{\lambda}{a}=\frac{h}{\Delta x},\qquad\Delta x\,\Delta p_x\approx h.
$$
The narrower the slit, the more definite the position, the stronger the diffraction, and the more uncertain the momentum. Here $\Delta x$ and $\Delta p_x$ are only rough ranges, not standard deviations, so the result gives the order of magnitude of $h$ and is consistent with Eq. (2.7). In order-of-magnitude estimates one often uses $\Delta x\,\Delta p_x\gtrsim\hbar$ or $\gtrsim h$, caring only about the order of magnitude.

### 2.3.3. The Energy–Time Uncertainty Relation

Corresponding to Eq. (2.7), energy and time also satisfy an uncertainty relation

$$
\Delta E\,\Delta t\gtrsim\frac{\hbar}{2}.\tag{2.8}
$$
Its meaning differs from that of Eq. (2.7): time is not a physical quantity of the particle, $\Delta t$ is the time required for the state of the system to change appreciably, for example the lifetime of an excited state or the duration of a wave train, and $\Delta E$ is the uncertainty of the energy of that state. By Fourier analysis, an oscillation lasting for a time $\Delta t$ contains a frequency range $\Delta\nu\sim1/\Delta t$, and multiplying by $h$ gives $\Delta E\,\Delta t\sim h$, the same as the relation $\tau_{\mathrm{c}}=1/\Delta\nu$ between **coherence time** and **spectral linewidth** in optics ([5.4.1](/5.4.1#sec-1.3.3)). Hence only a state of infinite lifetime (a stationary state) has a definite energy; for an excited state of finite lifetime the energy level has a certain width, and the spectral line it emits also has a certain natural width.

### 2.3.4. Order-of-Magnitude Estimates

The uncertainty relation is often used to estimate whether quantum effects are important.

**Example 2.3.1 (Electrons in Atoms Have No Trajectories)** Let the kinetic energy of an electron in an atom be $E_{\mathrm{k}}=10\,\mathrm{eV}$ and the size of the atom $r\sim10^{-10}\,\mathrm{m}$. The speed of the electron is

$$
v=\sqrt{\frac{2E_{\mathrm{k}}}{m_{\mathrm{e}}}}=\sqrt{\frac{2\times10\times1.60\times10^{-19}}{9.11\times10^{-31}}}\,\mathrm{m/s}\approx1.9\times10^6\,\mathrm{m/s}.
$$
The electron is confined within the atom, $\Delta x\sim10^{-10}\,\mathrm{m}$, so by Eq. (2.7),

$$
\Delta v=\frac{\Delta p}{m_{\mathrm{e}}}\ge\frac{\hbar}{2m_{\mathrm{e}}\Delta x}=\frac{1.05\times10^{-34}}{2\times9.11\times10^{-31}\times10^{-10}}\,\mathrm{m/s}\approx6\times10^5\,\mathrm{m/s},
$$
of the same order as $v$. The velocity of the electron is completely uncertain, the concept of an orbit does not apply to electrons in atoms, and they can only be described by a probability distribution (the electron cloud).

**Example 2.3.2 (Aiming a Bullet)** A bullet has mass $m=0.01\,\mathrm{kg}$ and the muzzle has diameter $0.5\,\mathrm{cm}$. The uncertainty of the transverse position of the bullet as it leaves the muzzle is $\Delta x\approx0.5\times10^{-2}\,\mathrm{m}$, and the uncertainty of the transverse velocity is

$$
\Delta v_x\ge\frac{\hbar}{2m\Delta x}=\frac{1.05\times10^{-34}}{2\times0.01\times0.5\times10^{-2}}\,\mathrm{m/s}\approx1\times10^{-30}\,\mathrm{m/s}.
$$
Even if this is taken as the maximum transverse velocity, it is far smaller than the speed of the bullet and has no effect on aiming. In macroscopic phenomena the effect of the uncertainty relation can be neglected.

**Example 2.3.3 (Position Uncertainty of a Photon)** Let light propagate in the $x$ direction with wavelength $\lambda$ and wavelength uncertainty (linewidth) $\Delta\lambda$. The photon momentum is $p_x=h/\lambda$, so $\Delta p_x=\frac{h}{\lambda^2}\Delta\lambda$, and the position uncertainty of the photon is

$$
\Delta x\approx\frac{h}{\Delta p_x}=\frac{\lambda^2}{\Delta\lambda}.
$$
This is exactly the **coherence length** of light, the length of the wave train ([Definition 1.3.2](/5.4.1#def-1.3.2)): the position uncertainty of the photon is the length of the corresponding wave train. For strictly monochromatic light $\Delta\lambda=0$, the wave train is infinitely long, and the energy of the photon is completely definite while its position is completely undetermined.

**Example 2.3.4 (Natural Width of an Energy Level)** An excited state of an atom has a lifetime $\Delta t\approx10^{-8}\,\mathrm{s}$; by Eq. (2.8), the width of this level is

$$
\Delta E\ge\frac{\hbar}{2\Delta t}=\frac{6.58\times10^{-16}\,\mathrm{eV\,s}}{2\times10^{-8}\,\mathrm{s}}\approx3.3\times10^{-8}\,\mathrm{eV}.
$$
This is very small compared with the level spacing (a few $\mathrm{eV}$), but it determines the natural width of the spectral line. The lifetime of the ground state is infinite, and its level has no natural width.

**Example 2.3.5 (Tracks in a Cloud Chamber)** An electron of kinetic energy $E_{\mathrm{k}}\approx10^8\,\mathrm{eV}$ enters a cloud chamber, and the size of the track is about $10^{-4}\,\mathrm{cm}$. Does the concept of a "trajectory" apply?

**Solution** The position uncertainty of the electron is $\Delta x\approx10^{-6}\,\mathrm{m}$, and the momentum uncertainty is $\Delta p_x\ge\frac{\hbar}{2\Delta x}\approx5\times10^{-29}\,\mathrm{kg\,m\,s^{-1}}$. Since $E_{\mathrm{k}}\gg m_{\mathrm{e}}c^2=0.511\,\mathrm{MeV}$, this is the extreme relativistic case, and the momentum of the electron is

$$
p\approx\frac{E_{\mathrm{k}}}{c}=\frac{10^8\times1.60\times10^{-19}}{3.00\times10^8}\,\mathrm{kg\,m\,s^{-1}}=5.3\times10^{-20}\,\mathrm{kg\,m\,s^{-1}}.
$$
Since $p\gg\Delta p_x$, on this scale the coordinate and momentum of the electron can be regarded as simultaneously definite, and the concept of a trajectory applies. In experiments, high-energy particles are in fact studied through the tracks they leave in cloud chambers and bubble chambers.

Comparing Example 2.3.1 with Example 2.3.5 shows that whether the concept of a trajectory applies depends on the scale of the problem: it depends on whether the $\Delta p$ given by the uncertainty relation is negligible compared with the momentum of the particle itself, that is, on whether the de Broglie wavelength is negligible compared with the characteristic length of the problem.

## Summary

| Topic | Key points |
|---|---|
| De Broglie relations | $E=h\nu=\hbar\omega$, $p=h/\lambda=\hbar k$; massive particles also have a wave nature |
| Experimental confirmation | Davisson–Germer (nickel single crystal), G. P. Thomson (polycrystalline films), Jönsson multiple slits; for electrons $\lambda=1.226\,\mathrm{nm}/\sqrt{U/\mathrm{V}}$ |
| Wave speeds | Phase velocity $u=E/p=c^2/v>c$; group velocity $v_{\mathrm{g}}=\mathrm{d}E/\mathrm{d}p=v$ |
| Wavelength | $\lambda=hc/\sqrt{E_{\mathrm{k}}^2+2E_{\mathrm{k}}mc^2}$; nonrelativistic $h/\sqrt{2mE_{\mathrm{k}}}$, extreme relativistic $hc/E_{\mathrm{k}}$ |
| Probability waves | $\lvert\Psi\rvert^2$ is the probability density; normalization $\int\lvert\Psi\rvert^2\,\mathrm{d}V=1$; standard conditions: finite, single-valued, continuous |
| Superposition | Probability amplitudes add, $\Psi_{12}=\Psi_1+\Psi_2$, probabilities do not; superposition principle $\Psi=\sum C_n\Psi_n$, with $\lvert C_n\rvert^2$ the probabilities |
| Free particle | $\Psi=A\,\mathrm{e}^{-\mathrm{i}(Et-px)/\hbar}$; momentum definite, position completely undetermined |
| Uncertainty relation | $\Delta x\,\Delta p_x\ge\hbar/2$ (the uncertainty principle of the Fourier transform); $\Delta E\,\Delta t\gtrsim\hbar/2$; range of validity of the trajectory concept |

## Questions

1. Which has the larger de Broglie wavelength, an electron or a proton of the same speed? What if they have the same kinetic energy?

   **Answer** in both cases the electron's is larger. For the same speed $\lambda=h/(mv)\propto1/m$; for the same kinetic energy (nonrelativistic) $\lambda=h/\sqrt{2mE_{\mathrm{k}}}\propto1/\sqrt{m}$.

2. Is a matter wave an **electromagnetic wave**?

   **Answer** no. An electromagnetic wave is an oscillation of the electromagnetic field, whereas a matter wave is an oscillation of the probability amplitude; uncharged particles such as neutrons also have matter waves.

3. Is the wave nature more pronounced the larger the momentum of the particle?

   **Answer** on the contrary, the larger the momentum, the shorter the wavelength, the harder it is to observe diffraction at obstacles of a given size, and the more pronounced the particle nature.

4. In the single-electron double-slit experiment, what happens to the pattern on the screen if a detector is placed behind one slit to determine through which slit each electron passes?

   **Answer** the interference fringes disappear and the distribution becomes $P_1+P_2$. A measurement that can distinguish the paths necessarily disturbs the electron, so that the probability amplitudes of the two paths are no longer coherent.

5. Is the uncertainty relation caused by insufficiently precise measuring instruments?

   **Answer** no. It comes from the properties of the wave function itself: the more concentrated the coordinate wave function, the more spread out its Fourier transform (the momentum probability amplitude), independently of the means of measurement.
