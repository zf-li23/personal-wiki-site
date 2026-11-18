---
title: Species, Genetic Variation and Molecular Population Ecology
description: "How ecologists measure and use genetic information: species concepts, DNA barcoding and the barcode gap, nomenclature and the PhyloCode; a review of the population processes of evolution and the hybrid origin of the Guizhou snub-nosed monkey; measures of genetic diversity (allelic diversity, polymorphic loci, observed and expected heterozygosity, nucleotide diversity, inbreeding coefficient); effective population size, its ecological determinants and its estimation by the linkage-disequilibrium and temporal methods, the 50/500 rule; differentiation and gene flow (F-statistics, F_ST and Nm); phylogeography, glacial refugia and recolonization; environmental DNA and metabarcoding."
---

Population ecology counts individuals; population genetics follows the genes they carry. The two meet wherever the size, structure and history of a population leave a genetic signature, and modern ecology uses that signature routinely: to decide what a species is, to identify specimens and diets from DNA, to estimate the effective size of a population and the rate at which it loses variation, to measure dispersal between populations that cannot be followed directly, and to reconstruct the history of ranges over glacial cycles. This chapter is about these uses. The theory behind them is developed elsewhere and is only summarized: the Hardy–Weinberg law, selection, drift and gene flow in [7.4.22](/7.4.22) and [7.4.23](/7.4.23), drift and the neutral theory in [7.10.6](/7.10.6), the coalescent in [7.10.7](/7.10.7), evolution in space in [7.10.10](/7.10.10), species and speciation in [7.10.11](/7.10.11) and [7.10.12](/7.10.12), and biogeography and phylogeography in [7.10.30](/7.10.30). The molecular adaptations of individuals to their environment were the subject of [7.19.7](/7.19.7); the genetic consequences of small population size for extinction risk link this chapter to [7.19.15](/7.19.15), and landscape genetics follows in [7.19.49](/7.19.49).

## 20.1. Species

### 20.1.1. Species Concepts

Ecologists count species, compare their niches and protect them, so they need a working definition of a species; there are many. The oldest is the **morphological species concept**: a species is a group of individuals that are very similar in morphology and physiology, differ from other such groups by consistent characters, and have a definite natural range, as the Amur hedgehog (*Erinaceus amurensis*) and the Siberian weasel (*Mustela sibirica*) are recognized by naturalists. Its weakness is that morphology can vary greatly within a species (the Cat Fanciers' Association recognizes 45 pedigreed breeds of the domestic cat *Felis catus*, all one species) and very little between species (**cryptic species**, [Definition 11.1.2](/7.10.11#def-11.1.2) of 7.10.11).

The **biological species concept** ([Definition 11.1.1](/7.10.11#def-11.1.1) of 7.10.11; Mayr 1942) defines species as groups of interbreeding natural populations that are reproductively isolated from other such groups: a species is a reproductive community and a gene pool. It explains why species are discrete in a given place, but it is hard or impossible to apply in four situations:

- allopatric populations, which never meet, so that it is unknown whether they would interbreed;
- species that do not interbreed in nature but do in captivity or cultivation (many ducks, big cats, orchids);
- organisms that reproduce asexually, including many bacteria, protists, fungi, plants and animals;
- fossils and other extinct organisms.

The **phylogenetic species concept** ([Definition 11.1.3](/7.10.11#def-11.1.3) of 7.10.11) instead defines a species as the smallest diagnosable cluster of individuals with a common ancestry, a lineage that is distinct from others in space and time. It applies to asexual organisms and fossils, but tends to divide traditional species into many more units. More than twenty species concepts have been proposed (Mayden 1997 listed 22), and most can be seen as different criteria for recognizing the same thing, a separately evolving metapopulation lineage (de Queiroz 2007): reproductive isolation, diagnosable differences, monophyly and ecological distinctness accumulate at different times as lineages diverge, which is why different criteria disagree for young species. **Ring species** ([Definition 11.1.4](/7.10.11#def-11.1.4) of 7.10.11) show this continuum in space. Whatever concept is used, the species is the basic unit of community ecology and conservation, and the choice of concept changes species counts, the ranges of species, and which populations are listed as threatened.

### 20.1.2. DNA Barcoding

**DNA barcoding** ([7.12.2](/7.12.2), [7.17.1](/7.17.1)) identifies specimens by a short, standardized DNA sequence that varies little within species and more between them. For most animals it is a 648-base-pair fragment of the mitochondrial gene for cytochrome *c* oxidase subunit I (COI); for land plants the chloroplast genes *rbcL* and *matK*, for fungi the nuclear ribosomal internal transcribed spacer (ITS), and for many purposes the 18S and 28S ribosomal RNA genes. Identification works if the largest distance within species is smaller than the smallest distance between species, a **barcode gap**; for COI in many animal groups a threshold of about 2 % sequence divergence is used as a first approximation, sequences that differ by less being provisionally assigned to the same species (Figure 1A).

Barcodes have changed the pace of taxonomy. In a revision of braconid parasitoid wasps of 11 subfamilies from the Área de Conservación Guanacaste in Costa Rica, Sharkey et al. (2021) described 416 species, 403 of them new, in a single paper. Most species were diagnosed by their COI barcode together with a photograph of the holotype, without the traditional morphological description, an approach the authors called "minimalist revision and description". Its supporters argue that it is the only way to describe the many millions of undescribed insect species before they disappear; critics, that species delimited by one mitochondrial gene with a fixed threshold can be wrong, because the barcode gap is absent in recently diverged species and in groups with incomplete lineage sorting or introgression (Figure 1B; [7.10.25](/7.10.25)), and that descriptions without morphology are hard to use for anyone without a sequencer. The best practice combines barcodes with morphology, ecology and nuclear markers (integrative taxonomy).

![The barcode gap, in simulated COI distances for 12 species with 10 individuals each, with within-species coalescence times drawn from an exponential distribution with mean 0.15 Myr and divergence accumulating at 2 % per Myr between lineages. A: species that split 2–12 Myr ago: within-species distances (blue) and between-species distances (red) are separated by a gap, and the 2 % threshold (dashed) assigns specimens correctly. B: a young radiation with splits 0.1–3 Myr ago: the distributions overlap and no single threshold separates species](./plots/barcode-gap.py)

### 20.1.3. Names

Species are named by **binomial nomenclature**, established by Linnaeus: the scientific name consists of the genus name and the specific epithet, as in *Panthera pardus*, the leopard. Rules of writing that apply in all fields of biology:

- scientific names of genera and species are italicized, names of higher taxa (Felidae, Carnivora) are not; the genus is capitalized, the specific epithet is in lowercase even if derived from a proper name;
- subspecies of animals have trinomial names, such as *Panthera pardus japonensis*, the North China leopard; varieties of plants are indicated by "var." in roman type, as in *Lilium brownii* var. *viridulum*, a variety of *L. brownii*;
- when needed, the name is followed by the author and the year of description, in roman type: *Panthera pardus* (Linnaeus, 1758) in zoological usage (the parentheses indicate that the species was originally described in another genus, here *Felis*);
- the genus may be abbreviated after its first use (*P. pardus*).

The codes of nomenclature (the International Code of Zoological Nomenclature, the International Code of Nomenclature for algae, fungi and plants, and the prokaryotic code) regulate names of ranked taxa from species to family and fix each name to a type specimen. The rules can change: in 2024 the Nomenclature Section of the International Botanical Congress in Madrid voted to replace the plant epithets derived from a racial slur (*caffra* and related forms) with *affra*. The *PhyloCode* (in force since 2020) is an alternative code for clades. It is rankless, applies only to monophyletic groups, and defines each name by a phylogenetic definition anchored on specimens, species or apomorphies: node-based (the clade originating from the most recent common ancestor of two specified taxa), branch-based (the clade of all organisms sharing a more recent ancestor with one taxon than with another) or apomorphy-based. For example, the clade of the most recent common ancestor of *Archaeopteryx* and living birds and all its descendants, often called Aves in older usage, is named Avialae in the PhyloCode's companion volume, which restricts Aves to the crown group of living birds. Like the higher ranks of the traditional codes, clades are real, but the decision where along a branch to draw the line between two species is not fixed by any code.

## 20.2. Evolutionary Processes in Populations

### 20.2.1. A Review

The modern synthesis ([7.10.1](/7.10.1)) unified Darwin's theory of natural selection, which he and Wallace proposed independently, with Mendelian genetics: populations are the units of evolution, evolution is the change of allele and genotype frequencies in the **gene pool** of a population, natural selection gives it direction, and reproductive isolation, often following geographic isolation, turns diverging populations into species. The main results used in ecology are these.

| Concept | Statement | Where |
|---|---|---|
| **Hardy–Weinberg equilibrium** | in an ideal population (very large, random mating, no migration, mutation or selection) allele and genotype frequencies stay constant, $p^2 : 2pq : q^2$ | [Definition 22.2.1](/7.4.22#def-22.2.1) of 7.4.22 |
| mutation | the ultimate source of variation; slow change of frequencies | [7.10.4](/7.10.4) |
| **gene flow** | movement of alleles between populations by dispersal of individuals or gametes | [Definition 23.2.1](/7.4.23#def-23.2.1) of 7.4.23 |
| nonrandom mating | **assortative mating**, inbreeding: change genotype frequencies, not allele frequencies | [7.4.22](/7.4.22) |
| **genetic drift** | random change of allele frequencies by sampling in finite populations; **population bottleneck**, **founder effect** | [Definition 23.5.1](/7.4.23#def-23.5.1), [23.5.3](/7.4.23#def-23.5.3) of 7.4.23 |
| selection | differential survival and reproduction of genotypes | [Definition 23.3.1](/7.4.23#def-23.3.1) of 7.4.23 |

The fitness of a genotype is its average number of offspring in the next generation, the product of its mean survival $l$ and its mean fecundity $m$: $W = ml$. **Relative fitness** $w$ divides by the fitness of the best genotype, and the **selection coefficient** is $s = 1 - w$. If genotype *Rr* leaves 500 offspring on average and *rr* 50, then $w_{rr} = 0.1$ and $s = 0.9$. Against a recessive genotype, the frequency $q$ of the recessive allele changes by $\Delta q = -spq^2/(1 - sq^2)$ per generation ([Formula 23.3.1](/7.4.23) of 7.4.23); because rare recessive alleles are hidden in heterozygotes, selection against them becomes very slow as $q$ falls. In the peppered moth (*Biston betularia*) the dark *carbonaria* form rose from rarity to about 98 % of the population near Manchester by the end of the nineteenth century, as soot darkened tree trunks and birds took more pale moths, and declined again after clean-air legislation ([7.10.3](/7.10.3)). Selection on quantitative traits is classified as **stabilizing selection**, **directional selection** or **disruptive selection** ([Definition 23.3.2](/7.4.23#def-23.3.2) of 7.4.23); stabilizing and directional selection usually reduce genetic variation, disruptive and balancing selection (heterozygote advantage, negative frequency dependence) maintain it. Sexual selection and kin selection are treated in [7.10.13](/7.10.13), [7.10.16](/7.10.16) and [7.19.21](/7.19.21).

### 20.2.2. Speciation and a Hybrid Species

In the classical geographic model of speciation, a geographic barrier divides a population and interrupts gene flow; the isolated populations adapt to their own environments and drift independently; reproductive isolating mechanisms evolve as a by-product, so that the populations remain distinct when they meet again. Speciation is classified by the geography of the populations as **allopatric speciation**, **parapatric speciation** or **sympatric speciation** ([7.10.12](/7.10.12)). New species can also arise from hybridization (**hybrid speciation**). Genomes of the five species of snub-nosed monkeys (*Rhinopithecus*) showed that the Guizhou snub-nosed monkey (*R. brelichi*), endemic to Mount Fanjing in Guizhou and one of the rarest primates in China, originated by hybridization between the ancestor of the golden snub-nosed monkey (*R. roxellana*) and the ancestor of the black-and-white and Myanmar snub-nosed monkeys (*R. bieti* and *R. strykeri*), about 1.9 million years ago (Wu et al. 2023). Its mosaic coat, with golden-yellow and dark parts, is explained by alleles from the two parental lineages: higher expression of *PAH* leads to more eumelanin and darker hair, and reduced expression of *SLC45A2* shifts pigment synthesis from eumelanin to yellow pheomelanin. Such mosaic coloration may have contributed to reproductive isolation from both parental lineages.

## 20.3. Measuring Genetic Diversity

The genetic diversity of a population is measured from a sample of genotypes at a set of marker loci (allozymes historically, now microsatellites, single-nucleotide polymorphisms and sequences).

**Definition 20.3.1 (Measures of Genetic Diversity)** For a sample from one population:

1. *Allelic diversity* $A$ is the mean number of alleles per locus. Because it increases with sample size, *allelic richness*, the number expected in a standardized sample (by rarefaction), is used for comparisons.
2. The **proportion of polymorphic loci** $P$ is the fraction of loci at which the most common allele has a frequency below 0.95 (or 0.99): if 6 of 10 loci are polymorphic, $P = 0.6$.
3. The *observed heterozygosity* $H_{\mathrm{o}}$ of a locus is the fraction of individuals that are heterozygous; it is averaged over loci.
4. The **expected heterozygosity** or gene diversity of a locus with allele frequencies $x_1, \dots, x_m$ is

$$
H_{\mathrm{e}} = 1 - \sum_{i=1}^m x_i^2,
$$
the probability that two alleles drawn at random differ (the heterozygosity of [Definition 22.2.2](/7.4.22#def-22.2.2) of 7.4.22); in a sample of $n$ diploids it is multiplied by $2n/(2n - 1)$ to remove the bias. In a population in Hardy–Weinberg equilibrium it equals the expected frequency of heterozygotes.
5. The **nucleotide diversity** ([Definition 4.6.1](/7.10.4#def-4.6.1) of 7.10.4) of a set of DNA sequences is the average proportion of sites that differ between two sequences drawn at random, $\pi = \sum_{i,j}x_ix_j\pi_{ij}$, where $x_i$ is the frequency of sequence type $i$ and $\pi_{ij}$ the proportion of differing sites between types $i$ and $j$.

Inbreeding (mating between relatives) does not change allele frequencies, so it leaves $H_{\mathrm{e}}$ unchanged at first, but it increases homozygosity at all loci and so reduces $H_{\mathrm{o}}$. The **inbreeding coefficient** ([7.4.7](/7.4.7)) of a population, measured from the deficit of heterozygotes,

$$
F = \frac{H_{\mathrm{e}} - H_{\mathrm{o}}}{H_{\mathrm{e}}} = 1 - \frac{H_{\mathrm{o}}}{H_{\mathrm{e}}},
\tag{20.1}
$$
is 0 under random mating and 1 if all individuals are homozygous (complete inbreeding). Negative values indicate an excess of heterozygotes, for example after a recent bottleneck or under heterozygote advantage. A heterozygote deficit can also be caused by population substructure within the sample (the **Wahlund effect**, [7.4.22](/7.4.22)) and by null alleles at microsatellite loci, so $F$ must be interpreted with care.

**Example 20.3.1** At a microsatellite locus, 40 individuals of a population have the genotypes $A_1A_1$: 10, $A_1A_2$: 12, $A_2A_2$: 8, $A_1A_3$: 6, $A_3A_3$: 4. The allele counts are $A_1$: $20 + 12 + 6 = 38$, $A_2$: $12 + 16 = 28$, $A_3$: $6 + 8 = 14$, of 80, so $x = (0.475, 0.35, 0.175)$. Then $H_{\mathrm{e}} = 1 - (0.226 + 0.123 + 0.031) = 0.621$ (unbiased: $0.621 \times 80/79 = 0.629$), $H_{\mathrm{o}} = 18/40 = 0.45$, and $F = 1 - 0.45/0.629 = 0.28$: a marked deficit of heterozygotes, which would suggest inbreeding, substructure or null alleles.

:::

Genetic diversity is lost by drift at a rate set by the effective population size (Section 20.4), and dramatically in bottlenecks: the northern elephant seal (*Mirounga angustirostris*), reduced by hunting to perhaps a few dozen individuals in the 1890s and now numbering more than 200,000, has almost no allozyme variation, and the cheetah (*Acinonyx jubatus*) shows the signature of ancient bottlenecks. Selection reduces or maintains diversity as described in Section 20.2. Sexually reproducing populations usually have more diversity than asexual ones, and outcrossing plants more than selfers. Mitochondrial and chloroplast genomes, which are haploid and usually inherited from one parent, have an effective size one quarter that of nuclear genes in a diploid population with equal sex ratio, so they lose variation four times faster and track recent population history most sensitively.

## 20.4. Effective Population Size

### 20.4.1. Definition and Ecological Determinants

The census size of a population, the number of individuals counted, determines its demographic fate; the **effective population size** $N_{\mathrm{e}}$ ([Definition 23.5.2](/7.4.23#def-23.5.2) of 7.4.23), the size of an ideal Wright–Fisher population that would lose heterozygosity at the same rate, determines its genetic fate. Heterozygosity is lost at the rate $1/(2N_{\mathrm{e}})$ per generation,

$$
H_t = H_0\left(1 - \frac{1}{2N_{\mathrm{e}}}\right)^t \approx H_0\,\mathrm{e}^{-t/(2N_{\mathrm{e}})},
\tag{20.2}
$$
and the inbreeding coefficient of a closed population rises correspondingly, $F_t = 1 - (1 - 1/(2N_{\mathrm{e}}))^t$ (Figure 2A). A new neutral mutation has initial frequency $1/(2N)$ in a population of $N$ diploids and is fixed with that probability; its fixation probability depends on the census size, whereas the time it takes and the rate at which variation is lost depend on $N_{\mathrm{e}}$. If a population of 10,000 individuals contains only 1000 successful breeders with random family sizes, its drift is that of a population of about 1000.

Three ecological features make $N_{\mathrm{e}}$ smaller than the census size $N$; their formulas are given in [Formula 23.5.1](/7.4.23) of 7.4.23.

- Unequal numbers of breeding males $N_m$ and females $N_f$: $N_{\mathrm{e}} = 4N_mN_f/(N_m + N_f)$, which is at most $N_m + N_f$, at an equal sex ratio (Figure 2B). Polygynous mating systems, in which a few males sire most offspring (elephant seals, red deer, lekking birds), have a low $N_{\mathrm{e}}/N$ ([7.19.21](/7.19.21)).
- Variance in reproductive success: $N_{\mathrm{e}} = (4N - 2)/(V_k + 2)$, where $V_k$ is the variance of the number of gametes contributed per individual. In clonal organisms in which a single clone dominates a population, $N_{\mathrm{e}}$ can approach 1, whatever the number of ramets. Many marine fishes and invertebrates with enormous fecundity and high, random early mortality have a "sweepstakes" reproduction in which a small fraction of parents produces most recruits in a given year, so $N_{\mathrm{e}}$ can be orders of magnitude below census sizes of millions (Hedgecock and Pudovkin 2011).
- Fluctuations in size over generations: the long-term $N_{\mathrm{e}}$ is the harmonic mean of the effective sizes in the individual generations, $1/N_{\mathrm{e}} = \frac1t\sum_{i=1}^t 1/N_{\mathrm{e},i}$ (Wright 1938), which is dominated by the smallest values. A single crash leaves a lasting genetic mark even after the population has recovered its former abundance: this is the genetic meaning of a bottleneck (Figure 2C).

In a survey of wild populations, fluctuations in population size reduced $N_{\mathrm{e}}$ on average by 65 %, unequal sex ratios by 36 % and variance in family size by about 46 %, and the ratio of effective to census size averaged about 0.1 (Frankham 1995); later compilations of genetic estimates give a median of about 0.14 (Palstra and Ruzzante 2008). Conservation programs that count individuals therefore overestimate genetic viability tenfold on average.

![Effective population size. A: expected heterozygosity in Wright–Fisher populations of effective size 10, 50 and 250 (points: mean of 2000 simulated loci; lines: Eq. (20.2)). B: the ratio of effective to census size with unequal numbers of breeding males and females, N_e = 4N_mN_f/(N_m + N_f): with one male to nine females, N_e is only 36 % of the number of breeders. C: a population of 1000–1500 individuals that crashes to 20 in one generation: over ten generations its arithmetic mean size is 1182, but its effective size, the harmonic mean, is only 175](./plots/effective-size.py)

### 20.4.2. Estimating Effective Size

Effective size can be estimated demographically, from the sex ratio, the variance in family size and the fluctuations of the population using the formulas above, but these data are rarely complete. Genetic methods estimate it from the consequences of drift.

- *Single-sample methods* use one sample of individuals from one generation. The most widely used is the *linkage-disequilibrium method* (Hill 1981; Waples 2006): in a small population few parents contribute genes to the next generation, and drift creates random associations between alleles at unlinked loci. The expected squared correlation of alleles at two unlinked loci is approximately $\mathbb{E}[r^2] \approx 1/(3N_{\mathrm{e}}) + 1/S$, where $S$ is the sample size, so $N_{\mathrm{e}}$ can be estimated from the excess of $r^2$ over its sampling expectation. Other single-sample methods use the excess of heterozygotes among the offspring of few parents, or reconstruct sibships from genotypes (Wang 2009).
- *Two-sample (temporal) methods* compare samples taken at least a generation apart. In a population of small $N_{\mathrm{e}}$, allele frequencies change faster. The standardized variance of the change in frequency (Nei and Tajima 1981) is

$$
F_c = \frac{1}{K}\sum_{i=1}^{K}\frac{(x_i - y_i)^2}{(x_i + y_i)/2 - x_iy_i},
$$
where $K$ is the number of alleles (summed over loci and averaged) and $x_i$, $y_i$ are the frequencies of allele $i$ at times 0 and $t$ generations. Part of $F_c$ is due to sampling, and the estimate corrected for sample sizes $S_0$ and $S_t$ (in individuals) is (Waples 1989)

$$
\hat N_{\mathrm{e}} = \frac{t}{2\left[F_c - \dfrac{1}{2S_0} - \dfrac{1}{2S_t}\right]},
\tag{20.3}
$$
with an additional term $+1/N$ in the bracket when individuals are sampled before reproduction and not returned to the population.

The temporal method estimates the harmonic mean $N_{\mathrm{e}}$ over the interval. Its precision depends on the number of independent alleles, the sample sizes and the ratio $t/N_{\mathrm{e}}$: drift must be large relative to sampling noise, so the method works well for small populations and poorly for large ones, whose estimates may even be infinite when the corrected $F_c$ is negative (Figure 3B). Museum and archived samples allow temporal estimates over decades.

### 20.4.3. The 50/500 Rule

How large must a population be to remain genetically healthy? Franklin (1980) and Soulé (1980) proposed the *50/500 rule*: an effective size of at least 50 to avoid serious inbreeding depression in the short term, and at least 500 to maintain evolutionary potential in the long term. The first number follows from animal breeders' experience that inbreeding increasing by no more than about 1 % per generation, $1/(2N_{\mathrm{e}}) \le 0.01$, can be tolerated. The second comes from the balance between drift, which removes additive genetic variance $V_A$ of a quantitative trait at the rate $1/(2N_{\mathrm{e}})$, and mutation, which adds new variance $V_M \approx 10^{-3}V_E$ per generation; at equilibrium $V_A = 2N_{\mathrm{e}}V_M$, so $N_{\mathrm{e}} = 500$ maintains $V_A \approx V_E$, a heritability of about 0.5.

The rule is now considered too low. Inbreeding depression has been observed in populations with $N_{\mathrm{e}}$ well above 50, the mutational variance that is relevant to fitness is smaller because many new mutations are deleterious, and Lande (1995) argued that about 5000 is needed to maintain potentially adaptive variation. Frankham et al. (2014) proposed revising the rule to 100/1000. With $N_{\mathrm{e}}/N \approx 0.1$, these correspond to census sizes of about 1000 and 10,000, of the same order as the minimum viable populations estimated demographically ([Definition 15.4.2](/7.19.15#def-15.4.2) of 7.19.15). Where small populations cannot be enlarged, **genetic rescue**, the introduction of individuals from other populations to restore variation ([7.19.52](/7.19.52)), can reverse inbreeding depression: the Florida panther recovered from about 20–30 individuals after eight pumas from Texas were released in 1995.

## 20.5. Differentiation and Gene Flow

### 20.5.1. F-Statistics

**Definition 20.5.1 (Genetic Differentiation and F-Statistics)** *Genetic differentiation* is the divergence of allele frequencies among the subpopulations of a species. Wright's F-statistics partition the deficit of heterozygotes in a subdivided population into components: with $H_{\mathrm{I}}$ the mean observed heterozygosity of individuals, $H_{\mathrm{S}}$ the mean expected heterozygosity within subpopulations and $H_{\mathrm{T}}$ the expected heterozygosity of the total population (all subpopulations pooled, under Hardy–Weinberg proportions),

$$
F_{\mathrm{IS}} = \frac{H_{\mathrm{S}} - H_{\mathrm{I}}}{H_{\mathrm{S}}}, \qquad
F_{\mathrm{ST}} = \frac{H_{\mathrm{T}} - H_{\mathrm{S}}}{H_{\mathrm{T}}}, \qquad
F_{\mathrm{IT}} = \frac{H_{\mathrm{T}} - H_{\mathrm{I}}}{H_{\mathrm{T}}},
$$
and $1 - F_{\mathrm{IT}} = (1 - F_{\mathrm{IS}})(1 - F_{\mathrm{ST}})$.

$F_{\mathrm{IS}}$ is the inbreeding coefficient (20.1) within subpopulations, and the **fixation index** $F_{\mathrm{ST}}$ ([7.4.22](/7.4.22), [7.10.10](/7.10.10)) the proportion of the total gene diversity due to differences between subpopulations. As a rough guide (Wright 1978), $F_{\mathrm{ST}}$ below 0.05 indicates little differentiation, 0.05–0.15 moderate, 0.15–0.25 great and above 0.25 very great differentiation. For highly polymorphic markers such as microsatellites, $H_{\mathrm{S}}$ is high and $F_{\mathrm{ST}}$ is bounded well below 1 even for completely isolated populations, so standardized measures (Hedrick's $G'_{\mathrm{ST}}$, Jost's $D$) are used alongside it. Differentiation is promoted by barriers to dispersal, **isolation by distance** ([Definition 10.3.1](/7.10.10#def-10.3.1) of 7.10.10), mating systems, divergent selection, mutation and drift, and reduced by gene flow.

**Example 20.5.1** Two equally sized populations have frequencies $p_1 = 0.8$ and $p_2 = 0.4$ of an allele. Then $H_{\mathrm{S}} = \frac12\bigl(2(0.8)(0.2) + 2(0.4)(0.6)\bigr) = 0.40$; the pooled frequency is $0.6$, so $H_{\mathrm{T}} = 2(0.6)(0.4) = 0.48$, and $F_{\mathrm{ST}} = (0.48 - 0.40)/0.48 = 0.17$: great differentiation.

:::

### 20.5.2. Gene Flow from F_ST

In Wright's island model, with many subpopulations of effective size $N_{\mathrm{e}}$, each receiving a fraction $m$ of its genes from a common pool of migrants per generation, drift and migration reach an equilibrium at which

$$
F_{\mathrm{ST}} \approx \frac{1}{1 + 4N_{\mathrm{e}}m},
\tag{20.4}
$$
derived from coalescence times in [Theorem 7.6.1](/7.10.7#thm-7.6.1) of 7.10.7. $N_{\mathrm{e}}m$ is the number of migrants (effective breeders) per generation. Differentiation is governed by this number, not by the migration rate alone: a large population with a small migration rate and a small population with a large one can be equally connected. The relation is steep at low gene flow (Figure 3A): one migrant every four generations ($N_{\mathrm{e}}m = 0.25$) reduces $F_{\mathrm{ST}}$ from 1 to 0.5, and one migrant per generation ($N_{\mathrm{e}}m = 1$) to 0.2. Hence the conservation rule of thumb that about one migrant per generation, and preferably one to ten (Mills and Allendorf 1996), is enough to prevent strong divergence of populations by drift while allowing local adaptation; Wright (1931) had concluded that $N_{\mathrm{e}}m \approx 1$ is the boundary between populations that behave as one and populations that diverge independently.

Inverting Eq. (20.4), $N_{\mathrm{e}}m \approx (1/F_{\mathrm{ST}} - 1)/4$, has been used widely to estimate gene flow from genetic data. Such indirect estimates must be treated with caution (Whitlock and McCauley 1999): they assume an island model at equilibrium, equal subpopulation sizes, no selection and no mutation of consequence, and real populations rarely satisfy these assumptions; populations that separated recently may have low $F_{\mathrm{ST}}$ without any current gene flow. Assignment of individuals to their populations of origin with multilocus genotypes and parentage analysis give more direct estimates of recent dispersal ([7.10.10](/7.10.10)). Gene flow depends on dispersal (and, in plants, on pollen and seed vectors), on the mode of reproduction and on the connectivity of the habitat: fragmentation reduces it, and the analysis of genetic structure against landscape features, landscape genetics, is the subject of [7.19.49](/7.19.49).

![Differentiation and the estimation of effective size. A: F_ST in an island model of 10 subpopulations of 50 diploids against the number of migrants per generation Nm (points: simulation of 200 loci; line: Eq. (20.4)); dashed lines mark Nm = 0.25 (F_ST = 0.5) and Nm = 1 (F_ST = 0.2). B: the temporal method, Eq. (20.3): estimates of N_e from samples of 50 individuals at 40 biallelic loci taken five generations apart, in 400 simulated populations with true N_e = 50 (blue) and 200 (red; solid lines: true values; dashed lines: medians of the estimates). Estimates for the smaller population are precise; those for the larger are widely scattered, some infinite (omitted) or very large (last bin)](./plots/differentiation-and-temporal.py)

## 20.6. Phylogeography and Environmental DNA

### 20.6.1. Reconstructing Population History

**Phylogeography** ([Definition 30.5.1](/7.10.30#def-30.5.1) of 7.10.30; Avise 2000) studies the principles and processes governing the geographic distribution of genealogical lineages within species and among closely related species. It combines the genealogy of genes sampled across the range with their geographic positions to infer the history of populations: where they lived, when they split, how they expanded and where they exchanged migrants. Its main tools are:

- the **molecular clock** ([Definition 23.7.1](/7.4.23#def-23.7.1) of 7.4.23; [7.10.24](/7.10.24)): if sequences diverge at a roughly constant rate, divergence between lineages measures the time since they split; for vertebrate mitochondrial DNA a rate of the order of 2 % divergence per million years between lineages is often used as a first approximation, but rates must be calibrated for each group;
- gene trees estimated by distance, parsimony, maximum likelihood or Bayesian methods ([7.8](/7.8));
- haplotype networks, in which closely related sequences are joined by the mutational steps that separate them; the statistical parsimony network (Templeton et al. 1992) connects haplotypes when the probability of parsimony exceeds 95 %. Networks represent the genealogy within species better than bifurcating trees, because ancestral haplotypes often persist in the population alongside their descendants and recombination and homoplasy create reticulations;
- **coalescent** theory ([7.10.7](/7.10.7)): the genealogy of a sample traced back to its most recent common ancestor is a random process whose shape depends on the effective population size, its changes, migration, selection and divergence, so models fitted to the genealogy estimate past population sizes, bottlenecks and expansions, divergence times and migration rates.

The repeated glaciations of the Pleistocene were the dominant influence on the present genetic structure of temperate species. At the Last Glacial Maximum, about 21,000 years ago, ice sheets covered much of northern Europe and North America, and many temperate species survived only in **glacial refugia**, areas where they persisted through the adverse period, in Europe mainly the Iberian, Italian and Balkan peninsulas (Hewitt 2000). Phylogeographic surveys infer refugia from the genetic diversity of present populations: refugial populations have higher diversity, more private alleles and older haplotypes than populations in recolonized areas, which were founded by a series of dispersal events from the leading edge of the expanding range, each losing variation (a series of founder effects, [7.19.17](/7.19.17)). Comparing the genetic similarity between populations in formerly glaciated areas and those in the refugia reveals the recolonization routes: in Europe the grasshopper *Chorthippus parallelus* recolonized most of the continent from the Balkans, the hedgehog from all three peninsulas, and the brown bear from Iberia and the Carpathians or farther east, with suture zones where lineages from different refugia meet. Species distribution models, which relate occurrences to climate, are projected onto reconstructions of past climates to locate potential refugia independently of the genetic data ([7.19.49](/7.19.49)), and the two lines of evidence are combined. In East Asia, where glaciers were less extensive, the mountains of southwestern China, the Qinling and the Taiwan region served as refugia for many species, and many lineages persisted in multiple refugia through the cold periods.

### 20.6.2. Environmental DNA and Metabarcoding

Organisms shed DNA into their surroundings in skin cells, mucus, feces, urine, pollen and gametes. This *environmental DNA* (eDNA) can be extracted from water, soil, sediment, air or snow and identified by sequence, without seeing or catching the organisms. Detection of a single target species uses species-specific quantitative PCR: eDNA surveys detect great crested newts in ponds and invasive Asian carp ahead of their invasion front more efficiently than traditional methods. *Metabarcoding* amplifies a barcode region from all the species in a sample with universal primers and sequences the mixture by high-throughput sequencing, giving a list of taxa present: fish communities from a liter of water, the diet of a herbivore from its feces, the fungi and invertebrates of a soil sample, or the past vegetation of a region from DNA preserved in lake sediments and permafrost (Taberlet et al. 2012). The limitations are those of any indirect method: detection does not prove that an organism is present (DNA can be transported downstream or brought in by predators), absence of detection does not prove absence, degradation of DNA depends on temperature, ultraviolet light and microbes, reference databases are incomplete, and the number of sequence reads is only loosely related to abundance or biomass. Used with these caveats, eDNA has become a standard tool of biodiversity monitoring.

## Summary

| Topic | Key quantities and results |
|---|---|
| species | morphological, biological ([Definition 11.1.1](/7.10.11#def-11.1.1) of 7.10.11) and phylogenetic concepts; most are criteria for recognizing separately evolving lineages |
| DNA barcoding | COI (animals), *rbcL* + *matK* (plants), ITS (fungi); ~2 % threshold; the barcode gap fails in young species (Figure 1); minimalist descriptions of 403 new braconids |
| names | binomials in italics; trinomials for subspecies, var. for plant varieties; codes regulate ranked names; PhyloCode defines clades |
| population processes | Hardy–Weinberg; mutation, gene flow, nonrandom mating, drift, selection; $W = ml$, $s = 1 - w$; hybrid origin of *R. brelichi* |
| diversity | $A$, $P$, $H_{\mathrm{o}}$, $H_{\mathrm{e}} = 1 - \sum x_i^2$, $\pi$ (Definition 20.3.1); $F = 1 - H_{\mathrm{o}}/H_{\mathrm{e}}$, Eq. (20.1) |
| effective size | $H_t = H_0(1 - 1/2N_{\mathrm{e}})^t$; sex ratio, variance in reproductive success, harmonic mean; $N_{\mathrm{e}}/N \approx 0.1$ |
| estimating $N_{\mathrm{e}}$ | linkage disequilibrium ($\mathbb{E}[r^2] \approx 1/(3N_{\mathrm{e}}) + 1/S$); temporal method, Eq. (20.3) |
| 50/500 rule | 50 against inbreeding depression, 500 for evolutionary potential; revised to 100/1000 or more |
| differentiation | $F_{\mathrm{IS}}, F_{\mathrm{ST}}, F_{\mathrm{IT}}$ (Definition 20.5.1); $F_{\mathrm{ST}} \approx 1/(1 + 4N_{\mathrm{e}}m)$, Eq. (20.4); about one migrant per generation prevents strong divergence |
| phylogeography | molecular clock, gene trees, haplotype networks, coalescent; refugia have higher diversity and private alleles; recolonization routes |
| eDNA | single-species detection and community metabarcoding; detection is not presence |

## Questions

1. A population of a deer has 200 adult females and 200 adult males, but only 20 males mate. Calculate $N_{\mathrm{e}}$ and the expected loss of heterozygosity over 20 generations. How would a management plan that culls males change this?

   **Answer** $N_{\mathrm{e}} = 4 \times 20 \times 200/220 = 72.7$. After 20 generations, $H_{20}/H_0 = (1 - 1/145.5)^{20} = 0.87$: 13 % of the heterozygosity is lost, compared with about 2.5 % for $N_{\mathrm{e}} = 400$. Culling males does not change $N_{\mathrm{e}}$ much as long as the number of breeding males is unchanged; what matters is how many males actually sire offspring. A cull that left fewer than 20 breeding males would lower $N_{\mathrm{e}}$ further; measures that increase the number of successful sires (for example, a more even age structure of males) would raise it.

2. A population was 500, 500, 50, 500 and 500 individuals in five successive generations. Calculate the harmonic mean, and compare with the arithmetic mean. What is the lesson for the management of populations that suffer occasional crashes?

   **Answer** $1/N_{\mathrm{e}} = \frac15(4/500 + 1/50) = \frac15(0.008 + 0.02) = 0.0056$, so $N_{\mathrm{e}} = 179$, against an arithmetic mean of 410. One bad generation reduces the long-term effective size by more than half. Preventing crashes (for example by protecting the population against catastrophes or keeping several separate subpopulations) preserves more genetic variation than raising the population size in good years.

3. Two samples of 50 individuals, taken 6 generations apart, give $F_c = 0.045$. Estimate $N_{\mathrm{e}}$, and explain why the estimate would be unreliable if $F_c$ were $0.021$.

   **Answer** Eq. (20.3): $F_c - 1/100 - 1/100 = 0.025$, so $\hat N_{\mathrm{e}} = 6/(2 \times 0.025) = 120$. If $F_c = 0.021$, the corrected value is $0.001$ and $\hat N_{\mathrm{e}} = 3000$; but the sampling correction (0.02) is then almost the whole of $F_c$, and small random errors in $F_c$ change the estimate enormously or make it negative (infinite $N_{\mathrm{e}}$). The temporal method is informative only when the drift signal $t/(2N_{\mathrm{e}})$ is large compared with the sampling noise $1/S$; for large populations one needs larger samples, more loci or longer intervals.

4. Explain why $F_{\mathrm{ST}} = 0.2$ between two populations of a fish in neighboring rivers does not prove that one migrant moves between them per generation.

   **Answer** $N_{\mathrm{e}}m = (1/0.2 - 1)/4 = 1$ follows only under the island model at equilibrium between drift and migration. If the populations were founded recently from different sources, or separated recently, $F_{\mathrm{ST}}$ reflects history rather than current gene flow; selection on the markers or linked loci, unequal population sizes, a stepping-stone rather than island structure, and high mutation rates of microsatellites all bias the estimate. Direct methods (tagging, assignment tests, parentage analysis) or coalescent models that separate divergence time from migration ([7.10.25](/7.10.25)) are needed to estimate current dispersal.

5. A survey of a plant across Europe finds the highest haplotype diversity and many private haplotypes in the Balkans, and a single haplotype throughout northern Europe. Interpret the pattern, and suggest how a species distribution model could test your interpretation.

   **Answer** The Balkans were probably a glacial refugium, in which the species persisted through the last glacial period with a large effective size, accumulating and keeping diverse lineages; northern Europe was recolonized after the ice retreated by expansion from the leading edge of the range, through a series of founder events that lost most haplotypes (the "southern richness, northern purity" pattern). A species distribution model fitted to the present distribution and climate can be projected onto reconstructions of the climate at the Last Glacial Maximum: if it predicts suitable climate in the Balkans (and little in the north) at that time, the interpretation is supported; suitable areas elsewhere without genetic signatures would suggest cryptic refugia or extinction of refugial lineages.

6. (Open question) A conservation agency plans to use eDNA metabarcoding of river water to monitor the fish fauna of the Yangtze after the fishing ban. Discuss the advantages, limitations and design of such a program.

   **Answer** Key points: advantages include high sensitivity for rare species (such as the Yangtze finless porpoise and rare cyprinids), no harm to animals, standardized sampling at many sites and times, and simultaneous detection of invasive species. Limitations: DNA is transported downstream, so detection localizes a species only to an upstream reach; detection probability varies with discharge, temperature and turbidity; reference databases for Chinese freshwater fishes are incomplete, and closely related species may share barcode sequences; read numbers are only loosely related to abundance. Design: replicate water samples per site and season, field and laboratory blanks against contamination, several markers (for example 12S and COI), occupancy models that estimate detection probability, calibration with traditional surveys (nets, hydroacoustics) at some sites, and archiving of samples for later reanalysis.
