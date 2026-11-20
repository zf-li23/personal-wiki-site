---
title: Community Assembly, Metacommunities and Neutral Theory
description: "How local communities are assembled from regional species pools: dispersal, environmental and biotic filters, Vellend's four processes, priority effects and assembly rules; metacommunities and the patch-dynamics, species-sorting, mass-effects and neutral paradigms, with a mass-effects model of alpha, beta and gamma diversity; Hubbell's unified neutral theory: zero-sum Moran dynamics, ecological drift, speciation and the fundamental biodiversity number, the Ewens sampling formula and Fisher's log-series, dispersal limitation and the beta-binomial local community, the Barro Colorado Island fit and the criticisms; negative density dependence and the Janzen–Connell hypothesis; niche and neutral as ends of a continuum."
---

The preceding chapters explained the composition of a community by what happens inside it: competition ([7.19.22](/7.19.22)–[7.19.23](/7.19.23)), predation ([7.19.24](/7.19.24)–[7.19.27](/7.19.27)), mutualism ([7.19.29](/7.19.29)), disturbance ([7.19.33](/7.19.33)) and succession ([7.19.36](/7.19.36)). But a patch of forest or a pond can contain only species that have arrived there, and the species that can arrive are those of the surrounding region, whose composition reflects speciation, extinction and history on much larger scales. This chapter places the local community in its regional context. Section 37.1 describes community assembly as a sequence of filters acting on a regional species pool, and the role of the order of arrival. Section 37.2 introduces metacommunities, sets of local communities linked by dispersal, and shows with a model how the rate of dispersal changes diversity at local and regional scales. Section 37.3 develops the most radical regional theory, Hubbell's unified neutral theory, in which species do not differ at all and community composition is the outcome of random birth, death, dispersal and speciation; its mathematics is that of the neutral theory of population genetics ([7.10.7](/7.10.7)), and we derive its main predictions. Section 37.4 turns to a mechanism that breaks neutrality in a specific way, negative density dependence caused by natural enemies (the Janzen–Connell hypothesis), and Section 37.5 places niche and neutral explanations on a common scale, that of modern coexistence theory ([7.19.23](/7.19.23)). The patterns that these theories try to explain, species abundance distributions and diversity indices, are described in [7.19.31](/7.19.31); the species–area relationship and island biogeography, the other classical regional theory, in [7.19.34](/7.19.34).

## 37.1. Community Assembly

### 37.1.1. Species Pools and Filters

**Definition 37.1.1 (Community Assembly)** **Community assembly** is the set of processes by which species from a regional pool colonize a site, persist and interact, so that a local **community** of a particular composition and relative abundance arises. The **species pool** of a site is the set of species available to colonize it: the regional pool is all species of the region; the geographic pool, those able to reach the site; the habitat pool, those able to persist under its abiotic conditions.

A common way of organizing assembly is as a sequence of filters (Belyea and Lancaster 1999):

1. *Dispersal constraints.* Of the regional pool, only species whose propagules reach the site within the relevant time can be present. Remote islands, isolated ponds and the interiors of large forest fragments receive few colonists, and their communities lack species that would thrive there.
2. *Environmental filtering*: species unable to survive and reproduce under the abiotic conditions of the site (temperature, salinity, soil pH, flooding) are excluded, whatever their competitors. Environmental filtering makes the species of a site more similar in the traits that confer tolerance than a random draw from the pool: the plants of a salt marsh all tolerate salinity, those of a serpentine outcrop all tolerate nickel and low calcium ([7.19.5](/7.19.5)).
3. *Internal dynamics.* Of the species that arrive and tolerate the conditions, interactions decide which persist and in what numbers: competitors may exclude each other, especially if they are similar ([7.19.23](/7.19.23)); predators, pathogens and mutualists may exclude or admit species.

Filters have consequences that can be detected in data. Environmental filtering tends to produce *trait clustering* (coexisting species more similar than expected), whereas competition among similar species produces *trait overdispersion* (coexisting species more different than expected); comparison with null models that draw communities at random from the pool ([7.19.33](/7.19.33)) is the standard test. The inference is not unambiguous: competition can also cause clustering when it excludes species that are weak competitors for reasons unrelated to niche differences (Mayfield and Levine 2010).

Vellend (2010, 2016) proposed that all processes of community ecology can be reduced to four, in direct analogy with the four processes of population genetics:

| Community process | Population-genetic analogue | Examples |
|---|---|---|
| Selection: deterministic fitness differences among species | natural selection | competitive exclusion, environmental filtering, frequency-dependent predation |
| Ecological drift: random changes in relative abundance | **genetic drift** ([7.4.23](/7.4.23)) | chance births and deaths in small communities |
| Speciation: origin of new species | mutation | adaptive radiation, which builds the regional pool |
| Dispersal: movement of organisms among communities | gene flow | colonization, mass effects, dispersal limitation |

Most theories emphasize one or two of these. Classical niche theory is a theory of selection; island biogeography ([7.19.34](/7.19.34)) a theory of dispersal and extinction; neutral theory (Section 37.3) a theory of drift, dispersal and speciation without selection.

### 37.1.2. Priority Effects and Assembly Rules

The filters do not specify the order in which species arrive, and the order often matters.

**Definition 37.1.2 (Priority Effect)** A **priority effect** is an effect of the order or timing of arrival of species on the outcome of their interactions, and hence on community composition.

In reef fishes of the genus *Thalassoma* at Moorea, *T. quinquevittatum* was the superior competitor when individuals of both species arrived simultaneously, but when the arrivals were staggered by 5 or 12 days the resident species fared best, whichever it was (Geange and Stier 2009). Fukami (2015) distinguished two mechanisms. In *niche preemption* early arrivals take up resources or space and reduce what is available to later ones; this is the strongly inhibitory case, and the two-species Lotka–Volterra model with $\alpha\beta > 1$ is its simplest form: with bistability ([7.19.22](/7.19.22)) the species that is first abundant wins. In *niche modification* early arrivals change the kind of niches available, for example by altering soil chemistry or nectar composition; the late arrivals that benefit are different from those that suffer. In nectar of the hummingbird-pollinated shrub *Mimulus aurantiacus*, yeasts and bacteria that arrive first change the sugar and amino acid content of the nectar and so determine which microbes can follow, and the resulting communities differ in how attractive the flowers are to pollinators (Peay, Belisle and Fukami 2012; Vannette, Gauthier and Fukami 2013).

Priority effects make assembly *historically contingent*: identical sites colonized by the same pool in different orders can end in different stable communities, a form of the **alternative stable states** treated in [7.19.39](/7.19.39). They are strongest when species arrive at intervals that are long relative to their generation time, when residents grow fast and when niches overlap.

Diamond (1975) proposed *assembly rules* for the birds of the Bismarck Archipelago: certain combinations of species were "forbidden", species pairs occurred in a checkerboard (each on different islands, never together), and the species present on an island depended on its size in a regular way. Connor and Simberloff (1979) showed that many of these patterns are expected even if species colonize islands independently, once island area and species frequency are taken into account; the resulting controversy produced the null-model methods of community ecology ([7.19.33](/7.19.33)). Later analyses with better null models found more checkerboards than expected in the Bismarck birds, many of them between congeners, so that competitive exclusion is a likely contributor (Gotelli and McCabe 2002), but the debate showed that assembly rules must be stated as testable deviations from a random expectation.

## 37.2. Metacommunities

### 37.2.1. Local Communities Linked by Dispersal

The regional pool is itself made of local communities. A **metapopulation** ([7.19.16](/7.19.16)) is a set of populations of one species linked by dispersal; the same idea applied to many species gives the metacommunity.

**Definition 37.2.1 (Metacommunity)** A **metacommunity** is a set of local communities linked by the dispersal of individuals of multiple, potentially interacting species (Wilson 1992; Leibold et al. 2004).

The concept makes explicit that the composition of a local community depends on processes at two scales: local interactions and the environment, and regional dispersal, extinction and colonization. A metacommunity has diversity at three scales: within local communities (**alpha diversity**), among them (**beta diversity**) and in the region as a whole (**gamma diversity**); the definitions and the partitioning of diversity among scales are given in [7.19.31](/7.19.31).

### 37.2.2. Four Paradigms

Leibold et al. (2004) classified metacommunity theories by three questions: are the patches environmentally the same or different; do species differ in their niches; and is dispersal slow or fast compared with local dynamics?

| Paradigm | Patches | Species | Dispersal | Mechanism of regional coexistence |
|---|---|---|---|---|
| Patch dynamics | identical | differ in competitive and colonizing ability | slow to moderate | **competition–colonization trade-off** ([7.19.16](/7.19.16)): good competitors win in a patch, good colonizers reach empty patches first |
| Species sorting | different | differ in niches | slow enough not to affect local outcomes, fast enough to reach all suitable patches | each species dominates the patches whose conditions suit it; composition tracks environment |
| Mass effects | different | differ in niches | fast | **source–sink dynamics** ([7.19.16](/7.19.16)): immigration from patches where a species is favored maintains it where it would be excluded |
| Neutral | identical (or irrelevant) | identical | any | none needed: drift, dispersal and speciation balance (Section 37.3) |

The paradigms are idealizations, and real metacommunities combine them; their use is to identify which processes leave which signatures. Under species sorting, composition is correlated with environment but not with distance once environment is accounted for. Under dispersal limitation (patch dynamics or neutral dynamics), composition becomes less similar with distance even in uniform environments (*distance decay* of similarity). Under mass effects, species occur in patches where they cannot persist alone, and local composition depends on that of neighboring patches. Statistical partitioning of the variation in composition into environmental and spatial components (variation partitioning, often with distance-based eigenvectors) is the common empirical approach, though it cannot by itself separate the processes cleanly.

The patch-dynamics paradigm has experimental support in microcosms. Cadotte et al. (2006) measured the time that 13 species of protozoans and rotifers took to colonize a series of connected bottles and, separately, their competitive ability in all pairwise combinations; the two were negatively correlated, as the trade-off requires.

### 37.2.3. A Mass-Effects Model

The effect of dispersal rate on diversity at different scales can be seen in a model of Mouquet and Loreau (2003). There are $N$ patches, each with many sites for sessile individuals (plants, corals), all occupied. Let $P_{ik}$ be the proportion of sites in patch $k$ held by species $i$, so that $\sum_i P_{ik} = 1$. Individuals die at rate $\mu$, and each vacant site is won by a propagule drawn from the local propagule rain, weighted by competitive ability. A fraction $a$ of the propagules produced in a patch disperses evenly to the other patches, so the propagule rain of species $i$ in patch $k$ is

$$
R_{ik} = (1 - a)P_{ik} + \frac{a}{N - 1}\sum_{l \ne k} P_{il},
$$
and with $c_{ik}$ the competitive ability of species $i$ in patch $k$,

$$
\frac{\mathrm{d}P_{ik}}{\mathrm{d}t} = \mu\left(\frac{c_{ik}R_{ik}}{\sum_j c_{jk}R_{jk}} - P_{ik}\right). \tag{37.1}
$$
Each patch has its own competitive hierarchy: species $i$ is the best competitor in patch $i$, and its ability declines with the distance in "environment" between patches.

**Proposition 37.2.1 (Limits of No and Complete Dispersal)** In model (37.1):

1. if $a = 0$, the only stable equilibrium in each patch is the monoculture of the species with the largest $c_{ik}$ there, so that alpha richness is 1 and gamma richness equals the number of species that are best somewhere;
2. if $a = 1$ and the number of patches is large, the propagule rain of species $i$ is the same in all patches, competition becomes a lottery over the whole region, and every species that persists is present in every patch: alpha and gamma richness become equal and beta diversity vanishes.

**Proof** 1. With $a = 0$, patch $k$ is isolated and $R_{ik} = P_{ik}$. Let $c_{1k}$ be the largest ability. For every other species, $\mathrm{d}\ln(P_{ik}/P_{1k})/\mathrm{d}t$ can be computed from (37.1): writing $W = \sum_j c_{jk}P_{jk}$, $\dot P_{ik}/P_{ik} = \mu(c_{ik}/W - 1)$, so $\mathrm{d}\ln(P_{ik}/P_{1k})/\mathrm{d}t = \mu(c_{ik} - c_{1k})/W < 0$. Hence $P_{ik}/P_{1k} \to 0$ and, since the proportions sum to 1, $P_{1k} \to 1$ whenever $P_{1k}(0) > 0$. 2. With $a = 1$, $R_{ik} = (Np_i - P_{ik})/(N - 1)$, which for large $N$ is $p_i$ in every patch; the local abundance is then $P_{ik} = c_{ik}p_i/\sum_j c_{jk}p_j$ at quasi-equilibrium, which is positive in every patch whenever $p_i > 0$, and the regional dynamics $\dot p_i = \mu(\frac1N\sum_k c_{ik}p_i/\sum_j c_{jk}p_j - p_i)$ involve only regional abundances. $\square$

Which species survive the regional lottery depends on their abilities averaged over patches; in the example of Figure 1, five of the twelve are lost.

Between these limits the outcome must be computed (Figure 1). At very low dispersal each patch is a monoculture of its locally best species, alpha richness is 1 and beta diversity maximal. As dispersal increases, immigrants from patches where a species is favored rescue it from exclusion where it is inferior: alpha richness rises, a mass effect. At high dispersal the regional lottery takes over, the regionally best competitors spread everywhere, and both alpha and gamma richness fall. Local diversity is therefore maximal at intermediate dispersal, regional diversity declines monotonically at high dispersal, and beta diversity declines throughout. The same hump in alpha diversity appears in experiments with connected microcosms (Cadotte 2006) and is one reason why corridors and other increases in connectivity ([7.19.49](/7.19.49)) can reduce regional diversity if they homogenize communities.

![Dispersal and diversity in a mass-effects metacommunity, Eq. (37.1), after Mouquet and Loreau (2003): 12 species in 12 patches, species i best in patch i, competitive ability declining with the cyclic distance between patches (c = exp(−0.35 d)) and varying slightly among species. A: equilibrium richness as a function of the proportion a of propagules that disperse: alpha (mean number of species per patch, green) rises from 1 to a maximum near a = 0.4 and then falls, gamma (whole metacommunity, blue) stays at 12 until dispersal is very high and then falls, and additive beta diversity (gamma − alpha, dashed) declines throughout. B: relative abundances in patch 1: its locally best species (blue) dominates at low dispersal and loses ground to immigrants as dispersal increases](./plots/metacommunity-dispersal.py)

## 37.3. The Unified Neutral Theory

### 37.3.1. Assumptions

A 50 ha plot on Barro Colorado Island (BCI) in Panama, mapped every five years since 1982, contains about 21 000 trees of at least 10 cm trunk diameter belonging to some 230 species, and more than 300 species when saplings are included. Explaining the coexistence of so many species by niche differences requires a correspondingly large number of niche axes or of stabilizing mechanisms. Hubbell (1979, 2001) asked instead how much of the structure of such communities could be explained if species did not differ at all.

**Definition 37.3.1 (Unified Neutral Theory of Biodiversity)** The **unified neutral theory of biodiversity** (Hubbell 2001) is a stochastic theory of community composition based on three assumptions:

1. *Ecological equivalence*: all individuals of all species of a trophically similar community (a guild, such as the canopy trees of a forest) have the same per capita rates of birth, death, dispersal and speciation;
2. *Zero sum*: the community is saturated, with a fixed number $J$ of individuals; every death is immediately followed by the replacement of the dead individual;
3. *Two scales*: a local community of $J$ individuals receives immigrants from a large metacommunity of $J_M$ individuals, in which new species arise by speciation.

The theory is "unified" because it predicts both the relative abundances of species (as in the theories of Fisher and Preston, [7.19.31](/7.19.31)) and the dependence of richness on area and isolation (as in island biogeography, [7.19.34](/7.19.34)) from a single mechanism. It is the community analogue of the **neutral theory of molecular evolution** ([7.4.23](/7.4.23)), with species in place of alleles, speciation in place of mutation and immigration in place of gene flow. The zero-sum assumption is the essential simplification: it makes the abundances of species dependent, so that one species can increase only if others decrease, exactly as allele frequencies in a population of fixed size.

### 37.3.2. Ecological Drift

Consider first a closed local community without immigration or speciation. Its dynamics are those of the neutral **Moran model** ([7.10.7](/7.10.7)): at each step one individual, chosen at random, dies, and is replaced by the offspring of an individual chosen at random among the $J - 1$ survivors. $J$ steps make one generation.

**Definition 37.3.2 (Ecological Drift)** **Ecological drift** is random change in the relative abundances of species caused by the stochasticity of birth, death and reproduction in a community of finite size, in the absence of fitness differences among species.

**Proposition 37.3.1 (Neutral Drift in a Closed Community)** In a closed neutral community of $J$ individuals, let $n$ be the abundance of a species and $p = n/J$ its relative abundance.

1. $n$ is a martingale: $\mathbb{E}[n_{t+1} \mid n_t] = n_t$; the species eventually either goes extinct or takes over the whole community, and it takes over with probability $p$.
2. In the diffusion approximation, the expected time until the species is lost or fixed is
$$
T(p) = -J\,[\,p\ln p + (1 - p)\ln(1 - p)\,] \tag{37.2}
$$
generations; for a species of a single individual, $T(1/J) \approx 1 + \ln J$.
3. With $S_0$ species initially, richness declines to 1; the expected time to monodominance is of the order of $J$ generations.

**Proof** 1. In one step the abundance increases by 1 if a non-member dies and a member reproduces, with probability $\frac{J - n}{J}\cdot\frac{n}{J - 1}$, and decreases by 1 if a member dies and a non-member reproduces, with probability $\frac{n}{J}\cdot\frac{J - n}{J - 1}$; these are equal, so the expected change is 0. A bounded martingale converges, and because every state $0 < n < J$ is left with positive probability, it converges to 0 or $J$; optional stopping gives $\mathbb{E}[n_\infty] = n_0$, hence $\mathbb{P}(n_\infty = J) = n_0/J = p$. 2. Per step the relative abundance changes by $\pm 1/J$, each with probability about $p(1 - p)$, so its variance per generation of $J$ steps is $J\cdot 2p(1 - p)/J^2 = 2p(1 - p)/J$, and the mean change is zero. The expected absorption time of a diffusion with zero drift and variance $v(p)$ per unit time solves $\frac12 v(p)T''(p) = -1$ with $T(0) = T(1) = 0$, here $p(1 - p)T'' = -J$, whose solution is (37.2). With $p = 1/J$, $-J[(1/J)\ln(1/J) + (1 - 1/J)\ln(1 - 1/J)] \approx \ln J + 1$. 3. Going backward in time, the ancestral lineages of the $J$ individuals coalesce as in the **coalescent** ([7.10.7](/7.10.7)); all individuals descend from a single ancestor after an expected time of the order of $J$ generations (the time to the most recent common ancestor), and at that time the community is a single species. $\square$

Drift is fast for rare species and slow for common ones. Most species that start with a few individuals disappear within a few generations, while the last two or three common species may persist for hundreds of generations (Figure 2A). For a forest of 21 000 trees with a generation time of about 50 years, monodominance would take of the order of a million years: drift alone is slow enough that a neutral community, replenished by speciation and immigration, can hold many species for a long time.

### 37.3.3. Speciation and the Fundamental Biodiversity Number

In the metacommunity, of $J_M$ individuals, each replacement is with probability $\nu$ an individual of a new species (point mutation speciation: a single individual founds a species) and otherwise the offspring of a random individual. Speciation is the analogue of mutation in the infinite-alleles model, and the equilibrium between loss by drift and gain by speciation is described by one parameter.

**Definition 37.3.3 (Fundamental Biodiversity Number)** The **fundamental biodiversity number** $\theta$ of a neutral metacommunity is the scaled speciation rate. For the Moran dynamics described here the exact value is $\theta = (J_M - 1)\nu/(1 - \nu) \approx J_M\nu$ (the expected number of new species per generation); Hubbell (2001) wrote $\theta = 2J_M\nu$, and other conventions differ by such constant factors, which reflect how generations are counted. All equilibrium predictions depend on $J_M$ and $\nu$ only through $\theta$.

The genealogy of a sample gives the equilibrium distribution. Trace the ancestors of $n$ individuals back in time. Their lineages coalesce in pairs when two of them share a parent, and a lineage ends when it reaches the individual that founded its species (a speciation event), because beyond that point it no longer carries information about the species identity of the sample. With $k$ lineages the next event is a speciation with probability $\theta/(\theta + k - 1)$ and a coalescence otherwise, exactly as in the **infinite-alleles model** ([7.10.7](/7.10.7)). Equivalently, the sample can be built forward by an urn scheme (Hoppe 1984): the first individual belongs to a new species; the $(k + 1)$-th belongs to a new species with probability $\theta/(\theta + k)$ and otherwise to the species of one of the previous $k$ individuals chosen at random.

**Theorem 37.3.1 (Ewens Sampling Formula)** Let $a_j$ be the number of species represented by exactly $j$ individuals in a random sample of $n$ individuals from a neutral metacommunity at equilibrium, so that $\sum_j ja_j = n$. Then

$$
\mathbb{P}(a_1, \dots, a_n) = \frac{n!}{\theta(\theta + 1)\cdots(\theta + n - 1)}\prod_{j=1}^n\frac{(\theta/j)^{a_j}}{a_j!}. \tag{37.3}
$$
The number of species $S_n$ in the sample is a sum of independent Bernoulli variables with success probabilities $\theta/(\theta + k)$, $k = 0, \dots, n - 1$, so that

$$
\mathbb{E}[S_n] = \sum_{k=0}^{n-1}\frac{\theta}{\theta + k} \approx \theta\ln\left(1 + \frac{n}{\theta}\right), \qquad \operatorname{Var}(S_n) = \sum_{k=0}^{n-1}\frac{\theta k}{(\theta + k)^2}. \tag{37.4}
$$
Given $S_n$, the partition $(a_j)$ does not depend on $\theta$: $S_n$ is a sufficient statistic for $\theta$.

**Proof** (sketch) In the urn, the probability of any particular sequence of species labels depends only on the resulting partition: each of the $S_n$ new species contributes a factor $\theta$, a species that ends with $j$ individuals contributes the factors $1\cdot2\cdots(j - 1) = (j - 1)!$ for its repeated draws, and the denominators contribute $\theta(\theta + 1)\cdots(\theta + n - 1)$. A given grouping of the $n$ (numbered) individuals into species thus has probability $\theta^{S_n}\prod_{j}((j - 1)!)^{a_j}/\theta^{(n)}$, with $\theta^{(n)} = \theta(\theta + 1)\cdots(\theta + n - 1)$ the rising factorial. The number of groupings of $n$ numbered individuals into $a_j$ groups of size $j$ ($j = 1, 2, \dots$) is $n!/\prod_j (j!)^{a_j}a_j!$. Multiplying, and using $(j - 1)!/j! = 1/j$, gives (37.3) (Ewens 1972). The $k$-th draw is a new species with probability $\theta/(\theta + k)$ independently of the earlier draws' labels, which gives the Bernoulli representation and (37.4); the approximation is $\sum_{k<n}\theta/(\theta + k) \approx \int_0^n \theta\,\mathrm{d}k/(\theta + k)$. Finally $\theta$ enters (37.3) only through $\theta^{S_n}/\theta^{(n)}$, so the conditional distribution of the partition given $S_n$ is free of $\theta$. $\square$

The expected abundance distribution follows from (37.3). The expected number of species with exactly $j$ individuals in a sample of $n$ is

$$
\mathbb{E}[a_j] = \frac{\theta}{j}\,\frac{n!}{(n - j)!}\,\frac{\Gamma(n - j + \theta)}{\Gamma(n + \theta)} \approx \frac{\theta}{j}\,x^j, \qquad x = \frac{n}{n + \theta}, \tag{37.5}
$$
for large $n$. This is *Fisher's log-series* (Fisher, Corbet and Williams 1943), the distribution that Fisher fitted to Malaysian butterflies and Williams to moths caught in light traps at Rothamsted: $S(j) = \alpha x^j/j$, with $S = -\alpha\ln(1 - x)$ species and $n = \alpha x/(1 - x)$ individuals. The neutral theory therefore explains Fisher's *diversity index* $\alpha$, an empirical constant for sixty years, as the fundamental biodiversity number: $\alpha = \theta$. In the limit of a very large metacommunity the density of species with relative abundance in $(x, x + \mathrm{d}x)$ is

$$
\phi(x)\,\mathrm{d}x = \theta\,x^{-1}(1 - x)^{\theta - 1}\,\mathrm{d}x, \qquad 0 < x < 1, \tag{37.6}
$$
the frequency spectrum of the infinite-alleles model (Ewens 1972): very many rare species, a few common ones, and an expected number $\theta$ of species per factor $\mathrm{e}$ of abundance at low abundance.

In a metacommunity of fixed size, richness approaches the equilibrium (37.4) from any initial state, losses by drift balancing gains by speciation (Figure 2B), and fluctuates around it: a neutral community is dynamic at equilibrium, with continual turnover of species.

![Ecological drift in a neutral community (Moran process). A: a closed community of J = 400 individuals that starts with 20 species of 20 individuals each; six runs (colored) and their mean (dashed), on a logarithmic time axis. Species are lost one by one, rapidly at first, and the community drifts towards a single species on a time scale of hundreds of generations. B: the same community with speciation probability ν = 0.025 per replacement (θ = 10.2), starting from one species: richness rises and then fluctuates around the equilibrium expectation E[S] = Σ θ/(θ + i) = 38.3 of Theorem 37.3.1 (dashed)](./plots/neutral-drift.py)

### 37.3.4. Dispersal Limitation and the Local Community

A local community, such as the BCI plot, is not a random sample of the metacommunity: most replacements are offspring of local trees, and immigrants arrive at a limited rate. In Hubbell's model each replacement in the local community is, with probability $m$, an immigrant drawn from the metacommunity and, with probability $1 - m$, the offspring of a random local survivor.

**Proposition 37.3.2 (Local Abundance under Dispersal Limitation)** Let a species have relative abundance $x$ in the metacommunity, assumed constant on the time scale of local dynamics. In a local community of $J$ individuals with immigration probability $m$, its abundance $n$ has the stationary distribution

$$
\mathbb{P}(n) = \binom{J}{n}\frac{\mathrm{B}(n + Ix,\ J - n + I(1 - x))}{\mathrm{B}(Ix,\ I(1 - x))}, \qquad I = \frac{m(J - 1)}{1 - m}, \tag{37.7}
$$
the beta-binomial distribution with parameters $J$, $Ix$ and $I(1 - x)$, where $\mathrm{B}$ is the Beta function. Its mean is $Jx$; as $m \to 1$ it tends to the binomial $\mathrm{Bin}(J, x)$ (random sampling), and as $m \to 0$ the community becomes dominated by few species.

**Proof** The abundance is a birth–death chain on $\{0, \dots, J\}$. It increases by one if a non-member dies and is replaced by a member, an immigrant or a local offspring:
$$
\lambda_n = \frac{J - n}{J}\left(mx + (1 - m)\frac{n}{J - 1}\right),
$$
and decreases by one if a member dies and is replaced by a non-member:
$$
\mu_n = \frac{n}{J}\left(m(1 - x) + (1 - m)\frac{J - n}{J - 1}\right).
$$
A birth–death chain has a reversible stationary distribution with $\mathbb{P}(n + 1)/\mathbb{P}(n) = \lambda_n/\mu_{n+1}$. Multiplying numerator and denominator by $(J - 1)/(1 - m)$,
$$
\frac{\mathbb{P}(n + 1)}{\mathbb{P}(n)} = \frac{(J - n)(n + Ix)}{(n + 1)(J - n - 1 + I(1 - x))},
$$
which is the ratio of successive terms of (37.7), since $\mathrm{B}(a + 1, b - 1)/\mathrm{B}(a, b) = a/(b - 1)$. The mean of the beta-binomial is $J\cdot Ix/(Ix + I(1 - x)) = Jx$. As $m \to 1$, $I \to \infty$ and the beta mixing distribution concentrates at $x$, giving the binomial; as $m \to 0$, $I \to 0$ and the beta-binomial puts its mass near $n = 0$ and $n = J$. $\square$

The parameter $I$ is the effective number of immigrants competing for each vacancy against local offspring. Combining (37.6) and (37.7), the expected number of species with $n$ individuals in the local community is

$$
\mathbb{E}[S_n] = \int_0^1 \theta\,x^{-1}(1 - x)^{\theta - 1}\binom{J}{n}\frac{\mathrm{B}(n + Ix,\ J - n + I(1 - x))}{\mathrm{B}(Ix,\ I(1 - x))}\,\mathrm{d}x, \tag{37.8}
$$
the result of Volkov et al. (2003) and Etienne and Alonso (2005) for Hubbell's *zero-sum multinomial* distribution, which Hubbell had obtained by simulation. Three parameters determine it: $J$ (measured), $\theta$ and $m$ (fitted).

Dispersal limitation changes the shape of the abundance distribution (Figure 3). Without it ($m \to 1$) the local community is a log-series sample, with its mode in the lowest abundance class. With limited immigration, rare species of the metacommunity are less likely to be present at all, while species already present increase by local reproduction: the number of singletons falls and the distribution in octaves of abundance acquires an interior mode, resembling Preston's lognormal distribution ([7.19.31](/7.19.31)). Neutral theory thus explains both classical distributions of relative abundance as limits of one model, distinguished by the rate of immigration. For the 21 000 trees of the BCI plot, Hubbell obtained a good fit with $\theta \approx 50$ and $m \approx 0.1$, which predicts about 235 species, close to the number observed; the fitted lognormal and the neutral distribution are almost indistinguishable over most of the range (Figure 3A).

![Species abundance distributions of the neutral theory, computed from Eq. (37.8) for J = 21 000 individuals and θ = 50, the size and parameter of the Barro Colorado Island tree plot. A: Preston plot, the expected number of species in octaves of abundance (1, 2–3, 4–7, …). With immigration probability m = 0.1 (bars, 235 species) the distribution has an interior mode and is closely matched by a lognormal (dashed, least-squares fit); without dispersal limitation (m = 1) it is Fisher's log-series (302 species, most in the lowest class); with strong dispersal limitation (m = 0.01) richness falls to 152 and rare species become scarcer. B: the same distributions as rank–abundance curves](./plots/neutral-sad.py)

### 37.3.5. Tests and Criticisms

Neutral theory makes precise predictions from few parameters, and that has made it the most tested null model of community ecology. The results are mixed.

- *Abundance distributions are weak tests.* The neutral distribution fits many tree, coral-reef and bird data sets well, but so do lognormal, niche-apportionment and other models with as many parameters; McGill (2003) found the lognormal as good as or better than the neutral fit for BCI. Distributions of abundance carry too little information to discriminate mechanisms, a conclusion confirmed by the fact that niche models with many niches can produce neutral-looking distributions (Chisholm and Pacala 2010).
- *Dynamics.* Neutrality predicts that changes in abundance are unrelated to abundance and to species identity. In BCI and other forest plots, changes over decades are often too small and too regular for drift: populations of common species are more stable than drift allows, and the per capita growth of species declines with their own abundance (negative density dependence, Section 37.4), which drift excludes.
- *Time scales.* For a common species of a large metacommunity to have reached its abundance by drift, it must be very old: under neutrality the expected age of a species with relative abundance $x$ is about $-J_Mx\ln x/(1 - x)$ generations (the Kimura–Ohta result for neutral alleles, in the Moran scaling), and for the abundant species of tropical forests this exceeds the known ages of tree species and genera by orders of magnitude (Ricklefs 2006; Leigh 2007). Point-mutation speciation also produces too many young, rare species. Models with *protracted speciation*, in which new species take time to become distinct, reduce but do not remove this problem (Rosindell et al. 2010).
- *Species differ.* Tree species of BCI differ conspicuously in shade tolerance, growth rate, drought sensitivity and susceptibility to pathogens, and these differences predict their distribution over soil nutrients and topography (Condit et al. 2013); the "unified" assumption of equivalence is false for any real guild.

What remains is the value of neutral theory as a null model with mechanism (Rosindell et al. 2012). It shows which patterns require no niche differences, it brings drift, dispersal limitation and speciation into community ecology, and it predicts phenomena that niche theory had ignored, such as the decay of similarity between plots with distance (Condit et al. 2002) and the relationship between diversity and area produced purely by dispersal limitation. Its success with static patterns and its failure with dynamics also teach a methodological lesson: patterns that many mechanisms predict cannot decide between them.

## 37.4. Negative Density Dependence and the Janzen–Connell Hypothesis

### 37.4.1. The Hypothesis

The strongest departure from neutrality in tropical forests is that individuals suffer more when surrounded by their own species. Janzen (1970) and Connell (1971) independently proposed a mechanism.

**Definition 37.4.1 (Janzen–Connell Hypothesis)** The **Janzen–Connell hypothesis** states that host-specific natural enemies (seed predators, herbivores and pathogens) that accumulate near adult plants, or where seeds and seedlings of their host are dense, reduce the survival of offspring near conspecific adults, and that this conspecific negative density and distance dependence prevents any species from monopolizing space and so maintains diversity.

Janzen's graphical argument is quantitative. Let the density of seeds at distance $r$ from the parent decline as $D(r) = \mathrm{e}^{-r/a}$, and let the probability that a seed or seedling escapes enemies, which are concentrated near the parent, rise as $E(r) = 1 - \mathrm{e}^{-r/b}$. The expected density of recruits, the population recruitment curve $D(r)E(r)$, is zero at the parent, rises, and falls again. Setting its derivative to zero,

$$
-\frac1a\,\mathrm{e}^{-r/a}\left(1 - \mathrm{e}^{-r/b}\right) + \frac1b\,\mathrm{e}^{-r/a}\mathrm{e}^{-r/b} = 0 \quad\Longrightarrow\quad r^* = b\ln\frac{a + b}{b}, \tag{37.9}
$$
the distance at which recruitment is maximal (Figure 4A). The space under and close to each adult is left free for other species: a tree is less likely to be replaced by its own species than by others.

At the community level the mechanism makes the per capita recruitment of a species decline with its abundance, which is a **stabilizing mechanism** in the sense of [7.19.23](/7.19.23): a species that becomes rare escapes its specialist enemies and recovers, one that becomes common suffers more. In a lottery model in which a vacant site is won with probability proportional to $n_i\,\mathrm{e}^{-kn_i/J}$ rather than to $n_i$, a species at low relative abundance has an advantage, and all species can be maintained indefinitely, whereas in the neutral lottery the same community loses species steadily by drift (Figure 4B). The requirement is host specificity: generalist enemies reduce survival near all adults equally and do not favor rare species.

![The Janzen–Connell mechanism. A: Janzen's recruitment curve. Seed density D(r) = exp(−r/10 m) declines with distance from the parent tree, the probability of escaping host-specific enemies E(r) = 1 − exp(−r/15 m) rises, and their product, the density of recruits, peaks at r* = b ln((a + b)/b) = 7.7 m (Eq. 37.9). B: a lottery community of 2000 individuals and initially 40 equally abundant species, all sites refilled each generation (three runs each). In the neutral lottery (gray) a species wins sites in proportion to its abundance and richness declines by drift; with conspecific negative density dependence (green), in which the per capita chance of winning a site falls as exp(−25 n/J), all 40 species persist](./plots/janzen-connell.py)

### 37.4.2. Evidence

The hypothesis has been tested in thousands of studies. Comita et al. (2014) selected 154 well-designed experimental and observational tests and found, in a meta-analysis, that the survival of seeds and seedlings was significantly lower near conspecific adults and at high conspecific density, in temperate as well as tropical forests; distance effects were clearer for seedlings than for seeds. Several lines of evidence identify the agents:

- *Soil pathogens.* In BCI, seedlings grown in soil collected under adults of their own species grew less than in soil from under other species, and the strength of this negative plant–soil feedback correlated with the rarity of the species: rare species suffered most from their own soil (Mangan et al. 2010). The feedback is thus strong enough to influence relative abundance.
- *Exclusion experiments.* Spraying seedling plots in a Belizean forest with fungicide reduced the diversity of seedlings that survived, and insecticide changed species composition, as expected if fungi and insects maintain diversity through species-specific mortality (Bagchi et al. 2014).
- *Biogeography.* Conspecific negative density dependence appears to be stronger in tropical than in temperate forests and stronger for rare species (Johnson et al. 2012; LaManna et al. 2017), although the statistical methods behind the latitudinal comparison have been criticized, because rare species and density estimates create biases (Hülsmann and Hartig 2018).

The Janzen–Connell effect is one of several frequency-dependent mechanisms that stabilize tropical diversity, together with the **storage effect** in fluctuating environments ([7.19.23](/7.19.23)) and recruitment limitation, which slows competitive exclusion because the best competitor fails to reach many sites (Hurtt and Pacala 1995).

## 37.5. Niche and Neutral as a Continuum

Modern coexistence theory ([7.19.23](/7.19.23)) gives a common scale on which neutral and niche theories can be placed. Two species coexist stably when their niche difference, measured by the overlap $\rho$ of their effects on themselves and on each other, is large enough to overcome their fitness difference, measured by a fitness ratio $\kappa_1/\kappa_2$:

$$
\rho < \frac{\kappa_1}{\kappa_2} < \frac1\rho .
$$
The neutral theory is the point $\rho = 1$, $\kappa_1/\kappa_2 = 1$: no niche difference and no fitness difference. At this point coexistence is not stable, since no force returns a species from low abundance, but exclusion is infinitely slow, and drift, which acts on every species equally, decides the outcome. Away from this point two kinds of mechanisms act: **equalizing mechanisms** reduce fitness differences and slow exclusion, **stabilizing mechanisms** give rare species an advantage. Neutral communities are therefore an extreme of equalization without stabilization, and their long persistence shows that equalization alone can maintain diversity for long times if the community is large and speciation and immigration add species.

| Feature | Niche communities (stabilized) | Neutral communities |
|---|---|---|
| Species differences | in niches (stabilizing) and fitness | none |
| Return of a rare species | yes: per capita growth rate higher when rare | no: per capita growth independent of abundance |
| Long-term richness | set by the number of niches or stabilizing mechanisms | set by the balance of speciation, immigration and drift ($\theta$, $m$, $J$) |
| Abundance distribution | depends on niche apportionment | zero-sum multinomial (log-series to lognormal) |
| Response to environment | composition tracks environment | composition independent of environment, dependent on distance |
| Main evidence | trait–environment relations, negative density dependence, removal experiments | fits of static abundance distributions, distance decay |

The two views can be combined. Similar species may be "emergently neutral": in models of competition along a niche axis, species self-organize into clumps of similar species, separated by gaps; within a clump fitness differences are small and exclusion is slow, so the clump behaves almost neutrally, while the clumps are kept apart by niche differences (Scheffer and van Nes 2006). In real forests both stabilizing and neutral processes operate: species sorting along soil and topographic gradients, negative density dependence from enemies, and dispersal limitation and drift among the many similar shade-tolerant species. The neutral theory remains the best available null model for the question how much structure needs explaining by differences among species.

## Summary

- Community assembly (Definition 37.1.1) proceeds from a regional species pool through dispersal, environmental and biotic filters; Vellend's four processes are selection, ecological drift, speciation and dispersal. Priority effects (Definition 37.1.2), by niche preemption or modification, make assembly historically contingent; assembly rules are judged against null models.
- A **metacommunity** (Definition 37.2.1) links local communities by dispersal. Four paradigms (patch dynamics, species sorting, mass effects, neutral) differ in whether patches and species differ and in the rate of dispersal. In the mass-effects model (37.1), alpha richness is maximal at intermediate dispersal, gamma richness falls at high dispersal and beta diversity declines throughout (Proposition 37.2.1, Figure 1).
- The **unified neutral theory of biodiversity** (Definition 37.3.1) assumes ecological equivalence and zero-sum dynamics. Ecological drift (Definition 37.3.2): fixation probability equals relative abundance, mean absorption time $-J[p\ln p + (1 - p)\ln(1 - p)]$ generations, monodominance after order $J$ generations (Proposition 37.3.1).
- Speciation balances drift; the fundamental biodiversity number $\theta \approx J_M\nu$ (Definition 37.3.3) determines the metacommunity, whose samples follow the Ewens sampling formula (Theorem 37.3.1): $\mathbb{E}[S_n] = \sum_{k<n}\theta/(\theta + k) \approx \theta\ln(1 + n/\theta)$, abundance distribution Fisher's log-series with $\alpha = \theta$.
- Dispersal limitation makes local abundances beta-binomial (Proposition 37.3.2); the local abundance distribution (37.8) moves from log-series ($m = 1$) to lognormal-like ($m$ small). BCI: $\theta \approx 50$, $m \approx 0.1$, about 235 species. Criticisms: abundance distributions cannot discriminate models, observed dynamics are too stable, implied species ages too long, species clearly differ.
- The Janzen–Connell hypothesis (Definition 37.4.1): host-specific enemies reduce recruitment near conspecific adults; maximum recruitment at $r^* = b\ln((a + b)/b)$ (Eq. 37.9); it is a stabilizing mechanism supported by meta-analysis, plant–soil feedback and fungicide experiments.
- Neutral theory is the point of zero niche and fitness differences in coexistence theory; real communities combine stabilizing and nearly neutral processes.

## Questions

1. Under neutral drift, a species has 10 individuals in a closed community of $J = 1000$. What is the probability that it eventually takes over the community, and what is the expected time until it is either lost or fixed?

   **Answer** The probability of fixation equals its relative abundance, $p = 0.01$ (Proposition 37.3.1). By (37.2), $T = -1000[0.01\ln 0.01 + 0.99\ln 0.99] = -1000[-0.0461 - 0.0099] \approx 56$ generations. Most of this time is accounted for by the rare event of fixation: the expected time conditional on loss is shorter, conditional on fixation it is about $J$ generations.

2. Williams' light-trap sample of $n = 15\,609$ moths at Rothamsted gives Fisher's $\alpha \approx 39$. How many species does the log-series predict? If $\alpha$ is interpreted as the fundamental biodiversity number, how many species would a sample of twice the size contain?

   **Answer** $\mathbb{E}[S] \approx \alpha\ln(1 + n/\alpha) = 39\ln(1 + 400.2) = 39 \times 5.99 = 234$ species. Doubling the sample gives $39\ln(1 + 800.5) = 39 \times 6.69 = 261$ species: in a log-series, each doubling of the sample adds about $\alpha\ln 2 = 27$ species once $n \gg \alpha$.

3. Show that for $m \to 1$ the local abundance of a species with metacommunity relative abundance $x$ is binomial, and interpret the parameter $I$ when $m$ is small.

   **Answer** With $I = m(J - 1)/(1 - m) \to \infty$, the beta distribution with parameters $Ix$ and $I(1 - x)$ has mean $x$ and variance $x(1 - x)/(I + 1) \to 0$, so the beta-binomial (37.7), a binomial with a beta-distributed success probability, becomes $\mathrm{Bin}(J, x)$: every individual is effectively an independent immigrant. For small $m$, $I \approx m(J - 1)$ is the expected number of immigrants among the $J - 1$ potential replacements, that is, the number of immigrants per generation that compete with local offspring for vacancies. When $I \ll 1$, local communities drift to few species between rare immigration events.

4. In Janzen's model (37.9), what happens to the position of the recruitment peak and to the strength of the effect if (a) seeds are dispersed farther ($a$ larger), (b) enemies are effective over larger distances ($b$ larger)?

   **Answer** (a) $r^* = b\ln(1 + a/b)$ increases with $a$; with $a \gg b$, $r^* \approx b\ln(a/b)$ and most recruits escape the zone of enemies, so the effect on recruitment near the parent remains but the fraction of seeds lost falls. (b) $r^*$ increases with $b$ (for $a$ fixed, $r^* \to a$ as $b \to \infty$), and recruitment is reduced over a wider zone; if $b$ is large compared with the spacing of conspecific adults, the enemies effectively cover the whole range of the species and recruitment is depressed everywhere in proportion to the density of adults, which is the community-level negative density dependence that stabilizes coexistence.

5. Why do fits of species abundance distributions provide weak evidence for or against neutral theory? Propose an observation that would distinguish neutral from niche dynamics more clearly.

   **Answer** Many mechanisms, neutral, niche apportionment and purely statistical, predict similar unimodal distributions in log abundance, because abundance is the product of many independent factors (a central-limit argument) and because distributions with two or three free parameters can be fitted to any such shape. Better tests use dynamics or responses: (1) the dependence of per capita growth on a species' own abundance, which is zero under neutrality and negative under stabilization, measured from repeated censuses; (2) invasion-from-rare experiments, which should show no advantage of rarity under neutrality; (3) the response of composition to environmental gradients after controlling for distance; (4) the temporal variance of abundances, which under drift should grow linearly with time, and the predicted ages of species compared with phylogenies.

6. (Open question) A conservation agency plans to link isolated ponds by channels so that aquatic invertebrates can disperse. Using the metacommunity paradigms, discuss how this could increase or decrease diversity at the pond and regional scales.

   **Answer** Points to cover: in isolated ponds, local communities may be dispersal-limited (species absent because they never arrived) and small populations vulnerable to extinction without rescue; increased dispersal adds species locally (alpha increases) through rescue and mass effects. If ponds differ in conditions (species sorting), moderate dispersal lets each species reach the ponds that suit it. Very high connectivity homogenizes communities: beta diversity falls, regionally dominant competitors or predators (such as fish, if they can pass) spread everywhere, and gamma diversity can fall, as in the mass-effects model (Figure 1). Channels can also spread pathogens and invasive species. A sound plan would therefore aim at intermediate connectivity, keep some ponds isolated (especially fish-free ones), and monitor alpha, beta and gamma diversity before and after.
