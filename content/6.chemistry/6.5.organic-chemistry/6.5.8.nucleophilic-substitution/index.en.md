---
title: Nucleophilic Substitution at Saturated Carbon
source_hash: 05e0a17a0b69
---

Nucleophilic substitution at a saturated carbon atom ($\mathrm{sp^3}$ carbon) was the first class of ionic reactions whose mechanisms were studied systematically, and it is the most frequently used "mechanistic template" of the whole course: an electron-rich reagent attacks an electron-poor carbon, and at the same moment, or soon afterward, a group departs with the bonding electron pair. In this chapter we take alkyl halides as substrates and, starting from rate laws, distinguish the SN2 and SN1 mechanisms. We discuss the structure, stability and rearrangements of carbocations, the stereochemistry of nucleophilic substitution, and the effects of the substrate, the leaving group, the nucleophile and the solvent on the rate and mechanism of the reaction, and we end with neighboring group participation.

The tools used in this chapter come from the preceding chapters and from other courses: bond polarity and the **inductive effect**, stabilization of carbocations by **hyperconjugation** ([6.5.2](/6.5.2#sec-2.3)); the pKa scale and the **Hammond postulate** ([6.5.3](/6.5.3#sec-3.10)); the description of chirality and configuration ([6.5.5](/6.5.5#sec-5.3.1)); rate laws and the determination of reaction order ([6.3.15](/6.3.15)); transition-state theory and the effect of solvents on reaction rates ([6.3.16](/6.3.16), [6.3.17](/6.3.17)). The next chapter, [6.5.9](/6.5.9), treats the **elimination reactions** that compete with substitution and extends the conclusions of this chapter to alcohols and ethers; [6.5.10](/6.5.10) deals with the reactions of alkyl halides with metals. Biological methylation (with *S*-adenosylmethionine), the alkylation of DNA and the mode of action of many drugs are all nucleophilic substitutions at saturated carbon, which is one of the foundations of chemical biology ([6.6](/6.6)).

## 8.1. Alkyl Halides and Nucleophilic Substitution

### 8.1.1. Structure and Nomenclature of Alkyl Halides

The product of replacing a hydrogen of a hydrocarbon by a halogen is a halogenoalkane or halide; an alkyl halide is one in which the halogen is bonded to an $\mathrm{sp^3}$ carbon. According to the number of carbon groups on the carbon atom that bears the halogen, alkyl halides are classified as primary ($\ce{RCH2X}$), secondary ($\ce{R2CHX}$) and tertiary ($\ce{R3CX}$). A halogen bonded to a double-bond carbon gives a vinyl halide, and one bonded to an aromatic ring gives an aryl halide; halides at the carbon next to a double bond or an aromatic ring are allylic and benzylic halides. This classification determines the reactivity discussed below.

In systematic nomenclature the halogens are named only as substituents (the prefixes fluoro-, chloro-, bromo- and iodo-); the main chain and numbering are chosen by the rules of [6.5.1](/6.5.1), and the prefixes are cited in alphabetical order:

```smiles
CCCC(C)(C)Br 2-bromo-2-methylpentane
CCC[C@H](Br)CC(C)(C)C (S)
ClCC1CCCCC1 chloromethylcyclohexane
```

The three compounds are 2-bromo-2-methylpentane, (*S*)-4-bromo-2,2-dimethylheptane (the locant set {2,2,4} is lower than {4,6,6} from the reverse numbering) and (chloromethyl)cyclohexane. Common names include chloroform ($\ce{CHCl3}$), carbon tetrachloride, iodoform ($\ce{CHI3}$), allyl bromide (3-bromoprop-1-ene) and benzyl chloride ((chloromethyl)benzene).

The **electronegativity** of the halogens exceeds that of carbon (Pauling values F 3.98, Cl 3.16, Br 2.96, I 2.66, C 2.55), so the $\ce{C-X}$ bond is polar and the carbon carries a partial positive charge. From F to I the bond length increases and the bond energy decreases, while the bond dipole moment changes little:

| | $\ce{CH3F}$ | $\ce{CH3Cl}$ | $\ce{CH3Br}$ | $\ce{CH3I}$ |
|---|---|---|---|---|
| C–X bond length / pm | 139 | 178 | 193 | 214 |
| $\ce{CH3-X}$ bond dissociation energy / $\mathrm{kJ\,mol^{-1}}$ | 460 | 350 | 294 | 239 |
| Dipole moment / $(10^{-30}\,\mathrm{C\,m})$ | 6.20 | 6.31 | 6.08 | 5.41 |
| $^1\mathrm{H}$ **chemical shift** $\delta$ of $\ce{CH3}$ | 4.26 | 3.05 | 2.68 | 2.16 |

(In debye the dipole moments are 1.86, 1.89, 1.82 and 1.62 D, with $1\,\mathrm{D} = 3.336\times10^{-30}\,\mathrm{C\,m}$.) The chemical shift of the methyl group moves downfield as the electronegativity of the halogen increases, direct evidence for deshielding by the inductive effect ([6.4.12](/6.4.12)); $\ce{CH4}$ is at 0.23, dichloromethane at 5.30 and chloroform at 7.26, so the effects of several halogens are roughly additive. The polarity of the C–X bond makes carbon an electron-poor center, and the decrease in bond energy with increasing size of the halogen makes the C–I bond the easiest to break. These two points determine the reactivity of alkyl halides: the carbon can be attacked by electron-rich reagents, and the halogen can leave with the electron pair.

### 8.1.2. Nucleophiles, Electrophiles and Leaving Groups

The four basic types of electron movement in [6.5.1](/6.5.1) all involve an electron-rich species attacking an electron-poor species. We now give these two kinds of species formal names.

**Definition 8.1.1 (Nucleophile and Electrophile)** A reagent that provides an electron pair in a reaction and forms a new covalent bond with an electron-poor atom (usually carbon) is called a **nucleophile** (often denoted Nu or $\ce{Nu-}$); a reagent that accepts an electron pair and forms a new bond with an electron-rich atom is called an **electrophile** (often denoted E or $\ce{E+}$).

Nucleophiles are **Lewis bases** and electrophiles are **Lewis acids** ([6.5.3](/6.5.3#sec-3.4)); the difference lies only in the reaction center, since a nucleophile attacks carbon whereas a base attacks a proton. The electron-rich sites of nucleophiles are of three kinds: lone pairs ($\ce{H2O}$, $\ce{NH3}$, $\ce{I-}$, $\ce{RS-}$), $\pi$ bonds (alkenes, aromatic rings, enols), and polar $\sigma$ bonds in which carbon carries a partial negative charge ($\ce{C-Mg}$, $\ce{C-Li}$, $\ce{H-Al}$, [6.5.10](/6.5.10#sec-10.3.1)). Electrophilic sites are also of three kinds: atoms that carry a positive charge or have an empty orbital (carbocations, $\ce{BF3}$), atoms that carry a partial positive charge because of the **inductive effect** (the carbon of $\ce{C-X}$ and $\ce{C=O}$), and the proton of $\ce{H-X}$.

**Definition 8.1.2 (Leaving Group)** The atom or group that departs from the substrate in a substitution or elimination reaction, taking with it the bonding electron pair to the carbon atom, is called a **leaving group** (often denoted X or LG).

**Definition 8.1.3 (Nucleophilic Substitution)** A reaction in which a nucleophile attacks the carbon atom bearing the leaving group in the substrate, forming a new C–Nu bond and expelling the leaving group, is called **nucleophilic substitution** (abbreviated SN):

$$
\ce{Nu- + R-X -> R-Nu + X-}.
$$
The molecule $\ce{R-X}$ that is attacked is called the substrate, the carbon bonded to the leaving group is the $\alpha$ carbon, and the carbon adjacent to it is the $\beta$ carbon.

The nucleophile may be negatively charged ($\ce{HO-}$, $\ce{CN-}$) or a neutral molecule ($\ce{H2O}$, $\ce{NH3}$); attack by a neutral nucleophile gives a positively charged product, which then loses a proton. The substrate may be neutral ($\ce{R-Br}$) or positively charged (a protonated alcohol $\ce{R-OH2+}$, a sulfonium ion $\ce{R-SR2+}$). With different nucleophiles the same alkyl halide can be converted into many classes of compounds, which is the most important use of nucleophilic substitution in synthesis:

![SN2 with a neutral nucleophile. The lone pair of ammonia attacks the α carbon of bromoethane and the C–Br bonding pair leaves with bromide, giving the ethylammonium ion; a second ammonia molecule removes a proton from nitrogen, giving ethylamine (which can be alkylated again, so the alkylation of ammonia gives mixtures)](./plots/nh3-alkylation.py)

| Nucleophile | Product | Class of product |
|---|---|---|
| $\ce{HO-}$, $\ce{H2O}$ | $\ce{R-OH}$ | Alcohol |
| $\ce{R'O-}$ | $\ce{R-OR'}$ | Ether (**Williamson ether synthesis**, [6.5.10](/6.5.10#sec-10.2.2)) |
| $\ce{R'COO-}$ | $\ce{R-OCOR'}$ | Ester |
| $\ce{HS-}$, $\ce{R'S-}$ | $\ce{R-SH}$, $\ce{R-SR'}$ | Thiol, sulfide ([6.5.26](/6.5.26#sec-26.8.2)) |
| $\ce{I-}$ | $\ce{R-I}$ | Alkyl iodide (Finkelstein reaction) |
| $\ce{CN-}$ | $\ce{R-CN}$ | Nitrile (the carbon chain is extended by one carbon, [6.5.20](/6.5.20#sec-20.4.2)) |
| $\ce{N3-}$ | $\ce{R-N3}$ | **Azide** (reduced to a primary amine, [6.5.23](/6.5.23#sec-23.5.3), [6.5.24](/6.5.24#sec-24.8.2)) |
| $\ce{NH3}$, $\ce{R'NH2}$ | $\ce{R-NH3+}$ etc. | Amine (polyalkylation, [6.5.23](/6.5.23#sec-23.5.1)) |
| $\ce{R'C#C-}$ | $\ce{R-C#CR'}$ | Alkyne ([6.5.11](/6.5.11#sec-11.12.3)) |
| **Enolate** | $\alpha$-Alkylated ketone or ester | [6.5.21](/6.5.21#sec-21.7), [6.5.22](/6.5.22#sec-22.8) |

## 8.2. Rate Laws and the Two Mechanisms

### 8.2.1. Two Kinds of Rate Law

The starting point for studying the mechanism of nucleophilic substitution is the **rate law** ([6.3.15](/6.3.15)). Two classical experiments give two different results.

1-Bromobutane and NaI in acetone give 1-iodobutane (the Finkelstein reaction). The initial-rate method gives:

| Experiment | $[\ce{BuBr}]_0 / (\mathrm{mol\,L^{-1}})$ | $[\ce{NaI}]_0 / (\mathrm{mol\,L^{-1}})$ | Initial rate $/ (\mathrm{mol\,L^{-1}\,s^{-1}})$ |
|---|---|---|---|
| 1 | 0.10 | 0.10 | $5.5\times10^{-5}$ |
| 2 | 0.20 | 0.10 | $1.1\times10^{-4}$ |
| 3 | 0.10 | 0.20 | $1.1\times10^{-4}$ |
| 4 | 0.20 | 0.20 | $2.2\times10^{-4}$ |

The rate is proportional to the concentrations of both reactants, $v = k[\ce{BuBr}][\ce{I-}]$ with $k = 5.5\times10^{-3}\,\mathrm{L\,mol^{-1}\,s^{-1}}$: this is a **second-order reaction**.

![The Finkelstein reaction (SN2). Iodide attacks C1 of 1-bromobutane from the side opposite to bromine, and the C–Br bonding pair leaves with bromide; NaI dissolves in acetone but NaBr precipitates, which drives the equilibrium toward 1-iodobutane](./plots/finkelstein.py)

In the hydrolysis of 2-bromo-2-methylpropane (*tert*-butyl bromide) in aqueous ethanol, a plot of $\ln[\ce{t-BuBr}]$ against time $t$ is a straight line, and neither the addition of $\ce{HO-}$ nor a change in the amount of water changes the rate: $v = k[\ce{t-BuBr}]$. This is a **first-order reaction**, and the rate is independent of the nucleophile.

Two rate laws for one class of reaction imply two mechanisms. In the nomenclature of Hughes and Ingold (1930s) they are called SN2 and SN1, the number being the **molecularity** of the **rate-determining step**.

### 8.2.2. The SN2 Mechanism

**Definition 8.2.1 (SN2 Reaction)** A nucleophilic substitution in which attack of the nucleophile on the $\alpha$ carbon and departure of the leaving group occur simultaneously in a single step is called an **SN2 reaction** (bimolecular nucleophilic substitution). It is an **elementary reaction** with the rate law

$$
v = k_2[\ce{RX}][\ce{Nu-}].
$$

![The SN2 reaction: hydroxide attacks (R)-2-bromobutane from the side opposite to bromine, through a trigonal bipyramidal transition state in which O, C and Br are collinear and the other three groups are coplanar, to give (S)-butan-2-ol with inverted configuration](./plots/sn2-mechanism.py)

In orbital terms, the lone pair of the nucleophile (the HOMO) must enter the LUMO of the substrate, the $\sigma^*$ **antibonding orbital** of the C–X bond. The large lobe of the $\sigma^*$ orbital on the carbon side points in the direction opposite to the C–X bond, and there is a node between C and X: attack from the back gives the maximum in-phase overlap, whereas attack from the front interacts with both lobes and the contributions cancel. Filling the $\sigma^*$ orbital with electrons weakens the C–X bond until it breaks, so bond making and bond breaking occur at the same time.

In the transition state the carbon is bonded to five groups: Nu, C and X lie on a straight line, each bearing a partial negative charge; the other three groups lie with the carbon in a plane perpendicular to this line, and the carbon is approximately $\mathrm{sp^2}$ hybridized and uses one p orbital to bond partially to both Nu and X. As the reaction goes from the transition state toward the products, the three groups flip to the other side like an umbrella blown inside out. The energy diagram has a single transition state and no intermediate ([6.5.3](/6.5.3#sec-3.6.1)).

The three characteristics of the SN2 reaction can all be deduced from this picture: (1) second-order kinetics; (2) inversion of configuration at a stereogenic carbon (Section 8.4); (3) great sensitivity to steric hindrance at the $\alpha$ and $\beta$ carbons (Section 8.5).

### 8.2.3. The SN1 Mechanism

**Definition 8.2.2 (SN1 Reaction)** A two-step nucleophilic substitution in which the substrate first undergoes heterolysis to a carbocation and a leaving group (the slow step), and the carbocation then combines with the nucleophile (the fast step), is called an **SN1 reaction** (unimolecular nucleophilic substitution). The rate-determining step involves only the substrate, and the rate law is

$$
v = k_1[\ce{RX}].
$$

The hydrolysis of *tert*-butyl bromide is a typical SN1 reaction; its stepwise mechanism is shown in the figure of [6.5.3](/6.5.3#sec-3.11.1). The C–Br bond undergoes **heterolysis** to give the *tert*-butyl cation and $\ce{Br-}$, the lone pair of water attacks the cationic carbon to give a protonated alcohol (an oxonium ion), and the oxonium ion transfers a proton to another water molecule to give *tert*-butyl alcohol and $\ce{H3O+}$. Recombination of the carbocation with $\ce{Br-}$ is just the reverse of the first step and gives no product.

The energy diagram of an SN1 reaction has two transition states with the high-energy carbocation intermediate between them. The first step is endothermic with a high barrier and is rate-determining; by the **Hammond postulate** the first transition state resembles the carbocation, so factors that stabilize the carbocation also stabilize the first transition state and speed up the reaction (Section 8.5). The second step has almost no barrier, and combination of the carbocation with the nucleophile is often close to diffusion control. With the **steady-state approximation** ([6.3.15](/6.3.15#sec-15.6.1)) the two steps can be written as

$$
v = \frac{k_1k_2[\ce{RX}][\ce{Nu}]}{k_{-1}[\ce{X-}] + k_2[\ce{Nu}]},
$$
where $k_{-1}$ is the rate constant for recombination of the carbocation with $\ce{X-}$. When $k_2[\ce{Nu}] \gg k_{-1}[\ce{X-}]$ (the solvent itself is the nucleophile, at a concentration of about $10$–$55\,\mathrm{mol\,L^{-1}}$), this reduces to $v = k_1[\ce{RX}]$. The "common-ion effect", the decrease in rate on adding $\ce{X-}$, is evidence for reversible ionization in the SN1 mechanism.

An SN1 reaction in which the nucleophile is the solvent itself is called solvolysis.

**Definition 8.2.3 (Solvolysis)** A nucleophilic substitution in which a solvent molecule (water, an alcohol, acetic acid, formic acid, etc.) acts as the nucleophile is called **solvolysis**; it is called hydrolysis when the solvent is water and alcoholysis when it is an alcohol.

### 8.2.4. Between the Two Mechanisms

SN1 and SN2 are two extremes. The hydrolysis of actual alkyl halides often has both a first-order and a second-order component. In $80\%$ ethanol–water, the first-order solvolysis rate constants $k_1$ of alkyl bromides and the second-order rate constants $k_2$ after addition of $\ce{HO-}$ are:

| Substrate | $k_1 / (10^{-5}\,\mathrm{s^{-1}})$ | $k_2 / (10^{-5}\,\mathrm{L\,mol^{-1}\,s^{-1}})$ |
|---|---|---|
| $\ce{CH3Br}$ | 0.35 | 2140 |
| $\ce{CH3CH2Br}$ | 0.14 | 170 |
| $\ce{(CH3)2CHBr}$ | 0.24 | 4.75 |
| $\ce{(CH3)3CBr}$ | 1010 | — |

From methyl to *tert*-butyl, the second-order (SN2) component decreases rapidly and the first-order (SN1) component suddenly increases at the tertiary carbon; both components are small for secondary halides, which are the most likely to show a mixture of mechanisms. These two columns of data are the quantitative source of the conclusions of Section 8.5.

## 8.3. Carbocations

### 8.3.1. Structure and Nomenclature

**Definition 8.3.1 (Carbocation)** A carbon atom that carries a positive charge, has only six valence electrons in its outer shell and is bonded to three atoms is called a **carbocation** (formerly "carbonium ion"). Ions containing such a carbon are also called carbocations.

The central carbon of the simplest carbocations is $\mathrm{sp^2}$ hybridized: the three $\mathrm{sp^2}$ orbitals form $\sigma$ bonds to three groups at bond angles of about $120^\circ$, giving a planar structure, and the unhybridized p orbital is perpendicular to the plane and empty. According to the number of carbon groups on the central carbon, carbocations are classified as methyl, primary, secondary and tertiary; they are named by adding "cation" to the name of the group (the *tert*-butyl cation $\ce{(CH3)3C+}$, IUPAC name 2-methylpropan-2-ylium).

In solution carbocations are usually intermediates with extremely short lifetimes. In the 1960s Olah used "superacids" (mixtures of $\ce{SbF5}$ with $\ce{FSO3H}$ or HF) at low temperature ($-70\,^\circ\mathrm{C}$, solvent $\ce{SO2ClF}$) to ionize alkyl halides or alkenes and obtained for the first time stable carbocation salts that could be observed for long periods and studied by NMR (Nobel Prize in Chemistry, 1994):

```smiles
C=C(C)C.F[Sb-](F)(F)(F)(F)F>>C[C+](C)C.F[Sb-](F)(F)(F)(F)F
```

![Olah's preparation of a persistent carbocation. In superacid the C=C pi electrons of isobutene take a proton, which bonds to the CH₂ end, so that the positive charge sits on the tertiary carbon; the extremely weakly nucleophilic SbF₆⁻ does not capture the tert-butyl cation](./plots/olah-protonation.py)

The $^{13}\mathrm{C}$ chemical shift of the cationic carbon of the *tert*-butyl cation is about $\delta$ 335, some 200 ppm downfield of an ordinary $\mathrm{sp^2}$ carbon ($\delta$ 120–150), and the $^1\mathrm{H}$ chemical shift of the methyl hydrogens is about $\delta$ 4.3 (about 0.9 in ordinary *tert*-butyl groups): the positive charge strongly deshields the central carbon and is also dispersed onto the adjacent C–H bonds by **hyperconjugation**. The cationic carbon of the isopropyl cation is at about $\delta$ 320.

### 8.3.2. Stability

The relative stabilities of carbocations can be compared by their gas-phase hydride affinities ($-\Delta H$ for $\ce{R+ + H- -> RH}$): the smaller the hydride affinity, the more stable the carbocation (data and discussion in [6.5.2](/6.5.2#sec-2.6)):

| Carbocation | $\ce{CH3+}$ | $\ce{CH3CH2+}$ | $\ce{(CH3)2CH+}$ | $\ce{(CH3)3C+}$ | Allyl | Benzyl |
|---|---|---|---|---|---|---|
| Hydride affinity / $\mathrm{kJ\,mol^{-1}}$ | 1305 | 1142 | 1029 | 967 | 1071 | 979 |

The order of stability is tertiary > secondary > primary > methyl; in the gas phase the allyl cation is slightly less stable than the isopropyl cation, and the benzyl cation is close to the *tert*-butyl cation; in solution both form readily. Alkyl groups stabilize carbocations mainly by **hyperconjugation**: $\alpha$ C–H (or C–C) $\sigma$ bonds parallel to the empty p orbital delocalize electrons partly into it ([6.5.2](/6.5.2#sec-2.6)); the *tert*-butyl cation has 9 such C–H bonds and the ethyl cation only 3. The greater **polarizability** of alkyl groups also contributes; the "electron-donating inductive effect" of alkyl groups often quoted is very weak and is not the main reason ([6.5.2](/6.5.2#sec-2.3)). (Hydride affinities are gas-phase data; in solution the differences between carbocations are reduced by solvation, but the order is unchanged.)

Other structural factors that stabilize carbocations are:

- p–$\pi$ conjugation: in allyl and benzyl cations the positive charge is delocalized over two (or more) carbons by the **conjugation effect**, and equivalent or similar **resonance structures** can be written ([6.5.1](/6.5.1#sec-1.6)); the triphenylmethyl cation can persist in solution for a long time.
- Lone pairs on heteroatoms: $\ce{CH3O-CH2+ <-> CH3O+=CH2}$; the lone pair of oxygen is conjugated with the empty p orbital (in the oxonium form every atom has an octet), and an $\alpha$-alkoxy carbocation is even more stable than a tertiary carbocation. This is the key intermediate in the hydrolysis of **acetals** ([6.5.16](/6.5.16#sec-16.5.2)) and the cleavage of glycosidic bonds ([6.5.32](/6.5.32)).
- **Aromaticity**: the cycloheptatrienyl cation (tropylium ion, $\ce{C7H7+}$) has 6 $\pi$ electrons and is aromatic; tropylium bromide is a salt that dissolves in water ([6.5.13](/6.5.13#sec-13.5.1)).
- The cyclopropyl group: the cyclopropylmethyl cation is unusually stable, because the electrons of the **bent bonds** of cyclopropane ([6.5.4](/6.5.4#sec-4.4.1)) overlap with the empty p orbital (the "bisected conformation").

![Delocalization that stabilizes carbocations. Top: in the methoxymethyl cation a lone pair of oxygen forms a C=O pi bond, giving an oxocarbenium ion in which every atom has an octet. Bottom: in the allyl cation the C=C pi electrons move toward the empty p orbital, so the positive charge is shared by the two terminal carbons](./plots/cation-resonance.py)

Conversely, the vinyl cation (with the positive charge on an $\mathrm{sp}$ carbon) and the phenyl cation (whose empty orbital is an $\mathrm{sp^2}$ orbital in the plane of the ring and cannot conjugate with the $\pi$ system) are both very unstable, which is why vinyl halides and aryl halides do not undergo SN1 reactions (Section 8.5.3).

### 8.3.3. Rearrangements of Carbocations

A hydrogen or an alkyl group on a carbon adjacent to a carbocation can migrate with its bonding electron pair to the cationic carbon, moving the positive charge to the carbon that was originally adjacent. The driving force of such 1,2-shifts is formation of a more stable carbocation (secondary → tertiary; a primary carbocation is not formed at all, the shift occurring concertedly with the departure of the leaving group). The barriers are often only a few $\mathrm{kJ\,mol^{-1}}$, so the shifts are faster than capture of the carbocation by the solvent.

![SN1 reaction of 2-bromo-3-methylbutane in water: ionization gives a secondary carbocation, a hydrogen on the adjacent carbon migrates with its electron pair (1,2-hydride shift) to give a tertiary carbocation, and capture by water gives the rearranged product 2-methylbutan-2-ol](./plots/hydride-shift.py)

The products of SN1 and **E1 reactions** ([6.5.9](/6.5.9#sec-9.3)) are therefore often rearranged products with a changed skeleton. When a hydrogen migrates, the shift is called a 1,2-hydride shift, and when an alkyl group migrates a 1,2-alkyl shift (Wagner–Meerwein rearrangement); rearrangement can also expand a ring (the cyclobutylmethyl cation becomes the cyclopentyl cation, releasing **ring strain**, [6.5.9](/6.5.9#sec-9.8.1)). A systematic discussion of carbocation rearrangements is found in [6.5.30](/6.5.30).

For example, 1-bromo-2,2-dimethylpropane (neopentyl bromide) solvolyzes slowly in ethanol and gives almost only rearranged products:

```smiles
CC(C)(C)CBr>>CCC(C)(C)OCC.CC=C(C)C
```

A primary carbocation is extremely unstable, and departure of the bromide occurs concertedly with migration of a methyl group, giving a tertiary carbocation directly, which is captured by ethanol (2-ethoxy-2-methylbutane) or loses a proton (2-methylbut-2-ene).

![Solvolysis of neopentyl bromide. A primary carbocation is too unstable to form; instead the methyl group anti to the leaving group migrates with its bonding pair to C1 as bromide leaves, giving the tertiary 2-methyl-2-butyl cation directly, which is captured by ethanol (2-ethoxy-2-methylbutane after loss of a proton) or loses a proton (2-methyl-2-butene)](./plots/neopentyl-rearrangement.py)

## 8.4. Stereochemistry of Nucleophilic Substitution

### 8.4.1. SN2: Inversion of Configuration

With a chiral substrate the consequence of back-side attack in the SN2 reaction can be seen directly. (*R*)-2-Bromobutane reacts with $\ce{NaOH}$ to give (*S*)-butan-2-ol, with complete inversion of **configuration** (see the figure in Section 8.2.2).

**Definition 8.4.1 (Walden Inversion)** The phenomenon in which, in an SN2 reaction, the nucleophile attacks from the side opposite to the leaving group, so that the three remaining groups at the stereogenic center flip to the other side in space and the configuration is inverted, is called the **Walden inversion**.

In 1896 Walden converted (−)-malic acid into (+)-malic acid by a series of substitution reactions and so discovered for the first time that substitution can change configuration. In 1935 Hughes and Ingold showed, with the exchange of (*R*)-2-iodooctane with radioactive $\ce{^{128}I-}$, that the rate of iodide exchange is exactly half the rate of **racemization**: each exchange inverts the configuration of one molecule, which is quantitative evidence for back-side attack in the SN2 reaction.

The SN2 reaction is **stereospecific** ([6.5.5](/6.5.5#sec-5.8.1)): one enantiomer gives only the product of the other configuration. Note that "inversion of configuration" refers to inversion of the spatial arrangement, and whether the R/S label changes depends on the rank of the new group in the CIP order (Question 3).

In cyclic substrates the requirement of back-side attack directly determines the relative configuration of the product: *cis*-1-bromo-4-methylcyclohexane reacts with $\ce{CN-}$ to give *trans*-4-methylcyclohexanecarbonitrile.

```smiles
C[C@H]1CC[C@@H](Br)CC1.[C-]#N>>C[C@H]1CC[C@H](C#N)CC1 trans
```

### 8.4.2. SN1: Racemization and Ion Pairs

A planar carbocation can be attacked by a nucleophile from either face. If the carbocation is completely "free", attack from the two faces is equally probable and the product is a **racemate**.

![SN1 reaction of (R)-3-bromo-3-methylhexane in water: ionization gives a planar tertiary carbocation; attack by water from the back (a) gives the (S)-alcohol with inverted configuration, and attack from the front (b) gives the (R)-alcohol with retained configuration; in practice somewhat more of the inverted product is formed](./plots/sn1-stereo.py)

In experiments SN1 reactions are usually accompanied by partial **racemization**, and the inverted product always slightly exceeds the retained one (typical inversion : retention ratios range from $55:45$ to $80:20$); "complete racemization in SN1" is only an idealization. Winstein explained this by the theory of ion pairs:

**Definition 8.4.2 (Ion Pair)** When a substrate ionizes, the carbocation and the departing anion do not separate at once but pass successively through a contact ion pair, in which the two are in direct contact, and a solvent-separated ion pair, with solvent molecules between them, and only then become free ions each surrounded by solvent:

$$
\ce{R-X <=> [R+ X-] <=> [R+ \Vert X-] <=> R+ + X-}.
$$
These combinations of cations and anions that have not yet completely separated are called **ion pairs**.

In a contact ion pair, $\ce{X-}$ blocks the face of the carbocation to which it was originally bonded, so the nucleophile can attack only from the back, giving the inverted product (this is already close to SN2); in a solvent-separated ion pair the shielding is weaker, but inversion still exceeds retention; only the free carbocation gives equal amounts of the two configurations. The overall result is inversion > retention, and the less stable the carbocation (the shorter its lifetime) and the more nucleophilic the solvent, the more inversion is observed. The existence of ion pairs also explains why an optically active substrate partly racemizes in solvolysis before the product is formed (return within the ion pair).

## 8.5. Effect of Substrate Structure

The rate of a reaction is determined by the energy of the transition state of the rate-determining step: for SN2 what matters is how crowded the five-coordinate transition state is, and for SN1 it is the stability of the carbocation (and of the first transition state, which resembles it).

### 8.5.1. Effect on SN2: Steric Hindrance

Relative rates of the SN2 reaction of alkyl bromides with $\ce{I-}$ in acetone ($25\,^\circ\mathrm{C}$):

| Substitution at the $\alpha$ carbon | $\ce{CH3Br}$ | $\ce{CH3CH2Br}$ | $\ce{(CH3)2CHBr}$ | $\ce{(CH3)3CBr}$ |
|---|---|---|---|---|
| Relative rate | 145 | 1 | 0.008 | Practically no reaction |

| Substitution at the $\beta$ carbon | $\ce{CH3CH2Br}$ | $\ce{CH3CH2CH2Br}$ | $\ce{(CH3)2CHCH2Br}$ | $\ce{(CH3)3CCH2Br}$ |
|---|---|---|---|---|
| Relative rate | 1 | 0.8 | 0.04 | 0.00001 |

The order of SN2 reactivity is methyl > primary > secondary ≫ tertiary. In the transition state the $\alpha$ carbon is bonded to five groups, and the more and the larger the substituents, the more crowded it is; a nucleophile approaching from the back also meets the groups on the $\beta$ carbon. Although neopentyl bromide is a primary alkyl halide, its three $\beta$ methyl groups block the back side completely, and its SN2 reaction is $10^5$ times slower than that of bromoethane. Electronic effects are secondary here, since the change in charge on the $\alpha$ carbon in the transition state is small.

### 8.5.2. Effect on SN1: Stability of the Carbocation

Relative rates of solvolysis of alkyl bromides in water (SN1 conditions):

| Substrate | $\ce{CH3Br}$ | $\ce{CH3CH2Br}$ | $\ce{(CH3)2CHBr}$ | $\ce{(CH3)3CBr}$ |
|---|---|---|---|---|
| Relative rate | < 1 | 1 | 12 | $1.2\times10^{6}$ |

The order of SN1 reactivity is tertiary > secondary > primary > methyl, in agreement with the order of carbocation stability. In addition, the three groups on the $\alpha$ carbon of a tertiary halide are crowded, with bond angles of about $109.5^\circ$; on ionization to the planar carbocation the angles open to $120^\circ$ and **steric strain** is released ("steric assistance"), which further accelerates the ionization of highly hindered tertiary halides.

The two mechanisms make opposite demands on the substrate: methyl and primary halides react almost exclusively by SN2, tertiary halides almost exclusively by SN1 (or E1 and E2, [6.5.9](/6.5.9#sec-9.6)), and secondary halides may follow either, the mechanism being decided by the nucleophile and the solvent.

### 8.5.3. Special Substrates

- Allylic and benzylic halides: both SN1 and SN2 are fast. SN1 gives a resonance-stabilized carbocation; in the SN2 transition state the p orbital of the $\alpha$ carbon is conjugated with the adjacent $\pi$ system, and the transition state is also stabilized. Under SN2 conditions, for example, allyl chloride reacts about 80 times faster than propyl chloride and benzyl chloride about 200 times faster. The SN1 products of allylic substrates are often two regioisomers (allylic rearrangement, related to **1,4-addition** in [6.5.11](/6.5.11#sec-11.6.1)).
- Vinyl and aryl halides: neither SN1 nor SN2 occurs. Vinyl and phenyl cations are very unstable; the C–X bond has partial double-bond character because the lone pairs of the halogen are conjugated with the $\pi$ bond, so the bond is shorter and stronger; and the direction of back-side attack is blocked by the $\pi$ electron cloud in the molecular plane and by the ring itself. Nucleophilic substitution of aryl halides goes by addition–elimination (**SNAr**, [6.5.14](/6.5.14#sec-14.11)) or by the **benzyne** mechanism ([6.5.15](/6.5.15#sec-15.1)).
- Bridgehead halides: bridgehead halides such as 1-bromobicyclo[2.2.1]heptane (1-bromonorbornane) are extremely slow by both mechanisms: the back side is completely blocked by the cage skeleton, so SN2 is impossible, and the bridgehead carbon cannot become planar, so the empty orbital of the carbocation formed cannot become a p orbital and SN1 is extremely slow too (the same root as Bredt's rule, [6.5.9](/6.5.9#sec-9.1)). The solvolysis of 1-bromobicyclo[2.2.1]heptane in 80% ethanol is about $10^{13}$ times slower than that of *tert*-butyl bromide. 1-Bromoadamantane, with its larger and more flexible cage, can undergo SN1, because the adamantyl cation can flatten to a limited extent.
- $\alpha$-Halo carbonyl compounds: the SN2 reaction of $\ce{ClCH2COCH3}$ with $\ce{I-}$ is tens of thousands of times faster than that of 1-chloropropane (the transition state is conjugated with the $\pi^*$ orbital of $\ce{C=O}$), but SN1 hardly occurs (the positive charge would be next to the electron-withdrawing carbonyl group).

![SN1 of an allylic halide with allylic rearrangement. 1-Chloro-2-butene ionizes to the 1-methylallyl cation, whose positive charge is shared by C1 and C3 (resonance); water attacks either end, giving 2-buten-1-ol and 3-buten-2-ol after loss of a proton](./plots/allylic-sn1.py)

## 8.6. Leaving Groups

The rate-determining step of both mechanisms includes breaking of the C–X bond, so the more easily the leaving group leaves, the faster both reactions are. The leaving ability of the halides is

$$
\ce{I-} > \ce{Br-} > \ce{Cl-} \gg \ce{F-}.
$$

It parallels the acidity of the conjugate acids: a good leaving group is the conjugate base of a strong acid, that is, a weak base. $\mathrm{p}K_{\mathrm{a}}$ (water, [6.5.3](/6.5.3#sec-3.1.4)): HI about $-10$, HBr about $-9$, HCl about $-7$, HF 3.20. A weak base can accommodate the negative charge stably on departure; the decrease of C–X bond energy (table in Section 8.1.1) and the increase in the **polarizability** of X also contribute. This relation between leaving ability and the $\mathrm{p}K_{\mathrm{a}}$ of the conjugate acid is one of the most useful empirical rules of the whole course:

| Leaving ability | Leaving group ($\mathrm{p}K_{\mathrm{a}}$ of conjugate acid, water) |
|---|---|
| Excellent | $\ce{CF3SO3-}$ (triflate, TfO⁻; about $-14$), $\ce{I-}$, $\ce{Br-}$, $\ce{CH3C6H4SO3-}$ (tosylate, TsO⁻, about $-2.8$), $\ce{CH3SO3-}$ (mesylate, MsO⁻, $-1.9$), $\ce{N2}$ (**diazonium salts**, [6.5.24](/6.5.24#sec-24.4)) |
| Good | $\ce{Cl-}$, $\ce{H2O}$ (leaving from a protonated alcohol; $\ce{H3O+}$ is 0), $\ce{R2O}$ (protonated ether), $\ce{R2S}$ (sulfonium ion) |
| Poor | $\ce{F-}$ (3.20), $\ce{RCOO-}$ (about 4.8), $\ce{R3N}$ (**quaternary ammonium salts**, $\ce{R3NH+}$ about 10) |
| Generally do not leave | $\ce{HO-}$ (14.00), $\ce{RO-}$ (15.5–18), $\ce{H2N-}$ (about 38), $\ce{H-}$, $\ce{R-}$ |

Alcohols and ethers therefore do not undergo nucleophilic substitution as such: $\ce{HO-}$ and $\ce{RO-}$ are strong bases and very poor leaving groups. For the hydroxy group to leave, it must first be converted into a good leaving group, and there are two common ways of doing so:

1. Protonation in strong acid: $\ce{R-OH + H+ <=> R-OH2+}$, with $\ce{H2O}$ as the leaving group; the Lewis acid $\ce{ZnCl2}$ acts in the same way by coordination to oxygen (Lucas reagent, [6.5.9](/6.5.9#sec-9.7.1)). This applies only to substrates that tolerate strong acid and to nucleophiles that are themselves weak bases ($\ce{Br-}$, $\ce{I-}$).
2. Conversion to a sulfonate ester: an alcohol reacts with 4-methylbenzenesulfonyl chloride (TsCl) or methanesulfonyl chloride (MsCl) in pyridine to give the tosylate $\ce{ROTs}$ or mesylate $\ce{ROMs}$. The negative charge of the sulfonate is delocalized over three oxygens, and its leaving ability is comparable to or better than that of $\ce{Br-}$. This step breaks only the O–H bond and leaves the C–O bond alone, so the configuration of a chiral alcohol is retained; the subsequent SN2 inverts the configuration, and the whole sequence is a clean inversion.

```smiles
C[C@@H](O)CCCCCC.Cc1ccc(cc1)S(=O)(=O)Cl>>C[C@@H](OS(=O)(=O)c1ccc(C)cc1)CCCCCC (R)-ROTs
C[C@@H](OS(=O)(=O)c1ccc(C)cc1)CCCCCC.[Br-]>>C[C@H](Br)CCCCCC (S)
```

![Converting an alcohol into a tosylate retains its configuration. Top: the oxygen lone pair of (R)-2-octanol attacks sulfur of tosyl chloride and chloride leaves; pyridine removes the proton from the oxonium ion. Only the O–H bond is broken; the C–O bond is untouched. Bottom: bromide attacks the stereocenter from the back (SN2) and the tosylate anion leaves with inversion, giving (S)-2-bromooctane. Ar = 4-methylphenyl, R = n-hexyl](./plots/tosylate-formation.py)

The differences in leaving ability allow "exchange first, substitute afterwards": a primary alkyl chloride hydrolyzes very slowly in water, but after a little $\ce{I-}$ is added, $\ce{I-}$ first displaces $\ce{Cl-}$ by SN2 to give the alkyl iodide, which hydrolyzes much faster and releases $\ce{I-}$ again; the iodide acts as a nucleophilic catalyst. Dimethyl sulfate $\ce{(CH3O)2SO2}$ and iodomethane are common methylating reagents in the laboratory (both are highly toxic and carcinogenic, and must be used in a fume hood).

## 8.7. Nucleophiles

### 8.7.1. Nucleophilicity

Only the rate-determining step of SN2 includes the nucleophile, so the strength of the nucleophile affects only the rate of SN2 and not that of SN1 (it affects only the product distribution of the second step of SN1).

**Definition 8.7.1 (Nucleophilicity)** The ability of a nucleophile to donate an electron pair to an electron-poor carbon atom and form a new bond is called **nucleophilicity**; it is measured by the rate constant of the reaction with the same substrate under the same conditions. Nucleophilicity is a kinetic property; basicity is the thermodynamic property of binding a proton, measured by the $\mathrm{p}K_{\mathrm{a}}$ of the conjugate acid.

Nucleophilicity often parallels basicity but not always. The rules are:

1. For the same attacking atom, an anion is stronger than a neutral species: $\ce{HO-} > \ce{H2O}$, $\ce{RO-} > \ce{ROH}$, $\ce{H2N-} > \ce{NH3}$, $\ce{RS-} > \ce{RSH}$.
2. For the same attacking atom, the stronger the base, the stronger the nucleophile: $\ce{RO-} > \ce{HO-} > \ce{ArO-} > \ce{RCOO-}$, the reverse of the acidity order of the conjugate acids, $\ce{ROH} < \ce{H2O} < \ce{ArOH} < \ce{RCOOH}$ (the *tert*-butoxide ion is an exception because of steric hindrance, see rule 5).
3. Within a period, nucleophilicity decreases from left to right together with basicity: $\ce{H2N-} > \ce{HO-} > \ce{F-}$, $\ce{NH3} > \ce{H2O}$.
4. Within a group (in protic solvents), nucleophilicity increases from top to bottom, the reverse of the order of basicity: $\ce{I-} > \ce{Br-} > \ce{Cl-} > \ce{F-}$, $\ce{RS-} > \ce{RO-}$, $\ce{R3P} > \ce{R3N}$. There are two reasons. The valence electrons of large atoms are far from the nucleus and the **polarizability** is high, so the electron cloud deforms easily to overlap with the $\sigma^*$ orbital; this is the "softness" of the **HSAB principle** (a saturated carbon is a soft electrophilic center, [6.5.3](/6.5.3#sec-3.4)). Small anions are strongly solvated by **hydrogen bonds** in protic solvents and must shed part of their solvent molecules before they can attack (Section 8.8). In aprotic solvents and in the gas phase the order of the halides becomes $\ce{F-} > \ce{Cl-} > \ce{Br-} > \ce{I-}$.
5. Bulky reagents are weak nucleophiles: potassium *tert*-butoxide, $t$-BuOK, is a strong base and a poor nucleophile; **lithium diisopropylamide** (LDA), lithium hexamethyldisilazide (LiHMDS), DBU and DBN are commonly used "non-nucleophilic strong bases" ([6.5.9](/6.5.9#sec-9.6.1)). Abstracting a peripheral proton does not require approaching a crowded carbon, so steric hindrance affects basicity far less than nucleophilicity.

In protic solvents, the order of nucleophilicity of common nucleophiles toward a saturated carbon is approximately:

$$
\ce{RS-} \approx \ce{ArS-} > \ce{CN-} > \ce{I-} > \ce{NH3}\,(\ce{RNH2}) > \ce{RO-} \approx \ce{HO-} > \ce{Br-} > \ce{PhO-} > \ce{Cl-} \gg \ce{H2O} > \ce{F-}.
$$

### 8.7.2. The Swain–Scott Equation

Swain and Scott (1953) made nucleophilicity quantitative. Taking the reaction of $\ce{CH3Br}$ in water ($25\,^\circ\mathrm{C}$) as the standard,

$$
\lg\frac{k}{k_0} = sn, \tag{8.1}
$$
where $k$ and $k_0$ are the rate constants of the reaction with the nucleophile and with water, respectively, $n$ is the nucleophilicity constant of the nucleophile (0 for water), and $s$ is the sensitivity of the substrate to nucleophilicity (1 for $\ce{CH3Br}$). It is another example of a **linear free-energy relationship**, besides the **Hammett equation** of [6.5.3](/6.5.3#sec-3.5):

| Nu | $\ce{HS-}$ | $\ce{CN-}$ | $\ce{I-}$ | $\ce{C6H5NH2}$ | $\ce{HO-}$ | $\ce{N3-}$ | $\ce{Br-}$ | Pyridine | $\ce{C6H5O-}$ | $\ce{Cl-}$ | $\ce{CH3COO-}$ | $\ce{F-}$ | $\ce{NO3-}$ | $\ce{H2O}$ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| $n$ | 5.1 | 5.1 | 5.0 | 4.5 | 4.2 | 4.0 | 3.9 | 3.6 | 3.5 | 3.0 | 2.7 | 2.0 | 1.0 | 0 |

Each increase of 1 in $n$ increases the rate tenfold: the reaction of $\ce{I-}$ with $\ce{CH3Br}$ is $10^5$ times faster than that of water. The order of nucleophilicity depends on the substrate: toward a harder electrophilic center such as a carbonyl carbon, the relative nucleophilicity of $\ce{HO-}$ and $\ce{RO-}$ is markedly higher than that of $\ce{I-}$ and $\ce{RS-}$ ([6.5.19](/6.5.19#sec-19.2.2)).

### 8.7.3. Ambident Nucleophiles and Counterions

Reagents with two nucleophilic sites are called **ambident nucleophiles**. $\ce{CN-}$ generally reacts at C with alkyl halides to give nitriles, but with $\ce{AgCN}$ ($\ce{Ag+}$ pulls off the halide, favoring SN1) it reacts mainly at N to give an **isocyanide**; the nitrite ion $\ce{NO2-}$ reacts at N to give a nitroalkane and at O to give an alkyl nitrite; enolates react at C and at O ([6.5.21](/6.5.21#sec-21.4.1)). Hard, charge-concentrated sites (O, the N end) tend to combine with electrophilic centers carrying more positive charge (SN1 type), and soft sites (C, S) tend to react by SN2, which can be understood qualitatively by the HSAB principle.

![Cyanide as an ambident nucleophile. Top: with NaCN in a polar aprotic solvent the carbon lone pair attacks bromoethane (SN2), giving propanenitrile. Bottom: in silver cyanide the carbon is bonded to silver, Ag⁺ also pulls bromide away (AgBr precipitates), and the nitrogen lone pair attacks, giving ethyl isocyanide](./plots/ambident-cyanide.py)

An anionic nucleophile always has a counterion. When an acetate $\ce{CH3COOM}$ is heated under reflux with an alkyl bromide in acetic acid, the rate increases as $\ce{M+}$ goes from $\ce{Li+}$, $\ce{Na+}$ and $\ce{K+}$ to $\ce{Cs+}$ and $\ce{R4N+}$: small cations form tight ion pairs with $\ce{CH3COO-}$ and lower the nucleophilicity of the anion, whereas large cations bind the anion weakly and leave it more "free". Crown ethers and cryptands that encapsulate $\ce{K+}$, and quaternary ammonium salts that carry anions into the organic phase (**phase-transfer catalysis**, [6.5.23](/6.5.23#sec-23.7.2)), all exploit this to raise nucleophilicity.

## 8.8. Solvent Effects

### 8.8.1. Classification of Solvents

Solvents are divided into polar and nonpolar according to their **relative permittivity** $\varepsilon_{\mathrm{r}}$ (dielectric constant) and dipole moment, those with $\varepsilon_{\mathrm{r}} > 15$ usually being counted as polar; and into protic and aprotic according to whether they can donate hydrogen bonds.

**Definition 8.8.1 (Protic and Polar Aprotic Solvents)** A solvent whose molecules contain a hydrogen bonded to an electronegative atom (O–H, N–H) and can act as a hydrogen-bond donor is called a **protic solvent**, such as water, alcohols, carboxylic acids and liquid ammonia; a solvent that is highly polar but contains no such hydrogen and cannot donate hydrogen bonds is called a **polar aprotic solvent**, such as DMSO, DMF, acetonitrile and acetone.

Properties of common solvents ($\varepsilon_{\mathrm{r}}$ at $20$–$25\,^\circ\mathrm{C}$, from the CRC Handbook):

| Solvent | Class | Boiling point / $^\circ\mathrm{C}$ | $\varepsilon_{\mathrm{r}}$ | Dipole moment / $(10^{-30}\,\mathrm{C\,m})$ |
|---|---|---|---|---|
| Water | Protic | 100 | 78.4 | 6.2 |
| Formic acid | Protic | 101 | 51 | 4.7 |
| Methanol | Protic | 65 | 32.7 | 5.7 |
| Ethanol | Protic | 78 | 24.6 | 5.6 |
| Propan-2-ol | Protic | 82 | 19.9 | 5.5 |
| Acetic acid | Protic | 118 | 6.2 | 5.8 |
| Dimethyl sulfoxide (DMSO) | Polar aprotic | 189 | 46.7 | 13.2 |
| *N*,*N*-Dimethylformamide (DMF) | Polar aprotic | 153 | 36.7 | 12.7 |
| Acetonitrile | Polar aprotic | 82 | 35.9 | 13.1 |
| Acetone | Polar aprotic | 56 | 20.7 | 9.6 |
| Dichloromethane | Aprotic, weakly polar | 40 | 8.9 | 5.3 |
| Tetrahydrofuran (THF) | Aprotic, weakly polar | 66 | 7.5 | 5.8 |
| Ethyl acetate | Aprotic, weakly polar | 77 | 6.0 | 5.9 |
| Diethyl ether | Aprotic, weakly polar | 35 | 4.3 | 3.8 |
| Benzene | Nonpolar | 80 | 2.3 | 0 |
| Hexane | Nonpolar | 69 | 1.9 | 0 |

### 8.8.2. Effect of the Solvent on SN1 and SN2

A solvent changes the free energy of activation through different degrees of solvation of the reactants and the transition state ([6.3.17](/6.3.17#sec-17.1.6)). The Hughes–Ingold rules can be summarized thus: when the transition state has more charge than the reactants (or more concentrated charge), a polar solvent accelerates the reaction; when it has less charge (or more dispersed charge), a polar solvent slows it down.

![Effect of solvent on the two mechanisms (schematic free-energy profiles): (a) in SN1 the transition state has charge separation, and a polar protic solvent stabilizes the ions and the transition state, lowering the barrier; (b) in SN2 with an anionic nucleophile, a protic solvent stabilizes the small reactant anion by hydrogen bonding more than the transition state with its dispersed charge, raising the barrier](./plots/solvent-effect.py)

In the rate-determining step of SN1 a pair of ions is formed from a neutral molecule, and the transition state has considerable charge separation. A polar protic solvent can stabilize the departing anion by dipoles and hydrogen bonds and the carbocation by lone pairs, greatly accelerating ionization. For the solvolysis of *tert*-butyl chloride in ethanol–water mixtures ($25\,^\circ\mathrm{C}$):

| Solvent | Ethanol | 40% water–60% ethanol | 80% water–20% ethanol | Water |
|---|---|---|---|---|
| Relative rate | 1 | 100 | 14 000 | 100 000 |

For SN2 the situation depends on the charge type. In reactions of an anionic nucleophile with a neutral substrate ($\ce{Nu- + RX}$), the negative charge goes from being concentrated on the small $\ce{Nu-}$ to being dispersed over both Nu and X, and the transition state is less polar than the reactants. A protic solvent surrounds the small anion tightly with hydrogen bonds and stabilizes the reactant, so the reaction is slower; the positive ends of the dipoles of polar aprotic solvents (the S of DMSO, the C of DMF) are buried inside the molecule and cannot solvate anions effectively, and only the negative end (O) solvates the cation, so the anion is "naked", high in energy and strongly nucleophilic. For the reactions of halides with $\ce{CH3I}$ ($25\,^\circ\mathrm{C}$, taking $\ce{Br-}$ in methanol as 1):

| Nucleophile | In methanol | In DMF | Increase (factor) |
|---|---|---|---|
| $\ce{I-}$ | 43 | 6 500 | 150 |
| $\ce{Br-}$ | 1 | 21 000 | $2\times10^4$ |
| $\ce{Cl-}$ | 0.04 | 41 000 | $1\times10^6$ |
| $\ce{F-}$ | 0.0006 | 49 000 | $8\times10^7$ |

The smaller the anion, the more strongly it is solvated in methanol and the greater the acceleration on changing to DMF, so much so that the order of nucleophilicity of the halides is completely reversed. This shows that "$\ce{I-} > \ce{F-}$" in rule 4 of Section 8.7.1 is mainly a solvent effect and not a property of the halides themselves. For an SN2 reaction in which a neutral nucleophile and a neutral substrate form an ion pair (as in the Menshutkin reaction, $\ce{R3N + R'X -> R3NR'+ X-}$), the transition state has charge separation and a polar solvent accelerates the reaction (data in [6.3.17](/6.3.17#sec-17.1.6)).

The synthetic conclusions are: for SN2, use a strong anionic nucleophile and a polar aprotic solvent (DMSO, DMF, acetone, acetonitrile); for SN1, use a weakly nucleophilic protic solvent (water, formic acid, alcohols).

### 8.8.3. Summary of the Influencing Factors

| Factor | Favors SN2 | Favors SN1 |
|---|---|---|
| Substrate | Methyl, primary; secondary (strong nucleophile, aprotic solvent) | Tertiary; secondary (weak nucleophile, protic solvent); allylic and benzylic react by either |
| Leaving group | Good leaving group | Good leaving group |
| Nucleophile | Strong, high concentration (mostly anions) | Weak ($\ce{H2O}$, $\ce{ROH}$), no effect on the rate |
| Solvent | Polar aprotic | Polar protic |
| Stereochemistry | Inversion (stereospecific) | Partial racemization, slightly more inversion |
| Rearrangement | None | Common |

## 8.9. Deciding the Mechanism: Diagnostic Experiments

To decide by which mechanism a nucleophilic substitution proceeds, we can examine in turn:

1. Kinetics: second order (first order in the nucleophile) or first order; whether changing the nucleophile concentration changes the rate.
2. Stereochemistry: whether a chiral substrate gives a product of inverted configuration or a partially racemized one.
3. Rearrangement: whether products with a changed skeleton are obtained.
4. Structure–reactivity relationships: whether the rate decreases (SN2) or increases (SN1) with increasing substitution at the $\alpha$ carbon; sensitivity to solvent polarity; when benzylic systems are examined with the **Hammett equation**, SN1 shows a large negative $\rho$ value ($\rho \approx -4$ to $-5$, [6.5.3](/6.5.3#sec-3.5)).
5. Isotope effects and the common-ion effect: $\alpha$-deuteration has a measurable secondary **kinetic isotope effect** on SN1 ($k_{\mathrm{H}}/k_{\mathrm{D}} \approx 1.10$–$1.25$, the carbon changing from $\mathrm{sp^3}$ to $\mathrm{sp^2}$) and close to 1 on SN2 ([6.5.3](/6.5.3#sec-3.11.4)); added $\ce{X-}$ slows SN1.

Two classical qualitative tests make use of these regularities and can be used to distinguish classes of alkyl halides:

- Silver nitrate in ethanol: $\ce{RX + AgNO3 ->[EtOH] RONO2 + AgX v}$. $\ce{Ag+}$ coordinates to the halogen and pulls away the halide, promoting ionization of the C–X bond (SN1 type). Tertiary, allylic and benzylic halides give a precipitate immediately at room temperature, secondary halides need heating, primary halides are slow even on heating, and vinyl and aryl halides do not react; for the same alkyl group RI > RBr > RCl.
- Sodium iodide in acetone: $\ce{R-Cl (Br) + NaI ->[acetone] R-I + NaCl v (NaBr v)}$. $\ce{I-}$ is a strong nucleophile and acetone a polar aprotic solvent, so the reaction goes by SN2; NaI dissolves in acetone whereas NaCl and NaBr do not, and precipitation drives the equilibrium (Le Chatelier's principle). Primary halides react fastest, secondary halides need heating, and tertiary halides hardly react. The order of reactivity is opposite for the two reagents, so they complement each other.

![Silver-assisted ionization in the silver nitrate–ethanol test. Ag⁺ accepts a lone pair of bromine in 2-bromo-2-methylpropane; the C–Br bond then breaks with both electrons going to bromine, AgBr precipitates, and the tert-butyl cation is captured by nitrate (or ethanol)](./plots/silver-assisted.py)

## 8.10. Neighboring Group Participation

### 8.10.1. The Phenomenon: Retention of Configuration and Anomalous Acceleration

SN2 inverts configuration, and SN1 partly racemizes it. Yet (*S*)-2-bromopropanoate hydrolyzes in dilute NaOH solution (or with $\ce{Ag2O}$ and water) to give (*S*)-lactic acid with retention of configuration; (*S*)-alanine undergoes **diazotization** with $\ce{NaNO2}$ in hydrochloric acid and gives (*S*)-2-chloropropanoic acid with retention of configuration (in water, (*S*)-lactic acid). Only in concentrated NaOH, where external $\ce{HO-}$ attacks directly, is (*R*)-lactic acid formed with inversion.

![Neighboring group participation in 2-bromopropanoate: the oxygen of the carboxylate displaces bromide from the back (intramolecular SN2, the first inversion) to give an α-lactone; water or hydroxide then opens the three-membered ring from the back (the second inversion); two inversions result in retention of configuration](./plots/ngp-lactone.py)

**Definition 8.10.1 (Neighboring Group Participation)** The phenomenon in which a group with lone pairs or $\pi$ electrons, suitably placed in the substrate molecule, attacks the reaction center from the back as the leaving group departs, forming a cyclic intermediate that is then opened by an external nucleophile, so that the reaction is accelerated or its stereochemical outcome changed, is called **neighboring group participation** (also called anchimeric assistance).

Neighboring group participation has three characteristics: (1) the rate is anomalously fast, because intramolecular attack is entropically far more favorable than intermolecular attack (the effective concentration is very high); (2) two SN2 inversions, with retention of configuration as the net result; (3) sometimes the product is rearranged, because the external nucleophile can attack either carbon of the cyclic intermediate.

### 8.10.2. Common Neighboring Groups

- Sulfur and nitrogen: mustard gas (bis(2-chloroethyl) sulfide, $\ce{(ClCH2CH2)2S}$) hydrolyzes much faster than the corresponding ether (bis(2-chloroethyl) ether). The sulfur atom first displaces $\ce{Cl-}$ intramolecularly to give a strained and extremely reactive three-membered cyclic sulfonium ion (an episulfonium ion), which is then opened by water or by N7 of guanine in DNA. Nitrogen mustards (such as bis(2-chloroethyl)methylamine) go through a similar aziridinium ion, can cross-link the two strands of DNA, and were the first anticancer alkylating agents; drugs such as cyclophosphamide are still designed on this principle ([6.6](/6.6)).
- Oxygen: a neighboring carboxylate (as in the figure above), an acetoxy group (forming a cyclic acetoxonium ion; neighboring group participation of the 2-acetoxy group controls the stereochemistry of glycosylation in carbohydrate chemistry, [6.5.32](/6.5.32)), and hydroxy and alkoxy groups (forming epoxide or tetrahydrofuran intermediates).
- Phenyl: Cram (1949) found that the acetolysis of both threo- and erythro-3-phenylbutan-2-yl tosylates in acetic acid proceeds mainly with retention of configuration, and that an optically active threo substrate gives a racemic threo product. This shows that the $\pi$ electrons of the benzene ring participate from the back to form a symmetrical bridged "phenonium ion", which acetic acid opens at either of the two carbons.
- C=C and C–C $\sigma$ bonds: the acetolysis of *anti*-7-norbornenyl tosylate is about $10^{11}$ times faster than that of the saturated analog, the $\pi$ electrons of the double bond participating from the back. The solvolysis of *exo*-2-norbornyl sulfonates is about 350 times faster than that of the *endo* isomers and gives racemic *exo* product; Winstein proposed that the C1–C6 $\sigma$ bond participates to form a bridged "nonclassical carbocation" (the positive charge shared by three carbons through a three-center, two-electron bond), while Brown argued for two rapidly equilibrating classical carbocations. This decades-long controversy was finally settled by low-temperature NMR and, in 2013, an X-ray crystal structure: the 2-norbornyl cation is a symmetrical bridged nonclassical structure.

![Neighboring group participation by sulfur in sulfur mustard. The sulfur lone pair displaces chloride intramolecularly (an intramolecular SN2), forming a strained three-membered episulfonium (thiiranium) ion; water, or N7 of guanine in DNA, then opens the ring at carbon. The second arm reacts in the same way, so the mustard can cross-link the two strands of DNA](./plots/mustard-episulfonium.py)

![Phenyl participation (Cram). In 3-phenyl-2-butyl tosylate the pi electrons of the phenyl ring on C3 attack C2 from the side opposite to the leaving group as tosylate departs, giving the symmetrical bridged phenonium ion (a spirocyclopropane fused to a cyclohexadienyl cation); acetic acid can open it at either carbon, each time with inversion at the carbon attacked](./plots/phenonium.py)

## 8.11. Biological Examples and Research Frontiers

The most important electrophilic methyl donor in the cell is *S*-adenosylmethionine (SAM): the sulfur of methionine bonds to C5′ of the adenosine of ATP to give a sulfonium ion, and the $\ce{R2S}$ at the sulfonium center is a good leaving group. A methyltransferase positions the nucleophilic atom of the substrate (C5 of a DNA cytosine, with the help of the enzyme; the amino group of a protein lysine; the hydroxy group of a catechol; and so on) behind the $\ce{S-CH3}$ bond and transfers the methyl group by the SN2 mechanism, with "inversion of configuration" at the methyl carbon (confirmed with the chiral methyl group $\ce{CHDT}$). Haloalkane dehalogenases use the carboxylate of an aspartate to displace the halogen of a haloalkane by SN2, forming a covalent ester intermediate that is then hydrolyzed; they degrade halogenated pollutants in the environment. The actions of carcinogenic alkylating agents (dimethyl sulfate, the metabolites of nitrosamines) and of anticancer drugs (nitrogen mustards) are all nucleophilic substitutions by nucleophilic atoms of DNA bases on them.

![Biological methylation by S-adenosylmethionine (SAM), as in catechol O-methyltransferase. The catechol oxygen, deprotonated in the active site, attacks the methyl carbon of the sulfonium ion, and the neutral thioether S-adenosylhomocysteine (SAH) leaves (SN2). Ado = 5′-deoxyadenosyl, R = CH₂CH₂CH(NH₃⁺)CO₂⁻](./plots/sam-methylation.py)

In the gas phase SN2 reactions can be studied without interference from solvent. Wester and co-workers (2008) used crossed molecular beams and ion imaging to observe single collisions of $\ce{Cl- + CH3I}$ directly and found that, besides the textbook direct back-side attack, there is at higher collision energies a "roundabout" mechanism in which $\ce{CH3I}$ is first knocked into a complete rotation before $\ce{Cl-}$ displaces the iodine. Such experiments, together with quantum-chemical calculations, carry the qualitative picture of this chapter down to the level of atomic motion.

## Summary

- Nucleophilic substitution $\ce{Nu- + R-X -> R-Nu + X-}$ is attack of a nucleophile (a Lewis base) on the electron-poor carbon bearing the leaving group. The polarity and cleavability of the C–X bond of alkyl halides (bond energy decreasing from F to I) are the source of their reactivity.
- The two mechanisms are distinguished by their rate laws (Definition 8.2.1, Definition 8.2.2):

  | | SN2 | SN1 |
  |---|---|---|
  | Rate law | $v = k_2[\ce{RX}][\ce{Nu}]$ | $v = k_1[\ce{RX}]$ |
  | Steps | One step, trigonal bipyramidal transition state | Two steps, through a carbocation intermediate |
  | Stereochemistry | Walden inversion (Definition 8.4.1), stereospecific | Partial racemization, slightly more inversion (ion pairs, Definition 8.4.2) |
  | Rearrangement | None | Common (1,2-hydride and 1,2-alkyl shifts) |
  | Substrate reactivity | Methyl > primary > secondary ≫ tertiary; sensitive to $\alpha$ and $\beta$ hindrance | Tertiary > secondary > primary; allylic and benzylic fast |
  | Nucleophile | Strong nucleophiles accelerate | No effect on the rate |
  | Solvent | Polar aprotic (anionic nucleophiles) | Polar protic |

- The carbocation (Definition 8.3.1) is a planar $\mathrm{sp^2}$ intermediate; its stability is tertiary > secondary > primary > methyl (hyperconjugation); conjugation, lone pairs on heteroatoms and aromaticity stabilize it further; it tends to rearrange to a more stable carbocation. Vinyl, aryl and bridgehead halides undergo neither mechanism readily.
- The leaving ability of a leaving group parallels the strength of its conjugate acid: $\ce{TfO-} > \ce{I-} > \ce{Br-} \approx \ce{TsO-} > \ce{Cl-} \gg \ce{F-}$; $\ce{HO-}$ and $\ce{RO-}$ must first be protonated or converted into sulfonate esters.
- Nucleophilicity (Definition 8.7.1) is a kinetic property: anions > neutral species; across a period it follows basicity; down a group (in protic solvents) $\ce{I-} > \ce{Br-} > \ce{Cl-} > \ce{F-}$, with the order reversed in aprotic solvents; bulky strong bases are weak nucleophiles. The Swain–Scott equation (Eq. (8.1)) makes it quantitative.
- Neighboring group participation (Definition 8.10.1): intramolecular back-side attack followed by external attack causes two inversions, so the result is retention of configuration accompanied by acceleration; S, N, O, phenyl, $\pi$ bonds and $\sigma$ bonds can all participate.

## Questions

1. The energy diagram for the hydrolysis of *tert*-butyl bromide has two transition states and one intermediate. Which energy difference in the diagram corresponds to the apparent activation energy of the reaction? Will adding NaOH speed up the reaction?

   **Answer** It corresponds to the energy difference from the reactant to the first transition state (ionization of the C–Br bond): ionization is the rate-determining step, the second transition state is lower in energy than the first, and once the carbocation is formed it is captured rapidly by water. The rate law $v = k_1[\ce{t-BuBr}]$ is independent of the nucleophile, so adding $\ce{HO-}$ does not speed up substitution; but a strong base makes E2 elimination the main reaction ([6.5.9](/6.5.9#sec-9.6)), and the product becomes 2-methylpropene.

2. What are the main products when 2-bromo-3-methylbutane is (a) heated in water and (b) treated with NaI in acetone? Explain with mechanisms.

   **Answer** (a) Water is a weak nucleophile and a protic solvent, so the secondary halide ionizes by SN1; the secondary carbocation formed becomes a tertiary carbocation by a 1,2-hydride shift, and the main product is 2-methylbutan-2-ol (see the figure in Section 8.3.3), with a little unrearranged 3-methylbutan-2-ol and the elimination product 2-methylbut-2-ene. (b) $\ce{I-}$ is a strong nucleophile and a weak base, and acetone is a polar aprotic solvent, so the reaction goes by SN2 to give unrearranged 2-iodo-3-methylbutane (with inversion of configuration for a chiral substrate); SN2 involves no carbocation, so there is no rearrangement.

3. (*R*)-2-Bromo-1-methoxypropane reacts with NaCN in DMSO by SN2. Is the configuration of the product designated *R* or *S*? Does an SN2 reaction always change the R/S label?

   **Answer** The product, 3-methoxy-2-methylpropanenitrile, has the (*R*) configuration. SN2 inverts the spatial arrangement, but the CIP order also changes: in the substrate $\ce{-Br} > \ce{-CH2OCH3} > \ce{-CH3} > \ce{-H}$, whereas in the product $\ce{-CH2OCH3}$ (C bearing O) $> \ce{-CN}$ (C bearing N, N, N; O > N) $> \ce{-CH3} > \ce{-H}$, so the new group drops from first to second place. The spatial inversion and the exchange of the first two ranks each change the label once, and the result is still R. The R/S label therefore does not necessarily change; inversion of configuration must be judged from the spatial arrangement and not from the label alone.

4. Arrange the following compounds in order of reactivity in SN2 reactions (with NaI/acetone) and in SN1 reactions (in 80% ethanol): (A) 1-bromobutane; (B) 2-bromobutane; (C) 2-bromo-2-methylpropane; (D) 3-bromoprop-1-ene; (E) 1-bromo-2,2-dimethylpropane.

   **Answer** SN2: D > A > B > E > C. The allylic halide is fastest (the transition state is conjugated with the $\pi$ bond); primary > secondary; neopentyl halide E, although primary, has its back side blocked by the *tert*-butyl group at the $\beta$ position and is slower than a secondary halide; the tertiary halide C hardly reacts. SN1: C > D > B > A ≈ E. The tertiary and allyl cations are the most stable (the order of D and C depends on the solvent, and they are close); secondary > primary; A and E are primary halides, for which SN1 is extremely slow (E undergoes methyl migration on solvolysis).

5. Why is the yield of the following reaction very low? How could it be improved? $\ce{(CH3)3C-Br + CH3CH2O- Na+ -> (CH3)3C-O-CH2CH3}$

   **Answer** A tertiary halide cannot undergo SN2, and sodium ethoxide is a strong base, so E2 elimination predominates and 2-methylpropene is obtained. *tert*-Butyl ethyl ether should be made by interchanging the two partners: potassium *tert*-butoxide as the nucleophile and bromoethane (a primary halide) in an SN2 reaction, $\ce{(CH3)3C-O- K+ + CH3CH2Br -> (CH3)3C-O-CH2CH3 + KBr}$ (Williamson ether synthesis, [6.5.10](/6.5.10#sec-10.2.2)).

6. Conversion of 1-bromooctane to octyl acetate with potassium acetate in refluxing acetic acid gives a poor yield. The reaction is markedly faster when 18-crown-6 is added or tetrabutylammonium acetate is used instead. Why?

   **Answer** In acetic acid, $\ce{K+}$ forms a tight ion pair with $\ce{CH3COO-}$, and acetic acid solvates $\ce{CH3COO-}$ by hydrogen bonds, so its nucleophilicity is very low. 18-Crown-6 encapsulates $\ce{K+}$ and tetrabutylammonium is a very bulky cation; both weaken the association with the anion and make the acetate more "free", increasing the rate of SN2. In general, the freer the anion of the nucleophile, the faster the SN2 reaction.

7. Which reagents and conditions should be chosen for each of the following transformations? (a) (*S*)-octan-2-ol → (*R*)-2-bromooctane; (b) (*S*)-octan-2-ol → (*S*)-2-bromooctane; (c) 1-chlorobutane → pentanenitrile.

   **Answer** (a) One inversion of configuration is needed: first form the (*S*)-tosylate with TsCl/pyridine (configuration retained), then carry out SN2 with LiBr in acetone or DMF (inversion) to give (*R*)-2-bromooctane; alternatively use $\ce{PBr3}$ directly (SN2, inversion, [6.5.9](/6.5.9#sec-9.7.2)). (b) Two inversions are needed: form the (*S*)-tosylate with TsCl/pyridine, carry out SN2 with $\ce{CH3COO-}$ in DMF to give the (*R*)-acetate, and hydrolyze it to (*R*)-octan-2-ol (ester hydrolysis cleaves the acyl–oxygen bond and does not touch the stereogenic carbon); then invert as in (a) to obtain (*S*)-2-bromooctane. (c) NaCN in DMSO by SN2: $\ce{CH3CH2CH2CH2Cl + NaCN -> CH3CH2CH2CH2CN + NaCl}$; in DMSO the $\ce{CN-}$ ion is naked and strongly nucleophilic, and even a primary alkyl chloride reacts smoothly.

8. How can one explain that (*S*)-2-bromopropanoic acid hydrolyzes to (*S*)-lactic acid in dilute NaOH and to (*R*)-lactic acid in concentrated NaOH?

   **Answer** In dilute base the concentration of external $\ce{HO-}$ is low, and the intramolecular carboxylate first displaces $\ce{Br-}$ from the back (the first inversion) to give an $\alpha$-lactone; water then opens the three-membered ring from the back (the second inversion), and the net result is retention of configuration, giving (*S*)-lactic acid (see the figure in Section 8.10.1). In concentrated base the concentration of $\ce{HO-}$ is high, the rate $k_2[\ce{HO-}]$ of the intermolecular SN2 reaction exceeds that of intramolecular participation, and a single direct inversion gives (*R*)-lactic acid.

9. The solvolysis of $\ce{XC6H4C(CH3)2Cl}$ (substituted cumyl chlorides) in 90% acetone was studied with the Hammett equation and gave $\rho \approx -4.5$ (plotted against $\sigma^+$). What does this result show?

   **Answer** A large negative $\rho$ shows that a great deal of positive charge develops on the benzylic carbon in the rate-determining step, and electron-donating substituents strongly accelerate the reaction, which is characteristic of SN1 ionization to a carbocation. The better correlation with $\sigma^+$ (rather than $\sigma$) shows that there is direct conjugation (resonance) between the para substituent and the positive charge, which is delocalized into the ring ([6.5.3](/6.5.3#sec-3.5)).
