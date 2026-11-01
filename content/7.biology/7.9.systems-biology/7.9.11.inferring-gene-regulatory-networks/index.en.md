---
title: Inferring Gene Regulatory Networks
description: "How regulatory networks are reconstructed from genome-wide data: the size and underdetermination of the problem; networks from binding (ChIP-seq, yeast one-hybrid, DNase footprints of 475 factors in 41 cell types); co-expression networks, partial correlation and the graphical lasso, WGCNA and topological overlap; mutual information, its estimation, the data processing inequality, ARACNe, CLR and MINDy; per-gene regression and GENIE3; Bayesian networks, Markov equivalence, perturbations and modular response analysis; regulon activity, SCENIC and master regulator analysis of the mesenchymal subtype of glioblastoma; and evaluation by precision–recall, DREAM challenges and the wisdom of crowds."
---

A cell type is defined less by the genes it contains than by the transcription factors that are active in it and the genes they control. The wiring diagram of this control, which factor regulates which gene, is the gene regulatory network. Its molecular parts are the subject of [7.2.11](/7.2.11)–[7.2.15](/7.2.15): factors that bind short motifs in **enhancers** and promoters and recruit or block the transcription machinery. This chapter asks how the network is reconstructed at genome scale from data: from where factors bind, and from how the expression of genes covaries across many samples or responds to perturbations. Network inference is the archetypal **inverse model** of systems biology ([7.9.1](/7.9.1#sec-1.4)): we observe the outputs of a system and ask what wiring produced them.

We state the problem and its difficulty (11.1), build networks from binding data (11.2), from correlations (11.3), from mutual information (11.4) and from regression (11.5), discuss causal inference and perturbations (11.6), use the networks to estimate the activity of regulators and find master regulators (11.7), and end with how inferred networks are evaluated (11.8). The binding data come from [7.9.8](/7.9.8), the expression data from [7.9.2](/7.9.2) and [7.9.5](/7.9.5), the perturbation atlases from [7.9.7](/7.9.7#sec-7.7); the general properties of networks, such as **degree distributions** and **network motifs**, are in [1.4.7](/1.4.7), and the analysis of the networks once built in [7.9.12](/7.9.12). Dynamic models fitted to time courses, the model-driven end of the same problem, are in [7.9.14](/7.9.14).

## 11.1. The Problem

**Definition 11.1.1 (Gene Regulatory Network)** A **gene regulatory network** (GRN) of a cell type or condition is a directed graph whose vertices are genes and whose arcs $i \to j$ join a gene $i$ encoding a transcription factor (or another regulator of transcription) to a gene $j$ whose transcription the product of $i$ controls; arcs may carry a sign (activation or repression) and a weight (strength or confidence).

The size of the problem is set by the numbers. The human genome encodes about $1600$ sequence-specific transcription factors (Lambert and colleagues, 2018, list $1639$) and about $20\,000$ protein-coding genes, plus many noncoding ones. The candidate arcs from factors to protein-coding genes number about $1600 \times 20\,000 = 3.2 \times 10^7$, while the true network is sparse: in bacteria, where networks are best known, fewer than $0.1\,\%$ of possible arcs exist, each gene has a few inputs (a compact **in-degree** distribution) and a few global regulators have hundreds of targets (a long-tailed **out-degree** distribution).

What an arc means depends on the evidence for it.

| Kind of evidence | What it shows | What it misses |
|---|---|---|
| Binding (ChIP-seq, footprints, one-hybrid) | the factor occupies a site near the gene | whether the binding changes transcription; which gene a distal site controls |
| Perturbation (knockout, knockdown, overexpression) | the factor's level changes the gene's expression | whether the effect is direct or passes through other genes |
| Covariation (co-expression, information) | expression of factor and gene are statistically dependent | direction, directness, and whether a common cause drives both |
| Sequence (motifs in promoters and enhancers) | a site that the factor could bind | whether the site is accessible and occupied in the cell type |

A direct regulatory arc is best supported by the combination of binding and a perturbation effect; each kind of evidence alone yields a different graph.

The data are also few. Suppose each gene's expression is modeled as a linear combination of the expression of all $p = 1600$ factors and measured in $n = 500$ samples. For every gene this is a regression with more unknowns than observations, an underdetermined problem with infinitely many exact solutions. Two assumptions make it solvable. Sparsity: each gene has few regulators, so the problem splits into $20\,000$ small regression problems with sparse solutions (11.5). And prior structure: only factors with a motif in a gene's regulatory regions, or with binding evidence there, are allowed as its regulators (11.2, 11.5.3).

Two strategies attack the problem from opposite ends.

| | Data-driven | Model-driven |
|---|---|---|
| Starts from | high-throughput profiles, with few assumptions | a mechanistic model of known or hypothesized parts |
| Method | statistical dependence, information, machine learning | fitting the parameters of the model to data |
| Strengths | comprehensive, unbiased by prior knowledge | interpretable, testable mechanisms, predictions of dynamics |
| Weaknesses | multiple testing, needs many samples, hard to tie to mechanism | results depend on the model; small systems only |
| Typical scale | the whole genome | a few to tens of genes ([7.9.14](/7.9.14)) |

The choice depends on the purpose and on what is known; in practice the two are combined, with data-driven methods proposing a network and model-driven work testing parts of it.

## 11.2. Networks from Binding

### 11.2.1. Experimental Maps

The direct way to find the targets of a factor is to see where it binds. **ChIP-seq** ([7.2.6](/7.2.6), [7.9.8](/7.9.8#sec-8.2)) maps the occupied sites of one factor in one cell type; ENCODE and related consortia have profiled hundreds of factors in a few cell lines. Assigning a peak to a gene is the first source of error: a peak within a few kilobases of a transcription start site is usually assigned to that gene, but most binding sites in mammals are distal and act through loops on genes up to a megabase away ([7.9.8](/7.9.8#sec-8.6)). Binding is also not regulation: in ChIP-seq studies of a factor, only a minority of bound genes change expression when the factor is removed, because many sites are redundant, inactive in the given condition, or nonfunctional.

Other methods map binding from the side of the gene. Yeast one-hybrid screens fuse a promoter fragment to a reporter in yeast and test it against a library of transcription factors; in the root of *Arabidopsis thaliana*, a screen of $50$ promoters of genes for secondary cell wall synthesis found factors bound to $42$ of them and assembled a densely interconnected network of factors and cell-wall genes (Taylor-Teeples and colleagues, 2015). Transcriptome profiling of a factor mutant in a factorial design (wild type and mutant, control and treatment, three replicates each) identifies the genes whose response depends on the factor, which are then scanned for overrepresented sequences: a motif enriched in the upstream regions of the coexpressed, factor-dependent genes is a candidate binding site of the factor ([7.8.8](/7.8.8)). The last approach is cheap and genome-wide but yields predictions, often too many, with both false positives and false negatives.

### 11.2.2. Footprint Networks

A factor bound in accessible chromatin protects the few base pairs under it from cleavage by DNase I, leaving a footprint in DNase-seq data (**DNase I footprinting**, footprint occupancy score in [Formula 8.3.1](/7.9.8#fml-8.3.1)). One DNase-seq experiment thus reports, in principle, the occupancy of all factors at once, and footprints matched to factor motifs identify which factor sits where.

**Algorithm 11.2.1 (Footprint-Based Regulatory Network)** (Neph and colleagues, 2012) For each cell type:

1. Map DNase I cleavage sites genome-wide and call footprints, short ($6$–$40$ bp) segments with significantly fewer cleavages than their flanks, within **DNase I hypersensitive sites**.
2. Match each footprint to the motifs (**position weight matrices** from TRANSFAC, JASPAR, UniPROBE) of the factors; a footprint matching the motif of factor $f$ is an occupied site of $f$.
3. For each gene $g$ encoding a transcription factor, collect the occupied sites in a window of $10$ kb centered on its transcription start site, and add an arc $f \to g$ for every factor $f$ with an occupied site in the window.

The result is a network among the factors themselves, the core of the regulatory network. The cost is dominated by motif matching, linear in the number of footprints times the number of motifs.

Applied to DNase-seq of $41$ human cell types, with about $500$ million cleavages sequenced per cell type and about $8.4$ million distinct footprints overall, the method built networks among $475$ factors: $38\,393$ distinct arcs in total, $11\,193$ per cell type on average (Neph and colleagues, 2012). Known circuits were recovered, such as the cross-regulation of the muscle factors and of the pluripotency factors of embryonic stem cells. The networks were markedly cell-type specific: most arcs occurred in a single cell type or a few, and only about $5\,\%$ were present in all $41$.

**Example 11.2.1** How much overlap would be expected by chance? A network of $11\,193$ arcs among $475$ factors has density $11\,193/475^2 = 0.0496$ (counting self-arcs). Two such networks drawn independently would share on average $11\,193^2/475^2 = 555$ arcs, also about $5\,\%$ of each. The figure of $5\,\%$ shared by all cell types is therefore not small: arcs shared by $41$ independent networks of this density would number $475^2 \times 0.0496^{41} \approx 10^{-48}$. The comparison shows that "only $5\,\%$" and "far more than chance" are both true, and that a statement about overlap needs its null model.

The cell-type specificity has several causes: factors and cofactors are expressed differently, chromatin accessibility differs, so that the same motif is occupied in one cell type and closed in another; but also technical ones, since footprints are noisy, motifs are incomplete, and a missing arc in one cell type may be a false negative. Systematic comparison helps to separate them: the networks of functionally related cell types were more similar to each other than to those of unrelated cell types, as measured by a normalized degree vector of the $475$ factors (the contribution of each factor to the arcs of the network), so that clustering the cell types by their networks grouped functionally related types together. Despite the different arcs, all $41$ networks had similar global architectures, and the same small subgraphs, in particular the feed-forward loop, were enriched in all of them as **network motifs** ([1.4.7](/1.4.7#def-7.8.4); their function is the subject of [7.9.15](/7.9.15)).

The limitations of binding networks are those of their evidence: motifs are known for only part of the factors and the recognition sequences are of varying quality; distal elements are missed by a window around the promoter; indirect binding through other proteins leaves no motif; and occupancy is not activity. Binding maps therefore serve best as a prior that restricts which arcs are allowed, to be combined with expression data (11.5.3, 11.7).

## 11.3. Correlation Networks

### 11.3.1. Co-Expression

Genes that are regulated together vary together. Across many samples (conditions, individuals, tumors, single cells) the expression profiles of a factor and its targets, and of the targets with each other, are correlated, and this covariation can be read without any binding data.

**Definition 11.3.1 (Co-Expression Network)** A **co-expression network** is an undirected weighted graph whose vertices are genes and whose edge weights $a_{ij} \in [0, 1]$ measure the similarity of the expression profiles of genes $i$ and $j$ across a set of samples, usually a function of their correlation; a hard-thresholded network keeps only the edges with similarity above a cutoff.

The similarity is the **correlation coefficient** of log-scale expression, or **Spearman's rank correlation coefficient** for robustness to outliers. Significance of each correlation, with the **false discovery rate** controlled over all $\binom{20\,000}{2} \approx 2 \times 10^8$ pairs, gives a hard threshold. Co-expression is the oldest genome-wide method (Eisen and colleagues, 1998) and the most widely used; it predicts functional relations, shared regulation and membership in pathways ([7.9.10](/7.9.10#sec-10.4)), but its edges are undirected and mostly indirect: two targets of one factor are correlated with each other as strongly as with the factor.

### 11.3.2. Partial Correlation and the Graphical Lasso

Indirect correlations are removed by conditioning. For a regulatory chain $X \to Y \to Z$ in which each step is linear with Gaussian noise, $X$ and $Z$ are correlated because both depend on $Y$, but they are independent given $Y$; the **partial correlation coefficient** ([3.3.9](/3.3.9)) of $X$ and $Z$ given $Y$ is zero.

**Example 11.3.1** Let $X \sim \mathcal{N}(0, 1)$, $Y = 0.8X + \varepsilon_1$ and $Z = 0.8Y + \varepsilon_2$, with noise variances $0.36$ so that all three variables have variance $1$. Then $\operatorname{Corr}(X, Y) = \operatorname{Corr}(Y, Z) = 0.8$ and $\operatorname{Corr}(X, Z) = 0.64$: a hard threshold at $0.5$ would add the indirect edge $X$–$Z$. The partial correlation is
$$
\rho_{XZ\cdot Y} = \frac{\rho_{XZ} - \rho_{XY}\rho_{YZ}}{\sqrt{(1 - \rho_{XY}^2)(1 - \rho_{YZ}^2)}} = \frac{0.64 - 0.64}{0.36} = 0,
$$
and the edge disappears.

Conditioning on all other genes at once has a compact form for the **multivariate normal distribution**.

**Formula 11.3.1 (Partial Correlations and the Precision Matrix)** Let $\boldsymbol{X} \sim \mathcal{N}_p(\boldsymbol{\mu}, \Sigma)$ and $\Omega = \Sigma^{-1}$, the precision matrix. The partial correlation of $X_i$ and $X_j$ given all other components is
$$
\rho_{ij\cdot\text{rest}} = -\frac{\Omega_{ij}}{\sqrt{\Omega_{ii}\Omega_{jj}}},
$$
and $X_i$ and $X_j$ are conditionally independent given the rest if and only if $\Omega_{ij} = 0$.

The graph with an edge wherever $\Omega_{ij} \neq 0$ is the Gaussian graphical model of the data. Estimating it requires the inverse of the **covariance matrix**, which does not exist when there are fewer samples than genes ($n < p$), and is very noisy when $n$ is not much larger than $p$. Sparse estimates solve both problems.

**Formula 11.3.2 (Graphical Lasso)** (Friedman, Hastie and Tibshirani, 2008) Given the sample covariance matrix $S$ and a penalty $\lambda > 0$, the *graphical lasso* estimates the precision matrix as
$$
\hat\Omega = \arg\max_{\Omega \succ 0}\Bigl\{\log\det\Omega - \operatorname{tr}(S\Omega) - \lambda\sum_{i \neq j}\lvert\Omega_{ij}\rvert\Bigr\},
$$
the Gaussian log-likelihood with an $\ell_1$ penalty on the off-diagonal entries, which sets many of them exactly to zero.

The penalty plays the role of the **Lasso** in regression: a larger $\lambda$ gives a sparser graph, and $\lambda$ is chosen by **cross-validation** or by stability across subsamples. A closely related estimator, neighborhood selection (Meinshausen and Bühlmann, 2006), regresses each gene on all others with the lasso and joins $i$ and $j$ when either regression selects the other; it is the regression approach of 11.5 applied to all genes symmetrically. Both assume linear Gaussian dependence, which expression on a log scale satisfies only roughly, and both treat factors and targets alike, so that edges remain undirected.

### 11.3.3. Weighted Co-Expression Network Analysis

Weighted gene co-expression network analysis (WGCNA; Zhang and Horvath, 2005; Langfelder and Horvath, 2008) gives up the reconstruction of individual edges and uses the co-expression network to find modules of co-regulated genes, which are then related to traits.

**Algorithm 11.3.1 (WGCNA)** Given an expression matrix of $p$ genes in $n$ samples and sample traits:

1. Adjacency. Compute all correlations $r_{ij}$ and the soft-thresholded adjacency $a_{ij} = \lvert r_{ij}\rvert^\beta$ (unsigned) or $a_{ij} = \bigl((1 + r_{ij})/2\bigr)^\beta$ (signed), with $a_{ii} = 0$. The power $\beta$ suppresses weak correlations continuously instead of cutting them at a threshold; it is chosen as the smallest value for which the degree distribution of the network is approximately a power law (the scale-free topology criterion), typically $\beta = 6$ for unsigned networks.
2. Topological overlap. Replace the adjacency by the topological overlap of Definition 11.3.2.
3. Modules. Cluster the genes by **hierarchical clustering** with average linkage on the dissimilarity $1 - \mathrm{TOM}_{ij}$ and cut the tree into branches (by a dynamic tree cut, with a minimum module size); each branch is a module, and the genes in no branch are left unassigned.
4. Module eigengenes. Summarize each module by its first principal component across samples (**principal component analysis**), the module eigengene, and correlate eigengenes with the traits.
5. Hub genes. Within a module of interest, rank genes by intramodular connectivity $\sum_{j \in \text{module}}a_{ij}$ or by module membership, the correlation of the gene with the eigengene.

The cost is $O(p^2n)$ for the correlations and $O(p^3)$ for the topological overlap; for $p = 20\,000$ genes, $p^2 = 4 \times 10^8$ entries must be held in memory, which is why analyses are often restricted to the most variable genes or computed block by block.

**Definition 11.3.2 (Topological Overlap)** In a weighted network with adjacency $a_{ij} \in [0, 1]$ and connectivities $k_i = \sum_ja_{ij}$, the **topological overlap** of vertices $i \neq j$ is
$$
\mathrm{TOM}_{ij} = \frac{l_{ij} + a_{ij}}{\min(k_i, k_j) + 1 - a_{ij}}, \qquad l_{ij} = \sum_{u \neq i, j}a_{iu}a_{uj};
$$
it lies in $[0, 1]$ and is large when $i$ and $j$ are connected to each other and to the same other vertices (Ravasz and colleagues, 2002, for unweighted networks).

**Example 11.3.2** Let genes $i$ and $j$ have $a_{ij} = 0.2$ and share two neighbors, $u$ with $a_{iu} = 0.8$, $a_{ju} = 0.7$ and $v$ with $a_{iv} = 0.6$, $a_{jv} = 0.5$, and no other connections. Then $k_i = 1.6$, $k_j = 1.4$, $l_{ij} = 0.8 \times 0.7 + 0.6 \times 0.5 = 0.86$ and $\mathrm{TOM}_{ij} = (0.86 + 0.2)/(1.4 + 1 - 0.2) = 0.48$: the weak direct similarity is reinforced by the shared neighbors. Two genes with the same direct similarity but no shared neighbors would have $\mathrm{TOM}_{ij} = 0.2/(0.2 + 1 - 0.2) = 0.2$.

![Weighted co-expression network analysis of 600 simulated genes in 60 samples: five modules of 140, 110, 80, 50 and 20 genes, each following a module eigengene with gene-specific loadings of random sign, and 200 noise genes. A: the scale-free topology fit index for the unsigned adjacency |r|^β; it exceeds the conventional cutoff 0.8 (dashed) already at β = 4 (dotted) and stays high for all larger β. B: the mean connectivity falls by orders of magnitude over the same range (dotted: β = 6). C: the topological overlap at β = 6, with genes ordered by average-linkage clustering on 1 − TOM; the bar marks the simulated modules (grey: noise genes). Cutting the tree at height 0.97 and keeping branches of at least 15 genes recovers the five modules (adjusted Rand index 0.99); no noise gene enters a module and 3 module genes are left unassigned](./plots/wgcna_modules.py)

The simulation shows both the strength of the method and the weakness of its tuning rule. Modules of correlated genes stand out clearly in the topological overlap, and the noise genes, whose correlations with everything are small, are excluded. But the scale-free fit index is high over a wide range of $\beta$, here for every $\beta \ge 4$, although the simulated network has no scale-free structure at all: the criterion constrains $\beta$ only loosely, and the premise that co-expression networks should be scale-free is itself an assumption (on the evidence for scale-free biological networks see [1.4.7](/1.4.7#sec-7.4.5) and [7.9.12](/7.9.12#sec-12.1)). In practice the modules are robust to the choice of $\beta$ within that range, and it is the module structure, not the exponent, that carries the biology.

Module–trait correlations are associations: a module correlated with a disease state may cause it, respond to it, or reflect a change in cell-type composition of the samples, which is the most common cause of large modules in tissue data. Modules found in bulk tissue should therefore be compared with cell-type signatures ([7.9.5](/7.9.5)), and in single-cell data co-expression is computed within cell types, on aggregated metacells or **pseudobulk** profiles, because the sparsity of single-cell counts weakens gene–gene correlations (hdWGCNA; Morabito and colleagues, 2023).

## 11.4. Information-Theoretic Methods

### 11.4.1. Mutual Information and Conditional Mutual Information

Correlation measures linear (Pearson) or monotone (Spearman) dependence. Regulation is often neither: a factor may activate a gene only above a threshold, act as an activator at low and a repressor at high concentration, or regulate a gene through a cycle such as the cell cycle. The **mutual information** ([Definition 35.3.1](/7.6.35#def-35.3.1)),
$$
I(X; Y) = \sum_{x, y}p(x, y)\log\frac{p(x, y)}{p(x)p(y)} = H(X) - H(X \mid Y),
$$
is zero if and only if $X$ and $Y$ are independent, and positive for any kind of dependence; here $H(X \mid Y)$ is the **conditional entropy**. For a bivariate normal distribution it is a function of the correlation alone.

**Formula 11.4.1 (Mutual Information of a Bivariate Normal Distribution)** If $(X, Y)$ is bivariate normal with correlation $\rho$, then
$$
I(X; Y) = -\tfrac{1}{2}\ln(1 - \rho^2)\ \text{nats} = -\tfrac{1}{2}\log_2(1 - \rho^2)\ \text{bits}.
$$

![Correlation and mutual information for six kinds of dependence between a regulator x and a target y (simulated, n = 400 each). Each panel gives the Pearson correlation r, the Spearman correlation ρ and the mutual information I in bits, estimated with the k-nearest-neighbor estimator of Kraskov, Stögbauer and Grassberger (k = 4). Linear and saturating responses are detected by all three; the U-shaped, periodic and ring-shaped dependences have correlations near zero (or weak) but clear mutual information; independent data give values near zero for all three](./plots/mi_vs_correlation.py)

In the figure, the linear panel has $r = 0.82$ and $I = 0.76$ bits, close to the $-\tfrac12\log_2(1 - 0.82^2) = 0.80$ bits of Formula 11.4.1. The U-shaped response has $r = 0.00$ but $I = 1.53$ bits, more than the linear case; the ring has $r = -0.04$ and $I = 1.25$ bits. For the saturating response the correlation is high ($0.86$) but reflects mostly the steep part; the mutual information ($1.48$ bits) also credits the plateau, where the target no longer depends on the regulator. Mutual information has a price: it ignores the sign of the dependence, and it is harder to estimate than a correlation.

**Definition 11.4.1 (Conditional Mutual Information)** The **conditional mutual information** of $X$ and $Y$ given $Z$ is
$$
I(X; Y \mid Z) = H(X \mid Z) - H(X \mid Y, Z) = \sum_{x, y, z}p(x, y, z)\log\frac{p(x, y \mid z)}{p(x \mid z)p(y \mid z)},
$$
the information that $Y$ carries about $X$ beyond what $Z$ carries; it is zero if and only if $X$ and $Y$ are conditionally independent given $Z$.

Two properties follow from the definitions and are used below. The chain rule, $I(X; Y, Z) = I(X; Z) + I(X; Y \mid Z)$, splits the information that two variables carry jointly. And conditional mutual information can be larger or smaller than the unconditional one: conditioning on a common cause removes dependence, while conditioning on a common effect creates it.

### 11.4.2. Estimation

Estimating mutual information from $n$ samples of continuous expression values is a density estimation problem.

| Estimator | Principle | Remarks |
|---|---|---|
| Binning (plug-in) | discretize each variable into $m$ bins, use the observed frequencies | simple; biased upward by about $(m - 1)^2/(2n)$ nats for independent variables (Miller–Madow); results depend on $m$ |
| Adaptive partitioning | split the $(x, y)$ plane recursively into quadrants at the medians until the points in a cell look uniform (a $\chi^2$ test) (Darbellay and Vajda, 1999) | adapts resolution to the data; used by ARACNe-AP |
| Kernel density | estimate $p(x, y)$, $p(x)$, $p(y)$ with Gaussian kernels (**kernel density estimation**) and average $\log[p(x,y)/p(x)p(y)]$ over the samples | smooth; bandwidth choice matters; used by the original ARACNe |
| $k$-nearest neighbors | from the distance of each point to its $k$-th neighbor in the joint space and the counts of points within that distance in each marginal (Kraskov, Stögbauer and Grassberger, 2004) | nearly unbiased for independent variables; the default for continuous data |
| Gaussian | Formula 11.4.1 with the sample correlation | fast; captures only linear dependence |

The bias of the plug-in estimator matters because network inference ranks millions of pairs, most of them independent. For two independent genes measured in $n = 100$ samples and $m = 10$ equal-frequency bins per gene, simulation gives a mean plug-in estimate of $0.50$ nats ($0.72$ bits), while the true value is $0$; the first-order Miller–Madow approximation $81/200 = 0.41$ nats underestimates it at this small $n$. A threshold for significance is therefore set by a null distribution, obtained by permuting the samples of one gene, rather than at zero.

### 11.4.3. The Data Processing Inequality

Mutual information, like correlation, is high for indirect pairs: the two ends of a chain share information through the middle. An inequality of information theory says that the indirect pair always shares less than either direct pair.

**Theorem 11.4.1 (Data Processing Inequality)** If $X$, $Y$, $Z$ form a **Markov chain** $X \to Y \to Z$, that is, $X$ and $Z$ are conditionally independent given $Y$, then
$$
I(X; Z) \le \min\{I(X; Y), I(Y; Z)\}.
$$

**Proof** By the chain rule applied in two orders,
$$
I(X; Y, Z) = I(X; Z) + I(X; Y \mid Z) = I(X; Y) + I(X; Z \mid Y).
$$
Conditional independence gives $I(X; Z \mid Y) = 0$, so $I(X; Z) = I(X; Y) - I(X; Y \mid Z) \le I(X; Y)$, since conditional mutual information is nonnegative. The chain $Z \to Y \to X$ is also Markov, and the same argument gives $I(X; Z) \le I(Y; Z)$. $\square$

In words: no processing of $Y$, by a cell or an analyst, can create information about $X$ that $Y$ does not have. For a network the consequence is a local test. In every triangle of genes connected by significant mutual information, if one of the three pairs is indirect (the chain passes through the third gene), it is the pair with the smallest mutual information.

**Algorithm 11.4.1 (ARACNe)** (Basso and colleagues, 2005; Margolin and colleagues, 2006) Algorithm for the reconstruction of accurate cellular networks. Given expression profiles of $p$ genes in $n$ samples (and optionally a list of transcription factors):

1. Estimate the mutual information $I_{ij}$ of all pairs (or all pairs that contain a factor).
2. Remove pairs with $I_{ij}$ below a threshold $I_0$ chosen from a null distribution of permuted data at a given p-value.
3. For every triangle $i, j, k$ of the remaining edges, remove the edge with the smallest mutual information, unless it is within a tolerance $\varepsilon$ (often $0$ to $15\,\%$) of the next smallest.
4. Optionally, repeat on bootstrap samples of the data and keep the edges found significantly more often than chance (consensus network).

Step 1 costs $O(p^2n)$ with the Gaussian estimator and up to $O(p^2n\log n)$ with neighbor-based estimators; step 3 costs $O(p^3)$ in the worst case and much less in sparse networks, where it examines each edge against the common neighbors of its ends.

**Example 11.4.1** For the chain of Example 11.3.1, Formula 11.4.1 gives $I(X; Y) = I(Y; Z) = -\tfrac12\ln(1 - 0.64) = 0.511$ nats and $I(X; Z) = -\tfrac12\ln(1 - 0.64^2) = 0.263$ nats. Theorem 11.4.1 holds with room to spare, and the pruning step removes the edge $X$–$Z$, the smallest of the triangle.

![The data processing inequality removes indirect edges (simulated, n = 300 samples of a linear Gaussian model). A: the true network of eight genes, with a feed-forward loop A → B → G, A → G. B: the mutual-information network: all pairs whose Gaussian mutual information exceeds the largest of 2000 values from permuted pairs, 26 edges of which the 18 in red join genes that are not directly connected. C: after the pruning step of Algorithm 11.4.1 with tolerance 0, all 18 indirect edges are gone, but so is the true edge A → G of the feed-forward loop (grey, dashed), the weakest of its triangle](./plots/dpi.py)

The figure shows what the inequality buys and what it costs. Of the $26$ edges with significant mutual information, $18$ are indirect, and pruning removes all of them while keeping $7$ of the $8$ true edges. The lost edge is part of a feed-forward loop, a triangle in which all three edges are direct: the inequality assumes that one of them is indirect, and removes the weakest ($I_{AG} = 0.28$ against $I_{AB} = 0.34$ and $I_{BG} = 0.44$ nats). Feed-forward loops are a common motif of transcription networks ([7.9.15](/7.9.15)), so ARACNe systematically underrepresents them; the tolerance $\varepsilon$ keeps triangles whose weakest edge is close to the others, at the price of keeping some indirect edges. The output is undirected; when only factors are allowed as regulators, edges between a factor and a non-factor are read as factor-to-gene arcs.

ARACNe was introduced with a network of human B cells reconstructed from expression profiles of normal and malignant B cells; the MYC regulon it predicted, with MYC as a major **hub** of the network, was validated by chromatin immunoprecipitation (Basso and colleagues, 2005). It has since been applied to many tumor types, where it supplies the regulons used in 11.7, and its adaptive-partitioning implementation (ARACNe-AP; Lachmann and colleagues, 2016) runs on whole genomes.

### 11.4.4. Context Likelihood of Relatedness

A different correction for indirect and spurious edges compares each pair with the background of each gene. Some genes have high mutual information with many others, for instance because they vary strongly across the samples, and their edges are less informative.

**Formula 11.4.2 (Context Likelihood of Relatedness)** (Faith and colleagues, 2007) Let $\mu_i$ and $\sigma_i$ be the mean and standard deviation of the mutual information of gene $i$ with all other genes, and $z_i = \max\{0, (I_{ij} - \mu_i)/\sigma_i\}$, $z_j$ the analogous value for gene $j$. The CLR score of the pair is
$$
z_{ij} = \sqrt{z_i^2 + z_j^2}.
$$

**Example 11.4.2** A pair has $I_{ij} = 0.30$; gene $i$ has background $\mu_i = 0.10$, $\sigma_i = 0.05$ and gene $j$ has $\mu_j = 0.25$, $\sigma_j = 0.10$. Then $z_i = 4$, $z_j = 0.5$ and $z_{ij} = \sqrt{16.25} = 4.03$: the pair is exceptional for gene $i$ though ordinary for gene $j$.

Applied to $445$ microarray profiles of *Escherichia coli*, CLR recovered known regulatory interactions and predicted $1079$ interactions at an estimated precision of $60\,\%$, of which a sample was confirmed by ChIP (Faith and colleagues, 2007).

### 11.4.5. Modulators of Regulation

A factor's effect on its targets often depends on a third molecule: a kinase that activates it, a cofactor, a protease that degrades it. Such modulation is invisible in pairwise dependence but appears as a change of the factor–target dependence with the level of the modulator, a three-way interaction measured by conditional mutual information.

**Algorithm 11.4.2 (MINDy)** (Wang and colleagues, 2009) Modulator inference by network dynamics. For a factor $T$, a candidate modulator $M$ and a target $G$:

1. Sort the samples by the expression of $M$ and take the two tails (for example the lowest and highest third).
2. Estimate the factor–target mutual information in each tail, $I^-(T; G)$ and $I^+(T; G)$, and their difference $\Delta I = I^+ - I^-$.
3. Assess $\Delta I$ against a null distribution obtained by permuting the samples between the tails; a significant $\Delta I > 0$ suggests that $M$ enhances the regulation of $G$ by $T$, $\Delta I < 0$ that it suppresses it.
4. Call $M$ a modulator of $T$ if it changes the regulation of a significant number of the targets of $T$.

**Example 11.4.3** If the correlation between factor and target is $0.7$ in samples with high modulator and $0.1$ in samples with low modulator, Formula 11.4.1 gives $I^+ = 0.337$ and $I^- = 0.005$ nats, and $\Delta I = 0.33$ nats; the modulator, invisible to any pairwise analysis if its own correlation with the target is weak, gates the regulation.

In human B cells, MINDy identified post-translational modulators of MYC, among them the kinase STK38, which affects MYC phosphorylation and degradation, BHLHB2, which antagonizes MYC activity, and MEF2B, which enhances it (Wang and colleagues, 2009). Three-way analyses need many samples with a wide range of each variable. Tumors provide them: variation among tumors of the same cancer type, a nuisance for many analyses, is the dynamic range from which regulatory interactions are inferred, which is why several hundred tumor profiles of one type are a standard input.

## 11.5. Regression and Machine Learning

### 11.5.1. One Regression per Gene

The regression view of network inference models each gene as a function of its potential regulators,
$$
x_j = f_j(\boldsymbol{x}_{R_j}) + \varepsilon_j, \qquad R_j \subseteq \{\text{transcription factors}\} \setminus \{j\},
$$
and estimates the regulators of each gene separately. This splits one problem with $p^2$ unknowns into $p$ independent problems with $\lvert R_j\rvert$ unknowns each, the dimension reduction that makes inference possible (Yeung, Tegnér and Collins, 2002). For linear $f_j$ with the **Lasso**, the regulators of gene $j$ are the factors with nonzero coefficients,
$$
\hat{\boldsymbol{\beta}}_j = \arg\min_{\boldsymbol{\beta}}\Bigl\{\tfrac{1}{2n}\bigl\Vert\boldsymbol{x}_j - X_R\boldsymbol{\beta}\bigr\Vert^2 + \lambda\Vert\boldsymbol{\beta}\Vert_1\Bigr\},
$$
with $\lambda$ chosen by cross-validation; correlated factors, such as paralogs, are better handled by the **elastic net**, which tends to select them together ([7.7.21](/7.7.21), [3.3.12](/3.3.12)). The coefficients are signed and directed, from factor to gene, but only because the candidate regulators were restricted to factors.

### 11.5.2. Tree Ensembles: GENIE3

Nonlinear and combinatorial regulation, such as a gene that requires two factors at once, is captured by flexible regressors.

**Algorithm 11.5.1 (GENIE3)** (Huynh-Thu, Irrthum, Wehenkel and Geurts, 2010) For each gene $j$:

1. Train a **random forest** (or extremely randomized trees) to predict the expression of $j$ from the expression of all transcription factors other than $j$.
2. For each factor $i$, compute its importance $w_{ij}$, the total decrease of the variance of $x_j$ achieved by the splits on $x_i$, summed over all trees and normalized by the variance of $x_j$.

Rank all factor–gene pairs by $w_{ij}$; the top of the list is the predicted network. The cost is $p$ forests of $T$ trees each, $O(pT\,\lvert R\rvert^{1/2}\,n\log n)$ when $\sqrt{\lvert R\rvert}$ factors are tried at each split.

GENIE3 was the best performer of the DREAM4 multifactorial network challenge and one of the best in DREAM5 (11.8). Its importances are directed (factor to gene) by construction and scale-free in the sense of needing no distributional assumptions, but they are not signed, and two correlated factors share the importance of their common effect, as in any **ensemble learning** method ([4.6.6](/4.6.6)). GRNBoost2 (Moerman and colleagues, 2019) replaces the forests by gradient boosting with early stopping and scales to hundreds of thousands of single cells; it is the first step of SCENIC (11.7.2).

### 11.5.3. Integrating Prior Knowledge

Expression data alone cannot tell a direct target from a gene correlated with it through other routes; binding data alone cannot tell a functional site from an inert one. Combining them reduces both errors. Prior knowledge (ChIP-seq peaks, motifs in accessible regions, curated interactions, protein interactions, **Gene Ontology** annotations) enters in two ways.

| Role | How | Example |
|---|---|---|
| Filter | restrict the candidate regulators $R_j$ of each gene to factors with binding or motif evidence in its regulatory regions | CellOracle restricts regulators to factors with motifs in accessible elements linked to the gene ([7.9.7](/7.9.7#sec-7.6.2)); SCENIC prunes co-expression modules by motif enrichment |
| Integrator | weight the evidence inside the statistical model | the Inferelator (Bonneau and colleagues, 2006) and its successors give smaller lasso penalties to prior edges; Bayesian priors on network structure |

A filter reduces the number of tests and the false positives, but it inherits the false negatives of the prior: a factor without a known motif can never be found. An integrator lets strong data override a missing prior, at the cost of more parameters to tune.

## 11.6. Causality and Perturbations

### 11.6.1. Bayesian Networks

Correlation, mutual information and regression detect dependence; regulatory arcs are causal claims. Probabilistic graphical models on a **directed acyclic graph** make the link precise.

**Definition 11.6.1 (Bayesian Network)** A **Bayesian network** for random variables $X_1, \dots, X_p$ is a directed acyclic graph $\mathcal{G}$ on the vertices $1, \dots, p$ together with conditional distributions $p(x_i \mid \boldsymbol{x}_{\mathrm{pa}(i)})$ of each variable given its parents in $\mathcal{G}$, such that the joint distribution factorizes as
$$
p(x_1, \dots, x_p) = \prod_{i=1}^{p}p(x_i \mid \boldsymbol{x}_{\mathrm{pa}(i)}).
$$

The factorization encodes **conditional independence** relations: each variable is independent of its non-descendants given its parents. Structure learning searches for the graph that best explains the data, either by maximizing a score such as the **Bayesian information criterion** over graphs (score-based search) or by testing conditional independences and assembling a graph consistent with them (constraint-based, for example the PC algorithm of Spirtes, Glymour and Scheines). The search space is enormous: the number of directed acyclic graphs on $p$ labeled vertices is $25$ for $p = 3$, $29\,281$ for $p = 5$ and $4.2 \times 10^{18}$ for $p = 10$ (Robinson's recurrence), so search is heuristic and limited to tens or hundreds of genes, or to modules.

More fundamentally, observational data cannot distinguish all graphs.

**Definition 11.6.2 (Markov Equivalence)** Two directed acyclic graphs are **Markov equivalent** if they encode the same set of conditional independence relations, and hence fit any observational data equally well.

**Theorem 11.6.1 (Verma and Pearl, 1990)** Two directed acyclic graphs are Markov equivalent if and only if they have the same skeleton (the same edges, ignoring direction) and the same v-structures (pairs of non-adjacent vertices with arcs into a common child, $i \to k \leftarrow j$).

For three genes in a chain, the graphs $X \to Y \to Z$, $X \leftarrow Y \leftarrow Z$ and $X \leftarrow Y \to Z$ are equivalent: all three say only that $X$ and $Z$ are independent given $Y$. The v-structure $X \to Y \leftarrow Z$ is different: $X$ and $Z$ are independent, but dependent given $Y$. Observational data thus determine the direction of some arcs (those in v-structures, and those whose reversal would create one) and leave the others undetermined.

Interventions break the equivalence. Setting $X$ by a knockout changes $Z$ in the chain $X \to Y \to Z$ but not in $X \leftarrow Y \to Z$. In a landmark study, Bayesian network learning on multiparameter flow cytometry of $11$ phosphorylated signaling proteins and phospholipids in thousands of single human T cells, measured under several perturbations of individual pathway components, reconstructed most of the known causal relations of the network and predicted new ones that were confirmed experimentally (Sachs and colleagues, 2005). Single cells supplied the sample size, and the perturbations the directions. Dynamic Bayesian networks, defined on time-lagged copies of the variables, use time series in the same way, and allow feedback loops, which a static directed acyclic graph cannot represent. The causal framework, with its assumptions (no unmeasured common causes, faithfulness), is treated in [7.7.15](/7.7.15).

### 11.6.2. Perturbation Data

Perturbations are the most direct evidence of regulation, and pooled screens now provide them at scale: Perturb-seq knocks down or knocks out thousands of genes and reads the transcriptome of each perturbed cell ([7.9.7](/7.9.7#sec-7.7.2)), giving a matrix of perturbation effects of each gene on every other. That matrix records total effects, direct and indirect: knocking down a factor changes its targets and the targets of its targets. Recovering direct effects from total effects is again an inverse problem, with a clean solution in the linear regime.

**Formula 11.6.1 (Modular Response Analysis)** (Kholodenko and colleagues, 2002) Let a network of $p$ genes be near a steady state of $\mathrm{d}\boldsymbol{x}/\mathrm{d}t = \boldsymbol{f}(\boldsymbol{x}, \boldsymbol{u})$, with Jacobian $J = \partial\boldsymbol{f}/\partial\boldsymbol{x}$, and let experiment $k$ perturb only gene $k$ (a small change of a parameter $u_k$ that acts on it directly). If $R$ is the matrix whose column $k$ is the measured change of the steady state in experiment $k$, then the local response coefficients $r_{ij} = J_{ij}/(-J_{ii})$, the direct effect of gene $j$ on gene $i$ relative to the self-decay of $i$, are
$$
r_{ij} = -\frac{(R^{-1})_{ij}}{(R^{-1})_{ii}}, \qquad r_{ii} = -1.
$$

**Proof** Linearizing at the steady state, the perturbation of $u_k$ by $\delta_k$ shifts the state by $R_{\cdot k} = -J^{-1}\boldsymbol{e}_k\,(\partial f_k/\partial u_k)\delta_k$, so $R = -J^{-1}D$ with $D$ diagonal. Hence $J = -DR^{-1}$: row $i$ of $J$ is row $i$ of $R^{-1}$ times the unknown factor $-D_{ii}$. The ratio $J_{ij}/J_{ii} = (R^{-1})_{ij}/(R^{-1})_{ii}$ does not depend on the unknown factor, and $r_{ij} = -J_{ij}/J_{ii}$. $\square$

**Example 11.6.1** In a chain $1 \to 2 \to 3$ with direct effects $r_{21} = r_{32} = 0.8$ and unit perturbations, the total responses are
$$
R = \begin{bmatrix} 1 & 0 & 0 \\ 0.8 & 1 & 0 \\ 0.64 & 0.8 & 1 \end{bmatrix}:
$$
perturbing gene $1$ changes gene $3$ by $0.64$, an indirect effect that a screen would report as a hit. Inverting $R$ gives back $r_{31} = 0$, $r_{21} = r_{32} = 0.8$. With noise of standard deviation $0.05$ added to each entry of $R$, the recovered coefficients are $r_{21} = 0.72$, $r_{32} = 0.79$ and spurious values of $0.01$–$0.03$ for the absent arcs: the inversion amplifies noise, more so for larger networks and when perturbation effects are small.

The approach requires one perturbation per gene, effects in the linear range, and a steady state; it handles feedback loops, which Bayesian networks cannot. In large Perturb-seq data, most perturbations have small effects and many share a generic stress response, so direct effects are estimated with regularized versions of the same idea, and with ordinary differential equation models for time courses (**ordinary differential equations**, [7.9.14](/7.9.14)). Inferring causal networks from single-cell perturbation screens is an active field whose methods are still being benchmarked against simple baselines ([7.9.7](/7.9.7#sec-7.7.3)).

## 11.7. Regulon Activity and Master Regulators

### 11.7.1. Activity from Targets

The mRNA level of a transcription factor is a poor measure of what it does. Its activity depends on phosphorylation, ligands, nuclear translocation, cofactors and degradation, none of which appears in its own expression. The expression of its targets integrates all of them.

**Definition 11.7.1 (Regulon Activity)** Given a set of signed targets of a transcription factor in a context (its **regulon**, here the activated and repressed targets inferred from binding, motifs or expression), the **regulon activity** of the factor in a sample, or its differential activity between two conditions, is a statistic of the expression of the targets in which activated targets count positively and repressed targets negatively, such as a weighted mean of their standardized expression or an enrichment score of the regulon in a ranked signature.

![A transcription factor whose activity changes while its mRNA does not (simulation: 2000 genes, 20 samples in each of two phenotypes). The factor T is activated post-translationally in phenotype B: its 40 activated targets rise and its 20 repressed targets fall, by 0.6 standard deviations on average. A: the mRNA of T does not differ (Welch test p = 0.34). B: the two-tailed enrichment of the regulon in the signature ranked by the t statistic: activated targets (green ticks, top) concentrate at the top and repressed targets (red ticks, bottom) at the bottom; enrichment scores 0.79 and 0.84, permutation p ≈ 0.001, the smallest attainable with 1000 random gene sets. C: the activity score of T per sample, the mean standardized expression of activated minus repressed targets, separates the phenotypes completely (Welch test p = 2 × 10⁻¹⁸)](./plots/regulon_activity.py)

The methods that compute such activities from curated or inferred regulons (VIPER, decoupler, and the single-sample scores AUCell and GSVA) are described in [7.9.3](/7.9.3#sec-3.4); here we treat how the regulons are built and how activities identify the regulators of a phenotype.

### 11.7.2. Single-Cell Regulons: SCENIC

**Algorithm 11.7.1 (SCENIC)** (Aibar and colleagues, 2017) Single-cell regulatory network inference and clustering. Given a count matrix of single cells:

1. Co-expression. For each gene, rank the transcription factors by GENIE3 or GRNBoost2 importance (Algorithm 11.5.1) and form candidate modules, sets of genes co-expressed with a factor.
2. Motif pruning (RcisTarget). Rank all genes by the motif score of the factor in their regulatory regions (a window around the transcription start site); keep a module only if its genes are enriched at the top of this ranking, and keep only the genes at the leading edge of the enrichment. The result is a regulon of likely direct targets.
3. Scoring (AUCell). For each cell, rank all genes by expression and compute the area under the recovery curve of each regulon among the top-ranked genes, a score independent of library size and normalization.
4. Clustering. Binarize or use the activity scores as features to cluster cells and to visualize them; regulons specific to a cluster indicate its identity regulators.

Step 2 turns a co-expression network into a regulatory one: a module co-expressed with a factor but not enriched for its motif is discarded as indirect or as the product of cell-type composition. Activities computed over many target genes are less sparse than single genes and transfer between data sets and species better than gene expression. The weaknesses are those of the parts: activating regulons are found more reliably than repressive ones (correlation-based modules of repressed genes are rarely enriched for the motif), factors without a known motif are lost, and co-expression across cell types confounds regulation with cell identity.

### 11.7.3. Master Regulator Analysis

A **master regulator** in the sense of [7.3.24](/7.3.24#def-24.4.1) is a factor whose activity is sufficient to establish a cellular program. Network inference turns this into a computational question: given two phenotypes, which factors' regulons explain the expression differences between them?

**Algorithm 11.7.2 (Master Regulator Analysis)** (MARINa; Lefebvre and colleagues, 2010; Carro and colleagues, 2010) Given expression profiles of samples of phenotypes A and B and a context-specific network (for example from ARACNe on a large collection of samples of the same tissue):

1. Signature. Rank the genes by a differential-expression statistic of B against A.
2. Regulons. For each factor, take its targets in the network, split into positively and negatively correlated targets.
3. Enrichment. Test each regulon by a two-tailed **gene set enrichment analysis**: positive targets at the top and negative targets at the bottom of the signature indicate increased activity in B, the reverse decreased activity. Assess significance by permuting the sample labels.
4. Shadow analysis. If the regulons of two significant factors overlap, the activity of one can make the other appear active. Split the targets into those of factor 1 only, those of factor 2 only, and the shared ones, and test each part separately: if the targets of factor 1 alone are not enriched, factor 1 is only a shadow of factor 2; if both unique parts are enriched more than the shared part, the factors act independently or antagonistically; if the shared targets are enriched more than either unique part, the factors act synergistically.
5. Report the factors with significant, non-shadow activity as candidate master regulators, and validate them by perturbation.

The analysis was introduced on high-grade glioma. Glioblastomas fall into expression subtypes, of which the mesenchymal subtype, with migratory, invasive and angiogenic features, has the worst prognosis. An ARACNe network built from glioma profiles and master regulator analysis of the mesenchymal against the proneural signature identified a small set of factors whose regulons together covered most of the mesenchymal signature; among them, C/EBPβ and STAT3 behaved as synergistic initiators. Ectopic expression of both reprogrammed neural stem cells toward the aberrant mesenchymal lineage, knockdown of both in glioma cells collapsed the mesenchymal signature and reduced tumor aggressiveness, and their combined expression in patients' tumors predicted poor outcome (Carro and colleagues, 2010). The case shows the full cycle: a data-driven network, a statistical question asked of it, a short list of hypotheses, and experiments that test them. Applied to cancer more broadly ([7.9.13](/7.9.13)), the same logic links driver mutations to the master regulators that implement their effect.

## 11.8. Evaluation

### 11.8.1. Gold Standards and Metrics

An inferred network is evaluated against a gold standard of known interactions: RegulonDB for *E. coli*, binding plus perturbation data for yeast, and curated collections and ChIP-seq for human cells. Every gold standard is incomplete, so "false positives" include undiscovered true interactions, and measured precision is a lower bound. Simulated data with known networks (from models of transcriptional dynamics with noise) avoid this problem but test only the processes that the simulator contains.

Because regulatory networks are sparse, the evaluation uses the **precision–recall curve** rather than the **ROC curve**: a false-positive rate that looks small in ROC space corresponds to many false positives when true edges are rare.

**Example 11.8.1** Among $3.2 \times 10^7$ candidate factor–gene pairs with $10^5$ true arcs, a method that recovers $30\,\%$ of the true arcs at a false-positive rate of $0.1\,\%$ reports $30\,000$ true and $0.001 \times 3.19 \times 10^7 = 31\,900$ false arcs: a precision of $0.48$. In ROC terms the same method sits at the excellent point (FPR $0.001$, TPR $0.3$), close to the vertical axis. Its **area under the curve** can be high while half of its predictions are wrong.

![Network-inference methods compared on a simulated network: 10 transcription factors, with four edges among them, regulate 50 targets with one to three activating or repressing saturating inputs; n = 200 samples. Each method ranks the 590 candidate edges from a factor to another gene, of which 118 are true. A: precision-recall curves. B: average precision (area under the precision-recall curve); dashed: a random ranking (precision 0.2). Methods: absolute Pearson correlation; absolute partial correlation given all other genes; k-nearest-neighbor mutual information after ARACNe pruning (pruned edges ranked after kept ones); CLR; GENIE3-style random-forest importance; and the community ranking, the mean of the five ranks](./plots/grn_pr.py)

In this simulation the average precisions are $0.69$ for correlation, $0.86$ for partial correlation, $0.70$ for ARACNe, $0.65$ for CLR, $0.75$ for random-forest importance, and $0.81$ for the community ranking, against $0.20$ for a random ranking. ARACNe keeps $60$ of the $590$ candidate edges, $49$ of them true (precision $0.82$ at recall $0.42$). The ranking of methods reflects the simulator: with mostly additive, monotone responses and more samples than genes, partial correlation is close to the right model; nonlinear or combinatorial regulation favors tree ensembles and mutual information. No single method is best on every network, which is the lesson of the community challenges.

### 11.8.2. Community Challenges and the Wisdom of Crowds

The DREAM challenges (Dialogue on Reverse Engineering Assessment and Methods) distributed expression data from networks unknown to the participants and scored the submitted predictions against withheld gold standards. In DREAM5, more than $30$ methods were assessed on simulated data and on compendia of microarrays of *E. coli*, *Staphylococcus aureus* and *Saccharomyces cerevisiae* (Marbach and colleagues, 2012). Methods of each family (regression, mutual information, correlation, Bayesian networks) did well on some networks and poorly on others, and performance on the eukaryote, yeast, was much lower than on the bacteria. The integration of all predictions into a community network, by averaging the ranks each method gave an edge, was as good as the best individual method on every data set and more robust than any of them; this is the "wisdom of crowds" effect, an instance of the variance reduction by averaging that makes **ensemble learning** work. The community network of *E. coli* yielded new interactions that were confirmed experimentally.

For single-cell data, systematic benchmarks have been more sobering: on experimental single-cell data sets, most methods recovered ChIP-seq-supported networks only modestly better than random, and better on synthetic data than on real data (Pratapa and colleagues, 2020). Dropouts, the confounding of regulation with cell identity, and the absence of perturbations all contribute. The practical consequences are those of this chapter: combine expression with binding and motif evidence, prefer methods whose assumptions match the question, report the evaluation against an appropriate baseline, and treat any inferred network as a ranked list of hypotheses.

The following code implements the three building blocks of Sections 11.4–11.5 on an expression matrix `X` (samples by genes).

```python
import numpy as np
from itertools import combinations
from sklearn.ensemble import RandomForestRegressor

def mi_binned(x, y, bins=10):
    """Plug-in mutual information (nats) with equal-frequency bins."""
    qx = np.searchsorted(np.quantile(x, np.linspace(0, 1, bins + 1)[1:-1]), x)
    qy = np.searchsorted(np.quantile(y, np.linspace(0, 1, bins + 1)[1:-1]), y)
    pxy = np.zeros((bins, bins))
    np.add.at(pxy, (qx, qy), 1)
    pxy /= pxy.sum()
    px, py = pxy.sum(1, keepdims=True), pxy.sum(0, keepdims=True)
    nz = pxy > 0
    return float((pxy[nz] * np.log(pxy[nz] / (px @ py)[nz])).sum())

def mi_matrix(X, bins=10):
    p = X.shape[1]
    M = np.zeros((p, p))
    for i, j in combinations(range(p), 2):
        M[i, j] = M[j, i] = mi_binned(X[:, i], X[:, j], bins)
    return M

def aracne_dpi(M, threshold, eps=0.0):
    """Keep pairs above the threshold, then drop the weakest edge of each triangle."""
    A = M > threshold
    np.fill_diagonal(A, False)
    keep = A.copy()
    p = M.shape[0]
    for i, j, k in combinations(range(p), 3):
        if A[i, j] and A[i, k] and A[j, k]:
            e = sorted([(M[i, j], (i, j)), (M[i, k], (i, k)), (M[j, k], (j, k))])
            if e[0][0] < (1 - eps) * e[1][0]:
                a, b = e[0][1]
                keep[a, b] = keep[b, a] = False
    return keep

def genie3(X, tf_idx, n_trees=500):
    """Importance W[i, j] of factor i for gene j (random forests, one per gene)."""
    p = X.shape[1]
    W = np.zeros((p, p))
    for j in range(p):
        regs = [i for i in tf_idx if i != j]
        rf = RandomForestRegressor(n_estimators=n_trees, max_features="sqrt", n_jobs=-1)
        rf.fit(X[:, regs], X[:, j])
        W[regs, j] = rf.feature_importances_
    return W
```

## Summary

| Approach | Evidence | Output | Main assumption | Main failure | Section |
|---|---|---|---|---|---|
| Binding maps | ChIP-seq, one-hybrid, footprints (Algorithm 11.2.1) | factor → gene, directed | occupancy implies regulation; nearby gene is the target | inert sites; distal targets; factors without motifs | 11.2 |
| Co-expression | correlation (Definition 11.3.1) | undirected, weighted | co-regulated genes covary | indirect edges; composition effects | 11.3.1 |
| Gaussian graphical model | partial correlation (Formula 11.3.1), graphical lasso (Formula 11.3.2) | undirected, conditional | linear Gaussian; sparsity | nonlinearity; $n \ll p$ | 11.3.2 |
| WGCNA | soft-thresholded adjacency, topological overlap (Definition 11.3.2) | modules, eigengenes, hubs (Algorithm 11.3.1) | modules are co-regulated units | weak tuning rule; cell-type composition | 11.3.3 |
| Information | mutual information (Formula 11.4.1), DPI (Theorem 11.4.1) | undirected, pruned (Algorithm 11.4.1); CLR (Formula 11.4.2) | indirect pairs are the weakest of triangles | removes feed-forward loops; estimation bias | 11.4 |
| Three-way | conditional MI (Definition 11.4.1) | modulators (Algorithm 11.4.2) | many samples with wide ranges | sample size | 11.4.5 |
| Regression | lasso, random forests (Algorithm 11.5.1) | factor → gene, ranked | each gene has few regulators | correlated regulators share credit | 11.5 |
| Causal | Bayesian networks (Definition 11.6.1), perturbations (Formula 11.6.1) | directed | acyclicity or linear steady state; no hidden confounders | Markov equivalence (Theorem 11.6.1); noise amplification | 11.6 |
| Activity | regulons (Definition 11.7.1), SCENIC (Algorithm 11.7.1) | factor activity per sample or cell | targets report activity | missing or wrong regulons | 11.7 |

- The problem is underdetermined: about $1600$ factors and $20\,000$ genes give $3.2 \times 10^7$ candidate arcs; sparsity, the decomposition into per-gene problems and prior knowledge make it tractable (11.1).
- Footprint networks of $475$ factors in $41$ cell types are cell-type specific, with about $5\,\%$ of arcs shared by all, far more than chance (Example 11.2.1); related cell types share core networks and all are enriched in feed-forward loops (11.2).
- Conditioning removes indirect edges: partial correlation (Example 11.3.1) and the data processing inequality (Example 11.4.1); the latter also removes the weakest edge of true feed-forward loops (11.4.3).
- Mutual information detects non-monotone dependence (the figure of 11.4.1) but must be estimated with care; plug-in estimates of independent genes are biased upward (11.4.2).
- Perturbations break Markov equivalence and, in the linear regime, give direct effects from total effects by inverting the response matrix (Formula 11.6.1, Example 11.6.1).
- Regulon activity measures what the factor's mRNA does not (Definition 11.7.1); master regulator analysis with shadow and synergy tests (Algorithm 11.7.2) identified C/EBPβ and STAT3 as initiators of the mesenchymal glioblastoma program.
- Inferred networks are evaluated by precision and recall (Example 11.8.1); no method wins everywhere, and the community ranking is the most robust (11.8).

## Questions

1. A ChIP-seq experiment finds a factor bound within $5$ kb of $3000$ genes, and knockdown of the factor changes the expression of $800$ genes, of which $250$ are among the bound ones. Which genes would you call direct targets, and what explains the other two groups?

   **Answer** The $250$ bound and responsive genes are the best candidates for direct targets: binding and a functional effect together. The $2750$ bound but unresponsive genes may have inert or redundant sites (other factors compensate), sites that act on more distant genes, or regulation that requires a condition not present in the experiment. The $550$ responsive but unbound genes are likely indirect targets, regulated through other factors downstream, or direct targets bound at distal enhancers beyond the $5$ kb window, which chromatin-conformation data ([7.9.8](/7.9.8#sec-8.6)) could reveal. Under independence, $3000 \times 800/20\,000 = 120$ genes would be both bound and responsive, so the overlap of $250$ is about twice the chance level, typical of such studies.

2. Two cell-type footprint networks among $475$ factors have $12\,000$ and $10\,000$ arcs and share $2000$. Compute the expected overlap under independent random placement and the fold enrichment. What null model would be more appropriate?

   **Answer** Possible arcs (with self-arcs): $475^2 = 225\,625$. Expected overlap $12\,000 \times 10\,000/225\,625 = 532$; fold enrichment $2000/532 = 3.8$ (a hypergeometric test gives an extremely small p-value). Uniform placement is too lenient: factors with many well-defined motifs and genes with large accessible promoters have arcs in many cell types for technical reasons. A better null preserves the in- and out-degrees of each factor in each network (**degree-preserving randomization**, [1.4.7](/1.4.7#sec-7.4.6)), which asks whether the specific arcs are shared beyond what the degrees imply.

3. In a linear Gaussian chain $X \to Y \to Z$ with $\operatorname{Corr}(X, Y) = 0.9$ and $\operatorname{Corr}(Y, Z) = 0.6$, compute $\operatorname{Corr}(X, Z)$, the partial correlation of $X$ and $Z$ given $Y$, and the three mutual informations. Which edge does ARACNe remove? What if the true network were the feed-forward loop $X \to Y \to Z$, $X \to Z$ with a weak direct arc?

   **Answer** $\operatorname{Corr}(X, Z) = 0.9 \times 0.6 = 0.54$; the partial correlation is $(0.54 - 0.54)/\sqrt{(1 - 0.81)(1 - 0.36)} = 0$. By Formula 11.4.1, $I(X; Y) = -\tfrac12\ln 0.19 = 0.830$, $I(Y; Z) = -\tfrac12\ln 0.64 = 0.223$, $I(X; Z) = -\tfrac12\ln(1 - 0.2916) = 0.172$ nats. The smallest is $X$–$Z$, which is removed, correctly. In the feed-forward loop the direct arc adds to the correlation of $X$ and $Z$, but if it is weak, $I(X; Z)$ may still be the smallest of the triangle and the true arc is removed; the partial correlation would be nonzero and would detect it, given enough samples. A tolerance $\varepsilon$ keeps the arc only if $I(X; Z)$ is within $\varepsilon$ of $I(Y; Z)$.

4. Compute the topological overlap of genes $i$ and $j$ with $a_{ij} = 0.5$ that share a single neighbor $u$ with $a_{iu} = a_{ju} = 0.9$ and have no other connections. Compare with the value without the shared neighbor, and explain why WGCNA clusters on the topological overlap rather than on the adjacency.

   **Answer** $l_{ij} = 0.81$, $k_i = k_j = 1.4$, $\mathrm{TOM}_{ij} = (0.81 + 0.5)/(1.4 + 1 - 0.5) = 0.69$. Without the neighbor, $k_i = k_j = 0.5$ and $\mathrm{TOM}_{ij} = 0.5/(0.5 + 1 - 0.5) = 0.5$. The topological overlap rewards shared neighborhoods, so it is less sensitive to noise in a single correlation: two genes in the same module are similar to many of the same genes even when their own correlation is attenuated by noise, and two unrelated genes with a spuriously high correlation share few neighbors. Clustering on $1 - \mathrm{TOM}$ therefore gives more stable modules.

5. Two genes measured in $n = 50$ samples are discretized into $8$ equal-frequency bins each. What plug-in mutual information do you expect if they are independent, and how would you set a significance threshold for a network of $10\,000$ genes?

   **Answer** The first-order Miller–Madow bias for independent variables is $(m_{xy} - m_x - m_y + 1)/(2n) = (64 - 8 - 8 + 1)/100 = 0.49$ nats (about $0.71$ bits), and simulations with $n = 100$, $m = 10$ show that the true bias is larger still at small $n$. A fixed threshold near zero would call almost every pair significant. Instead, compute the mutual information of many pairs with the samples of one gene permuted, which preserves the marginal distributions and the bias, and set the threshold at the quantile corresponding to the desired per-pair p-value, corrected for the about $5 \times 10^7$ pairs (for example a false discovery rate). Using fewer bins, a $k$-nearest-neighbor estimator, or more samples reduces the bias itself.

6. Which of the following directed acyclic graphs on three genes are Markov equivalent: (a) $X \to Y \to Z$; (b) $X \leftarrow Y \to Z$; (c) $X \to Y \leftarrow Z$; (d) $X \leftarrow Y \leftarrow Z$? Design a single knockout that distinguishes the graphs in the equivalence class.

   **Answer** (a), (b) and (d) have the same skeleton and no v-structure; they are equivalent (Theorem 11.6.1) and all imply only $X \perp Z \mid Y$. (c) has the v-structure $X \to Y \leftarrow Z$: $X \perp Z$ marginally but not given $Y$; it is in a class of its own. Knocking out $Y$ distinguishes the three: in (a) $Z$ changes and $X$ does not; in (b) both $X$ and $Z$ change; in (d) $X$ changes and $Z$ does not. Alternatively, knocking out $X$ changes $Y$ and $Z$ only in (a).

7. For two genes, perturbing gene $1$ changes the steady state by $(1, 0.5)$ and perturbing gene $2$ by $(0.2, 1)$ (columns of $R$). Compute the local response coefficients by Formula 11.6.1 and interpret them.

   **Answer** $R = \begin{bmatrix} 1 & 0.2 \\ 0.5 & 1\end{bmatrix}$, $\det R = 0.9$, $R^{-1} = \frac{1}{0.9}\begin{bmatrix} 1 & -0.2 \\ -0.5 & 1\end{bmatrix}$. Then $r_{12} = -(R^{-1})_{12}/(R^{-1})_{11} = 0.2$ and $r_{21} = -(R^{-1})_{21}/(R^{-1})_{22} = 0.5$. Gene $1$ activates gene $2$ with local strength $0.5$ and gene $2$ feeds back on gene $1$ with strength $0.2$: a positive feedback loop. The loop gain is $0.5 \times 0.2 = 0.1$, so the feedback amplifies every total response by $1/(1 - 0.1) = 1.11$ relative to the open loop.

8. A genome-wide inference method is evaluated on $1600 \times 20\,000$ candidate pairs with $10^5$ true arcs and reaches a true-positive rate of $0.3$ at a false-positive rate of $0.001$. Compute the precision. How would the precision change if the method were restricted, by motif evidence, to $5 \times 10^6$ candidate pairs containing $8 \times 10^4$ of the true arcs, with the same rates?

   **Answer** Candidates: $3.2 \times 10^7$, of which $3.19 \times 10^7$ are false. True positives $0.3 \times 10^5 = 30\,000$, false positives $0.001 \times 3.19 \times 10^7 = 31\,900$, precision $0.48$ (Example 11.8.1). After the filter: true positives $0.3 \times 8 \times 10^4 = 24\,000$, false positives $0.001 \times 4.92 \times 10^6 = 4920$, precision $0.83$. The prior loses $20\,\%$ of the true arcs (those without motif evidence) but removes most of the candidates, which raises the precision; this is the trade-off of a filter (11.5.3).

9. Explain why the mRNA of a transcription factor is often a poor indicator of its activity, and what a shadow analysis would conclude if the unique targets of factor 1 are not enriched in a signature while its targets shared with factor 2 are strongly enriched.

   **Answer** Activity depends on post-translational modification, ligand binding, localization, cofactors and degradation (for example STAT3 requires tyrosine phosphorylation, nuclear receptors their ligands); the mRNA level may not change when activity does (the figure in 11.7.1), and may even change in the opposite direction through feedback. The targets integrate all these effects. In the shadow analysis, if only the shared targets are enriched, the apparent activity of factor 1 is explained by factor 2: factor 1 is a shadow regulator, not a master regulator, and would not be prioritized for validation unless other evidence supports it.

10. (Open problem) You have single-cell RNA-seq and single-cell ATAC-seq of a differentiating tissue and want to identify the factors that drive one fate. Outline an analysis and the experiments that would test its predictions.

    **Answer** One route: (i) annotate cell states and the trajectory toward the fate ([7.9.7](/7.9.7)); (ii) infer regulons by combining co-expression (GRNBoost2) with motifs in accessible elements linked to genes by peak–gene correlation, as in SCENIC+ or CellOracle, so that each factor's targets are supported by both expression and chromatin; (iii) score regulon activity per cell (AUCell, decoupler) and find factors whose activity rises along the trajectory before the fate genes, with pseudobulk tests across replicate samples to avoid pseudoreplication; (iv) apply a master regulator analysis to the fate against its sister fate, with shadow analysis to remove redundant factors; (v) simulate knockouts in the inferred network to predict which factors shift the trajectory. Tests: CRISPR knockout or CRISPRi of the top candidates in a pooled Perturb-seq experiment in the differentiating system, reading the fate distribution and target expression; overexpression or CRISPR activation for sufficiency; and ChIP-seq or CUT&RUN of the factors to confirm direct binding at the predicted targets. Predictions that fail in this test are informative about the limits of the inferred network.
