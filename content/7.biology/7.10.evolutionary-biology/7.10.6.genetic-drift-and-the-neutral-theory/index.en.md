---
title: Genetic Drift and the Neutral Theory
description: "Random genetic drift as a source of evolution; the Wright–Fisher model as an absorbing Markov chain; the diffusion approximation, Kimura's fixation probability derived from the backward equation, mean times to fixation and loss, Wright's stationary distribution; variance and inbreeding effective sizes, the ratio Ne/N and changing population size; mutation–drift balance, estimating Ne from diversity and Lewontin's paradox; drift and selection: the Ne s criterion, the nearly neutral theory, the drift-barrier hypothesis, inbreeding load, crossing adaptive valleys and the shifting balance theory, clonal interference; the neutral theory of molecular evolution, the neutralist–selectionist debate, the overdispersed clock and the generation-time effect."
---

Evolution is to a large extent a random process. Which individuals survive an accident, which of two alleles a heterozygote passes to each child and how many children each parent has are matters of chance, and in a finite population chance alone changes allele frequencies from generation to generation. This **genetic drift** explains features of the living world that selection cannot: the loss of variation in small populations, the divergence of isolated populations at loci without any effect on fitness, the fixation of mildly deleterious mutations, and the steady accumulation of molecular differences between species that makes the **molecular clock** possible.

The basic facts are in [7.4.23](/7.4.23#sec-23.5): the **Wright–Fisher model** ([Definition 23.5.1](/7.4.23#def-23.5.1)), the properties of drift ([Theorem 23.5.1](/7.4.23#thm-23.5.1)), the **effective population size** and its formulas ([Definition 23.5.2](/7.4.23#def-23.5.2), [Formula 23.5.1](/7.4.23#fml-23.5.1)), **founder effects** and bottlenecks, Kimura's fixation probability ([Theorem 23.6.1](/7.4.23#thm-23.6.1)), the neutral substitution rate $k = \mu$ ([Theorem 23.7.1](/7.4.23#thm-23.7.1)) and neutral diversity $\theta = 4N_{\mathrm{e}}\mu$ ([Formula 23.7.1](/7.4.23#fml-23.7.1)). This chapter supplies the theory behind them, the diffusion approximation, and turns to the evolutionary questions: how strong drift is in real populations, when selection can overcome it, and how much of molecular evolution is neutral. The backward-in-time view of drift, the genealogy of a sample, is the subject of [7.10.7](/7.10.7); selection as it acts on new mutations is in [7.10.5](/7.10.5).

## 6.1. What Is Random Genetic Drift

In a pasture shared with cows, snails of the grove snail *Cepaea nemoralis* are crushed by hooves regardless of their shell color; on a given day in a given field some colors happen to be crushed more often. Mendelian segregation is a lottery even when everybody survives: a heterozygous parent of two children passes the same allele to both with probability $1/2$. Simulations of an idealized population, in which every individual has exactly the same chance of surviving and reproducing, show five features of drift ([7.4.23](/7.4.23#sec-23.5.1), figure):

1. it is unbiased: a frequency is as likely to go up as down, $\mathbb{E}[p_{t+1} \mid p_t] = p_t$;
2. it is stronger in smaller populations, with $\operatorname{Var}(p_{t+1} \mid p_t) = p_tq_t/2N$, by the law of large numbers for the binomial sampling of gametes;
3. it destroys variation within populations: every allele frequency eventually reaches 0 or 1;
4. it makes initially identical populations different, and the variance of frequencies among replicate populations grows;
5. it can fix an allele without any help from selection, with probability equal to its initial frequency.

The classical demonstration is Peter Buri's experiment with *Drosophila melanogaster* (1956). Replicate populations were founded with 16 heterozygotes for the eye-color alleles $bw$ and $bw^{75}$, which have no measurable effect on fitness in the laboratory, and each generation 8 males and 8 females were chosen at random to found the next. Within a few generations the frequencies were spread over the whole range; after 19 generations, in the series of 107 populations, $bw^{75}$ had been lost in 30 and fixed in 28. The populations as a whole showed a deficit of heterozygotes relative to Hardy–Weinberg proportions, the **Wahlund effect** produced by differences among populations ([7.4.22](/7.4.22#sec-22.4.4)), although each population was close to Hardy–Weinberg proportions internally. The variance among populations grew faster than predicted for $N = 16$; it fits an effective size of about $11.5$, because the flies' reproductive success varied more than in the ideal model.

Drift is visible in nature too. In College Station, Texas, 2218 garden snails *Cornu aspersum* sampled on two adjacent city blocks differed sharply in the frequency of an allele at the enzyme locus *GOT-1*; the street between the blocks blocks dispersal, and the difference almost certainly arose by drift. The northern elephant seal, reduced by hunting to fewer than 40 animals in the nineteenth century and now more than 100 000, has lost most of the genetic variation that museum specimens from before the crash still show. Two Chinese species went through still narrower bottlenecks. Père David's deer, or milu (*Elaphurus davidianus*), was already extinct in the wild when it became known to Western science in 1865, surviving only in the imperial hunting park south of Beijing; after that herd was lost around 1900, the species persisted only as the herd of about 18 animals gathered at Woburn Abbey in England, from which deer were returned to Beijing in 1985 and to Dafeng in Jiangsu in 1986. The crested ibis (*Nipponia nippon*), once widespread in East Asia, was reduced to 7 wild birds found in Yangxian, Shaanxi, in 1981. Both species now number in the thousands, and every living individual descends from these few founders; both have very low genetic diversity, which recovery in numbers cannot restore except by new mutation over many generations.

## 6.2. The Wright–Fisher Model as a Markov Chain

The Wright–Fisher model is a **Markov chain** ([3.5.9](/3.5.9)) on the number $i \in \{0, 1, \dots, 2N\}$ of copies of an allele, with transition probabilities

$$
P_{ij} = \binom{2N}{j}\Bigl(\frac{i}{2N}\Bigr)^j\Bigl(1 - \frac{i}{2N}\Bigr)^{2N - j}. \tag{6.1}
$$

The states $0$ and $2N$ are absorbing, and the distribution $\boldsymbol{\phi}_t$ of the state over replicate populations evolves as $\boldsymbol{\phi}_{t+1}^{\mathsf T} = \boldsymbol{\phi}_t^{\mathsf T}P$, the discrete-time analogue of a **master equation** ([7.6.32](/7.6.32#sec-32.2)). Two facts follow from linear algebra.

**Theorem 6.2.1 (Spectrum of the Wright–Fisher Chain)** The eigenvalues of $P$ are $\lambda_0 = \lambda_1 = 1$ and

$$
\lambda_k = \frac{(2N)!}{(2N - k)!\,(2N)^k} = \prod_{j = 0}^{k - 1}\Bigl(1 - \frac{j}{2N}\Bigr), \qquad k = 2, \dots, 2N. \tag{6.2}
$$

The two unit eigenvalues correspond to the absorbing states; the largest of the others, $\lambda_2 = 1 - 1/2N$, is the rate at which the probability of still being polymorphic, and the expected heterozygosity, decay in the long run.

**Proof** For any $k$, $\mathbb{E}[i_{t+1}(i_{t+1} - 1)\cdots(i_{t+1} - k + 1) \mid i_t]$ is the $k$-th factorial moment of $\mathrm{Bin}(2N, i_t/2N)$, which equals $\lambda_k\,(2N)^k(i_t/2N)^k = \lambda_ki_t^k$. Hence $P$ maps the space of polynomials in $i$ of degree at most $k$ into itself, with leading coefficient multiplied by $\lambda_k$; in the basis $1, i, i^2, \dots$ the matrix of $P$ acting on functions is triangular with diagonal entries $\lambda_0, \lambda_1, \dots, \lambda_{2N}$, which are therefore the eigenvalues. $\lambda_0 = \lambda_1 = 1$ ($i$ is a martingale), and $\lambda_2 = 1 - 1/2N$; for $k \ge 2$ the $\lambda_k$ decrease. $\square$

The same calculation with $k = 2$ gives the decay of heterozygosity in [Theorem 23.5.1](/7.4.23#thm-23.5.1) and the growth of the variance among replicate populations,

$$
\operatorname{Var}(p_t) = p_0q_0\Bigl[1 - \Bigl(1 - \frac{1}{2N}\Bigr)^t\Bigr], \tag{6.3}
$$

which approaches $p_0q_0$ as the populations are fixed for one allele or the other. This variance divided by $p_0q_0$ is the **fixation index** $F_{\mathrm{ST}}$ among replicate populations. For Buri's design, iterating the chain from $16$ copies of $32$ predicts that 25 of 107 populations would be absorbed by generation 19 for $N = 16$, and 43 for $N_{\mathrm{e}} = 11.5$; the observed 58 show that drift in the vials was stronger still in that series.

![The Wright–Fisher chain for Buri's design (Eq. (6.1), 2N = 32 gene copies, starting from 16 copies). A: the exact distribution of the number of copies over replicate populations after 1, 5, 10 and 19 generations, computed by matrix powers; the interior distribution spreads out, flattens and loses mass to the absorbing states 0 and 32 (bars at the ends, drawn as a fraction of populations). B: the variance of allele frequency among replicate populations, Eq. (6.3), for N = 16 and N = 11.5, and the fraction of populations absorbed (fixed or lost); after 19 generations about 23 % (N = 16) or 40 % (N = 11.5) are absorbed](./plots/wf-chain.py)

## 6.3. The Diffusion Approximation

### 6.3.1. Diffusion of Allele Frequencies

When $N$ is large, allele frequencies change by small amounts each generation, and the chain can be replaced by a continuous process, in the same way that a random walk with small steps becomes **Brownian motion** ([7.6.5](/7.6.5)).

**Definition 6.3.1 (Diffusion Approximation)** The **diffusion approximation** of a model of allele-frequency change describes the frequency $p$ as a continuous-time Markov process on $[0, 1]$ characterized by its infinitesimal mean and variance per generation,

$$
M(p) = \mathbb{E}[\Delta p \mid p], \qquad V(p) = \operatorname{Var}(\Delta p \mid p) = \frac{p(1 - p)}{2N_{\mathrm{e}}}, \tag{6.4}
$$

where $M(p)$ collects the deterministic forces (selection, mutation, migration) and $V(p)$ is the sampling variance of drift. The density $\phi(p, t)$ of the frequency over replicate populations then obeys the forward (Kolmogorov) equation, a Fokker–Planck equation,

$$
\frac{\partial\phi}{\partial t} = \frac12\frac{\partial^2}{\partial p^2}\bigl[V(p)\phi\bigr] - \frac{\partial}{\partial p}\bigl[M(p)\phi\bigr]. \tag{6.5}
$$

For genic selection with heterozygote advantage $s$ (fitnesses $1 : 1 + s : 1 + 2s$), $M(p) = sp(1 - p)$ by [Eq. (5.4)](/7.10.5#eq-5.4). The diffusion is accurate when $s$, $\mu$ and $1/N$ are small and their products with $N$ are of order one: the scaled parameters $N_{\mathrm{e}}s$ and $N_{\mathrm{e}}\mu$ then determine everything. This is the deeper reason why the relative strength of selection and drift is measured by $N_{\mathrm{e}}s$.

### 6.3.2. Fixation Probability

Questions about the eventual fate of an allele are answered by the backward equation, which follows the process from its starting point.

**Theorem 6.3.1 (Fixation Probability)** In the diffusion with mean $M$ and variance $V$, the probability $u(p)$ that an allele starting at frequency $p$ is eventually fixed solves

$$
\frac12V(p)u''(p) + M(p)u'(p) = 0, \qquad u(0) = 0, \quad u(1) = 1, \tag{6.6}
$$

so that

$$
u(p) = \frac{\int_0^pG(x)\,\mathrm{d}x}{\int_0^1G(x)\,\mathrm{d}x}, \qquad G(x) = \exp\Bigl(-\int_0^x\frac{2M(y)}{V(y)}\,\mathrm{d}y\Bigr). \tag{6.7}
$$

For genic selection, $2M/V = 4N_{\mathrm{e}}s$ and $u(p) = (1 - \mathrm{e}^{-4N_{\mathrm{e}}sp})/(1 - \mathrm{e}^{-4N_{\mathrm{e}}s})$, Kimura's formula ([Theorem 23.6.1](/7.4.23#thm-23.6.1)).

**Proof** Condition on the first generation: the allele is fixed from $p$ with the probability that it is fixed from wherever it is after one generation, so $u(p) = \mathbb{E}[u(p + \Delta p)]$. Expanding $u$ to second order and using $\mathbb{E}[\Delta p] = M$, $\mathbb{E}[(\Delta p)^2] \approx V$ (the square of the mean is of higher order), $0 = Mu' + \frac12Vu''$. This is a first-order linear equation for $u'$, with solution $u' = cG$; integrating and imposing the boundary conditions gives Eq. (6.7). For genic selection $G(x) = \mathrm{e}^{-4N_{\mathrm{e}}sx}$, whose integrals give Kimura's formula. $\square$

For a new mutation, $p = 1/(2N)$, and for $N_{\mathrm{e}}s \gg 1$, $u \approx 2sN_{\mathrm{e}}/N$, which is the establishment probability $2s/\sigma^2$ of [Theorem 5.3.1](/7.10.5#thm-5.3.1) with the variance of offspring number expressed through the effective size. Eq. (6.7) handles any form of selection. For underdominance with fitnesses $1 : 1 - s_{\mathrm{h}} : 1$, $M = s_{\mathrm{h}}p(1 - p)(2p - 1)$ and $G(x) = \exp[4N_{\mathrm{e}}s_{\mathrm{h}}x(1 - x)]$: the barrier at intermediate frequencies reduces the fixation probability of a new mutant roughly by a factor $\mathrm{e}^{-N_{\mathrm{e}}s_{\mathrm{h}}}$ (§6.5.4).

### 6.3.3. Times to Fixation and Loss

**Theorem 6.3.2 (Mean Absorption Times for a Neutral Allele)** For a neutral allele at initial frequency $p$, the mean time until it is fixed or lost, the mean time to fixation given that it is fixed, and the mean time to loss given that it is lost are, in generations,

$$
\bar t(p) = -4N_{\mathrm{e}}[p\ln p + q\ln q], \qquad \bar t_1(p) = -\frac{4N_{\mathrm{e}}q\ln q}{p}, \qquad \bar t_0(p) = -\frac{4N_{\mathrm{e}}p\ln p}{q}. \tag{6.8}
$$

For a new mutation ($p = 1/(2N)$), $\bar t_1 \approx 4N_{\mathrm{e}}$ and $\bar t_0 \approx 2(N_{\mathrm{e}}/N)\ln(2N)$.

**Proof** Conditioning on the first generation again, $\bar t(p) = 1 + \mathbb{E}[\bar t(p + \Delta p)]$, so $\frac12V\bar t'' = -1$ with $\bar t(0) = \bar t(1) = 0$ for $M = 0$. With $V = pq/(2N_{\mathrm{e}})$, $\bar t'' = -4N_{\mathrm{e}}/(pq) = -4N_{\mathrm{e}}(1/p + 1/q)$; integrating twice gives the first formula, as differentiation confirms. For the time to fixation, note that the allele is fixed from $p$ only if it is fixed from wherever it is after one generation, so $g(p) = u(p)\bar t_1(p)$ satisfies $g(p) = u(p) + \mathbb{E}[g(p + \Delta p)]$, that is $\frac12Vg'' = -u = -p$. Then $g'' = -4N_{\mathrm{e}}/q$, and $g = -4N_{\mathrm{e}}q\ln q$ satisfies it with $g(0) = g(1) = 0$; dividing by $u = p$ gives $\bar t_1$, and the time to loss follows by exchanging the alleles. As $p \to 0$, $-q\ln q/p \to 1$, so $\bar t_1 \to 4N_{\mathrm{e}}$; and $-p\ln p/q \approx p\ln(2N)$ gives $\bar t_0 \approx 4N_{\mathrm{e}}\ln(2N)/(2N)$. $\square$

The neutral mutations that will become substitutions take about $4N_{\mathrm{e}}$ generations to get there, $40\,000$ generations, roughly a million years, for $N_{\mathrm{e}} = 10^4$, while the great majority of new mutations disappear within a few generations. A beneficial mutation with $N_{\mathrm{e}}s \gg 1$ that is fixed takes about $(2/s)\ln(4N_{\mathrm{e}}s)$ generations, far less: the time scales of drift ($N_{\mathrm{e}}$) and selection ($1/s$) differ, which [7.10.8](/7.10.8#sec-8.3) uses to distinguish sweeps from drift.

### 6.3.4. Stationary Distributions

With mutation in both directions, $A \to a$ at rate $\mu$ and $a \to A$ at rate $\nu$, no allele is absorbed, and the forward equation (6.5) has a stationary solution.

**Formula 6.3.1 (Wright's Stationary Distribution)** With $M(p) = -\mu p + \nu q + sp q$ and $V = pq/(2N_{\mathrm{e}})$, the stationary density of the frequency of $A$ is

$$
\phi(p) \propto p^{4N_{\mathrm{e}}\nu - 1}(1 - p)^{4N_{\mathrm{e}}\mu - 1}\,\mathrm{e}^{4N_{\mathrm{e}}sp}. \tag{6.9}
$$

Without selection this is a $\mathrm{Beta}(4N_{\mathrm{e}}\nu, 4N_{\mathrm{e}}\mu)$ distribution: U-shaped when $4N_{\mathrm{e}}\mu, 4N_{\mathrm{e}}\nu < 1$ (most of the time the population is nearly fixed, drift dominating), flat at 1, and peaked at intermediate frequencies when mutation dominates.

**Proof** A stationary solution with zero probability flux satisfies $\frac12(V\phi)' = M\phi$, so $(V\phi)'/(V\phi) = 2M/V$ and $V\phi \propto \exp\int 2M/V$. Here $2M/V = 4N_{\mathrm{e}}[-\mu/q + \nu/p + s]$, whose integral is $4N_{\mathrm{e}}[\mu\ln q + \nu\ln p + sp]$; dividing by $V \propto pq$ gives Eq. (6.9). $\square$

The factor $\mathrm{e}^{4N_{\mathrm{e}}sp}$ is a Boltzmann factor: in the weak-mutation limit the population spends time in each state in proportion to its fitness raised to a power set by the population size, the statistical-mechanical analogy of [Theorem 41.3.1](/7.6.41#thm-41.3.1), with $N_{\mathrm{e}}$ playing the role of inverse temperature. Codon usage bias ([7.10.8](/7.10.8#sec-8.1)) is a direct application.

![The diffusion approximation (Theorems 6.3.1 and 6.3.2). A: fixation probability u(p) against the initial frequency for scaled selection 4N_e s = −4, 0, 2, 5 and 20 (Eq. (6.7)); dots: 4000 simulated Wright–Fisher populations of N = 50 per point. B: mean time until fixation or loss of a neutral allele, in units of N_e generations, against its initial frequency (Eq. (6.8), solid), and the mean time to fixation of the alleles that are fixed (dashed); dots: simulations with N = 50 (2000 populations per point)](./plots/diffusion.py)

![Wright's stationary distribution (Formula 6.3.1) for symmetric mutation, 4N_e μ = 4N_e ν = 0.2, 1 and 5 (curves), with the frequencies of a simulated Wright–Fisher population of N = 50 with mutation sampled every 10 generations over 200 000 generations (histograms). With weak mutation most of the time is spent near fixation (U shape); with strong mutation frequencies stay intermediate. The dashed curve adds selection, 4N_e s = 2, for 4N_e μ = 1](./plots/stationary.py)

## 6.4. How Strong Is Drift

### 6.4.1. Effective Population Sizes

The effective size of [Definition 23.5.2](/7.4.23#def-23.5.2) can be defined by different properties of the ideal population, and the definitions agree only when the population is constant in size and at equilibrium:

- the variance effective size $N_{\mathrm{e}}^{(V)}$ matches the sampling variance of allele frequencies, $\operatorname{Var}(\Delta p) = pq/(2N_{\mathrm{e}}^{(V)})$;
- the inbreeding effective size $N_{\mathrm{e}}^{(F)}$ matches the rate at which the probability of identity by descent rises, $\Delta F = (1 - F)/(2N_{\mathrm{e}}^{(F)})$;
- the coalescent effective size matches the rate at which two lineages coalesce backward in time, $1/(2N_{\mathrm{e}})$ ([7.10.7](/7.10.7#sec-7.2)).

The variance effective size depends on the number of offspring, the inbreeding effective size on the number of parents, so after a bottleneck followed by growth they differ. All three are lowered by unequal numbers of the sexes, by fluctuations in population size (the harmonic mean, dominated by the smallest generations) and by a variance of offspring number larger than Poisson ([Formula 23.5.1](/7.4.23#fml-23.5.1)). Elephant seals combine the last two: a few dominant males fight for harems and obtain most matings. Influenza viruses reach astronomical numbers during an epidemic but every outbreak starts from a few virions, and estimates of their effective size are a few hundred. Even the most numerous organism known, the marine bacterium *Pelagibacter ubique*, with perhaps $10^{28}$ cells, is finite and drifts.

Meta-analyses of populations of animals and plants put the ratio $N_{\mathrm{e}}/N$ typically around $0.1$, with a wide range. Species also differ in their history: the zebra finch *Taeniopygia guttata* in Australia has nucleotide diversity $\pi \approx 0.010$, while the population of the Lesser Sunda Islands, colonized from Australia about a million years ago, has $\pi \approx 0.002$; models of the variation suggest that the island population was founded by perhaps 9 birds, and that the present Australian effective size, about 7 million, grew from about 19 000 two million years ago.

### 6.4.2. Diversity and Effective Size

**Formula 6.4.1 (Mutation–Drift Equilibrium under Infinite Alleles)** If every mutation, at rate $\mu$ per gene per generation, creates a new allele, the probability $F$ that two gene copies are identical in state approaches the equilibrium

$$
F_{t+1} = \Bigl[\frac{1}{2N_{\mathrm{e}}} + \Bigl(1 - \frac{1}{2N_{\mathrm{e}}}\Bigr)F_t\Bigr](1 - \mu)^2, \qquad \hat F \approx \frac{1}{1 + 4N_{\mathrm{e}}\mu}, \qquad \hat H = \frac{\theta}{1 + \theta}. \tag{6.10}
$$

**Proof** Two copies drawn in generation $t + 1$ derive from the same parental copy with probability $1/(2N_{\mathrm{e}})$, and otherwise from two copies identical with probability $F_t$; they remain identical only if neither mutates. At equilibrium $\hat F[1 - (1 - 1/2N_{\mathrm{e}})(1 - 2\mu)] \approx (1 - 2\mu)/2N_{\mathrm{e}}$, so $\hat F(1/2N_{\mathrm{e}} + 2\mu) \approx 1/2N_{\mathrm{e}}$, to first order in $\mu$ and $1/N_{\mathrm{e}}$. $\square$

For DNA sequences, the per-site version is the **nucleotide diversity** $\pi \approx 4N_{\mathrm{e}}\mu$ ([Formula 23.7.1](/7.4.23#fml-23.7.1)), derived from the genealogy of two sequences in [7.10.7](/7.10.7#sec-7.3). It is the product of the mean coalescence time of two copies, $2N_{\mathrm{e}}$ generations, the mutation rate, and a factor 2 for the two lineages. Two consequences:

- diversity is highest where mutations are neutral: in noncoding DNA and at the third positions of codons, lower in exons; at the *Adh* gene of *D. melanogaster*, of 43 SNPs in 11 chromosomes, 17 were in exons and only 1 of these changed an amino acid;
- diversity measures the long-term effective size: with $\pi$ measured at neutral sites and $\mu$ from pedigrees or divergence, $N_{\mathrm{e}} = \pi/(4\mu)$. Humans give about $10^4$, much less than chimpanzees, *D. melanogaster* about $10^6$, *E. coli* far more; the nematode *Caenorhabditis remanei*, which outcrosses, has an effective size about 20 times that of the selfing *C. elegans*. Remarkably, the genome of one diploid individual suffices, because its two copies at each of millions of sites are many independent samples of the genealogy of two.

Chromosomes with different modes of inheritance confirm the logic. In a population with equal numbers of the sexes there are 3 X chromosomes and 1 Y for every 4 copies of an autosome, so X and Y diversities are predicted to be $3/4$ and $1/4$ of the autosomal value. In a survey of 1.4 million human SNPs, $\pi$ was $0.000765$ for autosomes, $0.000469$ for the X ($61\,\%$) and $0.000151$ for the nonrecombining Y ($20\,\%$), close to the prediction; differences in the variance of reproductive success between the sexes, the higher mutation rate in males and selection on the nonrecombining Y account for the rest.

**Definition 6.4.1 (Lewontin's Paradox)** *Lewontin's paradox* is the observation that genetic diversity varies among species over a far narrower range than their population sizes: census sizes span more than ten orders of magnitude, while neutral diversity in animals mostly lies between about $0.1\,\%$ and $10\,\%$.

Ants and vertebrates have heterozygosities of $0.2$–$1\,\%$, butterflies and bivalves $1$–$10\,\%$, and across animals diversity correlates with fecundity and propagule size more clearly than with abundance. Two explanations, not mutually exclusive, are recurrent bottlenecks, which keep the long-term harmonic-mean size low, and selection at linked sites (selective sweeps and **background selection**), which reduces diversity more strongly in large populations, where selection is more efficient ([7.10.8](/7.10.8#sec-8.3)). In a naive neutral model, two copies in a species with $N_{\mathrm{e}} = 10^9$ would have a common ancestor $2 \times 10^9$ generations ago, often older than the species or even the gene: drift alone cannot be extrapolated over such times.

## 6.5. Drift and Selection

### 6.5.1. The $N_{\mathrm{e}}s$ Criterion

Kimura's formula and the simulations of [7.4.23](/7.4.23#sec-23.6) give the rule of thumb: selection dominates when $|N_{\mathrm{e}}s| \gg 1$, drift when $|N_{\mathrm{e}}s| \ll 1$, and in between both matter. It is the ratio that matters, not the absolute strengths, so the same mutation can be effectively neutral in one species and strongly selected in another. In a species with $N_{\mathrm{e}} = 10^4$, mutations with $|s| < 10^{-5}$ behave as neutral; with $N_{\mathrm{e}} = 10^6$, as in *Drosophila*, selection can see effects a hundred times smaller. Species with very large effective sizes show correspondingly precise adaptation, for example a strong bias toward the codons that are translated most efficiently (**codon usage bias**, [7.10.8](/7.10.8#sec-8.1)).

### 6.5.2. The Nearly Neutral Theory

**Definition 6.5.1 (Nearly Neutral Theory)** The **nearly neutral theory** (Ohta 1973, extended in 1992) holds that a large fraction of new mutations at functional sites are **nearly neutral mutations**, with $|N_{\mathrm{e}}s|$ of order one, mostly slightly deleterious, so that their fate depends on both selection and drift and thus on the effective population size.

The substitution rate of mutations with a distribution of effects $f(s)$ is

$$
k = 2N\mu\int u(s)f(s)\,\mathrm{d}s, \tag{6.11}
$$

with $u(s)$ the fixation probability of a new mutation. For strictly neutral mutations $k = \mu$, independent of $N$; for slightly deleterious ones, $k$ decreases as $N_{\mathrm{e}}$ grows, because selection becomes able to see them. The theory makes testable predictions: small populations fix more slightly deleterious amino acid changes, so the ratio of nonsynonymous to synonymous divergence ($d_{\mathrm{N}}/d_{\mathrm{S}}$, [7.10.8](/7.10.8#sec-8.1)) is higher in lineages with small $N_{\mathrm{e}}$, and the fraction of amino acid substitutions that are adaptive is lower. Estimates agree: about half of the amino acid differences between closely related species of flies and bacteria, which have very large $N_{\mathrm{e}}$, appear to have been fixed by positive selection, but only about $15\,\%$ or less of those between humans and macaques. Drift has fixed many mutations with $s \approx -10^{-5}$ in human genomes.

**Definition 6.5.2 (Drift-Barrier Hypothesis)** The *drift-barrier hypothesis* (Lynch) holds that the precision of adaptation of traits whose improvement has small individual fitness benefits, such as the fidelity of DNA replication, is limited by drift: selection can improve such a trait only until the gain from a further step falls below about $1/N_{\mathrm{e}}$. It predicts that species with smaller $N_{\mathrm{e}}$ have higher mutation rates per site and less streamlined genomes.

Across bacteria, unicellular eukaryotes and multicellular organisms, the mutation rate per site per generation does decrease with effective size, as the hypothesis predicts; its implications for the expansion of genomes and gene structures in organisms with small populations are discussed in [7.10.18](/7.10.18), and those for the evolution of sex in [7.10.14](/7.10.14).

### 6.5.3. Inbreeding Load

**Definition 6.5.3 (Inbreeding Load)** In the sense used here, the **inbreeding load** is the reduction of mean fitness of a small population caused by the fixation, through drift, of deleterious alleles that selection would keep rare in a large population (also called drift load or fixation load). It differs from inbreeding depression, the lower fitness of offspring of related parents relative to offspring of unrelated parents within a population ([Definition 24.7.1](/7.4.24#def-24.7.1)); in conservation genetics the same term also denotes the number of lethal equivalents per gamete, the slope of the decline of log fitness with the inbreeding coefficient.

Fixed deleterious alleles cannot be purged by selection within the population, because there is no variation left at those loci; only immigration can restore them. An isolated population of the adder *Vipera berus* in Sweden, fewer than 40 snakes, was highly homozygous; litters were small and many offspring were deformed or stillborn. Twenty males from other populations were introduced in 1992 and removed in 1996; the recruitment of juveniles rose and the population rebounded, a "genetic rescue" by the reintroduction of alleles lost by drift. The same accumulation is a problem in zoo populations and a contributor to the extinction of small natural populations ([7.10.34](/7.10.34)).

### 6.5.4. Crossing Adaptive Valleys

Selection climbs the **adaptive landscape** ([Definition 5.7.1](/7.10.5#def-5.7.1)) and cannot cross valleys; drift can. An underdominant chromosomal rearrangement is selected against while rare, but in a small population drift can carry it past the unstable equilibrium, after which selection fixes it: a peak shift. By Eq. (6.7), the fixation probability of a single underdominant mutant relative to a neutral one falls roughly as $\mathrm{e}^{-N_{\mathrm{e}}s_{\mathrm{h}}}$ with the depth $s_{\mathrm{h}}$ of the heterozygote deficit: a reduction of heterozygote fitness of $1\,\%$ makes a peak shift virtually impossible unless $N_{\mathrm{e}}$ is in the tens or hundreds. Consistent with this, chromosomal rearrangements become fixed more often in weedy plants, which often self and pass through bottlenecks, than in long-lived plants.

**Definition 6.5.4 (Shifting Balance Theory)** The *shifting balance theory* (Wright 1931, 1932) proposes that adaptation in a species subdivided into many small, partly isolated demes proceeds in three phases: drift carries some demes across adaptive valleys (phase 1), selection takes them up to a higher peak (phase 2), and the superior demes export migrants and convert the rest of the species (phase 3, interdemic selection).

Each phase is possible, but their combination requires a delicate balance of deme size, migration and selection, and most population geneticists today doubt that it is a common mode of adaptation; valleys may also be bypassed in high-dimensional genotype spaces through ridges of nearly equal fitness, or crossed by double mutants in large populations.

### 6.5.5. Beneficial Mutations in Large Populations

Drift limits adaptation even in very large populations, because each new beneficial mutation must survive its first generations ([Theorem 5.3.1](/7.10.5#thm-5.3.1)); a mutation that arises rarely is usually lost. When beneficial mutations arise often, the limit is different: in asexual populations, mutations arising in different lineages compete and only one can be fixed, so most beneficial mutations are wasted (**clonal interference**, [§41.4.4](/7.6.41#sec-41.4.4) of 7.6.41), and the rate of adaptation grows only slowly with population size and mutation rate. In sexual populations recombination can bring such mutations together, but selection at linked sites still interferes, the **Hill–Robertson effect** of [7.10.14](/7.10.14).

![Drift and selection (Eq. (6.11), Theorem 6.3.1). A: substitution rate relative to the neutral rate for slightly deleterious mutations with an exponential distribution of effects of mean s̄ (2Nu averaged over the distribution), against the effective size N, for s̄ = 10⁻⁵, 10⁻⁴ and 10⁻³; the rate is near the neutral value while N s̄ ≪ 1 and falls as selection becomes able to see the mutations. B: fixation probability of a new underdominant mutation (fitnesses 1, 1 − s_h, 1) relative to a neutral one, from Eq. (6.7), against N s_h; the barrier makes fixation exponentially unlikely, so peak shifts by drift need small populations and shallow valleys](./plots/nearly-neutral.py)

## 6.6. The Neutral Theory of Molecular Evolution

### 6.6.1. Molecular Differences Between Species

The α-globin chains of shark, carp, dog and human differ at about $16\,\%$ of sites between dog and human, $48$–$49\,\%$ between carp and the mammals, and $53$–$59\,\%$ between shark and the others. The ranking follows phylogeny, not ecology: the carp's hemoglobin, although it extracts oxygen from water, is more similar to a human's than to a shark's. The number of differences grows with the time since the common ancestor, and across many genes the amounts of synonymous ($d_{\mathrm{S}}$), nonsynonymous ($d_{\mathrm{N}}$) and amino acid differences between humans and nine other vertebrates increase nearly linearly with fossil divergence times, the synonymous about five times faster than the nonsynonymous. Such regularities are the molecular clock ([Definition 23.7.1](/7.4.23#def-23.7.1)), and their explanation was Motoo Kimura's **neutral theory of molecular evolution** (1968; King and Jukes 1969).

The theory makes several claims (Kimura 1983):

- most mutations at functional sites are deleterious and are removed by **purifying selection**; most of the rest are neutral, and advantageous mutations are rare;
- the substitution rate equals the neutral mutation rate $\mu_{\mathrm{n}}$, the total mutation rate times the fraction of mutations that are neutral, so that two lineages separated for $t$ generations differ at $d = 2\mu_{\mathrm{n}}t$ sites ([Theorem 23.7.1](/7.4.23#thm-23.7.1));
- functionally more constrained molecules and sites evolve more slowly, because fewer of their mutations are neutral;
- polymorphism within species and divergence between species are two phases of the same process;
- morphological, physiological and behavioral evolution is driven largely by selection; the theory concerns the molecular level.

The third claim is overwhelmingly confirmed. Pseudogenes, which make no product, are among the fastest-evolving sequences of the genome, followed by intergenic regions and introns, with coding sequences slowest (human–chimpanzee comparisons); synonymous sites evolve faster than nonsynonymous ones; histone H4 differs at only two amino acids between plants and mammals, while fibrinopeptides, which are discarded after blood clotting, evolve about a thousand times faster. The opposite prediction of a purely selectionist view, that important molecules should evolve fastest because they have most to gain, fails.

### 6.6.2. The Neutralist–Selectionist Debate

Until the 1960s the classical view held that populations sit near an optimal wild type with little variation, and the balance view that variation is maintained by balancing selection ([7.10.5](/7.10.5#sec-5.5)). Gel electrophoresis of proteins (Harris 1966; Lewontin and Hubby 1966) then revealed that a quarter or more of enzyme loci in humans and *Drosophila* are polymorphic, too much, it seemed, to be maintained by balancing selection given its segregational load, while Haldane's cost of selection ([7.10.5](/7.10.5#sec-5.8)) seemed to forbid the rapid adaptive substitution implied by the protein clock. Kimura's answer was that most of both polymorphism and divergence is neutral.

**Example 6.6.1 (The Load of Many Overdominant Loci)** Suppose that a mammal is polymorphic at $n = 2000$ independently segregating loci, each maintained by heterozygote advantage with fitnesses $1 - s : 1 : 1 - s$ and $s = 0.01$, and that fitness is multiplicative across loci. At each locus the equilibrium frequency is $1/2$ and the segregational load is $s/2 = 0.005$ ([7.4.23](/7.4.23#ex-23.3.3)), so the mean fitness relative to an individual heterozygous at all loci is
$$
\bar w = (1 - s/2)^n = 0.995^{2000} \approx \mathrm{e}^{-10.0} \approx 4.4 \times 10^{-5}.
$$
To keep the population from shrinking, the average individual would have to produce about $1/\bar w \approx 22\,000$ offspring, of which all but about two die or fail to reproduce for genetic reasons. Calculations of this kind made it implausible that the polymorphism revealed by electrophoresis is maintained by overdominance, and favored neutrality. The argument depends on the multiplicative model: if selection acts by truncation on the number of homozygous loci, or is soft, so that only the excess of offspring over the carrying capacity is culled, the load is far smaller (Sved, Reed and Bodmer 1967; King 1967), and the load argument alone does not decide the debate. The selectionists replied that rates vary more than the theory allows.

Under the neutral theory, substitutions in a lineage form a **Poisson process**, so the number of substitutions in a fixed time has variance equal to its mean, an index of dispersion $R = 1$. Kimura himself found $R > 1$ for mammalian proteins; for β-globins of mammals the estimate is about $3.1$. The excess can be explained by episodes of adaptive evolution, as in lysozyme, which acquired a digestive function independently in ruminants and in leaf-eating colobine monkeys, with bursts of substitution and several identical amino acid replacements in the two groups ([7.10.8](/7.10.8#sec-8.1)), or by variation in the neutral mutation rate among lineages.

The molecular clock also ticks in generations, not years, if substitutions are neutral, so species with short generations should evolve faster per year. This generation-time effect is clear for synonymous sites and noncoding DNA (rodents evolve faster than primates) but weaker for amino acid replacements, a pattern that the nearly neutral theory explains: species with short generations usually have large populations, in which fewer slightly deleterious replacements are fixed, and the two effects partly cancel.

### 6.6.3. The Present View

Neither extreme has survived. Comparisons of polymorphism and divergence ([7.10.8](/7.10.8#sec-8.2)) show that positive selection drives a substantial fraction of amino acid substitutions in species with large populations; genome scans reveal sweeps; and selection on linked sites shapes diversity across whole genomes. Clocklike evolution itself does not prove neutrality: in experimental populations of *E. coli*, genetic changes accumulated at a nearly constant rate although they were shown to be driven by positive selection. At the same time, noncoding DNA free of constraint evolves at the mutation rate, much of the polymorphism in genomes is effectively neutral or slightly deleterious, and the neutral theory is the indispensable null hypothesis against which every test of selection is constructed ([7.10.8](/7.10.8)). The clock, calibrated and allowed to vary among lineages, is the basis of molecular dating ([7.10.24](/7.10.24)).

![Differences in the amino acid sequence of α-globin between four vertebrates (data from Futuyma & Kirkpatrick (2017), Fig. 7.17) against the age of their common ancestor (about 440 Mya for shark and bony vertebrates, 400 Mya for carp and tetrapods, 70 Mya for dog and human, as given there). Open dots: proportion of sites that differ; filled dots: Poisson-corrected distance −ln(1 − p), which allows for multiple substitutions at a site. The corrected distance grows roughly in proportion to time, the molecular clock; the uncorrected proportion saturates](./plots/hemoglobin.py)

## Summary

| Topic | Result |
|---|---|
| Wright–Fisher chain | binomial transitions (Eq. (6.1)), absorbing at 0 and $2N$; eigenvalues $\lambda_k = \prod_{j<k}(1 - j/2N)$, slowest decay $1 - 1/2N$ (Theorem 6.2.1); $\operatorname{Var}(p_t) = p_0q_0[1 - (1 - 1/2N)^t]$ (Eq. (6.3)) |
| diffusion | $M(p)$ and $V(p) = pq/2N_{\mathrm{e}}$, forward equation (6.5) (Definition 6.3.1); backward equation for fixation, $u = \int_0^pG/\int_0^1G$ (Theorem 6.3.1) |
| times | neutral: $\bar t = -4N_{\mathrm{e}}(p\ln p + q\ln q)$; new mutation fixed in $\approx 4N_{\mathrm{e}}$, lost in $\approx 2\ln(2N)$ generations (Theorem 6.3.2); beneficial: $\approx (2/s)\ln(4N_{\mathrm{e}}s)$ |
| stationary distribution | $\phi \propto p^{4N_{\mathrm{e}}\nu - 1}q^{4N_{\mathrm{e}}\mu - 1}\mathrm{e}^{4N_{\mathrm{e}}sp}$ (Formula 6.3.1) |
| effective size | variance, inbreeding and coalescent $N_{\mathrm{e}}$; $N_{\mathrm{e}}/N \sim 0.1$; harmonic mean, sex ratio, offspring variance |
| diversity | $\hat H = \theta/(1 + \theta)$ (Formula 6.4.1), $\pi \approx 4N_{\mathrm{e}}\mu$; X : autosomes $\approx 3/4$, Y $\approx 1/4$; Lewontin's paradox (Definition 6.4.1) |
| drift vs selection | $\lvert N_{\mathrm{e}}s\rvert \gg 1$ selection, $\ll 1$ drift; nearly neutral theory (Definition 6.5.1), $k = 2N\mu\int uf$ (Eq. (6.11)); drift barrier (Definition 6.5.2); inbreeding load (Definition 6.5.3); peak shifts $\propto \mathrm{e}^{-N_{\mathrm{e}}s_{\mathrm{h}}}$, shifting balance (Definition 6.5.4); clonal interference |
| neutral theory | $k = \mu_{\mathrm{n}}$, $d = 2\mu_{\mathrm{n}}t$; constraint slows evolution; overdispersed clock ($R \approx 3$ for globins); generation-time effect; the neutral model as null hypothesis |

## Questions

1. A neutral allele is at frequency $0.2$ in a population with $N_{\mathrm{e}} = 500$. What is the probability that it is eventually fixed, and how long does that take on average if it is?

   **Answer** The fixation probability is $0.2$ ([Theorem 23.5.1](/7.4.23#thm-23.5.1), or Eq. (6.7) with $G = 1$). By Eq. (6.8) the conditional time is $\bar t_1 = -4N_{\mathrm{e}}q\ln q/p = -2000 \cdot 0.8\ln 0.8/0.2 = 2000 \cdot 0.8 \cdot 0.2231/0.2 = 1785$ generations.

2. Derive Kimura's fixation probability for genic selection from the backward equation, and show that it reduces to $p$ when $s \to 0$.

   **Answer** With $M = spq$ and $V = pq/(2N_{\mathrm{e}})$, Eq. (6.6) reads $u'' + 4N_{\mathrm{e}}su' = 0$, so $u' = c\,\mathrm{e}^{-4N_{\mathrm{e}}sp}$ and $u(p) = (1 - \mathrm{e}^{-4N_{\mathrm{e}}sp})/(1 - \mathrm{e}^{-4N_{\mathrm{e}}s})$ after imposing $u(0) = 0$, $u(1) = 1$. As $s \to 0$, numerator and denominator are $4N_{\mathrm{e}}sp$ and $4N_{\mathrm{e}}s$ to first order, so $u \to p$.

3. A population of 1000 adults consists of 50 breeding males and 950 females, and every 10 generations it crashes to 20 individuals (sex ratio 1:1) for one generation. Estimate its effective size.

   **Answer** In normal generations $N_{\mathrm{e}} = 4 \cdot 50 \cdot 950/1000 = 190$; in the crash generation $N_{\mathrm{e}} = 20$. The harmonic mean over a cycle of 10 generations is $10/(9/190 + 1/20) = 10/(0.0474 + 0.05) = 103$. Both the skewed sex ratio and the crash reduce $N_{\mathrm{e}}$ an order of magnitude below the census size.

4. Why does the nearly neutral theory predict that $d_{\mathrm{N}}/d_{\mathrm{S}}$ is higher in species with small effective population size?

   **Answer** Synonymous mutations are close to neutral, so $d_{\mathrm{S}}$ is set by the mutation rate. Many nonsynonymous mutations are slightly deleterious; their fixation probability relative to neutral, $2Nu(s)$, is near 1 when $N_{\mathrm{e}}|s| \ll 1$ and falls steeply when $N_{\mathrm{e}}|s| \gg 1$ (Eq. (6.11)). In a small population more of them behave as neutral and are fixed, raising $d_{\mathrm{N}}$ relative to $d_{\mathrm{S}}$; in a large one purifying selection removes them.

5. Explain why the eigenvalue $1 - 1/2N$, and not the time to absorption, describes the decay of heterozygosity averaged over replicate populations.

   **Answer** The expected heterozygosity $\mathbb{E}[2p_tq_t]$ is a quadratic function of the state, and by the proof of Theorem 6.2.1 the expectation of a quadratic polynomial in $i$ is multiplied by $\lambda_2 = 1 - 1/2N$ each generation (the linear part is conserved). Absorption times vary among populations; the average heterozygosity combines populations still polymorphic with those already fixed (with heterozygosity 0), and its geometric decay is exact, $H_t = H_0(1 - 1/2N)^t$, from the first generation on.
