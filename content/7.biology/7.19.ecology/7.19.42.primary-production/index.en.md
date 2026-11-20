---
title: Primary Production
description: "Gross and net primary production, autotrophic and heterotrophic respiration, ecosystem respiration and net ecosystem production, with a pool model of NEP over stand age; production and productivity, biomass and units; global patterns (NPP by biome, land and ocean, NPP:B ratios), human appropriation of NPP, the distribution and trends of NPP in China and forest age; measurement by harvest, light–dark bottles (worked example), diel oxygen curves, chambers and eddy covariance, ¹⁴C uptake, chlorophyll, NDVI and the light-use efficiency model; the efficiency of primary production; limiting factors on land (the Miami model, actual evapotranspiration, precipitation in grasslands, growing season, nutrients) and in water (light, nutrients, iron, upwelling and Sverdrup's critical depth); the effects of consumers on primary production."
---

All energy that flows through an **ecosystem** (apart from that of chemosynthetic communities) enters it by photosynthesis, and the rate at which producers fix energy sets the upper limit to everything the consumers and decomposers can do. Plant physiology treats photosynthesis in the chloroplast, the leaf and the canopy ([7.13.8](/7.13.8), [7.13.9](/7.13.9)) and has already introduced **gross primary production** and **net primary production** ([7.13.1](/7.13.1#sec-1.3.2)). This chapter takes the ecosystem view. We define the components of the carbon balance of an ecosystem and the net ecosystem production that decides whether it is a sink or a source of carbon (42.1), describe how primary production varies across the Earth and how much of it humans use (42.2), explain how it is measured, from bottles of lake water to satellites (42.3), and ask how efficiently sunlight is converted (42.4) and what limits production on land and in water (42.5). Two quantitative models are at the center: the Miami model, which predicts terrestrial production from temperature and precipitation by the **law of the minimum**, and Sverdrup's critical depth, which explains the spring bloom of phytoplankton. The fate of primary production in food chains is the subject of the next two chapters ([7.19.43](/7.19.43), [7.19.44](/7.19.44)), and its role in the carbon cycle of [7.19.45](/7.19.45).

## 42.1. Concepts

### 42.1.1. Gross and Net Primary Production

Primary production is the production of organic matter by autotrophs. Gross primary production (GPP) is the total rate of photosynthetic fixation by the producers of an area; part of it is respired by the producers themselves (autotrophic respiration $R_{\mathrm{A}}$), and the rest, net primary production (NPP), is the organic matter available for the growth and reproduction of the producers, for herbivores and, after death, for decomposers:

$$
\mathrm{NPP} = \mathrm{GPP} - R_{\mathrm{A}}.
$$
In most ecosystems $R_{\mathrm{A}}$ is 40–60% of GPP, so that NPP is roughly half of GPP; it is a larger fraction in phytoplankton and young, fast-growing vegetation and a smaller one in old forests with much living wood to maintain ([7.13.12](/7.13.12)).

Organic matter fixed in an ecosystem is called autochthonous; organic matter imported from elsewhere (leaf litter falling into a stream, guano carried to a seabird colony) is allochthonous. The heterotrophs of the ecosystem (animals, fungi, heterotrophic bacteria, archaea and protists) consume both and release carbon by heterotrophic respiration $R_{\mathrm{H}}$. The total ecosystem respiration is $R_{\mathrm{E}} = R_{\mathrm{A}} + R_{\mathrm{H}}$.

**Definition 42.1.1 (Net Ecosystem Production)** **Net ecosystem production** (NEP) is the difference between gross primary production and ecosystem respiration,

$$
\mathrm{NEP} = \mathrm{GPP} - R_{\mathrm{E}} = \mathrm{NPP} - R_{\mathrm{H}}.
$$
It is the rate at which organic carbon accumulates in the ecosystem (in biomass, dead organic matter and soil) or is exported. An ecosystem with $\mathrm{NEP} > 0$ is a carbon sink, one with $\mathrm{NEP} < 0$ a carbon source.

NEP can be negative only if the ecosystem lives partly on stored or imported organic matter: a forest stand in the years after a clear-cut, whose decomposers are consuming the dead roots and slash; a peatland that is drained; and most streams and many small lakes, which respire more than they fix because they receive allochthonous litter from their catchments ([7.19.41](/7.19.41#sec-41.4.2)). Over larger areas and longer times, losses by fire, harvest and erosion must also be counted; net biome production (NBP) is NEP minus these non-respiratory losses, and it is NBP that determines the net exchange of carbon between the land and the atmosphere.

### 42.1.2. Production, Productivity and Biomass

Production is an amount per unit area and time; it is also called productivity when the emphasis is on the rate. It is expressed as dry matter ($\mathrm{g\,m^{-2}\,yr^{-1}}$ or $\mathrm{t\,ha^{-1}\,yr^{-1}}$; $1\,\mathrm{t\,ha^{-1}} = 100\,\mathrm{g\,m^{-2}}$), as carbon (dry plant matter is about 45–50% carbon, so $1\,\mathrm{g}$ dry matter $\approx 0.47\,\mathrm{g\,C}$), or as energy (about $18$–$20\,\mathrm{kJ}$ per gram of dry plant matter, more for seeds rich in lipids). Global fluxes are given in petagrams of carbon ($1\,\mathrm{Pg} = 10^{15}\,\mathrm{g}$ = 1 billion tonnes).

Biomass, or standing crop, is the amount of living organic matter present per unit area at a given moment ($\mathrm{g\,m^{-2}}$ or $\mathrm{t\,ha^{-1}}$). Production and biomass must not be confused: a phytoplankton community with a biomass of a few grams per square meter may produce several hundred grams per square meter per year, because its cells divide every day or two, whereas a forest with a biomass of 30 000 $\mathrm{g\,m^{-2}}$ produces about 1500 $\mathrm{g\,m^{-2}}$ per year. The ratio NPP:$B$ (per year) is a turnover rate, and its reciprocal $B/\mathrm{NPP}$ is the mean time a unit of biomass remains in the standing crop. NPP:$B$ averages about 0.04 for forests, 0.3 for other terrestrial vegetation and 17 for aquatic communities (Whittaker 1975; Begon and Townsend 2021). The low values of forests reflect the large proportion of biomass in wood, which is largely dead (heartwood) and does not photosynthesize; the high values of phytoplankton reflect the absence of support tissue and rapid turnover (a turnover time of days to weeks, against 1–20 years for land plants).

### 42.1.3. Net Ecosystem Production During Stand Development

The relation between NPP, decomposition and NEP can be made explicit with a two-pool model of a forest stand. Let $B(t)$ be the living biomass and $D(t)$ the dead organic matter (litter and soil carbon) per unit area. Biomass grows by NPP and loses a fraction $m$ per year as litter; dead matter receives the litter and is decomposed at a rate $k$ per year (the decomposition model of [7.19.44](/7.19.44#sec-44.5)):

$$
\begin{aligned}
\frac{\mathrm{d}B}{\mathrm{d}t} &= \mathrm{NPP}(t) - mB, \\
\frac{\mathrm{d}D}{\mathrm{d}t} &= mB - kD,
\end{aligned}
$$
with $R_{\mathrm{H}} = kD$, so that $\mathrm{NEP} = \mathrm{NPP} - kD = \mathrm{d}(B + D)/\mathrm{d}t$.

**Proposition 42.1.1** If NPP tends to a constant $N^*$, every solution tends to the equilibrium $B^* = N^*/m$, $D^* = N^*/k$, at which $\mathrm{NEP} = 0$. After a disturbance that kills the stand and leaves dead matter $D_0$, NEP is initially $\mathrm{NPP}(0) - kD_0$, which is negative if $D_0 > \mathrm{NPP}(0)/k$.

**Proof** The system is linear with constant input in the limit; its matrix $\begin{bmatrix} -m & 0 \\ m & -k \end{bmatrix}$ is triangular with eigenvalues $-m < 0$ and $-k < 0$, so the equilibrium is globally asymptotically stable. Setting the derivatives to zero gives $B^* = N^*/m$ and $D^* = mB^*/k = N^*/k$, so $R_{\mathrm{H}} = kD^* = N^*$ and NEP vanishes. The second statement follows from $\mathrm{NEP} = \mathrm{NPP} - kD$ at $t = 0$. $\square$

![Net ecosystem production in a pool model of forest stand development after a stand-replacing disturbance (Proposition 42.1.1; parameters: NPP = 1000 (1 − e^(−t/10)) g C m⁻² yr⁻¹ multiplied by an age factor that declines from 1 to 0.65; litter loss m = 0.03 yr⁻¹; decomposition k = 0.05 yr⁻¹; dead organic matter left by the disturbance D₀ = 8000 g C m⁻²). A: NPP, heterotrophic respiration and NEP; the stand is a carbon source for the first few years, while decomposers consume the dead matter and NPP is still low, then a strong sink for about a century; as NPP declines with stand age, NEP becomes slightly negative while the old stand loses some biomass, and it tends to zero at equilibrium. B: living biomass and dead organic matter; the dotted lines are the equilibria N*/m and N*/k](./plots/nep-stand-age.py)

The model explains three observations. Young and middle-aged forests are strong carbon sinks, whereas very old forests have NEP close to zero (though many old-growth forests still accumulate carbon slowly, because they never reach a true equilibrium); a recently disturbed site is a carbon source; and the equilibrium stores of carbon are proportional to the residence times $1/m$ and $1/k$, so that slow decomposition (cold, waterlogged soils) builds large stores of dead organic matter even at low NPP ([7.19.44](/7.19.44)). Odum (1969) made the ratio $P/R$, with $P$ = GPP, a key index of ecosystem development: greater than 1 in early succession, approaching 1 at maturity ([7.19.36](/7.19.36)).

## 42.2. Global Patterns

### 42.2.1. Primary Production of the Biomes

The global NPP of the Earth is about $105$–$110\,\mathrm{Pg\,C}$ per year, divided roughly equally between land (about 56–58) and oceans (about 49–51), and global GPP is about twice as large (Field et al. 1998; Begon and Townsend 2021). The classic compilation of Whittaker and Likens (1975) remains a useful picture of how this production is distributed:

| Ecosystem | Area / $10^6\,\mathrm{km^2}$ | Mean NPP / $\mathrm{g\,m^{-2}\,yr^{-1}}$ (dry matter) | Total NPP / $10^9\,\mathrm{t\,yr^{-1}}$ |
|---|---|---|---|
| Tropical rain forest | 17.0 | 2200 | 37.4 |
| Tropical seasonal forest | 7.5 | 1600 | 12.0 |
| Temperate evergreen forest | 5.0 | 1300 | 6.5 |
| Temperate deciduous forest | 7.0 | 1200 | 8.4 |
| Boreal forest | 12.0 | 800 | 9.6 |
| Woodland and shrubland | 8.5 | 700 | 6.0 |
| Savanna | 15.0 | 900 | 13.5 |
| Temperate grassland | 9.0 | 600 | 5.4 |
| Tundra and alpine | 8.0 | 140 | 1.1 |
| Desert and semidesert scrub | 18.0 | 90 | 1.6 |
| Extreme desert, rock, sand and ice | 24.0 | 3 | 0.07 |
| Cultivated land | 14.0 | 650 | 9.1 |
| Swamp and marsh | 2.0 | 2000 | 4.0 |
| Lake and stream | 2.0 | 250 | 0.5 |
| Open ocean | 332.0 | 125 | 41.5 |
| Upwelling zones | 0.4 | 500 | 0.2 |
| Continental shelf | 26.6 | 360 | 9.6 |
| Algal beds and reefs | 0.6 | 2500 | 1.6 |
| Estuaries | 1.4 | 1500 | 2.1 |

Several patterns stand out. Per unit area, the most productive ecosystems are algal beds and reefs, tropical rain forests, swamps and marshes, and estuaries; the least productive are deserts, tundra and the open ocean. Per unit area, the open ocean is about as unproductive as a desert scrub, yet because it covers two thirds of the Earth it accounts for about a third of global production. Tropical forests and savannas together account for about 60% of terrestrial NPP. On land, production declines from the equator to the poles, mainly because the growing season shortens; in the ocean the pattern is reversed, with higher production in the nutrient-rich waters of high latitudes and upwellings than in the subtropical gyres ([7.19.41](/7.19.41#sec-41.4.5)). Recent satellite-based estimates give a similar total with different details (for example, tropical forests about $16$–$23\,\mathrm{Pg\,C\,yr^{-1}}$ and savannas $15$–$19$; Begon and Townsend 2021).

### 42.2.2. Human Appropriation of Net Primary Production

Humans harvest crops, timber and grazing land and change the vegetation by land use. The human appropriation of net primary production (HANPP) is defined as the sum of the NPP harvested ($\mathrm{HANPP_{harv}}$, including crop residues and human-induced fire) and the NPP lost through land-use change ($\mathrm{HANPP_{luc}} = \mathrm{NPP_{pot}} - \mathrm{NPP_{act}}$, the difference between the potential NPP of natural vegetation and the actual NPP of the modified ecosystem; Haberl et al. 2007). Global HANPP rose from about $6.9\,\mathrm{Pg\,C\,yr^{-1}}$ in 1910 to $14.8\,\mathrm{Pg\,C\,yr^{-1}}$ in 2005, from 13% to 25% of potential terrestrial NPP, while the human population quadrupled; the efficiency of land use rose, but the share of terrestrial production available to all other species fell (Krausmann et al. 2013). HANPP is highest in densely populated agricultural regions (India, eastern China, Europe, the eastern United States), and it can be negative where irrigation and fertilizer raise actual NPP above the potential of a dry region. The use of biomass for energy would raise HANPP sharply ([7.19.54](/7.19.54)).

### 42.2.3. Primary Production in China

Satellite-based estimates put the mean terrestrial NPP of China at about $3\,\mathrm{Pg\,C}$ per year. Its distribution follows the gradients of heat and water ([7.19.41](/7.19.41#sec-41.2)): it is highest in the subtropical and tropical southeast (above $800\,\mathrm{g\,C\,m^{-2}\,yr^{-1}}$ in parts of Yunnan, Hainan and Taiwan), intermediate in the North China Plain and the Northeast, and very low over most of the area west of the Heihe–Tengchong line, where nearly half of the land produces less than $200\,\mathrm{g\,C\,m^{-2}\,yr^{-1}}$ (Zhou et al. 2021). Between 1982 and 2015 NPP increased over most of China, especially on the Loess Plateau and in the south, as a result of $\ce{CO2}$ fertilization, warming and, increasingly, afforestation and agricultural intensification: China and India account for about a third of the global greening observed by satellite since 2000, China mainly through forests (42%) and croplands (32%) (Chen et al. 2019).

The large carbon sink of Chinese forests owes much to their youth: most were planted or regenerated after the 1970s. As these forests age, their NPP and NEP are expected to decline (Proposition 42.1.1), and projections of forest age and NPP suggest that, without new planting or changed management, NPP will fall over most of the forested area by 2060–2100 and the forest carbon sink will weaken (Shang et al. 2023).

## 42.3. Measuring Primary Production

No method measures GPP or NPP directly over a whole ecosystem; each measures a component and relies on assumptions.

| Method | What it measures | Used in |
|---|---|---|
| Harvest | Increase in biomass, plus losses | Grasslands, crops, forests (with allometry) |
| Light–dark bottles | Change in dissolved $\ce{O2}$ | Plankton |
| Diel oxygen curve | Change in $\ce{O2}$ in open water | Streams, lakes, coral reefs |
| Gas exchange ($\ce{CO2}$) | Chambers or eddy covariance | Leaves, plants, whole ecosystems |
| ¹⁴C uptake | Carbon fixed in a sample | Plankton (ocean standard) |
| Chlorophyll and remote sensing | Pigment or light absorption, with a model | Regional and global scales |

### 42.3.1. The Harvest Method

On land, the vegetation of sample plots is clipped at intervals, dried to constant mass and weighed; the increase in biomass between harvests, corrected for parts lost to litter, death and herbivores, estimates NPP. Annual crops and grasslands with one growing season are simple: the peak biomass approximates above-ground NPP. In forests, trees are not harvested but measured, and their biomass is calculated from stem diameter and height with allometric equations fitted to felled trees; litterfall is collected in traps. Below-ground production is the largest source of error: roots may account for 40–85% of the total NPP of grasslands and a third or more in forests, and fine roots turn over within months, so that repeated coring, root windows (minirhizotrons) or isotope methods are needed. Converting dry mass to energy requires the energy content of the material, measured by bomb calorimetry.

### 42.3.2. The Light–Dark Bottle Method

In water, Gaarder and Gran (1927) measured plankton production by the oxygen it releases. Water samples from a given depth are filled into transparent (light) and opaque (dark) glass bottles; the initial oxygen concentration $c_{\mathrm{I}}$ is measured in a third bottle at once, and the light and dark bottles are incubated at the depth of sampling for a fixed time (usually 4–24 h), after which their oxygen concentrations $c_{\mathrm{L}}$ and $c_{\mathrm{D}}$ are measured (by Winkler titration or an oxygen electrode). In the dark bottle only respiration occurs, in the light bottle photosynthesis and respiration. Hence

$$
\begin{aligned}
\text{respiration} &= c_{\mathrm{I}} - c_{\mathrm{D}}, \\
\text{net production} &= c_{\mathrm{L}} - c_{\mathrm{I}}, \\
\text{gross production} &= c_{\mathrm{L}} - c_{\mathrm{D}},
\end{aligned}
$$
per volume of water and incubation time. Oxygen is converted to carbon by the stoichiometry of photosynthesis: 1 mol $\ce{O2}$ (32 g) corresponds to 1 mol C (12 g) if the photosynthetic quotient $\mathrm{PQ} = \Delta\ce{O2}/\Delta\ce{CO2}$ is 1, but phytoplankton using nitrate release more oxygen per carbon fixed (PQ about 1.2–1.4), so that

$$
\text{carbon fixed} = \frac{12}{32}\,\frac{\Delta c_{\ce{O2}}}{\mathrm{PQ}},
$$
and respiration is converted with the **respiratory quotient** (about 1).

**Example 42.3.1** Water from 1 m depth has $c_{\mathrm{I}} = 8.20\,\mathrm{mg\,O_2\,L^{-1}}$. After 12 h of daylight incubation, $c_{\mathrm{L}} = 9.50$ and $c_{\mathrm{D}} = 7.40\,\mathrm{mg\,O_2\,L^{-1}}$. Then respiration is $0.80$, net production $1.30$ and gross production $2.10\,\mathrm{mg\,O_2\,L^{-1}}$ in 12 h. With $\mathrm{PQ} = 1.2$, gross production is $2.10 \times 0.375/1.2 = 0.66\,\mathrm{mg\,C\,L^{-1}}$, that is $660\,\mathrm{mg\,C\,m^{-3}}$ in 12 h. If respiration continues at the same rate through the night, the community at this depth respires $1.60\,\mathrm{mg\,O_2\,L^{-1}}$ per day and fixes $2.10$, so its daily net production is $0.50\,\mathrm{mg\,O_2\,L^{-1}}$: the ratio $P/R$ of the sample is $2.10/1.60 \approx 1.3$. Repeating the measurement at several depths and integrating over depth gives the production of the water column per square meter.

![The oxygen methods for aquatic primary production. A: the light–dark bottle example (Example 42.3.1): oxygen in the initial, dark and light bottles, and the derived respiration, net production and gross production over a 12-hour incubation. B: the diel oxygen curve method in a simulated stream: dissolved oxygen (black) rises by day and falls by night; the rate of change, corrected for exchange with the atmosphere (reaeration coefficient 0.5 h⁻¹, saturation 9 mg L⁻¹), gives community metabolism (lower panel): at night it equals respiration (−0.25 mg L⁻¹ h⁻¹), which is extrapolated through the day (dashed), and the daytime excess over this line is gross primary production (green; 4.8 mg O₂ L⁻¹ d⁻¹ in the simulation, recovered from the curve).](./plots/oxygen-methods.py)

The method assumes that respiration is the same in light and dark, which is not quite true (light stimulates respiration and photorespiration, [7.13.8](/7.13.8)); bottles exclude grazers and turbulence and promote bacterial growth on the glass, so long incubations are biased; and in oligotrophic water the changes in oxygen are too small to measure, which is why the ¹⁴C method replaced it in the open ocean.

### 42.3.3. The Diel Oxygen Curve

In streams, shallow lakes and coral reefs, the whole community can be measured without bottles by recording dissolved oxygen in the open water over a day and night (H. T. Odum 1956). The oxygen concentration $c$ changes by production, respiration and exchange with the atmosphere:

$$
\frac{\mathrm{d}c}{\mathrm{d}t} = \mathrm{GPP}(t) - R + K\,(c_{\mathrm{sat}} - c),
$$
where $K$ is the reaeration coefficient and $c_{\mathrm{sat}}$ the saturation concentration. At night $\mathrm{GPP} = 0$, so the corrected rate of change gives $R$; assuming $R$ is constant over the day, GPP during the day is the corrected rate of change plus $R$, and daily GPP is the integral. The method integrates over the whole community and its habitat, but it requires an estimate of $K$ (from tracer gases or from the night-time data) and assumes constant respiration.

### 42.3.4. Carbon Dioxide Exchange and Eddy Covariance

On land, the uptake of $\ce{CO2}$ by leaves, whole plants or small plots is measured in enclosures: in a transparent chamber the decline of $\ce{CO2}$ gives net uptake, in a dark chamber respiration ([7.13.9](/7.13.9#sec-9.1)). The exchange of an entire ecosystem is measured by eddy covariance. Air moves over the canopy in turbulent eddies, and the net vertical flux of $\ce{CO2}$ through a plane above the canopy is the time average of the product of the fluctuations of vertical wind speed $w'$ and of $\ce{CO2}$ concentration $c'$,

$$
F = \overline{w'c'},
$$
measured ten or twenty times per second by a sonic anemometer and a fast gas analyser on a tower. $F$ is the net ecosystem exchange; summed over a year it gives NEP (with opposite sign). To separate it into GPP and $R_{\mathrm{E}}$, night-time fluxes (when $F = R_{\mathrm{E}}$) are fitted to a temperature function of respiration and extrapolated to the daytime; GPP is the difference. More than 1000 towers worldwide (the FLUXNET network, with ChinaFLUX) have shown how ecosystem exchange responds to light, temperature, drought and phenology, and provide the data used to calibrate satellite models.

### 42.3.5. Radioactive Carbon

Steemann Nielsen (1952) added a known amount of $^{14}\ce{C}$ as bicarbonate to a water sample, incubated it, filtered the phytoplankton and measured the radioactivity they had incorporated. Since the cells take up $^{14}\ce{C}$ in proportion to its share in the total dissolved inorganic carbon,

$$
\text{carbon fixed} = \frac{^{14}\mathrm{C}\ \text{in cells}}{^{14}\mathrm{C}\ \text{added}} \times C_{\mathrm{DIC}} \times 1.05,
$$
where $C_{\mathrm{DIC}}$ is the concentration of dissolved inorganic carbon and the factor 1.05 corrects for the slower uptake of the heavier isotope. The method is very sensitive and became the standard for oceanic production; a dark bottle corrects for non-photosynthetic uptake. Whether it measures GPP or NPP depends on the incubation time: in short incubations little of the labeled carbon is respired, so the result is close to GPP, in 24-hour incubations close to NPP.

### 42.3.6. Chlorophyll and Remote Sensing

Since the rate of photosynthesis per unit of chlorophyll at given light is fairly constant within a community, the chlorophyll content of a sample (extracted with acetone and measured by spectrophotometry or fluorescence) can be converted to production. The same principle allows production to be estimated from space. Green leaves absorb strongly in the red (chlorophyll a absorbs near 430 and 660 nm) and reflect strongly in the near infrared (700–1300 nm), where the internal structure of the leaf scatters light; soil and water reflect red and near-infrared light similarly. The normalized difference vegetation index,

$$
\mathrm{NDVI} = \frac{\rho_{\mathrm{NIR}} - \rho_{\mathrm{red}}}{\rho_{\mathrm{NIR}} + \rho_{\mathrm{red}}},
$$
where $\rho$ is the reflectance in each band, therefore ranges from below 0 for water, through about 0.1–0.2 for bare soil, to 0.6–0.9 for dense green vegetation.

![The principle of the normalized difference vegetation index (schematic reflectance spectra). Green vegetation absorbs red light (chlorophyll) and reflects near-infrared light strongly (leaf structure), producing the "red edge" near 700 nm; dry vegetation and soil have no red trough and moderate reflectance in both bands; water reflects little at all wavelengths, least in the near infrared. Shaded bands: red (630–690 nm) and near infrared (770–900 nm), as on Landsat; the NDVI of each surface computed from the mean reflectance in these bands is given in the legend.](./plots/ndvi-spectra.py)

The NDVI is roughly proportional to the fraction of photosynthetically active radiation absorbed by the canopy (fAPAR). Satellite estimates of production combine it with the **light-use efficiency** model of Monteith ([7.13.9](/7.13.9#sec-9.5)),

$$
\mathrm{GPP} = \varepsilon \times \mathrm{fAPAR} \times \mathrm{PAR},
$$
where PAR is the incident **photosynthetically active radiation** (about 45% of incoming shortwave radiation) and $\varepsilon$ is a conversion efficiency (grams of carbon per megajoule of absorbed PAR) reduced below its maximum by low temperature and high vapor pressure deficit. The MODIS GPP and NPP products are calculated in this way every eight days for the whole land surface. Ocean production is estimated similarly from the color of the sea, which gives surface chlorophyll, together with light and temperature. A newer signal is solar-induced chlorophyll fluorescence, a faint glow emitted by photosystem II, which tracks photosynthesis more directly than greenness.

## 42.4. The Efficiency of Primary Production

The efficiency of primary production is the fraction of incident solar energy fixed as GPP (or NPP). It is low. Of the solar radiation reaching the ground, only about 45% is photosynthetically active; part is reflected or transmitted, or falls on bare ground; the theoretical maximum quantum efficiency (eight to ten photons per $\ce{CO2}$ fixed) converts at most about a quarter of absorbed PAR energy into carbohydrate; and photorespiration, respiration and light saturation of the upper leaves take further shares. The theoretical upper limit of the conversion of total solar radiation into biomass is about 4.6% for C3 and 6% for C4 plants (Zhu, Long and Ort 2008; [7.13.9](/7.13.9#sec-9.5)).

Actual efficiencies are far lower. Under natural conditions the efficiency of GPP rarely exceeds 3% of incident solar radiation, although intensively managed crops have reached 6–8% over short periods; averaged over the globe and the year, the efficiency of NPP is about 0.2–0.5%, because most of the land is limited by water, cold or nutrients and most of the ocean by nutrients. In the forests and deserts of the International Biological Programme, coniferous forests converted 1–3% of PAR into above-ground NPP, deciduous forests 0.5–1% and deserts 0.01–0.2% (Webb et al. 1983). These numbers show that solar radiation is rarely the factor that limits production: efficiencies are low precisely where other factors limit, and the same radiation is used much more efficiently when water and nutrients are supplied, as in irrigated, fertilized agriculture. The low efficiency of deserts is mainly a consequence of sparse cover: per unit of leaf mass, desert plants are as productive as forest trees.

## 42.5. Factors Limiting Primary Production

### 42.5.1. Terrestrial Ecosystems

On land, the main limiting factors are water and temperature, then the length of the growing season and the supply of nutrients. Lieth (1975) captured the first two in the Miami model, fitted to NPP data from about 50 sites. Production limited by temperature alone and by precipitation alone are modeled by

$$
\begin{aligned}
\mathrm{NPP}_T &= \frac{3000}{1 + \mathrm{e}^{1.315 - 0.119\,T}}, \\
\mathrm{NPP}_P &= 3000\left(1 - \mathrm{e}^{-0.000664\,P}\right),
\end{aligned}
$$
in $\mathrm{g}$ dry matter $\mathrm{m^{-2}\,yr^{-1}}$, with the mean annual temperature $T$ in °C and the annual precipitation $P$ in mm. The temperature function is logistic, rising from near zero in cold climates to an upper limit of 3000; the precipitation function rises linearly at low $P$ (the initial slope is about $2\,\mathrm{g}$ dry matter per mm of rain) and saturates at high $P$. Following **Liebig's law of the minimum**, the predicted NPP is the smaller of the two:

$$
\mathrm{NPP} = \min\{\mathrm{NPP}_T, \mathrm{NPP}_P\}.
$$

**Proposition 42.5.1** For each temperature $T$ there is a unique precipitation $P^*(T) = -\ln\left(1 - (1 + \mathrm{e}^{1.315 - 0.119T})^{-1}\right)/0.000664$ above which production in the Miami model is temperature-limited and below which it is water-limited. $P^*(T)$ is increasing in $T$: warmer climates need more rain before temperature becomes limiting.

**Proof** $\mathrm{NPP}_P$ is strictly increasing in $P$ from 0 to 3000, and $0 < \mathrm{NPP}_T < 3000$, so the equation $\mathrm{NPP}_P(P) = \mathrm{NPP}_T(T)$ has the unique solution obtained by solving $1 - \mathrm{e}^{-0.000664P} = (1 + \mathrm{e}^{1.315 - 0.119T})^{-1}$ for $P$. For $P < P^*$ the precipitation term is the smaller, for $P > P^*$ the temperature term. Since $\mathrm{NPP}_T$ increases with $T$, the right-hand side increases with $T$, and so does $P^*$. $\square$

For example, at $T = 15\,^\circ\mathrm{C}$, $\mathrm{NPP}_T = 3000/(1 + \mathrm{e}^{-0.47}) = 1846$, and $P^* = -\ln(1 - 0.615)/0.000664 = 1438\,\mathrm{mm}$. For Beijing ($T \approx 12.9\,^\circ\mathrm{C}$, $P \approx 570\,\mathrm{mm}$) the model gives $\mathrm{NPP}_T = 1665$ and $\mathrm{NPP}_P = 945$, so production is water-limited at about $950\,\mathrm{g\,m^{-2}\,yr^{-1}}$; for Guangzhou ($22.6\,^\circ\mathrm{C}$, $1830\,\mathrm{mm}$), $\mathrm{NPP}_T = 2394$ and $\mathrm{NPP}_P = 2108$, about $2100$.

![The Miami model of terrestrial net primary production (Lieth 1975). A: production limited by mean annual temperature (red) and by annual precipitation (blue; upper axis). B: predicted NPP, the minimum of the two, as a function of temperature and precipitation; the dashed line is the boundary P*(T) of Proposition 42.5.1, above which temperature limits and below which water limits; dots: the five Chinese cities of the Whittaker diagram in 7.19.41. C: the Rosenzweig (1968) relation between NPP and actual evapotranspiration, log₁₀ NPP = 1.66 log₁₀ AET − 1.66, which combines the effects of heat and water in a single variable.](./plots/miami-model.py)

The Miami model is purely empirical and treats temperature and water as independent, whereas in reality they interact: higher temperature increases evaporative demand, so the same rainfall supports less production in a warmer climate. Rosenzweig (1968) used instead the actual evapotranspiration (AET), the amount of water that actually evaporates and transpires from a landscape in a year, which is high only where both water and energy are abundant:

$$
\log_{10}\mathrm{NPP} = 1.66\log_{10}\mathrm{AET} - 1.66,
$$
with NPP in $\mathrm{g\,m^{-2}\,yr^{-1}}$ (above-ground) and AET in mm. AET of 300 mm gives about $280$, of 1000 mm about $2100\,\mathrm{g\,m^{-2}\,yr^{-1}}$. Within a single biome the dependence on precipitation is often almost linear: across 100 grassland regions of the central United States, above-ground NPP increased from about 100 to 700 $\mathrm{g\,m^{-2}\,yr^{-1}}$ with precipitation from 200 to 1200 mm, $\mathrm{ANPP} \approx 0.6\,P - 34$ (Sala et al. 1988), and adding temperature did not improve the prediction. Along elevation gradients the relation with temperature is often hump-shaped, because warming lengthens the growing season at the cold end but increases evapotranspiration and water stress at the warm end (Jobbágy et al. 2002).

Three further factors modify these climatic limits:

- The length of the growing season accounts for much of the latitudinal decline of forest production: deciduous trees photosynthesize rapidly for a short season, evergreens slowly for a long one, and the number of days with active photosynthesis largely explains the difference between temperate and boreal forests.
- Soil texture and drainage alter the water available from a given rainfall: forests on sandy soils, which hold little water and lose nutrients by leaching, accumulate biomass more slowly than on finer soils.
- Nutrients set limits within the climatic envelope. Nitrogen limits production in most temperate and boreal forests and grasslands, in tundra and in deserts after rain, while phosphorus limits many tropical forests and savannas on old, weathered soils from which most phosphorus has been lost or bound in unavailable forms (Wang et al. 2010); nitrogen fertilization almost always increases production in temperate forests and fertilization of Alaskan tundra raised NPP by 23–300% (Shaver and Chapin 1986). Rising atmospheric $\ce{CO2}$ increases NPP by about 14–31% in enrichment experiments with C3 plants, but the response is often limited by nutrients.

### 42.5.2. Aquatic Ecosystems

In water, the limiting factors are light and nutrients. Light declines exponentially with depth ([7.19.3](/7.19.3#sec-3.4.3)), so that photosynthesis per unit volume falls with depth (often with **photoinhibition** at the surface on bright days), while respiration of the phytoplankton is roughly independent of depth. The depth at which gross photosynthesis just balances respiration is the compensation depth; it defines the base of the euphotic zone, above which net production is positive. The more nutrient-rich a lake, the more phytoplankton it contains, the more light they absorb, and the shallower its euphotic zone: production per square meter increases with fertility, but it is concentrated in a thinner layer.

In a mixed water column, phytoplankton cells are carried up and down by turbulence, and what matters is not the light at a fixed depth but the average light over the mixed layer. Sverdrup (1953) turned this observation into the first quantitative theory of the spring bloom.

**Proposition 42.5.2 (Sverdrup's Critical Depth)** Suppose that phytoplankton are uniformly mixed to the depth $D$ (the mixed layer depth), that light decreases as $I(z) = I_0\,\mathrm{e}^{-Kz}$, that gross photosynthesis per unit biomass is proportional to light, $aI(z)$, and that losses (respiration, and in later versions grazing and sinking) per unit biomass are a constant $r$ at all depths. Let $I_{\mathrm{c}} = r/a$ be the compensation irradiance. The population in the mixed layer grows if and only if

$$
\frac{D}{1 - \mathrm{e}^{-KD}} < \frac{I_0}{KI_{\mathrm{c}}}.
$$
If $I_0 > I_{\mathrm{c}}$, there is a unique critical depth $D_{\mathrm{cr}} > 0$ at which equality holds; the population grows when $D < D_{\mathrm{cr}}$ and declines when $D > D_{\mathrm{cr}}$. For $KD_{\mathrm{cr}} \gg 1$, $D_{\mathrm{cr}} \approx I_0/(KI_{\mathrm{c}})$.

**Proof** With biomass $B$ per unit volume uniform over the mixed layer, the depth-integrated photosynthesis is $\int_0^D aBI_0\mathrm{e}^{-Kz}\,\mathrm{d}z = aBI_0(1 - \mathrm{e}^{-KD})/K$, and the integrated losses are $rBD$. Net growth is positive iff $aI_0(1 - \mathrm{e}^{-KD})/K > rD$, which, after dividing by $a(1 - \mathrm{e}^{-KD})$ and using $r/a = I_{\mathrm{c}}$, is the stated inequality. The function $f(D) = D/(1 - \mathrm{e}^{-KD})$ is continuous and strictly increasing on $(0, \infty)$, with $f(D) \to 1/K$ as $D \to 0$ and $f(D) \to \infty$ as $D \to \infty$ (its derivative is $(1 - \mathrm{e}^{-KD} - KD\mathrm{e}^{-KD})/(1 - \mathrm{e}^{-KD})^2 > 0$, because $\mathrm{e}^{x} > 1 + x$ for $x > 0$). Hence $f(D) = I_0/(KI_{\mathrm{c}})$ has a unique solution iff $I_0/(KI_{\mathrm{c}}) > 1/K$, that is $I_0 > I_{\mathrm{c}}$, and $f(D) < I_0/(KI_{\mathrm{c}})$ exactly for $D < D_{\mathrm{cr}}$. When $KD \gg 1$, $\mathrm{e}^{-KD} \approx 0$ and $D_{\mathrm{cr}} \approx I_0/(KI_{\mathrm{c}})$. $\square$

The critical depth is always deeper than the compensation depth $z_{\mathrm{c}} = \ln(I_0/I_{\mathrm{c}})/K$: cells mixed below the compensation depth lose carbon there but gain it near the surface, and the population as a whole grows as long as the gains over the mixed layer exceed the losses. In winter at temperate and high latitudes, surface light $I_0$ is low and storms mix the water deeply, so $D > D_{\mathrm{cr}}$ and phytoplankton cannot grow, although nutrients are abundant; in spring, light increases ($D_{\mathrm{cr}}$ deepens) and warming stratifies the surface water ($D$ becomes shallower), and when $D$ falls below $D_{\mathrm{cr}}$ the spring bloom begins. The bloom then depletes the nutrients of the shallow mixed layer, and production in summer is nutrient-limited until autumn mixing returns nutrients to the surface, sometimes producing a smaller autumn bloom.

![Sverdrup's critical depth (Proposition 42.5.2). A: the criterion: depth-integrated gross photosynthesis (green) and losses (red line) for a mixed layer of depth D, with K = 0.1 m⁻¹, I₀ = 20 and I_c = 1.3 mol photons m⁻² d⁻¹; the compensation depth is where photosynthesis per unit volume equals losses, the critical depth where the integrated curves cross. B: a seasonal cycle at about 50° N (schematic): daily surface PAR rises from 5 in winter to 45 mol photons m⁻² d⁻¹ in summer, so the critical depth deepens from about 40 m to more than 300 m, while the mixed layer shoals from 250 m in winter to 25 m in summer; the bloom becomes possible (shaded) when the mixed layer becomes shallower than the critical depth, in early spring.](./plots/sverdrup.py)

The critical depth hypothesis explains why blooms begin in spring and why they begin earlier in sheltered, stratified waters, and it is still used, but it has been qualified. Blooms sometimes begin in winter in deep mixed layers, because deep mixing also dilutes the grazers and lowers grazing more than it lowers phytoplankton growth (the dilution–recoupling hypothesis; Behrenfeld 2010), and in a weakly turbulent mixed layer the relevant depth is that of active mixing rather than of the density profile.

Once light is sufficient, nutrients limit. In lakes, phosphorus is usually the limiting element: gross production of the phytoplankton of Canadian lakes increased more than threefold with total phosphorus (Carignan et al. 2000), and whole-lake experiments demonstrated that phosphorus alone causes **eutrophication** ([7.11.30](/7.11.30#sec-30.3.3)). Aquatic production is generally more nutrient-sensitive than terrestrial production, which nitrogen or phosphorus deficiency reduces by perhaps 20–40%. In the ocean, nitrogen and phosphorus are both scarce in the surface water of the subtropical gyres and occur in about the **Redfield ratio** of 16:1 ([7.19.6](/7.19.6#sec-6.4.1)), so both limit; high production occurs where nutrients are supplied by rivers, by coastal and equatorial upwelling, or by winter mixing. In about a third of the open ocean, the high-nutrient, low-chlorophyll regions of the Southern Ocean and the subarctic and equatorial Pacific, nitrate remains unused because the phytoplankton are limited by iron, which reaches the ocean mainly as wind-blown dust; experimental iron additions in these regions caused large blooms (Boyd et al. 2007). Over the ocean as a whole, NPP correlates with sea surface temperature and PAR as well, which helps satellite estimation.

## 42.6. Consumers and Primary Production

Herbivores remove only a small fraction of NPP in most terrestrial ecosystems, but their effect on production can be larger than their consumption suggests, and of either sign. In the Serengeti, McNaughton (1979, 1985) found that moderate grazing by wildebeest and other ungulates increased above-ground NPP compared with fenced plots, because grazed grasses regrow from basal meristems, the removal of old tissue improves the light environment of young leaves, and dung and urine return nitrogen in an available form (the grazing optimization hypothesis). Heavy grazing, by contrast, reduces production and, in dry grasslands, leads to degradation ([7.19.24](/7.19.24)). In lakes, predators control primary production from the top of the food chain: adding piscivorous fish reduces planktivorous fish, which releases large herbivorous zooplankton such as *Daphnia*, which graze down the phytoplankton, so that primary production and chlorophyll fall (Carpenter et al. 1985). This is a **trophic cascade**, and it shows that primary production is controlled not only from below, by resources, but also from above, by consumers ([7.19.39](/7.19.39)).

## Summary

- Primary production: $\mathrm{NPP} = \mathrm{GPP} - R_{\mathrm{A}}$; ecosystem respiration $R_{\mathrm{E}} = R_{\mathrm{A}} + R_{\mathrm{H}}$; net ecosystem production $\mathrm{NEP} = \mathrm{GPP} - R_{\mathrm{E}} = \mathrm{NPP} - R_{\mathrm{H}}$ (Definition 42.1.1) decides whether an ecosystem is a carbon sink or source. In a two-pool model NEP is negative after disturbance, positive in young stands and tends to zero at equilibrium (Proposition 42.1.1).
- Production (a rate) differs from biomass (a stock); NPP:$B$ is about 0.04 per year in forests and about 17 in aquatic communities.
- Global NPP is about $105\,\mathrm{Pg\,C\,yr^{-1}}$, half on land and half in the ocean; the most productive ecosystems per area are reefs and algal beds, tropical rain forests, marshes and estuaries; the open ocean is as unproductive per area as desert scrub. Humans appropriate about a quarter of potential terrestrial NPP. In China NPP falls from the southeast to the northwest, has increased since the 1980s, and the carbon sink of young forests will weaken as they age.
- Methods: harvest; light–dark bottles (R = $c_{\mathrm{I}} - c_{\mathrm{D}}$, NP = $c_{\mathrm{L}} - c_{\mathrm{I}}$, GP = $c_{\mathrm{L}} - c_{\mathrm{D}}$; Example 42.3.1); diel oxygen curves; chambers and eddy covariance ($F = \overline{w'c'}$); ¹⁴C uptake; chlorophyll, NDVI and the light-use efficiency model $\mathrm{GPP} = \varepsilon \cdot \mathrm{fAPAR} \cdot \mathrm{PAR}$.
- Efficiency: GPP rarely exceeds 3% of incident radiation; global NPP efficiency is about 0.2–0.5%; the theoretical maximum is about 4.6% (C3) and 6% (C4).
- Limits on land: water and temperature (Miami model $\mathrm{NPP} = \min\{\mathrm{NPP}_T, \mathrm{NPP}_P\}$, Proposition 42.5.1; Rosenzweig's AET relation), growing season, soil texture, nitrogen and phosphorus. Limits in water: light (compensation depth; Sverdrup's critical depth, Proposition 42.5.2, explains the spring bloom), nitrogen, phosphorus and iron, relieved by upwelling and mixing.
- Consumers modify production: moderate grazing can increase it, and trophic cascades control it from above.

## Questions

1. A forest has GPP $= 2000$, $R_{\mathrm{A}} = 1100$ and $R_{\mathrm{H}} = 800\,\mathrm{g\,C\,m^{-2}\,yr^{-1}}$. Calculate NPP, $R_{\mathrm{E}}$ and NEP. A stream draining the same catchment has GPP $= 200$ and $R_{\mathrm{E}} = 600\,\mathrm{g\,C\,m^{-2}\,yr^{-1}}$. How can its NEP be negative year after year?

   **Answer** NPP $= 2000 - 1100 = 900$, $R_{\mathrm{E}} = 1100 + 800 = 1900$ and NEP $= 2000 - 1900 = 100\,\mathrm{g\,C\,m^{-2}\,yr^{-1}}$ (equivalently NPP $- R_{\mathrm{H}} = 900 - 800$): the forest is a small sink. The stream has NEP $= 200 - 600 = -400$. It can sustain this indefinitely because it is not a closed system: its heterotrophs respire allochthonous organic matter (leaf litter, dissolved organic carbon) imported from the forest, part of the forest's NEP. Taking stream and forest together, the carbon balance must include this transfer.

2. In a light–dark bottle experiment the initial bottle contains $7.6\,\mathrm{mg\,O_2\,L^{-1}}$; after 6 h the light bottle contains $8.5$ and the dark bottle $7.3$. Calculate gross and net production and respiration in carbon units (PQ $= 1.25$, RQ $= 1.0$), and state two reasons why the gross production may be underestimated.

   **Answer** Respiration $= 7.6 - 7.3 = 0.3$, net production $= 8.5 - 7.6 = 0.9$ and gross production $= 8.5 - 7.3 = 1.2\,\mathrm{mg\,O_2\,L^{-1}}$ in 6 h. In carbon: gross $= 1.2 \times 0.375/1.25 = 0.36$, net $= 0.9 \times 0.375/1.25 = 0.27$ and respiration $= 0.3 \times 0.375 = 0.11\,\mathrm{mg\,C\,L^{-1}}$ (the net value is approximate because the two quotients differ). Gross production is underestimated if respiration in the light exceeds that in the dark (light-enhanced respiration, photorespiration), since the dark bottle then underestimates the respiration occurring in the light bottle; and if the bottle reduces the activity of the community (no turbulence, nutrient depletion during incubation). It can be overestimated if bacteria grow on the walls of the dark bottle more than in nature, inflating respiration.

3. Using the Miami model, compute the predicted NPP for (a) $T = 26\,^\circ\mathrm{C}$, $P = 2500\,\mathrm{mm}$ and (b) $T = -8\,^\circ\mathrm{C}$, $P = 300\,\mathrm{mm}$, and say which factor limits. Why does the model fail for a site at $T = 25\,^\circ\mathrm{C}$ with $P = 2500\,\mathrm{mm}$ falling almost entirely in two months?

   **Answer** (a) $\mathrm{NPP}_T = 3000/(1 + \mathrm{e}^{1.315 - 3.094}) = 3000/1.169 = 2567$; $\mathrm{NPP}_P = 3000(1 - \mathrm{e}^{-1.66}) = 3000 \times 0.810 = 2430$; NPP $\approx 2430\,\mathrm{g\,m^{-2}\,yr^{-1}}$, water-limited (barely). (b) $\mathrm{NPP}_T = 3000/(1 + \mathrm{e}^{2.267}) = 3000/10.65 = 282$; $\mathrm{NPP}_P = 3000(1 - \mathrm{e}^{-0.199}) = 542$; NPP $\approx 280$, temperature-limited. In the monsoonal site most rain falls in two months, runs off or drains below the roots, and the rest of the year is dry: the annual total overstates the water available during most of the growing season. The model uses annual means and ignores seasonality, soil water storage and the interaction between temperature and evaporation, which AET-based and process-based models take into account.

4. For a mixed layer with $K = 0.08\,\mathrm{m^{-1}}$ and $I_{\mathrm{c}} = 1.5\,\mathrm{mol\,photons\,m^{-2}\,d^{-1}}$, estimate the critical depth when $I_0 = 6$ (late winter) and $I_0 = 30$ (late spring). The winter mixed layer is 150 m deep. Will a bloom occur in late winter? Compare the critical depth with the compensation depth in late spring.

   **Answer** With the approximation $D_{\mathrm{cr}} \approx I_0/(KI_{\mathrm{c}})$: late winter $6/(0.08 \times 1.5) = 50\,\mathrm{m}$ (the exact root of $D/(1 - \mathrm{e}^{-KD}) = 50$ is about 49 m, since $\mathrm{e}^{-4} \approx 0.02$), late spring $30/0.12 = 250\,\mathrm{m}$. In late winter the mixed layer (150 m) is deeper than $D_{\mathrm{cr}}$ (50 m), so in Sverdrup's model no bloom occurs. In late spring the compensation depth is $z_{\mathrm{c}} = \ln(30/1.5)/0.08 = \ln 20/0.08 \approx 37\,\mathrm{m}$, much shallower than the critical depth of 250 m: phytoplankton mixed down to 250 m spend most of their time below the compensation depth but still achieve positive net growth over the layer as a whole.

5. (Open question) A province plans to raise its forest carbon sink by planting forests on grassland in a semi-arid region (annual precipitation 350 mm). Use the concepts of this chapter to discuss whether this is a good idea.

   **Answer** Points to consider: (a) climatically, 350 mm lies near the dry limit of forest (Miami model: $\mathrm{NPP}_P \approx 620$; the zonal vegetation is steppe), so trees may grow poorly, die in droughts, or survive only with irrigation; (b) trees transpire more than grass and can deplete deep soil water, as on parts of the Loess Plateau, reducing streamflow and leaving "small old trees"; (c) the carbon balance must include the whole ecosystem: grasslands store most of their carbon below ground, and site preparation can release soil carbon, so NEP may be negative for years (Proposition 42.1.1), and the net gain depends on the difference from the grassland's own NEP; (d) albedo: darker forest canopies absorb more radiation, partly offsetting the climate benefit in dry, bright regions; (e) biodiversity and grazing livelihoods of the steppe would be lost. Better options may be restoring degraded grassland (raising its soil carbon), planting in moister sites, and protecting existing forests. A defensible answer weighs water, carbon, energy balance and biodiversity rather than counting tree biomass alone.
