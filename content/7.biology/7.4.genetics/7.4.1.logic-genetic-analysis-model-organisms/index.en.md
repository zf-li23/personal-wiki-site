---
title: The Logic of Genetic Analysis and Model Organisms
description: What genetics studies and how it reasons from crosses to hidden genotypes; forward and reverse genetics and the logic of necessity, sufficiency and rescue; model organisms and how to choose one; ploidy and the three life cycles (zygotic, gametic and sporic meiosis); gene and allele nomenclature; a short history of genetics and the counting arguments that make it quantitative from the start.
---

Genetics is the science of heredity and variation: why offspring resemble their parents, why they also differ from them and from one another, and what the differences tell us about how organisms are built. Its characteristic method is indirect. A geneticist cannot see a **gene** in a pea plant or a fruit fly; what can be seen are phenotypes and their frequencies among the progeny of controlled crosses. From those frequencies one infers hidden genotypes, the number of genes involved, how their alleles interact and where the genes lie on **chromosomes**, and each inference can be tested with a further cross. Mendel in 1865 did exactly this, decades before anyone knew what a chromosome or DNA was, and the logic has not changed since: the counting is now done on DNA sequences of millions of people as well as on plants in a monastery garden, but the reasoning from observed ratios to unobserved genotypes is the same.

This course continues a single story. **Cell biology** ([7.3](/7.3)) described the machinery that copies chromosomes and distributes them at **mitosis** and **meiosis** ([7.3.21](/7.3.21)); genetics follows the consequences of that machinery for the transmission of traits, from one cross to whole populations; developmental biology ([7.5](/7.5)) uses the genetic methods introduced here to ask how one **genome** builds a whole organism. Molecular biology ([7.2](/7.2)) has already described what genes are made of and how they are expressed, so this course concentrates on what can be learned by perturbing genes and following their transmission. Because the observations are counts, almost every chapter has a calculation toolkit: the laws of probability and the χ² test (7.4.2), ratio modifications (7.4.4), Bayesian risk calculation in pedigrees (7.4.7), recombination frequencies and maps (7.4.8–7.4.9), **likelihoods** and LOD scores (7.4.14), allele-frequency dynamics (7.4.22–7.4.23) and variance components (7.4.24). The statistical tools themselves are developed in the statistics courses ([3.1](/3.1), [3.2](/3.2)) and are linked rather than re-derived. This chapter sets out the logic of genetic analysis, the organisms in which it is done, the life cycles that determine how genes are transmitted, the naming conventions and a short history.

## 1.1. What Genetics Studies

### 1.1.1. Three Levels of Analysis

Geneticists study the transmission of genetic information at three levels, and the subject is traditionally divided accordingly.

| Branch | Question | Typical data | Chapters |
|---|---|---|---|
| Transmission genetics | How are genes passed from parents to offspring? | phenotype counts in crosses and pedigrees | 7.4.2–7.4.11 |
| Molecular and developmental genetics | How does the information in DNA act within and between cells, and how is it changed? | mutant phenotypes, sequences, expression | 7.4.12–7.4.21 |
| Population, evolutionary and quantitative genetics | How do allele frequencies and heritable variation change over generations in a population? | allele frequencies, variances, genome-wide data | 7.4.22–7.4.25 |

The divisions are a convenience: the analysis of a human disease, for example, uses pedigrees (transmission), the identity of the mutated **gene** (molecular) and the frequency of the allele in the population (population genetics).

### 1.1.2. The Gene as a Unit Defined by Mutation and Segregation

Molecular biology defines a gene by its DNA: a region that is transcribed into a functional RNA together with the sequences that regulate it ([7.2.1](/7.2.1)). Classical genetics defined genes differently, and this operational definition is still the one used in every genetic screen: a gene is a unit that is identified because it can exist in alternative heritable forms, which segregate in crosses as Mendel's laws predict. A gene is first noticed when a heritable variant appears.

**Definition 1.1.1 (Wild Type and Mutant)** For a given property of an organism, the **wild type** is the form found most commonly in natural or standard laboratory populations, and the corresponding allele is the wild-type allele. A **mutant** is an individual, or a heritable variant form of the property, that differs from the wild type; the variant arises by **mutation**, a heritable change in the DNA.

"Wild type" is relative to a reference population. When two or more forms of a property are common in the same population (human ABO blood groups, for example), there is no single wild type; such genes are polymorphic (7.4.3).

The first step of genetic analysis is to decide whether a variant is heritable and how many genes are involved. Two examples show the reasoning, which the following chapters make systematic.

**Example 1.1.1** A fertile plant with white petals appears in a population with red petals. Crossed with a red plant, it gives only red-flowered progeny ($\mathrm{F}_1$); the $\mathrm{F}_1$ plants, self-fertilized, give 378 red-flowered and 122 white-flowered plants among 500. The ratio $378/122 \approx 3.1$ is close to 3:1, the ratio Mendel's law of segregation predicts for one gene with a dominant (red) and a recessive (white) allele (7.4.2): the expected numbers are $375$ and $125$, and the χ² statistic is

$$
\chi^2 = \frac{(378 - 375)^2}{375} + \frac{(122 - 125)^2}{125} = 0.024 + 0.072 = 0.096,
$$

far below the 5 % critical value $3.84$ for one degree of freedom. The white variant is therefore a recessive mutation in one gene, perhaps a gene for a pigment-synthesis **enzyme**; the cross alone cannot say which step is affected.

**Example 1.1.2** A short-winged fly crossed with a wild-type long-winged fly gives 788 progeny: 196 short-winged males, 194 short-winged females, 197 long-winged males and 201 long-winged females. About half the progeny are short-winged in both sexes. This is the 1:1 ratio expected if the short-winged parent is heterozygous for a dominant mutant allele $SH$ on an autosome ($SH/+ \times +/+$ gives $\tfrac12\, SH/+$ and $\tfrac12\, +/+$). The hypothesis predicts further ratios, which is how it is tested: two short-winged $\mathrm{F}_1$ flies crossed together should give $\tfrac14\, SH/SH$, $\tfrac12\, SH/+$, $\tfrac14\, +/+$, so 3/4 short-winged progeny if $SH/SH$ is viable, and 2/3 if it is lethal (7.4.3); two long-winged $\mathrm{F}_1$ flies should give only long-winged progeny. The mutation identifies a gene whose wild-type form is needed for normal wing development.

In both examples the genotypes are hidden and inferred from ratios, and the inference makes testable predictions. This is the core of genetic analysis.

## 1.2. Forward and Reverse Genetics

### 1.2.1. Two Directions of Inference

**Definition 1.2.1 (Forward and Reverse Genetics)** **Forward genetics** starts from a phenotype: one finds or induces mutants that show an altered phenotype, determines by crosses how many **genes** are involved, maps the **mutations** and identifies the responsible genes and DNA changes. **Reverse genetics** starts from a known gene or DNA sequence: one alters it deliberately (by a knockout, a point mutation, **RNA interference** or **genome editing**), observes the phenotype of the resulting mutant and infers the function of the normal gene product.

![Forward and reverse genetics. Forward genetics (top row) begins with a phenotype in natural variants or after random mutagenesis, screens for mutants, groups the mutations into genes by complementation, maps them by recombination and identifies the gene and the causal DNA change, which is confirmed by rescue. Reverse genetics (bottom row) begins with a gene known from its sequence, expression or homology, alters it in a targeted way, and characterizes the phenotype of the mutant. The two meet in a gene whose sequence and mutant phenotype are both known](./plots/forward-reverse-genetics.py)

The two approaches are complementary. Forward genetics makes no assumption about which genes matter, so it discovers genes nobody would have guessed; the price is that mapping and identifying the gene used to take years (now often weeks, by sequencing whole mutant **genomes**, 7.4.20). Reverse genetics was made routine by genome sequences, targeted mutagenesis in yeast and mice, **RNA interference** ([7.2.18](/7.2.18)) and **CRISPR–Cas9** ([7.2.24](/7.2.24)); its weakness is that a mutant may show no visible phenotype because other genes compensate (redundancy, 7.4.4) or because the relevant condition was not tested.

**Example 1.2.1 (Circadian rhythm, forward genetics)** Ronald Konopka and Seymour Benzer (1971) mutagenized *Drosophila* and screened for flies whose eclosion (emergence of adults from pupae) and locomotor activity were no longer rhythmic with a period of about 24 hours. They found three mutants, all mapping to one X-linked gene, *period*: $per^{s}$ (period about 19 h), $per^{l}$ (about 28 h) and $per^{0}$ (arrhythmic). Cloning *period* in the 1980s, and later *timeless* and others, revealed a transcriptional feedback loop in which the PER and TIM **proteins** repress their own genes with a delay that sets the period. Jeffrey Hall, Michael Rosbash and Michael Young received the 2017 Nobel Prize for this work. Nobody could have predicted the genes from the **biochemistry**; they were found because their mutant alleles changed a measurable behavior.

**Example 1.2.2 (A human trait, forward genetics without crosses)** Humans cannot be crossed, but a phenotype can still be the starting point. A genome-wide association study of attention-deficit hyperactivity disorder (Demontis and colleagues, 2023), comparing 38,691 affected individuals with 186,843 controls, found 27 regions of the genome in which some allele was significantly more common among the affected; these implicated 76 candidate genes, enriched among genes expressed in the early developing brain. Here the variants are natural and of small effect, and their identification uses statistics rather than controlled matings (7.4.25).

### 1.2.2. Necessity, Sufficiency and Rescue

A mutant phenotype is evidence about the normal function of a gene, and the type of experiment determines what kind of evidence it is.

| Experiment | What it shows | Example |
|---|---|---|
| Loss of function (null allele, knockout, knockdown) | the gene is necessary for the process | $per^{0}$ flies are arrhythmic |
| Gain of function (overexpression, expression in the wrong place or time) | the gene is sufficient, in that context, to drive the process | ectopic *eyeless* expression makes eyes on fly legs (7.5) |
| Rescue (a wild-type copy restores the phenotype) | the mutation in *this* gene, not a linked mutation elsewhere, causes the phenotype | a *per*$^{+}$ transgene restores rhythms in $per^{0}$ flies |

A mutagenized genome carries many mutations besides the one of interest, so a phenotype is attributed to a gene only after mapping places the mutation there and rescue (or an independent allele with the same phenotype) confirms it.

### 1.2.3. How Many Mutants Are Needed

Screens are probabilistic: each mutagenized genome or each random insertion hits a given gene with a small probability, and the question is how many must be examined.

**Formula 1.2.1 (Coverage of a Random Mutagenesis)** If each independent mutagenized genome (or insertion) hits a particular gene with probability $p$, the probability that at least one of $N$ independent genomes carries a hit in that gene is

$$
1 - (1 - p)^N \approx 1 - \mathrm{e}^{-Np},
$$

and the number needed to reach a probability $\gamma$ of at least one hit is

$$
N \ge \frac{\ln(1 - \gamma)}{\ln(1 - p)} \approx \frac{-\ln(1 - \gamma)}{p}.
$$

The approximation uses $\ln(1 - p) \approx -p$ for small $p$; the number of hits per gene is then approximately Poisson with mean $Np$ ([3.1.4](/3.1.4#sec-4.1.7)), and the expected fraction of genes not hit is $\mathrm{e}^{-Np}$.

**Example 1.2.3** Insertions of T-DNA into the *Arabidopsis* genome (about $1.35 \times 10^8$ bp) are approximately random. A gene with a 2 kb target region is hit by a given insertion with probability $p = 2000 / (1.35\times10^8) \approx 1.48\times10^{-5}$. For a 95 % chance of at least one insertion in the gene,

$$
N \ge \frac{-\ln 0.05}{1.48 \times 10^{-5}} = \frac{3.00}{1.48 \times 10^{-5}} \approx 2.0 \times 10^5
$$

independent insertion lines are needed. Public collections of several hundred thousand sequence-indexed insertion lines were built for this reason; even so, short genes and insertion "cold spots" remain unhit, and $\mathrm{e}^{-Np}$ never reaches zero.

## 1.3. Model Organisms

A **model organism** ([7.3.1](/7.3.1)) is studied intensively in the expectation that what is learned applies to others. For genetics the requirements are specific, because the method needs many generations and many progeny:

- small size and cheap maintenance, so that large populations can be kept;
- a short generation time, so that crosses over several generations take weeks rather than years;
- many progeny per mating, so that ratios can be measured precisely;
- easy and controlled mating (and, for plants and some animals, self-fertilization or inbred lines);
- a small, sequenced **genome** and a large set of genetic tools: mapped **mutations**, stock centers, **transformation**, targeted mutagenesis;
- conservation of **genes** and pathways with other organisms. Roughly two thirds of known human disease genes, and a similar or larger fraction of **cancer** genes, have recognizable counterparts in *Drosophila*, depending on the criteria used for similarity; the corresponding fractions in yeast are lower but still substantial, and most human genes have mouse **orthologs**.

| Organism | Generation time | Haploid genome (Mb) | Protein-coding genes | Haploid chromosome number $n$ | Phase of life cycle used for genetics | Characteristic tools |
|---|---|---|---|---|---|---|
| *Escherichia coli* | 20–30 min | 4.6 | ≈ 4 300 | 1 (circular) | haploid | conjugation, transduction (7.4.10), recombineering, deletion collection |
| Bacteriophages T4, λ | ≈ 30–60 min (one infection cycle) | 0.17 (T4), 0.049 (λ) | ≈ 300 (T4), ≈ 70 (λ) | 1 | haploid | plaque assays, fine-structure mapping (7.4.13) |
| *Saccharomyces cerevisiae* (budding yeast) | ≈ 90 min (mitotic); days for a full sexual cycle | 12 | ≈ 6 000 | 16 | haploid and diploid both stable | tetrads (7.4.9), gene replacement by homologous recombination, deletion collection |
| *Neurospora crassa* | ≈ 2–3 weeks (sexual cycle) | 41 | ≈ 10 000 | 7 | haploid | ordered tetrads, biochemical mutants (7.4.13) |
| *Arabidopsis thaliana* | 6–8 weeks | ≈ 135 | ≈ 27 000 | 5 | diploid sporophyte | self-fertilization, T-DNA insertion lines |
| *Zea mays* (maize) | 3–4 months | ≈ 2 300 | ≈ 40 000 | 10 | diploid sporophyte | cytogenetics, transposons (7.4.17), visible kernel traits |
| *Caenorhabditis elegans* | 3–4 days | 100 | ≈ 20 000 | 6 (XX hermaphrodite) | diploid | invariant cell lineage, RNAi by feeding, frozen stocks |
| *Drosophila melanogaster* | ≈ 10 days at 25 °C | ≈ 140 | ≈ 14 000 | 4 | diploid | balancer chromosomes, P elements, GAL4/UAS (7.4.19) |
| *Danio rerio* (zebrafish) | ≈ 3 months | ≈ 1 400 | ≈ 26 000 | 25 | diploid | transparent external embryos, large mutagenesis screens |
| *Mus musculus* (mouse) | ≈ 2–3 months | ≈ 2 700 | ≈ 20 000 | 20 | diploid | inbred strains, embryonic stem cells, knockouts |
| *Homo sapiens* (for comparison) | 20–30 years | ≈ 3 100 | ≈ 20 000 | 23 | diploid | pedigrees, population samples, sequencing |

![Model organisms of genetics arranged by generation time (horizontal axis) and haploid genome size (vertical axis), both on logarithmic scales. The organisms most used for classical transmission genetics combine short generation times with small genomes (lower left); vertebrates and maize have genomes a thousand times larger than bacteria and generation times measured in months; humans lie at the far right, which is why human genetics relies on pedigrees and population samples instead of crosses](./plots/model-organisms.py)

The choice depends on the question. Bacteria and phages give enormous numbers of individuals and allow selection for rare events (1 in $10^8$), which made them the organisms of molecular genetics. Yeast combines a eukaryotic cell with haploid genetics and easy gene replacement. *Drosophila* and *C. elegans* are the classical animals for genes of development and behavior, zebrafish for vertebrate development, and the mouse for mammalian physiology and disease models. Many questions, however, can only be asked in the organism in which the phenomenon occurs (pollinator behavior, the cognition of corvids, the odor of the corpse flower), and genome sequencing and **genome editing** have made genetic analysis possible in many non-model species.

## 1.4. Ploidy and Life Cycles

### 1.4.1. Haploid and Diploid

How **genes** are transmitted depends on how many copies of each **chromosome** a cell carries and on where in the life cycle **meiosis** occurs.

**Definition 1.4.1 (Ploidy)** A set of chromosomes containing one copy of each different chromosome of a species is a chromosome set; its number of chromosomes is the haploid number $n$. The **ploidy** of a cell is the number of chromosome sets it contains. A **haploid** cell or organism has one set ($n$ chromosomes); a **diploid** has two sets ($2n$), one from each parent, so that every chromosome except, in some species, the sex chromosomes is present as a pair of **homologues**. Cells with three or more sets are polyploid (triploid $3n$, tetraploid $4n$; 7.4.16).

Humans have $n = 23$: somatic cells are diploid with 46 chromosomes and gametes are haploid with 23. Ploidy counts chromosome sets, not DNA molecules: a diploid cell in G2 still has ploidy 2 although each chromosome consists of two sister chromatids. The amount of DNA is measured separately by the **C value** (7.4.5).

Ploidy determines how a **mutation** shows itself. In a haploid, each gene is present once, so every allele is expressed in the phenotype: there is no dominance, and the genotype can be read directly from the phenotype. In a diploid, a recessive allele can be carried hidden in a heterozygote, which is why diploids accumulate recessive mutations, why dominance (7.4.3) and the complementation test (7.4.4) exist, and why crosses must be designed to reveal recessive alleles (testcrosses, 7.4.2).

### 1.4.2. Three Places for Meiosis

Sexual reproduction alternates two events: fertilization, which doubles the ploidy, and meiosis, which halves it. Organisms differ in which phase lasts and grows.

**Definition 1.4.2 (Types of Life Cycle)** Eukaryotic life cycles are classified by the position of meiosis:

- **zygotic meiosis**: the zygote is the only diploid cell and undergoes meiosis at once; the organism lives as a haploid (many fungi such as *Neurospora*, green algae such as *Chlamydomonas*);
- **gametic meiosis**: meiosis produces the gametes directly, and all other cells are diploid (animals, many brown algae);
- **sporic meiosis**: meiosis produces haploid spores, which divide by **mitosis** into a multicellular haploid generation, the gametophyte, which later makes gametes by mitosis; fertilization gives the diploid sporophyte generation. The regular alternation of a multicellular diploid sporophyte and a multicellular haploid gametophyte is called **alternation of generations** (land plants and many algae).

Budding yeast is a special case: both haploid and diploid cells grow by mitosis indefinitely, and diploids undergo meiosis when starved.

![The three life cycles. Haploid phases (n) are shaded in one color and diploid phases (2n) in another; fertilization (F) doubles the ploidy and meiosis (M) halves it. Left: zygotic meiosis (*Chlamydomonas*, *Neurospora*), in which the zygote is the only diploid cell. Center: gametic meiosis (animals), in which the gametes are the only haploid cells. Right: sporic meiosis with alternation of generations (land plants), in which both phases are multicellular; in flowering plants the gametophyte is reduced to a few cells (the pollen grain and the embryo sac)](./plots/life-cycles.py)

The cell mechanics of meiosis are the same in all three cycles ([7.3.21](/7.3.21)); the consequences for genetic analysis differ.

| Life cycle | Genetic consequence | Used in |
|---|---|---|
| Zygotic meiosis | the products of a single meiosis can be recovered together as a tetrad and their genotypes read directly from haploid phenotypes | tetrad analysis in fungi (7.4.9) |
| Gametic meiosis | only one product of each female meiosis becomes the egg; the products of different meioses are mixed at random in the progeny, and genotypes are inferred from progeny ratios | most crosses in animals and pedigrees (7.4.2–7.4.8) |
| Sporic meiosis | mutations can be expressed and selected in the haploid gametophyte (pollen) as well as the diploid sporophyte; plants can often be self-fertilized | plant genetics, gametophytic self-incompatibility, pollen-lethal mutations |

Diploid cells in a haploid-dominant cycle, and haploid gametes in a diploid-dominant cycle, are reminders that "haploid organism" and "diploid organism" refer to the phase that lives and is studied, not to every cell.

## 1.5. Naming Genes and Alleles

Genetic nomenclature carries information about the **gene** and the allele in the typography itself, and every **model organism** community has its own rules. A few rules are general:

- gene names and symbols are written in italics (*lacZ*, *CDC28*, *white*); **proteins** are written in roman type (LacZ, Cdc28);
- the wild-type allele is marked with a superscript plus ($w^{+}$, or simply $+$ in a genotype); mutant alleles are distinguished by superscripts or numbers ($w^{1118}$, $cdc28\text{-}1$);
- in a genotype, the two alleles of a diploid at one locus are separated by a slash ($w^{+}/w^{1118}$, or $A/a$); genes on different **chromosomes** are separated by semicolons ($y;\,bw;\,st$), and genes on the same chromosome are listed in their order, with a slash between the two **homologues** ($th^{1}\,st^{2}/th^{2}\,st^{1}$); a single symbol means a homozygote unless heterozygosity is shown;
- sex chromosomes are written with capital roman letters (X, Y) and autosomes with numbers (1, 2, 21).

| Organism | Gene symbol | Wild-type and mutant alleles | Protein |
|---|---|---|---|
| Human | all capitals, italic: *HBB*, *CFTR*, *HTT* (the gene of Huntington disease) | variants named by their DNA or protein change, *CFTR* p.Phe508del | capitals, roman: CFTR |
| Mouse | first letter capital, italic: *Kit*, *Tyr* | superscripts: $Kit^{W}$, $Tyr^{c}$ (albino) | capitals: KIT, TYR |
| *Drosophila* | named after the phenotype of the first mutant allele found; lowercase if that allele was recessive (*white*, *w*; *wingless*, *wg*), capitalized if it was dominant (*Deformed*, $Dfd$; *Curly*, *Cy*) | superscripts: $w^{+}$, $w^{1}$, $w^{1118}$ | first letter capital: White, Wingless |
| *S. cerevisiae* | three letters and a number, capitals for the wild-type (dominant) allele: *CDC28*, *LEU2* | lowercase with an allele number for the mutant: $cdc28\text{-}1$, $leu2\text{-}3$; deletion $cdc28\Delta$ | first letter capital, often with p: Cdc28 (Cdc28p) |
| *E. coli* | three lowercase letters and a capital: *lacZ*, *recA*, *trpE* | $lacZ^{+}$, $lacZ^{-}$ or allele numbers; phenotypes in roman with superscript, Lac$^{+}$, Str$^{\mathrm{r}}$ | first letter capital: LacZ, RecA |
| *Arabidopsis* | capitals for the wild-type allele: *AGAMOUS* (*AG*) | lowercase for mutants, with numbers: $ag\text{-}1$ | capitals, roman: AG |

The *Drosophila* convention explains the strange names of many genes: a gene is named after what goes wrong when it is mutated, so *white* is required for red eye pigment and *wingless* for wing formation, not the other way round. This course writes Mendelian genotypes with single letters, a capital for the dominant and lowercase for the recessive allele ($A$ and $a$), and $A\_$ for "$AA$ or $Aa$" (a dominant phenotype whose second allele is unknown).

## 1.6. A Short History, and Why Genetics Is Quantitative

### 1.6.1. Milestones

![Milestones in the history of genetics, from Mendel's paper (1865, published 1866) and its rediscovery (1900), through the chromosome theory, linkage maps, one gene–one enzyme and the identification of DNA as the genetic material, to the double helix, the genetic code, recombinant DNA, the human genome, genome-wide association studies, genome editing and the first complete telomere-to-telomere human genome (2022). Events in the upper row concern transmission and mapping, those in the lower row molecular genetics and technology; the chapter where each is treated is given in parentheses](./plots/genetics-timeline.py)

| Year | Event | Chapter |
|---|---|---|
| 1865–1866 | Mendel presents and publishes his experiments on peas | 7.4.2 |
| 1900 | rediscovery of Mendel's work (de Vries, Correns, von Tschermak) | 7.4.2 |
| 1902–1903 | chromosome theory of inheritance (Sutton, Boveri) | 7.4.5 |
| 1905–1910 | linkage in sweet peas (Bateson, Punnett); X-linked *white* in *Drosophila* (Morgan) | 7.4.6, 7.4.8 |
| 1913 | first genetic map (Sturtevant) | 7.4.8 |
| 1918–1930 | synthesis of Mendelian and quantitative genetics (Fisher), population genetics (Fisher, Haldane, Wright) | 7.4.22–7.4.24 |
| 1927 | X-rays induce mutations (Muller) | 7.4.12 |
| 1941 | one gene–one enzyme (Beadle, Tatum) | 7.4.13 |
| 1943 | mutations arise before selection (Luria, Delbrück) | 7.4.12 |
| 1944, 1952 | DNA is the genetic material (Avery, MacLeod, McCarty; Hershey, Chase) | [7.2](/7.2) |
| 1946–1952 | recombination, conjugation and transduction in bacteria (Lederberg, Tatum, Zinder) | 7.4.10 |
| 1950 | transposable elements in maize (McClintock) | 7.4.17 |
| 1953 | double helix (Watson, Crick, using data of Franklin and Wilkins) | [7.2](/7.2) |
| 1955–1961 | fine structure of the gene (Benzer); genetic code is a triplet code (Crick, Brenner and colleagues; Nirenberg, Matthaei) | 7.4.13 |
| 1970s | recombinant DNA, DNA sequencing | [7.2.5](/7.2.5) |
| 1980s | positional cloning of disease genes; transgenic and knockout mice | 7.4.14, 7.4.19 |
| 1990–2003 | Human Genome Project | 7.4.14 |
| 2005–2007 | first genome-wide association studies | 7.4.25 |
| 2012 | CRISPR–Cas9 as a programmable nuclease | 7.4.19, [7.2.24](/7.2.24) |
| 2022 | complete telomere-to-telomere human genome | 7.4.14 |

The history is not finished. Mendelian transmission is settled, but the methods built on it keep changing what can be done: mapping now uses millions of markers, screens are run on whole **genomes** in cultured cells, and the genetics of complex traits, of genome evolution and of somatic **mutation** in **cancer** are active fields (7.4.21, 7.4.25).

### 1.6.2. Genetics Is a Counting Science

Mendel's decisive step was to count. Ratios such as 3:1 are statements about probabilities, and observed counts scatter around them as any random sample does; deciding whether a deviation is chance or a real departure from the hypothesis requires the statistical tools of [3.1](/3.1) and [3.2](/3.2). The simplest question is how large a family or progeny must be.

**Formula 1.6.1 (Sample Size to Observe a Class)** If each progeny independently belongs to a class with probability $p$, the probability that at least one of $n$ progeny does is $1 - (1-p)^n$. To observe the class with probability at least $\gamma$ one needs

$$
n \ge \frac{\ln(1 - \gamma)}{\ln(1 - p)}.
$$

**Example 1.6.1** How many $\mathrm{F}_2$ progeny of a monohybrid cross must be raised to see at least one recessive individual ($p = 1/4$) with probability 0.95? We need $1 - (3/4)^n \ge 0.95$, that is $(3/4)^n \le 0.05$ and

$$
n \ge \frac{\ln 0.05}{\ln 0.75} = \frac{-2.996}{-0.288} = 10.4,
$$

so $n = 11$ progeny ($(3/4)^{11} = 0.042$, while $(3/4)^{10} = 0.056$). For a class of probability $1/16$ (the double recessive of a dihybrid cross), $n \ge \ln 0.05 / \ln(15/16) = 46.4$, so 47 progeny are needed; for $1/64$ (three **genes**), 191.

The same reasoning, with the **binomial distribution** in place of a single trial, gives the probability of any number of progeny in a class, and it underlies the χ² test (7.4.2), the risk calculations of pedigrees (7.4.7) and the estimation of recombination frequencies (7.4.8). The following table lists the main tools of the course and where they appear.

| Tool | Used for | Chapter |
|---|---|---|
| product and sum rules, branch diagrams, binomial and multinomial probabilities | progeny of crosses with several genes | 7.4.2 |
| χ² goodness of fit | testing a ratio | 7.4.2, 7.4.4 |
| conditional probability | ratios with lethality; genotypes of individuals with a known phenotype | 7.4.2–7.4.4 |
| Bayes' theorem | carrier risk in pedigrees | 7.4.7 |
| recombination frequency, mapping functions, interference | genetic maps | 7.4.8, 7.4.9 |
| likelihood and LOD scores | linkage in human families | 7.4.14 |
| Hardy–Weinberg proportions, recurrence equations for allele frequencies | populations | 7.4.22, 7.4.23 |
| variance components and regression | heritability and response to selection | 7.4.24, 7.4.25 |

## Summary

- Genetics infers hidden genotypes from phenotype counts in crosses and tests each inference with further crosses (Examples 1.1.1, 1.1.2). It works at three levels: transmission, molecular–developmental and population–quantitative (1.1.1).
- A **gene** is identified genetically by heritable variants that segregate; **wild type** is the common form and a **mutant** a heritable variant (Definition 1.1.1).
- **Forward genetics** goes from phenotype to gene, **reverse genetics** from gene to phenotype (Definition 1.2.1). Loss of function shows necessity, gain of function sufficiency, and rescue establishes that a particular gene causes the phenotype (1.2.2).
- Random mutagenesis covers a gene with probability $1 - (1-p)^N \approx 1 - \mathrm{e}^{-Np}$; reaching probability $\gamma$ needs $N \approx -\ln(1-\gamma)/p$ **genomes** (Formula 1.2.1, Example 1.2.3).
- **Model organisms** combine short generation times, many progeny, controlled matings, small sequenced genomes and genetic tools (1.3).
- **Ploidy** counts **chromosome** sets: **haploid** $n$, **diploid** $2n$ (Definition 1.4.1). Haploids show every allele in the phenotype; diploids hide recessive alleles in heterozygotes.
- **Meiosis** can be zygotic (haploid organisms; **tetrads**), gametic (animals) or sporic (plants, with **alternation of generations**) (Definition 1.4.2).
- Gene names are italic and **proteins** roman; wild-type alleles carry a superscript $+$; each organism has its own conventions (1.5).
- Genetics is quantitative from the start: the number of progeny needed to observe a class of probability $p$ with probability $\gamma$ is $n \ge \ln(1-\gamma)/\ln(1-p)$, for example 11 for $p = 1/4$ (Formula 1.6.1, Example 1.6.1).

## Questions

1. Why does genetics need variants? Could Mendel's laws have been discovered in a population in which every plant had the same flower color?

   **Answer** No. **Genes** are detected through their alternative forms: transmission can only be followed when the parents differ at a gene, so that the offspring can be classified by which form they received. In a population without heritable variation every cross gives identical progeny and no ratio can be measured. This is why genetics starts from mutants and natural variants, and why a gene with no known variants is, to classical genetics, invisible.
2. Distinguish forward and reverse genetics, and explain why a reverse-genetic knockout without a visible phenotype does not prove that the gene has no function.

   **Answer** Forward genetics starts from a phenotype and searches for the genes whose **mutation** alters it; reverse genetics starts from a gene and asks what phenotype its mutation causes (Definition 1.2.1). A knockout may show no phenotype because another gene with an overlapping function compensates (redundancy, 7.4.4), because the gene acts only under conditions that were not tested (another temperature, diet, pathogen, stress, or a quantitative trait that was not measured), or because the effect is too small to see in a few individuals. Absence of a phenotype is therefore weak evidence; double mutants, sensitized backgrounds and more conditions are needed.
3. A mutagenesis screen in a haploid yeast recovers a temperature-sensitive mutant that does not grow at 37 °C. List the experiments that would establish which gene is responsible.

   **Answer** (1) Backcross the mutant to wild type and sporulate the diploid: a 2:2 segregation of growth and no growth among the four spores of each **tetrad** shows that a single nuclear mutation causes the phenotype (7.4.9). (2) Test complementation with known temperature-sensitive mutants (7.4.4) to see whether it is a new gene. (3) Map the mutation, or sequence the whole **genome** of the mutant and of segregants, to find the candidate DNA change. (4) Rescue: transform the mutant with a **plasmid** carrying the wild-type candidate gene and show that growth at 37 °C is restored (in yeast, also by complementation with a **genomic library**). Rescue by one gene, together with linkage of the phenotype to the mutation, identifies the responsible gene.
4. Give two reasons why *Drosophila* and *C. elegans* were chosen for genetic studies of development and behavior, and two reasons why the mouse is used despite its long generation time.

   **Answer** *Drosophila* and *C. elegans* have short generation times (about 10 and 3–4 days), many progeny, cheap maintenance and powerful tools (balancers and P elements in flies, an invariant cell lineage, **RNAi** by feeding and frozen stocks in worms); their genes and developmental pathways are conserved with vertebrates. The mouse is a mammal: its physiology, immune system and diseases are close to those of humans, and inbred strains, **embryonic stem cells** and knockout technology make reverse genetics in a mammal possible.
5. Explain why a recessive loss-of-function mutation is seen immediately in a haploid but can be carried unseen in a diploid. What does this imply for the frequency of recessive deleterious alleles in diploid populations?

   **Answer** A haploid has one copy of each gene, so the mutant allele alone determines the phenotype. A diploid heterozygote has a wild-type allele as well, which usually provides enough function (7.4.3), so the mutation is hidden. In diploid populations recessive deleterious alleles are exposed to selection only in homozygotes, which are rare when the allele is rare; such alleles therefore persist, mostly in heterozygous carriers (7.4.22, 7.4.23), and every human carries some.
6. In Example 1.1.1, suppose instead that the $\mathrm{F}_2$ had contained 340 red and 160 white plants. Test the 3:1 hypothesis with the χ² test at the 5 % level.

   **Answer** Expected numbers are 375 and 125. $\chi^2 = (340-375)^2/375 + (160-125)^2/125 = 3.27 + 9.80 = 13.07$. With one degree of freedom the 5 % critical value is 3.84 (the **p-value** is about $3\times10^{-4}$), so the 3:1 hypothesis is rejected. Possible explanations include reduced viability of red plants, more than one gene, or misclassification; they would be tested with further crosses.
7. In Example 1.1.2, the 788 progeny contained 390 short-winged and 398 long-winged flies. (a) Test the 1:1 hypothesis. (b) If two short-winged progeny are crossed and the mutation is lethal when homozygous, what fraction of their progeny is short-winged?

   **Answer** (a) Expected 394 each; $\chi^2 = 2 \times (4^2/394) = 0.081$, far below 3.84; the data agree with 1:1. (b) $SH/+ \times SH/+$ gives $\tfrac14\, SH/SH$ (dies), $\tfrac12\, SH/+$ and $\tfrac14\, +/+$; among the survivors the short-winged fraction is $\dfrac{1/2}{1/2 + 1/4} = 2/3$.
8. How many $\mathrm{F}_2$ progeny of a trihybrid cross $AaBbCc \times AaBbCc$ must be raised to observe at least one $aabbcc$ individual with probability 0.99?

   **Answer** $p = (1/4)^3 = 1/64$. $n \ge \ln 0.01 / \ln(63/64) = -4.605 / -0.01575 = 292.4$, so $n = 293$.
9. An EMS screen in *Drosophila* induces, on average, a mutation in a given gene in one of every 1 000 mutagenized X **chromosomes** ($p = 10^{-3}$). (a) How many chromosomes must be screened to recover at least one mutation in that gene with probability 0.95? (b) If 3 000 chromosomes are screened, what is the expected number of mutations recovered in the gene and the probability of recovering none?

   **Answer** (a) $N \ge \ln 0.05 / \ln(0.999) = 2.996 / 0.0010005 = 2994.3$, so 2 995 chromosomes. (b) The number of hits is approximately Poisson with mean $Np = 3$ (Formula 1.2.1); $\mathbb{P}(0) = \mathrm{e}^{-3} = 0.050$ (exactly $0.999^{3000} = 0.0497$).
10. A collection of $2\times10^5$ random insertion lines is made in a genome of $1.35\times10^8$ bp. (a) What fraction of genes with a 1 kb target is expected to carry no insertion? (b) With a 3 kb target? (c) What does this imply about screens that rely on such collections?

    **Answer** (a) $Np = 2\times10^5 \times 1000/1.35\times10^8 = 1.48$; the fraction without an insertion is $\mathrm{e}^{-1.48} = 0.23$. (b) $Np = 4.44$, $\mathrm{e}^{-4.44} = 0.012$. (c) Small genes are underrepresented, so a collection of this size misses about a quarter of 1 kb genes even if insertion is perfectly random (and insertion hotspots make it worse); absence of a mutant in a collection does not mean the gene is dispensable, and saturation requires either much larger collections or targeted mutagenesis.
11. A diploid species has $2n = 14$. How many chromosomes, and how many chromatids, are present in (a) a somatic cell in G1, (b) a somatic cell in G2, (c) a gamete? What is the ploidy in each case?

    **Answer** (a) 14 chromosomes, 14 chromatids (each chromosome is one DNA molecule), ploidy 2. (b) 14 chromosomes, each of two sister chromatids, 28 chromatids, ploidy still 2. (c) 7 chromosomes, 7 chromatids, ploidy 1. Ploidy counts chromosome sets, not DNA molecules (Definition 1.4.1).
12. In which type of life cycle can the four products of a single **meiosis** be recovered together and their genotypes read directly? Explain why this is useful.

    **Answer** In zygotic meiosis (fungi such as *Neurospora* and yeast, algae such as *Chlamydomonas*), the four haploid products remain together in an ascus or a zygospore and grow into haploid colonies whose phenotypes show their genotypes directly. Tetrad analysis (7.4.9) therefore sees every product of one meiosis, which allows the 2:2 segregation of a gene to be verified in each meiosis, gene–**centromere** distances to be measured and events such as gene conversion to be detected; in animals only one random product of each meiosis is sampled.
13. Write, using standard conventions, (a) the human gene for the cystic fibrosis transmembrane conductance regulator and its **protein**; (b) a yeast strain carrying the first temperature-sensitive allele of *CDC28*; (c) a *Drosophila* female heterozygous for a mutant *white* allele $w^{1}$ and for the dominant *Curly* mutation on chromosome 2.

    **Answer** (a) Gene *CFTR*, protein CFTR. (b) $cdc28\text{-}1$ (genotype *cdc28-1*; the wild-type allele is *CDC28*). (c) $w^{1}/w^{+};\, Cy/+$: the X-linked locus first, a semicolon, then the second chromosome.
