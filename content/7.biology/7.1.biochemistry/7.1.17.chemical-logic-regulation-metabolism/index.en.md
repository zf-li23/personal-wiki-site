---
title: The Chemical Logic and Regulation of Metabolism
description: The method chapter of Part II. The five classes of biochemical reactions, carbanion chemistry and electron sinks, the recurring oxidation sequence, biochemical equations and enzyme names; the coenzyme–vitamin table and the chemistry of CoA, lipoate, TPP, PLP, biotin, THF, SAM and coenzyme B12; regulation of pathways, its levels and time scales, near-equilibrium and far-from-equilibrium steps, substrate cycles, adenylate kinase and the energy charge; metabolic control analysis with the summation and connectivity theorems and a numerical example.
---

The previous chapter set up the energy accounts of **metabolism** ([7.1.16](/7.1.16)). This chapter supplies the two other tools that the rest of Part II uses in every chapter. The first is chemical: although a cell catalyzes thousands of reactions, they fall into five classes, a few reaction sequences recur in many pathways, and a dozen **coenzymes**, most derived from vitamins, supply the chemistry that amino acid **side chains** cannot. Each coenzyme is explained once, here, and later chapters refer back to it. The second tool is regulatory, the "feedback control" half of the thread of Part II ([7.1.1](/7.1.1)): how fluxes are controlled, on which time scales, why the controlled steps are those far from equilibrium, how the energy state of a cell is sensed through the adenine nucleotides, and how control of a flux is shared among the **enzymes** of a pathway, the subject of metabolic control analysis. The mechanisms by which single enzymes are regulated (allostery, covalent modification, cascades, ultrasensitivity) were described in [7.1.9](/7.1.9); here they are put together at the level of pathways. The organic chemistry behind the reactions (carbonyl condensations, decarboxylations, imines and enamines) is in [6.5.16](/6.5.16)–[6.5.22](/6.5.22), and systems-level models of metabolic networks are developed in [Systems Biology](/7.9).

## 17.1. Chemical Logic of Metabolism

### 17.1.1. Two Principles

Two chemical principles explain most of the reactions of metabolism. First, a covalent bond can break in two ways. In homolytic cleavage each atom keeps one electron, giving **radicals**; in heterolytic cleavage, much more common in biochemistry, one atom keeps both electrons. Heterolytic cleavage of C–C and C–H bonds gives a **carbanion** and a **carbocation**, or a proton and a hydride ion; all three anions and cations of carbon and hydrogen are highly unstable, and much of metabolic chemistry consists of tricks to avoid them. Second, most reactions are combinations of a **nucleophile** (an electron-rich group: hydroxyl, amino, thiolate, imidazole, carbanion) with an **electrophile** (an electron-poor center: carbonyl carbon, phosphorus of a phosphate, protonated imine carbon, $\ce{H+}$); a carbon atom can be either, depending on its neighbors.

### 17.1.2. Five Classes of Reactions

Lehninger groups the reactions of living cells into five classes. They are not exclusive (an isomerization may proceed through a radical), but almost every step of the pathways in 7.1.18–7.1.29 belongs to one of them.

| Class | What happens | How the cell makes it possible | Examples |
|---|---|---|---|
| Making or breaking C–C bonds | heterolytic cleavage or formation of a C–C bond | a carbonyl (or an imine, or a coenzyme) next to the reacting carbon stabilizes the carbanion; a good leaving group ($\mathrm{PP_i}$) generates a carbocation | aldolase (**aldol reaction**), citrate synthase and thiolase (**Claisen condensation**), **decarboxylation** of β-keto acids, carboxylations (biotin, **rubisco**), prenyltransferase (carbocation) |
| Internal rearrangements, isomerizations, eliminations | redistribution of electrons without change in the overall oxidation state | **general acid–base catalysis**; enediol and enolate intermediates | phosphohexose isomerase (aldose ⇌ ketose), triose phosphate isomerase, mutases, cis–trans isomerases, dehydrations (enolase, fumarase, aconitase) |
| Free-radical reactions | homolytic cleavage | a radical initiated by a coenzyme or a metal and kept inside the **active site** | coenzyme $\mathrm{B_{12}}$ mutases, radical SAM enzymes, **ribonucleotide reductase** (7.1.28), **DNA** photolyase |
| Group transfers | an acyl, glycosyl or phosphoryl group passes from one nucleophile to another | activation by a good leaving group (phosphate, pyrophosphate, thioester); nucleophilic substitution | kinases and phosphatases, acyltransferases, glycosyltransferases, **transaminases** (7.1.22) |
| Oxidations and reductions | loss or gain of electrons | universal electron carriers (**NAD**, **NADP**, **FAD**, **FMN**; [7.1.16](/7.1.16#sec-16.5)) | dehydrogenases, oxidases, oxygenases, reductases |

Making and breaking C–C bonds. The carbon of a carbonyl group is electrophilic, and a carbonyl also stabilizes a carbanion on the adjacent carbon by delocalizing its charge as an **enolate**. Three classes of C–C reactions use this: the aldol reaction (and its reverse, the aldolase step of **glycolysis**), the Claisen condensation, in which the carbanion is stabilized by an adjacent thioester (synthesis of citrate, [6.5.22](/6.5.22#sec-22.10.2)), and decarboxylation, in which the carbanion formed as $\ce{CO2}$ leaves is stabilized by a carbonyl two atoms away (acetoacetate decarboxylase, 7.1.21). A protonated **imine** (Schiff base) is a stronger electron sink than a carbonyl, which is why class I aldolases and **transaldolase** bind their **substrates** as Schiff bases with a Lys **residue** (7.1.18), and why pyridoxal phosphate works (17.2.3). Metal ions and general acids increase the electron-withdrawing power of a carbonyl further. Whole pathways are organized around putting a carbonyl group in the right place so that the next C–C bond can be made or broken: glucose is isomerized to fructose before it is cleaved (7.1.18), and **fatty acids** are oxidized at the β carbon before the thiolytic cleavage (7.1.21). Carbocations are rarer; they are generated by the departure of pyrophosphate in the prenyltransferase reactions of **isoprenoid** synthesis (7.1.26).

Rearrangements and eliminations. In the isomerization of glucose 6-phosphate to fructose 6-phosphate, C-1 is reduced (aldehyde to alcohol) and C-2 oxidized (alcohol to ketone) through an enediol intermediate, with two ionizable groups of the enzyme acting as general acid and general base; the molecule as a whole is neither oxidized nor reduced. Elimination of water from an alcohol introduces a C=C bond (enolase, fumarase); additions of water to C=C bonds are the reverse.

Radical reactions. Once thought rare, radical mechanisms occur where no polar mechanism is possible: rearrangements that exchange a hydrogen atom and a group on adjacent carbons (coenzyme $\mathrm{B_{12}}$, 17.2.5), reduction of ribonucleotides to deoxyribonucleotides, and many reactions initiated by the 5′-deoxyadenosyl radical generated from S-adenosylmethionine by the "radical SAM" enzymes.

Group transfers. Acyl transfer proceeds by addition of a nucleophile to the carbonyl carbon, giving a **tetrahedral intermediate** (**nucleophilic acyl substitution**; the chymotrypsin mechanism of [7.1.8](/7.1.8#sec-8.4.1) is an example). Glycosyl transfer is a substitution at the anomeric carbon, an acetal carbon. Phosphoryl transfer is an in-line displacement at phosphorus with a pentacovalent transition state ([7.1.16](/7.1.16#sec-16.3.4)). A general theme is activation: a poor leaving group such as –OH is converted into a good one (phosphate, pyrophosphate, AMP, CoA thioester) before the substitution.

Oxidations and reductions. Many biological oxidations are dehydrogenations, in which two electrons and two protons are removed and passed to NAD⁺ or FAD; the energy of most catabolic pathways is released in such steps ([7.1.16](/7.1.16#sec-16.4)).

### 17.1.3. A Recurring Sequence of Three Reactions

One sequence of three reactions occurs in at least three central pathways: the oxidation of a methylene group next to a carbonyl to a new carbonyl,

$$
\ce{-CH2-CH2-} \xrightarrow{\text{FAD}} \ce{-CH=CH-} \xrightarrow{\ce{H2O}} \ce{-CH(OH)-CH2-} \xrightarrow{\ce{NAD+}} \ce{-C(=O)-CH2-}.
$$
It forms the last three steps of the **citric acid cycle** (succinate → fumarate → malate → oxaloacetate, 7.1.20) and the four steps of each turn of **β oxidation**, after which a thiolase cleaves the β-keto thioester (7.1.21); fatty acid synthesis runs the same sequence in reverse, with NADPH as reductant for both reductions (7.1.26). Its chemistry explains the choice of electron acceptors: the first oxidation, of a saturated C–C bond, has a reduction potential near 0 V (fumarate/succinate $+0.031\,\mathrm{V}$), too positive to reduce $\ce{NAD+}$ ($\Delta_{\mathrm{r}}G'^{\circ} \approx +68\,\mathrm{kJ\,mol^{-1}}$), and is catalyzed by **flavoproteins** whose bound FAD has a potential close to that of the substrate; the third, of a secondary alcohol, is reducing enough for $\ce{NAD+}$ ([7.1.16](/7.1.16#sec-16.5.2)).

![The recurring three-step oxidation. Top: the general sequence, in which a methylene group β to a carbonyl (or thioester) becomes a carbonyl: dehydrogenation of –CH₂–CH₂– to a trans double bond by a flavoprotein (FAD → FADH₂), hydration of the double bond, and oxidation of the hydroxyl to a ketone by an NAD⁺-dependent dehydrogenase. Columns: the citric acid cycle (succinate → fumarate → malate → oxaloacetate; succinate dehydrogenase, fumarase, malate dehydrogenase), β oxidation of a fatty acyl-CoA (acyl-CoA dehydrogenase, enoyl-CoA hydratase, β-hydroxyacyl-CoA dehydrogenase) and fatty acid synthesis, which runs the sequence backwards on an acyl carrier protein with NADPH as reductant for both reductions](./plots/recurring-reactions.py)

### 17.1.4. Biochemical Equations and Enzyme Names

Biochemists write equations as sums of species. "ATP" in ATP + $\ce{H2O}$ → ADP + $\mathrm{P_i}$ stands for the mixture of $\ce{ATP^4-}$, $\ce{HATP^3-}$, $\ce{MgATP^2-}$ and the other forms present at a given pH and $[\ce{Mg^2+}]$; such a biochemical equation balances C, N, O and P but not H, Mg or charge, and its $K'$ depends on pH and $[\ce{Mg^2+}]$ ([7.1.16](/7.1.16#sec-16.2.1)). The chemical equation $\ce{ATP^4- + H2O -> ADP^3- + HPO4^2- + H+}$ balances every atom and charge and is the one to use for a mechanism. Following Lehninger, we use biochemical equations except where the mechanism is the subject.

Enzyme names follow conventions that are worth learning once (Lehninger 8e, Box 13-1):

| Name | Reaction | Example |
|---|---|---|
| kinase | transfer of a phosphoryl group from a nucleoside triphosphate to an acceptor | hexokinase, PEP carboxykinase, **protein kinases** |
| phosphatase | hydrolytic removal of a phosphoryl group (water attacks) | fructose 1,6-bisphosphatase, **phosphoprotein phosphatases** |
| phosphorylase | **phosphorolysis**: cleavage of a bond by attack of $\mathrm{P_i}$, which becomes attached | **glycogen phosphorylase** (glucose 1-phosphate) |
| synthase / synthetase | condensation without / with a nucleoside triphosphate as energy source | citrate synthase / succinyl-CoA synthetase |
| ligase | joining of two molecules with energy from ATP (or NAD); synthetases are ligases | **DNA ligase** |
| lyase | cleavage (or, in reverse, addition) by elimination, not by hydrolysis or oxidation | aldolase, fumarase, pyruvate decarboxylase |
| mutase, isomerase, epimerase | intramolecular group shift; isomerization; inversion at one stereocenter | phosphoglycerate mutase; triose phosphate isomerase; UDP-glucose 4-epimerase |
| dehydrogenase | oxidation with NAD⁺, NADP⁺ or FAD as acceptor (not $\ce{O2}$) | lactate dehydrogenase |
| oxidase | oxidation with $\ce{O2}$ as acceptor, O not incorporated in the product | **cytochrome oxidase**, **xanthine oxidase** |
| oxygenase (mono-, di-) | one or both O atoms of $\ce{O2}$ incorporated in the product | **cytochrome P-450** monooxygenases, **cyclooxygenase** |
| carboxylase / decarboxylase | addition / removal of $\ce{CO2}$ | pyruvate carboxylase (biotin) / pyruvate decarboxylase (TPP) |
| aminotransferase / amidotransferase | transfer of an amino group (PLP) / of the amide N of Gln | aspartate aminotransferase / glutamine–**PRPP** amidotransferase |

Many enzymes keep the name of the reaction in which they were first assayed, even when they work in the opposite direction in the cell: pyruvate kinase transfers a phosphoryl group from PEP to ADP, and lactate dehydrogenase usually reduces pyruvate.

## 17.2. Coenzymes and Vitamins

### 17.2.1. Vitamins and the Coenzyme Table

Amino acid side chains can act as acids, bases and nucleophiles, but they cannot carry hydride ions, stabilize the carbanion of a decarboxylating keto acid or transfer one-carbon units. These jobs are done by **coenzymes**, organic **cofactors** that bind to enzymes and are regenerated after each turnover ([7.1.3](/7.1.3), [7.1.8](/7.1.8#sec-8.1.2)). Most coenzymes participate in a narrow range of related reactions, so the coenzyme of an enzyme is often a good guide to its chemistry. Animals have lost the ability to make many of them and must obtain their precursors in the diet.

**Definition 17.2.1 (Vitamin)** A **vitamin** is an organic compound required in small amounts in the diet of an animal because it cannot synthesize it in sufficient quantity. The water-soluble vitamins (the B vitamins and vitamin C) are mostly precursors of coenzymes; the fat-soluble vitamins (A, D, E, K) are precursors of a chromophore, a hormone, an antioxidant and a cofactor ([7.1.12](/7.1.12#sec-12.5.4)).

The table collects the coenzymes of Part II. Each is described below by the chemistry that makes it useful.

| Vitamin | Coenzyme | Group carried | Chemical principle | Representative enzymes (chapter) | Deficiency |
|---|---|---|---|---|---|
| $\mathrm{B_1}$ thiamine | thiamine pyrophosphate (TPP) | aldehydes (activated two-carbon units) | thiazolium C-2 carbanion (ylide) adds to carbonyls; the ring is an electron sink | pyruvate decarboxylase (7.1.18), pyruvate and α-ketoglutarate dehydrogenases (7.1.20), **transketolase** (7.1.18, 7.1.25) | beriberi, Wernicke–Korsakoff syndrome |
| $\mathrm{B_2}$ riboflavin | FAD, FMN | electrons (1 or 2) and protons | isoalloxazine ring with semiquinone; potential set by the **protein** | succinate and acyl-CoA dehydrogenases (7.1.20–7.1.21), **Complex I** (7.1.23) | ariboflavinosis (cheilosis, angular stomatitis) |
| $\mathrm{B_3}$ niacin | NAD, NADP | hydride ion | C-4 of the pyridinium ring accepts $\ce{H-}$ | dehydrogenases (all chapters) | pellagra |
| $\mathrm{B_5}$ pantothenate | coenzyme A, phosphopantetheine | acyl groups | thioester: activated for transfer and for carbanion formation at C-α | PDH (7.1.20), β oxidation (7.1.21), **fatty acid synthase** (7.1.26) | rare ("burning feet") |
| $\mathrm{B_6}$ pyridoxine, pyridoxal, pyridoxamine | pyridoxal phosphate (PLP) | amino groups; electron sink for reactions at C-α of amino acids | Schiff base with the substrate; the protonated pyridine ring withdraws electrons | aminotransferases, amino acid decarboxylases (7.1.22, 7.1.27), glycogen phosphorylase (7.1.19) | dermatitis, neuropathy, convulsions in infants, microcytic anemia |
| $\mathrm{B_7}$ biotin | biotin bound to Lys (biocytin) | $\ce{CO2}$ | N-1′ of the ureido ring carries a carboxyl group on a long swinging arm | pyruvate carboxylase (7.1.19), **acetyl-CoA carboxylase** (7.1.26), propionyl-CoA carboxylase (7.1.21) | rare (raw egg white avidin): dermatitis, hair loss |
| $\mathrm{B_9}$ folate | tetrahydrofolate (THF) | one-carbon units (formyl, methenyl, methylene, methyl) | N-5 and N-10 carry the unit at several oxidation levels | serine hydroxymethyltransferase, **thymidylate synthase**, purine synthesis (7.1.27–7.1.28) | megaloblastic anemia; neural tube defects |
| $\mathrm{B_{12}}$ cobalamin | 5′-deoxyadenosylcobalamin, methylcobalamin | H atoms and alkyl groups | weak Co–C bond breaks homolytically (radical); $\ce{Co^+}$ is a supernucleophile | **methylmalonyl-CoA mutase** (7.1.21), methionine synthase (7.1.22) | pernicious anemia, neurological damage |
| C ascorbate | (cosubstrate) | electrons | keeps the $\ce{Fe^2+}$ of hydroxylases reduced | prolyl and lysyl hydroxylases (**collagen**) | scurvy |
| (not required by animals) | lipoate (lipoamide) | electrons and acyl groups | dithiolane ring on a Lys swinging arm | PDH and α-ketoglutarate dehydrogenase (7.1.20) | (arsenite poisoning blocks it) |
| (made from Met + ATP) | S-adenosylmethionine (SAM) | methyl groups; 5′-deoxyadenosyl radical | sulfonium ion: methyl is an excellent electrophile | DNA, **RNA**, protein and small-molecule methyltransferases | — |

### 17.2.2. Carriers of Acyl Groups and Aldehydes: CoA, Lipoate and TPP

**Definition 17.2.2 (Coenzyme A)** **Coenzyme A** (CoA, CoA-SH) consists of β-mercaptoethylamine, pantothenate (vitamin $\mathrm{B_5}$) and 3′-phospho-ADP; its terminal thiol forms thioesters with acyl groups, as in acetyl-CoA.

```smiles
CC(C)(COP(=O)([O-])OP(=O)([O-])OC[C@H]1O[C@@H](n2cnc3c(N)ncnc32)[C@H](O)[C@@H]1OP(=O)([O-])[O-])[C@@H](O)C(=O)NCCC(=O)NCCS CoA-SH
```

A thioester activates the acyl group in two ways ([7.1.16](/7.1.16#sec-16.3.3), [6.5.22](/6.5.22#sec-22.10.2)): the carbonyl carbon is a good electrophile with a good leaving group, the thiolate (acyl transfer; $\Delta_{\mathrm{r}}G'^{\circ}$ of acetyl-CoA hydrolysis $-31.4\,\mathrm{kJ\,mol^{-1}}$), and the α-hydrogens are more acidic than those of an oxygen ester, so the α carbon can become a nucleophile (Claisen condensations). The same phosphopantetheine arm, attached to a Ser residue, forms the **acyl carrier protein** of fatty acid synthesis (7.1.26). The adenosine part plays no chemical role; it is a handle for binding ([7.1.11](/7.1.11#sec-11.5)).

**Definition 17.2.3 (Lipoate)** **Lipoate** (lipoic acid, 6,8-dithiooctanoic acid) is a coenzyme bound in amide linkage to a Lys residue (lipoamide), whose cyclic disulfide accepts two electrons and an acyl group on its reduced dithiol; it is the swinging arm of the α-keto acid dehydrogenase complexes.

```smiles
O=C(O)CCCC[C@@H]1CCSS1 lipoate
```

**Definition 17.2.4 (Thiamine Pyrophosphate)** **Thiamine pyrophosphate** (TPP, thiamine diphosphate) is the coenzyme form of thiamine (vitamin $\mathrm{B_1}$); the carbon C-2 between N and S of its thiazolium ring, deprotonated to a carbanion (ylide), adds to carbonyl groups, and the positively charged ring stabilizes the carbanion that forms when a C–C bond next to the former carbonyl is broken.

```smiles
Cc1ncc(C[n+]2csc(CCOP(=O)([O-])OP(=O)([O-])[O-])c2C)c(N)n1 TPP
```

TPP solves the problem of breaking the bond between a carbonyl carbon and the adjacent carbon, as in the decarboxylation of α-keto acids, where no carbonyl two atoms away is available to stabilize the developing charge. The C-2 proton of the thiazolium ring is unusually acidic, because the adjacent positive N and the S atom stabilize the ylide. The ylide attacks the keto carbon of pyruvate; $\ce{CO2}$ leaves, and the electrons flow into the ring, giving a resonance-stabilized enamine (hydroxyethyl-TPP, "active acetaldehyde"). This intermediate is then protonated and releases acetaldehyde (pyruvate decarboxylase, 7.1.18), or is oxidized and its two-carbon unit transferred to lipoamide (pyruvate dehydrogenase, 7.1.20), or adds to an aldose (transketolase, 7.1.18). In each case TPP carries an aldehyde group as a nucleophile, an inversion of the normal electrophilic reactivity of a carbonyl carbon ("umpolung").

![Thiamine pyrophosphate in the decarboxylation of pyruvate (pyruvate decarboxylase). The C-2 carbanion (ylide) of the thiazolium ring attacks the carbonyl carbon of pyruvate; in the adduct the C–COO⁻ bond breaks and the electrons flow into the positively charged thiazolium ring, which acts as an electron sink, giving the enamine hydroxyethyl-TPP and CO₂. Protonation and release of acetaldehyde regenerate the ylide. R and R′ are the aminopyrimidine and pyrophosphoethyl substituents](./plots/tpp-decarboxylation.py)

### 17.2.3. Pyridoxal Phosphate

**Definition 17.2.5 (Pyridoxal Phosphate)** **Pyridoxal phosphate** (PLP), the coenzyme form of vitamin $\mathrm{B_6}$, is bound in the resting enzyme as a Schiff base (internal aldimine) with a Lys ε-amino group; an amino acid substrate displaces the Lys to form an external aldimine, in which the protonated pyridine ring acts as an electron sink for reactions at the α carbon.

```smiles
Cc1ncc(COP(=O)([O-])[O-])c(C=O)c1O PLP
```

PLP is the most versatile coenzyme. In the external aldimine, any of the three bonds to the α carbon of the amino acid (to H, to the carboxylate or to the side chain) can break, because the resulting carbanion is delocalized into the pyridinium ring (the quinonoid intermediate). Which bond breaks is decided by the enzyme, which holds that bond perpendicular to the plane of the conjugated system so that it overlaps with the π system (Dunathan's hypothesis). Breaking the C–H bond leads to **transamination** (7.1.22) and racemization; breaking the C–$\ce{COO-}$ bond, to decarboxylation (**biogenic amines**, 7.1.27); breaking the C–R bond, to aldol-type cleavages (serine hydroxymethyltransferase). In glycogen phosphorylase PLP plays an entirely different role: its phosphate acts as a general acid (7.1.19). Some 4% of all enzyme activities classified by the EC list depend on PLP.

### 17.2.4. Carriers of One-Carbon Units: Biotin, Tetrahydrofolate and S-Adenosylmethionine

Metabolism uses three carriers of one-carbon groups, at three oxidation levels.

**Definition 17.2.6 (Biotin)** **Biotin** (vitamin $\mathrm{B_7}$) is a coenzyme attached in amide linkage to a Lys residue (biocytin) of carboxylases; it carries $\ce{CO2}$, activated by ATP as carboxyphosphate, as a carboxyl group on N-1′ of its ureido ring, the most oxidized one-carbon unit.

```smiles
O=C(O)CCCC[C@@H]1SC[C@@H]2NC(=O)N[C@H]12 biotin
```

Biotin-dependent carboxylases work in two half-reactions at two active sites: the carboxylation of biotin with bicarbonate and ATP, and the transfer of the carboxyl group to the substrate (pyruvate, acetyl-CoA, propionyl-CoA). The biotinyl-Lys arm, about 1.4 nm long, carries the $\ce{CO2}$ between the two sites. Egg white contains avidin, which binds biotin with $K_{\mathrm{d}} \approx 10^{-15}\,\mathrm{M}$, among the strongest **noncovalent interactions** known (hence biotin deficiency after eating many raw eggs, and the biotin–streptavidin tag of the laboratory).

**Definition 17.2.7 (Tetrahydrofolate)** **Tetrahydrofolate** (THF, $\mathrm{H_4}$folate), the coenzyme form of folate (vitamin $\mathrm{B_9}$), consists of a reduced pterin, p-aminobenzoate and one or more glutamate residues; it carries one-carbon units on N-5, N-10 or both, at the oxidation levels of methanol (methyl), formaldehyde (methylene) and formate (formyl, formimino, methenyl).

```smiles
Nc1nc2c(c(=O)[nH]1)N[C@@H](CNc1ccc(cc1)C(=O)N[C@@H](CCC(=O)O)C(=O)O)CN2 THF
```

The one-carbon units on THF are interconverted by oxidation and reduction (with NADP) and used in the synthesis of purines, thymidylate, methionine and serine/glycine (7.1.27–7.1.28). Because DNA synthesis needs folate, its **antagonists** (methotrexate, an inhibitor of **dihydrofolate reductase**) are anticancer drugs and the sulfonamides, which block folate synthesis in bacteria, are antibiotics; deficiency causes megaloblastic anemia and, in pregnancy, neural tube defects, which is why flour is fortified with folic acid in many countries.

**Definition 17.2.8 (S-Adenosylmethionine)** **S-Adenosylmethionine** (SAM, AdoMet) is formed from methionine and ATP by transfer of the adenosyl group to the sulfur (with release of all three phosphates as $\mathrm{P_i}$ and $\mathrm{PP_i}$); its sulfonium ion makes the methyl group a strong electrophile, and SAM is the donor in almost all biological methylations.

```smiles
C[S+](CC[C@H](N)C(=O)O)C[C@H]1O[C@@H](n2cnc3c(N)ncnc32)[C@H](O)[C@@H]1O SAM
```

The transfer of a methyl group from SAM to a nucleophile (an O, N, S or C atom of a DNA base, a **histone** Lys, a catecholamine) is much faster than from $\mathrm{N^5}$-methyl-THF (SAM is about 1000 times more reactive as a methyl donor). The product S-adenosylhomocysteine is hydrolyzed to homocysteine, which is remethylated by methionine synthase with methyl-THF and coenzyme $\mathrm{B_{12}}$ (the activated methyl cycle, 7.1.22). In the radical SAM enzymes, a reduced iron–sulfur cluster cleaves SAM to methionine and the 5′-deoxyadenosyl radical, which starts radical reactions in more than 100 000 known protein sequences.

### 17.2.5. Coenzyme B12

**Definition 17.2.9 (Cobalamin)** **Cobalamin** (vitamin $\mathrm{B_{12}}$) is a corrin ring with a central cobalt ion coordinated by a dimethylbenzimidazole nucleotide; in its coenzyme forms the cobalt carries a 5′-deoxyadenosyl group (5′-deoxyadenosylcobalamin, coenzyme $\mathrm{B_{12}}$) or a methyl group (methylcobalamin), bound by a Co–C bond.

The Co–C bond of adenosylcobalamin is weak (bond dissociation energy about $130\,\mathrm{kJ\,mol^{-1}}$) and is broken homolytically in the active site to $\ce{Co^{2+}}$ and a 5′-deoxyadenosyl radical, which abstracts a hydrogen atom from the substrate; the substrate radical rearranges (a group moves to the adjacent carbon) and takes the hydrogen back. This is how methylmalonyl-CoA mutase converts methylmalonyl-CoA to succinyl-CoA in the oxidation of odd-chain fatty acids (7.1.21). In methionine synthase, methylcobalamin transfers its methyl group heterolytically, and the $\ce{Co^+}$ left behind is a very strong nucleophile that takes the next methyl group from methyl-THF. $\mathrm{B_{12}}$ is made only by bacteria and archaea; humans obtain it from animal food and absorb it with the help of intrinsic factor from the stomach. Failure of absorption (pernicious anemia, usually autoimmune) or a strict vegan diet without supplements leads to megaloblastic anemia, because folate is trapped as methyl-THF, and to neurological damage. Its structure, with more than 180 atoms, was solved by X-ray crystallography by Dorothy Hodgkin (Nobel Prize 1964).

The fat-soluble vitamins were treated with the **lipids** ([7.1.12](/7.1.12#sec-12.5.4)): vitamin A as the chromophore retinal of **rhodopsin** (7.1.14) and as the **hormone** retinoic acid, vitamin D as the precursor of the hormone calcitriol, vitamin E as a membrane antioxidant, vitamin K as the cofactor of γ-carboxylation of coagulation factors ([7.1.9](/7.1.9#sec-9.5.5)). Vitamin C (ascorbate) is a reductant rather than a group carrier.

```smiles
OC[C@H](O)[C@H]1OC(=O)C(O)=C1O ascorbate
```

## 17.3. Regulation of Metabolic Pathways

### 17.3.1. Pathways, Fluxes and Homeostasis

Dividing metabolism into pathways is a convenience; in the cell every pathway is connected to many others through shared metabolites. Glucose 6-phosphate in a hepatocyte can be degraded by glycolysis, oxidized in the **pentose phosphate pathway**, stored as **glycogen**, hydrolyzed to glucose for export, or converted into other sugars for **glycosylation**; every "decision" to use it one way changes the flow through all the others.

**Definition 17.3.1 (Metabolic Pathway, Metabolic Flux and Committed Step)** A **metabolic pathway** is a series of enzyme-catalyzed reactions in which the product of one is the substrate of the next, leading from a defined starting compound to a defined product; its intermediates are metabolites. The **metabolic flux** $J$ through a pathway in a steady state is the net rate of conversion of substrate into product (in $\mathrm{mol\,s^{-1}}$ per volume or per mass of tissue), equal to the net rate of every step. The **committed step** of a pathway is the first reaction that is essentially irreversible under cellular conditions and whose product has no other fate than the pathway.

In a steady state each intermediate is formed and consumed at the same rate, so its concentration stays constant while the flux through it may change many-fold: in the **dynamic steady state** ([7.1.1](/7.1.1#sec-1.3.1)) blood glucose is held near 5 mM whatever the rates of uptake from the gut, release by the liver and use by the tissues. It is useful to distinguish metabolic regulation, which holds a quantity (a concentration) constant while the flux changes, from metabolic control, which changes the output of a pathway in response to an outside signal. Both rely on the same molecular mechanisms; failure of either is the basis of many diseases, of which **diabetes mellitus**, a failure of glucose homeostasis, is the most common (7.1.29). About 12% of human **genes** encode regulatory proteins, among them more than 500 protein kinases.

### 17.3.2. Levels and Time Scales of Regulation

The rate of a reaction catalyzed by an enzyme is the product of the number of enzyme molecules and the activity of each, and both can be changed. The mechanisms differ above all in speed.

| Level | Mechanism | Typical time scale | Example |
|---|---|---|---|
| Amount of enzyme | **transcription** (transcription factors binding response elements), **mRNA** stability, **translation** | 10 min to hours | **insulin** induces **glucokinase** and lipogenic enzymes; **glucagon** induces PEP carboxykinase (7.1.19, 7.1.29) |
| | protein degradation (**ubiquitin**–**proteasome**) | hours to days (average half-life 0.9 days in liver, 10.7 days in muscle) | **HMG-CoA reductase** degraded when **sterols** are high (7.1.26) |
| Access of enzyme to substrate | compartmentation, transport across membranes | seconds to minutes | glucose uptake by GLUT4 in muscle (7.1.13); **carnitine shuttle** (7.1.21) |
| Activity of each molecule | substrate concentration relative to $K_{\mathrm{M}}$ | instantaneous (as fast as concentrations change) | hexokinase **isozymes** and blood glucose (7.1.19) |
| | **allosteric effectors** ([7.1.9](/7.1.9#sec-9.5.2)) | milliseconds to seconds | PFK-1 by ATP, AMP, citrate (7.1.18) |
| | reversible covalent modification ([7.1.9](/7.1.9#sec-9.5.3)) | seconds to minutes | glycogen phosphorylase and synthase (7.1.19) |
| | binding of regulatory proteins | seconds to minutes | **PKA** regulatory **subunits** and **cAMP** (7.1.14) |

![Time scales of metabolic regulation. Horizontal bars span the typical response times of each mechanism on a logarithmic time axis, from the turnover of a single enzyme molecule (microseconds to milliseconds) through allosteric regulation and covalent modification by protein kinases and phosphatases, to changes in the amount of enzyme by transcription, translation and protein degradation (hours to days). The fast mechanisms adjust the activity of existing molecules and respond to metabolites and second messengers; the slow ones change the enzyme complement of a tissue in response to diet and hormones](./plots/regulation-timescales.py)

An enzyme with a short half-life can reach a new steady-state level fast: after a change in its synthesis rate, the amount of a protein approaches its new level exponentially with the time constant of its degradation, $\tau = t_{1/2}/\ln 2$. Fast turnover costs energy, which is the price of responsiveness. Most enzymes are regulated at several levels at once, which gives both rapid and lasting adaptation.

### 17.3.3. Near-Equilibrium and Far-from-Equilibrium Steps

Not every step of a pathway can control its flux. Consider a step S ⇌ P with one-way rates $J_{+}$ (forward) and $J_{-}$ (backward), so that the net rate is $J = J_{+} - J_{-}$. For any enzyme-catalyzed reaction the ratio of the one-way fluxes, which can be measured with isotope tracers, is fixed by its actual Gibbs energy ([7.1.16](/7.1.16#sec-16.2.2)):

**Formula 17.3.1 (Flux–Force Relation)**

$$
\frac{J_{-}}{J_{+}} = \frac{Q}{K'} = \mathrm{e}^{\Delta_{\mathrm{r}}G/RT}, \qquad \frac{J}{J_{+}} = 1 - \mathrm{e}^{\Delta_{\mathrm{r}}G/RT}. \tag{17.1}
$$
A step with $\Delta_{\mathrm{r}}G = -2\,\mathrm{kJ\,mol^{-1}}$ at $37\,^\circ\mathrm{C}$ runs backward at 46% of its forward rate, so its net flux is only half of its forward flux; a step with $\Delta_{\mathrm{r}}G = -20\,\mathrm{kJ\,mol^{-1}}$ has $J_{-}/J_{+} = 4 \times 10^{-4}$ and is effectively irreversible. In practice a step with $Q$ within one to two orders of magnitude of $K'$, or $\lvert\Delta_{\mathrm{r}}G\rvert$ less than a few kJ mol⁻¹, is called near equilibrium.

The two kinds of steps behave differently. A near-equilibrium step usually has an enzyme with a capacity far larger than the flux; its net rate is the small difference between two large one-way rates and follows any change in the concentrations of its substrate or product. It passes on whatever flux the neighboring steps impose, in either direction, and it cannot be the place where the flux is set (its flux control coefficient is small, 17.4). A step far from equilibrium is limited by the activity of its enzyme, its rate is insensitive to the concentration of its product, and changing the activity of its enzyme changes the flux through the pathway. Regulated enzymes therefore catalyze reactions far from equilibrium, and pathways have them where they need them: at the committed step, at **branch points**, and wherever a reversal of flux must be prevented.

The data for glycolysis in heart muscle (Lehninger 8e, Table 13-10, from Newsholme and Start) show the pattern. The **mass-action ratios** of hexokinase, phosphofructokinase-1 and pyruvate kinase are three to five orders of magnitude below their equilibrium constants, those of the other seven enzymes within about one order:

| Enzyme | $K'$ | $Q$ (heart) | $\Delta_{\mathrm{r}}G'^{\circ}$ / (kJ mol⁻¹) | $\Delta_{\mathrm{r}}G$ (heart) / (kJ mol⁻¹) | Near equilibrium? |
|---|---|---|---|---|---|
| hexokinase | $1 \times 10^{3}$ | $8 \times 10^{-2}$ | $-17$ | $-27$ | no |
| phosphohexose isomerase | $4 \times 10^{-1}$ | $2.4 \times 10^{-1}$ | $+2.2$ | $-1.4$ | yes |
| phosphofructokinase-1 | $1.0 \times 10^{3}$ | $3 \times 10^{-2}$ | $-14$ | $-23$ | no |
| aldolase | $1.0 \times 10^{-4}$ | $9 \times 10^{-6}$ | $+24$ | $-6.0$ | yes |
| triose phosphate isomerase | $4 \times 10^{-2}$ | $2.4 \times 10^{-1}$ | $+7.5$ | $+3.8$ | yes |
| GAPDH + phosphoglycerate kinase | $2 \times 10^{3}$ | $9.0$ | $-13$ | $+3.5$ | yes |
| phosphoglycerate mutase | $1 \times 10^{-1}$ | $1.2 \times 10^{-1}$ | $+4.4$ | $+0.6$ | yes |
| enolase | $3$ | $1.4$ | $-3.2$ | $-0.5$ | yes |
| pyruvate kinase | $2 \times 10^{4}$ | $40$ | $-31$ | $-17$ | no |

(Small positive values of $\Delta_{\mathrm{r}}G$ for net forward steps are within the uncertainty of the measured concentrations, most of them total rather than free concentrations.)

![Near-equilibrium and far-from-equilibrium steps. A: the flux–force relation (Formula 17.3.1). The ratio of backward to forward one-way flux, and the fraction of the forward flux that is net flux, against −ΔrG at 37 °C; below about 6 kJ mol⁻¹ (shaded) a step runs substantially in both directions. B: actual Gibbs energy of the glycolytic steps in heart muscle (Lehninger 8e, Table 13-10): the three steps catalyzed by hexokinase, phosphofructokinase-1 and pyruvate kinase are far from equilibrium and are the regulated steps; the others are near equilibrium](./plots/near-equilibrium.py)

The far-from-equilibrium steps also protect the cell. If phosphofructokinase-1 were allowed to reach equilibrium ($K' \approx 1000$) at millimolar fructose 6-phosphate and ATP, fructose 1,6-bisphosphate would rise toward molar concentrations, with osmotic disaster. If ATP hydrolysis approached equilibrium, ATP would lose its **phosphorylation potential**. Enzymes that catalyze highly exergonic reactions are therefore regulated with particular care.

### 17.3.4. Opposing Pathways and Substrate Cycles

A pathway and its reverse (glycolysis and **gluconeogenesis**, fatty acid oxidation and synthesis, glycogen breakdown and synthesis) share their near-equilibrium steps but use different enzymes at the irreversible steps, so that each direction is exergonic. At each such pair, both enzymes are present in the same cell.

**Definition 17.3.2 (Substrate Cycle)** A pair of opposing, irreversible reactions catalyzed by different enzymes, such as fructose 6-phosphate + ATP → fructose 1,6-bisphosphate + ADP (PFK-1) and fructose 1,6-bisphosphate + $\ce{H2O}$ → fructose 6-phosphate + $\mathrm{P_i}$ (FBPase-1), forms a **substrate cycle**; its net result is the hydrolysis of ATP. When it runs without metabolic purpose it is called a futile cycle.

Cells regulate the two enzymes of a substrate cycle reciprocally, so that the same signal activates one and inhibits the other (AMP and **fructose 2,6-bisphosphate** activate PFK-1 and inhibit FBPase-1, 7.1.18–7.1.19); otherwise ATP would be wasted as heat. A modest rate of cycling is nevertheless useful, because it amplifies the sensitivity of the net flux. If the forward rate is $v_{\mathrm{f}}$ and the reverse rate $v_{\mathrm{r}}$, the net flux is $J = v_{\mathrm{f}} - v_{\mathrm{r}}$. An effector that increases $v_{\mathrm{f}}$ and decreases $v_{\mathrm{r}}$ by the same fraction $a$ changes $J$ by

$$
\frac{\Delta J}{J} = a\,\frac{v_{\mathrm{f}} + v_{\mathrm{r}}}{v_{\mathrm{f}} - v_{\mathrm{r}}}, \tag{17.2}
$$
so with $v_{\mathrm{r}} = 0.8\,v_{\mathrm{f}}$ a 10% change of each enzyme activity changes the net flux by 90%. The cost is the ATP hydrolyzed by the cycling, and the heat released is put to use in some cases (the flight muscles of bumblebees; brown fat uses a different mechanism, 7.1.23). The quantitative model is in [7.1.19](/7.1.19). Compartmentation is the other way of separating opposing pathways: fatty acids are oxidized in the mitochondrial matrix and synthesized in the cytosol, and the two pools of nicotinamide nucleotides are kept at different redox states ([7.1.16](/7.1.16#sec-16.5.1)).

### 17.3.5. Adenine Nucleotides and the Energy Charge

After the protection of its DNA, perhaps nothing is more important to a cell than a constant supply of ATP. Many ATP-using enzymes have $K_{\mathrm{M}}$ values for ATP of 0.1 to 1 mM, and [ATP] in a typical cell is 2 to 10 mM. A large fall in [ATP] would therefore lower the rates of hundreds of reactions at once (a kinetic effect), and it would also lower the phosphorylation potential (a thermodynamic effect, [7.1.16](/7.1.16#sec-16.3.2)). It is not surprising that the adenine nucleotides are among the most important allosteric effectors of metabolism.

Atkinson (1968) proposed a single number for the energy state of the adenylate pool, by analogy with the charge of a battery.

**Definition 17.3.3 (Energy Charge)** The **energy charge** of the adenylate system is

$$
\mathrm{EC} = \frac{[\mathrm{ATP}] + \tfrac12[\mathrm{ADP}]}{[\mathrm{ATP}] + [\mathrm{ADP}] + [\mathrm{AMP}]}, \tag{17.3}
$$
the number of phosphoanhydride bonds per adenine nucleotide divided by two; it ranges from 0 (all AMP) to 1 (all ATP).

Most cells keep the energy charge between about 0.8 and 0.95. Atkinson observed two types of response of enzymes to it. Enzymes of ATP-generating (catabolic) sequences, such as PFK-1 and pyruvate kinase, are inhibited as EC rises (R-type, for regenerating); enzymes of ATP-using (biosynthetic) sequences are activated (U-type, for utilizing). The two curves cross steeply near the operating range, so that the energy charge is stabilized: if it falls, ATP production speeds up and ATP consumption slows down.

AMP is an even more sensitive indicator than ATP. **Adenylate kinase** keeps the reaction 2 ADP ⇌ ATP + AMP near equilibrium ($K' = [\mathrm{ATP}][\mathrm{AMP}]/[\mathrm{ADP}]^2 \approx 1$; [7.1.16](/7.1.16#sec-16.3.5)), so

$$
[\mathrm{AMP}] = K'\,\frac{[\mathrm{ADP}]^2}{[\mathrm{ATP}]}. \tag{17.4}
$$
Because [ATP] is several times [ADP], and both are much larger than [AMP], a small fractional fall $\delta$ in [ATP] (the total adenylate staying constant) increases [ADP] by roughly the factor $1 + \delta[\mathrm{ATP}]/[\mathrm{ADP}]$ and [AMP] by roughly the square of that factor. With [ATP]/[ADP] = 10, a 10% fall in ATP nearly doubles [ADP] and increases [AMP] about fourfold; the higher the ratio of free ATP to free ADP, the larger the amplification. This is why the principal sensor of cellular energy, the **AMP-activated protein kinase** (7.1.29), responds to AMP (and ADP), and why AMP activates PFK-1 and glycogen phosphorylase in muscle. The redox ratios $[\ce{NAD+}]/[\mathrm{NADH}]$ and $[\ce{NADP+}]/[\mathrm{NADPH}]$, acetyl-CoA and citrate are the other common signals of the fuel state.

![The adenylate system. A: fractions of ATP, ADP and AMP against the energy charge (Definition 17.3.3), with adenylate kinase at equilibrium (K′ = 1); the shaded band is the range maintained by most cells. B: model responses of an R-type enzyme (in an ATP-regenerating pathway; an MWC enzyme inhibited by ATP at a regulatory site and activated by AMP) and a U-type enzyme (in an ATP-using pathway; Michaelis–Menten in ATP with ADP as competitive inhibitor) to the energy charge; parameters illustrative, after the curves of Atkinson. C: amplification of the AMP signal by adenylate kinase: fold increase in [AMP] against the fractional fall in [ATP] at constant total adenylate, for initial [ATP]/[ADP] ratios of 5, 10 and 30](./plots/energy-charge.py)

## 17.4. Metabolic Control Analysis

### 17.4.1. The Rate-Limiting Step and Its Problem

It was long assumed that each pathway has one rate-limiting enzyme, typically the first committed step, whose activity alone sets the flux. The assumption predicts that overproducing that enzyme should increase the flux in proportion. When Schaaff, Heinisch and Zimmermann (1989) overexpressed phosphofructokinase, the "rate-limiting enzyme" of glycolysis, and other glycolytic enzymes several-fold in yeast, the glycolytic flux to ethanol did not change. Similar results have been obtained for many pathways. Control of flux is usually shared among several steps, and it can move from one step to another when conditions change. *Metabolic control analysis* (MCA), developed by Kacser and Burns (1973) and independently by Heinrich and Rapoport (1974), makes this precise.

**Definition 17.4.1 (Flux Control Coefficient and Elasticity Coefficient)** For a pathway in a steady state with flux $J$, the **flux control coefficient** of enzyme $i$ is the fractional change in flux produced by a small fractional change in the concentration (activity) $E_i$ of that enzyme, all else being free to adjust:

$$
C^{J}_{i} = \frac{\partial\ln J}{\partial\ln E_i}.
$$
The **elasticity coefficient** of the rate $v_i$ of enzyme $i$ with respect to a metabolite S is the fractional change in $v_i$ produced by a fractional change in [S], with all other concentrations held constant:

$$
\varepsilon^{v_i}_{\mathrm{S}} = \frac{\partial\ln v_i}{\partial\ln[\mathrm{S}]}.
$$

The flux control coefficient is a property of the whole system: it says how much the flux depends on one enzyme in the presence of all the others. The elasticity is a local property of one enzyme, which can be calculated from its rate equation: for a Michaelis–Menten enzyme far from equilibrium, $\varepsilon^{v}_{\mathrm{S}} = K_{\mathrm{M}}/(K_{\mathrm{M}} + [\mathrm{S}])$, between 1 (unsaturated) and 0 (saturated); a product or feedback inhibitor gives a negative elasticity; and a near-equilibrium enzyme has very large elasticities, because by Formula 17.3.1 its net rate is proportional to $1 - Q/K'$ and changes greatly with small changes of $Q$. A "rate-limiting enzyme" in the classical sense is one with $C^J_i \approx 1$.

### 17.4.2. The Theorems

Two theorems connect the global and the local coefficients. They hold for any pathway in which each rate is proportional to the concentration of its enzyme.

**Theorem 17.4.1 (Summation Theorem)** The flux control coefficients of all enzymes of a pathway sum to one:

$$
\sum_i C^{J}_{i} = 1.
$$

**Proof** Multiply the concentrations of all enzymes by the same factor $\lambda$. Every rate is multiplied by $\lambda$; the metabolite concentrations that satisfied the steady-state conditions (all rates equal) still satisfy them, so they do not change, and the flux becomes $\lambda J$. Thus $J$ is a homogeneous function of degree 1 of the enzyme concentrations, and Euler's theorem for homogeneous functions gives $\sum_i E_i\,\partial J/\partial E_i = J$, which is the statement. $\square$

**Theorem 17.4.2 (Connectivity Theorem)** For every metabolite S of the pathway,

$$
\sum_i C^{J}_{i}\,\varepsilon^{v_i}_{\mathrm{S}} = 0.
$$

**Proof** (sketch) Change the enzyme concentrations by small fractions $\delta_i = \varepsilon^{v_i}_{\mathrm{S}}\,\delta$ chosen so that, if [S] simultaneously fell by the fraction $\delta$, every rate would remain unchanged: the direct effect $\delta_i$ on $v_i$ is cancelled by the effect $-\varepsilon^{v_i}_{\mathrm{S}}\delta$ of the change in [S]. The original state with [S] lowered by $\delta$ is then a steady state of the perturbed system with unchanged flux, so $\Delta\ln J = \sum_i C^J_i\delta_i = \delta\sum_i C^J_i\varepsilon^{v_i}_{\mathrm{S}} = 0$. $\square$

For a two-step pathway X → S → P with enzymes 1 and 2, the theorems give $C^J_1 + C^J_2 = 1$ and $C^J_1\varepsilon^{v_1}_{\mathrm{S}} + C^J_2\varepsilon^{v_2}_{\mathrm{S}} = 0$, hence

$$
C^{J}_{1} = \frac{\varepsilon^{v_2}_{\mathrm{S}}}{\varepsilon^{v_2}_{\mathrm{S}} - \varepsilon^{v_1}_{\mathrm{S}}}, \qquad C^{J}_{2} = \frac{-\varepsilon^{v_1}_{\mathrm{S}}}{\varepsilon^{v_2}_{\mathrm{S}} - \varepsilon^{v_1}_{\mathrm{S}}}. \tag{17.5}
$$
Since S is the product of enzyme 1 ($\varepsilon^{v_1}_{\mathrm{S}} \le 0$) and the substrate of enzyme 2 ($\varepsilon^{v_2}_{\mathrm{S}} > 0$), both coefficients lie between 0 and 1. The classical rate-limiting step is the special case in which enzyme 1 is insensitive to its product ($\varepsilon^{v_1}_{\mathrm{S}} = 0$): then $C^J_1 = 1$ and the second enzyme has no control. If enzyme 1 is near equilibrium, $\lvert\varepsilon^{v_1}_{\mathrm{S}}\rvert$ is large and its control coefficient is small, the statement of 17.3.3 in quantitative form. Control is thus distributed according to the elasticities, which depend on the concentrations; it is not a fixed property of an enzyme.

### 17.4.3. A Numerical Example

Consider a three-step pathway from a fixed source $\mathrm{X_0}$ (1 mM) through two intermediates to a sink $\mathrm{X_3}$ (0.01 mM), each step catalyzed by a reversible Michaelis–Menten enzyme,

$$
v_i = e_i\,\frac{(V_i/K_{\mathrm{S},i})\,([\mathrm{S}_{i-1}] - [\mathrm{S}_i]/K'_i)}{1 + [\mathrm{S}_{i-1}]/K_{\mathrm{S},i} + [\mathrm{S}_i]/K_{\mathrm{P},i}}, \qquad \mathrm{X_0} \xrightarrow{v_1} \mathrm{S_1} \xrightarrow{v_2} \mathrm{S_2} \xrightarrow{v_3} \mathrm{X_3},
$$
where $e_i$ is the relative amount of enzyme $i$ (1 in the reference state). The first enzyme ($V_1 = 2\,\mathrm{mM\,s^{-1}}$, $K'_1 = 10$) supplies the intermediates, the second is fast and near equilibrium ($V_2 = 10$, $K'_2 = 5$), the third consumes $\mathrm{S_2}$ ($V_3 = 3$, $K'_3 = 100$); all $K_{\mathrm{S}} = 0.5\,\mathrm{mM}$, $K_{\mathrm{P}} = 1\,\mathrm{mM}$. In a second version the end product of the pathway's supply branch, $\mathrm{S_2}$, inhibits the first enzyme allosterically, $v_1 \to v_1/(1 + ([\mathrm{S_2}]/K_{\mathrm{I}})^4)$ with $K_{\mathrm{I}} = 0.1\,\mathrm{mM}$ (**feedback inhibition**, [7.1.9](/7.1.9#sec-9.5.1)). Solving the steady-state equations $v_1 = v_2 = v_3$ numerically (with `fsolve`, [4.4.4](/4.4.4)) and changing each $e_i$ by a small fraction gives the control coefficients:

| | $C^J_1$ (supply) | $C^J_2$ (near equilibrium) | $C^J_3$ (demand) | $\sum C^J_i$ |
|---|---|---|---|---|
| without feedback | 0.89 | 0.04 | 0.07 | 1.00 |
| with **feedback inhibition** of enzyme 1 by $\mathrm{S_2}$ | 0.26 | 0.004 | 0.74 | 1.00 |

![Metabolic control analysis of a three-step pathway (17.4.3). A: the pathway, X₀ → S₁ → S₂ → X₃, with enzyme 1 (supply), a near-equilibrium enzyme 2 and enzyme 3 (demand); the dashed inhibition arc is the feedback inhibition of enzyme 1 by S₂ present in the second version. B and C: steady-state flux relative to the reference state when the amount of one enzyme is varied from 0.25 to 4 times its reference value (logarithmic axes), without feedback (B) and with feedback (C); the slope of each curve at the reference point (circle) is the flux control coefficient. D: the flux control coefficients in the two versions; each set sums to one (summation theorem). Feedback inhibition moves most of the control of flux from the supply enzyme to the demand enzyme, and the near-equilibrium enzyme has almost none in either case](./plots/mca-linear-pathway.py)

Three lessons follow. The control coefficients sum to one in both cases, as Theorem 17.4.1 requires. The near-equilibrium enzyme has almost no control, however large or small it is made. And feedback inhibition does not make the inhibited enzyme "rate-limiting"; it does the opposite: when the first enzyme is inhibited by the end product, any increase in its amount raises $[\mathrm{S_2}]$, which inhibits it again, and most of the control passes to the enzyme that consumes $\mathrm{S_2}$.

### 17.4.4. Supply and Demand

The example generalizes. Hofmeyr and Cornish-Bowden (2000) proposed to analyze metabolism as an economy of supply and demand blocks linked by an intermediate (ATP, an amino acid, NADPH). Feedback inhibition of the supply block by the linking intermediate makes the supply respond to demand: the flux is controlled by the demand block, and the role of the regulated supply enzyme is to keep the concentration of the intermediate constant (homeostasis), not to set the flux. In this view the allosteric regulation of PFK-1 by ATP and AMP (7.1.18) matches glycolytic flux to the rate of ATP consumption while keeping [ATP] nearly constant, and overexpressing PFK-1 changes little because the flux is set by the ATP demand of the cell. Experimental estimates of control coefficients in yeast and muscle glycolysis indeed put much of the control on glucose transport, hexokinase and ATP consumption, and comparatively little on PFK-1.

MCA has practical consequences: to increase the flux to a product in metabolic engineering, one must usually raise the activities of several enzymes together, or relieve feedback and increase demand, rather than overexpress the "key enzyme"; and a drug that inhibits an enzyme with a small control coefficient must inhibit it almost completely before the flux falls. Larger networks, branched pathways and the response coefficients of external effectors ($R^J_X = C^J_i\,\varepsilon^{v_i}_X$, the combined response theorem) are treated in [Systems Biology](/7.9).

## Summary

Chemistry: Five reaction classes (17.1.2): C–C bonds (carbanions stabilized by carbonyls, imines or coenzymes: aldol, Claisen, decarboxylation), rearrangements and eliminations (enediols, dehydrations), radicals ($\mathrm{B_{12}}$, radical SAM), group transfers (activation by phosphate, $\mathrm{PP_i}$, AMP, thioester) and oxidation–reduction (dehydrogenations to NAD⁺ and FAD). The sequence –CH₂–CH₂– → –CH=CH– (FAD) → –CHOH– ($\ce{H2O}$) → –CO– ($\ce{NAD+}$) recurs in the citric acid cycle, β oxidation and, reversed with NADPH, fatty acid synthesis (17.1.3).

Coenzymes (Definitions 17.2.1–17.2.9; table in 17.2.1):

| Coenzyme (vitamin) | Carries | Key chemistry |
|---|---|---|
| CoA ($\mathrm{B_5}$) | acyl | thioester |
| lipoate | electrons + acyl | disulfide on a Lys arm |
| TPP ($\mathrm{B_1}$) | aldehyde (C₂) | thiazolium ylide, electron sink; umpolung |
| FAD, FMN ($\mathrm{B_2}$); NAD, NADP ($\mathrm{B_3}$) | electrons; hydride | [7.1.16](/7.1.16#sec-16.5) |
| PLP ($\mathrm{B_6}$) | amino; reactions at C-α | Schiff base, pyridinium electron sink; bond chosen by geometry |
| biotin ($\mathrm{B_7}$) | $\ce{CO2}$ | carboxybiotin on a Lys arm |
| THF ($\mathrm{B_9}$) | one-carbon units, three oxidation levels | N-5, N-10 |
| $\mathrm{B_{12}}$ | H atoms, alkyl groups, methyl | homolysis of Co–C; $\ce{Co^+}$ nucleophile |
| SAM (Met + ATP) | methyl; 5′-deoxyadenosyl radical | sulfonium |

Regulation:

| Concept | Statement |
|---|---|
| Pathway, flux, committed step (Definition 17.3.1) | steady state: intermediates constant, flux variable; regulation (homeostasis) versus control |
| Levels and time scales (17.3.2) | enzyme amount (h–days), compartments, substrate, allostery (ms–s), covalent modification (s–min) |
| Flux–force relation (Formula 17.3.1) | $J_{-}/J_{+} = \mathrm{e}^{\Delta_{\mathrm{r}}G/RT}$; regulated steps are far from equilibrium (glycolysis: HK, PFK-1, PK) |
| Substrate cycle (Definition 17.3.2) | **reciprocal regulation**; cycling amplifies sensitivity, Eq. (17.2) |
| Energy charge (Definition 17.3.3) | 0.8–0.95 in cells; R-type and U-type enzymes; adenylate kinase amplifies AMP, Eq. (17.4) |
| Control coefficients (Definition 17.4.1) | $C^J_i = \partial\ln J/\partial\ln E_i$; elasticities $\varepsilon^{v_i}_{\mathrm{S}}$ |
| Theorems 17.4.1, 17.4.2 | $\sum C^J_i = 1$; $\sum C^J_i\varepsilon^{v_i}_{\mathrm{S}} = 0$; two steps: Eq. (17.5) |
| Supply–demand (17.4.4) | feedback inhibition transfers flux control to demand; the regulated enzyme provides homeostasis |

## Questions

1. Classify each reaction into one of the five classes and name the coenzyme, if any: (a) α-ketoglutarate → succinyl-CoA + $\ce{CO2}$; (b) 3-phosphoglycerate → 2-phosphoglycerate; (c) glutamate + pyruvate → α-ketoglutarate + alanine; (d) methylmalonyl-CoA → succinyl-CoA; (e) acetyl-CoA + $\ce{HCO3-}$ + ATP → **malonyl-CoA**.

   **Answer** (a) Oxidative decarboxylation: C–C bond breaking combined with oxidation; TPP, lipoate, CoA, FAD and NAD (α-ketoglutarate dehydrogenase). (b) Internal rearrangement (a group shift), catalyzed by a mutase with 2,3-bisphosphoglycerate as cofactor, no vitamin-derived coenzyme. (c) Group transfer of an amino group; PLP. (d) Free-radical rearrangement; coenzyme $\mathrm{B_{12}}$. (e) Formation of a C–C bond (carboxylation); biotin.

2. Explain why a carbonyl group is needed two carbons away for the decarboxylation of acetoacetate, and why the decarboxylation of pyruvate, an α-keto acid, requires TPP.

   **Answer** When $\ce{CO2}$ leaves, the electron pair of the C–C bond stays on the carbon. In acetoacetate (a β-keto acid) that carbon is adjacent to the ketone carbonyl, so the charge is delocalized as an enolate and the reaction is easy. In pyruvate the departing carboxylate is attached directly to the carbonyl carbon; the electrons would remain on the carbonyl carbon itself, giving an unstabilized acyl anion. TPP adds to the carbonyl, converting it into a carbon bonded to the thiazolium ring; the electrons left by $\ce{CO2}$ are then delocalized into the positively charged ring (an enamine), so TPP plays the role of the missing β carbonyl.

3. A step of a pathway has $\Delta_{\mathrm{r}}G = -1.5\,\mathrm{kJ\,mol^{-1}}$ at $37\,^\circ\mathrm{C}$ and a net flux of $1\,\mathrm{\mu mol\,g^{-1}\,min^{-1}}$. What are its forward and backward one-way fluxes? What would you expect to happen to the pathway flux if the amount of this enzyme were doubled?

   **Answer** $J_{-}/J_{+} = \mathrm{e}^{-1.5/2.58} = 0.56$, so $J = J_{+}(1 - 0.56)$ gives $J_{+} = 2.27$ and $J_{-} = 1.27\,\mathrm{\mu mol\,g^{-1}\,min^{-1}}$. Doubling the enzyme would move the step even closer to equilibrium (both one-way fluxes rise, the concentrations of its substrate and product readjust slightly), and the pathway flux would barely change: a near-equilibrium enzyme has a flux control coefficient near zero (17.4.2).

4. Calculate the energy charge of a cell with [ATP] = 5.0, [ADP] = 0.5 and [AMP] = 0.05 mM. Is adenylate kinase at equilibrium if $K' = 1$? If ATP falls to 4.5 mM with the total constant and adenylate kinase at equilibrium, estimate [ADP] and [AMP].

   **Answer** EC = (5.0 + 0.25)/5.55 = 0.946. $[\mathrm{ATP}][\mathrm{AMP}]/[\mathrm{ADP}]^2 = 5.0 \times 0.05/0.25 = 1.0$: at equilibrium. With [ATP] = 4.5 and [ADP] + [AMP] = 1.05: $4.5[\mathrm{AMP}] = [\mathrm{ADP}]^2$, so $[\mathrm{ADP}]^2 + 4.5[\mathrm{ADP}] - 4.725 = 0$, $[\mathrm{ADP}] = 0.88\,\mathrm{mM}$ and $[\mathrm{AMP}] = 0.17\,\mathrm{mM}$. A 10% fall in ATP raises ADP 1.8-fold and AMP 3.5-fold.

5. In a two-step pathway the elasticity of enzyme 1 to its product S is $-0.5$ and the elasticity of enzyme 2 to its substrate S is $0.25$. Compute the flux control coefficients. How do they change if enzyme 1 becomes completely insensitive to S?

   **Answer** By Eq. (17.5), $C^J_1 = 0.25/(0.25 + 0.5) = 1/3$ and $C^J_2 = 0.5/0.75 = 2/3$. With $\varepsilon^{v_1}_{\mathrm{S}} = 0$: $C^J_1 = 1$, $C^J_2 = 0$; enzyme 1 is then rate-limiting in the classical sense, because nothing downstream can feed back on it.

6. (Open question) A company wants to double the production of an amino acid by a bacterium in which the first enzyme of the pathway is feedback-inhibited by the product. Using the ideas of 17.4, compare three strategies: (a) overexpressing the first enzyme tenfold, (b) introducing a feedback-resistant mutant of the first enzyme, (c) (b) together with an increased export (demand) of the product.

   **Answer** Outline: (a) with feedback intact, the extra enzyme is inhibited by the accumulating product, its flux control coefficient is small (as in the example of 17.4.3), and the flux increases little. (b) A feedback-resistant enzyme removes the negative elasticity to the product; control moves back toward the first enzyme, so its activity now raises the flux, but the product accumulates inside the cell, and other steps or export may become limiting and toxic concentrations may arise. (c) Combining deregulated supply with increased demand (export, or a sink) distributes the change across the pathway, consistent with the summation theorem: large flux increases need coordinated changes in several steps. This is how industrial lysine and glutamate producers (*Corynebacterium glutamicum*) were developed; the strategy can be tested on a kinetic model by computing control coefficients before and after each modification.
