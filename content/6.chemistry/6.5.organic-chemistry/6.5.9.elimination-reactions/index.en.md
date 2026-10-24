---
title: Elimination Reactions
source_hash: 3de12b45c1e2
---

When an alkyl halide is treated with a **nucleophile**, the reagent can attack the $\alpha$ carbon and cause substitution ([6.5.8](/6.5.8)), or it can act as a base, abstracting a hydrogen from the $\beta$ carbon while the **leaving group** departs, to give a carbon–carbon double bond. Reactions of the second kind are called eliminations. They are the most widely used way of making alkenes, and they are always the competitor of substitution. In this chapter we first review briefly the structure, nomenclature and stability of alkenes, and then discuss the regioselectivity and stereochemistry of elimination according to the three mechanisms E1, E2 and E1cb. We summarize how to decide between substitution and elimination, and finally apply these conclusions to alcohols and ethers: halogenation, dehydration and ether formation of alcohols, and cleavage of the ether linkage.

This chapter depends on everything in [6.5.8](/6.5.8), on the conformational analysis of [6.5.4](/6.5.4) (the **Newman projection**, the **chair conformation** and the **axial bond**), and on the [pKa table](/6.5.3#sec-3.1.4), the **kinetic isotope effect** and **kinetic control** of [6.5.3](/6.5.3). The reverse of elimination is **electrophilic addition** ([6.5.11](/6.5.11#sec-11.3)); the E1cb mechanism is common in carbonyl chemistry, and the dehydration step of the **aldol reaction** ([6.5.22](/6.5.22#sec-22.1.2)) is one example.

## 9.1. Structure, Nomenclature and Stability of Alkenes

The double bond of an alkene consists of one $\sigma$ bond and one $\pi$ bond; the double-bond carbons are $\mathrm{sp^2}$ hybridized, and the four atoms directly bonded to them lie in one plane with the two double-bond carbons. The $\pi$ bond cannot rotate freely, so alkenes show cis–trans isomerism (Z/E, [6.5.5](/6.5.5#sec-5.1)). Structural parameters and the frontier orbitals are given in [6.5.11](/6.5.11#sec-11.1).

In naming, the longest chain containing the double bond is the main chain, the suffix is "-ene", the chain is numbered from the end nearer the double bond so that the double bond gets the lowest locant, and the locant is placed before "ene" (as in the current IUPAC recommendations):

```smiles
CC=CC(C)C 4-methylpent-2-ene
C=CC(C)CC 3-methylpent-1-ene
C/C=C/C1CCCCC1 (E)
CC1=CCCCC1 1-methylcyclohexene
```

They are 4-methylpent-2-ene (formerly 4-methyl-2-pentene), 3-methylpent-1-ene, (*E*)-prop-1-enylcyclohexane and 1-methylcyclohexene. In cycloalkenes the double-bond carbons are numbered 1 and 2.

The relative stabilities of alkenes can be compared by their enthalpies of hydrogenation: to give butane, but-1-ene releases $126.8\,\mathrm{kJ\,mol^{-1}}$, (*Z*)-but-2-ene $119.7$ and (*E*)-but-2-ene $115.5$ ([6.5.2](/6.5.2#sec-2.6)). The less heat released, the more stable the alkene. There are two rules:

- The more alkyl groups on the double-bond carbons, the more stable the alkene: tetrasubstituted > trisubstituted > disubstituted > monosubstituted > ethene. The main reason is **hyperconjugation** between the alkyl C–H bonds and the $\pi$ bond, together with the fact that an $\mathrm{sp^2}$–$\mathrm{sp^3}$ carbon–carbon bond is stronger than an $\mathrm{sp^3}$–$\mathrm{sp^3}$ bond.
- Trans is more stable than cis: the two cis alkyl groups on the same side repel each other (**steric strain**). *cis*-2,2,5,5-Tetramethylhex-3-ene is about $40\,\mathrm{kJ\,mol^{-1}}$ higher in energy than the trans isomer.

In small bridged rings the bridgehead carbon cannot form a double bond: the p orbitals of the double-bond carbons must be parallel, whereas the skeleton of a small bridged ring makes the p orbital of the bridgehead carbon almost orthogonal to that of the adjacent carbon. This empirical rule is called Bredt's rule; compounds such as bicyclo[2.2.1]hept-1-ene can be detected only as transient intermediates. It is also the reason why bridgehead halides undergo **SN1** reactions with difficulty ([6.5.8](/6.5.8#sec-8.5.3)).

## 9.2. β-Elimination and Zaitsev's Rule

**Definition 9.2.1 (Elimination Reaction)** A reaction in which one atom or group is removed from each of two adjacent atoms of the substrate molecule and a new $\pi$ bond (or a ring) is formed between the two atoms is called an **elimination reaction**. Removal of the leaving group from the $\alpha$ carbon and of a hydrogen from the $\beta$ carbon is called $\beta$-elimination (1,2-elimination):

$$
\ce{H-C_{\beta}-C_{\alpha}-X + B- -> C=C + B-H + X-}.
$$

Loss of hydrogen halide from an alkyl halide on heating with base in alcohol (dehydrohalogenation) is the most common $\beta$-elimination. When there is more than one $\beta$ carbon, different alkenes can form:

```smiles
CCC(C)Br>>C/C=C/C.C=CCC 81% : 19%
CCC(C)(C)Br>>CC=C(C)C.CCC(C)=C 71% : 29%
```

2-Bromobutane heated with KOH in ethanol gives 81% but-2-ene (mainly the E form) and 19% but-1-ene; 2-bromo-2-methylbutane gives 71% 2-methylbut-2-ene and 29% 2-methylbut-1-ene.

**Definition 9.2.2 (Zaitsev's Rule)** The empirical rule that in the $\beta$-elimination of an alkyl halide (or an alcohol) the main product is the alkene with more substituents on the double bond, formed by removal of a hydrogen from the $\beta$ carbon bearing fewer hydrogens, is called **Zaitsev's rule** (1875). The more highly substituted alkene is called the Zaitsev product.

The Zaitsev product is the thermodynamically more stable alkene (Section 9.1), and the transition states of both E1 and E2 already have partial double-bond character, so the factors that stabilize the product alkene also stabilize the transition state, and it is usually also the faster-forming product. But this is only an empirical rule: a bulky base, a poor leaving group or a positively charged leaving group steers the elimination toward the less substituted alkene (Section 9.4.3).

## 9.3. The E1 Mechanism

**Definition 9.3.1 (E1 Reaction)** A two-step elimination in which the substrate first ionizes to a carbocation (the rate-determining step) and the carbocation then loses a $\beta$-hydrogen to give the alkene is called an **E1 reaction** (unimolecular elimination). The rate law is $v = k_1[\ce{RX}]$.

![The E1 reaction: 2-bromo-2-methylbutane ionizes slowly in ethanol to the tertiary carbocation; ethanol acting as a base rapidly abstracts a proton from the adjacent CH2, the electron pair of the C–H bond becomes the π bond, and the Zaitsev product 2-methylbut-2-ene is formed](./plots/e1-mechanism.py)

The first step of E1 is exactly the same as that of **SN1**, and both go through the same **carbocation**; they differ only in the second step: combination of the carbocation with a nucleophile gives the substitution product (SN1), and loss of a $\beta$-hydrogen gives the alkene (E1). E1 and SN1 therefore always occur together, their ratio being decided by the second step of the carbocation and independent of the leaving group: *tert*-butyl bromide, *tert*-butyl chloride and *tert*-butyldimethylsulfonium ion give almost the same alkene/substitution product ratio on **solvolysis** in 80% ethanol, which shows that they go through the same "free" *tert*-butyl cation. Raising the temperature, or using weakly nucleophilic solvents or non-nucleophilic acids, increases the proportion of E1.

The characteristics of E1 are:

1. Two steps and two transition states, with a carbocation intermediate, so rearrangements often accompany it ([6.5.8](/6.5.8#sec-8.3.3)). For example, the alkene obtained from solvolysis of 1-bromo-2,2-dimethylpropane is mainly the rearranged 2-methylbut-2-ene: departure and methyl migration are concerted and the tertiary carbocation is formed directly, without passing through a primary carbocation.
2. The regioselectivity follows Zaitsev's rule: the transition state for loss of a proton to give the more highly substituted alkene is lower in energy (Section 9.2).
3. It is stereoselective but not stereospecific: the carbocation is planar, there is no geometric requirement as to which $\beta$-H is lost, and when both E and Z alkenes can form, the more stable E form predominates.
4. The order of reactivity is the same as for SN1: tertiary > secondary > primary; primary alkyl halides do not undergo E1.

![E1 with rearrangement: in the solvolysis of 1-bromo-2,2-dimethylpropane (neopentyl bromide), loss of bromide and the 1,2-shift of a methyl group with its bonding pair are concerted, so no primary carbocation forms and the tertiary carbocation is produced directly; ethanol removes a proton from the adjacent CH2, the C–H electron pair becomes the π bond, and the Zaitsev product 2-methylbut-2-ene results](./plots/e1-rearrangement.py)

## 9.4. The E2 Mechanism

### 9.4.1. Concerted Elimination and the Isotope Effect

**Definition 9.4.1 (E2 Reaction)** A one-step elimination in which the base abstracts a $\beta$-hydrogen, the electron pair of the C–H bond forms the $\pi$ bond, and the leaving group departs with the electron pair of the C–X bond, all three occurring simultaneously, is called an **E2 reaction** (bimolecular elimination). The rate law is $v = k_2[\ce{RX}][\ce{B-}]$.

![The E2 reaction: ethoxide abstracts the β-hydrogen that is antiperiplanar to bromine, the electron pair of the C–H bond enters between the carbons as the π bond, and bromine leaves with its electron pair, giving 2-methylpropene in one step](./plots/e2-mechanism.py)

E2 differs from **SN2** in the position attacked by the base: in SN2 the reagent acts as a nucleophile and attacks the $\alpha$ carbon, whereas in E2 it acts as a base and attacks the hydrogen at the $\beta$ position. The order of E2 reactivity is the opposite of that of SN2, tertiary > secondary > primary: the transition state already has partial double-bond character, so the more substituted the double bond formed, the more favorable it is; the base attacks an H at the periphery of the molecule and is not affected by hindrance at the $\alpha$ carbon. Under strongly basic conditions primary, secondary and tertiary alkyl halides can all undergo E2.

There is direct evidence for the concerted nature of E2. The elimination of 2-bromopropane and $\ce{(CD3)2CHBr}$ with sodium ethoxide in ethanol gives $k_{\mathrm{H}}/k_{\mathrm{D}} = 6.7$, close to the upper limit of a primary **kinetic isotope effect** ([6.5.3](/6.5.3#sec-3.11.4)), which shows that the C–H bond is broken in the rate-determining step; solvolysis of the same substrate under SN1/E1 conditions gives only a small secondary isotope effect for $\beta$-deuteration. The rate of E2 also depends on the leaving group ($\ce{RI} > \ce{RBr} > \ce{RCl}$), which shows that the C–X bond is broken in the rate-determining step too.

### 9.4.2. The Stereochemical Requirement: Antiperiplanar Geometry

**Definition 9.4.2 (Antiperiplanar)** The geometric relationship in which the torsion angle H–C$_\beta$–C$_\alpha$–X is $180^\circ$ (or close to $180^\circ$) is called **antiperiplanar** ([6.5.4](/6.5.4#sec-4.2.1)); the relationship in which the torsion angle is $0^\circ$ is called synperiplanar.

E2 elimination requires the H and X that are eliminated to be coplanar, in the great majority of cases antiperiplanar. There are both orbital and conformational reasons: the two p orbitals that form the $\pi$ bond must be parallel, so the C–H and C–X bonds should be coplanar in the transition state; in the antiperiplanar arrangement the C–H $\sigma$ bonding orbital and the C–X $\sigma^*$ antibonding orbital lie in the same plane and overlap best in phase, and the base and the leaving group are on opposite sides of the molecule, so the conformation is **staggered** and not **eclipsed**. Syn elimination takes place only when the molecule is rigid and cannot reach the antiperiplanar arrangement, and it is much slower.

The antiperiplanar requirement makes E2 a **stereospecific** reaction ([6.5.5](/6.5.5#sec-5.8.1)): the relative configuration of the substrate determines the configuration of the product alkene. *meso*-1,2-Dibromo-1,2-diphenylethane and sodium ethoxide give only (*E*)-1-bromo-1,2-diphenylethene, and the racemate gives only the (*Z*) isomer:

```smiles
Br[C@@H](c1ccccc1)[C@H](Br)c1ccccc1>>Br/C(c1ccccc1)=C/c1ccccc1 (E)
Br[C@@H](c1ccccc1)[C@@H](Br)c1ccccc1>>Br/C(c1ccccc1)=C\c1ccccc1 (Z)
```

The first line is the *meso* compound, and the second is one enantiomer of the racemate. A Newman projection with H and Br antiperiplanar shows why: in this conformation of the *meso* compound the Br on C1 and the phenyl on C2 are anti, so after elimination they are trans, which is the E form (the two phenyl groups cis); in the racemate they are gauche, giving the Z form (Question 2).

![Stereospecific E2 of the 1,2-dibromo-1,2-diphenylethanes in Newman projection along C1–C2, with the front H antiperiplanar to the back Br: in the *meso* isomer the front Br and the back phenyl are anti, so after elimination they are trans and the two phenyl groups are cis, giving (E)-1-bromo-1,2-diphenylethene; in the racemate (one enantiomer shown) they are gauche, giving the (Z) isomer](./plots/e2-stilbene-newman.py)

When the $\beta$ carbon bears two hydrogens and both conformations can reach the antiperiplanar arrangement, E2 is **stereoselective**: the conformation in which the two large groups are anti has the lower energy and also the lower transition state, and the E alkene predominates (the E : Z ratio of but-2-ene from 2-bromobutane is about 3 : 1). When the $\beta$ carbon bears only one hydrogen, there is only one antiperiplanar conformation, and the configuration of the product is determined entirely by the substrate, even if the less stable Z form results (Question 3).

### 9.4.3. Regioselectivity: Zaitsev and Hofmann Products

In E2 reactions with small strong bases ($\ce{HO-}$, $\ce{CH3O-}$, $\ce{C2H5O-}$), the transition state leading to the more highly substituted alkene is favorable electronically (the partly formed double bond is stabilized by hyperconjugation) and unfavorable sterically (the base must approach a more crowded CH or $\ce{CH2}$); the electronic effect wins, and Zaitsev's rule is obeyed. With a bulky base the steric effect wins, and the base preferentially abstracts a hydrogen from the less hindered and more numerous terminal methyl hydrogens:

| 2-Bromo-2-methylbutane + base | 2-Methylbut-2-ene (Zaitsev) | 2-Methylbut-1-ene (Hofmann) |
|---|---|---|
| $\ce{C2H5O- K+}$ / ethanol | 70% | 30% |
| $\ce{(CH3)3CO- K+}$ / *tert*-butyl alcohol | 28% | 72% |

![Regioselectivity of the E2 of 2-bromo-2-methylbutane: the small ethoxide ion removes a hydrogen from the inner CH2, the C–H electrons form the π bond and bromide leaves, giving mainly the more substituted Zaitsev product; the bulky *tert*-butoxide cannot easily reach the CH2 and removes one of the more numerous, less hindered methyl hydrogens, giving mainly the less substituted Hofmann product](./plots/hofmann-bulky-base.py)

**Definition 9.4.3 (Hofmann Rule)** A $\beta$-elimination whose main product is the alkene with fewer substituents on the double bond (formed by removal of hydrogen from the $\beta$ carbon bearing more hydrogens) is said to obey the **Hofmann rule**, and the less substituted alkene formed is called the Hofmann product.

There are three kinds of cases in which the Hofmann rule is obeyed: (1) bulky bases ($t$-BuOK, **LDA**, LiHMDS); (2) positively charged leaving groups, as in the **Hofmann elimination** of **quaternary ammonium salts** ($\ce{R-NMe3+}$, [6.5.23](/6.5.23#sec-23.8.2)) and the elimination of sulfonium salts ($\ce{R-SMe2+}$); and (3) poor leaving groups, such as alkyl fluorides. In the last two cases the C–X bond is less broken and the C–H bond more broken in the transition state, which has **carbanion** character ("E2 with E1cb character", Section 9.5); the more stable carbanion is the primary one, so the terminal hydrogen leaves more readily.

This regularity was discovered by Hofmann in 1851 in his study of the pyrolysis of quaternary ammonium hydroxides, more than twenty years before Zaitsev's rule.

### 9.4.4. E2 in Cyclohexane Systems

In cyclohexane the substituents on two adjacent carbons are antiperiplanar only when both occupy **axial bonds** (trans-diaxial); neither the C–X bond nor the ring C–H bonds are anti to a leaving group on an **equatorial bond**. The leaving group must therefore be axial and can eliminate only with an axial hydrogen on the adjacent carbon; a leaving group in an equatorial position must first undergo a **ring flip**.

- *cis*-1-Bromo-4-*tert*-butylcyclohexane: the *tert*-butyl group is locked equatorial ([6.5.4](/6.5.4#sec-4.6.1)), so bromine can only be axial, both adjacent carbons have trans axial hydrogens, and E2 with $\ce{CH3O-}$ is fast. In the trans isomer bromine is locked equatorial, and the ring would have to flip to the high-energy conformation with an axial *tert*-butyl group before elimination; the reaction is much slower.
- Menthyl chloride and neomenthyl chloride: in its stable chair conformation neomenthyl chloride has the isopropyl and methyl groups equatorial and chlorine axial, with trans-diaxial hydrogens on both adjacent carbons; E2 is fast and the main product is the Zaitsev product, menth-3-ene (about 3 : 1). In menthyl chloride all three substituents are equatorial, and the ring must flip to the conformation with all three axial, in which only C2 bears a trans axial hydrogen; the reaction is slower by a factor of about 200 and gives only the Hofmann-type menth-2-ene.

```smiles
CC(C)[C@@H]1CC[C@@H](C)C[C@@H]1Cl neomenthyl chloride
CC(C)[C@@H]1CC[C@@H](C)C[C@H]1Cl menthyl chloride
```

![E2 on the cyclohexane chair: in the stable chair of neomenthyl chloride the isopropyl and methyl groups are equatorial and chlorine is axial, and both neighboring carbons carry an axial hydrogen anti to chlorine; ethoxide removes the axial hydrogen on C2, elimination is fast, and 3-menthene is the main product. In menthyl chloride all three groups are equatorial; the ring must flip to the all-axial chair, in which only C6 has an axial hydrogen anti to chlorine (the C2 hydrogen has become equatorial), so elimination is about 200 times slower and gives only 2-menthene](./plots/menthyl-e2.py)

## 9.5. The E1cb Mechanism and the Spectrum of Elimination Mechanisms

### 9.5.1. E1cb

**Definition 9.5.1 (E1cb Reaction)** A two-step elimination in which a base first abstracts a $\beta$-hydrogen to give a carbanion (the conjugate base of the substrate), and the carbanion then expels the leaving group to form the double bond, is called an **E1cb reaction** (unimolecular elimination via the conjugate base). If the second step is rate-determining and the first is a fast equilibrium, the rate law is $v = kK[\ce{RX}][\ce{B-}]/[\ce{BH}]$.

E1cb requires the $\beta$-hydrogen to be sufficiently acidic and the **carbanion** formed to be sufficiently stable: the $\beta$ carbon bears an electron-withdrawing group such as carbonyl, nitro, cyano or sulfonyl, onto which the negative charge can be delocalized. Poor leaving groups such as $\ce{HO-}$ and $\ce{RO-}$ can then be expelled as well. The most important example is the dehydration of $\beta$-hydroxy carbonyl compounds:

![The E1cb elimination: hydroxide abstracts the acidic proton at the α position of the carbonyl group of 4-hydroxy-4-methylpentan-2-one to give an enolate (drawn as a carbanion), and HO⁻ is then expelled from the adjacent carbon to give the conjugated 4-methylpent-3-en-2-one](./plots/e1cb-mechanism.py)

This step is the last step of the **aldol reaction** ([6.5.22](/6.5.22#sec-22.1.2)), and the $\alpha,\beta$-unsaturated carbonyl product is stabilized by conjugation, which drives the equilibrium. In biology, enolase dehydrates 2-phosphoglycerate to phosphoenolpyruvate in glycolysis, and the dehydration of $\beta$-hydroxyacyl-ACP in fatty acid synthesis is also an E1cb-type elimination.

The stereochemistry of E1cb differs from that of E2: the carbanion intermediate is planar (or inverts rapidly) and can rotate about the C–C bond before the leaving group is lost, so E1cb has no antiperiplanar requirement, and the product is mainly the thermodynamically more stable alkene. Experimental evidence for E1cb is that, in $\ce{D2O}$/$\ce{DO-}$, the $\beta$-H of recovered starting material has been exchanged for D (the first step is reversible and faster than elimination).

Vicinal dihalides lose halogen on heating with zinc or magnesium to give alkenes:

$$
\ce{BrCH2CH2Br + Zn -> CH2=CH2 + ZnBr2}.
$$
This dehalogenation goes through metal insertion or **single electron transfer** and in many systems is an anti elimination; it is not an E1cb reaction, and it is used mainly to protect double bonds (bromine is added first and removed afterwards). Two successive E2 eliminations of a vicinal or geminal dihalide with $\ce{NaNH2}$ give an alkyne, one of the methods for preparing alkynes ([6.5.11](/6.5.11#sec-11.13)).

![Debromination of 1,2-dibromoethane with zinc: zinc inserts into one C–Br bond (by electron transfer from the metal surface) to give 2-bromoethylzinc bromide; the electron pair of the polar C–Zn bond forms the π bond while bromide leaves from the neighboring carbon, giving ethene and ZnBr2](./plots/zn-dehalogenation.py)

### 9.5.2. The E1–E2–E1cb Spectrum

The three mechanisms can be viewed as a continuous spectrum, arranged by the order in which the C–X and C–H bonds break in the transition state:

| | E1 | E2 | E1cb |
|---|---|---|---|
| Order of bond breaking | C–X breaks first | C–X and C–H simultaneously | C–H breaks first |
| Intermediate | Carbocation | None | Carbanion |
| Favorable substrates | Those that form stable carbocations easily (tertiary, benzylic) | Ordinary alkyl halides, sulfonates | Acidic $\beta$-H (electron-withdrawing group at the $\beta$ position) |
| Favorable conditions | Weak base, polar protic solvent | Strong base | Strong base, poor leaving group |
| Stereochemistry | Not specific, E form predominates | Antiperiplanar, stereospecific | Not specific, thermodynamic product |
| Regioselectivity | Zaitsev | Zaitsev (small base) or Hofmann (bulky base, charged leaving group) | The most acidic H is removed |

The transition state of E2 can itself lean toward either end: a "E1-like" transition state with more C–X cleavage has carbocation character and gives the Zaitsev product; an "E1cb-like" transition state with more C–H cleavage has carbanion character and gives the Hofmann product. The position of the transition state on the spectrum can be determined by heavy-atom isotope effects: in the **Hofmann elimination** of quaternary ammonium salts, the nitrogen isotope effect $k_{14}/k_{15}$ is 1.017 for $\ce{CH3CH2NMe3+}$ and 1.009 for $\ce{C6H5CH2CH2NMe3+}$, which shows that when the phenyl group makes the $\beta$-H more acidic, C–N cleavage in the transition state decreases and the transition state moves toward the E1cb end.

## 9.6. Competition Between Substitution and Elimination

### 9.6.1. Basis of the Decision

When an alkyl halide reacts with a nucleophile (base), all four mechanisms, **SN2**, **SN1**, E2 and E1, are possible. The steps in deciding the main product are:

1. Judge the nature of the reagent: the strengths of **nucleophilicity** and basicity ([6.5.8](/6.5.8#sec-8.7.1)).
2. Judge the type of substrate: methyl, primary, secondary or tertiary; whether it is allylic or benzylic; whether there is branching at the $\beta$ position.
3. From these determine the mechanism, and then the regioselectivity and stereochemistry.

Reagents can be divided into four classes:

| Type of reagent | Examples | Characteristics |
|---|---|---|
| Strong base, weak nucleophile | NaH, DBU, DBN, $t$-BuOK, **LDA** | Bulky or reacting only with protons; almost exclusively E2 |
| Strong base, strong nucleophile | $\ce{HO-}$, $\ce{CH3O-}$, $\ce{C2H5O-}$, $\ce{H2N-}$ | Negatively charged and strongly basic; SN2 and E2 compete |
| Weak base, strong nucleophile | $\ce{I-}$, $\ce{Br-}$, $\ce{Cl-}$, $\ce{RS-}$, $\ce{HS-}$, $\ce{RSH}$, $\ce{H2S}$, $\ce{N3-}$, $\ce{CN-}$, $\ce{RCOO-}$ | Highly polarizable or with fairly strong conjugate acids; mainly SN2 |
| Weak base, weak nucleophile | $\ce{H2O}$, $\ce{CH3OH}$, $\ce{C2H5OH}$ | Neutral molecules that can only wait for a carbocation to form: SN1 and E1 |

(The $\mathrm{p}K_{\mathrm{a}}$ of HCN, the conjugate acid of $\ce{CN-}$, is 9.21, that of $\ce{RSH}$ is about 10.5 and that of $\ce{HN3}$ is 4.72, all far lower than those of $\ce{H2O}$ (14.00) and $\ce{C2H5OH}$ (15.9); data in [6.5.3](/6.5.3#sec-3.1.4).)

Combining substrates with reagents gives the table for judging the main reaction:

| Substrate | Strong base, weak nucleophile | Strong base, strong nucleophile | Weak base, strong nucleophile | Weak base, weak nucleophile |
|---|---|---|---|---|
| Methyl | — | SN2 | SN2 | No reaction |
| Primary | E2 | Mainly SN2 (E2 with $\beta$ branching or with $t$-BuOK) | SN2 | No reaction |
| Secondary | E2 | Mainly E2, a little SN2 | SN2 | Slow SN1/E1 (solvolysis) |
| Tertiary | E2 | E2 | SN1 (with a little E1) | SN1 and E1 |

A secondary alkyl halide with a weak base and weak nucleophile (for example, heated in ethanol) does not fail to react but undergoes slow **solvolysis** (SN1/E1, often with rearrangement), much more slowly than a tertiary halide.

For example, 2-chloropentane and sodium ethoxide in ethanol: a secondary halide with a strong base and strong nucleophile reacts mainly by E2, the Zaitsev product (*E*)-pent-2-ene being the largest, followed by (*Z*)-pent-2-ene and pent-1-ene, with a little of the SN2 product 2-ethoxypentane (with inversion of configuration).

```smiles
CCC[C@H](C)Cl>>CC/C=C/C.CC/C=C\C.CCCC=C.CCC[C@@H](C)OCC
```

### 9.6.2. Temperature and Other Factors

- Temperature: raising the temperature favors elimination. Elimination produces three molecules (alkene, BH, $\ce{X-}$) from two (substrate and base), so $\Delta_{\mathrm{r}}S > 0$; its entropy of activation is also more positive than that of substitution and its enthalpy of activation higher. The higher the temperature, the more the $-T\Delta S$ term favors elimination.
- Concentration and strength of the base: a concentrated strong base favors E2; a dilute weak base favors SN1/E1.
- Solvent: solvents of lower polarity (such as ethanol compared with water) favor E2; $t$-BuOK in DMSO is an extremely strong base.
- Branching at the $\beta$ position: it slows SN2 and does not affect, or even accelerates, E2, so primary alkyl halides with $\beta$ branching often undergo E2.

## 9.7. Substitution Reactions of Alcohols

The hydroxy group of an alcohol is a very poor leaving group (the $\mathrm{p}K_{\mathrm{a}}$ of the conjugate acid of $\ce{HO-}$ is 14.00), and the key to substitution and elimination of alcohols is first to convert OH into a good **leaving group** ([6.5.8](/6.5.8#sec-8.6)): by protonation in acid to $\ce{ROH2+}$, by coordination to a Lewis acid, or by conversion to a sulfonate, sulfite or phosphite ester.

### 9.7.1. Reaction with Hydrogen Halides

$$
\ce{R-OH + HX -> R-X + H2O}.
$$

Reactivity: for the alcohol, tertiary > secondary > primary; for the hydrogen halide, HI > HBr > HCl ≫ HF (in agreement with the **nucleophilicity** of $\ce{X-}$; $\ce{F-}$, the conjugate base of HF, is weakly nucleophilic, and HF is a weak acid). A tertiary alcohol is protonated and then loses water to give a **carbocation** (SN1), and reacts with concentrated hydrochloric acid at room temperature; a primary alcohol, after protonation, is attacked by $\ce{X-}$ by SN2, which requires more forcing conditions (HBr at reflux, or $\ce{NaBr + H2SO4}$); a secondary alcohol lies between the two and is often accompanied by rearrangement and elimination. The reaction of a primary alcohol with HCl is very slow and requires the Lewis acid $\ce{ZnCl2}$, which coordinates to the hydroxyl oxygen and makes the C–O bond break more easily.

![SN1 reaction of a tertiary alcohol with concentrated hydrochloric acid: the hydroxy oxygen of 2-methylpropan-2-ol takes a proton from HCl, the protonated alcohol loses water (rate-determining) to give the *tert*-butyl cation, and chloride combines with it rapidly to give 2-chloro-2-methylpropane](./plots/alcohol-hx-sn1.py)

![SN2 reaction of a primary alcohol with hydrobromic acid: the hydroxy oxygen of butan-1-ol takes a proton from HBr, turning the hydroxy group into water, a good leaving group; bromide attacks the CH2 carbon from the back side as water leaves, with no primary carbocation, giving 1-bromobutane](./plots/alcohol-hx-sn2.py)

A solution of concentrated hydrochloric acid and anhydrous $\ce{ZnCl2}$ is called Lucas reagent and can distinguish primary, secondary and tertiary alcohols of up to six carbons (soluble in the reagent): tertiary alcohols (and allylic and benzylic alcohols) react immediately, and the insoluble alkyl chloride formed makes the solution turbid or separate into layers; secondary alcohols turn turbid after a few minutes; primary alcohols are unchanged at room temperature for a long time.

![The role of ZnCl2 in Lucas reagent (butan-2-ol as the example): the Lewis acid ZnCl2 coordinates to the hydroxy oxygen, the weakened C–O bond ionizes to a secondary carbocation and [ZnCl2(OH)]⁻, and chloride captures the carbocation; the 2-chlorobutane formed is insoluble in the reagent and makes the solution cloudy](./plots/lucas-zncl2.py)

### 9.7.2. Reaction with Phosphorus Halides

Primary and secondary alcohols are commonly converted into alkyl bromides with $\ce{PBr3}$ (or red phosphorus and bromine), into alkyl chlorides with $\ce{PCl3}$ or $\ce{PCl5}$, and into alkyl iodides with red phosphorus and iodine:

$$
\ce{3 ROH + PBr3 -> 3 RBr + H3PO3}.
$$

The mechanism has two steps: the lone pair of the alcohol oxygen attacks phosphorus and displaces one $\ce{Br-}$ to give the protonated phosphite $\ce{RO(H+)PBr2}$, which loses a proton, and $\ce{-OPBr2}$ is a good leaving group; $\ce{Br-}$ then attacks the carbon from the back by SN2 to give RBr and $\ce{HOPBr2}$, which goes on to react with the alcohol. There is no carbocation, so the reaction does not rearrange and a chiral secondary alcohol is inverted. Alcohols with $\beta$ branching, such as neopentyl alcohol, can also be converted into unrearranged bromides with $\ce{PBr3}$, whereas HBr causes rearrangement.

![(R)-Butan-2-ol and PBr3 give (S)-2-bromobutane: the hydroxy oxygen attacks phosphorus and displaces a bromide ion, giving a protonated dibromophosphite; after loss of the proton OPBr2 is a good leaving group, and bromide attacks the carbon from the back side (SN2), with no rearrangement and with inversion of configuration](./plots/pbr3.py)

### 9.7.3. Reaction with Thionyl Chloride: SNi

$$
\ce{R-OH + SOCl2 -> R-Cl + SO2 ^ + HCl ^}.
$$
Both by-products are gases and easily separated, which makes this the most convenient laboratory method for making alkyl chlorides; it too does not rearrange.

In the first step of the mechanism the alcohol attacks sulfur and loses $\ce{Cl-}$ and a proton to give the chlorosulfite $\ce{R-O-S(=O)Cl}$. The stereochemistry of the second step depends on the conditions:

![First step of the reaction of an alcohol with thionyl chloride: the hydroxy oxygen attacks sulfur and displaces chloride, and loss of the proton (as HCl) gives the alkyl chlorosulfite R–O–S(=O)Cl; the C–O bond is untouched, so the configuration of the carbon is unchanged](./plots/socl2-chlorosulfite.py)

**Definition 9.7.1 (SNi Mechanism)** The C–O bond of the chlorosulfite undergoes heterolysis to give a tight ion pair of a carbocation and $\ce{-OS(O)Cl}$; as the latter leaves it decomposes to $\ce{SO2}$ and $\ce{Cl-}$, and $\ce{Cl-}$ combines with the carbon on the same face from which the C–O bond departed, so that the configuration is retained. This substitution completed within the ion pair is called the **SNi mechanism** (internal nucleophilic substitution).

```smiles
C[C@@H](O)CCCCCC>>C[C@@H](Cl)CCCCCC retention
```

- Without base (or in diethyl ether or dioxane): SNi, with retention of configuration. In dioxane the solvent oxygen first attacks from the back (the first inversion) and $\ce{Cl-}$ then displaces the dioxane (the second inversion), and the result is also retention.
- With pyridine: pyridine combines with HCl, the concentration of free $\ce{Cl-}$ (as the pyridinium salt) increases, and it attacks the chlorosulfite from the back by SN2, with inversion of configuration.

![The two stereochemical outcomes of the second step: top, without base (SNi) the C–O bond ionizes to a tight ion pair of the carbocation and the chlorosulfite anion, which falls apart on the same face into SO2 and chloride, so chlorine takes the place of oxygen with retention of configuration; bottom, with pyridine free chloride attacks the chlorosulfite from the back side by SN2, with inversion](./plots/sni-vs-sn2.py)

SNi requires a fairly stable carbocation and is most evident for secondary and benzylic alcohols; primary alcohols react mainly by SN2 even without base. When a chiral alcohol is to be converted cleanly into a halide with inversion, SN2 of the sulfonate ([6.5.8](/6.5.8#sec-8.6)), $\ce{PBr3}$, or under mild conditions the **Appel reaction** ($\ce{PPh3/CBr4}$, [6.5.26](/6.5.26#sec-26.6.4)) and the **Mitsunobu reaction** ([6.5.26](/6.5.26#sec-26.6.3)) are usually used.

## 9.8. Dehydration of Alcohols

### 9.8.1. Intramolecular Dehydration to Alkenes

Heating an alcohol with concentrated sulfuric acid, phosphoric acid or $\ce{KHSO4}$ removes a molecule of water and gives an alkene:

$$
\ce{CH3CH2OH ->[\text{conc. } H2SO4][170\,^\circ C] CH2=CH2 + H2O}.
$$

Reactivity: tertiary > secondary > primary alcohols. A tertiary alcohol dehydrates in dilute sulfuric acid at $25$–$80\,^\circ\mathrm{C}$, a secondary alcohol needs concentrated acid at about $100\,^\circ\mathrm{C}$, and a primary alcohol needs concentrated sulfuric acid at $170$–$180\,^\circ\mathrm{C}$.

The dehydration of tertiary and secondary alcohols proceeds by E1: the hydroxy group is protonated, water leaves to give a carbocation (the rate-determining step), and a $\beta$-proton is then lost. The product follows Zaitsev's rule, is mainly the E isomer, and is often rearranged. The dehydration of primary alcohols does not go through a primary carbocation: a base ($\ce{HSO4-}$ or another molecule of alcohol) abstracts the $\beta$-H of the protonated primary alcohol while water leaves, that is, by the E2 mechanism, since a primary carbocation cannot exist as an intermediate in solution. Dehydration is reversible, and its reverse is the acid-catalyzed hydration of alkenes ([6.5.11](/6.5.11#sec-11.4.1)); heating and distilling off the alkene as it forms favors dehydration.

![Dehydration of a primary alcohol in hot concentrated sulfuric acid: a primary carbocation is too unstable to be an intermediate; after protonation of the hydroxy group, hydrogensulfate (or another alcohol molecule) removes a β-hydrogen, the C–H electron pair becomes the π bond and water leaves at the same time, an E2 elimination of the protonated alcohol](./plots/dehydration-e2-primary.py)

An example of rearrangement: 3,3-dimethylbutan-2-ol heated in phosphoric acid gives mainly products with a changed skeleton:

```smiles
CC(O)C(C)(C)C>>CC(C)=C(C)C.C=C(C)C(C)C.C=CC(C)(C)C 64% : 33% : 3%
```

The secondary carbocation becomes a tertiary carbocation by a 1,2-methyl shift, and loss of a proton gives 2,3-dimethylbut-2-ene (64%, Zaitsev) and 2,3-dimethylbut-1-ene (33%); the unrearranged 3,3-dimethylbut-1-ene is only 3%. Rearrangement can also expand a ring: 1-cyclobutylethanol dehydrates in acid to 1-methylcyclopentene, the ring bond of the 1-cyclobutylethyl cation migrating to give the cyclopentyl cation and releasing about $85\,\mathrm{kJ\,mol^{-1}}$ of **ring strain** (Question 5).

![Acid-catalyzed dehydration of 3,3-dimethylbutan-2-ol (E1 with rearrangement): the protonated alcohol loses water to give a secondary carbocation; a methyl group on the neighboring quaternary carbon migrates with its bonding pair (1,2-methyl shift) to give the more stable tertiary cation; water removes a proton from the adjacent CH, giving 2,3-dimethylbut-2-ene](./plots/dehydration-rearrangement.py)

![Ring expansion in the dehydration of 1-cyclobutylethanol: the protonated alcohol loses water to give the secondary 1-cyclobutylethyl cation, a ring C–C bond migrates to the cationic carbon and enlarges the four-membered ring to a five-membered one (a cyclopentyl cation, relieving about 85 kJ/mol of ring strain), and loss of a proton gives 1-methylcyclopentene](./plots/ring-expansion.py)

### 9.8.2. Intermolecular Dehydration to Ethers

At lower temperatures a primary alcohol undergoes intermolecular dehydration in concentrated sulfuric acid to give an ether:

$$
\ce{2 CH3CH2OH ->[\text{conc. } H2SO4][140\,^\circ C] CH3CH2OCH2CH3 + H2O}.
$$
The mechanism is SN2: the oxygen of one molecule of alcohol attacks the $\alpha$ carbon of another protonated alcohol, water leaves, and the protonated ether loses a proton. Intramolecular dehydration (elimination) and intermolecular dehydration (substitution) compete, and temperature is the deciding factor: high temperature favors elimination (entropy, Section 9.6.2) and lower temperature favors ether formation. The method is suitable only for making symmetrical primary alkyl ethers; secondary and tertiary alcohols dehydrate mainly to alkenes; mixed ethers are made by the **Williamson ether synthesis** ([6.5.10](/6.5.10#sec-10.2.2)).

![Intermolecular dehydration of ethanol to diethyl ether in concentrated sulfuric acid (SN2): the oxygen of one ethanol molecule attacks the CH2 carbon of a protonated ethanol molecule from the back side as water leaves, and the protonated ether then loses a proton](./plots/ether-formation.py)

## 9.9. Cleavage and Elimination of Ethers

### 9.9.1. Acidic Cleavage

Ethers are stable toward bases, oxidizing agents and reducing agents and are widely used as solvents; but on heating with concentrated HI or HBr the C–O bond is cleaved:

$$
\ce{R-O-R' + HX -> R-X + R'-OH}, \qquad \ce{R'-OH + HX -> R'-X + H2O}.
$$
HI > HBr ≫ HCl (57% HI, or KI with phosphoric acid, is commonly used). The ether is first protonated to a dialkyloxonium ion, which makes ROH a good leaving group; the substitution that follows proceeds by one of two mechanisms:

- Methyl or primary alkyl: $\ce{X-}$ attacks the less hindered carbon by SN2. Methyl alkyl ethers other than methyl *tert*-butyl ether always give iodomethane first.
- Tertiary alkyl (and benzyl, allyl): the protonated ether ionizes to a stable carbocation (SN1), and cleavage occurs even with a weaker acid (such as trifluoroacetic acid); in the absence of a good nucleophile E1 occurs and an alkene is formed. *tert*-Butyl ethers can therefore serve as **protecting groups** for alcohols: they are stable under basic and nucleophilic conditions and are removed in acid, releasing 2-methylpropene.

The order in which C–O bonds are cleaved is tertiary alkyl > secondary > primary > methyl (the order of SN1), whereas under SN2 conditions methyl > primary (the order of steric hindrance); both are far easier than cleavage of an aryl–O bond: the phenyl–O bond has partial double-bond character, and an aromatic ring cannot undergo SN1 or SN2. Anisole and HI therefore give only phenol and iodomethane and do not give iodobenzene. In the laboratory, aryl methyl ethers are often cleaved to phenols with $\ce{BBr3}$ at low temperature.

```smiles
COc1ccccc1.I>>Oc1ccccc1.CI
CC(C)(C)OC.I>>CC(C)(C)I.CO
```

(Cleavage of methyl *tert*-butyl ether is SN1, with iodine ending up on the *tert*-butyl group; cleavage of anisole is SN2 at the methyl group.)

![Cleavage of ethers by hydroiodic acid: top, in protonated anisole iodide attacks the methyl carbon by SN2 and the aryl–O bond stays intact, giving phenol and iodomethane; bottom, protonated *tert*-butyl methyl ether ionizes to the *tert*-butyl cation and methanol (SN1), and the cation is captured by iodide to give 2-iodo-2-methylpropane or, without a good nucleophile, loses a proton (E1) to give 2-methylpropene, which is how *tert*-butyl protecting groups are removed](./plots/ether-cleavage.py)

The three-membered ring of **epoxides** is highly strained and can be opened by nucleophiles even under basic conditions; see [6.5.10](/6.5.10#sec-10.9).

### 9.9.2. Elimination of Ethers

Simple ethers undergo elimination with difficulty, because $\ce{RO-}$ is a very poor leaving group. Extremely strong bases such as alkyllithiums, sodium amide and **LDA** can make ethers eliminate to alkenes (often with side reactions); such reactions mostly follow an E1cb or E1cb-like mechanism because of the extremely strong base required. Other pathways also exist: labeling experiments with $\ce{PhCD2OEt}$ show that benzyl ethyl ether first loses a proton at the benzylic position, and the carbanion formed abstracts the $\beta$-H of the ethyl group through a five-membered transition state while the C–O bond breaks and ethene is released ($\alpha',\beta$-elimination). When there is an electron-withdrawing group at the $\beta$ position, elimination is much easier: diethyl 2-(ethoxymethyl)malonate loses ethanol on mere heating to give diethyl methylenemalonate (E1cb). *tert*-Butyl ethers undergo E1 elimination readily in acid (Section 9.9.1).

![α′,β-Elimination of benzyl ethyl ether: a very strong base (an alkyllithium) first removes a benzylic proton; the carbanion takes a hydrogen from the ethyl CH3 group through a five-membered cyclic transition state, the C–H electron pair forms the C=C bond and the C–O bond breaks at the same time, releasing ethene and the benzyl alkoxide](./plots/benzyl-ether-elimination.py)

## 9.10. Research Frontier: Controlled Elimination

The regio- and stereoselectivity of elimination is an old problem in synthesis and a field in which new methods keep appearing. One example is the replacement of the base by a transition-metal catalyst: palladium or nickel inserts into a C–X bond and then forms the alkene by **β-hydride elimination** ([6.5.28](/6.5.28#sec-28.4.5)), and metal hydrides can add and eliminate repeatedly along the carbon chain ("chain walking"), forming the double bond selectively at a position remote from the functional group. Another is the dehydrogenative olefination by **photoredox catalysis** ([6.5.31](/6.5.31#sec-31.5)), which forms alkenes directly from C–H bonds at room temperature. In living organisms, dehydratases and lyases control the geometry of the product precisely by the E1cb mechanism: for example, the dehydration of malate catalyzed by fumarase gives only trans fumarate, and it is strictly an anti elimination, the stereochemistry having been established with D labeling and the Newman-projection analysis of this chapter.

## Summary

- $\beta$-Elimination (Definition 9.2.1) removes H and X from two adjacent carbons to give an alkene. The stability of alkenes increases with the number of substituents on the double bond, and trans is more stable than cis (Section 9.1); Zaitsev's rule (Definition 9.2.2) states that the main product is usually the more highly substituted alkene.
- The three mechanisms:

  | | E1 (Definition 9.3.1) | E2 (Definition 9.4.1) | E1cb (Definition 9.5.1) |
  |---|---|---|---|
  | Rate law | $k[\ce{RX}]$ | $k[\ce{RX}][\ce{B-}]$ | Depends on which step is slow |
  | Intermediate | Carbocation (rearrangement) | None | Carbanion |
  | Stereochemistry | Stereoselective (E predominates) | Antiperiplanar (Definition 9.4.2), stereospecific | No geometric requirement |
  | Regioselectivity | Zaitsev | Zaitsev; Hofmann (Definition 9.4.3) with bulky bases, positively charged or poor leaving groups | The most acidic H |
  | Typical substrates | Tertiary, secondary; weak bases | All kinds of alkyl halides; strong bases | Carbonyl, nitro or cyano at the $\beta$ position |

- E2 in cyclohexanes requires trans-diaxial H and X; the conformation determines the rate and the regioselectivity (neomenthyl chloride and menthyl chloride).
- Competition between substitution and elimination (Section 9.6): first judge the reagent (nucleophilicity and basicity) and then the type of substrate; strong bases and high temperature favor elimination, weak bases with strong nucleophiles favor SN2, and weak bases with weak nucleophiles (solvents) lead tertiary and secondary substrates to SN1/E1.
- Alcohols (Sections 9.7 and 9.8): HX (tertiary alcohols by SN1, primary by SN2, rearrangement possible; Lucas test), $\ce{PBr3}$ (SN2, inversion, no rearrangement), $\ce{SOCl2}$ (SNi with retention without base, Definition 9.7.1; inversion with pyridine); acid-catalyzed dehydration (tertiary and secondary by E1 with rearrangement, primary by E2), and at lower temperature intermolecular dehydration of primary alcohols to ethers (SN2).
- Ethers (Section 9.9): HI and HBr cleave the C–O bond, methyl and primary by SN2, tertiary by SN1; the aryl–O bond is not cleaved, and anisole gives phenol and iodomethane.

## Questions

1. Predict the main products and mechanisms when 2-bromo-2-methylbutane is (a) heated in ethanol, (b) treated with sodium ethoxide in ethanol, and (c) treated with potassium *tert*-butoxide in *tert*-butyl alcohol.

   **Answer** (a) A weakly basic, weakly nucleophilic protic solvent; the tertiary halide ionizes to the tertiary carbocation: SN1 gives 2-ethoxy-2-methylbutane, and E1 gives 2-methylbut-2-ene (Zaitsev, the main alkene) and a little 2-methylbut-1-ene; heating increases the proportion of E1. (b) A strong base; a tertiary halide cannot undergo SN2, and E2 occurs, mainly to the Zaitsev product 2-methylbut-2-ene (about 70%). (c) A bulky strong base; the regioselectivity of E2 shifts to the Hofmann product 2-methylbut-1-ene (about 72%).

2. Explain with Newman projections why *meso*-1,2-dibromo-1,2-diphenylethane and sodium ethoxide give only (*E*)-1-bromo-1,2-diphenylethene.

   **Answer** Looking along the C1–C2 bond, take the conformation in which the H on C1 and the Br on C2 are antiperiplanar. The two stereocenters of the *meso* compound have opposite configurations, and in this conformation the Br on C1 and the phenyl on C2 are anti, and the two phenyl groups are gauche. After elimination, the groups that were anti become trans across the double bond: the Br on C1 and the phenyl on C2 are trans and the two phenyl groups are cis. By CIP rules, Br > Ph on C1 and Ph > H on C2, and the higher-priority groups are on opposite sides, which is the (*E*) configuration. The racemate (R,R or S,S) in the same conformation has the Br on C1 gauche to the phenyl on C2, and gives the (*Z*) isomer. Note that the E form here is the isomer with the two phenyl groups cis, and E/Z must not be confused with whether two large groups are cis or trans.

3. The two diastereomers (3*S*,4*S*) and (3*S*,4*R*) of 3-bromo-2,2,4-trimethylhexane are treated with sodium ethoxide. What configuration of 2,2,4-trimethylhex-3-ene does each give?

   ```smiles
   CC(C)(C)[C@@H](Br)[C@@H](C)CC (3S,4S)
   CC(C)(C)[C@@H](Br)[C@H](C)CC (3S,4R)
   ```

   **Answer** C4 bears only one hydrogen, so E2 can proceed only through the one conformation in which C4–H and C3–Br are antiperiplanar, and the configuration of the product is determined by the substrate (stereospecific). In this conformation the *tert*-butyl group of the (3*S*,4*S*) isomer is gauche to the ethyl group on C4, so after elimination they are on the same side, giving (*Z*)-2,2,4-trimethylhex-3-ene; in the (3*S*,4*R*) isomer the *tert*-butyl and ethyl groups are anti, giving the (*E*) isomer. Even though the Z form is more crowded, (3*S*,4*S*) can give only it: the antiperiplanar requirement outweighs product stability.

4. Which of the following two chlorides undergoes E2 more readily? Draw the products of each.

   ```smiles
   CC(C)[C@@H]1CC[C@@H](C)C[C@@H]1Cl 1
   CC(C)[C@@H]1CC[C@@H](C)C[C@H]1Cl 2
   ```

   **Answer** 1 is neomenthyl chloride and 2 is menthyl chloride. In the stable conformation of 1 with the isopropyl and methyl groups both equatorial, chlorine is axial and both adjacent carbons have trans axial hydrogens, so E2 is fast and the main product is the Zaitsev-type menth-3-ene (the double bond at the carbon bearing the isopropyl group, about 75%), with some menth-2-ene. In 2 all three substituents are equatorial in the stable conformation, and the ring must flip to the high-energy conformation with all three substituents axial before Cl is axial; only C2 (on the side not bearing the isopropyl group) then has a trans axial hydrogen, the reaction is about 200 times slower, and only menth-2-ene is obtained.

5. Propose mechanisms for the following reactions: (a) 1-cyclobutylethanol heated in acid gives 1-methylcyclopentene; (b) 2,2-dimethylpropan-1-ol heated with HBr gives 2-bromo-2-methylbutane, whereas with $\ce{PBr3}$ it gives 1-bromo-2,2-dimethylpropane.

   **Answer** (a) Protonation of the hydroxy group and loss of water give a secondary carbocation (the 1-cyclobutylethyl cation); one C–C bond of the cyclobutane migrates to the cationic carbon, expanding the four-membered ring to a five-membered ring and giving a cyclopentyl cation (releasing ring strain), with the positive charge on the former ring carbon; a 1,2-hydride shift then gives the tertiary carbocation bearing the methyl group (or an adjacent H is lost directly), and loss of a proton gives the trisubstituted 1-methylcyclopentene. (b) In HBr, protonated neopentyl alcohol loses water with concomitant methyl migration (a primary carbocation is not formed, departure and migration being concerted) to give the tertiary carbocation, which is captured by $\ce{Br-}$; $\ce{PBr3}$ converts the hydroxy group into $\ce{-OPBr2}$, and $\ce{Br-}$ displaces it directly by SN2, with no carbocation and no rearrangement (the *tert*-butyl group at the $\beta$ position makes SN2 very slow, but it still proceeds).

6. Draw the mechanism of the following reaction: a tertiary alcohol with a decalin skeleton (steroid numbering; C8 bears a methyl group and the hydroxy group, and C10 bears the angular methyl group) loses the hydroxy group on treatment with $\ce{BF3}$ and, after a series of migrations, gives an alkene with the double bond at the ring fusion (C5=C10) and the angular methyl group moved to C9.

   ```smiles
   CC1(O)CCC2CCCCC2(C)C1>>CC1CCC2=C(CCCC2)C1C
   ```

   **Answer** $\ce{BF3}$ coordinates to the hydroxy group, and the C–O bond breaks to give the tertiary carbocation (C8). The axial hydrogen on the adjacent C9 transfers to C8 by a 1,2-hydride shift, and the positive charge moves to C9; the angular methyl group on C10 (originally trans-diaxial to C9–H) then migrates 1,2 to C9, and the positive charge moves to C10; finally the axial hydrogen on C5 is lost in an E1 fashion, forming the tetrasubstituted double bond between C5 and C10. In each migration the migrating group is antiperiplanar to the empty p orbital of the cationic carbon, a series of consecutive anti 1,2-shifts (the skeletal rearrangement of lanosterol in biosynthesis is also such a "chain of anti shifts").

7. What does anisole give on heating with excess HI? What does methyl *tert*-butyl ether give with one equivalent of HI? Why?

   **Answer** Anisole gives phenol and iodomethane: after protonation of the ether, $\ce{I-}$ attacks the methyl group by SN2; the phenyl–O bond has partial double-bond character and an aromatic carbon cannot undergo SN2 or SN1, so phenol is not converted further into iodobenzene. Methyl *tert*-butyl ether gives 2-iodo-2-methylpropane (*tert*-butyl iodide) and methanol: the protonated ether ionizes to the stable *tert*-butyl cation (SN1), which is captured by $\ce{I-}$, so the C–O bond is broken on the *tert*-butyl side and not on the methyl side preferred by SN2.

8. What are the main products of heating ethanol with concentrated sulfuric acid at $140\,^\circ\mathrm{C}$ and at $170\,^\circ\mathrm{C}$? Why does temperature change the product?

   **Answer** At $140\,^\circ\mathrm{C}$ the main product is diethyl ether (intermolecular SN2: ethanol attacks protonated ethanol), and at $170\,^\circ\mathrm{C}$ it is ethene (E2 of protonated ethanol). Elimination forms two molecules from one, so both $\Delta S$ and the entropy of activation are more favorable, and the enthalpy of activation is also higher; as the temperature rises the contribution of the $-T\Delta S$ term increases, and the rate of elimination grows faster than that of substitution.
