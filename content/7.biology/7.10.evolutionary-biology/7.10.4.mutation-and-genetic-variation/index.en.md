---
title: Mutation and Genetic Variation
description: "How variation is inherited and mixed (segregation and Hardy–Weinberg proportions, recombination and linkage disequilibrium, horizontal gene transfer); mutation as the ultimate source of variation (point and structural mutations, duplication, polyploidy, transposition); mutation rates per site, gene and genome and how they are estimated (phylogenetic, mutation-accumulation and direct methods; Bateman–Mukai); the distribution of fitness effects, pleiotropy, germline and somatic mutation; in what sense mutation is random (replica plating, mutation bias); measuring variation (allozymes, segregating sites, heterozygosity, nucleotide diversity, kinds of DNA variants); nongenetic inheritance (epigenetic, maternal, cultural)."
---

No two organisms are alike: people differ in hair color, the shape of the nose and the length of the fingers, and at millions of sites in their genomes. Physics and chemistry deal with identical electrons; evolution depends on differences. Natural selection acts only on heritable variation ([7.10.3](/7.10.3)), and drift, migration and the other processes of evolution change the frequencies of variants that already exist. This chapter asks where heritable variation comes from, how it is passed on and mixed, how fast new variation arises and what its effects are, how it is measured, and which forms of inheritance other than DNA sequence contribute to it.

The molecular mechanisms are covered elsewhere and are only linked here: DNA replication and repair ([7.2.7](/7.2.7), [7.2.8](/7.2.8)), recombination and mobile elements ([7.2.9](/7.2.9)), the kinds of mutations, their rates and the fluctuation test ([7.4.12](/7.4.12)), chromosomal rearrangements and polyploidy ([7.4.15](/7.4.15), [7.4.16](/7.4.16)), Hardy–Weinberg equilibrium and linkage disequilibrium ([7.4.22](/7.4.22)), and the detection of variants in sequencing data ([7.8.12](/7.8.12)). The emphasis here is on the evolutionary questions: what fraction of mutations is harmful or useful, whether mutation is random, and how much variation populations contain. The next chapters build the theory of how selection ([7.10.5](/7.10.5)) and drift ([7.10.6](/7.10.6)) act on this variation.

## 4.1. The Inheritance and Mixing of Variation

### 4.1.1. Genes, Alleles and Their Frequencies

The genetic material of almost all organisms is DNA; some viruses use RNA. The human genome has about $3.2 \times 10^9$ base pairs and roughly 20,000 protein-coding genes, which occupy only a small part of it ([7.2.2](/7.2.2)); genomes of bacteria can be a thousand times smaller and those of some plants, salamanders and protists hundreds of times larger, with little relation to the complexity of the organism ([7.10.18](/7.10.18)). A locus is a position in the genome; if the DNA at a locus varies among the chromosomes of a population, the locus is polymorphic and the variants are alleles. A single base that varies is a **single nucleotide polymorphism** (SNP). The **allele frequency** is the proportion of the gene copies in a population that carry a given allele: the alleles that cause albinism together have a frequency of about 0.007 in Europeans (about one person in 20,000 is homozygous and affected), and the A allele of the ABO blood groups has a frequency of about 0.25–0.3 in the United States.

Changes in protein-coding sequences are synonymous if, because of the redundancy of the **genetic code**, they do not change the amino acid, and nonsynonymous (replacement) if they do. At the sixth codon of human β-globin, GAG (glutamate) to GAA is synonymous; GAG to GTG replaces glutamate by valine and creates the sickle-cell allele $S$. The two kinds of change evolve very differently, a contrast that is the basis of many tests of selection ([7.10.8](/7.10.8), [7.10.23](/7.10.23)).

### 4.1.2. Mixing by Segregation

In sexual organisms segregation and recombination mix the genes of the parents in every generation. Segregation, the transmission of one of the two copies of each locus to each gamete, followed by random union of gametes, gives the **Hardy–Weinberg equilibrium** proportions $p^2 : 2pq : q^2$ after one generation of random mating, whatever the initial genotype frequencies, while leaving the allele frequencies unchanged ([7.4.22](/7.4.22#thm-22.2.1)). The conditions are an infinite population, no selection, mutation or migration, and random mating; no real population meets them exactly, but the equilibrium is the null model against which these processes are detected.

**Example 4.1.1** Among 654 adults from Musoma, in present-day Tanzania, typed at the β-globin locus there were 400 $AA$, 249 $AS$ and 5 $SS$. The frequency of $S$ is $q = (249 + 2 \times 5)/1308 = 0.198$, and the Hardy–Weinberg expectations are $0.643$, $0.318$ and $0.039$, or 420.6, 207.7 and 25.6 individuals. The observed excess of heterozygotes and deficit of both homozygotes gives $\chi^2 = 25.8$ with one degree of freedom ($P < 10^{-6}$; [7.4.22](/7.4.22#sec-22.2.2)). The departure is caused by differences in survival: in a region with malaria, $AS$ heterozygotes survive better than either homozygote ([7.4.23](/7.4.23#ex-23.3.3)).

### 4.1.3. Mixing by Recombination

Recombination combines in one gamete alleles at different loci that were inherited from different parents: loci on different chromosomes by independent assortment (recombination rate $r = 1/2$), loci on the same chromosome by crossing over ($0 \le r < 1/2$, smaller for closer loci). A nonrandom association of alleles at two loci is **linkage disequilibrium**, measured by $D = p_{AB} - p_A p_B$; it is defined in the same way for linked and unlinked loci. Mendelian inheritance alone makes $D$ decay by the factor $1 - r$ per generation ([7.4.22](/7.4.22#thm-22.3.1)), so that disequilibrium persists longest between closely linked sites, which is why it can be used to map genes ([7.4.25](/7.4.25)).

Two processes create disequilibrium. Selection on combinations of alleles (**epistasis** for fitness) does: in the primrose *Primula vulgaris*, the height of the anthers and the height of the stigma are controlled by two tightly linked loci, and the allele for high anthers is almost always combined with the allele for a low stigma (the "thrum" form) and vice versa ("pin"), because the rare recombinant plants, with anthers and stigma at the same height, self-fertilize and produce offspring that survive poorly; the complex behaves as a **supergene** ([7.4.15](/7.4.15)). Mixing of populations with different allele frequencies also creates disequilibrium: in an admixed population, alleles that are common in one source population are found together more often than expected, even at unlinked loci.

The amount of variation that recombination can generate is enormous. A pair of homologous chromosomes that differ at 1000 SNPs could in principle produce $2^{1000} \approx 10^{301}$ different recombinant chromosomes. Most of the genetic differences between individuals of a sexual species are new combinations of existing alleles rather than recent mutations, and selection can act on them for many generations even without new mutations ([7.10.1](/7.10.1#sec-1.4.2), [7.10.3](/7.10.3#sec-3.4.3)).

### 4.1.4. Mixing without Sex

Prokaryotes, viruses and a few eukaryotes reproduce without meiosis, but most still mix genes. **Horizontal gene transfer** moves DNA between individuals, of the same or of different species, by conjugation, by uptake of free DNA (transformation) and by viruses that carry host genes to new hosts (transduction) ([7.4.10](/7.4.10), [7.10.2](/7.10.2#sec-2.5.1)). The mechanisms differ from meiosis, but the evolutionary consequence is the same: new combinations of genes, including the spread of antibiotic resistance among pathogens.

## 4.2. Mutation: The Ultimate Source of Variation

DNA replication is very accurate but not perfect, and DNA is damaged by chemical reactions and radiation. The errors that escape **proofreading** and repair are mutations, the ultimate source of all genetic variation: without them there would be no variation, no evolution and no life. In a fundamental sense mutation is inevitable, since no physical process operates without error.

### 4.2.1. Kinds of Mutation

Mutations range from a single base to the whole genome. The classification of mutations and their consequences for genes was given in [7.4.12](/7.4.12#sec-12.2) and [7.4.15](/7.4.15); the table summarizes it from the evolutionary point of view.

| Kind | Change | Evolutionary notes |
|---|---|---|
| **Point mutation** | one base replaced: **transition** (purine to purine, pyrimidine to pyrimidine) or **transversion** | transitions are more frequent although there are twice as many possible transversions; at codon third positions most are synonymous, at second positions all are nonsynonymous |
| Insertion, deletion (**indel**) | a few to many bases gained or lost | in coding sequence often a frameshift; a 3-bp deletion in the chloride channel gene *CFTR* (ΔF508) is the commonest cystic fibrosis allele; expansions of CAG repeats cause Huntington disease ([7.4.12](/7.4.12#def-12.6.1)) |
| Duplication | a segment, or a whole gene, copied | creates gene families; duplicates may diverge into new functions ([7.10.18](/7.10.18)); copies can be homogenized by **gene conversion** |
| **Inversion** | a segment reversed | suppresses recombination in heterozygotes; humans and chimpanzees differ by about 1500 inversions fixed since their common ancestor, roughly 7 Myr ago |
| **Reciprocal translocation**, fusion, fission | segments exchanged between chromosomes, chromosomes joined or split | heterozygotes can be semisterile, contributing to isolation between species ([7.10.11](/7.10.11)); human chromosome 2 arose by fusion of two ancestral ape chromosomes |
| **Polyploidy**, **whole-genome duplication** | all chromosomes doubled | common in plants; can create a new species in one step ([7.4.16](/7.4.16), [7.10.12](/7.10.12)) |
| Transposition | a **transposon** inserts at a new site | a major source of spontaneous mutations in *Drosophila*; genome expansion ([7.4.17](/7.4.17)) |

Changes in chromosome number and structure accumulate through fusions and fissions, and chromosome numbers vary enormously: the Australian jack jumper ant *Myrmecia pilosula* has a single pair of chromosomes in females, the adder's-tongue fern *Ophioglossum reticulatum* about 630 pairs, and the ciliate *Oxytricha trifallax* about 16,000 tiny chromosomes in its somatic nucleus. Surprisingly often, such changes have no obvious phenotypic effect.

Point mutations in noncoding DNA can affect gene expression; the genetic changes underlying adaptation involve both coding and regulatory sequences ([7.10.19](/7.10.19)).

### 4.2.2. Where Mutations Come From

Most spontaneous point mutations arise from errors in replication that escape proofreading and **mismatch repair**, and from spontaneous chemical damage ([7.2.7](/7.2.7), [7.2.8](/7.2.8)). Two sources shape the pattern of mutation across genomes. *Slipped-strand mispairing* during replication of repeated sequences changes the number of repeat units, so that runs of one base and **microsatellites** have very high indel mutation rates, which makes microsatellites useful markers of individual identity and population structure. The **deamination** of cytosine produces uracil, which is recognized and removed; the deamination of 5-methylcytosine produces thymine, a normal base, leaving a G·T mismatch that is often repaired wrongly. Because mammals methylate cytosine mainly in CpG dinucleotides, C→T transitions at CpG sites are among the most frequent mutations in mammalian genomes, and CpG dinucleotides are depleted except in unmethylated CpG islands. Mutation rates also vary with replication timing, chromatin, distance from origins, and the presence of repeats.

## 4.3. Rates of Mutation

### 4.3.1. Per Site, per Gene and per Genome

The **mutation rate** $\mu$ is the probability that a mutation occurs per unit of DNA (base pair, gene, genome) per generation or per cell division ([7.4.12](/7.4.12#def-12.5.1), where typical values are tabulated). In *Escherichia coli* the rate is of the order of $10^{-10}$ per base pair per replication; in the human germline it is about $1.2 \times 10^{-8}$ per base pair per generation; in RNA viruses such as HIV, influenza and Ebola virus it is thousands of times higher, $10^{-5}$ to $10^{-3}$ per base, partly because their polymerases do not proofread. Rates per gene are higher than rates per base, because a gene mutates if any of its bases does: typically $10^{-5}$ to $10^{-7}$ per generation for protein-coding loci in animals.

**Formula 4.3.1 (Genomic Mutation Rate)** The expected number of new mutations per genome per generation is
$$
U = \mu G,
$$
for a per-site rate $\mu$ and $G$ sites. With $\mu = 1.2 \times 10^{-8}$ and a haploid human genome of $3.1 \times 10^9$ bp, each gamete carries about $37$ new mutations, and each child about 70; of these, on the order of one per gamete is deleterious.

Across species, per-site rates are lower in organisms with larger genomes among DNA-based microbes, so that the rate per genome per replication is roughly constant (about $0.003$, Drake's rule), whereas multicellular eukaryotes with large genomes and small effective population sizes have higher per-site rates per generation. Michael Lynch's **drift-barrier hypothesis** explains the pattern: selection favors lower mutation rates because most mutations are harmful, but it can push the rate down only until the benefit of a further reduction is too small to overcome genetic drift, a limit that is reached at higher rates in species with small effective population sizes ([7.10.6](/7.10.6)). Rates per generation also depend on the number of germline cell divisions: human eggs are formed in the fetus after about 30 divisions, whereas sperm are produced throughout adult life from stem cells that have divided more than 100 times, and most new point mutations in children come from the father, more as the father is older (the **paternal age effect**, [7.4.12](/7.4.12#def-12.5.3)).

### 4.3.2. Estimating Mutation Rates

Mutation rates are estimated in four ways ([7.4.12](/7.4.12#sec-12.5) for the classical methods).

1. *Phenotypic screens.* Count new mutants with a visible phenotype among many individuals (for example, new eye colors in *Drosophila* or new dominant diseases in humans); this gives per-locus rates for a few genes.
2. *The phylogenetic method.* A neutrally evolving segment accumulates substitutions at the rate $\mu$ per generation ([7.4.23](/7.4.23#thm-23.7.1)), so two species whose common ancestor lived $t$ generations ago differ at a fraction $D \approx 2\mu t$ of its sites.
3. *Mutation accumulation.* Many lines are founded from one genotype and propagated for many generations under conditions that minimize selection (single-individual or single-pair transfers); the lines are then sequenced, or their fitness measured (Section 4.4).
4. *Direct sequencing.* Sequence parents and offspring (trios), or the ancestor and descendants of a mutation-accumulation line, and count new mutations.

**Formula 4.3.2 (Estimators of the Mutation Rate)** (a) Phylogenetic: $\hat\mu = \dfrac{\hat D}{2t}$, with $\hat D$ the proportion of neutral sites that differ (corrected for multiple hits) and $t$ the number of generations since divergence. (b) Direct, from $m$ new mutations observed in one child at $L$ callable sites per haploid genome: $\hat\mu = \dfrac{m}{2L}$, since the child received two genomes. (c) Mutation accumulation, from $m$ mutations among $n$ lines propagated for $t$ generations, with $L$ sites surveyed per line: $\hat\mu = \dfrac{m}{nLt}$. Counts of mutations are approximately Poisson, so the standard error of $\hat\mu$ is about $\hat\mu/\sqrt m$.

**Example 4.3.1** (a) A trio in which 70 new single-nucleotide mutations are found at $2.8 \times 10^9$ callable sites gives $\hat\mu = 70/(2 \times 2.8 \times 10^9) = 1.25 \times 10^{-8}$ per site per generation, with a standard error of about $12\%$. (b) Human and chimpanzee genomes differ at about $1.2\%$ of aligned sites. Taking a split 6.5 Myr ago and a generation time of 25 years ($2.6 \times 10^5$ generations) gives $\hat\mu = 0.012/(2 \times 2.6 \times 10^5) = 2.3 \times 10^{-8}$, about twice the direct estimate. The discrepancy comes from the assumptions of the phylogenetic method: the genomes diverged before the species split, because ancestral polymorphism takes time to sort ([7.10.7](/7.10.7)); generation times and rates may have changed; and the date itself is uncertain. Reconciling the two estimates is a research problem of molecular dating ([7.10.24](/7.10.24)).

:::

The methods have complementary weaknesses. The phylogenetic method applies only to neutral sequences and needs the number of generations; mutation accumulation gives few mutations and works only for organisms that can be propagated in the laboratory; direct sequencing has no such assumptions, but mutations in any one gene are so rare that it gives only averages over large regions of the genome, and it must distinguish true mutations from sequencing errors.

## 4.4. The Effects of Mutations

### 4.4.1. Pleiotropy

Mutations affect every kind of trait, from the substrates a bacterium can use to the ability of a child to learn language. Almost every mutation with a phenotypic effect has effects on several traits, **pleiotropy**. Achondroplasia, caused by one recurrent substitution in the receptor gene *FGFR3*, reduces the conversion of cartilage to bone and thus the size of most bones, particularly in the limbs, and also affects longevity and many aspects of physiology. Pleiotropy means that a genetic change that improves one feature usually has side effects on others, a source of the trade-offs of [7.10.3](/7.10.3#sec-3.6) and of the genetic correlations of [7.10.9](/7.10.9).

### 4.4.2. The Distribution of Fitness Effects

**Definition 4.4.1 (Distribution of Fitness Effects)** The **distribution of fitness effects** (DFE) of new mutations is the probability distribution of their selection coefficients $s$, the proportional change in fitness they cause. A mutation with $s < 0$ is a **deleterious mutation**, one with $s > 0$ a **beneficial mutation**, and one whose effect is too small to be detected by selection, $\lvert 4N_{\mathrm{e}}s\rvert \ll 1$, is effectively neutral.

Mutations range from lethal through strongly and mildly deleterious and nearly neutral to beneficial, but most mutations with a detectable effect are deleterious, and beneficial ones are rare. The reason is easy to see for an enzyme: its sequence has been refined by selection, and most changes to the sequence disrupt its fold or its active site. Saturation mutagenesis of a short segment of the gene for the chaperone Hsp90 in yeast, which measured the fitness effects of 560 mutations, found most nonsynonymous changes and all stop codons to be deleterious, synonymous changes nearly neutral, and few beneficial. Statistical analyses of polymorphism in human genes indicate that the effects of new nonsynonymous mutations are broadly distributed, with roughly 12% decreasing fitness by 10% or more and many of very small effect. Most deleterious mutations are partly recessive: they are more than twice as harmful in homozygotes as in heterozygotes. The DFE of new mutations differs from the distribution of effects among the differences between species, which are enriched for beneficial and neutral changes, the ones that spread.

**Formula 4.4.1 (Gamma DFE)** The deleterious part of the DFE is commonly modeled by a gamma distribution of $\lvert s\rvert$ with shape $\beta$ and mean $\bar s$:
$$
f(\lvert s\rvert) = \frac{(\beta/\bar s)^\beta}{\Gamma(\beta)} \lvert s\rvert^{\beta - 1} \mathrm{e}^{-\beta\lvert s\rvert/\bar s}.
$$
A shape $\beta < 1$ gives a distribution with most mass near zero and a long tail of strongly deleterious mutations; the fraction of mutations that are effectively neutral in a population of effective size $N_{\mathrm{e}}$ is $F(1/4N_{\mathrm{e}})$, with $F$ the distribution function.

Because the boundary between neutral and selected is $\lvert s\rvert \approx 1/4N_{\mathrm{e}}$, the same mutations behave as mostly neutral in a small population and as mostly selected in a large one. This is the basis of the **nearly neutral theory** ([7.10.6](/7.10.6)): small populations fix more slightly deleterious mutations, and the rate of molecular evolution depends on population size. Methods for estimating the DFE from the site frequency spectrum are treated in [7.10.8](/7.10.8).

![The distribution of fitness effects of new deleterious mutations (Definition 4.4.1), modeled by a gamma distribution of |s| (Formula 4.4.1) with shape 0.2 and mean 0.04, illustrative values chosen so that 12% of mutations have |s| > 0.1, as estimated for human nonsynonymous mutations. A: the distribution of log10 |s|: a minority of mutations are strongly deleterious and most are mildly deleterious or nearly neutral. B: the fraction of the same mutations that behave as effectively neutral, |4N_e s| < 1, as a function of the effective population size: about 18% in a population of the size of the human one and 7% in one of the size of *Drosophila melanogaster*](./plots/dfe.py)

### 4.4.3. Measuring Effects by Mutation Accumulation

If mutation-accumulation lines are kept without selection, their fitness declines as deleterious mutations accumulate, and the lines diverge because each accumulates different mutations. The rate of decline and the rate of divergence give two moments of the DFE.

**Formula 4.4.2 (Bateman–Mukai Estimates)** Suppose each line gains a Poisson number of new mutations with mean $U$ per generation, each lowering fitness by an amount $s$ drawn independently from a distribution with moments $\mathbb{E}[s]$ and $\mathbb{E}[s^2]$, and effects are additive. Then after $t$ generations the mean and the variance of fitness among lines change at the rates
$$
\Delta M = U\,\mathbb{E}[s], \qquad \Delta V = U\,\mathbb{E}[s^2],
$$
and since $\mathbb{E}[s^2] \ge \mathbb{E}[s]^2$,
$$
U \ge \frac{(\Delta M)^2}{\Delta V}, \qquad \mathbb{E}[s] \le \frac{\Delta V}{\Delta M},
$$
with equality only if all effects are equal.

**Proof** The fitness decline of a line after $t$ generations is a compound Poisson sum $\sum_{i=1}^{K} s_i$ with $K \sim \mathrm{Poi}(Ut)$. Its mean is $\mathbb{E}[K]\mathbb{E}[s] = Ut\,\mathbb{E}[s]$ and its variance $\mathbb{E}[K]\operatorname{Var}(s) + \operatorname{Var}(K)\mathbb{E}[s]^2 = Ut(\operatorname{Var}(s) + \mathbb{E}[s]^2) = Ut\,\mathbb{E}[s^2]$, since for the Poisson distribution $\operatorname{Var}(K) = \mathbb{E}[K]$ ([3.1.4](/3.1.4)). Dividing by $t$ gives the rates; the inequalities follow from $\operatorname{Var}(s) \ge 0$. $\square$

The method, introduced by A. J. Bateman (1959) and Terumi Mukai (1964) for the viability of *Drosophila* chromosomes, gives a lower bound on $U$ and an upper bound on the mean effect: mutations of small effect are missed, so the estimates are biased toward fewer mutations of larger effect, as the simulation shows. Direct sequencing of mutation-accumulation lines now counts the mutations themselves, and combining the two kinds of data gives the mean effect per mutation.

![A mutation-accumulation experiment, simulated (Formula 4.4.2). 400 lines founded from one genotype are propagated for 50 generations without selection; each generation a line gains a Poisson number of new mutations with mean U = 0.4 per genome, each lowering fitness by an amount drawn from an exponential distribution with mean 0.02 (illustrative values). A: fitness of 20 lines (gray) and the mean of all lines (dots), with the expected decline 1 − U E[s] t. B: the variance of fitness among lines (blue) and its expectation U E[s²] t (dashed), both rising linearly. The Bateman–Mukai bounds computed from the slopes are U ≥ 0.21 and E[s] ≤ 0.038: with exponentially distributed effects they recover about half the true U and twice the true mean effect](./plots/mutation-accumulation.py)

### 4.4.4. Large Mutations and the Evolution of Mutation Rates

Some mutations have dramatic effects. Homeotic mutations transform one body part into another: the *Antennapedia* mutation of *Drosophila* converts the antennae into legs (**homeotic transformation**, [7.5.15](/7.5.15)). Such mutations disrupt developmental pathways that evolved through many smaller changes; they do not show that complex structures originate by single mutations. Goldschmidt's "hopeful monsters" ([7.10.1](/7.10.1#sec-1.4.1)) have been tested and rejected, although some adaptive differences between species do involve mutations of large effect ([7.10.9](/7.10.9)).

Because most mutations are harmful, natural selection in sexual organisms favors lower mutation rates; that the rates are not lower still is explained by the drift barrier and by the costs of more accurate replication. It is a strange fact that life, the product of natural selection, exists only because selection is not efficient enough to drive mutation rates to zero: without mutation, no adaptation to changing conditions would be possible. In asexual populations adapting to new conditions, mutator alleles, which raise the mutation rate, can increase in frequency by hitchhiking with the beneficial mutations they cause.

### 4.4.5. Germline and Somatic Mutations

In many animals a small group of cells is set aside early in development to form the germ line, which produces the gametes; the remaining cells form the soma. A **germline mutation** can be transmitted to the next generation; a **somatic mutation**, such as the mutations caused by ultraviolet light in skin cells, cannot ([7.4.12](/7.4.12#def-12.5.2)). Somatic mutations are nevertheless important in evolution: they cause cancer ([7.4.21](/7.4.21), [7.3.26](/7.3.26)), which reduces survival and reproduction, so that natural selection favors germline alleles that improve DNA repair and the suppression of tumors in long-lived, large organisms. Plants and some animals, such as sponges and corals, have no segregated germ line: their gametes arise from somatic cells that have divided many times during growth, so somatic mutations can be transmitted.

## 4.5. Is Mutation Random?

"Random" has several meanings, and mutation is random in one sense but not in others.

**Definition 4.5.1 (Mutation Bias)** **Mutation bias** is any systematic difference in the rates at which different kinds of mutations occur: among types of base substitution, among sequence contexts and genomic regions, or between gains and losses of a feature.

Mutation is not random in the sense of all changes being equally likely. Transitions are more frequent than transversions although there are twice as many possible transversions (in humans the ratio of transitions to transversions among new mutations and SNPs is about 2), because they distort the double helix less and escape repair more often; C→T changes at methylated CpG sites are about ten times more frequent than other substitutions; indels are frequent in repeats. Mutation biases can influence the course of evolution when the supply of mutations limits adaptation, because mutations that arise more often are more likely to be the ones that spread.

Mutation is random in the fundamental sense that matters for evolution: mutations are not directed toward what improves fitness in the conditions where they occur. A new environment does not increase the rate of the particular mutations that would be advantageous in it. Salvador Luria and Max Delbrück (1943) showed this with the **fluctuation test**: the numbers of phage-resistant bacteria in parallel cultures vary far more than a Poisson distribution allows, as expected if resistance mutations occur at random times during growth before exposure to the phage, and not if exposure induces them ([7.4.12](/7.4.12#sec-12.4)). Joshua and Esther Lederberg (1952) made the point visible with **replica plating**.

![The replica-plating experiment of Joshua and Esther Lederberg. A master plate carries colonies grown from a single phage-sensitive cell of *E. coli*; a velvet pad transfers cells from every colony, keeping their positions, to replica plates containing phage T1, which kills sensitive cells. Top: if the phage induced resistance mutations, surviving colonies would appear at different positions on different replica plates. Bottom: if resistance mutations arose at random before exposure, resistant cells are already present in particular colonies of the master plate (green rings), and survivors appear at the same positions on every replica plate. The second outcome is observed: resistant colonies can be recovered from the master plate without ever having been exposed to the phage](./plots/replica-plating.py)

The conclusion follows also from the mechanisms: DNA polymerase and the repair enzymes cannot distinguish a coding from a noncoding site, or a change that will help from one that will harm. Later experiments with nonlethal selection, such as bacteria unable to use lactose plated on lactose, showed that mutations allowing growth also arise after plating; the mechanism is a stress-induced increase of mutation rates over large parts of the genome (the SOS response and error-prone polymerases, [7.2.8](/7.2.8#def-8.6.2)), not a production of the needed mutations specifically. Environments can change mutation rates, as radiation and mutagens do, but the mutations they cause are not particularly suited to the environment. A population adapts because selection picks out the favorable mutations among the random ones.

## 4.6. Measuring Genetic Variation

### 4.6.1. From Visible Polymorphisms to Genomes

Until the 1960s genetic variation could be studied only in traits that happened to vary visibly (color patterns, blood groups) and only in a few organisms. Two views competed. In the classical view, associated with Hermann Muller, most loci have a single best, wild-type allele, and variation consists of rare deleterious mutations; in the balance view, associated with Dobzhansky, many loci are polymorphic because of balancing selection, and variation is abundant ([7.10.1](/7.10.1#sec-1.4.2)). Hidden variation could be revealed by inbreeding. With balancer chromosomes, which suppress recombination and carry a dominant marker, single wild chromosomes of *Drosophila* can be extracted and made homozygous; in Brazilian populations of *D. willistoni* studied by Dobzhansky and his colleagues, about 29 % of second chromosomes carried recessive lethals and another 13 % semilethals (data in Barton et al. 2007, Table 13.1), so that apparently normal wild flies carry a large load of concealed recessive mutations. Protein electrophoresis, introduced to population genetics in 1966 by Richard Lewontin and John Hubby for *Drosophila* and by Harry Harris for humans, resolved the question of quantity. It separates allelic forms of enzymes that differ in charge, the *allozymes*: variants encoded by alleles of the same locus, a subset of the **isozymes**, which comprise all enzymes of different sequence that catalyze the same reaction, including those encoded by different loci (paralogs). Electrophoresis can be applied to any organism and to loci chosen because they can be scored, not because they were known to vary. About a third of enzyme loci proved to be polymorphic in both flies and humans, far more variation than the classical view expected. The explanation of so much variation became the central debate of population genetics, between selectionists and neutralists ([7.10.6](/7.10.6)), and the narrow range of diversity across species of very different abundance remains a puzzle (**Lewontin's paradox**, [7.10.6](/7.10.6)).

![How much genetic variation is there? A: allozyme surveys by protein electrophoresis: the proportion of enzyme loci that are polymorphic and the average gene diversity H at those loci, in mammals, *Drosophila* and *Escherichia coli*. B: nucleotide diversity, the average proportion of sites that differ between two randomly chosen copies of the genome, in humans and in *Drosophila melanogaster* (log scale). Data from Barton et al. (2007), Chapter 13](./plots/variation.py)

Electrophoresis detects only some amino acid changes. DNA methods detect all kinds of variation ([7.4.14](/7.4.14#def-14.7.1), [7.8.12](/7.8.12)):

| Variant | Description | Uses |
|---|---|---|
| SNP | single-base difference; the commonest variant | genome-wide association, population structure ([7.4.25](/7.4.25), [7.8.13](/7.8.13)) |
| Indel | small insertion or deletion | |
| Microsatellite (STR) | variable number of short tandem repeats, high mutation rate | individual identification, paternity ([7.4.22](/7.4.22#sec-22.5)) |
| Copy number variant | deletion or duplication of kilobases to megabases | gene dosage; a first genome-wide survey found that a typical human carries about a dozen large deletions or duplications, averaging hundreds of kilobases |
| Inversion, translocation | balanced **structural variants** | suppressed recombination, supergenes |
| Transposable element insertion | presence or absence of a mobile element | |

### 4.6.2. Measures of Variation

Variation is summarized by a few statistics that can be compared across loci and species.

- *Proportion of polymorphic loci*: the fraction of loci at which the commonest allele has a frequency below some threshold (0.95 or 0.99). It depends on the threshold and on the sample size.
- *Gene diversity (expected heterozygosity)*: $H = 1 - \sum_i p_i^2$, the probability that two gene copies drawn at random from the population carry different alleles (**heterozygosity**, [7.4.22](/7.4.22#def-22.2.2)). It does not depend on the mating system and applies to haploids and selfers, for whom the observed heterozygosity would be misleading.

For DNA sequences, the unit is the nucleotide site.

**Definition 4.6.1 (Segregating Sites and Nucleotide Diversity)** In a sample of $n$ aligned sequences of length $L$, a *segregating site* is a site at which not all sequences carry the same base; $S$ is their number. The **nucleotide diversity** $\pi$ is the average number of differences per site between two sequences drawn at random from the sample:
$$
\pi = \frac{1}{L}\binom{n}{2}^{-1}\sum_{i<j} d_{ij},
$$
where $d_{ij}$ is the number of sites at which sequences $i$ and $j$ differ.

Equivalently, $\pi$ is the gene diversity computed site by site and averaged over sites (with the factor $n/(n-1)$ for sampling). The number of distinct sequences, the haplotypes, is a further statistic, but a poor one: in a long enough sequence every sampled copy is different. Most information lies in how the variants are combined, that is in the genealogy of the sample ([7.10.7](/7.10.7)).

**Example 4.6.1** Five alleles of the first eight codons of the alcohol dehydrogenase gene of *Drosophila pseudoobscura*:

```text
1  ATG TCT CTC ACC AAC AAG AAC GTC
2  ATG GCT CTC ACC AAC AAG AAC GTC
3  ATG TCG CTC ACC AAC AAG AAC GTC
4  ATG TCT TTG ACC AAC AAG AAC GTC
5  ATG TCT CTC ACC AAC AAG AAC GTG
```

There are $S = 5$ segregating sites among $L = 24$. The ten pairwise differences are 1, 1, 2, 1 (sequence 1 against 2–5), 2, 3, 2 (sequence 2 against 3–5), 3, 2 (sequence 3 against 4, 5) and 3 (4 against 5), summing to 20, so the mean is $2.0$ differences and $\pi = 2.0/24 = 0.083$. Translating, sequence 1 encodes Met-Ser-Leu-Thr-Asn-Lys-Asn-Val; only the change in sequence 2 (TCT→GCT, serine to alanine) is nonsynonymous; the others are synonymous: TCT→TCG (still serine), CTC→TTG (still leucine, a change at two sites) and GTC→GTG (still valine). Synonymous polymorphisms are more common than nonsynonymous ones because most amino acid changes are deleterious and are removed by selection.

:::

Under neutrality, mutation–drift equilibrium gives $\mathbb{E}[\pi] = \theta = 4N_{\mathrm{e}}\mu$ per site ([Formula 23.7.1 in 7.4.23](/7.4.23#fml-23.7.1)), and $S$ gives a second estimate of $\theta$ (Watterson's, [7.10.7](/7.10.7)); the comparison of estimates from different aspects of the data is the basis of tests of neutrality ([7.10.8](/7.10.8)). With the human $\pi \approx 0.0008$–$0.001$ and $\mu = 1.2 \times 10^{-8}$, $N_{\mathrm{e}} \approx \pi/4\mu \approx 17{,}000$–$21{,}000$, far smaller than the present population, a reflection of its small size during most of its history.

### 4.6.3. Patterns of Variation

Almost all species are genetically variable: allozyme surveys show 19% of loci polymorphic in mammals, 48% in *Drosophila* and 90% in *E. coli*, with average gene diversities of about 4%, 12% and 47%; nucleotide diversity is about $0.0008$ in humans and an order of magnitude higher, about $0.01$, in *D. melanogaster*. Diversity per site is lower than diversity per protein because a protein is encoded by hundreds of sites. Across species, nucleotide diversity is highest in prokaryotes, lower in unicellular eukaryotes and lowest in multicellular ones, and it is higher in more abundant species, but the relationship is weak. Within genomes, the rule is that changes with the least effect on the organism are the most polymorphic: in human genes, nonsynonymous diversity is less than a third of synonymous diversity, and diversity in noncoding flanking regions is lower than at synonymous sites, indicating functional constraint there too. Most of the variation of a species is found within local populations; populations of the same species typically differ only modestly in allele frequencies (by $F_{\mathrm{ST}}$ of 0.1–0.2 or less, [7.10.10](/7.10.10)).

## 4.7. Nongenetic Inheritance

Most inherited differences are differences in DNA (or RNA) sequence, but other mechanisms also transmit phenotypes across generations.

**Definition 4.7.1 (Nongenetic Inheritance)** **Nongenetic inheritance** is the transmission of phenotypic differences between generations by mechanisms other than differences in DNA sequence: epigenetic marks, maternal (and paternal) effects, and **cultural inheritance**, the transmission of information by learning from other individuals, through teaching, imitation and other forms of social transmission.

*Epigenetic inheritance* transmits states of chromatin that alter gene expression without changing the sequence: DNA methylation and histone modifications ([7.2.15](/7.2.15), [7.4.18](/7.4.18)). In the peloric mutant of toadflax (*Linaria vulgaris*), described by Linnaeus, all five petals bear nectar spurs and the flower is radially instead of bilaterally symmetrical; the mutant is due to heritable methylation that silences the gene *Lcyc*, not to a change of its sequence. Most epigenetic states are unstable and revert within a few generations (**transgenerational epigenetic inheritance**, [7.4.18](/7.4.18#def-18.6.1)): they can matter in the short term but contribute little to long-term evolutionary change.

Maternal effects occur when the genotype or phenotype of the mother determines the phenotype of her offspring (**maternal effect**, [7.4.11](/7.4.11#def-11.6.1)). The direction of coiling of the shell of the snail *Lymnaea peregra* is determined by the genotype of the mother, not by the snail's own; in mammals, the amount of milk an infant receives depends on the mother's physiology as well as her genotype and affects the infant's development. Maternal effects contribute to the resemblance of mothers and offspring for a generation or two.

*Cultural inheritance* differs from other forms in that information can pass between unrelated individuals as well as from parents to offspring. Young males of the white-crowned sparrow learn the local song dialect by hearing their father and other males, so populations a few tens of kilometers apart sing different dialects; in humans, language, religion, technology and dietary preferences are culturally inherited ([7.10.33](/7.10.33)). Human society would be impossible without it. For the great majority of organisms, however, evolutionary change results from genetic inheritance, and that is the focus of this course.

## Summary

- Variation is inherited and mixed by segregation (Hardy–Weinberg proportions, Example 4.1.1), recombination (which erodes linkage disequilibrium) and, in organisms without meiosis, horizontal gene transfer; recombination of existing variation generates most of the genetic differences between individuals of sexual species.
- Mutation is the ultimate source of variation. Its kinds range from point mutations (transitions, transversions; synonymous and nonsynonymous) through indels, duplications, inversions, translocations, fusions and fissions to polyploidy and transposition; replication slippage and the deamination of methylated CpG make repeats and CpG sites mutational hotspots.
- Mutation rates are about $10^{-10}$ per bp per replication in *E. coli*, $1.2 \times 10^{-8}$ per bp per generation in humans and $10^{-5}$–$10^{-3}$ in RNA viruses; the genomic rate $U = \mu G$ (Formula 4.3.1) is several tens per human gamete. Rates are estimated by phylogenetic, mutation-accumulation and direct methods (Formula 4.3.2, Example 4.3.1); their variation among species is explained by the drift barrier.
- Mutations are pleiotropic. The distribution of fitness effects (Definition 4.4.1) is dominated by deleterious and nearly neutral mutations, often modeled as a gamma distribution (Formula 4.4.1); which mutations are effectively neutral depends on $N_{\mathrm{e}}$. Mutation-accumulation experiments give the Bateman–Mukai bounds (Formula 4.4.2). Only germline mutations are transmitted, except in organisms without a segregated germ line.
- Mutation is biased (Definition 4.5.1) but random with respect to fitness: the fluctuation test and replica plating show that adaptive mutations arise before selection; stress raises mutation rates without directing them.
- Natural populations are highly variable. Variation is measured by the proportion of polymorphic loci, gene diversity, segregating sites and nucleotide diversity (Definition 4.6.1, Example 4.6.1); under neutrality $\mathbb{E}[\pi] = 4N_{\mathrm{e}}\mu$. Functionally important sites are less variable.
- Nongenetic inheritance (Definition 4.7.1) by epigenetic marks, maternal effects and culture is real but, except for culture in humans, contributes little to long-term evolution.

## Questions

1. In a sample of 1000 hermaphroditic daisies typed at a SNP, three populations had the following numbers of TT, TC and CC plants: population 1: 90, 420, 490; population 2: 200, 200, 600; population 3: 50, 500, 450. Which populations are in Hardy–Weinberg proportions, and what might explain the departures?

   **Answer** Population 1: $p_T = (180 + 420)/2000 = 0.30$; expected $90 : 420 : 490$, exactly as observed: in equilibrium. Population 2: $p_T = (400 + 200)/2000 = 0.30$; expected $90 : 420 : 490$; there is a large deficit of heterozygotes (200 instead of 420), as expected with self-fertilization or other inbreeding, or with a sample pooled from subpopulations with different allele frequencies (the Wahlund effect, [7.4.22](/7.4.22#thm-22.4.1)). Population 3: $p_T = (100 + 500)/2000 = 0.30$; expected again $90 : 420 : 490$; there is an excess of heterozygotes (500 instead of 420), which could be due to heterozygote advantage in survival or to disassortative mating, such as a self-incompatibility system. One generation of random mating would restore Hardy–Weinberg proportions in populations 2 and 3 if the causes were removed.

2. Explain why the Bateman–Mukai method gives a lower bound on the genomic deleterious mutation rate. If all mutations had the same effect, what would the method give?

   **Answer** From Formula 4.4.2, $U = (\Delta M)^2 / \Delta V \cdot \mathbb{E}[s^2]/\mathbb{E}[s]^2$, and $\mathbb{E}[s^2] \ge \mathbb{E}[s]^2$ with equality only when $\operatorname{Var}(s) = 0$. When effects vary, the variance among lines is dominated by the few mutations of large effect, so the method behaves as if there were fewer mutations of larger effect and underestimates $U$ (by a factor 2 for exponential effects, more for leptokurtic distributions such as a gamma with shape below 1). If all effects were equal, $(\Delta M)^2/\Delta V = U$ exactly and $\Delta V/\Delta M = s$.

3. Does an increase in mutation rate caused by stress (high temperature, starvation) contradict the statement that mutation is random? Does it increase the chance that a given mutation is adaptive, or the chance that a cell acquires an adaptive mutation?

   **Answer** No. Randomness in the evolutionary sense means that the mutations produced are not biased toward those that are favorable in the conditions; stress-induced mutagenesis increases the rate of mutations of all kinds, across large parts of the genome. It therefore does not increase the probability that any particular mutation is adaptive; most of the additional mutations are deleterious. It does increase the probability that a cell acquires some adaptive mutation, because more mutations of every kind occur, which is why such systems can be favored in populations under stress despite their cost (Section 4.4.4).

4. Two random human genomes differ at about one site in 1000. Using $\mu = 1.2 \times 10^{-8}$ per site per generation, estimate the effective population size, and explain why it is so much smaller than the present population.

   **Answer** Under neutrality $\pi = 4N_{\mathrm{e}}\mu$, so $N_{\mathrm{e}} = 0.001/(4 \times 1.2 \times 10^{-8}) \approx 21{,}000$. Diversity reflects the population size averaged over the hundreds of thousands of generations needed to build it up (the coalescence time is of order $4N_{\mathrm{e}}$ generations, [7.10.7](/7.10.7)), and this average is dominated by the small sizes of the ancestral population, including bottlenecks such as the expansion out of Africa; the enormous recent growth has not had time to increase diversity. $N_{\mathrm{e}}$ is in addition smaller than the census size because of variance in offspring number and other departures from the ideal population ([7.4.23](/7.4.23#def-23.5.2)).

5. (Open question) How would you test whether an inherited difference in flowering time between two plant populations is genetic, epigenetic or a maternal effect?

   **Answer** Outline: (i) grow plants from both populations in a common environment for several generations to remove direct environmental effects; (ii) make reciprocal crosses: a maternal effect makes $\mathrm{F}_1$ plants resemble their mother regardless of their own genotype, and disappears or segregates according to the mother's genotype in the next generation ([7.4.11](/7.4.11)); (iii) map the difference: a genetic difference segregates in an $\mathrm{F}_2$ in a Mendelian way and can be associated with sequence variants (QTL mapping, [7.4.25](/7.4.25)); (iv) look for an epiallele: compare methylation at candidate loci, test whether the difference is reversed by demethylating agents or erodes over generations, and check that it maps to a locus without any sequence difference.
