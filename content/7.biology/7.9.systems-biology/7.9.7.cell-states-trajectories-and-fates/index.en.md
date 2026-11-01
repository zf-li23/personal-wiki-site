---
title: Cell States, Trajectories and Fates
description: "From snapshots of single cells to dynamics: cell states as attractors of a Waddington landscape and the archetypes of cells that divide tasks, pseudotime by trees, principal curves and diffusion maps, RNA velocity from unspliced and spliced counts (steady-state and dynamical models, failure modes), fate probabilities as absorption probabilities of Markov chains, lineage tracing with heritable barcodes, cell–cell communication from ligand–receptor expression with permutation tests, reprogramming and transdifferentiation with pioneer factors and network-based predictions of conversion factors (Mogrify, CellOracle), and perturbation atlases: the Connectivity Map, Perturb-seq and the prediction of perturbation effects."
---

A single-cell experiment ([7.9.5](/7.9.5)) records a snapshot: each cell is destroyed when it is measured, so the data contain no trajectory of any one cell. Yet tissues are full of processes in progress (stem cells differentiating, immune cells activating, tumor cells changing state), and a snapshot of thousands of asynchronous cells samples every stage of them at once. This chapter is about turning such snapshots into statements about dynamics and fate. We first make precise what a cell state is: a point in expression space, held stable by the regulatory network as an **attractor** of a landscape (7.1). We then order cells along trajectories by their similarity, the pseudotime methods (7.2), and obtain a direction of change from the ratio of unspliced to spliced transcripts, the RNA velocity (7.3). Heritable barcodes record which cells share an ancestor, giving lineage information that expression alone does not contain (7.4). Cells also act on one another, and ligand and receptor expression suggests which (7.5). Finally we turn from observing fates to changing them: the reprogramming of one cell type into another and the computational choice of the factors that do it (7.6), and atlases of the transcriptional effects of thousands of drugs and genetic perturbations (7.7). The dynamical systems behind landscapes are those of [7.6.33](/7.6.33) and [7.5.10](/7.5.10); the biology of differentiation, stem cells and reprogramming is in [7.3.24](/7.3.24); the spatial side of communication is in [7.9.6](/7.9.6).

## 7.1. Cell States and Landscapes

### 7.1.1. A State Is a Point, a Type Is an Attractor

The expression profile of a cell is a vector $\boldsymbol{x} \in \mathbb{R}^G$ of the levels of $G$ genes. Most of this space is never occupied: regulatory interactions constrain which combinations are possible, and the cells of an organism fill a few low-dimensional regions. In the language of dynamical systems, the regulatory network defines a flow $\dot{\boldsymbol{x}} = \boldsymbol{f}(\boldsymbol{x})$, and a stable cell type corresponds to an **attractor** of the flow: a state to which nearby states return after a perturbation ([7.6.33](/7.6.33)). Huang and colleagues (2005) gave experimental support for this picture: promyelocytic leukemia cells driven toward the neutrophil fate by two different chemicals followed different paths through expression space at first, then converged onto the same final profile.

The simplest network with two attractors is the **genetic toggle switch** ([7.6.33](/7.6.33#sec-33.3)): two genes that repress each other. With $x$ and $y$ in units of their repression thresholds and time in units of the protein lifetime,
$$
\frac{\mathrm{d}x}{\mathrm{d}t} = \frac{a}{1 + y^{n}} - x, \qquad \frac{\mathrm{d}y}{\mathrm{d}t} = \frac{a}{1 + x^{n}} - y. \tag{7.1}
$$
For $a = 3$ and $n = 2$ there are three fixed points: two stable ones at $(2.618, 0.382)$ and $(0.382, 2.618)$, where the Jacobian has eigenvalues $-1/3$ and $-5/3$, and a saddle at $(1.213, 1.213)$, with eigenvalues $0.191$ and $-2.191$. Pairs of mutually repressing transcription factors of this kind sit at many branch points of differentiation, for example PU.1 and GATA1 at the choice between the myeloid and erythroid lineages of blood ([7.6.33](/7.6.33#sec-33.3.3)).

### 7.1.2. The Quasi-Potential

Waddington (1957) drew development as a ball rolling down a landscape of branching valleys: the **Waddington landscape** ([7.3.24](/7.3.24#sec-24.7.4)). For a gradient system $\dot{\boldsymbol{x}} = -\nabla U(\boldsymbol{x})$ the landscape is literally the potential $U$ ([7.5.10](/7.5.10#sec-10.2)), but regulatory networks are not gradient systems: mutual repression produces flows with rotational parts that no potential describes. Noise rescues the picture. Gene expression is stochastic (**transcriptional bursts**, [7.2.22](/7.2.22#sec-22.5)), and a network with noise has a stationary probability density $p_{\mathrm{s}}(\boldsymbol{x})$ of states.

**Definition 7.1.1 (Quasi-Potential)** The *quasi-potential* of a stochastic dynamical system with stationary density $p_{\mathrm{s}}$ is $U(\boldsymbol{x}) = -\ln p_{\mathrm{s}}(\boldsymbol{x})$ (up to an additive constant). Its local minima are the most probable states, near the attractors of the deterministic flow, and the height of the barrier between two minima sets the rate of noise-driven transitions between them.

For a gradient system with isotropic noise of strength $\sigma$, $p_{\mathrm{s}} \propto \mathrm{e}^{-2U/\sigma^2}$, so the quasi-potential is the potential rescaled; for general networks it is the natural generalization (Wang, Xu and Wang, 2008). In a population sampled at steady state, the density of cells in expression space estimates $p_{\mathrm{s}}$, which makes the landscape, in principle, observable from a snapshot: valleys are where cells accumulate.

**Example 7.1.1** The figure simulates Eq. (7.1) with Gaussian noise. The two valleys of $U$ lie at the attractors, separated by a ridge through the saddle. Cells started at the saddle fall into one valley or the other at random. A small bias in the inputs, $a_x = a(1 + \delta)$ and $a_y = a(1 - \delta)$, tilts the landscape: with weak noise ($\sigma = 0.15$), $\delta = 0.02$ sends $77\,\%$ of the cells into the $x$-high valley and $\delta = 0.04$ sends $92\,\%$; with strong noise ($\sigma = 0.45$) the same biases give only $61\,\%$ and $70\,\%$. The decision of a bistable network amplifies small differences when noise is weak and becomes a graded, probabilistic choice when it is strong, the two regimes of fate specification discussed in [7.5.10](/7.5.10).

![A Waddington landscape from a two-gene toggle switch (simulated, Eq. (7.1) with a = 3 and n = 2, Langevin dynamics). A: the quasi-potential −ln p (Definition 7.1.1) estimated from the stationary distribution of 4000 cells with noise σ = 0.2; the valleys are the two attractors, separated by a saddle; thin lines are the nullclines; ten cells started at the saddle fall into one valley or the other (colored by the valley reached). B: the fraction of cells started at the saddle that end in attractor 1 when the inputs are biased by δ, for weak and strong noise](./plots/landscape.py)

The landscape metaphor has limits. The real state space has thousands of dimensions, of which a two-dimensional picture is a projection; the density of cells reflects not only stability but also how fast cells pass through a region and how they proliferate or die there; and attractors are an idealization for terminally differentiated cells, whereas progenitor states are often transient. Attractor networks with many stored states, the **Hopfield network** of [7.6.33](/7.6.33#sec-33.7), show how a single network can hold many cell types as separate minima.

### 7.1.3. Archetypes: Cells That Divide Tasks

Clustering ([7.9.5](/7.9.5#sec-5.5.3)) assumes that cells come in discrete groups. Within one cell type they often do not: their expression fills a continuum. Multi-objective optimality explains a particular shape for such continua. If a cell must perform several tasks and its performance in each falls with distance from an optimal profile for that task, the profiles that cannot be improved in all tasks at once, the **Pareto front** ([7.6.40](/7.6.40#sec-40.4.2)), fill the polytope whose vertices are the optimal profiles: a line segment for two tasks, a triangle for three, a tetrahedron for four (Shoval and colleagues, 2012).

**Definition 7.1.2 (Archetype)** In the Pareto task inference framework, an *archetype* is a vertex of the polytope enclosing the data in trait space (here, expression space), interpreted as the profile best at one task; *archetype analysis* finds $k$ vertices $\boldsymbol{a}_1, \dots, \boldsymbol{a}_k$ such that every data point is approximately a convex combination $\sum_j w_j\boldsymbol{a}_j$ with $w_j \ge 0$, $\sum_j w_j = 1$, and the vertices are themselves convex combinations of data points (Cutler and Breiman, 1994).

The number of vertices is chosen by how much the fit improves with each added vertex, and its significance is tested by comparing the volume of the fitted polytope with that of data whose coordinates are permuted independently (Hart and colleagues, 2015). The tasks are then read from the genes enriched in the cells nearest each vertex (**gene set enrichment analysis**, [7.9.3](/7.9.3)). Two examples:

- In *Escherichia coli*, the expression of the $200$ most active promoters across conditions lies near a line segment from a growth archetype (ribosomal genes) to a survival archetype (stress genes); the position on the line is set by the competition of two sigma factors for RNA polymerase, $\theta = \sigma^{\mathrm{S}}/(\sigma^{\mathrm{S}} + \sigma^{70})$.
- Single hepatocytes of the mouse liver fill a tetrahedron in the space of the first three principal components, with archetypes specialized in the secretion of blood proteins, gluconeogenesis, detoxification, and lipid metabolism with iron homeostasis (Adler and colleagues, 2019). The archetypes are arranged in space along the oxygen gradient of the liver lobule: oxygen-hungry synthesis near the portal vein, detoxification near the central vein, a spatial division of labor ([7.9.6](/7.9.6)).

A cell type is then not a point but a region of task allocations, and the question "which cluster?" becomes "which mixture of tasks?". The method has an artifact to watch: projections of high-dimensional noise and of data with few strong axes can look like polytopes, which is why the permutation test is needed.

## 7.2. Pseudotime and Trajectories

### 7.2.1. Ordering Cells by Similarity

When a process is asynchronous, cells at different stages are present in one sample, and cells at similar stages have similar profiles. Ordering cells along a path of small steps through expression space therefore orders them in developmental time, without any marker chosen in advance (Trapnell and colleagues, 2014).

**Definition 7.2.1 (Pseudotime)** The **pseudotime** of a cell is its position along an inferred trajectory through expression space, measured from a chosen starting cell or state: a monotone function of the progress of the cell through the process, not a time in hours.

Trajectory inference has two parts: a topology (a line, a tree with branch points, a cycle such as the cell cycle, or a graph with merging branches) and the position of each cell on it. Methods differ in both.

- Minimum spanning trees. The first version of Monocle reduced the cells to a few dimensions, built the **minimum spanning tree** ([1.4.3](/1.4.3)) of all cells, and took its longest path as the main trajectory; later methods build the tree on cluster centers (TSCAN, Slingshot) to make it robust to noise. Slingshot then fits a smooth principal curve through each lineage of the tree.
- Principal curves and graphs. A principal curve (Hastie and Stuetzle, 1989) is a smooth curve each point of which is the average of the data points that project onto it; Monocle 2 and 3 fit principal graphs, trees or general graphs that pass through the middle of the data, in a low-dimensional embedding.
- Random walks on the neighbor graph. Diffusion pseudotime (Haghverdi and colleagues, 2016) and Palantir (Setty and colleagues, 2019) measure progress by a distance that averages over all paths of a **random walk** between cells on the $k$-nearest-neighbor graph of [7.9.5](/7.9.5#sec-5.5.2), which is robust to noise and to gaps. PAGA (Wolf and colleagues, 2019) summarizes the connectivity between clusters by a graph whose edges are weighted by how many more neighbor-graph edges join two clusters than a random model predicts, which recovers trajectory topologies including loops.

A benchmark of $45$ methods on real and synthetic data sets (Saelens and colleagues, 2019) found that no method is best for all topologies: methods that assume a linear or bifurcating trajectory do well when the assumption holds and fail when it does not, and the predicted topology should be checked against known biology.

### 7.2.2. Diffusion Pseudotime

**Formula 7.2.1 (Diffusion pseudotime)** Let $W$ be the symmetric matrix of Gaussian affinities on the neighbor graph, $w_{ij} = \exp\bigl(-\lVert\boldsymbol{z}_i - \boldsymbol{z}_j\rVert^2/(\sigma_i^2 + \sigma_j^2)\bigr)$ (times a normalization) with local widths $\sigma_i$, and $T = D^{-1}W$ the transition matrix of the random walk, $D = \operatorname{diag}(\sum_j w_{ij})$. With the eigenvalues $1 = \lambda_0 > \lambda_1 \ge \lambda_2 \ge \cdots$ of $T$ and its right eigenvectors $\boldsymbol{\psi}_l$, the diffusion pseudotime of cell $j$ relative to a root cell $r$ is
$$
\operatorname{dpt}(r, j) = \Bigl[\sum_{l \ge 1}\Bigl(\frac{\lambda_l}{1 - \lambda_l}\Bigr)^2\bigl(\psi_l(r) - \psi_l(j)\bigr)^2\Bigr]^{1/2}, \tag{7.2}
$$
the Euclidean distance between the rows $r$ and $j$ of $\sum_{t \ge 1}T^t$, the transition probabilities accumulated over random walks of all lengths, minus their stationary part.

The weight $\lambda_l/(1 - \lambda_l) = \sum_{t \ge 1}\lambda_l^t$ emphasizes the slow eigenvectors, the large-scale structure of the data, and suppresses the fast ones, which carry noise. In practice the sum is truncated to the leading $10$–$20$ eigenvectors. Branch points are where cells that are close to the root become distant from each other, which DPT detects by comparing the orderings from different roots.

**Example 7.2.1** The figure simulates $900$ cells that differentiate from a progenitor state through a branch point into two fates. Diffusion pseudotime from the earliest cell correlates with the true time with Spearman $\rho = 0.971$; the leading eigenvalues of $T$ are $0.9968$, $0.9944$ and $0.976$, so the weights of Eq. (7.2) are $311$, $177$ and $41$. The minimum spanning tree of $12$ cluster centers recovers the branching skeleton. One lesson is in panel B: the pseudotime reaches $0.71$ at the end of fate A and $1.0$ at the end of fate B, although both branches last equally long in real time, because fate B changes more genes along the way. Pseudotime measures the distance traveled in expression space, not elapsed time, and is not comparable between branches.

![Pseudotime and fate probabilities on a simulated branching differentiation (900 cells, 80 genes following smooth programs of the true time, Poisson counts; 10 principal components, 15 nearest neighbors). A: cells in the first two principal components colored by diffusion pseudotime (Formula 7.2.1) from a root cell (star), with the minimum spanning tree of 12 k-means centroids. B: pseudotime against the true time, by branch. C: the probability of reaching the terminal cells of fate A (circled), computed as absorption probabilities of a random walk on the neighbor graph that may not step backward in pseudotime (Formula 7.3.3)](./plots/pseudotime.py)

### 7.2.3. Assumptions

Every pseudotime analysis rests on assumptions that the data cannot check by themselves:

1. The process is sampled densely enough that consecutive stages overlap; gaps (a fast transition, a lost population) break the trajectory or join unrelated states.
2. The direction is known: similarity is symmetric, so a root must be chosen from markers or from another source (velocity, 7.3; timed samples; lineage, 7.4).
3. Similar states are connected by real transitions. Two lineages that converge on similar profiles, or a population that sits between two others because it is a mixture or a **doublet**, produce false paths.
4. Variation unrelated to the process (cell cycle, stress, batch) has been removed or is weaker than the process.

Pseudotime therefore orders states; whether cells actually move along the inferred path in the stated direction needs dynamic information, which the next sections add.

## 7.3. RNA Velocity

### 7.3.1. Unspliced Transcripts Look Ahead

A transcript is first made as a pre-mRNA containing introns and is then spliced (**RNA splicing**, [7.2.16](/7.2.16)). Reads from introns, a few to twenty percent of the reads in droplet data, count the unspliced molecules. A gene that has just been induced has many unspliced molecules relative to spliced ones; a gene that has just been shut off has few. The ratio therefore tells in which direction the level of each gene is moving (La Manno and colleagues, 2018).

**Formula 7.3.1 (Splicing kinetics)** For one gene with transcription rate $\alpha(t)$, splicing rate $\beta$ and degradation rate $\gamma$ of the spliced mRNA, the numbers of unspliced and spliced molecules satisfy
$$
\frac{\mathrm{d}u}{\mathrm{d}t} = \alpha(t) - \beta u, \qquad \frac{\mathrm{d}s}{\mathrm{d}t} = \beta u - \gamma s. \tag{7.3}
$$
At constant $\alpha$ the steady state is $u^* = \alpha/\beta$, $s^* = \alpha/\gamma$, on the line $u = (\gamma/\beta)s$ through the origin of the $(s, u)$ plane.

**Definition 7.3.1 (RNA Velocity)** The **RNA velocity** of a gene in a cell is the time derivative of its spliced mRNA, $v = \mathrm{d}s/\mathrm{d}t = \beta u - \gamma s$, estimated from the measured unspliced and spliced counts; the vector of velocities over genes predicts the cell's expression a short time ahead, $\boldsymbol{s}(t + \Delta t) \approx \boldsymbol{s}(t) + \boldsymbol{v}\Delta t$.

Equation (7.3) is linear and solvable. If transcription switches on at rate $\alpha$ from $u = s = 0$, then $u(t) = (\alpha/\beta)(1 - \mathrm{e}^{-\beta t})$ and
$$
s(t) = \frac{\alpha}{\gamma}\bigl(1 - \mathrm{e}^{-\gamma t}\bigr) + \frac{\alpha}{\gamma - \beta}\bigl(\mathrm{e}^{-\gamma t} - \mathrm{e}^{-\beta t}\bigr) \qquad (\beta \ne \gamma),
$$
and when it switches off, both decay toward zero. In the $(s, u)$ plane the cells trace an almond-shaped loop: the upper arc during induction ($u$ rises first, so cells lie above the steady-state line and $v > 0$), the lower arc during repression (cells below the line, $v < 0$). This phase portrait is the basic diagnostic plot of velocity analysis.

### 7.3.2. Estimating Velocity

The rates are not known, and only ratios matter if time is left in arbitrary units ($\beta = 1$).

**Algorithm 7.3.1 (Steady-State Velocity)** (velocyto; La Manno and colleagues, 2018)

1. Count spliced and unspliced UMIs per gene and cell (exonic and intronic reads; velocyto, STARsolo `Velocyto`, alevin-fry), normalize by cell size and smooth each cell's values by averaging over its $k$ nearest neighbors (moments).
2. For each gene, assume that the cells with the most extreme values (for example the top and bottom $5\,\%$ in both $u$ and $s$) are near steady state, and fit the slope $\hat\gamma$ of $u = \hat\gamma s$ through the origin by least squares on them.
3. The velocity of each cell is $v = u - \hat\gamma s$: positive above the line, negative below.
4. Combine genes: for each cell $i$ and neighbor $j$, compare the velocity vector with the displacement $\boldsymbol{s}_j - \boldsymbol{s}_i$ by their cosine correlation $c_{ij}$, and form transition probabilities $\pi_{ij} \propto \exp(c_{ij}/\sigma)$; projected onto a two-dimensional embedding, the expected displacement $\sum_j \pi_{ij}(\boldsymbol{e}_j - \boldsymbol{e}_i)$ gives the arrows of the familiar velocity plots.

The dynamical model of scVelo (Bergen and colleagues, 2020) drops the steady-state assumption: it fits $\alpha$, $\beta$, $\gamma$ and the switching time of each gene, and assigns each cell a latent time on the gene's trajectory, by an expectation–maximization algorithm (**EM algorithm**) that alternates between assigning cells to times on the induction or repression arc and refitting the rates. A shared latent time across genes, a pseudotime with a direction, follows.

**Example 7.3.1** In the figure, a gene is induced for $10\,\mathrm{h}$ at $\alpha = 2$ with $\beta = 1$ and $\gamma = 0.3\,\mathrm{h}^{-1}$: the steady state would be $u^* = 2$, $s^* = 6.7$, but after $10\,\mathrm{h}$ the spliced level has reached only $6.2$, since its half-life is $\ln 2/0.3 = 2.3\,\mathrm{h}$ against $0.69\,\mathrm{h}$ for the unspliced RNA. With Poisson sampling noise, the steady-state fit of $600$ cells gives $\hat\gamma = 0.377$ instead of $0.3$, because the extreme cells of the induction arc have not reached steady state, and the sign of the estimated velocity agrees with the true sign of $\mathrm{d}s/\mathrm{d}t$ in $80\,\%$ of the cells. Errors concentrate near the steady-state line, where the true velocity is small.

![RNA velocity of one gene (simulated: β = 1, γ = 0.3 per hour, transcription on at α = 2 for 10 h, then off; 600 cells at random times, Poisson counts). A: the phase portrait of unspliced against spliced molecules, with the induction (upper) and repression (lower) arcs, the true trajectory, the steady-state slope fitted to the extreme cells (Algorithm 7.3.1, dashed) and the velocities of some cells (arrows). B: the same cells against true time. C: two subpopulations with different degradation rates (0.3 and 0.9 per hour) share one fitted slope, and many cells receive a velocity of the wrong sign (circled)](./plots/rna_velocity.py)

### 7.3.3. When Velocity Fails

The model of Eq. (7.3) assumes constant splicing and degradation rates for each gene across all cells, a single switch of transcription, and that unspliced counts reflect unspliced molecules. Each assumption fails in real data (Bergen, Soldatov, Kharchenko and Theis, 2021):

- Different kinetics in different lineages. If a gene is degraded faster in one population, the pooled fit gives one slope between the two, and cells of both populations get wrong velocities. In panel C of the figure, the pooled slope is $0.41$ for subpopulations with $\gamma = 0.3$ and $0.9$; $23\,\%$ of the slow and $54\,\%$ of the fast cells receive a velocity of the wrong sign. Such multiple kinetics are common in hematopoiesis and the immune system.
- Transcriptional boosts. In erythroid maturation, a group of genes increases its transcription rate in mid-trajectory; their phase portraits curve upward and the steady-state model reverses the inferred direction (Barile and colleagues, 2021).
- Technical origins of intronic reads: internal priming of oligo(dT) on intronic A-rich stretches, retained introns and nuclear RNA all contribute "unspliced" counts without the meaning the model assumes.
- Low counts. Most genes have too few unspliced UMIs for a phase portrait; the result rests on a few hundred dynamic genes and on the smoothing over neighbors, which itself borrows the structure of the embedding, and projected arrows on a UMAP can look coherent even when the underlying velocities are not.

Velocity is most trustworthy when phase portraits of known genes show clear arcs, when the inferred direction agrees with markers of early and late states, and when it is confirmed by timed samples or metabolic labeling. In metabolic labeling (scSLAM-seq, sci-fate, scEU-seq), a pulse of 4-thiouridine marks newly made RNA, so new and old transcripts are distinguished chemically rather than through splicing, with a known labeling time that gives rates in absolute units (the bulk version is in [7.9.4](/7.9.4)).

### 7.3.4. From Velocity to Fate Probabilities

A direction of change turns the neighbor graph into a directed Markov chain, and the question "where will this cell go?" becomes a question about where the chain ends.

**Formula 7.3.2 (Velocity kernel)** (CellRank; Lange and colleagues, 2022) The transition probabilities from cell $i$ to its neighbors $j$ combine the velocity kernel $\pi_{ij}$ of Algorithm 7.3.1 with a connectivity kernel $w_{ij}/\sum_k w_{ik}$ from expression similarity,
$$
T_{ij} = (1 - \lambda)\,\pi_{ij} + \lambda\frac{w_{ij}}{\sum_k w_{ik}}, \tag{7.4}
$$
with a small weight $\lambda$ (for example $0.2$) that keeps the chain connected where velocities are noisy. Other kernels replace velocity by pseudotime (only transitions that do not go back in pseudotime, as in Palantir), by experimental time points (optimal transport between consecutive samples, Waddington-OT), or by metabolic labeling.

The terminal states are sets of cells where the chain stays, recognized as macrostates of the Markov chain (by a generalized Schur decomposition that groups slowly mixing cells, GPCCA) or chosen from markers. Making them absorbing, the fate probabilities follow from the theory of absorbing **Markov chains**.

**Formula 7.3.3 (Fate probabilities)** Order the cells so that the transient ones come first, and write the transition matrix as
$$
T = \begin{bmatrix} Q & R \\ O & I \end{bmatrix},
$$
with $Q$ the transitions among transient cells and $R$ those from transient cells into the terminal cells, grouped by terminal state. The probability that the chain started at transient cell $i$ is absorbed in terminal state $k$ is the entry $(i, k)$ of
$$
B = (I - Q)^{-1}R, \tag{7.5}
$$
and the expected number of steps before absorption is $(I - Q)^{-1}\boldsymbol{1}$.

**Proof** Let $b_{ik}$ be the absorption probability. Conditioning on the first step, $b_{ik} = \sum_{j \in \mathcal{T}} Q_{ij}b_{jk} + R_{ik}$, that is $B = QB + R$. If every transient cell can reach a terminal state, the spectral radius of $Q$ is below $1$, so $I - Q$ is invertible with $(I - Q)^{-1} = \sum_{t \ge 0}Q^t$, which gives Eq. (7.5). The same conditioning for the number of steps $m_i$ gives $\boldsymbol{m} = \boldsymbol{1} + Q\boldsymbol{m}$. $\square$

**Example 7.3.2** A progenitor state P stays with probability $0.5$ or moves to an intermediate state I; from I the chain returns to P with probability $0.2$, or is absorbed in fate A ($0.5$) or fate B ($0.3$). Then $Q = \begin{bmatrix} 0.5 & 0.5 \\ 0.2 & 0 \end{bmatrix}$, $R = \begin{bmatrix} 0 & 0 \\ 0.5 & 0.3 \end{bmatrix}$, $(I - Q)^{-1} = \begin{bmatrix} 2.5 & 1.25 \\ 0.5 & 1.25 \end{bmatrix}$ and both P and I reach A with probability $0.625$ and B with $0.375$; the expected numbers of steps to commitment are $3.75$ from P and $1.75$ from I. In the simulated branching data of Example 7.2.1, with a pseudotime-directed kernel, progenitor cells have fate probabilities near $0.44$ for fate A, and the probabilities sharpen after the branch point: $75\,\%$ of the cells within the first tenth of a branch, and all cells in its later part, have their larger probability for the branch they are on (figure in 7.2.2, panel C).

Fate probabilities make testable predictions: genes whose expression correlates with the probability of one fate among the still uncommitted cells are candidate drivers of the decision. They inherit all the weaknesses of the kernel, however; a probability computed from wrong velocities is precisely wrong.

## 7.4. Lineage Tracing

Expression similarity and velocity infer descent from states. *Lineage* is a different relation: which cells share a common ancestor. Two cells with similar profiles may come from different ancestors, and sister cells may diverge. Classical **lineage tracing** labels a cell and finds its descendants later ([7.5](/7.5)); single-cell methods make the label a sequence that is read together with the transcriptome, so that thousands of clones are followed at once.

**Definition 7.4.1 (Lineage Barcode)** A *lineage barcode* is a heritable DNA sequence, unique to a founder cell or acquired along a lineage, that is copied to all descendants and read out in single-cell sequencing, so that cells with the same barcode, or with barcodes sharing acquired marks, can be assigned to the same clone or subtree.

Three kinds of barcodes are used:

| Barcode | How it arises | Information | Examples |
|---|---|---|---|
| Static | a library of random sequences delivered by lentivirus, one per founder cell | clones (which cells share a founder) | LARRY, CellTag, TREX |
| Evolving | Cas9 introduces heritable insertions and deletions at an array of target sites over generations | a tree: cells sharing more edits are more closely related | GESTALT (McKenna and colleagues, 2016), scGESTALT, MEMOIR |
| Natural | somatic mutations, especially in mitochondrial DNA | trees in human tissue without engineering | mitochondrial variants (Ludwig and colleagues, 2019) |

Static barcodes need enough diversity that two founders rarely share one. With $D$ equally frequent barcodes and $n$ labeled founders, the probability that a founder shares its barcode with another is $1 - (1 - 1/D)^{n - 1} \approx 1 - \mathrm{e}^{-n/D}$: $1\,\%$ for $D = 10^6$ and $n = 10^4$. Real libraries are skewed, and their effective diversity, estimated from the barcode frequencies, is what enters the formula. Evolving barcodes reconstruct trees by the methods of phylogenetics ([7.8.6](/7.8.6)) applied to edit patterns, with the complications that edits saturate the array, that large deletions erase several sites at once, and that some edits recur independently.

The most informative design combines lineage with state at several times. In LARRY (Weinreb and colleagues, 2020), mouse hematopoietic progenitors were barcoded, a part of each clone was sequenced at once and the rest after further culture or transplantation: sisters of a progenitor sampled early revealed what its relatives eventually became. Early progenitors already showed fate biases that the transcriptome-based methods of 7.2 and 7.3 predicted only in part, which means either that the fate is decided by features not visible in mRNA (chromatin, protein, position) or that the methods miss information that is there. Lineage data are thus the ground truth against which trajectory methods are tested.

## 7.5. Cell–Cell Communication

### 7.5.1. Inferring Signals from Expression

Cells instruct one another by secreted factors, membrane-bound **ligands** and adhesion molecules ([7.1.14](/7.1.14)). Single-cell data measure the expression of ligands and **receptors** in each cell type, and databases of known pairs (CellPhoneDB, CellChatDB, OmniPath, with a few thousand curated interactions, many involving receptor complexes of several subunits) turn these into hypotheses about which types talk to which.

**Definition 7.5.1 (Cell–Cell Communication Analysis)** **Cell–cell communication** analysis infers, from the expression of ligands in sender cells and of their receptors in receiver cells, the pairs of cell types that may signal to each other through each ligand–receptor pair, with a score of interaction strength and a significance assessed against a null model of random cell labels.

**Formula 7.5.1 (Interaction scores)** For a ligand–receptor pair, let $L_i$ be the average expression of the ligand in cell type $i$ and $R_j$ that of the receptor in type $j$ (for a complex, the geometric mean or minimum over its subunits).

1. CellPhoneDB (Vento-Tormo and colleagues, 2018): the score is the mean $\frac{1}{2}(L_i + R_j)$ of the arithmetic means, set to zero if either is expressed in fewer than $10\,\%$ of the cells of its type.
2. CellChat (Jin and colleagues, 2021): the communication probability follows the law of mass action with saturation,
$$
P_{ij} = \frac{L_iR_j}{K + L_iR_j}, \tag{7.6}
$$
with $L$ and $R$ computed as trimeans $(Q_1 + 2Q_2 + Q_3)/4$ of the normalized expression, a robust average that is zero when fewer than about a quarter of the cells express the gene; further factors account for agonists, antagonists and co-receptors.

In both, significance comes from a permutation test: the cell-type labels are shuffled many times, the score is recomputed each time, and the p-value is the fraction of permuted scores at least as large as the observed one.

**Example 7.5.1** In the figure, type 1 expresses a ligand and types 2 and 3 its receptor, at different levels. The CellChat probabilities are $0.80$ for type 1 to type 2 and $0.64$ for type 1 to type 3, both above all of $1000$ permutations ($p = 0.001$, the smallest possible value with $1000$ permutations). Type 2 to type 2 gets $0.28$ with $p = 0.028$: the ligand's background expression of $0.3$ molecules per cell becomes a nonzero trimean, and with many pairs tested such marginal calls are false positives unless corrected for multiple testing. The saturation in Eq. (7.6) has a practical consequence: with $K = 0.5$, $L = 1.2$ and $R = 0.8$ give $P = 0.96/1.46 = 0.66$, and doubling the receptor raises it only to $0.79$.

![Scoring cell–cell communication from expression (simulated: four cell types of 150 cells; a ligand expressed mainly by type 1, its receptor by types 2 and, more weakly, 3). A: the CellChat communication probability (Formula 7.5.1) for each sender–receiver pair; stars mark pairs above 99 % of 1000 permutations of the cell labels. B: the permutation null distributions for two pairs and their observed values](./plots/communication.py)

### 7.5.2. What These Scores Mean

A high score means that the genes are expressed, not that signaling happens. mRNA levels of secreted proteins and receptors correlate imperfectly with protein, processing and activity; most ligands act only over short distances, and two cell types in different parts of a tissue do not communicate however high their score; and the downstream response is not checked. Comparisons of methods applied to the same data found that their top predictions overlap little (Dimitrov and colleagues, 2022), so results should be read as ranked hypotheses. Three kinds of extra evidence strengthen them:

- Response in the receiver: methods such as NicheNet score a ligand by whether its known target genes are induced in the receiver cells, which turns "can signal" into "seems to have signaled".
- Physical proximity: cells that touch can be caught together. Sequencing of physically interacting cell pairs (ProximID, Boisset and colleagues, 2018; PIC-seq) and counting of contacts in images both compare the observed number of contacts between two types with a null distribution from shuffled labels or randomly placed cells. In mouse bone marrow, mature neutrophils were found next to megakaryocytes more often than expected by chance, which imaging then confirmed.
- Spatial data: in spatial transcriptomics, a ligand and its receptor should be expressed in neighboring cells. Spatially constrained versions of these scores and the corresponding permutation tests are treated in [7.9.6](/7.9.6).

## 7.6. Reprogramming and Transdifferentiation

### 7.6.1. Changing the Attractor

If cell types are attractors held by networks of transcription factors, forcing the factors of another type should move a cell into its valley. Three experiments established that it does. In 1987, Davis, Weintraub and Lassar found that a single cDNA, *MyoD*, converts fibroblasts into myoblasts. In 2006, Takahashi and Yamanaka converted mouse fibroblasts into **induced pluripotent stem cells** with four factors, Oct4, Sox2, Klf4 and c-Myc (human cells followed in 2007; the Nobel Prize was awarded to Gurdon and Yamanaka in 2012). From 2010, **transdifferentiation** without passage through pluripotency was achieved for several targets: induced neurons from fibroblasts with Ascl1, Brn2 and Myt1l (Vierbuchen and colleagues, 2010), cardiomyocyte-like cells with Gata4, Mef2c and Tbx5 (Ieda and colleagues, 2010), and hepatocyte-like cells with Hnf4a and a Foxa factor (2011). The cell biology of these conversions is in [7.3.24](/7.3.24#sec-24.7); here we ask what the factors have in common and how they can be predicted.

Most reprogramming factors can open closed chromatin. A *pioneer factor* is a transcription factor that binds its motifs on nucleosomal DNA, in compacted chromatin not accessible to most factors, and makes the region accessible to others (Zaret and Carroll, 2011); FoxA, GATA, Ascl1 and the trio Oct4–Sox2–Klf4 bind such sites early in reprogramming. The other factors of a cocktail then stabilize the new network, often by positive feedback among themselves, while the network of the starting cell must be silenced. Conversion is inefficient (often a few percent of the cells), the resulting cells are frequently immature or partially converted, and many cells stall in intermediate states: in landscape terms, barriers are high and the new valley is shallow when only part of the network is supplied.

Small molecules can do the same job. Chemically induced pluripotent stem cells were obtained from mouse fibroblasts with a cocktail of seven compounds (Hou and colleagues, 2013) and from human cells by a stepwise chemical protocol (Guan and colleagues, 2022). The compounds act on signaling pathways and chromatin enzymes rather than as transcription factors, which suggests that the route through intermediate states matters as much as the end point. Single-cell profiling of these routes identified a transient, regeneration-like intermediate state in the human protocol, an example of trajectory methods (7.2–7.3) applied to engineered transitions.

### 7.6.2. Predicting Conversion Factors from Networks

Choosing factors for a new conversion by trial would mean testing combinations of about $1600$ human transcription factors. Computational methods rank candidates from expression data of the source and target cell types and a network of regulatory interactions.

**Algorithm 7.6.1 (Network-Based Ranking of Conversion Factors)** (Mogrify; Rackham and colleagues, 2016) Given expression profiles of the target cell type and of a background of other cell types (or of the source type), and a directed network of regulatory and protein interactions (from motif-based regulatory predictions and STRING, [7.9.10](/7.9.10)):

1. Gene score. For each gene $y$, test differential expression between the target and the background (DESeq-type models, [7.9.2](/7.9.2)) and set $G_y = \lvert\log_2\mathrm{FC}_y\rvert \cdot (-\log_{10}p_y)$, a combination of effect size and significance.
2. Network score. For each transcription factor $x$, sum the gene scores of its regulatory neighborhood up to a few steps, each weighted down by its level $\ell_y$ (distance from $x$) and by the out-degree $O_y$ of its parent:
$$
N_x = \sum_{y \in V_x}\frac{G_y}{\ell_y O_y}.
$$
3. Rank the factors by the sum of their ranks in $G$ and in $N$: a good candidate is itself specific to the target and regulates many genes specific to it.
4. Remove redundancy: going down the ranking, drop a factor whose regulated genes are already almost entirely covered by the factors above it, so that the selected set covers the identity genes of the target with few factors.

The cost is dominated by the neighborhood sums, $O(F \cdot \bar d^{\,\ell})$ for $F$ factors with mean out-degree $\bar d$ and depth $\ell$.

**Example 7.6.1** Take four factors and six target genes, with gene scores $G$ from fold changes and adjusted p-values: $T_1$ ($\log_2\mathrm{FC} = 3$, $p = 10^{-8}$, $G = 24$), $T_2$ ($1.5$, $10^{-3}$, $4.5$), $T_3$ ($0.5$, $0.2$, $0.35$), $T_4$ ($2$, $10^{-2}$, $4$), and genes $g_1, \dots, g_6$ with $G = 40, 31.5, 15, 0.04, 21, 0.09$. Let $T_1$ regulate $g_1$, $g_2$ and $T_2$; $T_2$ regulate $g_3$; $T_3$ regulate $g_1$, $g_2$, $g_3$, $g_5$; and $T_4$ regulate $g_4$, $g_5$, $g_6$. Then $N_{T_1} = (40 + 31.5 + 4.5)/3 + 15/(2 \cdot 1) = 32.8$, $N_{T_2} = 15$, $N_{T_3} = (40 + 31.5 + 15 + 21)/4 = 26.9$ and $N_{T_4} = 7.0$. The rank sums are $2$ ($T_1$), $5$ ($T_2$), $6$ ($T_3$) and $7$ ($T_4$). $T_3$, hardly induced itself, ranks second in the network score because its targets are; this is how the method finds factors that are expressed in both cell types but act differently. Its targets overlap those of $T_1$ except $g_5$, so it is kept as covering an additional identity gene.

Mogrify predicted known conversions and new ones, two of which were confirmed, including the conversion of dermal fibroblasts into keratinocytes. CellOracle (Kamimoto and colleagues, 2023) takes a dynamic view: it infers a cell-type-specific gene regulatory network from single-cell RNA and chromatin accessibility data ([7.9.8](/7.9.8), [7.9.11](/7.9.11)), simulates the shift in expression caused by knocking out or overexpressing a factor by propagating the change through the linear network for a few steps, and compares the simulated shift with the developmental flow on the neighbor graph, predicting whether the perturbation pushes cells toward or away from a fate. Both approaches inherit the incompleteness of the networks they use, and their predictions are starting points for experimental screens, now often run by CRISPR activation of candidate factors (**CRISPR activation**, [7.2.24](/7.2.24)).

## 7.7. Perturbation Atlases

### 7.7.1. The Connectivity Map

A cell state can be described by a signature, the genes going up and down compared with a reference state. If a drug produces the reverse of a disease signature, it may counteract the disease; if it produces the same signature as a known drug, it may share its mechanism.

**Definition 7.7.1 (Connectivity Map)** A **connectivity map** is a reference database of transcriptional profiles of cells treated with many perturbations (small molecules, gene knockdowns or overexpression), together with a method that scores the similarity of a query signature to each reference profile, positive for profiles that mimic the query and negative for profiles that reverse it.

The first Connectivity Map (Lamb and colleagues, 2006) profiled cell lines treated with a few hundred compounds on microarrays. Its successor, the L1000 platform (Subramanian and colleagues, 2017), measures $978$ landmark transcripts by a cheap bead-based assay and infers most of the rest from them, which made more than a million profiles affordable, across many cell lines, doses and times, with compounds, short hairpin RNAs and overexpression constructs.

**Algorithm 7.7.1 (Connectivity Score)** (Lamb and colleagues, 2006) A reference profile ranks all $n$ genes from most induced to most repressed by its perturbation. For a query with up genes $S_{\mathrm{up}}$ and down genes $S_{\mathrm{down}}$:

1. For a set $S$ of $t$ genes with sorted ranks $V(1) < \dots < V(t)$ in the reference, compute $a = \max_j\bigl[j/t - V(j)/n\bigr]$ and $b = \max_j\bigl[V(j)/n - (j - 1)/t\bigr]$, and set $\mathrm{ks}(S) = a$ if $a > b$, else $-b$: the signed maximal deviation of a **Kolmogorov–Smirnov test** of the set's ranks against uniform.
2. The raw score is $\mathrm{ks}(S_{\mathrm{up}}) - \mathrm{ks}(S_{\mathrm{down}})$ if the two have opposite signs, and $0$ otherwise: a reference connects only if the up genes go one way and the down genes the other.
3. Scale the raw scores of all references to $[-1, 1]$ by the largest positive and the most negative value (later versions normalize by the distribution of scores of random or matched profiles), and rank perturbations by score.

The running sums are the same as those of the **enrichment score** of gene set enrichment analysis ([7.9.3](/7.9.3)), without weights.

**Example 7.7.1** In the figure, a query of $100$ up and $100$ down genes is scored against references of $10\,000$ ranked genes. A reference that mimics the query gives $\mathrm{ks}_{\mathrm{up}} = +0.431$ and $\mathrm{ks}_{\mathrm{down}} = -0.410$, a raw score of $+0.841$; a reversing one gives $-0.871$. Among $2000$ random references, $49\,\%$ score exactly $0$ because the two sets deviate in the same direction, and $99\,\%$ have $\lvert\text{score}\rvert < 0.26$; references with half the shift score on average $+0.48$ and $-0.47$, all beyond $0.35$ in absolute value. The zero rule makes the score conservative but produces a spike in the null distribution, so significance is assessed by permutation.

![The connectivity score (Algorithm 7.7.1) on simulated profiles: a query of 100 up and 100 down genes against references ranking 10000 genes. A: running sums for a reference that mimics the query: the up set (red) deviates early, the down set (blue) late. B: a reference that reverses the query. C: scores of 2000 random references and of 20 weaker mimicking and 20 weaker reversing references (logarithmic axis)](./plots/cmap_score.py)

Reversal of disease signatures has suggested candidates for drug repurposing that were then tested in animal models, but most such predictions do not survive: cell lines differ from the diseased tissue, and a reversed signature need not reverse the disease. The method is better at recognizing mechanisms (compounds with the same target give similar profiles) than at curing.

### 7.7.2. Perturb-seq

Pooled CRISPR screens ([7.2.24](/7.2.24#sec-24.7)) read out a single phenotype, usually growth. Perturb-seq (Dixit and colleagues, 2016; Adamson and colleagues, 2016) and CROP-seq read the whole transcriptome: each cell receives a **single guide RNA** of a library, the guide or a barcode linked to it is captured in the same droplet as the cell's mRNA, and the expression profile of every cell is linked to its perturbation. A genome-scale experiment perturbed every expressed gene in a human leukemia cell line by **CRISPR interference** and profiled more than $2.5$ million cells (Replogle and colleagues, 2022).

The analysis groups cells by guide and compares them with cells carrying non-targeting guides, gene by gene, with the count models and **pseudobulk** reasoning of [7.9.5](/7.9.5#sec-5.6.3); it must deal with cells that received two guides or none, with guides that fail (a mixture of perturbed and unperturbed cells within one guide, resolved by mixture models), and with the cell cycle and other confounders. The result is a matrix of perturbation effects, perturbations by genes, whose clustering groups genes into complexes and pathways by the similarity of their knockdown phenotypes, the transcriptional analog of the genetic-interaction profiles of [7.9.10](/7.9.10).

### 7.7.3. Predicting Perturbations

If a model could predict the effect of any perturbation, or combination, in any cell type, experiments could be chosen in silico. Two kinds of models are being tested. Foundation models pretrained on tens of millions of single-cell profiles (Geneformer, scGPT) represent each cell as a sequence of gene tokens and can be fine-tuned to predict the profile after a gene is deleted or overexpressed; dedicated models (GEARS, CPA) combine a learned latent space with a gene-interaction graph or with compound embeddings. The vision is often called a virtual cell.

The benchmarks so far are sobering. On held-out single and double perturbations from Perturb-seq data, several deep-learning models did not predict the expression changes better than simple linear baselines, such as adding the effects of the two single perturbations to predict a double one (Ahlmann-Eltze, Huber and Anders, 2025). Part of the problem is the data: most perturbations in a given cell type have small effects, many measured effects are dominated by a generic stress response common to all perturbations, and the metrics used can reward predicting the average. Predicting perturbation effects is thus an open problem, and the evaluation of a model against a trivial baseline is the first thing to check in any claim of success.

## Summary

| Question | Model or method | Key point | Section |
|---|---|---|---|
| What is a cell type? | attractor of a regulatory network; quasi-potential $U = -\ln p_{\mathrm{s}}$ (Definition 7.1.1) | small biases decide fates when noise is weak (Example 7.1.1) | 7.1.1–7.1.2 |
| Continua within a type | archetypes on a Pareto front (Definition 7.1.2) | vertices are task specialists (hepatocytes, *E. coli*) | 7.1.3 |
| Order of cells | pseudotime (Definition 7.2.1): trees, principal curves, diffusion pseudotime (Formula 7.2.1) | orders states, not times; not comparable between branches (Example 7.2.1) | 7.2 |
| Direction of change | RNA velocity (Formula 7.3.1, Definition 7.3.1, Algorithm 7.3.1) | fails with multiple kinetics, boosts, few counts | 7.3.1–7.3.3 |
| Where cells go | Markov chain kernels (Formula 7.3.2), absorption probabilities $B = (I - Q)^{-1}R$ (Formula 7.3.3) | inherits the errors of the kernel | 7.3.4 |
| Who descends from whom | lineage barcodes (Definition 7.4.1): static, evolving, natural | ground truth for trajectory methods | 7.4 |
| Who talks to whom | ligand–receptor scores (Definition 7.5.1, Formula 7.5.1) with permutation tests | expression is not signaling; add response, proximity, space | 7.5 |
| Changing a fate | pioneer factors; network ranking of factors (Algorithm 7.6.1); CellOracle | predictions are hypotheses for screens | 7.6 |
| Effects of perturbations | connectivity map (Definition 7.7.1, Algorithm 7.7.1), Perturb-seq | prediction models must beat linear baselines | 7.7 |

A snapshot contains states; dynamics come from models (velocity, Markov chains) or from extra measurements (labeling, lineage, time courses, perturbations), and conclusions about fate are only as good as the assumptions that bridge the two.

## Questions

1. For the toggle switch of Eq. (7.1) with $a = 3$ and $n = 2$, verify that $(x, y) = (\phi^2, \phi^{-2})$ with $\phi = (1 + \sqrt 5)/2$ is a fixed point, and use the Jacobian eigenvalues given in 7.1.1 to estimate how long a cell takes to relax back to the attractor after a small perturbation, and how fast cells leave the neighborhood of the saddle.

   **Answer** $\phi^2 = 2.618$ and $\phi^{-2} = 0.382$. Check: $3/(1 + 0.382^2) = 3/1.1459 = 2.618$ and $3/(1 + 2.618^2) = 3/7.854 = 0.382$. At the attractor the eigenvalues are $-1/3$ and $-5/3$; the slow direction relaxes as $\mathrm{e}^{-t/3}$, a relaxation time of $3$ protein lifetimes. At the saddle the unstable eigenvalue is $0.191$, so deviations grow as $\mathrm{e}^{0.191t}$, a doubling time of $\ln 2/0.191 = 3.6$ lifetimes: a cell near the saddle lingers for several lifetimes before committing, which is why intermediate states are observed in snapshots of decisions.

2. In a phase portrait with fitted slope $\hat\gamma = 0.3$ (and $\beta = 1$), cell 1 has $u = 1.5$, $s = 3$ and cell 2 has $u = 0.4$, $s = 4$. Compute their velocities and say what they imply. If the true $\gamma$ of cell 2's population were $0.05$, what would change?

   **Answer** Cell 1: $v = 1.5 - 0.9 = +0.6$, above the steady-state line, the gene is being induced. Cell 2: $v = 0.4 - 1.2 = -0.8$, below the line, the gene is being repressed. With $\gamma = 0.05$, cell 2's true velocity is $0.4 - 0.2 = +0.2$: it is still accumulating spliced mRNA, and the pooled slope assigns it the wrong sign. Populations with different degradation rates need separate fits (or a model with cell-type-specific kinetics), otherwise the arrows of the velocity plot point backward for one of them (Figure in 7.3.2, panel C).

3. Using Formula 7.3.3, compute the fate probabilities in Example 7.3.2 if the intermediate state I can also stay in place with probability $0.2$ (taking it from fate A, so that from I: $0.2$ to P, $0.2$ to I, $0.3$ to A, $0.3$ to B).

   **Answer** Now $Q = \begin{bmatrix} 0.5 & 0.5 \\ 0.2 & 0.2 \end{bmatrix}$, $R = \begin{bmatrix} 0 & 0 \\ 0.3 & 0.3 \end{bmatrix}$. $I - Q = \begin{bmatrix} 0.5 & -0.5 \\ -0.2 & 0.8 \end{bmatrix}$ with determinant $0.4 - 0.1 = 0.3$, so $(I - Q)^{-1} = \frac{1}{0.3}\begin{bmatrix} 0.8 & 0.5 \\ 0.2 & 0.5 \end{bmatrix}$. Then $B = (I - Q)^{-1}R$ has both rows equal to $(0.5/0.3)(0.3, 0.3) = (0.5, 0.5)$: since A and B are now entered with equal probability from I, the only exit, both fates are equally likely from both states. Expected steps: $(I - Q)^{-1}\boldsymbol{1} = (1.3/0.3, 0.7/0.3) = (4.33, 2.33)$.

4. A lentiviral barcode library has $2 \times 10^5$ distinct barcodes, but the $10\,\%$ most frequent make up half of the library. Estimate the fraction of founder cells that share their barcode with another when $5000$ founders are labeled, first assuming equal frequencies and then using the effective diversity $D_{\mathrm{eff}} = 1/\sum_k f_k^2$.

   **Answer** Equal frequencies: $1 - \mathrm{e}^{-5000/200\,000} = 1 - \mathrm{e}^{-0.025} = 2.5\,\%$. Skewed: $20\,000$ barcodes carry frequency $0.5/20\,000 = 2.5 \times 10^{-5}$ each and $180\,000$ carry $0.5/180\,000 = 2.78 \times 10^{-6}$; $\sum f_k^2 = 20\,000 \times 6.25 \times 10^{-10} + 180\,000 \times 7.7 \times 10^{-12} = 1.25 \times 10^{-5} + 1.39 \times 10^{-6} = 1.39 \times 10^{-5}$, so $D_{\mathrm{eff}} = 72\,000$ and the collision fraction is about $1 - \mathrm{e}^{-5000/72\,000} = 6.7\,\%$. Skew reduces the usable diversity almost threefold; collisions merge unrelated clones and must be removed, for example by requiring barcodes seen in only one founder sample or by using combinations of two barcodes.

5. For a CellChat-type score (Eq. (7.6), $K = 0.5$), the ligand is expressed in $30\,\%$ of type-1 cells at a high level and the receptor in $90\,\%$ of type-2 cells at a moderate level. Explain why the trimean-based score may be zero for this pair while a mean-based score is high, and when each behavior is desirable.

   **Answer** With $30\,\%$ of the type-1 cells expressing the ligand, its first quartile and median are $0$ and only the third quartile is positive (the $75$th percentile lies among the expressing cells, near their lowest values), so the trimean is $Q_3/4$, a small number; if $25\,\%$ or fewer cells expressed it, the trimean, and hence $P$, would be exactly $0$. A mean-based score counts the expressing minority fully and is high. The trimean protects against signals carried by a few contaminating or doublet cells; the mean captures genuine signals from a subpopulation (a rare sender within a type), at the cost of more false positives. Annotating the expressing subpopulation as a type of its own resolves the dilemma.

6. Why does the connectivity score of Algorithm 7.7.1 set the score to zero when the up and down sets deviate in the same direction? Give a biological situation that produces this pattern.

   **Answer** A meaningful connection requires that the reference moves the query's up genes and down genes in opposite directions, mimicking (up genes induced, down genes repressed) or reversing the signature. If both sets are near the top of the reference ranking, the reference induces many genes indiscriminately, for example a generic stress response, a proliferation signature or a high-dose toxic effect that increases the expression of many genes and of the variance; such a profile would correlate with any signature whose genes are stress-responsive, and counting it as a connection would give spurious hits. The zero rule removes them at the cost of a point mass in the null distribution (Example 7.7.1).

7. In Example 7.6.1, what happens to the ranking if $T_4$ is also found to regulate $g_1$ and $g_2$? Discuss what this implies about the reliability of network-based predictions.

   **Answer** $T_4$'s neighborhood becomes $g_1, g_2, g_4, g_5, g_6$ with out-degree $5$, so $N_{T_4} = (40 + 31.5 + 0.04 + 21 + 0.09)/5 = 18.5$. The network ranks become $T_1$ ($32.8$), $T_3$ ($26.9$), $T_4$ ($18.5$), $T_2$ ($15$), and with the unchanged expression ranks ($T_1$, $T_2$, $T_4$, $T_3$) the rank sums are $2$ for $T_1$ and $6$ for each of $T_2$, $T_3$ and $T_4$: a single added edge turns a clear order into a three-way tie. Predictions are only as good as the regulatory network, which is incomplete and mostly not specific to the cell type; this is why the output is a ranked list for experimental testing, and why newer methods infer cell-type-specific networks from chromatin data.

8. A Perturb-seq screen plans $2000$ guides (two per gene for $1000$ genes) plus $100$ non-targeting controls. Cells are infected at a low multiplicity so that $10\,\%$ receive a guide, guide capture succeeds in $80\,\%$ of the cells, and $100$ cells per guide are wanted. How many cells must be profiled, and what fraction of infected cells carries two guides?

   **Answer** With Poisson infection at mean $m$ and $\mathbb{P}(\ge 1) = 0.10$, $m = -\ln 0.9 = 0.105$; among infected cells the fraction with two or more guides is $(1 - \mathrm{e}^{-m} - m\mathrm{e}^{-m})/(1 - \mathrm{e}^{-m}) = (1 - 0.9 - 0.0948)/0.1 = 5.2\,\%$. Infected cells are selected (by antibiotic or a marker) before profiling, so the profiled cells are mostly infected: $2100 \times 100 = 210\,000$ assigned cells are needed, and with $80\,\%$ capture about $263\,000$ profiled cells; removing the $\approx 5\,\%$ with two guides raises this to about $277\,000$. At about $10\,000$ cells per channel this is some $28$ channels, which is why such screens use cell hashing and overloading ([7.9.5](/7.9.5#sec-5.3.3)).

9. (Analysis) A study infers from RNA velocity that a population of tumor cells dedifferentiates into a stem-like state. Which checks would you ask for before accepting this conclusion?

   **Answer** Inspect phase portraits of the driving genes for clear induction and repression arcs, and check whether the direction is driven by a few genes; test for multiple kinetics across cell populations (fit per cluster) and for transcriptional boosts; compare the dynamical model with the steady-state model and with a pseudotime from an independent root; examine the intronic reads for internal priming. Independent evidence: lineage tracing (barcoded cells sorted from the differentiated population, which should give rise to stem-like cells), metabolic labeling to measure new transcription directly, a time course, or functional assays (sorting the non-stem cells and observing re-emergence of the stem-like state in culture or in vivo).

10. (Design) Design an analysis to find transcription factors whose activation would convert fibroblasts into a target cell type for which single-cell data exist, and plan how to test the predictions.

    **Answer** Compute gene scores for target against fibroblasts and other types by pseudobulk differential expression with donors as replicates; build a regulatory network for the target from single-cell multiome data (accessible motifs linked to genes, [7.9.8](/7.9.8)) or use a general network; rank factors by Algorithm 7.6.1 and remove redundant ones; simulate knock-in effects with a CellOracle-type model to see which factors push fibroblasts toward the target. Test by pooled CRISPR activation of the top $50$–$100$ factors in fibroblasts, single and in combination, with Perturb-seq readout, scoring each cell by its similarity to the target profile (a connectivity score or a classifier); validate the best combinations individually with protein markers and functional assays, and follow the conversion by single-cell time courses to identify intermediate and off-target states.
