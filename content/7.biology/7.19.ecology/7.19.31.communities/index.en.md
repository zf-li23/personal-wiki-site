---
title: "Communities: Composition and the Measurement of Diversity"
description: "The ecological community: definition, scales and characteristics, the organismic and individualistic concepts and assembly filters. Species composition: membership classes (dominant, constructive, subdominant, companion and accidental species) and quantitative characteristics (abundance scales, density, cover, frequency and Raunkiær's law, dominance, importance value). Diversity within communities: richness and sampling effort, richness indices, rarefaction, the Chao1 and ACE estimators with a proof that Chao1 is a lower bound, Simpson and Shannon indices, evenness and Hill numbers. Alpha, beta and gamma diversity and their partitioning. Species abundance distributions: rank–abundance diagrams, geometric series, broken stick, log-series and Fisher's alpha, Preston's log-normal and the veil line, niche apportionment. Global indicators: hotspots, the Biodiversity Intactness Index and the Living Planet Index."
---

With this chapter the course moves from populations and pairs of interacting species to communities: the assemblages of many species that live together. Community ecology asks why a place contains the species it does, in the numbers it does, and how these quantities vary in space and time. Before such questions can be answered, a community must be described, and this chapter introduces the tools of description: the concept of a community (Section 31.1), the roles and quantitative characteristics of its species (Section 31.2), the measurement of diversity within a community (Section 31.3) and across scales (Section 31.4), the distribution of abundances among species (Section 31.5), and the global indicators used to monitor biodiversity (Section 31.6). The physical structure of communities, their classification and ordination follow in [7.19.32](/7.19.32); the processes that structure them in [7.19.33](/7.19.33)–[7.19.39](/7.19.39). Many of the diversity measures were introduced for microbial communities in [7.8.14](/7.8.14); here we derive their properties and use them on plants and animals.

## 31.1. The Community

### 31.1.1. Definition and Scales

**Definition 31.1.1 (Ecological Community)** An **ecological community** is the assemblage of populations of all species that occur together in space and time, together with the interactions among them.

In practice ecologists study subsets: the plant community of a forest, the bird community of a wetland, the invertebrates of a stream, the microbes of a gut. A taxonomic subset is often called an assemblage, and a set of species that use the same resources in a similar way a guild (the seed-eating birds of a desert, the leaf-chewing insects of an oak). Communities can be recognized at any scale in a hierarchy of habitats: a temperate deciduous forest biome, a beech–maple wood within it, the invertebrates of a water-filled tree hole in one beech, or the biota of a deer's gut. No scale is more legitimate than another; the appropriate one depends on the question. The community together with its abiotic environment is the **ecosystem** ([7.19.40](/7.19.40)).

Plant communities have dominated the development of the subject, because plants stay in place and determine the physical structure of most terrestrial communities; many principles of community ecology were first established in vegetation science (phytosociology).

### 31.1.2. Characteristics of a Community

A community has properties that its member populations lack:

1. a species composition, the first criterion for distinguishing communities;
2. interactions among its species: the species of a community share an adaptation to its abiotic environment, and their interactions are, at least for a time, compatible with coexistence;
3. unequal importance of species: some control the structure of the community and its environment, most do not (Section 31.2.2);
4. a community environment: a forest creates its own microclimate, soil and light regime ([7.19.3](/7.19.3));
5. a structure: life forms and layers, horizontal pattern, temporal changes and trophic relations ([7.19.32](/7.19.32));
6. dynamics: seasonal and year-to-year change, succession and evolution ([7.19.36](/7.19.36));
7. a geographic range: communities are distributed according to climate and substrate ([7.19.41](/7.19.41));
8. boundaries, sharp in some places and gradual in most, with transition zones, ecotones, between them ([7.19.32](/7.19.32)).

### 31.1.3. Two Concepts of the Community

The nature of communities was debated from the beginning of ecology. Clements (1916) saw the plant community as an organism-like unit: its species are bound together by their interactions and common history, it develops through succession to a mature climax, as an organism develops to maturity, and communities have sharp boundaries and can be classified like species. This organismic concept underlies the association unit theory of vegetation classification ([7.19.32](/7.19.32)). Gleason (1926) proposed the individualistic concept: each species is distributed according to its own requirements and tolerances, and a community is the more or less fortuitous overlap of species that happen to tolerate the same conditions and to have arrived there, so that communities change gradually along environmental gradients and have no natural boundaries.

The analogy with organisms fails in several ways: populations persist when a community disappears; the development of a community is the replacement of populations rather than the growth of one body; the same community type is not reproduced from a "parent" community; and different stands of one community type have no genetic connection. Direct gradient analysis and ordination ([7.19.32](/7.19.32)) showed that species are distributed individualistically along gradients, with overlapping and differently shaped ranges. The modern view is close to Gleason's: a given site, by its physical properties, supports a reasonably predictable association of species, but the same species occurs with other species under other conditions, and community boundaries are mostly gradual. Communities are a level of organization to be studied, not discrete units, and discrete boundaries are not needed to study them.

The modern framework describes the assembly of a community as a series of filters acting on a regional pool of species: dispersal (which species can arrive), environment (which can persist under the abiotic conditions) and internal dynamics (which survive the interactions with the others) (Belyea and Lancaster 1999). Vellend (2010) reduced the processes to four: selection (deterministic differences in fitness among species, including niche differences and interactions), ecological drift (random changes in relative abundance), dispersal and speciation, the analogues of selection, drift, gene flow and mutation in population genetics. These processes are the subject of [7.19.33](/7.19.33)–[7.19.37](/7.19.37).

## 31.2. Species Composition

### 31.2.1. Species Lists and Sampling Plots

Community analysis begins with a list of the species present, obtained by sampling plots (quadrats, [7.19.8](/7.19.8)) placed in a stand that is homogeneous in composition and structure, avoiding transition zones. The plot must be large enough: the number of species recorded rises with plot area and levels off, and the *minimal area* is the area beyond which few new species are added, a few square meters in grassland, hundreds or thousands of square meters in species-rich forests. The list of all plant species of a region is its flora; the species list of a community, with each species' role and abundance, is the starting point for the descriptions below.

### 31.2.2. The Roles of Species

Species differ in their importance for the community, and vegetation science classifies them into membership classes.

**Definition 31.2.1 (Membership Classes of a Plant Community)** In a plant community:

- **dominant species** are those that control the structure and environment of the community, usually through large numbers, high cover, high biomass, large size or high vigor; each layer of a stratified community can have its own dominants;
- the **constructive species** (edificator) is the dominant of the dominant layer, usually the tree layer of a forest;
- subdominant species are less abundant and less influential than the dominants but still contribute to the character and environment of the community, often in a lower layer;
- companion species are common members that occur with the dominants without controlling the community;
- accidental (rare) species occur at low frequency and abundance: chance arrivals, invaders, or relicts of an earlier stage.

Communities with a single constructive species (many boreal forests and steppes) are distinguished from those with several (co-dominant communities, such as tropical rain forests). The concept of dominance is about control: removing a dominant changes the community and its environment profoundly, removing a companion species little. The same species can be dominant in one community and a companion in another; and an endemic species is not a membership class. Dominance should be distinguished from keystone status: a **keystone species** has an effect on the community out of proportion to its abundance, typically a predator or an engineer, whereas dominants are important because they are abundant ([7.19.33](/7.19.33)). Conservation must protect the dominant and constructive species, not only rare ones: they hold the community together.

### 31.2.3. Quantitative Characteristics

Description becomes quantitative with measures of how much of each species there is and how it is distributed.

- Abundance. In rapid field surveys, abundance is estimated on an ordinal scale. Chinese surveys use Drude's seven-class scale: Soc. (*sociales*, very abundant, the plants forming a closed canopy), Cop.³, Cop.², Cop.¹ (*copiosae*, very many, many, fairly many), Sp. (*sparsae*, scattered), Sol. (*solitariae*, sparse and few), Un. (*unicum*, a single or two individuals in the plot). The Braun-Blanquet cover–abundance scale (r, +, 1, 2, 3, 4, 5) combines abundance and cover and is standard in European phytosociology.
- Density: the number of individuals per unit area (for clonal plants, shoots or tussocks). *Relative density* is the percentage of all individuals that belong to a species; the *density ratio* compares a species with the densest one.
- Cover: the percentage of the plot area covered by the vertical projection of the aboveground parts of a species (*projective cover*). Because layers overlap, the covers of species sum to more than the total cover of the community. In forestry the cover of the tree layer is the *canopy closure*. *Basal cover* is the area of the stem bases, measured for trees at breast height (1.3 m) as basal area; the basal area of a tree species is called its "dominance" in this sense. Relative cover is the percentage of the summed covers of all species.
- Frequency: the percentage of plots in which a species occurs. Frequency depends on plot size and on the spatial pattern of the species: a clumped species has low frequency for its density ([7.19.8](/7.19.8)). Raunkiær (1918) grouped species into frequency classes A (1–20 %), B (21–40 %), C (41–60 %), D (61–80 %) and E (81–100 %) and found that, in homogeneous stands, $A > B > C \gtrless D < E$: most species are infrequent, and a second group, the dominants and constructive species, is present nearly everywhere ("Raunkiær's law of frequency"). A distribution with large B, C and D classes indicates a heterogeneous stand.
- Height, biomass and volume complete the list.

These are combined into one measure of the standing of each species.

**Definition 31.2.2 (Importance Value)** The *importance value* of a species in a community (Curtis and McIntosh 1951) is the sum of its relative density, relative frequency and relative dominance (relative basal area):

$$
\mathrm{IV} = \text{relative density} + \text{relative frequency} + \text{relative dominance},
$$
each expressed as a percentage, so that $\mathrm{IV}$ ranges from 0 to 300 and sums to 300 over all species. In grasslands relative cover replaces relative dominance.

**Example 31.2.1** In ten plots of a forest stand (hypothetical data), five tree species have the following values.

| Species | Stems | Plots occupied | Basal area / m² | Rel. density | Rel. frequency | Rel. dominance | IV |
|---|---|---|---|---|---|---|---|
| A | 40 | 10 | 3.2 | 40.0 | 32.3 | 53.3 | 125.6 |
| B | 25 | 8 | 1.6 | 25.0 | 25.8 | 26.7 | 77.5 |
| C | 20 | 6 | 0.6 | 20.0 | 19.4 | 10.0 | 49.4 |
| D | 10 | 5 | 0.4 | 10.0 | 16.1 | 6.7 | 32.8 |
| E | 5 | 2 | 0.2 | 5.0 | 6.5 | 3.3 | 14.8 |
| Total | 100 | 31 | 6.0 | 100 | 100 | 100 | 300 |

Relative frequency is computed from the sum of the frequencies of all species (here 31 occurrences). Species A, with the highest IV and the largest share of basal area, is the constructive species; B ranks second because it is frequent and has large trees, although C is nearly as dense. The importance value integrates numbers, distribution and size, and it is widely used to name communities, to select the dominants for classification ([7.19.32](/7.19.32)) and as the abundance measure in ordination.

## 31.3. Diversity within a Community

### 31.3.1. Richness and Sampling Effort

The simplest measure of diversity is the number of species, **richness** ([7.8.14](/7.8.14#def-14.4.1)). It is the most intuitive measure and, Poole (1974) argued, the only truly objective one, but it has a fundamental problem: it depends on how much was sampled. Common species appear in the first samples and rare species are added slowly, so the species count keeps increasing with effort (Figure 2A). Richness values can be compared only for equal area, equal number of individuals or equal sampling effort, and in stratified forests only for the same layer and size class. Richness indices that divide by a function of sample size are attempts to remove the effect:

$$
D_{\mathrm{Gl}} = \frac{S}{\ln A}\ \text{(Gleason 1922)},\qquad D_{\mathrm{Mg}} = \frac{S - 1}{\ln N}\ \text{(Margalef 1958)},\qquad D_{\mathrm{Mn}} = \frac{S}{\sqrt N}\ \text{(Menhinick 1964)},
$$
with $S$ the number of species, $A$ the area and $N$ the number of individuals. They assume a particular shape of the species–sample-size relation and are only roughly comparable across studies.

The modern approach standardizes samples statistically. A *species accumulation curve* plots the cumulative number of species against the number of individuals or samples. *Rarefaction* computes the number of species expected in a random subsample of $n$ individuals from a sample of $N$ individuals with $N_i$ individuals in species $i$ (Hurlbert 1971; Sanders 1968):

$$
\mathbb{E}[S_n] = \sum_{i=1}^{S}\left[1 - \binom{N - N_i}{n}\Big/\binom{N}{n}\right],
$$
because the term in brackets is the probability that species $i$ appears in the subsample. The **rarefaction curve** $\mathbb{E}[S_n]$ allows communities sampled with different effort to be compared at the size of the smallest sample, and its shape shows how close a sample is to saturation. Rarefaction curves can cross: a community of many rare species may show fewer species than an even community in small samples but more in large ones, and the comparison then depends on the sample size chosen (Figure 2A). Rarefaction discards information; extrapolation of the curve toward its asymptote (Colwell et al. 2012) uses all of it, and leads to the estimation of total richness.

### 31.3.2. Estimating the Number of Unseen Species

How many species were missed? The answer comes from the rare species in the sample: if many species were seen only once, many more are likely to have been missed altogether. Let $F_k$ be the number of species represented by exactly $k$ individuals in the sample ($F_1$ singletons, $F_2$ doubletons) and $S_{\mathrm{obs}}$ the number observed.

**Definition 31.3.1 (Chao1 Estimator)** The *Chao1 estimator* of species richness (Chao 1984) is

$$
\hat S_{\mathrm{Chao1}} = S_{\mathrm{obs}} + \frac{F_1^2}{2F_2},
$$
and its bias-corrected form, defined also when $F_2 = 0$, is $\hat S_{\mathrm{Chao1}} = S_{\mathrm{obs}} + \frac{n - 1}{n}\,\frac{F_1(F_1 - 1)}{2(F_2 + 1)}$ for a sample of $n$ individuals.

**Proposition 31.3.1** Under Poisson sampling, $\mathbb{E}[F_1]^2/(2\,\mathbb{E}[F_2])$ is a lower bound for the expected number $\mathbb{E}[F_0]$ of species present but unobserved.

**Proof** Let species $i$ contribute a Poisson number of individuals with mean $\lambda_i$ to the sample. Then $\mathbb{E}[F_k] = \sum_i \mathrm{e}^{-\lambda_i}\lambda_i^k/k!$, in particular $\mathbb{E}[F_0] = \sum_i\mathrm{e}^{-\lambda_i}$, $\mathbb{E}[F_1] = \sum_i\mathrm{e}^{-\lambda_i}\lambda_i$ and $\mathbb{E}[F_2] = \frac12\sum_i\mathrm{e}^{-\lambda_i}\lambda_i^2$. By the Cauchy–Schwarz inequality applied to the vectors $\bigl(\mathrm{e}^{-\lambda_i/2}\bigr)$ and $\bigl(\mathrm{e}^{-\lambda_i/2}\lambda_i\bigr)$,

$$
\Bigl(\sum_i\mathrm{e}^{-\lambda_i}\lambda_i\Bigr)^2 \le \Bigl(\sum_i\mathrm{e}^{-\lambda_i}\Bigr)\Bigl(\sum_i\mathrm{e}^{-\lambda_i}\lambda_i^2\Bigr),
$$
that is, $\mathbb{E}[F_1]^2 \le \mathbb{E}[F_0]\cdot2\,\mathbb{E}[F_2]$. $\square$

Equality holds when all species have the same detection rate; with heterogeneous rates the estimator underestimates, so Chao1 is a lower bound for richness, sensitive above all to the number of singletons. It was developed in statistics for "the number of classes in a population" and is widely used in microbial ecology. The *abundance-based coverage estimator* (ACE; Chao and Lee 1992) separates abundant species (more than 10 individuals, $S_{\mathrm{abund}}$) from rare ones ($S_{\mathrm{rare}}$, containing $N_{\mathrm{rare}}$ individuals) and corrects the rare part by the estimated sample coverage $C = 1 - F_1/N_{\mathrm{rare}}$, the fraction of the rare individuals' abundance that belongs to species seen more than once:

$$
\hat S_{\mathrm{ACE}} = S_{\mathrm{abund}} + \frac{S_{\mathrm{rare}}}{C} + \frac{F_1}{C}\,\gamma^2,\qquad
\gamma^2 = \max\Bigl[\frac{S_{\mathrm{rare}}}{C}\,\frac{\sum_{i=1}^{10}i(i - 1)F_i}{N_{\mathrm{rare}}(N_{\mathrm{rare}} - 1)} - 1,\ 0\Bigr],
$$
where $\gamma^2$ estimates the squared coefficient of variation of detection rates among rare species.

**Example 31.3.1** Two samples contain five species with the counts A: $(15, 2, 4, 0, 1)$ and B: $(2, 12, 20, 1, 1)$. In A, $S_{\mathrm{obs}} = 4$, $n = 22$, $F_1 = 1$, $F_2 = 1$: the classical Chao1 is $4 + 1/2 = 4.5$, the bias-corrected one $4 + 0 = 4$ (one singleton gives $F_1(F_1 - 1) = 0$). For ACE the rare species are those with 2, 4 and 1 individuals: $S_{\mathrm{rare}} = 3$, $N_{\mathrm{rare}} = 7$, $C = 1 - 1/7 = 0.857$, $\sum i(i - 1)F_i = 2 + 12 = 14$, $\gamma^2 = 3/0.857\cdot14/(7\cdot6) - 1 = 0.167$, and $\hat S_{\mathrm{ACE}} = 1 + 3.5 + 0.19 = 4.69$. In B, $S_{\mathrm{obs}} = 5$, $n = 36$, $F_1 = 2$, $F_2 = 1$: Chao1 $= 5 + 4/2 = 7$ (classical) or $5 + \frac{35}{36}\cdot\frac{2}{4} = 5.49$ (bias-corrected); for ACE, $S_{\mathrm{rare}} = 3$ (2, 1, 1), $N_{\mathrm{rare}} = 4$, $C = 0.5$, $\gamma^2 = \max(3/0.5\cdot2/12 - 1, 0) = 0$, and $\hat S_{\mathrm{ACE}} = 2 + 6 = 8$. Sample B, with two singletons, signals more unseen species than A; with such small samples the estimators differ widely, which is a warning against using them on few individuals.

:::

In large samples the estimators approach the true richness much faster than the observed count does (Figure 2B), but in small samples they too fall short. They should be reported with their confidence intervals, and comparisons are most reliable when based on samples of equal completeness (coverage) rather than equal size (Chao and Jost 2012).

![Rarefaction and richness estimators on simulated communities. A: rarefaction curves from samples of 1500 individuals of community 1 (150 species, very uneven log-normal abundances) and community 2 (80 species, more even): the curves cross near 180 individuals, so a comparison at small sample size would rank the communities the wrong way round. B: for community 1, mean over 40 samples of size n of the observed richness, the bias-corrected Chao1 and ACE; dashed: the true richness. The estimators approach 150 with a few hundred individuals, the observed count only with thousands](./plots/rarefaction-chao.py)

### 31.3.3. Heterogeneity Indices

Richness ignores relative abundance. A community of ten species with equal numbers is more diverse, in the everyday sense, than one in which a single species has more than half of the individuals and nine share the rest. Diversity combines richness with evenness, the equitability of the distribution of individuals among species, and heterogeneity indices measure both at once.

- The **Simpson index** $\lambda = \sum_i p_i^2$, with $p_i$ the proportion of individuals (or biomass) in species $i$, is the probability that two individuals drawn at random with replacement belong to the same species ([7.8.14](/7.8.14#def-14.4.1)). For a finite sample, drawing without replacement gives the unbiased form $\hat\lambda = \sum_i n_i(n_i - 1)/\bigl(N(N - 1)\bigr)$. Its complement $1 - \lambda$ (the Gini–Simpson index) is the probability that two individuals belong to different species, and $1/\lambda$ (the inverse Simpson index) is a diversity that increases with both richness and evenness, with maximum $S$ when all species are equally abundant.
- The **Shannon index** $H' = -\sum_i p_i\ln p_i$ is the entropy of information theory ([7.8.14](/7.8.14#def-14.4.1)): the uncertainty about the species of an individual drawn at random. The base of the logarithm sets the unit: bits for base 2, nats for base $\mathrm{e}$, decits (hartleys) for base 10. For fixed $S$, $H'$ is maximal, $H'_{\max} = \ln S$, when all species are equally abundant, and $0$ when there is only one species. The index is also called the Shannon–Wiener or Shannon–Weaver index (the spelling "Weiner" found in some texts is an error).

**Example 31.3.2** Two communities of 24 individuals each contain three species: C with $(8, 8, 8)$ and D with $(22, 1, 1)$. For C, $H' = \ln3 = 1.099$ and $\hat\lambda = 3\cdot8\cdot7/(24\cdot23) = 0.304$, so $1 - \hat\lambda = 0.696$. For D, $H' = -(\frac{22}{24}\ln\frac{22}{24} + 2\cdot\frac1{24}\ln\frac1{24}) = 0.345$ and $\hat\lambda = 22\cdot21/552 = 0.837$, $1 - \hat\lambda = 0.163$. Both indices rank C as more diverse, although the richness is the same (Figure 1A).

:::

The two indices weight species differently. The Simpson index is dominated by the commonest species (each enters with weight $p_i^2$) and is relatively insensitive to rare species, so it measures mainly dominance and evenness; the Shannon index weights species by $-\ln p_i$, which is large for rare species, and is more sensitive to richness. A long-term example: in the Park Grass experiment at Rothamsted, England, plots fertilized every year since 1856 declined steadily in diversity $H'$ and evenness over a century, while unfertilized plots changed little; abundant nutrients let the most productive species dominate (Crawley et al. 2005; the productivity–diversity relation is treated in [7.19.35](/7.19.35)).

### 31.3.4. Evenness

Evenness is diversity relative to its maximum for the given richness.

**Definition 31.3.2 (Pielou's Evenness)** *Pielou's evenness index* is $J' = H'/\ln S$, the ratio of the Shannon index to its maximum for $S$ species; it lies between 0 and 1, with $J' = 1$ for equal abundances. Simpson's evenness is $E_{1/\lambda} = (1/\lambda)/S$.

For communities C and D of Example 31.3.2, $J' = 1.000$ and $0.314$. Evenness indices inherit the dependence on $S$ (which must itself be estimated), and $J'$ in particular is not independent of richness; ratios of Hill numbers (below) are better behaved.

### 31.3.5. Hill Numbers

Indices such as $H'$ and $1 - \lambda$ are not diversities in the sense of "numbers of species": a community of 16 equally abundant species has $H' = \ln16 = 2.77$, one of 8 has $2.08$, and the first is not 1.33 times as diverse but twice. Hill (1973) unified the measures as effective numbers of species.

**Formula 31.3.1 (Hill Numbers)** The diversity of order $q$ of a community with relative abundances $p_1, \dots, p_S$ is

$$
{}^qD = \Bigl(\sum_{i=1}^{S}p_i^q\Bigr)^{1/(1 - q)},\qquad {}^1D = \lim_{q\to1}{}^qD = \exp\Bigl(-\sum_ip_i\ln p_i\Bigr) = \mathrm{e}^{H'} .
$$
Thus ${}^0D = S$ (richness), ${}^1D = \mathrm{e}^{H'}$ (the exponential of Shannon) and ${}^2D = 1/\lambda$ (inverse Simpson).

**Hill numbers** ([7.8.14](/7.8.14)) have three properties that make them the preferred measures (Jost 2006; Chao et al. 2014). (1) ${}^qD$ is the number of equally abundant species that would give the same value of the underlying index: a community with ${}^1D = 5$ is as diverse, in Shannon's sense, as one of five equally common species. (2) They obey the replication (doubling) principle: pooling two equally large communities with the same abundance distribution but no species in common doubles ${}^qD$, which the indices themselves do not do. (3) The order $q$ sets the sensitivity to rare species: $q = 0$ counts all species equally, $q = 1$ weights them by abundance, $q = 2$ emphasizes common species. ${}^qD$ decreases with $q$, and equals $S$ for all $q$ only when abundances are equal. A *diversity profile*, ${}^qD$ plotted against $q$, shows the whole picture: if two profiles do not cross, one community is more diverse than the other for every measure; if they cross, the ranking depends on the weight given to rare species (Figure 1B). The limit for $q \to \infty$ is $1/\max_ip_i$, the Berger–Parker measure of dominance.

![Diversity indices and Hill numbers. A: communities C (8, 8, 8) and D (22, 1, 1) of Example 31.3.2 with their richness, Shannon index, Simpson index (finite-sample form), Gini–Simpson index and Pielou's evenness. B: Hill diversity profiles: C is perfectly even (3 effective species at every order), D falls from 3 species (q = 0) to 1.41 (q = 1) and 1.19 (q = 2) because one species dominates; E, 20 species with geometrically declining abundances, has 7.6 effective species at q = 1 and 5.7 at q = 2](./plots/diversity-indices.py)

## 31.4. Diversity at Several Scales

Diversity depends on the scale of study. A landscape contains many habitat patches, each with its own species; the total diversity of the landscape depends both on the diversity within patches and on how different the patches are. Whittaker (1960, 1972) distinguished three components.

- **Alpha diversity** ([7.8.14](/7.8.14)) is the diversity within a single community or habitat patch, measured by any of the indices of Section 31.3.
- **Beta diversity** ([7.8.14](/7.8.14)) is the differentiation among communities: the extent of change in species composition from one community to another along an environmental gradient or across a region, the turnover of species.
- **Gamma diversity** is the total diversity of a region that contains several communities: the diversity of the pooled sample.

**Definition 31.4.1 (Whittaker's Beta Diversity)** With $\gamma$ the number of species in the region and $\bar\alpha$ the mean number of species per community, Whittaker's multiplicative beta diversity is

$$
\beta_W = \frac{\gamma}{\bar\alpha},
$$
the effective number of completely distinct communities in the region; $\beta_W - 1$ measures turnover, from 0 when all communities have the same species. The additive partition $\gamma = \bar\alpha + \beta_{\mathrm{add}}$, with $\beta_{\mathrm{add}} = \gamma - \bar\alpha$ the average number of species in the region missing from a community, is an alternative (Lande 1996).

**Example 31.4.1** Region I contains three communities with species $\{a, b\}$, $\{a, c\}$ and $\{b, c\}$; region II three communities that each contain $\{a, b, c\}$. Both regions have $\gamma = 3$. In I, $\bar\alpha = 2$ and $\beta_W = 1.5$ (turnover $0.5$, $\beta_{\mathrm{add}} = 1$); in II, $\bar\alpha = 3$ and $\beta_W = 1$ (no turnover).

:::

Beta diversity has several uses: it measures how strongly a gradient sorts species (high turnover along steep gradients of elevation or moisture), how heterogeneous a region is, and how much of the regional diversity is lost if only a few communities are protected; protecting several communities in a region of high beta diversity captures far more species than protecting one. Pairwise measures of compositional dissimilarity, such as the **Jaccard distance** $1 - \frac{a}{a + b + c}$ and the Sørensen dissimilarity $1 - \frac{2a}{2a + b + c}$ (with $a$ species shared and $b$, $c$ species unique to each community), and the **Bray–Curtis dissimilarity** for abundance data ([7.8.14](/7.8.14)), are the raw material of classification and ordination ([7.19.32](/7.19.32)). With Hill numbers, the multiplicative partition ${}^q\gamma = {}^q\alpha\cdot{}^q\beta$ holds for every order $q$ with appropriately defined alpha (Jost 2007), and ${}^q\beta$ ranges from 1 (identical communities) to $N$ ($N$ communities with no species in common). Hui and McGeoch (2014) extended the idea to zeta diversity, the mean number of species shared by $i$ sites, which declines as $i$ increases and describes how common and rare species contribute to turnover.

## 31.5. Species Abundance Distributions

### 31.5.1. Rank–Abundance Diagrams

Diversity indices compress the abundances into one number. The full information is in the distribution of abundances among species.

**Definition 31.5.1 (Species Abundance Distribution)** The *species abundance distribution* of a community is the frequency distribution of the abundances of its species: how many species have 1, 2, 3, … individuals. It is commonly displayed as a *rank–abundance diagram* (Whittaker plot), in which the relative abundance $p_i$ (usually on a log scale) is plotted against the rank $i$ of the species from the most to the least abundant, or as a histogram of species against abundance on a logarithmic scale (Preston plot).

Two regularities hold in almost all communities: a few species are common and most are rare, and on a log scale the distribution of abundances is unimodal or hollow. Many models have been fitted to them. Some are statistical descriptions; others derive from assumptions about how species divide resources, the niche apportionment models (Tokeshi 1993; McGill et al. 2007), and the hope is that the best-fitting model reveals the underlying process.

### 31.5.2. Niche Apportionment Models

- Geometric series (Motomura 1932). The most successful species pre-empts a fraction $k$ of the niche space (resources), the next a fraction $k$ of the remainder, and so on. With $S$ species,

$$
p_i = \frac{k(1 - k)^{i - 1}}{1 - (1 - k)^S},\qquad i = 1, \dots, S,
$$
a straight line on a rank–log-abundance plot with slope $\ln(1 - k)$. It describes species-poor, harsh or early-successional communities dominated by a few species. In the fertilized Park Grass plots, the fitted geometric series became steeper as dominance increased over the century.
- Broken stick (MacArthur 1957). The niche space, a stick of unit length, is broken at $S - 1$ points placed at random and simultaneously; each species receives one piece. The expected length of the $i$-th largest piece of a stick broken into $S$ pieces is

$$
p_i = \frac1S\sum_{j=i}^{S}\frac1j,
$$
the most even distribution of the classical models. It fits some assemblages of territorial birds and taxonomically narrow groups of similar species.
- Tokeshi's sequential models: in the *dominance pre-emption* model each new species takes more than half of the remaining niche (close to the geometric series); in the *random fraction* model a randomly chosen existing niche is split at a random point; in the *MacArthur fraction* model the niche to be split is chosen with probability proportional to its size, giving more even distributions; in the *dominance decay* model the largest niche is always split, the most even of all. Invertebrates on the structurally complex stream plant *Ranunculus yezoensis* were richer and more even than on the simple *Sparganium emersum*, and both distributions were closer to the random fraction than to the MacArthur fraction model.

### 31.5.3. Statistical Models: the Log-Series and the Log-Normal

Fisher, Corbet and Williams (1943) fitted the abundance of moths caught in light traps at Rothamsted and of Malayan butterflies with the log-series, in which the expected number of species with $n$ individuals is

$$
\mathbb{E}[S_n] = \alpha\frac{x^n}{n},\qquad n = 1, 2, \dots,\qquad S = \alpha\ln\Bigl(1 + \frac N\alpha\Bigr),\qquad x = \frac{N}{N + \alpha}.
$$
The most frequent class is that of singletons. The parameter $\alpha$, *Fisher's alpha*, is nearly independent of sample size once $N$ is large, which makes it a useful diversity index: $S$ grows only logarithmically with $N$, at a rate set by $\alpha$. Fisher derived the series as the limit of a negative binomial (a gamma mixture of Poisson sampling) as its shape parameter tends to zero. The log-series is also the species abundance distribution of the metacommunity in Hubbell's neutral theory, in which $\alpha$ becomes the fundamental biodiversity number $\theta$ ([7.19.37](/7.19.37)).

Preston (1948) grouped species into "octaves" of abundance (1, 2–3, 4–7, 8–15, … individuals, a log₂ scale) and found that the number of species per octave was a bell-shaped curve, a log-normal distribution of abundances: $\log N_i$ is approximately normal across species. A log-normal arises if the abundance of a species is the product of many independent factors (a multiplicative central limit theorem, **log-normal distribution**). In a small sample the left part of the distribution is hidden behind a "veil line": the rarest species have not been sampled, the mode of the observed distribution lies in the first octaves and the distribution looks like a log-series; as the sample grows, the veil moves left and the mode of the log-normal appears (Figure 3B, C). Whether real distributions are log-normal, log-series or something else, such as the zero-sum multinomial of neutral theory, is difficult to decide from data, because sampling distorts all of them and different models fit the same data almost equally well (McGill et al. 2007).

![Species abundance distributions. A: rank–abundance diagrams of four models for about 25 species: the geometric series (k = 0.4) is a straight line on the log scale and the most uneven, the broken stick the most even, with the log-series (Fisher's alpha = 5, N = 1000, 26 species) and the log-normal (log-sd 1.2) in between. B, C: Preston octave plots of samples of 500 and 20 000 individuals from one simulated community of 300 species with log-normal abundances: the small sample reveals 160 species with the mode in the first octave (the rest are hidden behind the veil line); the large sample reveals 288 species and the mode of the log-normal](./plots/rank-abundance.py)

## 31.6. Global Indicators of Biodiversity

At the global scale, the measurement of diversity serves conservation, which needs simple indicators to set priorities and to monitor change ([7.19.50](/7.19.50)–[7.19.52](/7.19.52)).

- Biodiversity hotspots (Myers et al. 2000) are regions with at least 1500 endemic species of vascular plants (more than 0.5 % of the world total) that have lost at least 70 % of their original habitat. Originally 25, now 36 hotspots cover about 2.5 % of the land surface but hold about half of the endemic plant species and 43 % of endemic terrestrial vertebrates. Southwest China (the Mountains of Southwest China) and the Indo-Burma region, which includes southern China, are among them.
- The Biodiversity Intactness Index (Scholes and Biggs 2005) is the mean abundance of the species originally present in an area, relative to their abundance in an undisturbed reference, averaged over species and weighted by area; it estimates how much of the original biodiversity remains. Global estimates, based on models of how land use affects local assemblages (the PREDICTS database), suggest that intactness has fallen below proposed safe limits over much of the land surface.
- The Living Planet Index, compiled by the Zoological Society of London and WWF, tracks the average change in the abundance of monitored vertebrate populations since 1970. Each population's year-to-year change is computed as a log ratio, $d_t = \log_{10}(N_t/N_{t-1})$; changes are averaged within species, then within taxonomic and regional groups, and the index is chained, $I_t = I_{t-1}\cdot10^{\bar d_t}$, with $I_{1970} = 1$. The 2022 report found an average decline of 69 % between 1970 and 2018, and the 2024 report a decline of 73 % between 1970 and 2020 for about 35 000 populations of 5500 species, steepest in Latin America and the Caribbean and in freshwater. Because the index averages log ratios, it is a geometric mean of trends that can be dominated by a few populations with extreme declines, and it does not say that 73 % of individual animals have disappeared (Leung et al. 2020).

These indicators complement the measures of this chapter: hotspots weight richness and endemism, intactness measures abundance relative to a baseline, and the Living Planet Index measures trends, but none measures diversity as such, and all depend on which taxa and places are monitored.

## Summary

| Topic | Key points |
|---|---|
| Community | **Ecological community** (Definition 31.1.1); scales from tree hole to biome; eight characteristics; organismic (Clements) and individualistic (Gleason) concepts; assembly filters and Vellend's four processes |
| Roles of species | Dominant species, constructive species, subdominant, companion and accidental species (Definition 31.2.1); dominance is not keystone status |
| Quantitative characteristics | Drude and Braun-Blanquet scales; density, cover, frequency (Raunkiær's law $A > B > C \gtrless D < E$), basal area; importance value $= $ rel. density $+$ rel. frequency $+$ rel. dominance (Definition 31.2.2, Example 31.2.1) |
| Richness | Depends on effort; Gleason, Margalef, Menhinick indices; **rarefaction curve** $\mathbb{E}[S_n]$; Chao1 (Definition 31.3.1), a lower bound by Cauchy–Schwarz (Proposition 31.3.1); ACE (Example 31.3.1) |
| Heterogeneity | **Simpson index** (dominance, insensitive to rare species), **Shannon index** (sensitive to rare species); Example 31.3.2: $H' = 1.099$ vs $0.345$, $\hat\lambda = 0.304$ vs $0.837$; Pielou's evenness (Definition 31.3.2) |
| Hill numbers | ${}^qD = (\sum p_i^q)^{1/(1-q)}$: $S$, $\mathrm{e}^{H'}$, $1/\lambda$ (Formula 31.3.1); effective numbers, doubling property, diversity profiles |
| Scales | **Alpha diversity**, **beta diversity**, **gamma diversity**; $\beta_W = \gamma/\bar\alpha$ (Definition 31.4.1, Example 31.4.1); additive partition; Jaccard, Sørensen, Bray–Curtis |
| Abundance distributions | Species abundance distribution and rank–abundance diagram (Definition 31.5.1); geometric series, broken stick, Tokeshi's models; log-series and Fisher's $\alpha$; Preston's log-normal and the veil line |
| Global indicators | Hotspots (≥ 1500 endemic plants, ≥ 70 % habitat lost; 36); Biodiversity Intactness Index; Living Planet Index (−73 % 1970–2020, a geometric mean of trends) |

## Questions

1. Why does the importance value use relative rather than absolute density, frequency and dominance? What would be lost by using only basal area?

   **Answer** The three quantities have different units (stems per area, percentage of plots, square meters per area) and different ranges; expressing each as a percentage of the community total makes them commensurable and gives each equal weight, and makes the values comparable between stands of different total density or basal area. Basal area alone would rank species by size and would rate a few large old trees above a numerous, widespread species of small trees that may dominate regeneration; density and frequency add information about numbers and spatial distribution.
2. Compute $H'$, $1/\lambda$ (with $\lambda = \sum p_i^2$) and Pielou's $J'$ for a community with relative abundances $(0.5, 0.25, 0.125, 0.125)$, and give ${}^0D$, ${}^1D$ and ${}^2D$.

   **Answer** $H' = -(0.5\ln0.5 + 0.25\ln0.25 + 2\cdot0.125\ln0.125) = 0.347 + 0.347 + 0.520 = 1.213$; $\lambda = 0.25 + 0.0625 + 2\cdot0.015625 = 0.344$, $1/\lambda = 2.91$; $J' = 1.213/\ln4 = 0.875$. ${}^0D = 4$, ${}^1D = \mathrm{e}^{1.213} = 3.36$, ${}^2D = 2.91$.
3. Prove the doubling property of ${}^qD$: if two communities with no species in common have the same Hill number ${}^qD = X$ and the same total abundance, the pooled community has ${}^qD = 2X$.

   **Answer** Pooling equal totals halves every relative abundance: the pooled community has abundances $p_i/2$ from the first community and $p'_j/2$ from the second. Then $\sum(p_i/2)^q + \sum(p'_j/2)^q = 2^{-q}\bigl(\sum p_i^q + \sum p_j'^q\bigr) = 2^{1-q}X^{1-q}$, because each sum equals $X^{1-q}$. Raising to the power $1/(1-q)$ gives $2X$. For $q = 1$, $H'_{\mathrm{pooled}} = H' + \ln2$, so $\mathrm{e}^{H'}$ doubles as well.
4. A sample of 400 individuals contains 60 species, 18 of them singletons and 9 doubletons. Estimate total richness with Chao1 (both forms). Why is the estimate a lower bound?

   **Answer** Classical: $60 + 18^2/(2\cdot9) = 60 + 18 = 78$. Bias-corrected: $60 + \frac{399}{400}\cdot\frac{18\cdot17}{2\cdot10} = 60 + 15.3 = 75.3$. By Proposition 31.3.1, $\mathbb{E}[F_1]^2/(2\mathbb{E}[F_2])$ underestimates the expected number of unseen species whenever detection rates differ among species, equality holding only if all species are equally detectable; real communities have many very rare species that are hardly ever caught, which the singletons and doubletons cannot reveal.
5. Explain how a small sample can make a log-normal species abundance distribution look like a log-series.

   **Answer** Species whose expected number of individuals in the sample is below about one are mostly missed or appear as singletons. In a small sample, the veil line lies to the right of the mode of the log-normal: the observed octave histogram consists only of the right tail and peaks in the first octave, which is the shape of the log-series (most frequent class: singletons). As sampling effort increases, the veil moves left and the mode appears. Fitting a model to the observed distribution without accounting for sampling therefore confuses sampling with community structure.
6. (Open) A conservation agency must choose between protecting one large area of 1000 km² in a single forest type and five areas of 200 km² spread along an elevation gradient. Which diversity components inform the choice, and what data would you collect?

   **Answer** The choice depends on the balance between alpha diversity (and the long-term viability of populations, which favors large areas) and beta diversity (turnover along the gradient, which favors multiple areas in different communities). Collect species lists and abundances from standardized plots along the gradient, estimate richness by rarefaction and Chao1, compute pairwise dissimilarities and $\beta_W$ or Hill-number beta, and estimate the gamma diversity captured by each design (e.g. from species accumulation over the plots included); add population viability considerations for area-sensitive species and the connectivity among areas. The SLOSS debate is treated in [7.19.34](/7.19.34).
