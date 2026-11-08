---
title: Analysis of Population Genomic Data
description: "Processing genotypes of many individuals at scale. Arrays and sequencing, the genotype matrix, PLINK 1 binary files (2-bit encoding) and PLINK 2. Sample quality control (sex check from X-chromosome inbreeding, missingness, heterozygosity, contamination) and relatedness (identity by state and by descent, the KING-robust kinship estimator, degree thresholds, removing related individuals); variant quality control (call rate, minor allele frequency, the exact Hardy–Weinberg test, LD pruning). Population structure: PCA of standardized genotypes, the genetic relationship matrix, the detection threshold of structure, projection onto reference panels; the ADMIXTURE model fitted by EM; f-statistics and ancient DNA. Haplotype phasing and genotype imputation with the Li–Stephens hidden Markov model, dosages and the imputation R². Association at biobank scale: residualized single-variant tests, linear mixed models (EMMAX, BOLT-LMM, REGENIE), LD clumping and summary statistics. Differentiation and selection scans: Hudson's F_ST, extended haplotype homozygosity and iHS, the lactase region."
---

A study of one genome ends with a list of variants ([7.8.12](/7.8.12)); a study of a population begins with the same list for thousands or millions of people, and with the computational problems this creates. The statistics of population genetics and of association mapping were developed in genetics: **Hardy–Weinberg equilibrium**, **linkage disequilibrium** and the **fixation index** in [7.4.22](/7.4.22), selection and drift in [7.4.23](/7.4.23), and the **genome-wide association study** with its tests, thresholds, stratification, fine-mapping and polygenic scores in [7.4.25](/7.4.25). This chapter does not repeat them. It is about the data and the computation: how genotypes of many individuals are stored, cleaned and checked for errors, sample swaps and relatives; how the genetic structure of a sample is measured by principal components and ancestry models; how unobserved genotypes are filled in from reference panels with a **hidden Markov model**; how association is computed for $10^5$–$10^6$ people and $10^7$ variants; and how differentiation and selection are scanned along the genome. The running examples are the lactase persistence variant rs4988235 in *MCM6* ([7.8.2](/7.8.2#sec-2.4)), whose frequencies in the continental groups of the 1000 Genomes Project and whose long haplotype are a textbook signal of selection ([7.4.23](/7.4.23#sec-23.8.2)), and the merging of one person's genotypes with the 1000 Genomes samples to place that person on a map of human variation. The general statistics used here (mixed models, multiple testing) belong to biostatistics ([7.7.17](/7.7.17), [7.7.20](/7.7.20)), and the mathematics of principal components to multivariate analysis ([3.4.5](/3.4.5)).

## 13.1. Genotype Data

### 13.1.1. Arrays and Sequencing

Population-scale genotypes come from two technologies. *Genotyping arrays* carry probes for a fixed set of $0.5$–$2\times10^6$ **single nucleotide polymorphisms**; the two allele-specific signals of each sample form clusters (two homozygous and one heterozygous) that a clustering algorithm turns into genotype calls. Arrays cost tens of dollars per sample and are the basis of biobanks, consumer genetics and most published GWAS, but they see only the chosen variants, mostly common ones, and rare variants or those absent from the design must be imputed (§13.4). *Sequencing* (whole genome, exome, or low-pass genomes at $0.5$–$4\times$, [7.8.9](/7.8.9#sec-9.6)) finds all variants, including rare ones, and is processed into VCF files by joint calling ([7.8.12](/7.8.12)). Whichever the source, the analysis works with the same object.

**Definition 13.1.1 (Genotype Matrix)** The **genotype matrix** of $n$ diploid individuals at $m$ biallelic variants is the $n\times m$ matrix $G$ whose entry $g_{ij} \in \{0, 1, 2\}$ is the number of copies of a designated allele (the alternative or the minor allele) carried by individual $i$ at variant $j$, with a code for missing genotypes; after imputation (§13.4) the entries are *dosages* $g_{ij} \in [0, 2]$, the expected allele counts.

For a biobank, $n \approx 5\times10^5$ and $m \approx 10^7$ after imputation, so $G$ has $5\times10^{12}$ entries: the matrix does not fit in memory, every algorithm must stream over it, and an operation costing more than $O(nm)$ is usually out of reach.

### 13.1.2. PLINK Formats

The program PLINK (Purcell and colleagues 2007; PLINK 1.9 and PLINK 2, Chang and colleagues 2015) defined the formats in which most genotype data are exchanged. The text format consists of a *PED* file (one line per individual: family ID, individual ID, father, mother, sex, phenotype and then two allele columns per variant) and a *MAP* file (one line per variant: chromosome, identifier, genetic position, base-pair position). Text is slow and large, so analyses use the binary fileset:

| File | Content | One line per |
|---|---|---|
| `.fam` | family ID, individual ID, father, mother, sex (`1` male, `2` female, `0` unknown), phenotype (`1` control, `2` case, `-9` or `0` missing, or a quantitative value) | individual |
| `.bim` | chromosome, variant ID, position in cM (often `0`), base-pair position, allele 1 (usually minor), allele 2 | variant |
| `.bed` | the genotypes in binary | — (variant-major blocks) |

**Formula 13.1.1 (PLINK 1 Binary Genotypes)** A `.bed` file begins with the three bytes `0x6C 0x1B 0x01` and then stores, for each variant in the order of the `.bim` file, the genotypes of the $n$ individuals in the order of the `.fam` file at $2$ bits each, four per byte starting from the low-order bits: `00` homozygous for allele 1, `01` missing, `10` heterozygous, `11` homozygous for allele 2. Each variant occupies $\lceil n/4\rceil$ bytes, so the file has $3 + m\lceil n/4\rceil$ bytes.

**Example 13.1.1** For $n = 5\times10^5$ individuals and $m = 8\times10^5$ array SNPs the `.bed` file has $10^{11}$ bytes ($100\,\mathrm{GB}$), and any variant can be read by seeking to byte $3 + j\lceil n/4\rceil$. An uncompressed VCF of the same genotypes, with at least four characters (`0/1` and a tab) per genotype, would exceed $1.6\,\mathrm{TB}$. PLINK 2's `.pgen` format compresses further by storing each variant relative to a similar earlier one (linkage disequilibrium makes neighboring variants alike), and adds dosages, phase and multiallelic variants; `.pvar` and `.psam` replace `.bim` and `.fam`.

```bash
# VCF (from joint calling or an imputation server) to PLINK 2 and PLINK 1 binary filesets
plink2 --vcf cohort.vcf.gz --set-all-var-ids '@:#:$r:$a' --max-alleles 2 --make-pgen --out cohort
plink2 --pfile cohort --make-bed --out cohort      # .bed/.bim/.fam for tools that need PLINK 1 files
```

The `--set-all-var-ids` option names each variant chromosome:position:ref:alt, because rs identifiers are missing for new variants and can change between dbSNP releases ([7.8.2](/7.8.2)). Merging data sets requires the same **reference genome** build and the same strand and allele coding at every variant, the harmonization problem of §13.5.4.

## 13.2. Quality Control

Errors in genotype data arise at every step: sample collection (mislabeled tubes, relatives recruited as unrelated, individuals of different ancestry), laboratory handling (plates swapped, DNA contaminated), the assay (poorly clustering probes, batches processed differently) and calling. A single bad SNP can produce a spurious genome-wide significant association, and a single contaminated sample can distort many. Quality control (QC) is therefore done systematically, first on samples and then on variants: removing a variant removes a potential discovery for every individual, whereas removing an individual costs only a fraction of the sample, so poor samples are removed first so that they do not drag good variants below the thresholds.

### 13.2.1. Sample Quality Control

*Sex check.* Men carry one X chromosome, so outside the **pseudoautosomal regions** they cannot be heterozygous at X-linked SNPs. The genetic sex inferred from X-chromosome homozygosity is compared with the reported sex; a discordance indicates a sample swap or a labeling error (and, rarely, a sex-chromosome aneuploidy or a person whose gender differs from the recorded sex, which must be handled with care).

**Formula 13.2.1 (Method-of-Moments Inbreeding Estimate)** For individual $i$ with $N_i$ non-missing genotypes at a set of SNPs with allele frequencies $p_j$, observed number of homozygous genotypes $O_i$ and expected number $E_i = \sum_j (1 - 2p_j(1 - p_j))$ under Hardy–Weinberg proportions,

$$
\hat F_i = \frac{O_i - E_i}{N_i - E_i}.
$$

It estimates the **inbreeding coefficient** of [7.4.7](/7.4.7#sec-7.5.1): $\hat F_i = 0$ for the homozygosity expected in a random-mating population, $1$ when every genotype is homozygous. On the X chromosome, PLINK's sex check calls an individual male if $\hat F > 0.8$ and female if $\hat F < 0.2$.

**Example 13.2.1** At $N = 10\,000$ non-missing X-chromosome SNPs whose allele frequencies give $E = 7000$ expected homozygotes, a sample with $O = 9990$ homozygous genotypes has $\hat F = 2990/3000 = 0.997$ (male; the $10$ heterozygous calls are genotyping errors), and one with $O = 7100$ has $\hat F = 0.033$ (female). If the first sample is recorded as female, it is flagged.

*Missingness and heterozygosity.* A sample whose DNA was degraded or too dilute fails at many SNPs; samples missing more than $2$–$5\,\%$ of genotypes are removed. The heterozygosity rate $(N_i - O_i)/N_i$ over autosomal SNPs (pruned for linkage disequilibrium, §13.2.3) has a narrow distribution among good samples: a higher rate indicates contamination by DNA of a second person (a mixture of two genotypes looks heterozygous wherever they differ), a lower rate indicates **consanguinity** or a sample from a population with less diversity than the rest. Samples outside the mean $\pm3$ standard deviations are inspected and usually removed. Contamination can also be estimated directly from the allele fractions in sequencing reads (VerifyBamID) or in the array intensities.

![Sample quality control (simulated, 2000 individuals). A: heterozygosity rate against missing genotype rate. Typical samples (gray) form a tight cloud; contaminated samples (red) have excess heterozygosity; samples from consanguineous unions (purple) have reduced heterozygosity, by a fraction equal to their inbreeding coefficient (1/16, 1/8 or 1/4); partly failed samples (yellow) have missing rates above 3 %. The dashed lines are the exclusion rules (missing rate ≥ 3 %, heterozygosity outside the mean ± 3 SD); they remove 29 samples, all 10 contaminated and 12 failed samples and 7 of the 12 consanguineous ones (the children of first cousins, F = 1/16, remain inside the band). B: the X-chromosome estimate F for reported males and females, with the thresholds 0.2 and 0.8; one reported female has F near 1 and one reported male F near 0, as after a swap of two samples](./plots/sample-qc.py)

### 13.2.2. Relatedness

Most analyses assume unrelated individuals: relatives share long segments of their genomes **identical by descent**, so their genotypes are not independent observations, and a duplicated sample counts one person twice. Relationships are inferred from the genotypes themselves.

Two alleles are *identical by state* (IBS) if they are the same base, and identical by descent (IBD) if they are copies of one ancestral allele ([7.4.7](/7.4.7#sec-7.5.1)). At each SNP a pair of individuals shares $0$, $1$ or $2$ alleles IBD with probabilities $(k_0, k_1, k_2)$ that depend only on their relationship; the **kinship coefficient** is $\varphi = k_1/4 + k_2/2$.

| Relationship | $(k_0, k_1, k_2)$ | $\varphi$ | Degree |
|---|---|---|---|
| duplicate, monozygotic twins | $(0, 0, 1)$ | $1/2$ | — |
| parent–offspring | $(0, 1, 0)$ | $1/4$ | first |
| full siblings | $(1/4, 1/2, 1/4)$ | $1/4$ | first |
| half-siblings, grandparent, avuncular | $(1/2, 1/2, 0)$ | $1/8$ | second |
| first cousins | $(3/4, 1/4, 0)$ | $1/16$ | third |
| unrelated | $(1, 0, 0)$ | $0$ | — |

PLINK 1.9 estimates $(k_0, k_1, k_2)$ by the method of moments from IBS counts and the sample allele frequencies, and reports $\hat\pi = \hat k_1/2 + \hat k_2 = 2\hat\varphi$. The estimate depends on the allele frequencies being right for both individuals, so in a sample of mixed ancestry it is biased: two unrelated people of the same minority ancestry share more alleles than the pooled frequencies predict and appear related. The KING estimators (Manichaikul and colleagues 2010) avoid allele frequencies altogether.

**Formula 13.2.2 (KING-Robust Kinship Estimator)** For individuals $i$ and $j$ typed at the same SNPs, let $N_{\mathrm{het},\mathrm{het}}$ be the number of SNPs at which both are heterozygous, $N_{\mathrm{IBS0}}$ the number at which they are opposite homozygotes ($AA$ and $aa$), and $N^{(i)}_{\mathrm{het}}$, $N^{(j)}_{\mathrm{het}}$ the numbers of heterozygous SNPs of each. Then

$$
\hat\varphi_{ij} = \frac{N_{\mathrm{het},\mathrm{het}} - 2N_{\mathrm{IBS0}}}{N^{(i)}_{\mathrm{het}} + N^{(j)}_{\mathrm{het}}}.
$$

For unrelated individuals in Hardy–Weinberg proportions at a SNP with allele frequency $p$, both are heterozygous with probability $(2pq)^2 = 4p^2q^2$ and opposite homozygotes with probability $2p^2q^2$, so the numerator has expectation $0$; for duplicates $N_{\mathrm{het},\mathrm{het}} = N_{\mathrm{het}}$ and $N_{\mathrm{IBS0}} = 0$, giving $1/2$. Because each pair is compared through its own heterozygosity, the estimate does not use population allele frequencies and remains approximately unbiased for related pairs within one ancestry group in a structured sample. KING assigns degrees by thresholds at the geometric midpoints between the expected kinships: $\hat\varphi > 2^{-3/2} = 0.354$ duplicates, $(0.177, 0.354]$ first degree, $(0.088, 0.177]$ second, $(0.044, 0.088]$ third. Parent–offspring pairs, who always share one allele IBD, have $N_{\mathrm{IBS0}} \approx 0$, which separates them from full siblings with the same $\varphi$.

**Example 13.2.2** Two samples have $N^{(i)}_{\mathrm{het}} = 205\,000$ and $N^{(j)}_{\mathrm{het}} = 195\,000$ heterozygous SNPs, $N_{\mathrm{het},\mathrm{het}} = 102\,000$ and $N_{\mathrm{IBS0}} = 1000$. Then $\hat\varphi = (102\,000 - 2000)/400\,000 = 0.25$: a first-degree pair. The small but nonzero IBS0 count could be genotyping error in a parent–offspring pair or a full-sib pair; with $m \approx 10^6$ SNPs of mean opposite-homozygote probability $\overline{2p^2q^2} \approx 0.07$ (frequencies spread between $0.05$ and $0.5$), unrelated pairs have IBS0 at about $7\,\%$ of SNPs and full siblings at a quarter of that, so a count of $1000$ ($0.1\,\%$ of the SNPs) indicates parent and child.

![Relationship inference from genotypes (simulated: 20 000 independent SNPs; pairs of six relationships drawn with their IBD probabilities). Each point is a pair: the KING-robust kinship (Formula 13.2.2) against the fraction of SNPs at which the two are opposite homozygotes. Relationships of different degree separate along the kinship axis at 1/2, 1/4, 1/8, 1/16 and 0; dashed lines are the KING thresholds. Parent–offspring and full-sib pairs have the same kinship but differ in IBS0 (zero for parent and child, a quarter of the unrelated value for siblings). On real chromosomes IBD is shared in long segments, which spreads each cloud more than here](./plots/kinship.py)

Removing relatives requires choosing which members of related groups to drop. The pairs above a threshold define a graph on the individuals ([1.4.1](/1.4.1)), and the largest unrelated subset is a maximum independent set of this graph, a problem that is NP-hard in general. PLINK 2's `--king-cutoff` uses a greedy rule: repeatedly remove the individual involved in the most remaining related pairs. Biobank analyses with mixed models (§13.5.2) keep the relatives instead and model their correlation, which preserves sample size.

### 13.2.3. Variant Quality Control

After sample QC, variants are filtered:

- *Call rate.* Variants missing in more than $2$–$5\,\%$ of samples are removed; so are variants whose missing rate differs between cases and controls (a test of differential missingness), because missingness correlated with phenotype creates false associations.
- *Minor allele frequency.* Rare variants on arrays are poorly called, since their heterozygote cluster is small and the homozygous minor cluster may be empty; filters of $1$–$5\,\%$ are common for array data, lower for sequencing.
- *Hardy–Weinberg proportions.* Calling errors distort genotype frequencies, typically by merging heterozygotes into a homozygous cluster, which creates a heterozygote deficit. A strong departure from Hardy–Weinberg proportions in controls ($p < 10^{-6}$ or so) flags a variant ([7.4.22](/7.4.22#sec-22.2.2)); in cases, departures can reflect true association and are not used for filtering.

The χ² test of Hardy–Weinberg proportions is unreliable when an expected genotype count is small, the rule for low-frequency variants; genotyping pipelines use the exact test ([Remark 22.2.1](/7.4.22#rem-22.2.1)), which conditions on the allele counts.

**Formula 13.2.3 (Exact Test of Hardy–Weinberg Proportions)** In a sample of $n$ individuals with $n_A$ copies of allele $A$ and $n_B = 2n - n_A$ of $B$, the probability under Hardy–Weinberg proportions of observing $n_{AB}$ heterozygotes (with $n_{AA} = (n_A - n_{AB})/2$ and $n_{BB} = (n_B - n_{AB})/2$) is

$$
\mathbb{P}(n_{AB} \mid n, n_A) = \frac{2^{n_{AB}}\, n!\, n_A!\, n_B!}{n_{AA}!\, n_{AB}!\, n_{BB}!\, (2n)!},
$$

for $n_{AB}$ of the same parity as $n_A$. The $p$-value is the sum of the probabilities of all values of $n_{AB}$ that are no more probable than the observed one (Wigginton and colleagues 2005). The probabilities can be computed by a recurrence from the mode in $O(\min(n_A, n_B))$ time.

**Example 13.2.3** Among $n = 1000$ controls a SNP has $980$ $AA$, $18$ $AB$ and $2$ $BB$ genotypes, so $\hat p_B = 0.011$ and the expected counts are $978.1$, $21.8$ and $0.12$. The χ² statistic is $29.8$ with $p = 4.7\times10^{-8}$, driven entirely by the expected count of $0.12$ for $BB$; the exact test gives $p = 0.0052$, a mild departure that would not be filtered at $10^{-6}$. For a common SNP with $300$, $400$ and $300$ genotypes (expected $250$, $500$, $250$) both tests give $p = 2.3\times10^{-10}$ and $2.5\times10^{-10}$: a heterozygote deficit of this size in controls almost always means that the heterozygote cluster was miscalled.

*LD pruning.* Analyses that treat SNPs as independent pieces of evidence (heterozygosity, kinship, PCA) are dominated by regions of high linkage disequilibrium if all SNPs are used. *Pruning* keeps an approximately independent subset: in windows of, say, $50$ SNPs moved by $5$, any pair with $r^2 > 0.2$ loses one member. Long-range LD regions (the major histocompatibility complex on chromosome 6, inversions on 8p23 and 17q21) are excluded altogether, because otherwise they produce principal components that describe a single locus rather than ancestry.

```bash
# Sample QC (PLINK 1.9 for the sex check), then PLINK 2
plink  --bfile cohort --check-sex --out qc/sex                      # F on chrX; PROBLEM rows are discordant
plink2 --pfile cohort --missing --out qc/miss                       # .smiss (samples), .vmiss (variants)
plink2 --pfile cohort --indep-pairwise 50 5 0.2 --exclude range long_range_ld.txt --out qc/prune
plink2 --pfile cohort --extract qc/prune.prune.in --het --out qc/het
plink2 --pfile cohort --extract qc/prune.prune.in --king-cutoff 0.0884 --out qc/unrel   # drop 2nd degree and closer
# Variant QC on the retained samples
plink2 --pfile cohort --keep qc/unrel.king.cutoff.in.id --remove qc/fail_samples.txt \
       --geno 0.02 --maf 0.01 --hwe 1e-6 --make-pgen --out cohort_qc
```

Batch effects deserve a separate check: samples processed on different plates, arrays or sequencing centers can differ systematically in call rates and allele frequencies at some SNPs. Testing each SNP for association with batch (as if batch were a phenotype) and removing those with significant differences protects the later association scan, especially when cases and controls were genotyped separately.

## 13.3. Population Structure

### 13.3.1. Principal Components of Genotypes

Allele frequencies differ among human populations because of their separate histories of drift, migration and admixture ([7.4.23](/7.4.23)), and the differences are spread over the whole genome. **Principal component analysis** of the genotype matrix summarizes them in a few coordinates (Cavalli-Sforza's maps of human variation; Price, Patterson and colleagues 2006). It is used to detect individuals of divergent ancestry, to describe the structure of a population, and to correct association tests for **population stratification** ([7.4.25](/7.4.25#sec-25.3.3)).

**Definition 13.3.1 (Standardized Genotypes and Genetic Relationship Matrix)** With $\hat p_j$ the sample frequency of the counted allele at variant $j$, the standardized genotype matrix $Z$ has entries

$$
z_{ij} = \frac{g_{ij} - 2\hat p_j}{\sqrt{2\hat p_j(1 - \hat p_j)}},
$$
and the **genetic relationship matrix** (GRM) is the $n\times n$ matrix $K = ZZ^{\mathsf T}/m$. Its entry $K_{ii'}$ estimates twice the kinship of individuals $i$ and $i'$ relative to the sample, and its diagonal estimates $1 + F_i$. Genotype principal components are the leading eigenvectors of $K$, equivalently the left singular vectors of $Z$ ([3.4.6](/3.4.6#sec-6.1.3)).

Standardizing by $\sqrt{2p(1-p)}$, the binomial standard deviation under Hardy–Weinberg proportions, gives every SNP unit variance, so rare variants weigh as much as common ones (whether this is desirable is debated; it is the convention of EIGENSOFT and GCTA). Computing all eigenvectors costs $O(n^2m)$, too much for biobanks; only the top $10$–$20$ are needed, and randomized or Lanczos algorithms find them in $O(nmk)$ time for $k$ components (FlashPCA, PLINK 2's `--pca approx`).

How much structure does PCA detect? Under the null of no structure, the eigenvalues of $K$ follow the Marchenko–Pastur law of random-matrix theory, with upper edge $(1 + \sqrt{n/m})^2$ for $n$ individuals and $m$ independent SNPs. An eigenvalue above the edge indicates structure, and its significance is tested with the Tracy–Widom distribution of the largest eigenvalue (Patterson and colleagues 2006, implemented in EIGENSOFT). The same theory gives a phase transition: two populations are distinguishable by PCA only if $F_{\mathrm{ST}} > 1/\sqrt{nm}$, roughly. With $n = 1000$ individuals and $m = 10^5$ SNPs the threshold is $10^{-4}$, far below the differentiation of $F_{\mathrm{ST}} \approx 0.1$ between continental groups and below that of most neighboring populations within a continent. Large data sets therefore reveal fine structure, as between regions of one country, that no single SNP could show.

**Example 13.3.1** The figure shows three simulated populations, each derived from a common ancestral population with divergence $F = 0.05$, $0.08$ and $0.12$, and $40$ individuals admixed between the first two. With $n = 340$ and $m = 5000$ SNPs, the Marchenko–Pastur edge is $(1 + \sqrt{340/5000})^2 = 1.59$. The two leading eigenvalues are $21.8$ and $14.1$, the third ($1.5$) lies below the edge: $K = 3$ populations produce $K - 1 = 2$ informative components. Admixed individuals lie on the segment between their two source populations, at a position proportional to their ancestry proportion, because their expected genotypes are the corresponding mixtures of the source frequencies.

![Genotype PCA of simulated data (Balding–Nichols model, 5000 SNPs): three populations of 100 individuals with divergence F = 0.05, 0.08 and 0.12 from a common ancestral population, and 40 individuals admixed between populations 1 and 2, colored by their true proportion of ancestry from population 1 (dark 0, yellow 1). A: the first two principal components of the standardized genotypes; admixed individuals lie between their sources. B: the leading eigenvalues of ZZᵀ/m on a log scale against the upper edge of the Marchenko–Pastur law for unstructured data (dashed): two eigenvalues stand far above it](./plots/genotype-pca.py)

Interpreting principal components requires care. The components reflect the genealogy of the sample (McVean 2009): the average coalescence times within and between groups. They depend on the composition of the sample, so an over-represented population dominates the top components; a group of relatives or a long-range LD region can produce its own component; and continuous gradients of variation, such as isolation by distance, appear as arcs and horseshoes that do not mean discrete groups. A PCA map of European genomes resembles the geographic map of Europe (Novembre and colleagues 2008) because genetic similarity decays with distance, not because PCA knows geography.

*Projection onto a reference.* A new sample, or a study cohort, is placed in the coordinate system of a reference panel by computing the reference principal components and multiplying the new standardized genotypes by the reference SNP loadings. This is how a person's genotypes merged with the 2504 individuals of the 1000 Genomes Project are compared with the five continental groups, and how cohorts are screened for individuals of divergent ancestry. Projected samples are *shrunk* towards the origin relative to the reference samples, because the reference samples contributed to their own components and the projected ones did not; the shrinkage grows with $n/m$, and EIGENSOFT and other tools correct it.

```bash
# One genome among the 1000 Genomes samples: merge, prune, compute PCs, project
plink --bfile kgp_hg38 --bmerge me --make-bed --out merged_b   # PLINK 1.9 merge; same build and alleles first
plink2 --bfile merged_b --make-pgen --out merged
plink2 --pfile merged --maf 0.05 --indep-pairwise 50 5 0.2 --out pr
plink2 --pfile merged --keep kgp_samples.txt --extract pr.prune.in --freq counts --pca allele-wts 10 --out ref
plink2 --pfile merged --keep me.id --read-freq ref.acount --score ref.eigenvec.allele 2 6 header-read \
       no-mean-imputation variance-standardize --score-col-nums 7-16 --out me_proj
```

### 13.3.2. Ancestry Proportions: the ADMIXTURE Model

PCA describes structure geometrically; a likelihood model describes it as ancestry from a few source populations. The model of STRUCTURE (Pritchard, Stephens and Donnelly 2000) and of the faster maximum-likelihood program ADMIXTURE (Alexander and colleagues 2009) is the same:

**Definition 13.3.2 (Admixture Model)** In **admixture analysis**, each individual $i$ has ancestry proportions $q_{i1}, \dots, q_{iK} \geq 0$ with $\sum_k q_{ik} = 1$ from $K$ ancestral populations, and each population $k$ has allele frequencies $f_{kj}$. Each of the two allele copies of individual $i$ at SNP $j$ independently comes from population $k$ with probability $q_{ik}$ and is then the counted allele with probability $f_{kj}$, so that

$$
g_{ij} \sim \mathrm{Bin}\Bigl(2, \sum_{k=1}^K q_{ik}f_{kj}\Bigr), \qquad \ln L(Q, F) = \sum_{i,j}\Bigl[g_{ij}\ln \sum_k q_{ik}f_{kj} + (2 - g_{ij})\ln\Bigl(1 - \sum_k q_{ik}f_{kj}\Bigr)\Bigr].
$$

**Algorithm 13.3.1 (EM for the Admixture Model)** The ancestral origin of each allele copy is a latent variable, so the **EM algorithm** applies. Starting from initial $Q$ and $F$:

1. E-step: for each $i, j, k$, the expected numbers of counted and uncounted allele copies of $i$ at $j$ that come from population $k$ are
   $$
   a_{ijk} = g_{ij}\frac{q_{ik}f_{kj}}{\sum_l q_{il}f_{lj}}, \qquad b_{ijk} = (2 - g_{ij})\frac{q_{ik}(1 - f_{kj})}{\sum_l q_{il}(1 - f_{lj})}.
   $$
2. M-step: $q_{ik} \leftarrow \sum_j (a_{ijk} + b_{ijk})/(2m)$ and $f_{kj} \leftarrow \sum_i a_{ijk}/\sum_i (a_{ijk} + b_{ijk})$.
3. Repeat until the log-likelihood stops increasing.

Each iteration costs $O(nmK)$ and increases the likelihood, but EM converges slowly when the parameters are many and weakly determined; ADMIXTURE uses block relaxation (alternately optimizing $Q$ and $F$ by sequential quadratic programming) with quasi-Newton acceleration, and missing genotypes are simply omitted from the sums. The likelihood has local maxima, so several random starts are compared.

![Ancestry proportions estimated by maximum likelihood (Algorithm 13.3.1, accelerated by SQUAREM and started from k-means on the leading principal components) on the simulated genotypes of the PCA figure (first 2000 SNPs). Each bar is one individual divided into its estimated ancestry components; individuals are ordered by population and, among the admixed individuals, by their true proportion from population 1. A: with K = 2, populations 1 and 2 share a component and population 1 appears as a 70:30 mixture, an artifact of too small a K. B: K = 3 separates the three sources, and the estimated proportions of the admixed individuals correlate with the true ones at r = 0.984](./plots/admixture.py)

The number $K$ is a modeling choice. ADMIXTURE estimates prediction error by cross-validation (holding out genotypes and predicting them) and the $K$ with the smallest error is a reasonable choice, but results for several $K$ are usually shown together, as in the figure. The components are not real populations: a population that went through a strong bottleneck, and so drifted far, tends to receive its own component whatever its history, and the same bar plot can arise from different histories (recent admixture, continuous gene flow, or a source population that was not sampled), so ancestry proportions are a summary of the data under a simple model, not a reconstruction of history (Lawson and colleagues 2018). The same caution applies to consumer "ancestry percentages", which depend on the reference populations chosen.

### 13.3.3. f-Statistics and Ancient DNA

Explicit tests of population history use allele-frequency correlations among populations, the *f-statistics* of Patterson and colleagues (2012). For populations $A, B, C, D$ with frequencies $p_A, \dots$ at each SNP, averaged over SNPs:

- $f_2(A, B) = \mathbb{E}[(p_A - p_B)^2]$, the drift separating $A$ and $B$ (the numerator of $F_{\mathrm{ST}}$, §13.6.1);
- $f_3(C; A, B) = \mathbb{E}[(p_C - p_A)(p_C - p_B)]$, which is significantly negative only if $C$ is a mixture of populations related to $A$ and $B$;
- $f_4(A, B; C, D) = \mathbb{E}[(p_A - p_B)(p_C - p_D)]$, which is zero if the four are related by a tree in which the pair $(A, B)$ is separated from $(C, D)$, and nonzero if gene flow connects, say, $B$ and $C$.

Their standard errors are computed by a block jackknife over large chromosome segments, which accounts for linkage disequilibrium, and results are reported as $Z$-scores (often $\lvert Z\rvert > 3$ as evidence). Combinations of $f$-statistics fit admixture graphs and estimate mixture proportions (qpAdm in ADMIXTOOLS).

Ancient DNA ([7.4.14](/7.4.14#sec-14.6)) is analyzed with the same tools after adjustments for its special errors: molecules are short and damaged, with C→T changes near the $5'$ ends, so reads are trimmed or C/T and G/A SNPs are restricted; coverage is usually far below $1\times$, so instead of diploid genotypes a single read is sampled at each SNP (*pseudo-haploid* calls); and samples are typed at a fixed set of informative SNPs (the "1240k" capture panel) and projected onto principal components computed from modern genomes. For example, the genome of Emperor Wu of the Northern Zhou dynasty (died 578), recovered from his remains, projects among ancient Northeast Asian individuals, and $f_4$-statistics place him closest to present-day Mongolic- and Tungusic-speaking populations (Du and colleagues 2024). Time series of ancient genomes also date selection directly: the lactase persistence allele was rare in Europe until about $3000$–$4000$ years ago ([7.4.23](/7.4.23#sec-23.8.2)).

## 13.4. Haplotype Phasing and Genotype Imputation

### 13.4.1. Phasing

A genotype $g_{ij} = 1$ says that one chromosome carries the allele but not which. Many analyses need the **haplotypes**: the alleles on each of the two homologous chromosomes.

**Definition 13.4.1 (Haplotype Phasing)** **Haplotype phasing** is the inference, from the genotypes of an individual (and of others, of relatives or of sequencing reads), of the two haplotypes whose allele counts sum to its genotypes. With $H$ heterozygous sites there are $2^{H-1}$ possible pairs of haplotypes.

There are three sources of phase information. In *family-based* phasing, the alleles transmitted from each parent are determined at all sites except those where parent and child are all heterozygous. In *read-based* phasing, a sequencing read or read pair that covers two heterozygous sites reveals their phase directly; long reads phase blocks of tens to hundreds of kilobases (WhatsHap, HiFi and nanopore data; [7.8.11](/7.8.11) for phased assemblies). In *population-based* (statistical) phasing, an individual's haplotypes are inferred as mosaics of haplotypes seen in other individuals, because unrelated people share long haplotype segments inherited from distant common ancestors. Population-based methods dominate for large cohorts; the phase accuracy is measured by the *switch error rate*, the fraction of consecutive heterozygous sites whose relative phase is wrong, and improves with sample size because the shared segments become longer. Current programs (SHAPEIT5, Eagle2, Beagle 5) phase hundreds of thousands of genomes.

### 13.4.2. The Li–Stephens Model

Phasing and imputation rest on one probabilistic model.

**Formula 13.4.1 (Li–Stephens Model)** Given a panel of $K$ haplotypes $h_1, \dots, h_K$ at $m$ ordered SNPs, a new haplotype $x$ is modeled by a hidden Markov model whose hidden state $s_j \in \{1, \dots, K\}$ is the panel haplotype it copies at SNP $j$ (Li and Stephens 2003):

$$
\mathbb{P}(s_{j+1} = l \mid s_j = k) = (1 - \rho_j)\,\boldsymbol{1}[k = l] + \frac{\rho_j}{K}, \qquad \mathbb{P}(x_j \mid s_j = k) = \begin{cases} 1 - \varepsilon & x_j = h_{kj},\\ \varepsilon & x_j \neq h_{kj}.\end{cases}
$$

The switch probability $\rho_j = 1 - \exp(-4N_e r_j/K)$ grows with the genetic distance $r_j$ between SNPs $j$ and $j+1$ (recombination breaks a copied segment) and falls as the panel grows (with more haplotypes, a closer relative is available); $\varepsilon$ absorbs mutation and genotyping error.

The model approximates the coalescent with recombination: a new haplotype is, locally, closest to some existing haplotype, and the closest one changes at recombination points. It is a **hidden Markov model** of the kind treated in [4.6.8](/4.6.8), and the posterior probabilities of the hidden states come from the **forward algorithm** and the **backward algorithm** ([4.6.8](/4.6.8#sec-8.3)). A general HMM with $K$ states costs $O(mK^2)$, but here the transition is a mixture of staying and jumping uniformly, so each forward step is

$$
\alpha_{j+1}(l) = \mathbb{P}(x_{j+1} \mid l)\Bigl[(1 - \rho_j)\,\alpha_j(l) + \frac{\rho_j}{K}\sum_k \alpha_j(k)\Bigr],
$$

and the sum is computed once per SNP: the cost is $O(mK)$. With reference panels of $10^5$ haplotypes this is still too slow per individual, and practical programs restrict the states to a few hundred haplotypes most similar to the target in each region (selected with positional Burrows–Wheeler transform indexes, which find long matches in time independent of $K$; [7.8.10](/7.8.10#sec-10.2.3) for the Burrows–Wheeler transform of sequences).

For phasing, the unknown haplotypes of an individual are sampled or optimized by alternating: given a guess of the haplotypes of everyone else, each individual's pair is updated under a diploid version of the model, whose hidden state is a pair of copied haplotypes.

### 13.4.3. Imputation

**Definition 13.4.2 (Genotype Imputation)** **Genotype imputation** is the prediction of genotypes at variants not typed in a sample, from the typed variants and a reference panel of haplotypes sequenced at all variants; the result for each untyped variant is a posterior distribution over genotypes, usually summarized by its dosage, the expected allele count.

The target's phased haplotypes, observed only at array SNPs, are run through the Li–Stephens model with the reference panel; the posterior copying probabilities at the typed SNPs are interpolated to the untyped variants between them, and the imputed allele probability is the posterior-weighted average of the panel alleles there (Minimac, IMPUTE5, Beagle 5). The quality depends above all on the panel: the 1000 Genomes Project ($2504$ individuals) imputes common variants well, the Haplotype Reference Consortium ($32\,470$ individuals) and the TOPMed panel (about $10^5$ genomes, accessible through an imputation server) impute variants down to frequencies of $10^{-3}$–$10^{-4}$, and a panel must contain the ancestry of the study, so population-specific panels (such as ChinaMAP for Chinese populations) improve imputation where global panels are thin.

![Imputation with the Li–Stephens model (simulated: a panel of 24 haplotypes over 300 SNPs, built as mosaics of 6 ancestral haplotypes; the target copies panel haplotypes 3, 17 and 8 in three segments, and only every fifth SNP is typed). A: posterior copying probabilities from the forward–backward algorithm at the typed SNPs; red boxes mark the haplotypes actually copied. Haplotypes descended from the same ancestral haplotype are identical at most typed SNPs, so the posterior is shared among them; in the first segment it falls on haplotype 23, which matches the target at every typed SNP, while haplotype 3 differs at one through an error in the target. B: imputed probability of allele 1 at the 240 untyped SNPs, colored by the true allele: 97.9 % are imputed correctly, against 76.7 % for the panel's majority allele. Identity of the copied haplotype is not needed, only that its alleles agree](./plots/li-stephens.py)

**Formula 13.4.2 (Imputation Quality R²)** For an imputed variant with dosages $d_1, \dots, d_n$ and estimated allele frequency $\hat p = \bar d/2$, the estimated squared correlation between imputed and true genotypes is

$$
\hat R^2 = \frac{\operatorname{Var}(d)}{2\hat p(1 - \hat p)},
$$

the ratio of the variance of the dosages to the binomial variance expected of true genotypes. Confident imputations produce dosages near $0$, $1$ and $2$ with the full variance ($\hat R^2 \approx 1$); uninformative imputations give every individual the dosage $2\hat p$ ($\hat R^2 = 0$). A variant imputed with $\hat R^2 = r^2$ carries the information of a sample of size $r^2 n$ with true genotypes, by the same argument as for a **tag SNP** ([Formula 25.2.1](/7.4.25#fml-25.2.1)).

**Example 13.4.1** Twelve individuals have dosages $0.02, 1.0, 1.9, 0.1, 0.95, 1.05, 0.0, 2.0, 0.9, 0.15, 1.1, 0.05$. Then $\hat p = 0.384$, the variance of the dosages is $0.466$ and $2\hat p(1 - \hat p) = 0.473$, so $\hat R^2 = 0.98$. If instead all dosages lie between $0.4$ and $0.6$ (mean $0.5$, variance $0.0042$), $\hat p = 0.25$ and $\hat R^2 = 0.011$: the panel gave no information about this variant, and an association test on it would have essentially no power. Variants with $\hat R^2 < 0.3$ are usually removed, and fine-mapping uses stricter thresholds.

Association tests use the dosages directly, as a continuous predictor; the uncertainty of imputation reduces power but, if the imputation is unbiased, does not create false positives.

## 13.5. Association at Biobank Scale

The statistical design of a GWAS, the single-SNP tests, genome-wide significance, the Manhattan and QQ plots, inflation and power were given in [7.4.25](/7.4.25#sec-25.3). Here we consider what makes such analyses feasible for $n \approx 5\times10^5$ and $m \approx 10^7$.

### 13.5.1. Single-Variant Regression with Covariates

The standard model for a quantitative trait $y$ regresses it, variant by variant, on the dosage $g_j$ and covariates $X$ (intercept, sex, age, genotyping batch and $10$–$20$ principal components, §13.3.1):

$$
\boldsymbol{y} = X\boldsymbol{\beta} + \gamma_j\boldsymbol{g}_j + \boldsymbol{\varepsilon}.
$$

Fitting each regression from scratch would cost $O(nc^2)$ per variant for $c$ covariates. By the **Frisch–Waugh–Lovell theorem**, the estimate of $\gamma_j$ equals that of the regression of the residuals of $\boldsymbol{y}$ on $X$ on the residuals of $\boldsymbol{g}_j$ on $X$. So the covariates are projected out once:

**Formula 13.5.1 (Residualized Association Test)** Let $M = I - X(X^{\mathsf T}X)^{-1}X^{\mathsf T}$, $\tilde{\boldsymbol{y}} = M\boldsymbol{y}$ and $\tilde{\boldsymbol{g}}_j = M\boldsymbol{g}_j$. Then

$$
\hat\gamma_j = \frac{\tilde{\boldsymbol{g}}_j^{\mathsf T}\tilde{\boldsymbol{y}}}{\tilde{\boldsymbol{g}}_j^{\mathsf T}\tilde{\boldsymbol{g}}_j}, \qquad t_j = \hat\gamma_j\sqrt{\frac{\tilde{\boldsymbol{g}}_j^{\mathsf T}\tilde{\boldsymbol{g}}_j\,(n - c - 1)}{\tilde{\boldsymbol{y}}^{\mathsf T}\tilde{\boldsymbol{y}} - \hat\gamma_j^2\,\tilde{\boldsymbol{g}}_j^{\mathsf T}\tilde{\boldsymbol{g}}_j}},
$$

and $\tilde{\boldsymbol{g}}_j = \boldsymbol{g}_j - X[(X^{\mathsf T}X)^{-1}X^{\mathsf T}\boldsymbol{g}_j]$ costs $O(nc)$. Processing variants in blocks turns the work into matrix–matrix products, and the whole scan costs $O(nmc)$.

For $n = 5\times10^5$, $m = 10^7$ and $c = 20$ this is $10^{14}$ multiply–adds, about an hour on a multicore server: reading and decompressing the genotypes, not arithmetic, is usually the bottleneck. Binary traits use **logistic regression**, which has no closed-form solution; programs fit the null model once and compute a score test for each variant, and use Firth's penalized likelihood or a saddlepoint approximation for rare variants and unbalanced case–control ratios, where the usual asymptotic tests are badly miscalibrated.

```bash
# Linear (quantitative) or logistic (binary) regression of every variant on the phenotype, with covariates
plink2 --pfile cohort_qc --pheno pheno.tsv --pheno-name LDL --covar covar.tsv \
       --covar-name sex,age,batch,PC1-PC10 --covar-variance-standardize \
       --glm hide-covar cols=+a1freq,+beta --out gwas_ldl
```

### 13.5.2. Linear Mixed Models

Principal components remove broad ancestry but not fine structure or relatedness. **Linear mixed models** add a random genetic background shared according to the GRM ([7.7.17](/7.7.17) for mixed models in general):

$$
\boldsymbol{y} = X\boldsymbol{\beta} + \gamma_j\boldsymbol{g}_j + \boldsymbol{u} + \boldsymbol{\varepsilon}, \qquad \boldsymbol{u} \sim \mathcal{N}(\boldsymbol{0}, \sigma_g^2 K), \quad \boldsymbol{\varepsilon} \sim \mathcal{N}(\boldsymbol{0}, \sigma_\mathrm{e}^2 I),
$$

so that $\operatorname{Cov}(\boldsymbol{y}) = V = \sigma_g^2K + \sigma_\mathrm{e}^2 I$, and each variant is tested by generalized least squares. Close relatives, cryptic relatedness and fine structure all appear as covariance in $K$, so the model controls them, and by modeling the polygenic background it also increases power. The direct computation needs $V^{-1}$ or its Cholesky factor: $O(n^3)$ operations and $O(n^2)$ memory, which for $n = 5\times10^5$ means $1.25\times10^{17}$ operations and $2\,\mathrm{TB}$ for one matrix in double precision. The history of the field is a sequence of ways around this:

| Method | Idea | Cost |
|---|---|---|
| EMMAX, FaST-LMM (2010–2011) | estimate $\sigma_g^2, \sigma_\mathrm{e}^2$ once under the null; eigendecompose $K = U\Lambda U^{\mathsf T}$; rotate $\boldsymbol{y}$, $X$ and every $\boldsymbol{g}_j$ by $U^{\mathsf T}$, after which $V$ is diagonal and each test is a weighted regression | $O(n^3)$ once, $O(n^2)$ per variant for the rotation; feasible for $n \lesssim 10^5$ |
| BOLT-LMM (2015) | never form $K$: products $K\boldsymbol{v} = Z(Z^{\mathsf T}\boldsymbol{v})/m$ cost $O(nm)$, and $V^{-1}\boldsymbol{y}$ is solved by the **conjugate gradient method**; a mixture prior on SNP effects increases power | $O(nm)$ per iteration, a few dozen iterations |
| REGENIE (2021) | step 1: ridge regressions of $\boldsymbol{y}$ on blocks of SNPs, stacked into a whole-genome predictor of the polygenic background, computed leaving out each chromosome; step 2: test each variant against $\boldsymbol{y}$ minus the prediction from the other chromosomes, with Firth or saddlepoint corrections for binary traits | linear in $n$ and $m$; many phenotypes at once |

Two details matter in all of them. First, the variant under test should not be part of the background: if it contributes to $K$, the model absorbs part of its effect (proximal contamination). Hence the *leave-one-chromosome-out* (LOCO) scheme: the background for variants on chromosome $c$ is computed from the other chromosomes. Second, the background model is fitted once per phenotype, and the per-variant tests reduce to the residualized computation of Formula 13.5.1, so the scan remains $O(nm)$.

```bash
# REGENIE: step 1 fits the polygenic background on array SNPs, step 2 tests imputed variants
regenie --step 1 --bed array_qc --phenoFile pheno.tsv --covarFile covar.tsv --bt \
        --bsize 1000 --lowmem --out fit
regenie --step 2 --pgen imputed --phenoFile pheno.tsv --covarFile covar.tsv --bt \
        --pred fit_pred.list --firth --approx --bsize 400 --minINFO 0.3 --out assoc
```

### 13.5.3. From Associated Variants to Loci

A true association is accompanied by every variant in linkage disequilibrium with the causal one, so a scan reports peaks of hundreds of significant variants. *LD clumping* reduces them to approximately independent signals:

**Algorithm 13.5.1 (LD Clumping)** Given association $p$-values and LD $r^2$ among variants (from the sample or a reference panel of the same ancestry):

1. Sort the variants with $p < p_1$ (for example $5\times10^{-8}$) by increasing $p$.
2. Take the most significant remaining variant as an index variant. Assign to its clump all remaining variants within a window (say $250\,\mathrm{kb}$ or $1\,\mathrm{Mb}$) with $r^2$ above a threshold (say $0.1$) to the index variant, and remove them from the list.
3. Repeat until no variant with $p < p_1$ remains.

Clumping is greedy and depends on the thresholds; two independent causal variants in moderate LD may be merged, or one signal split. *Conditional analysis* is the model-based alternative: refit with the index variant as a covariate and look for remaining significant variants (stepwise; GCTA-COJO does this from summary statistics and an LD reference). The resulting signals are the input to **fine-mapping** ([7.4.25](/7.4.25#sec-25.4.1)).

### 13.5.4. Summary Statistics

Individual genotypes are protected data, but their summaries are not.

**Definition 13.5.1 (Summary Statistics)** The **summary statistics** of an association study are, for every tested variant, its identifier and position (with the genome build), the effect and other alleles, the effect-allele frequency, the effect estimate (a regression coefficient or log odds ratio), its standard error, the $p$-value and the sample size; they are distributed in standard formats (GWAS-SSF of the GWAS Catalog) without individual-level data.

Summary statistics are enough for most downstream analyses: meta-analysis across cohorts (inverse-variance weighting of the effect estimates, [7.7.18](/7.7.18)), LD score regression for heritability and inflation ([Eq. (25.6)](/7.4.25#eq-25.6)), fine-mapping with an LD reference, **Mendelian randomization**, and the weights of **polygenic scores**. Combining them requires *harmonization*: the same genome build (convert by liftover, [7.8.2](/7.8.2)); the same effect allele (if study 2 reports the other allele, its effect changes sign and its frequency becomes $1 - f$); and the same strand. Strand matters for *ambiguous* (palindromic) SNPs, A/T and C/G, whose alleles on the opposite strand are the same pair: an A/T SNP reported with effect allele A could mean A on either strand. If its frequency is far from $0.5$, the frequencies resolve it (frequency $0.2$ in one study and $0.8$ in the other means a flip); near $0.5$ ($0.4$–$0.6$) it cannot be resolved and such SNPs are dropped.

**Example 13.5.1** Two cohorts report a variant C/T. Cohort 1 gives effect allele T, frequency $0.30$, $\hat\beta_1 = 0.050$, $\mathrm{SE} = 0.010$; cohort 2 gives effect allele C, frequency $0.71$, $\hat\beta_2 = -0.040$, $\mathrm{SE} = 0.015$. Aligning cohort 2 to T gives frequency $0.29$ and $\hat\beta_2 = 0.040$. The inverse-variance weights are $1/0.010^2 = 10\,000$ and $1/0.015^2 = 4444$; the meta-analysis estimate is $(10\,000 \cdot 0.050 + 4444 \cdot 0.040)/14\,444 = 0.0469$ with standard error $1/\sqrt{14\,444} = 0.0083$, $z = 5.6$. Without harmonization the two estimates would have canceled. Had the variant been A/T with frequencies $0.48$ and $0.51$, it would have been removed.

## 13.6. Differentiation and Selection Scans

Natural selection leaves two kinds of trace in population data: allele frequencies that differ between populations more than drift allows, and haplotypes that are longer than their frequency would predict. The theory of selection is in [7.4.23](/7.4.23#sec-23.3); here we compute the statistics.

### 13.6.1. Estimating F_ST

The **fixation index** of [7.4.22](/7.4.22#sec-22.4.4) was defined from population allele frequencies. Estimated from samples, it must account for sampling error, which inflates differences between sample frequencies, especially for small samples.

**Formula 13.6.1 (Hudson's F_ST Estimator)** For two populations with sample allele frequencies $\hat p_1, \hat p_2$ from $n_1$ and $n_2$ sampled chromosomes, at SNP $j$

$$
N_j = (\hat p_1 - \hat p_2)^2 - \frac{\hat p_1(1 - \hat p_1)}{n_1 - 1} - \frac{\hat p_2(1 - \hat p_2)}{n_2 - 1}, \qquad D_j = \hat p_1(1 - \hat p_2) + \hat p_2(1 - \hat p_1),
$$

and the genome-wide estimate is the *ratio of averages* $\hat F_{\mathrm{ST}} = \sum_j N_j/\sum_j D_j$ (Hudson and colleagues 1992; Bhatia and colleagues 2013). Without the correction terms, $N_j/D_j = 1 - H_{\mathrm{w}}/H_{\mathrm{b}}$, with $H_{\mathrm{w}}$ the mean heterozygosity within and $H_{\mathrm{b}}$ the probability that two alleles from different populations differ.

The average of per-SNP ratios is dominated by SNPs with small denominators (rare variants) and depends on the frequency spectrum of the SNPs analyzed; the ratio of averages does not. The Weir–Cockerham estimator, derived from an analysis of variance of allele indicators, is the other common choice; it weights populations by sample size.

**Example 13.6.1** For rs4988235, with the 1000 Genomes frequencies of the derived T allele $0.52$ in Europeans, $0.00$ in East Asians, $0.02$ in Africans, $0.11$ in South Asians and $0.22$ in admixed Americans ([7.8.2](/7.8.2#sec-2.4)), and $2\times503$ European and $2\times504$ East Asian chromosomes, Formula 13.6.1 gives $N = 0.2704 - 0.2496/1005 - 0 = 0.2702$ and $D = 0.52$, so $F_{\mathrm{ST}} = 0.52$. Against Africans it is $0.48$, against South Asians $0.33$ and against admixed Americans $0.18$ (without the small-sample corrections, $0.4815$, $0.326$ and $0.176$). Genome-wide $F_{\mathrm{ST}}$ between European and East Asian samples is about $0.1$, so this SNP is in the extreme tail of the distribution: an "$F_{\mathrm{ST}}$ outlier". Outliers alone are weak evidence, since drift produces a long tail and demographic history can mimic selection; they are compared with the genome-wide distribution or with simulations under a fitted demographic model, and combined with haplotype evidence.

### 13.6.2. Extended Haplotype Homozygosity

A new advantageous allele that rises to high frequency quickly drags its haplotype along (a *selective sweep*): there is little time for recombination to break the haplotype, so carriers of the allele share an unusually long segment around it, while carriers of the ancestral allele, whose lineages are old, share only short segments.

**Definition 13.6.1 (Extended Haplotype Homozygosity)** For a core allele $a$ carried by $n_a$ sampled haplotypes, the **extended haplotype homozygosity** at distance $x$ is the probability that two randomly chosen haplotypes carrying $a$ are identical over the whole interval from the core to $x$:

$$
\mathrm{EHH}_a(x) = \sum_{h} \binom{n_h}{2}\Bigl/\binom{n_a}{2},
$$

where the sum runs over the distinct haplotypes $h$ of the interval among the carriers of $a$, $n_h$ of each (Sabeti and colleagues 2002). $\mathrm{EHH}_a(0) = 1$, and it decays with distance as recombination and mutation diversify the haplotypes.

**Formula 13.6.2 (Integrated Haplotype Score)** Let $\mathrm{iHH}_A$ and $\mathrm{iHH}_D$ be the areas under the EHH curves of the ancestral and derived core alleles, integrated on both sides of the core until EHH falls below $0.05$. The unstandardized score is $\ln(\mathrm{iHH}_A/\mathrm{iHH}_D)$, and the *integrated haplotype score* (iHS) is this score standardized to mean $0$ and variance $1$ among SNPs of similar derived-allele frequency genome-wide (Voight and colleagues 2006). Large negative values indicate unusually long haplotypes carrying the derived allele.

Standardization by frequency is needed because, even without selection, a young (low-frequency) derived allele sits on longer haplotypes than an old one. iHS has most power for sweeps in progress, with the selected allele at intermediate frequency; for sweeps near fixation, comparisons between populations (XP-EHH, the population branch statistic) are used. All these statistics need phased haplotypes and a genetic map, and are computed by programs such as selscan from phased VCF files.

**Example 13.6.2** In the simulated sweep of the figure, the derived allele reached frequency $0.5$ in $300$ generations, so derived haplotypes keep the sweeping haplotype for a mean distance of $1/(300\times10^{-8}) = 333\,\mathrm{kb}$ on each side. At $100\,\mathrm{kb}$ from the core, $\mathrm{EHH}_D = 0.62$ while $\mathrm{EHH}_A = 0.005$. The integrals are $\mathrm{iHH}_D = 372\,\mathrm{kb}$ and $\mathrm{iHH}_A = 22\,\mathrm{kb}$, so the unstandardized score is $\ln(22/372) = -2.84$, far in the tail of neutral loci. In Europeans, the haplotype carrying the lactase persistence allele extends over more than $1\,\mathrm{Mb}$ at a frequency above $0.5$ (Bersaglieri and colleagues 2004), and the region is among the strongest iHS signals in the genome; the long haplotype is also why the allele is well tagged by array SNPs and accurately imputed.

![Extended haplotype homozygosity around a recent selective sweep (simulated: 100 haplotypes with the derived core allele, descended from one haplotype that rose to frequency 0.5 in 300 generations, and 100 haplotypes with the ancestral allele; 401 SNPs over ±1 Mb, recombination 10⁻⁸ per bp per generation, background linkage disequilibrium decaying over about 100 kb). A: EHH against distance for the two core alleles; the derived allele's haplotypes stay identical over hundreds of kilobases (iHH_D = 372 kb against iHH_A = 22 kb; unstandardized iHS −2.84). B: the haplotypes, sorted by core allele and by the extent of the sweeping haplotype; dark cells differ from the haplotype that swept, so the white block around the core is the shared haplotype, broken at different distances by recombination in each lineage](./plots/ehh-sweep.py)

Selection scans share a difficulty: demographic events (bottlenecks, expansions, admixture) also produce long haplotypes and differentiated SNPs across the genome, and background selection reduces diversity near genes. A candidate region is therefore credible when it is extreme relative to the genome and to demographic simulations, when several statistics agree, and when a functional variant and a plausible selective agent can be identified, as for *LCT* and dairying, *EDAR* in East Asians, or the Denisovan *EPAS1* haplotype in Tibetans ([7.4.14](/7.4.14#sec-14.6)).

## Summary

| Topic | Key points |
|---|---|
| Data | arrays ($0.5$–$2\times10^6$ SNPs, cluster calling) or sequencing; genotype matrix of counts or dosages (Definition 13.1.1); PLINK `.bed` at $2$ bits per genotype (Formula 13.1.1), `.pgen` compressed with dosages and phase; consistent IDs, build and alleles before merging |
| Sample QC | sex check from X-chromosome $\hat F$ (Formula 13.2.1, Example 13.2.1); missingness; heterozygosity outside mean $\pm3$ SD: contamination or consanguinity; batch effects |
| Relatedness | IBD sharing $(k_0, k_1, k_2)$ and **kinship coefficient**; KING-robust estimator without allele frequencies (Formula 13.2.2, Example 13.2.2); degree thresholds $0.354, 0.177, 0.088, 0.044$; IBS0 separates parent–offspring from siblings; greedy removal or mixed models |
| Variant QC | call rate, differential missingness, MAF, exact HWE test in controls (Formula 13.2.3; the χ² test fails for rare variants, Example 13.2.3); LD pruning and long-range LD regions |
| Structure | PCA of standardized genotypes and the GRM (Definition 13.3.1); Marchenko–Pastur edge and the $1/\sqrt{nm}$ detection threshold (Example 13.3.1); projection onto reference panels with shrinkage; ADMIXTURE model (Definition 13.3.2) fitted by EM (Algorithm 13.3.1); choice of $K$ and over-interpretation; $f_2$, $f_3$, $f_4$; ancient DNA as pseudo-haploid projected samples |
| Phasing and imputation | **haplotype** phasing from families, reads or populations (Definition 13.4.1); Li–Stephens HMM with $O(mK)$ forward–backward (Formula 13.4.1); imputation as posterior-weighted panel alleles (Definition 13.4.2); dosage $\hat R^2$ (Formula 13.4.2, Example 13.4.1); panels must match ancestry |
| Association at scale | residualize covariates once, $O(nmc)$ scan (Formula 13.5.1); score tests and Firth/SPA for binary traits; mixed models with the GRM: EMMAX, BOLT-LMM, REGENIE, LOCO; clumping (Algorithm 13.5.1) and conditional analysis; summary statistics (Definition 13.5.1) and harmonization of alleles, strands and builds (Example 13.5.1) |
| Selection | Hudson's $F_{\mathrm{ST}}$ as a ratio of averages (Formula 13.6.1); rs4988235 as an $F_{\mathrm{ST}}$ outlier (Example 13.6.1); EHH (Definition 13.6.1) and iHS (Formula 13.6.2, Example 13.6.2); demography as the main confounder |

## Questions

1. Why is sample QC done before variant QC, and what would go wrong if a few badly failed samples were kept while filtering variants at a call rate of $98\,\%$?

   **Answer** Removing a variant loses information about all individuals, removing a sample only one. If $3\,\%$ of the samples failed at most SNPs, every SNP would have at least $3\,\%$ missing genotypes and fail the $98\,\%$ call-rate filter, although it was typed well in the good samples. Filtering the failed samples first restores the true call rates, and then variant QC removes only variants that are poorly typed among good samples. The same logic applies to HWE and MAF: contaminated samples create apparent heterozygotes and distort genotype frequencies at all SNPs.

2. A reported female has an X-chromosome $\hat F = 0.98$, and the heterozygosity of her autosomes is normal. Give two explanations and the checks that distinguish them.

   **Answer** (a) A sample swap or labeling error: the DNA is from a man. Check the Y chromosome (intensities or genotype calls at Y SNPs, which should be present), check the sample's identity against other data (a duplicate, a relative in the study, a previous genotype) and trace the plate layout for a neighbor swap. (b) A true karyotype with a single X, such as Turner syndrome (45,X), which is homozygous on X but has no Y signal; or rare cases of complete androgen insensitivity (46,XY with female phenotype), which have Y signal. Normal autosomal heterozygosity excludes contamination and consanguinity; a swap is far more common than either karyotype, and in any case the sample's reported sex should not be "corrected" without confirmation.

3. Show that the KING-robust estimator has expectation $1/4$ for a parent–offspring pair at a SNP in Hardy–Weinberg proportions, in the sense that $\mathbb{E}[N_{\mathrm{het},\mathrm{het}} - 2N_{\mathrm{IBS0}}] = \tfrac14\,\mathbb{E}[N^{(i)}_{\mathrm{het}} + N^{(j)}_{\mathrm{het}}]$ per SNP.

   **Answer** Parent and child share exactly one allele IBD, so they are never opposite homozygotes: $N_{\mathrm{IBS0}} = 0$. Both are heterozygous when the shared allele is $A$ and the other two alleles are both $a$, or the shared allele is $a$ and the other two are both $A$: probability $p\cdot q^2 + q\cdot p^2 = pq$. Each is heterozygous with probability $2pq$, so $\mathbb{E}[N^{(i)}_{\mathrm{het}} + N^{(j)}_{\mathrm{het}}] = 4pq$ per SNP, and the ratio of expectations is $pq/(4pq) = 1/4$. The same holds at every SNP whatever $p$, which is why the estimator does not need allele frequencies.

4. A SNP among $1000$ controls has genotypes $996$, $0$, $4$ ($AA$, $AB$, $BB$). Compute the χ² and the exact test of Hardy–Weinberg proportions and explain the most likely cause.

   **Answer** $\hat p_B = 8/2000 = 0.004$; the expected counts are $992.0$, $7.97$ and $0.016$. The χ² statistic is $1000$ (the $4$ observed $BB$ against an expectation of $0.016$ dominate), $p \approx 10^{-219}$, a meaningless number because the approximation fails. The exact test, conditioning on $8$ copies of $B$, gives $p = 6.6\times10^{-12}$: observing no heterozygotes when about $8$ are expected is very unlikely. The likely cause is a calling error, the heterozygote cluster being absorbed into the homozygous ones, or $B$ being a probe artifact (for example a deletion making some samples look homozygous); the SNP should be removed, or its cluster plots inspected.

5. Why do principal components computed without LD pruning sometimes show a component that separates individuals into three groups unrelated to ancestry? How do you recognize and fix it?

   **Answer** A large region of strong LD with a common polymorphism of structure, such as the inversion at 8p23 or 17q21, or the MHC, contributes hundreds of highly correlated SNPs that vary together. Their joint variation (the three genotypes of the inversion: homozygous standard, heterozygous, homozygous inverted) can exceed the genome-wide ancestry signal on one component, which then separates individuals into three clusters. The loadings of such a component are concentrated in one region instead of spread over the genome. Excluding known long-range LD regions and pruning ($r^2 < 0.2$) before PCA removes it.

6. In a sample of $n = 2000$ individuals typed at $m = 300\,000$ pruned SNPs, what is the approximate threshold $F_{\mathrm{ST}}$ for PCA to detect two equal subpopulations? Would the difference between two neighboring regions of one country with $F_{\mathrm{ST}} = 0.001$ be visible?

   **Answer** $1/\sqrt{nm} = 1/\sqrt{6\times10^8} = 4.1\times10^{-5}$. $F_{\mathrm{ST}} = 0.001$ is about $25$ times the threshold, so the two regions would separate on a principal component even though no single SNP differs significantly between them; such fine structure is what causes residual stratification in large GWAS and why PCs (or mixed models) are included even in apparently homogeneous samples.

7. Explain why the forward step of the Li–Stephens model costs $O(K)$ per SNP instead of $O(K^2)$, and compute the number of operations of a naive implementation and of this one for $m = 10^6$ SNPs and $K = 10^4$ reference haplotypes.

   **Answer** The transition matrix is $(1 - \rho)I + (\rho/K)\boldsymbol{1}\boldsymbol{1}^{\mathsf T}$, so $\sum_k \alpha_j(k)P(k \to l) = (1 - \rho)\alpha_j(l) + (\rho/K)\sum_k\alpha_j(k)$: one sum, computed once, serves all $K$ states. Naive: $mK^2 = 10^{14}$ operations per target haplotype; with the trick: $mK = 10^{10}$, and with the restriction to a few hundred locally similar haplotypes, about $10^8$–$10^9$. For $10^6$ target haplotypes even the last figure requires state selection and parallelism, which is why imputation servers exist.

8. Imputation of a variant gives $\hat R^2 = 0.5$ in a GWAS of $n = 100\,000$. What is the effective sample size for that variant, and why is $\hat R^2$ usually lower for rare variants and for individuals whose ancestry is poorly represented in the reference panel?

   **Answer** The information is that of about $r^2 n = 50\,000$ individuals with true genotypes. Rare variants are carried by few panel haplotypes, so a target haplotype must copy exactly the right one to impute the allele, and the shared segments around rare alleles are short and easily missed; the dosages are pulled towards $2\hat p$, lowering $\operatorname{Var}(d)$ and $\hat R^2$. If the target's ancestry is rare in the panel, its closest panel haplotypes are distant relatives sharing only short segments, switches are frequent and uncertain, and alleles specific to that ancestry may be absent from the panel altogether.

9. Two cohorts report for an A/T SNP: cohort 1 effect allele A, frequency $0.15$, $\hat\beta = 0.08$; cohort 2 effect allele A, frequency $0.86$, $\hat\beta = -0.07$. What has probably happened, and how should the SNP be combined?

   **Answer** An A/T SNP looks the same on both strands. The frequencies ($0.15$ against $0.86 \approx 1 - 0.14$) indicate that cohort 2's "A" is the complement of cohort 1's, that is, cohort 2 is reported on the opposite strand, and its A corresponds to cohort 1's T. Aligning cohort 2 to cohort 1's A gives frequency $0.14$ and $\hat\beta = +0.07$, consistent with cohort 1. The frequency resolves the ambiguity only because it is far from $0.5$; if both had been near $0.5$ the SNP would have to be dropped.

10. Compute Hudson's $F_{\mathrm{ST}}$ (without sample-size corrections) for a SNP with frequencies $0.9$ and $0.1$, and compare it with a SNP at $0.55$ and $0.45$. Which SNP contributes more to a genome-wide ratio-of-averages estimate?

    **Answer** First SNP: $N = 0.8^2 = 0.64$, $D = 0.9\cdot0.9 + 0.1\cdot0.1 = 0.82$, $F_{\mathrm{ST}} = 0.78$. Second: $N = 0.01$, $D = 0.55\cdot0.55 + 0.45\cdot0.45 = 0.505$, $F_{\mathrm{ST}} = 0.020$. In the ratio of averages, each SNP contributes its numerator to the total numerator and its denominator to the total denominator; the first SNP adds $64$ times more to the numerator and only $1.6$ times more to the denominator, so highly differentiated SNPs dominate, as they should, while no SNP's weight is inflated by a tiny denominator.

11. (Design) You have array genotypes of $50\,000$ participants of a Chinese hospital-based cohort and want to run a GWAS of type 2 diabetes and a polygenic score from published European summary statistics. Outline the pipeline and its main pitfalls.

    **Answer** (1) Convert to PLINK 2, check the build and strand against the reference (GRCh38), harmonize alleles. (2) Sample QC: sex check, call rate, heterozygosity on pruned SNPs, KING kinship (keep relatives if a mixed model is used, otherwise remove second degree and closer), PCA with projection onto 1000 Genomes and East Asian references to flag divergent ancestry. (3) Variant QC: call rate, differential missingness by case status, MAF, HWE in controls, batch tests. (4) Phase (SHAPEIT5 or Eagle2) and impute against a panel rich in East Asian haplotypes (for example ChinaMAP or TOPMed), filter on $\hat R^2$. (5) Association with REGENIE (binary trait, Firth correction), covariates sex, age, batch, PCs; check $\lambda_{\mathrm{GC}}$ and the LD score regression intercept; clump and fine-map. (6) Polygenic score: European weights transfer poorly to East Asians (different LD and allele frequencies, [7.4.25](/7.4.25#sec-25.6)), so use multi-ancestry methods or East Asian GWAS weights, and evaluate in held-out participants. Pitfalls: hospital-based case ascertainment (cases from different regions than controls create stratification), cases and controls genotyped in different batches, and over-interpreting PCs or ADMIXTURE components as ethnic groups.

12. (Analysis) An iHS scan of a population finds a region with a standardized iHS of $-5$ around a SNP whose derived allele has frequency $0.6$. List the steps you would take before concluding that it is a target of positive selection.

    **Answer** Check data quality: phasing errors and genotyping artifacts can create apparent long haplotypes, as can a segmental duplication or a region of low recombination in the genetic map (iHS is computed in genetic distance, so a map error inflates it). Compare with the genome-wide distribution and with simulations under a demographic model of the population: bottlenecked populations have many long haplotypes. Look for consistent evidence from other statistics: high $F_{\mathrm{ST}}$ or population branch statistic against related populations, XP-EHH, a skewed frequency spectrum, and, if available, allele-frequency trajectories in ancient DNA. Finally, identify candidate functional variants on the haplotype (coding changes, regulatory variants overlapping enhancers, eQTLs; [7.8.12](/7.8.12), [7.4.25](/7.4.25#sec-25.4.2)) and a plausible selective pressure, as for the lactase enhancer and dairying.
