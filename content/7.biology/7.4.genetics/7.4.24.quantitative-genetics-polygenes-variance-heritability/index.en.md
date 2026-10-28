---
title: "Quantitative Genetics: Polygenes, Variance and Heritability"
description: Continuous variation from Mendelian genes. Quantitative, meristic and threshold traits; the multiple-factor hypothesis (Nilsson-Ehle, East) and the normal limit; estimating the number of loci (extreme classes, Castle–Wright); partitioning phenotypic variance into genetic and environmental parts and broad-sense heritability from inbred lines; genotypic values, average effects, breeding values and the additive and dominance variances; covariances between relatives and the estimation of narrow-sense heritability by parent–offspring regression and twin studies; the breeder's equation, truncation selection and long-term response; liability-threshold traits and recurrence risks; heterosis and inbreeding depression; what heritability does and does not mean.
---

Height, body weight, yield, blood pressure and the risk of most common diseases do not fall into the discrete classes of Mendel's peas. They vary continuously, run in families without clear ratios, and are influenced by environment. In the early twentieth century this seemed to divide the biometricians, who measured correlations between relatives, from the Mendelians, who counted ratios. The division was resolved by the multiple-factor hypothesis (many **genes** of small effect, each inherited in Mendelian fashion, plus environment) and by Fisher's paper of 1918, which derived the correlations between relatives from Mendelian inheritance and founded quantitative genetics. Its method is statistical: instead of **genotypes** we follow means, **variances** and **covariances**, and instead of ratios we estimate how much of the variation is genetic and how much of it a breeder can use.

This chapter develops the classical theory: the polygenic model and its normal limit (an application of the **central limit theorem**, [3.1.13](/3.1.13)), the partition of phenotypic **variance**, the decomposition of genetic values into additive and dominance parts at a single **locus** (which links the theory to the **population genetics** of [7.4.22](/7.4.22)), the resemblance between relatives and the estimation of heritability (by regression, [3.3.2](/3.3.2)), the response to selection, threshold traits, and heterosis. The genes behind quantitative variation are mapped in [7.4.25](/7.4.25). The additive polygenic model in its simplest form, with the **binomial distribution** of the number of "contributing" **alleles** and the extreme classes $(1/4)^n$, was introduced in [7.4.4](/7.4.4) (Definition 4.6.1, Formula 4.6.1); here it is the starting point.

## 24.1. Quantitative Traits and the Multiple-Factor Hypothesis

**Definition 24.1.1 (Quantitative Trait)** A **quantitative trait** is a trait whose **phenotype** is measured on a numerical scale and varies among individuals more or less continuously, so that individuals cannot be sorted into a few discrete classes. Three kinds are distinguished: continuous traits (height, milk yield), meristic traits, which are counts (bristle number, litter size, number of flowers), and threshold traits, which have two or a few phenotypic classes but an underlying continuous liability (§24.6). Traits influenced by many genes and the environment are called complex (multifactorial) traits.

### 24.1.1. Polygenes and the Normal Distribution

In 1909 Herman Nilsson-Ehle crossed wheat lines with red and white grain. Some crosses gave an F₂ with 15 red : 1 white, others 63 red : 1 white, and the red F₂ plants varied in shade from dark to light. He explained the results by two or three genes with additive effects, each "red" allele adding a similar amount of pigment ([7.4.4](/7.4.4)): the F₂ classes then follow $\binom{2n}{k}/4^n$ for $k$ contributing alleles. In 1916 E. M. East showed with corolla length in *Nicotiana longiflora* that the same logic explains truly continuous variation: the parental lines and their F₁ were each uniform genetically and varied only because of the environment, the F₂ was much more variable, and F₃ families raised from short, medium and long F₂ plants had different means (the variation was heritable) and smaller variances than the F₂ (many F₂ plants were already homozygous at some loci).

**Theorem 24.1.1 (Normal Limit of the Polygenic Model)** Let the genotypic value of an individual be the sum of contributions of $n$ unlinked loci, $G = \sum_{j=1}^n g_j$, each with finite variance and none dominating the total, and let the phenotype be $Z = G + E$ with an independent environmental deviation $E$. Then, as $n$ grows, the distribution of $Z$ (after centering and scaling) tends to the **normal distribution**.

**Proof** The $g_j$ are independent **random variables**, because unlinked loci assort independently and, under random mating, alleles at different loci are in **linkage** equilibrium ([7.4.22](/7.4.22), §22.3). Their standardized sum tends to $\mathcal{N}(0, 1)$ by the Lindeberg form of the **central limit theorem** ([3.1.13](/3.1.13)), and adding an independent $E$ (itself usually approximately normal, as the sum of many small influences) preserves the limit. $\square$

In an F₂ of two inbred lines differing at $n$ additive loci of equal effect, $G$ is a linear function of $\mathrm{Bin}(2n, 1/2)$; with environmental noise the Mendelian classes merge into a continuous distribution already for $n = 3$–$5$. The normal shape of a trait is therefore no evidence against Mendelian inheritance; it is what Mendelian inheritance predicts for many loci.

![The logic of East's tobacco experiment, simulated: inbred lines differing at five additive loci (each increasing allele adds 4 mm), environmental SD 3 mm. A: the parental lines and the F₁ are genetically uniform, and their spread is purely environmental; the F₂ is far more variable because the loci segregate (segregation variance V_F2 − V_F1 = n a²/2). B: F₃ families from F₂ plants with 2, 5 and 8 increasing alleles (short, intermediate, long): their means follow the genotypic values of their F₂ parents (the variation is heritable) and each family is less variable than the F₂ as a whole](./plots/segregation-variance.py)

### 24.1.2. How Many Loci?

**Formula 24.1.1 (Estimating the Number of Loci)** For a cross between two inbred lines that differ at $n$ unlinked additive loci of equal effect:

1. *Extreme classes.* The proportion of F₂ individuals as extreme as either parent is $(1/4)^n$ each, so $n \approx \log_4(1/f)$ for an observed proportion $f$ (when classes can be recognized).
2. *Castle–Wright estimator.* With parental means $\bar P_1, \bar P_2$ and the variances of the F₁ and F₂,

$$
n = \frac{(\bar P_1 - \bar P_2)^2}{8\,(V_{F_2} - V_{F_1})}. \tag{24.1}
$$

**Proof** (2) Let each locus contribute $-a$, $0$, $+a$ for 0, 1, 2 increasing alleles. Then $\bar P_1 - \bar P_2 = 2na$. In the F₂ each locus segregates $1 : 2 : 1$, with variance $\tfrac14a^2 + \tfrac12 \cdot 0 + \tfrac14a^2 = a^2/2$; for $n$ independent loci the genetic (segregation) variance is $na^2/2$. The F₁ is genetically uniform, so $V_{F_1} = V_E$ and $V_{F_2} - V_{F_1} = na^2/2$. Dividing, $(2na)^2/(8 \cdot na^2/2) = n$. $\square$

**Example 24.1.1** Two inbred lines have mean ear lengths of $40$ and $20\,\mathrm{cm}$; $V_{F_1} = 4\,\mathrm{cm^2}$ and $V_{F_2} = 14\,\mathrm{cm^2}$. Then $n = 20^2/(8 \cdot 10) = 5$ loci, each with $a = 20/(2 \cdot 5) = 2\,\mathrm{cm}$.

The estimate is a lower bound: unequal effects, linkage in **coupling**, increasing alleles dispersed between the parents (so that the parental difference understates the genetic differences), dominance and **epistasis** all make it smaller than the true number of segregating loci. Genome-wide mapping ([7.4.25](/7.4.25)) shows that for most traits the true number is very large, with a few loci of moderate effect and many of tiny effect.

### 24.1.3. Describing a Quantitative Trait

Qualitative and quantitative traits differ in the questions that can be asked about them, not in the kind of genes involved.

| Feature | Qualitative (Mendelian) trait | Quantitative trait |
|---|---|---|
| variation | discontinuous, a few distinct classes | continuous (or many classes) |
| genes | one or a few genes of large effect | many genes, mostly of small effect |
| environment | small influence on the class | substantial influence on the value |
| description | words (purple, white); ratios of counts | measurements; mean, variance, covariance |
| unit of analysis | individual crosses and **pedigrees** | populations and families, by statistics |
| examples | Mendel's pea traits, ABO blood groups, white eyes in *Drosophila* | height, yield, milk production, blood pressure |

The boundary is not absolute. Wheat kernel color behaves as a qualitative trait in a cross between lines that differ at one locus (3 red : 1 white) and as a quantitative trait in a cross between lines that differ at three (§24.1.1); a trait can be measured on a continuous scale (serum **cholesterol**) and classified clinically into two classes (hypercholesterolemia or not), which is the logic of threshold traits (§24.6); and one gene can contribute both to a discrete trait and, through its dosage, to a continuous one.

The classical multiple-factor hypothesis of Nilsson-Ehle and East, in the form in which it is often taught, stated that a quantitative trait is controlled by many genes (polygenes, or minor genes) whose effects are small, equal and additive, without dominance, sensitive to the environment, and often pleiotropic. The first two claims stand; the others were simplifications that made the model tractable. Mapping has shown that effects are unequal (an approximately **exponential distribution**, with a few loci of moderate effect and very many tiny ones, [7.4.25](/7.4.25)), that dominance and epistasis are common (§24.3, §24.7), and that the same genes can be major genes for rare alleles and minor genes for common ones (*LDLR* in **familial hypercholesterolemia** and in normal variation of cholesterol).

Quantitative traits are described by the statistics of a sample ([3.2](/3.2)).

**Formula 24.1.2 (Sample Statistics of a Trait)** For measurements $x_1, \dots, x_n$,

$$
\bar x = \frac1n\sum_{i=1}^n x_i, \qquad s^2 = \frac{1}{n - 1}\sum_{i=1}^n (x_i - \bar x)^2, \qquad s = \sqrt{s^2}, \qquad \mathrm{SE}(\bar x) = \frac{s}{\sqrt n}, \qquad \mathrm{CV} = \frac{s}{\bar x}.
$$

The **sample variance** $s^2$ (divisor $n - 1$, which makes it unbiased for the population variance) estimates $V_P$; the **standard deviation** $s$ measures the spread of individuals; the **standard error** measures the uncertainty of the mean, and shrinks as $1/\sqrt n$; the coefficient of variation compares variability between traits measured on different scales.

**Example 24.1.2** Ten ears from an inbred maize line measure $12, 14, 15, 15, 16, 16, 17, 18, 18, 19\,\mathrm{cm}$. Then $\bar x = 16.0\,\mathrm{cm}$, $s^2 = 40/9 = 4.44\,\mathrm{cm^2}$, $s = 2.11\,\mathrm{cm}$, $\mathrm{SE} = 0.67\,\mathrm{cm}$ and $\mathrm{CV} = 13\,\%$. Because the line is inbred, $s^2$ estimates the environmental variance $V_E$ (§24.2.2).

## 24.2. Partitioning Phenotypic Variance

### 24.2.1. Genetic and Environmental Variance

**Definition 24.2.1 (Variance Components)** Write the phenotypic value of an individual as $Z = G + E$, where the genotypic value $G$ is the mean phenotype of its genotype over the environments of the population and the environmental deviation $E$ has mean 0. The phenotypic variance $V_P = \operatorname{Var}(Z)$ is then

$$
V_P = V_G + V_E + 2\operatorname{Cov}(G, E) + V_{G\times E}, \tag{24.2}
$$

where $V_G$ is the genetic variance, $V_E$ the environmental variance, and the last two terms describe correlation between genotype and environment and **genotype–environment interaction** (genotypes responding differently to environments: differing **norms of reaction**, [7.4.3](/7.4.3)). In controlled experiments the last two terms are made zero by randomizing genotypes over environments and are otherwise absorbed into $V_G$ or $V_E$. The genetic variance is further decomposed into the additive, dominance and epistatic (interaction) variances, $V_G = V_A + V_D + V_I$ (§24.3).

**Definition 24.2.2 (Broad-Sense Heritability)** The **broad-sense heritability** is the proportion of phenotypic variance that is genetic,

$$
H^2 = \frac{V_G}{V_P}. \tag{24.3}
$$

It measures the extent to which differences in phenotype among individuals of the population are determined by differences in genotype, in the environments in which they were raised.

### 24.2.2. Estimates from Inbred Lines

Genetically uniform groups (an inbred line, an F₁ between two inbred lines, a clone) have $V_G = 0$, so their phenotypic variance estimates $V_E$. Conversely, the variance among the means of different inbred lines raised in a common set of environments estimates $V_G$.

**Example 24.2.1** Ten inbred lines A–J of a plant were grown in three environments and the time to flowering recorded:

| Line | A | B | C | D | E | F | G | H | I | J | Mean |
|---|---|---|---|---|---|---|---|---|---|---|---|
| environment 1 | 62 | 64 | 66 | 66 | 68 | 68 | 70 | 70 | 72 | 74 | 68 |
| environment 2 | 64 | 66 | 68 | 68 | 70 | 70 | 72 | 72 | 74 | 76 | 70 |
| environment 3 | 66 | 68 | 70 | 70 | 72 | 72 | 74 | 74 | 76 | 78 | 72 |
| mean | 64 | 66 | 68 | 68 | 70 | 70 | 72 | 72 | 74 | 76 | 70 |

All 30 values have variance $V_P = 14.67\,\mathrm{d^2}$ (dividing by $n = 30$). The variance among the ten line means is $V_G = (36 + 16 + 4 + 4 + 0 + 0 + 4 + 4 + 16 + 36)/10 = 12\,\mathrm{d^2}$, and the variance among the three environment means is $V_E = 8/3 = 2.67\,\mathrm{d^2}$. Here $V_P = V_G + V_E$ exactly, because every line responds to the environments in the same way (no interaction) and genotypes and environments are balanced (no correlation). Hence $H^2 = 12/14.67 = 0.82$. In a second experiment with the same lines in more variable environments, $V_E$ and hence $V_P$ would be larger and $H^2$ smaller: heritability is a property of a population in a set of environments, not of a trait. (In general the analysis of such a two-way layout is a two-way **analysis of variance**, [3.3.14](/3.3.14), with the genotype × environment interaction estimated from replicates.)

**Formula 24.2.1 (Broad-Sense Heritability from a Cross)** For two inbred parental lines, their F₁ and F₂ grown together,

$$
\hat V_E = \tfrac13\left(V_{P_1} + V_{P_2} + V_{F_1}\right), \qquad \hat V_G = V_{F_2} - \hat V_E, \qquad \hat H^2 = \frac{\hat V_G}{V_{F_2}} \tag{24.4}
$$

(often weighted as $\tfrac14V_{P_1} + \tfrac14V_{P_2} + \tfrac12V_{F_1}$, the proportions of the genotypes in an F₂ at a single locus).

**Example 24.2.2** With $V_{P_1} = 2.0$, $V_{P_2} = 2.4$, $V_{F_1} = 1.9$ and $V_{F_2} = 6.3$ (arbitrary units), $\hat V_E = 2.1$, $\hat V_G = 4.2$, $\hat H^2 = 0.67$ in the F₂.

## 24.3. Gene Action at a Single Locus

### 24.3.1. Genotypic Values

Broad-sense heritability tells how much variation is genetic, but not how much of it is transmitted to offspring: a parent passes on single alleles, not its genotype, so the dominance interaction between the two alleles of a parent is not inherited. To separate the transmissible part we follow Fisher and Falconer and model one locus.

**Definition 24.3.1 (Additive and Dominance Effects)** At a locus with alleles $A_1$ and $A_2$, measure genotypic values from the midpoint between the two **homozygotes**, so that

$$
G(A_1A_1) = -a, \qquad G(A_1A_2) = d, \qquad G(A_2A_2) = +a. \tag{24.5}
$$
The **additive effect** $a$ is half the difference between the homozygotes: the change in genotypic value caused by substituting one $A_2$ for one $A_1$ in the absence of dominance. The **dominance effect** $d$ is the deviation of the **heterozygote** from the midpoint. The ratio $d/a$ measures the degree of dominance: $0$ for no dominance (additive gene action), $1$ for **complete dominance** of $A_2$, between $0$ and $1$ for partial dominance (**incomplete dominance**) and greater than 1 for overdominance.

With allele frequencies $p$ (of $A_2$) and $q$ in Hardy–Weinberg proportions, the population mean is

$$
M = a(p - q) + 2dpq. \tag{24.6}
$$

**Definition 24.3.2 (Average Effect and Breeding Value)** The **average effect** of the allele substitution, $\alpha$, is the slope of the least-squares regression of genotypic value on the number of $A_2$ alleles (0, 1, 2) in the population, weighted by the genotype frequencies:

$$
\alpha = a + d(q - p). \tag{24.7}
$$
The **breeding value** of an individual is the value predicted by this regression, $A = \alpha(k - 2p)$ for an individual with $k$ copies of $A_2$ (deviations from the mean): $-2p\alpha$, $(q - p)\alpha$, $2q\alpha$ for the three genotypes. It equals twice the expected deviation of its offspring from the population mean when it is mated at random; summed over loci, it is what a parent transmits. The residual $D = G - M - A$ is the dominance deviation.

Equation (24.7) follows from the regression slope $\operatorname{Cov}(k, G)/\operatorname{Var}(k)$ with $\operatorname{Var}(k) = 2pq$; it can also be read directly: replacing a random $A_1$ by $A_2$ turns an $A_1A_1$ (probability $q$, its partner allele is $A_1$) into $A_1A_2$, a gain of $a + d$, or an $A_1A_2$ (probability $p$) into $A_2A_2$, a gain of $a - d$; the average gain is $q(a + d) + p(a - d) = a + d(q - p)$. The average effect depends on allele frequencies whenever there is dominance: it is a property of the allele in a population, not of the allele alone.

**Theorem 24.3.1 (Additive and Dominance Variance)** At one locus in Hardy–Weinberg proportions, the genetic variance splits into two uncorrelated parts,

$$
V_G = V_A + V_D, \qquad V_A = 2pq\alpha^2, \qquad V_D = (2pqd)^2. \tag{24.8}
$$

Over many loci in **linkage equilibrium** the additive and dominance variances add; the interaction (epistatic) variance $V_I$ collects the deviations from additivity between loci.

**Proof** The breeding value is the **fitted value** of a least-squares regression, and the dominance deviation is its residual, which is uncorrelated with the fitted values; hence $V_G = \operatorname{Var}(A) + \operatorname{Var}(D)$ (the same decomposition as the regression and residual sums of squares of the **simple linear regression model**, [3.3.4](/3.3.4)). $\operatorname{Var}(A) = \alpha^2\operatorname{Var}(k) = 2pq\alpha^2$. The dominance deviations are $-2q^2d$, $2pqd$, $-2p^2d$ for $A_1A_1$, $A_1A_2$, $A_2A_2$ (direct substitution), and their **mean square** is $q^2 \cdot 4q^4d^2 + 2pq \cdot 4p^2q^2d^2 + p^2 \cdot 4p^4d^2 = 4p^2q^2d^2(q^2 + 2pq + p^2) = (2pqd)^2$. $\square$

![Genotypic values at one locus and their decomposition, for a = 1, d = 0.6 and frequency p = 0.3 of the increasing allele A₂ (Theorem 24.3.1). Large dots: genotypic values, with area proportional to the Hardy–Weinberg genotype frequencies. Blue line: the weighted least-squares regression on the number of A₂ alleles; its slope is the average effect α = a + d(q − p) = 1.24, and its fitted values (small dots) are the breeding values. Dashed: the dominance deviations, the residuals of the regression. V_A is the variance of the fitted values (2pqα²) and V_D that of the residuals ((2pqd)²)](./plots/falconer-regression.py)

**Definition 24.3.3 (Narrow-Sense Heritability)** The **narrow-sense heritability** is the proportion of phenotypic variance due to additive genetic variance (the variance of breeding values),

$$
h^2 = \frac{V_A}{V_P}. \tag{24.9}
$$

It determines the resemblance between parents and offspring and the response to selection (§24.4–24.5), and is the heritability that breeders mean when they speak of "heritability".

**Example 24.3.1 (Dominance Reduces Transmission)** A plant breeder wants more flowers per plant. Flower number is controlled by a locus $B$ with alleles $B_1$ and $B_2$, both at frequency $0.5$, with no environmental variation.

- *Additive gene action.* $B_1B_1$, $B_1B_2$, $B_2B_2$ have 1, 2, 3 flowers; $M = 2$; $a = 1$, $d = 0$, $\alpha = 1$; $V_A = 2 \cdot 0.25 \cdot 1 = 0.5 = V_G$, so $h^2 = H^2 = 1$. Selecting plants with 3 flowers selects $B_2B_2$, whose offspring all have 3 flowers: the parental superiority is fully transmitted.
- *$B_2$ dominant.* The values are 1, 3, 3; $M = 2.5$; $a = 1$, $d = 1$, $\alpha = a + d(q - p) = 1$; $V_A = 0.5$, $V_D = (2 \cdot 0.25 \cdot 1)^2 = 0.25$, $V_G = 0.75$ (check: $0.25 \cdot 1.5^2 + 0.75 \cdot 0.5^2 = 0.75$). So $H^2 = 1$ but $h^2 = 0.5/0.75 = 0.67$. The 3-flowered plants are $B_2B_2$ and $B_1B_2$ in the ratio $1 : 2$; among them $B_2$ has frequency $2/3$, and their randomly mated offspring are $4/9$ $B_2B_2$, $4/9$ $B_1B_2$, $1/9$ $B_1B_1$, with mean $25/9 = 2.78$ flowers, less than the parents' 3. When there is dominance, the phenotype is not fully heritable in the narrow sense.

In plant breeding, $V_A$ is often estimated from the generations of a single cross: the two parental lines, the $\mathrm{F}_1$, the $\mathrm{F}_2$ and the two backcrosses $\mathrm{B}_1 = \mathrm{F}_1 \times \mathrm{P}_1$ and $\mathrm{B}_2 = \mathrm{F}_1 \times \mathrm{P}_2$, all grown together.

**Formula 24.3.1 (Narrow-Sense Heritability from Backcrosses)** If the loci in which the parents differ are unlinked and there is no epistasis or genotype–environment interaction,

$$
V_{F_2} = V_A + V_D + V_E, \qquad V_{B_1} + V_{B_2} = V_A + 2V_D + 2V_E,
$$

where $V_A$ and $V_D$ are the additive and dominance variances of the $\mathrm{F}_2$. Hence

$$
\hat V_A = 2V_{F_2} - (V_{B_1} + V_{B_2}), \qquad \hat h^2 = \frac{2V_{F_2} - V_{B_1} - V_{B_2}}{V_{F_2}} . \tag{24.17}
$$

**Proof** At one locus with values $-a$, $d$, $+a$ (Definition 24.3.1), the $\mathrm{F}_2$ has $p = q = \tfrac12$, so by Theorem 24.3.1 $V_A = 2 \cdot \tfrac14 a^2 = \tfrac12a^2$ and $V_D = (2 \cdot \tfrac14 d)^2 = \tfrac14d^2$. The backcross $\mathrm{B}_1$ consists of $\tfrac12\,A_1A_1$ ($-a$) and $\tfrac12\,A_1A_2$ ($d$), with genetic variance $\tfrac14(a + d)^2$; $\mathrm{B}_2$ has $\tfrac14(a - d)^2$. Their sum is $\tfrac12a^2 + \tfrac12d^2 = V_A + 2V_D$ per locus. Summing over independent loci and adding $V_E$ to each generation gives the two equations, and $2V_{F_2} - (V_{B_1} + V_{B_2}) = V_A$. $\square$

**Example 24.3.2** In a wheat cross the variances of plant height ($\mathrm{cm}^2$) are $V_{P_1} = 9$, $V_{P_2} = 11$, $V_{F_1} = 10$, $V_{F_2} = 40$, $V_{B_1} = 32$ and $V_{B_2} = 30$. Then $\hat V_E = 10$ (Formula 24.2.1), $\hat V_G = 30$, $\hat H^2 = 0.75$; $\hat V_A = 80 - 62 = 18$, $\hat h^2 = 18/40 = 0.45$, and $\hat V_D = 30 - 18 = 12$. Three quarters of the $\mathrm{F}_2$ variance is genetic, but less than half is additive: selection in the early generations of this cross will be less effective than $H^2$ suggests.

## 24.4. Resemblance Between Relatives

### 24.4.1. Covariances

Relatives resemble each other because they share alleles **identical by descent** ([7.4.7](/7.4.7)). For two relatives $X$ and $Y$, let $\theta_{XY}$ be their kinship coefficient (the probability that alleles drawn at random from each at a locus are IBD; the **coefficient of relationship** is $r = 2\theta$) and $\Delta_{XY}$ the probability that both of their alleles at a locus are IBD.

**Formula 24.4.1 (Genetic Covariance Between Relatives)** In a random-mating population without epistasis, and if relatives do not share environments,

$$
\operatorname{Cov}(Z_X, Z_Y) = 2\theta_{XY}V_A + \Delta_{XY}V_D. \tag{24.10}
$$

| Relatives | $2\theta$ | $\Delta$ | Covariance |
|---|---|---|---|
| parent and offspring | $1/2$ | $0$ | $\tfrac12V_A$ |
| full sibs | $1/2$ | $1/4$ | $\tfrac12V_A + \tfrac14V_D$ |
| half sibs, grandparent–grandchild, uncle–nephew | $1/4$ | $0$ | $\tfrac14V_A$ |
| first cousins | $1/8$ | $0$ | $\tfrac18V_A$ |
| monozygotic twins | $1$ | $1$ | $V_A + V_D$ |

**Proof** (parent–offspring) The offspring receives one allele from the parent, so its breeding value is half that of the parent plus contributions independent of the parent (the other parent's half and the Mendelian sampling deviation); its dominance deviation is uncorrelated with the parent's because the two share only one allele. Hence $\operatorname{Cov} = \operatorname{Cov}(A_X, \tfrac12A_X) = \tfrac12V_A$. In general the breeding values of $X$ and $Y$ have covariance $2\theta V_A$ (each shared IBD allele contributes its average effect to both), and the dominance deviations, which depend on both alleles jointly, covary only when both alleles are shared, with probability $\Delta$. $\square$

Shared environments (a common family environment, a common uterus, **maternal effects**) add a covariance $V_{E_c}$ that is the main difficulty of human quantitative genetics: relatives are similar both because they share genes and because they share homes.

### 24.4.2. Estimating Heritability

**Formula 24.4.2 (Parent–Offspring Regression)** By Formula 24.4.1 and the definition of the regression slope,

$$
b_{O\cdot P} = \frac{\operatorname{Cov}(O, P)}{\operatorname{Var}(P)} = \frac{\tfrac12V_A}{V_P} = \frac{h^2}{2}, \qquad b_{O\cdot\bar P} = \frac{\operatorname{Cov}(O, \bar P)}{\operatorname{Var}(\bar P)} = \frac{\tfrac12V_A}{\tfrac12V_P} = h^2, \tag{24.11}
$$

for the regression of offspring on one parent and on the midparent value $\bar P = (P_{\mathrm{m}} + P_{\mathrm{f}})/2$ respectively. The slope is estimated by least squares ([3.3.2](/3.3.2)).

The regression slope is preferred to the correlation because it is unaffected by selection of the parents (only the parental $x$ values are selected) and by differences in variance between generations. Its main pitfall is shared environment and maternal effects, which inflate the slope; animal breeders avoid it by cross-fostering (offspring raised by unrelated foster parents) and by using half-sib families sired by the same male (the paternal half-sib covariance $\tfrac14V_A$ is free of maternal effects).

![Estimating narrow-sense heritability by parent–offspring regression (simulated: 300 families per panel; the parents' breeding values have variance h², environmental deviations variance 1 − h²). A, B: mean of two offspring against the midparent value for h² = 0.3 and 0.8; the least-squares slope estimates h² (Formula 24.4.2). C: the same families for h² = 0.8 against one parent: the slope is h²/2. Dotted: the line of slope 1, which would mean complete resemblance](./plots/parent-offspring.py)

**Definition 24.4.1 (Twin Study)** A **twin study** compares the phenotypic correlations of monozygotic (MZ, identical) twins, who share all their genes, with those of same-sex dizygotic (DZ, fraternal) twins, who share on average half of their segregating alleles, to estimate the contributions of genes and shared environment to the variance of a trait.

**Formula 24.4.3 (Twin Estimates and the ACE Model)** Write the standardized phenotypic variance as $1 = h^2 + c^2 + \mathrm{e}^2$: additive genetic ($A$), common (shared) environment ($C$), unique environment ($E$). If MZ and DZ twins share their environments to the same degree (the equal-environments assumption) and there is no dominance,

$$
r_{\mathrm{MZ}} = h^2 + c^2, \qquad r_{\mathrm{DZ}} = \tfrac12h^2 + c^2, \qquad \text{so} \qquad h^2 = 2(r_{\mathrm{MZ}} - r_{\mathrm{DZ}}), \quad c^2 = 2r_{\mathrm{DZ}} - r_{\mathrm{MZ}}, \quad \mathrm{e}^2 = 1 - r_{\mathrm{MZ}}. \tag{24.12}
$$

The first relation is Falconer's formula. Modern twin analyses fit the ACE (or ADE, with dominance) model to variances and covariances by maximum likelihood.

**Example 24.4.1** For adult height, correlations of about $r_{\mathrm{MZ}} = 0.86$ and $r_{\mathrm{DZ}} = 0.47$ give $h^2 = 2 \cdot 0.39 = 0.78$, $c^2 = 0.94 - 0.86 = 0.08$ and $\mathrm{e}^2 = 0.14$. A negative $c^2$ (when $r_{\mathrm{MZ}} > 2r_{\mathrm{DZ}}$) signals dominance or epistasis.

Twin estimates rest on assumptions: that MZ twins are not treated more alike than DZ twins in ways that matter for the trait, that twins are representative of the population, and that **assortative mating** ([7.4.22](/7.4.22), §22.4.1) is negligible (it raises the DZ correlation and biases $h^2$ downward). MZ twins reared apart, and adoption studies, which compare adopted children with their biological and adoptive parents, offer partial checks; for height, body mass index and many psychiatric traits all designs give substantial heritabilities.

## 24.5. Response to Selection

### 24.5.1. The Breeder's Equation

**Definition 24.5.1 (Selection Differential and Response)** In artificial selection the parents of the next generation are chosen from a population with mean $\mu$. The **selection differential** $S = \mu_S - \mu$ is the difference between the mean of the selected parents and the population mean; the **response to selection** $R = \mu' - \mu$ is the difference between the mean of their offspring and the mean of the parental population.

**Theorem 24.5.1 (Breeder's Equation)** If the regression of offspring on midparent is linear,

$$
R = h^2S. \tag{24.13}
$$

**Proof** The expected phenotype of an offspring given its parents is $\mu + h^2(\bar P - \mu)$ by Formula 24.4.2 (a linear regression through the population means with slope $h^2$). Averaging over the selected pairs, whose midparent values have mean $\mu_S$, gives $\mu' = \mu + h^2(\mu_S - \mu)$. $\square$

The equation is exact for an infinitesimal model (very many loci of small effect, so that selection changes allele frequencies negligibly in one generation and breeding values stay normally distributed); with few loci of large effect it is an approximation. In Example 24.3.1 (dominant $B_2$, $h^2 = 2/3$), selecting the 3-flowered plants gives $S = 3 - 2.5 = 0.5$ and predicts $R = 0.33$, a mean of $2.83$, whereas the exact offspring mean is $2.78$: one generation of strong selection on a single locus changes the **allele frequency** (from $0.5$ to $2/3$) and with it $\alpha$ and $h^2$. Conversely, an observed response defines the *realized heritability* $h^2_{\mathrm{r}} = R/S$, or for several generations the slope of the cumulative response on the cumulative selection differential.

### 24.5.2. Truncation Selection

**Definition 24.5.2 (Truncation Selection and Selection Intensity)** In **truncation selection** all individuals above (or below) a threshold phenotype are selected as parents and the others are discarded. If the trait is normally distributed with phenotypic standard deviation $\sigma_P$ and the proportion $p$ is selected, the selection differential in standard deviation units is the **selection intensity**

$$
i = \frac{S}{\sigma_P} = \frac{\varphi(z)}{p}, \tag{24.14}
$$

where $z$ is the standardized threshold ($p = 1 - \Phi(z)$) and $\varphi$ the standard normal density: $i$ is the mean of a standard normal truncated at $z$.

**Formula 24.5.1 (Response to Truncation Selection)**

$$
R = h^2S = i\,h^2\sigma_P = i\,h\,\sigma_A. \tag{24.15}
$$

Response per year is $i\,h\,\sigma_A/L$ for a generation interval $L$, which is why modern breeding shortens $L$ (genomic selection, [7.4.25](/7.4.25)).

**Example 24.5.1** A breeder keeps the largest $20\,\%$ of the beans as seed. The threshold is $z = 0.842$, $\varphi(z) = 0.280$, so $i = 1.40$. If bean weight has $\sigma_P = 10\,\mathrm{mg}$ and $h^2 = 0.4$, then $S = 14.0\,\mathrm{mg}$ and $R = 5.6\,\mathrm{mg}$ per generation. Selecting the top $5\,\%$ gives $i = 2.06$ and $R = 8.3\,\mathrm{mg}$, at the cost of fewer parents and therefore faster inbreeding and drift.

![Truncation selection and the breeder's equation (standardized phenotypes). A: the top 20 % of the population are selected (threshold z = 0.84); their mean exceeds the population mean by S = iσ_P with selection intensity i = φ(z)/0.2 = 1.40; with h² = 0.4 their offspring have mean R = h²S = 0.56 (dashed). B: the selection intensity as a function of the proportion selected: 0.80 for half, 1.40 for 20 %, 2.06 for 5 % and 2.67 for 1 %](./plots/truncation-selection.py)

### 24.5.3. Long-Term Selection

Over many generations response continues as long as additive variance remains, and populations often go far beyond the range of the base population. In the Illinois long-term selection experiment on maize, started in 1896, more than 100 generations of selection raised the oil content of the kernel from about $5\,\%$ to more than $20\,\%$ in the high line and lowered it to about $1\,\%$ in the low line, with no clear plateau in the high line: far more loci contribute than any small set, and new **mutations** replenish variance. Response eventually slows because favorable alleles approach fixation, because selection on correlated traits (often fitness itself) opposes it, and because small breeding populations lose variance by drift ([7.4.23](/7.4.23)). **Natural selection** on quantitative traits, including stabilizing and disruptive selection and its multivariate form, is treated in 7.10.

## 24.6. Threshold Traits

Many diseases (cleft lip, pyloric stenosis, schizophrenia, **type 1 diabetes**) and some anatomical variants are either present or absent, yet are familial without Mendelian ratios. Falconer (1965) and Carter interpreted them by an underlying continuous variable.

**Definition 24.6.1 (Liability and Threshold Trait)** A **threshold trait** is a trait with discrete phenotypic classes (usually affected and unaffected) determined by an underlying continuous variable, the **liability**, which is the sum of many genetic and environmental contributions and is therefore normally distributed; individuals whose liability exceeds a threshold are affected. The heritability of liability is defined on this continuous scale.

If the population prevalence is $K$, the threshold on the standardized liability scale is $t = \Phi^{-1}(1 - K)$, and the mean liability of affected individuals is $\mu_{\mathrm{aff}} = \varphi(t)/K$. Relatives of affected people have a higher mean liability, so a larger fraction of them lies above the same threshold.

**Formula 24.6.1 (Falconer's Method)** If the prevalence in the population is $K$ and among relatives of affected individuals (of **coefficient of relationship** $r$) it is $K_R$, with thresholds $t = \Phi^{-1}(1 - K)$ and $t_R = \Phi^{-1}(1 - K_R)$, then the regression of relatives' liability on that of the affected is approximately

$$
b = \frac{t - t_R}{\mu_{\mathrm{aff}}}, \qquad h^2 \approx \frac{b}{r}. \tag{24.16}
$$

**Example 24.6.1** A disease has prevalence $K = 1\,\%$ and occurs in $5\,\%$ of the sibs of patients. Then $t = 2.326$, $t_R = 1.645$, $\mu_{\mathrm{aff}} = \varphi(2.326)/0.01 = 2.665$, $b = 0.681/2.665 = 0.256$, and $h^2 \approx 0.256/0.5 = 0.51$. The exact bivariate-normal model with $h^2 = 0.51$ gives a sib risk of $4.5\,\%$, so Falconer's approximation slightly underestimates $h^2$; modern analyses fit the bivariate normal model directly.

The model makes characteristic predictions: the recurrence risk is higher when the **proband** is more severely affected or when two relatives are already affected; it is higher for relatives of the less often affected sex (Carter effect: in pyloric stenosis, five times more common in boys, the relatives of affected girls have the higher risk, because girls need a greater liability); and it falls much faster than by half with each degree of relationship, because only the tail of the liability distribution counts.

![The liability-threshold model of a disease with prevalence K = 1 % (Definition 24.6.1). A: liability is standard normal in the population, and individuals above the threshold t = 2.33 are affected; the liability of first-degree relatives of affected individuals (h² = 0.5, normal approximation) is shifted to the right, so that 4.4 % of them exceed the threshold (exact bivariate-normal calculation). B: relative recurrence risk λ (risk to relatives divided by K) for monozygotic twins and first-, second- and third-degree relatives, for heritabilities of liability 0.5 and 0.8, against the halving with each degree expected for a rare dominant gene: under the threshold model the risk drops steeply with relatedness](./plots/liability-threshold.py)

## 24.7. Heterosis and Inbreeding Depression

**Definition 24.7.1 (Heterosis and Inbreeding Depression)** **Inbreeding depression** is the reduction of the mean of a trait, usually a component of fitness (viability, fertility, yield), in the offspring of related individuals. **Heterosis** (hybrid vigor) is the superiority of the F₁ of a cross between two lines or populations over the mean of the parents (mid-parent heterosis) or over the better parent.

**Theorem 24.7.1 (Means Under Inbreeding and Crossing)** At loci with dominance effects $d_j$ and allele frequencies $p_j$, $q_j$:

1. a population with **inbreeding coefficient** $F$ has mean $M_F = M_0 - 2F\sum_j p_jq_jd_j$, linear in $F$;
2. the F₁ of two populations whose allele frequencies differ by $y_j$ at each locus exceeds the mean of the two parental populations by $H_{F_1} = \sum_j d_jy_j^2$; for two inbred lines fixed for different alleles at $k$ loci, $H_{F_1} = \sum_{j=1}^k d_j$.

**Proof** (1) By Formula 22.4.1 ([7.4.22](/7.4.22)), inbreeding moves a fraction $F$ of heterozygotes, $2pqF$, into the two homozygous classes in equal numbers; each moved individual changes from $d$ to $\pm a$, an average change of $-d$; hence $\Delta M = -2pqdF$ per locus. (2) For populations with frequencies $p$ and $p - y$, compute the F₁ mean $a(p_1 + p_2 - 1) + d[p_1q_2 + p_2q_1]$ and subtract the mean of the parental means from Eq. (24.6); the additive terms cancel and the dominance terms leave $dy^2$. $\square$

Both phenomena therefore require directional dominance, $d > 0$ on average for the trait: alleles that increase fitness tend to be dominant, which is what the mutation–selection theory of [7.4.23](/7.4.23) predicts, because deleterious mutations are kept rare and partially recessive. The dominance hypothesis (Davenport, Bruce, Jones) explains heterosis by the masking in hybrids of different deleterious recessive alleles carried by each inbred line; the overdominance hypothesis (East, Shull) by heterozygote superiority at individual loci. A third view, the epistasis hypothesis, attributes part of heterosis to favorable interactions between alleles at different loci brought together in the hybrid; the three are not exclusive, and heterosis for a complex trait such as yield combines all of them. The data favor mostly dominance, with apparent overdominance often caused by linked dominant alleles in **repulsion** (pseudo-overdominance). Hybrid maize, developed from Shull's experiments (1908), roughly doubled yields in the twentieth century with improved management; hybrid rice exploits **cytoplasmic male sterility** ([7.4.11](/7.4.11)) to produce F₁ seed. Inbreeding depression is the reason why **consanguinity** raises disease risk ([7.4.7](/7.4.7)) and why small conservation populations decline ([7.4.23](/7.4.23)).

**Example 24.7.1** Suppose yield is influenced by 100 loci, each with $d = 0.5\,\mathrm{g}$ and $pq = 0.16$. Full-sib mating ($F = 0.25$) reduces the mean by $2 \cdot 0.25 \cdot 100 \cdot 0.16 \cdot 0.5 = 4\,\mathrm{g}$. Two inbred lines fixed for different alleles at 40 of these loci produce an F₁ exceeding their mid-parent value by $40 \cdot 0.5 = 20\,\mathrm{g}$.

**Remark 24.7.1 (Heterosis Declines in the F₂)** For two inbred lines fixed for different alleles, the $\mathrm{F}_1$ is heterozygous at every such locus and the $\mathrm{F}_2$ only at half of them, so the $\mathrm{F}_2$ mean is $\bar P + \tfrac12\sum d_j$: half of the heterosis is lost in one generation of self-fertilization or intercrossing of the $\mathrm{F}_1$. Further self-fertilization halves it again in each generation, whereas random mating within the $\mathrm{F}_2$ population keeps it at one half, because the heterozygote frequency stays at the Hardy–Weinberg value $2pq = \tfrac12$ ([7.4.22](/7.4.22)). This is why hybrid seed must be produced anew for every crop, and why the systems that make large-scale crossing possible (cytoplasmic male sterility with restorer lines, and environment-sensitive **genic male sterility**, [7.4.11](/7.4.11)) are central to hybrid breeding.

## 24.8. What Heritability Means

Heritability is among the most misunderstood quantities in biology. Its definition, a ratio of variances in a population, implies several limits.

- It belongs to a population in an environment. Heritability changes whenever genetic or environmental variance changes (Example 24.2.1): it is higher in a uniform environment and lower in a variable one, and it can differ between populations, ages and cohorts.
- It says nothing about individuals. A heritability of $0.8$ for height does not mean that $80\,\%$ of a person's height is due to genes; genes and environment both are necessary for every individual's phenotype, and their contributions to a single value cannot be separated.
- It does not explain differences between groups. In Lewontin's thought experiment, seeds from one genetically variable sack are sown in two fields, one fertilized and one not: within each field differences in height are entirely genetic ($H^2 = 1$), yet the difference between the fields is entirely environmental. A high within-group heritability is compatible with any cause of between-group differences.
- High heritability does not mean that a trait cannot be changed. **Phenylketonuria** is a single-gene disease, yet a low-phenylalanine diet prevents its effects; mean human height has risen by about $10\,\mathrm{cm}$ in many countries over a century of improving nutrition, while its heritability remained high. Heritability measures the sources of variation in present conditions, not the effects of new interventions.
- Fitness traits have low heritabilities (often $0.1$ or less for fertility and viability), not because they are unaffected by genes, but because selection uses up their additive variance while their environmental and dominance variances remain.

Breeders call heritabilities above about $0.5$ high, $0.2$–$0.5$ medium and below $0.2$ low. Approximate narrow-sense estimates illustrate the pattern (values vary between populations and studies):

| Organism | Trait | $h^2$ |
|---|---|---|
| human | adult height | $0.7$–$0.8$ |
| human | total fingerprint ridge count | $0.9$ |
| human | body mass index | $0.4$–$0.7$ |
| cattle | milk yield | $0.3$ |
| cattle | conception rate | $< 0.05$ |
| pig | back-fat thickness | $0.5$–$0.7$ |
| pig | litter size | $0.1$ |
| chicken | egg weight | $0.5$ |
| chicken | egg production | $0.1$–$0.3$ |
| *Drosophila melanogaster* | abdominal bristle number | $0.5$ |
| *Drosophila melanogaster* | egg production | $0.2$ |

Morphological traits tend to have high heritabilities and traits closely tied to fitness low ones, for the reason just given. Selection is most effective for the former; for the latter, breeders rely on crossing (heterosis), on reducing environmental variance by uniform management, and on selection of relatives (family and genomic selection).

Human height is the reference case: $h^2 \approx 0.8$ from twin and family studies in well-fed populations, a phenotype affected by thousands of loci, whose molecular dissection by association studies is the subject of [7.4.25](/7.4.25).

## Summary

| Topic | Key relations |
|---|---|
| polygenic model | $G = \sum g_j$, normal limit (Theorem 24.1.1); extreme F₂ classes $(1/4)^n$; Castle–Wright $n = (\bar P_1 - \bar P_2)^2/8(V_{F_2} - V_{F_1})$ (Formula 24.1.1), a lower bound |
| description (§24.1.3) | qualitative versus quantitative traits; $\bar x$, $s^2$ (divisor $n - 1$), $\mathrm{SE} = s/\sqrt n$, CV (Formula 24.1.2) |
| variance partition | $V_P = V_G + V_E\,(+2\operatorname{Cov} + V_{G\times E})$, $V_G = V_A + V_D + V_I$ (Definition 24.2.1); $H^2 = V_G/V_P$; $V_E$ from inbred lines and F₁ (Formula 24.2.1) |
| one locus | values $-a, d, +a$; $M = a(p - q) + 2dpq$; $\alpha = a + d(q - p)$; $V_A = 2pq\alpha^2$, $V_D = (2pqd)^2$ (Theorem 24.3.1); $h^2 = V_A/V_P$; from backcrosses $\hat h^2 = (2V_{F_2} - V_{B_1} - V_{B_2})/V_{F_2}$ (Formula 24.3.1) |
| relatives | $\operatorname{Cov} = 2\theta V_A + \Delta V_D$: PO $\tfrac12V_A$, FS $\tfrac12V_A + \tfrac14V_D$, HS $\tfrac14V_A$, MZ $V_A + V_D$ (Formula 24.4.1) |
| estimation | $b_{O\cdot P} = h^2/2$, $b_{O\cdot\bar P} = h^2$ (Formula 24.4.2); twins $h^2 = 2(r_{\mathrm{MZ}} - r_{\mathrm{DZ}})$, $c^2 = 2r_{\mathrm{DZ}} - r_{\mathrm{MZ}}$ (Formula 24.4.3) |
| selection | $R = h^2S$ (Theorem 24.5.1); $i = \varphi(z)/p$, $R = ih^2\sigma_P$ (Formula 24.5.1); realized $h^2 = R/S$ |
| threshold traits | $t = \Phi^{-1}(1 - K)$, $\mu_{\mathrm{aff}} = \varphi(t)/K$, $h^2 \approx (t - t_R)/(r\mu_{\mathrm{aff}})$ (Formula 24.6.1); risk falls steeply with relatedness |
| inbreeding / crossing | $M_F = M_0 - 2F\sum pqd$; $H_{F_1} = \sum dy^2$ (Theorem 24.7.1); requires directional dominance; $\mathrm{F}_2$ keeps half the heterosis (Remark 24.7.1) |

Heritability is population- and environment-specific, describes variation and not individuals, does not explain group differences, and does not imply immutability (§24.8).

## Questions

1. In a cross between two inbred lines of a plant, $1/256$ of the F₂ plants are as short as the short parent. (a) How many additive loci of equal effect are implied? (b) How many phenotypic classes would the F₂ show without environmental variation? (c) What fraction of the F₂ would be exactly intermediate?

   **Answer** (a) $(1/4)^n = 1/256$ gives $n = 4$. (b) $2n + 1 = 9$ classes (0 to 8 increasing alleles). (c) $\binom{8}{4}/4^4 = 70/256 = 0.273$.

2. Two inbred lines have mean body weights $12$ and $24\,\mathrm{g}$; $V_{F_1} = 2.5\,\mathrm{g^2}$ and $V_{F_2} = 5.5\,\mathrm{g^2}$. (a) Estimate the number of loci by Castle–Wright. (b) Estimate the broad-sense heritability in the F₂, using $V_{F_1}$ for $V_E$. (c) Why may the true number of loci be much larger?

   **Answer** (a) $n = 144/(8 \cdot 3) = 6$. (b) $\hat V_G = 3.0$, $\hat H^2 = 3.0/5.5 = 0.55$. (c) The formula assumes equal effects, no linkage, no dominance and all increasing alleles in one parent; unequal effects, linkage in coupling and dispersed alleles all reduce the estimate.

3. For Example 24.2.1, (a) verify $V_P$ from the table; (b) what would $H^2$ be if the same lines were grown in environments whose means were 62, 70 and 78 (with the same line differences)?

   **Answer** (a) Each value is line mean + environment deviation ($-2$, 0, $+2$); deviations from 70 are sums of independent line and environment parts, so $V_P = 12 + 8/3 = 14.67$. (b) $V_E = (64 + 0 + 64)/3 = 42.67$, $V_P = 54.67$, $H^2 = 12/54.67 = 0.22$.

4. At a locus, $A_2A_2$ has value 20, $A_1A_2$ 18 and $A_1A_1$ 10, and $p(A_2) = 0.6$. Compute $a$, $d$, the population mean, $\alpha$, $V_A$, $V_D$ and $V_G$, and check $V_G$ directly.

   **Answer** Midpoint 15, $a = 5$, $d = 3$. $M = 15 + 5(0.6 - 0.4) + 2 \cdot 3 \cdot 0.24 = 17.44$. $\alpha = 5 + 3(0.4 - 0.6) = 4.4$. $V_A = 2 \cdot 0.24 \cdot 4.4^2 = 9.293$; $V_D = (2 \cdot 0.24 \cdot 3)^2 = 2.074$; $V_G = 11.366$. Directly: $0.36(20 - 17.44)^2 + 0.48(18 - 17.44)^2 + 0.16(10 - 17.44)^2 = 2.359 + 0.151 + 8.856 = 11.366$.

5. In Question 4, what are the breeding values of the three genotypes? What would the mean of the offspring of an $A_2A_2$ parent mated at random be?

   **Answer** $A(A_2A_2) = 2q\alpha = 3.52$, $A(A_1A_2) = (q - p)\alpha = -0.88$, $A(A_1A_1) = -2p\alpha = -5.28$ (they average to zero). Offspring of $A_2A_2$: $M + \tfrac12 \cdot 3.52 = 19.20$. Check: the offspring are $A_2A_2$ with probability $0.6$ and $A_1A_2$ with $0.4$: $0.6 \cdot 20 + 0.4 \cdot 18 = 19.2$.

6. The slope of the regression of offspring on mother for egg weight in a poultry flock is $0.28$; the slope on midparent (the sire's breeding value estimated from his sisters) is $0.50$. Estimate $h^2$ from each. Why might they differ?

   **Answer** From one parent $h^2 = 2 \cdot 0.28 = 0.56$; from midparent $h^2 = 0.50$. The dam regression includes maternal effects (egg environment, cytoplasm, shared rearing), which inflate the one-parent estimate; estimates also have sampling error.

7. For a trait, $r_{\mathrm{MZ}} = 0.74$ and $r_{\mathrm{DZ}} = 0.46$. Estimate $h^2$, $c^2$ and $\mathrm{e}^2$. What would $r_{\mathrm{MZ}} = 0.6$, $r_{\mathrm{DZ}} = 0.2$ suggest?

   **Answer** $h^2 = 2 \cdot 0.28 = 0.56$, $c^2 = 0.92 - 0.74 = 0.18$, $\mathrm{e}^2 = 0.26$. In the second case $c^2 = 0.4 - 0.6 = -0.2 < 0$: the DZ correlation is less than half the MZ correlation, which suggests nonadditive genetic variance (dominance or epistasis, $\Delta = 1/4$ for DZ twins but 1 for MZ twins) or MZ-specific environmental similarity; an ADE model is appropriate.

8. Pigs in a herd have mean back-fat thickness $30\,\mathrm{mm}$ with $\sigma_P = 5\,\mathrm{mm}$; $h^2 = 0.45$. The breeder selects the leanest $10\,\%$ of boars and sows as parents. Predict the mean of the next generation. What is the realized heritability if the observed mean is $27.5\,\mathrm{mm}$?

   **Answer** $p = 0.1$: $z = 1.282$, $i = \varphi(1.282)/0.1 = 0.1755/0.1 = 1.755$. $S = -1.755 \cdot 5 = -8.77\,\mathrm{mm}$, $R = 0.45 \cdot (-8.77) = -3.95$: predicted mean $26.05\,\mathrm{mm}$. Realized $h^2 = -2.5/-8.77 = 0.29$.

9. A breeder can select either the top $50\,\%$ every year (generation interval 1 year) or the top $5\,\%$ with a generation interval of 2 years. Which gives the faster response per year, other things equal?

   **Answer** Response per year is $ih\sigma_A/L$. $i(0.5) = 0.798$, per year $0.798$; $i(0.05) = 2.063$, per year $1.031$. The second is faster by $29\,\%$ (though it uses fewer parents, which increases inbreeding).

10. A congenital malformation has a population prevalence of $0.1\,\%$ and a recurrence risk of $2\,\%$ among sibs. Estimate the heritability of liability by Falconer's method.

    **Answer** $t = \Phi^{-1}(0.999) = 3.090$, $t_R = \Phi^{-1}(0.98) = 2.054$, $\mu_{\mathrm{aff}} = \varphi(3.090)/0.001 = 3.367$. $b = 1.036/3.367 = 0.308$; $h^2 \approx 0.308/0.5 = 0.62$.

11. Pyloric stenosis is about five times as common in boys as in girls. Under the threshold model, which children of affected parents are at the highest risk, and why?

    **Answer** Girls need a higher liability to be affected (their threshold is higher). An affected mother therefore has a higher mean liability than an affected father and transmits more liability to her children; and sons, with the lower threshold, are more often affected. The highest risk is for the sons of affected mothers (Carter effect), observed at about $20\,\%$, versus about $5\,\%$ for the sons of affected fathers.

12. Show that one locus contributes to heterosis $dy^2$, using two populations fixed for opposite alleles ($y = 1$) and populations with frequencies $0.8$ and $0.3$ ($a = 2$, $d = 1$).

    **Answer** Fixed lines: means $+a$ and $-a$, mid-parent 0; F₁ all heterozygous, value $d$; heterosis $d \cdot 1^2 = d$. With $p_1 = 0.8$, $p_2 = 0.3$: parental means $M_1 = 2(0.6) + 2 \cdot 0.16 = 1.52$, $M_2 = 2(-0.4) + 2 \cdot 0.21 = -0.38$, mid-parent $0.57$. F₁: $A_2A_2$ $0.24$, $A_1A_2$ $0.8 \cdot 0.7 + 0.2 \cdot 0.3 = 0.62$, $A_1A_1$ $0.14$; mean $0.24 \cdot 2 + 0.62 \cdot 1 - 0.14 \cdot 2 = 0.82$. Heterosis $0.25 = d y^2 = 1 \cdot 0.5^2$.

13. Why does selection on a trait with high broad-sense but low narrow-sense heritability give little response? Give a breeding strategy for such a trait.

    **Answer** Response depends on $V_A$ (Theorem 24.5.1), the part of genetic variance transmitted by single alleles; dominance and epistatic variance are reassembled anew in each generation and not transmitted. For such traits (yield in maize) breeders exploit nonadditive variance by producing F₁ hybrids between complementary inbred lines (heterosis), or propagate superior genotypes clonally (potatoes, fruit trees), which transmits the whole genotype.

14. (Open question.) The heritability of a test score is $0.6$ within each of two groups, and their means differ by one standard deviation. Explain why it does not follow that the difference between the groups is genetic, and what kind of evidence could address the question.

    **Answer** Heritability describes the sources of variation within each group under its conditions; it is silent about the causes of the difference between groups, which may be entirely environmental (Lewontin's two fields, §24.8). Evidence about group differences must come from designs that vary the cause directly: changes in group differences over time or across environments (for test scores, large secular gains in a few decades), adoption across groups, comparison of environmental exposures, and genetic methods that test whether allele frequencies at associated loci differ in the predicted direction, which are themselves confounded by environment and by the poor portability of **polygenic scores** between populations ([7.4.25](/7.4.25)).

15. The heights (cm) of ten plants of an $\mathrm{F}_1$ are $20, 22, 23, 25, 25, 26, 27, 28, 30, 34$. Compute the mean, the sample variance, the standard deviation, the standard error of the mean and the coefficient of variation. Which of these estimates $V_E$?

    **Answer** $\bar x = 260/10 = 26.0$; $\sum(x_i - \bar x)^2 = 36 + 16 + 9 + 1 + 1 + 0 + 1 + 4 + 16 + 64 = 148$, so $s^2 = 148/9 = 16.4\,\mathrm{cm^2}$, $s = 4.06\,\mathrm{cm}$, $\mathrm{SE} = 4.06/\sqrt{10} = 1.28\,\mathrm{cm}$, $\mathrm{CV} = 15.6\,\%$. The $\mathrm{F}_1$ of two inbred lines is genetically uniform, so $s^2$ estimates $V_E$.
16. For a cross of two inbred lines, the variances of grain weight are $V_{P_1} = 3.2$, $V_{P_2} = 2.8$, $V_{F_1} = 3.0$, $V_{F_2} = 12.0$, $V_{B_1} = 9.0$ and $V_{B_2} = 8.4$. Estimate $H^2$ and $h^2$ in the $\mathrm{F}_2$, and $V_D$. Classify the heritability.

    **Answer** $\hat V_E = (3.2 + 2.8 + 3.0)/3 = 3.0$, $\hat V_G = 9.0$, $\hat H^2 = 0.75$. $\hat V_A = 2 \times 12.0 - 17.4 = 6.6$ (Formula 24.3.1), $\hat h^2 = 6.6/12 = 0.55$, high by the breeders' convention. $\hat V_D = 9.0 - 6.6 = 2.4$. Check: $V_{B_1} + V_{B_2}$ should be $V_A + 2V_D + 2V_E = 6.6 + 4.8 + 6.0 = 17.4$, as observed (the check is not independent: three equations, three unknowns).
17. Two inbred maize lines yield $6.0$ and $5.0\,\mathrm{t\,ha^{-1}}$ and their $\mathrm{F}_1$ $9.0\,\mathrm{t\,ha^{-1}}$. Assuming that heterosis is due to dominance at loci where the lines are fixed for different alleles, predict the mean yield of the $\mathrm{F}_2$ and of the $\mathrm{F}_3$ obtained by self-fertilization. Why do farmers buy new hybrid seed every year?

    **Answer** Mid-parent $5.5$; $\mathrm{F}_1$ heterosis $3.5$. The $\mathrm{F}_2$ keeps half of it: $5.5 + 1.75 = 7.25$; the selfed $\mathrm{F}_3$ a quarter: $5.5 + 0.875 = 6.375\,\mathrm{t\,ha^{-1}}$ (Remark 24.7.1). Seed saved from a hybrid crop is an $\mathrm{F}_2$, which yields less and is variable, because the **heterozygosity** of the $\mathrm{F}_1$ is lost by segregation.
18. In the wheat cross of Example 24.3.2, the breeder selects the tallest 20 % of the $\mathrm{F}_2$ plants and intercrosses them at random. Predict the response, and explain why the prediction based on $H^2$ would be too optimistic.

    **Answer** $\sigma_P = \sqrt{40} = 6.32\,\mathrm{cm}$, $i = 1.40$ for $p = 0.2$ (Example 24.5.1), $S = 8.85\,\mathrm{cm}$. $R = h^2 S = 0.45 \times 8.85 = 4.0\,\mathrm{cm}$. Using $H^2 = 0.75$ would predict $6.6\,\mathrm{cm}$, but the dominance part of the genetic superiority of the selected plants is not transmitted by their gametes (Example 24.3.1).
