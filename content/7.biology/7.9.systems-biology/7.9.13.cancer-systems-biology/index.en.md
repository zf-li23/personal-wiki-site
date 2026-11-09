---
title: Cancer Systems Biology
description: "Cancer as a disease of networks studied with the methods of the course: the hallmarks and the convergence of many mutations on few pathways; the cancer genome (classes of alteration, allele-specific copy number from depth ratios and B-allele fractions, purity, ploidy and cancer cell fractions, consortia and portals); mutational signatures (the 96 substitution classes, non-negative matrix factorization, refitting, aristolochic acid); drivers and passengers (background mutation rates and their covariates, recurrence tests, dN/dS, hotspots and the 20/20 rule, power); network-based driver inference (CNV–expression integration, ceRNA networks, mutated subnetworks, network-based stratification, phosphorylation-site mutations); molecular subtypes, classifiers, selection bias and prognostic signatures; dependencies, synthetic lethality, tumor mutational burden and immunotherapy."
---

Cancer is the disease in which the methods of systems biology have been used most. A tumor is a population of cells that has escaped the controls of a tissue through somatic mutations and epigenetic changes ([7.3.26](/7.3.26), [7.4.21](/7.4.21)); every tumor is different, yet tumors of a type share pathways, phenotypes and vulnerabilities. Large consortia have measured the genomes, transcriptomes, methylomes and proteomes of tens of thousands of tumors, and cell-line collections have measured how thousands of cancer cells respond to the loss of each gene and to hundreds of drugs. Turning these data into understanding requires most of what the earlier chapters developed: count models and multiple testing, matrix factorization, regulatory and interaction networks, network propagation, and the statistics of prediction and survival.

This chapter follows the questions in order. What kinds of alteration does a cancer genome carry, and how are they measured (13.2)? What do the patterns of mutations say about their causes (13.3)? Which alterations drive the tumor and which are passengers (13.4)? How do networks turn long lists of rare mutations into a few altered pathways (13.5)? How are tumors classified, and how can classifiers and prognostic signatures mislead (13.6)? And which dependencies of a tumor can be exploited by treatment (13.7)? The biology of cancer cells (the hallmarks, oncogenes and tumor suppressors, invasion, the immune response) is in [7.3.26](/7.3.26), the genetics (clonality, Knudson's model, hereditary cancer) in [7.4.21](/7.4.21), the detection of somatic variants from reads in [7.8.12](/7.8.12#sec-12.7), and the methods of survival analysis in [7.7.16](/7.7.16); this chapter uses them without repeating them.

## 13.1. Cancer as a Disease of Networks

The **hallmarks of cancer** summarize what a tumor cell must acquire: sustained proliferative signaling, evasion of growth suppressors, resistance to cell death, replicative immortality, angiogenesis, invasion and metastasis (Hanahan and Weinberg, 2000), with the reprogramming of energy metabolism and evasion of immune destruction added later, enabled by genome instability and tumor-promoting inflammation (2011), and more recently phenotypic plasticity, nonmutational epigenetic reprogramming, polymorphic microbiomes and senescent cells (Hanahan, 2022) ([7.3.26](/7.3.26#sec-26.5.2)). The hallmarks are capabilities of a system, not of a gene: each is produced by a network of signaling, regulation and metabolism, and each can be reached by alterations of many different genes.

This is the central observation of cancer genomics. Analyses of the first thousands of sequenced tumors classified about $140$ genes that drive tumorigenesis when mutated into $12$ signaling pathways, which in turn regulate three core cellular processes, cell fate, cell survival and genome maintenance (Vogelstein and colleagues, 2013). A typical solid tumor carries a few driver mutations, and two tumors of the same type often share none of them, yet their drivers hit the same pathways, frequently in a mutually exclusive way: tumors with an activating *KRAS* mutation rarely also carry an activating *BRAF* mutation, because one hit in the pathway suffices. Three questions follow (and organize this chapter): which of the many mutations in a tumor are drivers rather than **passenger mutations**; how the effect of a driver is transmitted and amplified through networks to produce the phenotype; and how the altered networks might be pushed back by treatment.

A tumor is also an evolving population and an ecosystem. **Clonal evolution** ([7.3.26](/7.3.26#sec-26.2.3)) makes it a mixture of subclones that differ in their mutations, with a phylogeny that can be reconstructed from the allele fractions of the mutations (13.2.3) and that changes under treatment, the subject of the evolution of drug resistance ([7.6.41](/7.6.41#sec-41.5)). The tumor microenvironment, fibroblasts, endothelial cells and immune cells that make up much of a tumor's mass, shapes growth and response to therapy; its composition is estimated from bulk expression by **cell-type deconvolution** ([7.9.5](/7.9.5#sec-5.7)) and mapped in place by spatial omics ([7.9.6](/7.9.6#sec-6.11.3)).

## 13.2. The Cancer Genome

### 13.2.1. Classes of Alteration

| Alteration | Size | Typical consequence | Detection from sequencing |
|---|---|---|---|
| single-nucleotide variant (SNV) | 1 bp | missense hotspot (oncogene) or truncation (tumor suppressor) | tumor–normal comparison of pileups ([7.8.12](/7.8.12#sec-12.7)) |
| small insertion or deletion (**indel**) | < 50 bp | **frameshift mutation**, often in **microsatellites** after loss of **mismatch repair** | local realignment and assembly |
| copy-number alteration | kb to whole chromosomes | amplification of oncogenes (*ERBB2*, *MYC*), homozygous deletion of suppressors (*CDKN2A*) | read depth and allele fractions (13.2.2) |
| **structural variant** | rearrangement | gene fusions (*BCR*–*ABL1*, *TMPRSS2*–*ERG*), enhancer hijacking | discordant pairs and split reads ([7.8.12](/7.8.12#sec-12.6)) |
| complex events | one or a few chromosomes | chromothripsis (shattering and random reassembly of a chromosome in one event), kataegis (clusters of substitutions near rearrangements) | patterns of breakpoints and copy-number oscillations |
| **whole-genome duplication** | genome | tolerance of further aneuploidy | ploidy estimation (13.2.2) |
| epigenetic change | gene to genome | silencing of suppressors by promoter methylation (*MLH1*, *CDKN2A*) | methylation arrays and bisulfite sequencing ([7.9.8](/7.9.8#sec-8.5)) |

Mutations are detected by comparing a tumor with normal tissue of the same patient: variants present in both are inherited, variants present only in the tumor are somatic. Whole-genome sequencing sees all classes; exome and targeted panels see coding SNVs and indels well and copy number less well. The first leukemia genome sequenced in this way already showed that most of the recurrent somatic mutations lay in genes that no one would have chosen as candidates (Ley and colleagues, 2008), the reason for unbiased sequencing.

### 13.2.2. Allele-Specific Copy Number, Purity and Ploidy

A tumor sample is a mixture of tumor cells and normal cells, and tumor cells are often far from diploid. Two signals measure copy number at heterozygous SNPs: the depth of the tumor relative to the normal (the log ratio, logR) and the fraction of reads carrying one of the two alleles (the B-allele fraction, BAF).

**Definition 13.2.1 (Purity, Ploidy and Allele-Specific Copy Number)** In a tumor sample, the *tumor purity* $\rho$ is the fraction of cells that are tumor cells, and the *tumor ploidy* $\psi$ is the average total copy number of the tumor genome. At a locus, the *allele-specific copy number* $(n_A, n_B)$ is the number of copies of each parental allele in the tumor cells, with total $n = n_A + n_B$.

**Formula 13.2.1 (Expected Log Ratio and B-Allele Fraction)** If normal cells are diploid with one copy of each allele, then at a heterozygous SNP in a segment with state $(n_A, n_B)$ (Van Loo and colleagues, 2010)
$$
\mathrm{logR} = \gamma\log_2\frac{2(1 - \rho) + \rho n}{2(1 - \rho) + \rho\psi}, \qquad \mathrm{BAF} = \frac{1 - \rho + \rho n_B}{2(1 - \rho) + \rho n} \ \text{ or its mirror } 1 - \mathrm{BAF},
$$
where $\gamma \le 1$ accounts for the compression of the signal by the platform ($\gamma = 1$ for sequencing).

**Proof** A cell population of which a fraction $\rho$ has $n$ copies and $1 - \rho$ has $2$ contributes DNA in proportion to $2(1 - \rho) + \rho n$ at the locus, against $2(1 - \rho) + \rho\psi$ on average over the genome, to which sequencing depth is normalized. Of the copies, $1 - \rho + \rho n_B$ carry allele B; which allele is called B depends on the SNP, so the observed fractions split into two mirror bands. $\square$

![Allele-specific copy number from tumor sequencing (simulation). Six segments carry the states (major, minor) = (1, 1), (2, 1), (1, 0), (2, 0), (2, 2) and (3, 1) in a sample of purity 0.7; 500 heterozygous SNPs per segment are sequenced at a depth of 60. A: log ratio of tumor to normal depth with segment means (red). B: B-allele fraction of the heterozygous SNPs, split into two mirror bands; copy-neutral loss of heterozygosity (2, 0) is visible here but not in A. C: fit of purity and ploidy: for each pair (ρ, ψ), every segment is assigned its nearest integer state and the distance of the observed segment means from the predictions is summed (logarithmic color scale); the minimum (cross) coincides with the true values (circle)](./plots/cn_states.py)

**Example 13.2.1** In the figure $\rho = 0.7$ and the tumor ploidy is $\psi = 2.67$. A segment with the normal state $(1, 1)$ has $\mathrm{logR} = \log_2(2/2.47) = -0.30$, not $0$: in a hyperdiploid tumor, a segment with two copies is relatively lost. The single-copy loss $(1, 0)$ has $\mathrm{logR} = -0.92$ and $\mathrm{BAF} = 0.23$ (or $0.77$); the copy-neutral **loss of heterozygosity** $(2, 0)$ has the same $\mathrm{logR}$ as $(1, 1)$, $-0.30$, but $\mathrm{BAF} = 0.15$; the states $(2, 2)$ and $(3, 1)$ share $\mathrm{logR} = 0.46$ and differ only in the BAF, $0.50$ against $0.29$. Neither signal alone determines the state; together they do, and the search over $(\rho, \psi)$ recovers $\rho = 0.70$ and $\psi = 2.7$ on a grid of step $0.075$.

:::

Methods such as ASCAT, ABSOLUTE, FACETS and Battenberg fit purity and ploidy in this way, by requiring that the segments take integer states. Their typical failure is an ambiguity of ploidy: a near-diploid solution and a near-tetraploid solution of lower purity can explain the same data almost equally well, and whole-genome doubling, common in advanced tumors, has to be decided from such a choice, from subclonal patterns or from single-cell data.

### 13.2.3. Clonal Structure

Purity and copy number turn the variant-allele fraction of a mutation into the fraction of tumor cells that carry it.

**Definition 13.2.2 (Cancer Cell Fraction)** The *cancer cell fraction* (CCF) of a somatic mutation is the fraction of tumor cells that carry it. By Formula 12.7.1 of [7.8.12](/7.8.12#fml-12.7.1), a mutation on $m$ of the $n$ copies of a locus in a sample of purity $\rho$ has the expected variant-allele fraction $f = \rho\,\mathrm{CCF}\,m/[\rho n + 2(1 - \rho)]$, so
$$
\mathrm{CCF} = \frac{f\,[\rho n + 2(1 - \rho)]}{\rho\,m}.
$$
Mutations with $\mathrm{CCF} \approx 1$ are clonal, present in every tumor cell; mutations with smaller CCF are subclonal.

**Example 13.2.2** In a sample of purity $0.6$, two heterozygous mutations at diploid loci have allele fractions $0.30$ and $0.18$. Their cancer cell fractions are $0.30 \times 2/0.6 = 1.0$ and $0.18 \times 2/0.6 = 0.6$: the first is clonal, the second marks a subclone of $60\,\%$ of the tumor cells.

:::

Clustering the CCFs of all mutations of a tumor, with binomial read-count likelihoods and a Dirichlet-process mixture (PyClone, DPClust), finds the subclones; the pigeonhole principle orders them into a phylogeny (two subclones whose CCFs sum to more than one must be nested), and sampling several regions of a tumor, or the same tumor before and after treatment, shows how the clones are distributed in space and selected in time. Normal tissues are also mosaics: sequencing of morphologically normal skin, esophagus, urothelium and blood finds clones carrying cancer driver mutations in a large fraction of cells, more with age and exposure, and clonal hematopoiesis in the blood confounds tumor–normal comparisons ([7.8.12](/7.8.12#sec-12.7)). A driver mutation is therefore necessary but not sufficient for cancer.

### 13.2.4. Consortia, Portals and Cell Lines

| Resource | Content | Typical use |
|---|---|---|
| TCGA (The Cancer Genome Atlas) | genomes or exomes, copy number, methylation, transcriptomes, proteins (RPPA) and clinical data of over $20\,000$ primary tumors and matched normals of $33$ cancer types | molecular characterization and pan-cancer analysis |
| ICGC and PCAWG | international cohorts; whole genomes of $2658$ tumors of $38$ types analyzed uniformly (Pan-Cancer Analysis of Whole Genomes, 2020) | non-coding drivers, structural variants, signatures |
| COSMIC | curated somatic mutations; the Cancer Gene Census of genes with evidence of driving cancer; the catalog of mutational signatures | interpretation of mutations |
| cBioPortal | interactive access to TCGA and many other studies: oncoprints, mutual exclusivity, survival by alteration | exploration, hypothesis generation |
| GEPIA | expression in TCGA tumors against GTEx normal tissues, survival by expression, deconvolution | expression questions |
| IntOGen | drivers called uniformly by several methods across cohorts | lists of driver genes per tumor type |
| CCLE and DepMap | molecular profiles of about a thousand cancer cell lines, genome-wide CRISPR loss-of-function screens and drug-sensitivity screens | dependencies and biomarkers (13.7) |

Portals invite quick analyses; they also make it easy to test a gene against many outcomes, cut points and cohorts, with the multiple-testing problems of 13.6.3.

## 13.3. Mutational Signatures

### 13.3.1. The Mutational Catalog

Each mutational process leaves a characteristic pattern in the genome, its **mutational signature** ([7.4.21](/7.4.21#def-21.1.1)): tobacco carcinogens bind guanine and cause C>A transversions, ultraviolet light causes C>T transitions at dipyrimidines, the spontaneous **deamination** of 5-methylcytosine causes C>T at CpG at a steady rate (a clock), APOBEC cytidine deaminases cause C>T and C>G at TCW motifs (W = A or T), and defects of mismatch repair and of homologous recombination leave their own patterns. Reading these patterns requires a representation of the mutations of a tumor.

**Definition 13.3.1 (Mutational Catalog)** A single-base substitution is described by the pyrimidine of the mutated base pair (C or T, which collapses complementary changes: a G>T on one strand is a C>A on the other) and its change (six classes: C>A, C>G, C>T, T>A, T>C, T>G), together with the bases immediately $5'$ and $3'$ of it ($4 \times 4 = 16$ contexts): $96$ classes in all. The *mutational catalog* of a set of tumors is the $96 \times N$ matrix $M$ of the counts of substitutions in each class in each of $N$ tumors.

Analogous catalogs exist for doublet substitutions, small indels (classified by length, repeat context and microhomology) and structural variants. A signature is a probability distribution over the classes, and the catalog of a tumor is the sum of the mutations produced by the processes active in its history.

### 13.3.2. Signatures by Non-Negative Matrix Factorization

**Definition 13.3.2 (Non-Negative Matrix Factorization)** Given a matrix $M \in \mathbb{R}_{\ge 0}^{p \times N}$ and a rank $k$, **non-negative matrix factorization** (NMF) finds $W \in \mathbb{R}_{\ge 0}^{p \times k}$ and $H \in \mathbb{R}_{\ge 0}^{k \times N}$ with $M \approx WH$, minimizing a divergence such as the squared Frobenius error $\lVert M - WH\rVert_{\mathrm{F}}^2$ or the generalized **Kullback–Leibler divergence** $\sum_{ij}\bigl(M_{ij}\ln\frac{M_{ij}}{(WH)_{ij}} - M_{ij} + (WH)_{ij}\bigr)$.

For mutational catalogs the columns of $W$, normalized to sum to one, are signatures and the entries of $H$ are exposures, the number of mutations each process contributed to each tumor. Non-negativity is what makes the factors interpretable: mutations are only added, never canceled, so each tumor is a sum of parts. **Principal component analysis** of the same matrix ([3.4.5](/3.4.5)) would produce orthogonal components with negative entries, not processes. Minimizing the Kullback–Leibler divergence is maximum likelihood under the model $M_{ij} \sim \mathrm{Poi}((WH)_{ij})$, the natural model for counts.

**Algorithm 13.3.1 (Multiplicative Updates)** (Lee and Seung, 2001) Start from positive $W$ and $H$ and repeat until convergence:
$$
H_{aj} \leftarrow H_{aj}\frac{\sum_iW_{ia}M_{ij}/(WH)_{ij}}{\sum_iW_{ia}}, \qquad W_{ia} \leftarrow W_{ia}\frac{\sum_jH_{aj}M_{ij}/(WH)_{ij}}{\sum_jH_{aj}};
$$
then rescale each column of $W$ to sum to one and the corresponding row of $H$ inversely. Each update does not increase the Kullback–Leibler divergence, and the factors stay non-negative because they are multiplied by non-negative ratios. Each iteration costs $O(pNk)$.

The objective is not convex, so the factorization is repeated from many random starts and the best or most stable solution kept. The rank is chosen by the trade-off between the fit and the stability of the signatures across bootstrap resamplings of the catalog (Alexandrov and colleagues, 2013): the error falls steeply until the true number of processes is reached and slowly afterward, while the signatures found at a too high rank are unstable splits of real ones.

![Recovering mutational signatures by non-negative matrix factorization (simulation). Four illustrative signatures over the 96 classes are mixed in 100 tumors with sparse gamma-distributed exposures (44 to 5949 mutations per tumor, median 1332), and counts are drawn from the Poisson distribution. A: true signatures (outline) and those recovered by NMF with rank 4 (bars, colored by base change), with their cosine similarities. B: true and estimated numbers of mutations attributed to each signature in each tumor carrying it (logarithmic axes). C: Poisson deviance of the best of 10 factorizations against the rank k](./plots/signatures_nmf.py)

**Example 13.3.1** In the figure, the four signatures are recovered with **cosine similarities** between $0.996$ and $0.9996$, and the Poisson deviance falls from $83\,640$ at rank $1$ to $24\,506$ at rank $3$ and $9234$ at rank $4$, then only to $8956$ at rank $5$; the deviance at rank $4$ is close to its expectation for Poisson noise, the number of entries ($9600$) minus the number of fitted parameters ($784$). Exposures are estimated within a median relative error of $4$ to $8\,\%$, but processes absent from a tumor are not estimated as zero: in tumors without the tobacco-like process, NMF attributes a median of $25$ mutations to it. Small exposures are the least reliable part of any signature analysis, which matters when the presence of a process (for example of homologous-recombination deficiency) is used to choose a treatment.

### 13.3.3. Refitting and Interpretation

Once a reference set of signatures exists, the catalog $\boldsymbol{m}$ of a single tumor is decomposed by refitting: non-negative least squares or Poisson regression of $\boldsymbol{m}$ on a chosen subset of reference signatures $W$, $\min_{\boldsymbol{h} \ge \boldsymbol{0}}\lVert\boldsymbol{m} - W\boldsymbol{h}\rVert$. The COSMIC catalog of reference signatures was derived by NMF from tens of thousands of tumors; the single-base-substitution signatures (SBS) are numbered, among them SBS1 (C>T at CpG, the clock-like deamination of methylcytosine), SBS2 and SBS13 (APOBEC), SBS3 (defective homologous recombination, as in *BRCA1*/*BRCA2*-deficient tumors), SBS4 (tobacco smoking), SBS6, SBS15, SBS26 and SBS44 (defective mismatch repair), SBS7 (ultraviolet light) and SBS22 (aristolochic acid). Refitting with too many signatures overfits: a tumor's mutations can be distributed among similar flat signatures in many ways, so refitting should use the signatures expected for the tumor type and test whether adding one improves the fit significantly.

Signatures have identified causes of cancer. Aristolochic acids, present in plants of the genus *Aristolochia* used in traditional herbal remedies, cause renal failure and urothelial cancer and leave a distinctive signature dominated by T>A transversions (SBS22). In liver cancers, the signature was found in $78\,\%$ of $98$ tumors from Taiwan and in $47\,\%$ of $89$ from mainland China, against $1.7\,\%$ in North America and $4.8\,\%$ in Europe (Ng and colleagues, 2017), a geographic pattern that matched the use of these remedies; the same signature marks large clonal expansions in morphologically normal urothelium of exposed people (Li and colleagues, 2020). The mutagen thus leaves its fingerprint before any tumor forms. Signatures also have clinical uses: the signature of homologous-recombination deficiency predicts sensitivity to PARP inhibitors and platinum beyond the carriers of *BRCA1*/*BRCA2* mutations, and mismatch-repair signatures identify the tumors likely to respond to immunotherapy (13.7.3).

## 13.4. Drivers and Passengers

### 13.4.1. The Background Mutation Rate

A gene is a candidate driver if it is mutated in more tumors than chance predicts. Chance is set by the rate at which mutations accumulate without selection.

**Definition 13.4.1 (Background Mutation Rate)** The *background mutation rate* of a genomic region in a tumor type is the rate per base and per tumor at which somatic mutations occur in the region in the absence of selection, the rate that passenger mutations follow.

The rate is not constant. It varies by three orders of magnitude between tumor types, from below $0.1$ per megabase in some pediatric tumors to above $100$ in melanomas and tumors with defective mismatch repair or polymerase proofreading (Lawrence and colleagues, 2013); between tumors of one type; between mutation classes and sequence contexts (13.3); and along the genome. Late-replicating, transcriptionally silent, heterochromatic regions accumulate more mutations than early-replicating, expressed, open ones (Schuster-Böckler and Lehner, 2012), because repair is less efficient there (transcription-coupled repair acts on expressed genes, mismatch repair is coupled to replication) and possibly because the nuclear periphery is more exposed. A model that assumes one rate for all genes finds false drivers among large genes in late-replicating regions: in early exome analyses, olfactory receptor genes and very long genes expressed at low levels repeatedly appeared among the "significantly mutated" genes.

**Formula 13.4.1 (Recurrence Test)** Let gene $g$ have $L_g$ coding bases at which a mutation would be counted, let $T$ tumors be sequenced, and let $\mu_g$ be its background rate per base and tumor. Under the null hypothesis of no selection, the number of mutations is approximately $X_g \sim \mathrm{Poi}(\lambda_g)$ with $\lambda_g = L_gT\mu_g$, and the one-sided p-value is $\mathbb{P}(X_g \ge x_g)$. Overdispersion between genes beyond what the covariates explain is modeled by a **negative binomial distribution** (a gamma-distributed rate).

**Example 13.4.1** A gene with $1.5\,\mathrm{kb}$ of coding sequence is mutated $8$ times in $500$ tumors. With a background rate of $1$ per megabase, $\lambda = 1500 \times 500 \times 10^{-6} = 0.75$ and $\mathbb{P}(X \ge 8) = 1.3 \times 10^{-6}$, which passes a **Bonferroni correction** for $18\,000$ genes ($2.8 \times 10^{-6}$). If the gene lies in a late-replicating region with three times the average rate, $\lambda = 2.25$ and $\mathbb{P}(X \ge 8) = 0.0023$: not significant. A threefold error in the background, well within the observed variation, decides the call.

:::

MutSigCV (Lawrence and colleagues, 2013) estimates a gene-specific background from the silent mutations in the gene and in genes with similar covariates (expression, replication time, chromatin state), and tests the excess of non-silent mutations against it. Modern methods combine evidence of three kinds: excess frequency, functional impact (truncating mutations in tumor suppressors, damaging missense changes) and positional clustering.

![Why recurrence tests need the right background mutation rate (simulation). 18 000 genes with log-normal coding lengths (median 1.2 kb) are sequenced in 400 tumors; the background rate varies with a covariate x (standing for replication timing and expression), log μ_g = log(1.5 × 10⁻⁶) + 0.6x + u_g with u_g ~ N(0, 0.5²), and 40 driver genes carry an excess of mutations. A: mutations per Mb per tumor against x (drivers red; genes without mutations at the bottom), with the fitted rate (solid) and the genome-wide rate (dashed). B: quantile–quantile plot of −log₁₀ p for the non-driver genes under three background models: one genome-wide rate (Poisson), a rate depending on x (Poisson regression), and the same with overdispersion (negative binomial, dispersion by moments after leaving out the 1 % of genes with the largest residuals). C: genes called at a false discovery rate of 10 % (Benjamini–Hochberg), true drivers and false positives](./plots/driver_qq.py)

**Example 13.4.2** In the simulation all $40$ drivers are found by every model, but the calls at a **false discovery rate** of $10\,\%$ (**Benjamini–Hochberg procedure**) include $277$ false positives with one genome-wide rate, $51$ when the rate depends on the covariate, and $20$ when, in addition, overdispersion is modeled. The remaining false positives come from the gene-level variation $u_g$ that no covariate captures, and the overdispersion estimated by moments ($\phi = 0.10$) underestimates the true value, $\mathrm{e}^{0.25} - 1 = 0.28$, because the most variable genes were excluded with the candidates. A quantile–quantile plot of the null genes, flat along the diagonal for a correct background, is the standard check; its departure from the diagonal well before the extreme tail is the signature of a misspecified background, not of discovery.

### 13.4.2. Selection Measured by dN/dS

Silent mutations are an internal control: they share the gene's local rate and context but are rarely selected.

**Formula 13.4.2 (dN/dS Ratio)** Let a gene have $n_{\mathrm{N}}$ non-synonymous and $n_{\mathrm{S}}$ synonymous somatic mutations, and let $L_{\mathrm{N}}$ and $L_{\mathrm{S}}$ be the expected numbers of non-synonymous and synonymous mutations per unit rate given the gene's sequence and the trinucleotide mutation spectrum of the tumors (the opportunities). The ratio
$$
\omega = \frac{n_{\mathrm{N}}/L_{\mathrm{N}}}{n_{\mathrm{S}}/L_{\mathrm{S}}}
$$
estimates the relative rate at which non-synonymous mutations are retained: $\omega > 1$ indicates positive selection, $\omega < 1$ negative selection, $\omega = 1$ neutrality. Separate ratios are computed for missense and truncating mutations.

**Example 13.4.3** A gene with $20$ missense and $2$ synonymous mutations, whose sequence offers three times as many opportunities for missense as for synonymous changes, has $\omega = (20/3)/(2/1) = 3.3$: an estimated $70\,\%$ of its missense mutations ($1 - 1/\omega$) are retained because of selection.

:::

The same ratio taken over all genes measures selection genome-wide. In about $7700$ tumors of $29$ types, dN/dS indicated that a tumor carries on average about four coding substitutions under positive selection, from fewer than one in some types to more than ten in others, and that negative selection on somatic mutations is very weak outside a few essential genes, so most passenger mutations are tolerated (Martincorena and colleagues, 2017). The method needs no assumption on covariates, because synonymous mutations calibrate the rate gene by gene, but it has low power for genes with few mutations and assumes that synonymous mutations are neutral, which fails where they disrupt splicing.

### 13.4.3. Hotspots and the Pattern of Mutations

Oncogenes are activated by a few specific changes that alter a function, so their mutations cluster at hotspots: *KRAS* codons 12, 13 and 61, *BRAF* V600, *PIK3CA* E542, E545 and H1047, *IDH1* R132. Tumor suppressors are inactivated by any change that destroys the protein, so their mutations are spread along the gene and are often truncating. The 20/20 rule turns this into a classification (Vogelstein and colleagues, 2013): a gene is classified as an oncogene if more than $20\,\%$ of its mutations are missense changes at recurrent positions, and as a tumor suppressor if more than $20\,\%$ are inactivating. Positional clustering is tested against the distribution of positions expected under the gene's mutation spectrum, in the linear sequence or in the three-dimensional protein structure, where residues far apart in sequence can form one functional surface.

### 13.4.4. The Limits of Statistics

The genes found by recurrence form a long tail: a few genes such as *TP53*, *KRAS* and *PIK3CA* are mutated in large fractions of tumors, most drivers in a few percent, and many presumably in less than one percent. Under the Poisson model of Example 13.4.1 with a gene-wise threshold of $0.05/18\,000$, a gene of $1.5\,\mathrm{kb}$ mutated in $2\,\%$ of tumors above a background of $1$ per megabase is detected with probability $0.07$ in $100$ tumors, $0.47$ in $300$ and $0.995$ in $1000$; with realistic background heterogeneity, more are needed, and the numbers rise steeply for tumor types with high mutation rates. Thousands of tumors per type are required to find the genes mutated at a few percent, and rarer drivers, non-coding drivers and drivers acting by copy number or methylation are harder still.

Recurrence also says nothing about mechanism: a list of significantly mutated genes does not say what the mutations do, why they are selected in one tissue and not another, or how genes mutated in different tumors relate to each other. Genome-wide association studies of inherited risk face the same problems of sample size and stringent thresholds ([7.4.25](/7.4.25)), and in both cases networks offer a way to combine weak signals from many genes into strong signals for a few pathways.

## 13.5. Network-Based Driver Inference

### 13.5.1. Two Directions

Network approaches start either from the genome or from the phenotype. Bottom-up, they ask which alterations of the genome perturb which regulatory programs: a mutation, deletion or epigenetic silencing upstream, a change in the activity of factors downstream. Top-down, they start from a phenotype (an expression subtype, a poor prognosis, resistance) and ask which regulators explain it, and then which alterations explain the regulators. Both use the networks of earlier chapters: regulatory networks inferred from tumor expression ([7.9.11](/7.9.11)), protein interaction networks ([7.9.10](/7.9.10)) and signaling networks.

### 13.5.2. Integrating Alterations with Expression

The simplest integration asks whether a copy-number change alters the expression of the genes in the segment. Amplified regions contain many genes, of which typically one is the driver; requiring that the gene's expression follow its copy number across tumors, and that the gene be needed by cells that carry the amplification, narrows the region. The approach identified *MITF* as an amplified lineage-survival oncogene in melanoma (Garraway and colleagues, 2005).

Regulatory networks extend this to genes that are not altered themselves. A gene can be dysregulated by alterations of its regulators, by changes of the modulators of these regulators (the MINDy analysis of [7.9.11](/7.9.11#sec-11.4.5)) or post-transcriptionally. A **microRNA** represses many targets, and RNAs that share binding sites for the same microRNAs compete for them: when one is lost, more microRNA is free to repress the others. Such competing endogenous RNAs (ceRNAs) were mapped in glioblastoma from matched microRNA and mRNA profiles with a **conditional mutual information** test, asking whether the expression of one RNA modulates the dependence of another on their shared microRNAs (Sumazin and colleagues, 2011). The resulting network linked the tumor suppressor *PTEN* to many ceRNA regulators, among them genes in frequently deleted regions, so that deletion of these regulators reduced *PTEN* expression although *PTEN* itself was intact. Such analyses explain why a pathway can be altered in tumors that carry no alteration of its known genes. Top-down, **master regulator** analysis of a tumor subtype finds the factors whose **regulon activity** explains the subtype's signature, as for C/EBPβ and STAT3 in mesenchymal glioblastoma ([7.9.11](/7.9.11#sec-11.7.3)), and the alterations upstream of these factors can then be searched for.

### 13.5.3. Mutated Subnetworks

If drivers in different tumors hit the same pathway, the mutated genes should cluster in interaction networks even when each gene is rarely mutated. **Network propagation** ([7.9.12](/7.9.12#sec-12.4.2)) tests this: HotNet2 (Leiserson and colleagues, 2015) places on each gene a "heat" proportional to its mutation frequency, diffuses it over an interaction network by a random walk with restart, and finds subnetworks in which more heat is exchanged than in networks with permuted heat, applied to $12$ cancer types; besides known pathways, it found subnetworks such as the cohesin and condensin complexes whose individual genes were too rarely mutated to be significant. A complementary signal is mutual exclusivity: genes in one pathway tend not to be mutated in the same tumor, and methods such as Dendrix (Vandin, Upfal and Raphael, 2012) search for gene sets whose mutations cover many tumors with few overlaps, which identifies alternative routes to the same capability.

### 13.5.4. Network-Based Stratification

Mutation profiles should classify tumors better than expression profiles: they are digital (present or absent), relative to the patient's own normal genome, and closer to the causes. In practice, two tumors rarely share mutated genes beyond the few common drivers, so clustering raw mutation profiles fails. Network-based stratification replaces each profile by its smoothed version on a network.

**Algorithm 13.5.1 (Network-Based Stratification)** (Hofree, Shen, Carter, Gross and Ideker, 2013) Given a binary tumor-by-gene matrix of somatic mutations and a gene interaction network:

1. Propagation. Smooth each tumor's mutation profile over the network by a random walk with restart (in the original work with restart probability $0.3$, written as a propagation constant $\alpha = 0.7$), and normalize the smoothed profiles across tumors by **quantile normalization**.
2. Factorization. Factor the smoothed matrix by non-negative matrix factorization with $k$ factors, regularized so that genes adjacent in the network receive similar loadings (network-regularized NMF), and assign each tumor to the factor with the largest weight.
3. Consensus. Repeat steps 1–2 on many subsamples of tumors and genes (for example $1000$ subsamples of $80\,\%$) and cluster the matrix of how often two tumors are assigned together (consensus clustering); choose $k$ by the stability of the consensus.
4. Interpretation. Compare the subtypes for survival, response to treatment and histology, and identify the network regions that define each subtype.

![Network-based stratification on a toy example (simulation). A: an interaction network of 36 genes: two pathways of 12 genes (blue and amber; pairs within a pathway interact with probability 0.35) joined by a few edges, and 12 other genes (gray). Each of 40 tumors carries one or two mutations in a gene of one pathway (20 tumors per pathway, one subtype each) and one or two passenger mutations anywhere; red outlines show the mutated genes of two tumors of the same subtype, which share no mutated gene (one outlined gene is a passenger in the other pathway). B: cosine similarity between the binary mutation profiles of the tumors, ordered by subtype. C: the same after propagation of each profile by a random walk with restart (restart probability 0.3). Below B and C: agreement of a rank-2 NMF with the true subtypes](./plots/nbs.py)

**Example 13.5.1** In the toy example only $33\,\%$ of pairs of tumors of the same subtype share a mutated gene. The mean cosine similarity of raw profiles is $0.12$ within subtypes and $0.05$ between them, and a rank-$2$ NMF of the raw matrix assigns $75\,\%$ of the tumors correctly; after propagation the similarities are $0.53$ and $0.31$ and the factorization assigns $95\,\%$ correctly. Propagation does not create information: it converts "mutated in the same pathway" into similarity, which is exactly the assumption that tumors of a subtype disrupt the same pathways.

:::

Applied to somatic mutations of ovarian, uterine and lung tumors from TCGA with several human interaction networks, the method found subtypes that were associated with survival or with histology, whereas clustering of the raw mutation profiles was not informative (Hofree and colleagues, 2013). The subtypes are only as good as the network: interaction maps are biased toward well-studied cancer genes ([7.9.12](/7.9.12#sec-12.1.2)), which can make known cancer genes central for reasons of ascertainment, and the result should be compared against degree-preserving randomized networks.

### 13.5.5. Mutations That Rewire Signaling

Mutations can also change the edges of a network instead of the activity of a node. Phosphorylation by kinases is the wiring of signaling, and a missense mutation at or near a phosphorylated residue can abolish a phosphorylation, or create or destroy a binding motif for a kinase. Mapping $241\,701$ missense SNVs from TCGA tumors onto $87\,060$ experimentally determined phosphosites in $10\,185$ proteins identified $16\,840$ phosphorylation-related SNVs in $5859$ genes, present in $89\,\%$ of the samples; for $29\,\%$ of them a specific mechanism, loss of a phosphosite or rewiring of a kinase–substrate interaction, could be predicted (Reimand, Wagih and Bader, 2013). The rewired interactions were enriched in signaling pathways known to drive cancer. The analysis illustrates a general point: the functional unit of a mutation may be an interaction, and the network, not the gene, is the level at which its effect is described.

## 13.6. Molecular Subtypes, Classifiers and Prognosis

### 13.6.1. Subtypes

Tumors of one organ differ in their molecular programs, and these differences often matter more for prognosis and treatment than histology.

| Cancer | Classification | Basis |
|---|---|---|
| breast | luminal A, luminal B, HER2-enriched, basal-like, normal-like; the PAM50 classifier assigns them from $50$ genes (Parker and colleagues, 2009) | expression |
| breast | ten integrative clusters in about $2000$ tumors (METABRIC; Curtis and colleagues, 2012) | copy number and its effect on expression |
| glioblastoma | proneural, neural, classical, mesenchymal (Verhaak and colleagues, 2010); master regulators of the mesenchymal state in [7.9.11](/7.9.11#sec-11.7.3) | expression with mutations and copy number |
| colorectal | consensus molecular subtypes CMS1 (immune, mismatch-repair deficient) to CMS4 (mesenchymal) (Guinney and colleagues, 2015) | consensus of six expression classifications |

Subtypes are found by unsupervised clustering ([3.4.11](/3.4.11)), NMF or consensus clustering, and turned into classifiers that assign new tumors. Two cautions apply. Bulk expression mixes tumor and non-tumor cells, so some "subtypes" partly reflect composition (the mesenchymal subtypes of several cancers are enriched in stromal cells); deconvolution or single-cell data separate the two. And a classification is useful only if it predicts something independent of what is already known, such as response to a treatment.

### 13.6.2. Classifiers and Selection Bias

With thousands of genes and tens to hundreds of patients, a classifier will fit the training data whatever the truth. **Cross-validation** estimates the error on new data, but only if every step that uses the outcome, including the selection of genes, is repeated inside each fold.

![Selection bias in cross-validation (simulation in the design of Simon and colleagues, 2003). Each data set has 20 specimens, 10 per class, and 6000 genes with independent standard normal log-ratios in both classes: there is nothing to predict. The classifier is the compound covariate predictor built from the 10 genes with the largest two-sample t statistics. For 300 data sets: the cumulative proportion of data sets with at most a given number of misclassifications out of 20, estimated by resubstitution, by leave-one-out cross-validation after selecting the genes on all 20 specimens, and by leave-one-out cross-validation with the selection repeated in each fold. Only the last is centered near 10, the expected number for a random guess](./plots/selection_bias.py)

**Example 13.6.1** In the simulation, resubstitution misclassifies no specimen in $99\,\%$ of the data sets. Leave-one-out cross-validation applied after selecting the genes on all specimens is hardly better: no error in $91\,\%$ of the data sets, a mean of $0.09$ errors out of $20$. With the selection inside each fold, the mean is $10.7$ errors and the central $90\,\%$ of the data sets lie between $3$ and $18$: the correct estimate of a classifier with no information, and a reminder of how variable error estimates are with $20$ specimens. Simon and colleagues (2003) made this point against published microarray classifiers; it applies to every high-dimensional predictor ([7.7.21](/7.7.21), [4.6.2](/4.6.2)).

:::

The same leakage arises when normalization, batch correction, imputation or the choice of a cutpoint uses all samples, and when the "independent" validation set was used to choose among several candidate models. The only fully honest estimate comes from data not touched during development, ideally from another cohort and platform.

### 13.6.3. Prognostic Signatures and Their Pitfalls

A prognostic signature predicts outcome irrespective of treatment; a predictive signature predicts benefit from a specific treatment. The best-known clinical success was designed as both. The 21-gene recurrence score for estrogen-receptor-positive breast cancer was developed by selecting $16$ cancer-related genes and $5$ reference genes from $250$ candidates in three studies, measured by RT-PCR on fixed tissue, and validated in an independent trial cohort of patients treated with tamoxifen (Paik and colleagues, 2004); a randomized trial later showed that for most women with an intermediate score, chemotherapy added to endocrine therapy gave no benefit (TAILORx; Sparano and colleagues, 2018), sparing many patients a toxic treatment.

Many published signatures did not replicate. One reason is that outcome in breast cancer is strongly associated with proliferation, which is reflected in the expression of hundreds of genes: in one analysis most random sets of genes were significantly associated with outcome, as were signatures of unrelated biology such as the effect of social defeat in mice (Venet, Dumont and Detours, 2011). A signature's association with outcome is therefore no evidence for its biology, and new signatures should be compared with a proliferation score and with standard clinical variables. A second reason is the flexibility of the analysis, illustrated by the optimal cutpoint.

![Survival by molecular subtype, and the optimal-cutpoint trap (simulation). A: 200 patients, 100 per subtype, with exponential survival (median 60 months in subtype 1, 30 in subtype 2: hazard ratio 2) and uniform censoring between 24 and 120 months; Kaplan–Meier curves with censoring ticks, log-rank test and Cox hazard ratio. B: 200 genes whose expression is unrelated to survival; for each, patients are split at every cutpoint between the 10th and 90th percentiles of expression and the smallest log-rank p value is kept; histogram of these minimal p values (logarithmic axis) with the nominal 0.05 (dashed). C: Kaplan–Meier curves of the null gene with the smallest minimal p value, split at its best cutpoint](./plots/subtype_km.py)

**Example 13.6.2** In panel A, the subtypes differ clearly: log-rank $p = 1.7 \times 10^{-4}$, Cox hazard ratio $1.99$ ($95\,\%$ interval $1.38$ to $2.87$), from $122$ deaths. In panel B, a gene without any effect, dichotomized at the cutpoint that minimizes the log-rank p value, gives $p < 0.05$ for $46\,\%$ of genes and $p < 0.01$ for $9.5\,\%$; the best of $200$ null genes, split at its $78$th percentile, has $p = 4 \times 10^{-4}$ and survival curves (panel C) that look like a strong marker. The minimum over cutpoints is not a p-value; the cutpoint must be fixed in advance (for example the median), the marker analyzed as a continuous covariate in a **proportional hazards model**, or the whole search included in a permutation test or a cross-validation ([7.7.16](/7.7.16)). Portals that offer survival plots "at the best cutoff" for any gene invite exactly this error.

### 13.6.4. The Immune Composition of Tumors

Deconvolution of bulk expression with reference profiles of immune and stromal cells ([7.9.5](/7.9.5#sec-5.7)) classifies tumors by their microenvironment: tumors rich in cytotoxic T cells ("inflamed" or "hot") against tumors from which T cells are excluded at the margin or absent ("cold"). Infiltration by T cells is associated with better prognosis in several cancers and with response to **immune checkpoint blockade**. Spatial methods add where the cells are, whether T cells are in contact with tumor cells or held in the stroma, which bulk deconvolution cannot see ([7.9.6](/7.9.6#sec-6.11.3)).

## 13.7. Dependencies and Therapy

### 13.7.1. Targeted Therapy and Oncogene Addiction

Some tumors depend on the driver that started them, a state called **oncogene addiction**: inhibiting the mutant kinase stops growth. Imatinib against BCR–ABL1 in chronic myeloid leukemia ([7.4.21](/7.4.21#sec-21.5)), HER2 antibodies against *ERBB2*-amplified breast cancer, and inhibitors of mutant EGFR, ALK fusions and BRAF V600E in lung cancer and melanoma are the classical examples of **targeted therapy** ([7.3.26](/7.3.26#sec-26.6.2)). The genotype, not the organ, selects the treatment, which has changed the design of clinical trials:

- a basket trial tests one drug in tumors of many organs that share one alteration (an ALK fusion in lung, colorectal or renal cancer);
- an umbrella trial assigns patients with one cancer type to different drugs according to their alterations.

Responses to targeted drugs are often strong but transient, because resistant subclones present before treatment are selected ([7.6.41](/7.6.41#sec-41.5)), which is the argument for combinations and for monitoring the clones by circulating tumor DNA ([7.9.8](/7.9.8#sec-8.5.4)).

### 13.7.2. Dependency Maps

Most tumors lack a targetable driver. Systematic screens look for the other genes a tumor depends on.

The Cancer Cell Line Encyclopedia profiled $947$ human cancer cell lines (mutations, copy number, expression) and measured the sensitivity of $479$ of them to $24$ drugs, showing that sensitivity could be predicted from molecular features: for example, expression of *SLFN11* predicted sensitivity to topoisomerase I inhibitors (Barretina and colleagues, 2012). The Cancer Dependency Map extended this to genome-wide **CRISPR screens** in about a thousand cell lines ([7.9.10](/7.9.10#sec-10.7)), estimating for every gene and cell line the effect of its loss on proliferation, corrected for guide efficiency and for the excess cutting toxicity in amplified regions. Genes fall into three groups: common essential genes needed by all cells (ribosome, proteasome, RNA polymerase), which are poor targets; non-essential genes; and selective dependencies, needed only by cells with a particular feature, which are the candidates.

The best selective dependencies are cases of **synthetic lethality** ([7.3.26](/7.3.26#sec-26.6.3), [7.4.21](/7.4.21#sec-21.5)) between a tumor alteration and a druggable gene. PARP inhibitors in *BRCA1*/*BRCA2*-deficient tumors are the clinical model. Dependency maps found new examples: cells with microsatellite instability depend on the WRN helicase (Chan and colleagues, 2019; Behan and colleagues, 2019); cells with deletion of *MTAP*, which is co-deleted with *CDKN2A* in many tumors, accumulate its substrate methylthioadenosine, which partly inhibits the methyltransferase PRMT5 and makes the cells hypersensitive to its further loss (Kryukov and colleagues, 2016; Mavrakis and colleagues, 2016). Paralog pairs are another source: a cell that has lost one paralog depends on the other. The statistics are those of genetic interaction screens: a dependency is called selective if the gene effect is associated with the feature across cell lines beyond what lineage and other confounders explain, with correction for testing thousands of genes against thousands of features.

### 13.7.3. Tumor Mutational Burden and Immunotherapy

Somatic mutations in expressed genes can create neoantigens, mutant peptides presented by MHC molecules and recognized by T cells. Tumors with more mutations present more neoantigens, and checkpoint blockade, which releases T cells from inhibition, works better in them.

**Definition 13.7.1 (Tumor Mutational Burden)** The **tumor mutational burden** (TMB) of a tumor is the number of somatic mutations (usually non-synonymous substitutions and indels in coding sequence) per megabase of sequence examined.

Across $27$ tumor types, the median TMB of a tumor type correlated with the objective response rate to PD-1 or PD-L1 inhibitors with a correlation coefficient of $0.74$ (Yarchoan, Hopkins and Jaffee, 2017). Tumors with mismatch-repair deficiency, whose TMB is very high, responded to PD-1 blockade regardless of their organ (Le and colleagues, 2015), and in 2017 this became the first tissue-agnostic approval of a cancer drug; in 2020 PD-1 blockade was approved for solid tumors with a TMB of at least $10$ mutations per megabase measured by a specified panel.

**Example 13.7.1** A targeted panel covers $1.1\,\mathrm{Mb}$ of coding sequence and finds $12$ somatic coding mutations: $\mathrm{TMB} = 12/1.1 = 10.9$ per megabase. Counting the mutations as Poisson, the exact $95\,\%$ interval for the count is $6.2$ to $21.0$, so for TMB it is $5.6$ to $19.1$ per megabase: the tumor is on the threshold of $10$ within sampling error. A tumor with $8$ mutations ($7.3$ per megabase, interval $3.1$ to $14.3$) has a probability of $0.18$ of showing $11$ or more mutations (above the threshold) in a repeated measurement if its true expectation were $8$. Thresholds on small panels classify tumors near the cutoff unreliably, and TMB values from different panels need calibration against whole-exome sequencing, because panels differ in size, gene content and the filtering of germline variants.

:::

TMB is an imperfect biomarker: it ignores which mutations are clonal (clonal neoantigens are better targets than subclonal ones), whether they are expressed and presented, the immune composition of the tumor (13.6.4) and the loss of antigen presentation by mutation of *B2M* or loss of HLA alleles. Models that combine these features predict response better than TMB alone, but none is yet accurate for individual patients.

### 13.7.4. Cancer Systems Biology in Practice

The analyses of this chapter combine into a workflow that recurs in research and in precision oncology:

```python
import numpy as np
import pandas as pd
from sklearn.decomposition import NMF
from lifelines import KaplanMeierFitter, CoxPHFitter
from lifelines.statistics import logrank_test

# 1. Mutational signatures: catalog of 96 classes x tumors (counts)
catalog = pd.read_csv("sbs96_catalog.tsv", sep="\t", index_col=0)      # rows: 96 classes
fits = [NMF(n_components=k, beta_loss="kullback-leibler", solver="mu", init="random",
            max_iter=2000, random_state=s).fit(catalog.values) for k in (3, 4, 5, 6) for s in range(10)]
best = {k: min((f for f in fits if f.n_components == k), key=lambda f: f.reconstruction_err_)
        for k in (3, 4, 5, 6)}
W = best[4].transform(catalog.values)                  # 96 x k
signatures = W / W.sum(0)                              # columns sum to one
exposures = best[4].components_ * W.sum(0)[:, None]   # k x tumors, in numbers of mutations

# 2. Survival by subtype with a pre-specified grouping (no optimal cutpoints)
clin = pd.read_csv("clinical.tsv", sep="\t")           # columns: months, death, subtype, age, stage
a, b = clin[clin.subtype == "A"], clin[clin.subtype == "B"]
print(logrank_test(a.months, b.months, a.death, b.death).p_value)
kmf = KaplanMeierFitter().fit(a.months, a.death, label="subtype A")
cox = CoxPHFitter().fit(pd.get_dummies(clin[["months", "death", "subtype", "age", "stage"]],
                                       drop_first=True, dtype=float),
                        duration_col="months", event_col="death")
cox.print_summary()                                    # hazard ratios adjusted for age and stage
```

The steps are general: decompose what is measured into interpretable parts (signatures, subtypes, regulon activities), relate them to outcomes with pre-specified analyses, and test the mechanisms they suggest by perturbation, in cell lines, organoids and model organisms, before they reach patients.

## Summary

| Question | Data | Method | Key formula or result | Pitfall | Section |
|---|---|---|---|---|---|
| What is altered? | tumor and normal genomes | somatic calling; logR and BAF | Formula 13.2.1; CCF (Definition 13.2.2) | purity and ploidy ambiguity; clonal hematopoiesis | 13.2 |
| What caused the mutations? | 96-class catalog | NMF (Algorithm 13.3.1), refitting | signatures recovered with cosine $> 0.99$ (Example 13.3.1) | spurious small exposures; overfitting in refitting | 13.3 |
| Which genes drive? | mutation counts | recurrence against the background rate (Formula 13.4.1); dN/dS (Formula 13.4.2); hotspots | a threefold error in the background decides a call (Example 13.4.1) | covariates and overdispersion (Example 13.4.2); power | 13.4 |
| Which pathways? | mutations, expression, networks | ceRNA and modulator networks; HotNet2; NBS (Algorithm 13.5.1) | propagation turns pathway sharing into similarity (Example 13.5.1) | biased interaction maps | 13.5 |
| Which subtype, which outcome? | expression, copy number, survival | clustering, classifiers, survival analysis | selection inside the folds (Example 13.6.1) | selection bias; optimal cutpoints (Example 13.6.2); proliferation | 13.6 |
| What can be treated? | CRISPR and drug screens; TMB | dependency maps; synthetic lethality | WRN in MSI, PRMT5 in *MTAP*-deleted cells; TMB (Definition 13.7.1) | panel size and calibration (Example 13.7.1) | 13.7 |

- Many mutations converge on few pathways: drivers of different tumors differ, the pathways they hit are shared, often with mutual exclusivity (13.1).
- Copy number is read jointly from depth and allele fractions, given purity and ploidy (Formula 13.2.1, Example 13.2.1); allele fractions become cancer cell fractions and a clonal phylogeny (Definition 13.2.2).
- Mutational signatures are found by Poisson NMF of the catalog (Definition 13.3.1, Algorithm 13.3.1) and identify causes such as aristolochic acid (13.3.3).
- Drivers are genes mutated beyond the background mutation rate (Definition 13.4.1), which varies with replication time, expression and chromatin; dN/dS calibrates selection gene by gene (Formula 13.4.2).
- Networks combine rare mutations into pathways: ceRNA and modulator networks explain dysregulation without mutation, network propagation finds mutated subnetworks, and network-based stratification classifies tumors by mutation profiles (Algorithm 13.5.1).
- Classifiers and prognostic signatures must be validated with every data-dependent step inside cross-validation (Example 13.6.1) and without optimal cutpoints (Example 13.6.2).
- Dependency maps and synthetic lethality extend targeted therapy beyond targetable drivers; TMB predicts response to immunotherapy on average but is noisy near thresholds (Example 13.7.1).

## Questions

1. In a tumor sample of purity $0.5$ and ploidy $2$, compute the expected logR and BAF (sequencing, $\gamma = 1$) for the states $(1, 1)$, $(1, 0)$, $(2, 0)$ and $(2, 1)$. Which pairs of states are indistinguishable by logR alone?

   **Answer** With $\rho = 0.5$, $\psi = 2$, the denominator of logR is $2(0.5) + 0.5 \times 2 = 2$. $(1, 1)$: $n = 2$, $\mathrm{logR} = \log_2(2/2) = 0$, $\mathrm{BAF} = (0.5 + 0.5)/2 = 0.5$. $(1, 0)$: $n = 1$, $\log_2(1.5/2) = -0.415$, $\mathrm{BAF} = 0.5/1.5 = 0.333$. $(2, 0)$: $n = 2$, $\mathrm{logR} = 0$, $\mathrm{BAF} = 0.5/2 = 0.25$. $(2, 1)$: $n = 3$, $\log_2(2.5/2) = 0.322$, $\mathrm{BAF} = 1/2.5 = 0.40$. The normal state $(1, 1)$ and copy-neutral loss of heterozygosity $(2, 0)$ have the same logR and are distinguished only by the BAF ($0.5$ against $0.25$ and $0.75$).

2. A heterozygous mutation lies in a region where the tumor has lost the other allele (state $(1, 0)$, the mutation on the remaining copy, $m = n = 1$). The sample purity is $0.8$ and the variant allele fraction is $0.65$. Is the mutation clonal? What would its allele fraction be if it had occurred after the loss of heterozygosity, on a chromosome that was then duplicated to $(2, 0)$ with the mutation on one copy?

   **Answer** $\mathrm{CCF} = f[\rho n + 2(1 - \rho)]/(\rho m) = 0.65 \times (0.8 + 0.4)/0.8 = 0.975$: clonal within sampling error. Expected allele fraction for a clonal mutation in that state: $0.8/(0.8 + 0.4) = 0.667$. If the region is $(2, 0)$ with the mutation on one of the two copies: $f = 0.8 \times 1/(0.8 \times 2 + 0.4) = 0.4$. The allele fraction thus reveals the order of events: a mutation on both copies of a duplicated LOH region ($f = 1.6/2.0 = 0.8$) occurred before the duplication, a mutation on one copy after it, which is how the timing of mutations relative to copy-number gains is inferred.

3. Explain why the 96-class representation uses the pyrimidine of the mutated base pair, and why principal component analysis of a mutational catalog gives less interpretable components than NMF.

   **Answer** A mutation changes a base pair, and its two strands are equivalent descriptions: G>T on one strand is C>A on the other, with the reverse-complemented context. Choosing the pyrimidine (C or T) as the reference collapses each pair of equivalent descriptions into one class, giving $6 \times 16 = 96$ classes instead of $192$, without losing information unless strand-specific processes (transcription-coupled repair, replication strand) are studied, for which strand-resolved catalogs are used. PCA finds orthogonal directions of maximal variance, with positive and negative loadings; mutational processes are non-negative and add up, are not orthogonal (several share C>T), and a component with negative loadings has no meaning as a process. NMF's non-negativity constraint gives parts that add, matching the generative model of the catalog as a sum of processes, and its KL objective is the Poisson likelihood for counts.

4. A tumor's catalog is refitted with $30$ reference signatures by non-negative least squares and is assigned small exposures to $12$ of them. What is wrong with this result, and how would you obtain a more reliable decomposition?

   **Answer** With many similar signatures (several are broad and flat), the least-squares problem is ill-conditioned and the solution distributes mutations among signatures to fit noise: small exposures to many signatures are typically spurious, as in Example 13.3.1 where an absent process still receives a median of $25$ mutations. Remedies: restrict refitting to the signatures known to occur in the tumor type; add signatures one at a time and keep one only if it improves the fit significantly (likelihood ratio test or a cosine-similarity threshold); assess the stability of exposures by bootstrap resampling of the tumor's mutations; report exposures with confidence intervals and require a minimum number of mutations before calling a process present.

5. Two genes have $1.2\,\mathrm{kb}$ of coding sequence and are sequenced in $600$ tumors. Gene A lies in an early-replicating, expressed region with a background rate of $0.5$ per megabase, gene B in a late-replicating region with $3$ per megabase. Each has $6$ mutations. Compute the Poisson p-values and discuss which is the better candidate driver. What additional evidence would you look at?

   **Answer** $\lambda_A = 1200 \times 600 \times 0.5 \times 10^{-6} = 0.36$, $\mathbb{P}(X \ge 6) = 1 - \sum_{x \le 5}\mathrm{e}^{-0.36}0.36^x/x! \approx 2.2 \times 10^{-6}$. $\lambda_B = 2.16$, $\mathbb{P}(X \ge 6) \approx 0.023$. Gene A is a strong candidate (it passes a Bonferroni threshold for $18\,000$ genes, $2.8 \times 10^{-6}$, narrowly), gene B is not significant genome-wide although it has the same count. Additional evidence: the ratio of non-synonymous to synonymous mutations (dN/dS) in each gene, which calibrates the local rate internally; the pattern of mutations (clustering at hotspots for an oncogene, truncating mutations for a tumor suppressor); the functional impact predicted for the missense changes; expression of the gene in the tissue (a gene not expressed is unlikely to be a driver); and replication in an independent cohort.

6. Show that if a gene's somatic rate per tumor is gamma-distributed across genes with mean $\lambda$ and coefficient of variation $c$, the count is negative binomial with variance $\lambda + c^2\lambda^2$. Using Example 13.4.1 ($\lambda = 0.75$, $8$ mutations), how large must $c$ be for $p$ to exceed $10^{-3}$?

   **Answer** If $X \mid \Lambda \sim \mathrm{Poi}(\Lambda)$ and $\Lambda \sim \Gamma(\alpha, \beta)$ with mean $\alpha/\beta = \lambda$ and variance $\alpha/\beta^2 = c^2\lambda^2$, then $X$ is negative binomial with $\mathbb{E}X = \lambda$ and $\operatorname{Var}X = \mathbb{E}\operatorname{Var}(X \mid \Lambda) + \operatorname{Var}\mathbb{E}(X \mid \Lambda) = \lambda + c^2\lambda^2$ (law of total variance). The upper tail at $8$ grows with $c$: numerically, $\mathbb{P}(X \ge 8)$ with $\lambda = 0.75$ is $1.3 \times 10^{-6}$ for $c = 0$, $4.1 \times 10^{-5}$ for $c = 0.5$, $2.0 \times 10^{-4}$ for $c = 0.7$ and $1.1 \times 10^{-3}$ for $c = 1$; $p$ exceeds $10^{-3}$ for $c$ above about $0.97$, a gene-to-gene variation of the rate by a factor of about two. Already $c = 0.5$ raises $p$ thirtyfold, above the Bonferroni threshold of Example 13.4.1. Overdispersion of this size turns a genome-wide discovery into an unremarkable count, which is why the background model matters more than the test.

7. In Example 13.5.1, propagation increased the similarity of tumors of the same subtype but also that of tumors of different subtypes (from $0.05$ to $0.31$). Why? What happens as the restart probability $r$ goes to $0$ and to $1$?

   **Answer** Propagation spreads every profile over the network; the two pathways are connected by a few edges and share the gray genes, so some heat from each tumor reaches the other pathway, and all smoothed profiles share a component proportional to the stationary distribution of the walk, which raises all similarities. As $r \to 1$, there is no propagation ($\boldsymbol{p} = \boldsymbol{p}_0$) and the profiles stay as sparse and dissimilar as the raw ones. As $r \to 0$, every profile converges to the stationary distribution of the random walk (proportional to degree), and all tumors become identical: subtype information is lost. Intermediate values (around $0.3$ to $0.5$) smooth within pathways before the heat reaches the rest of the network; the choice can be made by the stability of the resulting clusters, as in the consensus step of Algorithm 13.5.1.

8. A study selects $50$ prognostic genes from $20\,000$ by their association with survival in $120$ patients, builds a risk score, splits the same patients at the median score and reports a log-rank $p = 10^{-6}$. List the problems and describe a valid evaluation.

   **Answer** The genes were selected on the same patients, so the score is guaranteed to separate them (resubstitution), as in Example 13.6.1; the p-value has no meaning as evidence of prognostic value. Additional problems: no comparison with standard clinical variables and proliferation markers (random gene sets are often prognostic, 13.6.3); possible choice among many scoring methods or cutpoints. A valid evaluation: (i) pre-specify the selection and scoring procedure; (ii) estimate its performance by cross-validation in which gene selection and score construction are repeated within each fold, and compute the cross-validated risk groups or the cross-validated concordance index; (iii) assess significance by permuting survival times and repeating the entire procedure; (iv) test the fixed score in an independent cohort, as a continuous covariate in a Cox model adjusted for stage and other clinical predictors; and (v) compare with a proliferation score and with random gene sets of the same size.

9. Cell lines with a mutation in gene $M$ have a mean CRISPR gene effect of $-0.9$ for gene $D$ ($n = 25$, standard deviation $0.3$), against $-0.3$ in other lines ($n = 800$, standard deviation $0.3$). The comparison is one of $10^4$ genes times $500$ features. Is the dependency significant, and what confounders would you check?

   **Answer** Welch $t = (-0.9 + 0.3)/\sqrt{0.09/25 + 0.09/800} = -0.6/\sqrt{0.0036 + 0.0001125} = -0.6/0.0609 = -9.85$, with about $25.5$ degrees of freedom (Welch–Satterthwaite): $p \approx 4 \times 10^{-10}$. The number of tests is $5 \times 10^6$, so the Bonferroni threshold is $10^{-8}$: significant. Confounders: lineage (if $M$ is mutated mostly in one tissue whose lines generally depend on $D$, the association reflects lineage; test within lineages or include lineage as a covariate); copy number at $D$ (cutting in amplified regions reduces proliferation regardless of the gene); mutational burden and microsatellite instability (hypermutated lines carry many mutations, including in $M$, and share dependencies such as WRN); and screen quality and growth rate. Confirm with independent guides, RNA interference or a small-molecule inhibitor, and by introducing or correcting the mutation in isogenic lines.

10. (Design problem) Outline a systems-biology study to explain why some patients with a given cancer respond to immune checkpoint blockade and others do not, using pre-treatment tumor samples from a trial. Specify the data, the analyses and the safeguards against false discoveries.

    **Answer** Data: whole-exome sequencing of tumor and normal (TMB, clonality of mutations, neoantigen prediction with the patient's HLA types, loss of HLA heterozygosity, mutations in antigen presentation and interferon signaling such as *B2M*, *JAK1*/*JAK2*), RNA-seq (expression subtypes, immune deconvolution, interferon-γ signatures, regulon activities of key factors), multiplexed imaging or spatial transcriptomics on a subset (T-cell location relative to tumor cells), and clinical covariates (stage, prior treatment, performance status), with response and survival as outcomes. Analyses: pre-specified primary hypotheses (TMB, clonal neoantigen load, T-cell inflammation) tested with adjustment for covariates; an integrated predictor built with penalized regression or tree ensembles, evaluated by nested cross-validation with all feature selection inside the folds; mutational signatures (mismatch repair, tobacco, UV) as interpretable features; network analyses linking alterations in non-responders to pathways (propagation of mutations over interaction networks, master regulator analysis of the non-responder signature). Safeguards: control of the false discovery rate across exploratory features; no optimal cutpoints; comparison with simple baselines (TMB alone); validation in an independent trial cohort; and experimental tests of mechanisms (for example knocking out candidate genes in tumor cells in syngeneic mouse models treated with checkpoint blockade, or in vivo CRISPR screens).
