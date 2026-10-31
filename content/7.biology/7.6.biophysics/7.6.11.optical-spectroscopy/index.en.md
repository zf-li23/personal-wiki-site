---
title: "Optical Spectroscopy: Absorption, Circular Dichroism, Vibrational Spectroscopy and Fluorescence"
description: "The physics of optical spectroscopy of biological macromolecules. Light and matter: the classical oscillator and the complex refractive index, the Beer–Lambert law and the absorption cross-section, transition dipole moments, Fermi's golden rule, dipole and oscillator strengths, the Franck–Condon principle and Poisson progressions, the Jablonski diagram, line shapes. UV–visible absorption: π systems and chromophores, solvent and pH effects, ε280 of proteins, hypochromism and two-state DNA melting, exciton coupling of chromophores (H and J aggregates, CD couplets). Optical activity: circular birefringence, ORD and the Cotton effect, ellipticity and molar ellipticity, rotational strength, far-UV CD and secondary structure by constrained least squares, near-UV CD, nucleic acids. Vibrational spectroscopy: normal modes and the infrared selection rule, Raman scattering and its selection rule, anti-Stokes intensities, depolarization, resonance Raman, amide bands and secondary structure, second-derivative and band-fitting analysis, ATR and infrared dichroism. Fluorescence: excited-state kinetics, solvent relaxation and the Lippert–Mataga equation, tryptophan fluorescence, Stern–Volmer and Lehrer analysis of quenching, photoselection and the fundamental anisotropy, rotational diffusion and the Perrin equation, polarization binding assays, Förster theory of energy transfer, the orientation factor, probes and biosensors."
---

Light of wavelengths between about $180\,\mathrm{nm}$ and $25\,\mu\mathrm{m}$ interacts with the electrons and the nuclear vibrations of biological molecules. The resulting spectra are low in structural resolution, since a protein of several hundred residues gives a handful of broad bands, but they are fast, need micrograms of material, work in solution under any condition and follow changes from picoseconds to hours. Optical spectroscopy is therefore the everyday tool of molecular biophysics: absorbance gives concentrations and melting curves, circular dichroism gives secondary structure and stability, infrared and Raman spectra report hydrogen bonding and conformation, and fluorescence reports environment, mobility, binding and distance.

This chapter derives what each of these measurements sees from the physics of the interaction of light with molecules. It begins with the classical oscillator and the quantum description of a transition, with the transition dipole moment, the Franck–Condon principle and the kinetics of the excited state (11.1). UV–visible absorption is then applied to proteins and nucleic acids, including the coupling between neighboring chromophores that underlies hypochromism and exciton spectra (11.2). The difference in absorption of left and right circularly polarized light, circular dichroism, turns the helical arrangement of peptide groups into a spectrum (11.3). Infrared absorption and Raman scattering probe vibrations, above all the amide bands of the backbone (11.4). Fluorescence adds the time dimension: the lifetime and its quenching, the anisotropy and its decay by rotational diffusion, and Förster resonance energy transfer, the spectroscopic ruler (11.5). A comparison of the methods closes the chapter (11.6).

The instrumental side of these techniques was treated in analytical chemistry: UV–visible spectrophotometry and CD instruments in [6.4.9](/6.4.9), fluorometers, lifetime measurement and fluorescence microscopy in [6.4.10](/6.4.10), and infrared and Raman spectrometers in [6.4.11](/6.4.11); the quantum theory of radiative transitions is in [5.5.5](/5.5.5), polarized light and optical activity in [5.4.3](/5.4.3). They are used here and not repeated. The same physics continues in the next chapter ([7.6.12](/7.6.12)), where single molecules are observed by fluorescence, and returns in the energy transfer of photosynthesis and the photochemistry of vision ([7.6.18](/7.6.18)). Rotational diffusion, which sets the time scale of fluorescence anisotropy, was derived in [7.6.5](/7.6.5#sec-5.3.2), and the two-state thermodynamics used for melting curves in [7.6.8](/7.6.8).

## 11.1. Light and Matter

### 11.1.1. The Classical Oscillator: Dispersion and Absorption

The classical picture of absorption, due to Lorentz, already contains the main features of a spectrum. An electron of charge $-e$ and mass $m_{\mathrm{e}}$ bound to its equilibrium position by a restoring force $-m_{\mathrm{e}}\omega_0^2\boldsymbol{r}$ and damped by a friction $-m_{\mathrm{e}}\gamma\dot{\boldsymbol{r}}$ is driven by the electric field of a light wave $\boldsymbol{E} = \boldsymbol{E}_0\mathrm{e}^{-\mathrm{i}\omega t}$. Since the wavelength is much larger than a molecule, the field is uniform over it, and the magnetic force is negligible. The equation of motion

$$
\ddot{\boldsymbol{r}} + \gamma\dot{\boldsymbol{r}} + \omega_0^2\boldsymbol{r} = -\frac{e}{m_{\mathrm{e}}}\boldsymbol{E}_0\mathrm{e}^{-\mathrm{i}\omega t}
$$
has the steady-state solution $\boldsymbol{r} = -(e/m_{\mathrm{e}})\boldsymbol{E}/(\omega_0^2 - \omega^2 - \mathrm{i}\gamma\omega)$. Each oscillator carries the induced **electric dipole moment** $\boldsymbol{p} = -e\boldsymbol{r}$ (in the chemical literature dipole moments are usually written $\mu$; we follow the site convention $\boldsymbol{p}$), and $N$ oscillators per unit volume give the polarization $\boldsymbol{P} = N\boldsymbol{p} = \varepsilon_0\chi_{\mathrm{e}}\boldsymbol{E}$ with the complex susceptibility

$$
\chi_{\mathrm{e}}(\omega) = \frac{N\mathrm{e}^2}{\varepsilon_0m_{\mathrm{e}}}\,\frac{1}{\omega_0^2 - \omega^2 - \mathrm{i}\gamma\omega}.
$$

**Formula 11.1.1 (Complex Refractive Index of a Dilute Medium)** For $\lvert\chi_{\mathrm{e}}\rvert \ll 1$ the complex refractive index $\tilde n = \sqrt{1 + \chi_{\mathrm{e}}} \approx 1 + \chi_{\mathrm{e}}/2 = n + \mathrm{i}\kappa$ has the real and imaginary parts

$$
n(\omega) = 1 + \frac{N\mathrm{e}^2}{2\varepsilon_0m_{\mathrm{e}}}\,\frac{\omega_0^2 - \omega^2}{(\omega_0^2 - \omega^2)^2 + \gamma^2\omega^2}, \qquad
\kappa(\omega) = \frac{N\mathrm{e}^2}{2\varepsilon_0m_{\mathrm{e}}}\,\frac{\gamma\omega}{(\omega_0^2 - \omega^2)^2 + \gamma^2\omega^2}.
$$
A plane wave in the medium, $E_0\exp[\mathrm{i}(\tilde nk_0x - \omega t)]$ with $k_0 = \omega/c$, has its phase set by $n$ and its amplitude damped as $\mathrm{e}^{-\kappa k_0x}$, so the intensity decays with the absorption coefficient $\alpha = 2\kappa k_0 = 4\pi\kappa/\lambda_0$.

Near $\omega_0$, $\kappa$ is a Lorentzian of full width $\gamma$: the absorption band. The refractive index rises towards the band (normal dispersion), swings through the band in the opposite direction (anomalous dispersion) and returns to its background value on the far side. Absorption and dispersion are two aspects of one response function, and because the response is causal, each determines the other through the Kramers–Kronig relations; the same pair appears for circularly polarized light as circular dichroism and optical rotatory dispersion (11.3.1). Since every medium except vacuum contains oscillators, no material is transparent at all wavelengths: quartz cuvettes transmit from about $180\,\mathrm{nm}$ to the near infrared, and infrared cells are made of $\ce{CaF2}$, $\ce{BaF2}$ or $\ce{ZnSe}$.

### 11.1.2. The Beer–Lambert Law

**Theorem 11.1.1 (Beer–Lambert Law)** Let monochromatic, collimated light pass through a homogeneous, nonscattering solution of noninteracting absorbers at number density $N$, each of which removes photons with the cross-section $\sigma$, and let no other process (fluorescence reaching the detector, photochemistry, saturation) occur. Then the transmitted intensity after a path $l$ is $I = I_0\mathrm{e}^{-\sigma Nl}$, and the absorbance is

$$
A = \lg\frac{I_0}{I} = \varepsilon cl, \qquad \sigma = \frac{1000\ln 10}{N_{\mathrm{A}}}\,\varepsilon = 3.82\times10^{-21}\,\varepsilon\ \mathrm{cm^2}, \tag{11.1}
$$
with $c$ in $\mathrm{mol\,L^{-1}}$, $l$ in $\mathrm{cm}$ and the molar absorption coefficient $\varepsilon$ in $\mathrm{L\,mol^{-1}\,cm^{-1}}$.

**Proof** A slab of thickness $\mathrm{d}x$ and area $S$ contains $NS\,\mathrm{d}x$ absorbers whose total cross-section $\sigma NS\,\mathrm{d}x$ blocks the fraction $\sigma N\,\mathrm{d}x$ of the photons crossing it, so $\mathrm{d}I = -\sigma NI\,\mathrm{d}x$ and $I = I_0\mathrm{e}^{-\sigma Nl}$. With $N = N_{\mathrm{A}}c/1000$ (in $\mathrm{cm^{-3}}$, for $c$ in $\mathrm{mol\,L^{-1}}$) and $\ln(I_0/I) = \ln 10\cdot A$ gives $\varepsilon = \sigma N_{\mathrm{A}}/(1000\ln 10)$. $\square$

The cross-section makes the molecular meaning of $\varepsilon$ concrete. A strong dye with $\varepsilon = 1.5\times10^5\,\mathrm{L\,mol^{-1}\,cm^{-1}}$ has $\sigma = 5.7\times10^{-16}\,\mathrm{cm^2}$, an area of $(0.24\,\mathrm{nm})^2$, comparable to the size of its π system; tryptophan at $280\,\mathrm{nm}$ ($\varepsilon = 5600$) has $\sigma = 2\times10^{-17}\,\mathrm{cm^2}$. Absorbances of independent species add, $A = l\sum_i\varepsilon_ic_i$, which is the basis of multicomponent analysis. Deviations arise from scattering by aggregates (which adds an apparent absorbance growing as $\lambda^{-4}$, [7.6.9](/7.6.9)), from association of the absorbers at high concentration, from stray light at high absorbance and from polychromatic light; in practice absorbances between $0.1$ and about $1$ are measured, and the statistical treatment of photometric errors is in [6.4.9](/6.4.9#sec-9.4.5).

### 11.1.3. Transition Dipole Moments and Selection Rules

Quantum mechanically, light induces transitions between stationary states $\psi_i$ and $\psi_f$ of energies $E_i < E_f$. The coupling of the molecule to a uniform field $\boldsymbol{E}(t) = \boldsymbol{E}_0\cos\omega t$ is through its dipole moment operator $\hat{\boldsymbol{p}} = \sum_jq_j\hat{\boldsymbol{r}}_j$, the sum running over all electrons and nuclei, with the interaction energy

$$
\hat{H}'(t) = -\hat{\boldsymbol{p}}\cdot\boldsymbol{E}_0\cos\omega t.
$$
The operator is that of the permanent charge distribution of the molecule; an induced dipole, proportional to the field, would give an interaction quadratic in the field and describes scattering, not absorption (11.4.2).

**Definition 11.1.1 (Transition Dipole Moment)** The **transition dipole moment** of the transition $i \to f$ is the matrix element

$$
\boldsymbol{p}_{fi} = \langle\psi_f\rvert\hat{\boldsymbol{p}}\lvert\psi_i\rangle = \int\psi_f^*\,\hat{\boldsymbol{p}}\,\psi_i\,\mathrm{d}\tau.
$$
It is a vector fixed in the molecule; its length measures the strength of the transition and its direction the polarization of the light the transition absorbs or emits. A transition with $\boldsymbol{p}_{fi} = \boldsymbol{0}$ is (electric-dipole) forbidden.

Physically, the field mixes a little of $\psi_f$ into $\psi_i$; the superposition $\psi_i + c\,\psi_f\mathrm{e}^{-\mathrm{i}(E_f - E_i)t/\hbar}$ has a charge density that oscillates at the frequency $(E_f - E_i)/\hbar$ with the dipole amplitude $\boldsymbol{p}_{fi}$, and it is this oscillating dipole that exchanges energy with a resonant field.

**Theorem 11.1.2 (Absorption Rate)** To first order in time-dependent perturbation theory (Fermi's golden rule), the rate of the transition $i \to f$ induced by the field above is

$$
W_{i\to f} = \frac{\pi}{2\hbar^2}\,\lvert\boldsymbol{p}_{fi}\cdot\boldsymbol{E}_0\rvert^2\,g(\omega - \omega_{fi}), \qquad \omega_{fi} = (E_f - E_i)/\hbar,
$$
where $g$ is the normalized line-shape function of the transition ($\int g\,\mathrm{d}\omega = 1$; $\delta$-like for an isolated molecule, broadened in solution, 11.1.6). For an isotropic sample the orientational average $\langle\cos^2\theta\rangle = 1/3$ replaces $\lvert\boldsymbol{p}_{fi}\cdot\boldsymbol{E}_0\rvert^2$ by $\lvert\boldsymbol{p}_{fi}\rvert^2E_0^2/3$.

Three facts follow. First, the absorption of a molecule depends on its orientation as $\cos^2\theta$, where $\theta$ is the angle between $\boldsymbol{p}_{fi}$ and the polarization of the light; this photoselection is the basis of linear dichroism and fluorescence anisotropy (11.5.5). Second, the integrated absorption band measures $\lvert\boldsymbol{p}_{fi}\rvert^2$; the stimulated and spontaneous rates are fixed by the same matrix element through the **Einstein coefficients** ([5.5.5](/5.5.5)), so a strongly absorbing transition is also a fast emitter (11.5.1). Third, **selection rules** follow from symmetry: $\boldsymbol{p}_{fi}$ vanishes unless the product $\psi_f^*\hat{\boldsymbol{p}}\psi_i$ contains the totally symmetric representation of the molecular point group, and the operator does not act on spin, so transitions between states of different spin multiplicity (singlet to triplet) are forbidden as long as spin–orbit coupling is weak.

**Formula 11.1.2 (Dipole and Oscillator Strengths)** For a band measured in solution, the dipole strength and the oscillator strength are

$$
D = \lvert\boldsymbol{p}_{fi}\rvert^2 = 9.186\times10^{-3}\int\frac{\varepsilon(\tilde\nu)}{\tilde\nu}\,\mathrm{d}\tilde\nu\ \ \mathrm{D}^2, \qquad
f = 4.32\times10^{-9}\int\varepsilon(\tilde\nu)\,\mathrm{d}\tilde\nu,
$$
with $\varepsilon$ in $\mathrm{L\,mol^{-1}\,cm^{-1}}$ and the wavenumber $\tilde\nu$ in $\mathrm{cm^{-1}}$ ($1\,\mathrm{D} = 3.336\times10^{-30}\,\mathrm{C\,m}$; small corrections for the refractive index of the solvent are omitted).

The **oscillator strength** compares a transition with one classical electron oscillator ($f = 1$). The $\pi\to\pi^*$ band of the peptide group near $190\,\mathrm{nm}$ ($\varepsilon \approx 7000$ per residue, width about $5000\,\mathrm{cm^{-1}}$) has $f \approx 0.2$ and a transition dipole of about $3$ D; the strongly allowed bands of dyes reach $f \approx 1$, the $\mathrm{n}\to\pi^*$ band of the peptide group ($\varepsilon \approx 100$) has $f \approx 10^{-3}$.

### 11.1.4. Electronic and Vibrational Motion: The Franck–Condon Principle

The electronic bands of molecules in solution are broad, typically $3000$–$6000\,\mathrm{cm^{-1}}$, because every electronic transition is accompanied by vibrational transitions. Electrons move much faster than nuclei, so in the Born–Oppenheimer approximation the wavefunction factorizes into an electronic part, which depends parametrically on the nuclear coordinates $Q$, and a vibrational part $\chi_v(Q)$ that moves in the potential of the electronic state. If the electronic transition dipole $\boldsymbol{p}_{\mathrm{el}} = \langle\psi_{\mathrm{el}}'\rvert\hat{\boldsymbol{p}}\lvert\psi_{\mathrm{el}}\rangle$ depends little on $Q$ (the Condon approximation), then

$$
\boldsymbol{p}_{fi} = \boldsymbol{p}_{\mathrm{el}}\,\langle\chi_{v'}\vert\chi_v\rangle,
$$
and the intensity of the vibronic transition $v \to v'$ is proportional to the square of the overlap of the two vibrational wavefunctions.

**Definition 11.1.2 (Franck–Condon Factor)** The *Franck–Condon factor* of the vibronic transition $v \to v'$ is $\lvert\langle\chi_{v'}\vert\chi_v\rangle\rvert^2$. Its sum over all $v'$ is $1$, so the vibrational structure redistributes, but does not change, the total intensity of an electronic band.

This is the quantum form of the **Franck–Condon principle**: the electronic transition is so fast that the nuclei have the same positions and momenta just before and just after it, so the transition is vertical in a potential-energy diagram and leads to the vibrational levels of the upper state that overlap the initial vibrational wavefunction best. The excited state of a π system usually has longer, weaker bonds, its potential minimum is displaced, and the strongest vibronic line is not the $0$–$0$ line.

**Proposition 11.1.1 (Poisson Progression)** Let the ground and excited states have harmonic potentials of the same frequency $\omega$ in a coordinate $Q$, with minima displaced by $\Delta$ (in units of the zero-point amplitude $\sqrt{\hbar/m\omega}$). Then the Franck–Condon factors from $v = 0$ are

$$
\lvert\langle\chi_{v'}\vert\chi_0\rangle\rvert^2 = \mathrm{e}^{-S}\frac{S^{v'}}{v'!}, \qquad S = \frac{\Delta^2}{2},
$$
a Poisson distribution with mean $S$, the Huang–Rhys factor. The energy released by vibrational relaxation after a vertical transition, the reorganization energy, is $\lambda = S\hbar\omega$, and absorption and emission maxima are separated by approximately $2S\hbar\omega$ for $S \gg 1$.

**Proof** The ground-state wavefunction $\chi_0$ is a coherent state of the displaced oscillator; in the basis of the displaced oscillator it is $\mathrm{e}^{-\lvert\alpha\rvert^2/2}\sum_n(\alpha^n/\sqrt{n!})\chi_n'$ with $\alpha = -\Delta/\sqrt2$, so the squared coefficients are Poisson with mean $\lvert\alpha\rvert^2 = \Delta^2/2$. The potential energy of the excited state at the ground-state geometry exceeds its minimum by $\frac12m\omega^2(\Delta\sqrt{\hbar/m\omega})^2 = \frac12\Delta^2\hbar\omega = S\hbar\omega$, and the same amount is released in the ground state after emission, giving a total Stokes shift of $2S\hbar\omega$ between the vertical transitions. $\square$

![The Franck–Condon principle. A: potential curves of the ground state S0 and the excited state S1 with the same curvature and a displaced minimum; the ground-state v = 0 probability density (shaded) is reached vertically (absorption, black) and the excited state emits vertically from its own v' = 0 level (green). B: Franck–Condon factors of the Poisson progression for Huang–Rhys factors S = 0.3 (0–0 dominant, as in rigid aromatic dyes), 1 and 3 (broad, structureless bands). C: absorption and emission spectra built from the progression with S = 1, a vibrational quantum of 1400 cm⁻¹ and Gaussian broadening; they are mirror images about the 0–0 line, and their maxima are separated by the Stokes shift](./plots/franck-condon.py)

The proposition explains three empirical rules of molecular spectroscopy ([6.4.10](/6.4.10#sec-10.1.2)). The **Stokes shift**, the red shift of emission relative to absorption, is the reorganization energy paid twice, once in each electronic state, increased in polar solvents by solvent relaxation (11.5.2). The **mirror-image rule** holds when both states have the same vibrational frequencies, so that the progressions of absorption (to higher energy from the $0$–$0$ line) and emission (to lower energy) have the same Poisson weights. The width of a band reports how strongly the electronic excitation couples to nuclear motion: rigid, delocalized dyes have small $S$ and narrow, structured bands, whereas chromophores whose geometry changes on excitation, or that interact with polar solvent, have large $S$ and broad bands. Highly displaced excited states also tend to reach the ground-state potential surface at a crossing point, which opens fast radiationless decay; this is why flexible chromophores fluoresce weakly and become bright when they are immobilized, the basis of probes for amyloid fibrils (thioflavin T) and of the bright chromophore of **green fluorescent protein**, held rigid inside its β barrel.

### 11.1.5. The Fate of the Excited State: The Jablonski Diagram

After absorption, a molecule relaxes within about $10^{-12}\,\mathrm{s}$ to the lowest vibrational level of the lowest excited singlet state $\mathrm{S}_1$, by vibrational relaxation and internal conversion between singlet states. Because this is four or more orders of magnitude faster than emission, fluorescence comes from $\mathrm{S}_1$ whatever the excitation wavelength (**Kasha's rule**), and the emission spectrum does not depend on the excitation wavelength. From $\mathrm{S}_1$ several first-order processes compete; the **Jablonski diagram** summarizes them.

![Jablonski diagram of a fluorophore. Absorption (about 10⁻¹⁵ s) reaches vibrational levels of S1 or S2; vibrational relaxation and internal conversion (about 10⁻¹² s) bring the molecule to the lowest level of S1. From there fluorescence (radiative rate k_r of order 10⁸ s⁻¹), internal conversion (k_ic), intersystem crossing to the triplet T1 (k_isc), collisional quenching (k_q[Q]) and energy transfer to an acceptor (k_T) compete; the lifetime is the inverse of the sum of their rates and the quantum yield is k_r τ. The triplet decays by phosphorescence (10⁻³ to 10² s) or radiationlessly](./plots/jablonski.py)

**Formula 11.1.3 (Lifetime and Quantum Yield)** If the decay channels of $\mathrm{S}_1$ have first-order rate constants $k_{\mathrm{r}}$ (fluorescence), $k_{\mathrm{ic}}$, $k_{\mathrm{isc}}$, $k_{\mathrm{q}}[\ce{Q}]$ and $k_{\mathrm{T}}$, the population of $\mathrm{S}_1$ after a short pulse decays as $\mathrm{e}^{-t/\tau}$ with

$$
\tau = \frac{1}{k_{\mathrm{r}} + k_{\mathrm{ic}} + k_{\mathrm{isc}} + k_{\mathrm{q}}[\ce{Q}] + k_{\mathrm{T}}}, \qquad \Phi = k_{\mathrm{r}}\tau = \frac{\tau}{\tau_0}, \tag{11.2}
$$
where $\Phi$ is the fluorescence **quantum yield** and $\tau_0 = 1/k_{\mathrm{r}}$ the natural (radiative) lifetime.

Every additional pathway shortens the lifetime and lowers the yield in the same proportion, which is the principle behind the measurement of quenching (11.5.4) and of energy transfer (11.5.7) by lifetimes. The **fluorescence lifetime** of most organic fluorophores is $1$–$10\,\mathrm{ns}$, which sets the window of fluorescence: processes faster than the lifetime (solvent relaxation, local motions, rotation of small molecules) affect the emission, slower ones do not. Triplet states live microseconds to seconds; in single-molecule fluorescence they appear as dark intervals ("blinking", [7.6.12](/7.6.12)).

### 11.1.6. Band Positions, Widths and Shapes

A spectral band carries four kinds of information. Its position gives the energy gap and reports the environment of the chromophore (11.2.2). Its integrated intensity gives the dipole strength (Formula 11.1.2) and, at fixed band shape, the concentration. Its width reflects two kinds of broadening. *Homogeneous broadening* is the same for every molecule: the finite lifetime of the states gives each line a Lorentzian shape of full width $\Delta\tilde\nu = 1/(2\pi c\tau)$, which for an excited state of $1\,\mathrm{ns}$ is only $0.005\,\mathrm{cm^{-1}}$, but dephasing by collisions with solvent molecules in about $10^{-13}\,\mathrm{s}$ broadens lines to tens of $\mathrm{cm^{-1}}$. *Inhomogeneous broadening* arises because molecules in different local environments absorb at different frequencies; it gives Gaussian profiles and dominates in proteins and glasses. A convolution of the two, the Voigt profile, describes most bands; together with unresolved vibronic structure (Proposition 11.1.1) it makes electronic bands in solution a few thousand $\mathrm{cm^{-1}}$ wide and vibrational bands $10$–$30\,\mathrm{cm^{-1}}$ wide. The shape matters whenever overlapping bands are separated by fitting or derivatives (11.4.4).

## 11.2. Ultraviolet–Visible Absorption of Biomolecules

### 11.2.1. Electronic Transitions and Chromophores

In organic molecules the absorbing electrons are those of σ bonds, π bonds and nonbonding lone pairs (n). The σ and π systems interact weakly and can be treated separately. $\sigma\to\sigma^*$ transitions need the most energy and lie in the vacuum ultraviolet (ethane near $135\,\mathrm{nm}$). $\mathrm{n}\to\sigma^*$ transitions of saturated groups with heteroatoms ($\ce{-OH}$, $\ce{-NH2}$, $\ce{-SH}$) lie near $170$–$200\,\mathrm{nm}$. In the accessible range, above about $185\,\mathrm{nm}$ where oxygen and water begin to transmit, the bands of biological molecules are $\pi\to\pi^*$ and $\mathrm{n}\to\pi^*$ transitions of unsaturated groups, the **chromophores**. $\pi\to\pi^*$ bands are strong ($\varepsilon \sim 10^3$–$10^5$); $\mathrm{n}\to\pi^*$ bands are weak ($\varepsilon < 100$–$1000$), because the n orbital lies in the nodal plane of the π* orbital and the overlap of their charge distributions is small.

The energies of π systems follow from the Hückel model: for a linear polyene of $N$ conjugated carbon atoms the π orbital energies are $E_k = \alpha + 2\beta\cos[k\pi/(N + 1)]$, $k = 1, \dots, N$, with the resonance integral $\beta < 0$. For an even number of electrons the gap between the highest occupied and lowest unoccupied orbitals is $-4\beta\sin[\pi/(2(N + 1))]$, which falls as $1/N$; longer conjugation absorbs at longer wavelengths and more strongly. Real polyenes approach a finite gap of about $2\,\mathrm{eV}$, because alternation of single and double bonds keeps the π electrons partly localized; this is why the eleven conjugated double bonds of β-carotene absorb at $450\,\mathrm{nm}$ and the protonated Schiff base of retinal in **rhodopsin** absorbs near $500\,\mathrm{nm}$ only with the help of the protein environment ([7.6.18](/7.6.18)).

| Chromophore | Transition | $\lambda_{\max}$ / nm | $\varepsilon_{\max}$ / ($\mathrm{L\,mol^{-1}\,cm^{-1}}$) |
|---|---|---|---|
| Peptide group | $\mathrm{n}\to\pi^*$ | $\approx 220$ | $\approx 100$ |
| Peptide group | $\pi\to\pi^*$ | $\approx 190$ | $\approx 7000$ |
| Tryptophan | $\pi\to\pi^*$ ($^1\mathrm{L}_\mathrm{a}$, $^1\mathrm{L}_\mathrm{b}$) | $280$ ($219$) | $5600$ ($47\,000$) |
| Tyrosine | $\pi\to\pi^*$ | $274$ ($222$) | $1400$ ($8000$) |
| Phenylalanine | $\pi\to\pi^*$ | $257$ | $200$ |
| Cystine (disulfide) | $\mathrm{n}\to\sigma^*$ | $250$–$300$ (broad) | $\approx 125$ at $280$ |
| Nucleobases (average) | $\pi\to\pi^*$ | $\approx 260$ | $\approx 10^4$ per base |
| Heme (Soret band) | $\pi\to\pi^*$ | $\approx 410$–$430$ | $\approx 10^5$ |
| NADH (nicotinamide) | $\pi\to\pi^*$ | $340$ | $6220$ |
| FAD (isoalloxazine) | $\pi\to\pi^*$ | $450$ | $11\,300$ |

The table explains the standard practices of the laboratory. The peptide backbone absorbs far more strongly than any side chain, but at $190$–$220\,\mathrm{nm}$, where buffers and oxygen interfere; protein concentrations are therefore measured at $280\,\mathrm{nm}$ (11.2.3). NADH absorbs at $340\,\mathrm{nm}$ and $\ce{NAD+}$ does not, which is why dehydrogenase assays are read at $340\,\mathrm{nm}$. The Soret band of heme shifts with the ligation and oxidation state of the iron, and was the first window on the binding of oxygen and carbon monoxide to hemoglobin.

### 11.2.2. Environmental Effects: Solvent, pH and Neighboring Groups

The energy of a transition depends on how the environment stabilizes the ground and excited states. Most $\pi\to\pi^*$ excited states are more polar than the ground state, so polar solvents lower them more and shift the band to the red. In $\mathrm{n}\to\pi^*$ transitions the ground state is the more polar one and its lone pair accepts hydrogen bonds from protic solvents; the band shifts to the blue (by roughly the energy of a hydrogen bond) and weakens. Ionizable chromophores change their spectra with pH: the phenolate of tyrosine absorbs at $293\,\mathrm{nm}$ with $\varepsilon \approx 2400$, instead of $274\,\mathrm{nm}$ and $1400$ for the phenol ($\mathrm{p}K_{\mathrm{a}} \approx 10$), and spectrophotometric titration of a protein tells how many tyrosines are exposed and which are buried or hydrogen-bonded.

These shifts are small, a few nanometers, but they can be measured with high precision as difference spectra between two states of the same protein. Solvent perturbation spectroscopy compares a protein in buffer with the same protein in buffer containing $20\,\%$ ethylene glycol or sucrose: only chromophores accessible to the cosolvent shift, so the ratio of the difference spectrum to that of a model compound estimates the fraction of exposed tryptophans and tyrosines. Denaturation difference spectra, in which the aromatic bands shift by $2$–$3\,\mathrm{nm}$ to the blue on unfolding as the chromophores move from the hydrophobic interior into water, are an inexpensive way to follow unfolding. When a transition is followed between two states of a sample, all spectra cross at wavelengths where the two states absorb equally; such an **isosbestic point** shows that only two absorbing species are present.

### 11.2.3. Proteins: Concentration from the Sequence

**Formula 11.2.1 (Molar Absorption Coefficient of a Protein at 280 nm)** For a protein with $n_{\mathrm{W}}$ tryptophans, $n_{\mathrm{Y}}$ tyrosines and $n_{\mathrm{C}}$ disulfide bonds and no other chromophores,

$$
\varepsilon_{280} \approx 5500\,n_{\mathrm{W}} + 1490\,n_{\mathrm{Y}} + 125\,n_{\mathrm{C}}\quad (\mathrm{L\,mol^{-1}\,cm^{-1}}),
$$
with coefficients calibrated on native proteins (Pace and colleagues, 1995).

The derivation and the use of this formula are in [6.4.9](/6.4.9#sec-9.2.5). The physical point is that the side chains of tryptophan and tyrosine in a folded protein absorb within a few percent of the free amino acids in water: the environmental shifts of 11.2.2 move the bands by nanometers, and the band at $280\,\mathrm{nm}$ lies on the broad maximum, where small shifts change the absorbance little. The formula is accurate to about $5\,\%$ for proteins containing tryptophan and worse for proteins without, and fails for proteins with other chromophores (hemes, flavins, metal centers, bound nucleotides).

**Example 11.2.1 (Hen Egg-White Lysozyme)** Lysozyme ($129$ residues, $M = 14.3\,\mathrm{kDa}$) has $6$ tryptophans, $3$ tyrosines and $4$ disulfide bonds, so $\varepsilon_{280} = 6\times5500 + 3\times1490 + 4\times125 = 37\,970\,\mathrm{L\,mol^{-1}\,cm^{-1}}$, close to the measured $37\,970$–$38\,940$. A solution of absorbance $0.80$ in a $1\,\mathrm{cm}$ cell therefore contains $21\,\mu\mathrm{M}$ lysozyme, or $0.30\,\mathrm{mg\,mL^{-1}}$; equivalently, $A_{280}^{0.1\,\%} = \varepsilon/M = 2.65$. A preparation with $A_{260}/A_{280} > 0.6$ contains appreciable nucleic acid.

### 11.2.4. Nucleic Acids: Hypochromism and Melting

The bases of nucleic acids absorb near $260\,\mathrm{nm}$, but a double helix absorbs about $30$–$40\,\%$ less than its free nucleotides; heating separates the strands and restores the absorption, the **hyperchromic effect** of melting ([6.4.9](/6.4.9#sec-9.2.5)). The decrease in the duplex, **hypochromism** (the **hypochromic effect**), is not a property of single bases but of their stacking. Tinoco and Rhodes explained it in 1960 as an interaction of transition dipoles: the oscillating dipole of one base, induced by the light, creates at a stacked neighbor a field that opposes or reinforces its own oscillation. For bases stacked face to face, with in-plane transition dipoles roughly parallel, the in-phase combination of the dipoles is shifted to higher energy (11.2.5), and intensity is transferred from the $260\,\mathrm{nm}$ band to bands in the far ultraviolet; the total dipole strength of all bands is conserved, but the band that is measured loses intensity. Single-stranded nucleic acids are partly stacked and show part of the effect, so their absorbance also rises gently with temperature.

The change of $A_{260}$ with temperature is the classic way to measure the thermodynamics of duplex formation. For a transition between two states, duplex and coil, with fraction $f$ melted, the absorbance is a linear combination $A = (1 - f)A_{\mathrm{ds}}(T) + fA_{\mathrm{ss}}(T)$ of two sloping baselines, and the **two-state model** of [7.6.8](/7.6.8) gives $f(T)$.

**Formula 11.2.2 (Two-State Melting Curves)** (a) For an intramolecular transition (a hairpin, a long duplex in which helix and coil segments behave as independent cooperative units) with van 't Hoff enthalpy $\Delta H$ and midpoint $T_{\mathrm{m}}$,

$$
f = \frac{K}{1 + K}, \qquad K = \exp\left[-\frac{\Delta H}{R}\left(\frac{1}{T} - \frac{1}{T_{\mathrm{m}}}\right)\right], \qquad \left.\frac{\mathrm{d}f}{\mathrm{d}T}\right|_{T_{\mathrm{m}}} = \frac{\Delta H}{4RT_{\mathrm{m}}^2}.
$$
(b) For a duplex of two complementary strands at total strand concentration $C_{\mathrm{T}}$ (each strand $C_{\mathrm{T}}/2$), with standard enthalpy and entropy of association $\Delta H^\circ < 0$ and $\Delta S^\circ < 0$,

$$
\frac{1}{T_{\mathrm{m}}} = \frac{R}{\Delta H^\circ}\ln\frac{C_{\mathrm{T}}}{4} + \frac{\Delta S^\circ}{\Delta H^\circ},
$$
so a plot of $1/T_{\mathrm{m}}$ against $\ln C_{\mathrm{T}}$ gives $\Delta H^\circ$ and $\Delta S^\circ$ (standard concentration $1\,\mathrm{M}$).

![Melting of DNA followed by absorbance at 260 nm. A: two-state melting curves with Tm = 65 °C and van 't Hoff enthalpies of 150, 300 and 600 kJ/mol, between sloping baselines of duplex and single strands (dotted) and with 30 % hyperchromicity. B: the fraction melted (solid) and its temperature derivative (dashed, ×10): the derivative peaks at Tm with height ΔH_vH/(4RTm²), so a sharper transition means a larger cooperative unit. C: a bimolecular duplex of two 12-mers (dissociation enthalpy 400 kJ/mol, entropy 1.10 kJ mol⁻¹ K⁻¹) at total strand concentrations of 0.5, 5 and 50 µM: Tm rises with concentration, and 1/Tm is linear in ln(C_T/4) (inset)](./plots/dna-melting.py)

The width of the transition reports the size of the cooperative unit. A $12$-base-pair duplex melts with $\Delta H \approx 400\,\mathrm{kJ\,mol^{-1}}$, about $35\,\mathrm{kJ\,mol^{-1}}$ per base pair, over $15$–$20\,^\circ\mathrm{C}$; a long DNA melts over a few degrees in a series of domains of a few hundred base pairs, rich in AT first, and its melting temperature rises by about $0.4\,^\circ\mathrm{C}$ for each percent of GC. Comparison of the van 't Hoff enthalpy from the shape of the curve with the calorimetric enthalpy measured by DSC tests the two-state assumption ([7.6.8](/7.6.8)); the nearest-neighbor parameters used to predict the stability of oligonucleotides and primers were derived from hundreds of such optical melting curves. The kinetics of folding and the thermodynamics of RNA hairpins are treated in [7.6.16](/7.6.16).

### 11.2.5. Exciton Coupling of Chromophores

Hypochromism is one instance of a general effect: identical chromophores close to each other share their excitation. Let two chromophores with transition dipoles $\boldsymbol{p}_1$ and $\boldsymbol{p}_2$ of equal length $p$ and the same transition energy $E_0$ be separated by $\boldsymbol{R}_{12}$. The states with chromophore 1 or chromophore 2 excited are degenerate and are coupled by the electrostatic interaction of the two transition charge distributions; when $R$ is larger than the chromophores, the point-dipole approximation gives

$$
V_{12} = \frac{1}{4\pi\varepsilon_0n^2}\,\frac{\boldsymbol{p}_1\cdot\boldsymbol{p}_2 - 3(\boldsymbol{p}_1\cdot\hat{\boldsymbol{R}})(\boldsymbol{p}_2\cdot\hat{\boldsymbol{R}})}{R^3} = \frac{p^2\kappa}{4\pi\varepsilon_0n^2R^3},
$$
with the orientation factor $\kappa = \cos\theta_{12} - 3\cos\theta_1\cos\theta_2$ ($\theta_{12}$ the angle between the dipoles, $\theta_1$, $\theta_2$ their angles to $\boldsymbol{R}_{12}$) and the screening factor $1/n^2$ of the medium.

**Definition 11.2.1 (Exciton Coupling)** **Exciton coupling** is the splitting of the excited states of two or more identical chromophores by the interaction of their transition dipoles into delocalized states, excitons, in which the excitation is shared by all chromophores.

**Theorem 11.2.1 (Exciton States of a Dimer)** The excited states of the dimer are the combinations $\psi_\pm = (\psi_1^* \pm \psi_2^*)/\sqrt2$ with energies $E_\pm = E_0 \pm V_{12}$ and transition dipoles $\boldsymbol{p}_\pm = (\boldsymbol{p}_1 \pm \boldsymbol{p}_2)/\sqrt2$, so their dipole strengths are $p^2(1 \pm \cos\theta_{12})$, summing to $2p^2$. For a non-planar arrangement, the two exciton states have rotational strengths (11.3.3) of equal magnitude, proportional to $\tilde\nu_0\,\boldsymbol{R}_{12}\cdot(\boldsymbol{p}_1\times\boldsymbol{p}_2)$, and opposite sign.

**Proof** In the basis of the two locally excited states, the Hamiltonian is the $2\times2$ matrix with $E_0$ on the diagonal and $V_{12}$ off the diagonal; its eigenvectors are $\psi_\pm$ with eigenvalues $E_0 \pm V_{12}$. The transition dipole of $\psi_\pm$ from the ground state $\psi_1\psi_2$ is the corresponding combination of the local dipoles, and $\lvert\boldsymbol{p}_1 \pm \boldsymbol{p}_2\rvert^2/2 = p^2(1 \pm \cos\theta_{12})$. The magnetic transition moment of an electric dipole $\boldsymbol{p}_j$ oscillating at position $\boldsymbol{r}_j$ contains the term $(\omega/2)\boldsymbol{r}_j\times\boldsymbol{p}_j$; its scalar product with $\boldsymbol{p}_\pm$ gives the coupled-oscillator rotational strength $\pm(\pi\tilde\nu_0/2)\boldsymbol{R}_{12}\cdot(\boldsymbol{p}_1\times\boldsymbol{p}_2)$ up to the sign convention of $\boldsymbol{R}_{12}$. $\square$

![Exciton coupling of two identical chromophores with transition dipoles of 5 D at 1 nm (point-dipole approximation, n² = 1.77). A: energies of the in-phase (allowed, thick) and out-of-phase (forbidden, dashed) exciton states of parallel dipoles against the angle θ between the dipoles and the line joining them: head-to-tail (J) arrangements shift the allowed band to the red, side-by-side (H) arrangements to the blue, and the splitting vanishes at 54.7°; the maximal splitting is 142 cm⁻¹. B: absorption of the monomer and of H and J dimers (coupling exaggerated tenfold): the H dimer absorbs at higher energy and is hypochromic in the monomer band. C: a twisted dimer (dipoles at 60°): both exciton bands are allowed and have opposite rotational strengths, so the CD spectrum is a conservative couplet centered on the absorption maximum; the mirror-image dimer gives the inverted couplet](./plots/exciton-coupling.py)

**Example 11.2.2 (Size of the Coupling)** For $p = 5\,\mathrm{D} = 1.67\times10^{-29}\,\mathrm{C\,m}$, $R = 1\,\mathrm{nm}$ and $\kappa = 1$, $V = p^2/(4\pi\varepsilon_0R^3) = 2.5\times10^{-21}\,\mathrm{J} = 126\,\mathrm{cm^{-1}}$ in vacuum and $71\,\mathrm{cm^{-1}}$ with $n^2 = 1.77$. This is small compared with the width of an electronic band in solution, so the two exciton bands are not resolved in absorption; the coupling shows up as a shift and a change of intensity (hypochromism). In CD, however, the two bands have opposite signs, and even a small splitting produces a characteristic positive–negative couplet.

Three consequences matter for biological spectroscopy. First, stacked bases in nucleic acids and stacked aromatic dyes are H-like and hypochromic, whereas head-to-tail aggregates such as the J aggregates of cyanine dyes have a narrow, intense, red-shifted band. Second, in a helical polymer of $N$ identical chromophores the excitation is delocalized over many units; for the peptide $\pi\to\pi^*$ transition in an α helix, Moffitt (1956) showed that the exciton band splits into a component polarized parallel to the helix axis, near $208\,\mathrm{nm}$, and a doubly degenerate component polarized perpendicular to it, near $190\,\mathrm{nm}$: this is the origin of the characteristic CD of the α helix (11.3.4). Third, the sign of the exciton couplet of two chromophores gives the sense of their twist, the *exciton chirality method* used to determine absolute configurations of natural products. When the coupling is much smaller than the band width and the chromophores are not identical, the excitation does not delocalize but hops incoherently from donor to acceptor: this weak-coupling limit is Förster energy transfer (11.5.7), and the intermediate regime is that of the light-harvesting antennas of photosynthesis ([7.6.18](/7.6.18)).

## 11.3. Optical Activity and Circular Dichroism

### 11.3.1. Circular Birefringence and Optical Rotatory Dispersion

**Linearly polarized light** is the superposition of left and right **circularly polarized light** of equal amplitude ([5.4.3](/5.4.3)). A medium of **chiral** molecules responds differently to the two senses of rotation: it has different refractive indices $n_{\mathrm{L}}$, $n_{\mathrm{R}}$ and, inside an absorption band, different absorption coefficients $\varepsilon_{\mathrm{L}}$, $\varepsilon_{\mathrm{R}}$. Since all amino acids except glycine, all sugars and all nucleotides are chiral, and since proteins and nucleic acids fold into helices of one handedness, essentially every biological macromolecule is optically active.

After a path $l$, the two circular components of a linearly polarized beam have accumulated the phase difference $\delta = 2\pi l(n_{\mathrm{L}} - n_{\mathrm{R}})/\lambda$, and their superposition is again linearly polarized, with the plane rotated by

$$
\phi = \frac{\pi l}{\lambda}(n_{\mathrm{L}} - n_{\mathrm{R}}) \quad (\mathrm{rad}),
$$
positive (dextrorotatory, clockwise as seen by an observer looking towards the source) when $n_{\mathrm{L}} > n_{\mathrm{R}}$. A difference of $10^{-6}$ in the refractive indices rotates light of $500\,\mathrm{nm}$ by $0.36^\circ$ per centimeter. The rotation is normalized as the specific rotation $[\alpha] = \phi/(lc)$ ($\phi$ in degrees, $l$ in $\mathrm{dm}$, $c$ in $\mathrm{g\,mL^{-1}}$), the molar rotation $[\Phi] = [\alpha]M/100$ or, for polymers, the mean residue rotation $[m] = [\alpha]M_0/100$ with the mean residue mass $M_0 \approx 110$–$115\,\mathrm{g\,mol^{-1}}$ for proteins.

**Definition 11.3.1 (Optical Rotatory Dispersion)** The dependence of the optical rotation on wavelength is **optical rotatory dispersion** (ORD). Within an absorption band of an optically active chromophore the ORD curve changes sign, with a peak on one side of the band and a trough on the other; this anomalous dispersion is the *Cotton effect*, called positive when the peak lies on the long-wavelength side.

$n_{\mathrm{L}} - n_{\mathrm{R}}$ and $\varepsilon_{\mathrm{L}} - \varepsilon_{\mathrm{R}}$ are the real and imaginary parts of one complex response for circularly polarized light, as $n$ and $\kappa$ were in Formula 11.1.1, and they are related by the Kramers–Kronig transforms

$$
[\Phi](\lambda) = \frac{2}{\pi}\int_0^\infty[\theta](\lambda')\,\frac{\lambda'}{\lambda^2 - \lambda'^2}\,\mathrm{d}\lambda', \qquad
[\theta](\lambda) = -\frac{2}{\pi\lambda}\int_0^\infty[\Phi](\lambda')\,\frac{\lambda'^2}{\lambda^2 - \lambda'^2}\,\mathrm{d}\lambda'
$$
(principal values), with $[\theta]$ the molar ellipticity of 11.3.2. ORD and CD therefore contain the same information in principle. In practice CD is far easier to interpret: a CD band is confined to its absorption band and has its extremum at $\lambda_{\max}$, while every chromophore contributes to the ORD at all wavelengths, so overlapping bands and distant strong bands mix. ORD dominated the field until about 1970 (for example the Moffitt–Yang analysis of helix content at $233\,\mathrm{nm}$); since then CD has replaced it.

![A positive Cotton effect: a single optically active Gaussian band at 220 nm. The CD (blue) has the shape of the absorption band (dashed); the ORD (red), its Kramers–Kronig transform, passes through zero at the absorption maximum, with a peak on the long-wavelength side and a trough on the short-wavelength side, and it decays slowly far from the band, where it adds to the rotation measured at other wavelengths](./plots/cotton-effect.py)

### 11.3.2. Circular Dichroism and Ellipticity

**Circular dichroism** ([6.4.9](/6.4.9#sec-9.6.4)) is the difference $\Delta A = A_{\mathrm{L}} - A_{\mathrm{R}} = \Delta\varepsilon\,cl$, with $\Delta\varepsilon = \varepsilon_{\mathrm{L}} - \varepsilon_{\mathrm{R}}$. Unequal absorption leaves the two circular components with unequal amplitudes $E_{\mathrm{L}}$, $E_{\mathrm{R}}$, and their sum is elliptically polarized. Instruments report the ellipticity $\theta$, defined by $\tan\theta = (E_{\mathrm{R}} - E_{\mathrm{L}})/(E_{\mathrm{R}} + E_{\mathrm{L}})$, the ratio of the minor to the major axis of the ellipse.

**Proposition 11.3.1 (Ellipticity and Differential Absorbance)** For $\lvert\Delta A\rvert \ll 1$,

$$
\theta = \frac{\ln 10}{4}\Delta A\ \ \mathrm{rad} = 32.98\,\Delta A\ \ \mathrm{deg}, \qquad [\theta] = \frac{100\,\theta}{cl} = 3298\,\Delta\varepsilon\ \ \mathrm{deg\,cm^2\,dmol^{-1}},
$$
where the molar ellipticity $[\theta]$ uses $\theta$ in degrees, $c$ in $\mathrm{mol\,L^{-1}}$ and $l$ in $\mathrm{cm}$.

**Proof** Amplitudes scale as the square root of intensities, $E \propto 10^{-A/2} = \mathrm{e}^{-A\ln 10/2}$. With $A_{\mathrm{L,R}} = \bar A \pm \Delta A/2$,

$$
\tan\theta = \frac{\mathrm{e}^{-A_{\mathrm{R}}\ln10/2} - \mathrm{e}^{-A_{\mathrm{L}}\ln10/2}}{\mathrm{e}^{-A_{\mathrm{R}}\ln10/2} + \mathrm{e}^{-A_{\mathrm{L}}\ln10/2}} = \tanh\frac{\Delta A\ln10}{4} \approx \frac{\ln 10}{4}\Delta A,
$$
and $(\ln 10/4)(180/\pi) = 32.98$. Dividing by $cl$ and multiplying by $100$ gives $[\theta] = 3298\,\Delta\varepsilon$. $\square$

For proteins, $c$ is the concentration of residues, $[\theta]_{\mathrm{MRW}} = \theta M_0/(10\,l\,c_{\mathrm{m}})$ with $\theta$ in degrees, $l$ in $\mathrm{cm}$ and the mass concentration $c_{\mathrm{m}}$ in $\mathrm{mg\,mL^{-1}}$; this mean residue ellipticity makes proteins of different size comparable. The signals are small: an α-helical protein at $0.1\,\mathrm{mg\,mL^{-1}}$ in a $1\,\mathrm{mm}$ cell gives $\theta \approx -30\,\mathrm{mdeg}$ at $222\,\mathrm{nm}$, which corresponds to $\Delta A \approx 10^{-3}$ on a total absorbance near $0.5$. CD instruments therefore modulate the polarization at about $50\,\mathrm{kHz}$ with a photoelastic modulator and detect the alternating part of the signal ([6.4.9](/6.4.9#sec-9.6.4)).

### 11.3.3. Rotational Strength: The Origin of Circular Dichroism

Why does a chiral molecule absorb left and right circularly polarized light differently? A circularly polarized wave has an electric field that rotates in time at a fixed point and a helical pattern in space at a fixed time; it can tell left from right only through the variation of the field across the molecule, that is, through terms beyond the electric dipole approximation of 11.1.3. The leading such term is the coupling of the magnetic field to the magnetic dipole moment $\hat{\boldsymbol{m}}$ of the molecule.

**Theorem 11.3.1 (Rosenfeld Equation)** The circular dichroism of the transition $0 \to a$ in an isotropic sample is proportional to its rotational strength

$$
R_{0a} = \operatorname{Im}\left(\boldsymbol{p}_{0a}\cdot\boldsymbol{m}_{a0}\right),
$$
the imaginary part of the scalar product of the electric and magnetic transition dipole moments. In terms of the measured band,

$$
R_{0a} = 2.296\times10^{-39}\int\frac{\Delta\varepsilon(\tilde\nu)}{\tilde\nu}\,\mathrm{d}\tilde\nu\ \ \mathrm{erg\,cm^3}
$$
(in the customary cgs unit). The rotational strengths of all transitions of a molecule sum to zero.

A nonzero $R$ needs a transition that displaces charge (electric dipole) and circulates it (magnetic dipole) about a common axis, a helical displacement of charge; mirror-image molecules have opposite helicity and opposite $R$. A planar or otherwise achiral chromophore has $\boldsymbol{p}_{0a}\perp\boldsymbol{m}_{a0}$ or one of the two equal to zero, and becomes optically active only in a chiral environment. There are three mechanisms. An *inherently chiral chromophore* (a twisted disulfide bond, a helicene) has both moments nonparallel by itself. In the *one-electron mechanism* the static charges of a chiral environment mix electric- and magnetic-dipole-allowed transitions of an achiral chromophore, as for the $\mathrm{n}\to\pi^*$ transition of a peptide group or a carbonyl. In the *coupled-oscillator mechanism*, electric dipoles of different groups arranged chirally couple as in Theorem 11.2.1; this dominates the CD of helical polymers, of stacked bases and of the aromatic side chains in folded proteins. Free tyrosine and phenylalanine are only weakly optically active, because the rings rotate and their chiral center is far away, whereas the same side chains packed in a protein interior give distinct near-UV CD bands. Mirror-image proteins synthesized from D-amino acids, such as a D-polymerase that replicates L-DNA, give exactly inverted CD spectra.

### 11.3.4. Far-UV CD and Secondary Structure

In the far ultraviolet ($180$–$250\,\mathrm{nm}$) the CD of proteins comes from the peptide groups: the $\mathrm{n}\to\pi^*$ transition near $220\,\mathrm{nm}$ (one-electron mechanism) and the $\pi\to\pi^*$ transition near $190\,\mathrm{nm}$, split into exciton components by the regular arrangement of the peptides (coupled oscillators). Each type of **secondary structure** has its own geometry and hence its own spectrum, while tertiary structure contributes little.

| Structure | Positive band | Negative bands | $[\theta]_{222}$ / ($10^3\,\mathrm{deg\,cm^2\,dmol^{-1}}$) |
|---|---|---|---|
| **α helix** | $191$–$193\,\mathrm{nm}$ (strong) | $208\,\mathrm{nm}$ (parallel exciton component), $222\,\mathrm{nm}$ ($\mathrm{n}\to\pi^*$) | $\approx -35$ to $-40$ |
| **β sheet** | $195$–$198\,\mathrm{nm}$ | $215$–$218\,\mathrm{nm}$ (weaker, variable with twist) | $\approx -10$ to $-20$ |
| β turns | $\approx 205\,\mathrm{nm}$ (weak) | variable | small |
| Disordered, polyproline II | $\approx 218\,\mathrm{nm}$ (weak) | $195$–$198\,\mathrm{nm}$ (strong) | $\approx 0$ |

**Formula 11.3.1 (Linear Decomposition of a CD Spectrum)** To a first approximation the mean residue ellipticity of a protein is a linear combination of basis spectra of the secondary-structure classes $k$ with fractions $f_k$,

$$
[\theta](\lambda) = \sum_kf_k[\theta]_k(\lambda), \qquad f_k \ge 0, \quad \sum_kf_k = 1.
$$
The basis spectra are obtained by regression from proteins of known structure (reference sets of $50$–$100$ proteins), and the fractions of an unknown protein by constrained least squares, singular value decomposition or self-consistent methods (CONTIN, SELCON, CDSSTR, K2D, BeStSel).

The decomposition rests on four assumptions: the reference proteins have the same structures in solution as in their crystals; the contributions of the classes are additive; aromatic side chains, disulfides and prosthetic groups contribute nothing in the far ultraviolet; and each class has one spectrum independent of length, twist and environment. All four are approximations. Short helices have weaker bands per residue, twisted β sheets differ in spectrum, and aromatic residues contribute noticeably in some proteins. Helix contents come out within about $\pm5\,\%$, β-sheet and turn contents with errors of $10\,\%$ or more, and the accuracy depends strongly on how far into the ultraviolet the spectrum is measured, since the information on β structure lies largely below $200\,\mathrm{nm}$. Synchrotron radiation CD extends spectra to $160$–$170\,\mathrm{nm}$ and improves the β estimates.

![Secondary structure from far-UV CD (synthetic data). A: model basis spectra of α helix, β sheet and disordered chain, built from Gaussian bands at the characteristic positions. B: a spectrum of a protein with 35 % helix, 25 % sheet and 40 % disorder, with noise that increases below 200 nm, and its non-negative least-squares fit with the fractions constrained to sum to one; the residual is flat. C: means and standard deviations of the fitted fractions over 300 noisy replicates, using data from 185 nm or only from 205 nm: the helix fraction is robust, but the uncertainty of the β-sheet fraction grows when the region below 205 nm is lost (as in buffers containing chloride, imidazole or high salt). Real proteins add the larger systematic errors of the basis set itself](./plots/cd-deconvolution.py)

For peptides and proteins rich in helix, a single wavelength often suffices. The ellipticity at $222\,\mathrm{nm}$ is dominated by the helix, and an empirical calibration for a peptide of $n$ residues at temperature $t$ (in $^\circ\mathrm{C}$) is $[\theta]_{\mathrm{H}} = -40\,000(1 - 2.5/n) + 100t$ for the complete helix and $[\theta]_{\mathrm{C}} = 640 - 45t$ for the coil (Luo and Baldwin, 1997), with the helix fraction $f_{\mathrm{H}} = ([\theta]_{222} - [\theta]_{\mathrm{C}})/([\theta]_{\mathrm{H}} - [\theta]_{\mathrm{C}})$.

**Example 11.3.1 (Helix Content of a Peptide)** A peptide of $20$ residues at $25\,^\circ\mathrm{C}$ has $[\theta]_{222} = -20\,000\,\mathrm{deg\,cm^2\,dmol^{-1}}$. Then $[\theta]_{\mathrm{H}} = -40\,000\times0.875 + 2500 = -32\,500$, $[\theta]_{\mathrm{C}} = 640 - 1125 = -485$, and $f_{\mathrm{H}} = (-20\,000 + 485)/(-32\,500 + 485) = 0.61$. A $5\,\%$ error in the peptide concentration, the commonest source of error in CD, changes $f_{\mathrm{H}}$ by $0.03$; the concentration should therefore be determined by absorbance (Formula 11.2.1) or amino acid analysis rather than by weight.

Because the measurement takes minutes and needs about $10\,\mu\mathrm{g}$ of protein, the most frequent uses of far-UV CD are qualitative: to confirm that a recombinant protein or a mutant is folded like the wild type, and to follow $[\theta]_{222}$ against temperature or denaturant concentration to obtain unfolding curves and stability ([7.6.8](/7.6.8), [7.6.16](/7.6.16)). Stopped-flow CD follows the formation of secondary structure on the millisecond time scale.

### 11.3.5. Near-UV CD, Nucleic Acids and Practical Limits

Between $250$ and $320\,\mathrm{nm}$ the CD of proteins comes from the aromatic side chains (phenylalanine with fine structure at $255$, $261$ and $268\,\mathrm{nm}$, tyrosine near $275$–$282\,\mathrm{nm}$, tryptophan at $279$, $284$ and $291\,\mathrm{nm}$) and from disulfide bonds (broad, $250$–$300\,\mathrm{nm}$). The bands can be positive or negative and are about a hundred times weaker than in the far ultraviolet; they depend on the rigid, asymmetric packing of the side chains, so the near-UV spectrum is a fingerprint of the tertiary structure. A molten globule ([7.6.16](/7.6.16)) has the far-UV CD of the native protein but loses its near-UV CD. Prosthetic groups and metal centers (hemes, flavins, chlorophylls, copper sites) give CD in the visible region, which reports the binding and the oxidation state of the cofactor.

The CD of nucleic acids comes from the stacking of the bases, which are planar and individually almost inactive. B-DNA has a positive band near $275\,\mathrm{nm}$ and a negative band near $245\,\mathrm{nm}$, of nearly equal magnitude, a conservative couplet characteristic of exciton coupling; A-form duplexes (double-stranded RNA, RNA–DNA hybrids) have a strong positive band at $260\,\mathrm{nm}$ and a negative band at $210\,\mathrm{nm}$; left-handed Z-DNA gives a roughly inverted spectrum, with a negative band near $290\,\mathrm{nm}$; parallel G-quadruplexes have a positive band at $264\,\mathrm{nm}$. CD thus follows the B–A and B–Z transitions, the binding of intercalators and the folding of quadruplexes.

The practical limits come from absorption, not from CD. The total absorbance of sample, buffer and cell must stay below about $1$, or the light reaching the photomultiplier is too weak for a useful signal-to-noise ratio. Far-UV spectra are therefore measured in cells of $0.1$–$1\,\mathrm{mm}$, in dilute phosphate or fluoride buffers, at protein concentrations of $0.1$–$0.5\,\mathrm{mg\,mL^{-1}}$; chloride, imidazole, Tris and dithiothreitol absorb below $200$–$210\,\mathrm{nm}$, and $100\,\mathrm{mM}$ $\ce{NaCl}$ alone cuts the usable range at about $195\,\mathrm{nm}$ in a $1\,\mathrm{mm}$ cell. A magnetic field along the beam induces circular dichroism even in achiral chromophores (magnetic circular dichroism, MCD), which is used to study the electronic structure of metal centers and hemes.

## 11.4. Vibrational Spectroscopy

### 11.4.1. Normal Modes and the Infrared Selection Rule

A molecule of $N$ atoms has $3N - 6$ vibrational degrees of freedom ($3N - 5$ if linear). In the harmonic approximation the motion decomposes into independent **normal modes** $Q_k$, each a collective displacement of all atoms at one frequency; for a bond treated as two masses on a spring of force constant $k$, the frequency is

$$
\tilde\nu = \frac{1}{2\pi c}\sqrt{\frac{k}{\mu}}, \qquad \mu = \frac{m_1m_2}{m_1 + m_2},
$$
with $\mu$ here the reduced mass. A carbonyl ($k \approx 1200\,\mathrm{N\,m^{-1}}$, $\mu = 6.86\,\mathrm{u}$) vibrates near $1720\,\mathrm{cm^{-1}}$. Replacing hydrogen by deuterium almost doubles the reduced mass of an $\ce{N-H}$ oscillator and lowers its frequency by a factor of about $1.37$, from $3300$ to about $2400\,\mathrm{cm^{-1}}$; heavier isotopes ($^{13}\mathrm{C}$, $^{15}\mathrm{N}$, $^{18}\mathrm{O}$) shift frequencies by a few percent and are used to assign bands to particular groups or residues.

The transition dipole of a vibrational transition follows from Definition 11.1.1 with the dipole moment expanded in the normal coordinate,

$$
\boldsymbol{p}(Q) = \boldsymbol{p}_0 + \left(\frac{\partial\boldsymbol{p}}{\partial Q}\right)_0Q + \cdots, \qquad
\boldsymbol{p}_{10} = \left(\frac{\partial\boldsymbol{p}}{\partial Q}\right)_0\langle1\vert Q\vert0\rangle = \left(\frac{\partial\boldsymbol{p}}{\partial Q}\right)_0\sqrt{\frac{\hbar}{2\omega}},
$$
where $Q$ is mass weighted. The constant term $\boldsymbol{p}_0$ does not contribute, because $\langle1\vert0\rangle = 0$, and the harmonic matrix elements of $Q$ connect only neighboring levels.

**Theorem 11.4.1 (Infrared Selection Rule)** A normal mode absorbs infrared radiation in its fundamental transition only if the dipole moment changes along the mode, $(\partial\boldsymbol{p}/\partial Q)_0 \ne \boldsymbol{0}$, and the harmonic selection rule is $\Delta v = \pm1$; the intensity is proportional to $\lvert\partial\boldsymbol{p}/\partial Q\rvert^2$. A permanent dipole moment is neither necessary nor sufficient: the antisymmetric stretch of $\ce{CO2}$ is infrared active although the molecule has no dipole moment, and homonuclear diatomics ($\ce{N2}$, $\ce{O2}$) are inactive because no vibration can create one.

The theorem is the precise form of the **infrared active** criterion of [6.4.11](/6.4.11#sec-11.1.5). Anharmonicity relaxes the selection rule and gives weak overtones ($\Delta v = \pm2$) and combination bands; when an overtone falls near a fundamental of the same symmetry the two mix (**Fermi resonance**), as in the amide B band of proteins.

### 11.4.2. Raman Scattering

Light of frequency $\omega_0$ far from any absorption induces in a molecule the dipole $\boldsymbol{p}_{\mathrm{ind}} = \alpha\boldsymbol{E}$, where $\alpha$ is the **polarizability**. If the molecule vibrates, the polarizability is modulated, $\alpha(t) = \alpha_0 + (\partial\alpha/\partial Q)_0Q_0\cos\omega_vt$, and

$$
p_{\mathrm{ind}}(t) = \alpha_0E_0\cos\omega_0t + \frac12\left(\frac{\partial\alpha}{\partial Q}\right)_0Q_0E_0\left[\cos(\omega_0 - \omega_v)t + \cos(\omega_0 + \omega_v)t\right].
$$
The first term radiates at the incident frequency, elastic **Rayleigh scattering** ([7.6.9](/7.6.9)); the others radiate at $\omega_0 \mp \omega_v$, the Stokes and anti-Stokes lines of **Raman scattering**. Quantum mechanically, the molecule absorbs a photon into a virtual state and emits one, ending in a different vibrational level; the **Raman shift** $\tilde\nu_0 - \tilde\nu_{\mathrm{s}}$ equals the vibrational wavenumber and does not depend on the excitation wavelength.

**Theorem 11.4.2 (Raman Selection Rule and Intensities)** A normal mode is Raman active if the polarizability changes along it, $(\partial\alpha/\partial Q)_0 \ne 0$ (for some component of the polarizability tensor). The scattered power of a line grows as the fourth power of the scattered frequency and as $\lvert\partial\alpha/\partial Q\rvert^2$, and the ratio of anti-Stokes to Stokes intensity is

$$
\frac{I_{\mathrm{aS}}}{I_{\mathrm{S}}} = \left(\frac{\tilde\nu_0 + \tilde\nu_v}{\tilde\nu_0 - \tilde\nu_v}\right)^4\exp\left(-\frac{hc\tilde\nu_v}{k_{\mathrm{B}}T}\right),
$$
because anti-Stokes scattering starts from the thermally populated level $v = 1$.

In molecules with a center of symmetry, modes that are symmetric under inversion are Raman active and infrared inactive, and antisymmetric modes the reverse (rule of mutual exclusion, [6.4.11](/6.4.11#sec-11.5.2)); biological molecules have no center of symmetry, and most modes are active in both, with different intensities. Raman and infrared spectra are complementary: polar groups ($\ce{C=O}$, $\ce{O-H}$, $\ce{P=O}$) absorb strongly in the infrared, whereas polarizable, symmetric groups ($\ce{S-S}$, $\ce{C=C}$, $\ce{S-H}$, aromatic rings) scatter strongly in Raman.

**Example 11.4.1 (Anti-Stokes Intensities and Thermometry)** At $25\,^\circ\mathrm{C}$, $hc/k_{\mathrm{B}}T$ corresponds to $1/(207\,\mathrm{cm^{-1}})$. For a mode at $1000\,\mathrm{cm^{-1}}$ excited at $532\,\mathrm{nm}$ ($18\,797\,\mathrm{cm^{-1}}$), $I_{\mathrm{aS}}/I_{\mathrm{S}} = 1.53\times\mathrm{e}^{-4.8} = 0.013$; for the amide I band at $1660\,\mathrm{cm^{-1}}$ it is about $5\times10^{-4}$. Ordinary Raman spectrometers record only the Stokes side; the ratio itself measures the local temperature of a sample.

Raman scattering is weak: cross-sections are about $10^{-29}\,\mathrm{cm^2}$ per molecule, twelve to fourteen orders of magnitude below those of strong absorption, so lasers and efficient rejection of the Rayleigh line are needed. In exchange, water scatters weakly (its bending band at $1640\,\mathrm{cm^{-1}}$ is far weaker than in the infrared), samples can be crystals, fibers, viruses or living cells, and confocal Raman microscopy maps chemical composition at micrometer resolution without labels. The **depolarization ratio** $\rho = I_\perp/I_\parallel = 3\gamma^2/(45a^2 + 4\gamma^2)$ for polarized excitation, with $a$ and $\gamma$ the isotropic and anisotropic parts of the derived polarizability, lies between $0$ and $3/4$ and identifies totally symmetric modes ($\rho < 3/4$). **Resonance Raman spectroscopy** tunes the excitation into an electronic absorption band: the polarizability then contains a resonance denominator, and the modes of the chromophore that are displaced in the excited state (Proposition 11.1.1) are enhanced by $10^3$–$10^5$. The vibrations of heme, retinal, carotenoids and flavins can thus be observed selectively inside a protein of thousands of other modes; time-resolved resonance Raman of bacteriorhodopsin and rhodopsin established the all-*trans* to 13-*cis* (and 11-*cis* to all-*trans*) isomerization of the retinal Schiff base ([7.6.18](/7.6.18)). Surface-enhanced Raman scattering on nanostructured silver or gold reaches single-molecule sensitivity.

### 11.4.3. Amide Bands and Secondary Structure

The peptide group gives a set of characteristic vibrations, the amide bands; the infrared spectrum of a protein in the region $1500$–$1700\,\mathrm{cm^{-1}}$ is dominated by them.

| Band | Wavenumber / $\mathrm{cm^{-1}}$ | Main contributions |
|---|---|---|
| Amide A | $\approx 3300$ | $\ce{N-H}$ stretch |
| Amide B | $\approx 3100$ | Fermi resonance of amide A with the first overtone of amide II |
| Amide I | $1600$–$1700$ | $\ce{C=O}$ stretch ($\approx 80\,\%$), with $\ce{C-N}$ stretch and $\ce{N-H}$ bend |
| Amide II | $1510$–$1580$ | $\ce{N-H}$ in-plane bend coupled to $\ce{C-N}$ stretch; shifts to $\approx 1450$ (amide II′) on deuteration |
| Amide III | $1220$–$1340$ | $\ce{C-N}$ stretch and $\ce{N-H}$ bend, complex |
| Amide IV–VII | $600$–$770$ | out-of-plane and skeletal deformations |

**Definition 11.4.1 (Amide I Band)** The **amide I band** is the infrared and Raman band of the peptide backbone between $1600$ and $1700\,\mathrm{cm^{-1}}$, due mainly to the carbonyl stretching vibration. Its position depends on the hydrogen bonding of the carbonyl and on the coupling between neighboring peptide oscillators, and therefore on the secondary structure.

Two mechanisms make amide I structure sensitive. Hydrogen bonding of the carbonyl weakens the $\ce{C=O}$ bond and lowers its frequency. More importantly, the amide I oscillators of neighboring peptides are coupled through their transition dipoles, exactly as electronic transitions were in Theorem 11.2.1, so the vibration is delocalized into exciton-like modes whose frequencies and intensities reflect the geometry. In antiparallel β sheets this transition-dipole coupling splits amide I into a strong, low-frequency component near $1630\,\mathrm{cm^{-1}}$, polarized perpendicular to the strands, and a weak, high-frequency component near $1690\,\mathrm{cm^{-1}}$, polarized along them; the high-frequency component distinguishes antiparallel from parallel sheets. Intermolecular β sheets of amyloid fibrils and aggregates absorb even lower, at $1610$–$1625\,\mathrm{cm^{-1}}$.

| Structure | Amide I in $\ce{H2O}$ / $\mathrm{cm^{-1}}$ | Amide I in $\ce{D2O}$ / $\mathrm{cm^{-1}}$ |
|---|---|---|
| α helix | $1650$–$1658$ | $1648$–$1655$ |
| $3_{10}$ helix | $1660$–$1666$ | $1660$–$1666$ |
| Antiparallel β sheet | $1630$–$1635$ (strong), $1690$–$1695$ (weak) | $1625$–$1632$, $1675$–$1685$ |
| Parallel β sheet | $1630$–$1640$ | $1628$–$1635$ |
| Intermolecular β (aggregates, amyloid) | $1610$–$1625$, $1685$–$1695$ | $1610$–$1625$, $1680$–$1690$ |
| Turns | $1665$–$1685$ | $1660$–$1680$ |
| Disordered | $1655$–$1660$ | $1640$–$1648$ |

Water absorbs strongly at $1640\,\mathrm{cm^{-1}}$ (bending) and over $3000$–$3600\,\mathrm{cm^{-1}}$, on top of amide I; infrared spectra of proteins in $\ce{H2O}$ need path lengths of $6\,\mu\mathrm{m}$ or less and accurate subtraction of the buffer, and are often measured in $\ce{D2O}$, whose bending band lies at $1210\,\mathrm{cm^{-1}}$. Deuteration has a second use: the exchange of backbone $\ce{N-H}$ for $\ce{N-D}$ shifts amide II from about $1550$ to about $1450\,\mathrm{cm^{-1}}$, and the decay of the amide II band after transfer into $\ce{D2O}$ measures hydrogen–deuterium exchange of the whole protein, its residue-resolved version being measured by NMR and mass spectrometry ([7.6.13](/7.6.13)). In $\ce{D2O}$ the disordered component of amide I moves to about $1643\,\mathrm{cm^{-1}}$ and separates from the helix band, which barely moves.

### 11.4.4. Resolving Overlapping Bands

The amide I band of a protein is a single envelope, $50$–$70\,\mathrm{cm^{-1}}$ wide, made of components $10$–$20\,\mathrm{cm^{-1}}$ wide. Three mathematical procedures are used to resolve it, all of which trade signal-to-noise ratio for resolution and therefore need spectra of very high quality, with water vapor removed from the instrument and buffer subtracted accurately.

**Proposition 11.4.1 (Narrowing by the Second Derivative)** For a Lorentzian band $A(\tilde\nu) = A_0/[1 + ((\tilde\nu - \tilde\nu_0)/w)^2]$ of half width $w$, the negative second derivative has its maximum $2A_0/w^2$ at $\tilde\nu_0$ and a full width at half maximum of $0.65\,w$, a third of the original full width $2w$; for a Gaussian band the second derivative is narrowed to about half. Peak heights in the second derivative scale as $A_0/w^2$, so narrow components are enhanced relative to broad ones.

**Proof** With $x = (\tilde\nu - \tilde\nu_0)/w$, $-\mathrm{d}^2A/\mathrm{d}\tilde\nu^2 = (A_0/w^2)(2 - 6x^2)/(1 + x^2)^3$, equal to $2A_0/w^2$ at $x = 0$; setting it to half of this value and solving numerically gives $x = \pm0.327$. The Gaussian case is computed in the same way. $\square$

The second derivative locates the components but distorts their relative intensities. Fourier self-deconvolution divides the Fourier transform of the spectrum by that of an assumed Lorentzian line shape and applies an apodization function before transforming back; it preserves areas better but can create spurious side lobes if the assumed width is too large. Band fitting decomposes the original spectrum into Gaussian or Voigt components whose number and approximate positions come from the second derivative. Its result is not unique: a fit with many free parameters can reproduce an envelope within the noise with widely different component areas, and the conversion of areas to fractions assumes equal absorptivities of the components, which can differ by $30\,\%$ between structures.

![Amide I analysis (synthetic spectrum of a protein in D2O with five components: β sheet 1630, disordered 1643, α helix 1652, turns 1668 and high-frequency β 1684 cm⁻¹). A: the measured band is a broad envelope with two shoulders. B: the negative second derivative (Savitzky–Golay) resolves all five components, the narrow ones most strongly. C: a fit with five free Gaussians started from the second-derivative positions reproduces the envelope within the noise, yet assigns wrong fractions (a broad component absorbs intensity from its neighbors): band fitting must be constrained, for example by fixed widths or by independent data, to give reliable secondary-structure fractions](./plots/amide-i-fit.py)

Infrared spectroscopy is therefore most reliable for relative changes: the growth of the $1620\,\mathrm{cm^{-1}}$ band during amyloid formation, the conversion of helix to sheet, or the conformational change of a protein on ligand binding, followed in difference spectra in which unchanged parts cancel. Difference spectra with isotope-labeled residues and rapid-scan or step-scan Fourier-transform spectrometers follow single carboxyl groups and water molecules during the proton pumping of bacteriorhodopsin on microsecond time scales.

### 11.4.5. Sampling, Orientation and Applications

In **attenuated total reflectance** (ATR) the infrared beam is totally reflected inside a crystal of high refractive index $n_1$ (diamond $2.4$, germanium $4.0$, zinc selenide $2.4$), and the sample of index $n_2$ on its surface absorbs from the evanescent wave, whose amplitude decays as $\mathrm{e}^{-z/d_{\mathrm{p}}}$ with

$$
d_{\mathrm{p}} = \frac{\lambda_0}{2\pi\sqrt{n_1^2\sin^2\theta - n_2^2}}.
$$
For germanium at $45^\circ$ and $n_2 = 1.4$, $d_{\mathrm{p}} = 0.39\,\mu\mathrm{m}$ at $1650\,\mathrm{cm^{-1}}$; the short, reproducible path avoids the strong water absorption and makes ATR the method of choice for proteins in aqueous solution and for films of membranes deposited on the crystal. The same evanescent field, at visible wavelengths, is used for TIRF microscopy ([7.6.12](/7.6.12)).

Oriented samples, such as stacked membranes, fibers or stretched films, absorb polarized infrared light anisotropically, because absorption depends on $\lvert\boldsymbol{p}_{10}\cdot\boldsymbol{E}\rvert^2$ (Theorem 11.1.2). The dichroic ratio $R = A_\parallel/A_\perp$ between light polarized parallel and perpendicular to the director of a uniaxial sample is related to the order parameter of the transition dipoles, $S = \langle P_2(\cos\vartheta)\rangle = \langle(3\cos^2\vartheta - 1)/2\rangle$, by $R = (1 + 2S)/(1 - S)$, since $\langle\cos^2\vartheta\rangle = (1 + 2S)/3$ and the average of the squared perpendicular component is $(1 - S)/3$. For a helix tilted by $\beta$ from the director and a transition dipole at angle $\delta$ to the helix axis, $S = P_2(\cos\beta)P_2(\cos\delta)$. The amide I transition dipole makes about $38^\circ$ with the axis of an α helix, so a perfectly aligned transmembrane helix has $S = 0.43$ and $R = 3.3$, a helix lying in the membrane plane $S = -0.22$ and $R = 0.46$; the dichroism of amide I thus tells whether a peptide inserts into or lies on a membrane. (In ATR the measured ratio also depends on the field components of the evanescent wave, which are computed from the refractive indices.)

In lipids the symmetric and antisymmetric $\ce{CH2}$ stretches near $2850$ and $2920\,\mathrm{cm^{-1}}$ shift up by $2$–$4\,\mathrm{cm^{-1}}$ when the chains melt from the gel to the fluid phase, so infrared spectroscopy follows the phase transitions of membranes measured calorimetrically in [7.6.8](/7.6.8). In nucleic acids, bands between $1800$ and $1500\,\mathrm{cm^{-1}}$ report base pairing and stacking, those between $1500$ and $1250\,\mathrm{cm^{-1}}$ the glycosidic torsion and sugar pucker, and the phosphate stretches near $1220$ and $1090\,\mathrm{cm^{-1}}$ the backbone conformation and hydration (A, B and Z forms have distinct marker bands). Raman spectra of whole viruses, such as the P22 phage, reveal the secondary structure of the coat proteins, the conformation of the packaged DNA and even the hydrogen bonding of individual cysteine $\ce{S-H}$ groups (near $2570\,\mathrm{cm^{-1}}$), without disrupting the particle.

## 11.5. Fluorescence

### 11.5.1. Intensity, Lifetime and Quantum Yield

**Fluorescence** is spontaneous emission from $\mathrm{S}_1$. It is at least two to three orders of magnitude more sensitive than absorption, because it is measured against a dark background rather than as a small difference of two large intensities, and it carries more information: its spectrum, intensity, lifetime and polarization each respond to the environment and motion of the emitting group during the nanoseconds of the excited state. In dilute solution ($A < 0.05$) the intensity measured in a fluorometer is

$$
F = 2.303\,I_0\,\varepsilon(\lambda_{\mathrm{ex}})\,c\,l\,\Phi\,Z,
$$
the absorbed photon flux times the quantum yield times an instrumental collection factor $Z$; at higher absorbance the excitation is attenuated before the observed volume and the emission is reabsorbed, the **inner filter effect**, for which $F_{\operatorname{Corr}} \approx F_{\mathrm{obs}}10^{(A_{\mathrm{ex}} + A_{\mathrm{em}})/2}$ is a common correction. Since the observable is relative, quantum yields are measured against standards (quinine sulfate, fluorescein), and the most robust observables are those independent of concentration: the shape and position of the spectrum, the lifetime and the anisotropy.

The radiative rate is fixed by the absorption band, because both are governed by the same transition dipole (Theorem 11.1.2 and the **Einstein coefficients**). The Strickler–Berg relation, $k_{\mathrm{r}} \approx 2.88\times10^{-9}\,n^2\tilde\nu_{\max}^2\int\varepsilon\,\mathrm{d}\tilde\nu$ ($\tilde\nu$ in $\mathrm{cm^{-1}}$, $k_{\mathrm{r}}$ in $\mathrm{s^{-1}}$), gives natural lifetimes of a few nanoseconds for strongly allowed bands ($\varepsilon_{\max} \approx 10^5$) and of hundreds of nanoseconds for weak ones. Measured lifetimes and yields then separate $k_{\mathrm{r}} = \Phi/\tau$ from the radiationless rate $k_{\mathrm{nr}} = (1 - \Phi)/\tau$ (Formula 11.1.3). Lifetimes are measured by time-correlated single-photon counting or in the frequency domain ([6.4.10](/6.4.10#sec-10.3.3)); multiexponential decays are the rule for tryptophan in proteins and reveal heterogeneity of environments.

### 11.5.2. Solvent Relaxation and Environmental Sensitivity

The excited state of many fluorophores has a larger dipole moment than the ground state. Immediately after absorption the solvent around the molecule is still arranged for the ground-state dipole (a Franck–Condon state); within picoseconds the solvent molecules reorient to stabilize the new dipole, lowering the energy of $\mathrm{S}_1$, and emission then leads to a ground state surrounded by a solvent arranged for the excited state. Both steps lower the energy of the emitted photon. This general solvent effect, which depends only on the dielectric properties of the solvent, is described by the Lippert–Mataga equation.

**Formula 11.5.1 (Lippert–Mataga Equation)** For a fluorophore modeled as a point dipole in a spherical cavity of radius $a$, with dipole moments $p_{\mathrm{G}}$ and $p_{\mathrm{E}}$ in the ground and excited states, in a solvent of relative permittivity $\varepsilon_{\mathrm{r}}$ and refractive index $n$,

$$
\tilde\nu_{\mathrm{abs}} - \tilde\nu_{\mathrm{em}} = \frac{2\Delta f}{4\pi\varepsilon_0hca^3}(p_{\mathrm{E}} - p_{\mathrm{G}})^2 + \text{const}, \qquad
\Delta f = \frac{\varepsilon_{\mathrm{r}} - 1}{2\varepsilon_{\mathrm{r}} + 1} - \frac{n^2 - 1}{2n^2 + 1}.
$$
The orientation polarizability $\Delta f$ subtracts the fast electronic polarization (through $n^2$), which follows the excitation instantly, from the total polarization.

**Example 11.5.1 (Stokes Shift in Water)** Water has $\Delta f = 77/157 - 0.777/4.554 = 0.32$, cyclohexane $\Delta f \approx 0$. A probe whose dipole increases by $10\,\mathrm{D}$ on excitation, in a cavity of $0.5\,\mathrm{nm}$, gains $2\times0.32\times(3.34\times10^{-29})^2/(4\pi\varepsilon_0hc(5\times10^{-10})^3) \approx 2600\,\mathrm{cm^{-1}}$ of additional Stokes shift in water, about $70\,\mathrm{nm}$ for emission near $450\,\mathrm{nm}$.

Specific effects add to this: hydrogen bonding, proton transfer in the excited state, and the formation of charge-transfer states. Probes that exploit environmental sensitivity are blue shifted and brighter in hydrophobic sites. 1-Anilinonaphthalene-8-sulfonate (ANS) fluoresces weakly in water (lifetime about $0.25\,\mathrm{ns}$, maximum $515\,\mathrm{nm}$) and strongly when bound to hydrophobic patches of proteins (lifetime of several nanoseconds, maximum near $470\,\mathrm{nm}$); it binds avidly to molten globules and partly folded intermediates and is used to detect them ([7.6.16](/7.6.16)). Prodan, Laurdan and Nile red report the polarity and water content of membranes and condensates.

### 11.5.3. Intrinsic Fluorescence of Proteins

| | Trp | Tyr | Phe |
|---|---|---|---|
| Absorption maximum / nm | $280$ | $274$ | $257$ |
| $\varepsilon_{\max}$ / ($\mathrm{L\,mol^{-1}\,cm^{-1}}$) | $5600$ | $1400$ | $200$ |
| Emission maximum in water / nm | $\approx 350$ | $\approx 303$ | $\approx 282$ |
| Quantum yield | $0.13$ | $0.14$ | $0.02$ |
| Lifetime / ns | $3.1$ (multiexponential) | $3.6$ | $6.4$ |
| Brightness $\varepsilon\Phi$ | $730$ | $200$ | $4$ |

Phenylalanine is negligible, and tyrosine emission is often transferred to tryptophan or quenched in folded proteins, so the intrinsic fluorescence of most proteins is that of tryptophan; excitation at $295$–$300\,\mathrm{nm}$, on the red edge of the absorption, excites tryptophan alone. Tryptophan emission is exceptionally sensitive to its environment because its $^1\mathrm{L}_\mathrm{a}$ excited state has a large dipole moment and can be quenched by electron transfer to nearby peptide carbonyls, protonated histidines and disulfides. Fully buried, rigid tryptophans emit near $308$–$320\,\mathrm{nm}$ (azurin is the extreme), partly buried ones near $330\,\mathrm{nm}$, those on the surface in contact with bound water near $340\,\mathrm{nm}$, and fully exposed ones, as in the unfolded protein or free in water, near $350\,\mathrm{nm}$. The quantum yield varies from below $0.01$ to $0.3$ with the local quenching groups, so unfolding can increase or decrease intensity, but nearly always shifts the spectrum to the red.

A useful check of two-state behavior uses intensities at two wavelengths. If a protein unfolds between two states with fixed spectra $F_{\mathrm{N}}(\lambda)$ and $F_{\mathrm{U}}(\lambda)$, then $F(\lambda_1) = F_{\mathrm{N}}(\lambda_1) + f[F_{\mathrm{U}}(\lambda_1) - F_{\mathrm{N}}(\lambda_1)]$ and likewise at $\lambda_2$; eliminating the fraction $f$ shows that the points $(F(\lambda_1), F(\lambda_2))$ measured at all denaturant concentrations lie on a straight line. A kink in this "phase diagram" reveals a third state with a different spectrum; a straight line is consistent with, but does not prove, two-state behavior, since intermediates whose spectra are linear combinations of the end states remain invisible. Ratios such as $F_{320}/F_{365}$ (the "parameter A") condense the spectral shift into one number that is insensitive to the absolute intensity.

### 11.5.4. Quenching

Any process that depopulates $\mathrm{S}_1$ without emission quenches fluorescence ([6.4.10](/6.4.10#sec-10.2.3)). In collisional (dynamic) **quenching** a quencher Q deactivates the excited fluorophore on contact; in static quenching Q forms a nonfluorescent complex with the fluorophore in its ground state.

**Theorem 11.5.1 (Stern–Volmer Equations)** (a) For dynamic quenching with bimolecular rate constant $k_{\mathrm{q}}$, the steady-state intensities and lifetimes with and without quencher satisfy

$$
\frac{F_0}{F} = \frac{\tau_0}{\tau} = 1 + k_{\mathrm{q}}\tau_0[\ce{Q}] = 1 + K_{\mathrm{D}}[\ce{Q}].
$$
(b) For static quenching by complex formation with association constant $K_{\mathrm{S}}$, $F_0/F = 1 + K_{\mathrm{S}}[\ce{Q}]$ while $\tau_0/\tau = 1$. (c) If both occur, $F_0/F = (1 + K_{\mathrm{D}}[\ce{Q}])(1 + K_{\mathrm{S}}[\ce{Q}])$, a parabola, while $\tau_0/\tau = 1 + K_{\mathrm{D}}[\ce{Q}]$ remains linear.

**Proof** (a) Under steady illumination at excitation rate $k_{\mathrm{ex}}$, $\mathrm{d}[\mathrm{S}_1]/\mathrm{d}t = k_{\mathrm{ex}} - (1/\tau_0 + k_{\mathrm{q}}[\ce{Q}])[\mathrm{S}_1] = 0$, and $F \propto k_{\mathrm{r}}[\mathrm{S}_1]$, so $F_0/F = 1 + k_{\mathrm{q}}\tau_0[\ce{Q}]$; the lifetime is the inverse of the total decay rate, $1/\tau = 1/\tau_0 + k_{\mathrm{q}}[\ce{Q}]$. (b) Only the free fraction $1/(1 + K_{\mathrm{S}}[\ce{Q}])$ of fluorophores emits, with its unchanged lifetime. (c) The free fraction emits with the dynamically quenched yield. $\square$

The size of $k_{\mathrm{q}}$ distinguishes contact quenching from long-range mechanisms. For a **diffusion-controlled reaction** between spheres of radii summing to $R$ and diffusion coefficients summing to $D$, $k_{\mathrm{q}} = 4\pi RDN_{\mathrm{A}}$ (the Smoluchowski rate of [7.6.5](/7.6.5#fml-5.2.3)): $R = 0.6\,\mathrm{nm}$ and $D = 1.6\times10^{-9}\,\mathrm{m^2\,s^{-1}}$ give $7\times10^9\,\mathrm{M^{-1}\,s^{-1}}$, the observed order of magnitude for acrylamide and free tryptophan, and with $\tau_0 = 3\,\mathrm{ns}$ a Stern–Volmer constant of about $20\,\mathrm{M^{-1}}$. Values of $k_{\mathrm{q}}$ much larger than diffusion-limited point to static quenching or energy transfer; values much smaller to shielding of the fluorophore. Raising the temperature increases dynamic quenching (faster diffusion) and decreases static quenching (dissociation of the complex), a second way to tell them apart.

**Formula 11.5.2 (Lehrer Plot)** If a fraction $f_{\mathrm{a}}$ of the fluorescence comes from fluorophores accessible to the quencher (constant $K_{\mathrm{a}}$) and the rest is inaccessible, then $F_0/\Delta F = 1/(f_{\mathrm{a}}K_{\mathrm{a}}[\ce{Q}]) + 1/f_{\mathrm{a}}$ with $\Delta F = F_0 - F$: a plot of $F_0/\Delta F$ against $1/[\ce{Q}]$ is linear with intercept $1/f_{\mathrm{a}}$.

![Fluorescence quenching (simulated tryptophan data, τ0 = 3 ns). A: dynamic quenching (K_D = 18 M⁻¹) gives identical linear plots of F0/F and τ0/τ; static quenching (K_S = 8 M⁻¹) lowers the intensity but not the lifetime; both together give an upward-curving F0/F while τ0/τ stays linear. B: a protein with an exposed (K = 15 M⁻¹) and a buried (K = 0.05 M⁻¹) tryptophan, each contributing half of the fluorescence: the Stern–Volmer plot bends downward towards the plateau set by the inaccessible fluorophore. C: the Lehrer plot of the same data is linear, and its intercept 1/f_a ≈ 2 recovers the accessible fraction](./plots/stern-volmer.py)

Comparing quenchers of different charge and size maps the exposure of tryptophans: iodide, charged and hydrated, reaches only surface residues and is repelled by negative charge; acrylamide, neutral and polar, penetrates further; oxygen, small and apolar, penetrates proteins almost everywhere and quenches even buried tryptophans, evidence that protein interiors fluctuate on the nanosecond scale (Lakowicz and Weber, 1973). In living systems, quenching is a function: photosynthetic antennas switch on nonphotochemical quenching to dissipate excess excitation as heat ([7.6.18](/7.6.18)).

### 11.5.5. Photoselection and Fluorescence Anisotropy

Excitation with linearly polarized light selects molecules whose absorption transition dipoles are parallel to the polarization, since the absorption probability is $\cos^2\theta$ (Theorem 11.1.2). The emission of the selected molecules is then partly polarized, and its polarization decays as the molecules rotate.

**Definition 11.5.1 (Fluorescence Anisotropy)** With vertically polarized excitation, let $I_\parallel$ and $I_\perp$ be the emission intensities polarized parallel and perpendicular to the excitation, observed at right angles. The **fluorescence anisotropy** is

$$
r = \frac{I_\parallel - I_\perp}{I_\parallel + 2I_\perp},
$$
and the polarization is $P = (I_\parallel - I_\perp)/(I_\parallel + I_\perp)$, with $r = 2P/(3 - P)$. The denominator of $r$ is proportional to the total emission in all directions, so anisotropies of components add with their intensity weights, $r = \sum_if_ir_i$ with $f_i$ the fractional intensities; polarizations do not.

**Theorem 11.5.2 (Fundamental Anisotropy)** For an isotropic sample of immobile fluorophores whose absorption and emission transition dipoles make the angle $\beta$, the anisotropy is

$$
r_0 = \frac25\,P_2(\cos\beta) = \frac25\cdot\frac{3\cos^2\beta - 1}{2},
$$
between $0.4$ ($\beta = 0$) and $-0.2$ ($\beta = 90^\circ$), and zero at the magic angle $\beta = 54.7^\circ$.

**Proof** Let the excitation be polarized along $z$ and first let $\beta = 0$. A dipole at polar angle $\theta$ and azimuth $\varphi$ is excited with probability proportional to $\cos^2\theta$ and emits along $z$ and $x$ intensities proportional to $\cos^2\theta$ and $\sin^2\theta\cos^2\varphi$. Averaging over the isotropic distribution with the weight $\cos^2\theta$, $I_\parallel \propto \langle\cos^4\theta\rangle = 1/5$ and $I_\perp \propto \langle\cos^2\theta\sin^2\theta\cos^2\varphi\rangle = \frac12(1/3 - 1/5) = 1/15$, so $r_0 = (1/5 - 1/15)/(1/5 + 2/15) = 2/5$. If the emission dipole is at angle $\beta$ to the absorption dipole, with random azimuth about it, the addition theorem of spherical harmonics gives $\langle P_2(\cos\theta_{\mathrm{em}})\rangle = P_2(\cos\beta)\langle P_2(\cos\theta_{\mathrm{abs}})\rangle$, and since $r$ is proportional to $\langle P_2\rangle$ of the emission dipole the anisotropy is multiplied by $P_2(\cos\beta)$. $\square$

Measured fundamental anisotropies of tryptophan in vitrified solution range from about $0.3$ at $300\,\mathrm{nm}$ excitation to near $0$ at $290\,\mathrm{nm}$, because two overlapping, nearly perpendicular transitions ($^1\mathrm{L}_\mathrm{a}$ and $^1\mathrm{L}_\mathrm{b}$) absorb there; many dyes reach $0.37$–$0.39$. In practice the detection channels have different sensitivities, which is corrected with the $G$ factor measured with horizontally polarized excitation, $r = (I_{\mathrm{VV}} - GI_{\mathrm{VH}})/(I_{\mathrm{VV}} + 2GI_{\mathrm{VH}})$. Conversely, intensity and lifetime measurements that must be insensitive to rotation are made with an emission polarizer at $54.7^\circ$ to the excitation polarization (magic-angle conditions).

### 11.5.6. Rotational Diffusion and the Perrin Equation

**Definition 11.5.2 (Rotational Correlation Time)** The *rotational correlation time* $\tau_{\mathrm{rot}}$ of a molecule is the decay time of the orientational correlation function $\langle P_2(\boldsymbol{u}(0)\cdot\boldsymbol{u}(t))\rangle$ of a vector $\boldsymbol{u}$ fixed in it. For a sphere with rotational diffusion coefficient $D_{\mathrm{r}}$, $\tau_{\mathrm{rot}} = 1/(6D_{\mathrm{r}}) = \eta V/(k_{\mathrm{B}}T)$ ([7.6.5](/7.6.5#fml-5.3.2)).

Since the anisotropy is proportional to $\langle P_2\rangle$ of the emission dipole, rotation multiplies it by the orientational correlation function. For a rigid spherical molecule with a rigidly attached fluorophore,

$$
r(t) = r_0\,\mathrm{e}^{-t/\tau_{\mathrm{rot}}}, \tag{11.3}
$$
measured directly by polarized time-resolved fluorescence. Nonspherical molecules have up to five exponential terms, with correlation times that depend on the axial ratio ([7.6.8](/7.6.8#sec-8.7.3)).

**Theorem 11.5.3 (Perrin Equation)** For a fluorophore with single-exponential lifetime $\tau$ on a sphere, the steady-state anisotropy is

$$
r = \frac{r_0}{1 + \tau/\tau_{\mathrm{rot}}}, \qquad \frac{1}{r} = \frac{1}{r_0}\left(1 + \frac{\tau k_{\mathrm{B}}T}{\eta V}\right).
$$

**Proof** The steady-state anisotropy is the time average of $r(t)$ weighted by the emission $\mathrm{e}^{-t/\tau}/\tau$: $r = \int_0^\infty r_0\mathrm{e}^{-t/\tau_{\mathrm{rot}}}\mathrm{e}^{-t/\tau}\,\mathrm{d}t/\tau = r_0/(1 + \tau/\tau_{\mathrm{rot}})$. $\square$

A plot of $1/r$ against $T/\eta$, varied with temperature or glycerol (a Perrin plot), gives $r_0$ from the intercept and the hydrodynamic volume from the slope. The rotational correlation time of a globular protein in water at $20\,^\circ\mathrm{C}$, with hydrated volume $V = M(\bar v + h)/N_{\mathrm{A}}$ ($\bar v = 0.73\,\mathrm{mL\,g^{-1}}$, hydration $h = 0.3\,\mathrm{g\,g^{-1}}$), is about $0.42\,\mathrm{ns}$ per kilodalton: about $10\,\mathrm{ns}$ for $25\,\mathrm{kDa}$, comparable to fluorescence lifetimes. This coincidence makes anisotropy sensitive to the size of proteins and complexes.

**Example 11.5.2 (A Polarization Binding Assay)** A fluorescein-labeled peptide of $2\,\mathrm{kDa}$ ($\tau_{\mathrm{rot}} \approx 0.8\,\mathrm{ns}$, $\tau = 4\,\mathrm{ns}$, $r_0 = 0.38$) has $r = 0.38/(1 + 4/0.8) = 0.066$ free; bound to a $50\,\mathrm{kDa}$ protein ($\tau_{\mathrm{rot}} \approx 22\,\mathrm{ns}$) it has $r = 0.32$. Titrating $5\,\mathrm{nM}$ labeled peptide with protein then gives a binding curve without separating bound and free ligand. If binding changes the quantum yield by the factor $Q = \Phi_{\mathrm{B}}/\Phi_{\mathrm{F}}$, the anisotropies add with intensity weights and the bound fraction is $f_{\mathrm{B}} = (r - r_{\mathrm{F}})/[(r_{\mathrm{B}} - r)Q + (r - r_{\mathrm{F}})]$. Assays of this kind, which need only a mix-and-read step, are a standard of high-throughput screening.

![Fluorescence anisotropy. A: photoselection: polarized excitation creates an excited population distributed as cos²θ about the polarization (polar plot), from which r0 = 0.4 P2(cos β) follows. B: time-resolved anisotropy of a 25 kDa protein (τ_rot = 10.6 ns at 20 °C) and of its dimer, of a label that also wobbles rapidly (0.5 ns) in a cone (order parameter S² = 0.5) on the monomer, and the intensity decay (τ = 4 ns) that limits the observable time window. C: steady-state anisotropy of 5 nM of a labeled 2 kDa peptide titrated with a 50 kDa protein of K_D = 100 nM: r rises from the free to the bound value, read through the Perrin equation](./plots/anisotropy.py)

Most fluorophores are not rigidly attached. Local motion within a cone of semi-angle $\theta_{\mathrm{c}}$ adds a fast component, $r(t) = r_0[(1 - S^2)\mathrm{e}^{-t/\tau_{\mathrm{f}}} + S^2]\mathrm{e}^{-t/\tau_{\mathrm{rot}}}$, with the order parameter $S = \frac12\cos\theta_{\mathrm{c}}(1 + \cos\theta_{\mathrm{c}})$; the fast amplitude measures the flexibility of the label or of the segment carrying it, and the slow time the overall tumbling. The same order parameter appears in NMR relaxation ([7.6.13](/7.6.13)). In membranes the anisotropy of probes such as diphenylhexatriene reports lipid order, and the residual anisotropy $r_\infty = r_0S^2$ distinguishes gel from fluid phases. Homo-FRET between identical fluorophores also depolarizes the emission, which is used to detect clustering of proteins in cells.

### 11.5.7. Förster Resonance Energy Transfer

An excited donor D can transfer its energy without emission to an acceptor A whose absorption overlaps the donor emission. When the coupling is much smaller than the widths of the bands, as it is for chromophores more than about $2\,\mathrm{nm}$ apart, the excitation does not delocalize (compare 11.2.5) but hops incoherently, at a rate given by Fermi's golden rule. This is **Förster resonance energy transfer** (FRET).

**Theorem 11.5.4 (Förster Rate)** For point transition dipoles at distance $R$ in a medium of refractive index $n$, the rate of energy transfer is

$$
k_{\mathrm{T}} = \frac{1}{\tau_{\mathrm{D}}}\left(\frac{R_0}{R}\right)^6, \qquad
R_0^6 = \frac{9\ln10\,\kappa^2\Phi_{\mathrm{D}}J}{128\pi^5N_{\mathrm{A}}n^4}, \qquad
J = \int F_{\mathrm{D}}(\lambda)\,\varepsilon_{\mathrm{A}}(\lambda)\,\lambda^4\,\mathrm{d}\lambda,
$$
where $\tau_{\mathrm{D}}$ and $\Phi_{\mathrm{D}}$ are the lifetime and quantum yield of the donor without acceptor, $F_{\mathrm{D}}$ the donor emission spectrum normalized to unit area, $\varepsilon_{\mathrm{A}}$ the molar absorption coefficient of the acceptor, and

$$
\kappa^2 = (\cos\theta_{\mathrm{T}} - 3\cos\theta_{\mathrm{D}}\cos\theta_{\mathrm{A}})^2
$$
the orientation factor ($\theta_{\mathrm{T}}$ the angle between the dipoles, $\theta_{\mathrm{D}}$, $\theta_{\mathrm{A}}$ their angles to the line joining them). In practical units, $R_0 = 0.0211\,(\kappa^2\Phi_{\mathrm{D}}n^{-4}J)^{1/6}\,\mathrm{nm}$ with $J$ in $\mathrm{L\,mol^{-1}\,cm^{-1}\,nm^4}$.

**Proof** (outline) The interaction energy of the two transition dipoles is $V = \kappa\,p_{\mathrm{D}}p_{\mathrm{A}}/(4\pi\varepsilon_0n^2R^3)$, as in 11.2.5. The golden rule gives $k_{\mathrm{T}} = (2\pi/\hbar)\lvert V\rvert^2\rho$, where $\rho$ is the density of states for which donor de-excitation and acceptor excitation conserve energy, that is the overlap of the normalized donor emission and acceptor absorption line shapes. Hence $k_{\mathrm{T}} \propto \kappa^2p_{\mathrm{D}}^2p_{\mathrm{A}}^2R^{-6}\int g_{\mathrm{D}}g_{\mathrm{A}}$. The squared acceptor dipole and line shape are expressed through the measured absorption $\varepsilon_{\mathrm{A}}(\lambda)$ (Formula 11.1.2), and the squared donor dipole through its radiative rate $k_{\mathrm{r}} = \Phi_{\mathrm{D}}/\tau_{\mathrm{D}}$ and emission spectrum (Einstein relation between absorption and emission). Collecting constants gives the expression above; the factors $\lambda^4$ and $n^{-4}$ come from converting the dipole strengths and field screening to wavelengths and the medium. $\square$

**Formula 11.5.3 (Transfer Efficiency)** The efficiency, the fraction of donor excitations transferred, is

$$
E = \frac{k_{\mathrm{T}}}{k_{\mathrm{T}} + 1/\tau_{\mathrm{D}}} = \frac{1}{1 + (R/R_0)^6} = 1 - \frac{\tau_{\mathrm{DA}}}{\tau_{\mathrm{D}}} = 1 - \frac{F_{\mathrm{DA}}}{F_{\mathrm{D}}},
$$
measurable from the quenching of the donor (lifetime or intensity) or the sensitized emission of the acceptor. $R_0$, the *Förster radius*, is the distance at which $E = 1/2$.

The steep $R^{-6}$ law makes $E$ change from $0.98$ to $0.08$ between $0.5R_0$ and $1.5R_0$, and $R_0$ of common pairs lies between $2$ and $8\,\mathrm{nm}$, the size of proteins and their complexes. Stryer and Haugland (1967) confirmed the law with donor and acceptor at the two ends of rigid oligoprolines and called FRET a spectroscopic ruler.

**Example 11.5.3 (Förster Radius of Cy3–Cy5)** With $\Phi_{\mathrm{D}} = 0.3$ (Cy3 attached to DNA), $\kappa^2 = 2/3$, $n = 1.4$ and $J = 6\times10^{15}\,\mathrm{L\,mol^{-1}\,cm^{-1}\,nm^4}$, $\kappa^2\Phi_{\mathrm{D}}n^{-4}J = 3.1\times10^{14}$, whose sixth root is $261$, so $R_0 = 0.0211\times261 = 5.5\,\mathrm{nm}$. A tenfold error in $J$ would change $R_0$ by only $47\,\%$ ($10^{1/6} = 1.47$), and a factor of $2$ in $\kappa^2$ by $12\,\%$.

![Förster resonance energy transfer. A: efficiency against donor–acceptor distance for R0 = 2.5, 5.4 and 7 nm; the shaded band, 0.5 R0 to 1.5 R0 for the Cy3–Cy5 pair, is where E is most sensitive to distance. B: spectral overlap: normalized donor emission, acceptor absorption (model Cy3/Cy5 shapes) and the integrand F_D ε_A λ⁴ of the overlap integral J, weighted towards long wavelengths by λ⁴. C: distribution of κ² for randomly oriented but static dipoles (Monte Carlo): the mean is 2/3, but values range from 0 to 4 and the median is about 0.43, so a single static pair can deviate strongly from the isotropic value](./plots/fret.py)

The orientation factor is the main uncertainty in converting $E$ into $R$. For donor and acceptor that rotate freely and fast compared with the transfer time, $\kappa^2$ averages to $2/3$. For static random orientations its distribution is broad (panel C), although its effect on $R$ is damped by the sixth root. Low anisotropies of both dyes (11.5.5), measured on the labeled molecule, show that the dynamic average applies and bound the possible error; in single-molecule studies with flexible linkers distances are typically accurate to $5$–$10\,\%$ ([7.6.12](/7.6.12)). The point-dipole approximation itself fails below about $2\,\mathrm{nm}$, where the shapes of the transition densities matter, and below about $1\,\mathrm{nm}$ electron exchange (Dexter transfer) and contact quenching take over.

FRET is used in three ways. As a ruler, it measures distances and their changes within and between molecules: the bending of DNA by proteins, the conformations of the Holliday junction, the folding of ribozymes, the opening of transporters. As a proximity sensor, it reports the binding of two labeled partners, in solution and in living cells, where FRET between fluorescent proteins (CFP–YFP, mTurquoise–mVenus) is measured by acceptor photobleaching or by the lifetime of the donor ([7.3.2](/7.3.2#sec-2.6.3)). As a transducer, it converts a conformational change into a ratiometric color change in genetically encoded biosensors for calcium (cameleons), cAMP, kinase activities and mechanical tension ([6.4.10](/6.4.10#sec-10.3.4)). Between tyrosine and tryptophan, and between tryptophan and bound ligands such as dansyl groups or NADH, FRET occurs naturally and contributes to the quenching of intrinsic fluorescence in proteins.

### 11.5.8. Fluorescent Probes in Practice

Intrinsic fluorophores are limited to tryptophan, tyrosine and a few cofactors. NADH ($\lambda_{\mathrm{ex}} = 340\,\mathrm{nm}$, $\lambda_{\mathrm{em}} = 460\,\mathrm{nm}$) fluoresces and $\ce{NAD+}$ does not, while oxidized FAD fluoresces and $\mathrm{FADH_2}$ does not; the ratio of their autofluorescence is used to image the redox state of cells, and the lifetime of NADH distinguishes the free from the enzyme-bound pool. The nucleobases do not fluoresce usefully, but analogs such as 2-aminopurine do, and their fluorescence is quenched by stacking, a local probe of base flipping by DNA repair enzymes. Most experiments use extrinsic probes:

| Probe class | Examples | Size | Strengths | Limitations |
|---|---|---|---|---|
| Organic dyes | fluoresceins, rhodamines, cyanines (Cy3, Cy5), Alexa, Atto | $< 1\,\mathrm{nm}$, $0.5$–$1\,\mathrm{kDa}$ | bright ($\varepsilon \approx 10^5$), photostable with oxygen scavengers, $10^5$–$10^6$ photons before bleaching | site-specific labeling chemistry; possible perturbation |
| **Fluorescent proteins** | GFP variants, mCherry, photoactivatable and photoswitchable proteins | $27\,\mathrm{kDa}$, $2$–$4\,\mathrm{nm}$ | genetically encoded, fusion to any protein ([6.4.10](/6.4.10#sec-10.5)) | dimmer, $10^4$–$10^5$ photons before bleaching; maturation time |
| Self-labeling tags | HaloTag, SNAP-tag, CLIP-tag with dye ligands | $20$–$33\,\mathrm{kDa}$ | genetic targeting with dye brightness | ligand delivery, background |
| **Quantum dots** | CdSe/ZnS core–shell nanocrystals | $10$–$30\,\mathrm{nm}$ with coating | very bright, narrow emission tunable by size, almost no bleaching | large, blinking, multivalent attachment |
| Environment-sensitive dyes | ANS, Prodan, Laurdan, thioflavin T | small | report polarity, viscosity, amyloid | noncovalent, ambiguous binding sites |

Three artifacts recur. Light scattered by the solvent appears as a sharp peak at a fixed wavenumber shift: the $\ce{O-H}$ stretching Raman band of water lies $3400\,\mathrm{cm^{-1}}$ below the excitation, at $310\,\mathrm{nm}$ for excitation at $280\,\mathrm{nm}$ and at $328\,\mathrm{nm}$ for $295\,\mathrm{nm}$, inside the tryptophan emission band, and must be subtracted with a buffer blank. Concentrated samples suffer the inner filter effect (11.5.1). Intense illumination bleaches fluorophores, mostly through reactions of the triplet state with oxygen; in kinetic and imaging experiments the light dose must be controlled, and in single-molecule work oxygen is removed enzymatically and triplets are quenched chemically ([7.6.12](/7.6.12)).

## 11.6. Choosing a Spectroscopic Method

| Method | Observable | Reports | Sample | Time resolution | Main limitation |
|---|---|---|---|---|---|
| UV–visible absorption | $\varepsilon(\lambda)$, $A_{260}$, $A_{280}$ | concentration, purity, cofactor state, DNA melting (hypochromism) | $\mu\mathrm{g}$, any buffer above $230\,\mathrm{nm}$ | ms (stopped flow) to hours | little structural detail |
| Far-UV CD | $[\theta]$, $180$–$250\,\mathrm{nm}$ | secondary structure, folding, stability | $10$–$100\,\mu\mathrm{g}$, transparent buffer | ms (stopped flow) | basis-set errors, β fractions $\pm10\,\%$ |
| Near-UV and visible CD | $[\theta]$, $250$–$700\,\mathrm{nm}$ | tertiary packing, cofactor environment, nucleic acid conformation | mg | s | empirical interpretation |
| Infrared (FTIR, ATR) | amide I, II; difference spectra | secondary structure, aggregates, H/D exchange, single groups in difference spectra | $10$–$100\,\mu\mathrm{g}$, $\ce{D2O}$ or ATR | $\mu\mathrm{s}$ (step scan) | water absorption, overlapping bands |
| Raman, resonance Raman | vibrational shifts | conformation in any phase; chromophore structure inside proteins | solutions, crystals, cells | ps (pump–probe) | weak signal, fluorescence background |
| Steady-state fluorescence | $\lambda_{\max}$, intensity | environment of Trp or probes, binding, unfolding | nM–$\mu\mathrm{M}$ | ms | indirect, probe perturbation |
| Lifetime and quenching | $\tau$, $K_{\mathrm{SV}}$ | accessibility, heterogeneity | nM–$\mu\mathrm{M}$ | ps–ns | multiexponential analysis |
| Anisotropy | $r$, $r(t)$ | rotational correlation time, size, binding, flexibility | nM | ns | only for $\tau_{\mathrm{rot}} \lesssim 10\tau$ |
| FRET | $E$ | distances of $2$–$10\,\mathrm{nm}$, proximity, sensors | nM to single molecules | ns to hours | labeling, $\kappa^2$, linkers |

The methods are complementary rather than competing. A typical characterization of a new protein uses absorbance to measure its concentration, far-UV CD to confirm its fold and measure its thermal stability, tryptophan fluorescence to follow its denaturation and the binding of ligands, and FRET or anisotropy to follow its interactions; the structure itself comes from the high-resolution methods of [7.6.10](/7.6.10), [7.6.13](/7.6.13) and [7.6.14](/7.6.14), which optical spectra then test in solution and over time.

## Summary

Light and matter (11.1):

- The classical oscillator gives a complex refractive index whose imaginary part is the absorption band and whose real part shows anomalous dispersion (Formula 11.1.1); absorption and dispersion are Kramers–Kronig partners.
- Beer–Lambert law $A = \varepsilon cl$, with the cross-section $\sigma = 3.82\times10^{-21}\varepsilon\,\mathrm{cm^2}$ (Theorem 11.1.1).
- Absorption is driven by the transition dipole $\boldsymbol{p}_{fi} = \langle f\rvert\hat{\boldsymbol{p}}\lvert i\rangle$ (Definition 11.1.1), at a rate $\propto\lvert\boldsymbol{p}_{fi}\cdot\boldsymbol{E}_0\rvert^2$ (Theorem 11.1.2); dipole and oscillator strengths follow from the integrated band (Formula 11.1.2).
- Franck–Condon factors (Definition 11.1.2) of displaced oscillators form a Poisson progression with Huang–Rhys factor $S$; the Stokes shift is about $2S\hbar\omega$ (Proposition 11.1.1). Excited-state kinetics: $\tau = 1/\sum k$, $\Phi = k_{\mathrm{r}}\tau$ (Formula 11.1.3).

Absorption and circular dichroism (11.2–11.3):

| Quantity | Formula | Use |
|---|---|---|
| $\varepsilon_{280}$ of a protein | $5500n_{\mathrm{W}} + 1490n_{\mathrm{Y}} + 125n_{\mathrm{C}}$ (Formula 11.2.1) | concentration |
| Two-state melting | $f = K/(1 + K)$, $\mathrm{d}f/\mathrm{d}T\rvert_{T_{\mathrm{m}}} = \Delta H/4RT_{\mathrm{m}}^2$; bimolecular $1/T_{\mathrm{m}}$ linear in $\ln C_{\mathrm{T}}$ (Formula 11.2.2) | duplex thermodynamics |
| Exciton dimer | $E_\pm = E_0 \pm V_{12}$, $V_{12} \propto \kappa p^2/R^3$; dipole strengths $p^2(1 \pm \cos\theta_{12})$; opposite rotational strengths (Theorem 11.2.1) | hypochromism, H/J aggregates, CD couplets |
| Ellipticity | $\theta = 32.98\,\Delta A$ deg, $[\theta] = 3298\,\Delta\varepsilon$ (Proposition 11.3.1) | CD units |
| Rotational strength | $R = \operatorname{Im}(\boldsymbol{p}_{0a}\cdot\boldsymbol{m}_{a0})$ (Theorem 11.3.1) | origin of CD |
| Secondary structure | $[\theta](\lambda) = \sum f_k[\theta]_k(\lambda)$, constrained least squares (Formula 11.3.1) | helix $\pm5\,\%$, β $\pm10\,\%$ |

- ORD and CD are the dispersive and absorptive sides of optical activity (Definition 11.3.1). CD arises from inherently chiral chromophores, one-electron perturbation or coupled oscillators; the α helix owes its $208/190\,\mathrm{nm}$ exciton bands and its $222\,\mathrm{nm}$ band to the regular arrangement of peptide groups. Near-UV CD fingerprints tertiary structure, the CD of nucleic acids distinguishes A, B, Z and quadruplex forms.

Vibrational spectroscopy (11.4):

- Infrared activity requires $\partial\boldsymbol{p}/\partial Q \ne \boldsymbol{0}$, not a permanent dipole (Theorem 11.4.1); Raman activity requires $\partial\alpha/\partial Q \ne 0$, and $I_{\mathrm{aS}}/I_{\mathrm{S}}$ is a Boltzmann factor times $\nu^4$ (Theorem 11.4.2); resonance Raman selects chromophore modes.
- The amide I band (Definition 11.4.1) reports secondary structure through hydrogen bonding and transition-dipole coupling (helix $\approx 1652$, β $1630$ and $1690$, aggregates $1615$–$1625\,\mathrm{cm^{-1}}$). Second derivatives narrow Lorentzian bands to a third (Proposition 11.4.1); band fitting is not unique.
- ATR samples a depth $d_{\mathrm{p}} = \lambda_0/(2\pi\sqrt{n_1^2\sin^2\theta - n_2^2})$; infrared dichroism gives orientations through $R = (1 + 2S)/(1 - S)$.

Fluorescence (11.5):

- Lippert–Mataga: the Stokes shift grows with $\Delta f(p_{\mathrm{E}} - p_{\mathrm{G}})^2/a^3$ (Formula 11.5.1); tryptophan emits from $308$ (buried) to $350\,\mathrm{nm}$ (exposed).
- Quenching: $F_0/F = \tau_0/\tau = 1 + k_{\mathrm{q}}\tau_0[\ce{Q}]$ for dynamic, $\tau$ unchanged for static, product for both (Theorem 11.5.1); Lehrer plot for accessible fractions (Formula 11.5.2); diffusion limit $k_{\mathrm{q}} \approx 10^{10}\,\mathrm{M^{-1}\,s^{-1}}$.
- Anisotropy $r = (I_\parallel - I_\perp)/(I_\parallel + 2I_\perp)$ (Definition 11.5.1); $r_0 = 0.4P_2(\cos\beta)$ (Theorem 11.5.2); $r(t) = r_0\mathrm{e}^{-t/\tau_{\mathrm{rot}}}$ with $\tau_{\mathrm{rot}} = \eta V/k_{\mathrm{B}}T \approx 0.42\,\mathrm{ns\,kDa^{-1}}$ (Definition 11.5.2); Perrin $r = r_0/(1 + \tau/\tau_{\mathrm{rot}})$ (Theorem 11.5.3).
- FRET: $k_{\mathrm{T}} = \tau_{\mathrm{D}}^{-1}(R_0/R)^6$, $R_0^6 \propto \kappa^2\Phi_{\mathrm{D}}n^{-4}J$ (Theorem 11.5.4), $E = 1/[1 + (R/R_0)^6]$ (Formula 11.5.3); $R_0 = 2$–$8\,\mathrm{nm}$; $\kappa^2 = 2/3$ for fast isotropic rotation.

## Questions

1. A fluorescent dye has $\varepsilon = 8\times10^4\,\mathrm{L\,mol^{-1}\,cm^{-1}}$ at $488\,\mathrm{nm}$. What fraction of the photons of a laser beam does a single molecule absorb if the beam is focused to a spot of $0.5\,\mu\mathrm{m}$ diameter, and how many photons per second does it absorb at $100\,\mu\mathrm{W}$?

   **Answer** $\sigma = 3.82\times10^{-21}\times8\times10^4 = 3.1\times10^{-16}\,\mathrm{cm^2}$. The spot area is $\pi(0.25\times10^{-4}\,\mathrm{cm})^2 = 2.0\times10^{-9}\,\mathrm{cm^2}$, so the molecule absorbs a fraction $1.6\times10^{-7}$ of the photons. At $100\,\mu\mathrm{W}$ and $488\,\mathrm{nm}$ ($4.07\times10^{-19}\,\mathrm{J}$ per photon) the beam carries $2.5\times10^{14}$ photons per second, of which the molecule absorbs about $4\times10^7\,\mathrm{s^{-1}}$, close to the saturation rate $1/\tau$ of a nanosecond fluorophore; this is why single molecules can be detected in a confocal spot, and why higher powers give no more signal ([7.6.12](/7.6.12)).
2. Explain why the statement "a vibration is infrared active if the molecule has a permanent dipole moment" is wrong, using $\ce{CO2}$ and $\ce{N2}$, and say which of the four normal modes of $\ce{CO2}$ appear in the infrared and in the Raman spectrum.

   **Answer** The infrared transition dipole is $(\partial\boldsymbol{p}/\partial Q)_0\langle1\vert Q\vert0\rangle$; the permanent dipole $\boldsymbol{p}_0$ drops out because $\langle1\vert0\rangle = 0$ (Theorem 11.4.1). $\ce{CO2}$ has no permanent dipole, but its antisymmetric stretch ($2349\,\mathrm{cm^{-1}}$) and its doubly degenerate bend ($667\,\mathrm{cm^{-1}}$) create one and are infrared active. $\ce{N2}$ has a single, symmetric stretch that cannot create a dipole: it is infrared inactive. The symmetric stretch of $\ce{CO2}$ (about $1340\,\mathrm{cm^{-1}}$, split by Fermi resonance into $1285$ and $1388\,\mathrm{cm^{-1}}$) changes the polarizability but not the dipole and appears only in the Raman spectrum, in agreement with the rule of mutual exclusion for a centrosymmetric molecule; the stretch of $\ce{N2}$ is Raman active.
3. A protein has $3$ Trp, $9$ Tyr and $2$ disulfides and a molar mass of $32\,\mathrm{kDa}$. Compute $\varepsilon_{280}$ and $A_{280}^{0.1\,\%}$. A solution gives $A_{280} = 0.62$ and $A_{260} = 0.48$ in a $1\,\mathrm{cm}$ cell; what is the concentration, and is the preparation free of nucleic acid?

   **Answer** $\varepsilon_{280} = 3\times5500 + 9\times1490 + 2\times125 = 30\,160\,\mathrm{L\,mol^{-1}\,cm^{-1}}$ and $A_{280}^{0.1\,\%} = 30\,160/32\,000 = 0.94$. The concentration is $0.62/30\,160 = 20.6\,\mu\mathrm{M}$, or $0.66\,\mathrm{mg\,mL^{-1}}$. A pure protein has $A_{260}/A_{280} \approx 0.55$–$0.6$; the measured $0.77$ indicates contamination with nucleic acid of a few percent by mass, which also inflates $A_{280}$. A further purification step (or correction with the two-wavelength formulas of Warburg and Christian) is needed before the concentration can be trusted.
4. A 16-base-pair DNA duplex is melted at total strand concentrations of $2$ and $20\,\mu\mathrm{M}$ and gives $T_{\mathrm{m}} = 58.0$ and $62.3\,^\circ\mathrm{C}$. Estimate $\Delta H^\circ$ and $\Delta S^\circ$ of duplex formation.

   **Answer** From Formula 11.2.2(b), $1/T_{\mathrm{m}} = (R/\Delta H^\circ)\ln(C_{\mathrm{T}}/4) + \Delta S^\circ/\Delta H^\circ$. The two points give $1/331.15 - 1/335.45 = 3.87\times10^{-5}\,\mathrm{K^{-1}}$ for $\Delta\ln C_{\mathrm{T}} = \ln10 = 2.303$, so $R/\Delta H^\circ = -3.87\times10^{-5}/2.303 = -1.68\times10^{-5}$ and $\Delta H^\circ = -495\,\mathrm{kJ\,mol^{-1}}$ (about $-31\,\mathrm{kJ\,mol^{-1}}$ per base pair, reasonable). Then $\Delta S^\circ = \Delta H^\circ/T_{\mathrm{m}} - R\ln(C_{\mathrm{T}}/4) = -495\,000/331.15 - 8.314\ln(5\times10^{-7}) = -1495 + 120.6 = -1374\,\mathrm{J\,mol^{-1}\,K^{-1}}$. Two concentrations are the minimum; in practice five or more are used, and the van 't Hoff values are compared with calorimetry.
5. Two identical chromophores with transition dipoles of $6\,\mathrm{D}$ are stacked face to face at $0.34\,\mathrm{nm}$ with parallel dipoles (as bases in DNA, roughly). Estimate the exciton splitting with the point-dipole formula, comment on its validity, and explain why the duplex is hypochromic in its $260\,\mathrm{nm}$ band.

   **Answer** For side-by-side parallel dipoles $\kappa = 1$ and $V = p^2/(4\pi\varepsilon_0n^2R^3)$: $p^2 = (2.0\times10^{-29})^2 = 4.0\times10^{-58}\,\mathrm{C^2\,m^2}$, $R^3 = 3.93\times10^{-29}\,\mathrm{m^3}$, so $V = 4.0\times10^{-58}/(1.113\times10^{-10}\times1.77\times3.93\times10^{-29}) = 5.2\times10^{-20}\,\mathrm{J} \approx 2600\,\mathrm{cm^{-1}}$. This overestimates the real coupling considerably, because at $0.34\,\mathrm{nm}$ the chromophores (about $0.5\,\mathrm{nm}$ across) are not points and the transition charge densities partly cancel; in real DNA bases are also twisted by $36^\circ$ and the dipoles are not parallel. The qualitative result holds: the in-phase (allowed) combination of side-by-side dipoles is shifted to higher energy (H-type, Theorem 11.2.1), so intensity moves from the $260\,\mathrm{nm}$ band to shorter wavelengths, and the measured band is weaker than the sum of the monomers. Melting removes the stacking and the coupling, restoring the intensity.
6. The ellipticity of a $0.15\,\mathrm{mg\,mL^{-1}}$ solution of a protein (mean residue mass $112\,\mathrm{g\,mol^{-1}}$) in a $1\,\mathrm{mm}$ cell is $-42\,\mathrm{mdeg}$ at $222\,\mathrm{nm}$. Compute the mean residue ellipticity and $\Delta\varepsilon$ per residue, and estimate the helix content. What additional measurements would make the estimate reliable?

   **Answer** $[\theta]_{\mathrm{MRW}} = \theta M_0/(10lc) = -42\times10^{-3}\times112/(10\times0.1\times0.15) = -31\,360\,\mathrm{deg\,cm^2\,dmol^{-1}}$, and $\Delta\varepsilon = [\theta]/3298 = -9.5\,\mathrm{L\,mol^{-1}\,cm^{-1}}$ per residue. Taking about $-35\,000$ to $-37\,000$ for a long helix and $\approx 0$ for coil at $222\,\mathrm{nm}$, the helix content is about $85$–$90\,\%$, an almost entirely helical protein. Reliability requires an accurate concentration (absorbance with Formula 11.2.1 or amino acid analysis, since a $10\,\%$ error gives $10\,\%$ in the helix content), a full spectrum to at least $190\,\mathrm{nm}$ analyzed with a reference set (Formula 11.3.1), and checks that the absorbance stays below $1$ and the protein is not aggregated (light scattering distorts CD). Near-UV CD and a thermal unfolding curve confirm a stable tertiary structure.
7. In $\ce{H2O}$ the infrared spectrum of a protein shows a broad amide I maximum at $1654\,\mathrm{cm^{-1}}$. On transfer into $\ce{D2O}$, part of the band moves to $1643\,\mathrm{cm^{-1}}$ within seconds, the rest stays, and the amide II band at $1548\,\mathrm{cm^{-1}}$ decays over hours. Interpret these observations.

   **Answer** In $\ce{H2O}$ the bands of α helix (near $1652$) and disordered segments (near $1656$) overlap. Deuteration of the backbone amide lowers the frequency of the disordered component to about $1643\,\mathrm{cm^{-1}}$, while helix bands barely move, so the fast shift identifies solvent-exposed, disordered segments whose amide protons exchange within seconds. The decay of amide II ($\ce{N-H}$ bending; $\ce{N-D}$ appears as amide II′ near $1450\,\mathrm{cm^{-1}}$) over hours shows that most amide protons are protected by stable hydrogen bonds in the folded structure; the time course measures global hydrogen exchange, whose residue-specific analysis needs NMR or mass spectrometry ([7.6.13](/7.6.13)).
8. The tryptophan fluorescence of a protein ($\tau_0 = 4.5\,\mathrm{ns}$) is quenched by acrylamide with a linear Stern–Volmer plot of slope $3.0\,\mathrm{M^{-1}}$, and the lifetime falls in proportion. By iodide, the plot is linear with slope $0.2\,\mathrm{M^{-1}}$. What can you conclude about the tryptophan, and what experiment would test whether the quenching by acrylamide is dynamic?

   **Answer** $k_{\mathrm{q}} = K_{\mathrm{SV}}/\tau_0 = 3.0/4.5\times10^{-9} = 6.7\times10^8\,\mathrm{M^{-1}\,s^{-1}}$ for acrylamide, about a tenth of the diffusion-limited value for free tryptophan ($\approx 6\times10^9$); the tryptophan is partly shielded but accessible to a small neutral quencher, perhaps through fluctuations of the protein. For iodide $k_{\mathrm{q}} = 4.4\times10^7\,\mathrm{M^{-1}\,s^{-1}}$, a hundredfold below diffusion: the large, hydrated anion does not reach the residue, which is buried or surrounded by negative charge. That the lifetime falls in proportion to the intensity already indicates dynamic quenching (Theorem 11.5.1); a further test is temperature dependence: $K_{\mathrm{SV}}$ should increase with temperature roughly as $T/\eta$ for dynamic quenching and decrease for static quenching.
9. A fluorescent label ($\tau = 4\,\mathrm{ns}$, $r_0 = 0.36$) on a protein shows a steady-state anisotropy of $0.20$ at $20\,^\circ\mathrm{C}$ in buffer. Assuming a rigid spherical protein, compute $\tau_{\mathrm{rot}}$ and the apparent molar mass. Time-resolved measurements instead give $r(t) = 0.36[0.4\,\mathrm{e}^{-t/0.6\,\mathrm{ns}} + 0.6]\mathrm{e}^{-t/18\,\mathrm{ns}}$. Reinterpret.

   **Answer** From the Perrin equation, $\tau_{\mathrm{rot}} = \tau/(r_0/r - 1) = 4/(1.8 - 1) = 5.0\,\mathrm{ns}$, which at $0.42\,\mathrm{ns\,kDa^{-1}}$ corresponds to an apparent molar mass of only $12\,\mathrm{kDa}$. The time-resolved data show that the label wobbles rapidly ($0.6\,\mathrm{ns}$) with $S^2 = 0.6$, and that the protein tumbles with $18\,\mathrm{ns}$, corresponding to about $43\,\mathrm{kDa}$. The steady-state value is an average over both motions, $r = 0.36\int[0.4\mathrm{e}^{-t/0.6} + 0.6]\mathrm{e}^{-t/18}\mathrm{e}^{-t/4}\,\mathrm{d}t/4 = 0.36[0.4\times0.127 + 0.6\times0.818] = 0.195$, consistent with the measurement. A flexible linker makes the Perrin analysis underestimate the size; time resolution separates local and global motion.
10. Design a FRET experiment to test whether a two-domain enzyme closes on binding its substrate. Which labeling positions, dye pair and controls would you choose, and how large a change in $E$ do you expect if the distance between the labeling sites decreases from $6.0$ to $4.5\,\mathrm{nm}$?

    **Answer** Introduce two cysteines, one per domain, at surface positions whose distance in a structural model changes most on closure, in a cysteine-free background (or use unnatural amino acids), and label with a donor–acceptor pair whose $R_0$ is near the mean distance, for example Alexa 488–Alexa 594 ($R_0 \approx 6\,\mathrm{nm}$) or Cy3–Cy5 ($R_0 \approx 5.5\,\mathrm{nm}$). With $R_0 = 5.5\,\mathrm{nm}$, $E = 1/[1 + (6.0/5.5)^6] = 0.37$ open and $E = 1/[1 + (4.5/5.5)^6] = 0.77$ closed, a large change. Controls: donor-only and acceptor-only samples to measure leakage and direct excitation; activity assays showing that labeling does not impair function; anisotropies of both dyes to justify $\kappa^2 \approx 2/3$; donor lifetime measurements as an independent measure of $E$; and a nonbinding substrate analog or an inactive mutant. Single-molecule FRET would then tell whether the enzyme switches between discrete open and closed states or shifts a continuous distribution ([7.6.12](/7.6.12)).
