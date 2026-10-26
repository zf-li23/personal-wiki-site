---
title: Lipid Biosynthesis
description: Acetyl-CoA carboxylase and malonyl-CoA; fatty acid synthase and the acyl carrier protein; the four-step cycle and its comparison with β oxidation; NADPH and the citrate shuttle; regulation of fatty acid synthesis; elongation, desaturation and essential fatty acids; cytochrome P-450; eicosanoid synthesis; triacylglycerols, the triacylglycerol cycle and glyceroneogenesis; the two strategies of phospholipid synthesis, ether lipids and sphingolipids; cholesterol synthesis and its fates; lipoproteins, the LDL receptor and reverse cholesterol transport; SREBP, statins and PCSK9; steroid hormones and isoprenoids; the pathway cards.
---

**Lipids** are the largest energy store of animals and the material of every membrane, and this chapter shows how cells make them from water-soluble precursors. Three principles of anabolism, stated in [7.1.16](/7.1.16) and [7.1.17](/7.1.17), recur throughout. **Biosynthesis** is not **catabolism** in reverse: **fatty acid** synthesis uses a different activated intermediate (malonyl-CoA), a different carrier (the acyl carrier **protein**), a different reductant (**NADPH**) and a different compartment from **β oxidation** ([7.1.21](/7.1.21)), so that the two can be regulated reciprocally. Synthesis is reductive and endergonic, paid for with ATP and NADPH; fatty acid synthesis is the largest single consumer of NADPH in animals, which ties it to the **pentose phosphate pathway** ([7.1.18](/7.1.18#sec-18.6)). And each pathway is regulated at its **committed step**, acetyl-CoA carboxylase for **fatty acids** and HMG-CoA reductase for **cholesterol**, by **allosteric effectors**, by phosphorylation and by **transcription** factors that sense the product. The chapter then follows the assembly of fatty acids into triacylglycerols and membrane lipids, whose structures were introduced in [7.1.12](/7.1.12), and the synthesis, transport and regulation of cholesterol. Here the biochemistry meets medicine directly: the transport of cholesterol in plasma lipoproteins, the LDL **receptor** and the feedback system that controls it explain atherosclerosis and the action of statins, the most prescribed drugs in the world.

## 26.1. Biosynthesis of Fatty Acids

### 26.1.1. Malonyl-CoA and Acetyl-CoA Carboxylase

All the carbons of a fatty acid come from acetyl-CoA, but only the first two enter as acetyl; the others are added from malonyl-CoA, a three-carbon unit made by carboxylation of acetyl-CoA.

**Definition 26.1.1 (Acetyl-CoA Carboxylase and Malonyl-CoA)** **Acetyl-CoA carboxylase** (ACC) is the **biotin**-dependent enzyme that carboxylates acetyl-CoA to **malonyl-CoA**, the activated donor of two-carbon units in fatty acid synthesis:

$$
\text{acetyl-CoA} + \ce{HCO3-} + \ce{ATP} \to \text{malonyl-CoA} + \ce{ADP} + \mathrm{P_i} + \ce{H+}. \tag{26.1}
$$
It has three functional parts: a **biotin** carrier protein, a biotin carboxylase that carboxylates N-1′ of biotin with $\ce{HCO3-}$ and ATP, and a carboxyltransferase that moves the carboxyl group from biotin to acetyl-CoA. The reaction is irreversible and is the committed step of fatty acid synthesis.

```smiles
[O-]C(=O)CC(=O)SC malonyl-SCoA
```

(Malonyl-CoA, with **CoA** abbreviated to a methyl thioester.)

The chemistry is that of pyruvate carboxylase and propionyl-CoA carboxylase ([7.1.17](/7.1.17#sec-17.2.4)): the long biotinyl-lysine arm swings the activated carboxyl between two **active sites**. In animals the three activities are **domains** of one large **polypeptide**; ACC1 in the cytosol of liver and adipose tissue supplies fatty acid synthesis, and ACC2, bound to the outer mitochondrial membrane of muscle and heart, makes malonyl-CoA only to regulate the **carnitine shuttle** (Section 26.1.6). Bacteria have four separate **subunits**. Plants have both forms: a bacterial-type heteromeric **enzyme** in plastids and a homomeric one in the cytosol; grasses, exceptionally, have the homomeric form in their plastids too, which is why the aryloxyphenoxypropionate herbicides that inhibit it kill grasses selectively in broad-leaved crops.

### 26.1.2. Fatty Acid Synthase and the Acyl Carrier Protein

**Definition 26.1.2 (Fatty Acid Synthase and Acyl Carrier Protein)** **Fatty acid synthase** (FAS) is the enzyme system that builds saturated fatty acids from acetyl-CoA and malonyl-CoA by repeating a four-step cycle of condensation, reduction, dehydration and reduction, each turn adding two carbons. Throughout, the growing chain is attached as a **thioester** to the 4′-phosphopantetheine prosthetic group of the **acyl carrier protein** (ACP), a small protein (or domain) whose Ser residue carries the same phosphopantetheine as **coenzyme A**, or to the Cys of the β-ketoacyl-ACP synthase.

Seven activities are needed. In the type I systems of vertebrates and fungi they are domains of multifunctional polypeptides; in the type II systems of bacteria, plant plastids and mitochondria they are separate enzymes.

| Activity | Abbreviation | Role |
|---|---|---|
| malonyl/acetyl-CoA–ACP transferase | MAT | loads acetyl and malonyl groups from CoA onto ACP |
| β-ketoacyl-ACP synthase | KS | condensation; its Cys holds the growing acyl chain |
| β-ketoacyl-ACP reductase | KR | reduces the 3-keto group to a D-3-hydroxyl with NADPH |
| β-hydroxyacyl-ACP dehydratase | DH | removes water to give a trans-Δ² double bond |
| enoyl-ACP reductase | ER | reduces the double bond with NADPH |
| acyl carrier protein | ACP | carries the intermediates between the active sites |
| thioesterase | TE | releases palmitate when the chain reaches C16 |

The mammalian FAS I ($M_{\mathrm{r}}$ 240 000 per chain) works as a homodimer ($M_{\mathrm{r}}$ 480 000) in an X shape, with ACP tethered to the KR domain; the 2 nm phosphopantetheine arm, like the lipoyl arm of the **pyruvate dehydrogenase complex** ([7.1.20](/7.1.20#sec-20.1.3)), swings the **substrate** from site to site, so no intermediate is released (**substrate channeling**). Fungal FAS I is a barrel-shaped $\alpha_6\beta_6$ complex of two polypeptides. Type II synthases make a range of products (branched, hydroxy and unsaturated acids, the precursors of lipid A and of mycolic acids), and their separate enzymes are antibiotic targets: the antituberculosis drug isoniazid inhibits the enoyl-ACP reductase InhA of *Mycobacterium tuberculosis*, and triclosan the corresponding *E. coli* enzyme.

### 26.1.3. The Four-Step Cycle

Before the first cycle, MAT transfers the acetyl group of acetyl-CoA to ACP, from which it moves to the Cys of KS, and loads a malonyl group onto the now free ACP. Then, with the numbering of the first round:

1. Condensation. KS transfers the acetyl group from its Cys to C-2 of the malonyl group on ACP, releasing the malonyl carboxyl as $\ce{CO2}$: a decarboxylative **Claisen condensation** ([6.5.22](/6.5.22)) giving acetoacetyl-ACP. The $\ce{CO2}$ lost is the one added by ACC, so $\ce{CO2}$ is a catalyst of the pathway, not a substrate. The **decarboxylation** is what makes the condensation favourable: condensing two acetyl thioesters is uphill, but the loss of $\ce{CO2}$ generates the nucleophilic carbanion and drives the reaction, the energy having been invested in the ATP of reaction (26.1). The same carboxylation–decarboxylation trick drives the formation of PEP in **gluconeogenesis** ([7.1.19](/7.1.19#sec-19.1.2)).
2. Reduction. KR reduces the 3-keto group with NADPH to D-3-hydroxybutyryl-ACP, the D isomer, not the L isomer of **β oxidation**.
3. Dehydration. DH removes $\ce{H2O}$ from C-2 and C-3 to give trans-Δ²-butenoyl-ACP.
4. Reduction. ER reduces the double bond with NADPH to butyryl-ACP.

The butyryl group then moves from ACP to the KS Cys, a new malonyl group is loaded onto ACP, and the cycle repeats. After seven turns the palmitoyl group (16:0) is released by TE as free palmitate; the length is set by the KS, which does not accept acyl chains longer than C16, and by TE, which prefers C16. Carbons 15 and 16 of palmitate come from the priming acetyl-CoA, all others from malonyl-CoA.

![Fatty acid synthesis compared with β oxidation, drawn with the four intermediates in the same positions. Left, β oxidation in the mitochondrial matrix: acyl-CoA dehydrogenase (FAD), enoyl-CoA hydratase, L-3-hydroxyacyl-CoA dehydrogenase (NAD⁺) and thiolase remove an acetyl-CoA per turn. Right, fatty acid synthesis in the cytosol (in plants, the plastid stroma), running in the opposite direction on the acyl carrier protein (ACP): β-ketoacyl-ACP synthase (KS) condenses the acyl group with malonyl-ACP and releases CO₂; β-ketoacyl-ACP reductase (KR, NADPH) gives the D-3-hydroxy intermediate, β-hydroxyacyl-ACP dehydratase (DH) the trans-Δ² enoyl group, and enoyl-ACP reductase (ER, NADPH) the saturated acyl group, two carbons longer](./plots/fas-vs-beta-oxidation.py)

The comparison with β oxidation is worth memorizing:

| Feature | β oxidation (Definition 21.3.1 of [7.1.21](/7.1.21)) | Fatty acid synthesis |
|---|---|---|
| Compartment (animals) | mitochondrial matrix (and peroxisomes) | cytosol |
| Acyl carrier | CoA | ACP (and the KS Cys) |
| Two-carbon unit | released as acetyl-CoA | added from malonyl-CoA (with loss of $\ce{CO2}$) |
| Order of reactions | dehydrogenation, hydration, dehydrogenation, thiolysis | condensation, reduction, dehydration, reduction |
| Electron carriers | **FAD**, $\ce{NAD+}$ | NADPH (both reductions) |
| Stereochemistry of the 3-hydroxyacyl intermediate | L | D |
| Enzymes | separate enzymes, **trifunctional protein** for long chains | multifunctional FAS I (animals), separate enzymes in FAS II |
| Regulated step | carnitine palmitoyltransferase 1 (malonyl-CoA inhibits) | acetyl-CoA carboxylase |
| **Hormones** | **glucagon**, **epinephrine** stimulate | **insulin** stimulates |

### 26.1.4. Stoichiometry

Forming seven malonyl-CoA and running seven cycles:

$$
\begin{aligned}
7\,\text{acetyl-CoA} + 7\,\ce{CO2} + 7\,\ce{ATP} &\to 7\,\text{malonyl-CoA} + 7\,\ce{ADP} + 7\,\mathrm{P_i},\\
\text{acetyl-CoA} + 7\,\text{malonyl-CoA} + 14\,\mathrm{NADPH} + 14\,\ce{H+} &\to \text{palmitate} + 7\,\ce{CO2} + 8\,\ce{CoA} + 14\,\ce{NADP+} + 6\,\ce{H2O};
\end{aligned}
$$
overall,

$$
8\,\text{acetyl-CoA} + 7\,\ce{ATP} + 14\,\mathrm{NADPH} + 14\,\ce{H+} \to \text{palmitate} + 8\,\ce{CoA} + 7\,\ce{ADP} + 7\,\mathrm{P_i} + 14\,\ce{NADP+} + 6\,\ce{H2O}. \tag{26.2}
$$
(Only six waters appear because one is used by the thioesterase.) In animals the acetyl-CoA must also be brought out of mitochondria at a cost of 2 ATP per acetyl group (Section 26.1.5), so a palmitate costs about $7 + 16 = 23$ ATP and 14 NADPH, roughly 3 ATP per two-carbon unit; its complete oxidation returns 106 ATP ([7.1.21](/7.1.21#sec-21.3.3)).

### 26.1.5. Location, NADPH and the Citrate Shuttle

Fatty acid synthesis takes place where the $[\mathrm{NADPH}]/[\ce{NADP+}]$ ratio is high: in the cytosol of animals and yeast, where the ratio is about 75 in hepatocytes while $[\mathrm{NADH}]/[\ce{NAD+}]$ is only about $10^{-3}$ ([7.1.16](/7.1.16#sec-16.5.1)), and in the plastid stroma of plants, where NADPH comes from **photosystem I** ([7.1.24](/7.1.24)) and ACC is activated by the rise in pH and $\ce{Mg^2+}$ that accompanies illumination, like the **Calvin cycle** enzymes ([7.1.25](/7.1.25#sec-25.2.1)). In liver and adipose tissue, NADPH comes about equally from the **pentose phosphate pathway** and from malic enzyme.

The acetyl-CoA is made in mitochondria, from pyruvate and from the carbon skeletons of amino acids, but the inner membrane is impermeable to it.

**Definition 26.1.3 (Citrate Shuttle)** The **citrate shuttle** carries acetyl groups from the mitochondrial matrix to the cytosol: citrate synthase forms citrate from acetyl-CoA and oxaloacetate in the matrix; the citrate transporter exports it; ATP-citrate lyase in the cytosol cleaves it to acetyl-CoA and oxaloacetate (citrate + ATP + CoA → acetyl-CoA + oxaloacetate + ADP + $\mathrm{P_i}$); oxaloacetate is reduced to malate, which malic enzyme oxidatively decarboxylates to pyruvate, producing NADPH, and pyruvate returns to the matrix, where pyruvate carboxylase makes oxaloacetate again.

Per acetyl group, the shuttle costs two ATP (ATP-citrate lyase and pyruvate carboxylase) and converts one cytosolic **NADH** into one NADPH, about half of what synthesis needs. It is active when the **citric acid cycle** is saturated: high ATP and NADH inhibit isocitrate dehydrogenase ([7.1.20](/7.1.20#sec-20.4.2)), citrate accumulates and leaves the matrix, carrying the signal of abundance with it.

![The citrate shuttle. In the mitochondrial matrix, pyruvate dehydrogenase (PDH) makes acetyl-CoA and pyruvate carboxylase oxaloacetate, which citrate synthase joins into citrate. Citrate leaves on the citrate transporter; in the cytosol ATP-citrate lyase regenerates acetyl-CoA, which acetyl-CoA carboxylase (ACC) converts to malonyl-CoA for fatty acid synthase. Oxaloacetate is reduced by malate dehydrogenase (NADH) to malate, which malic enzyme decarboxylates to pyruvate, producing NADPH; pyruvate returns on the mitochondrial pyruvate carrier. The pentose phosphate pathway supplies the rest of the NADPH](./plots/citrate-shuttle.py)

### 26.1.6. Regulation

When an animal has more fuel than it needs, the excess is converted to fatty acids and stored as **triacylglycerols**; the switch is acetyl-CoA carboxylase, a **regulatory enzyme** controlled on three time scales.

1. Allosteric. Citrate, the signal of a saturated citric acid cycle and the carrier of the carbon itself, activates ACC (raising $V_{\max}$ up to tenfold) and promotes its polymerization into long, active filaments; palmitoyl-CoA, the end product, inhibits it (**feedback inhibition**) and favours the inactive **protomers**. The cytosolic protein MIG12 binds ACC and lowers the citrate needed for polymerization.
2. Covalent. **AMP-activated protein kinase** (AMPK), the sensor of low **energy charge** ([7.1.17](/7.1.17#sec-17.3.5)), phosphorylates ACC1 at Ser79 (and ACC2 at the corresponding site), which inactivates it and lowers its sensitivity to citrate; glucagon and epinephrine promote this inhibitory phosphorylation, and insulin promotes dephosphorylation. Citrate partly reactivates the phosphorylated enzyme, as AMP partly activates phosphorylase b ([7.1.19](/7.1.19#sec-19.5.2)).
3. Transcriptional. Insulin and dietary carbohydrate induce ACC, FAS, the stearoyl-CoA desaturase and the enzymes that supply NADPH, through the transcription factors SREBP-1c (activated by insulin through **mTORC1**, Section 26.5.6) and ChREBP (activated by glucose metabolites); polyunsaturated fatty acids suppress these **genes**, and the **nuclear receptor** LXR, activated by oxysterols, induces SREBP-1c.

Malonyl-CoA links synthesis and oxidation: it inhibits carnitine palmitoyltransferase 1, so the **carnitine shuttle** stops and newly made fatty acids are not oxidized in the same cell ([7.1.21](/7.1.21#sec-21.5.1)). Synthesis and β oxidation are thus regulated reciprocally by a single metabolite in a different compartment, which prevents a **futile cycle**. Inhibitors of ACC and FAS are being developed against fatty liver disease and cancer, whose cells often depend on de novo lipogenesis.

## 26.2. Elongation and Desaturation

### 26.2.1. Elongation

Palmitate is the precursor of longer fatty acids. The elongation systems of the smooth endoplasmic reticulum (and a minor system in mitochondria) add two carbons at a time from malonyl-CoA, with CoA instead of ACP as carrier, by the same four reactions catalyzed by separate membrane enzymes; the condensing enzymes, the elongases ELOVL1–7, determine the chain length of the product and are rate-limiting. Stearate (18:0) and the very-long-chain fatty acids of **sphingolipids**, myelin and skin lipids are made this way.

### 26.2.2. Desaturation

**Definition 26.2.1 (Fatty Acyl-CoA Desaturase)** A **fatty acyl-CoA desaturase** is an enzyme that introduces a cis double bond into a fatty acyl chain by removing two hydrogens; the vertebrate stearoyl-CoA desaturase (SCD) of the ER introduces a Δ⁹ double bond into palmitoyl- or stearoyl-CoA to give palmitoleate or oleate. It is a mixed-function oxidase: $\ce{O2}$ accepts four electrons, two from the acyl chain and two from NAD(P)H through the **flavoprotein** cytochrome $b_5$ reductase and cytochrome $b_5$, and is reduced to two $\ce{H2O}$:

$$
\text{stearoyl-CoA} + \mathrm{NADH} + \ce{H+} + \ce{O2} \to \text{oleoyl-CoA} + \ce{NAD+} + 2\,\ce{H2O}. \tag{26.3}
$$

The desaturase is the reason why animal fat is not solid tallow: oleate is the most abundant fatty acid of human adipose tissue. Its expression is induced by saturated fatty acids, SREBP-1c and LXR; mice lacking SCD1 are lean and resistant to diet-induced obesity and **insulin resistance**. In plants the first desaturation is made by a soluble stearoyl-ACP desaturase of the plastid that takes its electrons from ferredoxin; further double bonds at Δ¹² and Δ¹⁵ are introduced by desaturases of the ER (acting on oleate esterified in phosphatidylcholine) and of the plastid. Plants and bacteria regulate desaturation with temperature to keep their membranes fluid.

**Definition 26.2.2 (Essential Fatty Acid)** An **essential fatty acid** is a fatty acid required in the diet because the animal cannot synthesize it. For mammals the essential fatty acids are linoleate, 18:2(Δ⁹,¹²), the parent of the ω-6 family, and α-linolenate, 18:3(Δ⁹,¹²,¹⁵), the parent of the ω-3 family: mammals can introduce double bonds at Δ⁹ and, with "front-end" desaturases, at Δ⁵ and Δ⁶, between an existing double bond and the carboxyl end, but not beyond Δ⁹ toward the methyl end.

From linoleate, alternating elongation and Δ⁶ and Δ⁵ desaturation make γ-linolenate and arachidonate, 20:4(Δ⁵,⁸,¹¹,¹⁴); from α-linolenate they make eicosapentaenoate (EPA), 20:5. Docosahexaenoate (DHA), 22:6(Δ⁴,⁷,¹⁰,¹³,¹⁶,¹⁹), abundant in retina and brain, is made not by a Δ⁴ desaturase but by elongation to 24:5, Δ⁶ desaturation to 24:6 and one round of peroxisomal β oxidation (the Sprecher pathway). Conversion of α-linolenate to EPA and DHA is inefficient in humans, so fish, which obtain them from algae, are the main dietary source. Rats on a fat-free diet develop scaly skin and stunted growth, cured by linoleate (Burr and Burr, 1929), which established the concept.

### 26.2.3. Oxidases, Oxygenases and Cytochrome P-450

Enzymes that use $\ce{O2}$ are classified by the fate of its atoms.

| Class | What happens to $\ce{O2}$ | Examples |
|---|---|---|
| oxidase | electron acceptor, reduced to $\ce{H2O2}$ or $\ce{H2O}$; no O in the product | acyl-CoA oxidase of peroxisomes ([7.1.21](/7.1.21#sec-21.5.3)), glycolate oxidase, **cytochrome oxidase** ([7.1.23](/7.1.23)) |
| mixed-function oxidase | oxidizes two substrates at once (one of them NAD(P)H), $\ce{O2}$ reduced to $\ce{H2O}$ | fatty acyl-CoA desaturases; the **plasmalogen** desaturase |
| dioxygenase | both atoms enter the product | lipoxygenases, tryptophan 2,3-dioxygenase |
| monooxygenase (hydroxylase, mixed-function oxygenase) | one atom enters the product, the other becomes $\ce{H2O}$ with electrons from a cosubstrate | squalene monooxygenase, phenylalanine hydroxylase (tetrahydrobiopterin), **cytochrome** P-450 enzymes |

**Definition 26.2.3 (Cytochrome P-450)** **Cytochrome P-450** enzymes (CYPs) are heme–thiolate monooxygenases, named for the absorption band at 450 nm of the CO complex of their reduced form, which hydroxylate a substrate RH with one atom of $\ce{O2}$:

$$
\ce{R-H} + \ce{O2} + \mathrm{NADPH} + \ce{H+} \to \ce{R-OH} + \ce{H2O} + \ce{NADP+}, \tag{26.4}
$$
receiving electrons from NADPH through a **flavoprotein** (NADPH–cytochrome P-450 reductase in the ER) or through adrenodoxin reductase and the **iron–sulfur protein** adrenodoxin in mitochondria ([7.1.23](/7.1.23#sec-23.5.2)).

Humans have 57 CYP genes. Some are highly specific enzymes of steroid, **bile acid**, **vitamin** D and **eicosanoid** synthesis; others, mainly in the liver ER, have broad hydrophobic **binding sites** and hydroxylate drugs and xenobiotics, which, often followed by conjugation with glucuronate or glutathione, makes them soluble enough to excrete. Their activity varies with genotype and is induced by their substrates, which explains many drug interactions. Ethanol and barbiturates share a P-450: chronic drinking induces it and makes barbiturates less effective, whereas drinking together with a barbiturate makes both compete for the enzyme, and the combination of two depressants cleared slowly can be lethal. Acetaminophen (paracetamol) is normally conjugated, but a fraction is oxidized by CYP2E1 to a reactive quinone imine that glutathione detoxifies; an overdose exhausts hepatic glutathione and destroys liver cells, which is why the antidote, N-acetylcysteine, restores the supply of cysteine for glutathione synthesis ([7.1.27](/7.1.27)).

## 26.3. Eicosanoids

### 26.3.1. Release of Arachidonate

**Eicosanoids** ([7.1.12](/7.1.12#sec-12.5.2)) are not stored. In response to hormones, cytokines or injury, cytosolic phospholipase $\mathrm{A_2}$ (activated by $\ce{Ca^2+}$ and by MAP kinase phosphorylation) moves to membranes and releases arachidonate from C-2 of phosphatidylcholine and other phospholipids; this step limits the rate of eicosanoid synthesis. Glucocorticoids reduce eicosanoid production partly by inducing an inhibitor of phospholipase $\mathrm{A_2}$ (annexin A1) and by repressing COX-2.

### 26.3.2. The Cyclic Pathway

**Definition 26.3.1 (Cyclooxygenase)** **Cyclooxygenase** (COX, prostaglandin H₂ synthase) is the bifunctional heme enzyme of the ER that converts arachidonate into prostaglandin H₂: its cyclooxygenase activity adds two $\ce{O2}$ to make the cyclic endoperoxide hydroperoxide $\mathrm{PGG_2}$, and its peroxidase activity reduces the hydroperoxide to $\mathrm{PGH_2}$, the common precursor of the **prostaglandins**, prostacyclin and the thromboxanes.

Mammals have two **isozymes** with 60–65% sequence identity: COX-1, expressed constitutively, makes the **prostaglandins** that protect the gastric mucosa and the thromboxane of platelets; COX-2 is induced in inflammation and makes the prostaglandins of pain, fever and inflammation. Tissue-specific synthases convert $\mathrm{PGH_2}$ to the final products: thromboxane synthase of platelets to $\mathrm{TXA_2}$, prostacyclin synthase of endothelium to $\mathrm{PGI_2}$, other synthases to $\mathrm{PGE_2}$, $\mathrm{PGD_2}$ and $\mathrm{PGF_{2\alpha}}$. The subscript gives the number of double bonds: arachidonate gives series-2 prostanoids, EPA the generally less inflammatory series 3.

Nonsteroidal anti-inflammatory drugs act on the cyclooxygenase site. Aspirin acetylates a Ser **residue** in the substrate channel (Ser530 of COX-1), an irreversible inhibition ([7.1.9](/7.1.9#sec-9.4.4)); ibuprofen and naproxen are reversible competitive inhibitors. The pharmacology of low-dose aspirin and of the COX-2-selective inhibitors (rofecoxib and valdecoxib, withdrawn for cardiovascular risk; celecoxib) follows from the cell types that make each product ([7.1.12](/7.1.12#sec-12.5.2)).

### 26.3.3. The Linear Pathway and Pro-Resolving Mediators

Lipoxygenases are non-heme iron dioxygenases that insert $\ce{O2}$ at specific positions of arachidonate without cyclizing it. 5-Lipoxygenase of leukocytes, with its activating protein FLAP, makes leukotriene $\mathrm{A_4}$, the precursor of the chemoattractant $\mathrm{LTB_4}$ and of the cysteinyl leukotrienes $\mathrm{LTC_4}$ and $\mathrm{LTD_4}$, which constrict bronchi in asthma. This linear pathway is not inhibited by NSAIDs. Inflammation must also end (resolution, or catabasis): lipoxins, made from arachidonate by sequential lipoxygenases in two cell types, and resolvins, protectins and maresins, made from EPA and DHA, are specialized pro-resolving mediators that stop the recruitment of neutrophils and promote the clearance of debris. In plants, a 13-lipoxygenase begins the conversion of α-linolenate released from galactolipids into jasmonate, the hormone of defence against herbivores ([7.1.15](/7.1.15#sec-15.5.6)).

## 26.4. Triacylglycerols and Membrane Phospholipids

### 26.4.1. Phosphatidic Acid, the Branch Point

A 70 kg human stores about 15 kg of triacylglycerol, enough for about three months of basal energy needs, against a few hundred grams of **glycogen** that last about a day. Triacylglycerols and **glycerophospholipids** share the first steps. L-Glycerol 3-phosphate is made mainly by reduction of the glycolytic intermediate DHAP by the cytosolic glycerol 3-phosphate dehydrogenase (NADH), and in liver and kidney also by glycerol kinase. Glycerol-3-phosphate acyltransferase (GPAT) and acylglycerol-3-phosphate acyltransferase (AGPAT) then esterify C-1 and C-2 with fatty acyl-CoA, giving lysophosphatidic acid and **phosphatidic acid** ([7.1.12](/7.1.12#sec-12.4.1)). **Phosphatidic acid** is present only in trace amounts but is the **branch point**: phosphatidic acid phosphatase (lipin) converts it to 1,2-diacylglycerol, which **diacylglycerol** acyltransferase (DGAT) acylates to triacylglycerol, or it is activated to CDP-diacylglycerol for phospholipid synthesis (Section 26.4.3). In enterocytes, triacylglycerol is resynthesized instead from absorbed 2-monoacylglycerol.

### 26.4.2. Hormonal Control, the Triacylglycerol Cycle and Glyceroneogenesis

Insulin promotes the conversion of dietary carbohydrate and protein into fat: it activates ACC and induces lipogenic genes, stimulates **lipoprotein lipase** in adipose tissue and inhibits lipolysis. In untreated **diabetes** the reverse holds: without insulin the patient cannot make fatty acids from carbohydrate, oxidizes fat and makes **ketone bodies**, and loses weight ([7.1.21](/7.1.21#sec-21.6.3)).

Even in starvation, about 75% of the fatty acids released by lipolysis are re-esterified to triacylglycerols rather than oxidized, partly within adipose tissue and partly after a round trip through the liver.

**Definition 26.4.1 (Triacylglycerol Cycle)** The **triacylglycerol cycle** is the continuous breakdown of triacylglycerols to fatty acids and their re-esterification, within adipocytes and between adipose tissue and liver (fatty acids carried by albumin to the liver, triacylglycerols returned to adipose tissue in VLDL and released there by **lipoprotein lipase**).

The cycle is a **substrate cycle** ([7.1.17](/7.1.17#sec-17.3.4)) that costs energy (at least 7 ATP equivalents per triacylglycerol resynthesized, counting the activation of three fatty acids and glycerol 3-phosphate formation) but keeps a pool of fatty acids in rapid exchange that can be mobilized in emergencies. Re-esterification in adipose tissue needs glycerol 3-phosphate, yet adipocytes have little glycerol kinase and, in fasting, little **glycolysis**. They make it by **glyceroneogenesis** ([7.1.19](/7.1.19#sec-19.1.5)), an abbreviated **gluconeogenesis** from pyruvate to DHAP through pyruvate carboxylase and PEP carboxykinase (PEPCK), followed by glycerol 3-phosphate dehydrogenase. PEPCK is regulated reciprocally in the two tissues: glucocorticoids induce it in liver (more gluconeogenesis and **glyceroneogenesis**, more VLDL export) and repress it in adipose tissue (less re-esterification, more fatty acid release), increasing the flux through the cycle. Thiazolidinediones, **agonists** of the **nuclear receptor** PPARγ used against **type 2 diabetes**, induce PEPCK and glyceroneogenesis in adipose tissue; more fatty acid is re-esterified, plasma free fatty acids fall, and insulin sensitivity of muscle improves. Pioglitazone remains in use; rosiglitazone was restricted because of concerns about cardiovascular risk.

### 26.4.3. Two Strategies for Attaching Head Groups

The head group of a **glycerophospholipid** is joined to diacylglycerol by a phosphodiester bond, formed from two alcohols and one phosphate. One partner is always activated by cytidine diphosphate (CDP), and CMP leaves when the other alcohol attacks; the central role of cytidine nucleotides was discovered by Eugene Kennedy in the 1950s.

**Definition 26.4.2 (CDP-Diacylglycerol and Kennedy Pathways)** In the **CDP-diacylglycerol pathway** (strategy 1), phosphatidic acid reacts with CTP to give CDP-diacylglycerol, which transfers phosphatidate to the hydroxyl of a head-group alcohol (inositol, glycerol 3-phosphate or, in bacteria and yeast, serine). In the **Kennedy pathway** (strategy 2), the head-group alcohol (choline or ethanolamine) is phosphorylated and activated to CDP-choline or CDP-ethanolamine, which transfers the phosphocholine or phosphoethanolamine to diacylglycerol.

| Phospholipid | Mammalian route |
|---|---|
| phosphatidylcholine (40–50% of membrane lipids) | Kennedy pathway: choline kinase, CTP:phosphocholine cytidylyltransferase (CCT, rate-limiting, an amphitropic enzyme activated when it binds membranes poor in phosphatidylcholine), cholinephosphotransferase; in liver also triple methylation of phosphatidylethanolamine by **S-adenosylmethionine** (PEMT) |
| phosphatidylethanolamine | Kennedy pathway in the ER; decarboxylation of phosphatidylserine in mitochondria |
| phosphatidylserine | head-group exchange: PS synthase 1 (from phosphatidylcholine) and PS synthase 2 (from phosphatidylethanolamine) replace choline or ethanolamine by serine |
| phosphatidylinositol | CDP-diacylglycerol + inositol; phosphorylated by PI kinases to the phosphoinositides of signaling ([7.1.14](/7.1.14#sec-14.3.1)) |
| phosphatidylglycerol, cardiolipin | CDP-diacylglycerol + glycerol 3-phosphate → phosphatidylglycerol phosphate → phosphatidylglycerol; + a second CDP-diacylglycerol → cardiolipin in the inner mitochondrial membrane (bacteria join two phosphatidylglycerols) |

The fatty acids are edited after synthesis: in the Lands cycle, phospholipase $\mathrm{A_2}$ removes the acyl group at C-2 and a lysophosphatidylcholine acyltransferase (LPCAT1–4) adds another, which tailors the polyunsaturated content of each membrane. Choline deficiency, or a methionine-deficient diet that limits PEMT, causes fatty liver, because the liver cannot make enough phosphatidylcholine to package triacylglycerol into VLDL.

![Phosphatidic acid as the branch point of glycerolipid synthesis in mammals. Glycerol 3-phosphate (from dihydroxyacetone phosphate by glycerol 3-phosphate dehydrogenase, or from glycerol by glycerol kinase) is acylated by GPAT and AGPAT to lysophosphatidic acid and phosphatidic acid. Strategy 2: phosphatidic acid phosphatase (lipin) gives diacylglycerol, which DGAT acylates to triacylglycerol or which accepts phosphocholine or phosphoethanolamine from CDP-choline or CDP-ethanolamine. Strategy 1: CDP-diacylglycerol synthase (CDS) activates phosphatidic acid with CTP; CDP-diacylglycerol reacts with inositol to phosphatidylinositol and with glycerol 3-phosphate to phosphatidylglycerol, which with a second CDP-diacylglycerol gives cardiolipin. Head-group interconversions: PEMT methylates phosphatidylethanolamine to phosphatidylcholine with three S-adenosylmethionine; PS synthases 1 and 2 exchange serine for choline or ethanolamine; phosphatidylserine decarboxylase (PSD) in mitochondria regenerates phosphatidylethanolamine](./plots/glycerolipid-synthesis.py)

### 26.4.4. Ether Lipids and Sphingolipids

**Plasmalogens** and platelet-activating factor ([7.1.12](/7.1.12#sec-12.4.1)) are made in peroxisomes and the ER. DHAP is acylated at C-1; alkyl-DHAP synthase then exchanges the acyl group for a long-chain fatty alcohol, forming the ether bond; reduction, a second acylation and head-group attachment follow as for ester lipids; and a desaturase of the ER (identified only in 2020 as TMEM189, now PEDS1) introduces the vinyl ether double bond of plasmalogens. Defects of peroxisome biogenesis abolish plasmalogen synthesis, one cause of the severe neurological disease in Zellweger syndrome.

**Sphingolipids** ([7.1.12](/7.1.12#sec-12.4.4)) are built in four stages. Serine palmitoyltransferase, a **pyridoxal phosphate** enzyme of the ER and the committed step, condenses palmitoyl-CoA with serine (with loss of $\ce{CO2}$) to 3-ketosphinganine; NADPH reduces it to sphinganine; **ceramide** synthases (CerS1–6, each with its preferred chain length) attach a fatty acid in amide linkage; and a desaturase introduces the trans-Δ⁴ double bond, giving **ceramide**. In the Golgi, head groups are attached: phosphocholine from phosphatidylcholine (not from CDP-choline) to make **sphingomyelin**, and sugars from UDP-glucose or UDP-galactose to make **cerebrosides** and, by further **glycosylation**, **gangliosides**. Ceramide reaches the Golgi through the transfer protein CERT at contact sites between the ER and the Golgi.

Lipids made in the ER reach other membranes by vesicles and, often faster, by lipid transfer proteins at membrane contact sites; together with **flippases** ([7.1.13](/7.1.13#sec-13.2.2)), this builds the characteristic lipid composition and asymmetry of each organelle.

## 26.5. Cholesterol: Synthesis, Transport and Regulation

### 26.5.1. Carbon from Acetate

All 27 carbons of **cholesterol** come from acetyl-CoA. Feeding animals acetate labeled with $\ce{^{14}C}$ in the methyl or the carboxyl carbon and degrading the cholesterol formed showed which carbon of acetate became which carbon of the **sterol** (Konrad Bloch, Feodor Lynen, John Cornforth, George Popják; Nobel Prize 1964 to Bloch and Lynen). The labeling pattern revealed the isoprene units and the intermediates mevalonate and squalene. Every animal cell can make cholesterol, so it is not a dietary requirement; the liver makes most of it, about 600 mg a day in an adult on a low-cholesterol diet.

### 26.5.2. Four Stages

Stage 1, acetyl-CoA to mevalonate. Thiolase condenses two acetyl-CoA to acetoacetyl-CoA, and the cytosolic HMG-CoA synthase adds a third to give 3-hydroxy-3-methylglutaryl-CoA (HMG-CoA), the same reactions as in ketogenesis but in a different compartment ([7.1.21](/7.1.21#sec-21.6.1)). Both are Claisen condensations whose equilibria favour cleavage; they are pulled by the next, irreversible step.

**Definition 26.5.1 (HMG-CoA Reductase and Mevalonate)** **HMG-CoA reductase** is the integral membrane enzyme of the ER that reduces HMG-CoA with two NADPH to **mevalonate** (3,5-dihydroxy-3-methylpentanoate), releasing CoA; it catalyzes the committed and principal regulated step of the synthesis of cholesterol and of all other products of the mevalonate pathway in animals:

$$
\text{HMG-CoA} + 2\,\mathrm{NADPH} + 2\,\ce{H+} \to \text{mevalonate} + 2\,\ce{NADP+} + \ce{CoA}. \tag{26.5}
$$

Stage 2, activated isoprenes. Three kinase reactions transfer three phosphoryl groups from ATP to mevalonate; the 3-phosphate of 3-phospho-5-pyrophosphomevalonate is a good leaving group, and its departure together with decarboxylation gives Δ³-isopentenyl pyrophosphate (IPP). An isomerase converts part of it to dimethylallyl pyrophosphate (DMAPP).

```smiles
C[C@@](O)(CCO)CC(=O)[O-] mevalonate
C=C(C)CCOP(=O)([O-])OP(=O)([O-])[O-] IPP
CC(C)=CCOP(=O)([O-])OP(=O)([O-])[O-] DMAPP
```

Stage 3, condensation. The allylic pyrophosphate of DMAPP is a good leaving group; the double bond of IPP attacks the carbocation formed, a head-to-tail condensation that gives geranyl pyrophosphate (C10), and a second IPP gives farnesyl pyrophosphate (FPP, C15), both catalyzed by FPP synthase. Squalene synthase joins two FPP head to head, with reduction by NADPH, to the linear triterpene squalene (C30, first isolated from shark liver).

Stage 4, cyclization. Squalene monooxygenase (with $\ce{O2}$ and NADPH) makes squalene 2,3-**epoxide**, and oxidosqualene cyclase (lanosterol synthase) folds it and closes the four rings in a single cascade of cation–alkene cyclizations and shifts, one of the most complex reactions known in biochemistry, to lanosterol. About 19 further reactions (removal of three methyl groups, saturation and migration of double bonds; several by P-450 enzymes) convert lanosterol to cholesterol. Plants cyclize oxidosqualene to cycloartenol and make phytosterols (stigmasterol, sitosterol); fungi make ergosterol, the target of the antifungal azoles (which inhibit its CYP51 demethylase) and of terbinafine (which inhibits squalene monooxygenase). Squalene synthesis costs 18 ATP (three per activated isoprene); a molecule of cholesterol needs 18 acetyl-CoA, 18 ATP and about 16 NADPH.

![Cholesterol synthesis in four stages. Stage 1: thiolase and HMG-CoA synthase condense three acetyl-CoA to HMG-CoA, which HMG-CoA reductase reduces with 2 NADPH to mevalonate, the committed step and the target of statins. Stage 2: three ATP and a decarboxylation convert mevalonate to isopentenyl pyrophosphate (IPP), which an isomerase interconverts with dimethylallyl pyrophosphate (DMAPP). Stage 3: head-to-tail condensations give geranyl pyrophosphate (C10) and farnesyl pyrophosphate (FPP, C15); squalene synthase joins two FPP head to head (NADPH) to squalene (C30). Stage 4: squalene monooxygenase (O₂, NADPH) gives 2,3-oxidosqualene, which lanosterol synthase cyclizes to lanosterol; about 19 steps remove three carbons and give cholesterol (C27). FPP is also the branch point to dolichols, the side chain of ubiquinone, heme A and prenylated proteins](./plots/cholesterol-synthesis.py)

Plastids of plants, most bacteria, and the apicoplast of the malaria parasite make IPP and DMAPP by a different route, the methylerythritol phosphate (MEP) pathway from pyruvate and glyceraldehyde 3-phosphate, which animals lack; its second enzyme is inhibited by fosmidomycin, an antimalarial candidate.

### 26.5.3. Fates of Cholesterol

Cholesterol cannot be degraded to $\ce{CO2}$ by animals; the body disposes of it only by excretion. Most of the cholesterol made in the liver leaves in three forms: **bile acids** ([7.1.12](/7.1.12#sec-12.4.6)), made by hydroxylation of the steroid nucleus and shortening of the **side chain** (the first and rate-limiting enzyme is the P-450 CYP7A1), and conjugated with glycine or taurine to bile salts; free cholesterol secreted into bile; and cholesteryl esters, made by acyl-CoA:cholesterol acyltransferase (ACAT) of the ER, which are too hydrophobic for membranes and are stored in lipid droplets or packaged into lipoproteins. Bile salts are reabsorbed in the ileum and return to the liver many times a day (enterohepatic circulation); fibre and bile-acid-binding resins interrupt the circuit and force the liver to make more bile acid from cholesterol. Other tissues convert cholesterol to **steroid hormones** (Section 26.6.1) and to vitamin D (skin, liver and kidney), and oxysterols such as 25-hydroxycholesterol act as regulators (Section 26.5.6).

### 26.5.4. Plasma Lipoproteins

**Definition 26.5.2 (Lipoprotein and Apolipoprotein)** A plasma **lipoprotein** is a spherical particle with a core of triacylglycerols and cholesteryl esters and a surface monolayer of phospholipids, free cholesterol and one or more **apolipoproteins**, proteins that solubilize the lipids, target the particle to tissues by binding receptors, and activate or inhibit enzymes that act on it.

Lipoproteins are classified by density, which increases with the fraction of protein and falls with the fraction of triacylglycerol; they are separated by ultracentrifugation.

| Lipoprotein | Density / (g mL⁻¹) | Diameter / nm | Protein, % | Triacylglycerol, % | Cholesteryl esters + cholesterol, % | Main apolipoproteins | Origin and function |
|---|---|---|---|---|---|---|---|
| **chylomicron** | < 0.95 | 100–1000 | 2 | 85 | 4 | B-48, C-II, C-III, E, A-IV | intestine; dietary lipid to tissues |
| VLDL | 0.95–1.006 | 30–80 | 10 | 50 | 19 | B-100, C-II, C-III, E | liver; endogenous triacylglycerol to tissues |
| IDL | 1.006–1.019 | 25–35 | 18 | 30 | 30 | B-100, E | from VLDL |
| LDL | 1.019–1.063 | 18–25 | 23 | 10 | 45 | B-100 | from IDL; cholesterol to tissues |
| HDL | 1.063–1.21 | 5–12 | 55 | 4 | 17 | A-I, A-II, C, E | liver, intestine; reverse cholesterol transport |

(Compositions are typical weight percentages; the remainder is phospholipid. The chylomicron is defined in [7.1.21](/7.1.21#sec-21.1.2).)

| Apolipoprotein | Lipoproteins | Function |
|---|---|---|
| apoA-I | HDL | structural protein of HDL; activates LCAT; accepts cholesterol from ABCA1 |
| apoB-48 | chylomicrons | structural; one per particle; made from the same **mRNA** as apoB-100 after **RNA editing** introduces a **stop codon** at **codon** 2153 ([7.2.18](/7.2.18)) |
| apoB-100 | VLDL, IDL, LDL | structural (one 4536-residue chain per particle); **ligand** of the LDL receptor |
| apoC-II | chylomicrons, VLDL, HDL | activates lipoprotein lipase |
| apoC-III | chylomicrons, VLDL, HDL | inhibits lipoprotein lipase and remnant uptake |
| apoE | chylomicrons, VLDL, IDL, HDL | ligand for the LDL receptor and LRP1; clearance of remnants. The *APOE ε4* allele raises plasma cholesterol and is the strongest common genetic risk factor for Alzheimer disease |

**Definition 26.5.3 (VLDL, LDL and HDL)** **Very-low-density lipoprotein** (VLDL) is the triacylglycerol-rich lipoprotein secreted by the liver around apoB-100. **Low-density lipoprotein** (LDL) is the cholesterol-ester-rich particle that remains when lipoprotein lipase and hepatic lipase have removed most of the triacylglycerol of VLDL (through intermediate-density lipoprotein, IDL), and it delivers cholesterol to tissues through the LDL receptor. **High-density lipoprotein** (HDL) is the small, protein-rich lipoprotein formed from apoA-I that collects cholesterol from peripheral cells and carries it to the liver.

Three routes connect the tissues.

1. Exogenous pathway. Chylomicrons carry dietary lipid from the intestine through the lymph to the blood, where apoC-II activates lipoprotein lipase in the capillaries of muscle and adipose tissue; the cholesterol-rich remnants are taken up by the liver through apoE.
2. Endogenous pathway. The liver packages triacylglycerols and cholesteryl esters made from excess fuel into VLDL. Lipoprotein lipase converts VLDL to IDL, and hepatic lipase converts IDL to LDL. LDL, about 1500 cholesteryl ester molecules in a core surrounded by about 800 phospholipids, 500 cholesterol molecules and one apoB-100, carries most of the cholesterol in human plasma; it is taken up by LDL receptors of peripheral tissues and, mainly, of the liver.
3. Reverse cholesterol transport (Definition 26.5.5).

![The three routes of lipid transport. Exogenous pathway: the intestine secretes chylomicrons (apoB-48, C-II, E); lipoprotein lipase (LPL) with its activator apoC-II releases fatty acids from their triacylglycerol (TAG) to muscle and adipose tissue, and the remnants are taken up by the liver through apoE. Endogenous pathway: the liver secretes VLDL (apoB-100, C-II, E); LPL and hepatic lipase convert it via IDL to cholesterol-rich LDL, which LDL receptors on peripheral cells and, mostly, on the liver take up. Reverse cholesterol transport: lipid-poor apoA-I takes up cholesterol from peripheral cells and macrophages through ABCA1 and ABCG1; LCAT esterifies it (cholesterol C → cholesteryl ester CE), making mature HDL; the liver takes up cholesteryl esters selectively through SR-BI, and CETP transfers some to apoB lipoproteins. The liver excretes cholesterol into bile as such and as bile acids](./plots/lipoprotein-pathways.py)

### 26.5.5. The LDL Receptor and Reverse Cholesterol Transport

**Definition 26.5.4 (LDL Receptor)** The **LDL receptor** is the plasma membrane glycoprotein that binds apoB-100 of LDL (and apoE) and carries it into the cell by receptor-mediated endocytosis in clathrin-coated pits; in the acidic endosome the LDL dissociates and the receptor returns to the surface (about every 10 minutes), while the LDL is delivered to lysosomes, where its cholesteryl esters are hydrolyzed and its protein degraded.

Michael Brown and Joseph Goldstein discovered the receptor through familial hypercholesterolemia (Nobel Prize 1985). Fibroblasts of patients bound no LDL and, unlike normal cells, did not suppress their cholesterol synthesis when LDL was added. Cholesterol released in lysosomes leaves through the proteins NPC2 and NPC1; **mutations** in either cause Niemann–Pick disease type C, in which cholesterol accumulates in lysosomes. In the intestine a related protein, NPC1L1, takes up dietary and biliary cholesterol.

**Definition 26.5.5 (Reverse Cholesterol Transport)** **Reverse cholesterol transport** is the transfer of excess cholesterol from peripheral cells to the liver for excretion: lipid-poor apoA-I accepts cholesterol and phospholipid exported by the **ABC transporter** ABCA1, and HDL takes up more through ABCG1; lecithin–cholesterol acyltransferase (LCAT), activated by apoA-I, transfers an acyl group from phosphatidylcholine to cholesterol, and the cholesteryl esters fill the core and turn the discoidal nascent HDL into spherical HDL; the liver removes the cholesteryl esters selectively through the scavenger receptor SR-BI, without endocytosis of the particle, and cholesteryl ester transfer protein (CETP) moves part of them to VLDL and LDL in exchange for triacylglycerol.

Mutations in ABCA1 cause Tangier disease, with almost no HDL, cholesterol-laden tonsils and macrophages, and early cardiovascular disease. Plasma HDL cholesterol correlates inversely with cardiovascular risk, but this association is not causal in the simple sense: genetic variants that raise HDL cholesterol do not lower risk (Mendelian randomization), and CETP inhibitors that raise HDL cholesterol by 30–130% gave little or no benefit in large trials. The function of HDL in removing cholesterol from macrophages, rather than its cholesterol content, is what matters.

### 26.5.6. Regulation by SREBP and Sterols

Cholesterol synthesis is energetically costly, and excess cholesterol cannot be burned, so cells match synthesis to supply from LDL. HMG-CoA reductase activity varies more than a hundredfold.

**Definition 26.5.6 (SREBP)** A **sterol regulatory element-binding protein** (SREBP) is a membrane-bound transcription factor of the ER whose N-terminal basic helix–loop–helix–leucine zipper domain, released by proteolysis in the Golgi, activates genes with sterol regulatory elements: SREBP-2 controls the genes of cholesterol synthesis and uptake (HMG-CoA reductase, the LDL receptor and PCSK9), SREBP-1c those of fatty acid synthesis. The release is controlled by two sterol-sensing ER proteins: SCAP, which escorts SREBP to the Golgi in COPII vesicles, and Insig, which retains the SCAP–SREBP complex in the ER when cholesterol binds SCAP or oxysterols bind Insig.

When ER cholesterol falls below about 5% of the ER lipids, SCAP changes conformation, releases Insig and carries SREBP to the Golgi, where site-1 protease and the intramembrane site-2 protease cut it twice; the released domain enters the nucleus. When sterols return, the complex stays in the ER and the active domain already in the nucleus is degraded by the **proteasome**, so transcription stops within hours. The ER cholesterol threshold is sharp, so the system acts as a switch. Three further controls act on the enzyme itself:

1. Sterols (lanosterol, 25-hydroxycholesterol) make Insig bind HMG-CoA reductase and recruit **ubiquitin** ligases; the reductase is ubiquitinated and extracted from the ER membrane for degradation by the **proteasome** (ER-associated degradation), with a half-life that falls from hours to less than an hour.
2. AMP-activated protein kinase phosphorylates and inactivates the reductase when the energy charge is low; glucagon promotes and insulin opposes the phosphorylation.
3. High cellular cholesterol activates ACAT, storing the excess as esters, and activates LXR, which induces the export transporters ABCA1 and ABCG1 and the ubiquitin ligase IDOL, which degrades the LDL receptor; the bile acid receptor FXR represses CYP7A1.

![Feedback control of cellular cholesterol by SREBP-2 (SBGN activity flow; open arrows activate, bars inhibit). In the ER, cholesterol binding to SCAP and oxysterol binding to Insig keep the SCAP–SREBP-2 complex in the ER. When sterols fall, SCAP carries SREBP-2 to the Golgi, where site-1 and site-2 proteases release the nuclear bHLH-Zip domain, which activates the genes with sterol regulatory elements (SRE) for HMG-CoA reductase, the LDL receptor, PCSK9 and other sterol genes. HMG-CoA reductase makes cholesterol and the LDL receptor imports it. Sterols also trigger Insig-dependent ubiquitination and ER-associated degradation (ERAD) of the reductase, AMPK phosphorylates and inhibits it, and statins inhibit it competitively; PCSK9 sends the LDL receptor to lysosomal degradation](./plots/srebp-regulation.py)

### 26.5.7. Atherosclerosis, Familial Hypercholesterolemia and Drugs

When the supply of cholesterol exceeds what membranes, bile acids and hormones use, LDL accumulates in the wall of arteries. LDL retained in the extracellular matrix of the intima is oxidized, monocytes enter and become macrophages that take up oxidized LDL through scavenger receptors without feedback limitation, and they become lipid-laden foam cells; over decades the lesions grow into plaques of cholesterol (partly crystalline), foam cell debris, smooth muscle and scar tissue. Rupture of a plaque triggers a thrombus that occludes a coronary or cerebral artery: myocardial infarction or stroke. The causal role of LDL is established by genetics (mutations that raise or lower LDL change risk in proportion to the lifetime exposure) and by trials of drugs that lower LDL.

In familial hypercholesterolemia, mutations in the LDL receptor (or in apoB-100 or gain-of-function mutations in PCSK9) prevent the uptake of LDL; cells do not sense the plasma cholesterol and continue to synthesize their own. Heterozygotes (about 1 in 250 people) have plasma LDL cholesterol about twice normal and heart attacks in middle age; homozygotes have four to six times normal and can have heart attacks in childhood.

**Definition 26.5.7 (Statin)** A **statin** is a competitive inhibitor of HMG-CoA reductase whose dihydroxy acid group mimics the reaction intermediate (mevaldyl-CoA) and occupies the HMG-binding pocket, while its hydrophobic ring system fills a groove of the enzyme; statins bind with inhibition constants in the nanomolar range, about a thousand times more tightly than the substrate HMG-CoA ($K_{\mathrm{M}} \approx 4\,\mu\mathrm{M}$).

The first statin, compactin (mevastatin), was found by Akira Endo in 1976 after screening some 6000 fungal cultures for inhibitors of cholesterol synthesis; lovastatin, from *Aspergillus terreus*, was the first approved (1987), followed by synthetic statins (atorvastatin, rosuvastatin). By the equation of **competitive inhibition** ([7.1.9](/7.1.9#sec-9.4.1)), at [S] = $K_{\mathrm{M}}$ the activity left is $v/v_0 = 2/(2 + [\mathrm{I}]/K_{\mathrm{I}})$, so a statin at ten times its $K_{\mathrm{I}}$ leaves about 17% of the activity. The effect on plasma LDL is mostly indirect: lower synthesis lowers ER cholesterol, SREBP-2 is activated, and the liver makes more LDL receptors and clears more LDL from the blood. The same feedback also raises the amount of HMG-CoA reductase, so cholesterol synthesis falls much less than the direct inhibition would suggest. Statins lower LDL cholesterol by 30–50% and the risk of major cardiovascular events by about 20% per mmol L⁻¹ of LDL cholesterol lowered. By lowering mevalonate they also reduce **isoprenoid** products, including **ubiquinone**; muscle pain is the most common side effect, and serious myopathy is rare.

![Statins and the SREBP feedback. A: fractional activity of HMG-CoA reductase as a function of statin concentration for a competitive inhibitor at [S] = K_M, v/v₀ = (K_M + [S])/(K_M(1 + [I]/K_I) + [S]), for inhibition constants of 0.2, 2 and 20 nM. B: steady states of a minimal feedback model of a hepatocyte (illustrative parameters): SREBP activity s = 1/(1 + (C/K)⁴) falls with cellular cholesterol C; reductase protein and LDL receptors are proportional to s; cholesterol comes from synthesis (reductase amount × remaining activity f) and from LDL uptake; plasma LDL is inversely proportional to the number of LDL receptors. When the statin leaves 20% of the activity (f = 0.2), cellular cholesterol falls by only about a quarter, SREBP-driven reductase and receptor levels rise about 1.8-fold, synthesis falls to about 36% instead of 20%, and plasma LDL falls by about 45%](./plots/statin-inhibition.py)

Other drugs act on the same system. Ezetimibe inhibits the intestinal cholesterol transporter NPC1L1 and lowers LDL by about 20% on top of a statin. PCSK9, a secreted protein made under SREBP-2 control, binds the LDL receptor on the cell surface and diverts it to lysosomes instead of recycling; gain-of-function mutations cause familial hypercholesterolemia, and loss-of-function mutations lower LDL for life and protect against coronary disease. Monoclonal antibodies against PCSK9 (evolocumab, alirocumab, approved in 2015) and a **small interfering RNA** that silences its mRNA in the liver (inclisiran, 2020) lower LDL by about 50–60% more. Bempedoic acid inhibits ATP-citrate lyase, upstream of HMG-CoA reductase, in the liver only. Bile-acid-binding resins, the first drugs shown to reduce heart attacks by lowering cholesterol (1984), act by draining cholesterol into bile acids.

## 26.6. Steroid Hormones and Isoprenoids

### 26.6.1. Steroid Hormones

All **steroid hormones** ([7.1.12](/7.1.12#sec-12.5.3)) are made from cholesterol in the adrenal cortex, gonads and placenta, in small amounts compared with bile acids. The acute, hormone-controlled step is the delivery of cholesterol to the inner mitochondrial membrane by the steroidogenic acute regulatory protein (StAR), stimulated by ACTH or the gonadotropins through **cAMP**. There the side-chain cleavage enzyme P450scc (CYP11A1) hydroxylates C-22 and C-20 and cleaves the bond between them, giving pregnenolone and isocaproaldehyde; three $\ce{O2}$ and three NADPH are used, with electrons supplied by adrenodoxin reductase and adrenodoxin. Pregnenolone is the precursor of all steroid hormones:

| Product | Key enzymes from pregnenolone | Tissue |
|---|---|---|
| progesterone | 3β-hydroxysteroid dehydrogenase (3β-HSD) | corpus luteum, placenta |
| **cortisol** (glucocorticoid) | 3β-HSD, CYP17 (17α-hydroxylase), CYP21 (21-hydroxylase), CYP11B1 (11β-hydroxylase) | adrenal zona fasciculata |
| aldosterone (mineralocorticoid) | 3β-HSD, CYP21, CYP11B2 (aldosterone synthase) | adrenal zona glomerulosa |
| testosterone (androgen) | CYP17 (17α-hydroxylase and 17,20-lyase), 3β-HSD, 17β-HSD; 5α-reductase gives dihydrotestosterone in target tissues | testis (Leydig cells), adrenal |
| estradiol (estrogen) | aromatase (CYP19) from testosterone | ovary, placenta, adipose tissue |

Deficiency of 21-hydroxylase, the most common form of congenital adrenal hyperplasia, blocks cortisol synthesis; the lack of feedback raises ACTH, and the accumulated precursors are diverted to androgens, which virilize female infants. Many drugs inhibit steroidogenic enzymes: aromatase inhibitors (letrozole) treat estrogen-dependent breast cancer, 5α-reductase inhibitors (finasteride) prostate enlargement, and abiraterone (a CYP17 inhibitor) prostate cancer.

### 26.6.2. Isoprenoids

IPP and DMAPP are the building blocks of more than 30 000 isoprenoids (terpenoids) ([7.1.12](/7.1.12#sec-12.5.4)), classified by the number of isoprene units.

| Units (carbons) | Class | Examples |
|---|---|---|
| 2 (C10) | monoterpenes | geraniol, menthol, limonene, pinene: scents and resins of plants |
| 3 (C15) | sesquiterpenes, farnesyl | farnesyl groups of prenylated proteins (**Ras**); artemisinin; insect juvenile hormone |
| 4 (C20) | diterpenes, geranylgeranyl | phytol of **chlorophyll**, gibberellins, taxol; geranylgeranyl groups of Rab and Rho proteins |
| 6 (C30) | triterpenes | squalene, sterols |
| 8 (C40) | tetraterpenes | carotenoids, from which vitamin A derives |
| many | polyprenols | dolichol, the side chains of ubiquinone and **plastoquinone** and of vitamins E and K, natural rubber (cis-polyisoprene) |

Protein prenylation, the attachment of a farnesyl or geranylgeranyl group to a Cys near the C terminus by farnesyltransferase or geranylgeranyltransferases, anchors many signaling proteins to membranes ([7.1.13](/7.1.13#sec-13.1.6)). Several drugs target the pathway downstream of mevalonate: nitrogen-containing bisphosphonates (zoledronate) inhibit FPP synthase in osteoclasts and are used against osteoporosis, and the farnesyltransferase inhibitor lonafarnib (approved in 2020) treats progeria, whose mutant lamin A remains permanently farnesylated. Isoprenoid pathways are also targets of metabolic engineering: yeast engineered with the mevalonate pathway and plant enzymes makes artemisinic acid, the precursor of the antimalarial artemisinin.

## Summary

The pathway cards ([7.1.16](/7.1.16#sec-16.1.3)):

| Field | Fatty acid synthesis | Triacylglycerol and phospholipid synthesis | Cholesterol synthesis |
|---|---|---|---|
| Location | cytosol (animals; ACC1, FAS I); plastid stroma (plants; FAS II) | ER (and mitochondria, peroxisomes, Golgi) | cytosol and ER (mainly liver) |
| Net reaction | 8 acetyl-CoA + 7 ATP + 14 NADPH → palmitate + 8 CoA + 7 ADP + 7 $\mathrm{P_i}$ + 14 $\ce{NADP+}$ + 6 $\ce{H2O}$ (Eq. (26.2)) | glycerol 3-P + 3 acyl-CoA → TAG + 3 CoA + $\mathrm{P_i}$; phospholipids via CDP-diacylglycerol or CDP-alcohol | 18 acetyl-CoA + 18 ATP + ~16 NADPH → cholesterol |
| Energy account | 3 ATP and 2 NADPH per C₂ (including the citrate shuttle, Definition 26.1.3) | 2 ATP per fatty acid activated; 1 CTP per head group | 3 ATP per isoprene; 2 NADPH for mevalonate |
| Committed and regulated steps | acetyl-CoA carboxylase (Definition 26.1.1) | GPAT; lipin; CCT (phosphatidylcholine) | HMG-CoA reductase (Definition 26.5.1) |
| Activators | citrate (polymerization) | insulin; fatty acyl-CoA supply | SREBP-2 at low ER sterol (Definition 26.5.6) |
| Inhibitors | palmitoyl-CoA | — | statins (Definition 26.5.7); sterols (ERAD) |
| Covalent, hormonal and transcriptional control | AMPK phosphorylation (inactivates); glucagon, epinephrine (inhibit), insulin (activates); SREBP-1c, ChREBP; plants: light (pH, $\ce{Mg^2+}$) | glucocorticoids and thiazolidinediones (PPARγ) on PEPCK of glyceroneogenesis | AMPK phosphorylation; insulin, glucagon; LXR, FXR |
| Opposing pathway | β oxidation (malonyl-CoA ⊣ CPT1) | lipolysis (ATGL, **HSL**); triacylglycerol cycle (Definition 26.4.1) | excretion as bile acids and biliary cholesterol; reverse cholesterol transport (Definition 26.5.5) |
| **Coenzymes** (vitamins) | biotin ($\mathrm{B_7}$), pantetheine of ACP and CoA ($\mathrm{B_5}$), NADPH ($\mathrm{B_3}$) | CoA, CTP, **SAM**, **PLP** (serine palmitoyltransferase) | CoA, NADPH, ATP; P-450 **heme** |
| Diseases and drugs | isoniazid, triclosan (FAS II); herbicides (grass ACC); essential fatty acid deficiency | Zellweger syndrome (plasmalogens); choline-deficient fatty liver; thiazolidinediones | familial hypercholesterolemia, atherosclerosis, Niemann–Pick C, Tangier disease; statins, ezetimibe, PCSK9 antibodies and siRNA, bempedoic acid, resins |

| Topic | Key points |
|---|---|
| FAS (Definition 26.1.2) | MAT loads; KS condenses with decarboxylation; KR, DH, ER reduce; D-3-hydroxy; seven turns to palmitate; opposite of β oxidation in carrier, **cofactor**, compartment, stereochemistry |
| NADPH and the citrate shuttle (26.1.5) | NADPH from pentose phosphate pathway and malic enzyme; ATP-citrate lyase; 2 ATP per acetyl |
| Elongation and desaturation (26.2) | ER elongases; Δ⁹ desaturase (mixed-function oxidase, Definition 26.2.1); essential linoleate and α-linolenate (Definition 26.2.2); P-450 (Definition 26.2.3) |
| Eicosanoids (26.3) | phospholipase A₂; COX-1 and COX-2 (Definition 26.3.1), aspirin acetylates Ser; lipoxygenases, leukotrienes, pro-resolving mediators |
| Glycerolipids (26.4) | phosphatidic acid branch point; TAG cycle and glyceroneogenesis; CDP-diacylglycerol and Kennedy pathways (Definition 26.4.2); plasmalogens, ceramide and sphingolipids |
| Cholesterol (26.5) | acetyl-CoA → HMG-CoA → mevalonate → IPP/DMAPP → FPP → squalene → lanosterol → cholesterol; lipoproteins (Definitions 26.5.2, 26.5.3); LDL receptor (Definition 26.5.4); SREBP–SCAP–Insig switch; statins act mainly by inducing LDL receptors |
| Steroids and isoprenoids (26.6) | StAR and P450scc → pregnenolone; CYP17, CYP21, CYP11B, aromatase; prenylation; thousands of terpenoids |

## Questions

1. A soluble liver fraction synthesizing palmitate is given (a) uniformly ¹⁴C-labeled acetyl-CoA; (b) a trace of uniformly labeled acetyl-CoA with an excess of unlabeled malonyl-CoA. Where is the label in palmitate in each case?

   **Answer** (a) Acetyl-CoA is both the primer and, after carboxylation by ACC (present in the fraction), the source of malonyl-CoA; all carbons of palmitate come from it, so palmitate is uniformly labeled. (The carboxyl carbon of malonyl-CoA, which would come from $\ce{HCO3-}$, is lost as $\ce{CO2}$.) (b) The labeled acetyl-CoA is diluted out of the malonyl-CoA pool by the excess unlabeled malonyl-CoA, so it enters only as the primer, which becomes C-15 and C-16, the methyl end, of palmitate.

2. Write the net equation for the synthesis of palmitate from mitochondrial acetyl-CoA in liver, with the citrate shuttle supplying both the acetyl groups and part of the NADPH. How many NADPH must come from the pentose phosphate pathway?

   **Answer** Each acetyl group transferred costs ATP-citrate lyase (1 ATP) and pyruvate carboxylase (1 ATP); if all the oxaloacetate returns via malic enzyme, each turn converts one cytosolic NADH to NADPH. For 8 acetyl groups: 16 ATP and 8 NADH → 8 NADPH. Together with Eq. (26.2): 8 acetyl-CoA (mitochondrial) + 23 ATP + 8 NADH + 6 NADPH (+ $\mathrm{H^+}$, $\ce{H2O}$) → palmitate + 8 CoA + 23 ADP + 23 $\mathrm{P_i}$ + 8 $\ce{NAD+}$ + 6 $\ce{NADP+}$. Of the 14 NADPH, 8 come from malic enzyme and 6 from the pentose phosphate pathway (oxidation of 3 glucose 6-phosphate to ribulose 5-phosphate), in line with the estimate that each source supplies about half.

3. Why is the condensation of fatty acid synthesis made with malonyl-ACP, whereas the first condensation of cholesterol synthesis (two acetyl-CoA → acetoacetyl-CoA) uses no carboxylated intermediate?

   **Answer** Condensing two thioesters by a Claisen reaction is thermodynamically uphill. In fatty acid synthesis each condensation must be pushed forward seven times in a row against reverse thiolysis, at concentrations of intermediates kept low on the enzyme; the decarboxylation of the malonyl group makes each condensation irreversible, paid for by the ATP of carboxylation. In cholesterol synthesis acetoacetyl-CoA is used at once by HMG-CoA synthase, which releases CoA from a thioester and is favourable, and HMG-CoA is then removed irreversibly by HMG-CoA reductase (2 NADPH); the unfavourable first step is pulled by the steps after it.

4. Explain how insulin and glucagon coordinate fatty acid synthesis and β oxidation in the liver, naming the enzymes, their effectors and the compartments.

   **Answer** After a meal, insulin activates protein phosphatases that dephosphorylate (activate) ACC, induces ACC, FAS and SCD1 through SREBP-1c, and glucose metabolism raises citrate, which activates ACC; malonyl-CoA rises in the cytosol and inhibits CPT1 on the outer mitochondrial membrane, so newly made fatty acids are esterified rather than oxidized. In fasting, glucagon (PKA) and AMPK phosphorylate and inactivate ACC; malonyl-CoA falls (malonyl-CoA decarboxylase removes it), CPT1 is released, fatty acids from adipose tissue enter mitochondria and are oxidized, and acetyl-CoA goes to ketone bodies. The separation of compartments lets one cytosolic metabolite, malonyl-CoA, control the entry into the mitochondrial pathway.

5. A patient on a high-dose statin has a 40% lower plasma LDL cholesterol, yet a liver biopsy shows more HMG-CoA reductase protein than before treatment. Explain both observations, and predict the effect of adding a PCSK9 **antibody**.

   **Answer** The statin inhibits the reductase competitively; ER cholesterol falls slightly, SCAP–SREBP-2 moves to the Golgi and SREBP-2 activates its target genes, among them HMG-CoA reductase (and less sterol-triggered degradation of the enzyme), so the enzyme amount rises and partly compensates for the inhibition, and the LDL receptor, so the liver clears more LDL from the plasma. SREBP-2 also induces PCSK9, which limits the gain in receptors; a PCSK9 antibody prevents the lysosomal degradation of LDL receptors, adds to the number of recycling receptors, and lowers LDL by roughly another half.

6. Why are linoleate and α-linolenate essential for mammals while oleate is not? A cat cannot make arachidonate from linoleate. What does this imply for its diet?

   **Answer** Mammalian desaturases introduce double bonds only at Δ⁹ and, with front-end desaturases, between Δ⁹ and the carboxyl end (Δ⁶, Δ⁵); oleate (Δ⁹) can therefore be made from stearate, but double bonds at Δ¹² and Δ¹⁵ cannot, so linoleate (Δ⁹,¹²) and α-linolenate (Δ⁹,¹²,¹⁵) must be eaten. Cats have very low Δ⁶-desaturase activity, so they cannot convert linoleate to arachidonate efficiently; arachidonate itself is essential for them and must come from animal fat, one of the reasons why cats are obligate carnivores.

7. (Open question) Plasma HDL cholesterol is strongly and inversely associated with coronary heart disease, yet drugs that raise HDL cholesterol have failed to reduce heart attacks. Discuss what this teaches about causality and about the biochemistry of reverse cholesterol transport.

   **Answer** Points to cover: an association in observational data can arise because low HDL cholesterol accompanies the true causes (high triacylglycerol-rich lipoproteins, insulin resistance, obesity, smoking); Mendelian randomization, which uses genetic variants that change HDL cholesterol alone, finds no effect on risk, whereas variants that change LDL cholesterol do, in proportion to the change. Biochemically, the HDL cholesterol concentration measures a pool, not a flux: reverse cholesterol transport depends on the efflux capacity of HDL particles (ABCA1, ABCG1, apoA-I function, LCAT) and on the rate of uptake by the liver (SR-BI), so a drug that raises the pool by blocking CETP may slow the return of cholesterol rather than accelerate it; SR-BI deficiency raises HDL cholesterol and increases risk. Measurements of cholesterol efflux capacity, particle number and function, and randomized trials are needed to judge interventions; LDL (apoB) remains the established causal target.
