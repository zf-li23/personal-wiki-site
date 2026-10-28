---
title: "Mendel's Laws: Segregation and Independent Assortment"
description: Blending versus particulate inheritance; Mendel's experimental design and his seven pea traits; monohybrid crosses, the law of segregation, the F3 test and the testcross; dihybrid crosses and the law of independent assortment; a probability toolkit for crosses with many genes (product and sum rules, branch diagrams, counting rules, binomial and multinomial probabilities, conditional probabilities); χ² tests of genetic ratios and the controversy over Mendel's data; and the molecular identity of Mendel's genes.
---

Gregor Mendel's paper of 1866 (read to the Natural History Society of Brünn in 1865) is the founding document of genetics. From crosses between varieties of the garden pea he inferred that heredity is carried by discrete factors that come in pairs, separate cleanly when gametes form and combine at random at fertilization; and that the factors for different traits are distributed independently of one another. These two statements, the law of segregation and the law of independent assortment, explain the 3:1 and 9:3:3:1 ratios that appear among the progeny of hybrids, and they turn the prediction of offspring into a calculation with probabilities. This chapter follows Mendel's experiments and reasoning, develops the probability toolkit that the laws imply and that every later chapter uses, shows how to test a ratio statistically, and ends with the molecular identity of Mendel's genes.

The previous chapter (7.4.1) introduced the logic of inference from crosses; the physical basis of both laws, the behavior of chromosomes at meiosis ([7.3.21](/7.3.21)), is the subject of 7.4.5, and the main exception to independent assortment, linkage, of 7.4.8. The probability theory used here is developed in [3.1](/3.1): conditional probability in [3.1.2](/3.1.2), the binomial distribution in [3.1.4](/3.1.4#sec-4.1.3) and the multinomial distribution in [3.1.6](/3.1.6#sec-6.2.3); the χ² goodness-of-fit test in [3.2.6](/3.2.6#sec-6.3).

## 2.1. The Problem Mendel Solved

### 2.1.1. Blending and Particulate Inheritance

Before Mendel, the dominant idea was that parental traits blend in the offspring, as two paints mix. Blending explains why children often look intermediate, but it cannot explain why a trait absent in the parents reappears in a grandchild, and it has a quantitative consequence that is fatal to it as a theory of heredity.

**Formula 2.1.1 (Loss of Variation Under Blending)** Suppose that an offspring's value of a trait is the mean of its parents' values, $Z = \tfrac12(X + Y)$, with $X$ and $Y$ the values of two randomly mating parents, independent with variance $\sigma^2$. Then $\operatorname{Var}(Z) = \tfrac14(\sigma^2 + \sigma^2) = \tfrac12\sigma^2$, so after $t$ generations of random mating without new variation

$$
\sigma_t^2 = \frac{\sigma_0^2}{2^t}.
$$

Variation would be halved every generation and would practically disappear within ten (a factor $2^{-10} \approx 10^{-3}$). This was the objection that the engineer Fleeming Jenkin raised against Darwin in 1867: under blending, natural selection would have no variation left to act on. Real populations keep their variation from generation to generation. Particulate inheritance resolves the paradox: if heredity is carried by discrete factors that are transmitted unchanged, the factors are reshuffled every generation but not diluted, and the variation is conserved (the Hardy–Weinberg principle makes this precise, 7.4.22). Mendel's experiments demonstrated particulate inheritance directly.

### 2.1.2. Mendel's Experimental Design

Mendel's success came from his design more than from his choice of organism, although the pea suited him well. The garden pea, *Pisum sativum*, normally self-fertilizes (the flower closes around its own pollen), but it can be cross-fertilized by removing the anthers of one flower and dusting its stigma with pollen from another; it grows in one season and gives many seeds per plant; and seed traits (shape, color) can be scored on the seeds themselves, hundreds per plant. Mendel did not hunt for mutants: he obtained 34 varieties from seed merchants, tested them for two years for constancy, and chose seven traits, each with two clearly distinct forms.

**Definition 2.1.1 (Crosses and Generations)** A line is **true-breeding** (pure-breeding) for a trait if its self-fertilized or intercrossed progeny show the same form of the trait generation after generation. In a cross, the true-breeding parents form the parental generation P; their progeny is the first filial generation $\mathrm{F}_1$, and the progeny of $\mathrm{F}_1$ individuals crossed or self-fertilized among themselves is the second filial generation $\mathrm{F}_2$ (and so on). A **reciprocal cross** is the pair of crosses in which the phenotypes of the female and male parents are interchanged (white female × purple male, and purple female × white male).

Reciprocal crosses ask whether it matters which parent transmits a trait. For all seven of Mendel's traits it did not: the egg and the pollen contribute equally. (Exceptions to this rule, sex linkage and maternal inheritance, are the subjects of 7.4.6 and 7.4.11.)

| Trait | Dominant form | Recessive form | $\mathrm{F}_2$ dominant | $\mathrm{F}_2$ recessive | Ratio |
|---|---|---|---|---|---|
| Seed shape | round | wrinkled | 5 474 | 1 850 | 2.96 : 1 |
| Seed (cotyledon) color | yellow | green | 6 022 | 2 001 | 3.01 : 1 |
| Flower (and seed coat) color | purple (gray seed coat) | white (white seed coat) | 705 | 224 | 3.15 : 1 |
| Pod shape | inflated | constricted | 882 | 299 | 2.95 : 1 |
| Pod color (unripe) | green | yellow | 428 | 152 | 2.82 : 1 |
| Flower position | axial | terminal | 651 | 207 | 3.14 : 1 |
| Stem length | tall | dwarf | 787 | 277 | 2.84 : 1 |

The table gives Mendel's $\mathrm{F}_2$ counts. Three features of his approach were new: he started from true-breeding lines, he followed each trait separately before combining them, and he counted every progeny and interpreted the counts as ratios.

## 2.2. Monohybrid Crosses and the Law of Segregation

### 2.2.1. The Observations

In each of the seven crosses between true-breeding lines, Mendel observed:

1. the $\mathrm{F}_1$ plants all showed one of the two parental forms (purple, round, yellow), never an intermediate, whichever way the cross was made;
2. in the $\mathrm{F}_2$, obtained by self-fertilizing the $\mathrm{F}_1$, the other form reappeared, unchanged, in about one quarter of the plants;
3. the ratio of the two forms in the $\mathrm{F}_2$ was close to 3:1 for every trait.

The form shown by the $\mathrm{F}_1$ he called dominant, the one that disappeared and reappeared recessive. The reappearance of the recessive form, unaltered, shows that the $\mathrm{F}_1$ carried the factor for it although it did not express it: the factors did not blend.

### 2.2.2. Mendel's Model and Its Vocabulary

Mendel explained the observations with a model in which each plant carries two factors for each trait, one received from each parent; each gamete carries one of them; and gametes combine at random. In modern terms:

**Definition 2.2.1 (Gene, Allele, Locus)** The hereditary factor that determines a trait is a **gene** ([7.2.1](/7.2.1)). The alternative forms of a gene are its **alleles**; in a diploid each individual carries two alleles of each autosomal gene, which may be the same or different. The position of a gene on a chromosome is its **locus** (plural loci).

**Definition 2.2.2 (Genotype and Phenotype)** The **genotype** of an individual is the pair of alleles it carries at a locus (or, more generally, its allelic constitution at the loci under consideration); the **phenotype** is the observable form of the trait. An individual with two identical alleles at a locus ($YY$ or $yy$) is a **homozygote** (it is homozygous at that locus); one with two different alleles ($Yy$) is a **heterozygote** (heterozygous).

**Definition 2.2.3 (Dominant and Recessive)** An allele is **dominant** if the heterozygote has the same phenotype as the homozygote for that allele, and **recessive** if its phenotype is seen only in homozygotes. Dominance is a relation between two alleles with respect to a phenotype; it is not a property of an allele alone (7.4.3).

**Definition 2.2.4 (Monohybrid Cross)** A **monohybrid cross** is a cross between individuals heterozygous at one locus under study (for example the $\mathrm{F}_1$ of two true-breeding lines that differ in one trait, $Yy \times Yy$).

**Definition 2.2.5 (Law of Segregation)** The **law of segregation** (Mendel's first law): the two alleles of a gene in a diploid separate (segregate) from each other during the formation of gametes, so that each gamete receives one allele, and each allele is received by half of the gametes; gametes combine at random at fertilization.

The predictions follow by enumerating the gametes. A $Yy$ plant makes $Y$ and $y$ gametes with probability $\tfrac12$ each, on both the egg and the pollen side; random union gives

$$
\left(\tfrac12 Y + \tfrac12 y\right)^2 = \tfrac14\, YY + \tfrac12\, Yy + \tfrac14\, yy,
$$

a genotypic ratio of 1:2:1 and, because $YY$ and $Yy$ look alike, a phenotypic ratio of 3:1. The enumeration is conventionally drawn as a table.

**Definition 2.2.6 (Punnett Square)** A **Punnett square** (R. C. Punnett, 1905) is a table whose columns are the gametes of one parent and whose rows are those of the other, each with its probability; each cell is the zygote formed by the union of its row and column gametes, and has the product of their probabilities.

![The monohybrid cross. Left: true-breeding yellow (YY) and green (yy) parents give an all-yellow F1 (Yy); self-fertilization of the F1 gives the F2. Middle: the Punnett square of Yy × Yy, with the egg cells on the left and the pollen on top; three of the four equally likely cells contain at least one Y and are yellow. Right: the F3 test. Each yellow F2 plant is self-fertilized and its progeny classified; one third of the yellow F2 plants (YY) give only yellow progeny and two thirds (Yy) give yellow and green in 3:1, Mendel's 166 and 353 plants](./plots/monohybrid-cross.py)

### 2.2.3. Testing the Model: the F3 and the Testcross

A good model predicts things it was not built to explain. Mendel's model predicts that the dominant $\mathrm{F}_2$ class is a mixture: one third $YY$, two thirds $Yy$.

**Formula 2.2.1 (Genotype Given a Dominant Phenotype)** In the $\mathrm{F}_2$ of a monohybrid cross with complete dominance,

$$
\mathbb{P}(Yy \mid \text{dominant phenotype}) = \frac{\mathbb{P}(Yy)}{\mathbb{P}(YY) + \mathbb{P}(Yy)} = \frac{1/2}{3/4} = \frac23, \qquad \mathbb{P}(YY \mid \text{dominant}) = \frac13.
$$

This is a **conditional probability** ([3.1.2](/3.1.2#sec-2.3)): knowing the phenotype excludes $yy$ and renormalizes the rest. It is used in almost every genetic calculation in which an individual's phenotype, but not its genotype, is known (7.4.7).

**Example 2.2.1 (Mendel's F3 test)** Mendel self-fertilized 565 round-seeded $\mathrm{F}_2$ plants and examined their seeds: 193 gave only round seeds and 372 gave round and wrinkled in about 3:1, a ratio of 1:1.93. For seed color, 166 of 519 yellow plants bred true and 353 segregated (1:2.13). The expected counts for 1:2 are $188.3 : 376.7$ and $173 : 346$; the χ² values (2.5.1) are $0.17$ and $0.42$ with one degree of freedom, both consistent with the model. Recessive $\mathrm{F}_2$ plants, as predicted, bred true.

A more direct test of an individual's genotype is to cross it with the recessive homozygote, whose gametes carry only the recessive allele, so that every progeny's phenotype shows which allele it received from the tested parent.

**Definition 2.2.7 (Testcross)** A **testcross** is a cross between an individual of dominant phenotype and unknown genotype and a homozygous recessive individual. If the tested individual is homozygous dominant, all progeny show the dominant phenotype; if it is heterozygous, half show the dominant and half the recessive phenotype (1:1).

**Example 2.2.2** A purple-flowered plant of unknown genotype is testcrossed with a white-flowered plant. (a) All of 20 progeny are purple. If the plant were heterozygous, the probability of this would be $(1/2)^{20} \approx 9.5 \times 10^{-7}$, so it is homozygous $PP$ beyond reasonable doubt. (b) With only 3 progeny, all purple, the probability under heterozygosity is $(1/2)^3 = 1/8$, and the result is inconclusive. The testcross makes each gamete of the tested parent visible, which is why it is also the basic tool of linkage analysis (7.4.8).

## 2.3. Dihybrid Crosses and the Law of Independent Assortment

### 2.3.1. Two Traits at Once

Do the factors for different traits travel together, as they came from the parents, or separately? Mendel crossed true-breeding round yellow ($RRYY$) plants with wrinkled green ($rryy$) plants. The $\mathrm{F}_1$ were round yellow ($RrYy$).

**Definition 2.3.1 (Dihybrid Cross)** A **dihybrid cross** is a cross between individuals heterozygous at two loci under study, such as the self-fertilization of the $RrYy$ $\mathrm{F}_1$.

Among 556 $\mathrm{F}_2$ seeds Mendel counted 315 round yellow, 108 round green, 101 wrinkled yellow and 32 wrinkled green: a ratio close to 9:3:3:1, with two new combinations (round green and wrinkled yellow) that neither grandparent had. Looked at one trait at a time, the counts are $423 : 133$ round to wrinkled ($3.18:1$) and $416 : 140$ yellow to green ($2.97:1$): each gene still segregates 3:1. And 9:3:3:1 is exactly the product $(3:1) \times (3:1)$:

$$
\left(\tfrac34 R\_ + \tfrac14 rr\right)\left(\tfrac34 Y\_ + \tfrac14 yy\right) = \tfrac{9}{16} R\_Y\_ + \tfrac{3}{16} R\_yy + \tfrac{3}{16} rrY\_ + \tfrac{1}{16} rryy .
$$

**Definition 2.3.2 (Law of Independent Assortment)** The **law of independent assortment** (Mendel's second law): during gamete formation, the segregation of the alleles of one gene is independent of the segregation of the alleles of another gene. A dihybrid $RrYy$ therefore makes four kinds of gametes, $RY$, $Ry$, $rY$ and $ry$, in equal proportions (1:1:1:1).

![The dihybrid cross RrYy × RrYy. Each parent makes four kinds of gametes in equal proportions (circles); the 16 equally likely combinations give nine genotypes and four phenotypes in the ratio 9:3:3:1. Cells are colored by phenotype; the round green and wrinkled yellow classes are the new combinations](./plots/dihybrid-punnett.py)

Mendel tested the law with a dihybrid testcross. $RrYy \times rryy$ should give the four gametic types of the dihybrid directly, in a 1:1:1:1 ratio; with the dihybrid as the seed parent he obtained 31 round yellow, 26 round green, 27 wrinkled yellow and 26 wrinkled green ($\chi^2 = 0.62$, three degrees of freedom, $p = 0.89$). He also carried out a trihybrid cross ($RrYyAa$ selfed) and found the classes expected from $(3:1)^3 = 27:9:9:9:3:3:3:1$.

Independent assortment holds for genes on different chromosomes and for genes far apart on the same chromosome; genes close together on one chromosome are linked and violate it (7.4.8). Several of Mendel's seven genes lie on the same pea chromosome, but the pairs he combined in the dihybrid crosses he reported lie on different chromosomes or far enough apart to assort almost independently.

### 2.3.2. Branch Diagrams

For more than two genes a Punnett square becomes unwieldy ($2^3 \times 2^3 = 64$ cells for a trihybrid). Because the genes assort independently, the progeny of each gene can be treated separately and the results multiplied; a branch diagram (forked-line method) lays out this calculation.

![The branch diagram for the dihybrid cross RrYy × RrYy. Left: phenotypes; the first fork gives the outcomes for seed shape (3/4 round, 1/4 wrinkled), and each branch forks again for seed color (3/4 yellow, 1/4 green); the probability of each path is the product along it, giving 9/16, 3/16, 3/16, 1/16. Right: the same diagram for genotypes, with three outcomes per gene (1/4, 1/2, 1/4) and nine genotypes](./plots/branch-diagram.py)

## 2.4. A Probability Toolkit for Crosses

Mendel's laws turn the prediction of offspring into probability calculations, and the following rules cover most of them. All of them rest on two facts: each locus segregates 1:1 in a heterozygote, and unlinked loci assort independently.

### 2.4.1. Product and Sum Rules

**Formula 2.4.1 (Product and Sum Rules)** For independent events $A$ and $B$ (outcomes at unlinked loci, or the gametes from two different parents), $\mathbb{P}(A \cap B) = \mathbb{P}(A)\,\mathbb{P}(B)$ (*product rule*). For mutually exclusive events (different genotypes of the same individual), $\mathbb{P}(A \cup B) = \mathbb{P}(A) + \mathbb{P}(B)$ (*sum rule*). The probability of a genotype at one locus is a sum over the ways it can arise; for example, $\mathbb{P}(Aa)$ from $Aa \times Aa$ is $\mathbb{P}(A \text{ from egg}, a \text{ from pollen}) + \mathbb{P}(a \text{ from egg}, A \text{ from pollen}) = \tfrac14 + \tfrac14 = \tfrac12$.

**Algorithm 2.4.1 (Locus by Locus)** To find the probability of a given genotype or phenotype among the progeny of a cross involving several unlinked genes:

1. split the cross into one single-gene cross per locus (for $AaBbCc \times AabbCC$: $Aa \times Aa$, $Bb \times bb$, $Cc \times CC$);
2. for each locus, find the probability of the required genotype or phenotype ($\mathbb{P}(aa) = \tfrac14$, $\mathbb{P}(B\_) = \tfrac12$, $\mathbb{P}(C\_) = 1$);
3. multiply the probabilities over loci (product rule);
4. if the required outcome can be reached in several mutually exclusive ways ("at least one recessive trait", "the same phenotype as either parent"), add the probabilities of the ways (sum rule), or compute the complement.

**Example 2.4.1** In the cross $aaBbCcDD \times AaBbccDd$:

- $\mathbb{P}(aabbccdd) = \tfrac12 \cdot \tfrac14 \cdot \tfrac12 \cdot 0 = 0$, since the first parent can give only $D$;
- the probability of the phenotype $aaB\_ccD\_$ is $\tfrac12 \cdot \tfrac34 \cdot \tfrac12 \cdot 1 = \tfrac{3}{16}$;
- the probability that a progeny has the genotype of the first parent, $aaBbCcDD$, is $\tfrac12 \cdot \tfrac12 \cdot \tfrac12 \cdot \tfrac12 = \tfrac1{16}$; of the second parent, $AaBbccDd$, also $\tfrac12 \cdot \tfrac12 \cdot \tfrac12 \cdot \tfrac12 = \tfrac1{16}$; the probability that it has the genotype of neither parent is $1 - \tfrac18 = \tfrac78$.

### 2.4.2. Counting Rules for Many Genes

**Formula 2.4.2 (Counting Rules)** For an individual heterozygous at $n$ unlinked loci, each with two alleles and complete dominance, self-fertilized or crossed with an identical individual:

| Quantity | Number or probability |
|---|---|
| kinds of gametes | $2^n$, each with probability $(1/2)^n$ |
| gamete combinations (cells of the Punnett square) | $4^n$ |
| genotypes among the progeny | $3^n$ |
| phenotypes among the progeny | $2^n$ |
| probability of the all-dominant phenotype | $(3/4)^n$ |
| probability of the all-recessive phenotype (and genotype) | $(1/4)^n$ |
| probability of being homozygous at every locus | $(1/2)^n$ |
| probability of a progeny with exactly $k$ dominant phenotypes | $\binom{n}{k}(3/4)^k(1/4)^{n-k}$ |
| phenotypic ratio | the expansion of $(3 + 1)^n$ |

For $n = 3$ the phenotypic ratio is $(3+1)^3 = 27 : 9 : 9 : 9 : 3 : 3 : 3 : 1$, grouped by the number of dominant traits as $27 : 27 : 9 : 1$. The last rows follow because the phenotypes at the different loci are independent Bernoulli trials with success probability $3/4$, so the number of dominant traits has a binomial distribution.

**Example 2.4.2** In the $\mathrm{F}_2$ of $AaBbCcDd \times AaBbCcDd$: the number of genotypes is $3^4 = 81$ and of phenotypes $2^4 = 16$; $\mathbb{P}(aabbccdd) = 1/256$; $\mathbb{P}(A\_B\_C\_D\_) = 81/256$; $\mathbb{P}(AaBbCcDd) = (1/2)^4 = 1/16$; the probability of exactly two dominant traits is $\binom42 (3/4)^2 (1/4)^2 = 54/256 = 27/128$.

### 2.4.3. Families and Samples: Binomial and Multinomial Probabilities

The rules above give the probability for one progeny. The distribution of a class among several independent progeny follows the **binomial distribution** ([3.1.4](/3.1.4#sec-4.1.3)) or, for several classes, the **multinomial distribution** ([3.1.6](/3.1.6#sec-6.2.3)).

**Formula 2.4.3 (Binomial and Multinomial Probabilities)** If each of $n$ progeny independently belongs to a class with probability $p$, the probability that exactly $k$ of them do is

$$
\binom{n}{k} p^k (1-p)^{n-k}.
$$

If there are classes $1, \dots, m$ with probabilities $p_1, \dots, p_m$, the probability of $k_1, \dots, k_m$ progeny in the classes ($k_1 + \cdots + k_m = n$) is

$$
\frac{n!}{k_1! \cdots k_m!}\, p_1^{k_1} \cdots p_m^{k_m}.
$$

**Example 2.4.3** Two heterozygous carriers of a recessive disease ($Aa \times Aa$) have four children. Each child is affected with probability $1/4$. The probability that exactly one is affected is $\binom41 (1/4)(3/4)^3 = 27/64 \approx 0.42$; that at least one is affected, $1 - (3/4)^4 = 175/256 \approx 0.68$; that the first two are unaffected and the last two affected (one particular order), $(3/4)^2 (1/4)^2 = 9/256$. Probabilities for specified birth orders are products; probabilities for numbers of children in classes, regardless of order, carry the binomial coefficient.

**Example 2.4.4** Six progeny of $AaBb \times AaBb$: the probability of 3 $A\_B\_$, 1 $A\_bb$, 1 $aaB\_$ and 1 $aabb$ is

$$
\frac{6!}{3!\,1!\,1!\,1!} \left(\frac{9}{16}\right)^3 \frac{3}{16} \cdot \frac{3}{16} \cdot \frac{1}{16} = 120 \times 0.178 \times 0.0352 \times 0.0625 \approx 0.047.
$$

Even the most probable composition of a small family is not very probable: exact Mendelian ratios are expected only on average.

### 2.4.4. Conditional Probabilities in Crosses

**Example 2.4.5** A round yellow $\mathrm{F}_2$ plant from $RrYy \times RrYy$ is chosen at random and self-fertilized. What is the probability that a given seed it produces is wrinkled green? The plant's genotype is unknown; at each locus it is heterozygous with probability $2/3$ (Formula 2.2.1), independently for the two loci. A wrinkled seed requires the plant to be $Rr$ (probability $2/3$) and the seed to be $rr$ (probability $1/4$), so $\mathbb{P}(rr) = \tfrac23 \cdot \tfrac14 = \tfrac16$; similarly $\mathbb{P}(yy) = \tfrac16$, and

$$
\mathbb{P}(\text{wrinkled green}) = \frac16 \cdot \frac16 = \frac1{36}.
$$

The probability that the plant is $RrYy$ is $(2/3)^2 = 4/9$, and if it is, $1/16$ of its seeds are wrinkled green: $\tfrac49 \cdot \tfrac1{16} = \tfrac1{36}$, the same answer by the **law of total probability**. Note that $\mathbb{P}(\text{wrinkled green} \mid \text{round yellow parent})$ is not $1/16$: the uncertainty about the parent's genotype must be carried through the calculation.

**Example 2.4.6** Two seeds from the same plant of Example 2.4.5 are both wrinkled. What is now the probability that a third seed is wrinkled? The first seed already shows that the parent is $Rr$, so the answer is $1/4$, not $1/6$. Progeny of the same parent are independent only given the parent's genotype; observing them updates the probabilities of that genotype (Bayes' theorem, 7.4.7).

## 2.5. Testing Hypotheses: the χ² Test

### 2.5.1. Goodness of Fit

Observed counts never match a ratio exactly, and a genetic hypothesis must be judged by how large a deviation chance can produce. The standard tool is Pearson's χ² **goodness-of-fit test** ([3.2.6](/3.2.6#sec-6.3.2)).

**Formula 2.5.1 (χ² Statistic)** For observed counts $O_1, \dots, O_k$ in $k$ classes and expected counts $E_i = n p_i$ under the hypothesis,

$$
\chi^2 = \sum_{i=1}^{k} \frac{(O_i - E_i)^2}{E_i},
$$

which, when the hypothesis is true and all $E_i$ are large (a usual rule is $E_i \ge 5$), has approximately the $\chi^2$ distribution with $k - 1$ **degrees of freedom** (one fewer for each parameter estimated from the data).

**Algorithm 2.5.1 (Testing a Genetic Ratio)**

1. State the hypothesis as a ratio (9:3:3:1) and convert it to class probabilities.
2. Compute the expected counts $E_i = n p_i$ from the total $n$; merge classes with $E_i < 5$ (and reduce $k$ accordingly).
3. Compute $\chi^2$ and the degrees of freedom $k - 1$.
4. Find the **p-value**, the probability of a $\chi^2$ at least as large under the hypothesis. If $p < 0.05$ (or another chosen level), reject the hypothesis; otherwise the data are consistent with it. The 5 % critical values are $3.84$, $5.99$, $7.81$, $9.49$ for 1, 2, 3, 4 degrees of freedom.
5. A non-rejection does not prove the hypothesis; other hypotheses may fit as well ([7.4.4](/7.4.4#sec-4.5) compares two of them).

**Example 2.5.1** Mendel's dihybrid counts 315, 108, 101, 32 ($n = 556$) under 9:3:3:1 have expected counts $312.75$, $104.25$, $104.25$, $34.75$, and

$$
\chi^2 = \frac{2.25^2}{312.75} + \frac{3.75^2}{104.25} + \frac{3.25^2}{104.25} + \frac{2.75^2}{34.75} = 0.016 + 0.135 + 0.101 + 0.218 = 0.47,
$$

with three degrees of freedom; $p = 0.93$. The deviations are well within chance.

The test needs counts, not percentages: 60 % versus an expected 75 % is strong evidence against 3:1 among 1 000 progeny ($\chi^2 = 120$) but none among 20 ($\chi^2 = 2.4$, $p = 0.12$). For small samples with two classes, the exact binomial probability of a deviation at least as large can be computed instead.

![The χ² test as a simulation. A: the fraction of recessive progeny in 10 000 simulated F2 families of 100 and of 1 000 progeny each, under a true 3:1 ratio; the spread shrinks as the binomial standard deviation √(p(1−p)/n). B: the χ² statistic of the same simulated families (bars) and the density of the χ² distribution with one degree of freedom (curve); 5 % of the simulated values exceed the critical value 3.84 (dashed line), as the test intends](./plots/chi-square-simulation.py)

### 2.5.2. Were Mendel's Data Too Good?

In 1936 R. A. Fisher, the founder of modern statistics and a great admirer of Mendel, reanalyzed all of Mendel's experiments. Summing the χ² values of all the experiments he obtained a total of about 42 on 84 degrees of freedom; if Mendel's hypotheses were true and the data honest samples, a total this small or smaller would occur with probability about $7 \times 10^{-5}$. The data, in other words, fit the ratios better than chance allows.

Fisher found a second, sharper problem in the $\mathrm{F}_3$ tests of plant traits. To classify a dominant $\mathrm{F}_2$ plant as homozygous or heterozygous, Mendel raised 10 progeny from each. A heterozygote fails to show any recessive among 10 progeny with probability $(3/4)^{10} = 0.056$, and would be misclassified as homozygous.

**Formula 2.5.2 (Misclassification in a Progeny Test)** If each heterozygote is classified from $m$ progeny and declared homozygous when no recessive appears, the expected fractions of dominant $\mathrm{F}_2$ plants classified as homozygous and heterozygous are

$$
\frac13 + \frac23\left(\frac34\right)^m \quad\text{and}\quad \frac23\left(1 - \left(\frac34\right)^m\right),
$$

which for $m = 10$ are $0.371$ and $0.629$ instead of $1/3$ and $2/3$.

Mendel's six plant-trait progeny tests (600 plants) gave 201 apparent homozygotes and 399 heterozygotes, closer to the uncorrected 1:2 ($200 : 400$) than to the expected $222.7 : 377.3$ ($\chi^2 = 3.3$, $p \approx 0.07$ against the corrected expectation).

The debate that followed has not established misconduct, and the view of most historians and statisticians who have reexamined it (A. W. F. Edwards, D. J. Fairbanks, A. Franklin and others) is that the data are probably not fabricated. Mendel's text does not say that every plant was tested with exactly 10 progeny, and if more progeny were used for some, the expected bias is smaller; the "too good" fit across experiments can arise from unconscious decisions about when to stop counting or which experiments to report (an experiment that stops when the ratio looks right is biased toward fitting), and from the classification of borderline seeds. Whatever the explanation, the conclusions stand: they have been confirmed millions of times since.

![Mendel's data against the χ² test. Each point is one of Mendel's experiments (the seven F2 monohybrid ratios, the two seed-trait and six plant-trait F3 progeny tests, the dihybrid F2 and the dihybrid testcross), plotted as its p-value against the value expected for the same rank if the p-values were uniformly distributed, as they would be for honest data from true hypotheses. Points above the diagonal fit better than expected; Mendel's experiments lie mostly above it, the pattern behind Fisher's criticism](./plots/mendel-p-values.py)

## 2.6. The Molecular Identity of Mendel's Genes

The genes behind four of Mendel's traits were identified between 1990 and 2010, and the genes for the remaining three were reported in 2025 from the genome sequences of several hundred pea accessions. They show what dominance usually means at the molecular level: the dominant allele encodes a functional product, the recessive one does not, and one functional copy is enough.

| Trait | Gene (Mendel's symbol) | Product | Recessive allele |
|---|---|---|---|
| Seed shape | $R$ | starch-branching enzyme SBEI, which converts unbranched amylose into branched amylopectin | $r$: a 0.8 kb transposable element inserted in the gene, no functional enzyme; seeds accumulate sucrose, take up water, and wrinkle when they dry |
| Cotyledon color | $I$ (often written $Y$) | SGR (stay-green), required to dismantle chlorophyll–protein complexes during seed maturation | $i$: loss-of-function alleles; chlorophyll is retained and the seeds stay green |
| Flower color | $A$ | a bHLH transcription factor that activates the anthocyanin pathway | $a$: a single-base change at an intron splice site, no functional protein; white flowers and seed coats |
| Stem length | $Le$ | gibberellin 3-oxidase, which makes active gibberellin $\mathrm{GA_1}$ | $le$: a single amino-acid substitution (Ala → Thr) that lowers enzyme activity; less $\mathrm{GA_1}$, short internodes |

In every case the heterozygote has half the amount of the functional product and looks like the dominant homozygote. Why half is usually enough, and when it is not, is a question of how pathways respond to enzyme amount (7.4.3). The $r$ allele is caused by the insertion of a **transposon** ([7.2.9](/7.2.9)), an early example of how such elements make mutations (7.4.17).

## 2.7. Kinds of Traits, and Why Mendel Succeeded

Mendel chose traits whose forms are clear-cut. Traits fall into three kinds:

| Kind | Values | Example | Inheritance |
|---|---|---|---|
| Categorical (discrete) | a few distinct classes | purple or white flowers; affected or unaffected by a disease | often simple Mendelian ratios; some are threshold traits with complex inheritance (7.4.24) |
| Meristic (counting) | whole numbers | number of eggs in a clutch, of bristles, of vertebrae | usually complex |
| Continuous | any value in a range | height, weight, milk yield | many genes plus environment (7.4.24) |

Mendel's choice of categorical traits each controlled by one gene with two alleles, one completely dominant, was essential: had he studied height in a variety with many height genes, he would have seen intermediate $\mathrm{F}_1$ and a continuous $\mathrm{F}_2$, and blending would have seemed confirmed. The later demonstration that continuous traits are the joint effect of many Mendelian genes ([7.4.4](/7.4.4#sec-4.6), 7.4.24) united the two kinds of inheritance.

His work was ignored for 34 years. He was not seen as a professional biologist; botanists of the time were not used to statistical arguments; hybridization experiments with other species (notably *Hieracium*, which Mendel himself tried on the advice of Carl Nägeli and which reproduces largely asexually) seemed to contradict him; and nothing was known about chromosomes that could give the factors a physical basis. In 1900 Hugo de Vries, Carl Correns and Erich von Tschermak independently obtained similar ratios and found Mendel's paper. Within three years the parallel between the behavior of Mendel's factors and of chromosomes at meiosis was recognized (7.4.5), and the questions Mendel could not answer (where genes are, what they are made of, how they act and how they explain continuous traits) became the program of twentieth-century genetics.

## Summary

| Topic | Result |
|---|---|
| Blending vs particulate inheritance | blending halves the variance each generation, $\sigma_t^2 = \sigma_0^2/2^t$ (Formula 2.1.1); particulate factors conserve it |
| Design (Definition 2.1.1) | **true-breeding** lines, P, $\mathrm{F}_1$, $\mathrm{F}_2$; **reciprocal crosses** gave identical results |
| Vocabulary (Definitions 2.2.1–2.2.3) | **gene**, **allele**, **locus**; **genotype**, **phenotype**; **homozygote**, **heterozygote**; **dominant**, **recessive** |
| **Law of segregation** (Definition 2.2.5) | $Yy$ gives $\tfrac12 Y$, $\tfrac12 y$ gametes; $Yy \times Yy$ gives 1:2:1 genotypes, 3:1 phenotypes; **Punnett square** (Definition 2.2.6) |
| Genotype of a dominant $\mathrm{F}_2$ | $\mathbb{P}(Yy \mid \text{dominant}) = 2/3$ (Formula 2.2.1); Mendel's $\mathrm{F}_3$ test (Example 2.2.1) |
| **Testcross** (Definition 2.2.7) | $\times$ recessive homozygote: all dominant (homozygote) or 1:1 (heterozygote) |
| **Law of independent assortment** (Definition 2.3.2) | $RrYy$ gives four gametes 1:1:1:1; **dihybrid cross** gives 9:3:3:1; testcross 1:1:1:1 |
| Toolkit | product and sum rules (Formula 2.4.1); locus by locus (Algorithm 2.4.1); $2^n$ gametes, $3^n$ genotypes, $2^n$ phenotypes, $(3+1)^n$ (Formula 2.4.2); binomial and multinomial (Formula 2.4.3); conditional probabilities (Examples 2.4.5, 2.4.6) |
| χ² test | $\chi^2 = \sum (O-E)^2/E$, $k-1$ degrees of freedom (Formula 2.5.1, Algorithm 2.5.1); Mendel's dihybrid: $\chi^2 = 0.47$, $p = 0.93$ |
| Fisher's critique | total $\chi^2 \approx 42$ on 84 df; progeny-test misclassification $(3/4)^{10}$ (Formula 2.5.2); probably bias in stopping and reporting, not fraud |
| Molecular basis | dominant alleles encode functional SBEI, SGR, a bHLH factor, GA 3-oxidase; recessive alleles lack function |

## Questions

1. Under blending inheritance (Formula 2.1.1), how many generations of random mating reduce the variance of a trait to less than 1 % of its initial value? What observation in Mendel's crosses is incompatible with blending regardless of the variance argument?

   **Answer** We need $2^{-t} < 0.01$, $t > \log_2 100 = 6.64$, so 7 generations. Independently of the variance, blending cannot explain the reappearance, unchanged, of the recessive form (white flowers, green seeds) in the $\mathrm{F}_2$ after it had disappeared in the $\mathrm{F}_1$.
2. In a cross of two heterozygous pea plants $Tt \times Tt$ (tall dominant over dwarf), what fraction of the progeny is (a) dwarf, (b) tall and heterozygous, (c) heterozygous among the tall? (d) If a tall progeny is testcrossed and gives 8 tall and 0 dwarf, what is the probability that it is nevertheless heterozygous? (Use the prior from (c) and Bayes' theorem.)

   **Answer** (a) $1/4$. (b) $1/2$. (c) $2/3$. (d) $\mathbb{P}(8\text{ tall} \mid Tt) = (1/2)^8 = 1/256$ and $\mathbb{P}(8\text{ tall} \mid TT) = 1$. The posterior is $\dfrac{(2/3)(1/256)}{(2/3)(1/256) + (1/3)(1)} = \dfrac{2/768}{2/768 + 256/768} = \dfrac{2}{258} = 0.0078$.
3. In the cross $AaBbCcDdEe \times AaBbCcDdEe$ (all loci unlinked, complete dominance), find (a) the number of kinds of gametes of each parent, (b) the number of genotypes and of phenotypes among the progeny, (c) the probability of the phenotype $A\_bbC\_D\_ee$, (d) the probability of a progeny heterozygous at all five loci, (e) the probability of a progeny showing exactly three dominant traits.

   **Answer** (a) $2^5 = 32$. (b) $3^5 = 243$ genotypes and $2^5 = 32$ phenotypes. (c) $(3/4)^3(1/4)^2 = 27/1024 \approx 0.026$. (d) $(1/2)^5 = 1/32$. (e) $\binom53 (3/4)^3 (1/4)^2 = 10 \times 27/1024 = 270/1024 \approx 0.264$.
4. For the cross $AaBbCC \times aaBbCc$, find the probability that a progeny (a) is $aabbCc$, (b) shows all three dominant traits, (c) shows the same phenotype as the first parent, (d) shows a phenotype different from both parents.

   **Answer** Loci separately: $Aa \times aa$ gives $\tfrac12 Aa$, $\tfrac12 aa$; $Bb \times Bb$ gives $\tfrac34 B\_$, $\tfrac14 bb$; $CC \times Cc$ gives $\tfrac12 CC$, $\tfrac12 Cc$, all $C\_$. (a) $\tfrac12 \cdot \tfrac14 \cdot \tfrac12 = \tfrac1{16}$. (b) $\tfrac12 \cdot \tfrac34 \cdot 1 = \tfrac38$. (c) The first parent is $A\_B\_C\_$: $\tfrac38$. (d) The second parent is $aaB\_C\_$, with probability $\tfrac12 \cdot \tfrac34 = \tfrac38$; the two parental phenotypes are different, so the probability of a different phenotype is $1 - \tfrac38 - \tfrac38 = \tfrac14$ (these are the $A\_bbC\_$ and $aabbC\_$ classes, $\tfrac18 + \tfrac18$).
5. Two parents are both heterozygous for a recessive disease allele. Among their five children, what is the probability that (a) none is affected, (b) exactly two are affected, (c) at least two are affected, (d) the first child is affected and the other four are not?

   **Answer** With $p = 1/4$: (a) $(3/4)^5 = 243/1024 = 0.237$. (b) $\binom52 (1/4)^2(3/4)^3 = 10 \times 27/1024 = 0.264$. (c) $1 - \mathbb{P}(0) - \mathbb{P}(1) = 1 - 0.237 - 5 \times (1/4)(3/4)^4 = 1 - 0.237 - 0.396 = 0.367$. (d) $(1/4)(3/4)^4 = 81/1024 = 0.079$ (a specified order, no binomial coefficient).
6. Among 400 $\mathrm{F}_2$ progeny of a dihybrid cross the counts are 220, 85, 70, 25. Test the hypothesis 9:3:3:1.

   **Answer** Expected: 225, 75, 75, 25. $\chi^2 = 25/225 + 100/75 + 25/75 + 0/25 = 0.111 + 1.333 + 0.333 + 0 = 1.78$, with 3 degrees of freedom ($p = 0.62$). The 5 % critical value is 7.81: the data are consistent with 9:3:3:1.
7. A plant heterozygous for a recessive allele is self-fertilized and gives 70 dominant and 30 recessive progeny. (a) Test 3:1. (b) The same proportions are found among 1 000 progeny (700 : 300). Test again and explain the difference.

   **Answer** (a) Expected 75 : 25; $\chi^2 = 25/75 + 25/25 = 1.33$, $p = 0.25$: not rejected. (b) Expected 750 : 250; $\chi^2 = 2500/750 + 2500/250 = 13.3$, $p = 2.6 \times 10^{-4}$: rejected. The same proportional deviation is significant in a large sample because the sampling error shrinks as $1/\sqrt{n}$ while $\chi^2$ grows in proportion to $n$; possible causes of a real deficit of dominants are reduced viability of one genotype or misclassification.
8. A round yellow $\mathrm{F}_2$ plant from $RrYy \times RrYy$ is crossed with a wrinkled green plant. What is the probability that the first progeny is wrinkled green? Given that it is wrinkled green, what is the probability that the second progeny is also wrinkled green?

   **Answer** The plant is $Rr$ with probability $2/3$ and $Yy$ with probability $2/3$, independently. For a testcross progeny to be $rryy$ the plant must contribute $ry$: $\mathbb{P} = \tfrac23\cdot\tfrac12 \cdot \tfrac23\cdot\tfrac12 = \tfrac19$. A wrinkled green progeny proves that the plant is $RrYy$; the second progeny is then wrinkled green with probability $1/4$.
9. How many genotypes are possible at a locus with $k$ alleles in a diploid? How many genotypes are possible for three unlinked loci with 2, 3 and 4 alleles?

   **Answer** $k$ homozygotes and $\binom{k}{2}$ heterozygotes, $k(k+1)/2$ in total. For 2, 3 and 4 alleles: $3 \times 6 \times 10 = 180$ genotypes.
10. Using Formula 2.5.2, find the expected fractions of dominant $\mathrm{F}_2$ plants classified as homozygous if each is tested with 5, 10 and 20 progeny. How many progeny per plant are needed for the misclassification of heterozygotes to be below 1 %?

    **Answer** $\tfrac13 + \tfrac23(3/4)^m$: $m = 5$: $0.333 + 0.158 = 0.491$; $m = 10$: $0.371$; $m = 20$: $0.335$. Misclassification of a heterozygote is $(3/4)^m < 0.01$ for $m > \ln 0.01/\ln 0.75 = 16.0$, so 17 progeny.
11. Show that the χ² statistic for two classes with expected proportions $p$ and $1 - p$ equals $z^2$, where $z = (O_1 - np)/\sqrt{np(1-p)}$ is the standardized binomial count. Use it for Mendel's seed-shape data (5474 : 1850).

    **Answer** With $O_2 = n - O_1$, $(O_2 - E_2)^2 = (O_1 - E_1)^2 = d^2$, so $\chi^2 = d^2/(np) + d^2/(n(1-p)) = d^2/(np(1-p)) = z^2$. For seed shape, $n = 7324$, $np = 5493$, $d = -19$, $\sqrt{np(1-p)} = \sqrt{7324 \times 0.1875} = 37.06$, $z = -0.513$, $z^2 = 0.263$, matching the χ² computed directly ($p = 0.61$).
12. (Competition style.) A plant of genotype $AaBbCc$ is self-fertilized. (a) Among the progeny with the phenotype $A\_B\_C\_$, what fraction is true-breeding (homozygous at all three loci)? (b) If a progeny with phenotype $A\_B\_cc$ is chosen at random and crossed with an $aabbcc$ plant, what is the probability that its first progeny shows only the recessive phenotypes?

    **Answer** (a) $\mathbb{P}(AABBCC) = (1/4)^3 = 1/64$ and $\mathbb{P}(A\_B\_C\_) = 27/64$, so the fraction is $1/27$. (b) Given $A\_$, the plant is $Aa$ with probability $2/3$, and similarly for $B$; it is $cc$. The testcross progeny is $aabbcc$ if the plant contributes $abc$: $\tfrac23\cdot\tfrac12\cdot\tfrac23\cdot\tfrac12\cdot 1 = \tfrac19$.
