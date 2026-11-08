---
title: Carbon Assimilation in C3, C4 and CAM Plants
description: C3, C4 and CAM plants; competition between carboxylation and oxygenation by Rubisco, the temperature dependence of Γ* and the CO2 compensation point; the physiological significance of photorespiration; the three decarboxylation subtypes of C4 plants, CO2 concentration and leakage in the bundle sheath, the energy budget, light regulation and cold sensitivity of key enzymes, single-cell C4; the four phases of CAM, energy and water, facultative CAM; a full comparison of the three plant types; carbon isotope discrimination Δ and δ13C, Δ and water-use efficiency; the evolution of C4 photosynthesis and C4 rice.
source_hash: 08562b991251
---

The ATP and NADPH produced by the light reactions are used to reduce $\ce{CO2}$ to sugar. All oxygenic photosynthetic organisms fix carbon with the same enzyme, **Rubisco**, and the same **Calvin cycle**; their biochemical steps, stoichiometry and light regulation were written up in [7.1.25](/7.1.25), where the reaction sequences of the **C4 pathway** and **crassulacean acid metabolism** are also given. This chapter answers three questions from the viewpoint of plant physiology: Rubisco catalyzes both carboxylation and oxygenation, so what are the consequences of this competition at the leaf level (photorespiration, the **CO₂ compensation point**); how C4 and CAM plants avoid this problem through anatomy, biochemistry and regulation, and what each pays and gains; and how the photosynthetic type of a plant and its stomatal behavior during growth can be inferred from its carbon isotope composition. The structure of the leaf (**Kranz anatomy**) is in [7.12.23](/7.12.23#sec-23.5.6), the quantitative responses of photosynthetic rate to light, $\ce{CO2}$ and temperature are in the next chapter ([7.13.9](/7.13.9)), and the transport and partitioning of photosynthate are in [7.13.11](/7.13.11).

## 8.1. Three Types of Carbon Assimilation

### 8.1.1. C3, C4 and CAM

**Definition 8.1.1 (C3 Plant)** A plant that assimilates $\ce{CO2}$ only through the Calvin cycle, the first stable product being the three-carbon compound 3-phosphoglycerate, is called a **C3 plant**.

The great majority of plants (about 90% of species), including wheat, rice, soybean, cotton, potato and almost all trees, are C3 plants. About 3% of species add, before the Calvin cycle, a step in which phosphoenolpyruvate carboxylase (PEPC) fixes $\ce{HCO3-}$, the first product being a four-carbon dicarboxylic acid; they fall into two classes according to whether the two carboxylations are separated in space (C4 plants) or in time (CAM plants). The Calvin cycle is identical in all three; the difference lies only in the $\ce{CO2}$ environment in which Rubisco works:

| | C3 plants | C4 plants | CAM plants |
|---|---|---|---|
| Enzyme fixing atmospheric $\ce{CO2}$ | Rubisco | PEPC (mesophyll cells) | PEPC (at night) |
| First product | 3-phosphoglycerate (C3) | oxaloacetate (C4) | oxaloacetate (C4) |
| Site of Calvin cycle | mesophyll cells, day | bundle sheath cells, day | mesophyll cells, day |
| Separation of the two carboxylations | none | in space | in time |
| $\ce{CO2}$ at Rubisco | below atmospheric | about 10 times atmospheric | very high while stomata are closed by day |

### 8.1.2. Physiological Points on the Calvin Cycle

The Calvin cycle consumes 3 ATP and 2 NADPH per $\ce{CO2}$ fixed. The product triose phosphate has two fates: synthesis of starch in the chloroplast (stored by day, broken down and exported at night), or exchange with cytosolic $\mathrm{P_i}$ through the triose-phosphate translocator of the inner envelope, followed by sucrose synthesis in the cytosol and export from the leaf. The translocator is a one-for-one counter-exchange, so the amount of cytosolic $\mathrm{P_i}$ determines how fast triose phosphate is exported: sucrose synthesis releases $\mathrm{P_i}$ and promotes export; when sucrose synthesis is blocked $\mathrm{P_i}$ is insufficient, triose phosphate stays in the chloroplast and is converted to starch, and the rise in the 3-phosphoglycerate/$\mathrm{P_i}$ ratio also activates ADP-glucose pyrophosphorylase and speeds starch synthesis ([7.1.25](/7.1.25#sec-25.5.3)). If sink organs cannot take up photosynthate in time ([7.13.11](/7.13.11)), sugars and starch accumulate in the leaf, the recycling of $\mathrm{P_i}$ slows, and photosynthesis becomes limited by "triose phosphate utilization", the third limitation of the Farquhar model ([7.13.9](/7.13.9)). Main photosynthetic products differ among plants: the leaves of most dicots such as soybean, cotton and tobacco accumulate large amounts of starch by day; grass leaves such as wheat and rice have less starch and mainly sucrose (and fructans); onion and garlic accumulate glucose and fructose.

Five enzymes of the Calvin cycle (Rubisco, glyceraldehyde-3-phosphate dehydrogenase, fructose-1,6-bisphosphatase, sedoheptulose-1,7-bisphosphatase and phosphoribulokinase) are activated in the light: the last four have disulfide bonds reduced through the ferredoxin–**thioredoxin** system, whereas Rubisco has the sugar-phosphate inhibitor bound at its active site removed by Rubisco activase and needs alkalinization of the stroma and a rise in $\ce{Mg^2+}$ concentration to complete carbamylation. As a result the photosynthetic rate takes several minutes of "induction" after the start of illumination to reach steady state, which matters for the use of sunflecks under a canopy ([7.13.9](/7.13.9)). Rubisco activase is inactivated above 35 °C, one cause of the decline of photosynthesis at high temperature.

## 8.2. The Two Reactions of Rubisco and the Physiology of Photorespiration

### 8.2.1. Competition between Carboxylation and Oxygenation

Oxygenation by Rubisco produces one molecule of 2-phosphoglycolate, which is recovered through **photorespiration** (the C2 pathway, [7.1.25](/7.1.25#sec-25.3.1)), at a loss of one already fixed carbon for every two oxygenations. The ratio of oxygenation to carboxylation is $\phi = [\ce{O2}]/(S_{\mathrm{c/o}}[\ce{CO2}])$ ([7.1.25](/7.1.25#eq-25.5)), where $S_{\mathrm{c/o}}$ is the **specificity factor** of Rubisco. In leaf gas exchange a more convenient quantity is the photorespiratory compensation point $\Gamma^*$, the $\ce{CO2}$ concentration at which net assimilation would be zero with photorespiration but no mitochondrial respiration: $\phi = 2\Gamma^*/c_{\mathrm{c}}$, where $c_{\mathrm{c}}$ is the $\ce{CO2}$ concentration in the chloroplast. $\Gamma^*$ increases with temperature as an Arrhenius-type function (Bernacchi et al., 2001):

$$
\Gamma^*(T) = 42.75\,\mathrm{\mu mol\,mol^{-1}} \times \exp\!\left[\frac{37.83\,\mathrm{kJ\,mol^{-1}}\,(T - 298.15\,\mathrm{K})}{298.15\,\mathrm{K} \cdot R\,T}\right], \tag{8.1}
$$
and equals 25, 43 and 70 $\mathrm{\mu mol\,mol^{-1}}$ at 15, 25 and 35 °C. Warming strengthens photorespiration for two reasons: the solubility of $\ce{CO2}$ falls faster than that of $\ce{O2}$, and the specificity factor of Rubisco also falls with temperature.

The carbon lost by a C3 leaf, $0.5\phi$, thus depends on both temperature and $\ce{CO2}$ concentration (Figure 4). Taking intercellular $\ce{CO2}$ as 0.7 of atmospheric, in today's atmosphere (about $420\,\mathrm{\mu mol\,mol^{-1}}$) the loss is about 15% at 25 °C and about 24% at 35 °C; at 35 °C under the last glacial atmosphere ($180\,\mathrm{\mu mol\,mol^{-1}}$) the loss was as high as 56%.

![Carbon lost to photorespiration in C3 photosynthesis as a function of leaf temperature and atmospheric CO₂. $\Gamma^*$ is calculated from Eq. (8.1) with intercellular CO₂ $c_{\mathrm{i}} = 0.7c_{\mathrm{a}}$ (mesophyll resistance neglected), and the fraction lost is $0.5\phi = \Gamma^*/c_{\mathrm{i}}$. A: contours of the fraction lost; dashed lines are the CO₂ concentrations of the last glacial period (180), the preindustrial period (280), today (about 420) and a high-emission future (700 µmol mol⁻¹); the thick green line marks where the ATP consumed per net CO₂ fixed by C3, $(3 + 3.5\phi)/(1 - 0.5\phi)$, equals that of C4 (5.5 ATP at 20% leakage, Eq. (8.5)); to its lower right (hotter, lower CO₂) C4 is more economical: at 180, 280, 420 and 700 µmol mol⁻¹ the crossover temperatures are about 15, 23, 31 and 42 °C. B: fraction lost against temperature at four CO₂ concentrations](./plots/photorespiration-map.py)

### 8.2.2. The CO₂ Compensation Point

Net assimilation $A$ of a leaf in the light decreases as $\ce{CO2}$ concentration falls; the $\ce{CO2}$ concentration at which net assimilation is zero is the **CO₂ compensation point** $\Gamma$ ([7.1.25](/7.1.25#def-25.3.3)). It is higher than $\Gamma^*$ because, besides photorespiration, mitochondria continue to respire in the light (day respiration $R_{\mathrm{d}}$). Within the Rubisco-limited range, $A = V_{\mathrm{cmax}}(c - \Gamma^*)/(c + K) - R_{\mathrm{d}}$ ($K = K_{\mathrm{c}}(1 + O/K_{\mathrm{o}})$ is the apparent Michaelis constant of Rubisco for $\ce{CO2}$ in the presence of competition by $\ce{O2}$, see Eq. (9.3)); setting $A = 0$ gives

$$
\Gamma = \frac{\Gamma^* + K\,R_{\mathrm{d}}/V_{\mathrm{cmax}}}{1 - R_{\mathrm{d}}/V_{\mathrm{cmax}}}. \tag{8.2}
$$

**Example 8.2.1** At 25 °C take $\Gamma^* = 42.75$, $K_{\mathrm{c}} = 404.9\,\mathrm{\mu mol\,mol^{-1}}$, $K_{\mathrm{o}} = 278.4\,\mathrm{mmol\,mol^{-1}}$ and $O = 210\,\mathrm{mmol\,mol^{-1}}$ (Bernacchi et al., 2001); then $K = 404.9 \times (1 + 210/278.4) = 710\,\mathrm{\mu mol\,mol^{-1}}$. If $V_{\mathrm{cmax}} = 60$ and $R_{\mathrm{d}} = 1\,\mathrm{\mu mol\,m^{-2}\,s^{-1}}$, then by Eq. (8.2), $\Gamma = (42.75 + 710/60)/(1 - 1/60) = 54.8/0.983 = 55.5\,\mathrm{\mu mol\,mol^{-1}}$. Day respiration raises the compensation point about 13 units above $\Gamma^*$.

:::

The CO₂ compensation point of C3 plants is generally 40–100 $\mathrm{\mu mol\,mol^{-1}}$ at 25 °C and rises with temperature; that of C4 plants is 0–10 $\mathrm{\mu mol\,mol^{-1}}$ and is almost unaffected by $\ce{O2}$ and temperature. A classical demonstration puts a C3 plant and a C4 plant together in a sealed transparent container in the light: both draw $\ce{CO2}$ down to their own compensation points, the C4 plant pulling the concentration below the compensation point of the C3 plant, so that the C3 plant becomes a net releaser even in the light, the carbon it releases is taken up by the C4 plant, and after a few weeks the C3 plant dies. On this basis Chinese textbooks call C3 plants "high-compensation-point plants" and C4 plants "low-compensation-point plants".

### 8.2.3. Physiological Significance of Photorespiration

There are three kinds of direct evidence for photorespiration: $\ce{O2}$ inhibits photosynthesis of C3 leaves (the Warburg effect: lowering $\ce{O2}$ in air from 21% to 2% raises net photosynthesis of C3 leaves by about one third at 25 °C and leaves C4 leaves almost unchanged); an illuminated C3 leaf released $\ce{CO2}$ at a rate higher than the subsequent dark respiration for a minute or two after the light is suddenly turned off (the postillumination $\ce{CO2}$ burst, from glycine decarboxylation still in progress); and total carboxylation measured by isotope tracing exceeds net assimilation.

In today's atmosphere photorespiration consumes a large amount of carbon and energy of C3 plants ([7.1.25](/7.1.25#sec-25.3.1)), but it cannot simply be regarded as waste. As long as Rubisco oxygenates, recovery of 2-phosphoglycolate is necessary: mutants lacking any enzyme of the C2 pathway grow normally in high $\ce{CO2}$ and die in air (the "photorespiratory phenotype"). Beyond this, several other functions of photorespiration have been proposed:

| Function | Content | Status |
|---|---|---|
| Removing toxic intermediates | 2-phosphoglycolate inhibits triose-phosphate isomerase and glyoxylate inhibits activation of Rubisco | established: the fundamental reason the C2 pathway exists |
| Recovering carbon | 3 of the 4 carbons in two glycolates return to the Calvin cycle as 3-phosphoglycerate | established |
| Dissipating excess light energy and reducing power | each oxygenation consumes about 3.5 ATP and 2 NADPH equivalents; sustains electron flow when stomata close and $c_{\mathrm{c}}$ is low, reducing production of **reactive oxygen species** | supported by evidence; together with other electron sinks (Mehler reaction, cyclic electron flow) it relieves **photoinhibition** ([7.13.7](/7.13.7#sec-7.5.1)) |
| Link to nitrogen metabolism | synthesis of glycine and serine; $\ce{NH3}$ released in photorespiration is refixed by GS–GOGAT; nitrate assimilation in leaves depends on reducing power and metabolic flux supplied by photorespiration, and is weaker in high $\ce{CO2}$ | supported by evidence; mechanism still under study |
| Redox and signaling | $\ce{H2O2}$ produced by glycolate oxidase in peroxisomes participates in stress and immune signaling | supported by evidence |

In agriculture, therefore, the effort to suppress photorespiration is not to remove the C2 pathway (which would be lethal) but to reduce oxygenation itself (by raising $\ce{CO2}$ in the chloroplast through $\ce{CO2}$ enrichment in greenhouses or introduction of $\ce{CO2}$-concentrating mechanisms) or to shorten the recovery path (photorespiratory bypasses inside the chloroplast, [7.1.25](/7.1.25#sec-25.3.1)). Early photorespiration inhibitors (such as α-hydroxysulfonates, which inhibit glycolate oxidase) cause glycolate accumulation and do not raise net photosynthesis, and are no longer used.

## 8.3. C4 Plants

### 8.3.1. Characteristics of C4 Plants

**Definition 8.3.1 (C4 Plant)** A plant in which PEPC in mesophyll cells fixes $\ce{HCO3-}$ into a four-carbon dicarboxylic acid, which is then carried to the cells containing Rubisco and decarboxylated there to raise the $\ce{CO2}$ concentration, that is, a plant that assimilates $\ce{CO2}$ by the **C4 pathway** in cooperation with the Calvin cycle, is called a **C4 plant**.

There are about 8000 species of C4 plants, only about 3% of vascular plant species, yet they contribute about 23% of terrestrial gross primary production (Still et al., 2003). They are concentrated in the grasses (about 4600 species, including maize, sugarcane, sorghum, foxtail millet, proso millet, *Setaria*, *Digitaria* and most savanna grasses), the sedges (about 1300 species) and the Amaranthaceae (including the former Chenopodiaceae), with another 19 families in all including Asteraceae, Euphorbiaceae and Portulacaceae; the C4 pathway has at least 62 independent origins among angiosperms (Section 8.7.1). C4 plants are mostly annual herbs, distributed in the tropics, subtropics and the hot season of temperate regions; on the North American Great Plains grassland south of 40° N is dominated by C4 grasses and north of 45° N by C3 grasses. There are almost no C4 trees (a few Hawaiian *Euphorbia* trees are an exception). Many of the world's worst weeds are C4 plants (*Digitaria*, *Cyperus rotundus*, *Echinochloa*, *Cynodon dactylon*, *Imperata cylindrica* and others).

The leaves of C4 plants usually have **Kranz anatomy** ([7.12.23](/7.12.23#sec-23.5.6)): veins are dense and every mesophyll cell is next to a **bundle sheath** cell; bundle sheath cells are large and contain many chloroplasts; there are numerous **plasmodesmata** between the two cell types for diffusion of C4 and C3 acids. The division of labor between the two cell types is thorough: PEPC, carbonic anhydrase and pyruvate phosphate dikinase (PPDK) are only in mesophyll cells, Rubisco and the Calvin cycle only in the bundle sheath.

### 8.3.2. The Three Decarboxylation Subtypes

**Definition 8.3.2 (Decarboxylation Subtypes of C4 Plants)** According to the main decarboxylase releasing $\ce{CO2}$ in the bundle sheath, C4 plants fall into three biochemical subtypes: the **NADP-malic enzyme type** (NADP-ME type, in which NADP-malic enzyme in bundle sheath chloroplasts decarboxylates malate), the **NAD-malic enzyme type** (NAD-ME type, NAD-malic enzyme in mitochondria) and the **PEP carboxykinase type** (PCK type, in which PEP carboxykinase in the cytosol decarboxylates oxaloacetate).

| | NADP-ME type | NAD-ME type | PCK type |
|---|---|---|---|
| C4 acid moved into the bundle sheath | malate | aspartate | aspartate (and some malate) |
| Site and enzyme of decarboxylation | chloroplast, NADP-malic enzyme (produces NADPH) | mitochondrion, NAD-malic enzyme (aspartate is first converted to oxaloacetate, then reduced to malate) | cytosol, PEP carboxykinase (consumes 1 ATP) |
| C3 compound returned to the mesophyll | pyruvate | alanine | PEP, alanine, pyruvate |
| Bundle sheath chloroplasts | poorly developed grana, lacking PSII, centrifugal (along the outer wall) | with grana, centripetal (on the side toward the vascular bundle) | with grana, centrifugal |
| Leaf anatomy in grasses | one bundle sheath layer (the Kranz cells are the bundle sheath), with a suberized layer in the sheath cell wall | two sheaths (an inner thin-walled bundle sheath and an outer layer of Kranz cells), no suberized layer | two sheaths, with a suberized layer |
| Representative plants | maize, sugarcane, sorghum, foxtail millet, *Digitaria* | proso millet, finger millet, *Amaranthus*, *Portulaca*, *Atriplex* | guinea grass, Rhodes grass, *Zoysia* |

![The three biochemical subtypes of C4 photosynthesis, named for the decarboxylase in the bundle sheath. In each group the mesophyll cell is on the left and the bundle sheath cell on the right, connected by plasmodesmata. Common to all three: PEP carboxylase (PEPC) in the mesophyll cytosol fixes HCO₃⁻ as oxaloacetate (OAA), and the CO₂ released in the bundle sheath is refixed by Rubisco in the Calvin cycle. A: NADP-malic enzyme type (maize, sorghum, sugarcane): OAA is reduced to malate by NADP-malate dehydrogenase in mesophyll chloroplasts; NADP-malic enzyme in bundle sheath chloroplasts releases CO₂ and NADPH; pyruvate returns and PPDK regenerates PEP. B: NAD-malic enzyme type (proso millet, *Amaranthus*, *Atriplex*): OAA is transaminated to aspartate; in the bundle sheath mitochondria aspartate is converted back to OAA, reduced to malate and decarboxylated by NAD-malic enzyme; alanine returns to the mesophyll and is converted to pyruvate and PEP. C: PEP carboxykinase type (guinea grass): aspartate is converted to OAA and PEP carboxykinase in the bundle sheath cytosol decarboxylates it at the cost of one ATP; PEP (partly as alanine or pyruvate) returns to the mesophyll. Dashed lines: transport between cells](./plots/c4-subtypes.py)

The division into three subtypes comes from measurements of enzyme activity in the 1970s (Hatch et al.). Newer flux analyses and transcriptome studies show that the PCK type does not exist independently: PEP carboxykinase always operates as a supplementary route to the NADP-ME or NAD-ME type (maize bundle sheath also has considerable PCK activity), and so-called PCK-type plants in fact decarboxylate with NAD-ME and PCK together, the NADH produced by NAD-malic enzyme in mitochondria supplying ATP to PCK through oxidative phosphorylation (Furbank, 2011; Wang et al., 2014). C4 plants are now often divided into two large classes, NADP-ME and NAD-ME, each of which may have a PCK branch. Chinese sources sometimes write PCK as "PEP carboxylase kinase", which is a different enzyme (the protein kinase that phosphorylates PEPC, see Section 8.3.5); some also wrongly list the C3 grass *Leymus chinensis* as a PCK-type plant.

The bundle sheath chloroplasts of the NADP-ME type lack PSII and do not evolve oxygen, which makes the $\ce{O2}$ concentration in the bundle sheath even lower. NADP-malic enzyme supplies one NADPH per malate decarboxylated, which meets half of what is needed to reduce 3-phosphoglycerate; the other half of the 3-phosphoglycerate is carried to the mesophyll cells to be reduced and returns to the bundle sheath as triose phosphate. In the NADP-ME type, therefore, two shuttles operate simultaneously between the two cell types: malate/pyruvate and 3-phosphoglycerate/triose phosphate.

### 8.3.3. CO₂ Concentration and Leakage

The C4 cycle is an ATP-driven $\ce{CO2}$ pump. The substrate of PEPC is $\ce{HCO3-}$, whose concentration in cytosol at pH about 7.8 is tens of times that of dissolved $\ce{CO2}$; PEPC has high affinity for $\ce{HCO3-}$ and does not react with $\ce{O2}$. A C4 leaf can therefore draw intercellular $\ce{CO2}$ very low ($c_{\mathrm{i}}/c_{\mathrm{a}}$ about 0.3–0.4, against about 0.7 in C3 leaves) while $\ce{CO2}$ in the bundle sheath is pumped to about 10 times atmospheric. Chinese textbooks often contrast "a $K_{\mathrm{m}}$ for $\ce{CO2}$ of 7 µmol for PEPC and 450 µmol for Rubisco"; the real difference between the two enzymes lies in the concentration of the substrates ($\ce{HCO3-}$ versus $\ce{CO2}$) and in competition by $\ce{O2}$, and units must be kept consistent in the comparison (the $K_{\mathrm{c}}$ of Rubisco for $\ce{CO2}$ is about 10–15 µM in solution, equivalent to about $400\,\mathrm{\mu mol\,mol^{-1}}$ in the gas phase).

Not all the $\ce{CO2}$ pumped in is fixed by Rubisco: the $\ce{CO2}$ concentration in the bundle sheath is far higher than in the mesophyll, and part leaks back through the sheath cell wall and plasmodesmata to the mesophyll. The fraction of the PEPC carboxylation rate $V_{\mathrm{p}}$ that leaks out is called the leakiness $\varphi$, generally 0.2–0.3. Let $g_{\mathrm{bs}}$ be the conductance of the bundle sheath to $\ce{CO2}$; at steady state

$$
c_{\mathrm{bs}} - c_{\mathrm{m}} = \frac{\varphi V_{\mathrm{p}}}{g_{\mathrm{bs}}},\qquad A = (1 - \varphi)\,V_{\mathrm{p}}, \tag{8.3}
$$
where $c_{\mathrm{bs}}$ and $c_{\mathrm{m}}$ are the $\ce{CO2}$ concentrations in the bundle sheath and mesophyll (as gas-phase mole fractions). The suberized layer in the sheath cell wall and the low surface-to-volume ratio of sheath cells make $g_{\mathrm{bs}}$ very small, about one hundredth of the mesophyll conductance.

**Example 8.3.1** A maize leaf has net assimilation $A = 40\,\mathrm{\mu mol\,m^{-2}\,s^{-1}}$ and leakiness $\varphi = 0.2$, so $V_{\mathrm{p}} = 40/0.8 = 50$ and the leak flux is $10\,\mathrm{\mu mol\,m^{-2}\,s^{-1}}$. Taking $g_{\mathrm{bs}} = 3\,\mathrm{mmol\,m^{-2}\,s^{-1}}$, Eq. (8.3) gives $c_{\mathrm{bs}} - c_{\mathrm{m}} = 10\times10^{-6}/0.003 = 3.3\times10^{-3}$, that is $3300\,\mathrm{\mu mol\,mol^{-1}}$; with $c_{\mathrm{m}} \approx 100$ in the mesophyll, the bundle sheath has about $3400\,\mathrm{\mu mol\,mol^{-1}}$, 8 times atmospheric. At this concentration $\phi = 2\Gamma^*/c_{\mathrm{bs}} = 2 \times 42.75/3400 = 0.025$ and photorespiration loses only 1.3% of the carbon, in agreement with the measured "photorespiration is about 2%–3% of photosynthesis". If $g_{\mathrm{bs}}$ were doubled, the same leakiness would sustain only half the concentration difference, or to sustain the same concentration more would have to leak.

### 8.3.4. The Energy Budget

The ATP required by a C3 leaf per net $\ce{CO2}$ fixed increases with photorespiration ([7.1.25](/7.1.25#sec-25.4.1)):

$$
n_{\mathrm{ATP}}^{\mathrm{C3}} = \frac{3 + 3.5\,\phi}{1 - 0.5\,\phi}. \tag{8.4}
$$

In a C4 leaf, in addition to the Calvin cycle, each turn of the C4 cycle consumes 2 high-energy phosphate bonds at PPDK (ATP → AMP + $\mathrm{PP_i}$), and because of leakage $1/(1 - \varphi)$ turns of the C4 cycle are needed per net $\ce{CO2}$ fixed:

$$
n_{\mathrm{ATP}}^{\mathrm{C4}} = 3 + \frac{2}{1 - \varphi}, \tag{8.5}
$$
which is 5 without leakage and 5.5 at $\varphi = 0.2$. The NADPH requirement is the same in both (2 per $\ce{CO2}$). Differences among subtypes: the NADP-ME and NAD-ME types both regenerate PEP with PPDK and have the same theoretical value; the PCK branch consumes 1 ATP in the bundle sheath and returns PEP directly, saving the 2 of PPDK, so that if all decarboxylation were through PCK the theoretical cost would be about 4 ATP per $\ce{CO2}$, which may be why the PCK branch is so widespread. The statement in Chinese textbooks that "C4 consumes 2 more ATP per $\ce{CO2}$ fixed, that is $\ce{CO2}$:ATP:NADPH = 1:5:2" corresponds to the NADP-ME or NAD-ME type without leakage.

**Example 8.3.2** Use Eqs. (8.4) and (8.5) to decide which is more economical. At 25 °C and $c_{\mathrm{c}} = 250\,\mathrm{\mu mol\,mol^{-1}}$, $\phi = 2 \times 42.75/250 = 0.34$, and C3 needs $(3 + 1.20)/(1 - 0.17) = 5.06$ ATP, slightly below the 5.5 of C4. At 35 °C $\Gamma^* = 70$, $\phi = 0.56$, C3 needs $(3 + 1.96)/(1 - 0.28) = 6.9$, and C4 is much cheaper. Under light-limited conditions ATP consumption directly determines the quantum yield, so the quantum yield of C3 leaves is higher than that of C4 at low temperature and lower at high temperature, with a crossover temperature of about 25–30 °C (Ehleringer and Björkman, 1977; [7.13.9](/7.13.9)).

:::

The benefit of C4 is not only in energy. $\ce{CO2}$ concentration lets Rubisco work at nearly saturating substrate, so a C4 leaf needs only a fraction of the Rubisco of a C3 leaf to reach a higher photosynthetic rate, and its photosynthetic nitrogen-use efficiency is high; a C4 leaf can maintain the same assimilation at lower stomatal conductance, and its water-use efficiency is about twice that of C3 ([7.13.3](/7.13.3), [7.13.10](/7.13.10)). The costs are more ATP, more complex anatomy and gene regulation, and stronger sensitivity to low temperature.

### 8.3.5. Light Regulation of Key Enzymes and Cold Sensitivity

Three enzymes of the C4 pathway, like those of the Calvin cycle, are regulated by light, so that the C4 cycle runs only in the light and when the Calvin cycle can use the $\ce{CO2}$ (reaction details in [7.1.25](/7.1.25#sec-25.4.1)):

| Enzyme | Regulation | Effect in light |
|---|---|---|
| PEPC | PEPC kinase phosphorylates a Ser residue near the N terminus (synthesis of the kinase is light-induced); feedback inhibition by malate and aspartate, activation by glucose-6-phosphate and glycine | phosphorylated PEPC is insensitive to inhibition by malate, and its activity rises |
| PPDK | bifunctional PPDK regulatory protein: in the dark it phosphorylates a Thr residue using ADP as donor and inactivates the enzyme, and in the light it reactivates it by phosphorolysis with $\mathrm{P_i}$ | activity increases with light intensity |
| NADP-malate dehydrogenase | disulfide bonds reduced by the ferredoxin–thioredoxin system | activated in light, inactivated in the dark |

The regulation of PEPC runs in opposite directions in C4 and CAM plants: the PEPC kinase of C4 plants is expressed by day and that of CAM plants at night (Section 8.4.1), and both are controlled by phosphorylation by a **protein kinase** rather than by synthesis of new enzyme.

Most C4 plants are not cold-tolerant. PPDK is a tetramer unstable in the cold, dissociating and losing activity below 10 °C; in maize the content and activity of PPDK fall markedly in the cold and photosynthesis declines. Cold-tolerant C4 plants (such as *Miscanthus* × *giganteus*, which grows in southern England) maintain their PPDK and Rubisco content in the cold.

### 8.3.6. Single-Cell C4

Kranz anatomy is not required for C4 photosynthesis. The Central Asian desert chenopod *Suaeda aralocaspica* and at least two species of *Bienertia* complete the C4 cycle within a single green cell: in the former the chloroplasts are distributed at the two ends of the cell (the outer end carries out PEPC carboxylation and the PPDK reaction, the inner end decarboxylates and runs the Calvin cycle), and in the latter the cell has a central cytoplasmic compartment connected to the periphery by cytoplasmic bridges, in which chloroplasts containing Rubisco and mitochondria are clustered. The two kinds of chloroplast differentiate different enzyme compositions within one cell, and the large central vacuole or the long cytoplasmic distance limits back-leakage of $\ce{CO2}$. The aquatic *Hydrilla verticillata* induces a single-cell C4 cycle in warm water of low $\ce{CO2}$. PEPC-dependent carbon concentration also exists in diatoms.

## 8.4. CAM Plants

### 8.4.1. The Four Phases of CAM

**Definition 8.4.1 (CAM Plant)** A plant whose stomata are open at night, in which PEPC fixes $\ce{CO2}$ and stores it as malate in the vacuole, and whose stomata are closed by day while malate is decarboxylated and the $\ce{CO2}$ refixed by the Calvin cycle in the same cell, that is, a plant carrying out **crassulacean acid metabolism**, is called a **CAM plant**.

CAM plants make up about 6% of vascular plant species and are concentrated in the Crassulaceae, Cactaceae, Agavaceae, Bromeliaceae and Orchidaceae, including many epiphytes and desert succulents, and crops such as pineapple, agave and prickly pear; the aquatic quillwort *Isoetes* takes up $\ce{CO2}$ from water at night and is also a CAM plant. The name of crassulacean acid metabolism comes from the Crassulaceae: their leaves taste sour in the morning and not sour in the evening.

According to the daily course of stomata and enzyme activity, CAM is divided into four phases (Osmond, 1978; Figure 2):

| Phase | Time | Stomata | Carbon metabolism |
|---|---|---|---|
| I | night | open | PEPC fixes $\ce{CO2}$ (including respired $\ce{CO2}$), malate accumulates in the vacuole; vacuolar pH can fall to 3–4 and malate reach more than 100 mM |
| II | early morning | briefly open | PEPC activity falls and Rubisco activity rises, both fixing external $\ce{CO2}$ |
| III | day | closed | malate leaves the vacuole and is decarboxylated (by NADP-ME, NAD-ME or PCK depending on the plant), intercellular $\ce{CO2}$ can rise to more than ten times atmospheric, Rubisco refixes it, and the products are converted to starch or soluble sugars |
| IV | late afternoon | reopen | after malate is exhausted Rubisco fixes external $\ce{CO2}$ directly (C3 fashion); PEPC is then reactivated, passing to phase I |

![The four phases of CAM, drawn from a schematic numerical model; time runs from dusk (18:00) to dusk of the next day, and shading is night. A: net CO₂ uptake (solid line) and relative stomatal conductance (dashed line): in phase I CO₂ is taken up by PEPC at night (peak about 6 µmol m⁻² s⁻¹), phase II has a brief uptake peak in the early morning, in phase III stomata are closed and there is no gas exchange, and in phase IV stomata reopen in the late afternoon and fixation is directly by Rubisco. B: vacuolar malate (solid line, integrating the night-time PEPC fixation over 1.8 L tissue water per square meter of leaf, decarboxylated linearly during phase III by day) and intercellular CO₂ (dashed line, schematic): malate rises to about 130 mM at night and is consumed by day; CO₂ released by decarboxylation while stomata are closed raises intercellular CO₂ to about 6000 µmol mol⁻¹. Values are schematic](./plots/cam-phases.py)

The switching between phases is set by the circadian clock: the PEPC kinase gene of CAM plants is under clock control and transcribed at night, so that PEPC is phosphorylated and insensitive to malate (the "night form"); by day PEPC is dephosphorylated and strongly inhibited by the accumulated malate (the "day form"), which prevents the decarboxylated $\ce{CO2}$ from being recarboxylated in a futile cycle.

### 8.4.2. Energy and Water

The energy cost of CAM is higher than that of C4: besides the 3 ATP and 2 NADPH of the Calvin cycle, each $\ce{CO2}$ requires regeneration of PEP through PPDK (2 high-energy phosphate bonds), pumping malate into the vacuole against a concentration gradient (the tonoplast $\mathrm{H^+}$-ATPase needs about 1 ATP per malate pumped in) and synthesis and breakdown of starch between day and night; the frequently cited estimate is about 6.5 ATP and 2 NADPH per $\ce{CO2}$ ([7.1.25](/7.1.25#sec-25.4.2)). The order of energy conversion efficiency is C3 > C4 > CAM (when photorespiration is not considered).

What CAM buys is water. At night leaf temperature is low and air humidity high, so the difference in water vapor concentration between leaf and air is much smaller, and the same stomatal opening loses only a fraction of the water lost by day. On a molar basis, a C3 plant transpires about 400 molecules of water per molecule of $\ce{CO2}$ fixed, a C4 plant about 150 and a CAM plant about 50 ([7.13.3](/7.13.3#sec-3.4.5)).

**Example 8.4.1** A CAM leaf fixes $\ce{CO2}$ at a mean rate of $5\,\mathrm{\mu mol\,m^{-2}\,s^{-1}}$ during a 12 h night, an amount of $5\times10^{-6} \times 43\,200 = 0.216\,\mathrm{mol\,m^{-2}}$. If the leaf contains 1.8 L of cell sap per square meter, when all is stored as malate the concentration rises by $0.216/1.8 = 0.12\,\mathrm{mol\,L^{-1}}$, that is 120 mM; malate is a dibasic acid, and the titratable acidity increases by $240\,\mathrm{\mu eq\,mL^{-1}}$. The storage capacity is limited by vacuole volume, which is why CAM leaves are succulent with huge vacuoles: for the same leaf area, the thicker the leaf the more carbon can be stored in a night. By day this malate is decarboxylated during the phase III of about 8 h, at a mean release rate of $0.216/28\,800\,\mathrm{s} = 7.5\,\mathrm{\mu mol\,m^{-2}\,s^{-1}}$, comparable to the photosynthetic rate of a medium C3 leaf.

### 8.4.3. Facultative CAM and the Plasticity of CAM

The degree of CAM expression varies greatly among species and environments:

- Obligate CAM: mature tissues always carry out CAM, as in most cacti and *Kalanchoe* of the Crassulaceae.
- Facultative (inducible) CAM: C3 photosynthesis when water is plentiful, switching to CAM under drought or salt stress. The ice plant (*Mesembryanthemum crystallinum*) induces expression of PEPC and other genes within a few days under salt stress and is the model plant for studying CAM induction; among tropical *Clusia* there are C3, CAM and trees that switch reversibly between the two.
- CAM idling: in severe drought stomata are closed day and night and only respired $\ce{CO2}$ is refixed at night, with no net carbon gain but with maintenance of metabolism and photoprotection while waiting for rain.
- CAM cycling: stomata open by day for C3 fixation and close at night, only recycling respiratory $\ce{CO2}$ and producing a small daily fluctuation of acid.
- Coexistence of C4 and CAM: purslane (*Portulaca oleracea*) is a C4 plant that induces CAM in the same leaf in drought, the two cycles sharing some enzymes.

Because of the high water-use efficiency of CAM plants, introducing certain CAM traits (night-time stomatal opening, malate storage) into C3 crops, and growing agave and cacti on semiarid marginal land as forage and bioenergy crops, are current research directions.

## 8.5. Comparison of C3, C4 and CAM Plants

| Feature | C3 plants | C4 plants | CAM plants |
|---|---|---|---|
| Leaf structure | no Kranz anatomy; bundle sheath cells with few chloroplasts | Kranz anatomy (or single-cell C4); dense veins | succulent, large vacuoles, little differentiation of palisade and spongy tissue |
| Chloroplasts | only in mesophyll, one kind | two kinds, in mesophyll and bundle sheath (sheath of NADP-ME type lacks PSII) | one kind in mesophyll |
| First carboxylase | Rubisco | PEPC | PEPC (at night) |
| $\ce{CO2}$ compensation point / $\mathrm{\mu mol\,mol^{-1}}$ | 40–100 | 0–10 | 0–5 in the dark |
| Photorespiration | substantial, 15%–30% of fixed carbon lost at 25–30 °C | about 2%–3% of photosynthesis | low (higher in phase IV) |
| Inhibition of photosynthesis by $\ce{O2}$ | marked | almost none | almost none by day |
| Maximum net photosynthetic rate / $\mathrm{\mu mol\,m^{-2}\,s^{-1}}$ | 15–40 | 30–60 | 5–15 |
| Light saturation | often saturates at one half to two thirds of full sunlight | often still unsaturated in full sunlight | — |
| Photosynthetic optimum temperature | 20–30 °C | 30–40 °C | about 35 °C by day, lower optimum for night fixation |
| Quantum yield (30 °C) / $\mathrm{mol\,CO_2\,mol^{-1}}$ photons | about 0.05, falling with rising temperature | about 0.05, independent of temperature | lower |
| Energy per $\ce{CO2}$ (without photorespiration) | 3 ATP + 2 NADPH | 5–5.5 ATP + 2 NADPH | about 6.5 ATP + 2 NADPH |
| Intercellular $\ce{CO2}$, $c_{\mathrm{i}}/c_{\mathrm{a}}$ | about 0.7 | about 0.3–0.4 | low at night, very high by day |
| Transpiration ratio / $\mathrm{mol\,H_2O\,mol^{-1}\,CO_2}$ | about 400 | about 150 | about 50 |
| Photosynthetic nitrogen-use efficiency | low (Rubisco is a large fraction of leaf nitrogen) | high | — |
| Leaf $\delta^{13}\mathrm{C}$ | about −28‰ (−20 to −35‰) | about −14‰ (−10 to −17‰) | −10 to −22‰, between the two |
| Typical habitat and examples | mild and moist; wheat, rice, soybean, trees | hot, high light, seasonal drought; maize, sugarcane, sorghum, foxtail millet | arid, epiphytic; cacti, pineapple, agave, orchids |

The values in the table are typical ranges and vary greatly with species and growth conditions. The most important conclusion is that no type is superior in all environments. C4 wins in high temperature, strong light, drought and low $\ce{CO2}$, C3 is more economical in cool conditions, weak light (higher quantum yield) and high $\ce{CO2}$, and CAM trades growth rate for survival in extreme drought.

## 8.6. Carbon Isotope Discrimination

### 8.6.1. δ¹³C and Δ

Carbon has two stable **isotopes**, $^{12}\mathrm{C}$ at about 98.9% and $^{13}\mathrm{C}$ at about 1.1%. Plants prefer the lighter $^{12}\mathrm{CO_2}$ in photosynthesis, so the $^{13}\mathrm{C}/^{12}\mathrm{C}$ of plant material is lower than that of the atmosphere. Isotopic composition is expressed as the per mille deviation from a standard (Pee Dee belemnite carbonate, now the VPDB standard):

$$
\delta^{13}\mathrm{C} = \left(\frac{R_{\mathrm{sample}}}{R_{\mathrm{standard}}} - 1\right) \times 1000,\qquad R = \frac{^{13}\mathrm{C}}{^{12}\mathrm{C}}. \tag{8.6}
$$
where δ is in ‰. The $\delta^{13}\mathrm{C}$ of atmospheric $\ce{CO2}$ today is about −8.5‰ (the carbon in fossil fuels comes from ancient plants and is rich in $^{12}\mathrm{C}$; its combustion has gradually lowered the $\delta^{13}\mathrm{C}$ of the atmosphere from about −6.4‰ before industrialization).

**Definition 8.6.1 (Carbon Isotope Discrimination)** The selective exclusion of $^{13}\mathrm{C}$ by plants in photosynthesis is called **carbon isotope discrimination** and is measured by

$$
\Delta = \frac{\delta_{\mathrm{a}} - \delta_{\mathrm{p}}}{1 + \delta_{\mathrm{p}}} \approx \delta_{\mathrm{a}} - \delta_{\mathrm{p}} \tag{8.7}
$$
where $\delta_{\mathrm{a}}$ and $\delta_{\mathrm{p}}$ are the $\delta^{13}\mathrm{C}$ of atmospheric $\ce{CO2}$ and of the plant (δ taken as a decimal fraction in this equation). $\Delta$ does not depend on the standard chosen and is not affected by changes in atmospheric $\delta^{13}\mathrm{C}$, which makes comparison convenient.

Discrimination arises from two processes. When $\ce{CO2}$ diffuses from the atmosphere through the stomata into the leaf, $^{13}\mathrm{CO_2}$ diffuses slightly more slowly, a fractionation $a = 4.4$‰; the intrinsic discrimination of Rubisco against $^{13}\mathrm{CO_2}$ in carboxylation is about 29–30‰, and with a small contribution of PEPC the net carboxylation fractionation of a C3 leaf is $b \approx 27$‰. Which process is expressed depends on how much $\ce{CO2}$ is in the leaf. The model of Farquhar, O'Leary and Berry (1982) is

$$
\Delta_{\mathrm{C3}} = a + (b - a)\,\frac{c_{\mathrm{i}}}{c_{\mathrm{a}}}. \tag{8.8}
$$
When the stomata are wide open, $c_{\mathrm{i}} \to c_{\mathrm{a}}$, diffusion is unrestricted, the discrimination of Rubisco is fully expressed, and $\Delta \to b$; when the stomata are almost closed, nearly all the $\ce{CO2}$ entering the leaf is fixed, carboxylation cannot "choose", and $\Delta \to a$.

In C4 plants PEPC fixes $\ce{HCO3-}$; the equilibrium fractionation of $\ce{CO2}$ dissolving and hydrating to $\ce{HCO3-}$ enriches $^{13}\mathrm{C}$ in $\ce{HCO3-}$, and together with the discrimination of about 2‰ by PEPC itself the net effect is $b_4 \approx -5.7$‰ (25 °C); in the bundle sheath the discrimination of Rubisco is expressed only on the leaked part of the $\ce{CO2}$ (Farquhar, 1983):

$$
\Delta_{\mathrm{C4}} = a + (b_4 + b_3\varphi - a)\,\frac{c_{\mathrm{i}}}{c_{\mathrm{a}}}, \tag{8.9}
$$
where $b_3 \approx 30$‰ and $\varphi$ is the leakiness. Since $b_4 + b_3\varphi - a$ is close to zero, $\Delta$ of C4 plants is only 3–5‰ and hardly varies with $c_{\mathrm{i}}/c_{\mathrm{a}}$ (Figure 3). CAM plants fix with PEPC at night and directly with Rubisco in phases II and IV, so their $\delta^{13}\mathrm{C}$ lies between C4 and C3 according to the proportion of the two, and can be used to estimate the share of night-time fixation.

**Example 8.6.1** For a C3 leaf with $c_{\mathrm{i}}/c_{\mathrm{a}} = 0.7$: by Eq. (8.8), $\Delta = 4.4 + 22.6 \times 0.7 = 20.2$‰; by Eq. (8.7), $\delta_{\mathrm{p}} = (\delta_{\mathrm{a}} - \Delta)/(1 + \Delta) = (-8.5 - 20.2)/1.0202 = -28.1$‰. For a C4 leaf with $c_{\mathrm{i}}/c_{\mathrm{a}} = 0.4$ and $\varphi = 0.3$: $b_4 + b_3\varphi - a = -5.7 + 9.0 - 4.4 = -1.1$‰, $\Delta = 4.4 - 0.44 = 4.0$‰, $\delta_{\mathrm{p}} = -12.5$‰. The two fall within the typical ranges of C3 (about −28‰) and C4 (about −14‰), differing by about 15‰, which is easily distinguished by mass spectrometry.

![Carbon isotope discrimination and δ¹³C of the three photosynthetic plant types. A: discrimination Δ against $c_{\mathrm{i}}/c_{\mathrm{a}}$. C3 by Eq. (8.8) with $a = 4.4$‰ and $b = 27$‰; C4 by Eq. (8.9) with $b_4 = -5.7$‰, $b_3 = 30$‰ and leakiness φ = 0.2 (solid line) and 0.35 (dashed line); dots are typical operating points ($c_{\mathrm{i}}/c_{\mathrm{a}}$ = 0.7 for C3, 0.4 for C4). The right axis gives the corresponding plant δ¹³C for atmospheric δ¹³C = −8.5‰. A C3 leaf closing its stomata in drought has a falling $c_{\mathrm{i}}/c_{\mathrm{a}}$ and Δ decreases along the line; C4 has small Δ that hardly varies with $c_{\mathrm{i}}/c_{\mathrm{a}}$. B: schematic frequency distribution of leaf δ¹³C: C3 averages about −28‰, C4 about −14‰, and CAM plants lie between the two according to the proportion of night-time fixation; the dashed line is the δ¹³C of atmospheric CO₂. B is schematic, not data](./plots/isotopes.py)

### 8.6.2. Δ and Water-Use Efficiency

Equation (8.8) links an easily measured quantity (the $\delta^{13}\mathrm{C}$ of plant dry matter) with a quantity that is hard to measure over long periods (the $c_{\mathrm{i}}/c_{\mathrm{a}}$ averaged over the whole growth period), and the latter in turn determines the **water-use efficiency** of the leaf. By **Fick's law**, both photosynthetic rate and transpiration rate are proportional to stomatal conductance: $A = g_{\mathrm{s}}(c_{\mathrm{a}} - c_{\mathrm{i}})/1.6$ and $E = g_{\mathrm{s}}\,D$, where $g_{\mathrm{s}}$ is the stomatal conductance to water vapor (the diffusion coefficient of $\ce{CO2}$ is 1/1.6 that of water vapor) and $D$ is the difference in water vapor mole fraction between leaf and air. Thus

$$
\frac{A}{E} = \frac{c_{\mathrm{a}}\,(1 - c_{\mathrm{i}}/c_{\mathrm{a}})}{1.6\,D} = \frac{c_{\mathrm{a}}\,(b - \Delta)}{1.6\,D\,(b - a)}. \tag{8.10}
$$

At the same $c_{\mathrm{a}}$ and $D$, the smaller $\Delta$ is, the higher the water-use efficiency. For example, at $c_{\mathrm{a}} = 420\,\mathrm{\mu mol\,mol^{-1}}$ and $D = 0.02$ (a difference between saturation vapor pressure at leaf temperature and air vapor pressure of about 2 kPa), a C3 leaf ($c_{\mathrm{i}}/c_{\mathrm{a}} = 0.7$) has $A/E = 420\times10^{-6} \times 0.3/(1.6 \times 0.02) = 3.9\,\mathrm{mmol\,CO_2\,mol^{-1}\,H_2O}$ and a C4 leaf (0.4) has $7.9\,\mathrm{mmol\,mol^{-1}}$, exactly twice. On this basis Farquhar and Richards (1984) proposed using $\Delta$ as a screening index for water-use efficiency; Australian breeders selecting for low $\Delta$ released wheat cultivars with higher yield in dry cropping regions (such as Drysdale and Rees; Condon et al., 2004). Equation (8.10) also shows that when the same plant closes its stomata in drought, $\Delta$ falls and the $\delta^{13}\mathrm{C}$ of the tissue rises; along the Australian rainfall gradient from rainforest to desert, the $\delta^{13}\mathrm{C}$ of C3 leaves rises as rainfall decreases.

### 8.6.3. Other Applications

- Identifying the source of foods: cane sugar (C4) and beet sugar (C3) are chemically identical but their $\delta^{13}\mathrm{C}$ differs by about 14‰; adulteration of honey with corn syrup and of fruit juice with sucrose can both be detected by isotopes.
- Food webs and paleodiets: the $\delta^{13}\mathrm{C}$ of animal tissue reflects the photosynthetic type of the plants eaten. North Americans have higher $\delta^{13}\mathrm{C}$ than Europeans, reflecting the share of maize in the diet; segmental measurements of elephant tail hair reproduced the switching of elephants between tree leaves (C3) and grasses (C4) from the rainy to the dry season; $\delta^{13}\mathrm{C}$ of ancient human bone records the spread of maize agriculture in the Americas and millet agriculture in northern China.
- Paleoecology: $\delta^{13}\mathrm{C}$ of paleosol carbonate and mammalian tooth enamel shows that C4 grasslands expanded rapidly at low latitudes worldwide in the late Miocene, about 8 to 6 million years ago (Cerling et al., 1997).
- Tree rings: year-by-year $\delta^{13}\mathrm{C}$ records the water status of the growing season and the history of atmospheric $\ce{CO2}$.

## 8.7. Evolution of C4 Photosynthesis and C4 Rice

### 8.7.1. Evolution of C4 Photosynthesis

C4 photosynthesis is one of the most prominent examples of **convergent evolution**: it has arisen independently more than 60 times among angiosperms, the earliest origin about 30 million years ago in the Oligocene, coinciding with the fall of atmospheric $\ce{CO2}$ from several thousand $\mathrm{\mu mol\,mol^{-1}}$ to near today's level; it appeared many times afterward in the aridification and low-$\ce{CO2}$ period of the Miocene. The enzymes used (PEPC, NADP-ME, PPDK and others) already exist in C3 plants, serving anaplerotic functions, guard cell metabolism, seed development and so on; what evolution did was change their sites of expression, expression levels and regulation, together with changes in anatomy.

Because of the many independent origins, intermediate types between C3 and C4 have been retained in many groups, the best known being the genus *Flaveria* of the Asteraceae, which includes C3, C3–C4 intermediate, C4-like and fully C4 species. Comparing these species allows a rough evolutionary route to be inferred:

1. Preconditions: veins become dense, bundle sheath cells enlarge, and chloroplasts and mitochondria in the sheath increase ("proto-Kranz").
2. C2 photosynthesis: the glycine decarboxylase of photorespiration is expressed only in bundle sheath mitochondria, so glycine produced in the mesophyll must be carried to the sheath for decarboxylation, and the $\ce{CO2}$ released is concentrated and refixed in the sheath. This "photorespiratory pump" lowers the CO₂ compensation point to $10\text{–}30\,\mathrm{\mu mol\,mol^{-1}}$ and has arisen independently in *Moricandia* of the Brassicaceae, certain *Panicum* species of the Poaceae and intermediate species of *Flaveria*.
3. Establishment of the C4 cycle: PEPC and other enzymes are strongly expressed in the mesophyll and Rubisco in the sheath, the C4 cycle gradually replaces the glycine shuttle as the main $\ce{CO2}$ pump, and finally Rubisco disappears from the mesophyll.

Heckmann et al. (2013) built a mathematical model of the C3 to C4 transition from the biochemical parameters of *Flaveria* and found that every step along this route increased carbon assimilation, so that the fitness landscape is "smooth", which explains why C4 photosynthesis has arisen so often.

### 8.7.2. Introducing C4 Photosynthesis into Rice

Rice and wheat are C3 crops. If rice could carry out C4 photosynthesis, models estimate that radiation-use efficiency could rise by about 50% while the requirements for water and nitrogen fall, which is considered one of the routes to raising grain yield without increasing arable land. The international C4 Rice Consortium has worked on this since 2008, centered on the International Rice Research Institute, and needs to accomplish three things at the same time:

| Requirement | Content | Progress |
|---|---|---|
| Biochemistry | correct expression in mesophyll and bundle sheath of the enzymes and metabolite transporters of the C4 cycle | the five enzymes of the NADP-ME type have been expressed together in rice from a single vector (Ermakova et al., 2021) and labeling of C4 acids detected, but no effective $\ce{CO2}$ concentration has formed |
| Anatomy | increase vein density, enlarge bundle sheath cells and fill them with chloroplasts | several regulators controlling vein formation and sheath-cell chloroplast development identified; a complete Kranz structure cannot yet be built |
| Regulation | coordinated expression of the whole gene set by cell type and light | common cis-elements and transcription factors being sought in C4 plants such as maize and *Setaria* |

In parallel with C4 rice there are other routes to raising carbon assimilation: introducing cyanobacterial carboxysomes and bicarbonate transporters into the chloroplasts of C3 crops (carboxysomes have been assembled in tobacco), engineering Rubisco, introducing photorespiratory bypasses, and accelerating the relaxation of nonphotochemical quenching ([7.13.7](/7.13.7#sec-7.5.2)). Their expected gains and theoretical upper limits are compared in [7.13.9](/7.13.9).

## Summary

| Topic | C3 plants (Definition 8.1.1) | C4 plants (Definition 8.3.1) | CAM plants (Definition 8.4.1) |
|---|---|---|---|
| The two carboxylations | Rubisco only | spatial separation: PEPC in mesophyll, Rubisco in sheath | temporal separation: PEPC at night, Rubisco by day |
| Key structure | ordinary mesophyll | Kranz anatomy (or single-cell C4) | succulent leaves, large vacuoles |
| $\ce{CO2}$ compensation point | 40–100 µmol mol⁻¹, Eq. (8.2) | 0–10 | 0–5 in the dark |
| Energy (per $\ce{CO2}$) | 3 ATP + 2 NADPH, increased by photorespiration according to Eq. (8.4) | $3 + 2/(1 - \varphi)$ ATP, Eq. (8.5) | about 6.5 ATP |
| Photorespiration | 15%–30% of carbon, increasing with rising temperature and falling $\ce{CO2}$ | 2%–3% | low |
| Water | transpiration ratio about 400 | about 150 | about 50 |
| $\delta^{13}\mathrm{C}$ / $\Delta$ | −28‰ / about 20‰, varying with $c_{\mathrm{i}}/c_{\mathrm{a}}$ | −14‰ / 3–5‰ | between the two |

| Topic | Key points |
|---|---|
| Carboxylation and oxygenation | $\phi = 2\Gamma^*/c_{\mathrm{c}}$; $\Gamma^*$ rises with temperature, Eq. (8.1); carbon lost $0.5\phi$ |
| Significance of photorespiration | necessary detoxification and carbon recovery; dissipates excess energy; linked to nitrogen metabolism; reduce oxygenation rather than remove the C2 pathway |
| Three decarboxylation subtypes (Definition 8.3.2) | NADP-ME (chloroplast, malate/pyruvate, maize), NAD-ME (mitochondrion, aspartate/alanine, proso millet, *Amaranthus*), PCK (cytosol, consumes ATP, guinea grass); PCK mostly a supplementary route |
| $\ce{CO2}$ concentration and leakage | $c_{\mathrm{bs}} - c_{\mathrm{m}} = \varphi V_{\mathrm{p}}/g_{\mathrm{bs}}$, Eq. (8.3); about 8–10 times atmospheric in the sheath; leakage 20%–30% |
| Light regulation of C4 enzymes | PEPC phosphorylation (by day), PPDK activated by regulatory protein through phosphorolysis, NADP-MDH activated by thioredoxin; PPDK cold-labile |
| Four phases of CAM | I night PEPC; II early morning both enzymes; III day stomata closed, decarboxylation; IV late afternoon direct Rubisco fixation; clock controls PEPC kinase |
| Carbon isotope discrimination (Definition 8.6.1) | $\Delta \approx \delta_{\mathrm{a}} - \delta_{\mathrm{p}}$, Eq. (8.7); C3: $\Delta = a + (b - a)c_{\mathrm{i}}/c_{\mathrm{a}}$, Eq. (8.8); C4: Eq. (8.9) |
| Δ and water-use efficiency | $A/E = c_{\mathrm{a}}(b - \Delta)/[1.6D(b - a)]$, Eq. (8.10); breeding for low Δ |
| Evolution of C4 | more than 60 independent origins; proto-Kranz → C2 photosynthesis → C4 cycle; C4 rice requires engineering biochemistry, anatomy and regulation together |

Main equations: $\Gamma^*(T)$, Eq. (8.1); $\Gamma = (\Gamma^* + KR_{\mathrm{d}}/V_{\mathrm{cmax}})/(1 - R_{\mathrm{d}}/V_{\mathrm{cmax}})$, Eq. (8.2); leakage $c_{\mathrm{bs}} - c_{\mathrm{m}} = \varphi V_{\mathrm{p}}/g_{\mathrm{bs}}$, Eq. (8.3); ATP consumption $(3 + 3.5\phi)/(1 - 0.5\phi)$ and $3 + 2/(1 - \varphi)$, Eqs. (8.4), (8.5); $\delta^{13}\mathrm{C}$ and $\Delta$, Eqs. (8.6)–(8.9); $A/E$, Eq. (8.10).

## Questions

1. At 30 °C a C3 plant leaf has $V_{\mathrm{cmax}} = 80$ and $R_{\mathrm{d}} = 1.5\,\mathrm{\mu mol\,m^{-2}\,s^{-1}}$, and at this temperature $K = 1100\,\mathrm{\mu mol\,mol^{-1}}$. Find $\Gamma^*$ from Eq. (8.1) and then the CO₂ compensation point from Eq. (8.2). Why is the CO₂ compensation point of the same plant close to zero in 2% $\ce{O2}$?

   **Answer** By Eq. (8.1), $\Gamma^*(30\,^\circ\mathrm{C}) = 42.75 \times \exp[37\,830 \times 5/(298.15 \times 8.314 \times 303.15)] = 42.75 \times \exp(0.2518) = 42.75 \times 1.286 = 55.0\,\mathrm{\mu mol\,mol^{-1}}$. By Eq. (8.2), $\Gamma = (55.0 + 1100 \times 1.5/80)/(1 - 1.5/80) = (55.0 + 20.6)/0.981 = 77\,\mathrm{\mu mol\,mol^{-1}}$. $\Gamma^*$ is proportional to $[\ce{O2}]/S_{\mathrm{c/o}}$, so lowering $\ce{O2}$ from 21% to 2% reduces $\Gamma^*$ to about one tenth (about 5); $K = K_{\mathrm{c}}(1 + O/K_{\mathrm{o}})$ also decreases, what remains is mainly the day respiration term, and the compensation point falls to about $10\,\mathrm{\mu mol\,mol^{-1}}$, close to C4 plants, showing that the high compensation point of C3 plants comes mainly from photorespiration.

2. Using Eqs. (8.4) and (8.5), calculate at $c_{\mathrm{c}} = 200\,\mathrm{\mu mol\,mol^{-1}}$ (stomata partly closed) how much ATP a C3 leaf needs per net $\ce{CO2}$ fixed to equal a C4 leaf with leakiness 0.25. What are the corresponding $\Gamma^*$ and temperature?

   **Answer** C4: $3 + 2/0.75 = 5.67$. Setting $(3 + 3.5\phi)/(1 - 0.5\phi) = 5.67$ gives $3 + 3.5\phi = 5.67 - 2.83\phi$, $\phi = 2.67/6.33 = 0.421$. $\Gamma^* = \phi c_{\mathrm{c}}/2 = 0.421 \times 200/2 = 42.1\,\mathrm{\mu mol\,mol^{-1}}$, which by Eq. (8.1) is about 25 °C. That is, when stomata are partly closed C4 is more economical than C3 above 25 °C; when stomata are open (higher $c_{\mathrm{c}}$) the crossover temperature is higher. This explains why C4 plants dominate in regions that are hot and seasonally dry.

3. The $\delta^{13}\mathrm{C}$ of a plant's dry matter is −26.0‰ and that of the atmosphere −8.5‰. Find $\Delta$ and the growth-period mean $c_{\mathrm{i}}/c_{\mathrm{a}}$. At $c_{\mathrm{a}} = 420\,\mathrm{\mu mol\,mol^{-1}}$ and $D = 0.015$, what is its intrinsic water-use efficiency $A/E$? How does it compare with a plant of the same species with $\delta^{13}\mathrm{C} = -29.0$‰?

   **Answer** By Eq. (8.7), $\Delta = (-8.5 + 26.0)/(1 - 0.026) = 17.97$‰. By Eq. (8.8), $c_{\mathrm{i}}/c_{\mathrm{a}} = (17.97 - 4.4)/22.6 = 0.60$. By Eq. (8.10), $A/E = 420\times10^{-6} \times 0.40/(1.6 \times 0.015) = 7.0\,\mathrm{mmol\,mol^{-1}}$. For $\delta^{13}\mathrm{C} = -29.0$‰, $\Delta = 20.5/0.971 = 21.1$‰, $c_{\mathrm{i}}/c_{\mathrm{a}} = 0.74$ and $A/E = 420\times10^{-6} \times 0.26/0.024 = 4.6\,\mathrm{mmol\,mol^{-1}}$. The former has a water-use efficiency about 50% higher, possibly because of more conservative stomata or greater photosynthetic capacity (both lower $c_{\mathrm{i}}$); $\Delta$ alone cannot distinguish the two causes. The value is that of a C3 plant (−26‰ lies within the C3 range), not C4 or CAM.

4. Someone says: "CAM plants close their stomata by day, so they do not photosynthesize by day." What is wrong with this statement? Using the data of Example 8.4.1, explain where the fixation rate of Rubisco in CAM plants by day comes from, and estimate how much $\ce{CO2}$ the leaf can fix at most in one night if the vacuole can hold only 60 mM malate.

   **Answer** What CAM plants close by day (phase III) is the stomata; the light reactions and the Calvin cycle proceed as usual, and the $\ce{CO2}$ fixed comes from decarboxylation of malate stored in the vacuole at night, not from outside; the photochemical part of "photosynthesis" can occur only by day, and what happens at night is only prefixation by PEPC. In Example 8.4.1, 0.216 mol m⁻² of malate is decarboxylated over about 8 h, supplying $\ce{CO2}$ at a mean rate of $7.5\,\mathrm{\mu mol\,m^{-2}\,s^{-1}}$ for fixation by Rubisco. If the vacuole can hold only 60 mM, at most $0.060 \times 1.8 = 0.108\,\mathrm{mol\,m^{-2}}$ can be stored, and the mean night uptake rate cannot exceed $0.108/43\,200 = 2.5\,\mathrm{\mu mol\,m^{-2}\,s^{-1}}$: the growth rate of CAM plants is limited by vacuolar storage capacity, one of the main reasons they grow slowly.

5. (Open question) Rice is a C3 plant and maize a C4 plant. List the traits that must be changed to convert rice into a C4 plant, and explain why transferring only the maize PEPC gene into rice does not raise photosynthesis.

   **Answer** The traits to be changed include: vein density and bundle sheath anatomy (each mesophyll cell next to a sheath cell, sheath cells rich in chloroplasts with walls of low conductance to $\ce{CO2}$); high expression of PEPC, carbonic anhydrase, NADP-MDH and PPDK in the mesophyll, expression of NADP-ME and the Calvin cycle in the sheath, and removal of Rubisco from the mesophyll; transporters for malate, pyruvate, PEP, 3-phosphoglycerate and triose phosphate between the two cell types; light regulation of the enzymes (PEPC kinase, PPDK regulatory protein); and the regulatory network that coordinates expression of these genes by cell type. When only PEPC is introduced, the C4 acid fixed in the mesophyll has no isolated, Rubisco-containing sheath cell to go to, and the $\ce{CO2}$ released by decarboxylation in the same cell only returns to where it started, cannot be concentrated near Rubisco, and instead forms a futile cycle that consumes ATP; moreover, accumulation of malate and so on may interfere with other metabolism. The benefit of C4 photosynthesis comes from spatial separation plus $\ce{CO2}$ concentration as a whole, which a single enzyme cannot replicate.
