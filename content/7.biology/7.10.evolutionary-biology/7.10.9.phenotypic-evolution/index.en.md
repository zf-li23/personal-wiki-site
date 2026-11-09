---
title: Phenotypic Evolution
description: "Evolution of quantitative traits. Fitness functions and the forms of selection (directional, stabilizing, disruptive, correlational); selection differentials and Lande–Arnold selection gradients; the response to directional selection R = V_A β, dominance and epistasis, standing variation and new mutations, and evolutionary rescue with its critical rate of environmental change; artificial selection and long-term response; the G matrix, the multivariate breeder's equation, correlated responses, constraints and genetic lines of least resistance; phenotypic plasticity and the evolution of reaction norms; the genetic architecture of quantitative traits and the maintenance of their variation."
---

Most of the traits by which organisms differ, from body size and bill depth to flowering time and crop yield, are **quantitative traits**: they vary continuously and are influenced by many loci and by the environment. Their inheritance was treated in [7.4.24](/7.4.24): the partition of phenotypic variance $V_P$ into additive, dominance and environmental parts, the **narrow-sense heritability** $h^2 = V_A/V_P$, the **selection differential** and the **breeder's equation** $R = h^2S$ ([Theorem 24.5.1 in 7.4.24](/7.4.24#thm-24.5.1)); the mapping of the underlying loci is the subject of [7.4.25](/7.4.25). This chapter asks the evolutionary questions. How does natural selection act on a continuous phenotype, and how can its strength be measured in the wild? How fast does a trait evolve, and when is adaptation fast enough to save a population from a changing environment? How do correlations among traits steer and constrain evolution, how do organisms evolve responses to the environment itself, and what kind of genetic variation does all this use? The tools are those of single-locus selection theory ([7.10.5](/7.10.5)) recast for means, variances and covariances of phenotypes; the same tools reappear for life histories ([7.10.15](/7.10.15)), sexual selection ([7.10.13](/7.10.13)) and comparative analyses of trait evolution on phylogenies ([7.10.26](/7.10.26)).

## 9.1. Genotypes, Phenotypes and Continuous Variation

Variation in DNA is discrete, yet a trait such as human height varies smoothly. The connection is the one made in [7.4.24](/7.4.24#thm-24.1.1): a **phenotype** is the sum of contributions from many loci plus environmental effects, so that even a few loci with moderate environmental variance give a smooth, nearly normal distribution. Each **genotype** has its own distribution of phenotypes, and the population distribution is their mixture.

The evolutionary consequence is that a quantitative trait can be carried far outside its original range by changes in allele frequencies alone, without new mutations. Changing the frequency of the "large" allele from $0.25$ to $0.75$ at a single locus whose allele adds $3$ units moves the mean by $3$ units, and the two distributions overlap broadly; the rarest genotype ($A_2A_2$, frequency $0.25^2 = 6.25\,\%$) was already common enough to be seen. With many loci the situation changes qualitatively.

**Example 9.1.1** Let $50$ unlinked additive loci each carry an allele that adds $0.4$ units, all at frequency $p$. The mean genotypic value is $2 \cdot 50 \cdot 0.4\,p = 40p$, and the genetic variance is $\sum 2pq\,a^2 = 100 \cdot 0.16\,pq = 16pq$. Raising $p$ from $0.25$ to $0.75$ shifts the mean by $20$ units, while the genetic standard deviation at either frequency is $\sqrt{16 \cdot 0.1875} = 1.73$: the new mean lies more than eleven standard deviations above the old one. The genotype homozygous for all fifty "large" alleles had frequency $0.25^{100} \approx 6 \times 10^{-61}$ in the original population; it never existed there, yet after the shift it has frequency $0.75^{100} \approx 3 \times 10^{-13}$, and phenotypes near it are common. Selection on standing variation in many loci therefore creates genuinely new phenotypes by recombining existing alleles.

## 9.2. Fitness Functions and the Forms of Selection

**Definition 9.2.1 (Fitness Function)** A **fitness function** $w(z)$ gives the expected fitness (or a fitness component such as survival or mating success) of individuals with phenotype $z$. For several traits $\boldsymbol{z} = (z_1, \dots, z_k)^{\mathsf T}$ it is a surface $w(\boldsymbol{z})$ over the space of trait combinations.

The fitness function describes individuals. It must be distinguished from the **adaptive landscape** of [7.10.5](/7.10.5), which for a quantitative trait plots the *mean* fitness $\bar w$ of a population against its *mean* phenotype $\bar z$. The two are related by averaging $w(z)$ over the phenotype distribution, so the landscape is a smoothed version of the fitness function.

A classic estimate comes from horned lizards (*Phrynosoma mcalli*), which loggerhead shrikes (*Lanius ludovicianus*) kill and impale on thorns. Comparing horn lengths of living lizards with those of impaled ones gives survival as a function of relative horn length, and survival increases steadily with horn length. This is **directional selection** ([7.4.23](/7.4.23)): it favors one extreme and shifts the mean. A famous case is the drought of 1977 on Daphne Major in the Galápagos, during which the seeds available to the medium ground finch (*Geospiza fortis*) became larger and harder; of 751 birds measured before the drought about 90 survived, and survival rose with bill depth, so that the mean bill depth of the survivors was about $0.5\,\mathrm{mm}$ larger than before. Note that this is selection within a generation, not yet evolution.

**Definition 9.2.2 (Stabilizing, Disruptive and Correlational Selection)** For a quantitative trait, **stabilizing selection** favors individuals near the population mean, so that a peak of the fitness function lies within the distribution and selection reduces the phenotypic variance; **disruptive selection** favors both extremes over intermediates, a trough of the fitness function lies within the distribution and selection increases the variance. For two or more traits, **correlational selection** favors particular combinations of trait values, so that the effect of one trait on fitness depends on the value of another.

Human birth weight is the textbook case of stabilizing selection: infants much lighter or much heavier than average have lower survival to 28 days. Disruptive selection is seen in the black-bellied seedcracker (*Pyrenestes ostrinus*), in which birds with intermediate lower-mandible length survive worst; such selection rarely splits a population, but it makes intermediates rarer. In the laboratory, disruptive selection on the number of sternopleural bristles of *Drosophila melanogaster*, breeding each generation only from flies with many or few bristles, turned a unimodal distribution into a bimodal one within about a dozen generations (Thoday and Gibson 1962), although the result proved hard to repeat. In the large-eared horseshoe bat *Rhinolophus philippinensis* of Southeast Asia, three size morphs echolocate at frequencies that are close to successive harmonics of one fundamental; the larger morphs call at lower frequencies, detect larger insects at greater range and eat larger prey, and because the call is also used in mate recognition, the divergence of a frequency may contribute to reproductive isolation (Kingston and Rossiter 2004). In the northwestern garter snake (*Thamnophis ordinoides*), striped snakes that flee in a straight line and unstriped snakes that reverse course both survive well, whereas the other two combinations do not: a moving stripe makes it hard for a visual predator to judge speed, and reversals of an unstriped snake confuse it. That is correlational selection.

Whether selection is directional, stabilizing or disruptive is not a property of the fitness function alone but of the function together with the position of the population. Red crossbills (*Loxia curvirostra*) feeding on conifer cones have a fitness function for bill depth with several peaks, each corresponding to the bill that is best for one kind of cone. A population on a slope of this function experiences directional selection, one near a peak stabilizing selection and one in a trough disruptive selection (Figure, panel D). Selection can also change the mean and the variance at once.

![Modes of selection on a normally distributed trait. Top row: fitness functions w(z); bottom row: the trait density before selection (gray) and among survivors (green), with the selection differential S and the factor by which the variance changes. A: directional selection (logistic fitness) shifts the mean (S = 0.62) and slightly reduces the variance. B: stabilizing selection (Gaussian peak at the mean) leaves the mean unchanged and halves the variance. C: disruptive selection (a dip at the mean) increases the variance 1.7-fold. D: a fitness function with two peaks, as for bill depth in crossbills feeding on two kinds of cones; populations 1, 2 and 3 (dashed: before, solid: after selection) experience directional, disruptive and stabilizing selection, depending on where they lie](./plots/modes-of-selection.py)

For a Gaussian fitness function the effect of stabilizing selection on a normal distribution can be written exactly.

**Formula 9.2.1 (Gaussian Stabilizing Selection)** Let the phenotypes before selection be $\mathcal{N}(\bar z, V_P)$ and $w(z) = \exp[-(z - \theta)^2/(2\omega^2)]$, with optimum $\theta$ and width $\omega$ (small $\omega$ means strong selection). Then the selected individuals are again normal with

$$
\bar z^* = \frac{\omega^2\bar z + V_P\,\theta}{\omega^2 + V_P}, \qquad V_P^* = \frac{\omega^2 V_P}{\omega^2 + V_P}, \tag{9.1}
$$
and the mean fitness is $\bar w = \sqrt{\omega^2/V_s}\,\exp[-(\bar z - \theta)^2/(2V_s)]$ with $V_s = \omega^2 + V_P$.

**Proof** The product of the normal density and $w$ is the exponential of a quadratic in $z$; completing the square gives a normal density whose precision is the sum $1/V_P + 1/\omega^2$ and whose mean is the precision-weighted average of $\bar z$ and $\theta$, which is Eq. (9.1). Integrating the product over $z$ gives $\bar w$. $\square$

The mean fitness is itself a Gaussian function of $\bar z$, of width $V_s$: the adaptive landscape is a smoothed fitness function, as stated above. $V_s$ is often called the strength of stabilizing selection (a large $V_s$ means weak selection).

## 9.3. Measuring the Strength of Selection

### 9.3.1. Selection Differentials and Gradients

The **selection differential** $S = \bar z^* - \bar z$ ([7.4.24](/7.4.24#def-24.5.1)) measures how much selection changes the mean within a generation. With **relative fitness** $w$ (fitness divided by its mean, so that $\bar w = 1$), the mean after selection is $\bar z^* = \mathbb{E}[wz]$, and therefore

$$
S = \operatorname{Cov}(w, z). \tag{9.2}
$$
This identity (Robertson's covariance theorem) holds for any distribution. But $S$ mixes the direct effect of the trait on fitness with indirect effects of correlated traits: a trait with no effect on fitness has $S \neq 0$ if it is correlated with one that does.

**Definition 9.3.1 (Selection Gradient)** For traits $\boldsymbol{z}$ with phenotypic covariance matrix $P$, the (directional) **selection gradient** is the vector of partial regression coefficients of relative fitness on the traits,

$$
\boldsymbol{\beta} = P^{-1}\boldsymbol{S}, \qquad w = \alpha + \sum_i \beta_i z_i + \varepsilon, \tag{9.3}
$$
where $\boldsymbol{S}$ is the vector of selection differentials. For one trait $\beta = S/V_P$, the slope of the regression of relative fitness on the trait; its units are the inverse of the trait's units. The quadratic regression

$$
w = \alpha + \sum_i \beta_i z_i + \frac12\sum_{i,j}\gamma_{ij}z_iz_j + \varepsilon \tag{9.4}
$$
defines the matrix $\Gamma = (\gamma_{ij})$ of quadratic selection gradients: $\gamma_{ii} < 0$ indicates stabilizing and $\gamma_{ii} > 0$ disruptive selection on trait $i$, and $\gamma_{ij} \neq 0$ correlational selection on traits $i$ and $j$.

This regression approach was introduced by Lande and Arnold (1983). The partial regression is the point: $\beta_i$ measures selection acting directly on trait $i$, holding the other measured traits constant. The selection gradient plays for a quantitative trait the role that the **selection coefficient** plays for an allele. When phenotypes are normally distributed, $\boldsymbol{\beta}$ also equals the gradient of $\ln\bar w$ with respect to the mean phenotype (Lande 1979): populations climb the adaptive landscape in the direction of $\boldsymbol{\beta}$, and $\boldsymbol{\beta} = \boldsymbol{0}$ at a peak. In Formula 9.2.1, $\beta = \partial\ln\bar w/\partial\bar z = (\theta - \bar z)/V_s$ and $\gamma = -1/V_s$ to first order.

**Example 9.3.1** Female guppies (*Poecilia reticulata*) prefer males with more orange on the body. Regressing the relative mating success of males on the proportion of their body surface that is orange gives $\beta = 3.8$ (unitless, because the trait is a proportion): if they existed, completely orange males would have on average $3.8$ times more matings than males with no orange.

:::

In practice the fitness measured is usually a component (survival over a season, mating success) rather than lifetime fitness, survival is often binary, and the regression is then fitted to $0/1$ data; the gradients are still estimated by ordinary least squares on relative fitness, while their significance is tested with a model appropriate for the data, such as logistic regression. Two cautions apply. An unmeasured trait correlated with the measured ones, or an environmental factor that affects both the trait and fitness (well-fed individuals are both larger and more fecund), biases $\boldsymbol{\beta}$; and the gradients describe selection on phenotypes, whether or not the traits are heritable.

![Estimating selection gradients by regression on simulated data (500 individuals, survival probability increasing with the standardized trait but falling off at high values). A: relative fitness (jittered dots; circles: means in bins of 0.5 SD) against the trait. The slope of the linear regression is the directional gradient, β = 0.31 ± 0.04; the quadratic regression on z and z²/2 gives γ = −0.19 ± 0.05, detecting stabilizing selection on top of directional selection. B: a fitness surface with stabilizing and correlational selection (γ₁₁ = γ₂₂ = −0.4, γ₁₂ = 0.3); contours of relative fitness form a ridge along which high values of both traits, or low values of both, are favored. Dotted circle: 95 % of the phenotype distribution](./plots/lande-arnold.py)

### 9.3.2. Selection in Natural Populations

Thousands of selection gradients have been estimated in wild animals and plants. A compilation of 2819 estimates of $\beta$ for size from 143 studies, standardized by multiplying each $\beta$ by the trait's phenotypic standard deviation so that different traits can be compared, shows that directional selection is common and sometimes very strong: strong enough to shift the mean by more than a phenotypic standard deviation within a generation. Gradients can also test hypotheses about adaptation. If a trait is at its optimum, $\beta$ should be zero. Many birds can physiologically lay more eggs than they do; the selection gradient on clutch size is close to zero, because females that lay more eggs than average hatch more chicks but cannot feed them all ([7.10.15](/7.10.15)).

## 9.4. Evolution under Directional Selection

### 9.4.1. The Response to Selection

**Theorem 9.4.1 (Breeder's Equation in Gradient Form)** If offspring phenotype regresses linearly on midparent phenotype, the change in the mean phenotype from one generation to the next is

$$
\Delta\bar z = h^2S = V_A\beta. \tag{9.5}
$$

**Proof** The first equality is the breeder's equation ([Theorem 24.5.1 in 7.4.24](/7.4.24#thm-24.5.1)). Substituting $S = V_P\beta$ and $h^2 = V_A/V_P$ gives the second. $\square$

The gradient form separates the two ingredients of evolution as cleanly as possible: $\beta$ measures selection, $V_A$ measures heritable variation. The trait does not evolve if it is heritable but not selected ($\beta = 0$), or selected but without additive variance ($V_A = 0$). Two consequences are worth stating. The short-term rate of evolution can be predicted without knowing anything about the genes involved, and it does not depend on the number of loci; and, in the short term, it does not depend on population size: a small population with the same $V_A$ evolves as fast as a large one.

**Example 9.4.1** In the Galápagos finch *Geospiza fortis* the heritability of bill depth, estimated from parent–offspring regression, was about $0.8$. The 1977 drought produced a selection differential of about $0.53$ phenotypic standard deviations, which predicts a response of $R \approx 0.8 \cdot 0.53 = 0.42$ standard deviations; the offspring hatched in 1978 had bills about $0.6$ standard deviations deeper than those hatched in 1976: the response had the predicted direction and order of magnitude, though it was somewhat larger than predicted. (The calculation ignores selection at other stages of the life cycle, environmental effects on bill size and selection on correlated traits, §9.6.)

**Example 9.4.2** In a population of migratory locusts the mean leg length is $18.6\,\mathrm{mm}$ with phenotypic variance $V_P = 1.4\,\mathrm{mm^2}$ and heritability $h^2 = 0.37$, and the selection gradient is $\beta = -0.13\,\mathrm{mm^{-1}}$. Then $V_A = 0.37 \cdot 1.4 = 0.518\,\mathrm{mm^2}$ and $\Delta\bar z = 0.518 \cdot (-0.13) = -0.067\,\mathrm{mm}$: the mean leg length of the next generation is predicted to be $18.53\,\mathrm{mm}$, if no other trait is selected (but see Example 9.6.1).

### 9.4.2. Dominance and Epistasis

Only the additive part of the genetic variance contributes to Eq. (9.5). Imagine a plant whose height is determined by one overdominant locus: $A_1A_1$ and $A_2A_2$ are $20\,\mathrm{cm}$ tall and $A_1A_2$ is $25\,\mathrm{cm}$, both alleles at frequency $1/2$. All variation is genetic, but none is additive ($\alpha = 0$, [Theorem 24.3.1 in 7.4.24](/7.4.24#thm-24.3.1)). If only the tall plants reproduce, the next generation again has half short and half tall plants: selection has no lasting effect. Epistatic variance likewise contributes little to the permanent response, because the favorable combinations of alleles at different loci are broken up by recombination. For most traits the additive variance is much larger than the dominance and epistatic variances, so most genetic variation is usable by selection. But all three variances change as allele frequencies change: dominance and epistatic variance can be converted into additive variance (and back), and selection that fixes the contributing alleles erodes $V_A$ and slows the response.

### 9.4.3. Standing Variation and New Mutations

A trait responds immediately if it has **standing genetic variation** ([7.10.5](/7.10.5)); a trait without it must wait for mutations. The supply of new mutations is proportional to the number of gene copies, so the wait is longest in small populations. Mutation does replenish quantitative variation surprisingly fast. The *mutational variance* $V_M$, the increase per generation in the genetic variance among lines that start genetically identical and accumulate mutations without selection, is typically $10^{-3}$ to $10^{-2}$ of the environmental variance; in *Drosophila*, mutation raises the phenotypic variance of a trait by $0.1$–$1\,\%$ per generation. Since a heritability near $1/2$ means $V_A \approx V_E$, mutation alone would rebuild such variance in $100$–$1000$ generations. Nevertheless, populations that start without variation respond much more slowly: a review of six selection experiments that began with inbred lines found an average response over the first 50 generations of $0.07$ phenotypic standard deviations per generation, against about $0.5$ for bristle number in outbred *Drosophila*. How often adaptation in nature uses standing variation rather than new mutations is an open question.

### 9.4.4. Evolutionary Rescue

**Definition 9.4.1 (Evolutionary Rescue)** **Evolutionary rescue** is the recovery of a population that has begun to decline toward extinction because of an environmental change, brought about by adaptive evolution that restores positive population growth before the population is lost.

Rescue is a race between adaptation and decline, and Formula 9.2.1 turns it into a simple model. Let the expected number of offspring of an individual with phenotype $z$ be $W_{\max}\exp[-(z - \theta)^2/(2\omega^2)]$. A population with mean $\bar z$ then has mean fitness, its growth factor per generation,

$$
\bar W = W_0\exp\!\left[-\frac{(\bar z - \theta)^2}{2V_s}\right], \qquad W_0 = W_{\max}\sqrt{\omega^2/V_s}, \tag{9.6}
$$
and by Eq. (9.5) with $\beta = (\theta - \bar z)/V_s$ the mean moves toward the optimum by $\Delta\bar z = V_A(\theta - \bar z)/V_s$. After a sudden shift of the optimum by $\delta$, the lag $\bar z - \theta$ shrinks by the factor $1 - V_A/V_s$ per generation, and the population declines as long as the lag exceeds $\sqrt{2V_s\ln W_0}$. Whether it survives the bottleneck depends on how deep and how long the decline is: more additive variance shortens it, and a larger initial population, more beneficial mutations and physiological buffering of the change all make survival more likely.

A steadily changing environment, such as a warming climate, poses a different threshold.

**Formula 9.4.1 (Critical Rate of Environmental Change)** If the optimum moves at a constant rate $b$ per generation, $\theta_t = bt$, the lag of the mean in the model of Eq. (9.6) approaches $L = bV_s/V_A$, and the population persists in the long run only if $\bar W \geq 1$ at this lag, that is, if

$$
b \leq b_{\mathrm{c}} = V_A\sqrt{\frac{2\ln W_0}{V_s}}. \tag{9.7}
$$

**Proof** With $\theta_t = bt$ the lag $L_t = \theta_t - \bar z_t$ obeys $L_{t+1} = L_t(1 - V_A/V_s) + b$, whose fixed point is $L = bV_s/V_A$. Setting $\bar W = 1$ in Eq. (9.6) at this lag and solving for $b$ gives Eq. (9.7). $\square$

The critical rate is proportional to the additive variance and to the square root of the intrinsic growth rate $\ln W_0$, and it is lower when stabilizing selection is weak ($V_s$ large), because weak selection makes the population track the optimum slowly. Models of this kind (Lynch and Lande 1993; Gomulkiewicz and Holt 1995) are the basis of predictions about which species can adapt to climate change.

![Evolutionary rescue in the quantitative-genetic model of Eq. (9.6) with W₀ = 1.3 and V_s = 10 (phenotype in SD units); numbers follow density-dependent growth up to the carrying capacity K with Poisson sampling. A: after the optimum jumps by 3.5 SD, a population with V_A = 0.1 and K = 1000 declines and nearly always goes extinct (thick: median of 200 runs; thin: single runs); with four times the additive variance, or twenty times the carrying capacity, adaptation brings the growth rate back above 1 before the population is lost (fraction of runs surviving in the legend). B: with a steadily moving optimum the population settles at a lower size for rates below the critical rate b_c of Eq. (9.7) (here V_A = 0.3, b_c = 0.069 SD per generation) and goes extinct above it](./plots/evolutionary-rescue.py)

Rescue has been observed directly. Laboratory populations of yeast suddenly exposed to high salt concentrations first declined as cells died faster than they divided, then recovered as they adapted. In nature, transplant experiments with the partridge-pea (*Chamaecrista fasciculata*) moved plants from three populations along a north–south transect to sites as warm and dry as their home sites are predicted to become; the transplants had reduced fitness, and only one of the three populations had enough genetic variation to be likely to adapt. During the Pleistocene many species survived climate change by moving rather than adapting, and present climate change is more than a hundred times faster.

## 9.5. Artificial Selection

**Definition 9.5.1 (Artificial Selection)** **Artificial selection** is selection in which humans decide which individuals reproduce, according to their phenotypes (or, in modern breeding, their estimated breeding values).

The domestication of crops and animals, beginning some 11 000 years ago, was the first large-scale use of evolution by humans; the result is visible in every supermarket, whose wheat, tomatoes and milk come from species radically changed from their wild ancestors. Darwin used artificial selection as his main analogy for natural selection. Artificial selection is still effective: milk production and poultry growth continue to increase by $1$–$2\,\%$ per year. Selection experiments, often on *Drosophila* or *Escherichia coli*, show several general patterns.

- *Almost every trait responds.* Hundreds of experiments show an immediate response based on standing variation in nearly all traits and species.
- *Traits evolve far beyond their original range.* In the Illinois long-term selection experiment on maize ([7.4.24](/7.4.24)), the mean oil content of the kernel rose from $4.7\,\%$, when the highest value on any ear was $6\,\%$, to $22\,\%$ after 107 generations. In *Drosophila* selected for flying upwind toward a light, the average flight speed rose 85-fold, from $2$ to $170\,\mathrm{cm\,s^{-1}}$, in 100 generations of selecting the best $4.5\,\%$.
- *Large populations evolve faster and farther.* Nothing in Eq. (9.5) depends on population size, but over many generations the additive variance declines faster in small populations, through drift and the fixation of favorable alleles. Rare species may therefore adapt more slowly than common ones.
- *Strong selection on one trait has side effects on others.* Fifty years of selection for milk yield in dairy cattle raised production by about $1\,\%$ per year while fertility declined at about the same rate (§9.6).
- *Rates exceed those in the fossil record.* Measured in darwins (a change by a factor $\mathrm{e}$ per million years, i.e. about one part per million per year), rates of change under artificial selection are orders of magnitude higher than rates over long intervals of the fossil record, which mostly reflect long periods of little net change.

Why does the response continue for so long? If the additive variance were due to a few alleles of large effect, selection would fix them in a few tens of generations and the response would stop. Two explanations, not mutually exclusive, account for sustained responses. In the *infinitesimal model* the additive variance is due to very many alleles of small effect, each of whose frequencies changes only slightly, so that the variance stays nearly constant while the mean moves; the breeder's equation is then exact. Alternatively, new mutations, including some of large effect, arise in the selected lines and are picked up quickly. Sharp jumps in selected lines have sometimes been traced to single alleles of large effect, often recessive lethals with a large effect on the trait in heterozygotes, which are then held at intermediate frequency by the balance between artificial selection for heterozygotes and natural selection against homozygotes; when artificial selection is relaxed, the mean falls back as natural selection removes them. Mutations of large effect usually have deleterious pleiotropic effects, and their side effects are later reduced by modifier alleles of small effect.

![Long-term response to truncation selection in individual-based simulations (250 individuals, the best 50 become parents, unlinked loci, V_E = 1; two replicate lines in each panel). Top: change in the mean phenotype; bottom: additive genetic variance. A: ten loci with favorable alleles of large effect at frequency 0.1; the variance first rises as they reach intermediate frequencies, and the response stops when they are fixed after about 15 generations. B: 400 loci of small effect plus two major loci; the response continues throughout while the variance declines slowly. C: 100 loci with mutation (mutational variance 0.0023 per generation); the response continues at a high rate](./plots/long-term-response.py)

Over a few tens of generations, simply assuming constant additive variance predicts the response well; over longer periods we do not know enough about the genetic basis of variation to predict how long a response will last.

## 9.6. Correlated Traits

### 9.6.1. The G Matrix and the Multivariate Breeder's Equation

Traits are correlated: individuals with long arms tend to have long legs. Part of such a correlation is genetic, which means that selection on one trait changes others.

**Definition 9.6.1 (G Matrix and Genetic Correlation)** The **G matrix** of $k$ traits is the $k \times k$ covariance matrix of their breeding values: the additive genetic variances $G_{ii} = V_{A,i}$ on the diagonal and the additive genetic covariances $G_{ij}$ off it. The **genetic correlation** of traits $i$ and $j$ is $r_A = G_{ij}/\sqrt{G_{ii}G_{jj}}$.

**Theorem 9.6.1 (Multivariate Breeder's Equation)** If the breeding values and environmental deviations of the traits are multivariate normal and independent of each other, the change in the vector of trait means in one generation is

$$
\Delta\bar{\boldsymbol{z}} = G\boldsymbol{\beta} = GP^{-1}\boldsymbol{S}. \tag{9.8}
$$

**Proof** Under the assumptions, breeding values $\boldsymbol{a}$ and phenotypes $\boldsymbol{z} = \boldsymbol{a} + \boldsymbol{e}$ are jointly normal with $\operatorname{Cov}(\boldsymbol{a}, \boldsymbol{z}) = G$, so the regression of breeding value on phenotype is $\mathbb{E}[\boldsymbol{a} \mid \boldsymbol{z}] = \bar{\boldsymbol{a}} + GP^{-1}(\boldsymbol{z} - \bar{\boldsymbol{z}})$. Selection changes the mean phenotype of the parents by $\boldsymbol{S}$, hence their mean breeding value by $GP^{-1}\boldsymbol{S}$, and offspring inherit the mean breeding value of their parents. $\square$

Eq. (9.8) is due to Lande (1979). For two traits it reads $\Delta\bar z_1 = G_{11}\beta_1 + G_{12}\beta_2$: trait 1 changes both by the direct response to selection on itself and by a correlated response to selection on trait 2.

**Definition 9.6.2 (Correlated Response)** A **correlated response** (indirect response to selection) is the evolutionary change of a trait caused by selection on other traits with which it is genetically correlated, the term $\sum_{j \neq i} G_{ij}\beta_j$ in Eq. (9.8).

A trait can therefore evolve even when it is not selected at all, and it can evolve in the direction opposite to that favored by selection on it.

**Example 9.6.1** In the locusts of Example 9.4.2, wing length has $V_P = 3.6\,\mathrm{mm^2}$, $h^2 = 0.27$ and $\beta = 0.12\,\mathrm{mm^{-1}}$, and the additive genetic covariance of wing and leg length is $0.6\,\mathrm{mm^2}$. Then $G_{\mathrm{wing}} = 0.27 \cdot 3.6 = 0.972\,\mathrm{mm^2}$ and

$$
\begin{aligned}
\Delta\bar z_{\mathrm{leg}} &= 0.518 \cdot (-0.13) + 0.6 \cdot 0.12 = -0.067 + 0.072 = +0.005\,\mathrm{mm},\\
\Delta\bar z_{\mathrm{wing}} &= 0.6 \cdot (-0.13) + 0.972 \cdot 0.12 = -0.078 + 0.117 = +0.039\,\mathrm{mm}.
\end{aligned}
$$
Selection favors shorter legs, yet legs are predicted to become slightly longer, because the correlated response to selection for longer wings ($r_A = 0.6/\sqrt{0.518 \cdot 0.972} = 0.85$) outweighs the direct response.

:::

The same thing happened to Galápagos finches during the 1977 drought: selection directly favored narrower bills, yet the survivors had wider bills on average, because bill width is strongly correlated with body size and bill depth, which were favored. Correlated responses may also explain puzzling losses of structures. Cave populations of the Mexican tetra (*Astyanax mexicanus*) have lost their eyes; mutations that increase the sensitivity of the vibration-detecting sensory cells on the head, which the fish use to find prey in the dark, also reduce the eyes as a correlated effect.

### 9.6.2. Constraints, Trade-offs and Lines of Least Resistance

**Definition 9.6.3 (Evolutionary Constraint)** An **evolutionary constraint** is any feature of a population that prevents or slows evolution in a direction favored by selection. A genetic constraint is a lack of additive genetic variation in that direction, either in a single trait or, because of genetic correlations, in a combination of traits.

Species of *Drosophila* restricted to wet tropical forests have little or no genetic variation for tolerance of desiccation and cold, which may explain why their ranges do not expand into drier habitats (§10.8 in [7.10.10](/7.10.10)). Correlations add a subtler kind of constraint: every trait may vary while some combinations of traits do not. A deer selected to run faster benefits from stronger leg bones, but thicker bones are heavier; in quantitative-genetic terms, bone strength and weight are highly correlated, and evolution along one requires change in the other. This is a **trade-off** ([7.10.3](/7.10.3)) seen through the G matrix.

**Definition 9.6.4 (Genetic Line of Least Resistance)** The **genetic line of least resistance** of a population is the direction in trait space with the most additive genetic variance, the leading eigenvector $\boldsymbol{g}_{\max}$ of $G$ (Schluter 1996). Combinations of traits along $\boldsymbol{g}_{\max}$ evolve fastest; those along eigenvectors with small eigenvalues evolve slowly.

By Eq. (9.8), the response $G\boldsymbol{\beta}$ is the selection gradient rotated toward $\boldsymbol{g}_{\max}$ and stretched along it. In a northern (Minnesota) population of the partridge-pea, plant size (leaf number) and growth rate have a strong negative genetic correlation: there is ample variation for more leaves with slower growth, or fewer leaves with faster growth, but little for more leaves with faster growth, which is what a warmer climate favors. The negative correlation is predicted to make the population unable to adapt. In the butterfly *Bicyclus anynana*, artificial selection changed the sizes of two dorsal eyespots in every combination, large–large, small–small and large–small alike; selection on the colors of two ventral eyespots made both blacker or both more golden, but failed to make one black and the other gold, because their colors are genetically correlated.

![The G matrix and the multivariate breeder's equation. A: the 1-SD ellipse of the additive genetic covariance matrix of two traits with genetic correlation 0.8; its long axis is the genetic line of least resistance g_max. Selection favors larger z₁ and smaller z₂ (β), but the response Gβ points mostly along g_max: z₂ increases, a correlated response. B: evolution of the mean toward an optimum (star) under stabilizing selection (dots every 10 generations): with uncorrelated traits the path is straight; with genetic correlation 0.8 the population first moves along g_max, then creeps toward the optimum in the direction of little genetic variance](./plots/g-matrix.py)

A genetic correlation is a constraint in the long term only if it persists. As long as $G$ has no zero eigenvalue, a population under constant stabilizing selection eventually reaches its optimum, only slower and by a curved path (Figure, panel B); and genetic covariances themselves change as allele frequencies change. Many morphological traits are correlated with overall body size, and such correlations can be stable over thousands or millions of years, whereas others change over shorter periods. Whether the constraints seen in short-term experiments, like the *Bicyclus* eyespots, persist over macroevolutionary time is an open question that comparative studies of $G$ and of divergence among species address ([7.10.32](/7.10.32)).

### 9.6.3. Causes of Genetic Correlations

Genetic correlations have two sources. **Pleiotropy** ([7.4.3](/7.4.3)), the effect of one locus on several traits, creates correlations that persist as long as the alleles segregate: the many loci affecting human body size correlate nearly all morphological traits. **Linkage disequilibrium** ([7.4.22](/7.4.22)) between loci affecting different traits creates correlations that recombination erodes unless something maintains them. Correlational selection is one such force: in the garter snakes, color pattern and escape behavior are genetically correlated in the direction favored by selection. In the butterfly *Heliconius numata*, several wing-color morphs mimic different distasteful species, and predators select for particular combinations of color elements. The morphs are controlled by a small chromosome segment containing 18 genes, in which overlapping **inversions** ([7.4.15](/7.4.15)) suppress recombination: the inversions spread because they lock together favorable combinations of alleles, strengthening the genetic correlation that selection favors. Such a block of tightly linked loci that behaves as a single Mendelian unit is called a supergene.

## 9.7. Phenotypic Plasticity

Tadpoles of spadefoot toads (*Spea*) that hatch in ponds where algae are the main food develop into omnivores with large fat reserves; in ponds with many shrimp they develop into carnivores with large heads and a sharp beak, which grow faster and metamorphose earlier. Since such ponds tend to dry quickly, the switch is adaptive. This is **phenotypic plasticity** ([7.5.38](/7.5.38)): the production of different phenotypes by one genotype in different environments. Plasticity may be developmental and irreversible, as in the tadpoles, or physiological and reversible, as in tanning of light skin after exposure to ultraviolet light; it occurs in gene expression, morphology, physiology and behavior.

Plasticity is described by the **norm of reaction** ([7.4.3](/7.4.3#sec-3.5.4)) of each genotype, the phenotype as a function of the environment. When reaction norms of different genotypes are not parallel there is **genotype–environment interaction** (G×E), and the reaction norm itself has genetic variation and can evolve. In the water flea *Daphnia melanica*, individuals from lakes without fish develop dark melanin pigmentation, which protects them from ultraviolet radiation, under strong ultraviolet light; those from lakes with fish predators do not, because pigmentation would make them conspicuous. Plasticity is adaptive in one kind of lake and its absence in the other.

Not all plasticity is adaptive. When people from low elevations move to high elevations, their concentration of red blood cells increases; the response sounds adaptive, but it makes the blood more viscous, slows oxygen delivery and can cause illness. Tibetan highlanders have red-cell concentrations similar to those of lowlanders and have adapted through genetic changes in other traits (Andean highlanders, by contrast, do have elevated hemoglobin concentrations) ([7.10.8](/7.10.8), [7.10.33](/7.10.33)).

The evolution of plasticity can be modeled by treating the intercept and slope of a linear reaction norm as two correlated quantitative traits.

**Formula 9.7.1 (Optimal Plasticity with an Unreliable Cue)** Let a genotype develop the phenotype $z = a + b\,e_{\mathrm{d}}$ in response to the environment $e_{\mathrm{d}}$ experienced during development, while the optimum is $\theta = A + B\,e_{\mathrm{s}}$ in the environment $e_{\mathrm{s}}$ of selection, where $e_{\mathrm{d}}$ and $e_{\mathrm{s}}$ have equal variances and correlation $\rho$. Under Gaussian stabilizing selection, and ignoring costs of plasticity, the slope that maximizes mean fitness is

$$
b^* = \rho B. \tag{9.9}
$$

**Proof** Maximizing the expected log fitness $-\mathbb{E}[(z - \theta)^2]/(2V_s)$ is minimizing the mean squared deviation $\mathbb{E}[(a + b\,e_{\mathrm{d}} - A - B\,e_{\mathrm{s}})^2]$, a least-squares problem whose solution is the regression of $\theta$ on $e_{\mathrm{d}}$: $b^* = B\operatorname{Cov}(e_{\mathrm{d}}, e_{\mathrm{s}})/\operatorname{Var}(e_{\mathrm{d}}) = \rho B$. $\square$

Plasticity should therefore match the environmental sensitivity of the optimum ($B$) discounted by the reliability of the cue ($\rho$). Unreliable cues, a long delay between development and selection, and costs of maintaining the sensory and regulatory machinery all favor less plasticity than $B$; fixed developmental responses (**canalization**, [7.5.1](/7.5.1)) evolve where cues are uninformative. When a population moves into a new environment, plasticity may produce a roughly adaptive phenotype first, which selection then refines and may make constitutive (**genetic assimilation**, [7.5.39](/7.5.39); the role of plasticity in evolution is taken up in [7.10.19](/7.10.19)).

![Reaction norms and the evolution of plasticity. A: linear reaction norms of six hypothetical genotypes in two environments; their different slopes are genotype–environment interaction, and the ranking of genotypes changes between environments. B: evolution of the mean slope of the reaction norm in a quantitative-genetic model in which development responds to a cue correlated (ρ) with the environment of selection; for ρ = 0.9, 0.5 and 0.1 the mean slope approaches the optimum b* = ρB of Eq. (9.9) (dashed lines, B = 1), fluctuating because the environment varies randomly from generation to generation](./plots/reaction-norms.py)

Plasticity also complicates the study of geographic variation: a difference between populations may be plastic, genetic, or both. Common-garden experiments, which raise individuals from different populations in one environment, separate the two (an example is in §10.1 of [7.10.10](/7.10.10)).

## 9.8. The Genetic Architecture of Quantitative Traits

**Definition 9.8.1 (Genetic Architecture)** The **genetic architecture** of a trait is the number of loci that contribute to its variation, the distribution of their effects and allele frequencies, their dominance, epistasis and pleiotropy, and their location in the genome (coding or regulatory sequence, linkage relationships).

Quantitative genetics predicts short-term evolution without knowing the genes, but many questions require the architecture. Are differences between species due to many genes or a few? Is adaptation based on coding or regulatory changes? Do traits respond to new selection quickly from standing variation, or only after new mutations arise? When the same phenotype evolves independently in different species, are the same genes involved? The regions of the genome responsible are located by mapping **quantitative trait loci** in crosses and by genome-wide association within populations ([7.4.25](/7.4.25)); scanning genomes for loci with large differences in allele frequency between populations with different phenotypes has found loci for human adaptations in diet, disease resistance, pigmentation, stature and tolerance of high elevation and cold ([7.10.8](/7.10.8), [7.10.33](/7.10.33)). Mapping crosses are most powerful for large differences between populations or species, as for the tomato QTL *fw2.2*, which changes fruit weight by up to $30\,\%$ ([7.4.25](/7.4.25#sec-25.1.3)); association studies find loci contributing to variation within populations and need much larger samples.

### 9.8.1. How Many Loci?

The number of loci matters for evolution because many loci allow a trait to evolve far before its variation is exhausted (Example 9.1.1), as in the continuing responses of chicken growth and maize oil content. It also matters for medicine: a disease caused by one or two genes, such as hemophilia, can be targeted at those genes, whereas diabetes, heart disease and schizophrenia involve contributions from very many loci, mostly of small effect ([7.4.25](/7.4.25)). The infinitesimal model of §9.5 is the limiting case of very many loci of very small effect.

**Remark 9.8.1 (The Bulmer Effect)** Even under the infinitesimal model, selection changes the additive variance in the short term without changing allele frequencies appreciably: by favoring individuals with particular combinations of alleles at different loci, it creates linkage disequilibrium among them. Directional and stabilizing selection create negative disequilibrium and reduce $V_A$; disruptive selection increases it. Because unlinked loci lose half of their disequilibrium per generation, the variance settles at a new equilibrium within a few generations of constant selection and returns to its original value when selection stops.

### 9.8.2. What Maintains Quantitative Variation?

Nearly all quantitative traits are heritable, even though stabilizing selection, which is common, removes variation. The maintenance of this variation must combine the forces that maintain polymorphism at single loci ([7.10.5](/7.10.5)), and mutation is probably the most important. Mutations at loci affecting a trait under stabilizing selection move individuals away from the optimum and are therefore deleterious, giving a **mutation–selection balance** ([7.4.23](/7.4.23#thm-23.4.1)).

**Formula 9.8.1 (Variance Under Mutation–Stabilizing Selection Balance)** Suppose the trait is affected by $n$ loci, each mutating at rate $\mu$ per gamete to alleles of effect $\pm\alpha$ that are rare and additive, and stabilizing selection around the mean has strength $V_s$. Then at equilibrium

$$
V_A \approx 4n\mu V_s, \tag{9.10}
$$
independently of the effect size $\alpha$ (the "house of cards" approximation, Turelli 1984).

**Proof** In a heterozygote at the optimum the mutant allele shifts the phenotype by $\alpha$ and reduces fitness by $\alpha^2/(2V_s)$ (Eq. (9.6) for small deviations), which acts as the heterozygous selection coefficient $hs = \alpha^2/(2V_s)$. By [Theorem 23.4.1 in 7.4.23](/7.4.23#thm-23.4.1) the equilibrium frequency of such mutants is $q \approx \mu/(hs)$. A rare additive allele of effect $\alpha$ contributes $2q\alpha^2$ to the additive variance, so each locus contributes $2\alpha^2\mu \cdot 2V_s/\alpha^2 = 4\mu V_s$. $\square$

Large-effect mutations are rarer at equilibrium but each contributes more, which is why the effect size cancels. Whether mutation–selection balance can account for the observed variance is still debated: with realistic estimates of $V_s$ it requires many loci or high mutation rates, and much of the variance may be due to alleles that are under purifying selection mainly through their pleiotropic effects on other traits. Balancing selection, spatially and temporally varying selection, and gene flow between differently adapted populations ([7.10.10](/7.10.10)) all contribute as well.

### 9.8.3. Variation Within and Between Species

The loci responsible for standing variation within species may differ from those responsible for differences between species. Many mutations that contribute to quantitative variation have deleterious pleiotropic effects; under long-continued directional selection, such as the evolution of the blue whale from an ancestor the size of a cat, only mutations largely free of such side effects become fixed. So many alleles may contribute to variation within species while relatively few, and different ones, contribute to adaptive differences between species. The kinds of mutations may differ too: all molecular differences among species in flower-color intensity that have been studied are mutations in transcription factors, although these are a minority of the spontaneous mutations within species; and in sticklebacks that recently adapted to fresh water, perhaps $80\,\%$ of the genetic changes are regulatory rather than coding (cis-regulatory evolution is treated in [7.10.19](/7.10.19)).

Convergent phenotypes sometimes have the same genetic basis. Darker and lighter colors have evolved in many mammals, birds and reptiles through changes in the melanocortin-1 receptor gene *Mc1r*, whose product regulates pigment production in hair, feathers and scales; in the snow goose, the jaguar, the striped whiptail lizard and the rock pocket mouse (§10.5 in [7.10.10](/7.10.10)), different amino acid substitutions in the same receptor produce the color polymorphisms. This is **parallel evolution** ([7.10.2](/7.10.2)) at the level of the gene but not of the nucleotide.

Adaptation of a highly polygenic trait need not leave the signature of a selective sweep at any locus. When the optimum shifts, small changes in frequency at very many loci move the mean (polygenic adaptation), and the signal is detectable only by combining the small, coordinated shifts at loci identified by association studies ([7.10.8](/7.10.8)).

## Summary

| Concept | Statement | Reference |
|---|---|---|
| Polygenic potential | Allele-frequency change at many loci moves a trait far beyond its original range | Example 9.1.1 |
| Fitness function | Fitness of individuals as a function of phenotype; with the population's position it determines the mode of selection | Definition 9.2.1, Definition 9.2.2 |
| Gaussian selection | $\bar z^* = (\omega^2\bar z + V_P\theta)/(\omega^2 + V_P)$, $V_P^* = \omega^2V_P/(\omega^2 + V_P)$; $\bar w$ Gaussian of width $V_s = \omega^2 + V_P$ | Formula 9.2.1 |
| Measuring selection | $S = \operatorname{Cov}(w, z)$; $\boldsymbol{\beta} = P^{-1}\boldsymbol{S}$ (direct selection); $\gamma_{ij}$ from quadratic regression | Eq. (9.2), Definition 9.3.1 |
| Response | $\Delta\bar z = h^2S = V_A\beta$; only additive variance counts | Theorem 9.4.1 |
| Rescue | Lag decays by $1 - V_A/V_s$ per generation; critical rate $b_{\mathrm{c}} = V_A\sqrt{2\ln W_0/V_s}$ | Definition 9.4.1, Formula 9.4.1 |
| Artificial selection | Responses continue for long periods: many small loci and new mutations | Definition 9.5.1 |
| Correlated traits | $\Delta\bar{\boldsymbol{z}} = G\boldsymbol{\beta}$; correlated responses can oppose direct selection | Theorem 9.6.1, Definition 9.6.2 |
| Constraint | Little variance along a favored direction; $\boldsymbol{g}_{\max}$ is the line of least resistance | Definition 9.6.3, Definition 9.6.4 |
| Plasticity | Reaction norms evolve; optimal slope $b^* = \rho B$ | Formula 9.7.1 |
| Architecture | Number, effects, frequencies and interactions of loci; Bulmer effect; house of cards $V_A \approx 4n\mu V_s$ | Definition 9.8.1, Remark 9.8.1, Formula 9.8.1 |

The quantitative-genetic view treats evolution as the motion of a population's mean phenotype on an adaptive landscape at a rate set by $G$. Its strength is prediction without genes; its limits lie in the long term, where the variances and covariances themselves evolve and the genetic architecture decides what selection can do.

## Questions

1. Selection acts on a trait with $V_P = 4$ and $h^2 = 0.25$; the survivors' mean exceeds the population mean by $1.2$ units. Compute $\beta$, $V_A$ and the predicted response.

   **Answer** $\beta = S/V_P = 0.3$ per unit, $V_A = h^2V_P = 1$, and $\Delta\bar z = V_A\beta = h^2S = 0.3$ units.

2. Using Formula 9.2.1, show that stabilizing selection centered on the population mean leaves the mean unchanged and reduces the variance by the factor $\omega^2/(\omega^2 + V_P)$. Why does this not reduce the additive variance permanently under the infinitesimal model?

   **Answer** With $\theta = \bar z$, Eq. (9.1) gives $\bar z^* = \bar z$ and $V_P^* = V_P\omega^2/(\omega^2 + V_P)$. Under the infinitesimal model the reduction in additive variance among the selected parents is due to linkage disequilibrium (Remark 9.8.1), not to changed allele frequencies; recombination halves the disequilibrium of unlinked loci every generation, so the variance reaches a modest equilibrium reduction and recovers when selection stops. Only mutation–selection balance or drift determine the long-term variance.

3. In Example 9.6.1, what would the predicted change in leg length be if the genetic covariance were zero? If it were $-0.6\,\mathrm{mm^2}$? Is a covariance of $1.0\,\mathrm{mm^2}$ possible?

   **Answer** With $G_{12} = 0$, $\Delta\bar z_{\mathrm{leg}} = -0.067\,\mathrm{mm}$ (direct response only). With $G_{12} = -0.6$, $\Delta\bar z_{\mathrm{leg}} = -0.067 - 0.072 = -0.139\,\mathrm{mm}$, and the wing response becomes $0.078 + 0.117 = 0.195\,\mathrm{mm}$: here selection on each trait reinforces the response of the other. A covariance of $1.0$ is impossible, because $G$ must be positive semidefinite: $G_{12}^2 \leq G_{11}G_{22} = 0.503$, so $\lvert G_{12}\rvert \leq 0.71\,\mathrm{mm^2}$.

4. In the model of Formula 9.4.1 with $W_0 = 1.2$ and $V_s = 20$ (trait in SD units), what additive variance is needed for a population to persist if the optimum moves by $0.02$ SD per generation? What does this imply for species with long generation times?

   **Answer** $b_{\mathrm{c}} = V_A\sqrt{2\ln 1.2/20} = V_A\sqrt{0.01823} = 0.135V_A$. Persistence requires $0.135V_A \geq 0.02$, i.e. $V_A \geq 0.15$, a heritability of at least about $0.15$. Because the rate is per generation, a given rate of environmental change per year is a larger rate per generation for species with long generations, so long-lived species with low intrinsic growth rates have the lowest critical rates per year.

5. Derive the optimal plasticity of Formula 9.7.1 when development and selection occur in the same environment ($\rho = 1$) and when the cue is uninformative ($\rho = 0$). What phenotype is optimal in the second case?

   **Answer** For $\rho = 1$, $b^* = B$: the reaction norm should match the environmental dependence of the optimum exactly. For $\rho = 0$, $b^* = 0$: the phenotype should not respond to the cue, and the optimal intercept is $a^* = A + B\,\mathbb{E}[e_{\mathrm{s}}]$, the phenotype that is best on average (a canalized, "jack-of-all-trades" phenotype); if fitness depends on variance, bet-hedging strategies may also be favored.
