---
title: Epigenomes and the Three-Dimensional Genome
description: "Genome-wide measurements of the regulatory state of chromatin and their analysis: transcription-factor binding in vitro and in vivo (ChIP-seq, CUT&RUN, CUT&Tag), strand cross-correlation, peak calling with a local Poisson background, IDR and quality metrics; chromatin accessibility (DNase-seq, ATAC-seq, fragment-length ladders, digital footprints, chromVAR motif deviations, single-cell ATAC); histone modifications and chromatin states with ChromHMM; DNA methylation by bisulfite and direct sequencing, beta-binomial tests for differentially methylated regions, epigenetic clocks and cell-free DNA; the three-dimensional genome from 3C to Hi-C and Micro-C, matrix balancing, contact decay, A/B compartments, domains by insulation and directionality, loops and loop extrusion, structural variants; and the linking of regulatory elements to genes and disease variants with the activity-by-contact model."
---

The genome sequence is the same in every cell of an organism; what differs between a neuron and a hepatocyte is which parts of it are used. That choice is written in chromatin: which regions are accessible, which transcription factors are bound, how histones are modified, which cytosines are methylated, and which distant regions are folded together in the nucleus. Each of these layers can now be measured genome-wide, usually by converting a property of chromatin into a set of DNA fragments and sequencing them. This chapter treats the main measurements and the statistical models that turn their reads into regulatory maps: transcription-factor binding and peak calling (8.2), accessibility and footprints (8.3), histone modifications and chromatin states (8.4), DNA methylation (8.5), the three-dimensional organization of the genome (8.6), and the connection of regulatory elements to their target genes and to the variants found by genetic association studies (8.7). The molecular biology of chromatin is in [7.2.4](/7.2.4) and [7.2.15](/7.2.15), the experimental principles of ChIP, footprinting and library preparation in [7.2.6](/7.2.6), the polymer physics of chromosomes in [7.6.21](/7.6.21), and the representation and discovery of binding motifs in [7.8.8](/7.8.8). The regulatory networks built from these data are the subject of [7.9.11](/7.9.11).

## 8.1. Layers of Regulatory Information

The layers differ in what they report and in how directly they relate to gene activity.

| Layer | What is measured | Main assays | Typical signal |
|---|---|---|---|
| Accessibility | DNA not protected by nucleosomes | DNase-seq, ATAC-seq, MNase-seq (the converse: nucleosome positions) | peaks of $100$–$1000$ bp at promoters, enhancers, insulators |
| Factor binding | DNA bound by one protein | ChIP-seq, ChIP-exo, CUT&RUN, CUT&Tag | narrow peaks at motifs |
| Histone modifications | nucleosomes carrying one mark | ChIP-seq or CUT&Tag with mark-specific antibodies | narrow (H3K4me3, H3K27ac) or broad (H3K27me3, H3K36me3) domains |
| DNA methylation | 5-methylcytosine at each CpG | bisulfite or enzymatic conversion with sequencing, arrays, nanopore and PacBio reads | a fraction per CpG, usually high except at CpG islands and active enhancers |
| 3D structure | pairs of loci in spatial proximity | 3C, 4C, 5C, Hi-C, Micro-C, ChIA-PET, HiChIP; imaging | contact matrices: compartments, domains, loops |

The marks are correlated but not redundant. Active promoters are accessible, carry H3K4me3 and H3K27ac, and lie in unmethylated **CpG islands** ([7.2.15](/7.2.15#sec-15.7)); active **enhancers** are accessible and marked by H3K4me1 and H3K27ac; Polycomb-repressed genes carry H3K27me3; constitutive **heterochromatin** carries H3K9me3 and methylated DNA. Which mark causes which, and which merely follows transcription, is an open question for each locus; the measurements describe states, and causal statements need perturbations.

## 8.2. Transcription-Factor Binding

### 8.2.1. Methods

Where a transcription factor binds can be measured outside the cell, on naked DNA, or inside it, in chromatin.

| Method | Setting | Output | Strengths | Limitations |
|---|---|---|---|---|
| EMSA (gel shift, [7.2.6](/7.2.6)) | in vitro | binding to one probe | direct; affinities | one sequence at a time |
| Protein-binding microarrays | in vitro | binding to all $10$-mers on an array | complete motif specificity | naked DNA; no partners |
| SELEX, HT-SELEX | in vitro | sequences enriched over rounds of selection | long motifs, dimers | selection biases |
| Yeast one-hybrid | in a heterologous cell | which factors activate a reporter driven by a promoter | screens factor libraries against a promoter | false positives and negatives |
| ChIP-seq | in vivo | genomic regions crosslinked to the factor | real chromatin context, genome-wide | antibody quality; indirect binding; millions of cells |
| ChIP-exo | in vivo | ChIP with exonuclease trimming to the crosslink | near base-pair resolution | more complex library |
| CUT&RUN, CUT&Tag | in situ, permeabilized cells | DNA released by an antibody-tethered MNase (CUT&RUN) or Tn5 (CUT&Tag) | low background; thousands of cells or single cells | no crosslinking: weak or transient binding may be lost |

The in vitro methods give the intrinsic sequence preference of a factor, summarized by a **position weight matrix** ([7.8.8](/7.8.8)), which has the meaning of a binding energy ([7.6.41](/7.6.41#sec-41.3)). In cells, only a small fraction of the motif matches in the genome is bound: chromatin, cooperating factors and competing nucleosomes decide which. Comparing the transcriptomes of a factor's mutant and the wild type (with replicates, [7.9.2](/7.9.2)) and searching the promoters of affected genes for enriched motifs identifies candidate direct targets, but cannot distinguish direct from indirect effects. **ChIP-seq** ([7.2.6](/7.2.6)), the in vivo map of binding, is the workhorse of this section.

### 8.2.2. The Shape of a Binding Site in ChIP-seq Data

In ChIP-seq, crosslinked chromatin is fragmented to about $150$–$300$ bp, fragments bound by the factor are immunoprecipitated, and one end (single-end) or both ends (paired-end) of each fragment are sequenced. A fragment covering a binding site yields a read starting at its left end on the plus strand or at its right end on the minus strand, so around a site the plus-strand reads pile up upstream and the minus-strand reads downstream, separated by about one fragment length $d$ (figure below, panel A). Shifting each read by $d/2$ toward its $3'$ end, or extending it to length $d$, centers the signal on the site.

**Definition 8.2.1 (Strand Cross-Correlation)** The strand cross-correlation of a ChIP-seq library is the Pearson correlation, as a function of the shift $\delta$, between the genome-wide profile of plus-strand read starts and that of minus-strand read starts shifted by $\delta$. Its maximum at $\delta = d$ estimates the fragment length. The normalized strand coefficient is $\mathrm{NSC} = \mathrm{cc}(d)/\min_\delta \mathrm{cc}(\delta)$, and the relative strand coefficient $\mathrm{RSC} = (\mathrm{cc}(d) - \min\mathrm{cc})/(\mathrm{cc}(r) - \min\mathrm{cc})$ compares the fragment peak with the "phantom" peak at the read length $r$, which comes from mappability rather than binding.

Good libraries show a fragment-length peak well above the phantom peak; the ENCODE guidelines regard $\mathrm{NSC} > 1.05$ and $\mathrm{RSC} > 0.8$ as acceptable (Landt and colleagues, 2012). In real data the correlation is far from zero at all shifts, because of the clustering of background reads, so NSC values of $1.05$–$2$ are typical; the clean background of a simulation gives much larger values.

### 8.2.3. Peak Calling

**Definition 8.2.2 (Peak Calling)** **Peak calling** is the identification of genomic intervals in which reads of an enrichment assay (ChIP-seq, CUT&RUN, ATAC-seq and others) are significantly more frequent than expected from a background model, usually estimated from a control library (input chromatin, or a nonspecific antibody) of the same sample.

The background is not uniform. Open chromatin is fragmented more easily, amplified regions and copy-number gains give more reads, repeats and regions with unusual GC content are over- or under-represented. A global background rate would call all such regions peaks; the control library, processed identically, carries the same biases and can correct them.

**Algorithm 8.2.1 (Peak Calling with a Local Poisson Background)** (MACS; Zhang and colleagues, 2008)

1. Estimate the fragment length $d$ from the strand cross-correlation, or from paired-end reads directly, and shift every read by $d/2$ toward its $3'$ end (remove duplicate reads beyond what the sequencing depth predicts).
2. Scale the control to the same depth as the ChIP. Slide a window of width $2d$ across the genome and count the ChIP reads $k$ in it.
3. For each window, compute the local background
$$
\lambda_{\mathrm{local}} = \max\bigl(\lambda_{\mathrm{BG}}, \lambda_{1\,\mathrm{k}}, \lambda_{5\,\mathrm{k}}, \lambda_{10\,\mathrm{k}}\bigr),
$$
where $\lambda_{\mathrm{BG}}$ is the genome-wide expectation for a window and $\lambda_{1\,\mathrm{k}}, \lambda_{5\,\mathrm{k}}, \lambda_{10\,\mathrm{k}}$ are the control rates in $1$, $5$ and $10\,\mathrm{kb}$ around the window, rescaled to the window width: the largest plausible background.
4. The p-value of the window is $\mathbb{P}(X \ge k)$ for $X \sim \mathrm{Poi}(\lambda_{\mathrm{local}})$ (**Poisson distribution**). Merge adjacent significant windows into peaks, report the summit (the position of maximal pileup) and the fold enrichment $k/\lambda_{\mathrm{local}}$.
5. Control the **false discovery rate** across positions by the **Benjamini–Hochberg procedure**, or empirically by swapping ChIP and control and counting the "peaks" of the control.

The cost is linear in the number of reads. Broad marks (H3K27me3, H3K36me3) need a different model, for example a broad mode that links nearby weaker regions or methods built on windows of several kilobases (SICER, epic2), since no single window is enriched.

**Example 8.2.1** With $2d = 410$ bp and a genome-wide expectation of $\lambda_{\mathrm{BG}} = 24$ reads per window, a window with $45$ reads has $p = \mathbb{P}(X \ge 45) = 8.3 \times 10^{-5}$. If the control shows a fourfold higher background around it, $\lambda_{\mathrm{local}} = 96$ and the same $45$ reads are depleted, not enriched; $140$ reads would be needed for $p \approx 1.5 \times 10^{-5}$. In the simulation of the figure ($300$ sites on $2\,\mathrm{Mb}$, a $30\,\mathrm{kb}$ stretch with fourfold background in both libraries), the global background turns the whole biased stretch into one $30.5\,\mathrm{kb}$ "peak", within which its four real sites are buried; the local background finds $291$ of the $300$ sites as peaks no wider than $1.1\,\mathrm{kb}$, including two of the four in the biased stretch, and calls no region without a site. The fragment length estimated from the cross-correlation is $205$ bp for a true mean of $200$ bp.

![Peak calling for ChIP-seq with a local Poisson background (simulated: 300 binding sites with about 40 fragments each on top of 100000 background fragments in a 2 Mb region; a 30 kb stretch with fourfold background in both ChIP and input). A: plus-strand (above) and minus-strand (below) read starts around binding sites (dashed). B: the strand cross-correlation (Definition 8.2.1) peaks at the fragment length. C: −log10 p of window counts with the global background (thin) and with the local background of Algorithm 8.2.1 from the input (thick); dotted: p = 1e−5; triangles: true sites. The global background calls the whole biased stretch (shaded) as one enriched region](./plots/peak_calling.py)

### 8.2.4. Reproducibility and Quality

Peaks called at a lenient threshold in two biological replicates are ranked by significance, and the agreement of the two rankings decides how many are kept.

**Definition 8.2.3 (Irreproducible Discovery Rate)** (Li, Brown, Huang and Bickel, 2011) Model the pairs of ranks of peaks found in both replicates as a mixture of a reproducible component, in which the ranks are positively correlated, and an irreproducible one, in which they are independent (a copula mixture model). The local irreproducible discovery rate of a peak is the posterior probability that it belongs to the irreproducible component; the IDR of a set of peaks is the average of these probabilities, and ENCODE keeps peaks with IDR below $0.05$.

IDR uses replicates as they should be used: not by pooling them, which hides disagreement, but by asking which signals both see. Further checks are the fraction of reads in peaks (FRiP; it grows with the number of peaks, so it is compared between experiments on the same factor), the enrichment of the factor's known motif at the summits (centered within a few tens of base pairs for direct binding), the concentration of peaks at promoters and enhancers, and peaks found in many unrelated ChIP-seq experiments, the "hyper-ChIPable" or blacklisted regions (high-copy repeats, rRNA genes), which are removed. Differential binding between conditions is tested on read counts in a common set of peaks with the count models of [7.9.2](/7.9.2), with replicates and normalization by the reads in peaks or by spike-ins when global binding changes.

## 8.3. Chromatin Accessibility

### 8.3.1. Nucleases and Transposases

Nucleosomes protect $147$ bp of DNA ([7.2.4](/7.2.4)), and bound factors protect shorter stretches; the rest of the genome is accessible to enzymes. Four assays read this out:

- MNase-seq digests linker DNA with micrococcal nuclease and sequences the protected mononucleosomal fragments, mapping nucleosome positions (**nucleosome positioning**).
- DNase-seq sequences the ends of DNase I cuts; cuts concentrate in **DNase I hypersensitive sites**, the regulatory elements.
- FAIRE-seq separates nucleosome-depleted DNA by phenol–chloroform extraction after crosslinking.
- ATAC-seq inserts sequencing adapters with a hyperactive Tn5 transposase.

**Definition 8.3.1 (ATAC-seq)** **ATAC-seq** (assay for transposase-accessible chromatin with sequencing; Buenrostro and colleagues, 2013) is the measurement of chromatin accessibility by tagmentation of nuclei with Tn5 transposase loaded with sequencing adapters, which cuts accessible DNA and joins adapters in one step; each sequenced fragment has two insertion sites at its ends.

Because cutting and adapter ligation happen in one reaction, a library can be made from a few thousand cells, or from single nuclei, in hours. Tn5 inserts as a dimer with a $9$-bp duplication of the target, so the exact insertion sites are obtained by shifting plus-strand read starts by $+4$ bp and minus-strand starts by $-5$ bp. Quality is assessed by the fraction of fragments in peaks, by the transcription start site enrichment (the read density at TSSs relative to flanking regions), and by the fragment-length distribution.

The fragment lengths record chromatin structure (figure below, panel A). Fragments from nucleosome-free regions are shorter than $147$ bp and show a $10.5$-bp periodicity, because Tn5 cuts on one face of the DNA helix; longer fragments span one, two or more nucleosomes and form a ladder near $200$, $400$ and $600$ bp. In the simulated distribution of the figure, $37\,\%$ of fragments are shorter than $147$ bp, the ladder peaks lie at $196$, $389$ and $596$ bp, and the spectrum of the short fragments has its maximum at a period of $10.5$ bp. Fragment lengths can be separated before peak calling: short fragments map factor binding, long ones nucleosomes.

### 8.3.2. Footprints

Within an accessible region, a bound factor protects the few base pairs under it, which leave a dip in the cut profile: a footprint. **DNase I footprinting** on a single fragment of DNA ([7.2.6](/7.2.6)) became, with deep sequencing, digital genomic footprinting (Hesselberth and colleagues, 2009), and footprints of hundreds of factors were mapped across dozens of human cell types (Neph and colleagues, 2012).

**Formula 8.3.1 (Footprint occupancy score)** (Neph and colleagues, 2012) For a candidate site with $C$ cuts in its central segment and $L$, $R$ cuts in flanking segments of fixed length on either side, the footprint occupancy score is
$$
\mathrm{FOS} = \frac{C + 1}{L} + \frac{C + 1}{R}, \tag{8.1}
$$
small when the center is depleted relative to both flanks. Sites with FOS below a threshold, calibrated on shuffled cut profiles, are called footprints.

**Example 8.3.1** In the simulation of the figure, half of $1000$ motif sites are bound and lose $85\,\%$ of the insertions in the central $20$ bp. The aggregate profile of bound sites shows a deep footprint. For single sites, the median FOS is $0.61$ for bound and $2.0$ for unbound sites, and a threshold of $1$ calls $74\,\%$ of the bound and $10\,\%$ of the unbound sites footprints: single-site footprints need many cuts per site, and at typical depths they are reliable only for well-covered sites.

![Two signatures of ATAC-seq data (simulated). A: the fragment-length distribution: nucleosome-free fragments with a 10.5-bp helical modulation (inset), and fragments spanning one, two and three nucleosomes, above a smooth background. B: aggregate insertion profiles around motif sites of a transcription factor, bound (with a footprint over the motif) and unbound. C: footprint occupancy scores (Formula 8.3.1) of single sites](./plots/atac_fragments.py)

:::

Footprints have limits. DNase I and Tn5 have sequence preferences that produce footprint-like shapes even on naked DNA, which must be corrected by models of the enzyme's bias estimated from deproteinized DNA (methods such as TOBIAS); and factors that bind briefly, such as nuclear receptors, leave little or no footprint although they regulate their targets (Sung and colleagues, 2014). The absence of a footprint is therefore weak evidence of absence of binding.

### 8.3.3. Motif Accessibility and Single-Cell ATAC

Accessibility data rarely tell directly which factor opened a region. An indirect route asks whether the regions containing a factor's motif are, together, more accessible in some samples than expected.

**Formula 8.3.2 (Motif accessibility deviation)** (chromVAR; Schep and colleagues, 2017) Let $X_{ij}$ be the fragments of sample or cell $j$ in peak $i$, $m_{ik} = 1$ if peak $i$ contains motif $k$, and $E_{ij} = \bigl(\sum_{j'}X_{ij'}/\sum_{i',j'}X_{i'j'}\bigr)\sum_{i'}X_{i'j}$ the expected fragments if the cell's reads were distributed like those of all cells. The raw deviation of motif $k$ in cell $j$ is
$$
y_{jk} = \frac{\sum_i m_{ik}X_{ij} - \sum_i m_{ik}E_{ij}}{\sum_i m_{ik}E_{ij}}, \tag{8.2}
$$
and it is standardized to a z-score by the mean and standard deviation of the same quantity for random sets of peaks matched to the motif's peaks in GC content and average accessibility.

The deviations summarize tens of thousands of sparse peaks by a few hundred interpretable variables, the activity of each motif family. In human hematopoiesis, the accessibility of GATA motifs rises along the erythroid lineage and tracks GATA1 expression, while that of other families (CEBP in myeloid cells) marks other branches (Corces and colleagues, 2016). Similar motifs of related factors cannot be separated, and a motif's accessibility can rise because of a different factor that binds a similar sequence.

In single-cell ATAC-seq, a cell yields a few thousand to tens of thousands of fragments over hundreds of thousands of possible peaks, so the data are almost binary: a peak is open in a cell or not observed. Analysis binarizes the peak-by-cell matrix, weights it by term frequency times inverse document frequency (TF-IDF) and reduces it by a truncated singular value decomposition (latent semantic indexing, as in text analysis), then follows the graph-based clustering of [7.9.5](/7.9.5#sec-5.5). Genes are linked to nearby peaks whose accessibility correlates with their expression across cells, measured in the same nuclei (multiome) or matched across data sets; gene activity scores sum the accessibility around each gene. Atlases of single-cell accessibility across human tissues have defined candidate cis-regulatory elements (cCREs) cell type by cell type; the ENCODE registry alone lists about $0.9$ million human cCREs (ENCODE Project Consortium, 2020). Enrichment of GWAS variants of a disease in the cCREs of one cell type points to the cell type through which the disease acts (8.7).

## 8.4. Histone Modifications and Chromatin States

### 8.4.1. Marks and Domains

ChIP-seq or CUT&Tag with antibodies against modified histones maps the modifications reviewed in [7.2.15](/7.2.15#sec-15.2). Each mark has a typical genomic distribution:

| Mark | Distribution | Associated with |
|---|---|---|
| H3K4me3 | sharp peaks at promoters | active or poised promoters |
| H3K27ac | peaks at promoters and enhancers | active elements |
| H3K4me1 | broader peaks at enhancers | enhancers, active or primed |
| H3K36me3 | broad over transcribed gene bodies | elongation |
| H3K79me2 | $5'$ parts of transcribed genes | elongation |
| H3K27me3 | broad domains up to $100$ kb | Polycomb repression (**Polycomb group**) |
| H3K9me3 | broad domains, repeats, zinc-finger clusters | heterochromatin |

Combinations matter more than single marks. In embryonic stem cells, the promoters of many developmental genes carry both H3K4me3 and H3K27me3 (bivalent promoters, Bernstein and colleagues, 2006), which resolve to one mark or the other upon differentiation. Clusters of enhancers with unusually strong H3K27ac or Mediator signal, **super-enhancers** ([7.2.21](/7.2.21)), are found by stitching enhancer peaks within $12.5$ kb and ranking the stitched regions by total signal; the regions above the point where the slope of the ranked curve reaches $1$ are called super-enhancers (Whyte and colleagues, 2013). They are enriched near genes that define cell identity and near oncogenes in tumors.

### 8.4.2. Segmentation into Chromatin States

With $M$ marks measured along the genome, the combination at each position can be summarized by a small number of recurrent patterns.

**Definition 8.4.1 (Chromatin State)** A *chromatin state* is a class of genomic segments defined by a recurrent combination of chromatin marks, learned without supervision from genome-wide data, together with a label (active promoter, strong enhancer, transcribed, Polycomb-repressed, heterochromatin, quiescent) assigned by the enrichment of each class at known annotations.

**Formula 8.4.1 (Multivariate HMM segmentation)** (ChromHMM; Ernst and Kellis, 2010) Divide the genome into bins of $200$ bp and binarize each mark in each bin: $o_{tm} = 1$ if its read count exceeds the threshold of a Poisson test against the genome-wide mean ($p < 10^{-4}$), else $0$. A **hidden Markov model** ([4.6.8](/4.6.8)) with $K$ hidden states has transition probabilities $a_{kl}$ between consecutive bins and emissions that are independent Bernoulli variables given the state,
$$
\mathbb{P}(\boldsymbol{o}_t \mid z_t = k) = \prod_{m=1}^{M} p_{km}^{o_{tm}}(1 - p_{km})^{1 - o_{tm}}. \tag{8.3}
$$
The parameters are estimated by the **Baum–Welch algorithm**, and each bin is assigned its most probable state by posterior decoding.

The number of states is a choice of resolution; it is fixed by the interpretability of the states and by how well models with more states reproduce the states of smaller ones. The Roadmap Epigenomics Consortium (2015) applied a $15$-state model of five marks (H3K4me3, H3K4me1, H3K36me3, H3K27me3, H3K9me3) to $111$ reference epigenomes; a few percent of the genome falls in active promoter and enhancer states in any cell type, and most of it is in a quiescent state without marks. Segmentations of many cell types make it possible to ask, for any region, in which cell types it is an enhancer.

## 8.5. DNA Methylation

### 8.5.1. Measurements

In mammals, methylation of cytosine at CpG dinucleotides (**DNA methylation**, [7.2.15](/7.2.15#sec-15.7)) affects about $70$–$80\,\%$ of the roughly $28$ million CpGs of the human genome in somatic cells; unmethylated CpGs concentrate in CpG islands and active regulatory elements. Sodium bisulfite deaminates unmethylated cytosine to uracil, read as thymine after amplification, while 5-methylcytosine is protected. Sequencing converted DNA and comparing it with the reference gives, at each CpG, $M$ reads with C (methylated) and $U$ reads with T (unmethylated).

| Method | Coverage | Notes |
|---|---|---|
| Whole-genome bisulfite sequencing (WGBS) | all CpGs | the reference method; bisulfite degrades DNA; reads have reduced complexity (C becomes T), so special aligners map them (Bismark, bwa-meth) |
| Reduced representation (RRBS) | CpG-rich regions | digestion with MspI (CCGG) and size selection enrich CpG islands; cheaper |
| Enzymatic conversion (EM-seq) | all CpGs | TET2 and APOBEC3A instead of bisulfite; less DNA damage |
| Arrays (Illumina EPIC) | about $850\,000$–$930\,000$ chosen CpGs | cheap and standard in epidemiology and clinical cohorts |
| Nanopore, PacBio | CpGs on long single molecules | direct detection from the signal; phased methylation haplotypes |

Bisulfite and enzymatic conversion do not distinguish 5-methylcytosine from 5-hydroxymethylcytosine, the oxidation product made by TET enzymes; oxidative bisulfite sequencing and related methods separate them. Incomplete conversion makes unmethylated C look methylated; its rate is measured on spiked-in unmethylated DNA (bacteriophage λ) or on non-CpG cytosines, which are almost unmethylated in most mammalian cells, and should be well below $1\,\%$.

### 8.5.2. Methylation Levels and Their Variation

The methylation level of a CpG in a sample is estimated by $\hat\beta = M/(M + U)$, the fraction of methylated reads; on arrays, the analogous $\beta$ value is computed from two fluorescence intensities, and the logit $\log_2\bigl(\beta/(1 - \beta)\bigr)$, the M value, is used for linear models because its variance depends less on the mean. A sample is a population of cells, and $\beta$ is the fraction of DNA copies methylated, so values between $0$ and $1$ mean heterogeneity among cells or between the two alleles (imprinted regions are near $0.5$, [7.4](/7.4)).

Given the true level $m$ of a sample, $M$ is binomial with $M + U$ trials. Between biological replicates, $m$ itself varies.

**Formula 8.5.1 (Beta-binomial model of bisulfite counts)** For CpG $i$ in sample $j$ of group $g$, with coverage $N_{ij}$,
$$
M_{ij} \mid m_{ij} \sim \mathrm{Bin}(N_{ij}, m_{ij}), \qquad m_{ij} \sim \mathrm{Beta} \text{ with mean } \mu_{ig} \text{ and dispersion } \rho, \tag{8.4}
$$
so that $\mathbb{E}[M_{ij}] = N_{ij}\mu_{ig}$ and $\operatorname{Var}(M_{ij}) = N_{ij}\mu_{ig}(1 - \mu_{ig})\bigl[1 + (N_{ij} - 1)\rho\bigr]$ (**beta-binomial distribution**). The factor $1 + (N - 1)\rho$ is the variance inflation due to biological variation; with $\rho = 0$ the model is binomial.

The analogy with the negative binomial model of RNA-seq counts ([7.9.2](/7.9.2)) is exact: sampling noise of reads on top of biological variation between samples. Tests that pool the reads of replicates and compare groups by Fisher's exact test treat reads as independent units and ignore the second level.

**Example 8.5.1** A CpG has $18$ of $20$ methylated reads in one sample and $6$ of $20$ in another. Fisher's exact test gives $p = 2.4 \times 10^{-4}$, and a binomial Wald statistic is $z = (0.9 - 0.3)/\sqrt{0.9 \cdot 0.1/20 + 0.3 \cdot 0.7/20} = 4.9$. With dispersion $\rho = 0.09$ the variance is inflated by $1 + 19 \times 0.09 = 2.71$, and $z = 4.9/\sqrt{2.71} = 2.98$, $p = 0.003$. In the figure, $20\,000$ CpGs without any difference between two groups of three samples ($\rho = 0.09$) are tested both ways: Fisher's test on pooled reads calls $15\,\%$ significant at $p < 0.05$, three times the nominal rate, while a Wald test with the variance of Formula 8.5.1 and $\rho$ estimated from the data ($\hat\rho = 0.094$) calls $6.3\,\%$.

![Methylation levels from bisulfite sequencing and the test for differential methylation (simulated: beta-distributed true levels between replicates, Poisson coverage with mean 12). A: 40 CpGs in three samples of each of two groups with a differentially methylated region (shaded); points are single-sample levels, lines running means of the pooled group levels. B: p-values of 20000 null CpGs from Fisher's exact test on reads pooled over replicates, and from a Wald test with the beta-binomial variance of Formula 8.5.1](./plots/methylation.py)

### 8.5.3. Differentially Methylated Regions

Neighboring CpGs are correlated over hundreds of base pairs, and differences that matter biologically usually involve many of them.

**Definition 8.5.1 (Differentially Methylated Region)** A *differentially methylated region* (DMR) is a genomic interval of several consecutive CpGs whose methylation levels differ between groups of samples, beyond the variation between replicates, by more than a chosen magnitude.

DMR callers borrow strength from neighbors in two steps. BSmooth (Hansen, Langmead and Irizarry, 2012) smooths each sample's levels along the genome by local likelihood, computes a t-like statistic per CpG from the smoothed values across replicates, and reports runs of CpGs with statistics beyond a cutoff; DSS (Feng, Conneely and Wu, 2014) uses the beta-binomial model of Formula 8.5.1 with dispersions shrunk across CpGs by an empirical Bayes prior and a Wald test, then joins significant CpGs into regions. Significance of whole regions is assessed by permutation of sample labels, since the regions were selected from the same data.

### 8.5.4. Methylation as a Biomarker

Methylation states are stable in DNA, specific to cell types and altered systematically in cancer and with age, which makes them good biomarkers.

- Age. An **epigenetic clock** is a penalized regression (elastic net, [7.7.21](/7.7.21)) of age on methylation levels; Horvath's clock (2013) uses $353$ CpGs and predicts the age of most tissues with a median error of $3.6$ years. The difference between predicted and actual age is studied as a marker of biological aging.
- Tissue of origin. Cell-free DNA in plasma comes from dying cells, mostly blood cells, with a tumor fraction in cancer patients. Its fragments are about $167$ bp, the length of DNA on a nucleosome plus a linker, and their methylation patterns, compared with reference methylomes of cell types, identify the tissues of origin; phased patterns of several neighboring CpGs on one fragment (methylation haplotypes) are more specific than single CpGs (Guo and colleagues, 2017).
- Cancer detection. A targeted methylation assay of cell-free DNA for many cancer types had a specificity of $99.5\,\%$, an overall sensitivity of $51.5\,\%$ (much lower for stage I than for stage IV) and predicted the tissue of the cancer signal correctly in $88.7\,\%$ of the detected cases (Klein and colleagues, 2021). The positive predictive value depends on the prevalence (**sensitivity**, **specificity** and Bayes' rule, [7.7.3](/7.7.3)): with $1\,\%$ undiagnosed cancer in the tested population, $\mathrm{PPV} = 0.515 \times 0.01/(0.515 \times 0.01 + 0.005 \times 0.99) = 0.51$; with $0.5\,\%$ it is $0.34$. In a prospective study of about $6600$ adults, the PPV was $38\,\%$ (Schrag and colleagues, 2023). Whether such screening reduces mortality is being tested in randomized trials.

## 8.6. The Three-Dimensional Genome

### 8.6.1. From 3C to Hi-C

The two meters of DNA in a human nucleus are folded at many scales: chromosomes occupy territories, active and inactive regions segregate, domains of hundreds of kilobases interact internally, and loops bring enhancers to promoters ([7.2.4](/7.2.4#sec-4.3)). **Chromosome conformation capture** (3C, Dekker and colleagues, 2002) measures proximity by chemistry: crosslink chromatin with formaldehyde, digest it with a restriction enzyme, ligate the ends in dilute conditions so that crosslinked fragments join each other, and detect the junctions. The variants differ in which junctions they read.

| Method | Measures | Year |
|---|---|---|
| 3C | one pair of loci, by PCR | 2002 |
| 4C | all loci contacting one viewpoint | 2006 |
| 5C | all pairs among many chosen loci | 2006 |
| Hi-C | all pairs genome-wide: biotin marks the ligation junctions, which are pulled down and sequenced as read pairs | 2009 |
| in situ Hi-C | ligation in intact nuclei; higher resolution | 2014 |
| ChIA-PET, HiChIP | contacts anchored at sites bound by one protein (by ChIP) | 2009, 2016 |
| Micro-C | MNase instead of a restriction enzyme: nucleosome resolution | 2015 (yeast), 2020 (mammals) |
| single-cell Hi-C, imaging (chromatin tracing) | contacts or 3D positions in single cells | 2013, 2016 onward |

**Definition 8.6.1 (Hi-C)** **Hi-C** (Lieberman-Aiden and colleagues, 2009) is the genome-wide version of chromosome conformation capture in which ligation junctions between crosslinked fragments are labeled with biotin, enriched and sequenced from both ends; each valid read pair is a contact between the two genomic loci it maps to, and the counts of contacts between all pairs of genomic bins form a symmetric contact matrix.

### 8.6.2. From Read Pairs to a Contact Matrix

Each read of a pair is mapped separately (chimeric reads that span the junction are split), and pairs are classified: pairs within one restriction fragment (undigested "dangling ends", self-ligated circles) carry no contact information and are removed, as are PCR duplicates. The remaining valid pairs are binned at a resolution set by depth: the number of bin pairs grows with the square of the number of bins. At $10$ kb, the human genome has $3.1 \times 10^5$ bins and $4.8 \times 10^{10}$ bin pairs on and above the diagonal, so a matrix with useful counts at that resolution needs billions of contacts; the in situ Hi-C map of the lymphoblastoid cell line GM12878 had about $4.9$ billion (Rao and colleagues, 2014).

Contacts are biased: restriction fragment lengths, GC content and mappability make some bins more visible than others. Explicit models regress counts on these covariates (HiCNorm, a Poisson regression; Hu and colleagues, 2012); the standard approach assumes nothing about the sources and removes a visibility factor per bin.

**Algorithm 8.6.1 (Iterative Correction)** (ICE; Imakaev and colleagues, 2012) Assume the observed counts are $O_{ij} = b_ib_jT_{ij}$ with a bias $b_i$ per bin and a true matrix $T$ in which every bin has the same total coverage.

1. Remove the diagonal (and possibly the first off-diagonals) and bins with very low coverage.
2. Repeat: compute the row sums $r_i = \sum_j O_{ij}$, divide them by their mean, and replace $O_{ij}$ by $O_{ij}/(r_ir_j)$, accumulating $b_i \leftarrow b_ir_i$.
3. Stop when all row sums are equal to within a tolerance.

The cost per iteration is linear in the number of nonzero entries, and a few tens of iterations suffice.

The algorithm is the symmetric form of a classical matrix-scaling procedure.

**Theorem 8.6.1 (Sinkhorn–Knopp)** If a square nonnegative matrix $A$ has total support (every positive entry lies on a positive diagonal, for example if $A$ is positive), there are positive diagonal matrices $D_1$, $D_2$ such that $D_1AD_2$ is doubly stochastic, and $D_1AD_2$ is unique; alternately normalizing rows and columns converges to it. For symmetric $A$ one can take $D_1 = D_2$.

The assumption of equal coverage is strong: amplified or deleted regions in cancer genomes violate it, and copy-number-aware normalizations are used there. In the simulation of the figure below, ICE converges in $49$ iterations to a tolerance of $10^{-3}$, and the recovered biases correlate with the true ones with $r = 0.977$.

### 8.6.3. Contact Decay and Compartments

The most prominent feature of every contact matrix is the decay of contact frequency with genomic distance, $P(s)$, which tests polymer models of chromatin (**contact probability**, [7.6.21](/7.6.21#sec-21.6.2)): human interphase chromosomes follow $P(s) \propto s^{-1.08}$ over about $0.5$–$7$ Mb, close to the prediction for a **fractal globule**. To see structure beyond this decay, each diagonal of the matrix is divided by its mean, which gives the observed/expected matrix.

**Definition 8.6.2 (A/B Compartments)** The **A/B compartments** are two classes of genomic regions, typically hundreds of kilobases to several megabases long, such that regions of the same class contact each other more often than expected at their distance and regions of different classes less often: the A compartment is gene-rich, accessible and active, the B compartment gene-poor, late-replicating and often at the nuclear lamina.

**Algorithm 8.6.2 (Compartments from the First Eigenvector)** (Lieberman-Aiden and colleagues, 2009)

1. Compute the observed/expected matrix of one chromosome at a resolution of $50$–$500$ kb and its Pearson correlation matrix $C$, whose entry $(i, j)$ correlates the contact profiles of bins $i$ and $j$.
2. Compute the eigenvector $\boldsymbol{e}_1$ of $C$ for its largest eigenvalue (**principal component analysis** of the correlation matrix).
3. Orient the sign so that $\boldsymbol{e}_1$ correlates positively with gene density, GC content or active marks; bins with $e_{1,i} > 0$ are assigned to A, those with $e_{1,i} < 0$ to B.

**Example 8.6.1** The figure simulates a chromosome of $300$ bins with alternating compartments, domains and bin biases. The raw matrix shows stripes of bins with high or low visibility; after balancing, the checkerboard of compartments and the triangles of domains appear; the correlation matrix of the observed/expected values has the plaid pattern of two classes; and the sign of its first eigenvector, which explains $20\,\%$ of the variance of $C$, assigns all bins to their true compartment. Higher-resolution maps split the compartments into subcompartments (A1, A2, B1–B4 in Rao and colleagues, 2014) with distinct marks and nuclear positions.

![From raw Hi-C counts to compartments (simulated chromosome of 300 bins of 40 kb with A/B compartments, domains, contact decay 1/s and log-normal bin biases; about 3 million contacts). A: raw counts, log scale. B: after iterative correction (Algorithm 8.6.1). C: Pearson correlation of the observed/expected matrix. D: the first eigenvector (Algorithm 8.6.2) against the true compartments](./plots/hic_ice.py)

### 8.6.4. Domains and Loops

Along the diagonal, contact maps are divided into squares within which contacts are enriched: **topologically associating domains** (TADs, Dixon and colleagues, 2012; Nora and colleagues, 2012), typically $0.1$–$1$ Mb in mammals ([7.2.4](/7.2.4#sec-4.3)). Their boundaries are enriched in CTCF binding, housekeeping genes and transfer RNA genes.

**Definition 8.6.3 (Insulation Score)** (Crane and colleagues, 2015) The insulation score of bin $i$ is the mean contact frequency in a square of $w \times w$ bins of the balanced matrix that joins the $w$ bins upstream of $i$ to the $w$ bins downstream, usually expressed as $\log_2$ of its ratio to the chromosome-wide mean. Boundaries between domains are local minima of the insulation score, where few contacts cross.

The directionality index of Dixon and colleagues (2012) measures instead whether a bin contacts its upstream or its downstream neighbors more: with $A$ and $B$ the contacts of bin $i$ with the $w$ bins upstream and downstream and $E = (A + B)/2$,
$$
\mathrm{DI}_i = \operatorname{sgn}(B - A)\Bigl[\frac{(A - E)^2}{E} + \frac{(B - E)^2}{E}\Bigr], \tag{8.5}
$$
negative at the end of a domain and positive at its start; a hidden Markov model of DI segments the genome into domains.

**Example 8.6.2** On the simulated chromosome (figure), the insulation score with $w = 5$ bins finds all $19$ true domain boundaries in the interior, within one bin, together with $7$ further minima; all seven lie at switches between compartments, which also reduce the contacts crossing them. Domain and compartment boundaries coincide in part in real data as well, and callers are compared on their agreement across methods and resolutions rather than with a ground truth.

![Domains and their boundaries in the simulated, balanced Hi-C map. A: the matrix for bins 100–200 with true domain boundaries (ticks at the top edge) and boundaries called from the insulation score (dashed). B: the insulation score (Definition 8.6.3; triangles: called minima; dotted: true boundaries). C: the directionality index (Eq. (8.5))](./plots/tad_insulation.py)

:::

At kilobase resolution, many domains are seen to be bounded by peaks of contact between their corners: loops. HiCCUPS (Rao and colleagues, 2014) finds them as pixels enriched over a local background (a "donut" around the pixel and the regions below and to the left of it, all at the same distance from the diagonal), with Poisson tests and a false discovery rate computed separately for ranges of expected counts. About $10\,000$ loops were found in GM12878, and in more than $90\,\%$ of the loops with CTCF motifs at both anchors the two motifs point toward each other, a convergent orientation that inverting a single motif disrupts.

These observations are explained by **loop extrusion** ([7.2.4](/7.2.4#sec-4.3), [7.6.21](/7.6.21)): **cohesin** loaded onto chromatin extrudes a loop of growing size until it meets CTCF bound in the orientation that blocks it. Condensin extrudes DNA in vitro at up to about $1500$ bp per second, as single-molecule imaging showed (Ganji and colleagues, 2018). Acute degradation of cohesin removes loops and domains within hours, while compartments remain and even strengthen (Rao and colleagues, 2017): the two levels are formed by different mechanisms, compartments by the segregation of chromatin of similar state, domains and loops by extrusion. Gene expression changed surprisingly little upon loss of loops in these experiments, which suggests that most loops tune rather than switch genes.

### 8.6.5. Rewiring the Genome in Disease

Structural variants can move a gene into another regulatory landscape. At the human *EPHA4* locus, deletions, inversions and duplications that remove or move a TAD boundary bring limb enhancers into contact with *WNT6*, *IHH* or *PAX3*, and each causes a different limb malformation (brachydactyly, F-syndrome, polydactyly); mice engineered with the same variants reproduce the defects and the ectopic contacts (Lupiáñez and colleagues, 2015). In gliomas with *IDH* mutations, the oncometabolite 2-hydroxyglutarate inhibits TET demethylases, CTCF sites become hypermethylated, CTCF no longer binds them, and a lost domain boundary lets an enhancer activate the oncogene *PDGFRA* (Flavahan and colleagues, 2016). In tumors with many copy-number changes, breakpoints are enriched near domain boundaries and loop anchors, which may reflect the double-strand breaks made by topoisomerase II to relieve torsional stress at anchors. Mapping 3D structure is therefore part of interpreting noncoding structural variants in patients.

## 8.7. From Regulatory Elements to Genes and Variants

### 8.7.1. Linking Enhancers to Target Genes

An enhancer can regulate a gene hundreds of kilobases away, skipping nearer genes, so assigning elements to the nearest gene is often wrong. Tools for interpreting sets of regions, such as GREAT (McLean and colleagues, 2010), assign each region to genes whose regulatory domain (a basal region around the transcription start plus an extension up to the nearest neighbors' basal regions) contains it, and test the region set for enrichment of gene functions. Better predictions combine activity with contact.

**Formula 8.7.1 (Activity-by-contact model)** (Fulco and colleagues, 2019) For an element $E$ and a gene $G$ within $5$ Mb, let the activity $A_E$ be the geometric mean of the element's accessibility and H3K27ac signal, and $C_{E,G}$ the contact frequency between element and promoter from Hi-C (or from a power law of distance when no Hi-C is available). The ABC score is the element's share of the regulatory input of the gene,
$$
\mathrm{ABC}_{E,G} = \frac{A_EC_{E,G}}{\sum_{e \text{ within } 5\,\mathrm{Mb of } G} A_eC_{e,G}}, \tag{8.6}
$$
and element–gene pairs with a score above a threshold (about $0.02$) are predicted to be regulatory.

The model was calibrated against CRISPR interference of enhancers with a fluorescent in situ readout of gene expression (CRISPRi-FlowFISH), which tested more than $3500$ element–gene pairs for $30$ genes, and predicted the effects better than distance or activity alone.

**Example 8.7.1** A gene has three candidate elements with activities $A = 10$, $4$ and $30$ (arbitrary units) and contacts $C = 0.05$, $0.4$ and $0.01$. The products are $0.5$, $1.6$ and $0.3$, so the ABC scores are $0.21$, $0.67$ and $0.12$. The most active element is the least likely regulator of this gene, because it rarely contacts the promoter; the moderately active element with frequent contact dominates. All three pass the threshold of $0.02$, and a CRISPRi experiment would be expected to reduce expression by roughly the corresponding shares if the model's assumption of additive inputs holds.

### 8.7.2. Variants in Regulatory Elements

Most variants found by **genome-wide association studies** ([7.4.25](/7.4.25)) lie outside protein-coding sequence: $88\,\%$ of the trait-associated variants catalogued by 2009 were intronic or intergenic (Hindorff and colleagues, 2009). Regulatory maps turn such associations into mechanisms in three steps:

1. Which variant? Statistical **fine-mapping** ([7.4.25](/7.4.25#sec-25.4.1)) gives credible sets of candidate causal variants; those overlapping accessible chromatin, footprints or disrupted motifs in a relevant cell type gain priority.
2. Which cell type? Heritability of the trait is enriched in the regulatory elements of the cell types through which it acts, as stratified LD score regression and related methods estimate; for example, variants for Alzheimer's disease are enriched in elements accessible in microglia and myeloid cells.
3. Which gene? Element–gene links (ABC, Hi-C, correlation of accessibility with expression) and expression quantitative trait loci (**eQTLs**) connect the variant to a gene. Colocalization tests whether the association signal for the trait and the eQTL signal share one causal variant rather than two variants in linkage disequilibrium: coloc (Giambartolomei and colleagues, 2014) computes the posterior probabilities of the hypotheses of no association, association with one trait only, two distinct variants, and one shared variant.

The *FTO* locus treated in [7.4.25](/7.4.25#sec-25.4.2) is the classic example: the obesity-associated variants lie in an intron of *FTO* but act through an adipocyte-progenitor enhancer that contacts *IRX3* and *IRX5* half a megabase away. Each of the three steps can fail, and the final evidence is experimental: editing the variant and measuring the target gene and the cellular phenotype.

## Summary

| Layer | Measurement | Model or algorithm | Key point | Section |
|---|---|---|---|---|
| Factor binding | ChIP-seq, CUT&RUN, CUT&Tag | strand cross-correlation (Definition 8.2.1); peak calling with local Poisson background (Definition 8.2.2, Algorithm 8.2.1); IDR (Definition 8.2.3) | the control removes local biases (Example 8.2.1); replicates decide reproducibility | 8.2 |
| Accessibility | DNase-seq, ATAC-seq (Definition 8.3.1) | fragment-length ladder; footprints (Formula 8.3.1); motif deviations (Formula 8.3.2); TF-IDF/LSI for single cells | footprints need depth and bias correction (Example 8.3.1) | 8.3 |
| Histone marks | ChIP-seq, CUT&Tag | chromatin states by multivariate HMM (Definition 8.4.1, Formula 8.4.1); super-enhancer ranking | combinations of marks define states | 8.4 |
| DNA methylation | WGBS, RRBS, EM-seq, arrays, long reads | beta-binomial counts (Formula 8.5.1); DMRs (Definition 8.5.1) | replicates, not reads (Example 8.5.1); biomarkers: clocks, cfDNA | 8.5 |
| 3D structure | Hi-C (Definition 8.6.1), Micro-C, HiChIP | iterative correction (Algorithm 8.6.1, Theorem 8.6.1); compartments from E1 (Definition 8.6.2, Algorithm 8.6.2); insulation (Definition 8.6.3), DI (Eq. (8.5)); loops | compartments by segregation, domains and loops by extrusion | 8.6 |
| Elements to genes | Hi-C, accessibility, H3K27ac, eQTLs | ABC model (Formula 8.7.1); fine-mapping, colocalization | noncoding variants act through cell-type-specific elements | 8.7 |

All these assays share a design: convert a chromatin property into DNA fragments, count them, and compare the counts with a background that carries the same biases. The statistics are those of counts with two levels of variation, sampling and biology, and the conclusions about regulation they support are correlational until tested by perturbation.

## Questions

1. Why does a ChIP-seq peak caller use a control library, and why does MACS take the maximum of several background estimates rather than, for example, their average?

   **Answer** The control (input chromatin) is fragmented, sequenced and mapped like the ChIP sample and therefore carries the same biases: open chromatin, copy-number gains, repeats and GC effects all raise the read density without binding. Comparing ChIP reads with the local control rate removes them; a global rate would call every such region (Example 8.2.1). Taking the maximum of $\lambda_{\mathrm{BG}}$ and the control rates in $1$, $5$ and $10$ kb chooses, for each window, the largest plausible background, which is conservative: a true peak must exceed the background at every scale, and a sharp local bias (seen in the $1$ kb rate) or a broad one (seen in the $10$ kb rate) cannot produce a false call. Averaging would dilute a local bias by the lower rates around it.

2. A window of $2d = 400$ bp contains $30$ ChIP reads. The genome is $3 \times 10^9$ bp and the library has $2 \times 10^7$ reads. Compute the p-value against the genome-wide background. If the control indicates a local rate three times the genome-wide one, what is the p-value now?

   **Answer** $\lambda_{\mathrm{BG}} = 2 \times 10^7 \times 400/(3 \times 10^9) = 2.67$. $\mathbb{P}(X \ge 30 \mid \lambda = 2.67)$ is astronomically small (about $10^{-21}$). With $\lambda_{\mathrm{local}} = 8$, $\mathbb{P}(X \ge 30)$ is about $10^{-9}$: still a strong peak, with fold enrichment $30/8 = 3.75$ instead of $11$. The local correction changes the significance of a strong peak by orders of magnitude but does not remove it; it removes the weak "peaks" that are merely biased regions.

3. In an ATAC-seq experiment, $15\,\%$ of the fragments are shorter than $147$ bp, the fragment-length distribution has no visible nucleosome ladder, and the TSS enrichment is low. What went wrong, and what does a good library look like?

   **Answer** A library with few nucleosome-free fragments, no periodicity and low TSS enrichment suggests over-digestion of damaged or dead cells (Tn5 accesses naked DNA everywhere, giving a uniform background), too much transposase for too few nuclei, or contamination by mitochondrial DNA (which lacks nucleosomes and can take most reads). A good library has a large fraction of short fragments with a $10.5$-bp modulation, a clear ladder near $200$, $400$ and $600$ bp (figure in 8.3.1), a high fraction of reads in peaks and a TSS enrichment well above that of the flanks; remedies are better nuclei preparation (detergents that remove mitochondria, as in Omni-ATAC), fewer dead cells and a titrated Tn5-to-nuclei ratio.

4. Compute the footprint occupancy score (Formula 8.3.1) for a site with $3$ cuts in the center and $30$ and $24$ in the flanks, and for a site with $12$ cuts in the center and $15$ and $12$ in the flanks. Which is the stronger footprint, and why should footprints of short-lived binders be interpreted with care?

   **Answer** First site: $4/30 + 4/24 = 0.133 + 0.167 = 0.30$. Second site: $13/15 + 13/12 = 0.867 + 1.083 = 1.95$. The first is a deep footprint (center depleted about eightfold), the second shows no protection. A factor with a residence time of seconds is often absent when the enzyme cuts, so its sites are protected only in a small fraction of DNA copies and the footprint is shallow or absent, although the factor regulates the site; conversely, enzyme sequence bias can create footprint-like dips on naked DNA. FOS thresholds must be calibrated and the enzyme bias corrected.

5. Explain the chromVAR deviation (Formula 8.3.2) for a cell that has $600$ fragments in peaks containing a motif when the expected number is $500$, and why the z-score uses background peak sets matched in GC content and accessibility.

   **Answer** The raw deviation is $(600 - 500)/500 = 0.2$: the motif's peaks hold $20\,\%$ more of the cell's fragments than expected. Whether that is unusual depends on technical variation: cells differ in their fraction of reads in GC-rich or highly accessible peaks because of PCR and Tn5 biases and quality, and a motif whose peaks are GC-rich would show deviations from that alone. Background peak sets with the same GC and accessibility distribution undergo the same technical effects, so the z-score $(0.2 - \text{mean of background deviations})/\text{s.d.}$ isolates the part attributable to the motif.

6. Three replicates per group have methylated/total reads at one CpG of $(9/10, 14/16, 11/12)$ in group 1 and $(6/10, 9/12, 4/10)$ in group 2. Pool the reads and test the difference with a binomial Wald test, then with the beta-binomial variance with $\rho = 0.1$.

   **Answer** Group 1: $34/38 = 0.895$; group 2: $19/32 = 0.594$; difference $0.301$. Binomial: $\operatorname{Var}(\hat p_1) = 0.895 \times 0.105/38 = 0.00247$, $\operatorname{Var}(\hat p_2) = 0.594 \times 0.406/32 = 0.00754$, $z = 0.301/\sqrt{0.0100} = 3.01$. Beta-binomial (Formula 8.5.1 summed over samples): for group 1, $\sum_j N_j[1 + (N_j - 1)0.1] = 10 \times 1.9 + 16 \times 2.5 + 12 \times 2.1 = 84.2$, so $\operatorname{Var}(\hat p_1) = 0.895 \times 0.105 \times 84.2/38^2 = 0.00548$; for group 2, $10 \times 1.9 + 12 \times 2.1 + 10 \times 1.9 = 63.2$, $\operatorname{Var}(\hat p_2) = 0.594 \times 0.406 \times 63.2/32^2 = 0.0149$; $z = 0.301/\sqrt{0.0204} = 2.11$, $p = 0.035$. The variation between replicates shrinks $z$ by about $30\,\%$ and raises the p-value more than tenfold (from $0.003$ to $0.035$); with three replicates per group and many CpGs tested, this CpG alone is not convincing, and a DMR of several such CpGs would be.

7. Run one step of iterative correction by hand on the symmetric matrix with zero diagonal and off-diagonal entries $O_{12} = 40$, $O_{13} = 12$, $O_{14} = 4$, $O_{23} = 30$, $O_{24} = 8$, $O_{34} = 20$. Which bin is most visible, and what does the first step do?

   **Answer** Row sums: bin 1: $56$, bin 2: $78$, bin 3: $62$, bin 4: $32$; mean $57$, so $r = (0.982, 1.368, 1.088, 0.561)$. Bin 2 has the highest visibility and bin 4 the lowest. The first step divides each entry by $r_ir_j$: for example $O_{12} = 40/(0.982 \times 1.368) = 29.8$ and $O_{34} = 20/(1.088 \times 0.561) = 32.8$; the new row sums are $48.2$, $60.3$, $64.1$ and $50.4$, much closer to each other than before ($32$ to $78$). Iterating converges (Theorem 8.6.1) to a matrix with all row sums equal; note that this also removes any genuine difference in total contacts between bins, which is the price of the equal-visibility assumption.

8. In Example 8.7.1, suppose a deletion removes the second element. What are the new ABC scores, and what would the model predict for the gene's expression? What experiment tests the prediction?

   **Answer** The remaining products are $0.5$ and $0.3$, with scores $0.625$ and $0.375$. Under the model's assumption that expression is proportional to the summed input $\sum_e A_eC_{e,G}$, the input falls from $2.4$ to $0.8$, a $67\,\%$ reduction in expression. A CRISPRi experiment targeting the element (or a CRISPR deletion in a cell line), with expression measured by qPCR, FlowFISH or single-cell RNA-seq, tests it; departures from $67\,\%$ reveal nonadditive interactions between enhancers (redundancy, synergy) or compensation, which the model ignores.

9. After acute depletion of cohesin, loops and TADs disappear from Hi-C maps but A/B compartments remain and sharpen. What does this imply about the mechanisms of chromosome organization? Predict what happens after depletion of CTCF.

   **Answer** Two mechanisms act: loop extrusion by cohesin forms loops and domains, and the segregation of chromatin of similar state (active with active, inactive with inactive, perhaps by phase separation or binding of similar proteins) forms compartments; extrusion actively mixes chromatin across compartment boundaries, so its loss lets compartments become purer. After CTCF depletion, cohesin still extrudes but is no longer stopped at boundaries, so loop and domain boundaries anchored by CTCF weaken or vanish while extrusion continues (more random loops, fewer corner peaks), and compartments are largely unchanged; this is what CTCF degron experiments show.

10. (Analysis) A GWAS locus for an autoimmune disease has a credible set of $12$ variants in an intergenic region between two genes. Plan how to identify the causal variant, the cell type and the target gene.

    **Answer** Overlap the credible set with accessibility (ATAC-seq or single-cell ATAC) and H3K27ac maps of immune cell types; check which cell types show heritability enrichment for the disease and which variants lie in elements accessible in them; look for variants that disrupt or create motifs, with allele-specific accessibility or binding in heterozygous samples. Link the elements to genes with ABC scores from Hi-C or HiChIP in the relevant cell type, and test colocalization of the GWAS signal with eQTLs in that cell type (stimulated if the disease involves activation). Validate by CRISPRi of the element and base editing of the top variant in primary cells or a model line, measuring the candidate genes and a cellular phenotype (cytokine production, proliferation); a massively parallel reporter assay can test all $12$ alleles for regulatory activity at once.
