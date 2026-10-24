---
title: Carboxylic Acids
description: Structure, nomenclature, physical properties, and spectra of carboxylic acids; acidity and its structural factors (resonance, inductive effect, substituent effects in benzoic acids and the Hammett equation, the ortho effect, the field effect, physiological pH); salt formation, soaps, and resolution; reduction with LiAlH₄ and borane; decarboxylation (the cyclic transition state of β-keto acids, Kolbe electrolysis, the Hunsdiecker reaction, biological decarboxylation, and photoredox decarboxylative coupling); the HVZ reaction; reactions with organometallic reagents; unsaturated, halo, hydroxy, phenolic, and oxo acids.
source_hash: 0c0a6ac8c990
---

A carboxylic acid contains the carboxyl group $\ce{-COOH}$, in which carbon is in the highest oxidation state other than $\ce{CO2}$ (+3, [6.5.1](/6.5.1#sec-1.3.2)). It is the most common acid in organic chemistry and the parent of the large family of "carboxylic acid derivatives": esters, amides, acyl halides, anhydrides, and nitriles. This chapter deals with the carboxylic acids themselves. We first look at structure, nomenclature, physical properties, and spectroscopic features; then use the $\mathrm{p}K_{\mathrm{a}}$ scale of [6.5.3](/6.5.3#sec-3.1.4) and the **Hammett equation** to discuss the acidity of carboxylic acids quantitatively; then turn to reduction of the carboxyl group, decarboxylation, α-halogenation, and reactions with organometallic reagents; and finally introduce several classes of "special carboxylic acids" that carry another functional group: unsaturated, halo, hydroxy, phenolic, and oxo acids.

The other important class of reactions of the carboxyl group is replacement of the hydroxy group to give the various carboxylic acid derivatives (**nucleophilic acyl substitution**); this, together with the interconversion of the derivatives, is treated in [6.5.19](/6.5.19). Amides, nitriles, carbonic acid derivatives, and synthesis design are in [6.5.20](/6.5.20), and the enol chemistry of the α carbon of carboxylic acids is in [6.5.21](/6.5.21) and [6.5.22](/6.5.22). The tools used in this chapter are resonance theory ([6.5.1](/6.5.1#sec-1.6)); the **inductive effect**, the **conjugation effect**, and the **field effect** ([6.5.2](/6.5.2#sec-2.3), [6.5.2](/6.5.2#sec-2.5), [6.5.2](/6.5.2#sec-2.7)); the unified $\mathrm{p}K_{\mathrm{a}}$ table and the Hammett equation ([6.5.3](/6.5.3#sec-3.1.4), [6.5.3](/6.5.3#sec-3.5)); acid–base equilibria and the **Henderson–Hasselbalch equation** ([6.1.9](/6.1.9)); and **surfactants** and **micelles** ([6.3.19](/6.3.19), [6.3.21](/6.3.21)). Fatty acids, lactic acid, citric acid, and pyruvic acid are central metabolites in biochemistry ([7.1](/7.1)), and this chapter also points out the connection between their chemical properties and their biological functions.

## 18.1. Structure, Nomenclature, and Physical Properties

### 18.1.1. Structure of the Carboxyl Group

**Definition 18.1.1 (Carboxylic Acid)** An organic compound that contains the carboxyl group $\ce{-COOH}$ (a carbonyl group and a hydroxy group on the same carbon) is called a **carboxylic acid**, with general formula $\ce{RCOOH}$. The group $\ce{RC(=O)-}$ that remains when the hydroxy group is removed is called the **acyl group**; a compound in which the acyl group is bonded to a heteroatom and which gives a carboxylic acid on hydrolysis is called a **carboxylic acid derivative**.

The carboxyl carbon is $\mathrm{sp^2}$-hybridized, its three σ bonds are coplanar, and the bond angles are close to 120°. The lone pair of the hydroxy oxygen is conjugated with the π bond of C=O (p–π conjugation), which can be represented by two **resonance structures**:

```smiles
CC(=O)O
CC([O-])=[OH+]
```

The second resonance structure has charge separation and contributes less, but it accounts for two facts. First, the electrophilicity of the carboxyl carbon is lower than that of the carbonyl carbon of aldehydes and ketones: the lone pair of the hydroxy group partly "fills in" the electron deficiency of the carbonyl carbon (the polar resonance structure $\ce{R2C+-O-}$ of a ketone has no such compensation). Second, the two oxygen atoms differ in **nucleophilicity** and basicity: the carbonyl oxygen (the doubly bonded oxygen) is more electron-rich, protonation occurs on the carbonyl oxygen, and the positive charge of the resulting cation can be delocalized over both oxygen atoms (the $\mathrm{p}K_{\mathrm{a}}$ of a protonated carboxylic acid in Table 3.1 is about $-6$). This is the starting point of acid-catalyzed acyl substitution in [6.5.19](/6.5.19#sec-19.2.3).

The bond lengths reflect this conjugation: in formic acid C=O is about 120 pm and C–OH about 134 pm (C–O of alcohols is about 143 pm), whereas the two C–O bonds of the formate ion are equal, about 127 pm. The negative charge of a carboxylate ion is shared equally by the two oxygen atoms, which is the structural basis of the acidity of carboxylic acids (Section 18.2).

The family of carboxylic acid derivatives is as follows (the structures and reactivity of acyl halides, anhydrides, esters, and amides are compared in [6.5.19](/6.5.19#sec-19.1); a nitrile is in the same oxidation state as a carboxylic acid and gives the acid on hydrolysis, so it is also counted as a derivative). The structures below are acetic acid, acetyl chloride, acetic anhydride, methyl acetate, acetamide, and acetonitrile, in that order:

```smiles
CC(=O)O
CC(=O)Cl
CC(=O)OC(C)=O
CC(=O)OC
CC(N)=O
CC#N
```

### 18.1.2. Nomenclature

In systematic nomenclature, the carboxyl group is among the principal characteristic groups of highest priority ([6.5.1](/6.5.1#sec-1.4.2)): the carbon chain containing the carboxyl group is the main chain, the carboxyl carbon is numbered 1, and the ending -e of the parent alkane name is replaced by -oic acid. When the carboxyl group is attached to a ring, or the chain cannot include the carboxyl carbon, the suffix -carboxylic acid is used (the carboxyl carbon is not counted in the parent). By custom, Greek letters $\alpha, \beta, \gamma, \delta, \dots$ are also used, beginning with the carbon attached to the carboxyl group, and the terminal carbon is called $\omega$.

```smiles
CCC(C)CCC(=O)O
OC(=O)C1CCCCC1
OC(=O)CC1CCCC1
OC(=O)/C=C/C(=O)O
```

These are 4-methylhexanoic acid ($\gamma$-methylhexanoic acid), cyclohexanecarboxylic acid, cyclopentylacetic acid, and (E)-but-2-enedioic acid (fumaric acid). Most common carboxylic acids are usually called by trivial names, which mostly derive from their sources:

| Structure | Systematic name | Trivial name | Source and use |
|---|---|---|---|
| $\ce{HCOOH}$ | Methanoic acid | Formic acid | Venom of ants and bees |
| $\ce{CH3COOH}$ | Ethanoic acid | Acetic acid | Vinegar (about 5%); annual production exceeds $10^7$ t |
| $\ce{CH3CH2CH2COOH}$ | Butanoic acid | Butyric acid | Smell of rancid butter and of sweat |
| $\ce{CH3(CH2)14COOH}$ | Hexadecanoic acid | Palmitic acid | Fats and oils ([6.5.19](/6.5.19#sec-19.9.2)) |
| $\ce{CH3(CH2)16COOH}$ | Octadecanoic acid | Stearic acid | Fats and oils, soap |
| $\ce{C6H5COOH}$ | Benzoic acid | Benzoic acid | Preservative |
| $\ce{HOOC-COOH}$ | Ethanedioic acid | Oxalic acid | Spinach, rhubarb |
| $\ce{HOOCCH2COOH}$ | Propanedioic acid | Malonic acid | Malonic ester synthesis ([6.5.22](/6.5.22#sec-22.9)) |
| $\ce{HOOC(CH2)2COOH}$ | Butanedioic acid | Succinic acid | Intermediate of the citric acid cycle |
| $\ce{HOOC(CH2)4COOH}$ | Hexanedioic acid | Adipic acid | Monomer of nylon-66 ([6.5.19](/6.5.19#sec-19.6.1)) |
| 1,2-$\ce{C6H4(COOH)2}$ | Benzene-1,2-dicarboxylic acid | Phthalic acid | Plasticizers, dyes |
| 1,4-$\ce{C6H4(COOH)2}$ | Benzene-1,4-dicarboxylic acid | Terephthalic acid | Monomer of the polyester PET |

Most carboxylic acids in nature contain other functional groups: tartaric acid in grapes, citric acid in lemons, and malic acid in apples are all hydroxy acids (Section 18.7.3). In the 1770s and 1780s Scheele isolated tartaric, citric, malic, oxalic, lactic, and gallic acids from such natural sources, an early example of the isolation and purification of organic compounds.

### 18.1.3. Physical Properties

Carboxylic acids are both donors (O–H) and acceptors (C=O) of **hydrogen bonds**, and form cyclic dimers through two O–H⋯O hydrogen bonds of about $25$–$34\,\mathrm{kJ\,mol^{-1}}$ each: the O–H groups of the two molecules point at the C=O of the partner, forming an eight-membered ring that contains two hydrogen bonds. The dimers are abundant in nonpolar solvents and even in the gas phase (vapor density measurements of acetic acid give a molar mass close to that of the dimer). The boiling points of carboxylic acids are therefore much higher than those of alcohols of similar molar mass: acetic acid 118 °C, propan-1-ol 97 °C; formic acid 101 °C, ethanol 78 °C. In water the carboxyl group forms hydrogen bonds with water; $\mathrm{C_1}$–$\mathrm{C_4}$ carboxylic acids are miscible with water, the solubility falls rapidly as the hydrocarbon chain lengthens, and fatty acids with more than ten carbons are practically insoluble in water.

The lower carboxylic acids have strong, irritating odors; the $\mathrm{C_4}$–$\mathrm{C_9}$ acids are oily liquids with a rancid smell, and the higher fatty acids are odorless waxy solids. The melting points of straight-chain saturated monocarboxylic acids show an *odd–even effect*: acids with an even number of carbons melt higher than both neighboring acids with an odd number of carbons (data from CRC):

| Number of carbons | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|
| Melting point / °C | 16.6 | $-20.5$ | $-5.1$ | $-33.6$ | $-3.4$ | $-7.2$ | 16.5 | 12.4 | 31.4 |

The odd–even effect comes from crystal packing: in a zigzag extended chain, the carboxyl and methyl ends of an even-numbered chain lie on opposite sides of the chain axis (trans), so the hydrogen-bonded dimers can pack tightly layer upon layer; the two ends of an odd-numbered chain lie on the same side, the packing is looser, and the lattice energy is lower. Liquid-state properties (boiling points) show no such alternation.

### 18.1.4. Spectroscopic Features

The main points for the structure determination of carboxylic acids are as follows (the principles are in [6.4.11](/6.4.11), [6.4.12](/6.4.12), and [6.4.15](/6.4.15), and the methods of interpretation in [6.5.6](/6.5.6)):

| Method | Feature | Remark |
|---|---|---|
| IR | O–H stretch $2500$–$3300\,\mathrm{cm^{-1}}$, very broad, often superimposed on the C–H bands | Strong **hydrogen bonding** in the dimer |
| IR | C=O stretch about $1710\,\mathrm{cm^{-1}}$ (dimer); monomer in dilute solution about $1760\,\mathrm{cm^{-1}}$; conjugated acids $1680$–$1700\,\mathrm{cm^{-1}}$ | Hydrogen bonding weakens the C=O bond |
| IR | Carboxylate: two bands at $1550$–$1610$ and about $1400\,\mathrm{cm^{-1}}$ (asymmetric and symmetric stretches) | The two C–O bonds are equivalent and there is no separate C=O |
| $^1\mathrm{H}$ NMR | COOH at $\delta$ about 10–13, broad singlet; disappears on addition of $\ce{D2O}$ | Deshielding by hydrogen bonding, fast exchange ([6.5.6](/6.5.6#sec-6.5.5)) |
| $^1\mathrm{H}$ NMR | α-H at $\delta$ about 2.0–2.5 | Similar to the α-H of ketones |
| $^{13}\mathrm{C}$ NMR | Carboxyl carbon at $\delta$ about 170–185 | Upfield of ketones and aldehydes (190–220), because of the electron-donating conjugation of the hydroxy group |
| MS | **McLafferty rearrangement** ion of straight-chain carboxylic acids at $m/z = 60$; $\mathrm{M}-17$ (loss of OH), $\mathrm{M}-45$ (loss of COOH) | Strong $\ce{ArCO+}$ peak for aromatic acids |

## 18.2. Acidity

### 18.2.1. Why Carboxylic Acids Are Acids

Carboxylic acids ionize partially in water:

$$
\ce{RCOOH + H2O <=> RCOO- + H3O+}, \qquad K_{\mathrm{a}} = \frac{a(\ce{RCOO-})\,a(\ce{H3O+})}{a(\ce{RCOOH})}.
$$
The $\mathrm{p}K_{\mathrm{a}}$ of a simple aliphatic monocarboxylic acid is between 4 and 5, so these are weak acids, but stronger than carbonic acid, and they react with $\ce{NaHCO3}$ to release $\ce{CO2}$. From the unified table of [6.5.3](/6.5.3#sec-3.1.4), several kinds of O–H acids compare as follows:

| Acid | $\ce{CH3CH2OH}$ | $\ce{H2O}$ | $\ce{C6H5OH}$ | $\ce{H2CO3}$ (apparent) | $\ce{CH3COOH}$ | $\ce{HCOOH}$ | $\ce{CF3COOH}$ |
|---|---|---|---|---|---|---|---|
| $\mathrm{p}K_{\mathrm{a}}$ (water, 25 °C) | 15.9 | 14.00 | 9.99 | 6.35 | 4.76 | 3.75 | 0.52 |

Acetic acid is about $10^{11}$ times as strong an acid as ethanol, mainly because the negative charge of the carboxylate ion is spread over two highly electronegative oxygen atoms by two equivalent **resonance structures** (equal bond lengths, Section 18.1.1), whereas the negative charge of ethoxide is concentrated on one oxygen. Resonance stabilization also operates in the carboxylic acid itself (the charge-separated resonance structure of Section 18.1.1), but is much larger in the carboxylate ion, where the two resonance structures are exactly equivalent and no charge separation is required. A further factor is the **inductive effect**: the $\mathrm{sp^2}$ carbonyl carbon and the electronegative carbonyl oxygen pull electrons away from the O–H bond. Computational studies suggest that the two factors contribute about equally, but however one apportions them, the result is that the negative charge is much more stable in the carboxylate ion than in an alkoxide.

![The two equivalent resonance structures of acetate: the lone pair of the negatively charged oxygen forms a C=O $\pi$ bond while the original C=O $\pi$ electrons move onto the other oxygen; the two oxygens share the negative charge equally, and the two C–O bonds have the same length](./plots/carboxylate-resonance.py)

### 18.2.2. Inductive Effects and Hybridization

Electron-withdrawing substituents spread the negative charge of the carboxylate ion more widely and increase the acidity; the effect weakens rapidly with distance, falling by about a factor of three to two for each intervening carbon ([6.5.2](/6.5.2#sec-2.3)):

| Acid | $\mathrm{p}K_{\mathrm{a}}$ | Acid | $\mathrm{p}K_{\mathrm{a}}$ |
|---|---|---|---|
| $\ce{CH3COOH}$ | 4.76 | $\ce{CH3CH2CH2COOH}$ (butanoic acid) | 4.83 |
| $\ce{ClCH2COOH}$ | 2.87 | $\ce{CH3CH2CHClCOOH}$ (2-chlorobutanoic acid) | 2.86 |
| $\ce{Cl2CHCOOH}$ | 1.35 | $\ce{CH3CHClCH2COOH}$ (3-chlorobutanoic acid) | 4.05 |
| $\ce{Cl3CCOOH}$ | 0.66 | $\ce{ClCH2CH2CH2COOH}$ (4-chlorobutanoic acid) | 4.52 |
| $\ce{CF3COOH}$ | 0.52 | $\ce{HOCH2COOH}$ (glycolic acid) | 3.83 |

The influence of alkyl groups is small: formic acid 3.75, acetic acid 4.76, propanoic acid 4.87. The statement that "alkyl groups donate electrons" describes the trend only qualitatively; in fact the influence of alkyl groups on the acidity of carboxylic acids in solution comes mainly from solvation ([6.5.3](/6.5.3#sec-3.3)).

The hybridization of the α carbon also has an effect: the higher the s character, the more electron-withdrawing the carbon. Propanoic acid 4.87, acrylic acid 4.25, propiolic acid 1.89; cyclohexanecarboxylic acid 4.90, benzoic acid 4.20.

### 18.2.3. Substituent Effects in Benzoic Acids and the Hammett Equation

The ionization of substituted benzoic acids is exactly the defining reaction of the **Hammett equation** (Definition 3.5.1): the **substituent constant** is $\sigma_{\mathrm{X}} = \mathrm{p}K_{\mathrm{a}}(\ce{C6H5COOH}) - \mathrm{p}K_{\mathrm{a}}(\ce{XC6H4COOH})$. The table gives data in water at 25 °C (CRC) and the resulting $\sigma$ values:

| Substituent | ortho $\mathrm{p}K_{\mathrm{a}}$ | meta $\mathrm{p}K_{\mathrm{a}}$ | para $\mathrm{p}K_{\mathrm{a}}$ | $\sigma_m$ | $\sigma_p$ |
|---|---|---|---|---|---|
| H | 4.20 | 4.20 | 4.20 | 0 | 0 |
| $\ce{CH3}$ | 3.91 | 4.27 | 4.36 | $-0.07$ | $-0.16$ |
| $\ce{OCH3}$ | 4.09 | 4.09 | 4.47 | $+0.11$ | $-0.27$ |
| OH | 2.97 | 4.08 | 4.54 | $+0.12$ | $-0.34$ |
| Cl | 2.90 | 3.83 | 3.98 | $+0.37$ | $+0.22$ |
| $\ce{NO2}$ | 2.17 | 3.45 | 3.44 | $+0.75$ | $+0.76$ |

Meta substituents act mainly through the inductive effect: methoxy and hydroxy are electron-withdrawing at the meta position ($\sigma_m > 0$, the electronegativity of oxygen) but electron-donating at the para position ($\sigma_p < 0$), because a lone pair at the para position can push electrons by conjugation onto the ring carbon that bears the carboxyl group, and this $+\mathrm{M}$ effect outweighs the $-\mathrm{I}$ effect. The nitro group is electron-withdrawing at both positions and has an additional $-\mathrm{M}$ effect at the para position, but for benzoic acid there is no direct conjugation between the carboxyl group and a para nitro group, so $\sigma_p$ and $\sigma_m$ differ little (for phenols $\sigma_p^-$ must be used, [6.5.3](/6.5.3#sec-3.5)). The $\sigma$ values in the table differ by no more than 0.04 from the compiled values of Hansch and coworkers in [6.5.3](/6.5.3#sec-3.5), because the latter were determined from just this type of data.

Ortho-substituted benzoic acids are all stronger than their para isomers, even when the substituent is an electron-donating methyl or methoxy group (2-methylbenzoic acid, 3.91, is stronger than benzoic acid). This *ortho effect* cannot be explained by electronic effects; the main reason is steric hindrance: an ortho substituent pushes the carboxyl group out of the plane of the benzene ring and destroys the conjugation between ring and carboxyl group. In benzoic acid the electron-donating conjugation of the ring stabilizes the un-ionized acid (just as a hydroxy group stabilizes a carboxyl group); when the conjugation is lost the acid is relatively less stable, while the carboxylate ion is little affected by conjugation, so the acidity increases. Salicylic acid (2-hydroxybenzoic acid, 2.97) has an additional factor: after ionization the carboxylate forms a very strong intramolecular **hydrogen bond** with the ortho hydroxy group, which stabilizes the conjugate base. Because ortho substituents have both steric effects and such special interactions, the Hammett equation applies only to meta and para substituents.

### 18.2.4. Dicarboxylic Acids and the Field Effect

The two ionization constants of dicarboxylic acids differ greatly (CRC, 25 °C):

| Acid | $\mathrm{p}K_{\mathrm{a1}}$ | $\mathrm{p}K_{\mathrm{a2}}$ | Acid | $\mathrm{p}K_{\mathrm{a1}}$ | $\mathrm{p}K_{\mathrm{a2}}$ |
|---|---|---|---|---|---|
| Oxalic acid | 1.25 | 3.81 | Adipic acid | 4.41 | 5.41 |
| Malonic acid | 2.85 | 5.70 | Maleic acid | 1.92 | 6.23 |
| Succinic acid | 4.21 | 5.64 | Fumaric acid | 3.02 | 4.38 |
| Glutaric acid | 4.32 | 5.42 | Phthalic acid | 2.94 | 5.43 |

The first ionization is strengthened by the other electron-withdrawing carboxyl group (the $\mathrm{p}K_{\mathrm{a1}}$ of oxalic and malonic acids is far lower than that of acetic acid), and the second ionization is weakened by the already negatively charged $\ce{-COO-}$: the electric field of the negative charge repels departure of the second proton through space, a typical example of the **field effect** of [6.5.2](/6.5.2#sec-2.7) (Definition 2.7.1). The farther apart the two carboxyl groups are, the closer $\mathrm{p}K_{\mathrm{a2}} - \mathrm{p}K_{\mathrm{a1}}$ comes to the value $\lg 4 \approx 0.6$ given by the statistical factor (1.0 for adipic acid). Maleic acid has the largest difference (4.3): after the first ionization, the cis carboxylate forms a strong intramolecular hydrogen bond with the remaining COOH, which both stabilizes the monoanion (low $\mathrm{p}K_{\mathrm{a1}}$) and makes the second proton hard to remove (high $\mathrm{p}K_{\mathrm{a2}}$); fumaric acid, which is trans, has no such interaction.

### 18.2.5. Salt Formation, Physiological pH, and Applications

Carboxylic acids react with NaOH, $\ce{Na2CO3}$, and $\ce{NaHCO3}$ to give carboxylate salts. The sodium, potassium, and ammonium salts dissolve in water but not in organic solvents such as diethyl ether, and the carboxylic acid precipitates again on acidification. This allows carboxylic acids to be separated from neutral and basic organic compounds, and $\ce{NaHCO3}$ also separates carboxylic acids from phenols ([6.5.3](/6.5.3#sec-3.1.2), Example 3.1.1):

$$
\ce{RCOOH + NaHCO3 -> RCOONa + H2O + CO2 ^}.
$$

By the **Henderson–Hasselbalch equation** $\mathrm{pH} = \mathrm{p}K_{\mathrm{a}} + \lg\frac{[\ce{A-}]}{[\ce{HA}]}$ ([6.1.9](/6.1.9)), at physiological pH 7.4 the ratio $[\ce{CH3COO-}]/[\ce{CH3COOH}]$ for acetic acid is $10^{7.4-4.76} \approx 440$. Carboxylic acids in cells therefore exist almost entirely as carboxylate ions: in biochemistry one speaks of "lactate", "pyruvate", and "citrate", and metabolites remain in the cell as anions and cannot pass freely through the cell membrane; amino acids exist as zwitterions, and the Asp and Glu side chains on the surface of proteins are negatively charged. The same holds for the carboxyl groups of drug molecules, which determine solubility, membrane permeability, and distribution in the body (for example, aspirin is absorbed as the neutral molecule in the acidic environment of the stomach).

The sodium and potassium salts of long-chain fatty acids are soaps. Sodium stearate has a hydrophobic long hydrocarbon chain and a hydrophilic carboxylate group and is a typical anionic **surfactant**: at low concentration it forms an oriented monolayer on the water surface, and above the **critical micelle concentration** it aggregates in water into **micelles** with the hydrocarbon chains inside and the carboxylate groups outside; grease dissolves in the hydrophobic interior of the micelles and is washed away ([6.3.19](/6.3.19), [6.3.21](/6.3.21)). In hard water soaps form insoluble calcium and magnesium salts ("soap scum"), and in acidic water they turn back into insoluble fatty acids, which is why synthetic detergents (sodium alkylbenzenesulfonates, whose conjugate acids are strong acids) have replaced soap. The alkaline hydrolysis of fats and oils to make soap (**saponification**) is in [6.5.19](/6.5.19#sec-19.9.2).

Salt formation is also used for **chiral resolution** ([6.5.5](/6.5.5#sec-5.7.2)): a racemic amine forms salts with a carboxylic acid that is pure as a single **enantiomer** (such as (R,R)-tartaric acid) to give a pair of diastereomeric salts, which are separated by fractional crystallization on the basis of different solubility and then treated with base to give the single enantiomer of the amine; racemic carboxylic acids are resolved with natural **chiral** amines (quinine, strychnine, or (S)-1-phenylethylamine).

## 18.3. Reduction of Carboxylic Acids

The oxidation state of the carboxyl carbon is +3, and its electrophilicity is lowered further by conjugation with the hydroxy group, so carboxylic acids are harder to reduce than aldehydes and ketones: neither ordinary catalytic hydrogenation nor $\ce{NaBH4}$ reduces them. The usual reducing agents are $\ce{LiAlH4}$ and borane, and the products are primary alcohols. The three reactions below use $\ce{LiAlH4}$, $\ce{BH3*THF}$, and $\ce{LiAlH4}$, in that order (in the third reaction the C=C bond is retained):

```smiles
CCC(=O)O>>CCCO
OC(=O)c1ccccc1>>OCc1ccccc1
C/C=C/C(=O)O>>C/C=C/CO
```

$\ce{LiAlH4}$ first reacts as a base with the carboxyl group, releasing $\ce{H2}$ to give the lithium carboxylate. The carboxylate is negatively charged and even less electrophilic, but activated by the **Lewis acid** $\ce{AlH3}$ (or a coordinated aluminum species) it can still accept hydride, and the **tetrahedral intermediate** formed loses an oxyaluminate to give the aldehyde. The aldehyde is far more reactive than the carboxylate and is reduced at once to the alkoxide, so the reaction cannot be stopped at the aldehyde stage, and hydrolysis gives the primary alcohol. An isolated C=C bond is unaffected.

![The first step of the reduction of a carboxylic acid by $\ce{LiAlH4}$ is an acid–base reaction: an Al–H bond pair takes the acidic proton and the O–H electrons stay on oxygen, releasing $\ce{H2}$; activated by aluminum, the carboxylate accepts a hydride, the tetrahedral intermediate loses an aluminum oxide to give the aldehyde, which is reduced at once, and workup gives the primary alcohol](./plots/lialh4-acid.py)

Borane (usually $\ce{BH3*THF}$ or $\ce{BH3*SMe2}$) has better **chemoselectivity**. Borane is an electron-deficient Lewis acid that first reacts with the carboxylic acid with release of $\ce{H2}$ to give the triacyloxyborane $\ce{(RCOO)3B}$; in such an acyloxyborane the lone pairs of oxygen are partly donated to boron, the carbonyl group is activated, and hydride is transferred intramolecularly to the carbonyl carbon. Because borane is an **electrophile**, the more basic (the more electron-rich) the carbonyl oxygen, the faster the reaction, so borane reduces carboxylic acids faster than esters and does not reduce nitro groups, halogens, or acyl chlorides, exactly opposite to the selectivity of $\ce{LiAlH4}$, whose reactivity is governed by **nucleophilicity**:

```smiles
OC(=O)CCC(=O)OC>>OCCCC(=O)OC
```

(The selectivities of the various hydride reagents toward the various classes of carbonyl compounds are in [6.5.17](/6.5.17#sec-17.1.1) and [6.5.19](/6.5.19#sec-19.7).) A carboxylic acid can also be converted first into an ester or acyl chloride and then reduced. Reducing a carboxylic acid directly to the aldehyde requires special methods, such as reduction with lithium in methylamine solution at low temperature, or reduction to the alcohol followed by oxidation ([6.5.10](/6.5.10#sec-10.6)).

Catalytic hydrogenation of carboxylic acids requires high temperature and pressure; industrially, fatty acids (or their methyl esters) are hydrogenated to fatty alcohols over copper chromite catalysts. Reduction of carboxylic acids with molecular hydrogen under mild conditions is a frontier of homogeneous catalysis: for example, a cobalt–tridentate phosphine (triphos) catalyst reported in 2015 hydrogenates carboxylic acids to alcohols at about 100 °C and 8 MPa of hydrogen, and mechanistic studies indicate that a cobalt hydride takes part in the hydride transfer.

## 18.4. Decarboxylation

**Definition 18.4.1 (Decarboxylation)** The reaction in which a carboxylic acid or its salt loses the carboxyl group and releases carbon dioxide is called **decarboxylation**:

$$
\ce{R-COOH -> R-H + CO2}.
$$

In decarboxylation a C–C bond is broken, the carboxyl group leaves as $\ce{CO2}$ (carbon in oxidation state +4), and the carbon left behind gains electrons or hydrogen (its oxidation state decreases), so decarboxylation is formally an intramolecular disproportionation. How easily decarboxylation proceeds depends on whether the **carbanion** left after C–C cleavage (or the **radical**, or the **enol** formed through a cyclic **transition state**) is stable.

### 18.4.1. Thermal Decarboxylation

Ordinary fatty acids and their salts decarboxylate only with difficulty, requiring strong heating and giving complex products. The laboratory preparation of methane is the heating of sodium acetate with soda lime (NaOH + CaO); dry distillation of calcium carboxylates gives ketones ("ketonic decarboxylation"; acetone was once made industrially from calcium acetate):

$$
\ce{CH3COONa + NaOH ->[\Delta] CH4 + Na2CO3}, \qquad \ce{(CH3COO)2Ca ->[\Delta] CH3COCH3 + CaCO3}.
$$

Decarboxylation is much easier when the α carbon carries a strongly electron-withdrawing group. Trichloroacetate decarboxylates on heating to give the trichloromethyl anion, which is protonated to chloroform; the negative charge is stabilized by the **inductive effect** of the three chlorine atoms:

$$
\ce{Cl3C-COO- -> Cl3C- + CO2}.
$$

![Decarboxylation of trichloroacetate: the oxide lone pair forms the second C=O bond of $\ce{CO2}$ and the C–C bond pair stays on the $\ce{CCl3}$ carbon; the trichloromethyl anion takes a proton from water to give chloroform](./plots/trichloroacetate.py)

β-Keto acids (3-oxo carboxylic acids) and malonic acids decarboxylate at 100–150 °C by a different mechanism: the O–H of the carboxyl group forms an intramolecular **hydrogen bond** with the oxygen of the β carbonyl group, and through a six-membered cyclic transition state, proton transfer, C–C bond cleavage, and formation of $\ce{CO2}$ occur in a concerted manner to give first the enol, which then tautomerizes to the ketone. This pathway does not go through a carbanion, so it occurs readily only in the free acid (not in the carboxylate).

![Decarboxylation of a β-keto acid: the carboxyl O–H of acetoacetic acid forms an intramolecular hydrogen bond with the ketone carbonyl oxygen; through a six-membered cyclic transition state the ketone oxygen takes the proton, the electrons of the O–H bond become the second C=O bond of CO₂, and the electrons of the C–C bond become the C=C bond of the enol; the enol tautomerizes to acetone](./plots/beta-keto-decarboxylation.py)

A fine piece of evidence for the cyclic transition state comes from Bredt's rule: a β-keto acid in which the carboxyl group is at a bicyclic bridgehead and the carbonyl group is on a bridge (such as ketopinic acid) does not decarboxylate even when heated above its melting point, because the enol formed by the cyclic mechanism would require a bridgehead double bond, which is too strained in a small bicyclic system (Bredt's rule, [6.5.9](/6.5.9#sec-9.1)). The decarboxylation of β-keto acids and malonic acids is the last step of the **acetoacetic ester synthesis** and the **malonic ester synthesis** ([6.5.22](/6.5.22#sec-22.8), [6.5.22](/6.5.22#sec-22.9)):

```smiles
CC(=O)CC(=O)O>>CC(C)=O.O=C=O
OC(=O)C(C)C(=O)O>>CCC(=O)O.O=C=O
```

When dicarboxylic acids are heated, the relative positions of the two carboxyl groups determine the product (Blanc's rule: when ring formation is possible, five- or six-membered rings are formed preferentially):

| Dicarboxylic acid | Product on heating | Type |
|---|---|---|
| Oxalic acid (160–180 °C) | $\ce{HCOOH + CO2}$ (formic acid decomposes further to $\ce{CO + H2O}$) | Decarboxylation |
| Malonic acid (140–160 °C) | $\ce{CH3COOH + CO2}$ | Decarboxylation (β-carbonyl acid type) |
| Succinic and glutaric acids (about 300 °C, or heated with acetic anhydride) | Succinic and glutaric anhydrides (five- and six-membered rings) | Intramolecular dehydration |
| Adipic and pimelic acids (heated with $\ce{Ba(OH)2}$ or acetic anhydride) | Cyclopentanone, cyclohexanone $+ \ce{CO2 + H2O}$ | Dehydration and decarboxylation |
| Longer dicarboxylic acids | Polyanhydrides (chains) | Intermolecular dehydration |

### 18.4.2. Kolbe Electrolysis and the Hunsdiecker Reaction

When a concentrated aqueous solution of a carboxylate is subjected to **electrolysis**, an alkane in which the two hydrocarbyl groups of the carboxylic acids are joined is formed at the anode (Kolbe, 1849), the first synthesis in **organic electrochemistry** ([6.3.14](/6.3.14), [6.5.31](/6.5.31#sec-31.7.4)):

$$
\ce{2RCOO- -> R-R + 2CO2 + 2e-}\ (\text{anode}), \qquad \ce{2H2O + 2e- -> H2 + 2OH-}\ (\text{cathode}).
$$

The carboxylate gives up an electron to the electrode by **single electron transfer**, forming an acyloxy **radical**; acyloxy radicals decarboxylate extremely fast (the lifetime of an alkyl acyloxy radical is of the order of nanoseconds), and the alkyl radicals formed meet at high concentration on the electrode surface and couple ([6.5.7](/6.5.7#sec-7.2.3)). A mixture of two carboxylates gives a mixture of three coupling products, so Kolbe electrolysis is used mainly to synthesize symmetrical long-chain compounds, for example dimethyl sebacate from monomethyl adipate.

![Kolbe electrolysis: propanoate loses one electron at the anode to give the acyloxy radical; the single electron on oxygen and one electron of the C–C bond form the second C=O bond of CO₂, and the other electron of the C–C bond stays on the ethyl carbon; two ethyl radicals couple to give butane](./plots/kolbe-electrolysis.py)

Heating a silver carboxylate with bromine in $\ce{CCl4}$ gives an alkyl bromide with one carbon fewer (the Hunsdiecker reaction, first observed by Borodin in 1861):

$$
\ce{RCOOAg + Br2 ->[\Delta] RBr + CO2 + AgBr}.
$$

The silver carboxylate first reacts with bromine to give the acyl hypobromite $\ce{RCOOBr}$; the weak O–Br bond undergoes **homolysis**, the acyloxy radical decarboxylates, and the alkyl radical abstracts a bromine atom from another molecule of $\ce{RCOOBr}$, which makes a chain reaction. The modification of Cristol and Firth, which uses HgO and the free carboxylic acid instead of the silver salt that is hard to dry, is more convenient. These two reactions illustrate a general idea: if a carboxylic acid is converted into a derivative that readily loses one electron or readily undergoes homolysis, the carboxyl group can be used as a "handle" to generate alkyl radicals. The modern Barton decarboxylation (thiohydroxamate esters) and photoredox decarboxylation are both based on this idea.

![The radical chain of the Hunsdiecker reaction: the weak O–Br bond of the acyl hypobromite breaks homolytically (fishhook arrows); the acyloxyl radical loses $\ce{CO2}$, and the ethyl radical abstracts a bromine atom from another acyl hypobromite, giving bromoethane and a new acyloxyl radical that carries the chain](./plots/hunsdiecker.py)

### 18.4.3. Biological Decarboxylation and Decarboxylative Coupling

All decarboxylations in living organisms are catalyzed by enzymes and always make use of an "electron sink": a structure that can temporarily accommodate the electron pair left after C–C cleavage, corresponding to the β carbonyl group in a β-keto acid.

- In the ethanol fermentation of yeast, pyruvate decarboxylase uses thiamine pyrophosphate (TPP, the coenzyme form of vitamin $\mathrm{B_1}$) as cofactor. After deprotonation at C2, the thiazolium ring of TPP becomes a nucleophilic **carbene** (**ylide**) that adds to the ketone carbonyl group of pyruvate; when the adduct decarboxylates, the electron pair flows into the positively charged thiazolium ring, just as it flows into the carbonyl group of a β-keto acid. The acetaldehyde obtained is then reduced to ethanol. The role of TPP is a kind of **umpolung** ([6.5.16](/6.5.16#sec-16.10.4), Breslow 1958).
- Decarboxylation of amino acids (to give neurotransmitters such as dopamine, histamine, and γ-aminobutyric acid) uses pyridoxal phosphate as cofactor: the amino group forms an **imine** with pyridoxal, and the pyridinium ring is the electron sink.
- In the citric acid cycle, isocitrate is first oxidized to a β-keto acid (oxalosuccinate) and then decarboxylates; in fatty acid synthesis, the decarboxylation of malonyl coenzyme A drives C–C bond formation ([6.5.22](/6.5.22#sec-22.10.2)). These are all biological versions of the decarboxylation of β-carbonyl acids.

![Decarboxylation in pyruvate decarboxylase: the C2 carbanion of the thiazolium ring of TPP has added to the ketone carbonyl of pyruvate; in the adduct the carboxylate leaves as $\ce{CO2}$, the C–C electrons form a C=C bond to C2, and the C=N$^+$ $\pi$ electrons move onto nitrogen, the positively charged ring acting as the electron sink. The enamine intermediate is protonated and releases acetaldehyde (R and R′ are the pyrimidinylmethyl group and the diphosphoethyl side chain)](./plots/tpp-decarboxylation.py)

![Amino acid decarboxylation assisted by pyridoxal phosphate (PLP): the amino acid forms an aldimine with PLP, the carboxylate leaves as $\ce{CO2}$, and the C–C electrons flow through the C=N bond and the pyridine ring onto the protonated ring nitrogen (the electron sink), giving the quinonoid intermediate; protonation at the α carbon and hydrolysis of the imine release the amine (R is the amino acid side chain; $\ce{CH2OP}$ is the phosphorylated hydroxymethyl group)](./plots/plp-decarboxylation.py)

In synthetic chemistry, carboxylic acids are widely available, stable, and cheap, and in recent years have been used extensively as precursors of alkyl radicals: "decarboxylative coupling" converts the C–COOH bond directly into a C–C or C–heteroatom bond. A representative piece of work is that of MacMillan and coworkers in 2014, which combined visible-light **photoredox catalysis** with nickel catalysis: an excited iridium photocatalyst oxidizes the carboxylate, the alkyl radical formed is captured by nickel and coupled with an aryl halide, and natural carboxylic acids such as amino acids are directly arylated at room temperature. The photophysics and catalytic cycles of such reactions are in [6.5.31](/6.5.31#sec-31.5).

## 18.5. α-Halogenation: The HVZ Reaction

The α-H of a carboxylic acid is weakly acidic, but the carboxyl group activates the α-H less than the carbonyl group of aldehydes and ketones does: **enolization** of carboxylic acids under acid catalysis is very slow, and base first removes the O–H proton, after which the carboxylate ion forms an **enolate** with still more difficulty. A carboxylic acid therefore cannot be α-halogenated directly like a ketone ([6.5.21](/6.5.21#sec-21.5)) and must first be converted into an acyl halide, which enolizes more readily.

**Definition 18.5.1 (Hell–Volhard–Zelinsky Reaction)** The reaction of a carboxylic acid with bromine (or chlorine) in the presence of a little red phosphorus (or $\ce{PBr3}$, $\ce{PCl3}$) to give an α-halo carboxylic acid is called the **Hell–Volhard–Zelinsky reaction** (HVZ reaction):

$$
\ce{RCH2COOH + Br2 ->[PBr3] RCHBrCOOH + HBr}.
$$

Phosphorus and bromine form $\ce{PBr3}$, which converts part of the carboxylic acid into the acyl bromide. In the acyl bromide the carbonyl group is no longer conjugated with a hydroxy group, the acidity of the α-H is similar to that in aldehydes and ketones, and the content of the **enol** is much higher than in the carboxylic acid; the enol undergoes **electrophilic addition** with bromine followed by deprotonation to give the α-bromo acyl bromide. The α-bromo acyl bromide then exchanges with another molecule of carboxylic acid (through a mixed anhydride or through **acyl transfer** via a **tetrahedral intermediate**, see [6.5.19](/6.5.19#sec-19.2)) to give the α-bromo carboxylic acid and regenerate the acyl bromide, so only a catalytic amount of $\ce{PBr3}$ is needed. The reaction stops at monosubstitution, since the bromine introduced slows enolization.

![Key steps of the HVZ reaction: propanoyl bromide enolizes under acid catalysis; the enol, pushed by the oxygen lone pair, attacks Br₂ with its C=C π bond to give the protonated α-bromo acyl bromide, which loses a proton to give 2-bromopropanoyl bromide; this exchanges with propanoic acid to give 2-bromopropanoic acid and regenerate propanoyl bromide](./plots/hvz.py)

The halogen of an α-halo carboxylic acid is activated by the adjacent carbonyl group and undergoes **SN2** substitution readily ([6.5.8](/6.5.8#sec-8.5.3)); these acids are intermediates for α-hydroxy acids, α-amino acids, and α-cyano acids. The two reactions below use a large excess of ammonia, and aqueous NaOH followed by acidification, respectively:

```smiles
CC(Br)C(=O)O>>CC(N)C(=O)O
CC(Br)C(=O)O>>CC(O)C(=O)O
```

The reaction of 2-bromopropanoic acid with a large excess of ammonia gives racemic alanine (the preparation of amino acids is in [6.5.33](/6.5.33)); if an ester or amide is wanted in the end, the α-bromo acyl bromide intermediate can be treated directly with an alcohol or amine.

## 18.6. Reactions with Organometallic Reagents

The O–H of a carboxylic acid is an active hydrogen ($\mathrm{p}K_{\mathrm{a}}$ about 4–5), whereas **Grignard reagents** and **organolithium reagents** are extremely strong bases (the conjugate acid, an alkane, has a $\mathrm{p}K_{\mathrm{a}}$ of about 50). When they meet, the acid–base reaction occurs first and the Grignard reagent is quenched; the magnesium carboxylate formed is insoluble in ether solvents, and the carbonyl group has lost its electrophilicity because of the negative charge, so the reaction stops there:

$$
\ce{RCOOH + R'MgX -> RCOOMgX + R'H}.
$$

There must therefore be no carboxyl group in the substrate when a Grignard reagent is prepared or used (if necessary, the carboxyl group is first protected in a form other than an ester, or another route is used, [6.5.20](/6.5.20#sec-20.8.3)). Conversely, addition of a Grignard reagent to $\ce{CO2}$ (dry ice) followed by acidification is an important way to prepare a carboxylic acid with one more carbon ([6.5.10](/6.5.10#sec-10.3.3), [6.5.20](/6.5.20#sec-20.7.1)).

Organolithium reagents differ: lithium carboxylates are soluble in ether, and the strong **nucleophilicity** of organolithium reagents lets them add to the carbonyl group of the lithium carboxylate to give a stable dilithium salt (the dianion of a gem-diol). Under the reaction conditions this tetrahedral dianion does not lose $\ce{O^2-}$, so it does not go on to form a ketone that would then be attacked again; it becomes the gem-diol only on hydrolysis, which loses water to give the ketone. The reaction of a carboxylic acid with 2 equivalents of an organolithium reagent is therefore a direct method for preparing a ketone from a carboxylic acid:

```smiles
OC(=O)C1CCCCC1>>CC(=O)C1CCCCC1
```

![Ketone synthesis from a carboxylic acid and two equivalents of methyllithium: the first equivalent removes the acidic proton; the C–Li electrons of the second add to the carbonyl carbon of the lithium carboxylate, giving a tetrahedral dilithium salt. It cannot lose $\ce{O^2-}$, so no ketone forms in the flask; hydrolysis gives the gem-diol, which loses water to give the methyl ketone](./plots/organolithium-acid.py)

The first equivalent of MeLi is used for deprotonation and the second adds. Compare [6.5.19](/6.5.19#sec-19.8): when an ester reacts with a Grignard reagent, the **tetrahedral intermediate** loses alkoxide to give a ketone, the ketone is more reactive than the ester, and the result is double addition to give a tertiary alcohol.

## 18.7. Special Carboxylic Acids

### 18.7.1. Unsaturated Carboxylic Acids

According to the position of the C=C (or C≡C) relative to the carboxyl group, unsaturated carboxylic acids are classified as α,β-unsaturated acids (conjugated), β,γ-unsaturated acids, and so on. Important examples are acrylic acid, crotonic acid ((E)-but-2-enoic acid), methacrylic acid (the monomer of Plexiglas, PMMA, which polymerizes as its methyl ester, [6.5.11](/6.5.11#sec-11.11)), and cinnamic acid (3-phenylacrylic acid). The E isomer of cinnamic acid melts at 133 °C and the Z isomer (allocinnamic acid) at about 68 °C: the trans molecule has a regular shape and packs more tightly in the crystal.

In α,β-unsaturated carboxylic acids, the lone pair of the carboxyl hydroxy group is already conjugated with C=O, so the conjugation between C=C and C=O is part of a cross-conjugated system, and the stabilization is less pronounced than in α,β-unsaturated ketones. The reactions of these compounds are similar to those of α,β-unsaturated aldehydes and ketones:

- **Nucleophiles** (amines, thiols, cyanide) add to the β carbon, formally a 3,4-addition to C=C but actually a **1,4-addition** (**conjugate addition**, Definition 17.6.1) to the conjugated system O=C–C=C; esters are more often used, because the free acid is first neutralized by the amine.
- They act as dienophiles in the **Diels–Alder reaction**, the electron-withdrawing carboxyl group lowering the LUMO of the C=C ([6.5.12](/6.5.12#sec-12.4.3)).

Almost all natural unsaturated fatty acids are cis (Z): oleic acid ((9Z)-octadec-9-enoic acid), linoleic acid (9Z,12Z), and α-linolenic acid (9Z,12Z,15Z, an $\omega$-3 fatty acid). A cis double bond bends the carbon chain, so the molecules cannot pack tightly, and fats and oils rich in unsaturated fatty acids are therefore liquid at room temperature ([6.5.19](/6.5.19#sec-19.9.2)). The bis-allylic C–H bonds of polyunsaturated fatty acids are weak and are the starting point of lipid peroxidation ([6.5.7](/6.5.7#sec-7.3.3)).

### 18.7.2. Halo Acids

The position of the halogen relative to the carboxyl group determines the reactions of halo acids:

- α-Halo acids: the halogen is activated by the carbonyl group and readily undergoes **SN2** substitution (Section 18.5).
- β-Halo acids: in base they readily eliminate HX to give α,β-unsaturated acids (the α-H is acidic, and the reaction proceeds by **E1cB** or **E2**, [6.5.9](/6.5.9#sec-9.5.1)).
- γ- and δ-Halo acids: in base the carboxylate acts as an intramolecular nucleophile and displaces the halogen to give five- and six-membered lactones (Section 18.7.3). When the halogen is farther from the carboxyl group, lactone and hydroxy acid form together; for example, 6-bromohexanoic acid and aqueous $\ce{Ag2O}$ give a mixture of ε-caprolactone (a seven-membered ring) and 6-hydroxyhexanoic acid.

![Lactonization of a γ-halo acid in base: the carboxylate oxygen attacks the carbon bearing bromine from the back side (an intramolecular SN2 reaction) and bromide leaves, closing the five-membered ring of γ-butyrolactone](./plots/halo-acid-lactone.py)

Several important halo acids:

- Chloroacetic acid is made by chlorination of acetic acid in the presence of a catalyst and is a raw material for the herbicide 2,4-D, carboxymethylcellulose, and glycine.
- Fluoroacetic acid and its salts are highly toxic (sodium fluoroacetate was used as the rodenticide "1080"). Fluoroacetic acid itself is not toxic: in the body it is treated as acetic acid and converted into fluoroacetyl coenzyme A, which enters the citric acid cycle to give fluorocitrate, and this strongly inhibits aconitase and interrupts the citric acid cycle. This phenomenon, in which the body's own metabolism turns a harmless substance into a poison, is called "lethal synthesis" (Peters, 1950s). The leaves of the South African plant *Dichapetalum cymosum* contain fluoroacetic acid, and the carcasses of livestock that have eaten it can poison scavengers.
- Trifluoroacetic acid (TFA, $\mathrm{p}K_{\mathrm{a}} = 0.52$) is a strong acid commonly used in organic synthesis; it is volatile and easy to remove, and is often used to remove the Boc **protecting group** and tert-butyl esters ([6.5.19](/6.5.19#sec-19.4.3), [6.5.20](/6.5.20#sec-20.8.3)). Trifluoroacetamides are hydrolyzed more easily than ordinary acetamides (the **inductive effect** of three fluorine atoms makes the carbonyl group more electrophilic) and can be removed with $\ce{K2CO3}$ in methanol, so the trifluoroacetyl group can serve as a protecting group for amino groups.

### 18.7.3. Hydroxy Acids, Lactones, and Lactides

The important hydroxy acids are all natural products and contain **stereocenters**:

| Hydroxy acid | Structure | Source and use |
|---|---|---|
| Lactic acid (2-hydroxypropanoic acid) | $\ce{CH3CH(OH)COOH}$ | (S)-Lactic acid from anaerobic metabolism in muscle, yogurt; polylactic acid |
| Malic acid (2-hydroxybutanedioic acid) | $\ce{HOOCCH(OH)CH2COOH}$ | Apples; the natural form is (S), an intermediate of the citric acid cycle |
| Tartaric acid (2,3-dihydroxybutanedioic acid) | $\ce{HOOCCH(OH)CH(OH)COOH}$ | Grapes and tartar; the natural form is (2R,3R), and there is also a **meso compound** |
| Citric acid (2-hydroxypropane-1,2,3-tricarboxylic acid) | $\ce{HOOCCH2C(OH)(COOH)CH2COOH}$ | Lemons; food acidulant, citric acid cycle |

Tartaric acid has three stereoisomers: a pair of **enantiomers** and a **meso compound** ([6.5.5](/6.5.5#sec-5.4.2)). In 1848 Pasteur picked out by hand the two mirror-image crystals from crystals of racemic sodium ammonium tartrate, accomplishing the first **resolution**. Although citric acid has no stereocenter, its two $\ce{CH2COOH}$ groups are **enantiotopic** and enzymes can distinguish them, Ogston's famous explanation in 1948 of isotope-labeling experiments ([6.5.5](/6.5.5#sec-5.9.2)).

The electron-withdrawing inductive effect of the hydroxy group makes hydroxy acids stronger acids than the corresponding carboxylic acids: glycolic acid 3.83, lactic acid 3.86, acetic acid 4.76. A hydroxy acid combines the properties of an alcohol and a carboxylic acid, and the two groups influence each other; the most characteristic reaction is dehydration on heating, with a product that depends on the position of the hydroxy group.

**Definition 18.7.1 (Lactone)** A cyclic ester formed by dehydration between the carboxyl group and the hydroxy group in the same molecule is called a **lactone**. According to the position of the hydroxy group on the carbon chain of the carboxylic acid, they are called β-lactones (four-membered ring), γ-lactones (five-membered ring), δ-lactones (six-membered ring), and so on; in systematic nomenclature the heterocycle name is used, for example γ-butyrolactone is oxolan-2-one.

**Definition 18.7.2 (Lactide)** The six-membered cyclic diester (1,4-dioxane-2,5-dione) formed by mutual esterification of two molecules of α-hydroxy acid is called a **lactide** (the lactide of lactic acid is specifically called lactide proper).

| Position of OH | Product on heating (or acid catalysis) | Reason |
|---|---|---|
| α | Dehydration between two molecules gives the lactide | Only a three-membered ring could form intramolecularly, which is too strained |
| β | Intramolecular dehydration gives the α,β-unsaturated acid | A four-membered lactone is strained; the α-H is acidic and elimination gives the conjugated product |
| γ, δ | Intramolecular esterification gives five- and six-membered lactones, often spontaneously | Small entropy loss on ring closure, strain-free rings |
| Farther apart | Intermolecular dehydration gives a chain polyester | Low probability of macrocycle formation (high dilution is needed to obtain macrolactones) |

The following show lactic acid forming lactide, 3-hydroxybutanoic acid dehydrating to crotonic acid, and 4-hydroxybutanoic acid forming γ-butyrolactone:

```smiles
CC(O)C(=O)O>>CC1OC(=O)C(C)OC1=O
CC(O)CC(=O)O>>C/C=C/C(=O)O
OCCCC(=O)O>>O=C1CCCO1
```

![Acid-catalyzed lactonization of 4-hydroxybutanoic acid: after protonation of the carbonyl oxygen, the hydroxy group at the other end of the chain attacks the activated carbonyl carbon (an intramolecular Fischer esterification), and the five-membered tetrahedral intermediate loses water and a proton to give γ-butyrolactone](./plots/gamma-lactonization.py)

The esterification equilibrium of γ- and δ-hydroxy acids lies strongly on the side of the lactone even when water is not removed: the intramolecular reaction loses no translational entropy and five- and six-membered rings are strain-free, in contrast to the intermolecular esterification of [6.5.19](/6.5.19#sec-19.4.1), which requires removal of water. Many natural products contain a lactone structure, for example vitamin C (ascorbic acid, a γ-lactone in which **enolization** has occurred) and the macrolide antibiotics (erythromycin).

Lactide undergoes ring-opening polymerization catalyzed by tin(II) octanoate to give polylactic acid (PLA). Polylactic acid can be made from lactic acid obtained by fermentation of corn starch, hydrolyzes to lactic acid in the body and in the environment, and is used for absorbable surgical sutures, bone screws, and biodegradable packaging. Ring-opening polymerization is a kind of **transesterification** ([6.5.19](/6.5.19#sec-19.5.2)).

Other reactions of hydroxy acids:

- α- and β-Hydroxy acids heated with aldehydes give five- and six-membered cyclic compounds similar to **acetals** (the hydroxy and carboxyl groups each contribute one oxygen, [6.5.16](/6.5.16#sec-16.5.2)).
- The hydroxy group and the carboxylate of an α-hydroxy acid can coordinate to a metal ion at the same time to form a five-membered **chelate** ring. Citrate and tartrate are important chelating agents, and citrate is used as an anticoagulant (chelating $\ce{Ca^2+}$) and as a detergent builder.
- When an α-hydroxy acid is heated with dilute sulfuric acid, it decomposes to an aldehyde (or ketone) with one carbon fewer and formic acid; heated with concentrated sulfuric acid, it gives the aldehyde (or ketone), CO, and water. α-Bromination of a carboxylic acid by the HVZ reaction, hydrolysis to the α-hydroxy acid, and then this degradation constitute a way to "shorten" a carboxylic acid by one carbon:

```smiles
CCC(O)C(=O)O>>CCC=O.OC=O
```

### 18.7.4. Phenolic Acids

Salicylic acid (2-hydroxybenzoic acid) is made from sodium phenoxide and $\ce{CO2}$ under pressure and heat (the **Kolbe–Schmitt reaction**; about 125 °C, under pressure) followed by acidification; potassium phenoxide at a higher temperature (190–200 °C) gives mainly the thermodynamically more stable 4-hydroxybenzoic acid. The mechanism and conditions are in [6.5.15](/6.5.15#sec-15.8.6).

```smiles
[O-]c1ccccc1.O=C=O>>OC(=O)c1ccccc1O
```

Salicylic acid combines the properties of a phenol and a carboxylic acid:

- It gives a violet color with $\ce{FeCl3}$ (a color reaction of coordination by the phenolic hydroxy group).
- It is a much stronger acid than benzoic acid ($\mathrm{p}K_{\mathrm{a}} = 2.97$), because of the intramolecular **hydrogen bond** in the conjugate base (Section 18.2.3).
- It decarboxylates to phenol when heated above its melting point. The strong electron-donating effect of the hydroxy group also activates the ring carbon that carries the carboxyl group (the ipso position): when salicylic acid reacts with bromine water, the carboxyl group is replaced by bromine, and, as with phenol, a white precipitate of 2,4,6-tribromophenol forms ([6.5.15](/6.5.15#sec-15.8.1)).

The acetylation product of salicylic acid, acetylsalicylic acid, is aspirin (for acetylation see [6.5.19](/6.5.19#sec-19.3.3)). Its mechanism of action is an **acyl transfer** reaction: aspirin transfers its acetyl group to a serine hydroxy group in the active site of cyclooxygenase (COX); the esterified serine blocks access of arachidonic acid to the active site, the enzyme is irreversibly inhibited, and the synthesis of prostaglandins (signaling molecules that cause inflammation, fever, and pain) is reduced. Vane clarified this action in 1971 and shared the 1982 Nobel Prize in Physiology or Medicine with Bergström and Samuelsson. The connection between chemical properties and biological function is clear here: an ordinary carboxylic ester does not acylate proteins, but the acetyl group of aspirin is attached to a phenolic oxygen, and the phenoxide ion ($\mathrm{p}K_{\mathrm{a}}$ about 10) is a much better **leaving group** than an alkoxide, so aspirin is an activated acyl donor ([6.5.19](/6.5.19#sec-19.2.2)).

![Acetylation of cyclooxygenase by aspirin: the hydroxy group of the active-site serine (Enz–$\ce{CH2OH}$; a nearby base takes its proton) adds to the acetyl carbonyl of aspirin; the tetrahedral intermediate collapses and expels the phenoxide of salicylate, a good leaving group, leaving the serine acetylated](./plots/aspirin-cox.py)

Other phenolic acids: 4-aminosalicylic acid (PAS) was an early antituberculosis drug; the esters of 4-hydroxybenzoic acid (parabens) are preservatives in foods and cosmetics; gallic acid (3,4,5-trihydroxybenzoic acid) occurs in the tannins of gallnuts and tea and decarboxylates readily on heating to pyrogallol (benzene-1,2,3-triol), a strong reducing agent.

### 18.7.5. Oxo Acids

Oxo acids (aldehyde acids and keto acids) are classified as α-, β-, and γ-oxo acids according to the position of the carbonyl group relative to the carboxyl group.

In α-oxo acids, the two adjacent electron-withdrawing carbonyl groups activate each other. Glyoxylic acid $\ce{OHC-COOH}$ occurs in unripe fruit and disappears when the fruit ripens; its aldehyde group is especially electrophilic, and in aqueous solution it exists almost entirely as the hydrate $\ce{(HO)2CH-COOH}$ (compare the hydration of trichloroacetaldehyde in [6.5.16](/6.5.16#sec-16.5.1)). Glyoxylic acid can be prepared by partial reduction of oxalic acid (electrolysis or Mg/$\ce{H2SO4}$) or by hydrolysis of dichloroacetic acid.

Pyruvic acid $\ce{CH3COCOOH}$ is the end product of glycolysis and stands at the crossroads of the metabolism of sugars, fats, and amino acids. In the laboratory it can be prepared by heating tartaric acid with potassium hydrogen sulfate (dehydration and decarboxylation), or by hydrolysis of acetyl cyanide (pyruvonitrile) obtained from acetyl chloride and copper(I) cyanide. Heated with dilute sulfuric acid, pyruvic acid decarboxylates to acetaldehyde (the pyruvate decarboxylase of Section 18.4.3 catalyzes the same transformation); heated with concentrated sulfuric acid it loses CO to give acetic acid, similar to the loss of CO by α-hydroxy acids in concentrated sulfuric acid (the two equations below are the reactions in dilute and in concentrated sulfuric acid, respectively):

```smiles
CC(=O)C(=O)O>>CC=O.O=C=O
CC(=O)C(=O)O>>CC(=O)O.[C-]#[O+]
```

All β-keto acids are unstable and decarboxylate readily to ketones (Section 18.4.1). The simplest β-keto acid, acetoacetic acid, is one of the "ketone bodies": during starvation or in diabetes, the liver converts fatty acids to acetoacetic acid and 3-hydroxybutanoic acid for use by other tissues, and part of the acetoacetic acid decarboxylates spontaneously to acetone, which is why the breath of a patient with diabetic ketoacidosis smells of acetone.

The simplest γ-keto acid is levulinic acid (4-oxopentanoic acid), which dehydrates on heating to α- and β-angelica lactones (**enol** forms of γ-lactones). Levulinic acid can be obtained from cellulose or hexoses in acid through 5-hydroxymethylfurfural and is one of the "platform chemicals" for producing fuels and chemicals from biomass; it can be hydrogenated further to γ-valerolactone (a green solvent and fuel additive).

## Summary

| Topic | Key points |
|---|---|
| Structure | Carboxyl carbon $\mathrm{sp^2}$, hydroxy group conjugated with C=O: the carbonyl carbon is less electrophilic than in ketones, and the carbonyl oxygen is the site of protonation; the two C–O bonds of a carboxylate are equal (127 pm) |
| Physical properties and spectra | Dimers held by **hydrogen bonds**: high boiling points; odd–even alternation of melting points; IR broad O–H (2500–3300) and C=O (about 1710); $^1\mathrm{H}$ 10–13; $^{13}\mathrm{C}$ 170–185 |
| Acidity | Aliphatic monocarboxylic acids $\mathrm{p}K_{\mathrm{a}}$ 4–5 (acetic acid 4.76); resonance-stabilized carboxylate; electron-withdrawing **inductive effect** decays with distance; ionization of benzoic acids defines the Hammett $\sigma$ (Definition 3.5.1); the ortho effect comes from steric inhibition of resonance; $\mathrm{p}K_{\mathrm{a2}}$ of diacids is affected by the **field effect**; exist as carboxylates at physiological pH |
| Reduction | $\ce{LiAlH4}$ or $\ce{BH3}$ give primary alcohols; $\ce{NaBH4}$ does not react; $\ce{BH3}$ reduces carboxylic acids selectively in the presence of esters |
| Decarboxylation (Definition 18.4.1) | β-Keto acids and malonic acids through a six-membered cyclic **transition state**; strongly electron-withdrawing α groups through a **carbanion**; Kolbe electrolysis and the Hunsdiecker reaction through **radicals**; biological decarboxylation uses TPP or PLP as the electron sink |
| HVZ (Definition 18.5.1) | Catalyzed by $\ce{PBr3}$, through the **enol** of the acyl bromide; α-halo acids undergo **SN2** to give α-hydroxy acids and α-amino acids |
| Organometallics | RMgX is quenched; 2 equivalents of RLi give ketones through a stable dianion; RMgX + $\ce{CO2}$ gives carboxylic acids |
| Special carboxylic acids | α,β-Unsaturated acids: **conjugate addition**, dienophiles; halo acids: substitution, elimination, or lactone formation depending on position; hydroxy acids: α gives lactides (Definition 18.7.2), β gives unsaturated acids, γ/δ give lactones (Definition 18.7.1); salicylic acid and aspirin; pyruvic acid, acetoacetic acid |

## Questions

1. Arrange the following compounds in order of decreasing acidity and explain: acetic acid, phenol, ethanol, carbonic acid (apparent), trifluoroacetic acid, chloroacetic acid, water.

   **Answer** Trifluoroacetic acid (0.52) > chloroacetic acid (2.87) > acetic acid (4.76) > carbonic acid (6.35) > phenol (9.99) > water (14.00) > ethanol (15.9). The negative charge of a carboxylate ion is spread over two oxygen atoms by two equivalent **resonance structures**, so carboxylic acids are stronger than phenol (the negative charge is delocalized onto ring carbons, with less stabilization) and alcohols; the electron-withdrawing **inductive effect** of halogens increases the acidity further, three fluorines the most. Note that water (14.00) is stronger than ethanol, and the value 15.7 commonly given in textbooks should not be used for the comparison ([6.5.3](/6.5.3#sec-3.1.3)).

2. Why is the second ionization constant of a dicarboxylic acid smaller than the first? How do you explain that $\mathrm{p}K_{\mathrm{a2}} - \mathrm{p}K_{\mathrm{a1}}$ for succinic acid (1.43) is larger than for adipic acid (1.00), and that for maleic acid (4.31) is much larger than for fumaric acid (1.36)?

   **Answer** After the first ionization the molecule carries a negative charge, and the electric field of $\ce{-COO-}$ makes it harder for the second proton to leave, through space (the **field effect**) and through the carbon chain (the inductive effect); about 0.6 further comes from the statistical factor (a diacid has two ionizable protons, and the dianion has two sites that can accept a proton). The closer the two carboxyl groups, the stronger the electrostatic interaction, so the difference for succinic acid is larger than for adipic acid. In maleic acid the two carboxyl groups are cis and very close, and the monoanion forms a strong intramolecular **hydrogen bond** $\ce{-COO^-\cdots H-O-}$, which both makes the first ionization easier and "locks" the second proton; fumaric acid is trans, its two carboxyl groups are far apart and cannot form an intramolecular hydrogen bond, and the difference is only slightly larger than the statistical factor.

3. Which of the following compounds decarboxylate readily on heating? Write the products and explain the mechanism: (a) 3-oxobutanoic acid; (b) 2,2-dimethylpropanedioic acid; (c) pentanoic acid; (d) an aqueous solution of sodium trichloroacetate; (e) 2-nitroacetic acid.

   **Answer** (a) Readily, through a six-membered cyclic **transition state** to prop-1-en-2-ol, which tautomerizes to acetone. (b) Readily, likewise through a cyclic transition state (the C=O of the other carboxyl group plays the role of the β carbonyl group), giving 2-methylpropanoic acid. (c) Not readily: the $\ce{C4H9-}$ anion left after decarboxylation has no stabilization, and there is no β carbonyl group to form a cyclic transition state. (d) Readily: trichloroacetate loses $\ce{CO2}$ to give $\ce{Cl3C-}$, stabilized by the inductive effect, and protonation gives chloroform. (e) Readily: the **carbanion** left after decarboxylation is resonance-stabilized by the nitro group (nitromethane $\mathrm{p}K_{\mathrm{a}} = 10.2$), and nitromethane is formed. The rule is that decarboxylation is easy when the electron pair left behind can be accepted by a π acceptor at the β position (carbonyl, nitro, cyano, vinyl) or by a strong inductive effect.

4. 2,4,6-Trimethylbenzoic acid is very hard to esterify by refluxing with methanol and a little sulfuric acid, but dissolving it in concentrated sulfuric acid and pouring the solution into methanol gives the methyl ester in high yield. Explain the two observations, and state under what conditions this ester can be hydrolyzed.

   **Answer** Ordinary acid-catalyzed esterification (the AAc2 mechanism of [6.5.19](/6.5.19#sec-19.4.3)) requires methanol to attack the carbonyl carbon to form a **tetrahedral intermediate**; the two ortho methyl groups block the path of attack, and the tetrahedral intermediate is also very crowded. In concentrated sulfuric acid the carboxylic acid is protonated on the hydroxy oxygen and loses water to give the acylium ion $\ce{ArC#O+}$: the carboxyl group is pushed out of the plane of the ring by the ortho methyl groups, the linear C≡O+ of the acylium ion is coplanar with the ring and is stabilized by the **hyperconjugation** of the three methyl groups and by conjugation with the ring, and its formation also relieves steric crowding. Methanol attacks the linear acylium ion without hindrance, so the yield is high. This is the AAc1 mechanism: a unimolecular cleavage of the acyl–oxygen bond through an acylium ion, not an **SN1** reaction at a saturated carbon. By microscopic reversibility, hydrolysis of this ester must also proceed by the same pathway in concentrated sulfuric acid (dissolve in concentrated sulfuric acid and pour into water).

5. How can the reactions of this chapter be used to convert pentanoic acid into butanal?

   **Answer** By degradation through an α-hydroxy acid, which removes one carbon at the carboxyl end of the molecule: (1) $\ce{Br2}$ and a little $\ce{PBr3}$ (HVZ reaction) give 2-bromopentanoic acid; (2) aqueous NaOH, then acidification, gives 2-hydroxypentanoic acid by **SN2** substitution; (3) heating with dilute sulfuric acid decomposes it to butanal and formic acid.

6. Design methods to prepare from cyclohexanecarboxylic acid (a) cyclohexylmethanol, (b) cyclohexyl methyl ketone, (c) methyl cyclohexanecarboxylate; why can methylmagnesium bromide not be used for (b)?

   **Answer** (a) $\ce{LiAlH4}$ (in diethyl ether), then hydrolysis; or $\ce{BH3*THF}$. (b) 2 equivalents of methyllithium, then hydrolysis with dilute acid: the first equivalent deprotonates and the second adds to the lithium carboxylate to give a stable dilithium salt, which loses water on hydrolysis to give the ketone. Methylmagnesium bromide only converts the carboxylic acid into the insoluble magnesium carboxylate and does not add further. (c) Reflux with methanol and a little concentrated sulfuric acid (**Fischer esterification**, Definition 19.4.1, with a large excess of methanol); or methylation of the carboxylate by SN2 with $\ce{K2CO3}$ and iodomethane in DMF (the carboxylate is a good **nucleophile**, and this method does not involve the carbonyl group and is suited to hindered acids).

7. Distinguish benzoic acid, phenol, benzyl alcohol, and salicylic acid by chemical methods, and separate a mixture of benzoic acid and phenol.

   **Answer** Add $\ce{NaHCO3}$ solution: benzoic acid and salicylic acid dissolve with evolution of $\ce{CO2}$, whereas phenol and benzyl alcohol do not react. Add $\ce{FeCl3}$ to the first two: salicylic acid gives a violet color (phenolic hydroxy group), whereas benzoic acid gives no color (a pale yellow precipitate forms). Add $\ce{FeCl3}$ or bromine water to the latter two: phenol gives a violet color or a white precipitate of 2,4,6-tribromophenol, whereas benzyl alcohol does not react. Separation: dissolve the mixture in diethyl ether and extract with aqueous $\ce{NaHCO3}$; benzoic acid goes into the aqueous layer as its sodium salt (the $\mathrm{p}K_{\mathrm{a}}$ of phenol, 9.99, is higher than that of carbonic acid, 6.35, so phenol is not converted by $\ce{NaHCO3}$), and acidification of the aqueous layer precipitates benzoic acid; evaporating the ether layer gives phenol.

8. Write the main product of heating (or acid catalysis) of (a) 4-hydroxybutanoic acid, (b) 3-hydroxybutanoic acid, (c) 2-hydroxypropanoic acid, (d) 10-hydroxydecanoic acid.

   **Answer** (a) γ-Butyrolactone (a five-membered ring, formed spontaneously in acid even at room temperature). (b) But-2-enoic acid (crotonic acid, mainly the E form); β-hydroxy acids dehydrate to the conjugated unsaturated acid. (c) Lactide (3,6-dimethyl-1,4-dioxane-2,5-dione), by double esterification between two molecules. (d) A chain polyester; the eleven-membered lactone can be obtained only under high dilution.
