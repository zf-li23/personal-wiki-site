---
title: Linkage, Recombination and Genetic Mapping
description: Linkage and its discovery, crossing over as the physical basis of recombination, recombination frequency and the centimorgan, two-point and three-point testcrosses, double crossovers, coincidence and interference, the Haldane and Kosambi mapping functions, estimating recombination frequency from testcrosses and F2 data by maximum likelihood, the chi-square test for linkage, and the nonuniform landscape of recombination that separates genetic from physical maps.
---

The **law of independent assortment** holds only for genes on different chromosomes. Genes that lie on the same chromosome tend to be transmitted together, and the exceptions, the offspring in which the parental combinations of **alleles** have been reshuffled, arise from **crossing over** between **homologous chromosomes** in **meiosis** ([7.4.5](/7.4.5)). This chapter turns that observation into a measuring instrument. The proportion of recombinant offspring increases with the distance between two genes, so counts of offspring from well-designed crosses place genes in a linear order with distances in centimorgans: a genetic map. Building maps is the oldest quantitative method of genetics and still one of the most used; it is a small exercise in probability (the number and placement of crossovers), estimation (recombination frequency and its standard error, maximum likelihood from F2 data) and testing (is there linkage at all?). The cell mechanics of pairing, synapsis and chiasmata are described in [7.3.21](/7.3.21#sec-21.7.2) and the molecular mechanism of meiotic recombination in [7.2.9](/7.2.9#sec-9.5.2); here we use only their genetic consequences. Tetrad analysis in fungi, which observes all four products of one meiosis, follows in [7.4.9](/7.4.9), the mapping of bacterial genes by conjugation and transduction in [7.4.10](/7.4.10), and the mapping of human disease genes with LOD scores in [7.4.14](/7.4.14).

## 8.1. Linkage

### 8.1.1. Too Many Parental Types

In 1905 Bateson, Saunders and Punnett crossed sweet peas that differed in flower colour (purple $P$, dominant over red $p$) and pollen shape (long $L$, dominant over round $l$). The F2 of a $PP\,LL \times pp\,ll$ cross was very far from 9:3:3:1: of 6952 plants, 4831 were purple long, 390 purple round, 393 red long and 1338 red round. The two parental combinations were in excess and the two new combinations were rare. Each character on its own segregated normally (purple : red $5221 : 1731$, long : round $5224 : 1728$, both close to $3:1$), so the departure lay in the combination of the two loci, not in either of them. In a second cross, purple round by red long ($PP\,ll \times pp\,LL$), the F2 of 419 plants consisted of 226 purple long, 95 purple round, 97 red long and only 1 red round: now the combinations brought in by the parents (purple round, red long) were in excess and the double recessive was almost absent (Example 8.6.2). Bateson spoke of "coupling" of the dominant factors in the first cross and of "repulsion" in the second, but had no explanation. Morgan found the same pattern in *Drosophila* in 1911 with the X-linked genes *white* ($w$, white eyes) and *yellow* ($y$, yellow body): females heterozygous for both genes transmitted to their sons mostly the two allele combinations they had received from their parents, whichever those were, and only about $1\,\%$ new combinations. Because the sons receive their single X from the mother, the sons' phenotypes read the mother's gametes directly.

**Definition 8.1.1 (Parental and Recombinant Types)** Consider an individual heterozygous at two loci that received the haplotypes $AB$ and $ab$ from its two parents. Its gametes (and the offspring that display them) carrying $AB$ or $ab$ are **parental types**; those carrying $Ab$ or $aB$ are **recombinant types**. The classification is defined by the haplotypes of the previous generation, not by dominance or by the alleles themselves: in a heterozygote that received $Ab$ and $aB$, the gametes $Ab$ and $aB$ are parental.

**Definition 8.1.2 (Linkage)** Two loci show **linkage** when a double heterozygote produces parental-type gametes more often than recombinant-type gametes, that is, when the proportion of recombinant gametes is less than $1/2$. Loci that assort independently (proportion $1/2$) are unlinked.

Under independent assortment a dihybrid makes the four gametes in equal proportions, so half its gametes are recombinant; linkage is any departure toward fewer. The degree of linkage varies from almost complete (such as $w$ and $y$) to none detectable.

### 8.1.2. Coupling and Repulsion

**Definition 8.1.3 (Coupling and Repulsion)** In a double heterozygote at two linked loci, the dominant (or wild-type) alleles are in **coupling** (cis configuration) when they are on the same chromosome, $AB/ab$, and in **repulsion** (trans configuration) when they are on different homologues, $Ab/aB$. The arrangement is called the phase of the double heterozygote.

We write genotypes of linked loci with a slash between the haplotypes of the two homologues: $AB/ab$, or with gene symbols $w\,y^{+}/w^{+}\,y$. Phase decides which gametes are parental, and therefore which offspring are frequent: a testcross of $AB/ab$ gives mostly $AB$ and $ab$ phenotypes, a testcross of $Ab/aB$ mostly $Ab$ and $aB$. The recombination frequency itself does not depend on phase (Morgan's two series of crosses with $w$ and $y$ gave the same $\approx 1\,\%$).

### 8.1.3. Testcrosses Detect Linkage

**Example 8.1.1** A *Drosophila* female from a cross of a wild-type male with a black ($b$), vestigial ($vg$) female is $b^{+}\,vg^{+}/b\,vg$ (coupling). Testcrossed to a $b\,vg/b\,vg$ male, she gives 1000 offspring: 405 wild type, 415 black vestigial, 92 black and 88 vestigial. The parental types (wild type, black vestigial) are $820$, the recombinant types $180$, so the proportion of recombinants is $180/1000 = 0.18 < 1/2$: the genes are linked. In a testcross each offspring's phenotype reveals the female's gamete, which is why the testcross is the standard design for mapping.

## 8.2. Crossing Over Is the Basis of Recombination

### 8.2.1. The Cytological Proof

Morgan proposed in 1911 that recombinant types arise when homologous chromosomes exchange segments, an idea suggested by the chiasmata that Janssens had seen in meiotic prophase. The proof that genetic recombination is accompanied by a physical exchange came in 1931. Harriet Creighton and Barbara McClintock used a maize chromosome 9 that was cytologically marked at both ends, with a heterochromatic knob at one end and a segment of chromosome 8 attached by a translocation at the other, and carried the dominant alleles $C$ (coloured aleurone) and $Wx$ (starchy endosperm) near the two marks. In a plant heterozygous for this chromosome and a normal homologue carrying $c$ and $wx$, offspring that were recombinant for $C$ and $Wx$ had also exchanged the cytological marks, and parental-type offspring had not. Curt Stern obtained the same result in *Drosophila* with two X chromosomes of distinct shapes, one broken into two pieces and the other carrying a piece of the Y, marked with *carnation* and *Bar*.

### 8.2.2. Crossing Over Happens Between Two of Four Chromatids

Crossing over occurs in prophase I, after DNA replication, when each bivalent consists of four chromatids; a single exchange involves only two of them, one from each homologue (the evidence from tetrads is given in [7.4.9](/7.4.9#sec-9.4)). One crossover between two loci therefore produces two recombinant and two parental chromatids, and a meiosis with one crossover in an interval gives recombinant gametes with probability $1/2$, not $1$ (Figure). This is the origin of most of the arithmetic of this chapter.

![One and two crossovers at the four-chromatid stage. Each row of four bars is a bivalent: the two upper chromatids (blue) are sisters of one homologue, the two lower (pink) of the other, joined at the centromere (grey oval, left); A/a and B/b are two loci, and each X marks a crossover between the two chromatids it joins. (A) One crossover between the loci gives two recombinant (R) and two parental (P) chromatids. (B) The four kinds of double crossover between the same two loci: a two-strand double (both exchanges between the same pair of chromatids) gives no recombinant chromatids, the two kinds of three-strand double give two each, and a four-strand double gives four. If the chromatids involved in the second exchange are chosen at random, the four kinds are equally likely, and on average half the products are recombinant.](./plots/crossovers-four-chromatids.py)

Two features of crossing over matter for mapping. First, every bivalent normally has at least one crossover (the obligate crossover), because the chiasma it forms is what holds homologues together until anaphase I ([7.3.21](/7.3.21#sec-21.7.2)); chromosomes without a chiasma risk **nondisjunction** ([7.4.6](/7.4.6)). Second, crossovers on one bivalent are not placed independently: a crossover reduces the chance of another nearby (8.4.3). Crossing over also has a biological function beyond segregation: it creates new combinations of alleles on the same chromosome, and therefore variation on which selection can act.

## 8.3. Recombination Frequency and the Genetic Map

### 8.3.1. Recombination Frequency and the Centimorgan

**Definition 8.3.1 (Recombination Frequency)** The **recombination frequency** $r$ (recombination fraction, RF) between two loci is the probability that a gamete of a double heterozygote is recombinant for them. It is estimated as the proportion of recombinant offspring in a cross in which every offspring's genotype reveals the gamete, such as a testcross: $\hat r = R/n$ for $R$ recombinants among $n$ offspring.

**Definition 8.3.2 (Centimorgan)** The **centimorgan** (cM, map unit, m.u.) is the unit of genetic map distance: two loci are $1\,\mathrm{cM}$ apart when they are separated by a distance in which on average $0.01$ crossovers occur per chromatid per meiosis. For short distances, where multiple crossovers are negligible, $1\,\mathrm{cM}$ corresponds to $r = 1\,\%$. One hundred centimorgans are one morgan (M), after T. H. Morgan.

The distinction between recombination frequency (an observable, at most $1/2$) and map distance (the expected number of crossovers, which can exceed $1/2$) is the subject of 8.5. In Example 8.1.1, $\hat r = 0.18$, so $b$ and $vg$ are about $18\,\mathrm{cM}$ apart (their standard map positions are $2$-$48.5$ and $2$-$67.0$, a difference of $18.5\,\mathrm{cM}$).

### 8.3.2. Why Recombination Frequency Never Exceeds One Half

The logic of the last section gives a short proof. Let $K$ be the number of crossovers in the interval between two loci on a bivalent, and assume that each crossover involves two non-sister chromatids chosen at random, independently of the others (no chromatid interference). Follow one chromatid: each crossover involves it with probability $1/2$, and the chromatid is recombinant if it was involved in an odd number of them.

**Formula 8.3.1 (Mather's Formula)** With no chromatid interference,

$$
r = \tfrac12\bigl(1 - \mathbb{P}(K = 0)\bigr),
$$
where $\mathbb{P}(K = 0)$ is the probability that the bivalent has no crossover in the interval.

**Proof** Given $K = k \ge 1$, the number of crossovers involving the chromatid is $\mathrm{Bin}(k, 1/2)$, and a binomial variable with $p = 1/2$ is odd with probability $\tfrac12\bigl(1 - (1 - 2p)^k\bigr) = \tfrac12$. Given $K = 0$ the chromatid is parental. Averaging over $K$ gives the formula. $\square$

So $r \le 1/2$ for any distance, with $r \to 1/2$ as the interval becomes long enough to be almost certain to contain a crossover. Genes far apart on the same chromosome behave like genes on different chromosomes: they are syntenic (on the same chromosome) but genetically unlinked. Linkage is a genetic statement (can parental types be shown to be in excess?), synteny a physical one.

**Remark 8.3.1 (Meiocytes with a Crossover)** For an interval short enough never to receive more than one crossover, $\mathbb{P}(K = 0) = 1 - p_{\mathrm{x}}$, where $p_{\mathrm{x}}$ is the proportion of meiocytes (spermatocytes, oocytes, pollen or megaspore mother cells) with a crossover in the interval, and Formula 8.3.1 becomes $r = p_{\mathrm{x}}/2$: the percentage of meiocytes with a chiasma between two loci is twice the recombination frequency. If $16\,\%$ of meiocytes have a chiasma between two loci, $r = 8\,\%$; conversely $r$ cannot exceed $1/2$ even if every meiocyte has a crossover in the interval. Older textbooks call the recombination frequency the "crossover value"; strictly the two differ, because the mean number of crossovers per chromatid (the map distance, 8.5) exceeds the recombination frequency as soon as multiple crossovers occur, and the textbook phrase "actual crossover value = recombination value + 2 × double-crossover value" is the three-point correction of Algorithm 8.4.1.

### 8.3.3. Genetic Maps and Linkage Groups

Alfred Sturtevant, an undergraduate in Morgan's laboratory, realized in 1911 that recombination frequencies could serve as distances: if they are approximately additive, so that $r_{AC} \approx r_{AB} + r_{BC}$ for three loci, the genes must lie in a line. In 1913 he published the first map, of five X-linked genes of *Drosophila*.

**Definition 8.3.3 (Genetic Map)** A **genetic map** (linkage map) is the linear order of loci on a chromosome with the distances between them in centimorgans, derived from recombination frequencies. Positions are given from one end; in *Drosophila* a position is written with the chromosome, as $2$-$48.5$ for *black*.

![The first genetic map and today's. Left: Sturtevant's 1913 map of the *Drosophila* X chromosome from recombination between yellow body (*y*), white eyes (*w*), vermilion eyes (*v*), miniature wings (*m*) and rudimentary wings (*r*), positions in centimorgans from *y*. Right: the standard map positions of the same genes today; dashed lines join the same gene. The order is unchanged; the positions of the distal genes have shifted a few map units, mainly because Sturtevant's longer intervals underestimated distance (double crossovers, 8.4.2) and because later maps add many short intervals.](./plots/sturtevant-map.py)

**Definition 8.3.4 (Linkage Group)** A **linkage group** is a set of loci each of which is linked to at least one other member, directly or through a chain of linked loci. In a well-mapped organism the number of linkage groups equals the haploid number of chromosomes: four in *D. melanogaster*, ten in maize, 23 in humans (counting X; Y is largely not recombining).

Two genes at the ends of a long chromosome may show $r = 1/2$ in a direct cross and still belong to the same linkage group because each is linked to genes between them. This is how the map of a chromosome exceeds $50\,\mathrm{cM}$: the $X$ map of *Drosophila* is about $66\,\mathrm{cM}$ long, chromosome 2 about $107\,\mathrm{cM}$.

Two conventions of classical maps follow from building them gene by gene. Positions are counted from the gene nearest one end, which is placed at $0$; when a new gene is found beyond it, the zero is moved to the new gene and all positions are shifted (the *Drosophila* positions above have kept their historical zero at *yellow*, near the tip of the X). And in a poorly mapped organism the number of linkage groups can differ from the haploid number in either direction: chromosomes on which no marker has been found are missing, and the markers of one long chromosome may form two groups until markers between them connect the two. In the heterogametic sex the X and the Y are separate linkage groups except for the pseudoautosomal region ([7.4.6](/7.4.6)).

## 8.4. Two-Point and Three-Point Crosses

### 8.4.1. Two-Point Crosses and Their Limits

**Definition 8.4.1 (Two-Point and Three-Point Crosses)** A **two-point cross** measures the recombination frequency between two loci in a double heterozygote; a **three-point cross** follows three linked loci in one cross, usually a testcross of a triple heterozygote, which gives eight classes of offspring.

Two-point crosses can order genes (the pair with the largest distance flanks the third), but they have two weaknesses. Small differences are within sampling error: Sturtevant's data gave $y$–$m$ $34.3\,\%$ and $w$–$m$ $33.8\,\%$, which cannot order $y$ and $w$ relative to $m$ unless the samples are very large (the standard error of $\hat r = 0.34$ from 1000 flies is $0.015$, 8.6.1). And the distances do not add exactly: the recombination frequency of a long interval is less than the sum of its parts, because two crossovers within it restore the parental combination. A three-point cross solves both problems in one experiment.

### 8.4.2. The Three-Point Testcross

**Definition 8.4.2 (Double Crossover)** In a three-point cross with loci in the order $A$–$B$–$C$, a **double crossover** (DCO) gamete is one recombinant in both intervals, $A$–$B$ and $B$–$C$; relative to the parental haplotypes, it has exchanged only the allele of the middle locus.

If crossovers in the two intervals occurred independently, the probability of a double crossover gamete would be $r_1 r_2$, the product of the two recombination frequencies; for $r_1, r_2$ of a few percent this is by far the rarest class. The eight classes therefore come in four pairs of reciprocal products of about equal size: the two parental classes (largest), two pairs of single crossovers, one in each interval, and the double crossovers (smallest). Since a double crossover changes only the middle allele, comparing the double-crossover classes with the parental classes identifies the middle gene.

**Algorithm 8.4.1 (Analysis of a Three-Point Testcross)**

1. Group the eight phenotypic classes into four reciprocal pairs (two classes whose alleles are complementary at all three loci).
2. The largest pair are the parental haplotypes of the triple heterozygote; the smallest pair are the double crossovers.
3. Find the locus at which the double crossovers differ from the parental haplotypes that they otherwise resemble: that locus is in the middle. Rewrite all haplotypes in the gene order.
4. The pair recombinant only between the first and middle locus are single crossovers in interval 1, the pair recombinant only between the middle and the last locus are single crossovers in interval 2.
5. Compute each interval's recombination frequency counting the double crossovers in both: $r_1 = (\mathrm{SCO}_1 + \mathrm{DCO})/n$, $r_2 = (\mathrm{SCO}_2 + \mathrm{DCO})/n$.
6. The map distance between the outer genes is $r_1 + r_2$ (in percent, cM). The outer genes' direct recombination frequency, $(\mathrm{SCO}_1 + \mathrm{SCO}_2)/n$, is smaller by $2\,\mathrm{DCO}/n$.
7. Compute the expected number of double crossovers $r_1 r_2 n$, the coefficient of coincidence $C = \mathrm{DCO}/(r_1 r_2 n)$ and the interference $I = 1 - C$ (8.4.3).

**Remark 8.4.1** The algorithm assumes that all three loci are linked. Before applying it, collapse the data to each pair of loci and check the pair for linkage (Algorithm 8.7.1). If one locus assorts independently of the other two, the eight classes form four pairs of nearly equal size that differ only at that locus; the two smallest classes are then not double crossovers, and the data are analysed as a two-point cross of the linked pair. If only four classes appear, two of the loci are completely linked in the heterozygous parent (8.7.2) or too close for any recombinant to be seen in the sample.

**Example 8.4.1** A *Drosophila* female heterozygous for the recessive second-chromosome mutations $b$ (black body), $pr$ (purple eyes) and $vg$ (vestigial wings) is testcrossed with a $b\,pr\,vg/b\,pr\,vg$ male. The 4000 offspring, listed by the female's gamete, are:

| Gamete | Number | | Gamete | Number |
|---|---|---|---|---|
| $b^{+}\,pr\,vg^{+}$ | 1640 | | $b^{+}\,pr\,vg$ | 247 |
| $b\,pr^{+}\,vg$ | 1632 | | $b\,pr^{+}\,vg^{+}$ | 241 |
| $b\,pr\,vg^{+}$ | 118 | | $b^{+}\,pr^{+}\,vg^{+}$ | 5 |
| $b^{+}\,pr^{+}\,vg$ | 110 | | $b\,pr\,vg$ | 7 |

The parental haplotypes are $b^{+}\,pr\,vg^{+}$ and $b\,pr^{+}\,vg$ (1640, 1632); the double crossovers are $b^{+}\,pr^{+}\,vg^{+}$ and $b\,pr\,vg$ (5, 7). The double crossover $b^{+}\,pr^{+}\,vg^{+}$ differs from the parental $b^{+}\,pr\,vg^{+}$ only at $pr$, so $pr$ is in the middle, and the parental haplotypes in gene order are $b^{+}\,pr\,vg^{+}$ and $b\,pr^{+}\,vg$ (the order of the list happened to be correct). The classes $b\,pr\,vg^{+}$ and $b^{+}\,pr^{+}\,vg$ (118 + 110) changed the $b$ allele relative to $pr$ and $vg$, so they are single crossovers in interval $b$–$pr$; the classes $b^{+}\,pr\,vg$ and $b\,pr^{+}\,vg^{+}$ (247 + 241) are single crossovers in $pr$–$vg$. Then

$$
r_{b\text{–}pr} = \frac{228 + 12}{4000} = 0.060, \qquad r_{pr\text{–}vg} = \frac{488 + 12}{4000} = 0.125,
$$
and the map is $b$ —$6.0\,\mathrm{cM}$— $pr$ —$12.5\,\mathrm{cM}$— $vg$, with $b$–$vg$ $18.5\,\mathrm{cM}$. The direct recombination frequency between $b$ and $vg$ in the same data is $(228 + 488)/4000 = 17.9\,\%$: a two-point cross of the outer genes would miss the 24 chromatids (12 gametes counted twice) in which two crossovers cancelled.

![The eight gamete classes of the three-point testcross of Example 8.4.1, drawn in map order *b* – *pr* – *vg*. Each bar is the chromatid that the F1 female transmitted, coloured by the parental homologue it came from (blue: *b*⁺ *pr* *vg*⁺; pink: *b* *pr*⁺ *vg*); a change of colour marks a crossover in that interval. The double crossovers (bottom pair) have exchanged only the middle gene, which identifies *pr* as the middle locus.](./plots/three-point-cross.py)

The procedure is easy to automate, which is how one checks hand calculations:

```python
def three_point(counts):
    """counts: {haplotype tuple such as ('b+', 'pr', 'vg+'): number}. Returns order, r1, r2, C."""
    n = sum(counts.values())
    hap = sorted(counts, key=counts.get, reverse=True)
    p1, p2, dco = hap[0], hap[1], hap[-1]          # parental classes, one double-crossover class
    near = min((p1, p2), key=lambda p: sum(a != b for a, b in zip(p, dco)))
    mid = next(k for k in range(3) if dco[k] != near[k])   # the locus switched in the DCO
    order = [k for k in range(3) if k != mid]
    order.insert(1, mid)
    def switched(h, i, j):                          # recombinant between loci i and j?
        return (h[i] == p1[i]) != (h[j] == p1[j])
    a, b, c = order
    r1 = sum(m for h, m in counts.items() if switched(h, a, b)) / n
    r2 = sum(m for h, m in counts.items() if switched(h, b, c)) / n
    d = sum(m for h, m in counts.items() if switched(h, a, b) and switched(h, b, c)) / n
    return order, r1, r2, d / (r1 * r2)
```

### 8.4.3. Coincidence and Interference

In Example 8.4.1 independence would predict $r_1 r_2 n = 0.060 \times 0.125 \times 4000 = 30$ double crossovers, but only 12 were seen. A deficit of double crossovers is the rule in most organisms.

**Definition 8.4.3 (Coefficient of Coincidence and Interference)** For two adjacent intervals with recombination frequencies $r_1$ and $r_2$, the **coefficient of coincidence** is the ratio of observed to expected double crossovers,

$$
C = \frac{\text{observed DCO frequency}}{r_1 r_2},
$$
and the **interference** is $I = 1 - C$. $I = 0$ means that crossovers in the two intervals occur independently; $I = 1$ (complete interference) that a crossover in one interval prevents a crossover in the other; $I < 0$ (negative interference) that double crossovers are in excess.

In Example 8.4.1, $C = 12/30 = 0.40$ and $I = 0.60$. Interference here is crossover interference: it acts between chiasmata along a bivalent, with the strongest effect over short distances, and in most organisms it is nearly complete over $10$–$20\,\mathrm{cM}$ and fades with distance (Figure in 8.5.3). It is mediated by the synaptonemal complex and the axis of the meiotic chromosome, which spread an inhibitory signal from a designated crossover; one model treats the axis as a beam relieving mechanical stress (Kleckner). A second kind of interference, chromatid interference, would be a non-random choice of the chromatids involved in successive exchanges; it is weak or absent in most organisms tested by tetrad analysis ([7.4.9](/7.4.9#sec-9.4)), and the formulas of this chapter assume it is absent. Negative interference is found in fine-scale crosses within genes in phage and fungi, where the apparent excess of close double exchanges reflects mismatch repair of heteroduplex DNA in a single recombination event (gene conversion, [7.4.9](/7.4.9#sec-9.4)).

**Example 8.4.2 (Two-Point and Three-Point Data in Maize)** Three genes on maize chromosome 9, $C$/$c$ (coloured or colourless aleurone), $Sh$/$sh$ (full or shrunken endosperm) and $Wx$/$wx$ (starchy or waxy endosperm), were mapped both ways in classical experiments. Three two-point testcrosses gave $r_{C\text{–}Sh} = 3.6\,\%$, $r_{Wx\text{–}Sh} = 20\,\%$ and $r_{Wx\text{–}C} = 22\,\%$, which place $Sh$ in the middle. One three-point testcross of the triple heterozygote gave the map $wx$ —$18.4$— $sh$ —$3.5$— $c$, $21.9\,\mathrm{cM}$ in all, with $0.09\,\%$ double crossovers against $0.184 \times 0.035 = 0.64\,\%$ expected: $C = 0.14$, $I = 0.86$. The three-point distances are slightly smaller than the two-point ones, although only they include the double crossovers. The reason is that the estimates come from different crosses: the plants differed in genetic background, growing conditions and the sex of the heterozygous parent, all of which affect recombination (8.8.1), and each estimate has its own sampling error (for $\hat r = 0.2$ from 1000 kernels, $\operatorname{se} = 0.013$). A map is therefore assembled from estimates made in one design, preferably one multipoint cross with closely spaced markers, rather than by combining distances from different experiments.

## 8.5. Mapping Functions

### 8.5.1. From Recombination Frequency to Map Distance

Map distance $d$ (in morgans) is defined as the expected number of crossovers per chromatid in the interval; since a chiasma involves two of four chromatids, the expected number of chiasmata in the interval per bivalent is $2d$. Map distance is additive by definition (expectations add), while the recombination frequency is not, because multiple crossovers can cancel. A mapping function converts one into the other.

**Definition 8.5.1 (Mapping Function)** A **mapping function** is a function $r = M(d)$ that gives the recombination frequency of an interval of map length $d$, derived from a model of how crossovers are distributed; its inverse $d = M^{-1}(r)$ converts observed recombination frequencies into additive distances. Every mapping function satisfies $M(d) \approx d$ for small $d$ and $M(d) \to 1/2$ as $d \to \infty$.

**Formula 8.5.1 (Haldane Mapping Function)** If crossovers occur as a Poisson process along the chromosome (no interference) and without chromatid interference, then the number of chiasmata in an interval is $K \sim \mathrm{Poi}(2d)$ and

$$
r = \tfrac12\bigl(1 - \mathrm{e}^{-2d}\bigr), \qquad d = -\tfrac12\ln(1 - 2r).
$$

**Proof** By Formula 8.3.1, $r = \frac12\bigl(1 - \mathbb{P}(K = 0)\bigr)$, and for a **Poisson distribution** with mean $2d$, $\mathbb{P}(K = 0) = \mathrm{e}^{-2d}$. Solving for $d$ gives the inverse. $\square$

Haldane derived this in 1919. It is exact for its model and ignores interference, so it overestimates distances where interference is strong. Kosambi (1944) proposed a function in which the coincidence between adjacent short intervals rises with distance as $C = 2r$, so that interference is complete for very close intervals and vanishes at $r = 1/2$; integrating the resulting differential equation $\mathrm{d}r/\mathrm{d}d = 1 - 4r^2$ gives:

**Formula 8.5.2 (Kosambi Mapping Function)**

$$
r = \tfrac12\tanh(2d), \qquad d = \tfrac14\ln\frac{1 + 2r}{1 - 2r}.
$$

**Example 8.5.1** Two loci show $r = 0.30$. The Haldane distance is $-\frac12\ln 0.4 = 0.458\,\mathrm{M} = 45.8\,\mathrm{cM}$; the Kosambi distance is $\frac14\ln(1.6/0.4) = \frac14\ln 4 = 0.347\,\mathrm{M} = 34.7\,\mathrm{cM}$. At $r = 0.05$ they are $5.27$ and $5.02\,\mathrm{cM}$: the choice matters only for long intervals.

| $r$ | 0.05 | 0.10 | 0.20 | 0.30 | 0.40 | 0.45 |
|---|---|---|---|---|---|---|
| Haldane $d$ / cM | 5.3 | 11.2 | 25.5 | 45.8 | 80.5 | 115.1 |
| Kosambi $d$ / cM | 5.0 | 10.1 | 21.2 | 34.7 | 54.9 | 73.6 |

![Mapping functions. Left: recombination frequency r against map distance d for the linear relation r = d (valid for short intervals), the Haldane function (no interference) and the Kosambi function (interference decreasing with distance); both approach the ceiling r = 1/2. Right: the inverse functions, used to convert observed recombination frequencies into additive map distances; for r above about 0.3 the two give very different distances.](./plots/mapping-functions.py)

### 8.5.2. The Choice of Function

Short intervals avoid the problem: a map built from many intervals of less than $10\,\mathrm{cM}$ has almost the same distances under any mapping function, which is why the advice of classical genetics, map with many closely spaced markers, is also the modern practice. Kosambi's function describes most higher eukaryotes better than Haldane's and is the default of most linkage-mapping software for plants and animals; Haldane's is used in human genetics for multipoint calculations because it makes intervals independent (a Markov property that simplifies likelihoods). Neither is a mechanistic model. The relationship of $r$ to the probability $\mathbb{P}(K = 0)$ (Formula 8.3.1) also shows that no mapping function can be exact for all organisms: it depends on how the crossover count is distributed, which differs between species, sexes and chromosomes.

### 8.5.3. A Model of Interference

A model that fits interference in many species is the chi-square (counting) model of Foss, Stahl and colleagues (Zhao, Speed and McPeek 1995): recombination intermediates are placed along the bivalent as a Poisson process, and only every $(m+1)$-th becomes a chiasma, the rest being resolved as noncrossovers. The distances between successive chiasmata then follow a **gamma distribution** with shape $\nu = m + 1$ (rate $2\nu$ per morgan, mean $1/2$ morgan), instead of the exponential distribution of the Poisson case ($\nu = 1$). Estimates are $\nu \approx 4$–$5$ for *Drosophila* and humans and larger for some fungi; organisms with two crossover pathways (budding yeast, *Arabidopsis*, mammals) have a minor interference-free class of crossovers, made by MUS81, in addition to the interfering class made by MutLγ ([7.2.9](/7.2.9#sec-9.5.2)).

![Simulated crossovers with and without interference (100 cM bivalent). (A) Chiasma positions in 25 simulated meioses under the Poisson model (nu = 1, left) and the gamma (chi-square) model with nu = 4 (right): with interference, chiasmata are evenly spaced and almost never close together. (B) Coefficient of coincidence C between two 5 cM intervals as a function of the distance between their centres, estimated from 60 000 simulated chromatids: C stays near 1 without interference, and with interference it is near 0 for close intervals and rises to about 1 beyond 40 to 50 cM. (C) The number of chiasmata per bivalent: Poisson (mean 2, wide) for nu = 1, and far less variable for nu = 4, so that almost every bivalent has at least one chiasma, as the obligate crossover requires.](./plots/interference-simulation.py)

## 8.6. Estimating Recombination Frequency

### 8.6.1. Testcross: the Binomial Estimate

In a testcross each of $n$ offspring is independently recombinant with probability $r$, so the number of recombinants $R \sim \mathrm{Bin}(n, r)$ (**binomial distribution**, [3.1.4](/3.1.4#sec-4.1.3)).

**Formula 8.6.1 (Testcross Estimate)** The **maximum likelihood estimator** of $r$ from a testcross is $\hat r = R/n$, with **standard error**

$$
\operatorname{se}(\hat r) = \sqrt{\frac{\hat r(1 - \hat r)}{n}},
$$
and an approximate $95\,\%$ **confidence interval** $\hat r \pm 1.96\operatorname{se}(\hat r)$.

In Example 8.1.1, $\hat r = 0.18$, $\operatorname{se} = \sqrt{0.18 \times 0.82/1000} = 0.012$, and the $95\,\%$ interval is $0.156$–$0.204$. The standard error scales as $1/\sqrt n$: halving it requires four times as many offspring, which is why ordering genes $1\,\mathrm{cM}$ apart by two-point crosses needs thousands of flies, and why a three-point cross, in which the order is read from the rare double-crossover class instead of from differences between estimates, is more efficient.

### 8.6.2. F2 Data: Selfing and the Square-Root Method

In plants, where selfing is easier than testcrossing, recombination frequency is often estimated from an F2. With complete dominance at both loci, the double heterozygote produces the gametes $AB$, $Ab$, $aB$, $ab$ with frequencies that depend on phase, and only the double-recessive class $aabb$ reveals the gametes unambiguously: it requires an $ab$ gamete from both sides.

**Formula 8.6.2 (Square-Root Method)** In the F2 of a double heterozygote with complete dominance, let $f$ be the observed proportion of $aabb$ offspring. In coupling ($AB/ab$) the $ab$ gamete has frequency $(1 - r)/2$, so $f = \bigl((1 - r)/2\bigr)^2$ and

$$
\hat r = 1 - 2\sqrt{f};
$$
in repulsion ($Ab/aB$) the $ab$ gamete is recombinant, $f = (r/2)^2$, and $\hat r = 2\sqrt{f}$.

The square-root method uses only one of four classes. All the data are used by maximum likelihood. Write $\varphi = (1 - r)^2$ in coupling and $\varphi = r^2$ in repulsion. Summing the 16 cells of the Punnett square of the two (identical) gamete distributions gives the four phenotype classes:

$$
\mathbb{P}(A\_B\_) = \frac{2 + \varphi}{4}, \qquad \mathbb{P}(A\_bb) = \mathbb{P}(aaB\_) = \frac{1 - \varphi}{4}, \qquad \mathbb{P}(aabb) = \frac{\varphi}{4},
$$
which reduce to 9:3:3:1 at $\varphi = 1/4$ ($r = 1/2$).

**Formula 8.6.3 (Maximum Likelihood Estimate from an F2)** With counts $n_1, n_2, n_3, n_4$ in the classes $A\_B\_$, $A\_bb$, $aaB\_$, $aabb$ ($n = \sum n_i$), the **likelihood function** is multinomial and the log-likelihood is

$$
\ell(\varphi) = n_1\ln(2 + \varphi) + (n_2 + n_3)\ln(1 - \varphi) + n_4\ln\varphi + \text{const}.
$$
Setting $\ell'(\varphi) = 0$ gives the quadratic

$$
n\varphi^2 - (n_1 - 2n_2 - 2n_3 - n_4)\varphi - 2n_4 = 0,
$$
whose positive root is $\hat\varphi$; then $\hat r = 1 - \sqrt{\hat\varphi}$ (coupling) or $\hat r = \sqrt{\hat\varphi}$ (repulsion). The **Fisher information** per plant for $\varphi$ is $\sum_i (\partial p_i/\partial\varphi)^2/p_i = \frac{1}{16}\bigl(\frac{4}{2+\varphi} + \frac{8}{1-\varphi} + \frac{4}{\varphi}\bigr)$, and $\operatorname{se}(\hat r) = \operatorname{se}(\hat\varphi)/\lvert \mathrm{d}\varphi/\mathrm{d}r\rvert = \operatorname{se}(\hat\varphi)/(2\sqrt{\hat\varphi})$.

This model is the textbook example of the **EM algorithm**, which treats the $A\_B\_$ class as a mixture of two unobserved cells (the multinomial example of [3.5.6](/3.5.6#sec-6.1.4), whose $\theta$ is our $\varphi$); here the quadratic gives the answer directly.

**Example 8.6.1** Bateson's sweet-pea F2 (8.1.1) is in coupling ($PL/pl$): $n_1 = 4831$, $n_2 = 390$, $n_3 = 393$, $n_4 = 1338$, $n = 6952$. A **goodness-of-fit test** against 9:3:3:1 gives $\chi^2 = 3372$ with 3 **degrees of freedom**, an overwhelming rejection. The quadratic $6952\varphi^2 - (4831 - 1566 - 1338)\varphi - 2676 = 0$, i.e. $6952\varphi^2 - 1927\varphi - 2676 = 0$, has the positive root $\hat\varphi = 0.7743$, so $\hat r = 1 - \sqrt{0.7743} = 0.120$, with $\operatorname{se}(\hat r) = 0.0042$. The square-root method gives $1 - 2\sqrt{1338/6952} = 0.123$, close but less precise. The two genes are about $12\,\mathrm{cM}$ apart (they are on chromosome 7 of *Lathyrus odoratus*).

**Example 8.6.2 (A Repulsion F2)** Bateson's second sweet-pea F2 (8.1.1) came from $Pl/pL$ (repulsion): $n_1 = 226$, $n_2 = 95$, $n_3 = 97$, $n_4 = 1$, $n = 419$. Each locus segregates $3:1$ (purple : red $321 : 98$, long : round $323 : 96$). The square-root method gives $\hat r = 2\sqrt{1/419} = 0.098$. For the MLE, $n_1 - 2n_2 - 2n_3 - n_4 = -159$, so $419\varphi^2 + 159\varphi - 2 = 0$, $\hat\varphi = 0.0122$ and $\hat r = \sqrt{\hat\varphi} = 0.110$, with $\operatorname{se}(\hat r) = 0.048$. The estimate agrees with the coupling cross ($0.120$) but is about eleven times less precise from a sample seventeen times smaller; almost all the information is in the single red round plant (8.6.3).

### 8.6.3. Which Design Is Most Informative?

The amount of information that one offspring carries about $r$ depends on the cross (Figure). For a testcross it is $1/\bigl(r(1 - r)\bigr)$. An F2 with dominant markers in coupling is almost as informative (each F2 plant samples two meioses, but dominance hides much of the information), an F2 with codominant markers (such as DNA markers, [7.4.14](/7.4.14)) is about twice as informative as a testcross for small $r$, and an F2 in repulsion with dominant markers is nearly useless for tight linkage: at $r = 0.05$ one repulsion F2 plant carries about $1/20$ of the information of one testcross offspring, because the class that reveals recombination, $aabb$, has frequency $r^2/4$. Since the variance of $\hat r$ is $1/(n I(r))$, a design with information $I$ needs $n \propto 1/I$ individuals for a given precision.

![Information about the recombination frequency per individual. (A) Fisher information I(r) per offspring for a testcross, an F2 with codominant markers, an F2 with dominant markers in coupling and an F2 with dominant markers in repulsion (log scale); the number of individuals needed for a given standard error is proportional to 1/I(r). (B) The log-likelihood of r for Bateson's sweet-pea F2 (coupling, n = 6952), maximal at r = 0.120; the dashed line is 1.92 units below the maximum and marks the likelihood-based 95 % interval.](./plots/rf-estimation.py)

## 8.7. Testing for Linkage

### 8.7.1. The Chi-Square Test

Before estimating a distance we ask whether the loci are linked at all: is an excess of parental types larger than chance? The natural null hypothesis is $r = 1/2$. A tempting test is the goodness of fit of the four testcross classes to 1:1:1:1, but it has 3 degrees of freedom and rejects for any of three reasons: linkage, unequal segregation at locus $A$, or unequal segregation at locus $B$ (for example lower viability of a mutant). The test that isolates linkage is the test of independence in the $2 \times 2$ **contingency table** of the genotypes at the two loci ([3.2.6](/3.2.6#sec-6.4)), which does not assume 1:1 segregation.

**Algorithm 8.7.1 (Chi-Square Test for Linkage in a Testcross)**

1. Arrange the testcross offspring in a $2 \times 2$ table: rows the genotype at locus $A$ ($Aa$ or $aa$), columns the genotype at locus $B$.
2. Compute expected counts under independence, $E_{ij} = (\text{row}_i \text{ total})(\text{column}_j \text{ total})/n$.
3. Compute $\chi^2 = \sum_{ij}(O_{ij} - E_{ij})^2/E_{ij}$ and compare with the **chi-square distribution** with 1 degree of freedom (critical value $3.84$ at $\alpha = 0.05$, $6.63$ at $0.01$).
4. If the **null hypothesis** of independence is rejected and the parental classes are in excess, conclude that the loci are linked, and estimate $\hat r$.

**Example 8.7.1** For Example 8.1.1 the table is: $b^{+}vg^{+}$ 405, $b^{+}vg$ 88, $b\,vg^{+}$ 92, $b\,vg$ 415. The margins are 493, 507 (rows) and 497, 503 (columns), so for instance $E_{11} = 493 \times 497/1000 = 245.0$. Then $\chi^2 = 409.6$ with 1 degree of freedom, $p \approx 10^{-90}$: strong evidence of linkage. With small samples the decision is much less clear: 40 offspring with 14 recombinants ($\hat r = 0.35$) give $\chi^2 = 3.6$ (if the margins are 20:20), not significant at $5\,\%$, although the genes may well be linked. Sample size is an essential part of any conclusion of "no linkage".

The likelihood ratio of $r = \hat r$ against $r = 1/2$ is the basis of the LOD score of human genetics: the LOD is $\log_{10}$ of this **likelihood ratio** ([3.2.5](/3.2.5#sec-5.3)), $Z = \log_{10}\bigl[\hat r^{R}(1 - \hat r)^{n - R}/(1/2)^n\bigr]$. For Example 8.1.1, $Z = 96.3$. In human families, where each meiosis is precious, the evidence is accumulated across families, and a LOD of 3 is the conventional threshold ([7.4.14](/7.4.14)).

### 8.7.2. Complete Linkage in One Sex

In *Drosophila* males there is no crossing over at all: male meiosis is achiasmate, homologues being held together by special pairing proteins. Two loci on the same chromosome are therefore completely linked when transmitted by a male, and a male double heterozygote in coupling transmits only $AB$ and $ab$. The silkworm *Bombyx mori* has the reverse arrangement, achiasmate female meiosis. In both cases, the sex without crossing over is the heterogametic one. This regularity, that where only one sex lacks crossing over it is the heterogametic sex, is the *Haldane–Huxley rule* (Haldane 1922, Huxley 1928), which holds with few exceptions; it is distinct from Haldane's rule about hybrid sterility of the heterogametic sex in species crosses. In other organisms both sexes cross over but at different rates (8.8.1). This has a practical use: crossing a heterozygous male back to recessive females gives only two classes if two genes are syntenic, a quick test for assignment to a chromosome, and the absence of recombination in males lets *Drosophila* geneticists keep chromosomes intact for generations.

## 8.8. The Landscape of Recombination

### 8.8.1. Genetic Length and Crossover Counts

Recombination frequencies are a property of meiosis, so maps of the same chromosome differ between sexes and species. The genetic length of a chromosome in morgans is the mean number of crossovers per chromatid; the obligate crossover sets a floor of about $50\,\mathrm{cM}$ for any chromosome arm pair. Human autosomes total about $35\,\mathrm{M}$ sex-averaged: pedigree studies count about 27 crossovers per paternally and about 42 per maternally transmitted genome, and cytological counts of MLH1 foci, which mark crossovers in pachytene, give about twice these numbers per meiosis (about 50 in spermatocytes, 70 in oocytes), as expected since a gamete receives half the crossovers of a bivalent. The female map is about $1.6$–$1.7$ times longer than the male map. With an autosomal sequence of about $2.9 \times 10^9$ bp, the average rate is about $1.2\,\mathrm{cM/Mb}$. Rates differ greatly between organisms: about $2\,\mathrm{cM/Mb}$ in *Drosophila* (a genome of about $280\,\mathrm{cM}$ for $140\,\mathrm{Mb}$ of euchromatin), about $350\,\mathrm{cM/Mb}$ in budding yeast (a few kilobases per centimorgan), and well below $1\,\mathrm{cM/Mb}$ in large plant genomes such as wheat. Since the number of crossovers per chromosome is nearly fixed by the obligate crossover and interference, small chromosomes have higher rates per megabase.

Recombination frequency between the same two loci is also not a constant within a species, which is one reason why distances measured in different experiments disagree (Example 8.4.2). It depends on the sex of the heterozygous parent (above; in mammals the female map is longer, in *Drosophila* and *Bombyx* one sex has none, 8.7.2), on age (in *Drosophila* females it changes with maternal age), on temperature (in *Drosophila* it rises at both low and high temperatures, Plough 1917), on the genotype at modifier loci (the PRDM9 alleles of 8.8.2) and on the chromosomes themselves: a heterozygous inversion or translocation suppresses recovered crossovers near it ([7.4.15](/7.4.15)), and a reciprocal translocation even makes loci on two different chromosomes behave as linked (pseudolinkage, [7.4.15](/7.4.15#sec-15.5.3)). Ionizing radiation and DNA-damaging agents such as mitomycin C raise the frequency of exchange, above all of mitotic exchange ([7.4.9](/7.4.9#sec-9.5)).

### 8.8.2. Hotspots

Within a chromosome, crossovers are concentrated in *recombination hotspots*, regions of $1$–$2\,\mathrm{kb}$ where recombination is ten to a thousand times more frequent than in the flanking sequence; in humans a majority of crossovers fall in hotspots that occupy only a small fraction of the genome. In humans and mice hotspots are specified by PRDM9, a zinc-finger histone methyltransferase whose array binds a degenerate motif (a 13-mer, CCNCCNTNNCCNC, for the most common human allele) and marks nucleosomes with H3K4me3 and H3K36me3, where SPO11 then cuts ([7.2.9](/7.2.9#sec-9.5.2)). The zinc-finger array evolves fast, so hotspots differ between human populations (carriers of different PRDM9 alleles), between humans and chimpanzees (almost no shared hotspots) and between mouse subspecies; hotspots also erode themselves, because the broken homologue is repaired from the unbroken one and the motif is lost by gene conversion. Mammals without functional PRDM9, such as dogs, and yeast and plants place breaks at promoters and other open chromatin instead. Recombination is suppressed near centromeres and in heterochromatin, and often in large inversions ([7.4.15](/7.4.15)).

### 8.8.3. Genetic and Physical Maps

**Definition 8.8.1 (Physical Map)** A **physical map** gives the positions of loci or landmarks on a chromosome in units of DNA length (base pairs), or by their order relative to cytological landmarks (bands, cloned fragments); the complete genome sequence is the ultimate physical map.

Genetic and physical maps agree in order, but not in scale, because crossovers are unevenly distributed. Plotting genetic position against physical position (a Marey map) gives a monotone curve whose slope is the local recombination rate in $\mathrm{cM/Mb}$: flat across centromeres and heterochromatin, steep in hotspot-rich arms (Figure). Maps were the only way to locate genes until the 1980s, and they remain the way to find a gene known only by its phenotype: linkage to a molecular marker of known physical position leads to a candidate region and then to the gene. The cystic fibrosis gene is the classic example. Between 1938 and 1985 nothing was known of its location; it was then found to be linked to the enzyme polymorphism PON and to DNA markers on chromosome 7, and narrowed by further markers until the gene, *CFTR*, was cloned in 1989 ([7.4.14](/7.4.14)).

![Genetic versus physical map of a simulated metacentric chromosome of 100 Mb. (A) The local recombination rate (cM/Mb) along the chromosome: suppressed around the centromere, higher toward the telomeres, with narrow hotspots. (B) Marey map: cumulative genetic position (cM) against physical position (Mb); its slope is the local rate, flat across the centromere and steep in the distal arms. The dashed line is the chromosome average. Illustrative parameters.](./plots/genetic-physical-map.py)

## Summary

- **Linkage** (Definition 8.1.2): parental types in excess, recombination frequency $r < 1/2$; phase (Definition 8.1.3) decides which classes are parental (Definition 8.1.1). Testcross offspring read the gametes directly (Example 8.1.1).
- Recombination is crossing over between non-sister chromatids at the four-strand stage (8.2); one crossover gives two of four recombinant chromatids, and with random chromatid involvement $r = \frac12(1 - \mathbb{P}(K = 0)) \le \frac12$ (Formula 8.3.1).
- Recombination frequency (Definition 8.3.1), centimorgan (Definition 8.3.2), genetic map (Definition 8.3.3) and linkage groups (Definition 8.3.4), as many as the haploid chromosome number. Meiocytes with a chiasma in a short interval $= 2r$ (Remark 8.3.1).
- Three-point testcross (Algorithm 8.4.1): largest pair parental, smallest pair double crossovers (Definition 8.4.2), the middle gene is the one switched in the double crossovers; $r_i = (\mathrm{SCO}_i + \mathrm{DCO})/n$; coincidence $C = \mathrm{DCO}/(r_1 r_2)$, interference $I = 1 - C$ (Definition 8.4.3; Example 8.4.1: map $6.0 + 12.5\,\mathrm{cM}$, $C = 0.4$). Check pairwise linkage first (Remark 8.4.1); distances from different experiments need not agree (Example 8.4.2).
- Mapping functions (Definition 8.5.1):

  | Model | $r(d)$ | $d(r)$ |
  |---|---|---|
  | Short intervals | $r \approx d$ | $d \approx r$ |
  | Haldane (Poisson, Formula 8.5.1) | $\frac12(1 - \mathrm{e}^{-2d})$ | $-\frac12\ln(1 - 2r)$ |
  | Kosambi (Formula 8.5.2) | $\frac12\tanh 2d$ | $\frac14\ln\frac{1+2r}{1-2r}$ |

  Interference is described by the gamma (chi-square) model, $\nu \approx 4$–$5$ in flies and humans (8.5.3).
- Estimation: testcross $\hat r = R/n$, $\operatorname{se} = \sqrt{\hat r(1 - \hat r)/n}$ (Formula 8.6.1); F2 square-root method, coupling $1 - 2\sqrt f$, repulsion $2\sqrt f$ (Formula 8.6.2); F2 MLE from the quadratic $n\varphi^2 - (n_1 - 2n_2 - 2n_3 - n_4)\varphi - 2n_4 = 0$ (Formula 8.6.3; Example 8.6.1, sweet pea $\hat r = 0.120$; repulsion Example 8.6.2, $0.110 \pm 0.048$). Information per offspring: codominant F2 > testcross ≳ dominant F2 coupling ≫ dominant F2 repulsion.
- Test linkage with the $2 \times 2$ independence $\chi^2$ (1 df), not the 1:1:1:1 fit (Algorithm 8.7.1); the LOD score is the $\log_{10}$ likelihood ratio for $r = \hat r$ versus $1/2$.
- No crossing over in *Drosophila* males and *Bombyx* females, the heterogametic sexes (Haldane–Huxley rule, 8.7.2).
- Recombination landscape: about $35\,\mathrm{M}$ human autosomes, female map about 1.6–1.7 times the male, about $1.2\,\mathrm{cM/Mb}$; hotspots placed by PRDM9 in mammals; suppression at centromeres; recombination also varies with age, temperature, modifier genes and rearrangements (8.8). Genetic and physical maps (Definition 8.8.1) share order, not scale.

## Questions

1. A testcross of an $Aa\,Bb$ individual gives 92 $AB$, 108 $ab$, 9 $Ab$ and 11 $aB$ offspring (classified by the gamete of the heterozygote). What was the phase of the heterozygote, and what are $\hat r$, its standard error and a 95 % confidence interval?

   **Answer** The frequent classes $AB$ and $ab$ are parental, so the heterozygote was in coupling, $AB/ab$. $\hat r = 20/220 = 0.0909$, $\operatorname{se} = \sqrt{0.0909 \times 0.9091/220} = 0.0194$, interval $0.0909 \pm 0.0380$, i.e. $0.053$–$0.129$ (about $9\,\mathrm{cM}$).

2. In a cross of $Ab/aB$ (repulsion) with $ab/ab$, 1000 offspring are expected. If the two loci are $16\,\mathrm{cM}$ apart and multiple crossovers can be ignored, how many offspring of each class do you expect?

   **Answer** Parental (repulsion) gametes $Ab$ and $aB$ each $(1 - 0.16)/2 = 0.42$, recombinant $AB$ and $ab$ each $0.08$: 420 $Ab$, 420 $aB$, 80 $AB$, 80 $ab$.

3. Why can a single crossover between two loci produce only half recombinant gametes, and why does this imply $r \le 1/2$ for any distance?

   **Answer** Crossing over occurs at the four-chromatid stage and involves two of the four chromatids, so a bivalent with one crossover in the interval yields two recombinant and two parental chromatids. With several crossovers and random choice of chromatids, a given chromatid is involved in each crossover with probability $1/2$ and is recombinant if involved an odd number of times; given $k \ge 1$ crossovers this happens with probability exactly $1/2$ (Formula 8.3.1). Hence $r = \frac12\,\mathbb{P}(\text{at least one crossover}) \le \frac12$.

4. Genes $a$, $b$, $c$ are linked. Two-point crosses give $r_{ab} = 0.08$, $r_{bc} = 0.15$ and $r_{ac} = 0.21$. What is the gene order, and why is $r_{ac}$ less than $0.08 + 0.15$?

   **Answer** The largest distance is $a$–$c$, so $b$ is in the middle: $a$–$b$–$c$. $r_{ac}$ is smaller than the sum $0.23$ because double crossovers in the $a$–$c$ interval restore the parental combination of $a$ and $c$ and are not counted as recombinant; with no interference the deficit would be about $2 r_{ab} r_{bc} = 0.024$, close to the observed $0.02$.

5. A three-point testcross of a triple heterozygote of maize gives (gamete of the heterozygote): $+\,+\,+$ 74, $+\,+\,c$ 382, $+\,b\,+$ 3, $+\,b\,c$ 98, $a\,+\,+$ 106, $a\,+\,c$ 5, $a\,b\,+$ 364, $a\,b\,c$ 66 (total 1098). Determine the parental haplotypes, the gene order, the map distances, the coefficient of coincidence and the interference.

   **Answer** Parental: $+\,+\,c$ (382) and $a\,b\,+$ (364). Double crossovers: $+\,b\,+$ (3) and $a\,+\,c$ (5). The DCO $a\,+\,c$ differs from the parental $+\,+\,c$ only at $a$, so $a$ is the middle gene and the order is $b$–$a$–$c$. In this order the parental haplotypes are $+\,+\,c$ and $b\,a\,+$. Single crossovers between $b$ and $a$ switch only $b$: $b\,+\,c$ (98) and $+\,a\,+$ (106), total 204. Single crossovers between $a$ and $c$ switch only $c$: $+\,+\,+$ (74) and $b\,a\,c$ (66), total 140. Then $r_{ba} = (204 + 8)/1098 = 0.193$ and $r_{ac} = (140 + 8)/1098 = 0.135$; the map is $b$ —$19.3\,\mathrm{cM}$— $a$ —$13.5\,\mathrm{cM}$— $c$ ($32.8\,\mathrm{cM}$ in all). Expected DCO $0.193 \times 0.135 \times 1098 = 28.6$; $C = 8/28.6 = 0.28$, $I = 0.72$.

6. In the cross of Question 5, how many double-crossover offspring would you expect if the interference were $0.3$ instead?

   **Answer** $C = 0.7$, so $0.7 \times 0.193 \times 0.135 \times 1098 = 20$ double crossovers.

7. Convert recombination frequencies of $0.10$ and $0.40$ into map distances with the Haldane and Kosambi functions. Which conversion changes the result more, and why?

   **Answer** $r = 0.10$: Haldane $-\frac12\ln 0.8 = 11.2\,\mathrm{cM}$, Kosambi $\frac14\ln(1.2/0.8) = 10.1\,\mathrm{cM}$. $r = 0.40$: Haldane $-\frac12\ln 0.2 = 80.5\,\mathrm{cM}$, Kosambi $\frac14\ln 9 = 54.9\,\mathrm{cM}$. The long interval changes more, because the correction for undetected multiple crossovers grows with distance and the two models assume different amounts of interference.

8. Under the Haldane model, what is the probability that a chromatid is recombinant between loci $30\,\mathrm{cM}$ apart, and what is the probability that the bivalent has no chiasma in this interval?

   **Answer** $\mathbb{P}(K = 0) = \mathrm{e}^{-2 \times 0.3} = \mathrm{e}^{-0.6} = 0.549$; $r = \frac12(1 - 0.549) = 0.226$.

9. Show that Kosambi's function satisfies $\mathrm{d}r/\mathrm{d}d = 1 - 4r^2$ and that $r \approx d - \frac43 d^3$ for small $d$. Compare with Haldane's expansion.

   **Answer** $r = \frac12\tanh 2d$, so $\mathrm{d}r/\mathrm{d}d = \operatorname{sech}^2 2d = 1 - \tanh^2 2d = 1 - 4r^2$. With $\tanh x = x - x^3/3 + \dots$, $r = \frac12(2d - 8d^3/3) = d - \frac43 d^3$. Haldane: $\frac12(1 - \mathrm{e}^{-2d}) = d - d^2 + \frac23 d^3 - \dots$, which departs from $r = d$ already at second order; Kosambi's correction is of third order, reflecting strong interference over short distances.

10. An F2 of a coupling double heterozygote (complete dominance) consists of 1050 $A\_B\_$, 148 $A\_bb$, 142 $aaB\_$ and 260 $aabb$ plants. Estimate $r$ by the square-root method and by maximum likelihood, and give the standard error of the MLE. Compare with the standard error of a testcross of the same size.

    **Answer** Square root: $1 - 2\sqrt{260/1600} = 0.194$. MLE: $1600\varphi^2 - (1050 - 580 - 260)\varphi - 520 = 0$, i.e. $1600\varphi^2 - 210\varphi - 520 = 0$, $\hat\varphi = 0.6395$, $\hat r = 1 - 0.7997 = 0.200$. Fisher information per plant at $\hat\varphi$: $\frac1{16}(4/2.6395 + 8/0.3605 + 4/0.6395) = 1.871$; $\operatorname{se}(\hat\varphi) = 1/\sqrt{1600 \times 1.871} = 0.01827$, $\operatorname{se}(\hat r) = 0.01827/(2 \times 0.7997) = 0.0114$. A testcross of 1600 at $r = 0.2$ has $\operatorname{se} = \sqrt{0.16/1600} = 0.0100$, slightly better.

11. An F2 of a repulsion double heterozygote ($Ab/aB$) gives 9 $aabb$ plants out of 1600. Estimate $r$. Why is this design poor for tight linkage?

    **Answer** $f = 9/1600$, $\hat r = 2\sqrt f = 2 \times 0.075 = 0.15$. In repulsion the only informative class has frequency $r^2/4$; for small $r$ it is very rare and its count has a large relative sampling error (here $9 \pm 3$), and the other classes hardly change with $r$. The Fisher information per plant is about $1.0$ at $r = 0.05$, against $21$ for a testcross.

12. A testcross gives the table $AB$ 30, $Ab$ 20, $aB$ 10, $ab$ 40 (100 offspring). Test for linkage with the appropriate $\chi^2$ test, and explain why a 1:1:1:1 goodness-of-fit test would be misleading here.

    **Answer** Margins: $A$ 50, $a$ 50; $B$ 40, $b$ 60. Expected: $AB$ 20, $Ab$ 30, $aB$ 20, $ab$ 30. $\chi^2 = 100/20 + 100/30 + 100/20 + 100/30 = 16.7$, 1 df, $p = 4 \times 10^{-5}$: linked, $\hat r = 30/100 = 0.30$. The goodness of fit to 25 each gives $\chi^2 = (25 + 25 + 225 + 225)/25 = 20$ with 3 df; part of this deviation comes from the 40:60 segregation at locus $B$ (perhaps reduced viability of $B$), which is not evidence of linkage.

13. Compute the LOD score for linkage at $\hat r$ in Question 1. Would the data pass the conventional threshold of 3?

    **Answer** $Z = 20\log_{10}0.0909 + 200\log_{10}0.9091 - 220\log_{10}0.5 = -20.83 - 8.28 + 66.23 = 37.1$, far above 3.

14. A *Drosophila* male heterozygous $b\,vg^{+}/b^{+}\,vg$ is crossed to a $b\,vg/b\,vg$ female. What offspring do you expect, and what would the reciprocal cross with a heterozygous female (genes $18\,\mathrm{cM}$ apart) give?

    **Answer** Males do not cross over: only parental gametes, half black ($b\,vg^{+}$) and half vestigial ($b^{+}\,vg$), no wild type or black vestigial. A heterozygous female gives 41 % black, 41 % vestigial, 9 % wild type and 9 % black vestigial.

15. (Design) You can afford to score 500 offspring to estimate the distance between two genes expected to be about $5\,\mathrm{cM}$ apart in a self-fertile plant with dominant markers. Compare a testcross, a coupling F2 and a repulsion F2.

    **Answer** Using the information per individual (Figure in 8.6.3) at $r = 0.05$: testcross $I = 21.1$, coupling F2 $19.8$, repulsion F2 $1.0$. Standard errors $1/\sqrt{500 I}$: $0.0097$, $0.0100$ and $0.045$. A testcross or a coupling F2 gives $\hat r = 0.05 \pm 0.01$; a repulsion F2 cannot distinguish $5\,\mathrm{cM}$ from $0$ or $14\,\mathrm{cM}$. Choose the coupling F2 if testcrossing is laborious, and never the repulsion F2.

16. (Recombination landscape) A human chromosome of $130\,\mathrm{Mb}$ has a sex-averaged genetic length of $150\,\mathrm{cM}$, and the female map is 1.65 times the male map. What are the male and female lengths, the average rate in cM/Mb, and the mean number of chiasmata per bivalent in female meiosis?

    **Answer** With $(m + f)/2 = 150$ and $f = 1.65m$: $m = 300/2.65 = 113\,\mathrm{cM}$, $f = 187\,\mathrm{cM}$. Average $150/130 = 1.15\,\mathrm{cM/Mb}$. Female genetic length $1.87\,\mathrm{M}$ = mean crossovers per chromatid; chiasmata per bivalent $= 2 \times 1.87 = 3.7$.

17. In *Drosophila*, loci $C$ and $D$ are $20\,\mathrm{cM}$ apart. Flies $CD/cd$ of both sexes are intercrossed. What fraction of the offspring is $Cc\,Dd$, what fraction $cc\,dd$, and what are the four phenotype classes? How would the answer change if crossing over occurred at the same rate in males?

    **Answer** Females give $CD$ and $cd$ $0.4$ each, $Cd$ and $cD$ $0.1$ each; males do not cross over and give $CD$ and $cd$ $0.5$ each. $Cc\,Dd$ arises from $CD \times cd$ or $cd \times CD$: $0.4 \times 0.5 + 0.4 \times 0.5 = 0.40$; the female's recombinant gametes combined with a parental sperm give only single heterozygotes ($CC\,Dd$, $Cc\,dd$, $Cc\,DD$, $cc\,Dd$, $0.05$ each). $cc\,dd = 0.4 \times 0.5 = 0.20$. Phenotypes: $C\_D\_$ $0.70$, $C\_dd$ $0.05$, $ccD\_$ $0.05$, $ccdd$ $0.20$. With crossing over in both sexes ($0.4, 0.4, 0.1, 0.1$ from each), $Cc\,Dd$ would be $2(0.4^2 + 0.1^2) = 0.34$ (coupling and repulsion double heterozygotes together) and $cc\,dd$ $0.16$, the coupling F2 of Formula 8.6.2.

18. A plant $Aa\,Bb$ forms the gametes $Ab : aB : AB : ab = 4 : 4 : 1 : 1$. What is its phase and the recombination frequency? If it is selfed, what fraction of the offspring is homozygous at both loci, and what are the four phenotype frequencies (complete dominance)?

    **Answer** The frequent gametes $Ab$ and $aB$ are parental: repulsion, $Ab/aB$, $r = 0.2$. A selfed offspring is homozygous at both loci when it receives the same haplotype twice: $0.4^2 + 0.4^2 + 0.1^2 + 0.1^2 = 0.34$. With $\varphi = r^2 = 0.04$: $A\_B\_ = (2 + 0.04)/4 = 0.51$, $A\_bb = aaB\_ = 0.96/4 = 0.24$, $aabb = 0.01$.

19. (Self-fertilization) (a) The F2 of a coupling double heterozygote has $160$ $aabb$ plants among $1000$. Estimate $r$ and the expected numbers in the other classes. (b) The F2 of a repulsion double heterozygote has 25 $aabb$ among 10 000. Estimate $r$.

    **Answer** (a) $\sqrt{0.16} = 0.4$ is the frequency of the $ab$ gamete $= (1 - r)/2$, so $r = 0.2$. With $\varphi = 0.64$: $A\_B\_$ $660$, $A\_bb$ $90$, $aaB\_$ $90$, $aabb$ $160$. (b) $\sqrt{0.0025} = 0.05 = r/2$, so $r = 0.10$.

20. Loci $A$ and $C$ are $20\,\mathrm{cM}$ apart on the map, built from short intervals through a middle locus $B$. A testcross of $AC/ac$ shows only $18\,\%$ $A$–$C$ recombinants. What frequency of double crossovers (in the intervals $A$–$B$ and $B$–$C$) does this imply? If $r_{AB} = 0.12$ and $r_{BC} = 0.08$, what are $C$ and $I$?

    **Answer** The outer-gene recombination frequency is smaller than the sum of the intervals by twice the double-crossover frequency (Algorithm 8.4.1, step 6): $0.20 - 0.18 = 2\,\mathrm{DCO}$, so $\mathrm{DCO} = 0.01$. Expected under independence $0.12 \times 0.08 = 0.0096$, so $C = 0.01/0.0096 = 1.04$ and $I = -0.04$, no interference within sampling error.

21. A maize testcross $C\,Sh/c\,sh \times c\,sh/c\,sh$ gives 4032 coloured full, 149 coloured shrunken, 152 colourless full and 4035 colourless shrunken kernels. Compute $\hat r$ and its standard error. In what percentage of the meiocytes of the heterozygote was there a chiasma between the two loci?

    **Answer** $\hat r = (149 + 152)/8368 = 0.036$, $\operatorname{se} = \sqrt{0.036 \times 0.964/8368} = 0.0020$. For so short an interval double crossovers are negligible, so by Remark 8.3.1 a chiasma occurred in $2 \times 3.6 = 7.2\,\%$ of meiocytes.

22. A testcross of $Aa\,Bb\,Cc$ gives (gametes of the heterozygote) $ABC$ 210, $ABc$ 205, $abC$ 198, $abc$ 202, $AbC$ 44, $Abc$ 46, $aBC$ 47, $aBc$ 48. Analyse the data.

    **Answer** Collapse to pairs (Remark 8.4.1). $A$–$B$: recombinants $Ab$ and $aB$ $= 44 + 46 + 47 + 48 = 185$ of 1000, $\hat r = 0.185$, linked (parental $AB/ab$). $A$–$C$: parental-like ($AC$ or $ac$) $210 + 44 + 202 + 48 = 504$, non-matching $496$, $\hat r \approx 0.50$; $B$–$C$: likewise $0.50$. $C$ assorts independently of the $A$–$B$ chromosome: the classes come in pairs ($ABC$/$ABc$, $abC$/$abc$, …) of equal size that differ only at $C$. The genotype is $AB/ab\; C/c$ with $A$–$B$ $18.5\,\mathrm{cM}$; there are no double crossovers to find, and the two smallest classes are just recombinant $A$–$B$ haplotypes.

23. A female heterozygous at four loci forms 16 kinds of gametes: $ABCd$, $ABcD$, $abCd$, $abcD$ $15.75\,\%$ each; $ABCD$, $ABcd$, $abCD$, $abcd$ $6.75\,\%$ each; $AbCd$, $AbcD$, $aBCd$, $aBcD$ $1.75\,\%$ each; $AbCD$, $Abcd$, $aBCD$, $aBcd$ $0.75\,\%$ each. Which loci are linked, in which phase, and how far apart?

    **Answer** Sum the gametes over the other two loci for each pair. $A$–$B$: $AB + ab = 4(15.75 + 6.75)\,\% = 90\,\%$, so $AB/ab$ with $r = 0.10$. $C$–$D$: $Cd + cD = 4(15.75 + 1.75)\,\% = 70\,\%$, so repulsion $Cd/cD$ with $r = 0.30$. Every other pair ($A$–$C$, $A$–$D$, $B$–$C$, $B$–$D$) gives $50\,\%$: the two linked pairs are on different chromosomes. Check: each gamete frequency is the product of the two pair frequencies, for example $ABCd = 0.45 \times 0.35 = 0.1575$ and $AbCD = 0.05 \times 0.15 = 0.0075$. The genotype is $AB/ab\; Cd/cD$.

