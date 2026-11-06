---
title: Plant Respiration
description: "The concept, significance and measures of plant respiration (respiration rate, respiratory quotient and its calculation); degradation of starch and sucrose; features of plant glycolysis (PPi-dependent phosphofructokinase, the PEP carboxylase bypass, bottom-up regulation) and fermentation; features of the plant TCA cycle and malic enzyme; the glyoxylate cycle and germination of oilseeds; the physiological role of the pentose phosphate pathway; branches of plant mitochondrial electron transport: external and internal NAD(P)H dehydrogenases, alternative oxidase and cyanide-resistant respiration, uncoupling protein and thermogenesis; other terminal oxidases; regulation of respiration; growth and maintenance respiration; effects of temperature, O₂ and CO₂ and Q₁₀; respiration and storage of agricultural products."
source_hash: 85957f5b0fbb
---

Photosynthesis stores light energy in sugars, and respiration releases that energy again in a controlled manner for use by the cell, at the same time producing the carbon skeletons needed for the synthesis of many other substances. In broad outline plant respiration is the same as in animals (glycolysis, the citric acid cycle, oxidative phosphorylation), and the reactions and stoichiometry of these pathways were covered in biochemistry ([7.1.18](/7.1.18), [7.1.20](/7.1.20), [7.1.23](/7.1.23)). This chapter treats only what is distinctive in plants: the substrates of plant respiration are mainly sucrose and starch rather than glucose; glycolysis has several parallel bypasses and is regulated "from the bottom up"; and mitochondria have malic enzyme, non-proton-pumping NAD(P)H dehydrogenases and an alternative oxidase, which animals lack, so that a large electron flux can bypass ATP synthesis and be used to keep carbon metabolism flowing, to prevent the production of reactive oxygen species, and even to produce heat. These features reflect a basic circumstance of plant energy metabolism: plants are usually not short of energy (sunlight) but are limited more by water, nutrients and other factors, so metabolic flexibility often matters more than energy efficiency.

The chapter also treats respiration from the viewpoint of the whole plant and agriculture: a plant respires 30%–60% of the carbon it fixes in photosynthesis each day (Taiz et al.), and we consider how respiration divides into a part used for growth and a part used for maintenance (Section 12.10), how it varies with temperature, oxygen and $\ce{CO2}$ (Section 12.11), and how it can be controlled in the storage of agricultural products (Section 12.12).

## 12.1. Concept, Significance and Measures of Respiration

### 12.1.1. Concept and Significance

**Cellular respiration** in plants is the process in which living cells, using organic substances such as carbohydrates as substrates, oxidize and break them down step by step through a series of enzymatic reactions, releasing energy and producing various intermediates. Under aerobic conditions the substrate is completely oxidized to $\ce{CO2}$ and $\ce{H2O}$, which is aerobic respiration; under oxygen deficiency the substrate is only partly oxidized, producing products such as ethanol or lactate and releasing only a little energy, which is **anaerobic respiration** (anaerobic respiration in higher plants is **fermentation**, Section 12.3.4).

With sucrose, the main sugar transported and imported by plants, as substrate, the overall reaction of aerobic respiration is

$$
\ce{C12H22O11 + 12O2 -> 12CO2 + 11H2O}, \qquad \Delta_{\mathrm{r}}G'^{\circ} = -5760\ \mathrm{kJ\,mol^{-1}}.
$$
This is the reverse of photosynthesis: sucrose is completely oxidized to $\ce{CO2}$, and $\ce{O2}$ is reduced to water as the final electron acceptor.

The physiological significance of respiration:

1. Supply of energy: the free energy of the substrate is released step by step, mostly conserved as ATP, for use in uptake, transport, synthesis and growth;
2. Supply of carbon skeletons: intermediates of glycolysis, the pentose phosphate pathway and the citric acid cycle are the starting points for the synthesis of amino acids, nucleotides, lipids, phenolics, terpenoids, hormones and pigments (Section 12.4), so respiration is central to plant metabolism;
3. Supply of reducing power: NADH and NADPH are used for nitrate reduction, ammonium assimilation, fatty acid synthesis and so on;
4. Role in defense: respiration increases on wounding and infection, the pentose phosphate pathway supplies precursors for the synthesis of phenolics and phytoalexins, and polyphenol oxidase oxidizes phenolics to quinones that are toxic to pathogens (Section 12.8);
5. Heat production: in a few plants the inflorescence warms itself using a respiratory pathway that does not conserve energy (Section 12.7.5).

### 12.1.2. Respiration Rate and Respiratory Quotient

**Definition 12.1.1 (Respiration Rate)** The amount of $\ce{CO2}$ released or $\ce{O2}$ taken up per unit time by plant material per unit mass (fresh or dry weight), per unit area or per unit nitrogen content is the **respiration rate**, also called respiration intensity, commonly in $\mu\mathrm{mol\,g^{-1}\,s^{-1}}$ or $\mathrm{nmol\,g^{-1}\,s^{-1}}$; for leaves it is also often expressed in $\mu\mathrm{mol\,m^{-2}\,s^{-1}}$.

Methods of measurement include the infrared gas analyzer (measuring $\ce{CO2}$ release), the oxygen electrode (measuring $\ce{O2}$ consumption in solution), and the classical Warburg manometry and the small-basket method (absorbing $\ce{CO2}$ in alkali and titrating). On a fresh-weight basis, the respiration rate of whole plants is generally lower than that of animal tissue, mainly because the large vacuoles and cell walls of plant cells contain no mitochondria; but some plant tissues (developing buds, thermogenic inflorescences) have respiration rates comparable to those of the most active animal tissues, and isolated plant mitochondria respire as fast as mammalian ones or even faster.

**Definition 12.1.2 (Respiratory Quotient)** The ratio of the moles (or volumes) of $\ce{CO2}$ released to $\ce{O2}$ taken up by plant tissue over a period

$$
\mathrm{RQ} = \frac{n(\ce{CO2})_{\text{released}}}{n(\ce{O2})_{\text{taken up}}}
$$
is the **respiratory quotient**, also called the respiratory coefficient.

RQ depends on the degree of oxidation of the substrate: the higher the ratio of oxygen to carbon in the substrate molecule, the less $\ce{O2}$ is needed for complete oxidation and the larger the RQ.

**Example 12.1.1 (Respiratory Quotients of Several Substrates)** By the stoichiometry of complete oxidation:

- glucose: $\ce{C6H12O6 + 6O2 -> 6CO2 + 6H2O}$, $\mathrm{RQ} = 6/6 = 1.0$;
- tripalmitin: $\ce{C51H98O6 + 72.5O2 -> 51CO2 + 49H2O}$, $\mathrm{RQ} = 51/72.5 = 0.70$;
- malic acid: $\ce{C4H6O5 + 3O2 -> 4CO2 + 3H2O}$, $\mathrm{RQ} = 4/3 = 1.33$; citric acid $\ce{C6H8O7 + 4.5O2 -> 6CO2 + 4H2O}$ is also $1.33$;
- oxalic acid: $\ce{C2H2O4 + 0.5O2 -> 2CO2 + H2O}$, $\mathrm{RQ} = 4$.

The RQ of protein is about 0.8. Thus $\mathrm{RQ} \approx 1$ when carbohydrate is the substrate, $\mathrm{RQ} < 1$ for fat or protein, and $\mathrm{RQ} > 1$ for organic acids.

RQ also reflects the supply of $\ce{O2}$ and the fate of the substrate:

- ethanol fermentation releases $\ce{CO2}$ without consuming $\ce{O2}$, so an RQ clearly greater than 1 is a sign that fermentation is taking place (Section 12.11.2);
- when oilseeds germinate, fat is not completely oxidized but is converted to sugar through the glyoxylate cycle and gluconeogenesis (Section 12.5); this conversion consumes $\ce{O2}$ but releases little $\ce{CO2}$, and RQ can be far below 0.7. Take the conversion of palmitic acid to hexose as an example: the 16 carbons yield 4 succinate through β oxidation and the glyoxylate cycle, 4 carbons are finally lost as $\ce{CO2}$ in the PEP carboxykinase reaction, and the remaining 12 carbons become 2 hexoses,

  $$
  \ce{C16H32O2 + 11O2 -> 2C6H12O6 + 4CO2 + 4H2O},
  $$
  $\mathrm{RQ} = 4/11 = 0.36$. The RQ measured in early germinating oilseeds is often between 0.3 and 0.7, reflecting the proportions of conversion and complete oxidation;
- ripening apples and lemons and grapes at véraison use organic acids as the main respiratory substrate, and their RQ is greater than 1.

## 12.2. Degradation of Starch and Sucrose

In most plant cells the carbon for respiration comes from sucrose (from the phloem, [7.13.11](/7.13.11)), starch stored in plastids, triose phosphates from photosynthesis, and the products of lipid and protein degradation, rather than from free glucose.

### 12.2.1. Starch

Starch is synthesized and degraded only in plastids (chloroplasts and **amyloplasts**). Several enzymes cooperate to degrade it completely:

| Enzyme | Action | Product |
|---|---|---|
| α-Amylase | Can attack intact starch grains, hydrolyzing α-1,4 glycosidic bonds within the chain at random | Dextrins, maltose, glucose |
| β-Amylase | Cuts off maltose units in succession from the nonreducing end | Maltose, limit dextrin |
| Starch phosphorylase | Phosphorolysis of α-1,4 bonds from the nonreducing end (does not degrade branches) | Glucose-1-phosphate |
| Debranching enzymes (isoamylase, limit dextrinase) | Hydrolyze α-1,6 bonds at branch points | Linear fragments |

When transitory starch accumulated in leaves by day is degraded at night, the surface of the starch grain is first phosphorylated, for example by glucan water dikinase, which loosens it, and it is then degraded mainly by β-amylase to maltose; maltose enters the cytosol through a transporter in the chloroplast inner membrane, where it is converted to sucrose or enters glycolysis. In germinating cereal seeds, degradation of endosperm starch depends mainly on α-amylase secreted by the aleurone layer under induction by gibberellin ([7.13.20](/7.13.20)).

### 12.2.2. Sucrose

Plants break down sucrose by two pathways:

- The invertase pathway: invertases in the cell wall, vacuole or cytosol hydrolyze sucrose to glucose and fructose, and the hexoses are then phosphorylated in the cytosol by hexokinase using ATP. The invertase reaction is essentially irreversible and drives the reaction toward breakdown.
- The sucrose synthase pathway: sucrose synthase converts sucrose and UDP in the cytosol to fructose and UDP-glucose; UDP-glucose pyrophosphorylase then uses pyrophosphate ($\mathrm{PP_i}$) to convert UDP-glucose to UTP and glucose-1-phosphate. This reaction is close to equilibrium and saves one ATP.

Thus each sucrose molecule consumes 2–4 ATP in the initial stage of glycolysis, depending on whether it is broken down by sucrose synthase or by invertase. Transgenic plants and mutants lacking a particular invertase or sucrose synthase show that each enzyme is essential for particular processes (for example, fruit development in several crops requires sucrose synthase and cell wall invertase), but when one is missing the others can still sustain respiration. This phenomenon, in which different pathways perform similar functions and can substitute for one another without marked loss of function, is called metabolic redundancy and is a general feature of plant metabolism.

## 12.3. Features of Plant Glycolysis and Fermentation

### 12.3.1. Glycolysis in the Cytosol and in Plastids

The main reactions of plant glycolysis are almost the same as in animals ([7.1.18](/7.1.18)), but there are several special features. The glycolytic enzymes are present in both the cytosol and the plastids: the partial glycolysis that takes place in plastids supplies precursors for synthetic reactions in plastids (fatty acids, tetrapyrroles, aromatic amino acids). By day, the products of photosynthesis can enter glycolysis directly as triose phosphates; at night, the carbon from starch degradation enters cytosolic glycolysis mainly as glucose (and maltose). Glycolysis is like a funnel: its initial stage collects carbon from various carbohydrate sources and funnels it into triose phosphates; each sucrose molecule yields four triose phosphates, which in the energy-conserving stage yield four pyruvate, and the two **substrate-level phosphorylations** at phosphoglycerate kinase and pyruvate kinase give a net of four ATP (per sucrose).

In higher plants, some of the glycolytic enzymes also associate with the surface of the outer mitochondrial membrane when respiratory demand is high, allowing intermediates to pass directly between adjacent enzymes (**substrate channeling**), separate from the cytosolic glycolysis that supplies carbon to other processes.

### 12.3.2. Two Bypasses

PPi-dependent phosphofructokinase. Besides ATP-dependent phosphofructokinase (irreversible) and fructose-1,6-bisphosphatase in gluconeogenesis, the plant cytosol has a PPi-dependent phosphofructokinase, which catalyzes

$$
\text{fructose-6-phosphate} + \mathrm{PP_i} \rightleftharpoons \text{fructose-1,6-bisphosphate} + \mathrm{P_i}.
$$
Its content in most plant tissues is far higher than that of the ATP-dependent enzyme; the reaction is reversible and uses pyrophosphate in place of ATP as the phosphoryl donor. Transgenic plants in which it is inhibited still survive, showing that the ATP-dependent enzyme can take over its function. The concentration of pyrophosphate in the plant cytosol is fairly high, and using it in place of ATP can save energy, which is especially important under oxygen deficiency.

The PEP-to-malate bypass. PEP at the end of glycolysis can, besides being converted to pyruvate by pyruvate kinase, be carboxylated to oxaloacetate by the ubiquitous cytosolic PEP carboxylase and then reduced to malate by malate dehydrogenase using NADH. Malate can be transported into the vacuole for storage, or into the mitochondria, where it is oxidized by malic enzyme (Section 12.4). Thus both pyruvate kinase and PEP carboxylase can supply substrate to the mitochondria, with pyruvate predominating in most tissues. In transgenic tobacco with less than 5% of normal cytosolic pyruvate kinase activity, the respiration and photosynthesis rates of leaves are no different from controls, but root growth is reduced, showing that this bypass can partly replace pyruvate kinase. PEP carboxylase also serves to replenish the citric acid cycle intermediates that are withdrawn for synthesis (**anaplerotic reactions**), for example 2-oxoglutarate that is transported to the chloroplast for nitrogen assimilation.

### 12.3.3. Bottom-Up Regulation

Animal glycolysis is regulated mainly at phosphofructokinase by AMP, ATP and others, with secondary regulation at pyruvate kinase, and is "top-down." Plants are different: AMP and ATP are not the main effectors of plant phosphofructokinase and pyruvate kinase. The primary regulatory point of plant glycolysis is at the end, the consumption of PEP: pyruvate kinase and PEP carboxylase are feedback-inhibited by intermediates of the citric acid cycle and their derivatives (malate, citrate, 2-oxoglutarate, glutamate); accumulation of PEP then strongly inhibits ATP-dependent phosphofructokinase, an inhibition relieved by $\mathrm{P_i}$, so the cytosolic PEP/$\mathrm{P_i}$ ratio is the key to controlling glycolytic activity. Fructose-2,6-bisphosphate affects reactions in both directions and regulates the partitioning of sugar between respiration and synthesis. This "bottom-up" regulation allows plants to regulate the net flux of glycolysis to pyruvate independently of the Calvin cycle and of the interconversion of sucrose and starch, and lets glycolysis adjust to the demand of synthesis for precursors. Besides being a glycolytic enzyme, hexokinase acts as a glucose sensor that induces sugar-dependent gene expression.

### 12.3.4. Fermentation

Without oxygen, oxidative phosphorylation stops, the NADH produced by glycolysis can no longer be reoxidized, and glyceraldehyde-3-phosphate dehydrogenase stops for lack of $\ce{NAD+}$. Fermentation reduces pyruvate and regenerates $\ce{NAD+}$, allowing glycolysis to continue:

- **Alcoholic fermentation**: pyruvate decarboxylase decarboxylates pyruvate to acetaldehyde, and alcohol dehydrogenase reduces acetaldehyde to ethanol using NADH, with release of $\ce{CO2}$;
- **Lactic acid fermentation**: lactate dehydrogenase reduces pyruvate to lactate using NADH.

Flooding greatly slows the diffusion of oxygen in soil and makes root tissue hypoxic; this is the best-studied situation in plants. The initial response of maize roots to oxygen deficiency is lactic acid fermentation, followed by a switch to alcoholic fermentation: lactate accumulation acidifies the cytosol, and the lower pH inhibits lactate dehydrogenase and activates pyruvate decarboxylase, so metabolism turns to ethanol. Ethanol is thought to be the less toxic end product because it can diffuse out of the cell, whereas lactate accumulation acidifies the cytosol. Fermentation also occurs in the interior of large storage organs (potato tubers, tuberous roots) and in seeds in early germination before the seed coat has broken.

Efficiency of fermentation. The $\Delta_{\mathrm{r}}G'^{\circ}$ of complete oxidation of sucrose is $-5760\ \mathrm{kJ\,mol^{-1}}$; synthesis of ATP under the nonstandard conditions of the cell requires about $50\ \mathrm{kJ\,mol^{-1}}$. Glycolysis gives a net of 4 ATP per sucrose, and with ethanol or lactate as end product the energy conserved in ATP is only about 4% of the energy available in sucrose, most of the energy remaining in the ethanol or lactate; aerobic respiration gives about 60 ATP (Section 12.7.1) and conserves about 52%. Under oxygen deficiency, breaking down sucrose with sucrose synthase rather than invertase and using PPi in place of ATP can raise the ATP yield.

Because the energy recovery of fermentation is so low, sugar breakdown must speed up to maintain the ATP supply needed to keep the cell alive. This is how the **Pasteur effect** appears in plants: the rate of glycolysis rises on the change from aerobic to anaerobic conditions and falls on the change from anaerobic to aerobic conditions.

**Example 12.3.1 (How Fast Sugar Must Be Broken Down Under Oxygen Deficiency)** Aerobically each sucrose broken down gives about 60 ATP, and fermentation gives 4 (about 5 via the sucrose synthase pathway). To maintain the same ATP supply, the rate of sucrose breakdown in fermentation must be $60/4 = 15$ times that under aerobic conditions. In practice glycolysis in oxygen-deficient tissue can speed up only several-fold, the ATP supply still falls substantially, and metabolism turns to maintaining only the most basic functions.

Genes of glycolytic and fermentation enzymes are induced under oxygen deficiency. One mechanism by which plants sense oxygen is the N-end rule pathway: the N-terminal cysteine of group VII ERF transcription factors is oxidized by plant cysteine oxidase in the presence of oxygen, and the protein is then degraded; under oxygen deficiency they are stabilized and enter the nucleus to activate hypoxia-response genes. Over the long term under anoxic conditions plants grow poorly or even die, for three reasons: little energy is produced and respiratory substrates are consumed excessively; few intermediates are produced, so that insufficient raw material is available for the synthesis of cell components; and the accumulation of ethanol, lactate and acetaldehyde is toxic to cells. Many flood-tolerant plants (rice, sunflower) rely on **aerenchyma** running from leaf to root to deliver oxygen to the roots, and in mangroves *Avicennia*, *Rhizophora* and others grow respiratory roots that project above the water.

## 12.4. Features of Plant Mitochondria and the Citric Acid Cycle

### 12.4.1. Entry and Oxidation of Pyruvate

Plant mitochondria are usually spherical or rod-shaped, 0.5–1.0 µm in diameter and up to 3 µm long; a plant cell contains hundreds of mitochondria, and metabolically active tissues (such as guard cells) have particularly many. The outer membrane is permeable to metabolites and ions of molecular mass below about 10 kDa; the inner membrane is an osmotic barrier, and pyruvate enters the matrix through a transporter in the inner membrane in exchange for $\ce{OH-}$, is oxidatively decarboxylated to acetyl-CoA by the **pyruvate dehydrogenase complex**, and then enters the citric acid cycle ([7.1.20](/7.1.20)).

Pyruvate dehydrogenase is regulated by reversible phosphorylation and is inactivated by phosphorylation. Its kinase is inhibited by pyruvate and ADP and activated by NADH, acetyl-CoA and $\ce{NH4+}$, so the enzyme is active when substrate is plentiful and ATP demand is high. The activity of pyruvate dehydrogenase in leaves in the light falls to about 25% of that in the dark, partly because $\ce{NH4+}$ released by glycine oxidation in photorespiration activates the kinase.

Each pyruvate is completely oxidized in the mitochondria to 3 $\ce{CO2}$, producing 4 NADH and 1 $\ce{FADH2}$ and, by one substrate-level phosphorylation, 1 ATP. Per sucrose, the citric acid cycle produces in total 16 NADH, 4 $\ce{FADH2}$ (at succinate dehydrogenase) and 4 ATP.

### 12.4.2. Features of the Plant Citric Acid Cycle

- Succinyl-CoA synthetase produces ATP in plants and GTP in animals; the two are energetically equivalent.
- The matrix of plant mitochondria contains abundant NAD⁺-malic enzyme, which catalyzes the oxidative decarboxylation of malate:

  $$
  \text{malate} + \ce{NAD+} \to \text{pyruvate} + \ce{CO2} + \mathrm{NADH}.
  $$
  Together with malate dehydrogenase, it allows plant mitochondria to oxidize malate, citrate and other citric acid cycle intermediates completely to $\ce{CO2}$ without needing pyruvate supplied by glycolysis. Chinese textbooks often say that "NAD⁺-malic enzyme does not exist in other organisms," which is not accurate: animal mitochondria also have NAD(P)⁺-malic enzyme, but its content and role are much greater in plants. Malic enzyme allows plant mitochondria to metabolize the products of glycolysis by way of the PEP carboxylase bypass and also to regulate the level of organic acids in the cell: many plant tissues (not only **CAM plants**) store large amounts of malate or other organic acids in the vacuole, and as fruits ripen these are consumed by malic enzyme in the mitochondria. The rapid fall in malate content and rapid rise in sugar content in grape after véraison is just the result of the respiratory consumption of malate acting together with the change of unloading pathway ([7.13.11](/7.13.11#sec-11.8.2)).
- γ-Aminobutyric acid (GABA) accumulates under many stresses; it is synthesized from 2-oxoglutarate and degraded to succinate, and this "GABA shunt" bypasses two steps of the citric acid cycle; its functional relation to stress is still unclear.
- In the light, mitochondria of photosynthetic tissue oxidize glycine produced by photorespiration; the photorespiration rate can reach 20%–40% of the total photosynthetic rate, so by day photorespiration supplies the respiratory chain with more NADH than the normal respiratory pathway. At the same time the mitochondria supply the cytosol with ATP and supply 2-oxoglutarate for nitrogen assimilation.

## 12.5. The Glyoxylate Cycle and Germination of Oilseeds

Seeds of castor bean, sunflower, rape, cucumber and other plants have oil (**triglyceride**) as their main reserve, stored in **oil bodies** enclosed by a single phospholipid layer in the cells of the cotyledons or endosperm. Complete oxidation of 1 g of oil releases about 40 kJ of energy and of 1 g of starch about 15.9 kJ, so oil is a compact form of storage. On germination, the oil is converted to sucrose and transported to the growing seedling. This conversion requires the cooperation of three organelles:

1. Lipase hydrolyzes the triglyceride in the oil bodies to fatty acids and glycerol; oil bodies and glyoxysomes are often closely apposed in the cell.
2. Fatty acids enter the glyoxysome (a specialized peroxisome in the storage tissue of seeds), are activated to acyl-CoA, and broken down by **β oxidation** to acetyl-CoA. In animals β oxidation occurs in mitochondria; in the storage tissue of plant seeds it takes place entirely in glyoxysomes (in vegetative tissue, in peroxisomes). For each acetyl-CoA produced, 1/2 $\ce{O2}$ is reduced to water and one NADH is produced.
3. The **glyoxylate cycle** converts two acetyl-CoA to one succinate. Acetyl-CoA condenses with oxaloacetate to give citrate, citrate is transported to the cytosol and isomerized by aconitase to isocitrate, and isocitrate returns to the glyoxysome and is processed by the two enzymes specific to the glyoxylate cycle: isocitrate lyase cleaves isocitrate to succinate and glyoxylate, and malate synthase combines a second acetyl-CoA with glyoxylate to make malate. Malate is transported to the cytosol and oxidized to oxaloacetate, which returns to the glyoxysome to continue the cycle. Compared with the citric acid cycle, the glyoxylate cycle skips the two decarboxylation steps, so no carbon is lost as $\ce{CO2}$.
4. Succinate is transported into the mitochondria and converted to malate by two steps of the citric acid cycle; malate is exchanged out of the mitochondria for succinate and oxidized to oxaloacetate in the cytosol.
5. Oxaloacetate is converted to PEP and $\ce{CO2}$ by PEP carboxykinase (consuming ATP), bypassing irreversible pyruvate kinase, and then **gluconeogenesis** produces hexose and finally sucrose.

Part of the acetyl-CoA is completely oxidized to supply energy and the rest is converted to sucrose. Animals lack isocitrate lyase and malate synthase and cannot convert fatty acids to sugar on balance. After the seedling emerges into the light and the cotyledons turn green, the enzymes specific to the glyoxysome disappear, and glyoxysomes are converted to leaf peroxisomes that take part in photorespiration.

## 12.6. The Physiological Role of the Pentose Phosphate Pathway

The reactions of the **pentose phosphate pathway** are described in [7.1.18](/7.1.18). In plants it is carried out by soluble enzymes in the cytosol and in plastids, and under most conditions the plastid pathway predominates (Chinese textbooks often write only "takes place in the cytoplasm"). Studies of $\ce{CO2}$ release from isotope-labeled glucose show that it accounts for 10%–25% of glucose breakdown, the rest going mainly through glycolysis; this proportion varies with development and growth conditions. The first two oxidative reactions (glucose-6-phosphate dehydrogenase and 6-phosphogluconate dehydrogenase) are essentially irreversible, produce NADPH and release $\ce{CO2}$; the later nonoxidative reactions are reversible. The overall reaction for six turns is

$$
6\ \text{glucose-6-phosphate} + 12\ \ce{NADP+} + 7\ce{H2O} \to 5\ \text{glucose-6-phosphate} + 6\ce{CO2} + \mathrm{P_i} + 12\,\mathrm{NADPH} + 12\ce{H+}.
$$

Its physiological significance:

1. NADPH in the cytosol: used for biosynthetic reactions and stress defense, and the substrate for reactions that scavenge reactive oxygen species. The outer face of the plant mitochondrial inner membrane has an NADPH dehydrogenase (Section 12.7.2), so the reducing power generated by the pentose phosphate pathway can also be used to make ATP through the respiratory chain.
2. NADPH in plastids: in nongreen plastids such as the amyloplasts of roots, and in chloroplasts in the dark, the pentose phosphate pathway is the main source of NADPH, used for fatty acid synthesis and nitrogen assimilation (for example, reduction of nitrite in roots).
3. Raw materials for synthesis: the intermediate erythrose-4-phosphate condenses with PEP to begin the shikimate pathway, which synthesizes aromatic amino acids and the precursors of phenolic compounds such as lignin, flavonoids and phytoalexins. Induction of pentose phosphate pathway enzymes by stresses such as wounding agrees with the need of protective tissue to synthesize aromatic compounds, and this is the biochemical basis for the statement that "the pentose phosphate pathway is related to disease resistance." In most organisms it supplies the ribose-5-phosphate for nucleotide synthesis, but in plants ribose seems to be synthesized mainly by another pathway not yet clear.
4. Link with photosynthesis: its nonoxidative stage shares many intermediates and enzymes with the **Calvin cycle**.

The pentose phosphate pathway is redox regulated. The initial enzyme glucose-6-phosphate dehydrogenase is in many cases inhibited by a high NADPH/$\ce{NADP+}$ ratio; in chloroplasts in the light it is also reduced and inactivated by the ferredoxin–thioredoxin system, while the Calvin cycle is synthesizing fructose-6-phosphate and glyceraldehyde-3-phosphate and mass action drives the nonoxidative reactions in reverse, so erythrose-4-phosphate can still be synthesized in the light. Glucose-6-phosphate dehydrogenase in nongreen plastids is less sensitive to inactivation by thioredoxin and NADPH and can maintain a highly reduced state of plastid components in the absence of photosynthesis.

## 12.7. Branches of Plant Mitochondrial Electron Transport

### 12.7.1. The Main Chain and ATP Yield

The plant **respiratory chain** contains the same four complexes as in other organisms ([7.1.23](/7.1.23)). For each pair of electrons passing through **Complex I**, Complex III and **Complex IV**, 4, 4 and 2 $\ce{H+}$ are pumped out, respectively; Complex II does not pump protons. Per ATP synthesized by ATP synthase, 3 $\ce{H+}$ pass through $\mathrm{F_o}$, and one more $\ce{H+}$ is needed for the import of ADP and $\mathrm{P_i}$ and export of ATP across the mitochondrial membrane, a total of 4 $\ce{H+}$. Hence:

**Formula 12.7.1 (Estimating the P/O Ratio)**

$$
\mathrm{P/O} = \frac{\text{number of } \ce{H+} \text{ pumped per electron pair}}{\text{number of } \ce{H+} \text{ needed per ATP}}. \tag{12.1}
$$

| Electron entry | $\ce{H+}$ pumped (per 2e⁻) | Theoretical P/O | Measured ADP/O in isolated mitochondria |
|---|---|---|---|
| Complex I (e.g., oxidation of malate) | 4 + 4 + 2 = 10 | 2.5 | 2.4–2.7 |
| Complex II (succinate) | 4 + 2 = 6 | 1.5 | 1.6–1.8 |
| External NADH dehydrogenase (cytosolic NADH) | 6 | 1.5 | 1.6–1.8 |
| Directly to Complex IV (artificial electron donor) | 2 (another 2 consumed on the matrix side, equivalent to 4) | 1.0 | 0.8–0.9 |

Older textbooks (and Chinese contest materials) give a P/O of 3 for NADH and 2 for $\ce{FADH2}$; these were integers taken from "three coupling sites" before the proton stoichiometry was settled. By the chemiosmotic mechanism there is no reason for the P/O ratio to be an integer, and 2.5 and 1.5 are now in general use ([7.1.23](/7.1.23#sec-23.3.5)). Historically there were three hypotheses for how oxidation and phosphorylation are coupled: chemical coupling, conformational coupling and the **chemiosmotic theory**; the chemiosmotic theory was established long ago and the first two have only historical interest. In plant mitochondria the **proton-motive force** consists mainly of the electrical potential difference ($\Delta\psi \approx 0.2\ \mathrm{V}$), with $\Delta\mathrm{pH}$ about 0.5, unlike chloroplasts, which rely almost entirely on $\Delta\mathrm{pH}$.

By the theoretical P/O ratios, the ATP produced by complete oxidation of one sucrose (cytosolic NADH being oxidized by the external NADH dehydrogenase, not through the alternative pathway) is:

| Stage | ATP per sucrose |
|---|---|
| Glycolysis: 4 substrate-level phosphorylations | 4 |
| Glycolysis: 4 cytosolic NADH × 1.5 | 6 |
| Citric acid cycle: 4 substrate-level phosphorylations | 4 |
| Citric acid cycle: 4 $\ce{FADH2}$ × 1.5 | 6 |
| Citric acid cycle (including pyruvate dehydrogenase): 16 NADH × 2.5 | 40 |
| Total | 60 |

At $50\ \mathrm{kJ\,mol^{-1}}$, 60 ATP conserve about 3010 kJ, about 52% of the standard free energy of sucrose, the rest being lost as heat. Per glucose this is about 30 ATP.

### 12.7.2. Non-Proton-Pumping NAD(P)H Dehydrogenases

The respiratory chain of plants (and of many fungi and protists) has components that mammalian mitochondria lack: several NAD(P)H dehydrogenases and an alternative oxidase, all bound to the inner membrane and none pumping protons, so the energy released when NADH is oxidized by them cannot be conserved as ATP but becomes heat; they are therefore called "nonphosphorylating" components.

- Internal NADH dehydrogenase $\mathrm{ND_{in}(NADH)}$: on the matrix side of the inner membrane, it oxidizes NADH in the matrix and passes electrons to **ubiquinone**, and is insensitive to the Complex I inhibitors rotenone and piericidin. Complex I has a higher affinity for NADH (lower $K_{\mathrm{m}}$): when the matrix NADH level is low (ADP plentiful), Complex I predominates; when ADP becomes limiting and NADH accumulates, $\mathrm{ND_{in}(NADH)}$ becomes more active and acts as an "overflow valve." There is also an NADPH dehydrogenase on the matrix side.
- External NAD(P)H dehydrogenases $\mathrm{ND_{ex}(NADH)}$ and $\mathrm{ND_{ex}(NADPH)}$: on the side of the inner membrane facing the intermembrane space, mostly dependent on $\ce{Ca^2+}$ and insensitive to rotenone, they directly oxidize cytosolic NADH or NADPH, with electrons entering the main chain at the ubiquinone pool. They spare plants the need to rely on a malate–aspartate shuttle, as animals do, to oxidize cytosolic NADH.
- Other dehydrogenases that pass electrons to the respiratory chain: proline dehydrogenase (degrading proline accumulated under osmotic stress after the stress is relieved), electron-transfer flavoprotein:ubiquinone oxidoreductase (degrading amino acids during carbon starvation), and the plant-specific galactonolactone dehydrogenase (using cytochrome c as electron acceptor and catalyzing the last step of ascorbate synthesis).

These dehydrogenases and the NADPH dehydrogenases make plant respiration more flexible and allow the redox balance of NADH and NADPH in the mitochondria and the cytosol to be controlled separately.

### 12.7.3. Alternative Oxidase and Cyanide-Resistant Respiration

**Definition 12.7.1 (Cyanide-Resistant Respiration and Alternative Oxidase)** Respiration that continues under conditions where cytochrome c oxidase is inhibited by cyanide, carbon monoxide and the like is **cyanide-resistant respiration**. The terminal oxidase that catalyzes it is the **alternative oxidase** (AOX): a diiron protein bound to the matrix side of the inner membrane that accepts electrons directly from ubiquinol and reduces $\ce{O2}$ to water by four electrons, bypassing Complexes III and IV. The pathway by which electrons flow through the alternative oxidase to oxygen is the alternative pathway.

Most plants have a capacity for cyanide-resistant respiration comparable to that of the cytochrome pathway. Several points need clarifying:

- The alternative oxidase accepts electrons from ubiquinol (the ubiquinone pool), not from cytochrome b of Complex III (some Chinese sources are inaccurate on this).
- It reduces $\ce{O2}$ to water, not to hydrogen peroxide.
- It is insensitive to cyanide, carbon monoxide, azide, the signaling molecule nitric oxide and the Complex III inhibitor antimycin A, and is specifically inhibited by salicylhydroxamic acid (SHAM) and propyl gallate. Treatment with SHAM and with cyanide separately allows the capacities of the two pathways to be estimated; to measure their actual fluxes in intact tissue, oxygen-isotope discrimination is used (the two oxidases discriminate differently against $\ce{^{18}O}$). The results show that in most tissues a considerable fraction of respiration actually goes through the alternative pathway.

The P/O ratio of the alternative pathway. When electrons pass through the alternative oxidase, both proton-pumping sites, Complexes III and IV, are bypassed. By Eq. (12.1): matrix NADH through Complex I and then the alternative oxidase has only the 4 $\ce{H+}$ pumped by Complex I, $\mathrm{P/O} = 4/4 = 1.0$; through $\mathrm{ND_{in}}$ or $\mathrm{ND_{ex}}$ and then the alternative oxidase, or succinate through Complex II and then the alternative oxidase, there is no proton-pumping step and $\mathrm{P/O} = 0$. Cyanide-resistant respiration therefore has "$\mathrm{P/O} \le 1$," and most of the energy is released as heat; Chinese textbooks also call it heat-releasing respiration.

Regulation of the alternative oxidase. It functions as a dimer and is regulated in three ways: activity is high when the disulfide bond between the two subunits is reduced (by thioredoxin) and low when it is oxidized; the more reduced the ubiquinone pool, the more active it is; and α-keto acids (pyruvate, glyoxylate) strongly activate it. The first two points ensure that it is most active under reducing conditions, and the third that its activity is high when citric acid cycle substrates are plentiful. Its transcription is often specifically induced by various abiotic and biotic stresses (low temperature, drought, osmotic stress, phosphate deficiency, pathogens) and by reactive oxygen species; changes in mitochondrial state (reactive oxygen species, citrate) alter expression of the alternative oxidase gene in the nucleus through signals, an example of retrograde regulation. Its content and activity also increase as fruit ripens.

Significance of the alternative pathway:

1. Heat production: thermogenesis in the inflorescences of a few plants (Section 12.7.5).
2. Energy overflow: when the respiration rate exceeds the cell's demand for ATP (ADP very low), the reduction level in the mitochondria rises and the alternative oxidase is activated, so that glycolysis and the citric acid cycle can keep running and supply carbon skeletons for synthesis, unrestricted by ATP synthesis. The alternative pathway thus allows mitochondria to adjust ATP production and synthesis of carbon skeletons independently.
3. Prevention of reactive oxygen species formation: stress often inhibits mitochondrial respiration and over-reduces the ubiquinone pool, so electrons leak to $\ce{O2}$ to form superoxide anion and then hydrogen peroxide and hydroxyl radical. The alternative oxidase draws electrons from the ubiquinone pool, prevents over-reduction, limits formation of reactive oxygen species, and lessens damage to respiration caused by stress.
4. Resistance to respiratory inhibitors: it allows plants to respire in the presence of $\ce{CN-}$, CO and the like. Cyanide-resistant respiration is widespread in the floral organs and pollen of the Araceae, Nymphaeaceae and others, in the seeds of maize, rice, pea, mung bean and cotton, in potato tubers, sweet potato tuberous roots and carrot roots, and also in fungi such as smut fungi and yeasts.

### 12.7.4. Uncoupling Protein

Uncoupling protein in the inner membrane of mammalian mitochondria greatly increases the permeability of the membrane to protons, so that protons return to the matrix without passing through ATP synthase, producing less ATP and more heat; this is the mechanism of heat production in brown fat ([7.1.23](/7.1.23#sec-23.5.1)). The alternative oxidase of plants and the uncoupling protein of animals were once thought to be two means to the same end, so it was a surprise to find a similar uncoupling protein in plant mitochondria. Plant uncoupling protein is induced by stress and activated by reactive oxygen species; knockout mutants show reduced photosynthetic carbon assimilation and growth. Like the alternative oxidase, its main role is to prevent over-reduction of the electron transport chain and the formation of reactive oxygen species rather than to produce heat. Plant mitochondria thus have several ways of bypassing ATP synthesis (non-proton-pumping dehydrogenases, the alternative oxidase, uncoupling protein), whereas mammals have only uncoupling protein.

![Electron transport and ATP synthesis in the inner membrane of plant mitochondria (schematic). A: Complexes I–IV and ATP synthase, common to all eukaryotes. B: In addition, plants have non-proton-pumping components (B): the external NAD(P)H dehydrogenases on the intermembrane space side (NDex, oxidizing cytosolic NADH and NADPH, Ca²⁺-dependent), the internal NADH dehydrogenase on the matrix side (NDin, rotenone-insensitive), and the alternative oxidase (AOX, cyanide-insensitive, inhibited by SHAM) that passes electrons from ubiquinol directly to O₂; uncoupling protein (UCP) lets protons return to the matrix without passing through ATP synthase. Blue arrows show electron flow and red arrows proton flow; per electron pair, Complexes I, III and IV pump 4, 4 and 2 H⁺, respectively](./plots/plant-etc.py)

### 12.7.5. Thermogenesis

In plants of some families, including the Araceae, Nymphaeaceae, Annonaceae and Nelumbonaceae, the inflorescence or a part of the flower respires intensely and produces heat at flowering. In the voodoo lily (*Sauromatum guttatum*), before pollination the respiration rate of the appendix at the top of the spadix rises sharply, expression of the alternative oxidase (the uncoupling protein in some species) increases greatly, and the temperature of the appendix is about 25 °C above ambient. During thermogenesis amines, indoles and terpenoids volatilize, giving off a smell of decay that attracts pollinating insects. **Salicylic acid** is the signal that triggers thermogenesis in the voodoo lily (Raskin et al., 1987); its role in plant disease resistance was discovered only later ([7.13.25](/7.13.25)). Some thermogenic plants can also regulate their own temperature: when the eastern skunk cabbage (*Symplocarpus foetidus*) flowers in early spring, it keeps the spadix at about 15–22 °C for a week or two even when the air temperature falls to around freezing; the receptacle of the lotus (*Nelumbo nucifera*) is kept at about 30–36 °C during the two or three days of flowering. Such temperature regulation means that the respiration rate rises as the inflorescence temperature falls, the opposite of the usual temperature response (Section 12.11.1).

![Temperature regulation in a thermogenic inflorescence (simulation with a heat-balance model, with parameters illustrative of the order of magnitude in skunk cabbage). The heat production rate H of the inflorescence is set by respiration through the alternative pathway, and heat loss is proportional to the temperature difference between inflorescence and air; respiration is under negative feedback control: it speeds up when the inflorescence temperature is below the set point. A: air temperature (gray line) fluctuates between −4 °C and 10 °C over two days, while the inflorescence temperature (red line) is held at about 20 °C; B: the corresponding respiration rate (O₂ consumption) is highest at night when the air temperature is lowest. Model: C dT/dt = H − h(T − Tₐ), H = H₀ + k(T_set − T), with respiration rate calculated from about 470 kJ released per mol O₂](./plots/thermogenesis.py)

**Example 12.7.1 (Energy Estimate for Heat Production)** A 5 g spadix is maintained at 20 °C at an air temperature of 0 °C. Suppose its surface area is about $15\ \mathrm{cm^2}$ and the heat transfer coefficient (convection and radiation) about $15\ \mathrm{W\,m^{-2}\,K^{-1}}$; then the heat loss is

$$
P = hA\Delta T = 15\times(15\times10^{-4})\times20\ \mathrm{W} = 0.45\ \mathrm{W}.
$$
Complete oxidation of glucose releases $2870/6 \approx 478\ \mathrm{kJ}$ per mole of $\ce{O2}$ consumed, so maintaining this power requires $\ce{O2}$ consumption of

$$
\frac{0.45\ \mathrm{J\,s^{-1}}}{4.78\times10^{5}\ \mathrm{J\,mol^{-1}}} = 9.4\times10^{-7}\ \mathrm{mol\,s^{-1}},
$$
that is, about $0.19\ \mu\mathrm{mol\,s^{-1}}$ per gram fresh weight (about $0.25\ \mathrm{mL\,O_2\,g^{-1}\,min^{-1}}$), one to two orders of magnitude higher than ordinary plant tissue ($10^{-3}$–$10^{-2}\ \mu\mathrm{mol\,g^{-1}\,s^{-1}}$) and comparable to the muscles of small birds and insects in flight; consumption per day is about $0.45\times86400/1.6\times10^{4} \approx 2.4\ \mathrm{g}$ of glucose ($1.6\times10^{4}\ \mathrm{J\,g^{-1}}$), so a thermogenic inflorescence depends on a storage organ (the rhizome of skunk cabbage) for a continuous supply of sugar (parameters illustrative). The respiration rate of most plant organs is too low to raise the temperature appreciably even if all electrons went through the alternative pathway and uncoupling protein completely abolished the membrane potential.

## 12.8. Other Terminal Oxidases

Enzymes that finally pass electrons from the substrate to $\ce{O2}$ are called terminal oxidases. Besides cytochrome c oxidase and the alternative oxidase in the mitochondria, plant cells have several other classes of oxidases, which are not coupled to ATP synthesis and which Chinese textbooks collectively call "terminal oxidases outside the mitochondria":

| Oxidase | Location | Metal | Cyanide | Affinity for $\ce{O2}$ | Function |
|---|---|---|---|---|---|
| Cytochrome c oxidase (Complex IV) | Inner mitochondrial membrane | Fe (heme a, a₃), Cu | Sensitive (also inhibited by CO, azide) | Very high, $K_{\mathrm{m}} < 1\ \mu\mathrm{M}$ | Main terminal oxidase, coupled to ATP synthesis; active in young tissue |
| Alternative oxidase | Inner mitochondrial membrane (matrix side) | Diiron | Insensitive; inhibited by SHAM | Lower | Energy overflow, prevention of reactive oxygen species, heat production |
| Polyphenol oxidase (phenol oxidase) | Plastids (substrate in the vacuole), in contact when the cell is damaged | Cu | Sensitive | — | Oxidizes phenolics to quinones, which polymerize to brown substances; wound response and disease resistance |
| Ascorbate oxidase | Cell wall, apoplast | Cu | Sensitive | — | Oxidizes ascorbate; regulates the redox state of the apoplast |
| Glycolate oxidase | Peroxisomes | None (flavoprotein, FMN) | Insensitive (not inhibited by CO either) | Very low | Oxidizes glycolate to glyoxylate in photorespiration and produces $\ce{H2O2}$ |

Under normal conditions polyphenol oxidase is separated from its substrates in different compartments; when the tissue is wounded or senesces the compartments are disrupted and the two come into contact, phenolics are oxidized to quinones and polymerize further to brown, reddish-brown or blackish-brown substances, which is why cut fruits and vegetables turn brown. Quinones are toxic to microorganisms and prevent infection of the wound. Tea making uses this: for green tea there is first "fixation" (high temperature inactivates polyphenol oxidase) to keep the green color; for black tea the leaves are rolled after withering, which disrupts the cells and lets tea polyphenols be oxidized and polymerized to reddish-brown theaflavins and thearubigins. In flue-curing of tobacco, rapid dehydration inhibits phenol oxidase activity, prevents the leaf from turning black, and keeps a bright yellow color.

**Superoxide dismutase**, **catalase** and peroxidase are also related to oxygen, but they scavenge reactive oxygen species and do not pass electrons from respiratory substrates: superoxide dismutase dismutates $\ce{O2^.-}$ to $\ce{H2O2}$ and $\ce{O2}$, catalase decomposes $\ce{H2O2}$ to water and oxygen, and peroxidase uses $\ce{H2O2}$ to oxidize various substrates.

## 12.9. Regulation of Respiration

### 12.9.1. Adenylates and Bottom-Up Control

The **energy charge** ([7.1.17](/7.1.17)) describes the extent to which the high-energy phosphate bonds of the adenylate pool are filled and is generally stable at 0.75–0.95 in living cells: when it is high, ATP synthesis is inhibited and utilization speeds up, and when low the reverse. In plants the main executor of this regulation is not the glycolytic enzymes (AMP and ATP are not the main effectors of plant phosphofructokinase and pyruvate kinase) but the mitochondria: ADP and $\mathrm{P_i}$, the substrates of ATP synthesis, are the main short-term regulators of the rates of glycolysis, the citric acid cycle and oxidative phosphorylation.

Plant respiration is controlled in "bottom-up" order:

1. When the cytosolic demand for ATP falls and ADP decreases, the electron transport chain slows (**respiratory control**, the control of respiration rate by ADP as acceptor, [7.1.23](/7.1.23#sec-23.4.1));
2. The slowing of electron transport causes NADH to accumulate in the matrix, and NADH inhibits dehydrogenases of the citric acid cycle such as isocitrate dehydrogenase and 2-oxoglutarate dehydrogenase;
3. Intermediates of the citric acid cycle (citrate and others) and their derivatives (glutamate) accumulate and inhibit pyruvate kinase and PEP carboxylase in the cytosol, and the PEP concentration rises;
4. PEP inhibits the conversion of fructose-6-phosphate to fructose-1,6-bisphosphate, limiting carbon flow into glycolysis.

ADP regulates electron transport and ATP synthesis first, the latter regulates the citric acid cycle, and the citric acid cycle in turn regulates glycolysis. This lets the carbon pathways of respiration adjust to the demand of synthesis for precursors. In addition, reversible phosphorylation of pyruvate dehydrogenase (Section 12.4.1) controls the entry of carbon into the citric acid cycle, and thioredoxin may regulate enzymes of almost all mitochondrial pathways through reversible redox change of cysteines.

### 12.9.2. The Pasteur Effect and Oxygen

Oxygen inhibits fermentation and reduces sugar consumption (Section 12.3.4). From the metabolic viewpoint it is a consequence of bottom-up control: in the presence of oxygen ATP is plentiful, ADP and $\mathrm{P_i}$ are low, and the enzymes at the end of glycolysis are inhibited; under oxygen deficiency oxidative phosphorylation stops, ADP and $\mathrm{P_i}$ accumulate, PEP is rapidly consumed, the inhibition of phosphofructokinase is relieved, and glycolysis speeds up.

## 12.10. Growth Respiration and Maintenance Respiration

### 12.10.1. Two Components

**Definition 12.10.1 (Growth Respiration and Maintenance Respiration)** Respiration that supplies energy and reducing power for converting sugar into the substances that make up new tissue (protein, lipid, cell wall and so on) is **growth respiration**; respiration needed to maintain the function and turnover of existing tissue (turnover of proteins and membrane lipids, maintenance of ion gradients, repair) is **maintenance respiration**.

The two are of comparable size. Using whole-plant gas-exchange data from white clover, McCree (1970) proposed writing the daily respiration $R$ as a linear combination of gross photosynthesis $P$ (representing the scale of growth) and plant dry weight $W$ (representing the biomass to be maintained):

**Formula 12.10.1 (McCree Equation)**

$$
R = k\,P + c\,W, \tag{12.2}
$$
with, for white clover at 20 °C, $k \approx 0.25$ (growth respiration is about a quarter of gross photosynthesis) and $c \approx 0.015\ \mathrm{d^{-1}}$ (about 1.5% of dry weight is respired per day).

Thornley wrote an equivalent form with growth rate as the independent variable:

$$
R = \frac{1 - Y_{\mathrm{G}}}{Y_{\mathrm{G}}}\frac{\mathrm{d}W}{\mathrm{d}t} + m\,W, \tag{12.3}
$$
where $Y_{\mathrm{G}}$ is the growth efficiency (the fraction of carbon used for growth that is converted to new biomass) and $m$ is the maintenance coefficient. $Y_{\mathrm{G}}$ is determined by the chemical composition of the new tissue: synthesizing lipids and proteins needs more energy and reducing power than synthesizing cellulose and starch, so seeds rich in oil and protein have lower $Y_{\mathrm{G}}$; for ordinary vegetative tissue $Y_{\mathrm{G}}$ is about 0.7–0.8. The maintenance coefficient $m$ is positively correlated with protein content (protein turnover is the main cost of maintenance) and with temperature ($Q_{10}$ about 2), and is generally 0.01–0.05 $\mathrm{d^{-1}}$.

In the growth period under ample light, growth respiration predominates; in mature organs that have stopped growing and at high temperature, the share of maintenance respiration is large. As trees age, the proportion of nonphotosynthetic tissue increases and so do respiratory losses.

![Partitioning of growth and maintenance respiration (simulated data and fit of the McCree equation). A: daily respiration R and daily gross photosynthesis P of a set of growing plants measured under different light, both divided by plant dry weight W; by Eq. (12.2), R/W = k(P/W) + c, the slope k of the line is the growth respiration coefficient and the intercept c is the maintenance respiration coefficient (simulated with k = 0.25 and c = 0.015 d⁻¹, with 8% measurement error added; the estimates from the least-squares fit are marked on the plot). B: change of the two respiration components during 60 days of growth of a plant (logistic growth): early on growth respiration predominates, and later, as biomass accumulates and growth slows, maintenance respiration becomes the main part](./plots/growth-maintenance.py)

**Example 12.10.1** A plant has a dry weight of 40 g and on a certain day its gross photosynthetic fixation is equivalent to 4.0 g of dry matter. By the McCree equation ($k = 0.25$, $c = 0.015\ \mathrm{d^{-1}}$), respiration that day is $R = 0.25\times4.0 + 0.015\times40 = 1.0 + 0.6 = 1.6\ \mathrm{g}$, 40% of gross photosynthesis, for a net gain of 2.4 g. If shading reduces gross photosynthesis to 1.0 g, respiration is $0.25 + 0.6 = 0.85\ \mathrm{g}$, 85%, and the net gain is only 0.15 g; in continuous cloudy and rainy weather maintenance respiration may exceed photosynthesis and the plant consumes its reserves. This shows why weak light and high night temperatures are especially unfavorable to the carbon budget of crops.

## 12.11. Environmental Factors Affecting Respiration

### 12.11.1. Temperature and $Q_{10}$

Between 0 and 30 °C the respiration rate generally increases with temperature, reaches a plateau at 40–50 °C, and at higher temperatures the respiratory machinery is inactivated and the rate falls.

**Definition 12.11.1 (Temperature Coefficient)** The factor by which the respiration rate increases for each 10 °C rise in temperature,

$$
Q_{10} = \frac{R(T + 10)}{R(T)},
$$
is the **temperature coefficient** $Q_{10}$ of respiration. It describes the response of respiration to short-term temperature change, that is, $R(T) = R_{\mathrm{ref}}\,Q_{10}^{(T - T_{\mathrm{ref}})/10}$.

The $Q_{10}$ of plant respiration is generally about 2. Its relation to the apparent **activation energy** $E_{\mathrm{a}}$ of the **Arrhenius equation** is

$$
\ln Q_{10} = \frac{10\,E_{\mathrm{a}}}{RT(T + 10)}, \tag{12.4}
$$
so near 20 °C $Q_{10} = 2$ corresponds to $E_{\mathrm{a}} \approx 51\ \mathrm{kJ\,mol^{-1}}$ and $Q_{10} = 3$ to about $81\ \mathrm{kJ\,mol^{-1}}$. By Eq. (12.4), even if $E_{\mathrm{a}}$ is constant $Q_{10}$ falls as temperature rises; the measured $Q_{10}$ falls faster, and in data from many plants it is approximately $Q_{10} \approx 3.09 - 0.043\,T$ ($T$ in °C; Tjoelker et al., 2001), about 2.9 at 5 °C, about 2.0 at 25 °C and about 1.6 at 35 °C: at low temperature respiration is limited by the maximal activity of enzymes, and at high temperature more by substrate supply and ATP demand.

Over longer time scales plants acclimate to temperature: plants grown at low temperature have a greater respiratory capacity (more mitochondria and enzymes per unit tissue), and those grown at high temperature a smaller one, so the respiration rate of a plant grown long at one temperature, measured at that temperature, is closer to its original level than the rate after a short-term warming or cooling. Acclimation makes the apparent $Q_{10}$ of the long-term temperature response smaller than the $Q_{10}$ measured in the short term. If climate models extrapolate the effect of warming on plant respiration directly with the short-term $Q_{10} = 2$, they overestimate the increase in respiration.

**Example 12.11.1** The respiration rate of a leaf at 20 °C is $1.0\ \mu\mathrm{mol\,m^{-2}\,s^{-1}}$, with $Q_{10} = 2.2$. After a short-term warming to 30 °C it is $2.2\ \mu\mathrm{mol\,m^{-2}\,s^{-1}}$; at 25 °C it is $1.0\times2.2^{0.5} = 1.48\ \mu\mathrm{mol\,m^{-2}\,s^{-1}}$. If after long growth at 30 °C the basal rate at 20 °C ($R_{\mathrm{ref}}$) falls to 0.7, then the rate at 30 °C is $0.7\times2.2 = 1.54\ \mu\mathrm{mol\,m^{-2}\,s^{-1}}$, 30% less than without acclimation; from 1.0 for growth at 20 °C to 1.54 for growth at 30 °C, the apparent $Q_{10}$ of the long-term response is only 1.54.

![Temperature response of respiration rate and acclimation (model). A: short-term temperature response: constant Q₁₀ = 2 (dashed line) and a Q₁₀ = 3.09 − 0.043T that falls with temperature (solid line), with the rate at 20 °C taken as 1; above about 40 °C the respiratory machinery is inactivated (schematic). B: short-term response curves of plants acclimated at 15 °C and 30 °C (different basal rates, same shape); the dots are the rates at the respective growth temperatures, and the slope of the line joining them gives the apparent Q₁₀ of the long-term response, which is smaller than the short-term Q₁₀](./plots/q10-acclimation.py)

### 12.11.2. Oxygen

$\ce{O2}$ is a substrate of respiration. The $\ce{O2}$ concentration in water in equilibrium with air (21% $\ce{O2}$) at 25 °C is about $0.25\ \mathrm{mM}$, whereas the $K_{\mathrm{m}}$ of cytochrome c oxidase for $\ce{O2}$ is far below $1\ \mu\mathrm{M}$, so respiration would seem not to be affected by the external $\ce{O2}$ concentration. In practice, however, the respiration rate of whole organs falls when $\ce{O2}$ is below about 5%, and of tissue slices when below 2%–3%, because $\ce{O2}$ diffuses very slowly in aqueous solution: compact organs (seeds, potato tubers) have a marked $\ce{O2}$ concentration gradient from surface to center, which limits the ATP/ADP ratio; this is especially so for seeds with thick coats and for organs submerged in water. In hydroponics the solution must be aerated; **aerenchyma** and respiratory roots are structural adaptations of plants to low-oxygen environments.

As the $\ce{O2}$ concentration falls, aerobic respiration weakens and fermentation gradually strengthens.

**Definition 12.11.2 (Extinction Point of Anaerobic Respiration)** The $\ce{O2}$ concentration at which anaerobic respiration (fermentation) of a tissue is inhibited and stops as the external $\ce{O2}$ concentration rises is the **extinction point of anaerobic respiration**.

Below the extinction point the total $\ce{CO2}$ release is the sum of aerobic respiration and fermentation: at very low $\ce{O2}$ fermentation is vigorous and $\ce{CO2}$ release is large (RQ greater than 1); as $\ce{O2}$ rises fermentation is inhibited while aerobic respiration has not yet reached its maximum, so total $\ce{CO2}$ release shows a minimum; with further increase, aerobic respiration increases. The positions of the extinction point and the minimum vary with organ and temperature, mostly within a range of a few percent to ten-odd percent $\ce{O2}$. In storage, $\ce{O2}$ is usually controlled at a level slightly above that at which fermentation becomes appreciable, so that consumption of organic matter is minimal without accumulation of ethanol and acetaldehyde causing off-flavor and physiological injury.

![Effect of O₂ concentration on respiration and fermentation in fruit and vegetable tissue (model, parameters illustrative). CO₂ release from aerobic respiration increases with O₂ in Michaelis–Menten form (apparent K_m taken as 2.5%, reflecting diffusion limitation in the tissue), while CO₂ release from fermentation is inhibited by O₂; total CO₂ release (black line) is lowest at about 3% O₂, and fermentation essentially disappears at about 8% O₂ (extinction point of anaerobic respiration, taken where fermentation falls to 2% of its maximum); RQ (right axis, dashed line) is far above 1 at low O₂. The shading indicates the 2%–3% O₂ commonly used in controlled-atmosphere storage](./plots/storage-o2.py)

### 12.11.3. CO₂, Water and Other Factors

- $\ce{CO2}$: high $\ce{CO2}$ concentration inhibits respiration, but at the 3%–5% used in artificial storage the direct inhibition is limited; raising atmospheric $\ce{CO2}$ to $700\ \mu\mathrm{mol\,mol^{-1}}$ has no direct inhibitory effect on plant respiration, but ecosystem-level measurements indicate that respiration per unit biomass may fall as $\ce{CO2}$ rises, by a mechanism not yet clear.
- Water: dry seeds have a very low water content and respire extremely weakly; on water uptake respiration increases rapidly ([7.13.20](/7.13.20)). When the water content of grain exceeds the limit for safe storage (12%–14% for most grains), the respiration of seeds and attached microorganisms rises sharply, leading to heating and molding. In vegetative organs mild water loss sometimes raises respiration transiently, and severe water deficit lowers it.
- Mechanical injury: wounding markedly speeds up respiration: compartmentation is disrupted, oxidases come into contact with substrates, and phenolics are rapidly oxidized; some cells resume division and form callus, and growth respiration increases.
- Mineral nutrition: when soil nutrients are insufficient, root respiration increases, because active ion uptake and growth in search of nutrients both need ATP.
- Internal factors: fast-growing plants and vigorous young and reproductive organs respire faster; among mature vegetative organs the stem has the lowest respiration. After an organ matures respiration stays constant or declines slowly until senescence; an exception is the **climacteric** in many fruits (avocado, apple, banana), a sharp rise in respiration at the onset of ripening, when starch (banana) or organic acids (tomato, apple) are largely converted to sugar, accompanied by an increase in ethylene and in alternative pathway activity ([7.13.23](/7.13.23)).

## 12.12. Respiration and Storage of Agricultural Products

Respiration is central to metabolism: during the crop growth period it should be allowed to proceed smoothly to support growth; during storage of agricultural products it must be lowered to reduce consumption of organic matter and loss of quality.

Crop cultivation. Cultivation and loosening the soil, and digging ditches to drain water, ensure aerobic respiration of the roots; flooding makes the roots respire anaerobically and accumulate ethanol, leading to root rot; reducing toxic substances in paddy fields ($\ce{H2S}$ and others) inhibit cytochrome c oxidase. In raising rice seedlings in low temperature in early spring, low temperature damages mitochondrial structure, respiration "idles," ATP is insufficient and metabolism is disordered, and together with oxygen deficiency this can lead to seedling rot.

Grain storage. The principle is to lower respiration and inhibit microorganisms: dry thoroughly to below the safe water content (this inhibits not only seed respiration but, more, the multiplication of microorganisms), keep cool, and lower the $\ce{O2}$ partial pressure (fill with $\ce{N2}$ or $\ce{CO2}$, or seal so that $\ce{O2}$ is consumed). A grain pile with a high water content respires vigorously, and the heat and moisture released further promote respiration and microbial activity, forming a positive feedback of "heating."

Storage of fruits and vegetables. Fruits and vegetables are living tissue and cannot be dried; respiration must be lowered while freshness is maintained:

- Low temperature: lowers the respiration rate ($Q_{10}$ about 2–3), but chilling-sensitive fruits and vegetables (banana, cucumber and other kinds of tropical and subtropical origin) suffer **chilling injury** below a certain temperature ([7.13.27](/7.13.27)). Potato tubers stored above 10 °C have enough respiration and associated metabolism to sprout; below 5 °C respiration and sprouting are both inhibited, but stored starch is degraded to sucrose and the tubers become sweet (low-temperature sweetening); potatoes are therefore best stored at 7–9 °C.
- Controlled-atmosphere storage: at low temperature, $\ce{O2}$ is lowered to 2%–3% and $\ce{CO2}$ raised to 3%–5%. Low $\ce{O2}$ rather than none is used to avoid lowering the oxygen partial pressure in the tissue to the point of causing fermentation (Section 12.11.2).
- Control of ethylene: ripening of climacteric fruit is initiated by ethylene, and removing ethylene or using an inhibitor of ethylene action (1-MCP) can delay the climacteric and ripening ([7.13.15](/7.13.15)).
- Maintain humidity and avoid mechanical injury (injury speeds up respiration and makes the product susceptible to disease).

Processing of agricultural products. Use or inhibition of polyphenol oxidase (tea making, tobacco curing, Section 12.8).

## Summary

Features of plant respiration compared with animals:

| Aspect | Plant feature | Significance |
|---|---|---|
| Substrates | Sucrose, starch, organic acids, lipids; sucrose broken down by invertase or sucrose synthase | Metabolic redundancy; sucrose synthase saves ATP |
| Glycolysis | In both cytosol and plastids; PPi-dependent phosphofructokinase; PEP carboxylase + malate dehydrogenase bypass; bottom-up regulation (PEP/$\mathrm{P_i}$) | Flexible supply of carbon skeletons for synthesis; saves ATP under oxygen deficiency |
| Citric acid cycle | Succinyl-CoA synthetase produces ATP; NAD⁺-malic enzyme; oxidizes glycine from photorespiration in the light | Can completely oxidize organic acids; regulates fruit acidity |
| Glyoxylate cycle | Isocitrate lyase and malate synthase in the glyoxysome; β oxidation in the glyoxysome (peroxisome) | Oilseeds convert fat to sugar |
| Pentose phosphate pathway | Cytosol and plastids (mainly plastids), 10%–25% of glucose breakdown; regulated by NADPH/$\ce{NADP+}$ and thioredoxin | NADPH; erythrose-4-phosphate for the shikimate pathway |
| Electron transport | External and internal NAD(P)H dehydrogenases (non-proton-pumping, rotenone-resistant); alternative oxidase (cyanide-resistant, inhibited by SHAM); uncoupling protein | Energy overflow, prevention of reactive oxygen species, heat production |

P/O ratios of several electron pathways (4 $\ce{H+}$ per ATP):

| Pathway | $\ce{H+}$ pumped | P/O |
|---|---|---|
| NADH → Complex I → III → IV | 10 | 2.5 |
| Succinate or cytosolic NADH (NDex) → III → IV | 6 | 1.5 |
| NADH → Complex I → AOX | 4 | 1.0 |
| NDin / NDex / Complex II → AOX | 0 | 0 |

For a comparison of the terminal oxidases see the table in Section 12.8.

Main equations:

| Equation | Content |
|---|---|
| $\mathrm{RQ} = n(\ce{CO2})/n(\ce{O2})$ | Respiratory quotient: sugar 1.0, tripalmitin 0.70, protein about 0.8, malic acid 1.33, oxalic acid 4; fat → sugar 0.36; fermentation > 1 |
| Sucrose + 12 $\ce{O2}$ → 12 $\ce{CO2}$ + 11 $\ce{H2O}$, $-5760\ \mathrm{kJ\,mol^{-1}}$ | Aerobic respiration about 60 ATP per sucrose (52%); fermentation 4 ATP (4%) |
| Eq. (12.1) P/O = $\ce{H+}$ pumped / 4 | Estimate of the P/O ratio |
| Eq. (12.2) $R = kP + cW$ | McCree equation: white clover $k \approx 0.25$, $c \approx 0.015\ \mathrm{d^{-1}}$ |
| Eq. (12.3) $R = \frac{1 - Y_{\mathrm{G}}}{Y_{\mathrm{G}}}\frac{\mathrm{d}W}{\mathrm{d}t} + mW$ | Growth and maintenance respiration |
| $R(T) = R_{\mathrm{ref}}Q_{10}^{(T - T_{\mathrm{ref}})/10}$; Eq. (12.4) | $Q_{10} \approx 2$; $Q_{10} \approx 3.09 - 0.043T$; acclimation makes the long-term response smaller |
| $P = hA\Delta T$, 1 mol $\ce{O2}$ ≈ 470 kJ | Energy estimate for a thermogenic inflorescence (Example 12.7.1) |

Environment and storage: temperature (rising from 0 to 30 °C, $Q_{10}$ about 2); $\ce{O2}$ (limiting below about 5% in organs; extinction point of anaerobic respiration; minimum of total $\ce{CO2}$ release); $\ce{CO2}$ (high concentrations inhibit); water content (safe grain water content 12%–14%); injury (respiration speeds up). Fruits and vegetables: low temperature (avoid chilling injury; potato 7–9 °C), controlled atmosphere (2%–3% $\ce{O2}$, 3%–5% $\ce{CO2}$), ethylene control.

## Questions

1. A batch of germinating sunflower seeds took up $45\ \mu\mathrm{mol}$ $\ce{O2}$ and released $27\ \mu\mathrm{mol}$ $\ce{CO2}$ in 2 h. (a) Find the RQ; (b) assuming that the substrate consumed has only two fates, part of the palmitic acid being completely oxidized ($\mathrm{RQ} = 16/23 = 0.70$) and part being converted to hexose ($\mathrm{RQ} = 4/11$), estimate how much $\ce{O2}$ each part consumed.

   **Answer** (a) $\mathrm{RQ} = 27/45 = 0.60$. (b) Let complete oxidation consume $x$ and conversion $y$ ($\mu\mathrm{mol}$ $\ce{O2}$), with $x + y = 45$ and $0.696x + 0.364y = 27$. This gives $0.332x = 27 - 16.4 = 10.6$, $x \approx 32$, $y \approx 13$. That is, about 70% of the oxygen consumption is used for complete oxidation to supply energy and about 30% for converting fat to sugar. (Complete oxidation of palmitic acid is $\ce{C16H32O2 + 23O2 -> 16CO2 + 16H2O}$.)

2. In the mitochondria of a tissue, 60% of the matrix NADH enters through Complex I and 40% through $\mathrm{ND_{in}}$; of the electrons in the ubiquinone pool, 70% flow to oxygen through the cytochrome pathway and 30% through the alternative oxidase (electrons from both entries are partitioned in the same ratio). Estimate the average P/O ratio for oxidation of matrix NADH in this tissue. What is the P/O ratio if everything went through the "standard" pathway?

   **Answer** There are four combinations: Complex I + cytochrome pathway $0.6\times0.7 = 0.42$, P/O 2.5; Complex I + AOX $0.6\times0.3 = 0.18$, P/O 1.0; $\mathrm{ND_{in}}$ + cytochrome pathway $0.4\times0.7 = 0.28$, P/O 1.5 (only Complexes III and IV pump 6 $\ce{H+}$); $\mathrm{ND_{in}}$ + AOX $0.4\times0.3 = 0.12$, P/O 0. The average is $0.42\times2.5 + 0.18\times1.0 + 0.28\times1.5 + 0 = 1.05 + 0.18 + 0.42 = 1.65$. If everything went through the standard pathway it would be 2.5. The energy efficiency of this tissue is thus only 66% of the standard, the excess energy being released as heat; this is a quantitative expression of plants trading energy efficiency for metabolic flexibility.

3. A fruit has a respiration rate of $40\ \mathrm{mg\,CO_2\,kg^{-1}\,h^{-1}}$ at 25 °C, with $Q_{10} = 2.5$. (a) What is the respiration rate when stored at 5 °C? (b) If the sugar available in the fruit is $80\ \mathrm{g\,kg^{-1}}$, taking hexose as respiratory substrate, how many days are needed at 25 °C and at 5 °C for 10% of it to be respired?

   **Answer** (a) $40\times2.5^{-2} = 6.4\ \mathrm{mg\,CO_2\,kg^{-1}\,h^{-1}}$. (b) Respiring 10% means $8\ \mathrm{g}$ of hexose ($8/180 = 0.0444\ \mathrm{mol}$), producing $0.267\ \mathrm{mol} = 11.7\ \mathrm{g}$ $\ce{CO2}$. At 25 °C this takes $11.7\times10^{3}/40 = 293\ \mathrm{h} \approx 12\ \mathrm{d}$; at 5 °C it takes $11.7\times10^{3}/6.4 = 1830\ \mathrm{h} \approx 76\ \mathrm{d}$. Low temperature slows the loss about 6-fold; if the fruit is chilling-sensitive, the temperature cannot be lowered to where chilling injury occurs.

4. Analyze with the McCree equation: two wheat varieties have maintenance respiration coefficients of $0.012$ and $0.020\ \mathrm{d^{-1}}$, and both have a growth respiration coefficient of 0.25. In late grain filling the plant dry weight is $15\ \mathrm{t\,ha^{-1}}$ and daily gross photosynthesis is $0.20\ \mathrm{t\,ha^{-1}}$; find the daily net dry matter accumulation of each. How should "lowering respiration" be viewed from the standpoint of breeding?

   **Answer** Variety 1: $R = 0.25\times0.20 + 0.012\times15 = 0.05 + 0.18 = 0.23\ \mathrm{t\,ha^{-1}\,d^{-1}}$, net accumulation $0.20 - 0.23 = -0.03$, so reserves have begun to be consumed; variety 2: $R = 0.05 + 0.30 = 0.35$, net accumulation $-0.15$. In late stages with large biomass and declining photosynthesis, maintenance respiration is the main carbon loss, and a variety with a low maintenance coefficient loses much less. However, maintenance respiration supports protein turnover, ion gradients and repair and cannot be lowered arbitrarily; growth respiration is proportional to the amount of growth, so lowering it means lowering growth. A feasible direction is to lower "nonessential" respiration (for example by changing tissue composition, reducing unnecessary protein turnover, or reducing dissipation through the alternative pathway under suitable conditions) rather than to inhibit respiration across the board.

5. Why can the spadix of eastern skunk cabbage be held at about 20 °C in winter, whereas a potato tuber of the same size cannot warm up at the same air temperature? Which mitochondrial components does this heat production mainly depend on? Why can its respiration be said to "violate" the usual temperature response?

   **Answer** Heat production requires a very high respiration rate: by Example 12.7.1, maintaining a 20 °C temperature difference requires $\ce{O2}$ consumption of about $0.2\ \mu\mathrm{mol}$ per gram of tissue per second, one to two orders of magnitude higher than ordinary plant tissue; the respiration rate of a potato tuber is far too low, and even if all electrons went through the alternative pathway the heat production would be far from enough to offset heat loss. The cells of the skunk cabbage spadix are rich in mitochondria, and heat production depends mainly on the alternative oxidase (in some species also on uncoupling protein): electrons bypass Complexes III and IV, the energy is released as heat rather than as ATP, and respiration is no longer limited by ADP supply (it is not subject to respiratory control). Normally the respiration rate falls as temperature falls ($Q_{10} > 1$), whereas in this inflorescence respiration speeds up when the air and its own temperature fall, equivalent to a negative-feedback thermostat with an apparent $Q_{10}$ less than 1.
