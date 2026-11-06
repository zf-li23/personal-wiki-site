---
title: Assimilation of Nitrogen, Sulfur, Phosphorus and Iron
description: Nitrogen in the environment and the fluxes of the nitrogen cycle; toxicity of ammonium and nitrate; the sites, electron donors and regulation of nitrate reductase and nitrite reductase; nitrate assimilation in roots and shoots, photoassimilation and inhibition by high CO₂; GS–GOGAT, glutamate dehydrogenase, transamination and the synthesis of amides; the physiology of symbiotic nitrogen fixation (the low-oxygen environment of the nodule, leghemoglobin, carbon cost, export of amides and ureides); activation and reduction of sulfate and the synthesis of cysteine; assimilation of phosphate; binding of cations to organic compounds; acquisition of iron (Strategy I and Strategy II); energetics of assimilation and nitrogen use efficiency.
source_hash: 92b133a918ac
---

Nitrate and sulfate taken up by roots are in a highly oxidized state, whereas the nitrogen and sulfur in proteins are highly reduced; converting the former into the latter is one of the most energy-demanding reactions in living organisms. Incorporating the nitrogen of one nitrate ion into glutamine takes about 12 ATP equivalents, reducing sulfate to cysteine about 14, and symbiotic nitrogen fixation together with ammonium assimilation about 16. The process of incorporating inorganic nutrients into organic compounds such as pigments, cofactors, lipids, nucleic acids and amino acids is called nutrient assimilation. This chapter treats in turn the assimilation of nitrogen, sulfur, phosphorus and cations (with emphasis on iron), and ends by comparing their energy costs. The biochemistry of nitrogen metabolism (the structure and mechanism of nitrogenase, the regulation of GS–GOGAT, the biosynthesis of amino acids) is covered in [7.1.27](/7.1.27), and the establishment of the symbiosis of legumes with rhizobia in [7.11.31](/7.11.31). Here we take the viewpoint of plant physiology: in which organ and compartment assimilation takes place, where the electrons and energy come from, what regulates it, and what all this means for plant growth and agriculture. How nutrients enter root cells is described in the previous chapter, [7.13.5](/7.13.5).

## 6.1. Nitrogen in the Environment

About 78% (by volume) of the atmosphere is $\ce{N2}$, but the triple bond $\ce{N#N}$ is extremely stable, and the great majority of organisms cannot use it directly. The conversion of $\ce{N2}$ to ammonia or nitrate is called **nitrogen fixation**, which is of two kinds, industrial and natural. In the industrial Haber–Bosch process, $\ce{N2}$ and $\ce{H2}$ are combined to ammonia at about $200\,^\circ\mathrm{C}$, about 200 atmospheres ($20\,\mathrm{MPa}$) and over an iron catalyst, and more than 110 million tonnes of nitrogen fertilizer are produced in this way worldwide each year. Natural processes fix about 190 million tonnes of nitrogen per year, of which lightning accounts for about 8% and photochemical reactions about 2%, and the remaining 90% is biological nitrogen fixation by bacteria and cyanobacteria. Once fixed, nitrogen passes through the **nitrogen cycle** in the soil in forms such as $\ce{NH4+}$ and $\ce{NO3-}$ ([7.1.27](/7.1.27#sec-27.1.1)) and finally returns to the atmosphere by denitrification. The main fluxes of the terrestrial nitrogen cycle (in $\mathrm{Tg\,N\,a^{-1}}$, $1\,\mathrm{Tg} = 10^{12}\,\mathrm{g}$) are:

| Process | Meaning | Flux / ($\mathrm{Tg\,N\,a^{-1}}$) |
|---|---|---|
| Industrial fixation | Haber–Bosch synthesis of ammonia | 100 |
| Atmospheric fixation | Formation of nitrate by lightning and photochemical reactions | 19 |
| Biological fixation | Reduction of $\ce{N2}$ to ammonia by prokaryotes | 170 |
| Plant uptake | Uptake and assimilation of ammonium and nitrate by plants | 1200 |
| Volatilization | Loss of ammonia gas from soil to the atmosphere | 100 |
| Ammonium fixation | Ammonium trapped in the clay lattice | 10 |
| Denitrification | Reduction of nitrate to $\ce{N2O}$ and $\ce{N2}$ by bacteria | 210 |
| Nitrate leaching | Flow with groundwater out of the topsoil and eventually into the sea | 36 |

(Data: Schlesinger 1997, quoted from Taiz 6e, Table 13.1.) The flux of plant uptake is several times larger than the sum of all fixation, showing that nitrogen cycles repeatedly among plants, animals and soil; dividing the size of the pool by the fixed input, a nitrogen atom stays in organic form for about 370 years on average. After fertilization the concentrations of ammonium and nitrate in soil are high, and root uptake may exceed assimilation capacity, so that they accumulate in tissues.

Accumulated ammonium and nitrate affect plants differently. High concentrations of $\ce{NH4+}$ are toxic to both plants and animals. On the more alkaline side (chloroplast stroma, mitochondrial matrix, cytosol), $\ce{NH4+}$ forms $\ce{NH3}$ with $\ce{OH-}$, which passes freely through membranes; $\ce{NH3}$ diffuses to the more acidic side (thylakoid lumen, intermembrane space, vacuole) and combines with $\ce{H+}$ to become $\ce{NH4+}$ again. The net result is that the pH gradients across the membranes are dissipated, whereas electron transport in photosynthesis and respiration, the compartmentation of metabolites by the vacuole and the transmembrane transport of nutrients all depend on these gradients. Plants therefore assimilate ammonium rapidly near the sites where it is absorbed or produced and store the excess in the vacuole. Nitrate, by contrast, can be stored in large amounts in the vacuole and is harmless in transport between tissues. But when humans and livestock eat plant material with a very high nitrate content, nitrate can be reduced to nitrite, which combines with hemoglobin and makes it unable to carry oxygen (methemoglobinemia), and nitrate may also be converted into carcinogenic nitrosamines, so many countries limit the nitrate content of vegetables.

## 6.2. Nitrate Assimilation

### 6.2.1. Nitrate Reductase

Roots take up nitrate through low-affinity and high-affinity $\ce{H+}$–$\ce{NO3-}$ symporters ([7.13.5](/7.13.5#sec-5.2.4)), and most of it is eventually assimilated into organic nitrogen. The oxidation number of nitrogen falls from $+5$ ($\ce{NO3-}$) through $+3$ ($\ce{NO2-}$) to $-3$ ($\ce{NH4+}$), requiring a total of 8 electrons, in two steps.

**Definition 6.2.1 (Nitrate Reductase)** **Nitrate reductase** (NR) is the enzyme that catalyzes the reduction of nitrate to nitrite; it is located in the cytosol:

$$
\ce{NO3- + NAD(P)H + H+ -> NO2- + NAD(P)+ + H2O}. \tag{6.1}
$$

Nitrate reductase of higher plants is a dimer of two identical subunits, each carrying three prosthetic groups: FAD, heme (cytochrome $b_{557}$) and molybdenum bound to pterin (the molybdenum cofactor, MoCo). Electrons enter the C-terminal FAD domain from NADH (or NADPH), pass through the heme domain to the N-terminal molybdenum cofactor, and there reduce nitrate. The most common form uses only NADH; another form, found mainly in nonphotosynthetic tissues such as roots, can use NADH or NADPH. NADH comes from glycolysis and respiration; in leaves, photorespiration promotes the export of malate from the chloroplast, and malate is oxidized in the cytosol to produce NADH, supplying electrons for nitrate reduction. Nitrate reductase is the main molybdenum-containing protein of vegetative tissue, and one symptom of molybdenum deficiency is the accumulation of nitrate.

### 6.2.2. Regulation of Nitrate Reductase

Nitrate reductase is regulated by nitrate, light and sugars, at the levels of transcription, translation and post-translational modification:

- Induction: nitrate reductase is a typical inducible enzyme (a substrate-inducible enzyme, also called an adaptive enzyme in Chinese textbooks), and nitrate induces its synthesis. In barley seedlings the mRNA of nitrate reductase is detectable about 40 minutes after nitrate is added and peaks at 3 hours; enzyme activity rises more slowly and linearly, because protein synthesis presupposes the presence of the mRNA. Light and sugars also promote its expression; the end products of assimilation, glutamine and asparagine, inhibit the induction of nitrite reductase by nitrate.
- Post-translational regulation: darkness and $\ce{Mg^2+}$ activate a protein kinase that phosphorylates a serine residue in the "hinge 1" region between the two domains of nitrate reductase, and the phosphorylated enzyme binds the 14-3-3 inhibitor protein and is inactivated; light, sugars and other factors activate a phosphatase, and dephosphorylation restores the activity of the enzyme. This regulation is completed within minutes, much faster than synthesis or degradation of the enzyme (hours), so that nitrate reduction can be switched on and off rapidly in step with the reducing power and carbon skeletons supplied by photosynthesis, avoiding accumulation of toxic nitrite.

Because its activity changes sensitively with nitrogen nutrition and metabolic state, the nitrate reductase activity of leaves can be used as a physiological indicator in the diagnosis of crop nitrogen nutrition. Screening resistant mutants with chlorate ($\ce{ClO3-}$, an analog of nitrate that nitrate reductase reduces to toxic chlorite) yields mutants defective in nitrate transport or reduction; NRT1.1 (CHL1) was identified in this way.

### 6.2.3. Nitrite Reductase

Nitrite is highly reactive and potentially toxic; as soon as it is formed it is transported into the chloroplast (in leaves) or the proplastid (in roots) for further reduction.

**Definition 6.2.2 (Nitrite Reductase)** **Nitrite reductase** (NiR) is the enzyme in chloroplasts and root plastids that catalyzes the reduction of nitrite to ammonium, receiving 6 electrons from reduced **ferredoxin**:

$$
\ce{NO2- + 6 Fd_{red} + 8 H+ -> NH4+ + 6 Fd_{ox} + 2 H2O}. \tag{6.2}
$$

Nitrite reductase is a single polypeptide containing one iron–sulfur cluster ($\ce{Fe4S4}$) and a special heme (siroheme); the two together bind and reduce nitrite, intermediate nitrogen compounds do not accumulate, but 0.02%–0.2% of the nitrite is released as the greenhouse gas $\ce{N2O}$. It is encoded in the nucleus, synthesized in the cytosol and carries an N-terminal transit peptide that directs it to the plastid; nitrate and light induce its transcription. In leaves, reduced ferredoxin comes directly from photosynthetic electron transport (photosystem I, [7.1.24](/7.1.24)); in nonphotosynthetic tissues such as roots, NADPH produced in the oxidative stage of the **pentose phosphate pathway** reduces ferredoxin through ferredoxin–NADP⁺ reductase.

### 6.2.4. Nitrate Assimilation in Roots and Shoots

**Definition 6.2.3 (Nitrate Assimilation)** The whole process by which a plant reduces absorbed nitrate to ammonium by nitrate reductase and nitrite reductase and then incorporates it into amino acids is called *nitrate assimilation*.

Both roots and shoots can assimilate nitrate, and the partitioning between them varies with species and nitrate supply. Many plants reduce nitrate mainly in the root when the supply is low; as the supply increases, more nitrate is carried through the xylem to the shoot for reduction. Comparing the ratio of nitrate to reduced nitrogen (amino acids, amides, ureides) in xylem sap shows this division of labor: nitrate metabolism in cocklebur (*Xanthium strumarium*) takes place only in the shoot, and xylem sap is almost entirely nitrate; most nitrate in white lupin (*Lupinus albus*) is metabolized in the root, and the sap consists mainly of amides and amino acids; in general, species of temperate origin depend more on root assimilation than species of tropical or subtropical origin.

One advantage of nitrate assimilation in leaves is that it can use the reducing power of the light reactions directly: in the chloroplast stroma, assimilation reactions have NADPH, thioredoxin and reduced ferredoxin close at hand. This coupling of nutrient assimilation with photosynthetic electron transport is called *photoassimilation*. Photoassimilation takes place in the same compartment as C3 carbon fixation, and occurs on a large scale only when photosynthetic electron transport produces more reducing power than the **Calvin cycle** needs (as in strong light or low $\ce{CO2}$). High $\ce{CO2}$ therefore inhibits nitrate assimilation in the shoots of C3 plants: $\ce{CO2}$ competes with nitrate for reducing power, and high $\ce{CO2}$ also suppresses **photorespiration**, reducing the malate export driven by photorespiration and thus the NADH available for nitrate reduction. Contrary to the usual impression that photorespiration is wasteful, this shows that photorespiration plays a positive role in the carbon–nitrogen relations of plants. In C4 plants the first carboxylation in the cytosol of mesophyll cells produces large amounts of malate and NADH, so nitrate assimilation in C4 shoots is unaffected by $\ce{CO2}$ concentration and occurs only in mesophyll cells. With atmospheric $\ce{CO2}$ steadily rising, the grain protein content of C3 crops such as wheat has already begun to decline, and strengthening the assimilation of ammonium and nitrate in roots may be one breeding strategy.

![Assimilation of nitrate and ammonium in a mesophyll cell. $\ce{NO3-}$ from the xylem enters the cell through $\ce{H+}$ symporters (NRT) and is reduced in the cytosol to $\ce{NO2-}$ by nitrate reductase (NR) using two electrons from NADH; $\ce{NO2-}$ enters the chloroplast and is reduced to $\ce{NH4+}$ by nitrite reductase (NiR) using 6 reduced ferredoxin (Fd); $\ce{NH4+}$ (together with $\ce{NH4+}$ released in photorespiration) is incorporated into glutamate by glutamine synthetase GS (consuming ATP) to give glutamine, and glutamate synthase (Fd-GOGAT) transfers the amide group of glutamine to 2-oxoglutarate, producing two glutamate; glutamate supplies amino groups for other amino acids through aminotransferases (such as aspartate aminotransferase, Asp-AT), and asparagine synthetase (AS) forms asparagine for transport. Yellow boxes are the approximate cost of each step (ATP equivalents, from Taiz 6e, Fig. 13.20): NRT 1, NR 3, NiR 7 (including transport), GS/GOGAT 2, AS 2.](./plots/nitrogen-assimilation.py)

## 6.3. Ammonium Assimilation

### 6.3.1. The GS–GOGAT Pathway

Plants rapidly convert ammonium, whether from nitrate reduction, photorespiration or direct uptake from the soil, into amino acids, mainly through the sequential action of **glutamine synthetase** (GS) and **glutamate synthase** (GOGAT) (mechanism and regulation in [7.1.27](/7.1.27#sec-27.1.3)):

$$
\text{glutamate} + \ce{NH4+} + \ce{ATP} \to \text{glutamine} + \ce{ADP} + \mathrm{P_i}, \tag{6.3}
$$

$$
\text{glutamine} + \text{2-oxoglutarate} + 2\,\mathrm{Fd_{red}}\ (\text{or NADH} + \ce{H+}) \to 2\,\text{glutamate} + 2\,\mathrm{Fd_{ox}}\ (\text{or } \ce{NAD+}). \tag{6.4}
$$

Together, the two steps consume one ATP and two electrons per $\ce{NH4+}$ incorporated and produce one net glutamate. GS requires $\ce{Mg^2+}$, $\ce{Mn^2+}$ or $\ce{Co^2+}$ as cofactor and has a very high affinity for ammonium, which keeps free ammonium in tissues at a low level. Plants have distinct isoenzymes of GS and of GOGAT with a clear division of labor:

| Enzyme | Location | Function | Regulation |
|---|---|---|---|
| GS1 (cytosolic) | Germinating seeds, roots and the vascular bundles of shoots | Synthesis of glutamine for intercellular nitrogen transport | Little influence of light and sugars |
| GS2 (plastidic) | Root plastids, chloroplasts | In roots, synthesis of amide nitrogen for local use; in leaves, reassimilation of $\ce{NH4+}$ released in photorespiration | Regulated by light and sugars |
| Fd-GOGAT | Chloroplasts (also in root plastids under nitrate nutrition) | Nitrogen metabolism of photorespiration; in roots, assimilation of glutamine produced from nitrate reduction | Protein amount and activity increase with light |
| NADH-GOGAT | Plastids of roots and other nonphotosynthetic tissues, vascular bundles of developing leaves | Assimilation of $\ce{NH4+}$ taken up from the rhizosphere; assimilation of glutamine transported from roots or senescing leaves | |

The flux of $\ce{NH4+}$ released by photorespiration in the leaves of C3 plants (when glycine is converted to serine) is roughly an order of magnitude greater than primary nitrate assimilation, and almost all this ammonium is reassimilated by GS2 and Fd-GOGAT in the chloroplast; mutants lacking these two enzymes survive only at high $\ce{CO2}$ (which suppresses photorespiration).

### 6.3.2. Glutamate Dehydrogenase

Glutamate dehydrogenase (GDH) catalyzes a reversible reaction that can both synthesize glutamate and deaminate it:

$$
\text{2-oxoglutarate} + \ce{NH4+} + \mathrm{NAD(P)H} \rightleftharpoons \text{glutamate} + \ce{H2O} + \ce{NAD(P)+}. \tag{6.5}
$$

Mitochondria contain an NADH-dependent GDH and chloroplasts an NADPH-dependent GDH, both in considerable amounts; but GDH has a very low affinity for ammonium ($K_{\mathrm{m}}$ in the millimolar range) and could take part in assimilation only at very high ammonium concentrations, so it cannot replace the GS–GOGAT pathway. Its main function is to deaminate glutamate in the redistribution of nitrogen, for example in seed germination, leaf senescence and carbohydrate shortage, delivering the carbon skeletons of amino acids to the tricarboxylic acid cycle.

### 6.3.3. Transamination and Amides

After nitrogen has been incorporated into glutamine and glutamate, it enters other amino acids by **transamination**; the **aminotransferases** that catalyze these reactions all use pyridoxal phosphate (vitamin $\mathrm{B_6}$) as cofactor and are found in the cytosol, chloroplasts, mitochondria, glyoxysomes and peroxisomes. For example, aspartate aminotransferase transfers the amino group of glutamate to oxaloacetate:

$$
\text{glutamate} + \text{oxaloacetate} \to \text{2-oxoglutarate} + \text{aspartate}. \tag{6.6}
$$

Aspartate takes part in the malate–aspartate shuttle and in C4 plants also carries carbon from mesophyll to bundle sheath. After leaves or isolated chloroplasts are exposed to $\ce{^{14}CO2}$, the label rapidly enters glutamate, aspartate, alanine, serine and glycine, showing that the chloroplast is an important site of amino acid synthesis. The carbon skeletons of the various amino acids come from 3-phosphoglycerate, phosphoenolpyruvate and pyruvate of glycolysis and from 2-oxoglutarate and oxaloacetate of the tricarboxylic acid cycle. Plants can synthesize all 20 protein amino acids, including the essential amino acids that animals must obtain from food; the enzymes that synthesize these amino acids are absent in animals and are therefore ideal herbicide targets (for example, glyphosate inhibits EPSP synthase of the shikimate pathway).

Two amides, glutamine and asparagine, are especially important in plants and are the main forms of nitrogen transport and storage. Asparagine is formed by asparagine synthetase, which transfers the amide nitrogen of glutamine to aspartate:

$$
\text{glutamine} + \text{aspartate} + \ce{ATP} \to \text{glutamate} + \text{asparagine} + \ce{AMP} + \mathrm{PP_i}. \tag{6.7}
$$

Asparagine is stable and has a high N:C ratio (2 N : 4 C, against 2 N : 5 C for glutamine and 1 N : 5 C for glutamate), using little carbon, which suits long-distance transport and long-term storage; it was the first amide isolated, from asparagus in 1806. GS, GOGAT and asparagine synthetase are regulated in opposite ways, balancing the carbon and nitrogen metabolism of the plant. When light is strong and sugars abundant (ample energy), plastidic GS and Fd-GOGAT are promoted, the expression and activity of asparagine synthetase are inhibited, and nitrogen goes mainly into the carbon-rich glutamine and glutamate for the synthesis of new material; when energy is short the reverse holds, GS and GOGAT are inhibited, asparagine synthetase is promoted, and nitrogen is stored or transported as the nitrogen-rich, stable asparagine.

## 6.4. The Physiology of Symbiotic Nitrogen Fixation

### 6.4.1. Nitrogen-Fixing Organisms and Symbiotic Systems

Biological nitrogen fixation is catalyzed by the **nitrogenase** of prokaryotes (structure and mechanism in [7.1.27](/7.1.27#sec-27.1.2)), with the overall reaction

$$
\ce{N2 + 8 e- + 8 H+ + 16 ATP -> 2 NH3 + H2 + 16 ADP + 16 P_i}. \tag{6.8}
$$

Nitrogen-fixing prokaryotes include free-living ones and ones living symbiotically with plants. The free-living forms include aerobic *Azotobacter*, facultative *Klebsiella*, anaerobic *Clostridium* and photosynthetic bacteria, and cyanobacteria. The symbiotic forms are mainly legumes with **rhizobia** (*Rhizobium*, *Bradyrhizobium*, *Sinorhizobium* and others); actinorhizal plants such as alder and *Casuarina* with *Frankia*; *Azolla* with *Anabaena*; *Gunnera* with *Nostoc*; and C4 grasses such as sugarcane with endophytic or root-surface nitrogen-fixing bacteria (no nodules are formed, and endophytes in the stem apoplast of sugarcane may supply about 30% of the host's nitrogen). In Asian rice fields, cyanobacteria and the *Azolla*–*Anabaena* symbiosis are important nitrogen sources, the latter fixing up to $0.5\,\mathrm{kg}$ of nitrogen per hectare per day. The exchange of signals by which legumes and rhizobia form **root nodules** (flavonoids, NodD, **Nod factors**, LysM receptor kinases, nuclear calcium oscillations) and the infection process are described in [7.11.31](/7.11.31#sec-31.2.2); a "common symbiosis signaling pathway" is shared with arbuscular mycorrhizae. Here we deal only with the physiology of the nodule as a nitrogen-fixing organ.

### 6.4.2. Oxygen in the Nodule

Nitrogenase is irreversibly inactivated by $\ce{O2}$ with great ease (the half-life of the Fe protein in air is 30–45 s and that of the MoFe protein about 10 min), yet nitrogen fixation requires large amounts of ATP, which can be supplied only by aerobic respiration. The nodule resolves this contradiction with three mechanisms:

- A diffusion barrier: the nodule endodermis contains a layer of tissue with few intercellular spaces and variable gas permeability, so that free $\ce{O2}$ in the central infected zone is only $20$–$40\,\mathrm{nmol\,L^{-1}}$, about one ten-thousandth of that of air-saturated water (about $250\,\mu\mathrm{mol\,L^{-1}}$). The permeability increases in light and decreases in drought or on exposure to nitrate; the mechanism is not clear and may involve $\ce{K+}$ fluxes in infected cells.
- **Leghemoglobin**: the most abundant protein in infected cells, which makes active nodules pink. Its affinity for $\ce{O2}$ is very high ($K_{\mathrm{m}}$ about $10\,\mathrm{nmol\,L^{-1}}$, roughly tenfold higher than that of the human hemoglobin β chain). It was formerly thought to be an oxygen buffer, but the $\ce{O2}$ it binds would sustain nodule respiration for only a few seconds; its main role is to speed the diffusion of $\ce{O2}$ to the bacteroids (facilitated diffusion) at very low free $\ce{O2}$ concentrations.
- A high-affinity terminal oxidase: the respiratory chain of the **bacteroid** uses a terminal oxidase with an even higher affinity for $\ce{O2}$ than leghemoglobin ($K_{\mathrm{m}}$ about $7\,\mathrm{nmol\,L^{-1}}$), so that it can still synthesize ATP at such low oxygen concentrations.

![Physiology of a legume nodule (schematic). A: free $\ce{O2}$ concentration along the nodule radius (logarithmic scale, qualitative profile): near air saturation in the outer cortex (about $250\,\mu\mathrm{mol\,L^{-1}}$), falling steeply across the variable diffusion barrier of the endodermis (gray), and only $20$–$40\,\mathrm{nmol\,L^{-1}}$ in the central infected zone. B: exchange of materials in an infected cell: sucrose delivered by the phloem is broken down and converted to malate through PEP carboxylase, which supplies the bacteroids in the symbiosome; nitrogenase reduces $\ce{N2}$ to $\ce{NH3}$ (consuming 16 ATP and 8 electrons per $\ce{N2}$ and releasing 1 $\ce{H2}$); $\ce{NH3}$/$\ce{NH4+}$ crosses the symbiosome membrane and is assimilated by GS–GOGAT in the cytosol and plastids of the host cell; temperate legumes export amides (asparagine, glutamine) and tropical legumes export ureides through the xylem. Red dots indicate leghemoglobin in the cytosol.](./plots/nodule-exchange.py)

### 6.4.3. Exchange of Carbon and Nitrogen and the Cost of Fixation

The plant supplies carbon and energy to the bacteroids as dicarboxylic acids (mainly malate): sucrose is broken down in infected cells and converted to malate through PEP carboxylase and malate dehydrogenase, and a dicarboxylate transporter in the symbiosome membrane delivers it to the bacteroids. The bacteroids release the fixed $\ce{NH3}$ into the symbiosome space, from which it crosses the symbiosome membrane as $\ce{NH4+}$ or $\ce{NH3}$ into the host cell and is assimilated by GS–GOGAT, avoiding ammonium toxicity.

The cost of nitrogen fixation is high. By Eq. (6.8), reducing one $\ce{N2}$ requires 16 ATP and 8 electrons, 2 of which are necessarily used to reduce $2\ce{H+}$ to $\ce{H2}$; in rhizobia, 30%–60% of the energy supplied to nitrogenase is in fact lost as $\ce{H2}$. Some rhizobia have a nickel-containing uptake hydrogenase that oxidizes the $\ce{H2}$ released and recovers the electrons, raising the efficiency of fixation. The turnover number of nitrogenase is very low (only about 5 $\ce{N2}$ reduced per second), so bacteroids synthesize large amounts of nitrogenase, up to 20% of total cell protein. From the carbohydrate metabolism of legumes, plant respiration consumes about 9.3 mol of $\ce{CO2}$ per mole of $\ce{N2}$ fixed. Nitrogenase can also reduce acetylene to ethylene, a reaction used to measure nitrogenase activity (the acetylene reduction assay).

**Example 6.4.1** Converting the carbon cost of fixation. Each mole of $\ce{N2}$ ($28\,\mathrm{g}$ of nitrogen) consumes the respiratory carbon of $9.3\,\mathrm{mol}$ of $\ce{CO2}$, that is $9.3 \times 12 = 112\,\mathrm{g}$ of carbon, or about $4.0\,\mathrm{g}$ of carbon per gram of nitrogen. If the growth and maintenance of the nodule are included, estimates are often $6$–$12\,\mathrm{g}$ of carbon per gram of nitrogen ([Example 27.1.1 of 7.1.27](/7.1.27#ex-27.1.1)). When a soybean plant fixes $3\,\mathrm{g}$ of nitrogen in a season, fixation alone consumes about $12\,\mathrm{g}$ of carbon, equivalent to $30\,\mathrm{g}$ of sucrose; so when soil nitrate is plentiful, legumes reduce nodulation and fixation, and nitrate also lowers the $\ce{O2}$ permeability of nodules, assimilating ready-made nitrogen being "cheaper".

### 6.4.4. Export of Amides and Ureides

Organic nitrogen synthesized in the nodule is carried to the shoot in the xylem. By the composition of xylem sap, nitrogen-fixing legumes fall into two classes: legumes of temperate origin such as pea (*Pisum*), clover (*Trifolium*), faba bean (*Vicia*) and lentil (*Lens*) export amides (mainly asparagine or glutamine); legumes of tropical origin such as soybean (*Glycine*), common bean (*Phaseolus*), peanut (*Arachis*) and cowpea (*Vigna*) export ureides, mainly allantoin, allantoic acid and citrulline. Allantoin is formed in peroxisomes from uric acid derived from purine degradation, and allantoic acid is formed from allantoin in the endoplasmic reticulum. Allantoin and allantoic acid carry one nitrogen per carbon atom in the molecule ($\ce{C4H6N4O3}$, N : C = 1) and are the most carbon-economical forms of nitrogen transport. After arriving in the shoot these compounds are rapidly broken down to ammonium and enter the GS–GOGAT assimilation pathway.

## 6.5. Sulfate Assimilation

### 6.5.1. Sources of Sulfur

Most of the sulfur in plants comes from sulfate taken up by roots through $\ce{H+}$–$\ce{SO4^2-}$ symporters. Sulfate in soil comes mainly from weathering of the parent rock; $\ce{SO2}$ and $\ce{H2S}$ released by burning fossil fuels enter the soil with rain and are another source that has increased since industrialization. $\ce{SO2}$ reacts in the atmosphere with hydroxyl radicals and oxygen to form $\ce{SO3}$, which dissolves in water to give sulfuric acid, the main component of acid rain. Plants can also take up gaseous $\ce{SO2}$ through stomata and metabolize it, but prolonged exposure (over 8 h) to high concentrations (above 0.3 ppm) of $\ce{SO2}$ seriously injures tissue through the formation of sulfuric acid.

### 6.5.2. Activation and Reduction of Sulfate

The oxidation number of sulfur falls from $+6$ ($\ce{SO4^2-}$) to $-2$ (sulfur in cysteine), requiring a total of 8 electrons. Sulfate is very stable and must first be activated. The first step is catalyzed by ATP sulfurylase, in which sulfate replaces the pyrophosphate of ATP to give adenosine 5′-phosphosulfate (APS):

$$
\ce{SO4^2- + ATP -> APS + PP_i}. \tag{6.9}
$$

This reaction is thermodynamically very unfavorable and is driven by rapid conversion of the products: pyrophosphate is hydrolyzed to $2\,\mathrm{P_i}$ by inorganic pyrophosphatase, and APS is rapidly reduced or phosphorylated. Activating one sulfate therefore actually consumes two high-energy phosphate bonds of ATP (ATP → AMP). ATP sulfurylase is mainly in plastids, with a little in the cytosol.

Reduction of APS is the main pathway and takes place entirely in the plastid:

$$
\ce{APS + 2 GSH -> SO3^2- + 2 H+ + GSSG + AMP}, \tag{6.10}
$$

$$
\ce{SO3^2- + 6 Fd_{red} -> S^2- + 6 Fd_{ox}}. \tag{6.11}
$$

APS reductase receives 2 electrons from reduced glutathione (GSH) and forms sulfite; sulfite reductase receives 6 electrons from reduced ferredoxin and forms sulfide; it is homologous with nitrite reductase and likewise contains siroheme and an iron–sulfur cluster. Sulfide then reacts with O-acetylserine (OAS) to form cysteine. OAS is formed mainly in mitochondria, where serine acetyltransferase acetylates serine with acetyl-CoA; most cysteine is synthesized in the cytosol by O-acetylserine (thiol) lyase, also called cysteine synthase:

$$
\text{serine} + \text{acetyl-CoA} \to \text{OAS} + \text{CoA}, \qquad \text{OAS} + \ce{S^2-} \to \text{cysteine} + \text{acetate}. \tag{6.12}
$$

(Chinese textbooks sometimes call the latter enzyme "acetylserine sulfhydrylase", a name that is not accurate for the reaction: it does not catalyze sulfation but adds sulfide to OAS.) The reduction of sulfate to cysteine consumes about 14 ATP equivalents in all. Another pathway is the phosphorylation of APS by APS kinase to 3′-phosphoadenosine 5′-phosphosulfate (PAPS), from which cytosolic sulfotransferases transfer the sulfate group to choline, brassinosteroids, flavonols, glucosinolates, peptides and polysaccharides, forming sulfated metabolites; the oxidation state of the sulfur is unchanged. Methionine is synthesized from cysteine in plastids; cysteine and methionine are used in turn to synthesize proteins, glutathione, coenzyme A, S-adenosylmethionine (substrate of ethylene synthesis and of methyl transfer reactions) and others. Glutathione is also the precursor of **phytochelatins**, which chelate heavy metals such as cadmium.

The sulfate assimilation activity of leaves is generally much higher than that of roots, because photosynthesis supplies reduced ferredoxin and photorespiration produces serine, promoting the synthesis of OAS. Sulfur assimilated in leaves is carried in the phloem, mainly as glutathione, to shoot tips, root tips and fruits where protein synthesis is vigorous; glutathione is also a signal that coordinates sulfate uptake by roots with assimilation in the shoot. In *Arabidopsis*, apart from sulfite reductase and glutathione synthetase, the enzymes of sulfur assimilation are encoded by small multigene families.

## 6.6. Phosphate Assimilation

Roots take up phosphate through $\ce{H+}$–$\ce{H2PO4-}$ (or $\ce{HPO4^2-}$) symporters (the high-affinity PHT1 family, with $K_{\mathrm{m}}$ of $1$–$5\,\mu\mathrm{mol\,L^{-1}}$, [7.13.5](/7.13.5#sec-5.2.4)). Unlike nitrogen and sulfur, phosphorus is not reduced in the plant and always remains as phosphate with oxidation number $+5$, so assimilation is the incorporation of phosphate into organic compounds. The main entry is the synthesis of ATP: oxidative phosphorylation in mitochondria (energized by oxidation of NADH or succinate), photophosphorylation in chloroplasts, and substrate-level phosphorylation of glycolysis in the cytosol, in which inorganic phosphate is first incorporated into 1,3-bisphosphoglycerate in the glyceraldehyde-3-phosphate dehydrogenase reaction, forming a high-energy acyl phosphate that is then transferred to ADP to make ATP. Once phosphate groups are in ATP, they are transferred through many reactions into the various phosphate compounds such as sugar phosphates, phospholipids and nucleotides. The phosphate translocator in the chloroplast inner membrane exchanges inorganic phosphate for phosphorylated carbon compounds such as triose phosphate, coupling the export of photosynthate to the cycling of phosphorus ([7.13.8](/7.13.8), [7.13.11](/7.13.11)).

Phosphorus in the plant occupies several pools: metabolic phosphorus in the cytosol is kept relatively constant, the vacuole is the reservoir of inorganic phosphate, and in seeds phosphorus is stored as the calcium and magnesium salt of phytate (inositol hexaphosphate), which is broken down by phytase on germination. Available phosphorus in soil is often insufficient ([7.13.4](/7.13.4#sec-4.4.1)), and plants have a series of adaptations to phosphorus deficiency: induction of the expression of high-affinity phosphate transporters; secretion of acid phosphatases and organic acids to release phosphorus from organic phosphorus and sparingly soluble phosphates; an increase in lateral roots and root hairs and formation of cluster roots; strengthened symbiosis with arbuscular mycorrhizal fungi; and partial replacement of phospholipids in membranes by sulfolipids and galactolipids, freeing phosphorus for more essential uses.

## 6.7. Assimilation of Cations and Acquisition of Iron

### 6.7.1. Binding of Cations to Organic Compounds

The cations of macronutrients such as potassium, magnesium and calcium, and of micronutrients such as copper, iron, manganese, cobalt, sodium and zinc, taken up by plants are "assimilated" by binding to organic compounds through noncovalent bonds, in two ways:

- Coordination bonds: several oxygen or nitrogen atoms in the organic compound donate lone pairs to form bonds with the cation, and the positive charge of the cation is neutralized. Polyvalent cations are often bound in this way, for example the complex of copper with tartrate and the coordination of magnesium by the four nitrogen atoms of the chlorophyll porphyrin ring. Copper, zinc, iron and magnesium are all assimilated as coordination complexes.
- Electrostatic bonds: a positively charged cation and a negatively charged group (such as a carboxyl group $\ce{-COO-}$) attract each other, and the cation keeps its positive charge. The monovalent $\ce{K+}$ can form electrostatic complexes with the carboxyl groups of organic acids (such as potassium malate), but most of the $\ce{K+}$ accumulated in cells is present as free ion in the cytosol and vacuole, where it acts in osmotic regulation and enzyme activation. The divalent $\ce{Ca^2+}$ forms cross-links between parallel pectin chains (the "egg-box" model of calcium pectate), which is both coordination and electrostatic interaction and is the main form in which calcium is bound in the cell wall.

### 6.7.2. Acquisition of Iron: Strategy I and Strategy II

Iron in soil is present mainly as oxides and hydroxides of $\ce{Fe^3+}$ ($\ce{Fe(OH)2+}$, $\ce{Fe(OH)3}$, $\ce{Fe(OH)4-}$) and is extremely insoluble at neutral pH. From the solubility product of $\ce{Fe(OH)3}$ (about $10^{-39}$) one can estimate $[\ce{Fe^3+}] = K_{\mathrm{sp}}/[\ce{OH-}]^3$; at pH 7, $[\ce{OH-}] = 10^{-7}\,\mathrm{mol\,L^{-1}}$ and free $\ce{Fe^3+}$ is only about $10^{-18}\,\mathrm{mol\,L^{-1}}$; each unit rise in pH lowers the solubility 1000-fold. Even when the various hydroxy complexes are included, inorganic iron in neutral soil solution is far below what plants need for growth (about $10^{-8}$–$10^{-6}\,\mathrm{mol\,L^{-1}}$). Roots have evolved two strategies to raise the solubility and availability of iron.

Strategy I (dicots and nongrass monocots, such as pea, tomato, soybean and *Arabidopsis*):

1. Acidification of the rhizosphere: the plasma membrane $\ce{H+}$-ATPase (mainly AHA2 in *Arabidopsis*) extrudes more protons into the rhizosphere in iron deficiency, raising the solubility of $\ce{Fe^3+}$.
2. Secretion of chelators: roots secrete malate, citrate, phenolics (including coumarins), piscidic acid and others, which form soluble chelates with $\ce{Fe^3+}$.
3. Reduction: the ferric chelate reductase of the plasma membrane (FRO2 in *Arabidopsis*, a transmembrane flavocytochrome) uses cytosolic NAD(P)H as electron donor to reduce $\ce{Fe^3+}$ to the much more soluble $\ce{Fe^2+}$, which also releases iron from the chelate; its activity increases in iron deficiency, and mutants lacking FRO2 soon become chlorotic.
4. Uptake: IRT1, a transporter of the ZIP family, carries $\ce{Fe^2+}$ into epidermal cells; it can also transport zinc, manganese and cadmium (one route by which cadmium enters crops), and *Arabidopsis* lacking IRT1 dies unless iron is supplied.

Strategy II (grasses, such as barley, maize, oat, wheat and rice):

**Definition 6.7.1 (Phytosiderophore)** The nonprotein amino acids secreted by the roots of grasses that form highly stable, soluble chelates with $\ce{Fe^3+}$ are called **phytosiderophores** (mugineic acid-family phytosiderophores). They are synthesized from methionine via nicotianamine and include mugineic acid, 2′-deoxymugineic acid and avenic acid.

In iron deficiency, the roots of grasses secrete large amounts of phytosiderophores into the rhizosphere through the efflux transporter TOM1 (often with a pronounced diurnal rhythm, peaking in the morning); these chelate $\ce{Fe^3+}$, and the resulting Fe(III)–phytosiderophore complexes are taken up whole by YS1-type transporters in the plasma membrane of root epidermal cells (first identified from the yellow stripe mutant *ys1* of maize). The function of phytosiderophores is less affected by pH than the reductase of Strategy I, so grasses are generally less prone to iron deficiency than dicots on calcareous soils; the amounts secreted differ greatly among grass species (high in barley, low in rice), consistent with their tolerance of iron deficiency. Rice also has some features of Strategy I: in iron deficiency it increases expression of IRT-type transporters, taking up the $\ce{Fe^2+}$ abundant in flooded soil. Phytosiderophores differ chemically from the **siderophores** secreted by microorganisms but are similar in function.

![The two strategies by which roots acquire iron (schematic). A: Strategy I (dicots and nongrass monocots): the plasma membrane $\ce{H+}$-ATPase (AHA2) acidifies the rhizosphere, and roots secrete chelators such as malate, citrate and coumarins that dissolve $\ce{Fe(OH)3}$ in the soil; the ferric chelate reductase FRO2 reduces $\ce{Fe^3+}$ to $\ce{Fe^2+}$ with electrons from cytosolic NADPH; IRT1 of the ZIP family takes up $\ce{Fe^2+}$. B: Strategy II (grasses): mugineic acid-family phytosiderophores (PS), synthesized from methionine via nicotianamine, are secreted through TOM1 and chelate $\ce{Fe^3+}$; the Fe(III)–PS complex is taken up whole by YS1-type transporters. Both mechanisms are induced in iron deficiency.](./plots/iron-strategies.py)

### 6.7.3. Transport and Assimilation of Iron in the Plant

Iron taken up by roots is oxidized to $\ce{Fe^3+}$ in cells, and most of it is carried to the leaves in the xylem as an electrostatic complex with citrate; in the phloem and between cells, iron is transported mainly bound to nicotianamine. In leaves iron undergoes an important assimilation reaction: ferrochelatase inserts $\ce{Fe^2+}$ into the porphyrin ring of protoporphyrin, forming the heme groups of the cytochromes of chloroplasts and mitochondria; most of the iron in the plant is in heme. The nonheme iron of iron–sulfur proteins is bound covalently to the sulfur of cysteine residues, and there are also $\ce{Fe2S2}$ centers containing two iron atoms and two inorganic sulfurs.

Free iron not bound to organic compounds reacts with oxygen to form the extremely destructive hydroxyl radical ($\cdot\ce{OH}$, the Fenton reaction), so excess iron is stored in ferritin: 24 identical subunits form a hollow shell of about 480 kDa, within which is an iron oxide–phosphate core of several thousand iron atoms. Studies of *Arabidopsis* mutants show that ferritin is necessary to prevent oxidative damage but is not the main iron pool for seedling development or the normal operation of photosynthetic organs. The level of free iron in the cell regulates the synthesis of ferritin. The iron bound to ferritin may be readily absorbed by the human body, so ferritin-rich foods (such as soybean) have attracted attention: iron deficiency is the most common human nutritional deficiency worldwide, and raising the iron and zinc content of the edible parts of crops (biofortification) is an important goal of nutrition and breeding.

## 6.8. Energetics of Assimilation and Nitrogen Use Efficiency

Converting stable, low-energy, highly oxidized inorganic compounds into high-energy, highly reduced organic compounds requires a great deal of energy. The table and figure below compare the cost of several assimilation processes (ATP equivalents per N or S atom incorporated):

| Process | Number of electrons | Main electron source | ATP equivalents |
|---|---|---|---|
| $\ce{NH4+}$ → glutamate (GS–GOGAT) | 2 | Fd or NADH | about 2 (uptake not counted) |
| $\ce{NO3-}$ → glutamate (uptake + NR + NiR + GS–GOGAT) | 10 | NADH (NR), Fd (NiR, GOGAT) | about 12–13 |
| $\ce{N2}$ → amide nitrogen (symbiotic fixation + assimilation) | 4 (per N, including $\ce{H2}$) | Respiration of the bacteroid | about 16 |
| $\ce{SO4^2-}$ → cysteine | 8 | GSH (APS reductase), Fd (sulfite reductase) | about 14 |

The numbers of electrons follow from the changes in oxidation number: $+5 \to -3$ for nitrate gives 8, plus 2 for GOGAT; $+6 \to -2$ for sulfate gives 8; reducing $\ce{N2}$ to $2\ce{NH3}$ needs 6 electrons, plus the 2 that inevitably go to $\ce{H2}$, which is 4 per N. Different textbooks account for the ATP equivalents differently (for example, whether transmembrane transport is counted and whether one NAD(P)H is taken as 2.5 or 3 ATP), and the numbers differ (compare [Example 27.1.1 of 7.1.27](/7.1.27#ex-27.1.1)), but the order of magnitude is unchanged: using ammonium is the cheapest in energy, while reducing nitrate and sulfate and symbiotic fixation are all expensive.

![Energy cost of nutrient assimilation (per N or S atom incorporated; approximate values from Chapter 13 of Taiz 6e). A: ATP equivalents: ammonium incorporated into glutamate through GS–GOGAT about 2; nitrate to glutamate about 13 (uptake 1, nitrate reduction 3, nitrite reduction 7, GS–GOGAT 2); symbiotic fixation plus assimilation about 16 (per amide nitrogen); sulfate to cysteine about 14. B: the number of electrons required, from the change in oxidation number.](./plots/assimilation-energy.py)

The reduction of nitrate to ammonium consumes about 25% of the total energy expenditure of roots and shoots: a plant may spend a quarter of its energy on assimilating an element that makes up less than 2% of its dry weight. Many assimilation reactions take place in the chloroplast stroma and can use the reducing power produced by photosynthetic electron transport directly (photoassimilation), which lowers the cost compared with respiratory energy supply.

**Example 6.8.1** Comparing the cost of two nitrogen sources. A plant has 2% nitrogen in its dry matter, that is $20\,\mathrm{mg}$ of nitrogen per gram of dry matter, or $20/14.0 = 1.43\,\mathrm{mmol}$ N. If all of it is supplied as nitrate and assimilated in the root with respiratory energy, assimilation needs about $1.43 \times 12.5 = 18\,\mathrm{mmol}$ of ATP; taking about 30 ATP per glucose in aerobic respiration, this is equivalent to $0.60\,\mathrm{mmol}$ of glucose, or about $0.11\,\mathrm{g}$ of glucose per gram of dry matter. If it is supplied as ammonium, about $1.43 \times 2 = 2.9\,\mathrm{mmol}$ of ATP is needed, consuming only about $0.017\,\mathrm{g}$ of glucose. Synthesizing 1 g of plant dry matter requires about 1.2–1.5 g of glucose in all, so with respiratory energy supply nitrate assimilation can account for about 7%–9% of the plant carbon budget, and ammonium only about 1%. This explains why tissues short of carbohydrate, such as meristems, use ammonium preferentially ([7.13.4](/7.13.4#sec-4.5.2)); but ammonium nutrition is toxic and acidifies the rhizosphere, and most crops grow best when both nitrogen sources are present.

Nitrogen is the nutrient that is applied in the largest amounts in crop production and is also lost in the largest amounts: crops generally recover less than half of the nitrogen fertilizer applied, and the rest enters the environment by leaching, volatilization and denitrification (which produces the potent greenhouse gas $\ce{N2O}$). The ability of a crop to use nitrogen is commonly measured by *nitrogen use efficiency*, the grain yield produced per unit of nitrogen supplied:

$$
\mathrm{NUE} = \frac{G_{\mathrm{w}}}{N_{\mathrm{s}}} = \frac{N_{\mathrm{t}}}{N_{\mathrm{s}}} \times \frac{G_{\mathrm{w}}}{N_{\mathrm{t}}},
$$

where $G_{\mathrm{w}}$ is grain yield, $N_{\mathrm{s}}$ is the nitrogen supply (soil plus fertilizer), and $N_{\mathrm{t}}$ is the total nitrogen taken up by the plant. The right-hand side splits it into nitrogen uptake efficiency (the fraction of supplied nitrogen taken up, depending on the root system, transporters and fertilization method) and nitrogen internal utilization efficiency (grain produced per unit of nitrogen taken up, depending on assimilation, remobilization and harvest index). For example, with a nitrogen supply of $200\,\mathrm{kg\,ha^{-1}}$, plant uptake of $120\,\mathrm{kg\,ha^{-1}}$ and a grain yield of $7.2\,\mathrm{t\,ha^{-1}}$, the uptake efficiency is 0.60, the internal utilization efficiency is $60\,\mathrm{kg}$ grain per kg N, and NUE $= 36\,\mathrm{kg}$ grain per kg N. Improving these two components is the main route to reducing fertilizer inputs and environmental costs.

## Summary

| Nutrient | Form taken up | Key steps and enzymes of assimilation | Site | Electron source | Cost (ATP equivalents) |
|---|---|---|---|---|---|
| Nitrate | $\ce{NO3-}$ ($\ce{H+}$ symport) | Nitrate reductase (Definition 6.2.1; FAD, heme, MoCo) → nitrite reductase (Definition 6.2.2; $\ce{Fe4S4}$, siroheme) → GS–GOGAT | NR in cytosol; NiR, GS2, GOGAT in chloroplast or root plastid | NADH; Fd (leaf: light reactions; root: pentose phosphate pathway) | about 12–13 |
| Ammonium | $\ce{NH4+}$ (AMT) | GS (ATP) + GOGAT; GDH mainly deaminates; transamination; asparagine synthetase | GS1 cytosol (vascular tissue, seeds), GS2 plastid | Fd (leaf), NADH (root) | about 2 |
| $\ce{N2}$ (symbiotic) | — | Nitrogenase (16 ATP, 8 e⁻, 1 $\ce{H2}$) → host GS–GOGAT → export of amides or ureides | Bacteroids in infected cells of the nodule | Malate supplied by the plant | about 16; over 4 g C / g N |
| Sulfate | $\ce{SO4^2-}$ ($\ce{H+}$ symport); $\ce{SO2}$ through stomata | ATP sulfurylase → APS reductase (GSH) → sulfite reductase (Fd) → OAS (thiol) lyase → cysteine | Mainly leaf plastids; exported as glutathione | GSH, Fd | about 14 |
| Phosphate | $\ce{H2PO4-}$ ($\ce{H+}$ symport, PHT1) | Not reduced; incorporated into ATP by oxidative phosphorylation, photophosphorylation and substrate-level phosphorylation | Mitochondria, chloroplasts, cytosol | — | — |
| Iron | Strategy I: $\ce{Fe^2+}$; Strategy II: Fe(III)–phytosiderophore | Acidification + FRO2 reduction + IRT1; phytosiderophore (Definition 6.7.1) + YS1; ferrochelatase insertion into porphyrin; storage in ferritin | Root surface; chloroplast | NAD(P)H (FRO2) | — |

Distinctions:

| Term | Meaning | Do not confuse with |
|---|---|---|
| Nitrate reductase | Cytosol, 2 e⁻, NAD(P)H | Nitrite reductase (plastid, 6 e⁻, Fd) |
| GOGAT | Glutamine + 2-oxoglutarate → 2 glutamate | GDH (low affinity, mainly deaminating) |
| Amides | Asparagine, glutamine: exported by temperate legumes | Ureides (allantoin, allantoic acid): exported by tropical legumes |
| Leghemoglobin | Speeds diffusion of $\ce{O2}$ to bacteroids | Not a large-capacity buffer of $\ce{O2}$ |
| Phytosiderophore | Mugineic acid family secreted by grasses | Microbial siderophores (catechol and hydroxamate types) |
| Photoassimilation | Assimilation using the reducing power of the light reactions | Photorespiration (supplies NADH for nitrate reduction) |

Main equations:

| Equation | Meaning |
|---|---|
| $\ce{NO3- + NAD(P)H + H+ -> NO2- + NAD(P)+ + H2O}$, Eq. (6.1) | Nitrate reduction (2 e⁻) |
| $\ce{NO2- + 6 Fd_{red} + 8 H+ -> NH4+ + 6 Fd_{ox} + 2 H2O}$, Eq. (6.2) | Nitrite reduction (6 e⁻) |
| Eqs. (6.3), (6.4) | GS–GOGAT: 1 ATP + 2 e⁻ per $\ce{NH4+}$ |
| $\ce{N2 + 8 e- + 8 H+ + 16 ATP -> 2 NH3 + H2 + 16 ADP + 16 P_i}$, Eq. (6.8) | Nitrogen fixation |
| Eqs. (6.9)–(6.12) | Sulfate → APS → sulfite → sulfide → cysteine (8 e⁻) |
| $[\ce{Fe^3+}] = K_{\mathrm{sp}}/[\ce{OH-}]^3$ | Iron solubility falls 1000-fold per unit rise in pH |
| $\mathrm{NUE} = (N_{\mathrm{t}}/N_{\mathrm{s}})(G_{\mathrm{w}}/N_{\mathrm{t}})$ | Nitrogen use efficiency = uptake efficiency × internal utilization efficiency |

## Questions

1. Why is nitrate reductase in the cytosol and nitrite reductase in the plastid? What is the advantage of this separation?

   **Answer** Nitrate reduction needs only 2 electrons, which cytosolic NADH (from glycolysis and from the malate export driven by photorespiration) can supply; nitrite reduction needs 6 low-potential electrons, supplied by reduced ferredoxin, which is reduced directly by photosystem I in the chloroplast and by NADPH of the pentose phosphate pathway through FNR in root plastids, so nitrite reductase must be located in the plastid. Nitrite is toxic and reactive; after it is formed it is transported straight into the plastid and reduced, continuously with ammonium assimilation (GS2, GOGAT) in the same compartment, so that the concentration of the toxic intermediate stays very low. Having nitrate reductase in the cytosol also allows rapid regulation by phosphorylation and 14-3-3, so that nitrate reduction is synchronized with the reducing power and carbon skeletons produced by photosynthesis.

2. (Calculation) A leaf in light assimilates $\ce{CO2}$ at $5\,\mu\mathrm{mol\,m^{-2}\,s^{-1}}$ while reducing nitrite in the chloroplast and assimilating it through GS–GOGAT at $0.5\,\mu\mathrm{mol\,m^{-2}\,s^{-1}}$. How much reduced ferredoxin is needed per second per square meter? If the Calvin cycle needs 2 NADPH (4 electrons) per $\ce{CO2}$ fixed, what fraction of the sum of the electrons is consumed by nitrogen assimilation?

   **Answer** Nitrite reduction needs 6 Fd per N (Eq. (6.2)) and Fd-GOGAT 2 Fd per N (Eq. (6.4)), 8 in all: $0.5 \times 8 = 4\,\mu\mathrm{mol\,m^{-2}\,s^{-1}}$ of reduced ferredoxin (each Fd carries 1 electron). Carbon fixation needs $5 \times 4 = 20\,\mu\mathrm{mol}$ of electrons $\mathrm{m^{-2}\,s^{-1}}$. Nitrogen assimilation accounts for $4/(4 + 20) = 17\,\%$. (Nitrate reduction in the cytosol needs a further $0.5\,\mu\mathrm{mol}$ of NADH, that is 1 µmol of electrons.) This shows that photoassimilation of nitrogen competes with carbon fixation for the reducing power of the light reactions; at high $\ce{CO2}$ the Calvin cycle consumes more reducing power, which is one reason for the inhibition of nitrate assimilation in the shoots of C3 plants.

3. (Calculation) Estimate the concentration of free $\ce{Fe^3+}$ in soils of pH 6 and pH 8 using $K_{\mathrm{sp}}(\ce{Fe(OH)3}) = 10^{-39}$. By what factor do they differ? What does this mean for understanding iron-deficiency chlorosis in calcareous soils and the advantage of Strategy II?

   **Answer** At pH 6: $[\ce{OH-}] = 10^{-8}$, $[\ce{Fe^3+}] = 10^{-39}/10^{-24} = 10^{-15}\,\mathrm{mol\,L^{-1}}$; at pH 8: $[\ce{OH-}] = 10^{-6}$, $[\ce{Fe^3+}] = 10^{-39}/10^{-18} = 10^{-21}\,\mathrm{mol\,L^{-1}}$, a difference of $10^6$-fold (1000-fold per pH unit). Calcareous soils often have pH 7.5–8.5 and the solubility of inorganic iron is extremely low; Strategy I plants depend on acidifying the rhizosphere and on reduction, but high pH and the $\ce{HCO3-}$ in the soil both neutralize the protons extruded and inhibit the activity of FRO2, so dicots such as fruit trees readily show iron-deficiency chlorosis; the phytosiderophores secreted by grasses have extremely high binding constants for $\ce{Fe^3+}$ and are little affected by pH, so grasses can obtain iron in such soils.

4. Legumes reduce nodulation and nitrogen fixation when soil nitrate is plentiful. Explain this in terms of energy and carbon cost, and explain why tropical legumes export fixed nitrogen as ureides rather than amides.

   **Answer** Symbiotic fixation costs about 16 ATP equivalents per amide nitrogen (Eq. (6.8) plus assimilation), the plant must also supply malate to the bacteroids, consuming over 4 g of carbon per gram of nitrogen, plus the growth and maintenance of the nodule; absorbing and assimilating nitrate costs about 12–13 ATP equivalents, and in leaves the reducing power of the light reactions can be used, so not everything has to be supplied by respiration. When ready-made nitrate is available, assimilating it is therefore cheaper, and nitrate also lowers the $\ce{O2}$ permeability of nodules and inhibits nodulation (autoregulation, [7.11.31](/7.11.31#sec-31.2.4)). Ureides (allantoin $\ce{C4H6N4O3}$) have N : C = 1, more economical in carbon than asparagine (1 : 2) and glutamine (2 : 5), using the least carbon skeleton per nitrogen transported; tropical legumes grow in hot environments with strong respiration, where carbon is costly, and transporting nitrogen as ureides saves photosynthate.

5. (Calculation) A wheat field has a nitrogen supply (soil plus fertilizer) of $250\,\mathrm{kg\,ha^{-1}}$; at harvest the shoot has taken up $160\,\mathrm{kg\,ha^{-1}}$ of nitrogen and the grain yield is $8.0\,\mathrm{t\,ha^{-1}}$. Find the nitrogen uptake efficiency, internal utilization efficiency and nitrogen use efficiency. If split fertilization raises the uptake efficiency to 0.75 while the internal utilization efficiency is unchanged, by how much can yield rise at the same nitrogen supply?

   **Answer** Uptake efficiency $= 160/250 = 0.64$; internal utilization efficiency $= 8000/160 = 50\,\mathrm{kg}$ grain per kg N; NUE $= 8000/250 = 32\,\mathrm{kg\,kg^{-1}}$ ($= 0.64 \times 50$). When the uptake efficiency rises to 0.75, nitrogen uptake is $0.75 \times 250 = 187.5\,\mathrm{kg\,ha^{-1}}$ and yield is $187.5 \times 50 = 9.4\,\mathrm{t\,ha^{-1}}$, an increase of about 17%; or, keeping the yield at $8.0\,\mathrm{t\,ha^{-1}}$, the nitrogen supply need only be $160/0.75 = 213\,\mathrm{kg\,ha^{-1}}$, about $37\,\mathrm{kg}$ of nitrogen less. In practice the internal utilization efficiency falls as nitrogen uptake increases (diminishing returns, [7.13.4](/7.13.4#sec-4.3.2)), so this estimate is optimistic.
