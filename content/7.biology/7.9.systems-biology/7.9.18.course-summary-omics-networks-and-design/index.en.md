---
title: "Course Summary: Omics, Networks and Design Principles"
description: "A synthesis of the systems biology course: its three layers (measuring parts and states, connecting them into networks, explaining behavior by dynamics); the omics methods compared by measured object, data unit, statistical model, tools and the network edges they supply; the statistical structures that recur (counts with two levels of variation, mixtures and EM, null models and multiple testing, set statistics on rankings, embeddings and neighbor graphs, optimal transport and matrix scaling, hidden Markov models and Markov random fields, information theory); the network ideas that recur (the meaning of an edge, randomized null models, random walks, modules, motifs and the sign of feedback); dynamics and identifiability; an index of models; orders of magnitude of the data; a timeline of methods; and open problems."
---

The seventeen chapters of this course have followed one program from the measurement of molecules to the explanation of behavior. This chapter collects what they built without adding new results. It lays the methods side by side, points out the few mathematical structures that return under different names in different omics layers, indexes the models with their equations, gathers the orders of magnitude of the data, places the methods in time, and ends with the questions the field has not answered. Every equation and number is taken from the chapter that develops it, and the references (Theorem 11.4.1, Eq. (6.8), Example 2.2.1) lead back to the derivations and their assumptions. The structure follows the summary of the biophysics course ([7.6.42](/7.6.42)), whose quantitative-biology chapters are the physical foundation of the dynamical half of this one.

## 18.1. The Organization of the Course

### 18.1.1. Measure, Connect, Explain

**Systems biology** was defined in Definition 1.1.1 as the study of biological systems through the measurement, analysis and modeling of the interactions among many components, and the three tasks of the field as reconstruction, interrogation and application of networks (7.9.1, Section 1.5.2). The course is organized in three layers that correspond to these tasks.

| Layer | Chapters | Question | Typical output |
|---|---|---|---|
| Measure: parts and states | 7.9.2–7.9.9 | which molecules, in which cells and places, how many | count matrices, ratios, peaks, intensities; lists of changed features |
| Connect: wiring | 7.9.10–7.9.13 | which molecules interact, regulate or depend on each other | interaction, regulatory and co-expression networks; modules; candidate drivers and drugs |
| Explain: behavior | 7.9.14–7.9.17 | what a network does in time, and why it is built this way | rate equations, steady states and bifurcations, motif functions, noise and robustness, designs |

Chapter 7.9.1 sets out the questions, the omics layers and the distinction between a **forward model**, which computes behavior from structure and parameters, and an **inverse model**, which infers structure or parameters from data (Definition 1.5.1). The first layer is almost entirely inverse modeling of a simple kind: estimating abundances and their differences from counts. The second is inverse modeling of a hard kind: inferring a graph. The third combines forward models (what a motif computes) with inverse problems (fitting rate constants, and asking what the data have determined). The map below shows the chapters and the main lines along which they use each other.

![The course as a map. Chapters 7.9.2–7.9.9 measure parts and states: bulk transcriptomics, whose count model is reused for gene sets, RNA processing and single cells; single cells extended to space and to trajectories; the epigenome and three-dimensional genome; proteins and metabolites. Chapters 7.9.10–7.9.13 connect them: measured interactomes and inferred regulatory networks are analyzed in 7.9.12 and applied to cancer in 7.9.13. Chapters 7.9.14–7.9.17 explain behavior: kinetic models, transcription motifs, feedback and oscillation, noise, robustness, evolution and synthetic design. Thick arrows: data become edges, edges get rates. Right: the earlier courses each layer draws on (dashed)](./plots/course_map.py)

The direction of the arrows is the order of reading, but the dependence also runs backward. Network motifs (7.9.15) were discovered in a transcription network assembled from binding experiments of the kind treated in 7.9.8 and 7.9.11; the kinetic models of 7.9.14 are what modular response analysis (Formula 11.6.1) assumes when it reads direct effects from perturbation data; and the noise of 7.9.17 is the biological variation that the count models of 7.9.2 and 7.9.5 have to absorb. The single-cell chapters make the circle visible: the negative binomial distribution of UMI counts (Formula 5.4.1) is the distribution produced by bursty expression ([Theorem 32.4.1](/7.6.32#thm-32.4.1)), and the attractors of a regulatory network ([7.9.7](/7.9.7#sec-7.1)) are what clustering of a snapshot calls cell types.

### 18.1.2. Systems That Recur

A few data sets and systems were followed through several chapters, so that the same object was seen through different methods.

| System or data set | What it showed | Where |
|---|---|---|
| Airway smooth muscle with dexamethasone (Himes and colleagues, 2014): 4 donors × 2 conditions | paired design, 4691 genes at FDR 0.1 (3422 ignoring donors); glucocorticoid response and TNF-α signaling in gene sets | [7.9.2](/7.9.2#sec-2.7.2), Example 3.2.2, Example 3.3.1 |
| The *E. coli* transcription network (424 operons, 519 arcs) | sparse, long-tailed out-degree; negative autoregulation and the FFL as motifs | Example 15.2.1, [7.9.12](/7.9.12#sec-12.1.2), [7.9.1](/7.9.1#sec-1.5.1) |
| Yeast interactome and genetic-interaction map (about $9\times10^5$ interactions) | hubs and essentiality, functional modules from profile similarity | [7.9.10](/7.9.10#sec-10.6.2), [7.9.12](/7.9.12#sec-12.2) |
| Footprint networks of 475 factors in 41 cell types | cell-type-specific wiring with a shared core | Example 11.2.1 |
| Tumor consortia and dependency maps | drivers, signatures, subtypes, synthetic lethality | 7.9.13 |
| Simulated data with known truth | doublets, clusters, pseudobulk, deconvolution, segmentation, motifs, propagation | almost every chapter |

The last row is not an afterthought. Because the truth of a biological network is unknown, most of the quantitative statements of the course about the behavior of methods (false positive rates of cell-level tests, recovery of planted modules, the effect of a misspecified background) came from simulations whose generating model was known, and the conclusion of each was checked against the real data where they exist.

## 18.2. Omics Methods Compared

Each omics layer has its own chemistry, but the analyses share a design: a molecular property is converted into countable events (reads, molecules, spectra, fluorescent spots), the counts are compared with a background that carries the same biases, and the result is a list of features or a set of edges. The table compares the layers along the axes that decide the analysis.

| Layer (chapter) | Measured object | Data unit | Statistical model | Typical tools | Edges it supplies |
|---|---|---|---|---|---|
| Bulk transcriptome (7.9.2) | RNA fragments of a population | read counts per gene | negative binomial GLM with shrunken dispersion; BH ([7.7.20](/7.7.20)) | salmon, STAR, DESeq2, edgeR, limma | co-expression (7.9.11) |
| Gene sets (7.9.3) | annotations of genes | membership, rankings | hypergeometric tail, Eq. (3.1); running sum, Eq. (3.2); permutation | clusterProfiler, fgsea, GSVA | gene–process links |
| RNA processing, translation (7.9.4) | junctions, footprints, conversions, crosslinks | counts within one gene or site | binomial ratios with replicate variation (Algorithm 4.1.1); NB interaction (Formula 4.4.1); binomial mixture (Formula 4.5.1) | rMATS, RiboCode, GRAND-SLAM, eCLIP pipelines | RNA–protein binding |
| Single cells (7.9.5) | molecules of each cell | UMI counts per cell and gene | negative binomial (Formula 5.4.1); Pearson residuals (Formula 5.4.2); scVI (Formula 5.8.1) | Cell Ranger, scanpy, scvi-tools | regulons (Algorithm 11.7.1) |
| Space (7.9.6) | molecules at positions | counts per spot, cell or pixel; images | Poisson mixtures (Eq. (6.7)); Gaussian processes (Eq. (6.3)); Potts prior (Eq. (6.5)) | squidpy, SpatialData, Cellpose | neighbor graphs, niches, communication |
| States and fates (7.9.7) | snapshots, spliced and unspliced counts, barcodes | cells on a graph | diffusion distances (Formula 7.2.1); splicing ODE (Formula 7.3.1); absorbing Markov chain (Formula 7.3.3) | scVelo, CellRank, CellChat | ligand–receptor, factor–fate |
| Epigenome, 3D genome (7.9.8) | DNA fragments from chromatin | reads in bins and peaks; methylated fractions; contacts | local Poisson (Algorithm 8.2.1); beta-binomial (Formula 8.5.1); multivariate HMM (Formula 8.4.1); matrix balancing (Algorithm 8.6.1) | MACS, ChromHMM, cooler | factor–element, element–gene (Formula 8.7.1) |
| Proteome, metabolome (7.9.9) | ions of peptides and metabolites | spectra, intensities | target–decoy FDR (Formula 9.4.2); censored normal (Formula 9.5.2); isotope correction (Formula 9.8.1) | MaxQuant, DIA-NN, XCMS | kinase–substrate, fluxes |
| Interactome, screens (7.9.10) | binary pairs, complexes, double mutants, guides | spectral counts, colony sizes, guide counts | Poisson background (Example 10.3.1); evidence combination (Eq. (10.1)); NB guide test (Formula 10.7.1) | SAINT, STRING, MAGeCK | physical, functional, genetic edges |

Two common features stand out. First, the precision of almost every quantity is set by a small number of informative events, not by the total depth: the junction reads of one exon (Example 4.1.1), the reads of one CpG (Example 8.5.1), the guides of one gene (Example 10.7.2), the spectra of one protein. Second, every layer needs a background that shares the biases of the signal: input DNA for ChIP-seq, decoys for peptides, the tested genes for an enrichment, controls for affinity purification. Sections 18.3.1 and 18.3.3 return to both.

## 18.3. Recurring Statistical Structures

A small number of statistical structures carry most of the measurement and network chapters. The table lists them with a core equation and the chapters that use them; the figure shows the same information as a matrix, and the subsections show how each reappears.

| Structure | Core object | Appears in (7.9.n) |
|---|---|---|
| Counts with two levels of variation | $\operatorname{Var} = \mu + \phi\mu^2$; binomial and beta-binomial ratios | 2, 4, 5, 8, 9, 10, 13 |
| Latent variables and EM | mixtures of known components with unknown weights | 2, 4, 5, 6, 8 |
| Null models and multiple testing | BH, q-values, decoys, permutations, randomized networks | 1, 2, 3, 6, 8, 9, 10, 12, 13, 15 |
| Set statistics on rankings | hypergeometric tail, running sums, activity scores | 3, 7, 9, 11, 12 |
| Embeddings and neighbor graphs | PCA, NMF, kNN graphs, communities, diffusion maps | 2, 5, 6, 7, 8, 10, 11, 12, 13 |
| Optimal transport and matrix scaling | $\min\sum C_{ij}P_{ij}$ with fixed marginals; Sinkhorn iteration | 6, 7, 8 |
| Hidden Markov models and Markov random fields | hidden states coupled along a sequence or a graph | 6, 8 |
| Information theory | mutual information, entropy, codes | 6, 11, 16, 17 |

![Recurring mathematical structures (columns) in the chapters of the course (rows). A dot marks a chapter that develops the structure in a numbered statement or uses it in a worked analysis. Measurement chapters share count models, mixtures and multiple testing; network chapters share randomized nulls, neighbor graphs and random walks; the dynamical chapters share ordinary differential equations, noise and identifiability, and information theory links them to the measurement of networks](./plots/structures.py)

### 18.3.1. Counts with Two Levels of Variation

Nearly every omics measurement is a count, and nearly every count has two sources of variation: sampling, which is Poisson or binomial given the true abundance, and biological variation of the abundance between replicates. Integrating a Poisson count over a gamma-distributed rate gives the **negative binomial distribution** with $\operatorname{Var} = \mu + \phi\mu^2$; integrating a binomial over a beta-distributed fraction gives the **beta-binomial distribution**. The course used the pair everywhere.

| Quantity | Sampling level | Biological level | Where |
|---|---|---|---|
| Reads of a gene in a library | Poisson | gamma: NB with dispersion $\phi$ | Example 2.2.1, [7.7.20](/7.7.20) |
| UMIs of a gene in a cell | Poisson | gamma across cells of a type: NB with shape $\theta$ | Formula 5.4.1 |
| Inclusion reads of an exon | binomial in $I + S$ | logit-normal between replicates | Formula 4.1.1, Algorithm 4.1.1 |
| Footprints relative to mRNA | NB per assay | interaction term | Formula 4.4.1 |
| Methylated reads of a CpG | binomial | beta | Formula 8.5.1 |
| Reads of a guide | NB with mean–variance fit | — | Formula 10.7.1 |
| Mutations of a gene in tumors | Poisson with background rate | gamma between genes | Formula 13.4.1, Example 13.4.2 |

The consequence that the chapters drew again and again is that sequencing depth reduces only the sampling part. For a log fold change between two groups of $n$ libraries the variance is $(1/\mu_A + 1/\mu_B + 2\phi)/n$; at infinite depth it is $2\phi/n$, and only more **biological replicates** reduce it (Definition 2.2.1, Example 2.2.1: a fixed budget spent on $6 + 6$ libraries gives power $0.54$ against $0.34$ for $3 + 3$). The same law reappears as "replicates, not reads" for methylation (Example 8.5.1), as the replicate model of differential splicing (Example 4.1.2), and in its most dangerous form in single cells, where treating cells as replicates gives significance to $54\,\%$ of null genes (Example 5.6.1); the **pseudobulk** profile (Definition 5.6.1) restores the donor as the unit of replication. In cancer genomics the same structure appears between genes rather than between samples: a background mutation rate that ignores the gamma-distributed variation between genes produced $277$ false drivers in a simulation, against $20$ when overdispersion and covariates were modeled (Example 13.4.2).

![One count model for the whole course. A: squared coefficient of variation of a count, CV² = 1/μ + φ, for Poisson sampling alone and for negative binomial counts with the dispersions of the chapters, φ = 0.05 for bulk replicates (Example 2.2.1) and φ = 0.1 for UMI counts (θ = 10, Example 5.4.1): the sampling part falls with depth, the biological part is a floor (dotted). B: standard error of a log fold change for n = 3 and n = 6 replicates per group with φ = 0.05, against the depth of group A (group B twofold higher); dots mark the two designs of one budget of 120 million reads in Example 2.2.1, dotted lines the floors √(2φ/n)](./plots/counts.py)

The zeros of single-cell data are an instance of the same model. A gene of mean $0.5$ is zero in $61$ to $64\,\%$ of cells because $\mathrm{e}^{-0.5} = 0.61$ and $(1 + 0.5/2)^{-2} = 0.64$ ([7.9.5](/7.9.5#sec-5.4.1)); excess zeros signal heterogeneity of cell types, not a separate technical process, at least for UMI data.

### 18.3.2. Latent Variables, Mixtures and EM

Many measurements are mixtures of contributions from components that are known in form but unknown in proportion, and the **EM algorithm** estimates the proportions by alternating the assignment of observations to components with the re-estimation of the weights.

| Observation | Components | Weights estimated | Where |
|---|---|---|---|
| A read compatible with several transcripts | transcripts of a gene | transcript abundances | Eq. (2.1), Algorithm 2.3.1 |
| A read with T-to-C conversions | new and old RNA | new fraction $\theta$, hence half-life | Formula 4.5.1, Example 4.5.1 |
| The counts of a spot | reference cell types | cell-type proportions | Eq. (6.7), Algorithm 6.12.1 |
| A bulk profile | signature matrix | proportions (by nonnegative least squares) | Formula 5.7.1 |
| Pairs of peak ranks in two replicates | reproducible and irreproducible signal | local irreproducible discovery rate | Definition 8.2.3 |
| A cell's counts | latent state $\boldsymbol{z}_n$ | decoder of a generative model (variational inference) | Formula 5.8.1 |

The common lessons are those of mixture models in general. The likelihood can be flat in directions where components are similar (two isoforms differing only in a short exon, two cell types with similar profiles), so the estimate is precise only when the observations discriminate between components; and the model inherits the errors of its components, which is why deconvolution with references from another platform is biased in a way that depth does not remove ([7.9.6](/7.9.6#sec-6.12.1)). Factorizations in which both the components and the weights are learned, NMF of mutational catalogs (Definition 13.3.2, Algorithm 13.3.1) and the gene programs of single cells, are the unsupervised end of the same idea.

### 18.3.3. Null Models and Multiple Testing

Data-driven discovery in wide data needs a null model. With $8$ samples and $20\,000$ unrelated genes, about $340$ genes correlate with any phenotype beyond $\lvert r\rvert = 0.8$ by chance (Example 1.2.1). The course controlled such errors in two steps, both developed statistically in [7.7.20](/7.7.20): a p-value per feature from a null distribution, then a **false discovery rate** across features, usually by the **Benjamini–Hochberg procedure**. The interesting variation is in where the null distribution comes from.

| Null model | Construction | Where |
|---|---|---|
| Parametric | NB or Poisson tail given the background mean | Formula 10.7.1, Formula 13.4.1, Algorithm 8.2.1 |
| Control samples | input DNA, control purifications, non-targeting guides | Example 8.2.1, Example 10.3.1, [7.9.10](/7.9.10#sec-10.7.2) |
| Decoys | reversed or shuffled protein sequences | Definition 9.4.2, Formula 9.4.2 |
| Sample permutation | permute phenotype labels | [7.9.3](/7.9.3#sec-3.3.3) |
| Label permutation in space | permute cell labels over fixed positions | Proposition 6.10.1, Example 6.10.2 |
| Randomized networks | random digraphs, degree-preserving rewiring | Proposition 15.2.1, Algorithm 15.2.1 |
| Random gene sets of matched degree | sets drawn with the same degrees | Formula 12.6.2, Algorithm 12.4.1 |

The decoy approach is the clearest instance of the principle: a decoy match behaves like a wrong target match, so the number of decoys above a threshold estimates the number of false targets, and in a simulation of $20\,000$ spectra the estimate gave $6406$ accepted matches at an estimated $1\,\%$ FDR with a true false discovery proportion of $1.01\,\%$ (Example 9.4.3). The failures of the course were failures of the null. A background that does not share the selection biases inflates gene-set results ($79\,\%$ against $4.2\,\%$ false positives in the simulation of [7.9.3](/7.9.3#sec-3.2.2)); competitive gene-set tests that treat genes as independent are anticonservative under correlation ([7.9.3](/7.9.3#sec-3.3.3)); a test that uses the clusters it is testing returns small p-values for any data ([7.9.5](/7.9.5#sec-5.6.1)); and selecting genes or cutpoints on the data before evaluating them produces apparent classifiers and prognostic markers from noise (Example 13.6.1, Example 13.6.2). The rule that covers all of these is that every data-dependent choice belongs inside the null distribution, the permutation or the cross-validation.

### 18.3.4. Sets and Rankings

A second recurring structure turns a ranking of genes into a statement about a set of genes. **Over-representation analysis** asks whether a list contains more members of a set than a random subset would, a hypergeometric tail (Definition 3.2.1); **gene set enrichment analysis** walks down the full ranking with a weighted running sum (Definition 3.3.1) and needs no threshold. The same construction appears with other sets and other rankings:

- the connectivity score of a drug compares the up- and down-regulated genes of a query with each reference ranking (Algorithm 7.7.1, Example 7.7.1);
- regulon activity scores a factor by the expression of its signed targets (Definition 11.7.1), and master regulator analysis tests regulons against a signature (Algorithm 11.7.2);
- kinase activities are inferred from the phosphosites of their substrates ([7.9.9](/7.9.9#sec-9.6.3)), motif accessibility from the peaks that contain a motif (Formula 8.3.2);
- the members of a network module are tested for a shared annotation against the network background (Example 12.3.2).

In every case the result is a statement about a process, a regulator or a drug inferred from many weak signals, and in every case the set definitions carry the biases of the annotations: well-studied genes have more terms, and a regulon inferred from the same data on which it is scored is circular ([7.9.3](/7.9.3#sec-3.5)).

### 18.3.5. Embeddings, Neighbor Graphs and Factorizations

High-dimensional profiles are analyzed in three steps that recur from bulk to spatial data: reduce the dimension, build a graph of neighbors, and partition or order the graph.

| Step | Method | Where |
|---|---|---|
| Reduce | **principal component analysis** of variance-stabilized counts; Pearson residuals | [7.9.2](/7.9.2#sec-2.6), Formula 5.4.2 |
| Reduce, nonnegatively | NMF of catalogs or programs | Definition 13.3.2 |
| Reduce, by a leading eigenvector | A/B compartments from the correlation matrix | Algorithm 8.6.2 |
| Connect | kNN graph of cells; spatial graphs of neighboring cells | [7.9.5](/7.9.5#sec-5.5.2), [7.9.6](/7.9.6#sec-6.10.1) |
| Connect, by co-variation | soft-thresholded co-expression, topological overlap | Algorithm 11.3.1, Definition 11.3.2 |
| Partition | Leiden communities with a resolution parameter | Algorithm 5.5.1, Example 5.5.1 |
| Order | diffusion pseudotime, principal curves | Formula 7.2.1 |
| Smooth on a known network | network-based stratification | Algorithm 13.5.1 |

The neighbor graph of cells is the place where the statistics of measurement meet network science. Clusters of cells are communities found by maximizing the modularity $Q$ ([Definition 7.7.3](/1.4.7#def-7.7.3)) with the **Leiden algorithm**, and the choice of resolution decides whether a subtype is merged with its parent or a type is split into meaningless pieces (Example 5.5.1: four, five or twelve clusters for the same data). Two-dimensional maps such as t-SNE and UMAP preserve neighborhoods, not distances ([7.9.5](/7.9.5#sec-5.5.4)), and the pseudotime of a cell orders states, not times (Definition 7.2.1).

### 18.3.6. Optimal Transport and Matrix Scaling

**Optimal transport** (Definition 6.12.2) moves one distribution onto another at minimum total cost, Eq. (6.8). In the course it maps dissociated cells to spatial positions (Tangram, novoSpaRc), aligns consecutive sections, through the fused Gromov–Wasserstein problem of Eq. (6.10), links cells between time points (Waddington-OT, [7.9.7](/7.9.7#sec-7.3.4)), links the masks of neighboring planes in three-dimensional segmentation, and distributes a ligand over receivers within range (COMMOT). Its entropic form has the solution $P = \operatorname{diag}(\boldsymbol{u})\,\mathrm{e}^{-C/\varepsilon}\operatorname{diag}(\boldsymbol{v})$, and $\boldsymbol{u}, \boldsymbol{v}$ are found by alternately rescaling rows and columns to the prescribed marginals (Example 6.12.1: exact cost $0.6$, entropic cost $0.81$ at $\varepsilon = 1$).

The same iteration balances Hi-C maps. Iterative correction assumes $O_{ij} = b_ib_jT_{ij}$ with equal coverage of every bin in $T$ (Algorithm 8.6.1) and rescales rows and columns until all sums are equal; the Sinkhorn–Knopp theorem guarantees convergence to a unique doubly stochastic matrix (Theorem 8.6.1). Two problems that look unrelated, the removal of bin biases from a contact matrix and the transport of cells to positions, are therefore one algorithm: find the diagonal scalings of a positive matrix that fix its row and column sums. The registration of images by the Kabsch algorithm (Theorem 6.13.1), the rigid special case of matching point sets, is solved by a singular value decomposition, as is the superposition of protein structures in [7.8.17](/7.8.17).

### 18.3.7. Hidden Markov Models and Markov Random Fields

When hidden labels are correlated along a sequence or over a graph, the model couples the observation of each site to its label and the labels of neighboring sites to each other. Along the genome, ChromHMM learns chromatin states as the hidden states of a **hidden Markov model** whose emissions are the binarized marks of each bin (Definition 8.4.1, Formula 8.4.1), with forward–backward and Viterbi computations as in [4.6.8](/4.6.8). Over the spot grid of a tissue section, spatial domains are smoothed by a Potts prior that rewards equal labels of neighbors, Eq. (6.5), sampled by Gibbs sampling, Eq. (6.6); its strength $\gamma$ decides whether an isolated spot with an unusual profile keeps its own label or is absorbed by its neighbors (Example 6.11.1). The same coupling of hidden labels along a sequence underlies the profile and gene-finding models of [7.8.5](/7.8.5) and [7.8.7](/7.8.7).

### 18.3.8. Information

Information theory entered the course at four places. Network inference uses **mutual information** as a measure of dependence that detects non-monotone relations (Formula 11.4.1), and the **data processing inequality** (Theorem 11.4.1) as the reason to remove the weakest edge of every triangle, which removes indirect edges and, unavoidably, the weakest edge of true feed-forward loops (Example 11.4.1, [7.9.11](/7.9.11#sec-11.4.3)). Conditional mutual information finds modulators of regulation (Definition 11.4.1, Algorithm 11.4.2). In imaging transcriptomics, codes with a minimum Hamming distance correct readout errors (Definition 6.3.1; in Example 6.3.2 a distance-4 code raises the yield of correctly decoded molecules from $40\,\%$ to $78\,\%$). In the dynamics of signaling, a pulsatile factor encodes its input in frequency and keeps the ratios of its targets fixed (Definition 16.5.1, Example 16.5.1), and the **channel capacity** of a signaling pathway bounds what a cell can learn ([Theorem 35.3.1](/7.6.35#thm-35.3.1)). Finally, the value of information has a price in growth: a bet-hedging population loses exactly the entropy of its environment relative to one that senses it (Theorem 17.1.2; $0.500$ nats per period at $p = 0.8$, Example 17.1.3).

## 18.4. Recurring Network Ideas

### 18.4.1. What an Edge Means

The most consequential decision in a network analysis is often made before it starts, when an edge is given a meaning. The course met edges of five kinds.

| Kind | Edge means | Sources | Where |
|---|---|---|---|
| Physical | two molecules bind, directly or in a complex | two-hybrid, AP-MS, proximity labeling | [7.9.10](/7.9.10#sec-10.2) |
| Regulatory, causal | a factor changes the transcription of a gene | binding plus perturbation | Definition 11.1.1, Definition 15.1.1 |
| Functional | two genes act in one process | genomic context, phylogenetic profiles, text | Definition 10.4.1, Eq. (10.1) |
| Genetic | the double perturbation deviates from the singles | double mutants, combinatorial screens | Definition 10.6.1 |
| Statistical | expression covaries, conditionally or not | correlation, partial correlation, mutual information | Definition 11.3.1, Formula 11.3.1 |

A co-expression edge may mean regulation, common regulation or a shared cell type whose proportion varies; a genetic edge may join proteins that never touch, as in **synthetic lethality**; and a physical edge records an interaction that is possible, not one that occurs in every cell. The maps are also samples: each screen detects a fraction of the true interactions, and capture–recapture estimates of interactome size (Eq. (10.2)) are lower bounds when detectability varies. Topological conclusions are therefore conclusions about the map, and the robustness of a simulated interaction network measured on a $40\,\%$ sample changed from $84\,\%$ to $73\,\%$ under random removal and from $16\,\%$ to $6.5\,\%$ under attack ([7.9.12](/7.9.12#sec-12.1.3)).

### 18.4.2. Randomized Networks as Null Models

Whether a network property is remarkable depends on what a random network with the same basic statistics would show. The course used three ensembles in increasing order of realism.

1. The random digraph with the same number of vertices and arcs: in the *E. coli* network, $\lambda = A/N = 1.22$, so $\lambda$ self-arcs, $\lambda^3$ feed-forward loops and $\lambda^3/3$ three-cycles are expected (Proposition 15.2.1), against $40$ self-arcs, $42$ FFLs and no cycle observed (Example 15.2.1).
2. The **configuration model** and **degree-preserving randomization** ([Algorithm 7.4.2](/1.4.7#alg-7.4.2)), which keep every vertex's degree and remove the trivial explanation of motifs by hubs (Algorithm 15.2.1, Example 15.2.2).
3. Random sets of vertices with matched degrees, for disease modules and drug–disease proximity (Formula 12.6.2), and random subgraphs of the same size for active subnetworks (Algorithm 12.4.1).

The same idea, with networks replaced by sets of arcs, measured the overlap of cell-type-specific regulatory networks: two independent networks with the observed density would share only about $5\,\%$ of their arcs, so the observed sharing is far beyond chance (Example 11.2.1). Each null removes one explanation; a property that survives the degree-preserving null may still be explained by the sampling of the map or by the biology that produced the degrees (Definition 17.4.2, duplication and divergence).

### 18.4.3. Propagation and Random Walks

Many integrative methods of the course are Markov chains on graphs, differing in what the states and the transitions mean.

| Method | States | Transition | Quantity computed | Where |
|---|---|---|---|---|
| **Network propagation** (random walk with restart) | genes | to a random neighbor, or back to the seeds with probability $r$ | $\boldsymbol{p} = r(I - (1 - r)W)^{-1}\boldsymbol{p}_0$ | Formula 12.4.1 |
| **PageRank** | web pages, genes | to a random out-neighbor, or to a random page | stationary distribution | [Definition 7.6.4](/1.4.7#def-7.6.4) |
| Network-based stratification | genes, for each tumor | propagation of the mutation profile | smoothed profiles, then NMF | Algorithm 13.5.1 |
| IsoRank | pairs of vertices of two networks | to pairs of neighbors | similarity $R$ | Formula 12.7.1 |
| Diffusion pseudotime | cells | Gaussian affinities on the kNN graph | diffusion distance from a root | Formula 7.2.1 |
| CellRank | cells | velocity and connectivity kernels, Eq. (7.4) | absorption probabilities $B = (I - Q)^{-1}R$ | Formula 7.3.3, Example 7.3.2 |

On a path $a$–$b$–$c$ seeded at $a$ with $r = 0.5$, propagation gives $(0.583, 0.333, 0.083)$ (Example 12.4.2); in a three-state progenitor chain, both transient states reach fate A with probability $0.625$ (Example 7.3.2). The shared weakness follows from the shared mathematics: a walker visits high-degree vertices often, so propagation scores must be compared with degree-matched nulls ([7.9.12](/7.9.12#sec-12.4.2)), and a fate probability is only as good as the kernel that defines the transitions ([7.9.7](/7.9.7#sec-7.3.4)).

### 18.4.4. Modules

The idea that biological networks are built from modules, groups of components that act together and are more densely connected inside than outside, appeared at every scale of the course.

| Module | Found by | Where |
|---|---|---|
| Protein complexes and functional modules | community detection with the modularity $Q$ of [1.4.7](/1.4.7#def-7.7.3), MCODE | Example 12.3.1 ($Q = 0.62$ found against $0.60$ for the planted partition), Algorithm 12.3.1 |
| Genetic-interaction modules | similarity of interaction profiles | Definition 10.6.1, Example 10.6.1 |
| Co-expression modules and eigengenes | WGCNA | Algorithm 11.3.1 |
| Disease modules | the largest connected component of disease genes against random sets | Definition 12.6.1 |
| Cell types | Leiden communities of the cell graph | Algorithm 5.5.1 |
| Cellular neighborhoods | clusters of neighbor compositions | Definition 6.11.1 |
| Signatures and subtypes | NMF of mutation catalogs and propagated profiles | Algorithm 13.3.1, Algorithm 13.5.1 |

Why networks should be modular is a question of evolution, not of graph theory: environments whose goals change among combinations of shared subproblems select modular solutions (Definition 17.4.1), a quantitative form of the **modularity** of biological systems discussed in [7.6.40](/7.6.40).

### 18.4.5. Motifs and the Sign of Feedback

The third part of the course connected small subgraphs to function. A **network motif** ([Definition 7.8.4](/1.4.7#def-7.8.4)) is a subgraph far more frequent than in randomized networks, and in transcription networks each motif performs a definite task that can be read off simple equations, Eq. (15.1), with logic input functions, Formula 15.1.1.

| Motif | Function | Key relation | Where |
|---|---|---|---|
| Negative autoregulation | faster response, robust level | $T^{\mathrm{NAR}}_{1/2}/T^{\mathrm{simple}}_{1/2} = \beta_{\mathrm{s}}/(2\beta\ln 2)$ | Proposition 15.3.1 |
| Coherent FFL (AND) | **sign-sensitive delay**, persistence detection | $T_{\mathrm{ON}} = \alpha_Y^{-1}\ln[1/(1 - K_{YZ}/Y_{\mathrm{st}})]$ | Proposition 15.4.1, Example 15.4.1 |
| Incoherent FFL | pulse, acceleration, **fold-change detection** | $T_{1/2} = \alpha_Z^{-1}\ln[1/(1 - 1/2F)]$; scalar symmetry | Proposition 15.4.3, Proposition 15.4.4 |
| **Single-input module** | temporal order, last in first out | thresholds in one order | Proposition 15.5.1 |
| Positive autoregulation, toggle | slow response, memory, bistability | needs cooperativity | Proposition 16.1.1, Proposition 16.1.2 |
| Cascade with positive feedback | all-or-none, irreversible switch | gains multiply; loop gain $> 1$ | Proposition 16.2.1, Proposition 16.2.2 |
| Two-node negative loop | damped oscillation, noise-sustained pulses | eigenvalues, Eq. (16.4) | Proposition 16.4.1, Example 16.4.1 |
| Coupled positive–negative feedback | tunable frequency at fixed amplitude | relaxation oscillation | Definition 16.4.1, Example 16.4.2 |

Behind the table is the sign rule of [7.6.33](/7.6.33#sec-33.1.1): positive loops are necessary for multistability and negative loops for sustained oscillation, while feed-forward networks are stable and can neither remember permanently nor oscillate (Proposition 16.2.3). Two refinements of the course matter for analysis. The sign of a loop is not enough: a two-node positive loop without cooperativity is monostable (Proposition 16.1.2), and a negative loop needs delay or nonlinearity to oscillate, so that a three-stage loop needs gain above $\sec(\pi/3)^3 = 8$ ([Theorem 33.5.1](/7.6.33#thm-33.5.1)). And motifs are embedded: the interlocked FFLs of sporulation produce three waves of expression (Example 15.5.1), and two positive loops widen the bistable range of a switch from $4.3$- to $18$-fold (Example 16.2.2). The other large-scale regularity, that **hubs** are more often essential (Definition 12.2.1), turned out to need no special role of topology: if each interaction is essential with a small probability, the probability of essentiality rises with degree by itself (Formula 12.2.1, Example 12.2.1).

## 18.5. Dynamics and Inverse Problems

### 18.5.1. One Form of Equation

The dynamical chapters wrote every network in one form, $\mathrm{d}\boldsymbol{x}/\mathrm{d}t = N\boldsymbol{v}(\boldsymbol{x}, \boldsymbol{p})$, Eq. (14.1), with the **stoichiometric matrix** $N$ and rate laws $\boldsymbol{v}$ (Definition 14.2.1). Its left null space gives the **conserved moieties** (Theorem 14.2.1), time-scale separation reduces it (Formula 14.2.1; the same separation gives the transcription-network form Eq. (15.1)), and the course solved it with explicit and implicit methods, choosing implicit ones for stiff systems ($65\,630$ against $463$ evaluations, Example 14.3.3). The same equations appeared outside the dynamical chapters, which is the clearest sign that the three layers of the course are one subject:

- RNA velocity is the solution of a two-variable linear ODE for unspliced and spliced RNA, Eq. (7.3), read backward from a snapshot (Definition 7.3.1);
- the attractors of Eq. (7.1) and the quasi-potential $U = -\ln p_{\mathrm{s}}$ (Definition 7.1.1) are the dynamical meaning of a cell type;
- modular response analysis reads direct effects from the inverse of the matrix of steady-state responses of a linearized network (Formula 11.6.1, Example 11.6.1);
- metabolic labeling turns the fraction of new RNA into a degradation rate through the solution of a first-order ODE, Eq. (4.5).

### 18.5.2. Stability, Bifurcations and Noise

Steady states and their stability are read from the Jacobian; a pair of eigenvalues crossing the imaginary axis is a **Hopf bifurcation**, as in the Bier model of glycolysis at $K_{\mathrm{m}} = 15.24$ (Definition 14.4.1, Example 14.4.2), and many oscillators synchronize above a critical coupling, $r = \sqrt{1 - K_{\mathrm{c}}/K}$ (Theorem 16.4.1). Sensitivities organize the question of what matters: control coefficients of a network follow from its elasticities, $C^S = -(ND\varepsilon)^{-1}ND$, Eq. (14.8) (Theorem 14.5.1), and a drug's effect is its elasticity times the control coefficient of its target, the **combined response theorem** (Theorem 14.5.2). Noise adds a second level: a target inherits propagated noise $H^2\frac{\gamma_y}{\gamma_x + \gamma_y}\eta_x^2$ from its regulator, Eq. (17.1) (Theorem 17.1.1), damped oscillators pulse indefinitely when noise drives them (Example 16.4.1), and robust designs make chosen outputs insensitive to parameters: the bifunctional sensor fixes $Y_{\mathrm{p}} = k_{\mathrm{a}}K_2/k_{\mathrm{p}}$ independently of protein levels (Formula 17.2.1), and the BIG model compensates the whole glucose response for insulin sensitivity (Definition 17.3.1, Theorem 17.3.1).

### 18.5.3. What the Data Determine

The deepest recurring theme of the course may be identifiability: what a given experiment can determine, whatever the analysis. It appeared in every layer.

| Problem | What is not determined | What resolves it | Where |
|---|---|---|---|
| Gene induction measured early | the degradation rate | a time course over several time constants | Example 1.5.1 |
| Fluorescence with unknown scale | production rate and scale separately | an independent calibration | Example 14.7.1 |
| Michaelis–Menten from low substrate | $K_{\mathrm{M}}$ and $V_{\max}$ separately | higher $S_0$; profile likelihood | Examples 14.7.3–14.7.4, Formula 14.7.1 |
| Copy number of a tumor | purity and ploidy jointly | allele fractions and priors | Definition 13.2.1, Example 13.2.1 |
| Causal network from observational data | arc directions within a Markov equivalence class | interventions | Definition 11.6.2, Theorem 11.6.1 |
| Indirect versus direct dependence | the edge X–Z in a chain | conditioning: partial correlation, DPI | Example 11.3.1, Example 11.4.1 |
| Splicing kinetics from one snapshot | time scale of velocity | metabolic labeling, lineage | [7.9.7](/7.9.7#sec-7.3.3) |

The tools were the same throughout: the **profile likelihood** rather than the curvature of the likelihood (Formula 14.7.1), the **Fisher information** and its spectrum ([7.9.14](/7.9.14#sec-14.7.2)), and above all the design of the experiment, since non-identifiability is a property of the experiment, not of the model (Definition 14.7.1).

## 18.6. An Index of Models

The tables list the main models of the course with their defining equation and where they are developed. They are an index, not a substitute for the derivations, which state the assumptions.

Measurement (7.9.2–7.9.9):

| Model | Equation or rule | Where |
|---|---|---|
| EM for transcript abundances | $L(\boldsymbol{\alpha}) = \prod_c\bigl(\sum_{t \in T_c}\alpha_t/\tilde\ell_t\bigr)^{n_c}$ | Eq. (2.1), Algorithm 2.3.1 |
| TPM | $10^6(k_g/\tilde\ell_g)/\sum_h(k_h/\tilde\ell_h)$ | Definition 2.4.1 |
| Quantile normalization | rank $r$ replaced by the mean of rank $r$ | Definition 2.5.1 |
| Over-representation | hypergeometric tail | Eq. (3.1) |
| GSEA running sum | weighted hits minus misses | Eq. (3.2) |
| Percent spliced in | $\hat\psi = (I/l_I)/(I/l_I + S/l_S)$ | Eq. (4.1) |
| Differential translation | NB with assay × condition interaction | Eq. (4.2) |
| Labeled reads | binomial mixture of new and old RNA | Eq. (4.4), Eq. (4.5) |
| Multiplets | $m(\lambda) \approx \lambda/2$ | Eq. (5.1) |
| Sequencing saturation | $1 - U(r)/r$ with gamma abundances | Eq. (5.2), Eq. (5.3) |
| UMI counts | NB, $\operatorname{Var} = \mu + \mu^2/\theta$ | Eq. (5.4) |
| Pearson residuals | $(x - \hat\mu)/\sqrt{\hat\mu + \hat\mu^2/\theta}$ | Eq. (5.5) |
| Bulk deconvolution | $\min_{\boldsymbol{w} \ge \boldsymbol{0}}\lVert\boldsymbol{y} - S\boldsymbol{w}\rVert^2$ | Eq. (5.6) |
| scVI | latent $\boldsymbol{z}$, NB decoder | Eq. (5.7) |
| Spillover compensation | $\min_{\boldsymbol{x} \ge \boldsymbol{0}}\lVert\boldsymbol{y} - S\boldsymbol{x}\rVert^2$ | Eq. (6.1) |
| **Moran's I** | weighted autocovariance over variance | Eq. (6.2), Proposition 6.10.1 |
| Spatially variable genes | Gaussian process with squared-exponential kernel | Eq. (6.3) |
| Ripley's K | pair counts within $r$ | Eq. (6.4) |
| Spatial domains | Gaussian emissions, Potts prior | Eq. (6.5), Eq. (6.6) |
| Spot deconvolution | $y_{sg} \sim \mathrm{Poi}(N_s\sum_k\pi_{sk}\mu_{gk})$ | Eq. (6.7) |
| Optimal transport | $\min\sum C_{ij}P_{ij}$, marginals $\boldsymbol{a}, \boldsymbol{b}$ | Eq. (6.8) |
| Kabsch registration | rotation from the SVD of the cross-covariance | Eq. (6.9) |
| Fused Gromov–Wasserstein | expression cost plus distance distortion | Eq. (6.10) |
| Toggle landscape | $\dot x = a/(1 + y^n) - x$, $\dot y = a/(1 + x^n) - y$ | Eq. (7.1) |
| Diffusion pseudotime | diffusion distance from a root | Eq. (7.2) |
| Splicing kinetics, RNA velocity | $\dot u = \alpha - \beta u$, $\dot s = \beta u - \gamma s$ | Eq. (7.3) |
| Fate probabilities | $B = (I - Q)^{-1}R$ with the kernel of Eq. (7.4) | Eq. (7.5) |
| Communication probability | $P_{ij} = L_iR_j/(K + L_iR_j)$ | Eq. (7.6) |
| Peak calling | local Poisson background | Algorithm 8.2.1 |
| Footprint occupancy | $(C + 1)/L + (C + 1)/R$ | Eq. (8.1) |
| Chromatin states | multivariate Bernoulli HMM | Eq. (8.3) |
| Methylation counts | beta-binomial | Eq. (8.4) |
| Hi-C balancing | $O_{ij} = b_ib_jT_{ij}$, Sinkhorn–Knopp | Algorithm 8.6.1, Theorem 8.6.1 |
| Directionality index | signed $\chi^2$ of upstream and downstream contacts | Eq. (8.5) |
| ABC model | activity × contact, normalized | Eq. (8.6) |
| Peptide mass | $m/z = (M + zm_{\mathrm{H}^+})/z$ | Eq. (9.1)–(9.3) |
| Probability score | binomial tail of matched ions | Eq. (9.4) |
| Target–decoy FDR | $D(t)/T(t)$ | Eq. (9.5) |
| Ratio compression | co-isolation fraction $\phi$ | Eq. (9.6) |
| Censored intensities | normal likelihood with a detection limit | Eq. (9.7) |
| Isotope correction | $\boldsymbol{m} = A\boldsymbol{f}$ | Eq. (9.9) |

Networks (7.9.10–7.9.13):

| Model | Equation or rule | Where |
|---|---|---|
| Combined evidence | $S' = 1 - \prod(1 - s_i')$ with the prior removed | Eq. (10.1) |
| Interactome size | $\hat N = \pi_1n_1\pi_2n_2/m$ | Eq. (10.2) |
| Guide test, rank aggregation | NB tail; $\rho = \min_j\mathbb{P}(U_{(j)} \le r_j)$ | Formula 10.7.1, Eq. (10.3) |
| Partial correlation | $-\Omega_{ij}/\sqrt{\Omega_{ii}\Omega_{jj}}$ | Formula 11.3.1 |
| Graphical lasso | $\max\{\log\det\Omega - \operatorname{tr}(S\Omega) - \lambda\sum\lvert\Omega_{ij}\rvert\}$ | Formula 11.3.2 |
| Topological overlap | $(l_{ij} + a_{ij})/(\min(k_i, k_j) + 1 - a_{ij})$ | Definition 11.3.2 |
| Gaussian mutual information | $-\tfrac12\ln(1 - \rho^2)$ | Formula 11.4.1 |
| ARACNe | DPI pruning of triangles | Theorem 11.4.1, Algorithm 11.4.1 |
| CLR | $\sqrt{z_i^2 + z_j^2}$ | Formula 11.4.2 |
| GENIE3 | random-forest importance per target | Algorithm 11.5.1 |
| Modular response analysis | $r_{ij} = -(R^{-1})_{ij}/(R^{-1})_{ii}$ | Formula 11.6.1 |
| SCENIC | co-expression, motif pruning, AUCell | Algorithm 11.7.1 |
| Essential interactions | $1 - (1 - \beta)(1 - \alpha)^k$ | Formula 12.2.1 |
| Active subnetworks | $z_A = \sum z_v/\sqrt{k}$, standardized | Algorithm 12.4.1 |
| Random walk with restart | $r(I - (1 - r)W)^{-1}\boldsymbol{p}_0$ | Formula 12.4.1 |
| Differential co-expression | Fisher $z$ difference | Formula 12.5.1 |
| Disease network | bipartite projection $BB^{\mathsf T}$ | Formula 12.6.1 |
| Drug proximity | mean closest distance, degree-matched $z$ | Formula 12.6.2 |
| IsoRank | $R = \alpha W_1RW_2^{\mathsf T} + (1 - \alpha)E$ | Formula 12.7.1 |
| Copy number | logR and BAF from purity, ploidy, allele states | Formula 13.2.1 |
| Cancer cell fraction | VAF $\times$ copy number / purity | Definition 13.2.2 |
| Signatures | Poisson NMF by multiplicative updates | Algorithm 13.3.1 |
| Driver recurrence | $X_g \sim \mathrm{Poi}(L_gT\mu_g)$ | Formula 13.4.1 |
| Selection | $\omega = (n_{\mathrm{N}}/L_{\mathrm{N}})/(n_{\mathrm{S}}/L_{\mathrm{S}})$ | Formula 13.4.2 |
| Stratification | propagation, NMF, consensus | Algorithm 13.5.1 |
| Tumor mutational burden | mutations per megabase | Definition 13.7.1 |

Dynamics and design (7.9.14–7.9.17):

| Model | Equation or rule | Where |
|---|---|---|
| Reaction network | $\dot{\boldsymbol{x}} = N\boldsymbol{v}(\boldsymbol{x}, \boldsymbol{p})$ | Eq. (14.1) |
| Enzyme with conservation | Eq. (14.2); QSSA if $E_{\mathrm{T}}/(S_0 + K_{\mathrm{M}}) \ll 1$ | Formula 14.2.1 |
| Lotka–Volterra | $\dot x = x(\alpha - \beta y)$, $\dot y = y(-\gamma + \delta x)$ | Eq. (14.3) |
| Euler and Runge–Kutta | orders $1$ and $4$ | Eq. (14.4), Theorem 14.3.1, Algorithm 14.3.2 |
| Bier glycolytic oscillator | $\dot G = V_{\mathrm{in}} - k_1GT$, $\dot T = 2k_1GT - k_{\mathrm{p}}T/(T + K_{\mathrm{m}})$ | Eq. (14.5) |
| Sensitivity equations | $\dot S = JS + \partial\boldsymbol{f}/\partial\boldsymbol{p}$; steady state $-J^{-1}\partial\boldsymbol{f}/\partial\boldsymbol{p}$ | Eq. (14.6), Eq. (14.7) |
| Control coefficients | $C^S = -(ND\varepsilon)^{-1}ND$, $C^J = I + \varepsilon C^S$ | Eq. (14.8) |
| Fitting and intervals | $\chi^2$; profile likelihood threshold $3.84$ | Formula 14.6.1, Formula 14.7.1 |
| Transcription network | $\dot Y = f(X^*) - \alpha Y$; logic input functions | Eq. (15.1), Eq. (15.2) |
| Two-input promoter | independent binding of activator and repressor | Eq. (15.3) |
| Motif counts | $\lambda$, $\lambda^3$, $\lambda^3/3$ | Eq. (15.4) |
| Motif response times | Eq. (15.5), Eq. (15.7)–(15.9) | Propositions 15.3.1–15.4.3 |
| Fold-change detection | scalar symmetry | Eq. (15.10) |
| λ switch | CI–Cro model | Eq. (16.1) |
| Cascade gain, loop gain | $\prod R_k$; instability when $\partial\ln F/\partial\ln x > 1$ | Eq. (16.2), Eq. (16.3) |
| Two-node negative loop | eigenvalues | Eq. (16.4) |
| Li–Rinzel Ca²⁺ model | IP₃ receptor activation and inactivation | Eq. (16.5) |
| Kuramoto | $r = \sqrt{1 - K_{\mathrm{c}}/K}$ | Eq. (16.6) |
| Cascade noise | $\eta_y^2 = 1/\langle y\rangle + H^2\frac{\gamma_y}{\gamma_x + \gamma_y}\eta_x^2$ | Eq. (17.1) |
| Bet hedging | $\Lambda(q) = p\ln[qa_1 + (1 - q)b_1] + (1 - p)\ln[qa_2 + (1 - q)b_2]$ | Eq. (17.2), Theorem 17.1.2 |
| Insulin–glucose, BIG model | Eq. (17.3), Eq. (17.4) | Theorem 17.3.1 |
| Cost of regulation | $F_1 = pb - c$, $F_2 = p(b - c) - r$ | Formula 17.4.1 |
| FFL selection | $\varphi(D) = -c\beta D + \int_0^Db(Z)\,\mathrm{d}t$ | Eq. (17.5), Theorem 17.4.1 |
| Duplication–divergence | $\bar k \to 2p/(1 - 2q)$ | Theorem 17.4.2 |
| Retroactivity | slowdown $1 + p_{\mathrm{T}}K_{\mathrm{D}}/(K_{\mathrm{D}} + X)^2$ | Eq. (17.6) |

Models of the biophysics course used here:

| Model | Equation or rule | Where |
|---|---|---|
| Bursty expression | negative binomial copy numbers | [Theorem 32.4.1](/7.6.32#thm-32.4.1) |
| **Gillespie algorithm** | exponential waiting times, reaction chosen by propensity | [Algorithm 32.5.1](/7.6.32#alg-32.5.1) |
| **Linear noise approximation** | $JC + CJ^{\mathsf T} + D = 0$ | [Definition 32.6.2](/7.6.32#def-32.6.2) |
| **Genetic toggle switch** | bistable above a critical synthesis rate | [Theorem 33.3.1](/7.6.33#thm-33.3.1) |
| Goodwin loop | gain $> \sec(\pi/N)^N$ | [Theorem 33.5.1](/7.6.33#thm-33.5.1) |
| **Flux balance analysis** | $S\boldsymbol{v} = \boldsymbol{0}$, maximize an objective | [Definition 34.4.2](/7.6.34#def-34.4.2) |
| Integral feedback | adaptation independent of the input | [Theorem 35.6.1](/7.6.35#thm-35.6.1) |
| Logarithmic sensitivity | $\partial\ln y/\partial\ln p$ | [Definition 40.1.2](/7.6.40#def-40.1.2) |
| Archetypes | optima on the polytope of task specialists | [Theorem 40.4.1](/7.6.40#thm-40.4.1), Definition 7.1.2 |

## 18.7. Orders of Magnitude

Order-of-magnitude reasoning decides which analyses are possible before any code is written: whether a matrix fits in memory, whether a test survives correction for the number of candidates, whether a sample can determine the number of parameters. The figure collects the scales quoted in the chapters.

![Orders of magnitude of the data of the course, with the chapters that give them: from the 5–40 cells that share a Visium spot and the 8 libraries of the airway study, through the thousands of UMIs counted per cell, the 10⁵ mRNA molecules of a cell and the 10³–10⁸ copies of its proteins, the 10⁴–10⁵ cells of an experiment and the millions of an atlas, the 3.2 × 10⁷ candidate factor–gene arcs and 2 × 10⁸ gene pairs, to the 4.9 × 10⁹ contacts of a deep Hi-C map, the 4.8 × 10¹⁰ bin pairs of the genome at 10 kb, and the 4 × 10¹⁰ and 2.2 × 10¹¹ bytes of a whole-slide CODEX image and of the reads of one 30× genome](./plots/scales.py)

| Quantity | Value | Consequence | Where |
|---|---|---|---|
| A 30× human genome | $9.3\times10^{10}$ bases, about $220$ GB of reads | cohorts reach petabytes; analysis where the data are stored | Example 1.4.1 |
| mRNA per cell, captured by droplets | $\sim10^5$ molecules, a few thousand counted | most genes are zero or a few in each cell | [7.9.5](/7.9.5), Example 6.3.1 |
| Cells per experiment, per atlas | $10^4$–$10^5$; millions | sparse matrices, neighbor graphs instead of distance matrices | [7.9.5](/7.9.5) |
| Cells sharing a Visium spot | $5$–$40$ | spot data need deconvolution | Example 6.2.1 |
| Whole-slide CODEX image | $4\times10^{10}$ bytes | tiled processing with halos | Example 6.6.1, Algorithm 6.6.1 |
| Hi-C at $10$ kb | $3.1\times10^5$ bins, $4.8\times10^{10}$ bin pairs | billions of contacts for useful resolution | [7.9.8](/7.9.8#sec-8.6.2) |
| Protein copy numbers | $10^3$–$10^8$ per cell; plasma $> 10^{10}$ range | separation, enrichment and affinity methods | [7.9.9](/7.9.9#sec-9.1) |
| Candidate regulatory arcs | $1600 \times 20\,000 = 3.2\times10^7$ | inference is underdetermined; sparsity and priors | [7.9.11](/7.9.11#sec-11.1) |
| Gene pairs | $2\times10^8$; Bonferroni threshold $2.5\times10^{-10}$ | differential co-expression needs modules or many samples | Example 12.5.1 |
| Yeast double mutants | $2.3\times10^7$ tested, $\sim9\times10^5$ interactions | the only near-complete genetic network | [7.9.10](/7.9.10#sec-10.6.2) |
| Candidate arcs against precision | $30\,\%$ recall at $0.1\,\%$ false positive rate | most predicted arcs are false | Example 11.8.1 |

The last row generalizes. Whenever the number of candidates is $10^7$ or more and the true edges are $10^5$, a false positive rate that sounds small produces more false edges than true ones; precision, not the false positive rate, is the number to report for network inference.

## 18.8. A Short History in Methods

The history of systems biology is largely a history of measurement, with analysis methods following each new data type within a few years. Section 1.3 of 7.9.1 gives the institutional history; the timeline places the measurements and methods of the course.

![Measurements (left) and analysis methods and models (right) of systems biology, 1995–2025, with the chapters (7.9.n) where they appear: from cDNA microarrays, the first yeast interaction and genetic-interaction maps and SILAC, through RNA-seq, Hi-C, ATAC-seq, droplet single-cell RNA-seq, MERFISH, spatially barcoded arrays, Perturb-seq and the global yeast genetic map, to CODEX, Slide-seq, Stereo-seq, Xenium and genome-wide Perturb-seq; and from the centrality–lethality rule, network motifs, active subnetworks and modular response analysis, through GSEA, ARACNe, the connectivity map, target–decoy FDR, MACS, WGCNA, ChromHMM, GENIE3, IDR and ICE, mutational signatures and DESeq2, to SCENIC, RNA velocity, MNN, scVI, Harmony, Tangram, Cellpose, CellRank and SpatialData](./plots/timeline.py)

Three periods can be distinguished. Around 2000–2003 the first genome-scale maps of interactions and transcription networks gave network biology its founding observations: heavy-tailed degree distributions, the centrality–lethality rule and network motifs (7.9.12, 7.9.15). From about 2005 to 2014 the analysis of bulk sequencing data was consolidated, with gene-set analysis, network inference, peak calling, chromatin states and the count models of differential expression. Since 2015 the resolution has moved to single cells and to positions in tissues, and the methods to neighbor graphs, generative models, optimal transport and image analysis (7.9.5–7.9.7). The rate of change is itself a lesson: many tools of the course will be replaced within a decade, while the structures of Section 18.3 have persisted through every change of platform.

## 18.9. Open Problems

### 18.9.1. Causal Networks

Most networks of the course are statistical or physical maps, and the step to a causal wiring diagram is the central unsolved problem of the inverse half of systems biology. Observational data determine a network only up to Markov equivalence (Theorem 11.6.1); hidden confounders, above all cell-type composition, create edges; and benchmarks of inference from single-cell data found recovery only modestly better than random ([7.9.11](/7.9.11#sec-11.8.2)). Perturbations break the equivalence (Formula 11.6.1), and pooled screens with single-cell readout now perturb thousands of genes in one experiment ([7.9.7](/7.9.7#sec-7.7.2)), but the effects of most perturbations in a given cell type are small, and the combinatorial space of double perturbations, where **epistasis** lives, is far larger than any screen.

### 18.9.2. Context Specificity

Every edge holds in a context. Footprint networks share only about $5\,\%$ of their arcs across $41$ cell types (Example 11.2.1); genetic interactions change with conditions ([7.9.10](/7.9.10)); interaction maps record possible rather than realized contacts. The question is how to represent networks that change with cell type, state, position and time without estimating a separate network for every context from too few samples. Single-cell and spatial data supply the contexts; the statistical machinery for context-dependent networks with shared structure is still being built.

### 18.9.3. Topology Does Not Determine Dynamics

The motif chapters showed that a wiring diagram constrains behavior, through the sign rule and the stability of feed-forward networks, but does not determine it. A two-node positive loop is bistable or not depending on cooperativity (Proposition 16.1.2), a negative loop oscillates or not depending on gain and delay, and a cascade switches or not depending on loop gain (Proposition 16.2.2). The parameters that decide are rarely measured, and fits determine combinations of them (Section 18.5.3). Connecting the large networks of the second part of the course to the dynamical models of the third therefore remains open: the large maps lack rates, the dynamical models cover small circuits, and the designs that work for most parameters (integral feedback, bifunctional sensors, dynamical compensation) are the cases where topology does decide.

### 18.9.4. Foundation Models and Virtual Cells

Large models pretrained on tens of millions of single-cell profiles, and on spatial and pathology data, are proposed as representations of cell state that transfer across studies, and as predictors of the response to perturbations, the vision often called a virtual cell ([7.9.7](/7.9.7#sec-7.7.3), [7.9.6](/7.9.6#sec-6.14)). The present evidence is mixed: on held-out perturbations several deep-learning predictors did not beat simple linear baselines, such as adding the effects of two single perturbations to predict a double one (Ahlmann-Eltze, Huber and Anders, 2025), and zero-shot embeddings were often matched by principal components. Part of the difficulty is the data, in which most effects are small and many share a generic stress response; part is evaluation, in which metrics can reward predicting the average. The lesson for any such claim is the one of Section 18.3.3: compare against the strongest simple baseline before drawing biological conclusions.

### 18.9.5. Methods That Change Faster Than Questions

Omics technologies keep appearing: new layers (epitranscriptomes, proteoforms, spatial chromatin), new resolutions (subcellular imaging, three-dimensional tissues) and new scales (whole organs, cohorts of patients). Each brings data that are multimodal, sparse, noisy and heterogeneous, mostly snapshots at low sampling rates in time, and each requires integration across sequence, abundance, image and text. The understanding of networks has grown more slowly than the measurement of their parts: degree distributions and motifs were found two decades ago, while the questions of causality, context and dynamics above remain open. This asymmetry is why the connection to graph theory and network science ([1.4.7](/1.4.7)) and to dynamical systems ([2.4](/2.4)) is likely to matter more, not less, as the data grow. The applications named most often are the hierarchical organization from molecules to cells to tissues, data acquisition and analysis that assist clinical decisions, and the design of artificial biological systems, where the principles of 7.9.15–7.9.17 are tested by construction (Definition 17.5.1).

## 18.10. Connections to Other Courses

- [Network science](/1.4.7) supplies the general mathematics used throughout the second part: degree distributions, random graphs and the configuration model, centrality and PageRank, communities and modularity, percolation, and the statistics of motifs.
- [Ordinary differential equations](/2.4) supply the phase planes, linear stability, limit cycles and bifurcations of the third part; the Lotka–Volterra system (Eq. (14.3)) is treated there as a planar system.
- [Statistics](/3) and [machine learning](/4.6) supply PCA, clustering, the lasso, random forests, hidden Markov models and neural networks; [biostatistics](/7.7) supplies the count models and multiple testing ([7.7.20](/7.7.20)), survival analysis ([7.7.16](/7.7.16)) and prediction models ([7.7.21](/7.7.21)) that the measurement and cancer chapters apply.
- [Bioinformatics](/7.8) supplies reads, alignment, variant calling, motifs and position weight matrices, sequence models and structure prediction; this course starts where those methods have produced counts.
- [Biophysics](/7.6), especially its quantitative-biology chapters 7.6.32–7.6.41, supplies the stochastic and physical foundations of the dynamical part: the chemical master equation, toggle switches and oscillators, flux balance analysis, sensing limits, growth laws and robustness.
- Later biology courses use the results: evolution of networks by duplication and divergence, bet hedging and persisters in microbiology, the insulin–glucose circuit in physiology, single-cell atlases in immunology, and network motifs in computational neuroscience.

## Summary

- The course has three layers (18.1.1): measuring parts and states (7.9.2–7.9.9), connecting them into networks (7.9.10–7.9.13) and explaining behavior by dynamics and design (7.9.14–7.9.17); forward and inverse models (Definition 1.5.1) run through all three, and the dependence runs both ways, from the negative binomial of bursty expression (Formula 5.4.1) to the attractors that clustering calls cell types (18.1.1). A few systems recur: the airway experiment, the *E. coli* transcription network, the yeast interaction and genetic maps, and simulations with known truth (18.1.2).
- Omics layers share a design (18.2): convert a molecular property into countable events, compare with a background that shares the biases, and report features or edges; precision is set by the informative events of one feature.
- Eight statistical structures recur (18.3): counts with sampling and biological variation, where depth reduces only the first part and replicates are the unit of inference (Example 2.2.1, Definition 5.6.1, Example 5.6.1, Example 13.4.2); mixtures fitted by EM (Algorithm 2.3.1, Formula 4.5.1, Algorithm 6.12.1); null models from parameters, controls, decoys (Formula 9.4.2), permutations and randomized networks, with every data-dependent choice inside the null (Example 13.6.1, Example 13.6.2); set statistics on rankings (Definition 3.2.1, Definition 3.3.1, Algorithm 7.7.1, Definition 11.7.1); embeddings, neighbor graphs and communities (Algorithm 5.5.1, Formula 7.2.1, Algorithm 13.5.1); optimal transport and Sinkhorn scaling, one algorithm for mapping cells and balancing Hi-C (Definition 6.12.2, Theorem 8.6.1); hidden Markov models and Potts priors (Formula 8.4.1, Eq. (6.5)); and information, from the data processing inequality (Theorem 11.4.1) to error-correcting codes (Definition 6.3.1) and the entropy cost of bet hedging (Theorem 17.1.2).
- Network ideas recur (18.4): an edge must be read by its kind, and maps are samples; randomized networks of increasing realism are the null models of motifs and modules (Proposition 15.2.1, Example 15.2.1); propagation, PageRank, IsoRank, pseudotime and fate probabilities are Markov chains on graphs (Formula 12.4.1, Formula 12.7.1, Formula 7.3.3); modules appear from complexes to cell types and neighborhoods; motifs perform definite tasks, and the sign rule (positive loops for memory, negative loops for clocks, feed-forward networks stable; Proposition 16.2.3) organizes the dynamical chapters.
- Dynamics (18.5): one form $\dot{\boldsymbol{x}} = N\boldsymbol{v}$ (Eq. (14.1)) covers kinetic models, transcription networks, RNA velocity and response analysis; stability and Hopf bifurcations (Example 14.4.2), control coefficients (Theorem 14.5.1, Theorem 14.5.2), propagated noise (Theorem 17.1.1) and robust designs (Formula 17.2.1, Theorem 17.3.1) describe behavior; identifiability, from Markov equivalence (Theorem 11.6.1) to profile likelihoods (Formula 14.7.1), decides what data can determine.
- The model index (18.6) lists about one hundred models with their equations and places; the orders of magnitude (18.7) range from $5$–$40$ cells per spot to $10^{11}$ bytes per genome and $3.2\times10^7$ candidate arcs, so that precision, not the false positive rate, measures inferred networks; the timeline (18.8) runs from microarrays and the first interaction maps to single-cell and spatial methods.
- Open problems (18.9): causal inference from perturbations, context-specific networks, the gap between topology and dynamics, the evaluation of foundation models against simple baselines, and the rapid turnover of methods against slowly growing understanding of networks.

## Questions

1. A pseudobulk comparison has $4$ donors per condition, a gene with a mean of $50$ counts per pseudobulk sample in each condition and a between-donor dispersion $\phi = 0.1$. What is the standard error of the log fold change? Compare doubling the sequencing depth with doubling the number of donors, and give the limit at infinite depth.

   **Answer** By the variance formula of Example 2.2.1, $\operatorname{Var} = (1/\mu_A + 1/\mu_B + 2\phi)/n = (0.02 + 0.02 + 0.2)/4 = 0.06$, so the standard error is $0.245$. Doubling depth gives $(0.01 + 0.01 + 0.2)/4 = 0.055$, s.e. $0.235$, a gain of $4\,\%$; doubling donors gives $0.24/8 = 0.03$, s.e. $0.173$, a gain of $29\,\%$. At infinite depth the s.e. is $\sqrt{0.2/4} = 0.224$. For a twofold change ($\ln 2 = 0.693$) the approximate power of a two-sided test at $0.05$ rises from $0.81$ (4 donors) to $0.84$ with twice the depth but to $0.98$ with twice the donors. The between-donor variation is the floor (Figure in 18.3.1); this is why cells are not replicates (Example 5.6.1).

2. Show that the iterative correction of a Hi-C matrix and entropic optimal transport solve the same algebraic problem. Illustrate with the observed matrix $O = \begin{bmatrix} 9 & 3 \\ 3 & 1 \end{bmatrix}$.

   **Answer** Iterative correction seeks biases with $O_{ij} = b_ib_jT_{ij}$ such that $T$ has equal row sums (Algorithm 8.6.1), that is diagonal matrices $D$ with $DOD$ doubly stochastic up to a constant; the Sinkhorn–Knopp theorem guarantees a unique solution for a positive matrix (Theorem 8.6.1). Entropic transport writes the plan as $\operatorname{diag}(\boldsymbol{u})K\operatorname{diag}(\boldsymbol{v})$ with $K = \mathrm{e}^{-C/\varepsilon}$ and finds $\boldsymbol{u}, \boldsymbol{v}$ by alternately matching row and column sums to $\boldsymbol{a}, \boldsymbol{b}$ (Definition 6.12.2): the same scaling of a positive matrix, with prescribed instead of equal marginals. For the example, $O$ is the outer product of $(3, 1)$ with itself, so $b = (3, 1)$ and $T_{ij} = O_{ij}/(b_ib_j) = 1$ for all entries: the first bin is three times as visible, and after correction both bins have the same coverage. A matrix with genuine structure (more contacts within a domain) keeps that structure after balancing, because only row and column factors are removed.

3. On the path $a$–$b$–$c$ with restart probability $r = 0.5$, compute the propagation scores for a seed at $b$ and compare them with the seed at $a$ (Example 12.4.2). What does the comparison say about degree bias?

   **Answer** With $W = AK^{-1}$ and $\boldsymbol{p} = r(I - (1 - r)W)^{-1}\boldsymbol{p}_0$ (Formula 12.4.1), the seed at $b$ gives $\boldsymbol{p} = (0.167, 0.667, 0.167)$, against $(0.583, 0.333, 0.083)$ for the seed at $a$. A neighbor of the seed receives $0.333$ when it is the central vertex $b$ but only $0.167$ when it is an end: a seed of degree one sends its whole walk to its single neighbor, a seed of degree two splits it. Without restart, the stationary distribution of the walk is proportional to degree (here $1 : 2 : 1$), so high-degree vertices collect probability from many directions and rank high for almost any seed set in a large network. Scores must therefore be compared with those obtained from degree-matched random seeds ([7.9.12](/7.9.12#sec-12.4.2)).

4. A transcription network has $N = 1000$ genes and $A = 2000$ arcs and contains $100$ feed-forward loops and $5$ three-node feedback cycles. Compute the expected numbers in a random digraph and say what further null model is needed before calling the FFL a motif.

   **Answer** $\lambda = A/N = 2$, so Proposition 15.2.1 gives $\lambda^3 = 8$ FFLs and $\lambda^3/3 = 2.7$ cycles. The FFL count is $12.5$ times the expectation; the cycles are near expectation. But a random digraph has Poisson degrees, while real transcription networks have a few global regulators with hundreds of targets; hubs alone create many FFLs. The count must therefore also exceed that of degree-preserving randomizations ([Algorithm 7.4.2](/1.4.7#alg-7.4.2), Algorithm 15.2.1), as in Example 15.2.2, and ideally be confirmed in an independently compiled network.

5. Three genes form a chain $X \to Y \to Z$ with $\operatorname{Corr}(X, Y) = 0.9$ and $\operatorname{Corr}(Y, Z) = 0.5$ (Gaussian, so $\operatorname{Corr}(X, Z) = 0.45$). Compute the mutual informations and say which edge ARACNe removes. What goes wrong if $X$ also regulates $Z$ directly?

   **Answer** By Formula 11.4.1, $I(X; Y) = -\frac12\ln(1 - 0.81) = 0.830$ nats ($1.20$ bits), $I(Y; Z) = -\frac12\ln 0.75 = 0.144$ nats, $I(X; Z) = -\frac12\ln(1 - 0.2025) = 0.113$ nats. The data processing inequality (Theorem 11.4.1) is satisfied, and pruning removes the weakest edge of the triangle, $X$–$Z$, which is correct here. If $X$ also regulates $Z$ (a feed-forward loop), the triangle is real, but the pruning still removes its weakest edge, which may be a true one; ARACNe thus systematically under-reports feed-forward loops ([7.9.11](/7.9.11#sec-11.4.3)), the motif that 7.9.15 found most enriched. A tolerance $\varepsilon$ in the pruning, or direct evidence from binding, reduces the loss.

6. A linear network of three genes has direct effects $r_{21} = r_{32} = 0.5$ and unit self-decay. Compute the matrix of total steady-state responses to unit perturbations of each gene, and show how modular response analysis recovers the direct effects. Which observational method would have the same answer?

   **Answer** With $J = \begin{bmatrix} -1 & 0 & 0 \\ 0.5 & -1 & 0 \\ 0 & 0.5 & -1 \end{bmatrix}$ the responses are $R = -J^{-1} = \begin{bmatrix} 1 & 0 & 0 \\ 0.5 & 1 & 0 \\ 0.25 & 0.5 & 1 \end{bmatrix}$: perturbing gene $1$ changes gene $3$ by $0.25$, an indirect effect. Formula 11.6.1 gives $r_{ij} = -(R^{-1})_{ij}/(R^{-1})_{ii}$; since $R^{-1} = -J$, $r_{21} = r_{32} = 0.5$ and $r_{31} = 0$, as in Example 11.6.1. Observationally, partial correlation (Formula 11.3.1) and the data processing inequality also remove the edge $1$–$3$ of a chain, but they cannot orient it: the chain $1 \to 2 \to 3$ is Markov equivalent to $1 \leftarrow 2 \leftarrow 3$ and $1 \leftarrow 2 \to 3$ (Theorem 11.6.1). The perturbations supply the directions.

7. A two-node negative feedback loop has $\alpha_1 = \alpha_2 = 1$ and $\beta_1\beta_2 = 4$. Find the eigenvalues and the behavior, and explain why a third stage helps. What gain does a three-stage Goodwin loop need, and a five-stage one?

   **Answer** By Eq. (16.4), $\lambda = \bigl[-2 \pm \sqrt{0 - 16}\bigr]/2 = -1 \pm 2\mathrm{i}$: a stable focus, damped oscillations of period $2\pi/2 = 3.1$ removal times (Proposition 16.4.1). A two-variable loop with these signs can never cross the imaginary axis, since the trace is $-(\alpha_1 + \alpha_2) < 0$; delay is needed, by more stages or explicit delays. For a loop of $N$ identical stages the secant condition requires a gain above $\sec(\pi/N)^N$ ([Theorem 33.5.1](/7.6.33#thm-33.5.1)): $8$ for $N = 3$ and $2.89$ for $N = 5$. With noise, the damped two-node loop still pulses (Example 16.4.1), with amplitudes more variable than periods.

8. A regulator $X$ has mean $\langle x\rangle = 100$ molecules and Poisson noise; its target has $\langle y\rangle = 400$, logarithmic gain $H = 2$ and the same lifetime as $X$. What is the noise of $Y$? How does it change if $X$ fluctuates ten times faster than $Y$ is removed?

   **Answer** Eq. (17.1) gives $\eta_y^2 = 1/400 + 4 \cdot \tfrac12 \cdot 0.01 = 0.0025 + 0.02 = 0.0225$, a coefficient of variation of $15\,\%$, dominated by the propagated part (Theorem 17.1.1). With $\gamma_x = 10\gamma_y$ the factor $\gamma_y/(\gamma_x + \gamma_y) = 1/11$ gives $\eta_y^2 = 0.0025 + 0.0036 = 0.0061$, a CV of $7.8\,\%$: the slow target averages fast input noise. Gain amplifies propagated noise as $H^2$, so the ultrasensitivity that makes switches (Proposition 16.2.1) also makes them noisy.

9. A single-cell atlas has $10^6$ cells and $3\times10^4$ genes, of which $5\,\%$ of entries are nonzero. Estimate the memory of a dense 32-bit matrix and of a compressed sparse row matrix with 32-bit values and indices. Why does the standard workflow build a neighbor graph instead of a cell-by-cell distance matrix?

   **Answer** Dense: $10^6 \times 3\times10^4 \times 4 = 1.2\times10^{11}$ bytes, $120$ GB. Sparse: $1.5\times10^9$ nonzeros at $8$ bytes plus row pointers, about $1.2\times10^{10}$ bytes, $12$ GB. A distance matrix of $10^6$ cells would have $5\times10^{11}$ pairs, $2\times10^{12}$ bytes in 32 bits; a kNN graph with $k = 15$ has $1.5\times10^7$ edges. The graph keeps what clustering, pseudotime and embeddings need, local neighborhoods ([7.9.5](/7.9.5#sec-5.5.2)), at a cost linear in the number of cells; the same reasoning leads to tiling for whole-slide images (Algorithm 6.6.1).

10. A differential-expression analysis of $20\,000$ genes reports $4691$ genes at FDR $0.1$, and a proteomics run reports $6406$ peptide-spectrum matches at FDR $0.01$. How many false discoveries are expected in each list? Does an FDR of $0.1$ mean that each reported gene has a $10\,\%$ chance of being null?

    **Answer** At most about $0.1 \times 4691 = 469$ false genes and $0.01 \times 6406 = 64$ false matches are expected (in Example 9.4.3 the true proportion was $1.01\,\%$). The FDR is an average over the list: genes near the threshold have a much higher local false discovery rate than the strongest ones, so the probability of being null depends on the gene's own evidence (the local fdr of [7.7.20](/7.7.20)). A p-value is not a false discovery rate ([7.9.2](/7.9.2#sec-2.7.3)), and the estimated null fraction ($\hat\pi_0 = 0.65$ in the airway data) is what allows q-values to be less conservative than BH.

11. Name four places in the course where an analysis was invalidated by circularity or by a null model that did not share the biases of the data, and the remedy in each case.

    **Answer** (a) Marker genes tested between clusters found on the same data give small p-values for any data; the remedy is to treat them as descriptive or to test on held-out data ([7.9.5](/7.9.5#sec-5.6.1)). (b) Gene-set tests with the genome as background when only expressed genes could be selected inflate false positives ($79\,\%$ against $4.2\,\%$); the background must be the tested genes ([7.9.3](/7.9.3#sec-3.2.2)). (c) Classifiers whose genes were selected on all samples before cross-validation, and prognostic genes split at the optimal cutpoint, look strong when they are noise; all data-dependent steps must be inside the cross-validation, and cutpoints fixed in advance (Example 13.6.1, Example 13.6.2). (d) Driver genes called against one genome-wide mutation rate include hundreds of false positives; the background must include covariates and overdispersion (Example 13.4.2). Further cases are cell-level tests of donor effects (Example 5.6.1) and propagation scores without degree-matched nulls (18.4.3).

12. (Design) A cell-state transition in a tissue is suspected to be driven by a few transcription factors and signals from neighboring cells. Design a study using the methods of the course, from measurement to a tested model, and state the main statistical pitfall at each step.

    **Answer** One route: (1) profile the tissue by single-cell RNA and ATAC (multiome) in several donors per condition, and by a spatial method on serial sections (7.9.5, 7.9.6, 7.9.8); pitfalls: doublets, ambient RNA, cell-type composition, and the donor as the unit of replication (Definition 5.6.1). (2) Order the cells by pseudotime and estimate fate probabilities with a velocity or labeling kernel (Formula 7.2.1, Formula 7.3.3); pitfall: pseudotime orders states, not times, and velocity fails with multiple kinetics ([7.9.7](/7.9.7#sec-7.3.3)). (3) Infer regulons from co-expression pruned by motifs and accessibility (Algorithm 11.7.1) and rank factors by regulon activity along the trajectory (Definition 11.7.1); pitfall: correlation with cell identity, and DREAM-style benchmarks that show modest recovery (11.8). (4) Constrain ligand–receptor scores to neighbors within range in the spatial data ([7.9.6](/7.9.6#sec-6.11.3)); pitfall: expression is not signaling. (5) Test the top factors and signals by a pooled perturbation screen with single-cell readout ([7.9.7](/7.9.7#sec-7.7.2)), analyzed with guide-level count models and several guides per gene (Formula 10.7.1, Example 10.7.2). (6) Build a small kinetic model of the core circuit, fit it to time courses and check identifiability by profile likelihood (Formula 14.7.1), then ask whether its motifs (a toggle, a feed-forward loop) explain the switch-like or transient behavior observed (7.9.15, 7.9.16). Each step yields hypotheses; only the perturbations and the predictions of the fitted model test them.
