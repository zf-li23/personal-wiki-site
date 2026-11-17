---
title: Secondary Production, Ecological Efficiencies and Pyramids
description: "The energy budget of a consumer (ingestion, egestion, assimilation, respiration, production) and secondary production; the correlation of primary and secondary production; measuring secondary production by energy budgets and by growth plus reproduction, the equivalence of the two population formulas, cohorts and the Allen curve, the instantaneous growth method; ecological efficiencies (consumption, assimilation, production, ecological growth, Lindeman and trophic transfer efficiencies) and their relations, typical values for endotherms, ectotherms, herbivores and carnivores, the ten-percent rule and its variability, warming and transfer efficiency; pyramids of energy, biomass and numbers and why biomass and number pyramids can be inverted; energy flow in Cedar Bog Lake and Silver Springs, H. T. Odum's energy language, a compartment model of grazer and decomposer pathways, and the energetic limit to food chain length."
---

Net primary production ([7.19.42](/7.19.42)) is the food supply of all heterotrophs. This chapter follows it up the **food chain**. A herbivore eats only part of the plant production available to it, digests only part of what it eats, and converts only part of what it digests into its own body; the rest is lost as faeces, which pass to the decomposers, and as respiratory heat, which leaves the ecosystem. Each step can be expressed as an efficiency, and the product of the steps determines how much energy reaches the next **trophic level**. This is the trophic-dynamic view of the ecosystem founded by Lindeman (1942) and developed by E. P. and H. T. Odum, and it explains the regularities that Elton (1927) had first described as pyramids. We begin with the energy budget of a consumer and the measurement of secondary production (43.1–43.2), define the ecological efficiencies and their relations and give their typical values (43.3), derive the shapes of ecological pyramids (43.4), and analyse the classic energy-flow studies and a compartment model of the grazer and decomposer pathways (43.5). The structure of food webs and the length of food chains are treated in [7.19.38](/7.19.38), the decomposer pathway in [7.19.44](/7.19.44), and the energetics of individual animals in animal physiology ([7.14.30](/7.14.30)).

## 43.1. The Process of Secondary Production

### 43.1.1. The Energy Budget of a Consumer

The food energy taken in by a consumer per unit time, its ingestion (or consumption) $I$, has three fates. Part is not digested and is egested as faeces $F$; the rest is assimilated, $A = I - F$. Of the assimilated energy, part is lost in nitrogenous waste (urine, $U$), part is respired to provide the energy for maintenance and activity, $R$, and the remainder is converted into new tissue (growth, $P_{\mathrm{g}}$) and offspring (reproduction, $P_{\mathrm{r}}$):

$$
I = A + F, \qquad A = P + R, \qquad P = P_{\mathrm{g}} + P_{\mathrm{r}}.
$$
In ecosystem studies the urinary loss is usually combined with the faeces ($FU$, "egesta") or counted as part of respiration, and the equations are written with $A = I - FU$. For a plant, intake is the light absorbed, assimilation is gross primary production and $P$ is net primary production. The budget is an application of the **first law of thermodynamics** (energy is conserved and the terms must balance), and the respiratory loss is a consequence of the **second law of thermodynamics**: every transformation of energy degrades part of it to heat, and living organisms must continuously do work to maintain their ordered state.

**Definition 43.1.1 (Secondary Production)** **Secondary production** is the production of new biomass by heterotrophs, $P = A - R$ per unit area and time, including growth of individuals and production of offspring, whether or not the biomass survives to the end of the period.

The definition counts all tissue produced, including individuals that die or are eaten during the period: secondary production is a flux, like NPP, not the change in biomass.

### 43.1.2. Primary and Secondary Production

Since secondary production depends on primary production, the two are correlated across ecosystems. The production of zooplankton in lakes increases with that of phytoplankton and is consistently about a tenth of it; bacterial production in lakes and the sea parallels phytoplankton production; herbivore consumption increases almost proportionally with primary production across aquatic and terrestrial ecosystems (Cebrian and Lartigue 2004), and the breeding of Darwin's finches on the Galápagos increases with rainfall, which drives plant production. Within a population, secondary production is highest when birth rates and individual growth are highest, which in seasonal environments coincides with the peak of primary production.

The relation between successive levels is not always proportional. Across African savannas, the biomass of large carnivores increases with that of their herbivore prey only as about the 0.75 power ($B_{\mathrm{pred}} \propto B_{\mathrm{prey}}^{0.73}$), and the same sublinear scaling holds for many other predator–prey systems, including zooplankton and phytoplankton (Hatton et al. 2015): the richer an ecosystem, the more bottom-heavy its pyramid, presumably because density dependence reduces production per unit biomass at high prey densities.

## 43.2. Measuring Secondary Production

### 43.2.1. The Energy Budget Method

The terms of the energy budget can be measured separately. Ingestion is measured in the laboratory or field by giving a known amount of food and weighing what remains after 24 h, or from the gut contents and the rate of gut evacuation; faeces and urine are collected; the energy content of food and faeces is measured by bomb calorimetry; and respiration is measured as oxygen consumption or carbon dioxide production in a respirometer and converted to energy with the oxycalorific equivalent (about $20\,\mathrm{kJ}$ per litre of $\ce{O2}$, depending slightly on the substrate respired). Then

$$
P = A - R = (I - FU) - R.
$$
For free-living animals, the **field metabolic rate** is measured with doubly labelled water ([7.14.30](/7.14.30)). The energy budget method is used for individual animals and small populations; its errors accumulate because $P$ is the small difference of large quantities.

### 43.2.2. Growth and Reproduction

The alternative is to measure production directly as the tissue produced, $P = P_{\mathrm{g}} + P_{\mathrm{r}}$. For a population over a time interval, two bookkeeping formulas are used:

$$
\begin{aligned}
P &= \text{growth of individuals} + \text{biomass of offspring born} - \text{weight lost by individuals}, \\
P &= \Delta B + E,
\end{aligned}
$$
where $\Delta B$ is the change in population biomass and $E$ the biomass eliminated by death (including predation) and emigration during the interval. The two formulas are equivalent. Consider a cohort of $N(t)$ individuals with mean mass $w(t)$, so that its biomass is $B = Nw$.

**Proposition 43.2.1** The production of a cohort between $t_0$ and $t_1$ is

$$
P = \int_{t_0}^{t_1} N\,\frac{\mathrm{d}w}{\mathrm{d}t}\,\mathrm{d}t = \Delta B + \int_{t_0}^{t_1} w\left(-\frac{\mathrm{d}N}{\mathrm{d}t}\right)\mathrm{d}t,
$$
the growth of the individuals present at each moment, which equals the change of biomass plus the biomass of the individuals that died, each counted at its mass at death.

**Proof** By the product rule, $\mathrm{d}B/\mathrm{d}t = N\,\mathrm{d}w/\mathrm{d}t + w\,\mathrm{d}N/\mathrm{d}t$. Integrating from $t_0$ to $t_1$ gives $\Delta B = \int N\,\mathrm{d}w - \int w\,(-\mathrm{d}N)$, which rearranges to the stated equality. The first integral is production by definition (tissue added by the individuals alive); the second is the elimination $E$. $\square$

### 43.2.3. Cohorts and the Allen Curve

Allen (1951) plotted the number of survivors $N$ of a cohort of brown trout against their mean mass $w$. By Proposition 43.2.1, the area under this curve, $\int N\,\mathrm{d}w$, is the production of the cohort over its life. The Allen curve is the standard graphical method for cohort production of fish and aquatic invertebrates, and it shows at a glance how production is divided between the biomass remaining and the biomass lost to mortality, which is the food supply of predators. For populations that cannot be followed as cohorts, the instantaneous growth method estimates production in each interval as

$$
P = G\,\bar{B}, \qquad G = \frac{\ln(w_{t_1}/w_{t_0})}{t_1 - t_0},
$$
the specific growth rate times the mean biomass, which follows from $N\,\mathrm{d}w/\mathrm{d}t = (\mathrm{d}\ln w/\mathrm{d}t)\,Nw$ when $G$ is constant over the interval. The ratio of annual production to mean biomass, $P/\bar{B}$, is a turnover rate: about 1–3 per year for fish, 3–10 for many stream insects, and above 50 for small zooplankton.

![Cohort production and the Allen curve (simulated cohort: survival N(t) = 1000 e^(−0.8t) per 100 m², von Bertalanffy growth w(t) = 300 (1 − e^(−0.5t))³ g, over 6 years). A: survivors and mean mass against age. B: the Allen curve, survivors against mean mass. The total area under the curve is the cohort's production (Proposition 43.2.1); it is divided into the biomass eliminated by mortality during growth (light) and the biomass of the survivors at the end (dark). Most of the production of a fish cohort is eaten or dies before the end, the food supply of predators.](./plots/allen-curve.py)

## 43.3. Ecological Efficiencies

### 43.3.1. Definitions

The ratios between the energy flows of the budget, within and between trophic levels, describe how energy passes up a food chain.

**Definition 43.3.1 (Ecological Efficiency)** An **ecological efficiency** is a ratio, expressed as a percentage, between two energy flows (intake $I$, assimilation $A$, respiration $R$, production $P$) within one trophic level or between successive trophic levels, both measured in the same units of energy. Writing the subscript $n$ for trophic level $n$, the main efficiencies are:

| Efficiency | Definition | Meaning |
|---|---|---|
| Assimilation efficiency | $A_n/I_n$ | Fraction of food eaten that is absorbed (for plants: GPP/light absorbed) |
| Production efficiency (net growth efficiency) | $P_n/A_n$ | Fraction of assimilated energy converted to new biomass |
| Ecological growth efficiency (gross growth efficiency) | $P_n/I_n$ | Fraction of food eaten converted to new biomass |
| Consumption (exploitation) efficiency | $I_{n+1}/P_n$ | Fraction of the production of one level eaten by the next |
| Trophic-level assimilation efficiency (standard efficiency) | $A_{n+1}/A_n$ | Ratio of assimilation at successive levels |
| Trophic transfer efficiency | $P_{n+1}/P_n$ | Ratio of production at successive levels |

**Definition 43.3.2 (Lindeman Efficiency)** The **Lindeman efficiency** is the ratio of the energy intake of a trophic level to that of the level below,

$$
L_n = \frac{I_{n+1}}{I_n},
$$
where for the producers the intake is the light absorbed (or incident).

The definitions differ in which flows are compared, and published values are comparable only if this is stated. Lindeman himself compared the assimilation ("gross productivity") of successive levels, so that the values usually quoted for Cedar Bog Lake (43.5.1) are ratios $A_{n+1}/A_n$; Odum's textbook defines the Lindeman efficiency as the ratio of intakes (Odum and Barrett 2005), and many textbooks follow him. For a food chain whose efficiencies do not change from level to level, all these between-level ratios coincide. Units matter as well: a poultry farmer who obtains 1 kg of live chicken from 2.5 kg of feed speaks of a 40% conversion, but live chicken (about $8\,\mathrm{kJ\,g^{-1}}$) and dry feed (about $17\,\mathrm{kJ\,g^{-1}}$) differ in energy content, and the ecological growth efficiency in energy units is about 20% (Odum and Barrett 2005).

**Proposition 43.3.1** The between-level efficiencies factorize into within-level and consumption efficiencies:

$$
L_n = \frac{I_{n+1}}{I_n} = \frac{A_n}{I_n}\cdot\frac{P_n}{A_n}\cdot\frac{I_{n+1}}{P_n}, \qquad
\frac{P_{n+1}}{P_n} = \frac{I_{n+1}}{P_n}\cdot\frac{A_{n+1}}{I_{n+1}}\cdot\frac{P_{n+1}}{A_{n+1}}.
$$
If the assimilation, production and consumption efficiencies $a$, $p$, $c$ are the same at all consumer levels, then $L_n = A_{n+1}/A_n = P_{n+1}/P_n = acp$ for every consumer level, and the energy reaching level $n + k$ is $(acp)^k$ times that at level $n$.

**Proof** Both identities are telescoping products: the intermediate quantities cancel. With constant efficiencies, $I_{n+1} = cP_n = cpA_n = cpaI_n$, so $L_n = acp$; then $A_{n+1}/A_n = aI_{n+1}/(aI_n) = L_n$ and $P_{n+1}/P_n = pA_{n+1}/(pA_n) = L_n$. Iterating gives the power. $\square$

Because the transfer efficiency is a product of three fractions, each less than one, it is small, and its logarithm is the sum of three terms: the factor by which energy declines per level is set by whichever of the three is smallest.

### 43.3.2. Typical Values

The three component efficiencies vary systematically with the type of organism and food (Begon and Townsend 2021; Odum and Barrett 2005; Humphreys 1979):

- Consumption efficiency of herbivores is low where plants invest much in structural tissue: the median is below 5% in forests, about 25% in grasslands and more than 50% in phytoplankton communities, where the producers are small, fast-growing, unprotected cells. Plants with high growth rates, short generations and rapid turnover, and herbaceous plants with little support tissue, are eaten in larger proportion than woody plants. Vertebrate predators may consume 50–100% of the production of vertebrate prey, but perhaps only 5% of invertebrate prey production; invertebrate predators about 25%. Whatever is not eaten dies and enters the detritus, so that in most ecosystems 65–75% or more of the production of each level passes to decomposers.
- Assimilation efficiency depends mainly on the food. It is low for herbivores, detritivores and microbivores (typically 20–50%) and high for carnivores (80% or more). Plant tissues differ: seeds and fruits are assimilated with about 60–70% efficiency, young leaves about 50%, wood as little as 15%, because cellulose and lignin are hard to digest and plants contain defences ([7.19.24](/7.19.24)). Herbivores that harbour cellulose-digesting symbionts (ruminants, termites) raise their assimilation efficiency; for bacteria and fungi, which digest externally and absorb almost all of what they digest, the concept is hardly applicable.
- Production efficiency depends on metabolism and size. **Endotherms**, which spend most of their assimilated energy on maintaining a high body temperature, convert only 1–3% into production; small endotherms (shrews, wrens), which lose heat fastest, have the lowest efficiencies of all. **Ectotherms** have much higher values: about 10% for fish, 25–40% for non-insect invertebrates and 40–55% for non-social insects. Microorganisms and protists, with small size and rapid turnover, have very high production efficiencies. Among plants, autotrophic respiration consumes 40–60% of GPP, so that $P/A$ is 40–60%.

| Group (Humphreys 1979) | Production efficiency $P/A$ / % |
|---|---|
| Insectivores (shrews) | 0.9 |
| Birds | 1.3 |
| Small mammal communities | 1.5 |
| Other mammals | 3.1 |
| Fish and social insects | 9.8 |
| Non-insect invertebrates | 25.0 |
| Non-social insects | 40.7 |

![Ecological efficiencies. A: production efficiency (P/A) of animal groups (Humphreys 1979), on a logarithmic scale: endotherms convert only 1–3% of assimilated energy to production, ectotherms 10–40% or more. B: trophic transfer efficiency CE × AE × PE (Proposition 43.3.1) computed for three illustrative chains from typical component values: a mammalian herbivore in a forest (CE 5%, AE 50%, PE 2%), an insect herbivore in a grassland (CE 25%, AE 35%, PE 40%) and zooplankton grazing phytoplankton (CE 60%, AE 60%, PE 30%), with the ten-percent rule (dashed) for comparison.](./plots/efficiencies.py)

The contrasts multiply. A food chain of mammals in a forest passes on well under 1% of the energy from one level to the next, whereas a chain of invertebrates or plankton passes on 10% or more; the transfer from moose to wolf on Isle Royale is about 1%, that in a *Daphnia*–*Hydra* chain about 10% (Lawton 1981). Herbivores tend to have higher production efficiencies but lower assimilation efficiencies than carnivores.

### 43.3.3. The Ten-Percent Rule

Lindeman (1942) found that the efficiency of transfer between levels in the lakes he studied was of the order of 10–20%, and the "ten-percent rule" (or "law") became a rule of thumb: about a tenth of the energy reaching one trophic level reaches the next. It is not a law. In a compilation of 48 trophic studies of aquatic ecosystems, trophic transfer efficiencies ranged from about 2% to 24% with a mean of 10.13% (Pauly and Christensen 1995); in marine food webs the mean is about 13% from phytoplankton to zooplankton and benthic invertebrates and about 10% from these to fish (Ware 2000). Terrestrial chains involving endotherms are less efficient. The ten-percent rule is nevertheless useful for estimates: it implies that a fishery harvesting fish at the fourth trophic level is supported by about $10^3$ times its yield in primary production, which is why the yield of the world's fisheries is limited by the production of the oceans (Pauly and Christensen 1995 estimated that fisheries require about 8% of global aquatic primary production, and much more on continental shelves and in upwellings), and why eating plants supports more people than eating meat.

Transfer efficiency also changes with temperature. Because respiration rises with temperature faster than photosynthesis ([7.19.6](/7.19.6#sec-6.6.3)), warming is expected to reduce the efficiency of energy transfer. In outdoor experimental ponds warmed by 4 °C for seven years, Barneche et al. (2021) traced a ¹⁵N label from phytoplankton to zooplankton and found that the warmed ponds had lower phytoplankton and zooplankton biomass (by about 56% and 38% on average) and a lower efficiency of nitrogen transfer to the zooplankton. If this generalizes, warming will reduce the production available at the top of aquatic food webs, including fish, by more than the change in primary production would suggest.

## 43.4. Ecological Pyramids

**Definition 43.4.1 (Ecological Pyramid)** An **ecological pyramid** is a diagram of the trophic structure of a community in which each trophic level is represented by a horizontal bar whose length is proportional to a quantity at that level, with producers at the base: a pyramid of energy (or production) shows the energy flow through each level per unit area and time, a pyramid of biomass the standing biomass, and a pyramid of numbers the number of individuals.

Elton (1927) recognized the pyramid of numbers: in most communities there are many small animals at the base of the food chains and few large ones at the top. Pyramids of energy are always upright, whereas pyramids of biomass and numbers may be inverted.

**Proposition 43.4.1** In a food chain without imports, the energy flow (assimilation, or production) of each level is smaller than that of the level below: $A_{n+1} < P_n < A_n$. The biomass of level $n$ is $B_n = P_n/\pi_n$, where $\pi_n = P_n/B_n$ is the production-to-biomass (turnover) ratio of the level, so that

$$
\frac{B_{n+1}}{B_n} = \frac{P_{n+1}}{P_n}\cdot\frac{\pi_n}{\pi_{n+1}},
$$
and the biomass pyramid is inverted at level $n$ ($B_{n+1} > B_n$) if and only if the producers' turnover exceeds the consumers' by more than the inverse of the transfer efficiency, $\pi_n/\pi_{n+1} > P_n/P_{n+1}$.

**Proof** Without imports, level $n + 1$ eats only production of level $n$: $I_{n+1} \le P_n$; since assimilation is less than intake, $A_{n+1} < I_{n+1} \le P_n$, and since respiration is positive, $P_n < A_n$. Production also decreases, $P_{n+1} < A_{n+1} < P_n$. The biomass relation follows from $B_n = P_n/\pi_n$ for each level, and $B_{n+1} > B_n$ is equivalent to the stated inequality. $\square$

The proposition explains the inversions. In the English Channel the standing biomass of phytoplankton ($4\,\mathrm{g\,m^{-2}}$ dry mass) was smaller than that of zooplankton and bottom fauna ($21\,\mathrm{g\,m^{-2}}$; Harvey 1950), because phytoplankton divide about once a day (turnover of several hundred per year) while zooplankton turn over a few tens of times a year: a small but rapidly renewed producer biomass supports a larger but slowly renewed consumer biomass, as a small but fast-flowing spring can fill a large reservoir. Pyramids of numbers are inverted when the producers are large individuals, as in a temperate forest where one tree supports thousands of caterpillars, and in parasite food chains, where one host supports many parasites. Pyramids of energy cannot be inverted, except in ecosystems that import organic matter (a stream fed by forest litter), because of the second law of thermodynamics. Energy flow is therefore the most reliable basis for comparing populations: in a classic comparison of six primary consumer populations, from soil bacteria to deer, population density differed by a factor of $10^{17}$ and biomass by $10^5$, but energy flow by only a factor of about 5 (E. P. Odum 1968).

![Ecological pyramids computed from a model food chain (Proposition 43.4.1). A: pyramid of production for a plankton chain with NPP 1000 kJ m⁻² yr⁻¹ and transfer efficiencies of 13%, 10% and 10%, always upright. B: the corresponding pyramid of biomass (dry mass, at 20 kJ g⁻¹), with turnover ratios (P/B per year) of 300 for phytoplankton, 20 for zooplankton, 2 for planktivorous fish and 0.5 for piscivores: the rapidly renewed phytoplankton have a smaller standing biomass than the zooplankton, so the pyramid is inverted at its base. C: a pyramid of numbers for a temperate forest (per hectare, illustrative): a few hundred trees, a million herbivorous insects, tens of thousands of predatory insects and spiders and a few insectivorous birds, inverted at its base because the producers are large. Bar lengths are logarithmic in B and C.](./plots/pyramids.py)

## 43.5. Energy Flow Analysis

### 43.5.1. Cedar Bog Lake

Lindeman's (1942) study of Cedar Bog Lake, a small senescent lake in Minnesota, was the first quantitative energy budget of an ecosystem, and it is still the clearest illustration of the trophic-dynamic concept. In energy units ($\mathrm{J\,cm^{-2}\,yr^{-1}}$, converted from Lindeman's calories), the budget was:

| Trophic level | Assimilation $A$ | Respiration | To decomposers | Unused (stored in sediment) | Passed to next level |
|---|---|---|---|---|---|
| Producers | 464.6 | 96.3 | 12.5 | 293.0 | 62.8 |
| Herbivores | 62.8 | 18.8 | 2.1 | 29.3 | 12.6 |
| Carnivores | 12.6 | 7.5 | trace | 5.0 | — |

Incident solar radiation was about $497\,700\,\mathrm{J\,cm^{-2}\,yr^{-1}}$, so the efficiency of gross primary production was only about 0.1%. Each row balances: for the producers $96.3 + 12.5 + 293.0 + 62.8 = 464.6$. The transfer efficiencies between levels, in Lindeman's sense ($A_{n+1}/A_n$), were $62.8/464.6 = 13.5\%$ and $12.6/62.8 = 20.1\%$. The fraction of assimilated energy respired increased up the chain, from $96.3/464.6 = 21\%$ in the producers to 30% in the herbivores and 60% in the carnivores, which are more active. The large "unused" fraction, energy accumulating as peat and sediment, is characteristic of a lake that is filling in: the ecosystem was not in steady state, and Lindeman interpreted its succession towards a bog as a consequence of this imbalance.

![Energy flow in Cedar Bog Lake and a compartment model of the grazer and decomposer pathways. A: the fate of the energy assimilated at each trophic level in Cedar Bog Lake (Lindeman 1942; J cm⁻² yr⁻¹): respiration, passage to decomposers, accumulation in sediment (unused) and transfer to the next level, with the transfer efficiencies. B: the fraction of net primary production that is respired in the grazer chain or passes into dead organic matter in the compartment model of Proposition 43.5.1, for a forest (herbivore consumption efficiency 5%), a grassland (25%) and a plankton community (60%); the parameters are given in the text.](./plots/energy-flow.py)

### 43.5.2. Silver Springs and the Energy Language

H. T. Odum (1957) measured the energy flow of Silver Springs, Florida, a large spring-fed stream with constant temperature and chemistry, dominated by eelgrass (*Sagittaria*) and attached algae. In $\mathrm{kJ\,m^{-2}\,yr^{-1}}$ (converted from Odum's $\mathrm{kcal\,m^{-2}\,yr^{-1}}$ with $1\,\mathrm{kcal} = 4.184\,\mathrm{kJ}$): gross primary production was 87 070 (20 810 kcal), producer respiration 50 110, net primary production 36 960; the herbivores assimilated 14 090 and respired 7 910; the carnivores assimilated 1 600 and respired 1 320; the top carnivores assimilated 88 and respired 54; the decomposers processed 21 170 and respired 19 250; 10 460 were exported downstream as organic matter, and 2 030 were imported as bread fed to fish by visitors. Total respiration plus export equals GPP plus import, so the system was in steady state. GPP was about 1.2% of incident sunlight and 5% of the light absorbed by the plants; the assimilation of successive consumer levels was 16%, 11% and 5.5% of the level below.

To describe such systems, H. T. Odum developed an energy circuit language, a set of symbols for energy sources (circles), storages (tank shapes), producers (bullet shapes), consumers (hexagons), interactions in which one flow controls another (workgates) and heat sinks (the ground symbol), with the second law built in: every process and storage drains energy to a heat sink. The language makes it possible to write any ecosystem diagram as a system of differential equations, and it was the basis of his concepts of energy quality and eMergy, the solar energy required directly and indirectly to make a product (Odum and Barrett 2005). Real energy flows can be compared across ecosystems in such diagrams: forests have a small grazer pathway and large standing stocks of wood and dead organic matter; grasslands with large herds of grazers have a larger grazer pathway; plankton communities pass much of their production through grazers and have small standing stocks; and streams and deep-sea communities depend on imported dead organic matter.

### 43.5.3. A Compartment Model of Energy Flow

The general structure of energy flow (Heal and MacLean 1975; Begon and Townsend 2021) has two subsystems that share the same net primary production: a grazer system based on the consumption of living plants, and a decomposer system based on dead organic matter, which receives the unconsumed production and the faeces of every level of the grazer system, and the bodies and faeces of its own organisms. The two differ in one decisive respect: energy lost from the grazer system as faeces and dead bodies passes to the decomposer system, whereas faeces and dead bodies within the decomposer system return to its own base, the pool of dead organic matter, and are reprocessed until all the energy has been respired (or exported, or buried as peat, coal and oil). A simple compartment model makes this quantitative.

Let NPP $= N$ enter a chain of consumer levels. Level 2 eats a fraction $c_1$ of $N$, and each consumer level eats a fraction $c$ of the production of the level below, assimilates a fraction $a$ of its intake and converts a fraction $p$ of its assimilation into production. Everything not eaten, not assimilated or not respired becomes dead organic matter $D$. At steady state, dead organic matter is decomposed as fast as it is supplied.

**Proposition 43.5.1** In this model, the energy respired by the grazer system is

$$
R_{\mathrm{G}} = \frac{c_1 a (1 - p)}{1 - cap}\,N,
$$
the energy flowing into dead organic matter is $N - R_{\mathrm{G}}$, and in a steady state without imports, exports or burial, the total heterotrophic respiration equals $N$, so that $\mathrm{NEP} = 0$.

**Proof** The intake of level 2 is $I_2 = c_1N$, and that of level $k + 1$ is $I_{k+1} = cP_k = cpaI_k$, so $I_{k} = c_1N(cap)^{k-2}$ for $k \ge 2$. Each level respires $(1 - p)aI_k$; summing the geometric series (convergent since $cap < 1$) gives $R_{\mathrm{G}} = (1 - p)a c_1 N\sum_{j \ge 0}(cap)^j = c_1a(1 - p)N/(1 - cap)$. Every joule of $N$ is eventually either respired in the grazer system or released into dead organic matter (as uneaten production, faeces or uneaten consumer production), so the input to $D$ is $N - R_{\mathrm{G}}$. At steady state $D$ is constant, so the decomposers respire $N - R_{\mathrm{G}}$, and total heterotrophic respiration is $R_{\mathrm{G}} + (N - R_{\mathrm{G}}) = N$; by Definition 42.1.1 of [7.19.42](/7.19.42#sec-42.1.1), $\mathrm{NEP} = N - R_{\mathrm{H}} = 0$. $\square$

For a forest with $c_1 = 0.05$ and herbivores with $a = 0.4$ and $p = 0.1$ (a mixture of insects and mammals), and higher levels with $c = 0.25$, $a = 0.8$, $p = 0.1$, the herbivores respire $0.05 \times 0.4 \times 0.9 = 1.8\%$ of NPP and all higher levels together less than 0.04% (applying the proposition from level 3 upwards to the herbivore production $0.05 \times 0.4 \times 0.1\,N$), so the grazer system respires about 1.8% of NPP; in a grassland with $c_1 = 0.25$ and the same herbivore efficiencies, about 9%; in a plankton community with $c_1 = 0.6$, $a = 0.6$, $p = 0.3$ and $c = 0.3$, about 26%. In every case, more than 70% of NPP is respired by the decomposer system, which is therefore responsible for most of the secondary production and respiration in every ecosystem on Earth; even in the plankton, bacteria consume much of the dissolved organic matter released by phytoplankton (the **microbial loop**, [7.11.29](/7.11.29#sec-29.9.2)). The model also shows that the grazer system can be large only where plants are eaten in large proportion, that is, where they are small, fast-growing and poorly defended.

### 43.5.4. The Energetic Limit to Food Chain Length

**Proposition 43.5.2** If the transfer efficiency between levels is a constant $\tau < 1$ and a trophic level can persist only if its production is at least $P_{\min}$, the maximum number of trophic levels supported by a primary production $P_1$ is

$$
n_{\max} = 1 + \left\lfloor \frac{\ln(P_1/P_{\min})}{\ln(1/\tau)} \right\rfloor.
$$

**Proof** By Proposition 43.3.1, $P_n = \tau^{n-1}P_1$. The condition $P_n \ge P_{\min}$ is $(n - 1)\ln(1/\tau) \le \ln(P_1/P_{\min})$, and the largest integer $n$ satisfying it is the stated value. $\square$

With $\tau = 0.1$, each additional level requires ten times more primary production, and a hundredfold increase of productivity adds only two levels. This is the energetic explanation of why food chains rarely have more than four or five levels (Elton 1927; Hutchinson 1959). It predicts that chain length should increase with productivity, but the data show only weak relations: food chains are not much longer in productive than in unproductive lakes, and in a study of lakes, chain length (measured with nitrogen isotopes) increased with ecosystem size rather than productivity (Post et al. 2000). Other hypotheses, the dynamic stability of long chains, the size constraints of predators and the productive space (productivity times ecosystem size), are compared in [7.19.38](/7.19.38).

## Summary

- The energy budget of a consumer: $I = A + F$, $A = P + R$, $P = P_{\mathrm{g}} + P_{\mathrm{r}}$; secondary production (Definition 43.1.1) is the production of new heterotroph biomass, including tissue later lost to death or predation. Secondary production increases with primary production.
- Measurement: $P = (I - FU) - R$ (energy budget), or $P = \Delta B + E$ = growth + births − weight loss (Proposition 43.2.1); the area under the Allen curve is cohort production; $P = G\bar{B}$ (instantaneous growth method).
- Efficiencies (Definition 43.3.1): assimilation $A_n/I_n$, production $P_n/A_n$, ecological growth $P_n/I_n$, consumption $I_{n+1}/P_n$, **Lindeman efficiency** $I_{n+1}/I_n$ (Definition 43.3.2), standard $A_{n+1}/A_n$, trophic transfer $P_{n+1}/P_n$; between-level efficiencies are products of the three component efficiencies (Proposition 43.3.1).

| Component | Low | High |
|---|---|---|
| Consumption efficiency | Forests (< 5%) | Phytoplankton communities (> 50%); vertebrate predators of vertebrates (50–100%) |
| Assimilation efficiency | Herbivores, detritivores (20–50%; wood 15%) | Carnivores (≥ 80%); seeds (60–70%) |
| Production efficiency | Endotherms (1–3%; shrews < 1%) | Ectotherms (10% fish to 40–55% insects); microorganisms |

- Transfer efficiency averages about 10% in aquatic food webs (range 2–24%), lower in chains of endotherms; warming may reduce it.
- **Ecological pyramids** (Definition 43.4.1): energy pyramids are always upright; biomass pyramids are inverted when producers turn over much faster than consumers (plankton), number pyramids when producers are large (forests) or in parasite chains (Proposition 43.4.1).
- Energy flow: Cedar Bog Lake (transfer 13.5% and 20.1%, large storage in sediment), Silver Springs (steady state, GPP 1.2% of sunlight); H. T. Odum's energy language. In a compartment model, the grazer system respires $c_1a(1 - p)N/(1 - cap)$, a few percent of NPP in forests to about a quarter in plankton; the decomposer system respires the rest (Proposition 43.5.1). Energetics limits food chains to a few levels, $n_{\max} = 1 + \lfloor\ln(P_1/P_{\min})/\ln(1/\tau)\rfloor$ (Proposition 43.5.2), but chain length also depends on ecosystem size and stability.

## Questions

1. A caterpillar eats $100\,\mathrm{J}$ of leaf, produces $60\,\mathrm{J}$ of faeces and respires $24\,\mathrm{J}$. A shrew eats $100\,\mathrm{J}$ of caterpillars, produces $10\,\mathrm{J}$ of faeces and urine and respires $88\,\mathrm{J}$. Calculate the assimilation, production and ecological growth efficiencies of each, and explain the differences.

   **Answer** Caterpillar: $A = 100 - 60 = 40$, $P = 40 - 24 = 16\,\mathrm{J}$; assimilation efficiency 40%, production efficiency $16/40 = 40\%$, ecological growth efficiency 16%. Shrew: $A = 90$, $P = 90 - 88 = 2\,\mathrm{J}$; assimilation 90%, production $2/90 = 2.2\%$, ecological growth 2%. The caterpillar eats plant tissue rich in cellulose, lignin and defensive compounds, which it digests poorly, but as an ectotherm it spends little energy on maintenance and converts much of what it assimilates into growth. The shrew eats animal tissue, which is easily digested, but as a small endotherm with a high surface-to-volume ratio it spends almost all its assimilated energy on maintaining its body temperature and on activity.

2. A trout cohort has 2000 individuals of mean mass 10 g in spring, 800 of mean mass 60 g a year later and 300 of mean mass 150 g after two years. Estimate the cohort's production in each year with the Allen curve (trapezoidal rule) and check the result against $P = \Delta B + E$.

   **Answer** Year 1: $\int N\,\mathrm{d}w \approx \frac{2000 + 800}{2} \times (60 - 10) = 70\,000\,\mathrm{g}$. Year 2: $\frac{800 + 300}{2} \times (150 - 60) = 49\,500\,\mathrm{g}$. Check for year 1: $\Delta B = 800 \times 60 - 2000 \times 10 = 28\,000\,\mathrm{g}$; the 1200 fish that died, if they died on average at about the mean of the initial and final masses (35 g), represent $E \approx 42\,000\,\mathrm{g}$; $\Delta B + E \approx 70\,000\,\mathrm{g}$, in agreement. (The trapezoidal rule implicitly assumes that $N$ declines linearly with $w$ between samples; both estimates depend on this assumption.) Year 2: $\Delta B = 45\,000 - 48\,000 = -3000$, $E \approx 500 \times 105 = 52\,500$, sum $49\,500\,\mathrm{g}$. Note that in the second year production is large although the biomass declines.

3. In a grassland, NPP is $4000\,\mathrm{kJ\,m^{-2}\,yr^{-1}}$. Grasshoppers eat 20% of it, assimilate 35% of what they eat and have a production efficiency of 40%; birds eat 30% of the grasshopper production, assimilate 80% and have a production efficiency of 1.5%. Calculate the production of each level, the Lindeman efficiencies and the trophic transfer efficiencies.

   **Answer** Grasshoppers: $I_2 = 800$, $A_2 = 280$, $P_2 = 112\,\mathrm{kJ\,m^{-2}\,yr^{-1}}$. Birds: $I_3 = 33.6$, $A_3 = 26.9$, $P_3 = 0.40\,\mathrm{kJ\,m^{-2}\,yr^{-1}}$. Transfer efficiencies: $P_2/P_1 = 112/4000 = 2.8\%$ (= $0.2 \times 0.35 \times 0.4$), $P_3/P_2 = 0.40/112 = 0.36\%$ (= $0.3 \times 0.8 \times 0.015$). Lindeman efficiency $I_3/I_2 = 33.6/800 = 4.2\%$ (= $0.35 \times 0.4 \times 0.3$); $I_2/I_1$ requires the intake of the producers (absorbed light), which is not given. The endothermic birds are the bottleneck: their low production efficiency makes the bird level a very small fraction of the energy flow, even though they assimilate their food efficiently.

4. The phytoplankton of a lake have a mean biomass of $2\,\mathrm{g\,m^{-2}}$ and the zooplankton $5\,\mathrm{g\,m^{-2}}$. Is this consistent with the second law of thermodynamics? What turnover rates would make it consistent with a transfer efficiency of 10%?

   **Answer** Yes: the second law forbids an inverted pyramid of energy flow, not of standing biomass. By Proposition 43.4.1, $B_2/B_1 = (P_2/P_1)(\pi_1/\pi_2)$; with $P_2/P_1 = 0.1$ and $B_2/B_1 = 2.5$, the producers' turnover ratio must be 25 times that of the zooplankton, for example $\pi_1 = 250$ per year (cells dividing about every day and a half, allowing for losses) and $\pi_2 = 10$ per year. These are realistic values; the inverted biomass pyramid reflects the rapid turnover of the phytoplankton, and a snapshot of biomass says nothing about the flow of energy.

5. (Open question) Using Proposition 43.5.1 and the typical efficiencies, explain why the fraction of NPP consumed by herbivores is much larger in the open ocean than in a forest, and what consequences this has for the role of decomposers and for the accumulation of dead organic matter in the two ecosystems.

   **Answer** Points to include: (a) phytoplankton are single cells with no support tissue, little chemical defence and very rapid turnover, so grazers can eat a large fraction of production ($c_1 > 0.5$) with high assimilation efficiency; trees invest most of their production in wood and defended leaves, so $c_1$ is a few percent and assimilation efficiency is low; (b) by Proposition 43.5.1, the grazer system respires about a quarter of NPP in the plankton but only a few percent in a forest, so in forests almost all NPP goes to decomposers, mainly as leaf litter and wood; (c) consequently forests accumulate large stores of litter, dead wood and soil organic matter (especially where decomposition is slow), while in the ocean little organic matter accumulates at the surface: dead cells and faeces are consumed quickly by bacteria (the microbial loop) and a small fraction sinks to the deep sea, where it supports the deep-sea food web and part is buried in sediments (the biological pump); (d) even in the ocean, bacteria respire a large part of production, so the decomposer pathway is quantitatively dominant in both.
