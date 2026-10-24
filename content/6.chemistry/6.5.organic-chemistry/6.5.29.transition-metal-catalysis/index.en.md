---
title: Transition-Metal-Catalyzed Organic Reactions
description: How to write homogeneous catalytic cycles; the Wilkinson catalyst and homogeneous hydrogenation, the asymmetric hydrogenations of Knowles and Noyori; methanol carbonylation, hydroformylation and the Wacker oxidation; a unified framework for palladium-catalyzed cross-coupling (Heck, Suzuki–Miyaura, Kumada, Negishi, Stille, Sonogashira, Buchwald–Hartwig); π-allylpalladium and the Tsuji–Trost reaction; the Pauson–Khand and [2+2+2] cycloadditions; olefin metathesis and the Chauvin mechanism; the Cossee–Arlman mechanism of coordination polymerization.
source_hash: 973107313bd8
---

[6.5.28](/6.5.28) presented the electron counting of transition-metal organometallic compounds and six classes of elementary reactions. This chapter links these elementary reactions into catalytic cycles: in the cycle the metal repeatedly changes its **oxidation state** and coordination number, converting substrate to product on each turn and returning to its original form. Such reactions have changed the face of organic synthesis: four Nobel Prizes in Chemistry in the second half of the twentieth century (coordination polymerization in 1963, hydrogenation by **asymmetric catalysis** in 2001, **olefin metathesis** in 2005, palladium-catalyzed cross-coupling in 2010) were all awarded for transition-metal catalysis, and today a considerable fraction of the reactions forming C–C and C–N bonds in drug synthesis are palladium-catalyzed couplings. This chapter first presents the general way of writing catalytic cycles and their kinetics (connecting with the kinetics of **homogeneous catalysis** in [6.3.17](/6.3.17#sec-17.3.3)), and then discusses in turn hydrogenation, carbonylation and the Wacker oxidation, cross-coupling, π-allylpalladium, **cycloaddition**, olefin metathesis and coordination polymerization. The preparation of main-group organometallic reagents (Grignard, organozinc, organoboron, organotin, organosilicon) is treated in [6.5.10](/6.5.10) and [6.5.27](/6.5.27).

## 29.1. Homogeneous Catalytic Cycles

The mechanism of a transition-metal-catalyzed reaction is usually drawn as a closed cycle: each vertex is a metal complex (an intermediate), each edge an elementary reaction ([6.5.28](/6.5.28#sec-28.4)), with substrates entering at some edges and products leaving at others. Writing a reasonable cycle requires checking several points:

1. The complex added to the reaction system is often not the true **catalyst** but a catalyst precursor (precatalyst): $\ce{Pd(PPh3)4}$ must first dissociate to $\ce{Pd(PPh3)2}$, $\ce{Pd(OAc)2}$ must first be reduced to Pd(0) by a phosphine, amine or organometallic reagent, and $\ce{RhCl(PPh3)3}$ must first lose a phosphine.
2. The valence electron count of each intermediate is generally 16 or 18 (Tolman's 16/**18-electron rule**), and may also be that of a highly reactive 14-electron species; the change in electron count and **oxidation state** at each step must conform to the table of [6.5.28](/6.5.28#sec-28.4).
3. The intermediate with the highest concentration in the cycle is called the resting state, and it is usually the species observable by spectroscopy; what determines the overall rate is the energy difference from the resting state to the highest transition state (the turnover-limiting step), which is not necessarily a single "slow step".
4. The efficiency of a catalyst is measured by the **turnover number** and the **turnover frequency** ([6.3.20](/6.3.20)): the former (TON) is the number of substrate molecules converted per catalyst molecule before deactivation, the latter (TOF) the turnover number per unit time; the industrial Monsanto process has a TON above $10^6$, and laboratory coupling reactions often use 0.1%–5% (mole fraction) of palladium.

The **rate law** of **homogeneous catalysis** has the same form as the **Michaelis–Menten equation** of **enzyme catalysis** ([6.3.17](/6.3.17#sec-17.3.5)): the catalyst first binds the substrate to form an intermediate (a preequilibrium) and then converts it to product, so the rate often shows saturation kinetics in the substrate concentration and is first order in catalyst concentration. Inhibitors (excess ligand, a substrate or product that binds the metal too strongly) act just like competitive inhibition of enzymes: for example, adding $\ce{PPh3}$ slows Wilkinson hydrogenation because it pushes the catalyst back to the coordinatively saturated precursor (Section 29.2.1).

## 29.2. Homogeneous Hydrogenation

### 29.2.1. The Wilkinson Catalyst

Catalytic hydrogenation of alkenes on metal surfaces such as Pd/C, Pt and Raney Ni is **heterogeneous catalysis** ([6.5.11](/6.5.11#sec-11.9)). In 1965 Wilkinson and Coffey independently discovered that a soluble Rh(I) complex can catalyze hydrogenation of alkenes in solution at room temperature and atmospheric pressure.

**Definition 29.2.1 (Wilkinson's Catalyst)** Chlorotris(triphenylphosphine)rhodium(I), $\ce{RhCl(PPh3)3}$, is called **Wilkinson's catalyst**; it catalyzes the hydrogenation of alkenes and alkynes homogeneously at room temperature and atmospheric pressure.

It is prepared by refluxing $\ce{RhCl3*3H2O}$ with excess $\ce{PPh3}$ in ethanol, the excess phosphine also acting as reducing agent (being oxidized to $\ce{Ph3PO}$) and reducing Rh(III) to Rh(I). $\ce{RhCl(PPh3)3}$ is a 16-electron square-planar complex; the main pathway given by Halpern's kinetic studies can be simplified to the following cycle: first one phosphine dissociates, giving the 14-electron $\ce{RhCl(PPh3)2}$; $\ce{H2}$ undergoes **oxidative addition** to give a Rh(III) dihydride; the alkene coordinates; the alkene inserts into the Rh–H bond (**migratory insertion**, the turnover-limiting step); and the alkyl and hydride undergo **reductive elimination** to release the alkane, returning Rh to the +1 state.

![Simplified cycle of alkene hydrogenation catalyzed by Wilkinson's catalyst (L = PPh₃): after RhClL₃ dissociates to RhClL₂, oxidative addition of H₂, alkene coordination, migratory insertion (rate-determining) and reductive elimination occur in turn](./plots/wilkinson-cycle.py)

The mechanism determines its characteristics:

- High selectivity: it reduces only C=C and C≡C and does not reduce aromatic rings, aldehydes, ketones, esters, carboxylic acids, amides, nitriles, azo or nitro groups (these groups cannot coordinate to Rh in a suitable way and insert).
- Syn addition: both H atoms come from the same metal and add from the face on which the alkene is coordinated, so it is a **stereospecific** syn addition; with $\ce{D2}$, maleic acid gives meso-2,3-dideuteriosuccinic acid and fumaric acid gives the racemate.
- The rate is controlled by steric hindrance: monosubstituted and cis-disubstituted alkenes are fast, trans-disubstituted and trisubstituted ones slow, and tetrasubstituted ones hardly react, so the less hindered double bond in a molecule can be hydrogenated selectively; ethylene binds the metal too strongly and is hardly hydrogenated, and also inhibits hydrogenation of other alkenes.
- Unlike heterogeneous catalysis, there are no side reactions of double-bond migration and H/D exchange, and deuteration experiments give clean products.

### 29.2.2. Asymmetric Hydrogenation

Replacing $\ce{PPh3}$ in Wilkinson's catalyst by a chiral phosphine allows discrimination between the two faces of a **prochiral** alkene ([6.5.5](/6.5.5#sec-5.8.2)). In 1968 Knowles and Horner independently reported the first examples, with ee values of only about ten to twenty percent; Knowles then designed at Monsanto the bisphosphine DiPAMP with stereogenic phosphorus atoms and used the cationic complex $\ce{[Rh(DiPAMP)(cod)]+}$ for the asymmetric hydrogenation of an α-(acylamino)cinnamic acid, giving a precursor of L-DOPA (a drug for Parkinson's disease) in about 95% ee. This process went into production in 1974 and was the first industrial process of **asymmetric catalysis**.

It differs from Wilkinson's catalyst in two respects: first, a cationic complex (with a weakly coordinating anion such as $\ce{BF4-}$) is more electron-poor and has more vacant sites; second, it is substrate-directed: the carbonyl oxygen of the amide in the substrate coordinates to Rh and, together with the C=C, forms a chelate ring that fixes the orientation of the substrate relative to the chiral ligand. Halpern's kinetic studies found an unexpected result: the diastereomeric catalyst–substrate complex that predominates in solution reacts very slowly, and the product comes mainly from the minor complex, which reacts much faster with $\ce{H2}$ (the "anti-lock-and-key" behavior). The two complexes interconvert faster than hydrogenation, so the product ratio is determined only by the difference in transition-state energies of the two pathways, which is exactly the **Curtin–Hammett principle** ([6.5.3](/6.5.3#sec-3.9.3)).

Noyori's complexes of BINAP (a bisphosphine with **axial chirality**, [6.5.5](/6.5.5#sec-5.5.1)) and Ru(II) extended asymmetric hydrogenation to many alkenes and to β-keto esters and simple ketones (in Ru–BINAP–diamine catalysts the N–H of the ligand and the H on the metal are transferred simultaneously to C=O, called metal–ligand bifunctional catalysis, [6.5.17](/6.5.17#sec-17.2)). Industrially it is used to produce menthol (Takasago, through asymmetric isomerization), intermediates of carbapenem antibiotics, and others. Knowles and Noyori received the 2001 Nobel Prize in Chemistry for asymmetric catalytic hydrogenation.

```smiles
CC(=O)N/C(=C\c1ccc(O)c(OC)c1)C(=O)O>>CC(=O)N[C@@H](Cc1ccc(O)c(OC)c1)C(=O)O [Rh(DiPAMP)]+, H2
```

## 29.3. Carbonylation and the Wacker Oxidation

### 29.3.1. Methanol Carbonylation: the Monsanto and Cativa Processes

Most of the world's acetic acid is obtained by the reaction of methanol with CO: $\ce{CH3OH + CO -> CH3COOH}$. The Monsanto process (1970) uses $\ce{[RhI2(CO)2]-}$ and HI as the catalyst system, and the cycle consists of the elementary reactions of [6.5.28](/6.5.28#sec-28.4) in turn:

1. HI converts methanol to $\ce{CH3I}$;
2. $\ce{CH3I}$ undergoes **SN2**-type **oxidative addition** to the 16-electron $\ce{[RhI2(CO)2]-}$ (the turnover-limiting step), giving the Rh(III) complex $\ce{[CH3RhI3(CO)2]-}$;
3. The methyl group migrates to an adjacent CO (**migratory insertion**), giving an acyl complex, and the vacancy is occupied by CO;
4. Acetyl iodide is released by **reductive elimination**, returning Rh to $\ce{[RhI2(CO)2]-}$; acetyl iodide is hydrolyzed to acetic acid with regeneration of HI.

![Catalytic cycle of the Monsanto process: the 16-electron $\ce{[RhI2(CO)2]-}$ undergoes SN2-type oxidative addition with iodomethane (the turnover-limiting step, Rh(I) → Rh(III)); the methyl group migrates to an adjacent CO (migratory insertion) to give an acyl complex, and the vacancy is occupied by CO; acetyl iodide reductively eliminates, returning Rh to the +1 state. Outside the cycle, HI converts methanol to iodomethane, and water hydrolyzes acetyl iodide to acetic acid and regenerates HI](./plots/monsanto-cycle.py)

The rate is independent of the CO pressure and methanol concentration and proportional only to the concentrations of rhodium and $\ce{CH3I}$, which shows that step 2 is the **rate-determining step**. BP's Cativa process (1996) uses iridium instead: oxidative addition at Ir is about 150 times faster than at Rh, but migratory insertion is slower and a promoter such as Ru must be added to remove iodide; its catalyst is more stable, needs less water and gives fewer byproducts, and has replaced most Monsanto plants.

### 29.3.2. Hydroformylation

The formation, from an alkene, CO and $\ce{H2}$ under Co or Rh catalysis, of an aldehyde with one more carbon is called hydroformylation (the oxo process):

$$
\ce{RCH=CH2 + CO + H2 -> RCH2CH2CHO \ (linear) + RCH(CH3)CHO \ (branched)}.
$$

$\ce{HCo(CO)4}$ (Roelen, 1938) and $\ce{HRh(CO)(PPh3)3}$ (Wilkinson, 1960s) are two generations of catalysts, and the mechanism (Heck and Breslow) is: the alkene coordinates and inserts into M–H (Markovnikov or anti-Markovnikov), CO inserts into M–C, $\ce{H2}$ adds by **oxidative addition**, and the aldehyde is released by **reductive elimination**. The **regioselectivity** of alkene insertion determines the ratio of linear to branched aldehyde: bulky phosphines (such as excess triphenylphosphine, or bisphosphines with a large bite angle such as Xantphos) make the metal prefer to attach to the terminal carbon ([6.5.28](/6.5.28#sec-28.4.4)), giving the linear aldehyde. Hydroformylation produces more than ten million tonnes of aldehydes per year, which are then reduced to the alcohols used for plasticizers and detergents (butanol, 2-ethylhexanol).

![Cycle of rhodium-catalyzed hydroformylation (Heck–Breslow mechanism, L = PPh₃): the 16-electron $\ce{HRh(CO)L2}$ binds the alkene, the alkene inserts into the Rh–H bond with rhodium on the terminal carbon (favored by bulky phosphines, giving the linear aldehyde); after binding of CO the alkyl migrates to CO to give an acyl complex; $\ce{H2}$ adds oxidatively (Rh(I) → Rh(III)), and reductive elimination releases the aldehyde $\ce{RCH2CH2CHO}$](./plots/hydroformylation-cycle.py)

### 29.3.3. The Wacker Oxidation

**Definition 29.3.1 (Wacker Oxidation)** The reaction that oxidizes alkenes to carbonyl compounds in water (ethylene to acetaldehyde), with $\ce{PdCl2}$ as catalyst, $\ce{CuCl2}$ as cocatalyst and $\ce{O2}$ as the terminal oxidant, is called the **Wacker oxidation** (the Wacker process, 1959):

$$
\ce{CH2=CH2 + 1/2 O2 ->[PdCl2,\ CuCl2][H2O] CH3CHO}.
$$

Its key step is nucleophilic attack on a ligand ([6.5.28](/6.5.28#sec-28.4.7)): after ethylene coordinates to Pd(II), σ donation dominates, the carbons carry a partial positive charge (**umpolung**), and can be attacked by water.

![Catalytic cycle of the Wacker oxidation: PdCl₄²⁻ exchanges a ligand for ethylene, water attacks the coordinated ethylene from outside (anti hydroxypalladation) and loses a proton, β-hydride elimination, reinsertion of the enol and a second β-hydride elimination release acetaldehyde and leave Pd(0); CuCl₂ oxidizes Pd(0) back to Pd(II), and the CuCl formed is oxidized by O₂](./plots/wacker-cycle.py)

Several mechanistic details have experimental support:

- When the reaction is run in $\ce{D2O}$, the acetaldehyde contains no D: all the hydrogen of the acetaldehyde comes from ethylene, and no free vinyl alcohol is involved (otherwise keto–enol tautomerism would introduce D from the solvent). The Pd–H formed by **β-hydride elimination** stays together with the coordinated enol, H is inserted back in the opposite direction to give $\ce{Pd-CH(OH)CH3}$, and a further β-hydride elimination (losing the proton of O–H) gives acetaldehyde.
- The mode of attack by water changes with conditions: at high $\ce{Cl-}$ concentration water attacks the coordinated alkene from the face opposite the metal (anti hydroxypalladation, outer-sphere attack); at low $\ce{Cl-}$ concentration water first coordinates to Pd and then undergoes **migratory insertion** onto the alkene within the coordination sphere (syn hydroxypalladation). The two pathways are distinguished by the stereochemistry of deuterated alkenes.
- Palladium only cycles between two **oxidation states**: Pd(II) oxidizes the alkene and becomes Pd(0), $\ce{2 CuCl2}$ oxidizes it back to $\ce{PdCl2}$, and CuCl is then oxidized by $\ce{O2}$. Overall only oxygen is consumed.

In the laboratory, terminal alkenes are oxidized to methyl ketones with $\ce{PdCl2}$/CuCl/$\ce{O2}$ in DMF–water (the Tsuji–Wacker oxidation): water attacks the more substituted carbon in the Markovnikov sense, so a terminal alkene can be regarded as a "latent form" of a methyl ketone. Changing the ligands and oxidant can also give aldehydes (the anti-Markovnikov product).

```smiles
C=CCCCCCCCC>>CC(=O)CCCCCCCC PdCl2, CuCl, O2
```

## 29.4. Palladium-Catalyzed Cross-Coupling

### 29.4.1. A Unified Catalytic Cycle

**Definition 29.4.1 (Cross-Coupling Reaction)** The reaction in which, under catalysis by a transition metal (mainly Pd or Ni), an organic electrophile R–X (halide, sulfonate) and an organic nucleophile R′–M (organometallic reagent, amine, alcohol, alkene or terminal alkyne) combine to form an R–R′ (or R–N, R–O) bond is called a **cross-coupling reaction**.

Unlike **Gilman reagents** ([6.5.10](/6.5.10#sec-10.4.2)) or the Wurtz reaction, cross-coupling can join two $\mathrm{sp}^2$ carbons (aryl, alkenyl), which **SN2** cannot do (aryl and alkenyl halides do not undergo SN2). Apart from the Heck reaction (with alkenes) and Buchwald–Hartwig amination (with amines), the other couplings share the same three-step cycle (see the Suzuki cycle in Section 29.4.3):

1. **Oxidative addition**: Pd(0) and R–X give R–Pd(II)–X ([6.5.28](/6.5.28#sec-28.4.2)), often the turnover-limiting step. The reactivity order is $\ce{R-I} > \ce{R-OTf} \approx \ce{R-Br} \gg \ce{R-Cl}$; the configuration of alkenyl halides is retained.
2. **Transmetalation**: the **nucleophile** R′–M gives R′ to palladium and X to M ([6.5.28](/6.5.28#sec-28.4.6)); the different couplings differ mainly in this step.
3. **Reductive elimination**: the two organic groups are cis (a trans complex must first isomerize), R–R′ leaves, and Pd(0) is regenerated ([6.5.28](/6.5.28#sec-28.4.3)).

When R and R′ are alkyl groups two difficulties arise: alkylpalladium with a β-H readily undergoes **β-hydride elimination** ([6.5.28](/6.5.28#sec-28.4.5)), and oxidative addition of $\mathrm{sp}^3$ C–X bonds to Pd(0) is slow. Using nickel (which more readily follows single-electron pathways), bulky electron-rich ligands, or cooperative photoredox catalysis can partly overcome them (Fu, MacMillan and others).

| Coupling | Nucleophile | Year | Features |
|---|---|---|---|
| Kumada (Tamao–Kumada–Corriu) | RMgX | 1972 | Ni or Pd; inexpensive reagents, poor functional-group tolerance |
| Negishi | RZnX | 1977 | high reactivity, tolerates esters, nitriles, ketones; organozincs are made by zinc insertion or transmetalation |
| Stille (Migita–Kosugi–Stille) | $\ce{RSnBu3}$, $\ce{RSnMe3}$ | 1977–1978 | neutral conditions, tolerates almost all functional groups; tin reagents are toxic and hard to remove completely |
| Suzuki–Miyaura | $\ce{RB(OH)2}$, $\ce{RBpin}$, R–9-BBN | 1979 | requires base; boron reagents are stable and of low toxicity, can react in water, most widely used |
| Hiyama | $\ce{RSi(OR')3}$, $\ce{RSiMe2F}$ | 1988 | requires activation by $\ce{F-}$ (TBAF) or base |
| Sonogashira | terminal alkyne + CuI | 1975 | for alkynyl groups only; alkenyl and aryl halides |
| Mizoroki–Heck | alkene | 1971–1972 | no organometallic reagent needed, the product is a substituted alkene (β-hydride elimination) |
| Buchwald–Hartwig | amine (alcohol) | 1994 | forms C–N (C–O) bonds, requires strong base and specialized ligands |

### 29.4.2. The Heck Reaction

**Definition 29.4.2 (Heck Reaction)** The reaction in which an aryl or alkenyl halide (or sulfonate) couples with an alkene under the action of a Pd catalyst and a base, replacing an H on the alkene, is called the **Heck reaction** (the Mizoroki–Heck reaction):

$$
\ce{ArX + CH2=CHR ->[Pd(0),\ base] ArCH=CHR + base*HX}.
$$

The reaction was reported independently by Mizoroki (1971) and Heck (1972). The true catalyst is $\ce{Pd(0)L2}$, which can be obtained by dissociation of $\ce{Pd(PPh3)4}$ and is also often generated in situ from $\ce{Pd(OAc)2}$ and $\ce{PPh3}$ (the phosphine being oxidized to the phosphine oxide). The Heck cycle differs from the other couplings: the second step is not **transmetalation**, but coordination of the alkene followed by insertion into the Pd–Ar bond, and then **β-hydride elimination** releases the product.

![Catalytic cycle of the Heck reaction (neutral pathway, L = PPh₃): oxidative addition, alkene coordination, syn migratory insertion (aryl adds to the less substituted carbon), syn β-hydride elimination releasing the E product, and base removing HX from HPdL₂X to regenerate Pd(0)](./plots/heck-cycle.py)

- **Regioselectivity**: the aryl group adds to the less substituted end of the alkene (steric hindrance), almost exclusively for monosubstituted alkenes such as acrylates, acrylonitrile and styrene.
- **Stereoselectivity**: both insertion and β-hydride elimination are syn; after insertion the C–C single bond rotates, and the conformation with β-H syn-coplanar to Pd and the two large groups trans is lowest in energy, so the product is mainly the E alkene.
- The role of the base ($\ce{Et3N}$, $\ce{K2CO3}$, NaOAc) is to neutralize HX and reduce Pd(II)–H to Pd(0); without base the cycle stops at $\ce{HPdL2X}$.
- With aryl triflates, or on adding silver salts, the halide leaves palladium and the reaction follows the cationic pathway; intramolecular Heck reactions can build quaternary carbons and rings, and with chiral bisphosphines (BINAP) asymmetric Heck reactions can be realized (Shibasaki, Overman).

```smiles
Ic1ccccc1.C=CC(=O)OC>>COC(=O)/C=C/c1ccccc1 Pd(OAc)2, PPh3, Et3N
```

### 29.4.3. The Suzuki–Miyaura Coupling

**Definition 29.4.3 (Suzuki–Miyaura Coupling)** The reaction in which an organoboron compound (boronic acid, boronic ester, alkylborane) couples with an organic halide or sulfonate under the action of a Pd catalyst and a base is called the **Suzuki–Miyaura coupling** (the Suzuki coupling, 1979).

The advantages of organoboron reagents make it the most widely used coupling: arylboronic acids are air- and water-stable solids of low toxicity, and the boron byproduct is harmless boric acid; boronic acids and boronic esters can be obtained from **Grignard reagents** and borates, by Miyaura borylation (Pd-catalyzed coupling of $\ce{B2pin2}$ with aryl halides), by **hydroboration** ([6.5.11](/6.5.11#sec-11.4.6), [6.5.27](/6.5.27#sec-27.4.3)) or by Ir-catalyzed C–H borylation of arenes; the reaction can be run in water and alcohols and tolerates aldehydes, ketones, esters, nitro groups and unprotected OH and NH. Alkyl groups can also be coupled: R–9-BBN obtained by hydroboration of alkenes gives $\mathrm{C(sp^3)}$–$\mathrm{C(sp^2)}$ bonds with aryl halides.

Boron is not sufficiently electropositive, and the C–B bond has almost no **nucleophilicity**, so **transmetalation** depends on base. The base can act in two ways: by binding to boron to form a four-coordinate borate $\ce{[ArB(OH)3]-}$, raising the nucleophilicity of the aryl group; or by first converting Ar–Pd–X to Ar–Pd–OH (or OR), which transfers the aryl group to the neutral boronic acid through a Pd–O–B bridge. Kinetic studies (Hartwig and Carrow, 2011) show that under the commonly used aqueous–organic solvent conditions the latter pathway is much faster, and the following figure is drawn for this pathway.

![Catalytic cycle of the Suzuki–Miyaura coupling: oxidative addition of ArX to Pd(0); base replaces the halide by hydroxide; the hydroxypalladium and the arylboronic acid undergo transmetalation through a Pd–O–B bridge, releasing boric acid; once the two aryl groups are cis, reductive elimination gives the biaryl. The Negishi, Stille and Kumada couplings differ only in the reagent for the transmetalation step](./plots/suzuki-cycle.py)

```smiles
COc1ccc(Br)cc1.OB(O)c1ccccc1>>COc1ccc(-c2ccccc2)cc1 Pd(PPh3)4, Na2CO3
```

Biaryls are the skeleton of many drugs: the antihypertensive sartans (losartan) and anticancer kinase inhibitors contain them, and the Suzuki coupling is the standard method for building them.

### 29.4.4. The Kumada, Negishi and Stille Couplings

The cycles of these three couplings are the same as that of the Suzuki coupling and differ only in the transmetalating reagent; the differences are a compromise between reactivity and selectivity (the table in Section 29.4.1).

- Kumada coupling: in 1972 Kumada with Tamao, and Corriu, independently reported the Ni-catalyzed coupling of **Grignard reagents** with aryl and alkenyl halides, the first cross-coupling reaction; before this, Chatt and Shaw (1960) had prepared arylnickel complexes with Grignard reagents (**transmetalation**) and Yamamoto (1970) had observed **reductive elimination** from dialkylnickel compounds, which laid the groundwork. Bisphosphine complexes of Ni ($\ce{NiCl2(dppp)}$, $\ce{NiCl2(dppe)}$) are more active than monophosphine complexes, which is related to the need for a cis structure for reductive elimination, the bisphosphine holding the two groups cis. Coupling of alkenyl halides with alkenyl Grignard reagents retains the configuration of the double bond (**stereospecificity**), but secondary alkyl Grignard reagents isomerize to primary alkyl products through **β-hydride elimination** and reinsertion. The main drawback is that Grignard reagents are incompatible with carbonyl, nitrile and ester groups.
- Negishi coupling: the C–Zn bond of organozincs is more covalent and the **nucleophilicity** is lower, so esters, nitriles and ketones are tolerated; organozincs can be obtained by direct insertion of activated zinc (or Zn/LiCl, Knochel) into alkyl halides, or by transmetalation of organolithium and Grignard reagents with $\ce{ZnCl2}$. The Negishi coupling is often used to synthesize 4′-methylbiphenyl-2-carbonitrile, an intermediate of the sartans, and, with alkenylzincs, to build trisubstituted alkenes stereospecifically (as in the synthesis of the anti-breast-cancer drug tamoxifen).
- Stille coupling: organotins are stable in air and water, the conditions are neutral, and almost all functional groups are tolerated, which suits late-stage couplings in complex natural products; the drawbacks are that tin compounds are very toxic and the byproducts hard to remove completely, so it is used less and less in drug manufacture. The four groups on tin differ in their tendency to transfer, roughly alkynyl > alkenyl > aryl > allyl ≈ benzyl > alkyl, so with $\ce{R'SnBu3}$ or $\ce{R'SnMe3}$ only R′ is transferred.

![Transmetalation in the Kumada, Negishi and Stille couplings (L = PPh₃, Ar from the aryl halide, R from the organometallic reagent): the electrons of the R–M bond move toward palladium and those of the Pd–X bond toward the main-group metal, and through a four-center bridged transition state R is transferred to palladium with retention of configuration (a trans product isomerizes to cis before reductive elimination). M = MgBr is most reactive but does not tolerate carbonyls and nitriles; ZnCl is slower and tolerates esters, nitriles and ketones; $\ce{SnBu3}$ is neutral and slowest, with the transfer tendency of groups on tin alkynyl > alkenyl > aryl > alkyl](./plots/transmetalation-variants.py)

### 29.4.5. The Sonogashira Coupling

**Definition 29.4.4 (Sonogashira Coupling)** The reaction in which a terminal alkyne couples with an aryl or alkenyl halide under the action of a Pd catalyst, a Cu(I) cocatalyst and an amine to give an arylalkyne or enyne is called the **Sonogashira coupling** (Sonogashira, Tohda and Hagihara, 1975).

The reaction has two interlinked cycles: the palladium cycle is the same as in the other couplings; in the copper cycle π coordination of CuI to the terminal alkyne makes the C–H more acidic (the $\mathrm{p}K_{\mathrm{a}}$ of terminal alkynes is about 25, [6.5.3](/6.5.3#sec-3.1.4), and after coordination weak bases such as $\ce{Et3N}$ and $\ce{iPr2NH}$ can deprotonate), forming a copper acetylide, which transfers the alkynyl group to palladium.

![Palladium and copper cycles of the Sonogashira coupling: Cu(I) coordinates the terminal alkyne and the amine deprotonates it, giving a copper acetylide that undergoes transmetalation with ArPdL₂X; reductive elimination releases the arylalkyne](./plots/sonogashira-cycle.py)

The reaction conditions are mild (often at room temperature), many functional groups are tolerated, and the reaction is widely used in the synthesis of enyne and conjugated alkyne structures in drugs and natural products, molecular wires and organic electronic materials (Tour and coworkers used it to "assemble" the human-shaped molecule NanoPutian). A side effect of copper is that it catalyzes the oxidative dimerization of terminal alkynes in the presence of oxygen (Glaser coupling), so oxygen must be excluded, or copper-free conditions used.

```smiles
Ic1ccccc1.C#CCO>>OCC#Cc1ccccc1 PdCl2(PPh3)2, CuI, Et3N
```

### 29.4.6. The Buchwald–Hartwig Amination

**Definition 29.4.5 (Buchwald–Hartwig Amination)** The reaction in which an aryl halide or sulfonate couples with a primary or secondary amine under the action of a Pd catalyst, a phosphine ligand and a base to give an arylamine is called the **Buchwald–Hartwig amination**.

Migita and coworkers (1983) first reported the Pd-catalyzed C–N coupling of aryl bromides with aminotin reagents; in 1994 Buchwald and Hartwig almost simultaneously and independently developed the reaction directly with amines. This reaction solved an old problem of arylamine synthesis: the classical methods rely on nitration–reduction or on **nucleophilic aromatic substitution** ([6.5.14](/6.5.14#sec-14.11)), and the latter applies only to aromatic rings with strong electron-withdrawing groups.

In the cycle, coordination and deprotonation of the amine replace **transmetalation**: the amine coordinates to Ar–Pd(II)–X, a strong base (NaO$t$Bu, LiHMDS, $\ce{Cs2CO3}$) removes the N–H proton and the halide, giving an arylaminopalladium, and **reductive elimination** then forms the C–N bond.

![Catalytic cycle of the Buchwald–Hartwig amination (L is a bulky monophosphine): monoligated Pd(0)L adds oxidatively to ArX, the amine coordinates, the base deprotonates it to give the amidopalladium, and C–N reductive elimination releases the arylamine](./plots/buchwald-cycle.py)

The development of ligands is the main thread of this reaction: the first generation used $\ce{P}(o\text{-tolyl})_3$ and worked only for secondary amines; the bisphosphines BINAP and DPPF made primary amines react as well; Buchwald's dialkylbiaryl phosphines (XPhos, BrettPhos, RuPhos) and Hartwig's bulky alkylphosphines allow aryl chlorides, and even ammonia and amides, to be coupled. They have in common that they are "bulky and electron-rich" ([6.5.28](/6.5.28#sec-28.3.3)): electron richness promotes **oxidative addition**, and bulk keeps palladium monoligated and speeds reductive elimination. The side reaction competing with reductive elimination is β-hydride elimination of the amidopalladium (the α-C–H of the amine), which gives an imine and the dehalogenated arene ArH; bulky ligands can suppress it. The copper-catalyzed Ullmann–Goldberg reaction and the Chan–Lam coupling (arylboronic acids and amines with Cu(II) in air) are two other methods of forming C–N bonds.

```smiles
CC(C)(C)c1ccc(Cl)cc1.C1COCCN1>>CC(C)(C)c1ccc(N2CCOCC2)cc1 Pd2(dba)3, XPhos, NaOtBu
```

### 29.4.7. Other Couplings and C–H Activation

The same framework of "**oxidative addition**–ligand exchange–**reductive elimination**" can form other bonds: aryl halides with $\ce{Zn(CN)2}$ or $\ce{K4[Fe(CN)6]}$ give aryl nitriles under palladium catalysis ([6.5.20](/6.5.20#sec-20.4.2)); with alcohols and phenols they give aryl ethers (C–O coupling); in the presence of CO they give aryl ketones, esters and amides (carbonylative coupling); and when the **enolates** of ketones, esters and amides serve as **nucleophiles**, α-arylcarbonyl compounds result ([6.5.21](/6.5.21#sec-21.9)). A further direction is C–H activation: a directing group (pyridine, amide) brings palladium close to the ortho C–H bond, which is broken by concerted metalation–deprotonation, removing the need for prior introduction of a halogen or metal.

![Concerted metalation–deprotonation (CMD): the acetate on Pd(II) uses its other oxygen as an intramolecular base, and through a six-membered transition state the lone pair of oxygen removes the proton from the arene while the electrons of the C–H bond form the new Pd–C bond; neither Pd(IV) nor a free carbanion is involved, acetic acid is released, and an arylpalladium(II) results](./plots/cmd.py)

## 29.5. π-Allylpalladium and the Tsuji–Trost Reaction

**Definition 29.5.1 (Tsuji–Trost Reaction)** The reaction in which a substrate with a leaving group at the allylic position, such as an allyl acetate or carbonate, forms an $\eta^3$-allylpalladium under Pd(0) catalysis and is then attacked by a nucleophile, giving allylic substitution, is called the **Tsuji–Trost reaction** (Tsuji, 1965; Trost, 1973).

The mechanism is the $\eta^3$-allyl chemistry of [6.5.28](/6.5.28#sec-28.5.2): Pd(0) attacks from the face opposite the **leaving group**, the leaving group departs (**oxidative addition**, with inversion), giving an $\eta^3$-allylpalladium cation; a soft **nucleophile** (malonate anion, amine and the like, conjugate acid $\mathrm{p}K_{\mathrm{a}} < 25$) attacks the terminal carbon of the allyl group from the face opposite palladium (a second inversion), giving the product with net retention of configuration and regenerating Pd(0). Hard nucleophiles (Grignard reagents, organozincs) first attack the metal (**transmetalation**) and then undergo **reductive elimination** from the same side of palladium, with net inversion. The **regioselectivity** is generally attack of the nucleophile at the less hindered terminal carbon.

![Catalytic cycle of Tsuji–Trost allylic alkylation (L = PPh₃, Nu⁻ is the malonate anion): Pd(0)L₂ coordinates the double bond of allyl acetate; oxidative addition from the face opposite the leaving group releases acetate (first inversion) and gives the cationic η³-allylpalladium; the soft nucleophile attacks the terminal carbon of the allyl group from the face opposite palladium (second inversion), giving the η² complex of the product, which is released. Two inversions, net retention](./plots/tsuji-trost-cycle.py)

```smiles
CC(=O)OC/C=C/c1ccccc1.CCOC(=O)CC(=O)OCC>>CCOC(=O)C(C/C=C/c1ccccc1)C(=O)OCC Pd(PPh3)4, NaH
```

The C₂-symmetric bisphosphine ligands designed by Trost allow this reaction to proceed asymmetrically: the chiral "pocket" of the ligand determines at which end of the $\eta^3$-allyl, or at which face of a prochiral allyl, the nucleophile attacks (asymmetric allylic alkylation, **asymmetric catalysis**). It has been used in the synthesis of many drugs and natural products.

## 29.6. Metal-Catalyzed Cycloadditions

### 29.6.1. The Pauson–Khand Reaction

The formal [2+2+1] **cycloaddition** of an alkyne, an alkene and CO under the action of $\ce{Co2(CO)8}$ to give a cyclopentenone is called the Pauson–Khand reaction (1971):

```smiles
C#CCCCC.C1=CC2CCC1C2>>CCCCC1=CC2C(C1=O)C1CCC2C1 Co2(CO)8
```

The mechanism (Magnus) is a series of elementary reactions: the alkyne and $\ce{Co2(CO)8}$ form the stable $\ce{Co2(CO)6}(\mu\text{-alkyne})$ complex ([6.5.28](/6.5.28#sec-28.3.4)); one Co loses CO and coordinates the alkene; the alkene inserts into a Co–C bond to give a cobaltacycle; CO inserts; and **reductive elimination** gives the cyclopentenone. The intramolecular reaction (of enynes) builds a bicyclic skeleton in one step and is often used in the synthesis of terpenoid natural products; adding an amine oxide (which removes CO to create a vacancy, [6.5.28](/6.5.28#sec-28.4.7)) allows the reaction to proceed at room temperature.

![The Pauson–Khand reaction (terminal alkyne R–C≡C–H, ethylene and CO, simplified Magnus mechanism): the alkyne and $\ce{Co2(CO)8}$ form the stable $\ce{Co2(CO)6}$(μ-alkyne) complex (a tetrahedral C₂Co₂ core); one Co loses CO and binds the alkene, which inserts into the Co–C bond on the side of the less hindered alkyne carbon to give a cobaltacyclopentene ([Co] denotes a Co₂(CO)ₙ unit); CO inserts into the Co–CH₂ bond and reductive elimination closes the ring to the cyclopentenone, with the larger substituent R next to the carbonyl](./plots/pauson-khand.py)

### 29.6.2. The [2+2+2] Cycloaddition

Trimerization of three alkyne molecules to benzene is thermodynamically very favorable, but the barrier of the thermal reaction is extremely high (three molecules colliding at once, with unfavorable symmetry, [6.5.12](/6.5.12#sec-12.4)). Transition metals break it into feasible steps: two alkynes couple oxidatively on the metal to a metallacyclopentadiene, the third alkyne inserts (or adds by [4+2]), and **reductive elimination** gives the benzene ring. Reppe used Ni to catalyze trimerization and tetramerization of acetylene ([6.5.11](/6.5.11#sec-11.12.6)); Vollhardt used $\ce{CpCo(CO)2}$ to cotrimerize diynes and monoynes, building **polycyclic aromatic hydrocarbons**; with a nitrile in place of the third alkyne, cobalt catalysis gives substituted pyridines, an industrial synthesis of pyridines. The related copper-catalyzed azide–alkyne cycloaddition (CuAAC), which proceeds through copper acetylides, was mentioned in [6.5.12](/6.5.12#sec-12.4.5), and its use in **bioorthogonal chemistry** is described in [6.5.33](/6.5.33#sec-33.8.2).

![Cobalt-catalyzed [2+2+2] cyclotrimerization of alkynes (Vollhardt, CpCo, alkyne substituents omitted): two alkynes coordinated to CpCo couple oxidatively (Co(I) → Co(III)) to give a cobaltacyclopentadiene; the third alkyne adds to the metallacycle (insertion or [4+2] cycloaddition of the diene), and reductive elimination releases the benzene ring and regenerates CpCo; with a nitrile as the third component a pyridine is obtained](./plots/cyclotrimerization.py)

## 29.7. Olefin Metathesis

**Definition 29.7.1 (Olefin Metathesis)** The reaction in which, under catalysis by a metal carbene, the C=C bonds of two alkenes are broken and the alkylidene groups at the two ends recombine into new alkenes is called **olefin metathesis**:

$$
\ce{R1CH=CHR1 + R2CH=CHR2 <=> 2 R1CH=CHR2}.
$$

In 1964 Banks and Bailey (Phillips Petroleum) discovered disproportionation of propylene to ethylene and but-2-ene over heterogeneous molybdenum and tungsten catalysts (the Phillips triolefin process); today the reverse is used industrially, with metathesis of ethylene and butene to produce propylene. Every step of metathesis is reversible and the **equilibrium constant** is close to 1 (the kinds and numbers of bonds do not change), so the reaction is driven by entropy and by **Le Chatelier's principle**: removal of volatile ethylene, or use of **ring strain**.

In 1971 Chauvin proposed the mechanism now accepted: a metal carbene (alkylidene) and an alkene undergo [2+2] **cycloaddition** to give a metallacyclobutane, which then undergoes retro-[2+2] cleavage in the other direction, releasing a new alkene and forming a new metal carbene. The "exchange of partners" occurs repeatedly between metal carbene and alkene. This mechanism explains why cross metathesis of a cyclic alkene with an acyclic alkene gives the "crossed" product from the very start, and it was later confirmed by the metal carbenes and metallacyclobutanes isolated by Schrock and Grubbs.

![The Chauvin mechanism of olefin metathesis (self-metathesis of a terminal alkene): [M]=CH₂ and RCH=CH₂ undergo [2+2] to a metallacyclobutane, and retro-[2+2] releases ethylene and forms [M]=CHR; the latter undergoes [2+2] and retro-[2+2] with a second alkene molecule, releasing RCH=CHR and regenerating [M]=CH₂](./plots/metathesis-cycle.py)

There are two classes of practical homogeneous catalysts (Chauvin, Grubbs and Schrock received the 2005 Nobel Prize in Chemistry):

| | Schrock catalysts | Grubbs catalysts |
|---|---|---|
| Structure | alkylidene–imido complexes of high-valent Mo(VI) or W(VI), such as $\ce{Mo(=CHCMe2Ph)(=NAr)(OR)2}$ | Ru(II) carbenes: first generation $\ce{(PCy3)2Cl2Ru=CHPh}$ (1995), second generation with one $\ce{PCy3}$ replaced by an N-heterocyclic carbene (1999), Hoveyda–Grubbs catalyst with a chelating isopropoxybenzylidene |
| Carbene type | **Schrock carbene** ([6.5.28](/6.5.28#sec-28.5.4)) | neutral late-transition-metal carbene |
| Activity | very high, can handle hindered and electron-poor alkenes; catalysts can be designed to be highly stereoselective (Z-selective) and asymmetric | moderate to high |
| Tolerance | sensitive to air, water and protic or electrophilic groups such as aldehydes, alcohols and acids, must be handled in a glove box | stable to air and water, tolerates almost all functional groups, most commonly used |

There are several types of metathesis:

- Cross metathesis (CM): exchange between two different alkenes; the selectivity depends on the relative rates of self-metathesis of the two alkenes.
- Ring-closing metathesis (RCM): two terminal alkenes in one molecule form a cycloalkene with release of ethylene, favored by entropy and suited to five- to seven-membered rings and macrocycles (macrocycles must be made in dilute solution). For example, Yamamoto and coworkers (2003) used RCM to close an ether ring in the total synthesis of the ladder polyether toxin gambierol.
- Ring-opening metathesis (ROM) and ring-opening metathesis polymerization (ROMP): strained cycloalkenes (norbornene, cyclobutene, cyclooctene) open, driven by ring strain; in the absence of a chain-transfer agent polymers are formed (ROMP, a living polymerization with Grubbs catalysts).
- Acyclic diene metathesis polymerization (ADMET): polycondensation of α,ω-dienes with release of ethylene.
- Enyne metathesis: an alkene and an alkyne give a 1,3-diene.

```smiles
C=CCC(CC=C)(C(=O)OCC)C(=O)OCC>>CCOC(=O)C1(C(=O)OCC)CC=CC1.C=C Grubbs II
```

In chemical biology, ring-closing metathesis is used to connect two side chains of a peptide (alkenyl amino acids introduced beforehand) into a "staple", stabilizing the α-helical conformation and improving cell permeability (stapled peptides, Verdine and coworkers, 2000).

## 29.8. Coordination Polymerization: The Cossee–Arlman Mechanism

In **Ziegler–Natta catalysts** ([6.5.11](/6.5.11#sec-11.11)), an alkylaluminum reduces and alkylates $\ce{TiCl4}$, forming on the surface of $\ce{TiCl3}$ crystals a titanium center carrying one alkyl group and one vacant site. The chain-growth mechanism proposed by Cossee and Arlman (1964) is the repetition of two elementary reactions: ethylene or propylene coordinates to the vacant site on Ti and then inserts into the Ti–C bond ([6.5.28](/6.5.28#sec-28.4.4)), with the chain and the vacancy exchanging places. $\mathrm{d}^0$ Ti(IV) cannot back-donate electrons to the alkene, so the alkene complex is very weak and insertion follows quickly after each coordination; and because a $\mathrm{d}^0$ metal does not stabilize an alkene–hydride, **β-hydride elimination** (chain transfer) is much slower than insertion, and the chain can grow to tens of thousands of monomer units. An α-**agostic interaction** ([6.5.28](/6.5.28#sec-28.5.5)) stabilizes the transition state of insertion.

![The Cossee–Arlman chain-growth mechanism ([Ti] is a titanium center on the $\ce{TiCl3}$ surface, P the growing polymer chain, □ a vacant site): ethylene coordinates to the vacant site cis to the Ti–P bond ($\mathrm{d}^0$ titanium cannot back-donate, the complex is very weak and inserts immediately); the polymer chain migrates with the electron pair of the Ti–P bond to the distal alkene carbon while the π electrons bond the proximal carbon to titanium (a four-center transition state); the chain has grown by two carbons and the vacancy has moved to the place where the chain was, awaiting the next monomer](./plots/cossee-arlman.py)

Homogeneous **metallocene** catalysts ($\ce{Cp2ZrCl2}$ with methylaluminoxane, MAO, Kaminsky, 1980) are single-site, which allows the stereoregularity of the polymer to be predicted from the symmetry of the ligand: a $C_2$-symmetric bridged bis(indenyl)zirconium catalyst selects the same face of propylene at each insertion, giving isotactic polypropylene; a $C_s$-symmetric catalyst selects the two faces alternately, giving syndiotactic polypropylene.

## 29.9. Research Frontiers

Transition-metal catalysis is still developing rapidly, and three directions are most closely related to the later parts of this course. The first is to replace Pd, Rh and Ir by abundant metals such as Ni, Fe, Co and Cu: nickel readily undergoes **single electron transfer**, and combined with **photoredox catalysis** (Ni/photoredox dual catalysis, MacMillan, Doyle, Molander and others) it can couple alkyl carboxylic acids, alcohols and amines, forming $\mathrm{C(sp^3)}$–$\mathrm{C(sp^2)}$ bonds that were previously very hard to form ([6.5.31](/6.5.31#sec-31.5)). The second is direct functionalization of C–H bonds, which makes syntheses shorter and more atom-economical. The third is metal-catalyzed reactions in biological systems: palladium and ruthenium complexes that remove **protecting groups** or perform couplings in cells and synthesize drugs in situ in living cells, and artificial metalloenzymes engineered by directed evolution (placing iridium or rhodium complexes in the pocket of a protein, or engineering heme proteins to catalyze carbene transfers not found in nature). The latter combine the organometallic chemistry of this chapter with the selectivity of **enzyme catalysis**, and details are left to Chemical Biology, 6.6.

## Summary

The main catalytic reactions and their elementary steps:

| Reaction | Catalyst | Elementary steps (in order) | Key points |
|---|---|---|---|
| Wilkinson hydrogenation (Definition 29.2.1) | $\ce{RhCl(PPh3)3}$ | dissociation, $\ce{H2}$ **oxidative addition**, alkene coordination, **migratory insertion** (rate-determining), **reductive elimination** | reduces only C=C and C≡C; syn addition; less hindered double bonds are faster |
| Asymmetric hydrogenation | Rh–DiPAMP, Ru–BINAP | as above; substrate chelation directs | L-DOPA (1974); Curtin–Hammett control |
| Monsanto acetic acid process | $\ce{[RhI2(CO)2]-}$/HI | $\ce{CH3I}$ oxidative addition (rate-determining), CO migratory insertion, reductive elimination | the Cativa process uses Ir |
| Hydroformylation | $\ce{HCo(CO)4}$, $\ce{HRh(CO)(PPh3)3}$ | alkene insertion into M–H, CO insertion, $\ce{H2}$ oxidative addition, reductive elimination | linear/branched ratio controlled by ligand bulk |
| Wacker oxidation (Definition 29.3.1) | $\ce{PdCl2}$/$\ce{CuCl2}$/$\ce{O2}$ | coordination, attack of water on the coordinated alkene, **β-hydride elimination**/reinsertion, reoxidation of Pd(0) | H does not come from the solvent; terminal alkene → methyl ketone |
| Cross-coupling (Definition 29.4.1) | Pd(0), Ni(0) | oxidative addition, **transmetalation**, reductive elimination | Kumada (Mg), Negishi (Zn), Stille (Sn), Suzuki (B, Definition 29.4.3), Hiyama (Si) |
| Heck reaction (Definition 29.4.2) | Pd(0), base | oxidative addition, alkene insertion, β-hydride elimination, base regenerates Pd(0) | aryl adds to the less substituted carbon; E product |
| Sonogashira coupling (Definition 29.4.4) | Pd(0), CuI, amine | palladium cycle + transmetalation of the copper acetylide | terminal alkynes and sp² halides |
| Buchwald–Hartwig amination (Definition 29.4.5) | Pd, bulky electron-rich phosphine, strong base | oxidative addition, amine coordination and deprotonation, C–N reductive elimination | arylamines; side reaction β-hydride elimination |
| Tsuji–Trost reaction (Definition 29.5.1) | Pd(0) | oxidative addition (inversion), nucleophilic attack on the η³-allyl (inversion) | soft **nucleophiles** net retention, hard nucleophiles net inversion |
| Pauson–Khand, [2+2+2] | $\ce{Co2(CO)8}$, $\ce{CpCo(CO)2}$ | coordination, insertion, CO insertion, reductive elimination | cyclopentenones, benzenes and pyridines |
| **Olefin metathesis** (Definition 29.7.1) | Grubbs (Ru), Schrock (Mo, W) | [2+2] to a metallacyclobutane, retro-[2+2] | driven by entropy (removal of ethylene) or **ring strain**; CM, RCM, ROMP |
| Coordination polymerization | Ziegler–Natta, **metallocenes** | alkene coordination, insertion into M–C, repeated | ligand symmetry determines stereoregularity |

## Questions

1. Why can Wilkinson's catalyst hardly hydrogenate ethylene, yet hydrogenate hex-1-ene quickly? Why does adding excess $\ce{PPh3}$ slow the hydrogenation?

   **Answer** Ethylene is small and a good π acceptor, and the complex $\ce{RhCl(C2H4)(PPh3)2}$ it forms with Rh(I) is very stable and becomes an off-cycle "trap", holding the catalyst in an unreactive state; it also preferentially occupies the vacant site and prevents addition of $\ce{H2}$. Hex-1-ene binds Rh more weakly and can coordinate, insert and leave normally within the cycle. Excess $\ce{PPh3}$ shifts the equilibrium $\ce{RhClL3 <=> RhClL2 + L}$ to the left, lowering the concentration of the 14-electron active species; it can also coordinate to the dihydride and occupy the vacant site that the alkene needs. The rate is therefore inversely proportional to [$\ce{PPh3}$], equivalent to competitive inhibition.

2. In Knowles's L-DOPA synthesis, how does the cationic $\ce{[Rh(DiPAMP)]+}$ differ from Wilkinson's catalyst? Why must the substrate carry an amide group? The predominant catalyst–substrate complex in solution does not give the major product; does this contradict the enantioselectivity?

   **Answer** The cationic complex is more electron-poor, the weakly coordinating $\ce{BF4-}$ does not occupy a coordination site, and the metal has more vacant sites; the chiral bisphosphine is chelating and, unlike $\ce{PPh3}$, does not dissociate and lose the chiral environment. The carbonyl oxygen of the amide coordinates to Rh and, together with the C=C, fixes the substrate as a five-membered chelate ring, so that the substrate has only two orientations relative to the chiral ligand (two diastereomeric complexes), which is the precondition for high selectivity. The two diastereomeric complexes interconvert faster than the oxidative addition of $\ce{H2}$ (the selectivity-determining step), so by the **Curtin–Hammett principle** the product ratio depends only on the difference in transition-state energies of the two pathways and not on the equilibrium ratio of the two complexes; the minor complex reacts much faster with $\ce{H2}$ and so gives the major product. There is no contradiction.

3. Wacker oxidation of ethylene in $\ce{D2O}$ gives acetaldehyde containing no D. What mechanism does this result exclude?

   **Answer** It excludes the mechanism "free vinyl alcohol $\ce{CH2=CHOH}$ is formed first and then tautomerizes to acetaldehyde": in the tautomerization the H on carbon would come from the solvent and give $\ce{CH2DCHO}$ in $\ce{D2O}$. In fact, after hydroxypalladation gives $\ce{Pd-CH2CH2OH}$, the Pd–H obtained by **β-hydride elimination** does not leave the metal, H is inserted back with the opposite **regioselectivity** to give $\ce{Pd-CH(OH)CH3}$, and then the proton on the O–H side is lost and the Pd–C bond breaks, giving acetaldehyde. All four H atoms of acetaldehyde come from ethylene (only one H migrates within the molecule), and the D on O–H leaves as $\ce{D+}$.

4. Synthesize 4-methoxybiphenyl by Suzuki coupling: give the starting materials, catalyst and base, and explain the role of the base. What changes would be needed if the Negishi coupling were used instead?

   **Answer** 4-Bromoanisole + phenylboronic acid, $\ce{Pd(PPh3)4}$ (or $\ce{Pd(OAc)2}$/phosphine), aqueous $\ce{Na2CO3}$ or $\ce{K2CO3}$ with toluene or dioxane, with heating (bromobenzene and 4-methoxyphenylboronic acid can also be used). The base converts Ar–Pd–Br to Ar–Pd–OH, which undergoes **transmetalation** with the boronic acid through a Pd–O–B bridge (or turns the boronic acid into a four-coordinate borate, raising the **nucleophilicity** of the phenyl group); without base the neutral boronic acid hardly transmetalates. Negishi coupling: first prepare phenyl Grignard or phenyllithium from bromobenzene and Mg or $\ce{BuLi}$, then transmetalate with $\ce{ZnCl2}$ to PhZnCl and react it with 4-bromoanisole and a Pd catalyst in anhydrous THF; no base is needed, but anhydrous and oxygen-free conditions are required.

5. Iodobenzene reacts with methyl acrylate under $\ce{Pd(OAc)2}$, $\ce{PPh3}$ and $\ce{Et3N}$. (a) Write the product and explain the origin of the regio- and **stereoselectivity**. (b) What happens without $\ce{Et3N}$? (c) $\ce{Pd(OAc)2}$ is Pd(II); how does it become Pd(0)?

   **Answer** (a) Methyl (E)-cinnamate. When the alkene inserts into Pd–Ph, the phenyl group adds to the less hindered terminal $\ce{CH2}$ and Pd attaches to the carbon bearing the ester (the Pd–C bond so formed is also stronger); after insertion the C–C bond rotates to a conformation in which one β-H is syn-coplanar to Pd and Ph and $\ce{CO2Me}$ are trans, and syn β-hydride elimination gives the E product. (b) The cycle stops at $\ce{HPd(PPh3)2I}$ and Pd(0) cannot be regenerated, so the reaction stops after consuming an amount of substrate equal to that of the catalyst; the HI formed would also destroy the substrate. (c) After $\ce{PPh3}$ coordinates to Pd(II), acetate attacks the coordinated phosphine (or the reaction proceeds via water), the phosphine is oxidized to $\ce{Ph3PO}$ and palladium is reduced to $\ce{Pd(0)(PPh3)n}$; amines and alkenes can also reduce Pd(II) (through β-hydride elimination).

6. Synthesize diethyl cyclopent-3-ene-1,1-dicarboxylate from diethyl 2,2-diallylmalonate by ring-closing metathesis. Why must the reaction be run in dilute solution with continuous removal of ethylene? What would be obtained with cycloocta-1,5-diene and a Grubbs catalyst?

   **Answer** Intramolecular RCM competes with intermolecular cross metathesis (oligomerization), and dilute solution favors the intramolecular reaction (the rate of ring closure is independent of concentration, whereas the intermolecular reaction increases with concentration). Every metathesis step is reversible with an enthalpy change near zero, and the driving force is the entropy gain from release of ethylene, so removing ethylene (a nitrogen stream, reduced pressure) shifts the equilibrium toward the product. Cycloocta-1,5-diene has some **ring strain** and, with a Grubbs catalyst, undergoes ring-opening metathesis polymerization (ROMP), giving 1,4-polybutadiene; a small amount of a terminal alkene as chain-transfer agent can control the molecular weight.

7. (R)-Cyclohex-2-en-1-yl acetate (assume a single enantiomer, acetoxy group above the ring) reacts with sodium dimethyl malonate under $\ce{Pd(PPh3)4}$ catalysis. On which face of the ring is the malonate group in the product? And if the **nucleophile** is changed to PhZnCl?

   **Answer** Pd(0) attacks from the face opposite the acetoxy group (below the ring), acetate leaves, and the $\eta^3$-allylpalladium is below the ring (first inversion). The malonate anion is a soft nucleophile and attacks the terminal carbon from the face opposite palladium, that is, above the ring (second inversion), so the malonate group is on the same face (above) as the original acetoxy group, with net retention of configuration (because of the symmetry of the allyl group the product can form at C1 or C3, the two ends of the cyclohexenyl being equivalent). PhZnCl is a hard organometallic nucleophile: it first transfers the phenyl group to palladium (transmetalation, the phenyl group below the ring) and then undergoes **reductive elimination** from the same side of palladium, the phenyl group being below the ring, with net inversion of configuration.
