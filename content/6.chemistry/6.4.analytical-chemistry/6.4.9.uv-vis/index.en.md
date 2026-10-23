---
title: Ultraviolet–Visible Absorption Spectrophotometry
description: Molecular energy levels and band spectra; σ→σ*, n→σ*, π→π*, n→π* and charge-transfer transitions, chromophores, auxochromes, bathochromic and hypsochromic shifts, ultraviolet absorption of proteins and nucleic acids; derivation of the absorption law, additivity and deviations, transmittance and isosbestic points; spectrophotometers, the dual-wavelength method, derivative spectra and measurement error; multicomponent determination, composition of complexes and determination of pKa; surface plasmon resonance and circular dichroism.
source_hash: d18088c66b01
---

The energies of valence-electron transitions in molecules lie at roughly $1.5$–$6\,\mathrm{eV}$, corresponding to ultraviolet–visible light of $200$–$800\,\mathrm{nm}$. Measuring the absorption of light in this range by a solution serves two purposes: the position and shape of the absorption bands reveal the conjugated systems and chromophores in the molecule (the first step of spectral interpretation in 6.5, Organic Chemistry), and the strength of the absorption gives the concentration. The spectrophotometer is the most commonly used instrument in chemical and biological laboratories, indispensable for measuring the concentration of proteins and nucleic acids, following enzymatic reactions and measuring equilibrium constants. The **Beer–Lambert law**, **absorbance** and the **molar absorption coefficient** were defined in [6.3.17](/6.3.17#def-17.2.3); this chapter treats the physical origin of the law, the conditions under which it applies, and measurement error. The physics of molecular energy levels and of the **band spectrum** is in [5.5.5](/5.5.5#sec-5.3), and the principles of the source, monochromator and detector of spectroscopic instruments are in [6.4.7](/6.4.7#sec-7.1.3). At the end of the chapter we introduce two optical methods widely used in bioanalysis: surface plasmon resonance, which measures molecular interactions, and circular dichroism, which is used to determine protein secondary structure. The next chapter ([6.4.10](/6.4.10)) treats how molecules emit light after absorbing photons.

## 9.1. Molecular Energy Levels and Electronic Spectra

### 9.1.1. Molecular Energy Levels and Band Spectra

The energy of a molecule consists of the motion of the electrons, the vibration of the nuclei and the rotation of the molecule, $E = E_{\mathrm{e}} + E_{\mathrm{v}} + E_{\mathrm{r}}$, all of which are quantized ([5.5.5](/5.5.5#sec-5.3.1)). The spacings of adjacent levels differ by roughly an order of magnitude from one kind to the next:

| Transition | Level spacing | Spectral region | Spectrum |
|---|---|---|---|
| Electronic levels | $1$–$20\,\mathrm{eV}$ | Ultraviolet–visible ($60$–$1200\,\mathrm{nm}$) | Electronic spectrum (this chapter) |
| Vibrational levels | $0.05$–$1\,\mathrm{eV}$ | Infrared ($1$–$25\,\mu\mathrm{m}$) | Vibrational spectrum ([6.4.11](/6.4.11)) |
| Rotational levels | $0.005$–$0.05\,\mathrm{eV}$ | Far-infrared and microwave | Rotational spectrum |

When an electronic transition occurs, the vibrational and rotational states change simultaneously, so an electronic transition is not a single line but a band made up of many vibration–rotation lines. In solution, molecules collide continually with solvent molecules, the rotational lines broaden and merge, and the vibrational structure is often blurred as well, leaving only a broad absorption band: the **band spectrum** of a **molecular spectrum**. The $\mathrm{n}\to\pi^*$ absorption of s-tetrazine (1,2,4,5-tetrazine) at $500$–$550\,\mathrm{nm}$ is a typical example: in the vapor the fine vibrational and rotational structure can be seen, in nonpolar cyclohexane only the vibrational structure remains, and in water (where the solvent forms **hydrogen bonds** with the lone pairs of the nitrogen atoms) it becomes a smooth broad band.

```smiles
c1nncnn1
```

The ultraviolet–visible spectrum in solution therefore carries limited information: it mainly reflects the properties of the conjugated systems and chromophores in the molecule and cannot give the complete structure as infrared or nuclear magnetic resonance spectra can, but it is sensitive, quick to measure and inexpensive.

### 9.1.2. Ultraviolet–Visible Absorption Spectrophotometry

**Definition 9.1.1** A method of qualitative and quantitative analysis and structural study based on the selective absorption of ultraviolet–visible light (about $190$–$800\,\mathrm{nm}$) by the molecules of a substance is called **ultraviolet–visible spectrophotometry** (also ultraviolet–visible absorption spectrometry). Plotting absorbance (or molar absorption coefficient) against wavelength gives the absorption spectrum (absorption curve); the wavelength of strongest absorption is denoted $\lambda_{\max}$ and the corresponding molar absorption coefficient $\varepsilon_{\max}$.

Its characteristics are:

- Both qualitative analysis (from the position and shape of the absorption bands) and quantitative analysis (absorbance proportional to concentration) are possible; detectable concentrations are generally $10^{-6}$–$10^{-5}\,\mathrm{mol\,L^{-1}}$, and with color-forming reactions can reach the $10^{-7}\,\mathrm{mol\,L^{-1}}$ level.
- Physicochemical constants such as dissociation constants, the composition and stability constants of complexes, and reaction rates can be determined (Section 9.5).
- The instrument is simple, inexpensive and easy to operate, with a relative measurement error of about $1\%$–$2\%$.
- The range of application is wide: inorganic ions (most after color-forming reactions), organic compounds, drugs, and biological macromolecules such as proteins and nucleic acids.

The color of a substance arises from selective absorption of visible light: a solution shows the complementary color of the light it absorbs.

| Wavelength of light absorbed / nm | Color of light absorbed | Color of solution (complementary) |
|---|---|---|
| $400$–$435$ | Violet | Yellow-green |
| $435$–$480$ | Blue | Yellow |
| $480$–$490$ | Green-blue | Orange |
| $490$–$500$ | Blue-green | Red |
| $500$–$560$ | Green | Purple-red |
| $560$–$580$ | Yellow-green | Purple |
| $580$–$595$ | Yellow | Blue |
| $595$–$650$ | Orange | Green-blue |
| $650$–$780$ | Red | Blue-green |

$\ce{MnO4-}$ absorbs green light near $525\,\mathrm{nm}$ and appears purple-red, and $\ce{[Cu(NH3)4]^2+}$ absorbs orange-yellow light and appears deep blue. The history of spectrophotometry is one of progress in detection: visual colorimetry (the eye compares the depth of color), photoelectric colorimetry (filters and photocells), and spectrophotometry (prism or grating dispersion with photoelectric detection, allowing measurement at any wavelength).

## 9.2. Absorption Spectra and Molecular Structure

### 9.2.1. Electronic Transitions of Organic Molecules

According to **molecular orbital theory**, three kinds of valence electrons in organic molecules are relevant to ultraviolet–visible absorption: σ electrons forming single bonds, π electrons forming double and triple bonds, and the unshared lone-pair electrons (n electrons) on heteroatoms such as O, N, S and the halogens. They occupy the bonding orbitals σ and π and the nonbonding orbital n; the empty antibonding orbitals $\sigma^*$ and $\pi^*$ lie higher in energy. The usual order of energies is $\sigma < \pi < \mathrm{n} < \pi^* < \sigma^*$, and four kinds of transition are possible:

| Transition | Energy required | Typical $\lambda_{\max}$ | Typical $\varepsilon_{\max}$ / ($\mathrm{L\,mol^{-1}\,cm^{-1}}$) | Examples |
|---|---|---|---|---|
| $\sigma\to\sigma^*$ | Largest | $< 150\,\mathrm{nm}$ (vacuum ultraviolet) | — | Methane $122\,\mathrm{nm}$, ethane $135\,\mathrm{nm}$ |
| $\mathrm{n}\to\sigma^*$ | Large | $150$–$250\,\mathrm{nm}$ | $10^2$–$3\times10^3$ | $\ce{H2O}$ $167$ (1480), $\ce{CH3OH}$ $184$ (150), $\ce{CH3Cl}$ $173$ (200), $\ce{CH3I}$ $258$ (365), $\ce{(CH3)3N}$ $227$ (900) |
| $\pi\to\pi^*$ | Smaller | Isolated double bonds about $170$–$190\,\mathrm{nm}$, shifting to longer wavelengths on conjugation | $10^3$–$10^5$ | Ethylene $171$ (15 000), 1,3-butadiene $217$ (21 000) |
| $\mathrm{n}\to\pi^*$ | Smallest | $250$–$600\,\mathrm{nm}$ | $10$–$10^2$ | Acetone $279$ (15), s-tetrazine about $540$ |

The data are approximate values in saturated hydrocarbon or alcohol solvents, with $\varepsilon_{\max}$ in parentheses. Several rules follow.

- Saturated hydrocarbons have only $\sigma\to\sigma^*$ transitions and are transparent in the near ultraviolet, so hexane and cyclohexane can serve as solvents for ultraviolet spectra; saturated compounds containing heteroatoms (water, alcohols, ethers, alkyl halides) begin to absorb only near $200\,\mathrm{nm}$. The transparency limits (cutoff wavelengths) of solvents are about: water $190\,\mathrm{nm}$, acetonitrile $190\,\mathrm{nm}$, methanol $205\,\mathrm{nm}$, ethanol $210\,\mathrm{nm}$, dichloromethane $233\,\mathrm{nm}$, chloroform $245\,\mathrm{nm}$, acetone $330\,\mathrm{nm}$.
- Ultraviolet–visible spectral analysis of organic compounds rests mainly on $\pi\to\pi^*$ and $\mathrm{n}\to\pi^*$ transitions, which fall above $200\,\mathrm{nm}$, where instruments can measure.
- A $\pi\to\pi^*$ transition is symmetry-allowed and the absorption is strong ($\varepsilon \ge 10^4$); in an $\mathrm{n}\to\pi^*$ transition the n orbital and the $\pi^*$ orbital are almost orthogonal, the transition probability is smaller by two to three orders of magnitude, and the absorption is weak ($\varepsilon < 10^3$, often a few tens). The intensity of an absorption band is therefore a criterion for the type of transition.

### 9.2.2. Chromophores and Auxochromes

**Definition 9.2.1** An unsaturated group in a molecule that gives rise to absorption in the ultraviolet–visible region (a group containing π electrons, such as $\ce{C=C}$, $\ce{C=O}$, $\ce{N=N}$, $\ce{-NO2}$, $\ce{C#N}$ and the benzene ring) is called a **chromophore**. A saturated group containing n electrons ($\ce{-OH}$, $\ce{-OR}$, $\ce{-NH2}$, $\ce{-NR2}$, $\ce{-SH}$, $\ce{-Cl}$, $\ce{-Br}$ and so on) that does not itself absorb in the near ultraviolet but, when attached to a chromophore, shifts the absorption band to longer wavelengths and intensifies it is called an **auxochrome**.

The n electrons of an auxochrome are conjugated with the π electrons of the chromophore (n–π conjugation), which enlarges the π system and reduces the gap of the $\pi\to\pi^*$ transition. Four terms describe the shift and the change in intensity of an absorption band.

**Definition 9.2.2** The shift of the $\lambda_{\max}$ of an absorption band to longer wavelengths, owing to a change of substituent, solvent or structure, is called a **bathochromic shift** (red shift), and a shift to shorter wavelengths a **hypsochromic shift** (blue shift); an increase in absorption intensity ($\varepsilon_{\max}$) is called the **hyperchromic effect** and a decrease the **hypochromic effect**.

The three absorption bands of benzene all arise from $\pi\to\pi^*$ transitions: at $184\,\mathrm{nm}$ ($\varepsilon \approx 6\times10^4$), $204\,\mathrm{nm}$ ($\varepsilon \approx 7900$) and a weak band near $254\,\mathrm{nm}$ ($\varepsilon \approx 200$, symmetry-forbidden, with vibrational fine structure in nonpolar solvents, characteristic of aromatic rings). Auxochromes such as $\ce{-OH}$ and $\ce{-NH2}$ shift the latter two bands to the red and intensify them:

```smiles
c1ccccc1 1
Oc1ccccc1 2
[O-]c1ccccc1 3
Nc1ccccc1 4
```

| Compound | Absorption bands ($\lambda_{\max}$ / nm, $\varepsilon_{\max}$ in parentheses) |
|---|---|
| Benzene 1 | $204$ (7900), $256$ (200) |
| Phenol 2 | $210$ (6200), $270$ (1450) |
| Phenoxide anion 3 | $235$ (9400), $287$ (2600) |
| Aniline 4 | $230$ (8600), $280$ (1430) |
| Anilinium chloride | $203$ (7500), $254$ (160) |

When phenol dissociates to the anion, the oxygen carries an extra pair of electrons that can take part in conjugation, and the absorption shifts further to the red and intensifies; when aniline is protonated, the lone pair on nitrogen is occupied by $\ce{H+}$ and no longer conjugates with the benzene ring, and the spectrum almost returns to that of benzene. Comparing spectra in acidic and basic solution therefore shows whether a molecule contains a phenolic hydroxyl or an aromatic amine, which is also the basis of the photometric determination of $\mathrm{p}K_{\mathrm{a}}$ in Section 9.5.4.

### 9.2.3. Factors Affecting Absorption Bands

Conjugation: the larger the conjugated system, the smaller the gap between the highest occupied and lowest unoccupied orbitals (the **frontier orbitals**), and the $\pi\to\pi^*$ absorption shifts to the red and intensifies. Linear polyenes are the clearest example:

| Compound | Number of conjugated double bonds | $\lambda_{\max}$ / nm | $\varepsilon_{\max}$ | Color |
|---|---|---|---|---|
| Ethylene | 1 | $171$ | $15\,000$ | Colorless |
| 1,3-Butadiene | 2 | $217$ | $21\,000$ | Colorless |
| 1,3,5-Hexatriene | 3 | $258$ | $35\,000$ | Colorless |
| β-Carotene | 11 | $451$ | $1.4\times10^5$ | Orange |

β-Carotene absorbs blue light, which is why carrots are orange; the protonated Schiff base of retinal in the retina (11 conjugated bonds plus the protein environment) absorbs at about $500\,\mathrm{nm}$ and is the molecular basis of vision. The empirical rules for estimating $\lambda_{\max}$ from structure (the Woodward–Fieser rules) are treated in 6.5, Organic Chemistry, together with structure determination.

```smiles
CC1=C(C(C)(C)CCC1)/C=C/C(C)=C/C=C/C(C)=C/C=C/C=C(C)/C=C/C=C(C)/C=C/C2=C(C)CCCC2(C)C
```

Substituent effects: when an auxochrome (an electron-donating group with n electrons) and an electron-withdrawing chromophore ($\ce{-NO2}$, $\ce{C=O}$) are attached at opposite ends of the same conjugated system, a "push–pull" system results, the excited state has intramolecular charge-transfer character, and the absorption shifts strongly to the red. $p$-Nitrophenol has $\lambda_{\max} = 317\,\mathrm{nm}$ in acidic solution (colorless) and $\lambda_{\max} = 400\,\mathrm{nm}$ ($\varepsilon \approx 1.8\times10^4$, yellow) after dissociation to the anion; it can therefore serve as an acid–base indicator, and it is the common chromogenic product in assays of the activity of hydrolases such as phosphatases ($p$-nitrophenyl phosphate releases $p$-nitrophenol on hydrolysis, and the absorbance is measured at $405\,\mathrm{nm}$ in basic solution).

```smiles
Oc1ccc(cc1)[N+](=O)[O-] 1
[O-]c1ccc(cc1)[N+](=O)[O-] 2
```

**Solvent effect**: the polarity of the solvent affects the two kinds of transitions in opposite directions.

- $\pi\to\pi^*$ transitions: for most molecules the $\pi^*$ excited state is more polar than the ground state, a polar solvent stabilizes the excited state more strongly, the energy gap decreases, and the absorption undergoes a **bathochromic shift** (usually within $10$–$20\,\mathrm{nm}$).
- $\mathrm{n}\to\pi^*$ transitions: the n electrons of the ground state are stabilized by hydrogen bonding to polar solvents (especially protic ones); after excitation the n orbital holds only one electron and the hydrogen bond is weakened, so the ground state is lowered more than the excited state and the absorption undergoes a **hypsochromic shift**. The $\mathrm{n}\to\pi^*$ band of acetone is at $279\,\mathrm{nm}$ in hexane and $264.5\,\mathrm{nm}$ in water.

Whether the band shifts to the red or to the blue when the solvent is changed from nonpolar to polar can therefore help identify the type of transition. Polar solvents also wipe out vibrational fine structure (the tetrazine of Section 9.1.1). The solvent must be stated when spectra are compared, and in measurements one chooses a solvent in which the sample is soluble, which is transparent at the measuring wavelength and which does not react with the sample.

### 9.2.4. Absorption Spectra of Inorganic Compounds

d–d and f–f transitions: according to **crystal field theory** ([6.1.5](/6.1.5#sec-5.5)), when a transition metal ion forms a complex with ligands, the five d orbitals split into groups of different energy; transitions of d electrons between the split orbitals absorb visible light, and the absorption wavelength corresponds to the **crystal field splitting energy**: the stronger the ligand field, the larger the splitting and the shorter the absorption wavelength (the **spectrochemical series**). The absorption peak of $\ce{[Cu(H2O)6]^2+}$ is at about $800\,\mathrm{nm}$ (pale blue), and with the stronger-field ligand $\ce{NH3}$ the peak of $\ce{[Cu(NH3)4(H2O)2]^2+}$ moves to about $600\,\mathrm{nm}$ (deep blue). In centrosymmetric complexes d–d transitions are parity-forbidden (the Laporte rule) and occur weakly only through vibrations that break the symmetry; $\varepsilon$ is usually only $1$–$10^2\,\mathrm{L\,mol^{-1}\,cm^{-1}}$, too insensitive for quantitative analysis. The f–f transitions of lanthanide ions are shielded by the outer 5s and 5p electrons, and the absorption bands are narrow and sharp; the sharp absorption peaks of holmium oxide solution or holmium glass are used as standards for wavelength calibration of spectrophotometers.

Charge-transfer transitions:

**Definition 9.2.3** When a complex (or ion pair, or molecular complex) absorbs a photon, a transition in which an electron moves from an orbital belonging mainly to the electron donor to an orbital belonging mainly to the electron acceptor is called a **charge-transfer transition**. By direction one distinguishes ligand-to-metal (LMCT), metal-to-ligand (MLCT) and other types.

Charge-transfer transitions are both spin- and parity-allowed and the absorption is very strong, with $\varepsilon$ generally $10^3$–$10^5\,\mathrm{L\,mol^{-1}\,cm^{-1}}$; they are the main basis of sensitive inorganic color-forming reactions:

- LMCT: $\ce{MnO4-}$ ($525\,\mathrm{nm}$, $\varepsilon \approx 2.4\times10^3$), $\ce{CrO4^2-}$ ($372\,\mathrm{nm}$, $\varepsilon \approx 4.8\times10^3$), and the blood-red complex of $\ce{Fe^3+}$ with $\ce{SCN-}$ (about $480\,\mathrm{nm}$). It occurs most readily between a metal in a high oxidation state and an easily oxidized ligand.
- MLCT: the orange-red complex $\ce{[Fe(phen)3]^2+}$ of $\ce{Fe^2+}$ with 1,10-phenanthroline ($510\,\mathrm{nm}$, $\varepsilon = 1.1\times10^4$) is the classical method for iron; the MLCT excited state of $\ce{[Ru(bpy)3]^2+}$ also luminesces ([6.4.10](/6.4.10#sec-10.6.2)).

$\pi\to\pi^*$ transitions of ligands under the influence of metal ions: many organic color-forming reagents are themselves colored, and on coordination to a metal ion the electron distribution in the conjugated system changes, the absorption band shifts to the red or the blue, and its intensity changes. The complexes of azo reagents (arsenazo III, chlorophosphonazo III and so on) with $\ce{Ca^2+}$, rare earths, $\ce{U(VI)}$ and others have $\varepsilon$ up to $10^4$–$10^5$; the principle is the same as that of a **metallochromic indicator** ([6.4.3](/6.4.3#def-3.4.1)), the only difference being that the absorbance is measured here instead of watching for an abrupt color change.

### 9.2.5. Ultraviolet Absorption of Biological Macromolecules

The spectrophotometric measurements most often made in biochemical experiments are those of the concentration and purity of proteins and nucleic acids.

Proteins: the peptide bond absorbs strongly at $190$–$220\,\mathrm{nm}$ ($\pi\to\pi^*$ at about $190\,\mathrm{nm}$, $\mathrm{n}\to\pi^*$ at about $210$–$220\,\mathrm{nm}$), but many buffer components absorb there too; the usual choice is the absorption of the side chains of the aromatic amino acids near $280\,\mathrm{nm}$: tryptophan ($\varepsilon_{280} \approx 5500$), tyrosine ($\approx 1490$) and the disulfide bond of cystine ($\approx 125$); phenylalanine hardly absorbs at $280\,\mathrm{nm}$. The molar absorption coefficient of a denatured protein can be estimated from the amino acid sequence:

$$
\varepsilon_{280} \approx 5500\,n_{\mathrm{Trp}} + 1490\,n_{\mathrm{Tyr}} + 125\,n_{\mathrm{cystine}} \quad (\mathrm{L\,mol^{-1}\,cm^{-1}}),
$$
and native proteins usually differ from this by no more than about $5\%$. For proteins that contain no tryptophan or tyrosine (or when higher sensitivity is required), colorimetric assays are used: in the Bradford assay the absorption peak of Coomassie Brilliant Blue G-250 shifts from about $465\,\mathrm{nm}$ to $595\,\mathrm{nm}$ when it binds to protein (mainly basic and aromatic residues); the BCA and Lowry assays are based on a color reaction after the protein reduces $\ce{Cu^2+}$ to $\ce{Cu+}$.

```smiles
c1ccc2c(c1)c(c[nH]2)C[C@H](N)C(=O)O Trp
Oc1ccc(cc1)C[C@H](N)C(=O)O Tyr
```

Nucleic acids: the aromatic heterocyclic bases absorb strongly near $260\,\mathrm{nm}$. In a $1\,\mathrm{cm}$ cell, $A_{260} = 1$ corresponds to about $50\,\mu\mathrm{g\,mL^{-1}}$ of double-stranded DNA, $40\,\mu\mathrm{g\,mL^{-1}}$ of single-stranded RNA and about $33\,\mu\mathrm{g\,mL^{-1}}$ of single-stranded oligonucleotide (the last varies with the sequence; for accurate work $\varepsilon_{260}$ is calculated from the base composition). Pure DNA has $A_{260}/A_{280} \approx 1.8$ and RNA about $2.0$; a clearly lower ratio indicates contamination with protein or phenol, and a low $A_{260}/A_{230}$ indicates residual salts, guanidine or carbohydrates. Microvolume spectrophotometers, which use the surface tension of a droplet to form a path of $0.05$–$1\,\mathrm{mm}$ between two optical-fiber end faces and need only $1$–$2\,\mu\mathrm{L}$ of sample, were designed for measuring nucleic acids and proteins.

Melting of DNA: in the double helix the bases are stacked, and coupling between the π electrons makes the absorption weaker than that of the free bases (the hypochromic effect). Heating opens the double strand and destroys the stacking, and $A_{260}$ increases by about $30\%$–$40\%$, the **hyperchromic effect** of DNA denaturation. A plot of $A_{260}$ against temperature gives a sigmoidal melting curve, and the temperature at which the change is half complete is called the melting temperature $T_{\mathrm{m}}$; $T_{\mathrm{m}}$ rises with GC content (a GC pair has three hydrogen bonds and stronger stacking) and with ionic strength, and is the basis for designing PCR primers and choosing nucleic acid hybridization conditions.

## 9.3. The Absorption Law and Deviations from It

### 9.3.1. Derivation of the Absorption Law

**Definition 9.3.1** The ratio of the intensity $I$ of light transmitted through the sample to the intensity $I_0$ of the incident light, $\tau = I/I_0$, is called the **transmittance**, often expressed as a percentage. Absorbance and transmittance are related by $A = \lg(I_0/I) = -\lg\tau$.

Textbooks often write transmittance as $T$; to avoid confusion with the thermodynamic temperature and the period, this site uses the alternative notation $\tau$ of IUPAC and ISO 80000-7.

In [6.3.17](/6.3.17#def-17.2.3) the **Beer–Lambert law** was obtained directly from the statement that the fraction absorbed by a thin layer is proportional to the number of absorbing molecules. From the viewpoint of a single molecule, the proportionality coefficient has a definite physical meaning. Let parallel monochromatic light pass perpendicularly through a thin layer of cross-sectional area $S$ and thickness $\mathrm{d}x$ containing $\mathrm{d}n$ absorbing molecules. Each molecule can be regarded as a small target that "captures" photons, with an effective area $\sigma$ called the absorption cross section (equal to the geometric cross section of the molecule multiplied by the transition probability, in $\mathrm{cm^2}$). The total area of all targets in the thin layer is $\sigma\,\mathrm{d}n$ (the layer is so thin that the targets do not shade one another), and the probability that a photon is captured equals the fraction of the cross section occupied by this area:

$$
-\frac{\mathrm{d}I_x}{I_x} = \frac{\sigma\,\mathrm{d}n}{S}.
$$
At concentration $c$ ($\mathrm{mol\,L^{-1}}$) the number of molecules in a volume $S\,\mathrm{d}x$ ($\mathrm{cm^3}$) is $\mathrm{d}n = N_{\mathrm{A}}cS\,\mathrm{d}x/1000$; substituting and integrating over the path from $0$ to $b$ gives

$$
\ln\frac{I_0}{I} = \frac{\sigma N_{\mathrm{A}}}{1000}\,bc, \qquad A = \lg\frac{I_0}{I} = \varepsilon bc, \qquad \varepsilon = \frac{N_{\mathrm{A}}\sigma}{1000\ln 10} \approx 2.6\times10^{20}\,\sigma. \tag{9.1}
$$
Here the path length is written $b$ (in $\mathrm{cm}$; written $l$ in 6.3.17), and with $\sigma$ in $\mathrm{cm^2}$ the unit of $\varepsilon$ is $\mathrm{L\,mol^{-1}\,cm^{-1}}$. When the concentration is expressed as mass concentration $\rho$ ($\mathrm{g\,L^{-1}}$), one writes $A = abc$, where $a = \varepsilon/M$ is the mass absorption coefficient; biochemistry also often uses $A^{1\%}_{1\,\mathrm{cm}}$ (the absorbance of a $1\%$ solution in a $1\,\mathrm{cm}$ path). Equation (9.1) shows that $\varepsilon$ measures the light-absorbing ability of the molecule: for a fully allowed transition the absorption cross section of the molecule is about $10^{-15}\,\mathrm{cm^2}$ ($0.1\,\mathrm{nm^2}$, comparable to the size of a chromophore), corresponding to $\varepsilon \sim 10^5$; for a forbidden transition the transition probability is small and $\varepsilon$ is smaller by several orders of magnitude.

**Property 9.3.1 (Additivity)** When a solution contains several light-absorbing substances that do not interact, the total absorbance equals the sum of the absorbances of the components:

$$
A = \sum_i A_i = b\sum_i \varepsilon_i c_i. \tag{9.2}
$$
Additivity is the basis of simultaneous multicomponent determination (Section 9.5.2) and of subtracting the background with a blank solution: when the instrument is zeroed with a reference solution containing only solvent and reagents, what is measured is the absorbance of the analyte.

### 9.3.2. Deviations from the Absorption Law

The derivation of Eq. (9.1) implies several conditions: the incident light is monochromatic; the absorbing molecules do not interact and exist in only one form; the medium is homogeneous and does not scatter; and no light other than that transmitted reaches the detector. In actual measurements the calibration curve often bends toward the concentration axis at high concentrations (negative deviation), for three kinds of reasons.

Nonmonochromatic light: a monochromator delivers a band of wavelengths of finite width (the spectral bandwidth). Let the incident light consist of two wavelengths $\lambda_1$ and $\lambda_2$ of equal intensity, with molar absorption coefficients $\varepsilon_1$ and $\varepsilon_2$. The detector measures the total intensity:

$$
A = \lg\frac{I_{01} + I_{02}}{I_{01}\cdot 10^{-\varepsilon_1 bc} + I_{02}\cdot 10^{-\varepsilon_2 bc}} = \lg\frac{2}{10^{-\varepsilon_1 bc} + 10^{-\varepsilon_2 bc}}.
$$
$A$ is proportional to $c$ only if $\varepsilon_1 = \varepsilon_2$. For $\varepsilon_1 \ne \varepsilon_2$, $A \approx \frac{1}{2}(\varepsilon_1 + \varepsilon_2)bc$ at low concentration; at high concentration the more strongly absorbed wavelength is almost completely absorbed, the light transmitted is mainly the more weakly absorbed one, $A$ tends to $\varepsilon_{\min}bc + \lg 2$, and the slope of the calibration curve decreases (the figure below, left). One should therefore measure at the top of the absorption peak (where $\varepsilon$ varies most slowly with wavelength) and keep the spectral bandwidth much smaller than the width of the absorption band (usually no more than 1/10 of it).

Stray light: stray light is light not within the selected band that reaches the detector through scattering and reflection in the monochromator, and it is usually not absorbed by the sample. For a stray light intensity $I_{\mathrm{s}}$ the measured absorbance is

$$
A_{\mathrm{obs}} = \lg\frac{I_0 + I_{\mathrm{s}}}{I + I_{\mathrm{s}}},
$$
which tends to the constant $\lg(1 + I_0/I_{\mathrm{s}})$ when the sample absorbs very strongly ($I \ll I_{\mathrm{s}}$). With $0.1\%$ stray light the instrument cannot measure absorbances above about $3$; at the ends of the spectral range where the source energy is low and the detector insensitive (for example below $200\,\mathrm{nm}$) the fraction of stray light is larger and the deviation more severe.

![Negative deviations from the absorption law. Left: absorbance versus concentration when the incident light contains two wavelengths of equal intensity but different molar absorption coefficients; the plot is linear only when they are equal. Right: stray light makes the measured absorbance saturate at high absorbance](./plots/beer-deviations.py)

Chemical factors: if the analyte dissociates, associates, tautomerizes or interacts with the solvent, the various forms have different $\varepsilon$, and their proportions change with concentration, so $A$ is no longer proportional to the total concentration. A dichromate solution contains the equilibrium

$$
\ce{Cr2O7^2- + H2O <=> 2HCrO4- <=> 2CrO4^2- + 2H+},
$$
and dilution shifts it to the right; the absorption peak of $\ce{CrO4^2-}$ is at $372\,\mathrm{nm}$ and those of $\ce{Cr2O7^2-}$ near $350\,\mathrm{nm}$ and $450\,\mathrm{nm}$, so a calibration curve against total chromium concentration in an unbuffered solution bends. Controlling the pH (so that all chromium is present in one form) removes the deviation.

When two interconvertible light-absorbing species are at equilibrium, their absorption curves often cross at certain wavelengths:

**Definition 9.3.2** The wavelength at which two (or several) light-absorbing species that interconvert in a fixed stoichiometric relation have equal molar absorption coefficients is called an **isosbestic point**. At the isosbestic point the absorbance of the system depends only on the total concentration and not on the ratio of the species.

In a series of spectra of an acid–base indicator measured at different pH, all curves pass through the same point (figure in Section 9.5.4). A set of spectra with a clear isosbestic point is strong evidence that "only two light-absorbing species interconvert in the system"; drift of the isosbestic point indicates a third species (an intermediate, a by-product or a precipitate). The absorbance at the isosbestic point does not change with the degree of conversion and can be used as the wavelength for measuring the total concentration or as an internal reference.

High concentration and other factors: above about $0.01\,\mathrm{mol\,L^{-1}}$ the intermolecular distances shorten, the charge distributions of neighboring molecules affect one another, and $\varepsilon$ itself changes with concentration; the refractive index of the solution also changes with concentration, and strictly $\varepsilon$ contains a factor $n/(n^2+2)^2$. In a turbid sample light is scattered rather than absorbed and the apparent absorbance is too high; if the sample fluoresces, the transmitted light is too strong. The absorption law is thus a limiting law for dilute solutions, and quantitative analysis should be carried out within the linear range of the calibration curve.

### 9.3.3. The Lower Limit of Measurable Concentration

By Eq. (9.1), the upper limit of $\varepsilon$ is about $10^5\,\mathrm{L\,mol^{-1}\,cm^{-1}}$ (taking $\sigma \approx 10^{-15}\,\mathrm{cm^2}$ gives $2.6\times10^5$, and in practice it rarely exceeds $2\times10^5$).

**Example 9.3.1** If the instrument can reliably measure $1\%$ absorption ($\tau = 0.99$, $A = -\lg 0.99 = 0.0044$), with $b = 1\,\mathrm{cm}$ and $\varepsilon = 1\times10^5\,\mathrm{L\,mol^{-1}\,cm^{-1}}$, the lowest measurable concentration is

$$
c_{\min} = \frac{A}{\varepsilon b} = \frac{0.0044}{1\times10^5 \times 1} = 4.4\times10^{-8}\,\mathrm{mol\,L^{-1}}.
$$

This value is an order-of-magnitude estimate of the **limit of detection** of the method (it is determined by the lowest measurable absorbance and is often called the "theoretical sensitivity", but it is not the same thing as the **sensitivity** of [6.4.1](/6.4.1#def-1.8.2), which is the slope of the calibration curve). It shows that ordinary absorption photometry can hardly determine substances below $10^{-8}\,\mathrm{mol\,L^{-1}}$. The reason is that an absorption measurement must resolve a small difference between two large light intensities $I_0$ and $I$, so that fluctuations of the source become noise directly, whereas **fluorescence** measurement detects emitted light against a dark background and has a much lower detection limit ([6.4.10](/6.4.10#sec-10.2.1)). How this limit can be overcome is the subject of Question 1 of this chapter.

## 9.4. Spectrophotometers and Measurement Error

### 9.4.1. Components of the Instrument

An ultraviolet–visible spectrophotometer consists of a source, a monochromator, an absorption cell, a detector and a signal processing system; the general principles of the components are in [6.4.7](/6.4.7#sec-7.1.3).

- Source: in the visible and near-infrared a tungsten or tungsten–halogen lamp is used (about $320$–$2500\,\mathrm{nm}$; the iodine or bromine in a tungsten–halogen lamp redeposits evaporated tungsten on the filament, giving longer life and higher brightness); in the ultraviolet a deuterium lamp (about $160$–$380\,\mathrm{nm}$; the continuous spectrum arises from the electronic excitation and dissociation of $\ce{D2}$ molecules, and a deuterium lamp is 3–5 times brighter than the early hydrogen lamp). The two lamps switch automatically between $320$ and $360\,\mathrm{nm}$. Some instruments use a pulsed xenon lamp ($190$–$1100\,\mathrm{nm}$), which emits only at the instant of measurement, so that it has a long life and the sample is not irradiated continuously.
- Monochromator: mainly gratings (prisms are now little used). The spectral bandwidth is generally $0.5$–$2\,\mathrm{nm}$ and should be less than 1/10 of the half-width of the absorption band (Section 9.3.2).
- Absorption cell (cuvette): quartz (fused silica, transparent down to about $190\,\mathrm{nm}$) is required in the ultraviolet; optical glass ($\ge 350\,\mathrm{nm}$) or plastic can be used in the visible; the standard path length is $1\,\mathrm{cm}$, and others of $0.1$–$10\,\mathrm{cm}$ exist. A pair of cells should have matched transmittance, and care must be taken to keep the optical faces clean and to orient the cells correctly.
- Detector: the **photomultiplier tube** (sensitive, used in scanning instruments), the silicon photodiode, and the photodiode array (PDA) of hundreds to thousands of photodiodes or the **charge-coupled device** (multichannel detection, measuring the whole spectrum simultaneously).

### 9.4.2. Single-Beam, Double-Beam and Diode-Array Instruments

Single-beam spectrophotometer: one beam of light passes in turn through the reference solution (set to $\tau = 100\%$, that is, measuring $I_0$) and the sample solution (measuring $I$). The design is simple and the energy high, but the instrument must be rezeroed with the reference at every change of wavelength, so automatic scanning of spectra is difficult, and any drift of the source and detector between the two measurements becomes an error directly.

Double-beam spectrophotometer: the monochromatic light is divided into two beams by a rotating sector mirror (chopper) or a beam splitter, which pass alternately (or simultaneously) through the reference cell and the sample cell, and the detector measures the ratio of the two intensities. It needs no swapping of cells back and forth, slow drifts of source intensity and detector sensitivity are compensated simultaneously, and absorption spectra can be scanned quickly and automatically; it is the mainstream of general-purpose instruments. Like the single-beam instrument, however, it cannot eliminate background absorption of the sample solution itself (turbidity, absorption by coexisting substances), which requires the dual-wavelength method (Section 9.4.3).

Diode-array spectrophotometer: it uses a "reversed optical path": the polychromatic light first passes through the sample and is then dispersed by a grating onto the array detector, so that all wavelengths are measured simultaneously and a whole spectrum is obtained within a second. It has no moving parts and suits fast reaction kinetics, flow systems and the diode-array detector of high-performance liquid chromatography ([6.4.14](/6.4.14#sec-14.1.4)).

### 9.4.3. Dual-Wavelength Spectrophotometry

**Definition 9.4.1** A method of quantitative analysis in which two monochromators provide monochromatic light of wavelengths $\lambda_1$ and $\lambda_2$, a chopper makes them pass alternately through the same cell, and the difference of the absorbances at the two wavelengths, $\Delta A = A_{\lambda_2} - A_{\lambda_1}$, is measured, is called **dual-wavelength spectrophotometry**.

It uses only one cell and needs no reference solution. Let the absorption spectra of the analyte component a and an interfering component i overlap:

$$
A_{\lambda_1} = \varepsilon^{\mathrm{a}}_{\lambda_1}bc_{\mathrm{a}} + A^{\mathrm{i}}_{\lambda_1}, \qquad A_{\lambda_2} = \varepsilon^{\mathrm{a}}_{\lambda_2}bc_{\mathrm{a}} + A^{\mathrm{i}}_{\lambda_2}.
$$
Choose two wavelengths at which the interfering component has equal absorbance ($A^{\mathrm{i}}_{\lambda_1} = A^{\mathrm{i}}_{\lambda_2}$) and at which the absorption of the analyte differs as much as possible (usually $\lambda_2$ is taken at the absorption peak of the analyte); then

$$
\Delta A = (\varepsilon^{\mathrm{a}}_{\lambda_2} - \varepsilon^{\mathrm{a}}_{\lambda_1})bc_{\mathrm{a}} \propto c_{\mathrm{a}}, \tag{9.3}
$$
and the influence of the interfering component is eliminated completely. Likewise, scattering by a turbid sample and the background absorption $A_{\mathrm{b}}$ of the cell and the solution are approximately equal at two nearby wavelengths and cancel in $\Delta A$: the dual-wavelength method is suited to the determination of turbid liquids (whole blood, suspended cells, tissue homogenates) and of samples with background absorption.

### 9.4.4. Derivative Spectra

**Definition 9.4.2** The curve of the derivative of the absorbance with respect to wavelength, $\mathrm{d}^nA/\mathrm{d}\lambda^n$, plotted against wavelength is called the ($n$th-order) **derivative spectrum**, and the method of qualitative and quantitative analysis that uses it is called derivative spectrophotometry.

From $A = \varepsilon bc$, $\frac{\mathrm{d}^nA}{\mathrm{d}\lambda^n} = \frac{\mathrm{d}^n\varepsilon}{\mathrm{d}\lambda^n}bc$, so the derivative remains proportional to the concentration. Its properties are as follows.

1. An absorption peak of the zeroth-order spectrum corresponds to a zero of the first derivative and a minimum of the second derivative; a shoulder, inconspicuous in the zeroth-order spectrum, becomes a clear extremum in the derivative spectrum and can be used to locate overlapping peaks.
2. The sensitivity depends on $\mathrm{d}^n\varepsilon/\mathrm{d}\lambda^n$: the first derivative has its largest absolute value at the inflection point of the absorption curve (where the slope is greatest).
3. For an absorption band of width $w$ the amplitude of the $n$th derivative is roughly proportional to $1/w^n$: differentiation amplifies narrow bands and suppresses broad ones. Slowly varying backgrounds (scattering, broad interfering absorption) almost vanish in higher derivatives, and two heavily overlapping absorption bands may even be resolved.

Derivatives are obtained by instrument circuitry or by numerical differentiation of the digitized spectrum. Differentiation amplifies high-frequency noise, so in practice the spectrum is smoothed before differentiation (Savitzky–Golay filtering, that is, fitting a polynomial to the points in a sliding window by the method of **least squares** and differentiating it; `scipy.signal.savgol_filter`). Second- and fourth-derivative spectra are often used for the separate determination of the main component and excipients in pharmaceutical preparations, and for distinguishing the absorption bands of phenylalanine, tyrosine and tryptophan in proteins.

### 9.4.5. Measurement Error and the Optimal Absorbance Range

Even with ideal instruments and reagents, the reading of absorbance itself has an error. If the main error of the instrument is a constant absolute error $\Delta\tau$ in the reading of the transmittance (the reading error of phototube and galvanometer instruments, or when dark current and amplifier noise dominate), differentiating $c = -\lg\tau/(\varepsilon b)$ gives

$$
\mathrm{d}c = -\frac{0.4343}{\varepsilon b}\frac{\mathrm{d}\tau}{\tau}, \qquad \frac{\Delta c}{c} = \frac{0.4343\,\Delta\tau}{\tau\lg\tau}. \tag{9.4}
$$
The relative error of the concentration is large both when $\tau$ is very large (too little absorption) and when $\tau$ is very small (almost opaque). Setting $\frac{\mathrm{d}}{\mathrm{d}\tau}(\tau\lg\tau) = \lg\tau + \lg\mathrm{e} = 0$ gives $\tau = 1/\mathrm{e} = 0.368$, that is, the relative error is smallest at

$$
A = \lg\mathrm{e} = 0.434.
$$

**Example 9.4.1** Let $\Delta\tau = \pm 0.005$. At $A = 0.434$, $|\Delta c/c| = \frac{0.4343\times0.005}{0.368\times0.434} = 1.36\%$; at $A = 0.2$ ($\tau = 0.631$) and at $A = 0.8$ ($\tau = 0.158$) it is about $1.7\%$ in both cases; and at $A = 1.5$ it rises to $4.6\%$. In measurements one therefore adjusts the sample concentration or the path length of the cell so that the absorbance falls between $0.2$ and $0.8$.

The conclusion $A = 0.434$ depends on the premise that $\Delta\tau$ is constant. The photomultiplier tubes or photodiodes of modern instruments are often limited by photon shot noise, and the standard deviation of the transmittance is roughly proportional to $\sqrt{\tau^2 + \tau}$; the optimal absorbance then moves to about $0.96$, and the error remains modest even at $A$ of $1.5$–$2$; at the high-absorbance end, what finally limits the measurement is stray light (Section 9.3.2). For samples of high concentration whose absorbance lies outside the range, a standard solution of slightly lower concentration can be used as the reference in place of the blank (differential spectrophotometry), which amounts to expanding the transmittance scale.

![Relative error in concentration versus absorbance: for a constant transmittance reading error (Δτ = 0.005) the minimum lies at A = 0.434, and when limited by shot noise it moves to A ≈ 0.96; the shaded band is the commonly used range 0.2–0.8](./plots/photometric-error.py)

## 9.5. Quantitative Methods and Applications

### 9.5.1. Single-Component Determination and Color-Forming Reactions

Single components are determined with a **calibration curve** ([6.4.1](/6.4.1#sec-1.8.1)): a series of standard solutions is prepared, the absorbance is measured at the chosen wavelength and plotted against concentration, a line is fitted by **least squares**, and the concentration is found from the absorbance of the sample. The slope $\varepsilon b$ of the calibration curve is the **sensitivity** of the method ([6.4.1](/6.4.1#def-1.8.2)), which for a fixed path length is determined by the molar absorption coefficient. The measuring conditions are chosen as follows.

- **Wavelength**: generally $\lambda_{\max}$ (the highest sensitivity, and $\varepsilon$ varies most slowly with wavelength, so deviations due to nonmonochromatic light are smallest); if a coexisting substance interferes at $\lambda_{\max}$, another wavelength is chosen on the principle of "maximum absorption of the analyte, minimum of the interference".
- Reference solution: when both sample and color-forming reagent are colorless, the solvent (distilled water) is used as the reference; when the reagent is colored, a reagent blank (without sample, otherwise identical); when the sample itself is colored, a sample blank (without color-forming reagent). The reference solution removes the absorption of the cell, solvent, reagents and matrix, and amounts to a **blank determination**.
- Color-forming reaction: most inorganic ions absorb weakly in the ultraviolet–visible, and are first converted by a color-forming reagent into colored compounds of large $\varepsilon$. The reaction must be selective and sensitive ($\varepsilon \ge 10^4$), the product must have constant composition and be stable, and its color must differ greatly from that of the reagent ($\Delta\lambda_{\max} \ge 60\,\mathrm{nm}$); the amount of reagent, the acidity (which affects the formation of the complex and the color of the reagent itself, for the same reason as the acid effect in [6.4.3](/6.4.3#def-3.2.3)), the temperature and the time of color development must be controlled, and masking agents are used to eliminate interfering ions. For example, $\ce{Fe^2+}$ forms $\ce{[Fe(phen)3]^2+}$ ($510\,\mathrm{nm}$) with 1,10-phenanthroline at pH 2–9, and reducing $\ce{Fe^3+}$ to $\ce{Fe^2+}$ with hydroxylamine hydrochloride first allows total iron to be determined.

### 9.5.2. Simultaneous Determination of Several Components

When the absorption spectra of several components overlap, additivity of absorbance (9.2) allows one to measure the absorbance $A_i$ of the mixture at $m$ wavelengths, giving the **system of linear equations**

$$
A_i = b\sum_{j=1}^{k}\varepsilon_{ij}c_j, \quad i = 1, \dots, m, \qquad \text{that is,} \quad \boldsymbol{A} = bE\boldsymbol{c},
$$
where $\varepsilon_{ij}$ is the molar absorption coefficient of component $j$ at wavelength $\lambda_i$, determined from standard solutions of the pure components. For $m = k$ the system is simply solved; to reduce the influence of measurement error one usually measures at more wavelengths ($m > k$) and uses **least squares**, $\boldsymbol{c} = (E^{\mathsf T}E)^{-1}E^{\mathsf T}\boldsymbol{A}/b$ (the matrix method of [3.3.7](/3.3.7#sec-7.3.1)). The wavelengths should be chosen where the absorptions of the components differ greatly; otherwise the matrix $E$ is nearly singular and errors are amplified.

**Example 9.5.1** In $1\,\mathrm{mol\,L^{-1}}$ $\ce{H2SO4}$, the molar absorption coefficients of $\ce{Cr2O7^2-}$ and $\ce{MnO4-}$ are $369$ and $95\,\mathrm{L\,mol^{-1}\,cm^{-1}}$ at $440\,\mathrm{nm}$ and $11$ and $2350\,\mathrm{L\,mol^{-1}\,cm^{-1}}$ at $545\,\mathrm{nm}$. A mixed solution measured in a $1\,\mathrm{cm}$ cell gives $A_{440} = 0.393$ and $A_{545} = 0.598$. Find the two concentrations.

```python
import numpy as np

# rows: 440 nm, 545 nm; columns: Cr2O7(2-), MnO4(-); units L mol^-1 cm^-1
E = np.array([[369.0, 95.0],
              [11.0, 2350.0]])
A = np.array([0.393, 0.598])      # b = 1 cm
c = np.linalg.solve(E, A)
print(c)                          # [1.0007e-03 2.4978e-04] mol/L

# with more wavelengths than components, use least squares instead:
# c, *_ = np.linalg.lstsq(E_many, A_many, rcond=None)
```

The result is $c(\ce{Cr2O7^2-}) = 1.00\times10^{-3}\,\mathrm{mol\,L^{-1}}$ and $c(\ce{MnO4-}) = 2.50\times10^{-4}\,\mathrm{mol\,L^{-1}}$. Modern instruments record the whole spectrum and determine several components simultaneously by multivariate calibration of the full spectrum (classical least squares, partial least squares); the principle is the same, only the number of equations is far larger than the number of unknowns.

### 9.5.3. Determination of the Composition of Complexes

Spectrophotometry is the classical method for determining the composition (stoichiometric ratio) and stability constant of complexes in solution. Let the reaction be $m\ce{M} + n\ce{R} \ce{<=>} \ce{M_mR_n}$, with only the complex absorbing at the wavelength of measurement (or the absorption of M and R subtracted).

**Definition 9.5.1** The method in which the concentration $c_{\mathrm{M}}$ of the metal ion is held fixed, the concentration $c_{\mathrm{R}}$ of the ligand is increased progressively, the absorbance $A$ is plotted against $c_{\mathrm{R}}/c_{\mathrm{M}}$, and the stoichiometric ratio is found from the concentration ratio at the break of the curve is called the **mole-ratio method**.

For $c_{\mathrm{R}}/c_{\mathrm{M}} < n/m$, M is not completely complexed and $A$ increases linearly as R is added; beyond $n/m$ all of M has been converted and $A$ no longer increases. The intersection of the two extrapolated straight lines gives the stoichiometric ratio. If the complex is stable the break is sharp; if it is less stable, the complex partly dissociates near the equivalence point, the break is rounded, and this deviation can be used to find the stability constant. At the break ($c_{\mathrm{R}}/c_{\mathrm{M}} = n/m$) let the concentration of the complex if it did not dissociate at all be $c$ and the corresponding absorbance $A_0$ (obtained by extrapolating the two straight lines), and the measured absorbance $A'$; then the degree of dissociation of the complex is $\alpha = (A_0 - A')/A_0$, the equilibrium concentrations are $[\ce{M_mR_n}] = (1-\alpha)c$, $[\ce{M}] = m\alpha c$ and $[\ce{R}] = n\alpha c$, and the dissociation constant (instability constant) of the complex is

$$
K_{\mathrm{d}} = \frac{1}{\beta} = \frac{[\ce{M}]^m[\ce{R}]^n}{[\ce{M_mR_n}]} = \frac{(m\alpha c)^m(n\alpha c)^n}{(1-\alpha)c} = \frac{m^mn^n\alpha^{m+n}c^{m+n-1}}{1-\alpha}. \tag{9.5}
$$

**Example 9.5.2** For a 1:1 complex, at the break $c = 1.0\times10^{-4}\,\mathrm{mol\,L^{-1}}$, the extrapolated $A_0 = 0.500$ and the measured $A' = 0.450$. Then $\alpha = 0.10$, $K_{\mathrm{d}} = \alpha^2c/(1-\alpha) = 1.1\times10^{-6}$, and the **stability constant** is $\beta = 9.0\times10^5$ ($\lg\beta = 5.95$).

**Definition 9.5.2** The method in which the total concentration $c_{\mathrm{M}} + c_{\mathrm{L}}$ of metal ion and ligand is held constant while the proportion of the two (the mole fraction of the ligand, $x = c_{\mathrm{L}}/(c_{\mathrm{M}} + c_{\mathrm{L}})$) is varied, the absorbance is plotted against $x$, and the stoichiometric ratio is found from the position of the maximum is called the **method of continuous variations** (Job's method).

For a complex $\ce{ML_n}$, if the complex forms completely its concentration is $\min(c_{\mathrm{M}}, c_{\mathrm{L}}/n)$, which is largest at $c_{\mathrm{L}} = nc_{\mathrm{M}}$, that is, at

$$
x_{\max} = \frac{n}{n+1}
$$
(for a 1:1 complex at $x = 0.5$, for a 1:2 complex at $x = 2/3$); it can be shown that when the complex does not form completely the maximum remains at this position and only the peak is rounded, in which case it is located from the intersection of the tangents on both sides. The method of continuous variations requires that a single complex predominate in the solution; for systems in which several complexes coexist with similar stepwise stability constants, both methods give only average results, and global fitting of multiwavelength data is needed. There are also the slope-ratio method (two calibration curves with a large excess of metal or of ligand respectively, the stoichiometric ratio being found from the ratio of the slopes) and the equilibrium-shift method (plotting $\lg\frac{A}{A_{\max} - A}$ against $\lg c_{\mathrm{L}}$, the slope being the coordination number), whose principles are similar.

![The method of continuous variations (Job's method): total concentration 1.0×10⁻³ mol/L, only the complex absorbs; the maximum is at x = 1/2 for ML and at x = 2/3 for ML₂; for a smaller stability constant the peak is rounded but its position is unchanged](./plots/job-plot.py)

### 9.5.4. Determination of Acid Dissociation Constants

When the absorption spectra of an acid HB and its conjugate base $\ce{B-}$ differ (as for $p$-nitrophenol in Section 9.2.3), $\mathrm{p}K_{\mathrm{a}}$ can be determined spectrophotometrically. A series of solutions of the same total concentration $c$ and different pH is prepared, and the absorbance is measured at a given wavelength (usually an absorption peak of $\ce{B-}$ or HB) with $b = 1\,\mathrm{cm}$:

$$
A = \varepsilon_{\mathrm{HB}}[\ce{HB}] + \varepsilon_{\mathrm{B}}[\ce{B-}], \qquad c = [\ce{HB}] + [\ce{B-}].
$$
In strongly acidic solution the acid is entirely HB and $A_{\mathrm{HB}} = \varepsilon_{\mathrm{HB}}c$ is measured; in strongly basic solution it is entirely $\ce{B-}$ and $A_{\mathrm{B}} = \varepsilon_{\mathrm{B}}c$ is measured. Solving the two equations above gives

$$
[\ce{HB}] = \frac{A_{\mathrm{B}} - A}{\varepsilon_{\mathrm{B}} - \varepsilon_{\mathrm{HB}}}, \qquad [\ce{B-}] = \frac{A - A_{\mathrm{HB}}}{\varepsilon_{\mathrm{B}} - \varepsilon_{\mathrm{HB}}},
$$
and substitution into $K_{\mathrm{a}} = [\ce{H+}][\ce{B-}]/[\ce{HB}]$ gives

$$
\mathrm{p}K_{\mathrm{a}} = \mathrm{pH} + \lg\frac{A_{\mathrm{B}} - A}{A - A_{\mathrm{HB}}}. \tag{9.6}
$$
This is the **Henderson–Hasselbalch equation** in the form of absorbances. A measurement at a single pH suffices to calculate $\mathrm{p}K_{\mathrm{a}}$; a more reliable procedure is to measure a series of pH values and plot $\lg\frac{A - A_{\mathrm{HB}}}{A_{\mathrm{B}} - A}$ against pH (a straight line of slope 1 and intercept $-\mathrm{p}K_{\mathrm{a}}$), or to fit the sigmoidal $A$–pH curve directly by nonlinear **least squares** (`scipy.optimize.curve_fit`, [4.4.4](/4.4.4#sec-4.2.3)). The constant obtained in this way is the **concentration equilibrium constant** at a given ionic strength ([6.4.2](/6.4.2#sec-2.2.2)), which can be converted to the thermodynamic constant with activity coefficients if required. The method needs only about $10^{-5}\,\mathrm{mol\,L^{-1}}$ of substance and suits sparingly soluble or expensive compounds (drugs, chromophores in proteins); it is also used to determine the $\mathrm{p}K_{\mathrm{a}}$ of acid–base indicators.

![Photometric determination of p-nitrophenol (pKa = 7.15, c = 5.0×10⁻⁵ mol/L) (simulated data). Left: absorption spectra at different pH, acid form at 317 nm and base form at 400 nm; all curves pass through the isosbestic point at about 348 nm. Right: absorbance at 400 nm against pH, fitted with Eq. (9.6) by curve_fit](./plots/pka-isosbestic.py)

### 9.5.5. Photoacoustic Spectroscopy and Long-Path Absorption

Two techniques extend the range of absorption measurements.

- Photoacoustic spectroscopy: a sample in a closed cell is irradiated with intensity-modulated light (a chopped beam or a pulsed laser); the sample absorbs the light energy and converts it to heat by nonradiative relaxation, the periodic thermal expansion produces sound waves, and they are detected by a sensitive microphone (or piezoelectric transducer). The signal is proportional to the absorbed light energy and independent of the transmitted light, so samples whose transmission cannot be measured, such as powders, solids, turbid liquids and biological tissue, can be measured, as can very weak absorptions (the photoacoustic effect was discovered by Bell in 1880). In biomedical photoacoustic imaging, absorption by hemoglobin and other chromophores in tissue generates ultrasound signals, and blood vessels at a depth of several centimeters can be imaged.
- Long-path absorption cells: by Eq. (9.1) absorbance is proportional to the path length. With liquid-core waveguide capillaries whose inner walls have a high reflectivity (the wall material has a refractive index lower than that of water, so light propagates in the liquid core by total reflection), path lengths of several meters are possible, and with laser sources nutrients and trace metals in seawater can be measured at the $\mathrm{nmol\,L^{-1}}$ level; in gas analysis multipass cells and cavity ring-down spectroscopy extend the effective path to kilometers.

## 9.6. Surface Plasmon Resonance and Circular Dichroism

### 9.6.1. Surface Plasmon Resonance

The collective oscillation of free electrons in a metal is called a plasma oscillation. At the interface between a metal and a dielectric (glass, water), the oscillation of electron density can couple to an electromagnetic wave, forming a surface electromagnetic wave that propagates along the interface and decays exponentially in the direction perpendicular to it, the surface plasmon polariton. Its wavevector

$$
k_{\mathrm{sp}} = \frac{\omega}{c}\sqrt{\frac{\varepsilon_{\mathrm{m}}n_{\mathrm{s}}^2}{\varepsilon_{\mathrm{m}} + n_{\mathrm{s}}^2}}
$$
($\varepsilon_{\mathrm{m}}$ is the relative permittivity of the metal, a negative number of large absolute value for gold and silver in the visible; $n_{\mathrm{s}}$ is the **refractive index** of the dielectric; $c$ is the speed of light in vacuum) is larger than the wavevector $n_{\mathrm{s}}\omega/c$ of light of the same frequency in the dielectric, so light shining directly on the metal surface from the dielectric side cannot excite it, and a prism or grating is needed to supply the extra wavevector.

The most common arrangement is the Kretschmann configuration: a gold film of about $50\,\mathrm{nm}$ is deposited on the base of a prism of high refractive index $n_{\mathrm{p}}$, and the other side of the gold film is in contact with the sample solution. p-Polarized light is incident on the base inside the prism at an angle $\theta$ larger than the critical angle, and **total internal reflection** occurs; the evanescent wave at the interface passes through the very thin gold film, and its wavevector component parallel to the interface is $k_x = \frac{\omega}{c}n_{\mathrm{p}}\sin\theta$. When $k_x = \operatorname{Re}k_{\mathrm{sp}}$, the energy of the light is transferred to the surface plasmon and the reflected intensity drops sharply.

**Definition 9.6.1** The resonance phenomenon in which incident light that satisfies the wavevector-matching condition excites surface plasmons at a metal–dielectric interface and the reflected intensity shows a sharp minimum at a certain angle of incidence (or wavelength) is called **surface plasmon resonance** (SPR); the angle of incidence at minimum reflectance is called the resonance angle (SPR angle). The localized oscillation of electrons in metal nanoparticles excited directly by light is called localized surface plasmon resonance (LSPR, Section 9.6.3).

The electric field of the surface plasmon decays exponentially from the gold surface into the solution, with a decay length of about $200\,\mathrm{nm}$, so the resonance angle is sensitive only to the refractive index of a thin layer near the gold surface. When biomolecules bind to the surface, the refractive index of this layer increases and the resonance angle shifts; for proteins, the shift of the resonance angle is approximately proportional to the mass concentration of bound material on the surface. Commercial instruments express the resonance signal in response units RU, with $1\,\mathrm{RU}$ corresponding to a refractive index change of about $10^{-6}$, that is, about $1\,\mathrm{pg\,mm^{-2}}$ of protein.

The history of the phenomenon: Wood observed anomalous dark bands in the reflection spectra of metal gratings in 1902; Ritchie proposed the surface plasmon theoretically in 1957; Otto and Kretschmann proposed excitation by attenuated total reflection in a prism in 1968; Liedberg and coworkers first applied SPR to immunosensing in 1983, and commercial SPR biosensors appeared in 1990.

### 9.6.2. SPR Biosensing and Binding Kinetics

SPR is the most widely used label-free method for analyzing molecular interactions. One molecule (the ligand, such as an antibody, a receptor protein or DNA) is immobilized on the dextran or self-assembled monolayer on the gold film, the other (the analyte, such as an antigen or a drug molecule) flows over the surface in buffer, and the change of the response with time, the sensorgram, is recorded in real time. A cycle consists of baseline, association (injection of the analyte), dissociation (switching back to buffer) and regeneration (washing off the bound material with acid, base or high salt). It needs no fluorescent or radioactive label and no separation of free from bound molecules, and gives the association and dissociation rate constants directly; it is widely used in antibody screening, drug–target interactions ([6.6](/6.6)) and fragment-based drug discovery. As a **biosensor** ([6.4.6](/6.4.6#def-6.7.2)), its recognition element is the immobilized ligand and its transducer is the SPR optical system.

For the simplest 1:1 binding $\ce{A + B <=> AB}$ (A the analyte at constant concentration $c$, B the ligand on the surface), the response $R$ is proportional to $[\ce{AB}]$, and the maximum response $R_{\max}$ corresponds to all ligand being occupied:

$$
\frac{\mathrm{d}R}{\mathrm{d}t} = k_{\mathrm{a}}c(R_{\max} - R) - k_{\mathrm{d}}R. \tag{9.7}
$$
Since the analyte flows in continuously and its concentration is constant, the association phase is a **pseudo-first-order reaction**, and integration from $R(0) = 0$ gives

$$
R(t) = R_{\mathrm{eq}}\left(1 - \mathrm{e}^{-k_{\mathrm{obs}}t}\right), \qquad k_{\mathrm{obs}} = k_{\mathrm{a}}c + k_{\mathrm{d}}, \qquad R_{\mathrm{eq}} = \frac{R_{\max}c}{c + K_{\mathrm{D}}};
$$
in the dissociation phase ($c = 0$) $R(t) = R_0\mathrm{e}^{-k_{\mathrm{d}}(t - t_0)}$. The equilibrium dissociation constant is $K_{\mathrm{D}} = k_{\mathrm{d}}/k_{\mathrm{a}}$. Measuring several concentrations, one plots $k_{\mathrm{obs}}$ against $c$ as a straight line (slope $k_{\mathrm{a}}$, intercept $k_{\mathrm{d}}$), or fits all sensorgrams globally by nonlinear regression, obtaining $k_{\mathrm{a}}$, $k_{\mathrm{d}}$ and $K_{\mathrm{D}}$ together; fitting a Langmuir-type binding isotherm to the values of $R_{\mathrm{eq}}$ at different concentrations gives $K_{\mathrm{D}}$ independently. Of two drugs with the same $K_{\mathrm{D}}$, the one that dissociates more slowly (smaller $k_{\mathrm{d}}$, longer residence time $1/k_{\mathrm{d}}$) often acts for longer in vivo, which is information that equilibrium measurements cannot provide. Real data must also account for mass-transport limitation of the analyte to the surface, nonspecific adsorption and multivalent binding, which make the sensorgram deviate from a single exponential.

![SPR sensorgram (simulated data): 1:1 binding with ka = 1.0×10⁵ L mol⁻¹ s⁻¹ and kd = 1.0×10⁻³ s⁻¹ (KD = 10 nmol/L); analyte is injected at five concentrations during 0–300 s, followed by buffer for dissociation; the curves are a global least-squares fit of the five sensorgrams](./plots/spr-sensorgram.py)

### 9.6.3. Localized Surface Plasmon Resonance

In gold and silver nanoparticles much smaller than the wavelength of light, the electric field of the light drives the free electrons of the whole particle to oscillate collectively against the lattice of positive ions, giving strong absorption and scattering at the resonance frequency. For spherical gold nanoparticles of diameter about $10$–$20\,\mathrm{nm}$ the LSPR absorption peak is at about $520\,\mathrm{nm}$ and $\varepsilon$ can reach $10^8$–$10^9\,\mathrm{L\,mol^{-1}\,cm^{-1}}$ (per particle), so gold sols are wine red. The resonance wavelength varies with the size and shape of the particles (nanorods have two resonances, transverse and longitudinal, the latter tunable into the near-infrared), the refractive index of the surrounding medium and the interparticle distance:

- When particles aggregate, the plasmons of neighboring particles couple, the absorption peak shifts to the red and broadens, and the solution changes from red to purple-blue. Gold nanoparticles modified with oligonucleotides aggregate on hybridization with target DNA, giving a nucleic acid assay whose color change can be seen directly; the red line on lateral-flow test strips (pregnancy tests, rapid antigen tests) is likewise gold nanoparticles captured by antibodies.
- The local electric field near the particle is greatly enhanced, which is the basis of **surface-enhanced Raman scattering** ([6.4.11](/6.4.11#def-11.5.8)).

The Roman Lycurgus Cup (4th century AD) contains gold–silver alloy nanoparticles and appears green in reflected light and red in transmitted light, the earliest (unwitting) use of LSPR by humankind; the red of medieval stained glass in churches likewise comes from gold nanoparticles.

### 9.6.4. Circular Dichroism

**Linearly polarized light** can be decomposed into **circularly polarized light** of equal amplitude and opposite senses of rotation, left and right ([5.4.3](/5.4.3#sec-3.1.3)). **Chiral** molecules have different refractive indices for the two (this is **optical activity**, [5.4.3](/5.4.3#sec-3.9)) and, within an absorption band, absorb them differently.

**Definition 9.6.2** The property of a chiral substance that its molar absorption coefficients for left- and right-circularly polarized light are unequal is called circular dichroism; the spectrum obtained by plotting $\Delta\varepsilon = \varepsilon_{\mathrm{L}} - \varepsilon_{\mathrm{R}}$ (or the ellipticity, which is proportional to it) against wavelength is called the **circular dichroism** spectrum (CD spectrum).

Because the two circular components are absorbed to different extents, the two components of the transmitted light no longer have equal amplitudes, and the resultant is **elliptically polarized light**. The arctangent of the ratio of the minor to the major axis of the ellipse is called the ellipticity $\theta$. For small $\Delta A = A_{\mathrm{L}} - A_{\mathrm{R}}$, $\theta = \frac{\ln 10}{4}\Delta A$ (in radians), that is, $\theta/\mathrm{deg} = 32.98\,\Delta A$.

**Definition 9.6.3** The ellipticity normalized by the amount-of-substance concentration is called the **molar ellipticity**:

$$
[\theta] = \frac{100\,\theta}{cb}, \qquad [\theta] = 3298\,\Delta\varepsilon, \tag{9.8}
$$
where $\theta$ is in degrees, $c$ in $\mathrm{mol\,L^{-1}}$ and the path length $b$ in $\mathrm{cm}$, and $[\theta]$ is in $\mathrm{deg\,cm^2\,dmol^{-1}}$ ($\Delta\varepsilon$ in $\mathrm{L\,mol^{-1}\,cm^{-1}}$).

$\Delta\varepsilon$ can be positive or negative, so circular dichroism spectra have both positive and negative peaks; the CD spectra of a pair of **enantiomers** are mirror images. CD appears only within the absorption bands of chiral molecules and reflects the asymmetric environment of the chromophore better than the ordinary absorption spectrum, and it is used to infer the absolute configuration and conformation of organic molecules. The variation of optical rotation with wavelength (optical rotatory dispersion, ORD) shows an S-shaped anomaly near an absorption band (the Cotton effect); it and CD are the dispersive and absorptive aspects of the same phenomenon, related by the Kramers–Kronig relations, and modern work uses mainly CD.

A circular dichroism spectrometer uses a photoelastic modulator to switch between left- and right-circularly polarized light at about $50\,\mathrm{kHz}$ and detects the alternating component of the transmitted intensity. $\Delta A$ is typically only $10^{-5}$–$10^{-3}$, three to four orders of magnitude smaller than $A$, so a high light flux is required: far-ultraviolet measurements are made under a nitrogen purge (oxygen absorbs below $200\,\mathrm{nm}$), with a short path ($0.1$–$1\,\mathrm{mm}$) and weakly absorbing buffers (phosphate, fluoride; high concentrations of chloride, imidazole and Tris are to be avoided).

### 9.6.5. Circular Dichroism of Proteins and Nucleic Acids

In the far ultraviolet ($180$–$250\,\mathrm{nm}$) the CD of proteins arises from the $\mathrm{n}\to\pi^*$ and $\pi\to\pi^*$ transitions of the peptide bond. The peptide bond itself is not chiral, but in regular secondary structures many peptide bonds are arranged in a chiral geometry, their transitions couple, and a characteristic CD spectrum results (the molar ellipticity being calculated per mean residue concentration):

| Secondary structure | Positive peak | Negative peak |
|---|---|---|
| α helix | $192\,\mathrm{nm}$ (strong) | $208\,\mathrm{nm}$ and $222\,\mathrm{nm}$ (double negative peak, $[\theta]_{222} \approx -3.5\times10^4\,\mathrm{deg\,cm^2\,dmol^{-1}}$) |
| β sheet | $195$–$198\,\mathrm{nm}$ | $215$–$218\,\mathrm{nm}$ (weaker) |
| Random coil | About $218\,\mathrm{nm}$ (very weak) | About $198\,\mathrm{nm}$ (strong) |

![Far-ultraviolet CD spectra of the three basic secondary structures (schematic, based on the positions of the characteristic peaks): the α helix has a double negative peak at 208 and 222 nm and a strong positive peak at 192 nm; the β sheet has a negative peak at about 217 nm; the random coil has a strong negative peak at about 198 nm](./plots/cd-secondary-structure.py)

The CD spectrum of a protein is approximately a linear combination of the reference spectra of the various secondary structures weighted by their contents; decomposing it by **least squares** (or constrained fitting algorithms such as CONTIN and BeStSel) gives the contents of α helix, β sheet and so on, the estimate of α-helix content being fairly accurate and those of β sheet and turns rougher. CD needs only some tens of micrograms of protein and a few minutes of measurement and does not require crystallization, and is therefore often used to confirm that a recombinant protein is correctly folded, to compare mutants with the wild type, and to follow $[\theta]$ at $222\,\mathrm{nm}$ as a function of temperature or denaturant concentration to obtain unfolding curves and thermal stability. The CD in the near ultraviolet ($250$–$320\,\mathrm{nm}$) arises from the asymmetric environment of aromatic side chains and disulfide bonds and reflects the tertiary structure.

The CD of nucleic acids arises from the helical stacking of the bases: B-form DNA has a positive peak at about $275\,\mathrm{nm}$ and a negative peak at $245\,\mathrm{nm}$; the A form (double-stranded RNA) has a strong positive peak at $260\,\mathrm{nm}$ and a negative peak at $210\,\mathrm{nm}$; the spectrum of left-handed Z-DNA is roughly inverted. A parallel G-quadruplex has a positive peak at about $264\,\mathrm{nm}$ and a negative peak at $240\,\mathrm{nm}$. CD is therefore a convenient means of judging conformational transitions of nucleic acids and the mode of drug–nucleic acid binding.

## Summary

| Topic | Key points |
|---|---|
| Types of transitions | $\sigma\to\sigma^*$ (vacuum ultraviolet), $\mathrm{n}\to\sigma^*$, $\pi\to\pi^*$ (strong, $\varepsilon \ge 10^4$), $\mathrm{n}\to\pi^*$ (weak, $\varepsilon < 10^3$); d–d (weak), charge transfer (strong, $10^3$–$10^5$) |
| Structure and spectrum | The larger the conjugation, the greater the red shift and the intensification; n–π conjugation of auxochromes; polar solvents shift $\pi\to\pi^*$ to the red and $\mathrm{n}\to\pi^*$ to the blue |
| Biological macromolecules | Proteins at $280\,\mathrm{nm}$ (Trp, Tyr), nucleic acids at $260\,\mathrm{nm}$, $A_{260}/A_{280} \approx 1.8$; hyperchromic effect of DNA melting |
| Absorption law | $A = -\lg\tau = \varepsilon bc$, $\varepsilon = N_{\mathrm{A}}\sigma/(1000\ln10)$, $\varepsilon_{\max} \sim 10^5$; additive |
| Deviations | Nonmonochromatic light, stray light, chemical equilibria (isosbestic point), high concentration, scattering |
| Instruments | Deuterium + tungsten lamps, grating, quartz cell, PMT or diode array; single-beam, double-beam, dual-wavelength |
| Measurement error | $\Delta c/c = 0.434\Delta\tau/(\tau\lg\tau)$; for constant $\Delta\tau$ the optimum is $A = 0.434$, the suitable range $0.2$–$0.8$ |
| Applications | Multicomponent (linear equations / least squares), mole-ratio and Job methods ($x_{\max} = n/(n+1)$), $\mathrm{p}K_{\mathrm{a}} = \mathrm{pH} + \lg\frac{A_{\mathrm{B}} - A}{A - A_{\mathrm{HB}}}$ |
| SPR | The evanescent wave excites surface plasmons, and the resonance angle reflects the surface refractive index; $\mathrm{d}R/\mathrm{d}t = k_{\mathrm{a}}c(R_{\max} - R) - k_{\mathrm{d}}R$, $K_{\mathrm{D}} = k_{\mathrm{d}}/k_{\mathrm{a}}$ |
| CD | $\Delta\varepsilon = \varepsilon_{\mathrm{L}} - \varepsilon_{\mathrm{R}}$, $[\theta] = 3298\Delta\varepsilon$; α helix with double negative peak at $208$ and $222\,\mathrm{nm}$ |

The role of ultraviolet–visible spectra in organic structure determination (inferring conjugated systems and chromophores from absorption bands, the Woodward–Fieser rules) is treated in the chapter on spectroscopy in 6.5, Organic Chemistry, together with infrared, nuclear magnetic resonance and mass spectra.

## Questions

1. Example 9.3.1 estimates the lower limit of concentration measurable by ordinary spectrophotometry as about $4.4\times10^{-8}\,\mathrm{mol\,L^{-1}}$. In what ways can this limit be overcome?

   **Answer** From $c_{\min} = A_{\min}/(\varepsilon b)$: (1) increase $\varepsilon$, by choosing sensitive color-forming reagents or ternary complexes, by using labels of very large molar absorption coefficient such as gold nanoparticles, or by enzyme-catalyzed amplification of each analyte molecule into a large number of colored product molecules (enzyme-linked immunosorbent assay); (2) lengthen the path, with liquid-core waveguides, multipass cells or cavity ring-down (Section 9.5.5); (3) reduce $A_{\min}$, by stabilizing the source, compensating with a double beam, reducing noise by lock-in detection, or measuring the heat produced by absorption (photoacoustic, thermal lens); (4) preconcentrate beforehand, by extraction, ion exchange or solid-phase extraction, raising the concentration by several orders of magnitude; (5) switch to methods that detect against a dark background, such as fluorescence and chemiluminescence ([6.4.10](/6.4.10)).
2. Why must quartz cells be used in ultraviolet measurements? With ethanol as the solvent, can the absorption at $205\,\mathrm{nm}$ be measured?

   **Answer** Ordinary glass absorbs strongly below about $350\,\mathrm{nm}$, while quartz is transparent to about $190\,\mathrm{nm}$. The cutoff wavelength of ethanol is about $210\,\mathrm{nm}$, and its absorption at $205\,\mathrm{nm}$ is already strong, so the light transmitted through both reference and sample is weak and stray light and noise make the measurement unreliable; water or acetonitrile should be used instead.
3. A compound has $\lambda_{\max} = 300\,\mathrm{nm}$ ($\varepsilon = 40$) in hexane, which moves to $290\,\mathrm{nm}$ in ethanol. What type of transition is this?

   **Answer** The very small $\varepsilon$ and the blue shift in a polar protic solvent indicate the $\mathrm{n}\to\pi^*$ transition of a heteroatom chromophore such as a carbonyl group.
4. Can a double-beam instrument eliminate the background of a turbid sample? Why can the dual-wavelength method?

   **Answer** The reference beam of a double-beam instrument passes only through the reference cell and cannot compensate for scattering by the sample itself; in the dual-wavelength method two wavelengths pass through the same sample, the scattering is approximately equal at nearby wavelengths, and it cancels in $\Delta A$.
