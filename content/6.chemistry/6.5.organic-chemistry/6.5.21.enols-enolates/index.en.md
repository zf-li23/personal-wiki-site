---
title: Enols and Enolates
description: Acidity of the α-hydrogens of carbonyl compounds and the choice of base; keto–enol tautomerism (Kresge's enolization constants, acid and base catalysis, deuteration and racemization, effects of structure and solvent); structure of enolates, kinetic and thermodynamic enolates, ambident reactivity; α-halogenation and the haloform reaction; the Mannich reaction and the synthesis of tropinone; alkylation of enolates and Myers asymmetric alkylation; the Stork enamine reaction.
source_hash: d2a53fd25441
---

In the preceding chapters the carbonyl group always appeared as an **electrophile**: a **nucleophile** attacks the electron-poor carbonyl carbon ([6.5.16](/6.5.16#sec-16.2), [6.5.17](/6.5.17#sec-17.6)), or **nucleophilic acyl substitution** takes place at a carboxylic acid derivative ([6.5.19](/6.5.19#sec-19.2)). The carbonyl group has another side. It makes the C–H bonds on the adjacent α carbon acidic; loss of a proton gives an enolate, in which the negative charge is delocalized onto oxygen, and the carbonyl compound can also be converted by proton transfer into its isomer, the enol. Both enols and enolates are electron-rich carbon nucleophiles, so a carbonyl compound can serve as an electrophile and as a nucleophile; combining the two gives the aldol reaction and the **Claisen condensation**, the most important family of carbon–carbon bond-forming reactions ([6.5.22](/6.5.22)). This chapter first treats the acidity of α-hydrogens and keto–enol tautomerism, then the formation, **regioselectivity**, and ambident reactivity of enolates, then the reactions that need only a weak nucleophile (α-halogenation, the haloform reaction, and the Mannich reaction), and finally the alkylation of enolates and **enamines**. It makes heavy use of the unified p$K_{\mathrm{a}}$ table of [6.5.3](/6.5.3#sec-3.1.4) and of the notions of **kinetic control** and **thermodynamic control**; the alkylation step is the **SN2 reaction** of [6.5.8](/6.5.8#sec-8.2.2), and the formation of enamines is in [6.5.16](/6.5.16#sec-16.9.3). Many carbon–carbon bond formations and cleavages in living systems also proceed through enol or enamine intermediates; these are treated together in Section 22.10 of the next chapter.

## 21.1. Acidity of the α-Hydrogens

### 21.1.1. The α Carbon and Carbon Acids

**Definition 21.1.1** The carbon atom directly attached to a functional group (here the carbonyl group) is called the **alpha carbon**, and the hydrogens on it are called **alpha hydrogens**; the carbons further out are the β and γ carbons in turn.

Any C–H bond can in principle give its proton to a base, so hydrocarbons and other compounds containing C–H bonds can be regarded as "carbon acids", whose acidity is measured by $\mathrm{p}K_{\mathrm{a}}$. Alkanes have $\mathrm{p}K_{\mathrm{a}}$ values of about 50 and are scarcely acidic; a C–H bond next to a carbonyl group is more than 30 orders of magnitude more acidic. The factors that govern C–H acidity are the same as for O–H and N–H acids ([6.5.3](/6.5.3#sec-3.2)); in each case the key is the stability of the conjugate base (the **carbanion**):

- **Inductive effect**: an electron-withdrawing group on the α carbon increases the acidity.
- Delocalization: when the negative charge can be delocalized onto an atom of high **electronegativity**, the acidity is greatly enhanced. The difference between the allylic C–H of propene (about 43) and cyclopentadiene (about 16, giving the cyclopentadienyl anion, which has **aromaticity**, [6.5.13](/6.5.13#sec-13.5.1)) is the effect of delocalization and aromaticity.
- Geometry: delocalization requires the C–H bond to be parallel to the π system of the carbonyl group, so that the lone pair of the carbanion can overlap with π*. If the rigidity of a ring makes this alignment impossible (for example a bridgehead α-H, whose enolate would require a bridgehead double bond, Bredt's rule, [6.5.9](/6.5.9#sec-9.1)), that α-H is hardly acidic at all.
- Solvent: an enolate, whose negative charge is concentrated on oxygen, is stabilized by **hydrogen bonds** in **protic solvents**; in **polar aprotic solvents** such as DMSO all $\mathrm{p}K_{\mathrm{a}}$ values are higher ([6.5.3](/6.5.3#sec-3.3)), but the order among different acids is largely unchanged.

### 21.1.2. The α-Hydrogens of Carbonyl Compounds

The α-H of a carbonyl compound is strongly acidic mainly because the negative charge of the conjugate base can be delocalized onto the electronegative oxygen: of the two **resonance structures** of the enolate, the one with the charge on oxygen contributes more. In addition, the **inductive effect** of the carbonyl group and the **hyperconjugation** between the C–H bond and π*(C=O) weaken the C–H bond.

![Reaction of a carbonyl compound with a base is a proton transfer: the base removes the α-H that is parallel to the π system, the electrons of the C–H bond become the π bond of C=C, and the π electrons of C=O move onto oxygen; the enolate formed is written as two resonance structures, a carbanion form and an oxyanion form](./plots/enolate-formation.py)

The table below is taken from the [unified p$K_{\mathrm{a}}$ table of 6.5.3](/6.5.3#sec-3.1.4) (Tables 3.2 and 3.3). The $\mathrm{p}K_{\mathrm{a}}$ of a carbonyl compound refers to the equilibrium in which the keto form loses an α-H to give the enolate.

| Compound | $\mathrm{p}K_{\mathrm{a}}$ of α-H (water) | $\mathrm{p}K_{\mathrm{a}}$ (DMSO) |
|---|---|---|
| $\ce{CH3CHO}$ | 16.7 | — |
| $\ce{C6H5COCH3}$ | 18.3 | 24.7 |
| $\ce{CH3COCH3}$ | 19.3 | 26.5 |
| $\ce{CH3COOC2H5}$ | About 25 | — |
| $\ce{CH3CN}$ | About 29 | 31.3 |
| $\ce{CH3NO2}$ | 10.2 | 17.2 |
| $\ce{CH2(COOC2H5)2}$ (diethyl malonate) | About 13 | 16.4 |
| $\ce{CH3COCH2COOC2H5}$ (ethyl acetoacetate) | 10.7 | 14.2 |
| $\ce{CH3COCH2COCH3}$ (acetylacetone) | 8.9 | 13.3 |

Several trends:

- Aldehyde > ketone > ester ≈ nitrile > amide. A ketone has one more electron-donating alkyl group than an aldehyde; the alkoxy group of an ester and the amino group of an amide conjugate their lone pairs with the carbonyl group and weaken its ability to accept the negative charge of the α carbon, so the α-H of an ester is about 6 $\mathrm{p}K_{\mathrm{a}}$ units weaker than that of a ketone.
- The nitro group is a stronger electron-withdrawing and delocalizing group than the carbonyl group, and nitromethane is about as acidic as phenol.
- When a $\ce{CH2}$ group lies between two electron-withdrawing groups (**1,3-dicarbonyl compounds**, Section 22.7), the negative charge is delocalized onto two oxygens and the $\mathrm{p}K_{\mathrm{a}}$ falls to 9–13, more acidic than water and alcohols.

Acidities of different acids must be compared using data from the same solvent.

### 21.1.3. Choice of Base

Deprotonation is an acid–base equilibrium whose position is determined by the difference between the $\mathrm{p}K_{\mathrm{a}}$ of the carbonyl compound and that of the conjugate acid of the base ([6.5.3](/6.5.3#sec-3.1.2)):

$$
\ce{R2CH-COR' + B- <=> R2C=C(O^-)R' + BH}, \qquad \lg K = \mathrm{p}K_{\mathrm{a}}(\ce{BH}) - \mathrm{p}K_{\mathrm{a}}(\ce{R2CH-COR'}).
$$

| Base | $\mathrm{p}K_{\mathrm{a}}$ of conjugate acid | $\lg K$ with acetone (19.3) | Result |
|---|---|---|---|
| NaOH | 14.00 (water) | About $-5$ | Only a very small amount of enolate (reversible; enough to catalyze the aldol reaction) |
| $\ce{NaOCH2CH3}$ | 15.9 (ethanol) | About $-3.4$ | A small amount of enolate, reversible |
| NaH | About 35 ($\ce{H2}$, estimated) | Very large | Quantitative; heterogeneous, evolves $\ce{H2}$, rather slow |
| LDA | About 36 (diisopropylamine, THF) | About $+17$ | Fast, quantitative, irreversible |
| $\ce{NaNH2}$ | 41 ($\ce{NH3}$, DMSO) | Very large | Quantitative, but with strong **nucleophilicity**, so it adds to the carbonyl group |

(The $\lg K$ values in the table are rough estimates because the two $\mathrm{p}K_{\mathrm{a}}$ values come from different solvents; the reason for taking 14.00 rather than 15.7 for water is given in [6.5.3](/6.5.3#sec-3.1.3).)

*Lithium diisopropylamide*, abbreviated LDA ($\ce{LiN(i-Pr)2}$, made from diisopropylamine and $n$-BuLi in THF at $-78$ °C), is the standard base for generating enolates: it is basic enough to deprotonate all aldehydes, ketones, and esters completely, and its two isopropyl groups make it almost non-nucleophilic, so it does not add to the carbonyl group. LiHMDS and KHMDS are similar but slightly less basic. For 1,3-dicarbonyl compounds ($\mathrm{p}K_{\mathrm{a}}$ 9–13), sodium alkoxides give an essentially quantitative yield of enolate ($\lg K$ of about 3–7 with sodium ethoxide), and even $\ce{K2CO3}$ is sufficient.

The base must be matched to the reaction to be carried out. Reversible reactions that need only a catalytic amount of enolate (aldol condensation, **Claisen condensation**) use NaOH or an alkoxide; reactions that require quantitative formation of the enolate with no starting carbonyl compound remaining (alkylation, directed crossed aldol reactions) use LDA.

## 21.2. Keto–Enol Tautomerism

### 21.2.1. Tautomerism and Enol Content

**Definition 21.2.1** The rapid interconversion of two constitutional isomers, by migration of an atom or group (usually a proton) with a corresponding shift of a double bond, such that the two are in equilibrium, is called **tautomerism**; the two isomers are called tautomers. The tautomerism between a carbonyl compound $\ce{R2CH-C(=O)R'}$ (the keto form) and its **enol** $\ce{R2C=C(OH)R'}$ (the enol form) is called **keto–enol tautomerism**, and the formation of the enol from the keto form is called enolization.

Tautomers are two real compounds with their own structures and energies; the equilibrium can be measured, and in principle they can be separated. **Resonance structures**, in contrast, are merely different ways of drawing the same molecule ([6.5.1](/6.5.1#sec-1.6)). An enolate has two resonance structures; the keto and enol forms are tautomers.

For simple aldehydes and ketones the equilibrium lies almost completely on the keto side. A rough estimate from **bond enthalpies** ([6.5.3](/6.5.3#sec-3.7)): enolization replaces a C=O π bond and a C–H bond by a C=C π bond and an O–H bond, and the former pair is stronger by about $50$–$60\,\mathrm{kJ\,mol^{-1}}$. The precise enolization constant $K_{\mathrm{E}} = [\text{enol}]/[\text{ketone}]$ was measured by Kresge and coworkers by a kinetic method (the enol is first generated rapidly in solution, and the rate at which it reverts to the ketone is compared with the rate of its formation):

| Compound (water, 25 °C) | $\mathrm{p}K_{\mathrm{E}}$ | $K_{\mathrm{E}}$ |
|---|---|---|
| Acetaldehyde | 6.23 | $6\times10^{-7}$ |
| Cyclohexanone | 6.39 | $4\times10^{-7}$ |
| Acetophenone | 7.96 | $1.1\times10^{-8}$ |
| Acetone | 8.33 | $4.7\times10^{-9}$ |

For acetone, $\mathrm{p}K_{\mathrm{E}} = 8.33$ corresponds to $\Delta G^\circ = 2.303RT\,\mathrm{p}K_{\mathrm{E}} \approx 48\,\mathrm{kJ\,mol^{-1}}$. (Older literature, using bromine titration, found an enol content of acetone of about $1.5\times10^{-4}\,\%$, that is, $K_{\mathrm{E}} \approx 1.5\times10^{-6}$, about 300 times higher than the current value: the titration itself catalyzes enolization, which makes the result too high.)

The keto form, the enol form, and their common enolate form a thermodynamic cycle: the difference between the O–H acidity of the enol (acetone enol, $\mathrm{p}K_{\mathrm{a}} = 10.94$) and the C–H acidity of the keto form is $\mathrm{p}K_{\mathrm{E}}$:

$$
\mathrm{p}K_{\mathrm{a}}(\text{keto}) = \mathrm{p}K_{\mathrm{E}} + \mathrm{p}K_{\mathrm{a}}(\text{enol}) = 8.33 + 10.94 = 19.27,
$$
which is the 19.3 for acetone in the table. The acidity of an enol is similar to that of phenol, because the conjugate bases of both are the same kind of delocalized oxyanion; the keto form is only "weakly acidic" because it is so much more stable than the enol.

### 21.2.2. Acid and Base Catalysis

In pure, acid-free and base-free conditions the interconversion of ketone and enol is very slow: a direct 1,3-hydrogen shift passes through a highly strained four-membered **transition state** with a very high barrier. A trace of acid or base is enough to establish the equilibrium within seconds to hours. Both catalytic pathways consist of two proton transfers, in opposite order:

![Acid catalysis (top): the carbonyl oxygen is protonated first, and then water (or the conjugate base) removes the α-H to give the enol. Base catalysis (bottom): the base first removes the α-H to give the enolate, and oxygen then takes a proton from water to give the enol. The reverse of each pathway is the return of the enol to the keto form](./plots/enolization.py)

- Acid catalysis: protonation on oxygen first (a rapid equilibrium), then removal of the α-H by a weak base (water). The rate-determining step is the cleavage of the α-C–H bond, with rate $v = k[\text{ketone}][\ce{H3O+}]$.
- Base catalysis: removal of the α-H to give the enolate (the rate-determining step), followed by protonation on oxygen. Protonation of the enolate on oxygen gives the enol, and protonation on carbon returns the ketone; protonation on oxygen is faster (kinetic), whereas the product of protonation on carbon is more stable (thermodynamic).

Both pathways show a substantial primary **kinetic isotope effect** ($k_{\mathrm{H}}/k_{\mathrm{D}}$ about 5–7), showing that cleavage of the C–H bond is rate-determining.

### 21.2.3. Consequences of Tautomerism: Deuteration and Racemization

Enolization is reversible, and each enolization "erases" one hydrogen on the α carbon and the configuration of the α carbon:

- Deuteration: in $\ce{D2O}$ with a little NaOD (or $\ce{DCl}$), all enolizable α-hydrogens are exchanged for D one by one, while other C–H bonds are unaffected. Counting the exchanged hydrogens by mass spectrometry ([6.4.15](/6.4.15)) or $^1$H NMR tells how many α-H a molecule has: cyclohexanone exchanges 4, 2,2-dimethylcyclohexanone exchanges 2.
- **Racemization**: when the α carbon is a **stereocenter** bearing an α-H, the planar enol (or enolate) is protonated from the two faces with equal probability, and an optically active ketone gradually racemizes in acid or base ([6.5.5](/6.5.5#sec-5.6.2)). When the molecule contains other stereocenters, the configuration of the α carbon is adjusted to the thermodynamically more stable **epimer**: *trans*-2,4-disubstituted cyclohexanones are converted in base to the *cis* isomer with both substituents equatorial, and *cis*-1-decalone to *trans*-1-decalone.

![Base-catalyzed racemization: HO⁻ removes the α-H at the stereocenter of (S)-3-phenylbutan-2-one, the electrons of the C–H bond become the π bond of C=C and the π electrons of C=O move onto oxygen, giving a planar, achiral enolate; water protonates the α carbon from either face with equal probability, giving equal amounts of the (S) and (R) ketones](./plots/racemization.py)

Ingold and Wilson (1934) found that the rate of racemization of optically active *sec*-butyl phenyl ketone in acid is the same as the rate of its iodination, and that the iodination rate is independent of the iodine concentration: racemization and halogenation share the same rate-determining step, enolization (Section 21.5). To preserve the configuration of an α stereocenter in synthesis, strong acids, strong bases, and prolonged heating must be avoided; the racemization of activated amino acids in peptide synthesis through enolization (or through oxazolones) is a problem of the same kind ([6.5.33](/6.5.33)).

### 21.2.4. Factors Affecting Enol Content

The enol content of simple aldehydes and ketones is very small, but the following structural features can make the enol form important, even the major form:

| Compound | Enol content in the pure liquid | Main reason |
|---|---|---|
| Diethyl malonate | About $10^{-2}\,\%$ | The alkoxy groups of the two esters conjugate with the carbonyl groups, so enolization gains little |
| Ethyl acetoacetate | About 8 % | Conjugated enol + intramolecular **hydrogen bond** |
| Ethyl benzoylacetate | About 20 % | The enol C=C is conjugated with the benzene ring |
| Acetylacetone (pentane-2,4-dione) | About 80 % | Conjugation + intramolecular hydrogen bond in a six-membered ring |
| 1,1,1-Trifluoropentane-2,4-dione | About 97 % | Electron-withdrawing effect of $\ce{CF3}$ |
| Phenol (relative to cyclohexa-2,4-dienone) | Equilibrium constant about $10^{13}$ | **Aromaticity** |

![Keto–enol tautomerism of acetylacetone: the enol form is a conjugated O=C–C=C–OH system, and the OH forms an intramolecular hydrogen bond (dashed line) with the other carbonyl oxygen, closing a planar six-membered ring; only the (Z)-enol can form this hydrogen bond](./plots/acac-enol.py)

- Conjugation and intramolecular hydrogen bonding: the enol form of a **1,3-dicarbonyl compound** is a conjugated O=C–C=C–OH system in which the OH forms a six-membered-ring intramolecular **hydrogen bond** with the other carbonyl oxygen. The enol form is almost entirely the (Z) configuration that can form this hydrogen bond.
- Substituents: an electron-withdrawing group on the **active methylene compound** increases the enol content, whereas an electron-donating alkyl group decreases it (the enol content of 3-methylpentane-2,4-dione is clearly lower than that of acetylacetone; the substituent also repels the enol C=C plane sterically).
- Aromaticity: phenol is the enol form of a cyclohexadienone, and aromaticity pushes the equilibrium completely to the enol ([6.5.15](/6.5.15#sec-15.7)).
- Solvent: the enol content of ethyl acetoacetate is about 0.4 % in water, about 8 % in the pure liquid, and close to half in nonpolar solvents such as cyclohexane. Polar, hydrogen-bonding solvents preferentially solvate the more polar keto form (two carbonyl dipoles) and compete with the intramolecular hydrogen bond of the enol; in nonpolar solvents the intramolecular hydrogen bond stabilizes the less polar enol form.

In ethyl acetoacetate the interconversion of the two tautomers at room temperature is slower than the NMR time scale ([6.5.6](/6.5.6#sec-6.5.5)), so the $^1$H NMR spectrum shows signals for both the keto form ($\ce{CH2}$ at about 3.4 ppm) and the enol form (=CH at about 5.0 ppm, enol OH at about 12 ppm), and their ratio follows directly from the integrals. Ethyl acetoacetate behaves both as a ketone (adding HCN, $\ce{NaHSO3}$, and phenylhydrazine) and as an enol (decolorizing a solution of bromine in carbon tetrachloride, giving a violet-red color with $\ce{FeCl3}$, and evolving hydrogen with sodium metal). Both tautomers have been isolated by low-temperature handling in acid-free and base-free quartz apparatus (Knorr and K. H. Meyer, 1911); the enol form has the lower boiling point because of its intramolecular hydrogen bond.

## 21.3. Formation and Regioselectivity of Enolates

### 21.3.1. Enolates

**Definition 21.3.1** The anion formed when a carbonyl compound loses an α-H, with the negative charge delocalized between the α carbon and oxygen, $\ce{R2C=C(O^-)R' <-> R2C^--C(=O)R'}$, is called an **enolate**; its metal salts are called enolate salts.

The charge of an enolate is mainly on oxygen, but the coefficient of the **highest occupied molecular orbital** is larger on the α carbon (as in the HOMO of the allyl anion, [6.5.2](/6.5.2#sec-2.2)), and this determines its ambident reactivity (Section 21.4). In lithium, sodium, and potassium enolates the metal is bound to oxygen; in THF lithium enolates exist as aggregates such as dimers and tetramers, and the state of aggregation influences rate and selectivity.

### 21.3.2. Kinetic and Thermodynamic Enolates

An unsymmetrical ketone has two α carbons that can be deprotonated and gives two regioisomeric enolates. Take 2-methylcyclohexanone as an example:

```smiles
CC1CCCCC1=O>>CC1CCCC=C1[O-]
CC1CCCCC1=O>>CC1=C([O-])CCCC1
```

**Definition 21.3.2** When an unsymmetrical ketone is deprotonated, the enolate that is formed faster is called the **kinetic enolate**, usually the one with the less substituted double bond; the one that is more stable thermodynamically is called the **thermodynamic enolate**, usually the one with the more substituted double bond.

This is the classic example of **kinetic control** and **thermodynamic control** ([6.5.3](/6.5.3#sec-3.9.2)):

![Energy diagram for the formation of the two enolates of 2-methylcyclohexanone. Removal of the less hindered C6–H has the lower activation energy and gives the less substituted kinetic enolate; the more substituted C1=C2 enolate is more stable but forms more slowly. Under irreversible conditions the product ratio is set by the energy difference of the two transition states, under reversible conditions by the energy difference of the two enolates](./plots/kinetic-thermodynamic-enolate.py)

| | Kinetic control | Thermodynamic control |
|---|---|---|
| Base | Bulky strong base (LDA, LiHMDS), slight excess | Weaker base (NaH, KH, alkoxide, $\ce{Et3N}$), or a slight excess of ketone |
| Temperature and solvent | $-78$ °C, aprotic solvent (THF) | Room temperature or heating; protic solvent, or ketone present as a proton source |
| Reversibility | Deprotonation irreversible; no proton exchange between enolates | Enolates and ketone exchange protons continually until equilibrium is reached |
| 2-Methylcyclohexanone | About 99 : 1 in favor of the C6 side (less substituted) | In favor of the C2 side (more substituted), about 4 : 1 |

Two things account for the kinetic selectivity: C6 has two H whereas C2 has only one, and the C6–H is less hindered, so a bulky base reaches it more easily. The thermodynamic selectivity follows the stability of alkenes: the more alkyl groups on the double bond, the more stable it is (**hyperconjugation**, [6.5.9](/6.5.9#sec-9.1)). Equilibration under thermodynamic conditions is possible because the system contains both ketone (a proton donor) and enolate: each enolate can take a proton from the ketone, and the system finally drifts to the more stable one. With LDA, the same equilibration occurs if the ketone is in excess or is added too slowly, lowering the kinetic selectivity.

![Kinetic deprotonation of 2-methylcyclohexanone by LDA at −78 °C: lithium coordinates to the carbonyl oxygen, the amide nitrogen removes the H on the less hindered C6, the electrons of the C–H bond become the π bond of C=C and the π electrons of C=O move onto oxygen, giving the less substituted lithium enolate and diisopropylamine; diisopropylamine (pKa 36) is much weaker than the ketone, so this step is irreversible](./plots/lda-kinetic.py)

Either enolate can be trapped on oxygen with $\ce{Me3SiCl}$ to give a stable silyl enol ether that can be isolated and quantified (House, 1969); treating the silyl enol ether with MeLi regenerates the specified lithium enolate quantitatively, a common way to obtain a regiochemically pure enolate. The silyl enol ether is itself the **nucleophile** of the **Mukaiyama aldol reaction** (Definition 22.6.2). Another regiospecific method is to reduce an α,β-unsaturated ketone with Li/$\ce{NH3}$, or to subject it to **conjugate addition** with a copper reagent; both give the enolate at the original α carbon ([6.5.17](/6.5.17#sec-17.6.4), [6.5.17](/6.5.17#sec-17.7)).

An α,β-unsaturated ketone offers a third choice: LDA at $-78$ °C removes an H at the α' position (the other side of the carbonyl group) to give the cross-conjugated kinetic enolate, whereas under thermodynamic conditions an H at the γ position is removed to give the conjugated dienolate.

## 21.4. Reactivity of Enols and Enolates

### 21.4.1. Ambident Nucleophiles

**Definition 21.4.1** A nucleophile with two different nucleophilic atoms, each of which can bond to an electrophile, is called an **ambident nucleophile**. An enolate can react at carbon or at oxygen; $\ce{CN-}$, $\ce{NO2-}$, $\ce{SCN-}$, and phenoxide ions are also ambident nucleophiles.

```smiles
CC(=O)C(C)C(=O)C>>CC(=O)C(C)(C)C(=O)C
CC(=O)C(C)C(=O)C>>COC(C)=C(C)C(C)=O
```

The equations above show the products of C-methylation and O-methylation of the enolate of 3-methylpentane-2,4-dione. The competition between C and O can be understood with the principle of **hard and soft acids and bases** ([6.5.3](/6.5.3#sec-3.4)): the oxygen end carries the larger charge and is the hard nucleophilic center, whereas the carbon end has the larger orbital coefficient and is the soft nucleophilic center.

| Favors C-reaction | Favors O-reaction |
|---|---|
| Soft **electrophiles**: alkyl halides (especially iodides), carbonyl carbon, $\ce{Br2}$ | Hard electrophiles: $\ce{Me3SiCl}$ (the Si–O bond is very strong), acid anhydrides, dimethyl sulfate, $\ce{Me3O+}$, MeOTf |
| Counterions bound tightly to oxygen ($\ce{Li+}$, $\ce{Mg^2+}$), which shield the oxygen end | Large counterions ($\ce{K+}$), crown ethers, "naked" enolates |
| **Protic solvents** (**hydrogen bonds** shield oxygen), solvents of low polarity (THF) | Strongly coordinating **polar aprotic solvents** (HMPA, DMSO, DMF) |

![Ambident reactivity of the cyclohexanone enolate. Top: the hard oxygen end attacks the silicon of Me₃SiCl (the Si–O bond is very strong) and chloride leaves, giving the silyl enol ether (O-reaction). Bottom: the lone pair on oxygen pushes the π electrons of C=C, and the soft carbon end attacks iodomethane in an SN2 reaction to give 2-methylcyclohexanone (C-reaction)](./plots/ambident-enolate.py)

C-reaction forms the stronger C=O bond, and the product is thermodynamically more stable; O-reaction is often faster (the kinetic product). The same is true of protonation: protonation of an enolate on oxygen is fast and gives the enol, whereas protonation on carbon is slow and gives the stable keto form. C-reaction is usually what is wanted in synthesis; when an oxygen derivative of the enolate is needed (silyl enol ethers, enol triflates), a hard electrophile is used.

### 21.4.2. Comparison of Enols and Enolates

A carbonyl compound with α-H has two nucleophilic forms:

- Enol: formed in small amounts under acid or weak-base catalysis; neutral and of weak **nucleophilicity**, reacting only with very strong electrophiles (halogens, iminium ions, protonated carbonyl groups);
- Enolate: formed by strong bases; negatively charged and many orders of magnitude more nucleophilic than the enol, reacting with a wide range of electrophiles such as alkyl halides, aldehydes, ketones, and esters.

| **Nucleophile** | Electrophile | Product | Reaction | Section |
|---|---|---|---|---|
| Enol (acid-catalyzed) or enolate (base) | $\ce{X2}$ | α-Halo carbonyl compound | α-Halogenation, haloform reaction | 21.5 |
| Enol | Iminium ion $\ce{CH2=NR2+}$ | β-Amino carbonyl compound | Mannich reaction | 21.6 |
| Enolate, **enamine** | Alkyl halide RX | α-Alkyl carbonyl compound | Alkylation | 21.7, 21.8 |
| Enolate | Aldehyde, ketone | β-Hydroxy carbonyl compound | Aldol reaction | [6.5.22](/6.5.22#sec-22.1) |
| Enolate | Ester | **1,3-Dicarbonyl compound** | **Claisen condensation** | [6.5.22](/6.5.22#sec-22.3.1) |
| Stabilized enolate, enamine | α,β-Unsaturated carbonyl compound | 1,5-Dicarbonyl compound | **Michael addition** | [6.5.22](/6.5.22#sec-22.5.1) |

## 21.5. α-Halogenation and the Haloform Reaction

### 21.5.1. Acid-Catalyzed α-Halogenation

Aldehydes and ketones react with $\ce{Cl2}$, $\ce{Br2}$, or $\ce{I2}$ in acid (acetic acid is often the solvent, or HBr is added), and an α-H is replaced by halogen:

```smiles
CC(C)=O.BrBr>>CC(=O)CBr
```

![Mechanism of acid-catalyzed bromination: acetone is first enolized under acid catalysis (the rate-determining step); the lone pair on oxygen of the enol pushes the π electrons of C=C to attack Br₂, giving the protonated bromo ketone (an oxonium ion), which loses a proton to give bromoacetone](./plots/acid-bromination.py)

Lapworth (1904) found that the rate of acid-catalyzed halogenation of acetone, $v = k[\text{ketone}][\ce{H3O+}]$, is independent of the halogen concentration and that chlorination, bromination, and iodination have the same rate constant: the rate-determining step is the enolization, which does not involve the halogen, and the enol, once formed, is captured rapidly by the halogen. This is a classic example of deducing a mechanism from a rate law ([6.5.3](/6.5.3#sec-3.11.1)), and it is consistent with the **racemization** rate experiment of Section 21.2.3.

Halogenation under acidic conditions stops at monohalogenation: the halogen introduced is electron-withdrawing, lowers the basicity of the carbonyl oxygen, and makes the first protonation more difficult, so the next enolization is slower, and one equivalent of halogen reacts preferentially with unhalogenated ketone. An unsymmetrical ketone is halogenated mainly on the more substituted side, because acid-catalyzed enolization is reversible and the more substituted enol is more stable and forms in larger amounts (**thermodynamic control**): bromination of 2-methylcyclohexanone in acetic acid gives mainly 2-bromo-2-methylcyclohexanone.

α-Halo ketones are very useful intermediates:

- The halogen is activated by the carbonyl group, and the **SN2 reaction** is several orders of magnitude faster than for the corresponding alkyl halide ([6.5.8](/6.5.8#sec-8.5.3)).
- With $\ce{Li2CO3}$/LiBr in DMF, or with heating in pyridine, **E2** elimination gives an α,β-unsaturated ketone: one way to introduce a double bond next to a carbonyl group.
- Condensation with a thioamide gives a thiazole (Hantzsch thiazole synthesis), and condensation with a β-keto ester and ammonia (or an amine) gives a pyrrole (Hantzsch pyrrole synthesis), see [6.5.25](/6.5.25#sec-25.7.3).
- With NaOH or an alkoxide, rearrangement through a cyclopropanone intermediate gives a carboxylic acid or ester with one fewer ring carbon (the **Favorskii rearrangement**; mechanism in [6.5.30](/6.5.30#sec-30.8.5)); for example, 2-chlorocyclohexanone gives methyl cyclopentanecarboxylate in sodium methoxide.

### 21.5.2. Halogenation under Basic Conditions and the Haloform Reaction

Under basic conditions halogenation proceeds through the enolate. The halogen introduced is electron-withdrawing and makes the remaining α-H more acidic, so the second and third halogenations are faster than the first and the reaction cannot be stopped at monohalogenation: all the H on the same α carbon are replaced by halogen. The methyl group of a methyl ketone thus becomes $\ce{CX3}$, which is then attacked by hydroxide, and the carbon–carbon bond is cleaved:

![Bromination of acetone under basic conditions. Top: the lone pair on oxygen of the enolate pushes the π electrons of C=C to attack one bromine of Br₂, and bromide leaves, giving bromoacetone. Bottom: bromine is electron-withdrawing, the remaining H on CH₂Br is more acidic than the α-H of acetone, and HO⁻ removes it faster than the first time, so the reaction proceeds all the way to the CBr₃ ketone](./plots/base-bromination.py)

**Definition 21.5.1** The reaction of a methyl ketone $\ce{RCOCH3}$ (or $\ce{RCH(OH)CH3}$, which can be oxidized to a methyl ketone) with excess halogen in basic solution to give a carboxylate $\ce{RCOO-}$ with one carbon fewer and a haloform $\ce{CHX3}$ is called the **haloform reaction**; with iodine it is called the iodoform reaction.

$$
\ce{RCOCH3 + 3X2 + 4OH- -> RCOO- + CHX3 + 3X- + 3H2O}.
$$

![The carbon–carbon bond-cleaving step of the haloform reaction: HO⁻ attacks the carbonyl group of the tribromomethyl ketone to give a tetrahedral intermediate; the lone pair on the oxyanion pushes back to re-form C=O and expels CBr₃⁻, which is stabilized by the three bromines; it takes a proton from the carboxylic acid to give bromoform and the carboxylate](./plots/haloform.py)

The trihalomethyl anion can leave as a **leaving group** because the **inductive effect** of the three halogens (and **hyperconjugation** with C–X σ*) stabilizes the negative charge on carbon; this step is essentially a **nucleophilic acyl substitution** (addition–elimination, Definition 19.2.1). Uses of the haloform reaction:

- Identification: iodoform $\ce{CHI3}$ is a yellow precipitate with a characteristic odor (mp 119 °C). The test is positive for the $\ce{CH3CO-}$ unit (methyl ketones, acetaldehyde) and the $\ce{CH3CH(OH)-}$ unit (ethanol, isopropyl alcohol, and other 2-ols, which are first oxidized by $\ce{I2}$/NaOH to methyl ketones); methanol, other primary alcohols, and non-methyl ketones give a negative result.
- Synthesis: converting a methyl ketone into a carboxylic acid with one carbon fewer, often with sodium hypochlorite (bleach) as the halogen source: acetophenone gives benzoic acid, and pinacolone (3,3-dimethylbutan-2-one) gives 2,2-dimethylpropanoic acid. C=C bonds in the molecule are generally unaffected.

### 21.5.3. α-Halogenation of Carboxylic Acids and Their Derivatives

The enol content of a carboxylic acid itself is too low, and direct halogenation is slow; acyl halides enolize much more easily. The Hell–Volhard–Zelinsky (HVZ) reaction uses a catalytic amount of $\ce{PBr3}$ to convert part of the carboxylic acid to the acyl bromide; the acyl bromide enolizes and is brominated, and exchange with carboxylic acid gives the α-bromo acid and regenerates the acyl bromide (mechanism in [6.5.18](/6.5.18#sec-18.5)). For α-halogenation of esters and amides, the enolate is generally made first with LDA and then trapped with a "positive halogen" reagent such as NBS or $\ce{CBr4}$. **1,3-Dicarbonyl compounds** have a high enol content and react directly with $\ce{Br2}$ or NBS, halogenating at the carbon between the two carbonyl groups.

## 21.6. The Mannich Reaction

### 21.6.1. Reaction and Mechanism

**Definition 21.6.1** The condensation of an enolizable aldehyde or ketone, formaldehyde (or another reactive non-enolizable aldehyde), and a secondary amine (or a primary amine or an ammonium salt), which introduces an aminomethyl group at the α position of the carbonyl group and gives a β-amino carbonyl compound, is called the **Mannich reaction** (Mannich 1912); the product is called a **Mannich base**.

```smiles
CC(=O)c1ccccc1.C=O.CNC>>CN(C)CCC(=O)c1ccccc1
```

(Acetophenone, formaldehyde, and dimethylamine hydrochloride heated at reflux in ethanol give 3-(dimethylamino)-1-phenylpropan-1-one hydrochloride.) The reaction is carried out under weakly acidic conditions and comprises three steps: condensation of the amine with formaldehyde with loss of water to give an iminium ion ([6.5.16](/6.5.16#sec-16.9.3)); acid-catalyzed enolization of the carbonyl compound; and attack of the enol on the carbon of the iminium ion, followed by loss of a proton.

![Formation of the electrophile in the Mannich reaction. Top: the lone pair on the nitrogen of dimethylamine adds to the carbonyl carbon of formaldehyde, and the π electrons of C=O move onto oxygen; N-to-O proton transfer gives the hemiaminal. Bottom: in weak acid the OH is protonated, and the lone pair on nitrogen forms the C=N double bond and expels water, giving the methylenedimethylammonium ion (an iminium ion)](./plots/iminium-formation.py)

![The key step of the Mannich reaction: the iminium ion formed from formaldehyde and dimethylamine (methylenedimethylammonium) is a strong electrophile; the enol of acetone attacks its carbon, with the lone pair on oxygen pushing the π electrons of C=C, to give the protonated β-amino ketone, which loses a proton to give the Mannich base](./plots/mannich.py)

The essence of the Mannich reaction is the addition of an enol (**nucleophile**) to an iminium ion (**electrophile**), just as the aldol reaction is the addition of an enolate to a carbonyl group ([6.5.22](/6.5.22#sec-22.1)). An iminium ion is more electrophilic than an aldehyde, so the weakly nucleophilic enol can react with it, whereas the self-aldol reaction of the carbonyl compound is slow under the same weakly acidic conditions; hence the three components can be combined in one pot. One can also prepare an iminium salt in advance, such as Eschenmoser's salt $\ce{CH2=NMe2+ I-}$, and treat it with a silyl enol ether or an enolate.

Uses of Mannich bases: quaternization with MeI followed by base brings about **Hofmann elimination** (Definition 23.8.1) to give an α-methylene ketone ($\ce{RCOC(=CH2)R'}$) or a vinyl ketone. Vinyl ketones polymerize readily and are inconvenient to store, so a standard trick in the **Robinson annulation** ([6.5.22](/6.5.22#sec-22.5.2)) is to add the Mannich base (or its **quaternary ammonium salt**) directly to the reaction mixture and let it eliminate in situ.

### 21.6.2. The Synthesis of Tropinone and Mannich Reactions in Biosynthesis

Tropinone is the parent skeleton of the tropane **alkaloids** (atropine, scopolamine, cocaine, [6.5.23](/6.5.23#sec-23.1.3)). Willstätter (1901) synthesized tropinone from cycloheptanone in many steps with an overall yield of less than 1 %. Robinson (1917) imagined that tropinone might be formed in plants from simple precursors by a Mannich reaction, so he mixed succindialdehyde, methylamine, and acetone (better, calcium acetonedicarboxylate) in water and obtained tropinone in one step:

```smiles
O=CCCC=O.CN.O=C(O)CC(=O)CC(=O)O>>CN1C2CCC1CC(=O)C2
```

The mechanism consists of two Mannich reactions. Methylamine condenses with one aldehyde group of succindialdehyde to give an iminium ion, which is attacked by the enol of acetonedicarboxylic acid; the nitrogen then condenses with the other aldehyde group and closes the ring to give a second iminium ion, which is attacked by the other enol in the same molecule to form the bicyclic skeleton; finally the two β-keto acid groups undergo thermal **decarboxylation** ([6.5.18](/6.5.18#sec-18.4.1)). The two carboxyl groups of acetonedicarboxylic acid greatly increase the acidity of the α-H so that the enol forms more easily, and they can be removed after the reaction. Robinson's original yield was not high (about 17 % with acetone, about 40 % with the acetonedicarboxylate); Schöpf (1935) ran the reaction in a buffer at pH about 7 and raised the yield to about 90 %. This is the first classic example of "biomimetic synthesis": under nearly physiological conditions, a complex skeleton is built in one step from simple precursors that biosynthesis might use. The actual biosynthetic pathway was later shown to be different (a type III polyketide synthase makes a 3-oxoglutarate unit from two molecules of malonyl-CoA, which undergoes a Mannich-type condensation with the N-methylpyrrolinium ion, and a cytochrome P450 enzyme then oxidizes the ring closed), but Mannich-type C–C bond formation remains a key step in it.

![The second (intramolecular) Mannich reaction in Robinson's tropinone synthesis: after the first Mannich reaction and cyclization of nitrogen onto the second aldehyde group, the molecule contains an N-methylpyrrolinium ion and the enol of a β-keto acid; the lone pair on the enol oxygen pushes the π electrons of C=C to attack the iminium carbon, and the π electrons of C=N move onto nitrogen, forming the six-membered ring of the tropane skeleton; loss of a proton gives tropinone-2,4-dicarboxylic acid, and on heating the two β-keto acid groups decarboxylate to give tropinone](./plots/tropinone-mannich.py)

Mannich-type reactions are extremely common in the biosynthesis of alkaloids. When an amine with an ethylamine side chain on an aromatic ring condenses with an aldehyde to form an iminium ion, the electron-rich aromatic ring (as an analogue of the enol) attacks the iminium carbon intramolecularly to form a tetrahydroisoquinoline or tetrahydro-β-carboline ring; this is the Pictet–Spengler reaction (**electrophilic aromatic substitution**, [6.5.14](/6.5.14#sec-14.1)). Dopamine and acetaldehyde give salsolinol (1-methyl-6,7-dihydroxy-1,2,3,4-tetrahydroisoquinoline) in nearly neutral aqueous solution; in plants, norcoclaurine synthase catalyzes the same type of reaction between dopamine and 4-hydroxyphenylacetaldehyde to give the common precursor of the benzylisoquinoline alkaloids such as morphine. The asymmetric Mannich reaction under **organocatalysis** (proline catalysis, List 2000, with the same mechanism as the proline-catalyzed aldol reaction of [6.5.22](/6.5.22#sec-22.6.3)) gives β-amino ketones and β-amino acid derivatives with high enantioselectivity.

![The Pictet–Spengler cyclization of dopamine with acetaldehyde: the iminium ion formed from the amine and the aldehyde is attacked by the electron-rich catechol ring, at the position ortho to the side chain and para to one hydroxyl group; the π electrons of the ring form the new C–C bond and the π electrons of C=N move onto nitrogen. The aryl cation formed (its positive charge delocalized onto the para oxygen) loses a proton and restores aromaticity, giving salsolinol (a 1,2,3,4-tetrahydroisoquinoline)](./plots/pictet-spengler.py)

## 21.7. Alkylation of Enolates

### 21.7.1. Conditions and Limitations

An enolate reacts with an alkyl halide in an **SN2 reaction** to introduce an alkyl group at the α position of the carbonyl group:

![Alkylation of an enolate: LDA at −78 °C removes the α-H of cyclohexanone quantitatively to give the lithium enolate; the carbon end (the π bond) of the enolate attacks the carbon of iodomethane from the back side, and iodide leaves, giving 2-methylcyclohexanone](./plots/enolate-alkylation.py)

For the reaction to proceed cleanly the following conditions must be met, each corresponding to a side reaction:

| Requirement | Reason (the side reaction otherwise) |
|---|---|
| Use a strong base such as LDA and form the enolate quantitatively before adding the alkyl halide | With undeprotonated ketone present, the enolate undergoes an aldol reaction with the ketone, or exchanges protons between the alkylated product and the enolate, giving dialkylation products |
| Use methyl or primary alkyl halides, or allylic and benzylic halides and α-halo esters | Enolates are strong bases; secondary and tertiary alkyl halides mainly undergo **E2** elimination ([6.5.9](/6.5.9#sec-9.6.1)), and vinyl and aryl halides do not undergo SN2 |
| Aldehydes are generally not alkylated directly | The carbonyl group of an aldehyde is so reactive that the aldol reaction with unreacted aldehyde occurs as soon as the enolate forms; α-alkylation of aldehydes is carried out with **enamines** instead (Section 21.8) |
| No other, more acidic hydrogens in the molecule | For example, a primary amide $\ce{CH3CONH2}$ is deprotonated first on N (the N–H has $\mathrm{p}K_{\mathrm{a}}$ 25.5 in DMSO), giving the N-anion |

The enolates of esters, lactones, nitriles, and N,N-disubstituted amides (such as N-benzylpiperidin-2-one) can also be alkylated, and because there is no competition from the aldol reaction they are often better than aldehydes and ketones. A symmetrical ketone with only one H on each α carbon (such as 2,6-dimethylcyclohexanone or 2,4-dimethylpentan-3-one) has no problem of **regioselectivity**, and after monoalkylation to give a quaternary carbon it is less likely to be alkylated again. A more common approach is to place an extra removable activating group on the carbon to be alkylated: the **acetoacetic ester synthesis** and the **malonic ester synthesis** ([6.5.22](/6.5.22#sec-22.8), [6.5.22](/6.5.22#sec-22.9)).

### 21.7.2. Regioselectivity and Stereochemistry

The position of alkylation of an unsymmetrical ketone is decided by the enolate (Section 21.3.2):

```smiles
CC1CCCCC1=O>>CC1CCCC(C)C1=O
CC1CCCCC1=O>>CC1(C)CCCCC1=O
```

The upper line gives the main product (2,6-dimethylcyclohexanone) of forming the kinetic enolate with LDA at $-78$ °C and then adding MeI, and the lower line the main product under thermodynamic conditions (2,2-dimethylcyclohexanone). The selectivity of alkylation under thermodynamic conditions is often not high, because equilibration and alkylation proceed at the same time; it is more reliable to prepare a regiochemically pure silyl enol ether first, regenerate the specified lithium enolate with MeLi, and then alkylate.

The alkylation of a cyclohexanone enolate has a stereoelectronic requirement: the **electrophile** attacks perpendicular to the plane of the enolate and prefers the face from which the ring goes directly to a **chair conformation** ("axial attack"), so the new C–C bond is initially an **axial bond**; attack from the other face goes through a twist-boat **transition state** of higher energy. In a ring of fixed conformation, therefore, the kinetic product is often mainly the isomer with the new group axial; if the α-H of the product can enolize under the reaction conditions, it gradually epimerizes to the more stable isomer with the new group equatorial.

### 21.7.3. Myers Asymmetric Alkylation

Alkylation at the α carbon of an enolate usually creates a new **stereocenter**, but the two faces of a planar enolate are the same (**enantiotopic**), so ordinary alkylation gives only the **racemate**. A general way to control the configuration of the new stereocenter is to attach a chiral group to the molecule temporarily:

**Definition 21.7.1** A chiral group that is attached covalently and temporarily to a substrate in order to control the stereochemistry of a reaction, and that can be removed and recovered afterwards, is called a **chiral auxiliary**.

Myers (1994) used the inexpensive natural product pseudoephedrine as the chiral auxiliary: a carboxylic acid forms a tertiary amide with pseudoephedrine, at least 2 equiv of LDA (removing both the hydroxyl H and the α-H) in the presence of LiCl generates the (Z)-enolate, and an alkyl halide is then added:

```smiles
CCC(=O)N(C)[C@@H](C)[C@@H](O)c1ccccc1>>CCCCC(C)C(=O)N(C)[C@@H](C)[C@@H](O)c1ccccc1
CCCCC(C)C(=O)N(C)[C@@H](C)[C@@H](O)c1ccccc1>>CCCCC(C)C(=O)O
```

(First line: the N-propionamide of (1S,2S)-pseudoephedrine reacts with $n$-BuI under LDA/LiCl in THF to give the α-butylation product with a **diastereomeric excess** of more than 99 %; the configuration of the new stereocenter is determined by the auxiliary and is not shown in the formula. Second line: hydrolysis of the product in sulfuric acid–dioxane gives 2-methylhexanoic acid with an **enantiomeric excess** of 97 %.) One face of the enolate is shielded by the lithium alkoxide of the pseudoephedrine and the solvent coordinated to it, as well as by LiCl, and the electrophile attacks from the other face; the **diastereomeric excess** is usually above 90 %, and the detailed model for the selectivity is still discussed. LiCl breaks up the aggregates of the lithium enolate so that alkylation proceeds rapidly at low temperature, and it suppresses O-alkylation. The product amide can be hydrolyzed to the carboxylic acid, reduced to the primary alcohol or the aldehyde, or treated with an **organolithium reagent** to give a ketone, and the pseudoephedrine is recovered. Because pseudoephedrine is a controlled precursor chemical, Myers (2012) later developed the pseudoephenamine auxiliary, which performs equally well. The oxazolidinone auxiliaries of Evans are another widely used class of chiral auxiliaries and are more important in asymmetric aldol reactions. The chiral auxiliary method requires two steps, attachment and removal; controlling the stereochemistry directly with a chiral catalyst (**asymmetric catalysis**) is the more economical direction ([6.5.22](/6.5.22#sec-22.6)).

## 21.8. Alkylation and Acylation of Enamines

### 21.8.1. The Stork Enamine Reaction

The **enamine** formed by condensation of an aldehyde or ketone with a secondary amine ([6.5.16](/6.5.16#sec-16.9.3)) is the nitrogen analogue of an enol. The lone pair on nitrogen is conjugated with the C=C bond and puts partial negative charge on the β carbon; the **nucleophilicity** of an enamine lies between that of an enol and an enolate, yet it is neutral and reacts with **electrophiles** without the need for a strong base; the iminium ion formed after the reaction is hydrolyzed in water to give back the carbonyl compound and the secondary amine.

**Definition 21.8.1** The method in which an aldehyde or ketone is first converted with a secondary amine (often pyrrolidine, piperidine, or morpholine) into an enamine, the β carbon of the enamine is allowed to react with an alkyl halide, acyl halide, or α,β-unsaturated carbonyl compound, and the product is hydrolyzed to give an α-substituted carbonyl compound, is called the **Stork enamine reaction** (Stork 1954, 1963).

![The Stork enamine reaction: in the pyrrolidine enamine of cyclohexanone, the lone pair on nitrogen pushes the π electrons of C=C, and the β carbon attacks the carbon of allyl bromide, with bromide leaving, to give an iminium ion; the iminium ion is hydrolyzed in dilute acid to give 2-allylcyclohexanone and release pyrrolidine](./plots/stork-enamine.py)

- Alkylation: reactive alkyl halides (allyl halides, benzyl halides, α-halo ketones, α-halo esters, iodomethane) alkylate well on carbon; ordinary primary alkyl halides are alkylated to a considerable extent on nitrogen, giving **quaternary ammonium salts** that cannot be hydrolyzed to the desired product.
- Acylation: reaction with an acyl chloride, followed by hydrolysis, gives a 1,3-diketone; for example, cyclohexanone gives 2-acetylcyclohexanone through its pyrrolidine enamine and acetyl chloride. The HCl formed is taken up by a second molecule of enamine or by added triethylamine.
- **Conjugate addition**: enamines are excellent Michael donors and react with methyl vinyl ketone, acrylonitrile, and acrylates to give 1,5-dicarbonyl compounds, see [6.5.22](/6.5.22#sec-22.5).

![Acylation of an enamine: in the pyrrolidine enamine of cyclohexanone, the lone pair on nitrogen pushes the π electrons of C=C to attack the carbonyl carbon of acetyl chloride, and the π electrons of C=O move onto oxygen; the tetrahedral intermediate collapses, re-forming C=O and expelling chloride, to give the acyliminium ion; hydrolysis in dilute acid gives 2-acetylcyclohexanone and pyrrolidine](./plots/enamine-acylation.py)

Compared with enolates, the enamine method has several advantages:

| | Enolate (LDA) | Enamine |
|---|---|---|
| Polyalkylation | The product exchanges protons with the enolate, so dialkylation is possible | The iminium ion formed is no longer nucleophilic, so alkylation occurs only once |
| Aldehydes | Undergo self-aldol reaction and cannot be alkylated | Enamines of aldehydes can be alkylated |
| Conditions | Strong base, low temperature, anhydrous | Neutral; enamines can be isolated and distilled |
| **Regioselectivity** with unsymmetrical ketones | Depends on kinetic or thermodynamic conditions | Reaction mainly at the less substituted α carbon |
| Suitable alkyl halides | Methyl and primary alkyl halides | Only reactive alkyl halides |

An unsymmetrical ketone mainly gives the less substituted enamine: in the pyrrolidine enamine of 2-methylcyclohexanone, if the double bond were on the more substituted side, the methyl group and the pyrrolidine ring (which lies in the same plane because N is conjugated with C=C) would suffer severe A(1,3) strain, so the double bond lies toward C6, and alkylation takes place at the less hindered α carbon. Enamines are also key intermediates in **organocatalysis** (the 2021 Nobel Prize in Chemistry for List and MacMillan) and in class I aldolases, where a secondary amine (proline, or a lysine residue of the enzyme) is used as a catalyst in a catalytic cycle ([6.5.22](/6.5.22#sec-22.10.1), [6.5.22](/6.5.22#sec-22.6.3)).

### 21.8.2. Alkylation through Enols and Carbocations

A tertiary alkyl group cannot be introduced by SN2 (Section 21.7.1), but the roles can be reversed, with the enol (or silyl enol ether) acting as a **nucleophile** that captures a **carbocation**: silyl enol ethers react with tertiary alkyl halides under $\ce{TiCl4}$ or $\ce{ZnCl2}$ in an **SN1**-type α-tert-alkylation (Reetz, 1978), and **1,3-dicarbonyl compounds** react directly with benzylic and allylic alcohols under **Lewis acid** or Brønsted acid catalysis, with water as the only by-product. An enol is a weak nucleophile and reacts only with strong electrophiles such as stabilized carbocations (tertiary, allylic, and at the **benzylic position**), in agreement with the pattern of Section 21.4.2.

![SN1-type tertiary alkylation of a silyl enol ether: TiCl₄ removes chloride from tert-butyl chloride to give the tert-butyl cation; the lone pair on oxygen of the silyl enol ether pushes the π electrons of C=C to attack the carbocation, forming a C–C bond and a silyloxonium ion; chloride removes the trimethylsilyl group from oxygen to give 2-tert-butylcyclohexanone](./plots/silyl-enol-sn1.py)

## 21.9. Research Frontier: Catalytic Functionalization at the α Position of Carbonyl Compounds

Classical α-functionalization requires stoichiometric strong bases and substrates activated in advance. The advances of the past two decades use catalysts to introduce a variety of groups directly at the α position: Pd- and **chiral** phosphine-catalyzed α-arylation of ketones, esters, and amides (Buchwald, Hartwig; **reductive elimination** from an enolate and an arylpalladium species, [6.5.29](/6.5.29#sec-29.4.7)), which introduces aryl groups that SN2 cannot; asymmetric α-amination, α-fluorination, and α-chlorination by **organocatalysis** (through chiral **enamine** intermediates); and α-alkylation of aldehydes combining enamine catalysis with **photoredox catalysis** (Nicewicz and MacMillan, 2008): in the photocatalytic cycle a Ru(I) species reduces an α-bromo carbonyl compound to an electron-poor **radical**, which adds to the C=C of a chiral enamine; the α-amino radical formed is oxidized to an iminium ion and hydrolyzed, which closes the catalytic cycle ([6.5.31](/6.5.31#sec-31.5)).

![The radical step in enamine–photoredox α-alkylation of aldehydes: the electron-poor diethyl malonate radical adds to the C=C of the electron-rich chiral enamine, one electron of the π bond pairs with the radical to form the new C–C bond, and the other electron remains on the carbon next to nitrogen; the α-amino radical is oxidized by one electron to the iminium ion, and hydrolysis gives the alkylated aldehyde and regenerates the amine catalyst (R₂N stands for the imidazolidinone catalyst)](./plots/enamine-radical.py)

## Summary

- The acidity of α-H comes from delocalization in the enolate (negative charge on oxygen): aldehyde 16.7 < ketone 19.3 < ester about 25 ($\mathrm{p}K_{\mathrm{a}}$ in water), and **1,3-dicarbonyl compounds** 9–13. The base is chosen by $\lg K = \mathrm{p}K_{\mathrm{a}}(\ce{BH}) - \mathrm{p}K_{\mathrm{a}}(\text{carbonyl compound})$: alkoxides give only a small amount of enolate, LDA gives it quantitatively.
- Keto–enol tautomerism (Definition 21.2.1): $K_{\mathrm{E}}$ of simple aldehydes and ketones is $10^{-6}$–$10^{-9}$ (acetone $4.7\times10^{-9}$), and $\mathrm{p}K_{\mathrm{a}}(\text{keto}) = \mathrm{p}K_{\mathrm{E}} + \mathrm{p}K_{\mathrm{a}}(\text{enol})$; acid and base both catalyze it, with the consequences of D exchange of α-H and **racemization** of α stereocenters. Conjugation, intramolecular **hydrogen bonding**, electron-withdrawing groups, **aromaticity**, and nonpolar solvents increase the enol content.
- Enolates (Definition 21.3.1): LDA at $-78$ °C gives the less substituted kinetic enolate, and reversible conditions give the more substituted thermodynamic enolate (Definition 21.3.2); silyl enol ethers can be isolated and used to regenerate a specified enolate.
- Ambident nucleophiles (Definition 21.4.1): soft **electrophiles**, $\ce{Li+}$, and solvents of low polarity favor C-reaction; hard electrophiles ($\ce{Me3SiCl}$), large counterions, and HMPA favor O-reaction. An enol reacts only with strong electrophiles, an enolate with a wide range of electrophiles.

| Reaction | Nucleophilic form | Key points |
|---|---|---|
| Acid-catalyzed α-halogenation | Enol | Rate independent of $[\ce{X2}]$ (enolization is rate-determining); stops at monohalogenation; on the more substituted side |
| Haloform reaction (Definition 21.5.1) | Enolate | After polyhalogenation $\ce{CX3-}$ acts as the **leaving group**; iodoform identifies $\ce{CH3CO-}$ and $\ce{CH3CH(OH)-}$; methyl ketone → acid with one carbon fewer |
| Mannich reaction (Definition 21.6.1) | Enol + iminium ion | β-Amino ketones; Robinson–Schöpf tropinone synthesis; Pictet–Spengler |
| Alkylation | Enolate (LDA) | **SN2**: methyl and primary alkyl halides; **regioselectivity** set by the enolate; chiral auxiliary (Definition 21.7.1) controls stereochemistry (Myers) |
| Stork enamine reaction (Definition 21.8.1) | **Enamine** | Reactive alkyl halides, acyl chlorides, Michael acceptors; monoalkylation, also for aldehydes, on the less substituted side |

## Questions

1. Using the method of Section 21.1.3, estimate the equilibrium constants for the following deprotonations and decide whether the **carbanion** forms quantitatively: (a) ethyl acetoacetate + sodium ethoxide (in ethanol); (b) ethyl acetate + sodium ethoxide; (c) acetone + LDA; (d) acetophenone + potassium *tert*-butoxide (in *tert*-butyl alcohol).

   **Answer** (a) $\lg K = 15.9 - 10.7 = 5.2$, $K \approx 10^5$: quantitative, so the **acetoacetic ester synthesis** needs only sodium ethoxide. (b) $\lg K \approx 15.9 - 25 = -9$: at equilibrium only about $10^{-9}$ of the ester is present as the enolate, but this is enough for the **Claisen condensation** to proceed (deprotonation of the product drives the equilibrium, [6.5.22](/6.5.22#sec-22.3.1)). (c) $\lg K \approx 36 - 19.3 \approx 17$: quantitative and irreversible. (d) The $\mathrm{p}K_{\mathrm{a}}$ of *tert*-butyl alcohol is about 18 (in water), close to the 18.3 of acetophenone, so $K \approx 0.5$ and only part of the ketone is converted to the enolate; ketone and enolate are both present, which is a thermodynamic condition.

2. (S)-3-Methylpentan-2-one is dissolved in $\ce{D2O}$–dioxane containing a little NaOD and left to stand. (a) Which hydrogens are exchanged for D? What is the molecular formula of the final product? (b) How does the optical rotation of the solution change? (c) If (S)-3-methyl-3-phenylpentan-2-one is used instead, does the optical rotation change?

   **Answer** (a) The enolizable α-H are the 3 H on C1 and the 1 H on C3, 4 in all, and the final product is $\ce{CD3COCD(CH3)CH2CH3}$, that is, $\ce{C6H8D4O}$. (b) The H on C3 is exchanged through the planar enolate; D adds from either face with equal probability, the configuration at C3 is gradually lost, and the optical rotation falls to zero (**racemization**); the rate of racemization equals the rate of exchange of the C3–H. (c) C3 bears no H and cannot be enolized toward C3 (exchange at C1 still occurs); the **stereocenter** is unaffected and the optical rotation does not change.

3. Explain: (a) cyclohexane-1,3-dione exists mainly as the enol in aqueous solution even though its enol cannot form an intramolecular **hydrogen bond**; (b) the enol content of ethyl acetoacetate in water (about 0.4 %) is much lower than in cyclohexane (close to half); (c) phenol exists as the enol, and 1-naphthol and 2-naphthol are also almost entirely enol, but 9-anthrol coexists in solution with its keto form 9(10*H*)-anthracenone, with the latter predominating.

   **Answer** (a) The orientation of the two carbonyl groups in the ring is fixed, and the OH of the enol and the other carbonyl oxygen point in different directions and cannot form an intramolecular hydrogen bond; but the conjugated enol–ketone system (a vinylogous carboxylic acid, $\mathrm{p}K_{\mathrm{a}}$ about 5) is itself very stable, in water the OH hydrogen-bonds to the solvent, so the enol still predominates, and in the solid the molecules are linked into chains by intermolecular hydrogen bonds. (b) Water is a strong hydrogen-bond donor and acceptor, competes with the intramolecular hydrogen bond of the enol, and preferentially solvates the keto form, which has the larger dipole moment; cyclohexane cannot form hydrogen bonds, and the intramolecular hydrogen bond makes the enol form less polar and more stable in nonpolar solvents. (c) The driving force of enolization is the gain or loss of aromatic stabilization energy. The keto form of phenol loses the **aromaticity** of the whole benzene ring; the keto forms of the naphthols lose the aromaticity of one benzene ring, still at a large cost. In anthracenone, once C9 becomes $\mathrm{sp^3}$, two complete benzene rings remain, and the aromatic stabilization of the middle ring of anthracene itself is much smaller than that of two separate benzene rings (the resonance energy of anthracene is less than the sum for three benzene rings), so less aromaticity is lost on going to the keto form, and with the C=O bond being stronger than C=C, the keto form predominates.

4. 2-Methylcyclohexanone is treated under each of the following conditions and then $\ce{CH3I}$ is added. Write the main product and explain: (a) LDA, THF, $-78$ °C; (b) NaH, THF, room temperature, slight excess of ketone; (c) first pyrrolidine and TsOH in toluene with removal of water, then reaction with allyl bromide, and finally hydrolysis with dilute acid (here the **electrophile** is allyl bromide).

   **Answer** (a) 2,6-Dimethylcyclohexanone: LDA at low temperature removes the less hindered and more numerous C6–H irreversibly, giving the kinetic enolate. (b) Mainly 2,2-dimethylcyclohexanone (with some 2,6-dimethyl and polymethylated products): NaH forms the enolate slowly, the excess ketone acts as a proton source that equilibrates the two enolates, and the more stable tetrasubstituted enolate predominates; because equilibration and alkylation proceed together, the selectivity is not high. (c) 2-Allyl-6-methylcyclohexanone: the more substituted **enamine** suffers severe A(1,3) strain, so the enamine with the double bond at C1=C6 is formed and the allyl group adds to C6; the iminium ion formed does not react further, so only monoalkylation occurs, and hydrolysis gives the ketone.

5. Write the steps by which acetone gives iodoform in $\ce{I2}$/NaOH. Why does the monoiodo derivative of acetone undergo further iodination faster than acetone itself in NaOH, but stop at monoiodination in acetic acid? Which of ethanol, isopropyl alcohol, propan-1-ol, pentan-3-one, and acetophenone give a positive iodoform test?

   **Answer** The steps: $\ce{HO-}$ removes an α-H to give the enolate (rate-determining); the carbon of the enolate attacks $\ce{I2}$ to give iodoacetone; the same sequence is repeated twice on the same methyl group to give 1,1,1-triiodoacetone; $\ce{HO-}$ adds to the carbonyl group, and the **tetrahedral intermediate** expels $\ce{CI3-}$; $\ce{CI3-}$ takes a proton from acetic acid to give $\ce{CHI3}$ and acetate. Under basic conditions the rate-determining step is removal of the α-H by base, and the electron-withdrawing effect of iodine makes the remaining α-H on the same carbon more acidic and the carbanion more stable, so each iodination is faster than the one before. Under acidic conditions the rate-determining step is enolization, which requires protonation of the carbonyl oxygen first, and the electron-withdrawing effect of iodine reduces the basicity of the carbonyl oxygen, so the second enolization is actually slower. Positive: ethanol (oxidized to acetaldehyde), isopropyl alcohol (oxidized to acetone), acetophenone; negative: propan-1-ol (oxidized to propanal, which has no $\ce{CH3CO-}$ unit) and pentan-3-one (not a methyl ketone).

6. Prepare 1-phenylprop-2-en-1-one (phenyl vinyl ketone) from acetophenone, formaldehyde, and dimethylamine hydrochloride, writing the steps and the key points of each mechanism. Why is the isolated vinyl ketone often not used directly in synthesis?

   **Answer** (1) Mannich reaction: acetophenone, paraformaldehyde, and dimethylamine hydrochloride are heated at reflux in ethanol (with a little HCl); formaldehyde and dimethylamine form an iminium ion, which is attacked by the enol of acetophenone to give 3-(dimethylamino)-1-phenylpropan-1-one hydrochloride. (2) The amine is quaternized with $\ce{CH3I}$. (3) Base (for example aqueous $\ce{NaHCO3}$, or simply heating) brings about elimination: the carbonyl group makes the α-H acidic, base removes it to give the enolate, which expels trimethylamine (**E1cB**) to give the conjugated phenyl vinyl ketone. A vinyl ketone is a very strong Michael acceptor and polymerizes easily, so it is difficult to store and purify; when the stable Mannich base or its **quaternary ammonium salt** is added to a reaction such as the **Robinson annulation** and allowed to eliminate gradually in situ under basic conditions, the instantaneous concentration of vinyl ketone is low and side reactions such as polymerization are suppressed.

7. An α-benzyl group is introduced into cyclohexanone by (a) LDA/THF, $-78$ °C, then benzyl bromide; (b) morpholine/TsOH to form the enamine, reaction with benzyl bromide, and hydrolysis. If an isopropyl group is to be introduced at the α position, are the two methods feasible? Propose a feasible scheme.

   **Answer** Both (a) and (b) are feasible and give 2-benzylcyclohexanone; in (a), if the addition is done improperly, proton exchange between the product and the enolate gives a little 2,6-dibenzyl product, whereas (b) gives only monoalkylation. For introduction of an isopropyl group, 2-bromopropane is a secondary alkyl halide that mainly undergoes **E2** elimination with enolates and mainly alkylates on nitrogen, or does not react, with enamines, so neither method is good. One feasible scheme: a directed crossed aldol condensation with acetone (the LDA enolate of cyclohexanone adds to acetone, followed by dehydration) gives 2-isopropylidenecyclohexanone, and selective hydrogenation of the C=C (Pd/C, $\ce{H2}$) gives 2-isopropylcyclohexanone. Another scheme uses the enolate of 2-ethoxycarbonylcyclohexanone (the crossed Claisen condensation product of cyclohexanone and diethyl carbonate, [6.5.22](/6.5.22#sec-22.3.3)) with 2-iodopropane in DMSO: the stabilized 1,3-dicarbonyl anion is weakly basic, and its **SN2** reaction with a secondary alkyl halide outcompetes E2; hydrolysis and **decarboxylation** then remove the ester group.

8. Which of the following methods gives optically active 2-methylhexanoic acid? Explain: (a) double deprotonation of hexanoic acid with LDA, then reaction with $\ce{CH3I}$; (b) the amide of hexanoic acid with pseudoephedrine, treated with LDA/LiCl, then reaction with $\ce{CH3I}$ and hydrolysis; (c) the **racemate** of 2-methylhexanoic acid, salt formation with (R)-1-phenylethylamine and recrystallization.

   **Answer** (b) and (c). (a) The dianion formed is planar, its two faces are **enantiotopic**, and under achiral conditions the methyl group attacks from either face with equal probability, giving the racemate. (b) Pseudoephedrine is a chiral auxiliary that makes the two faces of the enolate **diastereotopic**; one face is shielded, methylation proceeds with high diastereoselectivity, and removal of the auxiliary by hydrolysis gives 2-methylhexanoic acid with one **enantiomer** predominating (the alternative combination for the Myers alkylation, the propionamide with $n$-BuI, gives the opposite configuration). (c) is a classical **resolution** ([6.5.5](/6.5.5#sec-5.7.2)): the two diastereomeric salts have different solubilities, and after recrystallization acidification gives a single enantiomer, but at most half of the starting material can be obtained.
