---
title: Tetrad Analysis and Mitotic Recombination
description: Fungal life cycles and the asci of yeast and Neurospora; parental ditypes, nonparental ditypes and tetratypes, the test for linkage and the recombination frequency from unordered tetrads, Perkins' formula and the exact tetrad frequencies under no interference; first- and second-division segregation in ordered tetrads, gene–centromere distances and the 2/3 limit; what tetrads prove about crossing over, chromatid interference and gene conversion; mitotic recombination, twin spots, genetic mosaics and FLP/FRT clones.
---

In a fly or a person the four products of one meiosis go their separate ways, and each offspring reveals only one of them; mapping must then count many offspring and infer what happened in meiosis on average ([7.4.8](/7.4.8)). In many fungi and some algae the four products of a single meiosis stay together in one sac and can be examined as a set. Such tetrads show directly what happens in an individual meiosis: they prove that crossing over occurs between two of four chromatids, they give recombination frequencies and their correction for double crossovers from one cross, they map centromeres as if they were genes, and they revealed gene conversion, the nonreciprocal exchange that led to the molecular models of recombination ([7.2.9](/7.2.9#sec-9.4)). The second half of the chapter turns to crossing over in mitosis. It is rare, but where it happens in a heterozygote it makes a patch of homozygous cells in an otherwise heterozygous body, a genetic mosaic; this is the basis of clonal analysis in *Drosophila*, of the mosaic analysis of development in [7.4.20](/7.4.20), and of one of the main routes to loss of heterozygosity in cancer ([7.4.21](/7.4.21)).

## 9.1. Fungi as Genetic Organisms

### 9.1.1. Two Model Life Cycles

The two classical organisms of tetrad analysis are ascomycete fungi, haploid for most of their life cycle (zygotic meiosis, [7.4.1](/7.4.1)).

- The budding yeast *Saccharomyces cerevisiae* has two mating types, $\mathit{MATa}$ and $\mathit{MAT\alpha}$. Haploid cells of opposite mating type fuse to form diploids, which grow by mitosis and, when starved of nitrogen and given a nonfermentable carbon source, undergo meiosis. The four haploid spores are enclosed in an ascus without any fixed arrangement. After digesting the ascus wall, the spores are separated with a micromanipulator and grown into colonies, whose genotypes are determined by replica plating or by sequencing.
- The bread mould *Neurospora crassa* has mating types $A$ and $a$. Fusion of nuclei of opposite mating type produces a transient diploid nucleus that immediately undergoes meiosis inside a narrow ascus. The spindles of the two meiotic divisions are aligned with the long axis of the ascus and do not overlap, so the four meiotic products lie in a row in the order in which they were produced; a mitosis follows, giving eight ascospores in four identical pairs. Spore-colour mutants allow patterns to be read under the microscope without germinating the spores. *Neurospora* has $n = 7$ chromosomes, completes a sexual cycle in about ten days and grows on a simple minimal medium, so that **auxotrophs** ([7.4.10](/7.4.10)) such as *lys*, *nic* or *ade* mutants, which need lysine, nicotinic acid or adenine, are scored by growth on supplemented versus minimal medium; some, such as *lys*, also ripen slowly and give pale ascospores that can be seen in the intact ascus.

**Definition 9.1.1 (Tetrad Analysis, Ascus and Ascospore)** An **ascus** is the sac in which an ascomycete fungus holds the products of one meiosis; the haploid spores in it are **ascospores**. The four products of one meiosis, considered together, form a tetrad, and **tetrad analysis** is the genetic analysis of the genotypes of all members of individual tetrads.

**Definition 9.1.2 (Ordered and Unordered Tetrads)** In an **unordered tetrad** (yeast, *Chlamydomonas*) the spores are arranged at random, so only the set of four genotypes is informative. In an **ordered tetrad** (*Neurospora*, *Sordaria*, *Ascobolus*) the spores lie in a linear ascus in an order that reflects the two meiotic divisions: the two halves of the ascus come from the two products of meiosis I, and each spore pair (or quarter, in an eight-spored ascus) from one product of meiosis II.

Haploidy has another advantage: a spore's phenotype shows its genotype directly, with no dominance to hide alleles, so each tetrad is in effect four testcross offspring from one meiosis.

### 9.1.2. Two Kinds of Information

Unordered tetrads tell us how two loci were distributed among the four products, which gives linkage and recombination between the loci. Ordered tetrads add the position of each locus relative to its centromere, because the arrangement shows whether the two alleles of a locus separated at the first or the second division. We treat them in turn.

## 9.2. Unordered Tetrads

### 9.2.1. Three Kinds of Tetrad

Consider a cross $AB \times ab$ in yeast; the diploid is $AB/ab$. A tetrad contains two $A$ and two $a$ spores and two $B$ and two $b$ spores (2:2 segregation at each locus, apart from gene conversion, 9.4.3), and there are only three possible combinations.

**Definition 9.2.1 (Parental Ditype, Nonparental Ditype and Tetratype)** For two loci in a cross $AB \times ab$:

- a **parental ditype** (PD) tetrad contains two kinds of spores, both parental: $AB, AB, ab, ab$;
- a **nonparental ditype** (NPD) tetrad contains two kinds, both recombinant: $Ab, Ab, aB, aB$;
- a **tetratype** (T) tetrad contains all four kinds: $AB, Ab, aB, ab$.

![Ascus patterns. (A) Ordered asci of *Neurospora* (eight spores; pale and dark spores carry the two alleles of a spore-colour gene). In the two first-division (MI) patterns the alleles separated at meiosis I, so each half of the ascus is uniform; in the four second-division (MII) patterns a crossover between the gene and its centromere made the alleles separate only at meiosis II. (B) The three kinds of unordered tetrads (yeast) for two loci in a cross AB × ab: parental ditype (PD), nonparental ditype (NPD) and tetratype (T).](./plots/ascus-patterns.py)

Which crossovers make which tetrads? With no crossover between the loci, all four chromatids are parental: PD. One crossover between the loci makes two recombinant chromatids: T. Two crossovers between the loci give PD, T or NPD according to the chromatids involved: a two-strand double gives PD, the two kinds of three-strand double give T, and a four-strand double gives NPD (Figure). Thus for linked loci an NPD tetrad requires at least two crossovers in the interval, while PD and T need none or one.

![Crossovers between two loci and the tetrads they produce. Each block shows the four chromatids of the bivalent (blue and pink: the two homologues) with crossovers marked by X between the chromatids involved, and the resulting four spores. No crossover gives a parental ditype, one crossover a tetratype; of the four equally likely kinds of double crossover, the two-strand double gives PD, the two three-strand doubles give T and the four-strand double gives NPD.](./plots/tetrad-crossovers.py)

### 9.2.2. The Test for Linkage

If the loci are on different chromosomes, PD and NPD arise from the two equally likely orientations of the two bivalents at metaphase I, and T arises when a crossover between one locus and its centromere has occurred (Figure in 9.2.1). Therefore:

- unlinked loci: $\mathbb{P}(\mathrm{PD}) = \mathbb{P}(\mathrm{NPD})$;
- linked loci: $\mathbb{P}(\mathrm{PD}) > \mathbb{P}(\mathrm{NPD})$, and for closely linked loci $\mathrm{PD} \gg \mathrm{NPD}$.

The test of linkage is therefore a test of $\mathrm{PD} = \mathrm{NPD}$: among the $\mathrm{PD} + \mathrm{NPD}$ ditype tetrads, the number of PD is $\mathrm{Bin}(\mathrm{PD} + \mathrm{NPD}, 1/2)$ under the null hypothesis of no linkage, and $\chi^2 = (\mathrm{PD} - \mathrm{NPD})^2/(\mathrm{PD} + \mathrm{NPD})$ with 1 degree of freedom is the usual approximation. Unlike the test in random spores, this test does not depend on the frequency of tetratypes, which reflects centromere distances, not linkage.

### 9.2.3. Recombination Frequency and Perkins' Formula

Each PD contains no recombinant spore, each T two of four, and each NPD four of four. Counting spores:

**Formula 9.2.1 (Recombination Frequency from Tetrads)** With $n$ tetrads,

$$
r = \frac{\mathrm{NPD} + \frac12\mathrm{T}}{n}.
$$

This is the same recombination frequency as from random spores, and like it, it underestimates distance when multiple crossovers occur. Tetrads allow a correction from the data themselves. Assume that there are at most two crossovers between the loci and no chromatid interference, so that the four kinds of double crossover occur in the ratio 1:2:1 (two-strand : three-strand : four-strand). Let $s$ and $q$ be the proportions of meioses with one and two crossovers. Then $\mathrm{NPD}/n = q/4$ (only four-strand doubles) and $\mathrm{T}/n = s + q/2$ (single crossovers and three-strand doubles), so $s = \mathrm{T}/n - 2\,\mathrm{NPD}/n$ and $q = 4\,\mathrm{NPD}/n$. The mean number of crossovers per meiosis (per bivalent) in the interval is $s + 2q = (\mathrm{T} + 6\,\mathrm{NPD})/n$, and the map distance, the mean number per chromatid, is half of it.

**Formula 9.2.2 (Perkins' Formula)** If at most two crossovers occur between the loci and there is no chromatid interference, the map distance in centimorgans is

$$
d = \frac{50\,(\mathrm{T} + 6\,\mathrm{NPD})}{n}.
$$

**Example 9.2.1** A yeast cross gives 400 tetrads: 231 PD, 11 NPD and 158 T. Linkage: $\chi^2 = (231 - 11)^2/242 = 200$, $p \approx 10^{-45}$, so the loci are linked. The recombination frequency is $(11 + 79)/400 = 22.5\,\%$, and Perkins' formula gives $d = 50(158 + 66)/400 = 28.0\,\mathrm{cM}$. The data were in fact generated from loci $30\,\mathrm{cM}$ apart without interference (9.2.4); Perkins' formula recovers most of the distance hidden by double crossovers, and its remaining deficit comes from triple and higher crossovers, which it ignores.

### 9.2.4. The Exact Model Without Interference

The assumption of at most two crossovers can be dropped. Treat the tetrad type as a Markov chain that is updated by each crossover in the interval, the crossover involving a random pair of non-sister chromatids. A crossover turns a PD or an NPD into a T. From a T, a crossover gives PD with probability $1/4$, NPD with probability $1/4$ and T with probability $1/2$ (of the four possible non-sister pairs, one restores the parental arrangement, one completes the nonparental arrangement, and two leave a tetratype). Writing $t_k$ for the probability of T after $k$ crossovers, $t_0 = 0$ and $t_{k+1} = (1 - t_k) + t_k/2 = 1 - t_k/2$, so

$$
t_k = \tfrac23\bigl(1 - (-\tfrac12)^k\bigr),
$$
and the probability of NPD after $k \ge 1$ crossovers is $t_{k-1}/4$.

**Formula 9.2.3 (Tetrad Frequencies Without Interference)** If the number of crossovers between two loci $d$ morgans apart is $K \sim \mathrm{Poi}(2d)$ (Haldane model, [7.4.8](/7.4.8)) and there is no chromatid interference, then

$$
\mathbb{P}(\mathrm{T}) = \tfrac23\bigl(1 - \mathrm{e}^{-3d}\bigr), \qquad \mathbb{P}(\mathrm{NPD}) = \tfrac16\bigl(1 - 3\mathrm{e}^{-2d} + 2\mathrm{e}^{-3d}\bigr),
$$
and $\mathbb{P}(\mathrm{PD}) = 1 - \mathbb{P}(\mathrm{T}) - \mathbb{P}(\mathrm{NPD})$.

**Proof** Average $t_K$ over $K \sim \mathrm{Poi}(\lambda)$ with $\lambda = 2d$, using $\mathbb{E}[x^K] = \mathrm{e}^{-\lambda(1 - x)}$: $\mathbb{E}[t_K] = \frac23(1 - \mathrm{e}^{-3\lambda/2}) = \frac23(1 - \mathrm{e}^{-3d})$. For NPD, $\mathbb{E}[t_{K-1}\boldsymbol{1}_{K \ge 1}]/4 = \frac16\bigl[(1 - \mathrm{e}^{-\lambda}) + 2\mathrm{e}^{-\lambda}(\mathrm{e}^{-\lambda/2} - 1)\bigr]$, which is the stated expression. $\square$

As a check, $\mathbb{P}(\mathrm{NPD}) + \frac12\mathbb{P}(\mathrm{T}) = \frac12(1 - \mathrm{e}^{-2d})$, the Haldane function. As $d \to \infty$ the frequencies approach $\mathrm{PD} = \mathrm{NPD} = 1/6$ and $\mathrm{T} = 2/3$; these are also the limiting frequencies for unlinked loci both far from their centromeres. Inverting the formula for $\mathbb{P}(\mathrm{NPD})$, or fitting all three frequencies by maximum likelihood, gives a distance that is exact under the model, while Perkins' formula is its second-order approximation.

![Tetrad frequencies and distance estimates under the Haldane model (no chiasma or chromatid interference). (A) PD, NPD and T frequencies as functions of the map distance between two loci; T rises toward its limit 2/3 and NPD toward 1/6; the MII frequency of a locus at distance d from its centromere (dashed) follows the same curve as T. (B) Distance estimates from tetrad data against the true distance: the uncorrected recombination frequency (NPD + T/2) saturates at 50 cM, Perkins' formula is accurate up to about 30 cM and then underestimates, and the exact inversion of the NPD formula is unbiased.](./plots/tetrad-theory.py)

## 9.3. Ordered Tetrads

### 9.3.1. First- and Second-Division Segregation

In an ordered ascus, the alleles of one locus, say $ws^{+}$ (black spores) and $ws$ (white spores), can be arranged in six ways. In two of them each half of the ascus is uniform (4:4, e.g. black-black-black-black-white-white-white-white), and in four the halves are mixed (2:2:2:2 or 2:4:2).

**Definition 9.3.1 (First-Division and Second-Division Segregation)** A locus shows **first-division segregation** (MI pattern) in an ascus when its two alleles separated at meiosis I, so that each half of an ordered ascus carries one allele; it shows **second-division segregation** (MII pattern) when the alleles separated only at meiosis II, so that each half carries both alleles.

Without a crossover between the locus and its centromere, the two chromatids of each homologue carry the same allele and are separated from the other homologue at meiosis I: an MI pattern. A crossover between locus and centromere puts one chromatid of each allele on each centromere, so the alleles are separated only when the sister centromeres part at meiosis II: an MII pattern (the meiotic divisions in these terms are the **reductional division** and the **equational division**, [7.4.5](/7.4.5)). The four MII patterns correspond to the two orientations at meiosis I and the two pairs of chromatids that can be involved, all equally likely.

### 9.3.2. Gene–Centromere Distance

An ascus with an MII pattern comes from a meiosis with a crossover between gene and centromere, in which two of the four chromatids are recombinant (in the sense of having exchanged the region between gene and centromere). Hence:

**Formula 9.3.1 (Gene–Centromere Distance)** If multiple crossovers between a locus and its centromere are negligible, the distance between them in centimorgans is half the percentage of asci with an MII pattern,

$$
d = \tfrac12 \times (\%\ \mathrm{MII}).
$$

**Example 9.3.1** Of 200 *Neurospora* asci from a cross $ws^{+} \times ws$, 170 show an MI pattern (86 and 84 of the two kinds) and 30 an MII pattern (8, 7, 8 and 7). MII frequency $15\,\%$, gene–centromere distance $7.5\,\mathrm{cM}$.

### 9.3.3. The Two-Thirds Limit

Double crossovers between a gene and its centromere do not all restore an MI pattern, so the MII frequency does not approach $100\,\%$. The same Markov argument as in 9.2.4 applies: after a crossover in the interval, an MI pattern always becomes MII, while an MII pattern returns to MI with probability $1/2$ (when the second crossover involves the chromatids that will separate it at the first division). With $m_k$ the MII probability after $k$ crossovers, $m_{k+1} = 1 - m_k/2$, the same recursion as for tetratypes, so $m_k = \frac23\bigl(1 - (-\frac12)^k\bigr)$.

**Formula 9.3.2 (MII Frequency Without Interference)** For a locus $d$ morgans from its centromere, with a Poisson number of crossovers and no chromatid interference,

$$
\mathbb{P}(\mathrm{MII}) = \tfrac23\bigl(1 - \mathrm{e}^{-3d}\bigr), \qquad d = -\tfrac13\ln\Bigl(1 - \tfrac32\,\mathbb{P}(\mathrm{MII})\Bigr).
$$
For small $d$, $\mathbb{P}(\mathrm{MII}) \approx 2d$, which is Formula 9.3.1; for loci far from the centromere, $\mathbb{P}(\mathrm{MII}) \to 2/3$.

An MII frequency near $2/3$ is therefore the signature of a locus effectively unlinked to its centromere. Frequencies above $2/3$ are impossible under the no-interference model but are observed for some distal loci in organisms with strong chiasma interference: if the arm almost always has exactly one crossover and rarely two, a locus beyond it shows MII in nearly every ascus. Lindegren, who first mapped centromeres in *Neurospora* in 1932, measured gene–centromere distances with this method.

### 9.3.4. Mapping Two Genes and a Centromere

With two loci in ordered tetrads, the three quantities, two MII frequencies and the recombination frequency between the loci, place the two genes and the centromere on one line.

**Algorithm 9.3.1 (Ordering Two Loci and a Centromere)**

1. For each locus compute the gene–centromere distance $d_A = \frac12\,\mathrm{MII}_A$ and $d_B = \frac12\,\mathrm{MII}_B$ (Formula 9.3.1, or 9.3.2 for long distances).
2. Test linkage between the loci with PD versus NPD (9.2.2) and compute $r_{AB}$ (Formula 9.2.1, Perkins' correction if needed).
3. If $r_{AB} \approx \lvert d_A - d_B\rvert$, the loci are on the same arm, with the one of smaller $d$ nearer the centromere; if $r_{AB} \approx d_A + d_B$, they are on opposite arms.
4. Check with the tetrad classes: for loci on the same arm, almost every ascus with an MII pattern for the proximal locus also shows MII for the distal locus.

**Example 9.3.2** In 400 ordered asci of a cross $AB \times ab$, locus $A$ shows MII in 40 asci and $B$ in 96, and there are 56 tetratypes and no NPD for $A$ and $B$. Then $d_A = 5.0\,\mathrm{cM}$, $d_B = 12.0\,\mathrm{cM}$, $r_{AB} = 28/400 = 7.0\,\%$. Since $12.0 - 5.0 = 7.0$, the order is centromere–$A$–$B$; if they were on opposite arms we would expect about $17\,\mathrm{cM}$ between them, around 136 tetratypes.

### 9.3.5. Unlinked Loci Linked to Their Centromeres

For two loci on different chromosomes with MII frequencies $x$ and $y$ (from either ordered asci or a centromere marker), the T frequency depends on the two gene–centromere distances: if neither locus shows MII, the tetrad is PD or NPD with probability $1/2$ each; if exactly one does, it is T; if both do, it is T with probability $1/2$ and PD or NPD with probability $1/4$ each.

**Formula 9.3.3 (Tetratypes of Unlinked Loci)** For loci on different chromosomes,

$$
\mathbb{P}(\mathrm{T}) = x + y - \tfrac32\,xy, \qquad \mathbb{P}(\mathrm{PD}) = \mathbb{P}(\mathrm{NPD}) = \tfrac12\bigl(1 - \mathbb{P}(\mathrm{T})\bigr).
$$

This is how yeast geneticists mapped centromeres with unordered tetrads: a locus tightly linked to its centromere (such as *TRP1* on chromosome IV) gives few tetratypes with any unlinked locus, $\mathbb{P}(\mathrm{T}) \approx y$, so it serves as a centromere marker. For two loci far from their centromeres, $x = y = 2/3$ and $\mathbb{P}(\mathrm{T}) = 2/3$.

### 9.3.6. The Seven Classes of Ordered Asci

For two linked loci in ordered asci each ascus can be classified three ways at once: MI or MII for the first locus, MI or MII for the second, and PD, NPD or T for the pair. Of the 36 possible spore arrangements of a cross $a\,b^{+} \times a^{+}\,b$, those that differ only by turning the ascus round or by the two equivalent arrangements of an MII pattern collapse into seven classes. With the gene order centromere–$a$–$b$, interval I between the centromere and $a$ and interval II between $a$ and $b$, the smallest number of crossovers that produces each class (found by enumerating crossovers between random non-sister chromatids) is:

| Class | $a$ | $b$ | Tetrad | Fewest crossovers |
|---|---|---|---|---|
| 1 | MI | MI | PD | none |
| 2 | MI | MI | NPD | two in II (four-strand) |
| 3 | MI | MII | T | one in II |
| 4 | MII | MI | T | one in I and one in II |
| 5 | MII | MII | PD | one in I |
| 6 | MII | MII | NPD | one in I and two in II |
| 7 | MII | MII | T | one in I and two in II |

Class 7 is sometimes described as a double crossover, but one crossover in each interval cannot produce it: after a crossover in I, each chromatid carries the alleles of $a$ and $b$ from the same parent, so a crossover in II between two non-sister chromatids carrying different alleles of $b$ returns $b$ to an MI pattern (class 4), and one between chromatids carrying the same allele of $b$ changes nothing. Only for loci on opposite arms is "MII, MII, T" the product of one crossover on each side of the centromere. The asymmetry between classes 3 and 4 is a test of gene order: if $a$ is proximal, MII at $a$ with MI at $b$ needs two crossovers and is rare, whereas MI at $a$ with MII at $b$ needs one.

**Example 9.3.3** A cross $a\,b^{+} \times a^{+}\,b$ in *Neurospora* gives 1000 asci: class 1, 712; class 2, 2; class 3, 144; class 4, 8; class 5, 130; class 6, 1; class 7, 3.

1. Linkage: $\mathrm{PD} = 712 + 130 = 842$, $\mathrm{NPD} = 2 + 1 = 3$: $\mathrm{PD} \gg \mathrm{NPD}$, linked.
2. Gene–centromere distances (Formula 9.3.1): MII for $a$ in classes 4–7, $142$ asci, $d_a = 7.1\,\mathrm{cM}$; MII for $b$ in classes 3 and 5–7, $278$ asci, $d_b = 13.9\,\mathrm{cM}$.
3. Distance between the genes (Formula 9.2.1): $\mathrm{T} = 144 + 8 + 3 = 155$, $r_{ab} = (3 + 77.5)/1000 = 8.05\,\%$.
4. Order: $d_a + r_{ab} = 15.15 \approx d_b$ (opposite arms would give $d_a + d_b = 21\,\mathrm{cM}$ between the genes). Of the 142 asci with MII at $a$, 134 ($94\,\%$) also show MII at $b$, against $27.8\,\%$ expected if the two loci were on different arms or chromosomes, and class 3 is eighteen times as frequent as class 4. The map is centromere —$7.1$— $a$ —$8.05$— $b$.

The direct centromere–$b$ distance, $13.9\,\mathrm{cM}$, is $1.25\,\mathrm{cM}$ shorter than the sum of the two intervals: the same underestimate as the outer-gene distance of a three-point cross ([7.4.8](/7.4.8#sec-8.4.2)), with the centromere as the third marker. Counting recombinant chromatids (two per MII ascus, two per T, four per NPD, and none for an MI pattern even when all four chromatids have exchanged the segment) makes the deficit explicit:

| Class | Asci | Centromere–$a$ | $a$–$b$ | Centromere–$b$ | Chromatids missing from centromere–$b$ |
|---|---|---|---|---|---|
| 2 | 2 | 0 | 4 | 0 | $2 \times 4 = 8$ |
| 3 | 144 | 0 | 2 | 2 | 0 |
| 4 | 8 | 2 | 2 | 0 | $8 \times 4 = 32$ |
| 5 | 130 | 2 | 0 | 2 | 0 |
| 6 | 1 | 2 | 4 | 2 | $1 \times 4 = 4$ |
| 7 | 3 | 2 | 2 | 2 | $3 \times 2 = 6$ |

The columns give recombinant chromatids per ascus. The missing chromatids total $50$ of $4000$, $1.25\,\%$, and come only from the asci with two or more crossovers between the centromere and $b$ (classes 2, 4, 6 and 7). Adding them gives $13.9 + 1.25 = 15.15\,\mathrm{cM}$. Long gene–centromere distances should therefore be obtained by adding short intervals, or corrected with Formula 9.3.2 when there is no interference.

## 9.4. What Tetrads Prove

### 9.4.1. Crossing Over at the Four-Strand Stage

If crossing over occurred before chromosome replication, between two chromosomes rather than two of four chromatids, each meiosis would produce either two parental or two recombinant genotypes, each in two copies: only PD and NPD tetrads, never a tetratype. The abundance of tetratypes for linked genes (40 % of tetrads in Example 9.2.1) shows that a crossover involves only two of the four chromatids, after replication. The MII patterns of ordered asci show the same thing for a gene and its centromere. Tetrads also show that crossing over is reciprocal: a tetratype contains both recombinant products, $Ab$ and $aB$, in one ascus, and in an MII ascus the two alleles of the exchanged segment are still present in a $2:2$ ratio; nothing is lost or gained, except in the rare asci with gene conversion (9.4.3).

### 9.4.2. Chromatid Interference

The derivations above assume that the chromatids involved in successive crossovers are chosen independently, so that the two-, three- and four-strand double crossovers are in the ratio 1:2:1. Tetrads test this, because with three markers the four kinds of double crossover in two adjacent intervals can be recognized and counted (the four-strand doubles between the outer markers appear directly as NPDs). In *Neurospora*, yeast and *Drosophila* (attached-X data), the observed ratios agree with 1:2:1 within sampling error or show only weak deviations, so chromatid interference is weak or absent, in contrast to the strong chiasma interference of [7.4.8](/7.4.8#sec-8.4.3).

### 9.4.3. Gene Conversion

At a locus heterozygous for two alleles, tetrads almost always segregate 2:2. In a small fraction of asci, typically between a few tenths of a percent and a few percent of tetrads depending on the locus (more for markers near a recombination hotspot), one finds 3:1 or 1:3 tetrads, in which one allele has been copied onto a chromatid of the other homologue.

**Definition 9.4.1 (Gene Conversion)** **Gene conversion** is the nonreciprocal transfer of sequence information from one homologous DNA molecule to another during recombination, so that one allele is converted into the other; in tetrads of a heterozygote it appears as a 3:1 or 1:3 segregation instead of 2:2 (6:2 or 2:6 in eight-spored asci).

In eight-spored asci (*Neurospora*, *Sordaria*, *Ascobolus*), where the two strands of each product's DNA are separated by the post-meiotic mitosis, one also sees 5:3 asci and aberrant 4:4 asci, in which the two members of a spore pair differ. These post-meiotic segregations show that the product of meiosis carried heteroduplex DNA, one strand from each parent, which was replicated without being repaired. Gene conversion is therefore the genetic trace of heteroduplex DNA formed at a recombination intermediate and corrected by **mismatch repair**, or of gap repair by copying from the homologue after a double-strand break ([7.2.9](/7.2.9#sec-9.5.1)). It has three consequences for mapping:

- conversion is associated with crossing over of flanking markers in a large fraction of cases (often a third to a half), but conversions without crossover are also frequent, as expected from the noncrossover pathways of double-strand-break repair;
- conversion of one site can carry nearby sites with it (co-conversion), with a probability that falls with distance over a few kilobases;
- some sites convert more often than others (polarity of conversion from the initiation site), which produces map expansions and negative interference in fine-structure crosses within a gene ([7.4.13](/7.4.13)).

## 9.5. Mitotic Recombination and Genetic Mosaics

### 9.5.1. Twin Spots

In 1936 Curt Stern noticed that *Drosophila* females heterozygous for two recessive X-linked markers, $y$ (yellow body and bristles) and $sn$ (singed, gnarled bristles), in repulsion, $y\,sn^{+}/y^{+}\,sn$, occasionally carried small patches of mutant tissue on an otherwise wild-type body: yellow patches, singed patches, and twin spots, a yellow patch next to a singed patch. On the X chromosome $y$ lies at the tip, $sn$ about $21\,\mathrm{cM}$ further in, and the centromere at the other end.

**Definition 9.5.1 (Mitotic Recombination and Twin Spot)** **Mitotic recombination** is crossing over between homologous chromosomes in a mitotic (somatic or premeiotic) cell, after replication, between non-sister chromatids. In a heterozygote it can make the region distal to the exchange homozygous in the two daughter cells; when the descendants of both daughters form adjacent patches of different mutant phenotypes, they form a **twin spot**.

Mitotic recombination is rare, because homologues do not normally pair in mitosis (they are paired in *Drosophila* somatic cells, which is why it is easiest to study there) and because mitotic double-strand breaks are mostly repaired by sister-chromatid recombination or by noncrossover pathways ([7.2.9](/7.2.9#sec-9.5.1)). Its frequency increases greatly after ionizing radiation, which is used to induce clones.

### 9.5.2. The Logic of Spot Types

The kind of spot depends on where the exchange happened and how the chromatids segregated (Figure). Consider the female $y\,sn^{+}/y^{+}\,sn$ (centromere proximal, $sn$ in the middle, $y$ distal):

| Exchange | Segregation of the recombinant chromatids | Daughter cells | Spot |
|---|---|---|---|
| Between centromere and $sn$ | to different poles | $y\,sn^{+}/y\,sn^{+}$ and $y^{+}\,sn/y^{+}\,sn$ | twin spot (yellow next to singed) |
| Between $sn$ and $y$ | to different poles | $y\,sn^{+}/y\,sn$ and $y^{+}\,sn^{+}/y^{+}\,sn$ | single yellow spot |
| Anywhere | to the same pole | both heterozygous | none |
| Two exchanges, one on each side of $sn$ | to different poles | $y\,sn/y^{+}\,sn$ and $y^{+}\,sn^{+}/y\,sn^{+}$ | single singed spot (rare) |

At mitosis each chromosome's two chromatids go to opposite poles, and the two chromatids that took part in the exchange go to different poles in half the cases (x segregation) and to the same pole in the other half (z segregation). Only x segregation makes the distal region homozygous, so only half the mitotic crossovers in an interval become visible. Twin spots are more frequent than single yellow spots because the centromere–$sn$ interval is longer in mitosis as well as in meiosis, single singed spots require two exchanges and are rare, and a twin spot can only be explained by a reciprocal exchange: the two daughter cells of one division carry the two reciprocal products. This was the first evidence that crossing over can happen in mitotic cells.

![Mitotic recombination and twin spots. (A) A *Drosophila* cell heterozygous *y* *sn*⁺ / *y*⁺ *sn* (blue: chromosome with *y*; pink: chromosome with *sn*; centromere left, *y* at the right tip) after replication, with a crossover between the centromere and *sn*. (B) If the recombinant chromatids go to different poles (x segregation), one daughter is homozygous *y* *sn*⁺ (yellow) and the other *y*⁺ *sn* (singed). (C) Their clones form adjacent patches, a twin spot, on a heterozygous wild-type background. (D) A crossover between *sn* and *y* gives a single yellow spot; the reciprocal daughter is wild type.](./plots/twin-spots.py)

**Example 9.5.1** If mitotic crossovers between the centromere and $sn$ occur in a given cell division with probability $p_1 = 2 \times 10^{-4}$ and between $sn$ and $y$ with probability $p_2 = 0.5 \times 10^{-4}$, and x and z segregation are equally likely, then per division the probabilities of founding a twin spot and a single yellow spot are $p_1/2 = 10^{-4}$ and $p_2/2 = 2.5 \times 10^{-5}$; a cuticle region formed from $10^4$ divisions of imaginal-disc cells would show on average $1$ twin spot and $0.25$ single yellow spots. The size of a spot reflects the number of divisions after the event: a clone induced $k$ divisions before the end of growth has about $2^k$ cells.

### 9.5.3. Genetic Mosaics and Clonal Analysis

**Definition 9.5.2 (Genetic Mosaic)** A **genetic mosaic** is an individual composed of cells of two or more genotypes derived from a single zygote, for example by mitotic recombination, chromosome loss, mutation or X-chromosome inactivation.

Mosaics are a tool for a basic question of developmental genetics: where and when must a gene act? A recessive lethal mutation that kills a homozygous embryo can still be studied in clones of homozygous cells made by mitotic recombination in a heterozygous animal. In the 1990s this became routine with the yeast site-specific recombinase FLP and its target FRT (Golic and Lindquist 1989; Xu and Rubin 1993): flies carry FRT sites at the base of a chromosome arm on both homologues, one homologue carries the mutation and the other a marker such as a GFP transgene, and FLP is expressed from a heat-shock promoter or a tissue-specific driver. Recombination at the FRT sites (**site-specific recombination**, [7.2.9](/7.2.9#sec-9.6)) yields twin clones: homozygous mutant cells without GFP next to homozygous wild-type cells with two copies, in a heterozygous background with one. Extensions mark only the mutant clone positively (MARCM, Lee and Luo 1999, which removes a repressor of a GAL4-driven marker along with the wild-type allele) or make whole mutant eyes. Clonal analysis with these tools is the subject of [7.4.20](/7.4.20); the same logic, now with Cre/loxP, is used in mice ([7.4.19](/7.4.19)).

### 9.5.4. Mitotic Recombination and Cancer

In humans mitotic recombination is one way that a cell heterozygous for a mutation in a tumour suppressor gene loses its only wild-type allele. A crossover between the centromere and the gene, followed by x segregation, makes one daughter cell homozygous for the mutant allele for the whole distal part of the arm, while markers proximal to the crossover stay heterozygous. This pattern, **loss of heterozygosity** (LOH) for a segment ending at a crossover point, was found by Cavenee and colleagues (1983) in retinoblastomas of patients heterozygous for an *RB1* mutation, and it is one of the mechanisms of the second hit in Knudson's model (**two-hit hypothesis**, [7.3.26](/7.3.26); its genetics in [7.4.21](/7.4.21)). Variation in when and where such somatic events occur also contributes to the incomplete penetrance and variable expressivity of hereditary cancer syndromes. Bloom syndrome, in which loss of the BLM helicase raises mitotic crossing over between sister chromatids and homologues, gives a direct demonstration: patients have many more LOH events in their somatic cells and a high risk of many cancers ([7.2.9](/7.2.9#sec-9.5.1)).

## Summary

- Tetrad analysis (Definition 9.1.1) examines all four products of one meiosis; unordered tetrads (yeast) give linkage between loci, ordered tetrads (*Neurospora*) also give distances to centromeres (Definition 9.1.2).
- Tetrad types (Definition 9.2.1) and their origin:

  | Crossovers between the loci | Tetrad |
  |---|---|
  | none | PD |
  | one | T |
  | two: two-strand / three-strand / four-strand (1:2:1) | PD / T / NPD |

- Linkage test: $\mathrm{PD} = \mathrm{NPD}$ if unlinked; $\chi^2 = (\mathrm{PD} - \mathrm{NPD})^2/(\mathrm{PD} + \mathrm{NPD})$ (9.2.2).
- $r = (\mathrm{NPD} + \frac12\mathrm{T})/n$ (Formula 9.2.1); Perkins $d = 50(\mathrm{T} + 6\,\mathrm{NPD})/n$ (Formula 9.2.2); exact frequencies without interference $\mathrm{T} = \frac23(1 - \mathrm{e}^{-3d})$, $\mathrm{NPD} = \frac16(1 - 3\mathrm{e}^{-2d} + 2\mathrm{e}^{-3d})$ (Formula 9.2.3; Example 9.2.1).
- Ordered tetrads: MI and MII patterns (Definition 9.3.1); gene–centromere distance $\frac12\,\%\mathrm{MII}$ (Formula 9.3.1), MII frequency $\frac23(1 - \mathrm{e}^{-3d})$ with limit $2/3$ (Formula 9.3.2); ordering two genes and a centromere (Algorithm 9.3.1); for unlinked loci $\mathrm{T} = x + y - \frac32 xy$ (Formula 9.3.3). Two linked loci give seven classes of ordered asci (9.3.6); the direct gene–centromere distance of a distal gene underestimates the sum of the intervals, as in a three-point cross (Example 9.3.3).
- Tetrads prove crossing over between two of four chromatids (9.4.1), show little chromatid interference (9.4.2) and reveal gene conversion (Definition 9.4.1): 3:1, 6:2, 5:3 and aberrant 4:4 asci, the trace of heteroduplex DNA and mismatch repair.
- Mitotic recombination (Definition 9.5.1) followed by x segregation makes distal markers homozygous: twin spots for exchanges proximal to both markers, single spots for exchanges between them (9.5.2); genetic mosaics (Definition 9.5.2), FLP/FRT and MARCM clones; LOH in cancer (9.5.4).

## Questions

1. Why can tetrad analysis prove that crossing over occurs at the four-chromatid stage, whereas random-spore analysis cannot?

   **Answer** Random spores only give the proportion of recombinant products, which would be the same whether exchange involved two of four chromatids or whole chromosomes. Tetrads show the products of single meioses: if exchange happened before replication, every meiosis would give two identical pairs (PD or NPD only). The frequent tetratypes, containing all four combinations, show that one exchange involves only two of four chromatids.

2. A yeast cross $AB \times ab$ gives 160 PD, 2 NPD and 38 T tetrads. Are the loci linked? Compute the recombination frequency and the Perkins distance.

   **Answer** $\chi^2 = (160 - 2)^2/162 = 154$, 1 df: linked. $r = (2 + 19)/200 = 10.5\,\%$; $d = 50(38 + 12)/200 = 12.5\,\mathrm{cM}$.

3. A yeast cross gives 48 PD, 52 NPD and 100 T. What do you conclude about linkage and about the loci's centromeres?

   **Answer** $\chi^2 = (48 - 52)^2/100 = 0.16$, $p = 0.69$: no evidence of linkage, consistent with loci on different chromosomes (or far apart on one). The tetratype frequency $0.5$ depends on the gene–centromere distances: $x + y - \frac32 xy = 0.5$; for example both loci with MII frequency $x = y = 1/3$ (the root of $2x - \frac32 x^2 = 0.5$) would give it.

4. Using Formula 9.2.3, compute the expected PD, NPD and T frequencies for loci $20\,\mathrm{cM}$ apart without interference, and the values of $(\mathrm{NPD} + \frac12\mathrm{T})$ and Perkins' distance they imply.

   **Answer** $\mathrm{T} = \frac23(1 - \mathrm{e}^{-0.6}) = 0.301$, $\mathrm{NPD} = \frac16(1 - 3\mathrm{e}^{-0.4} + 2\mathrm{e}^{-0.6}) = 0.0144$, $\mathrm{PD} = 0.685$. $r = 0.0144 + 0.150 = 0.165$; Perkins $50(0.301 + 0.086) = 19.4\,\mathrm{cM}$, close to the true $20$.

5. Derive Perkins' formula and state its assumptions.

   **Answer** Assume at most two crossovers in the interval and no chromatid interference (double crossovers two-, three- and four-strand in the ratio 1:2:1). With proportions $s$ (one crossover) and $q$ (two) of meioses, $\mathrm{NPD}/n = q/4$ and $\mathrm{T}/n = s + q/2$. The mean number of crossovers per bivalent is $s + 2q = \mathrm{T}/n - 2\,\mathrm{NPD}/n + 8\,\mathrm{NPD}/n = (\mathrm{T} + 6\,\mathrm{NPD})/n$; map distance is half the mean per bivalent, i.e. $50(\mathrm{T} + 6\,\mathrm{NPD})/n$ in cM.

6. In a *Neurospora* cross, 64 of 400 asci show an MII pattern for a spore-colour gene. What is the gene–centromere distance by Formula 9.3.1 and by Formula 9.3.2?

   **Answer** MII $= 0.16$: simple $8.0\,\mathrm{cM}$; corrected $-\frac13\ln(1 - 0.24) = 0.0915\,\mathrm{M} = 9.1\,\mathrm{cM}$.

7. A locus shows MII in 62 % of asci. What can you say about its distance from the centromere? What would 75 % mean?

   **Answer** Under no interference, $d = -\frac13\ln(1 - 0.93) = 0.89\,\mathrm{M}$, but near the limit $2/3$ the estimate is very imprecise: the locus is far from its centromere, effectively unlinked to it. 75 % exceeds $2/3$, which is impossible under the no-interference model; it indicates strong chiasma interference, with the interval between gene and centromere almost always receiving exactly one crossover (MII in every such ascus) and rarely two.

8. In ordered asci, gene $a$ shows MII in 12 % and gene $b$ in 20 % of asci, and the recombination frequency between $a$ and $b$ is 16 %. Draw the map.

   **Answer** $d_a = 6\,\mathrm{cM}$, $d_b = 10\,\mathrm{cM}$; $d_a + d_b = 16 \approx r_{ab}$, so $a$ and $b$ are on opposite arms: $a$ —$6$— centromere —$10$— $b$.

9. Two unlinked loci have MII frequencies $x = 0.1$ and $y = 0.3$. What fraction of unordered tetrads are tetratypes, PD and NPD?

   **Answer** $\mathrm{T} = 0.1 + 0.3 - 1.5 \times 0.03 = 0.355$; $\mathrm{PD} = \mathrm{NPD} = 0.3225$.

10. A diploid yeast heterozygous $leu2\text{-}1/leu2\text{-}2$ (two different mutant sites in *LEU2*) gives occasional Leu⁺ spores. How can such spores arise, and how would you distinguish crossing over from gene conversion with flanking markers?

    **Answer** A Leu⁺ allele requires combining the wild-type sites of both mutant alleles on one chromatid, either by a crossover between the two sites (reciprocal: the same tetrad also has a double-mutant chromatid) or by conversion of one mutant site to wild type (nonreciprocal: the tetrad has 3:1 segregation at that site and no double mutant). Flanking markers distinguish them: a crossover recombines the flanking markers in the Leu⁺ spore, while conversion may occur with or without exchange of flanking markers, and in tetrads the site shows 3:1 segregation.

11. Explain why an *Ascobolus* ascus can show 5:3 segregation of a spore-colour allele, but a yeast tetrad cannot show the corresponding pattern.

    **Answer** In eight-spored asci each meiotic product divides once more by mitosis, separating the two strands of its DNA into the two spores of a pair. If a product carried unrepaired heteroduplex DNA (one strand of each allele), the two spores differ, giving 5:3 (or aberrant 4:4). Yeast forms only four spores without a post-meiotic mitosis, so the heteroduplex is replicated within a growing colony and appears as a sectored colony rather than a distinct spore ratio.

12. In a female $y\,sn^{+}/y^{+}\,sn$, explain why single singed spots are much rarer than single yellow spots, and what spots a female $y\,sn/y^{+}\,sn^{+}$ (coupling) would show.

    **Answer** In repulsion, a single yellow spot needs one exchange between $sn$ and $y$ (with x segregation), whereas a singed spot without a yellow twin requires the distal $y^{+}$ to stay heterozygous while $sn$ becomes homozygous, which needs two exchanges, one on each side of $sn$. In coupling, an exchange between the centromere and $sn$ makes one daughter $y\,sn/y\,sn$ (a yellow singed spot) and the other $y^{+}\,sn^{+}/y^{+}\,sn^{+}$ (wild type, invisible); an exchange between $sn$ and $y$ gives single yellow spots. There are no twin spots.

13. Mitotic crossovers in a chromosome arm occur in a cell lineage at $10^{-5}$ per cell division, uniformly along the arm, and a tumour suppressor gene lies at the middle of the arm. In a heterozygous person, a tissue arises by $10^{9}$ divisions. How many cell lineages become homozygous mutant by this route?

    **Answer** Crossovers proximal to the gene occur at $0.5 \times 10^{-5}$ per division. Half of them are followed by x segregation, which gives one homozygous mutant daughter (and one homozygous wild-type daughter): $2.5 \times 10^{-6}$ per division. Over $10^{9}$ divisions about $2.5 \times 10^{3}$ homozygous mutant lineages arise, which is why somatic LOH is frequent enough to provide the second hit.

14. (Design) You want to see the phenotype of cells homozygous for a recessive lethal mutation $l$ on chromosome arm 2R of *Drosophila*. Describe a FLP/FRT experiment and what you would see.

    **Answer** Make flies $\mathit{FRT42D}\ l/\mathit{FRT42D}\ \mathit{ubi\text{-}GFP}$ carrying *hs-FLP* (or a tissue-specific FLP). Heat shock in larvae induces FLP-mediated exchange at the FRT sites in G2; x segregation gives twin clones: $l/l$ cells lacking GFP next to a twin with two GFP copies (brighter), in a background with one copy. The phenotype of the GFP-negative clone shows what the gene does in those cells, and comparing with the twin controls for the timing and size of the clone.

15. A pink strain of *Neurospora* is crossed with a white mutant strain. What fraction of the ascospore colonies is pink? A zygote of genotype $Rr\,Tt$ (two unlinked genes) undergoes meiosis and the post-meiotic mitosis: which of $Rr\,Tt$, $RR\,TT$, $Rr$ and $rt$ can be the genotype of an ascospore?

    **Answer** One half, whatever the dominance relation between the alleles: ascospores are haploid, each receives one allele, and segregation gives $4 : 4$ in every ascus. For the same reason an ascospore carries one allele of each gene: only $rt$ is possible ($Rr\,Tt$ and $RR\,TT$ are diploid genotypes, $Rr$ has two alleles of one gene and none of the other).

16. A cross of a spore-colour mutant $w$ with wild type gives 300 ordered asci: 128 $w\,w\,w\,w\,+\,+\,+\,+$ and 136 $+\,+\,+\,+\,w\,w\,w\,w$ (spores listed from the tip), and 9, 10, 8 and 9 asci of the four MII arrangements. Compute the gene–centromere distance with Formulas 9.3.1 and 9.3.2.

    **Answer** MII asci $9 + 10 + 8 + 9 = 36$, $12\,\%$; Formula 9.3.1 gives $6.0\,\mathrm{cM}$. Formula 9.3.2: $-\frac13\ln(1 - 0.18) = 0.066\,\mathrm{M} = 6.6\,\mathrm{cM}$.

17. A cross $a\,b^{+} \times a^{+}\,b$ gives 500 ordered asci in the seven classes of 9.3.6: class 1, 374; class 2, 2; class 3, 78; class 4, 38; class 5, 2; class 6, 2; class 7, 4. Are the loci linked? Draw the map with the centromere.

    **Answer** $\mathrm{PD} = 374 + 2 = 376$, $\mathrm{NPD} = 2 + 2 = 4$: $\chi^2 = 372^2/380 = 364$, linked. MII at $a$: classes 4–7, 46 asci, $d_a = 4.6\,\mathrm{cM}$; MII at $b$: classes 3 and 5–7, 86 asci, $d_b = 8.6\,\mathrm{cM}$. $\mathrm{T} = 78 + 38 + 4 = 120$, $r_{ab} = (4 + 60)/500 = 12.8\,\%$ (Perkins $14.4\,\mathrm{cM}$). Since $r_{ab} \approx d_a + d_b = 13.2$ and not $\lvert d_a - d_b\rvert = 4.0$, the genes are on opposite arms: $a$ —$4.6$— centromere —$8.6$— $b$. The other signatures agree: classes 3 and 4 are both common (each is a single crossover in one arm), and of the 46 asci with MII at $a$ only 8 ($17\,\%$) also show MII at $b$, as expected if crossovers in the two arms are independent ($2 \times 0.086 = 17\,\%$).

18. In Example 9.3.3, explain why class 4 asci contribute to the $a$–$b$ recombination and to the centromere–$a$ distance but not to the centromere–$b$ distance, and why this makes the direct estimate of $d_b$ too small.

    **Answer** A class 4 ascus has one crossover between the centromere and $a$ and one between $a$ and $b$. The chromatids involved are recombinant for each short interval, so they are counted for centromere–$a$ (MII at $a$) and for $a$–$b$ (tetratype). Between the centromere and $b$ the two exchanges cancel and $b$ segregates at the first division, so the ascus is counted as nonrecombinant for centromere–$b$. Two crossovers occurred in the centromere–$b$ interval but none is seen there, exactly as double crossovers are invisible to the outer genes of a three-point cross; adding the short intervals recovers them.

