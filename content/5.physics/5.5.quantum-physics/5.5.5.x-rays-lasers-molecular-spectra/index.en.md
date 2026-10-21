---
title: X-Rays, Lasers and Molecular Spectra
description: The continuous X-ray spectrum (bremsstrahlung and the cutoff wavelength) and the characteristic spectrum (K and L series, Moseley's law) with applications; spontaneous emission, stimulated absorption, stimulated emission and the Einstein coefficients, population inversion, the He–Ne laser, longitudinal and transverse modes of the optical resonator; electronic, vibrational and rotational levels of molecules, rotational spectra, rovibrational spectra and band spectra.
source_hash: 5ea7dd7480ba
---

The previous chapter ([5.5.4](/5.5.4)) treated the electrons in atoms with quantum mechanics: energy levels, quantum numbers, the structure of **electron shells** and the **Pauli exclusion principle**. This chapter discusses three important applications of atomic and molecular energy levels, each an example of atomic physics moving from "explaining spectra" to "using spectra". Section 5.1 treats X-ray spectra: the continuous spectrum comes from the radiation of electrons decelerating in the target, and its short-wavelength limit is another piece of evidence for the **photon** theory; the characteristic spectrum comes from transitions of inner-shell electrons, and Moseley used it to establish the physical meaning of the atomic number. The discovery of X-rays, their wave nature and their **diffraction** by crystals were covered in [5.4.2](/5.4.2#sec-2.5), so here we discuss only the spectra. Section 5.2 treats lasers: in 1916–1917 Einstein introduced stimulated emission in order to bring atoms and radiation into thermal equilibrium, and some forty years later it became the principle of the laser; the coherence of laser light was already used in [5.4.1](/5.4.1#sec-1.2). Section 5.3 (optional) treats molecular spectra: a molecule has two kinds of motion beyond those of an atom, vibration and rotation, whose energy levels are those of the **quantum harmonic oscillator** of [5.5.3](/5.5.3) and of the quantized rigid rotor, respectively; the resulting infrared and microwave spectra are basic tools in chemistry for identifying molecular structure.

## 5.1. X-Ray Spectra

### 5.1.1. Production of X-Rays and Composition of the Spectrum

An X-ray tube is a glass tube evacuated to a high vacuum: a heated cathode K emits thermal electrons, a high voltage $U$ of several tens of kilovolts is applied between the cathode and the anode A, and the accelerated electrons bombard the anode (usually a metal such as tungsten, molybdenum or copper, called the target), producing X-rays at the target. Separating the X-rays by wavelength with a crystal according to the Bragg formula ([5.4.2](/5.4.2#sec-2.5.3)) and measuring the intensity at each wavelength gives the X-ray emission spectrum.

Experiments show that the X-ray spectrum is the superposition of two parts (left of the figure below):

- The continuous spectrum contains all wavelengths, with intensity varying continuously with wavelength. On the short-wavelength side it has a sharp limiting wavelength $\lambda_{\min}$, which decreases as the voltage increases and is independent of the target material; the larger the atomic number of the target element, the stronger the continuous spectrum, but its shape is essentially unchanged.
- The line spectrum consists of several sharp lines superimposed on the continuous spectrum. Their wavelengths are determined by the target element and are independent of the voltage; they appear only when the voltage exceeds a certain value.

These differ greatly from optical atomic spectra. Optical line spectra come from transitions of valence electrons, with **photon** energies of $10^{-1}$–$10\,\mathrm{eV}$ (wavelengths from infrared to ultraviolet) and a periodic dependence on the element; X-ray line spectra come from transitions of inner-shell electrons, with photon energies of $10^3$–$10^5\,\mathrm{eV}$ (wavelengths of about $0.01$–$1\,\mathrm{nm}$) and a monotonic dependence on the element, without periodicity.

![X-ray spectra. Left: spectra of a molybdenum target at 15–30 kV (schematic; the continuum is drawn with Kramers' formula and vertical lines mark the cutoff wavelength for each voltage): the characteristic lines K_α (0.0709 nm) and K_β (0.0632 nm) appear only when the voltage exceeds the K-shell ionization energy of molybdenum, 20.0 keV, and their wavelengths do not change with voltage. Right: square root of the K_α1 line frequency versus atomic number for the elements (Moseley plot); the dashed line is Moseley's law](./plots/xray-spectrum.py)

### 5.1.2. The Continuous Spectrum and the Cutoff Wavelength

**Definition 5.1.1 (Bremsstrahlung)** The electromagnetic radiation emitted when a charged particle is sharply decelerated (or deflected) in the Coulomb field of a nucleus is called **bremsstrahlung** (German for "braking radiation").

Classical electrodynamics tells us that an accelerated charge radiates **electromagnetic waves** ([5.3.10](/5.3.10#sec-10.4)). A fast electron entering the target is strongly decelerated near the nuclei; each electron decelerates differently and so radiates at a different frequency, which is the origin of the continuous spectrum. The radiation depends mainly on the deceleration of the electron, so the shape of the continuous spectrum depends little on the target material; the larger the nuclear charge $Ze$, the larger the acceleration of the electron and the stronger the radiation. Empirically, the intensity per unit frequency interval is approximately (Kramers' formula)

$$
I_\nu\propto iZ(\nu_{\max}-\nu),\qquad \nu<\nu_{\max},
$$
where $i$ is the tube current. Bombarding a tungsten target with high-energy electrons from an electron accelerator produces very energetic "hard" X-rays.

Classical theory, however, cannot explain why the continuous spectrum has a short-wavelength limit independent of the target material: classically there is no definite upper bound relating the frequency of the radiation to the energy of the electron. The photon theory gives a simple explanation: the kinetic energy $eU$ of an electron can at most be converted entirely into the energy of one photon, that is, $h\nu_{\max}=eU$.

**Definition 5.1.2 (Cutoff Wavelength)** The short-wavelength limit of the continuous X-ray spectrum is called the **cutoff wavelength** (short-wavelength limit). From $h\nu_{\max}=eU$,

$$
\lambda_{\min}=\frac{c}{\nu_{\max}}=\frac{hc}{eU},
\tag{5.1}
$$
a relation known as the Duane–Hunt law.

Inserting the constants, $\lambda_{\min}=\dfrac{1.240\,\mathrm{nm}}{U/\mathrm{kV}}$; for $U=30\,\mathrm{kV}$, $\lambda_{\min}=0.0413\,\mathrm{nm}$. The cutoff wavelength depends only on the voltage and not on the target element. In 1915 Duane and Hunt measured $\lambda_{\min}$ as a function of $U$; the value of the **Planck constant** obtained from Eq. (5.1) agrees with that obtained from the **photoelectric effect**, showing the universality of $h$. For a time this was one of the most accurate methods of measuring $h$ ([5.5.1](/5.5.1#sec-1.1.5) mentions the 1921 measurement by Ye Qisun and others). The existence of the cutoff wavelength is another piece of evidence for the photon theory.

### 5.1.3. The Characteristic Spectrum and Moseley's Law

In 1906 Barkla found that the X-rays emitted by every element contain several components of different penetrating power, called, in order of decreasing penetrating power, the K, L, M, … series. After dispersion by a crystal, each series consists of several lines: the K series has $\mathrm{K}_\alpha$, $\mathrm{K}_\beta$, $\mathrm{K}_\gamma$, …, and the L series has $\mathrm{L}_\alpha$, $\mathrm{L}_\beta$, ….

**Definition 5.1.3 (Characteristic X-Ray)** The line spectrum of X-rays produced by transitions of inner electrons of an atom, with wavelengths determined by the element, is called **characteristic X-rays**.

The mechanism is as follows (in the language of the **electron shells** of [5.5.4](/5.5.4#sec-4.4.2)):

1. A fast electron knocks an electron out of the K shell ($n=1$) of a target atom, leaving a vacancy. This requires the energy of the incident electron to exceed the ionization energy of a K-shell electron, so below a certain threshold voltage there are no K-series lines (the threshold for molybdenum is $20.0\,\mathrm{keV}$, see the left of the figure above).
2. An outer electron makes a transition into this vacancy and emits a photon: a transition from the L shell ($n=2$) to the K shell emits the $\mathrm{K}_\alpha$ line, one from the M shell emits the $\mathrm{K}_\beta$ line, and so on; a vacancy in the L shell is filled by an electron from a still higher shell, emitting L-series lines.
3. Inner electrons are close to the nucleus, and the force on them is determined almost entirely by the nuclear charge and is independent of the chemical state of the atom. The positions of the characteristic lines are therefore determined by the element alone and change monotonically with atomic number, without periodicity.

An atom with a vacancy may also not emit light but instead give its energy to another outer electron and eject it (the Auger effect); this is the principle of Auger electron spectroscopy in surface analysis. Light elements decay mainly by the Auger process and heavy elements mainly by X-ray emission.

**Theorem 5.1.1 (Moseley's Law)** In 1913 Moseley measured the X-ray spectra of 38 elements from aluminum to gold and found that the frequency of the $\mathrm{K}_\alpha$ line and the atomic number $Z$ satisfy

$$
\sqrt{\nu_{\mathrm{K}_\alpha}}=0.496\times10^{8}\,\mathrm{Hz}^{1/2}\times(Z-1).
\tag{5.2}
$$

This law can be explained with the energy-level formula of a hydrogen-like ion (Theorem 4.1.2; for nuclear charge $Ze$ the levels are $-13.6\,\mathrm{eV}\cdot Z^2/n^2$). After a vacancy appears in the K shell, one electron remains there; the nuclear charge felt by the L electron making the transition is screened by this electron by about one unit, so the effective charge is about $(Z-1)e$. Thus

$$
h\nu_{\mathrm{K}_\alpha}\approx13.6\,\mathrm{eV}\times(Z-1)^2\Big(\frac1{1^2}-\frac1{2^2}\Big)=10.2\,\mathrm{eV}\times(Z-1)^2,
$$
that is, $\nu_{\mathrm{K}_\alpha}=\frac34R_\infty c\,(Z-1)^2$ and $\sqrt{\tfrac34R_\infty c}=4.97\times10^7\,\mathrm{Hz}^{1/2}$, in agreement with Eq. (5.2). For copper ($Z=29$), for example, the estimate is $8.0\,\mathrm{keV}$ (measured $8.05\,\mathrm{keV}$, $\lambda=0.154\,\mathrm{nm}$, the line most commonly used in X-ray diffraction). The deviation is larger for heavy elements (the estimate for tungsten is $54\,\mathrm{keV}$, the measured value $59.3\,\mathrm{keV}$) because the speeds of the inner electrons approach the speed of light and relativistic corrections are needed.

The significance of Moseley's law is that it shows that the atomic number $Z$ is not merely the ordinal number of an element in the periodic table but the positive charge of the nucleus (in units of $e$), which gave the arrangement of the periodic table a physical basis. Arranged by atomic mass, cobalt (58.93) and nickel (58.69) are in reversed order; Moseley's measurements confirmed that cobalt is number 27 and nickel number 28. He also pointed out that elements with $Z=43$, $61$ and $75$ had not yet been discovered; technetium, promethium and rhenium were later found. The characteristic spectrum depends only on the element and not on its chemical combination, which is precisely why it can be used for elemental analysis.

### 5.1.4. Applications of X-Rays

- Imaging: the penetrating power of X-rays varies with the density and atomic number of the material, which allows medical radiography, industrial flaw detection and customs inspection of cargo containers (container scanning can distinguish the declared cargo from the actual cargo). Computed tomography (CT) measures the attenuation of X-rays from many directions and reconstructs cross-sectional images from the projections; Hounsfield and Cormack received the 1979 Nobel Prize in Physiology or Medicine for it.
- Structure analysis: X-ray diffraction by crystals ([5.4.2](/5.4.2#sec-2.5)) determines crystal and molecular structures and is a basic tool in chemistry, materials science and structural biology.
- Composition analysis: a sample is excited by electrons, protons, α particles or X-rays, and the characteristic X-rays it emits are measured; the elements are identified from the energies of the lines (Moseley's law) and their amounts from the intensities. Excitation by protons is called particle-induced X-ray emission (PIXE) analysis; it has high sensitivity (below the $\mu\mathrm{g/g}$ level), needs only small samples, can analyze micro-regions from micrometers to millimeters, can measure many elements simultaneously and does not destroy the sample. The proton beam can be extracted from the accelerator into air, so the sample need not be placed in a vacuum. For example, PIXE analysis of the sword of King Goujian of Yue, excavated at Jiangling, Hubei, in 1965, showed that the blade consists mainly of copper and tin (with a little lead), that the iron content at the yellow patterns is far lower than in copper ore, and that the surface had been sulfurized, so that it has not rusted in more than two thousand years; the argon in the spectrum comes from the air. PIXE can also analyze trace elements (such as arsenic) in the human body from a few hairs.

## 5.2. Lasers

The word *laser* is an acronym for light amplification by stimulated emission of radiation, and its principle is stimulated emission. In 1954 Townes and coworkers first built a stimulated-emission amplifier for microwaves (the maser, using the ammonia transition at about $24\,\mathrm{GHz}$), and Basov and Prokhorov independently proposed the same principle; the three shared the 1964 Nobel Prize in Physics. In 1960 Maiman built the first laser (a ruby laser, wavelength $694.3\,\mathrm{nm}$), and in the same year Javan and coworkers built the first gas laser (the He–Ne laser).

### 5.2.1. Spontaneous Emission, Stimulated Absorption and Stimulated Emission

Consider two energy levels of an atom, $E_1<E_2$, and let $N_1$ and $N_2$ be the numbers of atoms per unit volume in these two levels. There are three kinds of interaction processes between the atoms and radiation of frequency $\nu=(E_2-E_1)/h$.

**Definition 5.2.1 (Spontaneous Emission)** An atom in the excited state $E_2$ spontaneously makes a transition to the lower level $E_1$ without external influence, emitting a photon of energy $h\nu=E_2-E_1$; this process is called **spontaneous emission**. The number of atoms undergoing spontaneous emission per unit volume per unit time is

$$
\Big(\frac{\mathrm{d}N_2}{\mathrm{d}t}\Big)_{\mathrm{sp}}=-A_{21}N_2,
$$
and the coefficient $A_{21}$, the probability per unit time that an atom undergoes spontaneous emission, is called the spontaneous emission coefficient.

The spontaneous emissions of individual atoms are independent random processes, and the phase, **polarization** and direction of propagation of the emitted photons are random, so the light from spontaneous emission is not **coherent light**. Ordinary light sources emit mainly by spontaneous emission ([5.4.1](/5.4.1#sec-1.2.1)).

With spontaneous emission alone, $N_2(t)=N_2(0)\,\mathrm{e}^{-A_{21}t}$. Hence the time an atom stays in $E_2$ follows an **exponential distribution** with parameter $A_{21}$, and the mean residence time is

$$
\tau=\frac{1}{N_2(0)}\int_0^\infty t\,\Big(-\frac{\mathrm{d}N_2}{\mathrm{d}t}\Big)\mathrm{d}t=\int_0^\infty tA_{21}\mathrm{e}^{-A_{21}t}\,\mathrm{d}t=\frac1{A_{21}},
$$
which is also the time for $N_2$ to fall to $1/\mathrm{e}$ of its initial value and is called the lifetime of the level $E_2$. The lifetime of a typical excited state is about $10^{-8}\,\mathrm{s}$; by the energy–time **Heisenberg uncertainty relation**, a finite lifetime gives the level a width, which determines the natural width of the spectral line ([5.5.2](/5.5.2#sec-2.3)).

**Definition 5.2.2 (Stimulated Absorption)** An atom in the lower level $E_1$ absorbs a photon of energy $h\nu=E_2-E_1$ and makes a transition to $E_2$; this process is called **stimulated absorption** (or simply absorption). Let $u_\nu$ be the energy density of the incident radiation per unit frequency interval near the frequency $\nu$; the number of atoms undergoing absorption per unit volume per unit time is

$$
\Big(\frac{\mathrm{d}N_1}{\mathrm{d}t}\Big)_{\mathrm{ab}}=-B_{12}u_\nu N_1,
$$
where $B_{12}u_\nu$ is the probability per unit time that an atom absorbs, and $B_{12}$ is called the absorption coefficient.

**Definition 5.2.3 (Stimulated Emission)** An atom in the excited state $E_2$, under the action of an external photon of energy $h\nu=E_2-E_1$, makes a transition to $E_1$ and emits a photon with the same frequency, phase, polarization direction and direction of propagation as the incident photon; this process is called **stimulated emission**. The number of atoms undergoing stimulated emission per unit volume per unit time is

$$
\Big(\frac{\mathrm{d}N_2}{\mathrm{d}t}\Big)_{\mathrm{st}}=-B_{21}u_\nu N_2,
$$
where $B_{21}$ is called the stimulated emission coefficient.

In stimulated emission one incident photon becomes two identical photons, which in turn cause stimulated emission and become four, eight, …; stimulated emission therefore amplifies light, and the amplified light is coherent. In quantum language, photons are **bosons**, and stimulated emission is precisely a manifestation of the tendency of bosons to cluster in the same state ([5.5.4](/5.5.4#sec-4.3.2)).

### 5.2.2. The Einstein Coefficients

**Definition 5.2.4 (Einstein Coefficients)** The spontaneous emission coefficient $A_{21}$, the stimulated emission coefficient $B_{21}$ and the absorption coefficient $B_{12}$ are collectively called the **Einstein coefficients**. They are determined by the properties of the atom alone and are independent of the radiation field and of the temperature.

In studying the thermal equilibrium of atoms with **black body** radiation, Einstein found that with only spontaneous emission and absorption, atoms and radiation cannot reach the equilibrium described by **Planck's law**; stimulated emission must also exist. Let the atoms coexist with equilibrium radiation at temperature $T$; in equilibrium the numbers of upward and downward transitions are equal:

$$
B_{12}u_\nu N_1=A_{21}N_2+B_{21}u_\nu N_2.
$$
In equilibrium the distribution of atoms over the levels obeys the **Boltzmann distribution** ([5.2.1](/5.2.1#sec-1.7)); if neither level has **degeneracy**, $N_2/N_1=\mathrm{e}^{-h\nu/(k_{\mathrm{B}}T)}$, so that

$$
u_\nu=\frac{A_{21}/B_{21}}{(B_{12}/B_{21})\,\mathrm{e}^{h\nu/(k_{\mathrm{B}}T)}-1}.
$$
On the other hand, the spectral energy density of equilibrium radiation, $u_\nu=\frac4cM_\nu$, is given by Planck's law (Eq. (1.5)):

$$
u_\nu=\frac{8\pi h\nu^3}{c^3}\,\frac1{\mathrm{e}^{h\nu/(k_{\mathrm{B}}T)}-1}.
$$
The two expressions must agree at all temperatures, which requires

**Theorem 5.2.1 (Einstein Relations)** For two nondegenerate levels,

$$
B_{12}=B_{21},\qquad A_{21}=\frac{8\pi h\nu^3}{c^3}\,B_{21}.
\tag{5.3}
$$
If the levels have degeneracies $g_1$ and $g_2$, the first relation becomes $g_1B_{12}=g_2B_{21}$.

This derivation conversely gives a concise proof of Planck's law. Eq. (5.3) has several consequences:

- Only one of the three coefficients is independent: a transition with strong spontaneous emission also has strong stimulated emission and absorption.
- In a radiation field in thermal equilibrium, the ratio of the rates of spontaneous and stimulated emission is $\frac{A_{21}}{B_{21}u_\nu}=\mathrm{e}^{h\nu/(k_{\mathrm{B}}T)}-1$. For visible light ($h\nu\approx2\,\mathrm{eV}$) this ratio is about $2\times10^3$ even in a filament at $3000\,\mathrm{K}$, so ordinary light sources emit mainly by spontaneous emission; in the microwave region $h\nu\ll k_{\mathrm{B}}T$, and stimulated emission actually dominates, which is one reason the maser appeared before the laser.
- $A_{21}/B_{21}\propto\nu^3$: the higher the frequency, the stronger spontaneous emission is relatively, and the harder it is for stimulated emission to dominate; this is why X-ray lasers are much harder to realize than visible-light lasers.

### 5.2.3. Population Inversion

When light of frequency $\nu$ passes through a system of atoms, stimulated emission strengthens it and absorption weakens it. The net effect of the two is proportional to

$$
B_{21}u_\nu N_2-B_{12}u_\nu N_1=B_{21}u_\nu(N_2-N_1)
$$
(for the nondegenerate case). For the light to be amplified we need $N_2>N_1$.

**Definition 5.2.5 (Population Inversion)** A state in which there are more atoms in the upper level than in the lower level ($N_2>N_1$) is called **population inversion**. A material in which population inversion can be achieved, and light thus amplified, is called an active material (gain medium).

This is impossible in thermal equilibrium: by the **Boltzmann factor**, $N_2/N_1=\mathrm{e}^{-(E_2-E_1)/(k_{\mathrm{B}}T)}<1$; for the $632.8\,\mathrm{nm}$ line of the He–Ne laser ($h\nu=1.96\,\mathrm{eV}$) this ratio is about $10^{-33}$ at room temperature. A population-inverted state is a nonequilibrium state, formally corresponding to a "negative temperature". To achieve it, energy from outside must continuously excite atoms to the upper level; this is called pumping. Pumping methods include optical excitation, electron collisions in a gas discharge, collisions between atoms, chemical reactions and current injection (semiconductor lasers, [5.5.6](/5.5.6)).

With only two levels, optical pumping can at best bring $N_2$ close to $N_1$ (stimulated absorption and stimulated emission have equal probabilities) and cannot produce inversion. An active material should therefore satisfy:

- Three or more energy levels take part in the process.
- The upper laser level is a metastable state, so that atoms can accumulate there.
- The lower laser level is not the ground state, and its spontaneous decay to still lower levels is fast, so that atoms leave the lower level in time (a four-level system). The lower level of the ruby laser is the ground state, making it a three-level system in which more than half of the atoms must be pumped up, so it can operate only in pulses; the He–Ne laser and the neodymium-doped yttrium aluminum garnet (Nd:YAG) laser are four-level systems, in which inversion is easily achieved.

**Definition 5.2.6 (Metastable State)** An excited state whose lifetime is far longer than that of an ordinary excited state (about $10^{-8}\,\mathrm{s}$) is called a **metastable state**; its lifetime can reach $10^{-3}\,\mathrm{s}$ or even longer. Its radiative transitions to lower levels are restricted by selection rules (§5.3.2) and have very small probability.

### 5.2.4. The He–Ne Laser

The main body of a He–Ne laser is a discharge capillary filled with a mixture of helium and neon (partial-pressure ratio about $5:1$ to $10:1$), with mirrors at both ends (internal-mirror type) or sealed with Brewster windows and mirrors outside the tube (external-mirror type, which gives **linearly polarized light**, see [5.4.3](/5.4.3)). Neon is the active material and helium the auxiliary material. It operates as follows (figure below):

1. Electron collisions in the discharge excite helium atoms to $2\,{}^3\mathrm{S}_1$ ($19.82\,\mathrm{eV}$) and $2\,{}^1\mathrm{S}_0$ ($20.62\,\mathrm{eV}$). Radiative transitions from these two levels to the ground state $1\,{}^1\mathrm{S}_0$ are forbidden, so they are metastable states and a large number of helium atoms accumulate in them.
2. The 5s and 4s levels of neon (that is, the configurations $2\mathrm{p}^55\mathrm{s}$ and $2\mathrm{p}^54\mathrm{s}$) have almost exactly the same energies as these two helium levels. When an excited helium atom collides with a ground-state neon atom, resonant energy transfer takes place: the helium returns to the ground state and the neon is excited to 5s or 4s. The 5s and 4s levels of neon are also metastable, with lifetimes much longer than those of the lower levels 4p and 3p, so population inversion is established.
3. Laser light is produced between 5s, 4s and 4p, 3p; the three strongest lines are

   | Transition | Wavelength | Region |
   |---|---|---|
   | 5s → 3p | $632.8\,\mathrm{nm}$ | red |
   | 4s → 3p | $1.15\,\mu\mathrm{m}$ | near infrared |
   | 5s → 4p | $3.39\,\mu\mathrm{m}$ | infrared |

   All of them occur between a metastable level and a level that is neither metastable nor the ground state, so inversion is easily achieved. Multilayer dielectric mirrors with high reflectivity at one wavelength select the desired line (the $3.39\,\mu\mathrm{m}$ and $632.8\,\mathrm{nm}$ lines share an upper level, and the former must be suppressed).
4. The 3p level quickly decays by spontaneous emission to 3s, which is metastable; neon atoms return to the ground state mainly by giving their energy to the tube wall in collisions (a nonradiative transition). The discharge tube is made very thin to increase collisions with the wall and empty the 3s level in time, thereby indirectly emptying the lower laser level.

![Relevant energy levels of the He–Ne laser (energies measured from the respective ground states; the vertical axis is broken below 16 eV): electron collisions in the discharge excite the two metastable states of helium, collisions transfer the energy resonantly to the 5s and 4s levels of neon, the red, orange and violet arrows are the three main laser transitions, and spontaneous emission 3p → 3s together with nonradiative de-excitation of 3s at the tube wall keeps the lower levels empty](./plots/he-ne-levels.py)

### 5.2.5. Optical Resonators: Longitudinal and Transverse Modes

In an active material in which population inversion has been achieved, stimulated emission triggered by spontaneous emission propagates in all directions, the distance over which it is amplified is short, and no strong light can form. Placing a pair of parallel mirrors at the two ends of the active material, one a fully reflecting mirror and the other a partially reflecting mirror (the output coupler), makes up an optical resonator.

**Definition 5.2.7 (Optical Resonator)** A device made of two (or more) mirrors that makes light pass through the active material many times back and forth along a definite direction is called an **optical resonator**.

Light propagating along the cavity axis travels back and forth between the two mirrors, is repeatedly amplified as it passes through the active material and builds up into an optical oscillation; light off the axis quickly escapes from the cavity and cannot be amplified continuously. Oscillation can be sustained only if the gain in one round trip exceeds the losses (transmission through the partial mirror, scattering, absorption). Let the reflectivities of the two mirrors be $R_1$ and $R_2$, the single-pass gain coefficient $G$ and the cavity length $L$; the threshold condition is $R_1R_2\mathrm{e}^{2GL}\ge1$. The functions of the resonator are:

- to make the light exit along the axis, which gives laser light its excellent directionality;
- to effectively lengthen the active material and enhance the amplification;
- to select frequencies, which gives laser light its excellent monochromaticity.

**Definition 5.2.8 (Longitudinal Mode)** As light travels back and forth in the resonator, only light satisfying the condition for constructive interference can build up a stable oscillation. Each stable optical oscillation (standing wave) formed along the axis of the cavity is called a **longitudinal mode**.

Let the cavity length be $L$ and the **refractive index** of the medium in the cavity be $n$; the round-trip **optical path length** must be an integer multiple of the vacuum wavelength:

$$
2nL=q\lambda_q,\qquad \nu_q=\frac{qc}{2nL},\qquad q=1,2,3,\dots
$$
This is exactly the same as the condition for a **standing wave** on a string fixed at both ends ([2.5.4](/2.5.4#sec-4.1.3), [5.1.7](/5.1.7#sec-7.7)). The frequency spacing between adjacent longitudinal modes is

$$
\Delta\nu_q=\frac{c}{2nL}.
\tag{5.4}
$$
For $L=1\,\mathrm{m}$ and $n\approx1$, $\Delta\nu_q=1.5\times10^8\,\mathrm{Hz}$, while $q$ is about $3\times10^6$.

**Example 5.2.1 (Number of Longitudinal Modes in a He–Ne Laser)** The $632.8\,\mathrm{nm}$ line of neon is broadened by the **Doppler effect** of the thermal motion of the atoms, and its **spectral linewidth** is about $\Delta\nu=1.3\times10^9\,\mathrm{Hz}$. Only longitudinal modes lying on the gain curve, where the gain exceeds the loss, can start to oscillate. For a cavity length of $1\,\mathrm{m}$, the number of longitudinal modes that can exist is about

$$
N\approx\frac{\Delta\nu}{\Delta\nu_q}=\frac{1.3\times10^9}{1.5\times10^8}\approx8.
$$
Shortening the cavity to $0.1\,\mathrm{m}$ increases $\Delta\nu_q$ to $1.5\times10^9\,\mathrm{Hz}$, which exceeds the linewidth, so only one longitudinal mode remains within the gain curve, and a single-longitudinal-mode output is obtained (figure below).

![Longitudinal modes on the gain curve. Left: cavity length L = 1 m, mode spacing 150 MHz; about ten modes whose gain exceeds the threshold (dashed line) oscillate simultaneously. Right: L = 0.1 m, mode spacing 1.5 GHz is larger than the width of the gain curve, and only one mode oscillates](./plots/laser-modes.py)

The linewidth of a single-longitudinal-mode laser is determined by the quality of the resonator and is far smaller than the width of the atomic line. The linewidth of an ordinary single-mode He–Ne laser is of order $\mathrm{kHz}$ to $\mathrm{MHz}$ ($\Delta\nu/\nu\sim10^{-12}$–$10^{-9}$); with frequency stabilization on an atomic or molecular line and locking of the laser to a high-quality reference cavity, $\Delta\nu/\nu$ can reach $10^{-15}$ or even less, and such lasers are the basis of optical clocks and gravitational-wave detection. From the **coherence length** $L_{\mathrm{c}}\approx c/\Delta\nu$ of [5.4.1](/5.4.1#sec-1.3.3), a laser with a linewidth of $1\,\mathrm{MHz}$ has a coherence length of about $300\,\mathrm{m}$, whereas ordinary light sources have only micrometers to millimeters.

**Definition 5.2.9 (Transverse Mode)** The stable distribution of laser intensity over a cross section perpendicular to the cavity axis is called the **transverse mode**, denoted $\mathrm{TEM}_{mn}$. It is caused mainly by diffraction at the edges of the mirrors and by the diversity of the initial spontaneous emission.

The intensity distribution of the lowest-order fundamental transverse mode $\mathrm{TEM}_{00}$ is a centrally symmetric Gaussian without nodal lines; higher-order transverse modes have dark lines or rings in the cross section, and the light spot splits into several parts. The fundamental mode has high brightness, small divergence (about $\lambda/(\pi w_0)$, with $w_0$ the beam waist radius) and the best **spatial coherence**; practical lasers often use a pinhole aperture or similar means to let only the fundamental mode oscillate.

### 5.2.6. Components and Properties of Lasers

A laser consists of three basic parts:

| Component | Function |
|---|---|
| Active material | has a suitable level structure (at least three levels) and can achieve population inversion |
| Excitation source (pump) | excites atoms and maintains population inversion |
| Optical resonator | provides positive feedback so that the light is amplified many times; selects direction and frequency, giving the laser good directionality and monochromaticity |

Compared with ordinary light sources, lasers have four features: good directionality, good monochromaticity, good coherence and high brightness. All of them come from stimulated emission and the resonator: a large number of photons are in the same quantum state. Lasers have wide applications in precision measurement (length measurement by **interference**, optical clocks, gravitational-wave detection), communications (optical fiber), machining (welding, cutting, photolithography), medicine (eye surgery), information storage (optical discs) and fundamental research (laser cooling of atoms, **Bose–Einstein condensation**).

## 5.3. Molecular Spectra

### 5.3.1. Structure of Molecular Energy Levels

Molecules can be excited by electric discharge, combustion and arcs, or illumination. Unlike the line spectra of atoms, molecular spectra appear in instruments of moderate resolution as groups of "bands", each band consisting of many closely spaced lines, and several bands together form a band system.

**Definition 5.3.1 (Molecular Spectrum)** The spectrum emitted or absorbed by a molecule in transitions between energy levels is called a **molecular spectrum**. A molecular spectrum made up of a large number of closely spaced lines appearing in groups is called a **band spectrum**.

The band structure arises because, besides the motion of the electrons, a molecule has the relative vibration of the nuclei and the rotation of the molecule as a whole. Nuclei are much heavier than electrons (mass ratio $M/m_{\mathrm{e}}\sim10^3$–$10^5$) and move much more slowly, so the three motions can be treated approximately separately (the Born–Oppenheimer approximation), and the energy of the molecule is

$$
E=E_{\mathrm{e}}+E_{\mathrm{v}}+E_{\mathrm{r}},
$$
the electronic, vibrational and rotational energies, respectively. Their level spacings differ greatly, roughly in the ratio $1:(m_{\mathrm{e}}/M)^{1/2}:(m_{\mathrm{e}}/M)$:

| Motion | Level spacing | Spectral region | Wave number commonly used in spectroscopy |
|---|---|---|---|
| Electronic (transitions of outer electrons) | $1$–$10\,\mathrm{eV}$ | visible, ultraviolet | $10^4$–$10^5\,\mathrm{cm^{-1}}$ |
| Vibrational | $0.05$–$0.5\,\mathrm{eV}$ | near and mid infrared ($2.5$–$25\,\mu\mathrm{m}$) | $400$–$4000\,\mathrm{cm^{-1}}$ |
| Rotational | $10^{-5}$–$10^{-2}\,\mathrm{eV}$ | far infrared, microwave | $0.1$–$100\,\mathrm{cm^{-1}}$ |

Spectroscopy commonly expresses line positions by the wave number $\tilde\nu=1/\lambda=\nu/c$, conventionally in $\mathrm{cm^{-1}}$ ($1\,\mathrm{cm^{-1}}$ corresponds to $1.24\times10^{-4}\,\mathrm{eV}$, or $30\,\mathrm{GHz}$). In what follows we take diatomic molecules as the example.

### 5.3.2. Rotational Levels and Rotational Spectra

Regard a diatomic molecule as a rigid dumbbell (rigid rotor) with the two nuclei a distance $r_0$ apart, rotating about an axis through the center of mass perpendicular to the bond axis. Its **moment of inertia** is $I=m_1r_1^2+m_2r_2^2=\mu r_0^2$, where $\mu=m_1m_2/(m_1+m_2)$ is the **reduced mass**. The classical rotational energy is $E_{\mathrm{r}}=\frac{L^2}{2I}$. In quantum mechanics the **eigenvalue** of the square of the **angular momentum** is $J(J+1)\hbar^2$ (Theorem 4.1.1), so

**Formula 5.3.1 (Energy Levels of the Rigid Rotor)**

$$
E_{\mathrm{r}}=\frac{\hbar^2}{2I}\,J(J+1)=hc\tilde B\,J(J+1),\qquad J=0,1,2,\dots,\qquad \tilde B=\frac{h}{8\pi^2cI},
\tag{5.5}
$$
where $\tilde B$ is called the rotational constant (expressed as a wave number). Each level has a **degeneracy** of $2J+1$.

**Remark 5.3.1** For molecular spectra we follow the IUPAC and chemistry convention: the rotational quantum number is written $J$ and the moment of inertia $I$; in the chapters on mechanics the moment of inertia is written $J$.

Transitions cannot take place between arbitrary pairs of levels.

**Definition 5.3.2 (Selection Rule)** The conditions given by quantum mechanics that determine whether a (electric dipole) radiative transition between two states can occur are called **selection rules**. Transitions that do not satisfy the selection rules are called forbidden transitions and have very small probability.

The selection rule for the rigid rotor is $\Delta J=\pm1$, and the molecule must have a permanent **electric dipole moment**: $\ce{HCl}$ and $\ce{CO}$ have pure rotational spectra, whereas homonuclear diatomic molecules such as $\ce{H2}$, $\ce{N2}$ and $\ce{O2}$ do not. The wave number of the absorption line from $J$ to $J+1$ is

$$
\tilde\nu=\frac{E_{\mathrm{r}}(J+1)-E_{\mathrm{r}}(J)}{hc}=2\tilde B(J+1),
$$
so the lines form an equally spaced series with spacing $2\tilde B$. Measuring the line spacing gives the moment of inertia and hence the bond length.

**Example 5.3.1 (Bond Length of HCl)** For $\mathrm{H}{}^{35}\mathrm{Cl}$ the rotational constant is $\tilde B=10.59\,\mathrm{cm^{-1}}$, and the line spacing is $2\tilde B=21.2\,\mathrm{cm^{-1}}$ (energy $2.6\times10^{-3}\,\mathrm{eV}$, in the far infrared). From $I=h/(8\pi^2c\tilde B)=2.64\times10^{-47}\,\mathrm{kg\,m^2}$ and $\mu=0.980\,\mathrm{u}$ we obtain $r_0=\sqrt{I/\mu}=127\,\mathrm{pm}$.

### 5.3.3. Vibrational Levels and Rovibrational Spectra

The vibration of the nuclei about the equilibrium separation $r_0$ can be regarded as **simple harmonic motion** at small amplitude (expanding the **potential energy curve** to second order near its minimum), and the levels are those of the **quantum harmonic oscillator** (Eq. (3.10)):

**Formula 5.3.2 (Vibrational Levels of a Diatomic Molecule)**

$$
E_{\mathrm{v}}=\Big(v+\frac12\Big)h\nu_0=\Big(v+\frac12\Big)hc\tilde\nu_0,\qquad v=0,1,2,\dots,
\tag{5.6}
$$
where $v$ is the vibrational quantum number (the notation standard in the chemistry literature), $\nu_0=\frac1{2\pi}\sqrt{k/\mu}$ is the classical vibration frequency, and $k$ is the force constant of the chemical bond.

The selection rule of the harmonic oscillator is $\Delta v=\pm1$, and the electric dipole moment of the molecule must change during the vibration (infrared activity). The vibrational spectrum of a harmonic oscillator therefore has only one line, $\tilde\nu=\tilde\nu_0$. The actual potential energy curve is not a parabola (bonds can break), so the level spacing decreases as $v$ increases, and weak overtone bands with $\Delta v=\pm2,\pm3,\dots$ appear. At room temperature $k_{\mathrm{B}}T\approx0.026\,\mathrm{eV}$ is much smaller than a vibrational quantum, and almost all molecules are in $v=0$ ([5.5.3](/5.5.3#sec-3.4.2)), so the absorption spectrum is dominated by the fundamental band $v=0\to1$. For $\ce{HCl}$, for example, the fundamental is at about $2886\,\mathrm{cm^{-1}}$ ($3.47\,\mu\mathrm{m}$, $0.36\,\mathrm{eV}$).

In a vibrational transition the rotational state changes at the same time ($\Delta J=\pm1$), so a single vibrational line splits into a group of rotational lines, forming a rovibrational band:

$$
\tilde\nu\approx\tilde\nu_0+2\tilde B m,\qquad m=\pm1,\pm2,\dots
$$
The lines with $\Delta J=+1$ ($m=J+1$) form the R branch and those with $\Delta J=-1$ ($m=-J$) the P branch; there is no line at $m=0$ (the band center). The intensity of each line is proportional to the population of the initial state, which by the **Boltzmann distribution** is $(2J+1)\mathrm{e}^{-hc\tilde B\,J(J+1)/(k_{\mathrm{B}}T)}$, strongest at $J\approx\sqrt{k_{\mathrm{B}}T/(2hc\tilde B)}-\frac12$. Because the mean bond length is slightly larger in the excited vibrational state, the rotational constant is slightly smaller, so the lines of the R branch become denser and those of the P branch sparser (figure below).

![Absorption spectrum of the fundamental rovibrational band of HCl at 300 K (line positions and relative intensities computed from the level formulas and the Boltzmann distribution): there is no line at the band center, 2886 cm⁻¹; on both sides are the P and R branches with spacing about 2B̃ ≈ 21 cm⁻¹, and the strongest lines correspond to J ≈ 3](./plots/rovibrational-spectrum.py)

Vibrational spectra are one of the main means of identifying molecular structure in chemistry: different functional groups ($\ce{O-H}$, $\ce{C=O}$, $\ce{C-H}$, etc.) have their own characteristic vibrational frequencies, which is the basis of infrared spectroscopy. The rovibrational absorption bands of molecules such as $\ce{H2O}$ and $\ce{CO2}$ in the atmosphere absorb infrared radiation from the ground and cause the greenhouse effect; in the wavelength ranges where their absorption is weak (about $0.3$–$2.5\,\mu\mathrm{m}$, $3.2$–$4.8\,\mu\mathrm{m}$ and $8$–$13\,\mu\mathrm{m}$), electromagnetic waves pass through the atmosphere well; these ranges are called "atmospheric windows" and are exploited in remote sensing and infrared astronomy.

### 5.3.4. Electronic Spectra and Band Spectra

Electronic transitions have the largest energies, in the visible and ultraviolet. In an electronic transition the vibrational and rotational states also change simultaneously, so one electronic transition corresponds to many vibrational bands (for different $v'\to v''$), and each vibrational band consists of many rotational lines:

- the electronic levels determine the position of the band system (group A, group B, …);
- the vibrational levels determine the positions of the individual bands within the system;
- the rotational levels determine the lines within each band, which are so close that they merge at low resolution, forming a band spectrum.

The spectra of the three kinds of motion are interwoven and quite complex, but they also contain a great deal of information on molecular structure. From microwaves to γ rays, the electromagnetic radiation in each region corresponds to a different kind of transition:

| Region | Main source |
|---|---|
| Microwave, far infrared | molecular rotation |
| Mid and near infrared | molecular vibration |
| Visible, ultraviolet | transitions of outer electrons of atoms and molecules |
| X-rays | transitions of inner electrons of atoms, bremsstrahlung |
| γ rays | transitions between nuclear energy levels |

## Summary

| Topic | Key points |
|---|---|
| X-ray continuous spectrum | bremsstrahlung; cutoff wavelength $\lambda_{\min}=hc/(eU)$, depending only on the voltage |
| X-ray characteristic spectrum | transitions of inner electrons, K, L, M series; Moseley's law $\sqrt{\nu_{\mathrm{K}_\alpha}}\propto Z-1$, $h\nu_{\mathrm{K}_\alpha}\approx10.2\,\mathrm{eV}\,(Z-1)^2$ |
| Three transition processes | spontaneous emission $A_{21}N_2$ (incoherent), absorption $B_{12}u_\nu N_1$, stimulated emission $B_{21}u_\nu N_2$ (coherent, amplifies light) |
| Einstein relations | $g_1B_{12}=g_2B_{21}$, $A_{21}=\frac{8\pi h\nu^3}{c^3}B_{21}$ |
| Conditions for lasing | population inversion (three- or four-level systems, metastable states, pumping); gain exceeding loss |
| Optical resonator | longitudinal modes $\nu_q=qc/(2nL)$, spacing $c/(2nL)$; transverse modes $\mathrm{TEM}_{mn}$ |
| Molecular levels | $E=E_{\mathrm{e}}+E_{\mathrm{v}}+E_{\mathrm{r}}$; $E_{\mathrm{v}}=(v+\frac12)h\nu_0$, $\Delta v=\pm1$; $E_{\mathrm{r}}=hc\tilde B\,J(J+1)$, $\Delta J=\pm1$ |

## Questions

1. Why does raising the voltage of an X-ray tube shorten the cutoff wavelength of the continuous spectrum without changing the wavelengths of the characteristic lines?
   Hint: the cutoff wavelength is determined by the conversion of the entire kinetic energy of one electron into one photon; the wavelengths of the characteristic lines are determined by the differences between inner levels of the target atom.
2. Use Moseley's law to estimate the wavelength of the $\mathrm{K}_\alpha$ line of iron ($Z=26$).
   Answer: $h\nu\approx10.2\,\mathrm{eV}\times25^2=6.4\,\mathrm{keV}$, $\lambda\approx0.194\,\mathrm{nm}$ (measured $0.194\,\mathrm{nm}$).
3. Why can population inversion not be achieved in a two-level system by optical pumping?
   Hint: the pump light causes absorption and stimulated emission alike, $B_{12}=B_{21}$, so the stronger the pumping, the closer $N_2$ approaches $N_1$, but it cannot exceed it.
4. Where does the monochromaticity of laser light come from? Why does shortening the cavity give a single longitudinal mode?
   Hint: the mode spacing $c/(2nL)$ is inversely proportional to the cavity length; when it exceeds the width of the gain curve, only one longitudinal mode can oscillate.
5. Why do $\ce{N2}$ and $\ce{O2}$ not absorb infrared radiation, whereas $\ce{CO2}$ and $\ce{H2O}$ are greenhouse gases?
   Hint: in a homonuclear diatomic molecule the electric dipole moment stays zero during vibration, so there is no infrared activity; the antisymmetric stretching and bending vibrations of $\ce{CO2}$ and all the vibrations of $\ce{H2O}$ change the dipole moment.
