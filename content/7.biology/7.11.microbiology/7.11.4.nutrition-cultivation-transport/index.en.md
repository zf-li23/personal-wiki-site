---
title: Nutrition, Cultivation and Nutrient Transport
description: "What a microbial cell is made of and what it must take up (macronutrients, trace elements, growth factors); the nutritional classes defined by energy source, electron donor and carbon source; nutrient uptake by porins, proton-driven permeases, ABC transporters, the phosphotransferase system and siderophores; defined, complex, selective, differential and enriched media; aseptic technique, pure cultures and colonies; enrichment, competition for a limiting nutrient, single-cell isolation and the culture of anaerobes."
---

A bacterium doubles its mass in as little as 20 minutes, and everything in the new cell, from its proteins to its membrane lipids, is built from what it takes up from the outside. Microbial nutrition is therefore the starting point of microbial physiology. This chapter asks three practical questions: what elements and compounds a cell needs; how it brings them across a membrane that is impermeable to almost everything; and how microbiologists exploit these needs to grow, select and isolate microorganisms in the laboratory. The energy-yielding reactions that drive all of this are the subject of the next chapter (7.11.5); the unusual ways of making a living that only microorganisms have (phototrophy without oxygen, lithotrophy, methanogenesis) follow in 7.11.6 and 7.11.7. General membrane transport, including its thermodynamics and the transporter families shared with eukaryotes, is in [7.1.13](/7.1.13) and [7.3.5](/7.3.5); here we concentrate on the systems that are characteristic of bacteria and archaea.

## 4.1. What a Cell Is Made Of

### 4.1.1. The Chemical Composition of a Bacterial Cell

About 70–75% of the wet mass of a bacterial cell is water; a single *Escherichia coli* cell weighs about $10^{-12}\,\mathrm{g}$. Of the dry mass, about half is carbon, a quarter oxygen and hydrogen together, about 13% nitrogen, and the remaining few percent phosphorus, sulfur, potassium, magnesium and other elements. The dry mass is mostly macromolecules, dominated by protein:

| Component | Share of dry mass in *E. coli* (%) | Main elements beyond C, H, O |
|---|---|---|
| Protein | 55 | N, S |
| RNA | 20.5 | N, P |
| Lipid | 9.1 | P |
| Polysaccharide (glycogen, peptidoglycan) | 5.0 | N |
| Lipopolysaccharide | 3.4 | N, P |
| DNA | 3.1 | N, P |
| Small molecules and ions | about 4 | K, Mg, Fe and others |

(Data for *E. coli* growing in glucose minimal medium, from Neidhardt et al. (1996), *Escherichia coli and Salmonella: Cellular and Molecular Biology*.) Two features are worth remembering. Most of the cell's nitrogen is in protein and RNA, and most of its phosphorus is in RNA, so fast-growing cells, which are rich in ribosomes ([7.6.39](/7.6.39#sec-39.2.1)), need proportionally more phosphorus. DNA, the genome, is a small fraction of the dry mass.

### 4.1.2. Macronutrients

**Definition 4.1.1 (Macronutrients and Micronutrients)** A **macronutrient** is an element (or a compound supplying it) that a cell requires in large amounts: carbon, nitrogen, phosphorus, sulfur, potassium, magnesium and, for many organisms, calcium, sodium and iron, besides the hydrogen and oxygen supplied by water. A **micronutrient** is required in very small amounts: the trace elements and the organic growth factors.

| Element | Usual sources | Main uses in the cell |
|---|---|---|
| C | organic compounds (sugars, organic acids, amino acids, aromatics) or $\ce{CO2}$ | all organic molecules |
| N | $\ce{NH4+}$, $\ce{NO3-}$, amino acids; $\ce{N2}$ for nitrogen fixers | proteins, nucleic acids, peptidoglycan |
| P | phosphate $\ce{HPO4^2-}$ | nucleic acids, phospholipids, ATP, teichoic acids |
| S | sulfate, sulfide, organic sulfur | cysteine, methionine, coenzyme A, biotin, thiamine, Fe–S clusters |
| K | $\ce{K+}$ | the main intracellular cation, enzyme activation, turgor |
| Mg | $\ce{Mg^2+}$ | ribosomes, membranes, nucleic acids, ATP-dependent enzymes |
| Ca, Na | $\ce{Ca^2+}$, $\ce{Na+}$ | Ca: heat resistance of endospores (7.11.3), stabilizing cell walls; Na: required by most marine bacteria |
| Fe | $\ce{Fe^2+}$, $\ce{Fe^3+}$ complexes | cytochromes, Fe–S proteins, catalase, nitrogenase |

Virtually all microorganisms can assimilate ammonium; many can reduce nitrate to ammonium for assimilation; a minority, the nitrogen-fixing bacteria and archaea, can use $\ce{N2}$ (7.11.6). Most bacteria require an organic carbon source; the **autotrophs** make all their carbon compounds from $\ce{CO2}$. Several compounds serve two or three roles at once: for a nitrifying bacterium ammonium is both nitrogen source and energy source, and for *E. coli* growing on amino acids the same molecules supply carbon, nitrogen and energy.

### 4.1.3. Trace Elements and Growth Factors

**Definition 4.1.2 (Trace Elements and Organic Micronutrients)** **Trace elements** are metals and a few nonmetals required in minute amounts, mostly as cofactors of enzymes. The organic micronutrients, called growth factors in microbiology, are organic compounds that an organism needs but cannot synthesize from its carbon and nitrogen sources: chiefly **vitamins**, and for some organisms amino acids, purines and pyrimidines, sterols or heme.

| Trace element | Example of a function |
|---|---|
| Co | coenzyme $\mathrm{B_{12}}$ |
| Cu | cytochrome $c$ oxidase (copper centers), plastocyanin |
| Mn | superoxide dismutase, the water-splitting complex of photosystem II |
| Mo | nitrogenase, nitrate reductase, formate dehydrogenase (some) |
| Ni | urease, most hydrogenases, coenzyme $\mathrm{F_{430}}$ of methanogens |
| Se | selenocysteine of formate dehydrogenase and glycine reductase |
| W | formate dehydrogenases and aldehyde oxidoreductases of some hyperthermophiles |
| V | vanadium nitrogenase |
| Zn | carbonic anhydrase, RNA and DNA polymerases, many DNA-binding proteins |

Trace elements are rarely added deliberately to laboratory media: impurities in the major salts, in water and in glassware usually supply enough. The need for growth factors varies enormously. *E. coli* requires none and makes every organic molecule from glucose and ammonium. Lactic acid bacteria of the genera *Lactobacillus*, *Leuconostoc* and *Streptococcus*, which live in milk, plant juices and the animal gut where such compounds are abundant, require several vitamins and many amino acids, more than humans do; **mycoplasmas**, which lack a cell wall, need sterols for their membranes. Most vitamins are precursors of coenzymes ([7.1.17](/7.1.17#sec-17.2.1)): thiamine of thiamine pyrophosphate, riboflavin of FMN and FAD, nicotinic acid of $\ce{NAD+}$, pantothenate of coenzyme A, $p$-aminobenzoate of folate.

Within a species, mutants that have lost the ability to make a growth factor are **auxotrophs**, and the wild type from which they derive is a **prototroph** ([7.4.10](/7.4.10#sec-10.1.2)). The fastidious requirements of some organisms have been put to use: before chromatography, the growth of a lactic acid bacterium that required a vitamin was the standard assay of that vitamin in foods (a microbiological assay).

## 4.2. Nutritional Classes

### 4.2.1. Three Questions

Every organism must obtain energy, electrons for its biosynthetic reductions, and carbon. Biochemistry classifies organisms by energy source into **phototrophs** and **chemotrophs**, and by carbon source into **autotrophs** and **heterotrophs** ([7.1.1](/7.1.1)). Microbiology needs a third axis, because chemotrophs differ in the kind of chemical they oxidize.

**Definition 4.2.1 (Chemoorganotroph and Chemolithotroph)** A **chemoorganotroph** conserves energy by oxidizing organic compounds; a **chemolithotroph** conserves energy by oxidizing inorganic compounds such as $\ce{H2}$, $\ce{H2S}$, $\ce{S^0}$, $\ce{NH4+}$, $\ce{NO2-}$ or $\ce{Fe^2+}$ (from Greek *lithos*, stone).

The prefixes combine. Chemoorganotrophs are almost always heterotrophs (chemoorganoheterotrophs), because the organic compound that supplies energy also supplies carbon. Most chemolithotrophs fix $\ce{CO2}$ and are chemolithoautotrophs. Among phototrophs:

**Definition 4.2.2 (Photoautotroph and Photoheterotroph)** A **photoautotroph** uses light as its energy source and $\ce{CO2}$ as its main carbon source; a **photoheterotroph** uses light as its energy source and organic compounds as its main carbon source.

**Definition 4.2.3 (Mixotrophy)** **Mixotrophy** is the combination of an autotrophic and a heterotrophic mode of nutrition. In bacteriology the term usually denotes a chemolithotroph that conserves energy from an inorganic electron donor while taking its carbon from organic compounds; in protistology it denotes a phototroph that also ingests or absorbs organic food.

![Nutritional classes of microorganisms, arranged by three choices: the energy source (light or chemicals), the electron donor (inorganic or organic) and the main carbon source (CO₂ or organic compounds). Each leaf names the class and representative organisms: photoautotrophs (cyanobacteria, purple and green sulfur bacteria, algae), photoheterotrophs (purple nonsulfur bacteria, heliobacteria), chemolithoautotrophs (nitrifying bacteria, sulfur and iron oxidizers, many hydrogen oxidizers and methanogens), mixotrophs (some sulfur oxidizers such as *Beggiatoa*), and chemoorganoheterotrophs (most bacteria in culture, fungi, protozoa, animals). Many organisms switch facultatively between classes (note at the bottom).](./plots/nutritional-classes.py)

| Class | Energy | Electron donor | Carbon | Examples |
|---|---|---|---|---|
| Photoautotroph | light | $\ce{H2O}$, $\ce{H2S}$, $\ce{S^0}$, $\ce{H2}$, $\ce{Fe^2+}$ | $\ce{CO2}$ | cyanobacteria, algae; purple sulfur bacteria (*Chromatium*), green sulfur bacteria (*Chlorobium*) |
| Photoheterotroph | light | organic | organic | purple nonsulfur bacteria (*Rhodobacter*, *Rhodospirillum*), heliobacteria |
| Chemolithoautotroph | inorganic chemicals | inorganic | $\ce{CO2}$ | *Nitrosomonas*, *Nitrobacter*, *Acidithiobacillus*, methanogens growing on $\ce{H2}$ and $\ce{CO2}$ |
| Mixotroph (bacterial sense) | inorganic chemicals | inorganic | organic | some strains of *Beggiatoa* |
| Chemoorganoheterotroph | organic chemicals | organic | organic | *E. coli*, *Bacillus*, *Pseudomonas*, fungi, protozoa |

Many organisms move between classes. Purple nonsulfur bacteria grow as photoheterotrophs in the light without oxygen and as chemoorganotrophs in the dark with oxygen; *Cupriavidus necator* (formerly *Ralstonia eutropha*) is a chemolithoautotroph on $\ce{H2}$ and $\ce{CO2}$ but switches to organic compounds when they are present. The classification describes modes of metabolism, not fixed taxa, and it says nothing about phylogeny: chemolithotrophy and phototrophy are scattered across distantly related lineages.

### 4.2.2. Further Distinctions

Other terms describe how an organism meets its needs rather than which needs it has. *Oligotrophs* grow at very low nutrient concentrations, as in the open ocean, whereas *copiotrophs* grow fast when nutrients are abundant and wait out scarcity; the distinction reappears in competition for a limiting nutrient (Section 4.5.3). Saprotrophs live on dead organic matter and parasites on living hosts; most bacteria and fungi take up dissolved nutrients across their surface (osmotrophy), whereas many protists engulf particles (phagotrophy, 7.11.20). The energetics of each class is the subject of the next three chapters: chemoorganotrophy by fermentation and respiration in 7.11.5, phototrophy and autotrophy in 7.11.6, and chemolithotrophy, anaerobic respiration and methanogenesis in 7.11.7. One point applies to every chemolithotroph and anoxygenic phototroph whose electron donor is more positive than $\ce{NAD+}$/NADH: it must spend energy to push electrons uphill to NADH before it can fix $\ce{CO2}$, which makes these lifestyles slow-growing.

## 4.3. Getting Nutrients into the Cell

### 4.3.1. The Barrier and the Need to Concentrate

The cytoplasmic membrane is permeable only to water, gases ($\ce{O2}$, $\ce{CO2}$, $\ce{NH3}$) and small uncharged or lipophilic molecules ([7.1.13](/7.1.13#sec-13.3.2)). Everything else, sugars, amino acids, ions, vitamins, must be carried by proteins. Transport in microorganisms faces a second problem: nutrients in nature are often present at micromolar or nanomolar concentrations, whereas metabolism needs millimolar pools inside. Most uptake is therefore active, against a concentration gradient, and the systems that operate at the lowest concentrations have the highest affinities.

In **gram-negative bacteria** solutes must first cross the **outer membrane**. Small hydrophilic molecules diffuse through porins, trimeric β-barrel channels (OmpF and OmpC in *E. coli*) that exclude molecules larger than about $600\,\mathrm{Da}$; larger nutrients such as maltodextrins, vitamin $\mathrm{B_{12}}$ and iron–siderophore complexes need specific outer-membrane receptors (Section 4.3.5). Once in the **periplasm**, solutes meet the cytoplasmic membrane, where the real work of concentration is done.

Some molecules cross the cytoplasmic membrane by **facilitated diffusion**, through a protein but only down their concentration gradient: glycerol enters *E. coli* through the glycerol facilitator GlpF, an aquaporin-family channel, and is trapped inside by phosphorylation. For all other nutrients, bacteria and archaea use three kinds of energized transport, which differ in the energy source and in what happens to the solute (the table in the Summary compares them).

![Transport systems in the envelope of a gram-negative bacterium (outside on top, cytoplasm below; outer membrane, periplasm with peptidoglycan, cytoplasmic membrane). From left to right: diffusion through a porin; a proton symporter (lactose permease, LacY) and a Na⁺/H⁺ antiporter driven by the proton-motive force; an ABC transporter whose periplasmic binding protein delivers maltose to a membrane channel energized by ATP hydrolysis on the cytoplasmic side; the phosphotransferase system, which phosphorylates glucose during transport using phosphoenolpyruvate; and uptake of an iron–siderophore complex through a TonB-dependent outer-membrane receptor, a periplasmic binding protein and an ABC transporter.](./plots/transport-systems.py)

### 4.3.2. Simple Transporters Driven by the Proton-Motive Force

A simple transporter is a single membrane protein, typically of the major facilitator superfamily with 12 transmembrane helices, that couples the movement of a solute to the movement of $\ce{H+}$ or $\ce{Na+}$ down its electrochemical gradient. **Symporters** carry the solute and the ion in the same direction; **antiporters** carry them in opposite directions ([7.1.13](/7.1.13#sec-13.3.3)). The energy comes from the **proton-motive force** generated by respiration or photosynthesis (7.11.5), or in fermenters by ATP synthase running in reverse.

The classic example is lactose permease (LacY) of *E. coli*, encoded in the *lac* operon ([7.2.11](/7.2.11#sec-11.1.1)), which brings in one proton with each lactose. Phosphate, sulfate, many amino acids and organic acids enter by their own symporters; marine bacteria use $\ce{Na+}$ symport, and $\ce{Na+}/\ce{H+}$ antiporters export sodium and help regulate cytoplasmic pH.

**Example 4.3.1** How far can a proton symporter concentrate an uncharged solute? At equilibrium the free energy of moving one proton inward balances that of moving one solute molecule outward against its gradient, so

$$
\ln\frac{[\mathrm{S}]_{\mathrm{in}}}{[\mathrm{S}]_{\mathrm{out}}} = -\frac{F\,\Delta p}{RT},
$$
where $\Delta p = \Delta\varphi - (2.303\,RT/F)\,\Delta\mathrm{pH}$ is the proton-motive force expressed as a potential (inside minus outside; negative in respiring cells). For *E. coli* with $\Delta p \approx -0.18\,\mathrm{V}$ at $25\,^\circ\mathrm{C}$ ($RT/F = 0.0257\,\mathrm{V}$), the ratio is $\mathrm{e}^{0.18/0.0257} \approx 1.1 \times 10^{3}$. A cation symported with two protons would reach the square of this. Real accumulation is lower because the solute leaks back and is consumed, but the calculation shows why the proton-motive force is enough to concentrate most nutrients a thousandfold.

### 4.3.3. ABC Transporters and Binding Proteins

**ABC transporters** ([7.1.13](/7.1.13#sec-13.5.4)) are the most numerous transporter family in most bacterial genomes; *E. coli* has about 80. Uptake systems of this family have three parts: two transmembrane domains forming the channel, two ATP-binding (ABC) domains on the cytoplasmic side, and a substrate-binding protein that captures the solute. In gram-negative bacteria the binding protein floats in the periplasm; in gram-positive bacteria and archaea, which lack a periplasm, it is anchored to the outer face of the membrane by a lipid tail or fused to the transporter.

The maltose system of *E. coli* is the best studied: the maltose-binding protein MalE closes around maltose like a Venus flytrap, docks on the MalFG channel and triggers ATP hydrolysis by the MalK dimer, which opens the channel inward. Two ATP are hydrolyzed per molecule transported. The binding proteins have dissociation constants in the nanomolar to low micromolar range, so ABC systems work at concentrations at which proton-driven permeases are nearly useless; this is why they dominate the genomes of oligotrophs such as the marine bacterium *Pelagibacter*. Other ABC transporters export molecules: drugs, lipopolysaccharide, toxins and capsule polysaccharides (7.11.15, 7.11.34).

### 4.3.4. Group Translocation: The Phosphotransferase System

**Definition 4.3.1 (Group Translocation)** **Group translocation** is transport in which the solute is chemically modified as it crosses the membrane, so that what appears inside is a different compound from what was taken up outside; the energy comes from an energy-rich compound rather than from an ion gradient.

**Definition 4.3.2 (Phosphotransferase System)** The **phosphotransferase system** (PTS, the phosphoenolpyruvate:carbohydrate phosphotransferase system) of bacteria takes up sugars and releases them in the cytoplasm as sugar phosphates. A phosphoryl group is relayed from phosphoenolpyruvate (PEP) to the cytoplasmic Enzyme I, to the small phosphocarrier protein HPr, and then to a sugar-specific Enzyme II complex: EIIA (cytoplasmic), EIIB (cytoplasmic, often fused to the next domain) and EIIC, the membrane channel, which transports the sugar while EIIB phosphorylates it.

Enzyme I and HPr are shared by all PTS sugars; each sugar (glucose, mannose, fructose, mannitol, $N$-acetylglucosamine and others) has its own Enzyme II. For glucose in *E. coli*, the relay is PEP → Enzyme I (a histidine) → HPr (His15) → EIIA$^{\mathrm{Glc}}$ (a histidine) → EIIB$^{\mathrm{Glc}}$ (a cysteine) → glucose, which emerges as glucose 6-phosphate.

![The glucose phosphotransferase system of *E. coli* as an SBGN process diagram. A phosphoryl group passes from phosphoenolpyruvate (PEP, which becomes pyruvate) to Enzyme I, HPr, EIIA^Glc and EIIB^Glc; the membrane channel EIIC^Glc transports glucose, which EIIB phosphorylates to glucose 6-phosphate. P marks a phosphorylated state. Below, the two regulatory outputs of EIIA^Glc: phosphorylated EIIA^Glc (glucose absent) activates adenylate cyclase, raising cAMP; unphosphorylated EIIA^Glc (glucose being transported) binds and inhibits lactose permease and other permeases (inducer exclusion).](./plots/pts-relay.py)

The PTS is economical. Transport and the first step of glycolysis are done for the price of one PEP, whereas a proton symporter followed by hexokinase costs one proton plus one ATP, and an ABC transporter followed by hexokinase three ATP. It is widespread among facultative and obligate anaerobes, for which ATP is scarce, and absent from many strict aerobes. Its second role is regulatory: the phosphorylation state of EIIA$^{\mathrm{Glc}}$ reports whether glucose is being taken up. When glucose flows in, EIIA$^{\mathrm{Glc}}$ is mostly unphosphorylated and blocks the permeases of other sugars, **inducer exclusion** ([7.2.11](/7.2.11#sec-11.3.3)); when glucose is absent, phosphorylated EIIA$^{\mathrm{Glc}}$ activates adenylate cyclase, and cAMP–CRP turns on the operons for alternative carbon sources. This is the mechanism of **catabolite repression** in *E. coli* and of the **diauxic growth** on glucose and lactose; regulatory networks of this kind are surveyed in 7.11.11.

### 4.3.5. Iron and Siderophores

Iron is the most demanding trace nutrient. Every respiring cell needs it for cytochromes and Fe–S proteins, but at neutral pH in the presence of oxygen it exists as ferric hydroxides whose solubility limits free $\ce{Fe^3+}$ to about $10^{-18}\,\mathrm{M}$, far below the micromolar level a bacterium needs. Inside an animal host the situation is worse, because transferrin, lactoferrin and ferritin hold iron out of reach, a defense called nutritional immunity.

**Definition 4.3.3 (Siderophore)** A **siderophore** (Greek, "iron carrier") is a low-molecular-weight compound secreted by a microorganism that binds $\ce{Fe^3+}$ with very high affinity and specificity and is taken back into the cell, as the iron complex, by a dedicated transport system.

The three main chemical classes are catecholates (enterobactin of *E. coli*, whose affinity constant for $\ce{Fe^3+}$, about $10^{49}\,\mathrm{M^{-1}}$, is the highest known), hydroxamates (ferrichrome of fungi, desferrioxamine of *Streptomyces*, used as the drug deferoxamine to treat iron overload in patients) and carboxylates or mixed types (pyoverdine, the yellow-green fluorescent pigment of *Pseudomonas*). In a gram-negative bacterium the ferric siderophore is too large for porins; it binds a specific outer-membrane receptor (FepA for enterobactin), which is energized by the TonB–ExbB–ExbD complex that transmits the proton-motive force of the cytoplasmic membrane across the periplasm. A periplasmic binding protein and an ABC transporter then carry the complex into the cytoplasm, where iron is released by reduction to $\ce{Fe^2+}$ or by hydrolysis of the siderophore. Synthesis of siderophores and their receptors is repressed by the regulator Fur when iron is plentiful.

Siderophores are shared goods: a cell that makes none can take up complexes made by its neighbors, and many bacteria carry receptors for siderophores they cannot synthesize. They are therefore a model system for the evolution of cooperation and cheating ([7.10.16](/7.10.16)), and in infections a contest between pathogen and host (7.11.33): the host protein lipocalin-2 sequesters enterobactin, and *Salmonella* and pathogenic *E. coli* evade it by making salmochelin, a glucosylated enterobactin that lipocalin-2 cannot bind. Many pathogens also take iron directly from heme and hemoglobin.

## 4.4. Culture Media

### 4.4.1. Defined and Complex Media

A culture medium is a nutrient solution prepared for growing microorganisms; it must be sterilized before use, usually by autoclaving at $121\,^\circ\mathrm{C}$, with heat-labile components sterilized by filtration (7.11.10).

**Definition 4.4.1 (Defined Medium and Complex Medium)** A **defined medium** (synthetic medium) is prepared from known amounts of pure chemicals, so that its exact composition is known. A **complex medium** contains digests or extracts of biological materials, such as peptones (protein hydrolysates), beef extract or yeast extract, whose exact composition is unknown.

| Medium | Composition per liter | Grows |
|---|---|---|
| Glucose–mineral salts (M9) | $\ce{Na2HPO4}$ 6 g, $\ce{KH2PO4}$ 3 g, $\ce{NaCl}$ 0.5 g, $\ce{NH4Cl}$ 1 g, $\ce{MgSO4}$ 2 mmol, $\ce{CaCl2}$ 0.1 mmol, glucose 4 g | *E. coli* (prototrophs) |
| Lysogeny broth (LB, Miller) | tryptone 10 g, yeast extract 5 g, $\ce{NaCl}$ 10 g | *E. coli* and many other heterotrophs, faster than in M9 |
| Thiosulfate–mineral salts | thiosulfate, phosphate, ammonium, $\ce{Mg^2+}$, trace metals, bicarbonate; no organic carbon | sulfur-oxidizing chemolithoautotrophs (*Thiobacillus*) |

A defined medium tells the experimenter exactly what the organism can use; it is required for physiological and genetic experiments, such as selecting **auxotrophs**. A simple defined medium with one carbon source works for organisms of great biosynthetic capacity like *E. coli*, but a lactic acid bacterium such as *Leuconostoc mesenteroides* grows in a defined medium only if about 20 amino acids, several vitamins and the purines and pyrimidines are added. For such organisms a complex medium is far easier to make, and even *E. coli* grows faster in one, because it is spared the synthesis of building blocks that the medium supplies. A semidefined medium adds a single undefined component, such as yeast extract, to a defined base. Complex media are sold as dehydrated powders that need only water.

### 4.4.2. Selective, Differential and Enriched Media

**Definition 4.4.2 (Selective, Differential and Enriched Media)** A **selective medium** contains agents that inhibit the growth of some organisms while allowing others to grow. A **differential medium** contains an indicator that reveals, by a visible change around the colonies, whether a particular metabolic reaction has taken place. An **enriched medium** is a complex medium supplemented with especially nutritious substances such as blood or serum, used to grow fastidious organisms.

Many media combine these functions, and they are the workhorses of diagnostic microbiology (7.11.16, 7.11.35):

| Medium | Selective agent | Differential reaction | Reading |
|---|---|---|---|
| Blood agar (complex base with about 5% sheep blood) | none (enriched) | hemolysis | β: clear zone, complete lysis of red cells (*Streptococcus pyogenes*, *Staphylococcus aureus*); α: greenish partial hemolysis, hemoglobin oxidized (*Streptococcus pneumoniae*, viridans streptococci); γ: no change (*Enterococcus*) |
| MacConkey agar | bile salts and crystal violet inhibit gram-positive bacteria | lactose fermentation, pH indicator neutral red | lactose fermenters (*E. coli*, *Klebsiella*, *Enterobacter*) form pink-red colonies; non-fermenters (*Salmonella*, *Shigella*, *Proteus*) are colorless |
| Eosin–methylene blue (EMB) agar | the dyes partly inhibit gram-positive bacteria | lactose fermentation, the dyes precipitate at low pH | strong acid producers (*E. coli*) dark with a green metallic sheen; weaker fermenters (*Enterobacter*) pink and mucoid; non-fermenters colorless |
| Mannitol salt agar | 7.5% NaCl selects staphylococci | mannitol fermentation, phenol red | *S. aureus* turns the medium yellow; most other staphylococci do not |
| Chocolate agar (blood lysed by heating) | none (enriched) | none | releases hemin (X factor) and $\ce{NAD+}$ (V factor) required by *Haemophilus influenzae* |

Selection can also be built from the nutrients and conditions rather than from inhibitors: a medium without fixed nitrogen selects nitrogen fixers, a medium with 20–25% NaCl selects extreme halophiles (7.11.9), and an antibiotic added to a medium selects cells that carry a resistance gene, the basis of selection in bacterial genetics ([7.4.10](/7.4.10#sec-10.1.2)).

### 4.4.3. Physical State

Media are used as liquids (broths), as solids and as semisolids. Liquid media serve for growing large quantities of cells and for following growth over time (7.11.8). Solid media immobilize cells so that each forms a separate colony (Section 4.5.2). The gelling agent is almost always agar, a polysaccharide from red algae: at about 1.5% it melts at about $85\,^\circ\mathrm{C}$ but does not set until it cools to about $40\,^\circ\mathrm{C}$, so heat-sensitive supplements and cells can be mixed into it, and very few bacteria can degrade it. Gelatin, used before it, melts at body temperature and is digested by many bacteria; agar was introduced into Robert Koch's laboratory in 1882 at the suggestion of Fanny Hesse, who used it in the kitchen (7.11.1). For chemolithoautotrophs, which are inhibited by the organic impurities of agar, silica gel is used instead. Semisolid media (0.3–0.5% agar) let motile bacteria spread from a stab, a simple test of motility.

### 4.4.4. Designing a Medium

A medium must supply every nutrient in usable form and in balanced amounts, and provide physicochemical conditions within the range the organism tolerates:

- *Nutrients.* The carbon and energy source in the largest amount (grams per liter), nitrogen next, then phosphorus, sulfur, $\ce{Mg^2+}$ and $\ce{K+}$, and growth factors in milligrams or less; the ratio of carbon to nitrogen decides whether the cells grow or store carbon as reserve polymers.
- *pH.* Most bacteria grow best near neutrality, fungi in slightly acidic media. Fermenters acidify their medium as they grow, so media are buffered with phosphate or contain solid $\ce{CaCO3}$ as a reserve base.
- *Osmotic strength and water activity.* Marine organisms need about 3% NaCl, halophiles much more; the general principles of **water activity** are in 7.11.9.
- *Redox potential.* Strict anaerobes need a low redox potential, provided by reducing agents (Section 4.5.5).

## 4.5. Pure Cultures and Isolation

### 4.5.1. Aseptic Technique

Microbiology became an experimental science when it became possible to grow one kind of organism at a time. A **pure culture** contains a single kind of microorganism, the descendants of one cell; keeping it pure requires **aseptic technique**, the set of practices that prevent contamination by the microorganisms present on every surface and in the air. Loops and needles are sterilized in a flame or are disposable, the mouths of tubes and flasks are protected from air currents, plates are opened only as far as necessary and only briefly, and work is done near a flame or in a laminar-flow cabinet. A sterile medium that shows no growth after incubation, when inoculated and handled in the same way as the cultures, controls for the technique itself.

### 4.5.2. Streak Plates, Spread Plates and Colonies

On a solid medium, a single cell grows into a visible mass, a **colony**, that typically contains $10^7$ to $10^9$ cells after one or two days. The streak plate is the standard way to obtain colonies from a mixture: a loopful of culture is drawn across one sector of the plate, and each subsequent sector is streaked with a fresh loop from the end of the previous one, so that cells are diluted step by step until they are deposited singly. Picking a well-separated colony and restreaking it two or three times gives a pure culture. In a spread plate a small volume of a diluted suspension is spread over the surface with a sterile spreader; in a pour plate it is mixed with molten agar that is then allowed to set. Both are used to count viable cells, which is discussed with growth in 7.11.8.

![The streak plate for isolating pure cultures. A: the four-sector streak; the loop is resterilized between sectors, and each sector is drawn from the end of the previous one (arrows), so that the cell density falls stepwise. B: the plate after incubation, simulated for a mixture of two bacteria: confluent growth in the first sector, separate colonies of both kinds in the last, from which a colony is picked and restreaked.](./plots/streak-plate.py)

Colonies have characteristic forms that are used in identification (7.11.16): the shape seen from above (circular, irregular, filamentous, rhizoid), the margin (entire, undulate, lobate), the elevation (flat, raised, convex, umbonate), the surface (smooth or rough, mucoid if the cells make a capsule), the consistency and the pigment. *Serratia marcescens* makes the red pigment prodigiosin, *Pseudomonas aeruginosa* the blue-green pyocyanin and the fluorescent pyoverdine. Smooth and rough colonies often reflect differences in the cell surface, such as the presence or absence of a capsule in pneumococci or of the O-antigen of **lipopolysaccharide** in enteric bacteria. A culture is accepted as pure when its colonies are uniform, its cells look alike and stain alike under the microscope, and it gives no growth of contaminants on media designed to favor them.

### 4.5.3. Enrichment and the Competition for a Limiting Nutrient

An **enrichment culture** uses a medium and incubation conditions that favor the desired organism over all others in a natural sample. The principle was formulated by Sergei Winogradsky and Martinus Beijerinck at the end of the nineteenth century (7.11.1): to find an aerobic nitrogen fixer, inoculate soil into a mineral medium with mannitol as the carbon source and no fixed nitrogen, and incubate in air; *Azotobacter*, which fixes nitrogen fast in air, takes over. Every combination of electron donor, electron acceptor, carbon source, light, temperature, pH and salinity defines an enrichment, and most of the metabolic types of 7.11.6 and 7.11.7 were first isolated this way. The Winogradsky column, a column of mud and water in which gradients of oxygen and sulfide develop, is a long-lived enrichment for many of them at once (7.11.7).

An enrichment proves that an organism with the selected abilities was present, but a failed enrichment proves nothing, and the winner of an enrichment is not necessarily abundant or important in the habitat. In a liquid enrichment the winner is the organism that grows best under laboratory conditions, which are usually far richer than nature. A simple model makes this precise. In a chemostat ([7.6.39](/7.6.39#sec-39.1.3)) fed with medium containing a limiting substrate at concentration $S_0$ at dilution rate $D$, species $i$ grows at the Monod rate $\mu_i(S) = \mu_{\max,i}S/(K_{\mathrm{s},i} + S)$ ([Formula 39.1.1](/7.6.39#fml-39.1.1)), and

$$
\frac{\mathrm{d}N_i}{\mathrm{d}t} = \bigl(\mu_i(S) - D\bigr)N_i, \qquad \frac{\mathrm{d}S}{\mathrm{d}t} = D(S_0 - S) - \sum_i \frac{\mu_i(S)N_i}{Y_i},
$$
where $N_i$ is the biomass of species $i$ and $Y_i$ its yield coefficient (biomass formed per substrate consumed).

**Formula 4.5.1 (Break-Even Concentration)** A species can persist at dilution rate $D < \mu_{\max,i}$ only if the substrate stays at or above its break-even concentration

$$
R^*_i = \frac{K_{\mathrm{s},i}\,D}{\mu_{\max,i} - D},
$$
at which its growth rate equals the dilution rate. When several species compete for one limiting substrate, the one with the lowest $R^*$ draws the substrate down below the break-even concentrations of all others and excludes them.

This is the microbial form of the competitive exclusion principle, and chemostat competitions between bacterial strains have confirmed it. Its consequence for enrichment is that the outcome depends on the conditions as much as on the organisms. At a low dilution rate (low substrate supply), a species with a small $K_{\mathrm{s}}$, an oligotroph with high-affinity uptake systems such as ABC transporters, wins even if its maximal growth rate is modest; at a high dilution rate, or in a batch culture where the substrate is initially abundant, a species with a high $\mu_{\max}$ wins. Batch enrichments therefore favor fast-growing "weeds", and diluting the inoculum before enrichment, or enriching at low substrate concentrations, recovers organisms that are slower-growing but more abundant in nature.

![Competition for a single limiting substrate in a chemostat (Monod kinetics, simulated). Species A grows fast (μmax = 1.0 h⁻¹) but has a low affinity (Ks = 2 mg L⁻¹); species B grows slowly (μmax = 0.5 h⁻¹) with a high affinity (Ks = 0.2 mg L⁻¹); equal yields. A: the break-even concentration R* of each species as a function of the dilution rate D; the curves cross at D ≈ 0.44 h⁻¹. B: at D = 0.2 h⁻¹ the high-affinity species B excludes A. C: at D = 0.47 h⁻¹ the fast grower A excludes B. Both species start at the same biomass; the substrate concentration in the vessel (gray) settles at the R* of the winner.](./plots/chemostat-competition.py)

### 4.5.4. Single Cells and the Uncultured Majority

Isolation can also be done before growth, by separating single cells. Dilution to extinction, a serial dilution of a sample in liquid medium until only a few tubes or wells receive any cell, gives cultures that each start from about one cell and are free of faster competitors. Single cells can be picked under the microscope with micromanipulators or **optical tweezers**, sorted by flow cytometry into the wells of microtiter plates, or encapsulated in droplets or microchambers of microfluidic devices, in which thousands of cultivations run in parallel. High-throughput dilution culture in sterilized seawater brought into culture *Pelagibacter ubique*, a member of the SAR11 clade and one of the most abundant organisms in the ocean, which had resisted conventional enrichment.

These methods address a long-standing problem: the number of colonies that grow from a natural sample is typically a small fraction, often less than 1%, of the cells counted under the microscope, the **great plate count anomaly** (7.11.8). Many of the missing organisms need low nutrient concentrations, long incubations, growth factors made by other microorganisms, or partners with which they live in **syntrophy** (7.11.7). Devices that incubate single cells in diffusion chambers placed back in their natural habitat, such as the iChip, are discussed with the methods of microbial ecology in 7.11.29.

### 4.5.5. Culturing Anaerobes

Strict anaerobes are killed or inhibited by oxygen (the oxygen classes and their causes are in 7.11.9), so oxygen must be excluded from their media and handling:

- *Reducing media.* Media are boiled to drive out oxygen and supplemented with reducing agents such as thioglycolate, cysteine or sodium sulfide, which lower the redox potential; the redox indicator resazurin, pink when oxidized and colorless when reduced, shows whether a medium is anoxic. In a tube of thioglycolate broth, oxygen diffuses only into the top layer, so the position of growth in the tube shows the oxygen relationship of an organism.
- *Anaerobic jars.* Plates are incubated in a sealed jar in which a chemical sachet generates $\ce{H2}$ and $\ce{CO2}$ (or binds $\ce{O2}$ directly); a palladium catalyst combines the hydrogen with the remaining oxygen to form water.
- *Anaerobic chambers.* For extensive work, cultures are handled in a glove box filled with an oxygen-free gas mixture of nitrogen, hydrogen and carbon dioxide, again with a palladium catalyst to remove traces of oxygen.
- *The Hungate technique.* For the most oxygen-sensitive organisms, such as the cellulolytic bacteria of the rumen and methanogens, Robert Hungate developed around 1950 a method in which media are prepared, dispensed and inoculated under a stream of oxygen-free gas and incubated in sealed tubes; in the roll-tube variant, molten agar is spun to form a thin layer on the inside wall of the tube, on which colonies can be picked.

## Summary

- A bacterial cell is about 70% water; its dry mass is about half carbon and mostly protein and RNA (Section 4.1.1). Macronutrients (C, N, P, S, K, Mg, and Ca, Na, Fe for many) are needed in large amounts, trace elements and organic growth factors in minute amounts (Definition 4.1.1, Definition 4.1.2); the need for growth factors ranges from none (*E. coli*) to dozens (lactic acid bacteria).
- Nutritional classes combine three choices (Definition 4.2.1, Definition 4.2.2, Definition 4.2.3):

  | Energy source | Electron donor | Carbon source | Class |
  |---|---|---|---|
  | light | inorganic or organic | $\ce{CO2}$ | photoautotroph |
  | light | organic | organic | photoheterotroph |
  | inorganic chemical | inorganic | $\ce{CO2}$ | chemolithoautotroph |
  | inorganic chemical | inorganic | organic | mixotroph |
  | organic chemical | organic | organic | chemoorganoheterotroph |

- Transport into prokaryotic cells (Section 4.3):

  | System | Energy | Solute modified? | Components | Typical affinity |
  |---|---|---|---|---|
  | Porin (outer membrane) | none (diffusion) | no | trimeric β-barrel | none, size cutoff about 600 Da |
  | Simple transporter (symport, antiport) | proton-motive force or $\ce{Na+}$ gradient | no | one membrane protein | micromolar to millimolar |
  | ABC transporter | 2 ATP per solute | no | binding protein, 2 membrane domains, 2 ATPase domains | nanomolar to micromolar |
  | Phosphotransferase system (Definition 4.3.2) | PEP | yes, phosphorylated | Enzyme I, HPr, sugar-specific EIIA, EIIB, EIIC | micromolar |
  | Siderophore uptake (Definition 4.3.3) | proton-motive force via TonB, then ATP | no | outer-membrane receptor, TonB–ExbB–ExbD, binding protein, ABC transporter | extremely high ($\ce{Fe^3+}$) |

  The PTS also reports glucose availability through EIIA$^{\mathrm{Glc}}$ and underlies inducer exclusion and catabolite repression in *E. coli*.
- Media are defined or complex (Definition 4.4.1); selective, differential or enriched (Definition 4.4.2), as in blood, MacConkey, EMB and mannitol salt agar; liquid, solid (agar) or semisolid; and must be balanced in nutrients, pH, osmotic strength and redox potential (Section 4.4.4).
- Pure cultures are obtained by aseptic technique and streaking or dilution, and recognized by uniform colonies and cells (Section 4.5.1, Section 4.5.2). Enrichment selects by the conditions; in competition for a limiting nutrient the species with the lowest break-even concentration $R^* = K_{\mathrm{s}}D/(\mu_{\max} - D)$ wins (Formula 4.5.1), so low substrate supply favors high-affinity oligotrophs and rich media favor fast growers. Single-cell methods and low-nutrient, high-throughput cultures recover organisms missed by enrichment; anaerobes need reducing media, anaerobic jars or chambers, or the Hungate technique (Section 4.5.5).

## Questions

1. *E. coli* takes up lactose by lactose permease, glucose by the phosphotransferase system and maltose by an ABC transporter. For each, name the energy source and say what form the sugar has when it reaches the cytoplasm. Which system would you expect to work best when the sugar is at $50\,\mathrm{nM}$, and why?

   **Answer** Lactose permease: proton-motive force (one $\ce{H+}$ per lactose); lactose arrives unchanged. PTS: phosphoenolpyruvate, via Enzyme I, HPr, EIIA, EIIB; glucose arrives as glucose 6-phosphate. ABC transporter: two ATP per maltose; maltose arrives unchanged. At $50\,\mathrm{nM}$ the ABC system works best, because its periplasmic binding protein has nanomolar affinity and captures the sugar before it is delivered to the channel.

2. Classify by nutritional class: (a) a bacterium that oxidizes $\ce{H2S}$ to sulfate with $\ce{O2}$ and fixes $\ce{CO2}$; (b) a purple bacterium growing anoxically in the light on succinate; (c) *Saccharomyces cerevisiae* fermenting glucose; (d) a methanogen growing on $\ce{H2}$ and $\ce{CO2}$; (e) a sulfur oxidizer that takes its carbon from acetate.

   **Answer** (a) Chemolithoautotroph. (b) Photoheterotroph (light energy, organic carbon and electron donor). (c) Chemoorganoheterotroph. (d) Chemolithoautotroph: $\ce{H2}$ is the electron donor and energy source, $\ce{CO2}$ the carbon source (and the electron acceptor). (e) Mixotroph in the bacteriological sense.

3. A stool sample is plated on MacConkey agar. Explain why gram-positive bacteria do not grow, and what pink and colorless colonies tell you. Why is MacConkey agar useful in looking for *Salmonella*?

   **Answer** Bile salts and crystal violet inhibit gram-positive bacteria, so the medium is selective for gram-negative rods. Lactose fermenters acidify the medium around their colonies and the neutral red indicator turns them pink-red (*E. coli*, *Klebsiella*); colonies that do not ferment lactose stay colorless. *Salmonella* and *Shigella* do not ferment lactose, so their colorless colonies stand out among the pink colonies of the abundant normal *E. coli*, and can be picked for further tests.

4. Two strains compete for glucose in a chemostat: strain A with $\mu_{\max} = 0.8\,\mathrm{h^{-1}}$, $K_{\mathrm{s}} = 1\,\mathrm{mg\,L^{-1}}$ and strain B with $\mu_{\max} = 0.4\,\mathrm{h^{-1}}$, $K_{\mathrm{s}} = 0.1\,\mathrm{mg\,L^{-1}}$. Which wins at $D = 0.1\,\mathrm{h^{-1}}$ and at $D = 0.35\,\mathrm{h^{-1}}$? What does this imply for enrichment from seawater in a rich batch medium?

   **Answer** By Formula 4.5.1, at $D = 0.1$: $R^*_A = 0.1/0.7 = 0.14$, $R^*_B = 0.01/0.3 = 0.033\,\mathrm{mg\,L^{-1}}$, so B wins. At $D = 0.35$: $R^*_A = 0.35/0.45 = 0.78$, $R^*_B = 0.035/0.05 = 0.70\,\mathrm{mg\,L^{-1}}$, so B still wins, narrowly. The curves cross where $D/(0.8 - D) = 0.1D/(0.4 - D)$, that is $0.4 - D = 0.08 - 0.1D$, $D \approx 0.36\,\mathrm{h^{-1}}$; above it A wins, and B washes out altogether at $D = 0.4\,\mathrm{h^{-1}}$. A rich batch medium keeps the substrate far above both $K_{\mathrm{s}}$, where only $\mu_{\max}$ matters, so it selects fast growers like A and misses the high-affinity oligotrophs that dominate seawater.

5. Why can a bacterium not simply take up ferric iron through a porin, and how does the siderophore system solve the problem? Why do some bacteria carry receptors for siderophores they do not make?

   **Answer** Free $\ce{Fe^3+}$ at neutral pH and in air is about $10^{-18}\,\mathrm{M}$, too little to diffuse in at a useful rate, and in a host it is bound to transferrin and lactoferrin. A siderophore binds $\ce{Fe^3+}$ with an affinity high enough to dissolve ferric hydroxides and strip iron from host proteins; the complex, too large for porins, is taken up by a TonB-dependent outer-membrane receptor, a periplasmic binding protein and an ABC transporter, and the iron is released inside by reduction or hydrolysis. Receptors for foreign siderophores let a cell use complexes made by others without paying for their synthesis (cheating on a shared good).
