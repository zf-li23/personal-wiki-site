---
title: Dormancy, Migration and Complex Life Cycles
description: "Escaping adverse conditions in time and space as life history strategies: dormancy as migration in time, predictive and consequential dormancy, diapause and its photoperiodic control with an optimal-switching model, cryptobiosis, torpor, hibernation and aestivation; seed dormancy, seed banks and Cohen's bet-hedging model of germination; migration patterns, insect migration and a model of partial migration; complex life cycles, metamorphosis and the mu/g rule for ontogenetic habitat shifts, parasite life cycles; and phenological change and mismatch under climate warming."
---

No habitat is favorable all the time. Organisms that cannot tolerate a bad season where they are can escape it in two ways: in time, by entering a dormant state until conditions improve, or in space, by moving to a place where conditions are better. Many also divide their life between habitats, feeding and growing in one and dispersing or reproducing in another, which requires a change of form. Dormancy, migration and complex life cycles are therefore components of the life history strategy ([7.19.18](/7.19.18)), and they can be analyzed with the same tools: trade-offs, the timing of decisions, and fitness in a variable environment. This chapter treats dormancy in animals and plants, with models of the timing of diapause and of the germination of seeds (Section 19.1), migration and its population consequences (Section 19.2), complex life cycles and the rule for switching between habitats (Section 19.3), and the responses of these timed life histories to climate change (Section 19.4). The physiology of diapause, of insect metamorphosis and of insect migration is described in [7.17.29](/7.17.29), torpor and hibernation in [7.14.31](/7.14.31), the molecular basis of extreme tolerance in [7.19.7](/7.19.7), and the behavior of migration and navigation in [7.18.20](/7.18.20) and [7.18.21](/7.18.21).

## 19.1. Escape in Time: Dormancy

### 19.1.1. Dormancy as Migration in Time

A dispersing propagule gains fitness if it is more likely to leave descendants elsewhere than at home; a delay in development gains fitness if the future is likely to be better than the present. Delayed recruitment is therefore "migration in time".

**Definition 19.1.1 (Dormancy)** **Dormancy** is a state of suspended or greatly reduced development, growth and metabolism, usually accompanied by increased tolerance of adverse conditions (drought, cold, heat, lack of food), in which an organism passes a period unfavorable for activity. It is *predictive* when it is entered in response to cues that anticipate the adverse conditions, before they arrive, and *consequential* when it is entered in response to the adverse conditions themselves (Müller 1970).

Predictive dormancy is typical of predictable, seasonal environments: it allows an organism to prepare (storing reserves, synthesizing protective compounds, moving to a sheltered site) and to be in a resistant stage when the bad season begins. In animals it is called **diapause** ([Definition 29.7.1](/7.17.29#def-29.7.1) of 7.17.29) and in plants innate or primary dormancy. Consequential dormancy, such as the quiescence of insects at temperatures below their developmental threshold, is typical of unpredictable environments: it costs the time lost before the response, but has two advantages: the organism enters dormancy only if adverse conditions actually occur, and it can resume activity as soon as they end.

### 19.1.2. Diapause and Its Timing

Diapause occurs in all developmental stages of insects, but at a fixed stage in each species. The field grasshopper *Chorthippus brunneus*, an annual, passes the winter in an obligatory egg diapause, from which it is released only after a long cold period (about five weeks at $0\,^\circ\mathrm{C}$); this prevents hatching during a brief warm spell in winter and synchronizes development in spring. Species with several generations a year usually have a facultative diapause confined to the generation that will meet the winter: *Drosophila obscura* has four generations a year in England, and only the adults that emerge in the short days of autumn store fat, arrest their gonadal development and enter diapause, recommencing in response to the long days of spring.

The usual cue is day length, which, unlike temperature, changes in exactly the same way every year: diapause is a form of **photoperiodism**. The response of a population is summarized by its **critical photoperiod** ([Definition 29.7.2](/7.17.29#def-29.7.2) of 7.17.29), the day length at which half the individuals enter diapause, which increases with latitude ([7.17.29](/7.17.29)). Three types of response are distinguished:

| Type | Response | Example |
|---|---|---|
| long-day type (short-day diapause) | develops in long days, enters diapause when day length falls below the critical photoperiod (often 13–17 h in temperate species) | Colorado potato beetle (*Leptinotarsa decemlineata*), most temperate insects |
| short-day type (long-day diapause) | develops in short days, enters diapause in long days; diapause in summer (aestivation) or a maternally determined egg diapause | bivoltine races of the silkworm *Bombyx mori* |
| intermediate type | develops within a band of day lengths, diapause above and below it | the yellow-tail moth *Euproctis similis* |

In the domesticated silkworm, whether a female lays diapausing eggs is determined by the temperature and day length she herself experienced as an embryo and young larva: high temperature and long days during her development lead to diapause eggs, which are laid in summer and hatch the next spring. The wild silkmoth *Bombyx mandarina*, its ancestor, relies more on the photoperiod experienced by the larvae (Shiomi 2021). Domestication has thus changed the cues, not the principle: the decision is taken well before the diapausing stage, on the basis of information that predicts the season.

When should a multivoltine insect stop producing another generation and produce diapausing offspring instead? A simple model shows the logic of the decision.

**Proposition 19.1.1 (Optimal Switch to Diapause)** An adult on date $t$ can produce diapausing offspring, each of which survives the winter (value 1), or $m$ non-diapausing offspring, which develop in a time $\tau$ into adults that can themselves produce diapausing offspring, but only if the season, which ends at a random date $E$ with survival function $S(x) = \mathbb{P}(E > x)$, has not ended by $t + \tau$. If a new generation is worth $m\,S(t + \tau)$, the adult should switch to diapause from the date $t^*$ at which

$$
m\,S(t^* + \tau) = 1 .
$$
If $E$ is normal with mean $T$ and standard deviation $\sigma$, then $t^* = T - \tau + \sigma z_{1/m}$, where $z_{1/m}$ is the upper $1/m$ quantile of the standard normal distribution.

**Proof** Breeding again yields $m$ offspring, each of which counts as one diapausing grandchild if it completes development before the end of the season, an event of probability $S(t + \tau)$; diapause yields one diapausing offspring per egg. The expected value of breeding again, $mS(t + \tau)$, decreases with $t$, so breeding is better before the date at which it equals 1 and diapause afterward. For the normal distribution, $S(x) = 1/m$ at $x = T + \sigma z_{1/m}$. $\square$

The switch date tracks the end of the season, which explains why the critical photoperiod must increase with latitude: farther north the season ends earlier, so the same switch date occurs at a longer day length. When a further generation pays well ($m$ large), the optimal switch is later than the date $T - \tau$ at which the last generation would just finish in an average year: the insect gambles on a late autumn. Uncertainty about the end of the season ($\sigma$) increases the effect (Figure 1). Cohen (1970) showed that, with uncertain season length, a mixture of diapausing and non-diapausing offspring can be optimal, a form of bet hedging (Section 19.1.5). Climate warming lengthens the season, and the critical photoperiods of the pitcher-plant mosquito *Wyeomyia smithii* in North America have evolved toward shorter day lengths within a few decades (Bradshaw and Holzapfel 2001; [7.17.29](/7.17.29)).

![When to switch to diapause (Proposition 19.1.1), with a generation time of τ = 30 days and an end of the season that is normally distributed with standard deviation 10 days. A: the expected value of producing another generation, mS(t + τ), against the date, for m = 5 and 20 offspring (mean end of season on day 270); diapause is favored where the curve falls below the value 1 of a diapausing egg (points: the switch dates). B: the switch date against the mean end of the season: it follows the season, and is later than the average-year deadline T − τ (dashed) the more a further generation pays](./plots/diapause-decision.py)

### 19.1.3. Cryptobiosis

At the extreme of dormancy, metabolism stops altogether. In **cryptobiosis** ([7.17.12](/7.17.12), [7.19.7](/7.19.7)) an organism survives in a state with no measurable metabolism and resumes life when conditions return. Tardigrades (water bears) can enter cryptobiosis at any stage of their life and show all four forms: *anhydrobiosis*, induced by desiccation; *cryobiosis*, by freezing; *osmobiosis*, by high osmotic pressure; and *anoxybiosis*, by lack of oxygen. In the dried "tun" state they have been reported to survive brief exposure to temperatures from near absolute zero to over $150\,^\circ\mathrm{C}$, high doses of ionizing radiation and the vacuum of space, and specimens of the Antarctic tardigrade *Acutuncus antarcticus* were revived after more than 30 years in a freezer (Tsujimoto et al. 2016). Rotifers, nematodes, the brine shrimp *Artemia* (whose cysts are dispersed by wind and birds between temporary salt lakes), resurrection plants and many seeds are cryptobiotic. Ecologically, cryptobiosis is a strategy for habitats that dry out or freeze unpredictably, such as mosses, lichens, temporary pools and soils, and it often doubles as a means of dispersal, because dry cysts and tuns are carried by wind.

### 19.1.4. Torpor, Hibernation and Aestivation

Endotherms pay a high energetic price for keeping warm when food is scarce, and many reduce it by **torpor** and **hibernation** ([Definition 31.6.6](/7.14.31#def-31.6.6) of 7.14.31): a controlled lowering of metabolic rate and body temperature, for hours (daily torpor) or for weeks (hibernation, a sequence of torpor bouts interrupted by brief arousals). Daily torpor is common in small birds and mammals with high mass-specific metabolic rates: the black metaltail hummingbird (*Metallura phoebe*) in the Peruvian Andes, whose body temperature is normally about $33\,^\circ\mathrm{C}$, can lower it to $3.3\,^\circ\mathrm{C}$ on cold nights (Wolf et al. 2020), the lowest value recorded in a bird. Hibernators, such as ground squirrels, dormice, hedgehogs and many bats, accumulate fat before winter, and their body temperature may fall to a few degrees above ambient. The winter dormancy of bears was once called "pseudo-hibernation", because their body temperature falls only by about $5\,^\circ\mathrm{C}$; but American black bears reduce their metabolic rate to about a quarter of the basal rate, and do not eat, drink, urinate or defecate for months (Tøien et al. 2011), and their dormancy is now regarded as hibernation in which metabolic suppression is largely independent of temperature.

The winter dormancy of ectotherms (frogs buried in mud, snakes in dens) is different in kind: their body temperature follows that of the surroundings, and they cannot rewarm themselves, so a hibernaculum that freezes kills them unless they are freeze tolerant, as the wood frog *Lithobates sylvaticus* is ([7.19.4](/7.19.4)). Endothermic hibernators, in contrast, increase their metabolic rate when the temperature falls too low, and arouse if it falls further. *Aestivation* is dormancy during the hot, dry season: African lungfishes (*Protopterus*) survive the drying of their pools for months, even years, in mucus cocoons in the mud; desert snails seal their shells; some desert rodents and the Malagasy fat-tailed dwarf lemur (*Cheirogaleus medius*), a primate that hibernates in tree holes during the dry season, show that the same physiology serves against heat and drought as against cold.

### 19.1.5. Seed Dormancy and Seed Banks

**Seed dormancy** ([7.12.19](/7.12.19)) is almost universal in flowering plants: the embryo ceases development while still on the parent, dries, and requires a specific stimulus to germinate. Three types are distinguished (Harper 1977):

- *innate* dormancy, in which the seed requires a specific external stimulus (water, cold, light, a particular ratio of red to far-red light, fire) before it can germinate; seedlings of such species appear in flushes;
- *enforced* dormancy, imposed by unfavorable external conditions (consequential); seeds of *Chenopodium album* from archaeological excavations were viable after 1700 years, and clones of the Missouri goldenrod *Solidago missouriensis* defoliated by a beetle disappeared above ground for 1–10 years and then reappeared from dormant rhizomes;
- *induced* dormancy, acquired during a period of enforced dormancy: the seeds of many weeds germinate in darkness when shed, but after burial they require light. Wesson and Wareing (1969) found that soil collected at night and kept in darkness produced no seedlings, whereas soil exposed to light produced many: seeds in the soil germinate only when disturbance (plowing, burrowing animals, tree falls) brings them to the surface.

The accumulation of dormant seeds in the soil forms a *seed bank*, whose composition can differ greatly from that of the vegetation above: in many grasslands and forests the seed bank is dominated by short-lived annuals and weeds, while the established vegetation consists of long-lived perennials whose seeds are short-lived. Seed banks buffer populations against bad years, preserve genetic variation from earlier generations, and determine the course of succession after disturbance ([7.19.36](/7.19.36)). They are also why plant metapopulations are hard to demonstrate ([7.19.16](/7.19.16)) and why restoration often cannot rely on the soil: in abandoned farmland along the Cache River in Illinois, the seeds of the dominant swamp trees, including bald cypress (*Taxodium distichum*), were absent from the seed bank even in intact swamps (Middleton 2003). Some trees store their seeds on the plant instead: in species with **serotiny** (many pines, *Banksia*, eucalypts), cones or fruits stay closed for years and release their seeds after fire, which creates the conditions for establishment.

Why should seeds of an annual not all germinate in the first suitable season? Cohen (1966) showed that delayed germination is a form of **bet hedging** in a random environment.

**Theorem 19.1.2 (Cohen's Germination Model)** Each year a fraction $g$ of the seeds in the seed bank germinates. A year is good with probability $p$, independently of other years; each germinating seed then produces $Y$ seeds, whereas in a bad year germinating seeds produce nothing. Seeds that do not germinate survive in the soil with probability $s < Y$. The long-run growth rate of the seed bank is

$$
G(g) = p\ln\bigl(gY + (1 - g)s\bigr) + (1 - p)\ln\bigl((1 - g)s\bigr),
$$
which is maximized at

$$
g^* = p - \frac{(1 - p)s}{Y - s}
$$
when this lies in $(0, 1)$, and at $g^* = 0$ if it is negative. Since $g^* < p$, optimal germination is spread over years, and less than the frequency of good years.

**Proof** The bank multiplies by $\lambda = gY + (1 - g)s$ in a good year and by $(1 - g)s$ in a bad year, so by the law of large numbers the long-run growth rate is $\mathbb{E}[\ln\lambda] = G(g)$ (Theorem 15.2.1 of [7.19.15](/7.19.15#thm-15.2.1)). $G$ is strictly concave, as a sum of logarithms of affine functions of $g$, and $G'(g) = \frac{p(Y - s)}{gY + (1 - g)s} - \frac{1 - p}{1 - g}$. Setting $G' = 0$ gives $p(Y - s)(1 - g) = (1 - p)\bigl(s + g(Y - s)\bigr)$, that is $g(Y - s) = p(Y - s) - (1 - p)s$, which is the stated $g^*$. $G'(g) \to -\infty$ as $g \to 1$, so the optimum is below 1; if $g^* \le 0$, $G'(0) \le 0$ and the optimum is $g = 0$ (within the model, a species that should never germinate cannot exist). $\square$

A genotype that germinates completely ($g = 1$) is wiped out by the first bad year, however productive it is in good ones; a genotype that holds back a fraction of its seeds loses some growth in good years but survives the bad ones. The better the seeds survive in the soil (large $s$) and the rarer the good years, the smaller the optimal germination fraction (Figure 2). If seeds can detect favorable conditions, for example by germinating only after a rainfall large enough to support growth to maturity, *predictive germination* reduces the need for bet hedging, and real desert annuals combine both. Venable (2007) analyzed 20 years of data on ten species of winter annuals in the Sonoran Desert: species whose reproductive success varied more from year to year had lower germination fractions, as the theory predicts.

![Cohen's model of germination in a random environment (Theorem 19.1.2), with Y = 10 seeds per germinating seed in good years and seed survival s = 0.8 in the soil. A: the long-run growth rate E[ln λ] of the seed bank against the fraction g germinating each year, for three probabilities p of a good year; points: the optimum g*. For p = 0.3 even the optimal strategy only just persists. B: the optimal germination fraction against p for three seed survivals (lines), always below p (dashed). C: seed bank size in one random sequence of good and bad years (p = 0.5) for complete germination (g = 1, red: wiped out by the first bad year, at the cross), the optimum g* = 0.46 and g = 0.1](./plots/seed-bank-bet-hedging.py)

## 19.2. Escape in Space: Migration

### 19.2.1. Migration and Dispersal

Movement in space is the alternative to dormancy. In the terminology used throughout this course, **migration** ([7.18.20](/7.18.20)) is directional movement of individuals between regions, often of whole populations and in a regular cycle, whereas **dispersal** ([Definition 10.2.1](/7.10.10#def-10.2.1) of 7.10.10) is the movement of individuals away from their place of birth or breeding, not in a common direction; its ecological consequences are treated in [7.19.16](/7.19.16). Migrations follow three patterns:

- repeated return journeys within an individual's life: most migratory birds, bats, baleen whales and large ungulates, which travel between breeding and wintering areas every year;
- a single return journey: Pacific salmon, which hatch in rivers, grow in the sea and return to their natal river to spawn and die (*anadromous*: breeding in fresh water, growing in the sea), and freshwater eels, which do the reverse (*catadromous*: growing in rivers and spawning in the sea; European and American eels in the Sargasso Sea);
- one-way journeys of each individual, in which the round trip is completed over several generations: the monarch butterfly (*Danaus plexippus*), whose autumn generation flies up to 4000 km from eastern North America to overwintering sites in the oyamel fir forests of central Mexico, and whose descendants recolonize the north over three or four generations in spring and summer; many aphids, moths and locusts.

### 19.2.2. Migrants and Distances

The distances can be enormous. The common swift of northern China, *Apus apus pekinensis*, which breeds in the eaves of old buildings in Beijing, winters in southern Africa: geolocators showed that it flies through Central Asia and the Arabian Peninsula, a round trip of about 30,000 km each year, as shown by geolocator studies begun in 2014. The Arctic tern (*Sterna paradisaea*) travels between Arctic breeding sites and the Antarctic pack ice, about 70,000 km a year along winding routes (Egevang et al. 2010), and bar-tailed godwits (*Limosa lapponica*) fly nonstop from Alaska to New Zealand, more than 11,000 km in about nine days, after fattening on the mudflats of the Yellow Sea on their way north ([7.18.20](/7.18.20)). Among mammals, humpback whales (*Megaptera novaeangliae*) that feed in Antarctic waters off the Antarctic Peninsula in summer breed off Colombia and Central America in winter, more than 8000 km away (Rasmussen et al. 2007), one of the longest regular migrations of any mammal.

Insects are the most numerous migrants. *Insect migration* ([Definition 29.8.1](/7.17.29#def-29.8.1) of 7.17.29) is recognized by behavior rather than distance: persistent, straightened-out movement, undistracted by resources that would normally arrest it, with distinct departure and arrival behavior and reallocation of energy to flight (Kennedy 1985; Dingle 1996). Radar studies over southern England estimated that about 3.5 trillion insects (3200 tonnes) migrate high above the ground each year, moving north in spring and south in autumn on favorable winds (Hu et al. 2016). In East Asia the brown planthopper (*Nilaparvata lugens*), the white-backed planthopper and the oriental armyworm (*Mythimna separata*) cannot overwinter in most of China; each spring they are carried northward from southern China and Indochina on the southwest monsoon, and the outbreaks they cause in northern rice and maize fields are forecast from the weather and the source populations ([7.17.29](/7.17.29), [7.19.53](/7.19.53)).

### 19.2.3. The Ecology of Migration

Migration pays when the benefit of better conditions elsewhere (food, a milder winter, safe breeding sites) exceeds its costs in energy, time and risk. A simple model shows why many species are partially migratory, some individuals staying and others leaving.

**Proposition 19.2.1 (Partial Migration)** Let residents survive the winter with probability $\mathrm{e}^{-w}$, where $w$ measures winter severity, and gain a breeding advantage from early settlement that is shared among residents, so that their breeding success is $1 + a(1 - f)$ when a fraction $f$ of the population stays ($a > 0$). Let migrants survive the journey and the winter with probability $S_{\mathrm{m}}$, independent of the winter, and have breeding success 1. Then the evolutionarily stable fraction of residents is

$$
f^* = \begin{cases} 1, & w \le \ln(1/S_{\mathrm{m}}), \\ 1 - \dfrac{S_{\mathrm{m}}\mathrm{e}^{w} - 1}{a}, & \ln(1/S_{\mathrm{m}}) < w < \ln\bigl((1 + a)/S_{\mathrm{m}}\bigr), \\ 0, & w \ge \ln\bigl((1 + a)/S_{\mathrm{m}}\bigr). \end{cases}
$$

**Proof** The fitness of a resident is $W_{\mathrm{r}}(f) = \mathrm{e}^{-w}\bigl(1 + a(1 - f)\bigr)$, decreasing in $f$, and that of a migrant $W_{\mathrm{m}} = S_{\mathrm{m}}$. A mixture is stable where $W_{\mathrm{r}}(f^*) = W_{\mathrm{m}}$: if $f$ rose above $f^*$, residents would do worse than migrants and $f$ would fall, and conversely. Solving gives the middle case. If $W_{\mathrm{r}}(1) = \mathrm{e}^{-w} \ge S_{\mathrm{m}}$, residency pays even when everyone stays ($f^* = 1$); if $W_{\mathrm{r}}(0) = \mathrm{e}^{-w}(1 + a) \le S_{\mathrm{m}}$, migration pays even for a lone resident ($f^* = 0$). $\square$

The model is a frequency-dependent game ([7.18.25](/7.18.25)): the benefit of staying declines as more individuals stay, so the two tactics coexist over a range of winters (Figure 3; Lundberg 1987, Kaitala et al. 1993). In reality, the choice is often conditional on the state of an individual: in European blackbirds (*Turdus merula*), robins and many fish (brown trout that remain in streams versus sea trout that migrate), dominant or larger individuals stay and subordinate or smaller ones migrate, and the proportions change with winter severity and with the climate. In Europe, the proportion of migratory blackcaps (*Sylvia atricapilla*) wintering in Britain instead of the Mediterranean has increased since the 1960s, a genetically based change favored by milder winters and garden feeding ([7.18.20](/7.18.20)).

Migration links the population dynamics of distant places. A migratory population can be limited by events on the breeding grounds, on the wintering grounds or at stopover sites, and conditions in one season carry over into the next: American redstarts (*Setophaga ruticilla*) that winter in good habitat arrive earlier and in better condition on the breeding grounds and raise more young (Norris et al. 2004). The decline of many shorebirds of the East Asian–Australasian flyway, including the critically endangered spoon-billed sandpiper (*Calidris pygmaea*) and the great knot, follows the loss of tidal flats around the Yellow Sea, where they refuel on migration (Studds et al. 2017): the conservation of migrants requires protecting every link of the annual cycle.

![A simple model of partial migration (Proposition 19.2.1), with migrant survival S_m = 0.6 and a breeding advantage a = 0.8 of residents shared among them. A: fitness of a resident when all others migrate (f = 0, solid) and when all stay (f = 1, dashed), and of a migrant, against winter severity w. B: the evolutionarily stable fraction of residents f*: all individuals stay in mild winters, all migrate in severe ones, and in between the two tactics coexist with equal fitness](./plots/migration-model.py)

## 19.3. Complex Life Cycles

### 19.3.1. Metamorphosis and the Division of Labor

**Definition 19.3.1 (Complex Life Cycle)** A *complex life cycle* is a life cycle that includes two or more ecologically distinct stages, separated by an abrupt change of morphology, physiology and habitat (a **metamorphosis**), each of which may use different resources and suffer different sources of mortality (Wilbur 1980). About 80 % of animal species have complex life cycles, including most insects (**holometaboly**, [7.17.29](/7.17.29)), most amphibians, many fishes and nearly all marine invertebrates with planktonic larvae.

A complex life cycle allows different stages to be specialized for different tasks, two in particular:

- Growth versus dispersal. In many insects the larva is a feeding and growing machine and the winged adult disperses and reproduces; mayflies live for months or years as aquatic nymphs and for a day or two as adults that cannot feed. In most sessile marine invertebrates (barnacles, corals, sea urchins) the reverse holds: the planktonic larva disperses and the sedentary adult grows and reproduces.
- Optimal use of habitats. Different stages exploit different resources, which can be most profitable at different sizes or in different seasons; tadpoles graze algae in ponds, frogs eat insects on land.

The cost is that each transition requires a reorganization of the body, a period of vulnerability, and constraints imposed by the need to function in both habitats. The timing of metamorphosis is itself a life history decision. Tadpoles in temporary ponds metamorphose earlier and at a smaller size when the pond dries quickly or food runs short, and later and larger when the aquatic habitat is good (Wilbur and Collins 1973): a larva should leave a habitat when its prospects there fall below those in the next stage.

### 19.3.2. The mu/g Rule

Werner and Gilliam (1984) made the last idea precise for animals that grow through a range of sizes and can choose among habitats in which growth and mortality depend on size.

**Theorem 19.3.1 (The mu/g Rule)** Let an individual grow from size $s_0$ to a size $S$ at which it matures, and let it be able to live, at each size, in one of several habitats $i$, with size-dependent growth rate $g_i(s) > 0$ and mortality rate $\mu_i(s)$. If the time taken does not matter (for example, all individuals mature at the same time of year whatever their route), the probability of surviving to size $S$ is maximized by being, at each size $s$, in the habitat that minimizes the ratio $\mu_i(s)/g_i(s)$. A switch from habitat 1 to habitat 2 should occur at the size $s^*$ at which

$$
\frac{\mu_1(s^*)}{g_1(s^*)} = \frac{\mu_2(s^*)}{g_2(s^*)} .
$$

**Proof** In habitat $i$, survival $l$ satisfies $\mathrm{d}\ln l/\mathrm{d}t = -\mu_i$ and size $\mathrm{d}s/\mathrm{d}t = g_i(s)$, so as a function of size, $\mathrm{d}\ln l/\mathrm{d}s = -\mu_i(s)/g_i(s)$. For a habitat sequence $i(s)$, the probability of surviving from $s_0$ to $S$ is

$$
l(S) = \exp\left(-\int_{s_0}^{S}\frac{\mu_{i(s)}(s)}{g_{i(s)}(s)}\,\mathrm{d}s\right),
$$
which is maximized by minimizing the integrand at every $s$. If the ratios of two habitats cross once, the optimal sequence switches at the crossing. $\square$

The rule says that a juvenile should accept a higher risk of death in a habitat only if its growth there is proportionally faster, because faster growth shortens the time spent at vulnerable sizes. Bluegill sunfish (*Lepomis macrochirus*) in Michigan lakes illustrate it. Small bluegills are vulnerable to largemouth bass (*Micropterus salmoides*), which are gape-limited; they stay in the vegetation of the littoral zone, where food is poorer but cover is good, and move to the open water, where zooplankton is more profitable, once they have outgrown the size that bass can eat. In lakes without bass, small bluegills use the open water as well, and in experiments the size at the shift increased with the density of predators (Werner et al. 1983; Werner and Hall 1988), as the rule predicts (Figure 4B). When the time to maturity also matters, as in seasonal environments or when maturity is reached at a fixed age rather than a fixed size, the rule must be modified, but it remains a good first approximation (Gilliam and Fraser 1987).

![The mu/g rule for ontogenetic habitat shifts (Theorem 19.3.1), for a fish growing from 5 to 150 mm with a constant mortality rate in a refuge habitat and gape-limited predation, declining with size, in open water, where growth is twice as fast. A: the ratio of mortality to growth rate in the two habitats against size (log axes); the switch size s* = 50 mm is where they cross. B: doubling predation in open water doubles the switch size to 100 mm. C: survival to 150 mm for fish that switch at a given size (line), maximal at s*, compared with staying in one habitat throughout (dashed)](./plots/habitat-switch.py)

### 19.3.3. Parasite Life Cycles

Many parasites have the most complex life cycles of all, with obligatory passage through two or more hosts. The pork tapeworm *Taenia solium* ([7.19.18](/7.19.18), [7.17.11](/7.17.11)) lives as an adult in the human intestine, its **definitive host**, and as a cysticercus in the muscles of a pig, its **intermediate host**; humans who swallow the eggs become accidental intermediate hosts, with cysticerci in the brain (neurocysticercosis) and other organs. Transmission from intermediate to definitive host is usually trophic: the definitive host eats the intermediate host. Such life cycles multiply opportunities for transmission and allow growth in a large definitive host, but each step has a low probability of success, which is compensated by enormous fecundity; and they create selection for parasites that change the behavior of the intermediate host so that it is eaten more often by the definitive host ([7.19.28](/7.19.28)). Breaking any link of the cycle (meat inspection, cooking, sanitation that keeps human feces away from pigs) controls the parasite, a direct application of life cycle analysis. Aphids, with alternation of hosts between a woody winter host and herbaceous summer hosts and **cyclical parthenogenesis** ([7.19.21](/7.19.21)), and rust fungi with up to five spore stages on two hosts, are other examples in which the life cycle, not the individual organism, is the unit of the life history.

## 19.4. Life Cycles in a Changing Climate

Because dormancy, migration and metamorphosis are timed by cues, they are among the life history traits most affected by climate change. The **phenology** of many species has advanced: a meta-analysis covering hundreds of species found that spring events (leafing, flowering, breeding, arrival of migrants) had advanced by 2.3 days per decade on average (Parmesan and Yohe 2003). Different species, and different trophic levels, respond to different cues: plants and insects mainly to temperature, many birds partly to day length, which does not change. Food chains then drift apart, a **phenological mismatch** ([7.18.20](/7.18.20)).

The best-known case involves the great tit (*Parus major*) and the winter moth (*Operophtera brumata*) in oak forests of the Netherlands. The caterpillar peak, which tits need for feeding their nestlings, advanced with warming springs much more than the laying date of the tits, so that the timing of breeding became increasingly mismatched and selection for earlier laying increased (Visser et al. 1998). In pied flycatchers (*Ficedula hypoleuca*), which winter in Africa and cannot sense spring temperatures in Europe, populations declined by about 90 % between 1987 and 2003 in Dutch areas where the food peak was earliest, but much less where it was late (Both et al. 2006). Long-distance migrants that time their departure by day length on the wintering grounds are particularly vulnerable.

A simple model shows how a growing mismatch turns into population decline. If the date of the food peak advances by $\delta_{\mathrm{f}}$ days per year and the breeding date of the consumer by $\delta_{\mathrm{b}} < \delta_{\mathrm{f}}$, the mismatch after $t$ years is $d = (\delta_{\mathrm{f}} - \delta_{\mathrm{b}})t$, and if breeding success declines with the mismatch as $\exp\bigl(-d^2/(2w^2)\bigr)$, where $w$ measures the breadth of the food peak, the population growth factor falls below 1 once the mismatch exceeds a threshold of the order of $w$ (Figure 5). Persistence depends on how fast the breeding date can follow, by plasticity or by evolution, which in turn depends on the heritability of laying date and on the strength of selection. The broad conclusions apply to all timed life histories: diapause thresholds evolve (the pitcher-plant mosquito), insects add generations in longer seasons (many bark beetles and moths are now bivoltine where they were univoltine; **voltinism**, [7.17.29](/7.17.29)), and species that cannot track the climate in time must track it in space ([7.19.17](/7.19.17)).

![An illustrative model of phenological mismatch. A: the food peak advances by 0.5 days per year and the time of peak food demand of the nestlings by 0.15 days per year, starting matched; the shading is the mismatch. B: mismatch (red, left axis) and population growth factor λ (purple, right axis), which falls below 1 when the mismatch exceeds about 6 days (breeding success declines as a Gaussian of the mismatch with a width of 8 days). C: population size for consumers that advance their breeding by 0.15 days per year (decline) and by 0.4 days per year (continued growth)](./plots/phenological-mismatch.py)

## Summary

| Strategy | Form | Control or rule | Examples |
|---|---|---|---|
| predictive dormancy (diapause) | arrested development at a fixed stage | photoperiod, critical photoperiod; switch when $mS(t + \tau) = 1$ (Proposition 19.1.1) | *Chorthippus* eggs, *Drosophila obscura*, silkworm |
| consequential dormancy | quiescence, enforced dormancy | direct response to adverse conditions | hibernating mammals' arousal, buried seeds |
| cryptobiosis | no measurable metabolism | desiccation, freezing, osmotic stress, anoxia | tardigrades, rotifers, *Artemia* cysts |
| torpor, hibernation, aestivation | controlled hypometabolism | food shortage, cold, drought | metaltail hummingbird, black bear, lungfish |
| seed bank | dormant seeds in the soil | innate, enforced and induced dormancy; $g^* = p - (1 - p)s/(Y - s)$ (Theorem 19.1.2) | desert annuals, arable weeds |
| migration | directed movement between regions | repeated, single return, multigenerational; partial migration (Proposition 19.2.1) | Beijing swift, godwit, humpback, monarch, planthoppers |
| complex life cycle | stages separated by metamorphosis | switch habitat where $\mu/g$ curves cross (Theorem 19.3.1) | insects, amphibians, bluegill, *Taenia* |

- Dormancy (Definition 19.1.1) is migration in time; predictive dormancy suits predictable seasons, consequential dormancy unpredictable ones.
- In a random environment, holding back part of the seeds or offspring is bet hedging; complete germination is driven extinct by the first bad year.
- Partial migration can be an evolutionarily stable mixture when the benefit of staying is shared; migratory populations depend on every place they visit.
- Complex life cycles (Definition 19.3.1) separate growth from dispersal and allow habitat shifts; the optimal size to switch habitats minimizes mortality per unit growth.
- Warming advances phenology at different rates across trophic levels; mismatch reduces breeding success and can cause population decline (pied flycatchers).

## Questions

1. In Proposition 19.1.1, take $\tau = 30$ days, an end of the season normally distributed with mean day 270 and standard deviation 10 days, and $m = 5$. Find the switch date. How does it change if warming shifts the mean end of the season to day 280, and why must the critical photoperiod then evolve?

   **Answer** $z_{1/5} = z_{0.2} = 0.84$, so $t^* = 270 - 30 + 8.4 \approx$ day 248. If the season ends 10 days later on average, $t^* \approx$ day 258. An insect that switches by day length must therefore switch at the day length of day 258 instead of day 248, which in late summer is shorter: the critical photoperiod must decrease. Since day length on a given date does not change with warming, a population that keeps its old critical photoperiod switches too early and wastes part of the season; selection favors shorter critical photoperiods, as observed in *Wyeomyia smithii*.

2. For Cohen's model with $Y = 10$, $s = 0.8$ and $p = 0.5$, compute $g^*$ and compare the long-run growth rates of $g = 1$, $g = g^*$ and $g = 0.5$.

   **Answer** $g^* = 0.5 - 0.5 \times 0.8/9.2 = 0.457$. For $g = 1$, $\lambda = 0$ in bad years and $G = -\infty$: extinction. For $g^*$: good years $\lambda = 4.57 + 0.43 = 5.0$, bad years $\lambda = 0.43$; $G = 0.5(\ln 5.0 + \ln 0.434) = 0.5(1.61 - 0.83) = 0.39$ per year. For $g = 0.5$: good $5.4$, bad $0.4$; $G = 0.5(1.69 - 0.92) = 0.385$, slightly lower. The optimum is flat near $g^*$, so moderate departures cost little, but complete germination is fatal.

3. Show that in the model of Proposition 19.2.1 the stable fraction of residents decreases with winter severity, and explain the prediction that milder winters should increase the proportion of residents in partially migratory birds.

   **Answer** In the mixed region $f^* = 1 - (S_{\mathrm{m}}\mathrm{e}^{w} - 1)/a$, and $\mathrm{d}f^*/\mathrm{d}w = -S_{\mathrm{m}}\mathrm{e}^{w}/a < 0$. Milder winters (smaller $w$) raise resident survival, so the fraction of residents at which both tactics have equal fitness rises; if migration is genetically or conditionally determined, the population evolves or shifts toward more residents. Increasing residency of blackbirds, robins and blackcaps in Europe in recent decades is consistent with this, although other factors (food in gardens, changes in migrant survival) also act.

4. Derive the switch size in the example of Figure 4 ($\mu_1 = 0.002$, $g_1 = 0.02s$; $\mu_2 = 0.2/s$, $g_2 = 0.04s$) and show that it scales with the density of predators in open water.

   **Answer** $\mu_1/g_1 = 0.1/s$ and $\mu_2/g_2 = 5/s^2$. Equality gives $0.1/s = 5/s^2$, so $s^* = 50$ mm. If predation in open water is multiplied by $k$, $\mu_2/g_2 = 5k/s^2$ and $s^* = 50k$: the switch size is proportional to predator density. For sizes below $s^*$ the open water has the higher $\mu/g$ (because $5k/s^2$ falls faster than $0.1/s$ as $s$ increases), so small fish should stay in the refuge.

5. (Open question) A conservation program protects the breeding grounds of a declining migratory shorebird. Which data would you collect to decide whether the population is limited elsewhere in its annual cycle, and how would you use them?

   **Answer** Key points: estimate vital rates by season (breeding success, survival on the wintering grounds and during migration) from marked or tracked individuals, using geolocators or GPS tags to map routes and stopovers and mark–recapture models to estimate survival by period; build a seasonal matrix model ([7.19.14](/7.19.14)) and compute the elasticities of λ to each rate; test for carry-over effects (condition at departure from stopovers predicting breeding success); compare trends with habitat change along the flyway (for East Asian shorebirds, loss of Yellow Sea mudflats); and identify migratory connectivity, i.e. whether birds from a given breeding area use particular stopovers. If adult survival during migration has the largest elasticity and has declined, protection must extend to stopover sites, as for the spoon-billed sandpiper and great knot.
