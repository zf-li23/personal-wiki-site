---
title: Pedigree Analysis and the Probability of Genetic Risk
description: Human genetics from family records. Pedigree symbols; recognizing autosomal dominant, autosomal recessive, X-linked and Y-linked inheritance and their complications; computing risks by chains of transmission; conditional probability and Bayes' theorem in genetic counseling (X-linked carriers, late-onset disease, carrier tests); consanguinity, identity by descent and the inbreeding coefficient by path counting; several traits at once; genetic counseling and testing.
---

In humans the experimenter cannot choose the crosses. Families are small, generations long, matings uncontrolled and pure-breeding lines nonexistent; the geneticist must work backward from the families that happen to exist. The tool is the **pedigree**, and the logic is Mendel's laws ([7.4.2](/7.4.2)) combined with the transmission of sex chromosomes ([7.4.6](/7.4.6)). This chapter has two halves. The first is qualitative: how to draw a pedigree and how to recognize the mode of inheritance of a trait from it. The second is quantitative and is the part most often tested in problems: how to compute the probability that a person is a carrier or that a child will be affected. Simple risks are products of transmission probabilities; risks that take account of everything known about a family are posterior probabilities, computed with **conditional probability** and Bayes' theorem ([3.1.2](/3.1.2#sec-2.3)). The same calculus, extended from single families to populations, gives the effects of consanguinity and leads to the inbreeding coefficient of population genetics ([7.4.22](/7.4.22)). Population carrier frequencies are taken here as given; the Hardy–Weinberg relation that produces them ($2pq$) is derived in [7.4.22](/7.4.22). Linkage analysis in human pedigrees, which uses the same probabilities with markers, follows in [7.4.14](/7.4.14).

## 7.1. Pedigrees

**Definition 7.1.1 (Pedigree and Proband)** A **pedigree** is a diagram of a family's relationships over several generations, in standard symbols, that records which members show a trait and, where known, their genotypes. The **proband** (propositus or index case) is the affected individual through whom the family first came to attention; the consultand is the person who seeks genetic counseling, who may or may not be affected.

The symbols follow the standardized nomenclature of the National Society of Genetic Counselors (Bennett and colleagues, 2008, updated 2022): squares for males, circles for females, diamonds for individuals of unspecified sex; filled symbols for affected individuals, a central dot for a heterozygous carrier who is not expected to manifest; a horizontal line between partners, a double line for a consanguineous union; a vertical line of descent to a horizontal sibship line, with siblings in birth order from left to right; a diagonal slash for a deceased person; an arrow (with P) for the proband. Generations are numbered with Roman numerals, individuals within a generation with Arabic numerals, so that "II-3" is the third individual of the second generation. Ages, genotypes and test results are written under the symbols.

Human pedigrees are informative in spite of their size because the same rules apply in every family: many small families, or several generations of one large family, add up to the samples that a single cross gives in an experimental organism. The study of a disease thus starts with collecting pedigrees, deciding the mode of inheritance, and then mapping the gene by linkage in the same families ([7.4.14](/7.4.14)).

## 7.2. Recognizing the Mode of Inheritance

Each mode of single-gene inheritance leaves a signature in pedigrees. For rare traits, which are the usual subject of pedigree analysis, the signatures are:

| Mode | Example | Who is affected | Transmission | Key test |
|---|---|---|---|---|
| autosomal dominant | Huntington disease, achondroplasia, Marfan syndrome | both sexes equally | every affected person has an affected parent (unless new mutation); an affected heterozygote transmits to half of the children; vertical pattern | male-to-male transmission excludes X-linkage |
| autosomal recessive | cystic fibrosis, phenylketonuria, sickle cell disease | both sexes equally | affected children usually have two unaffected carrier parents; one quarter of their siblings are affected; horizontal pattern, in one sibship | excess of consanguineous parents |
| X-linked recessive | hemophilia A, Duchenne muscular dystrophy, red-green color blindness | mostly males | passed from an affected man through all his daughters (carriers) to half of their sons; no father-to-son transmission; skips generations | sons of carrier women affected with probability $1/2$ |
| X-linked dominant | hypophosphatemic rickets | about twice as many females as males | affected men transmit to all daughters and no sons; affected women to half of their children | the daughters of an affected man |
| Y-linked | (no established example apart from male determination and fertility) | males only | from father to all sons | — |
| mitochondrial | Leber hereditary optic neuropathy | both sexes | only through the mother, to all (or a variable fraction) of her children | no transmission from men ([7.4.11](/7.4.11)) |

![Typical pedigrees of four modes of inheritance (filled: affected; central dot: carrier). A: autosomal dominant: affected individuals in every generation, transmission from affected parents of either sex to about half of their children, including father to son. B: autosomal recessive: the affected children have unaffected parents, here first cousins (double line), who are both carriers; the trait appears in one sibship. C: X-linked recessive: an affected man has carrier daughters (II-2, II-4), half of whose sons are affected; there is no father-to-son transmission. D: X-linked dominant: an affected man transmits the trait to all his daughters and none of his sons, while an affected woman transmits it to half of her children of either sex](./plots/inheritance-patterns.py)

**Algorithm 7.2.1 (Deciding the Mode of Inheritance)**

1. Is the trait transmitted only through mothers, to all their children? Consider mitochondrial inheritance.
2. Do affected children have two unaffected parents? If so, the trait is recessive (or a new mutation, or incompletely penetrant). If there are many affected males and no affected females, and the mothers' brothers or the maternal grandfathers are affected, it is probably X-linked recessive; otherwise autosomal recessive.
3. Is every affected person the child of an affected parent? Then the trait is probably dominant. If an affected father has an affected son, it is autosomal; if every daughter of an affected father is affected and every son unaffected, it is X-linked dominant.
4. Test the chosen hypothesis against every individual and mating of the pedigree; one counterexample (an affected son of an affected father under X-linkage; an affected child of two affected parents having an unaffected child under recessive inheritance) rejects it, unless one of the complications below can explain it.
5. When several hypotheses remain, compare their likelihoods: the probability of the observed pedigree under each mode (the logic of the LOD score, [7.4.14](/7.4.14)).

The patterns are clean only for rare, fully penetrant traits with a single cause. Real pedigrees are complicated by:

- incomplete **penetrance** and variable **expressivity** ([7.4.3](/7.4.3)): a dominant trait can skip a generation through an unaffected carrier;
- late onset: carriers of Huntington disease are unaffected until middle age, so young members cannot be classified (Section 7.4.3);
- new mutations: a dominant disease that strongly reduces reproduction, such as achondroplasia (about 80 % of cases are new mutations), appears without affected ancestors;
- **genetic heterogeneity** ([7.4.4](/7.4.4)): two deaf parents, each homozygous for a recessive mutation in a different gene, can have only hearing children;
- **phenocopies**: environmental causes that mimic the genetic phenotype;
- common recessive alleles: if the allele is frequent (blood groups, cystic fibrosis in some populations) a carrier often marries a carrier or an affected person, and a recessive trait can appear in consecutive generations (pseudodominance).

## 7.3. Risk by Chains of Transmission

### 7.3.1. Carriers

**Definition 7.3.1 (Carrier)** A **carrier** is an individual heterozygous for a recessive allele (autosomal, or X-linked in a female) who does not show the associated phenotype but can transmit the allele; by extension, a person who carries a dominant disease allele but is not (yet) affected because of incomplete or age-dependent penetrance.

Every risk calculation in a pedigree starts from what is certain and moves to what is uncertain.

**Algorithm 7.3.1 (Risk by a Chain of Transmission)**

1. Assign the genotypes that are certain: affected individuals, obligate carriers (the parents of a child with an autosomal recessive disease; the daughters of a man with an X-linked recessive disease; a woman with an affected son and an affected brother or maternal uncle).
2. For each uncertain individual on the path to the person at risk, write the probability of each genotype given the information above them in the pedigree, including their own phenotype.
3. Multiply the probabilities of transmission along the path: each heterozygous parent transmits a given allele with probability $1/2$.
4. Multiply by the probability that the final genotype gives the phenotype (penetrance), and sum over the independent ways in which the outcome can arise.

**Proposition 7.3.1 (The Unaffected Sibling of a Patient with a Recessive Disease)** If both parents are heterozygous $Aa$ for a fully penetrant recessive disease, an unaffected child is a carrier with probability $2/3$.

**Proof** The children are $AA$, $Aa$ and $aa$ with probabilities $1/4$, $1/2$, $1/4$. Knowing that the child is unaffected excludes $aa$, so $\mathbb{P}(Aa \mid \text{unaffected}) = \frac{1/2}{1/4 + 1/2} = \frac{2}{3}$. $\square$

The $2/3$ is the simplest conditional probability in genetics: the information "unaffected" changes the prior $1/2$ to $2/3$. Forgetting to condition on the phenotype of the person at risk is the commonest error in pedigree problems.

**Example 7.3.1** (a) A man whose brother has cystic fibrosis marries a woman whose sister has cystic fibrosis; neither is affected. The risk that their first child is affected is $\frac23 \cdot \frac23 \cdot \frac14 = \frac19$: both must be carriers and the child must receive $a$ from both. (b) If instead he marries an unrelated woman of European ancestry, among whom about 1 in 25 is a carrier, the risk is $\frac23 \cdot \frac{1}{25} \cdot \frac14 = \frac{1}{150}$. (c) If the couple of (a) already has an unaffected child, they are still at risk $1/9$ for the next child? No: the unaffected child carries information about the parents, and the risk must be recomputed by Bayes' theorem (Question 6).

### 7.3.2. Independent Traits and Combined Risks

When two traits are determined by unlinked autosomal loci, their transmission is independent (Proposition 5.3.1 of [7.4.5](/7.4.5)) and the probabilities multiply.

**Formula 7.3.1 (Two Independent Conditions)** If a child is affected by condition 1 with probability $p_1$ and by condition 2 with probability $p_2$, independently, then

| Outcome | Probability |
|---|---|
| both conditions | $p_1 p_2$ |
| condition 1 only | $p_1 (1 - p_2)$ |
| condition 2 only | $(1 - p_1) p_2$ |
| exactly one condition | $p_1 + p_2 - 2p_1p_2$ |
| at least one condition | $1 - (1 - p_1)(1 - p_2) = p_1 + p_2 - p_1 p_2$ |
| neither | $(1 - p_1)(1 - p_2)$ |

**Example 7.3.2** A man with polydactyly (autosomal dominant, heterozygous $Pp$) and a woman with normal fingers have a child with albinism (autosomal recessive) and normal fingers. The parents must be $Pp\,Aa$ and $pp\,Aa$. For the next child $p_1 = \mathbb{P}(\text{polydactyly}) = 1/2$ and $p_2 = \mathbb{P}(\text{albinism}) = 1/4$, so both conditions $1/8$, polydactyly only $3/8$, albinism only $1/8$, exactly one $1/2$, neither $3/8$.

The rule fails when the loci are linked (the probabilities depend on the phase and the **recombination frequency**, [7.4.8](/7.4.8)) and, in particular, when both are X-linked: a woman heterozygous at two X-linked loci transmits her two X chromosomes as wholes, apart from crossing over. If her alleles $a$ and $b$ are on the same X (coupling) and the loci are closely linked, her sons are mostly either doubly affected or unaffected; if they are on different X chromosomes (repulsion), her sons are mostly affected by one condition or the other.

**Remark 7.3.1 (Whose Sex Is Given?)** Problems distinguish "the probability that a son is affected" from "the probability that a child is an affected son". The first is conditional on the child being male; the second includes the probability $1/2$ that the child is male:

$$
\mathbb{P}(\text{affected son}) = \mathbb{P}(\text{son})\,\mathbb{P}(\text{affected} \mid \text{son}) = \tfrac12\,\mathbb{P}(\text{affected} \mid \text{son}).
$$

For a carrier mother of an X-linked recessive disease, $\mathbb{P}(\text{affected} \mid \text{son}) = 1/2$ and $\mathbb{P}(\text{affected son}) = 1/4$. For an autosomal disease the sex of the child is independent of the genotype, so $\mathbb{P}(\text{affected} \mid \text{son}) = \mathbb{P}(\text{affected})$; in Example 7.3.2 a son has both conditions with probability $1/8$, and the probability that the next child is a son with both conditions is $1/16$.

## 7.4. Conditional Probability and Bayes' Theorem

### 7.4.1. The Bayesian Table

Much of the information in a pedigree is negative: unaffected sons, unaffected adults past the age of onset, negative tests. Such information does not settle a genotype, but it changes its probability. The calculation is an application of Bayes' theorem ([Theorem 2.6.1](/3.1.2#thm-2.6.1)) with the genotypes as the partition, and genetic counselors arrange it as a table.

**Algorithm 7.4.1 (Bayesian Risk Table)** Let $H_1, \dots, H_m$ be the possible genotypes (hypotheses) of the person of interest and $D$ the observed data (phenotypes of relatives, test results) not yet used.

1. Prior: $\mathbb{P}(H_i)$, from the pedigree above the person (Algorithm 7.3.1), without using $D$.
2. Conditional: $\mathbb{P}(D \mid H_i)$, the probability of the data under each hypothesis; for independent observations (several children) it is a product.
3. Joint: $\mathbb{P}(H_i)\,\mathbb{P}(D \mid H_i)$.
4. Posterior: $\mathbb{P}(H_i \mid D) = \dfrac{\mathbb{P}(H_i)\,\mathbb{P}(D \mid H_i)}{\sum_j \mathbb{P}(H_j)\,\mathbb{P}(D \mid H_j)}$, the joint divided by the sum of the joints (the **law of total probability** for $\mathbb{P}(D)$).
5. The risk to a child is computed from the posterior, not from the prior.

The same calculation can be done with natural frequencies: imagine many women in the same position, count how many of each genotype would show the data, and take proportions. The result is the same and is often easier to check.

### 7.4.2. X-Linked Carrier Risk

**Example 7.4.1** A woman's brother has Duchenne muscular dystrophy, and her mother is an obligate carrier (she also has an affected brother). Ignoring new mutations, the woman is a carrier with prior probability $1/2$. She has three unaffected sons. Is she still at risk $1/4$ for each future son?

| | Carrier | Not a carrier |
|---|---|---|
| prior | $1/2$ | $1/2$ |
| conditional: 3 unaffected sons | $(1/2)^3 = 1/8$ | $1$ |
| joint | $1/16$ | $1/2$ |
| posterior | $\dfrac{1/16}{1/16 + 1/2} = \dfrac19$ | $\dfrac89$ |

Her probability of being a carrier is $1/9$, and the risk that her next son is affected is $\frac19\cdot\frac12 = \frac{1}{18}$, not $1/2 \cdot 1/2 = 1/4$ for a son.

**Formula 7.4.1 (Carrier Probability After Unaffected Sons)** For a woman with prior carrier probability $\pi$ for a fully penetrant X-linked recessive disease and $k$ unaffected sons,

$$
\mathbb{P}(\text{carrier} \mid k \text{ unaffected sons}) = \frac{\pi\,2^{-k}}{\pi\,2^{-k} + 1 - \pi}, \qquad \text{for } \pi = \tfrac12:\ \frac{1}{1 + 2^k}.
$$
Daughters give no information about her (they are unaffected either way), and affected sons make her an obligate carrier.

![Bayesian revision of carrier risk. A: a woman whose brother has an X-linked recessive disease is a carrier with prior probability 1/2; each unaffected son halves the odds that she is a carrier, so the posterior falls as 1/(1 + 2^k) with k unaffected sons (1/3, 1/5, 1/9, …), and the risk that her next son is affected is half of it. B: an unaffected sibling of a patient with an autosomal recessive disease (prior 2/3) who tests negative on a carrier panel that detects a fraction d of mutant alleles has a posterior carrier probability 2(1 − d)/(2(1 − d) + 1): 0.17 for d = 0.9 and 0.06 for d = 0.97](./plots/bayesian-carrier-risk.py)

In practice the prior must also account for new mutations. For a lethal X-linked recessive disease, a fraction of cases arise by new mutation in the mother's germline (about one third under mutation–selection equilibrium, Haldane's argument in [7.4.23](/7.4.23)), so the mother of an isolated case, with no other affected relatives, is not an obligate carrier; her prior is about $2/3$, and the Bayesian table then incorporates her unaffected sons and the results of carrier tests.

### 7.4.3. Late-Onset Disease

Huntington disease is autosomal dominant with nearly complete penetrance for alleles of 40 or more CAG repeats, but the symptoms begin on average at about 40–45 years (earlier with longer repeats; [7.4.12](/7.4.12)). An unaffected child of an affected parent is therefore not reassured by being healthy at 25, but is partly reassured at 60.

**Formula 7.4.2 (Age-Dependent Penetrance)** Let $F(t)$ be the probability that a carrier has developed the disease by age $t$. For a person with prior carrier probability $1/2$ who is unaffected at age $t$,

$$
\mathbb{P}(\text{carrier} \mid \text{unaffected at } t) = \frac{\frac12(1 - F(t))}{\frac12(1 - F(t)) + \frac12} = \frac{1 - F(t)}{2 - F(t)},
$$
and the prior risk for his or her child is half of this.

**Example 7.4.2** If half of carriers have shown symptoms by 45 ($F = 0.5$), an unaffected 45-year-old child of an affected parent is a carrier with probability $0.5/1.5 = 1/3$, and his child's risk is $1/6$. If 92 % of carriers have shown symptoms by 60, the posterior at 60 is $0.08/1.08 \approx 0.07$. Since the gene was identified (1993), presymptomatic testing can replace this calculation, but many people at risk choose not to be tested, and the Bayesian estimate remains the basis of their counseling.

![Age-dependent penetrance and posterior risk (illustrative parameters). A: cumulative probability F(t) that a carrier of a dominant late-onset allele has shown symptoms by age t, here a logistic distribution of the age at onset with mean 45 and scale 6 years. B: probability that the child of an affected parent is a carrier, given that the child is still unaffected at age t (solid; 0.48 at 30, 0.33 at 45, 0.07 at 60), and the risk for that person's own child (dashed, half as large)](./plots/late-onset-risk.py)

### 7.4.4. Tests That Detect Only Some Mutations

Carrier tests for recessive diseases with many alleles detect only a fraction $d$ (the detection rate, or sensitivity) of the mutant alleles; for cystic fibrosis panels of common variants $d$ ranges from about 0.9 in populations of northern European ancestry to much less in others, although full sequencing of *CFTR* raises it.

**Example 7.4.3** The unaffected brother of a patient with cystic fibrosis tests negative on a panel with $d = 0.9$. His prior is $2/3$ (Proposition 7.3.1). If he is a carrier, the test misses his mutant allele with probability $1 - d = 0.1$ (assuming his family's allele is a random one; if the family's mutation is known and tested, $d = 1$ for him). Posterior: $\frac{(2/3)(0.1)}{(2/3)(0.1) + (1/3)(1)} = \frac{1}{6} \approx 0.17$. If his partner, from a population with carrier frequency $1/25$, also tests negative, her posterior is $\frac{0.04 \times 0.1}{0.04 \times 0.1 + 0.96} \approx 0.0041$, and the risk for their child is $\frac16 \times 0.0041 \times \frac14 \approx 1.7\times10^{-4}$, about 1 in 5 800, instead of $\frac23 \times \frac1{25} \times \frac14 = 1/150$ before testing.

### 7.4.5. Incomplete Penetrance in Several Genotypes, and Natural Frequencies

When a phenotype occurs, with different probabilities, in more than one genotype (incomplete penetrance in carriers and phenocopies in non-carriers), the observation "affected" is evidence about the genotype rather than proof of it.

**Formula 7.4.3 (Genotype Given the Phenotype)** If genotypes $G_1, \dots, G_m$ have prior probabilities $\mathbb{P}(G_i)$ and the phenotype occurs in $G_i$ with probability (penetrance) $\pi_i$, then

$$
\mathbb{P}(G_i \mid \text{affected}) = \frac{\mathbb{P}(G_i)\,\pi_i}{\sum_j \mathbb{P}(G_j)\,\pi_j}, \qquad
\mathbb{P}(G_i \mid \text{unaffected}) = \frac{\mathbb{P}(G_i)(1 - \pi_i)}{\sum_j \mathbb{P}(G_j)(1 - \pi_j)} .
$$

Formula 3.5.1 of [7.4.3](/7.4.3#sec-3.5.1) is the special case with the phenotype in one genotype only.

**Example 7.4.4** A disease occurs in 50 % of people of genotype $Mm$ and in 5 % of people of genotype $mm$ (from other causes). A woman $Mm$ and a man $mm$ have an affected daughter. Before her phenotype is known she is $Mm$ or $mm$ with probability $1/2$ each; Formula 7.4.3 gives

$$
\mathbb{P}(Mm \mid \text{affected}) = \frac{\frac12 \cdot 0.5}{\frac12 \cdot 0.5 + \frac12 \cdot 0.05} = \frac{10}{11} \approx 0.91 .
$$

The same result by natural frequencies: of 200 such daughters, 100 are $Mm$, of whom 50 are affected, and 100 are $mm$, of whom 5 are affected; of the 55 affected daughters, 50 are $Mm$. The prior $1/2$ from Mendel's law becomes $10/11$ once the phenotype is known; it would be $1$ only if the disease never occurred in $mm$.

Posterior probabilities are passed down a pedigree like priors: once updated, a person's genotype probabilities are used for his or her descendants.

**Example 7.4.5** A woman (II-6) is the daughter of a carrier of hemophilia A and an unaffected father, so her prior carrier probability is $1/2$. She has six unaffected children, three sons and three daughters. Only the sons carry information about her: $\mathbb{P}(\text{3 unaffected sons} \mid \text{carrier}) = (1/2)^3$, and by Formula 7.4.1 her posterior is $\frac{1/16}{1/16 + 1/2} = 1/9$. One of her daughters (III-2, whose father is unaffected) is a carrier with probability $\frac19 \cdot \frac12 = \frac1{18}$, and her first son is affected with probability $\frac1{18} \cdot \frac12 = \frac1{36}$. If III-2 marries a man with hemophilia, the answer for her sons does not change (a son receives his X from the mother), but her daughters are then affected with probability $\frac1{18} \cdot \frac12 = \frac1{36}$ and are all at least carriers.

## 7.5. Consanguinity and Inbreeding

### 7.5.1. Identity by Descent

**Definition 7.5.1 (Consanguinity)** **Consanguinity** is relationship by descent from a common ancestor; a consanguineous mating is one between relatives, conventionally second cousins or closer.

Children of consanguineous matings are more often homozygous for rare recessive alleles, because both parents may have inherited the same allele from a common ancestor. Garrod noticed in 1902 that the parents of his patients with alkaptonuria were first cousins far more often than the few percent of first-cousin marriages in the British population would predict, and, advised by Bateson, concluded that the disease was a Mendelian recessive. The quantitative theory requires distinguishing two senses in which alleles are "the same".

**Definition 7.5.2 (Identity by Descent)** Two alleles are **identical by descent** (IBD) if they are both copies of one allele of a common ancestor, inherited through replication and transmission without intervening mutation. Alleles that have the same DNA sequence (or the same function) without such recent common origin are identical by state.

**Definition 7.5.3 (Inbreeding Coefficient and Coefficient of Relationship)** The **inbreeding coefficient** $F$ of an individual is the probability that its two alleles at a locus are identical by descent (Wright 1922; the probabilistic interpretation is due to Malécot and Cotterman). The kinship coefficient $\theta_{XY}$ of two individuals is the probability that an allele drawn at random from $X$ and an allele drawn at random from $Y$ at the same locus are identical by descent; it equals the inbreeding coefficient of a child of $X$ and $Y$. The **coefficient of relationship** $r_{XY} = 2\theta_{XY}$ (for non-inbred individuals) is the expected proportion of the genome that $X$ and $Y$ share identical by descent through their common ancestors.

Identity by descent is always relative to a reference population of founders, whose alleles are taken as not identical by descent; $F$ is the excess homozygosity over that population. The population-level inbreeding coefficient, and its effect on the genotype frequencies of a whole population ($p^2 + Fpq$, $2pq(1 - F)$, $q^2 + Fpq$), are treated in [7.4.22](/7.4.22).

### 7.5.2. The Path Method

**Formula 7.5.1 (Inbreeding Coefficient by Path Counting)** Let $I$ be an individual whose parents share common ancestors $A_1, A_2, \dots$. For each common ancestor and each pair of distinct lines of descent from it to the two parents of $I$ (an inbreeding loop) with no individual in common except the ancestor, let $n$ be the number of individuals in the loop, counting both parents and the ancestor but not $I$. Then

$$
F_I = \sum_{\text{loops}} \left(\frac{1}{2}\right)^{n} (1 + F_A),
\tag{7.1}
$$
where $F_A$ is the inbreeding coefficient of the common ancestor of the loop (zero if the ancestor is not inbred).

**Proof** Consider one loop with $n_1$ transmissions from the ancestor $A$ down to the father of $I$ and $n_2$ down to the mother, so $n = n_1 + n_2 + 1$. The allele that $I$ receives from its father descends from a particular one of $A$'s two alleles if each of the $n_1$ transmissions on the paternal line, and the transmission from the father to $I$, passed on the allele derived from $A$: probability $(1/2)^{n_1 + 1}$. The same holds for the maternal line with $n_2 + 1$ transmissions. Given that both alleles of $I$ come from $A$, they are IBD if they are copies of the same allele of $A$ (probability $1/2$) or copies of $A$'s two alleles that are themselves IBD (probability $\frac12 F_A$). Hence the loop contributes $(1/2)^{n_1 + n_2 + 2}(1 + F_A) = (1/2)^{n}(1 + F_A)$. Different loops (different ancestors, or different lines of descent) describe mutually exclusive events, because the alleles of $I$ can trace back to only one meeting point, so their contributions add. $\square$

![The inbreeding coefficient by path counting for the child (IV-1) of first cousins III-1 and III-2. The cousins' parents II-2 and II-3 are siblings, so there are two common ancestors, I-1 and I-2. The loop through I-1 (solid) and the loop through I-2 (dashed) each contain five individuals (III-1, II-2, the ancestor, II-3, III-2) and contribute (1/2)^5 each, so F = 2 (1/2)^5 = 1/16](./plots/first-cousin-paths.py)

| Relationship of the parents | Loops | $F$ of the child | $r$ of the parents |
|---|---|---|---|
| parent and child | 1 loop with $n = 2$ | $1/4$ | $1/2$ |
| full siblings | 2 loops with $n = 3$ | $1/4$ | $1/2$ |
| half siblings | 1 loop with $n = 3$ | $1/8$ | $1/4$ |
| uncle and niece (aunt and nephew) | 2 loops with $n = 4$ | $1/8$ | $1/4$ |
| double first cousins | 4 loops with $n = 5$ | $1/8$ | $1/4$ |
| first cousins | 2 loops with $n = 5$ | $1/16$ | $1/8$ |
| first cousins once removed | 2 loops with $n = 6$ | $1/32$ | $1/16$ |
| second cousins | 2 loops with $n = 7$ | $1/64$ | $1/32$ |

**Example 7.5.1** A woman is the child of half siblings, so her own inbreeding coefficient is $1/8$. Her son and her daughter (from different, unrelated fathers) have a child $T$. The only common ancestor of $T$'s parents is the woman, with one loop of $n = 3$; by Eq. (7.1) $F_T = (1/2)^3(1 + 1/8) = 9/64$, slightly more than the $1/8$ of a child of half siblings with a non-inbred common parent.

### 7.5.3. Risk of Recessive Disease

**Formula 7.5.2 (Recessive Disease in the Child of Relatives)** For a recessive allele with frequency $q$ in the population, a child with inbreeding coefficient $F$ is homozygous with probability

$$
\mathbb{P}(aa) = (1 - F)\,q^2 + F q = q^2 + F q(1 - q),
$$
since with probability $F$ its two alleles are IBD (one allele, mutant with probability $q$) and otherwise they are two independent draws. The relative risk compared with the child of unrelated parents is $1 + F(1 - q)/q \approx 1 + F/q$ for small $q$.

**Example 7.5.2** For phenylketonuria with $q = 0.01$ (incidence $10^{-4}$), the child of first cousins has risk $10^{-4} + \frac1{16}(0.01)(0.99) \approx 7.2\times10^{-4}$, a relative risk of about 7. For a rarer disease with $q = 0.001$ the risk is $10^{-6} + \frac{1}{16}(0.001)(0.999) \approx 6.3\times10^{-5}$, a relative risk of about 63. If 1 % of marriages are between first cousins, the fraction of all affected children of the rarer disease who are born to first cousins is $\frac{0.01 \times 6.3\times10^{-5}}{0.01 \times 6.3\times10^{-5} + 0.99 \times 10^{-6}} \approx 0.39$: the rarer the disease, the more its patients concentrate in consanguineous families, which is how Garrod recognized recessive inheritance.

The population figure of the formula applies to a couple about whom nothing else is known. When the family history is known, the pedigree itself gives the risk.

**Example 7.5.3** A man whose brother has an autosomal recessive disease marries his first cousin, the daughter of his father's sister; nobody else in the family is affected. The man is a carrier with probability $2/3$ (Proposition 7.3.1). His father is an obligate carrier, so one of the father's parents is a carrier, and the father's sister is a carrier with probability $1/2$ (ignoring the small chance of an allele entering from outside); her daughter is a carrier with probability $1/4$. The risk to their child is $\frac23 \cdot \frac14 \cdot \frac14 = \frac{1}{24}$, about 40 times the population risk if $q = 0.01$.

![Consanguinity and recessive disease. A: relative risk that the child of relatives is homozygous for a recessive allele of frequency q, compared with the child of unrelated parents, for F = 1/4 (siblings or parent and child), 1/16 (first cousins) and 1/64 (second cousins): it rises roughly as F/q for rare alleles. B: fraction of all affected children who are born to first cousins, when a fraction c of all marriages is between first cousins: for rare alleles most patients come from consanguineous families even if consanguineous marriages are uncommon](./plots/consanguinity-risk.py)

Inbreeding increases the frequency of homozygotes at every locus at once, and with them the expression of recessive deleterious alleles, the basis of inbreeding depression ([7.4.24](/7.4.24)). Consanguineous marriage remains common in many societies (more than 20 % of marriages in parts of the Middle East and South Asia); studies of first-cousin offspring find an excess of about 2–4 percentage points in birth defects and early mortality, which is substantial but much smaller than the popular estimate.

## 7.6. Genetic Counseling and Testing

**Definition 7.6.1 (Genetic Counseling)** **Genetic counseling** is the process of helping individuals and families understand the medical, psychological and familial implications of genetic contributions to disease: interpreting family and medical histories to assess the chance of occurrence or recurrence, educating about inheritance, testing, management, prevention and research, and supporting informed choices.

The counselor draws a pedigree of at least three generations, establishes the diagnosis and mode of inheritance, computes risks by the methods of Sections 7.3–7.5, and explains them. The aim is informed decision rather than direction: modern counseling is nondirective, and the choices (testing, reproduction, prenatal diagnosis) belong to the consultand. Several kinds of tests change the probabilities:

| Test | Sample and timing | What it gives |
|---|---|---|
| carrier screening | blood or saliva, before or during pregnancy | carrier status for recessive and X-linked diseases (panels or sequencing); detection rate $d < 1$ (Example 7.4.3) |
| presymptomatic and predictive testing | blood, adults at risk | genotype for late-onset dominant diseases (Huntington disease, hereditary cancers, [7.4.21](/7.4.21)) |
| noninvasive prenatal screening | cell-free fetal (placental) DNA in maternal blood, from 10 weeks | screening for trisomies and some other conditions by counting sequence reads; positive results confirmed by diagnostic testing |
| prenatal diagnosis | chorionic villus sampling (11–14 weeks) or amniocentesis (from 15 weeks) | the fetal karyotype or genotype, with a small procedure-related risk of miscarriage |
| preimplantation genetic testing | one or a few cells of embryos produced by in vitro fertilization, or polar bodies ([7.4.5](/7.4.5)) | selection of embryos without the familial mutation or aneuploidy ([7.4.14](/7.4.14)) |
| newborn screening | heel-prick blood | treatable conditions such as phenylketonuria, before symptoms |

The value of a test depends on the prior probability: a screening test with high sensitivity and specificity still yields mostly false positives when the condition is rare (the false-positive puzzle of [3.1.2](/3.1.2#sec-2.6.2)), which is why screening results are confirmed by diagnostic tests.

## Summary

- Pedigrees (Definition 7.1.1) use NSGC symbols; the proband brings the family to attention.
- Modes of inheritance are recognized by Algorithm 7.2.1 and the table of Section 7.2: male-to-male transmission excludes X-linkage; affected children of unaffected parents mean recessive inheritance; all daughters and no sons of an affected man mean X-linked dominance. Incomplete penetrance, late onset, new mutation, heterogeneity and phenocopies blur the patterns.
- Risks by chains of transmission (Algorithm 7.3.1): obligate genotypes first, then multiply transmission probabilities. Carriers (Definition 7.3.1); an unaffected sibling of a recessive patient is a carrier with probability $2/3$ (Proposition 7.3.1). Independent conditions combine by Formula 7.3.1; linked or X-linked loci do not. $\mathbb{P}(\text{affected son}) = \tfrac12\,\mathbb{P}(\text{affected} \mid \text{son})$ (Remark 7.3.1).
- Bayesian revision (Algorithm 7.4.1): prior × conditional = joint, normalized to the posterior; risks come from the posterior.

  | Situation | Posterior carrier probability |
  |---|---|
  | X-linked, prior $1/2$, $k$ unaffected sons | $1/(1 + 2^k)$ (Formula 7.4.1) |
  | dominant late onset, prior $1/2$, unaffected at age $t$ | $(1 - F(t))/(2 - F(t))$ (Formula 7.4.2) |
  | recessive, prior $\pi$, negative test with detection rate $d$ | $\pi(1 - d)/[\pi(1 - d) + 1 - \pi]$ (Example 7.4.3) |
  | phenotype in several genotypes with penetrances $\pi_i$, affected | $\mathbb{P}(G_i)\pi_i/\sum_j \mathbb{P}(G_j)\pi_j$ (Formula 7.4.3; natural frequencies, Example 7.4.4) |

  Posteriors are passed down the pedigree as priors for descendants (Example 7.4.5).

- Consanguinity (Definition 7.5.1) and identity by descent (Definition 7.5.2); inbreeding coefficient, kinship and the coefficient of relationship $r = 2\theta$ (Definition 7.5.3); path method $F = \sum (1/2)^n (1 + F_A)$ (Formula 7.5.1, Eq. (7.1)): first cousins $1/16$, half siblings and uncle–niece $1/8$, full siblings $1/4$, second cousins $1/64$.
- Recessive risk in the child of relatives $q^2 + Fq(1 - q)$, relative risk $\approx 1 + F/q$ (Formula 7.5.2); rare recessive diseases concentrate in consanguineous families.
- Genetic counseling (Definition 7.6.1) is nondirective; carrier, predictive, prenatal and preimplantation tests modify the probabilities, and their predictive value depends on the prior.

## Questions

1. In a pedigree, two affected parents have an unaffected daughter. Which modes of inheritance are excluded (assuming full penetrance and no new mutations)? Which remain?

   **Answer** Recessive inheritance is excluded: under autosomal recessive inheritance both affected parents are $aa$ and every child is $aa$; under X-linked recessive inheritance the daughter receives the father's mutant X and one of the mother's two mutant X chromosomes. X-linked dominant inheritance is excluded because an affected father transmits his X, and with it the trait, to every daughter. Y-linkage cannot affect a daughter at all. Only autosomal dominant inheritance with two heterozygous parents remains (the daughter is $aa$, probability $1/4$ for each child).
2. A woman's maternal uncle has hemophilia A; her mother and maternal grandparents are unaffected, and there is no other history. Ignoring new mutations, what is the probability that the woman is a carrier, and that her first son is affected?

   **Answer** The grandmother must be a carrier (her son is affected and the grandfather is unaffected). The woman's mother is a carrier with probability $1/2$; the woman with probability $1/2 \times 1/2 = 1/4$; her first son is affected with probability $1/4 \times 1/2 = 1/8$.
3. In Question 2 the woman's mother has had two unaffected sons. Recompute the woman's carrier probability.

   **Answer** First update the mother: prior $1/2$, conditional $(1/2)^2 = 1/4$ for two unaffected sons; posterior $\frac{1/8}{1/8 + 1/2} = 1/5$. The woman is a carrier with probability $1/5 \times 1/2 = 1/10$, and her first son is affected with probability $1/20$.
4. A man has achondroplasia (autosomal dominant, heterozygous) and his wife is unaffected. They also both carry, with certainty, a recessive allele for albinism. What is the probability that their child (a) has achondroplasia and albinism, (b) is unaffected by either, (c) has exactly one condition?

   **Answer** $p_1 = 1/2$, $p_2 = 1/4$, independent. (a) $1/8$. (b) $\frac12 \cdot \frac34 = 3/8$. (c) $\frac12\cdot\frac34 + \frac12\cdot\frac14 = 1/2$.
5. The unaffected sister of a woman with phenylketonuria marries an unrelated man from a population in which the incidence of phenylketonuria is 1 in 10 000. Assuming Hardy–Weinberg proportions (as given), what is the risk that their first child is affected?

   **Answer** $q = 0.01$, carrier frequency $2pq \approx 0.0198$. The sister is a carrier with probability $2/3$. Risk $= \frac23 \times 0.0198 \times \frac14 \approx 0.0033$, about 1 in 300.
6. In Example 7.3.1(a) the couple's first child is unaffected. What is the risk for their second child?

   **Answer** Hypotheses for the couple: both carriers (prior $\frac23\cdot\frac23 = \frac49$), otherwise ($\frac59$). Conditional probability of one unaffected child: $\frac34$ if both are carriers, $1$ otherwise. Posterior that both are carriers: $\frac{(4/9)(3/4)}{(4/9)(3/4) + 5/9} = \frac{1/3}{1/3 + 5/9} = \frac{3}{8}$. Risk for the second child $= \frac38 \times \frac14 = \frac{3}{32} \approx 0.094$, slightly less than $1/9 \approx 0.111$.
7. Compute the inbreeding coefficient of the child of (a) an uncle and his niece, (b) double first cousins, (c) second cousins, using Eq. (7.1).

   **Answer** (a) The uncle is a brother of the niece's parent; their common ancestors are the uncle's parents (the niece's grandparents). Each loop: uncle, grandparent, niece's parent, niece: $n = 4$. Two loops: $F = 2(1/2)^4 = 1/8$. (b) Double first cousins share all four grandparents; four loops with $n = 5$: $F = 4/32 = 1/8$. (c) Second cousins share two great-grandparents; each loop contains the two parents, their two parents, their two grandparents (who are siblings) and the common ancestor: $n = 7$; $F = 2/128 = 1/64$.
8. For a recessive disease with allele frequency $q = 0.005$, compute the risk for the child of first cousins and the relative risk compared with unrelated parents. What fraction of patients would be born to first cousins if 5 % of marriages were between first cousins?

   **Answer** Unrelated: $q^2 = 2.5\times10^{-5}$. First cousins: $2.5\times10^{-5} + \frac{1}{16}(0.005)(0.995) = 2.5\times10^{-5} + 3.11\times10^{-4} = 3.36\times10^{-4}$; relative risk about 13.4. Fraction from first-cousin marriages: $\frac{0.05 \times 3.36\times10^{-4}}{0.05 \times 3.36\times10^{-4} + 0.95 \times 2.5\times10^{-5}} = \frac{1.68\times10^{-5}}{1.68\times10^{-5} + 2.375\times10^{-5}} \approx 0.41$.
9. Explain why the coefficient of relationship of full siblings ($1/2$) equals that of parent and child, although siblings can share zero, one or two alleles IBD at a locus.

   **Answer** A parent and a child share exactly one allele IBD at every (autosomal) locus, so they share half of their alleles always. Full siblings share 0, 1 or 2 alleles IBD with probabilities $1/4$, $1/2$, $1/4$ (each parent transmits the same allele to both with probability $1/2$, independently), an average of one shared allele, i.e. $r = 1/2$; but the proportion varies from locus to locus and, across the genome, between sibling pairs ([7.4.5](/7.4.5), Example 5.4.2).
10. A 50-year-old man is the son of a woman with Huntington disease. He is unaffected. If 70 % of carriers have shown symptoms by age 50, what is the probability that he carries the allele, and the prior risk to his newborn daughter?

    **Answer** $(1 - 0.7)/(2 - 0.7) = 0.3/1.3 \approx 0.23$. His daughter's risk is half: $\approx 0.115$.
11. A carrier test for an autosomal recessive disease has detection rate 0.8. A woman from a population with carrier frequency $1/30$ tests negative. What is her posterior carrier probability? Her partner, who has an affected brother, tests positive. What is the risk for their child?

    **Answer** Woman: $\frac{(1/30)(0.2)}{(1/30)(0.2) + 29/30} = \frac{0.2}{29.2} \approx 0.0068$. The partner is now a known carrier (a positive test is assumed specific). Risk $= 1 \times 0.0068 \times \frac14 \approx 0.0017$, about 1 in 580.
12. (Comprehensive) II-1 and II-2 are an unaffected couple; II-1's brother has cystic fibrosis, and II-2 is from a population with carrier frequency $1/25$. They have two children, both unaffected. What is the probability that their third child has cystic fibrosis? What is it if the couple instead had one affected child?

    **Answer** Prior that both are carriers: $\frac23 \times \frac{1}{25} = \frac{2}{75}$. Two unaffected children have probability $(3/4)^2 = 9/16$ if both are carriers, 1 otherwise. Posterior: $\frac{(2/75)(9/16)}{(2/75)(9/16) + 73/75} = \frac{18/1200}{18/1200 + 1168/1200} = \frac{18}{1186} \approx 0.0152$. Risk for the third child $\approx 0.0152/4 \approx 0.0038$, about 1 in 264 (compared with $1/150$ before they had children). With one affected child both parents are obligate carriers, and the risk is $1/4$.
13. (Comprehensive) A woman whose brother has Duchenne muscular dystrophy (her mother is an obligate carrier) has two unaffected sons and a serum creatine kinase test that is raised in 70 % of carriers and 5 % of non-carriers; her result is normal. Compute her posterior carrier probability.

    **Answer** Prior $1/2$. Conditional for a carrier: two unaffected sons $\frac14$ times a normal test $0.3$, giving $0.075$; for a non-carrier: $1 \times 0.95 = 0.95$. Joint: $0.0375$ and $0.475$. Posterior $= 0.0375/0.5125 \approx 0.073$; the risk for her next son is about $0.037$.
14. A dominant disease has penetrance $0.8$ in $Aa$ and occurs in $2\,\%$ of $aa$ people from other causes. A child of an $Aa \times aa$ couple is (a) affected, (b) unaffected. Compute the probability that the child is $Aa$ in each case, and in case (b) the risk that the child's own first child (with an $aa$ partner) is affected.

    **Answer** Prior $\tfrac12$ each. (a) $\dfrac{0.5 \times 0.8}{0.5 \times 0.8 + 0.5 \times 0.02} = \dfrac{0.40}{0.41} = 0.976$. (b) $\dfrac{0.5 \times 0.2}{0.5 \times 0.2 + 0.5 \times 0.98} = \dfrac{0.10}{0.59} = 0.169$. Natural frequencies: of 1 000 children, 500 are $Aa$ (100 unaffected) and 500 $aa$ (490 unaffected); 100 of the 590 unaffected are $Aa$. Grandchild: $Aa$ with probability $0.169/2 = 0.085$, affected with probability $0.085 \times 0.8 + (1 - 0.085) \times 0.02 = 0.068 + 0.018 = 0.086$.
15. A woman is a carrier of red-green color blindness (X-linked recessive) and of albinism (autosomal recessive); her husband has normal vision and is also a carrier of albinism. Find (a) the probability that their next child is a color-blind son, (b) the probability that a son is color-blind, (c) the probability that a daughter is color-blind, (d) the probability that the next child is a son with both conditions, and (e) the probability that a son has both.

    **Answer** (a) $\tfrac12 \times \tfrac12 = \tfrac14$. (b) $\tfrac12$. (c) $0$ (every daughter receives the father's normal X). (d) $\tfrac14 \times \tfrac14 = \tfrac1{16}$ (an affected son, times albinism $\tfrac14$). (e) $\tfrac12 \times \tfrac14 = \tfrac18$ (Remark 7.3.1).
16. A couple has a child with cystic fibrosis. The wife's sister has phenylketonuria; the husband has no family history of phenylketonuria, and the carrier frequency in his population is $1/50$. For their next child, find the probability of (a) both diseases, (b) cystic fibrosis only, (c) phenylketonuria only, (d) at least one disease.

    **Answer** Both parents are obligate carriers for cystic fibrosis: $p_1 = \tfrac14$. Phenylketonuria: the wife is a carrier with probability $\tfrac23$, the husband $\tfrac1{50}$: $p_2 = \tfrac23 \cdot \tfrac1{50} \cdot \tfrac14 = \tfrac1{300}$. The loci are unlinked, and the uncertainty about the parents' genotypes concerns only the second locus, so Formula 7.3.1 applies. (a) $\tfrac1{1200}$. (b) $\tfrac14 \cdot \tfrac{299}{300} = \tfrac{299}{1200} \approx 0.249$. (c) $\tfrac34 \cdot \tfrac1{300} = \tfrac1{400}$. (d) $1 - \tfrac34 \cdot \tfrac{299}{300} = \tfrac{101}{400} \approx 0.253$.
17. In Example 7.4.5, the daughter III-2 has two unaffected sons. What are now the probabilities that III-2 and that her mother II-6 are carriers?

    **Answer** Three hypotheses, with priors from II-6's posterior $\tfrac19$: II-6 not a carrier (then III-2 is not), $\tfrac89$; II-6 a carrier and III-2 a carrier, $\tfrac1{18}$; II-6 a carrier and III-2 not, $\tfrac1{18}$. Conditional probabilities of two unaffected sons of III-2: $1$, $\tfrac14$, $1$. Joints: $\tfrac{64}{72}$, $\tfrac1{72}$, $\tfrac4{72}$; sum $\tfrac{69}{72}$. III-2 is a carrier with probability $\tfrac1{69} \approx 0.014$, and II-6 with probability $\tfrac{1 + 4}{69} = \tfrac5{69} \approx 0.072$, less than $\tfrac19$: the grandsons carry information about their grandmother too. (Starting from II-6's prior $\tfrac12$ and using all five sons in one table gives the same result.)
