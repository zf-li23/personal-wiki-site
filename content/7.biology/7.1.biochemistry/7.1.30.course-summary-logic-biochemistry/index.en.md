---
title: "Course Summary: The Logic of Biochemistry"
description: The whole course on one page. Structure, as a table running from chemical property to structure to function for every class of biomolecule, with binding and catalysis treated in one framework. Metabolism, as one map with three hubs and two currencies, then the pathway cards of every pathway, the opposing pathways side by side, the energy ledger of fuels and biosyntheses, the regulator × enzyme matrix and the four metabolic states, and a list of inhibitors, drugs and inherited diseases.
---

This chapter adds no new material; it brings the twenty-nine chapters together in the form the course was built to support. The course has two threads ([7.1.1](/7.1.1)). Part I (7.1.2–7.1.15) explains each class of biomolecule by its chemistry: weak interactions in water, the side chains of the twenty amino acids, the glycosidic bond, base pairing and stacking, and the amphipathic lipid together decide which structures form, and those structures decide what the molecules can do, from binding and catalysis to transport and signaling. Part II (7.1.16–7.1.29) explains metabolism by energy balance and feedback control: every pathway is a short sequence of the reaction classes of [7.1.17](/7.1.17), driven by the carriers ATP and NAD(P)H, made irreversible at a few steps far from equilibrium, and switched at those steps by allosteric effectors, phosphorylation and hormones. A great deal of detail still has to be memorized, above all the amino acids and the pathways, and this page gathers it into tables and charts to be learned against the two threads. Every entry points back to the chapter where it was derived; numbered objects such as Definition 18.1.1 link to their statements. The information pathways (replication, transcription, translation), the third part of Lehninger's book, are the subject of [7.2](/7.2).

## 30.1. Structure and Function

### 30.1.1. Weak Interactions Build Every Structure

The four **noncovalent interactions** (Definition 2.1.2) are each a few kJ mol⁻¹, comparable to $RT = 2.6\,\mathrm{kJ\,mol^{-1}}$ at 37 °C. Because so many act together, a native protein, a double helix or a bilayer is stable, and because each one is weak, binding stays reversible and structures stay dynamic. Every macromolecular structure in Part I is the arrangement that maximizes them in water.

| Interaction | Strength and range | Where it dominates | Chapters |
|---|---|---|---|
| hydrogen bond | about 23 kJ mol⁻¹ to break in water, net 4–10 between solutes that also bond to water; directional | α helix and β sheet (backbone), base pairs, specificity of binding | 7.1.2, 7.1.5, 7.1.11 |
| ionic interaction | strong in vacuum, screened by water ($\varepsilon_{\mathrm{r}} = 78.5$); strong when buried | salt bridges, binding of phosphates and DNA, metal sites | 7.1.2, 7.1.3 |
| **hydrophobic effect** (Definition 2.1.1) | entropic (ordered water released), $\Delta C_p > 0$ | protein cores, lipid bilayers, membrane proteins, ligand binding | 7.1.2, 7.1.6, 7.1.13 |
| van der Waals interaction | about 0.4–4 kJ mol⁻¹ per contact, very short range, many contacts | close packing of protein interiors, base stacking | 7.1.2, 7.1.5, 7.1.11 |

Two quantitative rules recur from 7.1.2 to 7.1.29: a factor of ten in an equilibrium constant or a rate corresponds to $RT\ln 10 = 5.7\,\mathrm{kJ\,mol^{-1}}$ at 25 °C (5.9 at 37 °C), and native structures are only marginally stable, by a few tens of kJ mol⁻¹ (Formula 6.2.1), so that they can be regulated, unfolded and degraded.

### 30.1.2. From Chemical Property to Function

The summaries of Part I each have a three-column table (structural feature → chemical property → biological function). Condensed to one row per class of biomolecule:

| Class | Units and linkage | Decisive chemistry | Structure it imposes | Function it allows | Key numbers |
|---|---|---|---|---|---|
| water (7.1.2) | H₂O, up to four H bonds | polar, high $\varepsilon_{\mathrm{r}}$, ionizes ($K_{\mathrm{w}} = 10^{-14}$) | solvent cage, hydrophobic effect | solvent, buffer (phosphate, His, bicarbonate, Definition 2.3.1), reactant | plasma pH 7.4 = 6.1 + lg(24/1.2) |
| amino acids (7.1.3) | 20 L-α-amino acids, five classes by R group | p$K_{\mathrm{a}}$ of side chains, hydropathy (Definition 3.2.1), Cys thiol, His near pH 7 | zwitterions; peptide chains written N → C (Definition 3.5.1) | catalysis, charge, modification sites (Definition 3.3.1) | p$K_{\mathrm{R}}$: Asp 3.65, Glu 4.25, His 6.0, Cys 8.2, Tyr 10.1, Lys 10.5, Arg 12.5 |
| proteins (7.1.4–7.1.6) | **peptide** bonds, planar and trans | only φ and ψ free (Definition 5.1.2); backbone H bonds | **α helix**, **β sheet**, motifs, domains; four levels (Definitions 5.2.1, 5.3.1, 5.5.1) | the native fold is the free-energy minimum (Proposition 6.1.1); chaperones assist (Definition 6.4.1); misfolding gives amyloid and prions (Definitions 6.5.1, 6.5.2) | 3.6 residues per turn, 0.15 nm rise; stability tens of kJ mol⁻¹ |
| binding proteins (7.1.7) | binding sites complementary to ligands | $K_{\mathrm{d}}$ (Definition 7.1.2); cooperativity between subunits (Definition 7.3.3) | T and R states (Definition 7.3.1) | myoglobin stores, hemoglobin transports $\ce{O2}$; antibodies recognize (Definition 7.4.2) | Mb $p_{50} = 0.26\,\mathrm{kPa}$; Hb $p_{50} \approx 3.5\,\mathrm{kPa}$, $n_{\mathrm{H}} \approx 3$ |
| enzymes (7.1.8–7.1.9) | active site of distant residues (Definition 8.2.1) | binding energy realized in the transition state (Definition 8.3.1, Formula 8.3.1); acid–base, covalent, metal ion catalysis | induced fit; catalytic triad (Definition 8.4.1) | rate enhancement without change of equilibrium; regulation (Definition 9.5.1) | $10^5$–$10^{17}$-fold; $k_{\mathrm{cat}}/K_{\mathrm{M}}$ up to $10^8$–$10^9\,\mathrm{M^{-1}\,s^{-1}}$ |
| carbohydrates (7.1.10) | monosaccharides, glycosidic bonds | anomeric configuration α or β; reducing end | (α1→4)/(α1→6) helices (Definition 10.3.2) vs (β1→4) ribbons (Definition 10.3.3) | fuel storage vs structure; glycans as a code read by lectins (Definition 10.5.2) | glycogen branch every 8–12 residues |
| nucleic acids (7.1.11) | nucleotides, 3′,5′-phosphodiester bonds | complementary H-bond patterns, stacking; 2′-OH in RNA | antiparallel B-DNA (Definition 11.3.3), A and Z forms | stable archive of information (DNA), labile and catalytic RNA | 10.5 bp per turn, 0.34 nm per bp; $T_{\mathrm{m}}$ Formula 11.4.1 |
| lipids (7.1.12) | fatty acids esterified to glycerol or sphingosine; isoprene units | amphipathic or wholly nonpolar; cis bonds bend chains | triacylglycerol droplets; bilayers | long-term fuel (37 kJ g⁻¹), membranes, signals, vitamins | first cis bond lowers the melting point by about 55 °C |
| membranes (7.1.13) | **lipid bilayer** (Definition 13.1.1) with proteins | 3 nm hydrophobic core; fluid; asymmetric | integral, peripheral, amphitropic proteins (Definition 13.1.2) | barrier, transport (Formula 13.3.1), gradients | Na⁺/K⁺-ATPase: 3 Na⁺ out, 2 K⁺ in, ~25% of resting energy use |
| signaling proteins (7.1.14–7.1.15) | receptors, G proteins, kinases, adaptors | conformational switches; reversible phosphorylation | GPCR–G protein, RTK–SH2 assemblies, nuclear receptors | amplification, integration, adaptation (Definition 14.1.1) | cascade gains multiply, up to $10^8$ |

### 30.1.3. Binding and Catalysis in One Framework

Part I uses one quantitative language for binding, catalysis, transport and signaling: each is a saturable function of a concentration, characterized by a midpoint and a steepness.

| Process | Law | Midpoint | Steepness and regulation | Statement |
|---|---|---|---|---|
| binding to independent sites | $\theta = [\mathrm{L}]/([\mathrm{L}] + K_{\mathrm{d}})$ | $K_{\mathrm{d}} = k_{\mathrm{off}}/k_{\mathrm{on}}$ | hyperbolic: 81-fold from 10% to 90% | Formula 7.1.1 |
| cooperative binding | **Hill equation**, $\theta = [\mathrm{L}]^{n_{\mathrm{H}}}/(K_{0.5}^{n_{\mathrm{H}}} + [\mathrm{L}]^{n_{\mathrm{H}}})$; **MWC model** | $K_{0.5}$ | $n_{\mathrm{H}} > 1$; heterotropic effectors shift the T ⇌ R equilibrium | Formulas 7.3.1, 7.3.2 |
| catalysis | Michaelis–Menten, $v_0 = k_{\mathrm{cat}}[\mathrm{E}]_{\mathrm{T}}[\mathrm{S}]/(K_{\mathrm{M}} + [\mathrm{S}])$ | $K_{\mathrm{M}}$ | specificity $k_{\mathrm{cat}}/K_{\mathrm{M}}$; in vivo $[\mathrm{S}]/K_{\mathrm{M}} \approx 0.01$–1 | [6.3.17](/6.3.17), Formula 9.1.1 |
| reversible inhibition | $v_0 = v_{\max}[\mathrm{S}]/(\alpha K_{\mathrm{M}} + \alpha'[\mathrm{S}])$ | $K_{\mathrm{M}}^{\mathrm{app}} = \alpha K_{\mathrm{M}}/\alpha'$ | competitive ($\alpha$), uncompetitive ($\alpha'$), mixed; $\mathrm{IC_{50}}$ | Theorem 9.4.1, Formula 9.4.1 |
| allosteric enzymes | MWC with apparent $L$ | $K_{0.5}$ | sigmoid; K and V systems; **feedback inhibition** | Formula 9.5.1, Definition 9.5.2 |
| modification cycles | Goldbeter–Koshland | $V_1 = V_2$ | **zero-order ultrasensitivity**: $R \to 1$ when both enzymes are saturated | Formula 9.6.1 |
| carriers | $V_0 = V_{\max}[\mathrm{S}]/(K_{\mathrm{t}} + [\mathrm{S}])$ | $K_{\mathrm{t}}$ | stereospecific, saturable; channels do not saturate at physiological concentrations | Formula 13.4.1 |
| receptors | operational model | $\mathrm{EC_{50}} = K_{\mathrm{A}}/(1 + \tau)$ | efficacy $\tau$; agonists and antagonists (Definition 14.1.2) | Formula 14.1.1 |
| kinase cascades | stacked modification cycles | input at half activation | apparent $n_{\mathrm{H}}$ about 5 at the MAPK | Formula 15.1.1 |

The steepness is what matters physiologically: a carrier of $\ce{O2}$ with a hyperbolic curve can deliver at most 29% of its load between lungs and tissues (Proposition 7.3.1), and a hormone can switch a pathway only if the response is steep in the signal.

![Four ways a protein converts an input into a response, on a common normalized axis (the ligand concentration relative to its half-saturating value, or the ratio of kinase to phosphatase activity V₁/V₂ for a modification cycle). A: hyperbolic binding (and Michaelis–Menten kinetics, Formula 7.1.1), cooperative binding with nH = 2.8 as in hemoglobin (Formula 7.3.1), the MAPK of a three-tier cascade with an apparent nH of about 4.9 (Formula 15.1.1) and a covalent modification cycle with both enzymes saturated, J = 0.01 (Formula 9.6.1); the shaded band is the range from 10% to 90% response. B: the response coefficient, the factor by which the input must change to move the response from 10% to 90%: 81 for a hyperbola, 81 to the power 1/nH for a Hill curve and about 1.2 for the saturated cycle](./plots/response-modules.py)

### 30.1.4. Signals Are Built from Binding and Catalysis

| Module | Input → output | Amplification and termination | Chapter |
|---|---|---|---|
| **G protein–coupled receptor** → G protein → effector | hormone → cAMP, IP₃ + DAG, Ca²⁺, cGMP (second messengers, Definition 14.2.4) | receptor is a GEF; Gα GTPase ends the signal; GRK and arrestin desensitize (Definition 14.2.7) | 7.1.14 |
| **receptor tyrosine kinase** → adaptors → Ras → MAPK; PI3K → PKB | growth factor, insulin → gene expression, glucose uptake, glycogen synthesis | trans-autophosphorylation; GAPs and phosphatases (PTEN) terminate | 7.1.15 |
| gated ion channels | ligand or voltage → membrane potential | $10^7$ ions per second per channel; inactivation | 7.1.14 |
| **nuclear receptor** | steroid, thyroid hormone, fatty acids (PPAR) → transcription | slow (hours), changes enzyme amount | 7.1.15, 7.1.29 |
| two-component system | stimulus → His kinase → Asp of response regulator | phosphorelay | 7.1.15 |

## 30.2. The Metabolic Map

### 30.2.1. Three Stages and Two Currencies

Catabolism converges in three stages (Definition 16.1.1): polymers are hydrolyzed to monomers; the monomers are oxidized to a few intermediates, above all acetyl-CoA; acetyl groups are oxidized to $\ce{CO2}$ in the **citric acid cycle** and the electrons are passed to $\ce{O2}$ in **oxidative phosphorylation**. Anabolism diverges from the same few precursors. The two directions are coupled through carriers kept far from equilibrium: ATP (phosphoryl group transfer, $\Delta_{\mathrm{r}}G'^{\circ} = -30.5\,\mathrm{kJ\,mol^{-1}}$, in cells −47 to −65), NADH for catabolic oxidations (cytosolic $[\ce{NAD+}]/[\mathrm{NADH}] \approx 10^{3}$), NADPH for reductive biosynthesis ($[\ce{NADP+}]/[\mathrm{NADPH}] \approx 10^{-2}$), and acetyl-CoA as the carrier of activated acyl groups (7.1.16).

### 30.2.2. One Map

![Overall map of energy metabolism in a liver-like mammalian cell, condensed from 7.1.18–7.1.28. The cytosol is on the left and at the top, the mitochondrial matrix in the box at the right. Black arrows are catabolic steps, blue arrows anabolic steps, including the gluconeogenic bypasses that run beside glycolysis (glucose 6-phosphatase, FBPase-1, and pyruvate carboxylase plus PEP carboxykinase through oxaloacetate). Gold: the three hubs, glucose 6-phosphate, pyruvate and acetyl-CoA. Glucose 6-phosphate exchanges with glycogen (phosphorylase, glycogen synthase), enters glycolysis or the oxidative pentose phosphate pathway (NADPH, ribose 5-phosphate for nucleotides). Pyruvate is reduced to lactate, carboxylated to oxaloacetate or oxidized by the PDH complex to acetyl-CoA, which also comes from β oxidation of fatty acyl-CoA imported by the carnitine shuttle. Acetyl-CoA enters the citric acid cycle, gives ketone bodies in the liver, or leaves the matrix as citrate (citrate shuttle) to supply cytosolic acetyl-CoA for fatty acid synthesis (ACC, FAS) and cholesterol synthesis (HMG-CoA reductase); palmitate is esterified with glycerol 3-phosphate to triacylglycerols. Amino groups go to urea, carbon skeletons to pyruvate and the cycle intermediates. NADH and FADH₂ from glycolysis, the PDH complex, β oxidation and the cycle feed the respiratory chain and ATP synthase. The small arcs mark the carriers used or made at each step](./plots/metabolic-map.py)

### 30.2.3. Three Hubs

| Hub | Comes from | Goes to | Decided by |
|---|---|---|---|
| glucose 6-phosphate | blood glucose (hexokinase, **glucokinase** in liver, Definition 19.2.2), glycogen (phosphorylase, phosphoglucomutase), gluconeogenesis | glycolysis; glycogen; oxidative **pentose phosphate pathway** (NADPH, ribose 5-phosphate); free glucose (liver, glucose 6-phosphatase in the ER); glucuronides | PFK-1 vs FBPase-1 (fructose 2,6-bisphosphate), glycogen synthase vs phosphorylase, G6PD ($\ce{NADP+}$) (7.1.18, 7.1.19) |
| pyruvate | glycolysis, lactate (LDH), alanine and other glucogenic amino acids | lactate (regenerates $\ce{NAD+}$, Definition 18.4.1); alanine; acetyl-CoA (**pyruvate dehydrogenase complex**, irreversible); oxaloacetate (pyruvate carboxylase) | acetyl-CoA inhibits the PDH complex and activates pyruvate carboxylase; PDH kinase and phosphatase; $\mathrm{O_2}$ supply (7.1.20) |
| acetyl-CoA | pyruvate, **β oxidation**, ketogenic amino acids, ketone bodies (outside the liver) | citric acid cycle; ketone bodies (liver, when oxaloacetate is withdrawn for gluconeogenesis); citrate shuttle → fatty acids, cholesterol; acetylation of proteins | citrate synthase (oxaloacetate supply), malonyl-CoA ⊣ CPT1, ACC (citrate, AMPK, hormones) (7.1.21, 7.1.26) |

Two consequences of the hubs explain much of physiology. Acetyl-CoA cannot be converted to pyruvate or to net oxaloacetate in animals (the PDH reaction is irreversible and the cycle loses both carbons as $\ce{CO2}$), so even-chain fatty acids give no glucose; plants and bacteria escape this with the **glyoxylate cycle** (Definition 20.5.1). And because the **citric acid cycle** is an **amphibolic pathway** (Definition 20.3.1), intermediates withdrawn for biosynthesis must be replaced by **anaplerotic reactions** (Definition 20.3.2).

### 30.2.4. Compartments and Shuttles

| Compartment | Pathways | Shuttles across its membrane |
|---|---|---|
| cytosol | glycolysis, pentose phosphate pathway, glycogen, most of gluconeogenesis, fatty acid synthesis, early cholesterol synthesis, purine and pyrimidine synthesis (except DHODH), part of the urea cycle | — |
| mitochondrial matrix | PDH complex, citric acid cycle, β oxidation, ketogenesis, pyruvate carboxylase, CPS I and OTC of the urea cycle, heme synthesis (first and last steps) | **carnitine shuttle** (acyl groups in, Definition 21.2.1); **citrate shuttle** (acetyl groups out, Definition 26.1.3); **malate–aspartate shuttle** (2.5 ATP) and **glycerol 3-phosphate shuttle** (1.5 ATP) for cytosolic NADH (Definitions 23.3.5, 23.3.6); ANT and phosphate carrier |
| inner mitochondrial membrane | respiratory chain, ATP synthase, succinate dehydrogenase, DHODH | proton circuit, **proton-motive force** (Definition 23.2.4) |
| ER | glucose 6-phosphatase, elongation and desaturation, TAG and phospholipid synthesis, HMG-CoA reductase, cytochrome P-450 | — |
| peroxisome | very-long-chain and branched fatty acid oxidation, plasmalogen synthesis, photorespiration (plants) | — |
| chloroplast | light reactions (thylakoid), **Calvin cycle**, starch, plant fatty acid synthesis | triose phosphate/$\mathrm{P_i}$ antiporter (7.1.25) |

## 30.3. Pathway Cards

Each chapter of Part II ends with a card for each of its pathways, using the fields of 16.1.3. Collected here, condensed to the regulation and the accounts; net reactions and diseases are in the chapters and in 30.5 and 30.7.

### 30.3.1. Degradative Pathways

| Pathway | Location | Yield | Committed and regulated steps | Activators | Inhibitors | Covalent and hormonal control | Coenzymes (vitamins) |
|---|---|---|---|---|---|---|---|
| **glycolysis** (7.1.18) | cytosol, all cells | 2 ATP + 2 NADH per glucose; $\Delta_{\mathrm{r}}G \approx -100\,\mathrm{kJ\,mol^{-1}}$ | hexokinase, PFK-1 (committed), pyruvate kinase | AMP, ADP, F2,6BP (PFK-1); F1,6BP (PK) | ATP, citrate, $\ce{H+}$ (PFK-1); G6P (hexokinase); ATP, acetyl-CoA, alanine, fatty acids (PK) | glucagon/PKA: PK-L ↓, F2,6BP ↓; insulin, HIF-1 induce | $\ce{NAD+}$ (niacin) |
| oxidative pentose phosphate pathway (7.1.18) | cytosol | 2 NADPH + ribose 5-P + $\ce{CO2}$ per G6P | G6PD | $\ce{NADP+}$ | NADPH | — | $\ce{NADP+}$; TPP (transketolase) |
| glycogen breakdown (7.1.19) | cytosol, liver and muscle | Glc 1-P without ATP; 3 ATP per residue to lactate | glycogen phosphorylase | AMP, $\ce{Ca^2+}$ (muscle) | ATP, G6P (muscle), glucose (liver) | epinephrine, glucagon → PKA → phosphorylase kinase → phosphorylase *a*; insulin → PP1 | PLP (B₆) |
| PDH complex and **citric acid cycle** (7.1.20) | matrix | 10 ATP per acetyl-CoA, 12.5 per pyruvate | PDH complex; citrate synthase, isocitrate DH, α-KG DH | AMP, CoA, $\ce{NAD+}$, $\ce{Ca^2+}$ (PDH); ADP, $\ce{Ca^2+}$ (IDH) | ATP, acetyl-CoA, NADH, fatty acids (PDH); citrate, succinyl-CoA (CS); NADH | PDH kinase (inactivates), PDH phosphatase (insulin, $\ce{Ca^2+}$) | TPP (B₁), lipoate, CoA (B₅), FAD (B₂), NAD (B₃) |
| **β oxidation** (7.1.21) | matrix (peroxisomes for very long chains) | palmitate 106 ATP (7n − 6, Formula 21.3.1) | CPT1 (carnitine shuttle) | fatty acid supply (fasting) | malonyl-CoA (CPT1); NADH, acetyl-CoA | PKA: lipolysis (HSL, perilipin); PPARα induces | CoA, FAD, NAD, carnitine; biotin, B₁₂ for odd chains |
| ketogenesis and ketolysis (7.1.21) | liver matrix; use in heart, muscle, brain | β-hydroxybutyrate → 2 acetyl-CoA + NADH − 1 GTP | mitochondrial HMG-CoA synthase | high fatty acid flux, low oxaloacetate | insulin | PPARα induces HMGCS2 | CoA, NAD |
| amino acid catabolism and **urea cycle** (7.1.22) | liver; CPS I and OTC in matrix | urea costs 4 high-energy phosphates | CPS I | N-acetylglutamate (obligatory), arginine | lack of N-acetylglutamate | glucagon, glucocorticoids induce all five enzymes | PLP (aminotransferases), THF, SAM, B₁₂, BH₄ |
| **oxidative phosphorylation** (7.1.23) | inner mitochondrial membrane | 2.5 ATP per NADH, 1.5 per $\ce{FADH2}$; 10 $\ce{H+}$ per NADH | Complex IV (far from equilibrium) | ADP, $\mathrm{P_i}$ (**respiratory control**, Definition 23.2.2) | high [ATP]/[ADP][$\mathrm{P_i}$]; IF1 in hypoxia | HIF-1, PGC-1α; norepinephrine → UCP1 | NAD, FMN, FAD, ubiquinone, hemes, Fe–S, Cu |

### 30.3.2. Biosynthetic Pathways

| Pathway | Location | Cost | Committed and regulated steps | Activators | Inhibitors | Covalent and hormonal control | Coenzymes (vitamins) |
|---|---|---|---|---|---|---|---|
| **gluconeogenesis** (7.1.19) | liver, kidney; PC in matrix, glucose 6-phosphatase in ER | 4 ATP + 2 GTP + 2 NADH per glucose | pyruvate carboxylase, PEPCK, FBPase-1, glucose 6-phosphatase | acetyl-CoA (PC) | AMP, F2,6BP (FBPase-1) | glucagon/PKA lowers F2,6BP; glucagon, cortisol induce PEPCK; insulin represses | biotin (B₇), NAD |
| glycogen synthesis (7.1.19) | cytosol, liver and muscle | 1 UTP per residue (+1 ATP from glucose) | glycogen synthase | G6P | phosphorylation (GSK3, PKA, AMPK) | insulin → PKB ⊣ GSK3; PP1 | UDP-glucose |
| light reactions (7.1.24) | thylakoid | 8 photons → $\ce{O2}$ + ~3 ATP + 2 NADPH | charge separation in PSII and PSI; $b_6f$ the slowest step | light | DCMU, atrazine; paraquat | state transitions (LHCII phosphorylation), cyclic flow | chlorophylls, carotenoids, plastoquinone, Mn₄CaO₅, Fe–S, Cu |
| **Calvin cycle** (7.1.25) | stroma | 3 ATP + 2 NADPH per $\ce{CO2}$ | **rubisco**, FBPase, SBPase, PRK | light: pH ≈ 8, $\ce{Mg^2+}$, reduced thioredoxin; rubisco activase | darkness (disulfides), CA1P | ferredoxin–thioredoxin switches | NADPH, TPP |
| **photorespiration** (7.1.25) | chloroplast, peroxisome, mitochondrion | about 3.5 ATP + 2 NADPH and 0.5 $\ce{CO2}$ lost per oxygenation | rubisco oxygenation ($S_{\mathrm{c/o}}$, Definition 25.3.2) | high $\ce{O2}$, high temperature | high $\ce{CO2}$ (C4, CAM) | — | PLP, THF, lipoate, NAD, FMN |
| fatty acid synthesis (7.1.26) | cytosol (plants: plastid) | 7 ATP + 14 NADPH per palmitate (+ 2 ATP per acetyl exported) | **acetyl-CoA carboxylase** | citrate | palmitoyl-CoA | AMPK, glucagon, epinephrine inactivate; insulin activates; SREBP-1c, ChREBP induce | biotin, pantetheine (ACP), NADPH |
| TAG and phospholipid synthesis (7.1.26) | ER | 2 ATP per fatty acid activated; 1 CTP per head group | GPAT, lipin, CCT | insulin | — | glyceroneogenesis (PEPCK) under glucocorticoids and PPARγ | CoA, CTP, SAM |
| cholesterol synthesis (7.1.26) | cytosol and ER, mainly liver | 18 acetyl-CoA + 18 ATP + ~16 NADPH | **HMG-CoA reductase** | SREBP-2 at low ER sterol | sterols (ERAD), **statins** | AMPK, glucagon inactivate; insulin opposes | CoA, NADPH |
| **nitrogen fixation** (7.1.27) | diazotrophs | 16 ATP + 8 e⁻ per $\ce{N2}$ | **nitrogenase** | ATP, low $\ce{NH4+}$ | ADP, $\ce{O2}$ | ADP-ribosylation of the Fe protein | Fe–S, FeMo cofactor |
| ammonia assimilation (7.1.27) | all organisms | 1 ATP + 1 NAD(P)H per glutamate | **glutamine synthetase** | α-KG, ATP | eight cumulative feedback inhibitors | adenylylation cascade (PII, UT/UR) | NAD(P)H or ferredoxin |
| amino acid synthesis (7.1.27) | cytosol, plastids | 12 (Gly, Ala) to 74 (Trp) high-energy bonds | first enzyme after each branch point | — | end products (Section 27.2.7) | repression, attenuation | PLP, THF, SAM, TPP, B₁₂ |
| heme synthesis (7.1.27) | mitochondria and cytosol | 8 Gly + 8 succinyl-CoA per heme | ALA synthase | — | heme; lead (ALAD, ferrochelatase) | heme represses ALAS1; iron controls ALAS2 | PLP |
| purine synthesis (7.1.28) | cytosol (purinosomes) | 6 high-energy phosphates per IMP | PRPP synthetase; Gln–PRPP amidotransferase | PRPP | IMP, AMP, GMP | mTORC1–ATF4, Myc | THF (folate) |
| pyrimidine synthesis (7.1.28) | cytosol; DHODH in inner membrane | 4 high-energy phosphates per UMP | CPS II (animals), ATCase (bacteria) | PRPP, ATP | UTP, UDP; CTP (bacterial ATCase) | ERK and S6K phosphorylate CAD | FMN, ubiquinone |

## 30.4. Opposing Pathways

Every degradative pathway that has a biosynthetic counterpart differs from it in at least one step: a pathway run backwards through the same enzymes would have the opposite sign of $\Delta_{\mathrm{r}}G$ and could not be switched independently. The difference is placed at the steps far from equilibrium (Formula 17.3.1), and the two directions are given different enzymes, different carriers or different compartments, and are controlled by **reciprocal regulation** (Definition 19.2.1). If both enzymes of a pair worked at once, the pair would form a **substrate cycle** (Definition 17.3.2) that hydrolyzes ATP.

| Pair | Compartments | Carriers and activated units | Redox coenzyme | Distinct enzymes (control points) | Reciprocal signals | Hormones |
|---|---|---|---|---|---|---|
| glycolysis / gluconeogenesis (7.1.19) | cytosol / cytosol + matrix (PC) + ER (glucose 6-phosphatase) | ATP made / 4 ATP + 2 GTP spent | $\ce{NAD+}$ / NADH (the same pair, run in opposite directions) | hexokinase vs glucose 6-phosphatase; PFK-1 vs FBPase-1; PK vs PC + PEPCK | F2,6BP and AMP: PFK-1 +, FBPase-1 −; acetyl-CoA: PDH −, PC + | insulin / glucagon (PFK-2/FBPase-2, PK-L) |
| glycogen breakdown / synthesis (7.1.19) | cytosol / cytosol | phosphorolysis to Glc 1-P / UDP-glucose | none | glycogen phosphorylase vs glycogen synthase | G6P: phosphorylase −, synthase +; AMP, $\ce{Ca^2+}$; glucose (liver) | PKA phosphorylates both (phosphorylase on, synthase off); insulin → PP1, PKB ⊣ GSK3 |
| β oxidation / fatty acid synthesis (7.1.21, 7.1.26) | matrix / cytosol | CoA / ACP, malonyl-CoA as donor | FAD, $\ce{NAD+}$ / NADPH | CPT1 vs ACC; L- vs D-3-hydroxyacyl intermediates | malonyl-CoA ⊣ CPT1; citrate activates ACC; palmitoyl-CoA inhibits ACC | glucagon, epinephrine, AMPK inactivate ACC; insulin activates ACC |
| amino acid degradation / synthesis (7.1.22, 7.1.27) | liver (urea cycle spans matrix and cytosol) / many tissues | transamination both ways; $\ce{NH4+}$ to urea / GS–GOGAT | $\ce{NAD+}$ (Glu DH) / NADPH | CPS I and the urea cycle vs the first enzyme after each branch point | N-acetylglutamate on CPS I; end-product feedback in synthesis | glucagon, glucocorticoids induce the urea cycle; essential amino acids (Definition 27.2.1) cannot be made at all |
| respiration / photosynthesis (7.1.23–7.1.25) | mitochondria / chloroplasts | the same rotary ATP synthase; Q cycle in Complex III and in $b_6f$ | NADH / NADPH | Complexes I–IV vs PSII, $b_6f$, PSI; citric acid cycle vs Calvin cycle | thioredoxin activates the Calvin cycle and inactivates G6PD in the light | — |
| purine synthesis / degradation and salvage (7.1.28) | cytosol | PRPP / free bases | — | amidotransferase vs xanthine oxidase; HGPRT and APRT salvage | IMP, AMP, GMP feedback | — |

The fatty acid pair shows the full logic in one example: the four reactions of β oxidation (oxidation, hydration, oxidation, thiolysis; 17.1.3) are reversed in synthesis by condensation, reduction, dehydration, reduction, on another carrier, in another compartment, with another reductant and another stereoisomer, and a single metabolite, malonyl-CoA, links them by inhibiting CPT1 (26.1.6).

## 30.5. Energy Accounting

### 30.5.1. Yield of Fuels

| Fuel | Route | ATP per molecule | Chapter |
|---|---|---|---|
| glucose | anaerobic glycolysis to lactate or ethanol | 2 | 7.1.18 |
| glycogen glucose residue | anaerobic, phosphorolysis saves the hexokinase ATP | 3 | 7.1.18, 7.1.29 |
| pyruvate | PDH + cycle + oxidative phosphorylation | 12.5 | 7.1.20 |
| acetyl-CoA | one turn of the cycle (3 NADH, 1 $\ce{FADH2}$, 1 GTP) | 10 | 7.1.20 |
| glucose | aerobic; 30 with the glycerol 3-phosphate shuttle, 32 with the malate–aspartate shuttle | 30–32 | 7.1.20, 7.1.23 |
| palmitate | activation (−2) + 7 turns of β oxidation + 8 acetyl-CoA | 106 ($7n - 6$, Formula 21.3.1) | 7.1.21 |
| β-hydroxybutyrate | 2 acetyl-CoA + 1 NADH − 1 GTP (CoA transfer) | 21.5 | 7.1.21 |
| NADH → $\ce{O2}$ | $\Delta E'^{\circ} = 1.136\,\mathrm{V}$, $\Delta_{\mathrm{r}}G'^{\circ} = -219\,\mathrm{kJ\,mol^{-1}}$ (Example 16.4.2) | 2.5 (**P/O ratio**, Formula 23.3.1) | 7.1.23 |

The ATP counts rest on the P/O ratios, which are not integers because ATP synthesis and proton pumping are coupled only through the **proton-motive force**: with a c ring of eight subunits, $8/3 + 1 = 3.7$ protons per ATP made and exported, and 10 protons per NADH (Example 23.3.1). Glucose oxidation conserves 34% of its free energy in standard terms and about 65% at the phosphorylation potential of the cell (20.2.5); fermentation gives about a fifteenth as much ATP, which is why the **Pasteur effect** exists and why the **Warburg effect** of proliferating cells needs another explanation (Definition 18.4.2). Per gram, fat (37 kJ g⁻¹) carries about six times the energy of hydrated glycogen (about 6 kJ g⁻¹) (Example 12.3.1); per carbon, palmitate gives 6.6 ATP and glucose 5.3, because fatty acid carbon is more reduced.

### 30.5.2. Cost of Biosynthesis

| Product | Cost | Chapter |
|---|---|---|
| glucose from 2 pyruvate | 4 ATP + 2 GTP + 2 NADH | 7.1.19 |
| glycogen residue from glucose | 1 ATP + 1 UTP | 7.1.19 |
| triose phosphate from 3 $\ce{CO2}$ | 9 ATP + 6 NADPH (C4 plants: 5 ATP + 2 NADPH per $\ce{CO2}$) | 7.1.25 |
| palmitate from 8 acetyl-CoA | 7 ATP + 14 NADPH; with the citrate shuttle 3 ATP + 2 NADPH per C₂ | 7.1.26 |
| cholesterol | 18 acetyl-CoA + 18 ATP + about 16 NADPH | 7.1.26 |
| $\ce{NH4+}$ from $\ce{N2}$ | about 13 ATP equivalents per $\ce{NH3}$ (Example 27.1.1) | 7.1.27 |
| amino acids | 12 (Gly, Ala) to 74 (Trp) high-energy bonds | 7.1.27 |
| IMP / UMP | 6 / 4 high-energy phosphates | 7.1.28 |
| urea | 4 high-energy phosphates (about 5 ATP recovered from NADH of Glu DH and MDH) | 7.1.22 |
| substrate cycling | $r/(1 - r)$ ATP per unit of net flux for an amplification $(1 + r)/(1 - r)$ (Eq. (19.5)) | 7.1.19 |

![The energy ledger of metabolism, assembled from the pathway cards. A: ATP formed per molecule of fuel, with P/O ratios of 2.5 for NADH and 1.5 for FADH₂; aerobic glucose yields 30 or 32 depending on the shuttle that carries cytosolic NADH into the mitochondria, palmitate 7n − 6 = 106, and β-hydroxybutyrate 21.5 (two acetyl-CoA plus one NADH, less the GTP spent on CoA transfer). B: the same yields per carbon atom; the reduced carbon of fatty acids and ketone bodies gives more ATP than carbohydrate carbon, and fermentation extracts very little. C: cost of biosynthesis per molecule of product, as high-energy phosphates (ATP, GTP, UTP, CTP) and as reduced carriers (NADH for gluconeogenesis, NADPH for the Calvin cycle, fatty acid and cholesterol synthesis), side by side; the palmitate cost includes the 2 ATP per acetyl group of the citrate shuttle](./plots/energy-ledger.py)

## 30.6. Regulation

### 30.6.1. Principles

| Principle | Statement | Chapter |
|---|---|---|
| regulate far from equilibrium | only steps with $\lvert\Delta_{\mathrm{r}}G\rvert \gg RT$ set the direction; near-equilibrium steps follow (Formula 17.3.1) | 7.1.17 |
| regulate the **committed step** | the first irreversible step unique to a pathway (Definition 17.3.1), often by **feedback inhibition** | 7.1.9, 7.1.17 |
| four time scales | allostery (ms–s), covalent modification (s–min), compartments, enzyme amount (h–days) | 7.1.17 |
| energy charge | held at 0.8–0.95 (Definition 17.3.3); AMP, amplified by adenylate kinase, is the sensitive signal | 7.1.17 |
| control is shared | **flux control coefficients** sum to one (Theorem 17.4.1); feedback hands control to demand (17.4.4) | 7.1.17 |
| switches need steepness | cooperativity, zero-order ultrasensitivity, cascades, substrate cycles (30.1.3) | 7.1.9, 7.1.15, 7.1.19 |
| hormones coordinate tissues | insulin (fed), glucagon (fasting), epinephrine (activity), cortisol (stress) act on the same few enzymes in opposite directions | 7.1.29 |

### 30.6.2. The Regulator × Enzyme Matrix

Most of the regulation of energy metabolism comes from about fifteen signals acting on about fifteen enzymes. The matrix shows every effect recorded on the pathway cards.

![Regulator × enzyme matrix of mammalian energy metabolism. Columns: the regulated enzymes, grouped by pathway (glycolysis, gluconeogenesis, glycogen, pyruvate oxidation and the citric acid cycle, fatty acids, sterols). Upper block: allosteric effectors; lower block: hormones and the energy-sensing kinase AMPK, with their net effect in the liver through phosphorylation (glucagon and epinephrine via PKA; insulin opposing it). Green "+": activates; red "−": inhibits; empty: no major direct effect. AMP, ATP and glucose 6-phosphate act on muscle phosphorylase, glucose on the liver enzyme; Ca²⁺ acts on phosphorylase through phosphorylase kinase and on the PDH complex through its phosphatase. Read across a row to see that each signal pushes all its targets in one physiological direction: AMP, ADP and Ca²⁺ toward ATP production, ATP, NADH and citrate away from it, insulin toward storage and glucagon toward mobilization](./plots/regulator-matrix.py)

Reading the matrix by rows gives the logic of each signal:

| Signal | Meaning | Turns on | Turns off |
|---|---|---|---|
| AMP, ADP | low energy charge | PFK-1, phosphorylase (muscle), PDH complex, isocitrate DH | FBPase-1 |
| ATP, NADH | high energy charge, reduced matrix | — | PFK-1, pyruvate kinase, PDH complex, citrate synthase, isocitrate DH, α-KG DH |
| $\ce{Ca^2+}$ | muscle contraction, hormone action | phosphorylase kinase, PDH phosphatase, isocitrate DH, α-KG DH | — |
| citrate | full citric acid cycle, carbon to spare | ACC (fat synthesis) | PFK-1, citrate synthase |
| acetyl-CoA | fatty acids are being oxidized | pyruvate carboxylase (gluconeogenesis) | PDH complex, pyruvate kinase (spare pyruvate for glucose) |
| malonyl-CoA | fat is being made | — | CPT1 (no simultaneous oxidation) |
| fructose 2,6-bisphosphate | fed liver (insulin), set by PFK-2/FBPase-2 | PFK-1 | FBPase-1 |
| glucose 6-phosphate | glucose abundant in the cell | glycogen synthase | hexokinase I–III, phosphorylase (muscle) |
| insulin | fed state | glycolysis, glycogen synthesis, PDH, fatty acid and cholesterol synthesis | gluconeogenesis, glycogenolysis, lipolysis |
| glucagon, epinephrine (PKA) | fasting, activity | glycogenolysis, gluconeogenesis, lipolysis | glycolysis (liver), glycogen synthesis, ACC, HMG-CoA reductase |
| **AMP-activated protein kinase** (Definition 29.4.4) | low energy charge in any tissue | catabolism (glucose uptake, fatty acid oxidation through ACC inhibition) | ACC, HMG-CoA reductase, GPAT, glycogen synthase, **mTORC1** |

### 30.6.3. Metabolic States

The same signals, combined, define the metabolic states of the whole body (7.1.29). The table shows the fuel of each tissue; the chart shows the direction of the main fluxes.

| State | Liver | Muscle | Adipose tissue | Brain |
|---|---|---|---|---|
| well fed | takes up glucose (glucokinase), stores glycogen, makes fatty acids and VLDL | GLUT4 glucose uptake, glycogen, protein synthesis | TAG synthesis from chylomicrons and VLDL (LPL) | glucose |
| early fasting | glycogenolysis, then gluconeogenesis from lactate, glycerol, amino acids; ketogenesis begins | fatty acids; releases alanine and glutamine (about 75 g protein per day) | lipolysis (HSL, ATGL) | glucose (about 120 g per day) |
| prolonged starvation | gluconeogenesis (kidney contributes), ketone bodies 5–7 mM | fatty acids, ketone bodies; protein breakdown falls to about 20 g per day | lipolysis until the fat is gone | up to about 60% from ketone bodies |
| untreated type 1 diabetes | gluconeogenesis and ketogenesis without the insulin brake; **ketoacidosis** (Definition 29.5.3) | no GLUT4 uptake; protein breakdown | uncontrolled lipolysis | glucose (hyperglycemia), ketone bodies |
| sprint | — | phosphocreatine (seconds), then glycogen → lactate (1–2 min); **Cori cycle** | — | — |

![Direction of the main fluxes in four metabolic states, relative to the postabsorptive state: well fed (insulin high, glucagon low), early fasting from hours to about day 3 (insulin falling, glucagon rising), prolonged starvation (insulin low, glucagon and cortisol high) and untreated type 1 diabetes (no insulin, glucagon very high). Rows: liver glycolysis, glycogen synthesis and breakdown, gluconeogenesis, fatty acid synthesis, β oxidation, ketogenesis and the urea cycle; adipose lipolysis and triacylglycerol synthesis; muscle glucose uptake and protein breakdown. Green: increased (double arrow, strongly increased); red: decreased; grey: roughly basal. In prolonged starvation the urea cycle and muscle proteolysis slow down as ketone bodies spare glucose and protein; in untreated type 1 diabetes the same mobilizing fluxes run without the restraint of insulin. A qualitative summary of 7.1.19–7.1.22 and 7.1.29, not measured data](./plots/fuel-states.py)

## 30.7. Inhibitors, Drugs and Diseases

### 30.7.1. Inhibitors of Energy Transduction

| Target | Agents | Chapter |
|---|---|---|
| glycolysis | iodoacetate (GAPDH), arsenate (uncouples the GAPDH step), fluoride (enolase) | 7.1.18 |
| PDH complex, citric acid cycle | arsenite (lipoate), fluoroacetate (via fluorocitrate, aconitase), malonate (succinate DH, competitive) | 7.1.20 |
| Complex I / II / III / IV | rotenone, amytal, piericidin A / malonate / antimycin A, myxothiazol / cyanide, azide, CO, $\ce{H2S}$ | 7.1.23 (table in 23.2.4) |
| ATP synthase | oligomycin, venturicidin, DCCD (Fₒ); aurovertin (F₁) | 7.1.23 |
| proton gradient (**uncouplers**, Definition 23.2.5) | DNP, FCCP; valinomycin (K⁺ ionophore); UCP1 physiologically | 7.1.23 |
| ADP/ATP exchange | atractyloside, bongkrekic acid | 7.1.23 |
| photosynthesis | DCMU, atrazine ($\mathrm{Q_B}$ site of PSII); paraquat (diverts electrons from PSI) | 7.1.24 |

The diagnostic logic is the same for all of them: an inhibitor of electron transfer stops both respiration and ATP synthesis, an inhibitor of ATP synthase stops both in coupled mitochondria (respiratory control), and only an uncoupler stops ATP synthesis while respiration speeds up (23.2.3).

### 30.7.2. Enzymes as Drug Targets

| Drug | Target | Mechanism | Use | Chapter |
|---|---|---|---|---|
| statins | HMG-CoA reductase | **competitive inhibition**, nanomolar $K_{\mathrm{I}}$; LDL lowered mostly via SREBP-2 and LDL receptors | hypercholesterolemia | 7.1.26 |
| allopurinol (oxypurinol), febuxostat | xanthine oxidase | substrate analog converted to a tightly bound inhibitor | **gout** | 7.1.28 |
| methotrexate, aminopterin; trimethoprim | dihydrofolate reductase | competitive, picomolar | cancer, rheumatoid arthritis; bacterial infections | 7.1.28 |
| 5-fluorouracil | thymidylate synthase | **suicide inactivator** (FdUMP) | cancer | 7.1.28 |
| hydroxyurea, gemcitabine; mycophenolate; leflunomide | ribonucleotide reductase; IMP DH; DHODH | hydroxyurea scavenges the tyrosyl radical; enzyme inhibitors | cancer; immunosuppression; arthritis | 7.1.28 |
| aspirin; ibuprofen | cyclooxygenase | **irreversible inhibitor** (acetylates Ser); reversible | pain, fever, platelet aggregation | 7.1.12, 7.1.26 |
| penicillin | transpeptidase | irreversible acylation of the active-site Ser | bacterial infections | 7.1.8 |
| HIV protease inhibitors | HIV protease | **transition-state analogs** | HIV infection | 7.1.8 |
| metformin | mitochondrial respiration and hepatocyte redox state; AMPK activation | lowers hepatic gluconeogenesis | **type 2 diabetes** | 7.1.29 |
| sulfonylureas | $\mathrm{K_{ATP}}$ channel of β cells (Definition 29.3.2) | close the channel, insulin secretion | type 2 diabetes, neonatal diabetes | 7.1.29 |
| SGLT2 inhibitors (gliflozins) | renal Na⁺–glucose symporter | glucose excreted in urine | type 2 diabetes | 7.1.13, 7.1.29 |
| fibrates; thiazolidinediones | PPARα; PPARγ | nuclear receptor agonists | dyslipidemia; insulin resistance | 7.1.21, 7.1.29 |
| ouabain, digoxin; omeprazole | Na⁺/K⁺-ATPase; gastric H⁺/K⁺-ATPase | P-type ATPase inhibitors | heart failure; ulcers | 7.1.13 |
| imatinib | BCR–ABL kinase | binds the inactive conformation | chronic myeloid leukemia | 7.1.15 |
| sodium bicarbonate | bicarbonate buffer | base of the buffer pair | metabolic acidosis (Example 2.3.1) | 7.1.2 |

The pattern of inhibition decides the dose–response: a competitive inhibitor (statin, methotrexate) can be overcome by substrate accumulating behind the block, so drugs that must hold a pathway down are designed to bind far more tightly than the substrate, or to react covalently (aspirin, 5-fluorouracil, penicillin) (Theorem 9.4.1, Definition 9.4.3).

### 30.7.3. Inherited and Deficiency Diseases

Most **inborn errors of metabolism** (Definition 22.3.2) follow one rule: the substrate of the missing enzyme accumulates, is diverted into side pathways, and the product is missing.

| Disease | Defect | Consequence | Chapter |
|---|---|---|---|
| **sickle cell anemia** | Hb β Glu6 → Val | deoxy-HbS polymerizes | 7.1.7 |
| lysosomal storage diseases (Tay–Sachs and others) | sphingolipid hydrolases | lipid accumulation in neurons | 7.1.12 |
| cystic fibrosis | CFTR (ABC family) | defective Cl⁻ channel; ΔF508 misfolding | 7.1.6, 7.1.13 |
| G6PD deficiency | glucose 6-phosphate dehydrogenase | hemolysis under oxidative stress (fava beans, drugs); malaria protection | 7.1.18 |
| pyruvate kinase deficiency; galactosemia; hereditary fructose intolerance | PK; galactose enzymes; aldolase B | hemolytic anemia; liver and brain damage; hypoglycemia after fructose | 7.1.18 |
| **glycogen storage diseases** (Definition 19.3.3): von Gierke, Pompe, McArdle | glucose 6-phosphatase; lysosomal α-glucosidase; muscle phosphorylase | fasting hypoglycemia; cardiomyopathy; exercise intolerance | 7.1.19 |
| PDH deficiency | PDH complex | lactic acidosis | 7.1.20 |
| MCAD, LCHAD, CPT and carnitine defects | β oxidation, carnitine shuttle | hypoketotic hypoglycemia in fasting | 7.1.21 |
| methylmalonic acidemia, pernicious anemia | methylmalonyl-CoA mutase, B₁₂ absorption | acidosis, megaloblastic anemia | 7.1.21, 7.1.22 |
| urea cycle defects (OTC deficiency, X-linked) | any of five enzymes, N-acetylglutamate synthase | hyperammonemia | 7.1.22 |
| **phenylketonuria**, alkaptonuria, **maple syrup urine disease** | Phe hydroxylase; homogentisate dioxygenase; branched-chain α-keto acid DH | intellectual disability unless treated by diet; dark urine; ketoaciduria | 7.1.22 |
| LHON, MERRF, MELAS, Leigh syndrome | mitochondrial DNA (heteroplasmy, Definition 23.5.2) | neuromuscular disease | 7.1.23 |
| familial hypercholesterolemia | LDL receptor (apoB-100, PCSK9) | high LDL, early atherosclerosis | 7.1.26 |
| porphyrias; lead poisoning | heme synthesis enzymes | accumulated precursors | 7.1.27 |
| **Lesch–Nyhan syndrome**, ADA-SCID, orotic aciduria, gout | HGPRT; adenosine deaminase; UMP synthase; urate excess | self-mutilation and hyperuricemia; immunodeficiency (dATP ⊣ RNR); anemia; arthritis | 7.1.28 |
| type 1 and type 2 diabetes | insulin secretion; insulin action and β-cell failure | hyperglycemia, ketoacidosis (type 1), complications | 7.1.29 |

Vitamin deficiencies fail at the coenzyme (table in 17.2.1): thiamine (beriberi, Wernicke–Korsakoff: pyruvate and α-KG dehydrogenases), niacin (pellagra: all NAD-dependent dehydrogenases), vitamin C (scurvy: collagen hydroxylases), cobalamin and folate (megaloblastic anemia: methionine synthase, thymidylate synthesis).

## Summary

- Structure (30.1): the four noncovalent interactions, each a few kJ mol⁻¹, and the chemistry of side chains, glycosidic bonds, bases and amphipathic lipids decide every structure of Part I; binding, catalysis, transport and signaling share one language of midpoints ($K_{\mathrm{d}}$, $K_{\mathrm{M}}$, $K_{0.5}$) and steepness (Hill coefficient, response coefficient).
- Map (30.2): catabolism converges on acetyl-CoA and $\ce{O2}$, anabolism diverges from the same precursors; three hubs (glucose 6-phosphate, pyruvate, acetyl-CoA) and two currencies (ATP and NAD(P)H) connect them; animals cannot make glucose from acetyl-CoA.
- Cards and pairs (30.3–30.4): each pathway is controlled at its committed, far-from-equilibrium steps; every opposing pair differs at those steps in enzyme, carrier, coenzyme or compartment and is regulated reciprocally.
- Ledger (30.5): glucose 30–32 ATP, palmitate 106, acetyl-CoA 10, NADH 2.5; biosynthesis costs ATP and NADPH in amounts fixed by stoichiometry.
- Regulation (30.6): about fifteen signals on about fifteen enzymes (Figure: regulator × enzyme matrix), integrated by insulin, glucagon, epinephrine, cortisol and AMPK into the fed, fasting, starving and diabetic states.
- Medicine (30.7): inhibitors of energy transduction reveal the coupling of oxidation and phosphorylation; drugs are enzyme inhibitors whose kinetic type decides how they work; inherited diseases accumulate the substrate of the missing enzyme.

## Questions

1. Describe the fuel metabolism of liver, muscle, adipose tissue and brain on the third day of a total fast, and explain why the concentration of ketone bodies rises.

   **Answer** By the third day liver glycogen is exhausted and insulin is low, glucagon high. Adipose tissue releases fatty acids (PKA activates HSL and perilipin), which muscle and liver oxidize. The liver makes glucose from lactate, glycerol and amino acids from muscle protein (about 75 g per day, carried as alanine and glutamine): glucagon lowers fructose 2,6-bisphosphate, so FBPase-1 is active and PFK-1 inactive, pyruvate kinase L is phosphorylated and inactive, PEPCK is induced, and the acetyl-CoA from β oxidation activates pyruvate carboxylase while inhibiting the PDH complex. Oxaloacetate is drawn off into gluconeogenesis, so acetyl-CoA from β oxidation cannot enter the citric acid cycle at the usual rate and is converted to acetoacetate and β-hydroxybutyrate, which the liver cannot use (it lacks SCOT) and exports. The brain still uses mainly glucose at this stage, but ketone bodies are rising toward the 5–7 mM of prolonged starvation, when they supply up to 60% of its energy and allow protein breakdown to fall to about 20 g per day (29.3.4).

2. Compare the sources of ATP in a 100 m sprint and in a marathon, and explain which signals switch them on.

   **Answer** A sprint lasts seconds: the ATP present and phosphocreatine (creatine kinase keeps [ATP] nearly constant) cover the first seconds, then glycogen is broken down to lactate in fast-twitch fibers. Contraction releases $\ce{Ca^2+}$, which activates phosphorylase kinase; ADP and AMP rise (adenylate kinase amplifies AMP), activating phosphorylase *b* and PFK-1; epinephrine adds PKA activation. Glycolysis from glycogen yields 3 ATP per residue, fast but small, and the lactate is reconverted to glucose in the liver later (Cori cycle). A marathon lasts hours: the power output is lower, so oxidative phosphorylation in slow-twitch fibers can supply it, with muscle glycogen, blood glucose (from liver glycogenolysis and gluconeogenesis) and, increasingly, fatty acids from adipose tissue (epinephrine-driven lipolysis); $\ce{Ca^2+}$ also activates the PDH phosphatase and the matrix dehydrogenases, and ADP drives respiration by respiratory control. When muscle glycogen runs out the runner must rely on fat, whose oxidation supports less power per unit of oxygen, and slows down.

3. A patient with untreated type 1 diabetes has hyperglycemia, ketoacidosis and weight loss despite eating. Trace each sign to the pathways in the regulator matrix and the pathway cards.

   **Answer** Without insulin, glucagon acts unopposed. In muscle and adipose tissue GLUT4 is not recruited, so glucose is not taken up; in liver, fructose 2,6-bisphosphate stays low, PFK-1 is off and FBPase-1 on, PEPCK and glucose 6-phosphatase are induced, glycogen synthase is phosphorylated (off) and phosphorylase is on: the liver makes and exports glucose although blood glucose is already high, and glucose is lost in urine. In adipose tissue, lipolysis is not restrained (no PDE3B activation, PKA keeps HSL active), so fatty acids flood the liver; ACC is inactive, malonyl-CoA is low, CPT1 is uninhibited, and β oxidation runs at full rate while oxaloacetate is withdrawn for gluconeogenesis, so ketone body synthesis exceeds use and the buffer capacity of bicarbonate, giving ketoacidosis (Definition 29.5.3). Muscle protein is broken down for gluconeogenesis, and fat and protein stores shrink: weight loss. Insulin reverses all of these switches at once.

4. Why can animals not make glucose from palmitate, while they can from glycerol and from propionate? How do germinating oilseeds solve the problem?

   **Answer** Palmitate is degraded entirely to acetyl-CoA. The PDH reaction is irreversible, so acetyl-CoA cannot become pyruvate, and in the citric acid cycle two carbons enter as acetyl and two leave as $\ce{CO2}$ before oxaloacetate is regenerated, so there is no net gain of oxaloacetate for PEPCK. Glycerol, by contrast, is phosphorylated and oxidized to dihydroxyacetone phosphate, a glycolytic intermediate, and propionyl-CoA from odd-chain fatty acids is carboxylated (biotin) and rearranged (coenzyme B₁₂) to succinyl-CoA, which adds carbon to the cycle and can leave as oxaloacetate (Definition 21.4.1). Oilseeds use the glyoxylate cycle (Definition 20.5.1): isocitrate lyase and malate synthase bypass the two decarboxylations, so two acetyl-CoA give one succinate, which becomes oxaloacetate and then glucose.

5. Isolated mitochondria oxidizing succinate in the presence of ADP and $\mathrm{P_i}$ are treated with (a) cyanide, (b) oligomycin, (c) oligomycin followed by DNP. Predict the rates of $\ce{O2}$ consumption and of ATP synthesis, and explain.

   **Answer** (a) Cyanide binds heme $a_3$ of Complex IV: electron flow to $\ce{O2}$ stops, so does proton pumping, and ATP synthesis stops; all carriers upstream become reduced. (b) Oligomycin blocks the Fₒ proton channel: ATP synthesis stops, the proton-motive force builds up until pumping is no longer possible against it, and $\ce{O2}$ consumption falls to the leak rate, the experimental proof that oxidation and phosphorylation are obligately coupled (respiratory control, Definition 23.2.2). (c) DNP carries protons back across the membrane, dissipating the gradient; respiration resumes at a high rate, limited only by the respiratory chain, but ATP is still not made, and the energy is released as heat (as with UCP1 in brown fat).

6. Statins, methotrexate and 5-fluorouracil all inhibit enzymes of biosynthesis. How does their mode of inhibition differ, and why does it matter in therapy?

   **Answer** Statins are competitive inhibitors of HMG-CoA reductase with nanomolar $K_{\mathrm{I}}$, about a thousand times tighter than the substrate; inhibition can in principle be overcome by HMG-CoA accumulating, and the cell responds by inducing more reductase via SREBP-2, so synthesis falls less than the direct inhibition would suggest, but the same response induces LDL receptors and lowers plasma LDL (26.5.7). Methotrexate is a folate analog that binds DHFR competitively with picomolar dissociation constants, so tightly that it behaves almost as an irreversible inhibitor and depletes tetrahydrofolate, stopping thymidylate and purine synthesis in rapidly dividing cells. 5-Fluorouracil is converted to FdUMP, which forms a covalent complex with thymidylate synthase and methylene-THF: a suicide inactivator (Definition 9.4.3), whose effect lasts until new enzyme is made. Covalent and very tight inhibitors give a durable block at low concentration; competitive inhibitors are reversible and their effect depends on the substrate level, which matters for dosing and for side effects.

7. (Open question) Using the energy ledger, explain why proliferating cancer cells and activated lymphocytes take up glucose at a high rate and ferment much of it to lactate even in the presence of oxygen.

   **Answer** A key point: by ATP alone the choice is irrational, since fermentation gives 2 ATP per glucose against 30–32 for oxidation. But a dividing cell needs carbon, NADPH and precursors as much as ATP: making one palmitate costs 14 NADPH and 8 acetyl-CoA, a nucleotide needs ribose 5-phosphate, glycine, aspartate and one-carbon units, and these come from glycolytic intermediates (3-phosphoglycerate for serine and glycine), the pentose phosphate pathway and citrate exported from the mitochondria. A high glycolytic flux keeps these intermediates abundant; reducing pyruvate to lactate regenerates the $\ce{NAD+}$ needed to sustain that flux without being limited by respiratory capacity, and HIF-1 and the PKM2 isozyme (7.1.18) favor this mode. The Warburg effect (Definition 18.4.2) is therefore better seen as a supply strategy for biosynthesis than as a defect of respiration; FDG-PET exploits the resulting glucose uptake to image tumors.
