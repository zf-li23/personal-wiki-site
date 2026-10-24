---
title: "Main-Group Organoelement Compounds: Lithium, Magnesium, Boron, Silicon, Fluorine and Iodine"
description: The polarity of M–C bonds in main-group organometallic compounds; preparation of organolithium reagents (lithium–halogen exchange), aggregation and 4c–2e bonding, solvents and stability, directed ortho metalation and addition reactions; the single-electron-transfer mechanism of formation, structure and Schlenk equilibrium of Grignard reagents; bonding in organoboron compounds, borane reagents and the selectivity of hydroboration, asymmetric hydroboration, 1,2-metallate rearrangements (carbonylation and Matteson homologation), boronic acids and boronic esters; bonding in organosilicon compounds, silyl ether protecting groups, the β-silicon effect and the Hosomi–Sakurai reaction, the Peterson olefination; properties of organofluorine compounds, their role in drugs, nucleophilic and electrophilic fluorination; the three-center four-electron bond of hypervalent iodine, IBX and the Dess–Martin oxidation, diaryliodonium salts.
source_hash: 0eb87e7da2ef
---

The previous chapter, [6.5.26](/6.5.26), treated phosphorus and sulfur from Groups 15 and 16. This chapter treats the other **main-group elements** that matter most in organic synthesis: the electropositive metals lithium and magnesium; boron and silicon, whose **electronegativity** is close to or slightly lower than that of carbon; and fluorine (the most electronegative element) and iodine (the most polarizable, and the one most readily forming **hypervalent molecules**), which stand at the two extremes. They bond to carbon in quite different ways (the C–Li and C–Mg bonds are strongly polarized toward carbon, B has an empty p orbital, the bonds of Si to O and F are especially strong and Si can be five-coordinate, the C–F bond is the strongest single bond carbon can form, and iodine can accommodate more than eight valence electrons through the **three-center four-electron bond**), and each bonding feature corresponds to a class of irreplaceable reagents.

The preparation and basic reactions of **organolithium reagents**, **Grignard reagents** and **Gilman reagents** were discussed in [6.5.10](/6.5.10#sec-10.3), and the **hydroboration** of alkenes in [6.5.11](/6.5.11#sec-11.4.6); this chapter treats their structure and mechanisms, together with new material from the chemistry of organoboron, organosilicon, organofluorine and organoiodine compounds. Boronic acids and boronic esters are the substrates of the **Suzuki–Miyaura coupling** in [6.5.29](/6.5.29#sec-29.4.3), which this chapter prepares for; the organometallic chemistry of transition metals is taken up in [6.5.28](/6.5.28).

## 27.1. Main-Group Organometallic Compounds

Compounds in which carbon is bonded directly to a metal are organometallic compounds (Definition 26.1.1 in [6.5.26](/6.5.26#def-26.1.1)). Among the main-group metals, the polarity of the C–M bond increases with the electropositivity of the metal (see the table in [6.5.10](/6.5.10#sec-10.3.1)):

| Group | Elements (Pauling **electronegativity**) | C–M bond | Representatives |
|---|---|---|---|
| 1 | Li 0.98, Na 0.93, K 0.82, Rb, Cs | Li: strongly **polar covalent bond**; Na and below: essentially ionic | $n$-BuLi; $\ce{C2H5Na}$, $\ce{PhCH2K}$ |
| 2 | Be 1.57, Mg 1.31, Ca 1.00 | Be, Mg: polar covalent bonds; organoberyllium compounds are electron-deficient | $\ce{RMgX}$, $\ce{R2Mg}$ |
| 13 | B 2.04, Al 1.61 | covalent; B and Al are electron-deficient in the valence shell and are **Lewis acids** | $\ce{R3B}$, $\ce{Et3Al}$ |
| 14 | Si 1.90, Sn 1.96 | covalent, of low polarity | $\ce{Me4Si}$, $\ce{Bu3SnH}$ |

The electronegativity of carbon is 2.55. Modern calculations (Streitwieser and coworkers) indicate that bonding in C–Li is mainly electrostatic; but $\ce{Li+}$ is very small and has a high **polarizing power**, so some covalent character with the **carbanion** remains, which is why organolithium compounds dissolve in hydrocarbons and form well-defined aggregates (Section 27.2.2). $\ce{Na+}$ and $\ce{K+}$ are larger, so C–Na and C–K bonds are essentially ionic, and organosodium and organopotassium compounds are insoluble in hydrocarbons. Moving to the right from Group 1, the carbanionic character and reactivity of carbon decrease in turn: organopotassium and organosodium compounds are extremely strong bases and decompose even in ethers, organolithium and organomagnesium compounds are the most useful carbon **nucleophiles** in the laboratory, and the carbon of organoboron, organosilicon and organotin compounds is hardly nucleophilic without activation, passing on carbon only by forming "ate" **coordination complexes** (borates, silicates) or by transmetalation to a transition metal ([6.5.29](/6.5.29#sec-29.4.1)).

## 27.2. Organolithium Compounds

### 27.2.1. Preparation of Organolithium Compounds

1. Direct synthesis: an alkyl halide reacts with lithium metal in a hydrocarbon or ether solvent ([6.5.10](/6.5.10#sec-10.4.1)): $\ce{R-X + 2 Li -> R-Li + LiX}$. RX is usually a chloride or bromide; methyllithium can be made from chloromethane and is often made from iodomethane (giving a solution containing LiI). Lithium containing 1%–2% sodium speeds the reaction. Unlike **Grignard reagents**, alkyllithiums dissolve in hydrocarbons such as pentane and hexane, and commercial $n$-BuLi, $s$-BuLi and $t$-BuLi are all hydrocarbon solutions.
2. Lithium–metal exchange (**transmetalation**): organotin and organomercury compounds exchange with alkyllithiums, for example $\ce{Bu3Sn-R + n-BuLi -> R-Li + Bu4Sn}$. The exchange proceeds with retention of configuration at carbon, so a chiral α-alkoxystannane gives a configurationally defined α-alkoxyorganolithium (Still).
3. Lithium–halogen exchange:

**Definition 27.2.1 (Lithium–Halogen Exchange)** The reaction in which an organolithium R′Li and an organic halide RX (X = Br, I) exchange lithium and halogen to give a new organolithium RLi is called **lithium–halogen exchange** (Gilman and Wittig, 1938):

$$
\ce{R-X + R'-Li <=> R-Li + R'-X}.
$$

The exchange is reversible, and the equilibrium lies on the side of the more stable **carbanion**: when R is aryl or alkenyl (an $\mathrm{sp^2}$ carbon, whose orbital carrying the negative charge has more s character) and R′ is alkyl, the equilibrium lies almost completely to the right. The reaction is extremely fast, complete in minutes at $-78$ to $-100\,^\circ\mathrm{C}$, faster than attack of the organolithium on many functional groups (esters, nitriles), so aryllithiums bearing these groups can be prepared at low temperature. The reactivity order is I > Br ≫ Cl; fluorides do not exchange. With $t$-BuLi, 2 equivalents are used: the second molecule of $t$-BuLi immediately undergoes **E2** elimination with the $t$-BuBr formed (giving isobutene, isobutane and LiBr), which makes the exchange irreversible and also prevents coupling of the ArLi formed with $t$-BuBr (Question 2). The exchange of aryl iodides passes through an iodine "ate" **coordination complex** $\ce{[Ar-I-R']- Li+}$ (observed by Reich using low-temperature NMR), which can be regarded as nucleophilic attack of a carbanion on iodine; the exchange of alkyl halides may partly proceed by radical pathways.

```smiles
Brc1ccc(cc1)C#N.CCCC[Li]>>[Li]c1ccc(cc1)C#N.CCCCBr
```

![Lithium–halogen exchange and the role of 2 equivalents of $t$-BuLi. Top: the electrons of the C–Li bond of butyllithium attack the iodine of iodobenzene to give the iodine "ate" complex $\ce{[Ph-I-Bu]- Li+}$, and the Ph–I bond then breaks toward the phenyl carbon, giving phenyllithium and 1-iodobutane, the equilibrium favoring the more stable sp² carbanion. Bottom: with $t$-BuLi, the C–Li electrons of a second molecule of $t$-BuLi remove a β-H of the $t$-butyl bromide formed (E2), releasing isobutane, isobutene and LiBr and making the exchange irreversible](./plots/lithium-halogen-exchange.py)

4. Metalation (deprotonation): an alkyllithium removes the proton of a fairly acidic C–H bond; see Section 27.2.4.

### 27.2.2. Aggregation and Bonding

In an isolated RLi molecule Li has only one valence electron but four valence orbitals, so a 2c–2e C–Li bond is far from "using up" these orbitals, and organolithium compounds exist as aggregates in crystals and in solution. Methyllithium is a tetramer $\ce{(CH3Li)4}$ in the crystal and in ether solution: the four Li atoms sit at the vertices of a tetrahedron, the four methyl groups lie above the four faces of the tetrahedron, and each carbon is bonded to three Li atoms ($\mu_3$-$\ce{CH3}$), the whole being a distorted $\ce{Li4C4}$ cubane skeleton.

![Structure of the methyllithium tetramer $\ce{(CH3Li)4}$: the four lithium atoms form a tetrahedron (dashed lines), the four methyl carbons lie outside the four faces of the tetrahedron, and each carbon is bonded to three lithium atoms, giving a $\ce{Li4C4}$ cubane-type skeleton (hydrogen atoms omitted)](./plots/methyllithium-tetramer.py)

In the covalent picture, each $\ce{Li3C}$ unit combines an $\mathrm{sp^3}$ orbital of carbon with orbitals of three Li atoms into one **bonding orbital** holding an electron pair, a four-center two-electron (4c–2e) bond, and four such bonds hold the skeleton together. Like the B–H–B **three-center two-electron bond** of diborane ([6.1.14](/6.1.14#sec-14.6.3)), this is how **electron-deficient compounds** "share" electrons (the same conclusion follows from combining the group orbitals of the $\ce{Li4}$ tetrahedron with the orbitals of the four carbons). Since C–Li bonding is predominantly ionic, however, this tetramer can also be regarded as an ionic cluster of alternating $\ce{CH3-}$ and $\ce{Li+}$; the two descriptions give the same geometry.

The degree of aggregation depends on the steric bulk of the hydrocarbon group and the coordinating ability of the solvent. The stronger the electron-donating ability of the solvent (or additive) and the stronger its coordination to Li, the lower the degree of aggregation:

| RLi | Hydrocarbon (hexane, cyclohexane) | $\ce{Et2O}$ | THF | With TMEDA |
|---|---|---|---|---|
| MeLi | insoluble | tetramer | tetramer | still tetramer |
| EtLi | hexamer | n/a | n/a | n/a |
| $n$-BuLi | hexamer | tetramer | tetramer ⇌ dimer | dimer |
| $t$-BuLi | tetramer | dimer | monomer | n/a |
| PhLi | insoluble | tetramer ⇌ dimer | dimer ⇌ monomer | dimer |
| $\ce{PhCH2Li}$, allyllithium | n/a | highly aggregated | mainly monomer | n/a |
| LDA | various aggregates | dimer | dimer | n/a |

(Compiled from Reich's review, Chem. Rev. 2013.)

In general, forms of lower aggregation are more reactive, sometimes by several orders of magnitude; but the species actually reacting may also be a small amount of monomer or a mixed aggregate, so one cannot look only at the major form. TMEDA ($N,N,N',N'$-tetramethylethane-1,2-diamine) is a bidentate ligand that breaks up the hexamer of $n$-BuLi into the dimer $\ce{[n-BuLi(TMEDA)]2}$ and further polarizes the C–Li bond by coordination, so that with TMEDA $n$-BuLi metalates benzene and toluene fairly quickly. Stronger donors such as HMPA and PMDTA can lead further to monomers or separated **ion pairs**.

### 27.2.3. Stability and Solvents

Organolithium compounds are extremely basic and attack ether solvents. $n$-BuLi first removes an α-H of THF, and the 2-lithiated THF formed then decomposes by retro-[3+2] cycloelimination to ethylene and the lithium enolate of acetaldehyde:

```smiles
C1CCOC1.CCCC[Li]>>C=C.C=CO[Li]
```

![Decomposition of THF by $n$-BuLi: the electrons of the C–Li bond of butyllithium remove the proton on the carbon next to oxygen, giving 2-lithiotetrahydrofuran and butane; the former undergoes retro-[3+2] cycloelimination: the electrons of the C–Li bond form a C=C bond, the opposite C–C bond becomes the double bond of ethylene, and the C–O bond breaks toward oxygen, giving ethylene and the lithium enolate of acetaldehyde](./plots/thf-cleavage.py)

The half-life of $n$-BuLi in THF at $20\,^\circ\mathrm{C}$ is only about 2 h, while it can be stored for days in diethyl ether, and $t$-BuLi in THF lasts only a few hours even at $-40\,^\circ\mathrm{C}$. Stock organolithium solutions are therefore best prepared and stored in hydrocarbon solvents, with the ether added at low temperature when needed; the actual concentration must be determined by titration (for example with diphenylacetic acid) before use. Alkyllithiums react violently and exothermically with water and oxygen, and $t$-BuLi ignites in air; for handling see [6.5.10](/6.5.10#sec-10.4.1).

### 27.2.4. Metalation and Directed Ortho Metalation

Proton transfer between an organolithium and a C–H acid is an acid–base equilibrium ([6.5.3](/6.5.3#sec-3.1.4)) that lies on the side of the weaker acid: the $\mathrm{p}K_{\mathrm{a}}$ of butane is about 50, so $n$-BuLi can remove protons from terminal alkynes (about 25), dithianes (about 31, [6.5.16](/6.5.16#sec-16.10.2)), the **benzylic position** of toluene (about 41) and even benzene (about 43), forming new organolithium compounds. This replacement of the hydrogen of a C–H bond by an alkali metal is called metalation, and is itself a method of preparing organolithium compounds. A thermodynamically feasible metalation may be kinetically slow: benzene and $n$-BuLi hardly react in hexane, and phenyllithium forms rapidly only after TMEDA is added.

If a benzene ring carries a substituent with a lone pair, metalation is directed to its ortho position:

**Definition 27.2.2 (Directed Ortho Metalation)** The reaction in which a heteroatom-containing substituent on an aromatic ring (a directed metalation group, DMG) coordinates the Li of an alkyllithium, so that the base removes the proton ortho to that substituent and selectively gives the ortho-aryllithium, is called **directed ortho metalation** (DoM; Gilman and Wittig, about 1940; developed systematically by Snieckus).

![Directed ortho metalation of N,N-diethylbenzamide: the amide oxygen coordinates the lithium of the alkyllithium (dashed line), bringing the basic carbon close to the ortho C–H bond (the complex-induced proximity effect); the electrons of the C–Li bond remove the ortho proton, and the aryllithium formed is still chelated by the amide oxygen; reaction with iodomethane introduces a methyl group ortho to the directing group](./plots/dom.py)

The ortho selectivity has two sources: coordination of Li to the DMG keeps the base near the ortho C–H bond (the complex-induced proximity effect, Beak), and the high **electronegativity** of the DMG acidifies the ortho C–H bond through the **inductive effect**; the aryllithium product is then stabilized by chelation to the DMG. The commonly used directing groups, roughly in order of directing power, are:

| Directing power | DMG |
|---|---|
| Strong | $\ce{-OCONEt2}$ (carbamate), $\ce{-CONEt2}$, $\ce{-CON^{-}R}$, $\ce{-SO2NR2}$, oxazoline, $\ce{-NHBoc}$ |
| Moderate | $\ce{-OMe}$, $\ce{-OCH2OMe}$, $\ce{-CH2NMe2}$, $\ce{-CF3}$, $\ce{-F}$, $\ce{-Cl}$ |
| Weak | $\ce{-NMe2}$, $\ce{-O-}$ |

Common bases are $s$-BuLi/TMEDA ($-78\,^\circ\mathrm{C}$, THF), $n$-BuLi or LDA, and LiTMP. The aryllithium formed reacts with various **electrophiles** ($\ce{CO2}$, DMF, aldehydes and ketones, $\ce{I2}$, $\ce{B(OMe)3}$, $\ce{Me3SiCl}$, alkyl halides) to give 1,2-disubstituted arenes. This complements the **directing effect** of **electrophilic aromatic substitution** ([6.5.14](/6.5.14#sec-14.3.2)): electron-donating groups in electrophilic substitution often give mixtures dominated by the para product, whereas DoM reacts only ortho, and preferentially at the position between two DMGs (the two DMGs act cooperatively).

A few points should be noted. Among the halogens only F (and Cl) are good DMGs, while Br and I preferentially undergo lithium–halogen exchange; o-fluorophenyllithium (and o-chlorophenyllithium) loses LiF above about $-50\,^\circ\mathrm{C}$ to give **benzyne** ([6.5.15](/6.5.15#sec-15.1.3)). On warming, an ortho-lithiated aryl carbamate undergoes migration of the carbamoyl group from oxygen to the ortho carbon, giving a salicylamide, the anionic **Fries rearrangement** (Snieckus, [6.5.15](/6.5.15#sec-15.8.3)).

### 27.2.5. Addition Reactions

To carbon–carbon multiple bonds: addition of organolithium compounds to isolated alkenes (carbolithiation) is not easy, but they can initiate the anionic polymerization of conjugated dienes and styrene. $n$-BuLi initiates the polymerization of isoprene in hydrocarbon solvents to give polyisoprene with more than about 90% cis-1,4 structure, with properties close to natural rubber; in polar solvents such as THF the ion pair at the chain end is looser and the 3,4- and 1,2-structures increase (Question 1). This polymerization has no termination step ("living polymerization", Szwarc, 1956), and two monomers can be added in sequence to give block copolymers (the SBS thermoplastic elastomers), an important type of **addition polymerization** ([6.5.11](/6.5.11#sec-11.11)).

To carbon–nitrogen multiple bonds: an organolithium adds to the C=N of pyridine (at the 2 position) to give the lithium salt of a 1,2-dihydropyridine, which on heating loses LiH and rearomatizes to give a 2-alkylpyridine (Ziegler, 1930), similar to the **Chichibabin reaction** of pyridine ([6.5.25](/6.5.25#sec-25.5.3)). Organolithium compounds add to nitriles to give iminyl anions, which are negatively charged and do not add a second molecule of RLi, and hydrolysis gives ketones ([6.5.20](/6.5.20#sec-20.4.3)).

![Addition of phenyllithium to pyridine (Ziegler): the electrons of the C–Li bond add to C2 next to nitrogen, the electrons of C=N move onto nitrogen, giving the lithium salt of a 1,2-dihydropyridine; on heating the lone pair on nitrogen re-forms the C=N bond, the C2–H bond breaks and hydrogen leaves as hydride (LiH), restoring aromaticity and giving 2-phenylpyridine; the last step is the same as in the Chichibabin reaction](./plots/pyridine-organolithium.py)

To carbon–oxygen multiple bonds: the addition of organolithium compounds to aldehydes and ketones is similar to that of **Grignard reagents** ([6.5.16](/6.5.16#sec-16.7.3)), and the stereochemistry can likewise be predicted by the **Felkin–Anh model**: when the α carbon carries a group of high **electronegativity** such as Cl, the **nucleophile** attacks the carbonyl group from the side opposite the C–Cl bond (the polar Felkin–Anh model). There are two differences:

- With α,β-unsaturated carbonyl compounds, organolithium compounds give almost only **1,2-addition** (the addition is fast and irreversible, a hard nucleophile attacking the hard carbonyl carbon); Grignard reagents give mixtures of 1,2- and 1,4-addition, and organocopper reagents undergo **conjugate addition** ([6.5.17](/6.5.17#sec-17.6.2)).
- With carboxylic acids: the first molecule of RLi removes the proton to give the lithium carboxylate, and the second adds to the carboxylate to give a stable lithium gem-diolate (the **tetrahedral intermediate** carries two negative charges and cannot collapse to a ketone by losing $\ce{O^2-}$); only hydrolysis gives the ketone, so there is no further addition to a tertiary alcohol. Grignard reagents cannot add to carboxylates in this way.

```smiles
OC(=O)c1ccccc1.C[Li]>>CC(=O)c1ccccc1
```

![Ketone synthesis from an organolithium and a carboxylic acid: the first molecule of RLi removes the proton of the carboxylic acid (not drawn), and the electrons of the C–Li bond of the second add to the carbonyl carbon of lithium benzoate, the electrons of C=O moving onto oxygen to give the dilithium salt of a gem-diol; this tetrahedral intermediate with two negative charges cannot lose $\ce{O^2-}$ and does not collapse to the ketone in the presence of the organolithium, so no further addition occurs; acidic workup gives the hydrate, which loses water to give acetophenone](./plots/organolithium-carboxylate.py)

### 27.2.6. Reactions with Alkyl Halides

Coupling (alkylation) of organolithium compounds with alkyl halides looks simple but is actually complicated, because lithium–halogen exchange competes and radical pathways may also operate. For example, phenyllithium and 1-iodobutane hardly give butylbenzene: exchange gives iodobenzene and butyllithium, and the latter then couples with iodobutane or eliminates, giving mixtures of octane, butenes and so on. **Cross-coupling** forming C–C bonds is generally carried out instead with organocopper reagents (**Gilman reagents**, [6.5.10](/6.5.10#sec-10.4.2)) or by transition-metal catalysis ([6.5.29](/6.5.29#sec-29.4)); organolithium compounds undergo **SN2** alkylation well only with reactive primary alkyl halides, allylic and benzylic halides, epoxides, dimethyl sulfate and the like.

## 27.3. Organomagnesium Compounds

### 27.3.1. Mechanism of Formation of Grignard Reagents

**Grignard reagents** form from alkyl halides on the surface of magnesium by **single electron transfer** ([6.5.10](/6.5.10#sec-10.3.2)):

$$
\ce{R-X + Mg -> [R-X]^{.-} + Mg^{.+} -> R^{.} + XMg^{.} -> R-MgX}.
$$

Magnesium gives one electron to the σ* orbital of C–X, the radical anion immediately fragments into an alkyl radical and a halide ion, and the radical then combines with $\ce{Mg^{.+}X}$ on the surface. Evidence that the intermediate is a radical includes: preparation from 6-bromohex-1-ene gives some cyclopentylmethylmagnesium bromide (cyclization of the hex-5-enyl radical, a **radical clock**, [6.5.7](/6.5.7#sec-7.5)); and Grignard reagents from chiral cyclopropyl bromides (such as 1-bromo-1-methyl-2,2-diphenylcyclopropane) are largely racemic, retaining only a little optical activity (Walborsky). Whether the radical stays adsorbed on the magnesium surface (Walborsky) or diffuses into solution and returns to the surface (Garst, Whitesides) has been argued for decades, and in fact both contribute.

![Evidence for radicals in the formation of Grignard reagents (radical clock): single electron transfer at the magnesium surface makes 6-bromohex-1-ene lose bromide, giving the hex-5-enyl radical; a part cyclizes by 5-exo-trig closure before being captured by magnesium ($k \approx 2\times10^5\,\mathrm{s^{-1}}$ at 25 °C): the single electron of the radical and one π electron form the new C–C bond (dashed line) while the other π electron moves to the terminal carbon, giving the cyclopentylmethyl radical, which finally gives cyclopentylmethylmagnesium bromide](./plots/radical-clock-grignard.py)

Poorly reactive halides (aryl chlorides, some bulky halides) can be treated with Rieke magnesium: reduction of $\ce{MgCl2}$ with potassium metal (or lithium and naphthalene) in THF gives a magnesium powder of very small particle size, free of oxide film and highly reactive, which reacts with aryl bromides even at $-78\,^\circ\mathrm{C}$ and makes Grignard reagents bearing ester and nitrile groups accessible. A more convenient modern method is halogen–magnesium exchange:

$$
\ce{Ar-I (\text{or } Ar-Br) + i-PrMgCl.LiCl -> Ar-MgCl.LiCl + i-PrI}.
$$

As in lithium–halogen exchange, the equilibrium favors the more stable $\mathrm{sp^2}$ **carbanion**. LiCl breaks up the aggregates of the Grignard reagent and forms a more reactive magnesiate, so the exchange proceeds from $-15\,^\circ\mathrm{C}$ to room temperature (Knochel's "turbo Grignard", 2004), and esters, nitriles and nitro groups in the molecule survive.

### 27.3.2. Structure and the Schlenk Equilibrium

Crystal structures show that in **Grignard reagents** magnesium is always coordinated by ether and four- or five-coordinate: in $\ce{EtMgBr(OEt2)2}$ and $\ce{PhMgBr(OEt2)2}$ magnesium is tetrahedral (Rundle, 1964), and in $\ce{MeMgBr(THF)3}$ it is trigonal bipyramidal. In solution, RMgX is in **Schlenk equilibrium** with $\ce{R2Mg}$ and $\ce{MgX2}$ (Definition 10.3.2 in [6.5.10](/6.5.10#sec-10.3.2)):

$$
\ce{2 RMgX <=> R2Mg + MgX2},
$$
and each component also exists as halide-bridged dimers and oligomers. Adding 1,4-dioxane precipitates $\ce{MgX2(dioxane)}$ and gives a halide-free dialkylmagnesium.

Two mechanisms are also possible for addition of Grignard reagents to carbonyl groups: polar **nucleophilic addition** (through a four- or six-membered transition state, the electron pair of the C–Mg bond attacking the carbonyl carbon directly) and **single electron transfer** followed by radical coupling. Peltzer, Eisenstein, Cascella and coworkers (2020) simulated the reaction of $\ce{CH3MgCl}$ in THF by ab initio molecular dynamics with explicit solvent molecules: several Schlenk-equilibrium species in solution (especially chloride-bridged dinuclear magnesium species) can be the reactive species, and for most aldehydes and aliphatic ketones the reaction follows the polar nucleophilic pathway; only when the carbonyl compound is easily reduced (aromatic ketones such as fluorenone and benzophenone, whose **ketyls** are those of [6.5.17](/6.5.17#sec-17.3.2)) and the nucleophilic pathway is sterically hindered does the single-electron-transfer pathway become important.

### 27.3.3. Bis-Grignard Reagents and Dialkylmagnesium Compounds

A compound containing two C–MgX units in the molecule (an alkylene dimagnesium dihalide) is called a bis-**Grignard reagent**. When the two halogens are far apart (1,4- and 1,5-dihaloalkanes, 1,4-dibromobenzene), each end reacts with magnesium separately to give $\ce{XMg(CH2)_nMgX}$, which can be used to synthesize cyclic compounds (by reaction with diesters and diketones). When the two halogens are close together, elimination occurs:

- 1,2-dihaloalkanes give alkenes and $\ce{MgX2}$ (1,2-dibromoethane is therefore used as an "activator", [6.5.10](/6.5.10#sec-10.3.2));
- 1,3-dibromopropane gives cyclopropane by an intramolecular **SN2**-type coupling;
- o-dihalobenzenes (such as 1-bromo-2-fluorobenzene) react with magnesium, and the o-halophenylmagnesium formed loses MgXF to give **benzyne**; when the reaction is run in furan, the benzyne is trapped by furan in a **Diels–Alder reaction**, giving 1,4-dihydro-1,4-epoxynaphthalene (Wittig, 1955).

```smiles
Fc1ccccc1Br.c1ccoc1>>C1=CC2OC1c1ccccc21
```

Dialkylmagnesium compounds $\ce{R2Mg}$ can be obtained by driving the **Schlenk equilibrium** with dioxane, and historically were also obtained by displacing organomercury compounds with magnesium ($\ce{R2Hg + Mg -> R2Mg + Hg}$, no longer used because mercury is highly toxic); addition of conjugated dienes to activated magnesium gives "butadiene magnesium", an equivalent of a divalent diene dianion.

## 27.4. Organoboron Compounds

### 27.4.1. Classification and Bonding

Classified by the groups attached to boron:

| Structure | Name | English name |
|---|---|---|
| $\ce{BH3}$ ($\ce{B2H6}$), $\ce{R_nBH_{3-n}}$ | borane, alkylborane | borane, alkylborane |
| $\ce{R2BOH}$, $\ce{R2BOR'}$ | borinic acid (dialkylborinic acid) and its esters | borinic acid, borinic ester |
| $\ce{RB(OH)2}$, $\ce{RB(OR')2}$ | boronic acid and its esters (such as the pinacol ester RBpin) | boronic acid, boronic ester |
| $\ce{B(OH)3}$, $\ce{B(OR)3}$ | boric acid, trialkyl borate | boric acid, borate ester |
| $\ce{R4B-}$, $\ce{RB(OH)3-}$, $\ce{RBF3-}$ | four-coordinate borates (such as potassium trifluoroborates $\ce{RBF3K}$) | borate (ate complex) |

Polyhedral boranes ($\ce{B5H9}$, $\ce{B10H14}$ and the closed $\ce{B12H12^{2-}}$) are classified by skeleton as closo, nido and arachno, and their structures are explained by the multicenter bonding theory of Lipscomb (Nobel Prize in Chemistry, 1976) ([6.1.14](/6.1.14#sec-14.6.3)). In organic synthesis the three-coordinate boranes and the boronic esters are mainly used.

Bonding at boron has three characteristics:

- **Electronegativity**: B 2.04 < H 2.20 < C 2.55. The hydrogen of a B–H bond is hydridic (boranes are sources of hydride), and the carbon of a B–C bond carries a partial negative charge, but the polarity is much smaller than for C–Mg and C–Li, so organoboranes are fairly stable toward water, alcohols and even air (boronic esters) under neutral conditions.
- Three-coordinate boron is trigonal planar with an empty p orbital, and is a **Lewis acid** and **electrophile**; on accepting an electron pair it becomes a tetrahedral borate, in which four-coordinate boron is negatively charged and the groups on boron become electron-rich and able to migrate (Section 27.4.5), so borates are "nucleophilic". The interconversion between these two states is the core of organoboron chemistry.
- Bonds to O and F are very strong (**mean bond enthalpies** in $\mathrm{kJ\,mol^{-1}}$): B–F 613, B–O 536, B–Cl 456, B–Br 377, B–H 389, B–C 356. Boron is "oxophilic", so the thermodynamic driving force for oxidation of the C–B bond to a C–O bond by $\ce{H2O2}$ is large.

Diborane contains two B–H–B **three-center two-electron bonds** ([6.5.11](/6.5.11#sec-11.4.6)), and bridging and terminal hydrogens can be distinguished by **infrared spectroscopy**: the terminal B–H **stretching vibration** is at about $2500$–$2600\,\mathrm{cm^{-1}}$, and the vibrations of the bridging B–H–B bonds occur at lower frequency, about $1500$–$2100\,\mathrm{cm^{-1}}$.

### 27.4.2. Borane Reagents

$\ce{B2H6}$ is a toxic, flammable gas, and in the laboratory its **coordination complexes** with **Lewis bases** are used: $\ce{BH3*THF}$ (in THF solution) and $\ce{BH3*SMe2}$ (BMS, of better stability and solubility but with the odor of a sulfide). $\ce{B2H6}$ itself can be generated in situ from $\ce{BF3}$ and $\ce{NaBH4}$:

$$
\ce{4 BF3 + 3 NaBH4 -> 3 NaBF4 + 2 B2H6}.
$$

When bulky alkenes react with $\ce{BH3}$, **hydroboration** stops at the mono- or dialkylborane, giving more selective reagents:

| Reagent | Preparation | Use |
|---|---|---|
| Bis(1,2-dimethylpropyl)borane $\ce{Sia2BH}$ (disiamylborane) | 2 equiv 2-methylbut-2-ene + $\ce{BH3}$ (steric hindrance stops the reaction at the dialkylborane) | selective hydroboration of terminal alkenes and alkynes |
| (1,1,2-Trimethylpropyl)borane $\ce{ThxBH2}$ (thexylborane) | 2,3-dimethylbut-2-ene + $\ce{BH3}$ | the two B–H bonds can add to different alkenes, giving mixed trialkylboranes and, via cyclic boranes, cyclic ketones |
| 9-Borabicyclo[3.3.1]nonane (9-BBN) | cycloocta-1,5-diene + $\ce{BH3}$ | exists as a dimer, a crystalline solid fairly stable in air; the highest **regioselectivity**; alkyl donor in the **Suzuki coupling** |
| Diisopinocampheylborane $\ce{Ipc2BH}$, monoisopinocampheylborane $\ce{IpcBH2}$ | 2 or 1 equiv α-pinene + $\ce{BH3}$ | asymmetric hydroboration (Section 27.4.3) |
| Catecholborane, pinacolborane (HBpin) | diol + $\ce{BH3}$ | slow to add by themselves; used in metal-catalyzed hydroboration, giving boronic esters directly |

```smiles
CC=C(C)C>>CC(C)C(C)BC(C)C(C)C
C1=CCCC=CCC1>>C1CC2CCCC(C1)B2
```

(The structures above are $\ce{Sia2BH}$ and 9-BBN, in that order; $\ce{BH3}$ is omitted from the reactants.)

### 27.4.3. Selectivity of Hydroboration and Asymmetric Hydroboration

The concerted four-center mechanism of **hydroboration**, the anti-Markovnikov orientation, syn addition and retention of configuration on oxidation are described in [6.5.11](/6.5.11#sec-11.4.6). Bulky boranes improve the regioselectivity (data of Brown; the ratios are for boron adding to the carbons shown):

| Substrate | Position of boron | $\ce{BH3}$ | $\ce{Sia2BH}$ | 9-BBN |
|---|---|---|---|---|
| Hex-1-ene | C1 : C2 | 94 : 6 | 99 : 1 | 99.9 : 0.1 |
| Styrene | terminal : **benzylic position** | 80 : 20 | 98 : 2 | 98.5 : 1.5 |
| (Z)-4-Methylpent-2-ene | C2 : C3 | 57 : 43 | 97 : 3 | 99.8 : 0.2 |

The borane approaches the less hindered face of the alkene, so hydroboration also has good facial selectivity. One face of α-pinene is blocked by the gem-dimethyl bridge, so $\ce{BH3}$ adds to the other face, and the diisopinocampheylborane $\ce{Ipc2BH}$ formed is a chiral dialkylborane. $\ce{Ipc2BH}$ made from optically pure α-pinene (a natural product, both enantiomers readily available) gives, in hydroboration–oxidation of cis-disubstituted alkenes (such as (Z)-but-2-ene), optically active secondary alcohols, initially in about 87% ee (Brown and Zweifel, 1961) and above 98% ee with reagent purified by recrystallization. This was one of the first methods of highly enantioselective **asymmetric synthesis**. $\ce{Ipc2BH}$ works poorly with trans- and trisubstituted alkenes, for which the less hindered $\ce{IpcBH2}$ is used instead.

The modern method is metal-catalyzed asymmetric hydroboration: Rh(I)–BINAP catalyzes the addition of catecholborane to styrene (Hayashi, 1989), with boron adding to the benzylic position (the opposite **regioselectivity** from the uncatalyzed reaction, via a benzylic rhodium intermediate formed by Rh–H insertion), and oxidation gives 1-phenylethanol in high ee.

### 27.4.4. Boranes as Reducing Agents and Protonolysis

$\ce{BH3}$ is an electrophilic hydride reagent whose selectivity differs from that of $\ce{NaBH4}$ (a nucleophilic hydride): it rapidly reduces carboxylic acids (an acyloxyborane forms first, the carbonyl being activated by B), aldehydes, ketones and alkenes, and reacts slowly with esters, lactones, amides (more slowly), alkyl halides and nitro groups, so carboxylic acids can be reduced selectively to primary alcohols in the presence of esters ([6.5.18](/6.5.18#sec-18.3)). $\ce{NaBH4}$, in contrast, reduces aldehydes and ketones but not carboxylic acids ([6.5.17](/6.5.17#sec-17.1.1)).

On heating a trialkylborane in a carboxylic acid (such as propanoic acid), the C–B bond is protonolyzed to a C–H bond with retention of configuration. An alkenylborane obtained by **hydroboration** of an alkyne gives a cis-alkene on protonolysis, a catalyst-free cis reduction (complementary to Lindlar hydrogenation, [6.5.11](/6.5.11#sec-11.12.1)):

```smiles
CCC#CCC>>CC/C=C\CC
```

### 27.4.5. 1,2-Metallate Rearrangements: Carbonylation and Matteson Homologation

In the oxidation that follows **hydroboration** ([6.5.11](/6.5.11#sec-11.4.6)), $\ce{HOO-}$ adds to boron to form a borate, and an alkyl group migrates with its bonding electron pair from B to the adjacent O while $\ce{HO-}$ leaves. This is an example of a general reaction in organoboron chemistry:

**Definition 27.4.1 (1,2-Metallate Rearrangement)** The reaction in which, in a four-coordinate borate (or the "ate" complex of another metal), a group attached to the metal migrates with its bonding electron pair to an adjacent atom that carries a leaving group or is electron-deficient, with simultaneous departure of the leaving group (or neutralization of the electron-deficient center), is called a **1,2-metallate rearrangement**. The migrating group keeps its configuration at the migrating carbon; if the terminus of migration is an $\mathrm{sp^3}$ carbon bearing a leaving group, that carbon is inverted (the migrating group enters from the side opposite the leaving group).

Changing the terminus of migration gives a series of methods for forming C–C bonds from organoboron compounds.

Carbonylation: a trialkylborane combines with CO, the carbon lone pair of CO filling the empty p orbital of boron to give a borate-type adduct; alkyl groups then migrate in succession from B to the carbonyl carbon (Brown, 1967).

![Carbonylation of a trialkylborane (first migration): the lone pair on the CO carbon attacks the empty orbital of boron to give an "ate" complex; one ethyl group migrates with its bonding electrons from the negatively charged boron to the electron-deficient carbonyl carbon (1,2-metallate rearrangement, with retention at the migrating carbon), the π electrons of C=O moving toward oxygen, giving an acylborane](./plots/borane-carbonylation.py)

By controlling the conditions, an alkyl group can be made to migrate once, twice or three times, and oxidation then gives different products:

| Conditions | Number of migrations | Product after oxidation (or hydrolysis) |
|---|---|---|
| CO with $\ce{LiAlH(OMe)3}$ or $\ce{LiBH4}$ (reduces the acylborane and prevents further migration) | 1 | aldehyde RCHO (buffered $\ce{H2O2}$ oxidation), or primary alcohol $\ce{RCH2OH}$ (alkaline hydrolysis): one carbon is added |
| CO, water, about $100\,^\circ\mathrm{C}$ | 2 | ketone $\ce{R2C=O}$ |
| CO, ethylene glycol, about $150\,^\circ\mathrm{C}$ | 3 | tertiary alcohol $\ce{R3COH}$ |

Hydroboration of a diene with $\ce{ThxBH2}$ gives a cyclic borane first, and on carbonylation the two ring carbons migrate to the same carbonyl carbon, giving a cyclic ketone: for example, penta-1,4-diene gives cyclohexanone via a borinane. The less toxic cyanide with trifluoroacetic anhydride (Pelter) or dichloromethyl methyl ether (Brown) is now often used in place of CO to achieve the same migrations.

Matteson homologation:

**Definition 27.4.2 (Matteson Homologation)** The method in which the alkylboronic ester of a chiral diol (such as pinanediol) reacts with dichloromethyllithium at low temperature to form a borate, an alkyl group displaces one chlorine by 1,2-metallate rearrangement to give an α-chloroboronic ester with one more carbon, and the latter reacts with a Grignard reagent or another nucleophile and displaces the second chlorine by a second 1,2-metallate rearrangement, so that each round adds one carbon and creates one stereocenter of defined configuration, is called **Matteson homologation**. Homologation means the conversion of a compound into its homologue having more carbon atoms.

![Matteson homologation: dichloromethyllithium (made from $\ce{CH2Cl2}$ and LDA at $-100\,^\circ\mathrm{C}$) adds to the empty orbital of a boronic ester to form a borate; promoted by $\ce{ZnCl2}$, the propyl group migrates with its bonding electrons from boron to the $\ce{CHCl2}$ carbon while one chloride leaves from the back, giving an α-chloroboronic ester. The chiral diol actually used (such as pinanediol) determines which chlorine leaves and hence the configuration of the new stereocenter](./plots/matteson.py)

$\ce{ZnCl2}$ coordinates the departing chlorine, promotes the migration and improves the diastereoselectivity (often above 99:1). In the second step R′MgX adds to boron and R′ migrates to the α carbon, displacing the remaining chlorine (with inversion), to give the secondary alkylboronic ester $\ce{R'CH(R)B(OR)2}$, which can serve as the substrate of the next round; finally oxidation gives an alcohol, or the product is used in other transformations. Displacing the α-chlorine with $\ce{LiN(SiMe3)2}$ and removing the silyl groups gives α-aminoboronic acids; the boronic acid "warhead" of bortezomib, a drug against multiple myeloma, is synthesized in this way (Section 27.4.6). The lithiation–borylation method developed by Aggarwal uses chiral α-lithiated carbamates in place of dichloromethyllithium and can build several adjacent **stereocenters** in succession like an "assembly line" (2014).

### 27.4.6. Boronic Acids and Boronic Esters

Boric acid $\ce{B(OH)3}$ is not a protic acid but a **Lewis acid**: it accepts $\ce{HO-}$ from water to form tetrahedral $\ce{B(OH)4-}$ and releases $\ce{H+}$, with an apparent $\mathrm{p}K_{\mathrm{a}} = 9.27$ (CRC, as in [6.1.14](/6.1.14#sec-14.6.4) and [6.4.2](/6.4.2)); the $\mathrm{p}K_{\mathrm{a}}$ of phenylboronic acid is about 8.8.

$$
\ce{B(OH)3 + 2 H2O <=> B(OH)4- + H3O+}.
$$

Alkylboronic acids $\ce{RB(OH)2}$ are obtained from **Grignard reagents** or organolithium compounds with trimethyl borate followed by hydrolysis, or from aryl halides and bis(pinacolato)diboron ($\ce{B2pin2}$) by palladium catalysis (Miyaura borylation); C–H bonds of arenes can also be borylated directly with iridium catalysts (Hartwig, Miyaura, Ishiyama). Most are air-stable, low-toxicity, easily handled solids, and their palladium-catalyzed coupling with aryl halides (the Suzuki–Miyaura reaction) is the method of choice for constructing biaryls, used in [6.5.29](/6.5.29#sec-29.4.3); protonolysis of the C–B bond under basic conditions (protodeboronation) is the main side reaction of this type of reaction.

```smiles
Brc1ccc(C)cc1.COB(OC)OC>>Cc1ccc(cc1)B(O)O
```

Boronic acids form five- or six-membered cyclic boronic esters reversibly with 1,2- and 1,3-diols, with stronger binding in basic solution (four-coordinate borate). This leads to two biomedical applications: arylboronic acids carrying a fluorophore change their fluorescence on binding glucose and are used as glucose sensors, and boronic acids bind the sugar chains on the surface of glycoproteins. The empty p orbital of boron can also be attacked by a nucleophilic group of an enzyme active site (the hydroxyl of serine or threonine) to form a tetrahedral borate that mimics the transition state of hydrolysis, so boronic acids are "warheads" of covalent reversible enzyme inhibitors: bortezomib (marketed in 2003, inhibiting the threonine protease of the proteasome), the β-lactamase inhibitor vaborbactam (2017) and the antifungal tavaborole all contain boron.

![A boronic acid "warhead" inhibiting a serine (threonine) protease (R is the rest of the inhibitor): the hydroxyl oxygen of an active-site residue adds to the empty p orbital of the three-coordinate boron, and after loss of a proton boron becomes a negatively charged tetrahedral borate that mimics the tetrahedral intermediate of amide hydrolysis; the addition is reversible, so the inhibition is covalent and reversible](./plots/boronic-acid-inhibitor.py)

## 27.5. Organosilicon Compounds

### 27.5.1. Classification

| Class | Structure | Examples |
|---|---|---|
| Organosilanes | $\ce{R_nSiH_{4-n}}$ (containing Si–C bonds) | tetramethylsilane (TMS, the internal standard of NMR), triethylsilane $\ce{Et3SiH}$ |
| Halosilanes | $\ce{R_nSiX_{4-n}}$ | chlorotrimethylsilane TMSCl, dichlorodimethylsilane |
| Silanols | $\ce{R3SiOH}$ | trimethylsilanol |
| Silyl ethers and siloxanes | $\ce{R3Si-OR'}$, $\ce{R3Si-O-SiR3}$ | tert-butyldimethylsilyl ethers, polydimethylsiloxane (silicone oil, silicone rubber) |
| Silicate esters | $\ce{Si(OR)4}$ | tetraethyl orthosilicate (TEOS, tetraethoxysilane) |

Industrially, dichlorodimethylsilane, the raw material of silicones, is obtained by the direct reaction of chloromethane with silicon powder over copper (the Müller–Rochow process), and its hydrolytic polycondensation gives the silicone polymers. No natural product containing an Si–C bond has been found; silicon occurs in organisms as silicic acid and silica (diatoms, grasses) and, when attached to organic molecules, only through Si–O–C bonds. Arnold and coworkers (2016) achieved carbene insertion into Si–H bonds under **enzyme catalysis** with a cytochrome c engineered by directed evolution, the first formation of Si–C bonds by a biological system.

### 27.5.2. Features of Bonding

Silicon (**electronegativity** 1.90) is more electropositive than both carbon (2.55) and hydrogen (2.20) and has a large atomic radius (the Si–C bond length is $187\,\mathrm{pm}$, that of C–C $154\,\mathrm{pm}$). The following table compares **mean bond enthalpies** of carbon and silicon ($\mathrm{kJ\,mol^{-1}}$, usual values from inorganic textbooks):

| Bond | $\bar D$ | Bond | $\bar D$ | Difference $\bar D(\ce{Si-Y}) - \bar D(\ce{C-Y})$ |
|---|---|---|---|---|
| C–O | 358 | Si–O | 452 | +94 |
| C–F | 485 | Si–F | 565 | +80 |
| C–Cl | 327 | Si–Cl | 381 | +54 |
| C–N | 305 | Si–N | 355 | +50 |
| C–H | 411 | Si–H | 318 | −93 |
| C–C | 346 | Si–Si | 222 | −124 |

Several characteristics of organosilicon chemistry can be understood from this:

- Silicon is oxophilic and fluorophilic (Question 7). Si–O and Si–F bonds are much stronger than the corresponding carbon bonds: the large electronegativity difference between the two atoms gives the bond a large ionic component, and electrostatic attraction contributes extra bond energy; the lone pairs of O and F also delocalize into the σ* orbitals of Si–C (**negative hyperconjugation**, Definition 26.3.1 in [6.5.26](/6.5.26#def-26.3.1)), which shortens the Si–O bond and widens the Si–O–Si angle (about $140^\circ$–$150^\circ$ in siloxanes). The older attribution of such effects to 3d orbitals of Si (pπ–dπ bonding) is outdated, as in the cases of phosphorus and sulfur. Formation of Si–O and Si–F bonds drives the removal of silyl ethers, the Peterson olefination, the Brook rearrangement and other reactions.
- The hydrogen of an Si–H bond is hydridic: silanes such as $\ce{Et3SiH}$ transfer hydride to **carbocations** in the presence of acid (ionic hydrogenation) and also reduce phosphine oxides to phosphines ([6.5.26](/6.5.26#sec-26.5.1)).
- The Si–Si bond is weak, and silicon does not form large numbers of stable long chains as carbon does: silanes $\ce{Si_nH_{2n+2}}$ rapidly become unstable as the chain lengthens, and higher silanes ignite in air. Chains carrying hydrocarbon groups are much more stable, however: fully methylated linear oligosilanes have been synthesized with more than ten silicon atoms, and polysilanes $\ce{(SiR2)_n}$ can have chains of thousands of silicon atoms; they have σ conjugation along the Si–Si backbone and are used as photoresists and semiconductor materials.
- Silicon is large and can accept a fifth ligand, so a **nucleophile** can attack silicon from the back of the tetrahedron and complete substitution through a five-coordinate silicate intermediate (unlike **SN2** at carbon, five-coordinate silicon is a low-energy intermediate rather than a transition state). The Si–Cl bond of chlorotrimethylsilane is therefore much more reactive than a C–Cl bond and is decomposed rapidly by alcohols and water at room temperature.
- The σ electrons of the C–Si bond lie high in energy and are polarized toward carbon, and can stabilize a β carbocation by **hyperconjugation** (Section 27.5.4); the C–Si σ* orbital in turn stabilizes an α **carbanion** (Section 27.5.5).

### 27.5.3. Silyl Ether Protecting Groups

Alcohols and chlorosilanes rapidly give silyl ethers in the presence of a base (triethylamine, imidazole); silyl ethers are stable to bases, organometallic reagents and most oxidants and reductants, and can be removed under mild conditions with fluoride ion or acid, so they are the most commonly used **protecting groups** for hydroxyl groups ([6.5.16](/6.5.16#sec-16.5.3)).

**Definition 27.5.1 (Silyl Ether)** A compound $\ce{R3Si-OR'}$ in which the hydrogen of an alcohol hydroxyl group is replaced by a trialkylsilyl group is called a **silyl ether**.

$$
\ce{(CH3)3SiCl + CH3CH2OH ->[\ce{Et3N}] CH3CH2OSi(CH3)3 + Et3NH+Cl-}.
$$

| Silyl group | Abbreviation | Introduction | Relative stability: acid | Relative stability: base | Removal |
|---|---|---|---|---|---|
| Trimethylsilyl | TMS | TMSCl, $\ce{Et3N}$ | 1 | 1 | partly removed by $\ce{K2CO3}$/MeOH, dilute acetic acid or even column chromatography |
| Triethylsilyl | TES | TESCl, imidazole | 64 | 10–100 | dilute acid, TBAF |
| tert-Butyldimethylsilyl | TBS (TBDMS) | TBSCl, imidazole, DMF (Corey, 1972); for hindered cases TBSOTf, 2,6-lutidine | $2\times10^4$ | $2\times10^4$ | TBAF (THF), HF·pyridine, AcOH/$\ce{H2O}$ |
| Triisopropylsilyl | TIPS | TIPSCl or TIPSOTf | $7\times10^5$ | $1\times10^5$ | TBAF (slower), HF |
| tert-Butyldiphenylsilyl | TBDPS | TBDPSCl, imidazole | $5\times10^6$ | $2\times10^4$ | TBAF, HF |

(Relative stability is taken as 1 for the rate of hydrolysis of TMS ethers; data from Greene's handbook of protecting groups.)

Stability is determined mainly by steric hindrance at silicon: the more crowded the silicon, the harder it is for a **nucleophile** (water, $\ce{HO-}$) to approach silicon from the back. These differences allow selective protection and removal in polyhydroxy compounds: TBSCl protects primary alcohols preferentially; TES or TMS can be removed selectively with dilute acid in the presence of TBS ethers; TBDPS is more acid-resistant than TBS, and TIPS more base-resistant than TBS. The most common reagent for removal is tetrabutylammonium fluoride (TBAF):

![Removal of a tert-butyldimethylsilyl ether by TBAF: fluoride attacks silicon, which accepts a fifth ligand to form a trigonal-bipyramidal five-coordinate silicate, and the Si–O bond then breaks, with the benzyl oxide leaving; the Si–F bond (about 565 kJ/mol) is stronger than the Si–O bond (about 452 kJ/mol), which makes the removal practically irreversible](./plots/silyl-ether-cleavage.py)

Silyl groups also protect other acidic hydrogens: the C–H of a terminal alkyne is protected with TMS ($n$-BuLi, then TMSCl; removal with $\ce{K2CO3}$/MeOH or TBAF), and carboxylic acids can be transiently converted to trimethylsilyl esters. Trapping an **enolate** with TMSCl and triethylamine gives a **silyl enol ether**, a "frozen" enol (the regiochemistry of the kinetic or thermodynamic enol is preserved, [6.5.21](/6.5.21#sec-21.3.2)), which adds as a nucleophile to aldehydes under the action of **Lewis acids** (the **Mukaiyama aldol reaction**, [6.5.22](/6.5.22#sec-22.6.2)). A summary of silyl ether and other protecting groups is given in [6.5.20](/6.5.20#sec-20.8.3).

### 27.5.4. The β-Silicon Effect and Allylsilanes

**Definition 27.5.2 (β-Silicon Effect)** The marked stabilization by a silicon atom of positive charge (a carbocation or a cationic transition state) on the carbon atom β to silicon is called the **β-silicon effect**. It arises from **hyperconjugation** between the C–Si σ bond and the empty p orbital of the carbocation, and requires the C–Si bond to be parallel to the empty p orbital (that is, **antiperiplanar** to the leaving group).

The σ orbital of the C–Si bond is high in energy (Si is electropositive) and has its larger coefficient on carbon, making it a very good donor, so a β-silyl **carbocation** is much more stable than the corresponding β-hydrogen carbocation: the calculated stabilization energy in the gas phase is about $160\,\mathrm{kJ\,mol^{-1}}$; in **solvolysis**, trans-2-(trimethylsilyl)cyclohexyl trifluoroacetate, in which Si and the **leaving group** are **antiperiplanar**, reacts about $10^{12}$ times faster than cyclohexyl trifluoroacetate, whereas the cis isomer, in which Si and the leaving group are at about $60^\circ$, is only about $10^4$ times faster (Lambert). By contrast, α-silyl groups stabilize carbocations only slightly (the inductive electron donation due to the electropositivity of silicon is offset by the longer C–Si bond and poor π overlap).

The β-silicon effect determines how allylsilanes and vinylsilanes react: when an **electrophile** attacks an allylsilane, it adds to the terminal carbon farther from silicon (the γ carbon), placing the positive charge β to silicon; a **nucleophile** (halide, solvent) then attacks silicon, and the electron pair of the C–Si bond forms a new C=C bond. The overall result is that the electrophile replaces silicon and the double bond undergoes an "allylic shift" (SE2′).

**Definition 27.5.3 (Hosomi–Sakurai Reaction)** The reaction in which an allylsilane reacts with an aldehyde, ketone, acetal or α,β-unsaturated ketone under the action of a Lewis acid ($\ce{TiCl4}$, $\ce{BF3*OEt2}$), introducing an allyl group at the carbonyl carbon (or β carbon) with a shift of the double bond to give a homoallylic alcohol (or a δ,ε-unsaturated ketone), is called the **Hosomi–Sakurai reaction** (1976).

![Hosomi–Sakurai allylation: $\ce{TiCl4}$ coordinates to the carbonyl oxygen of benzaldehyde; the terminal carbon of allyltrimethylsilane farther from silicon attacks the activated carbonyl carbon; the carbocation formed is β to silicon and is stabilized by hyperconjugation with the C–Si bond parallel to the empty p orbital; chloride attacks silicon, the electrons of the C–Si bond form the new C=C bond, and hydrolysis gives the homoallylic alcohol](./plots/sakurai.py)

Allylsilanes are neutral, stable compounds that can be purified by column chromatography, and they hardly react with aldehydes without activation by a **Lewis acid** or fluoride ion, which gives them much better functional-group compatibility than allyl **Grignard reagents**. With crotylsilanes and $\ce{TiCl4}$, whether the double bond is E or Z the product is mainly the syn homoallylic alcohol (an open, antiperiplanar transition state), with good diastereoselectivity. With α,β-unsaturated ketones the reaction occurs by **1,4-addition** (conjugate allylation). Activation by fluoride ion (forming a five-coordinate silicate) can also effect allyl transfer. In the reaction of vinylsilanes with electrophiles, the electrophile replaces silicon (ipso substitution) with retention of the double-bond configuration, which is also a result of the β-silicon effect.

### 27.5.5. The Peterson Olefination

**Definition 27.5.4 (Peterson Olefination)** The reaction in which an α-silyl carbanion (such as $\ce{Me3SiCH2Li}$ or $\ce{Me3SiCH2MgCl}$) adds to an aldehyde or ketone to give a β-hydroxysilane, which eliminates $\ce{R3SiOH}$ to give an alkene, is called the **Peterson olefination** (1968) and can be regarded as the silicon analogue of the **Wittig reaction**.

Silicon stabilizes an α-**carbanion** (trimethylsilylmethyllithium is made from chloromethyltrimethylsilane and lithium) because of the high polarizability of silicon and **negative hyperconjugation** of the carbanion lone pair (the σ electrons of the C–M bond) into the Si–C σ* orbital; the explanation by "pπ–dπ bonding of 3d orbitals" is outdated. The β-oxidosilane formed in the addition can be isolated as the β-hydroxysilane if the counterion is Li or Mg (strong O–M bond); if it is K or Na, the oxide immediately attacks silicon and eliminates.

![The Peterson olefination (basic conditions): the α-silyl carbanion adds to the carbonyl carbon, and the oxide formed attacks silicon intramolecularly; through a four-membered ring containing five-coordinate silicon, the C–Si and C–O bonds break simultaneously on the same side (syn elimination), giving the alkene and a silanolate](./plots/peterson.py)

A feature of the Peterson olefination is that the stereochemistry of elimination can be chosen:

- Basic conditions (KH, NaH, or $t$-BuOK): the oxide bonds to silicon and syn elimination occurs through a four-membered ring (similar to the decomposition of the oxaphosphetane in the **Wittig reaction**);
- Acidic conditions ($\ce{H2SO4}$, $\ce{BF3*OEt2}$): the hydroxyl group is protonated and leaves as water, and the silyl group leaves **antiperiplanar** to it (like **E2**, with the β-silicon effect stabilizing the cationic transition state), an anti elimination.

The same diastereomer of a β-hydroxysilane therefore gives an alkene of one geometry with base and the other with acid (Hudrlik and Peterson, 1975; Question 5). The byproduct hexamethyldisiloxane has a low **boiling point** and is easily removed, which is more convenient than the triphenylphosphine oxide of the Wittig reaction. The Peterson olefination is best suited to preparing terminal alkenes and methylene compounds, which are hard to control in the Wittig reaction.

![The two eliminations of the same diastereomer of (2S,3R)-3-(trimethylsilyl)butan-2-ol. Top (acid): the protonated hydroxyl group is antiperiplanar to the C–Si bond, water attacks silicon, the electrons of the C–Si bond form the C=C bond and water leaves (an anti elimination like E2, the β-silicon effect stabilizing the transition state), giving (E)-but-2-ene; bottom (KH): the oxide attacks silicon and syn elimination through a four-membered ring gives (Z)-but-2-ene](./plots/peterson-acid.py)

## 27.6. Organofluorine Compounds

### 27.6.1. Properties

Fluorine is the element of highest **electronegativity** (3.98), with a small atomic radius (**van der Waals radius** $147\,\mathrm{pm}$, close to the $120\,\mathrm{pm}$ of H and the $152\,\mathrm{pm}$ of O) and very low polarizability. The C–F bond therefore has several unusual features:

- The strongest single bond to carbon: the C–F bond length is $135\,\mathrm{pm}$ and the **mean bond enthalpy** about $485\,\mathrm{kJ\,mol^{-1}}$, and the more fluorines on the same carbon, the stronger the C–F bond (the **bond dissociation energy** of $\ce{CH3-F}$ is about $460$ and of $\ce{CF3-F}$ about $545\,\mathrm{kJ\,mol^{-1}}$). This mutual strengthening of geminal fluorines (the α-fluorine effect) arises from delocalization of the lone pair of one fluorine into the σ* orbital of another C–F bond, for the same reason as the **anomeric effect**; geminal fluorines also make other bonds on the same carbon, such as C–Cl, more stable. Thus $\ce{CCl4}$ and $\ce{CHCl3}$ undergo C–Cl cleavage (chain transfer) in radical polymerization and cannot be used as solvents for radical reactions, whereas fluorinated solvents such as $\ce{CFCl2CF2Cl}$ can.
- Electronic effects: a strong electron-withdrawing **inductive effect**, together with conjugation of the fluorine lone pairs with π systems (an electron-donating **conjugation effect**). Because of good 2p–2p overlap, the conjugative donation of fluorine is the strongest among the halogens, so the rate of para electrophilic substitution of fluorobenzene is similar to that of benzene ([6.5.14](/6.5.14#sec-14.3)).
- Conformation: 1,2-difluoroethane prefers the gauche conformation (the **gauche effect**, [6.5.4](/6.5.4#sec-4.2.4)), because the C–H σ orbital delocalizes into the anti C–F σ* orbital.
- Perfluorinated compounds are both hydrophobic and oleophobic: the C–F bond is highly polar, but the fluorine electron cloud at the molecular surface is tight and of low polarizability, so intermolecular **dispersion forces** are very weak, and perfluoroalkanes are immiscible with both hydrocarbons and water (the "fluorous phase"); polytetrafluoroethylene has an extremely low surface energy and is extremely chemically inert. The same stability makes per- and polyfluoroalkyl substances (PFAS, such as perfluorooctanoic acid) almost nondegradable in the environment, and they have become persistent pollutants.

### 27.6.2. The Role of Fluorine in Drugs

About one fifth to one quarter of current small-molecule drugs contain fluorine, and the proportion is higher among recently approved drugs; about half of the new pesticides registered in the past two decades contain fluorine. The main roles of fluorine are:

- Blocking metabolic sites: drugs are often oxidized (C–H → C–OH) and inactivated by cytochrome P450 of the liver at an aromatic ring or **benzylic position**; replacing the H at that position by F (a C–F bond cannot be oxidized in this way, and F is similar in size to H and does not change binding to the target) improves metabolic stability and prolongs the half-life.
- Tuning acidity and basicity: the **inductive effect** of fluorine lowers the basicity of nearby amines. Each fluorine introduced at the β position lowers the $\mathrm{p}K_{\mathrm{a}}$ of the ammonium ion by about 1.7: ethylammonium 10.7 (water, CRC), 2-fluoroethylammonium about 9.0, 2,2-difluoroethylammonium about 7.3, 2,2,2-trifluoroethylammonium about 5.7. Lower basicity gives the drug more of the neutral form at physiological pH, which crosses cell membranes more easily and also reduces some undesired binding.
- Raising lipophilicity: F and $\ce{CF3}$ on an aromatic ring increase the lipophilicity ($\log P$) of a molecule and improve absorption and passage across the blood–brain barrier (as in fluoxetine, which contains $\ce{CF3}$).
- As a "mechanism-based trap": 5-fluorouracil is converted in the body into 5-fluorodeoxyuridylate. The cysteine of thymidylate synthase attacks its C6 and methylenetetrahydrofolate adds to C5 as usual, but the H on C5 that would leave as a proton in the normal reaction has been replaced by F, and $\ce{F+}$ cannot leave, so the elimination cannot proceed; the enzyme is covalently "stuck" and DNA synthesis is blocked (suicide inhibition).

In addition, fluorodeoxyglucose (FDG) labeled with $^{18}\mathrm{F}$ (half-life about 110 min) is the most common tracer in positron emission tomography; $^{19}\mathrm{F}$ has a natural abundance of 100%, spin 1/2 and high sensitivity, and organisms have almost no background, so fluorinated probes can be used to study the conformation and ligand binding of proteins by $^{19}\mathrm{F}$ NMR ([6.4.12](/6.4.12)).

### 27.6.3. Nucleophilic Fluorination

Fluoride ion is strongly solvated by **hydrogen bonding** in **protic solvents** and has almost no **nucleophilicity**; the desolvated "naked" fluoride ion is, on the other hand, a very strong base. The key to nucleophilic fluorination is therefore to use a fluoride source that is well soluble and weakly solvated in **polar aprotic solvents**, and to suppress elimination:

- Inorganic fluorides: KF with 18-crown-6, CsF, or spray-dried KF in DMSO, DMF or sulfolane, for **SN2** or **nucleophilic aromatic substitution** (the Halex reaction: electron-poor aryl chlorides → aryl fluorides, the main industrial method for preparing fluoroarenes).
- Tetraalkylammonium fluorides: TBAF is highly soluble, but hydrated TBAF is weakly nucleophilic and anhydrous TBAF is strongly basic and unstable (it undergoes **Hofmann elimination**).
- From diazonium salts: thermal decomposition of aryldiazonium tetrafluoroborates gives fluoroarenes through aryl cations (the **Balz–Schiemann reaction**, [6.5.24](/6.5.24#sec-24.4.3)).
- Deoxyfluorination: diethylaminosulfur trifluoride (DAST) and the more stable Deoxo-Fluor convert alcohols into alkyl fluorides (by SN2, with inversion) and aldehydes and ketones into geminal difluorides; HF·pyridine (Olah's reagent) is used for epoxide opening and additions.
- Trifluoromethylation: trifluoromethyltrimethylsilane ($\ce{CF3SiMe3}$, the Ruppert–Prakash reagent), initiated by a catalytic amount of $\ce{F-}$, forms a five-coordinate silicate and transfers $\ce{CF3-}$ to aldehydes and ketones to give silyl ethers of trifluoromethyl alcohols, another application of the fluorophilicity of silicon.

![Trifluoromethylation of benzaldehyde by the Ruppert–Prakash reagent (TMS is trimethylsilyl): a catalytic amount of fluoride adds to silicon to form a five-coordinate silicate, weakening the Si–CF₃ bond, and $\ce{CF3}$ is transferred with its electron pair to the carbonyl carbon, the electrons of C=O moving onto oxygen; the alkoxide formed attacks the silicon of another molecule of $\ce{TMSCF3}$, and the new silicate passes $\ce{CF3}$ to the next molecule of aldehyde, the alkoxide acting as chain carrier; the product is the TMS ether of the trifluoromethyl alcohol](./plots/ruppert-prakash.py)

![Deoxyfluorination of (S)-octan-2-ol by DAST (hexyl written as C₆H₁₃): the alcohol oxygen attacks sulfur and displaces one fluoride, and loss of HF gives an alkoxyaminosulfur difluoride, so that OH becomes a good leaving group; fluoride attacks the alcohol carbon from the back (SN2) to give (R)-2-fluorooctane with inverted configuration, and $\ce{Et2N-S(=O)F}$ leaves. Substrates that readily form carbocations rearrange or eliminate](./plots/deoxyfluorination.py)

### 27.6.4. Electrophilic Fluorination

$\ce{F2}$ itself is the strongest electrophilic fluorinating agent, but it reacts violently and with poor selectivity and can be used only diluted and in special apparatus. In the laboratory reagents containing an N–F bond are used, which are stable, weighable solids:

- N-Fluorobenzenesulfonimide (NFSI, $\ce{(PhSO2)2N-F}$), a neutral reagent of moderate fluorinating power;
- Selectfluor (1-(chloromethyl)-4-fluoro-1,4-diazoniabicyclo[2.2.2]octane bis(tetrafluoroborate), F-TEDA-$\ce{BF4}$), in which N is positively charged, of fairly strong fluorinating power;
- N-Fluoropyridinium salts (Umemoto), in which substituents on the pyridine ring can tune the fluorinating power over a wide range, strongest with electron-withdrawing groups such as 2,6-dichloro on the ring.

In general, the more electron-poor the nitrogen attached to F (positively charged, bearing electron-withdrawing groups), the stronger the fluorinating power of the N–F reagent. They react with **enolates**, **silyl enol ethers**, β-dicarbonyl compounds and electron-rich arenes to introduce a C–F bond; in the presence of chiral catalysts (chiral amines, transition-metal **coordination compounds**) asymmetric fluorination can be achieved. Whether the mechanism is direct fluorine transfer of the **SN2** type or **single electron transfer** varies with the substrate and remains debated.

```smiles
CCOC(=O)C1CCCCC1=O>>CCOC(=O)C1(F)CCCCC1=O
```

(The above is the α-fluorination of ethyl 2-oxocyclohexane-1-carboxylate with Selectfluor.) Silver- and palladium-mediated aryl fluorination (Ritter and coworkers) and fluorination by **photoredox catalysis**, developed in recent years, have made "late-stage fluorination", the introduction of fluorine into a complex drug molecule in the last step of a synthesis, possible.

![Electrophilic fluorination of a β-keto ester by Selectfluor (the dication is drawn, $\ce{BF4-}$ omitted): the enol is the nucleophile, a lone pair on the O–H oxygen pushes the electrons of the C=C bond to attack fluorine, and the weak N–F bond breaks toward the positively charged nitrogen (fluorine transfer of the SN2 type; for some substrates a single-electron pathway competes), the carbonyl oxygen loses its proton, giving the α-fluoro keto ester](./plots/electrophilic-fluorination.py)

## 27.7. Organic Hypervalent Iodine Compounds

### 27.7.1. Hypervalence and the Three-Center Four-Electron Bond

The term "hypervalent" was proposed by Musher (1969): when certain elements of Groups 15–18 of the periodic table form compounds, the number of valence electrons around the **central atom** exceeds that allowed by the **octet rule**, and such molecules are called hypervalent molecules (**hypervalent molecules**, [6.1.3](/6.1.3#sec-3.4.5)), for example $\ce{PCl5}$, $\ce{SF6}$, $\ce{IF7}$. Iodine has the largest atoms, the lowest **electronegativity** (2.66) and the highest polarizability of the halogens, and forms hypervalent compounds most readily.

**Definition 27.7.1 (Hypervalent Iodine Compound)** An organoiodine compound in which the number of valence electrons around the iodine atom exceeds 8 is called a **hypervalent iodine compound**. In the IUPAC λ notation, trivalent iodine compounds $\ce{ArIL2}$ (10 valence electrons) are called $\lambda^3$-iodanes and pentavalent iodine compounds $\ce{ArIL4}$ (12 valence electrons) are called $\lambda^5$-iodanes (periodinanes).

Commonly used hypervalent iodine reagents:

| Reagent | Structure | Oxidation state | Use |
|---|---|---|---|
| (Dichloroiodo)benzene | $\ce{PhICl2}$ | I(III) | chlorination |
| (Diacetoxyiodo)benzene (PIDA) | $\ce{PhI(OAc)2}$ | I(III) | oxidation, oxidative dearomatization of phenols |
| [Bis(trifluoroacetoxy)iodo]benzene (PIFA) | $\ce{PhI(OCOCF3)2}$ | I(III) | stronger oxidant, **Hofmann rearrangement** ([6.5.20](/6.5.20#sec-20.2)) |
| Diaryliodonium salts | $\ce{Ar2I+X-}$ | I(III) | arylation |
| 2-Iodoxybenzoic acid (IBX) | cyclic $\ce{ArIO2}$ | I(V) | oxidation of alcohols (in DMSO) |
| Dess–Martin reagent (DMP) | triacetoxy derivative of IBX | I(V) | oxidation of alcohols |

The bonding can be seen in $\ce{PhICl2}$. It is a distorted T-shaped molecule: the two Cl atoms occupy the two axial vertices of a (pseudo) trigonal bipyramid, the phenyl group and the two lone pairs of iodine lie in the equatorial plane, and the Cl–I–Cl angle is close to $180^\circ$. Iodine combines one 5p orbital (no 5d orbital is needed) with the p orbitals of the two Cl atoms into three molecular orbitals, a **bonding orbital**, a nonbonding orbital and an **antibonding orbital**; four electrons occupy the first two, forming one Cl–I–Cl **three-center four-electron bond**. The nonbonding orbital is the **highest occupied molecular orbital** of the molecule, has a node at the central iodine atom, and concentrates electron density on the two terminal ligands, so iodine carries a partial positive charge and the two ligands partial negative charges. Such a three-center bond is longer, weaker and more polarized than an ordinary covalent bond: the ligands leave easily and iodine is electrophilic. The C–I bond and the Cl–I–Cl bond are mutually perpendicular, which is the general T-shaped structure of trivalent iodine reagents.

### 27.7.2. Synthesis and General Reactivity

Hypervalent iodine reagents are obtained by oxidation of iodoarenes: iodobenzene and $\ce{Cl2}$ give $\ce{PhICl2}$, and with peracetic acid it gives PIDA; 2-iodobenzoic acid oxidized with potassium peroxymonosulfate (Oxone) in water gives IBX (Frigerio and Santagostino, 1999), and acetylation of IBX with acetic anhydride catalyzed by TsOH gives DMP (Ireland and Liu, 1993).

The reactions of hypervalent iodine reagents mostly consist of two basic steps: (1) ligand exchange, in which a **nucleophile** (alcohol, carboxylic acid, enol) replaces one ligand (acetate) on iodine, an associative step; (2) **reductive elimination**, in which iodine leaves with an electron pair, being reduced from I(III) to I(I) (ArI) or from I(V) to I(III), while linking the ligand to the substrate or oxidizing the substrate. Iodobenzene is an excellent **leaving group** (about $10^6$ times better than triflate, called a "hypernucleofuge" by Ochiai), which accounts for the strong oxidizing power and mild conditions of hypervalent iodine reagents. Their oxidations are highly selective and of low toxicity, and they can replace the classical oxidants containing chromium, manganese, lead, mercury and thallium.

### 27.7.3. IBX and the Dess–Martin Oxidation

**Definition 27.7.2 (Dess–Martin Oxidation)** The reaction that oxidizes primary alcohols to aldehydes and secondary alcohols to ketones under neutral conditions at room temperature in dichloromethane with the Dess–Martin reagent (1,1,1-triacetoxy-1,1-dihydro-1,2-benziodoxol-3(1H)-one, DMP) is called the **Dess–Martin oxidation** (Dess and Martin, 1983).

![The Dess–Martin oxidation: propan-2-ol first exchanges one acetate on iodine(V) of DMP (releasing acetic acid) to give an alkoxyperiodinane; acetate removes the hydrogen on the alcohol carbon, the electrons of the C–H bond form the C=O bond and those of the I–O bond move to iodine, releasing acetone, and iodine is reduced from I(V) to I(III)](./plots/dess-martin.py)

The advantages of DMP are: complete in minutes to hours at room temperature; neutral (adding $\ce{NaHCO3}$ or pyridine neutralizes the acetic acid formed and protects acid-sensitive groups); no overoxidation, primary alcohols stopping at the aldehyde; compatible with sulfides, alkenes and N-**protecting groups** of amines; an α **stereocenter** is essentially not racemized, which suits oxidation of N-protected amino alcohols to amino aldehydes. A little water accelerates the reaction (partly hydrolyzed DMP is more reactive, Meyer and Schreiber, 1994). The drawbacks are that the reagent is rather expensive and that its precursor IBX can explode on impact or heating (above about $200\,^\circ\mathrm{C}$), so care is needed on a large scale (commercial "stabilized IBX" is mixed with benzoic acid and isophthalic acid).

IBX itself is insoluble in most organic solvents and can be used in DMSO or as a suspension in hot ethyl acetate, oxidizing alcohols to aldehydes and ketones in the same way; it can also oxidize vicinal diols to diketones without cleaving the C–C bond (unlike periodic acid, [6.5.10](/6.5.10#sec-10.7)). The mechanism of IBX is similar to that of DMP; after ligand exchange, the ligand on iodine must first rotate into a suitable position ("hypervalent twist", Goddard's calculations, 2005) before elimination. The **Swern oxidation** ([6.5.26](/6.5.26#sec-26.9.2)), DMP and TEMPO-catalyzed oxidations ([6.5.10](/6.5.10#sec-10.6.2)) are the three main methods for oxidizing alcohols to aldehydes and ketones in modern synthesis: Swern is cheap and suited to scale-up but needs low temperature and smells, DMP is the simplest to operate and the mildest, and the TEMPO-catalyzed method, with sodium hypochlorite or air as terminal oxidant, is the "greenest".

### 27.7.4. Other Applications and Research Frontiers

- Oxidative dearomatization of phenols: after oxygen ligand exchange between PIDA or PIFA and a phenol, iodine leaves as an excellent **leaving group** to give a phenoxenium ion (or does so in a concerted way), which is captured by an alcohol, a carboxylic acid or an intramolecular nucleophile to give dearomatized products such as quinone monoketals (**acetals**) and spirolactones, commonly used in total syntheses of natural products. With a chiral iodoarene as catalyst (generating I(III) in situ with mCPBA as terminal oxidant), catalytic asymmetric dearomative spirolactonization can be achieved (Kita, 2008).
- Diaryliodonium salts: prepared in one pot from iodoarenes, arenes, mCPBA and TfOH (Olofsson, 2007), they are "equivalents of aryl cations" and can transfer an aryl group to O, N and C **nucleophiles** without metals or with copper catalysis (the leaving group being ArI). Vinyliodonium salts effect the asymmetric α-vinylation of aldehydes under the cooperative catalysis of copper and a chiral amine (MacMillan, 2012).
- Others: Togni reagents (cyclic $\ce{CF3}$–I(III) compounds) are electrophilic trifluoromethylating reagents (Section 27.6); hypervalent iodine reagents are also used in difunctionalization of alkenes, C–H amination and oxidative coupling. "Catalytic hypervalent iodine chemistry", with an iodoarene as catalyst and a peracid or electrochemistry as terminal oxidant, which no longer produces stoichiometric iodobenzene, is the current direction of development.

![Oxidative dearomatization of p-cresol by PIDA (in methanol): the phenol first exchanges one acetate on iodine(III) (releasing acetic acid) to give an aryloxy-λ³-iodane; methanol attacks the para carbon, electron movement in the ring turns the C–O bond into C=O, and the O–I bond breaks, iodine taking the electron pair (I(III) reduced to iodobenzene, the excellent leaving group) and releasing acetate; methanol loses a proton, giving 4-methoxy-4-methylcyclohexa-2,5-dien-1-one](./plots/phenol-dearomatization.py)

## Summary

- The polarity of C–M bonds in main-group organometallic compounds increases with the electropositivity of the metal (Section 27.1): the carbon of Li and Mg compounds is a strong nucleophile and a strong base; the carbon of B and Si compounds is transferred only through "ate" **coordination complexes** or transmetalation.
- Organolithium compounds:

| Topic | Key points |
|---|---|
| Preparation | direct synthesis; lithium–metal exchange (**transmetalation**; retention of configuration); lithium–halogen exchange (Definition 27.2.1: equilibrium favors the $\mathrm{sp^2}$ **carbanion**, extremely fast, 2 equiv of $t$-BuLi); metalation |
| Structure | aggregates (MeLi tetramer, $\ce{Li4C4}$ cubane skeleton, 4c–2e bonds or ionic cluster); the degree of aggregation falls as the donor power of the solvent increases (TMEDA, THF) |
| Stability | attack THF (α-deprotonation, then retro-[3+2]); store as hydrocarbon solutions |
| Directed ortho metalation | Definition 27.2.2: Li coordinates to the DMG, ortho selectivity complementary to **SEAr**; o-fluorophenyllithium gives **benzyne**; anionic **Fries rearrangement** |
| Addition | initiate anionic (living) polymerization of dienes; 2-alkylation of pyridine; ketones from nitriles; 1,2-addition to α,β-unsaturated ketones; ketones from carboxylic acids (2 equiv) |

- **Grignard reagents**: formed on the magnesium surface by **single electron transfer** and radicals (**radical clock**, racemization of chiral cyclopropyl halides); Rieke magnesium and halogen–magnesium exchange with $i$-PrMgCl·LiCl; four- and five-coordinate magnesium coordinated by ether, **Schlenk equilibrium**; addition mainly by the polar mechanism, with single electron transfer for easily reduced aromatic ketones; bis-Grignard reagents and o-dihalobenzenes give benzyne.
- Organoboron compounds: empty p orbital (**Lewis acid**) ⇌ four-coordinate borate (can migrate); B–O is very strong. $\ce{Sia2BH}$, $\ce{ThxBH2}$ and 9-BBN improve the **regioselectivity** of **hydroboration**, and $\ce{Ipc2BH}$ achieves asymmetric hydroboration; $\ce{BH3}$ reduces carboxylic acids selectively; protonolysis gives cis-alkenes; the 1,2-metallate rearrangement (Definition 27.4.1) unifies oxidation, carbonylation (1, 2 or 3 migrations giving aldehydes, ketones or tertiary alcohols) and Matteson homologation (Definition 27.4.2); boric acid is a Lewis acid ($\mathrm{p}K_{\mathrm{a}}$ 9.27), forms esters with diols, and boronic acids are substrates of the **Suzuki coupling** and covalent reversible enzyme inhibitors.
- Organosilicon compounds: Si–O and Si–F are strong (oxophilicity, fluorophilicity), Si–H is hydridic, and Si can be five-coordinate; the stability of silyl ethers (Definition 27.5.1) is determined by steric hindrance (TMS < TES < TBS < TIPS, TBDPS), and they are removed with $\ce{F-}$ or acid; the β-silicon effect (Definition 27.5.2) requires C–Si to be parallel to the empty p orbital and determines the regiochemistry of the Hosomi–Sakurai reaction of allylsilanes (Definition 27.5.3); the Peterson olefination (Definition 27.5.4) eliminates syn under basic and anti under acidic conditions.
- Organofluorine compounds: C–F is the strongest single bond to carbon and geminal fluorines strengthen each other; fluorine blocks metabolic sites, lowers the $\mathrm{p}K_{\mathrm{a}}$ of neighboring amines (about 1.7 per β-F) and raises lipophilicity, and 5-FU is a mechanism-based trap; nucleophilic fluorination (KF/crown ether, TBAF, Halex, DAST, $\ce{CF3SiMe3}$) and electrophilic fluorination (NFSI, Selectfluor, N-fluoropyridinium salts).
- Hypervalent iodine (Definition 27.7.1): T-shaped I(III) with a **three-center four-electron bond**, iodine electrophilic and ArI a hypernucleofuge (a very good **leaving group**); reaction = ligand exchange + **reductive elimination**; IBX and the Dess–Martin oxidation (Definition 27.7.2) oxidize alcohols to aldehydes and ketones under neutral conditions at room temperature; PIDA/PIFA dearomatize, and diaryliodonium salts arylate.

## Questions

1. When an alkyllithium initiates the polymerization of isoprene, in which ways can the monomer be attached to the chain? Draw the structural unit of each. Why does $n$-BuLi in a hydrocarbon solvent give mainly cis-1,4-polyisoprene, whereas in THF the 3,4-structure increases markedly?

   **Answer** Isoprene is $\ce{CH2=C(CH3)-CH=CH2}$ (C1–C4). Four structural units are possible: 1,4-addition, in which both double bonds take part and the main chain is $\ce{-CH2-C(CH3)=CH-CH2-}$, the double bond being cis (Z) or trans (E); 1,2-addition, using only C1=C2, with main chain $\ce{-CH2-C(CH3)(CH=CH2)-}$ and a vinyl side chain; and 3,4-addition, using only C3=C4, with main chain $\ce{-CH2-CH(C(CH3)=CH2)-}$ and an isopropenyl side chain. In hydrocarbon solvents the C–Li bond at the chain end is a tight, aggregated, covalent-like **ion pair**, lithium coordinates to both double bonds of the incoming monomer, and the monomer enters in the s-cis conformation to give the cis-1,4 unit (above about 90%), similar to the cis-1,4 structure of natural rubber. In THF lithium is solvated and the chain end is a separated ion pair; the negative charge is delocalized over C1 and C3 of the allyl anion, the monomer can add through the C3 ("inner") end of the allyl, the proportions of 3,4- and 1,2-structures increase greatly, and the cis selectivity disappears.

2. To prepare 4-chlorophenyllithium from 1-bromo-4-chlorobenzene, should lithium metal, $n$-BuLi or $t$-BuLi be used? Why are 2 equivalents needed with $t$-BuLi? Would the chlorine in the product undergo exchange?

   **Answer** Lithium–halogen exchange with $n$-BuLi or $t$-BuLi at $-78\,^\circ\mathrm{C}$ in THF or diethyl ether is most suitable: the exchange rate is Br ≫ Cl, so only bromine is exchanged and chlorine remains; with lithium metal directly, a higher temperature is needed, the selectivity is poor, and coupling may occur. With $n$-BuLi the $n$-BuBr formed couples slowly with the aryllithium (or leaves the exchange equilibrium incomplete); with $t$-BuLi the second equivalent immediately undergoes **E2** elimination with the $t$-BuBr formed (giving isobutene, isobutane and LiBr), which makes the exchange irreversible and removes the alkyl halide that could react with the aryllithium. The product 4-chlorophenyllithium is stable at low temperature and the C–Cl does not exchange; with Li and Cl para, it cannot eliminate LiCl to give **benzyne** as o-halophenyllithiums do, but it should still be used quickly at low temperature to avoid reaction with ethereal solvents.

3. Predict the main products when the following compounds are treated with $s$-BuLi/TMEDA at $-78\,^\circ\mathrm{C}$ and then DMF is added: (a) anisole; (b) 3-methoxy-N,N-diethylbenzamide; (c) 4-bromoanisole (with $n$-BuLi).

   **Answer** (a) The methoxy group is a DMG of moderate strength and lithiation occurs ortho to it; formylation with DMF gives 2-methoxybenzaldehyde. (b) The two DMGs are meta to each other, and C2 between them is directed by both (cooperatively) and is the most acidic, so lithiation occurs at C2, giving 2-formyl-3-methoxy-N,N-diethylbenzamide. (c) Lithium–halogen exchange of an aryl bromide with $n$-BuLi is much faster than ortho lithiation, so bromine is replaced by lithium, giving 4-methoxybenzaldehyde rather than reaction ortho to the methoxy group.

4. Both of the following methods convert hex-1-ene into an alcohol. Write the products and explain the difference in regiochemistry and stereochemistry: (a) 9-BBN, then $\ce{H2O2}$/NaOH; (b) $\ce{Hg(OAc)2}$/$\ce{H2O}$, then $\ce{NaBH4}$. If the substrate is 1-methylcyclohexene, what is the relative configuration of the product of (a)?

   **Answer** (a) Boron adds to the terminal carbon (99.9%), the configuration is retained on oxidation, and hexan-1-ol is obtained (anti-Markovnikov). (b) Oxymercuration–demercuration proceeds through a mercurinium ion with Markovnikov orientation and gives hexan-2-ol (racemic), see [6.5.11](/6.5.11#sec-11.4.4). For 1-methylcyclohexene, **hydroboration** is a syn addition, with B adding to C2 and H to C1 (the carbon carrying the methyl group) on the same face, and oxidation retains the configuration, so OH is on the same side as the newly added H and trans to methyl: trans-2-methylcyclohexan-1-ol (racemic) is obtained.

5. A β-hydroxysilane has Si and OH in a syn relationship (drawn on the same side of a zigzag chain). What geometry of alkene is obtained with KH and with $\ce{H2SO4}$, respectively? Why can the same compound give two alkenes?

   **Answer** Base (KH) makes O⁻ attack Si, and syn elimination through a four-membered ring requires a conformation in which Si and O are eclipsed (syn-coplanar); acid ($\ce{H2SO4}$) protonates OH, which leaves as water, and Si leaves from the **antiperiplanar** position (anti elimination, the β-silicon effect stabilizing the transition state). In a Newman projection along the C2–C3 bond: in the zigzag chain the two hydrocarbon groups R and R′ are anti ($180^\circ$) and the Si and OH on the same side are $60^\circ$ apart. When the rear carbon is rotated by $60^\circ$ to eclipse Si and O, R and R′ are $120^\circ$ apart, each eclipsing an H on the opposite carbon, and after elimination they lie on opposite sides of the double bond: basic conditions give the (E)-alkene. When the rear carbon is rotated the other way by $120^\circ$ to make Si and O anti, R and R′ are $60^\circ$ apart (gauche), and after anti elimination they lie on the same side of the double bond: acidic conditions give the (Z)-alkene. The conformations required for the two eliminations differ by a $180^\circ$ rotation about the C–C bond, so the same diastereomer gives alkenes of opposite geometry; for the anti β-hydroxysilane the result is reversed (base gives Z, acid gives E). This stereodivergence, "one precursor, two alkenes", is an advantage of the Peterson olefination over the **Wittig reaction**.

6. A molecule contains the TES ether of a primary alcohol, the TBS ether of a secondary alcohol and the TBDPS ether of another secondary alcohol. How can only one of them be removed at a time?

   **Answer** First remove the TES ether with a mild acid (such as PPTS in methanol, or acetic acid/THF/water): TES is the least hindered and its acidic hydrolysis is about 300 times faster than that of TBS (64 against $2\times10^4$). Then remove the TBS ether with a somewhat stronger acid (such as HCl in methanol, or CSA); TBDPS is a further two orders of magnitude more stable toward acid and survives. Finally TBDPS is removed with TBAF. To remove TBS first in the presence of TBDPS, use acid rather than TBAF (the two have similar stability toward base and fluoride ion, so TBAF is not selective).

7. Why is silicon "oxophilic" and "fluorophilic"? Use this property to explain: (a) chlorotrimethylsilane fumes in moist air, whereas tert-butyl chloride hydrolyzes only slowly in water; (b) silyl ethers can be removed with TBAF; (c) 2-(trimethylsilyl)phenyl trifluoromethanesulfonate gives benzyne with CsF at room temperature.

   **Answer** The electronegativity differences between Si and O or F are large, the Si–O and Si–F bonds have a large ionic component, and electrostatic interaction contributes extra bond energy; the lone pairs of O and F also delocalize into the Si–C σ* orbitals (**negative hyperconjugation**), strengthening and shortening these bonds further. The Si–O (452) and Si–F (565 kJ/mol) bonds are stronger than C–O and C–F by about 90 and 80 kJ/mol, respectively, whereas Si–C and Si–H are weaker than the corresponding carbon bonds, so replacing C, H or Cl by O or F on silicon is thermodynamically very favorable. Kinetically, silicon is large and can accept a fifth ligand, a **nucleophile** attacking from the back to form a low-energy five-coordinate intermediate, so these substitutions are also fast. (a) TMSCl is hydrolyzed rapidly by water in the air through a five-coordinate intermediate to $\ce{Me3SiOH}$ (which condenses to $\ce{(Me3Si)2O}$) and HCl, and HCl with water vapor forms a white mist; the carbon of tert-butyl chloride cannot be five-coordinate and hydrolyzes slowly by **SN1** only. (b) $\ce{F-}$ attacks Si to form a five-coordinate silicate, the Si–O bond breaks, and the stronger Si–F bond forms. (c) $\ce{F-}$ attacks Si, the C–Si bond breaks, and the aryl anion (or concertedly) expels the neighboring triflate as a **leaving group**, giving benzyne ([6.5.15](/6.5.15#sec-15.1.3)); the driving force is the formation of the Si–F bond and the very good leaving ability of TfO⁻.

8. Explain: (a) the **solvolysis** of trans-2-(trimethylsilyl)cyclohexyl trifluoroacetate is about $10^{12}$ times faster than that of cyclohexyl trifluoroacetate, whereas the cis isomer is only about $10^4$ times faster; (b) allyltrimethylsilane reacts with $\ce{DCl}$ to give 3-deuteriopropene rather than 2-deuteriopropene.

   **Answer** (a) In the diaxial conformation of the trans isomer the C–Si bond is **antiperiplanar** to the C–O (leaving group) bond, so as the leaving group departs the C–Si σ electrons can delocalize in parallel into the developing empty p orbital (the **hyperconjugation** of the β-silicon effect is at a maximum), and may even assist departure by **neighboring group participation**. In the cis isomer the angle between C–Si and the leaving group is about $60^\circ$, the overlap of the C–Si σ orbital with the empty p orbital is much smaller, and the stabilization is much smaller. (b) $\ce{D+}$ adds to the terminal carbon C3 farther from silicon (the $\ce{CH2=}$ end), placing the positive charge on C2, β to silicon, where it is stabilized by hyperconjugation with the C–Si bond; $\ce{Cl-}$ then attacks Si, and the electrons of the C1–Si bond form the C1=C2 double bond. D remains on the original C3, which becomes the $\ce{CH2D}$ end of the new propene, that is, 3-deuteriopropene ($\ce{CH2=CH-CH2D}$); the double bond has shifted (SE2′).

9. Starting from 2-fluoroethylamine (conjugate acid $\mathrm{p}K_{\mathrm{a}}$ about 9.0) and ethylamine (10.7), estimate the fractions of the neutral molecules in blood plasma at pH 7.4. What does this imply for drug absorption?

   **Answer** The fraction of neutral molecules is $1/(1 + 10^{\mathrm{p}K_{\mathrm{a}} - \mathrm{pH}})$. Ethylamine: $10^{10.7-7.4} = 10^{3.3} \approx 2000$, a neutral fraction of about $5\times10^{-4}$. 2-Fluoroethylamine: $10^{9.0-7.4} = 10^{1.6} \approx 40$, a neutral fraction of about $2.5\times10^{-2}$, about 50 times more than for ethylamine. Only neutral molecules cross cell membranes by passive diffusion, so introducing a β-fluorine can markedly improve the membrane permeability and oral absorption of amine drugs and reduce accumulation in acidic organelles such as lysosomes; the price is that ionic interactions with the target that depend on the ammonium ion may weaken, so a balance has to be struck.

10. For oxidizing the following alcohols to aldehydes, which is most suitable among the **Swern oxidation**, the Dess–Martin oxidation and Jones reagent? (a) N-Boc-methioninol, containing a sulfide and a Boc-protected amino group (no racemization allowed); (b) 3-phenylpropan-1-ol on a 100 g scale; (c) oxidation of 2-phenylethanol to phenylacetic acid.

    **Answer** (a) The Dess–Martin oxidation (with $\ce{NaHCO3}$): neutral and fast at room temperature, it does not oxidize sulfides (Jones reagent would oxidize the sulfide and remove Boc), and the α **stereocenter** is essentially not racemized; the Swern oxidation is also possible, but needs $i$-$\ce{Pr2NEt}$ and strictly low temperature to avoid racemization, and the dimethyl sulfide formed adds its odor to that of the sulfide in the substrate. (b) The Swern oxidation (or its modification, the Parikh–Doering method): the reagents are cheap and suitable for scale-up; DMP is expensive and its precursor IBX is explosive, so it is unsuitable for large quantities; TEMPO/NaOCl catalytic oxidation could also be considered. (c) To obtain the carboxylic acid, use Jones reagent (the aldehyde hydrates in aqueous solution and is oxidized further) or TEMPO/NaOCl/$\ce{NaClO2}$ in a two-step, one-pot process; Swern and DMP stop at the aldehyde under anhydrous conditions.
