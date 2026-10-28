---
title: "Mutation: Kinds, Rates and Origins"
description: Mutation as the raw material and the tool of genetics; forward and reverse mutations; substitutions, insertions and deletions and their consequences in coding and noncoding DNA; loss- and gain-of-function alleles in Muller's classes and why they are dominant or recessive, with the poison-subunit calculation; the Luria–Delbrück fluctuation test, its distribution and the p0 method, and replica plating; mutation rates per gene, per base pair and per genome, and their measurement; trinucleotide repeat expansion and anticipation; mutagens, Muller's X-linked lethal test and the link between mutagens and carcinogens.
---

Every **allele** studied in the previous chapters arose by **mutation**, and almost every genetic analysis starts from **mutants**: Mendel's peas, Morgan's white-eyed fly and the **auxotrophs** of bacterial genetics ([7.4.10](/7.4.10)) are all variants that differ from the **wild type** at one **gene**. This chapter treats mutation as a genetic phenomenon. It asks three questions. What kinds of change occur in DNA, and what do they do to the product and to the **phenotype** of a **heterozygote**? How often do they occur, and how is a rate as small as $10^{-8}$ per **base pair** measured? And do **mutations** arise at random or in response to need? The chemistry of DNA damage and the repair systems that keep mutation rates low were described in [7.2.8](/7.2.8), and recombination in [7.2.9](/7.2.9); here we use their results. The next chapter turns the question around and uses collections of mutations to define what a gene is ([7.4.13](/7.4.13)); mutation in somatic cells returns in **cancer** genetics (7.4.21), and mutation as a force that changes allele frequencies, balanced by selection, in population genetics (7.4.23).

## 12.1. Mutation as a Tool of Genetic Analysis

**Definition 12.1.1 (Forward and Reverse Mutation)** A **forward mutation** changes a **wild-type** allele into a different (mutant) allele. A **reverse mutation** or **reversion** changes a mutant allele back to the wild-type sequence (true reversion) or to a sequence with wild-type function.

Forward mutation rates are almost always higher than reversion rates, often by one or two orders of magnitude. The reason is combinatorial: a gene can be inactivated by changes at hundreds of sites (any frameshift, any premature **stop codon**, many missense changes in essential **residues**), but a specific mutant can be restored only by a change at the mutant site or at a few compensating sites. In a classic yeast experiment, mutations in a gene needed for growth arose at rates of about $10^{-6}$ per gene per generation, while reversion of individual mutant alleles was at least ten times rarer, and some alleles (deletions) never reverted. This asymmetry is diagnostic: an allele that reverts is likely a point mutation, one that never reverts a deletion. Function can also be restored by a second mutation elsewhere, a **suppressor mutation** ([7.4.4](/7.4.4)), either in the same gene (an intragenic suppressor, such as a second frameshift that restores the **reading frame**) or in another gene (for example a **tRNA** that reads a premature stop **codon**).

## 12.2. Kinds of Mutation and Their Consequences

### 12.2.1. Changes in the DNA

Mutations are classified first by the change in the sequence: substitutions of one base pair for another, either **transitions** (purine to purine, pyrimidine to pyrimidine) or **transversions** (purine to pyrimidine or the reverse) ([7.2.8](/7.2.8#def-8.1.1)); insertions and deletions of one to many base pairs (indels); and larger changes, inversions, duplications and translocations, which are the subject of [7.4.15](/7.4.15). There are four transitions and eight **transversions**, yet transitions are about twice as common as transversions in human germline mutations, because the main spontaneous processes, cytosine **deamination**, especially of methylated CpG, and tautomeric mispairing, produce transitions.

**Definition 12.2.1 (Point Mutation)** A **point mutation** is a mutation that changes one or a few adjacent base pairs, a substitution or a small insertion or deletion, as opposed to a chromosomal rearrangement.

### 12.2.2. Consequences in Coding Sequences

**Definition 12.2.2 (Coding Mutations)** In a protein-coding sequence, a substitution is a **silent mutation** (*synonymous*) if the mutant **codon** specifies the same amino acid, a **missense mutation** if it specifies a different amino acid, and a **nonsense mutation** if it creates a **stop codon**, truncating the **protein**. A **frameshift mutation** is an insertion or deletion of a number of base pairs not divisible by three, which shifts the **reading frame** downstream of the mutation, changing all subsequent codons and usually creating a premature stop codon within a few dozen codons.

**Example 12.2.1 (Expected Classes of Random Substitutions)** Each of the 61 sense codons can change into 9 others by a single substitution, $61 \times 9 = 549$ possibilities. Enumerating them with the standard **genetic code** ([7.2.19](/7.2.19)) gives 134 synonymous ($24.4\,\%$), 392 missense ($71.4\,\%$) and 23 nonsense ($4.2\,\%$) changes. At third codon positions $126/183 = 69\,\%$ of substitutions are synonymous, which is why the third position evolves fastest. These are **expectations** for uniform mutation; real spectra are biased toward transitions and CpG sites. Similarly, if indel lengths were uniform, $2/3$ of them would cause frameshifts; in coding regions indels of multiples of three are overrepresented because frameshifts are removed by selection.

The converse of a nonsense mutation is a *nonstop mutation* (stop-loss), a substitution that changes the stop codon into a sense codon: **translation** continues into the 3′ untranslated region until the next in-frame stop codon, giving a longer protein, or, if there is none, the **mRNA** is degraded by nonstop decay. Hemoglobin Constant Spring, a common cause of α-thalassemia in Southeast Asia, carries the change UAA → CAA (Gln) in the stop codon of *HBA2*; its α-globin has 31 extra amino acids and is made in very small amounts because the mRNA is unstable. Of the 9 single-base changes of each of the three stop codons, 23 of the 27 give sense codons, and 4 give another stop codon.

Synonymous does not always mean neutral: a silent change can create or destroy a splice signal or alter translation speed. A mutation that has no effect on fitness is a *neutral mutation*; whether a mutation is neutral is a statement about selection, not about the protein, and most synonymous and many noncoding mutations are nearly neutral. Neutral mutations are the subject of the **neutral theory of molecular evolution** ([7.4.23](/7.4.23)). Missense mutations range from no effect to complete loss, depending on the residue; nonsense and frameshift mutations usually abolish function, partly because transcripts with premature stop codons are degraded by **nonsense-mediated decay**, though a stop codon near the end of a gene can leave a partially functional truncated protein.

### 12.2.3. Consequences outside Coding Sequences

Mutations outside the coding region act on the amount, timing or place of expression: changes in a **promoter** or an **enhancer** alter **transcription** ([7.2.12](/7.2.12), [7.2.14](/7.2.14)); changes in the **5′ splice site**, the **3′ splice site** or **branch point** cause **exon** skipping or **intron** retention ([7.2.16](/7.2.16)); changes in the ribosome-binding site, the 5′ or 3′ untranslated region or **polyadenylation signal** alter translation or mRNA stability. About $10\,\%$ of disease-causing variants in Mendelian disorders affect **splicing**, and most variants associated with common traits lie outside coding sequences (7.4.25).

## 12.3. Functional Classes of Mutant Alleles

### 12.3.1. Loss and Gain of Function

**Definition 12.3.1 (Loss- and Gain-of-Function Mutations)** A **loss-of-function mutation** reduces or abolishes the activity of a gene product. A **gain-of-function mutation** increases the activity of the product, or gives it a new activity, expression pattern or regulation.

H. J. Muller (1932) classified mutant alleles of *Drosophila* by comparing their **phenotypes** in different doses (**homozygous**, **heterozygous** with the wild type, and over a deletion of the gene). His terms are still used.

**Definition 12.3.2 (Muller's Classes)** A **null allele** (*amorph*) has no activity; a **hypomorph** has reduced activity of the normal kind; a **hypermorph** has increased activity of the normal kind; an **antimorph** or **dominant negative mutation** encodes a product that is inactive and also interferes with the wild-type product in the same cell; a **neomorph** has a new activity or is expressed at a new time or place. Amorphs and hypomorphs are loss-of-function alleles; hypermorphs and neomorphs are gain-of-function alleles; antimorphs are loss-of-function alleles that act dominantly.

The classes are defined by dosage tests. If $m$ is a hypomorph, $m/\mathrm{Df}$ (over a deletion) is more severe than $m/m$; if $m$ is an amorph, $m/m$ and $m/\mathrm{Df}$ are equally severe; adding a wild-type copy ($m/m/+$) restores a hypomorph or amorph, does not restore a hypermorph or neomorph, and only partly restores an antimorph, whose phenotype is made worse by adding more mutant copies and milder by adding wild-type copies.

![Muller's classes of mutant alleles on a scale of gene activity relative to the wild type (Definition 12.3.2). Amorphs (null alleles) have no activity, hypomorphs reduced activity and hypermorphs increased activity of the normal kind; antimorphs (dominant negative alleles) lower the activity of a heterozygote below that of a null heterozygote and are drawn below zero; neomorphs have a new function or ectopic expression and lie off the scale. The labels below the scale give the typical dominance relation in a heterozygote with the wild-type allele.](./plots/muller-morphs.py)

### 12.3.2. Why Most Loss-of-Function Alleles Are Recessive

A heterozygote for a null allele has half the gene dosage of the wild type. For most **enzymes** this makes no difference to the phenotype: flux through a **metabolic pathway** is shared among many enzymes and depends only weakly on any one of them (**metabolic control analysis** gives **flux control coefficients** that sum to 1 over the pathway, so a typical enzyme has a small one), and many genes are regulated so that a halved dosage is partly compensated. Wright (1934) and Kacser and Burns (1981) explained the general **recessive** character of loss-of-function alleles in this way. The exceptions are informative. **Haploinsufficiency** ([7.4.3](/7.4.3)) occurs when the product is rate limiting or acts in a dosage-sensitive way: transcription factors (*GLI3*, whose heterozygotes have extra digits in Greig cephalopolysyndactyly), structural proteins needed in large amounts, components that must be balanced with partners. Some loss-of-function alleles show **incomplete dominance** when the phenotype varies continuously with the amount of product, as for many pigment genes.

The absence of loss-of-function variants from a gene in large population samples is itself evidence of dosage sensitivity: in exome data from about 60 000 people, about 3000 human genes have far fewer predicted loss-of-function variants than expected from their mutation rates (Lek and colleagues 2016; refined with 140 000 **genomes** and exomes in gnomAD by Karczewski and colleagues 2020); these genes are enriched for **haploinsufficient** disease genes and for essential genes in **cell lines**.

### 12.3.3. Dominant Gain of Function and Dominant Negative Alleles

Gain-of-function alleles are usually **dominant**, because the wild-type allele cannot prevent the abnormal activity. In achondroplasia, the commonest form of dwarfism, almost all cases carry the same missense mutation (G380R) in *FGFR3*, the gene for a **receptor tyrosine kinase** that inhibits bone growth; the mutant **receptor** is active even without **ligand** (a hypermorph). The **dominant** allele of the *HTT* gene in Huntington disease is a neomorph: the expanded polyglutamine protein forms toxic aggregates (Section 12.6). The *Antennapedia* allele $Antp^{Ns}$ of *Drosophila* is a neomorph of the second kind: a regulatory rearrangement expresses the normal Antp protein in the head, where it transforms antennae into legs.

Dominant negative alleles arise most often in genes whose products act as **multimers**: the mutant **subunit** assembles with wild-type subunits and poisons the complex.

**Formula 12.3.1 (Poison-Subunit Model)** If a protein is a homo-oligomer of $n$ subunits, a fraction $f$ of the subunits in a cell are mutant, subunits assemble at random, and any mutant subunit inactivates the complex, then the fraction of active complexes is

$$
A = (1 - f)^{n}.
$$
In a heterozygote with equal expression of both alleles ($f = 1/2$), $A = (1/2)^n$, compared with $A = 1/2$ in a heterozygote for a null allele that makes no subunits.

**Example 12.3.1** For a tetramer, a heterozygote for a poison-subunit allele has $1/16 = 6.25\,\%$ active complexes, eight times fewer than a null heterozygote ($50\,\%$). The prediction explains why some missense alleles of the **tumor** suppressor p53, a tetrameric transcription factor, are dominant in cells, whereas truncating alleles act recessively (7.4.21), and why missense mutations in **collagen** I, a triple helix of two α1 and one α2 chains, cause more severe osteogenesis imperfecta than null alleles: a glycine substitution in α1 spoils $1 - (1/2)^2 = 3/4$ of the triple helices. Proteins that act as monomers ($n = 1$) cannot give dominant negative alleles by this mechanism.

![Dominant negative (poison-subunit) alleles in homo-oligomeric proteins (Formula 12.3.1). A: in a heterozygote with equal expression, the fraction of fully active complexes falls as (1/2)ⁿ with the number of subunits n (1/4 for dimers, 1/16 for tetramers), far below the 1/2 of a heterozygote for a null allele. B: fraction of active complexes against the fraction of mutant subunits for monomers, dimers, tetramers and hexamers; the dotted line marks equal expression.](./plots/dominant-negative.py)

Analysis of structures of thousands of human pathogenic missense variants supports the model: dominant negative mutations are strongly enriched at protein–protein interfaces of complexes (about $45\,\%$ of them lie at interfaces), whereas gain-of-function and **recessive** loss-of-function missense mutations show little interface enrichment (Gerasimavicius, Livesey and Marsh 2022). Because current pathogenicity predictors are trained largely on loss-of-function variants, many dominant negative and gain-of-function mutations are probably misclassified.

### 12.3.4. Classification by Phenotype

Muller's classes describe what a mutation does to gene activity. In practice mutants are first classified by the phenotype through which they are found, and the same mutation can belong to several classes.

| Class | Phenotype | Examples and remarks |
|---|---|---|
| Visible (morphological) | change in shape, size or color | *white* eyes and *vestigial* wings of *Drosophila*, dwarf peas |
| Lethal | death before reproductive age; dominant or recessive; acting in the gamete, zygote, embryo or later | yellow coat $A^{Y}$ of mice, lethal when homozygous (**lethal allele**, [7.4.3](/7.4.3)); **X-linked** lethals (Algorithm 12.7.1) |
| Reduced viability | graded by mortality: lethal (more than $90\,\%$ of carriers die), semilethal ($50$–$90\,\%$), subvital ($10$–$50\,\%$) | measured as the ratio of observed to expected mutant progeny (Question 16) |
| Conditional | mutant phenotype only under restrictive conditions | **temperature-sensitive alleles** (**conditional allele**, [7.4.3](/7.4.3)); the only way to study essential genes in **haploids** |
| Biochemical (nutritional) | loss of a metabolic function without visible change | **auxotrophs** such as $his^{-}$ ([7.4.10](/7.4.10)); **phenylketonuria** in humans |
| Resistance | growth in the presence of a drug, phage or toxin | streptomycin-resistant $str^{r}$ bacteria, phage-resistant $ton^{r}$ (Section 12.4) |
| Behavioral | change in a behavior | the *period* mutants of circadian rhythm ([7.4.13](/7.4.13#sec-13.4.2)) |

A loss-of-function allele that abolishes activity is a null allele (Definition 12.3.2); one that retains some activity is called *leaky* and is usually a hypomorph. Leaky and **conditional alleles** of essential genes are viable and therefore especially useful for analysis.

## 12.4. Mutations Arise at Random: The Fluctuation Test

### 12.4.1. The Question

When a culture of *E. coli* is exposed to bacteriophage T1, nearly all cells die, but a few survive and give rise to resistant colonies. Do the survivors acquire resistance because they meet the phage (the "induced" or adaptive hypothesis), or were they already resistant mutants that arose by chance during growth (the random-mutation hypothesis)? The two hypotheses predict the same average number of resistant cells. Salvador Luria and Max Delbrück (1943) realized that they predict different **variances**.

**Definition 12.4.1 (Fluctuation Test)** The **fluctuation test** compares the numbers of mutants among many small parallel cultures, each grown from a small inoculum to the same final size and then plated on selective medium, with the numbers among samples taken from one large culture. If mutations arise at random during growth, the parallel cultures show a **variance** far greater than the mean, with many cultures containing no mutants and a few containing very many ("jackpots") from mutations that happened early; samples from one culture show Poisson variation only.

### 12.4.2. The Models

Let a culture grow from $N_0$ to $N_t$ cells, so that about $N_t - N_0 \approx N_t$ cell divisions occur. Under the induced hypothesis, each of the $N_t$ cells becomes resistant on exposure with a small probability $a$, independently, so the number of resistant cells has a **Poisson distribution** with mean and variance $aN_t$. Under the random-mutation hypothesis, each division produces a mutant with probability $\mu$ (the mutation rate per cell division), and each mutant founds a clone that grows with the culture.

**Formula 12.4.1 (Luria–Delbrück Distribution)** In the random-mutation model, the number of mutational events in a culture is Poisson with mean $m = \mu N_t$ (the expected number of mutations). A mutation that occurs when the culture has $N$ cells produces a clone of about $N_t/N$ cells at the end (geometrically distributed with that mean in the Lea–Coulson model), and since mutations occur in proportion to the number of divisions, the value of $N$ at a mutation is uniformly distributed on $(N_0, N_t)$. The resulting distribution of the number $r$ of mutants per culture is the *Luria–Delbrück distribution*. Its properties:

$$
\mathbb{P}(r = 0) = \mathrm{e}^{-m}, \qquad \mathbb{E}[r] \approx m\ln\frac{N_t}{N_0}, \qquad \operatorname{Var}(r) \approx \frac{mN_t}{N_0} \gg \mathbb{E}[r].
$$
The tail is heavy, $\mathbb{P}(r \geq x) \approx m/x$ for large $x$, because a mutation in the first generations produces a clone comparable to the whole culture.

**Proof** Mutations are rare events among many divisions, so their number is Poisson with mean $\mu$ times the number of divisions, $\mu(N_t - N_0) \approx m$, and $\mathbb{P}(r = 0) = \mathbb{P}(\text{no mutation}) = \mathrm{e}^{-m}$. In deterministic exponential growth $N(s) = N_0\mathrm{e}^{s}$ (time measured in units of the inverse growth rate), mutations occur at rate $\mu\,\mathrm{d}N = \mu N_0\mathrm{e}^{s}\,\mathrm{d}s$, and one at time $s$ produces $\mathrm{e}^{t - s}$ mutant cells at time $t$; hence $\mathbb{E}[r] = \int_0^t \mu N_0\mathrm{e}^{s}\mathrm{e}^{t - s}\,\mathrm{d}s = \mu N_t t = m\ln(N_t/N_0)$. For the variance of a Poisson sum of clone sizes, $\operatorname{Var}(r) = \int_0^t \mu N_0\mathrm{e}^{s}\mathrm{e}^{2(t-s)}\,\mathrm{d}s \approx \mu N_t^2/N_0 = mN_t/N_0$, dominated by the earliest mutations. Finally, a clone exceeds $x$ cells if its mutation occurred while $N < N_t/x$, which has probability $(N_t/x)/N_t$ per mutation, so $\mathbb{P}(r \geq x) \approx m/x$. $\square$

The mean is therefore a poor **estimator** of $m$: it is dominated by rare jackpots and varies wildly between experiments. Three estimators are used instead.

**Algorithm 12.4.1 (Estimating the Mutation Rate from a Fluctuation Test)** From $C$ parallel cultures of final size $N_t$:

1. *p0 method* (Luria and Delbrück): if $C_0$ cultures have no mutants, $\hat m = -\ln(C_0/C)$. Accurate when $C_0/C$ is between about $0.1$ and $0.7$.
2. *Median method* (Lea and Coulson 1949): solve $\tilde r/m - \ln m = 1.24$ for $m$, where $\tilde r$ is the **median** number of mutants per culture.
3. *Maximum likelihood*: compute the Luria–Delbrück probabilities $p_r(m)$ by the recursion of Ma, Sandri and Sarkar (1992), $p_0 = \mathrm{e}^{-m}$, $p_r = \frac{m}{r}\sum_{k=0}^{r-1}\frac{p_k}{r - k + 1}$, and maximize $\sum_i \ln p_{r_i}(m)$ (**maximum likelihood estimation**, [3.2](/3.2)). This uses all the data and is the current standard.

Then $\hat\mu = \hat m/N_t$ mutations per cell division.

**Example 12.4.1** Twenty cultures of $2 \times 10^{8}$ cells; seven have no resistant mutants. Then $\hat m = -\ln(7/20) = 1.05$ and $\hat\mu = 1.05/(2 \times 10^{8}) = 5.2 \times 10^{-9}$ per cell division. If instead the median count were $10$, the median method gives $\hat m = 3.9$ (solving $10/m - \ln m = 1.24$) and $\hat\mu = 1.9 \times 10^{-8}$.

Luria and Delbrück observed exactly what the random-mutation model predicts: counts of T1-resistant bacteria in parallel cultures ranged from 0 to several hundred, with variances tens to hundreds of times the means, while samples from one culture had variances close to their means. Mutation to resistance had happened before selection. The same reasoning applies to **drug resistance** in tumors, where resistant cells are expected to be present before treatment whenever $\mu N \gtrsim 1$ ([7.3.26](/7.3.26)).

![The fluctuation test, simulated (Formula 12.4.1). Fifty parallel cultures grow from 1000 to 2 × 10⁸ cells. Under random mutation during growth (red), m = 1.2 mutations are expected per culture and each founds a clone of geometric size with mean N_t/N; under the induced hypothesis (blue), resistance arises only on exposure and the counts are Poisson with the same median. A: histogram of mutants per culture on logarithmic bins: random mutation gives many cultures without mutants, a long tail and a few jackpots of hundreds of cells. B: the fifty counts in rank order on a log scale (zero counts drawn at 0.5); the variance-to-mean ratio is about 1 for induced resistance and in the hundreds for random mutation.](./plots/fluctuation-test.py)

### 12.4.3. Replica Plating

**Definition 12.4.2 (Replica Plating)** **Replica plating** is the transfer of cells from every colony on a master plate to one or more other plates, preserving their positions, by pressing a sterile velvet pad first onto the master plate and then onto the new plates; it allows the same set of clones to be tested on several media.

Joshua and Esther Lederberg (1952) used it to show the random origin of resistance without any statistics. Colonies grown on a master plate without penicillin (or phage) were replica-plated onto several selective plates; resistant colonies appeared at the *same positions* on all replicas. Cells taken from the corresponding colonies on the master plate, which had never met the selective agent, were resistant, and by repeated selection of such colonies a pure resistant line could be isolated without exposure. Newcombe (1949) reached the same conclusion by spreading microcolonies: re-spreading cells on a plate before exposure to phage increased the number of resistant colonies, because the members of each pre-existing resistant clone were separated. Replica plating is also the standard method for finding auxotrophs (colonies that grow on complete but not on minimal medium; [7.4.10](/7.4.10)).

![Replica plating. A master plate without penicillin carries colonies, a few of which (red) consist of resistant cells. A velvet pad pressed on the master plate picks up cells from every colony and prints them, in the same arrangement, onto replica plates containing penicillin. Only resistant colonies grow on the replicas, and they appear at the same positions on all of them: the resistant cells were present on the master plate before any contact with penicillin.](./plots/replica-plating.py)

The fluctuation test and replica plating established that mutation is random with respect to the selective environment: it is not directed toward adaptive outcomes. This does not mean that mutation is uniform. Rates vary along the genome (hotspots, [7.4.13](/7.4.13)), with transcription, **replication** timing and **chromatin**, and with stress: in starving bacteria the **SOS response** and error-prone polymerases raise mutation rates genome-wide ([7.2.8](/7.2.8#sec-8.6)), so that more mutants appear under selection ("stress-induced mutagenesis"), but these mutations still occur without regard to which of them will be useful.

### 12.4.4. General Properties of Mutations

The results of this chapter can be collected into a short list of properties, each with its qualification.

| Property | Content | Qualification |
|---|---|---|
| Universality | mutations occur in all organisms and **viruses**, at every **locus** | rates differ by orders of magnitude (Section 12.5) |
| Randomness | which cell, gene and site mutates, and when, is not determined by the usefulness of the change (Section 12.4) | not uniform: hotspots, CpG sites, transcribed and late-replicating regions mutate faster |
| Lack of direction | a gene can mutate to many different alleles, the source of **multiple alleles** ([7.4.3](/7.4.3)) | the spectrum is biased toward transitions and loss of function |
| Reversibility | mutant alleles can revert (Definition 12.1.1) | forward rates exceed reverse rates; deletions do not revert |
| Recurrence | the same mutation arises independently again and again | new *white* alleles in fly stocks; nearly every case of achondroplasia is a new G380R change in *FGFR3* (Example 12.5.1) |
| Rarity | about $10^{-6}$–$10^{-5}$ per gene per gamete | high per genome: every human child carries about 70 new mutations |
| Mostly harmful, sometimes useful | most mutations with an effect lower fitness | the effect depends on the environment: semi-dwarf alleles that make stems short and stiff lower fitness in the wild but raise grain yield in fertilized fields (the *sd1* allele of rice and the *Rht* alleles of wheat of the Green Revolution) |

## 12.5. Mutation Rates and Their Measurement

**Definition 12.5.1 (Mutation Rate)** The **mutation rate** is the probability of a mutation per unit of DNA per unit of time: per gene (or per base pair, or per genome) per cell division in microorganisms and cell lines, or per gamete (per generation) in multicellular organisms. It is distinguished from the *mutant frequency*, the proportion of mutant cells in a population, which also depends on the history of growth and selection.

| Measure | Typical value |
|---|---|
| Spontaneous forward mutation, per gene per gamete (multicellular **eukaryotes**) | about $2$–$12 \times 10^{-6}$ on average; individual genes $10^{-9}$ to more than $10^{-3}$ |
| Per gene per cell division (bacteria, yeast) | about $10^{-8}$–$10^{-7}$ |
| Per base pair per replication (*E. coli*) | about $10^{-10}$ (after **proofreading** and **mismatch repair**) |
| Per genome per replication, DNA-based microbes | about $0.003$, remarkably constant (Drake's rule) |
| Human germline, per base pair per generation | about $1.2 \times 10^{-8}$ |
| Human germline, de novo mutations per child | about 60–70 single-nucleotide variants, a few indels, and about one new structural variant in every few children |
| RNA viruses, per base per replication | $10^{-6}$–$10^{-4}$ |

The human genome rate follows from the per base pair rate: $1.2 \times 10^{-8}$ per base pair per generation times the $6.2 \times 10^{9}$ base pairs of a **diploid** genome gives about 74 new mutations per child, in agreement with trio sequencing. Most fall in noncoding DNA; about 1–2 change amino acids.

Rates are measured in four ways. (1) *Fluctuation tests* in microorganisms and cells (Algorithm 12.4.1). (2) *Direct counting of new dominant phenotypes*: for a fully penetrant dominant condition, the number $n$ of affected children of unaffected parents among $B$ births gives $\hat\mu = n/(2B)$ per gene per gamete, because each child has received $2B$ gametes in all. (3) *Sequencing of parent–offspring trios* and of mutation-accumulation lines, which counts new mutations in whole genomes. (4) *Indirect estimates* from the equilibrium between mutation and selection, introduced by Haldane (1935) for hemophilia and treated in 7.4.23.

**Example 12.5.1 (Direct Estimate)** Suppose that among $242\,257$ births in a population, 7 children with achondroplasia had two unaffected parents. Then $\hat\mu = 7/(2 \times 242\,257) = 1.4 \times 10^{-5}$ per gene per gamete. This is an unusually high rate for a mutation at a single base pair (almost all cases are the same G380R change in *FGFR3*); it arises because spermatogonial **stem cells** carrying the mutation proliferate faster than others ("selfish selection" in the testis), so the mutation is enriched in sperm, strongly with paternal age.

**Definition 12.5.2 (Germline and Somatic Mutations)** A **germline mutation** arises in a cell of the germline (from the primordial germ cells to the gametes) and can be transmitted to offspring, in whom it is present in every cell. A **somatic mutation** arises in any other cell; it is passed to the descendants of that cell, forming a mutant clone (a **mosaic**), but not to offspring.

The distinction is sharp in animals, whose germline is set aside early in development, and blurred in plants, where flowers form late from the same shoot meristems as the rest of the plant. A somatic mutation in a shoot meristem can produce a *bud sport*, a branch with a new phenotype, which horticulturists propagate by grafting or cuttings; the navel orange and many red-skinned or early-ripening sports of apple, citrus and grape cultivars arose in this way. The shoot meristem of flowering plants has three cell layers (L1, L2, L3), each maintained by its own divisions, so a mutation in one layer gives a periclinal **chimera**; since the gametes descend from L2, only a mutation in L2 is transmitted through seed.

**Definition 12.5.3 (Paternal Age Effect)** The **paternal age effect** is the increase with the father's age at conception in the number of de novo mutations transmitted to a child, and in the incidence of disorders caused by them.

Germline mutation rates differ between the sexes. A human oocyte is the product of about 22 cell divisions, all completed before birth, whereas sperm produced at age 30 descend from about 400 successive divisions of spermatogonial stem cells (Crow 2000), which continue at about 23 per year. About $80\,\%$ of de novo point mutations are paternal in origin, and their number rises by about 1.5 per year of paternal age, compared with about 0.4 per year of maternal age (Jónsson and colleagues 2017; the data and fit are plotted in [7.2.8](/7.2.8#sec-8.8.2)). The maternal increase, in oocytes that do not divide, shows that damage, not only replication errors, contributes. Disorders caused by de novo mutations (achondroplasia, Apert syndrome, a fraction of autism and intellectual disability) correspondingly increase with paternal age.

## 12.6. Spontaneous Mutations and Repeat Expansion

### 12.6.1. Spontaneous Processes

Spontaneous mutations arise from the unavoidable chemistry of DNA and from errors of replication; their mechanisms and frequencies are described in [7.2.8](/7.2.8#sec-8.1), and the main points relevant here are summarized in the table.

| Process | Lesion or error | Typical mutation | Repair that limits it |
|---|---|---|---|
| **Depurination** | loss of a purine (**AP site**) | substitutions opposite the site | BER |
| **Deamination** | C → U; 5-methyl-C → T | G·C → A·T transitions, especially at CpG | BER (uracil glycosylase); T·G **mismatch repair** |
| Oxidation | 8-oxoguanine | G·C → T·A transversions | BER (OGG1, MUTYH) |
| Tautomeric shifts (**tautomerism**) | rare imino or enol forms pair wrongly | transitions | **proofreading**, mismatch repair |
| Misincorporation | wrong base inserted by polymerase | substitutions, about $10^{-5}$ before proofreading | proofreading ($100$-fold), mismatch repair ($100$–$1000$-fold) |
| Replication slippage in repeats | looped-out repeat units | small insertions and deletions in **microsatellites**; repeat expansions | mismatch repair |

Mismatch repair defects raise the mutation rate at **microsatellites** by $100$- to $1000$-fold, the microsatellite instability of Lynch syndrome tumors.

### 12.6.2. Trinucleotide Repeat Expansion and Anticipation

Repeats of three nucleotides in about 20 to more than 40 human genes are unstable: in transmission they change length, mostly by expansion, and long alleles cause disease.

**Definition 12.6.1 (Trinucleotide Repeat Expansion)** A **trinucleotide repeat expansion** is a mutation that increases the number of copies of a tandemly repeated trinucleotide (CAG, CGG, CTG, GAA and others) beyond the normal range; its probability, and the size of the change, increase with the length of the repeat. A **premutation** is an allele with a repeat length above the normal range but below the disease range, which does not cause the main disease but is unstable and likely to expand in the next generation.

**Definition 12.6.2 (Anticipation)** **Anticipation** is the tendency of an inherited disease to appear at an earlier age, with greater severity, in successive generations of a family; in repeat expansion disorders it is explained by the progressive expansion of the repeat.

The mechanism is slipped-strand mispairing during replication or repair: on a template of repeats, a strand slips and forms a **hairpin**, which mismatch repair proteins (MSH2–MSH3) stabilize and process into an expansion ([7.2.8](/7.2.8#sec-8.4)). Repeat diseases fall into two groups. In *polyglutamine diseases* (Huntington disease, several spinocerebellar ataxias), a CAG repeat in a coding region encodes an expanded glutamine tract; the protein misfolds and aggregates, a neomorphic and dominant effect ([7.1.6](/7.1.6)). In *noncoding repeat diseases*, the repeat lies in an untranslated region or intron: in fragile X syndrome a CGG expansion in the 5′ UTR of *FMR1* causes methylation of the **CpG island** and silencing (loss of function); in myotonic dystrophy type 1 a CTG repeat in the 3′ UTR of *DMPK* produces toxic RNA that sequesters splicing regulators; in Friedreich ataxia a GAA repeat in an intron reduces transcription of frataxin. Intronic and 3′ UTR expansions can also be translated without a **start codon** (repeat-associated non-AUG translation) into toxic repeat peptides.

| Disease (gene, repeat) | Normal | Premutation or intermediate | Disease | Expansion bias |
|---|---|---|---|---|
| Fragile X syndrome (*FMR1*, CGG, 5′ UTR) | 5–44 | 55–200 (45–54 intermediate) | > 200 (full mutation, methylated) | expansion to full mutation only through mothers |
| Huntington disease (*HTT*, CAG, coding) | ≤ 26 | 27–35 (intermediate); 36–39 (reduced **penetrance**) | ≥ 40 (full penetrance) | large expansions mostly through fathers |
| Myotonic dystrophy type 1 (*DMPK*, CTG, 3′ UTR) | 5–34 | 35–49 | ≥ 50; congenital form > 1000 | congenital form through mothers |

For fragile X, the probability that a mother's premutation expands to a full mutation in a child rises steeply with its length: a few percent for 55–59 repeats, roughly one third for 70–79, more than $80\,\%$ for 90–99 and nearly $100\,\%$ above 100 (Nolin and colleagues 2003); AGG interruptions within the repeat stabilize it. Premutation carriers have their own disorders (fragile X-associated tremor/ataxia in older men, primary ovarian insufficiency in about $20\,\%$ of women). The "Sherman paradox", that the risk of fragile X for relatives depends on their position in the **pedigree**, was resolved by the discovery of the dynamic mutation.

**Formula 12.6.1 (Age at Onset of Huntington Disease)** A parametric survival model fitted to about 2900 patients (Langbehn and colleagues 2004) gives the mean age at onset as a function of the number $c$ of CAG repeats on the expanded allele:

$$
\bar a(c) \approx 21.54 + \exp(9.556 - 0.146\,c)\ \text{years}, \qquad 41 \leq c \leq 56.
$$
For example $\bar a(42) = 52$, $\bar a(45) = 41$, $\bar a(50) = 31$ years. The repeat length explains about $60$–$70\,\%$ of the variance in age at onset; the rest depends on **modifier genes** (many in DNA repair, which affect somatic expansion) and environment.

![Trinucleotide repeat expansion in Huntington disease (Formula 12.6.1). A: repeat classes of the *HTT* CAG tract (normal up to 26, intermediate 27–35, reduced penetrance 36–39, full penetrance 40 or more) and the mean age at onset predicted by the Langbehn model over its range of validity: each additional repeat lowers the onset age, steeply at first. B: anticipation in simulated paternal lineages that start from 42 repeats and gain a random number of repeats (mean 4, illustrative) at each transmission through a father: the predicted onset age falls in each generation.](./plots/repeat-expansion.py)

## 12.7. Induced Mutations

### 12.7.1. Mutagens

**Definition 12.7.1 (Mutagen)** A **mutagen** is a physical or chemical agent that raises the frequency of mutations above the spontaneous rate. A **base analog** is a mutagen that resembles a normal base closely enough to be incorporated into DNA but pairs ambiguously; an **intercalating agent** is a flat polycyclic molecule that inserts between stacked base pairs and causes insertions and deletions of single base pairs during replication.

Mutagens differ in their specificity, which made them tools for analyzing the **genetic code** and mutation itself; the chemistry of each lesion is described in [7.2.8](/7.2.8#sec-8.1.2).

| Mutagen | Action | Main mutations |
|---|---|---|
| 5-Bromouracil (base analog of T) | its rare enol form pairs with G | A·T ↔ G·C transitions |
| 2-Aminopurine (base analog of A) | pairs with C as well as T | A·T ↔ G·C transitions |
| Nitrous acid | deaminates C to U, A to hypoxanthine | transitions in both directions |
| Hydroxylamine | hydroxylates C, which then pairs with A | G·C → A·T only |
| Ethyl methanesulfonate (EMS), *N*-ethyl-*N*-nitrosourea (ENU) | alkylate bases ($O^6$-ethylguanine pairs with T) | G·C → A·T (EMS); A·T changes too (ENU) |
| Proflavine, acridine orange, ICR-191 (intercalating agents) | stretch the helix | ±1 frameshifts |
| Ultraviolet light | **pyrimidine dimers** | C → T, CC → TT at dipyrimidines |
| X-rays, γ-rays | strand breaks, oxidized bases | deletions, rearrangements |
| Aflatoxin B1 (after metabolic activation) | bulky guanine adducts | G·C → T·A |

EMS and ENU are the standard mutagens of forward genetic screens in *Drosophila*, *C. elegans*, zebrafish and mice (7.4.19): at doses that give one mutation per gene in about every $10^3$ genomes they produce mostly point mutations, including hypomorphic and conditional alleles that deletions and insertions cannot give.

### 12.7.2. Muller's Test for X-Linked Lethals

Muller (1927) showed that X-rays cause mutations, the first proof that heredity can be changed experimentally (Nobel Prize 1946). He needed a quantitative test for new mutations anywhere on a **chromosome**, including the commonest kind, recessive lethals, which have no visible phenotype.

**Algorithm 12.7.1 (Detection of X-Linked Recessive Lethals in *Drosophila*)** 1. Irradiate wild-type males and cross them with females carrying a balancer X chromosome marked with the dominant mutation *Bar* (narrow eyes) and inversions that suppress crossing over (in Muller's original ClB chromosome, also a recessive lethal). 2. Each F1 daughter carries one treated paternal X and one *Bar* X. Mate each F1 female individually. 3. Among her sons, half receive the *Bar* X and half the treated X. If the treated X carries a recessive lethal anywhere, the non-*Bar* sons die: the cross produces only *Bar* sons. 4. The frequency of X-linked lethals is the fraction of F1 females that produce no non-*Bar* sons.

The test is a screen with a digital readout over about 1000 genes at once. Spontaneous X-linked lethals arise at about $0.1$–$0.2\,\%$ per X chromosome per generation; X-rays raise the frequency in proportion to the dose, by roughly $3\,\%$ per $1000\,\mathrm{R}$ in mature sperm, with no detectable threshold (Timoféeff-Ressovsky and colleagues, 1930s). The linear relation, expected if each mutation is caused by a single ionizing event, was the basis of the linear no-threshold model of radiation protection; the mega-mouse experiments of W. L. and L. B. Russell later showed that in mouse spermatogonia chronic exposure is less mutagenic than the same dose given acutely, because repair can act between hits.

### 12.7.3. Mutagens as Carcinogens

Most **carcinogens** are mutagens, often after metabolic activation by liver enzymes; the Ames test, which detects reversion of histidine auxotrophs of *Salmonella* in the presence of a liver extract, uses this correlation to screen chemicals ([7.2.8](/7.2.8#sec-8.7.1)). It is a reversion assay: tester strains carry a missense or a frameshift allele of a *his* gene, so that base-substitution mutagens and frameshift mutagens are detected by different strains, a direct application of the classes in Section 12.2.

### 12.7.4. Induced Mutations in Breeding

*Mutation breeding* is the use of induced mutations to create new variants of crops, ornamentals and industrial microorganisms. Seeds, pollen, buds or cultures are treated with γ-rays, X-rays, fast neutrons, ion beams or chemical mutagens (EMS, sodium azide), and the progeny are screened for improved traits; more than 3000 mutant cultivars of over 200 species have been officially released, among them semi-dwarf rice and barley and the deep-red 'Rio Red' grapefruit. In industrial microbiology, repeated rounds of X-ray, ultraviolet and chemical mutagenesis followed by selection raised the penicillin yield of *Penicillium chrysogenum* more than a thousand-fold from the strains of the 1940s. Induced mutations broaden the range of variants, including alleles that are absent from the cultivated gene pool, and can change one trait of an established variety while leaving the rest of its **genotype** intact.

Two features of the method follow from earlier sections. The dose is a compromise between mutation frequency and survival: the number of mutations rises in proportion to the dose (Section 12.7.2), but so do chromosome breaks and sterility, so plants are usually treated at the dose that reduces growth or survival by about half. And most induced mutations are recessive, while a treated seed or bud is a **chimera** of mutated and unmutated cells. The treated generation (M1) therefore shows almost no mutant phenotypes; they are found in the next generation (M2), after selfing has made a quarter of the progeny of a heterozygous sector homozygous. Today the induced mutations of a population of M2 plants can also be found directly by sequencing (TILLING), and targeted mutations are made by **genome editing** ([7.4.19](/7.4.19)).

## 12.8. Repair, Mutation and Disease: an Overview

Mutation rates are set by the balance between damage and replication errors on one side and repair on the other ([7.2.8](/7.2.8#sec-8.8.1)). Inherited defects of repair raise the mutation rate in somatic cells and cause cancer predisposition, usually through a germline loss-of-function allele and a second, somatic hit in the tumor (7.4.21).

| Repair process | Human disorder (gene) | Mutational consequence |
|---|---|---|
| **Nucleotide-excision repair** | xeroderma pigmentosum (*XPA*–*XPG*) | UV-induced C → T at dipyrimidines in skin |
| Mismatch repair | Lynch syndrome (*MLH1*, *MSH2*, *MSH6*, *PMS2*) | microsatellite instability, $100$–$1000$-fold more substitutions |
| **Homologous recombination** | hereditary breast and ovarian cancer (*BRCA1*, *BRCA2*) | deletions with microhomology, rearrangements |
| **Base-excision repair** | *MUTYH*-associated polyposis | G·C → T·A transversions |
| Polymerase proofreading | polymerase proofreading-associated polyposis (*POLE*, *POLD1*) | ultramutated tumors |

The full table, with the mechanisms, is in [7.2.8](/7.2.8#sec-8.7.2). Repair cannot be perfect, and it would not be favored if it were: the mutation rate of a species reflects the cost of fidelity and the limit set by genetic drift on selection for lower rates (the drift-barrier hypothesis of Lynch), and mutation is the ultimate source of all the genetic variation on which selection acts (7.4.23).

## Summary

| Topic | Key results |
|---|---|
| Direction (Definition 12.1.1) | forward rates exceed reversion rates (many ways to inactivate, few to restore); deletions do not revert; suppressors restore function at a second site |
| Kinds (Definitions 12.2.1, 12.2.2) | transitions about twice as common as transversions; random substitutions in codons: 24% synonymous, 71% missense, 4% nonsense (Example 12.2.1); frameshifts if indel length not divisible by 3; nonstop (stop-loss) mutations extend the protein (Hb Constant Spring); neutral mutations have no effect on fitness; noncoding mutations change expression or splicing |
| Function (Definitions 12.3.1, 12.3.2) | Muller's amorph, hypomorph, hypermorph, antimorph, neomorph, defined by dosage tests; loss of function usually recessive (excess capacity), except haploinsufficiency; gain of function and neomorphs dominant (*FGFR3* G380R, *HTT*, $Antp^{Ns}$) |
| Dominant negative (Formula 12.3.1) | active fraction $(1-f)^n$; heterozygote $(1/2)^n$, 1/16 for tetramers vs 1/2 for null; p53, collagen; enriched at interfaces |
| Phenotypic classes (12.3.4) | visible, lethal (lethal > 90 %, semilethal 50–90 %, subvital 10–50 % mortality), conditional, biochemical, resistance, behavioral; null vs leaky |
| Randomness (Definitions 12.4.1, 12.4.2; Formula 12.4.1; Algorithm 12.4.1) | Luria–Delbrück: $\mathbb{P}(r=0)=\mathrm{e}^{-m}$, heavy tail, variance ≫ mean; p0, median and ML estimators; $\hat\mu = \hat m/N_t$; replica plating and Newcombe's spreading |
| General properties (12.4.4) | universal, random (with hotspots), undirected (**multiple alleles**), reversible, recurrent, rare, mostly harmful but environment dependent (semi-dwarf cereals) |
| Rates (Definitions 12.5.1–12.5.3) | $10^{-6}$–$10^{-5}$ per gene per gamete; human $1.2\times10^{-8}$ per bp per generation, about 70 de novo mutations per child, 80% paternal, +1.5 per paternal year; direct estimate $n/(2B)$ (Example 12.5.1); bud sports and periclinal chimeras: only L2 mutations pass through seed |
| Spontaneous mutation and repeats (Definitions 12.6.1, 12.6.2; Formula 12.6.1) | deamination, **depurination**, oxidation, tautomers, slippage; fragile X (CGG > 200, expands through mothers), HD (CAG ≥ 40, onset falls with length), DM1; anticipation |
| Induced mutation (Definition 12.7.1, Algorithm 12.7.1) | base analogs, deaminating and alkylating agents, intercalators, UV, ionizing radiation, each with its spectrum; Muller's X-linked lethal test; linear dose response; mutagens as **carcinogens** (Ames test); mutation breeding: dose for about half survival, chimeric M1, recessive mutants found in M2 (12.7.4) |
| Repair and disease (12.8) | repair defects raise somatic mutation rates and cause cancer syndromes; mutation as the source of variation |

## Questions

1. A gene of 1200 coding base pairs is mutated by random single-base substitutions, uniformly over its sense codons. (a) What fraction of substitutions is expected to be nonsense? (b) Assume that the gene is inactivated by any nonsense mutation and by any missense change at 50 critical residues, and by nothing else. What fraction of all possible point substitutions inactivates it? (c) Why is the reversion rate of a nonsense allele so much lower than the forward rate?

   **Answer** (a) About $23/549 = 4.2\,\%$ (Example 12.2.1). (b) The gene has 400 codons and $400 \times 9 = 3600$ possible substitutions. Nonsense: $0.042 \times 3600 \approx 151$. At the 50 critical codons, about $0.714 \times 9 = 6.4$ of the 9 substitutions are missense, $50 \times 6.4 \approx 321$. Total $472/3600 \approx 13\,\%$. (c) Forward mutation can occur at any of about 150 nonsense sites and 320 missense sites (and by any frameshift), but reversion of one particular nonsense allele requires a change at that one codon (or a suppressor elsewhere): one or two specific substitutions out of 3600.

2. Explain why, for a protein that functions as a homodimer, a missense allele that produces a stable but inactive subunit can be dominant while a nonsense allele of the same gene is recessive. Calculate the active fraction of dimers in heterozygotes for each, and in a heterozygote in which the mutant allele is expressed at twice the level of the wild-type allele.

   **Answer** The stable mutant subunit assembles with wild-type subunits and inactivates the dimers it joins; the nonsense allele makes no subunit (or the mRNA is removed by **nonsense-mediated decay**), so the wild-type subunits form only active dimers. With equal expression: missense $(1 - 1/2)^2 = 1/4$ active; nonsense: all complexes active but only half as many, $1/2$ of wild-type activity. If the mutant is expressed twice as much, $f = 2/3$ and $(1/3)^2 = 1/9 \approx 11\,\%$ (Formula 12.3.1).

3. A hexameric **helicase** is encoded by one gene. How many-fold less activity does a heterozygote for a poison-subunit allele have than a heterozygote for a null allele (equal expression)? What fraction of mutant subunits would reduce activity to $10\,\%$?

   **Answer** $(1/2)^6 = 1/64$ versus $1/2$: 32-fold less. $(1 - f)^6 = 0.1$ gives $1 - f = 0.1^{1/6} = 0.681$, $f = 0.32$.

4. In a fluctuation test, 50 cultures each grow to $N_t = 5 \times 10^{8}$ cells; 18 contain no resistant mutants. Estimate $m$ and the mutation rate. How many cultures with no mutants would you expect if the rate were twice as high?

   **Answer** $\hat m = -\ln(18/50) = 1.02$; $\hat\mu = 1.02/(5 \times 10^{8}) = 2.0 \times 10^{-9}$ per cell division (Algorithm 12.4.1). With $m = 2.04$: $50\,\mathrm{e}^{-2.04} = 6.5$ cultures.

5. Under the induced hypothesis, the mean number of resistant cells per culture in Question 4 would be equal to its variance. Suppose that the observed counts have mean 25 and variance 4000. Which hypothesis do the data support, and why is the mean a poor estimate of $m$ under the other?

   **Answer** The variance-to-mean ratio is $160$, far above the value 1 expected for a Poisson count, as predicted by the random-mutation model, where early mutations produce jackpots and $\operatorname{Var}(r) \approx mN_t/N_0$ (Formula 12.4.1). The mean $\mathbb{E}[r] \approx m\ln(N_t/N_0)$ is dominated by rare large clones; in a finite sample it fluctuates widely and depends on $N_0$, so $m$ is estimated from the proportion of zeros, the median or by maximum **likelihood**.

6. Solve the Lea–Coulson median equation for $m$ when the median number of mutants in 30 cultures of $10^{8}$ cells is 5, and give the mutation rate.

   **Answer** $5/m - \ln m = 1.24$ gives $m \approx 2.38$ (by numerical solution: at $m = 2.38$, $2.10 - 0.87 = 1.23$). $\hat\mu = 2.38/10^{8} = 2.4 \times 10^{-8}$ per cell division.

7. In a newborn screening program, 12 infants with a fully penetrant dominant disorder are found among $500\,000$ births; 2 of them have an affected parent. Estimate the mutation rate per gene per gamete. What are the main sources of error?

   **Answer** New mutations: $10$; $\hat\mu = 10/(2 \times 500\,000) = 1.0 \times 10^{-5}$ (Example 12.5.1). Errors: incomplete penetrance or late onset in a parent (inflating new mutations), nonpaternity, **genetic heterogeneity** (several genes give the same phenotype, so the estimate is for all of them together), **phenocopies**, germline mosaicism in a parent, and reduced viability of affected fetuses (underestimation).

8. A child is born to a father aged 40 and a mother aged 30. Using about 1.5 additional paternal and 0.4 additional maternal de novo mutations per year of age, and taking about 50 paternal mutations at age 30 and 13 maternal at age 30, estimate the expected number of de novo point mutations in the child, and compare with a child of two 30-year-old parents. What fraction of the difference would you expect to affect protein sequences, if about $1.5\,\%$ of the genome is coding?

   **Answer** Paternal $50 + 1.5 \times 10 = 65$, maternal $13$: total about $78$, versus $63$; difference $15$ mutations. Coding fraction: $15 \times 0.015 \approx 0.2$ additional coding mutations, of which about $70\,\%$ missense or nonsense: roughly $0.16$ additional protein-altering mutations per child; small per child, but measurable in the incidence of de novo dominant disorders.

9. A woman carries an *FMR1* premutation of 85 CGG repeats. Her husband has a normal allele. (a) What is the probability that a son is affected by fragile X syndrome, if a premutation of this size expands to a full mutation in about $60\,\%$ of transmissions? (b) A daughter with a full mutation is affected less often and less severely than a son. Why? (c) Why does her brother, if he carries the same premutation, have no affected children?

   **Answer** (a) The son receives the premutation X with probability $1/2$; it expands with probability $0.6$; so $0.5 \times 0.6 = 0.30$. (b) A daughter with a full mutation has a normal *FMR1* on her other X; random **X-chromosome inactivation** leaves the normal allele active in a variable fraction of cells, so only about half of such girls have intellectual disability. (c) Expansion to the full mutation occurs essentially only in female transmission; a premutation transmitted by a man to his daughters remains a premutation (it may change a little), so they are carriers, and the risk appears in her children.

10. Using Formula 12.6.1, compute the predicted mean age at onset of Huntington disease for 43 and 48 CAG repeats. A father with 43 repeats transmits an allele with 48. By how many years is onset expected to be advanced?

    **Answer** $\bar a(43) = 21.54 + \exp(9.556 - 6.278) = 21.54 + \mathrm{e}^{3.278} = 21.54 + 26.5 = 48.1$ years; $\bar a(48) = 21.54 + \exp(9.556 - 7.008) = 21.54 + \mathrm{e}^{2.548} = 21.54 + 12.8 = 34.3$ years. Anticipation of about $14$ years in one generation (a mean; individual onsets vary by a decade or more).

11. In Muller's test, 2000 F1 females from irradiated fathers were mated individually, and 64 produced only *Bar* sons; in the control, 3 of 1000 did. (a) Estimate the induced X-linked lethal frequency. (b) If the X carries about 900 genes in which a lethal can occur, what is the induced lethal mutation rate per gene? (c) Why must the balancer suppress **crossing over**?

    **Answer** (a) Treated $64/2000 = 3.2\,\%$; spontaneous $0.3\,\%$; induced $\approx 2.9\,\%$ per X. (b) $0.029/900 \approx 3.2 \times 10^{-5}$ per gene per treated gamete. (c) In the F1 female, crossing over between the treated X and the balancer would separate a lethal from the treated chromosome or move it onto the *Bar* chromosome, so that the sons' phenotype would no longer report the state of the treated X (Algorithm 12.7.1).

12. Hydroxylamine causes only G·C → A·T transitions. A mutant induced by hydroxylamine is treated again with hydroxylamine, and also with 2-aminopurine. Which treatment can revert it, and what does reversion by an intercalating agent but not by base analogs indicate?

    **Answer** A G·C → A·T mutation can be reverted only by an A·T → G·C transition, which hydroxylamine cannot produce, but 2-aminopurine (which causes transitions in both directions) can. Reversion by an intercalating agent and not by base analogs indicates that the original mutation was a frameshift (reverted by a nearby compensating insertion or deletion), not a substitution; this logic was used by Crick, Brenner and colleagues to show that the code is read in triplets ([7.2.19](/7.2.19)).

13. (Open question) The fluctuation test shows that resistance mutations precede selection. Does this exclude any influence of the environment on mutation? Discuss stress-induced mutagenesis, transcription-associated mutation and CRISPR-based adaptive immunity in bacteria.

    **Answer** Outline: the test excludes *directed* mutation (an environment specifically inducing the useful mutation), not effects of the environment on the *rate*. Stress induces error-prone polymerases and the SOS response, raising mutation rates broadly, including in genes irrelevant to the stress; transcription increases mutation rates in transcribed genes (more single-stranded DNA, collisions), so induction of a gene can raise its own mutation rate somewhat, which looks partly "directed" but is not specific to useful changes. CRISPR–Cas immunity is a genuinely Lamarckian-looking process: bacteria acquire spacers from infecting phage DNA and transmit them to descendants; it is an acquired, heritable, specific adaptation, but it is a dedicated molecular system for recording foreign sequences, not mutation in the usual sense. The principle that mutation is random with respect to its fitness effects remains well supported.

14. A culture of *E. coli* is grown with a mutagen, and many independent mutants are sequenced in a $1000\,\mathrm{bp}$ region that originally contains $520$ G·C pairs. In total 10 mutations are found, all transitions, and the $(A+T)/(G+C)$ ratio of the region in the mutants is lower than in the wild type. (a) In which direction did the transitions go? (b) Which mutagens of the table in Section 12.7.1 fit, and which are excluded? (c) Compute the ratio before and after if all 10 had instead been G·C → A·T changes.

    **Answer** (a) A lower $(A+T)/(G+C)$ means G·C pairs were gained: A·T → G·C. (b) Base analogs (5-bromouracil, 2-aminopurine) and nitrous acid, which cause transitions in both directions, fit; hydroxylamine and EMS, which cause only G·C → A·T, and intercalating agents, which cause frameshifts, are excluded. (c) Before: $480/520 = 0.923$; after ten G·C → A·T changes: $490/510 = 0.961$.

15. (a) List the single-base substitutions of the stop codon UAA and classify them. (b) How many of the 27 single-base substitutions of the three stop codons are nonstop mutations? (c) Why is the α-globin of Hb Constant Spring 31 amino acids longer, rather than extending to the end of the mRNA?

    **Answer** (a) CAA (Gln), AAA (Lys), GAA (Glu), UUA (Leu), UCA (Ser), UAU and UAC (Tyr) are nonstop mutations; UGA and UAG keep a stop codon (they are "synonymous" for termination). (b) UAA gives 7 nonstop changes, UAG 8 and UGA 8: 23 of 27. (c) Translation continues in the same frame into the 3′ untranslated region and stops at the first in-frame stop codon there, 31 codons downstream of the mutated one.

16. A recessive mutation $m$ of *Drosophila* is suspected of lowering viability. Among 800 adult progeny of $m/+ \times m/+$ there are 90 $m/m$ flies. Estimate the relative viability of $m/m$ and classify the allele.

    **Answer** Without loss, $m/m : (\text{others}) = 1 : 3$. Observed $90 : 710$. Relative viability $= (90/710)/(1/3) = 0.38$, so about $62\,\%$ of $m/m$ zygotes die: a semilethal allele (mortality between $50$ and $90\,\%$; Section 12.3.4). Comparing with the other genotypes of the same cross, rather than with the total, corrects for any general loss of progeny.

17. In an EMS mutation-breeding program, each M1 plant carries a new recessive loss-of-function allele of a target gene in its germline with probability $10^{-3}$. (a) How many M1 plants are needed to have a $95\,\%$ chance that at least one carries such an allele? (b) An M1 plant carrying the allele is selfed. How many M2 plants of its family must be grown to see at least one homozygous mutant with probability $0.9$? (c) How does the answer to (b) change if the M1 plant is a chimera in which the mutant sector produced only half of the seeds?

    **Answer** (a) $1 - (1 - 10^{-3})^N \geq 0.95$ gives $N \geq \ln 0.05/\ln 0.999 = 2995$ plants. (b) Each M2 plant is homozygous with probability $1/4$: $1 - (3/4)^k \geq 0.9$ requires $k = 9$ ($1 - 0.75^8 = 0.89998$ falls just short; $1 - 0.75^9 = 0.925$). (c) The homozygote probability is $1/8$, and $1 - (7/8)^k \geq 0.9$ requires $k = 18$. Screening about $3000 \times 9 = 27\,000$ M2 plants is the scale of real forward screens; it is why mutant collections are pooled and why sequencing-based TILLING is used.

18. An apple tree produces a branch with red-skinned fruit on an otherwise green-fruited cultivar. (a) How can the new phenotype be propagated? (b) The red color proved to come from a dominant mutation present only in the L1 layer of the branch's meristem. Will seedlings from its fruit be red? (c) What if the mutation had been in L2?

    **Answer** (a) By grafting budwood of the branch onto rootstocks: vegetative propagation copies the meristem, layers and all. (b) No: the gametes descend from L2, which is not mutant, so the mutation is not transmitted through seed (the epidermis-derived skin color is a property of the chimera, not of its gametes). (c) The pollen and eggs of flowers on the branch would carry the dominant allele. Apples are self-incompatible, so the branch would be crossed with another cultivar, and half of the seedlings would inherit the allele and have red fruit.
