---
title: "Populations: Abundance, Sampling and Spatial Pattern"
description: "The population as the unit of population ecology: definition and basic features; unitary and modular organisms, genets and ramets, growth forms and integration; the four questions of population dynamics and the BIDE equation; population size and density; estimating abundance: total counts (the Tsinghua crow counts), quadrats and their sampling error, line transects, point counts and distance sampling, camera traps and occupancy models, passive acoustic monitoring and the vocal activity rate, mark–recapture (Lincoln–Petersen as a maximum likelihood estimator, Chapman's estimator and variance, assumptions and catchability heterogeneity, Schnabel and Jolly–Seber), removal sampling (Leslie regression, two-pass estimator), relative indices and hyperstability; spatial pattern: regular, random and clumped dispersion, Poisson and negative binomial quadrat counts, the index of dispersion and its chi-squared test, Lloyd's mean crowding, Taylor's power law, the Clark–Evans nearest-neighbor ratio and Ripley's K and L functions; scale and the causes of pattern; plant architecture."
---

With this chapter we move from the individual organism to the population. Population ecology asks how many individuals of a species there are, where they are, how their numbers change and why. All these questions begin with measurement, and the measurement of abundance is far from trivial: animals hide, move and are rarely seen all at once, and plants and other modular organisms do not even come in obvious units. We therefore start with the concept of a population and of the individuals that compose it, then treat the methods of estimating population size and density, which are statistical estimation problems ([3.2](/3.2)), and finally the description and analysis of the spatial pattern of individuals. The changes of numbers in time, births and deaths in life tables, population growth and its regulation, are the subjects of the following chapters ([7.19.9](/7.19.9)–[7.19.17](/7.19.17)); the genetic structure of populations is treated in evolutionary biology ([7.10](/7.10)) and, from the ecological side, in [7.19.20](/7.19.20).

## 8.1. The Population

### 8.1.1. Definition and Basic Features

**Definition 8.1.1 (Population)** A group of individuals of the same species that occupy a particular area at the same time is called a **population**.

The definition leaves the boundaries to the investigator. Sometimes they are obvious (the sticklebacks of a small lake, the lizards of an island); often they are set by the purpose of the study (the aphids of one leaf, one tree or one wood); and when a species is distributed continuously over a large area, a population is an arbitrary portion of it, and density is then the more useful quantity. A population in the ecological sense is a real biological entity and must not be confused with the statistical population ([3.2](/3.2)), the set of all possible observations from which a sample is drawn, although the population ecologist constantly draws statistical samples from biological populations.

Populations are the units in which species exist in nature, the units of evolution (allele frequencies change in populations, [7.10](/7.10)) and the components of communities ([7.19.31](/7.19.31)). A population has properties that individuals do not have:

- spatial properties: a distribution area and a pattern of individuals within it (Section 8.4);
- numerical properties: size and density, and the rates of birth, death, immigration and emigration that change them;
- genetic properties: a gene pool with a particular composition and diversity, which also changes;
- system properties: interactions among individuals (competition, cooperation, mating) that regulate the population and give it a degree of self-organization.

### 8.1.2. Unitary and Modular Organisms

Counting the individuals of a population assumes that we know what an individual is. For many organisms this is not obvious.

**Definition 8.1.2 (Unitary and Modular Organisms)** An organism whose form and sequence of life-cycle phases are determinate, each individual developing directly from a zygote into a body with a fixed number of parts, is called a **unitary organism**. An organism that grows by the repeated production of units of construction (modules: leaves with their buds, shoots, polyps, zooids), forming a usually branched structure whose form and development are indeterminate, is called a **modular organism**.

Mammals, birds, insects and most other animals are unitary: a dog has four legs whether it lives a short or a long time, and the crows that roost at night on the Tsinghua campus can be counted as discrete individuals. Most plants, fungi, sponges, corals, hydroids, bryozoans and colonial ascidians are modular: the same germinating seed may produce a stunted sapling with a handful of leaves or a branching tree with tens of thousands of leaves, depending on its circumstances.

**Definition 8.1.3 (Genet and Ramet)** The genetic individual derived from one zygote, together with all modules produced from it, is called a **genet**. A module or group of modules that is capable of independent existence, whether or not it is still connected to the rest of the genet, is called a **ramet**.

Ramets arise when the connections between parts of a genet (stolons, rhizomes, root suckers) die or are broken: strawberry plants spread by runners, duckweeds and water hyacinth fall to pieces as they grow and can fill a whole lake with the ramets of a few genets, *Hydra* produces new individuals by budding, and the banyan fig *Ficus annulata* forms "a forest from a single tree" through aerial roots that thicken into trunks. One genet of quaking aspen (*Populus tremuloides*) in Utah, known as Pando, consists of about 47 000 stems over 43 ha, with an estimated mass of some 6000 t. For modular organisms both levels matter: the number of genets describes genetic diversity and the outcome of selection, but the number of modules (leaves, tillers, polyps) often determines ecological effects, such as the amount of grass available to grazing cattle.

Modular organisms differ from unitary ones in several further respects:

- Growth form: some concentrate growth vertically (trees, in which the connecting stem becomes wood and persists), others spread laterally over or in a substrate (stoloniferous and rhizomatous plants, encrusting corals and bryozoans); modules are often organized at several levels (leaves into rosettes in the strawberry, shoots into branch systems in trees).
- Age structure within the individual: modules are born and die continually, and the age structure of the leaves of a plant can change with resources: in the herb *Wedelia trilobata*, fertilization increases both the birth and the death rates of leaves, so fertilized plants carry more and younger leaves (Suárez 2016).
- Senescence: many modular organisms show no increase in mortality with age (trees, gorgonian corals), whereas their modules senesce; whole organisms die from becoming too large or from disease rather than from programmed senescence.
- Integration: connected ramets share resources, and the balance of costs and benefits changes with age. In the grass *Holcus lanatus*, young daughter ramets grow better when connected to their parent; older daughters suffer from competition with the parent, and for daughters eight weeks old the connection becomes a drain rather than a benefit (Bullock et al. 1994).

### 8.1.3. The Questions of Population Dynamics

Population dynamics is the study of the changes of population size and distribution in time and space. It asks four questions: how many individuals there are (size and density); where they are (distribution and pattern); how their numbers change (growth, fluctuation, dispersal); and why (regulation). The basic accounting identity of population ecology is:

**Formula 8.1.1 (BIDE Equation)** The number of individuals in a population changes between two times according to

$$
N_{t+1} = N_t + B - D + I - E,
$$
where $B$ and $D$ are the numbers of births and deaths and $I$ and $E$ the numbers of immigrants and emigrants in the interval.

Every model of population dynamics in the following chapters is a hypothesis about how the four terms depend on the population itself, on other populations and on the environment. Measuring them is hard: births often occur unseen (half of the embryos of many mammals and plants die before birth or seed maturation), dead bodies disappear quickly, and losses through death and emigration are difficult to tell apart.

## 8.2. Size and Density

The *population size* is the number of individuals in a defined area (sometimes measured as biomass or energy content); *population density* is the size per unit of area, volume or habitat (per square kilometer, per liter of water, per leaf or per host). Density can be expressed per unit of total area (crude density) or per unit of the habitat actually used (ecological density); the two can differ greatly for species confined to patches of habitat. Absolute density is the actual number per unit area; relative density (an index of abundance) only allows comparisons in time or space (Section 8.3.8). For modular organisms one must state whether genets, ramets or modules are counted.

The conservation of large mammals shows why accurate numbers matter. The Asian elephant (*Elephas maximus*), whose historical range in China reached the Yellow River valley some 3000 years ago, now survives in China only in southern Yunnan (Xishuangbanna, Pu'er and Lincang), with about 300 individuals; whether this number is rising or falling, and how fast, determines the management of a species that increasingly comes into conflict with farmers.

## 8.3. Estimating Abundance

### 8.3.1. Total Counts

A complete count (census) of all individuals is possible only when the individuals are conspicuous and the area well defined: colonies of seabirds, large mammals on open plains counted from the air, trees in a forest plot, or birds gathering at a communal roost. Every winter the crows that roost at night on the Tsinghua University campus in Beijing are counted by students of the university's animal protection association as the birds fly in at dusk: 6067 in early 2023, 4905 on 30 December 2024 and 3921 on 6 February 2026 (1728 in the area near the southeast gate and 2193 near the Zijing dormitories). Even a total count is an estimate with errors: birds are missed or counted twice, and the date matters, since the number of birds using a winter roost changes through the season with weather and food. A series of counts made with the same method on comparable dates is therefore more informative about trends than any single count.

### 8.3.2. Quadrats

For organisms that do not move much (plants, sessile animals, soil animals), abundance is estimated by counting the individuals in sample units.

**Definition 8.3.1 (Quadrat)** A sample plot of fixed size and shape (classically a square, also the name of the frame used to mark it) within which all individuals are counted is called a **quadrat**.

If $n$ quadrats of area $a$ are placed at random in a study area of area $A$ and contain $x_1, \dots, x_n$ individuals, the mean density is estimated by $\bar x/a$ and the total population by

$$
\hat N = \frac{A}{a}\,\bar x, \qquad \widehat{\operatorname{Var}}(\hat N) = \left(\frac{A}{a}\right)^2\frac{s^2}{n}\left(1 - \frac{na}{A}\right),
$$
where $s^2$ is the sample variance of the counts and the last factor is the finite-population correction ([3.2](/3.2)). The precision therefore depends on the variance among quadrats, which in turn depends on the spatial pattern of the population (Section 8.4): for a clumped population, many small quadrats give a more precise estimate than a few large ones of the same total area. Quadrats must be representative, which is ensured by random placement; systematic placement on a grid covers the area evenly and is often more precise when density varies smoothly, but it can give biased variance estimates and fail when the pattern is periodic; stratified random sampling places quadrats at random within strata (habitats) and estimates each stratum separately. The size of the quadrat is chosen according to the size and density of the organism: 0.1–1 m² for herbs, 100–1000 m² for trees.

The most complete form of plot sampling is the large permanent forest plot, in which every woody stem above 1 cm in diameter is mapped, measured and identified, and the census is repeated every five years. The 20 ha (200 000 m²) plot on Dongling Mountain near Beijing, part of the Chinese Forest Biodiversity Monitoring Network and the global ForestGEO network, records warm-temperate deciduous forest in this way; such plots provide the mapped data from which spatial patterns (Section 8.4) and demographic rates of trees are estimated.

### 8.3.3. Transects, Point Counts and Distance Sampling

Mobile animals that are seen or heard, especially birds, are counted along line transects (the observer walks a predetermined route and records all individuals detected on both sides) or at point counts (the observer stands at fixed points for a fixed time and records all individuals within a radius). Both methods give indices unless the probability of detection is estimated, because individuals far from the observer are more likely to be missed. Distance sampling estimates this probability from the distances at which animals are detected (Buckland et al. 2001).

Along a transect of length $L$, let $g(x)$ be the probability of detecting an animal at perpendicular distance $x$, with $g(0) = 1$ (animals on the line are always seen). The *effective strip half-width* is $\mu = \int_0^\infty g(x)\,\mathrm{d}x$: the number of animals detected is, on average, the number that would be counted in a strip of half-width $\mu$ if all were seen. If $n$ animals are detected, the density is estimated by

$$
\hat D = \frac{n}{2L\hat\mu}.
$$
The detection function is estimated from the distribution of observed distances, whose density is $f(x) = g(x)/\mu$. For the half-normal model $g(x) = \mathrm{e}^{-x^2/(2\sigma^2)}$, $\mu = \sigma\sqrt{\pi/2}$, and the **maximum likelihood estimator** of $\sigma$ from distances $x_1, \dots, x_n$ is $\hat\sigma = \left(\frac{1}{n}\sum x_i^2\right)^{1/2}$ (figure below). For point counts, with radial distances $r$ and detection function $g(r)$, the density is $\hat D = n/(k\pi\hat\rho^2)$ for $k$ points, where $\rho^2 = 2\int_0^\infty r\,g(r)\,\mathrm{d}r$ defines the effective radius ($\rho^2 = 2\sigma^2$ for the half-normal). The method assumes that animals on the line or point are detected with certainty, that they are detected at their initial position before moving in response to the observer, and that distances are measured accurately.

![Removal and distance sampling. A: Leslie regression for a removal study with six successive catches of equal effort (42, 31, 27, 18, 16 and 12 animals): each catch is plotted against the number already removed, and the fitted line meets the horizontal axis at the estimated population size, about 188 (Example 8.3.2). B: perpendicular distances of 300 simulated detections from a line transect, with the fitted half-normal detection function; the dashed line is the effective strip half-width $\mu$, the distance within which as many animals would be counted, if all were seen, as are actually detected at all distances.](./plots/removal-and-distance.py)

### 8.3.4. Camera Traps and Occupancy

Camera traps, triggered by the heat and movement of passing animals, record secretive and nocturnal mammals over months without disturbance. Individually recognizable animals (tigers, snow leopards and other spotted or striped cats) can be "captured" and "recaptured" in photographs and analyzed by capture–recapture methods (Section 8.3.6), in modern work by spatially explicit capture–recapture, which also estimates the area each individual uses. For species without individual marks, cameras are often used to estimate occupancy: the proportion of sites (camera locations or grid cells) at which a species is present.

The difficulty is that a species can be present at a site and not be detected. In the occupancy model of MacKenzie et al. (2002), each of $S$ sites is occupied with probability $\psi$, and at an occupied site the species is detected on each of $K$ visits (or sampling days) independently with probability $p$. The probability of a detection history, for example "detected on visits 1 and 3 of 3", is $\psi p(1 - p)p$; the probability of never detecting the species at a site is $\psi(1 - p)^K + (1 - \psi)$, the sum of occupied-but-missed and unoccupied. Maximizing the product of these probabilities over sites estimates $\psi$ and $p$ separately. The naive occupancy, the fraction of sites where the species was detected at least once, estimates $\psi\left[1 - (1 - p)^K\right] < \psi$ and is biased low; with $p = 0.2$ and $K = 5$ visits, two thirds of occupied sites are recognized ($1 - 0.8^5 = 0.67$). Occupancy is related to abundance but is not the same thing: an occupied site may hold one animal or many.

### 8.3.5. Passive Acoustic Monitoring

Autonomous recorders left in the field record sound continuously for weeks or months at low cost and without disturbance. Passive acoustic monitoring is similar to a point count with a microphone instead of an observer, but it produces enormous amounts of data that must be analyzed automatically, by species-recognition algorithms (increasingly deep-learning classifiers) or by acoustic indices that summarize the soundscape: the acoustic complexity index (variability of intensity in each frequency band), the acoustic diversity index and acoustic entropy (evenness of sound among frequency bands and times), the bioacoustic index (sound energy in the bands used by birds) and the normalized difference soundscape index (the ratio of biological to anthropogenic sound). These indices correlate with species richness, but the correlation varies among habitats.

For the abundance of a single species, the simplest acoustic measure is the vocal activity rate (VAR), the number of vocalizations of the species per unit time. In a study in Spain, VAR increased linearly with the number of European bee-eaters (*Merops apiaster*) present at a colony, but it saturated with the number of Dupont's larks (*Chersophilus duponti*), whose territorial males sing less as density rises; VAR is thus a usable index of abundance only after it has been calibrated for each species.

### 8.3.6. Mark–Recapture

For mobile animals that can be caught and marked, the most widely used method is the following.

**Definition 8.3.2 (Mark–Recapture)** A method of estimating population size and demographic rates in which animals are caught, marked individually or as a batch, released and recaptured in later samples, the proportion of marked animals among those recaptured being used to estimate the size of the population, is called **mark–recapture** (capture–recapture).

In the simplest design, $M$ animals are caught, marked and released; after they have mixed with the rest of the population, a second sample of $n$ animals is caught, of which $m$ are marked. If the proportion of marked animals is the same in the sample as in the population, $m/n = M/N$, which gives the Lincoln–Petersen estimator

$$
\hat N_{\mathrm{LP}} = \frac{Mn}{m}.
$$

**Proposition 8.3.1 (Lincoln–Petersen as Maximum Likelihood)** In a closed population of size $N$ in which all individuals have the same probability of capture, the number $m$ of marked animals in the second sample has a **hypergeometric distribution**, and the maximum likelihood estimate of $N$ is the integer part of $Mn/m$.

**Proof** If the second sample is a random sample of $n$ from the $N$ animals, of which $M$ are marked, then $\mathbb{P}(m \mid N) = \binom{M}{m}\binom{N - M}{n - m}\big/\binom{N}{n}$. As a function of $N$, the ratio of successive likelihoods is

$$
\frac{L(N)}{L(N - 1)} = \frac{(N - M)(N - n)}{N(N - M - n + m)},
$$
which is at least 1 if and only if $(N - M)(N - n) \geq N(N - M - n + m)$, that is $Mn \geq Nm$, or $N \leq Mn/m$. The likelihood therefore increases up to $N = \lfloor Mn/m\rfloor$ and decreases afterwards. $\square$

The estimator is biased upward in small samples (and undefined when $m = 0$). Chapman's modification,

$$
\hat N_{\mathrm{C}} = \frac{(M + 1)(n + 1)}{m + 1} - 1,
$$
is nearly unbiased when $M + n \geq N$, and its variance is estimated by

$$
\widehat{\operatorname{Var}}(\hat N_{\mathrm{C}}) = \frac{(M + 1)(n + 1)(M - m)(n - m)}{(m + 1)^2(m + 2)}
$$
(Seber 1970); an approximate 95% confidence interval is $\hat N_{\mathrm{C}} \pm 2\,\mathrm{SE}$, though for small $m$ intervals based on the distribution of $m$ are better, since the distribution of $\hat N$ is strongly skewed.

**Example 8.3.1** In a pond, 50 newts are caught, marked with a toe clip and released; a week later, 60 are caught, of which 8 are marked. Estimate the population size with a confidence interval.

**Solution** $\hat N_{\mathrm{LP}} = 50 \times 60/8 = 375$; $\hat N_{\mathrm{C}} = 51 \times 61/9 - 1 = 344.7 \approx 345$. The variance is $51 \times 61 \times 42 \times 52/(81 \times 10) = 8388$, so $\mathrm{SE} \approx 92$ and the approximate 95% interval is about 160–530. With only 8 recaptures the estimate is very imprecise; to reach a coefficient of variation of about 10%, roughly 100 marked recaptures are needed, since the coefficient of variation is approximately $1/\sqrt{m}$.

:::

The method rests on assumptions, each of which can fail:

1. The population is closed: no births, deaths, immigration or emigration between samples (in practice, the interval is short relative to the turnover of the population).
2. All individuals have the same probability of capture in each sample, and marking does not change it.
3. Marks are not lost and are correctly recorded.
4. Marked animals mix randomly with unmarked ones.

Violations of assumption 2 are the most common and the most serious. Animals that learn to enter traps for bait ("trap-happy") are recaptured more often than expected, which inflates $m$ and leads to underestimation of $N$; "trap-shy" animals have the opposite effect. Even without behavioral responses, individuals differ in catchability (by age, sex, social status or the position of their home range relative to the traps), and heterogeneity always biases two-sample estimates downward, because the same catchable animals tend to appear in both samples (figure below). Many-sample designs allow these effects to be modeled. The Schnabel method for a closed population sampled $t$ times, with $C_i$ animals caught in sample $i$, $R_i$ of them already marked and $M_i$ marked animals in the population before sample $i$, uses $\hat N = \sum C_iM_i/\sum R_i$. For open populations, the Jolly–Seber model estimates, for each sampling occasion, the population size, the survival rate (strictly, apparent survival, which includes permanent emigration) and the number of new animals entering; its modern descendants (Cormack–Jolly–Seber models, implemented in programs such as MARK) are among the main tools for estimating survival rates of wild animals ([7.19.9](/7.19.9)).

![Mark–recapture estimators. A: sampling distributions of the Lincoln–Petersen and Chapman estimators in 50 000 simulated studies of a closed population of 400 animals, with 50 marked and a second sample of 60 (on average 7.5 recaptures). The distributions are skewed and wide; the Lincoln–Petersen estimator overestimates on average, Chapman's estimator is nearly unbiased. B: effect of individual heterogeneity in catchability (capture probabilities drawn from beta distributions with mean 0.14 and increasing coefficient of variation): the same easily caught animals tend to be caught twice, the proportion of marked animals in the second sample is too high, and the population is increasingly underestimated.](./plots/mark-recapture.py)

### 8.3.7. Removal Sampling

When animals are removed (trapped and killed, or kept until the end of the study) rather than released, the decline of the catch with successive equal-effort removals estimates the population. Suppose that in a closed population each animal is caught with probability $p$ in each removal. If $K_i$ animals have been removed before removal $i$, the expected catch is

$$
\mathbb{E}[C_i] = p\,(N - K_i).
$$
A plot of $C_i$ against $K_i$ is therefore a straight line with slope $-p$ and intercept $pN$, which meets the $K$ axis at $K = N$ (Leslie and Davis 1939). Fitting the line by least squares ([3.3](/3.3)) estimates $p$ and $N$. With only two removals, the equations $C_1 = pN$ and $C_2 = p(N - C_1)$ give

$$
\hat N = \frac{C_1^2}{C_1 - C_2}, \qquad \hat p = 1 - \frac{C_2}{C_1},
$$
which requires $C_2 < C_1$ (Seber and Le Cren 1967); more removals are analyzed by the maximum likelihood method of Zippin (1958). The assumptions are a closed population and a constant capture probability, which fails if the most catchable animals are taken first, again leading to underestimation. Removal methods are used for small mammals (removal trapping on a grid of traps, known in Chinese practice as a variant of the "standard minimum" method), for fishes caught by successive passes of electrofishing in a stream section blocked by nets, and for pests and fishery stocks, where the catch per unit effort declines as the stock is fished down.

**Example 8.3.2** Successive removals of equal effort from a vole population gave catches of 42, 31, 27, 18, 16 and 12. Estimate the population size by the Leslie regression and by the two-pass formula applied to the first two catches.

**Solution** The numbers removed before each catch are $K_i = 0, 42, 73, 100, 118, 134$. Regression of $C_i$ on $K_i$ gives slope $-0.221$ and intercept $41.6$, so $\hat p = 0.22$ and $\hat N = 41.6/0.221 \approx 188$ (figure above, panel A). The two-pass estimate is $42^2/(42 - 31) = 160$, with $\hat p = 0.26$. The two-pass estimate uses only part of the information and is sensitive to sampling error in two catches; here the third catch (27) is larger than the trend, and the regression over all six removals is preferable. A total of 146 animals has been removed, so about 40 remain by the regression estimate.

:::

### 8.3.8. Relative Abundance

When absolute numbers cannot be obtained, an index of abundance proportional to population size can still show changes in time and differences between places: the number caught per trap-night (snap traps for rodents, pitfall traps for ground beetles, light traps for moths), plankton per net haul, fecal pellet counts for deer, call counts for frogs and birds (the "calling rank" of leopard frogs at ponds), the number of burrows, nests, earth mounds or tracks in snow, fur returns of trapping companies (the Hudson's Bay Company records of lynx and snowshoe hare, [7.19.25](/7.19.25)), and the catch per unit effort (CPUE) of fisheries.

Every index assumes that it is proportional to abundance, $I = qN$, with a constant catchability $q$. If $q$ changes, the index misleads. In fisheries, CPUE often remains high while a stock declines, because fishers concentrate on the remaining aggregations of fish and improve their technology, a phenomenon called hyperstability; it contributed to the failure to recognize the collapse of the northern cod stock off Newfoundland, which was closed to fishing in 1992. Conversely, an index can decline without any change in abundance if behavior changes (fewer calls at high density, as in the larks of Section 8.3.5). Indices should therefore be calibrated against absolute estimates whenever possible.

## 8.4. Spatial Pattern

### 8.4.1. Three Types of Dispersion

**Definition 8.4.1 (Dispersion Pattern)** The spatial arrangement of the individuals of a population within its habitat is called its **dispersion pattern** (internal distribution pattern). Three basic types are distinguished by comparison with a random arrangement: in a regular (uniform) pattern individuals are more evenly spaced than at random; in a random pattern each individual has the same probability of occurring at any point, independently of the others; and in a clumped (aggregated, contagious) pattern individuals are closer together than at random.

The three types form a continuum. Regular patterns arise when individuals avoid or inhibit each other: **territory** holders, nesting colonial seabirds pecking at their neighbors, desert shrubs competing for water, trees thinned by competition, and plantations. Random patterns arise when the environment is uniform and individuals neither attract nor repel each other; they are rare in nature (flour beetles in a jar of flour are the classic example). Clumped patterns, by far the most common, arise from three kinds of causes: the heterogeneity of the habitat (individuals aggregate where conditions and resources are favorable), the mode of reproduction and dispersal (seeds falling near the parent, clonal growth, offspring that stay near their birthplace) and social behavior (the **selfish herd**, flocks, schools and colonies, cooperative breeding among philopatric relatives).

Pattern depends on scale. Aphids living on one tree species appear clumped in a landscape (they occur only in woodland), clumped within the wood (only on their host trees), perhaps random within the canopy of one tree, and regular at the scale of a leaf, where individuals keep apart. A statement about dispersion is therefore meaningful only for a stated scale, which in quadrat methods is the quadrat size and in distance methods the range of distances examined. The terminology also needs care: older ecological texts call regular patterns "overdispersed" and clumped ones "underdispersed", whereas in statistics overdispersion means a variance greater than the mean, which is the signature of clumping; the terms are best avoided.

### 8.4.2. Quadrat Counts: Poisson and Negative Binomial

If individuals are placed independently and uniformly over an area with mean density $\lambda$ per quadrat area, the number in a quadrat follows a **Poisson distribution** ([3.1.4](/3.1.4)), $\mathbb{P}(X = x) = \mathrm{e}^{-\lambda}\lambda^x/x!$, because the quadrat contains a small fraction of the many individuals, each independently ([7.5.36](/7.5.36) and the law of rare events). The Poisson distribution has its variance equal to its mean, which suggests comparing the two.

**Definition 8.4.2 (Index of Dispersion)** For counts $x_1, \dots, x_n$ in $n$ quadrats with mean $\bar x$ and sample variance $s^2$, the ratio $I = s^2/\bar x$ is called the **index of dispersion** (variance-to-mean ratio). $I \approx 1$ suggests a random pattern, $I < 1$ a regular pattern (in the limit of perfect regularity every quadrat has the same count and $I = 0$) and $I > 1$ a clumped pattern.

**Proposition 8.4.1 (Index-of-Dispersion Test)** If the counts are independent Poisson variables with the same mean, the statistic

$$
\chi^2 = \frac{(n - 1)s^2}{\bar x} = \sum_{i=1}^n\frac{(x_i - \bar x)^2}{\bar x}
$$
has approximately a $\chi^2_{n-1}$ distribution (for $\bar x$ not too small, roughly $\bar x \geq 1$ with $n \geq 10$).

**Proof** The second form of the statistic is the Pearson goodness-of-fit statistic for a table of $n$ cells with observed counts $x_i$ and equal expected counts $\bar x$, which, conditional on the total $\sum x_i$, is the test of a multinomial with equal cell probabilities; conditional on the total, independent Poisson counts with equal means are multinomial with equal probabilities, and the Pearson statistic is asymptotically $\chi^2$ with $n - 1$ degrees of freedom ([3.6.12](/3.6.12)). $\square$

Values of $\chi^2$ in the upper tail indicate clumping, values in the lower tail regularity. A clumped pattern is often described by the **negative binomial distribution**, with mean $\mu$ and variance $\mu + \mu^2/k$; the parameter $k > 0$, the **dispersion parameter**, measures aggregation inversely: as $k \to \infty$ the distribution tends to the Poisson, and small $k$ (below about 1) indicates strong clumping. A natural mechanism produces it.

**Proposition 8.4.2 (Gamma–Poisson Mixture)** If the count in a quadrat is Poisson with mean $\Lambda$ and $\Lambda$ varies among quadrats according to a **gamma distribution** with shape $k$ and mean $\mu$, then the counts have a negative binomial distribution with mean $\mu$ and variance $\mu + \mu^2/k$.

**Proof** With $\Lambda \sim \Gamma(k, k/\mu)$ (shape $k$, rate $k/\mu$),

$$
\mathbb{P}(X = x) = \int_0^\infty \frac{\mathrm{e}^{-\lambda}\lambda^x}{x!}\cdot\frac{(k/\mu)^k\lambda^{k-1}\mathrm{e}^{-k\lambda/\mu}}{\Gamma(k)}\,\mathrm{d}\lambda
= \frac{\Gamma(x + k)}{x!\,\Gamma(k)}\left(\frac{k}{k + \mu}\right)^k\left(\frac{\mu}{k + \mu}\right)^x,
$$
using $\int_0^\infty\lambda^{x+k-1}\mathrm{e}^{-\lambda(1 + k/\mu)}\,\mathrm{d}\lambda = \Gamma(x + k)(1 + k/\mu)^{-(x+k)}$; this is the negative binomial probability function. By the laws of total expectation and variance, $\mathbb{E}X = \mathbb{E}\Lambda = \mu$ and $\operatorname{Var}(X) = \mathbb{E}\Lambda + \operatorname{Var}(\Lambda) = \mu + \mu^2/k$. $\square$

The proposition says that a population that is random within patches whose quality varies is clumped overall, with $1/k$ equal to the squared coefficient of variation of the local mean density; it is one reason why the negative binomial fits so many ecological counts (insects per plant, parasites per host).

**Example 8.4.1** The numbers of a herb in 100 quadrats of 1 m² were: 0 individuals in 30 quadrats, 1 in 18, 2 in 14, 3 in 10, 4 in 8, 5 in 6, 6 in 4, 7 in 3, 8 in 3, 9 in 2 and 10 in 2. Test for randomness and fit a negative binomial distribution.

**Solution** $\bar x = 245/100 = 2.45$ and $s^2 = 6.94$, so $I = 2.83$. The test statistic is $\chi^2 = 99 \times 2.83 = 280$ on 99 degrees of freedom; since $\chi^2_{99}$ has mean 99 and standard deviation $\sqrt{198} \approx 14$, the value lies about 13 standard deviations above the mean ($p \approx 10^{-19}$), and the hypothesis of a random pattern is firmly rejected in favor of clumping. The moment estimate of $k$ is $\hat k = \bar x^2/(s^2 - \bar x) = 6.00/4.49 = 1.34$. The Poisson distribution with mean 2.45 predicts 8.6 empty quadrats against 30 observed and too many quadrats with 2–4 plants, whereas the negative binomial fits well (figure below; a formal goodness-of-fit test would pool the sparse classes and lose one further degree of freedom for $\hat k$).

:::

![Quadrat counts. A: frequency distribution of counts in 100 quadrats (Example 8.4.1) with the expected frequencies under the Poisson distribution of the same mean and under the negative binomial distribution with $k$ estimated by the method of moments: the Poisson underestimates both empty quadrats and quadrats with many individuals. B: sample variance against sample mean for sets of 50 quadrats taken from random (Poisson) and clumped (negative binomial, $k$ = 2 and 0.5) populations over a range of densities; the lines are $s^2 = \bar x$ and $s^2 = \bar x + \bar x^2/k$. On logarithmic axes the clumped populations have slopes approaching 2 at high density, as described by Taylor's power law.](./plots/quadrat-counts.py)

The index of dispersion depends on density: for the negative binomial, $I = 1 + \mu/k$. Two measures avoid this. Lloyd's mean crowding, $m^* = \bar x + (s^2/\bar x - 1)$, estimates the average number of other individuals in the same quadrat as a randomly chosen individual, which is what an individual experiences; the patchiness index $m^*/\bar x$ equals 1 for a random pattern and $1 + 1/k$ for the negative binomial, independent of density. Across many samples of the same species at different densities, the variance is often a power function of the mean, $s^2 = a\,\bar x^b$ (Taylor's power law), with $b$ between 1 (random) and about 2 (strongly aggregated); $b$ is roughly a species characteristic and is used to design sampling plans for pest insects.

### 8.4.3. Nearest-Neighbor Distances

Quadrat methods depend on the quadrat size. When the positions of individuals have been mapped (trees in a plot, nests in a colony), distances between them can be used instead. In a completely random (Poisson) pattern of density $\rho$ individuals per unit area, the probability that there is no other individual within distance $r$ of a given individual is the probability that a circle of area $\pi r^2$ is empty, $\mathrm{e}^{-\rho\pi r^2}$. The nearest-neighbor distance therefore has the density $f(r) = 2\pi\rho r\,\mathrm{e}^{-\rho\pi r^2}$ (a Rayleigh distribution), with mean and variance

$$
\mathbb{E}[r] = \frac{1}{2\sqrt\rho}, \qquad \operatorname{Var}(r) = \frac{4 - \pi}{4\pi\rho}.
$$
Clark and Evans (1954) compared the observed mean nearest-neighbor distance $\bar r$ with this expectation through the ratio $R = 2\bar r\sqrt\rho$: $R = 1$ for a random pattern, $R < 1$ for a clumped pattern (approaching 0 when all individuals are at the same point) and $R > 1$ for a regular pattern, with a maximum of $2.149$ for a hexagonal lattice. The significance of a departure is tested with $z = (\bar r - \mathbb{E}r)/\mathrm{SE}$, $\mathrm{SE} = 0.26136/\sqrt{n\rho}$ for $n$ individuals. Individuals near the edge of the mapped area have their true nearest neighbors outside it, which biases $\bar r$ upward unless a buffer zone is used.

### 8.4.4. Ripley's K and L Functions

The nearest-neighbor ratio describes pattern at one, small scale. Ripley's K function describes it at all scales at once. For a stationary point pattern of intensity $\lambda$ (individuals per unit area), $\lambda K(r)$ is the expected number of further individuals within distance $r$ of a typical individual (**Ripley's K function**, [7.9.6](/7.9.6)). For complete spatial randomness, the **Poisson process** of points, $K(r) = \pi r^2$. It is convenient to use the variance-stabilized transform $L(r) = \sqrt{K(r)/\pi}$, for which $L(r) = r$ under randomness: $L(r) - r > 0$ indicates clumping at scale $r$ (more neighbors within $r$ than expected) and $L(r) - r < 0$ regularity. $K$ is estimated by counting, for each individual, the others within distance $r$, with an edge correction, and dividing by $\lambda$ and the number of individuals. Because the sampling distribution of $\hat L$ is complex, significance is judged against simulation envelopes: many random patterns with the same number of points in the same area are generated, and the observed $\hat L(r) - r$ is compared with their range at each $r$ (figure below).

The function reveals patterns that change with scale: the clumped pattern of the figure has positive $L(r) - r$ up to beyond the size of the clusters, with a maximum near the cluster radius; the regular pattern has a marked deficit of neighbors below the inhibition distance. Mapped tree plots analyzed in this way typically show that seedlings and saplings are strongly clumped around parents and in gaps, and that the clumping decreases with size class as density-dependent mortality thins the clumps ([7.19.37](/7.19.37)); bivariate versions of $K$ test whether two species or two size classes attract or repel each other.

![Spatial point patterns. A–C: a regular pattern (sequential inhibition: no two points closer than 0.055), a random pattern (Poisson process) and a clumped pattern (Thomas process: clusters around 20 random parent points), each with 150 points in a unit square with periodic boundaries. D: Ripley's $L(r) - r$ for the three patterns with the envelope of 99 random patterns (grey): the random pattern stays within the envelope, the clumped pattern lies above it at all scales up to about 0.2, with a maximum near the cluster size, and the regular pattern lies below it, most strongly at the inhibition distance.](./plots/point-patterns.py)

### 8.4.5. Plant Architecture

Within the individual, modular organisms also have a spatial structure. The architecture of a plant is the spatial arrangement of its repeated modules: the pattern of branching (monopodial or sympodial), the orientation of shoots (orthotropic or plagiotropic), the positions of flowering, and the rhythm of growth. Hallé and Oldeman (1970) showed that the growth patterns of tropical trees can be described by about two dozen architectural models, each a program of how meristems grow, branch and flower. Architecture determines how a plant intercepts light and displays its leaves, how it occupies space and shades or tolerates neighbors, and how it responds to damage: it is the link between the modular construction of plants and their interactions with the environment and with each other.

## Summary

- A population is a group of individuals of one species in one area at one time (Definition 8.1.1), the unit of species existence, evolution and community composition, with spatial, numerical, genetic and system properties.
- Unitary organisms have determinate form; modular organisms grow by repeating modules (Definition 8.1.2), so the genet and its ramets (Definition 8.1.3) must be distinguished; modules have their own births, deaths and age structure; connected ramets are physiologically integrated.
- Population dynamics asks how many, where, how they change and why; the BIDE equation $N_{t+1} = N_t + B - D + I - E$ (Formula 8.1.1) is the basic accounting.
- Size and density (crude, ecological; absolute, relative) are estimated by total counts (the Tsinghua crow counts, 6067, 4905 and 3921), quadrats ($\hat N = A\bar x/a$, precision set by the variance among quadrats), transects, point counts and distance sampling ($\hat D = n/(2L\hat\mu)$, half-normal $\mu = \sigma\sqrt{\pi/2}$), camera traps and occupancy models (naive occupancy $\psi[1 - (1 - p)^K]$ is biased low), and passive acoustic monitoring (acoustic indices; VAR must be calibrated).
- Mark–recapture (Definition 8.3.2): Lincoln–Petersen $Mn/m$ is the maximum likelihood estimate under the hypergeometric model (Proposition 8.3.1); Chapman's $(M + 1)(n + 1)/(m + 1) - 1$ is nearly unbiased; assumptions are closure, equal catchability, permanent marks and mixing; heterogeneity and trap-happiness cause underestimation; Schnabel and Jolly–Seber methods extend the design.
- Removal sampling: $\mathbb{E}[C_i] = p(N - K_i)$, so the Leslie regression meets the axis at $N$; two removals give $C_1^2/(C_1 - C_2)$. Relative indices assume constant catchability; CPUE can be hyperstable.
- Dispersion is regular, random or clumped (Definition 8.4.1) and depends on scale. Random quadrat counts are Poisson; the index of dispersion $s^2/\bar x$ (Definition 8.4.2) is tested by $(n - 1)s^2/\bar x \sim \chi^2_{n-1}$ (Proposition 8.4.1); patchy Poisson counts are negative binomial with variance $\mu + \mu^2/k$ (Proposition 8.4.2); mean crowding and Taylor's power law describe aggregation independently of density.
- Mapped patterns: the Clark–Evans ratio $R = 2\bar r\sqrt\rho$ (1 random, < 1 clumped, up to 2.149 regular) and Ripley's $L(r) - r$ with simulation envelopes, which describe pattern at all scales. Plant architecture is the spatial pattern of modules within an individual.

## Questions

1. In a mark–recapture study of a lizard population, 120 lizards are marked; in the second sample 100 are caught, of which 30 are marked. Calculate the Lincoln–Petersen and Chapman estimates and an approximate 95% confidence interval. If the lizards that are easy to catch tend to be caught in both samples, in which direction is the estimate biased?

   **Answer** $\hat N_{\mathrm{LP}} = 120 \times 100/30 = 400$; $\hat N_{\mathrm{C}} = 121 \times 101/31 - 1 = 393.2$. Variance: $121 \times 101 \times 90 \times 70/(31^2 \times 32) = 2.50\times10^3$, $\mathrm{SE} \approx 50$, so the approximate 95% interval is $393 \pm 100$, about 293–493. If catchable animals tend to be caught twice, the proportion marked in the second sample exceeds the proportion marked in the population, $m$ is too large and $N$ is underestimated: the true population is probably larger than 393.

2. Show that, in the removal model $\mathbb{E}[C_i] = p(N - K_i)$, the expected catches decline geometrically, $\mathbb{E}[C_i] = pN(1 - p)^{i-1}$. What does a plot of $\ln C_i$ against $i$ estimate, and how does it relate to the Leslie regression?

   **Answer** After $i - 1$ removals, each original animal remains with probability $(1 - p)^{i-1}$, so the expected number remaining is $N(1 - p)^{i-1}$ and the expected catch is $p$ times that. Equivalently, $N - K_i$ decreases by the factor $(1 - p)$ per removal in expectation. Hence $\ln\mathbb{E}[C_i] = \ln(pN) + (i - 1)\ln(1 - p)$: a plot of $\ln C_i$ against $i$ (the DeLury method) is linear with slope $\ln(1 - p)$ and intercept $\ln(pN)$, from which $p$ and $N$ follow. The Leslie regression uses cumulative catch as the explanatory variable instead of the removal number; both estimate the same parameters, but the DeLury method is preferable when effort varies (catch per unit effort against cumulative effort).

3. For a Poisson pattern of density $\rho$, derive the mean nearest-neighbor distance $1/(2\sqrt\rho)$. What is the expected mean nearest-neighbor distance of trees at a density of 400 per hectare, and what would $R$ be if the trees were planted on a square grid?

   **Answer** $\mathbb{P}(r_{\min} > r) = \mathrm{e}^{-\rho\pi r^2}$, so $\mathbb{E}[r] = \int_0^\infty\mathrm{e}^{-\rho\pi r^2}\,\mathrm{d}r = \frac{1}{2}\sqrt{\pi/(\rho\pi)} = 1/(2\sqrt\rho)$, using $\int_0^\infty\mathrm{e}^{-ar^2}\,\mathrm{d}r = \frac{1}{2}\sqrt{\pi/a}$. With $\rho = 400\,\mathrm{ha^{-1}} = 0.04\,\mathrm{m^{-2}}$, $\mathbb{E}[r] = 1/(2 \times 0.2) = 2.5\,\mathrm{m}$. On a square grid with the same density the spacing is $1/\sqrt\rho = 5\,\mathrm{m}$, every tree's nearest neighbor is 5 m away, and $R = 2 \times 5 \times 0.2 = 2.0$ (below the hexagonal maximum 2.149).

4. Explain why the same population can appear clumped with large quadrats and random or even regular with small ones. How should the quadrat size be chosen in a study of the spatial pattern of a shrub?

   **Answer** Pattern is a property of a scale. If shrubs are clumped in patches of favorable soil about 20 m across but regularly spaced within patches because of competition for water, quadrats larger than the spacing but smaller than the patches mainly sample within patches and show regularity or randomness, quadrats comparable with patch size compare patches with gaps and show strong clumping, and very large quadrats average over many patches and approach randomness again. One should therefore not rely on one quadrat size: use a range of sizes (blocked-quadrat variance analysis, plotting variance against block size to find the scale of patches), or map the plants and use Ripley's $L$ function, which shows pattern as a function of distance; the choice should be guided by the biological question (the scale at which competition acts, the scale of soil heterogeneity).

5. (Open question) Design a monitoring program for the wintering crows on the Tsinghua campus that could tell whether the decline from 6067 to 3921 between 2023 and 2026 is real. What sources of error would you address?

   **Answer** Points to consider: standardize the date (several counts spread over midwinter each year rather than one count on varying dates), time (from a fixed time before sunset until dark), weather conditions, and the counting stations and routes, with the same observers trained in block counting; count all roost sites on and near campus simultaneously, because roosts shift between sites and some birds may have moved off campus; estimate observer error by having two observers count the same flocks or by counting photographs and videos of incoming flocks; replicate counts within a season to estimate within-season variance, so that a trend between years can be tested against it; record species composition, since several corvid species roost together; and relate any decline to possible causes (changes in winter food in the city, disturbance, trees removed at roosts, regional trends from other Beijing roosts and Christmas-count style surveys).
