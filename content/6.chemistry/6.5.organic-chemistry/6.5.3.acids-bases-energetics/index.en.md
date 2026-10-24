---
title: Organic Acids, Bases and the Energetics of Reactions
description: The pKa scale and the course-wide table of pKa values (in water and in DMSO), and why the pKa of water is taken as 14.00; structural factors and solvent effects on acidity; Lewis acids and bases and hard and soft acids and bases; the Hammett equation and substituent constants; energy diagrams, ΔG° and equilibrium constants, estimating reaction enthalpies from bond enthalpies; the Eyring equation and the time scale of reactions; kinetic and thermodynamic control, the Curtin–Hammett principle and the Hammond postulate; rate laws, intermediates, isotopic labeling, crossover experiments and kinetic isotope effects.
source_hash: f5c54e601c14
---

Whether an organic reaction can occur, how far it proceeds, how fast it is and which product it gives are different aspects of one set of thermodynamic and kinetic principles. This chapter arranges these principles as working tools for organic chemistry. The first part is acids and bases: almost every organic reaction contains a proton transfer or can be viewed as a Lewis acid–base reaction in the broad sense, and $\mathrm{p}K_{\mathrm{a}}$ is the most useful number for predicting these steps; 3.1 gives the table of $\mathrm{p}K_{\mathrm{a}}$ values used throughout the course, and later chapters only cite this table. The second part is the linear free-energy relationship (the Hammett equation), which turns the qualitative electronic effects of [6.5.2](/6.5.2) into measurable numbers. The third part is the energetics of reactions: energy diagrams, $\Delta G^\circ$ and equilibrium constants, estimation of heats of reaction from bond enthalpies, the time scales given by transition state theory, kinetic and thermodynamic control of selectivity, the Hammond postulate, and the experimental methods for studying reaction mechanisms. The quantitative treatment of acid–base equilibria is in [6.1.9](/6.1.9) and [6.4.2](/6.4.2), and the derivations of chemical equilibrium and of reaction rate theory are in [6.3.7](/6.3.7), [6.3.15](/6.3.15) and [6.3.16](/6.3.16); they are not repeated here, and only their use in organic chemistry is described.

Thermodynamic data in this chapter are values at 298.15 K in $\mathrm{kJ\,mol^{-1}}$; the organic chemistry literature still often uses $\mathrm{kcal\,mol^{-1}}$, with $1\,\mathrm{kcal\,mol^{-1}} = 4.184\,\mathrm{kJ\,mol^{-1}}$ (exact).

## 3.1. Brønsted Acids and Bases and the pKa Scale

### 3.1.1. Proton Transfer in Organic Reactions

According to **Brønsted–Lowry theory**, an acid that gives up a proton becomes its **conjugate base** ([6.1.9](/6.1.9#sec-9.1.2)). Proton transfer plays two typical roles in organic reactions. One is protonation of a heteroatom, which turns a poor **leaving group** into a good one ($\ce{ROH}$ becomes $\ce{ROH2+}$) or makes a carbonyl carbon more electron-poor and more easily attacked. The other is removal of a proton from a C–H bond by a base, giving a *carbanion*, a trivalent carbon species that carries a negative charge and a lone pair and is a strongly nucleophilic intermediate ([6.5.21](/6.5.21#sec-21.1)).

![Curly arrows for acid–base steps: (a) protonation of acetone by hydronium; the protonated ketone has a resonance structure in the form of a carbocation, so the carbonyl carbon is activated; (b) a Lewis acid–base reaction without a proton: the lone pair of diethyl ether enters the empty orbital of BF₃](./plots/acid-base-arrows.py)

The **curly arrow** of a proton transfer goes from the lone pair of the base to the H being removed, and at the same time the electron pair of the H–A bond returns to A (part (a)). Proton transfer between O and N atoms is generally very fast, close to diffusion control ([6.3.15](/6.3.15)), and is therefore usually not the rate-determining step in a mechanism; deprotonation of a C–H bond, however, can be very slow (3.11.4).

### 3.1.2. pKa and the Position of Equilibrium

The strength of an acid HA in a solvent is expressed by the **acid dissociation constant** $K_{\mathrm{a}}$ or by $\mathrm{p}K_{\mathrm{a}} = -\lg K_{\mathrm{a}}$: the smaller the $\mathrm{p}K_{\mathrm{a}}$, the stronger the acid and the weaker its conjugate base. The strength of a base is expressed by the $\mathrm{p}K_{\mathrm{a}}$ of its conjugate acid (sometimes written $\mathrm{p}K_{\mathrm{aH}}$): the larger the $\mathrm{p}K_{\mathrm{a}}$ of the conjugate acid, the stronger the base.

Combining two acid–base pairs predicts the position of equilibrium of any proton transfer:

$$
\ce{HA + B- <=> A- + HB}, \qquad K = \frac{K_{\mathrm{a}}(\ce{HA})}{K_{\mathrm{a}}(\ce{HB})} = 10^{\,\mathrm{p}K_{\mathrm{a}}(\ce{HB}) - \mathrm{p}K_{\mathrm{a}}(\ce{HA})}. \tag{3.1}
$$
The equilibrium lies on the side of the weaker acid and the weaker base ("a strong acid displaces a weak acid"); each unit of difference between the two $\mathrm{p}K_{\mathrm{a}}$ values changes $K$ by a factor of 10 and $\Delta_{\mathrm{r}}G^\circ = -RT\ln K$ by $RT\ln10 = 5.71\,\mathrm{kJ\,mol^{-1}}$ (298 K). For an acid to be almost completely (> 99%) deprotonated, the $\mathrm{p}K_{\mathrm{a}}$ of the conjugate acid of the base used must be at least 2 units higher.

**Example 3.1.1** (a) Can phenol be completely converted to sodium phenoxide by aqueous NaOH? (b) Can it be converted by an $\ce{NaHCO3}$ solution? (c) How can these two facts be used to separate a mixture of benzoic acid, phenol and toluene?

**Solution** From Table 3.1, (a) the reaction $\ce{C6H5OH + OH- <=> C6H5O- + H2O}$ has $K = 10^{14.00 - 9.99} \approx 10^{4}$, which is essentially complete. (b) $\ce{C6H5OH + HCO3- <=> C6H5O- + H2CO3}$ has $K = 10^{6.35 - 9.99} \approx 10^{-3.6}$ and hardly proceeds, whereas for benzoic acid with $\ce{HCO3-}$, $K = 10^{6.35 - 4.20} \approx 10^{2}$, and the reaction occurs with evolution of $\ce{CO2}$. (c) Dissolve the mixture in diethyl ether and extract first with aqueous $\ce{NaHCO3}$; benzoic acid goes into the aqueous layer as its sodium salt. Then extract with aqueous NaOH; phenol goes into the aqueous layer. Toluene stays in the ether layer. Acidifying the two aqueous layers separately precipitates benzoic acid and phenol. $\square$

### 3.1.3. The pKa of Water: 14.00 or 15.7

Many organic chemistry books and papers give the $\mathrm{p}K_{\mathrm{a}}$ of water as 15.7 and that of $\ce{H3O+}$ as $-1.7$; in this wiki we always use 14.00 and 0, the same convention as in [6.1.9](/6.1.9) with $K_{\mathrm{w}} = 1.0\times10^{-14}$, acetic acid 4.76 and so on. The difference comes from the treatment of the solvent water:

- In the thermodynamic standard equilibrium constant, the solvent has the pure liquid as its standard state and the activity $a(\ce{H2O}) = 1$, so for $\ce{H2O + H2O <=> H3O+ + OH-}$, $K_{\mathrm{a}}(\ce{H2O}) = a(\ce{H3O+})a(\ce{OH-})/a(\ce{H2O}) = K_{\mathrm{w}}$ and $\mathrm{p}K_{\mathrm{a}} = 14.00$; similarly $K_{\mathrm{a}}(\ce{H3O+}) = 1$ and $\mathrm{p}K_{\mathrm{a}} = 0$. The $\mathrm{p}K_{\mathrm{a}}$ values of the other acids are also measured and defined by this convention.
- The value 15.7 comes from writing water into the expression as a solute of concentration $55.5\,\mathrm{mol\,L^{-1}}$: $K_{\mathrm{w}}/[\ce{H2O}] = 10^{-14}/55.5$, $\mathrm{p}K_{\mathrm{a}} = 14.00 + \lg 55.5 = 15.74$; the $-1.74$ for $\ce{H3O+}$ arises in the same way. The numbers obtained this way are not on the same standard as the $\mathrm{p}K_{\mathrm{a}}$ values of the other acids in the tables, and using them in Eq. (3.1) introduces an error of 1.74.

With a consistent convention, water (14.00) is slightly more acidic than methanol (15.5) and ethanol (15.9) in aqueous solution; comparing 15.7 with the values for alcohols leads to the opposite, wrong conclusion.

### 3.1.4. The Unified pKa Tables

The following three tables are the $\mathrm{p}K_{\mathrm{a}}$ data used throughout the course. Values that can be measured directly in water (roughly between $-2$ and 16) are the 25 °C data of the CRC Handbook of Chemistry and Physics, in agreement with [6.1.9](/6.1.9) and [6.4.2](/6.4.2). Very strong and very weak acids that cannot be measured in water (see the leveling effect in 3.3) can only be estimated from acidity functions, thermodynamic cycles or extrapolation; they are marked "ca." in the tables, different sources may differ by 1–2 units, and they are suitable only for comparing orders of magnitude. For weak C–H and N–H acids with $\mathrm{p}K_{\mathrm{a}}$ above about 20, the reliable data are the values measured in dimethyl sulfoxide (DMSO) by Bordwell and coworkers, listed in Table 3.3; the solvent must be stated when they are cited.

Table 3.1  Strong acids and protonated organic compounds in water (25 °C)

| Acid | Conjugate base | $\mathrm{p}K_{\mathrm{a}}$ | Acid | Conjugate base | $\mathrm{p}K_{\mathrm{a}}$ |
|---|---|---|---|---|---|
| $\ce{CF3SO3H}$ (TfOH) | $\ce{CF3SO3-}$ | ca. $-14$ | $\ce{(CH3CH2)2OH+}$ (protonated ether) | $\ce{(CH3CH2)2O}$ | ca. $-3.6$ |
| HI | $\ce{I-}$ | ca. $-10$ | $\ce{H2SO4}$ | $\ce{HSO4-}$ | ca. $-3$ |
| $\ce{RC#NH+}$ (protonated nitrile) | $\ce{RC#N}$ | ca. $-10$ | $\ce{CH3C6H4SO3H}$ (TsOH) | $\ce{CH3C6H4SO3-}$ | ca. $-2.8$ |
| HBr | $\ce{Br-}$ | ca. $-9$ | $\ce{CH3OH2+}$ (protonated alcohol) | $\ce{CH3OH}$ | ca. $-2.2$ |
| $\ce{RCH=OH+}$ (protonated aldehyde) | $\ce{RCHO}$ | ca. $-8$ | $\ce{CH3SO3H}$ (MsOH) | $\ce{CH3SO3-}$ | $-1.9$ |
| HCl | $\ce{Cl-}$ | ca. $-7$ | $\ce{HNO3}$ | $\ce{NO3-}$ | $-1.4$ |
| $\ce{(CH3)2C=OH+}$ (protonated ketone) | $\ce{(CH3)2C=O}$ | ca. $-7$ | $\ce{CH3C(OH)=NH2+}$ (protonated amide, protonated on O) | $\ce{CH3CONH2}$ | ca. $-0.5$ |
| $\ce{RC(OH)2+}$ (protonated carboxylic acid) | $\ce{RCOOH}$ | ca. $-6$ | $\ce{H3O+}$ | $\ce{H2O}$ | $0$ |
| Conjugate acid of pyrrole protonated at C2 | Pyrrole | $-3.8$ | | | |

Table 3.2  Organic acids and conjugate acids of organic bases in water (25 °C)

| Acid | $\mathrm{p}K_{\mathrm{a}}$ | Acid | $\mathrm{p}K_{\mathrm{a}}$ |
|---|---|---|---|
| (O–H acids) | | (N–H acids and ammonium ions) | |
| 2,4,6-Trinitrophenol (picric acid) | 0.42 | 4-Nitroanilinium $\ce{O2NC6H4NH3+}$ | 1.0 |
| $\ce{CF3COOH}$ | 0.52 | $\ce{C6H5NH3+}$ (anilinium) | 4.60 |
| $\ce{CCl3COOH}$ | 0.66 | $\ce{HN3}$ | 4.72 |
| $\ce{CHCl2COOH}$ | 1.35 | Pyridinium $\ce{C5H5NH+}$ | 5.23 |
| $\ce{H3PO4}$ | 2.16 | Imidazolium | 6.99 |
| $\ce{ClCH2COOH}$ | 2.87 | Phthalimide (N–H) | 8.3 |
| HF | 3.20 | $\ce{NH4+}$ | 9.25 |
| HCOOH | 3.75 | 4-Dimethylaminopyridinium (DMAP–H⁺) | 9.6 |
| $\ce{C6H5COOH}$ | 4.20 | Succinimide (N–H) | 9.6 |
| $\ce{CH3COOH}$ | 4.76 | $\ce{(CH3)3NH+}$ | 9.80 |
| $\ce{H2CO3}$ (apparent value, including dissolved $\ce{CO2}$) | 6.35 | $\ce{C6H5SO2NH2}$ | 10.1 |
| 4-Nitrophenol | 7.15 | $\ce{CH3NH3+}$ | 10.66 |
| $\ce{C6H5OH}$ | 9.99 | $\ce{(CH3)2NH2+}$ | 10.73 |
| $\ce{HCO3-}$ | 10.33 | $\ce{(CH3CH2)3NH+}$ | 10.75 |
| $\ce{H2O2}$ | 11.6 | Piperidinium | 11.12 |
| $\ce{CF3CH2OH}$ | 12.4 | Pyrrolidinium | 11.27 |
| $\ce{H2O}$ | 14.00 | Guanidinium $\ce{C(NH2)3+}$ | 13.6 |
| $\ce{CH3OH}$ | 15.5 | Imidazole (N–H) | 14.5 |
| $\ce{CH3CH2OH}$ | 15.9 | $\ce{CH3CONH2}$ (N–H) | ca. 15 |
| $\ce{(CH3)2CHOH}$ | ca. 17 | Pyrrole (N–H) | ca. 17.5 |
| $\ce{(CH3)3COH}$ | ca. 18 | $\ce{NH3}$ | Not measurable in water, ca. 38 (estimated) |
| (S–H acids) | | (C–H acids) | |
| $\ce{C6H5SH}$ | 6.62 | HCN | 9.21 |
| $\ce{H2S}$ | 7.05 | $\ce{CH3COCH2COCH3}$ (acetylacetone) | 8.9 |
| SH of cysteine (free amino acid) | 8.2 | $\ce{CH3NO2}$ | 10.2 |
| $\ce{CH3SH}$ | 10.3 | $\ce{CH3COCH2COOC2H5}$ (ethyl acetoacetate) | 10.7 |
| $\ce{CH3CH2SH}$ | 10.6 | $\ce{CH2(CN)2}$ | 11.2 |
| | | $\ce{CH2(COOC2H5)2}$ (diethyl malonate) | ca. 13 |
| | | Cyclopentadiene | ca. 16 |
| | | $\ce{CH3CHO}$ ($\alpha$-H) | 16.7 |
| | | $\ce{C6H5COCH3}$ ($\alpha$-H) | 18.3 |
| | | $\ce{CH3COCH3}$ ($\alpha$-H) | 19.3 |
| | | $\ce{CH3COOC2H5}$ ($\alpha$-H) | ca. 25 |
| | | $\ce{HC#CH}$ | ca. 25 |
| | | $\ce{CH3CN}$ | ca. 29 |
| | | $\ce{C6H5CH3}$ (benzylic), $\ce{CH2=CHCH3}$ (allylic) | ca. 41, ca. 43 |
| | | $\ce{C6H6}$, $\ce{CH2=CH2}$ | ca. 43, ca. 44 |
| | | $\ce{CH4}$, $\ce{CH3CH3}$ | ca. 50 |

(The $\mathrm{p}K_{\mathrm{a}}$ of aldehydes and ketones refers to loss of an $\alpha$-H from the keto form to give an **enolate**, measured by the kinetic method of Kresge and coworkers; the N–H of pyrrole and imidazole is dissociation as an acid, and pyridinium and imidazolium are conjugate acids. For acetic acid and the dicarboxylic acids such as malonic and oxalic acid, see [6.1.9](/6.1.9) and [6.5.2](/6.5.2#sec-2.7).)

Table 3.3  $\mathrm{p}K_{\mathrm{a}}$ in DMSO (25 °C, Bordwell and coworkers)

| Acid | $\mathrm{p}K_{\mathrm{a}}$(DMSO) | Acid | $\mathrm{p}K_{\mathrm{a}}$(DMSO) |
|---|---|---|---|
| (O–H and S–H acids) | | (C–H acids) | |
| 4-Nitrophenol | 10.8 | $\ce{CH2(CN)2}$ | 11.1 |
| $\ce{C6H5SH}$ | 10.3 | HCN | 12.9 |
| $\ce{C6H5COOH}$ | 11.1 | Acetylacetone | 13.3 |
| $\ce{CH3COOH}$ | 12.3 | Ethyl acetoacetate | 14.2 |
| $\ce{C6H5OH}$ | 18.0 | Diethyl malonate | 16.4 |
| $\ce{CH3OH}$ | 29.0 | $\ce{CH3NO2}$ | 17.2 |
| $\ce{CH3CH2OH}$ | 29.8 | Cyclopentadiene | 18.0 |
| $\ce{H2O}$ | 31.4 | Indene | 20.1 |
| $\ce{(CH3)3COH}$ | 32.2 | $\ce{C6H5CH2CN}$ | 21.9 |
| (N–H acids and ammonium ions) | | Fluorene | 22.6 |
| Pyridinium | 3.4 | $\ce{C6H5COCH3}$ | 24.7 |
| $\ce{(CH3CH2)3NH+}$ | 9.0 | $\ce{CH3COCH3}$ | 26.5 |
| $\ce{NH4+}$ | 10.5 | $\ce{C6H5C#CH}$ | 28.8 |
| Succinimide | 14.7 | $\ce{CH3SO2C6H5}$ | 29.0 |
| $\ce{C6H5SO2NH2}$ | 16.1 | $\ce{(C6H5)3CH}$ | 30.6 |
| Imidazole | 18.6 | $\ce{CH3CN}$ | 31.3 |
| Indole | 21.0 | $\ce{(C6H5)2CH2}$ | 32.2 |
| Pyrrole | 23.0 | $\ce{CH3SOCH3}$ | 35.1 |
| $\ce{(C6H5)2NH}$ | 25.0 | $\ce{C6H5CH3}$ | ca. 43 |
| $\ce{CH3CONH2}$ | 25.5 | $\ce{CH4}$ | ca. 56 |
| $\ce{C6H5NH2}$ | 30.6 | | |
| $\ce{NH3}$ | 41 | | |

Commonly used bases, arranged by the strength of the conjugate acid ("—" means there are no reliable data in that solvent):

| Base | Conjugate acid | $\mathrm{p}K_{\mathrm{a}}$ (water) | $\mathrm{p}K_{\mathrm{a}}$ (other solvent) | Typical use |
|---|---|---|---|---|
| $n$-BuLi | Butane | ca. 50 | — | Metalation, lithium–halogen exchange ([6.5.27](/6.5.27#sec-27.2.1)) |
| $\ce{NaNH2}$ | $\ce{NH3}$ | — | 41 (DMSO) | Deprotonation of terminal alkynes ([6.5.11](/6.5.11#sec-11.12.2)) |
| LDA (**lithium diisopropylamide**) | $\ce{(i-Pr)2NH}$ | — | ca. 36 (THF) | Quantitative formation of kinetic enolates ([6.5.21](/6.5.21#sec-21.3.2)) |
| NaH | $\ce{H2}$ | ca. 35 (estimated) | — | Deprotonation of alcohols and 1,3-dicarbonyl compounds; heterogeneous, evolution of $\ce{H2}$ drives the reaction |
| LiHMDS, KHMDS | $\ce{HN(SiMe3)2}$ | — | ca. 30 (DMSO), ca. 26 (THF) | Bulky, weakly nucleophilic strong bases |
| $t$-BuOK | $\ce{(CH3)3COH}$ | ca. 18 | 32.2 (DMSO) | Elimination ([6.5.9](/6.5.9#sec-9.4.3)) |
| $\ce{NaOCH2CH3}$ | $\ce{CH3CH2OH}$ | 15.9 | 29.8 (DMSO) | Claisen condensation ([6.5.22](/6.5.22#sec-22.3.1)) |
| NaOH | $\ce{H2O}$ | 14.00 | 31.4 (DMSO) | Saponification, aldol condensation |
| DBU | DBU–H⁺ | — | 24.3 (acetonitrile) | Strong organic base, elimination |
| $\ce{K2CO3}$ | $\ce{HCO3-}$ | 10.33 | — | Alkylation of phenols and 1,3-dicarbonyl compounds |
| $\ce{(CH3CH2)3N}$ | $\ce{(CH3CH2)3NH+}$ | 10.75 | 9.0 (DMSO) | Scavenging the acid formed in acylation |
| $\ce{NaHCO3}$ | $\ce{H2CO3}$ | 6.35 | — | Mild base, extraction of carboxylic acids |
| Pyridine | Pyridinium | 5.23 | 3.4 (DMSO) | Solvent and base, acylation catalyst |

## 3.2. Structural Factors That Affect Acidity

The strength of an acid depends on the relative stability of HA and $\ce{A-}$; in a group of acids of similar structure the decisive factor is usually the stability of the conjugate base $\ce{A-}$: the more stable the conjugate base, the stronger the acid. The four factors that determine the stability of $\ce{A-}$, in order of general importance, are the atom that carries the charge, resonance, the **inductive effect** and orbital hybridization.

| Factor | Rule | Example ($\mathrm{p}K_{\mathrm{a}}$ in water, Tables 3.1–3.3) |
|---|---|---|
| Charged atom: same period | The greater the electronegativity, the better the atom accommodates negative charge | Acidity $\ce{CH4}$ (ca. 50) < $\ce{NH3}$ (ca. 38) < $\ce{H2O}$ (14.00) < HF (3.20) |
| Charged atom: same group | The larger the atom, the more the negative charge is spread over a larger volume and the weaker the H–A bond, so the stronger the acid (this overrides electronegativity) | Acidity HF (3.20) < HCl (ca. $-7$); $\ce{H2O}$ (14.00) < $\ce{H2S}$ (7.05); $\ce{CH3OH}$ (15.5) < $\ce{CH3SH}$ (10.3) |
| Resonance | Delocalization of negative charge onto electronegative atoms gives the greatest stabilization | Acidity ethanol (15.9) < phenol (9.99) < acetic acid (4.76); propane (ca. 50) < acetone (19.3) < acetylacetone (8.9) |
| Inductive effect | Electron-withdrawing groups stabilize negative charge, with rapid decay with distance | Acidity ethanol (15.9) < 2,2,2-trifluoroethanol (12.4); acetic acid (4.76) < chloroacetic acid (2.87) < trichloroacetic acid (0.66) |
| Hybridization | The greater the s character, the closer the lone pair is to the nucleus | Acidity ethane (ca. 50) < ethene (ca. 44) < ethyne (ca. 25); basicity piperidine (conjugate acid 11.12) > pyridine (5.23), the lone pair of the sp² N is weakly basic |
| Aromaticity | A conjugate base that is aromatic is especially stable | Cyclopentadiene ca. 16 (the conjugate base is a 6π aromatic anion, [6.5.13](/6.5.13#sec-13.5.1)), much stronger than ordinary alkenes |

Basicity is judged by the mirror image of this: the more stable the lone pair (delocalized, on a more electronegative atom, with higher s character), the weaker the base. The conjugate acids of amines have $\mathrm{p}K_{\mathrm{a}}$ about 10–11; for aniline it is only 4.60 (the lone pair is conjugated with the benzene ring); protonation of the N of an amide is below $-1$ (the lone pair is conjugated with the carbonyl group; amides are actually protonated on O, Table 3.1); for pyridine it is 5.23 (an sp² lone pair); for pyrrole $-3.8$ (the lone pair is part of the aromatic 6π system, and protonation can occur only on carbon and destroys aromaticity).

When several factors act together they must be analyzed case by case. For example, phenol (9.99) is $10^6$ times more acidic than cyclohexanol (about 16 in water, estimated) because the negative charge of the phenoxide is delocalized to the *ortho* and *para* positions of the ring; 4-nitrophenol (7.15) is stronger still because the $-$M effect of the nitro group pulls the negative charge further onto the oxygens of the nitro group, whereas 3-nitrophenol (8.36, water, CRC) can use only the **inductive effect** and the effect is smaller. This is why the Hammett equation of 3.5 needs $\sigma^-$.

![Why 4-nitrophenol is a stronger acid than phenol: in 4-nitrophenoxide the lone pair on the phenoxide oxygen can be pushed through the ring all the way onto an oxygen of the nitro group (four curved arrows); the C–O bond gains double-bond character, the ring becomes quinoid and the negative charge ends up on the electronegative nitro oxygen. 3-Nitrophenoxide has no such structure, and its nitro group acts by induction only](./plots/nitrophenoxide-resonance.py)

## 3.3. Solvent Effects

The $\mathrm{p}K_{\mathrm{a}}$ is a property of an acid in a particular solvent, and the $\mathrm{p}K_{\mathrm{a}}$ of the same acid in different solvents can differ by more than ten units:

| Acid | Water | DMSO | Acetonitrile |
|---|---|---|---|
| Benzoic acid | 4.20 | 11.1 | 21.5 |
| 4-Cyanobenzoic acid | 3.55 | 9.27 | 19.34 |
| Acetic acid | 4.76 | 12.3 | 23.5 |
| Phenol | 9.99 | 18.0 | 29.1 |
| Water | 14.00 | 31.4 | — |
| Malononitrile | 11.2 | 11.1 | — |
| Triethylammonium ion | 10.75 | 9.0 | 18.8 |

The main reason for these differences is the different ability of solvents to solvate ions, especially small anions with concentrated charge. Water has the largest relative permittivity (about 78) and can donate hydrogen bonds, and it strongly stabilizes anions such as $\ce{RCOO-}$, $\ce{RO-}$ and $\ce{OH-}$ in which the charge is concentrated on oxygen. DMSO (relative permittivity about 47) and acetonitrile (about 36) cannot act as hydrogen-bond donors, anions are "naked" and unstable in them, and the $\mathrm{p}K_{\mathrm{a}}$ of carboxylic acids, phenols, alcohols and water in DMSO is 7–17 units higher than in water; acetonitrile has a still lower permittivity and a weaker stabilizing effect on cations (the protonated solvent), so its $\mathrm{p}K_{\mathrm{a}}$ values are higher yet. (The statement that "from water to DMSO to acetonitrile the solvent accepts protons ever less readily" is inaccurate: DMSO is a much stronger hydrogen-bond acceptor than water, its gas-phase proton affinity is also much larger than that of water, and it solvates N–H cations well, so the $\mathrm{p}K_{\mathrm{a}}$ of the triethylammonium ion is in fact slightly lower in DMSO than in water.)

Conjugate bases with highly delocalized negative charge depend much less on solvation: the $\mathrm{p}K_{\mathrm{a}}$ of malononitrile is almost the same in water and in DMSO, and the $\mathrm{p}K_{\mathrm{a}}$ values in DMSO of C–H acids such as fluorene and triphenylmethane follow the same relative order as in the gas phase. In the gas phase there is no solvent and acidity is determined entirely by the molecule: the order of acidity of alcohols in the gas phase is $(\mathrm{CH_3})_3\mathrm{COH} > (\mathrm{CH_3})_2\mathrm{CHOH} > \mathrm{CH_3CH_2OH} > \mathrm{CH_3OH} > \mathrm{H_2O}$, since large alkyl groups stabilize negative charge through their polarizability; in water the order is completely reversed, because the small $\ce{CH3O-}$ is solvated more easily than the large $\ce{(CH3)3CO-}$. The explanation that "the electron-donating inductive effect of alkyl groups weakens *tert*-butyl alcohol" therefore applies only in solution, and what acts in solution is in fact solvation.

The solvent also limits the range of $\mathrm{p}K_{\mathrm{a}}$ that can be measured. The strongest acid that can exist in water is $\ce{H3O+}$ and the strongest base is $\ce{OH-}$: any acid stronger than $\ce{H3O+}$ gives its proton completely to water, and any base stronger than $\ce{OH-}$ takes a proton completely from water; this is the **leveling effect** of the solvent ([6.1.9](/6.1.9#sec-9.1.2)). The measurable $\mathrm{p}K_{\mathrm{a}}$ range in water is therefore roughly $-2$ to 16; stronger acids must be measured with acidity functions in concentrated acids (the Hammett acidity function $H_0$), and weaker acids in solvents such as DMSO that are more basic and themselves less acidic. The consequence for synthesis is that to generate a carbanion with $\mathrm{p}K_{\mathrm{a}}$ above 16 (for example the quantitative generation of the enolate of a ketone), water or an alcohol cannot be the solvent, and one must use an aprotic solvent such as THF or DMSO with a strong base such as LDA ([6.5.21](/6.5.21#sec-21.1.3)).

## 3.4. Lewis Acids and Bases and Hard and Soft Acids and Bases

Lewis generalized acids and bases to the acceptance and donation of electron pairs: a species that can accept an electron pair is a **Lewis acid**, one that can donate an electron pair is a **Lewis base**, and the two combine to form a Lewis acid–base adduct ([6.1.9](/6.1.9#sec-9.1.3)), such as the combination of diethyl ether with $\ce{BF3}$ in part (b) of the figure above. Brønsted acid–base reactions are a special case of Lewis acid–base reactions ($\ce{H+}$ is a Lewis acid).

In the Lewis sense almost all polar organic reactions are acid–base reactions: **nucleophiles** are Lewis bases, **electrophiles** are Lewis acids, and the curly arrow always points from the Lewis base to the Lewis acid. The only difference is one of habit: when the reaction center is H the reaction is called an acid–base reaction, and when it is C it is called a nucleophilic or electrophilic reaction. Lewis acids such as $\ce{BF3}$, $\ce{AlCl3}$, $\ce{TiCl4}$, $\ce{ZnCl2}$, $\ce{SnCl4}$, $\ce{Mg^2+}$ and $\ce{Li+}$ are often used in organic synthesis to coordinate to the lone pairs of a carbonyl group or a halogen and make the substrate more electron-poor, thereby activating it (Friedel–Crafts reactions, [6.5.14](/6.5.14#sec-14.9); Lewis acid catalyzed Diels–Alder reactions, [6.5.12](/6.5.12#sec-12.4.3)).

The principle of **hard and soft acids and bases** (Pearson, 1963; [6.1.9](/6.1.9#sec-9.1.4)) divides Lewis acids and bases into hard and soft:

| | Hard | Borderline | Soft |
|---|---|---|---|
| Acids | $\ce{H+}$, $\ce{Li+}$, $\ce{Na+}$, $\ce{K+}$, $\ce{Mg^2+}$, $\ce{Ca^2+}$, $\ce{Al^3+}$, $\ce{BF3}$, $\ce{RCO+}$, carbonyl carbon | $\ce{Fe^2+}$, $\ce{Cu^2+}$, $\ce{Zn^2+}$, $\ce{R3C+}$, $\ce{SO2}$ | $\ce{Cu+}$, $\ce{Ag+}$, $\ce{Au+}$, $\ce{Hg^2+}$, $\ce{Pd^2+}$, $\ce{Pt^2+}$, $\ce{Br2}$, $\ce{I2}$, electrophilic centers on saturated carbon (such as the carbon of $\ce{CH3-I}$), terminal carbons of conjugated systems |
| Bases | $\ce{F-}$, $\ce{OH-}$, $\ce{H2O}$, $\ce{ROH}$, $\ce{RO-}$, $\ce{RCOO-}$, $\ce{NH3}$, $\ce{RNH2}$, $\ce{Cl-}$ | $\ce{Br-}$, $\ce{N3-}$, pyridine, aniline | $\ce{RS-}$, $\ce{RSH}$, $\ce{R2S}$, $\ce{I-}$, $\ce{CN-}$, $\ce{SCN-}$, $\ce{R3P}$, $\ce{H-}$, $\ce{CO}$, alkenes, arenes |

Hard species are small, have concentrated charge and low polarizability; soft species are large, have dispersed charge and high polarizability ([6.5.2](/6.5.2#sec-2.4)). The rule is "hard prefers hard, soft prefers soft": the combination of a hard acid with a hard base is mainly electrostatic, and that of a soft acid with a soft base is mainly orbital (covalent). In organic chemistry this explains qualitatively several kinds of selectivity:

- Thiolate and $\ce{I-}$ undergo **SN2** substitution at saturated carbon (soft–soft), whereas small, strongly basic alkoxides more easily remove a $\beta$-H and cause elimination (combining with the hard $\ce{H+}$, [6.5.9](/6.5.9#sec-9.6.1)).
- Organolithium and Grignard reagents (hard) add to the carbonyl carbon of $\alpha$,$\beta$-unsaturated ketones (**1,2-addition**), and organocopper reagents (soft) add to the $\beta$ carbon (**1,4-addition**, [6.5.17](/6.5.17#sec-17.6.2)).
- **Ambident nucleophiles** such as enolates react on O with hard electrophiles (acyl chlorides, chlorotrimethylsilane) and on C with soft electrophiles (iodomethane) ([6.5.21](/6.5.21#sec-21.4.1)).

The concepts of hardness and softness are qualitative. A more quantitative treatment (the Klopman–Salem equation) divides the interaction between two molecules into a charge term and a frontier orbital term: hard–hard interactions are charge controlled, and soft–soft interactions are controlled by HOMO–LUMO overlap ([6.5.12](/6.5.12#sec-12.2.2)).

## 3.5. Linear Free-Energy Relationships and the Hammett Equation

[6.5.2](/6.5.2) discussed the electronic effects of substituents qualitatively. Hammett (1937) found that the effects of *meta* or *para* substituents on the benzene ring on many different reactions are proportional: a substituent that strengthens benzoic acid also increases, in a fixed proportion, the acidity of phenylacetic acid and the rate of alkaline hydrolysis of ethyl benzoate. Since $\lg K$ and $\lg k$ are proportional to $\Delta_{\mathrm{r}}G^\circ$ and $\Delta^{\ddagger}G^\circ$, respectively, such proportionality is called a *linear free-energy relationship*.

**Definition 3.5.1 (Hammett Equation)** For reactions of *meta*- or *para*-substituted benzene derivatives,

$$
\lg\frac{K_{\mathrm{X}}}{K_{\mathrm{H}}} = \rho\sigma_{\mathrm{X}}, \qquad \lg\frac{k_{\mathrm{X}}}{k_{\mathrm{H}}} = \rho\sigma_{\mathrm{X}} \tag{3.2}
$$
is called the **Hammett equation**, where $K_{\mathrm{X}}$ and $k_{\mathrm{X}}$ are the equilibrium constant or rate constant when the substituent is X. The quantity $\sigma_{\mathrm{X}}$, which depends only on the substituent and its position, is called the **substituent constant** and is defined by the ionization of substituted benzoic acids in water at 25 °C: $\sigma_{\mathrm{X}} = \mathrm{p}K_{\mathrm{a}}(\ce{C6H5COOH}) - \mathrm{p}K_{\mathrm{a}}(\ce{XC6H4COOH})$; the quantity $\rho$, which depends only on the reaction and its conditions, is called the **reaction constant**, and for the ionization of benzoic acid $\rho = 1$ by definition.

A substituent with $\sigma > 0$ is electron-withdrawing (it strengthens benzoic acid), and one with $\sigma < 0$ is electron-donating. The *meta* value $\sigma_m$ mainly reflects the inductive effect, and the *para* value $\sigma_p$ also contains the **conjugation effect**. When there is direct conjugation ("through-conjugation") between the reaction center and a *para* substituent, the ordinary $\sigma_p$ is not sufficient: when positive charge develops at the reaction center (a **carbocation**) and is conjugated directly with an electron-donating group, $\sigma_p^+$ is used (Brown–Okamoto, defined from the solvolysis of cumyl chloride), and when negative charge develops and is conjugated directly with an electron-withdrawing group, $\sigma_p^-$ is used (defined from the ionization of phenols and anilinium ions).

| Substituent X | $\sigma_m$ | $\sigma_p$ | $\sigma_p^+$ | $\sigma_p^-$ |
|---|---|---|---|---|
| $\ce{N(CH3)2}$ | $-0.16$ | $-0.83$ | $-1.7$ | |
| $\ce{NH2}$ | $-0.16$ | $-0.66$ | $-1.3$ | |
| OH | $+0.12$ | $-0.37$ | $-0.92$ | |
| $\ce{OCH3}$ | $+0.12$ | $-0.27$ | $-0.78$ | |
| $\ce{CH3}$ | $-0.07$ | $-0.17$ | $-0.31$ | |
| H | $0$ | $0$ | $0$ | $0$ |
| F | $+0.34$ | $+0.06$ | $-0.07$ | |
| Cl | $+0.37$ | $+0.23$ | $+0.11$ | |
| Br | $+0.39$ | $+0.23$ | $+0.15$ | |
| I | $+0.35$ | $+0.18$ | $+0.14$ | |
| $\ce{COCH3}$ | $+0.38$ | $+0.50$ | | $+0.84$ |
| $\ce{CF3}$ | $+0.43$ | $+0.54$ | $+0.61$ | $+0.65$ |
| CN | $+0.56$ | $+0.66$ | $+0.66$ | $+1.00$ |
| $\ce{NO2}$ | $+0.71$ | $+0.78$ | $+0.79$ | $+1.27$ |

(Data are from the compilation of Hansch, Leo and Taft (*Chem. Rev.* 1991, 91, 165); $\sigma^+$ and $\sigma^-$ are meaningful only for substituents that can conjugate directly with the reaction center, and a blank means not applicable or not commonly used.)

The reaction constant $\rho$ reflects the sensitivity of the reaction to electronic effects and its direction: $\rho > 0$ means that electron-withdrawing groups accelerate the reaction (or shift the equilibrium to the right), indicating that negative charge accumulates (or positive charge is lost) at the reaction center from reactant to transition state (or product); $\rho < 0$ means that positive charge accumulates; the larger $\lvert\rho\rvert$, the greater the change in charge or the closer it is to the benzene ring.

| Reaction (conditions) | $\rho$ | Remarks |
|---|---|---|
| Ionization of $\ce{ArCOOH}$ (water, 25 °C) | $1.00$ | Definition |
| Ionization of $\ce{ArCH2COOH}$ (water, 25 °C) | $0.49$ | One more $\ce{CH2}$ reduces the transmission by about half |
| Ionization of $\ce{ArOH}$ (water, 25 °C) | $2.23$ | The negative charge is directly on the ring; $\sigma^-$ is used for *para* electron-withdrawing groups |
| Ionization of $\ce{ArNH3+}$ (water, 25 °C) | $2.89$ | Same as above |
| Alkaline hydrolysis of $\ce{ArCOOC2H5}$ (85% ethanol, 25 °C) | $+2.5$ | The rate-determining step forms a negatively charged tetrahedral intermediate ([6.5.19](/6.5.19#sec-19.2.1)) |
| Solvolysis of $\ce{ArC(CH3)2Cl}$ (90% acetone, 25 °C) | $-4.5$ (against $\sigma^+$) | The rate-determining step forms a carbocation ([6.5.8](/6.5.8#sec-8.9)) |

![Hammett plot for substituted phenols in water at 25 °C (pKa from the CRC, σ from Hansch, Leo and Taft 1991). The line is a least-squares fit through the origin to the meta substituents and to the para substituents without π acceptors, ρ ≈ 2.27; para-nitro and para-cyano plotted against σₚ (open circles) deviate clearly from the line and return to it when σₚ⁻ (filled squares) is used](./plots/hammett-phenols.py)

The figure above is an example of finding a reaction constant from the data of Table 3.2: $\mathrm{p}K_{\mathrm{a}}(\mathrm{H}) - \mathrm{p}K_{\mathrm{a}}(\mathrm{X})$ is plotted against $\sigma$ and fitted by a straight line through the origin using **least squares** ([3.3](/3.3)), giving $\rho = 2.27$, close to the literature value 2.23. The $\rho$ of phenol is more than twice that of benzoic acid because the negative charge of the phenoxide is directly on the ring. For 4-nitrophenol the $\mathrm{p}K_{\mathrm{a}}$ predicted with $\sigma_p = 0.78$ is 8.2, whereas the measured value is 7.15; the prediction with $\sigma_p^- = 1.27$ is 7.1, in agreement with the measurement, which quantitatively accounts for the through-conjugation of negative charge onto the nitro group (3.2).

Hammett plots are a tool for studying mechanisms: the sign and magnitude of $\rho$ suggest the change in charge in the transition state, and a Hammett plot that bends in the middle often indicates that the rate-determining step or the mechanism changes as the substituent changes. For aliphatic systems and *ortho* substituents, electronic and steric effects are mixed and require a different treatment (the Taft equation), which is not pursued here.

## 3.6. Energy Diagrams and Equilibrium

### 3.6.1. Energy Diagrams

The energy of a reacting system varies with the positions of the nuclei and forms a **potential energy surface**; an energy diagram along the lowest-energy path from reactants to products (the **reaction coordinate**) gives the energy profile of the reaction ([6.3.16](/6.3.16#sec-16.2)). In organic chemistry the diagram usually plotted is Gibbs energy against the reaction coordinate.

![Free-energy profiles. Left: a one-step exergonic reaction; the Gibbs energy of activation determines the rate and the reaction Gibbs energy determines the position of equilibrium. Right: a two-step reaction through one intermediate; the first transition state is the highest point and the first step is rate-determining. A transition state is a maximum on the reaction coordinate and an intermediate is a minimum](./plots/energy-profiles.py)

In reading an energy diagram one must distinguish:

- A **transition state** is a maximum on the energy profile (a saddle point on the potential energy surface); its lifetime is only that of one molecular vibration (about $10^{-13}\,\mathrm{s}$), it cannot be isolated and cannot be observed directly by ordinary spectroscopy. A **reaction intermediate** is a minimum between two transition states; its lifetime can range from picoseconds to hours, and in principle it can be detected or even isolated.
- The Gibbs energy difference $\Delta_{\mathrm{r}}G^\circ$ between start and end is the thermodynamic factor that determines whether and how far a reaction proceeds, independent of the pathway; the Gibbs energy difference $\Delta^{\ddagger}G^\circ$ from reactant to transition state is the kinetic factor that determines how fast it is, and depends on the pathway.
- In a multistep reaction, the step containing the transition state of highest Gibbs energy relative to the starting material is the rate-determining step; it is not necessarily the step with the largest activation energy (relative to the preceding intermediate).
- By the **principle of microscopic reversibility**, the reverse reaction goes through the same pathway and the same transition state, so the Gibbs energy of activation of the reverse reaction is $\Delta^{\ddagger}G^\circ - \Delta_{\mathrm{r}}G^\circ$; the forward and reverse activation energies are equal only when $\Delta_{\mathrm{r}}G^\circ = 0$.

### 3.6.2. ΔG° and the Equilibrium Constant

The relation (see [6.3.7](/6.3.7)) between the **standard equilibrium constant** and the **standard reaction Gibbs energy**

$$
\Delta_{\mathrm{r}}G^\circ = -RT\ln K^\circ = -2.303\,RT\lg K^\circ \tag{3.3}
$$
directly connects thermodynamic data with the extent to which a reaction proceeds. At 298 K, $2.303\,RT = 5.71\,\mathrm{kJ\,mol^{-1}}$: each change of $5.71\,\mathrm{kJ\,mol^{-1}}$ in $\Delta_{\mathrm{r}}G^\circ$ changes $K^\circ$ by a factor of 10. For an isomerization $\ce{A <=> B}$:

| $\Delta_{\mathrm{r}}G^\circ$ / (kJ mol⁻¹) | $\Delta_{\mathrm{r}}G^\circ$ / (kcal mol⁻¹) | $K^\circ$ (298 K) | Fraction of B at equilibrium |
|---|---|---|---|
| $+20$ | $+4.8$ | $3.1\times10^{-4}$ | 0.03% |
| $+10$ | $+2.4$ | $0.018$ | 1.7% |
| $+5.7$ | $+1.4$ | $0.10$ | 9% |
| $0$ | $0$ | $1$ | 50% |
| $-5.7$ | $-1.4$ | $10$ | 91% |
| $-10$ | $-2.4$ | $56$ | 98.3% |
| $-20$ | $-4.8$ | $3.2\times10^{3}$ | 99.97% |
| $-40$ | $-9.6$ | $1.0\times10^{7}$ | > 99.999% |

A difference of a few $\mathrm{kJ\,mol^{-1}}$ can change the composition of the products significantly: $10\,\mathrm{kJ\,mol^{-1}}$ already gives an equilibrium composition of about 98 : 2. The energy differences in conformational equilibria ([6.5.4](/6.5.4#sec-4.6.1)) and **tautomerism** equilibria ([6.5.21](/6.5.21#sec-21.2.1)) are typically in this range.

## 3.7. Estimating Reaction Enthalpies and Entropies

$\Delta_{\mathrm{r}}G^\circ = \Delta_{\mathrm{r}}H^\circ - T\Delta_{\mathrm{r}}S^\circ$. When enthalpies of formation are not available, the enthalpy change of a gas-phase reaction can be estimated from **bond enthalpies** ([6.1.6](/6.1.6)):

$$
\Delta_{\mathrm{r}}H^\circ \approx \sum \bar D(\text{bonds broken}) - \sum \bar D(\text{bonds formed}).
$$

**Example 3.7.1** Estimate $\Delta_{\mathrm{r}}H^\circ$ and $\Delta_{\mathrm{r}}G^\circ$ at 298 K for $\ce{CH2=CH2(g) + HCl(g) -> CH3CH2Cl(g)}$ and discuss the effect of temperature. Mean bond enthalpies: C=C 610, H–Cl 432, C–C 346, C–H 413, C–Cl $339\,\mathrm{kJ\,mol^{-1}}$; standard molar entropies $S^\circ$: $\ce{C2H4}$ 219.3, HCl 186.9, $\ce{C2H5Cl}$ $276.0\,\mathrm{J\,mol^{-1}\,K^{-1}}$; standard molar enthalpies of formation: $\ce{C2H4}$ $+52.4$, HCl $-92.3$, $\ce{C2H5Cl}$ $-112.1\,\mathrm{kJ\,mol^{-1}}$.

**Solution** C=C and H–Cl are broken and C–C, C–H and C–Cl are formed: $\Delta_{\mathrm{r}}H^\circ \approx (610 + 432) - (346 + 413 + 339) = -56\,\mathrm{kJ\,mol^{-1}}$. The accurate value from the enthalpies of formation is $-112.1 - 52.4 + 92.3 = -72.2\,\mathrm{kJ\,mol^{-1}}$, so the bond-enthalpy estimate is off by about $16\,\mathrm{kJ\,mol^{-1}}$, which is the usual accuracy of the mean bond enthalpy method. Two gas molecules combine into one, and $\Delta_{\mathrm{r}}S^\circ = 276.0 - 219.3 - 186.9 = -130.2\,\mathrm{J\,mol^{-1}\,K^{-1}}$, so

$$
\Delta_{\mathrm{r}}G^\circ = -72.2 - 298.15 \times (-0.1302) = -33.4\,\mathrm{kJ\,mol^{-1}}, \qquad K^\circ \approx 7\times10^{5}.
$$
The enthalpy is favorable and the entropy unfavorable, and the term $-T\Delta_{\mathrm{r}}S^\circ$ grows as the temperature rises; neglecting the temperature dependence of $\Delta_{\mathrm{r}}H^\circ$ and $\Delta_{\mathrm{r}}S^\circ$, the temperature at which $\Delta_{\mathrm{r}}G^\circ = 0$ is about $72.2/0.1302 \approx 555\,\mathrm{K}$. Addition is favorable at low temperature; in the gas phase above 300 °C the equilibrium turns toward the reverse reaction, that is, chloroethane loses HCl to give ethene. $\square$

There are several rules of thumb for entropy: when two molecules combine into one in the gas phase, $\Delta_{\mathrm{r}}S^\circ$ is about $-120$ to $-150\,\mathrm{J\,mol^{-1}\,K^{-1}}$ (mainly the loss of the translational entropy of one molecule), and somewhat smaller in solution; a ring-forming reaction within a molecule loses only the entropy of internal rotation and is much more favorable than an intermolecular combination, which is one reason why five- and six-membered rings form readily. Note also that the mean bond enthalpy is an average over many compounds, and for the cleavage of a specific bond (such as a C–H bond in a radical reaction) the **bond dissociation energy** of that bond should be used ([6.5.7](/6.5.7#def-7.2.2)).

## 3.8. Transition State Theory and the Time Scale of Reactions

Transition state theory relates the rate constant to the Gibbs energy of activation by the **Eyring equation** ([6.3.16](/6.3.16#sec-16.3)):

$$
k = \frac{k_{\mathrm{B}}T}{h}\exp\left(-\frac{\Delta^{\ddagger}G^\circ}{RT}\right) = \frac{k_{\mathrm{B}}T}{h}\exp\left(\frac{\Delta^{\ddagger}S^\circ}{R}\right)\exp\left(-\frac{\Delta^{\ddagger}H^\circ}{RT}\right), \tag{3.4}
$$
where $\Delta^{\ddagger}G^\circ$ is the **Gibbs energy of activation**, and $\Delta^{\ddagger}H^\circ$ and $\Delta^{\ddagger}S^\circ$ are the **enthalpy of activation** and the **entropy of activation** (bimolecular reactions have an additional factor for the concentration standard state, see [6.3.16](/6.3.16#sec-16.3.2)). At 298 K, $k_{\mathrm{B}}T/h$ is $6.21\times10^{12}\,\mathrm{s^{-1}}$. If $k$ is measured at different temperatures and $\ln(k/T)$ is plotted against $1/T$, the slope gives $-\Delta^{\ddagger}H^\circ/R$ and the intercept gives $\Delta^{\ddagger}S^\circ$.

The Eyring equation has a form similar to the empirical **Arrhenius equation** $k = A\exp(-E_{\mathrm{a}}/RT)$ but a different meaning:

| | Eyring equation | Arrhenius equation |
|---|---|---|
| Origin | Transition state theory, applicable to elementary reactions | Empirical formula summarizing experiments, usable for overall reactions |
| Parameters | $\Delta^{\ddagger}H^\circ$ and $\Delta^{\ddagger}S^\circ$, with clear physical meaning | **Pre-exponential factor** $A$ and apparent activation energy $E_{\mathrm{a}}$ |
| Relation | In solution $E_{\mathrm{a}} = \Delta^{\ddagger}H^\circ + RT$, $A = \frac{\mathrm{e}k_{\mathrm{B}}T}{h}\mathrm{e}^{\Delta^{\ddagger}S^\circ/R}$ (unimolecular reactions) | |

The organic chemistry literature mainly uses the Eyring equation because its parameters can be compared directly with transition states from quantum chemical calculations. From Eq. (3.4) the **half-life** of a first-order reaction, $t_{1/2} = \ln2/k$, can be related to the Gibbs energy of activation:

| $\Delta^{\ddagger}G^\circ$ / (kJ mol⁻¹) | (kcal mol⁻¹) | $-78\,^\circ\mathrm{C}$ | $20\,^\circ\mathrm{C}$ | $100\,^\circ\mathrm{C}$ |
|---|---|---|---|---|
| 41.8 | 10 | 27 ms | 3 µs | 64 ns |
| 62.8 | 15 | 3.0 h | 17 ms | 54 µs |
| 83.7 | 20 | ca. 140 years | 1.5 min | 46 ms |
| 92.0 | 22 | — | 48 min | 0.7 s |
| 104.6 | 25 | — | 5.7 d | 39 s |
| 125.5 | 30 | — | 83 years | 9.2 h |

This table gives a useful sense of scale:

- A reaction that is complete within a few hours at room temperature has $\Delta^{\ddagger}G^\circ$ of about $90$–$100\,\mathrm{kJ\,mol^{-1}}$; a reaction above about $105\,\mathrm{kJ\,mol^{-1}}$ (25 kcal mol⁻¹) practically does not occur at room temperature and needs heating.
- Near 298 K, each decrease of $5.7\,\mathrm{kJ\,mol^{-1}}$ in $\Delta^{\ddagger}G^\circ$ increases the rate tenfold; raising the temperature of the same reaction from 20 °C to 100 °C increases the rate by a factor of tens to $10^5$ (the larger the activation energy, the greater the effect of temperature).
- At $-78\,^\circ\mathrm{C}$ (dry ice–acetone bath) only processes with $\Delta^{\ddagger}G^\circ$ below about $60\,\mathrm{kJ\,mol^{-1}}$ proceed in a reasonable time, so low temperature can "freeze out" side reactions or isomerizations with higher activation energies, a common means of kinetic control (3.9).

(These values assume a transmission coefficient of 1 and are order-of-magnitude estimates. H-atom transfer may also involve tunneling, 3.11.4.)

The entropy of activation also has diagnostic value: unimolecular rearrangements and decompositions have $\Delta^{\ddagger}S^\circ$ near 0 or positive; a bimolecular reaction loses translational and rotational degrees of freedom of one molecule in the transition state, and $\Delta^{\ddagger}S^\circ$ is generally $-80$ to $-150\,\mathrm{J\,mol^{-1}\,K^{-1}}$; highly ordered cyclic transition states (such as in the Diels–Alder reaction, [6.5.12](/6.5.12#sec-12.4.3)) are at the negative end of this range.

## 3.9. Selectivity: Kinetic and Thermodynamic Control

### 3.9.1. Selectivity

**Definition 3.9.1 (Selectivity)** When a reactant can form different products by several pathways, the tendency to form a particular product is called the **selectivity** of the reaction and is expressed as the ratio of the products (or the percentage of one of them).

According to the relation between the products, several kinds of selectivity are distinguished in organic chemistry: when the substrate has several **functional groups** and reacts with only one of them, this is *chemoselectivity*, for example the reduction of a ketone but not an ester by $\ce{NaBH4}$ ([6.5.17](/6.5.17#sec-17.1.1)); when a reaction can occur at different positions of the same functional group and favors one position, it is *regioselectivity*, for example the Markovnikov orientation of the addition of HBr to propene ([6.5.11](/6.5.11#sec-11.3.2)); the tendency to form different stereoisomers is stereoselectivity, see [6.5.5](/6.5.5#sec-5.8.1).

### 3.9.2. Kinetic Control and Thermodynamic Control

Let reactant A form product B or C (written for simplicity with first-order steps):

$$
\ce{B <=>[k_{-1}][k_1] A <=>[k_2][k_{-2}] C}.
$$

**Definition 3.9.2 (Kinetic Control)** When the steps that form the products are irreversible (or cannot reverse within the reaction time), the ratio of the products is determined by the ratio of the rate constants of the pathways,

$$
\frac{[\ce{B}]}{[\ce{C}]} = \frac{k_1}{k_2} = \exp\left(-\frac{\Delta^{\ddagger}G^\circ_1 - \Delta^{\ddagger}G^\circ_2}{RT}\right),
$$
and this situation is called **kinetic control**; the product that forms faster (the product of the pathway with the lower Gibbs energy of activation) is called the kinetic product.

**Definition 3.9.3 (Thermodynamic Control)** When the steps that form the products are reversible and equilibrium is reached within the reaction time, the ratio of the products is determined by their relative stability,

$$
\frac{[\ce{B}]}{[\ce{C}]} = \exp\left(-\frac{G^\circ(\ce{B}) - G^\circ(\ce{C})}{RT}\right),
$$
independent of the pathway, and this situation is called **thermodynamic control**; the more stable product is called the thermodynamic product.

If the pathway with the lower Gibbs energy of activation also gives the more stable product, the two kinds of control give the same major product and need not be distinguished; only when the product that forms faster is not the more stable one do the reaction conditions determine the result. Low temperature, short time and irreversible conditions then give the kinetic product; high temperature, long time and reversible conditions give the thermodynamic product.

![Kinetic and thermodynamic control. Top: A forms B over a lower barrier and the more stable C over a higher barrier; bottom: the rate constants at 298 K from the Eyring equation, and the composition against time obtained from the matrix exponential of the first-order rate matrix. At short times B dominates (B : C equals the ratio of the forward rate constants, about 56 : 1); the reverse reaction of B is very slow, and only after hours to a day does the system reach equilibrium, in which C dominates (C : B about 56 : 1)](./plots/kinetic-thermodynamic-control.py)

The composition in the figure is the solution $\boldsymbol{x}(t) = \mathrm{e}^{Kt}\boldsymbol{x}(0)$ of the linear system of ordinary differential equations $\frac{\mathrm{d}\boldsymbol{x}}{\mathrm{d}t} = K\boldsymbol{x}$ ([2.4](/2.4); a unified treatment of opposing, parallel and consecutive reactions is in [6.3.15](/6.3.15#sec-15.4.4)). The two time scales differ greatly: $k_1 \approx 0.06\,\mathrm{s^{-1}}$ converts A within a minute, whereas the rate constant for B returning to A is only about $10^{-3}\,\mathrm{s^{-1}}$, and most of the A formed returns to B again, so relaxation to thermodynamic equilibrium is much slower. In such a system "the time at which the reaction is stopped" determines the product.

Typical examples are the addition of HBr to buta-1,3-diene, which gives mainly the 1,2-adduct at low temperature and mainly the more stable 1,4-adduct above room temperature ([6.5.11](/6.5.11#sec-11.6.2)); the deprotonation of an unsymmetrical ketone with LDA at $-78\,^\circ\mathrm{C}$, which gives the less substituted kinetic enolate, whereas under reversible conditions the more substituted thermodynamic enolate forms ([6.5.21](/6.5.21#sec-21.3.2)); and the sulfonation of naphthalene, which gives naphthalene-1-sulfonic acid at 80 °C and naphthalene-2-sulfonic acid at 160 °C ([6.5.15](/6.5.15#sec-15.6.2)).

### 3.9.3. The Curtin–Hammett Principle

Another common situation is that the reactant itself exists in two rapidly interconverting forms (**conformers**, **tautomers** or rapidly interconverting isomers), each of which gives a different product.

**Definition 3.9.4 (Curtin–Hammett Principle)** If the interconversion of two reactant forms $\mathrm{A_1}$ and $\mathrm{A_2}$ is much faster than their reactions to the products $\mathrm{P_1}$ and $\mathrm{P_2}$, the product ratio depends only on the difference between the Gibbs energies of the two transition states,

$$
\frac{[\mathrm{P_1}]}{[\mathrm{P_2}]} = \exp\left(-\frac{G^\circ(\mathrm{TS_1}) - G^\circ(\mathrm{TS_2})}{RT}\right),
$$
and not on the equilibrium composition of $\mathrm{A_1}$ and $\mathrm{A_2}$. This conclusion is called the **Curtin–Hammett principle**.

**Proof** The fast equilibrium keeps $[\mathrm{A_2}]/[\mathrm{A_1}] = K = \exp(-[G^\circ(\mathrm{A_2}) - G^\circ(\mathrm{A_1})]/RT)$ constant throughout the reaction, so

$$
\frac{\mathrm{d}[\mathrm{P_1}]/\mathrm{d}t}{\mathrm{d}[\mathrm{P_2}]/\mathrm{d}t} = \frac{k_1[\mathrm{A_1}]}{k_2[\mathrm{A_2}]} = \frac{k_1}{k_2K}.
$$
By the Eyring equation $k_i \propto \exp(-[G^\circ(\mathrm{TS}_i) - G^\circ(\mathrm{A}_i)]/RT)$, and on substitution the Gibbs energies of both $\mathrm{A_1}$ and $\mathrm{A_2}$ cancel, leaving only $\exp(-[G^\circ(\mathrm{TS_1}) - G^\circ(\mathrm{TS_2})]/RT)$. The ratio does not change with time and is therefore also the final product ratio. $\square$

The significance of this principle is that it corrects a common error of reasoning: "the major conformer reacts to give the major product." In fact, a conformer present in very small amount that reacts through a lower transition state can still give the major product; the equilibrium composition matters only when interconversion is slower than reaction (which is then kinetic control in the sense of Definition 3.9.2). The **ring flip** of cyclohexane derivatives ($\Delta^{\ddagger}G^\circ \approx 45\,\mathrm{kJ\,mol^{-1}}$, about $10^5$ times per second at room temperature, [6.5.4](/6.5.4#sec-4.5.3)) is almost always faster than their reactions, so reactions of conformers generally obey the Curtin–Hammett principle; for example the **E2** elimination of chloromenthanes can proceed only through the minor conformer in which chlorine is axial ([6.5.9](/6.5.9#sec-9.4.4)).

## 3.10. The Hammond Postulate

Thermodynamics and kinetics of a reaction are not completely unrelated: factors that stabilize the product (such as the degree of substitution of a radical or **carbocation**) usually act partly in the transition state as well, so that among similar reactions the more exothermic ones are often faster. The Hammond postulate describes the extent of this correlation.

**Definition 3.10.1 (Hammond Postulate)** Two states that are adjacent on the reaction coordinate and close in energy are also similar in structure. Therefore the transition state of a strongly exothermic step occurs early and resembles the reactants, and the transition state of a strongly endothermic step occurs late and resembles the product (or intermediate). This corollary is called the **Hammond postulate**.

Radical halogenation is the clearest example (see [6.5.7](/6.5.7#sec-7.7.3)). Abstraction of a hydrogen from propane by a chlorine atom or a bromine atom:

| Step | $\Delta_{\mathrm{r}}H^\circ$ / (kJ mol⁻¹) | Transition state | Relative reactivity of secondary and primary H (per H) |
|---|---|---|---|
| $\ce{Cl^{\bullet} + CH3CH2CH3 -> HCl + CH3CH2CH2^{\bullet}}$ | ca. $-9$ | Early, close to reactants | |
| $\ce{Cl^{\bullet} + CH3CH2CH3 -> HCl + (CH3)2CH^{\bullet}}$ | ca. $-19$ | Early, close to reactants | ca. $4 : 1$ (25 °C) |
| $\ce{Br^{\bullet} + CH3CH2CH3 -> HBr + CH3CH2CH2^{\bullet}}$ | ca. $+57$ | Late, close to the radical | |
| $\ce{Br^{\bullet} + CH3CH2CH3 -> HBr + (CH3)2CH^{\bullet}}$ | ca. $+47$ | Late, close to the radical | ca. $80 : 1$ (125 °C) |

(Calculated from the bond dissociation energies in the table of [6.5.7](/6.5.7#def-7.2.2): $\ce{CH3CH2CH2-H}$ 423, $\ce{(CH3)2CH-H}$ 413, H–Cl 432, H–Br $366\,\mathrm{kJ\,mol^{-1}}$.) Chlorination is exothermic, only a small part of the C–H bond is broken in the transition state, and the difference in stability between secondary and primary radicals (about $10\,\mathrm{kJ\,mol^{-1}}$) shows up only slightly in the transition state, so the selectivity is low; bromination is endothermic, the transition state resembles the radical, almost all of the difference in radical stability shows up in the activation energy, and the selectivity is high. This is one source of the rule of thumb "the higher the reactivity, the lower the selectivity".

The Hammond postulate is qualitative. A related quantitative empirical relation is the Bell–Evans–Polanyi relation: within a family of reactions the activation energy is approximately linear in the reaction enthalpy, $E_{\mathrm{a}} = E_0 + \alpha\Delta_{\mathrm{r}}H$, with $0 < \alpha < 1$; $\alpha$ is small for an early transition state and close to 1 for a late one. The most important use of the Hammond postulate is to infer the energy of the transition state of the step that forms an intermediate from the stability of that intermediate: in **SN1** reactions, **electrophilic addition** and **electrophilic aromatic substitution**, the step that forms the carbocation is a strongly endothermic rate-determining step with a transition state close to the carbocation, so every factor that stabilizes the carbocation accelerates the reaction ([6.5.8](/6.5.8#sec-8.5.2), [6.5.11](/6.5.11#sec-11.3.1), [6.5.14](/6.5.14#sec-14.2.1)).

## 3.11. Methods for Studying Reaction Mechanisms

### 3.11.1. Rate Laws and Mechanisms

A **reaction mechanism** is the sequence of all the **elementary reactions** through which a reaction proceeds, together with the order of bond breaking and bond formation, the energy changes and the stereochemistry in each step. A mechanism cannot be proved, only excluded by experiment: a reasonable mechanism must be compatible with all the experimental facts, and studying a mechanism means designing experiments that distinguish between several possible mechanisms.

The most basic evidence is the **rate law**. For a reaction $m\ce{A} + n\ce{B} \to$ products, the experimentally measured $v = k[\ce{A}]^a[\ce{B}]^b$ gives the **reaction order** $a + b$. The order is determined by experiment, is in general not equal to the stoichiometric coefficients, and is not necessarily equal to the molecularity of the rate-determining step: the rate law reflects the composition of the rate-determining step and the steps before it ([6.3.15](/6.3.15#sec-15.6)). Take the hydrolysis of 2-bromo-2-methylpropane (*tert*-butyl bromide) in water as an example:

![The SN1 hydrolysis of 2-bromo-2-methylpropane has three elementary steps: (1) heterolysis of the C–Br bond to give the tert-butyl cation (slow, rate-determining); (2) attack of water on the carbocation to give an oxonium ion (fast); (3) proton transfer to another water molecule to give 2-methylpropan-2-ol (fast)](./plots/sn1-hydrolysis.py)

The rate-determining step involves only *tert*-butyl bromide, so $v = k[\ce{(CH3)3CBr}]$, independent of the concentration of the nucleophile (water or $\ce{OH-}$); the one-step substitution of chloromethane with $\ce{OH-}$ ([6.5.1](/6.5.1#sec-1.2.2), part (a) of the figure) has $v = k[\ce{CH3Cl}][\ce{OH-}]$. These two rate laws distinguish the **SN1** and **SN2** mechanisms ([6.5.8](/6.5.8#sec-8.2)).

Several points about order need attention:

- The rate-determining step of a first-order reaction is not necessarily unimolecular: if there is a fast pre-equilibrium before the rate-determining step, or if the other reactant is in large excess (the solvent water), the apparent order is lowered; the latter is called a **pseudo-first-order reaction**. The SN1 hydrolysis in water is first order, but this alone cannot exclude participation of water in the rate-determining step.
- Zero order occurs not only in reactions with a catalyst surface that is saturated: whenever the rate is independent of the concentration of a reactant, the order in that species is zero; for example SN1 reactions are zero order in the nucleophile, and enzymes are zero order in the substrate at substrate saturation ([6.3.17](/6.3.17)).
- The rate law of a multistep reaction can be derived from the mechanism by the **steady-state approximation** or the pre-equilibrium approximation and then compared with experiment ([6.3.15](/6.3.15#sec-15.6)).

### 3.11.2. Products, Intermediates and Stereochemistry

- Products and byproducts: complete identification of all products (including minor byproducts) often directly excludes certain mechanisms. For example, rearranged products accompanying an SN1 reaction show the presence of a **carbocation** ([6.5.8](/6.5.8#sec-8.3.3)).
- Detection and trapping of intermediates: carbocations can be observed directly by NMR in superacids at low temperature (Olah); radicals can be detected by EPR or trapped with radical traps such as TEMPO ([6.5.7](/6.5.7#sec-7.4.2)); **benzyne** can be trapped by furan in a Diels–Alder reaction ([6.5.15](/6.5.15#sec-15.1.4)). If the reaction is inhibited or a trapped product is formed when a trapping agent is added, this supports the existence of the intermediate.
- In situ spectroscopy and fast kinetics: online IR and NMR monitoring and fast methods such as stopped flow and flash photolysis ([6.3.15](/6.3.15)) can follow the formation and disappearance of intermediates.
- Stereochemistry: the stereochemistry of the product is often decisive evidence for distinguishing mechanisms, such as the inversion of configuration in SN2 reactions ([6.5.8](/6.5.8#sec-8.4.1)), the requirement of anti coplanarity in E2 reactions ([6.5.9](/6.5.9#sec-9.4.2)) and the **stereospecificity** of pericyclic reactions ([6.5.12](/6.5.12#sec-12.3.4)).
- Computation: calculating the energies of the transition states and intermediates of the various pathways by quantum chemical methods is now a routine tool of mechanistic study, and the results must be corroborated by experiment (rates, selectivity, isotope effects).

![Trapping a radical intermediate with TEMPO: the persistent nitroxide radical TEMPO (2,2,6,6-tetramethylpiperidin-1-yloxyl) neither abstracts hydrogen nor starts chains, but couples with carbon radicals almost at the diffusion limit; one electron from each radical (fishhook arrows) forms the new C–O bond of an alkoxyamine that can be isolated and identified](./plots/tempo-trap.py)

### 3.11.3. Isotopic Labeling and Crossover Experiments

Labeling specific atoms of a reactant with **isotopes** such as ²H, ¹³C, ¹⁸O and ¹⁵N and then determining the position of the labeled atom in the product by mass spectrometry or NMR allows the breaking and forming of bonds to be traced. Classic examples are the esterification of an ¹⁸O-labeled alcohol, in which ¹⁸O appears in the ester and not in the water, showing that the C–O bond of the carboxylic acid is the one that breaks ([6.5.19](/6.5.19#sec-19.4.1)); and the reaction of ¹⁴C-labeled chlorobenzene with $\ce{NaNH2}$, in which half of the label appears on the carbon that carries the amino group and half on the adjacent carbon, proving a symmetrical benzyne intermediate ([6.5.15](/6.5.15#sec-15.1.1)).

![¹⁸O labeling in the acid-catalyzed esterification of acetic acid with methanol: the labeled oxygen of methanol attacks the carbonyl carbon of the protonated acid, and after proton transfer the water that leaves carries an oxygen of the acid, so the label ends up in the ester ($\ce{CH3C(=O)-^{18}OCH3}$) and not in the water. The acyl C–O bond breaks, not the alkyl C–O bond of methanol](./plots/isotope-esterification.py)

**Definition 3.11.1 (Crossover Experiment)** An experiment in which two structurally similar reactants carrying different labels (isotopes or substituents) react together in the same system, and the products are examined for "crossover products" in which the two labels are exchanged, in order to decide whether the migrating group ever leaves the molecule, is called a **crossover experiment**.

The absence of crossover products shows that the migration occurs within the molecule (the group never leaves the original molecule, as in the concerted Claisen rearrangement, [6.5.12](/6.5.12#sec-12.5.6)); the presence of crossover products shows that the group existed as an independent fragment (an ion or a radical) that combined with another molecule outside the solvent cage (as in part of the pathway of the Fries rearrangement, [6.5.15](/6.5.15#sec-15.8.3)).

### 3.11.4. Kinetic Isotope Effects

The change in rate when an H taking part in the reaction is replaced by D is called the **kinetic isotope effect** and is expressed as $k_{\mathrm{H}}/k_{\mathrm{D}}$. Its main source is the zero-point energy ([6.3.16](/6.3.16#sec-16.2.3)): the reduced mass of a C–D bond is larger, its stretching frequency is about $1/1.36$ that of C–H, and its zero-point energy is lower; if the C–H bond is broken in the transition state, this stretching vibration becomes the reaction coordinate and the difference in zero-point energy disappears in the transition state, so the C–D bond needs more activation energy. With a C–H stretching vibration $\tilde\nu = 2900\,\mathrm{cm^{-1}}$ (C–D about $2130\,\mathrm{cm^{-1}}$), the difference in zero-point energy is estimated as $\frac12 hc\Delta\tilde\nu N_{\mathrm{A}} \approx 4.6\,\mathrm{kJ\,mol^{-1}}$, so

$$
\frac{k_{\mathrm{H}}}{k_{\mathrm{D}}} \approx \exp\left(\frac{4.6\,\mathrm{kJ\,mol^{-1}}}{RT}\right) \approx 6.4 \quad (298\,\mathrm{K}).
$$

On this basis one can distinguish:

| Type | $k_{\mathrm{H}}/k_{\mathrm{D}}$ (25 °C) | Meaning | Example |
|---|---|---|---|
| Primary isotope effect | ca. 2–8 | The bond to the isotope breaks in the rate-determining step | E2 elimination (ca. 7, [6.5.9](/6.5.9#sec-9.4.1)); halogenation of ketones (enolization is rate-determining, [6.5.21](/6.5.21#sec-21.5.1)) |
| Very large primary effect | > 10 | The H atom tunnels through the barrier | Some enzymatic and radical H transfers |
| Secondary isotope effect | ca. 0.7–1.4 | The bond to the isotope does not break, only the hybridization etc. changes | The effect of $\alpha$-D in SN1 reactions is about 1.1–1.2 |
| No isotope effect | ca. 1 | Breaking of the C–H bond is not in the rate-determining step | Nitration of benzene (formation of the **σ complex** is rate-determining, [6.5.14](/6.5.14#sec-14.2.2)) |

The primary isotope effect is greatest when H lies symmetrically between donor and acceptor in the transition state, and is smaller for earlier or later transition states, so its magnitude also gives information about the structure of the transition state.

![Origin of the primary kinetic isotope effect: in the reactant well the zero-point energies of the C–H and C–D stretches are about 17.3 and 12.7 kJ/mol (2900 and 2130 cm⁻¹); at the transition state this stretch has become the reaction coordinate, so both isotopologues reach approximately the same top, and the C–D compound needs about 4.6 kJ/mol more activation energy, $k_{\mathrm{H}}/k_{\mathrm{D}} \approx 6.4$ at 298 K](./plots/kie-zpe.py)

## Summary

- The smaller the $\mathrm{p}K_{\mathrm{a}}$, the stronger the acid; the equilibrium constant of a proton transfer is $K = 10^{\mathrm{p}K_{\mathrm{a}}(\text{product acid}) - \mathrm{p}K_{\mathrm{a}}(\text{reactant acid})}$ (Eq. (3.1)), each unit corresponding to $5.71\,\mathrm{kJ\,mol^{-1}}$; the $\mathrm{p}K_{\mathrm{a}}$ of water is taken as 14.00 and that of $\ce{H3O+}$ as 0 (15.7 and $-1.7$ come from writing 55.5 M into the expression). The $\mathrm{p}K_{\mathrm{a}}$ values of the whole course are those of Tables 3.1–3.3: CRC values in water, and Bordwell values in DMSO for weak C–H and N–H acids, with the solvent stated.
- The more stable the conjugate base, the stronger the acid: charged atom (electronegativity within a period, atomic size within a group) > resonance > induction > hybridization; aromaticity makes cyclopentadiene acidic. Basicity is the mirror image.
- Solvation determines acidity in solution: small anions with concentrated charge are stabilized by hydrogen bonding in water and are unstable in DMSO and acetonitrile, so the $\mathrm{p}K_{\mathrm{a}}$ rises by 7–17; delocalized anions are less affected. The leveling effect limits the measurable range in water to about $-2$ to 16.
- Lewis acid–base theory includes all polar reactions (nucleophile = Lewis base, electrophile = Lewis acid); the principle of hard and soft acids and bases explains the selectivity of substitution versus elimination, 1,2- versus 1,4-addition, and O versus C reaction of ambident nucleophiles.
- The Hammett equation (Definition 3.5.1) $\lg(k_{\mathrm{X}}/k_{\mathrm{H}}) = \rho\sigma$: $\sigma_m$ is mainly the inductive effect, $\sigma_p$ contains the conjugation effect, and $\sigma^+$ and $\sigma^-$ are used for through-conjugation; $\rho > 0$ means accumulation of negative charge and $\rho < 0$ of positive charge.
- $\Delta_{\mathrm{r}}G^\circ = -RT\ln K^\circ$ (Eq. (3.3)) determines the extent of reaction and $\Delta^{\ddagger}G^\circ$ determines the rate (Eyring equation, Eq. (3.4)); at room temperature $90$–$100\,\mathrm{kJ\,mol^{-1}}$ corresponds to hours, and at $-78\,^\circ\mathrm{C}$ only reactions below about $60\,\mathrm{kJ\,mol^{-1}}$ proceed. The error of a reaction enthalpy estimated from bond enthalpies is about $10$–$20\,\mathrm{kJ\,mol^{-1}}$; a reaction that reduces the number of molecules is entropically unfavorable and reverses at high temperature.
- Kinetic control (Definition 3.9.2): the product ratio is set by $\Delta\Delta^{\ddagger}G^\circ$ (low temperature, short time, irreversible); thermodynamic control (Definition 3.9.3): set by the $\Delta G^\circ$ of the products (high temperature, long time, reversible). Curtin–Hammett principle (Definition 3.9.4): for rapidly interconverting reactant forms, the product ratio depends only on the Gibbs energy difference of the two transition states.
- The Hammond postulate (Definition 3.10.1): exothermic steps have early transition states (resembling reactants) and endothermic steps have late transition states (resembling products); it explains why bromination is more selective than chlorination and why factors that stabilize the carbocation accelerate SN1 and similar reactions.
- Mechanistic study: rate law (order ≠ stoichiometry), products and intermediates (detection, trapping), stereochemistry, isotopic labeling and crossover experiments (Definition 3.11.1), kinetic isotope effects (primary ca. 2–8, zero-point estimate about 6.4; about 1 means that C–H cleavage is not rate-determining).

## Questions

1. Decide whether each statement is correct: (a) a one-step exothermic reaction has $\Delta_{\mathrm{r}}H < 0$; (b) the transition state of a one-step endothermic reaction is closer to the product than that of an exothermic reaction; (c) in a two-step reaction, the step with the larger activation energy (relative to the preceding intermediate) is necessarily the rate-determining step; (d) the forward and reverse activation energies of a one-step reaction are equal.

   **Answer** (a) Correct; "exothermic" means $\Delta_{\mathrm{r}}H < 0$. (b) Correct (Hammond postulate). (c) Wrong: the rate-determining step is determined by the transition state of highest Gibbs energy relative to the starting material; if the intermediate formed in the first step is of high energy, the transition state of the second step may be the highest point of the whole profile, even though the activation energy of the second step itself (relative to the intermediate) is smaller. (d) Wrong: the reverse activation energy equals $\Delta^{\ddagger}G^\circ - \Delta_{\mathrm{r}}G^\circ$, and the two are equal only when $\Delta_{\mathrm{r}}G^\circ = 0$.
2. At 298 K, what is the fraction of B at equilibrium for the isomerization $\ce{A <=> B}$ when $\Delta_{\mathrm{r}}G^\circ$ is $+1$, $-1$, $-2$ and $-10\,\mathrm{kcal\,mol^{-1}}$?

   **Answer** $K^\circ = \exp(-\Delta_{\mathrm{r}}G^\circ/RT)$ with $RT = 0.5925\,\mathrm{kcal\,mol^{-1}}$: for $+1$, $K^\circ = 0.185$ and B is 16%; for $-1$, $K^\circ = 5.4$ and 84%; for $-2$, $K^\circ = 29$ and 97%; for $-10$, $K^\circ = 2.2\times10^7$ and > 99.99%.
3. A first-order reaction has a half-life of 1.5 min at 20 °C. Estimate its $\Delta^{\ddagger}G^\circ$; if $\Delta^{\ddagger}S^\circ \approx 0$, about what is its half-life at 100 °C?

   **Answer** $k = \ln2/90\,\mathrm{s} = 7.7\times10^{-3}\,\mathrm{s^{-1}}$; $\Delta^{\ddagger}G^\circ = RT\ln\frac{k_{\mathrm{B}}T}{hk} = 8.314 \times 293.15 \times \ln\frac{6.11\times10^{12}}{7.7\times10^{-3}}\,\mathrm{J\,mol^{-1}} \approx 83.7\,\mathrm{kJ\,mol^{-1}}$ (20 kcal mol⁻¹). When $\Delta^{\ddagger}S^\circ \approx 0$, $\Delta^{\ddagger}G^\circ$ hardly changes with temperature, and at 373 K $k = 7.78\times10^{12}\exp(-83700/(8.314\times373.15))\,\mathrm{s^{-1}} \approx 15\,\mathrm{s^{-1}}$, $t_{1/2} \approx 0.05\,\mathrm{s}$, in agreement with the table in 3.8.
4. Two sets of reactions have the following energy diagrams. In the first set, the barrier for A + B to form C is lower and C is higher in energy, the barrier to form D is higher and D is lower in energy, and both barriers are far too high for the reverse reactions of the products to occur; in the second set the situation is the same, but the barriers for the reverse reactions of both products are low. Which set is under thermodynamic control and which under kinetic control? What is the major product in each?

   **Answer** In the first set the products cannot revert, so it is under kinetic control and the major product is C, which forms faster; in the second set the products can interconvert through A + B and reach equilibrium, so it is under thermodynamic control and the major product is the more stable D.
5. A cyclohexane derivative has a substituent that can be axial or equatorial; the two conformers interconvert about $10^5$ times per second, and at equilibrium the equatorial conformer is 95%. Only the axial conformer can undergo reaction 1 through a lower transition state, and the equatorial conformer undergoes reaction 2 through another transition state. What determines the product ratio? Does the predominance of the equatorial conformer mean that the product of reaction 2 predominates?

   **Answer** Conformational interconversion is much faster than reaction, so the Curtin–Hammett principle applies: the product ratio is determined only by the Gibbs energy difference of the two transition states, $[\mathrm{P_1}]/[\mathrm{P_2}] = \exp(-[G^\circ(\mathrm{TS_1}) - G^\circ(\mathrm{TS_2})]/RT)$. The conformational equilibrium is only part of this difference ($G^\circ(\mathrm{TS}_i) = G^\circ(\mathrm{A}_i) + \Delta^{\ddagger}G^\circ_i$), so if the activation energy of the reaction of the axial conformer is low enough that the absolute Gibbs energy of $\mathrm{TS_1}$ is below that of $\mathrm{TS_2}$, the product of reaction 1 still predominates, even though the axial conformer is only 5%.
6. (a) Can aqueous NaOH convert acetone to its enolate to a significant extent? (b) Why is LDA in THF needed to generate the enolate of acetone quantitatively? (c) Can a solution of $\ce{NaOCH2CH3}$ in ethanol deprotonate diethyl malonate completely?

   **Answer** (a) $K = 10^{14.00 - 19.3} = 10^{-5.3}$, so only a very small fraction is present as the enolate at equilibrium, but this is enough to catalyze reactions such as the aldol condensation (the enolate is continuously consumed and formed again). (b) In THF, diisopropylamine (ca. 36) is far weaker as an acid than acetone (26.5 in DMSO), $K \approx 10^{9}$, and the deprotonation is quantitative and irreversible; THF contains no protons that can be removed and does not level the strong base. (c) Diethyl malonate has $\mathrm{p}K_{\mathrm{a}}$ about 13 in water, about $10^{3}$ times more acidic than ethanol (15.9), $K \approx 10^{3}$, and the deprotonation is essentially complete; this is the basis of the **malonic ester synthesis** ([6.5.22](/6.5.22#sec-22.9)).
7. The alkaline hydrolysis of substituted ethyl benzoates has $\rho = +2.5$. (a) By what factor is ethyl 4-nitrobenzoate faster than ethyl benzoate? And ethyl 4-methoxybenzoate? (b) What does the positive $\rho$ indicate?

   **Answer** (a) $\lg(k_{\mathrm{X}}/k_{\mathrm{H}}) = 2.5 \times 0.78 = 1.95$, faster by about a factor of 90; for *para*-methoxy, $2.5 \times (-0.27) = -0.68$, slower by about a factor of 4.7. (b) Electron-withdrawing groups accelerate the reaction, showing that negative charge accumulates near the ester carbonyl group in the rate-determining step: addition of $\ce{OH-}$ to the carbonyl group to form a negatively charged tetrahedral intermediate is rate-determining ([6.5.19](/6.5.19#sec-19.4.2)).
8. In one reaction the rate falls to $1/6.5$ when a C–H of the substrate is replaced by C–D; in another reaction $k_{\mathrm{H}}/k_{\mathrm{D}} = 1.0$. What does each indicate?

   **Answer** The first reaction has a primary kinetic isotope effect close to the maximum zero-point estimate, showing that the C–H bond breaks in the rate-determining step and that H lies roughly symmetrically between donor and acceptor in the transition state. The second has no isotope effect, so cleavage of the C–H bond is not in the rate-determining step (it may break in a fast step after the rate-determining step, as in the deprotonation of the σ complex in electrophilic aromatic substitution).
