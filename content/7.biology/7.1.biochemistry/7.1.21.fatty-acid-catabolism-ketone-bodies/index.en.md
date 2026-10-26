---
title: Fatty Acid Catabolism and Ketone Bodies
description: Triacylglycerols as fuel; digestion, chylomicrons and lipoprotein lipase; hormonal mobilization by ATGL, HSL and perilipin; activation of fatty acids and the carnitine shuttle; the four steps of β oxidation, its stoichiometry and ATP yield; unsaturated and odd-chain fatty acids, propionyl-CoA and coenzyme B12; regulation by malonyl-CoA and PPARα, MCAD deficiency; peroxisomal β oxidation, α and ω oxidation; formation and use of ketone bodies, ketosis and ketoacidosis; the pathway cards.
---

Fatty acids are the largest energy store of animals. Triacylglycerols supply 40% or more of the daily energy of people in industrialized countries, more than half of the needs of liver, heart and resting skeletal muscle, and almost all the energy of hibernating animals and migrating birds; vascular plants use them during germination. This chapter follows a fatty acid from the gut or the adipocyte to acetyl-CoA. The chemistry repeats what the citric acid cycle taught ([7.1.20](/7.1.20)): a carboxylic acid is activated as a **thioester** of CoA, and the inert $\ce{-CH2-CH2-}$ chain is broken after a carbonyl has been created next to it by the recurring sequence dehydrogenation–hydration–dehydrogenation ([7.1.17](/7.1.17#sec-17.1.3)), followed by a thiolytic cleavage, a reverse **Claisen condensation**. The regulation, by malonyl-CoA at the entry into mitochondria, keeps β oxidation and fatty acid synthesis ([7.1.26](/7.1.26)) apart. When the liver oxidizes more fat than it needs, it converts the surplus acetyl-CoA to ketone bodies, a water-soluble fuel that even the brain can use in starvation, and that becomes dangerous in uncontrolled diabetes ([7.1.29](/7.1.29)).

## 21.1. Digestion, Mobilization and Transport of Fats

### 21.1.1. Fat as Fuel

The properties of **triacylglycerols** that make them good stores ([7.1.12](/7.1.12#sec-12.3.2)) create problems for their use.

| Property | Advantage for storage | Problem for use |
|---|---|---|
| highly reduced alkyl chains | about 38 kJ g⁻¹ on complete oxidation, more than twice carbohydrate or protein (about 17 kJ g⁻¹) | — |
| insoluble in water | stored anhydrous in lipid droplets; no effect on **osmolarity**; glycogen carries about twice its mass of water | must be emulsified for digestion and carried in the blood by proteins |
| chemically inert | can be stored in large amounts without side reactions | the C–C bonds must be activated before they can be broken |

Cells obtain fatty acids from the diet, from lipid droplets of adipose tissue, from synthesis in the liver (from excess carbohydrate, exported as VLDL) and, in starvation, from autophagy of their own membranes.

### 21.1.2. Digestion and Chylomicrons

In the small intestine, **bile salts**, amphipathic derivatives of cholesterol made in the liver and stored in the gallbladder (taurocholate, glycocholate, [7.1.12](/7.1.12)), emulsify dietary fat into mixed **micelles** ([6.3.19](/6.3.19)), which multiplies the surface accessible to pancreatic lipase. The lipase (with its cofactor colipase) hydrolyzes triacylglycerols to 2-monoacylglycerols and fatty acids, which enter the enterocytes, are re-esterified to triacylglycerols, and are packaged with cholesterol, phospholipids and apolipoproteins into large lipoprotein particles.

**Definition 21.1.1 (Chylomicron)** A **chylomicron** is the largest and least dense lipoprotein particle (diameter about 100–1000 nm, more than 85% triacylglycerol), formed in enterocytes around apolipoprotein B-48, which carries dietary lipids through the lymph and the blood to the tissues.

Chylomicrons enter the lymph (which turns milky after a fatty meal) and then the blood, where they acquire apolipoprotein C-II from HDL.

**Definition 21.1.2 (Lipoprotein Lipase)** **Lipoprotein lipase** is the extracellular lipase bound to the luminal surface of the capillary endothelium of muscle, heart and adipose tissue that hydrolyzes the triacylglycerols of chylomicrons and VLDL to fatty acids and 2-monoacylglycerol; it is activated by apoC-II.

Muscle oxidizes the fatty acids released, adipose tissue re-esterifies them. The cholesterol-rich chylomicron remnants are taken up by the liver by receptor-mediated endocytosis. The lipoproteins and their metabolism are treated with lipid synthesis ([7.1.26](/7.1.26)). Deficiency of lipoprotein lipase or apoC-II causes familial chylomicronemia, with triacylglycerols in the plasma above 10 g L⁻¹ and attacks of pancreatitis.

### 21.1.3. Mobilization of Stored Fat

In adipocytes, triacylglycerols and sterol esters form lipid droplets covered by a monolayer of phospholipids and by perilipins, proteins that restrict the access of lipases. When blood glucose falls or in stress, epinephrine (through β-adrenergic receptors) and in some species glucagon raise cAMP and activate PKA ([7.1.14](/7.1.14#sec-14.2.2)). PKA phosphorylates perilipin 1, which releases its partner CGI-58 (comparative gene identification-58); CGI-58 activates adipose triglyceride lipase (ATGL), which removes the first fatty acid. PKA also phosphorylates hormone-sensitive lipase, which moves to the droplet surface.

**Definition 21.1.3 (Hormone-Sensitive Lipase)** **Hormone-sensitive lipase** (HSL) is the cytosolic lipase of adipocytes and steroidogenic cells that hydrolyzes mainly diacylglycerols (and cholesteryl esters) and is activated by PKA phosphorylation in response to epinephrine, so that, with ATGL and monoacylglycerol lipase, it releases fatty acids and glycerol from stored triacylglycerol.

Insulin opposes lipolysis by activating phosphodiesterase 3B (through PKB), which lowers cAMP; this is one of the most sensitive actions of insulin, effective at concentrations below those needed for glucose uptake.

![Hormonal mobilization of stored triacylglycerol in an adipocyte (SBGN process description). Epinephrine raises cAMP and activates PKA, which phosphorylates perilipin 1 on the lipid droplet and hormone-sensitive lipase (HSL). Phosphorylated perilipin releases CGI-58, which activates adipose triglyceride lipase (ATGL). ATGL hydrolyzes triacylglycerol (TAG) to diacylglycerol (DAG), phosphorylated HSL hydrolyzes DAG to monoacylglycerol (MAG), and monoacylglycerol lipase (MGL) releases glycerol; each step frees a fatty acid (FA). Insulin activates phosphodiesterase 3B (PDE3B), which lowers cAMP. Fatty acids leave the cell bound to serum albumin; glycerol is taken up by the liver](./plots/lipid-mobilization.py)

The free fatty acids leave the adipocyte and bind to serum albumin ($M_{\mathrm{r}}$ about 66 500, half of the plasma protein), which has seven high-affinity sites for fatty acids and also carries many drugs. Albumin delivers them to muscle, heart and renal cortex, which take them up with membrane transporters (CD36 and others). The glycerol, about 5% of the energy of a triacylglycerol, is phosphorylated by glycerol kinase in the liver, oxidized to dihydroxyacetone phosphate and used for gluconeogenesis or glycolysis ([7.1.19](/7.1.19#sec-19.1.5)).

## 21.2. Activation and Transport into Mitochondria

### 21.2.1. Activation

The enzymes of β oxidation are in the mitochondrial matrix (Kennedy and Lehninger, 1948). Before entering, a fatty acid is activated by a fatty acyl-CoA synthetase (fatty acid thiokinase) of the outer mitochondrial membrane (isozymes for short, medium, long and very long chains), in two steps through an enzyme-bound acyl adenylate, a mixed anhydride:

$$
\begin{aligned}
\text{R–COO}^- + \ce{ATP} &\to \text{R–CO–AMP} + \mathrm{PP_i},\\
\text{R–CO–AMP} + \text{CoA–SH} &\to \text{R–CO–S–CoA} + \ce{AMP},\\
\mathrm{PP_i} + \ce{H2O} &\to 2\,\mathrm{P_i};
\end{aligned}
\qquad
\text{overall } \Delta_{\mathrm{r}}G'^{\circ} = -34\,\mathrm{kJ\,mol^{-1}}. \tag{21.1}
$$
Two phosphoanhydride bonds are consumed to make one thioester, which is why activation costs the equivalent of two ATP. Acyl adenylates are the general way biochemistry activates carboxyl groups (aminoacyl-tRNA synthesis is the same reaction, [7.2](/7.2)). Fatty acyl-CoA in the cytosol can be used to make membrane lipids and triacylglycerols, or be oxidized.

### 21.2.2. The Carnitine Shuttle

Short- and medium-chain fatty acids (12 carbons or fewer) cross the inner mitochondrial membrane and are activated in the matrix. Long-chain acyl-CoA cannot cross, and CoA itself is kept in two separate pools.

**Definition 21.2.1 (Carnitine Shuttle)** The **carnitine shuttle** carries long-chain fatty acyl groups into the mitochondrial matrix: carnitine palmitoyltransferase 1 (CPT1) of the outer membrane transfers the acyl group from CoA to carnitine; the carnitine/acylcarnitine translocase of the inner membrane exchanges acylcarnitine for free carnitine; and carnitine palmitoyltransferase 2 (CPT2) on the matrix side of the inner membrane transfers the acyl group back to mitochondrial CoA.

![Activation of a long-chain fatty acid and the carnitine shuttle. On the outer mitochondrial membrane, acyl-CoA synthetase forms fatty acyl-CoA (with AMP and pyrophosphate, which is hydrolyzed). CPT1, in the outer membrane, transfers the acyl group to carnitine, releasing cytosolic CoA; malonyl-CoA, the first intermediate of fatty acid synthesis, inhibits CPT1. Acylcarnitine crosses the inner membrane on the carnitine/acylcarnitine translocase in exchange for carnitine. CPT2 on the matrix face transfers the acyl group to mitochondrial CoA, and the fatty acyl-CoA enters β oxidation](./plots/carnitine-shuttle.py)

Conversion to the carnitine ester commits the acyl group to oxidation, and the CPT1 step is rate-limiting for the oxidation of long-chain fatty acids and the site of its main regulation (21.5.1). Carnitine (β-hydroxy-γ-trimethylammonium butyrate) is made from Lys and Met in liver and kidney and obtained from meat. Inherited defects of CPT1 (liver), CPT2 (muscle cramps and myoglobinuria after prolonged exercise or fasting) or the translocase, and carnitine deficiency, impair fat oxidation; in the liver forms the result is hypoketotic hypoglycemia during fasting, because neither ketone bodies nor the ATP for gluconeogenesis can be made from fat.

## 21.3. β Oxidation

### 21.3.1. Knoop's Experiment

In 1904 Franz Knoop fed dogs fatty acids whose ω carbon carried a phenyl group, a label the animal could not remove. Fatty acids with an even number of carbons gave phenylacetate (excreted as phenylaceturate), those with an odd number benzoate (excreted as hippurate). Knoop concluded that fatty acids are degraded by oxidation at the β carbon and removal of two carbons at a time, β oxidation; the experiment was one of the first uses of a synthetic label to trace a metabolic pathway, decades before isotopes.

### 21.3.2. Four Steps

**Definition 21.3.1 (β Oxidation)** **β oxidation** is the pathway that degrades a fatty acyl-CoA by repeated cycles of four reactions, each removing the two carboxyl-terminal carbons as acetyl-CoA: dehydrogenation of C-2 and C-3 by acyl-CoA dehydrogenase (FAD) to a trans-Δ² double bond; hydration to L-3-hydroxyacyl-CoA by enoyl-CoA hydratase; dehydrogenation to 3-ketoacyl-CoA by L-3-hydroxyacyl-CoA dehydrogenase ($\ce{NAD+}$); and thiolysis by thiolase (acyl-CoA acetyltransferase), which yields acetyl-CoA and an acyl-CoA shortened by two carbons.

```smiles
CCCCCCCCCCCCCC(=O)CC(=O)SC 3-ketoacyl-SCoA
```

(The 3-ketoacyl thioester of palmitate, with the CoA abbreviated to a methyl thioester: the carbonyl at C-3, the β carbon, makes the C-2–C-3 bond the weak link.)

1. Acyl-CoA dehydrogenases are **flavoproteins** with chain-length–specific isozymes: very-long-chain (VLCAD, 12–18 carbons, bound to the inner membrane), medium-chain (MCAD, 4–14) and short-chain (SCAD, 4–8), the last two soluble in the matrix. The reduced FAD passes its electrons to the electron-transferring flavoprotein (ETF), then to ETF:ubiquinone oxidoreductase and ubiquinone ([7.1.23](/7.1.23)), about 1.5 ATP per pair. The reaction resembles succinate dehydrogenase: an α–β double bond is introduced in a carboxylic acid derivative with FAD as acceptor, because the potential of a saturated C–C bond is too positive for $\ce{NAD+}$ ([7.1.17](/7.1.17#sec-17.1.3)). The double bond is trans, unlike the cis bonds of natural unsaturated fatty acids.
2. Enoyl-CoA hydratase adds water across the trans double bond; the reaction is **stereospecific**, giving only the L stereoisomer of 3-hydroxyacyl-CoA, as fumarase gives L-malate.
3. L-3-Hydroxyacyl-CoA dehydrogenase, absolutely specific for the L isomer, oxidizes the hydroxyl to a ketone with $\ce{NAD+}$ (as malate dehydrogenase does).
4. Thiolase attacks the keto carbon (C-3) with the thiol of CoA; the C-2–C-3 bond breaks with acetyl-CoA as the leaving carbanion (stabilized as the enolate of a thioester), and the rest of the chain leaves as a new acyl-CoA. Thiolysis is a reverse Claisen condensation.

**Definition 21.3.2 (Trifunctional Protein)** The mitochondrial **trifunctional protein** (TFP) is an $\alpha_4\beta_4$ complex of the inner membrane that catalyzes steps 2–4 of β oxidation for acyl chains of 12 carbons or more: each α subunit carries the enoyl-CoA hydratase and long-chain 3-hydroxyacyl-CoA dehydrogenase activities, each β subunit the thiolase; the intermediates are channeled between the active sites.

Chains of 12 carbons or fewer are handled by soluble matrix enzymes. The four steps are the same, with the same chemical logic, as the conversion of succinate to oxaloacetate in the citric acid cycle and as the oxidation of the branched-chain amino acids ([7.1.22](/7.1.22)), almost certainly products of gene duplication.

![One turn of mitochondrial β oxidation. Acyl-CoA dehydrogenase introduces a trans double bond between C-2 and C-3, passing two electrons through FAD and the electron-transferring flavoprotein (ETF) to ubiquinone (Q); enoyl-CoA hydratase adds water to give L-3-hydroxyacyl-CoA; L-3-hydroxyacyl-CoA dehydrogenase oxidizes it with NAD⁺ to 3-ketoacyl-CoA; thiolase cleaves it with CoA to acetyl-CoA and an acyl-CoA two carbons shorter, which starts the next turn. A chain of n carbons makes n/2 − 1 turns; for long chains, steps 2–4 are catalyzed by the trifunctional protein of the inner membrane](./plots/beta-oxidation.py)

### 21.3.3. Stoichiometry and Yield

One pass, for palmitoyl-CoA:

$$
\text{palmitoyl-CoA} + \ce{CoA} + \text{FAD} + \ce{NAD+} + \ce{H2O} \to \text{myristoyl-CoA} + \text{acetyl-CoA} + \ce{FADH2} + \ce{NADH} + \ce{H+};
$$
seven passes convert palmitoyl-CoA (C16) to eight acetyl-CoA:

$$
\text{palmitoyl-CoA} + 7\,\ce{CoA} + 7\,\text{FAD} + 7\,\ce{NAD+} + 7\,\ce{H2O} \to 8\,\text{acetyl-CoA} + 7\,\ce{FADH2} + 7\,\ce{NADH} + 7\,\ce{H+}. \tag{21.2}
$$

**Formula 21.3.1 (ATP Yield of a Saturated Fatty Acid)** For a saturated fatty acid with an even number $n$ of carbons, oxidized completely to $\ce{CO2}$ with 1.5 ATP per $\ce{FADH2}$, 2.5 per NADH and 10 per acetyl-CoA in the citric acid cycle ([7.1.20](/7.1.20#sec-20.2.5)), and 2 ATP equivalents for activation,

$$
\mathrm{ATP}(n) = \left(\frac{n}{2} - 1\right)(1.5 + 2.5) + \frac{n}{2}\cdot 10 - 2 = 7n - 6. \tag{21.3}
$$

For palmitate, 28 ATP come from β oxidation and 80 from the citric acid cycle, 108 per palmitoyl-CoA and 106 per palmitate:

$$
\text{palmitoyl-CoA} + 23\,\ce{O2} + 108\,\mathrm{P_i} + 108\,\ce{ADP} \to \ce{CoA} + 108\,\ce{ATP} + 16\,\ce{CO2} + 23\,\ce{H2O}.
$$
The standard Gibbs energy of oxidation of palmitate is about $-9800\,\mathrm{kJ\,mol^{-1}}$, of which $106 \times 30.5 = 3230\,\mathrm{kJ\,mol^{-1}}$ (33%) is conserved in standard terms and more than 60% with the cellular phosphorylation potential, about the same as for glucose. Per carbon, a fatty acid gives more ATP than glucose (106/16 = 6.6 against 32/6 = 5.3), because its carbons are more reduced ([7.1.16](/7.1.16#sec-16.4.2)); per gram, more than twice as much (0.41 against 0.18 mol ATP per mol per g), and about seven times as much as hydrated glycogen.

![ATP from the complete oxidation of saturated even-chain fatty acids (Formula 21.3.1, ATP = 7n − 6), compared with glucose (32 ATP). A: ATP per molecule (palmitate, n = 16: 106). B: ATP per carbon atom, rising toward 7 as the cost of activation is spread over more carbons. C: ATP per gram of fuel; the dotted line is glycogen stored with about 2 g of water per g](./plots/fatty-acid-yield.py)

Each pair of electrons that reaches $\ce{O2}$ forms one water. Hibernating bears oxidize only fat for months; the metabolic water replaces the water lost in breathing, the glycerol supplies gluconeogenesis, and urea nitrogen is recycled into amino acids, so that the bear neither eats, drinks nor urinates. The fat of a camel's hump supplies water in the same way (Question 3).

## 21.4. Unsaturated and Odd-Chain Fatty Acids

### 21.4.1. Unsaturated Fatty Acids

Most natural unsaturated fatty acids have cis double bonds at odd positions (oleate cis-Δ⁹, linoleate cis-Δ⁹,¹², [7.1.12](/7.1.12#sec-12.2.1)), which the hydratase cannot use. Two auxiliary enzymes solve the problem.

- After three turns, oleoyl-CoA becomes cis-Δ³-dodecenoyl-CoA. Δ³,Δ²-Enoyl-CoA isomerase moves the double bond to the trans-Δ² position, the normal substrate of the hydratase, and β oxidation continues. Oleate gives 9 acetyl-CoA like stearate, but one $\ce{FADH2}$ fewer (1.5 ATP less), because the acyl-CoA dehydrogenase is bypassed once.
- Linoleoyl-CoA, after three turns, the isomerase and one more turn, gives cis-Δ⁴-decenoyl-CoA, which acyl-CoA dehydrogenase converts to the conjugated trans-Δ²,cis-Δ⁴-dienoyl-CoA. 2,4-Dienoyl-CoA reductase reduces it with NADPH to trans-Δ³-enoyl-CoA, which the isomerase converts to trans-Δ². Each double bond at an even position thus costs an NADPH; each double bond in general costs about 1.5 ATP.

### 21.4.2. Odd-Chain Fatty Acids and Propionyl-CoA

Fatty acids with an odd number of carbons, common in plants, marine organisms and ruminant fat (from rumen bacteria, which also produce large amounts of propionate), are oxidized normally until the last thiolysis gives acetyl-CoA and propionyl-CoA. Propionyl-CoA, which also comes from Ile, Val, Met and Thr ([7.1.22](/7.1.22)) and from branched fatty acids, is converted to succinyl-CoA in three steps:

$$
\text{propionyl-CoA} \xrightarrow[\text{biotin; ATP, } \ce{HCO3-}]{\text{propionyl-CoA carboxylase}} \text{D-methylmalonyl-CoA} \xrightarrow{\text{epimerase}} \text{L-methylmalonyl-CoA} \xrightarrow[\text{coenzyme } \mathrm{B_{12}}]{\text{mutase}} \text{succinyl-CoA}.
$$

**Definition 21.4.1 (Methylmalonyl-CoA Mutase)** **Methylmalonyl-CoA mutase** is the mitochondrial enzyme that rearranges L-methylmalonyl-CoA to succinyl-CoA by exchanging the –CO–S-CoA group on C-2 with a hydrogen atom on the adjacent methyl carbon; it requires 5′-deoxyadenosylcobalamin (coenzyme $\mathrm{B_{12}}$).

The mechanism is a **radical** rearrangement ([7.1.17](/7.1.17#sec-17.2.5)): homolysis of the weak Co–C bond of the coenzyme gives a 5′-deoxyadenosyl radical, which abstracts a hydrogen atom from the methyl group of the substrate; the substrate radical rearranges, and the hydrogen is returned to the product from the 5′-deoxyadenosine, never exchanging with the solvent. **Cobalamin** was the last vitamin to be isolated (1948) and has the most complex structure; Dorothy Crowfoot Hodgkin solved it by X-ray crystallography in 1956 (Nobel Prize in Chemistry 1964). It is made only by some bacteria and archaea; humans need about 2.4 µg a day from animal foods and absorb it in the ileum bound to intrinsic factor, a glycoprotein secreted by the stomach. In pernicious anemia, autoimmune destruction of the cells that make intrinsic factor prevents absorption; methylmalonyl-CoA accumulates (the methylmalonic acid in urine is a diagnostic marker), and the deficient methionine synthase causes megaloblastic anemia and neurological damage ([7.1.22](/7.1.22)).

Inherited deficiency of propionyl-CoA carboxylase (about 1 in 100 000 births) causes propionic acidemia, of the mutase or of $\mathrm{B_{12}}$ metabolism methylmalonic acidemia: propionyl-CoA accumulates, traps CoA, and is released as propionate and other organic acids that acidify the blood. Treatment restricts protein (the main source of propionyl-CoA), supplies carnitine (which carries propionyl groups out as propionylcarnitine) and, for some patients, biotin or vitamin $\mathrm{B_{12}}$.

![Auxiliary reactions of β oxidation. A: unsaturated fatty acids. Oleoyl-CoA (18:1, cis-Δ⁹) gives, after three turns, cis-Δ³-dodecenoyl-CoA, which enoyl-CoA isomerase converts to the trans-Δ² intermediate of β oxidation. Linoleoyl-CoA (18:2, cis-Δ⁹,¹²) gives, after three turns, the isomerase, a fourth turn and acyl-CoA dehydrogenase, a trans-Δ²,cis-Δ⁴-dienoyl-CoA; 2,4-dienoyl-CoA reductase reduces it with NADPH to trans-Δ³-decenoyl-CoA, and the isomerase gives trans-Δ². B: odd-chain fatty acids. The final thiolysis gives propionyl-CoA, which is carboxylated by the biotin enzyme propionyl-CoA carboxylase to D-methylmalonyl-CoA, epimerized to L-methylmalonyl-CoA and rearranged by methylmalonyl-CoA mutase (coenzyme B₁₂) to succinyl-CoA](./plots/odd-unsaturated.py)

Propionyl-CoA is the only part of a fatty acid that can become glucose in animals: succinyl-CoA is converted to oxaloacetate and enters gluconeogenesis ([7.1.19](/7.1.19#sec-19.1.5)). In ruminants, propionate from the rumen is the main precursor of blood glucose.

## 21.5. Regulation and Other Oxidation Pathways

### 21.5.1. Regulation

Fatty acyl-CoA in the cytosol of a hepatocyte can be oxidized in mitochondria or esterified to triacylglycerols and phospholipids; the choice is made at CPT1. Malonyl-CoA, the product of acetyl-CoA carboxylase (ACC) and the first intermediate of fatty acid synthesis, inhibits CPT1. When glucose is abundant and insulin high, ACC is active (dephosphorylated), malonyl-CoA rises, and fatty acids made from glucose are not oxidized in the same cell: a reciprocal regulation of two opposing pathways in two compartments, which prevents a futile cycle. When glucose is scarce, glucagon (PKA) and low energy (AMP-activated protein kinase, AMPK) phosphorylate and inactivate ACC; malonyl-CoA falls, CPT1 is released and fatty acids are oxidized, while glucagon also mobilizes them from adipose tissue. In muscle, which does not synthesize fat, the isozyme ACC2 bound to mitochondria makes malonyl-CoA only to regulate CPT1, and malonyl-CoA decarboxylase removes it. Within the matrix, a high $[\mathrm{NADH}]/[\ce{NAD+}]$ inhibits 3-hydroxyacyl-CoA dehydrogenase and a high [acetyl-CoA] inhibits thiolase.

On a longer time scale, the nuclear receptor PPARα, activated by fatty acids and their derivatives (and by fibrate drugs), induces the transporters, CPT1 and CPT2, the acyl-CoA dehydrogenases and the enzymes of ketogenesis in liver, heart and muscle during fasting, at birth (when the heart switches from glucose and lactate to fat) and with endurance training ([7.1.29](/7.1.29)).

### 21.5.2. Inherited Defects

More than 20 inherited defects of fatty acid transport and oxidation are known. The most common is MCAD deficiency: in northern Europeans about 1 in 40 is a carrier of the common mutation and about 1 in 10 000 to 20 000 newborns is affected. Patients cannot oxidize fatty acids of 6 to 12 carbons; during fasting or infection they develop hypoketotic hypoglycemia, fatty liver, vomiting and coma, with octanoylcarnitine in the blood, and before diagnosis was common 25–60% died in early childhood. Newborn screening by tandem mass spectrometry of acylcarnitines detects the disease, and avoiding long fasts makes the prognosis good. Defects of the long-chain hydroxyacyl-CoA dehydrogenase activity of the trifunctional protein (LCHAD) cause cardiomyopathy and myopathy, and a fetus with the defect can cause acute fatty liver in the heterozygous mother during pregnancy.

### 21.5.3. Peroxisomal β Oxidation

Peroxisomes of animals and plants (and the glyoxysomes of germinating seeds) also carry out β oxidation, with three differences:

- The first oxidation is catalyzed by acyl-CoA oxidase, a flavoprotein that passes the electrons directly to $\ce{O2}$, forming $\ce{H2O2}$, which catalase destroys; the energy of this step is released as heat, not conserved as ATP. The NADH of the second oxidation and the acetyl-CoA are exported.
- In animals, peroxisomes oxidize very-long-chain fatty acids (C24, C26), branched fatty acids (pristanate) and the side chains of bile acid precursors, shortening them to medium chains that are completed in mitochondria; they have no citric acid cycle. Long-chain fatty acids are oxidized in mitochondria.
- In plants, peroxisomes and glyoxysomes are the main site of β oxidation; the acetyl-CoA from seed oils feeds the glyoxylate cycle ([7.1.20](/7.1.20#sec-20.5.1)).

The enzymes of the second to fourth steps form a multifunctional protein in peroxisomes. In Zellweger syndrome, a defect of peroxisome biogenesis, and in X-linked adrenoleukodystrophy, a defect of the peroxisomal ABC transporter ABCD1 that imports very-long-chain acyl-CoA ([7.1.13](/7.1.13#sec-13.5.4)), very-long-chain fatty acids accumulate in blood and brain; X-ALD destroys the myelin of boys within a few years of onset.

### 21.5.4. α and ω Oxidation

**Definition 21.5.1 (α Oxidation and ω Oxidation)** **α oxidation** is the peroxisomal removal of a single carbon from the carboxyl end of a fatty acid with a methyl branch at C-3, by hydroxylation at C-2 (phytanoyl-CoA hydroxylase, $\ce{O2}$), cleavage to formyl-CoA and an aldehyde one carbon shorter, and oxidation of the aldehyde, after which β oxidation can proceed. **ω oxidation** is the oxidation of the terminal methyl (ω) carbon of a fatty acid in the endoplasmic reticulum, by a cytochrome P-450 hydroxylase (with $\ce{O2}$ and NADPH), alcohol dehydrogenase and aldehyde dehydrogenase, to a dicarboxylic acid.

Phytanic acid, a 3,7,11,15-tetramethyl fatty acid derived from the phytol chain of chlorophyll, reaches humans in dairy products and ruminant fat (50–100 mg a day). Its methyl group on C-3 blocks the formation of a 3-keto intermediate; α oxidation converts it to pristanic acid, whose β oxidation gives alternately acetyl-CoA and propionyl-CoA. In Refsum disease, a defect of phytanoyl-CoA hydroxylase, phytanic acid accumulates and causes retinitis pigmentosa, neuropathy and deafness; patients avoid dietary phytanate.

ω Oxidation is a minor pathway for medium-chain fatty acids (C10–C12) in liver and kidney. The dicarboxylic acids formed can be β-oxidized from either end (to adipate and succinate); the pathway becomes significant when mitochondrial β oxidation is impaired, which is why dicarboxylic acids appear in the urine of patients with MCAD deficiency.

## 21.6. Ketone Bodies

### 21.6.1. Formation in the Liver

**Definition 21.6.1 (Ketone Bodies)** The **ketone bodies** are acetoacetate, D-β-hydroxybutyrate and acetone, formed from acetyl-CoA in liver mitochondria and exported to extrahepatic tissues as a water-soluble fuel (the name is historical: they are not particles, and β-hydroxybutyrate is not a ketone).

Ketogenesis takes place in the matrix of liver mitochondria in four steps.

1. Thiolase condenses two acetyl-CoA to acetoacetyl-CoA (the reverse of the last step of β oxidation).
2. Mitochondrial HMG-CoA synthase (HMGCS2, the committed and regulated step, induced by PPARα in fasting) adds a third acetyl-CoA to give 3-hydroxy-3-methylglutaryl-CoA (HMG-CoA). The cytosolic isozyme makes HMG-CoA for cholesterol synthesis ([7.1.26](/7.1.26)).
3. HMG-CoA lyase cleaves HMG-CoA to acetoacetate and acetyl-CoA. The net result of steps 1–3 is 2 acetyl-CoA + $\ce{H2O}$ → acetoacetate + 2 CoA + $\ce{H+}$.
4. D-β-Hydroxybutyrate dehydrogenase reduces part of the acetoacetate with NADH to D-β-hydroxybutyrate; the ratio of the two follows the mitochondrial $[\mathrm{NADH}]/[\ce{NAD+}]$ and is usually 3–6 in favor of β-hydroxybutyrate. This enzyme is specific for the D isomer and distinct from the L-specific dehydrogenase of β oxidation; the two stereochemical series keep the hydroxyacyl pools of degradation (L) and of ketone bodies and fatty acid synthesis (D) apart.

A small fraction of acetoacetate decarboxylates spontaneously (and with acetoacetate decarboxylase) to acetone ([7.1.17](/7.1.17#sec-17.1.2)), which is exhaled; the smell of acetone on the breath is a sign of ketosis.

```smiles
CC(=O)CC(=O)[O-] acetoacetate
C[C@@H](O)CC(=O)[O-] D-β-hydroxybutyrate
CC(C)=O acetone
```

Why make ketone bodies at all? When gluconeogenesis draws oxaloacetate out of the citric acid cycle ([7.1.19](/7.1.19)) and fatty acid oxidation is fast, the liver cannot oxidize all its acetyl-CoA, and its limited CoA becomes tied up as acetyl-CoA. Ketogenesis releases the CoA, lets β oxidation continue to supply the ATP and NADH for gluconeogenesis, and exports the energy of the remaining acetyl groups in a form the blood can carry without albumin and that crosses the blood–brain barrier, which fatty acids do not.

### 21.6.2. Use in Extrahepatic Tissues

Heart, skeletal muscle, renal cortex and, in starvation, the brain take up acetoacetate and β-hydroxybutyrate through monocarboxylate transporters and convert them to acetyl-CoA. β-Hydroxybutyrate is oxidized back to acetoacetate; succinyl-CoA:3-ketoacid CoA transferase (SCOT, β-ketoacyl-CoA transferase, thiophorase) transfers CoA from succinyl-CoA to acetoacetate; and thiolase cleaves acetoacetyl-CoA to two acetyl-CoA, which enter the citric acid cycle. The CoA transfer bypasses the succinyl-CoA synthetase step of the cycle, so it costs one GTP per acetoacetate. The liver lacks SCOT: it makes ketone bodies but cannot use them, so the flow between organs goes one way.

![Ketone bodies. In liver mitochondria, thiolase, HMG-CoA synthase and HMG-CoA lyase convert acetyl-CoA to acetoacetate, which β-hydroxybutyrate dehydrogenase reduces to D-β-hydroxybutyrate with NADH; some acetoacetate decarboxylates spontaneously to acetone. Both ketone bodies travel in the blood (crossing membranes on monocarboxylate transporters) to the mitochondria of extrahepatic tissues (heart, brain in starvation, skeletal muscle), where β-hydroxybutyrate is oxidized to acetoacetate, succinyl-CoA:3-ketoacid CoA transferase (SCOT, absent from liver) forms acetoacetyl-CoA, and thiolase gives two acetyl-CoA for the citric acid cycle](./plots/ketone-bodies.py)

In prolonged starvation, blood ketone bodies rise from below 0.1 mM after a night's fast to 5–7 mM after several weeks, and the brain adapts by inducing the transporters and enzymes: after about a month of fasting ketone bodies supply about two thirds of its energy (Owen, Cahill and colleagues, 1967), which spares the glucose that would otherwise have to come from muscle protein. Ketone bodies are therefore protein-sparing, the key to surviving long fasts ([7.1.29](/7.1.29)). Ketogenic diets, very low in carbohydrate, use the same adaptation and are an established treatment of drug-resistant epilepsy in children and of PDH deficiency ([7.1.20](/7.1.20#sec-20.1.4)).

### 21.6.3. Ketosis and Ketoacidosis

**Definition 21.6.2 (Ketosis)** **Ketosis** is an elevated concentration of ketone bodies in the blood (and their appearance in the urine); when it exceeds the buffering capacity of the blood and lowers the pH, it is ketoacidosis.

Acetoacetic acid ($\mathrm{p}K_{\mathrm{a}} \approx 3.6$) and β-hydroxybutyric acid ($\mathrm{p}K_{\mathrm{a}} \approx 4.7$) are fully ionized at blood pH, so each molecule made releases a proton. In physiological ketosis of fasting (up to about 7 mM), the protons are buffered and the kidney excretes the excess. In untreated type 1 diabetes, the lack of insulin removes the brake on lipolysis and on ketogenesis: fatty acids flood the liver, malonyl-CoA falls and CPT1 is fully active, glucagon drives gluconeogenesis, which withdraws oxaloacetate, and ketone bodies can exceed 20 mM (Lehninger quotes 90 mg per 100 mL in blood and 5000 mg per 24 h in urine, against normal values below 3 mg and 125 mg). The bicarbonate buffer is consumed, the blood pH falls below 7.3 (**acidosis**, [7.1.2](/7.1.2)), breathing becomes deep and rapid (Kussmaul respiration) to blow off $\ce{CO2}$, and without insulin, fluid and potassium the patient falls into coma. Diabetic ketoacidosis is one of the main acute complications of diabetes ([7.1.29](/7.1.29)); SGLT2 inhibitors can cause it at nearly normal blood glucose.

## Summary

The pathway cards ([7.1.16](/7.1.16#sec-16.1.3)):

| Field | β oxidation | Ketone body metabolism |
|---|---|---|
| Location | mitochondrial matrix (VLCAD and trifunctional protein on the inner membrane); peroxisomes for very long and branched chains; activation on the outer mitochondrial membrane | synthesis: liver mitochondria; use: mitochondria of heart, muscle, kidney, brain (not liver) |
| Net reaction | palmitoyl-CoA + 7 CoA + 7 FAD + 7 $\ce{NAD+}$ + 7 $\ce{H2O}$ → 8 acetyl-CoA + 7 $\ce{FADH2}$ + 7 NADH + 7 $\ce{H+}$ (Eq. (21.2)) | synthesis: 2 acetyl-CoA + $\ce{H2O}$ → acetoacetate + 2 CoA + $\ce{H+}$; acetoacetate + NADH + $\ce{H+}$ ⇌ D-β-hydroxybutyrate + $\ce{NAD+}$; use: acetoacetate + succinyl-CoA → acetoacetyl-CoA + succinate → 2 acetyl-CoA |
| Energy account | activation: 2 ATP equivalents (Eq. (21.1)); 4 ATP per turn, 10 per acetyl-CoA; ATP = 7n − 6 (Formula 21.3.1), palmitate 106; about 38 kJ g⁻¹ | β-hydroxybutyrate gives 2 acetyl-CoA + 1 NADH, at the cost of 1 GTP (CoA transfer) |
| Committed and regulated steps | CPT1 (carnitine shuttle, Definition 21.2.1) | mitochondrial HMG-CoA synthase; supply of fatty acids to the liver |
| Activators | fatty acids (supply); fasting | high fatty acid flux, low oxaloacetate (gluconeogenesis) |
| Inhibitors | CPT1: malonyl-CoA; 3-hydroxyacyl-CoA DH: NADH; thiolase: acetyl-CoA | insulin (lipolysis, ACC) |
| Covalent, hormonal and transcriptional control | epinephrine, glucagon (PKA: perilipin, HSL, Definition 21.1.3) mobilize fat; PKA and AMPK inactivate ACC; insulin activates ACC and PDE3B; PPARα induces the enzymes | PPARα induces HMGCS2; insulin deficiency → ketoacidosis |
| Opposing pathway | fatty acid synthesis (cytosol; malonyl-CoA ⊣ CPT1; 7.1.26) | — |
| Coenzymes (vitamins) | CoA ($\mathrm{B_5}$), FAD ($\mathrm{B_2}$), NAD ($\mathrm{B_3}$), carnitine; odd chains: biotin ($\mathrm{B_7}$), coenzyme $\mathrm{B_{12}}$ | CoA, NAD |
| Diseases and drugs | MCAD and LCHAD/TFP deficiency, CPT and carnitine defects (hypoketotic hypoglycemia); propionic and methylmalonic acidemia, pernicious anemia; Zellweger syndrome, X-ALD, Refsum disease; lipoprotein lipase deficiency; fibrates (PPARα) | diabetic ketoacidosis (Definition 21.6.2); ketogenic diet (epilepsy, PDH deficiency) |

| Topic | Key points |
|---|---|
| Transport (21.1) | bile salts and micelles; chylomicrons (Definition 21.1.1), lipoprotein lipase and apoC-II (Definition 21.1.2); ATGL, HSL, MGL; albumin |
| Entry (21.2) | acyl adenylate, PPi hydrolysis; CPT1 – translocase – CPT2; two CoA pools |
| β oxidation (Definition 21.3.1) | FAD-dehydrogenation (trans-Δ²), hydration (L), NAD⁺-dehydrogenation, thiolysis; ETF; trifunctional protein (Definition 21.3.2); same chemistry as succinate → oxaloacetate |
| Auxiliary pathways (21.4) | enoyl-CoA isomerase; 2,4-dienoyl-CoA reductase (NADPH); propionyl-CoA → succinyl-CoA (biotin, epimerase, B₁₂ mutase, Definition 21.4.1) |
| Other oxidations (21.5) | peroxisomes: acyl-CoA oxidase, H₂O₂, very long chains; α oxidation of phytanate; ω oxidation in the ER (Definition 21.5.1) |
| Ketone bodies (Definitions 21.6.1, 21.6.2) | HMG-CoA pathway in liver; SCOT in other tissues; brain in starvation; ketoacidosis in diabetes |

## Questions

1. How many ATP are obtained from the complete oxidation of (a) stearate (18:0), (b) oleate (18:1 cis-Δ⁹), (c) heptadecanoate (17:0)? Use 2.5 ATP per NADH, 1.5 per FADH₂ and 10 per acetyl-CoA.

   **Answer** (a) Formula 21.3.1: $7 \times 18 - 6 = 120$. (b) The isomerase bypasses one acyl-CoA dehydrogenase step, so one $\ce{FADH2}$ fewer: 118.5. (c) Seven turns give 7 $\ce{FADH2}$, 7 NADH (28 ATP), 7 acetyl-CoA (70 ATP) and one propionyl-CoA; activation costs 2. Propionyl-CoA → succinyl-CoA costs 1 ATP (carboxylase); succinyl-CoA → oxaloacetate in the cycle gives 1 GTP, 1 $\ce{FADH2}$, 1 NADH (5 ATP); to oxidize the four carbons completely, oxaloacetate → PEP (−1 GTP) → pyruvate (+1 ATP) → acetyl-CoA (+2.5) → 10: total for propionyl-CoA about $-1 + 5 - 1 + 1 + 2.5 + 10 = 16.5$. Sum: $28 + 70 + 16.5 - 2 = 112.5$.

2. A patient with MCAD deficiency fasts overnight during an infection and becomes hypoglycemic, with low ketone bodies and high octanoylcarnitine. Explain each finding.

   **Answer** Long chains are shortened normally to about C8 (VLCAD and the trifunctional protein work), but medium-chain acyl-CoA cannot be oxidized further; it accumulates and is exported as octanoylcarnitine. The liver therefore makes little acetyl-CoA (low ketone bodies) and little ATP and NADH for gluconeogenesis, and the tissues that normally burn fat in fasting consume glucose instead: hypoglycemia. The fasting state and infection raise the demand for fat oxidation and expose the defect.

3. Show that a camel obtains water from oxidizing the fat of its hump. How much water does the complete oxidation of 1 kg of tripalmitoylglycerol yield? ($M_{\mathrm{r}}$ 807.3.)

   **Answer** Tripalmitin $\ce{C51H98O6}$ + 72.5 $\ce{O2}$ → 51 $\ce{CO2}$ + 49 $\ce{H2O}$. 1 kg is 1.239 mol, which gives $1.239 \times 49 \times 18.02\,\mathrm{g} = 1.09\,\mathrm{kg}$ of water, more than the mass of the fat. Part of it is lost again in the extra breathing needed to supply the $\ce{O2}$ (72.5 mol per mol), so the net gain depends on how much water the exhaled air carries away; the benefit is nevertheless that fat is a store of both energy and water.

4. Why can the liver make ketone bodies but not use them, and why can the brain use ketone bodies but not fatty acids?

   **Answer** The liver lacks succinyl-CoA:3-ketoacid CoA transferase, the enzyme that activates acetoacetate; it can only make and export them, so a one-way flow from liver to other tissues is guaranteed even when the liver itself oxidizes fat intensively. Fatty acids circulate bound to albumin and do not cross the blood–brain barrier efficiently (and brain mitochondria have little capacity for β oxidation); ketone bodies are small water-soluble anions carried by monocarboxylate transporters, whose expression rises in starvation.

5. A child with methylmalonic acidemia improves when given large doses of vitamin B₁₂, another does not. What do these responses tell you about the defects? Which other compounds accumulate?

   **Answer** A response to $\mathrm{B_{12}}$ points to a defect in the uptake or conversion of cobalamin to adenosylcobalamin, or a mutase with reduced affinity for the coenzyme, which high concentrations of the vitamin can overcome; no response points to a mutase lacking activity. Methylmalonyl-CoA and propionyl-CoA accumulate, giving methylmalonic acid, propionate, 3-hydroxypropionate, methylcitrate (from propionyl-CoA and oxaloacetate) and propionylcarnitine; propionyl-CoA also inhibits other enzymes (e.g. of the urea cycle), causing hyperammonemia.

6. (Open question) In untreated type 1 diabetes, blood glucose and ketone bodies are both high, while in prolonged starvation glucose is low-normal and ketone bodies high. Explain the difference in terms of insulin, glucagon and the regulatory points of this chapter and of 7.1.19, and why ketoacidosis is rare in starvation.

   **Answer** Outline: in both states glucagon is high and malonyl-CoA low, so fatty acids enter liver mitochondria freely and ketogenesis is active. In starvation, a small amount of insulin persists; it restrains lipolysis (PDE3B) and the flux of fatty acids to the liver, and the ketone bodies stimulate some insulin secretion themselves, a negative feedback; glucose is low-normal because gluconeogenesis is limited by precursors and the brain spares glucose by using ketone bodies. In type 1 diabetes, insulin is absent: lipolysis is unrestrained (huge fatty acid supply), muscle and adipose tissue take up little glucose (no GLUT4), and gluconeogenesis and glycogenolysis are maximal, so glucose rises while ketogenesis far exceeds the capacity of extrahepatic tissues to oxidize ketone bodies. The production of protons outruns buffering and renal excretion, and the osmotic diuresis from glucose adds dehydration; in starvation the same pathways run at a rate the body can buffer.
