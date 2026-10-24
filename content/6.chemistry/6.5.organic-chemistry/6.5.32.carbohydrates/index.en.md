---
title: Carbohydrates
description: Definition and classification of carbohydrates; the structure determination of glucose; configurations of monosaccharides (D/L, Fischer projections, the D-aldose family, epimers); cyclic structures (hemiacetals, anomers, pyranoses and furanoses, Haworth projections and chair conformations, the kinetics of mutarotation, the anomeric effect); reactions of monosaccharides (epimerization and enediols in base, reducing sugars and oxidants, periodate, reduction, osazone formation, Kiliani–Fischer chain extension, Wohl and Ruff degradations, the Seliwanoff test, esterification, etherification and acetal protection of hydroxy groups); Fischer's proof of the configuration of glucose; glycosides and the glycosidic bond; disaccharides and polysaccharides; chemical glycosylation (donors and promoters, oxocarbenium ions, neighboring group participation and 1,2-trans selectivity, solvent effects, NMR assignment of anomeric configuration, the Yu glycosylation).
source_hash: 05b89faf2f5e
---

**Carbohydrates** (sugars) are the most abundant organic compounds in nature: through photosynthesis, plants fix about $10^{11}$ tonnes of carbon into sugars each year, and cellulose and starch are the most abundant biopolymers. In living systems sugars serve as forms of energy storage and transport (starch, glycogen, glucose, sucrose), as structural materials (cellulose in plant cell walls, chitin in the exoskeletons of insects and crustaceans, peptidoglycan in bacterial cell walls), and as signals for cell recognition: a difference of a single terminal monosaccharide in the glycan chains on the surface of red blood cells determines the ABO blood group, and the dense glycan shield on viral surface proteins (for example the high-mannose glycans on the spike protein of SARS-CoV-2) helps the virus evade immune recognition. The roles of sugars in metabolism, signal transduction, and immunity are left to biochemistry; this chapter treats only the chemistry of sugars: structure, configuration, reactions, and synthesis.

The chemistry of sugars rests almost entirely on the preceding chapters. A monosaccharide is a polyhydroxy aldehyde or ketone, and its configuration is described by the **Fischer projection** and the **D/L nomenclature** of [6.5.5](/6.5.5#sec-5.3). In water it exists mainly as an intramolecular **hemiacetal** ([6.5.16](/6.5.16#sec-16.5.2)), which gives rise to anomers, mutarotation, and the anomeric effect; the **conformational analysis** of the ring follows [6.5.4](/6.5.4#sec-4.6). The reactions of monosaccharides are those of aldehydes, ketones, and alcohols ([6.5.10](/6.5.10), [6.5.16](/6.5.16), [6.5.17](/6.5.17), [6.5.21](/6.5.21)); a glycoside is an **acetal**, and the formation of the glycosidic bond proceeds through an oxocarbenium ion whose stereochemistry is governed by **neighboring group participation** ([6.5.8](/6.5.8#sec-8.10)) and by the solvent. Sugars in nucleosides and nucleic acids are discussed in [6.5.33](/6.5.33).

## 32.1. Definition and Classification of Sugars

### 32.1.1. Carbohydrates

Early analyses gave molecular formulas for glucose, sucrose, and cellulose that could all be written as $\ce{C_x(H2O)_y}$, hence the name "carbohydrate" (hydrate of carbon). The name is purely historical: lactic acid $\ce{C3H6O3}$ fits the formula but is not a sugar, while rhamnose $\ce{C6H12O5}$ and deoxyribose $\ce{C5H10O4}$ are sugars that do not fit it, and amino sugars even contain nitrogen. The structural definition is as follows.

**Definition 32.1.1 (Carbohydrate)** Polyhydroxy aldehydes, polyhydroxy ketones, and compounds that give them on hydrolysis are collectively called **carbohydrates** (also *saccharide*s). A sugar that cannot be hydrolyzed further into simpler polyhydroxy aldehydes or ketones is called a **monosaccharide**; a compound formed from about 2–10 monosaccharide units joined by glycosidic bonds is called an **oligosaccharide**, and one composed of exactly two units is a **disaccharide**; a macromolecule composed of many more units (hundreds to tens of thousands) is called a **polysaccharide**.

There are also sugar derivatives: amino sugars (such as 2-amino-2-deoxy-D-glucose, glucosamine), deoxy sugars, uronic acids, sugar alcohols, and glycoproteins and glycolipids, in which sugars are joined to proteins and lipids.

### 32.1.2. Classification of Monosaccharides

**Definition 32.1.2 (Aldoses and Ketoses)** A monosaccharide containing an aldehyde group is called an **aldose**, and one containing a ketone carbonyl group is called a **ketose**.

Monosaccharides are named according to the number of carbon atoms as trioses, tetroses, pentoses, hexoses, and so on, which combined with the carbonyl type gives aldopentose, ketohexose, etc. In natural ketoses the carbonyl group is almost always at C2. The most common monosaccharides are:

| Monosaccharide | Type | Occurrence |
|---|---|---|
| D-glyceraldehyde, dihydroxyacetone | aldotriose, ketotriose | intermediates of glycolysis (as phosphates) |
| D-ribose, 2-deoxy-D-ribose | aldopentoses | RNA, DNA, ATP, coenzymes |
| D-glucose | aldohexose | starch, cellulose, glycogen, blood sugar |
| D-mannose, D-galactose | aldohexoses | glycoproteins, lactose |
| D-fructose | ketohexose | honey, fruit, sucrose |

### 32.1.3. Determination of the Structure of Glucose

Before spectroscopic methods existed, the structure of glucose was deduced from a series of chemical reactions, a model of classical structure determination:

1. Elemental analysis and molecular weight determination give $\ce{C6H12O6}$.
2. Reaction with acetic anhydride gives a pentaacetate: there are five OH groups. Because two OH groups on the same carbon are unstable, the five OH groups sit on five different carbons.
3. Glucose forms an oxime with hydroxylamine, adds HCN, and is oxidized by **Tollens' reagent**: there is a carbonyl group. Oxidation by bromine water gives a monocarboxylic acid (gluconic acid) with the same number of carbons, which shows that the carbonyl group is an aldehyde.
4. Prolonged reduction with HI and red phosphorus gives *n*-hexane: the six carbons form an unbranched chain.

Glucose is therefore 2,3,4,5,6-pentahydroxyhexanal, $\ce{HOCH2(CHOH)4CHO}$. The same method applied to fructose shows that it also has five OH groups and one carbonyl group and gives *n*-hexane on HI reduction, but it is not oxidized by bromine water; hydrolysis and reduction of its **cyanohydrin** give 2-methylhexanoic acid (glucose gives heptanoic acid), so CN adds at C2 and fructose is 1,3,4,5,6-pentahydroxyhexan-2-one.

## 32.2. Configuration of Monosaccharides

### 32.2.1. The D Series and the L Series

The four carbons C2–C5 of an aldohexose $\ce{HOCH2(CHOH)4CHO}$ are **stereocenters**, so there are $2^4 = 16$ **stereoisomers** (8 pairs of enantiomers); an aldopentose has $2^3 = 8$, an aldotetrose 4, and an aldotriose (glyceraldehyde) 2; a ketohexose has only three stereocenters and 8 stereoisomers.

The configuration of a sugar is conventionally represented by the **Fischer projection** ([Definition 5.3.2](/6.5.5#def-5.3.2)): the carbon chain is arranged vertically with C1 (the aldehyde group, or the $\ce{CH2OH}$ of a ketose) at the top, and the horizontal bonds at each stereocenter point toward the reader. The **absolute configuration** of a sugar is given by the **D/L nomenclature** ([Definition 5.3.3](/6.5.5#def-5.3.3)): if the OH on the highest-numbered stereogenic carbon (the one farthest from the carbonyl group, called the configurational reference atom) is on the right, the sugar is D; if it is on the left, L, because this center has the same configuration as that of D-glyceraldehyde ((*R*)-glyceraldehyde). D/L is unrelated to the direction of optical rotation: D-glucose is dextrorotatory and D-fructose is levorotatory, written D-(+)-glucose and D-(−)-fructose.

Starting from D-glyceraldehyde, each addition of one carbon at the carbonyl end (the Kiliani–Fischer chain extension of Section 32.4.5) gives a new pair of aldoses in which the new stereocenter is C2 while the existing stereocenters are unchanged; in this way all the D-aldoses are obtained:

![The D-aldose family: simplified Fischer projections from D-glyceraldehyde to the eight D-aldohexoses (a horizontal line points to the side bearing OH; H is omitted). Chain extension of each aldose gives two aldoses with opposite configuration at C2; the OH on the reference atom (red) is always on the right. Aldoses marked with an asterisk give a meso aldaric acid on oxidation with nitric acid](./plots/aldose-family.py)

Every D-aldose has an L enantiomer whose Fischer projection has the OH groups on all stereogenic carbons (not only the reference atom) on the opposite side. It is best to memorize the names of the aldohexoses in the order of the figure (allose, altrose, glucose, mannose, gulose, idose, galactose, talose; the mnemonic is "All altruists gladly make gum in gallon tanks").

Most sugars in nature are D, which is related to the biosynthetic pathways by which ribose and glucose derive from D-glyceraldehyde 3-phosphate; but the statement "all natural sugars are D" is not true. Important L-sugars include L-arabinose (hemicellulose and pectin in plant cell walls), L-fucose (6-deoxy-L-galactose, the H antigen of ABO blood groups), L-rhamnose (6-deoxy-L-mannose, plant and bacterial polysaccharides), and L-iduronic acid (heparin and dermatan sulfate); vitamin C (L-ascorbic acid) is also a sugar derivative of the L series.

### 32.2.2. Epimers and Common Monosaccharides

D-Glucose and D-mannose differ only in the configuration at C2, and D-glucose and D-galactose only in the configuration at C4; they are C2 and C4 **epimers**, respectively ([Definition 5.4.2](/6.5.5#def-5.4.2)). The interconversion of epimers (Section 32.4.1) and the phenomenon of a common osazone (Section 32.4.4) involve only C2.

The **Fischer projections** of the most important monosaccharides (the positions of OH on C2, C3, C4, and C5, from top to bottom) are: D-glucose "right–left–right–right", D-mannose "left–left–right–right", D-galactose "right–left–left–right", D-ribose "right–right–right" (C2–C4 of the pentose); D-fructose is the ketohexose with the same C3–C5 as glucose, "left–right–right". The configuration of glucose can be memorized from the pattern "right–left–right–right" in the figure, and the others deduced from the epimeric relationships.

## 32.3. Cyclic Structures of Monosaccharides

### 32.3.1. Facts That the Open-Chain Form Cannot Explain

According to the open-chain structure of Section 32.1.3, glucose should show all the properties of an aldehyde, but experiments show that:

- glucose does not form an addition product with $\ce{NaHSO3}$ and gives only a weak color with Schiff's reagent (fuchsin–sulfurous acid);
- the infrared spectra of the solid and of solutions show no aldehyde C=O stretching band ($1720$–$1740\,\mathrm{cm^{-1}}$); the $^1\mathrm{H}$ NMR spectrum shows no aldehyde proton ($\delta$ 9–10), but one doublet each near $\delta$ 5.2 and 4.6;
- in the presence of HCl glucose reacts with only one molecule of methanol to give a stable methyl glucoside that is no longer reducing (an aldehyde and an alcohol in acid should give an **acetal** with two OR groups);
- there are two crystalline forms of glucose: the one crystallized from water or ethanol melts at $146\,^\circ\mathrm{C}$, and a freshly prepared solution has a **specific rotation** ([Definition 5.6.1](/6.5.5#def-5.6.1)) of $+112.2^\circ$; the one crystallized from hot acetic acid or pyridine melts at $150\,^\circ\mathrm{C}$, and a fresh solution has a specific rotation of $+18.7^\circ$. On standing, the specific rotations of both solutions change gradually and finally settle at $+52.7^\circ$.

These facts show that the aldehyde group is no longer present in most glucose molecules: it has formed a cyclic **hemiacetal** with an intramolecular hydroxy group ([Definition 16.5.1](/6.5.16#def-16.5.1)). The **equilibrium constants** for the formation of intramolecular hemiacetals with five- and six-membered rings are large ([6.5.16](/6.5.16#sec-16.5.2)); the C5–OH of glucose adds to the C1 aldehyde group to give an oxygen-containing six-membered ring.

### 32.3.2. Anomers, Pyranoses, and Furanoses

On ring closure C1 changes from a planar aldehyde carbon to a tetrahedral **hemiacetal** carbon and becomes a new **stereocenter**, so cyclic glucose has two configurations at C1.

**Definition 32.3.1 (Anomeric Carbon and Anomers)** The hemiacetal carbon formed from the carbonyl carbon when a monosaccharide cyclizes (C1 of an aldose, C2 of a 2-ketose) is called the **anomeric carbon**, and the hydroxy group on it is called the hemiacetal (glycosidic) hydroxy group. Two cyclic isomers that differ only in the configuration at the anomeric carbon are called **anomers**: in the Fischer projection, the one in which the hemiacetal hydroxy group is on the same side as the oxygen on the configurational reference atom is the $\alpha$ anomer, and the one in which it is on the opposite side is the $\beta$ anomer.

Anomers are a special kind of **epimer**. For D-sugars, in the Haworth formula below this definition is equivalent to: the $\alpha$ anomer has the hemiacetal hydroxy group trans to the $\ce{CH2OH}$ on the reference atom (C6 of an aldohexose) on opposite faces of the ring, and the $\beta$ anomer has it cis, on the same face.

**Definition 32.3.2 (Pyranose and Furanose)** A cyclic monosaccharide containing a six-membered ring made of five carbons and one oxygen (a tetrahydropyran ring) is called a **pyranose**, and one containing a five-membered ring made of four carbons and one oxygen (a tetrahydrofuran ring) is called a **furanose**.

The ring size is written into the name: $\alpha$-D-glucopyranose, $\beta$-D-fructofuranose. The perspective formula of cyclic structures was introduced by Haworth:

**Definition 32.3.3 (Haworth Projection)** The sugar ring is drawn as a regular planar polygon perpendicular to the plane of the paper (the ring oxygen is usually at the back right and the anomeric carbon at the right, with the ring bonds nearest the reader drawn bold), and the substituents on each ring carbon are drawn above or below the ring plane. The cyclic structural formula obtained in this way is called a **Haworth projection**.

The rule for drawing a Haworth formula from a **Fischer projection**: groups on the right in the Fischer projection point down in the Haworth formula, and groups on the left point up; the $\ce{CH2OH}$ on C5 of a D-pyranose points up.

![The equilibrium of D-glucose in water: the open-chain aldehyde (Fischer projection) and the two pyranose hemiacetals (Haworth projections). OH groups on the right in the Fischer projection point down in the Haworth projection; at the newly formed anomeric carbon C1 (red), OH pointing down is the $\alpha$ anomer and OH pointing up is the $\beta$ anomer](./plots/glucose-haworth.py)

In aqueous solution (25 °C), D-glucose is about 36% $\alpha$-pyranose and 64% $\beta$-pyranose; the furanoses amount to less than 1%, and the open-chain aldehyde to only about 0.003%. The equilibrium compositions of other monosaccharides differ: D-ribose contains about 59% $\beta$-pyranose, 20% $\alpha$-pyranose, 13% $\beta$-furanose, and 7% $\alpha$-furanose; D-fructose contains about 70% $\beta$-pyranose, 23% $\beta$-furanose, and small amounts of the $\alpha$ forms, but in sucrose and in fructose 1,6-bisphosphate it is bound as the furanose. The ribose and deoxyribose of nucleic acids are also $\beta$-furanoses ([6.5.33](/6.5.33#sec-33.9.1)):

```smiles
OC[C@H]1O[C@@H](O)[C@H](O)[C@@H](O)[C@@H]1O β-Glcp
OC[C@H]1O[C@@H](O)[C@H](O)[C@@H](O)[C@H]1O β-Galp
O[C@]1([C@H]([C@@H]([C@H](O1)CO)O)O)CO β-Fruf
C([C@@H]1[C@H]([C@H]([C@@H](O1)O)O)O)O β-Ribf
C1[C@@H]([C@H](O[C@H]1O)CO)O β-dRibf
```

(In order: $\beta$-D-glucopyranose, $\beta$-D-galactopyranose, $\beta$-D-fructofuranose, $\beta$-D-ribofuranose, and 2-deoxy-$\beta$-D-ribofuranose.)

The ring size was first established by chemical methods (Haworth, Hirst): all the free hydroxy groups of a methyl glycoside are methylated, and the glycosidic bond is then hydrolyzed; in the methylated sugar obtained, only the anomeric carbon and the carbon that took part in ring formation carry a free OH, and oxidative cleavage of this compound allows the position of ring closure to be deduced from the products. Periodate oxidation (Section 32.4.2) can also distinguish pyranosides from furanosides.

### 32.3.3. Mutarotation

**Definition 32.3.4 (Mutarotation)** The gradual change with time of the specific rotation of a freshly prepared sugar solution until it reaches a constant value is called **mutarotation**. It results from the interconversion of the two anomers through the open-chain form.

The interconversion of the $\alpha$ and $\beta$ anomers proceeds by ring opening and ring closure: the **hemiacetal** opens to the aldehyde, which then closes again by attack of the C5–OH on one of the two faces of the carbonyl group. It is catalyzed by acids and bases (an acid protonates the ring oxygen, or a base removes the proton of the hemiacetal OH), and also efficiently by molecules that have both an acidic and a basic group (such as 2-hydroxypyridine); in pure water it is slow. The equilibrium composition can be calculated from the equilibrium **specific rotation**: let the mole fraction of the $\beta$ anomer be $x$, neglecting the open-chain form and the furanoses,

$$
112.2^\circ(1 - x) + 18.7^\circ\, x = 52.7^\circ, \qquad x = 0.636.
$$

The open-chain form is only a steady-state intermediate at very low concentration, so mutarotation can be treated as a pair of first-order **opposing reactions** $\alpha \rightleftharpoons \beta$ ([6.3.15](/6.3.15#sec-15.4.1)): whichever anomer one starts from, the specific rotation approaches its equilibrium value exponentially with the same rate constant $k = k_1 + k_{-1}$,

$$
[\alpha](t) - [\alpha]_{\mathrm{eq}} = \bigl([\alpha]_0 - [\alpha]_{\mathrm{eq}}\bigr)\,\mathrm{e}^{-(k_1 + k_{-1})t}.
$$

![Mutarotation of glucose: starting from pure $\alpha$ and pure $\beta$ anomers, the specific rotation approaches $+52.7^\circ$ exponentially with the same rate constant (the rate constant is of the order of magnitude found at room temperature without catalyst and only sets the time axis)](./plots/mutarotation.py)

From the measured $k$ and the **equilibrium constant** $K = k_1/k_{-1} = x/(1-x) = 1.75$, $k_1$ and $k_{-1}$ can be found separately. That the $\beta$ anomer predominates is related to the ring conformation of glucose (Section 32.3.4); mutarotases in living organisms catalyze the same conversion, since some enzymes use only one anomer (glucose oxidase oxidizes only $\beta$-D-glucose, [6.4.6](/6.4.6)).

### 32.3.4. Conformations of Pyranoses and the Anomeric Effect

Like cyclohexane, a pyranose ring adopts a **chair conformation** ([Definition 4.5.1](/6.5.4#def-4.5.1)). D-Glucopyranose usually adopts the $^4C_1$ conformation, with C4 above the ring plane and C1 below it:

![$\alpha$- and $\beta$-D-glucopyranose in the $^4C_1$ chair conformation (H atoms on C2–C5 omitted). All OH groups and the $\ce{CH2OH}$ of the $\beta$ anomer are equatorial; the hemiacetal hydroxy group (red) of the $\alpha$ anomer is axial](./plots/glucose-chair.py)

All five non-hydrogen substituents of $\beta$-D-glucopyranose are in **equatorial bond** positions, which is possible for no other aldohexose (inverting any one **stereocenter** places a large group in an **axial bond** position); this is often used to explain why glucose is the most abundant monosaccharide in nature. By the steric effects of [6.5.4](/6.5.4#sec-4.6.1) the $\beta$ anomer should predominate overwhelmingly; in fact, however, the $\alpha$ anomer is still present at 36%, and in the acid-catalyzed equilibrium of methyl glucosides (in methanol) the $\alpha$ anomer actually accounts for about two-thirds. This shows that a substituent of high **electronegativity** on the anomeric carbon has an additional tendency to prefer the axial position.

**Definition 32.3.5 (Anomeric Effect)** In a pyranose ring (and in other saturated heterocycles), an electronegative substituent (OR, OH, halogen) on the carbon adjacent to the ring heteroatom tends to occupy the axial position rather than the sterically more favorable equatorial one. This effect is called the **anomeric effect**.

The magnitude of the anomeric effect is about $4$–$8\,\mathrm{kJ\,mol^{-1}}$, and there are two complementary explanations:

- The orbital explanation: the axial C1–O bond is **antiperiplanar** to a lone-pair orbital of the ring oxygen, so the lone pair $n_{\mathrm{O}}$ can delocalize into the **antibonding orbital** $\sigma^*_{\mathrm{C{-}O}}$ of the C1–OR bond. This is a **negative hyperconjugation** (Definition 26.3.1; ordinary **hyperconjugation** is in [Definition 2.6.1](/6.5.2#def-2.6.1)). It shortens the ring O–C1 bond and lengthens the C1–OR bond, as crystal structures confirm. An equatorial C1–O bond is not antiperiplanar to a lone pair and gets no such stabilization.
- The dipole explanation: when the substituent is equatorial, the lone-pair dipole of the ring oxygen and the dipole of the C1–O bond are roughly parallel and repel each other; when it is axial they are nearly opposed, and the molecular dipole moment is smaller.

![The orbital picture of the anomeric effect: Newman projections of 2-methoxytetrahydropyran viewed along the ring O5–C1 bond (O5 in front, C1 behind, ring bonds O5–C5 and C1–C2 gauche). Left: with axial OMe, the C1–OMe bond is antiperiplanar to a lone pair of the ring oxygen, which delocalizes into the σ* orbital of C1–OMe (negative hyperconjugation). Right: with equatorial OMe, the C1–OMe bond is anti to the ring bond O5–C5, and no lone pair is aligned with it](./plots/anomeric-newman.py)

The dipole explanation accounts for the influence of the solvent: a polar solvent solvates the conformer with the larger dipole better and weakens the anomeric effect. 2-Methoxytetrahydropyran is about 83% axial in $\ce{CCl4}$ but only about 52% in $\ce{D2O}$. The **hemiacetal** OH of glucose is strongly solvated in water and its anomeric effect is weak, and together with the steric advantage of the equatorial OH this makes the $\beta$ anomer the majority; the OMe of a methyl glycoside is less strongly solvated, and the anomeric effect prevails. The anomeric effect also determines the configuration of the thermodynamic product in chemical glycosylation (Section 32.6.2).

## 32.4. Reactions of Monosaccharides

### 32.4.1. Epimerization in Base and the Aldose–Ketose Interconversion

In dilute base (or a weak base such as pyridine), monosaccharides undergo **epimerization** at C2, and aldoses and ketoses interconvert at the same time (the Lobry de Bruyn–van Ekenstein rearrangement, 1895). D-Glucose left for four days at $35\,^\circ\mathrm{C}$ in $8\times10^{-3}\,\mathrm{mol\,L^{-1}}$ NaOH gives about 28% D-fructose and 3% D-mannose, the rest remaining D-glucose. The mechanism is the **enolization** (**tautomerism**, [Definition 21.2.1](/6.5.21#def-21.2.1)) of the open-chain aldehyde: the $\alpha$-H on C2 is removed by base to give a 1,2-enediol; C2 of the enediol is planar, so when C1 is protonated C2 can regain a proton from either face and return to glucose or mannose; if instead the C2–OH loses its proton and C1 gains one, a ketose is formed.

![Base-catalyzed aldose–ketose isomerization, illustrated with the smallest pair, D-glyceraldehyde and dihydroxyacetone. Top: $\ce{HO-}$ removes the $\alpha$-H on C2, and the enolate formed is protonated on oxygen to give a 1,2-enediol; the planar C2 can regain a proton on either face, so C2 epimerizes. Bottom: the C2–OH loses a proton and C1 is protonated, converting the enediol to a ketose](./plots/enediol.py)

This reaction determines two practical problems of sugar chemistry: treating sugars under basic conditions (for example etherification with a strong base) causes epimerization and degradation, so the sugar must first be protected or the reaction carried out on the glycoside; and basic **Tollens' reagent** and **Fehling's solution** cannot distinguish aldoses from ketoses (Section 32.4.2). In living organisms the same enediol mechanism operates under **enzyme catalysis**: triose phosphate isomerase interconverts dihydroxyacetone phosphate and D-glyceraldehyde 3-phosphate in glycolysis, and phosphoglucose isomerase interconverts glucose 6-phosphate and fructose 6-phosphate.

### 32.4.2. Oxidation

**Definition 32.4.1 (Reducing Sugar)** A sugar that reduces mild oxidants such as Tollens' reagent and Fehling's (or Benedict's) solution is called a **reducing sugar**; otherwise it is a nonreducing sugar. Every sugar that contains a free hemiacetal hydroxy group and can open to an aldehyde or an $\alpha$-hydroxy ketone is a reducing sugar.

**Tollens' reagent** and **Fehling's solution** ([6.5.17](/6.5.17#sec-17.5.2)) oxidize the aldehyde group of an aldose, giving a silver mirror and brick-red $\ce{Cu2O}$, respectively. Ketoses such as fructose are also reducing sugars, for two reasons: these reagents are basic, and in them a ketose isomerizes to an aldose through the enediol (Section 32.4.1); and an $\alpha$-hydroxy ketone can itself be oxidized by $\ce{Cu^2+}$. These two reagents therefore distinguish only reducing from nonreducing sugars, not aldoses from ketoses. Benedict's reagent, used clinically to detect sugar in urine (an alkaline $\ce{Cu^2+}$ solution with citrate in place of tartrate), works on the same principle, although the glucose oxidase method ([6.4.6](/6.4.6)) is now mostly used instead.

The selectivity of different oxidants:

| Oxidant | Conditions | Product from an aldose | Ketose |
|---|---|---|---|
| Tollens', Fehling's, Benedict's | basic, mild oxidant | aldonic acid (and degradation products) | also oxidized |
| Bromine water | pH 5–6, weakly acidic | aldonic acid, which on heating forms a $\gamma$- or $\delta$-**lactone** | not oxidized (no isomerization in acid), so it can be used to distinguish |
| Dilute nitric acid | heat | aldaric acid: both the C1 aldehyde group and the terminal $\ce{CH2OH}$ are oxidized to COOH | the C1–C2 bond is cleaved, giving a diacid with one carbon fewer |
| Periodic acid | room temperature, aqueous | all C–C bonds between vicinal diols and in $\alpha$-hydroxy aldehydes are cleaved | same |
| Glucose oxidase, $\ce{O2}$ | physiological | only $\beta$-D-glucose is oxidized, giving D-glucono-$\delta$-lactone and $\ce{H2O2}$ | — |

In oxidation by bromine water, what is actually oxidized is the **hemiacetal** of the pyranose (the $\beta$ anomer faster), which gives the aldonolactone ($\delta$-lactone) directly; this then hydrolyzes or isomerizes to the more stable $\gamma$-lactone. Industrially glucose is oxidized electrolytically in a $\ce{CaBr2}$ solution: $\ce{Br2}$ formed at the anode oxidizes glucose to gluconic acid, $\ce{OH-}$ formed at the cathode converts it to calcium gluconate, and $\ce{Br-}$ is recycled. Oxidation of only the primary alcohol at C6, leaving the aldehyde group, gives a uronic acid; chemically this requires protecting the aldehyde group first (for example in a glycoside), while in living organisms it is done by UDP-glucose dehydrogenase; glycoside formation between glucuronic acid and drug molecules (glucuronidation) is the main route of detoxification in the liver.

The aldaric acids obtained by nitric acid oxidation have identical ends and may be meso: in the figure above, the aldaric acids of D-erythrose, D-ribose, D-xylose, D-allose, and D-galactose (those marked with an asterisk) have a mirror plane and are optically inactive (D-galactaric acid is mucic acid, sparingly soluble in water and a diagnostic reaction for galactose). Whether an aldaric acid is optically active is the main tool in Fischer's determination of the configuration of sugars (Section 32.5).

Periodate oxidation consumes one molecule of $\ce{HIO4}$ per C–C bond cleaved: the terminal $\ce{CH2OH}$ gives formaldehyde, each internal CHOH gives formic acid, an aldehyde carbon gives formic acid, and a ketone carbon gives $\ce{CO2}$ (or formic acid). Hence

![Periodate cleavage of a vicinal diol (butane-2,3-diol as a model): the diol loses water with periodate to form a five-membered cyclic periodate diester; three electron pairs move simultaneously in the ring: the C–C bond becomes the π bond of one C=O, the electron pair of one O–I bond stays on iodine, and that of the other O–I bond becomes the π bond of the second C=O. Iodine is reduced from +7 to +5 (iodate), and the two carbons become carbonyl groups. A cis diol forms the cyclic ester easily, so it reacts faster than a trans diol](./plots/periodate.py)

$$
\text{D-glucose} + 5\,\ce{HIO4} \longrightarrow 5\,\ce{HCOOH} + \ce{HCHO}, \qquad \text{D-fructose} + 5\,\ce{HIO4} \longrightarrow 3\,\ce{HCOOH} + 2\,\ce{HCHO} + \ce{CO2}.
$$

By measuring the amount of $\ce{HIO4}$ consumed and of formic acid and formaldehyde formed, the ring size of a glycoside and the linkage positions of a sugar chain can be deduced (Question 4).

### 32.4.3. Reduction

The carbonyl group of an aldose or ketose is reduced to a polyol, called an alditol, by $\ce{NaBH4}$ (or, industrially, by Ni-catalyzed hydrogenation). D-Glucose is reduced to D-glucitol (sorbitol) and D-mannose to D-mannitol; reduction of C2 of D-fructose creates a new **stereocenter** and gives a mixture of sorbitol and mannitol. Both ends of an alditol are $\ce{CH2OH}$, so different sugars can give the same alditol: D-glucitol and L-gulitol are the same compound (rotating the **Fischer projection** of D-glucitol by $180^\circ$ in the plane of the paper gives the other); D-galactitol (dulcitol) is meso. Sorbitol, xylitol, and erythritol are low-calorie sweeteners, and sorbitol is also the starting material of the industrial synthesis of vitamin C (the Reichstein process: sorbitol is oxidized microbiologically to L-sorbose, which is then protected, oxidized, and lactonized to give L-ascorbic acid).

### 32.4.4. Osazone Formation

Heating an aldose or ketose with excess phenylhydrazine (3 equivalents) gives yellow crystals that are sparingly soluble in water, called sugar osazones.

**Definition 32.4.2 (Osazone)** The product in which both C1 and C2 of a sugar are converted to phenylhydrazones $\ce{C=N-NHPh}$ is called an **osazone**.

The first molecule of phenylhydrazine forms a phenylhydrazone with the carbonyl group (as in the formation of an **imine**, [6.5.16](/6.5.16#def-16.9.1)); the phenylhydrazone is converted by **tautomerism** into a carbonyl group at C2 (the details of this step are still debated; the net result is that the CHOH at C2 is oxidized to C=O and the second molecule of phenylhydrazine is reduced to aniline and $\ce{NH3}$); the third molecule of phenylhydrazine forms a second phenylhydrazone with the new carbonyl group, and the intramolecular **hydrogen bond** between the two hydrazone groups stabilizes the product, so the reaction stops at C2 and C3 is not oxidized further.

![The Weygand mechanism of osazone formation (R is the rest of the sugar chain). Top: the C1 phenylhydrazone is converted by enol–hydrazine tautomerism (an Amadori-type rearrangement) into a 1-(2-phenylhydrazinyl)-2-ketone; C2 is oxidized and C1 reduced. Bottom: in the enol form, the lone pair of O–H, the C=C bond, and the N–N bond move simultaneously, releasing aniline and giving an α-imino ketone; condensation with two molecules of phenylhydrazine and exchange of the C1 imine (releasing NH₃) then gives the osazone stabilized by an intramolecular hydrogen bond](./plots/osazone.py)

```smiles
OC[C@@H](O)[C@@H](O)[C@H](O)[C@@H](O)C=O.NNc1ccccc1.NNc1ccccc1.NNc1ccccc1>>OC[C@@H](O)[C@@H](O)[C@H](O)C(=NNc1ccccc1)C=NNc1ccccc1.Nc1ccccc1.N.O.O
```

Osazone formation involves only C1 and C2, so sugars with the same configuration from C3 onward give the same osazone: D-glucose, D-mannose, and D-fructose all give the same D-glucosazone. Fischer discovered phenylhydrazine (1875) and used the crystal form, melting point, and rate of formation of osazones to identify sugars; before chromatography this was the main way of distinguishing sugars, and a "common osazone" also gives direct evidence for the configurational relationships between sugars.

### 32.4.5. Chain Extension and Chain Shortening

**Definition 32.4.3 (Kiliani–Fischer Synthesis)** Addition of HCN to an aldose gives two C2-epimeric **cyanohydrins**, and conversion of the cyano group into an aldehyde group gives two aldoses with one more carbon than the starting material. This method of lengthening an aldose by one carbon at a time is called the **Kiliani–Fischer synthesis**.

The classical procedure (Kiliani 1885, Fischer 1890): the **cyanohydrin** is hydrolyzed to the aldonic acid, which on heating forms a lactone, and the lactone is then reduced to the aldose with sodium **amalgam** at pH 3–5 (a lactone is more easily reduced than the free acid, and the aldose is not reduced further). The modern improvement: catalytic hydrogenation over poisoned Pd/$\ce{BaSO4}$ reduces the cyano group selectively to an imine, which hydrolyzes at once to the aldehyde and gives the new aldose in one step. The two **epimers** are generally formed in unequal amounts and can be separated by chromatography.

```smiles
OC[C@@H](O)[C@@H](O)[C@H](O)C=O>>OC[C@@H](O)[C@@H](O)[C@H](O)[C@@H](O)C=O.OC[C@@H](O)[C@@H](O)[C@H](O)[C@H](O)C=O
```

![Kiliani–Fischer chain extension (only the top two carbons of the aldose are drawn; R is the rest of the sugar chain). Top: cyanide adds to the planar aldehyde group from either face, the former C1 becomes a new stereocenter, and two C2-epimeric cyanohydrins are formed (generally in unequal amounts). Bottom (modern improvement): hydrogenation over poisoned Pd/BaSO₄ stops at the imine, and hydrolysis of the imine gives the aldehyde, an aldose with one more carbon](./plots/kiliani-fischer.py)

(Chain extension of D-arabinose gives D-glucose and D-mannose.)

Degradation removes C1 of an aldose and gives an aldose with one carbon fewer; the original chirality of C2 disappears (it becomes the new aldehyde group) while the other **stereocenters** are unchanged:

**Definition 32.4.4 (Wohl Degradation and Ruff Degradation)** An aldose is first converted to its oxime, which is dehydrated with acetic anhydride and sodium acetate to an acetylated nitrile; the acetyl groups are then removed with base (sodium methoxide or ammonia) with loss of HCN, giving an aldose with one carbon fewer. This is called the **Wohl degradation** (1893). An aldose is first oxidized with bromine water to the aldonic acid, whose calcium salt is decarboxylated by $\ce{Fe^3+}$ (or $\ce{Fe^2+}$) and $\ce{H2O2}$, C2 being oxidized to an aldehyde group and giving an aldose with one carbon fewer. This is called the **Ruff degradation** (1898).

The last step of the Wohl degradation is just the reverse of cyanohydrin formation: the alkoxide at C2 pushes its electron pair back to form C=O, and cyanide leaves. The Ruff degradation proceeds through radical **decarboxylation** (similar to Kolbe electrolysis, [6.5.18](/6.5.18#sec-18.4.2)) and the yields are generally modest; it is used industrially to prepare D-arabinose from D-gluconic acid (which is then used to synthesize riboflavin). Chain extension and shortening link the members of the aldose family, and it was with these reactions that Fischer established the relative configurations of the sugars.

![The Wohl degradation (R is the rest of the sugar chain): the aldose oxime is dehydrated and fully acetylated by acetic anhydride and sodium acetate to give an acetylated nitrile; after sodium methoxide removes the acetyl groups, the alkoxide at C2 of the cyanohydrin pushes its electron pair back to form C=O and cyanide leaves (the reverse of cyanohydrin formation). The new aldehyde carbon is the original C2, and the aldose has lost one carbon](./plots/wohl.py)

![The Ruff degradation (R is the rest of the sugar chain): Fe³⁺ removes one electron from the aldonate to give an acyloxy radical; it loses CO₂ (fishhook arrows: one electron of the C1–C2 bond pairs with the oxygen radical, and the other stays on C2); the α-hydroxyalkyl radical then loses one electron and one proton, and C2 becomes the aldehyde group of the aldose with one carbon fewer](./plots/ruff.py)

### 32.4.6. Characteristic Reaction of Ketoses

In concentrated hydrochloric acid, ketoses lose three molecules of water much faster than aldoses, giving 5-hydroxymethylfurfural (HMF), which condenses with resorcinol to a red xanthene-type product; this is the Seliwanoff test (1887) that distinguishes ketoses from aldoses.

```smiles
OC[C@@H](O)[C@@H](O)[C@H](O)C(=O)CO>>OCc1ccc(C=O)o1.O.O.O
```

It depends on rate rather than on presence or absence: an aldose must first isomerize or dehydrate by a slower route, so on brief heating only ketoses give a deep red color, while on prolonged heating aldoses also give a pale red. Fructose-containing disaccharides and polysaccharides such as sucrose are first hydrolyzed in concentrated acid and also test positive. Similarly, pentoses dehydrate to furfural in concentrated acid, and with orcinol (5-methylresorcinol) give a blue-green product (the Bial test), used to detect ribose in RNA. The formation of HMF and furfural is also the basis of producing platform chemicals from cellulose and hemicellulose, and part of the reason sugars brown on heating in foods (the other part is the Maillard reaction between sugars and amino acids).

### 32.4.7. Reactions and Protection of Hydroxy Groups

The several hydroxy groups of a sugar have similar reactivity, and in synthesis they must be distinguished by reaction conditions and **protecting groups** ([Definition 16.5.2](/6.5.16#def-16.5.2); for a summary table see [6.5.20](/6.5.20#sec-20.8.3)). Some general rules: the primary hydroxy group (C6) is the least hindered and is protected first, selectively, by bulky reagents (trityl chloride, TBSCl); the **hemiacetal** hydroxy group is the most reactive (its $\mathrm{p}K_{\mathrm{a}}$ is about 12.3, about 3 units lower than that of an ordinary alcohol because C1 bears the ring oxygen) and can be selectively glycosylated or activated; a cis vicinal diol forms a five-membered cyclic **ketal** more easily than a trans diol.

- Esterification: glucose with excess acetic anhydride in pyridine gives the pentaacetate, with all OH groups (including the hemiacetal OH) acetylated. Heating with sodium acetate as catalyst gives mainly the $\beta$-pentaacetate (the OH of the $\beta$ anomer is equatorial and more easily acylated, and the anomers have no time to interconvert under basic conditions); with a **Lewis acid** catalyst such as $\ce{ZnCl2}$ or $\ce{HClO4}$, equilibration through the anomeric carbon gives the thermodynamically stable $\alpha$-pentaacetate (the anomeric effect). Esters are removed by transesterification in $\ce{NaOMe}$/MeOH (Zemplén deacetylation) without affecting glycosidic bonds.
- Etherification: methylation of all hydroxy groups with iodomethane in the presence of $\ce{Ag2O}$, or with NaH and iodomethane (the Hakomori method), is used for the methylation analysis of Section 32.3.2; benzyl ethers (NaH, BnBr) are stable to both acids and bases and are finally removed by catalytic hydrogenolysis, making them the most commonly used "permanent" protecting group in sugar chemistry. Etherification is usually carried out on glycosides, to prevent the hemiacetal from ring opening and undergoing **epimerization** in base.
- Acetals and ketals: glucose and acetone in acid give 1,2:5,6-di-$O$-isopropylidene-$\alpha$-D-glucofuranose ("diacetone glucose"). In pyranose glucose the C2–OH/C3–OH and C3–OH/C4–OH pairs are both trans and do not easily form five-membered ketals, so the equilibrium shifts to the furanose form: in the furanose, C1–OH and C2–OH are cis, and the C5, C6 diol is outside the ring, so two five-membered ketals can form. This is a typical example of "the protecting group changes the ring size", and it also leaves the C3–OH of glucose as the only free hydroxy group, which can be modified on its own. Benzaldehyde (or its dimethyl acetal), on the other hand, reacts selectively with the C4–OH and C6–OH of a pyranoside to give a six-membered 4,6-$O$-benzylidene acetal (a 1,3-dioxane, in a **chair conformation** with the phenyl group equatorial).

```smiles
OC[C@H]1O[C@H](OC)[C@H](O)[C@@H](O)[C@@H]1O.O=Cc1ccccc1>>CO[C@H]1O[C@@H]2CO[C@@H](c3ccccc3)O[C@H]2[C@H](O)[C@H]1O.O
```

(Methyl $\alpha$-D-glucopyranoside gives the 4,6-$O$-benzylidene acetal.)

## 32.5. Fischer's Proof of the Configuration of Glucose

Fischer completed the proof of the relative configuration of glucose in 1891, a classic of determining stereostructure by chemical reasoning, and received the 1902 Nobel Prize in Chemistry for his work on sugars and purines. The **absolute configuration** could not be determined at the time; Fischer stipulated that the OH on C5 is on the right (the D form), and this arbitrary convention was confirmed to be correct by Bijvoet's X-ray determination in 1951 ([6.5.5](/6.5.5#sec-5.3.3)). With this convention, the sugars below are described by the positions of the OH groups on C2, C3, and C4 in the figure of Section 32.2.1 (C5 is always "right").

1. D-Arabinose gives D-glucose and D-mannose by the Kiliani–Fischer synthesis. Hence glucose and mannose are C2 **epimers**, and their C3, C4, and C5 have the same configurations as C2, C3, and C4 of arabinose.
2. Oxidation of arabinose with nitric acid gives an optically active diacid. Among the four D-aldopentoses, the aldaric acids of ribose and xylose are meso, so arabinose can only be arabinose or lyxose of the figure (OH on C2 on the left).
3. Oxidation of glucose and mannose with nitric acid gives optically active diacids in both cases. If arabinose were the lyxose of the figure, one of the two hexoses obtained from it by chain extension would be galactose, whose diacid is meso, contrary to the facts. So arabinose is "left–right–right", and glucose and mannose are "right–left–right–right" and "left–left–right–right" in some order.
4. The two are distinguished by "interchanging the ends": the C1 and C6 of a sugar are exchanged (oxidize first to the diacid, then reduce the other end to an aldehyde group), and one sees whether another aldohexose results. The diacid of "left–left–right–right" has equivalent ends (after a $180^\circ$ rotation in the plane of the paper it coincides with itself), so interchanging the ends gives the sugar itself; the diacid of "right–left–right–right" corresponds after interchanging the ends to another aldohexose, L-gulose. Fischer found that glucaric acid can also be obtained by oxidation of L-gulose (that is, glucaric acid = L-gularic acid), while mannaric acid comes only from mannose. So glucose is "right–left–right–right" and mannose is "left–left–right–right".

The proof uses only three kinds of reaction: chain extension, nitric acid oxidation, and measurement of optical activity. It shows the power of symmetry arguments: to decide whether a diacid is meso, one need only see whether its **Fischer projection** is symmetric top to bottom.

## 32.6. Glycosides

### 32.6.1. Glycosides and the Glycosidic Bond

**Definition 32.6.1 (Glycoside and Glycosidic Bond)** The product formed by dehydration between the hemiacetal hydroxy group of a sugar and a hydroxy group (or amino or thiol group) of another molecule is called a **glycoside**; the part of a glycoside other than the sugar is called the aglycone. The bond linking the anomeric carbon to the aglycone is called the **glycosidic bond**; according to the atom attached to the anomeric carbon it is classified as an O-, N-, S-, or C-glycosidic bond, and according to the configuration of the anomeric carbon as an $\alpha$- or $\beta$-glycosidic bond.

A glycoside is an **acetal** ([Definition 16.5.1](/6.5.16#def-16.5.1)) and therefore has the properties of an acetal: it is stable in base and hydrolyzed in acid (through the same oxocarbenium ion as in its formation); it has no free **hemiacetal** hydroxy group and cannot open, so it shows no mutarotation, is not a reducing sugar, and does not form an osazone. A glycoside is named by writing the aglycone first and then the glycosyl group with the ring size: "methyl $\alpha$-D-glucopyranoside". Nucleosides are N-glycosides ([6.5.33](/6.5.33#sec-33.9.1)), and cyanogenic glycosides such as amygdalin are glycosides of a **cyanohydrin** ([6.5.16](/6.5.16#def-16.7.1)).

In living organisms the hydrolysis of glycosides is catalyzed by glycosidases, which are strictly specific for the configuration of the glycosidic bond: maltase hydrolyzes only $\alpha$-glucosides, and emulsin ($\beta$-glucosidase) only $\beta$-glucosides. This is why humans have amylases that degrade starch ($\alpha$-1,4 bonds) but no cellulase to degrade cellulose ($\beta$-1,4 bonds).

### 32.6.2. Fischer Glycosylation

Heating a monosaccharide in an anhydrous alcohol with a little strong acid (HCl, an acidic resin) gives a glycoside (Fischer 1893). The mechanism is that of **acetal** formation: the protonated **hemiacetal** hydroxy group leaves as water, pushed out by a lone pair of the ring oxygen, and a planar oxocarbenium ion is formed; the alcohol adds to C1 from above or below the ring, and loss of a proton gives the two anomers:

![Acid-catalyzed glycosylation, illustrated with tetrahydropyran-2-ol, the simplest model of a pyranose hemiacetal. Top: the protonated hemiacetal hydroxy group leaves as water, pushed out by a lone pair of the ring oxygen, to give a planar oxocarbenium ion (the slow step). Bottom: methanol adds to C1 from either face and loses a proton, giving the methyl glycosides of both anomers. All steps are reversible](./plots/oxocarbenium.py)

Every step is reversible, and the product ratio is determined thermodynamically, favoring the $\alpha$ anomer stabilized by the anomeric effect: glucose in methanol gives about 2:1 $\alpha$- and $\beta$-methyl glucopyranosides (a short reaction time gives the kinetic product, the furanosides, which with longer times convert to the more stable pyranosides). This method is suitable only for glycosylation with simple alcohols (methanol, benzyl alcohol, allyl alcohol): the alcohol must be used in large excess as solvent, and the product is a mixture of anomers. To join two sugars, the methods of Section 32.8 are needed.

## 32.7. Disaccharides and Polysaccharides

### 32.7.1. Disaccharides

A disaccharide is a glycoside formed by dehydration between the **hemiacetal** hydroxy group of one monosaccharide and a hydroxy group of another. Depending on whether the second monosaccharide supplies an alcoholic or a hemiacetal hydroxy group, disaccharides fall into two classes:

- Reducing disaccharides: the anomeric carbon of one monosaccharide is linked to an alcoholic hydroxy group (usually C4–OH) of the other, and the second monosaccharide retains a free hemiacetal hydroxy group and can open. It shows mutarotation, forms an osazone, and is a reducing sugar. Maltose, cellobiose, and lactose belong to this class.
- Nonreducing disaccharides: the anomeric carbons of the two monosaccharides are joined through one oxygen ("head to head"), both hemiacetal hydroxy groups are used up, and no part of the molecule can open; there is no mutarotation, no osazone, and it is not a reducing sugar. Sucrose and trehalose belong to this class.

The linkage of a disaccharide is written as "glycosyl-(linkage position)-sugar": maltose is $\alpha$-D-Glc$p$-(1→4)-D-Glc$p$, the arrow pointing from the sugar that supplies the anomeric carbon to the linkage position on the other; nonreducing disaccharides use a double-headed arrow, as in trehalose, $\alpha$-D-Glc$p$-(1↔1)-$\alpha$-D-Glc$p$.

| Disaccharide | Composition and linkage | Reducing | Source and notes |
|---|---|---|---|
| Sucrose | $\alpha$-D-Glc$p$-(1↔2)-$\beta$-D-Fru$f$ | no | sugar cane, sugar beet; $[\alpha]_{\mathrm{D}} = +66.5^\circ$, hydrolysis gives levorotatory invert sugar |
| Maltose | $\alpha$-D-Glc$p$-(1→4)-D-Glc$p$ | yes | product of the amylase hydrolysis of starch |
| Cellobiose | $\beta$-D-Glc$p$-(1→4)-D-Glc$p$ | yes | product of the partial hydrolysis of cellulose |
| Lactose | $\beta$-D-Gal$p$-(1→4)-D-Glc$p$ | yes | milk (about 7% in human milk, about 4.7% in cow's milk) |
| Trehalose | $\alpha$-D-Glc$p$-(1↔1)-$\alpha$-D-Glc$p$ | no | fungi, insect hemolymph; helps organisms tolerate desiccation and freezing |

```smiles
OC[C@H]1O[C@H](O[C@]2([C@H]([C@@H]([C@H](O2)CO)O)O)CO)[C@H](O)[C@@H](O)[C@@H]1O sucrose
OC[C@H]1O[C@@H](O)[C@H](O)[C@@H](O)[C@@H]1O[C@H]2O[C@H](CO)[C@@H](O)[C@H](O)[C@H]2O maltose
OC[C@H]1O[C@@H](O)[C@H](O)[C@@H](O)[C@@H]1O[C@@H]2O[C@H](CO)[C@H](O)[C@H](O)[C@H]2O lactose
```

(Maltose and lactose are drawn with the $\beta$ anomer at the reducing end; in solution the two anomers at the reducing end equilibrate by mutarotation.)

A few points deserve attention:

- The fructose part of sucrose is a furanose, and sucrose is both a glucoside and a fructoside. Hydrolyzed by acid or invertase it gives equal amounts of D-glucose (equilibrium $[\alpha]_{\mathrm{D}} = +52.7^\circ$) and D-fructose (equilibrium $-92.4^\circ$), and the **specific rotation** of the mixture is about the average of the two, $\tfrac12(52.7 - 92.4) \approx -20^\circ$. The sign of rotation changes from dextro to levo, so the hydrolysate is called *invert sugar*; the main component of honey is invert sugar. The glycosidic bond of sucrose joins two anomeric carbons, and the oxocarbenium ion formed in acid (the fructofuranosyl cation) is particularly stable, so sucrose is hydrolyzed by acid more easily than maltose.
- Lactose is a galactoside: its glycosidic bond is supplied by the anomeric carbon of galactose and attached to the C4–OH of glucose, and is a $\beta$-galactosidic bond, not a glucosidic one. The glucose unit retains the free hemiacetal hydroxy group. In most adults the activity of lactase ($\beta$-galactosidase) in the small intestine declines, and undigested lactose is fermented by bacteria in the colon; this is lactose intolerance.
- Maltose and cellobiose have the same composition and the same linkage position and differ only in the configuration of the glycosidic bond ($\alpha$ versus $\beta$). This difference determines the entirely different structures and properties of starch and cellulose (Section 32.7.2).

### 32.7.2. Polysaccharides

Cellulose is a linear polysaccharide of D-glucose joined by $\beta$-(1→4) glycosidic bonds, with a degree of polymerization of up to tens of thousands. The $\beta$ configuration turns each glucose unit by $180^\circ$ relative to the previous one, so the chain extends into a flat ribbon, and many intrachain (O3–H⋯O5′) and interchain **hydrogen bonds** bind parallel chains into crystalline microfibrils; cellulose is therefore strong, insoluble in water, and hard to hydrolyze by acids and enzymes. Cotton contains more than about 90% cellulose and wood about 40%–50%. Esterification of cellulose with nitric acid gives cellulose nitrate (guncotton, celluloid) and acetylation gives cellulose acetate (acetate fiber); dissolving in alkali and $\ce{CS2}$ followed by regeneration gives viscose fiber (rayon). Chitin is similar in structure to cellulose except that the OH on C2 is replaced by an acetamido group (a $\beta$-(1→4) polymer of *N*-acetylglucosamine), and is the main component of arthropod exoskeletons and fungal cell walls.

Starch is the glucose stored by plants and consists of two components:

- Amylose (15%–30%): a long chain of D-glucose joined by $\alpha$-(1→4) bonds. The $\alpha$ configuration gives an angle between adjacent units, and the chain coils naturally into a left-handed helix with about 6 glucose units per turn, the interior of the helix being hydrophobic.
- Amylopectin (70%–85%): the main chain also has $\alpha$-(1→4) bonds, with a branch joined by an $\alpha$-(1→6) bond every 24–30 glucose units. Glycogen, the storage form in animals, is similar in structure to amylopectin but more densely branched (one branch every 8–12 units), with more nonreducing ends, so glycogen phosphorylase can degrade it from many ends at once and release glucose quickly.

Starch turns blue with iodine because iodine and iodide line up inside the helical cavity of amylose as long chains of polyiodide ions (mainly $\ce{I3-}$ and $\ce{I5-}$ units); electrons delocalize along the helix axis in the chain, and the absorption shifts to longer wavelength (about 600 nm). This is a host–guest inclusion, and the color comes from the electronic structure of the polyiodide chain itself, not merely from a weak interaction between iodine and starch. The branches of amylopectin are short and can hold only short polyiodide chains, giving a purple-red color; glycogen gives a red-brown color; when starch is hydrolyzed stepwise by acid or amylase, the color changes from blue through purple and red to colorless, which can be used to follow the progress of hydrolysis.

Native starch exists as granules insoluble in cold water: both components are insoluble in cold water because of the semicrystalline structure of the granule. In hot water the granules absorb water and swell and the crystalline regions melt (gelatinization); amylose dissolves out into solution and amylopectin swells into a viscous paste. On cooling, the amylose chains reassociate by hydrogen bonding and precipitate (retrogradation, which is why cold rice and bread harden), whereas the amylopectin paste is more stable.

## 32.8. Chemical Glycosylation

### 32.8.1. Donors, Acceptors, and Promoters

The core of the chemical synthesis of oligosaccharides and glycoconjugates is the formation of a glycosidic bond of specified position and configuration between two sugars. In **retrosynthesis**, the glycosidic bond is cleaved into a "glycosyl cation" synthon carrying a **leaving group** at the anomeric carbon, from which an oxocarbenium ion can form, and an alcohol with a free hydroxy group:

**Definition 32.8.1 (Glycosylation, Glycosyl Donor, and Glycosyl Acceptor)** A reaction that forms a glycosidic bond at the anomeric carbon of a sugar is called a **glycosylation**. A compound that carries an activatable leaving group at the anomeric carbon and supplies the glycosyl group in the reaction is called a **glycosyl donor**, and the compound that supplies the hydroxy group (or other nucleophilic group) is called a **glycosyl acceptor**; the reagent that makes the leaving group of the donor depart is called a promoter or activator.

A glycosylation is evaluated by its yield, anomeric **stereoselectivity** ($\alpha/\beta$ ratio), **regioselectivity** and **chemoselectivity** (when the acceptor has several hydroxy groups or other functional groups), mildness of conditions, and cost. The commonly used donors and promoters are:

| Method | Donor (leaving group at the anomeric carbon) | Promoter | Characteristics |
|---|---|---|---|
| Fischer glycosylation | OH (free sugar) | $\ce{H+}$ | reversible, under **thermodynamic control**, suitable only for simple alcohols |
| Koenigs–Knorr method (1901) | Br, Cl | $\ce{Ag2CO3}$, $\ce{Ag2O}$, AgOTf, Hg(II) salts | the first effective method; glycosyl halides are unstable |
| Glycosyl fluorides | F | $\ce{BF3.OEt2}$, $\ce{Cp2HfCl2}$/AgOTf | the strong C–F bond makes the donor stable |
| Trichloroacetimidate method (Schmidt, 1980) | $\ce{OC(=NH)CCl3}$ | catalytic TMSOTf or $\ce{BF3.OEt2}$ | highly reactive, mild conditions, most widely used |
| Thioglycosides | SPh, SEt | NIS/TfOH, DMTST, $\ce{Ph2SO}$/$\ce{Tf2O}$ | stable to most protection–deprotection conditions; allow "preactivation" and stepwise activation |
| *o*-Alkynylbenzoates (Yu, 2008) | $\ce{OC(=O)C6H4-2-C#CR}$ | catalytic $\ce{Ph3PAuOTf}$ | nearly neutral conditions, suitable for acid-sensitive acceptors (Section 32.8.6) |

The reactivity of a donor is also tuned by the **protecting groups**: electron-withdrawing ester protecting groups destabilize the oxocarbenium ion and make the donor "disarmed", whereas electron-donating benzyl ethers make the donor "armed". Fraser-Reid used this to couple an armed donor selectively with a disarmed acceptor that has the same type of leaving group, and then to activate the latter for the next coupling, which is the basis of one-pot multistep oligosaccharide synthesis.

![The Schmidt trichloroacetimidate method (tetrahydropyranyl as a donor model). Top: the anomeric alkoxide formed with base (DBU or K₂CO₃) adds to the cyano carbon of trichloroacetonitrile, and protonation of the nitrogen gives the O-glycosyl trichloroacetimidate. Bottom: a catalytic Lewis or Brønsted acid (TMSOTf, drawn here as H⁺) activates the imidate nitrogen, a lone pair of the ring oxygen pushes out the trichloroacetamide (a very weak base after tautomerization to the amide), and the oxocarbenium ion formed is trapped by the acceptor alcohol](./plots/imidate.py)

### 32.8.2. Mechanism: The Oxocarbenium Ion

Most glycosylations proceed through the same oxocarbenium ion as the Fischer glycosylation (the figure of Section 32.6.2): the promoter ($\ce{Ag+}$ removing halide, a **Lewis acid** coordinating the imidate N, the **electrophile** $\ce{I+}$ activating a sulfur atom) makes the **leaving group** depart, and a lone pair of the ring oxygen forms a partial double bond to C1, giving a planarized oxocarbenium ion (the ring in a half-chair conformation). This is a process like an **SN1 reaction** ([6.5.8](/6.5.8#sec-8.2.3)): the acceptor attacks from both faces, and the anomeric stereochemistry is hard to control. In reality there is a continuum between SN1 and the **SN2 reaction**: a tight **ion pair** with the leaving group, or an $\alpha$-glycosyl triflate formed at low temperature, can be displaced by the acceptor from the back side to give a product with inverted configuration (Crich used a 4,6-$O$-benzylidene-protected mannose donor, via the $\alpha$-triflate, to obtain the difficult $\beta$-mannosides by an SN2 pathway). The main means of controlling the anomeric configuration are the **neighboring group participation** and **solvent effects** described below.

### 32.8.3. Neighboring Group Participation and 1,2-trans Glycosides

When a donor carries an ester **protecting group** (acetyl, benzoyl, pivaloyl) on C2, then as the oxocarbenium ion forms, the neighboring ester carbonyl oxygen attacks C1 from below to give a stable bicyclic acyloxonium ion (a 1,3-dioxolan-2-ylium ion). This is **neighboring group participation** ([Definition 8.10.1](/6.5.8#def-8.10.1)): the ester group blocks this face of C1, the acceptor can attack only from the other face, and the glycosidic bond formed is trans to the substituent on C2.

![Neighboring group participation in glycosylation, illustrated with a model glycosyl bromide having an acetoxy group on C2 cis to the bromide. The carbonyl oxygen of the acetate displaces bromide to give a cis-fused bicyclic acyloxonium ion; it blocks one face of C1, and methanol can attack only from the other face, giving the glycoside trans to the C2 substituent (1,2-trans)](./plots/ngp-glycosylation.py)

A donor with an acyl group on C2 therefore reliably gives 1,2-trans glycosides: D-glucose, D-galactose, and 2-acetamido-2-deoxy sugars (the C2 substituent pointing down) give $\beta$-glycosides, and D-mannose and L-rhamnose (the C2–OH pointing up) give $\alpha$-glycosides. The main side reaction is attack of the acceptor on the central carbon of the acyloxonium ion (instead of C1), which gives an orthoester; the orthoester can rearrange to the desired glycoside in acid.

![The orthoester side reaction in glycosylation with neighboring group participation (same model as in the previous figure): the acceptor alcohol attacks the central carbon of the bicyclic acyloxonium ion instead of C1, and loss of a proton gives a 1,2-orthoester; under acid catalysis the orthoester dissociates again to the acyloxonium ion, which then opens at C1 to give the desired 1,2-trans glycoside](./plots/orthoester.py)

1,2-cis Glycosides ($\alpha$-glucosides, $\alpha$-galactosides, $\beta$-mannosides) are harder to make: C2 must carry a nonparticipating ether protecting group (benzyl), and the stereochemistry has to be controlled by the anomeric effect, the solvent, the temperature, remote groups, and special donors; this remains one of the central difficulties of carbohydrate chemistry.

### 32.8.4. Solvent Effects

The **stereoselectivity** of donors protected as ethers depends strongly on the solvent:

- In acetonitrile the $\beta$ (equatorial) product is favored: the nitrogen of acetonitrile attacks the oxocarbenium ion, kinetically giving mainly the axial $\alpha$-nitrilium ion, and the acceptor displaces it from the back side (the equatorial direction) to give the $\beta$-glycoside (the "nitrile effect").
- In diethyl ether and dioxane the $\alpha$ (axial) product is favored: the equatorial oxonium adduct that the ether forms with the oxocarbenium ion (equatorial because of the reverse anomeric effect) is displaced by the acceptor from the back side to give the $\alpha$-glycoside; the anomeric effect also makes the $\alpha$ product more stable thermodynamically.

![The nitrile effect in glycosylation (model donor with a nonparticipating methoxy group on C2): acetonitrile adds to the oxocarbenium ion mainly from the axial (α) face to give an α-nitrilium ion (cis to the C2 substituent in this figure); the acceptor displaces acetonitrile from the other face in an SN2-like step, giving the equatorial β glycoside (here 1,2-trans)](./plots/nitrile-effect.py)

### 32.8.5. NMR Assignment of Anomeric Configuration

The anomeric configuration of glycosylation products is assigned by $^1\mathrm{H}$ and $^{13}\mathrm{C}$ NMR (**chemical shifts** and **coupling constants**, [6.4.12](/6.4.12#sec-12.3.3)). The most reliable criterion is the three-bond coupling constant between H1 and H2: by the **Karplus equation** the coupling constant varies with the **dihedral angle** between the two C–H bonds, being largest when the dihedral angle is close to $180^\circ$ (trans diaxial) and smaller near $60^\circ$. In a $\beta$-glucoside in the $^4C_1$ conformation, H1 and H2 are both axial and the dihedral angle is about $180^\circ$; in an $\alpha$-glucoside, H1 is equatorial and H2 axial, and the dihedral angle is about $60^\circ$. In mannose H2 is equatorial, and $J_{1,2}$ is small for both anomers, so one turns to the one-bond coupling $^1J_{\mathrm{C1,H1}}$ of the anomeric carbon: it is about 10 Hz smaller when the anomeric C–H bond is axial ($\beta$) than when it is equatorial ($\alpha$), because the $\sigma^*$ of an axial C–H bond accepts negative hyperconjugation from the ring-oxygen lone pair (the Perlin effect).

| Pyranoside ($^4C_1$) | H1 | $J_{1,2}$ / Hz | $^1J_{\mathrm{C1,H1}}$ / Hz | $\delta(\mathrm{H1})$ |
|---|---|---|---|---|
| $\beta$-glucosides, $\beta$-galactosides (H1, H2 diaxial) | axial | 7–9 | about 160 | higher field (about 4.3–4.6) |
| $\alpha$-glucosides, $\alpha$-galactosides | equatorial | 3–4 | about 170 | lower field (about 4.8–5.2) |
| $\beta$-mannosides (H2 equatorial) | axial | about 1 | about 160 | higher field |
| $\alpha$-mannosides | equatorial | 1–2 | about 170 | lower field |

This is exactly how the $^1\mathrm{H}$ NMR spectrum of free glucose is interpreted: the doublet at $\delta$ 5.2 ($J \approx 3.7$ Hz) is $\alpha$-H1 and the doublet at $\delta$ 4.6 ($J \approx 8$ Hz) is $\beta$-H1, and their integral ratio is the ratio of the anomers (about 36:64, consistent with the value calculated from the optical rotation in Section 32.3.3).

### 32.8.6. The Yu Glycosylation and Frontiers of Carbohydrate Chemistry

Traditional glycosylations mostly need equivalent amounts of heavy-metal salts or strong **Lewis acids**, and acid-sensitive acceptors (complex natural products containing tertiary alcohols, **acetals**, or other glycosidic bonds) are difficult to use. The method developed by Biao Yu (Shanghai Institute of Organic Chemistry, Chinese Academy of Sciences) in 2008 uses glycosyl *o*-alkynylbenzoates as donors and a catalytic amount of the Au(I) complex $\ce{Ph3PAuOTf}$ as promoter: the $\pi$-philic Au(I) activates the alkyne, the ester carbonyl oxygen adds to it intramolecularly and cyclizes to an isobenzopyrylium, releasing the glycosyl group as an oxocarbenium ion at the same time, and the leaving fragment finally protodeaurates. The conditions are nearly neutral, and the method has been used in the total synthesis of many complex glycosylated natural products.

![The Yu glycosylation (tetrahydropyranyl as a donor model). Top: Ph₃PAu⁺ coordinates to the alkyne, and the ester carbonyl oxygen attacks the distal carbon of the alkyne (6-endo-dig) to give an isobenzopyrylium ion bearing a vinylgold group. Bottom: a lone pair of the sugar ring oxygen pushes out the neutral isocoumarin, releasing the glycosyl oxocarbenium ion for capture by the acceptor; the vinylgold species is protodeaurated, regenerating the catalyst](./plots/yu-gold.py)

The synthesis of oligosaccharides has long lagged behind the automated synthesis of peptides and nucleic acids ([6.5.33](/6.5.33#sec-33.7.6)), because each glycosidic bond involves a choice of both position and configuration, and a monosaccharide has several hydroxy groups that must be distinguished. Advances of the past two decades include Seeberger's automated solid-phase oligosaccharide assembly; one-pot glycosylation based on the "preactivation" of thioglycosides, by which Xinshan Ye and coworkers synthesized in 2017 a 92-mer arabinogalactan of the *Mycobacterium tuberculosis* cell wall; the preparation of homogeneous glycoproteins and glycoconjugate vaccines from chemically synthesized glycans and glycopeptides by Danishefsky and others (several groups in China also work on glycopeptide cancer vaccines); and, in 2021, the report by the Tianjin Institute of Industrial Biotechnology, Chinese Academy of Sciences, of an artificial pathway for the synthesis of starch from $\ce{CO2}$ and $\ce{H2}$ in a cell-free system through 11 chemical–enzymatic steps.

## Summary

| Topic | Key points |
|---|---|
| Structure of monosaccharides | Polyhydroxy aldehydes (aldoses) or ketones (ketoses, carbonyl at C2); the structure of glucose was established from the pentaacetate, bromine water oxidation, and HI reduction to *n*-hexane |
| Configuration | **Fischer projection**; OH on the reference atom (the highest-numbered stereogenic carbon) on the right means D; the D-aldose family is obtained from D-glyceraldehyde by stepwise chain extension; glucose is "right–left–right–right", mannose is the C2 **epimer**, galactose the C4 epimer; natural sugars are mostly D, but L-fucose, L-rhamnose, and L-arabinose also occur |
| Cyclic structures | Intramolecular **hemiacetals** (Definitions 32.3.1–32.3.3): pyranoses and furanoses, the anomeric carbon, and $\alpha$/$\beta$ anomers; groups on the right of the Fischer projection point down in the Haworth formula; in water glucose is 36% $\alpha$, 64% $\beta$, and about 0.003% open-chain |
| Mutarotation and conformation | Mutarotation is a first-order **opposing reaction**, and $[\alpha]$ gives the equilibrium composition; all large groups of $\beta$-D-glucopyranose are equatorial; the anomeric effect (Definition 32.3.5) arises from $n_{\mathrm{O}}\to\sigma^*_{\mathrm{C{-}O}}$ and dipole interactions and weakens with solvent polarity |
| Reactions | Epimerization and aldose–ketose interconversion through the enediol in dilute base; reducing sugars (Definition 32.4.1) reduce Tollens' reagent and **Fehling's solution** (ketoses too); bromine water oxidizes only aldoses; nitric acid gives aldaric acids (meso or not is evidence of configuration); periodate cleaves vicinal diols; $\ce{NaBH4}$ reduces to alditols; osazones (Definition 32.4.2) involve only C1 and C2; Kiliani–Fischer chain extension (Definition 32.4.3) and Wohl and Ruff degradations (Definition 32.4.4); the Seliwanoff test relies on faster dehydration of ketoses |
| Protection | The primary OH is most easily protected by bulky groups; the hemiacetal OH is the most reactive; cis diols form acetonides (diacetone glucose changes the ring to the furanose form) and 4,6-$O$-benzylidene acetals; benzyl ethers are the permanent **protecting group** and esters are removed by the Zemplén method |
| Fischer's proof | Chain extension, nitric acid oxidation, and optical activity; a symmetric diacid is meso; interchanging the ends distinguishes glucose from mannose |
| Glycosides and disaccharides | A glycoside is an **acetal** (Definition 32.6.1), shows no mutarotation, is nonreducing, and is hydrolyzed in acid; reducing (maltose, cellobiose, lactose) and nonreducing (sucrose, trehalose) disaccharides; invert sugar about $-20^\circ$; lactose is a $\beta$-galactoside |
| Polysaccharides | Cellulose is $\beta$-(1→4), flat, and forms fibers through **hydrogen bonds**; starch has an $\alpha$-(1→4) helix and $\alpha$-(1→6) branches; the iodine color comes from polyiodide chains in the helix |
| Chemical glycosylation | Donors, acceptors, and promoters (Definition 32.8.1); oxocarbenium ions; **neighboring group participation** by a C2 acyl group gives 1,2-trans products; acetonitrile favors $\beta$ and diethyl ether favors $\alpha$; $J_{1,2}$ and $^1J_{\mathrm{C1,H1}}$ assign the anomeric configuration; the Yu glycosylation activates *o*-alkynylbenzoates with Au(I) catalysis |

## Questions

1. Glucose reacts with 5 mol of acetic anhydride to give a pentaacetate; reduction with HI and red phosphorus gives *n*-hexane; addition of HCN followed by hydrolysis and exhaustive reduction with HI gives heptanoic acid. Fructose under the same conditions finally gives 2-methylhexanoic acid. Deduce the structures of glucose and fructose from these facts, and state what each fact rules out.

   **Answer** The pentaacetate shows that there are five OH groups and that two OH groups cannot be on the same carbon (a gem-diol is unstable), so the five OH groups are on five different carbons; the remaining oxygen is the carbonyl oxygen. Reduction with HI/P to *n*-hexane shows that the six carbons form an unbranched chain, ruling out branching. Hydrolysis and exhaustive reduction of the **cyanohydrin** give unbranched heptanoic acid, showing that CN added at a terminal carbon, so the carbonyl group is at C1 and glucose is an aldehyde (consistent with oxidation by bromine water to a monocarboxylic acid with the same number of carbons), $\ce{HOCH2(CHOH)4CHO}$. Fructose gives 2-methylhexanoic acid, showing that CN added at C2 and the added carbon became a branch on C2, so the carbonyl group is at C2 and fructose is $\ce{HOCH2(CHOH)3COCH2OH}$.

2. A freshly prepared solution of $\beta$-D-glucopyranose has a **specific rotation** of $+18.7^\circ$, which on standing reaches $+52.7^\circ$; the pure $\alpha$ anomer has $+112.2^\circ$. (a) Find the ratio of the two anomers at equilibrium and the **equilibrium constant** $K = [\beta]/[\alpha]$. (b) Starting from the $\alpha$ anomer, the specific rotation is found to fall from $+112.2^\circ$ to $+82.5^\circ$ in 46 min; find $k_1$ ($\alpha\to\beta$) and $k_{-1}$. (c) What should the integral ratio of the two doublets at $\delta$ 5.2 and 4.6 in the $\ce{^1H}$ NMR spectrum be?

   **Answer** (a) $112.2(1-x) + 18.7x = 52.7$ gives $x = 0.636$: 36.4% $\alpha$ and 63.6% $\beta$, $K = 0.636/0.364 = 1.75$. (b) $\ln\frac{112.2 - 52.7}{82.5 - 52.7} = \ln\frac{59.5}{29.8} = 0.692 = (k_1 + k_{-1})\times 46\,\mathrm{min}$, so $k_1 + k_{-1} = 0.0150\,\mathrm{min^{-1}}$ (half-life 46 min); from $k_1/k_{-1} = K = 1.75$, $k_1 = 0.0150\times1.75/2.75 = 9.5\times10^{-3}\,\mathrm{min^{-1}}$ and $k_{-1} = 5.5\times10^{-3}\,\mathrm{min^{-1}}$. (c) The integral ratio of the doublets at $\delta$ 5.2 ($\alpha$-H1, $J\approx3.7$ Hz) and $\delta$ 4.6 ($\beta$-H1, $J\approx8$ Hz) is about 36:64.

3. Fructose has no aldehyde group; why does it give a silver mirror with **Tollens' reagent**? How can glucose be distinguished from fructose with one reagent? Why does sucrose not reduce **Fehling's solution**, while its acid hydrolysate does?

   **Answer** Tollens' reagent is basic (it contains $\ce{NH3}$ and $\ce{OH-}$), and in base fructose isomerizes through the 1,2-enediol to glucose and mannose (the Lobry de Bruyn–van Ekenstein rearrangement), and the aldoses are oxidized; an $\alpha$-hydroxy ketone can also be oxidized itself. Acidic bromine water (pH 5–6) distinguishes them: it oxidizes only the aldose (the bromine water is decolorized), while in acid fructose does not isomerize and is not oxidized; the Seliwanoff test (fructose quickly gives a deep red color) can also be used. In sucrose the two anomeric carbons of glucose and fructose are joined through the glycosidic bond, there is no free **hemiacetal** hydroxy group, and it cannot open to an aldehyde or an $\alpha$-hydroxy ketone, so it is not a reducing sugar; after hydrolysis the free glucose and fructose are both reducing sugars.

4. Methyl $\alpha$-D-glucopyranoside and methyl $\alpha$-D-glucofuranoside are each oxidized with periodic acid. How much $\ce{HIO4}$ does each consume, and what small molecules are formed? How can the ring size of a methyl glycoside be determined from this?

   **Answer** The free OH groups of the pyranoside are on C2, C3, and C4 (C6 is a primary alcohol, and C5 carries the ring oxygen and does not form a vicinal diol with C6); the C2–C3 and C3–C4 bonds are cleaved, consuming 2 molecules of $\ce{HIO4}$, C3 is released as formic acid, and a dialdehyde (containing C1, C2 and C4, C5, C6) is obtained. The free OH groups of the furanoside are on C2, C3, C5, and C6: the C2–C3 bond is cleaved (1 molecule), and the C5–C6 bond is cleaved (1 molecule), so 2 molecules of $\ce{HIO4}$ are also consumed, but formaldehyde (C6) is released and no formic acid is formed. When the amounts consumed are equal, it is therefore enough to see whether formic acid or formaldehyde is formed to decide the ring size (this is the classical method of Hudson and others).

5. Which of the following sugars give the same osazone with excess phenylhydrazine? D-Glucose, D-mannose, D-fructose, D-galactose, D-talose, D-allose. Which give meso alditols on reduction with $\ce{NaBH4}$?

   **Answer** Osazone formation changes only C1 and C2, and sugars with the same configuration at C3–C5 give the same osazone: D-glucose, D-mannose, and D-fructose give the same osazone; D-galactose and D-talose (C2 **epimers**) give another one; D-allose and its C2 epimer D-altrose (not in the question) give the same osazone, so among those in the question allose stands alone. Both ends of an alditol are $\ce{CH2OH}$, and the criterion is the same as the symmetry of the aldaric acid: D-galactitol and D-allitol are meso (the hexoses marked with an asterisk in the figure); the alditols of glucose, mannose, and talose are optically active; fructose gives a mixture of sorbitol and mannitol, both of which are optically active.

6. (Fischer's proof) Using only Kiliani–Fischer chain extension, the Ruff degradation, nitric acid oxidation, and measurement of optical activity, explain how the configurations of D-arabinose, D-glucose, and D-mannose can be determined (take the OH on C5 on the right as the convention).

   **Answer** (1) Chain extension of arabinose gives glucose and mannose (conversely, Ruff degradation of either gives arabinose), so the two are C2 epimers, and C3–C5 are the same as C2–C4 of arabinose. (2) The diacid of arabinose is optically active: among the D-aldopentoses with the C4 OH on the right, ribose (right–right–right) and xylose (right–left–right), whose diacids are meso, are excluded, leaving "left–right–right" and "left–left–right". (3) The diacids of glucose and mannose are both optically active: if arabinose were "left–left–right", the chain-extension product "right–left–left–right" (galactose) would have a meso diacid, a contradiction; so arabinose is "left–right–right", and glucose and mannose are "right–left–right–right" and "left–left–right–right". (4) The diacid of "left–left–right–right" coincides with itself on rotation by $180^\circ$ in the plane of the paper and can be obtained from only one aldohexose; the diacid of "right–left–right–right" after rotation corresponds to L-gulose. Experiment shows that glucaric acid can also be obtained from another aldohexose (L-gulose), so glucose is "right–left–right–right" and mannose is "left–left–right–right".

7. Compare sucrose, maltose, cellobiose, and lactose: the constituent monosaccharides, the ring sizes, which carbon supplies the glycosidic bond, the configuration of the glycosidic bond, and whether the sugar is reducing. Why can humans digest starch but not cellulose?

   **Answer** Sucrose: glucose (pyranose) + fructose (furanose), the two anomeric carbons (Glc C1, Fru C2) joined, $\alpha$ (Glc) and $\beta$ (Fru), nonreducing. Maltose: two glucopyranoses, Glc C1 joined by an $\alpha$ bond to C4 of the other glucose, reducing. Cellobiose: the same as maltose but with a $\beta$ bond, reducing. Lactose: galactopyranose C1 joined by a $\beta$ bond to C4 of glucopyranose, reducing (the reducing end is glucose). The $\alpha$-(1→4) bond of starch and the $\beta$-(1→4) bond of cellulose are different glycosidic bonds, and glycosidases are strictly specific for the anomeric configuration; humans have amylases and maltase that hydrolyze $\alpha$-glucosidic bonds but no cellulase to hydrolyze $\beta$-(1→4) bonds (ruminants degrade cellulose with microorganisms in the rumen).

8. To synthesize cyclohexyl $\beta$-D-glucopyranoside from 2,3,4,6-tetra-$O$-acetyl-$\alpha$-D-glucopyranosyl bromide and cyclohexanol, which promoter should be chosen? What determines the configuration of the product? If the $\alpha$-glucoside is wanted, how should the protecting groups of the donor and the solvent be changed? How can the anomeric configuration of the product be confirmed by NMR?

   **Answer** Use a silver salt such as $\ce{Ag2CO3}$ or AgOTf (the Koenigs–Knorr method) to remove bromide. The acetoxy group on C2 forms, by **neighboring group participation**, an acyloxonium ion cis-fused on the $\alpha$ face, and cyclohexanol can attack C1 only from the $\beta$ face, giving the 1,2-trans $\beta$-glycoside (note the orthoester by-product). To obtain the $\alpha$-glucoside (1,2-cis), C2 must carry a nonparticipating benzyl ether (for example a tetra-$O$-benzyl-protected trichloroacetimidate or thioglycoside donor), and the reaction is run in diethyl ether or dioxane at lower temperature, exploiting the ether effect and the anomeric effect (avoid acetonitrile, which favors $\beta$). If H1 of the product is a doublet with $J_{1,2}\approx 8$ Hz ($\delta$ about 4.4), it is $\beta$; if $J_{1,2}\approx 3.5$ Hz ($\delta$ about 4.9), it is $\alpha$; $^1J_{\mathrm{C1,H1}}$ can also be measured (about 160 Hz for $\beta$, about 170 Hz for $\alpha$).

9. Why do glucose and acetone in acid give the furanose 1,2:5,6-diacetonide rather than a pyranose **ketal**? Which hydroxy group is free in the product, and what use is this?

   **Answer** Acetone ketals form preferentially as five-membered 1,3-dioxolanes, which require the two OH groups to be cis (small **dihedral angle**). In pyranose glucose in the $^4C_1$ conformation, the adjacent OH groups (C2/C3, C3/C4) are all trans and diequatorial, and a fused five-membered ketal would be strained; in the furanose, however, C1–OH and C2–OH are on the same side of the ring ($\alpha$-furanose), and C5, C6 is an exocyclic vicinal diol, so two strain-free ketals can form. Ketalization is reversible, and through the open-chain form the equilibrium is drawn toward the furanose that can form the bisketal. In the product only the C3–OH is free, and it can be modified individually by oxidation, inversion of configuration, alkylation, and so on; it is a common starting point for the synthesis of rare sugars and sugar analogs.
