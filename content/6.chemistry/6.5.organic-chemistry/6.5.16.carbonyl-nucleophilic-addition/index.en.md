---
title: Nucleophilic Addition to Aldehydes and Ketones
source_hash: d92e680b0bee
---

The carbonyl group, C=O, is the most important functional group in organic chemistry: the chemistry of aldehydes and ketones, carboxylic acids and their derivatives, sugars, and many biomolecules is built on its reactions. In contrast to the π bond of an alkene, the π bond of a carbonyl group is strongly polarized and the carbon end is electron-poor, so the characteristic reaction of aldehydes and ketones is not electrophilic addition but nucleophilic addition, in which a **nucleophile** attacks the carbonyl carbon. This chapter begins with the structure of the carbonyl group and its **frontier orbitals**, and then discusses the thermodynamics of nucleophilic addition, the trajectory of attack (the Bürgi–Dunitz angle), acid and base catalysis, reactivity, and stereochemistry (the Felkin–Anh model, which draws on the **conformational analysis** of [6.5.4](/6.5.4#sec-4.2) and the Re/Si faces of [6.5.5](/6.5.5#sec-5.9.2)). It then treats additions of oxygen, sulfur, carbon, and nitrogen nucleophiles in turn, and ends with umpolung, the strategy that turns the carbonyl carbon into a nucleophilic center. Addition of hydride (reduction), oxidation, and the conjugate addition to α,β-unsaturated aldehydes and ketones are covered in the next chapter, [6.5.17](/6.5.17); reactions at the α carbon (enols and enolates) are in [6.5.21](/6.5.21) and [6.5.22](/6.5.22); nucleophilic acyl substitution of carboxylic acid derivatives is in [6.5.19](/6.5.19). Acetals (glycosides), imines (Schiff bases), and the umpolung chemistry of vitamin B1 recur throughout biochemistry, so this chapter emphasizes their mechanisms.

## 16.1. Structure and Nomenclature of Aldehydes and Ketones

### 16.1.1. Structure of the Carbonyl Group

The carbonyl carbon bonds through $\mathrm{sp^2}$ **hybrid orbitals** and lies in one plane with its three substituents, with bond angles close to $120^\circ$. The C=O bond length is about $121\,\mathrm{pm}$, shorter than that of a C–O single bond ($143\,\mathrm{pm}$). The **electronegativity** of oxygen is greater than that of carbon (Pauling values 3.44 and 2.55), so both the σ and the π electrons are drawn toward oxygen and the carbonyl group has a large dipole moment: $2.33\,\mathrm{D}$ for formaldehyde and $2.88\,\mathrm{D}$ for acetone (CRC). The polarization is represented by two **resonance structures**:

```smiles
CC(C)=O.C[C+](C)[O-]
```

The charge-separated structure on the right contributes less, but it shows the two kinds of reactivity of the carbonyl group. The carbon end is an electrophilic center that accepts nucleophiles; the oxygen end carries a partial negative charge and two lone pairs, and is the site of Brønsted basicity and of **Lewis base** behavior, binding a proton or a **Lewis acid**. Once oxygen is protonated or coordinated to a Lewis acid, the positive character of the carbonyl carbon increases further (calculated partial charge on C: about $+0.5$ for formaldehyde, about $+0.6$ after protonation), which is the basis of acid catalysis. Protonated aldehydes and ketones are, however, very strong acids ($\mathrm{p}K_{\mathrm{a}}$ about $-7$ to $-8$, [Table 3.1 in 6.5.3](/6.5.3#sec-3.1.4)), so only a tiny fraction of the carbonyl groups is protonated in dilute acid.

Three molecular orbitals of the carbonyl group (**molecular orbital theory**, [6.1.3](/6.1.3); the Hückel treatment of π systems is in [6.5.2](/6.5.2#sec-2.2)) are relevant to reactivity:

| Orbital | Character | Chemical significance |
|---|---|---|
| π (C=O bonding) | Polarized toward O, low in energy | Much lower than the π orbital of C=C, so the carbonyl group is not readily attacked by electrophiles |
| n (oxygen lone pair) | Lies in the molecular plane; the **highest occupied molecular orbital** | Interacts with $\ce{H+}$ and Lewis acids (coordination in the plane, along the lone-pair direction) |
| π* (C=O antibonding) | Large coefficient on C; the **lowest unoccupied molecular orbital** | Lower than the π* of C=C; accepts electrons from the nucleophile, which attacks carbon from above or below the plane |

Because the π* orbital is low in energy and has a large coefficient on carbon, carbonyl compounds react with nucleophiles far more readily than alkenes do; the HOMO (π) of an alkene is high in energy, and alkenes react with electrophiles ([6.5.11](/6.5.11#sec-11.1.3)). The n→π* transition of the carbonyl group is a weak, symmetry-forbidden absorption (acetone: $\lambda_{\max} \approx 280\,\mathrm{nm}$, $\varepsilon \approx 15\,\mathrm{L\,mol^{-1}\,cm^{-1}}$); its origin and solvent effects are discussed in [6.4.9](/6.4.9). The main spectroscopic evidence for aldehydes and ketones is the C=O stretching vibration in the infrared (about $1715\,\mathrm{cm^{-1}}$ for saturated ketones and about $1730\,\mathrm{cm^{-1}}$ for aldehydes, which also show two aldehyde C–H bands at $2720$ and $2820\,\mathrm{cm^{-1}}$), the aldehyde proton in the ¹H NMR spectrum ($\delta$ 9–10), and the carbonyl carbon in the ¹³C NMR spectrum ($\delta$ 190–220) ([6.5.6](/6.5.6#sec-6.4.2)).

### 16.1.2. Nomenclature

Aldehydes and ketones are named by the substitutive nomenclature of [6.5.1](/6.5.1#sec-1.4). The suffix of an aldehyde is -al; the aldehyde carbon is counted in the main chain and numbered 1. When the aldehyde group is attached to a ring, the suffix -carbaldehyde is used. The suffix of a ketone is -one, and the position of the carbonyl group must be given. An aldehyde ranks above a ketone in the order of principal characteristic groups, and both rank above alcohols and amines (the [priority table in 6.5.1](/6.5.1#sec-1.4.2)); as prefixes, the aldehyde group is formyl and the =O of a ketone is oxo.

```smiles
CCCCC(=O)CC 1
CC(C)C(O)CC=O 2
O=CC1CCCCC1 3
CC(=O)CCC(=O)O 4
CC(=O)c1ccccc1 5
O=C(c1ccccc1)c1ccccc1 6
```

| No. | Name | Remark |
|---|---|---|
| 1 | heptan-3-one | Numbered from the end nearer the carbonyl group |
| 2 | 3-hydroxy-4-methylpentanal | The aldehyde has priority and OH is a prefix; hydroxy precedes methyl alphabetically |
| 3 | cyclohexanecarbaldehyde | The aldehyde carbon is not counted in the ring |
| 4 | 4-oxopentanoic acid | Trivial name levulinic acid; the carboxylic acid has priority and the ketone is a prefix |
| 5 | 1-phenylethan-1-one | Trivial name acetophenone |
| 6 | diphenylmethanone | Trivial name benzophenone |

The retained names in common use are formaldehyde, acetaldehyde, benzaldehyde, and acetone (the preferred IUPAC name). Ketones are also classified by whether the two groups on the carbonyl group are the same (simple ketones such as acetone) or different (mixed ketones such as acetophenone); this is merely a customary distinction.

Aldehydes and ketones cannot form **hydrogen bonds** among themselves, so their boiling points are higher than those of alkanes and ethers of similar molar mass but lower than those of alcohols. Their oxygen atoms accept hydrogen bonds, and the lower aldehydes and ketones (formaldehyde, acetaldehyde, acetone) are miscible with water. Formaldehyde (annual world production of tens of millions of tonnes, mainly for urea–formaldehyde and phenol–formaldehyde resins) and acetone (a solvent and a feedstock for bisphenol A and methyl methacrylate) are the aldehyde and ketone produced in the largest quantities.

## 16.2. General Principles of Nucleophilic Addition

### 16.2.1. Thermodynamics and Reversibility of Addition

**Definition 16.2.1 (Nucleophilic Addition)** A nucleophile $\ce{Nu-}$ (or a neutral molecule with a lone pair) attacks the electron-poor atom of an unsaturated bond, the π electrons move onto the more electronegative atom, and this atom then combines with an electrophile (usually a proton). The net result is that Nu and E add to the two atoms that were originally unsaturated. This type of reaction is called **nucleophilic addition**.

Nucleophilic addition to a carbonyl group converts the trigonal planar $\mathrm{sp^2}$ carbon into a tetrahedral $\mathrm{sp^3}$ carbon, and the product $\ce{R2C(OH)Nu}$ is often called the tetrahedral adduct. Three points distinguish the position of equilibrium from that in additions to C=C:

- The π bond of C=O is strong. From the average bond enthalpies of [6.1.3](/6.1.3), the π part of C=O is about $745 - 358 \approx 390\,\mathrm{kJ\,mol^{-1}}$, far more than the roughly $264\,\mathrm{kJ\,mol^{-1}}$ of C=C. The enthalpy change for addition of H–X (X = OH, OR, NHR, CN, $\ce{SO3-}$) to a carbonyl group is therefore small, and together with the entropy loss of combining two molecules into one, the equilibrium constant is usually close to or smaller than 1. Such additions are reversible, and the products often react further (loss of water, substitution), so the position of equilibrium must be controlled by concentration, removal of water, and similar means (Sections 16.5 and 16.9).
- The C–metal bond is weak. Addition of organolithium and Grignard reagents to aldehydes and ketones breaks a weak, polar C–M bond and forms strong C–C and O–M bonds. It is strongly exothermic and practically irreversible; so is addition of hydride reagents ($\ce{LiAlH4}$, $\ce{NaBH4}$, [6.5.17](/6.5.17#sec-17.1.1)). Additions of carbanions and hydride are therefore under kinetic control, and the product ratio reflects the energies of the transition states (Section 16.4).
- Substituents. On addition the bond angle is compressed from $120^\circ$ to about $109.5^\circ$ and the substituents move closer together: the larger the substituents, the more crowded the adduct (Section 16.3).

According to what happens after the addition, nucleophilic additions to aldehydes and ketones fall into three types:

| Type | Process | Examples | Reversibility |
|---|---|---|---|
| Simple addition | Nu adds to carbon; O accepts a proton or metal | Hydration, HCN, $\ce{NaHSO3}$, organometallics, hydride | The first three are reversible; the last two are not |
| Addition followed by substitution | The OH of the tetrahedral adduct is protonated and leaves; a second nucleophile substitutes | Alcohols and thiols give acetals and thioacetals | Reversible (acid-catalyzed) |
| Addition followed by elimination | The tetrahedral adduct loses water to give a new C=N or C=C bond | Primary amines give imines and secondary amines give enamines; Wittig reaction | Imines and enamines: reversible; Wittig: irreversible |

### 16.2.2. Direction of Attack: The Bürgi–Dunitz Angle

The HOMO of the nucleophile (a lone pair or a C–M σ bond) must overlap with the π* orbital of the carbonyl group. The lobe of π* on carbon is perpendicular to the molecular plane, but it is out of phase with the lobe on oxygen. Attack from directly above ($90^\circ$) would therefore also give repulsive overlap with the out-of-phase lobe on oxygen, and the most favorable direction is tilted away from the oxygen side, making an obtuse angle with the C=O bond.

**Definition 16.2.2 (Bürgi–Dunitz Angle)** When a nucleophile attacks a carbonyl carbon, it approaches the carbon atom above or below the carbonyl plane, and the angle between the Nu···C direction and the C=O bond is about $107^\circ$ ($105^\circ$–$110^\circ$). This angle is called the **Bürgi–Dunitz angle**, and the corresponding path of attack is called the Bürgi–Dunitz trajectory.

In 1973–1974, Bürgi, Dunitz, and Lehn compared close intramolecular N···C=O and O···C=O contacts in many crystal structures: the shorter the distance, the more the carbonyl carbon is displaced out of the plane (pyramidalized), and the directions of contact cluster around $107^\circ$. These "frozen reaction paths" agree with ab initio calculations. The Bürgi–Dunitz angle underlies many stereochemical phenomena in this chapter: the Felkin–Anh model (Section 16.4.2), axial attack on cyclohexanones ([6.5.17](/6.5.17#sec-17.1.2)), and axial attack of sulfur ylides (Section 16.8.3). If a nucleophile cannot approach along this path because of steric constraints (for example, when it is hemmed in by large groups on both sides), the reaction is very slow.

![The π* orbital of formaldehyde (large lobe on carbon, out of phase with the lobe on oxygen) and the direction of nucleophilic attack: Nu approaches the carbon atom from above the plane at about 107° to the C=O bond](./plots/burgi-dunitz.py)

### 16.2.3. Acid and Base Catalysis

Nucleophilic addition proceeds under three kinds of conditions with different mechanisms:

- Basic (or neutral) conditions, strong nucleophiles. A negatively charged nucleophile ($\ce{HO-}$, $\ce{CN-}$, $\ce{RS-}$, $\ce{R-}$, $\ce{H-}$) attacks the carbonyl carbon directly to give an alkoxide, which then takes a proton from the solvent or from an acid. The rate-determining step is usually the nucleophilic attack.
- Acidic conditions, weak nucleophiles. The acid first protonates the carbonyl oxygen (or a Lewis acid coordinates to it), giving a more positively charged oxonium ion (one resonance structure is a carbocation), and only then can a neutral, weak nucleophile ($\ce{H2O}$, ROH) attack; a proton is then lost. Protonation occurs on the in-plane lone pair of oxygen (the n orbital), not on the π bond.
- General acid–base catalysis. In buffered solutions, proton transfer often occurs simultaneously with C–Nu bond formation (in hydration, for example, one water molecule attacks while another transfers a proton to oxygen at the same time); the transition state contains a cyclic proton-transfer channel formed by several water molecules. This kind of catalysis is most common in the active sites of enzymes.

The two modes of catalysis have the following limits: acidic nucleophiles and strong bases cannot coexist, and basic nucleophiles ($\ce{RMgX}$, $\ce{RLi}$, $\ce{LiAlH4}$) cannot be used in acid; the addition of amines requires weakly acidic conditions between the two extremes (Section 16.9.1).

![Hydration of a carbonyl group. Top: base catalysis; $\ce{HO-}$ adds to the carbonyl carbon, and the alkoxide takes a proton from water and regenerates $\ce{HO-}$. Bottom: acid catalysis; after protonation of the carbonyl oxygen, a neutral water molecule attacks, and loss of a proton gives the gem-diol](./plots/hydration.py)

## 16.3. Reactivity

The reactivity of aldehydes and ketones toward nucleophilic addition is determined by two factors, electronic and steric:

1. Electronic effects. Alkyl groups donate electrons to the carbonyl carbon through **hyperconjugation** and a weak **inductive effect**, stabilizing the carbonyl group and lowering the positive character of carbon. Aryl groups and C=C double bonds conjugate with the carbonyl group through the **conjugation effect** and stabilize it further (the conjugation is lost on addition). Electron-withdrawing groups ($\ce{CCl3}$, $\ce{CF3}$, another carbonyl group) destabilize the carbonyl group and favor addition.
2. Steric effects. Addition changes carbon from three-coordinate to four-coordinate, the bond angles decrease, and large groups crowd one another; the approaching nucleophile is also hindered by the substituents.

Taken together, the order of reactivity is

$$
\ce{HCHO} > \ce{RCHO} > \ce{ArCHO} \approx \ce{R2CO} > \ce{ArCOR} > \ce{Ar2CO}
$$
that is, aldehydes are more reactive than ketones, aliphatic compounds are more reactive than aromatic ones, and electron-poor ones are the most reactive. The equilibrium constant of hydration is the most direct measure of this trend (25 °C, $K_{\mathrm{hyd}} = [\text{hydrate}]/[\text{carbonyl compound}]$, with the activity of water taken as 1):

| Compound | $K_{\mathrm{hyd}}$ | Form in aqueous solution |
|---|---|---|
| Acetone | $1.4\times10^{-3}$ | Almost entirely the ketone |
| Acetaldehyde | about 1.2 | About half is hydrate |
| Formaldehyde | $2.3\times10^{3}$ | Almost entirely the hydrate (methanediol) |
| Trichloroacetaldehyde | about $3\times10^{4}$ | Stable hydrate (chloral hydrate, crystalline) |
| Hexafluoroacetone | about $1\times10^{6}$ | Stable hydrate |
| Cyclopropanone | very large | Exists as the hydrate |

The hydration of cyclopropanone illustrates a further factor, ring strain. The ideal bond angle of an $\mathrm{sp^2}$ carbon is $120^\circ$, but in a three-membered ring it is only about $60^\circ$; on becoming $\mathrm{sp^3}$ the **angle strain** is reduced ([6.5.4](/6.5.4#sec-4.3.3)), so small-ring ketones add nucleophiles especially easily. Addition to cyclohexanone is also easier than to open-chain ketones (addition relieves the eclipsing interactions between the carbonyl group and the adjacent C–H bonds), whereas cyclopentanone is less reactive.

## 16.4. Stereochemistry of Addition

### 16.4.1. The Two Faces of a Prochiral Carbonyl Group

The carbonyl carbon is a trigonal planar **prochiral** center: if the groups on the two sides of the carbonyl group are different ($\ce{RCOR'}$ or $\ce{RCHO}$), a nucleophile (different from R and R′) that attacks from the two faces gives a pair of enantiomeric stereocenters. By the definition in [6.5.5](/6.5.5#sec-5.9.2), the two faces are the **Re face** and the Si face. If the molecule has no other source of chirality, the two faces are entirely equivalent (**enantiotopic**) and the product is racemic. To obtain a single enantiomer, a chiral reagent, catalyst, or enzyme must be introduced (such as the **CBS reduction** of [6.5.17](/6.5.17#sec-17.2.1), or the face-selective transfer of hydride from $\ce{NADH}$ by alcohol dehydrogenase).

If the substrate itself has a stereocenter (usually on the α carbon of the carbonyl group), the two faces are diastereotopic, and attack at the two faces gives a pair of **diastereomers**, generally in unequal amounts; this is substrate-controlled **stereoselectivity**. The models for predicting this selectivity have evolved through several generations.

### 16.4.2. The Cram Rule and the Felkin–Anh Model

Cram (1952) gave the first empirical rule: the three groups on the α carbon are classified by size as L (large), M (medium), and S (small); in the reactive conformation the carbonyl oxygen (which is bulky when coordinated to the metal of the reagent) is eclipsed with L, and the nucleophile attacks from the side of S. This rule gives the correct major product in most cases, but the reactive conformation it assumes is eclipsed, in conflict with the principle of avoiding **torsional strain**, and it cannot explain the results when an electronegative group is on the α carbon. Karabatsos (1967) and Felkin (1968) proposed staggered transition-state models, and Anh and Eisenstein (1977) combined them with the Bürgi–Dunitz trajectory on the basis of orbital theory; this is the model in general use today.

**Definition 16.4.1 (Felkin–Anh Model)** When an aldehyde or ketone with an α stereocenter is attacked by a nucleophile, in the favored transition state the large group L on the α carbon is perpendicular to the carbonyl plane, in the position anti-periplanar to the nucleophile; the nucleophile approaches the carbonyl carbon along the Bürgi–Dunitz trajectory on the side of the small group S (rather than the medium group M). The model that predicts the major diastereomer in this way is called the **Felkin–Anh model**.

![Newman projections, viewed along the α-carbon–carbonyl-carbon bond, of the Felkin–Anh model (left) and the Cram chelation model (right). Left: the large group L is perpendicular to the carbonyl plane and Nu attacks at about 107° past the small group S. Right: the metal coordinates to both the carbonyl oxygen and the α-alkoxy group, locking an eclipsed conformation, and Nu attacks from the side of S to give the anti-Felkin product](./plots/felkin-anh.py)

The model rests on two arguments. (1) In the staggered conformation, the attacking nucleophile is anti to L, so crowding near the forming Nu–C bond is minimal (Felkin's torsional-strain argument). (2) Anh pointed out that the σ* orbital of the C–L bond anti to the forming Nu–C bond can interact with it and lower the energy of the transition state, so the bond in this position should be the one with the lowest-energy σ*. Of the two staggered conformations with L perpendicular to the carbonyl plane, Nu attacking along $107^\circ$ passes closer to either M or S, and passing S is the more favorable.

**Example 16.4.1** Addition of $\ce{CH3MgI}$ to (S)-2-phenylpropanal. On the α carbon, L = Ph, M = $\ce{CH3}$, S = H. According to the Felkin–Anh model, methyl attacks past H, and the major product is (2S,3S)-3-phenylbutan-2-ol, in a ratio of about 2:1 to the minor diastereomer (Cram's 1952 data). Modest selectivity is typical: when M and S on the α carbon differ little in size, the diastereoselectivity is only 2:1 to 5:1.

There are two important extensions:

- The polar Felkin–Anh model. When the α carbon carries an electronegative group (halogen, OR, $\ce{NR2}$), the σ* orbital of the C–X bond is low in energy, and this group occupies the position of L (anti to Nu) regardless of its size. This also explains the selectivity of α-halo ketones. Cornforth and coworkers (1959) explained the same phenomenon by dipole repulsion: the conformation in which the C=O and C–Cl dipoles are antiparallel is the most stable, and the nucleophile attacks from the side of the small group. The two models give the same prediction for most substrates, and recent calculations favor a modified Cornforth conformation (Evans and coworkers, 2003).
- The Cram chelation model. When there is a group that can coordinate to a metal (OR, OBn, $\ce{NR2}$) at the α or β position, and the reagent or an additive contains a metal that can chelate ($\ce{Mg^2+}$, $\ce{Zn^2+}$, $\ce{Ti^4+}$, $\ce{Ce^3+}$), the metal coordinates to both the carbonyl oxygen and the heteroatom, forming a five-membered (or six-membered) **chelate** ring that holds C=O and C–OR in an eclipsed conformation on the same side; the nucleophile attacks from the side of the smaller of the two remaining groups. The product is the opposite of that predicted by the polar Felkin–Anh model (the "anti-Felkin" product). With a bulky silyl ether protecting group (TBS, TIPS, which cannot coordinate) or a reagent that cannot chelate, Felkin selectivity returns, so either diastereomer of the same substrate can be obtained selectively.

```smiles
CC(OCc1ccccc1)C(C)=O>>CC(OCc1ccccc1)C(C)(O)CCCC
```

In this reaction, the α-benzyloxy ketone adds $n$-BuMgBr in THF to give the syn diol monoether under chelation control, with a diastereoselectivity of up to 99:1; with a similar ketone bearing α-OTBS the selectivity is reversed and lower.

The α stereocenter of an aldehyde or ketone can undergo **racemization** by enolization under basic or acidic conditions ([6.5.21](/6.5.21#sec-21.2.3)), so these reactions should be run at low temperature with no excess of base.

## 16.5. Oxygen Nucleophiles

### 16.5.1. Hydration

Addition of water to an aldehyde or ketone gives a geminal diol (gem-diol), the hydrate of the carbonyl compound. The position of equilibrium is determined by the factors of Section 16.3; both acid and base catalyze the reaction but do not change the equilibrium constant (see the scheme in Section 16.2.3). A gem-diol generally cannot be isolated, because the equilibrium returns to the carbonyl compound when the water is removed. The exceptions are the hydrates of compounds with strongly electron-withdrawing groups: chloral hydrate $\ce{CCl3CH(OH)2}$ (the first synthetic sedative-hypnotic drug) and ninhydrin hydrate (the reagent that gives a color with amino acids). Commercial formaldehyde is a solution of about 37% in water (formalin), in which formaldehyde exists almost entirely as methanediol and the oligomers $\ce{HO(CH2O)_nH}$.

When an aldehyde or ketone is treated with $\ce{H2^{18}O}$, the carbonyl oxygen exchanges rapidly with $\ce{^{18}O}$, which is evidence that hydration is reversible and passes through the symmetrical gem-diol.

### 16.5.2. Hemiacetals and Acetals

Like water, an alcohol adds to an aldehyde or ketone to give a hemiacetal (from an aldehyde) or a hemiketal (from a ketone); under acid catalysis, the hemiacetal reacts with a second molecule of alcohol with loss of water to give an acetal.

**Definition 16.5.1 (Hemiacetals and Acetals)** A compound $\ce{R2C(OH)OR'}$ in which one carbon atom carries one OH and one OR group is called a **hemiacetal**. A compound $\ce{R2C(OR')2}$ in which one carbon atom carries two OR groups is called an **acetal**. Those derived from ketones are also called hemiketals and ketals, respectively (IUPAC now classifies all of them as hemiacetals and acetals).

Acetal formation takes place in two stages (scheme). (1) Acid-catalyzed addition gives the hemiacetal, in a manner similar to hydration, with an equilibrium constant usually smaller than 1. (2) The OH of the hemiacetal is protonated and leaves as water, giving an oxocarbenium ion stabilized by the lone pair of oxygen; a second molecule of alcohol attacks it and a proton is lost. The C–O bond cleavage in the second stage is of the SN1 type, and the rate-determining step is the formation of the oxocarbenium ion: OH itself is a very poor leaving group, and the acid converts it into the good leaving group $\ce{H2O}$. Base cannot catalyze the second stage because it cannot make $\ce{HO-}$ leave, so only the hemiacetal is formed in basic solution.

![Acid-catalyzed acetal formation: the carbonyl group is protonated, the alcohol adds, and loss of a proton gives the hemiacetal; the OH is protonated and water leaves to give an oxocarbenium ion, which is attacked by a second molecule of alcohol and deprotonated to give the acetal. Every step is reversible, and the reverse process is the acid-catalyzed hydrolysis of the acetal](./plots/acetal.py)

Every step is reversible, and formation and hydrolysis of acetals are the two directions of one equilibrium:

$$
\ce{R2C=O + 2R'OH <=>[H+] R2C(OR')2 + H2O}
$$
By **Le Chatelier's principle**, to obtain the acetal one uses a large excess of alcohol and removes water (a Dean–Stark trap with azeotropic benzene or toluene, molecular sieves, triethyl orthoformate; Section 16.5.4); to hydrolyze an acetal one works in aqueous acid. Aldehydes form acetals readily, but the equilibrium for simple ketones with monohydric alcohols is very unfavorable (loss of entropy: three molecules become two). The formation of five- and six-membered cyclic ketals with ethane-1,2-diol and propane-1,3-diol (1,3-dioxolanes and 1,3-dioxanes), however, is favorable, because addition of the second OH is intramolecular and the entropy loss is much smaller.

```smiles
O=C1CCCCC1.OCCO>>C1CCC2(CC1)OCCO2
```

Intramolecular hemiacetals are particularly stable. When a hydroxy group and a carbonyl group can form a five- or six-membered ring, the equilibrium between the open-chain form and the cyclic hemiacetal lies on the side of the ring: more than 99% of glucose in aqueous solution exists as the cyclic pyranose hemiacetal. The chemistry of the anomeric carbon of sugars, glycosides (which are acetals), and glycosidic bonds is in [6.5.32](/6.5.32). Bicyclic intramolecular ketals are common among insect pheromones; for example, frontalin, the aggregation pheromone of bark beetles, is obtained by intramolecular ketalization of a dihydroxy ketone in acid:

```smiles
CC(=O)CCCC(C)(O)CO>>CC12CCCC(C)(OC1)O2
```

### 16.5.3. Acetals as Protecting Groups

Acetals are stable toward bases, nucleophiles, hydride reducing agents, organometallic reagents, and most oxidants (they are ethers), but they are readily hydrolyzed back to the carbonyl compound in aqueous acid. These are exactly the properties required of a protecting group.

**Definition 16.5.2 (Protecting Group)** In the synthesis of a polyfunctional molecule, a functional group is first converted reversibly into a derivative that is stable under the conditions of a reaction to be carried out elsewhere in the molecule, and the original group is restored quantitatively after the reaction is complete. The group introduced in this derivative is called a **protecting group** of that functional group.

A good protecting group must meet the following requirements: it is introduced and removed in high yield under mild conditions; it is stable under the intended reaction conditions; and it introduces no new stereocenter (or at least causes no separation problems). The most common protecting group for a carbonyl group is the ethane-1,2-diol ketal (a 1,3-dioxolane), introduced with TsOH catalysis and Dean–Stark removal of water in toluene and removed with dilute acid in acetone–water.

**Example 16.5.1** Synthesis of 5-hydroxypentan-2-one from ethyl 4-oxopentanoate (ethyl levulinate). Direct reduction with $\ce{LiAlH4}$ would reduce both the ketone and the ester. The ketone is first protected as the ethane-1,2-diol ketal, then $\ce{LiAlH4}$ reduces the ester to a primary alcohol, and finally the ketal is hydrolyzed in dilute acid:

```smiles
CCOC(=O)CCC(C)=O>>CCOC(=O)CCC1(C)OCCO1
CCOC(=O)CCC1(C)OCCO1>>OCCCC1(C)OCCO1
OCCCC1(C)OCCO1>>CC(=O)CCCO
```

Conversely, an aldehyde group can be protected while an alkene is oxidized: acrolein is first converted to its diethyl acetal with ethanol in dry HCl, the double bond is then dihydroxylated with cold dilute permanganate, and hydrolysis of the acetal finally gives glyceraldehyde. Without protection, the aldehyde group would be oxidized first. A summary of the choice of protecting groups and of orthogonal protection (protecting groups removed one at a time under mutually compatible conditions) is in [6.5.20](/6.5.20#sec-20.8.3).

### 16.5.4. Orthoesters

An orthoacid $\ce{RC(OH)3}$ is the form of a "hydrate" of a carboxylic acid and cannot exist, but its esters, the orthoesters $\ce{RC(OR')3}$, are stable compounds. Triethyl orthoformate $\ce{HC(OC2H5)3}$ is prepared from chloroform and sodium ethoxide:

```smiles
ClC(Cl)Cl.CC[O-]>>CCOC(OCC)OCC
```

Under acid catalysis, an orthoester exchanges alkoxy groups with an aldehyde or ketone to give the acetal (ketal) and ethyl formate:

```smiles
CC(C)=O.CCOC(OCC)OCC>>CCOC(C)(C)OCC.CCOC=O
```

The beauty of this reaction is that it "consumes" the water that is formed (the orthoester is hydrolyzed to an ester and an alcohol) and so drives the equilibrium toward the ketal; it is therefore especially useful for ketones that form ketals with difficulty, and orthoesters are also common chemical drying agents. Orthoesters are stable to base and hydrolyzed rapidly in dilute acid, so they can serve as protecting groups for carboxylic acids (for example, OBO esters).

## 16.6. Sulfur Nucleophiles

### 16.6.1. Addition of Sodium Hydrogen Sulfite

Aldehydes, aliphatic methyl ketones, and cyclic ketones with fewer than eight carbon atoms react with saturated sodium hydrogen sulfite solution to give white crystalline sodium α-hydroxysulfonates. The nucleophilic atom is sulfur: the lone pair on S in sulfite is more polarizable (softer) than that on O and attacks the carbonyl carbon to form a C–S bond.

```smiles
CC(C)=O.O=S([O-])O>>CC(C)(O)S(=O)(=O)[O-]
```

![Addition of hydrogensulfite to acetone: the polarizable lone pair on sulfur (not oxygen) attacks the carbonyl carbon and the C=O $\pi$ electrons move onto oxygen; proton transfer from the $\ce{SO3H}$ group to the alkoxide gives the α-hydroxysulfonate](./plots/bisulfite.py)

The adduct dissolves in water but not in organic solvents or in saturated sodium hydrogen sulfite solution; on addition of dilute acid (releasing $\ce{SO2}$) or sodium carbonate (forming $\ce{CO2}$) it decomposes back to the original aldehyde or ketone. The reaction can be used to separate and purify aldehydes and methyl ketones from other organic compounds. The reason for the limited scope is the same as for cyanohydrins: the enthalpy change of addition of S is small (the S–O and S=O bonds are both weak), the equilibrium is sensitive to steric hindrance, and bulkier ketones hardly react; the use of "excess, saturated" sodium hydrogen sulfite serves to push the equilibrium toward the adduct.

### 16.6.2. Thioacetals and Desulfurization with Raney Ni

Thiols are more nucleophilic than alcohols (S is softer and more polarizable). Under acid catalysis ($\ce{HCl}$, $\ce{BF3*OEt2}$) they react with aldehydes and ketones to give thioacetals (thioketals); propane-1,3-dithiol or ethane-1,2-dithiol is commonly used to form the cyclic 1,3-dithianes and 1,3-dithiolanes:

```smiles
CCC(=O)CC.SCCCS>>CCC1(CC)SCCCS1
```

**Definition 16.6.1 (Thioacetal)** A compound $\ce{R2C(SR')2}$ in which one carbon atom carries two SR groups is called a **thioacetal**.

Compared with acetals, thioacetals have a large formation constant and are very stable toward acid: the lone pair of S is in a 3p orbital, which overlaps poorly with the carbon 2p orbital, so the thionium ion $\ce{R2C=S+R'}$ is less stable than the oxocarbenium ion and acidic hydrolysis is very slow. Thioacetals are removed by exploiting the thiophilicity of S (a soft base and a soft acid; the principle of **hard and soft acids and bases**): with aqueous $\ce{HgCl2}$ ($\ce{Hg^2+}$ coordinates strongly to S), or by oxidizing S with NBS, hypervalent iodine, or similar reagents and then hydrolyzing.

Another important reaction of thioacetals is desulfurization with Raney Ni (porous nickel with adsorbed hydrogen): the C–S bonds undergo hydrogenolysis and the original carbonyl group becomes $\ce{CH2}$. This is a neutral method for reducing a carbonyl group to a methylene group, complementary to the Wolff–Kishner reduction (basic, Section 16.9.4) and the **Clemmensen reduction** (acidic, [6.5.17](/6.5.17#sec-17.3.4)):

```smiles
O=C1CCCCC1>>C1CCC2(CC1)SCCS2
C1CCC2(CC1)SCCS2>>C1CCCCC1
```

### 16.6.3. Schiff's Reagent

When $\ce{SO2}$ is passed into a solution of fuchsine, the dye adds sulfurous acid and is decolorized; the result is Schiff's reagent. Aldehydes regenerate a colored quinoid dye (magenta) with it, whereas ketones give no color; the magenta color from formaldehyde does not fade on addition of sulfuric acid, while that from other aldehydes does, which distinguishes formaldehyde. The reagent must be free of base and oxidants and must not be heated (which would drive off the sulfurous acid and cause false positives). Feulgen staining (specific for DNA) and PAS staining (for polysaccharides) in histology are both based on this reaction: aldehyde groups are first generated on the deoxyribose of DNA or on sugars with acid or periodic acid, and the color is then developed with Schiff's reagent.

## 16.7. Carbon Nucleophiles

### 16.7.1. Hydrogen Cyanide and Cyanohydrins

Hydrogen cyanide adds to aldehydes, aliphatic methyl ketones, and small-ring ketones to give α-hydroxy nitriles, the cyanohydrins.

**Definition 16.7.1 (Cyanohydrin)** A compound $\ce{R2C(OH)CN}$ in which one carbon atom carries both OH and CN is called a **cyanohydrin**.

The nucleophile is the cyanide ion $\ce{CN-}$, not the HCN molecule: pure HCN hardly reacts with acetone, but the reaction is rapid when a little base is added. HCN is a weak acid ($\mathrm{p}K_{\mathrm{a}} = 9.21$, [Table 3.2 in 6.5.3](/6.5.3#sec-3.1.4)), and the reaction is run under slightly basic conditions: $\ce{CN-}$ attacks the carbonyl carbon, and the resulting alkoxide takes a proton from HCN and regenerates $\ce{CN-}$. This is Lapworth's classic study (1903) and one of the earliest organic reaction mechanisms established by kinetics. To avoid handling highly toxic HCN directly in the laboratory (lethal dose about $1\,\mathrm{mg\,kg^{-1}}$), acid is usually added slowly to a mixture of NaCN or KCN and the carbonyl compound, or trimethylsilyl cyanide ($\ce{Me3SiCN}$, which gives the silyl-protected cyanohydrin under Lewis acid catalysis) or acetone cyanohydrin is used as the cyanide source.

![Formation of a cyanohydrin: $\ce{CN-}$ attacks the carbonyl carbon, and the alkoxide takes a proton from HCN to give the cyanohydrin and regenerate $\ce{CN-}$ (the base-catalyzed cycle)](./plots/cyanohydrin.py)

Cyanohydrin formation is reversible, and the position of equilibrium follows the same pattern as the addition of sodium hydrogen sulfite. In acid, or on heating in strong base, the cyanohydrin decomposes back to the aldehyde or ketone and HCN. Cyanohydrins are useful synthetic intermediates: acidic hydrolysis gives α-hydroxy acids, and catalytic hydrogenation or reduction with $\ce{LiAlH4}$ gives β-amino alcohols. Industrially, acetone cyanohydrin is the starting material for methyl methacrylate (the monomer of Plexiglas).

```smiles
CC(C)=O>>CC(C)(O)C#N
CC(C)(O)C#N>>CC(C)(O)C(=O)O
```

Cyanogenic glycosides. Many plants store cyanohydrins as glycosides (acetals) as a defensive substance: amygdalin (the gentiobioside of mandelonitrile) in bitter almonds, apricot kernels, and apple and cherry seeds, and linamarin (the glucoside of acetone cyanohydrin) in cassava. When the tissue is damaged, β-glucosidase hydrolyzes the glycosidic bond and the released cyanohydrin is cleaved by hydroxynitrile lyase to the aldehyde or ketone and HCN. Cassava (the staple food of about 800 million people) must therefore be detoxified by soaking, fermentation, or thorough heating before it is eaten; sweet potato contains no cyanogenic glycosides and has no such problem when eaten raw. Plants do not synthesize these glycosides by the reverse of cyanohydrin formation, but biosynthesize them from amino acids through oxime intermediates. The reverse reaction of hydroxynitrile lyase is now used to prepare chiral cyanohydrins industrially (for example (R)-mandelonitrile, ee > 99%), a successful example of asymmetric synthesis by **enzyme catalysis**.

### 16.7.2. Acetylide Ions

Terminal alkynes have a $\mathrm{p}K_{\mathrm{a}}$ of about 25 ([Table 3.2 in 6.5.3](/6.5.3#sec-3.1.4)); the acetylide ion formed by deprotonation with $\ce{NaNH2}$, $n$-BuLi, or a Grignard reagent adds to aldehydes and ketones to give propargylic alcohols ([6.5.11](/6.5.11#sec-11.12.3)). In industry, the addition of acetylene to acetone is catalyzed directly by KOH in ether solvents (the Favorskii reaction) to give 2-methylbut-3-yn-2-ol; partial hydrogenation over Lindlar catalyst gives 2-methylbut-3-en-2-ol, and dehydration gives isoprene:

```smiles
CC(C)=O.C#C>>CC(C)(O)C#C
CC(C)(O)C#C>>CC(C)(O)C=C
CC(C)(O)C=C>>C=CC(C)=C
```

This route has been used historically to produce isoprene and intermediates for vitamin A and for terpenoid fragrances such as linalool; the propargylic alcohol skeleton is very useful in synthesis, and the alkynyl group can be further reduced, hydrated, or coupled.

### 16.7.3. Organolithium and Grignard Reagents

**Organolithium reagents** and **Grignard reagents** are equivalents of carbanions. Their addition to aldehydes and ketones followed by acidic hydrolysis gives alcohols, one of the most important ways to form C–C bonds and lengthen carbon chains: formaldehyde gives primary alcohols, other aldehydes give secondary alcohols, and ketones give tertiary alcohols. Their preparation, structure, and basic reactions were discussed in [6.5.10](/6.5.10); only the points related to the carbonyl group are added here:

- Mechanism. The reaction is run in ether. The carbonyl oxygen first coordinates to Mg (Lewis acid activation), and then R is transferred from Mg to the carbonyl carbon. Computational studies show that a six-membered ring transition state involving a dimer of the Grignard reagent (one Mg activates the carbonyl group and R on the other Mg attacks) is more favorable than a unimolecular four-membered ring transition state; the direction of attack of R still obeys the Bürgi–Dunitz angle. With hindered aromatic ketones the reaction can proceed by **single electron transfer** ([6.5.7](/6.5.7#sec-7.2.3)) to give a **ketyl** ([6.5.17](/6.5.17#sec-17.3.2)) that then recombines.
- Side reactions. When a hindered ketone reacts with a Grignard reagent that has a β-H (such as isopropylmagnesium bromide), a β-H of the alkyl group on Mg is transferred as hydride to the carbonyl carbon through a six-membered ring transition state, and the ketone is reduced to the alcohol (a reaction of the same kind as the **MPV reduction**, [6.5.17](/6.5.17#sec-17.2.2)) while the Grignard reagent becomes an alkene. A ketone with relatively acidic α-H can also be deprotonated by the Grignard reagent acting as a base to give the enolate, and the starting ketone is recovered after workup. Organocerium reagents, formed from organolithium reagents and $\ce{CeCl3}$, are weakly basic and strongly nucleophilic, and suppress both side reactions.
- Synthetic design. An alcohol can be disconnected in several ways at a Grignard reaction; for example, 2-phenylbutan-2-ol can be prepared from acetophenone + ethylmagnesium bromide, from butan-2-one + phenylmagnesium bromide, or stepwise from ethyl propanoate. The choice of disconnection is discussed under **retrosynthetic analysis** in [6.5.20](/6.5.20#sec-20.8.1).

```smiles
CC(=O)c1ccccc1.CC[Mg]Br>>CCC(C)(O)c1ccccc1
```

![Addition of a Grignard reagent to a ketone: magnesium coordinates to the carbonyl oxygen (dashed), the C–Mg bond pair moves to the carbonyl carbon and the C=O $\pi$ electrons move onto oxygen, giving the magnesium alkoxide; acidic workup gives the tertiary alcohol](./plots/grignard-addition.py)

![Reduction as a side reaction of Grignard reagents: di-tert-butyl ketone and isopropylmagnesium bromide react through a six-membered cyclic transition state; the β-H is transferred as a hydride to the carbonyl carbon and the C–Mg electrons form the C=C bond of propene, giving the magnesium salt of the alcohol (the same type of reaction as the MPV reduction)](./plots/grignard-reduction.py)

## 16.8. Ylides

**Definition 16.8.1 (Ylide)** A neutral compound $\ce{R2C^{-}-X^{+}R'_n}$ in which a negatively charged carbon atom is directly bonded to a positively charged heteroatom (P, S, N, etc.) is called an **ylide**.

Phosphorus ylides are often written in the double-bond form $\ce{Ph3P=CR2}$ (called a phosphorane), but this "double bond" is not a π bond involving d orbitals: the 3d orbitals of P are too high in energy, and calculations show that the P–C bond is a strongly polarized single bond, with the negative charge on carbon stabilized by **negative hyperconjugation** into the P–C σ* orbitals. Both ways of drawing are acceptable; the thing to remember is that the carbon is nucleophilic. A phosphorus ylide is made by the **SN2** reaction ([6.5.8](/6.5.8#sec-8.2.2)) of triphenylphosphine with an alkyl halide to give a phosphonium salt, followed by removal of an α-H with base:

```smiles
c1ccc(cc1)P(c1ccccc1)c1ccccc1.CCBr>>CC[P+](c1ccccc1)(c1ccccc1)c1ccccc1
CC[P+](c1ccccc1)(c1ccccc1)c1ccccc1>>C[CH-][P+](c1ccccc1)(c1ccccc1)c1ccccc1
```

The acidity of the α-H of phosphonium salts varies greatly with the substituents on the α carbon: $\ce{Ph3P+CH3}$ has a $\mathrm{p}K_{\mathrm{a}}$(DMSO) of 22.4 and requires deprotonation with $n$-BuLi, NaH, or NaHMDS, whereas $\ce{Ph3P+CH2CO2C2H5}$ has a value of about 9 (DMSO) and NaOH or $\ce{K2CO3}$ suffices. On this basis phosphorus ylides are divided into three classes:

| Class | Substituent on the α carbon | Example | Properties | Wittig reaction with aldehydes |
|---|---|---|---|---|
| Nonstabilized ylides | Alkyl, H | $\ce{Ph3P=CHCH3}$ | Highly reactive; sensitive to water and oxygen; generated in situ | Mainly (Z)-alkenes |
| Semistabilized ylides | Aryl, alkenyl | $\ce{Ph3P=CHPh}$ | Intermediate | Z/E mixtures |
| Stabilized ylides | COR, COOR, CN | $\ce{Ph3P=CHCO2C2H5}$ | The negative charge is delocalized onto the carbonyl group; isolable and air-stable; react only with aldehydes | Mainly (E)-alkenes |

### 16.8.1. The Wittig Reaction

**Definition 16.8.2 (Wittig Reaction)** The reaction of a phosphorus ylide with an aldehyde or ketone, in which the oxygen of the carbonyl group is replaced by the carbon of the ylide to give an alkene and triphenylphosphine oxide, is called the **Wittig reaction**.

```smiles
O=C1CCCCC1.C=P(c1ccccc1)(c1ccccc1)c1ccccc1>>C=C1CCCCC1.O=P(c1ccccc1)(c1ccccc1)c1ccccc1
```

The great advantage of the Wittig reaction is that the position of the new C=C double bond is completely defined (exactly where the carbonyl group was), whereas the elimination of alcohols often gives mixtures of double-bond positions; it also allows the synthesis of thermodynamically unfavorable exocyclic methylene alkenes (methylenecyclohexane in the equation above). G. Wittig received the 1979 Nobel Prize in Chemistry for this work (shared with H. C. Brown for organoboron chemistry). The driving force of the reaction is the formation of the very strong P=O bond (bond dissociation enthalpy about $575\,\mathrm{kJ\,mol^{-1}}$).

Mechanism. Two pathways were proposed historically: the carbon of the ylide first attacks the carbonyl carbon to give a zwitterionic betaine, which then closes to an oxaphosphetane; or the two react directly in a [2+2] cycloaddition to give the oxaphosphetane. The current conclusion (a series of studies by Vedejs and coworkers; the 2013 review by Byrne and Gilheany) is that under lithium-salt-free conditions all types of phosphorus ylides react with aldehydes by a concerted but asynchronous [2+2] cycloaddition, irreversibly and directly giving the oxaphosphetane (observable by low-temperature $\ce{^{31}P}$ NMR at a chemical shift of about $-60$ to $-70$), with no observable betaine intermediate; the oxaphosphetane then undergoes a syn retro-[2+2] cycloreversion that stereospecifically gives the alkene and $\ce{Ph3P=O}$.

![The Wittig reaction: the nucleophilic carbon of the ylide bonds to the carbonyl carbon and the carbonyl oxygen bonds to phosphorus, giving an oxaphosphetane by [2+2] cycloaddition; the four-membered ring decomposes by retro-[2+2] to the alkene and triphenylphosphine oxide. The cis or trans relationship of the two substituents in the oxaphosphetane is converted directly into the Z/E configuration of the alkene](./plots/wittig.py)

Stereoselectivity. Because formation of the oxaphosphetane is irreversible and its decomposition is stereospecific, the Z/E ratio of the alkene is determined by the energy difference between the two transition states leading to the cis and trans oxaphosphetanes (**kinetic control**):

- Nonstabilized ylides react fast, with an early, "puckered" transition state: R of the aldehyde and R′ of the ylide lie on the same side of the forming four-membered ring, avoiding the 1,3-interaction between the aldehyde substituent and the large phenyl groups on phosphorus, so the cis oxaphosphetane and hence the (Z)-alkene is formed.
- Stabilized ylides react more slowly, with a late, nearly planar transition state in which the 1,2-repulsion between the substituents on the two ring carbons is dominant; the dipole–dipole interaction between the ylide carbonyl group and the aldehyde carbonyl group also favors the trans arrangement, so the (E)-alkene is formed.

An earlier explanation turned on whether the betaines can interconvert: addition of stabilized ylides is reversible and the betaines equilibrate to the more stable trans form, whereas nonstabilized ylides eliminate quickly and are locked in the kinetic cis form. This was the explanation of the 1960s and 1970s and has been refuted by the experiments above (under lithium-free conditions no such equilibrium can be detected by crossover experiments or low-temperature NMR). In the presence of lithium salts the situation does differ: $\ce{Li+}$ coordinates to oxygen and gives betaine-type intermediates and "stereochemical drift", so for high Z selectivity the ylide is generated with NaHMDS or KHMDS to avoid the lithium salts introduced by $n$-BuLi. The Schlosser modification, in turn, uses the effect of lithium salts at low temperature to turn the reaction of a nonstabilized ylide toward (E)-alkenes.

As examples of applications: in the synthesis of bixin, a dialdehyde reacts with two molecules of the stabilized ylide $\ce{Ph3P=CHCO2CH3}$, and both new double bonds are E; in the synthesis of jasmone, the nonstabilized ylide $\ce{Ph3P=CHC2H5}$ introduces the Z double bond in the side chain.

### 16.8.2. The Horner–Wadsworth–Emmons Reaction

Replacing the phosphonium salt by a phosphonate gives the more commonly used modified procedure.

**Definition 16.8.3 (Horner–Wadsworth–Emmons Reaction)** The reaction of the phosphonate carbanion, formed from a phosphonate $\ce{(RO)2P(O)CH2Z}$ (Z is an electron-withdrawing group) with base, with an aldehyde or ketone to give an alkene and a water-soluble dialkyl phosphate salt is called the **Horner–Wadsworth–Emmons reaction**, abbreviated the HWE reaction.

Phosphonates are made from triethyl phosphite and alkyl halides by the **Arbuzov reaction** ([6.5.26](/6.5.26#sec-26.6.2)). Triethyl phosphonoacetate has a $\mathrm{p}K_{\mathrm{a}}$(DMSO) of 18.6 and is deprotonated with NaH, $t$-BuOK, or DBU/LiCl. Compared with the Wittig reaction, the HWE reaction has three advantages: the phosphonate carbanion is more nucleophilic than the corresponding stabilized phosphorus ylide and reacts with ketones; the by-product $\ce{(EtO)2PO2-}$ is soluble in water and removed by washing ($\ce{Ph3PO}$ is often very hard to separate from the product); and the E selectivity is high (generally > 90:10).

```smiles
CCOC(=O)CP(=O)(OCC)OCC.O=Cc1ccccc1>>CCOC(=O)/C=C/c1ccccc1
```

The E selectivity comes from the reversibility of the intermediates: addition of the phosphonate carbanion to the aldehyde is reversible, so the two diastereomeric addition intermediates (β-oxido phosphonates) can interconvert through the reverse reaction, while their closure to the oxaphosphetane occurs at different rates; the one with the substituents trans closes faster, so the product is mainly the (E)-alkene (a Curtin–Hammett situation, [6.5.3](/6.5.3#sec-3.9.3)). With the electron-poor bis(trifluoroethyl) phosphonate $\ce{(CF3CH2O)2P(O)CH2CO2Me}$ under KHMDS/18-crown-6 conditions, ring closure is faster and the addition becomes irreversible, and the product turns to the (Z)-alkene (the Still–Gennari modification, 1983).

![The HWE reaction: the phosphonate carbanion attacks the carbonyl carbon of the aldehyde, the resulting β-oxido anion attacks phosphorus to form the oxaphosphetane, and this decomposes to the (E)-α,β-unsaturated ester and diethyl phosphate anion](./plots/hwe.py)

### 16.8.3. Sulfur Ylides

Sulfur ylides are obtained by deprotonation of sulfonium salts (trialkylsulfonium salts) or sulfoxonium salts with strong base: dimethylsulfonium methylide $\ce{(CH3)2S+CH2-}$ (from trimethylsulfonium iodide and NaH in DMSO) and dimethylsulfoxonium methylide $\ce{(CH3)2S(O)+CH2-}$ (from trimethylsulfoxonium iodide).

**Definition 16.8.4 (Corey–Chaykovsky Reaction)** The reaction of a sulfur ylide with an aldehyde or ketone to give an epoxide, or with an α,β-unsaturated carbonyl compound to give a cyclopropane, is called the **Corey–Chaykovsky reaction**.

The difference between phosphorus and sulfur ylides lies in what happens after addition: both first form a C–C bond at the carbonyl carbon to give a zwitterionic adduct. The P–O bond is very strong, and the oxide of a phosphorus ylide attacks phosphorus, finally giving the alkene. The S–O bond is weak and dimethyl sulfide is an excellent **leaving group**, so the oxide of a sulfur ylide instead attacks the positively charged $\ce{CH2}$ from the back side intramolecularly, displacing dimethyl sulfide by an intramolecular SN2 substitution and forming a three-membered ring, an **epoxide**.

![Corey–Chaykovsky epoxidation: the carbon of dimethylsulfonium methylide attacks the carbonyl carbon of cyclohexanone, the resulting oxide attacks $\ce{CH2}$ intramolecularly, and dimethyl sulfide leaves to give the spiro epoxide](./plots/sulfur-ylide.py)

Selectivity is determined by reversibility. The two sulfur ylides show very different selectivities, often attributed to "size", but the more fundamental reason is whether the first addition is reversible:

- Dimethylsulfonium methylide is a nonstabilized ylide; its addition is fast and irreversible, and the product reflects the kinetic direction of attack. With cyclohexanone, the small nucleophile attacks axially along the Bürgi–Dunitz trajectory (as in the axial attack of $\ce{LiAlH4}$ in [6.5.17](/6.5.17#sec-17.1.2)), so the new C–C bond is axial and the epoxide oxygen is equatorial: 4-tert-butylcyclohexanone gives the two spiro epoxides in a ratio of about 83:17 (isolated yields 64% and 13%). With α,β-unsaturated ketones it undergoes **1,2-addition** at the carbonyl group to give vinyl epoxides.
- The negative charge of dimethylsulfoxonium methylide is partly stabilized by S=O, and its addition is reversible, so the adduct can return to the starting materials before ring closure. With cyclohexanone, the equilibrium favors the sterically less hindered adduct with an equatorial C–C bond (which then closes), and the product is mainly the epoxide with axial oxygen (89%). With α,β-unsaturated ketones, the reversible 1,2-adduct returns to the starting materials, while the irreversible **1,4-addition** (**conjugate addition**, [6.5.17](/6.5.17#sec-17.6.2)) gives an enolate that closes intramolecularly to the cyclopropane. Ester-stabilized sulfonium ylides (such as $\ce{(CH3)2S=CHCO2C2H5}$) likewise give cyclopropanes.

```smiles
CC1=CCC(C(C)=C)CC1=O>>CC1=CCC(C(C)=C)CC12CO2
C=CC=O>>O=CC1CC1C(=O)OCC
```

The first equation is the 1,2-addition of $\ce{(CH3)2S=CH2}$ to carvone (89%), and the second is the cyclopropanation of acrolein with $\ce{(CH3)2S=CHCO2C2H5}$ (63%, trans:cis = 5:1).

## 16.9. Nitrogen Nucleophiles

### 16.9.1. Imines and the Effect of pH

A primary amine adds to an aldehyde or ketone to give first a hemiaminal (also called a carbinolamine), which then loses water to form a C=N double bond.

**Definition 16.9.1 (Imine)** A compound $\ce{R2C=NR'}$ containing a C=N double bond (R′ is H or a hydrocarbon group) is called an **imine**; an imine with a hydrocarbon group on N is also called a **Schiff base**.

```smiles
O=Cc1ccccc1.CN>>CN=Cc1ccccc1
```

Imines of aliphatic aldehydes are unstable and easily hydrolyzed or self-condensed; imines of aromatic aldehydes with aromatic amines (stabilized by conjugation) can be isolated. Every step in imine formation is reversible: removal of water (molecular sieves, azeotropic distillation) drives the formation, whereas in aqueous acid the imine is hydrolyzed back to the aldehyde or ketone and the amine (the mechanism of the reverse reaction is the same as that of the forward reaction, in the opposite direction).

![Imine formation: the nitrogen of the amine attacks the carbonyl carbon, and proton transfer gives the hemiaminal; after protonation of the OH, the lone pair on nitrogen pushes out water to give the iminium ion, and loss of the proton on N gives the imine](./plots/imine.py)

The rate of imine formation as a function of pH is bell-shaped, with a maximum at pH about 4–5 (the classic study by Jencks). The reason is that the two steps need opposite conditions:

- The second step (loss of water from the hemiaminal) needs acid to convert OH into a good leaving group; in neutral and basic solutions it is the rate-determining step, and the rate increases with increasing acidity.
- The first step needs the free amine as the nucleophile. The conjugate acids of amines have $\mathrm{p}K_{\mathrm{a}}$ values of about 9–11 ([Table 3.2 in 6.5.3](/6.5.3#sec-3.1.4)); the more acidic the solution, the less free amine there is. Below pH about 4 almost all of the amine is protonated, the addition of the first step becomes rate-determining, and the rate decreases with increasing acidity.

The compromise between the two gives the maximum at pH about 4–5. The same holds for amine derivatives with lower $\mathrm{p}K_{\mathrm{a}}$ values (3–8), such as hydroxylamine, hydrazine, and semicarbazide.

Imines are ubiquitous in biochemistry. The coenzyme of transaminases, pyridoxal phosphate (PLP), forms Schiff bases successively with a lysine residue and with the substrate amino acid. Class I **aldolases** form an iminium ion with the substrate ketone through an active-site lysine and convert it to an enamine to carry out the **aldol reaction**. In the retina, retinal forms a protonated Schiff base with a lysine of opsin, and its photoisomerization is the first step of vision. In drug design, the reversible hydrolysis of imines is also used to design prodrugs and pH-responsive drug release systems (hydrolysis in weakly acidic tumor tissue or in endosomes).

### 16.9.2. Oximes, Hydrazones, and Semicarbazones

The C=N compounds formed from aldehydes and ketones with ammonia derivatives $\ce{H2N-Y}$ are all more stable than simple imines: the lone pair on Y (O, N) is conjugated with C=N, lowering the electrophilicity of the C=N carbon and making the hydrolysis equilibrium unfavorable.

| Reagent | Product | Name of product |
|---|---|---|
| $\ce{H2N-OH}$ (hydroxylamine) | $\ce{R2C=N-OH}$ | *Oxime* |
| $\ce{H2N-NH2}$ (hydrazine) | $\ce{R2C=N-NH2}$ | Hydrazone |
| $\ce{H2N-NHPh}$ (phenylhydrazine) | $\ce{R2C=N-NHPh}$ | Phenylhydrazone |
| $\ce{H2N-NH-C6H3(NO2)2}$ (2,4-dinitrophenylhydrazine) | 2,4-Dinitrophenylhydrazone | Yellow or orange-red crystals |
| $\ce{H2N-NHCONH2}$ (semicarbazide) | $\ce{R2C=N-NHCONH2}$ | Semicarbazone |

These products are mostly crystalline with sharp melting points, and before the spread of spectroscopic methods they were the main means of identifying aldehydes and ketones (2,4-dinitrophenylhydrazine is still used to detect carbonyl groups); they can be hydrolyzed back in dilute acid, so they are also used to separate and purify aldehydes and ketones. Oximes are important synthetic intermediates: in acid they undergo the Beckmann rearrangement to **amides** ([6.5.30](/6.5.30)), and the Beckmann rearrangement of cyclohexanone oxime is the industrial route to caprolactam, the monomer of nylon-6. Oximes and hydrazones are also used as stable linkages in bioconjugate chemistry ("oxime ligation" and "hydrazone ligation", aniline-catalyzed).

```smiles
O=C1CCCCC1.NO>>ON=C1CCCCC1
```

### 16.9.3. Enamines

A secondary amine also adds to an aldehyde or ketone to give an iminium ion, but there is no H on N to be lost; if the carbonyl compound has an α-H, the iminium ion loses the α-H to give an enamine with a C=C–N unit.

**Definition 16.9.2 (Enamine)** A compound $\ce{R2C=CR-NR2}$ in which a nitrogen atom is directly bonded to a carbon–carbon double bond is called an **enamine**.

![Enamine formation: the iminium ion formed by addition of the secondary amine and loss of water has no N–H to lose, so a base (the amine or the solvent) removes an α-H; the electrons of the C–H bond form the C=C double bond, the positive charge disappears, and the enamine results](./plots/enamine.py)

```smiles
O=C1CCCCC1.C1CCNC1>>C1CCC(=CC1)N1CCCC1
```

The secondary amines commonly used are pyrrolidine, piperidine, and morpholine, with TsOH catalysis and azeotropic removal of water in toluene. An enamine can be regarded as the nitrogen analogue of an enol: the lone pair on N is conjugated with C=C, which makes the β carbon a nucleophilic center (a resonance structure of the iminium ion). It reacts with alkyl halides, acyl chlorides, and α,β-unsaturated carbonyl compounds, and hydrolysis introduces a substituent at the α position of the carbonyl group, the **Stork enamine reaction** ([6.5.21](/6.5.21#sec-21.8.1)). Enamines are also reactive intermediates in **organocatalysis** (proline-catalyzed asymmetric aldol reactions, [6.5.22](/6.5.22#sec-22.6.3), the work of List, Nobel Prize in Chemistry 2021) and in the reactions of class I aldolases. Enamines are rapidly hydrolyzed in aqueous acid back to the carbonyl compound and the secondary amine. A tertiary amine has no N–H and does not undergo this kind of condensation with aldehydes and ketones. Aldehydes without α-H (such as benzaldehyde) can only reach the stage of the iminium ion or the aminal $\ce{RCH(NR2)2}$ with secondary amines.

In the total synthesis of goniomitine (Xu, Wang, and Zhu, 2013), an aldehyde bearing a primary amine formed a cyclic enamine rather than an imine on intramolecular condensation: imines and enamines are tautomers, and when the C=C can conjugate with an aromatic ring or lies in a stable ring, the enamine form is more stable, just as the enol form of carbonyl compounds predominates in 1,3-dicarbonyl compounds ([6.5.21](/6.5.21#sec-21.2.4)).

### 16.9.4. The Wolff–Kishner–Huang Minlon Reduction

When a hydrazone is heated in strong base, nitrogen is evolved and the original carbonyl group is reduced to a methylene group.

**Definition 16.9.3 (Wolff–Kishner Reduction)** The reaction in which the hydrazone formed from an aldehyde or ketone and hydrazine decomposes at high temperature in strong base with evolution of $\ce{N2}$, reducing the carbonyl group to $\ce{CH2}$, is called the **Wolff–Kishner reduction**.

The original procedure of Wolff (1912) and Kishner (1911) heated the hydrazone with sodium alkoxide in a sealed tube to about $200\,^\circ\mathrm{C}$, which was inconvenient and slow. The modification of Huang Minlon (1946, at Harvard University) places the aldehyde or ketone, 85% hydrazine hydrate, and KOH or NaOH in a high-boiling solvent, diethylene glycol (bp $245\,^\circ\mathrm{C}$) or ethylene glycol; the mixture is first refluxed to form the hydrazone, and then water and excess hydrazine are distilled off so that the temperature rises to about $200\,^\circ\mathrm{C}$ and decomposition is completed. The reaction takes a few hours at atmospheric pressure and the yield is very high. The improvement came from an accident: the stopper of the flask leaked, water and hydrazine distilled off, and the temperature rose; the mixture turned "pitch black", yet the yield was higher, and Huang Minlon carefully analyzed the cause. It is the first organic reaction named after a Chinese chemist. The solvent must be a high-boiling glycol: low-boiling ethers (such as 1,2-dimethoxyethane, bp $85\,^\circ\mathrm{C}$) cannot reach the temperature needed for decomposition.

Mechanism. Base removes a proton from the N–H of the hydrazone; the resulting anion (with negative charge delocalized onto carbon) is protonated at carbon by the solvent to give $\ce{R2CH-N=NH}$ (this step is rate-determining and needs high temperature); loss of the N–H proton then gives $\ce{R2CH-N=N-}$, which loses $\ce{N2}$ and leaves a carbanion, and the carbanion is immediately protonated by the solvent. The evolution of nitrogen makes the reaction irreversible.

![Mechanism of the Wolff–Kishner reduction: base removes the N–H of the hydrazone, the anion is protonated on carbon to give the diazene; a second deprotonation is followed by loss of nitrogen, and the resulting carbanion is protonated by the solvent, so that the carbonyl carbon finally becomes $\ce{CH2}$](./plots/wolff-kishner.py)

```smiles
O=C(CCCCCCCCCCCCCCC(=O)O)CCCCCCCCCCCCCCC(=O)O>>O=C(O)CCCCCCCCCCCCCCCCCCCCCCCCCCCCCC(=O)O
```

(In this equation a keto diacid is reduced to hentriacontanedioic acid.) The Wolff–Kishner reduction is carried out in strong base and is suitable for acid-sensitive substrates; for base-sensitive substrates (esters, alkyl halides) the **Clemmensen reduction** ([6.5.17](/6.5.17#sec-17.3.4)) is used, and when neither is suitable, desulfurization of the thioacetal (Section 16.6.2) is used.

## 16.10. Umpolung

### 16.10.1. The Concept of Umpolung

The carbonyl carbon is electrophilic and its α carbon (through the enolate) is nucleophilic; with this "natural" polarity, the reactions of aldehydes and ketones always involve a nucleophile adding to the carbonyl carbon. If the carbonyl carbon itself could be made negatively charged, structures that cannot be obtained directly with the natural polarity could be built, such as 1,2-dicarbonyl compounds and α-hydroxy ketones (in which the two carbonyl carbons are directly bonded).

**Definition 16.10.1 (Umpolung)** A strategy in which the natural polarity (electrophilic or nucleophilic) of an atom is temporarily reversed by chemical modification so that it can react with the opposite polarity, and the modification is removed after the reaction to restore the functional group, is called **umpolung** (German for "polarity reversal"), systematically developed by Seebach.

There are two approaches to the umpolung of aldehydes: (1) add a group that can stabilize a carbanion, so that the original aldehyde C–H becomes acidic enough to be deprotonated by base (the dithiane method); (2) add an electron-withdrawing nucleophilic catalyst that is easily lost ($\ce{CN-}$, an N-heterocyclic carbene), and remove it after the reaction (the benzoin condensation).

### 16.10.2. 1,3-Dithianes

An aldehyde and propane-1,3-dithiol give a 2-substituted 1,3-dithiane (Section 16.6.2). The C2–H lies between two S atoms and is fairly acidic: 1,3-dithiane has a $\mathrm{p}K_{\mathrm{a}}$ of about 31 (Streitwieser, in cyclohexylamine) and 2-phenyl-1,3-dithiane has a $\mathrm{p}K_{\mathrm{a}}$(DMSO) of 30.7, so it can be deprotonated with $n$-BuLi in THF at low temperature. The carbanion is stabilized by the polarizability of S and by the C–S σ* orbitals (not by d orbitals). 2-Lithio-1,3-dithiane is an equivalent of an "acyl anion": it reacts with alkyl halides, epoxides, aldehydes, and ketones, and finally hydrolysis with aqueous $\ce{HgCl2}$ gives a ketone, or desulfurization with Raney Ni gives an alkane. This is the Corey–Seebach method (1965).

![Umpolung with 1,3-dithiane: $n$-BuLi removes C2–H, and 2-lithio-1,3-dithiane reacts as a nucleophile with an alkyl bromide in an SN2 reaction; hydrolysis with $\ce{HgCl2}$ gives the ketone. The carbon of the original aldehyde group changes from electrophilic to nucleophilic](./plots/dithiane.py)

```smiles
O=Cc1ccccc1>>c1ccc(cc1)C1SCCCS1
c1ccc(cc1)C1SCCCS1>>CCCCC1(c2ccccc2)SCCCS1
CCCCC1(c2ccccc2)SCCCS1>>CCCCC(=O)c1ccccc1
```

### 16.10.3. The Benzoin Condensation

Two molecules of an aromatic aldehyde condense under cyanide catalysis to give an α-hydroxy ketone.

**Definition 16.10.2 (Benzoin Condensation)** The condensation of two molecules of an aromatic aldehyde catalyzed by $\ce{CN-}$ (or an N-heterocyclic carbene), in which the carbonyl carbon of one aldehyde adds in nucleophilic form to the carbonyl carbon of the other to give an α-hydroxy ketone $\ce{ArCH(OH)COAr}$, is called the **benzoin condensation**; the product from benzaldehyde, 2-hydroxy-1,2-diphenylethan-1-one, is known as benzoin.

In the mechanism (Lapworth, 1903), $\ce{CN-}$ plays three roles. It is the nucleophile that first adds to the aldehyde. It is an electron-withdrawing group that makes the original aldehyde C–H in the adduct (which also carries a phenyl group on the same carbon) acidic enough that proton transfer gives a carbanion; this step is the umpolung. And it is a good leaving group, which departs after the carbanion has attacked the second molecule of aldehyde and proton transfer has occurred, regenerating the catalyst. Only aromatic aldehydes react smoothly: the phenyl group and CN together stabilize the carbanion, whereas the α-H of an aliphatic aldehyde is more easily removed and the **aldol condensation** ([6.5.22](/6.5.22#sec-22.1)) takes place instead.

![Cyanide-catalyzed benzoin condensation: $\ce{CN-}$ adds to benzaldehyde; proton transfer gives the carbanion stabilized by CN and phenyl (umpolung); the carbanion attacks a second molecule of benzaldehyde; after proton transfer $\ce{CN-}$ leaves to give benzoin](./plots/benzoin.py)

### 16.10.4. Vitamin B1 and the Breslow Intermediate

In living organisms the same chemistry is carried out by the pyrophosphate ester of vitamin B1 (thiamine), TPP, the coenzyme of pyruvate decarboxylase, the pyruvate dehydrogenase complex, transketolase, and other enzymes. Breslow (1958) proposed a unified mechanism: the C2–H of the thiazolium ring is quite acidic ($\mathrm{p}K_{\mathrm{a}}$ about 18 in water; Washabaugh and Jencks, 1988), and deprotonation gives a **carbene**, an N-heterocyclic carbene (NHC), which can also be drawn as a zwitterionic ylide. Like $\ce{CN-}$, the NHC carbon adds to the aldehyde, and proton transfer gives the Breslow intermediate, an enaminol: the original aldehyde carbon has become an electron-rich alkene carbon, a nucleophilic acyl anion equivalent. It attacks the second molecule of aldehyde and then releases the carbene catalyst to give the α-hydroxy ketone.

**Definition 16.10.3 (Breslow Intermediate)** The enaminol $\ce{(NHC)=C(OH)R}$ formed by proton transfer after addition of an N-heterocyclic carbene (such as a thiazolium or triazolium ylide) to an aldehyde is called the **Breslow intermediate**; it is the acyl anion equivalent in NHC-catalyzed umpolung reactions.

![Vitamin B1-type catalysis: deprotonation of C2–H of the thiazolium salt gives the N-heterocyclic carbene; the carbene carbon adds to the carbonyl carbon of the aldehyde, and proton transfer gives the Breslow intermediate, in which the original aldehyde carbon is the nucleophilic enaminol carbon](./plots/breslow.py)

The two catalysts of the benzoin condensation are thus unified: $\ce{CN-}$ and NHCs are both nucleophilic catalysts that act by "addition, proton transfer, departure", differing only in how they stabilize the carbanion (the inductive and conjugative effects of CN; conjugation with the positively charged iminium C=N⁺ of the thiazolium ring). In pyruvate decarboxylase, the carbene of TPP adds to the ketone carbonyl group of pyruvate, and the carboxyl group is lost as $\ce{CO2}$ (the electrons flow to the positively charged thiazolium ring, which acts like the carbonyl group in the **decarboxylation** of β-keto acids, [6.5.18](/6.5.18#sec-18.4.1)); protonation of the resulting Breslow intermediate releases acetaldehyde, which is how acetaldehyde arises in the ethanol fermentation of yeast. The biological significance of these reactions belongs to biochemistry; the point to stress here is that the catalytic chemistry used by the enzyme is the same as the $\ce{CN-}$ catalysis in a flask.

Artificial NHC catalysis has become an important branch of organocatalysis: the asymmetric benzoin condensation catalyzed by chiral triazolium salts, the Stetter reaction of aldehydes with α,β-unsaturated acceptors (giving 1,4-dicarbonyl compounds), and further modes such as acyl azoliums and homoenolates obtained by oxidation of the Breslow intermediate. Stable NHCs themselves (Arduengo, 1991) appear as metal ligands in [6.5.28](/6.5.28#sec-28.5.4).

## Summary

- The π* orbital of the carbonyl group is low in energy with a large coefficient on carbon, and the n orbital is the HOMO. The characteristic reactions of aldehydes and ketones are therefore attack of a nucleophile on carbon from above or below the plane at the Bürgi–Dunitz angle of about $107^\circ$ (Definition 16.2.2), and binding of $\ce{H+}$ or a Lewis acid by oxygen in the plane.
- Reactivity: $\ce{HCHO}$ > aldehydes > ketones, aliphatic > aromatic; electron-withdrawing substituents and small-ring strain favor addition; the equilibrium constant of hydration is a direct measure (the table in Section 16.3).
- The π bond of C=O is strong, so additions of H–X (water, alcohols, HCN, $\ce{NaHSO3}$, amines) are reversible and the equilibrium is controlled by concentration and removal of water; additions of organometallics and hydride are irreversible and under kinetic control.
- Stereochemistry: the Re/Si faces of the prochiral carbonyl group; aldehydes and ketones with an α stereocenter are predicted by the Felkin–Anh model (Definition 16.4.1), in which L is perpendicular to the carbonyl plane and Nu attacks past S; an electronegative group occupies the L position (polar Felkin–Anh); a chelating α-OR with a chelating metal gives the anti-Felkin product.

| Nucleophile | Product | Conditions and key points |
|---|---|---|
| $\ce{H2O}$ | gem-Diol (hydrate) | Acid or base catalysis; generally not isolable |
| ROH | Hemiacetal, then acetal (Definition 16.5.1) | Acid catalysis, removal of water; acetals are stable to base and serve as protecting groups (Definition 16.5.2); orthoesters remove water |
| $\ce{HSO3-}$ | α-Hydroxysulfonate | Aldehydes, methyl ketones, small-ring ketones; separation and purification |
| RSH | Thioacetal (Definition 16.6.1) | Stable to acid, hydrolyzed with $\ce{HgCl2}$; desulfurization with Raney Ni gives $\ce{CH2}$ |
| $\ce{CN-}$ | Cyanohydrin (Definition 16.7.1) | Base-catalyzed, reversible; cyanogenic glycosides |
| $\ce{RC#C-}$, RLi, RMgX | Alcohols | Irreversible; 1°/2°/3° alcohols; reduction and enolization as side reactions |
| $\ce{Ph3P=CHR}$ | Alkenes | Wittig (Definition 16.8.2): irreversible [2+2]; Z with nonstabilized, E with stabilized ylides |
| $\ce{(EtO)2P(O)CH-Z}$ | (E)-Alkenes | HWE (Definition 16.8.3): reversible addition gives E; Still–Gennari gives Z |
| $\ce{Me2S=CH2}$ / $\ce{Me2S(O)=CH2}$ | Epoxides / cyclopropanes | Corey–Chaykovsky (Definition 16.8.4): selectivity depends on whether the addition is reversible |
| $\ce{RNH2}$, $\ce{H2NY}$ | Imines (Definition 16.9.1), oximes, hydrazones, semicarbazones | Fastest at pH 4–5; biochemistry of Schiff bases |
| $\ce{R2NH}$ | Enamines (Definition 16.9.2) | Requires α-H; the β carbon is nucleophilic |
| $\ce{H2NNH2}$, KOH | $\ce{CH2}$ | Wolff–Kishner–Huang Minlon reduction (Definition 16.9.3), diethylene glycol, about 200 °C |

- Umpolung (Definition 16.10.1) turns the carbonyl carbon into a nucleophilic center: the 1,3-dithiane anion is an acyl anion equivalent; $\ce{CN-}$ and N-heterocyclic carbenes catalyze the benzoin condensation (Definition 16.10.2), the latter through the Breslow intermediate (Definition 16.10.3), which is also the chemistry of the vitamin B1 coenzyme.

## Questions

1. Using the average bond enthalpies of [6.1.3](/6.1.3), explain why the addition of HCN and $\ce{NaHSO3}$ to acetone is "awkward" (it works only for aldehydes, methyl ketones, and small-ring ketones), whereas the addition of $\ce{CH3Li}$ to formaldehyde is practically irreversible.

   **Answer** In the addition of H–X, the π part of C=O (about $390\,\mathrm{kJ\,mol^{-1}}$) and the H–X bond are broken, and C–X and O–H bonds are formed. For HCN, an H–C bond (about $528\,\mathrm{kJ\,mol^{-1}}$; the C–H bond of HCN is very strong) is broken and C–C (346) and O–H (about 463) bonds are formed; for hydrogen sulfite, the C–S bond formed (about 272) is weaker. In both cases the enthalpy change is only a few tens of $\mathrm{kJ\,mol^{-1}}$ exothermic, and the entropy loss of combining two molecules into one ($-T\Delta S$ is about $+30\,\mathrm{kJ\,mol^{-1}}$ in solution) together with the crowding of substituents in the product (a ketone has one more alkyl group than an aldehyde) is enough to cancel it, so the equilibrium constant is close to 1 and only sterically unhindered aldehydes, methyl ketones, and small-ring ketones add favorably. The addition of $\ce{CH3Li}$ to formaldehyde breaks the weak C–Li bond (of the order of $200\,\mathrm{kJ\,mol^{-1}}$) and forms a C–C bond and a very strong O–Li bond, with an exothermicity of more than $70\,\mathrm{kJ\,mol^{-1}}$; the equilibrium constant is enormous and the reverse reaction is negligible.

2. Which of the following compounds exist mainly as hydrates in water? (a) acetone; (b) trifluoroacetaldehyde; (c) cyclopropanone; (d) benzaldehyde; (e) the aldehyde group of malonaldehyde. Explain.

   **Answer** (b) and (c). The $\ce{CF3}$ group of trifluoroacetaldehyde is strongly electron-withdrawing, which destabilizes the carbonyl group and stabilizes the hydrate (as with trichloroacetaldehyde). The $\mathrm{sp^2}$ carbon of cyclopropanone has a severely compressed bond angle in the three-membered ring, and on becoming $\mathrm{sp^3}$ the angle strain is reduced, so it is almost completely hydrated. The $K_{\mathrm{hyd}}$ values of acetone (two electron-donating methyl groups) and benzaldehyde (the benzene ring is conjugated with the carbonyl group and hydration would lose the conjugation) are both small. Malonaldehyde exists in water mainly in the enol form (3-hydroxyacrolein, stabilized by an intramolecular hydrogen bond and conjugation) and its anion, not as the hydrate, which is characteristic of **1,3-dicarbonyl compounds** ([6.5.21](/6.5.21#sec-21.2.4)).

3. Write the complete mechanism for the acid-catalyzed formation of 2-phenyl-1,3-dioxolane from benzaldehyde and ethane-1,2-diol, identify the rate-determining step, and explain why the acetal is not formed in base and why the acetal is not hydrolyzed in base.

   **Answer** (1) The carbonyl oxygen is protonated; (2) one OH of the diol attacks the carbonyl carbon; (3) loss of a proton gives the hemiacetal; (4) the OH of the hemiacetal is protonated; (5) water is lost, giving the oxocarbenium ion stabilized by the lone pair on oxygen and the benzene ring (the rate-determining step); (6) the other OH of the same molecule attacks the oxocarbenium carbon, forming the five-membered ring; (7) loss of a proton gives the acetal. In base, the first addition can occur (the alkoxide attacks) to give the hemiacetal anion, but the next step requires OH to leave as $\ce{HO-}$, a very poor leaving group, and base cannot convert it into a good one, so the reaction stops at the hemiacetal. Conversely, the first step of acetal hydrolysis requires protonation of OR so that it leaves as an alcohol; in basic solution there are not enough protons and an alkoxide cannot leave, so the acetal (as an ether) is stable.

4. Starting from ethyl 4-oxocyclohexanecarboxylate, synthesize 4-(hydroxymethyl)cyclohexan-1-one (that is, reduce the ester to a primary alcohol while keeping the ketone carbonyl group).

   **Answer** First protect the ketone as the ethane-1,2-diol ketal (ethyl 1,4-dioxaspiro[4.5]decane-8-carboxylate) with ethane-1,2-diol and TsOH in toluene with a Dean–Stark trap. Then reduce the ester to the primary alcohol with $\ce{LiAlH4}$ in diethyl ether or THF (the acetal is stable under these basic reducing conditions). Finally hydrolyze the ketal with dilute HCl in acetone–water to give 4-(hydroxymethyl)cyclohexan-1-one. Without protection, $\ce{LiAlH4}$ would first reduce the more reactive ketone carbonyl group.

5. Eating raw cassava is poisonous, whereas eating raw sweet potato is harmless; eating too many bitter almonds is also dangerous. Explain this with the chemistry of this chapter, and explain why cassava can be eaten safely after soaking, fermentation, and cooking.

   **Answer** Cassava contains linamarin (the glucoside of acetone cyanohydrin) and bitter almonds contain amygdalin (the glycoside of mandelonitrile); these are acetals (glycosides) of cyanohydrins. When chewing breaks the cells, the plant's own β-glucosidase hydrolyzes the glycosidic bond and releases the cyanohydrin; the formation of cyanohydrins is reversible, and under neutral to basic conditions (and by the action of hydroxynitrile lyase) the cyanohydrin decomposes into acetone or benzaldehyde and HCN, which inhibits cytochrome c oxidase and causes poisoning. Sweet potato contains no cyanogenic glycosides. Soaking and fermentation let the enzyme hydrolyze the glycosides outside the body, and the HCN formed evaporates or is removed with the water; cooking inactivates the enzyme and decomposes the remaining cyanohydrin, and HCN evaporates.

6. (S)-2-Phenylpropanal adds $\ce{CH3MgBr}$. Using the Felkin–Anh model, draw the favored transition state and predict the configuration of the major product; what changes in the major product if the substrate is replaced by (S)-2-benzyloxypropanal and the reaction with $\ce{CH3MgBr}$ is run in THF?

   **Answer** In the first reaction, L = Ph, M = $\ce{CH3}$, S = H. Viewed along the C2–C1 bond, Ph is placed perpendicular to the carbonyl plane, and Nu attacks at about $107^\circ$ from the direction anti to Ph and close to H, giving mainly (2S,3S)-3-phenylbutan-2-ol (about 2:1 to 3:1). In the second reaction, the α-OBn group can chelate $\ce{Mg^2+}$: Mg coordinates to both the carbonyl oxygen and the ether oxygen, fixing C=O and C–OBn in an eclipsed conformation on the same side, so that the remaining H and $\ce{CH3}$ lie on opposite sides of the carbonyl plane; the methyl nucleophile attacks from the side of H to give the chelation-controlled syn product ((2S,3S)-3-benzyloxybutan-2-ol) with high selectivity. It is the diastereomer of the product predicted by the polar Felkin–Anh model (OBn in the L position).

7. 4-tert-Butylcyclohexanone reacts with $\ce{(CH3)2S=CH2}$ to give mainly the epoxide with equatorial oxygen (64% versus 13%), and with $\ce{(CH3)2S(O)=CH2}$ to give mainly the product with axial epoxide oxygen (89%). Explain the difference in terms of the direction of attack and the reversibility of the reaction.

   **Answer** The conformation of 4-tert-butylcyclohexanone is locked by the tert-butyl group. $\ce{(CH3)2S=CH2}$ is a nonstabilized ylide and its addition is irreversible, so the product ratio is determined by the transition state of attack: when the small nucleophile attacks axially along the Bürgi–Dunitz trajectory, it avoids eclipsing with the equatorial C–H bonds at C2 and C6 (torsional strain), so $\ce{CH2}$ enters the axial position and O is equatorial, and ring closure gives the epoxide with equatorial O. $\ce{(CH3)2S(O)=CH2}$ is stabilized by S=O and its addition is reversible, so the axial adduct returns to the starting materials and the system finally flows to the adduct that is more stable before ring closure (the large $\ce{CH2S(O)Me2+}$ group equatorial, avoiding 1,3-diaxial interactions); ring closure gives the epoxide with equatorial $\ce{CH2}$ and axial O. This is a contrast between **kinetic control** and **thermodynamic control**.

8. Why is the rate of imine formation from a carbonyl compound and an amine highest at pH about 4.5? Which step becomes slower at pH 1 and at pH 10?

   **Answer** The first step needs the free amine as the nucleophile, and the second step (loss of water from the hemiaminal) needs acid to protonate the OH into a good leaving group. At pH 1 the amine is almost entirely protonated to the ammonium ion (the conjugate acid has a $\mathrm{p}K_{\mathrm{a}}$ of about 10), the concentration of free amine is very low, and the nucleophilic addition becomes slow and rate-determining. At pH 10 free amine is plentiful, but the OH of the hemiaminal is rarely protonated, so loss of water is slow and rate-determining. At pH 4–5 the compromise between the two gives the greatest overall rate.

9. What method converts the carbonyl group to a methylene group in each of the following? (a) 4-oxo-4-phenylbutanoic acid → 4-phenylbutanoic acid; (b) a compound containing both an acetal and a ketone carbonyl group, in which only the ketone is to be reduced; (c) a ketone containing an ester group.

   **Answer** (a) The substrate tolerates both acid and base, so the **Clemmensen reduction** (Zn(Hg)/concentrated HCl, [6.5.17](/6.5.17#sec-17.3.4)) or the Huang Minlon reduction can be used; this is a common step after Friedel–Crafts acylation. (b) Acetals are acid-sensitive, so use the Wolff–Kishner–Huang Minlon reduction (strong base, in which the acetal is stable). (c) The ester would be hydrolyzed under the strongly basic, high-temperature conditions of the Wolff–Kishner reduction and might also be hydrolyzed in the concentrated acid of the Clemmensen reduction; the mildest method is to form the thioketal with ethane-1,2-dithiol and $\ce{BF3*OEt2}$ and then desulfurize with Raney Ni in ethanol (neutral conditions).

10. Synthesize 1-phenylpentan-1-one (butyl phenyl ketone) from benzaldehyde by the 1,3-dithiane method, giving the reagents for each step, and explain why this route amounts to joining a "benzoyl anion" to 1-bromobutane.

    **Answer** (1) Benzaldehyde with propane-1,3-dithiol and $\ce{BF3*OEt2}$ (or HCl) gives 2-phenyl-1,3-dithiane; (2) $n$-BuLi, THF, $-30\,^\circ\mathrm{C}$, removes C2–H; (3) 1-bromobutane is added, and SN2 alkylation occurs; (4) hydrolysis with $\ce{HgCl2}$ and $\ce{CaCO3}$ in aqueous acetonitrile gives 1-phenylpentan-1-one. With the natural polarity, the carbonyl carbon of benzaldehyde can only accept nucleophiles and cannot be joined to 1-bromobutane, which is also an electrophile. In the dithiane anion this carbon is negatively charged and corresponds to a $\ce{PhC(=O)-}$ acyl anion, which bonds to the electrophilic carbon of the alkyl halide; this is the umpolung.

11. The benzoin condensation can be catalyzed by $\ce{CN-}$ or by vitamin B1. Write the two mechanisms side by side, state the three properties required of the catalyst, and explain why hydroxide or methoxide cannot catalyze the reaction.

    **Answer** In both mechanisms, the catalyst ($\ce{CN-}$ or the thiazolium carbene) adds to the carbonyl carbon of the first aldehyde molecule; a proton is transferred from the original aldehyde carbon to oxygen, giving a carbanion (in the case of $\ce{CN-}$) or the Breslow intermediate (an enaminol); this nucleophilic carbon attacks the second aldehyde molecule; and after proton transfer the catalyst leaves to give the α-hydroxy ketone. The catalyst must (1) be a good nucleophile that can add to the aldehyde; (2) after addition, acidify the C–H on the original aldehyde carbon and stabilize the resulting carbanion (by being electron-withdrawing and able to conjugate); and (3) finally be a good leaving group. $\ce{HO-}$ and $\ce{CH3O-}$ can add to aldehydes, but in the adducts the oxygen cannot stabilize an adjacent carbanion (it donates electrons instead), so the C–H is not removed; in concentrated base benzaldehyde undergoes the **Cannizzaro reaction** ([6.5.17](/6.5.17#sec-17.4)) instead.
