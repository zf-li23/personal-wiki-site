---
title: Resources, Stoichiometry and the Metabolic Theory of Ecology
description: "Conditions and resources; Tilman's classification of resources by their growth isoclines (essential, perfectly substitutable, complementary, antagonistic, inhibitory) and the resource dimensions of the niche; radiation, water, mineral nutrients and oxygen as resources, depletion zones of nitrate and phosphate; organisms as food: C:N ratios of plants and animals, plant parts, digestion; ecological stoichiometry: the Redfield ratio, stoichiometric homeostasis, the threshold elemental ratio and consumer-driven nutrient recycling, the growth rate hypothesis; body size and allometry: the mouse–elephant curve, lifespan, generation time and r_max; the metabolic theory of ecology: the central equation, derivations of the 2/3 and 3/4 exponents (surface argument, West–Brown–Enquist network, supply-network argument), the Boltzmann–Arrhenius factor, the ontogenetic growth model, scaling of development, r_max, mortality and population density, the energy equivalence rule, and the controversies."
---

An organism's environment consists of conditions, which it tolerates, and resources, which it consumes. The previous chapters dealt mainly with conditions (temperature, salinity, pH) and with water and soil, which are both; this chapter is about resources and about the rate at which organisms use them. It has three parts. The first classifies resources and describes the resources of plants (radiation, CO₂, water, mineral nutrients) and of animals (other organisms). The second, ecological stoichiometry, treats organisms as packages of chemical elements and asks what follows from the fact that consumers and their food differ in elemental composition. The third, the metabolic theory of ecology, treats metabolic rate as the rate at which an organism takes up and transforms resources, and derives from its dependence on body size and temperature quantitative predictions for growth, life history, population growth and abundance. The physiology of photosynthesis and mineral nutrition is in plant physiology ([7.13.4](/7.13.4), [7.13.8](/7.13.8), [7.13.9](/7.13.9)), the measurement of metabolic rate and Kleiber's law in animal physiology ([7.14.30](/7.14.30#sec-30.3)); here we build on them. The classification of resources prepares the theory of resource competition ([7.19.23](/7.19.23)); stoichiometry returns in the cycling of elements in ecosystems ([7.19.46](/7.19.46)); and metabolic theory is used to explain patterns of diversity ([7.19.35](/7.19.35)).

## 6.1. Conditions and Resources

### 6.1.1. Two Kinds of Environmental Factor

The ecological factors of [7.19.2](/7.19.2) fall into two kinds that act on organisms in different ways (Begon and Townsend 2021, following Tilman 1982).

**Definition 6.1.1 (Conditions and Resources)** An abiotic environmental factor that varies in space and time, to which organisms respond, but which is not used up by them, is called a **condition** (temperature, humidity, pH, salinity, current speed). Anything that is consumed by an organism, in the sense that its quantity or availability to other organisms is reduced by the organism's activity, is called a **resource** (light, CO₂, water, mineral nutrients, oxygen, food, nest sites, mates).

"Consumed" does not mean "eaten": a hole occupied by a nesting bird is no longer available to another bird, and a female that has mated may be unavailable to other males. The distinction matters because only resources can be competed for ([7.19.11](/7.19.11), [7.19.22](/7.19.22)). Some factors are both: water is a resource for a plant and a condition for a fish. Conditions alter the rates at which resources are used (temperature sets the rate of photosynthesis, Section 6.6.3), and they define the limits within which a species can persist; resources define the amounts available for growth and reproduction.

The primary division among consumers follows the type of resource. **Autotrophs** assimilate inorganic resources into organic matter: photoautotrophs (plants, algae, cyanobacteria) use radiation, CO₂, water and mineral nutrients; chemoautotrophs (some bacteria and archaea of hydrothermal vents, sediments and soils) use the energy of oxidizing inorganic compounds such as H₂S, NH₃ or Fe²⁺. **Heterotrophs** use organic matter made by others: predators, grazers and parasites eat living organisms, saprotrophs (decomposers and detritivores) dead ones ([7.19.44](/7.19.44)).

### 6.1.2. Classification of Resources

Every plant needs many resources, each taken up independently and by different mechanisms: no amount of nitrogen replaces phosphorus. A carnivore, by contrast, can replace one prey species by another of similar size. Tilman (1982) turned this contrast into a classification of resources taken in pairs, based on how the growth rate of a consumer depends on their two amounts $R_1$ and $R_2$. Let $g(R_1, R_2)$ be the per-capita growth rate of a population (or individual growth) in an environment with these amounts. A *growth isocline* is a curve in the $(R_1, R_2)$ plane along which $g$ is constant; the isocline $g = 0$ is the **zero net growth isocline**, which separates the resource combinations on which the population can increase from those on which it declines.

| Type | Definition | Shape of isoclines | Example of $g$ | Example |
|---|---|---|---|---|
| Essential | Neither resource can replace the other | Right angles parallel to both axes | $\min\{f_1(R_1), f_2(R_2)\} - m$ | Nitrogen and phosphorus for a plant; two hosts of a parasite that must alternate between them |
| Perfectly substitutable | Either can wholly replace the other | Straight lines | $f(w_1R_1 + w_2R_2) - m$ | Wheat and barley for a chicken, zebra and gazelle for a lion |
| Complementary | Substitutable, but less of both is needed together than either alone | Bowed towards the origin | $f(R_1 + R_2 + c\sqrt{R_1R_2}) - m$, $c > 0$ | Beans (rich in lysine) and rice (rich in sulfur amino acids) for a vegetarian |
| Antagonistic | Substitutable, but more of both is needed together | Bowed away from the origin | as above with $c < 0$ | Seeds containing different toxins that act synergistically (Janzen et al. 1977) |
| Inhibitory | Essential but harmful in excess | Closed curves | $\min\{h_1(R_1), h_2(R_2)\} - m$, $h$ unimodal | Light, CO₂, water, iron: needed, but toxic at high levels |

Here $f(R) = \mu_{\max}R/(K + R)$ is a saturating (Monod) uptake function, $m$ the mortality or maintenance rate and $w_i$ the value of resource $i$ relative to the other. For essential resources the growth rate is set by the resource in shortest supply relative to need, which is the **law of the minimum** of Liebig ([7.13.4](/7.13.4)); the zero isocline is then the right angle through $(R_1^*, R_2^*)$, where $R_i^* = Km/(\mu_{\max} - m)$ solves $f_i(R_i) = m$. This minimal resource level, below which the population cannot persist, will be the basis of the **R* rule** of resource competition ([7.19.23](/7.19.23)).

![Resource-dependent growth isoclines (after Tilman 1982). In each panel the thick line is the zero net growth isocline; dashed and dotted lines join resource combinations giving the same negative and positive growth rates, and the shaded region is where the population grows. (a) Essential resources: growth is set by the scarcer resource, and the isoclines are right angles. (b) Perfectly substitutable resources: straight isoclines, with resource 2 worth half as much as resource 1. (c) Complementary resources: isoclines bowed towards the origin, so a mixed diet needs less in total. (d) Antagonistic resources: isoclines bowed away from the origin. (e) Inhibitory resources: essential but toxic in excess, so the isoclines are closed curves. Growth functions are given in the table.](./plots/resource-isoclines.py)

The zero isocline of each pair of resources is a boundary of the **ecological niche** ([7.10.15](/7.10.15)) in those two dimensions. Together with the tolerance ranges of conditions ([7.19.2](/7.19.2)), these boundaries define Hutchinson's niche as an $n$-dimensional hypervolume within which the population can maintain itself. Some resource dimensions are not continuous axes: the larval food plants of a butterfly (*Heliconius* on *Passiflora*, the monarch on milkweeds) or the nest sites of a hole-nesting bird are better described as lists of suitable items.

## 6.2. The Resources of Plants

### 6.2.1. Radiation, CO₂ and Water

Solar radiation is the only energy source of green plants, but it is a resource that cannot be stored: radiation not intercepted when it arrives is lost forever. Photosynthetically active radiation (400–700 nm) makes up about 45% of the solar spectrum at the ground. The response of photosynthesis to light (light compensation and saturation points, sun and shade leaves), its distribution in the canopy and the leaf area index are treated in [7.13.9](/7.13.9) and [7.19.3](/7.19.3); the ecological point is that radiation is unevenly distributed in space (the canopy shades the understory, creating resource depletion zones beneath every leaf) and in time (sunflecks, seasons), and that plants are adapted either to exploit it at high intensity or to tolerate shade.

CO₂ reaches the chloroplasts by diffusion through the stomata, so its uptake is inseparable from the loss of water ([7.19.5](/7.19.5#sec-5.1.3)). Its concentration in the air is nearly uniform (420 ppm in 2024) but varies near the ground and in dense canopies, where it falls by day and rises by night. The three photosynthetic pathways differ in how they cope with the low CO₂ and high O₂ of the modern atmosphere: **C3 plants** fix CO₂ directly with Rubisco, which also reacts with O₂ (photorespiration), especially at high temperature; **C4 plants** concentrate CO₂ in the bundle sheath, which suppresses photorespiration and raises the optimum temperature and the water-use efficiency; **CAM plants** fix CO₂ at night and close their stomata by day ([7.13.8](/7.13.8)). C4 grasses dominate tropical savannas and warm grasslands, CAM plants deserts and epiphytic habitats, and the rising atmospheric CO₂ is expected to favor C3 plants, other things being equal.

### 6.2.2. Mineral Nutrients and Depletion Zones

Besides C, H and O, plants need the macronutrients N, P, K, S, Ca and Mg and the micronutrients Fe, Mn, Zn, Cu, B, Mo, Cl and Ni; some groups need others (Si for diatoms and grasses, Co for nitrogen-fixing symbioses, Na for some C4 and CAM plants). Each element is taken up separately as an ion, and each moves through soil in its own way, which determines how roots must forage for it. A root takes up ions at its surface and creates a depletion zone around itself, into which ions diffuse from the surrounding soil. A diffusing substance spreads over a distance of the order of $\sqrt{Dt}$ in time $t$ ([2.5.7](/2.5.7)), so the width of the depletion zone depends on the effective diffusion coefficient $D$ of the ion in soil.

**Example 6.2.1** In moist soil the effective diffusion coefficient of nitrate is about $10^{-10}\,\mathrm{m^2\,s^{-1}}$, that of phosphate, which is strongly adsorbed on soil particles, about $10^{-13}\,\mathrm{m^2\,s^{-1}}$. Estimate the width of the depletion zone that develops around a root in one day and discuss the consequences.

**Solution** With $t = 8.64\times10^4\,\mathrm{s}$, $\sqrt{Dt} \approx 3\times10^{-3}\,\mathrm{m} = 3\,\mathrm{mm}$ for nitrate and $\sqrt{Dt} \approx 9\times10^{-5}\,\mathrm{m} \approx 0.1\,\mathrm{mm}$ for phosphate. Roots a few millimeters apart therefore draw on the same nitrate (their depletion zones overlap and neighboring roots, of the same or different plants, compete for nitrate), and nitrate is best exploited by an extensive, not very finely branched root system; nitrate is also mobile with soil water and easily leached. Phosphate is taken up only from the immediate surroundings of the root, so plants must explore the soil intensively, with fine roots and long root hairs. This is why **mycorrhizae**, whose hyphae extend up to 100 times farther than root hairs, matter most for phosphate, and why plants of extremely phosphorus-poor soils (the Proteaceae of Western Australia and South Africa) form cluster roots that release carboxylates to mobilize bound phosphate.

:::

Nitrogen is required in greater amounts than any other mineral element and most often limits plant production on land, phosphorus in many freshwater and tropical ecosystems, and iron in parts of the open ocean ([7.19.46](/7.19.46)). Many plants overcome nitrogen shortage through symbioses with nitrogen-fixing bacteria (legumes with rhizobia, alders with *Frankia*), and most rely on mycorrhizal fungi for phosphorus ([7.19.29](/7.19.29)). Because species differ in root architecture, mycorrhizal type and the depth from which they take nutrients, they may deplete different resources to different extents, which is one mechanism allowing plant species to coexist ([7.19.23](/7.19.23)).

### 6.2.3. Oxygen

Oxygen is a resource for all aerobic organisms as the terminal electron acceptor of respiration. It is rarely in short supply in air, but its low solubility and slow diffusion in water make it limiting in water and waterlogged soils ([7.19.5](/7.19.5#sec-5.2.1)), and it is depleted wherever microbial respiration of abundant organic matter exceeds supply (eutrophic lakes, sediments, the pitchers of carnivorous plants loaded with prey). Many microbes then respire anaerobically with other electron acceptors (nitrate, Mn⁴⁺, Fe³⁺, sulfate, CO₂), in a sequence of decreasing energy yield. Thawing permafrost illustrates the ecosystem consequences: as palsas turn into bogs and fens, anaerobic methanogenic archaea produce methane, a more potent greenhouse gas than CO₂, and the fraction of anaerobically respired carbon emitted as methane rises as acetoclastic methanogens increase (McCalley et al. 2014).

## 6.3. Organisms as Food

### 6.3.1. Consumers

Heterotrophs that eat living organisms differ in how they use their food ([7.18.22](/7.18.22#sec-22.1.1)). True predators kill their prey soon after attack and eat it (a lynx eating a hare, but also a water flea eating algal cells or a squirrel eating an acorn, both herbivorous predators); grazers take part of many prey without killing them; parasites feed on one or a few hosts for a long time, usually without killing them; and parasitoids develop in a single host and kill it. Generalists (polyphagous species) take many kinds of food, usually in a rank order of preference; specialists (monophagous or oligophagous species) take one or a few. Long-lived consumers are more likely to be generalists, since no single food lasts their whole life; short-lived ones can time their life cycle to that of a single food, and specialization permits efficient structures for handling it, at the cost of having to find it: the hawkmoth *Xanthopan praedicta*, with a proboscis 20–25 cm long, is the only pollinator of the Malagasy orchid *Angraecum sesquipedale*, whose nectar spur is about 30 cm long.

### 6.3.2. Plants and Animals as Packages of Resources

The body of a plant and the body of an animal are very different packages of resources (table below). The most important difference is the cell wall: cellulose, hemicellulose and lignin give plant tissue a high fiber content and a high ratio of carbon to other elements. Leaves have C:N ratios (by mass) of about 20–50, wood of several hundred, whereas bacteria, fungi and animals have ratios of about 4–10. Most of the plant's nitrogen is in the meristems, young leaves and seeds, which are the most heavily defended parts; fruits are sugar-rich rewards for dispersers and contain little nitrogen.

| Food | Typical C:N (mass) | Main components | Value to a consumer |
|---|---|---|---|
| Wood, bark | 200–500 | Cellulose, lignin | Very poor; exploited with symbiotic microbes (termites, some beetles) |
| Mature leaves | 20–50 | Cellulose, protein, defensive compounds | Moderate; nitrogen often limiting |
| Seeds | 10–30 | Starch or oil, storage proteins | Rich and concentrated; defended chemically and mechanically |
| Fruits | 30–80 | Sugars, water | Energy-rich, nitrogen-poor |
| Animal tissue | 4–7 | Protein, fat | Rich; composition similar in all animals |
| Microbial biomass | 4–10 | Protein, nucleic acids | Rich; colonized detritus is preferred by detritivores |

The composition of herbivores, in contrast, is remarkably uniform: there is little to choose, in protein, fat, water and minerals per gram, between a diet of caterpillars, cod or venison. Carnivores therefore face no special digestive problems, and their digestive tracts are short and similar; their problems are finding, catching and handling prey. Herbivores and detritivores eat food that is rich in carbon and poor in nitrogen, and the transition from plant to herbivore involves "burning off" the excess carbon: the waste products of plant eaters are carbon-rich (CO₂, fiber in feces, the sugary honeydew of aphids), those of carnivores nitrogen-rich. Most animals lack cellulases and rely on symbiotic gut microbes to digest cellulose, in the foregut (the **ruminant stomach**), the hindgut (horses, termites) or the cecum (rabbits, which reingest their soft feces); chewing by mammals and grinding in the gizzard of birds break the cell walls so that enzymes can reach the cell contents ([7.19.29](/7.19.29)). Detritivores prefer litter colonized by microbes, which immobilize nitrogen from their surroundings and so lower the C:N ratio of the litter as it decomposes ([7.19.44](/7.19.44)).

Unlike radiation or nutrients, the resources of heterotrophs fight back: prey and plants defend themselves physically, chemically and behaviorally, on ecological and evolutionary time scales ([7.19.24](/7.19.24)).

## 6.4. Ecological Stoichiometry

### 6.4.1. Organisms as Chemical Mixtures

The differences in C:N between plants and animals are one instance of a general principle: organisms are built of chemical elements in proportions that differ from those of their food and of their environment, and the mass balance of each element constrains growth, reproduction and the recycling of nutrients.

**Definition 6.4.1 (Ecological Stoichiometry)** The study of the balance of multiple chemical elements (above all C, N and P) in ecological interactions and processes is called **ecological stoichiometry** (Sterner and Elser 2002).

The approach goes back to Liebig's law of the minimum and to the work of Alfred Redfield, who found in the 1930s that the nitrate and phosphate of deep seawater occur in nearly the same ratio as nitrogen and phosphorus in plankton.

**Definition 6.4.2 (Redfield Ratio)** The average molar ratio of carbon, nitrogen and phosphorus in marine phytoplankton, $\ce{C}:\ce{N}:\ce{P} = 106:16:1$, is called the **Redfield ratio**.

Redfield interpreted the match as the result of biological control: the composition of deep water reflects the remineralization of sinking plankton, and nitrogen fixation and denitrification adjust the oceanic nitrate inventory towards the needs of phytoplankton. The ratio is an average, not a constant: phytoplankton of warm, nutrient-poor subtropical gyres have C:N:P near 195:28:1, those of cold, nutrient-rich polar waters near 78:13:1 (Martiny et al. 2013), and freshwater seston varies even more (C:P from below 100 to more than 1000). The ratio of nutrient supply to the Redfield ratio is the standard first diagnosis of nutrient limitation in water: a dissolved N:P well above 16 suggests P limitation, well below 16 N limitation ([7.19.46](/7.19.46)).

### 6.4.2. Stoichiometric Homeostasis

Organisms differ in how closely their composition follows that of their resources. Let $x$ be the ratio of two elements (say N:P) in the resource and $y$ the same ratio in the consumer. Sterner and Elser (2002) describe the relation by

$$
y = c\,x^{1/H},
$$
where $H \geq 1$ is the regulation coefficient. $H = 1$ means no homeostasis ($y \propto x$: the organism is what it eats), $H \to \infty$ strict homeostasis ($y = c$ regardless of $x$). Autotrophs are relatively flexible: algae grown under P limitation can raise their C:P several-fold, storing excess carbon as starch or lipid. Animals are much more homeostatic, because their bodies consist mainly of protein, nucleic acids and bone, whose compositions are fixed; zooplankton such as *Daphnia* (C:P about 80–90) keep nearly constant composition on foods whose C:P ranges over an order of magnitude. A homeostatic consumer eating food that does not match its needs must therefore dispose of the elements in excess, and this has two consequences.

### 6.4.3. The Threshold Elemental Ratio and Nutrient Recycling

Consider a strictly homeostatic consumer with body C:P ratio $Q_{\mathrm{B}}$ (molar) eating food with C:P ratio $Q_{\mathrm{F}}$ at a rate of $I$ units of carbon per unit time. It assimilates a fraction $a_{\mathrm{C}}$ of the carbon, of which a fraction $e_{\mathrm{C}}$ remains after respiration for growth, and a fraction $a_{\mathrm{P}}$ of the phosphorus, all of which can be used for growth (phosphorus is not respired). Growth, measured in carbon, is limited either by carbon or by phosphorus:

$$
G = \min\left\{a_{\mathrm{C}}e_{\mathrm{C}}I,\; Q_{\mathrm{B}}\,a_{\mathrm{P}}\frac{I}{Q_{\mathrm{F}}}\right\}.
$$

**Proposition 6.4.1 (Threshold Elemental Ratio)** Growth is carbon-limited if $Q_{\mathrm{F}} < Q^*$ and phosphorus-limited if $Q_{\mathrm{F}} > Q^*$, where

$$
Q^* = \frac{a_{\mathrm{P}}}{a_{\mathrm{C}}e_{\mathrm{C}}}\,Q_{\mathrm{B}}
$$
is the *threshold elemental ratio* (TER) of the consumer. When carbon-limited, the consumer releases phosphorus at the rate $I\left(a_{\mathrm{P}}/Q_{\mathrm{F}} - a_{\mathrm{C}}e_{\mathrm{C}}/Q_{\mathrm{B}}\right)$; when phosphorus-limited, it releases no assimilated phosphorus and gets rid of the excess carbon by respiration or egestion.

**Proof** The two terms of the minimum are equal when $a_{\mathrm{C}}e_{\mathrm{C}} = Q_{\mathrm{B}}a_{\mathrm{P}}/Q_{\mathrm{F}}$, that is at $Q_{\mathrm{F}} = Q^*$; for smaller $Q_{\mathrm{F}}$ (P-rich food) the P term is larger, so carbon limits, and vice versa. Phosphorus incorporated into new biomass is $G/Q_{\mathrm{B}}$; the assimilated phosphorus is $a_{\mathrm{P}}I/Q_{\mathrm{F}}$; at steady body composition the difference is excreted. With $G = a_{\mathrm{C}}e_{\mathrm{C}}I$ this gives the stated rate, which is positive exactly when $Q_{\mathrm{F}} < Q^*$; for $Q_{\mathrm{F}} \geq Q^*$, $G = Q_{\mathrm{B}}a_{\mathrm{P}}I/Q_{\mathrm{F}}$ and all assimilated phosphorus is used. $\square$

For *Daphnia* ($Q_{\mathrm{B}} \approx 85$, $a_{\mathrm{P}} \approx 0.8$, $a_{\mathrm{C}}e_{\mathrm{C}} \approx 0.24$) the TER is about 280, within the range of measured values (about 200–300). Lake seston often has C:P above 300, especially in summer when phytoplankton are P-limited, so *Daphnia* is often limited by the phosphorus content rather than the quantity of its food, and its growth on P-poor algae can be restored by adding phosphate to the food. This explains why *Daphnia*, which has a high P demand, does poorly in lakes with high seston C:P, whereas copepods, with lower P demand (C:P about 200–300 in their bodies), do better; and it explains the effect of consumers on nutrient cycling. A consumer recycles the element that is in excess relative to its needs: P-rich *Daphnia* retains phosphorus and recycles nitrogen at high N:P, which pushes phytoplankton towards P limitation, whereas P-poor copepods recycle at lower N:P (consumer-driven nutrient recycling; Sterner et al. 1992). Herbivores eating plants with C:N far above their own TER for nitrogen likewise retain nitrogen and lose carbon, which is why compensatory feeding (eating more of a poor food) is common in insects on nitrogen-poor plants.

![Stoichiometric models. A: gross growth efficiency of carbon of a homeostatic consumer with body C:P 85 (Daphnia-like; carbon assimilation 0.8, net production efficiency of assimilated carbon 0.3, phosphorus assimilation 0.8) as a function of the C:P of its food (Proposition 6.4.1). Growth is carbon-limited below the threshold elemental ratio (TER ≈ 280) and phosphorus-limited above it, where efficiency falls as the excess carbon must be respired or egested. B: phosphorus released by the consumer per unit carbon eaten: excess phosphorus is excreted on P-rich food and none is released above the TER. C: the growth rate hypothesis in a simple composition model: as specific growth rate increases, the RNA content rises (as required for ribosomes), so the P content rises (right axis) and body N:P falls from about 29 to 8 (left axis).](./plots/stoichiometry.py)

### 6.4.4. The Growth Rate Hypothesis

Why do organisms differ in their C:N:P? A large part of the answer is the composition of their machinery for growth.

**Proposition 6.4.2 (Growth Rate Hypothesis)** Rapidly growing organisms have low C:P and N:P ratios, because rapid growth requires many ribosomes and ribosomal RNA is rich in phosphorus (Elser et al. 1996).

The argument is quantitative. Protein synthesis is carried out by ribosomes at a nearly fixed rate per ribosome, so the ribosome content needed rises in proportion to the specific growth rate $\mu$: in bacteria the RNA:protein ratio rises linearly with $\mu$ (the **bacterial growth laws**, [7.6.39](/7.6.39)), and the same holds approximately in eukaryotes. RNA contains about 9–10% phosphorus by mass, protein none, and RNA is the largest pool of P in most fast-growing cells; nitrogen is about 16% of both protein and RNA, so the N content changes little. Writing the P content as a baseline (DNA, phospholipids) plus a term proportional to RNA, and RNA as a linear function of $\mu$, gives P content increasing linearly and N:P decreasing hyperbolically with growth rate (panel C of the figure above). The hypothesis is supported across bacteria, zooplankton and insects: fast-developing *Daphnia* and larval insects have high RNA and P contents and low N:P, slow-growing copepods and adult insects low ones, and in *Drosophila* selected for fast development RNA content increases. It links three levels: the molecular composition of cells, the life history of the organism (its growth rate) and the nutrient cycling of ecosystems (a P-rich, fast-growing consumer sequesters P and recycles N).

## 6.5. Body Size

### 6.5.1. Allometry

Size is the most conspicuous trait of an organism, spanning more than 20 orders of magnitude of mass from mycoplasmas ($10^{-13}\,\mathrm{g}$) to blue whales ($10^{8}\,\mathrm{g}$) and giant sequoias ($10^{9}\,\mathrm{g}$). Almost every physiological and ecological rate changes with size according to a power law,

$$
Y = Y_0 M^b, \qquad \log Y = \log Y_0 + b\log M,
$$
a relation of **allometry** ([7.5.34](/7.5.34#sec-34.6)) with normalization constant $Y_0$ and allometric exponent $b$, the slope on logarithmic axes. If an organism's metabolic rate $B$ scales with exponent $b$, the rate per unit mass $B/M$ scales with $b - 1$, and the time to complete a process that requires a fixed amount of energy or material per unit mass (to mature, to double in mass) scales with $1 - b$. Exponents can be ontogenetic (within an individual as it grows) or phylogenetic (across species of different size).

Life is faster in small organisms. Per gram, a resting mouse metabolizes about 20 times faster than an elephant (the "mouse–elephant curve"), as **Kleiber's law**, $B \propto M^{3/4}$, implies ($B/M \propto M^{-1/4}$; [7.14.30](/7.14.30#sec-30.3)). The effects of size on the ecology of a species can be summarized as follows:

1. The total food requirement increases with size, but the requirement per unit mass decreases; small endotherms must feed almost continuously.
2. Large organisms have fewer predators and are less affected by environmental fluctuations, because they store more reserves relative to their needs and can move farther to escape bad conditions.
3. Large organisms live longer, mature later and have longer generations: lifespan and generation time scale approximately as $M^{1/4}$ (Bonner 1965 found generation time roughly proportional to length, $\propto M^{1/3}$, over the whole range from bacteria to sequoias).
4. Consequently the maximal rate of population increase $r_{\max}$, the **intrinsic rate of increase** under ideal conditions ([7.10.15](/7.10.15)), decreases with size, approximately as $M^{-1/4}$: Fenchel (1974) found three parallel lines of slope about $-0.27$ for unicellular organisms, ectothermic metazoans and endotherms, with intercepts increasing in that order, reflecting the different metabolic levels of the three groups.
5. Small, short-lived species with high $r_{\max}$ recover quickly from disturbance and track environmental fluctuations; large, long-lived species are buffered against them but recover slowly from reductions in numbers, which makes them vulnerable to harvesting ([7.19.53](/7.19.53)).

Southwood (1976) gave a classic interpretation of point 4: small organisms have high mass-specific metabolic rates and short lives, and a high $r_{\max}$ compensates for the short reproductive period. The metabolic theory below turns these correlations into a single quantitative framework, in which both lifespan and $r_{\max}$ follow from the scaling of metabolism.

![Body size and the pace of life. A: the mouse–elephant curve: mass-specific resting metabolic rate of eleven mammals from shrew to elephant against body mass, with Kleiber's line $B/M = 3.39\,M^{-1/4}\,\mathrm{W\,kg^{-1}}$ (the same data as the figure in 7.14.30). The shrew lies far above the line: very small endotherms spend much energy on thermoregulation. B: schematic of the size scaling of maximal population growth rate: parallel lines of slope −1/4 for unicells, ectotherms and endotherms (Fenchel 1974), with illustrative offsets. C: schematic of the energy equivalence rule (Section 6.6.4): population density falling as $M^{-3/4}$ and individual metabolic rate rising as $M^{3/4}$ make the energy use of a population independent of body size.](./plots/size-scaling.py)

## 6.6. The Metabolic Theory of Ecology

### 6.6.1. The Central Equation

Metabolic rate is the rate at which an organism takes up, transforms and expends energy and materials, and so the rate at which it uses resources, grows, reproduces and dies. The metabolic theory of ecology starts from the idea that the two variables with the strongest effect on metabolic rate, body size and temperature, can be combined in a single equation, and derives from it predictions at the levels of the individual, the population, the community and the ecosystem (Gillooly et al. 2001; Brown et al. 2004).

**Definition 6.6.1 (Metabolic Theory of Ecology)** The **metabolic theory of ecology** (MTE) is the theory that the whole-organism metabolic rate $B$ is determined by body mass $M$ and body temperature $T$ (in kelvin) according to

$$
B = B_0\,M^{3/4}\,\mathrm{e}^{-E/(k_{\mathrm{B}}T)}, \tag{6.1}
$$
where $B_0$ is a normalization constant characteristic of a group of organisms, $E \approx 0.6$–$0.7\,\mathrm{eV}$ the average activation energy of the respiratory reactions and $k_{\mathrm{B}} = 8.617\times10^{-5}\,\mathrm{eV\,K^{-1}}$ the **Boltzmann constant**, and that the rates of ecological processes follow from Eq. (6.1).

The equation has two parts, a power law of mass and a Boltzmann–Arrhenius factor of temperature, which we take in turn.

### 6.6.2. Why 3/4? Derivations of the Mass Exponent

The simplest argument gives an exponent of $2/3$.

**Proposition 6.6.1 (Surface Argument)** If the metabolic rate of a set of geometrically similar organisms is limited by exchange across a surface (heat loss, uptake of oxygen or nutrients) and the exchange per unit area is the same in all of them, then $B \propto M^{2/3}$.

**Proof** For geometrically similar bodies of linear size $L$ and equal density, mass $M \propto L^3$ and surface area $A \propto L^2$, so $A \propto M^{2/3}$. If $B$ is proportional to $A$, then $B \propto M^{2/3}$. $\square$

This is Rubner's **surface law** ([7.14.30](/7.14.30#sec-30.3.1)). Kleiber's empirical exponent near $3/4$ remained without a convincing theoretical basis until West, Brown and Enquist (1997) derived it from the geometry of the networks that distribute resources inside organisms (blood vessels, tracheae, xylem).

**Theorem 6.6.1 (West–Brown–Enquist)** Suppose that resources are distributed by a hierarchical branching network with the following properties: (i) each vessel at level $k$ branches into $n$ vessels at level $k + 1$, from the aorta ($k = 0$) to the capillaries ($k = N$); (ii) the network is space-filling, each vessel serving a region of volume proportional to the cube of its length, so that $n\,l_{k+1}^3 = l_k^3$; (iii) branching is area-preserving, $n\,r_{k+1}^2 = r_k^2$, as required for the reflection-free transmission of pulsatile flow in large vessels; (iv) the terminal units (capillaries) have the same size and the same flow in organisms of all sizes; (v) the volume of fluid in the network is proportional to body mass. Then $B \propto M^{3/4}$.

**Proof** Let $\gamma = l_{k+1}/l_k = n^{-1/3}$ and $\beta = r_{k+1}/r_k = n^{-1/2}$ by (ii) and (iii). Level $k$ has $n^k$ vessels, so the number of capillaries is $N_{\mathrm{c}} = n^N$, and by (iv) the metabolic rate, which equals the total flow delivered, is $B \propto N_{\mathrm{c}}$. Writing $r_k = r_N\beta^{k - N}$ and $l_k = l_N\gamma^{k - N}$, the fluid volume of the network is

$$
V = \sum_{k=0}^{N} n^k\pi r_k^2 l_k = \pi r_N^2 l_N\,n^N\sum_{k=0}^{N}\left(n\beta^2\gamma\right)^{k - N}
= \pi r_N^2 l_N\,N_{\mathrm{c}}\sum_{j=0}^{N}\left(n^{1/3}\right)^{j},
$$
because $n\beta^2\gamma = n\cdot n^{-1}\cdot n^{-1/3} = n^{-1/3}$ and we set $j = N - k$. The geometric series equals $\left(n^{(N+1)/3} - 1\right)/\left(n^{1/3} - 1\right) \approx n^{N/3}\,n^{1/3}/\left(n^{1/3} - 1\right)$ for large $N$: the volume is dominated by the largest vessels. Since $n^{N/3} = N_{\mathrm{c}}^{1/3}$ and the capillary dimensions $r_N$, $l_N$ are invariant, $V \propto N_{\mathrm{c}}^{4/3}$. By (v), $M \propto V \propto N_{\mathrm{c}}^{4/3}$, so $N_{\mathrm{c}} \propto M^{3/4}$ and $B \propto M^{3/4}$. $\square$

The same calculation predicts other quarter-power scalings: the radius of the aorta $r_0 = r_N\beta^{-N} = r_N N_{\mathrm{c}}^{1/2} \propto M^{3/8}$, its length $l_0 = l_N N_{\mathrm{c}}^{1/3} \propto M^{1/4}$, and the time for blood to circulate, the ratio of volume to flow, $V/B \propto M^{1/4}$. Measured values for mammals are close to these. In small vessels, where viscosity dominates and flow is not pulsatile, Poiseuille flow (the **Hagen–Poiseuille law**) favors $n\,r_{k+1}^3 = r_k^3$ (Murray's law) instead of area preservation; the complete model, with a crossover between the two regimes, gives exponents slightly below $3/4$ for small mammals, approaching $3/4$ only for very large ones, consistent with the curvature of the data ([7.14.30](/7.14.30#sec-30.3.2)).

A simpler argument, without the details of branching, is due to Banavar, Maritan and Rinaldo (1999). If an organism of linear extent $L$ contains a number of metabolic sites proportional to $L^3$, each served at the same rate by a network from a central source, then $B \propto L^3$. In an efficient network the average distance from source to site is of order $L$, so the amount of fluid (and resource) in transit at any moment is at least proportional to $B\,L \propto L^4$. If this amount is proportional to body mass, $M \propto L^4$ and therefore $B \propto M^{3/4}$; the extent of the network grows as $M^{1/4}$, which is the origin of the quarter-power scaling of times. The argument shows that the exponent follows from two assumptions: transport through a network whose path lengths grow with the size of the organism, and a fixed proportion of the body devoted to the fluid in transit. If the flow velocity itself is size-independent and the network fluid is not proportional to mass, the same reasoning gives exponents closer to $2/3$ (Banavar et al. 2010).

How well do the data agree? The exponent is not universal. Across metazoans it is near $3/4$, but across unicellular eukaryotes it is close to 1 and across prokaryotes greater than 1 (DeLong et al. 2010); for mammals measured under strict basal conditions it is near $0.69$ (White and Seymour 2003), and the log–log relation curves upward (Kolokotrones et al. 2010); in plants it is near 1 for seedlings and approaches $3/4$ in large plants (Mori et al. 2010). Glazier (2010) proposed that the exponent varies between $2/3$ (surface-limited) and 1 (volume-limited) with the level of metabolic activity. An alternative view is that metabolism is set by demand rather than supply: size and metabolic rate co-evolve as parts of a life history, and transport networks evolve to meet whatever demand the life history requires (Harrison 2017). The most defensible conclusion is that $b$ is generally below 1 for multicellular organisms, that $3/4$ is a good first approximation for the large range of sizes over which metazoans are compared, and that the deviations themselves are informative. Most ecological predictions of MTE (below) depend on $b$ only through the exponent $b - 1$ of mass-specific rates, which changes little between $b = 0.67$ and $b = 0.75$.

### 6.6.3. Temperature: the Boltzmann–Arrhenius Factor

The rates of biochemical reactions increase exponentially with temperature according to the **Arrhenius equation**, $k = A\,\mathrm{e}^{-E_{\mathrm{a}}/(RT)}$, or per molecule $\mathrm{e}^{-E/(k_{\mathrm{B}}T)}$ with $E$ in eV. MTE assumes that whole-organism metabolism, the sum of very many reactions, behaves as one reaction with an **apparent activation energy** $E \approx 0.65\,\mathrm{eV}$ ($63\,\mathrm{kJ\,mol^{-1}}$), the average found for aerobic respiration across plants, animals and microbes. Over the narrow range of biological temperatures this exponential is practically equivalent to a $Q_{10}$ description ([7.19.4](/7.19.4)): the ratio of rates at $T_2 = T_1 + 10\,\mathrm{K}$ is

$$
Q_{10} = \exp\!\left[\frac{E}{k_{\mathrm{B}}}\left(\frac{1}{T_1} - \frac{1}{T_2}\right)\right] \approx \exp\!\left[\frac{10E}{k_{\mathrm{B}}T_1^2}\right],
$$
which for $E = 0.65\,\mathrm{eV}$ and $T_1 = 293\,\mathrm{K}$ gives $Q_{10} \approx 2.4$.

The equation suggests a way of comparing organisms measured at different temperatures. Taking logarithms of Eq. (6.1),

$$
\ln B = \ln B_0 + \tfrac{3}{4}\ln M - \frac{E}{k_{\mathrm{B}}}\cdot\frac{1}{T},
$$
so that the temperature-corrected rate $B\,\mathrm{e}^{E/(k_{\mathrm{B}}T)}$ should scale as $M^{3/4}$ alone, and the mass-corrected rate $B\,M^{-3/4}$ should give a straight Arrhenius plot of slope $-E$ against $1/(k_{\mathrm{B}}T)$. Gillooly et al. (2001) found that this double correction collapses data for unicells, plants, invertebrates, fishes, amphibians and reptiles onto common lines, and that the difference between endotherms and ectotherms is largely accounted for by body temperature (figure below).

![Temperature correction in the metabolic theory (simulated data). A: metabolic rates of 160 simulated ectotherms from 1 mg to 10 kg, measured at body temperatures of 5, 15, 25 and 35 °C, generated from Eq. (6.1) with $E = 0.65$ eV and log-normal scatter: the four temperatures form parallel bands. B: the temperature-corrected rate $B\,\mathrm{e}^{E/(k_{\mathrm{B}}T)}$ collapses the bands onto one line, whose fitted slope estimates the mass exponent. C: the mass-corrected rate $\ln(B\,M^{-3/4})$ against $1/(k_{\mathrm{B}}T)$ is a straight Arrhenius plot whose slope estimates $-E$.](./plots/mte-temperature.py)

The temperature dependence has well-known limits. The exponential describes only the rising part of the thermal performance curve; above the optimum, rates fall steeply ([7.19.4](/7.19.4)). Activation energies differ among processes (photosynthesis, about 0.3 eV, is less temperature-sensitive than respiration, which has consequences for the carbon balance of a warming world, [7.19.47](/7.19.47)), among taxa and between acute and evolutionary responses, with a median near 0.55–0.65 eV and a wide range (Dell et al. 2011). Clarke (2004) argued that the agreement of the average with biochemical activation energies is partly coincidental, because organisms adapt their enzymes to temperature. These criticisms concern the generality of a single $E$, not the existence of strong, roughly exponential temperature dependence.

### 6.6.4. Predictions

The power of MTE is that Eq. (6.1), with a few additional assumptions, predicts the scaling of many ecological quantities. Throughout, $\propto$ means proportionality at fixed $B_0$ and $E$.

**Proposition 6.6.2 (Ontogenetic Growth Model)** Suppose that the metabolic energy of an individual of mass $m$ is spent on maintaining existing tissue at a rate proportional to $m$ and on building new tissue at a fixed energy cost per unit mass: $B_0\,m^{3/4} = B_{\mathrm{m}}\,m + E_{\mathrm{m}}\,\mathrm{d}m/\mathrm{d}t$. Then

$$
\frac{\mathrm{d}m}{\mathrm{d}t} = a\,m^{3/4}\left[1 - \left(\frac{m}{M}\right)^{1/4}\right], \qquad a = \frac{B_0}{E_{\mathrm{m}}},\quad M = \left(\frac{B_0}{B_{\mathrm{m}}}\right)^4,
$$
where $M$ is the asymptotic (adult) mass. With $r = (m/M)^{1/4}$ and $\tau = a t/(4M^{1/4}) - \ln\!\left[1 - (m_0/M)^{1/4}\right]$, every species follows the same curve $1 - r = \mathrm{e}^{-\tau}$, and the time to reach a given fraction of adult mass is proportional to $M^{1/4}$ (West, Brown and Enquist 2001).

**Proof** Dividing the energy balance by $E_{\mathrm{m}}$ gives $\mathrm{d}m/\mathrm{d}t = a m^{3/4} - (B_{\mathrm{m}}/E_{\mathrm{m}})m = a m^{3/4}\left[1 - (B_{\mathrm{m}}/B_0)m^{1/4}\right]$, and growth stops at $m^{1/4} = B_0/B_{\mathrm{m}}$, which defines $M$. Substituting $m = M r^4$, $\mathrm{d}m/\mathrm{d}t = 4Mr^3\,\mathrm{d}r/\mathrm{d}t = aM^{3/4}r^3(1 - r)$, so $\mathrm{d}r/\mathrm{d}t = \frac{a}{4M^{1/4}}(1 - r)$, a linear equation with solution $1 - r(t) = (1 - r_0)\,\mathrm{e}^{-at/(4M^{1/4})}$, which is $1 - r = \mathrm{e}^{-\tau}$ with $\tau$ as defined. The time to reach a given $r$ from a given $r_0$ is $t = (4M^{1/4}/a)\ln[(1 - r_0)/(1 - r)] \propto M^{1/4}$. $\square$

The model is a version of the von Bertalanffy growth equation with exponent $3/4$, and its universal curve fits the growth of fishes, birds, mammals and invertebrates remarkably well (figure below). Adding temperature through $B_0 \propto \mathrm{e}^{-E/(k_{\mathrm{B}}T)}$ predicts that development time scales as $M^{1/4}\,\mathrm{e}^{E/(k_{\mathrm{B}}T)}$; Gillooly et al. (2002) showed that egg hatching times of zooplankton, insects, fishes, amphibians and birds collapse onto one line when corrected in this way.

![The ontogenetic growth model (Proposition 6.6.2). A: growth curves of four hypothetical species with adult masses from 10 g to 10 t and the same growth constant $a$: larger species take longer to grow, the time scaling as $M^{1/4}$ (each factor of 100 in mass multiplies the time by about 3.2). B: plotted in the dimensionless variables $1 - (m/M)^{1/4}$ and $\tau$, all four species fall on the single curve $\mathrm{e}^{-\tau}$.](./plots/ontogenetic-growth.py)

The same scaling of times carries over to the population.

**Proposition 6.6.3 (Scaling of Population Rates)** If the generation time $T_{\mathrm{g}}$ scales like other biological times, $T_{\mathrm{g}} \propto M^{1/4}\,\mathrm{e}^{E/(k_{\mathrm{B}}T)}$, and the net reproductive rate $R_0$ (offspring per individual per generation) is independent of size, then the maximal rate of population increase and the mortality rate scale as

$$
r_{\max} \propto M^{-1/4}\,\mathrm{e}^{-E/(k_{\mathrm{B}}T)}, \qquad Z \propto M^{-1/4}\,\mathrm{e}^{-E/(k_{\mathrm{B}}T)}.
$$

**Proof** A population growing at its maximal rate multiplies by $R_0$ per generation, so $r_{\max} \approx \ln R_0/T_{\mathrm{g}}$ ([7.19.9](/7.19.9)), which with constant $R_0$ is proportional to $1/T_{\mathrm{g}}$. At demographic equilibrium the expected lifetime is of the same order as the generation time, so the instantaneous mortality rate $Z$, the reciprocal of mean lifespan, scales in the same way. $\square$

Savage et al. (2004) found the predicted scaling of $r_{\max}$ across organisms from unicells to mammals after temperature correction, and the mortality rates of fish stocks in the wild scale as $M^{-1/4}$ with the predicted temperature dependence. The predictions explain Fenchel's parallel lines (Section 6.5.1) and Southwood's interpretation: $r_{\max}$ and lifespan are two consequences of a single metabolic pace of life.

The last prediction concerns abundance. If the individuals of a species living in a region use a total supply of resources $S$ per unit area, and the population density $N$ adjusts until their combined requirement $N B$ matches the supply, then $N = S/B \propto S\,M^{-3/4}\,\mathrm{e}^{E/(k_{\mathrm{B}}T)}$.

**Definition 6.6.2 (Energy Equivalence Rule)** The empirical observation that population density across species scales approximately as $M^{-3/4}$, so that the total energy flux of a population is independent of the body size of its members, is called the **energy equivalence rule** (Damuth 1981, 1987).

Damuth found a slope of $-0.75$ for the population densities of 307 species of herbivorous mammals: on average, a population of mice uses as much energy per unit area as a population of deer. The rule holds only as a central tendency (densities of species of the same size vary by four orders of magnitude), and it fails between trophic levels: carnivores have steeper slopes and much lower intercepts, because the energy available to them is reduced by the inefficiency of energy transfer between trophic levels ([7.19.43](/7.19.43)). The temperature term predicts that, at the same mass and supply, populations of ectotherms are denser in cold than in warm environments, and the combination of the temperature term with energy equivalence was used by Allen, Brown and Gillooly (2002) to predict how the number of species should increase with environmental temperature ([7.19.35](/7.19.35)).

**Example 6.6.1** Using MTE with $E = 0.65\,\mathrm{eV}$, compare the maximal rate of increase (a) of two related ectotherms of 1 g and 1 kg at the same temperature, and (b) of the same species at 10 °C and 20 °C.

**Solution** (a) $r_{\max} \propto M^{-1/4}$, so the ratio is $(10^3)^{1/4} = 5.6$: the small species can increase 5.6 times faster per unit time. (b) $r_{\max}(20\,^\circ\mathrm{C})/r_{\max}(10\,^\circ\mathrm{C}) = \exp\!\left[\frac{0.65}{8.617\times10^{-5}}\left(\frac{1}{283.15} - \frac{1}{293.15}\right)\right] = \exp(0.909) = 2.5$. A 10 °C warming has about the same effect as a 40-fold reduction in body mass ($2.5^4 \approx 39$); in this sense temperature and size are interchangeable determinants of the pace of life.

:::

MTE has been extended to communities and ecosystems, where the respiration of a community is the sum of individual metabolic rates and the turnover of biomass scales as $M^{-1/4}$, and it has been combined with ecological stoichiometry, since the rates of uptake of N and P are themselves set by metabolism (Allen and Gillooly 2009). Its strengths are the small number of parameters and the explicit mechanistic link between physiology and ecology; its weaknesses are the variability of the exponents and activation energies, the neglect of the many factors (resource supply, predation, life-history trade-offs) that shift species away from the central tendency, and the debate about whether supply networks or demand set the scaling. As with other general theories, the residuals from its predictions are often as interesting as the predictions themselves.

## Summary

- Conditions are tolerated, resources consumed (Definition 6.1.1); only resources are competed for. Autotrophs use inorganic resources, heterotrophs organic ones.
- Resources taken in pairs are essential, perfectly substitutable, complementary, antagonistic or inhibitory, recognized by the shapes of their growth isoclines; the zero net growth isocline is a boundary of the niche, and for essential resources it is set by $R_i^* = Km/(\mu_{\max} - m)$ (Liebig's law of the minimum).
- Plants need radiation, CO₂, water and some 14 mineral elements; depletion zones of mobile nitrate are millimeters wide, those of adsorbed phosphate a tenth of a millimeter (Example 6.2.1), which explains the different foraging strategies of roots and the importance of mycorrhizae for phosphorus.
- Plant tissues have high and variable C:N (leaves 20–50, wood hundreds), animal tissues low and uniform C:N (4–7); herbivores burn off carbon, carnivores excrete nitrogen, and most animals depend on symbiotic microbes to digest cellulose.
- Ecological stoichiometry (Definition 6.4.1): the Redfield ratio C:N:P = 106:16:1 (Definition 6.4.2) is an average with systematic variation; animals are more homeostatic ($y = c\,x^{1/H}$) than autotrophs. A homeostatic consumer is C-limited below and P-limited above its threshold elemental ratio $Q^* = a_{\mathrm{P}}Q_{\mathrm{B}}/(a_{\mathrm{C}}e_{\mathrm{C}})$ and recycles the element in excess (Proposition 6.4.1). Fast growth requires P-rich ribosomes, so fast-growing organisms have low C:P and N:P (Proposition 6.4.2).
- Allometry $Y = Y_0 M^b$: mass-specific rates scale as $M^{b-1}$, times as $M^{1-b}$; with $b = 3/4$, mass-specific metabolism and $r_{\max}$ scale as $M^{-1/4}$, lifespan and generation time as $M^{1/4}$.
- MTE (Definition 6.6.1): $B = B_0 M^{3/4}\mathrm{e}^{-E/(k_{\mathrm{B}}T)}$, $E \approx 0.65$ eV ($Q_{10} \approx 2.4$). The surface argument gives $2/3$ (Proposition 6.6.1); a space-filling, area-preserving network with invariant capillaries and fluid volume proportional to mass gives $3/4$ (Theorem 6.6.1), as does the supply-network argument; observed exponents vary (about 0.69 for strict mammal BMR, 1 for protists, > 1 for prokaryotes).
- Predictions: the universal ontogenetic growth curve with growth times $\propto M^{1/4}$ (Proposition 6.6.2); $r_{\max}$ and mortality $\propto M^{-1/4}\mathrm{e}^{-E/(k_{\mathrm{B}}T)}$ (Proposition 6.6.3); population density $\propto M^{-3/4}\mathrm{e}^{E/(k_{\mathrm{B}}T)}$ and the energy equivalence rule (Definition 6.6.2). A 10 °C warming has about the same effect on $r_{\max}$ as a 40-fold reduction in mass (Example 6.6.1).

## Questions

1. For two essential resources with Monod growth functions $f_i(R_i) = \mu_{\max}R_i/(K_i + R_i)$ and mortality $m$, derive the zero net growth isocline. How does it change if mortality increases, and what does this imply for the resource levels a species can tolerate?

   **Answer** Growth is $g = \min\{f_1(R_1), f_2(R_2)\} - m$, and $g = 0$ requires that the smaller of the two $f_i$ equals $m$. Each $f_i(R_i) = m$ gives $R_i^* = K_i m/(\mu_{\max} - m)$ (requiring $\mu_{\max} > m$). The isocline consists of the vertical half-line $R_1 = R_1^*$, $R_2 \geq R_2^*$, and the horizontal half-line $R_2 = R_2^*$, $R_1 \geq R_1^*$: a right angle with corner $(R_1^*, R_2^*)$. Since $\mathrm{d}R_i^*/\mathrm{d}m = K_i\mu_{\max}/(\mu_{\max} - m)^2 > 0$, higher mortality moves the corner outward, more steeply as $m$ approaches $\mu_{\max}$: a species subject to heavy predation or disturbance needs richer resources, and it cannot persist at all if $m \geq \mu_{\max}$. This is the basis of the prediction that the competitor with the lower $R^*$ wins ([7.19.23](/7.19.23)).

2. A herbivorous insect with body C:N 6 (by mass) assimilates 50% of the carbon and 70% of the nitrogen of its food and respires 60% of the assimilated carbon. Find its threshold elemental ratio for C:N and decide whether it is N- or C-limited on leaves with C:N 30. What would you expect it to do?

   **Answer** Applying Proposition 6.4.1 to nitrogen: $a_{\mathrm{C}}e_{\mathrm{C}} = 0.5 \times 0.4 = 0.2$, $a_{\mathrm{N}} = 0.7$, so $Q^* = 0.7 \times 6/0.2 = 21$. Leaves with C:N 30 exceed the TER, so growth is nitrogen-limited; growth efficiency of carbon is $Q_{\mathrm{B}}a_{\mathrm{N}}/Q_{\mathrm{F}} = 6 \times 0.7/30 = 0.14$ instead of 0.2, and the excess carbon must be respired or egested. Expected responses: compensatory feeding (eating more, at the cost of handling more fiber and toxins), selective feeding on N-rich tissues (young leaves, phloem), higher nitrogen assimilation efficiency, and faster growth when plants are fertilized; this is why outbreaks of many herbivorous insects follow increases in plant nitrogen.

3. In the proof of Theorem 6.6.1, the fluid volume was dominated by the largest vessels. Repeat the calculation assuming that branching follows Murray's law $n\,r_{k+1}^3 = r_k^3$ at all levels, and find the resulting exponent. Why is area preservation needed to obtain 3/4?

   **Answer** With $\beta = n^{-1/3}$, $n\beta^2\gamma = n\cdot n^{-2/3}\cdot n^{-1/3} = 1$, so every level contributes the same volume and $V = \pi r_N^2 l_N\,N_{\mathrm{c}}(N + 1)$. Since $N = \ln N_{\mathrm{c}}/\ln n$, $V \propto N_{\mathrm{c}}\ln N_{\mathrm{c}}$, so $M \propto N_{\mathrm{c}}\ln N_{\mathrm{c}}$ and $B \propto N_{\mathrm{c}}$ grows as $M/\ln M$, almost isometrically (an effective exponent close to 1). The 3/4 law therefore requires that the network volume grow faster than the number of capillaries, which area-preserving branching of the large vessels provides ($V \propto N_{\mathrm{c}}^{4/3}$); in the full model of West et al. the large, pulsatile vessels are area-preserving and only the small, viscous ones follow Murray's law, and the large vessels dominate the volume in large animals.

4. The energy equivalence rule predicts that herbivore population density scales as $M^{-3/4}$. If total population biomass is $NM$, how should it scale with body mass? Use the result to explain why, in a pasture, the biomass of soil bacteria may be small although their respiration is comparable to that of the cattle.

   **Answer** Biomass per unit area $NM \propto M^{-3/4}M = M^{1/4}$: populations of large species have larger standing biomass for the same energy flux, because each gram of a large organism metabolizes more slowly ($B/M \propto M^{-1/4}$). Conversely, a small standing biomass of small organisms can process as much energy as a large biomass of large ones. Bacteria, with mass-specific metabolic rates many orders of magnitude higher than cattle (and the different normalization constant of unicells), can respire as much energy per hectare from a biomass of a few hundred kilograms as the cattle do from several tonnes; this is Odum's point that standing crop depends on the size of the organisms, not only on the energy flow through a trophic level.

5. (Open question) Under global warming, MTE predicts faster metabolism and faster population turnover of ectotherms. Discuss what additional information you would need to predict whether the population size of a particular ectotherm will increase or decrease.

   **Answer** Points to discuss: Eq. (6.1) predicts only the rising part of the thermal performance curve; whether a population benefits depends on where current temperatures lie relative to its optimum and critical maximum ([7.19.4](/7.19.4)): tropical ectotherms already near their optimum may decline. Resource supply must rise as fast as demand, but primary production has a lower activation energy than respiration, so consumers may become food-limited (energy equivalence predicts lower density at higher $T$ for a fixed supply). Body size often decreases with warming (the temperature–size rule), changing fecundity and vulnerability to predators. Interactions matter: predators and parasites also speed up; phenological mismatch with food may arise ([7.18](/7.18)); oxygen supply in water falls with temperature (Section 6.2.3, [7.19.5](/7.19.5)). Needed: the thermal performance curves of the species and its resources, its temperature-dependent vital rates, its interactions, and the projected change in the variability, not only the mean, of temperature.
