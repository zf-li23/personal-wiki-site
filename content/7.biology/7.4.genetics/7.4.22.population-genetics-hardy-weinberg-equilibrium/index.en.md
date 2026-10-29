---
title: "Population Genetics I: Hardy–Weinberg Equilibrium and Mating Systems"
description: "Genetics of populations rather than of crosses. Gene pools, allele and genotype frequencies and their estimation; the Hardy–Weinberg law, its proof and its tests; rare recessive alleles and carriers, multiple alleles (ABO by gene counting and the EM algorithm) and X-linked loci; haplotypes, linkage disequilibrium (D, D′, r²) and its decay; assortative mating, inbreeding and regular inbreeding systems; population subdivision, the Wahlund effect and F_ST; random match probabilities and paternity indices in forensic genetics."
---

Mendel's laws describe what happens in a controlled cross between parents of known **genotype** ([7.4.2](/7.4.2)); human **pedigrees** apply them to one family at a time ([7.4.7](/7.4.7)). Most questions about heredity, however, concern whole populations, in which matings are not arranged, parents' genotypes are unknown, and not every individual leaves offspring: How common is a disease **allele**, and how many people carry it unawares? Why does a dominant **phenotype** not spread to fixation? How much does marriage between relatives raise the risk of recessive disease in a population? How unlikely is it that two people share a DNA profile by chance? Population genetics answers these by treating the population as a pool of **genes**, Mendelian transmission as random sampling from that pool, and inheritance as a dynamical system on allele and genotype frequencies.

This chapter treats the population in which nothing changes the allele frequencies: large, randomly mating, free of **mutation**, migration and selection. Its central result, the Hardy–Weinberg law, is the null model of the subject, in the same way that a constant velocity is the null model of mechanics: once we know what an "ideal" population does, every departure from it measures a force. We then extend the law to several alleles, to the X **chromosome** and to two linked loci (**linkage** disequilibrium, the basis of **association mapping** in [7.4.25](/7.4.25)), and relax random mating (assortative mating, inbreeding, subdivision). The forces that do change allele frequencies (mutation, migration, selection and drift) follow in [7.4.23](/7.4.23); the inheritance of continuous traits in populations in [7.4.24](/7.4.24). The probability tools are those of the **binomial distribution** and the **multinomial distribution** ([3.1.4](/3.1.4), [3.1.6](/3.1.6)), the χ² test ([3.2.6](/3.2.6#sec-6.3)) and the **inbreeding coefficient** of [7.4.7](/7.4.7).

## 22.1. Populations, Gene Pools and Frequencies

**Definition 22.1.1 (Population Genetics and Gene Pool)** **Population genetics** is the study of the genetic composition of populations: the distribution of alleles and genotypes, and of the phenotypes they produce, and the processes that change them in space and time. A population (in the genetic sense) is a group of individuals of one species that live in the same place at the same time and, if the species reproduces sexually, can mate with one another. Its **gene pool** is the set of all gene copies at a **locus** (or in the **genome**) carried by its breeding members; for an autosomal locus in $N$ **diploid** individuals it has $2N$ copies.

Populations are rarely counted completely; we observe a sample of $n$ individuals and infer the frequencies of the population from it.

**Definition 22.1.2 (Genotype and Allele Frequencies)** At an autosomal **locus** with alleles $A$ and $a$, let a sample of $n$ individuals contain $n_{AA}$, $n_{Aa}$, $n_{aa}$ individuals of the three **genotypes**. The **genotype frequencies** are the proportions $P = n_{AA}/n$, $H = n_{Aa}/n$, $Q = n_{aa}/n$ ($P + H + Q = 1$). The **allele frequency** of an **allele** is the proportion of gene copies in the gene pool that are of that type:

$$
p = \frac{2n_{AA} + n_{Aa}}{2n} = P + \tfrac12 H, \qquad q = \frac{2n_{aa} + n_{Aa}}{2n} = Q + \tfrac12 H, \qquad p + q = 1.
$$

Genotype frequencies determine allele frequencies, but not conversely: the populations $(P, H, Q) = (0.5, 0, 0.5)$ and $(0.25, 0.5, 0.25)$ both have $p = 1/2$. With **codominance** (MN blood groups, DNA markers) genotypes are counted directly; with dominance the classes $AA$ and $Aa$ look alike, and allele frequencies can be estimated only with a model of how genotypes arise, which is the Hardy–Weinberg law of the next section.

**Formula 22.1.1 (Sampling Error of an Allele Frequency)** If the $2n$ gene copies of the sample are drawn independently from a pool with frequency $p$ (which holds under Hardy–Weinberg proportions), the number of $A$ copies is binomial, $2n\hat p \sim \mathrm{Bin}(2n, p)$, so $\hat p$ is unbiased with **standard error**

$$
\operatorname{SE}(\hat p) = \sqrt{\frac{p(1-p)}{2n}}. \tag{22.1}
$$

Without Hardy–Weinberg proportions the two copies in one individual are not independent and $\operatorname{Var}(\hat p) = p(1-p)(1 + F)/(2n)$, where $F$ is the inbreeding coefficient of §22.4.

**Example 22.1.1** A sample of $n = 1000$ people typed for the MN blood group contains 298 $MM$, 489 $MN$ and 213 $NN$. The genotype frequencies are $0.298$, $0.489$, $0.213$; the allele frequency of $M$ is $p = (2 \cdot 298 + 489)/2000 = 1085/2000 = 0.5425$, and $q = 0.4575$. By Eq. (22.1), $\operatorname{SE}(\hat p) = \sqrt{0.5425 \cdot 0.4575/2000} = 0.011$.

At an **X-linked** locus males are **hemizygous**: each man carries one gene copy and each woman two, so in a sample of $m$ men and $f$ women the gene pool has $m + 2f$ copies, and the allele frequency is (number of copies in men + number in women)$/(m + 2f)$.

## 22.2. The Hardy–Weinberg Law

### 22.2.1. Assumptions and Proof

At the beginning of the twentieth century some biologists argued that a dominant allele, such as the one for brachydactyly, should increase until three quarters of the population showed the dominant phenotype, and that recessive traits such as blond hair would gradually disappear. In 1908 the mathematician G. H. Hardy and, independently, the physician Wilhelm Weinberg showed that Mendelian inheritance by itself does not change allele frequencies at all.

**Definition 22.2.1 (Hardy–Weinberg Equilibrium)** A population is in **Hardy–Weinberg equilibrium** (HWE) at a locus if its genotype frequencies equal the products of the allele frequencies, $P = p^2$, $H = 2pq$, $Q = q^2$ (more generally, $p_i^2$ for $A_iA_i$ and $2p_ip_j$ for $A_iA_j$); these are the Hardy–Weinberg proportions.

The law holds under the following idealized assumptions about the population and the locus:

1. the organism is diploid and reproduces sexually, and generations do not overlap;
2. the population is very large (in the model, infinite), so that frequencies do not fluctuate by chance;
3. mating is random with respect to the genotype at the locus;
4. there is no mutation;
5. there is no migration into or out of the population;
6. genotypes do not differ in viability or fertility (no selection), and segregation is Mendelian (no **meiotic drive**);
7. allele frequencies are the same in males and females (for an autosomal locus).

**Theorem 22.2.1 (Hardy–Weinberg Law)** Under assumptions 1–7, whatever the genotype frequencies $(P, H, Q)$ of the parents, (a) the allele frequency $p = P + H/2$ is the same in the offspring generation, and (b) the offspring genotype frequencies are $p^2$, $2pq$, $q^2$. Hence a population reaches Hardy–Weinberg proportions after a single generation of random mating and stays there.

**Proof** Random mating of individuals with Mendelian segregation is equivalent to random union of gametes: a parent of genotype $AA$ produces only $A$ gametes, $Aa$ produces $A$ and $a$ in equal numbers, and $aa$ only $a$. The frequency of $A$ among all gametes is therefore $P + \tfrac12 H = p$, and that of $a$ is $q$. A zygote is formed from an egg and a sperm drawn independently from the gamete pool, so by the product rule it is $AA$ with probability $p \cdot p$, $aa$ with probability $q^2$, and $Aa$ with probability $pq + qp = 2pq$ (an $A$ egg with an $a$ sperm, or the reverse). This proves (b). The allele frequency among the zygotes is $p^2 + \tfrac12 \cdot 2pq = p(p + q) = p$, which proves (a). Applying the argument again to the next generation gives the same frequencies. $\square$

The same result follows from the table of the nine mating types: for example $AA \times AA$ matings occur with frequency $P^2$ and give only $AA$; $AA \times Aa$ with frequency $2PH$ give $AA$ and $Aa$ in equal numbers; summing the contributions gives offspring frequency $P^2 + PH + H^2/4 = (P + H/2)^2 = p^2$ for $AA$. The gamete argument is shorter and generalizes immediately.

**Example 22.2.1** A population founded by 1000 $AA$ and 1000 $aa$ individuals, equally divided between the sexes, has $p = q = 0.5$ and no **heterozygotes**. After one generation of random mating, $25\,\%$ of the offspring are $AA$, $50\,\%$ $Aa$ and $25\,\%$ $aa$, and these proportions persist.

Three consequences deserve emphasis.

- Variation is conserved. Mendelian inheritance does not blend away variation; in an ideal population allele frequencies are constant, so variation is lost or changed only by the evolutionary forces of [7.4.23](/7.4.23).
- Dominance does not change allele frequencies. Whether an allele is **dominant** or **recessive** affects phenotype frequencies but not its own frequency. The famous 3:1 ratio holds in an F₂, where $p = 1/2$, not in a population.
- Hardy–Weinberg proportions are a neutral reference. Departures from Hardy–Weinberg proportions in a sample (an excess of **homozygotes**, for example) indicate inbreeding, subdivision, selection between zygote and adult, or, most often in practice, **genotyping** errors.

The geometry of the law is shown in the figure: the genotype frequencies of a population are a point in a triangle, and the Hardy–Weinberg populations form a parabola in it.

![Hardy–Weinberg proportions. A: the frequencies of AA (p²), Aa (2pq) and aa (q²) as functions of the allele frequency q of a; the heterozygote frequency is at most 1/2 (at p = q = 1/2), and a rare allele occurs almost entirely in heterozygotes. B: De Finetti diagram: each population is a point whose distances from the three sides are its genotype frequencies (height above the base = heterozygote frequency, horizontal position = allele frequency q). The parabola H = 2pq contains the populations in Hardy–Weinberg proportions; the MN sample of Example 22.2.2 lies on it. Points below the parabola have a deficit of heterozygotes: inbreeding with F = 0.3 and 0.7 at the same allele frequency, a self-fertilizing plant population, and the pooled sample of two subpopulations (§22.4.4)](./plots/hardy-weinberg.py)

### 22.2.2. Testing Hardy–Weinberg Proportions

**Algorithm 22.2.1 (χ² Test of Hardy–Weinberg Proportions)**

1. Estimate the allele frequency $\hat p = (2n_{AA} + n_{Aa})/2n$ from the sample.
2. Compute the expected counts $n\hat p^2$, $2n\hat p\hat q$, $n\hat q^2$.
3. Compute $X^2 = \sum (O - E)^2/E$ over the three genotype classes.
4. Compare with $\chi^2_1$: three classes, minus one for the fixed total, minus one estimated parameter, leave one degree of freedom (the **goodness-of-fit test** with estimated parameters, [3.2.6](/3.2.6#sec-6.3.3)). Reject HWE at level $0.05$ if $X^2 > 3.84$.

**Example 22.2.2** For the MN sample of Example 22.1.1, $\hat p = 0.5425$, and the expected counts are $1000 \cdot 0.5425^2 = 294.3$, $1000 \cdot 2 \cdot 0.5425 \cdot 0.4575 = 496.4$ and $209.3$. Then

$$
X^2 = \frac{(298 - 294.3)^2}{294.3} + \frac{(489 - 496.4)^2}{496.4} + \frac{(213 - 209.3)^2}{209.3} = 0.22,
$$

with $p = 0.64$: the sample is consistent with Hardy–Weinberg proportions.

**Remark 22.2.1** The χ² approximation is poor when an expected count is small, which is the rule for rare alleles; genotyping centers then use the exact test, which computes the probability of the observed number of heterozygotes conditional on the allele counts (Levene 1949; Wigginton and colleagues 2005). The test has little power: to detect an inbreeding coefficient of $F = 0.05$ at $p = 0.5$, several thousand individuals are needed, because the **statistic** is approximately $nF^2$. A population can therefore be in Hardy–Weinberg proportions at a locus under strong selection, provided selection acts after the genotypes are counted or acts weakly; agreement with HWE never proves the absence of evolutionary forces. In genome-wide studies a strong departure from HWE in controls is used mainly as a quality filter for genotyping errors ([7.4.25](/7.4.25)).

### 22.2.3. Rare Recessive Alleles and Carriers

For a **recessive** disease the heterozygotes cannot be recognized by phenotype, and the allele frequency must be inferred from the frequency of affected homozygotes under the assumption of HWE.

**Formula 22.2.1 (Recessive Allele Frequency and Carriers)** If a fraction $Q$ of the population is affected by a fully penetrant autosomal recessive disease and the population is in HWE, then

$$
\hat q = \sqrt{Q}, \qquad \text{carrier frequency } 2\hat p\hat q \approx 2\sqrt{Q}, \qquad \frac{\text{carriers}}{\text{affected}} = \frac{2pq}{q^2} = \frac{2p}{q} \approx \frac{2}{q}. \tag{22.2}
$$

**Example 22.2.3** Cystic fibrosis affects about 1 in 2500 newborns of European ancestry. Then $q = \sqrt{1/2500} = 0.02$ and the **carrier** frequency is $2 \cdot 0.98 \cdot 0.02 = 0.039$, about 1 in 25: for every affected child there are about $2/q = 98$ carriers. The probability that two unrelated people are both carriers is $0.039^2 \approx 1/650$, and their child is affected with probability $1/4$ of that, $1/2600$, close to the incidence, as it must be.

Equation (22.2) explains a basic fact of human genetics: nearly all copies of a rare recessive allele are hidden in healthy **carriers**. It also shows why selection against affected homozygotes is slow (Formula 23.3.3) and why **consanguinity** concentrates rare recessive disease (§22.4.2). The estimate is only as good as the assumptions: inbreeding or population subdivision inflates the frequency of homozygotes, so that $\sqrt{Q}$ overestimates $q$.

### 22.2.4. Multiple Alleles and the ABO Blood Groups

With **multiple alleles** $A_1, \dots, A_k$ of frequencies $p_1, \dots, p_k$, random union of gametes gives the multinomial expansion $(p_1 + \cdots + p_k)^2$: homozygotes $A_iA_i$ have frequency $p_i^2$ and heterozygotes $A_iA_j$ ($i < j$) frequency $2p_ip_j$. There are $k$ homozygous and $k(k-1)/2$ heterozygous genotypes.

**Definition 22.2.2 (Heterozygosity)** The **heterozygosity** of a locus is the probability that two gene copies drawn at random from the population are different alleles; under HWE it is the frequency of heterozygotes,

$$
H = 1 - \sum_{i=1}^k p_i^2. \tag{22.3}
$$

It is at most $1 - 1/k$, reached when all alleles are equally frequent. Observed heterozygosity is the actual proportion of heterozygous individuals; expected heterozygosity (gene diversity) is Eq. (22.3) computed from the allele frequencies.

The ABO blood group is the classic three-allele system: $I^A$ and $I^B$ are codominant and both dominant to $i$ ([7.4.3](/7.4.3)). Let their frequencies be $p$, $q$, $r$. Under HWE the four phenotypes have frequencies

| Phenotype | Genotypes | Frequency |
|---|---|---|
| A | $I^AI^A$, $I^Ai$ | $p^2 + 2pr$ |
| B | $I^BI^B$, $I^Bi$ | $q^2 + 2qr$ |
| AB | $I^AI^B$ | $2pq$ |
| O | $ii$ | $r^2$ |

Because A and B individuals have hidden genotypes, the allele frequencies cannot be counted directly. Two classical solutions:

**Formula 22.2.2 (Bernstein's Estimates for ABO)** From the phenotype frequencies $\bar A, \bar B, \bar O$, using $\bar A + \bar O = (p + r)^2$ and $\bar B + \bar O = (q + r)^2$,

$$
\hat r = \sqrt{\bar O}, \qquad \hat p = 1 - \sqrt{\bar B + \bar O}, \qquad \hat q = 1 - \sqrt{\bar A + \bar O}. \tag{22.4}
$$

These estimates do not sum exactly to 1; the discrepancy is a check on the assumptions.

The efficient solution is maximum likelihood: the four phenotype counts are multinomial with the probabilities in the table. The likelihood has no closed-form maximum, but it becomes trivial if the hidden genotypes were known, which is exactly the situation of the **EM algorithm** ([3.5.6](/3.5.6)). In genetics this particular EM was invented long before the general method, as "gene counting" (Ceppellini, Siniscalco and Smith 1955).

**Algorithm 22.2.2 (Gene Counting: EM for ABO)** Let the counts be $n_A, n_B, n_{AB}, n_O$ in a sample of $n$. Start from any $(p, q, r)$ with positive entries, and repeat until the estimates stop changing:

1. *E-step.* Split each ambiguous phenotype in proportion to the current genotype probabilities:
   $$
   n_{AA} = n_A\frac{p^2}{p^2 + 2pr}, \quad n_{AO} = n_A - n_{AA}, \qquad n_{BB} = n_B\frac{q^2}{q^2 + 2qr}, \quad n_{BO} = n_B - n_{BB}.
   $$
2. *M-step.* Count alleles as if these were the genotype counts:
   $$
   p = \frac{2n_{AA} + n_{AO} + n_{AB}}{2n}, \qquad q = \frac{2n_{BB} + n_{BO} + n_{AB}}{2n}, \qquad r = 1 - p - q.
   $$

Each iteration increases the likelihood; convergence to the maximum likelihood estimate is fast when the alleles are common.

**Example 22.2.4** In a sample of 1000 people there are 437 of group A, 109 of group B, 45 of AB and 409 of O. Bernstein's estimates are $\hat r = \sqrt{0.409} = 0.6395$, $\hat p = 1 - \sqrt{0.518} = 0.2803$, $\hat q = 1 - \sqrt{0.846} = 0.0802$ (sum $1.00003$). Gene counting from $p = q = r = 1/3$ gives $(0.3138, 0.0952, 0.5910)$ after one iteration, $(0.2868, 0.0811, 0.6321)$ after two, and converges to $\hat p = 0.2803$, $\hat q = 0.0802$, $\hat r = 0.6395$, essentially Bernstein's values. The fitted phenotype counts (437.0, 109.0, 45.0, 409.0) reproduce the data, as expected for a sample generated under HWE.

### 22.2.5. X-Linked Loci

**Formula 22.2.3 (X-Linked Frequencies at Equilibrium)** If an **X-linked** allele has frequency $q$ in both sexes, then **hemizygous** males have the allele with frequency $q$ and females are homozygous with frequency $q^2$ and heterozygous with frequency $2pq$. For a recessive trait, the ratio of affected females to affected males is $q$.

**Example 22.2.5** Red–green color vision defects affect about $8\,\%$ of men of European ancestry, so $q \approx 0.08$; the predicted frequency in women is $q^2 = 0.0064$, close to the observed $0.4$–$0.5\,\%$, and $2pq = 0.147$ of women are carriers. (The calculation treats the several alleles at the *OPN1LW*/*OPN1MW* gene cluster as one.) This is why rare X-linked recessive diseases such as hemophilia A, with $q \approx 10^{-4}$ in males, are almost never seen in women. For an X-linked dominant trait the relation is reversed: males are affected with frequency $q$, females with frequency $q^2 + 2pq = q(2 - q)$, so a rare X-linked dominant condition affects nearly twice as many women as men.

When allele frequencies are estimated from a sample that contains both sexes, the gene copies must be counted, not the individuals: each woman carries two X chromosomes, each man one.

**Formula 22.2.4 (X-Linked Allele Frequency by Gene Counting)** In a sample of $N_f$ women, of whom $n_{aa}$ are homozygous and $n_{Aa}$ heterozygous for allele $a$, and $N_m$ men, of whom $n_a$ carry $a$,

$$
\hat q = \frac{2n_{aa} + n_{Aa} + n_a}{2N_f + N_m}.
$$

**Example 22.2.6** A school survey of 300 girls and 300 boys for red–green color vision finds 3 affected girls, 42 carrier girls (identified from their families or by genotyping) and 21 affected boys. Then $\hat q = (2 \cdot 3 + 42 + 21)/(2 \cdot 300 + 300) = 69/900 = 0.077$, and $\hat p = 0.923$. Averaging the proportions of affected boys ($0.070$) and of $a$ alleles in girls ($48/600 = 0.080$) with equal weights would give $0.075$, a different answer, because the girls contribute two thirds of the X chromosomes.

The approach to equilibrium differs from the autosomal case. A son receives his X from his mother; a daughter one X from each parent. If $q_m$ and $q_f$ are the frequencies in males and females of one generation, then in the next

$$
q_m' = q_f, \qquad q_f' = \tfrac12(q_m + q_f). \tag{22.5}
$$

**Theorem 22.2.2 (Approach to Equilibrium at an X-Linked Locus)** Under random mating, the weighted mean $\bar q = \tfrac13 q_m + \tfrac23 q_f$ (each woman carries two X chromosomes) is constant, and the difference between the sexes changes sign and halves every generation: $q_f' - q_m' = -\tfrac12(q_f - q_m)$. Both frequencies converge to $\bar q$, oscillating around it.

**Proof** From Eq. (22.5), $\tfrac13 q_m' + \tfrac23 q_f' = \tfrac13 q_f + \tfrac13 (q_m + q_f) = \tfrac13 q_m + \tfrac23 q_f$, and $q_f' - q_m' = \tfrac12(q_m + q_f) - q_f = -\tfrac12(q_f - q_m)$. Hence $q_f - q_m$ tends to 0 geometrically, and both frequencies tend to the conserved mean. $\square$

Genotype frequencies in females reach Hardy–Weinberg proportions only as $q_m$ and $q_f$ converge (a female zygote's frequency of homozygotes is $q_mq_f$, not $q_f^2$); with a difference of $0.3$ between the sexes, it takes about 5 generations for the difference to fall below $0.01$.

![Approach to equilibrium at an X-linked locus in a population founded with allele frequency 0.3 in females and 0 in males. Each generation males take the frequency of the females of the previous generation and females the mean of both sexes (Eq. (22.5)); the difference between the sexes changes sign and halves every generation while the weighted mean (2q_f + q_m)/3 = 0.2 stays constant (Theorem 22.2.2)](./plots/x-linked-approach.py)

## 22.3. Two Loci: Haplotypes and Linkage Disequilibrium

### 22.3.1. Measures of Disequilibrium

With two loci, one generation of random mating is no longer enough to reach equilibrium, because chromosomes, not individual alleles, are transmitted.

**Definition 22.3.1 (Haplotype)** A **haplotype** is the combination of alleles at several loci on one chromosome (one homolog). Two chromosomes with the same allele at each of the loci considered have the same haplotype.

Consider loci $A/a$ and $B/b$ with allele frequencies $p_A, p_a, p_B, p_b$, and let $p_{AB}, p_{Ab}, p_{aB}, p_{ab}$ be the haplotype frequencies in the gamete pool.

**Definition 22.3.2 (Linkage Disequilibrium)** The **linkage disequilibrium** coefficient is

$$
D = p_{AB} - p_Ap_B = p_{AB}\,p_{ab} - p_{Ab}\,p_{aB}. \tag{22.6}
$$
The loci are in **linkage equilibrium** if $D = 0$, so that every haplotype frequency is the product of its allele frequencies (the alleles at one locus carry no information about the alleles at the other); otherwise they are in linkage disequilibrium (LD), also called gametic phase disequilibrium. Two normalized measures are used:

$$
D' = \frac{D}{D_{\max}}, \quad D_{\max} = \begin{cases}\min(p_Ap_b,\ p_ap_B), & D > 0,\\ \min(p_Ap_B,\ p_ap_b), & D < 0,\end{cases} \qquad r^2 = \frac{D^2}{p_Ap_ap_Bp_b}. \tag{22.7}
$$

$|D'| = 1$ means that at least one of the four haplotypes is absent (no evidence of recombination between the loci since the haplotypes arose); $r^2$ is the square of the **correlation coefficient** between the allele indicators at the two loci on the same chromosome ([3.1.10](/3.1.10)), and $r^2 = 1$ only if just two haplotypes exist and each allele at one locus predicts its partner at the other perfectly.

The two identities in Eq. (22.6) are equivalent: substituting $p_{Ab} = p_A - p_{AB}$, $p_{aB} = p_B - p_{AB}$ and $p_{ab} = 1 - p_A - p_B + p_{AB}$ gives $p_{AB}p_{ab} - p_{Ab}p_{aB} = p_{AB} - p_Ap_B$. Note also $p_{AB} = p_Ap_B + D$, $p_{Ab} = p_Ap_b - D$, $p_{aB} = p_ap_B - D$, $p_{ab} = p_ap_b + D$.

**Example 22.3.1** Suppose two SNPs, $A/a$ and $B/b$, each have allele frequencies $1/2$ and the haplotype frequencies are $p_{AB} = p_{ab} = 0.4$, $p_{Ab} = p_{aB} = 0.1$. Then $D = 0.4 - 0.25 = 0.15$; $D_{\max} = \min(0.25, 0.25) = 0.25$, so $D' = 0.6$; and $r^2 = 0.15^2/0.5^4 = 0.36$. In linkage equilibrium all four haplotypes would have frequency $0.25$.

The two measures answer different questions. $D'$ reflects the recombination history of a pair of sites and tends to be near 1 within blocks of the genome that have rarely recombined; $r^2$ measures how well one site predicts the other, which is what matters for mapping: a test at a marker in LD $r^2$ with a causal variant has the power of a test at the causal variant with $r^2$ times the **sample size** ([7.4.25](/7.4.25)).

### 22.3.2. Decay of Disequilibrium

**Theorem 22.3.1 (Decay of Linkage Disequilibrium)** In an infinite randomly mating population without selection, mutation or migration, with **recombination frequency** $r$ between the loci,

$$
D_t = (1 - r)^t D_0. \tag{22.8}
$$

Allele frequencies stay constant; for unlinked loci ($r = 1/2$) disequilibrium halves every generation.

**Proof** A gamete produced by an individual is non-recombinant with probability $1 - r$, in which case it is a copy of one of the parent's two haplotypes, chosen with probability $1/2$ each; since parental haplotypes are drawn from the pool, such a gamete is $AB$ with probability $p_{AB}$. With probability $r$ it is recombinant, carrying the allele at $A$ from one parental chromosome and the allele at $B$ from the other; under random mating the two chromosomes of an individual are independent draws from the pool, so a **recombinant gamete** is $AB$ with probability $p_Ap_B$. Hence $p_{AB}' = (1 - r)p_{AB} + rp_Ap_B$, and subtracting $p_Ap_B$ (unchanged) gives $D' = (1 - r)D$. $\square$

The approach to linkage equilibrium is gradual, in contrast with the single generation needed for Hardy–Weinberg proportions at one locus. For loci $1\,\mathrm{cM}$ apart ($r = 0.01$) the half-life of $D$ is $\ln 0.5/\ln 0.99 = 69$ generations, about 1700 years in humans; for $0.1\,\mathrm{cM}$ (about $100\,\mathrm{kb}$) it is about 700 generations.

**Remark 22.3.1 (Sources of Linkage Disequilibrium)** LD is created by every process that makes haplotype frequencies depart from the product of allele frequencies.

- *New mutation.* A mutation arises on one chromosome, so at first it is found only with the alleles of that chromosome at nearby loci: if a new allele $a$ arises on an $Ab$ chromosome in a population of $AB$ and $Ab$ haplotypes, the haplotype $aB$ is absent and $|D'| = 1$ until recombination creates it.
- *Genetic drift.* In a finite population, random sampling of haplotypes creates LD of order $1/(4N_e r)$ ([7.4.23](/7.4.23)); this is the main source of LD between nearby common SNPs in humans.
- *Selection.* Epistatic selection favoring particular combinations, and the rapid spread of a favored allele that carries its neighbors with it (a selective sweep), generate LD.
- *Admixture and subdivision.* Mixing populations with different allele frequencies creates LD even between unlinked loci; it then decays at rate $r$, a fact used to date admixture events.

Because LD decays at rate $r$, the length of the haplotype that a mutation still shares with its ancestral chromosome measures its age. After $g$ generations the ancestral segment extends on each side of the mutation over an exponentially distributed length with mean $1/g$ morgans; the expected total length is $2/g$ morgans, about $2\,\mathrm{cM}$ for a mutation 100 generations old. This principle dated the spread of the lactase persistence allele ([7.4.23](/7.4.23)) and underlies the mapping of disease mutations in isolated populations by shared ancestral haplotypes ([7.4.25](/7.4.25)).

![Decay of linkage disequilibrium under random mating, D_t = (1 − r)^t D_0 (Theorem 22.3.1). A: unlinked loci (r = 1/2) lose half of their disequilibrium each generation; tightly linked loci keep it for hundreds of generations (dots mark the half-life ln 2/r for r = 0.1, 0.01, 0.001). B: the probability that the ancestral haplotype is intact over a distance d on one side of a mutation of age g generations, e^(−gd); the expected length of the shared haplotype around the mutation is 2/g morgans, so young mutations sit on long haplotypes and old mutations on short ones](./plots/ld-decay.py)

## 22.4. Nonrandom Mating

### 22.4.1. Assortative Mating

**Definition 22.4.1 (Assortative Mating)** **Assortative mating** is mating in which the choice of partner depends on phenotype. It is positive when similar phenotypes mate more often than at random, and negative (disassortative) when dissimilar phenotypes mate more often. Mating that depends on ancestry rather than phenotype is inbreeding (§22.4.2); mating with neighbors in a spatially extended population (isolation by distance) has effects similar to subdivision (§22.4.4).

Positive assortative mating affects only the loci that influence the trait on which partners are chosen, and those loci that are in LD with them; it increases the homozygosity at these loci and creates positive LD (correlations) among the alleles that increase the trait, which in turn raises the genetic **variance** of the trait. In humans assortative mating is almost universally positive: the correlation between partners is about $0.2$–$0.25$ for height, about $0.4$–$0.5$ for educational attainment, and substantial for several common diseases and psychiatric conditions. This matters for the estimation of heritability and of the effects of genetic variants on such traits ([7.4.24](/7.4.24), [7.4.25](/7.4.25)).

Negative assortative mating maintains variation: a rare type finds partners more easily than a common one. The self-incompatibility systems of flowering plants are extreme cases: pollen carrying an S allele cannot fertilize a plant with the same allele, so a rare S allele always has an advantage, and populations maintain dozens of S alleles at nearly equal frequencies (**frequency-dependent selection**, [7.4.23](/7.4.23)).

### 22.4.2. Inbreeding in a Population

In [7.4.7](/7.4.7) the **inbreeding coefficient** $F$ of an individual was defined as the probability that its two alleles at a locus are **identical by descent**, and computed from a **pedigree** by path counting. In a population, $F$ is the mean of this probability over individuals, and it modifies Hardy–Weinberg proportions in a simple way.

**Formula 22.4.1 (Genotype Frequencies with Inbreeding)** In a population with allele frequencies $p, q$ and inbreeding coefficient $F$ (relative to a base population in which alleles are not identical by descent),

$$
P = p^2 + Fpq, \qquad H = 2pq(1 - F), \qquad Q = q^2 + Fpq. \tag{22.9}
$$

Conversely, $F = 1 - H_{\mathrm{obs}}/2pq$ is the proportional deficit of heterozygotes.

**Proof** With probability $F$ the two alleles of an individual are IBD, hence copies of one ancestral allele: the individual is $AA$ with probability $p$ and $aa$ with probability $q$. With probability $1 - F$ they are two independent draws from the pool, giving Hardy–Weinberg proportions. Therefore $P = Fp + (1 - F)p^2 = p^2 + Fp(1 - p) = p^2 + Fpq$, and similarly for $Q$; $H = (1 - F)2pq$. The allele frequency is $P + H/2 = p^2 + Fpq + pq(1 - F) = p$, unchanged. $\square$

Inbreeding thus redistributes genotypes without changing allele frequencies: it converts heterozygotes into homozygotes in equal numbers on both sides. Its main effect on rare recessive alleles follows from Eq. (22.9): affected homozygotes have frequency $q^2 + Fpq \approx q(q + F)$, a ratio $(q + F)/q$ to the random-mating value. For $q = 0.01$ and $F = 0.1$ the frequency is $0.00109$, $10.9$ times $q^2$; for the children of first cousins ($F = 1/16$) and $q = 0.005$ it is $13.4$ times. The rarer the allele, the larger the relative effect, which is why parental consanguinity is a hallmark of the rarest recessive diseases ([7.4.7](/7.4.7)). Since inbreeding exposes all deleterious recessive alleles at once, it reduces the mean of fitness-related traits, the **inbreeding depression** analyzed in [7.4.24](/7.4.24).

### 22.4.3. Regular Systems of Inbreeding

Plant and animal breeders inbreed systematically to produce homozygous lines. Each system gives a recursion for $F_t$ in generation $t$, derived by the path method or by following **identity by descent** one generation back.

**Formula 22.4.2 (Inbreeding Coefficient Under Regular Systems)** Starting from a non-inbred population ($F_0 = 0$):

| System | Recursion | Panmictic index $1 - F_t$ |
|---|---|---|
| self-fertilization | $F_t = \tfrac12(1 + F_{t-1})$ | $(1/2)^t$ |
| full-sib mating | $F_t = \tfrac14(1 + 2F_{t-1} + F_{t-2})$ | $\sim c\,(0.809)^t$, $0.809 = (1 + \sqrt5)/4$ |
| half-sib mating | $F_t = \tfrac18(1 + 6F_{t-1} + F_{t-2})$ | $\sim c\,(0.890)^t$, $0.890 = (3 + \sqrt{17})/8$ |
| random mating, size $N$ | $F_t = \tfrac{1}{2N} + \left(1 - \tfrac{1}{2N}\right)F_{t-1}$ | $(1 - 1/2N)^t$ |

The asymptotic factors are the largest roots of the characteristic equations of the linear recursions for $1 - F_t$ ($4x^2 = 2x + 1$ and $8x^2 = 6x + 1$).

**Proof** (selfing) The two alleles of an offspring of selfing are copies of alleles of the one parent. With probability $1/2$ they are copies of the same parental allele (IBD); with probability $1/2$ they are copies of the parent's two alleles, which are IBD with probability $F_{t-1}$. Hence $F_t = \tfrac12 + \tfrac12F_{t-1}$, and $1 - F_t = \tfrac12(1 - F_{t-1})$. The other rows follow in the same way from the kinship coefficients of sibs; the last row is the effect of drift, derived in [7.4.23](/7.4.23). $\square$

Under selfing, heterozygosity halves every generation, which is the reason why naturally self-fertilizing plants such as *Arabidopsis thaliana* and Mendel's peas are almost completely homozygous. Twenty generations of full-sib mating, the standard definition of an inbred mouse strain, give $F = 0.986$.

![Loss of heterozygosity under regular systems of inbreeding, shown as the panmictic index 1 − F on a log scale (Formula 22.4.2). Self-fertilization halves it every generation; full-sib mating reduces it asymptotically by the factor 0.809 per generation and half-sib mating by 0.890; drift alone in a randomly mating population of N = 50 reduces it by 1 − 1/2N = 0.99 per generation. Dashed: 20 generations of full-sib mating (F = 0.986), the definition of an inbred strain](./plots/inbreeding-systems.py)

### 22.4.4. Population Subdivision and the Wahlund Effect

Real populations are often divided into partially isolated subpopulations (demes) with different allele frequencies. A sample that pools them shows a deficit of heterozygotes even if each subpopulation is in HWE.

**Theorem 22.4.1 (Wahlund Effect)** Let a population consist of subpopulations with weights $c_i$ ($\sum c_i = 1$) and allele frequencies $p_i$, each in Hardy–Weinberg proportions, and let $\bar p = \sum c_ip_i$ and $\operatorname{Var}(p) = \sum c_i(p_i - \bar p)^2$. Then the pooled frequencies are

$$
\bar P = \bar p^2 + \operatorname{Var}(p), \qquad \bar H = 2\bar p\bar q - 2\operatorname{Var}(p), \qquad \bar Q = \bar q^2 + \operatorname{Var}(p). \tag{22.10}
$$

**Proof** $\bar P = \sum c_ip_i^2 = \bar p^2 + \operatorname{Var}(p)$ by the definition of **variance** ([3.1.8](/3.1.8)); similarly $\bar Q = \sum c_iq_i^2 = \bar q^2 + \operatorname{Var}(q)$ with $\operatorname{Var}(q) = \operatorname{Var}(p)$; and $\bar H = 1 - \bar P - \bar Q$. $\square$

**Definition 22.4.2 (Wahlund Effect and Fixation Index)** The deficit of heterozygotes in a pooled sample of genetically different subpopulations, relative to Hardy–Weinberg proportions at the pooled allele frequency, is the **Wahlund effect** (Wahlund 1928). Wright's **fixation index** measures the differentiation of the subpopulations as the proportional reduction of heterozygosity,

$$
F_{\mathrm{ST}} = \frac{H_{\mathrm{T}} - H_{\mathrm{S}}}{H_{\mathrm{T}}} = \frac{\operatorname{Var}(p)}{\bar p(1 - \bar p)}, \tag{22.11}
$$

where $H_{\mathrm{T}} = 2\bar p\bar q$ is the expected heterozygosity of the total population and $H_{\mathrm{S}} = \sum c_i 2p_iq_i$ the mean expected heterozygosity within subpopulations. $F_{\mathrm{ST}}$ is 0 when all subpopulations have the same allele frequencies and 1 when each is fixed for one allele.

Comparing Eqs. (22.10) and (22.9), subdivision acts on the pooled sample like inbreeding with $F = F_{\mathrm{ST}}$: individuals in the same subpopulation are more likely to share alleles by descent than individuals drawn at random from the whole. Wright's hierarchical $F$-statistics combine the two sources of homozygosity, inbreeding within subpopulations ($F_{\mathrm{IS}}$) and subdivision ($F_{\mathrm{ST}}$), into the total $F_{\mathrm{IT}}$:

$$
1 - F_{\mathrm{IT}} = (1 - F_{\mathrm{IS}})(1 - F_{\mathrm{ST}}). \tag{22.12}
$$

**Example 22.4.1** Two equal subpopulations have allele frequencies $0.2$ and $0.8$. Each is in HWE ($0.04 : 0.32 : 0.64$ and $0.64 : 0.32 : 0.04$), so the pooled sample is $0.34 : 0.32 : 0.34$. The pooled allele frequency is $\bar p = 0.5$, for which HWE predicts $0.25 : 0.5 : 0.25$; the heterozygote deficit is $0.18 = 2\operatorname{Var}(p)$ with $\operatorname{Var}(p) = 0.09$, and $F_{\mathrm{ST}} = 0.09/0.25 = 0.36$. A χ² test on a pooled sample would reject HWE and might be misread as evidence of inbreeding or selection.

For humans, $F_{\mathrm{ST}}$ between continental populations averaged over the genome is about $0.1$–$0.15$; equivalently, about $85$–$90\,\%$ of human genetic diversity is found within any one population, and only a small part distinguishes populations (Lewontin 1972, confirmed by genome sequencing). Differentiation is larger at a minority of loci under local selection (skin pigmentation, lactase persistence, high-altitude adaptation). Population structure is the main confounder of association studies, because allele frequencies and disease rates may both differ between subpopulations ([7.4.25](/7.4.25)); the balance between drift, which creates $F_{\mathrm{ST}}$, and migration, which erodes it, is treated in [7.4.23](/7.4.23).

![The Wahlund effect (Theorem 22.4.1). A: two equal subpopulations with allele frequencies 0.2 and 0.8, each in Hardy–Weinberg proportions; their pooled sample (0.34 : 0.32 : 0.34) has far fewer heterozygotes than Hardy–Weinberg proportions at the pooled frequency 0.5 (0.25 : 0.50 : 0.25). B: for two equal subpopulations with frequencies 0.5 − x and 0.5 + x, the heterozygote deficit 2 Var(p) = 2x² and the fixation index F_ST = 4x²; dots mark the example of panel A (x = 0.3)](./plots/wahlund.py)

## 22.5. Applications: Forensic Identification and Paternity

### 22.5.1. Random Match Probability

Forensic DNA profiles consist of the genotypes at a set of highly polymorphic **microsatellite** loci (short tandem repeats; the US CODIS system uses 20 core loci), each with 10–30 alleles. When the profile of a crime-scene sample matches a suspect, the court needs to know how often such a match would occur by chance.

**Definition 22.5.1 (Random Match Probability)** The **random match probability** of a DNA profile is the probability that a person chosen at random from a reference population, unrelated to the source of the sample, has the same profile.

**Formula 22.5.1 (Product Rule and θ Correction)** If the loci are in HWE and in linkage equilibrium (they are chosen on different chromosomes or far apart), the random match probability is the product over loci of the genotype frequencies,

$$
\text{RMP} = \prod_{\text{loci}} \begin{cases} p_i^2, & \text{homozygote } A_iA_i,\\ 2p_ip_j, & \text{heterozygote } A_iA_j.\end{cases} \tag{22.13}
$$

To allow for population structure and relatedness within a population, the National Research Council (1996) recommends replacing each factor by the conditional probability that a second person has the genotype given that the first does (Balding and Nichols 1994), with a coancestry coefficient $\theta$ (in effect, $F_{\mathrm{ST}}$ of the subpopulation; $0.01$ in general, up to $0.03$ for small isolated groups):

$$
A_iA_i\colon \frac{[2\theta + (1 - \theta)p_i][3\theta + (1 - \theta)p_i]}{(1 + \theta)(1 + 2\theta)}, \qquad A_iA_j\colon \frac{2[\theta + (1 - \theta)p_i][\theta + (1 - \theta)p_j]}{(1 + \theta)(1 + 2\theta)}. \tag{22.14}
$$

**Example 22.5.1** A three-locus profile is heterozygous at locus 1 for alleles of frequencies $0.1$ and $0.2$, homozygous at locus 2 for an allele of frequency $0.15$, and heterozygous at locus 3 for alleles of frequencies $0.05$ and $0.3$. By the product rule, RMP $= (2 \cdot 0.1 \cdot 0.2)(0.15^2)(2 \cdot 0.05 \cdot 0.3) = 0.04 \cdot 0.0225 \cdot 0.03 = 2.7 \times 10^{-5}$, about 1 in 37 000. With $\theta = 0.01$ the RMP is $4.6 \times 10^{-5}$ (1 in 22 000), with $\theta = 0.03$ it is $1.1 \times 10^{-4}$ (1 in 9400): the correction always favors the defendant, and its effect is largest for rare alleles and homozygotes. With 20 loci, typical profiles have RMPs of $10^{-20}$ or less.

The random match probability is not the probability that the suspect is innocent. Confusing the two is the prosecutor's fallacy: if 1 person in a million matches and the population of possible sources is 10 million, about 10 people would match, and without other evidence the match alone gives a posterior probability of guilt of about $1/11$ (**Bayes' theorem**). The proper summary is the **likelihood ratio** of the evidence under the two hypotheses (the suspect is the source; an unknown person is the source), which for a simple match is $1/\text{RMP}$. Relatives of the suspect have far higher match probabilities than unrelated people (a full sib shares both alleles at a locus with probability $1/4$ or more), which is why familial searching of databases works.

### 22.5.2. Paternity Testing

**Formula 22.5.2 (Paternity Index)** At a locus where the child's paternal (obligate) allele $A_i$ has frequency $p_i$, the paternity index is the **likelihood ratio**

$$
\text{PI} = \frac{\mathbb{P}(\text{child's genotype} \mid \text{alleged father is the father})}{\mathbb{P}(\text{child's genotype} \mid \text{a random man is the father})} = \frac{t}{p_i}, \tag{22.15}
$$

where $t$ is the probability that the alleged father transmits $A_i$ ($1/2$ if he is heterozygous, $1$ if homozygous). Indices of independent loci multiply into the combined paternity index CPI; with prior probability $\pi$ of paternity, the posterior probability is $\pi\,\text{CPI}/[\pi\,\text{CPI} + (1 - \pi)]$, which equals $\text{CPI}/(\text{CPI} + 1)$ for the conventional prior $\pi = 1/2$.

**Example 22.5.2** A child has the paternal allele $A_7$ (frequency $0.05$) and the alleged father is heterozygous for it: PI $= 0.5/0.05 = 10$, and with prior $1/2$ this locus alone gives a probability of paternity of $10/11 = 0.909$. Fifteen loci with indices of about 10 each give CPI $\approx 10^{15}$ and a probability of paternity indistinguishable from 1. An exclusion (the man lacks the obligate allele) at two or more loci excludes paternity; a single exclusion may be a **mutation**, since **microsatellites** mutate at about $10^{-3}$ per locus per generation.

### 22.5.3. Carrier Screening

Expanded carrier screening tests prospective parents for hundreds of recessive conditions. For one condition with carrier frequency $c = 2pq$, the probability that a random couple are both carriers is $c^2$ and the risk to each child $c^2/4$; summed over many conditions, about $1$–$2\,\%$ of couples are at risk for at least one. Targeted programs exploit population differences in allele frequency, the result of **founder effects** and drift ([7.4.23](/7.4.23)): Tay–Sachs screening among Ashkenazi Jews (carrier frequency about 1 in 30) reduced the incidence of the disease in that population by more than $90\,\%$ since the 1970s, and β-thalassemia screening in Cyprus and Sardinia had similar effects.

## Summary

The ideal population (Theorem 22.2.1): infinite size, random mating, no mutation, migration or selection, equal frequencies in the sexes. Then

| Quantity | Result |
|---|---|
| allele frequency | $p = P + H/2$, constant; $\operatorname{SE}(\hat p) = \sqrt{pq/2n}$, Eq. (22.1) |
| genotypes | $p^2 : 2pq : q^2$ after one generation of random mating |
| test | χ² with 1 df (Algorithm 22.2.1); exact test for rare alleles; low power (Remark 22.2.1) |
| rare recessive | $q = \sqrt{Q}$, carriers $\approx 2q$, carriers/affected $\approx 2/q$, Eq. (22.2) |
| $k$ alleles | $p_i^2$, $2p_ip_j$; heterozygosity $H = 1 - \sum p_i^2$, Eq. (22.3); ABO by Bernstein, Eq. (22.4), or gene counting (EM, Algorithm 22.2.2) |
| X-linked | males $q$, females $q^2$ (recessive) or $q(2-q)$ (dominant); gene counting $\hat q = (2n_{aa} + n_{Aa} + n_a)/(2N_f + N_m)$ (Formula 22.2.4, Example 22.2.6); difference between sexes $\times(-1/2)$ per generation, mean $(q_m + 2q_f)/3$ conserved (Theorem 22.2.2) |

Two loci: haplotype frequencies $p_{AB} = p_Ap_B + D$; $D'$ and $r^2$ (Eq. (22.7)); $D_t = (1 - r)^tD_0$ (Theorem 22.3.1), so linkage equilibrium is approached slowly for linked loci; LD is created by mutation, drift, selection and admixture, and the length of the ancestral haplotype ($2/g$ morgans) dates a mutation.

Nonrandom mating changes genotype but not allele frequencies:

| Process | Effect |
|---|---|
| positive assortative mating | homozygosity and LD at trait loci only |
| inbreeding | $p^2 + Fpq$, $2pq(1 - F)$, $q^2 + Fpq$ at all loci (Formula 22.4.1); rare recessives $\times (q + F)/q$ |
| selfing / full sibs / half sibs | $1 - F$ per generation $\times 1/2$, $0.809$, $0.890$ (Formula 22.4.2) |
| subdivision | Wahlund deficit $2\operatorname{Var}(p)$ (Theorem 22.4.1); $F_{\mathrm{ST}} = \operatorname{Var}(p)/\bar p\bar q$; $1 - F_{\mathrm{IT}} = (1 - F_{\mathrm{IS}})(1 - F_{\mathrm{ST}})$ |

Applications: random match probability by the product rule with the θ correction (Formula 22.5.1), a likelihood ratio and not the probability of innocence; paternity index $t/p_i$ (Formula 22.5.2); carrier risk $c^2/4$ per child.

## Questions

1. In a sample of 200 individuals typed for a codominant marker there are 90 $AA$, 80 $Aa$ and 30 $aa$. Estimate the allele frequencies with their standard errors and test for Hardy–Weinberg proportions.

   **Answer** $\hat p = (180 + 80)/400 = 0.65$, $\hat q = 0.35$; $\operatorname{SE} = \sqrt{0.65 \cdot 0.35/400} = 0.024$. Expected counts $200 \cdot 0.4225 = 84.5$, $200 \cdot 0.455 = 91.0$, $200 \cdot 0.1225 = 24.5$. $X^2 = 5.5^2/84.5 + 11^2/91 + 5.5^2/24.5 = 0.358 + 1.330 + 1.235 = 2.92$ with 1 df, $p = 0.087$: no significant departure at the $5\,\%$ level, although heterozygotes are somewhat deficient.

2. An autosomal recessive disease affects 1 in 10 000 births in a randomly mating population. (a) What fraction of the population are carriers? (b) How many carriers are there per affected person? (c) What is the risk that the first child of two unrelated, unaffected people from this population is affected? (d) What if one partner is known to be a carrier?

   **Answer** (a) $q = 0.01$, carriers $2pq = 2 \cdot 0.99 \cdot 0.01 = 0.0198$, about 1 in 50. (b) $2pq/q^2 = 198$. (c) An unaffected person is a carrier with probability $2pq/(1 - q^2) \approx 0.0198$; risk $0.0198^2 \cdot 1/4 = 9.8 \times 10^{-5}$, essentially the population incidence. (d) $1 \cdot 0.0198 \cdot 1/4 = 0.005$, 1 in 200.

3. Why does the allele frequency of a recessive disease estimated as $\sqrt{Q}$ tend to be too high in a population with frequent consanguineous marriages? By how much, if $F = 0.02$ and the true $q = 0.005$?

   **Answer** Inbreeding adds homozygotes: $Q = q^2 + Fpq$ (Formula 22.4.1). With $q = 0.005$, $Q = 0.000025 + 0.02 \cdot 0.995 \cdot 0.005 = 0.000025 + 0.0000995 = 0.0001245$, so $\sqrt{Q} = 0.0112$, more than twice the true frequency. Most affected individuals in such a population are children of consanguineous unions.

4. In a population the ABO phenotype frequencies are A $0.45$, B $0.13$, AB $0.06$, O $0.36$. Estimate the allele frequencies by Bernstein's method and check their sum. What would the expected frequency of AB be?

   **Answer** $\hat r = \sqrt{0.36} = 0.600$; $\hat p = 1 - \sqrt{0.13 + 0.36} = 1 - 0.700 = 0.300$; $\hat q = 1 - \sqrt{0.45 + 0.36} = 1 - 0.900 = 0.100$; sum $1.000$. Expected AB $= 2\hat p\hat q = 0.06$, as observed; the data are consistent with HWE.

5. About $8\,\%$ of men in a population have an X-linked recessive color vision defect. Assuming HWE, what fraction of women (a) are affected, (b) are carriers? (c) A woman whose father is affected marries an unaffected man; what is the probability that their first son is affected? (d) That their first child is an affected daughter?

   **Answer** (a) $q^2 = 0.0064$. (b) $2pq = 2 \cdot 0.92 \cdot 0.08 = 0.147$. (c) She is an obligate carrier (her father gave her his X), so a son is affected with probability $1/2$. (d) A daughter receives the father's normal X, so she cannot be affected: probability 0.

6. A population is founded by migrants among whom an X-linked allele has frequency $0.3$ in women and $0$ in men. (a) What are the frequencies in each sex in the next three generations? (b) What is the equilibrium frequency? (c) After how many generations is the difference between the sexes less than $0.01$?

   **Answer** By Eq. (22.5): generation 1, $q_m = 0.300$, $q_f = 0.150$; generation 2, $0.150$, $0.225$; generation 3, $0.225$, $0.1875$. (b) $\bar q = (0 + 2 \cdot 0.3)/3 = 0.2$. (c) The difference is $0.3 \cdot (1/2)^t$ in absolute value; $0.3/2^t < 0.01$ requires $2^t > 30$, $t = 5$ (difference $0.0094$).

7. Two SNPs have the haplotype frequencies $AB$ $0.50$, $Ab$ $0.10$, $aB$ $0.05$, $ab$ $0.35$. (a) Compute $p_A$, $p_B$, $D$, $D'$ and $r^2$. (b) If the SNPs are $5\,\mathrm{cM}$ apart and the population mates at random, what is $D$ after 10 generations? (c) What is the frequency of $AB$ at linkage equilibrium?

   **Answer** (a) $p_A = 0.60$, $p_B = 0.55$; $D = 0.50 - 0.60 \cdot 0.55 = 0.17$ (check: $0.50 \cdot 0.35 - 0.10 \cdot 0.05 = 0.17$). $D > 0$, $D_{\max} = \min(0.6 \cdot 0.45, 0.4 \cdot 0.55) = \min(0.27, 0.22) = 0.22$, $D' = 0.773$. $r^2 = 0.17^2/(0.6 \cdot 0.4 \cdot 0.55 \cdot 0.45) = 0.0289/0.0594 = 0.487$. (b) $r \approx 0.05$: $D_{10} = 0.17 \cdot 0.95^{10} = 0.102$. (c) $p_Ap_B = 0.33$.

8. Explain why one generation of random mating establishes Hardy–Weinberg proportions at each of two loci but not linkage equilibrium between them. Can unlinked loci be in linkage disequilibrium?

   **Answer** HWE at one locus requires only that the two gametes forming a zygote be independent, which random mating guarantees at once. Linkage equilibrium requires that the alleles on one gamete at two loci be independent; a gamete is a copy of a parental chromosome unless recombination occurs, so the association is broken only in the fraction $r$ of gametes that are recombinant, giving $D_t = (1 - r)^tD_0$. Yes: unlinked loci ($r = 1/2$) can be in LD, for example right after admixture of two populations with different allele frequencies at both loci, or under epistatic selection; it then halves every generation.

9. A rare recessive allele has frequency $q = 0.01$. (a) Compare the frequency of affected homozygotes in a randomly mating population with that in a population with mean inbreeding coefficient $F = 0.1$. (b) Among the children of first cousins ($F = 1/16$)?

   **Answer** (a) $q^2 = 10^{-4}$; $q^2 + Fpq = 10^{-4} + 0.1 \cdot 0.99 \cdot 0.01 = 1.09 \times 10^{-3}$, 10.9 times higher. (b) $10^{-4} + 0.0625 \cdot 0.0099 = 7.19 \times 10^{-4}$, 7.2 times the random-mating risk.

10. A plant population with heterozygosity $0.5$ at a locus switches to self-fertilization. (a) What is the heterozygosity after 5 generations? (b) What is the inbreeding coefficient after 3 generations of full-sib mating starting from non-inbred parents? (c) Why does full-sib mating reduce heterozygosity more slowly than selfing?

    **Answer** (a) $0.5 \cdot (1/2)^5 = 0.0156$. (b) $F_1 = \tfrac14(1 + 0 + 0) = 0.25$, $F_2 = \tfrac14(1 + 0.5 + 0) = 0.375$, $F_3 = \tfrac14(1 + 0.75 + 0.25) = 0.5$. (c) The two alleles of a selfed offspring come from one parent and are IBD with probability at least $1/2$; those of a sib-mated offspring come from two parents (sibs) whose kinship coefficient is only $1/4$ in a non-inbred family, so identity accumulates more slowly (factor $0.809$ instead of $0.5$ per generation asymptotically).

11. A sample pools three equal subpopulations with allele frequencies $0.1$, $0.4$ and $0.7$, each in HWE. (a) What heterozygosity is observed, and what is expected from the pooled allele frequency? (b) Compute $F_{\mathrm{ST}}$. (c) If in addition each subpopulation has $F_{\mathrm{IS}} = 0.05$, what is $F_{\mathrm{IT}}$?

    **Answer** (a) $\bar p = 0.4$; $H_{\mathrm{S}} = \tfrac13(0.18 + 0.48 + 0.42) = 0.36$; $H_{\mathrm{T}} = 2 \cdot 0.4 \cdot 0.6 = 0.48$. (b) $\operatorname{Var}(p) = \tfrac13(0.09 + 0 + 0.09) = 0.06$; $F_{\mathrm{ST}} = 0.06/0.24 = 0.25$ (equivalently $(0.48 - 0.36)/0.48$); the deficit $0.12 = 2\operatorname{Var}(p)$. (c) $1 - F_{\mathrm{IT}} = 0.95 \cdot 0.75 = 0.7125$, $F_{\mathrm{IT}} = 0.2875$.

12. For the three-locus profile of Example 22.5.1, (a) verify the random match probability with $\theta = 0.01$; (b) explain why the θ correction increases the match probability most for homozygotes at rare alleles.

    **Answer** (a) Locus 1: $2(0.01 + 0.99 \cdot 0.1)(0.01 + 0.99 \cdot 0.2)/(1.01 \cdot 1.02) = 2 \cdot 0.109 \cdot 0.208/1.0302 = 0.04401$; locus 2: $(0.02 + 0.1485)(0.03 + 0.1485)/1.0302 = 0.02920$; locus 3: $2(0.0595)(0.307)/1.0302 = 0.03546$. Product $4.56 \times 10^{-5}$, 1 in 22 000. (b) $\theta$ adds a probability of order $\theta$ that the second person carries the allele by shared descent; this is negligible compared with $p_i$ for common alleles but dominates when $p_i \lesssim \theta$, and a homozygote requires two such copies, so its factor rises from $p_i^2$ to about $(2\theta + p_i)(3\theta + p_i)$.

13. A child carries the paternal allele $A_{12}$ with frequency $0.08$ at one locus and $B_3$ with frequency $0.2$ at another. The alleged father is homozygous $A_{12}A_{12}$ and heterozygous for $B_3$. Compute the combined paternity index and the probability of paternity with prior $1/2$. How would a prior of $0.1$ change the result?

    **Answer** PI$_1 = 1/0.08 = 12.5$, PI$_2 = 0.5/0.2 = 2.5$, CPI $= 31.25$. Posterior with $\pi = 1/2$: $31.25/32.25 = 0.969$. With $\pi = 0.1$: $0.1 \cdot 31.25/(0.1 \cdot 31.25 + 0.9) = 3.125/4.025 = 0.776$. The likelihood ratio is the evidence; the posterior also depends on the prior, which is why courts are often given the CPI rather than a probability.

14. (Open question.) A study finds a large excess of homozygotes at one SNP in a sample of cases and controls, but not at neighboring SNPs. List possible explanations and how you would distinguish them.

    **Answer** Possibilities: (i) genotyping error, for example a **null allele** (a polymorphism in a probe or **primer** site prevents detection of one allele, so heterozygotes are called homozygotes) or poor cluster separation, which affects one assay and not its neighbors; (ii) a deletion polymorphism, in which hemizygous individuals appear homozygous; (iii) selection or association with the disease, if the excess is confined to cases; (iv) inbreeding or population structure, which would affect all loci similarly and is therefore unlikely to explain a single SNP. Checks: compare cases and controls separately; examine the raw intensity data and call rates; genotype with an independent method; look for a copy-number change and for Mendelian inconsistencies in families; compute $F$ genome-wide.

15. In a moth population in Hardy–Weinberg equilibrium, the light color is recessive to dark. Among 10 000 moths, 1600 are light. (a) What are the allele frequencies? (b) How many moths are heterozygous? (c) What fraction of the dark moths are heterozygous?

    **Answer** (a) $q = \sqrt{0.16} = 0.4$, $p = 0.6$ (Formula 22.2.1). (b) $2pq \cdot 10\,000 = 0.48 \cdot 10\,000 = 4800$. (c) Dark moths: $p^2 + 2pq = 0.84$; heterozygous fraction $0.48/0.84 = 4/7 \approx 0.57$.

16. A sample of 400 women and 400 men is typed for an X-linked marker with alleles $A$ and $a$: women $AA$ 260, $Aa$ 120, $aa$ 20; men $A$ 290, $a$ 110. (a) Estimate the frequency of $a$ by gene counting. (b) Estimate it separately in each sex. (c) Are the women's genotype frequencies consistent with Hardy–Weinberg proportions at their own allele frequency?

    **Answer** (a) $\hat q = (2 \cdot 20 + 120 + 110)/(2 \cdot 400 + 400) = 270/1200 = 0.225$ (Formula 22.2.4). (b) Women $(40 + 120)/800 = 0.200$; men $110/400 = 0.275$. (c) With $q_f = 0.2$, expected $256 : 128 : 16$; $X^2 = 16/256 + 64/128 + 16/16 = 0.06 + 0.50 + 1.00 = 1.56$ with 1 df, $p = 0.21$: consistent. The difference between the sexes ($0.20$ vs $0.275$) is larger than the sampling error would usually give (a two-sample test gives $z \approx 2.9$) and could reflect recent immigration; Theorem 22.2.2 predicts that it halves in each generation.

17. In a population in Hardy–Weinberg equilibrium for the ABO blood groups, $9\,\%$ of people have group O and the frequency of $I^{A}$ is $0.2$. What are the frequencies of groups A, B and AB?

    **Answer** $r = \sqrt{0.09} = 0.3$, so $q = 1 - 0.2 - 0.3 = 0.5$. Group A: $p^2 + 2pr = 0.04 + 0.12 = 0.16$; B: $q^2 + 2qr = 0.25 + 0.30 = 0.55$; AB: $2pq = 0.20$; O: $0.09$; total $1.00$.

18. An X-linked dominant disorder affects 2 in 10 000 men. (a) Assuming equilibrium, what fraction of women are affected? (b) What is the ratio of affected women to affected men? (c) Among the children of an affected man and an unaffected woman, which are affected?

    **Answer** (a) $q = 2 \times 10^{-4}$; affected women $q(2 - q) = 4.0 \times 10^{-4}$. (b) $2 - q \approx 2$: almost twice as many women as men. (c) All his daughters (they receive his X) and none of his sons (they receive his Y).
