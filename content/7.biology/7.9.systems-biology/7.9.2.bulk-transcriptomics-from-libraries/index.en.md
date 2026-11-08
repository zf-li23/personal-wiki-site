---
title: "Bulk Transcriptomics: From Libraries to Differential Expression"
description: "The measurement of transcriptomes and the complete RNA-seq workflow: microarrays, RNA-seq and NanoString; experimental design (RNA selection, strandedness, read layout, depth against replicates, batches); counting reads in genes, pseudoalignment and the EM algorithm for isoforms; CPM, FPKM and TPM; LOWESS and quantile normalization of arrays; quality control, variance-stabilized PCA and sample distances; differential expression with DESeq2-type models on the airway data, MA and volcano plots and p-value diagnostics; batch correction and complex designs."
---

A transcriptome profile answers the question: which genes does a population of cells express, and how much, under a given condition? Comparing profiles between conditions, genotypes or patients is the most common experiment in genomics, and its standard form, RNA sequencing followed by a test for differential expression, is the template on which most other omics analyses are built. This chapter follows one experiment from the choice of library to the list of changed genes. The data are those of the airway study (Himes and colleagues, 2014): primary airway smooth-muscle cells from four donors, each cultured with and without the glucocorticoid dexamethasone, eight RNA-seq libraries in all. Glucocorticoids are the mainstay of asthma treatment, and the study asked which genes they induce or repress in the muscle that narrows the airways.

The statistical theory of the analysis, the **negative binomial distribution** of counts and its overdispersion, normalization by size factors, the generalized linear model and the control of the **false discovery rate**, is developed on the same data in [7.7.20](/7.7.20); sample distances, clustering and principal components in [7.7.19](/7.7.19). Here we treat what precedes and surrounds the statistics: how the measurement is made (2.1, 2.2), how reads become counts (2.3) and units (2.4), how microarray intensities are normalized (2.5), how data are checked (2.6), how the test is run and its results read (2.7), and how batches and complex designs are handled (2.8). How RNA is converted into a sequencing library is in [7.2.6](/7.2.6); reads, quality values and alignment to a genome, including spliced alignment, in [7.8.9](/7.8.9) and [7.8.10](/7.8.10). The functional interpretation of the gene lists is the subject of the next chapter.

## 2.1. Transcriptomes and How They Are Measured

The **transcriptome** of a mammalian cell contains a few hundred thousand mRNA molecules (and several times more ribosomal RNA, which is usually removed), distributed over some ten thousand expressed genes with a dynamic range of five orders of magnitude: a few genes are present at thousands of copies per cell, most at one to a hundred ([7.6.20](/7.6.20)). A transcriptome measurement must therefore count rare and abundant molecules in one assay, and it measures steady-state levels, which reflect both synthesis and degradation ([7.2.22](/7.2.22), [7.2.6](/7.2.6#sec-6.3)).

| Technology | Principle | Strengths | Limits |
|---|---|---|---|
| Two-colour microarray (spotted or Agilent, 60-mer probes) | two samples labeled with different dyes hybridize competitively to one array; the ratio of intensities is read | direct comparison on one array; cheap per sample | ratio only; dye bias; needs known sequences |
| One-colour oligonucleotide array (Affymetrix, 25-mer probes) | one sample per array; each gene measured by a probe set of 11–20 probes, historically paired with mismatch probes for background | standardized platform; large public compendia | cross-hybridization; saturation at high and background at low intensity |
| RNA-seq | cDNA fragments are sequenced and the reads counted per gene | counts with a wide dynamic range; no need for prior sequences; isoforms, fusions, variants, new transcripts | library biases; cost and computation |
| NanoString | color-coded probe pairs hybridize to target RNA and are counted directly, without reverse transcription or amplification | digital counts from small or degraded samples, e.g. fixed clinical tissue | hundreds of genes, not the transcriptome |
| Targeted RNA-seq, high-throughput qPCR | amplification or capture of selected genes | sensitivity for chosen targets | limited coverage |

Microarrays dominated from the late 1990s to about 2010 and left two legacies: vast public data sets that are still reanalyzed, and the statistical methods, normalization (2.5), moderated tests and false discovery rates, that RNA-seq inherited. RNA-seq measures molecules by counting, not by fluorescence, and its counts carry the Poisson sampling noise of a finite library on top of the biological variation between samples ([7.6.32](/7.6.32), [7.7.20](/7.7.20)).

## 2.2. Experimental Design

### 2.2.1. The Library

The choices made at the bench determine what can be learned:

| Choice | Options | Consequence |
|---|---|---|
| RNA selection | poly(A) selection; ribosomal RNA depletion | poly(A) selection captures mature mRNA and loses non-polyadenylated RNAs (histone mRNAs, many noncoding RNAs) and degraded samples; depletion keeps them, and pre-mRNA introns as well |
| Strand | unstranded; stranded (dUTP marking of the second strand) | stranded libraries assign reads to the correct strand, necessary for antisense and overlapping genes |
| Read layout | single-end; paired-end, read length | paired ends help isoforms, fusions and alignment in repeats; single-end short reads suffice for gene-level counts |
| Depth | reads per library | about 5–25 million for highly expressed genes, 30–60 million for a global view with some splicing, 100–200 million for detailed isoform analysis or assembly |
| Replicates | number of independent samples per condition | sets the power to detect differences (2.2.2) |

The dUTP protocol, the most common stranded method, incorporates dUTP into the second cDNA strand and destroys it before amplification, so that the sequenced read 1 is the reverse complement of the RNA. The counting software must be told: a stranded library counted as unstranded loses antisense information, and one counted with the wrong strand loses most of its reads (2.3).

### 2.2.2. Replicates and Depth

**Definition 2.2.1** A **biological replicate** is an independent biological sample of a condition (another donor, animal, culture or plant grown separately), whose differences from the other replicates include the natural biological variation; a **technical replicate** is a repeated measurement of the same biological sample (another library from the same RNA, or another sequencing run of the same library).

Only biological replicates support conclusions about the condition: the question is whether dexamethasone changes expression in airway muscle, not in one particular culture dish. Technical replicates of RNA-seq vary little beyond Poisson sampling and are rarely needed. Typical minima are two or three replicates for cell lines, three or more for animals and many more for human subjects; benchmarks with many replicates suggest six or more per group for reliable detection of moderate changes (Schurch and colleagues, 2016).

With a fixed budget there is a trade-off between the number of libraries and the number of reads in each. The variance of a log fold change estimated from $n$ replicates per group at mean count $\mu$ is approximately
$$
\operatorname{Var}(\widehat{\log \mathrm{FC}}) \approx \frac{1}{n}\left(\frac{1}{\mu_A} + \frac{1}{\mu_B} + 2\phi\right),
$$
where $\phi$ is the biological dispersion of the negative binomial model ($\operatorname{Var} = \mu + \phi\mu^2$, [7.7.20](/7.7.20)). Depth increases $\mu$ and shrinks only the Poisson terms $1/\mu$; replicates divide the whole expression, including the biological term $2\phi$, by $n$. Once $\mu$ is a few times larger than $1/\phi$, more depth hardly helps.

**Example 2.2.1** Take a gene that receives a fraction $10^{-6}$ of all reads, a twofold change, dispersion $\phi = 0.05$ (biological coefficient of variation $\sqrt\phi \approx 22\%$) and a two-sided test at level $0.001$. A budget of $120$ million reads spent as $3 + 3$ libraries of $20$ million gives $\mu_A = 20$ and power $0.34$; spent as $6 + 6$ libraries of $10$ million it gives $\mu_A = 10$ and power $0.54$. Increasing the depth of the three-replicate design tenfold, to $200$ million reads per library, raises its power only to $0.64$, close to its ceiling of $0.69$ at infinite depth, while six replicates have a ceiling of $0.98$.

![Replicates against sequencing depth (normal approximation, lines; 4000 simulated negative binomial experiments, points). A: a budget of 120 million reads shared among 2n libraries, for a weakly and a moderately expressed gene with a twofold change: more replicates at lower depth win. B: power against depth per library for 3 and 6 replicates per group: depth saturates at the ceiling set by biological variation (dotted)](./plots/replicates_depth.py)

### 2.2.3. Batches

**Definition 2.2.2** A **batch effect** is a systematic difference between groups of measurements that arises from technical conditions of their processing (date, operator, reagent lot, library kit, sequencing run or instrument) rather than from the biology being studied.

Batch effects are ubiquitous and often larger than the effects of interest. They are harmless when the design is balanced, so that every batch contains samples of every condition and batch can be included in the model, and fatal when batch and condition are confounded. If all treated samples are prepared on Monday and all controls on Tuesday, no analysis can separate treatment from day: in the simulation of the figure (panel B), with no true treatment effect at all, $117$ of $2000$ genes reach $p < 0.01$, against $21$ when the same batch effect is present in a balanced design and modeled (panel C), close to the $20$ expected by chance. The remedy is in the design: randomize the order of processing, block by batch (process one sample of each condition together, [3.8](/3.8)), and record every technical variable.

The airway experiment is a paired design in this sense. Each donor's cells were cultured with and without the drug, so donor-to-donor variation, which is large in primary cells, is a block that can be removed by including the donor in the model (2.7).

## 2.3. From Reads to Counts

### 2.3.1. Counting Reads in Genes

After reads are aligned to the genome with a spliced aligner such as STAR or HISAT2 ([7.8.10](/7.8.10)), each read is assigned to the gene whose exons it overlaps, using an annotation in GTF format ([7.8.2](/7.8.2)). Tools such as htseq-count and featureCounts implement explicit rules for ambiguous cases. In the default union mode of htseq-count, a read is counted for a gene if all the exonic positions it covers belong to that gene alone; reads overlapping exons of two genes are "ambiguous", and reads aligned to several genomic locations (multi-mapping reads) are discarded. The strand option must match the library: for the dUTP protocol, `--stranded=reverse` in htseq-count or `-s 2` in featureCounts. The output is the count matrix, genes by samples, the input of all that follows.

Reference-guided assembly (StringTie) goes further and reconstructs the transcripts present in the sample from the spliced alignments, including unannotated isoforms; its abundances are reported per transcript.

### 2.3.2. Pseudoalignment and the EM Algorithm

Most reads of a gene are compatible with several of its isoforms, and genes in families share sequence. Rather than aligning every read base by base, the programs kallisto and salmon determine only which transcripts a read could have come from.

**Definition 2.3.1** The **pseudoalignment** of a read is the set of transcripts in a reference transcriptome with which the read is compatible, determined from the exact matches of its $k$-mers to the transcripts (for example by intersecting the sets of transcripts containing each $k$-mer), without computing a base-level alignment. Reads with the same set form an equivalence class.

Abundances are then estimated from the counts of the equivalence classes. Let $\alpha_t$ be the probability that a read comes from transcript $t$, and $\tilde\ell_t$ its effective length, the number of positions at which a fragment can start ($\ell_t - \bar\ell_{\mathrm{frag}} + 1$, corrected for the fragment length distribution). A read from $t$ falls at a given compatible position with probability $1/\tilde\ell_t$, so the **likelihood function** of the abundances, given the classes $c$ with counts $n_c$ and compatible sets $T_c$, is
$$
L(\boldsymbol{\alpha}) = \prod_{c} \Bigl(\sum_{t \in T_c} \frac{\alpha_t}{\tilde\ell_t}\Bigr)^{n_c}. \tag{2.1}
$$
It is maximized by the **EM algorithm** ([3.5.6](/3.5.6)), treating the transcript of origin of each read as missing data.

**Algorithm 2.3.1 (EM for Transcript Abundances)** Start from any $\boldsymbol{\alpha}^{(0)}$ with positive entries summing to one, and repeat until the change is negligible:

1. E-step: for each class $c$ and $t \in T_c$, the expected fraction of its reads that came from $t$ is $z_{ct} = \dfrac{\alpha_t/\tilde\ell_t}{\sum_{u \in T_c}\alpha_u/\tilde\ell_u}$.
2. M-step: $\alpha_t \leftarrow \dfrac{1}{N}\sum_{c \ni t} n_c z_{ct}$, with $N = \sum_c n_c$.

The transcript fractions are $\rho_t = (\alpha_t/\tilde\ell_t)/\sum_u(\alpha_u/\tilde\ell_u)$, and the TPM of 2.4 is $10^6\rho_t$. Each iteration costs time proportional to the total size of the compatible sets of the classes, which is far smaller than the number of reads, and the likelihood never decreases.

**Example 2.3.1** A gene has two isoforms: T1 with exons 1, 2 and 3 ($400$, $200$ and $600$ nt) and T2, which skips exon 2 ($1000$ nt). For $100$-nt reads, the effective lengths are $1101$ and $901$. Of $2000$ reads simulated from transcript fractions $\boldsymbol\rho = (0.3, 0.7)$, $1651$ lie entirely in exon 1 or exon 3 and are compatible with both, $194$ touch exon 2 and fit only T1, and $155$ span the exon 1–exon 3 junction and fit only T2. EM converges from any start to $\hat{\boldsymbol\alpha} = (0.348, 0.652)$, that is $\hat{\boldsymbol\rho} = (0.304, 0.696)$. The unique reads alone would suggest the opposite ($194 > 155$): they are informative only after the different lengths of the unique regions ($299$ start positions for T1, $99$ for T2) are taken into account, which the likelihood (2.1) does automatically.

![The EM algorithm for two isoforms. A: isoform T1 (exons 1–3) and T2 (exons 1 and 3), and the three compatibility classes of 2000 simulated reads. B: the estimated read fraction of T1 from five starting values, converging to the maximum-likelihood estimate (dashed). C: the log-likelihood increases at every iteration](./plots/isoform_em.py)

:::

Transcript estimates are summed to genes for gene-level testing (the tximport approach), using the estimated counts and an offset for the average transcript length of each gene in each sample, so that a change in isoform usage is not mistaken for a change in expression. Pseudoalignment is an order of magnitude faster than spliced alignment and gives comparable gene-level results; alignment remains necessary for new transcripts, variants and visualization.

```bash
# quality trimming, then two routes to a count matrix (paired-end, dUTP-stranded library)
fastp -i S1_R1.fastq.gz -I S1_R2.fastq.gz -o S1_R1.trim.fq.gz -O S1_R2.trim.fq.gz -h S1.fastp.html

# route 1: spliced alignment and gene-level counting
STAR --genomeDir star_index --readFilesIn S1_R1.trim.fq.gz S1_R2.trim.fq.gz \
     --readFilesCommand zcat --runThreadN 8 --outSAMtype BAM SortedByCoordinate \
     --outFileNamePrefix S1.
featureCounts -p --countReadPairs -s 2 -T 8 -a genes.gtf -o counts.txt S1.Aligned.sortedByCoord.out.bam

# route 2: pseudoalignment and EM quantification of transcripts
salmon index -t transcripts.fa -i salmon_index
salmon quant -i salmon_index -l A -1 S1_R1.trim.fq.gz -2 S1_R2.trim.fq.gz \
     --validateMappings -p 8 -o quant/S1
```

## 2.4. Units of Expression

Raw counts depend on the depth of each library and on the length of each gene: a gene twice as long yields twice the reads at the same molar abundance. Units that correct for these are used to display and compare expression levels.

**Definition 2.4.1** Let $k_{g}$ be the count of gene (or transcript) $g$ in a library, $N = \sum_g k_g$ the total count and $\tilde\ell_g$ the effective length in nucleotides. Counts per million are $\mathrm{CPM}_g = 10^6 k_g/N$. **Fragments per kilobase per million** (FPKM; RPKM for single-end reads) are
$$
\mathrm{FPKM}_g = \frac{k_g}{(\tilde\ell_g/10^3)(N/10^6)},
$$
and **transcripts per million** are
$$
\mathrm{TPM}_g = 10^6\,\frac{k_g/\tilde\ell_g}{\sum_h k_h/\tilde\ell_h}.
$$

TPM first divides by length and then normalizes, so the TPM of a sample always sum to $10^6$ and estimate the fraction of transcripts (not of reads) contributed by each gene; FPKM normalizes by the total number of reads, and its sum varies from sample to sample. TPM is therefore the better unit for comparing the composition of samples, but neither unit removes composition effects.

**Example 2.4.1** Three genes of $1$, $2$ and $4$ kb have counts $(100, 200, 400)$ in sample 1 and $(100, 200, 1600)$ in sample 2. In sample 1 all have $100$ reads per kilobase, so each has TPM $333\,333$ and FPKM $142\,857$ (sum $428\,571$). In sample 2 the third gene is four times more expressed: TPM become $(166\,667, 166\,667, 666\,667)$ and FPKM $(52\,632, 52\,632, 210\,526)$, summing to $315\,789$. The first two genes have exactly the same counts in both samples, yet their TPM halve and their FPKM fall $2.7$-fold, because the third gene took a larger share of the library.

The example shows why within-sample units cannot be used to test for differential expression. If a few genes become very highly expressed, as hemoglobin genes do in samples contaminated by red blood cells, every other gene appears to decrease. Differential expression is therefore tested on raw counts, with normalization factors estimated under the assumption that most genes do not change (the median-of-ratios size factors of DESeq2 and the trimmed mean of M-values of edgeR, [7.7.20](/7.7.20)); length cancels when the same gene is compared between samples.

```python
import numpy as np

def tpm(counts, eff_len):
    """counts: genes x samples array of (estimated) counts; eff_len: effective lengths in nt."""
    rate = counts / eff_len[:, None]
    return 1e6 * rate / rate.sum(axis=0)

def fpkm(counts, eff_len):
    return counts / (eff_len[:, None] / 1e3) / (counts.sum(axis=0) / 1e6)

counts = np.array([[100, 100], [200, 200], [400, 1600]], float)
length = np.array([1000, 2000, 4000], float)
print(tpm(counts, length).round(0))   # columns sum to 1e6
print(fpkm(counts, length).round(0))  # column sums differ
```

## 2.5. Normalization of Microarray Data

Microarray intensities need a different normalization, and the methods remain in use for arrays and for other intensity data such as proteomics. Two kinds of artifact are typical: arrays differ in overall brightness (amount of labeled RNA, scanner settings), and in two-colour arrays the dyes differ in an intensity-dependent way. Both are seen in the M–A plot, which plots for each gene the log ratio $M = \log_2(R/G)$ of the red and green intensities against the mean log intensity $A = \tfrac12(\log_2 R + \log_2 G)$. If most genes do not change, the cloud should be centred on $M = 0$ at every $A$; a curved cloud reveals dye bias. **Locally weighted regression** (LOWESS) of $M$ on $A$ estimates the curve, and subtracting it centres the cloud (figure, panels A and B). A robust variant, the invariant-set method, fits the curve only to genes whose ranks are similar in both channels, so that strongly changed genes do not distort it (Li and Wong, 2001).

For one-colour arrays, the standard is to make the distributions identical.

**Definition 2.5.1** **Quantile normalization** of $m$ samples of $G$ values each replaces, in every sample, the value of rank $r$ by the mean, over the $m$ samples, of their values of rank $r$; after it all samples have exactly the same empirical distribution.

It is the normalization step of the RMA procedure for Affymetrix arrays (Irizarry, Bolstad and colleagues, 2003) and works well when the samples differ only technically. Its assumption is strong: the distribution of expression must be the same in all samples. When a large fraction of genes truly changes in one group, as after a global loss of transcription or between very different tissues, quantile normalization erases part of the real change and creates spurious ones: in the simulation of panel D, where $30\%$ of genes double in two of four arrays, the median log fold change of the changed genes falls from $1$ to $0.69$ and the unchanged genes appear to fall by $0.29$. The same caution applies to any normalization that assumes most genes are unchanged, including the size factors of RNA-seq, and global changes are best measured with spike-in RNA added in proportion to cell number.

![Normalization of microarray data (simulated). A: the M–A plot of a two-colour array with intensity-dependent dye bias; truly changed genes in red, the LOWESS fit in blue. B: after subtraction of the LOWESS curve. C: densities of four one-colour arrays before (thin) and after quantile normalization (thick, identical). D: when 30% of the genes truly double in arrays 3 and 4, quantile normalization shrinks their log fold changes and shifts the unchanged genes](./plots/ma_normalization.py)

## 2.6. Quality Control and Exploration

The first task when data arrive is not analysis but checking how they were produced and whether they are fit for use. For RNA-seq the checks proceed in layers:

| Stage | Check | Warning sign |
|---|---|---|
| Reads | base quality, adapter content, duplication ([7.8.9](/7.8.9)) | quality falling along the read; high duplication from low input |
| Alignment | fraction of reads aligned and assigned to genes; fraction of rRNA; strand | low assignment (genomic DNA, wrong strand option); high rRNA after depletion |
| Coverage | gene-body coverage, transcript integrity number (TIN, RSeQC) | coverage piled at the 3′ end: degraded RNA |
| Library | total counts, number of detected genes | a library far smaller or less complex than the others |
| Biology | known marker genes and sex-chromosome genes; known responses | a sample whose markers contradict its label |
| Samples | clustering of replicates; PCA | a sample clustering with the wrong group: swapped label or outlier |

Exploration of sample relations needs a transformation. Counts have a variance that grows with the mean, so distances between samples computed on raw or log counts are dominated by either the highly expressed or the noisy weakly expressed genes. A **variance-stabilizing transformation** of the negative binomial counts, or the closely related regularized logarithm, gives values whose variance is roughly independent of the mean; the transformation used by DESeq2 behaves like $\log_2$ for large counts and compresses small ones. On these values sample-to-sample distances, **hierarchical clustering** and **principal component analysis** ([3.4.5](/3.4.5), [7.7.19](/7.7.19)) or **multidimensional scaling** ([3.4.6](/3.4.6)) show the main sources of variation.

In the airway data between $15.2$ and $30.8$ million fragments per library are counted in genes, and $33\,469$ of the $63\,677$ annotated genes have at least one read. On the variance-stabilized expression of the $500$ most variable genes, the first principal component ($39\%$ of the variance) separates treated from untreated samples, and the second ($27\%$) and later components separate the four donors (figure, panel A). The donor effect is nearly as large as the treatment effect, which is why the design that pairs the samples by donor matters.

![Design and batch structure in sample PCA. A: the airway data, PCA of variance-stabilized expression of the 500 most variable genes: PC1 separates dexamethasone-treated (orange) from untreated samples (blue), PC2 the four donors' cell lines (marker shape). B, C: simulations with no treatment effect, 2000 genes and a batch shift in 300 of them: p-values for treatment when batch is identical to treatment (B), and when the design is balanced and batch is modeled (C)](./plots/airway_pca.py)

## 2.7. Differential Expression in Practice

### 2.7.1. The Model and the Workflow

**Definition 2.7.1** A gene is **differentially expressed** between conditions if its mean expression, after normalization for library size and composition, differs between them; a test for **differential expression** decides, for each gene, whether the data are consistent with no difference, and estimates the size of the difference as a log fold change.

The tools in general use, DESeq2 (Love, Huber and Anders, 2014), edgeR (Robinson, McCarthy and Smyth, 2010) and limma-voom (Law and colleagues, 2014), share a framework that is derived in [7.7.20](/7.7.20): the count $K_{ij}$ of gene $i$ in sample $j$ is negative binomial with mean $\mu_{ij} = s_j q_{ij}$, where $s_j$ is a size factor, and $\log q_{ij} = \boldsymbol{x}_j^{\mathsf T}\boldsymbol{\beta}_i$ is a **generalized linear model** with the **design matrix** rows $\boldsymbol{x}_j$; the dispersion of each gene is shrunk towards a trend shared by all genes, because a handful of replicates cannot estimate a variance well; and the tests are corrected for multiplicity by the **Benjamini–Hochberg procedure**. limma-voom instead transforms counts to $\log$ CPM, estimates the mean–variance relationship, and uses precision weights in linear models with moderated $t$ statistics. The steps of a run correspond to these concepts:

| Step | What it does | Concept ([7.7.20](/7.7.20)) |
|---|---|---|
| filter genes with very few reads | removes genes with no power | independent filtering |
| set the design `~ cell + dex`, reference level `untrt` | donor as a block, treatment as the effect of interest | design matrix, paired design |
| estimate size factors | median of ratios to a pseudo-reference sample | normalization for depth and composition |
| estimate dispersions | gene-wise maximum likelihood, trend, shrinkage | overdispersion, empirical Bayes |
| fit the GLM, Wald test | $\hat\beta$ for `dex`, standard error, $z$ statistic | negative binomial GLM |
| adjust p-values | Benjamini–Hochberg | false discovery rate |
| shrink log fold changes | adaptive prior on $\beta$ | shrinkage estimation |

In Python the same model is fitted by pydeseq2 (the R equivalents are `DESeqDataSetFromMatrix`, `DESeq`, `results` and `lfcShrink` in DESeq2, or `DGEList`, `calcNormFactors`, `estimateDisp` and `glmQLFit` in edgeR):

```python
import pandas as pd
from pydeseq2.dds import DeseqDataSet
from pydeseq2.ds import DeseqStats

counts = pd.read_csv("airway_counts.csv", index_col=0)      # genes x samples, raw integer counts
meta = pd.read_csv("airway_coldata.csv", index_col=0)[["cell", "dex"]]
meta["dex"] = pd.Categorical(meta["dex"], categories=["untrt", "trt"])   # untreated = reference level

counts = counts[counts.sum(axis=1) >= 10]                     # drop genes with almost no reads
dds = DeseqDataSet(counts=counts.T, metadata=meta, design="~cell + dex")
dds.deseq2()                                                  # size factors, dispersions, GLM fit

stats = DeseqStats(dds, contrast=["dex", "trt", "untrt"], alpha=0.1)
stats.summary()                                               # Wald tests and BH-adjusted p-values
res = stats.results_df                                        # baseMean, log2FoldChange, lfcSE, stat, pvalue, padj
stats.lfc_shrink(coeff="dex[T.trt]")                          # shrunken log2 fold changes
dds.vst()                                                     # variance-stabilized values for PCA and heatmaps
```

The results table has one row per gene: `baseMean`, the mean of the normalized counts over all samples; `log2FoldChange`, the estimate of $\beta_{\text{dex}}/\ln 2$; `lfcSE`, its standard error; `stat`, the Wald statistic; `pvalue`; and `padj`, the Benjamini–Hochberg adjusted p-value, left missing for genes removed by independent filtering or flagged as outliers.

### 2.7.2. The Airway Results

Of the $22\,369$ genes with at least $10$ reads in total, $18\,899$ pass independent filtering. The size factors of the eight libraries range from $0.67$ to $1.40$. At an adjusted p-value below $0.1$, $4691$ genes are differentially expressed, $2538$ up and $2153$ down in treated cells; below $0.05$, $3888$; and $1042$ also change more than twofold. The most significant genes include classic glucocorticoid targets:

| Gene | Mean count | $\log_2$ fold change | Adjusted p | Known role |
|---|---|---|---|---|
| *SPARCL1* | 997 | 4.57 | $1.0\times10^{-161}$ | matricellular protein |
| *DUSP1* | 3409 | 2.95 | $2.5\times10^{-135}$ | MAP kinase phosphatase, anti-inflammatory |
| *KLF15* | 561 | 4.46 | $4.0\times10^{-100}$ | transcription factor, glucocorticoid-induced |
| *PER1* | 777 | 3.19 | $1.0\times10^{-95}$ | clock gene with a glucocorticoid response element |
| *VCAM1* | 508 | −3.68 | $1.0\times10^{-95}$ | adhesion molecule, repressed |
| *ZBTB16* | 385 | 7.35 | $2.1\times10^{-40}$ | transcription factor, strongly induced |
| *FKBP5* | 2564 | 4.05 | $8.6\times10^{-26}$ | co-chaperone of the glucocorticoid receptor, negative feedback |
| *TSC22D3* (GILZ) | 2206 | 3.19 | $3.3\times10^{-19}$ | glucocorticoid-induced leucine zipper |
| *CRISPLD2* | 3082 | 2.63 | $6.7\times10^{-60}$ | the gene highlighted by the original study |

The values were computed with pydeseq2, a reimplementation of DESeq2; the R package gives very similar numbers. The induction of *FKBP5*, *TSC22D3*, *PER1* and *DUSP1* in nearly every glucocorticoid-treated cell type makes them positive controls: their presence near the top of the list is part of quality control.

The pairing matters. Fitting the same data with the design `~ dex`, which ignores the donor, finds $3422$ genes at an adjusted p below $0.1$ instead of $4691$: the donor differences, about as large as the treatment effect (2.6), are then counted as noise.

### 2.7.3. Reading the Results

**Definition 2.7.2** An **MA plot** of a differential-expression analysis plots, for each gene, the log fold change against the mean normalized expression (on a logarithmic scale). A **volcano plot** plots, for each gene, a measure of significance, usually $-\log_{10}$ of the (adjusted) p-value, against the log fold change.

The MA plot shows how the precision of the fold change depends on expression: weakly expressed genes, with few reads, have wildly scattered maximum-likelihood fold changes, and significance requires a larger change at low counts (figure, panel A). Shrinking the fold changes towards zero with a prior estimated from all genes pulls in the unreliable estimates and leaves well-measured ones nearly unchanged (panel B); the shrunken values are better for ranking genes by effect size and for displays. The volcano plot shows the joint selection by size and significance; at $|\log_2\mathrm{FC}| > 1$ on the shrunken scale and adjusted $p < 0.05$, $463$ genes are induced and $378$ repressed (panel C).

The histogram of the raw p-values is the first diagnostic of any large-scale test. It should consist of a flat floor, the p-values of genes without change, which are uniform on $(0, 1)$, and a peak near zero, the genes with change (panel D). In the airway data the height of the floor estimates the proportion of unchanged genes at $\hat\pi_0 = 0.65$ (Storey's estimator with $\lambda = 0.5$). A histogram that rises towards $p = 1$, or has a hump in the middle, signals a misspecified model, for example an ignored batch or a wrong dispersion estimate.

![Differential expression in the airway data (pydeseq2, design ~ cell + dex). A: MA plot of maximum-likelihood log2 fold changes; genes with adjusted p < 0.1 in colour (orange: induced, blue: repressed). B: the same with shrunken fold changes. C: volcano plot of −log10 adjusted p against shrunken log2 fold change, thresholds at padj = 0.05 and twofold. D: histogram of raw p-values of the 18899 genes kept by independent filtering, with the estimated floor of null genes (dashed)](./plots/volcano_ma.py)

A p-value of $0.05$ for one gene does not mean that $5\%$ of the genes declared significant are false discoveries. It means that a gene without any change would reach such a value with probability $0.05$; among $20\,000$ unchanged genes about $1000$ would, whatever the number of true changes. The proportion of false discoveries among the genes declared significant, the false discovery rate, depends on how many genes truly change and is controlled by the adjusted p-values; the distinction between the type I error rate of one test, the family-wise error rate and the FDR is made precise in [7.7.20](/7.7.20). Bonferroni correction at $0.05$ would declare $1398$ airway genes significant, against $3888$ at an FDR of $0.05$.

## 2.8. Batches, Hidden Variables and Complex Designs

When batches are known and balanced, they are included in the design as a factor, like the donor in the airway analysis, and the test of the condition is adjusted for them. Correction of the data themselves is needed only for displays and for methods that cannot include covariates. ComBat (Johnson, Li and Rabinovic, 2007) models each gene's values in each batch as shifted and scaled, estimates the batch parameters with empirical Bayes shrinkage across genes, and removes them; ComBat-seq applies the same idea to counts with a negative binomial model. Correction is legitimate only when the condition of interest is not confounded with batch and is protected in the model: correcting a confounded design removes the biology along with the batch.

Unknown sources of variation, such as differences in RNA quality, cell composition or time of collection, are estimated from the data. Surrogate variable analysis (SVA) finds directions of variation in the residuals after the condition is fitted; RUV (remove unwanted variation) estimates them from control genes or spike-ins assumed not to respond. The estimated factors enter the design as covariates.

Designs beyond two groups are expressed through the design matrix. With two factors, genotype and treatment, the question whether the treatment effect differs between genotypes is a test of their interaction term. A time course is analyzed by including time (as a factor, or as a spline with a few degrees of freedom) and testing by the **likelihood ratio test** whether the full model with time explains the counts better than a reduced model without it; correlations between successive time points of the same individual call for blocking by individual or for mixed models ([7.7.17](/7.7.17)). Whatever the design, the contrast that answers the biological question should be written down before the analysis.

## Summary

- Transcriptome profiles are measured by microarrays (fluorescence of hybrids), RNA-seq (counts of sequenced fragments) or targeted counting (NanoString); RNA-seq counts span a wide dynamic range and carry Poisson and biological variation (2.1).
- Design choices: poly(A) selection or rRNA depletion, stranded libraries (dUTP: read 1 is antisense), read layout and depth (2.2.1). Biological replicates (Definition 2.2.1) set the power; depth reduces only the Poisson part of the variance $(1/\mu_A + 1/\mu_B + 2\phi)/n$, so with a fixed budget more replicates usually win (Example 2.2.1). Batch effects (Definition 2.2.2) are harmless in balanced designs and fatal when confounded with the condition.
- Counts come from alignment and counting rules (union mode, strand option) or from pseudoalignment (Definition 2.3.1) and EM on equivalence classes (Eq. (2.1), Algorithm 2.3.1, Example 2.3.1).
- CPM, FPKM and TPM correct for depth and length (Definition 2.4.1); TPM sums to $10^6$; none removes composition effects (Example 2.4.1), so tests use raw counts with size factors.
- Microarrays are normalized by LOWESS on the M–A plot and by quantile normalization (Definition 2.5.1), which fails when many genes truly change (2.5).
- Quality control proceeds from reads to biology; variance-stabilized data, sample distances and PCA reveal the structure: in the airway data PC1 ($39\%$) is treatment and PC2 ($27\%$) donor (2.6).
- Differential expression (Definition 2.7.1) is tested with negative binomial GLMs with shrunken dispersions and BH adjustment ([7.7.20](/7.7.20)); with design `~ cell + dex` the airway data give $4691$ genes at FDR $0.1$, including *FKBP5*, *TSC22D3*, *PER1*, *DUSP1* and *KLF15*; ignoring the pairing gives $3422$ (2.7.2).
- MA and volcano plots (Definition 2.7.2) and the p-value histogram ($\hat\pi_0 = 0.65$) are the standard diagnostics; a p-value is not a false discovery rate (2.7.3).
- Known batches enter the design; ComBat(-seq) corrects data for display; SVA and RUV estimate hidden factors; interactions and time courses are tested by contrasts and likelihood ratio tests (2.8).

## Questions

1. A laboratory sequences one pooled RNA sample from five mice per condition, four times each, at $50$ million reads per library. What can and cannot be concluded from the comparison?

   **Answer** The four libraries are technical replicates of one pooled sample per condition, so the analysis estimates only technical (essentially Poisson) variation. A test would declare significant any difference between the two pools, including differences due to the particular mice pooled, so the result does not generalize to the condition. Pooling averages away biological variation without measuring it: the effective number of biological replicates is one per group. Five separate libraries per condition at $20$ million reads would cost less and allow a valid test.

2. In Example 2.2.1, what power do $4 + 4$ libraries of $15$ million reads have, and what does a design with $3 + 3$ libraries need to reach the same power?

   **Answer** With $\mu_A = 15$, $\mu_B = 30$ and $\phi = 0.05$, the variance of the log fold change is $(1/15 + 1/30 + 0.1)/4 = 0.05$, the standard error $0.224$, and $z = \ln 2/0.224 = 3.10$ against the critical value $3.29$, giving power $\Phi(3.10 - 3.29) \approx 0.42$. With three replicates the variance is $(1/\mu + 1/(2\mu) + 0.1)/3$; equality with $0.05$ requires $1.5/\mu = 0.05$, that is $\mu = 30$, or $30$ million reads per library ($180$ million in total instead of $120$ million).

3. Classify each as a technical or biological issue and say how it would appear in quality control: (a) RNA degraded during transport, (b) a library prepared with the wrong strand setting in the counting step, (c) a mislabeled sample, (d) contamination with genomic DNA.

   **Answer** (a) Technical; gene-body coverage biased towards the 3′ end, low TIN, a sample apart in PCA. (b) Technical, of analysis rather than of the library: most reads unassigned or counted as antisense, the assigned fraction far below that of correctly counted samples; recounting with the right option fixes it. (c) An error of record keeping; marker genes, sex-chromosome genes or the known response contradict the label, and the sample clusters with the other group. (d) Technical; many reads in introns and intergenic regions evenly, on both strands of a stranded library, and a lower fraction assigned to exons.

4. In Example 2.3.1, compute the expected numbers of reads in each compatibility class for the true fractions $\boldsymbol\rho = (0.3, 0.7)$ and compare them with the simulated counts.

   **Answer** Reads come from T1 with probability $w_1 = 0.3\cdot1101/(0.3\cdot1101 + 0.7\cdot901) = 330.3/961.0 = 0.344$. A T1 read starts at one of $1101$ positions; it is unique to T1 if it overlaps exon 2, i.e. starts at positions $301$–$599$ ($299$ positions), so $P(\text{T1 only} \mid \text{T1}) = 299/1101$. A T2 read spans the junction if it starts at positions $301$–$399$ ($99$ of $901$). Expected counts in $2000$ reads: T1 only $2000\cdot0.344\cdot299/1101 = 187$, T2 only $2000\cdot0.656\cdot99/901 = 144$, both $2000 - 187 - 144 = 1669$. The simulation gave $194$, $155$ and $1651$, within Poisson fluctuation (standard deviations about $14$, $12$ and $18$).

5. Why do the TPM values of a gene computed by salmon from two samples not give a valid test of differential expression, even with replicates?

   **Answer** TPM are relative within each sample: if other genes change, a constant gene changes in TPM (Example 2.4.1). TPM also discard the count scale that determines the Poisson part of the variance, so a TPM of $50$ from $10$ reads and one from $10\,000$ reads are treated alike. The correct input is the estimated counts (summed to genes with the length offsets of tximport), normalized by size factors estimated under the assumption that most genes do not change, and tested with a count model.

6. Write a vectorized computation of Welch $t$ statistics for $20\,000$ genes in two groups of $4$ samples, and explain why it is much faster than a loop over genes.

   **Answer** With `X` a $20\,000 \times 8$ array of log expression and boolean masks `a`, `b` for the groups:

   ```python
   import numpy as np
   from scipy import stats

   def welch_t(X, a, b):
       ma, mb = X[:, a].mean(1), X[:, b].mean(1)
       va, vb = X[:, a].var(1, ddof=1), X[:, b].var(1, ddof=1)
       na, nb = a.sum(), b.sum()
       se2 = va / na + vb / nb
       t = (ma - mb) / np.sqrt(se2)
       df = se2 ** 2 / ((va / na) ** 2 / (na - 1) + (vb / nb) ** 2 / (nb - 1))
       return t, 2 * stats.t.sf(np.abs(t), df)
   ```

   The work is the same, a few arithmetic operations per value, but it is done by compiled loops over contiguous arrays instead of $20\,000$ interpreted function calls, each with its own overhead of argument checking and object creation; the speed-up is typically two to three orders of magnitude. `scipy.stats.ttest_ind(X[:, a], X[:, b], axis=1, equal_var=False)` does the same. With four samples per group, however, gene-wise variances are unstable, and the moderated statistics of limma or the count models of DESeq2 are preferable ([7.7.20](/7.7.20)).

7. Ignoring the donor reduced the airway result from $4691$ to $3422$ genes at FDR $0.1$. Explain the mechanism in terms of the model, and say when ignoring a pairing would not cost power.

   **Answer** With `~ cell + dex` the donor means are parameters, and the dispersion measures only the variation of each donor's treated sample around its predicted value; with `~ dex` the donor-to-donor differences remain in the residuals, inflating the estimated dispersion of every gene with donor-dependent expression and hence the standard errors of the treatment effect. The donor effect costs three degrees of freedom, which matters little with eight samples when the donor variation is large. If donors did not differ (no between-donor variance), the paired model would only lose degrees of freedom and gain nothing; pairing pays when the within-pair correlation is substantial, as here, where PC2 and later components separate the donors.

8. A study compares tumors processed in 2019 with normal tissues processed in 2023 and finds $8000$ differentially expressed genes. ComBat with year as batch removes most of them. Which result is right?

   **Answer** Neither can be trusted, because year and tissue type are completely confounded: the data contain no information to separate them. Before correction, the differences are tumor effects plus batch effects; after "correction" for year, the tumor effects have been removed together with the batch, since ComBat cannot tell them apart. The only remedies are design ones: process new samples of both kinds together, or include within each batch some samples of the other kind (for example tumor-adjacent normal tissue from 2019) to estimate the batch effect separately.

9. A p-value histogram from a differential-expression analysis of $15\,000$ genes is flat except for a broad hump between $0.6$ and $0.9$ and a deficit near $0$. What does this suggest?

   **Answer** The null p-values are not uniform: the test is conservative, giving too large p-values. Typical causes are an overestimated variance (for example a strong unmodeled factor inflating the dispersion of many genes, or an outlier sample), or a test whose assumptions do not hold for the data, such as a $t$ test on discrete low counts. One should look for hidden structure (PCA of residuals, SVA), check for outlier samples, and refit with the missing covariates. A well-specified analysis with no differential expression would give a flat histogram, one with true changes a flat floor with a peak near zero.
