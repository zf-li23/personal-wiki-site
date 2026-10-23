---
title: Infrared and Raman Spectroscopy
description: The harmonic oscillator model and force constants for diatomic molecules, anharmonicity and overtones; normal vibrations of polyatomic molecules, stretching and bending, infrared activity; fundamentals, overtones, combination bands, vibrational coupling and Fermi resonance; group frequencies, the functional group and fingerprint regions, characteristic frequency tables and the factors that influence them, degree of unsaturation and spectrum interpretation, the amide bands of proteins; dispersive and Fourier-transform infrared spectrometers, the interferogram, ATR and sample preparation; infrared quantitation, near-infrared spectroscopy and multivariate calibration; Raman scattering, Stokes and anti-Stokes lines, Raman activity and the rule of mutual exclusion, depolarization ratio, Raman spectrometers, resonance Raman and surface-enhanced Raman scattering.
source_hash: 18434569fe2f
---

The spacings between the vibrational energy levels of molecules lie between $0.05$ and $0.5\,\mathrm{eV}$, and the corresponding radiation falls in the infrared region. Vibrational spectra can be measured in two ways: a molecule absorbs an infrared photon of the same frequency as a vibration (infrared absorption), or an incident visible photon is scattered as a photon whose energy differs from the original by one vibrational quantum (Raman scattering). Both methods measure the same set of vibrations, but their selection rules differ, and the two are therefore complementary. The frequency of a vibration is determined by the force constant of the chemical bond and the masses of the atoms, and is further influenced by neighboring groups; functional groups therefore have their own characteristic frequencies, while the vibrational spectrum of the molecule as a whole is as unique as a fingerprint. This makes vibrational spectroscopy one of the most widely used means of identifying the structure of organic and biological molecules. The quantum mechanics of vibrational and rotational levels was treated in physics ([5.5.5](/5.5.5#sec-5.3)), and the contribution of vibrations to thermodynamic functions in [6.3.11](/6.3.11#sec-11.4). This chapter treats the selection rules and group frequencies of vibrational spectra (11.1–11.2), Fourier-transform infrared spectrometers and sampling techniques (11.3), quantitative analysis and near-infrared spectroscopy (11.4), and finally Raman spectroscopy (11.5). The components common to spectroscopic instruments (monochromators, detectors, noise) are discussed in [6.4.7](/6.4.7#sec-7.1.3), and the absorption law in [6.4.9](/6.4.9#sec-9.3.1). Many worked examples of the combined use of infrared spectra, nuclear magnetic resonance ([6.4.12](/6.4.12)) and mass spectrometry ([6.4.15](/6.4.15#sec-15.4)) for the elucidation of organic structures are given in [organic chemistry](/6.5).

## 11.1. Molecular Vibrations and Infrared Selection Rules

### 11.1.1. The Infrared Region and Infrared Spectroscopy

**Definition 11.1.1 (Infrared Absorption Spectroscopy)** The absorption spectrum produced when molecules absorb infrared radiation and undergo transitions between vibrational (accompanied by rotational) energy levels is called an infrared absorption spectrum. The method of qualitative, quantitative and structural analysis based on it is called **infrared spectroscopy** (IR).

The infrared region is divided by wavelength into three parts, of which the mid-infrared is the most used in organic structure analysis:

| Region | Wavelength | Wavenumber $\tilde\nu$ | Main transitions |
|---|---|---|---|
| Near-infrared | $0.78$–$2.5\,\mu\mathrm{m}$ | $12800$–$4000\,\mathrm{cm^{-1}}$ | overtones and combinations of $\ce{O-H}$, $\ce{N-H}$ and $\ce{C-H}$ stretching vibrations (11.4.2) |
| Mid-infrared | $2.5$–$25\,\mu\mathrm{m}$ | $4000$–$400\,\mathrm{cm^{-1}}$ | fundamental vibrations, accompanied by rotation |
| Far-infrared | $25$–$1000\,\mu\mathrm{m}$ | $400$–$10\,\mathrm{cm^{-1}}$ | skeletal vibrations of heavy atoms, lattice vibrations, pure rotations |

Some authors place the boundary between the mid- and far-infrared at $50\,\mu\mathrm{m}$ ($200\,\mathrm{cm^{-1}}$). The abscissa of an infrared spectrum is usually the wavenumber (decreasing from $4000$ to $400\,\mathrm{cm^{-1}}$ from left to right) and the ordinate is the **transmittance** $\tau$ (in percent, absorption peaks pointing downward) or the absorbance. The wavenumber is proportional to the energy; $1000\,\mathrm{cm^{-1}}$ corresponds to $0.124\,\mathrm{eV}$ or $12.0\,\mathrm{kJ\,mol^{-1}}$ ([6.4.7](/6.4.7#sec-7.1.1)).

In 1800 Herschel used a thermometer to discover "invisible heat radiation" beyond the red end of the solar spectrum. Commercial double-beam prism infrared spectrophotometers appeared in the 1940s, gratings replaced prisms in the 1960s, and Fourier-transform infrared spectrometers became widespread in the 1970s; attenuated total reflection, infrared microscopy and infrared imaging followed. The characteristics of infrared spectroscopy are these: almost all compounds except monatomic and homonuclear diatomic molecules absorb in the infrared; gases, liquids and solids can all be measured; the spectra are rich in information and are used mainly for identification and structure determination, but also for quantitation; and the technique can serve as a detector for chromatography.

### 11.1.2. Diatomic Molecules: The Harmonic Oscillator Model

If a chemical bond is regarded as a massless spring and the two atoms as balls of masses $m_1$ and $m_2$, the vibration about the equilibrium position is **simple harmonic motion**. By Hooke's law, the vibrational frequency depends only on the force constant $k$ and the **reduced mass** $\mu = m_1m_2/(m_1 + m_2)$:

$$
\nu = \frac{1}{2\pi}\sqrt{\frac{k}{\mu}},\qquad \tilde\nu = \frac{\nu}{c} = \frac{1}{2\pi c}\sqrt{\frac{k}{\mu}}.
\tag{11.1}
$$
Inserting the constants, with $k$ in units of $10^2\,\mathrm{N\,m^{-1}}$ and $\mu$ in atomic mass units $\mathrm{u}$,

$$
\tilde\nu/\mathrm{cm^{-1}} \approx 1303\sqrt{\frac{k/(10^2\,\mathrm{N\,m^{-1}})}{\mu/\mathrm{u}}}.
\tag{11.2}
$$
In quantum mechanics the vibrational levels are those of the **quantum harmonic oscillator**, $E_v = (v + \frac12)h\nu$, with the selection rule $\Delta v = \pm 1$, so that the absorption frequency equals the classical frequency of Eq. (11.1) ([5.5.5](/5.5.5#sec-5.3.3)). At room temperature $k_{\mathrm{B}}T \approx 207\,\mathrm{cm^{-1}}$ is much smaller than a vibrational quantum, and nearly all molecules are in $v = 0$ ([6.3.11](/6.3.11#sec-11.4)), so infrared absorption is dominated by $v = 0 \to 1$.

Two rules follow from Eq. (11.1):

- Between atoms of the same kind, the higher the bond order and the larger the force constant, the higher the frequency. The force constants of carbon–carbon single, double and triple bonds are about $5$, $10$ and $15\times10^2\,\mathrm{N\,m^{-1}}$; with $\mu = 6.0\,\mathrm{u}$, Eq. (11.2) gives $1190$, $1680$ and $2060\,\mathrm{cm^{-1}}$, in agreement with the observed values of about $1200$ for $\ce{C-C}$, $1650$ for $\ce{C=C}$ and $2150\,\mathrm{cm^{-1}}$ for $\ce{C#C}$.
- For similar force constants, the smaller the reduced mass, the higher the frequency. For $\ce{C-H}$, $\mu = 0.93\,\mathrm{u}$ and the force constant is about $4.8\times10^2\,\mathrm{N\,m^{-1}}$, giving $\tilde\nu \approx 2960\,\mathrm{cm^{-1}}$, far higher than for $\ce{C-C}$. The stretching vibrations of all hydrogen-containing groups ($\ce{O-H}$, $\ce{N-H}$, $\ce{C-H}$) therefore lie above $2800\,\mathrm{cm^{-1}}$.

**Example 11.1.1** (1) The fundamental of $\mathrm{H}^{35}\mathrm{Cl}$ is $2886\,\mathrm{cm^{-1}}$ ([5.5.5](/5.5.5#sec-5.3.3)); find the force constant. (2) Estimate the stretching wavenumber of a carbonyl group $\ce{C=O}$ ($k \approx 12\times10^2\,\mathrm{N\,m^{-1}}$). (3) Where does the stretching vibration move when $\ce{C-H}$ is replaced by $\ce{C-D}$?

**Solution** (1) $\mu = \frac{1.008\times34.969}{1.008 + 34.969}\,\mathrm{u} = 0.980\,\mathrm{u}$, and by Eq. (11.2), $k = 0.980\times(2886/1303)^2\times10^2\,\mathrm{N\,m^{-1}} = 481\,\mathrm{N\,m^{-1}}$.

(2) $\mu = \frac{12\times16}{28}\,\mathrm{u} = 6.86\,\mathrm{u}$, and $\tilde\nu \approx 1303\sqrt{12/6.86} = 1720\,\mathrm{cm^{-1}}$, in agreement with the observed value of $1715\,\mathrm{cm^{-1}}$ for aliphatic ketones.

(3) The force constant does not change on isotopic substitution; $\mu(\ce{C-D}) = 1.72\,\mathrm{u}$, so the frequency falls by the factor $\sqrt{0.930/1.72} = 1/1.36$ to about $2170\,\mathrm{cm^{-1}}$, in a "clear region" in which few other groups absorb. Deuterium labeling is used both to assign bands and to trace metabolites in cells through the $\ce{C-D}$ vibration (11.5.4), and both rely on this.

Older literature uses CGS units and writes force constants in $\mathrm{dyn\,cm^{-1}}$ (that is, $\mathrm{g\,s^{-2}}$) or $\mathrm{mdyn\,Å^{-1}}$: $1\,\mathrm{mdyn\,Å^{-1}} = 10^5\,\mathrm{dyn\,cm^{-1}} = 10^2\,\mathrm{N\,m^{-1}}$, so a single bond is about $5\times10^5\,\mathrm{g\,s^{-2}}$.

### 11.1.3. Anharmonicity and Overtones

The actual **potential energy curve** is not a parabola: the bond breaks when the internuclear distance becomes large, and the potential energy approaches the dissociation limit. It is commonly described by the **Morse potential** ([6.3.16](/6.3.16#def-16.2.1)), whose energy levels are

$$
E_v = hc\Big[\tilde\omega_{\mathrm{e}}\Big(v + \frac12\Big) - \tilde\omega_{\mathrm{e}}x_{\mathrm{e}}\Big(v + \frac12\Big)^2\Big],
\tag{11.3}
$$
where $\tilde\omega_{\mathrm{e}}$ is the harmonic wavenumber and $x_{\mathrm{e}}$ (about $0.005$–$0.02$) is the anharmonicity constant. The level spacing decreases with increasing $v$, and the selection rule is relaxed to $\Delta v = \pm1, \pm2, \dots$ (with rapidly decreasing transition probability). The wavenumber of the $v = 0\to1$ transition is $\tilde\omega_{\mathrm{e}}(1 - 2x_{\mathrm{e}})$ and that of $v = 0\to2$ is $2\tilde\omega_{\mathrm{e}}(1 - 3x_{\mathrm{e}})$, slightly less than twice the former. For $\ce{HCl}$, $\tilde\omega_{\mathrm{e}} = 2990.9\,\mathrm{cm^{-1}}$ and $\tilde\omega_{\mathrm{e}}x_{\mathrm{e}} = 52.8\,\mathrm{cm^{-1}}$, which give $2885$ and $5665\,\mathrm{cm^{-1}}$; the observed values are $2886$ and $5668\,\mathrm{cm^{-1}}$, and the intensity of the latter is about one percent of that of the former.

![The harmonic oscillator potential (dashed) and the Morse potential (solid) of H³⁵Cl with their vibrational levels: the level spacing of the Morse potential decreases with increasing v, so the 0→2 transition (first overtone, 5665 cm⁻¹) lies slightly below twice the fundamental (2885 cm⁻¹)](./plots/anharmonic-levels.py)

### 11.1.4. Normal Vibrations of Polyatomic Molecules

A molecule of $N$ atoms has $3N$ motional **degrees of freedom**. Subtracting the 3 of overall translation and the 3 of rotation (only 2 for a linear molecule, since rotation about the bond axis is meaningless) leaves $3N - 6$ vibrational degrees of freedom ($3N - 5$ for a linear molecule). In the small-amplitude approximation a complicated vibration can be decomposed into $3N - 6$ independent **normal modes**: in each normal mode all atoms pass through their equilibrium positions with the same frequency and the same phase, and each is equivalent to a harmonic oscillator ([6.3.11](/6.3.11#sec-11.4)). According to the manner of atomic motion, normal vibrations fall into two large classes.

**Definition 11.1.2** Vibrations in which the bond length changes while the bond angle remains essentially unchanged are called **stretching vibrations** (symbol $\nu$), divided into symmetric stretching $\nu_{\mathrm{s}}$ and asymmetric (antisymmetric) stretching $\nu_{\mathrm{as}}$. Vibrations in which the bond angle changes while the bond length remains essentially unchanged are called **bending vibrations** (deformation vibrations), divided into in-plane bending (scissoring $\delta$, in-plane rocking $\rho$) and out-of-plane bending (out-of-plane wagging $\omega$, twisting $\tau$).

Changing a bond angle is easier than changing a bond length, so the frequencies of a given group generally follow $\nu_{\mathrm{as}} > \nu_{\mathrm{s}} > \delta$. The six vibrations of the methylene group are shown in the figure below.

![The six vibrations of a CH₂ group: symmetric and antisymmetric stretching, scissoring and in-plane rocking (arrows are atomic displacements), out-of-plane wagging and twisting (+ and − denote displacement out of and into the plane of the paper)](./plots/ch2-modes.py)

**Example 11.1.2** $\ce{H2O}$ is a nonlinear triatomic molecule with $3\times3 - 6 = 3$ normal vibrations: symmetric stretching $3657\,\mathrm{cm^{-1}}$, bending $1595\,\mathrm{cm^{-1}}$ and antisymmetric stretching $3756\,\mathrm{cm^{-1}}$ (gas phase). $\ce{CO2}$ is linear and has $3\times3 - 5 = 4$ normal vibrations: symmetric stretching (about $1333\,\mathrm{cm^{-1}}$), antisymmetric stretching ($2349\,\mathrm{cm^{-1}}$) and two mutually perpendicular bending vibrations of the same frequency ($667\,\mathrm{cm^{-1}}$, a **degeneracy** of two). All three vibrations of $\ce{H2O}$ change the dipole moment and absorb infrared light. In the symmetric stretching of $\ce{CO2}$ the two $\ce{C=O}$ bond dipoles always cancel and the dipole moment remains zero, so this vibration does not absorb infrared light; the infrared spectrum of $\ce{CO2}$ therefore has only two fundamental peaks, at $2349$ and $667\,\mathrm{cm^{-1}}$ (the $667\,\mathrm{cm^{-1}}$ peak is two degenerate vibrations superimposed).

### 11.1.5. Infrared Activity and Absorption Intensity

The medium through which the radiation field couples to a vibrating molecule is the molecular **electric dipole moment** $\boldsymbol{p}$. Only if the vibration makes the dipole moment vary periodically is the molecule equivalent to an electric dipole oscillating at the vibrational frequency, able to exchange energy with an electromagnetic wave of that frequency.

**Definition 11.1.3 (Infrared Activity)** A normal vibration that changes the electric dipole moment of the molecule, that is, with $(\partial\boldsymbol{p}/\partial Q)_0 \ne \boldsymbol{0}$ ($Q$ is the normal coordinate of the vibration), is **infrared active** and gives rise to infrared absorption; a vibration that leaves the dipole moment unchanged is **infrared inactive**.

The absorption intensity is proportional to $\lvert\partial\boldsymbol{p}/\partial Q\rvert^2$: highly polar bonds ($\ce{C=O}$, $\ce{O-H}$, $\ce{C-O}$, $\ce{Si-O}$) absorb very strongly, whereas nonpolar or highly symmetric bonds ($\ce{C=C}$, $\ce{C#C}$, $\ce{S-S}$) absorb weakly or not at all. The statement that "symmetric stretching vibrations are infrared inactive" does not hold in general: only vibrations that leave the dipole moment unchanged are inactive, such as the symmetric stretching of $\ce{CO2}$, whereas the symmetric stretching of $\ce{H2O}$ is infrared active.

The number of observed fundamental peaks is generally smaller than $3N - 6$, for several reasons: infrared-inactive vibrations give no peak; degenerate vibrations give a single peak; peaks of similar frequency overlap and cannot be resolved; some peaks are too weak; and some vibrations lie outside the range of the instrument (such as low-frequency vibrations of heavy atoms). On the other hand, overtones, combination bands and the like (11.1.6) add some peaks.

Absorption intensity is roughly classified into five grades by the **molar absorption coefficient** $\varepsilon$: $\varepsilon > 200\,\mathrm{L\,mol^{-1}\,cm^{-1}}$ is very strong (vs), $75$–$200$ strong (s), $25$–$75$ medium (m), $5$–$25$ weak (w), and $< 5$ very weak (vw); band shapes are further described as broad (br) or sharp (sh). Infrared absorption is much weaker than ultraviolet–visible absorption (for which $\varepsilon$ can reach $10^4$–$10^5$), which is one reason for the low sensitivity of infrared quantitation (11.4.1).

### 11.1.6. Bands Other Than Fundamentals

**Definition 11.1.4** The absorption arising from a transition from the vibrational ground state ($v = 0$) to the first excited state ($v = 1$) is called the **fundamental band**. The absorption arising from a transition to $v = 2, 3, \dots$ is called an **overtone**; its wavenumber is slightly less than an integral multiple of the fundamental. The absorption produced by the simultaneous excitation of two (or more) normal vibrations is called a **combination band**; its wavenumber is approximately the sum of the two fundamentals (a difference band corresponds to their difference and is generally very weak).

The intensities of overtones and combination bands are generally only $1/10$ to $1/1000$ of those of fundamentals; they are mostly weak peaks in the mid-infrared and are the principal source of near-infrared spectra (11.4.2). Substituted benzenes have a group of weak combination peaks at $2000$–$1650\,\mathrm{cm^{-1}}$ whose pattern varies with the substitution and can help to determine the substitution positions.

**Definition 11.1.5 (Vibrational Coupling)** The interaction of two oscillators in a molecule that have similar frequencies and a common atom (or are close together), which combines the original vibrations into an in-phase and an out-of-phase vibration whose frequencies split, one higher and one lower, is called **vibrational coupling**.

$\ce{CO2}$ is the simplest example. If the two $\ce{C=O}$ bonds did not influence each other, they would absorb near the same frequency; in fact they share the central carbon atom and are strongly coupled, splitting into the in-phase symmetric stretching (about $1333\,\mathrm{cm^{-1}}$, infrared inactive) and the out-of-phase antisymmetric stretching ($2349\,\mathrm{cm^{-1}}$). Note that the other peak in the infrared spectrum of $\ce{CO2}$, at $667\,\mathrm{cm^{-1}}$, is a bending vibration and has nothing to do with this coupling: coupling accounts for the splitting of the two stretching vibrations at $2349$ and $1333\,\mathrm{cm^{-1}}$. Other examples: the two $\ce{C=O}$ groups of an acid anhydride give a doublet at $1820$ and $1760\,\mathrm{cm^{-1}}$; $\ce{-CH3}$, $\ce{-CH2-}$, $\ce{-NH2}$ and $\ce{-NO2}$ all have symmetric and antisymmetric stretching vibrations; the $\ce{C-O}$ stretching vibrations of methanol, ethanol and 2-butanol are at $1034$, $1053$ and $1105\,\mathrm{cm^{-1}}$, respectively, the differences arising from different degrees of coupling between the $\ce{C-O}$ stretch and the neighboring $\ce{C-C}$ stretches. Coupling displaces the frequencies of some groups from their "standard" positions, which complicates the identification of functional groups; but precisely because coupling makes the low-frequency vibrations involve the whole molecular skeleton, infrared spectra can be used to confirm a specific compound (the fingerprint region, 11.2.1).

**Definition 11.1.6 (Fermi Resonance)** When the overtone or combination band of one vibration has a frequency close to that of another fundamental and the same symmetry, the two interact: their frequencies are pushed apart and the intensity is redistributed (an originally very weak overtone or combination band becomes stronger). This phenomenon is called **Fermi resonance**.

A typical example: the aldehyde $\ce{C-H}$ stretching vibration is in Fermi resonance with the overtone of its bending vibration (about $1390\,\mathrm{cm^{-1}}$), giving two medium-intensity peaks at $2820$ and $2720\,\mathrm{cm^{-1}}$; the $2720\,\mathrm{cm^{-1}}$ peak is rarely overlapped by other peaks and is characteristic of aldehydes. The symmetric stretching of $\ce{CO2}$ ($1333$) is in Fermi resonance with the overtone of the bending vibration ($2\times667$), which appears in the Raman spectrum as a doublet at $1285$ and $1388\,\mathrm{cm^{-1}}$.

## 11.2. Group Frequencies and Spectrum Interpretation

### 11.2.1. Group Frequencies, the Functional Group Region and the Fingerprint Region

The spectra of a large number of compounds show that a given functional group always absorbs at similar wavenumbers in different molecules. The reason is that the vibrational frequencies of hydrogen-containing groups (small $\mu$) and multiple bonds (large $k$) are far higher than those of the molecular skeleton, so their coupling to the skeleton is weak and the vibration is essentially localized in the group.

**Definition 11.2.1 (Group Frequency)** The absorption frequency of a group that always appears within a narrow range of wavenumbers in different molecules, essentially independent of the rest of the molecule, is called the **group frequency** (characteristic absorption frequency) of that group.

**Definition 11.2.2** The mid-infrared spectrum is divided by the nature of the absorption into two regions. The $4000$–$1300\,\mathrm{cm^{-1}}$ region is the **functional group region**: stretching vibrations of hydrogen-containing groups and of triple and double bonds appear here, with few peaks that are easy to assign, and it is used to decide which functional groups are present. Below $1300\,\mathrm{cm^{-1}}$ is the **fingerprint region**, comprising stretching vibrations of single bonds ($\ce{C-C}$, $\ce{C-O}$, $\ce{C-N}$) and the various bending vibrations; the frequencies are similar and strongly coupled, and the peaks are numerous and complex and mostly cannot be assigned one by one, but they differ from molecule to molecule, like a human fingerprint, and are used to confirm a compound by comparison with a reference spectrum.

Some books place the boundary between the two regions at $1500\,\mathrm{cm^{-1}}$. Note that the several vibrations of one group should appear together: a methyl group should absorb at $2960$, $2870$, $1460$ and $1375\,\mathrm{cm^{-1}}$, and a long methylene chain at $2925$, $2850$, $1465$ and $720\,\mathrm{cm^{-1}}$. The presence of a group can be concluded only when all these "correlation peaks" appear.

![Approximate ranges of the main group frequencies in the mid-infrared region: the functional group region (4000–1300 cm⁻¹) and the fingerprint region (below 1300 cm⁻¹); dotted lines roughly separate the X–H stretching, triple-bond and cumulated-double-bond, and double-bond sections](./plots/group-frequency-chart.py)

### 11.2.2. Table of Characteristic Absorption Frequencies

From high to low wavenumber, the mid-infrared region can be divided into six sections (intensity: s strong, m medium, w weak, br broad):

| Section / $\mathrm{cm^{-1}}$ | Group and vibration | Wavenumber / $\mathrm{cm^{-1}}$ | Remarks |
|---|---|---|---|
| (1) $4000$–$2500$: X–H stretching | $\ce{O-H}$ (free) | $3650$–$3590$ (m, sharp) | dilute solution or gas phase |
| | $\ce{O-H}$ (associated, alcohols, phenols) | $3550$–$3200$ (s, br) | hydrogen bonding broadens the peak and shifts it to lower frequency |
| | $\ce{O-H}$ (carboxylic acid dimer) | $3300$–$2500$ (s, very broad) | overlaps the $\ce{C-H}$ peaks |
| | $\ce{N-H}$ | $3500$–$3300$ (m) | primary amines and amides, two peaks ($\nu_{\mathrm{as}}$, $\nu_{\mathrm{s}}$); secondary, one; tertiary, none |
| | ≡C–H | about $3300$ (s, sharp) | terminal alkynes |
| | =C–H, aromatic $\ce{C-H}$ | $3100$–$3000$ (m) | $3000$ is the dividing line: $\ce{C-H}$ on unsaturated carbon lies above it |
| | saturated $\ce{C-H}$ | $2960$, $2925$, $2870$, $2850$ (s) | in order: $\nu_{\mathrm{as}}$ of $\ce{CH3}$, $\nu_{\mathrm{as}}$ of $\ce{CH2}$, $\nu_{\mathrm{s}}$ of $\ce{CH3}$, $\nu_{\mathrm{s}}$ of $\ce{CH2}$ |
| | aldehyde $\ce{C-H}$ | $2820$, $2720$ (m) | Fermi resonance doublet |
| | $\ce{S-H}$ | $2600$–$2550$ (w) | |
| (2) $2500$–$2000$: triple bonds and cumulated double bonds | $\ce{C#N}$ | $2260$–$2220$ (m, sharp) | |
| | $\ce{C#C}$ | $2260$–$2100$ (w) | symmetrically substituted internal alkynes may give no peak |
| | $\ce{C=C=C}$, $\ce{N=C=O}$, $\ce{O=C=O}$ | $1950$, $2270$, $2349$ | the rotation–vibration doublet of atmospheric $\ce{CO2}$ at $2360$/$2340$ must be removed by background subtraction |
| (3) $2000$–$1500$: double-bond stretching | $\ce{C=O}$ | $1850$–$1630$ (s) | see the table below |
| | $\ce{C=C}$ (alkene) | $1680$–$1620$ (m–w) | very weak when symmetrically substituted |
| | aromatic ring skeleton | $1600$, $1580$, $1500$, $1450$ (m) | the last three do not always all appear |
| | $\ce{N-H}$ bending, $\ce{C=N}$, $\ce{NO2}$ | $1650$–$1550$, $1690$–$1640$, $1550$ and $1350$ | |
| (4) $1500$–$1300$: $\ce{C-H}$ bending | $\ce{CH3}$ | $1460$ ($\delta_{\mathrm{as}}$), $1375$ ($\delta_{\mathrm{s}}$) | splitting of $1375$ into a $1385$/$1365$ doublet indicates a gem-dimethyl (isopropyl) group |
| | $\ce{CH2}$ scissoring | $1465$ | |
| (5) $1300$–$910$: single-bond stretching and skeletal vibrations | $\ce{C-O}$ | $1300$–$1000$ (s) | primary alcohols about $1050$, secondary about $1100$, tertiary about $1150$; esters have strong peaks at $1300$–$1150$ |
| | $\ce{C-N}$ | $1250$–$1020$ (aliphatic amines), $1340$–$1250$ (aromatic amines) | |
| | $\ce{C-F}$ | $1400$–$1000$ (s) | |
| (6) below $910$ | alkene =C–H out-of-plane bending | monosubstituted $990$ and $910$, trans-disubstituted $970$, gem-disubstituted $890$, cis about $700$ | determines the substitution pattern of the double bond |
| | aromatic $\ce{C-H}$ out-of-plane bending | monosubstituted $770$–$730$ and $710$–$690$, ortho $770$–$735$, meta $810$–$750$ and $710$–$690$, para $860$–$800$ | determines the substitution pattern of the benzene ring |
| | $(\ce{CH2})_n$ in-plane rocking ($n \ge 4$) | $720$ | indicates a long chain |
| | $\ce{C-Cl}$, $\ce{C-Br}$ | $800$–$600$, $600$–$500$ | |

The carbonyl stretching vibration gives one of the strongest and most useful bands in an infrared spectrum, and its position is sensitive to the attached groups:

| Compound type | $\tilde\nu(\ce{C=O})$ / $\mathrm{cm^{-1}}$ | Compound type | $\tilde\nu(\ce{C=O})$ / $\mathrm{cm^{-1}}$ |
|---|---|---|---|
| acid anhydride | $1820$ and $1760$ (doublet) | aliphatic ketone | $1715$ |
| acyl fluoride, acyl chloride | about $1870$, $1815$–$1785$ | carboxylic acid (monomer / dimer) | about $1760$ / $1710$ |
| ester | $1750$–$1735$ | $\alpha,\beta$-unsaturated ketone, aryl ketone | $1685$–$1665$ |
| aldehyde | $1740$–$1720$ | amide | $1690$–$1630$ |
| | | carboxylate | about $1600$ and $1400$ ($\nu_{\mathrm{as}}$, $\nu_{\mathrm{s}}$) |

The two values for the carboxylic acid $\ce{C=O}$ must be distinguished: about $1760\,\mathrm{cm^{-1}}$ is the value of the free monomer (gas phase or very dilute solution), whereas carboxylic acids in the pure liquid and in the solid exist as hydrogen-bonded dimers, for which $\ce{C=O}$ moves to about $1710\,\mathrm{cm^{-1}}$.

### 11.2.3. Factors Influencing Group Frequencies

Group frequencies shift with electronic effects within the molecule and with intermolecular interactions. The direction of the shift can be understood from Eq. (11.1): any factor that increases the bond order (the force constant) raises the frequency.

1. Inductive effect: an electronegative atom or group attached to the carbonyl carbon withdraws electrons, reduces the contribution of the polar structure $\ce{C^+-O^-}$ of $\ce{C=O}$, enhances the double-bond character and raises the frequency. The $\ce{C=O}$ bands of acetone, acetyl chloride and acetyl fluoride lie at $1715$, about $1806$ and about $1869\,\mathrm{cm^{-1}}$, respectively (the structures of the three are shown below in that order).

```smiles
CC(C)=O
CC(Cl)=O
CC(F)=O
```

2. Resonance effect: a lone pair on the substituent conjugates with the carbonyl group, gives $\ce{C=O}$ some single-bond character and lowers the frequency. In an amide the lone pair of nitrogen is delocalized onto the carbonyl ($\ce{R-C(=O)-NH2 <-> R-C(-O^-)=NH2+}$), and $\ce{C=O}$ drops to $1690$–$1630\,\mathrm{cm^{-1}}$. The alkoxy group of an ester has both an electron-withdrawing inductive effect and an electron-donating resonance effect; the inductive effect dominates, and the $\ce{C=O}$ of an ester is higher than that of a ketone.
3. Conjugation effect: when $\ce{C=O}$ is conjugated with $\ce{C=C}$ or an aromatic ring, $\pi$-electron delocalization weakens the double-bond character and lowers the frequency by $20$–$40\,\mathrm{cm^{-1}}$: aliphatic ketones $1715$, $\alpha,\beta$-unsaturated ketones about $1675$, acetophenone about $1685\,\mathrm{cm^{-1}}$.
4. **Hydrogen bonding**: formation of a hydrogen bond weakens the $\ce{X-H}$ bond, shifts the stretching vibration to lower frequency and makes the band markedly broader and stronger. The free $\ce{O-H}$ of an alcohol gives a sharp peak at about $3620\,\mathrm{cm^{-1}}$, the associated $\ce{O-H}$ a broad peak at $3400$–$3200\,\mathrm{cm^{-1}}$. Intermolecular hydrogen bonds weaken as the concentration decreases (on dilution with $\ce{CCl4}$ the broad peak weakens and the sharp peak strengthens), whereas intramolecular hydrogen bonds are independent of concentration, which allows the two to be distinguished. A $\ce{C=O}$ that accepts a hydrogen bond also moves to lower frequency (carboxylic acid dimers).
5. Ring strain: the smaller the ring, the higher the frequency of an exocyclic double bond (such as the $\ce{C=O}$ of a cyclic ketone: cyclohexanone $1715$, cyclopentanone $1745$, cyclobutanone $1780\,\mathrm{cm^{-1}}$) and the lower the frequency of an endocyclic double bond (cyclohexene $1646$, cyclopentene $1611$, cyclobutene $1566\,\mathrm{cm^{-1}}$).
6. Physical state and solvent: gas-phase molecules interact least and have the highest frequencies, and may show rotational fine structure; polar solvents lower the frequencies of polar groups. The physical state and the sampling method should be stated with the spectrum of any compound.

### 11.2.4. Degree of Unsaturation and Spectrum Interpretation

**Definition 11.2.3 (Degree of Unsaturation)** The quantity calculated from the molecular formula,

$$
U = 1 + n_4 + \frac{n_3 - n_1}{2}
\tag{11.4}
$$
is called the **degree of unsaturation**, where $n_4$, $n_3$ and $n_1$ are the numbers of tetravalent (C, Si), trivalent (N, P) and monovalent (H, halogen) atoms, respectively; divalent atoms (O, S) are not counted.

A double bond or a ring contributes 1 to the degree of unsaturation, a triple bond 2, and a benzene ring 4 (three double bonds and one ring): for benzene $\ce{C6H6}$, $U = 1 + 6 - 6/2 = 4$. When $U \ge 4$, a benzene ring should be considered.

The general procedure for interpreting an infrared spectrum is the following.

1. Obtain the molecular formula from elemental analysis ([6.4.13](/6.4.13#sec-13.6.4)) and mass spectrometry ([6.4.15](/6.4.15#sec-15.4.2)) and calculate the degree of unsaturation.
2. Examine the functional group region first, find the few strongest peaks and decide which functional groups are present (the presence or absence of $\ce{O-H}$/$\ce{N-H}$, $\ce{C=O}$, $\ce{C=C}$, aromatic rings, and $\ce{C-H}$ on either side of $3000\,\mathrm{cm^{-1}}$), confirming with correlation peaks.
3. Then examine the fingerprint region to determine the substitution pattern (out-of-plane bending of alkenes and benzene rings) and other details.
4. Assemble the possible structures that are chemically reasonable, compare them with reference spectra (the Sadtler collections, databases such as SDBS), and confirm in combination with nuclear magnetic resonance and mass spectrometry.

**Example 11.2.1** A compound of molecular formula $\ce{C12H24}$ has the main infrared peaks $3077$ (m), $2925$, $2855$ (s), $1640$ (m), $1465$ (m), $991$, $909$ (s) and $721\,\mathrm{cm^{-1}}$ (w). Deduce its structure.

**Solution** $U = 1 + 12 - 24/2 = 1$, so there is one double bond or one ring. The $3077\,\mathrm{cm^{-1}}$ band (above $3000$) is =C–H stretching and the $1640\,\mathrm{cm^{-1}}$ band is $\ce{C=C}$ stretching, so the compound is an alkene and the degree of unsaturation is used up. The bands at $2925$ and $2855\,\mathrm{cm^{-1}}$ are very strong while that at $2960\,\mathrm{cm^{-1}}$ is inconspicuous, so $\ce{CH2}$ groups greatly outnumber $\ce{CH3}$; the $1465\,\mathrm{cm^{-1}}$ band is $\ce{CH2}$ scissoring, and the $721\,\mathrm{cm^{-1}}$ band shows that four or more $\ce{CH2}$ groups are connected. The two strong bands at $991$ and $909\,\mathrm{cm^{-1}}$ are the out-of-plane bending of a monosubstituted alkene $\ce{RCH=CH2}$. The structure is 1-dodecene $\ce{CH2=CH(CH2)9CH3}$:

```smiles
C=CCCCCCCCCCC
```

**Example 11.2.2** A compound of molecular formula $\ce{C12H24O2}$ has a strong, broad absorption at $3300$–$2500\,\mathrm{cm^{-1}}$ on which sharp peaks at $2955$, $2920$ and $2850\,\mathrm{cm^{-1}}$ are superimposed, and further peaks at $1705$ (vs), $1465$, $1410$, $1300$–$1200$ (several peaks), $940$ (br) and $720\,\mathrm{cm^{-1}}$. Deduce its structure.

**Solution** $U = 1 + 12 - 24/2 = 1$. The very strong peak at $1705\,\mathrm{cm^{-1}}$ is $\ce{C=O}$ and uses up the whole degree of unsaturation. The strong, broad absorption at $3300$–$2500\,\mathrm{cm^{-1}}$, extending down to $2500\,\mathrm{cm^{-1}}$, is the associated $\ce{O-H}$ of a carboxylic acid dimer, and together with the $1705\,\mathrm{cm^{-1}}$ band (the $\ce{C=O}$ of the dimer) shows that the compound is a carboxylic acid. The bands at $2920$ and $2850\,\mathrm{cm^{-1}}$ are much stronger than that at $2955\,\mathrm{cm^{-1}}$, and the $720\,\mathrm{cm^{-1}}$ band shows a long methylene chain. The remaining peaks are assigned as follows: $1465\,\mathrm{cm^{-1}}$ is $\ce{CH2}$ scissoring (with a contribution from $\ce{CH3}$), $1410\,\mathrm{cm^{-1}}$ is the in-plane $\ce{C-O-H}$ bending, $1300$–$1200\,\mathrm{cm^{-1}}$ is $\ce{C-O}$ stretching (coupled with $\ce{O-H}$ bending), and the broad $940\,\mathrm{cm^{-1}}$ band is the out-of-plane $\ce{O-H}$ bending of the dimer, also characteristic of carboxylic acids. The structure is lauric acid (dodecanoic acid) $\ce{CH3(CH2)10COOH}$:

```smiles
CCCCCCCCCCCC(=O)O
```

### 11.2.5. Infrared Spectra of Biological Macromolecules

The infrared spectrum of a protein is dominated by several characteristic vibrations of the peptide bond $\ce{-CO-NH-}$, called the amide bands:

| Band | Wavenumber / $\mathrm{cm^{-1}}$ | Main origin |
|---|---|---|
| Amide A | about $3300$ | $\ce{N-H}$ stretching |
| Amide I | $1700$–$1600$ | $\ce{C=O}$ stretching (about 80%) |
| Amide II | about $1550$ | coupling of in-plane $\ce{N-H}$ bending and $\ce{C-N}$ stretching |
| Amide III | $1320$–$1220$ | $\ce{C-N}$ stretching and $\ce{N-H}$ bending, weaker |

The amide I band is the most sensitive to secondary structure: the $\ce{C=O}$ oscillators of the individual peptide bonds are coupled to each other through hydrogen bonds and transition dipole interactions (the vibrational coupling of 11.1.6), and the manner of coupling depends on the geometric arrangement of the backbone. In general, $\alpha$-helices absorb at $1658$–$1648\,\mathrm{cm^{-1}}$, $\beta$-sheets at $1640$–$1620\,\mathrm{cm^{-1}}$ (antiparallel $\beta$-sheets have an additional weak peak at about $1685\,\mathrm{cm^{-1}}$), random coils at about $1645\,\mathrm{cm^{-1}}$ and turns at $1685$–$1660\,\mathrm{cm^{-1}}$; the intermolecular $\beta$-sheets of amyloid fibrils give a low-frequency peak at $1630$–$1610\,\mathrm{cm^{-1}}$. The bands of the components are broad and overlapping, and the actual amide I band is a single asymmetric broad peak; resolving it by second derivatives or Fourier self-deconvolution and fitting the areas of the components allows the secondary structure content to be estimated.

The bending vibration of water at $1645\,\mathrm{cm^{-1}}$ overlaps the amide I band, so protein solutions are often measured in $\ce{D2O}$ (the bending vibration of $\ce{D2O}$ moves to about $1210\,\mathrm{cm^{-1}}$, and the amide II band after deuterium exchange, called II′, moves to about $1450\,\mathrm{cm^{-1}}$), or in $\ce{H2O}$ using a very thin sample cell or attenuated total reflection (11.3.4). Compared with **circular dichroism** ([6.4.9](/6.4.9#sec-9.6.5)), infrared spectroscopy is more sensitive to $\beta$-sheets and can measure turbid samples, membrane proteins and solid aggregates; the two often confirm each other.

![The amide I band of two proteins (synthetic examples): left, a protein dominated by α-helix; right, a protein dominated by β-sheet; in the upper panels the black line is the sum of the components (colored); in the lower panels the negative second derivative separates the overlapping components](./plots/amide-i-band.py)

Other biomolecules: the symmetric $\ce{CH2}$ stretching vibration of lipids (about $2850\,\mathrm{cm^{-1}}$) rises by $2$–$4\,\mathrm{cm^{-1}}$ when a membrane changes from the gel phase to the liquid-crystalline phase and is used to study membrane fluidity; the phosphodiester groups of nucleic acids have strong peaks at about $1230$ and $1090\,\mathrm{cm^{-1}}$ (the antisymmetric and symmetric stretching of $\ce{PO2-}$) and the double bonds of the bases absorb at $1700$–$1600\,\mathrm{cm^{-1}}$; the $\ce{C-O}$ and $\ce{C-C}$ stretching vibrations of carbohydrates are concentrated at $1200$–$900\,\mathrm{cm^{-1}}$. The infrared spectrum of a cell or tissue is the superposition of these components, and cell types and diseased tissue can be distinguished without staining (11.3.4).

## 11.3. Infrared Spectrometers

### 11.3.1. Dispersive Infrared Spectrophotometers

Early infrared spectrometers have the same structure as ultraviolet–visible spectrophotometers ([6.4.7](/6.4.7#sec-7.1.3)), consisting of a source, a cell, a monochromator and a detector; most are of the double-beam type and disperse with a prism ($\ce{NaCl}$, $\ce{KBr}$) or a grating:

- Source: the Nernst glower (a rod sintered from rare-earth oxides such as $\ce{ZrO2}$ and $\ce{Y2O3}$, nonconducting at room temperature, conducting after being preheated to about $700\,^\circ\mathrm{C}$, and operating at about $1700\,^\circ\mathrm{C}$), the silicon carbide rod (Globar, about $1300\,^\circ\mathrm{C}$) and the nichrome wire are all continuous sources close to a **black body**, and their radiation in the mid-infrared is weak.
- Detector: thermal detectors (thermocouples, bolometers, pyroelectric detectors) respond at all wavelengths and need no cooling but are slow; photon detectors (**semiconductors** such as $\ce{InSb}$, $\ce{PbSe}$ and $\ce{HgCdTe}$) are much more sensitive but need liquid-nitrogen cooling.
- Optical materials: glass and quartz absorb infrared light, so windows and cells are made of crystals such as $\ce{NaCl}$, $\ce{KBr}$, $\ce{CaF2}$ and $\ce{ZnSe}$; the alkali halides absorb moisture easily, so the working environment must be dry.

Because both the source and the detector perform poorly, the slits cannot be too narrow if sufficient energy is to be obtained, which limits the resolution and the signal-to-noise ratio, and scanning a spectrum takes several minutes. Dispersive instruments have now been almost entirely replaced by Fourier-transform infrared spectrometers and survive only in a few dedicated instruments.

### 11.3.2. Fourier-Transform Infrared Spectrometers

**Definition 11.3.1 (Fourier-Transform Infrared Spectroscopy)** The method in which an interferometer replaces the monochromator, the light intensity is recorded as a function of the optical path difference, and the infrared spectrum is obtained from it by a Fourier transform in a computer is called **Fourier-transform infrared spectroscopy** (FTIR).

The heart of FTIR is the **Michelson interferometer** ([5.4.1](/5.4.1#sec-1.8)): the light from the source is divided into two beams by a beam splitter (in the mid-infrared usually a germanium-coated $\ce{KBr}$ plate), the beams are reflected by a fixed mirror and a moving mirror, recombine and produce **interference**, and then pass through the sample to the detector. When the moving mirror is displaced by $x$, the optical path difference of the two beams is $\delta = 2x$. For monochromatic light of wavenumber $\tilde\nu$, the detector signal varies cosinusoidally with $\delta$,

$$
I(\delta) = \frac{1}{2}B(\tilde\nu)\big[1 + \cos(2\pi\tilde\nu\delta)\big],
$$
where $B(\tilde\nu)$ is the spectral intensity of the source (after passing the sample). The constant term carries no spectral information and is discarded, leaving only the modulated part. When the moving mirror travels at a uniform velocity $v_{\mathrm{m}}$, light of wavenumber $\tilde\nu$ is modulated into an alternating signal of frequency $f = 2v_{\mathrm{m}}\tilde\nu$: for $v_{\mathrm{m}} = 0.16\,\mathrm{cm\,s^{-1}}$, light of $1000\,\mathrm{cm^{-1}}$ corresponds to $320\,\mathrm{Hz}$, in the audio range, which the detector can follow easily. All wavenumbers of a continuous source are present at once, and the detector measures their superposition:

**Definition 11.3.2 (Interferogram)** The variation of the modulated part of the detector signal with the optical path difference,

$$
I(\delta) = \int_0^{\infty} B(\tilde\nu)\cos(2\pi\tilde\nu\delta)\,\mathrm{d}\tilde\nu
\tag{11.5}
$$
is called the **interferogram** (constant factors omitted).

Eq. (11.5) shows that the interferogram is the cosine **Fourier transform** ([2.5.6](/2.5.6#def-6.2.1)) of the spectrum, and its inverse transform gives the spectrum:

$$
B(\tilde\nu) = 2\int_{-\infty}^{\infty} I(\delta)\cos(2\pi\tilde\nu\delta)\,\mathrm{d}\delta.
\tag{11.6}
$$
In practice the interferogram is a finite sequence sampled at discrete path differences, and the transform is computed with the **fast Fourier transform** ([4.4.4](/4.4.4#sec-4.7)). At zero path difference all wavenumbers interfere constructively, and the interferogram has a sharp "center burst"; away from zero the cosines of the different wavenumbers fall out of phase and the signal decays rapidly into small fluctuations.

![Interferogram of a Michelson interferometer (left) and the spectrum recovered with the fast Fourier transform (right): monochromatic light gives a cosine, two spectral lines give beats, and a broadband source gives a center burst at zero path difference; the information on the two absorption bands in the spectrum is spread over the whole interferogram](./plots/ftir-interferogram.py)

Several important relations of FTIR follow from Fourier analysis:

- Resolution: when the maximum path difference of the moving mirror is $\Delta$, the smallest resolvable wavenumber difference is about $\Delta\tilde\nu \approx 1/\Delta$. A resolution of $2\,\mathrm{cm^{-1}}$ requires $\Delta = 0.5\,\mathrm{cm}$, and a gas-phase spectrum at $0.1\,\mathrm{cm^{-1}}$ requires $10\,\mathrm{cm}$. Truncation of the interferogram at $\Delta$ gives the spectral lines side lobes in the shape of a $\mathrm{sinc}$ function; multiplying by a weighting function that tends to zero at the two ends before transformation (apodization) suppresses the side lobes at the cost of slightly broader lines.
- Sampling: a He–Ne laser ($632.8\,\mathrm{nm}$) sharing the optical path of the interferometer also produces interference fringes, and the instrument samples at each zero crossing of the laser fringes, so that the sampling interval is exactly an optical path difference of $\lambda_{\mathrm{HeNe}}/2 = 316.4\,\mathrm{nm}$. By the sampling theorem, the highest wavenumber that can be measured without aliasing is $1/\lambda_{\mathrm{HeNe}} = 15803\,\mathrm{cm^{-1}}$, which covers the entire mid- and near-infrared.
- Wavenumber accuracy: because the path difference is referenced to the laser wavelength, the wavenumber scale of each measurement is accurate to the order of $0.01\,\mathrm{cm^{-1}}$, which facilitates spectral subtraction and library searching (the Connes advantage).

Compared with dispersive instruments, FTIR has two further fundamental advantages:

- The multiplex advantage (Fellgett advantage): all wavenumbers reach the detector simultaneously, so for the same measurement time the integration time for each wavenumber is $M$ times that of a dispersive instrument ($M$ is the number of spectral resolution elements). The noise of infrared detectors is independent of the signal (detector-noise-limited), so the signal-to-noise ratio is improved by a factor of about $\sqrt{M}$; conversely, to reach the same signal-to-noise ratio, a complete spectrum needs less than a second. In the ultraviolet–visible region the noise of photomultiplier tubes is dominated by shot noise ([6.4.7](/6.4.7#sec-7.5.4)), which increases with the total light intensity, and this advantage disappears; the Fourier-transform method is therefore used mainly in the infrared.
- The throughput advantage (Jacquinot advantage): an interferometer needs no slit and can use a large circular aperture, so that the light flux reaching the detector is higher by one to two orders of magnitude.

FTIR is a single-beam instrument: the background single-beam spectrum $B_0(\tilde\nu)$ without a sample is measured first, then the sample spectrum $B(\tilde\nu)$, and their ratio is the transmittance $\tau(\tilde\nu) = B/B_0$, which also removes the responses of the source, beam splitter and detector and the absorption of atmospheric $\ce{H2O}$ and $\ce{CO2}$ (provided the atmosphere does not change between the two measurements; the optical path is often purged with dry air or nitrogen). The commonly used detectors are DTGS (deuterated triglycine sulfate pyroelectric detector), which operates at room temperature, and MCT ($\ce{HgCdTe}$ photoconductive detector), which is cooled with liquid nitrogen, sensitive and fast, and used for rapid scanning, infrared microscopy and hyphenation with chromatography. The speed of FTIR allows its use as a detector for gas chromatography (GC-IR) and the tracking of reactions on millisecond to second time scales (rapid-scan and step-scan techniques).

### 11.3.3. Sample Preparation for Transmission Measurements

- Solids: in the pellet method, $1$–$2\,\mathrm{mg}$ of sample is ground with about $200\,\mathrm{mg}$ of dry $\ce{KBr}$ and pressed under vacuum into a transparent disk. In the mull method (Nujol), the sample is ground with paraffin oil into a paste sandwiched between two salt plates; the paraffin oil itself absorbs in the $\ce{C-H}$ region (perfluorokerosene can be used to measure that region). In the film method, a solution is evaporated on a salt plate to form a film, which suits polymers. $\ce{KBr}$ readily absorbs water, and the water peaks at $3400$ and $1640\,\mathrm{cm^{-1}}$ are common interferences.
- Liquids: a pure liquid is sandwiched between two salt plates as a liquid film or filled into a liquid cell $0.01$–$1\,\mathrm{mm}$ thick; solutions commonly use $\ce{CCl4}$ and $\ce{CS2}$ as solvents (they are transparent in different regions and complement each other).
- Gases: a gas cell with a $10\,\mathrm{cm}$ path; for trace gases, multiple-reflection long-path cells (path lengths up to tens of meters).
- Aqueous solutions: water absorbs very strongly at $3400$ and $1640\,\mathrm{cm^{-1}}$, so transmission measurements need $\ce{CaF2}$ windows and a cell only a few micrometers thick; attenuated total reflection (11.3.4) is more convenient.

The thickness of a cell can be found from the interference fringes of the empty cell. Light is reflected repeatedly between the two window surfaces in the cell, and the transmitted intensity fluctuates periodically with wavenumber; adjacent transmission maxima satisfy $2nb\tilde\nu = m$ ($m$ an integer, $n$ the refractive index of the medium in the cell, $n = 1$ for an empty cell), so if $N$ fringes are counted between $\tilde\nu_1$ and $\tilde\nu_2$,

$$
b = \frac{N}{2n(\tilde\nu_1 - \tilde\nu_2)}.
\tag{11.7}
$$
For example, an empty cell with $10$ fringes between $2000$ and $1000\,\mathrm{cm^{-1}}$ has $b = 10/(2\times1000\,\mathrm{cm^{-1}}) = 5.0\times10^{-3}\,\mathrm{cm} = 50\,\mu\mathrm{m}$.

### 11.3.4. Attenuated Total Reflection and Other Reflection Techniques

**Definition 11.3.3 (Attenuated Total Reflection)** When infrared light inside a crystal of refractive index $n_1$ strikes the interface between the crystal and the sample (refractive index $n_2 < n_1$) at an angle of incidence greater than the critical angle, it is totally reflected, but an evanescent wave that decays exponentially along the normal still enters the sample; the sample absorbs energy from the evanescent wave and the reflected light is attenuated at the absorbing wavenumbers. The method of measuring this attenuated reflection spectrum is called **attenuated total reflection** (ATR).

The distance over which the electric-field amplitude of the evanescent wave decays to $1/\mathrm{e}$ of its value at the interface is called the penetration depth:

$$
d_{\mathrm{p}} = \frac{\lambda_1}{2\pi\sqrt{\sin^2\alpha - (n_2/n_1)^2}},
\tag{11.8}
$$
where $\alpha$ is the angle of incidence and $\lambda_1 = \lambda/n_1$ is the wavelength of the light in the crystal. The condition $\sin\alpha > n_2/n_1$ is the condition for **total internal reflection** ([5.1.7](/5.1.7#sec-7.6.3)). For example, for a diamond crystal ($n_1 = 2.4$), an organic sample ($n_2 = 1.5$) and $\alpha = 45^\circ$, $d_{\mathrm{p}} \approx 2.0\,\mu\mathrm{m}$ at $1000\,\mathrm{cm^{-1}}$ ($\lambda = 10\,\mu\mathrm{m}$); with a germanium crystal ($n_1 = 4.0$) it is only $0.66\,\mu\mathrm{m}$. Because $d_{\mathrm{p}} \propto \lambda$, peaks at low wavenumbers are relatively stronger in an ATR spectrum than in a transmission spectrum, and a correction is needed when comparing with transmission spectra.

ATR probes only a layer about $0.5$–$5\,\mu\mathrm{m}$ thick at the surface of the sample and needs almost no sample preparation: a solid is pressed against the crystal or a liquid dropped on the crystal and measured, and powders, rubbers, fibers, coatings and aqueous solutions are all suitable. The effective path length in an aqueous solution is only a few micrometers, and the absorption of water does not saturate, so ATR is the common method for protein solutions, biological membranes and living cells (11.2.5). ATR has now become the most common sampling mode in FTIR.

Other reflection techniques:

- Diffuse reflectance (DRIFTS): light striking a loose powder is partly specularly reflected at the particle surfaces, and the rest enters the powder and, after repeated refraction, scattering and absorption between the particles, emerges diffusely from the surface; this light carries the absorption information. The diffusely reflected light is collected with an integrating sphere or an ellipsoidal mirror, and the Kubelka–Munk function $f(R_\infty) = (1 - R_\infty)^2/(2R_\infty)$ ($R_\infty$ is the reflectance of an infinitely thick sample) replaces the absorbance. The technique is used for powders, catalysts (which can be measured in situ at high temperature and in a reaction atmosphere) and near-infrared analysis.
- Photoacoustic spectroscopy: the sample absorbs modulated infrared light and heats, causing periodic expansion of the gas in a closed cell; the resulting sound wave is detected with a microphone (the principle is that of the photoacoustic spectroscopy in [6.4.9](/6.4.9#sec-9.5.5)). It suits strongly absorbing, opaque samples that are difficult to prepare, such as coal, carbon black and rubber.
- Infrared microscopy and imaging: an infrared microscope focuses the light onto a region of a few to tens of micrometers, and with a focal-plane array detector gives chemical images with one spectrum per pixel, used for the compositional distribution in tissue pathology, polymers and tablets. The spatial resolution is diffraction-limited, of the order of the wavelength (a few micrometers); nanoscale infrared spectroscopy based on an atomic force microscope probe (AFM-IR) can overcome this limit.

## 11.4. Quantitative Analysis and Near-Infrared Spectroscopy

### 11.4.1. Infrared Quantitative Analysis

Infrared quantitation likewise rests on the **Beer–Lambert law** $A = \varepsilon bc$ ([6.4.9](/6.4.9#sec-9.3.1)). An absorption peak free of interference is selected and the **absorbance** is measured by the baseline method: a tangent to the spectrum on both sides of the peak is drawn as the baseline, the baseline transmittance $\tau_0$ and the peak transmittance $\tau$ at the peak maximum are read, and $A = \lg(\tau_0/\tau)$; a **calibration curve** is then prepared with standards ([6.4.1](/6.4.1#sec-1.8.1)). For several components, measurements are made at several wavenumbers and simultaneous equations are solved.

Compared with ultraviolet–visible spectrophotometry, the accuracy and sensitivity of infrared quantitation are poorer: the source is weak and the detector noise large; the spectral bandwidth of a dispersive instrument is comparable to the width of infrared absorption peaks, causing deviations from the absorption law; $\varepsilon$ is small, and to prevent saturation of strong peaks only very short path lengths can be used, so the sensitivity is low; and there are many absorption peaks, so it is difficult to find a peak free of interference. Infrared spectroscopy is therefore used mainly for qualitative analysis. The situation has improved with the spread of FTIR, and infrared quantitation has become routine in some fields: gas analysis ($\ce{CO}$, $\ce{CO2}$, $\ce{CH4}$, $\ce{N2O}$ and others, measured in air and flue gas with long-path-cell FTIR gas analyzers), additives and copolymer composition in polymers, and water and additives in petroleum products.

### 11.4.2. Near-Infrared Spectroscopy

**Definition 11.4.1 (Near-Infrared Spectroscopy)** The analytical method that uses absorption or diffuse reflectance in the wavelength region $780$–$2500\,\mathrm{nm}$ ($12800$–$4000\,\mathrm{cm^{-1}}$) is called **near-infrared spectroscopy** (NIR). The absorption in this region consists mainly of overtones and combinations of the stretching vibrations of hydrogen-containing $\ce{X-H}$ groups ($\ce{X} = \ce{C}$, $\ce{N}$, $\ce{O}$, $\ce{S}$).

The $\ce{X-H}$ bond has a small reduced mass and a large anharmonicity, so its overtones and combinations are much stronger than those of other groups, and near-infrared spectra reflect almost exclusively hydrogen-containing groups; examples are the $\ce{O-H}$ combination band (about $1940\,\mathrm{nm}$) and first overtone (about $1450\,\mathrm{nm}$) of water in cereals. The intensity is only $1/10$ to $1/1000$ of that of a mid-infrared fundamental, each successive overtone is weaker by about another order of magnitude, and the optical path of the sample cell is lengthened correspondingly. Taking the $\ce{C-H}$ stretching vibration as an example:

| Band | Wavelength / $\mathrm{nm}$ | Relative intensity (order of magnitude) | Suitable path length |
|---|---|---|---|
| fundamental | $3380$–$3510$ | $1$ | $0.1$–$4\,\mathrm{mm}$ |
| first overtone | $1690$–$1755$ | $10^{-2}$ | $0.1$–$2\,\mathrm{cm}$ |
| second overtone | $1127$–$1170$ | $10^{-3}$ | $0.5$–$5\,\mathrm{cm}$ |
| third overtone | $845$–$875$ | $10^{-4}$ | $5$–$10\,\mathrm{cm}$ |

The corresponding bands of $\ce{O-H}$ lie at shorter wavelengths: the fundamental of free $\ce{O-H}$ is at about $2.7$–$2.8\,\mu\mathrm{m}$ (about $3600\,\mathrm{cm^{-1}}$) and its first overtone at about $1.4\,\mu\mathrm{m}$.

Weak absorption seems a disadvantage but is an advantage in near-infrared analysis: samples need no dilution and path lengths of centimeters can be used; short-wavelength near-infrared light penetrates solids to a depth of several centimeters and can measure through glass bottles and packaging, or on the production line, online and nondestructively, with fiber-optic probes. A near-infrared instrument consists of a tungsten–halogen lamp, a grating (or interferometer, or acousto-optic tunable filter) and a $\ce{Si}$ ($< 1100\,\mathrm{nm}$) or $\ce{InGaAs}$ or $\ce{PbS}$ detector; it is simple and robust and suits field and online analysis.

### 11.4.3. Multivariate Calibration and Applications

Near-infrared bands are broad and overlapping, and the information on one component is spread over many wavelengths, so a single-wavelength calibration curve does not work and chemometric multivariate calibration is needed. The spectra of $n$ standard samples at $p$ wavelengths ($p$ often several hundred to over a thousand) are arranged in a matrix $X$ ($n\times p$), the contents determined by a reference method (such as Kjeldahl nitrogen determination or drying and weighing) form a vector $\boldsymbol{y}$, and a regression model of $\boldsymbol{y}$ on $X$ is built. Since $p > n$ and the wavelengths are highly collinear, ordinary **least squares** cannot be used, and two dimension-reducing regressions are common:

- **Principal component regression** ([3.4.7](/3.4.7)): principal component analysis of $X$ is performed first, and the first few principal components replace the original variables in the regression.
- *Partial least squares regression*, abbreviated PLS: the extracted latent variables must both explain the variance of $X$ and correlate strongly with $\boldsymbol{y}$, so that the same prediction accuracy is usually reached with fewer components than in principal component regression; it is the method most used in near-infrared analysis.

The number of latent variables is determined by **cross-validation** ([3.4.10](/3.4.10)), and the predictive ability of the model must also be tested with an independent set of validation samples. A finished model applies only to samples similar to the calibration samples, and must be updated or transferred when the sample type or the instrument changes.

The International Council for Near Infrared Spectroscopy was founded in 1988 and the *Journal of Near Infrared Spectroscopy* began publication in 1993. Typical applications are the following.

- Agriculture and food: moisture, protein, fat and starch in grain and feed (several parameters are given by a single measurement in a few tens of seconds, replacing time-consuming chemical analysis), and the sugar content and ripeness of fruit.
- Pharmaceuticals: identification of raw materials and online monitoring of blend uniformity and tablet content; it is one of the core tools of process analytical technology (PAT).
- Petrochemicals and polymers: octane number of gasoline, polymer composition and reaction progress.

The "near-infrared spectroscopy" of medicine (cerebral oxygenation monitoring) measures the electronic absorption of hemoglobin at $650$–$950\,\mathrm{nm}$, not vibrational absorption; it exploits the property that biological tissue absorbs least in this "optical window", where light can penetrate several centimeters.

## 11.5. Raman Spectroscopy

### 11.5.1. Raman Scattering

In 1928 Raman and Krishnan observed weak spectral lines of frequency different from that of the incident light in light scattered by liquids (in the same year Landsberg and Mandelstam independently observed the same phenomenon in quartz crystals), and Raman received the Nobel Prize in Physics in 1930.

**Definition 11.5.1 (Raman Scattering)** The scattering in which a photon collides inelastically with a molecule, so that the frequency of the scattered light differs from that of the incident light by a vibrational (or rotational) frequency of the molecule, is called **Raman scattering**.

In contrast, elastic scattering, in which the scattered light has the same frequency as the incident light, is **Rayleigh scattering** ([5.4.3](/5.4.3#sec-3.4.2)). The scattering process can be viewed as the molecule absorbing an incident photon and making a transition to a "virtual state" of very short lifetime (not an eigenstate of the molecule), and then emitting a photon and returning to some vibrational level. Return to the original level is Rayleigh scattering; return to a level one vibrational quantum higher gives a scattered photon that has lost one vibrational quantum; a molecule in $v = 1$ that returns to $v = 0$ after scattering gives a scattered photon that has gained one vibrational quantum.

**Definition 11.5.2** The Raman line of frequency $\nu_0 - \nu_{\mathrm{vib}}$, lower than the frequency $\nu_0$ of the incident light, is called the **Stokes line**; the line of frequency $\nu_0 + \nu_{\mathrm{vib}}$ is called the **anti-Stokes line**.

**Definition 11.5.3 (Raman Shift)** The wavenumber difference $\Delta\tilde\nu = \tilde\nu_0 - \tilde\nu_{\mathrm{s}}$ between the incident and scattered light is called the **Raman shift**; it is positive for Stokes lines and negative for anti-Stokes lines.

The Raman shift equals the vibrational wavenumber of the molecule and is independent of the wavelength of the excitation light: with excitation at $532\,\mathrm{nm}$ or $785\,\mathrm{nm}$, the strongest line of $\ce{CCl4}$ is at $459\,\mathrm{cm^{-1}}$ in both cases. The abscissa of a Raman spectrum is therefore the Raman shift, and the spectrum can be compared directly with the infrared spectrum.

![Energy-level diagrams of infrared absorption, Rayleigh scattering, Stokes and anti-Stokes Raman scattering, resonance Raman scattering and fluorescence: Raman scattering proceeds via a virtual state, the excitation light of resonance Raman falls within an electronic absorption band, and fluorescence is emission from a real excited state](./plots/raman-energy-diagram.py)

Raman scattering is very weak: Rayleigh scattering is about $10^{-3}$ of the incident light, Raman scattering is again about three orders of magnitude weaker than Rayleigh scattering, and the Raman cross section of a single molecule is more than ten orders of magnitude smaller than the effective fluorescence cross section. This is why Raman spectroscopy could not be widely applied before the advent of the laser. The scattering intensity is proportional to the fourth power of the frequency (the same origin as the **Rayleigh scattering law**), which is important in choosing the laser wavelength (11.5.4).

Anti-Stokes lines arise from molecules in vibrationally excited states; by the **Boltzmann distribution**, the intensity ratio of the two lines is

$$
\frac{I_{\mathrm{aS}}}{I_{\mathrm{S}}} = \left(\frac{\tilde\nu_0 + \Delta\tilde\nu}{\tilde\nu_0 - \Delta\tilde\nu}\right)^4\exp\!\left(-\frac{hc\,\Delta\tilde\nu}{k_{\mathrm{B}}T}\right).
\tag{11.9}
$$
At room temperature the anti-Stokes lines are much weaker, and the larger the shift the weaker they are, so usually only Stokes lines are recorded; conversely, measuring the intensity ratio gives the temperature of the sample, which is used for contactless temperature measurement in laser heating, combustion flames and microdevices.

![Left: simulated Raman spectrum of CCl₄ at 298 K with 532 nm excitation; the Stokes and anti-Stokes lines are distributed symmetrically on either side of the Rayleigh line, and the anti-Stokes lines are weakened according to Eq. (11.9). Right: the ratio of anti-Stokes to Stokes intensity as a function of temperature for several Raman shifts](./plots/stokes-antistokes.py)

**Example 11.5.1** With $532\,\mathrm{nm}$ laser excitation at $298\,\mathrm{K}$, what is the ratio of the anti-Stokes to the Stokes intensity of the $459\,\mathrm{cm^{-1}}$ line of $\ce{CCl4}$?

**Solution** $\tilde\nu_0 = 10^7/532 = 18797\,\mathrm{cm^{-1}}$, and the frequency factor is $(19256/18338)^4 = 1.216$; $hc\Delta\tilde\nu/(k_{\mathrm{B}}T) = 1.4388\,\mathrm{cm\,K}\times459\,\mathrm{cm^{-1}}/298\,\mathrm{K} = 2.216$, and $\mathrm{e}^{-2.216} = 0.109$. The intensity ratio is $1.216\times0.109 = 0.133$.

### 11.5.2. Raman Activity and the Rule of Mutual Exclusion

The selection rule for Raman scattering can be understood from classical electromagnetic theory. The electric field of the incident light, $\boldsymbol{E} = \boldsymbol{E}_0\cos(2\pi\nu_0t)$, deforms the electron cloud of the molecule and produces an **induced dipole** $\boldsymbol{p} = \alpha\boldsymbol{E}$, where the proportionality factor $\alpha$ is the **polarizability** of the molecule ([6.1.4](/6.1.4#sec-4.3.5); in general a second-rank tensor, treated here as a scalar). When the molecule vibrates, the polarizability varies with the normal coordinate $Q = Q_0\cos(2\pi\nu_{\mathrm{vib}}t)$,

$$
\alpha = \alpha_0 + \left(\frac{\partial\alpha}{\partial Q}\right)_0Q + \cdots,
$$
and substitution followed by the product-to-sum formula gives

$$
\boldsymbol{p} = \alpha_0\boldsymbol{E}_0\cos(2\pi\nu_0t) + \frac{1}{2}\left(\frac{\partial\alpha}{\partial Q}\right)_0Q_0\boldsymbol{E}_0\big[\cos 2\pi(\nu_0 - \nu_{\mathrm{vib}})t + \cos 2\pi(\nu_0 + \nu_{\mathrm{vib}})t\big].
\tag{11.10}
$$
The oscillating induced dipole radiates: the first term is Rayleigh scattering of unchanged frequency, and the second gives Stokes and anti-Stokes scattering at frequencies $\nu_0 \mp \nu_{\mathrm{vib}}$. Classical theory gives the two equal intensities; the difference in intensity (Eq. (11.9)) arises from the populations of the levels and is a quantum effect.

**Definition 11.5.4 (Raman Activity)** A normal vibration that changes the polarizability of the molecule, that is, with $(\partial\alpha/\partial Q)_0 \ne 0$, is **Raman active** and gives rise to Raman scattering.

Infrared activity depends on the change of the dipole moment, and Raman activity on the change of the polarizability (the deformability of the electron cloud); the symmetry requirements are different. For a molecule with a center of symmetry, the dipole moment is a quantity that changes sign under inversion, whereas the polarizability is invariant under inversion, so that:

**Definition 11.5.5 (Rule of Mutual Exclusion)** The normal vibrations of a molecule with a center of symmetry cannot be both infrared active and Raman active: vibrations symmetric with respect to the center of symmetry can only be Raman active, and antisymmetric vibrations can only be infrared active. This regularity is called the **rule of mutual exclusion**.

$\ce{CO2}$ has a center of symmetry: the symmetric stretching appears only in the Raman spectrum (the Fermi-resonance doublet at $1285$/$1388\,\mathrm{cm^{-1}}$, 11.1.6), while the antisymmetric stretching and the bending appear only in the infrared spectrum. For molecules without a center of symmetry (such as $\ce{H2O}$), a vibration can have both activities. A few vibrations have neither; for example, the $\ce{CH2}$ twisting vibration of ethylene (about $1027\,\mathrm{cm^{-1}}$) changes neither the dipole moment nor the polarizability and gives no peak in either spectrum. Some books also call "both activities are possible without a center of symmetry" and "neither is active" rules, but only the rule of mutual exclusion is a general law; the other two merely state that without a center of symmetry there is no such restriction.

Even for molecules without a center of symmetry, the strengths of the two spectra are often complementary:

| | Infrared absorption | Raman scattering |
|---|---|---|
| Condition of occurrence | change of dipole moment | change of polarizability |
| Strong peaks | polar groups: $\ce{C=O}$, $\ce{O-H}$, $\ce{N-H}$, $\ce{C-O}$, $\ce{Si-O}$ | nonpolar, symmetric, easily polarized groups: $\ce{C=C}$, $\ce{C#C}$, $\ce{S-S}$, $\ce{C-S}$, $\ce{N=N}$, ring-breathing vibrations of aromatic rings |
| Water | strong absorption, severe interference | very weak, aqueous solutions can be measured directly |
| Sample and container | salt plates, KBr pellets, ATR | glass vials, capillaries, through packaging; almost no sample preparation |
| Main interferences | water and $\ce{CO2}$ | fluorescence background, heating or photolysis of the sample |
| Low-frequency region | generally down to $400\,\mathrm{cm^{-1}}$ | down to below $100\,\mathrm{cm^{-1}}$ (lattice vibrations, metal–ligand vibrations) |

The Raman intensity is proportional to the concentration (the scattered signal does not involve a logarithm as absorption does), and the peaks are narrower and overlap less than in the infrared, which favors quantitation and the analysis of mixtures. Among biomolecules, the $\ce{S-S}$ stretching of disulfide bonds (about $510\,\mathrm{cm^{-1}}$, the position depending on the conformation of $\ce{C-S-S-C}$), the ring vibrations of tryptophan and tyrosine (the intensity ratio of the tyrosine doublet at $850$/$830\,\mathrm{cm^{-1}}$ reflects the hydrogen-bonding state of the phenolic hydroxyl), the amide I band (about $1670$–$1650\,\mathrm{cm^{-1}}$) and the amide III band can all be measured in aqueous solution and complement the infrared spectrum (11.2.5).

### 11.5.3. Depolarization Ratio

When the excitation is **linearly polarized light**, the scattered light is generally partially polarized, and the degree of polarization reflects the symmetry of the vibration.

**Definition 11.5.6 (Depolarization Ratio)** With excitation by a linearly polarized laser and observation at right angles to the direction of incidence, the ratio of the intensities of the components of the scattered light polarized perpendicular and parallel to the polarization of the incident light,

$$
\rho = \frac{I_\perp}{I_\parallel}
$$
is called the **depolarization ratio** of that Raman line.

From the derivatives of the polarizability tensor, $\alpha'_{ij} = (\partial\alpha_{ij}/\partial Q)_0$, two quantities independent of the molecular orientation can be defined: the isotropic part (mean) $\bar\alpha' = \frac13(\alpha'_{xx} + \alpha'_{yy} + \alpha'_{zz})$ and the anisotropy $\gamma'$. Averaging over all orientations of the molecule gives

$$
\rho = \frac{3\gamma'^2}{45\bar\alpha'^2 + 4\gamma'^2}.
\tag{11.11}
$$
Hence:

- For a non-totally-symmetric vibration, $\bar\alpha' = 0$ and $\rho = 3/4$; such bands are called depolarized.
- For a totally symmetric vibration, $\bar\alpha' \ne 0$ and $0 \le \rho < 3/4$; such bands are called polarized. For totally symmetric vibrations of highly symmetric molecules (such as tetrahedral or octahedral ones), $\gamma' = 0$ and $\rho \approx 0$.

The depolarization ratio therefore distinguishes the symmetry of vibrations: for example, for $\ce{CCl4}$ the $459\,\mathrm{cm^{-1}}$ band (totally symmetric stretching) has $\rho \approx 0$, and the bands at $218$ and $314\,\mathrm{cm^{-1}}$ have $\rho = 3/4$. The statement that "the smaller $\rho$, the higher the symmetry of the molecule" confuses the molecule with the vibration: $\bar\alpha'$ is the isotropic part of the derivative of the polarizability and decides whether a particular vibration is totally symmetric, not how symmetric the whole molecule is. By counting the number of polarized bands and comparing with the predictions for various candidate structures, the symmetry of a molecule can be inferred. For example, the Raman spectrum of the crystal violet cation (shown below) agrees with the prediction for a propeller-shaped structure of $D_3$ symmetry, showing that the three dimethylaminophenyl groups are equivalent and that the positive charge is delocalized over the whole conjugated system rather than localized on one nitrogen atom.

```smiles
CN(C)c1ccc(cc1)C(c1ccc(cc1)N(C)C)=C1C=CC(C=C1)=[N+](C)C
```

### 11.5.4. Raman Spectrometers

A Raman spectrometer consists of a laser source, a sample compartment, a dispersive system (or an interferometer) and a detector; the scattered light is generally collected at $90^\circ$ or $180^\circ$ (backscattering, the usual geometry of micro-Raman).

- Laser sources: commonly used are $532\,\mathrm{nm}$ (frequency-doubled Nd:YAG), $633\,\mathrm{nm}$ (He–Ne, $632.8\,\mathrm{nm}$), $785\,\mathrm{nm}$ (diode laser) and $1064\,\mathrm{nm}$ (Nd:YAG); early instruments mostly used the argon-ion laser ($488.0$ and $514.5\,\mathrm{nm}$). The scattering intensity is proportional to $\nu^4$, so excitation at $532\,\mathrm{nm}$ is about 16 times stronger than at $1064\,\mathrm{nm}$; but shorter wavelengths more readily excite the **fluorescence** of the sample or of impurities, whose intensity can exceed the Raman signal by several orders of magnitude and swamp it completely. Biological and colored samples are mostly excited at $785\,\mathrm{nm}$ or $1064\,\mathrm{nm}$, trading intensity for a low fluorescence background.
- Rejection of Rayleigh light: Rayleigh scattering is more than $10^3$ times stronger than Raman scattering and lies very close to the Raman lines. It is now removed with notch filters or long-pass edge filters (optical density $\ge 6$ at the laser line), which allow small shifts of $50$–$100\,\mathrm{cm^{-1}}$ to be measured; formerly double or triple monochromators with very low stray light were needed.
- Dispersion and detection: dispersive instruments use a grating spectrograph and a cooled **charge-coupled device** ([6.4.7](/6.4.7#sec-7.5.3)) to record a whole spectral range simultaneously. Silicon CCDs are insensitive beyond $1\,\mu\mathrm{m}$, so instruments with $1064\,\mathrm{nm}$ excitation use an interferometer and an $\ce{InGaAs}$ or liquid-nitrogen-cooled $\ce{Ge}$ detector (FT-Raman), making up for the low intensity of near-infrared excitation through the multiplex advantage.
- Micro-Raman: the laser is focused on the sample through a microscope objective, and a pinhole as in the **confocal microscope** ([6.4.10](/6.4.10#def-10.4.1)) rejects out-of-focus signal; the lateral resolution approaches the diffraction limit ($< 1\,\mu\mathrm{m}$) and there is some depth-sectioning ability. Chemical images obtained by point-by-point scanning show, without labeling, the distribution of lipids ($\ce{CH2}$, about $2850\,\mathrm{cm^{-1}}$), proteins (about $2930\,\mathrm{cm^{-1}}$) and nucleic acids (about $785\,\mathrm{cm^{-1}}$) in cells; molecules labeled with $\ce{C-D}$ or alkyne groups (about $2100$–$2200\,\mathrm{cm^{-1}}$, the "silent region" of cells) can be used to trace metabolism (11.1.2). Coherent Raman techniques such as stimulated Raman scattering (SRS) raise the imaging speed to video rate.
- Samples: liquids, solids and gases can all be measured, in glass vials, and at varied temperature and pressure; to prevent decomposition or heating of the sample by the intense light, a spinning cell or reduced power can be used.

### 11.5.5. Resonance Raman and Surface-Enhanced Raman Scattering

The sensitivity of ordinary Raman spectroscopy is low, and two enhancement effects have made it a tool for trace analysis and biological research.

**Definition 11.5.7 (Resonance Raman)** When the frequency of the excitation light is close to or within an electronic absorption band of the molecule (chromophore), the Raman scattering intensity of the vibrational modes coupled to that electronic transition increases by a factor of $10^3$–$10^6$. This phenomenon, and the spectroscopic method exploiting it, are called **resonance Raman** spectroscopy.

The modes that are enhanced are mainly totally symmetric vibrations that change the geometry of the excited state, so resonance Raman is highly selective: in a macromolecule only the vibrations near the chromophore are emphasized, and the signal from the rest is negligible. Typical applications are heme proteins such as hemoglobin and cytochromes (excited in the Soret band, the "marker bands" of the porphyrin ring report the oxidation state, spin state and coordination of the iron), the retinal in rhodopsin and bacteriorhodopsin, and carotenoids ($\ce{C=C}$ at about $1520$, $\ce{C-C}$ at about $1160\,\mathrm{cm^{-1}}$). Under resonance conditions fluorescence is also excited, and deep-ultraviolet excitation at $200$–$260\,\mathrm{nm}$ avoids it (fluorescence appears at longer wavelengths) while selectively enhancing the vibrations of aromatic amino acids and peptide bonds.

**Definition 11.5.8 (Surface-Enhanced Raman Scattering)** The phenomenon in which the Raman scattering intensity of molecules adsorbed on or near the surface of a roughened or nanostructured metal (mainly Ag, Au, Cu) is many orders of magnitude greater than that of free molecules in solution is called **surface-enhanced Raman scattering** (SERS).

In 1974 Fleischmann et al. observed a strong Raman signal of pyridine on a roughened silver electrode, and in 1977 Jeanmaire and Van Duyne, and Albrecht and Creighton, independently pointed out that it was an enhancement effect. The enhancement arises from two mechanisms:

- Electromagnetic enhancement (the main contribution): the incident light excites localized **surface plasmon resonances** of the metal nanostructure ([6.4.9](/6.4.9#sec-9.6.3)) and produces a very strong local electric field near the surface; the scattered light is enhanced in the same way, and the total enhancement factor is about the fourth power of the local field enhancement, $G \approx \lvert E_{\mathrm{loc}}/E_0\rvert^4$. It decays rapidly with distance from the surface (a few nanometers) and is largest in the gaps between two nanoparticles ("hot spots").
- Chemical enhancement: charge transfer between the molecule and the metal changes the polarizability of the molecule; it contributes about $10$–$10^2$ and acts only on molecules chemisorbed directly.

The enhancement factor averaged over the whole surface is generally $10^6$–$10^8$, and can exceed $10^{10}$ at hot spots. The often-quoted "$10^{12}$–$10^{14}$" comes from early estimates in the 1997 single-molecule SERS experiments of Nie and Emory and of Kneipp et al., in which the dye molecules (rhodamine 6G, crystal violet) were simultaneously under resonance conditions (surface-enhanced resonance Raman scattering, SERRS); later quantitative studies showed that the enhancement by SERS alone is of the order of $10^{10}$, the remainder coming from the resonance Raman contribution. Nevertheless, single-molecule SERS demonstrated that Raman spectroscopy can reach single-molecule sensitivity.

SERS requires that the molecule adsorb on the enhancing substrate or be very close to the surface: nitrogen-containing heterocycles (pyridine), sulfur compounds, carboxylic acids, dyes and many biomolecules give good SERS signals. The common substrates are silver or gold sols, assembled films of nanoparticles and nanoarrays prepared by lithography. Applications include the rapid detection of trace organic pollutants, pesticide residues and explosives; SERS tags (gold nanoparticles with adsorbed reporter molecules) for immunoassays and cell imaging, where the narrow peaks of different tags facilitate multiplexed detection; and tip-enhanced Raman spectroscopy (TERS), in which a metal tip acts as a single hot spot and chemical images with nanometer spatial resolution can be obtained.

## Summary

| Topic | Key points |
|---|---|
| Harmonic oscillator | $\tilde\nu = \frac{1}{2\pi c}\sqrt{k/\mu}$, $\tilde\nu/\mathrm{cm^{-1}} \approx 1303\sqrt{(k/10^2\,\mathrm{N\,m^{-1}})/(\mu/\mathrm{u})}$; large $k$ and small $\mu$ give high frequency |
| Anharmonicity | Morse potential, level spacing decreases with $v$, overtones slightly below integral multiples of the fundamental |
| Normal vibrations | $3N - 6$ (linear $3N - 5$); stretching $\nu_{\mathrm{as}} > \nu_{\mathrm{s}}$ > bending |
| Infrared activity | change of dipole moment; intensity $\propto \lvert\partial\boldsymbol{p}/\partial Q\rvert^2$ |
| Beyond fundamentals | overtones, combination bands; vibrational coupling splits frequencies; Fermi resonance (aldehyde 2820/2720) |
| Group frequencies | functional group region $4000$–$1300$, fingerprint region $< 1300\,\mathrm{cm^{-1}}$; inductive effect raises, conjugation and hydrogen bonding lower the $\ce{C=O}$ frequency |
| Degree of unsaturation | $U = 1 + n_4 + (n_3 - n_1)/2$ |
| Proteins | amide I ($\alpha$-helix about $1655$, $\beta$-sheet about $1630\,\mathrm{cm^{-1}}$), amide II |
| FTIR | the interferogram is the Fourier transform of the spectrum; $\Delta\tilde\nu \approx 1/\Delta$; multiplex, throughput and wavenumber-accuracy advantages |
| ATR | $d_{\mathrm{p}} = \lambda_1/(2\pi\sqrt{\sin^2\alpha - (n_2/n_1)^2})$, a few micrometers |
| Near-infrared | overtones and combinations of $\ce{X-H}$; weak, deeply penetrating; multivariate calibration (principal component regression, partial least squares) |
| Raman | inelastic scattering; Raman shift = vibrational wavenumber; $I_{\mathrm{aS}}/I_{\mathrm{S}}$ given by the Boltzmann factor |
| Raman activity | change of polarizability; mutual exclusion with infrared when there is a center of symmetry |
| Depolarization ratio | $\rho = 3\gamma'^2/(45\bar\alpha'^2 + 4\gamma'^2)$; totally symmetric $< 3/4$, non-totally-symmetric $= 3/4$ |
| Enhancement | resonance Raman $10^3$–$10^6$; SERS average $10^6$–$10^8$, hot spots $> 10^{10}$ |

The combined interpretation of a large number of functional groups is treated in the spectroscopy chapter of [organic chemistry](/6.5), where the group frequencies of this chapter, the chemical shifts and coupling constants of [6.4.12](/6.4.12) and the fragmentation rules of [6.4.15](/6.4.15#sec-15.4) are used together.

## Questions

1. Why do $\ce{N2}$ and $\ce{O2}$ not absorb infrared light yet are Raman active? What does this mean for the measurement of greenhouse gases in the atmosphere?

   **Answer** The dipole moment of a homonuclear diatomic molecule is zero throughout the vibration, but the polarizability changes with the bond length. The main components of the atmosphere therefore do not interfere with infrared measurements, whereas molecules with infrared-active vibrations, such as $\ce{CO2}$, $\ce{CH4}$, $\ce{H2O}$ and $\ce{N2O}$, absorb the infrared radiation from the ground and are greenhouse gases ([5.5.5](/5.5.5#sec-5.3.3)).
2. How do the abscissa (Raman shift) and the intensity differ between Raman spectra of the same compound measured with $532\,\mathrm{nm}$ and $785\,\mathrm{nm}$ lasers?

   **Answer** The Raman shift is the same (it equals the vibrational wavenumber and does not depend on the excitation wavelength). Away from electronic absorption, the $\nu^4$ dependence makes the scattering intensity with $532\,\mathrm{nm}$ excitation about $(785/532)^4 \approx 4.7$ times that with $785\,\mathrm{nm}$, but the fluorescence background of the sample is usually also much stronger.
3. In an FTIR measurement, by how much must the travel of the moving mirror be increased to improve the resolution from $4\,\mathrm{cm^{-1}}$ to $0.5\,\mathrm{cm^{-1}}$? How does the signal-to-noise ratio change at constant measurement time when detector noise dominates?

   **Answer** The maximum path difference increases from $0.25\,\mathrm{cm}$ to $2\,\mathrm{cm}$, and the mirror travel from about $0.125\,\mathrm{cm}$ to $1\,\mathrm{cm}$ (8-fold). With detector noise dominating, the signal in each resolution element is proportional to the width of the element, so at constant measurement time the signal-to-noise ratio falls to about $1/8$; restoring the original signal-to-noise ratio requires about $64$ times the measurement time (the signal-to-noise ratio is proportional to the square root of time).
