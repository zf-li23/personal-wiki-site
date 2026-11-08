---
title: Single-Cell Transcriptomics
description: "Measuring the transcriptome of individual cells: why averages mislead, the technologies (cell isolation, cell barcodes and UMIs, Poisson loading and multiplets, combinatorial indexing), from reads to a count matrix (empty droplets, ambient RNA, doublets, sequencing saturation), the statistics of UMI counts (negative binomial sampling, the zero-inflation question, normalization and Pearson residuals, highly variable genes, imputation), principal components, nearest-neighbor graphs and clustering by community detection, t-SNE and UMAP, annotation by markers and references, pseudobulk analysis against pseudoreplication, composition and batch integration, multimodal and deconvolution methods, and the scverse workflow with AnnData, scanpy and scvi-tools."
---

A tissue is a mixture of cell types and states, and a bulk transcriptome ([7.9.2](/7.9.2)) reports the weighted average of their expression. Single-cell RNA sequencing measures the transcripts of each cell separately: tens of thousands of cells per experiment, millions in atlas projects. The price is sparsity. A mammalian cell contains a few hundred thousand mRNA molecules, of which a droplet protocol captures and counts a few thousand, so most genes are observed zero or a few times in each cell. This chapter follows the data from the experiment to the biological conclusion: why single cells (5.1), how cells and molecules are labeled (5.2), how reads become a matrix of molecule counts with the empty droplets, contamination and doublets removed (5.3), what statistical model the counts follow (5.4), how cells are embedded and grouped into clusters by community detection on a nearest-neighbor graph (5.5), how clusters are named and compared between conditions without pseudoreplication (5.6), measurements beyond RNA (5.7), and the scverse software ecosystem in which these steps are carried out (5.8). The physical origin of cell-to-cell variation in transcript numbers is in [7.6.32](/7.6.32); the general methods of dimension reduction and clustering are in [3.4](/3.4) and [4.6](/4.6); the mathematics of community detection is in [network science](/1.4.7). Cell trajectories and fates, which use the same data, are the subject of [7.9.7](/7.9.7), and measurements that keep the positions of cells in a tissue that of [7.9.6](/7.9.6).

## 5.1. Why Single Cells

An average can hide everything that matters. A bulk measurement cannot tell whether a gene rose in every cell or a cell type that expresses it became more frequent, whether expression is graded or bimodal, or whether a rare population exists at all.

**Example 5.1.1** A tissue contains cell type A, expressing a gene at $10$ molecules per cell, and type B at $100$. If the fraction of B rises from $20\,\%$ to $40\,\%$ after an injury, the bulk level rises from $0.8 \times 10 + 0.2 \times 100 = 28$ to $0.6 \times 10 + 0.4 \times 100 = 46$, a $1.64$-fold increase, without any cell changing its expression. A bulk differential expression analysis would report an induced gene; single-cell data report a change of composition.

:::

Variation between cells of one type is itself informative. Gene expression is stochastic, with transcripts made in **transcriptional bursts** ([7.6.32](/7.6.32#sec-32.4)), and cells pass through states (cycle phases, differentiation stages, responses to signals) at different times, so a snapshot of many cells samples a dynamic process. Single-cell data have revealed new cell types (for example a subset of dendritic cells in human blood, Villani and colleagues, 2017), rare cells such as the pulmonary ionocyte that expresses most of the *CFTR* mRNA of the airway epithelium (2018), and the composition of tumors and their immune infiltrates. The Human Cell Atlas (founded in 2016) aims at reference maps of all human cell types; Tabula Sapiens (2022) profiled about $500\,000$ cells from $24$ organs, most from the same donors; perturbation atlases now profile cells after thousands of drug or genetic perturbations, up to about $10^8$ cells in one data set.

## 5.2. Technologies

### 5.2.1. Isolating Cells

**Definition 5.2.1 (Single-Cell RNA Sequencing)** **Single-cell RNA sequencing** (scRNA-seq) is the sequencing of transcripts from individual cells or nuclei in which every cDNA molecule is labeled, before the material of different cells is pooled, with a sequence that identifies its cell of origin.

Dissociation of a tissue into a suspension of live single cells comes first; it stresses the cells (inducing immediate early genes such as *FOS* within minutes), loses fragile or large cells (neurons, adipocytes) and changes the proportions. Single-nucleus RNA-seq of frozen tissue avoids enzymatic dissociation at the cost of measuring only nuclear RNA, richer in unspliced pre-mRNA. Cells or nuclei are then separated by one of four principles:

| Principle | Examples | Cells per experiment | Transcript coverage | Note |
|---|---|---|---|---|
| Sorting into plates | **fluorescence-activated cell sorter** (FACS) into 96- or 384-well plates; Smart-seq2, Smart-seq3 | $10^2$–$10^3$ | full length | sensitive; isoforms, mutations (7.9.4); costly per cell |
| Microfluidic chambers | Fluidigm C1 | $10^2$ | full length | historical |
| Droplets or microwells | Drop-seq, inDrop (2015), 10x Genomics Chromium, Seq-Well, BD Rhapsody | $10^3$–$10^5$ | $3'$ or $5'$ ends with UMIs | the standard for atlases |
| Combinatorial indexing | sci-RNA-seq, SPLiT-seq | $10^5$–$10^7$ | $3'$ ends | no isolation: fixed cells are barcoded in successive rounds of pooling and splitting |

### 5.2.2. Cell Barcodes and UMIs

**Definition 5.2.2 (Cell Barcode)** A **cell barcode** is a short sequence, the same for all capture oligonucleotides delivered to one cell (on one bead, in one well, or by one combination of indexing rounds), that is copied into every cDNA made from that cell so that reads can be assigned to cells after pooling.

In the 10x Genomics $3'$ chemistry (figure), each gel bead carries millions of oligonucleotides, each made of a primer site for sequencing read $1$, a $16$-nt cell barcode identical on the bead, a $12$-nt **unique molecular identifier** (UMI, [7.8.9](/7.8.9#sec-9.3.3)) that differs between oligonucleotides, and a $30$-nt poly(dT). A microfluidic chip encapsulates beads and cells in nanoliter droplets of reagent in oil (gel beads in emulsion, GEMs). The cell lyses, its polyadenylated mRNAs anneal to the oligonucleotides, and **reverse transcription** with **template switching** adds a known sequence at the $5'$ end of each cDNA. The droplets are then broken, and the barcoded cDNA of all cells is amplified and made into one library. Read $1$ ($28$ nt) gives barcode and UMI, read $2$ (about $90$ nt) a piece of the transcript near its $3'$ end. Because amplified copies of one molecule share barcode and UMI, counting distinct UMIs counts molecules and removes the amplification bias; the remaining error is the capture efficiency, about $10$–$40\,\%$ of the mRNA molecules of a cell in current droplet methods.

![Barcoding in a droplet experiment (the 10x Genomics 3′ chemistry). A: a cell and a gel bead enclosed in an oil droplet; the lysed cell's mRNAs bind to the bead's oligonucleotides. B: each oligonucleotide carries a read 1 primer site, a 16-nt cell barcode shared by all oligos of the bead, a 12-nt UMI that differs between oligos, and poly(dT); reverse transcription copies the mRNA, and template switching at its 5′ end adds a known sequence (TSO). C: the final library molecule: read 1 (28 nt) reads barcode and UMI, the index read the sample, read 2 the cDNA near the 3′ end of the transcript](./plots/droplet_barcoding.py)

### 5.2.3. Loading Statistics

Cells enter droplets at random. Beads are packed so that nearly every droplet receives exactly one, but the number of cells per droplet follows a **Poisson distribution** with mean $\lambda$, the ratio of cells loaded to droplets made.

**Formula 5.2.1 (Multiplet rate)** With $\lambda$ cells per droplet on average, the fraction of droplets with at least one cell is $1 - \mathrm{e}^{-\lambda}$, and among them the fraction with two or more is
$$
m(\lambda) = \frac{1 - \mathrm{e}^{-\lambda} - \lambda\mathrm{e}^{-\lambda}}{1 - \mathrm{e}^{-\lambda}} = \frac{\lambda}{2} + O(\lambda^2). \tag{5.1}
$$
The multiplet rate grows linearly with the number of cells loaded.

**Example 5.2.1** A channel produces of the order of $10^5$ droplets, and about $60\,\%$ of the loaded cells are recovered. Recovering $1000$ cells requires loading about $1650$, so $\lambda = 0.0165$ and $m = 0.8\,\%$, the multiplet rate of "about $0.8\,\%$ per $1000$ cells" quoted for such instruments; for $10\,000$ recovered cells, $\lambda = 0.165$ and $m = 8.0\,\%$ (figure in 5.3.4, panel B). Experimenters trade throughput against multiplets, and sample multiplexing (5.3.3) lets them overload a channel and remove the multiplets afterwards. Only $1.6\,\%$ of droplets contain a cell at $\lambda = 0.0165$: the rest contain only beads and ambient RNA.

:::

In combinatorial indexing, a cell's barcode is the combination of indices received in $r$ rounds of splitting into $b$ wells, so there are $B = b^r$ barcodes; with $N$ cells, a given cell shares its combination with another with probability $1 - (1 - 1/B)^{N - 1} \approx 1 - \mathrm{e}^{-N/B}$. Three rounds of $96$ wells give $B = 884\,736$; with $10^5$ cells, $10.7\,\%$ of the cells collide, so a fourth round or fewer cells are needed.

## 5.3. From Reads to a Count Matrix

### 5.3.1. The Pipeline

The primary analysis, run by Cell Ranger for 10x data or by the faster open alternatives STARsolo, alevin-fry and kallisto|bustools, has five steps: (1) correct cell barcodes against the list of barcodes present on the beads, allowing one mismatch; (2) align read $2$ to the genome with a spliced aligner, or pseudo-align it to the transcriptome ([7.8.10](/7.8.10)); (3) assign each read to a gene, counting intronic reads as well for nuclei; (4) collapse reads with the same barcode, UMI and gene into one molecule, merging UMIs that differ by one base (the directional method, [Algorithm 9.3.1](/7.8.9#alg-9.3.1)); (5) decide which barcodes are cells. The output is a sparse matrix of UMI counts, genes by barcodes, of which typically more than $90\,\%$ of the entries are zero.

```bash
# 10x data: count UMIs per gene and cell against a prebuilt reference
cellranger count --id=pbmc --transcriptome=refdata-gex-GRCh38-2024-A \
                 --fastqs=fastq/ --sample=pbmc --create-bam=false --localcores=16
# The same with STARsolo (barcode whitelist of the chemistry; Gene and GeneFull counts)
STAR --genomeDir star_index --readFilesIn pbmc_R2.fastq.gz pbmc_R1.fastq.gz --readFilesCommand zcat \
     --soloType CB_UMI_Simple --soloCBwhitelist 3M-february-2018.txt --soloUMIlen 12 \
     --soloFeatures Gene GeneFull --soloCellFilter EmptyDrops_CR --runThreadN 16
```

### 5.3.2. Cells, Empty Droplets and Ambient RNA

Most barcodes come from droplets without a cell, which still contain mRNA released from damaged cells into the suspension: *ambient RNA*. On a log–log plot of the total UMI count of each barcode against its rank (the barcode rank plot, figure below, panel A), cell barcodes form a plateau at thousands of UMIs, followed by a steep drop (the knee) to the empty droplets with tens of UMIs. A threshold at the knee misses small cells, whose totals approach the ambient level. EmptyDrops (Lun and colleagues, 2019) tests each barcode against the ambient profile instead.

**Algorithm 5.3.1 (Distinguishing Cells from Empty Droplets)**

1. Ambient profile: sum the counts of barcodes with very few UMIs (for example below $100$), which are certainly empty, and estimate the ambient expression proportions $\boldsymbol{a} = (a_1, \dots, a_G)$, with a small pseudocount.
2. Null model: an empty droplet with total $t$ has counts drawn from a Dirichlet-multinomial distribution with mean proportions $\boldsymbol{a}$ (the Dirichlet allows for more variation than a multinomial).
3. Test: for each barcode above the low threshold, compute the log-probability of its counts under the null model, and obtain a p-value by comparing it with the log-probabilities of profiles simulated from the null with the same total (Monte Carlo).
4. Decision: call cells at a false discovery rate (for example $0.1\,\%$), and keep all barcodes above the knee regardless.

Ambient RNA also contaminates the real cells: a T cell in a sample with many lysed red cells contains hemoglobin transcripts. SoupX and CellBender estimate the ambient profile from empty droplets and subtract, cell by cell, a contribution proportional to it; the contamination fraction is often $2$–$10\,\%$ and can reach $20\,\%$ in difficult tissues. Low-quality cells are removed by three metrics, usually with thresholds at a few median absolute deviations from the median of each sample: few detected genes or UMIs (empty or damaged droplets), and a high fraction of mitochondrial transcripts (cells whose cytoplasmic mRNA leaked out through a broken membrane while the mitochondria kept theirs).

### 5.3.3. Doublets

**Definition 5.3.1 (Doublet)** A **doublet** is a barcode whose counts come from two cells captured together (more generally a multiplet); it is *heterotypic* if the two cells are of different types and *homotypic* if they are of the same type.

Heterotypic doublets are the harmful ones: they look like intermediate states or new cell types expressing markers of two lineages. Computational detection simulates them.

**Algorithm 5.3.2 (Doublet Scoring by Simulation)** (Scrublet; Wolock, Lopez and Klein, 2019)

1. Simulate doublets by adding the counts of randomly chosen pairs of observed barcodes, about twice as many as there are barcodes.
2. Normalize observed and simulated profiles together, project them onto principal components, and build a $k$-nearest-neighbor graph of all of them.
3. The doublet score of an observed barcode is the fraction of simulated doublets among its neighbors, corrected for the ratio of simulated to observed barcodes; call doublets above a threshold between the two modes of the score distribution.

The cost is that of the neighbor search, nearly linear in the number of barcodes with approximate methods. Homotypic doublets cannot be found this way, since they resemble single cells of the type, but they do less harm. Experimental methods are more reliable: in cell hashing, cells of different samples are labeled with antibodies to ubiquitous surface proteins carrying sample-specific oligonucleotide barcodes, and a droplet with two sample barcodes is a doublet; with genetically different donors, natural variants in the reads identify the donor of each cell (demuxlet, souporcell) and reveal doublets of cells from different donors. Pooling and demultiplexing several samples in one channel also removes the batch effect between those samples.

### 5.3.4. Sequencing Saturation

How deeply should a library be sequenced? Each read samples one of the molecules in the library of a cell; at first most reads reveal new molecules, later most repeat known ones.

**Formula 5.3.1 (Sequencing saturation)** If $r$ reads of a cell reveal $U(r)$ distinct molecules (barcode–UMI–gene combinations), the *sequencing saturation* is
$$
\mathrm{sat}(r) = 1 - \frac{U(r)}{r}, \tag{5.2}
$$
the fraction of reads that repeat an already observed molecule. If the cell's library contains $M$ molecules, each present in amplified copies whose numbers follow a gamma distribution with shape $k$, the number of distinct molecules seen is
$$
U(r) = M\Bigl[1 - \Bigl(1 + \frac{r}{Mk}\Bigr)^{-k}\Bigr], \tag{5.3}
$$
which tends to $M(1 - \mathrm{e}^{-r/M})$ when all molecules are equally abundant ($k \to \infty$). The derivation is that of the zero class of the negative binomial (5.4.1): a molecule with relative abundance $\lambda$ is missed by $r$ reads with probability $\mathrm{e}^{-\lambda r/M}$, averaged over a gamma distribution of $\lambda$.

**Example 5.3.1** One library of about $10\,000$ cells was sequenced on one, two, three and four lanes, with mean reads per cell $17\,959$, $35\,479$, $52\,576$ and $69\,880$ and reported saturations $41.3$, $58.5$, $68.0$ and $74.0\,\%$; the median number of detected genes per cell rose from $1489$ to $1879$, $2051$ and $2152$ (data of Zhang and colleagues, 2020). Fitting Eq. (5.3) by least squares gives $M = 22\,600$ molecules per cell and $k = 1.39$, and reproduces the four saturations to within $0.1$ percentage point; equal abundances ($k \to \infty$, $M = 16\,900$) fit worse (figure, panel C). The fitted model predicts that $90\,\%$ saturation would need about $213\,000$ reads per cell, three times the deepest run, for only about $17\,\%$ more molecules. Most experiments stop at $20\,000$–$50\,000$ reads per cell: beyond that, more cells are usually worth more than more reads per cell.

![Three quantitative checks of a droplet experiment. A: barcode rank plot (simulated): UMIs per barcode against rank, both on log scales, for 8000 cell-containing droplets among 150000 barcodes of empty droplets with ambient RNA; the knee separates cells (dark) from background. B: the multiplet rate of Formula 5.2.1 as a function of the number of cells recovered, assuming about 1e5 droplets per channel and 60% recovery of loaded cells. C: sequencing saturation of one library sequenced on one to four lanes (points: data of Zhang and colleagues, 2020) with Eq. (5.3) fitted for equal molecule abundances (dashed) and for gamma-distributed abundances (solid); dotted: 90% saturation](./plots/barcode_rank.py)

## 5.4. Statistics of UMI Counts

### 5.4.1. The Sampling Model

Let $x_{gc}$ be the UMI count of gene $g$ in cell $c$. Molecules are captured and sequenced independently, each with a small probability, so given the true numbers of molecules the counts are close to Poisson; the true numbers vary between cells of one type because of bursty transcription and differences in cell size and state. Integrating a Poisson count over a gamma-distributed rate gives the **negative binomial distribution**, the same result as for bursty protein production ([Theorem 32.4.1](/7.6.32#thm-32.4.1)).

**Formula 5.4.1 (Negative binomial model of UMI counts)** In a population of cells of one type,
$$
x_{gc} \sim \text{negative binomial with mean } \mu_{gc} = s_c\,q_g \text{ and shape } \theta_g, \qquad \operatorname{Var}(x_{gc}) = \mu_{gc} + \frac{\mu_{gc}^2}{\theta_g}, \tag{5.4}
$$
where $s_c$ is the size factor of the cell (its total captured molecules, proportional to the product of its mRNA content and the capture efficiency) and $q_g$ the expected fraction of the cell's molecules from gene $g$. The probability of a zero is $\mathbb{P}(x_{gc} = 0) = (1 + \mu_{gc}/\theta_g)^{-\theta_g}$, and $\mathrm{e}^{-\mu_{gc}}$ in the Poisson limit $\theta_g \to \infty$.

The many zeros of single-cell data were long called "dropouts" and modeled by zero-inflated distributions, with an extra probability of a technical zero. For UMI data from droplets this is not needed (Svensson, 2020): across genes, the fraction of zeros follows the negative binomial prediction from each gene's mean, and genes of mean $0.5$ are zero in about $61$–$64\,\%$ of cells simply because $\mathrm{e}^{-0.5} = 0.61$ (Poisson) and $(1 + 0.5/2)^{-2} = 0.64$ (negative binomial, $\theta = 2$). Excess zeros appear when the cells are heterogeneous, for example for a marker expressed in only one of two types (figure, panel A), and they reflect biology. Full-length protocols without UMIs, in which amplification and capture fail more erratically, do show genuine zero inflation. The statistical debate and its consequences for differential expression are taken up in [7.7.20](/7.7.20).

### 5.4.2. Normalization

Cells differ in size factor by an order of magnitude, and the first task is to remove this technical variation. Three approaches are common.

1. Scaling and the shifted logarithm: divide each cell's counts by its total and multiply by a common constant (the median total, or $10^4$), then take $\log(1 + y)$. Simple and robust, it is the default of most pipelines, but the variance of the result still depends on the mean, and genes with high expression dominate the subsequent steps less than those of intermediate expression (figure, panel B).
2. Pooled size factors (scran): estimate size factors on pools of cells, where counts are less sparse, and deconvolve them to individual cells, as in the median-of-ratios method of bulk RNA-seq ([7.7.20](/7.7.20)).
3. Model residuals: fit the count model of Formula 5.4.1 and use residuals, which have approximately unit variance for genes without biological variation.

**Formula 5.4.2 (Analytic Pearson residuals)** (Lause, Berens and Kobak, 2021) With $n_c = \sum_g x_{gc}$, $n_g = \sum_c x_{gc}$ and $n = \sum_{g,c}x_{gc}$, take the expected count $\hat\mu_{gc} = n_cn_g/n$ and a common shape $\theta$ (for example $100$). The normalized value is
$$
z_{gc} = \frac{x_{gc} - \hat\mu_{gc}}{\sqrt{\hat\mu_{gc} + \hat\mu_{gc}^2/\theta}}, \tag{5.5}
$$
clipped to $[-\sqrt N, \sqrt N]$ for $N$ cells. sctransform (Hafemeister and Satija, 2019) uses the same residuals from a regularized negative binomial regression on $\log n_c$.

**Example 5.4.1** For a gene with $\hat\mu = 5$ in a cell and $\theta = 10$, the denominator is $\sqrt{5 + 2.5} = 2.74$: a count of $0$ gives $z = -1.83$, $5$ gives $0$, $20$ gives $5.48$. Under the shifted logarithm the same counts become $0$, $1.79$ and $3.04$ (after scaling to the same total), compressing the high value.

![Zeros and variance in UMI counts (simulated: 3000 cells, size factors log-normal with s.d. 0.4, biological variation gamma with shape 5). A: the fraction of zeros of each gene against its mean, with the Poisson and negative binomial predictions; markers expressed in only one of two cell types (orange) have extra zeros from heterogeneity. B: variance of each gene after the shifted logarithm and after analytic Pearson residuals (Formula 5.4.2): the logarithm leaves a strong dependence on the mean; residuals of genes without biological variation (dark) have variance close to 1, and genes with biological variation rise above it. C: counts of one gene with mean 2 and the Poisson and negative binomial distributions with the same mean](./plots/umi_zeros.py)

### 5.4.3. Highly Variable Genes

Most genes vary between cells only by sampling noise. Using all of them for the embedding adds noise; selecting the genes with more variation than expected concentrates the biological signal.

**Definition 5.4.1 (Highly Variable Gene)** A **highly variable gene** of a single-cell data set is a gene whose variance across cells exceeds, by a chosen ranking or threshold, the variance expected for genes of the same mean under a model of technical variation; in practice the top $1000$–$5000$ genes by such a standardized variance.

**Algorithm 5.4.1 (Highly Variable Genes by Standardized Variance)** (the "vst" method of Seurat, flavor `seurat_v3` in scanpy)

1. For each gene compute the mean $\bar x_g$ and variance $s_g^2$ of the raw counts across cells.
2. Fit a smooth curve (local polynomial regression) of $\log s_g^2$ against $\log\bar x_g$; its value $\hat s_g^2$ is the expected variance of a gene of that mean.
3. Standardize the counts, $z_{gc} = (x_{gc} - \bar x_g)/\hat s_g$, clip at $\sqrt N$, and compute the variance of the clipped values for each gene.
4. Rank genes by this variance (within each batch, combining ranks across batches) and keep the top $n$.

The cost is $O(\text{nonzero entries})$. With Pearson residuals, the variance of the residuals of Formula 5.4.2 serves the same purpose directly. The selection affects everything downstream: cell-cycle genes are highly variable in most tissues and may dominate the clusters, and are sometimes removed or regressed out.

### 5.4.4. Imputation and Denoising

Can the zeros be "filled in"? MAGIC (van Dijk and colleagues, 2018) smooths expression over the graph of similar cells: from a $k$-nearest-neighbor graph it builds a row-stochastic matrix $T$ of transition probabilities of a **random walk** (a **Markov chain**) between cells, with Gaussian affinities adapted to the local density, and replaces the data by $T^tX$, the average of each cell's expression over the cells reached in $t$ steps (typically $t = 3$). Deep count autoencoders (DCA, 2019) learn a low-dimensional representation and output the parameters of a negative binomial for each entry. Both remove sampling noise and recover gene–gene relations that the sparse data hide, but they also create correlations from nothing: smoothing over neighbors makes the genes of a cluster correlated even when they are independent within it, and a differential expression test on imputed values, which are no longer independent across cells, has invalid p-values. Imputed values are useful for visualizing a gene or a gradient; statistical tests should use the counts with a model, and embeddings can use the latent spaces of count models directly (5.8.3).

## 5.5. Dimension Reduction, Neighbor Graphs and Clustering

### 5.5.1. Principal Components

The normalized and scaled expression of the highly variable genes is reduced by **principal component analysis** ([3.4.5](/3.4.5)) to $20$–$50$ components, computed by a randomized or truncated singular value decomposition of the sparse matrix ([3.4.6](/3.4.6)). The leading components capture the main differences between cell types; later ones are mostly noise, and the number kept is chosen from the decline of the explained variances (the elbow) or by comparing with components of permuted data. Each component should be inspected: one correlated with the total UMI count or the mitochondrial fraction signals a technical axis, and one loaded on cell-cycle genes a biological but often unwanted one.

### 5.5.2. Nearest-Neighbor Graphs

Distances in the space of principal components are meaningful locally, between cells of similar state, but not globally, where the data lie on curved and branched manifolds. The analysis therefore represents the data as a graph in which each cell is joined to its $k$ most similar cells (**k-nearest neighbors**, typically $k = 10$–$30$, Euclidean distance in the PC space); the graph is symmetrized by keeping an edge if either cell lists the other. Two weightings are common. Seurat uses the shared nearest neighbors: the weight of an edge between cells $i$ and $j$ with neighbor sets $N_k(i)$, $N_k(j)$ (each including the cell itself) is the Jaccard index $\lvert N_k(i) \cap N_k(j)\rvert/\lvert N_k(i) \cup N_k(j)\rvert$; two cells with $k = 10$ sharing $6$ neighbors have weight $6/(20 - 6) = 0.43$. Scanpy uses the fuzzy weights of UMAP, $w_{ij} = \exp(-(d_{ij} - \rho_i)/\sigma_i)$ with $\rho_i$ the distance to the nearest neighbor of $i$ and $\sigma_i$ a local scale, symmetrized as $w_{ij} + w_{ji} - w_{ij}w_{ji}$. Both downweight edges between cells in different dense regions. Exact neighbor search costs $O(N^2)$ distance evaluations; approximate methods (random projection trees, hierarchical navigable small-world graphs) bring it to about $O(N\log N)$, which makes graphs of millions of cells feasible.

### 5.5.3. Clusters as Communities

A cell type, in this graph, is a set of cells more densely connected among themselves than to the rest: a community ([Definition 7.7.1](/1.4.7#def-7.7.1)). Clustering by **community detection** on the neighbor graph replaced $k$-means and hierarchical clustering ([3.4.11](/3.4.11)) in single-cell analysis because it needs no number of clusters in advance, finds clusters of any shape and size, and scales to millions of cells.

**Algorithm 5.5.1 (Graph-Based Clustering of Cells)**

1. Build the weighted neighbor graph of 5.5.2 on the leading principal components.
2. Maximize the modularity with a resolution parameter $\gamma_{\mathrm{r}}$,
   $$
   Q_{\gamma} = \frac{1}{2M}\sum_{i,j}\left(A_{ij} - \gamma_{\mathrm{r}}\frac{k_ik_j}{2M}\right)\delta(g_i, g_j),
   $$
   ([Definition 7.7.3](/1.4.7#def-7.7.3) with the resolution of [7.7.3](/1.4.7#sec-7.7.3)), by the **Louvain algorithm** or, preferably, the **Leiden algorithm** ([Algorithms 7.7.3 and 7.7.4](/1.4.7#alg-7.7.4)), which guarantees connected communities.
3. Repeat for several resolutions and random seeds; choose the resolution at which the clusters are stable and biologically interpretable (distinct marker genes, 5.6.1).

The Leiden algorithm runs in time nearly linear in the number of edges, seconds for $10^5$ cells. The resolution sets the scale: small $\gamma_{\mathrm{r}}$ merges similar types, large $\gamma_{\mathrm{r}}$ splits types into states or into arbitrary pieces.

**Example 5.5.1** In the simulation of the figure, $600$ cells of five types, one of which differs from another in only $16$ of $400$ genes, give a neighbor graph with $7100$ edges ($k = 15$ on $15$ components). The Louvain algorithm (a numpy implementation; the Leiden implementation `leidenalg` gave the same partitions up to a few cells) finds four communities for $\gamma_{\mathrm{r}} \le 0.3$, which merge the subtype with its parent (adjusted Rand index $0.93$ against the true types); five for $0.5 \le \gamma_{\mathrm{r}} \le 1.5$, which recover the types (index $0.99$, modularity $Q_1 = 0.75$); and $7$, $10$ and $12$ communities at $\gamma_{\mathrm{r}} = 2$, $2.5$ and $3$, which split the largest type into pieces with no biological meaning. A plateau of the number of clusters over a range of resolutions, visualized as a tree of clusters across resolutions (clustree), is the usual evidence of a natural scale.

![Clustering cells by community detection on a nearest-neighbor graph (simulated data: 600 cells of five types, the fifth differing from the fourth in 16 of 400 genes; 15 principal components, 15 nearest neighbors, 7100 edges). A: the graph in a force-directed layout, cells colored by their true type. B: the communities found by the Louvain algorithm at resolution 1 (colored by the type that dominates each), which recover the five types. C: the number of communities and the adjusted Rand index against the true types as functions of the resolution parameter: small values merge the subtype with its parent, large values split the largest type](./plots/knn_leiden.py)

:::

Clusters are not cell types by themselves. A continuous process, such as differentiation along a trajectory ([7.9.7](/7.9.7)), is cut into arbitrary clusters at any resolution; doublets and stressed cells form clusters of their own; and a statistically distinct cluster may be a state of a known type rather than a new type. The interpretation comes from markers, references and experiments (5.6).

### 5.5.4. Visualization

Two-dimensional maps of cells are made with nonlinear embeddings that preserve neighborhoods. **t-SNE** ([3.4.6](/3.4.6#sec-6.4)) matches Gaussian neighbor probabilities in the original space to heavy-tailed Student-$t$ probabilities in the plane by minimizing their **Kullback–Leibler divergence**. UMAP (McInnes, Healy and Melville, 2018) starts from the fuzzy neighbor graph of 5.5.2 and places points to minimize the cross-entropy between the graph weights $w_{ij}$ and low-dimensional similarities $v_{ij} = (1 + a\lVert\boldsymbol{y}_i - \boldsymbol{y}_j\rVert^{2b})^{-1}$,
$$
\sum_{i \ne j}\Bigl[w_{ij}\log\frac{w_{ij}}{v_{ij}} + (1 - w_{ij})\log\frac{1 - w_{ij}}{1 - v_{ij}}\Bigr],
$$
optimized by stochastic gradient descent with negative sampling; the repulsive second term, which t-SNE lacks in this form, tends to keep more of the global arrangement, though much of that difference comes from the initialization (UMAP from a spectral embedding, t-SNE often from random positions). Both maps distort: the sizes of clusters, the distances between clusters and the density of points are not meaningful, two clusters adjacent on the map need not be similar, and the map changes with the parameters (perplexity, number of neighbors, minimum distance) and the random seed (Chari and Pachter, 2023). They are for display and for checking analyses, not for measurement; clustering, distances and trajectories are computed on the graph or in the PC space.

## 5.6. Annotation and Comparison

### 5.6.1. Marker Genes

A cluster is named by the genes that distinguish it. The standard test compares each cluster with all other cells, gene by gene, by the **Wilcoxon rank-sum test**, and reports the log fold change of mean normalized expression and the fractions of cells in and outside the cluster in which the gene is detected. In the classic data set of $2700$ blood mononuclear cells (PBMC 3k, 10x Genomics), the B-cell cluster has *CD79A* detected in $93.6\,\%$ of its cells and $4.1\,\%$ of the others, with an average $\log_2$ fold change of $6.9$; *MS4A1* (CD20) gives $85.5\,\%$ against $5.3\,\%$. Such genes, together with known markers (*CD3E* for T cells, *CD14* and *LYZ* for classical monocytes, *FCGR3A* for nonclassical monocytes, *NKG7* and *GNLY* for NK cells, *PPBP* for platelets), name the clusters.

The p-values of these tests are not valid in the usual sense: the clusters were defined from the same data to differ, so testing them for differences ("double dipping") yields tiny p-values even for random splits of a homogeneous population. Marker lists should be ranked by effect size and specificity, not interpreted as discoveries; valid inference after clustering requires sample splitting, count splitting (dividing each count binomially into two independent parts, one for clustering and one for testing) or selective inference.

### 5.6.2. Reference-Based Annotation

Manual annotation is slow and subjective; with the growth of atlases, automatic annotation against references has become standard. SingleR correlates (Spearman) each cell or cluster with the expression profiles of labeled reference samples, using genes that distinguish the reference labels, and iteratively refines the assignment on the subset of best-matching labels. CellTypist trains a regularized **logistic regression** on large immune and tissue atlases. Reference mapping (Azimuth, scArches, symphony) projects the new cells into the integrated embedding of a reference atlas and transfers labels from the nearest reference cells, which also gives a confidence score. Marker databases (CellMarker, PanglaoDB) and marker-based scoring (ScType, scoring each cell by sets of positive and negative markers) are useful where no reference exists. Every automatic label is a hypothesis: references miss rare or disease-specific states, and cell states induced by the experiment (stress, activation) are easily mistaken for types.

### 5.6.3. Pseudoreplication and Pseudobulk

Comparing conditions (disease against healthy donors, treated against control) is where single-cell data are most often analysed incorrectly. Cells of one donor are not independent replicates: they share the donor's genotype, age, sample handling and batch. A test that treats the cells of each condition as replicates confuses the variation between donors with an effect of the condition, and its false positive rate grows with the number of cells (Squair and colleagues, 2021; Zimmerman, Espeland and Langefeld, 2021).

**Definition 5.6.1 (Pseudobulk)** The **pseudobulk** profile of a cell type in a sample is the sum (or mean) of the UMI counts of each gene over the cells of that type in that sample. Differential expression between conditions is then tested on the pseudobulk profiles, with the samples as replicates, by the count models of bulk RNA-seq (DESeq2, edgeR, limma-voom; [7.7.20](/7.7.20)).

**Example 5.6.1** The figure simulates genes without any effect of the condition, measured in three donors per condition whose means vary by a log-normal donor effect (s.d. $0.3$). With $200$ cells per donor, a Wilcoxon test between the $600$ cells of each condition calls $54\,\%$ of the null genes significant at $p < 0.05$; a t-test on the six pseudobulk values calls $5.1\,\%$, the nominal level. With $10$ cells per donor the cell-level test calls $13\,\%$, with $400$ cells $66\,\%$: more cells make it more confident about the wrong comparison. Mixed models with a random effect of the donor are the alternative to pseudobulk; in benchmarks they performed no better and are much slower.

![Pseudoreplication in single-cell differential expression (simulated null genes, three donors per condition with a donor effect of s.d. 0.3, negative binomial counts). A: p-values of 2000 null genes with 200 cells per donor, from a Wilcoxon test treating cells as replicates (filled) and from a t-test on pseudobulk values of the six donors (line); under the null hypothesis they should be uniform (dashed). B: the share of null genes called significant at p < 0.05 as the number of cells per donor grows](./plots/pseudobulk.py)

### 5.6.4. Composition

A condition may change the proportions of cell types rather than their expression (Example 5.1.1). Proportions are compositional: if one type expands, all others shrink in relative terms, even if their absolute numbers are unchanged, so testing each type separately by a binomial or Poisson model of its counts gives spurious decreases. Methods for differential abundance model the counts of all types of a sample jointly (scCODA, a Bayesian Dirichlet-multinomial model with a reference type; propeller, a linear model on transformed proportions) with samples as replicates, again; Milo tests abundance in overlapping neighborhoods of the cell graph instead of in clusters, which detects shifts within a continuous population.

### 5.6.5. Batch Effects and Integration

Samples processed on different days, with different reagent lots or protocols, differ systematically, and the differences can exceed those between cell types: a UMAP colored by sample shows islands of each sample instead of shared types. Integration methods align cells of the same type across batches while keeping biological differences, which is possible only if the batches share at least some cell types and if the design is not confounded (all control samples in one batch and all treated in another cannot be rescued).

**Algorithm 5.6.1 (Mutual Nearest Neighbors)** (Haghverdi and colleagues, 2018) To correct batch $2$ onto batch $1$:

1. Normalize both batches the same way and represent the cells in a common space (cosine-normalized expression of shared highly variable genes, or a joint PCA).
2. For every cell of each batch find its $k$ nearest neighbors in the other batch; a pair $(i, j)$ with $i$ in batch $1$ and $j$ in batch $2$ is a mutual nearest neighbor (MNN) pair if each is among the $k$ nearest neighbors of the other.
3. For each MNN pair compute the correction vector $\boldsymbol{x}_i - \boldsymbol{x}_j$; for every cell of batch $2$, average the correction vectors of nearby MNN pairs with Gaussian kernel weights and add the average to the cell.

The assumption is that MNN pairs are cells of the same type, and that the batch effect varies smoothly across the space, nearly orthogonal to the biological differences. Harmony (Korsunsky and colleagues, 2019) iterates between a soft clustering in PC space that rewards clusters mixing all batches and a linear correction of each batch within each cluster; Seurat's anchor method finds MNN-like anchors in a space of canonical correlation analysis; scVI (5.8.3) includes the batch as a covariate of a generative model. Benchmarks (scIB, Luecken and colleagues, 2022) score methods on two competing criteria, batch mixing and conservation of biological variation; overcorrection that merges genuinely different states is a real risk. Integrated embeddings are used for clustering and annotation, while differential expression should use the original counts with the batch in the model.

## 5.7. Beyond RNA Alone

Several methods add other measurements of the same cells:

- Surface proteins: in CITE-seq (Stoeckius and colleagues, 2017), antibodies carrying oligonucleotide barcodes with a poly(A) tail are captured like mRNA, so each cell yields counts of tens to hundreds of surface proteins along with its transcriptome; protein counts are far less sparse than mRNA counts and resolve immune subsets that RNA blurs. The same chemistry gives cell hashing (5.3.3).
- Chromatin accessibility: single-nucleus ATAC-seq, alone or with RNA-seq of the same nucleus (multiome), measures regulatory elements; its analysis is in [7.9.8](/7.9.8). Methods such as weighted nearest neighbors (Hao and colleagues, 2021), totalVI and MOFA+ combine the modalities into one representation.
- Perturbations: in Perturb-seq and CROP-seq, cells receive guide RNAs of a CRISPR library whose identity is read in the same droplet, so the transcriptomic effect of each perturbation is measured in pooled screens ([7.9.10](/7.9.10)); lineage barcodes record the descent of cells ([7.9.7](/7.9.7)).
- Space: spatial transcriptomics keeps the positions of cells or spots in a tissue section; it is the subject of [7.9.6](/7.9.6), which also treats the deconvolution of spots containing several cells.

The same idea of deconvolution recovers cell-type proportions from bulk data with a single-cell reference.

**Formula 5.7.1 (Deconvolution of a bulk profile)** Let $S$ be a $G \times K$ signature matrix whose column $j$ is the mean expression of $G$ marker genes in cell type $j$ (from single-cell data or sorted cells), and $\boldsymbol{y}$ the bulk expression of the same genes. The proportions $\boldsymbol{w} \ge \boldsymbol{0}$ solve approximately $\boldsymbol{y} = S\boldsymbol{w}$, for example by nonnegative least squares,
$$
\hat{\boldsymbol{w}} = \arg\min_{\boldsymbol{w} \ge \boldsymbol{0}}\lVert\boldsymbol{y} - S\boldsymbol{w}\rVert^2, \tag{5.6}
$$
normalized to sum to $1$. CIBERSORT (Newman and colleagues, 2015) uses $\nu$-support vector regression, which is robust to genes that fit badly; MuSiC weights genes by their consistency across subjects.

**Example 5.7.1** Take five marker genes and three cell types with signature (rows genes, columns types, in counts per million)
$$
S = \begin{bmatrix} 200 & 5 & 10 \\ 10 & 300 & 20 \\ 5 & 10 & 150 \\ 50 & 60 & 40 \\ 100 & 20 & 80 \end{bmatrix},
$$
and a bulk sample of proportions $(0.6, 0.3, 0.1)$, $\boldsymbol{y} = S\boldsymbol{w} = (122.5, 98, 21, 52, 74)^{\mathsf T}$. With $10\,\%$ multiplicative noise added to each gene, $\boldsymbol{y} = (124.0, 96.7, 22.4, 52.5, 70.1)^{\mathsf T}$, and Eq. (5.6) gives the proportions $(0.603, 0.297, 0.099)$ after normalization. In practice the hard parts are the choice of the reference (a cell type missing from $S$ is absorbed by the others), differences in mRNA content between types, which bias proportions of cells relative to proportions of RNA, and platform differences between reference and bulk data.

## 5.8. The scverse Workflow

The analyses of this chapter are carried out in one of two software ecosystems: Seurat and Bioconductor in R, or scverse in Python, a community of interoperating packages (anndata, scanpy, muon, scvi-tools, squidpy, spatialdata) around shared data structures. We use scverse.

### 5.8.1. AnnData and MuData

An AnnData object stores one matrix of cells by features with aligned annotations:

| Slot | Shape | Content |
|---|---|---|
| `X` | $N \times G$ | the main matrix, usually sparse (compressed sparse rows): counts, or normalized values |
| `obs` | $N$ rows | data frame of per-cell annotations: sample, QC metrics, cluster labels |
| `var` | $G$ rows | data frame of per-gene annotations: gene IDs, highly variable flags |
| `layers` | $N \times G$ each | alternative matrices of the same shape, such as `counts` and `log1p` |
| `obsm`, `varm` | $N \times d$, $G \times d$ | multidimensional annotations: `X_pca`, `X_umap`, `X_scVI`; PCA loadings |
| `obsp` | $N \times N$ | cell–cell graphs: `connectivities`, `distances` |
| `uns` | — | unstructured metadata: parameters, colors, results of tests |

Subsetting cells or genes keeps all slots aligned, and the object is stored as one HDF5 (`.h5ad`) or Zarr file, which can be read lazily for data larger than memory. MuData holds several AnnData objects, one per modality (`rna`, `prot`, `atac`), with a shared `obs` for the cells measured in all of them.

### 5.8.2. A Standard Analysis

The following code runs the steps of 5.3–5.6 on the PBMC 3k data. The thresholds suit this data set and must be chosen for each new one by inspecting the distributions.

```python
import scanpy as sc

adata = sc.datasets.pbmc3k()              # 2700 cells x 32738 genes, raw UMI counts
adata.var_names_make_unique()

# Quality control (5.3.2): mitochondrial fraction, genes per cell; doublet scores (5.3.3)
adata.var["mt"] = adata.var_names.str.startswith("MT-")
sc.pp.calculate_qc_metrics(adata, qc_vars=["mt"], percent_top=None, log1p=False, inplace=True)
adata = adata[(adata.obs.n_genes_by_counts > 200) & (adata.obs.n_genes_by_counts < 2500)
              & (adata.obs.pct_counts_mt < 5)].copy()
sc.pp.filter_genes(adata, min_cells=3)
sc.pp.scrublet(adata)                     # adds doublet_score and predicted_doublet to obs
adata = adata[~adata.obs.predicted_doublet].copy()

# Normalization (5.4.2), keeping the counts for count models
adata.layers["counts"] = adata.X.copy()
sc.pp.normalize_total(adata, target_sum=1e4)
sc.pp.log1p(adata)

# Highly variable genes on the counts (Algorithm 5.4.1), PCA (5.5.1)
sc.pp.highly_variable_genes(adata, n_top_genes=2000, flavor="seurat_v3", layer="counts")
adata.raw = adata                         # log-normalized values of all genes, for plots and markers
sc.pp.scale(adata, max_value=10)
sc.tl.pca(adata, n_comps=50, mask_var="highly_variable")

# Neighbor graph (5.5.2), Leiden communities (Algorithm 5.5.1), UMAP (5.5.4)
sc.pp.neighbors(adata, n_neighbors=15, n_pcs=30)
for res in (0.4, 0.8, 1.2):
    sc.tl.leiden(adata, resolution=res, key_added=f"leiden_{res}",
                 flavor="igraph", n_iterations=2, random_state=0)
sc.tl.umap(adata, random_state=0)

# Marker genes (5.6.1) and a first look
sc.tl.rank_genes_groups(adata, groupby="leiden_0.8", method="wilcoxon", use_raw=True)
sc.pl.umap(adata, color=["leiden_0.8", "CD79A", "CD14", "NKG7"])
adata.write_h5ad("pbmc3k_processed.h5ad")
```

Comparisons between conditions then aggregate the counts layer by sample and cell type (`sc.get.aggregate(adata, by=["sample", "cell_type"], func="sum", layer="counts")`) and test the pseudobulk profiles with a count model (Definition 5.6.1), for example with the Python port of DESeq2 (pydeseq2). Integration across batches uses `sc.external.pp.harmony_integrate` on the PCA, or scVI.

For readers who know Seurat, the steps correspond as follows:

| Step | Seurat (R) | scanpy (Python) |
|---|---|---|
| Read 10x output | `Read10X`, `CreateSeuratObject` | `sc.read_10x_mtx`, `sc.read_10x_h5` |
| QC metrics | `PercentageFeatureSet` | `sc.pp.calculate_qc_metrics` |
| Normalization | `NormalizeData`; `SCTransform` | `sc.pp.normalize_total` + `sc.pp.log1p`; `sc.experimental.pp.normalize_pearson_residuals` |
| Variable genes | `FindVariableFeatures(selection.method = "vst")` | `sc.pp.highly_variable_genes(flavor="seurat_v3")` |
| Scaling, PCA | `ScaleData`, `RunPCA` | `sc.pp.scale`, `sc.tl.pca` |
| Graph, clusters | `FindNeighbors`, `FindClusters` (Louvain by default) | `sc.pp.neighbors`, `sc.tl.leiden` |
| Embedding | `RunUMAP`, `RunTSNE` | `sc.tl.umap`, `sc.tl.tsne` |
| Markers | `FindAllMarkers`, `FindMarkers` | `sc.tl.rank_genes_groups` |
| Integration | `IntegrateLayers` (CCA, RPCA, Harmony) | `sc.external.pp.harmony_integrate`, scvi-tools |

### 5.8.3. Generative Models: scvi-tools

The steps of 5.4–5.6 each make their own approximation (a log transformation, a linear PCA, a separate correction for batches). A probabilistic model can replace them with one.

**Formula 5.8.1 (The scVI model)** (Lopez and colleagues, 2018) For cell $n$ in batch $b_n$ with observed library size $\ell_n$:
$$
\boldsymbol{z}_n \sim \mathcal{N}(\boldsymbol{0}, I_d), \qquad \boldsymbol{\rho}_n = \operatorname{softmax}\bigl(f_{\boldsymbol{\omega}}(\boldsymbol{z}_n, b_n)\bigr), \qquad x_{ng} \mid \boldsymbol{z}_n \sim \text{negative binomial with mean } \ell_n\rho_{ng} \text{ and shape } \theta_g, \tag{5.7}
$$
where $\boldsymbol{z}_n$ is a latent state of dimension $d \approx 10$–$30$, $f_{\boldsymbol{\omega}}$ a neural network (the decoder) and $\rho_{ng}$ the expected fraction of the cell's transcripts from gene $g$. An encoder network $q_{\boldsymbol{\phi}}(\boldsymbol{z}_n \mid \boldsymbol{x}_n, b_n)$ approximates the posterior, and both networks are trained by maximizing the **evidence lower bound**, as in a variational autoencoder ([4.7](/4.7)).

Because the batch enters the decoder, the latent space $\boldsymbol{z}$ is encouraged to describe biology independently of batch: it is used as an integrated embedding for the neighbor graph and clustering. The decoder gives denoised expression $\ell\boldsymbol{\rho}$ for any batch, and differential expression is computed from the posterior of $\boldsymbol{\rho}$ in two groups of cells. Extensions in scvi-tools use the same framework for annotation with partial labels (scANVI), RNA plus surface proteins (totalVI), chromatin accessibility (PeakVI, MultiVI), reference mapping of new data onto a trained model (scArches) and spatial deconvolution (DestVI, [7.9.6](/7.9.6)). The model needs a GPU for large data sets and careful checks: a latent space that mixes batches perfectly may also have removed biology, and posterior differential expression, like any test across cells, does not replace replication across samples (5.6.3).

### 5.8.4. Reproducibility

Single-cell analyses involve many choices and random steps, so a result is reproducible only if they are recorded: package versions (a `conda` or `uv` environment file), random seeds for the neighbor search, Leiden and UMAP, the thresholds of quality control, the number of genes and components, and the resolution. Raw counts should be kept in a layer and the processed object saved with its parameters in `uns`. Conclusions should be checked for robustness to these choices: a cluster or a differentially abundant population that appears at only one resolution or one number of genes is weak evidence.

## Summary

| Stage | Problem | Model or method | Section |
|---|---|---|---|
| Design | averages hide composition and states | single-cell profiles (Example 5.1.1) | 5.1 |
| Capture | assigning molecules to cells and counting them | cell barcode (Definition 5.2.2), UMI; Poisson loading and multiplets (Formula 5.2.1) | 5.2 |
| Cell calling | empty droplets, ambient RNA | barcode rank plot; Dirichlet-multinomial test (Algorithm 5.3.1); ambient subtraction | 5.3.2 |
| Doublets | two cells in one droplet | simulated doublets and kNN scores (Algorithm 5.3.2); hashing, genotypes | 5.3.3 |
| Depth | how many reads per cell | saturation with gamma-distributed abundances (Formula 5.3.1, Example 5.3.1) | 5.3.4 |
| Counts | sparsity and zeros | negative binomial (Formula 5.4.1); zeros from sampling and heterogeneity | 5.4.1 |
| Normalization | size factors, mean–variance relation | shifted log; Pearson residuals (Formula 5.4.2) | 5.4.2 |
| Feature selection | noise of most genes | highly variable genes (Definition 5.4.1, Algorithm 5.4.1) | 5.4.3 |
| Structure | types and states | PCA, kNN graph, Leiden with resolution (Algorithm 5.5.1, Example 5.5.1) | 5.5 |
| Display | two-dimensional maps | t-SNE, UMAP: neighborhoods only, not distances | 5.5.4 |
| Annotation | naming clusters | Wilcoxon markers (no valid p-values after clustering), references | 5.6.1–5.6.2 |
| Comparison | conditions across donors | pseudobulk with samples as replicates (Definition 5.6.1, Example 5.6.1); compositional models | 5.6.3–5.6.4 |
| Batches | technical differences between samples | MNN (Algorithm 5.6.1), Harmony, scVI | 5.6.5 |
| Integration | other modalities, bulk data | CITE-seq, multiome; deconvolution (Formula 5.7.1) | 5.7 |
| Software | data structures and pipelines | AnnData, MuData, scanpy, scvi-tools (Formula 5.8.1) | 5.8 |

The two errors that most often invalidate single-cell conclusions are statistical, not technical: treating cells as independent replicates when comparing conditions (Example 5.6.1), and interpreting test statistics or map distances that the analysis itself produced (5.5.4, 5.6.1).

## Questions

1. A gene has mean $0.2$ UMIs per cell in a homogeneous population. What fraction of cells is expected to have zero counts under a Poisson model and under a negative binomial with $\theta = 1$? What would a fraction of $95\,\%$ zeros suggest?

   **Answer** Poisson: $\mathrm{e}^{-0.2} = 0.819$. Negative binomial: $(1 + 0.2/1)^{-1} = 0.833$. At low means the two barely differ, and about $82$–$83\,\%$ of cells are zero for purely statistical reasons. $95\,\%$ zeros at the same mean means the expression is concentrated in few cells: the mean of $0.2$ could come from $5\,\%$ of cells with mean $4$ (the zero fraction among them would be $\mathrm{e}^{-4} = 0.02$, so $95.1\,\%$ zeros overall). The population is then heterogeneous for this gene, a marker of a rare subpopulation, rather than "zero-inflated" by a technical failure.

2. A lab wants $20\,000$ cells from one sample. Compare running one channel with $20\,000$ recovered cells and two channels with $10\,000$ each, using Formula 5.2.1 with $10^5$ droplets per channel and $60\,\%$ recovery. How does cell hashing change the calculation?

   **Answer** One channel: $\lambda = 20\,000/0.6/10^5 = 0.333$, $m = (1 - \mathrm{e}^{-0.333} - 0.333\mathrm{e}^{-0.333})/(1 - \mathrm{e}^{-0.333}) = (1 - 0.7165 - 0.2388)/0.2835 = 0.158$: about $16\,\%$ of barcodes are multiplets. Two channels: $\lambda = 0.167$, $m \approx 8\,\%$ each. With hashing of, say, eight samples pooled into one channel, a doublet of cells from two samples carries two hashtags and is removed; the fraction of doublets with two different samples is $1 - 1/8 = 7/8$ for equal pools, so only about $2\,\%$ of barcodes remain undetected (homotypic-in-sample) doublets even at $16\,\%$ multiplets, and the channel can be overloaded at the cost of discarding the detected doublets.

3. Fit the saturation curve of Example 5.3.1 mentally: if a library of $M = 20\,000$ molecules per cell with equal abundances is sequenced to $r = 20\,000$ reads per cell, what is the saturation, and how many molecules are seen? How many reads give $90\,\%$ of the molecules?

   **Answer** $U = M(1 - \mathrm{e}^{-1}) = 0.632M = 12\,640$ molecules, saturation $1 - 12\,640/20\,000 = 0.368$. Seeing $90\,\%$ of the molecules requires $1 - \mathrm{e}^{-r/M} = 0.9$, $r = M\ln 10 = 46\,000$ reads per cell. With unequal abundances (finite $k$, Eq. (5.3)) the rare molecules are seen later, so more reads are needed for the same fraction; the fit of Example 5.3.1 has $k = 1.39$, and $90\,\%$ of molecules would need $r/(Mk) = 0.1^{-1/k} - 1 = 4.24$, $r = 4.24 \times 1.39\,M = 5.9\,M$ reads, about $133\,000$ reads per cell for $M = 22\,600$.

4. Explain why clustering with a fixed number of clusters by $k$-means on the first two UMAP coordinates is a poor procedure, and describe a better one.

   **Answer** UMAP coordinates do not preserve distances or densities between clusters (5.5.4): two dimensions discard most of the information in the PC space, cluster sizes on the map are distorted, and the layout depends on parameters and seeds. $k$-means also assumes compact, roughly spherical clusters of similar size and needs the number of clusters in advance. A better procedure builds a nearest-neighbor graph in $20$–$50$ principal components (or a scVI latent space), finds communities with the Leiden algorithm over a range of resolutions and seeds (Algorithm 5.5.1), chooses a resolution with stable clusters and distinct markers, and uses UMAP only to display the result.

5. Two cells have $10$ nearest neighbors each (including themselves), of which $4$ are shared. Compute the shared-nearest-neighbor weight of their edge. Why is such a weight preferred to the plain kNN edge?

   **Answer** Jaccard index $4/(10 + 10 - 4) = 4/16 = 0.25$. The plain kNN graph joins a cell to its $k$ nearest neighbors even when they lie in a different dense region (for a cell at the border of a cluster, or in a small cluster with fewer than $k$ members); shared neighbors measure whether two cells live in the same neighborhood, so edges between clusters get low weights and edges within get high weights, which sharpens the community structure that modularity optimization detects and makes it robust to outlying cells.

6. In a study of $4$ patients and $4$ controls with $5000$ cells each, a cell-level Wilcoxon test finds $3000$ genes differentially expressed in monocytes at FDR $5\,\%$; a pseudobulk analysis with DESeq2 finds $40$. Which result should be reported, and what explains the difference?

   **Answer** The pseudobulk result. The unit of replication is the person: there are $8$ independent samples, not $40\,000$ cells. The cell-level test treats each cell as a replicate, so any difference between the $4$ patients and $4$ controls, including differences between individuals that are unrelated to disease (genotype, age, sample processing), becomes enormously significant with thousands of cells (Example 5.6.1 shows a false positive rate of $54\,\%$ for null genes). Pseudobulk tests whether the difference between groups exceeds the variation between individuals, which is the relevant question; with only $4$ per group the power is limited, and the honest conclusion is that few genes change robustly, or that more donors are needed.

7. A cluster appears only in the samples processed on the second day and expresses *FOS*, *JUN* and heat-shock genes. Give two explanations and how to distinguish them.

   **Answer** It may be a dissociation artifact: immediate early and heat-shock genes are induced within minutes by enzymatic digestion at $37^\circ\mathrm{C}$, and a change of protocol or timing on the second day would produce such a state in cells of several types; or it may be a batch effect between days combined with a genuine biological state present only in those donors. Check whether the cluster contains cells of several types (by their lineage markers), compare with a published dissociation signature, and test whether the signature is reduced with cold-active proteases, single-nucleus RNA-seq or fixation before dissociation. If the samples of the second day are also of one condition, the design is confounded and cannot separate the explanations; balancing conditions across days is the remedy for the next experiment.

8. Using Example 5.7.1, what happens to the estimated proportions if a fourth cell type, present at $20\,\%$ in the bulk sample, is missing from the signature matrix?

   **Answer** The bulk profile becomes $0.8S\boldsymbol{w}' + 0.2\boldsymbol{s}_4$, with $\boldsymbol{w}'$ the proportions of the three known types among themselves; nonnegative least squares fits the extra signal with the columns it has, so the proportions of the types whose signatures resemble $\boldsymbol{s}_4$ are inflated, and the residual $\lVert\boldsymbol{y} - S\hat{\boldsymbol{w}}\rVert$ becomes large on the genes specific to the missing type. A large residual, or genes systematically underfitted, is the diagnostic; the remedy is a more complete reference, for example from single-cell data of the same tissue, and reporting proportions as relative to the types modeled.

9. (Design) Plan the analysis of a single-cell study comparing tumors of $6$ patients who responded to immunotherapy with $6$ who did not, including quality control, annotation and the main statistical tests.

   **Answer** Process each sample with STARsolo or Cell Ranger; call cells with EmptyDrops (Algorithm 5.3.1), remove ambient RNA, filter low-quality cells per sample by median absolute deviations, and remove doublets (Algorithm 5.3.2, or hashing or genotype demultiplexing if samples were pooled). Normalize, select highly variable genes per sample, and integrate the samples (Harmony or scVI with the patient as batch), checking that malignant cells, which differ between patients, are not forced together. Cluster with Leiden at several resolutions, annotate immune and stromal types against a reference (5.6.2) and confirm with markers; identify malignant cells by inferred copy-number changes. Test differences in composition between responders and non-responders with patients as replicates (5.6.4), and differential expression within each cell type by pseudobulk with a count model (Definition 5.6.1), adjusting for covariates and controlling the false discovery rate across genes and cell types. Report effect sizes with intervals, validate key populations by flow cytometry or imaging, and, with only $6$ patients per group, treat the results as hypotheses for a larger cohort.
