---
title: Seed Dormancy, Germination and Seedling Establishment
description: "Seed viability and vigor and their assay, application of the longevity equation; primary and secondary dormancy, coat-imposed dormancy and embryo dormancy, the ABA/GA balance, DOG1, after-ripening and stratification; signals that break dormancy: light and phytochrome (red/far-red reversal, threshold model), low temperature, nitrate, karrikins in smoke; conditions for germination and the three phases of water uptake, respiration and enzyme activation; hydrotime and hydrothermal time models; mobilization of reserves: gibberellin-induced α-amylase in the aleurone layer, fats, proteins and phytate; vivipary and preharvest sprouting; seedling establishment: etiolation, the apical hook and ethylene; dormancy of buds and perennating organs."
source_hash: fae5c903a73a
---

The seed is the most durable stage in the life cycle of angiosperms: a dry seed has almost no measurable metabolism and can survive in the soil for years or even decades, and much longer in a seed bank. Germination, in contrast, is the riskiest and irreversible decision in the life cycle: once the radicle breaks through the seed coat, the seedling must establish the capacity for autotrophy before its reserves are exhausted. Seeds have therefore evolved elaborate mechanisms to "decide" when to germinate: dormancy postpones germination to a suitable season, while signals such as light, temperature, water, nitrate and smoke tell the seed where it is in the soil and what surrounds it. This chapter discusses these mechanisms from the physiological point of view: seed viability and longevity, the hormonal basis of dormancy, the signals that break dormancy, water uptake, metabolic resumption and mobilization of reserves during germination, and the regulation of growth as the seedling emerges.

The structure of seeds, the types of dormancy (Baskin's five classes), the Ellis–Roberts equation for seed longevity, the external conditions for germination and the types of seedling have been covered in botany ([7.12.19](/7.12.19)), and the development of the embryo and endosperm is in [7.12.30](/7.12.30); we do not repeat them here, but link to them and add the physiological and quantitative parts. The synthesis and signaling of hormones are in [7.13.14](/7.13.14) (gibberellin and the **aleurone layer**) and [7.13.15](/7.13.15) (abscisic acid, ethylene), the photochemistry of **phytochrome** and **photomorphogenesis** are in [7.13.16](/7.13.16), and the conversion of fat to sugar by the **glyoxylate cycle** is in [7.13.12](/7.13.12). The development and maturation of seeds (including the establishment of dormancy and desiccation tolerance) are in [7.13.23](/7.13.23).

## 20.1. Seed Viability, Vigor and Longevity

### 20.1.1. Viability and Vigor

The physiological definition of seed germination is the series of physiological and morphological changes that occur in a mature seed under suitable conditions, from the start of water uptake until the radicle breaks through the seed coat (**seed germination**, [7.12.19](/7.12.19#sec-19.5)); in production, germination is often considered complete when an independent seedling has formed. The physiological essence of germination is the completion of the transition from heterotrophy to autotrophy. Whether a seed can germinate depends first of all on whether it is alive and on how "well" it is alive.

**Definition 20.1.1 (Seed Viability and Seed Vigor)** Whether the embryo of a seed is alive and has the potential to germinate under suitable conditions is called **seed viability**, usually expressed as the percentage of viable seeds; the sum of the properties that determine the rapid, uniform germination of an acceptable seed lot and its growth into normal seedlings over a wide range of field conditions is called **seed vigor**.

Viability is a binary property of "dead or alive", whereas vigor is a matter of degree: two seed lots that both have 95 % germination behave identically under the favorable conditions of the laboratory, but in a cold, wet field one lot may emerge uniformly and the other sparsely. Seeds lose vigor first and viability later during aging, so vigor is a more sensitive indicator of seed quality.

Rapid tests of viability are as follows.

| Method | Principle | Judgment |
|---|---|---|
| Tetrazolium (TTC) test | Dehydrogenases of living cells reduce colorless 2,3,5-triphenyltetrazolium chloride to red, insoluble triphenylformazan; a solution of about 0.5 %–1 % is commonly used, in the dark and freshly prepared | Embryos stained red are viable; the location and depth of staining can be graded in detail |
| Red ink (dye exclusion) test | The plasma membrane of living cells is selectively permeable and does not take up the dye; dead cells are stained | Embryos not stained are alive and stained ones are dead (the opposite of TTC) |
| Bromothymol blue (BTB) test | Living seeds release $\ce{CO2}$ in respiration, turning the indicator from blue to yellow | A yellow halo around the seed means alive |
| Fluorescence-on-paper test | The plasma membrane of dead seeds is broken and fluorescent substances leak onto filter paper | A fluorescent halo means dead |
| Germination test | Actual germination under standard conditions | Most reliable but time-consuming (days to weeks) |

The TTC method was first used on seeds and was later also used to stain mammalian tissue to detect ischemic necrosis (such as brain infarcts). Vigor is commonly measured by accelerated aging (treatment for several days at about $41$–$45\,^\circ\mathrm{C}$ and near-saturated humidity before measuring germination), electrical conductivity (the conductivity of the soak water reflects membrane integrity, and low-vigor seeds leak more) and the cold test.

### 20.1.2. Longevity and Storage

The viability of orthodox seeds declines during storage as a cumulative normal distribution, the probit of survival decreases linearly with time, and the Ellis–Roberts equation (Eq. (19.1) of [7.12.19](/7.12.19#sec-19.4.2)) gives the quantitative effects of moisture content and temperature:

$$
v = K_i - \frac{p}{\sigma}, \qquad \log_{10}\sigma = K_E - C_W\log_{10}m - C_HT - C_QT^2.
$$

**Example 20.1.1 (Comparison of Storage Conditions)** Use the species constants determined for barley by Ellis and Roberts (1980), $K_E = 9.983$, $C_W = 5.896$, $C_H = 0.040$ and $C_Q = 0.000428$, to compare the time for a seed lot with initial viability 98 % ($K_i = \Phi^{-1}(0.98) = 2.05$) to fall to 85 % ($v = 1.04$) under two conditions.

(1) Moisture content 12 %, $20\,^\circ\mathrm{C}$: $\log_{10}\sigma = 9.983 - 5.896 \times 1.0792 - 0.80 - 0.171 = 2.649$, $\sigma = 446\,\mathrm{d}$; $p = (2.05 - 1.04) \times 446 = 450\,\mathrm{d}$, about 1.2 years. (2) Moisture content 8 %, $5\,^\circ\mathrm{C}$: $\log_{10}\sigma = 9.983 - 5.896 \times 0.9031 - 0.20 - 0.0107 = 4.448$, $\sigma = 2.8\times10^4\,\mathrm{d}$, $p \approx 2.8\times10^4\,\mathrm{d} \approx 78$ years. Lowering the moisture content by 4 percentage points and the temperature by $15\,^\circ\mathrm{C}$ lengthens longevity about 60-fold, of the same order of magnitude as Harrington's rule of thumb (longevity roughly doubles for each 1 % decrease in moisture content or each $5\,^\circ\mathrm{C}$ decrease in temperature: $2^4 \times 2^3 = 128$-fold).

:::

The causes of seed deterioration in storage include peroxidation of membrane lipids and membrane damage, oxidation and damage of proteins and nucleic acids, and consumption of reserves and inactivation of enzymes. In seeds dried to a moisture content of about 5 %–10 % the cytoplasm is in a glassy state in which molecular motion is extremely slow, which is the physical basis for the longer life at low moisture content; when the moisture content is too low (below about 3 %–5 %), lipid peroxidation actually speeds up, so there is an optimal range of low moisture content. DNA repair and mitochondrial repair in the early phase of imbibition (phase II of germination) can partly restore the vigor of aged seeds, which is the principle of priming: seeds are allowed to take up water under a controlled low water potential (for example in PEG solution) into phase II but are not allowed to protrude the radicle, and are then dried and sown, and they germinate faster and more uniformly (Section 20.5). Recalcitrant seeds do not tolerate drying and cannot be stored dry and cold ([7.12.19](/7.12.19#sec-19.4.2)).

## 20.2. The Physiology of Dormancy

### 20.2.1. Types of Dormancy

**Seed dormancy** is the state in which a viable seed fails to germinate although water, temperature and oxygen are all suitable ([7.12.19](/7.12.19#sec-19.4.1)), and it differs from "quiescence", in which a seed fails to germinate merely for lack of water: mature seeds at dispersal usually have a moisture content below $0.1\,\mathrm{g\,g^{-1}}$ dry weight, metabolism has stopped and they are quiescent; a quiescent seed germinates as soon as it takes up water, whereas a dormant seed needs additional treatment or signals. By the time at which dormancy arises, it is divided into the following types.

- Primary dormancy: induced by **abscisic acid** while the seed matures on the mother plant, so that the seed is already dormant at dispersal.
- Secondary dormancy: a seed whose dormancy has been broken re-enters dormancy after long imbibition under unfavorable conditions (high temperature, anoxia, darkness). Release of primary dormancy and induction of secondary dormancy alternate, so that seeds in the soil "cycle" between dormant and nondormant states with the seasons and germinate only in the suitable season (dormancy cycling).

By the site of dormancy, it is divided into dormancy imposed by the seed coat (and other covering tissues) and embryo dormancy.

| Type | Mechanism | Examples | Release |
|---|---|---|---|
| Coat-imposed: impermeable | Cuticle, suberin layer and lignified palisade sclereid layer | Legumes (clover, alfalfa), lotus (the ancient lotus seeds of [7.12.19](/7.12.19#sec-19.4.2)) | Mechanical or chemical scarification; animal digestive tract |
| Coat-imposed: mechanical resistance | The thick-walled endosperm is too hard for the radicle to emerge | *Arabidopsis*, tomato, coffee, tobacco | Enzymatic weakening of cell walls of the micropylar endosperm |
| Coat-imposed: restricted gas exchange | The permeability of the coat to $\ce{O2}$ is far lower than to water (about $10^4$-fold difference in charlock *Sinapis arvensis*); oxidation of phenolics in the coat consumes $\ce{O2}$ | Charlock, many grasses | High oxygen, removal of the coat |
| Coat-imposed: inhibitors | Phenolic acids, tannins and coumarins in the coat or pericarp prevent germination or prevent the escape of inhibitors from the embryo | Tomato and melons do not germinate inside the fruit; *Arabidopsis* *tt* (little proanthocyanidin in the coat) has weak dormancy and short longevity | Repeated leaching |
| Embryo: physiological | The hormone balance of the embryo itself (high ABA, low GA sensitivity) | Apple, hazelnut, European ash (removal of cotyledons releases) | Stratification, after-ripening, gibberellin |
| Embryo: morphological | The embryo is not fully developed | Celery, carrot (embryo small, growing 2–4 d in the endosperm after imbibition before emerging); orchids, broomrape (embryo undifferentiated) | Waiting for embryo growth |

### 20.2.2. The Balance of ABA and GA

For a long time **abscisic acid** was thought to inhibit germination and **gibberellin** to promote it; the hormone balance hypothesis holds that their ratio determines whether a seed is dormant or germinates (Taiz et al.). The "ratio" has two meanings: the amounts of the two hormones and the sensitivity of the tissue to them.

- Amount is determined by the balance of synthesis and inactivation: the rate-limiting step of ABA synthesis is 9-*cis*-epoxycarotenoid dioxygenase (NCED), and inactivation is mainly by ABA 8′-hydroxylase CYP707A2; the last step of GA synthesis, GA 3-oxidase (GA3ox; $\mathrm{GA_9} \to \mathrm{GA_4}$ in *Arabidopsis*, $\mathrm{GA_{20}} \to \mathrm{GA_1}$ in lettuce), is rate-limiting, and GA 2-oxidase (GA2ox) inactivates it.
- Sensitivity is determined by the signaling pathway: ABA signaling acts through PYR/PYL receptors, PP2C and SnRK2 kinases on the transcription factors ABI3, ABI4 and ABI5; GA through the receptor GID1 promotes the degradation of DELLA proteins (mainly RGL2 in germination) (signaling pathways in [7.1.15](/7.1.15#sec-15.5.2)). Early in seed development sensitivity to ABA is high and to GA low, and later the reverse, while the seed becomes more and more sensitive to environmental signals such as temperature and light.

Genetic evidence: seeds of the *Arabidopsis* ABA-deficient mutant (*aba*) have no dormancy, ABA-insensitive mutants *abi1* and *abi3* also have weak dormancy, and the same holds for ABA-deficient tomato mutants; maize *vp* (viviparous) mutants germinate on the ear, among which *vp2*, *vp5*, *vp7*, *vp9* and *vp14* are ABA-deficient (*vp14* encodes NCED) and *vp1* is ABA-insensitive (VP1 is a homolog of ABI3); vivipary of ABA-deficient types can be partly suppressed by exogenous ABA. The key experiment is that maize vivipary also requires GA synthesized early in embryo development as a positive signal, and a double mutant lacking both GA and ABA is not viviparous: what determines germination is therefore the ratio of ABA to GA, not the absolute amount of ABA (Taiz et al.). The two hormones also regulate each other: GA promotes germination through degradation of DELLA, and DELLA promotes expression of ABA synthesis genes and *ABI5*; ABA promotes accumulation of DELLA, forming mutually antagonistic positive feedback that lets the seed switch between the two stable states of "dormancy" and "germination", and environmental signals need only push this switch across the threshold (for the dynamics of the **toggle switch** see [7.6.33](/7.6.33#sec-33.3)). **Ethylene** and **brassinosteroid** weaken the inhibition of germination by ABA, and ABA in turn inhibits ethylene synthesis.

### 20.2.3. DOG1: A Quantitative Trait of Dormancy

Among natural variation in depth of seed dormancy in *Arabidopsis*, the quantitative trait locus with the largest effect is *DELAY OF GERMINATION 1* (*DOG1*, Bentsink et al. 2006). DOG1 protein accumulates during seed maturation, and the amount of DOG1 in the seed is positively correlated with dormancy depth; the lower the temperature experienced by the mother plant during seed maturation, the higher the *DOG1* expression and the deeper the seed dormancy, which "records" the maternal environment in the seed. DOG1 enhances ABA signaling by binding and inhibiting the PP2C-type phosphatases AHG1 and AHG3 (Née et al. 2017; Nishimura et al. 2018); it also affects GA synthesis. Homologs of *DOG1* also take part in the regulation of dormancy in wheat, rice and lettuce and are among the candidate genes for breeding resistance to preharvest sprouting in crops.

### 20.2.4. After-Ripening and Stratification

The term **after-ripening** does not mean exactly the same in Chinese and English literature. In the English literature and in textbooks such as Taiz et al., after-ripening refers to the natural release of dormancy after a period of dry storage at room temperature: barley needs only a few weeks and curly dock (*Rumex crispus*) 5 years; seeds of *Nicotiana plumbaginifolia* after 14 days of dry storage need about 10 days of moist conditions before germination begins, and after 10 months of dry storage only 3 days (Taiz et al.). During dry storage the ABA content of the seed declines (by about 40 % in *N. plumbaginifolia*), and sensitivity to ABA decreases and sensitivity to GA and environmental signals increases; when the moisture content is too low (about 5 %) the effect of after-ripening is weakened, possibly because after-ripening depends on slow nonenzymatic oxidation in the dry state (such as oxidation of specific mRNAs and proteins by reactive oxygen species). In nature, the seeds of winter annuals complete after-ripening in the hot, dry summer and germinate in autumn. Chinese textbooks often also call the requirement for several weeks to months in moist, cold conditions before germination after-ripening (Definition 19.4.1 of [7.12.19](/7.12.19#sec-19.4.1)), which in the English literature belongs to stratification below.

**Definition 20.2.1 (Stratification)** The treatment in which imbibed seeds are kept at moist, low temperature (generally $0$–$10\,^\circ\mathrm{C}$, commonly $1$–$5\,^\circ\mathrm{C}$) for weeks to months to release dormancy is called **stratification**; the name comes from the traditional practice of overwintering seeds in layers with moist sand or soil, and now moist seeds are usually kept in a refrigerator.

Stratification simulates overwintering of temperate plants: seeds do not germinate in autumn but germinate in spring after experiencing the low temperature of winter; stratification also synchronizes germination. Intact apple seeds need about 80 days of stratification at $5\,^\circ\mathrm{C}$ to reach maximal germination, isolated embryos only about 50 days, so the coat and endosperm raise the chilling requirement of the embryo by about 30 days (Visser 1956; Taiz et al.). During stratification expression of GA synthesis genes (*GA3ox1*) rises and ABA synthesis falls. The seeds of many woody plants such as Rosaceae, conifers, ginseng and dove tree (the stone needs 1–2 years of stratification) require stratification. Other methods of breaking dormancy in production include scarifying mechanically or treating the coat with concentrated sulfuric acid (hard seeds), sun-drying seeds, soaking in warm water, washing with water to remove inhibitors (tomato, cucumber), treatment with potassium nitrate or gibberellin, and physical treatments such as X-rays and ultrasound.

## 20.3. Environmental Signals That Break Dormancy

### 20.3.1. Light

Many small seeds need light to germinate (photoblasty). The need for light may be satisfied by a single brief exposure (lettuce cultivar Grand Rapids), by intermittent illumination (*Kalanchoe*) or by a specific photoperiod (birch seeds need long days and Canada hemlock short days).

**Definition 20.3.1 (Light-Requiring and Dark-Requiring Seeds)** Seeds that germinate well in light and do not germinate or germinate poorly in darkness are called **light-requiring seeds**; seeds that germinate well in darkness and whose germination is inhibited by light are called dark-requiring seeds.

Light-requiring seeds include lettuce, tobacco, *Arabidopsis*, carrot, mulberry and rhododendron; dark-requiring seeds include melons, onion, tomato (some cultivars), *Nigella*, cockscomb, amaranth and dodder; the seeds of most crops are insensitive to light (neutral seeds). Most light-requiring seeds are very small and have few reserves, and only by germinating near the soil surface can the seedling emerge; light is the signal by which they judge "I am at the soil surface", and far-red-rich light under a canopy tells them that competitors are above.

The photoreceptor for germination is **phytochrome** ([7.13.16](/7.13.16)). Borthwick, Hendricks and others (1952) found that lettuce seeds germinate in red light (about 660 nm) and do not germinate in far-red light (about 730 nm), and that when red and far-red light are given alternately, germination is determined by the last exposure (Figure 3A); this red/far-red reversibility was the basis for the discovery of phytochrome. What acts physiologically is the fraction of phytochrome in the Pfr form, $\varphi = \mathrm{Pfr}/\mathrm{Ptot}$: saturating red light brings $\varphi$ to a **photostationary state** of about 0.85, saturating far-red light lowers it to about 0.03, and light under a canopy (low R:FR) gives an intermediate value. Individual seeds in a population differ in their threshold for $\varphi$, and the germination fraction can be described by a normal distribution of thresholds: $G = \Phi[(\varphi - \mu)/s]$ (Figure 3B). Seeds with a high threshold germinate only at an open soil surface and are sensitive to shading; seeds with extremely low thresholds germinate under the very weak light in the soil, which is achieved by the very-low-fluence response mediated by phytochrome A (buried seeds can germinate after a momentary exposure during tillage, which is one reason why weeds emerge in large numbers after tillage). In *Arabidopsis* seeds phytochrome B is the main receptor: Pfr enters the nucleus and promotes degradation of the transcription factor PIF1 (PIL5), which normally represses *GA3ox* and induces *GA2ox* and ABA synthesis genes (Oh et al. 2004, 2007), so red light changes the ABA/GA ratio. The site of action of light is the endosperm: the dormancy of all light-requiring seeds is coat-imposed, and after removal of the endosperm the embryo can germinate even in darkness; light allows the radicle to penetrate the endosperm, in some species by enzymatic weakening of the cell walls of the micropylar endosperm.

Applying GA or cytokinin can replace light or red light in promoting germination of light-requiring seeds in darkness, and this effect cannot be reversed by far-red light (because it bypasses phytochrome).

![Control of germination of light-requiring seeds by phytochrome. A: Red (R) and far-red (FR) reversibility (after the experiments of Borthwick et al. 1952 on lettuce Grand Rapids, values illustrative): germination is very low in darkness; a brief red exposure promotes germination, a following far-red exposure cancels the effect of red, and when red and far-red are given alternately germination is determined by the last exposure. B: Germination as a function of the phytochrome photoequilibrium Pfr/Ptot, described by a normal distribution of thresholds in the seed population (G = Φ[(Pfr/Ptot − μ)/s], s = 0.08); the three curves represent populations with low, intermediate and high thresholds; vertical lines mark the photoequilibria after far-red (about 0.03), under a canopy (about 0.15) and after red (about 0.85)](./plots/photoblasty.py)

### 20.3.2. Temperature

Temperature has two different effects on dormancy: low-temperature stratification (Section 20.2.4) and high-temperature after-ripening release dormancy, whereas in nondormant seeds temperature determines the rate of germination (Section 20.5). Many seeds germinate better under alternating day–night temperatures than at constant temperature: a large diurnal temperature range implies that the seed is near the soil surface or in a gap without vegetation cover, which is a favorable signal for small-seeded pioneer plants. High temperature (for example above $30\,^\circ\mathrm{C}$) puts seeds of lettuce and others into thermodormancy or secondary dormancy, which is why lettuce sown in summer emerges poorly.

### 20.3.3. Nitrate and Nitric Oxide

Among the chemical signals present in the natural environment, nitrate (often acting together with light) is probably the most important. The seeds of some plants (such as hedge mustard *Sisymbrium officinale*) have an absolute requirement for nitrate and light to germinate. Nitrate is both a nutrient and a signal: through the transcription factor NLP8 it directly induces the ABA-inactivating gene *CYP707A2* and lowers ABA in the seed (Yan et al. 2016). Soil nitrate concentration rises after tillage, in gaps or after disturbance of vegetation, so, like light, it signals an environment with few competitors. Nitric oxide (NO) also breaks dormancy: *Arabidopsis* mutants that cannot synthesize NO have lower germination, and applied NO restores it (Taiz et al.).

### 20.3.4. Smoke and Karrikins

In fire-prone ecosystems in Australia, South Africa, California and elsewhere, the seeds of many plants germinate in large numbers after fire. The heat of the fire cracks hard seed coats; the more general signal is smoke. Flematti et al. (2004) isolated the main active compound from the smoke of burning cellulose; it was later named karrikinolide (KAR1) and belongs to a class of butenolide lactones called karrikins (a name proposed in 2009).

**Definition 20.3.2 (Karrikin)** A class of butenolide compounds that are produced from carbohydrates such as cellulose when plant material burns, are present in smoke and ash, and promote germination of the seeds of many plants at extremely low concentrations is called **karrikins**.

```smiles
CC1=C2C=COC=C2OC1=O KAR1
```

The most active KAR1 (3-methyl-2H-furo[2,3-c]pyran-2-one) is active at about $10^{-9}\,\mathrm{mol\,L^{-1}}$ and is also effective on many plants that never experience fire (including *Arabidopsis*). Karrikins resemble **strigolactone** in structure (both have a butenolide ring) and the perception pathways are also similar: the karrikin receptor KAI2 (KARRIKIN INSENSITIVE 2) is an α/β hydrolase paralogous to the strigolactone receptor D14, and both cooperate with the F-box protein MAX2 to degrade repressor proteins through the ubiquitin–proteasome pathway (SMAX1 and SMXL2 in the karrikin pathway; Nelson et al. 2011; Stanga et al. 2013). KAI2 is much older than D14 (present already in algae and bryophytes), and KAI2 mutants have phenotypes even in plants that never meet karrikins, so its natural ligand is thought to be an unidentified, plant-produced "KAI2 ligand", and karrikins are merely foreign molecules that happen to mimic it. Like nitrate and light, karrikins ultimately lower ABA synthesis or signaling and raise GA synthesis or signaling, that is, change the ABA/GA ratio (Taiz et al.).

![Integration of signals in seed dormancy and germination (SBGN activity flow diagram, simplified; arrows indicate promotion, bars indicate inhibition, dashed lines indirect actions). Red light through phytochrome B (Pfr) causes degradation of the transcription factor PIF1/PIL5, which normally represses GA synthesis (GA3ox) and promotes GA inactivation (GA2ox) and ABA synthesis (NCED); cold stratification promotes GA3ox; nitrate induces the ABA-inactivating enzyme CYP707A2; karrikins in smoke cause degradation of the repressor SMAX1 through KAI2–MAX2; dry storage (after-ripening) reduces the action of DOG1. ABA maintains dormancy and inhibits germination through ABI3/ABI5; GA degrades DELLA (RGL2) and releases its inhibition of germination; DOG1 enhances ABA signaling; ABA and DELLA promote each other, forming a switch between two stable states](./plots/dormancy-network.py)

## 20.4. Conditions and Process of Germination

### 20.4.1. Conditions for Germination

Germination requires suitable water, temperature and oxygen, and sometimes also light and nitrate (the external conditions of germination and the cardinal temperatures of various crops are in [7.12.19](/7.12.19#sec-19.5.1)). Of these, water is the most critical: the moisture content of air-dry seeds is 5 %–15 %, far below the level needed for active metabolism, and water uptake also supplies the turgor needed for cell expansion. The minimum water uptake required for germination (as a percentage of air-dry weight) differs with the reserves: protein-rich seeds take up the most water, starch seeds less, and oil seeds still less (values differ somewhat among sources).

| Crop | Water uptake / % | Crop | Water uptake / % |
|---|---|---|---|
| Rice | 35 | Cotton | 60 |
| Wheat | 60 | Pea | 186 |
| Maize | 40 | Soybean | 120 |
| Rapeseed | 48 | Broad bean | 157 |

Oxygen: normal germination of seeds generally requires an $\ce{O2}$ content of the air above 10 %, and seeds rich in fat (cotton, peanut) need more oxygen than starch seeds (wheat, rice) because oxidation of fat consumes more $\ce{O2}$ (low **respiratory quotient**, [7.13.12](/7.13.12)). Rice can germinate under flooding and anoxia, but only the coleoptile elongates and the radicle hardly grows: elongation of the coleoptile involves only cell expansion and no cell division, and the energy supplied by anaerobic respiration is sufficient; growth of the radicle and plumule needs cell division and must have aerobic respiration. Under anoxia the rice coleoptile can still elongate because anoxia-induced α-amylase (through the CIPK15–SnRK1A–MYBS1 signal, Lee et al. 2009) breaks down starch to sustain fermentation. Attention to drainage and oxygen supply is therefore needed in raising rice seedlings.

### 20.4.2. The Three Phases of Water Uptake

Water uptake by seeds has three phases, "fast–slow–fast" (Figure 1A; Taiz et al.).

1. Phase I (imbibition): the dry seed takes up water rapidly. The driving force is the **matric potential**: the micro-capillaries of cell walls and the surfaces of macromolecules such as proteins and starch bind water strongly, so that the water potential of a dry seed is as low as tens to hundreds of megapascals (**imbibition**, [7.13.2](/7.13.2)). Dead seeds also imbibe, so phase I is a physical process. Rehydration of macromolecules activates basic metabolism: respiration, transcription and translation. After all binding sites are saturated with water the matric potential no longer falls and water uptake slows.
2. Phase II (plateau): there is little water uptake, and this is the preparatory phase before growth. Breakdown of reserves in the embryo begins, osmotically active solutes increase, and the **solute potential** gradually falls; the cytoskeleton is rebuilt, DNA repair and repair and proliferation of mitochondria begin, stored mRNAs are translated or degraded, and new mRNAs begin to be transcribed. The seed may swell and rupture the coat. Penetration of the seed coat by the radicle marks completion of germination; it may be a one-step process (the radicle emerges as soon as the coat is broken) or a two-step process (the coat is ruptured first and the radicle emerges only after the micropylar endosperm is weakened).
3. Phase III (growth): after the radicle protrudes, wall loosening and cell expansion lower the water potential (the Lockhart mechanism of [7.13.17](/7.13.17#sec-17.3)), water uptake rises rapidly again and reserves are mobilized in large amounts. This phase already belongs to seedling growth after germination.

Chinese textbooks often write the water potential of the three phases as $\Psi_{\mathrm{w}} \approx \Psi_{\mathrm{m}}$ in phase I (imbibitional water uptake) and $\Psi_{\mathrm{w}} = \Psi_{\mathrm{s}} + \Psi_{\mathrm{p}}$ in phase III (osmotic water uptake), which summarizes the change in driving force. Rapid imbibition is injurious to dry seeds: the membranes of dry seeds are in a gel state, and rapid water uptake (especially at low temperature) ruptures the membranes before they recover the liquid-crystalline state, so that large amounts of solutes leak out; large-seeded legumes such as soybean and bean are most sensitive (imbibitional chilling injury), and slow rehydration in air of higher humidity before sowing can alleviate it.

### 20.4.3. Respiration and Enzyme Activation

The change in respiration rate resembles that of water uptake (Figure 1B). In phase I the hydrated mitochondria resume activity and respiration rises sharply; in phase II respiration stalls, the seed coat restricts the entry of $\ce{O2}$, some anaerobic respiration occurs and the respiratory quotient is often greater than 1; in phase III the radicle penetrates the coat, the $\ce{O2}$ supply increases, new mitochondria and respiratory enzyme systems form in the embryo, and respiration again rises sharply; afterward, if the seedling stays in darkness, reserves are exhausted and respiration declines. The statement that the respiratory quotient is greater than 1 in phase I and less than 1 in phase II has the two phases reversed: fermentation ($\mathrm{RQ} > 1$) occurs in phase II, when oxygen supply is limited.

Enzymes in germination have two sources.

- Activation of existing enzymes: present in dry seeds in a bound or inactive form and released or activated after water uptake, such as β-amylase (bound to protein and released by protease cleavage), R-enzyme (debranching enzyme) and phosphatases.
- Newly synthesized enzymes: synthesized de novo under the control of nucleic acids, such as α-amylase, lipase, proteases and nitrate reductase; inhibitors of transcription and translation can block their appearance.

![Three phases of water uptake and respiration in seed germination (phenomenological model, illustrative parameters). A: Water content (water per gram dry weight). Phase I is imbibition driven by matric potential, and the water content approaches a plateau exponentially; in phase II there is little water uptake, metabolism resumes, DNA and mitochondrial repair occur and breakdown of reserves begins; the radicle breaks through the coat at about 30 h (vertical dashed line), completing germination; in phase III cell expansion drives a second rapid increase in water uptake. Dead seeds (dashed) also imbibe but do not enter phase III. B: Respiration ($\ce{O2}$ uptake, relative values): in phase I hydrated mitochondria resume respiration, in phase II it stalls (the coat restricts oxygen supply), and after the radicle emerges new mitochondria form and oxygen supply improves, so respiration rises rapidly a second time](./plots/imbibition.py)

## 20.5. Quantitative Models of Germination: Hydrotime and Hydrothermal Time

The times at which individual seeds in a lot germinate differ, and the germination curve (cumulative germination against time) is S-shaped. The less water and the lower the temperature, the slower and less uniform the germination and the lower the final germination (for tomato seeds shown by Taiz et al., all seeds germinate at an external water potential of 0 MPa and almost none at $-1.0\,\mathrm{MPa}$). Gummerson (1986) and Bradford (1990) proposed a concise population model.

**Definition 20.5.1 (Hydrotime Model)** Let each seed $g$ have a base water potential $\Psi_{\mathrm{b}}(g)$ (this seed does not germinate when the external water potential is below it); the time $t_g$ it needs to germinate at water potential $\Psi$ satisfies

$$
\theta_{\mathrm{H}} = \left[\Psi - \Psi_{\mathrm{b}}(g)\right]t_g,
\tag{20.1}
$$
that is, the product of "water potential above the threshold × time" is a constant $\theta_{\mathrm{H}}$ (hydrotime, in $\mathrm{MPa\,h}$); $\Psi_{\mathrm{b}}$ is normally distributed in the seed population, with mean $\Psi_{\mathrm{b}}(50)$ and standard deviation $\sigma_{\Psi_{\mathrm{b}}}$. This model is called the **hydrotime model**.

The seeds that have germinated by time $t$ are those with $\Psi_{\mathrm{b}}(g) \le \Psi - \theta_{\mathrm{H}}/t$, so the cumulative germination fraction is

$$
G(t, \Psi) = \Phi\!\left(\frac{\Psi - \theta_{\mathrm{H}}/t - \Psi_{\mathrm{b}}(50)}{\sigma_{\Psi_{\mathrm{b}}}}\right),
\tag{20.2}
$$

where $\Phi$ is the standard normal distribution function. With only three parameters, Eq. (20.2) describes all germination curves at all water potentials: when the probit $\Phi^{-1}(G)$ is plotted against $\Psi - \theta_{\mathrm{H}}/t$, data at different water potentials fall on a single straight line with slope $1/\sigma_{\Psi_{\mathrm{b}}}$ (Figure 2B); this is exactly the idea of the **probit model** ([7.7.14](/7.7.14)), which has the same origin as the seed longevity equation.

The physiological meaning of the parameters: $\theta_{\mathrm{H}}$ determines how fast germination is, $\Psi_{\mathrm{b}}(50)$ measures the tolerance of the seed to water deficit and its degree of dormancy, and $\sigma_{\Psi_{\mathrm{b}}}$ measures the uniformity of germination. Dormancy and its release can be understood as a shift of the distribution of $\Psi_{\mathrm{b}}$ (Bradford 2002): ABA raises $\Psi_{\mathrm{b}}(50)$ (less negative, so the seed needs more water to germinate), and GA, after-ripening, stratification, light and priming lower it; when $\Psi_{\mathrm{b}}(50)$ is above 0, most seeds do not germinate even in pure water, which is dormancy.

In the suboptimal temperature range the effect of temperature is the same as that of thermal time (**thermal time**, [7.13.17](/7.13.17#sec-17.7)): $\theta_{\mathrm{T}} = (T - T_{\mathrm{b}})t_g$. Combining the two gives the hydrothermal time model (Gummerson 1986; Bradford 1995):

$$
\theta_{\mathrm{HT}} = \left[\Psi - \Psi_{\mathrm{b}}(g)\right](T - T_{\mathrm{b}})\,t_g,
\tag{20.3}
$$

in $\mathrm{MPa\,^\circ C\,h}$, which describes the effects of water and temperature on germination simultaneously between $T_{\mathrm{b}}$ and the optimum temperature and is used to predict field emergence time and weed emergence.

**Example 20.5.1 (Hydrotime)** A lot of tomato seeds has parameters $\theta_{\mathrm{H}} = 30\,\mathrm{MPa\,h}$, $\Psi_{\mathrm{b}}(50) = -0.70\,\mathrm{MPa}$ and $\sigma_{\Psi_{\mathrm{b}}} = 0.20\,\mathrm{MPa}$. (1) In pure water ($\Psi = 0$), the time for half the seeds to germinate is $t_{50} = \theta_{\mathrm{H}}/[0 - (-0.70)] = 43\,\mathrm{h}$; at $\Psi = -0.4\,\mathrm{MPa}$, $t_{50} = 30/0.30 = 100\,\mathrm{h}$. (2) What is the maximum fraction of seeds that can germinate at $\Psi = -0.4\,\mathrm{MPa}$? As $t \to \infty$, $G = \Phi[(-0.4 + 0.70)/0.20] = \Phi(1.5) = 93\,\%$; at 120 h, $G = \Phi[(-0.4 - 0.25 + 0.70)/0.20] = \Phi(0.25) = 60\,\%$. (3) If priming lowers $\Psi_{\mathrm{b}}(50)$ to $-0.90\,\mathrm{MPa}$ ($\theta_{\mathrm{H}}$ unchanged), $t_{50}$ in pure water is shortened to $30/0.90 = 33\,\mathrm{h}$ and at $-0.4\,\mathrm{MPa}$ to $60\,\mathrm{h}$.

![The hydrotime model of germination (Eqs. (20.1), (20.2); parameters of the order of magnitude of tomato seeds: θ_H = 30 MPa h, Ψ_b(50) = −0.70 MPa, σ = 0.20 MPa, illustrative). A: Cumulative germination curves at different external water potentials (curves are the model, points are simulated counts of 100 seeds): the lower the water potential, the later and less uniform the onset of germination and the lower the final germination. B: Data at all water potentials plotted as probit(G) against Ψ − θ_H/t all fall on a single straight line (dashed), whose slope is 1/σ and whose intercept gives Ψ_b(50)](./plots/hydrotime.py)

## 20.6. Mobilization of Reserves

The reserves of angiosperm seeds are stored in the endosperm or cotyledons: starch in amyloplasts, protein in protein storage vacuoles (protein bodies) and lipids in oil bodies. After germination the large-scale mobilization of reserves supplies the seedling with nutrients until it can be autotrophic; this process includes three steps: hydrolysis in the storage tissue, transport in soluble form to the embryo, and resynthesis at the growth sites.

### 20.6.1. Starch: The Aleurone Layer of Cereals

A cereal grain consists of the embryo, the endosperm and the fused seed coat–pericarp. The triploid endosperm is divided into the central starchy endosperm (cells dead and filled with starch grains) and the **aleurone layer** surrounding it, which consists of one to several layers of living cells; the embryo has a specialized absorptive organ, the scutellum ([7.12.19](/7.12.19)). During germination aleurone cells synthesize and secrete hydrolytic enzymes into the starchy endosperm, and the sugars and amino acids released are absorbed through the scutellum and transported to the growing embryo (Figure 4A).

Experiments in the 1960s established the hormonal control of this system: secretion of starch-hydrolyzing enzymes by barley aleurone requires the presence of the embryo; $\mathrm{GA_3}$ can replace the embryo (Yomo 1960; Paleg 1960); the embryo synthesizes GA during germination and releases it into the endosperm (the natural active GA in cereals is $\mathrm{GA_1}$). Deembryonated "half-seeds" or isolated aleurone layers contain only one type of cell that responds to GA and are classic materials for studying GA signaling; the brewing industry adds GA in malting barley to speed up amylase production. The molecular mechanism (Taiz et al., Figure 4B) is as follows.

1. GA binds the soluble receptor GID1, and after its conformational change GID1 binds DELLA proteins (SLN1 in barley); DELLA is ubiquitinated by the SCF-type ubiquitin ligase (SLY1/GID2) and degraded by the 26S proteasome; the aleurone layer of the rice *gid1* mutant cannot synthesize α-amylase.
2. After DELLA degradation, the early response gene *GA-MYB* begins to be expressed within about 1 h; induction of GA-MYB does not require protein synthesis (cycloheximide does not inhibit it) and it is a primary response gene.
3. GA-MYB protein binds the conserved GA response element (GARE, TAACAAA) in the promoter of α-amylase genes and activates transcription; α-amylase mRNA rises about 3 h later than GA-MYB mRNA (Gubler et al. 1995) and is a secondary response gene; mutation of the GARE prevents MYB from binding and α-amylase is not expressed; constitutive expression of GA-MYB in the absence of GA can also induce α-amylase.
4. α-Amylase is synthesized on the rough endoplasmic reticulum and packaged and secreted through the Golgi apparatus; secretion requires a GA-activated $\ce{Ca^2+}$–calmodulin-dependent pathway.
5. ABA inhibits GA-induced α-amylase: VP1 acts as a transcriptional repressor of some GA-induced genes, and ABA also inhibits expression of *GA-MYB*. ABA thus both maintains dormancy and prevents mobilization of reserves before dormancy is released.

Starch is degraded by hydrolytic and phosphorolytic pathways (enzyme actions in [7.13.12](/7.13.12#sec-12.2.1)).

| Pathway | Enzymes | Product |
|---|---|---|
| Hydrolysis | α-Amylase (endo-α-1,4 cleavage, can act on intact starch grains), β-amylase (exo-acting from the nonreducing end, producing maltose), R-enzyme (debranching enzyme, hydrolyzing α-1,6 bonds), maltase | Glucose |
| Phosphorolysis | Starch phosphorylase ($\mathrm{G}_n + \mathrm{P_i} \to \mathrm{G}_{n-1} + $ glucose-1-phosphate) | Glucose-1-phosphate |

Sugars are synthesized into sucrose (the transport form) in the scutellum and transported to the embryonic axis and plumule, where they serve as respiratory substrates or for synthesis of new structural materials.

![Mobilization of starch in a cereal grain (schematic). A: Germinating grain: gibberellin (GA) synthesized by the embryo diffuses through the scutellum to the aleurone layer (purple, living cells); aleurone cells synthesize and secrete hydrolytic enzymes such as α-amylase into the starchy endosperm (green, dead cells, dots are starch grains), and the sugars produced by breakdown are absorbed through the scutellum and transported to the embryo. B: One aleurone cell: GA₁ binds the receptor GID1, the GA–GID1–DELLA complex is ubiquitinated by SCF(SLY1), and DELLA is degraded by the 26S proteasome; the GA-MYB gene is expressed within about 1 h, GA-MYB protein binds the GARE element in the α-amylase gene promoter, and α-amylase mRNA rises after about 3 h; α-amylase is synthesized on the rough endoplasmic reticulum and secreted to the outside through the Golgi apparatus and secretory vesicles, and secretion requires Ca²⁺–calmodulin; ABA inhibits expression of GA-MYB](./plots/aleurone.py)

### 20.6.2. Fats, Proteins and Phytate

Mobilization of fat: triacylglycerols in oilseeds (rapeseed, cotton, peanut, sunflower, castor bean) are stored in oil bodies, whose surface has oil body proteins (oleosins). In germination lipase hydrolyzes triacylglycerol to glycerol and fatty acids; fatty acids enter glyoxysomes (specialized peroxisomes) and undergo β-oxidation to acetyl-CoA, which is converted by the glyoxylate cycle to succinate; succinate is transported to mitochondria and converted to malate by part of the TCA cycle, malate is oxidized in the cytosol to oxaloacetate, PEP carboxykinase produces PEP, gluconeogenesis forms hexose, and finally sucrose is synthesized and transported to the embryonic axis (details of the pathway and the respiratory quotient in [7.13.12](/7.13.12#sec-12.5)); glycerol is phosphorylated and oxidized to dihydroxyacetone phosphate and enters gluconeogenesis. By the stoichiometry of conversion of palmitic acid to hexose in [7.13.12](/7.13.12), $\ce{C16H32O2 + 11O2 -> 2C6H12O6 + 4CO2 + 4H2O}$, $256\,\mathrm{g}$ of palmitic acid yields at most $360\,\mathrm{g}$ of glucose, about $1.4\,\mathrm{g}$ of sugar per gram of fatty acid: fat is a more compact form of carbon storage than starch.

Mobilization of protein: storage proteins in protein storage vacuoles (prolamins and glutelins of cereals, globulins of legumes) are hydrolyzed by proteases to small peptides, and peptidases hydrolyze the small peptides completely to amino acids. The fates of the amino acids are: resynthesis of proteins; formation of new amino acids by transamination; oxidative deamination to produce ammonia and keto acids, with ammonia stored and transported as amides such as asparagine and glutamine to avoid ammonia toxicity.

Mobilization of phytate: phosphorus in mature seeds is stored mainly as phytate (inositol hexakisphosphate), often 60 %–80 % of total seed phosphorus; phytate binds $\ce{K+}$, $\ce{Mg^2+}$, $\ce{Ca^2+}$ and others as phytin salts stored in globoids in protein storage vacuoles, so it is also a storage form of several mineral elements. In germination phytase hydrolyzes phytate to inositol and phosphate; phosphate takes part in energy metabolism and nucleic acid synthesis, and inositol can be used for synthesis of cell wall materials. Phytate strongly chelates iron and zinc and lowers the bioavailability of these elements in cereals and legumes for humans and monogastric animals (pigs, chickens); unused phytate phosphorus is excreted in feces and causes phosphorus pollution, so phytase is often added to feed and low-phytate crop cultivars are bred.

## 20.7. Vivipary and Preharvest Sprouting

Seeds without dormancy or with very shallow dormancy germinate on the mother plant. Germination of seeds on the mother plant before they are mature, as a normal part of development of the species, is called vivipary (**vivipary**, [7.12.32](/7.12.32)), seen in estuarine and intertidal plants such as mangroves: the seed of the red mangrove (*Rhizophora mangle*) germinates inside the fruit, the hypocotyl grows into a dart-shaped propagule, and after falling it is planted in the mud and takes root. In crops such as cereals it is a harmful trait.

**Definition 20.7.1 (Preharvest Sprouting)** The phenomenon in which physiologically mature seeds with shallow dormancy encounter rainy weather before harvest and germinate on the mother plant (the ear) is called **preharvest sprouting**, also called sprouting in the ear.

Wheat, barley, rice and sorghum are most prone to preharvest sprouting when they meet prolonged rain at maturity. After germination starts, the aleurone layer secretes α-amylase, starch in the endosperm is broken down, and the processing quality of the grain (the baking performance of flour) falls seriously, even before the radicle is seen to emerge; the flour industry uses the "falling number" to measure amylase activity and thereby the degree of preharvest sprouting. The situation in mutants was discussed in Section 20.2.2: vivipary (germination on the ear) of maize *vp* mutants results from defects in ABA synthesis or signaling. Resistance to preharvest sprouting in wheat is related to grain color: red-grained cultivars generally have deeper dormancy than white-grained ones, the red color is determined by flavonoids (proanthocyanidins) in the seed coat, and the *R* gene that controls it encodes a MYB transcription factor; in addition, dormancy genes such as *TaPHS1* (*TaMFT*), *TaSdr* and rice *Sdr4* have been cloned. Measures to prevent preharvest sprouting are breeding cultivars with moderate dormancy (neither sprouting in the ear nor emerging unevenly after sowing), harvesting promptly, and spraying plant growth retardants (such as paclobutrazol and daminozide, agents that inhibit GA synthesis) at maturity to delay germination; similar methods can be used to prevent early germination of peanut in the soil.

## 20.8. Seedling Establishment

### 20.8.1. From Germination to Autotrophy

Seedling establishment is the stage from radicle emergence until the seedling no longer depends on the seed reserves and can live independently. Its definition varies with the discipline: physiologically it means from radicle emergence until reserves are exhausted, agronomically the appearance of the first true leaf, ecologically the time when the environment begins to exert selection on seedling survival, and in developmental biology the time when the seedling can sustain its own growth (Taiz et al.). Seedlings at this stage are most sensitive to biotic and abiotic adversity: in the field about 10 %–55 % of maize seedlings and 48 %–70 % of soybean seedlings die at this stage (Taiz et al.). The larger the seed and the more the reserves, the better seedling establishment is assured, which is the physiological basis of the trade-off between seed size and number. The relation of seedling emergence types (epigeal and hypogeal cotyledons) to sowing depth is in [7.12.19](/7.12.19#sec-19.6).

### 20.8.2. Seedlings in Darkness

Seedlings germinating in the soil are in darkness and grow according to the program of **skotomorphogenesis** (etiolation): in dicots the hypocotyl is long and thin with its tip bent into a hook, the cotyledons are closed, and plastids remain at the etioplast stage; in grasses the coleoptile and mesocotyl elongate and the leaves do not expand. This form lets the seedling use its limited reserves for rapid elongation through the soil while protecting the fragile shoot apex. As soon as the seedling sees light it switches to **photomorphogenesis**: elongation slows, the hook opens, and the cotyledons expand and turn green ([7.13.16](/7.13.16)). In darkness there is little Pfr, the hypocotyl is highly sensitive to GA, and GA strongly promotes hypocotyl elongation; after exposure to light Pfr lowers the sensitivity of the hypocotyl to GA. GA-deficient pea mutants therefore show the "de-etiolated" form even in darkness (only chlorophyll does not form); **brassinosteroid** acts similarly, and the BR-deficient *Arabidopsis* mutant *det2* has a short, thick hypocotyl and open cotyledons in darkness (Taiz et al.). The signals of GA (through DELLA), BR and phytochrome all converge on PIF transcription factors.

### 20.8.3. The Apical Hook and Ethylene

Formation and maintenance of the apical hook is asymmetric growth caused by **ethylene**: the outer side of the hook elongates faster than the inner side. The dynamics of the hook has three phases: formation, maintenance and opening. Auxin is also required: the auxin-insensitive mutant *axr1* does not form a hook, the auxin transport inhibitor NPA prevents hook formation, and the auxin concentration is higher on the inner side of the hook (inhibiting inner-side elongation); this lateral auxin gradient is induced by ethylene and resembles the auxin redistribution in tropic movements; *HOOKLESS1* (*HLS1*) is a gene required for ethylene to induce the hook (Lehman et al. 1996). The hook opens on exposure to light: red light opens the hook and far-red light reverses the effect of red, showing that the receptor is phytochrome; red light inhibits ethylene synthesis in the hook tissue, inner-side elongation speeds up, the growth rates of the two sides become equal, and the hook straightens (Taiz et al.).

Ethylene also explains how seedlings "feel" soil resistance: when emergence is obstructed the seedling synthesizes more ethylene, which appears as the **triple response**, with hypocotyl elongation inhibited, lateral thickening and a deeper hook ([7.13.15](/7.13.15)). At ethylene concentrations above about $0.1\,\mu\mathrm{L\,L^{-1}}$, the cortical microtubules of hypocotyl cells turn from transverse to longitudinal, the newly deposited microfibrils turn with them, and the cells expand laterally ([7.13.17](/7.13.17#sec-17.2.3)); a short, thick hypocotyl is better able to push through the soil. Inhibition of hypocotyl elongation by ethylene has two phases: the first occurs rapidly within about 15 min of adding ethylene and the second is slower and sustained; the ethylene signaling mutant *ein3/eil1* lacks only the second phase (Binder et al. 2004; Taiz et al.). EIN3, the key transcription factor of ethylene signaling, together with PIF3 in light signaling integrates information on soil pressure and illumination: when the seedling nears the soil surface and sees light, the ethylene response is suppressed and the hook opens (Zhong et al. 2014).

## 20.9. Dormancy of Buds and Perennating Organs

Seeds are not the only organs that go dormant. Buds of perennial plants and perennating organs such as tubers, bulbs and corms are also dormant, to survive the unfavorable season.

Bud dormancy is divided by the source of control into three classes (Lang et al. 1987).

| Type | Source of control | Example |
|---|---|---|
| Paradormancy | Organs other than the bud | Axillary buds under apical dominance ([7.13.18](/7.13.18#sec-18.6)) |
| Endodormancy | The bud itself; a certain amount of cold (the chilling requirement) is needed to release it | Winter buds formed in autumn by temperate deciduous trees |
| Ecodormancy | Unfavorable environment (cold, drought) | Buds in early spring after endodormancy has been released but while temperatures are still low |

Winter buds of temperate deciduous trees form in autumn under short days and are enclosed by bud scales; short days and low temperature induce endodormancy, in which the flowering genes *FT*, *CO* and *TFL1*, phytochrome A and the biological clock take part; in poplar, for example, short days lower *FT* expression and the cell cycle in the bud stops (Taiz et al.). Release of endodormancy requires accumulation of enough cold. The chilling requirement of fruit trees is commonly calculated in "chill hours", the accumulated number of hours between $0$ and $7.2\,^\circ\mathrm{C}$; the more precise Utah model assigns different weights to each hour according to temperature (about $2.5$–$9\,^\circ\mathrm{C}$ is most effective, and high temperature has a negative effect). The chilling requirements of different cultivars of apple and peach range from several hundred to more than a thousand chill hours: when the chilling requirement is not met, bud break and flowering in spring are uneven and fruit set is poor, which is the main limitation of warm winters and of introducing temperate fruit trees to the subtropics; chemicals such as hydrogen cyanamide can partly replace chilling. After dormancy is released, buds break according to thermal time (heat time under ecodormancy).

Potato tubers have a dormancy period after harvest; dormancy is maintained by ABA and released by increases in cytokinin and GA. In production, dormancy is broken (for seed tubers used in two crops a year or autumn sowing) by soaking cut pieces for about 10 min in $0.5$–$1\,\mathrm{mg\,L^{-1}}$ GA solution or for 8–12 h in thiourea solution; dormancy is prolonged and sprouting in storage prevented by treatment with a 0.4 % methyl naphthaleneacetate powder, a method also used for onion and garlic. Storage at low temperature ($3$–$5\,^\circ\mathrm{C}$ for potato) also inhibits sprouting but converts starch in the tubers to reducing sugars and affects the quality for frying (storage in [7.13.12](/7.13.12)).

## Summary

| Topic | Content | Key points |
|---|---|---|
| Viability and vigor (Definition 20.1.1) | TTC, red ink, BTB, fluorescence; accelerated aging, conductivity | Vigor is lost first, viability later |
| Longevity | Ellis–Roberts equation ([7.12.19](/7.12.19)) | Moisture content and temperature act multiplicatively; glassy state; priming |
| Types of dormancy | Primary, secondary, dormancy cycling; coat-imposed (impermeable, mechanical, gas, inhibitors) and embryo (physiological, morphological) | Quiescence ≠ dormancy |
| Hormones | ABA/GA ratio (amount × sensitivity); NCED, CYP707A2, GA3ox, GA2ox; ABI3/5, DELLA (RGL2) | Maize *vp* and double mutant; mutually antagonistic switch |
| DOG1 | Major QTL of dormancy; enhanced by maternal cold | Inhibits PP2C (AHG1), enhances ABA signaling |
| Release of dormancy | After-ripening (dry storage, the English sense); stratification (Definition 20.2.1) | Apple: seeds 80 d, isolated embryos 50 d |
| Light (Definition 20.3.1) | Phytochrome; R/FR reversibility; Pfr/Ptot threshold; phyB–PIF1 → GA/ABA | Light-requiring seeds are small; coat-imposed; GA can replace light |
| Other signals | Alternating temperature, nitrate (NLP8 → CYP707A2), NO, karrikins (Definition 20.3.2; KAI2–MAX2–SMAX1) | All change the ABA/GA ratio |
| Water uptake | Phase I imbibition (matric potential, dead seeds also imbibe), II plateau (metabolism and repair), III growth | Radicle emergence = completion of germination; imbibitional chilling injury |
| Respiration | Fast–slow–fast; fermentation in phase II (RQ > 1) | Enzymes: activated (β-amylase) and newly synthesized (α-amylase) |
| Quantitative | Hydrotime (Definition 20.5.1) and hydrothermal time | Three parameters describe all germination curves |
| Mobilization | Aleurone layer: GA–GID1–DELLA → GA-MYB → GARE → α-amylase; ABA inhibits | Fat becomes sugar through the glyoxylate cycle; phytate is 60 %–80 % of seed phosphorus |
| Preharvest sprouting (Definition 20.7.1) | Shallow dormancy; red grain more resistant | Vivipary (mangrove) is a normal trait |
| Seedling establishment | Etiolation: GA, BR inhibit photomorphogenesis; hook: ethylene + auxin, opened by red light | Soil resistance → ethylene → triple response |
| Buds and perennating organs | Paradormancy, endodormancy (chilling requirement), ecodormancy; potato tubers | GA, thiourea break; methyl naphthaleneacetate prolongs |

Main equations:

| Equation | Content |
|---|---|
| $v = K_i - p/\sigma$, $\log_{10}\sigma = K_E - C_W\log_{10}m - C_HT - C_QT^2$ | Seed longevity equation (Eq. (19.1) of [7.12.19](/7.12.19)) |
| Eq. (20.1) $\theta_{\mathrm{H}} = [\Psi - \Psi_{\mathrm{b}}(g)]t_g$ | Hydrotime |
| Eq. (20.2) $G = \Phi[(\Psi - \theta_{\mathrm{H}}/t - \Psi_{\mathrm{b}}(50))/\sigma]$ | Cumulative germination; probit linearization |
| Eq. (20.3) $\theta_{\mathrm{HT}} = [\Psi - \Psi_{\mathrm{b}}(g)](T - T_{\mathrm{b}})t_g$ | Hydrothermal time |
| $G = \Phi[(\mathrm{Pfr}/\mathrm{Ptot} - \mu)/s]$ | Threshold model of light-requiring seeds |
| $\ce{C16H32O2 + 11O2 -> 2C6H12O6 + 4CO2 + 4H2O}$ | Fat to sugar: about 1.4 g sugar per g fatty acid |

## Questions

1. A lot of wheat seeds shows 96 % of embryos stained red by the TTC test, but only 70 % emerge in moist soil at $10\,^\circ\mathrm{C}$. (a) What are the viability and the vigor of this lot? (b) List two vigor tests that can quantify this difference, and state what property of the seed each detects.

   **Answer** (a) Viability is high (96 % of embryos alive) and vigor is lower: under slightly unfavorable conditions (cold, moist soil) 26 % of the viable seeds fail to emerge normally, probably because they have already deteriorated partly during storage (membrane damage, decreased repair capacity). (b) Conductivity test: a measured quantity of seeds is soaked in deionized water for a set time and the conductivity of the soak water is measured; high conductivity indicates poor membrane integrity and much solute leakage. Accelerated aging test: after treatment for 2–4 days at about $42\,^\circ\mathrm{C}$ and near-saturated humidity, germination is measured; the more the germination falls, the lower the ability of the seed to resist deterioration (its storage potential). The cold test can also directly simulate conditions of early spring sowing.

2. Using the Ellis–Roberts equation with the barley constants (Example 20.1.1), calculate the time for a seed lot with initial viability 98 % to fall to 85 % at 10 % moisture content and $-18\,^\circ\mathrm{C}$, and compare with 5 % moisture content at $-18\,^\circ\mathrm{C}$. Discuss why seed banks still test viability regularly.

   **Answer** At $T = -18$: $C_HT = -0.72$, $C_QT^2 = 0.000428 \times 324 = 0.139$. Moisture content 10 %: $\log_{10}\sigma = 9.983 - 5.896 + 0.72 - 0.139 = 4.668$, $\sigma = 4.66\times10^4\,\mathrm{d}$, $p = 1.01\sigma = 4.7\times10^4\,\mathrm{d} \approx 129$ years. Moisture content 5 %: $\log_{10}\sigma = 9.983 - 5.896 \times 0.699 + 0.72 - 0.139 = 6.443$, $\sigma = 2.77\times10^6\,\mathrm{d}$, $p \approx 7.7\times10^3$ years. The model extrapolation goes far beyond the times and conditions actually verified (the equation is calibrated only for moisture contents of about 5 %–25 % and a limited temperature range, and the species constants also have errors), and the initial quality of seed lots, the drying process and the airtightness of packaging all vary; below about 5 % moisture content deterioration may actually speed up. Seed banks therefore sample regularly on a schedule to test germination and regenerate before viability falls to about 85 %.

3. A lot of lettuce seeds germinates 5 % in darkness, 90 % after 5 min of red light, and 8 % when 5 min of far-red light immediately follows the red. (a) If one waits 6 h after the red light before giving far-red, what might the germination be? Why? (b) In $10^{-5}\,\mathrm{mol\,L^{-1}}$ $\mathrm{GA_3}$, germination in darkness is 85 % and far-red cannot inhibit it. Explain where this result places GA in the signaling pathway.

   **Answer** (a) Germination would be clearly higher than 8 %, possibly close to the level with red alone: within hours Pfr has already started downstream irreversible processes (degradation of PIF1, induction of GA synthesis genes, weakening of the endosperm), and converting Pfr back to Pr then comes too late to "undo" the signal; photoreversibility is lost with time, and this "escape time" reflects the kinetics of the downstream events. (b) GA lies downstream of phytochrome signaling: red light raises GA synthesis and lowers its inactivation through phyB–PIF1, and applied GA directly satisfies this need, so light is no longer required; far-red affects only the state of phytochrome and cannot remove the GA already added, so it cannot reverse the effect.

4. Using the hydrotime model (parameters of Example 20.5.1), answer: (a) At $\Psi = -0.2\,\mathrm{MPa}$, how many hours are needed to reach 10 % and 90 % germination? (b) The soil water potential at sowing is $-0.3\,\mathrm{MPa}$; to reach 50 % germination within 72 h, to what value must priming lower $\Psi_{\mathrm{b}}(50)$ at least?

   **Answer** (a) $G = \Phi[(\Psi - \theta_{\mathrm{H}}/t - \Psi_{\mathrm{b}}(50))/\sigma]$, $\Phi^{-1}(0.10) = -1.28$, $\Phi^{-1}(0.90) = 1.28$. For 10 %: $-0.2 - 30/t + 0.70 = -0.256$, $30/t = 0.756$, $t = 40\,\mathrm{h}$; for 90 %: $-0.2 - 30/t + 0.70 = 0.256$, $30/t = 0.244$, $t = 123\,\mathrm{h}$. (b) The requirement is $t_{50} = \theta_{\mathrm{H}}/[\Psi - \Psi_{\mathrm{b}}(50)] \le 72$: $-0.3 - \Psi_{\mathrm{b}}(50) \ge 30/72 = 0.417$, $\Psi_{\mathrm{b}}(50) \le -0.72\,\mathrm{MPa}$. The original value is $-0.70$, so only a slight decrease (about $0.02\,\mathrm{MPa}$) is needed; if uniformity is also required, $\sigma$ must be reduced as well.

5. Why is red-grained wheat said to be more resistant to preharvest sprouting than white-grained wheat, and yet cultivars with no dormancy at all or with excessively deep dormancy are both undesirable in production? Explain in terms of the ABA/GA balance, the role of the seed coat and agricultural requirements.

   **Answer** Key points: the red color comes from proanthocyanidin-type compounds in the seed coat; phenolics of the coat can restrict oxygen entry and retain inhibitors, and the *R* gene (MYB) that controls color is connected to pathways related to ABA sensitivity and dormancy, so red-grained cultivars have a higher germination threshold (higher $\Psi_{\mathrm{b}}$) when rain comes at maturity and do not readily sprout in the ear. Cultivars with no dormancy at all start germinating in the ear as soon as it rains at maturity, the aleurone layer secretes α-amylase, the falling number drops and quality is damaged; cultivars with excessively deep dormancy germinate slowly and unevenly when sown after harvest (especially in regions with two crops a year where sowing follows harvest immediately) and need after-ripening or treatment. The ideal is "moderate dormancy": dormancy is maintained during the weeks before harvest and is released after harvest by short dry storage (after-ripening), which requires adjusting ABA synthesis and sensitivity (for example by combinations of alleles at loci such as *DOG1*, *TaPHS1* and *Sdr*) and introducing dormancy genes that do not depend on seed coat color into white-grained cultivars.
