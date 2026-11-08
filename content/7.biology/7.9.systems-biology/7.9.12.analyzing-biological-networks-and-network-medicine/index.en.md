---
title: Analyzing Biological Networks and Network Medicine
description: "What can be learned from biological networks once they are built: the topology of protein-interaction, metabolic and transcription networks and the limits of incomplete maps; robustness to failure and attack; hubs, essentiality and the centrality–lethality rule, date and party hubs, bottlenecks; modules, MCODE and functional enrichment, hierarchical modularity; active subnetworks, network propagation by random walks with restart and diffusion, and its degree bias; differential networks; network medicine: the human disease network, disease modules, network separation and drug–disease proximity; network alignment with PathBLAST and IsoRank; and a complete analysis in Cytoscape and networkx."
---

The previous chapters built networks: physical and genetic interaction networks in [7.9.10](/7.9.10), regulatory networks in [7.9.11](/7.9.11). This chapter asks what can be learned from them. Three kinds of questions recur. Structural questions ask what the network looks like, which vertices are central and which groups of vertices form modules. Integrative questions use the network as a scaffold for other data: which connected region of the network responds to a perturbation, which genes near the known disease genes are good candidates. And comparative questions ask how networks differ between conditions or species. The answers are the basis of network medicine, the use of interaction networks to understand disease and find drugs.

The mathematics comes from network science, [1.4.7](/1.4.7): **degree distributions**, **centrality**, **community structure**, **percolation** and **random walks** on networks are defined there and used here without repetition. We look at the topology of real biological networks and at the limits of the maps (12.1), at hubs and essentiality (12.2), modules (12.3), active subnetworks and network propagation (12.4), differential networks (12.5), network medicine (12.6), the alignment of networks across species (12.7), and the tools for all of this (12.8). The five features of complex networks were introduced for biology in [7.6.34](/7.6.34#sec-34.1), the biological meaning of **modularity** and robustness in [7.6.40](/7.6.40), and the network motifs of transcription networks are the subject of [7.9.15](/7.9.15). Network methods for cancer, in which genes are mutated rather than expressed differently, are developed in [7.9.13](/7.9.13).

## 12.1. The Topology of Real Biological Networks

### 12.1.1. Kinds of Biological Networks

| Network | Vertices | Edges | Directed | Typical source |
|---|---|---|---|---|
| Protein interaction | proteins | physical binding | no | two-hybrid, AP-MS ([7.9.10](/7.9.10)) |
| Transcriptional regulation | factors, genes | factor regulates gene | yes, signed | binding and expression ([7.9.11](/7.9.11)) |
| Metabolic | metabolites (and reactions) | conversion by an enzyme | yes | genome annotation, KEGG, curated models |
| Signaling | proteins | modification, activation | yes, signed | literature, phosphoproteomics |
| Genetic interaction | genes | non-additive double-mutant phenotype | no, signed | SGA, CRISPR screens ([7.9.10](/7.9.10#sec-10.6)) |
| Co-expression | genes | correlated expression | no, weighted | expression compendia ([7.9.11](/7.9.11#sec-11.3)) |
| Disease | diseases, genes | gene implicated in disease | bipartite | OMIM, GWAS (12.6) |

Each row is a different graph, and network statistics are meaningful only within one kind: a metabolic network in which the currency metabolites (ATP, water, NADH) are vertices has a few vertices of enormous degree that a network without them does not.

### 12.1.2. Degree Distributions

The first finding of network biology was that these networks are not **random graphs**. In the metabolic networks of $43$ organisms from all three domains of life, the in- and out-degree distributions of metabolites followed power laws with exponents near $2.2$ (Jeong and colleagues, 2000); the yeast protein interaction network from the first two-hybrid screens had a heavy-tailed **degree distribution**, well fitted by a power law with an exponential cutoff, $p_k \propto (k + k_0)^{-\gamma}\mathrm{e}^{-(k + k_0)/k_c}$ (Jeong and colleagues, 2001). Similar distributions were reported for the interaction networks of the worm, the fly and humans.

Transcription networks have a characteristic asymmetry (Alon, 2019). They are sparse: typically fewer than $0.1\,\%$ of possible arcs exist, with a mean of $2$ to $10$ arcs per vertex. Their **out-degree** distribution is long-tailed: many factors regulate a few genes and a few global regulators, such as CRP (responding to glucose starvation) and RpoS (general stress) in *E. coli*, regulate hundreds. Their **in-degree** distribution is compact, close to a Poisson distribution, because a bacterial promoter has room for only a few binding sites; animal genes, with distal enhancers, have larger in-degrees. The sparsity reflects selection: a single mutation in a binding site removes an arc, so only arcs with a function are kept.

Two cautions temper the early claims. First, a heavy tail is not a power law, and careful fitting of degree distributions finds convincing power laws in a minority of real networks, biological ones included ([1.4.7](/1.4.7#sec-7.4.5)). Second, the maps are samples. Each screen detects a fraction of the true interactions, literature-curated networks favor well-studied proteins, and sampling changes the degree distribution: subnetworks of a **scale-free network** are not in general scale-free (Stumpf, Wiuf and May, 2005), and a network with a narrow distribution can look heavy-tailed after biased sampling ([7.9.10](/7.9.10#sec-10.5.4)). Topological conclusions should be stated for the map, compared with null models that preserve its sampling design, and checked on maps from independent methods.

### 12.1.3. Robust Yet Fragile

The robustness of a network to the loss of vertices is a **percolation** problem: how many vertices can be removed before the **giant component** breaks apart ([1.4.7](/1.4.7#sec-7.8.1)). Networks with a heavy-tailed degree distribution tolerate random failures, which rarely hit a hub, and are fragile under attacks on their hubs. In a cell, random failure corresponds to mutations of random genes, and attack to mutations or drugs that hit the most connected proteins: the same structure that explains why most mutations are tolerated suggests why some proteins are essential and some drugs are effective.

![Robustness of a simulated protein interaction network and of an incomplete map of it. The network of 3000 proteins is grown by duplication and divergence: a random protein is duplicated, the copy keeps each interaction of its parent with probability 0.4 and binds its parent with probability 0.1 (9194 interactions, mean degree 6.1, maximum 128). The map keeps each interaction with probability 0.4, like a screen of limited sensitivity (3643 interactions, mean degree 2.4, maximum 50; 25% of the proteins have no interaction). A: degree distributions, logarithmically binned. B: size of the largest connected component relative to the number of proteins, when a fraction f of the proteins is removed at random (solid) or in decreasing order of degree (dashed)](./plots/ppi_robustness.py)

The simulation uses duplication and divergence, a model of how interaction networks grow by gene duplication (Vázquez and colleagues, 2003), which generates a heavy-tailed degree distribution without preferential attachment. The complete network loses its giant component (below $5\,\%$ of the proteins) after random removal of $84\,\%$ of the proteins, but after removal of only the $16\,\%$ with the highest degree. The map tells the same story with different numbers: its largest component contains only $69\,\%$ of the proteins before any removal, collapses under random removal at $73\,\%$ and under attack at $6.5\,\%$. Robustness measured on an incomplete map underestimates the robustness of the real network; the qualitative contrast between failure and attack survives sampling, the numbers do not. Structural robustness, the connectivity of a graph, is also different from the functional **robustness** of the cell, which depends on the dynamics of the interactions and on redundancy ([7.6.40](/7.6.40)).

## 12.2. Hubs and Essentiality

### 12.2.1. The Centrality–Lethality Rule

A gene is essential if its deletion kills the cell or organism under standard conditions; in yeast about a fifth of the genes are essential, and in human cell lines the essential genes are found by **CRISPR screens** ([7.9.10](/7.9.10#sec-10.7)). Are essential proteins special in the network?

**Definition 12.2.1 (Centrality–Lethality Rule)** The **centrality–lethality rule** is the observation that in protein interaction networks the probability that a protein is essential increases with its degree, and more generally with its **centrality**: highly connected proteins are more often essential than poorly connected ones.

The rule was found in the yeast two-hybrid network (Jeong and colleagues, 2001) and confirmed in many later maps. Its explanation was debated. The original interpretation was topological: hubs hold the network together, and their removal disconnects it (12.1.3). Two later analyses located the cause in function instead.

**Formula 12.2.1 (Essential Interactions)** (He and Zhang, 2006) Suppose that each interaction of a protein is, independently with probability $\alpha$, essential (required for an essential function, for example the integrity of an essential complex), and that a protein is essential if at least one of its interactions is essential or, independently with probability $\beta$, for reasons outside the network. Then a protein of degree $k$ is essential with probability
$$
\mathbb{P}(\text{essential} \mid k) = 1 - (1 - \beta)(1 - \alpha)^k.
$$

**Example 12.2.1** With illustrative values $\alpha = 0.03$ and $\beta = 0.05$, a protein with $1$ interaction is essential with probability $0.079$, with $5$ interactions $0.18$, with $15$ interactions $0.40$ and with $30$ interactions $0.62$. The probability rises with degree although no topological role of the hubs is assumed: hubs are more often essential simply because they have more interactions that could be essential.

:::

Fitted to yeast data, this model explained the correlation without a role for connectivity as such (He and Zhang, 2006). A related analysis found that essentiality is concentrated in densely connected modules, essential complexes, and that hubs are essential largely because they belong to them (Zotenko, Mestre, O'Leary and Przytycka, 2008). The rule thus describes a real correlation, useful for prioritizing genes, but its cause is the organization of essential functions in complexes rather than the global connectivity of the network.

### 12.2.2. Date Hubs, Party Hubs and Bottlenecks

Hubs differ among themselves. Integrating the yeast interaction network with expression data, Han and colleagues (2004) distinguished party hubs, which are co-expressed with most of their partners and interact with them at the same time and place, from date hubs, which bind different partners at different times or locations and whose partners are not co-expressed with them. Removing date hubs fragmented the network more than removing party hubs, suggesting that date hubs connect modules and party hubs act within them. The dichotomy proved sensitive to the data and the threshold used, and later analyses found a continuum rather than two classes (Batada and colleagues, 2006; Agarwal, Deane, Porter and Jones, 2010); the underlying idea, that the role of a hub depends on whether its interactions are simultaneous, remains useful, and structural data now distinguish proteins that use one interface for many partners (which cannot bind them at once) from proteins with several interfaces.

The role of connecting modules is measured more directly by **betweenness centrality** ([Definition 7.6.2](/1.4.7#def-7.6.2)), the fraction of shortest paths passing through a vertex. Vertices of high betweenness, bottlenecks, need not have high degree. In regulatory networks, betweenness predicted essentiality better than degree did (Yu, Kim, Sprecher, Trifonov and Gerstein, 2007).

![Modules of a small simulated interaction network: four complexes of 8, 7, 6 and 5 proteins (each pair within a complex interacting with probability 0.7), joined by five interactions between complexes, and four peripheral proteins (62 interactions). A: communities found by recursive spectral bisection of the modularity matrix (the leading-eigenvector method): four communities with modularity Q = 0.62, which agree with the complexes except for one protein of the lower left complex that is assigned, with its link, to the lower right one. B: vertex size proportional to degree and color to betweenness centrality (dark: high). Two proteins share the highest degree, 7: the one labeled "highest degree" lies inside its complex (normalized betweenness 0.06), while the one with the highest betweenness (0.41) joins its complex to two others](./plots/modules.py)

## 12.3. Modules

### 12.3.1. Functional Modules

Cells are organized in modules: groups of molecules that act together in one function and interact more among themselves than with the rest, such as complexes, pathways and organelles (Hartwell, Hopfield, Leibler and Murray, 1999; **modularity** in the biological sense, [7.6.40](/7.6.40)). In a network, modules appear as **community structure**, and the algorithms of **community detection** ([1.4.7](/1.4.7#sec-7.7)), modularity maximization by the **Louvain algorithm** or the **Leiden algorithm**, spectral methods, stochastic block models, find them. The network [modularity](/1.4.7#def-7.7.3) $Q$ of a partition measures how many more edges fall within communities than expected in a random network with the same degrees.

**Example 12.3.1** In the network of the figure, the leading-eigenvector method finds four communities with $Q = 0.62$. The partition into the four planted complexes has $Q = 0.60$: the algorithm prefers a partition that moves one protein, with a link to another complex, into it. Maximizing $Q$ recovers the planted structure almost but not exactly, and a protein assigned to a community is a hypothesis about its membership, not a fact.

:::

Communities found by modularity maximization have known limits: a resolution limit (small modules in a large network are merged), many near-optimal partitions, and no allowance for proteins in several complexes. Methods designed for protein complexes therefore look for dense regions directly.

**Algorithm 12.3.1 (MCODE)** (Bader and Hogue, 2003) Molecular complex detection in a protein interaction network:

1. Vertex weighting. For each vertex $v$, take its closed neighborhood (the vertex and its neighbors), find the highest $k$-core of the subgraph it induces (the largest $k$ such that a subgraph with all degrees at least $k$ exists), and weight $v$ by $k$ times the density of that core.
2. Complex prediction. Starting from the heaviest vertex not yet assigned, grow a complex by adding neighbors whose weight is at least $(1 - \theta)$ times the weight of the seed (vertex weight percentage $\theta$, by default $0.2$), recursively; repeat from the next heaviest vertex.
3. Post-processing. Optionally remove vertices with only one connection in the complex ("haircut") or add neighbors above a density threshold ("fluff"); score each complex by its density times its number of vertices, and keep those above a score threshold.

The weighting costs $O(\lvert V\rvert\bar d^{\,3})$ for mean degree $\bar d$; the complexes can overlap at their boundaries. A typical setting keeps complexes with score above $2$ and at least $4$ vertices.

### 12.3.2. Functional Enrichment of Modules

A module is interpreted by the functions of its members. The standard test is **over-representation analysis** ([7.9.3](/7.9.3)): in a network of $N$ proteins, of which $K$ carry a **Gene Ontology** annotation, a module of $n$ proteins contains $x$ annotated ones, and the p-value is the upper tail of the **hypergeometric distribution**. In Cytoscape the BiNGO app (Maere, Heymans and Kuiper, 2005) computes it for all GO terms and displays the enriched terms as a subgraph of the ontology.

**Example 12.3.2** In the network of the figure ($N = 30$), suppose $9$ proteins carry an annotation: the $7$ members of one complex and $2$ others. The community containing that complex has $8$ members, $7$ of them annotated. The probability of $7$ or more annotated proteins in a random set of $8$ is $1.3 \times 10^{-4}$.

:::

Enrichment must be computed against the right background, the proteins present in the network rather than the genome: well-studied proteins are both more often in interaction maps and more often annotated, so the genome as background inflates every enrichment. And a module found because its members share interactions in curated databases is partly enriched by construction, since curators often record interactions within known pathways.

### 12.3.3. Hierarchical Modularity

Real networks combine modularity with a heavy-tailed degree distribution and high clustering, which a network of separate dense modules does not have. Ravasz and colleagues (2002) found in the metabolic networks of $43$ organisms that the **clustering coefficient** $C(k)$ of vertices of degree $k$ falls roughly as $1/k$: low-degree vertices sit in dense modules, while hubs join modules whose members are not linked to each other. A hierarchical model built by repeatedly copying and linking modules reproduces this scaling, and the hierarchy of modules matches the classical division of metabolism into pathways. In transcription networks the same scaling has a simpler origin: a factor $X$ that regulates $Y$ and, together with $Y$, $k$ output genes (a multi-output feed-forward loop) has $k + 1$ neighbors among which there are only $k$ links, so $C \approx k/\binom{k+1}{2} \approx 2/k$ (Alon, 2019; [7.9.15](/7.9.15)). Global statistics of networks are the sum of their local circuit patterns, which must be understood one by one.

## 12.4. Active Subnetworks and Network Propagation

### 12.4.1. Active Subnetworks

A list of differentially expressed or mutated genes is easier to interpret when the genes are connected. An active subnetwork brings the network and the measurements together.

**Definition 12.4.1 (Active Subnetwork)** Given a network and, for each vertex $v$, a score $z_v$ of its response to a perturbation or of its association with a phenotype, an **active subnetwork** is a connected subgraph whose aggregate score is significantly higher than that of connected subgraphs of the same size chosen at random.

**Algorithm 12.4.1 (jActiveModules)** (Ideker, Ozier, Schwikowski and Siegel, 2002) Convert each gene's p-value to $z_v = \Phi^{-1}(1 - p_v)$. For a connected subgraph $A$ of $k$ vertices, let $z_A = \sum_{v \in A}z_v/\sqrt{k}$, and standardize it by the mean $\mu_k$ and standard deviation $\sigma_k$ of $z_A$ over random sets of $k$ vertices: $s_A = (z_A - \mu_k)/\sigma_k$. Search for subgraphs of high $s_A$ by **simulated annealing**, toggling vertices in and out of a candidate set and accepting changes by the Metropolis rule, or by greedy growth from each vertex; report the subgraphs with the highest scores, and repeat with several conditions to find subgraphs active in each.

**Example 12.4.1** A connected set of four genes with $z = 2.1$, $1.5$, $2.8$ and $0.9$ has $z_A = 7.3/2 = 3.65$; none of the four alone would pass a genome-wide threshold, but together they form a candidate module, to be compared with the distribution of $z_A$ in random connected sets of four.

:::

The subgraph search is NP-hard, which is why heuristics are used, and its result depends on the network: a dense network allows connected high-scoring sets to be assembled from unrelated genes, so the null distribution must be estimated in the same network. Later methods solve the problem exactly or near-exactly as a prize-collecting Steiner tree or maximum-weight connected subgraph. A metabolic version scores each metabolite by the expression changes of the enzymes that use it, identifying reporter metabolites around which regulation is concentrated (Patil and Nielsen, 2005), a bridge from expression and proteomics to metabolic networks ([7.9.9](/7.9.9)).

### 12.4.2. Network Propagation

Active subnetworks select vertices; propagation scores all of them. The principle, "guilt by association", is that genes close in the network to genes known to be involved in a function or disease are likely to be involved too.

**Definition 12.4.2 (Network Propagation)** **Network propagation** assigns to every vertex of a network a score obtained by spreading an initial signal $\boldsymbol{p}_0$ on a set of seed vertices along the edges, by a random walk with restart, by diffusion, or by a related linear operator; the score of a vertex measures its proximity to the seeds, weighted over all paths.

**Formula 12.4.1 (Random Walk with Restart)** Let $A$ be the adjacency matrix of a connected undirected network, $W = AK^{-1}$ the column-normalized transition matrix ($K$ the diagonal matrix of degrees), $\boldsymbol{p}_0$ a probability vector on the seeds and $r \in (0, 1]$ the restart probability. A walker that at each step returns to the seeds with probability $r$ and otherwise moves to a random neighbor has the visiting distribution
$$
\boldsymbol{p}_{t+1} = (1 - r)W\boldsymbol{p}_t + r\boldsymbol{p}_0,
$$
which converges from any start to
$$
\boldsymbol{p} = r\bigl(I - (1 - r)W\bigr)^{-1}\boldsymbol{p}_0.
$$

**Proof** $W$ is column-stochastic, so its induced $\ell_1$ norm is $1$ and its **spectral radius** is at most $1$; the map $\boldsymbol{p} \mapsto (1 - r)W\boldsymbol{p} + r\boldsymbol{p}_0$ is a contraction in the $\ell_1$ norm with factor $1 - r < 1$, and by the Banach fixed-point theorem the iteration converges to its unique fixed point. The fixed point satisfies $(I - (1 - r)W)\boldsymbol{p} = r\boldsymbol{p}_0$, and $I - (1 - r)W$ is invertible because $(1 - r)W$ has spectral radius below $1$ (its inverse is the Neumann series $\sum_t(1 - r)^tW^t$). $\square$

This is personalized **PageRank** ([1.4.7](/1.4.7#sec-7.6.3)), with teleportation to the seeds instead of to all vertices, and the expansion $\boldsymbol{p} = r\sum_t(1 - r)^tW^t\boldsymbol{p}_0$ shows that it sums walks of every length from the seeds, each weighted geometrically. Diffusion gives the continuous-time analog: heat placed on the seeds and flowing along edges is distributed after time $t$ as $\boldsymbol{h}(t) = \mathrm{e}^{-tL}\boldsymbol{h}_0$, the **heat kernel** of the **Laplacian matrix** $L = K - A$ ([1.4.7](/1.4.7#sec-7.8.3)), computed with the **matrix exponential**.

**Example 12.4.2** On a path $a$–$b$–$c$ with seed $a$ and $r = 0.5$, Formula 12.4.1 gives $\boldsymbol{p} = (0.583, 0.333, 0.083)$: the seed keeps more than half of the probability, its neighbor a third, and the vertex at distance two a twelfth. A larger $r$ keeps the scores closer to the seeds, a smaller $r$ spreads them farther; values of $r$ between $0.2$ and $0.5$ are common.

![Network propagation on a simulated network of 40 proteins grown by preferential attachment (two edges per new protein), with three seed proteins (thick blue outline). A: the visiting probability p of a random walk with restart (r = 0.3, Formula 12.4.1), on a logarithmic color scale. B: z-scores of the same values against 1000 random seed sets with matching degrees. The hub (degree 14, a neighbor of one seed) has the highest score after the seeds in A (p = 0.082), because many walks pass through it, but a z-score of only 0.52 in B; after the seeds, the highest z-score (1.04) belongs to a protein of degree 5 adjacent to a seed](./plots/propagation.py)

The figure shows the main pitfall. Without restart, the stationary distribution of a random walk is proportional to degree ([1.4.7](/1.4.7#sec-7.8.3)), and with restart the scores of vertices far from the seeds still follow it. Hubs therefore score highly for any seed set, and a ranking by raw propagation scores rediscovers the hubs. Scores are made specific by comparing them with those obtained from random seed sets of the same degrees (as in panel B), by **degree-preserving randomization** of the network ([1.4.7](/1.4.7#sec-7.4.6)), or by dividing by the stationary distribution. Validation must also avoid circularity: if a disease gene was added to an interaction database because it was studied together with other disease genes, propagation will rediscover it for that reason alone; cross-validation by leaving out known genes, and networks from systematic screens rather than literature, address this.

:::

Propagation is used to predict gene function from annotated neighbors, to prioritize candidate disease genes in a linkage or association region by their proximity to known disease genes (Köhler, Bauer, Horn and Robinson, 2008; Vanunu, Magger, Ruppin, Shlomi and Sharan, 2010), to amplify weak signals from **genome-wide association studies** by smoothing gene scores over the network, and to find modules significantly hit by somatic mutations in cancer ([7.9.13](/7.9.13)); a review called it a universal amplifier of genetic associations (Cowen, Ideker, Raphael and Sharan, 2017).

## 12.5. Differential Networks

Networks change between conditions: the same factor regulates different genes in different cell types ([7.9.11](/7.9.11#sec-11.2.2)), and genetic interactions are rewired when cells are exposed to DNA damage (Bandyopadhyay and colleagues, 2010). Differential network analysis looks for edges that change rather than for genes whose level changes (de la Fuente, 2010; Ideker and Krogan, 2012). A pair of genes may be strongly coexpressed in healthy tissue and not in tumors, because the regulator that couples them is lost, while neither gene changes its mean expression.

**Formula 12.5.1 (Test for Differential Co-Expression)** Let $r_A$ and $r_B$ be the correlations of a pair of genes in independent samples of sizes $n_A$ and $n_B$. With the **Fisher z-transformation** $z = \operatorname{artanh} r$,
$$
Z = \frac{\operatorname{artanh} r_A - \operatorname{artanh} r_B}{\sqrt{1/(n_A - 3) + 1/(n_B - 3)}}
$$
is approximately standard normal under $H_0\colon \rho_A = \rho_B$ for bivariate normal data.

**Example 12.5.1** With $r_A = 0.8$, $r_B = 0.2$ and $n_A = n_B = 50$: $\operatorname{artanh} 0.8 = 1.099$, $\operatorname{artanh} 0.2 = 0.203$, the standard error is $\sqrt{2/47} = 0.206$, so $Z = 4.34$ and $p = 1.4 \times 10^{-5}$. Among the $2 \times 10^8$ pairs of $20\,000$ genes this would not survive a Bonferroni correction ($0.05/2 \times 10^8 = 2.5 \times 10^{-10}$); differential co-expression needs many samples, a restriction to candidate pairs or modules, or a test at the level of modules (for example comparing the mean correlation within a module).

:::

Correlations also differ between groups for reasons other than rewiring: a smaller range of expression in one group, from lower variance or fewer cell types, attenuates its correlations, and differences in cell-type composition create and destroy correlations in bulk data. Conditional networks computed within cell types from single-cell data, and the comparison of regulon activities ([7.9.11](/7.9.11#sec-11.7)) rather than of individual correlations, reduce these problems. Changing edges detected this way are hypotheses about altered regulation, to be tested by perturbing the presumed regulator in each condition.

## 12.6. Network Medicine

### 12.6.1. The Human Disease Network

Genes and diseases form a **bipartite graph**: a disease is linked to the genes whose mutations cause it. Goh and colleagues (2007) built this graph, the diseasome, from the catalog of Mendelian disorders (OMIM), with about $1300$ disorders and $1800$ disease genes, and studied its two projections.

**Formula 12.6.1 (Bipartite Projection)** Let $B$ be the $m \times n$ incidence matrix of a bipartite graph between diseases and genes ($B_{dg} = 1$ if gene $g$ is implicated in disease $d$). The disease network has the weighted adjacency $BB^{\mathsf T}$ with its diagonal removed, in which $(BB^{\mathsf T})_{dd'}$ is the number of genes shared by diseases $d$ and $d'$; the gene network has the adjacency $B^{\mathsf T}B$ without its diagonal, the number of diseases shared by two genes.

In the human disease network, disorders of the same class (cancers, neurological diseases, metabolic diseases) clustered together, and genes associated with the same disorder were more likely to interact physically, to be coexpressed and to share functional annotations. A finding that distinguishes disease genes from essential genes: essential genes tend to be hubs at the center of the interactome, whereas most disease genes are nonessential and lie at its functional periphery; mutations in central essential genes are more often lethal in embryos than causes of disease in adults. The network view also explains comorbidity: diseases that share genes, or whose genes interact, occur together in patients more often than expected (Barabási, Gulbahce and Loscalzo, 2011).

### 12.6.2. Disease Modules

If the genes of a disease interact, they should form a connected region of the interactome.

**Definition 12.6.1 (Disease Module)** A **disease module** is a connected subgraph of the interactome whose perturbation, by mutation, loss or altered expression of its members, causes or contributes to a disease; it is detected by the observation that the known genes of the disease are significantly more connected to each other than random genes of the same degrees.

Menche and colleagues (2015) combined physical interaction data into an interactome of $13\,460$ proteins and $141\,296$ interactions and asked, for each of $299$ diseases, whether the known disease genes form a largest connected component larger than expected for random gene sets with the same degrees; most did. Because the interactome is incomplete, the connected component of known genes is small, and the module is only partly observable; the size of the observed component depends on the coverage of the interactome, and percolation theory predicts that modules become visible only above a coverage threshold, which the then-current interactome had just reached for many diseases.

![Disease modules and drug proximity in a simulated interactome of 3000 proteins grown by preferential attachment (8994 interactions). A disease module of 60 proteins is planted as a connected region; only 30 of them, chosen at random, are known disease genes. A: the largest connected component of the 30 known genes (7 proteins, line) against 1000 random sets of 30 proteins with matching degrees (histogram, mean 2.1, standard deviation 0.84): z = 5.8. B: the closest distance d_c between the four targets of a drug and the known disease genes (Formula 12.6.2), for a drug whose targets lie in the module (blue, d_c = 1.00, z = −3.5) and a drug with random targets (red, d_c = 2.25, z = −0.2); the histogram shows 1000 degree-matched random target sets for the random drug (the null distribution of the module drug is similar, mean 2.16)](./plots/proximity.py)

The simulation shows why significance, not size, is the criterion. Only $7$ of the $30$ known genes are connected in the largest component, although all $60$ module genes are connected; but random sets give components of about $2$ proteins, so the observed $7$ is $5.8$ standard deviations above the mean. The relation between two diseases is measured by the separation of their modules,
$$
s_{AB} = \langle d_{AB}\rangle - \frac{\langle d_{AA}\rangle + \langle d_{BB}\rangle}{2},
$$
where $\langle d_{AA}\rangle$ is the mean over the genes of $A$ of the shortest distance to another gene of $A$, and $\langle d_{AB}\rangle$ the mean over the genes of both diseases of the shortest distance to a gene of the other. Negative separation means overlapping modules, and diseases with overlapping modules showed more similar symptoms, more shared pathways and higher comorbidity than diseases with separated modules (Menche and colleagues, 2015).

### 12.6.3. Drugs in the Network

A drug acts on its targets, usually several of them with different affinities, and its metabolites may act on others; its effect is the perturbation of the network around them. Drug–target networks, bipartite graphs between approved drugs and their target proteins, showed that most drugs target proteins already targeted by other drugs, and that targets of drugs for a disease tend to be near, but not identical with, the genes that cause it (Yıldırım, Goh, Cusick, Barabási and Vidal, 2007). Proximity in the interactome turns this into a quantitative prediction.

**Formula 12.6.2 (Network Proximity of a Drug to a Disease)** (Guney, Menche, Vidal and Barabási, 2016) For a drug with target set $T$ and a disease with gene set $S$, the closest distance is
$$
d_c(S, T) = \frac{1}{\lvert T\rvert}\sum_{t \in T}\min_{s \in S}d(s, t),
$$
with $d$ the shortest-path distance in the interactome. Its significance is the z-score $z = (d_c - \mu)/\sigma$ against the distances of random target and disease sets with matching degrees; $z$ well below $0$ indicates that the drug's targets are closer to the disease module than chance.

In the simulation, the drug with targets inside the module has $d_c = 1.00$, each target adjacent to a known disease gene, and $z = -3.5$; the drug with random targets has $d_c = 2.25$ and $z = -0.2$. In real data, drugs known to be effective for a disease were proximal to its module more often than other drugs, and proximity has been used to propose drug repurposing; for COVID-19, for instance, network proximity to the human proteins bound by viral proteins ([7.9.10](/7.9.10#sec-10.5.5)) was combined with diffusion and other predictors to rank candidate drugs for testing (Gysi and colleagues, 2021). Such rankings are hypotheses; as for the host–pathogen map itself, most candidates did not show clinical benefit. Expression signatures provide complementary evidence: drugs whose transcriptional effect reverses a disease signature in the **connectivity map** ([7.9.7](/7.9.7#sec-7.7.1)) are candidates independent of the interactome.

### 12.6.4. Multilayer Networks

Disease involves several kinds of relations at once: physical interactions, regulation, co-expression in the affected tissue, metabolic reactions. A multilayer network has one layer per kind of relation on the same set of genes, with edges between layers joining the copies of each gene. Random walks with restart generalize to such networks: the walker moves within a layer or jumps to the same gene in another layer, and its stationary distribution combines the evidence of all layers without collapsing them into one graph. Tissue-specific networks, in which the interactome is restricted to proteins expressed in a tissue, are the simplest case, and they explain part of the tissue specificity of diseases caused by ubiquitously expressed genes.

## 12.7. Network Alignment

Sequence alignment finds corresponding residues of two sequences ([7.8.3](/7.8.3)); network alignment finds corresponding vertices of two networks, typically the protein interaction networks of two species. A good correspondence pairs proteins with similar sequences (likely **orthologs**) that sit in similar network neighborhoods, and the conserved parts of the networks reveal complexes and pathways preserved by evolution; the alignment also transfers functional annotation from a well-studied species to a less studied one, more reliably than sequence similarity alone when proteins have several paralogs.

**Definition 12.7.1 (Network Alignment)** Given networks $G_1 = (V_1, E_1)$ and $G_2 = (V_2, E_2)$ and a similarity $S_{ij} \ge 0$ between vertices $i \in V_1$ and $j \in V_2$, a **network alignment** is a partial injective map $f\colon V_1 \to V_2$; a local alignment maps small conserved subnetworks, possibly many-to-many, and a global alignment maps as much of $V_1$ as possible, maximizing a combination of the vertex similarity $\sum_iS_{if(i)}$ and the number of conserved edges $\lvert\{(u, v) \in E_1 : (f(u), f(v)) \in E_2\}\rvert$.

Maximizing conserved edges alone over all bijections is a quadratic assignment problem: with $P$ a **permutation matrix**, maximize $\operatorname{tr}(A_1PA_2P^{\mathsf T})$, which includes subgraph isomorphism as a special case and is NP-hard. Alignment algorithms are therefore heuristics or relaxations, for instance optimizing over doubly stochastic matrices instead of permutations, with alternating projected gradient steps, and rounding at the end.

**Algorithm 12.7.1 (PathBLAST)** (Kelley and colleagues, 2003) Local alignment of pathways:

1. Build a global alignment graph whose vertices are pairs of proteins, one from each network, with at least weak sequence similarity (BLAST $E < 0.01$); join two pairs by an edge if the proteins interact in both networks (a conserved interaction), or if they interact in one and are within distance two in the other (a gap), or are dissimilar (a mismatch).
2. Score a path $P$ of the alignment graph by
$$
S(P) = \sum_{v \in P}\log\frac{p(v)}{p_{\mathrm{random}}} + \sum_{e \in P}\log\frac{q(e)}{q_{\mathrm{random}}},
$$
where $p(v)$ is the probability that the two proteins of $v$ are true homologs and $q(e)$ the probability that the interactions of $e$ are real, each compared with a random background.
3. Find the highest-scoring paths of fixed length (four in the original work) by dynamic programming on many acyclic subgraphs obtained by randomly orienting the edges, and assess their significance against alignments of randomized networks.

Applied to the networks of yeast and the bacterium *Helicobacter pylori*, PathBLAST found conserved pathways between species separated by more than a billion years; NetworkBLAST extended the idea to conserved complexes in several species (Sharan and colleagues, 2005).

**Formula 12.7.1 (IsoRank)** (Singh, Xu and Berger, 2008) Two vertices are similar if their neighbors are similar: with $N(i)$ the neighbors of $i$, the topological similarity $R_{ij}$ of $i \in V_1$ and $j \in V_2$ satisfies
$$
R_{ij} = \sum_{u \in N(i)}\sum_{v \in N(j)}\frac{R_{uv}}{\lvert N(u)\rvert\,\lvert N(v)\rvert},
$$
and with sequence information, in matrix form, $R = \alpha W_1RW_2^{\mathsf T} + (1 - \alpha)E$, where $W_k = A_kK_k^{-1}$ are the column-normalized adjacency matrices and $E$ the normalized sequence similarity. The fixed point is computed by power iteration; it is the stationary distribution of a random walk with restart on the product graph of $G_1$ and $G_2$, whose vertices are the pairs $(i, j)$. A one-to-one alignment is then extracted from $R$ greedily or by a maximum-weight assignment (the **Hungarian algorithm**).

![Global alignment of two small networks (illustrative). Network 2 (right in each panel) is network 1 (left) of a related species with one interaction lost (d–e), one gained and an extra protein g′. Sequence similarity identifies most orthologs, but two pairs of paralogs, a1/a2 and b1/b2, are equally similar to both candidate orthologs. A: alignment by sequence similarity alone (maximum-weight assignment), in which the ties between paralogs are broken arbitrarily, here both wrongly; green: correct pairs, red: wrong pairs. B: IsoRank (α = 0.6), which adds the similarity of neighborhoods and resolves the paralogs. Edge correctness EC, the fraction of the 11 edges of network 1 mapped onto edges of network 2: 0.45 and 0.91; since d–e has no counterpart, 10/11 = 0.91 is the maximum](./plots/isorank.py)

Alignments are evaluated topologically and biologically. Edge correctness, the fraction of edges of $G_1$ mapped onto edges of $G_2$, measures conserved topology; the size of the largest connected subgraph conserved by the alignment rewards coherent regions over scattered matches; the symmetric substructure score penalizes mapping sparse regions onto dense ones. Functional coherence, the fraction of aligned pairs that share GO annotations, tests whether the alignment is biologically meaningful. Topology-only aligners (GRAAL; Kuchaiev, Milenković, Memišević, Hayes and Pržulj, 2010) achieve high edge correctness with poor functional coherence, and sequence-only alignments the reverse, which is why combining both, as in IsoRank, works best. All such scores are limited by the incompleteness of the maps: an interaction missing in one species is more often missing from the map than from the cell.

## 12.8. Tools

### 12.8.1. A Cytoscape Analysis

Cytoscape (Shannon and colleagues, 2003) is the standard desktop tool for network analysis and visualization; its analyses are organized as a sequence of steps, shown here on its classic example, a yeast network of genes involved in galactose utilization with expression data from perturbation experiments (Ideker and colleagues, 2001).

| Step | Action | Result |
|---|---|---|
| Network | import an edge list (SIF format: source, interaction type, target) or a table | the graph, with node and edge tables |
| Attributes | import node tables keyed by gene identifier: gene names, expression ratios, p-values per condition | annotated network |
| Statistics | NetworkAnalyzer: degree, in- and out-degree, clustering coefficient, shortest paths, betweenness | node attributes and distributions |
| Style | map attributes to visual properties: in-degree to node size, expression ratio to a diverging fill color, p-value to border width | a figure that shows the data on the network |
| Layout | force-directed (organic) layouts for overview, hierarchical layouts for directed networks | readable drawings |
| Modules | apps: jActiveModules (Algorithm 12.4.1, subnetworks responding in several conditions), MCODE (Algorithm 12.3.1, dense complexes) | candidate modules |
| Enrichment | BiNGO or ClueGO: GO enrichment of a module against the network as background | functional interpretation |
| Selection | filters by attribute, first neighbors, paths between selected sets, sources and sinks of a directed network | subnetworks for follow-up |

Networks and their styles are shared through NDEx, the network data exchange (Pratt and colleagues, 2015), and Cytoscape can be driven from Python or R through its REST interface, which makes the analysis reproducible.

### 12.8.2. Programmatic Analysis

For larger analyses and pipelines, networks are analyzed in code: networkx (Python), igraph (C, with Python and R interfaces) and graph-tool for speed. The following code loads a STRING network ([7.9.10](/7.9.10#sec-10.5.1)), computes basic statistics and communities, propagates from seed genes with personalized PageRank, normalizes against degree-matched random seeds, and tests a module for enrichment.

```python
import numpy as np
import pandas as pd
import networkx as nx
from scipy.stats import hypergeom

# STRING edges: protein1, protein2, combined_score (0-1000)
edges = pd.read_csv("string_edges.tsv", sep="\t")
edges = edges[edges.combined_score >= 700]              # high-confidence interactions
G = nx.from_pandas_edgelist(edges, "protein1", "protein2")
G = G.subgraph(max(nx.connected_components(G), key=len)).copy()

deg = dict(G.degree())
btw = nx.betweenness_centrality(G, k=500, seed=0)       # sampled for large networks
comms = nx.community.louvain_communities(G, resolution=1.0, seed=0)
Q = nx.community.modularity(G, comms)

def rwr(G, seeds, r=0.3):
    """Random walk with restart = personalized PageRank with damping 1 - r."""
    pers = {v: (1.0 if v in seeds else 0.0) for v in G}
    return nx.pagerank(G, alpha=1 - r, personalization=pers)

def degree_matched(G, seeds, n_rand=200, n_bins=10, seed=0):
    """z-scores of propagation scores against random seeds with similar degrees."""
    rng = np.random.default_rng(seed)
    nodes = np.array(list(G))
    logk = np.log([deg[v] for v in nodes])
    bins = np.digitize(logk, np.quantile(logk, np.linspace(0, 1, n_bins + 1)[1:-1]))
    where = {v: b for v, b in zip(nodes, bins)}
    obs = pd.Series(rwr(G, seeds))
    null = []
    for _ in range(n_rand):
        rand = {rng.choice(nodes[bins == where[s]]) for s in seeds}
        null.append(pd.Series(rwr(G, rand)))
    null = pd.concat(null, axis=1)
    return (obs - null.mean(1)) / null.std(1)

def enrichment(module, annotated, background):
    """One-sided hypergeometric p-value of the overlap of a module with an annotation."""
    module, annotated = set(module) & background, set(annotated) & background
    x = len(module & annotated)
    return hypergeom.sf(x - 1, len(background), len(annotated), len(module))
```

## Summary

| Question | Method | Key formula or object | Caveat | Section |
|---|---|---|---|---|
| What does the network look like? | degree distributions, clustering, components | long-tailed out-degree, compact in-degree (transcription) | maps are biased samples | 12.1 |
| How robust is it? | random and targeted removal | percolation | map coverage changes the numbers (figure in 12.1.3) | 12.1.3 |
| Which proteins matter? | degree, betweenness | centrality–lethality (Definition 12.2.1), essential interactions (Formula 12.2.1) | cause is complex membership, not connectivity | 12.2 |
| Which groups act together? | community detection, MCODE (Algorithm 12.3.1), enrichment | modularity $Q$; hypergeometric test (Example 12.3.2) | resolution limit; background choice | 12.3 |
| Which region responds? | active subnetworks (Definition 12.4.1, Algorithm 12.4.1) | $z_A = \sum z_v/\sqrt{k}$ standardized | null in the same network | 12.4.1 |
| Which genes are near the seeds? | propagation (Definition 12.4.2) | $\boldsymbol{p} = r(I - (1 - r)W)^{-1}\boldsymbol{p}_0$ (Formula 12.4.1) | degree bias; circularity | 12.4.2 |
| Which edges change? | differential co-expression | Fisher $z$ test (Formula 12.5.1) | composition and range effects; multiple testing | 12.5 |
| Where is a disease? | disease modules (Definition 12.6.1) | largest component z-score; separation $s_{AB}$ | incomplete interactome | 12.6.2 |
| Which drugs might work? | proximity (Formula 12.6.2) | $d_c$ and its z-score | hypotheses only | 12.6.3 |
| What is conserved? | alignment (Definition 12.7.1), PathBLAST (Algorithm 12.7.1), IsoRank (Formula 12.7.1) | edge correctness, functional coherence | NP-hard; incomplete maps | 12.7 |

- Biological networks have heavy-tailed degree distributions and are robust to random failure but fragile under attack on hubs; in a simulated interaction network the giant component survives random removal of $84\,\%$ of the proteins but not targeted removal of $16\,\%$, and an incomplete map gives different numbers (12.1).
- Hubs are more often essential (Definition 12.2.1); the essential-interaction model (Example 12.2.1) and the concentration of essential genes in complexes explain the correlation without a topological role of hubs (12.2.1).
- Modules are found by community detection and dense-region methods (Algorithm 12.3.1), with modularity close to but not identical with the true partition (Example 12.3.1), and interpreted by enrichment against the network background (Example 12.3.2).
- Network propagation is personalized PageRank (Formula 12.4.1); its scores must be corrected for degree (the figure of 12.4.2).
- Differential co-expression needs many samples (Example 12.5.1) and care with composition effects (12.5).
- Disease genes form modules detectable as connected components larger than chance (the figure of 12.6.2); drugs close to a disease module (Formula 12.6.2) are candidates for repurposing (12.6).
- Network alignment combines sequence and neighborhood similarity; IsoRank resolves paralogs that sequence alone cannot (the figure of 12.7).

## Questions

1. Explain why a metabolic network in which ATP, ADP, water and NAD(H) are included as vertices has a different degree distribution and average path length from one in which they are removed. Which version is more appropriate for studying how metabolic pathways connect?

   **Answer** Currency metabolites participate in hundreds of reactions, so including them creates a few vertices of very high degree, a heavier tail of the degree distribution and very short paths: almost any two metabolites are connected through ATP or water in two steps. These paths are chemically meaningless, because the carbon skeleton does not pass through ATP. For studying the connectivity of pathways, one removes currency metabolites or uses atom-mapping to keep only edges that transfer carbon; the resulting network has longer, biochemically meaningful paths and a less extreme degree distribution.

2. A two-hybrid screen detects $20\,\%$ of the true interactions of a network uniformly at random. If a protein has $50$ true interactions, what are the mean and standard deviation of its observed degree? How does uniform sampling change the shape of a power-law degree distribution, and what kind of sampling changes it more?

   **Answer** The observed degree is $\mathrm{Bin}(50, 0.2)$: mean $10$, standard deviation $\sqrt{50 \times 0.2 \times 0.8} = 2.83$. Uniform edge sampling rescales degrees by $0.2$ and adds binomial noise; the tail of a power law keeps roughly its exponent for large degrees, but low-degree proteins lose all their interactions (a protein of degree $2$ is unobserved with probability $0.64$), so the observed network loses vertices and the distribution bends at small degrees. Non-uniform sampling changes the shape more: if well-studied proteins (or the baits of a screen) are sampled more completely, they become hubs of the map regardless of their true degree, and subnetworks of scale-free networks are not scale-free (12.1.2).

3. Using Formula 12.2.1 with $\alpha = 0.03$ and $\beta = 0.05$, compute the probability of essentiality for proteins with $2$ and $20$ interactions. If, in reality, essentiality depends only on membership in essential complexes, why would degree still be correlated with essentiality?

   **Answer** $k = 2$: $1 - 0.95 \times 0.97^2 = 1 - 0.95 \times 0.9409 = 0.106$. $k = 20$: $1 - 0.95 \times 0.97^{20} = 1 - 0.95 \times 0.5438 = 0.483$. Members of large stable complexes have many interactions, in particular in co-complex (AP-MS, matrix-expanded) data where each member of a complex of $s$ subunits gets degree at least $s - 1$; essential complexes such as the ribosome, RNA polymerase and the proteasome are large. Degree is therefore a proxy for membership in large complexes, and the correlation follows without a causal role for connectivity (Zotenko and colleagues, 2008).

4. In a network with $M = 62$ edges, a candidate module of $8$ proteins has $20$ internal edges and total degree $46$. Compute its contribution to the modularity $Q = \sum_c\bigl[e_c/M - (d_c/2M)^2\bigr]$, where $e_c$ is the number of internal edges and $d_c$ the total degree of community $c$. Is the module denser than expected?

   **Answer** $e_c/M = 20/62 = 0.323$; $(d_c/2M)^2 = (46/124)^2 = 0.1376$; contribution $0.185$. The expected number of internal edges for a random network with the same degrees is $M(d_c/2M)^2 = 62 \times 0.1376 = 8.5$, so the module has $20/8.5 = 2.3$ times more internal edges than expected; it is a strong community. Its internal density, $20/\binom{8}{2} = 0.71$, is also high, as expected for a complex.

5. Compute the random-walk-with-restart scores for a star network with center $c$ and three leaves $\ell_1, \ell_2, \ell_3$, seed $\ell_1$, and $r = 0.5$. Then explain the degree bias in a larger network.

   **Answer** Let $x$, $y$, $w$ be the scores of $\ell_1$, $c$ and each other leaf. Each leaf passes all its probability to $c$; $c$ passes a third to each leaf. Fixed point: $x = 0.5 \cdot y/3 + 0.5$, $w = 0.5 \cdot y/3$, $y = 0.5(x + 2w)$. Then $y = 0.5(0.5 + y/6 + y/3) = 0.25 + y/4$, so $y = 1/3$, $x = 0.5 + 1/18 = 0.556$, $w = 1/18 = 0.056$; the sum is $0.556 + 0.333 + 2 \times 0.056 = 1$. The center receives a third of the probability although it is not a seed, because every walk passes through it. In larger networks, high-degree vertices receive probability from many directions, roughly in proportion to their degree, so raw scores favor hubs for any seed set; z-scores against degree-matched random seeds or division by the stationary distribution (proportional to degree) remove this bias.

6. Two genes have correlation $0.6$ in $30$ healthy samples and $0.3$ in $30$ tumors. Test whether the correlation differs, and discuss two reasons other than rewiring that could produce such a difference.

   **Answer** $\operatorname{artanh} 0.6 = 0.693$, $\operatorname{artanh} 0.3 = 0.310$; standard error $\sqrt{2/27} = 0.272$; $Z = 1.41$, $p = 0.16$: not significant, $30$ samples per group cannot distinguish these correlations. Alternative explanations even for a significant difference: (i) different variance or range: if tumors have a narrower range of expression of one gene, its correlations are attenuated; (ii) composition: in bulk data, a correlation driven by varying proportions of a cell type that expresses both genes changes when the composition varies differently, for instance in tumors with different stromal content. Analyses within cell types or with adjustment for composition, and replication, are needed.

7. A disease has $40$ known genes, whose largest connected component in the interactome has $12$ genes; for $1000$ degree-matched random sets of $40$ genes, the mean is $4.1$ and the standard deviation $1.9$. Compute the z-score and explain why the component contains only a fraction of the known genes even if all of them belong to one disease module.

   **Answer** $z = (12 - 4.1)/1.9 = 4.2$: the genes are significantly connected, evidence for a disease module. Only $12$ of $40$ are connected because the interactome is incomplete: interactions among the disease genes are missing from the map, so the module breaks into pieces; and some known genes may act through relations (regulation, metabolism) not represented in a physical interactome. In the simulation of 12.6.2, all $60$ module genes are connected in the true network, but only $7$ of $30$ known genes form the largest component. As coverage of the interactome grows, the observed component grows, as percolation theory predicts.

8. Compute the closest distance $d_c$ (Formula 12.6.2) for a drug with targets $t_1$, $t_2$, $t_3$ whose shortest distances to the nearest disease gene are $1$, $2$ and $4$. If degree-matched random target sets give $\mu = 2.6$ and $\sigma = 0.4$, is the drug proximal? What would you need before proposing it for repurposing?

   **Answer** $d_c = (1 + 2 + 4)/3 = 2.33$; $z = (2.33 - 2.6)/0.4 = -0.67$: not significantly proximal. One target is adjacent to the disease module, which might matter if it is the main target; proximity based on the closest distance averages over all targets. Before proposing the drug: check which targets are bound at therapeutic concentrations, whether the effect on the targets would move the disease module in the right direction (activation or inhibition), transcriptional evidence (does the drug reverse the disease signature in the connectivity map), and clinical or epidemiological evidence; network proximity alone generates hypotheses.

9. In the IsoRank example, sequence similarity cannot distinguish the paralogs a1 and a2. Explain how the iteration $R = \alpha W_1RW_2^{\mathsf T} + (1 - \alpha)E$ resolves the ambiguity, and what happens with $\alpha = 0$ and with $\alpha$ close to $1$.

   **Answer** The term $W_1RW_2^{\mathsf T}$ gives the pair $(a1, a1')$ similarity from the similarity of its neighbors, $(c, c')$, $(d, d')$ and $(b1, b1')$, which are high because these proteins have unambiguous orthologs; the pair $(a1, a2')$ gets similarity from pairs such as $(c, e')$, which are low. After iteration, $R_{a1,a1'} > R_{a1,a2'}$ and the assignment is correct. With $\alpha = 0$, $R = E$ and the ambiguity remains (sequence only). With $\alpha$ close to $1$, sequence information is nearly ignored and $R$ approaches the dominant eigenvector of the product-graph walk, which depends only on topology: structurally equivalent vertices (for example the two symmetric halves of the network) become indistinguishable, and alignments can match proteins with unrelated sequences. Intermediate values combine both.

10. (Design problem) A GWAS of a complex disease yields $15$ genome-wide significant loci, each containing several genes. Outline a network-based analysis to prioritize causal genes and pathways, and how you would guard against artifacts.

    **Answer** (i) Gene scores: for each locus, map candidate genes by distance, eQTL colocalization and chromatin contacts ([7.9.8](/7.9.8)), and compute gene-level association statistics genome-wide (not only at significant loci). (ii) Network: a high-confidence interactome from systematic screens (to limit literature bias), optionally restricted to proteins expressed in the disease-relevant tissue. (iii) Propagation: smooth gene scores by random walk with restart or diffusion (Formula 12.4.1), and compute z-scores against degree-matched permutations or by permuting gene scores within degree bins; prioritize, at each locus, the gene with the highest propagated score. (iv) Modules: test whether the prioritized genes form a connected component larger than chance (12.6.2) and find active subnetworks (Algorithm 12.4.1); test modules for GO enrichment against the network background. (v) Guards: cross-validation by holding out loci and checking whether their genes are recovered from the others; comparison with a network-free baseline (nearest gene); checks that results do not merely follow degree or the number of publications per gene; and replication of modules in an independent cohort or with a second network. Experimental follow-up: perturbation of prioritized genes in a relevant cell type (CRISPR screens with disease-relevant readouts).
