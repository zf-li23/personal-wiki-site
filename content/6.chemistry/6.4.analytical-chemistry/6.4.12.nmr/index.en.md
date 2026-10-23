---
title: Nuclear Magnetic Resonance Spectroscopy
description: Nuclear spin and nuclear magnetic moment, energy levels in a magnetic field and the resonance condition, gyromagnetic ratios and resonance frequencies of common nuclei, the Boltzmann distribution and sensitivity, macroscopic magnetization and longitudinal and transverse relaxation; nuclear shielding and chemical shift, TMS and DSS, effects of electronegativity, ring currents, hybridization and hydrogen bonding, table of ¹H chemical shifts; spin–spin coupling and coupling constants, the n+1 rule, geminal and vicinal coupling and the Karplus relation, chemical and magnetic equivalence, second-order spectra, integration and decoupling; superconducting magnets, pulsed Fourier transform and the free induction decay, probes and field locking; ¹³C spectra, the nuclear Overhauser effect and DEPT, COSY, TOCSY, HSQC, HMBC, NOESY, protein structure determination in solution; magic-angle spinning and cross polarization in solid-state NMR, magnetic resonance imaging and functional MRI.
source_hash: 1adb56ced036
---

Nuclear magnetic resonance (NMR) exploits transitions between the energy levels of magnetic nuclei in a strong magnetic field. The resonance frequencies lie in the radiofrequency region and the energies are extremely small, so the sensitivity of NMR is far lower than that of optical spectroscopic methods. On the other hand, NMR is exceptionally sensitive to the chemical environment of a nucleus: nuclei of the same kind resonate at slightly different frequencies because of differences in the shielding by the surrounding electrons (chemical shifts), and neighboring nuclei interact through the electrons in the chemical bonds and split the lines (spin–spin coupling). The chemical shift tells us what kind of group an atom is in, the coupling tells us which atoms it is bonded to and what their geometric relationship is, and the peak area tells us the number of atoms. NMR is therefore the most powerful method for determining the structures of organic molecules and the principal means of determining the three-dimensional structures of proteins in solution and of studying molecular dynamics, and it has given rise to magnetic resonance imaging in medicine. The physical basis of NMR, namely the nuclear **magnetic moment**, the **gyromagnetic ratio** and **Larmor precession**, was treated in electromagnetism ([5.3.8](/5.3.8#sec-8.2.3)); the populations of the energy levels follow the **Boltzmann distribution** ([5.2.1](/5.2.1)); and the transformation from the time signal to the spectrum is a **Fourier transform** ([2.5.6](/2.5.6#def-6.2.1)). This chapter treats in turn the principles and relaxation of NMR (12.1), chemical shifts (12.2), spin–spin coupling (12.3), pulsed Fourier-transform spectrometers (12.4), carbon spectra and two-dimensional spectra (12.5), and finally solid-state NMR and magnetic resonance imaging (12.6). Many worked examples of structure elucidation by NMR are given in [organic chemistry](/6.5).

Notation in this chapter: $I$ is the nuclear spin quantum number (not the ionic strength), $m_I$ the nuclear spin magnetic quantum number, $\gamma$ the gyromagnetic ratio (not an activity coefficient), $\boldsymbol{m}$ the nuclear magnetic moment (consistent with [5.3.8](/5.3.8); the NMR literature often writes $\boldsymbol{\mu}$), $\boldsymbol{M}$ the macroscopic magnetization, $B_0$ the magnetic flux density of the static field, $\sigma$ the nuclear shielding constant (not the standard deviation), $\delta$ the chemical shift, $J$ the coupling constant (not a rotational quantum number), and $T_1$ and $T_2$ the relaxation times.

## 12.1. Principles of Nuclear Magnetic Resonance

### 12.1.1. A Brief History

In 1924 Pauli proposed that atomic nuclei have spin and a magnetic moment, to explain the hyperfine structure of atomic spectra. In 1938 Rabi first observed nuclear magnetic resonance with the molecular-beam method (Nobel Prize in Physics, 1944). In 1945–1946 Purcell (Harvard University, solid paraffin) and Bloch (Stanford University, water) independently observed NMR signals in condensed matter, and shared the 1952 Nobel Prize in Physics. Around 1950 it was found that the resonance frequency of a given nucleus varies with its chemical environment (the chemical shift), and in 1951 Arnold and coworkers obtained the three groups of peaks of ethanol, which brought NMR into chemistry. In 1953 Varian introduced the first commercial NMR spectrometer (continuous wave, $30\,\mathrm{MHz}$). In 1966 Ernst and Anderson invented pulsed Fourier-transform NMR, and in 1971 Jeener put forward the idea of two-dimensional NMR; Ernst subsequently established its theory and experimental methods and received the 1991 Nobel Prize in Chemistry. Wüthrich developed the method of determining the three-dimensional structures of biological macromolecules in solution by NMR and received the 2002 Nobel Prize in Chemistry. Lauterbur and Mansfield received the 2003 Nobel Prize in Physiology or Medicine for magnetic resonance imaging.

### 12.1.2. Nuclear Spin and Nuclear Magnetic Moment

**Definition 12.1.1 (Nuclear Spin Quantum Number)** The spin angular momentum $\boldsymbol{P}$ of an atomic nucleus is quantized, with magnitude $\lvert\boldsymbol{P}\rvert = \hbar\sqrt{I(I + 1)}$, where $I = 0, \frac12, 1, \frac32, \dots$ is called the **nuclear spin quantum number**; its component along any direction (taken as the $z$ axis) can only be $P_z = m_I\hbar$, with $m_I = I, I - 1, \dots, -I$, a total of $2I + 1$ values.

$I$ is determined by the numbers of protons and neutrons in the nucleus, and the following empirical rules hold:

| Protons and neutrons | Mass number | $I$ | Examples |
|---|---|---|---|
| both even | even | $0$ | $^{12}\mathrm{C}$, $^{16}\mathrm{O}$, $^{32}\mathrm{S}$ |
| one odd, one even | odd | half-integer | $^{1}\mathrm{H}$, $^{13}\mathrm{C}$, $^{15}\mathrm{N}$, $^{19}\mathrm{F}$, $^{31}\mathrm{P}$ ($\frac12$); $^{11}\mathrm{B}$, $^{23}\mathrm{Na}$ ($\frac32$); $^{17}\mathrm{O}$ ($\frac52$) |
| both odd | even | integer | $^{2}\mathrm{H}$, $^{14}\mathrm{N}$ ($1$); $^{10}\mathrm{B}$ ($3$) |

Nuclei with $I = 0$ have no magnetic moment and give no NMR signal, so $^{12}\mathrm{C}$ and $^{16}\mathrm{O}$, the most abundant nuclei in the skeletons of organic molecules, are "invisible". Nuclei with $I \ne 0$ have a magnetic moment proportional to the spin angular momentum,

$$
\boldsymbol{m} = \gamma\boldsymbol{P},\qquad m_z = \gamma\hbar m_I,
\tag{12.1}
$$
and the proportionality factor $\gamma$ is the gyromagnetic ratio of the nucleus, a constant characteristic of each nuclide. The charge distribution of a nucleus with $I = \frac12$ is spherically symmetric; that of a nucleus with $I \ge 1$ is not, and such a nucleus has an electric quadrupole moment that interacts with the electric field gradient at the nucleus, so that relaxation is fast and the lines are broad (quadrupolar nuclei). The nuclei most used in chemistry are therefore those with $I = \frac12$.

### 12.1.3. Energy Levels in a Magnetic Field and the Resonance Condition

When a nucleus is placed in a static magnetic field $B_0$ along the $z$ direction, the potential energy of the magnetic moment is

$$
E = -m_zB_0 = -\gamma\hbar m_IB_0,
\tag{12.2}
$$
and the originally degenerate $2I + 1$ states split into equally spaced levels (the nuclear **Zeeman effect**). A nucleus with $I = \frac12$ has two levels: $m_I = +\frac12$ (for $\gamma > 0$ the moment is parallel to the field and the energy is lower; denoted $\alpha$) and $m_I = -\frac12$ (denoted $\beta$). The selection rule for magnetic dipole transitions is $\Delta m_I = \pm1$, and the spacing of adjacent levels is $\Delta E = \gamma\hbar B_0$.

**Definition 12.1.2 (Nuclear Magnetic Resonance)** The phenomenon in which magnetic nuclei in a static field $B_0$ absorb radiofrequency radiation of frequency

$$
\nu_0 = \frac{\gamma B_0}{2\pi}
\tag{12.3}
$$
and undergo transitions between nuclear spin levels is called **nuclear magnetic resonance**; the method of recording the absorption signal as a function of frequency is called NMR spectroscopy.

Eq. (12.3) is the fundamental equation of NMR. Classically, a magnetic moment in a magnetic field experiences a torque and precesses about the field with angular frequency $\omega_0 = \gamma B_0$ ([5.3.8](/5.3.8#sec-8.2.5)); the resonance frequency is the precession (Larmor) frequency, and the orientation of the moment can be changed continuously only by a radiofrequency field rotating at this frequency. By Eq. (12.3), in a given field different nuclei (different $\gamma$) resonate at different frequencies, so only one kind of nucleus is observed in each experiment; for a given nucleus the resonance frequency is proportional to the field, so spectrometers are conventionally labeled by the resonance frequency of $^1\mathrm{H}$: $2.35\,\mathrm{T}$ is a "$100\,\mathrm{MHz}$" and $11.74\,\mathrm{T}$ a "$500\,\mathrm{MHz}$" instrument.

Properties of common nuclei ($\gamma$ and the natural abundances are IUPAC-recommended values; the resonance frequency is the value for $^1\mathrm{H}$ at $500.00\,\mathrm{MHz}$, that is, $B_0 = 11.74\,\mathrm{T}$; the relative sensitivity is the ratio to $^1\mathrm{H}$ at natural abundance, see 12.1.4):

| Nucleus | $I$ | Natural abundance / % | $\gamma$ / $(10^7\,\mathrm{rad\,s^{-1}\,T^{-1}})$ | Resonance frequency / $\mathrm{MHz}$ | Relative sensitivity |
|---|---|---|---|---|---|
| $^1\mathrm{H}$ | $\frac12$ | $99.99$ | $26.752$ | $500.00$ | $1$ |
| $^2\mathrm{H}$ | $1$ | $0.0115$ | $4.107$ | $76.75$ | $1.1\times10^{-6}$ |
| $^{13}\mathrm{C}$ | $\frac12$ | $1.07$ | $6.728$ | $125.73$ | $1.7\times10^{-4}$ |
| $^{14}\mathrm{N}$ | $1$ | $99.64$ | $1.934$ | $36.13$ | $1.0\times10^{-3}$ |
| $^{15}\mathrm{N}$ | $\frac12$ | $0.364$ | $-2.713$ | $50.68$ | $3.8\times10^{-6}$ |
| $^{19}\mathrm{F}$ | $\frac12$ | $100$ | $25.181$ | $470.47$ | $0.83$ |
| $^{31}\mathrm{P}$ | $\frac12$ | $100$ | $10.839$ | $202.40$ | $0.066$ |

For $^1\mathrm{H}$, $\gamma/(2\pi) = 42.577\,\mathrm{MHz\,T^{-1}}$. The resonance frequencies lie in the radiofrequency region (wavelengths of the order of meters), and the photon energy is only about $3\times10^{-25}\,\mathrm{J}$ ($2\,\mu\mathrm{eV}$), five orders of magnitude smaller than that of an infrared photon.

### 12.1.4. The Boltzmann Distribution and Sensitivity

At thermal equilibrium the numbers of nuclei in the two levels obey the Boltzmann distribution:

$$
\frac{N_\beta}{N_\alpha} = \exp\left(-\frac{\Delta E}{k_{\mathrm{B}}T}\right) = \exp\left(-\frac{\gamma\hbar B_0}{k_{\mathrm{B}}T}\right) \approx 1 - \frac{\gamma\hbar B_0}{k_{\mathrm{B}}T}.
\tag{12.4}
$$
The probabilities of absorption and stimulated emission are equal, so the net absorption comes only from the population difference of the two levels, whose fraction of the total number of nuclei is about $\gamma\hbar B_0/(2k_{\mathrm{B}}T)$.

**Example 12.1.1** Find the population ratio for $^1\mathrm{H}$ in a $500\,\mathrm{MHz}$ spectrometer at $298\,\mathrm{K}$.

**Solution** $\Delta E/(k_{\mathrm{B}}T) = h\nu_0/(k_{\mathrm{B}}T) = \frac{6.626\times10^{-34}\times5.00\times10^8}{1.381\times10^{-23}\times298} = 8.05\times10^{-5}$, and $N_\beta/N_\alpha = 0.999920$. That is, for every $10^6$ nuclei in the upper level there are $1000080$ in the lower level, an excess of only $80$. In spectrometers of $100$, $200$ and $300\,\mathrm{MHz}$ this excess is about $16$, $32$ and $48$, respectively.

Thus NMR "uses" only about one nucleus in a hundred thousand, which is the fundamental reason for its low sensitivity (by comparison, in visible spectroscopy nearly all molecules are in the ground state). The signal intensity is roughly proportional to the population difference ($\propto \gamma B_0$), the magnetic moment of each nucleus ($\propto \gamma$), and the increase of the electromotive force induced in the coil with the precession frequency ($\propto \gamma B_0$); the noise increases slowly with frequency, and altogether the signal-to-noise ratio is roughly proportional to $\gamma^{5/2}B_0^{3/2}$. The relative sensitivity (receptivity) of different nuclei is calculated as $\gamma^3I(I + 1)$ times the natural abundance; $^{13}\mathrm{C}$ has only about $1/5900$ of the sensitivity of $^1\mathrm{H}$ ($\gamma$ is about $1/4$ that of $^1\mathrm{H}$ and the abundance is $1.07\%$), and $^{15}\mathrm{N}$ only $4\times10^{-6}$. Ways to increase the sensitivity include raising the field, cooling the probe (12.4.4), signal averaging (12.4.3), isotopic enrichment (12.5.4), transferring the polarization of high-$\gamma$ nuclei to low-$\gamma$ nuclei (12.5.1, 12.6.1), and hyperpolarization techniques (such as dynamic nuclear polarization), which produce population differences far above the thermal-equilibrium value.

The Earth's magnetic field (about $50\,\mu\mathrm{T}$) is about $10^5$ times weaker than an NMR magnet, but NMR can also be observed in it (resonance frequency about $2\,\mathrm{kHz}$); the signal is very weak, but the Earth's field is extremely homogeneous and the lines are very narrow. Such methods are used for portable measurements and teaching.

### 12.1.5. Macroscopic Magnetization and Relaxation

The vector sum of the large number of nuclear magnetic moments in a sample is the macroscopic **magnetization** $\boldsymbol{M}$. At thermal equilibrium the components of the individual moments in the plane perpendicular to $B_0$ have random orientations and cancel; along $B_0$ there is a net component because of the population difference, so that $\boldsymbol{M}$ lies along the $z$ axis with magnitude $M_0$. A radiofrequency pulse can tilt $\boldsymbol{M}$ away from the $z$ axis (12.4.3); under continuous radiofrequency irradiation the transitions tend to equalize the populations of the two levels and the net absorption vanishes, which is called saturation. For the system to return to equilibrium there must be processes that restore the populations and that make the transverse component disappear; these are relaxation.

**Definition 12.1.3** The process by which the longitudinal component $M_z$ of $\boldsymbol{M}$ returns to its equilibrium value $M_0$ is called **longitudinal relaxation** (spin–lattice relaxation), with time constant $T_1$:

$$
\frac{\mathrm{d}M_z}{\mathrm{d}t} = -\frac{M_z - M_0}{T_1}.
$$
In longitudinal relaxation the nuclear spins give energy to the surrounding molecules (collectively the "lattice"), which is converted into thermal motion, and the populations of the spin system return to the Boltzmann distribution. The process by which the transverse component $M_{xy}$ decays to zero is called **transverse relaxation** (spin–spin relaxation), with time constant $T_2$:

$$
\frac{\mathrm{d}M_{xy}}{\mathrm{d}t} = -\frac{M_{xy}}{T_2}.
$$
It originates from small differences and fluctuations in the local fields experienced by the individual nuclei, which make the precessions of the nuclear moments gradually lose phase coherence; no exchange of energy with the lattice is needed.

These two equations together with the precession of the magnetic moment constitute the Bloch equations. Always $T_2 \le 2T_1$, and in practice $T_2 \le T_1$. Relaxation is caused by the fluctuation of local magnetic fields produced by molecular motion, mainly the magnetic dipole–dipole interaction with neighboring nuclei, so the relaxation times reflect the size of the molecule, the speed of its motion, its interaction with the solvent and the anisotropy of its motion.

Transverse relaxation determines the line width. $T_2$ is the time for which the magnetization remains coherent in the transverse plane, and by the Fourier relation between time and frequency the line has a Lorentzian shape with full width at half maximum

$$
\Delta\nu_{1/2} = \frac{1}{\pi T_2}.
\tag{12.5}
$$
Inhomogeneity of the magnetic field makes the resonance frequency differ slightly from place to place in the sample, and the actual line width is determined by the apparent transverse relaxation time $T_2^*$, which includes this effect. Small molecules in solution tumble rapidly, $T_1 \approx T_2$ is about $0.5$–$10\,\mathrm{s}$, and the line width is less than $1\,\mathrm{Hz}$, a prerequisite for high-resolution NMR; large molecules (proteins) tumble slowly, $T_2$ is short and the lines are broad, which limits the size of molecules that can be studied by solution NMR; in solids $T_2$ is only of the order of microseconds and the lines are $\mathrm{kHz}$ wide (12.6.1). $T_1$ determines how long one must wait between measurements: quantitative determination requires a wait of about $5T_1$.

Nuclear magnetic resonance in oil-well logging exploits relaxation: the $T_1$ and $T_2$ of water and oil in rock pores, and of bound water and mobile fluid, differ, and the measured distribution of relaxation times allows them to be distinguished and the pore sizes to be estimated.

## 12.2. Chemical Shift

### 12.2.1. Nuclear Shielding and Chemical Shift

If all protons resonated at exactly the same frequency according to Eq. (12.3), the hydrogen spectra of all compounds would consist of a single line and NMR could not be used for structure analysis. In fact the electrons around a nucleus undergo circulation in the external magnetic field (the same principle as diamagnetism, [5.3.8](/5.3.8#sec-8.2.5)), and the induced field produced by this circulation opposes the external field, so that the field actually experienced by the nucleus is slightly less than $B_0$.

**Definition 12.2.1 (Nuclear Shielding Constant)** The field experienced by a nucleus, as reduced by the surrounding electrons, is

$$
B = (1 - \sigma)B_0,
$$
and the dimensionless constant $\sigma$ is called the **nuclear shielding constant** of the nucleus; the resonance frequency is therefore $\nu = \gamma(1 - \sigma)B_0/(2\pi)$.

$\sigma$ is very small (about $10^{-5}$ for $^1\mathrm{H}$), but its variation with chemical environment is large enough to be measured by a high-resolution spectrometer. The greater the shielding, the lower the resonance frequency (or, in a field sweep, the higher the field required for resonance), which is called "upfield"; less shielding is called "downfield", or "deshielding". The frequencies of different spectrometers differ, and so do the frequency differences, so the position is expressed as a value relative to a reference compound:

**Definition 12.2.2 (Chemical Shift)** The relative difference between the resonance frequency $\nu$ of a nucleus and the resonance frequency $\nu_{\mathrm{ref}}$ of the same kind of nucleus in a reference compound,

$$
\delta = \frac{\nu - \nu_{\mathrm{ref}}}{\nu_{\mathrm{ref}}}\times10^6
\tag{12.6}
$$
is called the **chemical shift**, with unit ppm ($10^{-6}$).

Because both $\nu$ and $\nu_{\mathrm{ref}}$ are proportional to $B_0$, $\delta$ is independent of the field, and values of $\delta$ measured on different spectrometers can be compared directly; by definition $\delta \approx (\sigma_{\mathrm{ref}} - \sigma)\times10^6$. Expressed as a frequency, $1\,\mathrm{ppm}$ is $500\,\mathrm{Hz}$ on a $500\,\mathrm{MHz}$ spectrometer and only $100\,\mathrm{Hz}$ on a $100\,\mathrm{MHz}$ instrument: the higher the field, the farther apart in frequency are peaks with different chemical shifts, which is one of the main reasons for the pursuit of high fields. The abscissa of a spectrum is $\delta$, decreasing from left to right (the left side is downfield, with deshielded nuclei).

### 12.2.2. Reference Compounds

The reference compound for $^1\mathrm{H}$ and $^{13}\mathrm{C}$ spectra is tetramethylsilane (TMS) $\ce{Si(CH3)4}$, whose $\delta$ is defined to be $0$. The advantages of TMS are these: its 12 hydrogens are completely equivalent and give a single sharp peak; silicon is less electronegative than carbon, so the electron density on the methyl groups is high and the shielding large, and its peak lies upfield of the peaks of almost all organic compounds, so that nearly all other values of $\delta$ are positive; it is chemically inert and does not react with the sample; and it has a low boiling point ($26.6\,^\circ\mathrm{C}$) and is easily removed after the measurement so that the sample can be recovered. Note that $\delta$ of the reference compound is zero by definition, irrespective of whether its $\sigma$ is zero; TMS is in fact highly shielded.

TMS is insoluble in water. In aqueous solutions (including biological samples) DSS (sodium 4,4-dimethyl-4-silapentane-1-sulfonate) is commonly used as an internal reference; the trimethylsilyl protons give a peak at almost the same position as TMS, and IUPAC recommends it as the reference for NMR of biological macromolecules. Another common one is TSP (sodium 3-trimethylsilylpropionate, with deuterated methylene groups), but its chemical shift varies slightly with pH. The figure below shows the structures of TMS and DSS in that order:

```smiles
C[Si](C)(C)C TMS
C[Si](C)(C)CCCS(=O)(=O)[O-].[Na+] DSS
```

References for other nuclei: liquid ammonia (or nitromethane) for $^{15}\mathrm{N}$, $\ce{CFCl3}$ for $^{19}\mathrm{F}$ and $85\%$ phosphoric acid for $^{31}\mathrm{P}$. In practice the residual peak of the undeuterated solvent in a deuterated solvent (such as $\ce{CHCl3}$ in $\ce{CDCl3}$, $\delta = 7.26$) is often used as a secondary reference.

### 12.2.3. Factors Influencing Chemical Shifts

(1) Electronegativity and the inductive effect. The more electronegative the atom attached to the carbon, the more strongly it attracts electrons, the lower the electron density around the proton, the lower the shielding and the larger $\delta$.

| Compound | $\delta(\ce{CH3})$ | Compound | $\delta(\ce{CH3})$ |
|---|---|---|---|
| $\ce{(CH3)4Si}$ | $0$ (by definition) | $\ce{CH3OH}$ | $3.40$ |
| $\ce{CH3I}$ | $2.16$ | $\ce{CH3F}$ | $4.26$ |
| $\ce{CH3Br}$ | $2.68$ | $\ce{CH3NO2}$ | $4.29$ |
| $\ce{CH3Cl}$ | $3.05$ | $\ce{CH2Cl2}$, $\ce{CHCl3}$ | $5.30$, $7.26$ |

The effects of substituents are roughly additive: as the number of chlorine atoms increases from one to three, $\delta$ increases from $3.05$ to $5.30$ and $7.26$. The effect decreases rapidly with the number of bonds separating the proton from the substituent: in 1-bromopropane, $\ce{CH2Br}$, the middle $\ce{CH2}$ and $\ce{CH3}$ appear at $3.40$, $1.89$ and $1.03$, respectively.

(2) Magnetic anisotropy and ring currents. The induced field produced by the circulation of $\pi$ electrons in the external field has different directions at different points of space, so that nearby nuclei are shielded in some regions and deshielded in others, depending on the position of the nucleus relative to the $\pi$ system.

**Definition 12.2.3 (Ring-Current Effect)** When the plane of an aromatic ring is perpendicular to the external field, the delocalized $\pi$ electrons of the ring form a ring current. The induced field it produces opposes the external field inside the ring and above and below it, and reinforces the external field outside the ring near the ring plane; protons outside the ring are therefore deshielded and shifted downfield, and protons inside or above the ring are shielded and shifted upfield. This effect is called the **ring-current effect**.

The protons of benzene appear at $\delta = 7.3$, about $2$ above those of alkenes (about $5.3$), mainly because of the ring current. [18]Annulene ($18$ $\pi$ electrons, satisfying Hückel's $4n + 2$ rule) has 12 outer hydrogens and 6 inner hydrogens, which at low temperature appear at $\delta \approx 9.3$ and $-3.0$, respectively; in 15,16-dimethyldihydropyrene the two methyl groups positioned above the center of the aromatic ring appear at $\delta = -4.25$. Conversely, the ring current is one of the experimental criteria for deciding whether a ring is aromatic (an antiaromatic ring with $4n$ $\pi$ electrons produces a ring current in the opposite direction).

```smiles
C1=CC=CC=CC=CC=CC=CC=CC=C1
```

Other multiple bonds are also magnetically anisotropic: an aldehyde proton lies in the deshielding region of $\ce{C=O}$ and appears at $\delta = 9$–$10$; the $\pi$ electrons of a triple bond circulate about the bond axis, so a proton along the bond axis lies in the shielding region, and the protons of acetylene appear at $\delta \approx 1.8$, farther upfield than those of ethylene.

In proteins, protons close in space to aromatic side chains (phenylalanine, tyrosine, tryptophan) are affected by the ring current, and their chemical shifts can deviate by $1$–$2\,\mathrm{ppm}$ from the random-coil values, and methyl peaks at $\delta < 0$ may even occur. These dispersed peaks are themselves evidence that the protein has folded into a well-defined three-dimensional structure.

(3) Hybridization. The protons of ethane, ethylene and acetylene appear at $\delta = 0.86$, $5.28$ and $1.80$, respectively. The $\mathrm{sp}^2$ and $\mathrm{sp}$ carbons have more s character and are more electronegative, and from the inductive effect alone $\delta$ of the protons should increase in that order; the anomaly of acetylene comes from the anisotropic shielding by the triple bond mentioned above. Terminal alkyne protons generally appear between $1.7$ and $3.1$.

(4) Hydrogen bonding and exchange. Protons attached to O, N and S have a lower electron density after forming **hydrogen bonds** and shift downfield. The extent of hydrogen bonding varies with concentration, temperature and solvent, so $\delta$ of such protons is not fixed (alcohols $0.5$–$5$, phenols $4$–$8$, carboxylic acids $10$–$13$, amides $5$–$9$), and the peaks are often broad. These protons can also exchange with the solvent: when a drop of $\ce{D2O}$ is added to the sample and shaken, the $\ce{OH}$, $\ce{NH}$ and $\ce{COOH}$ peaks disappear because H is replaced by D, which allows them to be identified. The rates of exchange of backbone amide protons of proteins with the solvent can differ by many orders of magnitude; amide protons that are hydrogen-bonded or buried exchange slowly, so measurement of H/D exchange rates can be used to study the folding and stability of proteins.

### 12.2.4. Chemical Shifts of Common Protons

| Proton type | $\delta$ | Proton type | $\delta$ |
|---|---|---|---|
| $\ce{R-CH3}$ (saturated) | $0.8$–$1.0$ | $\ce{CH3-O}$, $\ce{-CH2-O-}$ | $3.3$–$4.0$ |
| $\ce{R2CH2}$ | $1.2$–$1.4$ | $\ce{-CH2-X}$ (X = Cl, Br) | $3.0$–$3.7$ |
| $\ce{R3CH}$ | $1.4$–$1.7$ | alkyne H | $1.7$–$3.1$ |
| $\ce{CH3-C=C}$ (allylic) | $1.6$–$1.9$ | alkene H | $4.5$–$6.5$ |
| $\ce{CH3-C=O}$ | $2.0$–$2.6$ | aromatic H | $6.5$–$8.5$ (benzene $7.3$) |
| $\ce{CH3-Ar}$ | $2.2$–$2.5$ | aldehyde H | $9$–$10$ |
| $\ce{CH3-N}$ | $2.2$–$3.0$ | $\ce{OH}$ of carboxylic acids, phenols, alcohols | see 12.2.3 |

Within a given type of structure, a methine proton is generally about $0.3\,\mathrm{ppm}$ above a methylene proton, and a methylene proton about $0.3\,\mathrm{ppm}$ above a methyl proton. Substituents on a benzene ring affect the chemical shifts of the various positions according to their electronic effects: electron-donating groups ($\ce{-OH}$, $\ce{-OCH3}$, $\ce{-NH2}$) shift the ortho and para protons upfield, electron-withdrawing groups ($\ce{-NO2}$, $\ce{-COR}$) shift the ortho protons downfield; in alkyl-substituted benzenes the five aromatic hydrogens have similar chemical shifts and often form a single cluster of peaks.

Ethanol was the first example in the history of NMR to show chemical shifts: $\ce{CH3}$ at $1.22$ (triplet), $\ce{CH2}$ at $3.69$ (quartet), and $\ce{OH}$ at a position that varies with concentration (about $2.6$, usually a singlet because of rapid exchange); the areas of the three groups of peaks are in the ratio $3:2:1$.

```smiles
CCO
```

## 12.3. Spin–Spin Coupling

### 12.3.1. Coupling and Coupling Constants

When ethanol is measured on a high-resolution spectrometer, the peaks of both $\ce{CH3}$ and $\ce{CH2}$ split into several lines. This splitting does not come from differences in chemical environment but from the interaction between neighboring magnetic nuclei.

**Definition 12.3.1** The interaction in which the spin of one nucleus influences, through the bonding electrons, the local magnetic field experienced by a neighboring magnetic nucleus and thereby splits its resonance line is called **spin–spin coupling** ($J$ coupling). The distance between adjacent lines after splitting is called the **coupling constant** $J$, with unit $\mathrm{Hz}$.

The mechanism of coupling is as follows: the spin of a nucleus slightly polarizes the spins of nearby bonding electrons, and this polarization is transmitted along the chemical bonds to another nucleus (the Fermi contact interaction); the coupling constant is therefore independent of the magnetic field and decreases rapidly with the number of bonds between the two nuclei. $^nJ$ denotes coupling across $n$ bonds. The direct magnetic dipole interaction of two nuclei through space averages to zero in solution because of the rapid tumbling of the molecules and causes no splitting (but it causes relaxation and the NOE, 12.5.1). To decide whether the distance between two lines in a spectrum is a coupling or a chemical-shift difference, one can measure on spectrometers of two different field strengths: a spacing that is unchanged when expressed in $\mathrm{Hz}$ is a coupling, and one proportional to the field strength is a chemical-shift difference.

### 12.3.2. The n+1 Rule

Take an ethyl group $\ce{-CH2-CH3}$ as an example. The protons of $\ce{CH3}$ are influenced by the two protons of the adjacent $\ce{CH2}$: the spins of these two protons can be $\alpha\alpha$, $\alpha\beta$, $\beta\alpha$ or $\beta\beta$, which increase, leave unchanged (two ways) or decrease the local field experienced by the $\ce{CH3}$ protons, respectively, so the $\ce{CH3}$ peak splits into a triplet with intensity ratio $1:2:1$ and a spacing of $J$ between adjacent lines. Similarly, the protons of $\ce{CH2}$ are influenced by the $2^3 = 8$ combinations of the three protons of $\ce{CH3}$, which fall into four groups of $1:3:3:1$ according to the total $m_I$, and the $\ce{CH2}$ peak splits into a quartet. The coupling constants of the two groups of peaks are the same (about $7\,\mathrm{Hz}$), which is the criterion for deciding which protons are coupled to each other.

![First-order coupling splitting of an ethyl group (J = 7.0 Hz): CH₃ is split by the two protons of CH₂ into a 1:2:1 triplet and CH₂ by the three protons of CH₃ into a 1:3:3:1 quartet; above, the tree diagram of successive splittings](./plots/ethyl-splitting.py)

In general, a group of nuclei coupled to $n$ equivalent nuclei with $I = \frac12$ is split into an $n + 1$ multiplet, and the intensity ratios of the lines are the coefficients of the binomial expansion $(a + b)^n$ (Pascal's triangle): singlet, doublet ($1:1$), triplet ($1:2:1$), quartet ($1:3:3:1$), quintet ($1:4:6:4:1$), sextet, and so on. For coupling to nuclei of spin $I$ the multiplicity is $2nI + 1$; for example, the $^{13}\mathrm{C}$ signal of $\ce{CDCl3}$ is split by one D ($I = 1$) into a $1:1:1$ triplet. If coupling to two inequivalent groups of nuclei ($n$ and $m$ of them) occurs with different coupling constants, the splitting gives $(n + 1)(m + 1)$ lines; if the two coupling constants are approximately equal, the pattern is approximately an $n + m + 1$ multiplet. The $n + 1$ rule holds only in first-order spectra (12.3.5).

### 12.3.3. Types of Coupling and the Karplus Relation

- Geminal coupling $^2J$ (two hydrogens on the same carbon): generally $-10$ to $-15\,\mathrm{Hz}$ for an $\mathrm{sp}^3$ methylene group and $0$–$3\,\mathrm{Hz}$ for a terminal $\ce{=CH2}$. Geminal coupling appears as splitting in the spectrum only when the two hydrogens on the carbon are chemically inequivalent (for example, a methylene group adjacent to a stereocenter, or in a ring); between chemically equivalent geminal hydrogens there is still coupling, but it does not show (12.3.4). The statement that "there is no coupling between hydrogens on the same carbon" is therefore incorrect.
- Vicinal coupling $^3J$ (hydrogens on adjacent carbons): the most important coupling. About $7\,\mathrm{Hz}$ for freely rotating alkyl chains; $6$–$12\,\mathrm{Hz}$ for cis and $12$–$18\,\mathrm{Hz}$ for trans in alkenes, which allows cis and trans isomers to be distinguished; $7$–$9\,\mathrm{Hz}$ for ortho positions of a benzene ring.
- Long-range coupling $^4J$ and beyond: generally less than $3\,\mathrm{Hz}$; it can be observed in benzene rings (meta $1$–$3$, para $0$–$1\,\mathrm{Hz}$), at allylic positions and in W-shaped arrangements in rigid skeletons.
- Heteronuclear coupling: $^1J_{\mathrm{CH}}$ increases with the hybridization of carbon, about $125$, $160$ and $250\,\mathrm{Hz}$ for $\mathrm{sp}^3$, $\mathrm{sp}^2$ and $\mathrm{sp}$, respectively; on each side of every peak in a hydrogen spectrum there is a $^{13}\mathrm{C}$ satellite of intensity about $0.55\%$, which arises from this coupling. Couplings of $^1\mathrm{H}$ to $^{19}\mathrm{F}$ and $^{31}\mathrm{P}$ are also common, and $^2J_{\mathrm{HF}}$ can reach $45$–$50\,\mathrm{Hz}$.

The magnitude of vicinal coupling depends strongly on the dihedral angle between the two $\ce{C-H}$ bonds, which makes it a tool for determining conformations.

**Definition 12.3.2 (Karplus Relation)** The relation between the vicinal coupling constant and the $\ce{H-C-C-H}$ dihedral angle $\phi$,

$$
{}^3J(\phi) = A\cos^2\phi + B\cos\phi + C
\tag{12.7}
$$
is called the **Karplus equation**, where $A$, $B$ and $C$ are empirical parameters depending on the substituents and the kinds of atoms (typical values for $\ce{H-C-C-H}$ are about $A \approx 8$, $B \approx -1$, $C \approx 1\,\mathrm{Hz}$).

$^3J$ is largest at $\phi = 180^\circ$ (about $10\,\mathrm{Hz}$), slightly smaller at $0^\circ$, and smallest near $90^\circ$ ($1$–$2\,\mathrm{Hz}$). In chair cyclohexane the dihedral angle between two axial hydrogens is about $180^\circ$ and $^3J_{\mathrm{aa}} = 8$–$13\,\mathrm{Hz}$; for axial–equatorial and equatorial–equatorial pairs it is about $60^\circ$ and $2$–$5\,\mathrm{Hz}$. In carbohydrate chemistry this is used to distinguish anomers: in $\beta$-D-glucopyranose H1 and H2 are both axial and $^3J_{12} \approx 8\,\mathrm{Hz}$, whereas for the $\alpha$ anomer it is about $3.7\,\mathrm{Hz}$. In proteins the $^3J_{\mathrm{HN,H\alpha}}$ between the backbone amide proton and the $\alpha$ proton is determined by the backbone dihedral angle $\phi$: about $4\,\mathrm{Hz}$ for an $\alpha$-helix ($\phi \approx -60^\circ$) and about $9$–$10\,\mathrm{Hz}$ for a $\beta$-sheet ($\phi \approx -120^\circ$), one of the constraints used to determine secondary structure (12.5.4).

![The Karplus relation. Left: vicinal coupling constant of H–C–C–H versus dihedral angle (A = 7.8, B = −1.0, C = 1.4 Hz), with the ax–ax and ax–eq dihedral angles of the chair conformation of cyclohexane marked; right: ³J(HN,Hα) of the polypeptide backbone versus the backbone dihedral angle φ (parameters of Vuister and Bax), with the typical φ of α-helices and β-sheets shaded](./plots/karplus.py)

### 12.3.4. Chemical Equivalence and Magnetic Equivalence

Whether coupling shows up as line splitting depends on whether the nuclei are equivalent.

**Definition 12.3.3 (Chemical Equivalence)** Nuclei in a molecule that can be interchanged by a symmetry operation or by rapid conformational change have the same chemical shift and are called **chemically equivalent** nuclei.

For example, the three hydrogens of the $\ce{CH3}$ group of ethanol interchange by rapid rotation about the $\ce{C-C}$ bond and are chemically equivalent. In an achiral environment, nuclei interchanged by a mirror plane (enantiotopic nuclei) are also chemically equivalent; but the two hydrogens of a $\ce{CH2}$ group adjacent to a stereocenter cannot be interchanged by any symmetry operation (diastereotopic), are generally chemically inequivalent, have different chemical shifts, and show geminal splitting between each other.

**Definition 12.3.4 (Magnetic Equivalence)** A set of chemically equivalent nuclei whose coupling constants to any other nucleus in the molecule are also the same are called **magnetically equivalent** nuclei.

Coupling between magnetically equivalent nuclei causes no splitting (for example, the coupling among the three hydrogens within a $\ce{CH3}$ group cannot be seen in the spectrum), which is why TMS gives a single peak and the $\ce{CH3}$ of an ethyl group is only a triplet. Chemical equivalence does not imply magnetic equivalence: the two hydrogens of 1,1-difluoroethylene are chemically equivalent, but each hydrogen couples to the two fluorines with different coupling constants (one cis, one trans), so they are not magnetically equivalent and the spectrum is a complicated AA′XX′ system; the aromatic hydrogens of para-disubstituted benzenes are in the same situation (AA′BB′). Spin systems are commonly denoted by letters: nuclei with similar chemical shifts are given adjacent letters (A, B, C) and those with very different shifts letters far apart (X); the number of equivalent nuclei is written as a subscript, so an ethyl group is $\mathrm{A_2X_3}$, and chemically equivalent but magnetically inequivalent nuclei carry primes.

### 12.3.5. First-Order and Second-Order Spectra

The $n + 1$ rule, the binomial intensity ratios, and the identification of the center of a multiplet with the chemical shift are simple regularities that hold only when the chemical shift difference of two coupled groups (in $\mathrm{Hz}$) is much larger than the coupling constant, roughly $\Delta\nu/J > 10$; such spectra are called first-order spectra. When $\Delta\nu/J$ is smaller, second-order spectra result: the positions and intensities of the lines deviate from the simple rules, and extra lines may even appear. The simplest second-order system is the AB system of two nuclei with $I = \frac12$; it still has four lines, but the two inner lines are strengthened and the two outer lines weakened, and the two doublets "lean toward each other", which is called the roof effect; the chemical shifts are not at the midpoints of the doublets. Quantum mechanics gives the exact result: with $D = \sqrt{(\Delta\nu)^2 + J^2}$, the four lines lie at $\pm(D \pm J)/2$ from the center, and the intensity ratio of the inner to the outer lines is $(1 + J/D):(1 - J/D)$. As $\Delta\nu \to 0$ the outer lines vanish and the inner lines merge into one (the $\mathrm{A_2}$ system; coupling between equivalent nuclei does not show).

![Line shape of an AB system (J = 8 Hz) as a function of Δν/J: at Δν/J = 10 the spectrum is nearly first order (AX); as Δν/J decreases, the inner lines grow and the outer lines weaken (roof effect); at Δν = 0 it becomes a singlet (A₂); red bars mark the chemical shifts of A and B](./plots/ab-system.py)

The roof effect is also useful: the direction of the lean points toward the group of peaks to which a multiplet is coupled, which helps to decide which two groups of peaks are coupled. Raising the field increases $\Delta\nu$ (in $\mathrm{Hz}$) while $J$ is unchanged, so second-order spectra tend toward first-order ones, another advantage of high-field spectrometers.

### 12.3.6. Peak Area and Quantitation

Under conditions of full relaxation, the integrated area of a group of peaks is proportional to the number of nuclei producing it. The spectrometer plots the integral curve on the spectrum, and the ratio of the integral heights of the groups of peaks is the ratio of the numbers of the various kinds of hydrogen. Because an NMR signal responds equally to every nucleus, independently of molecular structure, in the **internal standard method** ([6.4.1](/6.4.1#def-1.8.9)) a known amount of a high-purity internal standard (such as maleic acid or 1,3,5-trimethoxybenzene) is added to the sample and the integrals of the two are compared to obtain the content or purity of the sample, without a reference standard of the analyte. This quantitative NMR (qNMR) is one of the primary methods for determining the purity of organic compounds; it requires a wait of $5T_1$ or more between acquisitions so that all nuclei relax completely.

### 12.3.7. Decoupling

**Definition 12.3.5 (Decoupling)** The method in which a second radiofrequency field irradiates continuously at the resonance frequency of one group of nuclei, so that the spin states of this group flip rapidly and the average local field experienced by the nuclei coupled to them no longer splits their lines, causing the original multiplets to collapse into singlets, is called **decoupling** (double irradiation).

Homonuclear decoupling is used to determine which peaks are coupled to each other; heteronuclear broadband decoupling (irradiating all $^1\mathrm{H}$) is the routine method for $^{13}\mathrm{C}$ spectra (12.5.1). Take isopropyl acetate $\ce{CH3COOCH(CH3)2}$ as an example: in the ordinary hydrogen spectrum the acetyl $\ce{CH3}$ is a singlet at $\delta \approx 2.0$, the two $\ce{CH3}$ groups (6 H) of the isopropyl group give a doublet at $\delta \approx 1.2$, and the $\ce{CH}$ gives a septet at $\delta \approx 5.0$. On irradiating the methyl groups at $\delta = 1.2$, the septet collapses into a singlet; on irradiating the methine at $\delta = 5.0$, the doublet collapses into a singlet. This confirms that the two groups of peaks are coupled to each other.

```smiles
CC(=O)OC(C)C
```

### 12.3.8. Example: Methyl Butanoate

**Example 12.3.1** A compound of molecular formula $\ce{C5H10O2}$ has the $^1\mathrm{H}$ NMR spectrum $\delta$ $3.67$ (singlet), $2.30$ (triplet), $1.65$ (sextet), $0.95$ (triplet), with integral ratio $3:2:2:3$. Deduce its structure.

**Solution** The degree of unsaturation is $U = 1 + 5 - 10/2 = 1$. The 10 hydrogens divide by the integral ratio into groups of 3, 2, 2 and 3. The three-hydrogen singlet at $3.67$ has a large chemical shift and no neighboring hydrogens and is an $\ce{OCH3}$ attached to oxygen; the remainder is $\mathrm{C_3H_7}$ and one $\ce{C=O}$ (which uses up the degree of unsaturation). The triplet at $0.95$ is a $\ce{CH3}$ adjacent to a $\ce{CH2}$; the triplet at $2.30$ is a $\ce{CH2}$ adjacent to $\ce{C=O}$ and bonded to another $\ce{CH2}$ on the other side; the $\ce{CH2}$ at $1.65$ has $3 + 2 = 5$ neighboring hydrogens in total. The structure is methyl butanoate $\ce{CH3CH2CH2COOCH3}$:

```smiles
CCCC(=O)OC
```

The middle $\ce{CH2}$ is coupled to the $\ce{CH3}$ and to the other $\ce{CH2}$ and should in principle give $4\times3 = 12$ lines according to $(n + 1)(m + 1)$; but the two coupling constants are almost equal (both about $7.4\,\mathrm{Hz}$), so the 12 lines coincide into a sextet with intensity ratio $1:5:10:10:5:1$, that is, $n + m + 1 = 6$. Seeing only six lines does not mean that the instrumental resolution is insufficient: even with infinite resolution the lines would coincide, because the coupling constants are equal.

## 12.4. NMR Spectrometers

### 12.4.1. Basic Components

An NMR spectrometer consists of four parts: a magnet that produces a strong and homogeneous static field; a probe that holds the sample, transmits the radiofrequency pulses and receives the signal; a radiofrequency generator, receiver and digitizing system (the console); and a computer that performs the Fourier transform and data processing.

### 12.4.2. Magnets

- Permanent magnets: the field is generally no more than $2\,\mathrm{T}$ ($85\,\mathrm{MHz}$ for $^1\mathrm{H}$); simple and economical, consuming no electric power or cryogens, but sensitive to temperature, so that thermostating is required. Present-day benchtop NMR instruments ($40$–$100\,\mathrm{MHz}$) use permanent magnets and serve for teaching, reaction monitoring and quality control.
- Electromagnets: the field does not exceed about $2.35\,\mathrm{T}$; they need a high-power supply and water cooling, and have been phased out.
- Superconducting magnets: coils of niobium–titanium alloy wire (with niobium–tin at high fields) immersed in liquid helium at $4.2\,\mathrm{K}$ and thermally shielded by a liquid-nitrogen jacket. The coils are in the superconducting state, the current flows continuously in a closed circuit, and the field is extremely stable; only periodic refilling with liquid helium and liquid nitrogen is needed. Magnets of $400$–$800\,\mathrm{MHz}$ ($9.4$–$18.8\,\mathrm{T}$) are the most common; in the 1990s the highest was $750\,\mathrm{MHz}$ ($17.6\,\mathrm{T}$), and since 2020 commercial $1.2\,\mathrm{GHz}$ ($28.2\,\mathrm{T}$) spectrometers with inserts of high-temperature superconducting coils have been available, used mainly for biological macromolecules.

A higher field has three benefits: the sensitivity increases (roughly $\propto B_0^{3/2}$), chemical shift differences (in $\mathrm{Hz}$) increase and the peaks are more widely dispersed, and second-order effects weaken. Besides the field strength, the homogeneity and stability of the field are equally important: to resolve a line width of $0.1\,\mathrm{Hz}$ at $500\,\mathrm{MHz}$, the relative variation of the field over the sample volume must be below $10^{-10}$. For this purpose a set of shim coils produces correcting fields (shimming), and the $^2\mathrm{H}$ signal of the deuterated solvent is used as feedback to compensate drift of the field at all times (field locking).

### 12.4.3. Continuous Wave and Pulsed Fourier Transform

Early continuous-wave (CW) spectrometers either swept the radiofrequency at fixed field (frequency sweep) or swept the field at fixed frequency (field sweep), so that the groups of nuclei came into resonance in turn. At any moment only a small range of frequencies is in resonance and all other nuclei are "waiting", so recording a spectrum takes several minutes and the sensitivity is low, the same predicament as that of the dispersive infrared spectrometer ([6.4.11](/6.4.11#sec-11.3.2)).

**Definition 12.4.1 (Pulsed Fourier-Transform NMR)** The method in which a strong, short radiofrequency pulse excites all the resonance frequencies of one kind of nucleus simultaneously, the time signal after the pulse is recorded and the spectrum is obtained from it by a Fourier transform is called **pulsed Fourier-transform NMR** (FT-NMR).

Viewed in a coordinate system rotating at the radiofrequency, the radiofrequency field $B_1$ is stationary and the magnetization $\boldsymbol{M}$ rotates about $B_1$ during the pulse with angular frequency $\gamma B_1$; a pulse of duration $t_{\mathrm{p}}$ rotates $\boldsymbol{M}$ through an angle $\theta = \gamma B_1t_{\mathrm{p}}$. A pulse that rotates $\boldsymbol{M}$ from the $z$ axis into the transverse plane is called a $90^\circ$ pulse, with a typical length of about $10\,\mu\mathrm{s}$; the shorter the pulse, the wider the range of frequencies excited (about $1/t_{\mathrm{p}}$, that is, about $100\,\mathrm{kHz}$), enough to cover the whole spectral width of $^1\mathrm{H}$ (about $6\,\mathrm{kHz}$ at $500\,\mathrm{MHz}$) or of $^{13}\mathrm{C}$ (about $28\,\mathrm{kHz}$).

**Definition 12.4.2 (Free Induction Decay)** After the pulse ends, the components of the transverse magnetization precess about $B_0$ at their respective Larmor frequencies and induce a decaying oscillating voltage in the receiver coil. This signal is called the **free induction decay** (FID).

Each nucleus of a given chemical shift contributes an oscillation at its resonance frequency, decaying as $\exp(-t/T_2)$, and the FID is their superposition:

$$
s(t) = \sum_k A_k\,\mathrm{e}^{2\pi\mathrm{i}\nu_kt}\,\mathrm{e}^{-t/T_{2,k}}.
\tag{12.8}
$$
($\nu_k$ is the frequency relative to the radiofrequency carrier; the receiver detects two quadrature components simultaneously, so the signal is complex.) Under the Fourier transform of $s(t)$, each term becomes a Lorentzian peak at $\nu_k$ with full width at half maximum $1/(\pi T_{2,k})$ (Eq. (12.5)) and area proportional to $A_k$. In practice the FID is digitized at equal time intervals and the transform is computed with the **fast Fourier transform** ([4.4.4](/4.4.4#sec-4.7)): the sampling interval $\Delta t$ determines the spectral width ($1/\Delta t$) and the total sampling time determines the digital resolution.

![Free induction decay of two spectral lines (left) and the spectrum obtained from it by the fast Fourier transform (right): with T₂ = 0.5 s the FID decays slowly and the lines are narrow (0.64 Hz); with T₂ = 0.05 s the FID decays quickly and the lines are 10 times broader](./plots/nmr-fid-spectrum.py)

The advantage of FT-NMR is that a single pulse excites all the nuclei, the whole spectrum is obtained in seconds, and the experiment can be repeated many times in a short time with the FIDs accumulated. The signal is coherent and grows by a factor of $n$ on $n$ accumulations; the noise is random and grows only by a factor of $\sqrt n$, so that the signal-to-noise ratio

$$
S/N \propto \sqrt{n}.
$$
Four accumulations double the signal-to-noise ratio and 100 accumulations improve it tenfold. A typical $^1\mathrm{H}$ spectrum needs 8–16 accumulations and a minute or two, a $^{13}\mathrm{C}$ spectrum hundreds to thousands of accumulations and minutes to hours. More importantly, pulse methods allow the design of many pulse sequences to manipulate the nuclear spins: for example, the inversion-recovery sequence $180^\circ$–$\tau$–$90^\circ$ measures $T_1$, the spin echo ($90^\circ$–$\tau$–$180^\circ$–$\tau$) cancels the effect of field inhomogeneity to measure $T_2$, and the NOE, polarization transfer, two-dimensional spectra and imaging described later in this chapter are all built on pulse methods.

### 12.4.4. Probes and Samples

The probe is a cylindrical component at the center of the magnet containing a radiofrequency coil tuned to the frequency of the nucleus under study, which both transmits the pulses and receives the signal. Dual-nucleus probes ($^1\mathrm{H}$/$^{13}\mathrm{C}$) and multinuclear broadband probes can measure different nuclei; inverse probes have the inner coil for $^1\mathrm{H}$ detection and suit heteronuclear two-dimensional spectra (12.5.3). A cryoprobe cools the coil and preamplifier to about $20\,\mathrm{K}$, greatly reducing thermal noise and improving the signal-to-noise ratio by a factor of 3–4, which is equivalent to shortening the measurement time by about a factor of 10 and is of great significance for biological samples of low concentration.

Samples are usually prepared as solutions in glass tubes of $5\,\mathrm{mm}$ outer diameter (about $0.6\,\mathrm{mL}$): small organic molecules need a few milligrams (more for $^{13}\mathrm{C}$ spectra) and proteins $0.1$–$1\,\mathrm{mmol\,L^{-1}}$. The solvent should contain no hydrogen, or a deuterated solvent should be used ($\ce{CDCl3}$, $\ce{DMSO}$-$d_6$, $\ce{D2O}$, $\ce{CD3OD}$, $\ce{C6D6}$), so that strong solvent peaks do not mask the sample and the $^2\mathrm{H}$ signal needed for field locking is provided; to observe amide protons, proteins are measured in $90\%$ $\ce{H2O}$/$10\%$ $\ce{D2O}$ with pulse sequences that suppress the water peak. The viscosity of the solution should not be too high, and solid particles and paramagnetic impurities broaden the lines.

## 12.5. Carbon Spectra and Two-Dimensional NMR

### 12.5.1. Carbon-13 NMR

$^{13}\mathrm{C}$ has $I = \frac12$, a natural abundance of $1.07\%$ and a sensitivity of only about $1/5900$ of that of $^1\mathrm{H}$, so $^{13}\mathrm{C}$ NMR became a routine method only after the appearance of FT methods. The low abundance also has an advantage: the probability that a molecule contains two $^{13}\mathrm{C}$ atoms is only about $10^{-4}$, so $^{13}\mathrm{C}$–$^{13}\mathrm{C}$ coupling can be ignored, and after the $^1\mathrm{H}$ couplings are removed by broadband decoupling each chemically inequivalent carbon gives a single peak. The range of $^{13}\mathrm{C}$ chemical shifts is about $0$–$220\,\mathrm{ppm}$, about 20 times that of hydrogen spectra, and the peaks seldom overlap; in general there are as many peaks as kinds of carbon in the molecule, giving direct information on the carbon skeleton. For example, cyclohexene has only three peaks ($127.3$, $25.3$, $22.9$), corresponding to the three kinds of carbon determined by the symmetry of the molecule.

Ranges of chemical shifts of common carbons (relative to TMS):

| Carbon type | $\delta$ | Carbon type | $\delta$ |
|---|---|---|---|
| $\ce{R-CH3}$ | $0$–$35$ | $\ce{C#C}$ | $65$–$90$ |
| $\ce{R2CH2}$ | $15$–$40$ | $\ce{C=C}$ | $100$–$150$ |
| $\ce{R3CH}$ | $25$–$50$ | aromatic carbon | $110$–$160$ |
| $\ce{C-N}$ | $30$–$65$ | $\ce{C#N}$ | $115$–$125$ |
| $\ce{C-O}$ (alcohols, ethers) | $50$–$90$ | $\ce{C=O}$ of carboxylic acids, esters, amides | $160$–$185$ |
| | | $\ce{C=O}$ of aldehydes, ketones | $190$–$220$ |

Broadband decoupling has a further effect: irradiating $^1\mathrm{H}$ enhances the signals of the $^{13}\mathrm{C}$ nuclei adjacent to them.

**Definition 12.5.1 (Nuclear Overhauser Effect)** The change in the signal intensity of one nucleus that results from saturating (or inverting) the resonance of another nucleus close to it in space, through cross-relaxation caused by the magnetic dipole–dipole interaction between the two nuclei, is called the **nuclear Overhauser effect** (NOE).

The NOE in $^{13}\mathrm{C}\{^1\mathrm{H}\}$ experiments enhances the carbon signal by a factor of up to $1 + \gamma_{\mathrm{H}}/(2\gamma_{\mathrm{C}}) = 2.99$. The NOE arises from the dipolar interaction, its magnitude is proportional to the $-6$th power of the distance between the two nuclei, and it is significant only within about $0.5\,\mathrm{nm}$, which makes it a tool for measuring interatomic distances in molecules (12.5.3).

The peak intensities of an ordinary (broadband-decoupled) $^{13}\mathrm{C}$ spectrum are not strictly proportional to the number of carbon atoms: the NOE enhancement differs from carbon to carbon, and quaternary carbons, with no directly attached hydrogen, have a small NOE and a long $T_1$ (up to tens of seconds) and relax incompletely under rapid accumulation, so that their peaks are very weak. But the statement that "the peak intensities of carbon spectra are independent of the number of carbons and cannot be used for quantitation" is too absolute: with inverse-gated decoupling (decoupling only during acquisition, which removes the couplings without generating an NOE) and an acquisition interval lengthened to $5T_1$ or more (or with a paramagnetic relaxation reagent added), $^{13}\mathrm{C}$ spectra can also be quantitative.

To distinguish how many hydrogens are attached to a carbon, the DEPT experiment (distortionless enhancement by polarization transfer) is commonly used: it transfers the polarization of $^1\mathrm{H}$ to $^{13}\mathrm{C}$, enhancing the signal by about $\gamma_{\mathrm{H}}/\gamma_{\mathrm{C}} \approx 4$; in the DEPT-135 spectrum $\ce{CH}$ and $\ce{CH3}$ give positive peaks and $\ce{CH2}$ negative peaks, and the DEPT-90 spectrum shows only $\ce{CH}$ peaks; quaternary carbons give no peaks, and comparison with the ordinary carbon spectrum determines the type of every carbon.

### 12.5.2. Principles of Two-Dimensional NMR

In the one-dimensional spectra of complex molecules the peaks overlap severely, and the coupling relationships are difficult to extract from the multiplets one by one.

**Definition 12.5.2 (Two-Dimensional NMR)** A pulse sequence into which an evolution time $t_1$ that is incremented stepwise is introduced, so that for each $t_1$ an FID is recorded as a function of the detection time $t_2$ and a two-variable signal $s(t_1, t_2)$ is obtained; Fourier transformation with respect to both time variables then gives a spectrum with the two frequencies $F_1$ and $F_2$ as coordinates. This method is called **two-dimensional NMR** (2D NMR).

The general structure of a two-dimensional experiment is "preparation, evolution ($t_1$), mixing, detection ($t_2$)": during the evolution period the magnetization precesses at the frequency of a nucleus, and this frequency is "labeled" on the phase or amplitude of the signal; during the mixing period the magnetization is transferred to another nucleus through coupling or the NOE; during the detection period it precesses at the frequency of the latter. A peak (cross peak) appearing at $(F_1, F_2) = (\nu_A, \nu_B)$ therefore shows that there is an interaction between nuclei A and B. The two-dimensional spectrum spreads signals that are crowded on a single frequency axis in a one-dimensional spectrum over a plane, which both reduces overlap and shows directly the connections between nuclei.

### 12.5.3. Common Two-Dimensional Spectra

| Two-dimensional spectrum | Two dimensions | Meaning of the cross peak | Main use |
|---|---|---|---|
| COSY (correlation spectroscopy) | $^1\mathrm{H}$–$^1\mathrm{H}$ | two protons coupled through $^2J$ or $^3J$ | tracing neighboring protons, linking spin systems |
| TOCSY (total correlation spectroscopy) | $^1\mathrm{H}$–$^1\mathrm{H}$ | all protons in one uninterrupted coupling network | identifying complete spin systems such as amino acid residues and sugar rings |
| HSQC (heteronuclear single-quantum correlation) | $^1\mathrm{H}$–$^{13}\mathrm{C}$ or $^1\mathrm{H}$–$^{15}\mathrm{N}$ | directly bonded ($^1J$) H and C (or N) | matching hydrogens with the carbons that carry them; the "fingerprint spectrum" of proteins |
| HMBC (heteronuclear multiple-bond correlation) | $^1\mathrm{H}$–$^{13}\mathrm{C}$ | H and C separated by 2–3 bonds | connecting structural fragments across quaternary carbons and heteroatoms |
| NOESY (NOE spectroscopy) | $^1\mathrm{H}$–$^1\mathrm{H}$ | protons closer than about $0.5\,\mathrm{nm}$ in space, intensity $\propto r^{-6}$ | determining configuration, conformation and the three-dimensional structure of macromolecules |

In a COSY spectrum both axes are $^1\mathrm{H}$ chemical shifts; the peaks on the diagonal (diagonal peaks) reproduce the one-dimensional spectrum and give no coupling information, and cross peaks off the diagonal, symmetric about it, show that two groups of protons are coupled to each other. Starting from one peak and following "diagonal peak, cross peak, diagonal peak", one can link the protons along an entire carbon chain.

![Schematic COSY spectrum of methyl butanoate: dots are diagonal peaks and squares are cross peaks; the cross peaks between δ 2.30 and 1.65 and between 1.65 and 0.95 connect the three groups of protons of the propyl chain, and the OCH₃ at δ 3.67 has no cross peak](./plots/cosy-schematic.py)

The $^1\mathrm{H}$–$^{15}\mathrm{N}$ HSQC is especially important in protein studies: except for proline, the backbone amide $\ce{N-H}$ of every amino acid residue gives one peak, and well-dispersed peaks show that the protein is properly folded; which peaks move on addition of a ligand (chemical shift perturbation) indicates the binding site, a method commonly used in fragment-based drug screening.

### 12.5.4. Determination of Protein Structures in Solution

The method established by Wüthrich in the 1980s made NMR one of the three methods of structural biology, together with X-ray crystallography and cryo-electron microscopy. The main steps are the following.

1. Sample: the protein is expressed in a medium with $\ce{^{15}NH4Cl}$ and $^{13}\mathrm{C}$-glucose as the sole nitrogen and carbon sources so that it is uniformly labeled with $^{15}\mathrm{N}$ and $^{13}\mathrm{C}$ (large proteins are also deuterated) and prepared as a solution of about $0.1$–$1\,\mathrm{mmol\,L^{-1}}$.
2. Sequence-specific assignment: TOCSY identifies the spin system of each residue, and short distances between neighboring residues in NOESY (for example, between an $\alpha$ proton and the amide proton of the next residue) link them in the order of the amino acid sequence; labeled proteins are linked directly along the backbone with $^1\mathrm{H}$–$^{15}\mathrm{N}$–$^{13}\mathrm{C}$ triple-resonance experiments.
3. Structural constraints: the intensities of NOESY cross peaks give upper limits for proton–proton distances ($\le 0.5\,\mathrm{nm}$, calibrated according to $r^{-6}$); $^3J_{\mathrm{HN,H\alpha}}$ gives the backbone dihedral angle $\phi$ through the Karplus relation (12.3.3); the chemical shifts themselves are also related to secondary structure ($\mathrm{C}_\alpha$ shifts downfield in $\alpha$-helices and upfield in $\beta$-sheets); slowly exchanging amide protons (12.2.3) indicate hydrogen bonds; and residual dipolar couplings measured in weakly orienting media give the orientations of bond vectors.
4. Structure calculation: using these constraints as targets, simulated annealing or restrained molecular dynamics yields a set (typically about 20) of structures that all satisfy the constraints, and the spread among them reflects the precision of the structure.

Compared with crystallography, NMR determines structures in solution under near-physiological conditions, needs no crystals, can measure the motions of proteins on all time scales from picoseconds to seconds (relaxation, chemical exchange), and can study intrinsically disordered proteins and weak interactions; its limitation is molecular size, conventional methods being suited to proteins below about $30$–$50\,\mathrm{kDa}$, while deuteration, TROSY and methyl-selective labeling allow larger complexes to be studied. NMR is also used in metabolomics (direct measurement of the $^1\mathrm{H}$ spectra of dozens of metabolites in biological fluids such as urine and serum) and in the study of proteins inside cells. These topics are treated further in [chemical biology](/6.6).

## 12.6. Solid-State NMR and Magnetic Resonance Imaging

### 12.6.1. Solid-State NMR

In solids, solution methods give lines tens of $\mathrm{kHz}$ wide that provide almost no chemical information. There are two reasons. One is the magnetic dipole–dipole interaction between nuclei, whose magnitude is proportional to the $-3$rd power of the internuclear distance and to $(3\cos^2\theta - 1)$ ($\theta$ is the angle between the internuclear vector and $B_0$). The other is the anisotropy of the chemical shift: the shielding constant varies with the orientation of the molecule relative to $B_0$ and likewise contains a $(3\cos^2\theta - 1)$ term. In solution the molecules tumble rapidly and isotropically, the average of $\cos^2\theta$ is $1/3$, and both terms average to zero; in a solid the orientations of the molecules are fixed and differ from each other, and the spectrum of a powder sample is the superposition of all orientations, a broad "powder pattern".

**Definition 12.6.1 (Magic-Angle Spinning)** The method in which the sample is spun at high speed about an axis at the angle $\theta_{\mathrm{m}} = \arccos(1/\sqrt3) = 54.74^\circ$ to $B_0$, so that the factor $(3\cos^2\theta - 1)$ in the dipolar interaction and in the chemical shift anisotropy averages to zero over time and the lines are narrowed, is called **magic-angle spinning** (MAS), and $\theta_{\mathrm{m}}$ is called the magic angle.

The spinning rate must exceed the magnitude of the anisotropic interaction (in $\mathrm{Hz}$) for the line to become a narrow line; at lower rates a series of spinning sidebands separated by the spinning rate appears on both sides of the central peak. Modern MAS probes spin at $10$–$100\,\mathrm{kHz}$ or more.

![Left: the orientation factor 3cos²θ − 1 in the dipolar coupling and the chemical shift anisotropy, which vanishes at the magic angle of 54.74°; right: simulated spectra for an axially symmetric chemical shift tensor (anisotropy 8 kHz), showing the broad static powder pattern, the central peak and spinning sidebands at 2 kHz magic-angle spinning, and almost a single narrow line at 12 kHz](./plots/magic-angle.py)

**Definition 12.6.2 (Cross Polarization)** The method of transferring the polarization of abundant nuclei ($^1\mathrm{H}$) to rare nuclei ($^{13}\mathrm{C}$, $^{15}\mathrm{N}$) through the dipolar coupling, under the simultaneous action of two radiofrequency fields satisfying the Hartmann–Hahn condition $\gamma_{\mathrm{H}}B_{1\mathrm{H}} = \gamma_{\mathrm{C}}B_{1\mathrm{C}}$, is called **cross polarization** (CP).

Cross polarization enhances the $^{13}\mathrm{C}$ signal by up to $\gamma_{\mathrm{H}}/\gamma_{\mathrm{C}} \approx 4$, and the interval between repeated measurements is determined by the shorter $T_1$ of $^1\mathrm{H}$, so that there is no need to wait for the much longer $T_1$ of $^{13}\mathrm{C}$; during acquisition, high-power $^1\mathrm{H}$ decoupling removes the $^1\mathrm{H}$–$^{13}\mathrm{C}$ dipolar coupling. CP/MAS is the standard method for high-resolution $^{13}\mathrm{C}$ spectra of solids. Solid-state NMR is used for polymers, the crystal forms of drugs (identification of polymorphs), zeolites and catalysts ($^{27}\mathrm{Al}$, $^{29}\mathrm{Si}$), battery materials, and biological systems that cannot be crystallized and are insoluble, such as the structures of amyloid fibrils and membrane proteins.

### 12.6.2. Magnetic Resonance Imaging

**Definition 12.6.3 (Magnetic Resonance Imaging)** The method in which magnetic field gradients that vary linearly with position are superimposed on the static field, so that the resonance frequency of nuclei varies with position and the NMR signal is thereby spatially encoded, and in which the spatial distribution of nuclear density (mainly of $^1\mathrm{H}$ in water and fat) and of relaxation properties is then reconstructed as an image by Fourier transformation, is called **magnetic resonance imaging** (MRI).

Under a gradient $G_x$ along the $x$ direction, $\nu(x) = \gamma(B_0 + G_xx)/(2\pi)$, so the frequency of the signal corresponds directly to position (frequency encoding), and the Fourier transform of the FID is the projection of the sample onto the $x$ direction. Practical imaging uses three sets of gradient coils: a selective pulse together with a gradient excites only a thin slice (slice selection); within the slice one direction is frequency-encoded and the other phase-encoded, and the two-dimensional data acquired ("$k$-space") yield a tomographic image by two-dimensional Fourier transformation. Clinical MRI mostly uses $1.5\,\mathrm{T}$ and $3\,\mathrm{T}$; research systems reach $7\,\mathrm{T}$ and above.

The image contrast of MRI comes mainly not from proton density (the water contents of the various soft tissues differ little) but from differences in relaxation times:

- $T_1$-weighted images (short repetition and echo times): tissues with short $T_1$ give strong signals; fat is bright and cerebrospinal fluid dark.
- $T_2$-weighted images (long repetition and echo times): tissues with long $T_2$ give strong signals; cerebrospinal fluid, edema and many lesions are bright.
- Contrast agents: $\ce{Gd^3+}$ has 7 unpaired electrons and is strongly paramagnetic; its chelates (such as Gd–DTPA and Gd–DOTA) greatly shorten the $T_1$ of the protons of surrounding water molecules, so that sites where the contrast agent accumulates become bright in $T_1$-weighted images, which is used to show blood vessels and lesions with a disrupted blood–brain barrier. The ligand must form a chelate with $\ce{Gd^3+}$ that is very stable both thermodynamically and kinetically, because free $\ce{Gd^3+}$ is toxic (for the **stability constant** of chelates see [6.1.9](/6.1.9#sec-9.7.1)). Iron oxide nanoparticles shorten $T_2$ and darken the region locally.

Functional magnetic resonance imaging (fMRI) uses the blood itself as a contrast agent. Deoxyhemoglobin is paramagnetic and oxyhemoglobin diamagnetic; when neurons are active, the local blood flow increases by more than the oxygen consumption, the proportion of deoxyhemoglobin falls, the local field becomes more homogeneous, $T_2^*$ lengthens and the signal in $T_2^*$-weighted images increases; this is the blood-oxygen-level-dependent (BOLD) signal (Ogawa, 1990). In 1991 Belliveau et al. obtained the first functional images of the human visual cortex by intravenous injection of a contrast agent, and from 1992 the BOLD method made human brain imaging possible without a contrast agent, since when it has become a basic tool of cognitive neuroscience. In addition, diffusion-weighted imaging measures the diffusion of water molecules and is used for early diagnosis of stroke and for tracking nerve fiber tracts; magnetic resonance spectroscopy (MRS) measures the NMR spectra of metabolites (such as creatine, lactate and $N$-acetylaspartate) in vivo. MRI uses no ionizing radiation, but the strong magnetic field requires the strict exclusion of ferromagnetic objects.

## Summary

| Topic | Key points |
|---|---|
| Nuclear spin | nuclei with $I = 0$ (even–even nuclei) give no signal; nuclei with $I = \frac12$ give the narrowest lines |
| Resonance condition | $\nu_0 = \gamma B_0/(2\pi)$; $42.577\,\mathrm{MHz\,T^{-1}}$ for $^1\mathrm{H}$ |
| Sensitivity | population difference $\approx \gamma\hbar B_0/(2k_{\mathrm{B}}T)$, about $10^{-5}$; $S/N \propto \gamma^{5/2}B_0^{3/2}$, accumulation $\propto \sqrt n$ |
| Relaxation | $T_1$ (longitudinal, energy given to the lattice), $T_2$ (transverse, loss of phase coherence); $\Delta\nu_{1/2} = 1/(\pi T_2)$ |
| Chemical shift | $\delta = (\nu - \nu_{\mathrm{ref}})/\nu_{\mathrm{ref}}\times10^6$, independent of field strength; TMS (organic), DSS (aqueous) |
| Influencing factors | electronegativity, ring current (deshielding outside aromatic rings), anisotropy of triple bonds and carbonyls, hybridization, hydrogen bonding and exchange |
| Coupling | $J$ (Hz) independent of field strength; $n + 1$ rule and binomial intensity ratios; $^3J$ given by the Karplus relation |
| Equivalence | chemical equivalence: same $\delta$; magnetic equivalence: in addition the same $J$ to all other nuclei; no splitting among equivalent nuclei |
| Second-order spectra | roof effect at small $\Delta\nu/J$, AB system $D = \sqrt{\Delta\nu^2 + J^2}$ |
| FT-NMR | $90^\circ$ pulse → FID → Fourier transform |
| $^{13}\mathrm{C}$ spectra | $0$–$220\,\mathrm{ppm}$; broadband decoupling and NOE; DEPT; quantitation needs inverse-gated decoupling |
| Two-dimensional spectra | COSY, TOCSY (coupling networks), HSQC, HMBC (heteronuclear), NOESY (distance in space $\propto r^{-6}$) |
| Solid-state NMR | magic angle $54.74^\circ$; cross polarization |
| MRI | spatial encoding by gradient fields; $T_1$ and $T_2$ weighting; $\ce{Gd^3+}$ contrast agents; BOLD |

## Questions

1. According to $\nu_0 = \gamma B_0/(2\pi)$, all protons in the same field resonate at the same frequency. Why can hydrogen spectra nevertheless be used to study molecular structure?

   **Answer** The field actually experienced by a nucleus is $(1 - \sigma)B_0$, and the shielding constant $\sigma$ varies with the electronic structure around the nucleus, so protons in different chemical environments resonate at slightly different frequencies (chemical shifts, 12.2).
2. Why do lines split on a high-resolution spectrometer? How can one decide whether the distance between two lines is a coupling constant or a chemical-shift difference?

   **Answer** The spin states of neighboring magnetic nuclei change the local field experienced by a nucleus through the bonding electrons (spin–spin coupling, 12.3). Measure at different field strengths: a distance in Hz that does not change is a coupling constant, and one proportional to the field strength is a chemical-shift difference.
3. Why does TMS give only one peak?

   **Answer** The 12 hydrogens can be interchanged by the symmetry operations of the molecule and by rapid rotation of the methyl groups and are chemically equivalent; their couplings to the other magnetic nuclei in the molecule (at natural abundance almost only $^1\mathrm{H}$) are also all the same, so they are magnetically equivalent, and coupling between magnetically equivalent nuclei causes no splitting. The satellites from $^{13}\mathrm{C}$ and $^{29}\mathrm{Si}$ are very weak.
