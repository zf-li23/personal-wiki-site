---
title: Arynes, Other Reactions of Arenes, and Phenols
description: Evidence for, structure, generation and reactions of benzyne (isotope labeling, cycloaddition, regioselectivity of nucleophilic addition); catalytic hydrogenation and Birch reduction of arenes; radical addition of chlorine and hexachlorocyclohexane; benzylic radicals, cations and anions, side-chain halogenation and oxidation, benzyl protecting groups; polyarylmethanes and biphenyl; reactions and orientation of naphthalene, anthracene and phenanthrene, and metabolic activation and carcinogenicity of polycyclic aromatic hydrocarbons; structure and acidity of phenols, electrophilic substitution, ether and ester formation, the Fries rearrangement, FeCl₃ color test, the Reimer–Tiemann and Kolbe–Schmitt reactions, oxidation to quinones, and industrial syntheses of phenol; aromatization.
source_hash: cea3f67f6bf3
---

[6.5.14](/6.5.14) treated substitution on the aromatic ring; this chapter discusses the rest of the chemistry of arenes. The first part concerns reactions of the aromatic ring itself: haloarenes without electron-withdrawing groups undergo substitution under strongly basic conditions through the highly reactive benzyne intermediate, and the aromatic ring can also be reduced (catalytic hydrogenation, Birch reduction) or undergo radical addition under more severe conditions, at the cost of aromaticity. The second part concerns reactions of the carbon attached to the aromatic ring (the benzylic position): the aromatic ring stabilizes benzylic radicals, cations and anions by resonance, which makes the benzylic position the most reactive position in the molecule. The third part treats polyarylmethanes, biphenyl and fused arenes, whose aromaticity is weaker than that of benzene ([6.5.13](/6.5.13#sec-13.7.1)) and whose reactions are concentrated at particular positions; polycyclic aromatic hydrocarbons are metabolically activated in the body and cause cancer, a meeting point of organic chemistry, toxicology and molecular biology. The fourth part is phenols: conjugation of the hydroxy group with the aromatic ring makes phenols far more acidic than alcohols and the ring highly activated, and many named reactions of phenols (Fries, Reimer–Tiemann, Kolbe–Schmitt) and their industrial synthesis (the cumene process) are treated here. For the general properties of alcohols and ethers see [6.5.10](/6.5.10), for the chemistry of **quinones** see [6.5.17](/6.5.17#sec-17.8), and for phenolic acids see [6.5.18](/6.5.18#sec-18.7.4).

## 15.1. Benzyne

### 15.1.1. Evidence for the Elimination–Addition Mechanism

Haloarenes without activating groups also undergo nucleophilic substitution with extremely strong bases: chlorobenzene and potassium amide in liquid ammonia ($-33\,^\circ\mathrm{C}$) give aniline; chlorobenzene and aqueous NaOH at $350\,^\circ\mathrm{C}$ under pressure give phenol. These reactions cannot proceed through the Meisenheimer complex of [6.5.14](/6.5.14#sec-14.11): there is no group on the ring that can accept negative charge.

The decisive evidence came from isotopic labeling (Roberts, 1953). Chlorobenzene labeled with $^{14}\mathrm{C}$ at C1 reacts with $\ce{KNH2}$ to give aniline in which half of the amino groups are attached to the labeled carbon and half to the adjacent carbon. Direct substitution could give only the former; the result shows that the reaction proceeds through a symmetrical intermediate in which the two adjacent carbons are equivalent. Other evidence:

- haloarenes without an ortho H (such as 2-bromo-1,3-dimethylbenzene) do not react;
- 2-chlorotoluene and 3-chlorotoluene both give mixtures of ortho and meta toluidines with $\ce{NaNH2}$, the substituent having "moved" (cine substitution);
- dienes such as furan and anthracene added to the reaction trap the intermediate and give Diels–Alder adducts (15.1.4).

**Definition 15.1.1 (Benzyne)** The highly reactive intermediate $\ce{C6H4}$ containing one "triple bond" in the ring, formed by removing one substituent from each of two adjacent carbons of a benzene ring (H and a leaving group), is called **benzyne** (*o*-benzyne, 1,2-didehydrobenzene); such intermediates of aromatic rings in general are called arynes.

The reaction proceeds in two steps: the strong base removes the H ortho to the leaving group (this H being activated by the inductive effect of the halogen) to give an aryl anion, which loses halide to give benzyne (elimination); amide adds to either carbon of the benzyne to give a new aryl anion, which takes a proton from ammonia (addition). The mechanism is therefore called the elimination–addition mechanism, exactly the reverse of the addition–elimination of SNAr.

![The benzyne mechanism (elimination–addition). Top: amide removes the H ortho to chlorine, and the aryl anion loses chloride to give benzyne. Bottom: amide adds to one carbon of the benzyne, and the aryl anion formed takes a proton from ammonia. When the chlorine on the labeled carbon (*) is replaced, half of the amino groups end up on the labeled carbon and half on the adjacent carbon](./plots/benzyne.py)

### 15.1.2. Structure

Benzyne is not a molecule with a true C≡C triple bond: a six-membered ring cannot accommodate a $180^\circ$ sp bond angle. The σ framework of the ring is essentially unchanged, and the extra bond of the "triple bond" is formed by sideways overlap, inside the plane of the ring, of the sp² orbitals on two adjacent carbons that were formerly bonded to hydrogen. These two orbitals diverge from each other by about $60^\circ$ and overlap poorly, so this "π bond" is very weak and its LUMO is very low in energy; benzyne is a very strong electrophile and dienophile. This in-plane bond is orthogonal to the aromatic π system, and the aromaticity is unchanged.

Benzyne was once thought to exist only as an intermediate. In 1992 its infrared spectrum was measured in an argon matrix at 8 K (the stretching vibration of the "triple bond" at about $1846\,\mathrm{cm^{-1}}$, between that of an ordinary double and triple bond); Warmuth (1997) photolyzed a benzyne precursor enclosed in a molecular container (a hemicarcerand) and measured the NMR spectrum of benzyne at $-198\,^\circ\mathrm{C}$. Rotational spectroscopy gives a C1–C2 bond length of about $124\,\mathrm{pm}$, much shorter than the $139\,\mathrm{pm}$ of benzene and close to that of a triple bond ($120\,\mathrm{pm}$).

### 15.1.3. Generation of Benzyne

| Method | Precursor and conditions | Comment |
|---|---|---|
| Dehydrohalogenation | Haloarene + $\ce{NaNH2}$/$\ce{NH3}$, PhLi, LDA | The earliest method; very strongly basic, poor functional group tolerance |
| Elimination from an o-haloarylmetal | 1-Bromo-2-fluorobenzene + Mg or $n$-BuLi, $-78\,^\circ\mathrm{C}$ | The o-fluoroaryllithium or Grignard reagent formed loses $\ce{LiF}$ |
| Loss of neutral molecules | Diazotization of 2-aminobenzoic acid gives the diazonium carboxylate zwitterion, which loses $\ce{N2}$ and $\ce{CO2}$ on heating | Neutral conditions; the dry diazonium carboxylate can explode |
| Fluoride-induced (Kobayashi, 1983) | 2-(Trimethylsilyl)phenyl trifluoromethanesulfonate + CsF or TBAF, room temperature | Most commonly used now; $\ce{F-}$ attacks Si (the Si–F bond is very strong, [6.5.27](/6.5.27#sec-27.5.2)) and triflate leaves |
| Hexadehydro-Diels–Alder (Hoye, 2012) | Intramolecular [4+2] cycloaddition of a 1,3-diyne with an alkyne, on heating | No reagent needed; gives polysubstituted arynes |

```smiles
Nc1ccccc1C(=O)O>>[N+](#N)c1ccccc1C(=O)[O-]
```

![Two ways of generating benzyne under neutral conditions. Top: the Kobayashi precursor: fluoride attacks the silicon of 2-(trimethylsilyl)phenyl triflate, the electrons of the C–Si bond form the in-plane bond of benzyne, and triflate leaves at the same time. Bottom: benzenediazonium-2-carboxylate (from diazotization of anthranilic acid) fragments on heating: the carboxylate becomes CO₂, the electrons of the C–C bond form the in-plane bond, and N₂ leaves](./plots/benzyne-generation.py)

### 15.1.4. Reactions of Benzyne

The LUMO of benzyne is very low, and it reacts rapidly with nucleophiles and dienes of all kinds:

- Nucleophilic addition: $\ce{NH2-}$, $\ce{RO-}$, $\ce{RS-}$, enolates and organolithiums all add to benzyne, and the aryl anion formed is protonated or trapped by an electrophile.
- **Diels–Alder reaction**: benzyne is a very strong dienophile; with furan it gives 1,4-epoxy-1,4-dihydronaphthalene, with anthracene it adds at the 9,10 positions to give triptycene (9,10-dihydro-9,10-[1,2]benzenoanthracene), and with cyclopentadiene it gives benzonorbornadiene ([6.5.12](/6.5.12#sec-12.4.3)).
- Dimerization: in the absence of a trapping agent, benzyne dimerizes to biphenylene.

The reaction schemes below represent benzyne generated in situ from a Kobayashi precursor (with CsF):

```smiles
C[Si](C)(C)c1ccccc1OS(=O)(=O)C(F)(F)F.o1cccc1>>C1=CC2OC1c1ccccc12
C[Si](C)(C)c1ccccc1OS(=O)(=O)C(F)(F)F.c1ccc2cc3ccccc3cc2c1>>c1ccc2c(c1)C1c3ccccc3C2c2ccccc21
```

![Diels–Alder reaction of benzyne, acting as the dienophile, with furan: the low-lying in-plane π bond of benzyne and the diene of furan form both bonds in one concerted step through a cyclic transition state (three curved arrows), giving 1,4-epoxy-1,4-dihydronaphthalene](./plots/benzyne-furan.py)

### 15.1.5. Regioselectivity

Substituted benzynes add nucleophiles with two possible orientations. Three examples:

| Haloarene (+ $\ce{NaNH2}$/$\ce{NH3}$) | Benzyne | Product |
|---|---|---|
| 2-Chlorotoluene | 3-Methylbenzyne | Mixture of meta- and ortho-toluidine (no marked selectivity) |
| 1-Chloro-2-(trifluoromethyl)benzene | 3-(Trifluoromethyl)benzyne | Only 3-(trifluoromethyl)aniline (meta) |
| 2-Chloroanisole | 3-Methoxybenzyne | Only 3-methoxyaniline (meta) |

Two effects determine the orientation. The first is elimination: an electron-withdrawing group ($\ce{CF3}$) makes the adjacent H more acidic, and in substrates such as 1-chloro-3-(trifluoromethyl)benzene this determines from which side the benzyne is formed: H2, between Cl and $\ce{CF3}$, is the most acidic, so 3-(trifluoromethyl)benzyne forms and only 3-(trifluoromethyl)aniline is obtained. The second is addition: after nucleophilic addition, the negative charge remains in an sp² orbital of the other carbon (in the plane of the ring, orthogonal to the π system), which cannot delocalize by resonance and can be stabilized only by inductive effects; the closer the negative charge is to an electron-withdrawing group, the better. For a 3-substituted benzyne, the nucleophile adds to C1, farther from the substituent, leaving the negative charge on C2 next to the substituent, stabilized by the $-$I effect of $\ce{CF3}$ or $\ce{OCH3}$, and the meta product results. $\ce{OCH3}$ is electron-donating toward the aromatic ring ($+$M), but its conjugation plays no role here and only the inductive effect operates, so it behaves like $\ce{CF3}$; the inductive effect of methyl is weak, and there is almost no selectivity.

![Regioselectivity of addition to substituted benzynes. First figure: 3-methoxybenzyne and amide ion. Top (observed): NH₂⁻ adds to C1, remote from OCH₃, and the new aryl anion is left on C2, right next to OCH₃ (its lone pair is in an in-plane sp² orbital and is stabilized only by the −I effect); protonation gives 3-methoxyaniline only. Bottom (not observed): addition to C2 would leave the negative charge on C1, far from OCH₃. Second figure: in 1-chloro-3-(trifluoromethyl)benzene, H2, between Cl and CF₃, is the most acidic; elimination gives 3-(trifluoromethyl)benzyne, and addition again puts the negative charge next to CF₃, so only 3-(trifluoromethyl)aniline forms](./plots/benzyne-regio.py)

Garg, Houk and coworkers (from 2010) explained these results in a unified way with the "aryne distortion model": an electronegative substituent at the 3 position distorts the geometry of the benzyne, so that the bond angle at C1 is larger and closer to linear, the orbital at C1 has more p character, and the nucleophile preferentially attacks this "flatter" carbon. 3-Halo and 3-silyl arynes designed on this basis give products with high regioselectivity, and arynes have thus become common intermediates in the synthesis of polysubstituted aromatic rings and natural products.

## 15.2. Reduction of Arenes

### 15.2.1. Catalytic Hydrogenation

Catalytic hydrogenation of the aromatic ring is much more difficult than that of alkenes ([6.5.13](/6.5.13#sec-13.1.2): the first hydrogenation step of benzene is endothermic). Benzene needs about $175\,^\circ\mathrm{C}$ and $18\,\mathrm{MPa}$ over Ni to be hydrogenated to cyclohexane; with Rh/C, Ru/C or $\ce{PtO2}$ the conditions can be milder. Once the reaction begins, the intermediate cyclohexadiene and cyclohexene are hydrogenated more readily than benzene, so the reaction cannot be stopped at an intermediate stage. Because the aromatic ring is hard to hydrogenate, C=C, C≡C, C=O and $\ce{NO2}$ in the molecule can be selectively reduced in the presence of the ring (Pd/C, room temperature and atmospheric pressure), and styrene can be selectively hydrogenated to ethylbenzene. Industrially, hydrogenation of benzene gives cyclohexane, which is oxidized to cyclohexanol and cyclohexanone for the production of nylon ([6.5.20](/6.5.20)).

### 15.2.2. Birch Reduction

**Definition 15.2.1 (Birch Reduction)** The reduction of an arene with an alkali metal (Li, Na, K) in liquid ammonia, with an alcohol (ethanol, tert-butyl alcohol) as the proton source, to give a nonconjugated cyclohexa-1,4-diene is called the **Birch reduction** (Birch, 1944).

```smiles
c1ccccc1>>C1=CCC=CC1
```

Alkali metals dissolve in liquid ammonia (boiling point $-33.3\,^\circ\mathrm{C}$) to give a deep blue solution in which the species is the solvated electron $\ce{e-(NH3)}$: the color of the solution is independent of the metal, the conductivity is high, and the solution is paramagnetic. The mechanism is the same as that of the dissolving-metal reduction of alkynes ([6.5.11](/6.5.11#sec-11.12.1)) and has four steps (electron, proton, electron, proton):

1. A solvated electron enters the LUMO of the arene to give a radical anion;
2. the carbanion part of the radical anion takes a proton from the alcohol (ammonia is not acidic enough, $\mathrm{p}K_{\mathrm{a}}$ 41 (DMSO); an alcohol is needed as the proton source) to give a cyclohexadienyl radical;
3. the radical takes up a second electron to give a cyclohexadienyl anion (a pentadienyl anion);
4. this anion is protonated at the central carbon to give cyclohexa-1,4-diene.

![Mechanism of the Birch reduction: electron transfer gives a radical anion, protonation by the alcohol gives a cyclohexadienyl radical, a second electron transfer gives a cyclohexadienyl anion, and this is protonated at the central carbon of the pentadienyl system to give the nonconjugated cyclohexa-1,4-diene](./plots/birch.py)

Why is the nonconjugated 1,4-diene obtained, and not the more stable conjugated 1,3-diene? The last step is under kinetic control (**kinetic control**, [6.5.3](/6.5.3#def-3.9.2)): protonation of the pentadienyl anion occurs at the carbon of greatest charge density. The simple Hückel method gives equal coefficients for the nonbonding orbital on C1, C3 and C5 ([Eq. (2.2) of 6.5.2](/6.5.2#eq-2.2), 1/3 of the charge each) and cannot discriminate; more accurate calculations (Birch, Hinde and Radom, 1980) show that the central carbon C3 carries the most negative charge, and the transition state for protonation there is the lowest in energy. The product 1,4-diene isomerizes slowly to the conjugated 1,3-diene only under basic conditions.

Substituents determine the positions of the double bonds (the empirical rules are consistent with the mechanism: electron-withdrawing groups stabilize an adjacent negative charge, and electron-donating groups make the adjacent carbon less able to carry negative charge):

- Electron-donating groups ($\ce{-OCH3}$, alkyl) remain on the double bonds: anisole is reduced to 1-methoxycyclohexa-1,4-diene. This is an enol ether, and hydrolysis with dilute acid gives cyclohex-3-enone, which isomerizes in acid to conjugated cyclohex-2-enone. This is an important method for preparing cyclohexenones from aromatic rings and played a key role in the synthesis of steroid hormones (preparation of 19-nor steroids from the aromatic A ring of estrogens, such as the oral contraceptive norethisterone).
- Electron-withdrawing groups ($\ce{-COOH}$, $\ce{-COOR}$) remain on the sp³ carbon: benzoic acid is reduced to cyclohexa-2,5-diene-1-carboxylic acid.

```smiles
COc1ccccc1>>COC1=CCC=CC1
COC1=CCC=CC1>>O=C1CCCC=C1
OC(=O)c1ccccc1>>OC(=O)C1C=CCC=C1
```

![Cyclohexenones from anisole. Birch reduction leaves the donor OCH₃ on a double bond, and the resulting 1-methoxycyclohexa-1,4-diene is an enol ether: in dilute acid, pushed by the oxygen lone pair, the enol ether double bond is protonated at C2 to give an oxocarbenium ion; water adds to C1, and the hemiacetal loses methanol to give cyclohex-3-enone; stronger acid moves the double bond into conjugation through the enol, giving cyclohex-2-enone](./plots/birch-anisole.py)

A C=C conjugated with a benzene ring is reduced before the aromatic ring; an isolated C=C not conjugated with the benzene ring is not reduced (its LUMO is too high).

Reductive alkylation of the Birch reduction. If an alkyl halide is used in place of the proton source to trap the final carbanion, an alkyl group can be introduced at an sp³ carbon: a benzoate ester (or benzamide) is reduced in Na/$\ce{NH3}$ to an enolate (a carbonyl-stabilized pentadienyl anion), which then reacts with an alkyl halide to form a quaternary carbon center at the carbon that originally bore the ester group (Schultz and coworkers achieved asymmetric reductive alkylation with chiral benzamides).

The handling of liquid ammonia and alkali metals is hazardous, and methods that avoid liquid ammonia have recently been developed: Li with ethylenediamine in THF (a modification of the Benkeser reduction), and "electrochemical Birch reduction", in which solvated electrons are generated electrochemically at room temperature (Baran and coworkers, *Science* 2019), which opens the way to large-scale use of this reaction, now more than 70 years old.

## 15.3. Radical Addition

Benzene and chlorine undergo radical chain addition under ultraviolet irradiation (without a Lewis acid) (for the mechanism of chain reactions see [6.5.7](/6.5.7#sec-7.6)), adding three molecules of $\ce{Cl2}$ at a time to give 1,2,3,4,5,6-hexachlorocyclohexane $\ce{C6H6Cl6}$ (hexachlorocyclohexane, HCH). The intermediate dichlorocyclohexadiene and tetrachlorocyclohexene are much more reactive than benzene, so the addition does not stop at an intermediate stage.

```smiles
c1ccccc1.ClCl>>ClC1C(Cl)C(Cl)C(Cl)C(Cl)C1Cl
```

The product is a mixture of 8 stereoisomers, of which the γ isomer (lindane, with three Cl axial and three equatorial) has the highest insecticidal activity and the β isomer (all six Cl equatorial) is the most stable (for **conformational analysis** see [6.5.4](/6.5.4#sec-4.6.3)). HCH was used in large quantities as an insecticide in the mid-twentieth century; it is chemically stable and highly lipophilic and accumulates in the environment and the food chain. Its contemporary DDT was the main target of Rachel Carson's *Silent Spring* (1962), a book that helped bring about the modern environmental movement. α-HCH, β-HCH and lindane were listed in Annex A (elimination) of the Stockholm Convention on Persistent Organic Pollutants in 2009 (the 12 persistent organic pollutants first listed when the convention was signed in 2001 did not include HCH). China stopped producing HCH in 1983.

## 15.4. Reactions at the Benzylic Position

### 15.4.1. The Benzylic Position and Benzylic Resonance

The saturated carbon directly attached to an aromatic ring is called the *benzylic position*. For a radical, cation or anion formed at a benzylic carbon, the p orbital (or the orbital containing the lone pair) overlaps in parallel with the π system of the ring, and the unpaired electron, positive charge or negative charge is delocalized onto the ortho and para positions of the ring. This stabilization is similar to that of the allyl group ([6.5.2](/6.5.2#sec-2.2.2)), but the delocalization of the benzyl group puts the charge on the ring, where bond formation would destroy aromaticity, so benzylic systems react only at the benzylic carbon, whereas both ends of an allyl system can react ([6.5.7](/6.5.7#sec-7.8)).

| Benzylic species | Manifestation of stability |
|---|---|
| Radical | The **bond dissociation energy** of the benzylic C–H bond of toluene is about $375\,\mathrm{kJ\,mol^{-1}}$ ($90\,\mathrm{kcal\,mol^{-1}}$), about $50\,\mathrm{kJ\,mol^{-1}}$ less than the C–H of ethane ($423$) (table in [6.5.7](/6.5.7#sec-7.3.1)) |
| Cation | SN1 solvolysis of benzyl chloride is much faster than that of primary alkyl halides; the p-methoxybenzyl cation is more stable still |
| Anion | The $\mathrm{p}K_{\mathrm{a}}$ of toluene is about 43 (DMSO), about $10^{13}$ times stronger than methane (about 56); diphenylmethane 32.2, triphenylmethane 30.6 ([Table 3.3 of 6.5.3](/6.5.3#sec-3.1.4)) |

### 15.4.2. Benzylic Radical Halogenation

Toluene undergoes radical substitution at the benzylic position with $\ce{Cl2}$ or $\ce{Br2}$ under light or heat in the absence of a Lewis acid, giving benzyl chloride or bromide; with excess halogen, $\ce{C6H5CHCl2}$ and $\ce{C6H5CCl3}$ are obtained (hydrolyzed to benzaldehyde and benzoic acid, respectively). NBS allows selective monobromination (the Wohl–Ziegler reaction; for its mechanism and selectivity see [6.5.7](/6.5.7#sec-7.8)). Note the correspondence between conditions and products: $\ce{Cl2}$/$\ce{FeCl3}$ (in the dark) substitutes on the ring (**SEAr**, [6.5.14](/6.5.14#sec-14.7)), and $\ce{Cl2}$ with light substitutes on the side chain.

```smiles
Cc1ccccc1>>ClCc1ccccc1
ClCc1ccccc1>>ClC(Cl)c1ccccc1
ClC(Cl)c1ccccc1>>ClC(Cl)(Cl)c1ccccc1
```

![Benzylic radical halogenation. First figure: the four resonance structures of the benzyl radical; the single electron is shared by the benzylic carbon and the ortho and para carbons of the ring, which is why the benzylic C–H bond is weak. Second figure: the two propagation steps of the chain (fishhook arrows): a bromine atom abstracts the benzylic hydrogen, and the benzyl radical then abstracts a bromine atom from Br₂ (kept at a low concentration by NBS), regenerating the bromine atom](./plots/benzylic-radical.py)

### 15.4.3. Nucleophilic Substitution and Elimination at the Benzylic Position

Both **SN1** and **SN2** reactions of benzylic halides are fast ([6.5.8](/6.5.8#sec-8.5.3)). Tertiary benzylic halides (such as 2-chloro-2-phenylpropane) undergo very fast SN1 reaction because the benzyl cation is stabilized by resonance; the SN2 reaction of primary benzylic halides is also faster than that of ordinary primary alkyl halides, because in the SN2 transition state the p orbital of the central carbon (partially bonded to both the nucleophile and the leaving group) is conjugated with the π system of the benzene ring. A para electron-donating group (such as $\ce{OCH3}$) makes even primary benzylic halides tend toward SN1. Elimination at the benzylic position ([6.5.9](/6.5.9#sec-9.5.2)) is also easy: E1 proceeds through the benzyl cation, and in the E2 transition state the double bond being formed is conjugated with the benzene ring, the product being a styrene-type compound conjugated with the ring.

### 15.4.4. Oxidation at the Benzylic Position

Hot $\ce{KMnO4}$ solution or $\ce{Na2Cr2O7}$/$\ce{H2SO4}$ oxidizes the entire side chain of an alkylbenzene, leaving only the carbon attached to the ring and giving benzoic acid; benzoic acid is obtained however long the side chain. The reaction requires at least one H on the benzylic carbon: tert-butylbenzene is not oxidized. Industrially, p-xylene is oxidized with air over Co/Mn salts to terephthalic acid, used to produce poly(ethylene terephthalate) (PET, [6.5.19](/6.5.19#sec-19.5.3)). $\ce{MnO2}$ selectively oxidizes benzylic (and allylic) alcohols to aldehydes or ketones without affecting ordinary alcohols.

```smiles
CCCc1ccccc1>>OC(=O)c1ccccc1
Cc1ccc(C)cc1>>OC(=O)c1ccc(cc1)C(=O)O
OCc1ccccc1>>O=Cc1ccccc1
```

### 15.4.5. The Benzyl Protecting Group

Benzyl ethers $\ce{ROCH2Ph}$ ($\ce{ROBn}$) are stable to acids, bases, oxidants and reducing hydride reagents, but the benzylic C–O bond can be cleaved under neutral conditions by catalytic hydrogenolysis ($\ce{H2}$, Pd/C) to give the original alcohol and toluene. Benzyl is therefore a commonly used **protecting group** for the hydroxy group of alcohols ([6.5.20](/6.5.20#sec-20.8.3)): the alcohol is converted to the benzyl ether with NaH and benzyl bromide, and after the other steps the group is removed by hydrogenolysis. The p-methoxybenzyl group (PMB) can also be removed oxidatively with DDQ, orthogonally to benzyl. The benzyloxycarbonyl group (Cbz, Z) protects amines in the same way and is the classical protecting group of peptide synthesis ([6.5.33](/6.5.33)).

```smiles
OC1CCCCC1>>C(OC1CCCCC1)c1ccccc1
C(OC1CCCCC1)c1ccccc1>>OC1CCCCC1.Cc1ccccc1
```

## 15.5. Polyarylmethanes and Biphenyl

### 15.5.1. Polyarylmethanes

Polyarylmethanes such as diphenylmethane and triphenylmethane are prepared by Friedel–Crafts reactions: benzene with dichloromethane (or benzyl chloride) and $\ce{AlCl3}$ gives diphenylmethane, and benzene with chloroform gives triphenylmethane. They have properties of two kinds: the aromatic rings are activated by the alkyl group and readily undergo SEAr, and the benzylic position is activated by several aromatic rings, so that the C–H bond is weak and acidic and is easily oxidized and substituted. Triphenylmethane is oxidized by $\ce{H2CrO4}$ to triphenylmethanol, gives bromotriphenylmethane with $\ce{Br2}$ under light, and is deprotonated by $\ce{NaNH2}$ to the red sodium triphenylmethanide. The triphenylmethyl radical, discovered by Gomberg (1900), was the first **persistent radical** ([6.5.7](/6.5.7#sec-7.3.4)); the triphenylmethyl cation is a stable carbocation, and triphenylmethyl (trityl, Tr) and 4,4′-dimethoxytrityl (DMTr) are bulky protecting groups for primary alcohols, the latter used in the solid-phase synthesis of nucleic acids ([6.5.33](/6.5.33)).

```smiles
c1ccccc1.ClCCl>>c1ccc(cc1)Cc1ccccc1
c1ccccc1.ClC(Cl)Cl>>c1ccc(cc1)C(c1ccccc1)c1ccccc1
```

### 15.5.2. Biphenyl

The two rings of biphenyl are numbered 1–6 and 1′–6′. Industrially it is obtained by dehydrogenative coupling of benzene at about $700\,^\circ\mathrm{C}$; the classical laboratory methods are the Ullmann reaction (iodoarenes with copper powder, heated) and the Wurtz–Fittig reaction (bromoarenes with sodium), and now the Pd-catalyzed **Suzuki coupling** ([6.5.29](/6.5.29#sec-29.4.3)) is generally used, which can join two different aromatic rings.

```smiles
Ic1ccccc1>>c1ccc(cc1)-c1ccccc1
```

One benzene ring is an activating ortho, para director for the other (conjugation of the π systems), and the two rings can activate each other: nitration of biphenyl gives mainly 4-nitrobiphenyl (the para position is less hindered), with a little 2-nitrobiphenyl. The second nitro group enters the other ring (the nitro group deactivates the ring on which it sits), giving 4,4′-dinitrobiphenyl and 2,4′-dinitrobiphenyl. The two rings of biphenyl are twisted by about $44^\circ$ in the gas phase (a compromise between conjugation and repulsion of the ortho hydrogens); when large substituents are present at the ortho positions rotation is hindered, giving atropisomerism (**axial chirality**, [6.5.5](/6.5.5#sec-5.5.1)).

## 15.6. Fused Arenes

### 15.6.1. Energy and Reactivity

The total resonance energy of fused arenes is greater than that of benzene, but the resonance energy per ring is less than that of benzene (empirical values from heats of combustion or hydrogenation):

| | Benzene | Naphthalene | Anthracene | Phenanthrene |
|---|---|---|---|---|
| Resonance energy / $\mathrm{kJ\,mol^{-1}}$ | 150 | 251 | 352 | 381 |
| Per ring / $\mathrm{kJ\,mol^{-1}}$ | 150 | 126 | 117 | 127 |

(Data converted from 36, 60, 84 and 91 $\mathrm{kcal\,mol^{-1}}$; the reference structure is the same "cyclohexatriene" as in [6.5.13](/6.5.13#sec-13.1.2).) Fused arenes are therefore more reactive than benzene: they undergo SEAr readily, and at certain positions also undergo addition readily, because after addition the remaining part is still one or two complete benzene rings and less aromatic stabilization energy is lost.

### 15.6.2. Naphthalene

Electrophilic substitution of naphthalene occurs mainly at the α position (C1). The σ complex formed by attack at the α position has two resonance structures that keep an intact benzene ring, whereas attack at the β position (C2) has only one; resonance structures that retain a benzene ring are much lower in energy, so the transition state for α attack is lower (kinetic control).

![σ Complexes of naphthalene: attack at C1 (top) gives two resonance structures that keep an intact benzene ring (the positive charge in the other ring being on C2 or C4); attack at C2 (bottom) gives only one such resonance structure. The remaining resonance structures that put the positive charge in the other ring destroy the aromaticity of both rings and contribute less](./plots/naphthalene-sear.py)

```smiles
c1ccc2ccccc2c1>>[O-][N+](=O)c1cccc2ccccc12
c1ccc2ccccc2c1>>Brc1cccc2ccccc12
```

Nitration of naphthalene with mixed acid at room temperature gives 1-nitronaphthalene (about 95%); with bromine in refluxing carbon tetrachloride, 1-bromonaphthalene is obtained without a catalyst. β-Substitution products can be obtained in two cases:

- Sulfonation: at $80\,^\circ\mathrm{C}$ naphthalene-1-sulfonic acid is obtained (kinetic control), and at $160\,^\circ\mathrm{C}$ naphthalene-2-sulfonic acid (thermodynamic control, [6.5.3](/6.5.3#sec-3.9.2)). Sulfonation is reversible, and there is marked steric repulsion between the sulfonic acid group of the 1-isomer and the H on C8 (the peri position), so the 2-isomer is more stable. Naphthalene-2-sulfonic acid is the raw material for β-substituted naphthalenes such as 2-naphthol.
- Large electrophiles: Friedel–Crafts acetylation gives mainly 1-acetylnaphthalene in $\ce{CS2}$, and mainly 2-acetylnaphthalene in nitrobenzene (where the electrophile and solvent form a bulky complex).

Orientation in substituted naphthalenes: an activating group directs substitution into the same ring, in accordance with the directing rules (the activating group of a 1-substituted naphthalene points to C4 (and C2), that of a 2-substituted one to C1); a deactivating group directs substitution into the other ring at C5 or C8.

```smiles
COc1ccc2ccccc2c1>>COc1ccc2ccccc2c1Br
[O-][N+](=O)c1cccc2ccccc12>>[O-][N+](=O)c1cccc2c([N+](=O)[O-])cccc12
```

Oxidation and reduction of naphthalene:

- $\ce{CrO3}$/acetic acid at low temperature ($10$–$15\,^\circ\mathrm{C}$) oxidizes naphthalene to 1,4-naphthoquinone; air over $\ce{V2O5}$ (about $400\,^\circ\mathrm{C}$) oxidizes one ring away completely to give phthalic anhydride, the industrial route to plasticizers and alkyd resins.
- Na/ethanol or Birch reduction reduces naphthalene to 1,4-dihydronaphthalene; catalytic hydrogenation first gives 1,2,3,4-tetrahydronaphthalene (tetralin), and under more forcing conditions ($\ce{H2}$/Pt, heating) decahydronaphthalene (decalin; for cis–trans isomerism see [6.5.4](/6.5.4#sec-4.7.2)).

```smiles
c1ccc2ccccc2c1>>O=C1C=CC(=O)c2ccccc12
c1ccc2ccccc2c1>>O=C1OC(=O)c2ccccc12
c1ccc2ccccc2c1>>C1CCC2CCCCC2C1
```

### 15.6.3. Anthracene and Phenanthrene

The reactions of anthracene and phenanthrene are concentrated at the 9 and 10 positions, because after reaction there two complete benzene rings remain (the least aromatic stabilization energy is lost).

- Anthracene adds bromine at low temperature at the 9 and 10 positions (a 1,4-addition as far as the middle ring is concerned) to give 9,10-dibromo-9,10-dihydroanthracene, which loses HBr on heating to give 9-bromoanthracene. The 9 and 10 positions of anthracene form an excellent diene and undergo Diels–Alder reactions with maleic anhydride and benzyne. Anthracene is oxidized by $\ce{CrO3}$/acetic acid (or $\ce{HNO3}$) to 9,10-anthraquinone. Reduction of 2-ethylanthraquinone and its reoxidation (by air back to the anthraquinone, with formation of $\ce{H2O2}$) is the anthraquinone process for the industrial production of hydrogen peroxide.
- The C9=C10 bond of phenanthrene is much like an isolated double bond ([6.5.13](/6.5.13#sec-13.7.1)): it adds bromine to give 9,10-dibromo-9,10-dihydrophenanthrene, which loses HBr on heating to give 9-bromophenanthrene; it is oxidized by $\ce{CrO3}$/acetic acid to 9,10-phenanthrenequinone; and catalytic hydrogenation gives 9,10-dihydrophenanthrene.

```smiles
c1ccc2cc3ccccc3cc2c1.BrBr>>BrC1c2ccccc2C(Br)c2ccccc12
c1ccc2cc3ccccc3cc2c1.O=C1OC(=O)C=C1>>O=C1OC(=O)C2C1C1c3ccccc3C2c2ccccc21
c1ccc2cc3ccccc3cc2c1>>O=C1c2ccccc2C(=O)c2ccccc12
c1ccc2c(c1)ccc1ccccc12>>O=C1C(=O)c2ccccc2-c2ccccc12
```

### 15.6.4. Polycyclic Aromatic Hydrocarbons and Cancer

**Definition 15.6.1 (Polycyclic Aromatic Hydrocarbon)** A compound containing only carbon and hydrogen and formed by the fusion of two or more aromatic rings is called a **polycyclic aromatic hydrocarbon** (PAH).

PAHs are produced by incomplete combustion of organic matter: grilled and smoked foods, cigarette smoke, car exhaust, forest fires and refuse incineration. In 1775 the surgeon Percivall Pott of St Bartholomew's Hospital in London noticed that chimney sweeps were prone to scrotal cancer, the first association of an environmental chemical with cancer; in the 1930s Kennaway and Cook isolated the strongly carcinogenic benzo[a]pyrene from coal tar.

PAHs themselves are chemically inert, and it is their metabolites in the body that cause cancer. Take benzo[a]pyrene as an example: the cytochrome P450 enzymes in the liver (CYP1A1, CYP1B1), whose proper function is to oxidize lipophilic foreign substances to water-soluble products that are readily excreted, first epoxidize the 7,8 double bond; epoxide hydrolase hydrolyzes the epoxide to the trans-7,8-diol; P450 epoxidizes the 9,10 double bond once more to give the 7,8-diol 9,10-epoxide (BPDE). This epoxide lies in the "bay region" of the molecule, the benzylic carbocation formed on opening is stabilized by resonance over the fused rings, and because of steric hindrance it is not easily detoxified by epoxide hydrolase. It is a very strong electrophile and undergoes nucleophilic substitution with the exocyclic amino group (N2) of guanine in DNA to form a covalent adduct, leading to G→T transversion mutations on replication; in lung cancers of smokers, the mutational hotspots of the tumor suppressor gene *TP53* are exactly the positions to which BPDE preferentially binds. Metabolic activation is common to many carcinogens, and their molecular mechanisms are treated further in biochemistry and molecular biology.

```smiles
c1ccc2c(c1)cc1ccc3cccc4ccc2c1c34>>OC1C(O)c2cc3ccc4cccc5ccc(c2C2OC12)c3c45
```

## 15.7. Structure and Acidity of Phenols

### 15.7.1. Structure

Compounds in which a hydroxy group is attached directly to an aromatic ring are called phenols. The O of phenol is sp² hybridized, and one of its lone pairs is in a p orbital conjugated with the π system of the ring ($+$M): the C–O bond ($136\,\mathrm{pm}$) is shorter than the C–O bond of methanol ($143\,\mathrm{pm}$), the electron density on O is reduced, and the electron density of the ring (especially the ortho and para positions) is raised. Conjugation makes the dipole moment of phenol (gas phase $1.22\,\mathrm{D}$) smaller than that of methanol ($1.70\,\mathrm{D}$): the σ polarization of the C–O bond points toward O while the delocalization of the lone pair points toward the ring, and the two partly cancel (values measured in solution depend on the solvent).

A phenol can be regarded as a kind of stable enol: the keto tautomer of phenol, cyclohexa-2,4-dienone, has lost aromaticity, and the equilibrium lies almost entirely on the phenol side ([6.5.21](/6.5.21#sec-21.2.4)). Many natural products contain phenolic hydroxy groups: capsaicin in chili peppers, resveratrol in grapes and red wine, catechins in tea, the amino acid tyrosine, the neurotransmitters dopamine and epinephrine, and the estrogen estradiol.

### 15.7.2. Acidity

Phenol ($\mathrm{p}K_{\mathrm{a}}$ 9.99) is about $10^6$ times more acidic than cyclohexanol (about 16): the negative charge of the phenoxide ion is delocalized onto the ortho and para positions of the ring ([6.5.3](/6.5.3#sec-3.2)). Substituents on the ring affect the acidity according to their electronic effects (in the Hammett equation $\rho = 2.23$ for phenols, and electron-withdrawing conjugating groups at the para position require $\sigma_p^-$, see [6.5.3](/6.5.3#sec-3.5)).

| Phenol | $\mathrm{p}K_{\mathrm{a}}$ (water, 25 °C; CRC data for values not in Table 3.2) | Comment |
|---|---|---|
| Cyclohexanol | about 16 | No resonance |
| 4-Methylphenol | 10.26 | $+$I, hyperconjugation, slightly weaker |
| 4-Methoxyphenol | 10.21 | $+$M and $-$I nearly balanced |
| Phenol | 9.99 | |
| 4-Chlorophenol | 9.41 | $-$I |
| 3-Nitrophenol | 8.36 | Only $-$I |
| 2-Nitrophenol | 7.23 | $-$M and $-$I; an intramolecular hydrogen bond makes it slightly weaker than the para isomer |
| 4-Nitrophenol | 7.15 | Negative charge delocalized onto the oxygens of the nitro group |
| 2,4-Dinitrophenol | 4.07 | |
| 2,4,6-Trinitrophenol (picric acid) | 0.42 | Strength approaching that of a strong acid |

![Resonance structures of the 4-nitrophenoxide ion: the negative charge on the phenoxide oxygen is delocalized onto the ortho and para carbons of the ring (as in phenoxide itself), and from the para carbon on through the nitro group onto an electronegative oxygen (the nitronate-type structure). A meta nitro group cannot take part in this delocalization and has only its −I effect, so 3-nitrophenol is a much weaker acid](./plots/phenoxide-resonance.py)

Practical consequences of the acidity:

- Phenol dissolves in aqueous NaOH (forming sodium phenoxide) but not in aqueous $\ce{NaHCO3}$ ($\mathrm{p}K_{\mathrm{a}}$ of $\ce{H2CO3}$ is 6.35, and the equilibrium constant is about $10^{-3.6}$, [Example 3.1.1 of 6.5.3](/6.5.3#sec-3.1.2)); carboxylic acids (about 4–5) dissolve in both. This is the method for separating phenols from carboxylic acids. When $\ce{CO2}$ is passed into a sodium phenoxide solution, phenol is liberated again.
- 2,4-Dinitrophenol is a lipid-soluble weak acid that can carry protons across the inner mitochondrial membrane, dissipating the proton gradient that drives ATP synthesis and "uncoupling" oxidative phosphorylation, with the energy lost as heat. It was used as a weight-loss drug in the 1930s and was banned because of fatal hyperthermia.

The phenoxide ion is a weaker base than an alkoxide and also a weaker nucleophile (the negative charge is delocalized). It is an ambident nucleophile: it can react at O (ether and ester formation) or at the ortho and para carbons of the ring (Reimer–Tiemann, Kolbe–Schmitt), depending on the electrophile and conditions.

## 15.8. Reactions of Phenols

### 15.8.1. Electrophilic Substitution

$\ce{-OH}$ (especially $\ce{-O-}$) is one of the strongest activating groups; SEAr of phenol occurs under mild conditions and fast, mainly at the ortho and para positions, is difficult to stop at monosubstitution, and is accompanied by easy oxidation.

- Bromination: phenol and bromine water immediately give a white precipitate of 2,4,6-tribromophenol, with very high sensitivity (about $10\,\mathrm{mg\,L^{-1}}$ can be detected), usable for the determination of phenol in wastewater. Bromination in a nonpolar solvent ($\ce{CS2}$, $\ce{CCl4}$) at low temperature ($0$–$5\,^\circ\mathrm{C}$), where phenol is not ionized, gives mainly 4-bromophenol. $\ce{SO2Cl2}$ or tert-butyl hypochlorite can be used for selective chlorination.
- Nitration: phenol and dilute nitric acid (about 20%) react at room temperature to give 2-nitrophenol and 4-nitrophenol. 2-Nitrophenol (yellow, melting point $45\,^\circ\mathrm{C}$) forms an intramolecular hydrogen bond and is volatile, so it can be separated from 4-nitrophenol (melting point $114\,^\circ\mathrm{C}$, intermolecular hydrogen bonds) by steam distillation. Concentrated nitric acid oxidizes phenol to tar; picric acid is made by sulfonation first and then nitration (the sulfonic acid groups being replaced by nitro groups).
- Sulfonation: at room temperature ($15$–$25\,^\circ\mathrm{C}$) 2-hydroxybenzenesulfonic acid is obtained (kinetic product), and at $80$–$100\,^\circ\mathrm{C}$ 4-hydroxybenzenesulfonic acid (thermodynamic product).
- The Friedel–Crafts reaction is not useful: the phenolic hydroxy group coordinates to $\ce{AlCl3}$, and acylation occurs first on O. C-Acylation of phenols uses the Fries rearrangement (15.8.3). For coupling of phenols with **diazonium salts** (**azo coupling**) see [6.5.24](/6.5.24#sec-24.6.2).

```smiles
Oc1ccccc1>>Oc1c(Br)cc(Br)cc1Br
Oc1ccccc1>>Oc1ccc(Br)cc1
Oc1ccccc1>>Oc1ccccc1[N+](=O)[O-].Oc1ccc(cc1)[N+](=O)[O-]
```

![Bromination of phenol in water needs no Lewis acid: the oxygen lone pair pushes electrons through the ring as in an enol, the para carbon attacks Br₂ and the Br–Br bond breaks heterolytically, giving a protonated cyclohexadienone (an oxonium ion in which every atom has an octet); loss of the proton from C4 restores the ring. In water the reaction does not stop: the ortho positions react in the same way, and 2,4,6-tribromophenol precipitates](./plots/phenol-bromination.py)

### 15.8.2. Ether and Ester Formation

The phenoxide ion undergoes the **Williamson ether synthesis** with alkyl halides ([6.5.10](/6.5.10#sec-10.2.2)); with dimethyl sulfate it gives anisole. The C(aryl)–O bond of aryl ethers is very strong, so cleavage of an ether with HBr or HI always gives a phenol and an alkyl halide, not a haloarene; $\ce{BBr3}$ is the usual reagent for cleaving methyl aryl ethers. Aryl allyl ethers undergo the **Claisen rearrangement** on heating to give 2-allylphenols ([6.5.12](/6.5.12#sec-12.5.6)).

```smiles
Oc1ccccc1.CI>>COc1ccccc1
Oc1ccccc1.COS(=O)(=O)OC>>COc1ccccc1
```

Alcohols can be esterified directly with carboxylic acids under acid catalysis (**Fischer esterification**, [6.5.19](/6.5.19#sec-19.4.1)), whereas phenols are weakly nucleophilic and the equilibrium is unfavorable, so acyl chlorides or anhydrides are generally used, with catalysis by base (pyridine, aqueous NaOH, $\ce{K2CO3}$) or acid ($\ce{H2SO4}$, $\ce{H3PO4}$). Salicylic acid and acetic anhydride under catalysis by a little sulfuric acid give acetylsalicylic acid (aspirin, [6.5.18](/6.5.18#sec-18.7.4)).

```smiles
Oc1ccccc1.CC(=O)Cl>>CC(=O)Oc1ccccc1
OC(=O)c1ccccc1O.CC(=O)OC(C)=O>>CC(=O)Oc1ccccc1C(=O)O
```

### 15.8.3. The Fries Rearrangement

**Definition 15.8.1 (Fries Rearrangement)** The reaction in which a phenolic ester is heated with a Lewis acid ($\ce{AlCl3}$, etc.) and the acyl group migrates from oxygen to the ortho or para position of the aromatic ring, giving an o- or p-hydroxyaryl ketone, is called the **Fries rearrangement** (Fries, 1908).

```smiles
CC(=O)Oc1ccccc1>>CC(=O)c1ccccc1O.CC(=O)c1ccc(O)cc1
```

Mechanism: $\ce{AlCl3}$ coordinates to the carbonyl oxygen (or phenolic oxygen) of the ester, and the C(acyl)–O bond breaks heterolytically to give an acylium ion and an aluminum phenoxide; the acylium ion, within the solvent cage or after entering solution, attacks the aromatic ring activated by $\ce{-OAlCl2}$ (SEAr), and hydrolysis gives the hydroxyaryl ketone.

![Mechanism of the Fries rearrangement: AlCl₃ coordinates to the phenolic oxygen of the ester, the C(acyl)–O bond breaks to give an acylium ion and aluminum phenoxide dichloride; the acylium ion attacks the para (or ortho) position of the ring, the σ complex loses a proton, and hydrolysis gives 4-hydroxyacetophenone](./plots/fries.py)

Temperature determines the product ratio: at lower temperature (below about $60\,^\circ\mathrm{C}$) the para product predominates (kinetic control), and at higher temperature (above $160\,^\circ\mathrm{C}$) the ortho product predominates (thermodynamic control: the carbonyl group of the o-hydroxyaryl ketone forms a stable six-membered chelate ring with O–Al). Is the Fries rearrangement intermolecular or intramolecular? A **crossover experiment** in which two esters (such as 4-methylphenyl acetate and phenyl propanoate) react together ([6.5.3](/6.5.3#def-3.11.1)) shows that at least part of the acylium ions escape the solvent cage and react with another molecule (giving crossover products); the proportion of the intramolecular pathway is often higher in the ortho product. The intermolecular and intramolecular components of the Fries rearrangement therefore depend on the substrate, solvent and temperature. Phenolic esters undergo the photo-Fries rearrangement through radical pairs under ultraviolet irradiation ([6.5.31](/6.5.31)).

### 15.8.4. Color Reaction with FeCl₃

Most phenols form purple, blue or green complexes with aqueous $\ce{FeCl3}$, which can be used to identify phenols; compounds with an **enol** structure (such as ethyl acetoacetate, [6.5.22](/6.5.22#sec-22.7.1)) also give colors. The commonly written equation $\ce{6C6H5OH + FeCl3 -> H3[Fe(OC6H5)6] + 3HCl}$ is only schematic: what is actually formed is Fe(III)–phenoxide complexes whose composition varies with pH and concentration, and the color arises from a charge-transfer transition from phenoxide to Fe(III) (**coordination compounds**, [6.1.5](/6.1.5)).

### 15.8.5. The Reimer–Tiemann Reaction

**Definition 15.8.2 (Reimer–Tiemann Reaction)** The reaction in which a phenol and chloroform are heated in strongly basic aqueous solution to introduce an aldehyde group ortho (and para) to the phenolic hydroxy group, giving a hydroxybenzaldehyde, is called the **Reimer–Tiemann reaction**.

Phenol gives salicylaldehyde (2-hydroxybenzaldehyde, 20%–35%) and a little 4-hydroxybenzaldehyde (8%–12%); the yield is not high, but the procedure is simple. The electrophile is dichlorocarbene ([6.5.11](/6.5.11#sec-11.10.2)): $\ce{OH-}$ removes the proton of chloroform, and the trichloromethyl anion loses $\ce{Cl-}$ (α-elimination) to give $\ce{:CCl2}$; a ring carbon of the phenoxide ion attacks the electron-poor carbene carbon, and the dichloromethyl intermediate formed is hydrolyzed in base to the aldehyde group. The preference for the ortho position is generally attributed to coordination and ion-pair interactions between the phenoxide and the carbene (or its precursor) at the interface of the two phases.

![Mechanism of the Reimer–Tiemann reaction. Top: hydroxide removes the proton of chloroform, and the trichloromethyl anion loses chloride to give dichlorocarbene. Bottom: the ortho carbon of the phenoxide ion attacks dichlorocarbene, tautomerization restores the aromatic ring, and the dichloromethyl group is hydrolyzed in base to the aldehyde group](./plots/reimer-tiemann.py)

### 15.8.6. The Kolbe–Schmitt Reaction

**Definition 15.8.3 (Kolbe–Schmitt Reaction)** The reaction in which dry sodium or potassium phenoxide reacts with carbon dioxide under heat and pressure to give a hydroxybenzoic acid is called the **Kolbe–Schmitt reaction**.

Sodium phenoxide and $\ce{CO2}$ at about $125\,^\circ\mathrm{C}$ under pressure give sodium salicylate, and acidification gives salicylic acid. This is the industrial method of producing salicylic acid (and hence aspirin), and one of the few large-scale reactions in which $\ce{CO2}$ is used as a C1 feedstock.

```smiles
[O-]c1ccccc1.[Na+].O=C=O>>OC(=O)c1ccccc1[O-].[Na+]
```

Mechanism: a ring carbon of the phenoxide ion attacks the carbon of $\ce{CO2}$ ($\ce{CO2}$ is a weak electrophile, and the phenoxide makes the ring highly electron-rich), with Na⁺ coordinating to both the O of the phenoxide and an O of $\ce{CO2}$ and bringing $\ce{CO2}$ to the ortho position; tautomerization then restores the aromatic ring. The sodium salt and lower temperature favor the ortho position; the potassium salt and higher temperature (about $200$–$250\,^\circ\mathrm{C}$) favor the para position (4-hydroxybenzoic acid, used to produce paraben preservatives and liquid-crystal polymers). The larger $\ce{K+}$ chelates the phenoxide oxygen less well, and the carboxylation is reversible, giving the thermodynamically more stable para product at high temperature; the ortho product can also be converted to the para product at high temperature.

![Mechanism of the Kolbe–Schmitt reaction: the ortho carbon of the phenoxide ion attacks the carbon of CO₂, Na⁺ coordinates to the phenoxide oxygen and an oxygen of CO₂ so that carboxylation occurs at the ortho position; the subsequent proton transfer restores the aromatic ring and gives salicylate](./plots/kolbe-schmitt.py)

### 15.8.7. Oxidation to Quinones

Phenols are readily oxidized. Pure phenol is colorless and gradually turns red or brown in air through oxidation. Phenol is oxidized by $\ce{K2Cr2O7}$/$\ce{H2SO4}$ to 1,4-benzoquinone (p-benzoquinone), and further oxidation opens the ring; hydroquinone and catechol are even more easily oxidized to the corresponding quinones. The reversible redox interconversion of quinone and hydroquinone ($\ce{Q + 2H+ + 2e- <=> QH2}$) is the chemical basis of ubiquinone (coenzyme Q) and plastoquinone in biological electron-transport chains; for the chemistry of **quinones** see [6.5.17](/6.5.17#sec-17.8.3). Because most oxidants are colored, oxidation of phenols is not generally used for identification; in nitration, sulfonation and similar reactions the conditions must be controlled so that the phenol is not oxidized.

```smiles
Oc1ccccc1>>O=C1C=CC(=O)C=C1
Oc1ccc(O)cc1>>O=C1C=CC(=O)C=C1
```

Phenols readily donate the hydrogen atom of the O–H bond, and the phenoxyl radical formed is stabilized by resonance, so hindered phenols (such as 2,6-di-tert-butyl-4-methylphenol, BHT) and vitamin E (tocopherol) are effective radical scavengers, used as antioxidants in foods and plastics and protecting cell membranes from lipid peroxidation ([6.5.7](/6.5.7#sec-7.3.3)).

## 15.9. Industrial Syntheses of Phenol

| Method | Reaction | Comment |
|---|---|---|
| Cumene process | Benzene and propene (acidic zeolite catalyst) give cumene; air oxidation to cumene hydroperoxide; acid-catalyzed cleavage to phenol and acetone | The source of most phenol today, with acetone as a coproduct |
| Benzenesulfonate alkali fusion | Sodium benzenesulfonate and molten NaOH at $320$–$350\,^\circ\mathrm{C}$ give sodium phenoxide, then acidification | The earliest industrial method, now obsolete |
| Hydrolysis of chlorobenzene (Dow process) | Chlorobenzene and aqueous NaOH at about $360\,^\circ\mathrm{C}$, $20\,\mathrm{MPa}$ | Under these conditions chlorobenzene without activating groups reacts at least in part through benzyne (isotope-labeled products show ortho substitution), and it is not a typical SNAr |
| Raschig–Hooker process | Benzene, HCl and $\ce{O2}$ over a copper catalyst give chlorobenzene, which is hydrolyzed with steam over $\ce{Ca3(PO4)2}$ at about $425\,^\circ\mathrm{C}$ | HCl is recycled |

The second step of the cumene process is a radical chain **autoxidation** ([6.5.7](/6.5.7#sec-7.3.3)): the tertiary benzylic C–H bond of cumene is very weak, and abstraction of hydrogen by $\ce{O2}$ gives cumene hydroperoxide. The third step is the acid-catalyzed Hock rearrangement: the terminal O of the hydroperoxide is protonated, and as water leaves the phenyl group migrates from C to the electron-poor O (the migratory aptitude of phenyl is high, [6.5.30](/6.5.30)), giving an oxonium ion; addition of water gives a hemiketal, which decomposes to phenol and acetone.

![The Hock rearrangement in the cumene process: the terminal oxygen of cumene hydroperoxide is protonated, and as water leaves the phenyl group migrates to oxygen; the oxonium ion formed combines with water to give a hemiketal, which decomposes to phenol and acetone](./plots/cumene-hock.py)

```smiles
c1ccccc1.C=CC>>CC(C)c1ccccc1
CC(C)c1ccccc1.O=O>>CC(C)(OO)c1ccccc1
CC(C)(OO)c1ccccc1>>Oc1ccccc1.CC(C)=O
```

Preparation of naphthols: alkali fusion of naphthalene-1-sulfonic acid and naphthalene-2-sulfonic acid (15.6.2) gives 1-naphthol and 2-naphthol, respectively; hydrolysis of 1-naphthylamine (naphthalen-1-amine) with dilute sulfuric acid at about $200\,^\circ\mathrm{C}$ under pressure also gives 1-naphthol. In the presence of sodium bisulfite, naphthols and naphthylamines can be interconverted reversibly (the Bucherer reaction).

## 15.10. Aromatization

Reactions that form an aromatic ring from a nonaromatic precursor are called aromatizations. Aromatization gains the aromatic stabilization energy and is usually thermodynamically favorable, so it can serve as the driving force of a synthesis.

- Catalytic dehydrogenation: cyclohexane and cyclohexene are dehydrogenated to benzene on heating over Pt, Pd or Ni; tetralin and decalin are dehydrogenated to naphthalene. Catalytic reforming of petroleum uses Pt catalysts to cyclize and dehydrogenate alkanes to arenes ([6.5.7](/6.5.7#sec-7.9.2)), the main source of arenes. Dehydrogenation can also be accompanied by isomerization, as in the conversion of methylcyclopentane to benzene over Pt.
- Dehydrogenation with oxidants: in the laboratory, DDQ (2,3-dichloro-5,6-dicyano-1,4-benzoquinone), chloranil, sulfur or selenium dehydrogenate dihydro and tetrahydro aromatic rings under mild conditions; DDQ abstracts hydride, and the carbocation formed loses a proton.
- Enzyme-catalyzed aromatization: aromatase (cytochrome P450 family CYP19A1) aromatizes the A ring of androgens (androstenedione, testosterone) to estrogens (estrone, estradiol): after three oxidations the C19 methyl group is removed as formic acid and the A ring becomes a phenol. Aromatase inhibitors (letrozole, anastrozole) treat hormone-receptor-positive breast cancer by blocking the biosynthesis of estrogens.
- Nonbenzenoid aromatic systems: cyclopentadiene and Na give the aromatic cyclopentadienyl anion (with loss of $\ce{H2}$); cycloheptatriene adds $\ce{Br2}$ and then loses HBr to give tropylium bromide ([6.5.13](/6.5.13#sec-13.5.1)).

```smiles
C1CCCCC1>>c1ccccc1
CC1CCCC1>>c1ccccc1
```

## Summary

- Benzyne (Definition 15.1.1): strong bases make haloarenes undergo substitution by elimination–addition, with the $^{14}\mathrm{C}$-labeled products each half and half; the "triple bond" is a weak overlap of two sp² orbitals in the plane of the ring (C1–C2 about $124\,\mathrm{pm}$). Generation: dehydrohalogenation, o-haloarylmetals, diazonium carboxylates, Kobayashi precursor + $\ce{F-}$, hexadehydro-Diels–Alder. Reactions: nucleophilic addition, Diels–Alder (furan, anthracene → triptycene), dimerization. The orientation of addition is determined by the inductive effect near the carbon carrying the negative charge ($\ce{OCH3}$ and $\ce{CF3}$ both give the meta product), or understood through the aryne distortion model.
- Hydrogenation of aromatic rings is harder than that of alkenes and does not stop at intermediate stages. The Birch reduction (Definition 15.2.1): e⁻, H⁺, e⁻, H⁺, with protonation at the central carbon (kinetic control) giving the 1,4-diene; electron-donating groups remain on the double bonds and electron-withdrawing groups on the sp³ carbon; anisole → cyclohexenone; reductive alkylation is possible.
- Benzene and $\ce{Cl2}$ add under light to give hexachlorocyclohexane (the γ isomer is insecticidal and the β isomer the most stable; listed in the Stockholm Convention in 2009).
- Benzylic position (radical BDE about $375\,\mathrm{kJ\,mol^{-1}}$; $\mathrm{p}K_{\mathrm{a}}$ of toluene about 43 (DMSO)): halogenation with light occurs on the side chain and with a Lewis acid on the ring; SN1, SN2 and elimination are all fast; $\ce{KMnO4}$ oxidizes side chains having a benzylic H to COOH; benzyl ethers are deprotected by hydrogenolysis. The benzylic position of polyarylmethanes is more reactive (trityl); biphenyl reacts mainly at the 4 position.
- Fused arenes have a lower resonance energy per ring than benzene; naphthalene undergoes α substitution (two resonance structures retaining a benzene ring), sulfonation at $80\,^\circ\mathrm{C}$ gives α and at $160\,^\circ\mathrm{C}$ β; activating groups direct to the same ring and deactivating groups to the other ring (C5, C8); naphthalene is oxidized to 1,4-naphthoquinone or phthalic anhydride. Anthracene and phenanthrene add and are oxidized at the 9,10 positions. Polycyclic aromatic hydrocarbons (Definition 15.6.1) are activated by P450 and epoxide hydrolase to diol epoxides, which bind covalently to N2 of guanine in DNA and cause cancer.
- Phenols: the lone pair of O is conjugated with the ring; $\mathrm{p}K_{\mathrm{a}}$ 9.99 (electron-withdrawing groups at ortho and para greatly increase the acidity, picric acid 0.42), soluble in NaOH but not in $\ce{NaHCO3}$. SEAr is extremely fast (bromine water → tribromophenol; low temperature, nonpolar solvent → para monobromide); ether and ester formation at O; the Fries rearrangement (Definition 15.8.1, para at low temperature, ortho at high temperature); FeCl₃ color test; Reimer–Tiemann (Definition 15.8.2, $\ce{:CCl2}$, ortho aldehyde); Kolbe–Schmitt (Definition 15.8.3, $\ce{CO2}$, ortho with Na, para at high temperature with K); oxidation to quinones; hindered phenols are antioxidants.
- The industrial synthesis of phenol is mainly the cumene process (autoxidation + Hock rearrangement, with coproduct acetone). Aromatization: catalytic dehydrogenation, DDQ, aromatase (androgens → estrogens).

## Questions

1. Write the products of the following reactions and give reasons: (a) 1-chloro-4-methylbenzene with $\ce{NaNH2}$/$\ce{NH3}$; (b) 2-bromoanisole with $\ce{NaNH2}$/$\ce{NH3}$; (c) 2-bromo-1,3-dimethylbenzene with $\ce{NaNH2}$/$\ce{NH3}$.

   **Answer** (a) Only 4-methylbenzyne can form (the two positions ortho to Cl are equivalent), and $\ce{NH2-}$ adds to the two carbons of the benzyne with almost no selectivity, giving a mixture of 4-methylaniline and 3-methylaniline (about 1∶1). (b) 3-Methoxybenzyne is formed, and $\ce{NH2-}$ adds to the carbon remote from $\ce{OCH3}$, so that the negative charge falls on the carbon next to $\ce{OCH3}$ (stabilized by $-$I), giving only 3-methoxyaniline. (c) Neither position ortho to bromine has an H, so benzyne cannot form and there is no reaction (which is also one of the pieces of evidence for the benzyne mechanism).
2. 1-Chloro-4-(trifluoromethyl)benzene is treated with $\ce{NaNH2}$. Which H is removed preferentially in the elimination step? What is the product?

   **Answer** The two H atoms ortho to Cl (C3 and C5) are equivalent and both are meta to $\ce{CF3}$, so only one benzyne forms: C3≡C4, with $\ce{CF3}$ meta to C3 and para to C4. On addition, a negative charge left on C3, which is nearer to $\ce{CF3}$, is somewhat more stable, so $\ce{NH2-}$ adds slightly preferentially to C4; but the $-$I effect falls off rapidly with distance and C3 (meta) and C4 (para) differ little, so the product is a mixture of comparable amounts of 4-(trifluoromethyl)aniline (which looks like direct substitution) and 3-(trifluoromethyl)aniline. Because $\ce{CF3}$ is not close to either benzyne carbon, the selectivity is much smaller than for 1-chloro-2-(trifluoromethyl)benzene (which gives 3-(trifluoromethyl)benzyne, with $\ce{CF3}$ right next to one benzyne carbon).
3. Why does the Birch reduction need an alcohol as the proton source? Why is the product the nonconjugated cyclohexa-1,4-diene? What does the Birch reduction product of anisole give on treatment with acid?

   **Answer** Liquid ammonia is too weakly acidic ($\mathrm{p}K_{\mathrm{a}}$ 41 in DMSO) to protonate the radical anion effectively, and the radical anion would return its electron to the arene (an unfavorable equilibrium); an alcohol ($\mathrm{p}K_{\mathrm{a}}$ about 16–18) is enough to protonate the carbanion irreversibly without reacting too quickly with the alkali metal. The nonconjugated product results from kinetic control: the final pentadienyl anion is protonated at the central carbon, where the negative charge density is greatest, giving the 1,4-diene; although the conjugated 1,3-diene is more stable, the basicity is insufficient to isomerize it under the reaction conditions. Anisole gives 1-methoxycyclohexa-1,4-diene ($\ce{OCH3}$ on the double bond), an enol ether, which is hydrolyzed by dilute acid to cyclohex-3-enone and isomerizes in strong acid to conjugated cyclohex-2-enone.
4. Methyl benzoate is reduced with Na/$\ce{NH3}$ and tert-butyl alcohol (1 equivalent), and then iodomethane is added. Write the product and the key intermediate.

   **Answer** After two electrons and one proton, the species formed is a pentadienyl anion stabilized by the ester carbonyl group (that is, the enolate of the ester, with the negative charge on C1, which bears the ester group, and on the carbonyl oxygen); it is no longer protonated by the (already used up) alcohol but is alkylated at C1 by iodomethane, giving methyl 1-methylcyclohexa-2,5-diene-1-carboxylate, in which C1 is a quaternary carbon. This is the reductive alkylation of the Birch reduction.
5. How can the following be synthesized from benzene: (a) 4-nitrobenzoic acid; (b) 3-nitrobenzoic acid; (c) 1-phenylpropan-1-ol (a benzylic alcohol)?

   **Answer** (a) Benzene → toluene (Friedel–Crafts methylation), nitration to 4-nitrotoluene (the para isomer separated), then oxidation of the methyl group with $\ce{KMnO4}$ or $\ce{Na2Cr2O7}$/$\ce{H2SO4}$. (b) Oxidize toluene to benzoic acid first (meta directing), then nitrate. (c) Acylation with propanoyl chloride/$\ce{AlCl3}$ gives propiophenone, whose carbonyl group is reduced with $\ce{NaBH4}$ ([6.5.17](/6.5.17)); or propylbenzene is brominated at the benzylic position with NBS and then hydrolyzed (accompanied by elimination).
6. Write the principal resonance structures of the σ complexes formed by attack of phenanthrene at C9 and at C1, and explain why both electrophilic substitution and addition of phenanthrene occur at the 9,10 positions.

   **Answer** On attack at C9, the positive charge is delocalized onto C10 and the whole peripheral ring on which it sits, and in the σ complex formed both outer benzene rings can keep a complete aromatic sextet (when the positive charge is delocalized into one benzene ring, the other remains intact); on attack at C1, the outer ring attacked loses its aromaticity, the positive charge is delocalized into the middle ring and the other outer ring, and at most one intact benzene ring can be retained. The intermediate retaining two benzene rings is the lowest in energy, so the 9 position is the most reactive. The same holds for addition: the 9,10-addition product, 9,10-dihydrophenanthrene, contains two intact benzene rings (a biphenyl structure) and loses the least aromatic stabilization energy (the resonance energy of phenanthrene, 381, less about $2 \times 150$ for biphenyl).
7. Design a crossover experiment to decide whether the Fries rearrangement is intramolecular or intermolecular, and predict the two outcomes.

   **Answer** Mix two esters in equimolar amounts and treat them with $\ce{AlCl3}$ under the same conditions, for example 4-methylphenyl acetate (giving 2-hydroxy-5-methylacetophenone) and phenyl propanoate (giving hydroxypropiophenone). If the reaction were entirely intramolecular, the products would be only these two "original-partner" ketones; if the acylium ion leaves its original molecule, crossover products would also be obtained: hydroxyacetophenone (the acetyl group having gone to phenol) and 2-hydroxy-5-methylpropiophenone. The crossover products are quantified by GC–MS or HPLC. The experimental result is that crossover products are detected, which shows that at least part of the reaction proceeds through free acylium ions (intermolecular); the proportion of crossover products varies with the conditions, which shows that a part also proceeds within the solvent cage.
8. Use $\mathrm{p}K_{\mathrm{a}}$ values to decide: (a) Does phenol dissolve in aqueous $\ce{Na2CO3}$? (b) How can an ether solution of benzoic acid, phenol and toluene be separated?

   **Answer** (a) The $\mathrm{p}K_{\mathrm{a}}$ of $\ce{HCO3-}$, the conjugate acid of $\ce{CO3^2-}$, is 10.33 and that of phenol is 9.99, so $K = 10^{10.33 - 9.99} \approx 2$ and phenol can be partly converted to sodium phenoxide and dissolve (essentially fully so at high concentration); $\ce{NaHCO3}$ ($\ce{H2CO3}$ 6.35), however, cannot dissolve phenol. (b) First extract with aqueous $\ce{NaHCO3}$: benzoic acid (4.20) goes into the aqueous layer as sodium benzoate and is precipitated by acidification; then extract the ether layer with aqueous NaOH: phenol goes into the aqueous layer as sodium phenoxide and is liberated by passing in $\ce{CO2}$ or by acidification; toluene remains in the ether layer.
9. In the cumene process, why does the phenyl group and not the methyl group migrate? What is the product if sec-butylbenzene is used in place of cumene?

   **Answer** In the Hock rearrangement the migrating group moves with its electron pair to the electron-poor oxygen, and in the migration transition state the migrating group carries partial positive charge; the phenyl group can stabilize this positive charge through a bridged transition state of the σ complex (benzenium ion) type, and its migratory aptitude is far greater than that of methyl (for the general rules of migratory aptitude see [6.5.30](/6.5.30)). sec-Butylbenzene is oxidized to 2-phenylbutan-2-yl hydroperoxide, and on rearrangement the phenyl group still migrates, giving phenol and butan-2-one (the migratory aptitude of ethyl is also lower than that of phenyl).
