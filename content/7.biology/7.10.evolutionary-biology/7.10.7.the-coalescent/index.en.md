---
title: The Coalescent
description: "Gene genealogies traced backward in time; Kingman's coalescent derived from the Wright–Fisher model: pairwise coalescence, exponential waiting times at rate k(k − 1)/2, the time to the most recent common ancestor and total branch length, the Moran model and robustness; mutations on the genealogy: the infinite-sites and infinite-alleles models, θ = 4Neμ, pairwise differences, segregating sites and Watterson's estimator, the site frequency spectrum θ/i, likelihood and Bayesian estimation of θ; simulating the coalescent; changing population size, nonhomogeneous Poisson processes and skyline methods; the structured coalescent and FST from coalescence times; recombination and the ancestral recombination graph; selection and genealogies; a first look at the multispecies coalescent."
---

The theory of the previous chapters looks forward in time: given a population, how will its allele frequencies change? Data look backward. A sample of DNA sequences is the product of a history that we did not observe, and the natural model for it is the history of the sample itself: its genealogy, traced back until all lineages meet in a common ancestor. This change of perspective, made around 1980 by John Kingman, Richard Hudson and Fumio Tajima, is the coalescent. It ignores the rest of the population, which is irrelevant to the data, models the shape and branch lengths of the genealogy, and then places mutations on the branches; the probability of a sample under a population model follows, and with it estimation and testing.

The chapter derives the coalescent from the Wright–Fisher model of [7.10.6](/7.10.6#sec-6.2), uses it to derive the neutral diversity $\theta = 4N_{\mathrm{e}}\mu$ of [Formula 23.7.1](/7.4.23#fml-23.7.1), the estimators of $\theta$ and the site frequency spectrum, and extends it to changing population size, population structure and recombination. These results are the basis of the tests of selection in [7.10.8](/7.10.8), of molecular dating in [7.10.24](/7.10.24) and of the multispecies coalescent of gene trees within species trees in [7.10.25](/7.10.25). The **most recent common ancestor** of a set of gene copies is defined in [Definition 23.8.1](/7.4.23#def-23.8.1), and the human examples (mitochondrial and Y-chromosome ancestors, genealogical versus genetic ancestry) are in [7.4.23](/7.4.23#sec-23.8.1).

## 7.1. Gene Genealogies

**Definition 7.1.1 (Gene Genealogy)** The **gene genealogy** of a sample of gene copies at a nonrecombining locus is the tree of their lines of descent: following each copy backward in time from parent to parent, two lineages coalesce in the generation in which they derive from the same parental copy, and the genealogy ends at the most recent common ancestor of the sample. Its topology and the times between coalescences are random under any population model.

The figure shows a Wright–Fisher population of 10 gene copies over many generations. Each copy picks its parent at random from the previous generation. Looking forward, most copies leave no descendants after a few generations, by drift; looking backward from the last generation, the lineages of the present copies merge until a single ancestral copy remains. The genealogy of the present copies is a small part of the whole pedigree of gene copies, and only it matters for the data.

Three consequences of this picture recur throughout:

- every locus has a common ancestor in the past, but different loci have different genealogies and different ancestors: the ancestor of all human mitochondrial DNA was carried by a woman, that of all Y chromosomes by a man, and they did not live at the same time ([7.4.23](/7.4.23#sec-23.8.1));
- a common ancestor is not the only individual of its time; its contemporaries were ancestors at other loci or had no descendants;
- genealogies extend across species: the mitochondria of humans and chimpanzees trace back to a common ancestral mitochondrion perhaps 8 million years old, older than the split of the species, and all mitochondria of living eukaryotes to one of some 2 billion years ago.

![A Wright–Fisher genealogy. A: a population of 10 haploid gene copies (circles; two allele colors) followed for 16 generations, oldest at the top; each copy is linked to the parental copy it was drawn from. Dark lines are the lineages ancestral to the last generation, faint lines those that left no descendants; tracing backward, the ten present lineages coalesce one by one. B: the number of distinct ancestral lineages of the 10 present copies against the number of generations back, for this genealogy (steps) and its mean over 2000 simulated populations (dots) compared with the coalescent prediction (line): coalescence is fast while many lineages remain and slow for the last two](./plots/genealogy.py)

## 7.2. Kingman's Coalescent

### 7.2.1. Two Gene Copies

Take two copies from a Wright–Fisher population of $N$ diploids. The first picks a parent among the $2N$ copies of the previous generation, and the second picks the same parent with probability $1/(2N)$. Generations are independent, so the time $T_2$ back to their common ancestor is geometric,

$$
\mathbb{P}(T_2 > t) = \Bigl(1 - \frac{1}{2N}\Bigr)^t \approx \mathrm{e}^{-t/2N}, \qquad \mathbb{E}[T_2] = 2N. \tag{7.1}
$$

Measured in units of $2N$ generations, $T_2$ is an exponential variable with mean 1 and variance 1 (an **exponential distribution**, the continuous limit of the **geometric distribution**). The spread is large: the $95\,\%$ range of $T_2$ is from $0.05N$ to $7.4N$ generations. In any population that departs from the Wright–Fisher ideal (unequal sexes, varying size, variance of offspring number), the rate of pairwise coalescence defines an effective size, the coalescent effective size of [7.10.6](/7.10.6#sec-6.4): two copies coalesce at rate $1/(2N_{\mathrm{e}})$ per generation.

### 7.2.2. A Sample of $n$ Gene Copies

With $k$ lineages, the probability that no two of them pick the same parent in one generation is $\prod_{j=1}^{k-1}(1 - j/2N) \approx 1 - \binom{k}{2}/(2N)$, neglecting terms of order $1/N^2$ (two simultaneous coalescences, or three lineages merging at once). In units of $2N$ generations, coalescence therefore happens at rate $\binom{k}{2}$, and each of the $\binom{k}{2}$ pairs is equally likely to be the one that merges.

**Definition 7.2.1 (Kingman Coalescent)** The **coalescent** (Kingman's coalescent) for a sample of $n$ gene copies is the random genealogy generated backward in time as follows, with time in units of $2N_{\mathrm{e}}$ generations: when there are $k$ lineages, wait an exponential time $T_k$ with rate $\binom{k}{2} = k(k - 1)/2$, then merge a pair of lineages chosen uniformly at random; repeat until one lineage, the most recent common ancestor, is left. The waiting times $T_n, T_{n-1}, \dots, T_2$ are independent, and independent of the sequence of merged pairs.

The topology alone is a random "labelled history" in which every sequence of mergers is equally likely; there are $\prod_{k=2}^{n}\binom{k}{2} = n!(n - 1)!/2^{n-1}$ of them. The derivation needs only that $n \ll N$ and that the variance of offspring number is finite, which is why the coalescent describes many population models other than Wright–Fisher, with $N_{\mathrm{e}}$ absorbing the differences.

**Theorem 7.2.1 (Height and Length of the Coalescent Tree)** Let $T_{\mathrm{MRCA}} = \sum_{k=2}^nT_k$ be the *time to the most recent common ancestor* (TMRCA) of the sample and $L = \sum_{k=2}^nkT_k$ the total length of its branches, in units of $2N_{\mathrm{e}}$ generations. Then

$$
\mathbb{E}[T_{\mathrm{MRCA}}] = 2\Bigl(1 - \frac1n\Bigr), \qquad \operatorname{Var}(T_{\mathrm{MRCA}}) = 8\sum_{j=1}^{n-1}\frac{1}{j^2} - 4\Bigl(3 - \frac2n - \frac{1}{n^2}\Bigr), \tag{7.2}
$$

$$
\mathbb{E}[L] = 2\sum_{j=1}^{n-1}\frac1j, \qquad \operatorname{Var}(L) = 4\sum_{j=1}^{n-1}\frac{1}{j^2}. \tag{7.3}
$$

In generations, $\mathbb{E}[T_{\mathrm{MRCA}}] = 4N_{\mathrm{e}}(1 - 1/n)$.

**Proof** $T_k$ is exponential with rate $\binom{k}{2}$, so $\mathbb{E}[T_k] = 2/(k(k - 1)) = 2[1/(k - 1) - 1/k]$, and the sum telescopes to $2(1 - 1/n)$. The variance is $\sum_k 4/(k^2(k - 1)^2)$; squaring $1/(k(k - 1)) = 1/(k - 1) - 1/k$ gives $1/(k - 1)^2 - 2/(k(k - 1)) + 1/k^2$, and summing over $k = 2, \dots, n$ yields $2\sum_{j=1}^{n-1}j^{-2} - 1 + n^{-2} - 2(1 - 1/n)$, which times 4 is Eq. (7.2). For the length, $\mathbb{E}[kT_k] = 2/(k - 1)$ and $\operatorname{Var}(kT_k) = 4/(k - 1)^2$; independence gives Eq. (7.3). $\square$

The formulas have striking consequences. Even for a very large sample the expected height is only 2, twice the expected time for the last two lineages, $\mathbb{E}[T_2] = 1$: for half of its history a genealogy has just two lineages, and its depth is almost entirely the luck of when these two meet. The variance of the height tends to $8\pi^2/6 - 12 \approx 1.16$, nearly all of it from $T_2$. The total length grows only like $2\ln n$: adding sequences adds short twigs near the tips. The probability that the most recent common ancestor of a sample of $n$ is also that of the whole population is $(n - 1)/(n + 1)$, already $0.8$ for $n = 9$. For inference this means that more sequences from one locus add little information about the depth of history; more loci, with independent genealogies, add much more. For humans, with $N_{\mathrm{e}} \approx 10^4$ and 20-year generations, genealogies older than about $4.15 \times 2N_{\mathrm{e}}$ generations, $1.7$ million years, are rare at any locus, so neutral variation within our species says almost nothing about earlier times.

### 7.2.3. The Moran Model and Robustness

**Definition 7.2.2 (Moran Model)** The **Moran model** is a model of a haploid population of constant size $N$ with overlapping generations: at each step one individual, chosen at random, reproduces, and one, chosen at random among the others, dies and is replaced by the offspring; $N$ steps make one generation.

Two given lineages coalesce at a step if one of them is the newborn and the other its parent, which has probability $2/(N(N - 1))$, or about $2/N$ per generation: twice the rate in a haploid Wright–Fisher population of size $N$. The Moran model of size $N$ therefore has the coalescent of a Wright–Fisher population of $N/2$ haploid copies, because the variance of offspring number per generation is twice as large. In general, a population whose individuals have offspring numbers with variance $\sigma^2$ coalesces at a rate proportional to $\sigma^2$, so $N_{\mathrm{e}}$ is inversely proportional to $\sigma^2$, the same dependence as in [Formula 23.5.1](/7.4.23#fml-23.5.1). Kingman's coalescent fails only when single individuals can occasionally replace a large fraction of the population in one generation; this "sweepstakes" reproduction, proposed for some marine organisms with enormous fecundity and high larval mortality, produces genealogies with multiple simultaneous mergers.

![Kingman's coalescent (Definition 7.2.1, Theorem 7.2.1). A: three independent coalescent genealogies of n = 20 gene copies drawn on the same time scale (units of 2N_e generations); the trees differ greatly in depth, coalescence is rapid near the tips and the last two lineages take about half of the height. B: distribution of the time to the most recent common ancestor of n = 20 over 20 000 simulated genealogies (histogram) and of the time T₂ during which the last two lineages persist, with their expectations 2(1 − 1/n) = 1.9 and 1 (vertical lines); the dashed curve is the exponential density of T₂](./plots/kingman.py)

## 7.3. Mutations on the Genealogy

### 7.3.1. Mutation Models and $\theta$

Neutral mutations do not affect the genealogy, so they can be added afterwards: along each branch, mutations occur as a **Poisson process** with rate $\mu$ per generation, where $\mu$ is the mutation rate of the locus or of a site.

**Definition 7.3.1 (Infinite-Sites and Infinite-Alleles Models)** In the **infinite-sites model** every mutation occurs at a site that has not mutated before in the history of the sample, so each segregating site records exactly one mutation and sequences can be compared without correction for multiple hits. In the **infinite-alleles model** every mutation produces an allele not previously present, and only the identity or non-identity of alleles is observed.

The infinite-sites model is a good approximation for sequences within a species, where diversity per site is low; it fails for divergent sequences, which need the finite-site substitution models of [7.10.20](/7.10.20). The infinite-alleles model is natural for electrophoretic alleles and microsatellites with many states.

**Definition 7.3.2 (Population Mutation Rate)** The **population mutation rate** is $\theta = 4N_{\mathrm{e}}\mu$ for a diploid locus or site with mutation rate $\mu$ per generation (for haploid or uniparental loci, $2N_{\mathrm{e}}\mu$). In units of $2N_{\mathrm{e}}$ generations, mutations occur along each branch at rate $\theta/2$.

The single parameter $\theta$ combines the population size and the mutation rate, which the sample cannot separate: a large population with low mutation rate and a small one with high mutation rate give the same data. Estimates for humans are about $0.0006$ per site, two sequences differing about once every $1700$ base pairs.

### 7.3.2. Pairwise Differences and Segregating Sites

**Theorem 7.3.1 (Differences Between Two Sequences)** Under the infinite-sites model, the number $x$ of differences between two sequences at a locus with population mutation rate $\theta$ (for the locus) has the geometric distribution

$$
\mathbb{P}(x = j) = \frac{1}{1 + \theta}\Bigl(\frac{\theta}{1 + \theta}\Bigr)^j, \qquad \mathbb{E}[x] = \theta, \qquad \operatorname{Var}(x) = \theta + \theta^2. \tag{7.4}
$$

Under the infinite-alleles model, the probability that two copies carry different alleles is $H = \theta/(1 + \theta)$.

**Proof** Two lineages coalesce at rate 1, and mutations occur on the two lineages at total rate $2 \cdot \theta/2 = \theta$. Going back in time, the next event is a mutation with probability $\theta/(1 + \theta)$ and a coalescence with probability $1/(1 + \theta)$, independently of the past, because of the memorylessness of exponential waiting times. So the number of mutations before coalescence is geometric as stated, and two copies are different alleles under infinite alleles if at least one mutation precedes the coalescence, which has probability $\theta/(1 + \theta)$. $\square$

This is the genealogical derivation of [Formula 23.7.1](/7.4.23#fml-23.7.1) and of Formula 6.4.1 of [7.10.6](/7.10.6#sec-6.4): neutral diversity is the mean coalescence time of two copies, $2N_{\mathrm{e}}$ generations, times the mutation rate along two lineages. The variance $\theta + \theta^2$ exceeds the Poisson variance $\theta$, because the coalescence time itself varies.

For $n$ sequences, the number of segregating (polymorphic) sites $S$ counts the mutations on the whole tree, and given the total length $L$ it is Poisson with mean $L\theta/2$.

**Theorem 7.3.2 (Segregating Sites)** For a sample of $n$ sequences under the infinite-sites model,

$$
\mathbb{E}[S] = \theta a_n, \qquad \operatorname{Var}(S) = \theta a_n + \theta^2b_n, \qquad a_n = \sum_{i=1}^{n-1}\frac1i, \quad b_n = \sum_{i=1}^{n-1}\frac{1}{i^2}. \tag{7.5}
$$

**Proof** By Theorem 7.2.1, $\mathbb{E}[S] = \mathbb{E}[L]\theta/2 = \theta a_n$. By the law of total variance, $\operatorname{Var}(S) = \mathbb{E}[L\theta/2] + \operatorname{Var}(L\theta/2) = \theta a_n + (\theta^2/4) \cdot 4b_n$. $\square$

**Definition 7.3.3 (Watterson Estimator)** The **Watterson estimator** of $\theta$ is $\hat\theta_W = S/a_n$; Tajima's estimator is the mean number of pairwise differences, $\hat\theta_\pi = \binom{n}{2}^{-1}\sum_{i<j}x_{ij}$. Both are unbiased for $\theta$ under the standard neutral model, and are often reported per site after division by the number of sites.

**Example 7.3.1** Ten sequences of 1000 bp have $S = 20$ segregating sites. With $a_{10} = 2.829$, $\hat\theta_W = 7.07$ per locus, or $0.0071$ per site. Its standard deviation, from Eq. (7.5) with $b_{10} = 1.540$, is $\sqrt{7.07 \cdot 2.829 + 7.07^2 \cdot 1.540}/2.829 = 3.5$: a coefficient of variation of about $50\,\%$, which more sequences of the same locus would reduce only slowly.

The variance of $\hat\theta_W$ falls only like $1/\ln n$ as the sample grows, and that of $\hat\theta_\pi$,

$$
\operatorname{Var}(\hat\theta_\pi) = \frac{n + 1}{3(n - 1)}\theta + \frac{2(n^2 + n + 3)}{9n(n - 1)}\theta^2, \tag{7.6}
$$

does not tend to zero at all (Tajima 1983): all sequences share one genealogy, and its randomness cannot be averaged out within a locus. Precision comes from many unlinked loci.

### 7.3.3. The Site Frequency Spectrum

With an outgroup to identify the ancestral state, each segregating site has a derived allele carried by $i$ of the $n$ sequences, $1 \le i \le n - 1$.

**Definition 7.3.4 (Site Frequency Spectrum)** The (unfolded) **site frequency spectrum** of a sample of $n$ sequences is the vector $(\xi_1, \dots, \xi_{n-1})$, where $\xi_i$ is the number of segregating sites at which the derived allele is present in exactly $i$ sequences. Without an outgroup only the folded spectrum $\eta_i = \xi_i + \xi_{n-i}$ ($i \le n/2$, counted once when $i = n/2$) is observed.

**Theorem 7.3.3 (Neutral Site Frequency Spectrum)** Under the standard neutral coalescent with the infinite-sites model,

$$
\mathbb{E}[\xi_i] = \frac{\theta}{i}, \qquad i = 1, \dots, n - 1. \tag{7.7}
$$

**Proof** A mutation on a branch subtending $i$ of the $n$ tips produces a derived allele of frequency $i$, so $\mathbb{E}[\xi_i] = (\theta/2)\mathbb{E}[L_i]$, where $L_i$ is the total length of branches subtending exactly $i$ tips. During the epoch with $k$ lineages, which has expected length $2/(k(k - 1))$, each of the $k$ lineages subtends $i$ tips with probability $\binom{n-i-1}{k-2}/\binom{n-1}{k-1}$, because under the coalescent the partition of the $n$ tips among $k$ ancestors is uniform over compositions (a Pólya urn property). Hence

$$
\mathbb{E}[L_i] = \sum_{k=2}^{n-i+1}k\cdot\frac{2}{k(k - 1)}\cdot\frac{\binom{n-i-1}{k-2}}{\binom{n-1}{k-1}} = \frac2i,
$$

the last equality being a binomial identity (Fu 1995) that Question 3 asks to check for small $n$. $\square$

The spectrum is L-shaped: singletons are the most common class, and the expected numbers fall as $1/i$. Summing Eq. (7.7) gives $\mathbb{E}[S] = \theta a_n$ again. Every summary statistic of polymorphism is a weighted sum of the spectrum: $\hat\theta_W$ weights all classes equally, $\hat\theta_\pi = \sum_i i(n - i)\xi_i/\binom{n}{2}$ weights intermediate frequencies most, and the estimator $\hat\theta_H = \sum_i i^2\xi_i/\binom{n}{2}$ of Fay and Wu weights high-frequency derived alleles; all have expectation $\theta$ under neutrality, and their differences are the neutrality tests of [7.10.8](/7.10.8#sec-8.2). Under the infinite-alleles model the analogous result is the Ewens sampling formula: the expected number of distinct alleles in a sample of $n$ is $\sum_{i=0}^{n-1}\theta/(\theta + i)$, and given that number, the distribution of the allele counts does not depend on $\theta$, which allows a test of neutrality without knowing $\theta$.

### 7.3.4. Estimating $\theta$ by Likelihood

The simple estimators use summaries; likelihood uses the whole data. For $L$ unlinked loci with only two sequences each, with $x_i$ differences among $l_i$ sites, Theorem 7.3.1 gives the log likelihood under the infinite-sites model

$$
\ell(\theta) = \sum_{i=1}^{L}\Bigl[x_i\ln\frac{l_i\theta}{1 + l_i\theta} - \ln(1 + l_i\theta)\Bigr], \tag{7.8}
$$

with $\theta$ per site, maximized numerically (**maximum likelihood estimation**). With many sequences per locus, the likelihood is an average over all genealogies $G$ and branch lengths $\boldsymbol{t}$,

$$
f(X \mid \theta) = \sum_G\int f(G, \boldsymbol{t} \mid \theta)\,f(X \mid G, \boldsymbol{t})\,\mathrm{d}\boldsymbol{t}, \tag{7.9}
$$

where $f(G, \boldsymbol{t} \mid \theta)$ is the coalescent density (a product of exponential densities, by Definition 7.2.1) and $f(X \mid G, \boldsymbol{t})$ is the phylogenetic likelihood of the alignment on the genealogy, computed by **Felsenstein's pruning algorithm** ([Algorithm 6.5.1](/7.8.6#alg-6.5.1)) under a finite-site substitution model. The sum over genealogies is far too large to enumerate, but **Markov chain Monte Carlo** ([3.5.9](/3.5.9)) can sample genealogies and $\theta$ jointly from their **posterior distribution**: proposals change node ages, rearrange the genealogy (for example by subtree pruning and regrafting) and change $\theta$. Such genealogy-based estimates can be much more efficient than $\hat\theta_W$ and $\hat\theta_\pi$, because they use the information in the shape of the tree.

**Example 7.3.2** For three noncoding human loci of 6.6–10 kb with 54–63 sequences each, sampled from African and non-African populations, a Bayesian analysis under the JC69 model with a gamma prior of mean $0.001$ gave a posterior mean of $\theta = 0.00053$ per site, with $95\,\%$ credibility interval $(0.00037, 0.00072)$ (Rannala and Yang 2003). With a mutation rate of $10^{-9}$ per site per year and 20-year generations, this corresponds to $N_{\mathrm{e}} \approx 0.00053/(4 \cdot 20 \cdot 10^{-9}) \approx 6600$, with interval $4600$–$9000$; the posterior mean times to the most recent common ancestor of the three loci were about $0.36$, $0.69$ and $0.49$ million years.

![The site frequency spectrum and estimators of θ (Theorems 7.3.2 and 7.3.3). A: mean unfolded site frequency spectrum of 2000 simulated samples of n = 20 sequences with θ = 10 per locus (bars) and the neutral expectation θ/i (dots and line). B: sampling distributions of Watterson's estimator θ_W = S/a_n and of Tajima's θ_π over the same simulations; both are centered on θ = 10 (vertical line) but are broad, and θ_π is broader, as Eq. (7.6) predicts](./plots/sfs.py)

## 7.4. Simulating the Coalescent

Simulating a sample forward in time requires following the whole population, $N = 10^4$ to $10^8$ individuals over many generations, to obtain a sample of 2 to 30. The coalescent simulates only the sample.

**Algorithm 7.4.1 (Coalescent Simulation of a Neutral Sample)** To simulate $n$ sequences of $l$ sites with population mutation rate $\theta$ per site:

1. set $k = n$ and let the lineages be the $n$ tips; while $k > 1$, draw a waiting time from the exponential distribution with rate $k(k - 1)/2$, advance the time, join two lineages chosen at random into a new node at that time, and set $k \leftarrow k - 1$;
2. generate a random sequence at the root and evolve it down the branches: a branch of length $T$ (in units of $2N_{\mathrm{e}}$ generations) carries on average $T\theta/2$ substitutions per site, under any substitution model ([7.10.20](/7.10.20));
3. under the infinite-sites model, step 2 reduces to placing a Poisson number of mutations with mean $T\theta l/2$ on each branch, each at a new site.

An alternative merges the two steps: with $k$ lineages, coalescence and mutation are competing Poisson processes with rates $k(k - 1)/2$ and $kl\theta/2$, the next event being a coalescence with probability $(k - 1)/(k - 1 + l\theta)$; this works only when all mutations have the same rate. Programs such as ms, which implement these algorithms with extensions for population size changes, structure and recombination, made coalescent simulation the standard way to obtain null distributions of test statistics.

## 7.5. Changing Population Size

### 7.5.1. Time-Varying Coalescence Rates

If the population size $N(t)$ at time $t$ in the past varies, lineages coalesce faster when the population is small: with $k$ lineages the rate per generation is $\binom{k}{2}/(2N(t))$. The coalescent is then a nonhomogeneous Poisson process, and the probability density of the coalescence times $t_n < t_{n-1} < \dots < t_2$ (time measured backward from the present, $t_{n+1} = 0$) and the genealogy is

$$
f(G, t_n, \dots, t_2) = \prod_{k=2}^{n}\frac{1}{2N(t_k)}\exp\Bigl(-\binom{k}{2}\int_{t_{k+1}}^{t_k}\frac{\mathrm{d}s}{2N(s)}\Bigr), \tag{7.10}
$$

the product of the rates of the events that happened and the probabilities that no event happened in between. A simple trick simulates it: draw the waiting times of the standard coalescent and transform the time axis so that each unit of the new axis corresponds to $2N(t)$ generations.

Population history shapes genealogies:

- in a population that has grown exponentially, $N(t) = N_0\mathrm{e}^{-rt}$ backward in time, coalescences are pushed back toward the time when the population was small, and the genealogy becomes star-like: long terminal branches, many singletons, an excess of rare variants;
- a bottleneck causes a burst of coalescence while the population is small: lineages that survive it are compressed into a few, and the genealogy has a star-shaped part at the time of the bottleneck;
- a population that has recently declined has relatively few recent coalescences and long internal branches, an excess of intermediate-frequency variants.

Genealogies of HIV sequences illustrate the contrast: sequences of the *gag* gene sampled from 200 infected individuals in northern Britain in 1993 have the star-like shape of an epidemic in exponential growth, while *env* sequences sampled from one patient over seven years have a genealogy typical of a population of roughly constant size.

### 7.5.2. Inferring Population History

Eq. (7.10) turns sequence data into information about $N(t)$. Parametric models, such as exponential growth with $\theta(t) = \theta_0\mathrm{e}^{-rt}$, are analyzed by likelihood or Bayesian MCMC as in §7.3.4. Nonparametric models avoid assuming a functional form: the skyline plot (Pybus and colleagues 2000) estimates a population size for each interval between coalescences of an estimated genealogy, and the Bayesian skyline plot (Drummond and colleagues 2005) makes $N(t)$ piecewise constant with change points and averages over genealogies by MCMC, giving a credibility band for the population size through time back to the common ancestor of the sample. Related methods with smoothing priors on $\ln N(t)$ are standard in the study of epidemics, where sequences sampled at different times calibrate the genealogy ([7.8.6](/7.8.6#sec-6.8.3)). From a single diploid genome, the variation of the coalescence time of its two copies along the chromosome (§7.7) gives $N(t)$ with surprisingly good resolution, the basis of the pairwise sequentially Markovian coalescent (PSMC) of Li and Durbin (2011).

![Population history and the genealogy (Eq. (7.10)). Top: one simulated genealogy of n = 20 gene copies for each history, on the same scale (units of 2N₀ generations, N₀ the present size): constant size; exponential growth at rate r = 10 per 2N₀ generations backward in time; a bottleneck of size 0.05N₀ lasting 0.05 time units starting 0.2 time units ago. Bottom: the shape of the corresponding mean site frequency spectra over 2000 simulations with θ = 10, the proportion of segregating sites in each frequency class divided by its neutral value (dotted line at 1). Growth produces an excess of singletons; this bottleneck, which lets only a few lineages through, produces an excess of both rare and high-frequency derived alleles relative to intermediate ones, and both reduce total diversity](./plots/demography.py)

## 7.6. Genealogies in Structured Populations

**Definition 7.6.1 (Structured Coalescent)** The **structured coalescent** is the coalescent for a population divided into demes connected by migration: backward in time, each lineage moves from its deme to another at the backward migration rate, and two lineages can coalesce only when they are in the same deme, at rate $1/(2N_i)$ per generation in a deme of $N_i$ diploids.

**Theorem 7.6.1 (Coalescence Times in the Island Model)** In the island model with $n$ demes of $N$ diploids each, each lineage migrating with probability $m$ per generation to one of the other $n - 1$ demes chosen at random, the mean coalescence times of two copies sampled from the same deme and from different demes are

$$
\bar T_0 = 2nN, \qquad \bar T_1 = 2nN + \frac{n - 1}{2m}. \tag{7.11}
$$

**Proof** Two lineages in the same deme coalesce with probability $1/(2N)$ per generation and become separated with probability about $2m$; two lineages in different demes come together when one of them moves into the deme of the other, with probability $2m/(n - 1)$. To first order in $1/N$ and $m$, conditioning on the first generation gives $\bar T_0 = 1 + 2m\bar T_1 + (1 - 1/2N - 2m)\bar T_0$ and $\bar T_1 = 1 + [2m/(n - 1)]\bar T_0 + [1 - 2m/(n - 1)]\bar T_1$. The second equation gives $\bar T_1 = \bar T_0 + (n - 1)/(2m)$; substituting in the first, $\bar T_0/(2N) = 1 + (n - 1) = n$. $\square$

Remarkably, the mean coalescence time within a deme is the total number of gene copies, whatever the migration rate: subdivision does not change the mean, only the distribution, which becomes bimodal, with a chance of recent coalescence within the deme and a long tail from lineages that wander through the whole population. The fixation index has a genealogical definition that generalizes [Eq. (23.12)](/7.4.23#eq-23.12) to any structure (Slatkin 1991):

$$
F_{\mathrm{ST}} = \frac{\bar T - \bar T_0}{\bar T}, \tag{7.12}
$$

where $\bar T$ is the mean coalescence time of two copies taken at random from the whole population. For many demes $\bar T \approx \bar T_1$, and Eq. (7.11) gives $F_{\mathrm{ST}} \approx [(n - 1)/2m]/[2nN + (n - 1)/2m] \to 1/(1 + 4Nm)$ as $n \to \infty$. Under the infinite-sites model, mean coalescence times are proportional to mean numbers of differences, so $F_{\mathrm{ST}}$ can be estimated from sequences: if pairs of genes from the same deme differ at $2.0$ sites on average and random pairs at $8.1$, $F_{\mathrm{ST}} = (8.1 - 2.0)/8.1 = 0.75$. In a continuous two-dimensional population the analogous role is played by Wright's neighborhood size $N_{\mathrm{b}} = 4\pi\rho\sigma^2$, with $\rho$ the density and $\sigma^2$ the variance of dispersal distance per generation; the spatial models are in [7.10.10](/7.10.10). The coalescent with migration between two recently separated populations, the isolation-with-migration model, is used to distinguish gene flow from shared ancestral polymorphism ([7.10.25](/7.10.25)).

![The structured coalescent (Theorem 7.6.1). A: distribution of the coalescence time of two gene copies sampled from the same deme (blue) and from different demes (orange) in an island model of 10 demes of N = 50 diploids with 4Nm = 1, from 20 000 simulations, in units of 2nN generations; vertical lines: the means of Eq. (7.11). Copies from the same deme either coalesce quickly or escape and coalesce much later; the mean within demes equals 2nN. B: F_ST computed from mean coalescence times, Eq. (7.12), against 4Nm for 10 demes (dots: simulation; line: Eq. (7.11)), compared with Wright's 1/(1 + 4Nm) for infinitely many demes (dashed)](./plots/structure.py)

## 7.7. Recombination and the Ancestral Recombination Graph

In a sexual population, recombination gives different parts of a chromosome different ancestries. Backward in time, a lineage carrying two linked sites splits at a recombination event into two lineages, one carrying each site, which may coalesce with different lineages before possibly reuniting.

**Definition 7.7.1 (Ancestral Recombination Graph)** The **ancestral recombination graph** (ARG) of a sample of recombining sequences is the graph of their ancestry backward in time, in which lineages coalesce in pairs at rate 1 per pair (in units of $2N_{\mathrm{e}}$ generations) and each lineage splits by recombination at rate $\rho/2$, where $\rho = 4N_{\mathrm{e}}r$ is the population recombination rate for the recombination fraction $r$ across the region. Each site has a marginal genealogy, the tree embedded in the graph that follows that site, and neighboring sites have correlated marginal genealogies.

For two sites, everything depends on $N_{\mathrm{e}}r$: if it is large, the two sites spend most of their ancestry in different individuals and have nearly independent genealogies; if it is small, they share one. Linkage disequilibrium ([Definition 22.3.2](/7.4.22#def-22.3.2)) is the population-level expression of this sharing: two sites with the same genealogy have associated alleles. Under neutrality the expected standardized disequilibrium between two sites is approximately

$$
\sigma_d^2 = \frac{\mathbb{E}[D^2]}{\mathbb{E}[p_1q_1p_2q_2]} \approx \frac{10 + \rho}{22 + 13\rho + \rho^2} \tag{7.13}
$$

(Ohta and Kimura 1971), which decays like $1/\rho$ for large $\rho$: disequilibrium generated by drift extends over distances at which $4N_{\mathrm{e}}r$ is of order 10. In humans, a study of 20 copies of chromosome 21 found 35 989 SNPs in 21 Mb of unique sequence; in one 19-kb region, 26 SNPs could have formed $2^{26}$ combinations, but only seven haplotypes were present. Such haplotype blocks reflect the shared ancestry of closely linked sites, and allow most common variation to be captured by a subset of SNPs (**tag SNPs** of [7.4.25](/7.4.25)).

Along a chromosome the marginal genealogies change at each recombination that matters, and the full ARG is hard to infer. The sequentially Markov coalescent approximates it by a Markov process along the sequence: at a recombination point a lineage of the current tree detaches below the break and recoalesces elsewhere, so that each new marginal tree depends only on the previous one. This approximation underlies PSMC (§7.5.2) and the copying model of Li and Stephens ([Formula 13.4.1](/7.8.13#fml-13.4.1)), in which a new haplotype is a mosaic of existing ones, the hidden-state analogue of recombination in the ARG. Modern methods infer approximate ARGs for thousands of genomes and date the coalescences along them.

![The genealogy of two copies along a chromosome (sequentially Markov coalescent, n = 2). Each recombination event, which occurs at rate proportional to the current coalescence time, detaches one lineage at a uniformly chosen height below the common ancestor, and the lineage coalesces again at a random time above that height under the population history. A: coalescence time along 5 Mb of a simulated diploid genome (ρ = 4N_e r = 0.0004 per bp, roughly the human value; constant population size), in units of 2N_e generations; dashed: its mean 1. B: the same for a population that went through a bottleneck (size 0.1 of the present between 0.1 and 0.2 time units ago): coalescence times pile up at the bottleneck. The distribution of these segment ages along one genome is what PSMC inverts to estimate N(t)](./plots/smc.py)

## 7.8. Selection and the Genealogy

The neutral coalescent assumes that the genealogy is independent of the alleles; selection breaks this independence at the selected site and, through linkage, at sites near it ([7.10.5](/7.10.5#sec-5.4.2)):

- a selective sweep produces a burst of coalescence at the time of the sweep at sites linked to the selected allele: the genealogy is star-like near the selected site, as after a bottleneck, but only locally ([7.10.8](/7.10.8#sec-8.3));
- balancing selection keeps alleles in the population for very long times, so the genealogy at and near the selected site has two or more deep clades, one per allele, and an excess of intermediate-frequency variants; at the self-incompatibility loci of plants and the MHC of vertebrates, allelic lineages are older than species, so an allele can be more similar to an allele of another species than to other alleles of its own (trans-species polymorphism);
- purifying selection against deleterious mutations at linked sites (background selection) makes the genealogy of a neutral site resemble that of a smaller population, reducing its effective size.

Because demography affects all loci alike while selection acts locally, genome-wide data allow the two to be separated, the strategy of [7.10.8](/7.10.8).

## 7.9. From Populations to Species

When gene copies are sampled from several species, their genealogy runs inside the branches of the species tree: within each ancestral species, lineages coalesce at rate $1/(2N_{\mathrm{e}})$ of that species, and lineages from different species can coalesce only in a common ancestral species. This is the **multispecies coalescent**, the subject of [7.10.25](/7.10.25). Its first lesson follows directly from Eq. (7.1). For three species with species tree $((A, B), C)$, let the internal branch, the ancestral species of $A$ and $B$, last $\tau$ units of $2N_{\mathrm{e}}$ generations. The lineages from $A$ and $B$ coalesce within it with probability $1 - \mathrm{e}^{-\tau}$; if they fail, all three lineages enter the common ancestor of the three species, where each of the three possible pairs is equally likely to coalesce first. Hence

$$
\mathbb{P}(\text{gene tree} = \text{species tree}) = 1 - \tfrac23\mathrm{e}^{-\tau}, \qquad \mathbb{P}(\text{each discordant tree}) = \tfrac13\mathrm{e}^{-\tau}. \tag{7.14}
$$

For an internal branch of $2N_{\mathrm{e}}$ generations ($\tau = 1$), a quarter of the loci have a gene tree that differs from the species tree, purely because ancestral polymorphism persisted through the speciation events; this is **incomplete lineage sorting** ([Definition 6.1.5](/7.8.6#def-6.1.5) and the discussion there). When speciation events are close in time relative to the effective sizes, as for humans, chimpanzees and gorillas, substantial fractions of the genome support each of the three possible trees.

## Summary

| Topic | Result |
|---|---|
| gene genealogy | ancestry of a sample traced backward; every locus has its own genealogy and common ancestor (Definition 7.1.1) |
| two copies | $\mathbb{P}(T_2 > t) \approx \mathrm{e}^{-t/2N_{\mathrm{e}}}$, mean $2N_{\mathrm{e}}$ generations (Eq. (7.1)) |
| Kingman coalescent | exponential waiting times with rate $\binom{k}{2}$ per $2N_{\mathrm{e}}$ generations, random pairs (Definition 7.2.1); $\mathbb{E}[T_{\mathrm{MRCA}}] = 4N_{\mathrm{e}}(1 - 1/n)$, $\mathbb{E}[L] = 2a_n$ (Theorem 7.2.1); Moran model $N_{\mathrm{e}} = N/2$ (Definition 7.2.2) |
| mutations | infinite sites / alleles (Definition 7.3.1), $\theta = 4N_{\mathrm{e}}\mu$ (Definition 7.3.2); two sequences: geometric, mean $\theta$, $H = \theta/(1 + \theta)$ (Theorem 7.3.1); $\mathbb{E}[S] = \theta a_n$ (Theorem 7.3.2); $\hat\theta_W = S/a_n$, $\hat\theta_\pi$ (Definition 7.3.3) |
| site frequency spectrum | $\mathbb{E}[\xi_i] = \theta/i$ (Theorem 7.3.3); estimators of $\theta$ as weighted spectra |
| inference | multi-locus likelihood (Eq. (7.8)); full likelihood over genealogies by MCMC (Eq. (7.9)); human $\theta \approx 0.0005$ per site |
| simulation | generate the genealogy, then drop mutations (Algorithm 7.4.1) |
| population size | nonhomogeneous rates $\binom{k}{2}/2N(t)$ (Eq. (7.10)); growth and bottlenecks give star-like trees and excess rare variants; skyline plots, PSMC |
| structure | structured coalescent (Definition 7.6.1); $\bar T_0 = 2nN$, $\bar T_1 = 2nN + (n - 1)/2m$ (Theorem 7.6.1); $F_{\mathrm{ST}} = (\bar T - \bar T_0)/\bar T$ (Eq. (7.12)) |
| recombination | ARG with $\rho = 4N_{\mathrm{e}}r$ (Definition 7.7.1); $\sigma_d^2 \approx (10 + \rho)/(22 + 13\rho + \rho^2)$ (Eq. (7.13)); sequentially Markov coalescent, Li–Stephens |
| selection and species | sweeps compress, balancing selection deepens genealogies; three species: concordance $1 - \frac23\mathrm{e}^{-\tau}$ (Eq. (7.14)) |

## Questions

1. Show that the expected time during which a coalescent tree of $n$ lineages has exactly two lineages is at least half of its expected height, for every $n \ge 2$.

   **Answer** $\mathbb{E}[T_2] = 1$ and $\mathbb{E}[T_{\mathrm{MRCA}}] = 2(1 - 1/n) < 2$, so $\mathbb{E}[T_2]/\mathbb{E}[T_{\mathrm{MRCA}}] = n/(2(n - 1)) > 1/2$, with equality only in the limit $n \to \infty$.

2. Twenty sequences of a 2 kb locus contain $S = 30$ segregating sites, and the mean number of pairwise differences is $5.0$. Compute $\hat\theta_W$ and $\hat\theta_\pi$ per site. Which kinds of history or selection would explain the difference?

   **Answer** $a_{20} = \sum_{i=1}^{19}1/i = 3.548$, so $\hat\theta_W = 30/3.548 = 8.46$ per locus, $0.0042$ per site; $\hat\theta_\pi = 5.0$ per locus, $0.0025$ per site. $\hat\theta_\pi < \hat\theta_W$ indicates an excess of rare variants relative to neutral equilibrium (Theorem 7.3.3): population growth, a recent bottleneck or a selective sweep at a linked site, or purifying selection keeping slightly deleterious variants rare. Distinguishing them requires comparison with other loci ([7.10.8](/7.10.8)).

3. Verify the identity $\mathbb{E}[L_i] = 2/i$ of Theorem 7.3.3 for $n = 3$.

   **Answer** For $n = 3$ the tree has one epoch with 3 lineages (expected length $2/(3 \cdot 2) = 1/3$) and one with 2 (expected length 1). With 3 lineages each subtends 1 tip, contributing $3 \cdot 1/3 = 1$ to $L_1$. With 2 lineages, one subtends 1 tip and the other 2, contributing $1$ to $L_1$ and $1$ to $L_2$. So $\mathbb{E}[L_1] = 2 = 2/1$ and $\mathbb{E}[L_2] = 1 = 2/2$. In the formula, $k = 2$ gives $2 \cdot \binom{3-i-1}{0}/\binom{2}{1} = 1$ and $k = 3$ (only for $i = 1$) gives $1 \cdot \binom{1}{1}/\binom{2}{2} = 1$, as found.

4. In an island model with 20 demes of $N = 100$ diploids and $m = 0.005$, compute $\bar T_0$, $\bar T_1$ and $F_{\mathrm{ST}}$, and compare with $1/(1 + 4Nm)$.

   **Answer** $\bar T_0 = 2 \cdot 20 \cdot 100 = 4000$ generations; $\bar T_1 = 4000 + 19/0.01 = 5900$. The mean over random pairs is $\bar T = (1/20)\bar T_0 + (19/20)\bar T_1 = 5805$, so $F_{\mathrm{ST}} = (5805 - 4000)/5805 = 0.311$. Wright's formula gives $1/(1 + 2) = 0.333$; the difference comes from the finite number of demes.

5. For three species, the internal branch of the species tree lasts $0.5 \times 2N_{\mathrm{e}}$ generations. What fraction of unlinked loci are expected to support each of the three rooted topologies? Why does the most frequent gene tree still estimate the species tree correctly?

   **Answer** By Eq. (7.14), the species tree topology has probability $1 - \frac23\mathrm{e}^{-0.5} = 0.596$ and each of the two discordant topologies $\frac13\mathrm{e}^{-0.5} = 0.202$. Because the two discordant topologies are equally probable and each is less probable than the concordant one for any $\tau > 0$, the most frequent topology across many loci is the species tree; this is not true for all four or more species, where anomalous gene trees can be the most frequent ([7.10.25](/7.10.25)).
