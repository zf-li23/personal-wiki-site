---
title: Nucleophilic Acyl Substitution and Carboxylic Acid Derivatives
description: Structure, nomenclature, physical properties, and IR features of acyl halides, anhydrides, esters, and amides; the addition–elimination mechanism of nucleophilic acyl substitution, the tetrahedral intermediate, and the order of reactivity; acid–base catalysis and nucleophilic catalysis by DMAP; preparation and reactions of acyl chlorides and anhydrides; Fischer esterification and the four mechanisms of ester hydrolysis (BAc2, AAc2, AAc1, AAl1) with the evidence for them; lactones, transesterification, and polyesters (enzymatic degradation of PET); formation of amides (DCC) and their hydrolysis, nylons; reduction of derivatives and reactions with organometallic reagents; acyl transfer in biology (thioesters and coenzyme A, triglycerides and saponification, phospholipids).
source_hash: 7d8f42f92916
---

The carboxylic acid derivatives (acyl halides, anhydrides, esters, and amides) all contain the acyl group $\ce{RC(=O)-}$, and their interconversions with one another and with carboxylic acids follow a single mechanism: a **nucleophile** adds to the carbonyl carbon to give a tetrahedral intermediate, and a **leaving group** is then eliminated to regenerate C=O. This is nucleophilic acyl substitution. Together with nucleophilic substitution at saturated carbon in [6.5.8](/6.5.8), it is one of the two most fundamental substitution mechanisms in organic chemistry, and it is the most common reaction in protein synthesis, fat metabolism, and drug action in living organisms.

This chapter first compares the structures and reactivities of the various derivatives and establishes the addition–elimination mechanism and the order of reactivity. It then discusses in turn acyl halides and anhydrides; esters (the four mechanisms of esterification and hydrolysis, lactones, transesterification, and polyesters); the formation and hydrolysis of amides; and the addition of hydride reagents and organometallic reagents to the derivatives. Finally it treats acyl transfer in biology: thioesters and coenzyme A, triglycerides and saponification, and phospholipids. The properties of carboxylic acids themselves are in [6.5.18](/6.5.18); other reactions of amides (the **Hofmann rearrangement**, dehydration), nitriles, carbonic acid derivatives, and synthesis design are in [6.5.20](/6.5.20); reactions at the α carbon of esters (the **Claisen condensation**) are in [6.5.22](/6.5.22); the formation of the peptide bond and the chemical synthesis of peptides are in [6.5.33](/6.5.33). This chapter uses the **nucleophilic addition** to carbonyl groups of [6.5.16](/6.5.16#sec-16.2), the $\mathrm{p}K_{\mathrm{a}}$ table and the **Hammett equation** of [6.5.3](/6.5.3#sec-3.1.4), and the concepts of **leaving group** and **carbocation** of [6.5.8](/6.5.8#sec-8.6).

## 19.1. Structure and Properties of Carboxylic Acid Derivatives

### 19.1.1. Classification and Nomenclature

**Definition 19.1.1 (Acyl Halides, Anhydrides, Esters, and Amides)** A compound $\ce{RCOX}$ in which the hydroxy group of a carboxyl group is replaced by a halogen is called an **acyl halide**. The compound $\ce{RCO-O-COR'}$ formed by dehydration of two molecules of carboxylic acid is called an **acid anhydride**. A compound $\ce{RCOOR'}$ in which the hydroxy group is replaced by an alkoxy or aryloxy group is called an **ester**. A compound $\ce{RCONR'2}$ in which the hydroxy group is replaced by an amino or substituted amino group is called an **amide**. Cyclic esters and amides are called lactones and lactams, respectively.

All are named on the basis of the corresponding carboxylic acid:

| Class | Name format | Examples |
|---|---|---|
| Acyl halides | -oyl halide (-carbonyl halide) | Acetyl chloride, benzoyl chloride |
| Anhydrides | -oic anhydride; for unsymmetrical anhydrides the acids are cited in alphabetical order | Acetic anhydride, acetic propanoic anhydride, succinic anhydride, phthalic anhydride |
| Esters | Alkyl -oate | Ethyl acetate, diethyl malonate |
| Amides | -amide; substituents on N take the prefix N- | N,N-Dimethylformamide (DMF), N-methylacetamide |
| Lactones, lactams | -olide or the heterocycle name | γ-Butyrolactone (oxolan-2-one), ε-caprolactam (azepan-2-one) |

```smiles
CCC(=O)Cl
CC(=O)OC(=O)CC
O=C1CCC(=O)O1
CCOC(=O)CC(=O)OCC
CN(C)C=O
O=C1CCCCCN1
```

These are propanoyl chloride, acetic propanoic anhydride, succinic anhydride, diethyl malonate, DMF, and ε-caprolactam.

### 19.1.2. Electronic Structure: Competition between Induction and Resonance

In every derivative the acyl group is attached to an atom L that carries a lone pair, and L acts on the carbonyl group in two ways at once:

- The **inductive effect**: L is more electronegative than carbon and withdraws electrons through the σ bond, making the carbonyl carbon more electron-poor;
- The **conjugation effect**: the lone pair of L is conjugated with the π bond of C=O (p–π conjugation) and pushes electrons toward the carbonyl carbon, which can be represented by the charge-separated **resonance structure** $\ce{R-C(-O^-)=L+}$.

The balance between the two determines the electrophilicity of the carbonyl group. The lone pair of nitrogen is high in energy (nitrogen is less electronegative) and similar in size to the carbon 2p orbital, so conjugation is the strongest and the carbonyl carbon of an amide is the least electrophilic. The lone pair of chlorine is in a 3p orbital that overlaps poorly with the carbon 2p orbital, so conjugation is very weak while inductive electron withdrawal is strong, and the carbonyl carbon of an acyl chloride is the most electrophilic. The alkoxy group of an ester lies between the two; in an anhydride the lone pair of the bridging oxygen must be conjugated with two carbonyl groups at once and donates less to each.

There is direct structural evidence for the conjugation in amides. The C–N bond of an amide (about 135 pm) is distinctly shorter than that of an amine (about 147 pm); N is trigonal planar, and O, C, N and the atoms attached to them are coplanar. The barrier to rotation about the C–N bond is about $80$–$90\,\mathrm{kJ\,mol^{-1}}$, and rotation is slow at room temperature, so the two methyl groups of DMF appear in the $^1\mathrm{H}$ NMR spectrum as two separate singlets ($\delta$ about 2.9 and 3.0), one on the same side as the carbonyl oxygen and one on the same side as the hydrogen ([6.5.6](/6.5.6#sec-6.5.5)). The planarity and rigidity of the peptide bond are the basis of the secondary structure of proteins ([6.5.33](/6.5.33)).

### 19.1.3. Physical Properties and Spectra

Acyl chlorides, anhydrides, and esters have no O–H or N–H and cannot form **hydrogen bonds** with one another, so their boiling points are much lower than those of carboxylic acids of similar molar mass. Primary and secondary amides form strong N–H⋯O=C hydrogen bonds between molecules and have high boiling and melting points; all but formamide are solids. Tertiary amides have no N–H but have large dipole moments (DMF about 3.8 D) and still boil high.

| Compound | $\ce{CH3COCl}$ | $\ce{CH3COOCH3}$ | $\ce{(CH3CO)2O}$ | $\ce{CH3COOH}$ | $\ce{CH3CON(CH3)2}$ | $\ce{CH3CONH2}$ |
|---|---|---|---|---|---|---|
| Boiling point / °C | 51 | 57 | 140 | 118 | 165 | 221 |

Acyl halides and anhydrides are irritants and decompose on contact with water; lower esters have fruity odors and are the source of the aromas of many flowers and fruits (isopentyl acetate smells of banana and methyl butanoate of pineapple). DMF, N,N-dimethylacetamide (DMA), and N-methylpyrrolidone (NMP) are commonly used **polar aprotic solvents**.

The carbonyl stretching frequency directly reflects the electronic effects of Section 19.1.2: inductive electron withdrawal shortens and strengthens the C=O bond and raises the frequency; conjugative electron donation gives the C=O bond some single-bond character and lowers the frequency (the carbonyl region is discussed in detail in [6.5.6](/6.5.6#sec-6.4.2)).

| Compound | Acetyl chloride | Acetic anhydride | Methyl acetate | Acetaldehyde | Acetone | Acetic acid (dimer) | Acetamide | Acetate ion |
|---|---|---|---|---|---|---|---|---|
| $\tilde\nu(\ce{C=O}) / \mathrm{cm^{-1}}$ | 1806 | 1820, 1760 | 1746 | 1727 | 1715 | 1710 | about 1680 | about 1580 |

An anhydride has two carbonyl bands, from coupling of the symmetric and asymmetric stretches of the two C=O groups. The C=O band of an amide (the "amide I band") lies at $1630$–$1690\,\mathrm{cm^{-1}}$ and is an infrared probe for the secondary structure of proteins ([6.4.11](/6.4.11)). In $^{13}\mathrm{C}$ NMR the carbonyl carbons of the derivatives are all at $\delta$ 160–180, upfield of aldehydes and ketones.

## 19.2. Nucleophilic Acyl Substitution

### 19.2.1. The Addition–Elimination Mechanism

After a **nucleophile** adds to an aldehyde or ketone, the tetrahedral product has no good **leaving group**, and the reaction stops at the addition product ([6.5.16](/6.5.16#sec-16.2.1)). The carbonyl carbon of a carboxylic acid derivative bears a group L that can leave, so the tetrahedral intermediate formed on addition can lose L and regenerate C=O, and the net result is substitution:

$$
\ce{RCOL + Nu- -> RCONu + L-}.
$$

**Definition 19.2.1 (Nucleophilic Acyl Substitution)** The reaction in which a nucleophile replaces the leaving group attached to the carbonyl carbon of an acyl compound is called **nucleophilic acyl substitution**, also called an acyl transfer reaction. It generally proceeds by the addition–elimination mechanism: the nucleophile first adds to the carbonyl carbon, which changes from $\mathrm{sp^2}$ to $\mathrm{sp^3}$, and the leaving group then departs with its electron pair, returning the carbonyl carbon to $\mathrm{sp^2}$.

**Definition 19.2.2 (Tetrahedral Intermediate)** The $\mathrm{sp^3}$ intermediate $\ce{R-C(O^-)(Nu)(L)}$ (or its protonated form) formed in nucleophilic acyl substitution by addition of the nucleophile to the carbonyl carbon is called the **tetrahedral intermediate**.

![The addition–elimination mechanism of nucleophilic acyl substitution (basic hydrolysis of methyl acetate as an example): hydroxide adds to the carbonyl carbon, the π electrons of C=O move onto oxygen, and the tetrahedral intermediate forms; the electron pair on the oxide pushes back and methoxide leaves; acetic acid gives its proton to methoxide, which makes the whole reaction irreversible](./plots/tetrahedral-intermediate.py)

This differs from **SN2** at saturated carbon, where formation of the new bond and cleavage of the old bond occur simultaneously through a five-coordinate **transition state**; nucleophilic acyl substitution goes through a real four-coordinate intermediate, and the two steps are separate. Evidence for the mechanism comes from isotope exchange (Bender, 1951): when ethyl benzoate labeled with $^{18}\mathrm{O}$ in the carbonyl oxygen is hydrolyzed with base in ordinary water and the reaction is stopped part way, the $^{18}\mathrm{O}$ content of the unhydrolyzed ester recovered has fallen. The two oxygens of the tetrahedral intermediate (the original carbonyl oxygen and the oxygen from $\ce{HO-}$) become equivalent by proton transfer, so if the intermediate loses $\ce{HO-}$ instead of ethoxide and returns to the ester, there is a one-half chance that the labeled oxygen is lost. Direct SN2-type substitution would not cause unreacted ester to lose the label.

Addition to the carbonyl carbon is in most cases the **rate-determining step**. On going from the reactants to the tetrahedral intermediate the carbonyl carbon accumulates negative charge, so electron-withdrawing substituents accelerate the reaction: the Hammett reaction constant for basic hydrolysis of ethyl benzoates is $\rho = +2.5$ ([6.5.3](/6.5.3#sec-3.5)).

### 19.2.2. Order of Reactivity

The approximate relative rates of reaction of the derivatives with water (hydrolysis) are:

$$
\ce{RCOCl} > \ce{(RCO)2O} > \ce{RCOOR'} > \ce{RCONH2}, \qquad 10^{11} : 10^{7} : 1 : <10^{-2}.
$$

The two steps explain this order separately:

- The addition step: the more electrophilic the carbonyl carbon, the faster the addition. According to Section 19.1.2, acyl chlorides are the most electrophilic (the conjugation of Cl is weak) and amides the least (the conjugation of N is strong).
- The elimination step: the more stable (the less basic) the leaving group, the more easily it leaves. The basicities of the leaving groups can be compared through the $\mathrm{p}K_{\mathrm{a}}$ values of their conjugate acids ([6.5.3](/6.5.3#sec-3.1.4)): $\ce{Cl-}$ (HCl about $-7$), $\ce{RCOO-}$ (4.76), $\ce{RO-}$ (about 16), $\ce{NH2-}$ ($\ce{NH3}$ about 38).

The two factors give the same order. This leads to a general rule for the interconversion of derivatives: reactions always go from the more reactive to the less reactive derivative ("downhill"); an acyl chloride can be converted directly into an anhydride, ester, or amide, and an ester can be converted into an amide, but not the reverse. To turn a less reactive derivative into a more reactive one, it must first be hydrolyzed to the carboxylic acid, which is then activated as an acyl chloride or anhydride (Section 19.3).

Note that leaving ability depends on the basicity of the leaving group, not on the **electronegativity** of L. Fluorine is more electronegative than chlorine, but $\ce{F-}$ is a much stronger base than $\ce{Cl-}$ (the $\mathrm{p}K_{\mathrm{a}}$ of HF is 3.20) and the conjugation of the 2p lone pairs of F with the carbonyl group is also stronger, so acyl fluorides are much more stable than acyl chlorides, can exist in water for a short time, and are used in peptide synthesis as a mild form of carboxyl activation.

### 19.2.3. Acid and Base Catalysis

When the nucleophile is very weak (water, alcohols) and the carbonyl group is not reactive enough (esters, amides, carboxylic acids), the reaction needs catalysis, a kind of **acid–base catalysis**:

- Base catalysis: the base converts a weak nucleophile into a strong one ($\ce{H2O -> HO-}$, $\ce{ROH -> RO-}$). In the basic hydrolysis of esters $\ce{HO-}$ is consumed, so strictly it is "base-promoted" rather than catalyzed. Weaker bases (such as acetate and imidazole) can also partly remove a proton from the attacking water molecule in the transition state, which is called general base catalysis and is very common in the active sites of enzymes.
- Acid catalysis: protonation of the carbonyl oxygen (the cation formed is stabilized by resonance over two oxygens) greatly raises the electrophilicity of the carbonyl carbon, so that even weak nucleophiles can add; the leaving group is also protonated and becomes a good leaving group ($\ce{-OH -> -OH2+}$, $\ce{-OR -> -O+HR}$, $\ce{-NH2 -> -NH3+}$).

When the nucleophile is itself a base (an amine), or the product contains a strong acid (HCl), acid catalysis and the use of base are limited; these specific cases are discussed in the later sections.

## 19.3. Acyl Halides and Anhydrides

### 19.3.1. Preparation of Acyl Chlorides

The hydroxy group of a carboxylic acid is a poor **leaving group** ($\ce{HO-}$, $\mathrm{p}K_{\mathrm{a}}$ 14.00), so to prepare an acyl chloride it must first be converted into a good one. The usual reagents are thionyl chloride $\ce{SOCl2}$, oxalyl chloride $\ce{(COCl)2}$ (with a catalytic amount of DMF), $\ce{PCl3}$, and $\ce{PCl5}$:

$$
\ce{RCOOH + SOCl2 -> RCOCl + SO2 ^ + HCl ^}, \qquad \ce{3RCOOH + PCl3 -> 3RCOCl + H3PO3}.
$$

The advantage of thionyl chloride is that the by-products are all gases, which leave the reaction mixture and drive the reaction to completion, and the product can simply be distilled. The mechanism has two parts: the carboxylic acid attacks sulfur and loses HCl to give an acyl chlorosulfite; the $\ce{-OS(O)Cl}$ group of the latter is an excellent leaving group, chloride substitutes it by the addition–elimination mechanism, and the departing $\ce{ClSO2-}$ decomposes into $\ce{SO2}$ and $\ce{Cl-}$.

![Conversion of a carboxylic acid into an acyl chloride with thionyl chloride: in the acyl chlorosulfite, chloride adds to the carbonyl carbon to give a tetrahedral intermediate; the electron pair on the oxide pushes back, and chlorosulfite leaves and decomposes into SO₂ and chloride](./plots/thionyl-chloride.py)

The oxalyl chloride–DMF method is milder: DMF and oxalyl chloride form the chloroiminium salt (the Vilsmeier reagent) $\ce{[Me2N=CHCl]+Cl-}$, which activates the carboxylic acid and regenerates DMF, so only a catalytic amount of DMF is needed; the by-products CO, $\ce{CO2}$, and HCl are all gases.

![Acyl chloride formation with oxalyl chloride and DMF: top, DMF and oxalyl chloride give the chloroiminium (Vilsmeier) reagent with loss of CO and $\ce{CO2}$; middle, the carboxylic acid displaces chloride from the reagent to give an acyloxyiminium ion, and chloride adds to its carbonyl carbon; bottom, the tetrahedral intermediate collapses, the C–O electrons forming the C=O bond of DMF and the C=N$^+$ $\pi$ electrons moving onto nitrogen, so DMF is released and the acyl chloride forms](./plots/vilsmeier-acyl-chloride.py)

### 19.3.2. Reactions of Acyl Chlorides

Acyl chlorides are the most reactive derivatives and react rapidly with water, alcohols, and amines at room temperature without a catalyst, but base is needed to neutralize the HCl formed:

```smiles
CC(=O)Cl.O>>CC(=O)O.Cl
CC(=O)Cl.OCC>>CCOC(C)=O.Cl
CC(=O)Cl.NC>>CNC(C)=O.Cl
```

These are hydrolysis, alcoholysis (with pyridine or triethylamine added), and aminolysis (with 2 equivalents of amine, one of which acts as the base; or in a two-phase system of aqueous NaOH and an organic solvent, the Schotten–Baumann conditions). Only primary and secondary amines and ammonia give stable amides. The acylammonium ion formed by attack of a tertiary amine on an acyl chloride has no N–H and cannot lose a proton to become a neutral amide; it is positively charged, is itself a very strong acylating agent, and transfers the acyl group to other **nucleophiles**, which is the principle of nucleophilic catalysis below. The **Friedel–Crafts acylation** of arenes with acyl chlorides in the presence of $\ce{AlCl3}$ is in [6.5.14](/6.5.14#sec-14.9.3).

![Aminolysis of acetyl chloride by methylamine: the amine nitrogen adds to the carbonyl carbon and the C=O $\pi$ electrons move onto oxygen; the tetrahedral intermediate collapses, the oxide pushing back and chloride leaving; a second equivalent of amine removes the proton from nitrogen, giving N-methylacetamide](./plots/acyl-chloride-amine.py)

In acylation reactions pyridine is more than a base. 4-Dimethylaminopyridine (DMAP), as a nucleophilic catalyst, accelerates the acylation of alcohols by anhydrides (including hindered tertiary alcohols) by about $10^4$: the ring nitrogen of DMAP is more nucleophilic than the oxygen of an alcohol and first forms an N-acylpyridinium ion with the anhydride; the positive charge of the pyridinium ion can be delocalized onto the dimethylamino group, so it forms easily; its carbonyl group is extremely electrophilic and the leaving group (neutral DMAP) is excellent, so it is much more reactive than the anhydride. The alcohol attacks the N-acylpyridinium ion, and DMAP leaves and is regenerated.

![Nucleophilic catalysis by DMAP: the ring nitrogen of DMAP attacks acetic anhydride (addition–elimination combined into one step) to give the N-acetylpyridinium ion and acetate; ethanol adds to the N-acetylpyridinium ion, neutral DMAP leaves, and loss of a proton gives ethyl acetate and regenerates DMAP](./plots/dmap-catalysis.py)

### 19.3.3. Anhydrides

Direct dehydration of two molecules of carboxylic acid ($\ce{P2O5}$) is inefficient. Methods commonly used in the laboratory are the reaction of an acyl chloride with a carboxylate (which can give unsymmetrical anhydrides); heating a carboxylic acid with acetic anhydride while continuously distilling off the acetic acid formed, to give higher anhydrides; and heating of diacids to give five- and six-membered cyclic anhydrides (succinic, glutaric, phthalic, and maleic anhydrides, [6.5.18](/6.5.18#sec-18.4.1)). Industrially, acetic anhydride is made by addition of acetic acid to ketene ([6.5.17](/6.5.17#sec-17.9)) or by carbonylation of methyl acetate.

The reactions of anhydrides are the same as those of acyl chlorides, only milder; the leaving group is a carboxylate and the by-product is a carboxylic acid rather than HCl. Acetic anhydride is the most commonly used acetylating reagent:

```smiles
OC(=O)c1ccccc1O.CC(=O)OC(C)=O>>CC(=O)Oc1ccccc1C(=O)O.CC(=O)O
Oc1ccc(N)cc1.CC(=O)OC(C)=O>>CC(=O)Nc1ccc(O)cc1.CC(=O)O
```

The first is the acetylation of salicylic acid to aspirin (catalyzed by a little concentrated sulfuric acid), and the second the acetylation of 4-aminophenol to paracetamol (acetaminophen): the amino group is much more nucleophilic than the phenolic hydroxy group, and only N is acetylated, a simple example of **chemoselectivity**.

Cyclic anhydrides react with nucleophiles by ring opening to give products with a derivative at one end and a free carboxyl group at the other. This is a good way to derivatize a symmetrical diacid at one end only: directly treating the diacid with 1 equivalent of amine gives a mixture of monoamide, diamide, and starting material, whereas if the diacid is first converted into the cyclic anhydride, the anhydride has only one "leaving group", and the carboxylate formed on ring opening does not react further.

```smiles
O=C1CCCC(=O)O1.CCCNC>>CCCN(C)C(=O)CCCC(=O)O
```

![Ring opening of glutaric anhydride: the amine adds to one carbonyl carbon, and collapse of the tetrahedral intermediate expels the ring oxygen as a carboxylate in the same molecule; proton transfer from nitrogen gives the amide acid, and the carboxylate is not attacked again](./plots/anhydride-opening.py)

(Glutaric anhydride and N-methylpropylamine give 5-[methyl(propyl)amino]-5-oxopentanoic acid.) In an unsymmetrical mixed anhydride the nucleophile attacks the less hindered, more electrophilic carbonyl group. This can be exploited by forming a mixed anhydride of a carboxylic acid with a hindered acyl chloride (such as pivaloyl chloride or 2,4,6-trichlorobenzoyl chloride) so that the alcohol attacks only the carbonyl group of the original carboxylic acid; the latter, in the presence of DMAP, is used in the synthesis of macrolactones (the Yamaguchi esterification, 1979).

## 19.4. Esterification and Ester Hydrolysis

### 19.4.1. Fischer Esterification

**Definition 19.4.1 (Fischer Esterification)** The reversible reaction in which a carboxylic acid and an alcohol are heated with a strong acid catalyst (concentrated sulfuric acid, p-toluenesulfonic acid, dry HCl) to give an ester and water is called **Fischer esterification** (Fischer and Speier, 1895):

$$
\ce{RCOOH + R'OH <=>[\ce{H+}] RCOOR' + H2O}.
$$

Esterification is reversible, and the standard equilibrium constant is not large: for acetic acid and ethanol near room temperature $K \approx 4$, corresponding to $\Delta_{\mathrm{r}}G^\circ = -RT\ln K \approx -3.4\,\mathrm{kJ\,mol^{-1}}$, and both the enthalpy and entropy of reaction are small. With $K = 4$, when equimolar amounts of acid and alcohol react, the conversion $x$ at equilibrium satisfies

$$
\frac{x^2}{(1-x)^2} = 4, \qquad x = \frac{2}{3};
$$
if ethanol is in tenfold excess, $x^2 / [(1-x)(10-x)] = 4$, and the solution is $x \approx 0.97$. All ways of raising the yield therefore shift the equilibrium (the **equilibrium constant** itself does not change): use a large excess of the cheaper starting material (usually the alcohol), or continuously remove a product, for example by distilling off water as the toluene–water **azeotrope** with a Dean–Stark trap, or by distilling off the ester when it has a low boiling point.

Fischer esterification proceeds by an acid-catalyzed addition–elimination mechanism (in Ingold's notation AAc2: Acid-catalyzed, Acyl–oxygen cleavage, bimolecular). Every step is reversible; read backward, it is the acid-catalyzed hydrolysis of the ester.

![Mechanism of Fischer esterification (AAc2): the top row shows protonation of the carbonyl oxygen and addition of methanol to the activated carbonyl carbon to give the tetrahedral intermediate; the bottom row shows proton transfers that turn a hydroxy group into the good leaving group water, expulsion of water by the remaining hydroxy group to give the protonated ester, and loss of a proton to give methyl acetate](./plots/fischer-esterification.py)

There is experimental evidence for both key conclusions of the mechanism:

1. The bond cleaved is the acyl–oxygen bond, not the alkyl–oxygen bond (the alcohol supplies the alkoxy group, not the hydroxy group). In the esterification of benzoic acid with methanol labeled with $^{18}\mathrm{O}$, the labeled oxygen stays entirely in the ester and the water formed contains no label (Roberts and Urey, 1938).
2. The carbon of the alcohol is not affected. In esterification with an optically active secondary alcohol (such as (R)-butan-2-ol), the configuration of the alcohol part of the ester is retained; on hydrolysis of the ester the alcohol is obtained with unchanged configuration. If the C–O bond of the alcohol were broken (**SN1** or **SN2**), **racemization** or inversion of configuration would occur.

The rate-determining step is the addition of the alcohol to the protonated carbonyl group, and the apparent rate law is $v = k_{\mathrm{obs}}[\ce{RCOOH}][\ce{R'OH}]$, with $k_{\mathrm{obs}}$ proportional to the concentration of the acid catalyst. Acid catalysis lowers the activation energy of the addition step. The more hindered the acid or the alcohol, the more crowded the tetrahedral intermediate and the slower the reaction:

- Acids: $\ce{HCOOH} > \ce{CH3COOH} > \ce{RCH2COOH} > \ce{R2CHCOOH} > \ce{R3CCOOH}$;
- Alcohols: $\ce{CH3OH}$ > primary > secondary; tertiary alcohols readily dehydrate to alkenes or form **carbocations** in acid and are generally not esterified by the Fischer method.

Besides Fischer esterification, other common methods of esterification are the reaction of acyl chlorides or anhydrides with alcohols in the presence of pyridine or DMAP (Section 19.3); SN2 reaction of a carboxylate with an alkyl halide such as iodomethane in DMF (the configuration of the alcohol is not involved); formation of methyl esters from carboxylic acids with **diazomethane** or $\ce{TMSCHN2}$ ([6.5.24](/6.5.24#sec-24.5.2)); the Steglich esterification activated by DCC and DMAP (Section 19.6.1); and the **Mitsunobu reaction** (inversion of configuration at the carbon of the alcohol, Definition 26.6.2).

### 19.4.2. Basic Hydrolysis of Esters: Saponification

**Definition 19.4.2 (Saponification)** The hydrolysis of an ester in aqueous base (NaOH, KOH) to give a carboxylate and an alcohol is called **saponification**, a name derived from the alkaline hydrolysis of fats and oils to make soap:

$$
\ce{RCOOR' + NaOH -> RCOONa + R'OH}.
$$

Saponification follows the BAc2 mechanism (Base-promoted, Acyl–oxygen cleavage, bimolecular) of Section 19.2.1, with rate law $v = k[\ce{RCOOR'}][\ce{HO-}]$. Unlike acid-catalyzed hydrolysis, saponification is irreversible: after the tetrahedral intermediate loses $\ce{R'O-}$, the carboxylic acid formed immediately gives its proton to $\ce{R'O-}$ (the $\mathrm{p}K_{\mathrm{a}}$ of the acid is about 4.8 and that of the alcohol about 16, so the equilibrium constant is about $10^{11}$), and the carboxylate is negatively charged and is no longer attacked by **nucleophiles**. Esters are therefore generally hydrolyzed with base, followed by acidification to obtain the carboxylic acid; more than 1 equivalent of base is needed.

The evidence for BAc2 is the same as for AAc2:

- Isotope labeling: when pentyl acetate is hydrolyzed with base in $\ce{H2^{18}O}$, $^{18}\mathrm{O}$ appears in the acetate and not in the pentanol (Polanyi and Szabo, 1934), showing that the acyl–oxygen bond is cleaved; conversely, when an ordinary ester is hydrolyzed with $\ce{Na^{18}OH}$, the label appears in the carboxylate.
- Stereochemistry: when the alcohol part has a **stereocenter**, the configuration of the alcohol obtained on hydrolysis is retained.
- Bender's $^{18}\mathrm{O}$ exchange experiment proved the existence of the tetrahedral intermediate (Section 19.2.1).

### 19.4.3. The Four Mechanisms of Ester Hydrolysis

Ingold classified the mechanisms of hydrolysis (and formation) of esters by three features: acid catalysis (A) or base promotion (B); cleavage of the acyl–oxygen bond (Ac) or the alkyl–oxygen bond (Al); and a bimolecular (2) or unimolecular (1) rate-determining step. Of the eight combinations, four are common:

| Mechanism | Bond cleaved | Rate-determining step | Esters to which it applies | Evidence or characteristic |
|---|---|---|---|---|
| BAc2 | Acyl–oxygen | Addition of $\ce{HO-}$ to the carbonyl carbon | Almost all esters in base | Retention of configuration of the alcohol; $^{18}\mathrm{O}$ exchange; irreversible |
| AAc2 | Acyl–oxygen | Addition of water to the protonated carbonyl group | Esters of primary and secondary alcohols and ordinary carboxylic acids in dilute acid | Reverse of Fischer esterification; reversible |
| AAc1 | Acyl–oxygen | Loss of the alcohol from the protonated ester to give an acylium ion | Esters that are very hindered on both sides of the carbonyl group (such as 2,4,6-trimethylbenzoates), in concentrated sulfuric acid | The acylium ion is linear, and attack by nucleophiles is not hindered |
| AAl1 | Alkyl–oxygen | Dissociation of the protonated ester to a stable carbocation | tert-Butyl, benzyl, and diphenylmethyl esters, which can give stable carbocations | $^{18}\mathrm{O}$-labeled water enters the alcohol; **chiral** alcohols racemize; the carbocation can eliminate to an alkene |

![Acid-catalyzed cleavage of a tert-butyl ester (AAl1): after protonation, the bond between the ester oxygen and the tert-butyl group undergoes heterolysis, the electron pair stays on oxygen and forms the C=O of the carboxylic acid, giving acetic acid and the tert-butyl cation; the cation loses a proton to give isobutene (or is trapped by water to give tert-butyl alcohol)](./plots/aal1.py)

![The AAc1 mechanism (methyl 2,4,6-trimethylbenzoate in concentrated sulfuric acid): after protonation of the alkoxy oxygen, the carbonyl oxygen lone pair pushes and the C–O electrons leave with methanol, giving a linear acylium ion; water attacks the acyl carbon along its axis, unhindered by the two ortho methyl groups](./plots/aac1.py)

AAc1 and AAl1 are both unimolecular, but they relate differently to SN1 at saturated carbon in [6.5.8](/6.5.8#sec-8.2.3): in AAl1 the bond cleaved is a C–O bond at a saturated carbon, and it really is an SN1 reaction with the carboxylic acid as the **leaving group**; in AAc1 an acylium ion is formed and the reaction center is the carbonyl carbon, so it should not be called an SN1 reaction ([6.5.18](/6.5.18), Question 4).

The AAl1 mechanism is useful in synthesis: tert-butyl esters are very stable toward base and nucleophiles (steric hindrance shields the carbonyl group and BAc2 is very slow), yet cleave rapidly at room temperature in anhydrous trifluoroacetic acid with evolution of isobutene. The tert-butyl ester is therefore a **protecting group** for the carboxyl group, complementary to methyl and ethyl esters, which are hydrolyzed in base (the table of protecting groups in [6.5.20](/6.5.20#sec-20.8.3)). A less common mechanism, BAl2, is SN2 attack of a nucleophile at the alkyl carbon of the ester, for example when a methyl ester is heated with LiI in pyridine, iodide attacks the methyl group to give lithium carboxylate and iodomethane; it is suitable for base-sensitive substrates that cannot be saponified.

![The BAl2 mechanism: iodide attacks the methyl carbon of the methyl ester from the back side (SN2 at the saturated carbon, not attack at the carbonyl group) and the carboxylate leaves, giving the lithium carboxylate and iodomethane](./plots/bal2.py)

## 19.5. Lactones, Transesterification, and Polyesters

### 19.5.1. Lactones

The formation and ring opening of lactones (Definition 18.7.1) follow the same mechanisms as for esters. γ- and δ-Hydroxy acids lactonize spontaneously in acid; lactones open in base to give hydroxy acid salts, which close again on acidification. Intramolecular esterification to macrolactones (rings of twelve members or more) is entropically unfavorable and must be carried out under high dilution with activation methods (such as the Yamaguchi esterification, Section 19.3.3), so that the intramolecular reaction wins over intermolecular polymerization. The syntheses of macrolide antibiotics such as erythromycin and of macrolide musks (such as cyclopentadecanolide) depend on such methods.

### 19.5.2. Transesterification

**Definition 19.5.1 (Transesterification)** The reversible reaction in which an ester and an alcohol exchange alkoxy groups under acid or base catalysis to give another ester and another alcohol is called **transesterification**:

$$
\ce{RCOOR' + R''OH <=>[\ce{H+}\text{ or }\ce{R''O-}] RCOOR'' + R'OH}.
$$

The acid-catalyzed mechanism is the same as AAc2. In base catalysis the **nucleophile** is the alkoxide $\ce{R''O-}$ (BAc2 type, but the irreversible proton-transfer step is absent, so it is still an equilibrium). The two alkoxy groups leave with similar ease and the equilibrium constant is close to 1, so a large excess of alcohol or continuous distillation of the low-boiling alcohol formed is used to drive the reaction. Under base catalysis the alkoxide corresponding to the target ester should be used (such as sodium ethoxide for ethyl esters), otherwise unwanted transesterification occurs.

Applications of transesterification:

- Biodiesel: fats and oils (triglycerides, Section 19.9.2) undergo transesterification with methanol catalyzed by NaOH or $\ce{CH3ONa}$ to give fatty acid methyl esters and glycerol. Fatty acid methyl esters have much lower viscosity and boiling points than the fats and oils and can replace diesel fuel.
- Preparation of esters of higher alcohols from esters of cheap lower alcohols, or the reverse: transesterification of natural waxes (esters of higher fatty acids with higher alcohols, such as triacontyl palmitate $\ce{C15H31COOC30H61}$, the main component of beeswax) with ethanol gives the higher alcohols.
- Ring-opening polymerization of lactones (lactide → polylactic acid, [6.5.18](/6.5.18#sec-18.7.3)) and the production and degradation of polyesters.

### 19.5.3. Polyesters

Condensation (step-growth polymerization) of a dicarboxylic acid (or its dimethyl ester) with a diol gives a polyester. The most important polyester is poly(ethylene terephthalate) (PET), made by direct esterification of terephthalic acid with ethylene glycol, or by transesterification of dimethyl terephthalate with ethylene glycol followed by polycondensation, and used for beverage bottles and polyester fibers:

```smiles
OC(=O)c1ccc(cc1)C(=O)O.OCCO>>O=C(OCCO)c1ccc(cc1)C(=O)OCCO
```

(Only the first step is drawn here: terephthalic acid and two molecules of ethylene glycol give bis(2-hydroxyethyl) terephthalate; at high temperature and reduced pressure this undergoes continuing transesterification with distillation of ethylene glycol to give high-molar-mass PET.) Unlike the **addition polymerization** of [6.5.11](/6.5.11#sec-11.11), every step of a polycondensation releases a small molecule, the molar mass grows slowly with conversion, and a high polymer is obtained only when the conversion approaches 100%, so the purity of the monomers and an equimolar ratio are very important ([6.3.21](/6.3.21)).

The ester bonds of PET hydrolyze extremely slowly at ordinary temperature, and discarded PET can persist in the environment for hundreds of years. Chemical recycling uses transesterification (heating with ethylene glycol or methanol, "alcoholysis") or hydrolysis to return to the monomers. In 2016 Yoshida and coworkers isolated from soil at a recycling plant a bacterium, *Ideonella sakaiensis* 201-F6, which secretes a PET hydrolase (PETase) that hydrolyzes the surface of PET to mono(2-hydroxyethyl) terephthalate; a second enzyme then hydrolyzes this to terephthalic acid and ethylene glycol, and the bacterium grows on them as carbon source. PETase is a serine hydrolase and has the same mechanism as the proteases of Section 19.6 below: the serine hydroxy group in the active site attacks the ester carbonyl group to give an acyl–enzyme intermediate, which is then hydrolyzed. Thermostable mutants subsequently obtained by protein engineering (such as LCC-ICCG in 2020 and FAST-PETase in 2022) can depolymerize most of a sample of PET within hours to days, and enzymatic recycling has reached the demonstration-plant stage.

## 19.6. Formation and Hydrolysis of Amides

### 19.6.1. Formation of Amides

Amides can be obtained from acyl chlorides and anhydrides with ammonia or amines (Section 19.3), and also by ammonolysis of esters (much milder than with acyl chlorides, requiring heating or a long reaction time, for example a methyl ester with ammonia in methanol):

```smiles
CC(=O)OCC.N>>CC(N)=O.CCO
```

When a carboxylic acid and an amine are mixed, the first reaction is a rapid acid–base reaction that gives the ammonium carboxylate; the carboxylate in the salt is only weakly electrophilic and the amine is protonated and has lost its **nucleophilicity**, so the amide forms only on dehydration at high temperature (about 180–200 °C). This is how nylon-66 is made industrially: adipic acid and hexane-1,6-diamine first form a salt ("nylon salt", easily purified and guaranteeing a 1:1 ratio), which is then heated to lose water and polycondense.

To form an amide directly from a carboxylic acid and an amine under mild conditions, a coupling agent is used to activate the carboxylic acid in situ. The classic coupling agent is dicyclohexylcarbodiimide (DCC, Sheehan and Hess, 1955): the carboxylic acid first gives its proton to one nitrogen of the carbodiimide, and the carboxylate adds to the central carbon to give an O-acylisourea. The O-acylisourea is an activated ester whose leaving group becomes the very stable dicyclohexylurea (DCU, insoluble in most organic solvents and removed by filtration) on departure, so that an amine can attack its carbonyl group at room temperature to give the amide.

![Amide formation by the carbodiimide method (drawn for brevity as the isopropyl-substituted DIC; DCC carries cyclohexyl groups): the carboxylate adds to the central carbon of the protonated carbodiimide to give an O-acylisourea; methylamine adds to the acyl carbon, and addition–elimination with proton transfers gives N-methylacetamide and the urea](./plots/dcc-coupling.py)

The O-acylisourea also undergoes side reactions: it can rearrange by an intramolecular O→N acyl shift to a stable, unreactive N-acylurea; in peptide synthesis the activated amino acid can also undergo **racemization** through an oxazolone intermediate. Additives such as 1-hydroxybenzotriazole (HOBt), which rapidly convert the O-acylisourea into an active ester, suppress both side reactions; uronium and phosphonium coupling agents such as HATU are based on the same idea. Peptide coupling and solid-phase synthesis are in [6.5.33](/6.5.33). DCC together with a catalytic amount of DMAP is also used to form esters from carboxylic acids and alcohols (the Steglich esterification, 1978), which is suitable for acid-sensitive substrates and hindered alcohols.

Polyamides are another important class of condensation polymers. Nylon-66 (Carothers, DuPont, 1935) is obtained by polycondensation of adipic acid and hexane-1,6-diamine, and nylon-6 by ring-opening polymerization of caprolactam ([6.5.25](/6.5.25#sec-25.9.2)). In the laboratory, a solution of adipoyl chloride in an organic solvent is carefully layered on an alkaline aqueous solution of hexane-1,6-diamine, a nylon film forms immediately at the interface, and a thin filament can be pulled out continuously (the "nylon rope" experiment). The rigid chains of the aromatic polyamide Kevlar (poly(p-phenylene terephthalamide), Kwolek, 1965) line up in sheets through interchain N–H⋯O=C **hydrogen bonds**; its specific strength is about five times that of steel, and it is used in body armor and composites:

```smiles
O=C(Cl)c1ccc(cc1)C(=O)Cl.Nc1ccc(N)cc1>>O=C(Nc1ccc(N)cc1)c1ccc(cc1)C(=O)Cl
```

(Again only the first amide bond is drawn.)

### 19.6.2. Hydrolysis of Amides

Amides are the most stable carboxylic acid derivatives, and their hydrolysis requires strong acid or strong base and prolonged heating. The half-life of the hydrolysis of a peptide bond in neutral water at room temperature is measured in years to hundreds of years (different estimates give about 7 years to about 500 years); this kinetic stability is a precondition for proteins to serve as structural materials and carriers of information, and organisms speed up hydrolysis by more than $10^{10}$ with proteases (**enzyme catalysis**, [6.5.33](/6.5.33)).

Acidic hydrolysis. The amide is protonated on oxygen (the conjugate acid of the O-protonated amide has a $\mathrm{p}K_{\mathrm{a}}$ of about $-0.5$, [Table 3.1 in 6.5.3](/6.5.3#sec-3.1.4); the lone pair of N is conjugated with the carbonyl group and protonation on N is unfavorable), and water adds to the activated carbonyl carbon; in the tetrahedral intermediate a proton transfers to nitrogen, and $\ce{-NH3+}$ becomes a good leaving group. The ammonia that leaves is immediately protonated to ammonium ion ($\mathrm{p}K_{\mathrm{a}}$ 9.25) and can no longer attack the carboxylic acid, so acidic hydrolysis is irreversible and requires at least 1 equivalent of acid.

![Acidic hydrolysis of an amide: water attacks O-protonated acetamide to give the tetrahedral intermediate, and a proton transfers to nitrogen; the hydroxy group pushes out NH₃ to give protonated acetic acid; ammonia is protonated to ammonium ion, which makes the reaction irreversible](./plots/amide-hydrolysis.py)

Basic hydrolysis. $\ce{HO-}$ adds to the carbonyl carbon, but $\ce{NH2-}$ (the $\mathrm{p}K_{\mathrm{a}}$ of $\ce{NH3}$ is about 38) is an extremely poor leaving group, and the tetrahedral intermediate prefers to lose $\ce{HO-}$ and return to the starting material. Only in concentrated base, when the other O–H of the tetrahedral intermediate is also deprotonated to give a dianion, is the push strong enough to expel the amide anion (which is protonated by water at once); the carboxylate and ammonia at the end no longer react, so basic hydrolysis is also irreversible.

```smiles
CC(N)=O.O>>CC(=O)O.[NH4+]
CC(N)=O.[OH-]>>CC(=O)[O-].N
```

![Basic hydrolysis of an amide: the tetrahedral intermediate formed by addition of $\ce{HO-}$ prefers to lose $\ce{HO-}$ again (reversibly); after a second deprotonation the dianion pushes hard enough, an oxide forming the C=O bond while the C–N electrons leave with $\ce{NH2-}$, which water protonates at once](./plots/amide-base-hydrolysis.py)

## 19.7. Reduction of Derivatives

The reactions of hydride reagents ([6.5.17](/6.5.17#sec-17.1.1)) with carboxylic acid derivatives follow a single pattern: hydride adds to the carbonyl carbon to give a tetrahedral intermediate; the intermediate loses the **leaving group** to give an aldehyde; the aldehyde is more reactive than the original derivative (except for acyl chlorides) and is reduced at once by a second hydride, finally giving an alcohol. To stop at the aldehyde stage, a less reactive, more hindered hydride reagent must be used, or the tetrahedral intermediate must be made sufficiently stable at low temperature that it does not break down in the presence of hydride.

| Derivative | Reagent and product | Remark |
|---|---|---|
| Acyl chlorides | $\ce{LiAlH4}$ or $\ce{NaBH4}$ → primary alcohol | The most reactive; both reagents reduce them |
| Acyl chlorides | $\ce{LiAl(OtBu)3H}$, $-78$ °C → aldehyde | The three tert-butoxy groups lower the reactivity of the hydride so that only the most reactive acyl chloride is reduced; Rosenmund catalytic hydrogenation ($\ce{H2}$, $\ce{Pd/BaSO4}$) can also be used |
| Anhydrides | $\ce{LiAlH4}$ → two molecules of primary alcohol; cyclic anhydrides with $\ce{NaBH4}$ → lactone | Cyclic anhydrides are reactive; $\ce{NaBH4}$ first reduces them to a hydroxycarboxylate, which closes on acidification |
| Esters | $\ce{LiAlH4}$ → two alcohols ($\ce{RCH2OH + R'OH}$) | $\ce{NaBH4}$ does not normally reduce esters; $\ce{LiBH4}$ does |
| Esters | DIBAL-H, $-78$ °C → aldehyde | At low temperature the aluminum **hemiacetal** intermediate is stable |
| Amides | $\ce{LiAlH4}$ → amine (C=O becomes $\ce{CH2}$) | Through an iminium ion, not an aldehyde |
| Amides | DIBAL-H, or Weinreb amide with $\ce{LiAlH4}$ → aldehyde | The stable tetrahedral intermediate breaks down on workup |
| Carboxylic acids | $\ce{LiAlH4}$ or $\ce{BH3}$ → primary alcohol | [6.5.18](/6.5.18#sec-18.3) |
| Nitriles | $\ce{LiAlH4}$ → primary amine; DIBAL-H → aldehyde | [6.5.20](/6.5.20#sec-20.4.3) |

```smiles
CCCC(=O)OCC>>CCCCO.CCO
CCCC(=O)OCC>>CCCC=O.CCO
```

![Reduction of ethyl propanoate by $\ce{LiAlH4}$: a hydride adds to the carbonyl carbon, and collapse of the tetrahedral intermediate with loss of ethoxide gives the aldehyde; being more reactive than the ester, the aldehyde takes a second hydride at once, and workup gives propan-1-ol (Al omitted from the alkoxides)](./plots/lialh4-ester.py)

These are the reductions of ethyl butanoate with $\ce{LiAlH4}$ and with DIBAL-H ($-78$ °C), respectively. DIBAL-H (diisobutylaluminum hydride) is a Lewis acidic, neutral hydride reagent: aluminum first coordinates to the carbonyl oxygen of the ester and then transfers hydride to the carbonyl carbon, and the aluminum hemiacetal formed does not lose the alkoxy group at $-78$ °C, so no aldehyde is present in the reaction mixture; on addition of water the hemiacetal breaks down to the aldehyde. At higher temperature or with excess reagent the alcohol is obtained, and the selectivity of DIBAL-H depends mainly on control of temperature and stoichiometry.

![Partial reduction of an ester to an aldehyde by DIBAL-H: aluminum coordinates to the carbonyl oxygen and hydride is transferred to the carbonyl carbon; the aluminum hemiacetal formed is stable at −78 °C; on acidic aqueous workup the hemiacetal breaks down to give propanal](./plots/dibal-ester.py)

Amides are reduced by $\ce{LiAlH4}$ to amines rather than alcohols, which is the most important difference from esters. In the tetrahedral intermediate there are two lone-pair donors that could push out a leaving group: the oxygen bound to aluminum and the nitrogen. Nitrogen is the stronger electron donor and pushes out the $\ce{O-Al}$ group, forming an iminium ion (rather than an aldehyde); the iminium ion then accepts a hydride to give the amine. Primary, secondary, and tertiary amides give primary, secondary, and tertiary amines, respectively, an important method for preparing amines ([6.5.23](/6.5.23#sec-23.5.5)). Lactams give cyclic amines on reduction.

![Reduction of an amide with LiAlH₄: hydride adds to the carbonyl carbon of N,N-dimethylacetamide; in the tetrahedral intermediate the lone pair of nitrogen pushes out the oxygen bound to aluminum to give an iminium ion; a second hydride adds to give N,N-dimethylethylamine](./plots/lialh4-amide.py)

N-Methoxy-N-methylamides (Weinreb amides, Nahm and Weinreb, 1981) are a useful variant: after addition of a hydride reagent or organometallic reagent, the methoxy oxygen chelates the metal, the five-membered-ring tetrahedral intermediate is stable under the reaction conditions and breaks down to the aldehyde or ketone only on workup, so no second addition occurs.

![Weinreb ketone synthesis: methylmagnesium bromide adds to the carbonyl carbon of N-methoxy-N-methylbenzamide; in the tetrahedral intermediate magnesium is chelated by the alkoxide and the methoxy oxygen (dashed), and the five-membered ring does not collapse under the reaction conditions, so no second addition occurs; aqueous acidic workup gives acetophenone](./plots/weinreb.py)

## 19.8. Derivatives and Organometallic Reagents

The reactions of organometallic reagents with derivatives follow the same pattern as those of hydride (addition–elimination–addition), the difference being that the intermediate product is a ketone rather than an aldehyde:

- An ester reacts with 2 equivalents of **Grignard reagent** or **organolithium reagent** to give a tertiary alcohol with two identical hydrocarbyl groups; formate esters give secondary alcohols. After the first addition the tetrahedral intermediate loses the alkoxy group to give a ketone, the ketone is more reactive than the ester and is attacked at once by the second equivalent of reagent, and even 1 equivalent of reagent does not give the ketone but a mixture of the tertiary alcohol and unreacted ester. Acyl chlorides and anhydrides behave in the same way with Grignard reagents.
- Acyl chlorides react with **lithium dialkylcuprates** (Gilman reagents, Definition 10.4.2) and stop at the ketone: copper reagents are softer, with lower **nucleophilicity**, and can substitute the most reactive acyl chlorides without adding to the ketone formed.
- A Weinreb amide gives a ketone with 1 equivalent of Grignard reagent (Section 19.7).
- A nitrile and a Grignard reagent give an imine salt, which is hydrolyzed to a ketone on workup ([6.5.20](/6.5.20#sec-20.4.3)).
- A carboxylic acid and 2 equivalents of organolithium reagent give a ketone ([6.5.18](/6.5.18#sec-18.6)).

![Reaction of an ester with two equivalents of Grignard reagent: the C–Mg bond adds to the carbonyl carbon of methyl acetate, the tetrahedral intermediate loses methoxide to give acetone; acetone is attacked at once by a second equivalent of methylmagnesium bromide, and acidic workup gives tert-butyl alcohol](./plots/ester-grignard.py)

```smiles
CC(=O)OC>>CC(C)(c1ccccc1)c1ccccc1
CCCC(=O)Cl>>CCCC(C)=O
```

The first is the reaction of methyl acetate with 2 equivalents of phenylmagnesium bromide to give 1,1-diphenylethanol, and the second that of butanoyl chloride with lithium dimethylcuprate to give pentan-2-one.

## 19.9. Acyl Transfer in Biology

Acyl transfer in living organisms takes place in neutral water at 37 °C. Under these conditions carboxylic acids exist as carboxylates ([6.5.18](/6.5.18#sec-18.2.5)) and cannot be attacked by **nucleophiles** at all; esters and amides are too stable; and acyl chlorides and anhydrides would be hydrolyzed at once. The solution of biology is to activate carboxylic acids as two kinds of "moderately reactive" acyl donors: acyl phosphates (such as the acyl adenylates formed with the participation of ATP) and thioesters.

### 19.9.1. Thioesters and Coenzyme A

**Definition 19.9.1 (Thioester)** A compound $\ce{RC(=O)SR'}$ formed by dehydration of a carboxylic acid and a thiol is called a **thioester**.

The carbonyl group of a thioester lies between that of an anhydride and that of an ester. The 3p lone pair of sulfur overlaps poorly with the 2p orbital of the carbonyl carbon, so the conjugative stabilization is much weaker than that of oxygen in an ester (similar to chlorine in an acyl chloride) and the carbonyl group is more electrophilic; the thiolate ion ($\mathrm{p}K_{\mathrm{a}}$ of $\ce{CH3SH}$ 10.3) is also a much better **leaving group** than an alkoxide (about 16). Thioesters are therefore readily attacked by amines, alcohols, and other thiols, yet are stable enough in neutral water to exist and be transported in cells. The α-H of a thioester is also more acidic than that of an ester (conjugation of the thioester carbonyl group with the α **carbanion** is not "shared" by sulfur), and **enolates** form readily, which is the basis of the **Claisen condensation** in biology ([6.5.22](/6.5.22#sec-22.10.2)).

The most important thioester in biology is acetyl coenzyme A (acetyl-CoA): coenzyme A is a long-chain thiol (the terminal SH comes from cysteamine) to which the acetyl group is attached as a thioester. The standard biochemical Gibbs energy of hydrolysis of acetyl-CoA is about $-31.5\,\mathrm{kJ\,mol^{-1}}$, comparable to $-30.5\,\mathrm{kJ\,mol^{-1}}$ for the hydrolysis of ATP to ADP, and it counts as a "high-energy" compound. It transfers the acetyl group to amines (the synthesis of acetylcholine, the acetylation of histones), to the **enol** of oxaloacetate (the first step of the citric acid cycle, formally an aldol-type addition), or to another acetyl-CoA (the Claisen condensation in fatty acid and cholesterol synthesis). β-Oxidation of fatty acids cuts off two carbons at a time, and the product is also acetyl-CoA ([7.1](/7.1)).

Acyl exchange between a thioester and a thiol (thioester exchange) is fast in neutral water, which is the key to "native chemical ligation" in the chemical synthesis of proteins: the C-terminal thioester of one peptide first undergoes thioester exchange with the N-terminal cysteine of another peptide, and an S→N acyl shift through a five-membered ring **transition state** then gives the native peptide bond ([6.5.33](/6.5.33)).

![The S-to-N acyl shift of native chemical ligation: after thiol exchange, the C-terminal acyl group of peptide 1 sits on the side-chain sulfur of the N-terminal cysteine of peptide 2; the free amino group adds to the thioester carbonyl through a five-membered ring, and collapse of the tetrahedral intermediate with loss of the thiolate gives a native peptide bond](./plots/native-chemical-ligation.py)

### 19.9.2. Triglycerides and Saponification

**Definition 19.9.2 (Triglyceride)** The triester formed by esterification of all three hydroxy groups of glycerol (propane-1,2,3-triol) with fatty acids is called a **triglyceride** (triacylglycerol), the main component of animal and plant fats and oils.

The fatty acids in natural fats and oils are almost all straight-chain carboxylic acids with an even number of carbons (synthesized two carbons at a time from acetyl-CoA, [6.5.22](/6.5.22#sec-22.10.2)); common ones are:

| Fatty acid | Carbons:double bonds | Position of double bonds | Melting point / °C |
|---|---|---|---|
| Palmitic acid (hexadecanoic acid) | 16:0 | — | 63 |
| Stearic acid (octadecanoic acid) | 18:0 | — | 69 |
| Oleic acid | 18:1 | 9Z | 13 |
| Linoleic acid | 18:2 | 9Z,12Z | $-5$ |
| α-Linolenic acid | 18:3 | 9Z,12Z,15Z | $-11$ |

The straight chains of saturated fatty acids pack tightly, and triglycerides rich in saturated fatty acids (animal fats) are solid at room temperature and are called fats; cis double bonds bend the chain, and plant oils rich in unsaturated fatty acids are liquid and are called oils. Catalytic hydrogenation of oils ("hardening") gives solid margarine, but during partial hydrogenation double bonds isomerize to trans, producing trans fats that are harmful to the cardiovascular system, whose use is now restricted in many countries.

Alkaline hydrolysis of fats and oils is saponification (Definition 19.4.2): each molecule of triglyceride consumes 3 molecules of NaOH and gives glycerol and 3 molecules of sodium fatty acid salt, which is soap (a **surfactant**, [6.5.18](/6.5.18#sec-18.2.5)):

```smiles
CCCCCCCCCCCCCCCCCC(=O)OCC(COC(=O)CCCCCCCCCCCCCCCCC)OC(=O)CCCCCCCCCCCCCCCCC>>OCC(O)CO.CCCCCCCCCCCCCCCCCC(=O)[O-]
```

(Saponification of glyceryl tristearate to glycerol and stearate.) The number of milligrams of KOH required to saponify 1 g of fat or oil is called the saponification value, and it is inversely proportional to the average molar mass of the fat or oil: for glyceryl tristearate ($M = 891.5\,\mathrm{g\,mol^{-1}}$) the saponification value is $3 \times 56.11 \times 1000 / 891.5 \approx 189$. In living organisms triglycerides are hydrolyzed by lipases; lipases are also serine hydrolases, act at the oil–water interface, and often need bile salts to emulsify the fat into small droplets ([6.3.21](/6.3.21)).

### 19.9.3. Phospholipids

Phospholipids are the main component of cell membranes. The most common glycerophospholipids have glycerol 3-phosphate as the backbone: the hydroxy groups at C1 and C2 are esterified with fatty acids (usually an unsaturated fatty acid at C2), and the phosphate at C3 is esterified in turn with an alcohol (choline, ethanolamine, serine, inositol) to form a phosphodiester. An example is phosphatidylcholine (lecithin):

```smiles
CCCCCCCCCCCCCCCC(=O)OC[C@H](COP(=O)([O-])OCC[N+](C)(C)C)OC(=O)CCCCCCC/C=C\CCCCCCCC
```

(1-Palmitoyl-2-oleoyl-sn-glycero-3-phosphocholine; the configuration at C2 is R.) A phospholipid molecule has two hydrophobic fatty acid chains and a charged polar head (the phosphate is negatively charged and the quaternary ammonium of choline positively charged, [6.5.23](/6.5.23#sec-23.7.3)), and is an **amphiphile**. Unlike soap, which has only one chain, a two-chain phospholipid has a nearly cylindrical cross-section and does not form **micelles** in water but assembles spontaneously into bilayers, which close into vesicles (liposomes); this is the basic structure of biological membranes.

The carboxylic ester bonds of phospholipids can be hydrolyzed by phospholipases: phospholipase $\mathrm{A_2}$ selectively hydrolyzes the ester bond at C2, releasing unsaturated fatty acids such as arachidonic acid, which is converted by cyclooxygenase into prostaglandins, the very pathway that aspirin inhibits ([6.5.18](/6.5.18#sec-18.7.4)). Phospholipase $\mathrm{A_2}$ in snake and bee venoms destroys cell membranes and is one source of their toxicity. The metabolism and transport of phospholipids, triglycerides, and cholesterol in the body are discussed in [7.1](/7.1); from the chemical point of view, all the "linkages" in these molecules are ester bonds (carboxylic esters and phosphate esters), and their formation and cleavage are all nucleophilic acyl (or phosphoryl) substitutions.

## Summary

| Topic | Key points |
|---|---|
| Mechanism (Definitions 19.2.1, 19.2.2) | Addition–elimination: Nu adds to give the tetrahedral intermediate (often the **rate-determining step**), then the **leaving group** is eliminated; Bender's $^{18}\mathrm{O}$ exchange proves the intermediate |
| Reactivity | Acyl chlorides > anhydrides > esters > amides (hydrolysis $10^{11} : 10^7 : 1 : <10^{-2}$); governed by the conjugative electron donation of L and the basicity of the leaving group (not the **electronegativity**); conversion from more reactive to less reactive derivatives |
| Catalysis | Acid: protonates the carbonyl oxygen and improves the leaving group; base: generates a strong **nucleophile** (consumed in saponification); DMAP: nucleophilic catalysis through the N-acylpyridinium ion |
| Acyl chlorides, anhydrides | $\ce{SOCl2}$ (gaseous by-products) and $\ce{(COCl)2}$/DMF give acyl chlorides; reactions with water, alcohols, and amines need base; cyclic anhydrides open to mono-derivatized diacids |
| Esterification and hydrolysis | Fischer esterification (Definition 19.4.1) is reversible, $K \approx 4$, driven by excess or removal of water; saponification (Definition 19.4.2) is irreversible; four mechanisms BAc2, AAc2, AAc1 (hindered, acylium ion), AAl1 (tert-butyl esters, alkyl–oxygen cleavage, removal with TFA) |
| Lactones, transesterification, polyesters | Transesterification (Definition 19.5.1) is reversible: biodiesel, production and alcoholysis of PET; PETase is a serine hydrolase |
| Amides | Carboxylic acid + amine first gives a salt, and high temperature or DCC activation is needed (O-acylisourea, HOBt suppresses side reactions); hydrolysis needs strong acid or strong base and is irreversible under both; nylon, Kevlar |
| Reduction | $\ce{LiAlH4}$: esters, acyl chlorides, anhydrides → alcohols, amides → amines (through iminium ions); $\ce{LiAl(OtBu)3H}$: acyl chlorides → aldehydes; DIBAL-H ($-78$ °C): esters → aldehydes |
| Organometallics | RMgX and RLi add twice to esters to give tertiary alcohols; $\ce{R2CuLi}$ with acyl chlorides and RMgX with Weinreb amides or nitriles give ketones |
| Biology | Thioesters (Definition 19.9.1): weak conjugation and a good leaving group make them activated acyl donors, acetyl-CoA; triglycerides (Definition 19.9.2) and saponification, the saponification value; the bilayer of phospholipids |

## Questions

1. Which carbonyl carbon is the most electrophilic and which the least in the following compounds? Arrange them by rate of hydrolysis and explain: phenyl acetate, ethyl acetate, acetyl chloride, acetamide, acetic anhydride, 2,2,2-trifluoroethyl acetate.

   **Answer** Acetyl chloride > acetic anhydride > phenyl acetate > 2,2,2-trifluoroethyl acetate > ethyl acetate > acetamide. In an acyl chloride the conjugative electron donation of chlorine is the weakest and $\ce{Cl-}$ is the best **leaving group**; the bridging oxygen of an anhydride is conjugated with two carbonyl groups at once, and the leaving group is a carboxylate (4.76). Among the three esters, the basicities of the leaving groups increase in the order phenoxide (phenol 9.99) < trifluoroethoxide (12.4) < ethoxide (15.9), and the lone pair of the phenoxy oxygen is partly delocalized into the benzene ring and conjugates less with the carbonyl group; phenyl acetate is therefore the most reactive (which is also why aspirin can acylate proteins). In an amide the conjugation of nitrogen is the strongest and the leaving group is the worst, so it is the least reactive.

2. Aqueous $\ce{Na^{18}OH}$ is used to hydrolyze ethyl acetate. In which product does $^{18}\mathrm{O}$ appear? If unhydrolyzed ethyl acetate is recovered part way through the reaction, does it contain $^{18}\mathrm{O}$? What about the hydrolysis of tert-butyl acetate in dilute sulfuric acid–$\ce{H2^{18}O}$?

   **Answer** The BAc2 mechanism cleaves the acyl–oxygen bond; $^{18}\mathrm{OH^-}$ adds to the carbonyl carbon and the label stays in the acetate, while the ethanol contains no label. The recovered ester contains a little $^{18}\mathrm{O}$ (carbonyl oxygen): the two oxygens of the tetrahedral intermediate become equivalent by proton transfer, and when the intermediate loses ordinary $\ce{HO-}$ and returns to the starting material it carries the label into the carbonyl group of the ester (Bender's experiment). tert-Butyl acetate in acid cleaves the alkyl–oxygen bond by the AAl1 mechanism to give the tert-butyl cation, which is captured by $\ce{H2^{18}O}$, so the label appears in the tert-butyl alcohol and the acetic acid contains no label (part of the cation also eliminates to isobutene).

3. Give the reagents for the following conversions and explain why they cannot be done in one step: (a) acetamide → ethyl acetate; (b) benzoic acid → benzaldehyde; (c) ethyl acetate → butan-2-one.

   **Answer** (a) An amide is more stable than an ester and cannot be alcoholyzed directly to the ester; hydrolyze it with acid or base to acetic acid and then carry out Fischer esterification (excess ethanol, concentrated sulfuric acid catalyst), or first convert the acid into acetyl chloride and treat it with ethanol. (b) Reduction with $\ce{LiAlH4}$ goes past the aldehyde directly to the alcohol; first convert the acid into benzoyl chloride with $\ce{SOCl2}$ and then reduce with $\ce{LiAl(OtBu)3H}$ at $-78$ °C (or Rosenmund hydrogenation); alternatively reduce to benzyl alcohol first and then oxidize with a mild oxidant such as PCC ([6.5.10](/6.5.10#sec-10.6.2)). (c) Ethylmagnesium bromide adds twice to the ester to give a tertiary alcohol (3-methylpentan-3-ol); instead, hydrolyze the ester to acetic acid, convert it to acetyl chloride, and treat it with lithium diethylcuprate to give butan-2-one; or convert the ester into the Weinreb amide and treat it with 1 equivalent of ethylmagnesium bromide.

4. What is obtained from 1 equivalent of methanol and succinic anhydride? Compared with the direct reaction of succinic acid with 1 equivalent of methanol and sulfuric acid, which method gives the purer monomethyl ester?

   **Answer** Methanol attacks one carbonyl group of the cyclic anhydride and opens the ring to give monomethyl succinate $\ce{HOOCCH2CH2COOCH3}$; the other end is now a free carboxylic acid, which does not react further with methanol in the absence of acid catalysis, so the product is a single compound. In direct Fischer esterification the two carboxyl groups have the same reactivity, and statistically a mixture of diacid, monoester, and diester is obtained (and the equilibrium has to be driven by excess alcohol), so the monoester is impure.

5. Draw the mechanism of the following reaction: (R)-butan-2-ol and acetic anhydride in pyridine; what is the configuration of the sec-butyl acetate obtained? What if (R)-2-bromobutane and sodium acetate in DMF are used instead?

   **Answer** In the first reaction the oxygen of the alcohol adds as a **nucleophile** to the carbonyl carbon of the anhydride (pyridine as base, or nucleophilic catalysis through the N-acetylpyridinium ion), and the tetrahedral intermediate loses acetate and then a proton; the C–O bond of the alcohol is not broken, so the product is (R)-butan-2-yl acetate with retention of configuration. In the second reaction acetate attacks the saturated carbon by **SN2** substitution with inversion of configuration to give (S)-butan-2-yl acetate (the CIP order is the same in both: OAc and Br are both first). The two methods give opposite configurations, which is the stereochemical basis for using esterification and SN2 to distinguish "acyl–oxygen cleavage" from "alkyl–oxygen cleavage".

6. What is obtained from ethyl formate with excess phenylmagnesium bromide followed by acidification? Can ethyl acetate with 1 equivalent of phenylmagnesium bromide give acetophenone?

   **Answer** After the first addition ethyl formate loses ethoxide to give benzaldehyde, which is attacked by a second equivalent of PhMgBr to give diphenylmethanol $\ce{Ph2CHOH}$ (a secondary alcohol). Ethyl acetate with 1 equivalent of PhMgBr cannot give acetophenone: the acetophenone formed is more reactive than the ester and reacts with the remaining **Grignard reagent** as soon as it forms, so the product is a mixture of 1,1-diphenylethanol and unreacted ethyl acetate. To obtain acetophenone, use acetyl chloride with lithium diphenylcuprate, the Weinreb amide of acetic acid with PhMgBr, or acetonitrile with PhMgBr (hydrolysis of the imine salt).

7. Compound 1 (7-methoxymethylnorborn-5-en-2-one) is converted in two steps into 3 (a cis-substituted cyclopentene bearing a $\ce{CH2COOH}$, a hydroxy group, and a $\ce{CH2OCH3}$). Deduce the structure of the intermediate 2 and give the conditions of the two steps.

   **Answer** This is the beginning of Corey's synthesis of prostaglandins. The first step is a **Baeyer–Villiger oxidation** (for example, m-chloroperoxybenzoic acid and $\ce{NaHCO3}$, Definition 17.5.1): the bridgehead carbon (a tertiary carbon) of the bridged ketone, which has the larger **migratory aptitude**, migrates to oxygen with retention of configuration and the ring expands by one atom, giving the bicyclic lactone 2 (a 2-oxabicyclo[3.2.1]oct-6-en-3-one skeleton bearing $\ce{CH2OCH3}$ at position 8). The second step is saponification of the lactone followed by acidification (aqueous NaOH, then careful acidification), which opens the ring to give the hydroxy acid 3: the $\ce{CH2}$ that was attached to the carbonyl group becomes $\ce{CH2COOH}$, and the migrating bridgehead carbon becomes the carbon bearing the hydroxy group. Neither the Baeyer–Villiger migration nor ester hydrolysis (BAc2) changes the configuration of the ring carbons, so the relative configuration on the ring of 1 is transferred intact to the cyclopentene ring of 3.

8. Why do organisms use acetyl coenzyme A (a thioester) rather than ethyl acetate as the donor of the acetyl group? Why not acetic anhydride?

   **Answer** The carbonyl group of ethyl acetate is effectively stabilized by conjugation with the lone pair on oxygen, and ethoxide is a poor leaving group, so in neutral water without strong acid or base it can hardly transfer the acetyl group to an amine or alcohol. Acetic anhydride is reactive, but it hydrolyzes rapidly in water, cannot be stored and transported in the cell, and lacks selectivity. The reactivity of a thioester lies between the two: the 3p lone pair of sulfur is weakly conjugated with the carbonyl group and the thiolate is a good leaving group, so acyl transfer is thermodynamically favorable (hydrolysis $\Delta G^{\circ\prime} \approx -31.5\,\mathrm{kJ\,mol^{-1}}$), while the thioester is kinetically stable enough in neutral water that it reacts quickly only under enzyme catalysis. In addition, the large "handle" of coenzyme A allows enzymes to recognize and bind it.
