---
title: The Genetical Theory of Natural Selection
description: "Selection observed in real time; absolute and relative fitness, fitness components and mean fitness; the spread of beneficial mutations, the rate of adaptation and Haldane's sieve; the establishment probability 2s of a new mutation from a branching process; side effects of selection: pleiotropy, trade-offs, genetic hitchhiking and the footprint of a selective sweep, standing genetic variation; balancing selection: overdominance, negative frequency dependence, the Levene model of multiple-niche polymorphism and geometric-mean fitness in fluctuating environments; underdominance and positive frequency dependence; Fisher's fundamental theorem and Wright's adaptive landscape; mutation load, the load paradox and Haldane's cost of selection."
---

Natural selection is a simple idea, but its consequences depend on how fitness differences translate into changes of the gene pool, and that translation is the subject of this chapter. The title is that of R. A. Fisher's book of 1930, which, together with the work of J. B. S. Haldane and Sewall Wright, joined Mendelian inheritance to Darwin's theory and founded the **modern synthesis** ([7.10.1](/7.10.1)). The one-locus theory of selection is already in [7.4.23](/7.4.23#sec-23.3): the recursion for one generation of selection ([Theorem 23.3.1](/7.4.23#thm-23.3.1)), the changes of allele frequency for the main patterns of dominance ([Formula 23.3.1](/7.4.23#fml-23.3.1)), the time scale $1/s$ ([Formula 23.3.2](/7.4.23#fml-23.3.2)), heterozygote advantage ([Theorem 23.3.2](/7.4.23#thm-23.3.2)) and **mutation–selection balance** ([Theorem 23.4.1](/7.4.23#thm-23.4.1)). We build on them without repeating them.

The questions here are those of evolutionary biology rather than genetics. How fast can a population adapt, and what limits it? Why are most new beneficial mutations lost? What does selection at one locus do to its neighbors? Which forms of selection preserve variation, and which destroy it? Does selection make populations better adapted on average, and in what sense? How much does the steady rain of deleterious mutations cost? Selection on quantitative traits follows in [7.10.9](/7.10.9); the interaction of selection with random drift, treated here only for the fate of a new mutation, is the subject of [7.10.6](/7.10.6), and the traces that selection leaves in genome sequences are the subject of [7.10.8](/7.10.8).

## 5.1. Natural Selection Observed

### 5.1.1. Evolution in Real Time

The rise of the melanic form of the peppered moth in industrial England and its fall after clean-air legislation ([Example 23.3.4](/7.4.23#ex-23.3.4)) was the first case of evolution by **natural selection** documented as it happened, and Haldane's calculation of its selection coefficient showed that selection in nature can be much stronger than Darwin had imagined. Hundreds of cases are now known, and many are responses to environments changed by humans:

- populations of the German cockroach *Blattella germanica* exposed to poisoned glucose baits evolved, within a few years, an aversion to glucose: a single mutation makes the neurons that respond to bitter compounds also fire on glucose, so the insects avoid the bait;
- bacteria evolve resistance to antibiotics, insects to insecticides and weeds to herbicides, often within a few years of a new compound coming into use;
- artificial selection by breeders changes domesticated species quickly: broiler chicken strains whose selection was stopped in 1957, 1978 and 2005, raised side by side, weigh about $0.9$, $1.8$ and $4.2\,\mathrm{kg}$ at 56 days.

Experimental evolution makes the process repeatable. In Richard Lenski's long-term evolution experiment, twelve populations of *Escherichia coli* founded from one ancestor have been propagated in a glucose-limited medium since 1988; their fitness relative to the ancestor, measured in direct competition, has increased for tens of thousands of generations without reaching a plateau ([§41.4.4](/7.6.41#sec-41.4.4) of 7.6.41).

### 5.1.2. Selection and Inheritance

Selection and evolution are not the same thing. Evolution by selection requires two correlations: between a trait and the number of offspring an individual leaves (this is selection), and between the trait in parents and in their offspring (this is inheritance). If both hold, the mean of the trait among the offspring differs from its mean among the parents before selection; if the trait is not heritable, selection acts every generation but nothing changes across generations. For quantitative traits this logic is the **breeder's equation**, $R = h^2S$ ([Theorem 24.5.1](/7.4.24#thm-24.5.1)), to which [7.10.9](/7.10.9) returns; for alleles at a locus, inheritance is Mendelian and the recursions below are exact.

## 5.2. Fitness

**Definition 5.2.1 (Absolute Fitness and Fitness Components)** The **absolute fitness** $W$ of an individual is the number of zygotes it contributes to the next generation over its lifetime; the absolute fitness of a genotype, allele or phenotype is the mean absolute fitness of the individuals that carry it. The **fitness components** are the factors into which fitness decomposes along the life cycle: survival from zygote to adult (viability), mating success, fertilization success and fecundity. Often two components suffice,

$$
W = \mathbb{P}(\text{survival to maturity}) \times \mathbb{E}[\text{offspring} \mid \text{survival}]. \tag{5.1}
$$

The strength of selection is determined by proportional differences: an individual with two offspring is very successful if the others have one, and a failure if they have four. This is why the recursions use the **relative fitness** $w = W/W_{\mathrm{ref}}$ of [Definition 23.3.1](/7.4.23#def-23.3.1), the ratio to a reference genotype chosen for convenience, and why the **selection coefficient** is defined relative to that reference. A constant factor common to all genotypes cancels.

**Definition 5.2.2 (Mean Fitness)** The **mean fitness** of a population is the average fitness of its members. At one locus with genotype frequencies in Hardy–Weinberg proportions, $\bar w = p^2w_{11} + 2pqw_{12} + q^2w_{22}$; the marginal fitnesses of the two alleles are the mean fitnesses of the genotypes that carry them, weighted by the probability that an allele finds itself in each,

$$
w_1 = pw_{11} + qw_{12}, \qquad w_2 = pw_{12} + qw_{22}, \qquad \bar w = pw_1 + qw_2. \tag{5.2}
$$

With these, the recursion of [Theorem 23.3.1](/7.4.23#thm-23.3.1) takes the compact form

$$
\Delta p = \frac{p(w_1 - \bar w)}{\bar w} = \frac{pq\,(w_1 - w_2)}{\bar w}: \tag{5.3}
$$

an allele increases when its marginal fitness exceeds the mean. The difference $\alpha = w_1 - w_2$ is the average effect on fitness of substituting allele 1 for allele 2, the same quantity as the average effect of [Definition 24.3.2](/7.4.24#def-24.3.2) with fitness as the trait.

**Example 5.2.1** The genotypes $A_1A_1$, $A_1A_2$ and $A_2A_2$ survive from egg to adult with probabilities $0.90$, $0.85$ and $0.75$, and surviving females lay $50$, $55$ and $70$ eggs. By Eq. (5.1) the absolute fitnesses are $45$, $46.75$ and $52.5$, so with $A_1A_1$ as reference $w_{11} = 1$, $w_{12} = 1.039$, $w_{22} = 1.167$: the genotype with the poorest survival is the fittest, because fecundity outweighs it. At $p_2 = 0.5$ the mean fitness is $0.25 + 0.519 + 0.292 = 1.061$, and the frequency of $A_2$ after one generation is $(0.25 \cdot 1.167 + 0.25 \cdot 1.039)/1.061 = 0.520$.

In continuous time, with overlapping generations, the natural measure is the Malthusian fitness $m = \ln W$ per unit time, the exponential growth rate of a genotype; differences in $m$ play the role of selection coefficients, and the logistic equation of §5.3 is exact for them.

## 5.3. Positive Selection and the Rate of Adaptation

### 5.3.1. The Spread of a Beneficial Mutation

**Positive selection** spreads an allele that raises fitness. When a new allele $A_2$ increases fitness by a proportion $s$ for each copy, the relative fitnesses are $1 : 1 + s : 1 + 2s$ for $A_1A_1 : A_1A_2 : A_2A_2$. By Eq. (5.2), with $p$ the frequency of $A_2$, $\bar w = 1 + 2sp$ and $w_2 - w_1 = s$, so Eq. (5.3) gives

$$
\Delta p = \frac{sp(1 - p)}{1 + 2sp} \approx sp(1 - p), \qquad \frac{\mathrm{d}p}{\mathrm{d}t} = sp(1 - p). \tag{5.4}
$$

The rate of evolution is the product of the strength of selection $s$ and the genetic variation $p(1 - p)$: no selection, or no variation, means no evolution. The continuous version is the logistic equation ([2.4](/2.4)); its solution $\ln[p_t/(1 - p_t)] = \ln[p_0/(1 - p_0)] + st$ gives the time from $10\,\%$ to $90\,\%$ as $2\ln 9/s \approx 4.4/s$ generations, $88$ generations for $s = 0.05$ and $220$ for $s = 0.02$. An advantage of $1\,\%$, which no field study could measure, replaces an allele in a few hundred generations.

*Fixation*, the state in which an allele has reached frequency 1 and all others are lost, is the end of positive selection: positive selection consumes the variation it acts on. Dominance shapes the path ([Formula 23.3.1](/7.4.23#fml-23.3.1) and its figure): a favored dominant allele rises fast while rare, because heterozygotes enjoy the full benefit, and slowly when common, because the last copies of the recessive allele hide in heterozygotes; a favored recessive allele is almost invisible while rare.

### 5.3.2. Establishment of a New Mutation

A new mutation appears as a single copy, and its first few generations are a lottery. A heterozygous carrier with two offspring fails to transmit the mutation to either with probability $1/4$, however large its advantage. The deterministic recursion describes the mutation only once it is common enough for such accidents to average out.

**Theorem 5.3.1 (Establishment Probability)** Let each copy of a rare allele leave a random number $K$ of copies in the next generation, independently of the other copies, with mean $\mathbb{E}[K] = 1 + s$ ($s > 0$ small) and variance $\operatorname{Var}(K) = \sigma^2$. The probability that the allele is not lost, its probability of establishment, is

$$
\pi \approx \frac{2s}{\sigma^2}. \tag{5.5}
$$

For Poisson offspring numbers ($\sigma^2 = 1 + s$), the exact value solves $1 - \pi = \mathrm{e}^{-(1 + s)\pi}$, and $\pi \approx 2s$.

**Proof** While rare, the copies of the allele form a **branching process** (a Galton–Watson process). Let $f(x) = \mathbb{E}[x^K]$ be the **probability generating function** of $K$ ([Definition 11.1.1](/3.1.11#def-11.1.1)). The line descended from one copy dies out with probability $u$ if and only if each of its $K$ daughter lines dies out, so $u = \sum_k \mathbb{P}(K = k)u^k = f(u)$; when $\mathbb{E}[K] > 1$ the extinction probability is the root of this equation in $[0, 1)$. Put $u = 1 - \pi$ and expand $f$ about 1, using $f(1) = 1$, $f'(1) = \mathbb{E}[K] = 1 + s$ and $f''(1) = \mathbb{E}[K(K - 1)] = \sigma^2 + (1 + s)^2 - (1 + s)$:

$$
1 - \pi \approx 1 - (1 + s)\pi + \tfrac12\bigl[\sigma^2 + s(1 + s)\bigr]\pi^2 .
$$

Hence $s\pi \approx \frac12[\sigma^2 + s(1 + s)]\pi^2$, so $\pi \approx 2s/[\sigma^2 + s(1 + s)] \approx 2s/\sigma^2$ for small $s$. For the Poisson distribution, $f(x) = \mathrm{e}^{(1 + s)(x - 1)}$, which gives the exact equation. $\square$

In a diploid Wright–Fisher population, a new allele with heterozygote fitness $1 + s$ transmits a number of copies that is approximately Poisson with mean $1 + s$, so $\pi \approx 2s$: Haldane's result of 1927, which Kimura's diffusion formula ([Theorem 23.6.1](/7.4.23#thm-23.6.1)) reproduces for $N_{\mathrm{e}}s \gg 1$ and which [7.10.6](/7.10.6#sec-6.3) derives from the diffusion approximation. A larger variance of offspring number (a smaller $N_{\mathrm{e}}/N$) lowers it in proportion. A mutation that raises fitness by $1\,\%$, a large effect, is lost 98 times in 100. The fate is decided early: the probability that $n$ independent copies all die out is $(1 - \pi)^n \approx \mathrm{e}^{-2sn}$, negligible once $n$ is a few times $1/(2s)$. An established allele then follows the deterministic trajectory, but it reaches that stage faster than average, because the surviving lines are those that happened to multiply early.

![Establishment of a new beneficial mutation (Theorem 5.3.1). A: probability that a single new copy escapes loss, against its advantage s per copy: the exact branching-process value for Poisson offspring numbers (solid), Haldane's 2s (dashed), Kimura's diffusion formula for N = 500 (dotted), and the fraction of 20 000 simulated Wright–Fisher populations of N = 500 in which the mutation was fixed (dots, 95 % intervals). B: the number of copies of 60 new mutations with s = 0.05 in a population of N = 5000 (log scale); most are lost within a few generations (grey), and the few that pass about 1/(2s) = 10 copies (dashed) are effectively safe and grow roughly exponentially](./plots/establishment.py)

**Definition 5.3.1 (Fixation Probability)** The **fixation probability** of an allele is the probability that it eventually reaches frequency 1. For a new beneficial mutation in a large population it equals, to a good approximation, the establishment probability of Theorem 5.3.1.

The establishment probability also depends on dominance, because selection on a rare allele acts through heterozygotes: with fitnesses $1 : 1 + hs : 1 + s$, a new mutation is established with probability about $2hs$. Recessive beneficial mutations ($h$ near 0) are therefore almost always lost, and those that are fixed are biased toward dominance.

**Definition 5.3.2 (Haldane's Sieve)** **Haldane's sieve** is the bias, among adaptive substitutions that arise from new mutations, toward alleles that are dominant in their effect on fitness, because recessive beneficial mutations are invisible to selection while rare and are lost by drift.

The sieve is weaker when adaptation uses alleles already present at appreciable frequency (§5.4.2), because then homozygotes exist from the start.

### 5.3.3. The Rate of Adaptation

**Formula 5.3.1 (Rate of Adaptive Substitution)** If beneficial mutations with advantage $s$ arise at rate $\mu_{\mathrm{b}}$ per gene copy per generation in a diploid population of size $N$ (with $N_{\mathrm{e}} = N$), the expected number of new beneficial mutations per generation is $2N\mu_{\mathrm{b}}$, each is established with probability $2s$, and the rate of adaptive substitution is

$$
k_{\mathrm{a}} \approx 2N\mu_{\mathrm{b}} \cdot 2s = 4N\mu_{\mathrm{b}}s. \tag{5.6}
$$

Unlike the neutral rate $k = \mu$ ([Theorem 23.7.1](/7.4.23#thm-23.7.1)), the adaptive rate grows with population size, because a large population produces more mutations while drift loses the same fraction of them.

**Example 5.3.1** Let $\mu_{\mathrm{b}} = 10^{-8}$ and $s = 0.01$. In a population of $N = 10^4$, an established beneficial mutation appears on average once every $1/(4N\mu_{\mathrm{b}}s) = 250\,000$ generations: adaptation at this locus is limited by the supply of mutations. In a population of $N = 10^8$, one appears every 25 generations, much faster than the roughly $(2/s)\ln(4Ns) \approx 3000$ generations that a sweep takes; several beneficial mutations then compete, the regime of **clonal interference** in asexual populations ([§41.4.4](/7.6.41#sec-41.4.4) of 7.6.41), and the rate of adaptation is set by the time a sweep takes rather than by the mutation supply.

The waiting time for a new mutation can be avoided when the allele is already present. *Standing genetic variation* is the genetic variation present in a population before a change in the environment makes some of it beneficial; an allele at frequency $p_0$ is established almost surely if $2Np_0 \gg 1/(2s)$ copies are present. Adaptation from standing variation is faster than from new mutation, starts from alleles that have already passed the filter of purifying selection in the old environment, and is less affected by Haldane's sieve.

## 5.4. Side Effects of Selection

### 5.4.1. Pleiotropy and Trade-Offs

Selection on one trait changes others through **genetic correlation**, and one cause of genetic correlation is **pleiotropy**: alleles that make individuals taller also make their feet larger. Male mammals have nipples as a pleiotropic side effect of selection for lactation in females. When an allele raises one **fitness component** and lowers another, there is a **trade-off**, and selection favors the allele with the highest fitness overall. Light skin in human populations far from the equator is a selected trait: an allele of *SLC24A5* that changes an alanine to a threonine rose to high frequency in Europe, and different alleles at other loci lighten the skin of East Asians, plausibly because reduced pigmentation allows synthesis of vitamin D under weak ultraviolet light; the cost is a higher risk of skin cancer.

Trade-offs usually do not maintain polymorphism: one allele generally has the higher overall fitness and is fixed. An exception is the horn polymorphism of male Soay sheep on St Kilda, where about $13\,\%$ of males have vestigial horns. Homozygotes for the allele $Ho^P$ mostly have small horns, which lower their mating success but raise their survival; homozygotes for $Ho^+$ have large horns, mate more and survive less; heterozygotes have large horns, and their overall fitness is the highest, so the trade-off produces heterozygote advantage (§5.5.1).

### 5.4.2. Genetic Hitchhiking

**Definition 5.4.1 (Genetic Hitchhiking)** **Genetic hitchhiking** is the change in frequency of an allele caused by selection on an allele at another locus with which it is in linkage disequilibrium (LD).

**Formula 5.4.1 (Hitchhiking Change)** Let allele $A_2$ at locus $A$ have selective advantage $s_A$ per copy (haploid or genic selection), and let locus $B$ be neutral. With $D = P_{A_2B_2} - p_Ap_B$ the disequilibrium between $A_2$ and $B_2$ ([Definition 22.3.2](/7.4.22#def-22.3.2)),

$$
\Delta p_B = \frac{s_AD}{1 + s_Ap_A} \approx s_AD. \tag{5.7}
$$

**Proof** Haplotypes carrying $A_2$ have fitness $1 + s_A$, the others 1, so the mean fitness is $1 + s_Ap_A$. After selection the frequency of $B_2$ is $[(1 + s_A)P_{A_2B_2} + P_{A_1B_2}]/(1 + s_Ap_A) = (p_B + s_AP_{A_2B_2})/(1 + s_Ap_A)$. Subtracting $p_B = p_B(1 + s_Ap_A)/(1 + s_Ap_A)$ gives $s_A(P_{A_2B_2} - p_Ap_B)/(1 + s_Ap_A)$. $\square$

Formula 5.4.1 is the two-locus analogue of Eq. (5.4), with $D$ in place of the variance $p(1 - p)$. It needs disequilibrium, not physical linkage, but recombination destroys disequilibrium at rate $r$ per generation ([Theorem 22.3.1](/7.4.22#thm-22.3.1)), so lasting hitchhiking needs tight linkage. In an experiment with *Drosophila melanogaster*, a recessive lethal allele of *Glued* was placed in complete association with marker alleles at two linked enzyme loci; as the lethal declined, the markers declined with it, the more distant marker (*Est-6*, $8.6\,\%$ recombination with *Glued*) less than the closer one (*Pgm*, $3.5\,\%$). In bacteria, alleles that raise the mutation rate (mutators) can spread by hitchhiking with the beneficial mutations they produce.

A new beneficial mutation arises on one chromosome, in complete disequilibrium with every allele on it. As it sweeps to fixation it carries a stretch of that chromosome with it, and recombination has little time to break the association at nearby sites. The fixation of the mutation then removes variation in the surrounding region: this is a **selective sweep** ([7.8.13](/7.8.13#sec-13.6.2)), and its size is set by the ratio of recombination to selection.

**Formula 5.4.2 (Footprint of a Selective Sweep)** Let a new mutation with advantage $s$ per copy sweep from frequency $1/(2N)$ to fixation in a population of $2N$ gene copies, and let a neutral site be at recombination fraction $r \ll s$ from it. A neutral lineage sampled at the end of the sweep escapes from the selected background by recombination with probability about $1 - (2N)^{-r/s}$, and the heterozygosity at the neutral site just after the sweep, relative to before, is

$$
\frac{H_{\mathrm{after}}}{H_{\mathrm{before}}} \approx 1 - (2N)^{-2r/s}. \tag{5.8}
$$

**Proof** Trace a lineage backward through the sweep. While it sits on a chromosome carrying the beneficial allele (frequency $p$), it recombines onto a chromosome without it at rate $r(1 - p)$ per generation. With $\mathrm{d}p/\mathrm{d}t = sp(1 - p)$, the expected number of such events over the sweep is

$$
\int r(1 - p)\,\mathrm{d}t = \int_{1/2N}^{1} \frac{r(1 - p)}{sp(1 - p)}\,\mathrm{d}p = \frac{r}{s}\ln(2N),
$$

so the lineage stays in the selected background with probability $\mathrm{e}^{-(r/s)\ln 2N} = (2N)^{-r/s}$. Two lineages that both stay descend from the single chromosome on which the mutation arose, so they are identical at the neutral site; lineages that escape keep their old ancestry. Treating the two lineages as independent, the heterozygosity is reduced by the factor $1 - (2N)^{-2r/s}$. $\square$

The region of reduced diversity extends to $r \approx s/\ln(2N)$: for $s = 0.01$ and $2N = 2 \times 10^4$, heterozygosity is reduced by $86\,\%$ at $r = 10^{-3}$ and by $18\,\%$ at $r = 10^{-4}$, about 100 kb and 10 kb at a recombination rate of $10^{-8}$ per base pair. Strong selection makes wide sweeps. The domestication of maize from teosinte in Mesoamerica illustrates the pattern: selection for plants with a single stalk instead of a bushy form fixed a regulatory variant of the gene *tb1* (*teosinte branched1*), and diversity in maize is drastically reduced around it relative to teosinte; other evidence places the causal variant in a noncoding region about 60 kb upstream of the gene.

When selection acts on standing variation, the beneficial allele already sits on several haplotypes, having recombined onto different backgrounds while it was neutral or rare; at fixation only a short region around the selected site loses variation, a pattern that [7.10.8](/7.10.8#sec-8.3) calls a soft sweep. Comparing the width of the footprint with the strength of selection therefore tells whether adaptation used a new mutation or standing variation.

![Genetic hitchhiking (Formulas 5.4.1 and 5.4.2). A: a beneficial allele A₂ with s = 0.05 per copy (black) sweeps from frequency 0.001 on a chromosome that also carries the neutral allele B₂, absent elsewhere; B₂ rises with it, to fixation when the two loci are completely linked (r = 0, the curve hidden under that of A₂) and less as the recombination fraction r grows, because recombination moves B₂ onto chromosomes without A₂ (deterministic two-locus recursion for a haploid population). B: heterozygosity at a neutral site at distance x from the selected site just after a sweep, relative to before, from Eq. (5.8) with 2N = 2 × 10⁴ and r = 10⁻⁸ per bp per generation, for s = 0.001, 0.01 and 0.1; dots: 40 simulated sweeps with s = 0.05 in a forward Wright–Fisher population of 2N = 2000 haplotypes with recombination, relative to an unlinked site, close to the prediction for these values (dashed) and slightly below it, because sweeps that succeed start faster than the deterministic trajectory](./plots/hitchhiking.py)

## 5.5. Selection That Maintains Variation

Directional selection removes variation, and so does drift; the abundant variation of natural populations ([7.10.4](/7.10.4)) needs explanations. One is mutation (§5.8 and [7.10.6](/7.10.6)); the others are forms of **balancing selection**, which share one feature: an allele becomes relatively fitter as it becomes rarer.

### 5.5.1. Overdominance

**Heterozygote advantage** maintains a stable polymorphism at $\hat q = s_1/(s_1 + s_2)$ ([Theorem 23.3.2](/7.4.23#thm-23.3.2)), with sickle-cell hemoglobin in malarial regions as the classical case. Another comes from the threespine stickleback *Gasterosteus aculeatus*. Marine sticklebacks are covered with bony lateral plates, and freshwater populations derived from them repeatedly lose most plates through an allele of the gene *Eda*. In a lake in Alaska colonized by marine fish, the low-plated allele spread over about a decade with estimated fitnesses $1 : 0.98 : 0.12$ for low-plated homozygotes, heterozygotes and fully plated homozygotes, strong directional selection; in an experimental pond, by contrast, the estimated fitnesses $0.83 : 1 : 0.43$ were overdominant and the population settled at a stable polymorphism with the low allele at frequency $0.57/(0.17 + 0.57) = 0.77$. Fitnesses belong to an environment, not to an allele.

Heterozygote advantage is probably not the main cause of balanced polymorphism. Many organisms that are mostly haploid (many fungi) or mostly homozygous (selfing plants) are as variable as outcrossing diploids, although overdominance cannot act where heterozygotes are absent; and every overdominant locus imposes a segregational load (§5.8).

### 5.5.2. Negative Frequency-Dependent Selection

**Definition 5.5.1 (Negative and Positive Frequency Dependence)** Selection is frequency-dependent when the fitness of a genotype or phenotype depends on its frequency in the population. It is **negative frequency-dependent selection** when fitness decreases as the type becomes more common, so that rare types are favored, and **positive frequency-dependent selection** when fitness increases with frequency, so that the common type is favored.

In a haploid model with two types, Eq. (5.3) reads $\Delta p = pq[w_A(p) - w_a(p)]/\bar w$, and an interior equilibrium $\hat p$ is where the two fitnesses are equal. It is stable when the fitness difference decreases through it, $\frac{\mathrm{d}}{\mathrm{d}p}(w_A - w_a) < 0$ at $\hat p$, which is the case under negative frequency dependence. **Frequency-dependent selection** of this kind has diverse examples:

- the elder-flowered orchid *Dactylorhiza sambucina* has yellow and purple morphs in roughly equal numbers and offers no nectar; in experimental arrays of 50 plants with different morph ratios, bumblebees visited the rare color more often, so both male (pollen removal) and female (fruit set) success of a morph declined as it became more common, probably because the bees learn to avoid the unrewarding common color;
- at the self-incompatibility loci of plants, pollen carrying an allele present in the pistil cannot fertilize it, so a rare allele can fertilize almost every plant; the evening primrose *Oenothera organensis*, with fewer than 1000 plants in a few canyons of New Mexico, had 34 alleles in a sample of 135 plants;
- in Batesian mimicry, a palatable mimic loses protection as it becomes common relative to its distasteful model; females of the swallowtail *Papilio dardanus* mimic several model species with morphs controlled by a **supergene**;
- the fitness of a sex is frequency-dependent, which keeps the sex ratio near 1:1 ([7.10.13](/7.10.13));
- in a population of *Pseudomonas fluorescens* in an unshaken vial, a smooth type growing in the broth, a "wrinkly spreader" forming a mat at the surface and a "fuzzy spreader" each invade when rare, and the three coexist; the mechanism is the exploitation of different niches.

The last example shows the common thread: a rare type gains because the resource, mate or niche it uses is underexploited. Antagonistic coevolution with parasites, which adapt to the common host type, is another source of negative frequency dependence and is treated in [7.10.17](/7.10.17).

### 5.5.3. Multiple-Niche Polymorphism

When genotypes are adapted to different habitats within one population, each habitat can act as a refuge for one allele.

**Definition 5.5.2 (Multiple-Niche Polymorphism)** A **multiple-niche polymorphism** is a polymorphism maintained because different genotypes are favored in different niches of a population's habitat, with the contribution of each niche to the next generation fixed by its carrying capacity (soft selection). Its standard model is the Levene model (1953): after random dispersal of zygotes into the niches, selection acts within each niche, each niche $i$ contributes a fixed proportion $c_i$ of the adults, and the adults mate at random.

**Theorem 5.5.1 (Protected Polymorphism in the Levene Model)** In the haploid Levene model let allele $A$ have relative fitness $v_i$ in niche $i$ (with $a$ fitness 1). Then each allele increases when rare, so that a polymorphism is protected, if and only if

$$
\sum_i c_iv_i > 1 \quad\text{and}\quad \Bigl(\sum_i \frac{c_i}{v_i}\Bigr)^{-1} < 1, \tag{5.9}
$$

that is, the arithmetic mean of the fitness of $A$ over niches exceeds 1 and its harmonic mean is below 1.

**Proof** Within niche $i$ selection changes the frequency of $A$ to $p_i' = pv_i/(1 + (v_i - 1)p)$, and the pooled frequency is $p' = \sum_ic_ip_i'$. When $A$ is rare, $p_i' \approx pv_i$ and $p' \approx p\sum_ic_iv_i$, so $A$ increases if $\sum c_iv_i > 1$. When $a$ is rare, its frequency in niche $i$ becomes $q_i' \approx q/v_i$, so $a$ increases if $\sum c_i/v_i > 1$, which is the second condition. $\square$

Since the harmonic mean is never larger than the arithmetic mean, the window between the conditions exists only when fitnesses differ among niches, and it is narrow unless they differ a lot: with two equal niches and $v = (1.5, 0.6)$, the arithmetic mean is $1.05$ and the harmonic mean $0.86$, so the polymorphism is protected; with $v = (1.1, 0.85)$ it is not, because the arithmetic mean is below 1. Habitat choice, in which each genotype preferentially settles in the niche where it does well, widens the conditions greatly and allows polymorphism even with weak selection. Herbivorous insects with host races are candidates: the pea aphid *Acyrthosiphon pisum* has races adapted to different crop plants, with different alleles favored at several loci. Where the scale of environmental variation exceeds the dispersal distance, selection varies in space rather than among niches of one population and produces clines, such as that of an inversion of the malaria mosquito *Anopheles funestus* along a north–south transect in Cameroon; that case is the subject of [7.10.10](/7.10.10).

### 5.5.4. Selection Fluctuating in Time

Variation of selection in time maintains polymorphism much less easily than variation in space. In a haploid population, the odds $p/q$ are multiplied every generation by the ratio of the fitnesses of the two types, so after $t$ generations

$$
\frac{p_t}{q_t} = \frac{p_0}{q_0}\prod_{\tau = 1}^{t}\frac{w_A(\tau)}{w_a(\tau)}. \tag{5.10}
$$

The type with the larger geometric mean fitness wins, whatever the arithmetic means.

**Formula 5.5.1 (Geometric-Mean Fitness)** Under temporally fluctuating selection in a large population, the long-run fate of a type is determined by its geometric mean fitness $\bigl(\prod_{\tau}w(\tau)\bigr)^{1/t}$, equivalently by the time average of $\ln w$. In diploids, a polymorphism is protected if the heterozygote has a higher geometric mean fitness than both homozygotes, even if it is never the fittest genotype in any generation (Haldane and Jayakar 1963).

**Example 5.5.1** A species has two generations a year with identical survival and fecundities $50$, $55$, $70$ for $A_1A_1$, $A_1A_2$, $A_2A_2$ in spring and $70$, $65$, $55$ in autumn. The geometric means are $\sqrt{3500} = 59.2$, $\sqrt{3575} = 59.8$ and $\sqrt{3850} = 62.0$: $A_2A_2$ has the highest and $A_2$ is fixed, although it is the worst genotype every autumn. With fecundities $55$, $65$, $75$ in spring and $75$, $65$, $55$ in autumn, the geometric means are $64.2$, $65.0$ and $64.2$: the heterozygote, never the best, has the highest geometric mean, and both alleles are maintained.

Because the geometric mean penalizes variance (for small fluctuations it is about the arithmetic mean minus half the variance), traits that reduce the variance of fitness across years can be favored even at a cost to mean fitness, the principle of **bet hedging** taken up in [7.10.15](/7.10.15). Fluctuations that are fast relative to the response average out; slow ones let one allele drift toward fixation in each phase.

![Selection that maintains variation (Theorem 5.5.1, Formula 5.5.1). A: change in frequency per generation in haploid models of frequency-dependent selection, w_A − w_a = −0.2(p − 0.5) (negative, a stable equilibrium at 0.5, filled dot) and +0.2(p − 0.5) (positive, an unstable threshold, open dot); arrows give the direction of change. B: the Levene model with two equal niches: fitness of allele A in niche 1 and niche 2 (that of a is 1); in the shaded region the arithmetic mean exceeds 1 and the harmonic mean is below 1, so both alleles increase when rare; the dots mark v = (1.5, 0.6) and (0.6, 1.5), protected, and (1.1, 0.85), not protected. C: two generations a year with the fecundities of Example 5.5.1; with schedule 1 the allele A₂ is fixed, with schedule 2 the heterozygote has the highest geometric mean fitness and the frequency settles near 0.5 (shown once a year; within each year it oscillates)](./plots/balancing.py)

## 5.6. Selection That Favors the Common Type

**Underdominance**, the inferiority of heterozygotes, has an unstable interior equilibrium ([Theorem 23.3.2](/7.4.23#thm-23.3.2)): the allele that starts above the threshold is fixed, the other lost. Its outcome depends on history, and a new underdominant mutation, being rare and almost always in heterozygotes, is eliminated. Yet chromosomal rearrangements whose heterozygotes are semisterile have been fixed in many lineages. Sunflowers are an example: species of *Helianthus* differ by translocations and inversions, and hybrids heterozygous for these rearrangements have reduced fertility because the chromosomes pair poorly at meiosis. Such rearrangements can only be fixed by forces other than selection, by drift in small populations ([7.10.6](/7.10.6#sec-6.5.4)) or by **meiotic drive** ([7.10.16](/7.10.16)).

Positive frequency dependence has the same consequence. The butterfly *Heliconius erato* is distasteful to birds and has many geographic races with strikingly different color patterns; the co-occurring *H. melpomene* has parallel races that match them (Müllerian mimicry). Birds learn to avoid the locally common pattern, so a butterfly with the pattern of a neighboring race is attacked more. In a field experiment, butterflies with the local pattern survived more than twice as well as transplanted ones, corresponding to selection coefficients of about $0.17$ at each of the three major color-pattern loci. Within a race there is little variation in pattern: positive frequency dependence, like underdominance, removes variation and makes the outcome depend on the starting point.

## 5.7. The Evolution of Mean Fitness

### 5.7.1. Fisher's Fundamental Theorem

**Theorem 5.7.1 (Fundamental Theorem of Natural Selection)** At one locus with constant genotype fitnesses and random mating, the change in mean fitness in one generation is

$$
\Delta\bar w = \frac{V_A}{\bar w} + (w_{11} - 2w_{12} + w_{22})(\Delta p)^2, \qquad V_A = 2pq\alpha^2, \quad \alpha = w_1 - w_2, \tag{5.11}
$$

where $V_A$ is the additive genetic variance in fitness. For weak selection the second term, of third order in the selection coefficients, is negligible, and $\Delta\bar w \approx V_A/\bar w$; with fitness measured relative to the mean ($\bar w = 1$), the increase in mean fitness equals the additive genetic variance in fitness.

**Proof** By Eq. (5.3), $\Delta p = pq\alpha/\bar w$. Mean fitness $\bar w(p) = p^2w_{11} + 2pqw_{12} + q^2w_{22}$ is a quadratic polynomial in $p$ with $\mathrm{d}\bar w/\mathrm{d}p = 2[p(w_{11} - w_{12}) + q(w_{12} - w_{22})] = 2\alpha$ (by Eq. (5.2)) and $\mathrm{d}^2\bar w/\mathrm{d}p^2 = 2(w_{11} - 2w_{12} + w_{22})$. Taylor's formula is exact for a quadratic:

$$
\Delta\bar w = 2\alpha\,\Delta p + (w_{11} - 2w_{12} + w_{22})(\Delta p)^2 = \frac{2pq\alpha^2}{\bar w} + (w_{11} - 2w_{12} + w_{22})(\Delta p)^2 .
$$

The additive variance of fitness at one locus in Hardy–Weinberg proportions is $2pq\alpha^2$ ([Theorem 24.3.1](/7.4.24#thm-24.3.1), with fitness as the trait), which completes the proof. $\square$

**Example 5.7.1** With $w_{11} = 1$, $w_{12} = 1.05$, $w_{22} = 1.1$ and the frequency of $A_2$ equal to $0.5$, the average effect of $A_2$ is $\alpha = 1.075 - 1.025 = 0.05$, so $V_A = 2 \cdot 0.25 \cdot 0.0025 = 0.00125$ and $\bar w = 1.05$. The theorem predicts $\Delta\bar w = 0.00125/1.05 = 0.00119$. Directly, $\Delta p = 0.25 \cdot 0.05/1.05 = 0.0119$, and since $\bar w = 1 + 0.1p$ here, $\Delta\bar w = 0.00119$: for additive fitnesses the curvature term vanishes and the theorem is exact.

Because a variance is never negative, selection increases mean fitness, and does so fastest when the additive variance in fitness is largest. This explains the rhythm of a sweep: $\bar w$ hardly changes while the favored allele is rare, rises fastest near $p = 1/2$, and stops at fixation. At one locus with any number of alleles and constant fitnesses, mean fitness indeed never decreases under random mating (Kingman 1961). Fisher stated the theorem for the whole genome, and in that form it is a statement about the part of the change in mean fitness caused by natural selection: the "environment", including the genetic background and the other members of the population, deteriorates as the population evolves, so that the total change in $\bar w$ can be zero or negative even when selection constantly pushes it up. Estimates of the additive variance in relative fitness are often a few percent; mean fitness does not rise by a few percent per generation, because changing environments, new deleterious mutations and competition take back what selection gives.

The theorem fails as a statement about total mean fitness when fitnesses are frequency-dependent. A mutation that lets a shrub grow a trunk and shade its neighbors spreads, because carriers outcompete non-carriers; once most plants have trunks they shade one another, and with resources diverted from fruit, mean fecundity is lower than in the ancestral population. Bacteria that make bacteriocins, toxins that kill competitors, spread in the same way while the costs of toxin and immunity lower the growth of the whole population. Selection among individuals does not optimize the population (the levels of selection, [7.10.3](/7.10.3) and [7.10.16](/7.10.16)). With several loci, epistasis and recombination can also make mean fitness decrease, since recombination breaks up favorable combinations.

### 5.7.2. The Adaptive Landscape

**Definition 5.7.1 (Adaptive Landscape)** The **adaptive landscape** (Wright 1932) is the mean fitness of a population as a function of its allele frequencies, $\bar w(p_1, p_2, \dots)$. Under constant fitnesses and weak selection, selection moves the allele frequencies uphill on this surface, at one locus at the rate

$$
\Delta p = \frac{pq}{2}\,\frac{\mathrm{d}\ln\bar w}{\mathrm{d}p}, \tag{5.12}
$$

the form of [Eq. (23.5)](/7.4.23#eq-23.5) of 7.4.23.

The adaptive landscape must be distinguished from the **fitness landscape** of [Definition 41.4.1](/7.6.41#def-41.4.1), the fitness of individual genotypes over the space of sequences. A point of the adaptive landscape is a population, not a genotype, and its height is an average; Wright himself used both pictures, which has caused much confusion. On the adaptive landscape, directional selection is a slope rising to a peak at fixation, overdominance a peak at an interior frequency, and underdominance a valley between two peaks at the boundaries; with several loci and epistasis there can be several peaks separated by valleys. Selection alone cannot cross a valley, because it only climbs; whether drift can carry a population across, and Wright's theory that the alternation of drift and selection in subdivided populations explores the landscape, are the subject of [7.10.6](/7.10.6#sec-6.5.4).

![Wright's adaptive landscape (Definition 5.7.1). Top: genotype fitnesses for directional selection (1, 1.05, 1.1), overdominance (0.9, 1, 0.8) and underdominance (1.1, 1, 1.2) at a locus with alleles A₁ and A₂. Middle: the landscape, mean fitness against the frequency p of A₂, with arrows for the direction of change; filled dots are peaks (stable equilibria: fixation, the interior polymorphism at p = 1/3, and the two boundaries), the open dot the valley at p = 1/3 under underdominance. Bottom right: a two-locus landscape for haploids with epistasis (genotypes AB and ab fitter than Ab and aB), mean fitness under linkage equilibrium as contours over the two allele frequencies, with trajectories of Eq. (5.12) that climb to one of two peaks according to the starting point](./plots/landscape.py)

## 5.8. Deleterious Mutation and Genetic Load

### 5.8.1. Mutation Load

Most mutations with any effect on fitness are deleterious (the **distribution of fitness effects**, [7.10.4](/7.10.4)). **Purifying selection** removes them, mutation keeps introducing them, and the balance ([Theorem 23.4.1](/7.4.23#thm-23.4.1)) leaves each deleterious allele at a frequency of about $\mu/(hs)$ when it is partially expressed in heterozygotes. One consequence can be checked against medical data: for an autosomal dominant disorder with fitness $1 - s$ of affected individuals, the fraction of affected births caused by a new mutation equals $s$, because at equilibrium the alleles lost by selection, a fraction $s$ of those in affected individuals, are replaced by new mutations. Achondroplasia, with $s \approx 0.8$, is caused by a new mutation in about $80\,\%$ of cases; Huntington disease, whose effects come after reproduction, in about $1\,\%$.

**Definition 5.8.1 (Mutation Load)** The **mutation load** is the proportional reduction of the mean fitness of a population, relative to a population free of deleterious mutations, caused by recurrent deleterious mutation; it is the part of the genetic load ([Definition 23.4.1](/7.4.23#def-23.4.1)) due to mutation.

By the Haldane–Muller principle ([Theorem 23.4.2](/7.4.23#thm-23.4.2)) the load at a locus is about $2\mu$, independent of $s$: every deleterious mutation that enters the population must eventually be removed by a "genetic death", a failure to survive or reproduce, whether it is lethal and removed at once or mild and removed after many generations.

**Formula 5.8.1 (Genome-Wide Mutation Load)** If deleterious mutations at different loci act independently (multiplicatively) on fitness, and $U$ is the rate of new deleterious mutations per diploid genome per generation, the mean fitness relative to a mutation-free genome is $\prod_i(1 - 2\mu_i) \approx \mathrm{e}^{-U}$, and

$$
L = 1 - \mathrm{e}^{-U}. \tag{5.13}
$$

Estimates of $U$ for humans are about 2, which gives $L = 0.86$: the mean fitness of the population would be only $14\,\%$ of that of a mutation-free genotype, and each person would need to have about seven times the offspring required for replacement for the population to persist. This is the load paradox, and its resolutions are not fully settled:

- selection is often soft: when the number of survivors is set by resources, a genetic death is a lost place in competition, and the absolute productivity of the population is not reduced in proportion;
- if fitness declines faster than multiplicatively with the number of mutations (synergistic epistasis), or if selection acts like truncation, removing the individuals with the most mutations, each selective death removes several mutations at once, and the load for a given $U$ is much smaller;
- many mutations have small effects and are removed slowly, so their load is spread over long times, and sex and recombination change how efficiently they are removed ([7.10.14](/7.10.14)).

The paradox remains one of the arguments that most of the human genome is not under strong selective constraint (a large functional fraction would imply an implausibly large $U$), a theme of [7.10.8](/7.10.8#sec-8.6).

### 5.8.2. The Cost of Selection

Positive selection also has a cost. When the environment changes and a previously rare allele becomes favored, the population is less fit than it would be if it already carried the new optimum, and it pays the difference, summed over the generations of the substitution, in selective deaths. Haldane (1957) showed that with additive selection the total cost of replacing an allele that starts at frequency $p_0$ is about $2\ln(1/p_0)$ selective deaths per individual in the population, independent of the strength of selection: strong selection costs much per generation for a short time, weak selection little for a long time. For $p_0 = 10^{-4}$ this is about 18, and model variants give 10–40. Haldane concluded that a population could not carry more than about one substitution every few hundred generations, far fewer than the rate of amino acid substitution measured a decade later, and this "substitution load" was one of Kimura's motivations for the neutral theory ([7.10.6](/7.10.6#sec-6.6)).

The argument is less restrictive than it seemed. Comparisons of polymorphism and divergence suggest about 270 000 adaptive amino acid substitutions between *Drosophila simulans* and *D. yakuba* in about 6 million years of separate evolution, one in each lineage every few hundred generations at ten generations per year, which requires a load of only a few percent per generation ([7.10.8](/7.10.8#sec-8.2)). As for mutation load, truncation-like selection, in which the individuals carrying the most favorable combinations reproduce, fixes many favorable alleles with the same selective deaths, so the cost does not simply add over loci.

![Mean fitness under selection and mutation (Theorem 5.7.1, Formula 5.8.1). A: the increase of mean fitness per generation, Δw̄, during the spread of a favored allele, for additive fitnesses (1, 1.05, 1.1; line, from frequency 0.01) and for a recessive advantage (1, 1, 1.1; dashed, from 0.1), compared with the prediction V_A/w̄ of the fundamental theorem (dots); the curves coincide for additive fitness and differ only slightly for the recessive case, by the third-order term of Eq. (5.11). The increase is largest when the additive variance in fitness is largest. B: the genome-wide mutation load L = 1 − e^(−U) against the deleterious mutation rate U per diploid genome; the human estimate U ≈ 2 gives L ≈ 0.86, the load paradox](./plots/fundamental-theorem.py)

## Summary

| Topic | Result |
|---|---|
| fitness | absolute fitness = zygotes produced, product of fitness components (Eq. (5.1)); relative fitness and marginal fitnesses $w_1, w_2$, mean fitness $\bar w$ (Definition 5.2.2); $\Delta p = pq(w_1 - w_2)/\bar w$ (Eq. (5.3)) |
| spread of a beneficial allele | $1 : 1 + s : 1 + 2s$ gives $\Delta p \approx spq$, logistic, $10\,\% \to 90\,\%$ in $4.4/s$ generations (Eq. (5.4)) |
| establishment | branching process: $\pi \approx 2s/\sigma^2$, $\approx 2s$ for Poisson offspring (Theorem 5.3.1); $\approx 2hs$ with dominance, hence Haldane's sieve (Definition 5.3.2) |
| rate of adaptation | $k_{\mathrm{a}} \approx 4N\mu_{\mathrm{b}}s$, increasing with $N$ (Formula 5.3.1); mutation-limited in small, sweep-limited in large populations; standing variation avoids the wait |
| hitchhiking | $\Delta p_B \approx s_AD$ (Formula 5.4.1); sweep footprint $H_{\mathrm{after}}/H_{\mathrm{before}} \approx 1 - (2N)^{-2r/s}$, width $r \approx s/\ln 2N$ (Formula 5.4.2) |
| balancing selection | overdominance; negative frequency dependence (Definition 5.5.1); Levene model: AM $> 1 >$ HM of fitness across niches (Theorem 5.5.1); fluctuating selection: geometric mean decides (Formula 5.5.1) |
| favoring the common type | underdominance and positive frequency dependence: unstable thresholds, history-dependent outcome, variation removed |
| mean fitness | $\Delta\bar w \approx V_A/\bar w$ (Theorem 5.7.1); adaptive landscape $\bar w(p)$ and hill climbing (Definition 5.7.1), distinct from the genotype fitness landscape; frequency dependence can lower $\bar w$ |
| load | mutation load $\approx 2\mu$ per locus, $1 - \mathrm{e}^{-U}$ genome-wide (Formula 5.8.1), the load paradox; Haldane's cost of selection $\approx 2\ln(1/p_0)$ deaths per substitution |

The chapter's theme is that selection acts on variation, and that the variation available, at the locus and at linked loci, shapes what selection can do: rare alleles are exposed only through heterozygotes and are lost by chance, linked alleles ride along, and the same selective force can remove variation or preserve it depending on whether rarity is an advantage.

## Questions

1. Why is a new beneficial mutation with advantage $s = 0.05$ lost with probability about $0.9$ even in an infinitely large population, and why does this not slow adaptation much for mutations that recur often?

   **Answer** The loss happens while the mutation is present in a few copies, through the randomness of survival, reproduction and Mendelian segregation, which does not depend on population size: by Theorem 5.3.1 the establishment probability is about $2s = 0.1$. A mutation that arises $2N\mu$ times per generation is established on average after $1/(4N\mu s)$ generations, and in a large population this waiting time is short compared with the time of the sweep; chance loss matters most for mutations that arise rarely or only once.

2. Two equal niches give allele $A$ of a haploid fitnesses $v_1 = 1.2$ and $v_2 = 0.85$ relative to $a$. Is the polymorphism protected? What if $v_2 = 0.8$?

   **Answer** For $v = (1.2, 0.85)$: arithmetic mean $1.025 > 1$, harmonic mean $2/(1/1.2 + 1/0.85) = 2/(0.833 + 1.176) = 0.995 < 1$, so both alleles increase when rare and the polymorphism is protected (Theorem 5.5.1). For $v = (1.2, 0.8)$: arithmetic mean $1.0$, so $A$ does not increase when rare; the harmonic mean is $0.96$, so $a$ increases when rare and $A$ is eventually lost.

3. Explain why the fundamental theorem does not contradict the observation that the mean fitness of real populations does not increase steadily.

   **Answer** The theorem describes the change in mean fitness caused by selection on the existing additive variance, with the environment held fixed. In reality the environment, including other species, competitors of the same species and the genetic background, changes as the population evolves; new deleterious mutations arrive; and fitnesses are often frequency-dependent. The selective increase is offset by these changes, so total mean fitness can stay constant (population size is regulated) while selection keeps pushing it up.

4. A selective sweep with $s = 0.002$ and one with $s = 0.05$ occur in populations with $2N = 10^5$ and a recombination rate of $10^{-8}$ per base pair. Estimate the distance at which heterozygosity is reduced by half.

   **Answer** From Eq. (5.8), $(2N)^{-2r/s} = 1/2$ gives $r = s\ln 2/(2\ln 2N) = s \cdot 0.693/(2 \cdot 11.5) = 0.030s$. For $s = 0.002$, $r = 6.0 \times 10^{-5}$, about 6 kb; for $s = 0.05$, $r = 1.5 \times 10^{-3}$, about 150 kb. The width of the footprint is proportional to $s$, so strong sweeps are the easiest to detect.

5. In Example 5.5.1 (second schedule), why does the heterozygote's advantage in geometric mean fitness maintain both alleles although it is never the fittest genotype in any season?

   **Answer** Over a year the frequency is multiplied by the product of the seasonal fitness ratios. When an allele is rare it occurs almost only in heterozygotes, so its growth over a year depends on the ratio of the heterozygote's yearly product of fitnesses ($65 \cdot 65 = 4225$) to that of the common homozygote ($55 \cdot 75 = 4125$). Since $4225 > 4125$, each rare allele increases over a full year, whichever it is, and the polymorphism is protected; within the year the frequency oscillates as the homozygotes alternate in being favored.
