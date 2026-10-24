---
title: Reduction, Oxidation and Conjugate Addition of Carbonyl Compounds
source_hash: 173653033e2e
---

The preceding chapter, [6.5.16](/6.5.16), discussed **nucleophilic addition** to aldehydes and ketones by type of nucleophilic atom. This chapter begins with the most widely used class, the addition of hydride, that is, the reduction of aldehydes and ketones to alcohols, together with other methods of reducing the carbonyl group to a methylene group or of reductively coupling it to a vicinal diol or an alkene. It then treats the oxidation of aldehydes and ketones (the tests for aldehydes, α-oxidation by $\ce{SeO2}$, and the Baeyer–Villiger oxidation) and the disproportionation of aldehydes without α-H. Finally it discusses the new questions that arise when a carbonyl group is conjugated with a C=C bond: whether a **nucleophile** adds to the carbonyl carbon (**1,2-addition**) or to the β carbon (conjugate addition), and the two special classes of unsaturated carbonyl compounds, quinones and ketenes. To judge oxidation and reduction one uses the oxidation states of carbon from [6.5.1](/6.5.1#sec-1.3.2); the ketyls formed by one-electron reduction continue the chemistry of **radical ions** in [6.5.7](/6.5.7#sec-7.2.3); and the quinone–hydroquinone couple links organic chemistry to the electrochemistry of [6.1.11](/6.1.11) and is the chemical basis of electron-transport chains in living organisms. The chemistry of enols and **enolates** at the α position of the carbonyl group is in [6.5.21](/6.5.21#sec-21.2), and the use of the Michael addition in the **Robinson annulation** is in [6.5.22](/6.5.22#sec-22.5.2).

## 17.1. Hydride Reducing Agents

### 17.1.1. Lithium Aluminum Hydride and Sodium Borohydride

The reduction of aldehydes and ketones to alcohols by metal hydrides is in essence the **nucleophilic addition** of hydride ($\ce{H-}$) to the carbonyl group: aldehydes give primary alcohols and ketones give secondary alcohols. The two most common reagents are lithium aluminum hydride $\ce{LiAlH4}$ (LAH) and sodium borohydride $\ce{NaBH4}$. They are not sources of free $\ce{H-}$ (the $\ce{H-}$ of NaH acts only as a base, not as a **nucleophile**) but transfer hydride to the carbonyl carbon through the Al–H and B–H bonds: the H atoms of tetrahedral $\ce{AlH4-}$ and $\ce{BH4-}$ carry partial negative charge, and as they bond to the carbonyl carbon, the metal cation ($\ce{Li+}$, $\ce{Na+}$) or a proton from the solvent binds to the carbonyl oxygen. Each $\ce{AlH4-}$ or $\ce{BH4-}$ can in principle transfer four hydrides in succession to give a tetraalkoxyaluminate (borate), which on hydrolysis gives the alcohol.

![Reduction of acetone by sodium borohydride in methanol: the electron pair of the B–H bond adds to the carbonyl carbon while the O–H proton of methanol is transferred to the carbonyl oxygen, giving isopropyl alcohol and a methoxyborohydride, which goes on to transfer the remaining B–H bonds](./plots/borohydride.py)

![Reduction of cyclohexanone by lithium aluminum hydride in dry ether: $\ce{Li+}$ coordinates to and activates the carbonyl oxygen (dashed), an Al–H bond pair is transferred to the carbonyl carbon, and an alkoxyaluminate forms; the remaining three Al–H bonds reduce three more ketone molecules, and hydrolysis gives cyclohexanol](./plots/lialh4-ketone.py)

The two reagents differ in reactivity and conditions of use:

| | $\ce{LiAlH4}$ | $\ce{NaBH4}$ |
|---|---|---|
| Solvent | Anhydrous diethyl ether, THF; reacts violently with water and alcohols, releasing $\ce{H2}$ | Methanol, ethanol, water (stable in base; decomposes rapidly in acid) |
| Aldehydes, ketones → alcohols | Yes | Yes (at room temperature) |
| Acyl chlorides → alcohols | Yes | Yes |
| Esters, lactones → alcohols | Yes | Slow or no reaction (the basis of selective reduction of ketones) |
| Carboxylic acids → primary alcohols | Yes | No (carboxylates form) |
| Amides → amines, nitriles → primary amines | Yes | No |
| Opening of epoxides, alkyl halides → alkanes | Yes | Generally no |
| Isolated C=C, C≡C | No | No |
| Nitro groups | Aliphatic nitro compounds → amines | No |
| Workup | Careful successive addition of water, aqueous NaOH, and water (Fieser workup) to decompose the aluminum salts | Dilute acid or water |

$\ce{LiAlH4}$ is highly reactive and poorly selective; $\ce{NaBH4}$ is mild and can reduce aldehydes and ketones alone in the presence of esters, amides, nitriles, nitro groups, and halogens. For example, 4-nitrobenzaldehyde is reduced by $\ce{NaBH4}$ in ethanol to 4-nitrobenzyl alcohol; ethyl 3-oxobutanoate (ethyl acetoacetate) is reduced only at the ketone carbonyl group by $\ce{NaBH4}$, whereas $\ce{LiAlH4}$ reduces both the ketone and the ester to give butane-1,3-diol:

```smiles
CCOC(=O)CC(C)=O>>CCOC(=O)CC(C)O
CCOC(=O)CC(C)=O>>CC(O)CCO
```

Replacing Al–H by alkoxy groups tunes the reactivity and selectivity: lithium tri-tert-butoxyaluminum hydride $\ce{LiAlH(OtBu)3}$ is less reactive and reduces acyl chlorides only as far as the aldehyde. Diisobutylaluminum hydride (DIBAL, $\ce{(i-Bu)2AlH}$) is a neutral, Lewis acidic reducing agent that is soluble in toluene and hexane; it first coordinates to the carbonyl oxygen and then transfers hydride, reduces esters to aldehydes at low temperature ([6.5.19](/6.5.19#sec-19.7)), and cleanly 1,2-reduces α,β-unsaturated ketones to allylic alcohols (Section 17.7).

Borane ($\ce{BH3*THF}$ or $\ce{BH3*SMe2}$) is an electrophilic reducing agent: it is a **Lewis acid** and first coordinates to the electron-rich carbonyl oxygen. Its selectivity is therefore opposite to that of $\ce{NaBH4}$: borane rapidly reduces carboxylic acids (the acid first forms an acyloxyborane with release of $\ce{H2}$, which is then reduced) and amides, but reduces esters more slowly. Borane also undergoes **hydroboration** with isolated C=C bonds ([6.5.11](/6.5.11#sec-11.4.6)), which gives an organoborane rather than an alkane; to obtain the alkane the C–B bond must additionally be protonolyzed with a carboxylic acid.

### 17.1.2. Stereochemistry of the Reduction of Cyclohexanones

The two faces of the carbonyl group of a substituted cyclohexanone are not equivalent, and hydride can attack from the axial direction (giving an equatorial OH) or from the equatorial direction (giving an axial OH). Take 4-tert-butylcyclohexanone, whose conformation is locked by the tert-butyl group, as an example (the **chair conformation** and the **A value** are in [6.5.4](/6.5.4#sec-4.6.1)):

```smiles
CC(C)(C)C1CCC(=O)CC1>>CC(C)(C)[C@H]1CC[C@H](O)CC1
CC(C)(C)C1CCC(=O)CC1>>CC(C)(C)[C@H]1CC[C@@H](O)CC1
```

| Reducing agent | trans (OH equatorial) : cis (OH axial) | Main direction of attack |
|---|---|---|
| $\ce{LiAlH4}$ | about 90:10 | Axial |
| $\ce{NaBH4}$ | about 85:15 | Axial |
| L-Selectride ($\ce{LiBH(\mathit{s}-Bu)3}$) | about 7:93 | Equatorial |
| $\ce{Al(O\mathit{i}Pr)3}$/isopropyl alcohol (MPV, equilibrium) | about 80:20 | **Thermodynamic control** |

Small hydride reagents attack preferentially from the axial direction and give the thermodynamically more stable equatorial alcohol. The axial direction of attack approaches the axial H atoms at C3 and C5 and seems more crowded; it is favored because, in attack from the equatorial direction along the **Bürgi–Dunitz angle**, the forming C–H bond almost eclipses the axial C–H bonds at C2 and C6, which gives rise to **torsional strain** (Felkin, 1968), whereas such eclipsing is absent in axial attack. Cieplak and others also proposed an orbital explanation (interaction of the forming bond with the **antiperiplanar** C–H σ orbitals), which is still debated, but both point to the same experimental fact. The very bulky lithium tri-sec-butylborohydride (L-Selectride) suffers severe clashes with the axial H atoms at C3 and C5 in axial attack, so it attacks from the equatorial direction and gives the axial alcohol (the less stable product under **kinetic control**). The axial attack of sulfur **ylides** ([6.5.16](/6.5.16#sec-16.8.3)) has the same origin.

![The two directions of attack on the chair of 4-tert-butylcyclohexanone: small hydride donors ($\ce{LiAlH4}$, $\ce{NaBH4}$) attack from the axial direction (below), avoiding eclipsing with the axial C–H bonds on C2 and C6, and give the equatorial alcohol; bulky L-Selectride avoids the axial hydrogens on C3 and C5 (the one on C3 is drawn; that on C5 lies directly behind it) and attacks from the equatorial direction (above), giving the axial alcohol](./plots/axial-attack.py)

In rigid bicyclic ketones, steric hindrance decides. In camphor, the gem-dimethyl group on C7 blocks the exo face of the carbonyl group, so $\ce{LiAlH4}$ can attack only from the endo face, and the main product is isoborneol with an exo OH (about 90%) rather than borneol with an endo OH. Norcamphor has no C7 methyl groups, hydride attacks from the more open exo face, and the main product is the endo alcohol.

### 17.1.3. Luche Reduction and Hard–Soft Selectivity

In an α,β-unsaturated ketone both the β carbon and the carbonyl carbon are electrophilic centers (Section 17.6). $\ce{NaBH4}$ alone often gives a mixture of 1,2-reduction (the allylic alcohol) and 1,4-reduction (the saturated ketone, which can be reduced further to the saturated alcohol); when $\ce{CeCl3*7H2O}$ is added in methanol, almost only the allylic alcohol is obtained.

**Definition 17.1.1 (Luche Reduction)** The reduction of an α,β-unsaturated aldehyde or ketone with $\ce{NaBH4}$ in methanol in the presence of $\ce{CeCl3}$, which selectively gives the allylic alcohol (1,2-reduction), is called the **Luche reduction**.

```smiles
O=C1C=CCCC1>>OC1C=CCCC1
```

![Luche reduction: the methoxyborohydride $\ce{HB(OMe)3-}$ formed under $\ce{Ce^3+}$ catalysis is a harder hydride donor; methanol bound to $\ce{Ce^3+}$ becomes more acidic and hydrogen-bonds to the carbonyl oxygen (dashed). The hydride adds to the carbonyl carbon (the hard site) and the carbonyl oxygen takes the proton from the activated methanol, giving the allylic alcohol](./plots/luche.py)

$\ce{Ce^3+}$ acts in two ways (Luche's studies of 1978–1981): (1) it catalyzes the reaction of $\ce{BH4-}$ with methanol to give methoxyborohydrides such as $\ce{HB(OMe)3-}$, which by the principle of **hard and soft acids and bases** are "harder" than $\ce{BH4-}$ and prefer to attack the carbonyl carbon, where charge is concentrated (a hard site), rather than the β carbon, where the orbital coefficient is large (a soft site); (2) lanthanide ions are hard Lewis acids, and NMR studies show that they coordinate preferentially to the solvent methanol rather than to the carbonyl group, and the coordinated methanol, being more acidic, activates the carbonyl oxygen by **hydrogen bonding**. The Luche conditions show another kind of **chemoselectivity**: aldehydes rapidly form **acetals** with methanol under $\ce{Ce^3+}$ catalysis and are not reduced, so a ketone in the same molecule can be reduced selectively in the presence of an aldehyde (the opposite of the usual order of reactivity).

## 17.2. Asymmetric Reduction and the MPV Reduction

### 17.2.1. The CBS Reduction

To reduce a **prochiral** ketone to a **chiral** secondary alcohol, the **Re face** and the Si face of the carbonyl group ([6.5.5](/6.5.5#sec-5.9.2)) must be distinguished. The chiral oxazaborolidine catalysts developed by Corey, Bakshi, and Shibata (1987) can do this.

**Definition 17.2.1 (CBS Reduction)** The enantioselective reduction of a prochiral ketone to a secondary alcohol with a chiral oxazaborolidine derived from proline as catalyst and borane as the hydride source is called the **CBS reduction** (Corey–Bakshi–Shibata reduction).

The catalyst is obtained by condensing (S)-α,α-diphenylprolinol with borane or methylboronic acid. The mechanism is bifunctional: $\ce{BH3}$ coordinates to the lone pair of N of the oxazaborolidine ring and is activated as a stronger hydride donor, while the Lewis acidity of the ring B is increased; the carbonyl oxygen of the ketone then coordinates to ring B, in an orientation that places the large group $\mathrm{R_L}$ of the ketone away from the substituent of the catalyst; hydride is transferred from $\ce{BH3}$ on N to the carbonyl carbon through a six-membered ring **transition state**. Because the ketone can bind in only one orientation, hydride attacks from only one face, the configuration of the product is predictable, and the **enantiomeric excess** ([6.5.5](/6.5.5#sec-5.7.3)) is usually higher than 95%. For example, reduction of 2-chloro-1-(4-fluorophenyl)ethan-1-one with the (S)-CBS catalyst gives (S)-2-chloro-1-(4-fluorophenyl)ethan-1-ol (75%, ee 90%; $\ce{CH2Cl}$ has higher priority than the aryl group, so this is the same face selectivity as in the reduction of acetophenone to (R)-1-phenylethan-1-ol).

```smiles
O=C(CCl)c1ccc(F)cc1>>O[C@H](CCl)c1ccc(F)cc1
```

![CBS reduction of acetophenone: $\ce{BH3}$ is bound to the ring nitrogen of the oxazaborolidine, and the ring boron binds the carbonyl oxygen of the ketone (dashed) on the side that puts the small methyl group near the B-methyl and the large phenyl group away from the catalyst; a B–H hydride is delivered to the carbonyl carbon through a six-membered ring, and workup gives (R)-1-phenylethanol](./plots/cbs.py)

Other important methods of asymmetric reduction are Noyori's chiral Ru–BINAP–diamine catalyzed hydrogenation and transfer hydrogenation (Noyori and Knowles received the 2001 Nobel Prize in Chemistry for hydrogenation by **asymmetric catalysis**, [6.5.29](/6.5.29#sec-29.2.2)) and, increasingly common in industry, enzymatic methods: ketoreductases (KREDs) engineered by directed evolution use NADPH as the hydride source to reduce ketones in water to alcohols of a single **enantiomer**, often with ee greater than 99.5%. The face selectivity of the enzyme is the same thing as the specificity of alcohol dehydrogenase for the pro-R hydrogen in [6.5.5](/6.5.5#sec-5.9.2): the dihydropyridine ring of the coenzyme NAD(P)H transfers one particular hydrogen at C4 as hydride to one particular face of the carbonyl group of the substrate.

### 17.2.2. The Meerwein–Ponndorf–Verley Reduction and the Oppenauer Oxidation

Aluminum isopropoxide reduces aldehydes and ketones to alcohols while itself being oxidized to acetone; the reaction is reversible.

**Definition 17.2.2 (Meerwein–Ponndorf–Verley Reduction)** The reversible reaction in which an aldehyde or ketone is reduced to an alcohol, with isopropyl alcohol as the hydride source and aluminum isopropoxide (or another metal alkoxide) as catalyst, while acetone is formed, is called the **Meerwein–Ponndorf–Verley reduction**, abbreviated MPV reduction. Its reverse, the oxidation of a secondary alcohol to a ketone with acetone or cyclohexanone as hydrogen acceptor under aluminum alkoxide catalysis, is called the **Oppenauer oxidation**.

$$
\ce{R2C=O + (CH3)2CHOH <=>[Al(O\mathit{i}Pr)3] R2CHOH + (CH3)2C=O}
$$
In the mechanism, hydride is transferred in a six-membered ring transition state on aluminum: the carbonyl oxygen of the substrate coordinates to Al, the C–H of an isopropoxide group on the same Al is transferred as hydride to the carbonyl carbon, and the isopropoxide becomes acetone and leaves; the alkoxide of the substrate exchanges with the solvent isopropyl alcohol and regenerates the catalyst.

![Six-membered ring transition state of the MPV reduction: the carbonyl oxygen coordinates to aluminum, and the α-H of an isopropoxide group on aluminum is transferred as hydride to the carbonyl carbon, giving a new aluminum alkoxide and acetone](./plots/mpv.py)

It is an equilibrium whose direction is controlled by **Le Chatelier's principle**: the MPV reduction uses a large amount of isopropyl alcohol as solvent and continually distills off the low-boiling acetone (bp $56\,^\circ\mathrm{C}$) to drive the reduction to completion; the Oppenauer oxidation uses a large amount of acetone (or cyclohexanone or benzoquinone, which have a higher oxidation potential) as hydrogen acceptor and often aluminum tert-butoxide. Because the reaction is equilibrium-controlled, the product is the thermodynamically more stable alcohol (the equatorial alcohol predominates among substituted cyclohexanols). The MPV reduction has excellent **chemoselectivity**: C=C, C≡C, nitro groups, halogens, and esters are unaffected; for example, 2-nitrobenzaldehyde is reduced to 2-nitrobenzyl alcohol and cinnamaldehyde to cinnamyl alcohol. The Oppenauer oxidation was the standard method in the steroid industry for oxidizing 3-hydroxy-Δ⁵-steroids to Δ⁴-3-ketones (for example, the preparation of progesterone and testosterone from cholesterol-type precursors), in which the double bond moves into conjugation. The reducing side reaction of **Grignard reagents** ([6.5.16](/6.5.16#sec-16.7.3)) and the Cannizzaro reaction below are hydride transfers of the same kind.

## 17.3. Other Methods of Reduction

### 17.3.1. Catalytic Hydrogenation

Aldehydes and ketones are hydrogenated to alcohols over catalysts such as Pt, Pd, Ni (Raney Ni), and Ru; for example, benzaldehyde is reduced quantitatively to benzyl alcohol over Pt under hydrogen at $0.2\,\mathrm{MPa}$, and acetone is reduced to isopropyl alcohol over Raney Ni. Hydrogenation of a carbonyl group is usually slower than that of C=C: over Pd, an isolated or conjugated C=C is almost always reduced before an aldehyde or ketone carbonyl group (Section 17.7); to reduce the carbonyl group, Pt, Ru, Raney Ni, or higher pressure is preferred, and aldehydes are easier than ketones. The relative reactivity of an aldehyde group, C=C, and a ketone carbonyl group in nonconjugated systems varies with catalyst and conditions, and there is no universal order. Large quantities of alcohols in industry (such as 1-butanol and 2-ethylhexanol from the products of hydroformylation of aldehydes, and sorbitol from glucose) are produced by catalytic hydrogenation.

### 17.3.2. Dissolving-Metal Reduction and Ketyls

Active metals (Na, Li, K, Mg, Zn) can transfer an electron to the π* orbital of a carbonyl group to give a **radical anion**, the ketyl.

**Definition 17.3.1 (Ketyl)** The radical anion $\ce{R2C^{.}-O-}$ formed when a carbonyl compound accepts one electron is called a **ketyl**.

A ketyl is a kind of **radical ion** ([6.5.7](/6.5.7#sec-7.2.3)), with the unpaired electron mainly on carbon and the negative charge mainly on oxygen. The ketyl of benzophenone (formed from sodium and benzophenone in THF) is deep blue and quite stable, and can be observed by **electron paramagnetic resonance**; it reacts rapidly with water and oxygen, so in the laboratory "sodium–benzophenone" is used to distill solvents such as THF and diethyl ether, and the blue color indicates that the solvent is free of water and oxygen. What becomes of the ketyl depends on the solvent:

- In **protic solvents** (alcohols, or liquid ammonia with added alcohol), the ketyl is protonated to a neutral hydroxyalkyl **radical**, which takes up another electron to become a **carbanion** and is protonated to give the alcohol (unimolecular reduction). Since the reaction proceeds through the carbanion intermediate under equilibrium conditions, substituted cyclohexanones give mainly the thermodynamically stable equatorial alcohol. This method is now rarely used for aldehydes and ketones, but the reduction of esters by sodium–ethanol (the Bouveault–Blanc reduction, [6.5.19](/6.5.19#sec-19.7)) and the **Birch reduction** (Definition 15.2.1) are reactions of the same type.
- In aprotic solvents (benzene, THF), the ketyl concentration is high, two radicals couple at carbon to give the dianion of a vicinal diol, and hydrolysis gives the vicinal diol (bimolecular reduction), the pinacol coupling.

### 17.3.3. Pinacol Coupling and the McMurry Reaction

**Definition 17.3.2 (Pinacol Coupling)** The reaction in which an aldehyde or ketone is reduced by one electron with an active metal or low-valent metal reagent to give a ketyl, two ketyls couple at carbon, and hydrolysis gives a vicinal diol is called **pinacol coupling**.

Acetone reacts with magnesium amalgam in benzene, and coupling through a magnesium bis(ketyl) chelate followed by hydrolysis gives pinacol (2,3-dimethylbutane-2,3-diol), whose **pinacol rearrangement** in acid is in [6.5.10](/6.5.10#sec-10.8); benzophenone gives 1,1,2,2-tetraphenylethane-1,2-diol with sodium. Among modern methods, samarium(II) iodide ($\ce{SmI2}$, Kagan's reagent) in THF at room temperature carries out intramolecular and intermolecular pinacol couplings and ketyl–olefin cyclizations under mild conditions and is widely used in the total synthesis of natural products.

![Pinacol coupling: sodium transfers an electron to benzophenone to give the ketyl (radical anion); the carbon radicals of two ketyls form a bond with their single electrons (fishhook arrows) to give the dianion of the vicinal diol](./plots/pinacol.py)

With a stronger oxophilic reducing agent, low-valent titanium ($\ce{TiCl3}$ or $\ce{TiCl4}$ with $\ce{LiAlH4}$, Zn, Zn–Cu, and so on, generated in situ), the coupling does not stop at the vicinal diol: on heating, the titanium pinacolate on the titanium surface is deoxygenated further to give the alkene and titanium oxides (the strong Ti–O bond is the driving force).

**Definition 17.3.3 (McMurry Reaction)** The reductive coupling of two molecules of aldehyde or ketone (or two carbonyl groups in one molecule) with low-valent titanium to give an alkene is called the **McMurry reaction**.

```smiles
O=C(c1ccccc1)c1ccccc1>>c1ccc(cc1)C(c1ccccc1)=C(c1ccccc1)c1ccccc1
```

The McMurry reaction can synthesize highly congested tetrasubstituted alkenes that are very hard to obtain by other methods (tetraphenylethylene, as well as the tetraphenylethylene skeleton in aggregation-induced emission materials and the overcrowded alkenes in molecular motors, [6.5.5](/6.5.5#sec-5.1.4)), and its intramolecular version can close both large and small rings. Coupling two different ketones gives a mixture of three alkenes unless one of them is in large excess (or one is a diaryl ketone).

### 17.3.4. The Clemmensen Reduction

**Definition 17.3.4 (Clemmensen Reduction)** The reaction in which an aldehyde or ketone is heated with zinc amalgam and concentrated hydrochloric acid and the carbonyl group is reduced to a methylene group is called the **Clemmensen reduction**.

Zinc amalgam is prepared by treating zinc granules with a solution of $\ce{HgCl2}$ in dilute hydrochloric acid; mercury forms an amalgam on the zinc surface and suppresses the side reaction of zinc with acid to evolve hydrogen. The mechanism is still not entirely clear: it does not go through the alcohol (alcohols are not reduced to alkanes under these conditions), and is generally believed to involve **single electron transfer** at the zinc surface through carbenoid organozinc intermediates. It is suited to acid-stable substrates, especially aryl alkyl ketones: **Friedel–Crafts acylation** ([6.5.14](/6.5.14#sec-14.9.3)) followed by Clemmensen reduction is the standard route for introducing a straight-chain alkyl group onto an aromatic ring without rearrangement.

```smiles
O=C(O)CCC(=O)c1ccccc1>>O=C(O)CCCc1ccccc1
```

![One commonly proposed course of the Clemmensen reduction (the mechanism is not settled, and the alcohol is not an intermediate): the protonated ketone takes two electrons from the zinc surface to give an α-hydroxyalkylzinc species; after protonation of the OH, the C–Zn electrons push out water, giving a zinc carbenoid, which two protonations (with electron transfer) turn into the $\ce{CH2}$ group](./plots/clemmensen.py)

The three methods for reducing a carbonyl group to a methylene group are complementary:

| Method | Conditions | Suited to | Not suited to |
|---|---|---|---|
| Clemmensen reduction | Zn(Hg), concentrated HCl, heat | Acid-stable substrates, aryl ketones | **Acetals**, tertiary alcohols, acid-sensitive groups |
| **Wolff–Kishner reduction**, Huang Minlon modification ([6.5.16](/6.5.16#sec-16.9.4)) | $\ce{N2H4}$, KOH, diethylene glycol, about 200 °C | Base-stable substrates | Esters, alkyl halides, base-sensitive groups |
| **Thioacetal**–Raney Ni desulfurization ([6.5.16](/6.5.16#sec-16.6.2)) | Dithiol/$\ce{BF3}$; Raney Ni, ethanol | Neutral conditions, most functional groups | Other sulfur atoms, C=C that Ni can hydrogenate |

## 17.4. The Cannizzaro Reaction

Aldehydes without α-H (formaldehyde, benzaldehyde, 2,2-dimethylpropanal, furfural) cannot undergo **enolization** and disproportionate in concentrated base: one molecule of aldehyde is oxidized to the carboxylate and another is reduced to the alcohol.

**Definition 17.4.1 (Cannizzaro Reaction)** The disproportionation of an aldehyde without α-H in concentrated strong base, in which half is converted into the carboxylate and half into the primary alcohol, is called the **Cannizzaro reaction**.

```smiles
O=Cc1ccccc1.O=Cc1ccccc1>>O=C([O-])c1ccccc1.OCc1ccccc1
```

Mechanism: $\ce{HO-}$ adds to the aldehyde to give a tetrahedral alkoxide (which in concentrated base loses a proton to become a dianion), and its C–H is transferred as hydride to the carbonyl carbon of a second molecule of aldehyde, itself becoming the carboxylic acid; proton transfer between the carboxylic acid and the alkoxide gives the carboxylate and the alcohol and makes the reaction irreversible. Hydride transfer is the rate-determining step, and the rate law is $v = k_3[\ce{RCHO}]^2[\ce{HO-}] + k_4[\ce{RCHO}]^2[\ce{HO-}]^2$, corresponding to the monoanion and the dianion, respectively, as the hydride donor; when the reaction is run in $\ce{D2O}$, the $\ce{CH2}$ of the alcohol formed contains no D, showing that the transferred H comes from another molecule of aldehyde, not from the solvent.

![The Cannizzaro reaction: hydroxide adds to benzaldehyde, and the C–H of the tetrahedral alkoxide is transferred as hydride to the carbonyl carbon of a second molecule of benzaldehyde, giving benzoic acid and benzyl alkoxide, which exchange a proton to give benzoate and benzyl alcohol](./plots/cannizzaro.py)

The crossed Cannizzaro reaction. When two different aldehydes without α-H react together the products are complex; if one of them is formaldehyde, however, then since formaldehyde is the most easily attacked by $\ce{HO-}$, it preferentially becomes the hydride donor and is oxidized to formate, and the other aldehyde is reduced to the alcohol. The industrial synthesis of pentaerythritol (a raw material for alkyd resins and for the explosive PETN) consists of three **aldol reactions** and one crossed Cannizzaro reaction: the three α-H atoms of acetaldehyde undergo aldol addition to formaldehyde in turn, and the resulting 3-hydroxy-2,2-bis(hydroxymethyl)propanal, which has no α-H, is reduced by excess formaldehyde:

```smiles
CC=O.C=O>>OCC(CO)(CO)C=O
OCC(CO)(CO)C=O.C=O>>OCC(CO)(CO)CO.O=C[O-]
```

The intramolecular version of the Cannizzaro reaction is seen in 1,2-dicarbonyl compounds: glyoxal gives glycolate in base, and the analogous reaction of benzil, accompanied by migration of a phenyl group, is the **benzilic acid rearrangement** (Definition 30.4.1).

## 17.5. Oxidation of Aldehydes and Ketones

### 17.5.1. Oxidation of Aldehydes to Carboxylic Acids

The carbonyl carbon of an aldehyde carries an H and is easily oxidized to a carboxylic acid (the oxidation state of carbon rises from +1 to +3). Common oxidants are $\ce{CrO3}$/$\ce{H2SO4}$ (Jones reagent), $\ce{KMnO4}$, $\ce{Ag2O}$, $\ce{H2O2}$, and peroxy acids. In modern synthesis the most widely used is the Pinnick oxidation: $\ce{NaClO2}$ oxidizes aldehydes in a weakly acidic buffer, with 2-methylbut-2-ene to scavenge the by-product HOCl; the conditions are mild and leave C=C and most functional groups untouched. The oxidation of aldehydes mostly proceeds through the hydrate (gem-diol) or a similar adduct, which is then oxidized like an alcohol ([6.5.10](/6.5.10#sec-10.6)); so aldehydes that are extensively hydrated are oxidized more easily. Benzaldehyde standing in air slowly turns into benzoic acid, by a **radical** chain reaction through an acyl radical and a peroxy acid (**autoxidation**, [6.5.7](/6.5.7#sec-7.3.3)).

![Pinnick oxidation: chlorous acid adds to the aldehyde; the adduct fragments in a pericyclic step through a five-membered ring, in which the terminal oxygen of the chlorite takes the aldehydic H, the C–H electrons form the new C=O bond, and the O–Cl electrons leave with chlorine, giving the carboxylic acid and HOCl; 2-methylbut-2-ene removes the HOCl](./plots/pinnick.py)

The carbonyl carbon of a ketone carries no H and is not easily oxidized; strong oxidants (hot concentrated $\ce{HNO3}$, $\ce{KMnO4}$) cleave C–C bonds, and cyclohexanone is oxidized by nitric acid to adipic acid, the industrial route to a monomer of nylon-66.

### 17.5.2. Tollens' Reagent and Fehling's Solution

Two weak oxidants oxidize only the aldehyde group and not alcohol hydroxy groups or C=C, and are used to distinguish aldehydes from ketones:

- *Tollens' reagent*: a solution of silver nitrate in aqueous ammonia, containing colorless $\ce{[Ag(NH3)2]+}$. The aldehyde is oxidized to the ammonium carboxylate and $\ce{Ag+}$ is reduced to metallic silver, which forms a silver mirror on clean glass walls (the "silver mirror test") and otherwise a black precipitate:
$$
\ce{RCHO + 2[Ag(NH3)2]+ + 3HO- -> RCOO- + 2Ag v + 4NH3 + 2H2O}
$$
- *Fehling's solution*: an alkaline solution of copper(II) sulfate and sodium potassium tartrate, in which $\ce{Cu^2+}$ forms a deep blue complex ion with tartrate (preventing precipitation of $\ce{Cu(OH)2}$). Aliphatic aldehydes reduce $\ce{Cu^2+}$ to a brick-red precipitate of $\ce{Cu2O}$; aromatic aldehydes react very slowly and generally do not give a positive test. Benedict's solution, in which sodium citrate replaces the tartrate, is more stable.
$$
\ce{RCHO + 2Cu^2+ + 5HO- -> RCOO- + Cu2O v + 3H2O}
$$

These two reagents (and Benedict's solution) are also used to detect sugars: aldoses such as glucose and α-hydroxy ketones such as fructose (which in base interconvert with aldoses through enediols) both give positive tests and are called reducing sugars ([6.5.32](/6.5.32)). They were historically used to test for sugar in urine; urine and blood glucose tests today use the enzymatic method with glucose oxidase (GOx): in the test strip GOx oxidizes glucose to gluconic acid and produces $\ce{H2O2}$, and a peroxidase then uses $\ce{H2O2}$ to oxidize a chromogen; blood glucose meters use electrochemical sensors based on GOx or glucose dehydrogenase ([6.4.6](/6.4.6)). The enzymatic method is specific for glucose and free of interference from other reducing substances.

### 17.5.3. α-Oxidation with Selenium Dioxide

$\ce{SeO2}$ oxidizes the $\ce{CH2}$ or $\ce{CH3}$ group adjacent to the carbonyl group of an aldehyde or ketone to a carbonyl group, giving 1,2-dicarbonyl compounds (the Riley oxidation, 1932), usually at reflux in aqueous dioxane or acetic acid:

```smiles
O=C1CCCCC1>>O=C1CCCCC1=O
CC(=O)c1ccccc1>>O=CC(=O)c1ccccc1
```

Mechanism: the **enol** form of the aldehyde or ketone attacks the electrophilic Se=O to give an α-keto seleninic acid $\ce{RCOCH(R')Se(O)OH}$; by a [2,3]-**sigmatropic rearrangement** or direct elimination (loss of $\ce{H2O}$ and Se(II)), a C=O bond forms at the α carbon, and selenium is reduced to red elemental selenium. The allylic oxidation of alkenes by $\ce{SeO2}$ ([6.5.11](/6.5.11#sec-11.8.4)) is another reaction of the same reagent; selenium compounds are toxic, and catalytic amounts of $\ce{SeO2}$ with a co-oxidant are now often used.

![α-Oxidation by $\ce{SeO2}$ (Riley oxidation): the enol of cyclohexanone attacks the electrophilic selenium while an Se=O $\pi$ pair moves onto oxygen, and proton transfer gives the α-keto seleninic acid; a [2,3]-sigmatropic shift gives a selenium(II) ester, which eliminates water and elemental selenium to give cyclohexane-1,2-dione](./plots/riley.py)

### 17.5.4. The Baeyer–Villiger Oxidation

When a ketone reacts with a peroxy acid, a substituent on one carbon migrates to oxygen, inserting an oxygen atom between the carbonyl group and that group to give an ester; cyclic ketones give lactones.

**Definition 17.5.1 (Baeyer–Villiger Oxidation)** The reaction in which a ketone (or aldehyde) is treated with a peroxy acid (or hydrogen peroxide and a Lewis acid) and one group attached to the carbonyl group migrates from carbon to oxygen to give an ester (a lactone from a cyclic ketone) is called the **Baeyer–Villiger oxidation**.

Common peroxy acids are meta-chloroperoxybenzoic acid (mCPBA, the commercial material contains about 70%–80%, the rest being 3-chlorobenzoic acid and water, which is safer), trifluoroperacetic acid ($\ce{CF3CO3H}$, the most reactive), and peracetic acid.

```smiles
CC(=O)c1ccccc1>>CC(=O)Oc1ccccc1
O=C1CCCCC1>>O=C1CCCCCO1
CC1CCCCC1=O>>CC1CCCCC(=O)O1
CC(=O)[C@@H](C)c1ccccc1>>CC(=O)O[C@@H](C)c1ccccc1
```

Mechanism. (1) The peroxy acid adds to the (acid-activated) carbonyl group to give a tetrahedral peroxy **hemiketal**, the Criegee intermediate. (2) In the rate-determining step, the electrons of the C–R bond **antiperiplanar** to the O–O bond push R, with its bonding pair, to the adjacent oxygen while the O–O bond undergoes **heterolysis** and carboxylate leaves. (3) The protonated ester loses a proton. Migration is a concerted intramolecular process, so if the migrating group is a **stereocenter**, its configuration is retained (the fourth equation above: (S)-3-phenylbutan-2-one gives (S)-1-phenylethyl acetate with retention of configuration).

![The Baeyer–Villiger oxidation: the peroxy acid adds to the carbonyl group of cyclohexanone to give the Criegee intermediate; the ring C–C bond antiperiplanar to the O–O bond migrates to oxygen and carboxylate leaves; loss of a proton gives ε-caprolactone](./plots/baeyer-villiger.py)

Selectivity of migration. Of the two groups, the one better able to accommodate positive charge migrates preferentially (the migrating group carries partial positive charge in the migration **transition state**), and the approximate **migratory aptitude** order is

$$
\text{tertiary alkyl} > \text{cyclohexyl} > \text{secondary alkyl} > \text{benzyl} > \text{phenyl} > \text{vinyl} > \text{primary alkyl} > \text{methyl}
$$
(the 1993 review by Krow; electron-donating substituents on an aryl group make it migrate faster, for example 4-methoxyphenyl > phenyl > 4-nitrophenyl; the relative order of benzyl, phenyl, and secondary alkyl varies with substrate and conditions). Hydrogen in aldehydes migrates fastest, so aldehydes are usually oxidized to carboxylic acids; but electron-rich aromatic aldehydes (such as 4-hydroxybenzaldehyde) mainly undergo aryl migration to give a formate ester, which on hydrolysis gives the phenol (the Dakin oxidation). Thus acetophenone gives phenyl acetate, and in 2-methylcyclohexanone the oxygen is inserted on the more substituted side, giving 7-methyloxepan-2-one. The Baeyer–Villiger oxidation of cyclohexanone gives ε-caprolactone, the industrial source of the monomer of polycaprolactone (a biodegradable medical polymer). In living organisms, Baeyer–Villiger monooxygenases (BVMOs), which use a flavin peroxide as oxidant and NADPH as reductant, can enantioselectively oxidize **prochiral** cyclic ketones and are used to prepare **chiral** lactones. The Baeyer–Villiger oxidation, as a rearrangement by 1,2-migration to an electron-deficient oxygen, is compared with other rearrangements in [6.5.30](/6.5.30#sec-30.2.2).

![Dakin oxidation: the hydroperoxide anion adds to the carbonyl group of 4-hydroxybenzaldehyde; in the tetrahedral adduct the oxide pushes, the electron-rich aryl group migrates with its bonding pair to the proximal oxygen, and the O–O bond breaks with loss of $\ce{HO-}$, giving an aryl formate, which is hydrolyzed in the base to hydroquinone and formate](./plots/dakin.py)

The cumene process. The industrial co-production of phenol and acetone (the cumene or Hock process) contains a migration of the same kind: benzene and propene give cumene by **Friedel–Crafts alkylation**; the tertiary C–H of cumene is autoxidized by air to cumene hydroperoxide (a radical chain, [6.5.7](/6.5.7#sec-7.3.3)); when the hydroperoxide loses water under acid catalysis, the phenyl group migrates from carbon to the electron-deficient oxygen (the Hock rearrangement), and the oxocarbenium ion formed is hydrolyzed to phenol and acetone.

```smiles
CC(C)c1ccccc1>>CC(C)(OO)c1ccccc1
CC(C)(OO)c1ccccc1>>Oc1ccccc1.CC(C)=O
```

![Hock rearrangement: after protonation of the terminal OH of cumene hydroperoxide, the phenyl group migrates with its bonding pair from carbon to the electron-poor proximal oxygen as water leaves; the oxocarbenium ion adds water to give a hemiketal, which falls apart into phenol and acetone](./plots/hock.py)

## 17.6. Addition to α,β-Unsaturated Aldehydes and Ketones

### 17.6.1. Structure and the Two Electrophilic Positions

Unsaturated aldehydes and ketones fall into three classes according to the relative positions of the C=C bond and the carbonyl group: C=C directly attached to the carbonyl carbon (ketenes $\ce{R2C=C=O}$, Section 17.9), C=C conjugated with the carbonyl group (α,β-unsaturated aldehydes and ketones), and the two separated by a saturated carbon (with properties of the separate alkene and aldehyde or ketone). The C=C and C=O of an α,β-unsaturated aldehyde or ketone form a conjugated **delocalized π bond**, and the **resonance structures** place positive charge on the carbonyl carbon (C1) and the β carbon (C3):

```smiles
C=CC=O.[CH2+]C=C[O-]
```

A **nucleophile** therefore has two positions of attack: **1,2-addition**, to the carbonyl carbon, and conjugate addition to the β carbon (**1,4-addition**). In a calculation of the π orbitals of acrolein by the **Hückel method** of [6.5.2](/6.5.2#sec-2.2) (oxygen parameters $h_{\mathrm{O}} = 1$, $k_{\mathrm{CO}} = 1$), the LUMO has its largest coefficient on the β carbon and the next largest on the carbonyl carbon, whereas charge (electrostatic interaction) is concentrated on the carbonyl carbon. This is the orbital origin of the competition between the two modes of addition.

![π molecular orbitals of acrolein from the Hückel method (Coulomb integral of O taken as α + β, resonance integral of C=O taken as β): energy levels on the left, atomic coefficients of the LUMO on the right. The LUMO has its largest coefficient on the β carbon (C3), where soft nucleophiles attack](./plots/acrolein-huckel.py)

**Definition 17.6.1 (Conjugate Addition)** The reaction in which a nucleophile adds to the β carbon of an α,β-unsaturated carbonyl compound (or another alkene conjugated with an electron-withdrawing group), the negative charge moves by conjugation onto the carbonyl oxygen to give an enolate, and the enolate is then protonated at the α carbon (or combines with another electrophile) is called **conjugate addition**.

The product of conjugate addition is formally the "3,4-addition" (Nu and H add across C=C), but mechanistically it is a 1,4-addition: Nu adds to C4 (counting from oxygen in O=C–C=C) and a proton adds to O1 to give the **enol**, which then converts to the ketone by **tautomerism** ([6.5.21](/6.5.21#sec-21.2)).

![General mechanism of conjugate addition: the nucleophile attacks the β carbon, the π electrons of C=C move to the bond between the α and carbonyl carbons, and the π electrons of C=O move onto oxygen to give the enolate; after protonation of oxygen (or of the α carbon), the enol tautomerizes to the saturated ketone](./plots/conjugate-addition.py)

### 17.6.2. 1,2-Addition versus 1,4-Addition

| Tendency | Nucleophile | Reason |
|---|---|---|
| 1,2-Addition | RLi, $\ce{LiAlH4}$, Luche conditions, most **Grignard reagents** with aldehydes | Hard, fast, and irreversible; attack the carbonyl carbon, which has the larger charge (**kinetic control**) |
| 1,2-Addition | $\ce{NH2OH}$, $\ce{H2NNH2}$, semicarbazide | The crystalline oximes and hydrazones formed precipitate from solution and pull the equilibrium toward the 1,2-product |
| 1,4-Addition | Amines, thiols, $\ce{CN-}$, alcohols (base-catalyzed), stabilized **carbanions** (anions of malonates and acetoacetates) | Soft, or the addition is reversible: the 1,2-adduct returns to the starting materials and finally flows to the 1,4-product, which retains the strong C=O bond (**thermodynamic control**) |
| 1,4-Addition | **Lithium dialkylcuprates** $\ce{R2CuLi}$, Grignard reagents with catalytic Cu(I) | Soft organocopper reagents, reacting through a copper π complex |
| Depends on steric hindrance | Grignard reagents with ketones | 1,4 when the carbonyl group is hindered, 1,2 when it is not |

The 1,4-product retains the strong C=O bond at the expense of the weaker C=C bond and is always thermodynamically more stable; the competition between 1,2- and 1,4-addition is therefore, like the addition to conjugated dienes in [6.5.11](/6.5.11#sec-11.6.2), a matter of kinetic versus thermodynamic control.

### 17.6.3. The Michael Addition

**Definition 17.6.2 (Michael Addition)** The conjugate addition, under base catalysis, of a stabilized carbanion (a Michael donor, such as the anion of a malonate, acetoacetate, nitroalkane, or cyanoacetate) to an α,β-unsaturated carbonyl compound, nitrile, nitroalkene, or similar compound (a Michael acceptor) is called the **Michael addition**.

```smiles
CCOC(=O)CC(=O)OCC.C=CC(C)=O>>CCOC(=O)C(CCC(C)=O)C(=O)OCC
```

The equation above is the Michael addition of diethyl malonate to but-3-en-2-one (methyl vinyl ketone) catalyzed by sodium ethoxide. The $\mathrm{p}K_{\mathrm{a}}$ values of Michael donors lie between 9 and 13 ([Table 3.2 in 6.5.3](/6.5.3#sec-3.1.4): acetylacetone 8.9, ethyl acetoacetate 10.7, diethyl malonate about 13), and an alkoxide, an amine, or DBU in catalytic amounts generates enough anion; the **enolate** formed after the addition (the α-H of the carbonyl group, $\mathrm{p}K_{\mathrm{a}}$ about 19–25) is a stronger base and takes a proton from the solvent or another molecule of donor, regenerating the base that catalyzes the reaction. Michael's earliest example (1887) was the addition of a malonate to ethyl cinnamate; the new C–C bond in the product lies between the donor and the β carbon of the acceptor and often creates a new **stereocenter**. The Michael addition followed by an intramolecular aldol condensation makes up the **Robinson annulation** (Definition 22.5.1), which is extremely important in the synthesis of the six-membered rings of steroids and terpenoids.

![Michael addition: the enolate of diethyl malonate attacks the β carbon of methyl vinyl ketone, the C=C $\pi$ electrons move between the α carbon and the carbonyl carbon, and the C=O $\pi$ electrons move onto oxygen, giving a new enolate; it takes a proton from ethanol and regenerates ethoxide](./plots/michael.py)

The Michael addition is equally important in biological and medicinal chemistry. The conjugate addition of the thiol of glutathione to α,β-unsaturated carbonyl compounds (such as acrolein and NAPQI, a metabolite of acetaminophen) is the main route of cellular detoxification. Many "covalent drugs" are designed with a weak Michael acceptor in the molecule (an acrylamide "warhead") that binds irreversibly and covalently to a cysteine thiol near the active site of the target protein, such as ibrutinib for lymphoma and osimertinib for lung cancer. The asymmetric Michael addition by **organocatalysis** (through iminium or **enamine** intermediates, [6.5.16](/6.5.16#sec-16.9.3)) is one of the core reactions in the work for which MacMillan and List received the 2021 Nobel Prize in Chemistry.

### 17.6.4. Conjugate Addition of Organocopper Reagents

Lithium dialkylcuprates (**Gilman reagents**, $\ce{R2CuLi}$, formed from two equivalents of RLi and CuI, [6.5.10](/6.5.10#sec-10.4.2)) undergo almost exclusively conjugate addition and are the standard method for introducing alkyl, aryl, and alkenyl groups at the β position; Grignard reagents also turn to 1,4-addition in the presence of 1–5 mol% of CuI or $\ce{CuBr*SMe2}$.

```smiles
CC1=CC(=O)CCC1>>CC1(C)CCCC(=O)C1
```

(3-Methylcyclohex-2-en-1-one reacts with $\ce{(CH3)2CuLi}$ to introduce a methyl group at the quaternary carbon, giving 3,3-dimethylcyclohexanone.) The mechanism is not a simple "soft carbanion" addition: d¹⁰ Cu(I) first forms a π complex with the C=C of the α,β-unsaturated ketone (with $\ce{Li+}$ activating the carbonyl group at the same time), then undergoes **oxidative addition** to give a β-copper(III) enolate, and finally **reductive elimination** forms the C–C bond (these elementary steps are in [6.5.28](/6.5.28#sec-28.4.2)). The lithium enolate formed in the conjugate addition can be trapped in situ with an alkyl halide or an aldehyde, introducing two groups at the α and β positions in one operation (tandem conjugate addition–alkylation); Noyori's "three-component coupling" for prostaglandins attaches the two side chains to a cyclopentenone in this way. With copper catalysts bearing **chiral** phosphine ligands, the conjugate addition of Grignard or organozinc reagents can be carried out with high enantioselectivity (Feringa and coworkers).

![Conjugate addition of lithium dimethylcuprate to 3-methylcyclohex-2-en-1-one: after forming a $\pi$ complex with the C=C bond, Cu(I) undergoes oxidative addition to the β-cuprio(III) lithium enolate; in the reductive elimination the Cu–$\ce{CH3}$ electrons form the new C–C bond and the Cu–C electrons return to copper, releasing MeCu; protonation of the lithium enolate gives 3,3-dimethylcyclohexanone](./plots/cuprate.py)

The **cyclopropanation** of α,β-unsaturated ketones by sulfur **ylides** ([6.5.16](/6.5.16#sec-16.8.3)) is another important conjugate addition: stabilized ylides, which add reversibly, finally enter the 1,4-pathway.

## 17.7. Selective Reduction of Unsaturated Aldehydes and Ketones

An α,β-unsaturated aldehyde or ketone has two reducible positions, C=C and C=O, and the choice of reducing agent gives one of three products:

| Product | Method | Remarks |
|---|---|---|
| Allylic alcohol (only C=O reduced) | Luche reduction (Section 17.1.3); DIBAL; $\ce{LiAlH4}$ at low temperature; MPV reduction; 9-BBN | 1,2-Reduction |
| Saturated aldehyde or ketone (only C=C reduced) | $\ce{H2}$, Pd/C (controlled amount of $\ce{H2}$); Li/liquid ammonia; L-Selectride or K-Selectride (most cyclic α,β-unsaturated ketones); Stryker's reagent (a copper hydride) | Conjugate reduction (1,4-reduction) |
| Saturated alcohol (both reduced) | Excess $\ce{H2}$, Pt or Ni; excess $\ce{LiAlH4}$ with heating (cinnamaldehyde) | — |

For cinnamaldehyde, for example, $\ce{NaBH4}$ or $\ce{LiAlH4}$ at $-10\,^\circ\mathrm{C}$ gives cinnamyl alcohol; excess $\ce{LiAlH4}$ in refluxing diethyl ether gives 3-phenylpropan-1-ol (first 1,2-reduction, and the allylic aluminum alkoxide formed then undergoes intramolecular hydroalumination of the neighboring C=C; this is a special case caused by the phenyl group together with the allylic alcohol, and ordinary C=C bonds are not reduced by $\ce{LiAlH4}$). Acrolein is hydrogenated over Ni in succession, first to propanal and then to propan-1-ol; in conjugated systems C=C is catalytically hydrogenated more easily than C=O.

```smiles
O=C/C=C/c1ccccc1>>OC/C=C/c1ccccc1
O=C/C=C/c1ccccc1>>OCCCc1ccccc1
```

Li/liquid ammonia reduction of cyclic α,β-unsaturated ketones (Birch type) first adds an electron to the LUMO to give a **radical anion**, which is protonated at the β carbon and takes up a second electron to give a lithium enolate. In the absence of a proton source this remains as an **enolate** that can be alkylated in situ, and the thermodynamically more stable stereochemistry is formed, the trans ring fusion (Stork's steroid synthesis). Ene reductases (the "Old Yellow Enzyme" family) in living organisms reduce C=C conjugatively in a **stereoselective** manner with flavin and NADPH, another example of biocatalysis.

## 17.8. Quinones

### 17.8.1. Structure and Nomenclature

Quinones are cyclic conjugated diketones: the two carbonyl groups lie in the same six-membered ring, which contains two C=C bonds (or bonds shared with a fused ring), and the whole molecule differs from the corresponding aromatic diphenol (hydroquinone) by only two hydrogen atoms.

**Definition 17.8.1 (Quinone)** A nonaromatic cyclic conjugated diketone derived from an aromatic compound by replacing an even number of CH groups of the aromatic ring by C=O and rearranging the double bonds into conjugation (such as cyclohexa-2,5-diene-1,4-dione) is called a **quinone**.

```smiles
O=C1C=CC(=O)C=C1 1
O=C1C=CC=CC1=O 2
O=C1C=CC(=O)c2ccccc21 3
O=C1c2ccccc2C(=O)c2ccccc12 4
O=C1C(=O)c2ccccc2-c2ccccc21 5
```

| No. | Name | Systematic name |
|---|---|---|
| 1 | 1,4-Benzoquinone (*p*-benzoquinone) | Cyclohexa-2,5-diene-1,4-dione |
| 2 | 1,2-Benzoquinone (*o*-benzoquinone) | Cyclohexa-3,5-diene-1,2-dione |
| 3 | 1,4-Naphthoquinone | Naphthalene-1,4-dione |
| 4 | 9,10-Anthraquinone | Anthracene-9,10-dione |
| 5 | 9,10-Phenanthrenequinone | Phenanthrene-9,10-dione |

There is no **aromaticity** in the quinone ring, and the bond lengths clearly alternate between single and double (in 1,4-benzoquinone C=C $134\,\mathrm{pm}$, C–C $148\,\mathrm{pm}$). Quinones are all colored: 1,4-benzoquinone is yellow and 1,2-benzoquinone is red; their n→π* absorption and the π→π* absorption of the conjugated C=C–C=O extend into the visible region ([6.4.9](/6.4.9)). The anthraquinone skeleton is the parent of natural dyes such as alizarin and of many synthetic dyes, and is also the carrier in the anthraquinone process for the industrial production of hydrogen peroxide (2-ethylanthraquinone is reduced by $\ce{H2}$ to the anthrahydroquinone, which is oxidized back to the anthraquinone by air with release of $\ce{H2O2}$).

### 17.8.2. Addition Reactions of Quinones

Quinones are α,β-unsaturated ketones and also reactive dienophiles:

- Addition to C=C: 1,4-benzoquinone adds $\ce{Br2}$ to give di- or tetrabromides; as an electron-poor dienophile it undergoes the **Diels–Alder reaction** with buta-1,3-diene at room temperature ([6.5.12](/6.5.12#sec-12.4.3)), a classic step for building fused rings in Woodward's syntheses of steroids (1951) and reserpine (1956).
- Addition to C=O: with hydroxylamine, mono- and dioximes are formed. The monoxime of 1,4-benzoquinone and 4-nitrosophenol are two **tautomers** of the same compound (the quinone oxime form predominates in solution). Organometallic reagents add to the carbonyl group to give quinols (4-hydrocarbyl-4-hydroxycyclohexa-2,5-dienones), which in acid undergo the dienone–phenol rearrangement (migration of the hydrocarbyl group to the adjacent carbon) to give hydrocarbyl-substituted benzenediols: the restoration of aromaticity is the driving force.
- Aromatization after conjugate addition: HCl, HCN, amines, and thiols undergo **1,4-addition** to quinones, and the **enol** formed tautomerizes to the aromatic hydroquinone; for example, 1,4-benzoquinone and HCl give 2-chlorobenzene-1,4-diol. The product (a substituted hydroquinone) can be reoxidized to a substituted quinone by unreacted quinone, so the reaction of amines with quinones often gives 2,5-diaminoquinones. In living organisms, quinones among the metabolites of many toxicants and drugs bind covalently to cysteine and lysine of proteins in this way, which is the origin of their toxicity.

```smiles
O=C1C=CC(=O)C=C1.Cl>>Oc1ccc(O)c(Cl)c1
```

![Conjugate addition of HCl to 1,4-benzoquinone: after protonation of one carbonyl oxygen, $\ce{Cl-}$ attacks the β carbon (C3), the C2=C3 $\pi$ electrons move to C1–C2, and the C=O $\pi$ electrons move onto the protonated oxygen, giving an enol; tautomerization of the remaining ketone (the C3–H proton moves to the C4 oxygen) restores aromaticity and gives 2-chlorobenzene-1,4-diol](./plots/quinone-hcl.py)

### 17.8.3. The Quinone–Hydroquinone Couple and Semiquinones

1,4-Benzoquinone (Q) and benzene-1,4-diol (hydroquinone, $\ce{H2Q}$) form a reversible two-electron, two-proton **redox couple**:

$$
\ce{Q + 2H+ + 2e- <=> H2Q}, \qquad E^\circ = +0.699\,\mathrm{V}
$$
(25 °C, versus the standard hydrogen electrode, CRC). According to the **Nernst equation** ([6.1.11](/6.1.11)), at $\mathrm{pH} < \mathrm{p}K_{\mathrm{a1}}$, $E = E^\circ - 0.0592\,\mathrm{V}\times\mathrm{pH} - \frac{0.0592\,\mathrm{V}}{2}\lg\frac{[\ce{H2Q}]}{[\ce{Q}]}$, and the potential falls by $59\,\mathrm{mV}$ per pH unit; above the $\mathrm{p}K_{\mathrm{a}}$ values of the two acid dissociations of hydroquinone (about 9.9 and 11.4), the number of protons taking part decreases and the slope becomes $-29.6\,\mathrm{mV}$ and then 0. Equimolar quinone and hydroquinone form a dark green charge-transfer complex, quinhydrone; in its saturated solution $[\ce{Q}] = [\ce{H2Q}]$, and the potential of a platinum electrode depends only on pH. This is the quinhydrone electrode (a kind of **redox electrode**, [6.3.13](/6.3.13#sec-13.1.4)), formerly used to measure pH.

![Conditional potential of the 1,4-benzoquinone/hydroquinone couple as a function of pH (equal concentrations of quinone and of total reduced forms): the slope is −59 mV/pH below pH 9.9, −30 mV/pH between the two acid dissociation constants, and independent of pH above pH 11.4](./plots/quinone-potential.py)

The two-electron reduction takes place in two steps: the quinone first accepts one electron to give the semiquinone **radical anion** (observable by **electron paramagnetic resonance** in basic solution or aprotic solvents), then accepts one electron and two protons to become hydroquinone; in neutral aqueous solution the semiquinone is protonated to the neutral semiquinone **radical**.

**Definition 17.8.2 (Semiquinone)** The radical intermediate ($\ce{Q^{.-}}$ or $\ce{QH^{.}}$) formed when a quinone accepts one electron (and a proton) is called a **semiquinone**.

```smiles
O=C1C=CC(=O)C=C1>>[O-]c1ccc([O])cc1
[O-]c1ccc([O])cc1>>Oc1ccc(O)cc1
```

The chemistry of quinone, hydroquinone, and semiquinone is central to biological energy conversion: ubiquinone (coenzyme Q₁₀) in the mitochondrial respiratory chain and plastoquinone in photosynthesis act as lipid-soluble carriers of electrons and protons that shuttle between the two sides of the membrane, taking up two protons from one side of the membrane and releasing them on the other side with every two-electron reduction (the Q cycle), thereby building the proton gradient; vitamin K (a 1,4-naphthoquinone) is the cofactor of γ-carboxylation of clotting factors. Quinones with a high oxidation potential are common dehydrogenating oxidants in organic synthesis: 2,3-dichloro-5,6-dicyano-1,4-benzoquinone (DDQ) and tetrachloro-1,4-benzoquinone (chloranil) aromatize hydroaromatic compounds, and DDQ is also used to remove the *p*-methoxybenzyl (PMB) **protecting group**.

## 17.9. Ketenes

**Definition 17.9.1 (Ketene)** A compound $\ce{R2C=C=O}$ containing the cumulated C=C=O structure is called a **ketene**; the simplest is ethenone (ketene itself) $\ce{H2C=C=O}$.

(Ketenes should not be confused with α,β-unsaturated ketones such as cyclohexenone, which are called enones; the term ketene is reserved here for C=C=O compounds.) The central carbon of a ketene is sp-hybridized and, as in allenes, the two π systems of C=C and C=O are perpendicular to each other; the π* orbital of the carbonyl group lies in the molecular plane and has a large coefficient on the central carbon, so a **nucleophile** attacks the central carbon in the molecular plane. Ketene itself is a highly toxic gas with an irritating odor (bp $-56\,^\circ\mathrm{C}$); it is unstable and dimerizes to diketene at room temperature. Preparations:

- Pyrolysis of acetone or acetic acid at $700$–$850\,^\circ\mathrm{C}$ (acetic acid dehydrated over $\ce{AlPO4}$), used industrially to produce acetic anhydride;
- Loss of HCl from acyl chlorides with triethylamine at low temperature (an **E1cB** type elimination; the ketene formed is used in situ);
- The **Wolff rearrangement** of α-diazo ketones (photolysis or Ag(I) catalysis, Definition 24.5.2).

![Ketene formation from an acyl chloride and triethylamine (E1cb): the amine removes the α-H, made acidic by the carbonyl group, to give the enolate; the oxide pushes back to form C=O while chloride leaves from the same carbon, giving methylketene](./plots/ketene-e1cb.py)

Addition of compounds with active hydrogen. Ketene is a strong acylating agent: water, alcohols, amines, carboxylic acids, and HCl all add to the C=O (the nucleophilic atom bonds to the central carbon and H adds to oxygen), and the **enol** formed then undergoes **tautomerism** to acetic acid, acetate esters, acetamide, acetic anhydride, and acetyl chloride. The net effect is to introduce an acetyl group.

![Addition of an alcohol to ketene: the lone pair on the alcohol oxygen attacks the central carbon in the molecular plane, the π electrons of C=O move onto oxygen to give the enolate and the protonated alcohol; proton transfer gives the enol, which tautomerizes to methyl acetate](./plots/ketene-addition.py)

```smiles
C=C=O.OC(C)=O>>CC(=O)OC(C)=O
C=C=O.CC[Mg]Br>>CCC(C)=O
```

After addition of a **Grignard reagent**, hydrolysis of the magnesium enolate formed gives a methyl ketone. The [2+2] **cycloaddition** of ketenes gives cyclobutanones ([6.5.12](/6.5.12#sec-12.4.6)), and the [2+2] addition to **imines** gives β-lactams (the Staudinger reaction, [6.5.25](/6.5.25#sec-25.9.2)).

Diketene. The dimer of ketene is 4-methyleneoxetan-2-one (a β-lactone), called diketene. It undergoes ring-opening acylation with alcohols, amines, and the like to give acetoacetate esters and acetoacetamides, which amounts to introducing a four-carbon acetoacetyl group; the industrial ethyl acetoacetate ([6.5.22](/6.5.22#sec-22.8)) is produced from diketene and ethanol.

```smiles
C=C1CC(=O)O1.CCO>>CCOC(=O)CC(C)=O
```

## Summary

- Hydride reduction: $\ce{LiAlH4}$ is highly reactive and reduces most carbonyl compounds; $\ce{NaBH4}$ is mild and reduces only aldehydes and ketones (and acyl chlorides); DIBAL is Lewis acidic; borane is electrophilic, rapidly reduces carboxylic acids, and undergoes **hydroboration** with C=C. Small reagents attack cyclohexanones axially (avoiding torsional strain) and give equatorial alcohols; L-Selectride attacks equatorially and gives axial alcohols.
- Selective reduction: the Luche reduction (Definition 17.1.1) reduces only C=O; the CBS reduction (Definition 17.2.1) uses a **chiral** oxazaborolidine to distinguish the Re face from the **Si face**; the MPV reduction and the Oppenauer oxidation (Definition 17.2.2) are equilibrium-controlled hydride transfers with excellent **chemoselectivity**.

| Transformation | Method |
|---|---|
| C=O → CH–OH | $\ce{NaBH4}$, $\ce{LiAlH4}$, DIBAL, $\ce{BH3}$, catalytic hydrogenation, MPV, CBS (asymmetric) |
| 2 C=O → vicinal diol | Pinacol coupling (Definition 17.3.2): Mg(Hg), Na (aprotic solvent), $\ce{SmI2}$; through ketyls (Definition 17.3.1) |
| 2 C=O → C=C | McMurry reaction (Definition 17.3.3): low-valent titanium |
| C=O → $\ce{CH2}$ | Clemmensen (Definition 17.3.4, acid), Wolff–Kishner–Huang Minlon (base), **thioacetal**/Raney Ni (neutral) |
| 2 ArCHO → $\ce{ArCOO-}$ + $\ce{ArCH2OH}$ | Cannizzaro reaction (Definition 17.4.1): aldehydes without α-H, concentrated base; crossed with formaldehyde |
| RCHO → RCOOH | Jones, $\ce{KMnO4}$, $\ce{Ag2O}$, Pinnick ($\ce{NaClO2}$); tests: Tollens (silver mirror), Fehling ($\ce{Cu2O}$) |
| $\ce{RCOCH2R'}$ → $\ce{RCOCOR'}$ | $\ce{SeO2}$ (Riley) |
| $\ce{RCOR'}$ → $\ce{RCOOR'}$ | Baeyer–Villiger oxidation (Definition 17.5.1): tertiary alkyl > cyclohexyl > secondary alkyl > benzyl > phenyl > vinyl > primary alkyl > methyl, with retention of configuration |

- α,β-Unsaturated aldehydes and ketones: the LUMO has its largest coefficient on the β carbon and the charge is concentrated on the carbonyl carbon; hard, irreversible **nucleophiles** undergo **1,2-addition** (**kinetic control**), and soft or reversible nucleophiles undergo conjugate addition (Definition 17.6.1, **thermodynamic control**); the Michael addition (Definition 17.6.2) is carried out by stabilized **carbanions**; copper reagents give exclusively **1,4-addition**.
- Quinones (Definition 17.8.1): nonaromatic conjugated diketones, colored; C=C addition, dienophiles, and aromatization after conjugate addition; for Q/$\ce{H2Q}$, $E^\circ = 0.699\,\mathrm{V}$ and the potential changes by $-59\,\mathrm{mV}$ per pH unit; one-electron reduction gives the semiquinone (Definition 17.8.2); ubiquinone and plastoquinone are electron and proton carriers in biological membranes.
- Ketenes (Definition 17.9.1): nucleophiles attack the central carbon in the molecular plane, and ketenes are acetylating agents; diketene is an acetoacetylating agent.

## Questions

1. Camphor is reduced by $\ce{LiAlH4}$ in diethyl ether at 0 °C to give 84.5% isoborneol (exo-OH) and 9.5% borneol (endo-OH). Explain the origin of the selectivity; what is the main product if norcamphor (no C7 methyl groups) is used instead?

   **Answer** The carbonyl group of camphor is at C2, and its exo face points toward the one-carbon bridge C7, which carries two methyl groups; the one on the same side as the carbonyl group blocks the **Bürgi–Dunitz trajectory** from the exo direction. The endo face points toward the two-carbon bridge C5–C6, which has only endo-H atoms and is less hindered. Hydride attacks from the endo face and OH remains on the exo face, giving isoborneol. In norcamphor, C7 carries only H, and the exo face is more open than the endo face (which is blocked by the endo-H atoms at C5 and C6); hydride attacks from the exo face and the main product is endo-norborneol. Both cases are controlled by steric hindrance, in opposite directions.

2. Give synthetic routes: (a) ethyl 4-hydroxypentanoate from ethyl 4-oxopentanoate (without reducing the ester); (b) pentane-1,4-diol from ethyl 4-oxopentanoate; (c) cyclohex-2-en-1-ol from cyclohex-2-en-1-one; (d) cyclohexanone from cyclohex-2-en-1-one.

   **Answer** (a) $\ce{NaBH4}$, ethanol, 0 °C: only the ketone is reduced (the product lactonizes easily to γ-valerolactone in acid, so strong acid must be avoided in the workup). (b) $\ce{LiAlH4}$, THF, then hydrolysis: both the ketone and the ester are reduced. (c) Luche reduction: $\ce{NaBH4}$/$\ce{CeCl3*7H2O}$, methanol (or DIBAL, $-78\,^\circ\mathrm{C}$). (d) $\ce{H2}$ (1 equivalent), Pd/C; or Li/liquid ammonia followed by quenching with $\ce{NH4Cl}$; or conjugate reduction with L-Selectride.

3. The MPV reduction is reversible. How can it be driven to completion in the direction of reduction? How is the Oppenauer oxidation driven to completion? Why does the MPV reduction of 4-tert-butylcyclohexanone give mainly the trans alcohol?

   **Answer** The MPV reduction uses a large amount of isopropyl alcohol as solvent (excess of a reactant) and continually distills off the acetone formed (bp $56\,^\circ\mathrm{C}$, the most volatile component of the system), shifting the equilibrium to the right by **Le Chatelier's principle**. The Oppenauer oxidation conversely uses a large amount of acetone or cyclohexanone (or the more strongly oxidizing benzoquinone) as hydrogen acceptor. Because alcohols and ketones in the MPV system interconvert continually under aluminum catalysis, the product ratio is determined by equilibrium (**thermodynamic control**): the OH of trans-4-tert-butylcyclohexanol is equatorial and more stable than that of the cis isomer (OH axial, with 1,3-diaxial interactions), so the trans alcohol predominates.

4. What is mainly obtained when a mixture of formaldehyde and benzaldehyde reacts in concentrated NaOH? Explain why formaldehyde is the one that is oxidized. Write the steps in the synthesis of pentaerythritol from acetaldehyde and formaldehyde.

   **Answer** Mainly benzyl alcohol and sodium formate. The carbonyl group of formaldehyde has no electron-donating alkyl or aryl group and no steric hindrance, so it adds $\ce{HO-}$ most easily and the tetrahedral anion $\ce{H2C(OH)O-}$ is present at the highest concentration; as the hydride donor it transfers H to benzaldehyde and itself becomes formic acid. Pentaerythritol: in base, the **enolate** of acetaldehyde undergoes aldol addition to three molecules of formaldehyde in succession to give $\ce{(HOCH2)3C-CHO}$ (3-hydroxy-2,2-bis(hydroxymethyl)propanal, which has no α-H); it undergoes a crossed Cannizzaro reaction with a fourth molecule of formaldehyde and is reduced to $\ce{C(CH2OH)4}$, while formaldehyde is oxidized to formate. The overall reaction is $\ce{CH3CHO + 4HCHO + NaOH -> C(CH2OH)4 + HCOONa}$.

5. Predict the main product of each of the following Baeyer–Villiger oxidations (mCPBA): (a) cyclobutanone; (b) 1-cyclohexylethan-1-one; (c) 4-methoxyacetophenone; (d) 1-[(1R,2S)-2-methylcyclopentyl]ethan-1-one (only the migrating group and configuration are asked).

   **Answer** (a) γ-Butyrolactone (oxolan-2-one); the strain of cyclobutanone makes the reaction especially fast, and even $\ce{H2O2}$ can oxidize it. (b) Cyclohexyl acetate: the secondary alkyl group (cyclohexyl) migrates much more readily than methyl. (c) 4-Methoxyphenyl acetate: the electron-rich aryl group migrates in preference to methyl. (d) The secondary alkyl group (cyclopentyl) migrates, giving (1R,2S)-2-methylcyclopentyl acetate: the configuration of the migrating carbon is retained (the **chiral** carbon that bore the acetyl group keeps its spatial arrangement; the newly attached O and the former acetyl group are both the highest-priority group on that carbon, so the CIP descriptor does not change).

6. Draw the mechanism of the acid-catalyzed conversion of cumene hydroperoxide to phenol and acetone, and point out what it has in common with the Baeyer–Villiger oxidation.

   **Answer** (1) The terminal OH of the hydroperoxide is protonated; (2) as water is lost, the phenyl group migrates with its bonding pair from carbon to the electron-deficient oxygen (concerted, avoiding an unstable oxenium ion), giving the oxocarbenium ion $\ce{(CH3)2C=O+-Ph}$ stabilized by the lone pair on oxygen; (3) water attacks the oxocarbenium carbon to give a **hemiketal**; (4) the hemiketal breaks down to phenol and acetone. As in the Baeyer–Villiger oxidation, the key step is the 1,2-migration of a group to an electron-deficient oxygen (the **leaving group** takes the electrons when the O–O bond breaks), and the **migratory aptitude** is determined in both by the ability of the migrating group to accommodate positive charge (phenyl migrates much faster than methyl).

7. Do the following reagents react with 3-methylbut-3-en-2-one ($\ce{CH2=C(CH3)COCH3}$) or cyclohex-2-en-1-one mainly by **1,2-addition** or **1,4-addition**? (a) $\ce{CH3Li}$; (b) $\ce{(CH3)2CuLi}$; (c) $\ce{CH3MgBr}$ + 5 mol% CuI; (d) $\ce{PhSH}$/$\ce{Et3N}$; (e) $\ce{NaBH4}$/$\ce{CeCl3}$; (f) diethylamine.

   **Answer** (a) 1,2-Addition to give a tertiary allylic alcohol (hard, fast, irreversible). (b) 1,4-Addition (copper reagent). (c) 1,4-Addition (catalytic copper converts the **Grignard reagent** into an organocopper species). (d) 1,4-Addition (a soft sulfur **nucleophile**, thia-Michael addition, reversible and under thermodynamic control). (e) 1,2-Reduction to the allylic alcohol (Luche). (f) 1,4-Addition (aza-Michael addition, reversible; the hemiaminal from 1,2-addition returns to the starting materials).

8. Starting from cyclohex-2-en-1-one and diethyl malonate, what compound is obtained after Michael addition, hydrolysis, and **decarboxylation**? Explain why only a catalytic amount of base is needed.

   **Answer** The diethyl malonate anion adds to the β carbon of cyclohexenone to give diethyl 2-(3-oxocyclohexyl)malonate; after acidic hydrolysis of the two ester groups, heating decarboxylates the substituted malonic acid ([6.5.18](/6.5.18#sec-18.4.1)) to give (3-oxocyclohexyl)acetic acid. The enolate formed in the addition is a stronger base than the malonate anion (its conjugate acid is the α-H of the ketone, $\mathrm{p}K_{\mathrm{a}}$ about 19–20, compared with about 13 for diethyl malonate); it takes a proton from another molecule of diethyl malonate or from the solvent ethanol, forming the product and regenerating the malonate anion or ethoxide, so the base is not consumed in the cycle.

9. Using electrode potentials, explain why at pH 7 1,4-benzoquinone can oxidize ascorbic acid (vitamin C), whereas this oxidizing power is weakened in strong base. Calculate the potential of the quinone–hydroquinone couple at pH 7 and $[\ce{Q}] = [\ce{H2Q}]$.

   **Answer** At pH 7, below the $\mathrm{p}K_{\mathrm{a1}}$ of hydroquinone (about 9.9), $E = 0.699 - 0.0592 \times 7 = 0.285\,\mathrm{V}$. The conditional potential of the dehydroascorbic acid/ascorbic acid couple at pH 7 is about $+0.06\,\mathrm{V}$, lower than $0.285\,\mathrm{V}$, so the quinone can oxidize ascorbic acid to dehydroascorbic acid. The potential of the quinone couple falls with increasing pH (59 mV per unit, with a smaller slope above pH 9.9), and in strong base the oxidizing power of the quinone is clearly weakened. Living organisms regulate the potentials of quinones precisely through the uptake and release of protons.

10. What are obtained when ketene reacts with water, methanol, ammonia, acetic acid, HCl, and $\ce{CH3MgBr}$ (followed by hydrolysis)? What about diketene with ethanol? Why is ketene called an "acetylating agent"?

    **Answer** Acetic acid, methyl acetate, acetamide, acetic anhydride, acetyl chloride, and acetone (hydrolysis of the magnesium enolate gives the methyl ketone). Diketene opens with ethanol to give ethyl acetoacetate. In these reactions the $\ce{CH2=C=O}$ unit of ketene combines with H–Nu to give $\ce{CH3C(=O)-Nu}$, that is, an acetyl group is attached to the nucleophilic atom, the same result as with acetyl chloride or acetic anhydride but without a by-product (addition rather than substitution), so ketene is called an acetylating agent; diketene introduces the acetoacetyl group $\ce{CH3COCH2CO-}$.
