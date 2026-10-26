---
title: The Citric Acid Cycle
description: Cellular respiration in three stages; the pyruvate dehydrogenase complex, its five coenzymes and substrate channeling; the eight reactions of the citric acid cycle with their chemical logic, energetics and stereochemistry (prochiral citrate), isotope tracing of acetyl carbons; ATP yield of glucose oxidation; the cycle as an amphibolic hub, anaplerotic reactions and biotin; regulation of PDH and the cycle, metabolons, moonlighting aconitase, oncometabolites; the glyoxylate cycle and its regulation; the pathway cards.
---

Glycolysis releases only about 5% of the free energy of glucose ([7.1.18](/7.1.18#sec-18.2.4)); most of the rest is obtained when pyruvate is oxidized completely to $\ce{CO2}$ in the mitochondria. This chapter covers the first two of the three stages of this cellular respiration: the oxidative decarboxylation of pyruvate to acetyl-CoA by the pyruvate dehydrogenase complex, and the oxidation of the acetyl group in the citric acid cycle (tricarboxylic acid cycle, Krebs cycle), which collects the electrons as NADH and $\ce{FADH2}$. The third stage, the transfer of these electrons to $\ce{O2}$ coupled to ATP synthesis, is oxidative phosphorylation ([7.1.23](/7.1.23)). The cycle is also the meeting point of the catabolism of carbohydrates, fats ([7.1.21](/7.1.21)) and amino acids ([7.1.22](/7.1.22)), and the source of precursors for biosynthesis; its intermediates are drawn off and refilled continuously. Every step is one of the five reaction classes of [7.1.17](/7.1.17#sec-17.1.2), its coenzymes are those of the table in [7.1.17](/7.1.17#sec-17.2.1), and the last three steps are the recurring oxidation sequence of [7.1.17](/7.1.17#sec-17.1.3), met again in β oxidation. The glyoxylate cycle, the variant that lets plants and microorganisms make sugar from fat, closes the chapter.

## 20.1. Production of Acetyl-CoA

### 20.1.1. Three Stages of Respiration

**Definition 20.1.1 (Cellular Respiration)** **Cellular respiration** is the complete oxidation of organic fuels to $\ce{CO2}$ and $\ce{H2O}$ with $\ce{O2}$ (or, in some microorganisms, another inorganic compound) as the final electron acceptor. It occurs in three stages: (1) oxidation of glucose, fatty acids and amino acids to the acetyl group of acetyl-CoA; (2) oxidation of the acetyl group to $\ce{CO2}$ in the citric acid cycle, with the electrons collected by $\ce{NAD+}$ and FAD; (3) transfer of these electrons through the respiratory chain to $\ce{O2}$, coupled to ATP synthesis by oxidative phosphorylation.

In eukaryotes all three stages take place in mitochondria, as Eugene Kennedy and Albert Lehninger showed in 1948 with isolated mitochondria; in bacteria the enzymes of the cycle are in the cytosol and the plasma membrane plays the role of the inner mitochondrial membrane. Pyruvate from glycolysis crosses the outer membrane through porins and the inner membrane on the mitochondrial pyruvate carrier (MPC), a $\ce{H+}$-coupled symporter.

### 20.1.2. The Pyruvate Dehydrogenase Complex

**Definition 20.1.2 (Pyruvate Dehydrogenase Complex)** The **pyruvate dehydrogenase complex** (PDH complex) is a multienzyme complex of the mitochondrial matrix that catalyzes the oxidative decarboxylation of pyruvate,

$$
\text{pyruvate} + \ce{CoA} + \ce{NAD+} \to \text{acetyl-CoA} + \ce{CO2} + \ce{NADH}, \qquad \Delta_{\mathrm{r}}G'^{\circ} = -33.4\,\mathrm{kJ\,mol^{-1}}, \tag{20.1}
$$
with three enzymes, pyruvate dehydrogenase (E1), dihydrolipoyl transacetylase (E2) and dihydrolipoyl dehydrogenase (E3), and five coenzymes: **thiamine pyrophosphate** (bound to E1), **lipoate** (bound to E2), FAD (bound to E3), **coenzyme A** and $\ce{NAD+}$.

E2 forms the core of the complex: 24 subunits arranged as a cube in *E. coli*, 60 as a pentagonal dodecahedron in mammals and gram-positive bacteria, around which many copies of E1 and E3 (and in mammals the E3-binding protein) are bound, a particle of up to 10 MDa, larger than a ribosome. E2 consists of one to three N-terminal lipoyl domains, each with a lipoyl group in amide linkage to a Lys, a peripheral subunit-binding domain, and the catalytic acyltransferase domain of the core, joined by flexible linkers of 20–30 residues rich in Ala and Pro. Two regulatory enzymes, PDH kinase and PDH phosphatase, are part of the mammalian complex (20.4.1). The reaction is irreversible in the cell: labeled $\ce{CO2}$ is not incorporated into pyruvate, which is why acetyl-CoA from fat cannot become glucose in animals ([7.1.19](/7.1.19#sec-19.1.5)).

### 20.1.3. Five Reactions in One Complex

The oxidative decarboxylation is done in five steps that never release an intermediate.

1. E1 decarboxylates pyruvate with TPP, exactly as pyruvate decarboxylase does ([7.1.17](/7.1.17#sec-17.2.2)), giving hydroxyethyl-TPP (C-2 of pyruvate, at the oxidation level of an aldehyde, bound to the thiazolium carbanion). This step is the slowest.
2. E1 oxidizes the hydroxyethyl group to an acetyl group and transfers it to one sulfur of the oxidized lipoyl disulfide of E2; the two electrons reduce the disulfide, giving an acetyl thioester and a thiol (acetyl-dihydrolipoamide). The energy of the oxidation is conserved in the **thioester**.
3. E2 transfers the acetyl group to CoA (a transesterification), releasing acetyl-CoA and the fully reduced dihydrolipoyl group.
4. E3 reoxidizes the dihydrolipoyl group to the disulfide, reducing its tightly bound FAD.
5. E3 transfers the electrons from $\ce{FADH2}$ to $\ce{NAD+}$, giving NADH, which carries them to the respiratory chain (about 2.5 ATP per pair, [7.1.23](/7.1.23)).

**Definition 20.1.3 (Substrate Channeling)** **Substrate channeling** is the transfer of an intermediate from one active site to the next of a multienzyme complex (by a covalent swinging arm, a tunnel or an electrostatic path) without its release into the bulk solution.

The lipoyllysyl arm, about 1.4 nm long and carried on the flexible E2 linkers, swings between the active sites of E1, E2 and E3, which may be 5 nm or more apart. Channeling keeps the local concentration of the intermediates high, prevents side reactions of the reactive acetyl and the thiol, and protects the cell from them. The same strategy, with biotin or phosphopantetheine as the tethered carrier, appears in carboxylases (20.3.3) and fatty acid synthase ([7.1.26](/7.1.26)).

![The pyruvate dehydrogenase complex. E1 (pyruvate dehydrogenase, with TPP) decarboxylates pyruvate (1) and transfers the hydroxyethyl group, oxidized to acetyl, to the disulfide of the lipoyl group of E2 (2). The lipoyllysyl arm of E2 (dihydrolipoyl transacetylase) carries the acetyl thioester to the E2 active site, where the acetyl group is transferred to CoA (3), and then the reduced dithiol to E3 (dihydrolipoyl dehydrogenase), which reoxidizes it with FAD (4) and passes the electrons to NAD⁺ (5). The three positions of the arm are shown with its state: oxidized (S–S), acetylated (S–Ac, SH) and reduced (SH, SH)](./plots/pdh-complex.py)

### 20.1.4. A Family of α-Keto Acid Dehydrogenases

Three complexes with the same architecture oxidize α-keto acids: the PDH complex, the α-ketoglutarate dehydrogenase complex of the cycle (step 4, 20.2.2), and the branched-chain α-keto acid dehydrogenase complex that oxidizes the keto acids derived from Val, Ile and Leu ([7.1.22](/7.1.22)). Their E1 and E2 subunits are homologous, with different substrate specificities, and within a species all three share the same E3, which acts on the common substrate, dihydrolipoamide. They arose by gene duplication and divergence, a recurrent theme of metabolic evolution ([7.1.1](/7.1.1)).

The complex depends on four vitamins: thiamine (TPP), pantothenate (CoA), riboflavin (FAD) and niacin (NAD). Thiamine deficiency (beriberi, Wernicke–Korsakoff syndrome) impairs pyruvate oxidation, with a rise of blood pyruvate and lactate, and damages above all the brain, which normally oxidizes glucose almost exclusively. Arsenite (and organic arsenicals, such as the war gas lewisite) form a stable cyclic adduct with the dithiol of reduced lipoamide and block all three complexes. Inherited PDH deficiency, mostly of the X-linked E1α subunit, causes lactic acidosis and neurological damage; a ketogenic diet, which supplies acetyl-CoA without pyruvate, helps some patients.

## 20.2. Reactions of the Citric Acid Cycle

### 20.2.1. A Cycle That Oxidizes Acetate

**Definition 20.2.1 (Citric Acid Cycle)** The **citric acid cycle** is the cyclic pathway of the mitochondrial matrix (of the cytosol in bacteria) in which the acetyl group of acetyl-CoA is condensed with oxaloacetate to citrate, and citrate is converted back to oxaloacetate in seven steps, with release of two $\ce{CO2}$, reduction of three $\ce{NAD+}$ and one FAD (as ubiquinone, 7.1.23) and formation of one GTP or ATP by substrate-level phosphorylation.

Hans Krebs proposed the cycle in 1937 from experiments on minced pigeon breast muscle. Albert Szent-Györgyi had found that small amounts of the four-carbon dicarboxylic acids (succinate, fumarate, malate, oxaloacetate) stimulate $\ce{O2}$ consumption far beyond what their own oxidation would require, that is, catalytically; Krebs showed that citrate, isocitrate and α-ketoglutarate act the same way, that oxaloacetate condenses with a product of pyruvate to citrate, and that malonate, a competitive inhibitor of succinate dehydrogenase, blocks the oxidation of pyruvate whatever acid is added and causes succinate to accumulate. The only explanation was a cycle (Nobel Prize 1953, shared with Fritz Lipmann, discoverer of coenzyme A).

Why a cycle? The direct oxidation of acetate is chemically impractical: decarboxylating a two-carbon acid would leave methane, which almost no organism can oxidize. Methylene groups next to carbonyls are readily oxidized, so the cell first attaches the methyl group of acetyl-CoA to the carbonyl of oxaloacetate (an aldol-type addition, making it a methylene of citrate), moves a hydroxyl into position, and then removes two carbons by oxidative decarboxylations of a β-keto acid and an α-keto acid, each prepared by a carbonyl at the right place. All three steps that make or break C–C bonds rely on a properly placed carbonyl ([7.1.17](/7.1.17#sec-17.1.2)). The four-carbon unit is regenerated by the recurring sequence dehydrogenation (FAD), hydration and dehydrogenation ($\ce{NAD+}$) ([7.1.17](/7.1.17#sec-17.1.3)). Oxaloacetate thus acts catalytically: one molecule can in principle oxidize an unlimited number of acetyl groups, and its concentration in the matrix is micromolar.

![The citric acid cycle. Pyruvate enters the mitochondrion on the mitochondrial pyruvate carrier (MPC) and is converted to acetyl-CoA by the pyruvate dehydrogenase complex. Eight steps follow clockwise from oxaloacetate: citrate synthase (condensation), aconitase (isomerization through cis-aconitate), isocitrate dehydrogenase and the α-ketoglutarate dehydrogenase complex (oxidative decarboxylations, each giving NADH and CO₂), succinyl-CoA synthetase (substrate-level phosphorylation of GDP or ADP), succinate dehydrogenase (FAD), fumarase (hydration) and malate dehydrogenase (NADH). Steps 1, 3 and 4 are irreversible in the cell (one head); the others are near equilibrium](./plots/tca-cycle.py)

### 20.2.2. The Eight Steps

| Step | Enzyme | Reaction | Class (7.1.17) | $\Delta_{\mathrm{r}}G'^{\circ}$ / (kJ mol⁻¹) |
|---|---|---|---|---|
| 1 | citrate synthase | acetyl-CoA + oxaloacetate + $\ce{H2O}$ → citrate + CoA | C–C bond formation | $-32.2$ |
| 2 | aconitase (aconitate hydratase) | citrate ⇌ isocitrate (via cis-aconitate) | isomerization (dehydration–rehydration) | $+13.3$ |
| 3 | isocitrate dehydrogenase | isocitrate + $\ce{NAD+}$ → α-ketoglutarate + $\ce{CO2}$ + NADH | oxidative decarboxylation | $-20.9$ |
| 4 | α-ketoglutarate dehydrogenase complex | α-ketoglutarate + CoA + $\ce{NAD+}$ → succinyl-CoA + $\ce{CO2}$ + NADH | oxidative decarboxylation | $-33.5$ |
| 5 | succinyl-CoA synthetase | succinyl-CoA + $\mathrm{P_i}$ + GDP ⇌ succinate + CoA + GTP | substrate-level phosphorylation | $-2.9$ |
| 6 | succinate dehydrogenase | succinate + E-FAD ⇌ fumarate + E-$\ce{FADH2}$ | oxidation | $\approx 0$ |
| 7 | fumarase (fumarate hydratase) | fumarate + $\ce{H2O}$ ⇌ L-malate | hydration | $-3.8$ |
| 8 | malate dehydrogenase | L-malate + $\ce{NAD+}$ ⇌ oxaloacetate + NADH + $\ce{H+}$ | oxidation | $+29.7$ |

(Values from Lehninger 8e.)

1. Citrate synthase condenses the methyl carbon of acetyl-CoA with the carbonyl carbon (C-2) of oxaloacetate. The reaction is a **Claisen condensation** in the sense of [7.1.17](/7.1.17#sec-17.1.2): an active-site Asp removes a proton from the methyl group, the enol(ate) of the thioester attacks the ketone of oxaloacetate as in an **aldol reaction**, and the product, citroyl-CoA, is hydrolyzed in the active site; the hydrolysis of this thioester makes the step strongly exergonic, which is needed because oxaloacetate is scarce. The enzyme is a homodimer whose small domain closes over the active site when oxaloacetate binds (**induced fit**), creating the site for acetyl-CoA; a second conformational change after the condensation triggers hydrolysis. The ordered binding (oxaloacetate first) prevents the wasteful hydrolysis of acetyl-CoA in the absence of its partner. The mechanism is drawn in [6.5.22](/6.5.22#sec-22.10.2).
2. Aconitase converts citrate to isocitrate by removing water to give enzyme-bound cis-aconitate and adding it back with the opposite orientation. At equilibrium (pH 7.4, 25 °C) the mixture contains less than 10% isocitrate; the reaction runs forward because isocitrate is removed. The enzyme has a [4Fe–4S] cluster of which one Fe is not bound to Cys and coordinates a carboxyl and the hydroxyl of the substrate, acting as a Lewis acid. Fluoroacetate (in some plants, and the rodenticide "1080") is converted by citrate synthase to fluorocitrate, which inhibits aconitase; this "lethal synthesis" makes fluoroacetate one of the most toxic small molecules.
3. Isocitrate dehydrogenase oxidizes the secondary alcohol of isocitrate to a ketone (giving the transient β-keto acid oxalosuccinate, bound to $\ce{Mn^2+}$) and decarboxylates it to α-ketoglutarate (2-oxoglutarate). The NAD-dependent **isozyme** (IDH3) of the matrix is the cycle enzyme and is allosterically regulated; NADP-dependent isozymes in the cytosol and peroxisomes (IDH1) and matrix (IDH2) supply NADPH.
4. The α-ketoglutarate dehydrogenase complex catalyzes a second oxidative decarboxylation, by the same chemistry as the PDH complex (20.1.4), conserving the energy in the thioester succinyl-CoA.
5. Succinyl-CoA synthetase (succinic thiokinase; "synthetase" because a nucleoside triphosphate takes part, [7.1.17](/7.1.17#sec-17.1.4)) uses the energy of the thioester ($\Delta_{\mathrm{r}}G'^{\circ}$ of hydrolysis about $-36\,\mathrm{kJ\,mol^{-1}}$) to make a phosphoanhydride bond: $\mathrm{P_i}$ displaces CoA to give succinyl phosphate, which phosphorylates His246 of the α subunit, and the phosphohistidine phosphorylates GDP or ADP. This is the only **substrate-level phosphorylation** of the cycle. Two isozymes differ in their β subunit, one specific for GDP (abundant in liver and kidney, which use GTP for gluconeogenesis), one for ADP (in brain, heart and muscle); **nucleoside diphosphate kinase** equilibrates GTP with ATP. Two "power helices" point the positive ends of their dipoles at the phosphohistidine and stabilize it.
6. Succinate dehydrogenase, a flavoprotein with covalently bound FAD and three iron–sulfur clusters, oxidizes succinate to fumarate. It is the only membrane-bound enzyme of the cycle, an integral protein of the inner mitochondrial membrane, and is identical with Complex II of the respiratory chain: its electrons go to ubiquinone and yield about 1.5 ATP ([7.1.23](/7.1.23)). The trans double bond is formed stereospecifically. Malonate, which resembles succinate but has no $\ce{-CH2-CH2-}$ to oxidize, is a classic example of **competitive inhibition** ([7.1.9](/7.1.9#sec-9.4.1)).
7. Fumarase adds water across the trans double bond of fumarate, by an anti addition through a carbanion transition state, and forms only L-malate; it does not act on the cis isomer maleate, nor on D-malate in reverse. It is the textbook example of a **stereospecific** enzyme.
8. Malate dehydrogenase oxidizes L-malate to oxaloacetate. The standard equilibrium lies far toward malate, but citrate synthase removes oxaloacetate continuously and keeps it below about 1 µM, so that the step runs forward in the cell. The same enzyme, run in reverse, moves reducing equivalents in the malate–aspartate shuttle ([7.1.23](/7.1.23)) and in gluconeogenesis ([7.1.19](/7.1.19#sec-19.1.2)).

### 20.2.3. Citrate, a Symmetric Molecule That Reacts Asymmetrically

When ¹⁴C became available in the 1940s, an experiment seemed to exclude citrate from the cycle. Acetate labeled in its carboxyl group was fed to tissue, and the α-ketoglutarate isolated was labeled only in the carboxyl group farther from the keto group (the γ-carboxyl). Citrate is achiral, and its two $\ce{-CH2COO-}$ arms are chemically identical; if it were an intermediate, the label should have been spread equally over both carboxyls of α-ketoglutarate. Alexander Ogston (1948) resolved the paradox: an achiral molecule of the type $\ce{CX2YZ}$ placed on an asymmetric active site that binds it at three points can bind in only one orientation, so the enzyme distinguishes the two identical groups. Citrate is a **prochiral** molecule (**prochirality**, [6.5.5](/6.5.5)): its two arms are enantiotopic, and aconitase always acts on the arm derived from oxaloacetate (the pro-R arm), never on the one derived from acetyl-CoA.

```smiles
OC(=O)C[C@@](O)(CC(=O)O)C(=O)O citrate
OC(=O)C[C@H](C(=O)O)[C@@H](O)C(=O)O isocitrate
```

(The cycle intermediate is (2R,3S)-isocitrate; the SMILES shows its two stereocenters.)

### 20.2.4. Tracing Carbon Atoms

Ogston's rule fixes the fate of every carbon, which can be followed by bookkeeping. The two $\ce{CO2}$ released in a turn come from the oxaloacetate that started it (from its C-1 at isocitrate dehydrogenase and its C-4 at α-ketoglutarate dehydrogenase), not from the acetyl group that just entered. The acetyl carbons survive the first turn and reach succinate, whose symmetry, like that of fumarate, erases the distinction between its two ends: each new oxaloacetate carries the former acetyl carbons in one of two orientations with equal probability.

**Example 20.2.1** Follow a single pulse of acetyl-CoA labeled in the carboxyl carbon ([1-¹⁴C]acetyl). After turn 1 the label is in a carboxyl group of succinate, hence in C-1 or C-4 of oxaloacetate; both are released in turn 2, so all the label leaves as $\ce{CO2}$ in the second turn. A methyl label ([2-¹⁴C]acetyl) becomes a methylene of succinate, hence C-2 or C-3 of oxaloacetate; in turn 2 these carbons become the succinyl-CoA carboxyl (from C-3) or a succinate methylene (from C-2), so after turn 2 half of the label is in carboxyls and is released in turn 3, and the other half repeats the process. The fractions released in turns 3, 4, 5, … are $\tfrac12, \tfrac14, \tfrac18, \dots$; after $n \geq 2$ turns the fraction remaining is $2^{-(n-2)}$.

![Fate of a ¹⁴C label from acetyl-CoA in the citric acid cycle, computed by mapping each carbon atom through the eight steps (a single pulse of labeled acetyl-CoA enters turn 1; succinate and fumarate are treated as symmetric, so each new oxaloacetate carries the former acetyl carbons in either orientation with probability ½). A: fraction of the label released as CO₂ in each turn. A carboxyl label is released entirely in turn 2; a methyl label is not released in turns 1–2, then half of what remains leaves in each turn. B: cumulative fraction released](./plots/tca-isotope-tracing.py)

Today ¹³C-labeled glucose, glutamine or acetate and NMR or mass spectrometry are used to measure the fluxes through the cycle and its exchanges in living tissues and tumors: the labeling patterns of glutamate (which equilibrates with α-ketoglutarate) report the relative rates of the cycle, of anaplerosis and of pyruvate carboxylation, the basis of ¹³C metabolic flux analysis.

### 20.2.5. Energy

One turn of the cycle:

$$
\text{acetyl-CoA} + 3\,\ce{NAD+} + \text{FAD} + \ce{GDP} + \mathrm{P_i} + 2\,\ce{H2O} \to 2\,\ce{CO2} + 3\,\ce{NADH} + \ce{FADH2} + \ce{GTP} + 3\,\ce{H+} + \ce{CoA}. \tag{20.2}
$$
With about 2.5 ATP per NADH and 1.5 per $\ce{FADH2}$ (the P/O ratios explained in [7.1.23](/7.1.23)), one turn yields 10 ATP, almost ten times the single GTP made directly. For the complete oxidation of glucose:

| Stage | Reduced coenzymes and nucleotides formed directly | ATP ultimately formed |
|---|---|---|
| glycolysis: hexokinase, PFK-1 | $-2$ ATP | $-2$ |
| glycolysis: 2 glyceraldehyde 3-phosphate | 2 NADH (cytosolic) | 3 or 5 (depends on the shuttle, 7.1.23) |
| glycolysis: 2 phosphoglycerate kinase, 2 pyruvate kinase | 4 ATP | 4 |
| 2 pyruvate → 2 acetyl-CoA | 2 NADH | 5 |
| 2 isocitrate, 2 α-ketoglutarate, 2 malate | 6 NADH | 15 |
| 2 succinyl-CoA | 2 GTP (ATP) | 2 |
| 2 succinate | 2 $\ce{FADH2}$ | 3 |
| total | | 30–32 |

In standard terms, $32 \times 30.5 = 976\,\mathrm{kJ\,mol^{-1}}$ is conserved out of $2840\,\mathrm{kJ\,mol^{-1}}$, an efficiency of 34%; with the actual phosphorylation potential in cells ([7.1.16](/7.1.16#sec-16.3.2)) the efficiency is about 65%. Aerobic oxidation thus extracts about fifteen times as much ATP from glucose as fermentation ([7.1.18](/7.1.18#sec-18.4.4)).

## 20.3. The Hub of Intermediary Metabolism

### 20.3.1. An Amphibolic Pathway

**Definition 20.3.1 (Amphibolic Pathway)** An **amphibolic pathway** serves both in **catabolism** and in **anabolism** ([7.1.16](/7.1.16#sec-16.1.1)).

The eight-step cycle seems elaborate for oxidizing a two-carbon unit, but it also accepts three-, four- and five-carbon skeletons from the breakdown of amino acids at other points, and it supplies precursors:

- oxaloacetate and α-ketoglutarate are transaminated to aspartate and glutamate, the starting points of other amino acids and of purine and pyrimidine nucleotides ([7.1.27](/7.1.27), [7.1.28](/7.1.28));
- succinyl-CoA condenses with glycine to begin porphyrin and heme synthesis ([7.1.27](/7.1.27));
- citrate is exported to the cytosol, where ATP-citrate lyase cleaves it to acetyl-CoA for fatty acid and sterol synthesis ([7.1.26](/7.1.26));
- oxaloacetate (via malate) is the substrate of gluconeogenesis ([7.1.19](/7.1.19)).

But in animals there is no net synthesis of oxaloacetate from acetyl-CoA: for every two carbons that enter, two leave as $\ce{CO2}$. Every molecule withdrawn must be replaced.

![The citric acid cycle as a hub. Intermediates are withdrawn for biosynthesis (blue): citrate for fatty acids and sterols, α-ketoglutarate for glutamate and the amino acids and purines derived from it, succinyl-CoA for porphyrins, oxaloacetate for aspartate and its products and, through PEP, for glucose. Anaplerotic reactions (green) refill the cycle: pyruvate carboxylase, PEP carboxykinase (and PEP carboxylase in plants and bacteria) and malic enzyme; amino acid carbon and odd-chain fatty acids enter at α-ketoglutarate and succinyl-CoA](./plots/tca-hub.py)

### 20.3.2. Anaplerotic Reactions

**Definition 20.3.2 (Anaplerotic Reaction)** An **anaplerotic reaction** (Greek, "filling up") replenishes the intermediates of the citric acid cycle withdrawn for biosynthesis, usually by carboxylating a three-carbon compound to oxaloacetate or malate.

| Reaction | Enzyme | Where |
|---|---|---|
| pyruvate + $\ce{HCO3-}$ + ATP → oxaloacetate + ADP + $\mathrm{P_i}$ | pyruvate carboxylase (biotin) | liver, kidney (the main anaplerotic reaction of mammals), brain, adipose tissue |
| PEP + $\ce{CO2}$ + GDP ⇌ oxaloacetate + GTP | PEP carboxykinase | heart, skeletal muscle |
| PEP + $\ce{HCO3-}$ → oxaloacetate + $\mathrm{P_i}$ | PEP carboxylase | plants (C4 and CAM photosynthesis, [7.1.25](/7.1.25)), yeast, bacteria |
| pyruvate + $\ce{HCO3-}$ + NAD(P)H ⇌ malate + NAD(P)⁺ | malic enzyme | widely distributed in eukaryotes and bacteria |

Pyruvate carboxylase is almost inactive without acetyl-CoA: when acetyl-CoA, the fuel of the cycle, accumulates, it stimulates the formation of oxaloacetate to burn it. Glutamine (via glutamate and α-ketoglutarate, glutaminolysis) is the main anaplerotic substrate of many proliferating cells and tumors.

### 20.3.3. Biotin and Other Tethers

Pyruvate carboxylase has four identical subunits, each with a **biotin** bound to a Lys. As in all biotin enzymes ([7.1.17](/7.1.17#sec-17.2.4)), the reaction occurs at two sites: in the biotin carboxylase site, bicarbonate is activated by ATP as carboxyphosphate and transferred to N-1′ of biotin; the long biotinyl-Lys arm carries the carboxyl group to the carboxyltransferase site of the adjacent subunit, where it is transferred to the enolate of pyruvate. Lipoate in the α-keto acid dehydrogenases, biotin in the carboxylases and the phosphopantetheine of acyl carrier protein are the three biological tethers; all three are covalently attached to proteins, enter cells on the same transporter (the sodium-dependent multivitamin transporter), and channel intermediates between active sites. Avidin of egg white binds biotin with a dissociation constant of about $10^{-15}\,\mathrm{M}$ and inhibits all biotin enzymes.

### 20.3.4. Incomplete Cycles and Evolution

Many anaerobic bacteria have an incomplete cycle: without α-ketoglutarate dehydrogenase, they run the first steps oxidatively (oxaloacetate → citrate → α-ketoglutarate) and the others reductively (oxaloacetate → malate → fumarate → succinate), not to generate energy but to make biosynthetic precursors. Such branched pathways may resemble an ancestral stage of the cycle; some autotrophic bacteria and archaea run the whole cycle backward (the reductive citric acid cycle), fixing $\ce{CO2}$ with ferredoxin as reductant, and this cycle has been proposed as one of the oldest metabolic pathways.

## 20.4. Regulation

### 20.4.1. The PDH Complex

The entry of pyruvate carbon into the cycle is a key decision in animals, because once pyruvate is converted to acetyl-CoA it can no longer become glucose. The PDH complex is regulated at two levels.

- Allosterically, its products ATP, acetyl-CoA and NADH, and long-chain fatty acids, inhibit it; AMP, CoA and $\ce{NAD+}$, which accumulate when too little acetate enters the cycle, activate it. The ratios $[\mathrm{ATP}]/[\mathrm{ADP}]$, $[\mathrm{NADH}]/[\ce{NAD+}]$ and $[\text{acetyl-CoA}]/[\mathrm{CoA}]$ are the signals.
- Covalently, in vertebrates (and probably plants, but not *E. coli*), by phosphorylation of three Ser residues of the E1α subunit by PDH kinase, which inactivates it, and dephosphorylation by PDH phosphatase, which reactivates it. PDH kinase is activated by ATP, NADH and acetyl-CoA and inhibited by ADP, $\ce{NAD+}$ and pyruvate; PDH phosphatase is activated by $\ce{Ca^2+}$ (in muscle, in step with contraction) and by insulin (in adipose tissue). Mammals have four kinase isoforms; PDK4 is induced in starvation and diabetes, which switches muscle and heart from glucose to fat oxidation and spares pyruvate and lactate for gluconeogenesis.

Dichloroacetate, an analog of pyruvate, inhibits PDH kinase and so activates the complex; it is used for congenital lactic acidosis and has been tested in cancer, to divert pyruvate from lactate (the Warburg effect, [7.1.18](/7.1.18#sec-18.4.4)) into mitochondrial oxidation.

### 20.4.2. Three Exergonic Steps

Within the cycle, the three steps far from equilibrium can each become rate-limiting.

- Citrate synthase is limited by the supply of its substrates, acetyl-CoA and oxaloacetate; the concentration of oxaloacetate depends on the near-equilibrium malate dehydrogenase reaction and falls when $[\mathrm{NADH}]/[\ce{NAD+}]$ rises. Citrate (product), succinyl-CoA and ATP inhibit it; ADP relieves the inhibition by ATP.
- Isocitrate dehydrogenase (NAD) is inhibited by ATP and NADH and activated by ADP and $\ce{Ca^2+}$.
- α-Ketoglutarate dehydrogenase is inhibited by its products succinyl-CoA and NADH and activated by $\ce{Ca^2+}$.

In muscle $\ce{Ca^2+}$, the signal for contraction, activates PDH phosphatase, isocitrate dehydrogenase and α-ketoglutarate dehydrogenase, so that ATP production rises as ATP is consumed (feedforward). Citrate also links the cycle to glycolysis by inhibiting PFK-1 ([7.1.18](/7.1.18#sec-18.5.1)): when the cycle is well supplied, glucose is spared. In the terms of [7.1.17](/7.1.17#sec-17.4.4), the cycle is a supply block whose rate is set by the demand for ATP, signaled through $[\mathrm{NADH}]/[\ce{NAD+}]$ and $[\mathrm{ATP}]/[\mathrm{ADP}]$; most of the flux control lies outside it, in the respiratory chain and ATP use.

![Regulation of pyruvate oxidation and the citric acid cycle in mammals, in SBGN activity-flow notation (filled arrows: carbon flow; open arrows: activation; bars: inhibition). Signals of energy sufficiency (ATP, NADH, acetyl-CoA, fatty acids) inhibit the PDH complex directly and through activation of PDH kinase, which inactivates E1 by phosphorylation; signals of energy demand (ADP, AMP, NAD⁺, CoA, pyruvate) act oppositely. PDH phosphatase is activated by Ca²⁺ and insulin; dichloroacetate (DCA) inhibits the kinase. Citrate synthase is inhibited by citrate, succinyl-CoA and ATP; isocitrate dehydrogenase is inhibited by ATP and NADH, activated by ADP and Ca²⁺; α-ketoglutarate dehydrogenase is inhibited by succinyl-CoA and NADH, activated by Ca²⁺](./plots/tca-regulation.py)

### 20.4.3. Metabolons and Moonlighting

**Definition 20.4.1 (Metabolon)** A **metabolon** is a transient complex of sequential enzymes of a pathway, held together by noncovalent interactions, that channels intermediates between their active sites.

The enzymes of the cycle are usually described as soluble proteins of the matrix (except succinate dehydrogenase), but their concentration in the matrix is very high (about 50% protein by mass), and malate dehydrogenase, citrate synthase and aconitase associate into a metabolon: a path of positive electrostatic potential on the surface of the malate dehydrogenase–citrate synthase complex guides the negatively charged oxaloacetate from one active site to the next, and mutations of Arg to Asp along the path reduce channeling. Dilution of cell extracts dissociates such complexes, which is why they escaped classical enzymology.

**Definition 20.4.2 (Moonlighting Protein)** A **moonlighting protein** has two or more unrelated functions in the same polypeptide.

Cytosolic aconitase is the classic example. When the cell is short of iron, its [4Fe–4S] cluster falls apart, and the apoprotein, called iron regulatory protein 1 (IRP1), opens into a conformation that binds iron-responsive elements, hairpins in the untranslated regions of mRNAs. Binding to the 5′ element of ferritin mRNA blocks its translation (less iron storage); binding to the 3′ elements of transferrin-receptor mRNA stabilizes it (more iron uptake). When iron is restored, the cluster reassembles and IRP1 becomes aconitase again. Many glycolytic enzymes also moonlight (GAPDH in DNA repair and transcription, several glycolytic enzymes as lens crystallins).

### 20.4.4. The Cycle in Cancer

Mutations of cycle enzymes are rare and severe, and three of them showed that intermediates can act as signals.

**Definition 20.4.3 (Oncometabolite)** An **oncometabolite** is a metabolite whose accumulation, caused by a mutation of a metabolic enzyme, promotes tumor formation.

- Inherited loss of succinate dehydrogenase causes paragangliomas and pheochromocytomas (and gastrointestinal stromal tumors), loss of fumarase hereditary leiomyomatosis and renal cell cancer. Succinate or fumarate accumulate and inhibit the α-ketoglutarate-dependent dioxygenases, among them the prolyl hydroxylases that mark the hypoxia-inducible factor HIF-1α for degradation; HIF is stabilized in normal oxygen ("pseudohypoxia") and induces glycolysis and angiogenesis. Fumarate also modifies Cys residues (succination). The two enzymes are therefore tumor suppressors ([7.1.15](/7.1.15#sec-15.6.2)).
- In most low-grade gliomas and in some acute myeloid leukemias, a heterozygous point mutation of the NADP-dependent isocitrate dehydrogenase (IDH1 R132 or IDH2 R140/R172) changes the activity of the enzyme: it reduces α-ketoglutarate with NADPH to (R)-2-hydroxyglutarate, which reaches millimolar concentrations and inhibits α-ketoglutarate-dependent histone and DNA demethylases (TET enzymes), so the cells keep a hypermethylated, undifferentiated state. Inhibitors of the mutant enzymes (ivosidenib for IDH1, enasidenib for IDH2, vorasidenib for both) are approved drugs, a rare case of a cancer therapy designed from a metabolic discovery.
- Lehninger 8e also notes that many tumors down-regulate the mitochondrial pyruvate carrier, so that pyruvate stays in the cytosol and is reduced to lactate.

## 20.5. The Glyoxylate Cycle

### 20.5.1. Two Bypasses Save Two Carbons

**Definition 20.5.1 (Glyoxylate Cycle)** The **glyoxylate cycle** is a variant of the citric acid cycle, present in plants, fungi, many bacteria and some invertebrates but not in vertebrates, in which isocitrate lyase cleaves isocitrate to succinate and glyoxylate and malate synthase condenses glyoxylate with a second acetyl-CoA to malate, so that the two decarboxylation steps are bypassed and there is net synthesis of a four-carbon compound from acetyl-CoA:

$$
2\,\text{acetyl-CoA} + \ce{NAD+} + 2\,\ce{H2O} \to \text{succinate} + 2\,\ce{CoA} + \ce{NADH} + \ce{H+}. \tag{20.3}
$$

Citrate synthase, aconitase and malate dehydrogenase work as in the citric acid cycle (as separate isozymes), and malate synthase uses the same Claisen chemistry as citrate synthase. In seeds that store oil (sunflower, castor bean, cucumber) the cycle runs in glyoxysomes, specialized peroxisomes that also contain the enzymes of β oxidation ([7.1.21](/7.1.21#sec-21.5.3)); it is how seedlings make sugars and cell-wall polysaccharides from fat before they can photosynthesize. *E. coli* and yeast use it to grow on acetate or fatty acids, and *Mycobacterium tuberculosis* needs isocitrate lyase to persist on host lipids in macrophages, which has made the enzyme a drug target.

### 20.5.2. Three Compartments

In the seedling, succinate from the glyoxysome enters the mitochondrion, where succinate dehydrogenase and fumarase convert it to malate; malate passes to the cytosol, is oxidized to oxaloacetate, and PEP carboxykinase and gluconeogenesis ([7.1.19](/7.1.19)) make hexose phosphates and sucrose, the transport form of carbon in plants ([7.1.25](/7.1.25)). The physical separation of the glyoxysomal enzymes from the mitochondrial cycle prevents the acetyl-CoA from being oxidized to $\ce{CO2}$.

![The glyoxylate cycle in a germinating oilseed. In the glyoxysome, fatty acids are β-oxidized to acetyl-CoA; citrate synthase and aconitase act as in the citric acid cycle, but isocitrate lyase splits isocitrate into succinate and glyoxylate, malate synthase condenses glyoxylate with a second acetyl-CoA, and malate dehydrogenase regenerates oxaloacetate. Succinate is converted to malate in the mitochondrion (succinate dehydrogenase, fumarase); in the cytosol, malate is oxidized to oxaloacetate and converted by PEP carboxykinase to phosphoenolpyruvate, the substrate of gluconeogenesis and sucrose synthesis](./plots/glyoxylate-cycle.py)

### 20.5.3. Sharing Isocitrate

In *E. coli*, isocitrate is the branch point: isocitrate dehydrogenase sends it into the citric acid cycle (energy), isocitrate lyase into the glyoxylate cycle (biosynthesis). The partition is regulated by covalent modification of isocitrate dehydrogenase. A bifunctional protein, isocitrate dehydrogenase kinase/phosphatase (AceK), phosphorylates Ser113 of the dehydrogenase, which blocks the binding of isocitrate and inactivates it; its phosphatase domain reverses the modification. When the cell grows on acetate, about three quarters of the dehydrogenase is phosphorylated; isocitrate then rises, and the lyase, whose affinity for isocitrate is about a hundred times lower than that of the dehydrogenase, takes a larger share. Intermediates of glycolysis and the cycle (oxaloacetate, pyruvate, PEP, 3-phosphoglycerate) and AMP inhibit the kinase and activate the phosphatase, so the dehydrogenase becomes active when the cell has carbon to burn, and the same metabolites inhibit the lyase. As with PFK-2/FBPase-2 ([7.1.19](/7.1.19#sec-19.2.4)), one protein with opposing activities responds to the signals with a ratio that is insensitive to its own amount; for the AceK system, Shinar, Rabinowitz and Alon (2009) showed that the bifunctional design makes the steady-state flux robust to variations in the concentrations of the proteins.

## Summary

The pathway cards ([7.1.16](/7.1.16#sec-16.1.3)):

| Field | Pyruvate dehydrogenase and citric acid cycle | Glyoxylate cycle |
|---|---|---|
| Location | mitochondrial matrix (succinate dehydrogenase in the inner membrane); bacterial cytosol | glyoxysomes of oilseeds (with mitochondria and cytosol); bacteria, fungi |
| Net reaction | pyruvate + CoA + $\ce{NAD+}$ → acetyl-CoA + $\ce{CO2}$ + NADH (Eq. (20.1)); acetyl-CoA + 3 $\ce{NAD+}$ + FAD + GDP + $\mathrm{P_i}$ + 2 $\ce{H2O}$ → 2 $\ce{CO2}$ + 3 NADH + $\ce{FADH2}$ + GTP + 3 $\ce{H+}$ + CoA (Eq. (20.2)) | 2 acetyl-CoA + $\ce{NAD+}$ + 2 $\ce{H2O}$ → succinate + 2 CoA + NADH + $\ce{H+}$ (Eq. (20.3)) |
| Energy account | 10 ATP per acetyl-CoA (1 GTP directly), 12.5 per pyruvate; 30–32 ATP per glucose; efficiency 34% (standard), about 65% (cellular) | no decarboxylation; carbon conserved for gluconeogenesis |
| Committed and regulated steps | PDH complex (irreversible, commits pyruvate carbon to oxidation or fat); citrate synthase, isocitrate DH, α-ketoglutarate DH | isocitrate lyase versus isocitrate DH (branch point) |
| Activators | PDH: AMP, CoA, $\ce{NAD+}$, pyruvate (via PDK), $\ce{Ca^2+}$ (via PDP); IDH: ADP, $\ce{Ca^2+}$; α-KGDH: $\ce{Ca^2+}$; pyruvate carboxylase: acetyl-CoA | (*E. coli*) glycolytic and cycle intermediates activate IDH via the AceK phosphatase |
| Inhibitors | PDH: ATP, acetyl-CoA, NADH, fatty acids; CS: citrate, succinyl-CoA, ATP; IDH: ATP, NADH; α-KGDH: succinyl-CoA, NADH | lyase: PEP, 3-phosphoglycerate and other intermediates |
| Covalent, hormonal and transcriptional control | PDH kinase (Ser of E1α) and phosphatase (insulin, $\ce{Ca^2+}$); PDK4 induced in fasting | AceK phosphorylation of IDH (Ser113) |
| Opposing pathway | none in animals (no net acetyl-CoA → oxaloacetate); anaplerosis replaces withdrawn intermediates (Definition 20.3.2) | — |
| Coenzymes (vitamins) | TPP ($\mathrm{B_1}$), lipoate, CoA ($\mathrm{B_5}$), FAD ($\mathrm{B_2}$), NAD ($\mathrm{B_3}$); biotin ($\mathrm{B_7}$) for anaplerosis | NAD, CoA |
| Diseases and drugs | beriberi, PDH deficiency (lactic acidosis), arsenite; fluoroacetate (aconitase); malonate (SDH); SDH, FH and IDH1/2 mutations, 2-hydroxyglutarate (Definition 20.4.3), IDH inhibitors; dichloroacetate | isocitrate lyase as a target in tuberculosis |

| Topic | Key points |
|---|---|
| PDH complex (Definitions 20.1.2, 20.1.3) | E1 (TPP), E2 core with lipoyl arm, E3 (FAD); five steps; channeling; shared E3 with α-KGDH and BCKDH |
| Eight steps (20.2.2) | condensation (Claisen/aldol, thioester hydrolysis), isomerization (Fe–S), two oxidative decarboxylations, substrate-level phosphorylation (phospho-His), FAD oxidation (Complex II), stereospecific hydration, $\ce{NAD+}$ oxidation pulled by low [OAA] |
| Stereochemistry and tracing (20.2.3–20.2.4) | citrate prochiral; CO₂ of a turn comes from the OAA, not the new acetyl; carboxyl label released in turn 2, methyl label half per turn from turn 3 (Example 20.2.1) |
| Hub (Definitions 20.3.1, 20.3.2) | outflows to amino acids, heme, fatty acids, glucose; anaplerosis by pyruvate carboxylase (acetyl-CoA), PEPCK, PEP carboxylase, malic enzyme |
| Regulation (20.4) | PDH: products and PDK/PDP; three exergonic steps by NADH/NAD⁺, ATP/ADP, Ca²⁺, products; metabolon (Definition 20.4.1); aconitase/IRP1 (Definition 20.4.2) |
| Glyoxylate cycle (Definition 20.5.1) | isocitrate lyase and malate synthase bypass both decarboxylations; three compartments in seeds; AceK |

## Questions

1. Write the net equation for the complete oxidation of one pyruvate by the PDH complex and the citric acid cycle, and count the ATP formed with P/O ratios of 2.5 (NADH) and 1.5 (FADH₂).

   **Answer** Pyruvate + 4 $\ce{NAD+}$ + FAD + GDP + $\mathrm{P_i}$ + 2 $\ce{H2O}$ → 3 $\ce{CO2}$ + 4 NADH + $\ce{FADH2}$ + GTP + 4 $\ce{H+}$ (CoA is regenerated). ATP: $4 \times 2.5 + 1.5 + 1 = 12.5$ per pyruvate, 25 per glucose from the two pyruvates; with the 2 ATP and 2 cytosolic NADH (3 or 5 ATP) of glycolysis this gives 30–32.

2. Malate dehydrogenase has $\Delta_{\mathrm{r}}G'^{\circ} = +29.7\,\mathrm{kJ\,mol^{-1}}$. If $[\ce{NAD+}]/[\mathrm{NADH}]$ in the matrix is 10 and [malate] is 0.2 mM, what is the highest concentration of oxaloacetate at which the reaction can still run forward at 37 °C?

   **Answer** Forward flux requires $\Delta_{\mathrm{r}}G < 0$, i.e. $Q < K'$ with $K' = \mathrm{e}^{-29.7/2.58} = 1.0 \times 10^{-5}$ and $Q = [\mathrm{OAA}][\mathrm{NADH}]/([\mathrm{malate}][\ce{NAD+}])$. So $[\mathrm{OAA}] < K'\,[\mathrm{malate}]\,[\ce{NAD+}]/[\mathrm{NADH}] = 1.0 \times 10^{-5} \times 0.2\,\mathrm{mM} \times 10 = 2 \times 10^{-5}\,\mathrm{mM} = 0.02\,\mu\mathrm{M}$ (ignoring the $\ce{H+}$ already included in $K'$). Oxaloacetate must be kept at nanomolar free concentration, which is achieved by the strongly exergonic citrate synthase reaction and by channeling in the metabolon.

3. Glucose labeled with ¹⁴C at C-1 is oxidized by glycolysis, PDH and the citric acid cycle. In which turn of the cycle is the label first released as CO₂? Where would label from C-3 or C-4 of glucose be lost?

   **Answer** C-1 of glucose becomes C-3 of glyceraldehyde 3-phosphate, the methyl carbon of pyruvate, and the methyl carbon of acetyl-CoA ([7.1.18](/7.1.18), Question 1). A methyl label is not released in turns 1 and 2; half of it appears in CO₂ in turn 3, then half of the rest in each turn (Example 20.2.1). C-3 and C-4 of glucose become the carboxyl of pyruvate and are released as CO₂ by the PDH complex, before the cycle.

4. Why is a ketogenic diet used for patients with PDH deficiency, and why does thiamine deficiency damage the brain first?

   **Answer** In PDH deficiency pyruvate cannot be oxidized; it accumulates and is reduced to lactate (lactic acidosis), and tissues dependent on glucose oxidation, above all the brain, are short of acetyl-CoA. A ketogenic diet supplies fat, whose β oxidation in the liver gives ketone bodies that the brain converts to acetyl-CoA without PDH ([7.1.21](/7.1.21)). Thiamine deficiency affects PDH, α-ketoglutarate dehydrogenase and transketolase; the brain normally depends almost entirely on aerobic oxidation of glucose, which needs both dehydrogenases, so it suffers first.

5. Explain why animals cannot convert acetyl-CoA to glucose, while germinating sunflower seeds can, and calculate how many acetyl-CoA are needed per glucose in the seed.

   **Answer** In the citric acid cycle two carbons are lost as CO₂ per acetyl group entering, so there is no net gain of oxaloacetate, and PDH is irreversible; animals lack isocitrate lyase and malate synthase. In the glyoxylate cycle two acetyl-CoA give one succinate (Eq. (20.3)), which is converted to oxaloacetate and then to PEP with loss of one CO₂ (PEP carboxykinase). Two PEP (from two succinates, i.e. four acetyl-CoA) make one glucose: 4 acetyl-CoA, 8 carbons in, 6 in glucose, 2 lost as CO₂ by PEPCK.

6. (Open question) In *E. coli* growing on acetate, the flux at the isocitrate branch point is divided between isocitrate dehydrogenase ($K_{\mathrm{M}}$ for isocitrate in the micromolar range) and isocitrate lyase ($K_{\mathrm{M}}$ about a hundred times higher). Sketch a model showing how partial phosphorylation of the dehydrogenase redirects flux to the lyase, and argue why the cell does not simply regulate the lyase.

   **Answer** Outline: with total isocitrate supply $J$, the steady state satisfies $J = (1 - \varphi)V_1 S/(K_1 + S) + V_2 S/(K_2 + S)$, where $\varphi$ is the phosphorylated (inactive) fraction of the dehydrogenase, $K_1 \ll K_2$. With $\varphi = 0$ the dehydrogenase, saturated at low $S$, consumes nearly all the flux and keeps $S$ near $K_1$, where the lyase is almost inactive. Raising $\varphi$ lowers the dehydrogenase capacity; $S$ rises toward $K_2$ and the lyase takes the excess, its share increasing steeply because it works in its linear range. Regulating the dehydrogenase rather than the lyase makes use of the difference in affinity: a modest change of one enzyme moves $S$ by orders of magnitude and switches the partition, while the lyase, being unsaturated, responds to $S$ automatically. The bifunctional AceK adds robustness: the phosphorylated fraction depends on the ratio of its two activities, which the metabolites set, not on its amount.
