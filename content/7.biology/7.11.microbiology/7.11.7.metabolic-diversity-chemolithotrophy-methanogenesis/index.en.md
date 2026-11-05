---
title: "Metabolic Diversity II: Chemolithotrophy, Anaerobic Respiration and Methanogenesis"
description: Energy from inorganic electron donors (hydrogen, sulfur, iron, ammonia, nitrite, anammox), respiration with nitrate, sulfate, metals and other acceptors, the one-carbon metabolisms of acetogens, methanogens and methanotrophs, syntrophy and the Winogradsky column.
---

A respiring cell needs only two things: an electron donor and an electron acceptor whose reduction potentials are far enough apart to pay for ATP. Animals use one pair, organic carbon and oxygen. Bacteria and archaea use almost every pair that the chemistry of the Earth's surface offers: hydrogen, sulfide, ferrous iron, ammonia and nitrite as donors; nitrate, manganese and iron oxides, sulfate, sulfur, carbon dioxide and many organic compounds as acceptors. This chapter surveys these metabolisms from the standpoint of energy, building on the redox thermodynamics of [7.1.16](/7.1.16#sec-16.4) and on the respiratory chains of [7.11.5](/7.11.5). It follows on from [7.11.6](/7.11.6), which treated light and the pathways of autotrophy, and prepares the element cycles of [7.11.30](/7.11.30), where the same reactions reappear as global fluxes. The organisms themselves are described in the diversity chapters, [7.11.17](/7.11.17)–[7.11.19](/7.11.19).

## 7.1. Respiration Defined by Donor and Acceptor

### 7.1.1. Energy from Redox Couples

A redox reaction is the sum of two half-reactions; the couple with the more negative $E'^{\circ}$ is oxidized, and the free energy released is

$$
\Delta_{\mathrm{r}}G'^{\circ} = -zF\,\Delta E'^{\circ}, \qquad \Delta E'^{\circ} = E'^{\circ}_{\text{acceptor}} - E'^{\circ}_{\text{donor}},
$$
where $z$ is the number of electrons transferred and $F = 96.485\,\mathrm{kJ\,mol^{-1}\,V^{-1}}$ ([Formula 16.4.1](/7.1.16#sec-16.4.4)). Comparing reactions per electron, or per two electrons, removes the arbitrariness of the stoichiometry and shows directly how much energy each electron carries down the respiratory chain. The actual Gibbs energy in the cell differs from $\Delta_{\mathrm{r}}G'^{\circ}$ by $RT\ln Q$, which matters greatly when one product is kept at very low concentration (7.5).

How much energy does a cell need? Synthesizing ATP in vivo costs about $50$–$60\,\mathrm{kJ\,mol^{-1}}$ (the phosphorylation potential, [7.1.16](/7.1.16#sec-16.3.2)); with 3–4 protons per ATP, translocating one proton is worth about $15$–$20\,\mathrm{kJ\,mol^{-1}}$. A reaction that releases about $-20\,\mathrm{kJ}$ per turnover can therefore just pump one ion and is often quoted as the minimum on which an organism can live, although slowly growing anaerobes appear to subsist on somewhat less.

![Energy available from inorganic electron donors and from the alternative electron acceptors. A: standard transformed Gibbs energy per two electrons for chemolithotrophic reactions (aerobic reactions after Madigan et al. 2019; the anaerobic H₂ reactions from the standard values in the text). The dashed line marks about −20 kJ, the smallest energy change per reaction that is commonly estimated to be usable. Oxidations of H₂ and sulfur compounds release much more energy than those of nitrite, ammonium or ferrous iron, and H₂ yields far less with sulfate or CO₂ than with O₂. B: the electron-acceptor ladder, ΔG'° for the complete oxidation of one acetate (8 electrons, E'° of CO₂/acetate −0.29 V) with each acceptor; the bars for manganese and iron oxides depend on the mineral (range bars). The order from top to bottom is the order in which the acceptors are used up with depth in sediments.](./plots/redox-energetics.py)

### 7.1.2. Assimilatory and Dissimilatory Reduction

Nitrate, sulfate and $\ce{CO2}$ are reduced by almost all microorganisms in small amounts to make cell material. Only some use them as electron acceptors for energy conservation, and the two processes must be distinguished.

**Definition 7.1.1 (Assimilatory and Dissimilatory Reduction)** In **assimilatory reduction** an inorganic compound (nitrate, sulfate, $\ce{CO2}$) is reduced, at the expense of energy, only as far as needed for biosynthesis, and the product (an amino or sulfhydryl group, organic carbon) is incorporated into cell material. In **dissimilatory reduction** the compound serves as the terminal electron acceptor of an **anaerobic respiration**: large amounts are reduced, energy is conserved, and the product ($\ce{N2}$, $\ce{N2O}$, $\ce{NH4+}$, $\ce{H2S}$, $\ce{CH4}$, acetate) is excreted.

The enzymes differ as well: assimilatory nitrate reductase is cytoplasmic and repressed by ammonium, dissimilatory nitrate reductase is membrane-bound and repressed by $\ce{O2}$; assimilatory sulfate reduction proceeds through phosphoadenosine phosphosulfate, dissimilatory through adenosine phosphosulfate (7.3.3).

### 7.1.3. The Price of Being a Chemolithoautotroph

A **chemolithotroph** conserves energy by oxidizing an inorganic compound; most chemolithotrophs are also autotrophs and fix $\ce{CO2}$, usually by the Calvin cycle, while some (**mixotrophy**) take carbon from organic compounds. Autotrophy needs NAD(P)H. Only $\ce{H2}$ ($-0.41\,\mathrm{V}$) and a few other donors are negative enough to reduce $\ce{NAD+}$ directly; electrons from sulfide, thiosulfate, nitrite, ammonia and ferrous iron enter the respiratory chain at the level of quinones or cytochromes and must be pushed up to $\ce{NAD+}$ by reverse electron transport ([Definition 6.2.2](/7.11.6#def-6.2.2)). The burden falls hardest on the weakest donors.

**Example 7.1.1** A nitrite oxidizer obtains electrons at $E'^{\circ}(\ce{NO3-}/\ce{NO2-}) = +0.43\,\mathrm{V}$ and passes them to $\ce{O2}$ ($+0.82\,\mathrm{V}$), releasing $2F \times 0.39 \approx 74\,\mathrm{kJ}$ per nitrite. To reduce one $\ce{NAD+}$ ($-0.32\,\mathrm{V}$) it must raise two electrons by $0.75\,\mathrm{V}$, which costs $2F \times 0.75 \approx 145\,\mathrm{kJ}$, the free energy of about two nitrites. One turn of the Calvin cycle per $\ce{CO2}$ needs 2 NAD(P)H and 3 ATP; at about $55\,\mathrm{kJ}$ per ATP the minimum is $2 \times 145 + 3 \times 55 \approx 455\,\mathrm{kJ}$, or six to seven nitrites per $\ce{CO2}$ at perfect efficiency, before any energy is spent on growth. Real efficiencies are far below this ideal, which is why nitrifiers and iron oxidizers grow slowly and produce little biomass for the amount of substrate they turn over.

## 7.2. Chemolithotrophy

### 7.2.1. Hydrogen Oxidation

Hydrogen is a product of many fermentations and of geochemistry (serpentinization, radiolysis), and the "hydrogen bacteria" (Knallgas bacteria) oxidize it with $\ce{O2}$:

$$
\ce{H2 + 1/2 O2 -> H2O}, \qquad \Delta_{\mathrm{r}}G'^{\circ} = -237\,\mathrm{kJ\,mol^{-1}}.
$$

**Definition 7.2.1 (Hydrogenase)** A **hydrogenase** is an enzyme that catalyzes the reversible oxidation of molecular hydrogen, $\ce{H2 <=> 2 H+ + 2 e-}$. Hydrogenases are classified by the metals of their active site into [NiFe]-, [FeFe]- and [Fe]-hydrogenases; [NiFe] enzymes predominate in $\ce{H2}$ uptake, [FeFe] enzymes in $\ce{H2}$ production by fermenters.

The model organism *Cupriavidus necator* (formerly *Ralstonia eutropha*) has two [NiFe] hydrogenases: a membrane-bound enzyme that feeds electrons into the quinone pool and so into the respiratory chain, and a soluble enzyme that reduces $\ce{NAD+}$ directly for the Calvin cycle; both are unusually $\ce{O2}$-tolerant. Hydrogen bacteria are facultative chemolithotrophs: in the presence of organic substrates they repress hydrogenases and the Calvin cycle and grow as chemoorganotrophs, an adaptation to the fact that $\ce{H2}$ is fleeting in oxic environments, where it is consumed by anaerobes before it can diffuse up. Many soil bacteria (actinobacteria, for example) have high-affinity hydrogenases that scavenge the trace $\ce{H2}$ of the atmosphere (about 0.5 ppm) and use it to survive starvation; this soil sink removes most of the atmospheric $\ce{H2}$.

### 7.2.2. Oxidation of Reduced Sulfur Compounds

Sulfide, elemental sulfur, thiosulfate and sulfite are oxidized, usually to sulfate, by the "colorless sulfur bacteria" (as opposed to the pigmented phototrophic sulfur bacteria of [7.11.6](/7.11.6)). It was in sulfur bacteria (*Beggiatoa*) that Sergei Winogradsky discovered chemolithotrophy in the 1880s, the idea that life can draw its energy from an inorganic reaction.

| Reaction | Electrons | $\Delta_{\mathrm{r}}G'^{\circ}$ (kJ per reaction) | kJ per 2 e⁻ |
|---|---|---|---|
| $\ce{HS- + H+ + 1/2 O2 -> S^0 + H2O}$ | 2 | −209.4 | −209 |
| $\ce{S^0 + 3/2 O2 + H2O -> SO4^2- + 2 H+}$ | 6 | −587.1 | −196 |
| $\ce{H2S + 2 O2 -> SO4^2- + 2 H+}$ | 8 | −798.2 | −200 |
| $\ce{S2O3^2- + H2O + 2 O2 -> 2 SO4^2- + 2 H+}$ | 8 | −818.3 | −205 |

Values after Madigan et al. (2019). Every oxidation of sulfur to sulfate releases protons, so sulfur oxidizers acidify their environment, and many are acidophiles: *Acidithiobacillus thiooxidans* grows at pH 1–2, and the archaeon *Sulfolobus* at pH 2–3 and 80 °C.

Two biochemical strategies exist. In the Sox system (best studied in *Paracoccus pantotrophus*), a set of periplasmic enzymes binds the sulfur compound covalently to a carrier protein (SoxYZ) and oxidizes it all the way to sulfate without free intermediates, feeding the electrons into cytochrome *c*. Organisms that store sulfur, such as *Beggiatoa* and the purple and green sulfur bacteria, lack the key enzyme SoxCD; they deposit $\ce{S^0}$ as globules and later oxidize it in the cytoplasm with a reverse-acting dissimilatory sulfite reductase (rDsr) and APS reductase, which yields one ATP by substrate-level phosphorylation per sulfite (via ATP sulfurylase run backwards).

Sulfide oxidizers live where sulfide from below meets oxygen or nitrate from above, and the larger ones have striking adaptations to this gradient:

- *Beggiatoa* forms white mats of gliding filaments at the sediment surface, tracking the narrow zone where both $\ce{O2}$ and $\ce{H2S}$ are present.
- *Thiomargarita namibiensis*, from the sediments off Namibia, has cells up to about 0.75 mm in diameter, most of whose volume is a vacuole storing nitrate at about 0.8 M; it can oxidize stored sulfur with stored nitrate for months while buried. *Thiomargarita magnifica* (described in 2022), with filamentous cells up to about 2 cm long, is the largest bacterium known.
- *Achromatium* contains calcite inclusions as well as sulfur globules.
- *Thiobacillus denitrificans* and many marine sulfur oxidizers use nitrate instead of $\ce{O2}$ and so couple the sulfur and nitrogen cycles; the cable bacteria (7.3.4) solve the problem of separated donor and acceptor electrically.

### 7.2.3. Iron Oxidation

The aerobic oxidation of ferrous iron yields very little energy, and at neutral pH $\ce{Fe^2+}$ is oxidized spontaneously by $\ce{O2}$ within minutes, leaving little for microorganisms. Iron oxidizers therefore live in two kinds of habitat.

In acidic waters (pH below about 3) ferrous iron is stable in air, and acidophiles such as *Acidithiobacillus ferrooxidans*, *Leptospirillum ferrooxidans* (Nitrospirota) and the archaeon *Ferroplasma* oxidize it:

$$
\ce{2 Fe^2+ + 1/2 O2 + 2 H+ -> 2 Fe^3+ + H2O}, \qquad \Delta_{\mathrm{r}}G \approx -33\,\mathrm{kJ}\ \text{per}\ \ce{Fe^2+}\ \text{at pH 2}.
$$
At pH 2 the $\ce{Fe^3+}/\ce{Fe^2+}$ couple is at $+0.77\,\mathrm{V}$, close to $\ce{O2}/\ce{H2O}$, so the electron transport chain is very short: an outer-membrane cytochrome *c* oxidizes $\ce{Fe^2+}$, the periplasmic copper protein rusticyanin passes the electron to cytochrome *c* and cytochrome $aa_3$, which reduces $\ce{O2}$. The large natural proton gradient across the membrane (periplasm pH 1–2, cytoplasm about 6.5) drives ATP synthase, but the protons that enter must be consumed by $\ce{O2}$ reduction, so the cell can use the gradient only while it oxidizes iron. NADH for the Calvin cycle is made by reverse electron transport from a very positive potential, the most expensive case of all; a cell must oxidize large amounts of iron to make a little biomass, and these bacteria are noticed by the ochre $\ce{Fe(OH)3}$ precipitates they leave rather than by their numbers. Their role in **acid mine drainage** and in the industrial leaching of metal ores is treated in [7.11.30](/7.11.30).

At neutral pH, iron oxidizers such as *Gallionella* and the marine *Mariprofundus ferrooxydans* (Zetaproteobacteria) live at oxic–anoxic interfaces, where $\ce{Fe^2+}$-rich groundwater or vent fluid meets traces of $\ce{O2}$, and outcompete the abiotic reaction at low $\ce{O2}$; they excrete their oxidized iron as twisted organic stalks or sheaths, which keeps the cell from being encrusted. Under anoxic conditions $\ce{Fe^2+}$ is oxidized with nitrate by some chemolithotrophs and with light by photoferrotrophs ([7.11.6](/7.11.6#sec-6.2.6)).

### 7.2.4. Nitrification

**Definition 7.2.2 (Nitrification)** **Nitrification** is the aerobic oxidation of ammonia to nitrite and of nitrite to nitrate by chemolithotrophic microorganisms. In most environments it is carried out in two steps by two groups: ammonia oxidizers (bacteria, genera usually named *Nitroso*-, and archaea) and nitrite oxidizers (bacteria, *Nitro*-).

The ammonia-oxidizing bacteria (AOB, *Nitrosomonas*, *Nitrosospira*; Betaproteobacteria and Gammaproteobacteria) oxidize ammonia in two steps:

$$
\ce{NH3 + O2 + 2 H+ + 2 e- -> NH2OH + H2O}\ \ (\text{AMO}), \qquad \ce{NH2OH + H2O -> NO2- + 5 H+ + 4 e-}\ \ (\text{HAO}).
$$
Ammonia monooxygenase (AMO), a copper membrane enzyme related to the particulate methane monooxygenase (7.4.3), inserts one oxygen atom from $\ce{O2}$ and needs two electrons; hydroxylamine oxidoreductase (HAO) in the periplasm releases four. Two of these four electrons therefore return to AMO, and only two reach the terminal oxidase and pump protons. With $E'^{\circ}(\ce{NO2-}/\ce{NH4+}) = +0.34\,\mathrm{V}$, the overall reaction $\ce{NH4+ + 3/2 O2 -> NO2- + 2 H+ + H2O}$ yields $-275\,\mathrm{kJ}$ (6 electrons), and the nitrite oxidizers (*Nitrobacter*, *Nitrospira*, *Nitrococcus*), using nitrite oxidoreductase (NXR), only $-74\,\mathrm{kJ}$ per nitrite. Both groups fix $\ce{CO2}$ by the Calvin cycle, except *Nitrospira*, which uses the reverse citric acid cycle.

Two discoveries changed this picture.

- Ammonia-oxidizing archaea (AOA) of the Nitrososphaerota (formerly Thaumarchaeota) were first recognized from metagenomes and isolated in 2005 (*Nitrosopumilus maritimus*). They have an archaeal AMO and a copper-based electron transport chain, fix $\ce{CO2}$ with the 3HP/4HB cycle ([7.11.6](/7.11.6#sec-6.5.4)), and have a far higher affinity for ammonia than AOB; they make up a large fraction of the prokaryotes of the deep ocean and outnumber AOB in most soils.
- Complete ammonia oxidizers were found in 2015 in the genus *Nitrospira* (Definition 7.2.3).

**Definition 7.2.3 (Comammox)** **Comammox** (complete ammonia oxidation) is the oxidation of ammonia all the way to nitrate by a single organism, found in bacteria of the genus *Nitrospira*, which carry both AMO/HAO and NXR.

Thermodynamic arguments had predicted it: a complete oxidizer gains more energy per ammonia ($-349\,\mathrm{kJ}$, 8 electrons) and should be favoured where growth is slow and substrate scarce, as in biofilms and drinking-water filters, where comammox *Nitrospira* are indeed common.

Nitrification makes nitrate, the nitrogen form most easily leached from soils, and is the first step of nitrogen removal in wastewater treatment; nitrifiers are also a significant source of nitrous oxide.

### 7.2.5. Anaerobic Ammonium Oxidation

For a long time ammonium was thought to be inert in the absence of $\ce{O2}$. In the 1990s, a denitrifying wastewater reactor in Delft was found to lose ammonium and nitrite together, and the organism responsible turned out to be a new kind of planctomycete.

**Definition 7.2.4 (Anammox)** **Anammox** (anaerobic ammonium oxidation) is the chemolithoautotrophic oxidation of ammonium with nitrite as electron acceptor to dinitrogen,

$$
\ce{NH4+ + NO2- -> N2 + 2 H2O}, \qquad \Delta_{\mathrm{r}}G'^{\circ} = -357\,\mathrm{kJ\,mol^{-1}},
$$
carried out by bacteria of the order Brocadiales (Planctomycetota, formerly Planctomycetes), such as "*Candidatus* Brocadia", "*Ca.* Kuenenia" and "*Ca.* Scalindua", none of which has been obtained in pure culture.

The reaction takes place in a membrane-bounded compartment.

**Definition 7.2.5 (Anammoxosome)** The **anammoxosome** is the membrane-bounded intracytoplasmic compartment of anammox bacteria in which the anammox reaction and ATP synthesis take place. Its membrane contains ladderane lipids, with fused cyclobutane rings, which form an unusually dense barrier.

Inside, nitrite is reduced to nitric oxide; hydrazine synthase combines NO and ammonium to hydrazine ($\ce{N2H4}$), the rocket fuel and a strong reductant; and hydrazine dehydrogenase oxidizes it to $\ce{N2}$, the electrons cycling back to the first two steps and generating a proton-motive force across the anammoxosome membrane. The dense ladderane membrane is thought to keep the toxic, volatile hydrazine in. Electrons for $\ce{CO2}$ fixation, by the Wood–Ljungdahl pathway, come from the oxidation of some nitrite to nitrate. Anammox bacteria grow very slowly (doubling times of one to two weeks).

Anammox is responsible for a large part of the loss of fixed nitrogen from the ocean, especially in the oxygen minimum zones, and is used in wastewater treatment, where partial nitritation followed by anammox removes ammonium with less aeration and no added organic carbon.

![The microbial transformations of inorganic nitrogen, arranged by the oxidation state of N. Nitrification (blue-green) proceeds by ammonia monooxygenase (AMO) and hydroxylamine oxidoreductase (HAO) in ammonia-oxidizing bacteria and archaea, then nitrite oxidoreductase (NXR) in nitrite oxidizers; comammox *Nitrospira* do both (dashed). Denitrification (red-brown) reduces nitrate through nitrite, nitric oxide and nitrous oxide to N₂ (Nar/Nap, Nir, Nor, Nos). Anammox (purple) reduces nitrite to NO, combines it with ammonium to hydrazine, and oxidizes hydrazine to N₂ by hydrazine dehydrogenase (HDH). DNRA reduces nitrite to ammonium, and nitrogenase fixes N₂ to ammonia. The global fluxes of the nitrogen cycle are discussed in 7.11.30.](./plots/nitrogen-transformations.py)

## 7.3. Anaerobic Respiration

### 7.3.1. The Electron-Acceptor Ladder

Where oxygen is absent, other acceptors take its place, and because their $E'^{\circ}$ values differ, the energy available from the same donor falls step by step (panel B of the figure in 7.1.1). Organisms that use a more positive acceptor gain more energy, grow faster and outcompete those using more negative ones, and many respiratory enzymes are repressed when a better acceptor is present. In sediments and waterlogged soils, where acceptors are supplied from above and consumed by organic matter, they are therefore used up in a characteristic vertical sequence: oxygen, then nitrate, manganese(IV) oxides, iron(III) oxides, sulfate and finally $\ce{CO2}$ (methanogenesis). The same sequence is seen in time in a flooded rice field, and in space in aquifers downstream of a pollution source.

| Acceptor couple | $E'^{\circ}$ (V) | Process | Example organisms |
|---|---|---|---|
| $\ce{O2}/\ce{H2O}$ | +0.82 | aerobic respiration | — |
| $\ce{NO3-}/\ce{N2}$ | +0.75 | denitrification | *Pseudomonas stutzeri*, *Paracoccus denitrificans* |
| $\ce{MnO2}/\ce{Mn^2+}$ | about +0.4 | manganese reduction | *Shewanella*, *Geobacter* |
| $\ce{NO3-}/\ce{NO2-}$ | +0.43 | nitrate reduction | *Escherichia coli* |
| $\ce{Fe(III)}$ oxide/$\ce{Fe^2+}$ | about −0.1 to +0.2 | iron reduction | *Geobacter*, *Shewanella* |
| DMSO/DMS, TMAO/TMA | +0.16, +0.13 | organic acceptors | *E. coli*, *Shewanella* |
| fumarate/succinate | +0.03 | fumarate respiration | *E. coli*, *Wolinella* |
| $\ce{SO4^2-}/\ce{HS-}$ | −0.22 | sulfate reduction | *Desulfovibrio*, *Archaeoglobus* |
| $\ce{S^0}/\ce{HS-}$ | −0.27 | sulfur reduction | *Desulfuromonas*, *Pyrodictium* |
| $\ce{CO2}/\ce{CH4}$ | −0.24 | methanogenesis | *Methanobacterium*, *Methanosarcina* |
| $\ce{CO2}$/acetate | −0.29 | acetogenesis | *Acetobacterium* |

The potentials of the solid manganese and iron oxides depend on the mineral and on the concentration of the dissolved product; the values given are for pH 7.

### 7.3.2. Nitrate Reduction and Denitrification

**Definition 7.3.1 (Denitrification)** **Denitrification** is the dissimilatory reduction of nitrate or nitrite to the gaseous products nitric oxide, nitrous oxide and dinitrogen,

$$
\ce{NO3- ->[Nar/Nap] NO2- ->[Nir] NO ->[Nor] N2O ->[Nos] N2},
$$
by respiratory enzymes: nitrate reductase (membrane-bound Nar or periplasmic Nap), nitrite reductase (copper NirK or cytochrome $cd_1$ NirS), nitric oxide reductase and nitrous oxide reductase.

Most denitrifiers are facultative aerobes (*Pseudomonas*, *Paracoccus*, *Bacillus*) that respire $\ce{O2}$ when it is available; nitrate and low $\ce{O2}$ together induce the denitrification enzymes. Some archaea and even a foraminiferan protist denitrify. Many organisms have only part of the pathway: *E. coli* reduces nitrate only to nitrite, and many bacteria lack nitrous oxide reductase and release $\ce{N2O}$, which is a greenhouse gas about 270 times as potent as $\ce{CO2}$ over 100 years and the main present-day destroyer of stratospheric ozone. Agricultural soils fertilized with nitrogen are the largest anthropogenic source.

Denitrification removes fixed nitrogen from soils and waters: harmful in agriculture, where fertilizer is lost, and useful in wastewater treatment, where nitrate would otherwise cause eutrophication. Its alternative is the dissimilatory reduction of nitrate to ammonium.

**Definition 7.3.2 (Dissimilatory Nitrate Reduction to Ammonium)** **Dissimilatory nitrate reduction to ammonium** (DNRA) is the respiratory reduction of nitrate via nitrite to ammonium (in *E. coli* by the cytochrome *c* nitrite reductase NrfA), which retains the nitrogen in the ecosystem in a form available to plants.

DNRA tends to dominate where organic electron donors are abundant relative to nitrate (in sulfidic sediments and the gut), denitrification where nitrate is in excess.

### 7.3.3. Dissimilatory Sulfate Reduction

Sulfate is abundant in seawater (about 28 mM) but is a poor electron acceptor ($E'^{\circ}(\ce{SO4^2-}/\ce{HSO3-}) = -0.52\,\mathrm{V}$), and must be activated first.

**Definition 7.3.3 (Dissimilatory Sulfate Reduction)** **Dissimilatory sulfate reduction** is the anaerobic respiration with sulfate as terminal electron acceptor, reducing it with eight electrons to sulfide. Sulfate is activated by ATP sulfurylase to adenosine 5′-phosphosulfate (APS), APS reductase (AprAB) reduces APS to sulfite and AMP, and dissimilatory sulfite reductase (DsrAB, with DsrC) reduces sulfite to sulfide.

**Definition 7.3.4 (Sulfate-Reducing Bacteria)** **Sulfate-reducing bacteria** (SRB) are obligately anaerobic microorganisms that conserve energy by dissimilatory sulfate reduction. Most belong to the Desulfobacterota (formerly Deltaproteobacteria: *Desulfovibrio*, *Desulfobacter*, *Desulfobacterium*), others to the Bacillota (*Desulfotomaculum*) and Nitrospirota (*Thermodesulfovibrio*); the archaeon *Archaeoglobus* reduces sulfate by the same pathway.

Activation costs one ATP that is hydrolysed to AMP and pyrophosphate, the equivalent of two ATP, so the energy balance is tight. With $\ce{H2}$,

$$
\ce{4 H2 + SO4^2- + H+ -> HS- + 4 H2O}, \qquad \Delta_{\mathrm{r}}G'^{\circ} = -152\,\mathrm{kJ},
$$
and periplasmic hydrogenases with the low-potential cytochrome $c_3$ generate a proton-motive force that yields about one net ATP per sulfate. Sulfate reducers are of two physiological types: incomplete oxidizers such as *Desulfovibrio* oxidize lactate, pyruvate or ethanol only to acetate, while complete oxidizers such as *Desulfobacter* and *Desulfobacterium* oxidize acetate and fatty acids to $\ce{CO2}$ by a modified citric acid cycle or the reversed Wood–Ljungdahl pathway ($\ce{CH3COO- + SO4^2- + 3 H+ -> 2 CO2 + H2S + 2 H2O}$, $\Delta_{\mathrm{r}}G'^{\circ} \approx -57\,\mathrm{kJ}$). Some grow autotrophically with $\ce{H2}$ and $\ce{CO2}$.

Sulfate reduction is the dominant terminal process of organic matter mineralization in marine sediments, where it accounts for up to about half of the carbon oxidized; the sulfide it produces blackens the mud with iron sulfide, feeds the sulfur oxidizers and phototrophs above, and corrodes iron pipes. Other sulfur respirations are linked to it:

- Sulfur reducers such as *Desulfuromonas acetoxidans* (and many hyperthermophilic archaea) reduce $\ce{S^0}$ but not sulfate, which they cannot activate.
- Some sulfate reducers gain energy by **disproportionation** of thiosulfate, sulfite or sulfur, oxidizing one sulfur atom and reducing another: $\ce{S2O3^2- + H2O -> SO4^2- + HS- + H+}$, $\Delta_{\mathrm{r}}G'^{\circ} = -21.9\,\mathrm{kJ}$, which recycles the sulfur intermediates produced by sulfide oxidation.

### 7.3.4. Metal Reduction and Extracellular Electron Transfer

Iron(III) and manganese(IV) are abundant electron acceptors in soils and sediments, but they occur as insoluble oxides that cannot enter a cell.

**Definition 7.3.5 (Dissimilatory Metal Reduction)** **Dissimilatory metal reduction** is the anaerobic respiration with oxidized metals, above all iron(III) and manganese(IV) oxides, as terminal electron acceptors, coupled to the oxidation of organic compounds or $\ce{H2}$.

**Definition 7.3.6 (Extracellular Electron Transfer)** **Extracellular electron transfer** (EET) is the transport of respiratory electrons from the cytoplasmic membrane across the cell envelope to an acceptor outside the cell (a mineral, an electrode or another cell), or in the reverse direction.

The two model organisms illustrate the mechanisms. *Shewanella oneidensis*, a facultative anaerobe, uses the Mtr pathway: the quinol dehydrogenase CymA in the inner membrane, the periplasmic decaheme cytochrome MtrA, the outer-membrane porin MtrB and the surface decaheme cytochromes MtrC and OmcA, which hand electrons to the mineral; it also secretes flavins that shuttle electrons to more distant surfaces. *Geobacter sulfurreducens*, a strict anaerobe that oxidizes acetate completely, makes electrically conductive filaments that reach the mineral. They were first described as conductive type IV pili ("microbial nanowires", 2005); cryo-electron microscopy later showed that the main filaments are polymers of the hexaheme cytochrome OmcS (2019), and the respective roles of pili and cytochrome filaments are still being settled.

Electron transfer between cells extends these principles:

- Direct interspecies electron transfer (DIET) connects *Geobacter* with methanogens (*Methanothrix*) or connects anaerobic methane-oxidizing archaea with their sulfate-reducing partners (7.4.4).
- Some bacteria conduct electrons along their own multicellular filaments (Definition 7.3.7).

**Definition 7.3.7 (Cable Bacteria)** **Cable bacteria** are filamentous bacteria of the family Desulfobulbaceae that conduct electrons over centimetres along a filament of thousands of cells, coupling the oxidation of sulfide in deeper sediment to the reduction of oxygen or nitrate at the surface.

Discovered in 2012, they explain why sulfide in some sediments disappears centimetres below the reach of oxygen; the conductive fibres run in the shared periplasm along the filament.

Metal reducers are used to remove soluble uranium(VI) from groundwater by reducing it to insoluble uranium(IV), and *Geobacter* biofilms power microbial fuel cells, in which an anode replaces the iron oxide.

### 7.3.5. Other Electron Acceptors

- Organic acceptors: fumarate (reduced to succinate by fumarate reductase), trimethylamine $N$-oxide (TMAO, from marine fish; its reduction to trimethylamine gives spoiled fish its smell) and dimethyl sulfoxide (DMSO). *E. coli* uses all three when $\ce{O2}$ and nitrate are absent.
- Halogenated organic compounds: see Definition 7.3.8 below.
- Metalloids and oxyanions: arsenate is reduced to arsenite (which mobilizes arsenic in groundwater; *Desulfosporosinus auripigmenti* (formerly *Desulfotomaculum auripigmentum*) precipitates it as the yellow mineral orpiment, $\ce{As2S3}$), selenate to selenite and elemental selenium, and chlorate and perchlorate to chloride. Perchlorate reducers produce chlorite, which chlorite dismutase splits into chloride and $\ce{O2}$; the $\ce{O2}$ is then respired, a rare biological route to oxygen without light.
- Protons: the hyperthermophilic archaeon *Pyrococcus furiosus* oxidizes sugars via a modified glycolysis that reduces ferredoxin instead of NAD and transfers the electrons to protons with a membrane-bound, proton-pumping hydrogenase, a respiration with $\ce{H+}$ as the acceptor.

**Definition 7.3.8 (Organohalide Respiration)** **Organohalide respiration** (dehalorespiration) is the anaerobic respiration with halogenated organic compounds as electron acceptors, which are reductively dehalogenated by cobalamin-containing reductive dehalogenases.

*Dehalococcoides mccartyi* uses only organohalides and reduces the solvent tetrachloroethene stepwise to ethene, and some strains dechlorinate polychlorinated biphenyls; cultures containing it are added to contaminated aquifers for bioremediation.

## 7.4. One-Carbon Metabolism

### 7.4.1. Acetogenesis

**Definition 7.4.1 (Acetogen)** An **acetogen** is a strictly anaerobic bacterium that uses the Wood–Ljungdahl pathway ([Definition 6.5.3](/7.11.6#def-6.5.3)) both to fix $\ce{CO2}$ and to conserve energy, reducing $\ce{CO2}$ to acetate as the terminal electron-accepting process:

$$
\ce{4 H2 + 2 HCO3- + H+ -> CH3COO- + 4 H2O}, \qquad \Delta_{\mathrm{r}}G'^{\circ} = -105\,\mathrm{kJ}.
$$

Acetogens (*Acetobacterium woodii*, *Clostridium ljungdahlii*, *Moorella thermoacetica*, in which Harland Wood and Lars Ljungdahl worked out the pathway) are mostly gram-positive and very versatile: besides $\ce{H2}$ and CO they use sugars, methanol, the methoxy groups of lignin monomers and many other substrates, and glucose is fermented to three acetate, the third coming from $\ce{CO2}$ reduction with the electrons of glycolysis. In the termite hindgut, acetogens rather than methanogens consume most of the $\ce{H2}$, and their acetate is the main energy source of the insect.

The energetics of acetogenesis is a lesson in how little energy is needed for life. The one ATP made from acetyl phosphate is spent at formyl-tetrahydrofolate synthetase, so there is no net substrate-level phosphorylation. Energy is conserved by a membrane complex, Rnf (or Ech in some species), which oxidizes reduced ferredoxin with $\ce{NAD+}$ and pumps $\ce{Na+}$ (in *A. woodii*) or $\ce{H+}$; a $\ce{Na+}$-driven ATP synthase completes the chain. About 0.3 ATP is made per acetate. The reduced ferredoxin needed by Rnf and by CO dehydrogenase is more negative than $\ce{H2}$ at physiological pressures, and is obtained by a coupling mechanism found widely in anaerobes.

**Definition 7.4.2 (Electron Bifurcation)** Flavin-based **electron bifurcation** is a mechanism by which an enzyme-bound flavin accepts two electrons from a donor and passes one to a high-potential acceptor (exergonic) and the other to a low-potential acceptor (endergonic), so that the first reaction drives the second; for example, two $\ce{H2}$ reduce one $\ce{NAD+}$ and one ferredoxin together.

Electron bifurcation, discovered in 2008, explains how many anaerobes make reduced ferredoxin and is central to the energy metabolism of methanogens (7.4.2) and fermenting clostridia. Acetogens are also used industrially to convert carbon monoxide-rich waste gases into ethanol and acetate.

### 7.4.2. Methanogenesis

**Definition 7.4.3 (Methanogenesis and Methanogen)** **Methanogenesis** is the formation of methane as the end product of energy metabolism. It is carried out only by **methanogens**, strictly anaerobic archaea, and in all of them ends with the reduction of methyl-coenzyme M by methyl-coenzyme M reductase.

Methanogens use three kinds of substrate (standard values per reaction):

| Type | Reaction | $\Delta_{\mathrm{r}}G'^{\circ}$ | Examples |
|---|---|---|---|
| Hydrogenotrophic | $\ce{4 H2 + CO2 -> CH4 + 2 H2O}$ (also formate) | −131 kJ | *Methanobacterium*, *Methanococcus*, *Methanobrevibacter* |
| Methylotrophic | $\ce{4 CH3OH -> 3 CH4 + CO2 + 2 H2O}$ (also methylamines, methanethiol) | −319 kJ | *Methanosarcina*, *Methanosphaera* (with $\ce{H2}$) |
| Acetoclastic | $\ce{CH3COO- + H+ -> CH4 + CO2}$ | about −36 kJ | *Methanosarcina*, *Methanothrix* (formerly *Methanosaeta*) |

The chemistry uses coenzymes found nowhere else: methanofuran and tetrahydromethanopterin carry the C1 unit as it is reduced; the deazaflavin coenzyme $\mathrm{F_{420}}$, which fluoresces blue-green under ultraviolet light and is used to recognize methanogens under the microscope, is the hydride donor; coenzyme M (2-mercaptoethanesulfonate) carries the methyl group in the last step; and coenzyme B donates the final electrons. Methyl-coenzyme M reductase, containing the nickel tetrapyrrole $\mathrm{F_{430}}$, forms methane and the heterodisulfide CoM-S-S-CoB.

![The pathways of methanogenesis converge on methyl-coenzyme M. Centre, hydrogenotrophic methanogenesis: CO₂ is reduced on methanofuran (MFR) with reduced ferredoxin, then on tetrahydromethanopterin (H₄MPT) with reduced coenzyme F₄₂₀ to methyl-H₄MPT; the membrane-bound methyltransferase (Mtr) moves the methyl group to coenzyme M and pumps Na⁺; methyl-coenzyme M reductase (Mcr) forms CH₄ and the heterodisulfide CoM–S–S–CoB, which heterodisulfide reductase (Hdr) reduces again. Left, methylotrophic methanogenesis: methyltransferases transfer the methyl group of methanol or methylamines to coenzyme M. Right, acetoclastic methanogenesis: acetyl-CoA is split by CO dehydrogenase/acetyl-CoA synthase (CODH/ACS); the methyl group enters at the methyl-pterin level and the carbonyl is oxidized to CO₂.](./plots/methanogenesis-pathways.py)

Energy is conserved by ion gradients; there is no substrate-level phosphorylation. In hydrogenotrophic methanogens without cytochromes, the methyl transfer from methyl-H₄MPT to coenzyme M pumps $\ce{Na+}$, and the reduced ferredoxin for the first step is made by an electron-bifurcating heterodisulfide reductase that couples the reduction of CoM-S-S-CoB by $\ce{H2}$ to the reduction of ferredoxin; the yield is about 0.5 ATP per methane. Methanogens with cytochromes (Methanosarcinales) also have a membrane-bound heterodisulfide reductase that receives electrons via methanophenazine and pumps protons, which allows them to use acetate and methyl compounds. Methanogens belong to several archaeal lineages, including Methanobacteriota and Halobacteriota (formerly all in the Euryarchaeota); their diversity is described in [7.11.19](/7.11.19).

Methanogenesis is the terminal step of anaerobic decomposition wherever sulfate and the other acceptors are exhausted: in freshwater sediments, wetlands and rice paddies, the rumen and the large intestine, landfills and anaerobic digesters. In freshwater sediments about two thirds of the methane comes from acetate and one third from $\ce{H2}$ and $\ce{CO2}$. Biological methanogenesis produces on the order of a billion tonnes of methane a year, the largest source of this greenhouse gas; most of it is consumed again by methanotrophs before it reaches the atmosphere.

### 7.4.3. Aerobic Methanotrophy and Methylotrophy

**Definition 7.4.4 (Methylotroph and Methanotroph)** A **methylotroph** is an organism that uses reduced one-carbon compounds (methanol, methylamines, formaldehyde, methane) or other compounds without carbon–carbon bonds as its sole source of carbon and energy. A **methanotroph** is a methylotroph that can use methane.

Aerobic methanotrophs oxidize methane through methanol, formaldehyde and formate to $\ce{CO2}$. The first step is catalyzed by methane monooxygenase (MMO), in two unrelated forms: the copper particulate MMO (pMMO) in the membrane, present in nearly all methanotrophs, and the soluble di-iron MMO (sMMO), made by some species when copper is scarce, which has a very broad substrate range and co-oxidizes trichloroethylene and other pollutants. Methanol dehydrogenase uses calcium in the classical MxaF enzyme, but many methylotrophs have a lanthanide-dependent enzyme (XoxF); the volcanic-mud methanotroph *Methylacidiphilum fumariolicum* cannot grow without rare-earth elements, the first organism found to depend strictly on lanthanides.

Formaldehyde, at the oxidation level of cell material, is the branch point between energy and biosynthesis, and the assimilation pathway divides the methanotrophs:

| | Type I | Type II |
|---|---|---|
| Taxonomy | Gammaproteobacteria (*Methylomonas*, *Methylobacter*, *Methylococcus*) | Alphaproteobacteria (*Methylosinus*, *Methylocystis*) |
| C1 assimilation | ribulose monophosphate pathway (formaldehyde + ribulose 5-phosphate) | serine pathway (formaldehyde + glycine, plus $\ce{CO2}$) |
| Internal membranes | stacks of vesicular discs | paired membranes along the periphery |

The ribulose monophosphate pathway is cheaper, because all cell carbon comes from formaldehyde; the serine pathway needs extra NADH and ATP. Acidophilic methanotrophs of the Verrucomicrobiota fix $\ce{CO2}$ by the Calvin cycle instead. Methanotrophs in soils and at the oxic surface of sediments and wetlands consume most of the methane produced below, and upland soils oxidize atmospheric methane with high-affinity methanotrophs. Non-methanotrophic methylotrophs such as *Methylobacterium*, pink bacteria common on leaves, live on the methanol released by plant cell walls.

### 7.4.4. Anaerobic Oxidation of Methane

Marine sediments produce large amounts of methane, yet very little escapes from them: it is oxidized below the sediment surface without $\ce{O2}$.

**Definition 7.4.5 (Anaerobic Oxidation of Methane)** The **anaerobic oxidation of methane** (AOM) is the oxidation of methane coupled to the reduction of sulfate, nitrate, nitrite or metal oxides. With sulfate it is carried out by consortia of anaerobic methanotrophic archaea (ANME), which oxidize methane by running the methanogenic pathway in reverse, and sulfate-reducing bacteria that take up the electrons:

$$
\ce{CH4 + SO4^2- -> HCO3- + HS- + H2O}, \qquad \Delta_{\mathrm{r}}G'^{\circ} \approx -17\,\mathrm{kJ}.
$$

The energy available is barely enough for two partners, and the consortia grow with doubling times of months. They form tight aggregates in the sulfate–methane transition zone of marine sediments and around methane seeps, and remove most of the methane produced in the seabed. How the partners exchange electrons was long unclear; $\ce{H2}$ and other diffusible intermediates do not explain the rates, and the current evidence favours direct interspecies electron transfer through multiheme cytochromes and conductive filaments (7.3.4). Other variants dispense with a partner:

- "*Candidatus* Methanoperedens nitroreducens" (ANME-2d) oxidizes methane in reverse methanogenesis with nitrate, reducing it to nitrite, in freshwater sediments; some relatives use iron or manganese oxides.
- "*Candidatus* Methylomirabilis oxyfera" (phylum Methylomirabilota, formerly NC10) oxidizes methane with nitrite in a unique way: it reduces nitrite to NO and apparently dismutates two NO into $\ce{N2}$ and $\ce{O2}$, then uses the internally produced $\ce{O2}$ for an aerobic methane monooxygenase ("intra-aerobic" methanotrophy) in a strictly anoxic environment.

Related archaea oxidize short-chain alkanes (butane, ethane) anaerobically in a similar way, via alkyl-coenzyme M (7.5.3).

## 7.5. Syntrophy

### 7.5.1. Interspecies Hydrogen Transfer

Many anaerobic degradations cannot be carried out by any single organism, because they are endergonic under standard conditions.

**Definition 7.5.1 (Syntrophy)** **Syntrophy** is a mutualistic metabolic interaction in which two organisms together carry out a catabolic reaction that neither can carry out alone, because one partner keeps the concentration of the other's product (usually $\ce{H2}$ or formate) low enough for that partner's reaction to be exergonic.

**Definition 7.5.2 (Interspecies Hydrogen Transfer)** **Interspecies hydrogen transfer** is the transfer of $\ce{H2}$ from a hydrogen-producing fermenting organism to a hydrogen-consuming partner (a methanogen, sulfate reducer or acetogen), which maintains the low $\ce{H2}$ partial pressure that makes the producer's reaction thermodynamically possible.

The classical example was "*Methanobacillus omelianskii*", long considered a single methanogen that converts ethanol into acetate and methane. In 1967 Bryant and colleagues showed that it was a coculture of two organisms: one oxidizing ethanol to acetate and $\ce{H2}$, the other (*Methanobacterium*) reducing $\ce{CO2}$ with the $\ce{H2}$:

$$
\begin{aligned}
\ce{2 CH3CH2OH + 2 H2O &-> 2 CH3COO- + 2 H+ + 4 H2} && \Delta_{\mathrm{r}}G'^{\circ} = +19.4\,\mathrm{kJ}\\
\ce{4 H2 + CO2 &-> CH4 + 2 H2O} && \Delta_{\mathrm{r}}G'^{\circ} = -130.7\,\mathrm{kJ}\\
\ce{2 CH3CH2OH + CO2 &-> 2 CH3COO- + 2 H+ + CH4} && \Delta_{\mathrm{r}}G'^{\circ} = -111.3\,\mathrm{kJ}
\end{aligned}
$$

The coupled reaction is exergonic, but its energy must be shared between the two partners, and each gains energy only if the $\ce{H2}$ partial pressure lies between two limits. The actual Gibbs energy, $\Delta_{\mathrm{r}}G = \Delta_{\mathrm{r}}G'^{\circ} + RT\ln Q$ ([Formula 16.2.1](/7.1.16#sec-16.2.2)), contains $p(\ce{H2})$ to a positive power for the producer and a negative power for the consumer.

**Example 7.5.1** For the oxidation of butyrate, $\ce{C3H7COO- + 2 H2O -> 2 CH3COO- + H+ + 2 H2}$, $\Delta_{\mathrm{r}}G'^{\circ} = +48.1\,\mathrm{kJ}$. With butyrate and acetate at 1 mM, at 25 °C ($RT = 2.48\,\mathrm{kJ\,mol^{-1}}$),

$$
\Delta_{\mathrm{r}}G = 48.1 + 2.48\ln\frac{(10^{-3})^2\,p(\ce{H2})^2}{10^{-3}} = 48.1 - 17.1 + 4.96\ln p(\ce{H2}),
$$
which is negative only for $p(\ce{H2}) < \mathrm{e}^{-31.0/4.96} \approx 2\times10^{-3}\,\mathrm{bar}$. At $10^{-5}\,\mathrm{bar}$, a typical value in methanogenic habitats, $\Delta_{\mathrm{r}}G \approx -26\,\mathrm{kJ}$. The methanogen, on the other hand ($\ce{4 H2 + HCO3- + H+ -> CH4 + 3 H2O}$, $-135.6\,\mathrm{kJ}$, with 50 mM bicarbonate and 0.5 bar methane), needs $p(\ce{H2}) > 2\times10^{-6}\,\mathrm{bar}$. Both gain energy only in the window between about $2\times10^{-6}$ and $2\times10^{-3}\,\mathrm{bar}$.

![The thermodynamic window of syntrophy (ΔG = ΔG'° + RT ln Q at 25 °C with 1 mM fatty acids and acetate, 50 mM bicarbonate and 0.5 bar CH₄; standard values after Thauer et al. 1977). A: butyrate oxidation to acetate and H₂ becomes exergonic below about 2 × 10⁻³ bar H₂, methanogenesis from H₂ above about 2 × 10⁻⁶ bar; both partners can gain energy within the shaded window. B: for propionate, with three H₂ per molecule and a more positive ΔG'° (+76.1 kJ), the window shrinks to about 2 × 10⁻⁶ to 10⁻⁴ bar. The methanogenic reaction is scaled to the H₂ produced by one fatty acid.](./plots/syntrophy-window.py)

Within the window, each partner has to live on a few tens of kilojoules per reaction, near the minimum discussed in 7.1.1. The syntroph faces an additional problem: it must produce $\ce{H2}$ ($-0.41\,\mathrm{V}$ at standard pressure) from NADH ($-0.32\,\mathrm{V}$) or, in fatty acid oxidation, from the electron-transfer flavoprotein of butyryl-CoA dehydrogenase (about $-0.1\,\mathrm{V}$), which needs reverse electron transport or electron confurcation, consuming part of the meagre energy. The rate of degradation is limited by the diffusion of $\ce{H2}$ between the partners, and syntrophs and methanogens grow in close contact in flocs and granules; formate is an alternative carrier, and some partners exchange electrons directly.

### 7.5.2. Syntrophy in the Anaerobic Food Chain

In a methanogenic environment the degradation of polymers proceeds through a chain of guilds: hydrolytic and fermenting bacteria break down polysaccharides, proteins and lipids into sugars, amino acids and fatty acids and ferment them to acetate, $\ce{H2}$, $\ce{CO2}$, propionate, butyrate and alcohols; syntrophs (*Syntrophomonas wolfei* for butyrate and longer fatty acids, *Syntrophobacter* and *Pelotomaculum* for propionate, *Syntrophus* for benzoate) convert the reduced intermediates to acetate and $\ce{H2}$; and methanogens consume $\ce{H2}$ and acetate. Without syntrophs, reduced fermentation products would accumulate and degradation would stop wherever electron acceptors other than $\ce{CO2}$ are exhausted. Where nitrate, iron or sulfate is available, syntrophy is unnecessary: a sulfate reducer can oxidize butyrate or propionate completely by itself. The anaerobic food chain and its role in the carbon cycle and in **anaerobic digestion** are treated in [7.11.30](/7.11.30).

### 7.5.3. Hydrocarbon Degradation

Hydrocarbons, from natural seeps and oil spills, are degraded by many microorganisms, but their C–H bonds must first be activated.

- Aerobically, oxygenases insert oxygen: alkane monooxygenases (the membrane enzyme AlkB, cytochromes P450) hydroxylate the terminal carbon, and the resulting fatty acid is degraded by β-oxidation; aromatic rings are hydroxylated by mono- and dioxygenases to catechols, which ring-cleaving dioxygenases open. Specialists such as the marine *Alcanivorax borkumensis* bloom after oil spills.
- Anaerobically, without $\ce{O2}$, toluene and alkanes are activated by the addition of fumarate to a carbon atom (by the glycyl-radical enzymes benzylsuccinate and alkylsuccinate synthase), benzene and naphthalene probably by carboxylation, and the aromatic ring is reduced rather than oxidized in the benzoyl-CoA pathway. These degradations are coupled to nitrate, iron or sulfate reduction, and in methanogenic environments even long-chain alkanes are converted to methane by syntrophic consortia (shown in 1999). Archaea related to the ANME oxidize short-chain alkanes via alkyl-coenzyme M.

## 7.6. The Winogradsky Column

The metabolisms of this chapter and the last can all be seen in one simple enrichment.

**Definition 7.6.1 (Winogradsky Column)** A **Winogradsky column** is a glass cylinder filled with mud supplemented with cellulose (shredded paper) and sulfate (gypsum, $\ce{CaSO4}$), with carbonate as buffer, topped with water and incubated in the light for weeks to months, in which opposing gradients of oxygen (from above) and sulfide (from below) develop and the microbial groups stratify according to their requirements for light, oxygen and sulfide.

In the dark mud at the bottom, cellulose is degraded by fermenters, whose products feed sulfate reducers; their sulfide blackens the mud and diffuses upward. Methane is formed once sulfate is exhausted. Above, in the light but still anoxic zone, green and then purple sulfur bacteria oxidize the sulfide; purple nonsulfur bacteria grow above them where sulfide is low; at the oxic–anoxic interface colourless sulfur oxidizers such as *Beggiatoa* use $\ce{O2}$ and $\ce{H2S}$ together; and cyanobacteria and algae in the water and on the upper mud produce the oxygen. Where the layers sit is a matter of diffusion and reaction, as a simple model shows.

![The Winogradsky column as a redox gradient. A: schematic of the layers that develop in a mud column with cellulose and calcium sulfate in the light: algae and cyanobacteria in the water, aerobic heterotrophs, colourless sulfur oxidizers at the O₂/H₂S interface, purple nonsulfur, purple sulfur and green sulfur bacteria in the illuminated anoxic zone, and fermenters, sulfate reducers (black iron sulfide) and methanogens in the mud. B: steady state of a one-dimensional reaction–diffusion model (dimensionless depth): O₂ diffuses in from the top and is consumed by respiration and by reaction with sulfide; sulfide diffuses up from the sulfate-reducing mud and is consumed by O₂ and, below the oxic zone where light remains, by anoxygenic phototrophs (inhibited by O₂). The two sulfide-consuming rates peak at the interface (colourless sulfur oxidizers) and a short distance below it (phototrophs), reproducing the layering in A.](./plots/winogradsky-column.py)

The model makes the point that the narrow bands are not imposed by the organisms' preferences alone but by the chemistry: sulfide and oxygen annihilate each other within a thin zone because their reaction (chemical and biological) is fast compared with their diffusion, and phototrophs can use sulfide only below that zone and only as deep as the light reaches. The same structure, compressed to millimetres, is found in microbial mats and, stretched to metres, in stratified lakes and the Black Sea ([7.11.29](/7.11.29)).

## Summary

- Energy yield follows from the reduction potentials of donor and acceptor, $\Delta_{\mathrm{r}}G'^{\circ} = -zF\Delta E'^{\circ}$; life is possible down to about −20 kJ per reaction. Assimilatory and dissimilatory reductions differ in purpose, scale and enzymes (Definition 7.1.1).
- Chemolithotrophs oxidize inorganic donors; except for $\ce{H2}$, their donors are too positive to reduce $\ce{NAD+}$, so autotrophy requires reverse electron transport, and the weakest donors (nitrite, ferrous iron) give the lowest yields (Example 7.1.1).

| Donor | Key enzymes or systems | Examples | Remarks |
|---|---|---|---|
| $\ce{H2}$ | [NiFe] hydrogenases (Definition 7.2.1) | *Cupriavidus necator* | facultative; soil bacteria scavenge atmospheric $\ce{H2}$ |
| $\ce{H2S}$, $\ce{S^0}$, $\ce{S2O3^2-}$ | Sox system; rDsr and APS reductase | *Beggiatoa*, *Thiomargarita*, *Acidithiobacillus* | acidify; some use nitrate |
| $\ce{Fe^2+}$ | outer-membrane cytochrome, rusticyanin | *A. ferrooxidans*, *Gallionella* | acidophiles or interface specialists |
| $\ce{NH3}$ → $\ce{NO2-}$ | AMO, HAO | *Nitrosomonas*, *Nitrosopumilus* (AOA) | nitrification (Definition 7.2.2) |
| $\ce{NO2-}$ → $\ce{NO3-}$ | NXR | *Nitrobacter*, *Nitrospira* | comammox *Nitrospira* do both (Definition 7.2.3) |
| $\ce{NH4+}$ + $\ce{NO2-}$ | hydrazine synthase, anammoxosome | *Ca.* Brocadia, *Ca.* Scalindua | anammox (Definitions 7.2.4, 7.2.5) |

- Anaerobic respirations use acceptors in the order of their potentials: $\ce{O2}$ > nitrate (denitrification, DNRA; Definitions 7.3.1, 7.3.2) > Mn(IV) > Fe(III) (metal reduction and extracellular electron transfer, cable bacteria; Definitions 7.3.5–7.3.7) > sulfate (activation to APS; Definitions 7.3.3, 7.3.4) > $\ce{CO2}$; organic, halogenated and metalloid acceptors broaden the list (Definition 7.3.8).
- One-carbon metabolism: acetogens use the Wood–Ljungdahl pathway for energy (Definition 7.4.1), conserving it through Rnf and electron bifurcation (Definition 7.4.2); methanogens (Definition 7.4.3) make $\ce{CH4}$ from $\ce{H2}/\ce{CO2}$, methyl compounds or acetate with unique coenzymes and methyl-coenzyme M reductase; aerobic methanotrophs (Definition 7.4.4) use MMO and the RuMP or serine pathway; anaerobic methane oxidation (Definition 7.4.5) runs methanogenesis backwards in consortia with sulfate reducers.
- Syntrophy (Definitions 7.5.1, 7.5.2) makes endergonic oxidations of alcohols and fatty acids possible within a narrow window of $\ce{H2}$ pressure (Example 7.5.1) and links fermentation to methanogenesis.
- The Winogradsky column (Definition 7.6.1) displays the redox gradient and the resulting layers of phototrophs, sulfur oxidizers, sulfate reducers and methanogens in one enrichment.

## Questions

1. Why do nitrifying bacteria and acidophilic iron oxidizers produce so little biomass compared with hydrogen bacteria, even though all use $\ce{O2}$ as acceptor?

   **Answer** Their donors release little energy per electron ($-74\,\mathrm{kJ}$ per nitrite, about $-33\,\mathrm{kJ}$ per ferrous iron against $-237\,\mathrm{kJ}$ per $\ce{H2}$), and because their donors are far more positive than $\ce{NAD+}$, the NADH for the Calvin cycle must be made by reverse electron transport at a high cost (Example 7.1.1); hydrogen bacteria reduce $\ce{NAD+}$ directly with a soluble hydrogenase.

2. In a coastal sediment, nitrate disappears in the top few millimetres, sulfate over tens of centimetres and methane appears only below that. Explain the sequence.

   **Answer** Electron acceptors are consumed in order of decreasing energy yield (7.3.1): nitrate (and Mn, Fe oxides) gives more energy per electron than sulfate, so nitrate reducers outcompete sulfate reducers until nitrate is gone; sulfate is abundant in seawater (about 28 mM) and lasts deeper; methanogens are outcompeted by sulfate reducers for $\ce{H2}$ and acetate as long as sulfate is present, and any methane diffusing up is oxidized anaerobically in the sulfate–methane transition zone.

3. Show from the reactions why denitrification removes nitrogen from an ecosystem but DNRA does not, and state one environmental consequence of incomplete denitrification.

   **Answer** Denitrification converts nitrate to the gases NO, $\ce{N2O}$ and $\ce{N2}$, which escape to the atmosphere; DNRA converts nitrate to ammonium, which remains dissolved or adsorbed and available to plants and microorganisms. Incomplete denitrification releases $\ce{N2O}$, a potent greenhouse gas and the main ozone-depleting emission today.

4. A coculture of *Syntrophomonas* and a methanogen degrades butyrate, but the syntroph alone does not. Using Example 7.5.1, explain why, and predict what happens if sulfate is added.

   **Answer** Butyrate oxidation to acetate and $\ce{H2}$ has $\Delta_{\mathrm{r}}G'^{\circ} = +48\,\mathrm{kJ}$ and becomes exergonic only below about $2\times10^{-3}\,\mathrm{bar}$ $\ce{H2}$; in pure culture $\ce{H2}$ accumulates and the reaction stops, whereas the methanogen keeps $\ce{H2}$ near $10^{-5}\,\mathrm{bar}$. With sulfate, sulfate reducers consume $\ce{H2}$ to even lower pressures and outcompete the methanogen; some can oxidize butyrate themselves, so methane production declines.

5. Why can methanogens, acetogens and anammox bacteria all use the Wood–Ljungdahl pathway, while aerobic chemolithotrophs cannot?

   **Answer** The pathway is the cheapest route of $\ce{CO2}$ fixation (about 1 ATP per pyruvate) and, in acetogens and methanogens, part of energy metabolism itself; but its key enzymes (CO dehydrogenase/acetyl-CoA synthase, formate dehydrogenase, corrinoid iron–sulfur protein) contain nickel, cobalt and iron–sulfur clusters that are inactivated by $\ce{O2}$, so it is restricted to strict anaerobes ([7.11.6](/7.11.6#sec-6.5.6)).
