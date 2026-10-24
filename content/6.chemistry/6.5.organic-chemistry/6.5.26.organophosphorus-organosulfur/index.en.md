---
title: Organophosphorus and Organosulfur Compounds
description: The concept of organoelement compounds; classification, nomenclature and P(III)/P(V) tautomerism of organophosphorus compounds, bonding at phosphorus (the ionic–negative hyperconjugation description of P=O) and its configuration, phosphate esters in living systems; basicity, nucleophilicity, coordination and reducing power of phosphines, the Staudinger reduction, the Arbuzov, Mitsunobu and Appel reactions and alkene inversion; classification and bonding of organosulfur compounds, acidity and nucleophilicity of thiols, disulfide bonds and glutathione, sulfonium salts, sulfoxides and the Swern oxidation, sulfonic acids, sulfonyl chlorides and sulfa drugs, sulfur-stabilized carbanions, sulfur ylides and the Julia olefination.
source_hash: 17bda4214c54
---

So far the heteroatoms in organic molecules have been mainly O, N and the halogens. This chapter and the next, [6.5.27](/6.5.27), deal with compounds in which carbon is bonded directly to other elements of the periodic table. Their bonding differs markedly from that of second-period elements (the atoms are large and of low **electronegativity**, their π bonds to carbon are weak, and they can carry more than four ligands), and each brings its own set of irreplaceable reagents. This chapter treats phosphorus and sulfur, from Groups 15 and 16. Both are essential to life: the backbone of nucleic acids and ATP are phosphate esters, protein structure and redox balance depend on the thiol groups and disulfide bonds of cysteine, and acetyl groups are transferred in metabolism as thioesters (coenzyme A). In synthesis they provide a family of reactions driven by the formation of the P=O bond (Wittig, Arbuzov, Mitsunobu, Appel, Staudinger) and sulfur-containing groups that stabilize an adjacent **carbanion**.

This chapter uses the **SN2 reaction** and the **leaving group** of [6.5.8](/6.5.8), the unified $\mathrm{p}K_{\mathrm{a}}$ table of [6.5.3](/6.5.3#sec-3.1.4), and the inorganic chemistry of phosphorus and sulfur in [6.1.3](/6.1.3) and [6.1.14](/6.1.14). The **Wittig reaction**, the **HWE reaction**, sulfur ylides and the **umpolung** of 1,3-dithianes were already discussed in [6.5.16](/6.5.16); here we only review them and add the phosphorus and sulfur chemistry behind them. The role of phosphine ligands in transition-metal catalysis is treated in [6.5.28](/6.5.28#sec-28.3.3) and [6.5.29](/6.5.29), and nucleotides and the synthesis of nucleic acids by the **phosphoramidite method** in [6.5.33](/6.5.33#sec-33.9.4).

## 26.1. Organoelement Compounds

Organic compounds all contain carbon, usually together with H, O and N, and sometimes halogens. Other elements are often called heteroelements.

**Definition 26.1.1 (Organoelement Compound)** A compound containing a bond between carbon and a heteroelement X (a C–X bond) is called an **organoelement compound**. If X is a metal, the compound is an organometallic compound ([6.5.28](/6.5.28#sec-28.1)); if X is a nonmetal (B, Si, P, S, Se, and so on), it is a nonmetal organoelement compound. In the narrow sense, "organoelement compound" refers only to the latter class.

By convention, compounds in which phosphorus is linked to carbon indirectly through O, S or N (phosphate esters, phosphorothioates, phosphoramides) are also counted as organophosphorus compounds, whereas thiols and sulfides are generally just regarded as organic compounds. This chapter treats P and S; B, Si, F, I and the main-group metals Li and Mg are taken up in [6.5.27](/6.5.27).

Compared with the second-period elements C, N and O, the elements of the third period and below share several features that determine most of the chemistry of this chapter and the next:

| Property | Period 2 (C, N, O) | Period 3 and below (Si, P, S, etc.) | Consequence |
|---|---|---|---|
| Atomic radius and polarizability | small, hard to polarize | large, easily polarized | P and S are soft **nucleophiles** (**HSAB principle**) |
| **Electronegativity** (Pauling) | C 2.55, N 3.04, O 3.44 | Si 1.90, P 2.19, S 2.58 | H on P or Si is hydridic (P–H and Si–H can serve as hydride donors) |
| π bonds to C and O | good 2p–2p overlap, strong π bonds | poor 3p–2p overlap, weak π bonds | thioketones, silenes and the like are very unstable |
| Coordination number | at most 4 | can be 5 or 6 ($\ce{PCl5}$, $\ce{SF6}$) | five-coordinate intermediates and transition states (phosphoryl **acyl transfer**, substitution at Si) |
| Single bonds to O and F | ordinary | very strong (P–O, Si–O, Si–F) | "oxophilicity" and "fluorophilicity" drive many reactions |
| Effect on an adjacent **carbanion** | O destabilizes, N barely helps | P, S and Si stabilize an α-carbanion | ylides, α-thio and α-silyl carbanions |

The "extra" bonding ability of third-period elements was long attributed in textbooks to participation of 3d orbitals in **hybridization** or in d–p π bonding. Modern quantum-chemical calculations show that the 3d orbitals of P and S lie much higher in energy than 3s and 3p and are too diffuse in space to contribute appreciably to bonding ([6.1.3](/6.1.3#sec-3.4.5)). Throughout this chapter we therefore describe such bonds in terms of bond polarity, the **three-center four-electron bond** and **negative hyperconjugation** (Section 26.3.2), and predict geometries with VSEPR theory.

## 26.2. Classification and Nomenclature of Organophosphorus Compounds

### 26.2.1. Phosphines and Phosphonium Salts

Phosphorus and nitrogen both belong to Group 15, with valence configuration $3\mathrm{s}^2 3\mathrm{p}^3$, and phosphorus forms compounds analogous to the amines:

| Nitrogen compound | Phosphorus compound | Name |
|---|---|---|
| $\ce{NH3}$ ammonia | $\ce{PH3}$ | phosphine |
| $\ce{RNH2}$ primary amine | $\ce{RPH2}$ | primary phosphine |
| $\ce{R2NH}$ secondary amine | $\ce{R2PH}$ | secondary phosphine |
| $\ce{R3N}$ tertiary amine | $\ce{R3P}$ | tertiary phosphine |
| $\ce{R4N+X-}$ **quaternary ammonium salt** | $\ce{R4P+X-}$ | phosphonium salt |
| none | $\ce{R5P}$ | phosphorane |

**Definition 26.2.1 (Phosphine)** Phosphine $\ce{PH3}$ and its derivatives $\ce{R_nPH_{3-n}}$ ($n = 1, 2, 3$) in which hydrogen atoms are replaced by hydrocarbon groups are collectively called **phosphines**. According to the number of hydrocarbon groups they are classified as primary, secondary and tertiary phosphines.

The most commonly used tertiary phosphines are triphenylphosphine ($\ce{Ph3P}$, a white crystalline solid stable in air) and tributylphosphine (a liquid readily oxidized by air); trimethylphosphine and many lower trialkylphosphines ignite spontaneously in air. Nitrogen has no five-coordinate analogue, whereas phosphorus forms five-coordinate compounds such as $\ce{Ph5P}$ (Section 26.3.3).

### 26.2.2. Derivatives of Phosphorus Oxoacids

Most organophosphorus compounds are derivatives of the **oxoacids** of phosphorus. They are classified by the oxidation state of phosphorus and by the presence or absence of a P–C bond. Replacing one OH of a phosphoric acid by C gives a phosphonic acid, replacing two gives a phosphinic acid; the trivalent counterparts are named with the endings -ite:

| Structure | Oxidation state of P | Name | P–C bond |
|---|---|---|---|
| $\ce{(HO)3P=O}$, $\ce{(RO)3P=O}$ | +5 | phosphoric acid, phosphate | no |
| $\ce{RP(=O)(OH)2}$, $\ce{RP(=O)(OR')2}$ | +5 | phosphonic acid, phosphonate | yes |
| $\ce{R2P(=O)OH}$ | +5 | phosphinic acid | yes |
| $\ce{R3P=O}$ | +5 | phosphine oxide | yes |
| $\ce{P(OR)3}$ | +3 | phosphite | no |
| $\ce{RP(OR')2}$ | +3 | phosphonite | yes |
| $\ce{R2POR'}$ | +3 | phosphinite | yes |
| $\ce{R3P}$ | +3 | phosphine | yes |

The **electronegativity** of carbon (2.55) is higher than that of P (2.19), so a P–C bond, like a P–O bond, raises the oxidation state of P by one: four-coordinate compounds containing P=O are all P(V), and three-coordinate compounds with a lone pair are all P(III).

```smiles
OP(=O)(O)O
CCOP(=O)(OCC)OCC
CP(=O)(O)O
CP(C)(=O)O
O=P(c1ccccc1)(c1ccccc1)c1ccccc1
CCOP(OCC)OCC
```

The structures above are, in order, phosphoric acid, triethyl phosphate, methylphosphonic acid, dimethylphosphinic acid, triphenylphosphine oxide and triethyl phosphite.

### 26.2.3. Tautomerism between Trivalent and Pentavalent Forms

A dialkyl phosphite $\ce{(RO)2P-OH}$ and the corresponding dialkyl phosphonate ($\ce{(RO)2P(=O)H}$, with H bonded directly to P) are related by proton-transfer **tautomerism**, analogous to keto–enol tautomerism ([6.5.21](/6.5.21#sec-21.2)). The equilibrium lies almost completely on the pentavalent form with P=O and P–H bonds, driven by the very strong P=O bond (Section 26.3.4). This is why phosphorous acid $\ce{H3PO3}$ has the structure $\ce{HP(=O)(OH)2}$ and is only a diprotic acid ([6.1.14](/6.1.14#sec-14.1.5) deduces this structure from its acidity using Pauling's rules).

```smiles
CCOP(O)OCC>>CCOP(=O)OCC
CP(C)O>>CP(C)=O
```

The second equilibrium is that between a phosphinous acid $\ce{R2P-OH}$ and a secondary phosphine oxide $\ce{R2P(=O)H}$. The small amount of the trivalent tautomer can coordinate to metals, so the air-stable secondary phosphine oxides are often used as "pre-ligands".

## 26.3. Bonding and Configuration at Phosphorus

### 26.3.1. Three-Coordinate Phosphorus: Pyramidal Phosphines and Inversion

The phosphorus atom of a tertiary phosphine carries a lone pair, and the molecule is trigonal pyramidal, like an amine. The bond angles, however, are closer to $90^\circ$: the H–P–H angle of $\ce{PH3}$ is $93.5^\circ$, the C–P–C angle of $\ce{P(CH3)3}$ is about $99^\circ$, whereas that of $\ce{NH3}$ is $106.7^\circ$. This shows that P bonds mainly with 3p orbitals and that its lone pair has more s character (the extent of "hybridization" is low, because 3s and 3p differ considerably in energy and spatial distribution).

A direct consequence of the high s character of the lone pair is a high inversion barrier. The **nitrogen inversion** of amines has a barrier of only about $25\,\mathrm{kJ\,mol^{-1}}$ and occurs hundreds of millions of times per second at room temperature ([6.5.23](/6.5.23#sec-23.3.2)), whereas inversion of a phosphine must pass through a transition state in which P is trigonal planar, with a barrier of about $120$–$150\,\mathrm{kJ\,mol^{-1}}$, so the configuration can persist for years at room temperature. A phosphine carrying three different groups is therefore a chiral compound that can be separated by **chiral resolution**, with the phosphorus atom as a **stereocenter**; DIPAMP, discussed below, is a ligand with stereogenic phosphorus atoms.

### 26.3.2. Four-Coordinate Phosphorus and the P=O Bond

Four-coordinate phosphorus (phosphonium salts $\ce{R4P+}$, phosphate esters, phosphine oxides) is always tetrahedral. Phosphine oxides are conventionally written $\ce{R3P=O}$, and the question is what this "double bond" is.

The traditional explanation is that a lone pair on P in an $\mathrm{sp}^3$ **hybrid orbital** forms a σ dative bond to O, and O then "back-donates" a 2p lone pair into an empty 3d orbital on P to form a d–p π bond. This was the model of the 1950s to 1970s; modern calculations have refuted it (Reed and Schleyer, 1990; Gilheany's 1994 review): the occupation of the 3d orbitals of P in P=O is only about 0.1 electron, and they merely serve as polarization functions. The current description is:

**Definition 26.3.1 (Negative Hyperconjugation)** The delocalization of a lone pair on an electron-rich atom (or of a negatively charged carbon) into the σ* orbital of a bond to an adjacent, more electronegative atom is called **negative hyperconjugation**. It is a donor–acceptor interaction in which electrons flow from an n orbital into a σ* orbital, opposite in direction to the delocalization of a C–H σ bond into the empty p orbital of a carbocation (**hyperconjugation**, [6.5.2](/6.5.2#sec-2.6)).

In a phosphine oxide the P–O bond is essentially a strongly polarized σ bond, $\ce{R3P+-O-}$. Each of the three lone pairs on O delocalizes into the σ* orbital of one of the three P–C bonds, which shortens and strengthens the P–O bond and makes it cylindrically symmetric about the P–O axis (like the π electrons of a triple bond). The formulas $\ce{R3P=O}$ and $\ce{R3P+-O-}$ therefore describe the same electronic structure: the double-bond formula emphasizes that the bond is short and strong, the ionic formula that oxygen is electron-rich and phosphorus electrophilic.

```smiles
CP(C)(C)=O
C[P+](C)(C)[O-]
```

Experimental data agree with this picture. The P–O bond length in $\ce{Ph3P=O}$ is about $148\,\mathrm{pm}$, clearly shorter than the P–OR single bonds in phosphate esters (about $157$–$160\,\mathrm{pm}$); the P–O dipole moment is large, and the oxygen of a phosphine oxide is a very strong **hydrogen bond** acceptor and **Lewis base** (triphenylphosphine oxide co-crystallizes with phenols and carboxylic acids and is often hard to separate from products). The same description applies to the P–C bond of phosphorus ylides ([6.5.16](/6.5.16#sec-16.8)), the S–O bond of sulfoxides and sulfones (Section 26.9.1) and the P–O bonds of phosphate.

### 26.3.3. Five- and Six-Coordinate Phosphorus

Five-coordinate phosphorus ($\ce{PF5}$, $\ce{PCl5}$, $\ce{Ph5P}$, the oxaphosphetane of the **Wittig reaction**) is generally trigonal bipyramidal, and in a few cases (some spirocyclic phosphoranes) square pyramidal. In a trigonal bipyramid the axial and equatorial bonds are not equivalent: the axial bonds are longer and weaker and can be regarded as an F–P–F-type **three-center four-electron bond** (using one 3p orbital of P and orbitals of the two ligands, [6.1.3](/6.1.3#sec-3.4.5)), whereas the three equatorial bonds are ordinary two-center bonds. Two empirical rules follow:

- Ligands of higher **electronegativity** preferentially occupy axial positions (the axial three-center bond places negative charge on the two terminal ligands), and small rings (four- and five-membered) span one axial and one equatorial position (an internal angle of about $90^\circ$). This preference is called apicophilicity.
- Axial and equatorial ligands can exchange in pairs through a square-pyramidal transition state (Berry **pseudorotation**). The barrier is usually very low, so the NMR spectra of five-coordinate phosphorus compounds often show equivalent ligands.

Six-coordinate phosphorus occurs as octahedral anions ($\ce{PF6-}$, $\ce{PCl6-}$). Describing five- and six-coordination as $\mathrm{sp^3d}$ and $\mathrm{sp^3d^2}$ hybridization is likewise outdated, and VSEPR theory suffices to determine the geometry ([6.1.3](/6.1.3#sec-3.4.5)). Five-coordinate phosphorus is important because it is the intermediate or transition state of phosphoryl transfer: a **nucleophile** attacks a tetrahedral phosphorus opposite a **leaving group**, passing through a trigonal-bipyramidal structure in which both nucleophile and leaving group occupy axial positions. This is the "**SN2**" at phosphorus (the hydrolysis of RNA, Section 26.4).

### 26.3.4. Bond Strengths and Oxophilicity

The following table gives mean bond enthalpies of phosphorus bonds (in kJ/mol; usual textbook values, which, as in [6.1.6](/6.1.6), are suitable only for estimates and comparisons):

| Bond | $\bar D/(\mathrm{kJ\,mol^{-1}})$ | Length/pm | Comparison | $\bar D/(\mathrm{kJ\,mol^{-1}})$ |
|---|---|---|---|---|
| C–P | 264 | 184 | C–N | 305 |
| P–O | 335 | 163 | N–O | 201 |
| P=O (phosphine oxide) | about 540–580 | 148 | C=O | 745 |
| P–F | 490 | 154 | | |
| P–Cl | 326 | 203 | | |

The most striking point is that, in contrast to nitrogen, bonds from phosphorus to oxygen are much stronger than those to carbon or nitrogen. In individual molecules the P–O **bond dissociation energy** of $\ce{R3P=O}$ varies with the substituents, about $580$ for $\ce{Me3PO}$ and $555\,\mathrm{kJ\,mol^{-1}}$ for $\ce{Ph3PO}$, within the range of the table. The energy released on converting a trivalent phosphine into a phosphine oxide is enough to drive many otherwise unfavorable transformations:

$$
\ce{R3P + 1/2 O2 -> R3P=O}, \qquad \Delta_{\mathrm{r}}H^\circ \approx -300\ \text{to}\ -330\,\mathrm{kJ\,mol^{-1}}
$$

The Wittig, Arbuzov, Mitsunobu, Appel and Staudinger reactions of this chapter, and the alkene inversion of Section 26.6.5, are all driven by the formation of the P=O bond.

## 26.4. Phosphate Esters in Living Systems

Almost all organophosphorus compounds in living organisms contain no P–C bond; they are esters of phosphoric acid:

| Type | Structure | Examples |
|---|---|---|
| Phosphate monoester | $\ce{ROP(=O)(O-)2}$ | glucose 6-phosphate, phosphorylated serine and tyrosine residues |
| Phosphate diester | $\ce{(RO)2P(=O)O-}$ | backbone of DNA and RNA, phospholipids, cAMP |
| Diphosphate (pyrophosphate) monoester | $\ce{RO-P(=O)(O-)-O-P(=O)(O-)2}$ | ADP, geranyl pyrophosphate (terpene biosynthesis) |
| Triphosphate monoester | $\ce{RO-P-O-P-O-P}$ (three phosphoryl groups) | ATP, GTP and dNTPs |

```smiles
Nc1ncnc2c1ncn2[C@@H]1O[C@H](COP(=O)([O-])OP(=O)([O-])OP(=O)([O-])[O-])[C@@H](O)[C@H]1O
```

The structure above is the tetraanion of adenosine triphosphate (ATP). Why are phosphate esters so suitable as the backbone and the energy currency of life? Westheimer's answer (1987) is that phosphoric acid is triprotic and that a diester still carries one negative charge ($\mathrm{p}K_{\mathrm{a}}$ about 1–2). The charge repels **nucleophiles** such as $\ce{HO-}$, so that phosphate diesters are thermodynamically hydrolyzable but kinetically extremely stable: the half-life for spontaneous hydrolysis of the **phosphodiester bond** in DNA in neutral water at 25 °C is estimated at about 30 million years (Schroeder and Wolfenden, 2006). The charge also keeps nucleic acids inside the cell and soluble in water. Phosphoric anhydride bonds (between the β and γ phosphates of ATP) are likewise kinetically stable but thermodynamically unstable (hydrolysis of ATP to ADP has $\Delta_{\mathrm{r}}G^{\circ\prime} \approx -30.5\,\mathrm{kJ\,mol^{-1}}$); the phosphoryl group is transferred only under enzymatic catalysis, so the process can be controlled precisely ([7.1](/7.1)).

RNA hydrolyzes much more readily than DNA, and the only difference is the 2′-OH of ribose. In base (or in the active site of a ribonuclease) the deprotonated 2′-oxygen attacks the adjacent phosphorus "in line", opposite the 5′-O, through a five-coordinate trigonal-bipyramidal transition state; the 5′-O leaves, and a 2′,3′-cyclic phosphate is formed (Section 26.3.3). DNA lacks the 2′-OH and cannot be attacked intramolecularly in this way. This is one of the chemical reasons why DNA rather than RNA serves as the long-term carrier of genetic information.

![Base-catalyzed hydrolysis of RNA: the ribose 2′-oxyanion attacks the phosphorus of the adjacent 3′-phosphodiester opposite the P–O5′ bond, through a five-coordinate transition state; the 5′-oxygen of the next nucleotide leaves, giving a 2′,3′-cyclic phosphate. B is a nucleobase; R and R′ are the remainder of the chain](./plots/rna-cleavage.py)

## 26.5. Preparation and Reactions of Phosphines

### 26.5.1. Preparation of Phosphines

The most common laboratory and industrial methods are substitution of phosphorus halides by carbon **nucleophiles** and the reaction of phosphide anions with **electrophiles**:

- Phosphorus halides with organometallic reagents: $\ce{PCl3}$ reacts with three equivalents of a **Grignard reagent** or **organolithium reagent** to give a tertiary phosphine. With controlled stoichiometry and bulky groups one obtains $\ce{R2PCl}$ and $\ce{RPCl2}$, which can be treated with a different organometallic reagent to give mixed tertiary phosphines. Industrially, $\ce{Ph3P}$ is made in one pot from $\ce{PCl3}$, chlorobenzene and sodium metal.
- Alkylation of phosphide anions: reduction of $\ce{Ph2PH}$ or $\ce{Ph3P}$ with Li gives $\ce{Ph2PLi}$, a very strong soft nucleophile that undergoes an **SN2 reaction** with alkyl halides to give tertiary phosphines (1,2-bis(diphenylphosphino)ethane, dppe, is made from $\ce{Ph2PLi}$ and 1,2-dichloroethane).
- Addition of P–H bonds to unsaturated bonds (hydrophosphination): $\ce{PH3}$ or a secondary phosphine adds to alkenes under a **radical initiator** or metal catalysis, with anti-Markovnikov orientation like **hydroboration**; asymmetric hydrophosphination catalyzed by chiral metal **coordination compounds** is a modern route to chiral phosphines.
- Reduction of phosphine oxides: silanes such as $\ce{HSiCl3}$ and phenylsilane reduce phosphine oxides to phosphines (the Si–O bond is very strong, [6.5.27](/6.5.27#sec-27.5.2)). This is the basis for recycling $\ce{Ph3PO}$ and for "phosphine-catalytic" Wittig and Mitsunobu reactions.

```smiles
ClP(Cl)Cl.C[Mg]Br>>CP(C)C
c1ccc(cc1)[P-]c1ccccc1.ClCCCl>>c1ccc(cc1)P(CCP(c1ccccc1)c1ccccc1)c1ccccc1
```

### 26.5.2. Basicity and Nucleophilicity

The lone pair of a phosphine makes it basic and gives it **nucleophilicity**, but the comparison with amines runs in opposite directions: phosphines are weaker bases than amines yet stronger nucleophiles.

| Conjugate acid | $\mathrm{p}K_{\mathrm{a}}$ (water) | Conjugate acid | $\mathrm{p}K_{\mathrm{a}}$ (water) |
|---|---|---|---|
| $\ce{PH4+}$ | about $-14$ | $\ce{NH4+}$ | 9.25 |
| $\ce{(CH3)3PH+}$ | 8.65 | $\ce{(CH3)3NH+}$ | 9.80 |
| $\ce{(CH3CH2)3PH+}$ | 8.69 | $\ce{(CH3CH2)3NH+}$ | 10.75 |
| $\ce{(C6H5)3PH+}$ | 2.73 | $\ce{C6H5NH3+}$ | 4.60 |

(The phosphine data are values of Streuli, titrated in nitromethane and converted to the aqueous scale (1960); for the amines see Table 3.2 of [6.5.3](/6.5.3#sec-3.1.4). The value for $\ce{PH4+}$ is an estimate, corresponding to a $\mathrm{p}K_{\mathrm{b}}$ of about 28 for $\ce{PH3}$.)

$\ce{PH3}$ is an extremely weak base because its lone pair occupies an orbital of very high s character that must be "rehybridized" on protonation. Inductive and polarization effects of alkyl groups bring the basicity of alkylphosphines close to that of amines, while in arylphosphines the lone pair is conjugated with the benzene ring and the basicity falls. On the other hand, P is a large, easily polarized atom whose lone pair is high in energy and extends far from the nucleus, and it is not strongly solvated by **hydrogen bonding** as amines are, so the nucleophilicity of tertiary phosphines ([6.5.8](/6.5.8#sec-8.7.1)) is very high: in Pearson's nucleophilicity parameter $n_{\ce{CH3I}}$ (measured with iodomethane as substrate), $\ce{Et3P}$ has 8.72 and $\ce{Et3N}$ 6.66, so triethylphosphine reacts with iodomethane about two orders of magnitude faster. Phosphines are typical soft bases and tend to attack soft electrophilic centers ($\mathrm{sp^3}$ carbon, halogens, sulfur, low-valent metals) rather than protons and carbonyl carbons.

Tertiary phosphines react with a variety of electron-poor substrates: with alkyl halides by **SN2** to give quaternary phosphonium salts (Section 26.5.3); with α,β-unsaturated carbonyl compounds by **conjugate addition**, giving **zwitterions** that are the reactive intermediates of "phosphine-catalyzed" reactions such as the Morita–Baylis–Hillman reaction; and in strong acid they can add to alkenes (through **carbocations**) to give phosphonium salts. Electron-rich alkylphosphines are oxidized to phosphine oxides in air, so they are often sold and weighed as their tetrafluoroborate salts $\ce{[R3PH]+BF4-}$ (the salts are air-stable, high-melting and easy to weigh), and a base is added to liberate the phosphine when needed.

When a very bulky phosphine (such as $\ce{(t-Bu)3P}$) and a very bulky **Lewis acid** (such as $\ce{B(C6F5)3}$) are brought together, steric hindrance prevents them from forming an acid–base adduct, and the pair can cooperatively cleave small molecules such as $\ce{H2}$ by **heterolysis** to give $\ce{[R3PH]+[HB(C6F5)3]-}$. Such "frustrated Lewis pairs" (Stephan, 2006) have made metal-free hydrogenation possible.

![Heterolysis of $\ce{H2}$ by a frustrated Lewis pair: tri-tert-butylphosphine and tris(pentafluorophenyl)borane cannot combine because of steric hindrance; the $\ce{H2}$ molecule held between them is polarized, the phosphorus lone pair forms a bond to one hydrogen, and the electron pair of the H–H bond moves into the empty p orbital of boron, giving a phosphonium cation and a hydridoborate anion](./plots/frustrated-lewis-pair.py)

### 26.5.3. Quaternary Phosphonium Salts

The **SN2 reaction** of a tertiary phosphine with an alkyl halide gives a quaternary phosphonium salt, the precursor of Wittig reagents (phosphorus ylides, [6.5.16](/6.5.16#sec-16.8)). Treatment of a phosphonium salt with $\ce{Ag2O}$ and water gives a phosphonium hydroxide $\ce{R4P+OH-}$, but it reacts differently from hydroxides of **quaternary ammonium ions**. Quaternary ammonium hydroxides undergo **Hofmann elimination** on heating ($\ce{HO-}$ acts as a base and removes a β-H, [6.5.9](/6.5.9#sec-9.4.3), [6.5.23](/6.5.23)), whereas in a phosphonium hydroxide $\ce{HO-}$ adds to phosphorus as a **nucleophile**, giving a five-coordinate intermediate that then expels the hydrocarbon group best able to stabilize negative charge (benzyl > phenyl > alkyl), leaving a phosphine oxide and a hydrocarbon. The difference arises because P can be five-coordinate and because the P=O bond is so strong:

```smiles
c1ccc(cc1)C[P+](c1ccccc1)(c1ccccc1)c1ccccc1.[OH-]>>Cc1ccccc1.O=P(c1ccccc1)(c1ccccc1)c1ccccc1
```

![Decomposition of a phosphonium hydroxide (benzyltriphenylphosphonium): hydroxide adds to phosphorus to give a five-coordinate hydroxyphosphorane (trigonal bipyramid, OH and benzyl axial); a second hydroxide removes the O–H proton, the electrons of the O–H bond form the P=O bond while the P–C bond breaks and its electrons stay on carbon, so that the benzyl group, which best stabilizes negative charge, leaves as a carbanion and takes up a proton from water to give toluene and triphenylphosphine oxide](./plots/phosphonium-hydroxide.py)

Long-chain quaternary phosphonium salts (such as hexadecyltributylphosphonium bromide) can serve as **phase-transfer catalysts** like quaternary ammonium salts ([6.5.23](/6.5.23#sec-23.7.2)), and they are more heat-resistant (no Hofmann elimination), so they can be used at higher temperatures.

### 26.5.4. Phosphines as Ligands

Phosphines are the most important ligands in transition-metal chemistry: the lone pair on P forms a σ dative bond to the metal, and the σ* orbitals of the P–C bonds can accept electrons back from filled metal d orbitals (**π back-bonding**; not the 3d orbitals of P). Changing the substituents on phosphorus tunes both the electron-donating ability (the **Tolman electronic parameter**) and the size (the **Tolman cone angle**) of the ligand continuously, and so tunes the activity and selectivity of the catalyst ([6.5.28](/6.5.28#sec-28.3.3)). Three Nobel Prizes in Chemistry depend on phosphine ligands: the 2001 prize for the **asymmetric catalysis** of hydrogenation by Knowles and Noyori (shared with Sharpless's asymmetric oxidation), the 2005 prize for olefin metathesis by Chauvin, Grubbs and Schrock (the Grubbs catalyst contains $\ce{PCy3}$), and the 2010 prize for palladium-catalyzed coupling by Heck, Negishi and Suzuki ([6.5.29](/6.5.29#sec-29.4)).

Chiral phosphine ligands are at the heart of asymmetric catalysis:

```smiles
COc1ccccc1[P@](CC[P@](c1ccccc1)c1ccccc1OC)c1ccccc1
c1ccc(cc1)P(c1ccccc1)c1ccc2ccccc2c1-c1c(P(c2ccccc2)c2ccccc2)ccc2ccccc12
```

- DIPAMP (the first structure, the (R,R) configuration): a bisphosphine ligand developed by Knowles at Monsanto, with stereogenic phosphorus atoms (Section 26.3.1). Its rhodium **coordination complex** catalyzes the asymmetric hydrogenation of enamides, and in 1974 it was used for the industrial production of levodopa (L-DOPA), a drug for Parkinson's disease ([6.5.29](/6.5.29#sec-29.2.2)).
- BINAP (the second structure): two diphenylphosphino groups on a binaphthyl skeleton, with chirality arising from the **axial chirality** of the binaphthyl ([6.5.5](/6.5.5#sec-5.5.1)). The BINAP–Ru and BINAP–Rh systems are used in industrial asymmetric hydrogenation and asymmetric isomerization, respectively (the Takasago synthesis of menthol).
- JosiPhos: a ferrocene-based bisphosphine whose iridium complex catalyzes the asymmetric hydrogenation of imines, used in the production of the herbicide (S)-metolachlor at more than 10,000 tonnes per year, the largest-scale asymmetric catalytic process.
- Spirocyclic bisphosphines such as SDP: chiral ligands and catalysts developed by Qi-Lin Zhou on a rigid spirobiindane skeleton.

### 26.5.5. Phosphines as Reducing Agents: The Staudinger Reduction

The tendency of P(III) to be oxidized to P(V)=O makes tertiary phosphines mild, highly selective reducing agents (and at the same time "oxygen acceptors"):

- deoxygenation of epoxides to alkenes ($\ce{Ph3P}$ or $\ce{Ph2PLi}$, [6.5.10](/6.5.10#sec-10.9); for the stereochemistry see Section 26.6.5);
- reduction of disulfides to thiols: $\ce{Ph3P}$ in aqueous solvent reduces $\ce{RSSR}$ to 2 RSH and leaves nitro groups on aromatic rings untouched. In biochemistry, the water-soluble, odorless tris(2-carboxyethyl)phosphine (TCEP) is often used to reduce the disulfide bonds of proteins (Section 26.8.4); it is more stable than dithiothreitol (DTT), effective over a wide pH range, and contains no thiol group itself, so it does not interfere with subsequent thiol labeling;
- deoxygenation of peroxides, sulfoxides and N-oxides;
- reduction of **azides** to amines (the Staudinger reduction).

**Definition 26.5.1 (Staudinger Reduction)** The reaction in which an organic azide $\ce{RN3}$ reacts with a tertiary phosphine with loss of $\ce{N2}$ to give an iminophosphorane $\ce{R3P=NR}$, which is hydrolyzed to a primary amine $\ce{RNH2}$ and a phosphine oxide, is called the **Staudinger reduction**:

$$
\ce{R-N3 + Ph3P -> R-N=PPh3 + N2}, \qquad \ce{R-N=PPh3 + H2O -> R-NH2 + Ph3P=O}.
$$

![The Staudinger reduction: the lone pair of triphenylphosphine attacks the terminal nitrogen of the azide to give a zwitterionic phosphazide; this closes to a four-membered ring and then fragments, like the oxaphosphetane of the Wittig reaction, to $\ce{N2}$ and the iminophosphorane, which is hydrolyzed to the amine and triphenylphosphine oxide](./plots/staudinger.py)

An iminophosphorane $\ce{R3P=NR'}$ is a nitrogen ylide (an aza-ylide), and its P–N bond is, like the P–O and P–C bonds of ylides, of the ionic–**negative hyperconjugation** type. Staudinger discovered the reaction in 1919. It proceeds under mild conditions (room temperature, THF and water) and does not reduce esters, ketones, alkenes or nitro groups. It is often combined with "**SN2** substitution by azide" to convert alkyl halides or alcohols (via the Mitsunobu reaction, Section 26.6.3) into primary amines, with the configuration determined by the SN2 step ([6.5.24](/6.5.24#sec-24.8.2)). Iminophosphoranes undergo the aza-**Wittig reaction** with aldehydes and ketones to give **imines**, and the intramolecular aza-Wittig reaction is a common route to nitrogen heterocycles.

If a triarylphosphine bearing an ortho methyl ester is used in the Staudinger reaction, the nitrogen of the iminophosphorane attacks the neighboring ester before hydrolysis and forms a stable amide bond, linking the phosphine to the molecule that carried the azide. This is the Staudinger ligation (Saxon and Bertozzi, 2000): azides and phosphines are both almost unreactive toward biomolecules in cells, yet react specifically with each other, making this one of the earliest **bioorthogonal reactions** (Bertozzi received the 2022 Nobel Prize in Chemistry for bioorthogonal chemistry, [6.5.33](/6.5.33#sec-33.8.2)).

## 26.6. Organophosphorus Reagents in Synthesis

### 26.6.1. Review of the Wittig and HWE Reactions

The **Wittig reaction** of phosphorus ylides with aldehydes and ketones and the **Horner–Wadsworth–Emmons reaction** of phosphonate **carbanions** were discussed in detail in [6.5.16](/6.5.16#sec-16.8); here we summarize them only from the standpoint of phosphorus chemistry:

- The P–C bond of a phosphorus ylide is, like P=O, of the ionic–**negative hyperconjugation** type (Section 26.3.2), so the ylide carbon is nucleophilic; electron-withdrawing groups on the α carbon delocalize the negative charge and give stabilized ylides. According to the α substituent, ylides are classified as nonstabilized (alkyl), semistabilized (aryl, alkenyl) and stabilized (COR, COOR, CN).
- Mechanism: in the absence of lithium salts, the ylide and an aldehyde undergo a concerted [2+2] **cycloaddition** directly to an oxaphosphetane (five-coordinate phosphorus, Section 26.3.3), which decomposes by retro-[2+2] cleavage. The Z/E selectivity is under **kinetic control**, determined by the transition states leading to the two oxaphosphetanes; the older explanation in terms of equilibration of betaines has been refuted experimentally ([6.5.16](/6.5.16#sec-16.8.1)).
- Driving force: formation of $\ce{Ph3P=O}$ (Section 26.3.4). The byproduct $\ce{Ph3PO}$ is hard to remove and is the main drawback of the Wittig reaction; the HWE reaction gives a water-soluble phosphate diester salt and is highly E-selective. In situ reduction of $\ce{Ph3PO}$ to $\ce{Ph3P}$ with a silane allows the Wittig reaction to be run with only a catalytic amount of phosphine (O'Brien, 2009).

HWE reagents (phosphonates) are prepared by the Arbuzov reaction below; used one after the other, the Arbuzov and HWE reactions convert an alkyl halide into an alkene in two steps.

### 26.6.2. The Arbuzov Reaction

**Definition 26.6.1 (Arbuzov Reaction)** The reaction of a trialkyl phosphite with an alkyl halide to give a dialkyl alkylphosphonate and a new alkyl halide is called the **Arbuzov reaction**, also known as the Michaelis–Arbuzov reaction:

$$
\ce{P(OR)3 + R'-X -> R'-P(=O)(OR)2 + R-X}.
$$

The reaction occurs in two steps, both **SN2**: the phosphorus of the phosphite (a soft nucleophilic center) attacks the alkyl halide to give an alkoxyphosphonium salt; the halide ion then attacks the carbon of one of the O–R groups of the phosphonium salt, the C–O bond breaks, and the electron pair stays on oxygen to form the P=O bond.

![The Arbuzov reaction: the phosphorus of triethyl phosphite attacks the $\ce{CH2}$ of ethyl bromoacetate in an SN2 reaction to give an alkoxyphosphonium salt; bromide then attacks the $\ce{CH2}$ of one ethoxy group in an SN2 reaction, giving triethyl phosphonoacetate (an HWE reagent) and bromoethane](./plots/arbuzov.py)

Key points:

- Substrates: primary alkyl halides, allylic and benzylic halides and α-halo esters react well; secondary alkyl halides react slowly, and tertiary alkyl, aryl and vinyl halides do not react (the first step is SN2). With α-halo ketones (especially chloro ketones), phosphorus attacks the carbonyl group and rearranges to an enol phosphate (the Perkow reaction) instead of the β-keto phosphonate.
- The R–X formed in the second step is itself an alkyl halide, and if it is more reactive than R′X it reacts further with the phosphite, giving mixtures. Trimethyl or triethyl phosphite is therefore normally used: the MeX or EtX formed has a low **boiling point** and distills out of the mixture on heating.
- The driving force is P(III) → P(V)=O; in the Arbuzov reaction one C–O bond is replaced by a C–P bond and a P=O bond.
- Trivalent phosphorus compounds of similar structure (phosphonites $\ce{RP(OR')2}$, phosphinites $\ce{R2POR'}$) react in the same way, giving phosphinates and phosphine oxides, respectively.

![The Perkow reaction: triethyl phosphite with chloroacetone. The soft phosphorus does not displace chloride but adds to the carbonyl carbon, with the C=O electrons moving to oxygen; the oxyanion bonds to phosphorus while the electrons of the P–C bond form a C=C bond and chloride leaves, so that phosphorus migrates from carbon to oxygen, giving an enol phosphonium ion; chloride then removes one ethyl group in an SN2 reaction (as in the second step of the Arbuzov reaction), giving an enol phosphate and chloroethane](./plots/perkow.py)

### 26.6.3. The Mitsunobu Reaction

Replacing the hydroxyl group of an alcohol by another group usually requires first converting OH into a good **leaving group** (sulfonate, halide, [6.5.8](/6.5.8#sec-8.6)) and then carrying out an **SN2** substitution. The Mitsunobu reaction combines these two steps in one pot under neutral conditions at room temperature.

**Definition 26.6.2 (Mitsunobu Reaction)** The reaction in which an alcohol is converted by triphenylphosphine and diethyl azodicarboxylate (DEAD) or diisopropyl azodicarboxylate (DIAD) into R–Nu by an acidic nucleophile NuH, with inversion of configuration at the carbon bearing the hydroxyl group, is called the **Mitsunobu reaction** (Mitsunobu and Yamada, 1967):

$$
\ce{R-OH + Nu-H + Ph3P + EtO2C-N=N-CO2Et -> R-Nu + Ph3P=O + EtO2C-NH-NH-CO2Et}.
$$

![The Mitsunobu reaction: triphenylphosphine adds to the N=N bond of DEAD to give a zwitterion (betaine) whose nitrogen anion removes the proton of the carboxylic acid; the oxygen of the alcohol attacks the phosphorus of the phosphonium salt, expelling diethyl hydrazinedicarboxylate to give an alkoxyphosphonium ion; the carboxylate attacks the former alcohol carbon from the back (SN2), converting (S)-butan-2-ol into the (R)-benzoate, and triphenylphosphine oxide leaves](./plots/mitsunobu.py)

The mechanism has three key features. (1) DEAD serves as both "activator" of $\ce{Ph3P}$ and "proton acceptor": the betaine they form is basic enough to remove the proton of NuH. (2) The oxygen of the alcohol attacks the positively charged phosphorus, forming the alkoxyphosphonium ion $\ce{R-O-P+Ph3}$; the original OH (which would leave as $\ce{HO-}$, a very poor leaving group) becomes $\ce{O=PPh3}$, an excellent leaving group. (3) The attack of $\ce{Nu-}$ on carbon is SN2, so the stereogenic carbon of a secondary alcohol undergoes complete **Walden inversion**. Overall, $\ce{Ph3P}$ is oxidized and DEAD is reduced to the hydrazine.

Scope and limitations:

- Alcohols: primary and secondary alcohols are good substrates, and secondary alcohols undergo complete inversion; tertiary alcohols do not react (SN2), and hindered secondary alcohols may eliminate.
- The **nucleophile** must be acidic enough to be deprotonated by the betaine: in general $\mathrm{p}K_{\mathrm{a}}$ of NuH $\lesssim 11$, at most about 13–15. The less acidic the nucleophile, the more easily the hydrazine anion formed is itself alkylated, which is the main side reaction. Common nucleophiles are carboxylic acids (giving esters; 4-nitrobenzoic acid is best), phenols (aryl ethers), imides (phthalimide, giving a Gabriel-type precursor of primary amines), $\ce{HN3}$ or diphenylphosphoryl azide (DPPA, giving azides), thiols and thioacetic acid (sulfides, thioesters), and β-diketones and β-keto esters (carbon nucleophiles; malonates are not acidic enough).
- Intramolecular Mitsunobu reactions can form three- to seven-membered cyclic ethers and amines.

The most common use is "inverting the configuration of a secondary alcohol": 4-nitrobenzoic acid as the nucleophile gives the ester with inverted configuration, and hydrolysis then converts a secondary alcohol into its **epimer** (Question 3). The drawback is poor atom economy: each R–Nu formed produces one equivalent of $\ce{Ph3PO}$ and hydrazine, which are troublesome to separate. Denton and coworkers (2019) developed a catalytic Mitsunobu reaction: an o-hydroxybenzyl diphenylphosphine oxide serves as catalyst and, with water removed in a Dean–Stark apparatus, dehydrates intramolecularly to a cyclic alkoxyphosphonium salt, which activates the alcohol; the carboxylate then gives the ester with inversion by SN2 and the catalyst is regenerated, with water as the only byproduct (Question 4).

### 26.6.4. The Appel Reaction and Related Halogenations

The same idea (turn OH into $\ce{O-P+Ph3}$ and then displace it by halide ion in an **SN2** reaction), with $\ce{CCl4}$ or $\ce{CBr4}$ in place of DEAD, converts alcohols into alkyl halides:

**Definition 26.6.3 (Appel Reaction)** The reaction in which an alcohol is converted by triphenylphosphine and a carbon tetrahalide ($\ce{CCl4}$, $\ce{CBr4}$) into an alkyl halide, with inversion of configuration at a secondary center, is called the **Appel reaction** (1975).

$\ce{Ph3P}$ first attacks a bromine of $\ce{CBr4}$ to give $\ce{Ph3P+Br}$ and $\ce{CBr3-}$; $\ce{CBr3-}$ removes the proton of the alcohol (giving $\ce{CHBr3}$), the alkoxide attacks phosphorus to form an alkoxyphosphonium salt, and finally $\ce{Br-}$ displaces $\ce{Ph3PO}$ by SN2, exactly as in the last step of the Mitsunobu reaction.

```smiles
C[C@H](O)CCc1ccccc1.BrC(Br)(Br)Br>>C[C@@H](Br)CCc1ccccc1.BrC(Br)Br
```

![Mechanism of the Appel reaction: the lone pair of $\ce{Ph3P}$ attacks a bromine of $\ce{CBr4}$ and the electrons of the C–Br bond stay on carbon, giving a bromotriphenylphosphonium ion and $\ce{CBr3-}$; $\ce{CBr3-}$ removes the proton of the alcohol (releasing $\ce{CHBr3}$), and the alkoxide attacks phosphorus with loss of bromide to give an alkoxyphosphonium ion; bromide attacks the alcohol carbon from the back (SN2), converting (S)-4-phenylbutan-2-ol into the (R)-bromide with inverted configuration, and triphenylphosphine oxide leaves](./plots/appel.py)

The conditions of the Appel reaction are neutral and produce no HX, so it suits acid-sensitive substrates and complements $\ce{PBr3}$, $\ce{SOCl2}$ and similar methods ([6.5.9](/6.5.9#sec-9.7)). With $\ce{I2}$/$\ce{Ph3P}$/imidazole one obtains alkyl iodides. The $\ce{Ph3P=CBr2}$ formed from $\ce{Ph3P}$ and $\ce{CBr4}$ reacts with aldehydes to give 1,1-dibromoalkenes, the first step of the Corey–Fuchs alkyne synthesis ([6.5.11](/6.5.11#sec-11.13)).

### 26.6.5. Inversion of Alkene Configuration

Phosphorus chemistry can convert a (Z)-alkene into an (E)-alkene or the reverse (Vedejs and Fuchs, 1971). The steps are: (1) epoxidation of the alkene with a peroxy acid (syn addition, configuration retained, [6.5.11](/6.5.11#sec-11.8.1)); (2) opening of the epoxide from the back by $\ce{Ph2PLi}$ in an **SN2** reaction (inversion at one carbon) to give a β-oxido phosphine; (3) quaternization of phosphorus with iodomethane to give a β-oxido phosphonium salt (a betaine); (4) attack of the oxide on phosphorus and syn elimination through an oxaphosphetane (the same as the second step of the **Wittig reaction**), giving the alkene and $\ce{Ph2MePO}$.

Anti ring opening (one inversion) followed by syn elimination interchanges the relative positions of the substituents on the two sides of the double bond:

```smiles
CCCC/C=C\CCCC>>CCCC/C=C/CCCC
```

![Conversion of the epoxide of (Z)-but-2-ene into (E)-but-2-ene: diphenylphosphide opens the cis epoxide in an SN2 reaction (inversion at the carbon attacked), giving a β-oxido phosphine; iodomethane quaternizes phosphorus to give the betaine; after rotation to bring the oxide and phosphorus to the same side, oxygen attacks phosphorus to form an oxaphosphetane, and syn decomposition of the four-membered ring releases the (E)-alkene and methyldiphenylphosphine oxide](./plots/alkene-inversion.py)

This is the same chemistry as the deoxygenation of epoxides by $\ce{Ph3P}$ mentioned in [6.5.10](/6.5.10#sec-10.9): both epoxidation and deoxygenation are stereospecific, the former with retention, while the latter involves one inversion on ring opening, so the overall result is inversion of the double-bond configuration.

### 26.6.6. Organophosphorus Pesticides, Nerve Agents and Drugs

Many organophosphorus compounds are strongly bioactive because they resemble phosphate esters in structure:

- Organophosphorus pesticides (trichlorfon, parathion, malathion) and nerve agents (sarin, VX) are derivatives of phosphate or phosphonate esters carrying good leaving groups (F, 4-nitrophenol, enols, and so on). The hydroxyl group of the active-site serine of acetylcholinesterase attacks their phosphorus (substitution at phosphorus, Section 26.3.3), the **leaving group** leaves, the enzyme is irreversibly phosphorylated and inactivated, and acetylcholine accumulates in the synapse, causing poisoning (covalent inhibition in **enzyme catalysis**, [6.3.17](/6.3.17)). The antidote pralidoxime (2-PAM) is a pyridinium oxime whose oximate oxygen is a strong α-effect **nucleophile** and can transfer the phosphoryl group off the serine before "aging" occurs.
- Glyphosate ($\ce{HO2CCH2NHCH2P(=O)(OH)2}$) contains a P–C bond and is an analogue of phosphoenolpyruvate that inhibits EPSP synthase in the plant pathway of aromatic amino acid biosynthesis.
- Bisphosphonates (P–C–P) are analogues of pyrophosphate (P–O–P) that are not hydrolyzed in the body; they bind to hydroxyapatite in bone and are used to treat osteoporosis. Phosphonate nucleotide analogues (tenofovir) and "ProTide" prodrugs (sofosbuvir) exploit the stability of P–C or P–N bonds in vivo.

![Organophosphate inhibition of acetylcholinesterase and reactivation by pralidoxime. Top: the hydroxyl group of the active-site serine attacks the phosphorus of sarin while the imidazole of histidine simultaneously removes the O–H proton; fluoride leaves, serine is phosphonylated, and the enzyme is inactivated. Bottom: the oximate oxygen of pralidoxime (2-PAM, an α-effect nucleophile) attacks the same phosphorus, the serine oxygen leaves, and the enzyme is restored (effective only before the phosphonylated enzyme "ages" by losing its isopropyl group)](./plots/ache-phosphorylation.py)

## 26.7. Classification and Bonding of Organosulfur Compounds

### 26.7.1. Classification and Nomenclature

Sulfur and oxygen are both in Group 16, and many oxygen-containing compounds have sulfur analogues; the **oxidation state** of sulfur can also range from −2 to +6, and there are families of compounds with no oxygen counterparts:

| Oxygen compound | Sulfur compound | Structure | Name |
|---|---|---|---|
| alcohol | thiol | R–SH | thiol |
| phenol | thiophenol | Ar–SH | thiophenol |
| ether | sulfide (thioether) | R–S–R′ | sulfide (thioether) |
| peroxide | disulfide | R–S–S–R′ | disulfide |
| oxirane | thiirane | three-membered ring | thiirane |
| oxonium salt | sulfonium salt | $\ce{R3S+X-}$ | sulfonium salt |
| aldehyde, ketone | thioaldehyde, thioketone | R(H)C=S | thioaldehyde, thioketone |
| urea | thiourea | $\ce{(H2N)2C=S}$ | thiourea |
| ester | thioester | RC(=O)SR′ | thioester |
| carboxylic acid | thio S-acid, thio O-acid, dithio acid | RC(=O)SH, RC(=S)OH, RC(=S)SH | thioic acids |
| none | sulfoxide, sulfone | $\ce{R2S=O}$, $\ce{R2SO2}$ | sulfoxide, sulfone |
| none | sulfenic, sulfinic, sulfonic acid | RSOH, $\ce{RSO2H}$, $\ce{RSO3H}$ | sulfenic, sulfinic, sulfonic acid |

The last three families and the sulfoxides and sulfones have no oxygen analogues and can be regarded as derivatives of sulfuric or sulfurous acid (a sulfonic acid is sulfuric acid with one OH replaced by a hydrocarbon group, a sulfone has both OH groups replaced). In nomenclature, –SH as a substituent is called sulfanyl (IUPAC 2013) and RS– is called alkylsulfanyl (methylsulfanyl, $\ce{CH3S-}$); when a thiol is the **principal characteristic group**, the suffix -thiol is added to the parent name (ethanethiol).

### 26.7.2. Features of Bonding at Sulfur

- **Electronegativity**: S has 2.58, almost the same as C (2.55), so the C–S bond is almost nonpolar; the H of an S–H bond carries a partial positive charge, but much less than in O–H (**hydrogen bonding** of thiols is very weak).
- Large atomic size and high polarizability: S is a soft nucleophilic center, and thiolates are among the best **SN2** **nucleophiles**; S binds strongly to soft metal ions ($\ce{Hg^2+}$, $\ce{Pb^2+}$, $\ce{Cd^2+}$, Pd, Au), which is why sulfur compounds "poison" metal catalysts.
- Weak π bonds: C=S involves 2p–3p overlap and its π bond is much weaker than that of C=O, so thioaldehydes and most thioketones are unstable and polymerize readily; stable thiocarbonyl compounds (thioureas, thioamides, dithioesters) have a lone pair on N or S conjugated with C=S.
- Multiple oxidation states: one sulfur atom can be oxidized step by step, sulfide → sulfoxide → sulfone, thiol → disulfide → sulfenic acid → sulfinic acid → sulfonic acid.
- Stabilization of an adjacent **carbanion**: the α-H atoms of sulfides, sulfoxides, sulfones and sulfonium salts are appreciably acidic (see the table below), which is the most important property of sulfur reagents in synthesis (Section 26.11).

| Compound | $\mathrm{p}K_{\mathrm{a}}$ (DMSO) | Compound | $\mathrm{p}K_{\mathrm{a}}$ (DMSO) |
|---|---|---|---|
| $\ce{CH4}$ | about 56 | $\ce{CH3SOCH3}$ (DMSO) | 35.1 |
| $\ce{C6H5SCH3}$ | 42 | $\ce{(C6H5S)2CH2}$ | 30.8 |
| $\ce{CH3SO2C6H5}$ | 29.0 | 2-phenyl-1,3-dithiane | 30.7 |

(Data of Bordwell and coworkers; for $\ce{CH4}$, DMSO and $\ce{CH3SO2C6H5}$ see Table 3.3 of [6.5.3](/6.5.3#sec-3.1.4), for 2-phenyl-1,3-dithiane see [6.5.16](/6.5.16#sec-16.10.2).)

A single sulfide group lowers the $\mathrm{p}K_{\mathrm{a}}$ of a methyl group by about 14 units, two sulfur atoms by about 25 units, and a sulfonyl group even more. This stabilization, and the S–O bonds in sulfoxides and sulfones, were traditionally attributed to the 3d orbitals of S (d–p π bonding); the current explanation is the same as for phosphorus: carbanion stabilization comes from the high polarizability of the large sulfur atom and from negative hyperconjugation into the C–S σ* orbital (Definition 26.3.1); the S–O bond of a sulfoxide is a polar bond of the $\ce{S+-O-}$ type, and a sulfone can be written $\ce{R2S^{2+}(O-)2}$, with the lone pairs on O delocalized into the S–C σ* orbitals.

Bond energies are also revealing (**mean bond enthalpies**, kJ/mol): C–S 272, S–S 226, S–F 284, S–Cl 255. In contrast to phosphorus, the dissociation enthalpy of the S–O bond in a sulfoxide (about $360\,\mathrm{kJ\,mol^{-1}}$ for DMSO) is much lower than that of the P–O bond in a phosphine oxide (about $555\,\mathrm{kJ\,mol^{-1}}$); the bond energy of the diatomic molecule SO (about $522\,\mathrm{kJ\,mol^{-1}}$) cannot be used to estimate the S–O bond in sulfoxides. This difference determines the different fates of sulfur ylides and phosphorus ylides (Section 26.11.2).

## 26.8. Thiols, Sulfides and Disulfides

### 26.8.1. Physical Properties and Acidity of Thiols

**Definition 26.8.1 (Thiol)** A compound RSH in which a sulfhydryl group (–SH) is bonded to an $\mathrm{sp^3}$ carbon is called a **thiol** (formerly mercaptan); if –SH is bonded to an aromatic ring, the compound is called a thiophenol.

S–H···S **hydrogen bonds** are very weak, so the boiling points of thiols are much lower than those of the corresponding alcohols: methanethiol $6\,^\circ\mathrm{C}$ (methanol $65\,^\circ\mathrm{C}$), ethanethiol $35\,^\circ\mathrm{C}$ (ethanol $78\,^\circ\mathrm{C}$), and their solubility in water is also low. Lower thiols have an extremely foul odor; humans can smell ethanethiol at parts-per-billion levels, so traces of thiols are added to odorless natural gas as a warning agent. The odors of the defensive secretion of skunks, of rotting vegetables and of bad breath come from thiols and sulfides.

Thiols are much more acidic than alcohols ([6.5.3](/6.5.3#sec-3.1.4), Table 3.2):

| Acid | $\mathrm{p}K_{\mathrm{a}}$ (water) | Acid | $\mathrm{p}K_{\mathrm{a}}$ (water) |
|---|---|---|---|
| $\ce{CH3CH2SH}$ | 10.6 | $\ce{CH3CH2OH}$ | 15.9 |
| $\ce{C6H5SH}$ | 6.62 | $\ce{C6H5OH}$ | 9.99 |
| $\ce{H2S}$ | 7.05 | $\ce{H2O}$ | 14.00 |
| SH of cysteine | 8.2 | | |

Acidity increases down a group ($\ce{H2O}$ < $\ce{H2S}$, HF < HCl), mainly because the H–S bond is weaker than the H–O bond, and secondarily because S is large and easily polarized, so the negative charge is spread over a larger volume. A thiol is therefore almost completely converted into thiolate in aqueous NaOH, whereas ethanol is not; at physiological pH a small fraction of the sulfhydryl groups of cysteine exists as thiolate, and the microenvironment of an enzyme active site can lower its $\mathrm{p}K_{\mathrm{a}}$ to 4–5, which makes cysteine the most reactive nucleophilic residue in proteins ([6.5.33](/6.5.33#sec-33.3.5)).

### 26.8.2. Nucleophilicity and the Preparation of Sulfides

A thiolate is a very strong **nucleophile** with only weak basicity (the $\mathrm{p}K_{\mathrm{a}}$ of its conjugate acid is about 10, about 6 units lower than that of an alkoxide), so with primary and secondary alkyl halides it undergoes almost only **SN2** reaction, rather than the extensive elimination alkoxides show with secondary halides ([6.5.9](/6.5.9#sec-9.6)). This gives a route to sulfides:

```smiles
CC[S-].CCCBr>>CCCSCC
```

When thiols are prepared from NaSH and alkyl halides, the thiol formed is alkylated further to the sulfide. A better method uses thiourea as an equivalent of sulfide ion: the sulfur of thiourea reacts with the alkyl halide by SN2 to give an isothiouronium salt, which is hydrolyzed in base to release the thiol; alternatively, potassium thioacetate gives a thioacetate, which is then hydrolyzed or reduced.

```smiles
CCCCBr.NC(N)=S>>CCCCSC(N)=[NH2+]
CCCCSC(N)=[NH2+]>>CCCCS
```

The sulfur of a sulfide also has lone pairs and is a much better nucleophile than the oxygen of an ether: sulfides form sulfonium salts with alkyl halides (Section 26.8.3), which ethers cannot do. The toxicity of mustard gas (bis(2-chloroethyl) sulfide), with two β-chloroethyl groups on sulfur, comes from **internal nucleophilic substitution** by sulfur:

![Alkylation by mustard gas: the lone pair of sulfur displaces chloride intramolecularly in an SN2 reaction to give a highly strained three-membered episulfonium ion; a nucleophile (N7 of guanine in DNA, denoted Nu) opens the three-membered ring. The other chloroethyl arm reacts in the same way, so one molecule of mustard gas can cross-link the two strands of DNA](./plots/mustard.py)

**Neighboring group participation** by sulfur makes the hydrolysis of mustard gas several orders of magnitude faster than that of an ordinary primary alkyl chloride ([6.5.8](/6.5.8#sec-8.10)). With nitrogen in place of sulfur, the same structure gives nitrogen mustards ($\ce{RN(CH2CH2Cl)2}$), which cross-link DNA through aziridinium ions in the same way and were the first anticancer alkylating agents.

### 26.8.3. Sulfonium Salts

Sulfides react with alkyl halides or dimethyl sulfate to give trialkylsulfonium salts $\ce{R3S+X-}$. The trigonal-pyramidal sulfur atom of a sulfonium salt inverts slowly, so sulfonium salts with three different groups are chiral. Sulfonium salts have two main reactions:

- As alkylating agents: a dialkyl sulfide is a good **leaving group**, and **nucleophiles** attack the α carbon of the sulfonium salt by **SN2**. The universal biological methyl donor S-adenosylmethionine (SAM) is a sulfonium salt: the sulfide of methionine attacks the 5′-carbon of ATP to give SAM, and various methyltransferases then transfer its $\ce{S+-CH3}$ by SN2 to nucleophilic sites such as cytosine in DNA, lysine in proteins and the oxygen of catecholamines ([6.5.8](/6.5.8#sec-8.11)).
- As precursors of ylides: a strong base removes an α-H to give a sulfur ylide (Section 26.11.2).

![Methyl transfer from S-adenosylmethionine (SAM) (catechol O-methyltransferase, COMT): SAM is a sulfonium salt (Ado is 5′-deoxyadenosyl, R is the remainder of methionine); the phenoxide of dopamine attacks the methyl carbon from the side opposite sulfur (SN2), and the neutral sulfide S-adenosylhomocysteine (SAH) leaves](./plots/sam-methylation.py)

### 26.8.4. Redox Chemistry and Disulfide Bonds

Thiols are readily oxidized to disulfides by mild oxidants ($\ce{I2}$, $\ce{H2O2}$, $\ce{O2}$ in air catalyzed by traces of metal ions), and disulfides can be reduced back to thiols by mild reducing agents (Zn/acid, $\ce{NaBH4}$, $\ce{NaHSO3}$, phosphines, dithiothreitol):

$$
\ce{2 RSH <=>[\ce{[O]}][\ce{[H]}] RS-SR}.
$$

Strong oxidants ($\ce{HNO3}$, $\ce{KMnO4}$, excess $\ce{H2O2}$) oxidize thiols all the way to sulfonic acids $\ce{RSO3H}$, through sulfenic acids $\ce{RSOH}$ and sulfinic acids $\ce{RSO2H}$; these oxidized forms of cysteine in proteins are molecular switches in reactive-oxygen-species signaling.

**Definition 26.8.2 (Disulfide Bond)** A covalent single bond –S–S– between two sulfur atoms is called a **disulfide bond**. A disulfide bond formed by oxidation of the sulfhydryl groups of two cysteine residues in a protein (cystine) is called a disulfide bridge.

Exchange between thiols and disulfides (thiol–disulfide exchange) is an **SN2 reaction** of a thiolate at a sulfur atom: the **nucleophile** attacks one sulfur along the S–S bond axis, and the other sulfur leaves as thiolate.

![Thiol–disulfide exchange: the thiolate $\ce{RS-}$ attacks one sulfur atom of the disulfide R′S–SR′ along the S–S bond axis, and the other sulfur leaves as $\ce{R'S-}$, giving the mixed disulfide RS–SR′. The reaction is reversible, and the equilibrium is determined by the concentrations and redox potentials of the thiols](./plots/thiol-disulfide.py)

This reaction is fast even in neutral water and is the chemical basis for the formation, breaking and "shuffling" of disulfide bonds in cells:

- Glutathione (GSH, γ-glutamylcysteinylglycine) is the most abundant thiol in cells (1–10 mM). In the cytoplasm the ratio of GSH to its disulfide GSSG is usually greater than 100, and the standard potential of the $\ce{GSSG}/\ce{2GSH}$ **redox couple** is $E^{\circ\prime} \approx -0.24\,\mathrm{V}$ (pH 7), forming the cell's "redox buffer", which keeps protein sulfhydryl groups reduced through thiol–disulfide exchange.
- Disulfide bonds of secreted proteins (insulin, antibodies) form in the endoplasmic reticulum, where the environment is comparatively oxidizing, and protein disulfide isomerase shuffles mispaired disulfide bonds into the correct pairing through a series of exchange reactions; proteins in the cytoplasm rarely have disulfide bonds.
- In the laboratory, protein disulfide bonds are opened with excess dithiothreitol (DTT, $E^{\circ\prime} \approx -0.33\,\mathrm{V}$) or TCEP (Section 26.5.5): after exchange with the protein, DTT closes intramolecularly to a stable six-membered cyclic disulfide, which drives the equilibrium.

![Reduction of a disulfide bond by dithiothreitol (DTT): one thiolate of DTT attacks one sulfur of RS–SR (thiol–disulfide exchange) and $\ce{RS-}$ leaves, giving a mixed disulfide; the other thiolate of DTT attacks, intramolecularly, the sulfur attached to the original chain and closes to a six-membered cyclic disulfide (trans-4,5-dihydroxy-1,2-dithiane), releasing the second $\ce{RS-}$. The intramolecular step is very favorable and drives the reduction to completion](./plots/dtt.py)

The S–S bond of a disulfide ($\mathrm{MeS-SMe}$ about $270\,\mathrm{kJ\,mol^{-1}}$) is weaker than a C–C bond and can be cleaved photochemically or by radicals; the polysulfide cross-links of vulcanized rubber can likewise exchange on heating.

Sulfides are oxidized to sulfoxides by $\ce{H2O2}$ or $\ce{NaIO4}$ at room temperature, and with excess oxidant (or 2 equivalents of mCPBA) further to sulfones (Section 26.9).

### 26.8.5. Thioesters and Coenzyme A

**Thioesters** RC(=O)SR′ formed from carboxylic acids and thiols ([6.5.19](/6.5.19#sec-19.9.1)) are the "activated acyl" compounds of living systems: the 3p lone pair of sulfur is poorly conjugated with the carbonyl group, so the carbonyl is more electrophilic than in an ordinary ester, $\ce{RS-}$ (the $\mathrm{p}K_{\mathrm{a}}$ of its conjugate acid is about 10) is a better **leaving group** than $\ce{RO-}$, and the α-H of a thioester is also more acidic than that of an ester. The terminal sulfhydryl group of coenzyme A (CoA–SH) comes from cysteamine, and acetyl-CoA passes on the acetyl group in the citric acid cycle and in fatty acid and cholesterol biosynthesis as an **electrophile** (**acyl transfer**) or as a **nucleophile** (through its enol, **Claisen condensation**, [6.5.22](/6.5.22#sec-22.10.2)). A thioester can be exchanged by another thiol (transthioesterification), which is the basis of **native chemical ligation** in the chemical synthesis of proteins ([6.5.33](/6.5.33#sec-33.7.7)).

### 26.8.6. Antidotes for Heavy-Metal Poisoning

The sulfhydryl group is a soft base and binds very tightly to soft heavy metals such as Hg, Pb, As and Cd (the **HSAB principle**); molecules with two adjacent sulfhydryl groups form five-membered **chelates** with metals and bind even more strongly. Antidotes for heavy-metal poisoning are exactly such dithiols:

```smiles
OCC(S)CS
OC(=O)[C@@H](S)[C@@H](S)C(=O)O
```

- Dimercaprol (BAL, British anti-Lewisite, the first structure above): developed in World War II to counter lewisite, an arsenic-containing blistering agent, and used for poisoning by arsenic, mercury, gold and bismuth.
- Succimer (meso-2,3-dimercaptosuccinic acid, DMSA, the second) and its sodium salt: very water-soluble and of low toxicity, orally active, and used for poisoning by lead, mercury, arsenic and antimony.

The strong coordination of sulfur to transition metals also has a drawback: sulfur compounds cause **catalyst poisoning** of hydrogenation catalysts such as Pd, Pt and Ni. Raney Ni can hydrogenolyze C–S bonds (desulfurization, [6.5.16](/6.5.16#sec-16.6.2)) precisely because the large amount of nickel and adsorbed hydrogen on its surface can "swallow" the sulfur.

## 26.9. Sulfoxides and Sulfones

### 26.9.1. Structure and Properties

**Definition 26.9.1 (Sulfoxides and Sulfones)** A compound $\ce{R2S=O}$ in which sulfur carries two hydrocarbon groups and one oxygen atom is called a **sulfoxide**, and a compound $\ce{R2SO2}$ in which sulfur carries two hydrocarbon groups and two oxygen atoms is called a **sulfone**.

The sulfur of a sulfoxide still carries a lone pair, and the molecule is trigonal pyramidal; the inversion barrier at sulfur is high (about $150$–$170\,\mathrm{kJ\,mol^{-1}}$; p-tolyl methyl sulfoxide racemizes only at about $200\,^\circ\mathrm{C}$), so sulfoxides with two different hydrocarbon groups are stable chiral compounds, with sulfur as a **stereocenter**. The description of the S–O bond of a sulfoxide as a σ bond between an $\mathrm{sp^3}$ **hybrid orbital** of S and a p orbital of O, with p electrons of O then back-donated into 3d orbitals of S, is outdated, like the old model of P=O (Section 26.7.2): the S–O bond is a strongly **polar bond** of the $\ce{S+-O-}$ type, with **negative hyperconjugation** of the lone pairs of O into the S–C σ* orbitals. An important example of a chiral sulfoxide is the antiulcer drug omeprazole (a benzimidazole sulfoxide, marketed as the racemate) and its single enantiomer esomeprazole (S configuration). Omeprazole itself is a prodrug: in the strongly acidic environment of gastric parietal cells it rearranges to a sulfenamide, which forms a disulfide bond with a cysteine sulfhydryl group of the proton pump ($\ce{H+/K+}$-ATPase) and irreversibly inhibits gastric acid secretion.

Dimethyl sulfoxide (DMSO) is the most important sulfoxide: boiling point $189\,^\circ\mathrm{C}$, dielectric constant about 47, it dissolves many organic compounds and inorganic salts and is a typical **polar aprotic solvent** ([6.5.8](/6.5.8#sec-8.8.1)). Its oxygen is a good **donor atom** and **hydrogen bond** acceptor, and the sulfur carries a partial positive charge. DMSO penetrates skin and carries dissolved substances in with it, so gloves must be worn.

The sulfur of a sulfone is tetrahedral with no lone pair, and sulfones are chemically very stable, neither easily oxidized nor easily reduced; the sulfonyl group is strongly electron-withdrawing, lowering the $\mathrm{p}K_{\mathrm{a}}$(DMSO) of the α-H to about 29 (Section 26.7.2), and the α-sulfonyl **carbanion** is the key to the Julia olefination (Section 26.11.3). The sulfone structure occurs in many drugs (such as dapsone against leprosy) and in heat-resistant engineering plastics (polysulfones).

### 26.9.2. The Swern Oxidation

The oxygen of a sulfoxide is nucleophilic, and after "activation" by an **electrophile** the sulfur becomes a very good electrophilic center and a very good **leaving group**, so a sulfoxide can serve as a mild oxidant. The most important application is the oxidation of alcohols to aldehydes and ketones.

**Definition 26.9.2 (Swern Oxidation)** The reaction in which dimethyl sulfoxide is activated with oxalyl chloride at $-78\,^\circ\mathrm{C}$, a primary or secondary alcohol is added, and triethylamine is then added, oxidizing the alcohol to an aldehyde or ketone while DMSO is reduced to dimethyl sulfide, is called the **Swern oxidation** (Omura and Swern, 1978).

$$
\ce{R2CHOH + (CH3)2SO + (COCl)2 + 2 Et3N -> R2C=O + (CH3)2S + CO + CO2 + 2 Et3NH+Cl-}.
$$

The mechanism has three stages:

1. Activation: the oxygen of DMSO attacks one carbonyl group of oxalyl chloride with loss of $\ce{Cl-}$; $\ce{Cl-}$ then attacks sulfur, and the oxalyl group fragments to CO and $\ce{CO2}$, giving the chlorodimethylsulfonium ion $\ce{(CH3)2S+Cl}$. This step releases gas and is strongly exothermic, so it must be carried out at $-78\,^\circ\mathrm{C}$.
2. The oxygen of the alcohol attacks the sulfur of the sulfonium ion and $\ce{Cl-}$ leaves, giving the alkoxysulfonium ion $\ce{R2CH-O-S+(CH3)2}$.
3. Triethylamine is added and removes a proton from a methyl group on sulfur to form a sulfonium ylide; the **carbanion** of the ylide removes the H on the alcohol carbon intramolecularly through a five-membered transition state, the electron pair of the C–H bond forms C=O, the O–S bond breaks, and dimethyl sulfide is released.

![The activation step of the Swern oxidation: the oxygen of DMSO adds to one carbonyl carbon of oxalyl chloride, and the tetrahedral intermediate (not drawn) loses chloride to give an acyloxysulfonium ion; chloride attacks sulfur and the S–O bond breaks, releasing chlorooxalate and the chlorodimethylsulfonium ion; chlorooxalate fragments: the oxyanion forms $\ce{CO2}$, the electrons of the C–C bond stay on the other carbon, whose oxygen lone pair completes the triple bond of CO as chloride leaves](./plots/swern-activation.py)

![The last two steps of the Swern oxidation: the oxygen of cyclohexanol attacks the sulfur of the chlorodimethylsulfonium ion and chloride leaves, giving an alkoxysulfonium ion; triethylamine removes a proton from S–CH₃ to give a sulfonium ylide, whose carbon removes the hydrogen on the alcohol carbon intramolecularly through a five-membered transition state, giving cyclohexanone and dimethyl sulfide](./plots/swern.py)

Step 3 is an intramolecular syn elimination (like the thermal elimination of sulfoxides in Section 26.9.3); the base only serves to form the ylide, and aldehydes are therefore not oxidized further to carboxylic acids (the mixture contains no water and no stronger oxidant). The Swern oxidation is mild and metal-free, suitable for substrates with many sensitive functional groups, and an α **stereocenter** is generally not racemized (using the bulky $i$-$\ce{Pr2NEt}$ in place of $\ce{Et3N}$ reduces racemization further). Its drawbacks are the strong stench of the byproduct dimethyl sulfide (which can be oxidized by bleach to odorless DMSO or dimethyl sulfone) and the need for low temperature: above about $-60\,^\circ\mathrm{C}$ the alkoxysulfonium ion undergoes a Pummerer-type rearrangement to give the methylthiomethyl ether $\ce{ROCH2SCH3}$ as a byproduct.

DMSO can also be activated by other electrophiles: $\ce{SO3}$·pyridine (the Parikh–Doering oxidation, which can be run from 0 °C to room temperature) and DCC with acid (the Pfitzner–Moffatt oxidation). The method that generates the chlorosulfonium ion directly from NCS and dimethyl sulfide is called the Corey–Kim oxidation. These methods complement chromium(VI) oxidants ([6.5.10](/6.5.10#sec-10.6.2)) and the **Dess–Martin oxidation** ([6.5.27](/6.5.27#sec-27.7.3)).

### 26.9.3. Other Reactions of Sulfoxides

- Thermal elimination: a sulfoxide with a β-H undergoes syn elimination on heating (about $100$–$150\,^\circ\mathrm{C}$) through a five-membered transition state (the Ei mechanism), giving an alkene and a sulfenic acid RSOH. The selenium analogue, a selenoxide, eliminates at room temperature, so introducing selenium α to a carbonyl group with PhSeCl and then oxidizing with $\ce{H2O2}$ is a common route from aldehydes and ketones to α,β-unsaturated aldehydes and ketones.
- Pummerer rearrangement: a sulfoxide is acylated in acetic anhydride and loses an α-H to give a thionium ion $\ce{RS+=CH2}$; acetate adds to carbon, giving an α-acetoxy sulfide, which amounts to oxidation of the α carbon of a sulfide.
- The [2,3]-**sigmatropic rearrangement** between allylic sulfoxides and sulfenates (the **Mislow–Evans rearrangement**) and the [2,3] shift of sulfonium ylides are treated in [6.5.30](/6.5.30#sec-30.8.4).
- Chiral sulfoxides can serve as **chiral auxiliaries**: the addition of the α-**carbanion** of a sulfoxide to carbonyl compounds shows good diastereoselectivity, and sulfur can afterwards be removed with Raney Ni or by thermal elimination.

![Syn elimination of a selenoxide (Ei): 2-(phenylselanyl)cyclohexanone is oxidized by $\ce{H2O2}$ to the selenoxide, which at room temperature passes through a five-membered transition state in which the oxygen on selenium removes the hydrogen on the adjacent ring carbon (Se and H leave from the same side); the electrons of the C–H bond form the C=C bond and the C–Se bond breaks, giving cyclohex-2-en-1-one and benzeneselenenic acid PhSeOH; thermal elimination of sulfoxides follows the same mechanism but requires heating](./plots/selenoxide-elimination.py)

![The Pummerer rearrangement (methyl phenyl sulfoxide with acetic anhydride, Ac is acetyl): the oxygen of the sulfoxide attacks the carbonyl carbon of the anhydride and acetate leaves, giving an acyloxysulfonium ion; acetate removes a proton from S–CH₃, the electrons of the C–H bond form a C=S bond, the S–O bond breaks and acetate leaves, giving the thionium ion $\ce{PhS+=CH2}$; acetate adds to carbon and the π electrons of C=S return to sulfur, giving the α-acetoxy sulfide](./plots/pummerer.py)

## 26.10. Sulfonic Acids and Their Derivatives

### 26.10.1. Sulfonic Acids, Sulfonyl Chlorides and Sulfonates

A sulfonic acid $\ce{RSO3H}$ is sulfuric acid with one OH replaced by a hydrocarbon group. Benzenesulfonic acid and p-toluenesulfonic acid are obtained by sulfonation of arenes ([6.5.14](/6.5.14#sec-14.8)), and methanesulfonic acid by oxidation of methanethiol or dimethyl disulfide.

- Acidity: sulfonic acids are strong acids; $\mathrm{p}K_{\mathrm{a}}$ of p-toluenesulfonic acid (TsOH) is about $-2.8$, of methanesulfonic acid (MsOH) $-1.9$ and of trifluoromethanesulfonic acid (TfOH) about $-14$ ([6.5.3](/6.5.3#sec-3.1.4)): the negative charge is delocalized over three oxygens. TsOH is a solid, easy to weigh and soluble in organic solvents, and is the most commonly used acid catalyst in organic synthesis (**acetal** formation, esterification, dehydration).
- Sulfonyl chlorides: treatment of a sulfonic acid with $\ce{PCl5}$ or $\ce{SOCl2}$ replaces –OH by chlorine; aryl sulfonyl chlorides can also be obtained directly from arenes and chlorosulfonic acid. Sulfonyl chlorides are **electrophiles**, attacked at sulfur by alcohols and amines to give sulfonates and sulfonamides.

$$
\ce{CH3SO2OH + PCl5 -> CH3SO2Cl + POCl3 + HCl}.
$$

- Sulfonates: alcohols react with TsCl or MsCl in pyridine or triethylamine to give p-toluenesulfonates (tosylates) and methanesulfonates (mesylates). This step breaks only the O–H bond of the alcohol, so the configuration at the alcohol carbon is unchanged; a sulfonate is an excellent **leaving group** (its conjugate acid is a strong acid), and the following **SN2** reaction inverts the configuration at carbon. "Sulfonylation (retention) + SN2 (inversion)" and the Mitsunobu reaction (one-step inversion) are the two standard routes for replacing OH by other groups ([6.5.8](/6.5.8#sec-8.6)). Trifluoromethanesulfonates (triflates, TfO–) are among the best leaving groups, and triflates of enols and phenols are common substrates in **cross-coupling** ([6.5.29](/6.5.29#sec-29.4)).

```smiles
C[C@@H](O)CCCC.Cc1ccc(cc1)S(Cl)(=O)=O>>C[C@@H](OS(=O)(=O)c1ccc(C)cc1)CCCC
C[C@@H](OS(=O)(=O)c1ccc(C)cc1)CCCC.[C-]#N>>C[C@H](C#N)CCCC
```

- Replacement of the sulfonic acid group: arenesulfonic acids lose the sulfonic acid group on heating in dilute acid (sulfonation is reversible, and the sulfonic acid group is often used as a temporary "blocking group", [6.5.14](/6.5.14#sec-14.8)); fusion with NaOH gives phenols ([6.5.15](/6.5.15#sec-15.9)), and fusion with NaCN gives aryl nitriles.

### 26.10.2. Sulfa Drugs

Sulfanilamide (4-aminobenzenesulfonamide) closely resembles 4-aminobenzoic acid (PABA) in shape, size and charge distribution (the distances between the two key atoms are about 0.67 and 0.69 nm, respectively). Bacteria must synthesize folic acid themselves: dihydropteroate synthase attaches PABA to a pteridine, and dihydrofolate synthase then adds glutamate. Sulfanilamide competes with PABA for the active site of dihydropteroate synthase (competitive inhibition), so bacteria lacking folate cannot synthesize nucleotides and stop multiplying; humans take up folate from food and do not need this enzyme, so sulfanilamide is of low toxicity to humans.

```smiles
Nc1ccc(cc1)S(N)(=O)=O
Nc1ccc(cc1)C(=O)O
Cc1cc(NS(=O)(=O)c2ccc(N)cc2)no1
```

The structures above are, in order, sulfanilamide, PABA and sulfamethoxazole (SMZ). The first sulfa drug, Prontosil, is a red azo dye that Domagk found in 1932 to be effective in mice infected with streptococci and published in 1935 (Nobel Prize in Physiology or Medicine, 1939); in the same year Tréfouël and coworkers at the Pasteur Institute showed that it is reduced in the body with cleavage of the azo bond and that the active agent is the metabolite sulfanilamide, one of the first prodrugs to be recognized. Sulfamethoxazole combined with trimethoprim (TMP, which inhibits dihydrofolate reductase, further down the folate pathway) gives co-trimoxazole; the two block the same metabolic pathway in sequence and act synergistically ([7.1](/7.1)).

The synthesis of sulfanilamide is a classic example of a **protecting group**:

```smiles
CC(=O)Nc1ccccc1.OS(=O)(=O)Cl>>CC(=O)Nc1ccc(cc1)S(Cl)(=O)=O
CC(=O)Nc1ccc(cc1)S(Cl)(=O)=O.N>>CC(=O)Nc1ccc(cc1)S(N)(=O)=O
CC(=O)Nc1ccc(cc1)S(N)(=O)=O.O>>Nc1ccc(cc1)S(N)(=O)=O.CC(=O)O
```

Acetanilide (rather than aniline) reacts with chlorosulfonic acid to give 4-acetamidobenzenesulfonyl chloride, which is treated with ammonia and finally hydrolyzed to remove the acetyl group. Acetylation has three effects: it prevents the free amino group from being protonated by chlorosulfonic acid ($\ce{-NH3+}$ is a meta-directing **deactivating group**) or from reacting with the sulfonyl chloride; the acetamido group is still an ortho/para-directing **activating group**, and its bulk directs substitution mainly to the para position; and on hydrolysis the sulfonamide is much more stable than the acetamide, so only the acetyl group can be removed selectively. The N–H of a sulfonamide is somewhat acidic ($\mathrm{p}K_{\mathrm{a}}$ of $\ce{C6H5SO2NH2}$ is 10.1), which affects the solubility of sulfa drugs and their crystallization in urine. The artificial sweetener saccharin is also a cyclic sulfonimide.

### 26.10.3. Alkylbenzenesulfonates and Surfactants

Sodium dodecylbenzenesulfonate ($\ce{C12H25C6H4SO3Na}$) is the anionic **surfactant** used in the largest amounts in laundry powders ([6.3.19](/6.3.19)): the long alkyl chain is hydrophobic and the sulfonate hydrophilic. It is made by sulfonation and neutralization of dodecylbenzene (from the **Friedel–Crafts alkylation** of benzene with dodecene). The highly branched alkylbenzenes obtained in the early days from propylene tetramer gave sulfonates that microorganisms could hardly degrade, causing foam in rivers; today only linear alkylbenzenes (LAS) are used, which are biodegradable. Compared with soap (a carboxylate), the conjugate acid of a sulfonate is a strong acid, and no calcium or magnesium precipitates form in hard water.

## 26.11. Organosulfur Reagents in Synthesis

### 26.11.1. Sulfur-Stabilized Carbanions and Umpolung

Stabilization of an α-**carbanion** by the sulfur atom (Section 26.7.2) is the core of sulfur reagents in synthesis. The α-H atoms of sulfides, dithianes, sulfoxides and sulfones can all be removed by strong bases: sulfides and dithianes need $n$-BuLi, sulfones $n$-BuLi or LDA, and more acidic compounds such as β-keto sulfones and β-disulfones need only NaH or even $\ce{K2CO3}$. The carbanions formed react with alkyl halides, epoxides, aldehydes and ketones and acylating agents, and sulfur can finally be removed:

- Hydrolysis with $\ce{HgCl2}$ (**thioacetal** → carbonyl): the 2-lithio derivative of a 1,3-dithiane is an equivalent of an "acyl anion", a classic example of **umpolung** (Corey–Seebach, [6.5.16](/6.5.16#sec-16.10.2)). A carbonyl carbon can normally be attacked only by **nucleophiles**, but once converted to a thioacetal it becomes a nucleophile itself.
- Hydrogenolysis with Raney Ni (C–S → C–H) or removal of the sulfonyl group by reduction with Na(Hg) or Mg/MeOH: the sulfonyl group first activates the α carbon and is removed after use, a "removable **activating group**".
- Thermal elimination (sulfoxides, selenoxides → alkenes, Section 26.9.3).

Besides dithianes, the carbanions of methylthiomethyl p-tolyl sulfone and methylthiomethyl sulfoxide ($\ce{CH3SCH2S(O)CH3}$) are also equivalents of the formyl anion.

### 26.11.2. Sulfur Ylides

Deprotonation of a sulfonium salt with a strong base (NaH/DMSO, $n$-BuLi) gives a sulfonium ylide $\ce{R2S+-CH2-}$, and deprotonation of trimethylsulfoxonium iodide gives the sulfoxonium ylide $\ce{(CH3)2S(O)+-CH2-}$. Their reactions with aldehydes and ketones (the **Corey–Chaykovsky reaction**) were discussed in [6.5.16](/6.5.16#sec-16.8.3); here we use bond energies to explain how it diverges from the **Wittig reaction**. Both kinds of ylide first add to the carbonyl carbon to give a β-oxido "onium" salt. In the phosphorus ylide adduct the oxide bonds to phosphorus, and because the P–O bond is very strong (about $555\,\mathrm{kJ\,mol^{-1}}$) an alkene and a phosphine oxide are finally formed; in the sulfur ylide adduct the S–O bond is weak (about $360\,\mathrm{kJ\,mol^{-1}}$) and a dialkyl sulfide is a very good **leaving group**, so the oxide instead attacks the $\ce{CH2}$ intramolecularly by **SN2** to give an epoxide.

With α,β-unsaturated ketones, the common rule of thumb is "an unsubstituted sulfur ylide gives the epoxide by 1,2-addition, a substituted one gives the cyclopropane by 1,4-addition"; the more accurate criterion is whether the addition is reversible ([6.5.16](/6.5.16#sec-16.8.3)). The reactive, unstable dimethylsulfonium methylide adds irreversibly to the carbonyl group by **1,2-addition**; ylides stabilized by S=O (sulfoxonium ylides) or by an ester group (such as $\ce{(CH3)2S+-CH-CO2Et}$) add reversibly in a 1,2 fashion and finally give cyclopropanes through irreversible **1,4-addition** (**conjugate addition**) and intramolecular SN2. Substituents on the α carbon correlate with 1,4-selectivity because electron-withdrawing substituents stabilize the ylide and make the addition reversible (Question 5). Sulfur ylides made from chiral sulfides allow catalytic asymmetric epoxidation (Aggarwal).

![Cyclopropanation of cyclohex-2-en-1-one by a sulfoxonium ylide (Corey–Chaykovsky): the stabilized dimethylsulfoxonium methylide adds to the β carbon (conjugate addition; its 1,2-addition to the carbonyl group is reversible), the electrons of C=C move toward the carbonyl group and those of C=O onto oxygen, giving an enolate; the carbon of the enolate attacks the $\ce{CH2}$ attached to sulfur from the back (intramolecular SN2, 3-exo-tet ring closure) and DMSO leaves, giving bicyclo[4.1.0]heptan-2-one](./plots/sulfoxonium-cyclopropanation.py)

### 26.11.3. The Julia Olefination

**Definition 26.11.1 (Julia Olefination)** The reaction in which the α-carbanion of a sulfone adds to an aldehyde (or ketone), and the resulting β-hydroxy sulfone (or its ester) gives an alkene by reductive elimination or by intramolecular rearrangement and elimination, is called the **Julia olefination**.

The classical Julia–Lythgoe olefination (Julia and Paris, 1973; Kocienski and Lythgoe, 1978) has three steps:

1. A phenyl sulfone $\ce{PhSO2CH2R}$ is deprotonated with $n$-BuLi and adds to an aldehyde R′CHO to give the β-oxido sulfone;
2. The oxide is acylated with acetic anhydride or benzoyl chloride to the β-acyloxy sulfone;
3. Reduction with sodium **amalgam** (or $\ce{SmI2}$): the sulfonyl group accepts electrons and leaves, giving a **carbanion** (or radical) intermediate, and the acyloxy group is then eliminated to give the alkene.

```smiles
CCCS(=O)(=O)c1ccccc1.O=CCCC>>CCC(C(O)CCC)S(=O)(=O)c1ccccc1
CCC(C(OC(C)=O)CCC)S(=O)(=O)c1ccccc1>>CC/C=C/CCC
```

The carbanion or radical intermediate of the reduction step can rotate about the C–C bond and equilibrate to the more stable conformation, so whichever diastereomer the β-acyloxy sulfone is, the product is mainly the (E)-alkene, often above 95:5. This complements exactly the Wittig reaction of nonstabilized ylides (Z-selective), and the Julia olefination is therefore often used to construct (E)-disubstituted double bonds in total syntheses of natural products.

The Julia–Kocienski modification (Julia 1991, Kocienski 1998) replaces phenyl by benzothiazol-2-yl (BT) or 1-phenyl-1H-tetrazol-5-yl (PT). The β-oxide is not acylated but attacks the ipso carbon of the heteroaromatic ring directly and intramolecularly (the Smiles rearrangement, an intramolecular **nucleophilic aromatic substitution**), and the aryl group migrates from sulfur to oxygen; the sulfinate formed then eliminates $\ce{SO2}$ and the aryloxide, giving the alkene in one pot without sodium amalgam and with equally high E selectivity.

![The Julia–Kocienski olefination (PT is 1-phenyl-1H-tetrazol-5-yl; R and R′ come from the sulfone and the aldehyde, respectively): after addition of the sulfone anion to the aldehyde, the β-oxide attacks the ipso carbon of the tetrazole (through a spirocyclic Meisenheimer-type intermediate, not drawn), the C–S bond breaks, and the heteroaryl group migrates from sulfur to oxygen (Smiles rearrangement), giving a sulfinate; the sulfinate undergoes anti elimination, releasing $\ce{SO2}$ and the tetrazolyl oxide, to give the (E)-alkene (the anti relationship is set in the addition step)](./plots/julia-kocienski.py)

### 26.11.4. Research Frontiers

The chemistry of sulfur and phosphorus compounds is still developing rapidly. Sulfur-containing drugs make up a considerable share of marketed small-molecule drugs (54 of the top 200 small-molecule drugs by retail sales in 2018 contain sulfur). The sulfur(VI)–fluoride exchange (SuFEx) click chemistry proposed by Sharpless and coworkers (2014) exploits the fact that sulfonyl fluorides are stable in water yet react reliably with **nucleophiles** under specific conditions; it is used both to link molecules and to design probes and drugs that bind covalently to tyrosine and lysine residues of proteins. In phosphorus chemistry, the P(III)/P(V) redox cycle has been used to design reductions catalyzed by organophosphorus compounds (phosphine-catalyzed Wittig, Mitsunobu and Staudinger reactions), replacing classical methods that require stoichiometric phosphine; all of these are direct applications of the "P=O driving force" and of the soft **nucleophilicity** of sulfur discussed in this chapter.

## Summary

- P and S in organoelement compounds (Definition 26.1.1) differ from second-period elements: the atoms are large and easily polarized, their **electronegativity** is close to that of carbon, their π bonds to carbon are weak, they can be five- and six-coordinate, their single bonds to O are strong, and they stabilize an α-**carbanion**. None of these properties needs participation of 3d orbitals for its explanation: P=O, S=O and the P–C bond of ylides are strongly polar σ bonds plus **negative hyperconjugation** of lone pairs into σ* orbitals (Definition 26.3.1).
- Phosphorus:

| Topic | Key points |
|---|---|
| Classification | phosphines (Definition 26.2.1) and phosphonium salts; phosphates, phosphonates, phosphinates, phosphine oxides; phosphites; P(III)/P(V) tautomerism favors the P=O form |
| Configuration | phosphines are pyramidal with an inversion barrier of about 125–150 kJ/mol, so P can be a **stereocenter**; five-coordinate P is a trigonal bipyramid, electronegative ligands occupy axial positions, Berry **pseudorotation** |
| Basicity and **nucleophilicity** | weaker bases than amines ($\ce{Ph3PH+}$ 2.73), stronger soft **nucleophiles** than amines |
| Biology | phosphate diesters are negatively charged and kinetically stable; the 2′-OH of RNA attacks intramolecularly and makes it easy to hydrolyze |
| Reactions driven by P=O | Wittig and HWE (6.5.16); Arbuzov (Definition 26.6.1) to phosphonates; Mitsunobu (Definition 26.6.2) and Appel (Definition 26.6.3) through alkoxyphosphonium ions, **SN2** with inversion; Staudinger reduction (Definition 26.5.1) converts azides into amines; deoxygenation of epoxides and alkene inversion |

- Sulfur:

| Compound | Properties and reactions |
|---|---|
| Thiols (Definition 26.8.1) | about 5 $\mathrm{p}K_{\mathrm{a}}$ units more acidic than alcohols (EtSH 10.6), weak **hydrogen bonds**, foul odor; thiolates are strong nucleophiles and weak bases, giving only SN2; bind soft metals (antidotes BAL, DMSA) |
| Sulfides, sulfonium salts | sulfides are nucleophilic and form sulfonium salts (methyl transfer by SAM); **neighboring group participation** in mustard gas |
| Disulfide bonds (Definition 26.8.2) | thiol ⇌ disulfide redox; thiol–disulfide exchange is SN2 at S; GSH/GSSG buffer, DTT, TCEP |
| Sulfoxides, sulfones (Definition 26.9.1) | sulfoxides are pyramidal and can be chiral; DMSO is a **polar aprotic solvent**; Swern oxidation (Definition 26.9.2); syn thermal elimination of sulfoxides; sulfones stabilize an α-carbanion |
| Sulfonic acids and derivatives | strong acids (TsOH, MsOH, TfOH); sulfonates are good **leaving groups** (configuration retained on formation); sulfa drugs inhibit dihydropteroate synthase; LAS **surfactants** |
| Synthetic reagents | **umpolung** of dithianes; sulfur ylides give epoxides and cyclopropanes (weak S–O bond); the Julia olefination (Definition 26.11.1) gives (E)-alkenes |

## Questions

1. What kind of chemical bond is the P=O in triphenylphosphine oxide? Why is the "d–p π bond" description wrong? Use this picture to explain why $\ce{Ph3P=O}$ is a very strong **hydrogen bond** acceptor and why its P=O bond is much shorter than the P–O single bond in a phosphate ester.

   **Answer** P=O is mainly a strongly polarized σ bond ($\ce{Ph3P+-O-}$) plus **negative hyperconjugation** of the lone pairs of O into the three P–C σ* orbitals (Definition 26.3.1). Calculations show that the 3d orbitals of P are too high in energy and too diffuse, with an occupation of only about 0.1 electron in P=O, so no genuine d–p π bond can form. In this picture O carries a large negative charge, and so is a strong hydrogen bond acceptor and **Lewis base**; negative hyperconjugation also adds some "multiple-bond" character to P–O (three lone pairs delocalize simultaneously, with cylindrical symmetry), so the bond length (about 148 pm) is shorter, and the bond energy larger, than for a P–OR single bond without this interaction (about 160 pm).

2. Compare triethylamine and triethylphosphine: which is the stronger base, and which is the stronger **nucleophile** toward iodomethane? Why does heating a hydroxide of **quaternary ammonium ions** give an alkene, whereas heating benzyltriphenylphosphonium hydroxide gives toluene and triphenylphosphine oxide?

   **Answer** Triethylamine is the stronger base by about a factor of 100 (conjugate acid $\mathrm{p}K_{\mathrm{a}}$ 10.75 versus 8.69), and triethylphosphine is a much stronger nucleophile: P is large and easily polarized, its lone pair is high in energy and weakly solvated, and it is a soft nucleophile that reacts quickly with soft $\mathrm{sp^3}$ carbon. The N of a quaternary ammonium ion cannot expand its coordination number, so $\ce{HO-}$ can only attack a β-H as a base, giving **Hofmann elimination**. The P of a quaternary phosphonium ion can accept attack by $\ce{HO-}$ to form a five-coordinate intermediate, which then expels the most stable **carbanion** (the benzyl anion is more stable than phenyl or alkyl anions) while forming the very strong P=O bond, so toluene and $\ce{Ph3PO}$ are obtained.

3. Starting from 3β-cholestanol, synthesize 3α-aminocholestane and 3β-aminocholestane. How many inversions of configuration does each need? Give the reagents.

   **Answer** The 3α-amine needs one inversion: a Mitsunobu reaction ($\ce{Ph3P}$, DEAD) with phthalimide or $\ce{HN3}$ (or DPPA) as the nucleophile inverts C3 by **SN2** to give the 3α-phthalimide or 3α-azide, which is converted to the 3α-amine by hydrazinolysis (Gabriel) or by Staudinger reduction ($\ce{Ph3P}$, $\ce{H2O}$). Alternatively, the alcohol can first be converted into the mesylate (retention) and then treated with $\ce{NaN3}$ (SN2, inversion), followed by reduction. The 3β-amine needs retention of configuration, that is, two inversions: first a Mitsunobu reaction with 4-nitrobenzoic acid gives the 3α-ester (first inversion), which is hydrolyzed to the 3α-alcohol, and a second Mitsunobu reaction as above (azide or imide, second inversion) followed by reduction gives the 3β-amine. (Another route is oxidation of the alcohol to the ketone followed by **reductive amination**, but the **stereoselectivity** then has to be controlled by the reduction step and the process is not stereospecific.)

4. Denton's catalytic Mitsunobu reaction uses (2-hydroxybenzyl)diphenylphosphine oxide as catalyst and a carboxylic acid as nucleophile, at reflux with removal of water in a Dean–Stark apparatus; it needs neither an azodicarboxylate nor a stoichiometric amount of phosphine. Given that the catalyst exists in equilibrium between four-coordinate and five-coordinate phosphorus, write the catalytic cycle and explain why the reaction is called "redox neutral".

   **Answer** (1) Under the action of acid (the carboxylic acid), the P=O of the catalyst is protonated or interacts with the phenolic OH, the phenolic oxygen attacks phosphorus intramolecularly, and loss of one molecule of water gives a cyclic five-membered alkoxyphosphonium salt (a benzoxaphospholium, with four-coordinate P⁺, in equilibrium with its five-coordinate phosphorane form) with carboxylate as counterion; removal of water drives this step. (2) The substrate alcohol attacks the phosphorus of this phosphonium salt, the ring P–O(aryl) bond breaks and the phenolic OH is restored, giving the alkoxyphosphonium ion $\ce{R-O-P+}$. (3) Carboxylate attacks the alcohol carbon from the back (SN2), giving the ester with inverted configuration and releasing the original phosphine oxide catalyst. The overall reaction is RCOOH + R′OH → RCOOR′ + $\ce{H2O}$; phosphorus remains +5 throughout the cycle (P=O or P⁺–O) and is neither oxidized nor reduced, so no oxidant such as DEAD is needed, $\ce{Ph3PO}$ need not be reduced back to a phosphine, and the only byproduct is water.

5. Write the mechanism for the formation of a cyclopropane from dimethylsulfoxonium methylide and chalcone (1,3-diphenylprop-2-en-1-one). Why does dimethylsulfonium methylide give mainly the epoxide with the same substrate?

   **Answer** The ylide carbon adds to the β carbon of the C=C bond (1,4-addition) and electrons are pushed onto the carbonyl oxygen, giving an **enolate**; the α carbon of the enolate attacks intramolecularly, by SN2, the $\ce{CH2}$ on the positively charged sulfur (the former ylide carbon), DMSO leaves, and the three-membered ring closes, giving 1-benzoyl-2-phenylcyclopropane (mainly trans). The negative charge of the sulfoxonium ylide is stabilized by S=O, and its 1,2-addition to the carbonyl group is reversible, so the adduct can return to the starting materials; the enolate formed by 1,4-addition is more stable and ring closure is irreversible, so the reaction finally flows to the cyclopropane. Dimethylsulfonium methylide is unstable and reactive, its 1,2-addition is fast and irreversible (the adduct closes rapidly to the epoxide), and the product is determined kinetically, mainly the vinyl epoxide.

6. What methods would you use for each of the following transformations? Write the key intermediates. (a) (E)-1,3-Diphenylprop-1-ene from benzyl bromide and phenylacetaldehyde (high E selectivity required); (b) (S)-octan-2-yl acetate → (R)-octan-2-ol; (c) 3-phenylpropan-1-ol → 3-phenylpropanal (no metal oxidants, and the product must not be oxidized further).

   **Answer** (a) Benzyl bromide is heated with $\ce{P(OEt)3}$, and the Arbuzov reaction (two SN2 steps, with an alkoxyphosphonium salt as intermediate) gives diethyl benzylphosphonate with bromoethane distilling off; NaH then generates the benzylphosphonate carbanion (the phenyl group stabilizes the negative charge), which undergoes the **HWE reaction** with phenylacetaldehyde, giving the (E)-alkene through reversible addition and an oxaphosphetane. If the α position of the carbanion carries no stabilizing group such as phenyl or carbonyl (as in a simple alkylphosphonate), the HWE reaction proceeds poorly, and for an (E)-disubstituted alkene the Julia olefination is more appropriate. (b) First hydrolyze (or methanolyze with $\ce{K2CO3}$/MeOH) to give (S)-octan-2-ol (configuration retained, acyl–oxygen bond cleaved), then invert with a Mitsunobu reaction ($\ce{Ph3P}$, DEAD, 4-nitrobenzoic acid) to the (R)-ester, and hydrolyze to (R)-octan-2-ol. (c) Swern oxidation ($\ce{(COCl)2}$, DMSO, $-78\,^\circ\mathrm{C}$, then $\ce{Et3N}$); the intermediates are the chlorodimethylsulfonium ion, the alkoxysulfonium ion and the sulfonium ylide, and since the mixture is anhydrous the aldehyde is not oxidized to the carboxylic acid.

7. Explain: (a) ethanethiol ($\mathrm{p}K_{\mathrm{a}}$ 10.6) is about 5 units more acidic than ethanol (15.9); (b) sodium ethanethiolate with 2-bromobutane in ethanol gives almost only the substitution product, whereas sodium ethoxide with the same substrate gives a large amount of alkene; (c) a thiol left in air at pH 8 gradually forms the disulfide, and adding EDTA slows the process.

   **Answer** (a) The H–S bond is weaker than the H–O bond, and S is large and easily polarized, spreading the negative charge over a larger volume, so $\ce{RS-}$ is more stable than $\ce{RO-}$ and the conjugate acid is stronger. The increase in acidity down a group is determined mainly by bond strength. (b) $\ce{EtS-}$ is a strong soft nucleophile but only weakly basic (conjugate acid $\mathrm{p}K_{\mathrm{a}}$ about 10.6, against about 15.9 for the conjugate acid of $\ce{EtO-}$), so its SN2 reaction at a secondary carbon is much faster than **E2** removal of a β-H; $\ce{EtO-}$ is a strong base and a hard nucleophile, and E2 competes strongly with its substitution on secondary halides. (c) At pH 8 part of the thiol exists as thiolate, which is oxidized by $\ce{O2}$ (through thiyl radicals or electron transfer after coordination to metals), and traces of $\ce{Cu^2+}$ and $\ce{Fe^3+}$ catalyze this process; EDTA chelates these metal ions and suppresses the catalyzed oxidation. This is why sulfhydryl-containing buffers in biochemical experiments often contain EDTA.

8. Write the two steps by which glutathione (GSH) reduces a protein disulfide bond P–S–S–P′. Why is only a slight excess of DTT over the disulfide needed to drive the reduction to completion, whereas a monothiol such as 2-mercaptoethanol usually requires a large excess?

   **Answer** In the first step $\ce{GS-}$ attacks one sulfur of the disulfide: P–S–S–P′ + $\ce{GS-}$ → P–S–SG + $\ce{P'S-}$ (a mixed disulfide); in the second step another $\ce{GS-}$ attacks the sulfur of the mixed disulfide: P–S–SG + $\ce{GS-}$ → $\ce{PS-}$ + GSSG. Both steps are thiol–disulfide exchange (SN2 at S) with equilibrium constants near 1 for each step, so a monothiol must be used in large excess to drive the equilibrium. After the first exchange of DTT, the second sulfhydryl group is right next to the sulfur of the mixed disulfide, so the second step is intramolecular and forms a stable six-membered cyclic disulfide (trans-4,5-dihydroxy-1,2-dithiane); the **equilibrium constant** is very large ($E^{\circ\prime} = -0.33\,\mathrm{V}$, more negative than $-0.24\,\mathrm{V}$ for GSH), so nearly stoichiometric DTT reduces the disulfide completely.

9. Why must aniline be acetylated first in the synthesis of sulfanilamide (4-aminobenzenesulfonamide) from aniline? Explain why the last step hydrolyzes only the acetamide and not the sulfonamide.

   **Answer** Free aniline is protonated in chlorosulfonic acid to the anilinium ion, and $\ce{-NH3+}$ is a deactivating group with a meta **directing effect**; even if not protonated, the amino group would react with the sulfonyl chloride formed, giving sulfonamides and polymers. Acetylation converts the amino group into an acetamido group that is still ortho/para-directing but of moderate activity; its bulk directs substitution mainly to the para position, and N is no longer nucleophilic. In the final hydrolysis with dilute acid or base, the carbonyl carbon of the acetamide is a normal center for **nucleophilic acyl substitution**; the sulfur of the sulfonamide is a tetrahedral S(VI), attack on it requires a five-coordinate intermediate, and its hydrolysis is much slower than that of a carboxamide, so only the acetyl group is removed selectively.

10. In which of the following reactions is the formation of the P=O bond, or the breaking and formation of S–O bonds, the main driving force? (a) The **Wittig reaction**; (b) the Swern oxidation; (c) the Corey–Chaykovsky epoxidation; (d) the Staudinger reduction; (e) the Julia–Lythgoe olefination.

    **Answer** (a) Formation of $\ce{Ph3P=O}$: yes. (b) The S–O bond in DMSO is broken, sulfur is reduced to dimethyl sulfide, and the alcohol is oxidized; the driving force is the formation of the very strong C=O bond and of stable small molecules ($\ce{Me2S}$, CO, $\ce{CO2}$, $\ce{Et3NH+Cl-}$), and the release of CO and $\ce{CO2}$ in the activation step makes activation irreversible. (c) No S–O bond is formed: the S–O bond is weak, and dimethyl sulfide leaves as a **leaving group** in the intramolecular SN2 substitution, driven by formation of the C–O bond and release of the stable sulfide. (d) Formation of $\ce{N2}$ and (after hydrolysis) $\ce{Ph3P=O}$: yes. (e) No P is involved; the sulfonyl group leaves as sulfinate in the reduction, driven by the electrons supplied by the reducing agent (Na/Hg) and by formation of the C=C bond.
