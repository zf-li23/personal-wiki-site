---
title: Molecular Phylogenetics
description: "Inferring trees from sequences: rooted and unrooted trees, clades, Newick and the number of trees; gene trees and species trees, duplication and speciation nodes; substitution models as continuous-time Markov chains (JC69, K80, HKY, GTR, gamma rate variation, protein models) and distance corrections; distance methods (additivity, the four-point condition, UPGMA and neighbor joining with worked examples); maximum parsimony with the Fitch and Sankoff algorithms and long-branch attraction; maximum likelihood with Felsenstein's pruning algorithm, tree search and model selection; bootstrap support, consensus trees and Bayesian inference; practice with MAFFT, trimAl and IQ-TREE; the tree of life, horizontal gene transfer and genomic epidemiology. Running example: the gene tree of the MCM family."
---

Every alignment of homologous sequences ([7.8.3](/7.8.3), [7.8.5](/7.8.5)) is a record of descent: the sequences differ because mutations accumulated along the lineages that separated them from a common ancestor. Molecular phylogenetics reads this record backwards and infers the branching history, a tree, together with the amount of change along each branch. Trees are the frame of reference of comparative biology: they decide which genes are orthologs and can transfer function, date divergences with the **molecular clock** ([7.6.41](/7.6.41#sec-41.2.3)), trace the spread of epidemics, reveal **horizontal gene transfer** and organize all life into three domains. The chapter treats the objects (trees, gene trees and species trees), the models of sequence change (substitution models as continuous-time **Markov chains**), and the three families of inference methods: distance methods, which are fast and transparent; maximum parsimony, which minimizes the number of changes; and the model-based methods, maximum likelihood and Bayesian inference, which are the standard today. It ends with the assessment of uncertainty, a practical workflow and applications. The population-level processes that make gene trees differ from species trees (the coalescent) and the biology of molecular evolution belong to [7.10](/7.10); the neutral theory that explains the clock was given in [7.4.23](/7.4.23#sec-23.7). The running example is the MCM family of [7.8.5](/7.8.5): its gene tree contains both the duplications that created the six eukaryotic paralogs MCM2–7 and the speciations that separate the MCM6 orthologs of nine species.

## 6.1. Trees

### 6.1.1. Rooted and Unrooted Trees

**Definition 6.1.1 (Phylogenetic Tree)** A **phylogenetic tree** of a set of $n$ taxa (species, genes or individual sequences) is a tree, in the sense of graph theory ([1.4.3](/1.4.3)), whose leaves are labeled by the taxa and whose internal vertices represent ancestors; each edge (branch) may carry a nonnegative *branch length*, the expected number of substitutions per site along it. In a *rooted* tree one vertex, the root, is the common ancestor of all taxa and gives the branches a direction in time; an *unrooted* tree specifies only the relationships. A tree is *binary* (fully resolved) when every internal vertex of an unrooted tree has degree $3$ (and the root of a rooted tree has two children); a vertex of higher degree is a *polytomy*.

The *topology* is the branching pattern without branch lengths; a *cladogram* shows only the topology, a *phylogram* draws branch lengths to scale. Most methods infer unrooted trees, because the models used are time-reversible (Section 6.2.1) and contain no information about where the root lies. Rooting requires additional information.

**Definition 6.1.2 (Outgroup)** An **outgroup** is a taxon known from independent evidence to lie outside the group under study (the *ingroup*); placing the root on the branch that connects the outgroup to the rest of the unrooted tree roots the ingroup.

Without an outgroup, a tree can be rooted at the midpoint of its longest path (*midpoint rooting*), which is correct only if rates are roughly constant, or by fitting a clock model in which the root is the vertex from which tips are equidistant. In the MCM example, the single MCM of an archaeon roots the eukaryotic family, because the duplications that produced MCM2–7 happened in the eukaryotic lineage after it separated from archaea.

**Definition 6.1.3 (Clade)** A set of taxa that consists of a common ancestor and all of its descendants in a rooted tree is a **clade**, or **monophyletic group**. A group that contains a common ancestor and only some of its descendants is *paraphyletic* (reptiles without birds), and a group whose members do not share an ancestor in the group is *polyphyletic* (warm-blooded animals). Two clades whose common ancestor has no other descendants are *sister groups*.

A tree records relationships, not progress. Humans and chimpanzees are sister groups; neither descends from the other, and the order of the tips along the page has no meaning, since the two subtrees of any vertex can be swapped.

**Definition 6.1.4 (Newick Format)** The **Newick format** writes a rooted tree as nested parentheses: a clade is the comma-separated list of its subtrees in parentheses, optionally followed by a label (a name or a support value) and a branch length after a colon, and the tree ends with a semicolon. For example `((human:0.02,mouse:0.02):0.20,fly:0.25);`. An unrooted tree is written as a rooted one with a trifurcation at the top level.

Newick, named after the seafood restaurant where it was agreed in 1986, is the input and output format of almost all phylogenetic software; NEXUS adds blocks for data and annotations, and the tree viewers iTOL and FigTree read both ([7.8.1](/7.8.1#sec-1.4.3)).

### 6.1.2. How Many Trees?

**Theorem 6.1.1 (Number of Trees)** The number of unrooted binary trees with $n \ge 3$ labeled leaves is

$$
U(n) = (2n - 5)!! = 1 \cdot 3 \cdot 5 \cdots (2n - 5),
$$
and the number of rooted binary trees is $R(n) = U(n + 1) = (2n - 3)!!$.

**Proof** An unrooted binary tree with $n$ leaves has $n - 2$ internal vertices and $2n - 3$ edges (it has $2n - 2$ vertices, and a tree has one edge fewer than vertices). For $n = 3$ there is one tree. Every tree with $n + 1$ leaves arises in exactly one way from a tree with $n$ leaves by attaching leaf $n + 1$ to the middle of one of its $2n - 3$ edges (removing leaf $n + 1$ and suppressing the resulting vertex of degree $2$ inverts the operation). Hence $U(n + 1) = (2n - 3)U(n)$ and $U(n) = \prod_{k=3}^{n-1}(2k - 3) = (2n - 5)!!$. A rooted tree with $n$ leaves becomes an unrooted tree with $n + 1$ leaves when the root is replaced by an edge to an extra leaf, and this is a bijection; so $R(n) = U(n + 1)$. $\square$

| $n$ | $4$ | $5$ | $6$ | $10$ | $20$ | $50$ |
|---|---|---|---|---|---|---|
| unrooted $U(n)$ | $3$ | $15$ | $105$ | $2\,027\,025$ | $2.2\times10^{20}$ | $2.8\times10^{74}$ |
| rooted $R(n)$ | $15$ | $105$ | $945$ | $3.4\times10^{7}$ | $8.2\times10^{21}$ | $2.8\times10^{76}$ |

The number grows faster than exponentially, and finding the best tree under parsimony or likelihood is NP-hard (Foulds and Graham 1982 for parsimony; Roch 2006 for likelihood). Exhaustive search is possible up to about $10$ taxa and branch-and-bound up to about $20$; beyond that all methods are heuristic searches (Section 6.5.2) or constructive algorithms such as neighbor joining (Section 6.3.3).

### 6.1.3. Gene Trees and Species Trees

A tree built from one gene is a statement about that gene, which need not be the history of the species that carry it.

**Definition 6.1.5 (Gene Tree and Species Tree)** A **gene tree** is the phylogeny of the copies of a gene (or of any genomic segment without internal recombination) sampled from one or more species. A **species tree** is the phylogeny of the species themselves, the pattern of their population splits. Gene trees are embedded in the species tree; their internal vertices are speciation vertices, where the gene lineages separate because the species do, or duplication vertices, where a gene was copied within a genome.

The two kinds of vertices define the relationships between homologous genes: genes whose last common ancestor is a speciation vertex are **orthologs**, genes whose last common ancestor is a duplication vertex are **paralogs** ([7.1.4](/7.1.4#sec-4.4.1)). Reconciling a gene tree with a known species tree, by placing each vertex of the gene tree into the species tree with the fewest duplications and losses, labels the vertices and is how databases such as Ensembl Compara classify homologs as one-to-one, one-to-many or many-to-many orthologs and as within-species paralogs. The gene tree can disagree with the species tree for three reasons:

- *Hidden paralogy*: a duplication followed by different losses in different lineages makes paralogs look like orthologs.
- *Incomplete lineage sorting*: when speciations follow each other quickly, the gene lineages of an ancestral population may not have coalesced before the next split, and the gene tree topology differs from the species tree with a probability set by the time between splits in units of the effective population size. About $30\,\%$ of the genome of humans, chimpanzees and gorillas has a gene tree in which humans are not closest to chimpanzees. The theory is the coalescent of [7.10](/7.10).
- **Horizontal gene transfer**, in which a gene moves between species (Section 6.8.2).

Species trees are therefore inferred from many genes, either by concatenating their alignments into a supermatrix or by summary methods that combine the gene trees and account for incomplete lineage sorting (ASTRAL, which finds the species tree that agrees with the largest number of quartets of the gene trees).

## 6.2. Substitution Models

### 6.2.1. Substitutions as a Markov Process

The proportion $p$ of differing sites between two sequences underestimates the number of substitutions, because a site can change more than once, and back. A model of how a site changes over time corrects for this; the simplest, the Jukes–Cantor model, was used in [7.6.41](/7.6.41#sec-41.2.3) to derive the **Jukes–Cantor distance**. All models used in practice share its structure.

**Definition 6.2.1 (Substitution Model)** A **substitution model** for an alphabet of $s$ states ($4$ nucleotides, $20$ amino acids or $61$ sense codons) is a continuous-time **Markov chain** on the states, with rate matrix $Q = (q_{ij})$, $q_{ij} \ge 0$ for $i \ne j$ the instantaneous rate of change from $i$ to $j$ and $q_{ii} = -\sum_{j \ne i}q_{ij}$. The probability of being in state $j$ after time $t$ given state $i$ at time $0$ is the entry of the **matrix exponential**

$$
P(t) = \mathrm{e}^{Qt}. \tag{6.1}
$$
Sites evolve independently and identically (up to a rate factor, Section 6.2.3). The chain is assumed stationary, with equilibrium frequencies $\pi$ ($\pi Q = 0$), and *time-reversible*, $\pi_iq_{ij} = \pi_jq_{ji}$. $Q$ is scaled so that the mean rate $-\sum_i\pi_iq_{ii}$ equals $1$; then the branch length $t$ is the expected number of substitutions per site.

Reversibility is the **detailed balance condition** of [3.5.9](/3.5.9): the process looks the same forwards and backwards in time. It makes the likelihood of a tree independent of the position of the root (Section 6.5.1), which is why the inferred trees are unrooted, and it makes $Q$ similar to a symmetric matrix, so that $\mathrm{e}^{Qt}$ is computed from one eigendecomposition $Q = U\Lambda U^{-1}$ as $U\mathrm{e}^{\Lambda t}U^{-1}$ for all branch lengths.

### 6.2.2. Nucleotide Models

The nucleotide models form a hierarchy, each relaxing an assumption of the previous one. Writing $Q$ in terms of exchangeabilities $r_{ij} = r_{ji}$ and frequencies, $q_{ij} = r_{ij}\pi_j$ for $i \ne j$:

| Model | Exchangeabilities | Frequencies | Free parameters |
|---|---|---|---|
| JC69 (Jukes and Cantor 1969) | all equal | equal | $0$ |
| K80 (Kimura 1980) | **transitions** $\kappa$, **transversions** $1$ | equal | $1$ |
| F81 (Felsenstein 1981) | all equal | free | $3$ |
| HKY85 (Hasegawa, Kishino and Yano 1985) | transitions $\kappa$, transversions $1$ | free | $4$ |
| TN93 (Tamura and Nei 1993) | A↔G and C↔T different, transversions $1$ | free | $5$ |
| GTR (Tavaré 1986) | six free (five after scaling) | free | $8$ |

**Definition 6.2.2 (GTR Model)** The **general time-reversible model** (GTR) is the most general reversible substitution model on four nucleotides: $q_{ij} = r_{ij}\pi_j$ for $i \ne j$ with six exchangeabilities $r_{\mathrm{AC}}, r_{\mathrm{AG}}, r_{\mathrm{AT}}, r_{\mathrm{CG}}, r_{\mathrm{CT}}, r_{\mathrm{GT}}$ (one fixed by the scaling of Definition 6.2.1) and free base frequencies $\pi$.

Transitions (purine to purine, pyrimidine to pyrimidine) are more frequent than transversions in almost all genomes, by a factor $\kappa$ of $2$ to $10$, for chemical reasons (deamination of methylcytosine, tautomeric mispairing; [7.2](/7.2)). For JC69 and K80, $P(t)$ has a closed form, and so do the distance corrections.

**Formula 6.2.1 (K80 Distance)** If $P$ and $Q$ are the proportions of sites that differ by a transition and by a transversion between two sequences, the maximum likelihood estimate of their distance under K80 is

$$
d = -\frac{1}{2}\ln(1 - 2P - Q) - \frac{1}{4}\ln(1 - 2Q). \tag{6.2}
$$
With $Q = 2P$ (transitions and transversions in the proportions of equal rates) it reduces to the JC69 distance $d = -\frac{3}{4}\ln(1 - \frac{4}{3}p)$ with $p = P + Q$.

### 6.2.3. Rate Variation among Sites

Sites of a gene do not evolve at the same rate: second codon positions and catalytic residues change rarely, third codon positions often. The standard model lets each site have a rate factor $\rho$ drawn from a **gamma distribution** with mean $1$ and shape $\alpha$ (Yang 1993), written "+Γ"; small $\alpha$ (below $1$) means strong heterogeneity, most sites nearly invariant and a few very fast. For computation the gamma is replaced by $4$ to $8$ equiprobable categories, each represented by its mean (the *discrete gamma*), and the likelihood of a site averages over the categories. A proportion of invariable sites ("+I") can be added. Without rate variation, distances and branch lengths are underestimated, because the fast sites saturate while the slow ones have barely changed.

**Formula 6.2.2 (JC69 + Gamma Distance)** Under JC69 with gamma-distributed rates of shape $\alpha$, the distance corresponding to a proportion $p$ of differing sites is

$$
d = \frac{3}{4}\alpha\left[\left(1 - \frac{4}{3}p\right)^{-1/\alpha} - 1\right]. \tag{6.3}
$$
As $\alpha \to \infty$ it tends to the JC69 distance.

**Example 6.2.1** Two aligned sequences of $1000$ sites differ at $150$ sites by transitions and $50$ by transversions: $P = 0.15$, $Q = 0.05$, $p = 0.20$. The p-distance is $0.200$; JC69 gives $-0.75\ln(1 - 0.2667) = 0.233$; K80 gives $-0.5\ln(0.65) - 0.25\ln(0.9) = 0.215 + 0.026 = 0.242$; JC69 + Γ gives $0.273$ for $\alpha = 1$ and $0.322$ for $\alpha = 0.5$. At $20\,\%$ difference the choice of model already changes the estimated number of substitutions by more than half, and the differences grow quickly with divergence.

:::

![Correcting observed differences for multiple substitutions. Pairs of sequences of 3000 sites were simulated under K80 with transition/transversion ratio κ = 4 and gamma-distributed rates (α = 0.5, eight categories), one pair for each true distance d from 0.05 to 2.5 substitutions per site. A: the observed proportion of differing sites p; the JC69 expectation (line) saturates at 3/4, and with strong rate variation the observed p rises even more slowly, because the fast sites saturate while the slow ones remain unchanged. B: distances estimated from the same pairs by the p-distance and the JC69, K80 and JC69 + Γ formulas. Only the estimator that models rate variation (with the true α) follows the diagonal; the others underestimate long distances severely, and all estimates become noisy as saturation is approached](./plots/distance-corrections.py)

Proteins are modeled with $20 \times 20$ empirical exchangeability matrices estimated from large sets of alignments, in the tradition of Dayhoff's PAM matrices ([7.8.3](/7.8.3#sec-3.3.2)): JTT (Jones, Taylor and Thornton 1992), WAG (Whelan and Goldman 2001) and LG (Le and Gascuel 2008), with the frequencies of the data ("+F") and gamma rates. Codon models (Goldman and Yang 1994) distinguish synonymous and nonsynonymous substitutions; their ratio $d_{\mathrm{N}}/d_{\mathrm{S}}$ measures selection on proteins and is treated in [7.10](/7.10). Models that let the process vary across the tree (nonstationary composition) or across sites (profile mixture models such as C60) reduce artifacts in deep phylogenies but are expensive.

## 6.3. Distance Methods

### 6.3.1. Additive and Ultrametric Distances

Distance methods first estimate all pairwise distances with a substitution model and then find a tree whose path lengths fit them.

**Definition 6.3.1 (Additive and Ultrametric Distances)** A distance matrix $D$ on $n$ taxa is *additive* if there is a tree with nonnegative branch lengths such that $D_{ij}$ is the length of the path between $i$ and $j$ for all pairs. A rooted tree is an **ultrametric tree** if all leaves are at the same distance from the root; its path-length distances are *ultrametric*: for every three taxa, $D_{ij} \le \max(D_{ik}, D_{jk})$, so the two largest of the three distances are equal.

**Theorem 6.3.1 (Four-Point Condition)** A metric $D$ is additive if and only if for every four taxa $i, j, k, l$ the two largest of the three sums $D_{ij} + D_{kl}$, $D_{ik} + D_{jl}$ and $D_{il} + D_{jk}$ are equal (Buneman 1974). The tree is then unique, and the smallest sum identifies the pairs that are separated by an internal branch, whose length is half the difference between the largest and smallest sums.

The necessity is seen on a quartet tree $((i, j), (k, l))$ with internal branch $b$: $D_{ij} + D_{kl}$ excludes $b$, and the other two sums both contain every branch, $b$ twice. Ultrametric distances are what a strict molecular clock produces; additive distances are what any tree produces when the distances are estimated without error. Real distances are neither, because of sampling error and model misspecification, and the methods differ in how they behave then.

### 6.3.2. UPGMA

**Algorithm 6.3.1 (UPGMA)** The *unweighted pair group method with arithmetic mean* (Sokal and Michener 1958), average-linkage **hierarchical clustering** applied to taxa:

1. Treat each taxon as a cluster of size $1$ at height $0$.
2. Find the two clusters $A$ and $B$ with the smallest distance $D_{AB}$; join them under a new vertex at height $D_{AB}/2$.
3. Set the distance from the new cluster $A \cup B$ to every other cluster $C$ to the size-weighted average $D_{(A\cup B)C} = (|A|D_{AC} + |B|D_{BC})/(|A| + |B|)$.
4. Repeat until one cluster remains.

The time is $O(n^2)$ with suitable data structures ($O(n^3)$ naively), and the result is an ultrametric rooted tree, a **dendrogram**. If the distances are ultrametric, UPGMA returns the correct tree; if rates differ among lineages, it can fail, because a fast-evolving taxon looks distant from its sister.

**Example 6.3.1** For six taxa with distances $D_{AB} = 2$; $D_{AC} = D_{BC} = 4$; $D_{AD} = D_{BD} = D_{CD} = 6$, $D_{AE} = D_{BE} = D_{CE} = 6$, $D_{DE} = 4$; and $D_{\cdot F} = 8$ for all others, UPGMA joins A and B at height $1$; the new distances are $D_{(AB)C} = 4$, $D_{(AB)D} = D_{(AB)E} = 6$, $D_{(AB)F} = 8$. Next C joins (A, B) at height $2$ (a tie with D–E at the same distance $4$, resolved arbitrarily, here giving the same tree either way), then D and E at height $2$, then the two groups at height $3$ and finally F at height $4$: the tree `((((A:1,B:1):1,C:2):1,(D:2,E:2):1):1,F:4);`. These distances are ultrametric, and UPGMA reproduces the clock tree exactly.

### 6.3.3. Neighbor Joining

Neighbor joining (Saitou and Nei 1987) replaces "closest pair" by a criterion that is not fooled by unequal rates: a pair is joined if its members are close to each other *relative to their distances from everybody else*.

**Algorithm 6.3.2 (Neighbor Joining)** Given distances $D$ on $n$ taxa, with $R_i = \sum_kD_{ik}$:

1. Compute $Q_{ij} = (n - 2)D_{ij} - R_i - R_j$ for all pairs and choose the pair $(i, j)$ minimizing $Q_{ij}$.
2. Join $i$ and $j$ to a new vertex $u$ with branch lengths

   $$
   b_{iu} = \frac{1}{2}D_{ij} + \frac{R_i - R_j}{2(n - 2)}, \qquad b_{ju} = D_{ij} - b_{iu}.
   $$
3. Replace $i$ and $j$ by $u$, with $D_{uk} = \frac{1}{2}(D_{ik} + D_{jk} - D_{ij})$ for all other $k$.
4. Repeat until three vertices remain, and join them to a central vertex with the lengths that fit their three distances.

Each step takes $O(n^2)$, so the algorithm takes $O(n^3)$; heuristics (RapidNJ, FastME's balanced minimum evolution, BIONJ with variance weighting) are used for thousands of taxa.

**Theorem 6.3.2 (Consistency of Neighbor Joining)** If $D$ is additive for a binary tree $T$, neighbor joining returns $T$ with its branch lengths (Saitou and Nei 1987; Studier and Keppler 1988). It still returns the correct topology if every entry of $D$ differs from the additive distances of $T$ by less than half the length of the shortest internal branch (Atteson 1999).

Neighbor joining is therefore a consistent method whenever the distance estimates are: with a correct substitution model and long enough sequences, the estimated distances converge to additive ones and the topology to the true tree. The quantity minimized at each step, $Q_{ij}$, is equivalent to choosing the join that minimizes the total branch length of the resulting tree in the balanced minimum-evolution sense (Gascuel and Steel 2006).

**Example 6.3.2** For seven taxa with distances

| | A | B | C | D | E | F | G |
|---|---|---|---|---|---|---|---|
| B | $63$ | | | | | | |
| C | $94$ | $79$ | | | | | |
| D | $111$ | $96$ | $47$ | | | | |
| E | $67$ | $16$ | $83$ | $100$ | | | |
| F | $23$ | $58$ | $89$ | $106$ | $62$ | | |
| G | $107$ | $92$ | $43$ | $20$ | $96$ | $102$ | |

the row sums are $R = (465, 404, 435, 480, 424, 440, 460)$. The smallest $Q$ is $Q_{\mathrm{DG}} = 5 \times 20 - 480 - 460 = -840$, so D and G are joined first, with $b_{\mathrm{D}} = 10 + (480 - 460)/10 = 12$ and $b_{\mathrm{G}} = 8$; the new vertex has distance $(47 + 43 - 20)/2 = 35$ to C. The following joins are C with (D, G) (branches $15$ and $20$), A with F ($14$ and $9$) and B with E ($6$ and $10$), and the last three vertices are joined with branches $40$, $25$ and $18$: the tree is `((C:15,(D:12,G:8):20):40,(A:14,F:9):25,(B:6,E:10):18);`. The matrix satisfies the four-point condition for all $35$ quartets, so it is additive and this tree reproduces every entry exactly ($D_{\mathrm{AB}} = 14 + 25 + 18 + 6 = 63$). Note that the closest pair, B and E at $16$, is joined only fourth: UPGMA would have joined it first.

:::

![UPGMA and neighbor joining on additive distances from a tree without a molecular clock. A: the true tree, in which taxon B evolves five times faster than its sister A; the table gives its path-length distances, the input of both methods. B: UPGMA assumes equal rates and builds an ultrametric tree: it joins D with E, A with the slowly evolving C, and these two clusters before B, so the clade (A, B) is lost. C: neighbor joining corrects each distance by the total divergence of the two taxa and recovers the true unrooted tree with its branch lengths, drawn here with the root on the branch between the (A, B, C) and (D, E) groups as in A. All trees are drawn on the same scale](./plots/upgma-vs-nj.py)

**Example 6.3.3 (The MCM Gene Tree)** We computed distances between the $15$ MCM proteins of [7.8.5](/7.8.5) from their FAMSA alignment ($1282$ columns) with Kimura's approximation for proteins, $d = -\ln(1 - p - 0.2p^2)$, where $p$ is the proportion of differing residues among the columns where both sequences have a residue, and built the neighbor-joining tree, rooted with the archaeal MCM. The six MCM6 orthologs of animals and fungi and the three of plants and the slime mold *Dictyostelium* form one clade, separated from the human paralogs MCM2, MCM3, MCM4, MCM5 and MCM7 by long branches: the paralogs diverged by duplications in the ancestor of all eukaryotes, more than $1.5$ billion years ago, so that human MCM6 is far more similar to yeast Mcm6 ($d = 0.89$) than to human MCM2, MCM3 or MCM5 ($d = 1.53$–$1.59$). The support for these groups is examined in Section 6.6.

## 6.4. Maximum Parsimony

### 6.4.1. The Parsimony Score

**Definition 6.4.1 (Maximum Parsimony)** The *parsimony score* of a tree for an alignment is the minimum, over all assignments of states to the internal vertices, of the number of state changes along its branches, summed over sites. **Maximum parsimony** chooses the tree with the smallest score. A site is *parsimony-informative* if at least two states each occur in at least two taxa; other sites have the same score on all trees.

For a given tree the score of each site is computed by dynamic programming from the leaves to the root.

**Algorithm 6.4.1 (Fitch Algorithm)** For one site on a rooted binary tree (an unrooted tree is rooted anywhere; the score does not depend on the root):

1. Assign each leaf the set containing its state.
2. Visiting internal vertices from the leaves upward, assign vertex $v$ with children sets $S_1$ and $S_2$ the set $S_1 \cap S_2$ if it is nonempty, and otherwise $S_1 \cup S_2$, adding $1$ to the score.
3. The score is the number of unions; a most-parsimonious reconstruction of ancestral states is obtained by a downward pass that chooses a state of the root set and, at each child, keeps the parent's state if it is in the child's set.

The algorithm takes $O(n)$ per site (Fitch 1971; proved optimal by Hartigan 1973). Sankoff's algorithm (1975) generalizes it to unequal costs $c(a, b)$ (for instance transversions costing more than transitions): each vertex stores the minimal cost $S_v(a)$ of its subtree given state $a$, computed as $S_v(a) = \sum_{\text{children } w}\min_b[c(a, b) + S_w(b)]$, in $O(ns^2)$ per site.

**Example 6.4.1** On the tree $(((1, 2), 3), (4, 5))$ with states A, A, G, G, A at one site, the Fitch sets are $\{\mathrm{A}\}$ for $(1, 2)$; $\{\mathrm{A}\} \cup \{\mathrm{G}\} = \{\mathrm{A}, \mathrm{G}\}$ for $((1, 2), 3)$, with one change; $\{\mathrm{A}, \mathrm{G}\}$ for $(4, 5)$, with a second change; and $\{\mathrm{A}, \mathrm{G}\} \cap \{\mathrm{A}, \mathrm{G}\} = \{\mathrm{A}, \mathrm{G}\}$ at the root, without a further change. The score is $2$: for example, root A, with changes to G on the branches leading to taxa 3 and 4.

:::

Parsimony needs no model, explains the data by the fewest events and was the dominant method for morphological data and early molecular data. Its weakness is that it treats every change as equally unlikely whatever the branch length; on long branches several changes at the same site (*homoplasy*) are expected, and parsimony misreads them.

### 6.4.2. Long-Branch Attraction

**Definition 6.4.2 (Long-Branch Attraction)** **Long-branch attraction** is the tendency of inference methods to group taxa with long branches together, regardless of their true relationships, because parallel changes on long branches make them share states by chance. Felsenstein (1978) showed that for four taxa with two long non-sister branches and a short internal branch (the *Felsenstein zone*), maximum parsimony converges to the wrong tree as the number of sites grows: it is statistically inconsistent.

The reason is clear on the quartet $((\mathrm{A}, \mathrm{B}), (\mathrm{C}, \mathrm{D}))$ with long branches to A and C. A site supports the true split if A and B share a state that C and D do not; on the short branches this requires the single change on the internal branch. A site supports the wrong split $((\mathrm{A}, \mathrm{C}), (\mathrm{B}, \mathrm{D}))$ if A and C have independently changed to the same state, which on two long branches is frequent; if such sites outnumber the informative changes on the internal branch, parsimony prefers the wrong tree, and more data make it more certain.

![Long-branch attraction in the Felsenstein zone. A: the true unrooted tree ((A, B), (C, D)), in which the non-sister taxa A and C have long branches (1.0 expected substitutions per site) and B, D and the internal branch are short (0.1). B: the proportion of 100 data sets simulated under the Jukes–Cantor model for which each method recovers the true topology, against the number of sites: maximum parsimony; neighbor joining on Jukes–Cantor distances; and maximum likelihood under the Jukes–Cantor model, with branch lengths optimized for each of the three topologies. Parsimony converges to the wrong tree ((A, C), (B, D)), which groups the long branches (0 of 100 correct from 200 sites on); the model-based methods are consistent and recover the true tree in 96–100 % of data sets with 2000 sites](./plots/long-branch.py)

Model-based methods correct for multiple changes and are consistent when the model is adequate, but they are not immune: if the model underestimates multiple substitutions (no rate variation, wrong composition), likelihood also attracts long branches. Long-branch attraction has caused famous errors, such as the early placement of fast-evolving microsporidia (in fact relatives of fungi) at the base of the eukaryotic tree. Remedies are better models, removal of the fastest sites, and above all denser sampling of taxa, which breaks long branches into shorter ones.

## 6.5. Maximum Likelihood

### 6.5.1. The Likelihood of a Tree

Under a substitution model, a tree with branch lengths assigns a probability to every alignment column, and the **likelihood function** of the tree is the product over columns. Maximum likelihood (Felsenstein 1981) chooses the topology and branch lengths (and model parameters) that maximize it, an application of **maximum likelihood estimation** to a parameter space that contains a discrete part, the topology.

For one site, the probability of the observed leaf states is a sum over the unobserved states of all $n - 1$ internal vertices of a rooted version of the tree, $s^{n-1}$ terms. Dynamic programming reduces this to a pass over the tree.

**Algorithm 6.5.1 (Felsenstein's Pruning Algorithm)** For a site with observed leaf states, root the tree at any vertex and define the partial likelihood $L_v(a)$ of vertex $v$ as the probability of the leaf states below $v$ given state $a$ at $v$:

1. At a leaf with state $x$, $L_v(a) = 1$ if $a = x$ and $0$ otherwise (for a gap or ambiguous base, $1$ for every compatible state).
2. At an internal vertex $v$ with children $w$ on branches of length $t_w$, visiting vertices from the leaves upward,

   $$
   L_v(a) = \prod_{\text{children } w}\left[\sum_bP_{ab}(t_w)L_w(b)\right].
   $$
3. The likelihood of the site is $\sum_a\pi_aL_{\mathrm{root}}(a)$; the log-likelihood of the tree is the sum of the logarithms over sites, and with rate categories each site's likelihood is averaged over the categories.

The time is $O(ns^2)$ per site and per rate category (Felsenstein 1981), and identical columns are computed once. By reversibility, the likelihood is the same for every placement of the root (Felsenstein's "pulley principle"), so the root can be moved to any branch, which is used to optimize one branch length at a time.

**Example 6.5.1** Take the tree with root $r$, two children $x$ and $y$ at distance $0.05$, leaves 1 and 2 below $x$ at distances $0.1$ and $0.2$, leaves 3 and 4 below $y$ at $0.1$ and $0.3$, and a site with states A, C, A, A under JC69 ($P_{aa}(t) = \frac{1}{4} + \frac{3}{4}\mathrm{e}^{-4t/3}$, $P_{ab}(t) = \frac{1}{4} - \frac{1}{4}\mathrm{e}^{-4t/3}$; for $t = 0.1$ these are $0.906$ and $0.031$). The partial likelihoods (for A, C, G, T) are $L_x = (0.0530, 0.0257, 0.0018, 0.0018)$, $L_y = (0.6823, 0.0026, 0.0026, 0.0026)$ and $L_r = (0.03309, 0.00034, 0.00004, 0.00004)$, and the site likelihood is $\frac{1}{4}\sum_aL_r(a) = 0.00838$, log-likelihood $-4.78$. Rooting the same tree at $x$ instead (with the branch $x$–$y$ of length $0.1$) gives the same value, as the pulley principle states. Almost all the probability comes from state A at the root, with a single change to C on the branch to leaf 2.

### 6.5.2. Searching Tree Space

Branch lengths of a fixed topology are optimized numerically, one at a time by Newton's method using the derivatives of $P(t)$, until the likelihood converges. The topology is found by local search: starting from a quick tree (neighbor joining or a parsimony tree built by stepwise addition), rearrangements are tried and kept if they increase the likelihood.

- *Nearest-neighbor interchange* (NNI) swaps two of the four subtrees around an internal branch; a binary unrooted tree has $2(n - 3)$ NNI neighbors.
- *Subtree pruning and regrafting* (SPR) cuts a subtree and reattaches it on any other branch, $O(n^2)$ neighbors.
- *Tree bisection and reconnection* (TBR) cuts the tree into two parts and reconnects them by any pair of branches, $O(n^3)$ neighbors.

Larger moves escape more local optima at a higher cost per step. The current programs, RAxML-NG (Kozlov and colleagues 2019) and IQ-TREE 2 (Minh and colleagues 2020), combine SPR or NNI searches with lazy evaluation of the likelihood only near the change, vectorized pruning and, in IQ-TREE, a stochastic perturbation of the best tree followed by renewed search to escape local optima. Trees of a few thousand sequences and genome-scale alignments are routine on a server; for millions of closely related genomes, such as SARS-CoV-2, placement methods add each new sequence to an existing tree by parsimony (UShER, Turakhia and colleagues 2021).

### 6.5.3. Choosing a Model

More parameters always increase the likelihood, so models are compared with criteria that penalize parameters: the **Akaike information criterion** $\mathrm{AIC} = 2k - 2\ln L$ and the **Bayesian information criterion** $\mathrm{BIC} = k\ln m - 2\ln L$ with $k$ free parameters and $m$ sites, or, for nested models, the **likelihood ratio test** with $2\Delta\ln L$ compared with a $\chi^2$ distribution. Branch lengths count as parameters ($2n - 3$ of them) but are the same for all models compared on one tree. ModelFinder (Kalyaanamoorthy and colleagues 2017), built into IQ-TREE, fits hundreds of models with and without +Γ, +I and +F on a quick tree and selects by BIC; for protein alignments, LG + Γ or a mixture model is chosen most often. The choice matters most for deep divergences, where saturation and compositional differences are strong.

## 6.6. Uncertainty in Trees

### 6.6.1. The Bootstrap

An estimated tree is a point estimate; for a topology, a discrete object, standard errors and intervals have no meaning, but the stability of each branch can be measured. Felsenstein (1985) applied the **bootstrap** of [3.5.7](/3.5.7): resample the alignment columns with replacement, rebuild the tree from each replicate, and count how often each branch reappears.

**Definition 6.6.1 (Bootstrap Support)** For a branch of the estimated tree, which splits the taxa into two sets, the **bootstrap support** is the percentage of $B$ trees, each inferred by the same method from an alignment of the same length obtained by sampling its columns with replacement, that contain the same split.

The PHYLIP programs make each step explicit: `seqboot` generates the resampled alignments, `dnadist` computes distances for each, `neighbor` builds a tree for each, and `consense` counts the splits. A *majority-rule consensus tree* contains all splits present in more than half of a collection of trees (bootstrap replicates or posterior samples), labeled with their frequency; splits are compatible if they occur together in one tree, and the majority-rule splits are always compatible.

Bootstrap support is not the probability that a clade is true. Under the conditions of the simulations of Hillis and Bull (1993), clades with $70\,\%$ support were correct in at least $95\,\%$ of cases, which is the origin of the rule of thumb that $70\,\%$ is "well supported", but the relation depends on the data and the method. The support measures sampling variation only: a method that is consistently wrong, as parsimony in the Felsenstein zone, gives high bootstrap support to the wrong clade, and genome-scale alignments give $100\,\%$ to almost every branch, whether the model is adequate or not. Faster approximations replace the full bootstrap in large analyses: the ultrafast bootstrap of IQ-TREE (Hoang and colleagues 2018), whose values are less conservative (a clade is considered supported at $95\,\%$), and the SH-like approximate likelihood ratio test (SH-aLRT, Guindon and colleagues 2010), whose support is conventionally accepted above $80\,\%$.

**Example 6.6.1 (Support in the MCM Gene Tree)** We resampled the $1282$ columns of the MCM alignment $1000$ times and rebuilt the neighbor-joining tree of Example 6.3.3 from each replicate. The MCM6 clade appeared in all $1000$ trees, as did the pairs human–mouse, fly–mosquito, fission yeast–budding yeast and *Arabidopsis*–rice. The deep relationships among the paralogs are unstable: MCM2 with MCM3 in $54\,\%$, MCM4 with MCM7 in $33\,\%$ (MCM4 with MCM5 appeared in $36\,\%$), and the other paralog groupings in $31$–$33\,\%$. Within MCM6, the slime mold grouped with the plants in $61\,\%$ and the animals with the fungi (the opisthokonts) in only $21\,\%$, although the species tree accepted from many genes places *Dictyostelium* with animals and fungi in the Amorphea. A single protein contains too little signal to resolve divergences that occurred over a short interval more than a billion years ago, and the support values say so.

![A gene tree of the MCM family: the neighbor-joining tree of Kimura protein distances from the FAMSA alignment of 15 MCM proteins (1282 columns), rooted with the MCM of the archaeon *Saccharolobus solfataricus*, with bootstrap percentages from 1000 replicates. Vertices where eukaryotic paralogs separate are duplications (squares); vertices inside the MCM6 clade (shaded) are speciations, and orthologs are the MCM6 proteins of different species. The MCM6 orthologs form a clade with 100 % support, while the order of the duplications that produced MCM2–7 is poorly resolved (31–54 %), and the grouping of animals with fungi, part of the accepted species tree, receives 21 %](./plots/mcm-gene-tree.py)

### 6.6.2. Bayesian Inference

Bayesian phylogenetics (Rannala and Yang 1996; Mau, Newton and Larget 1997) places a **prior distribution** on topologies, branch lengths and model parameters and computes their **posterior distribution** with **Markov chain Monte Carlo**: the chain proposes changes (an NNI or SPR move, a rescaled branch length, a new $\alpha$), accepts them with the **Metropolis–Hastings algorithm** acceptance probability, and after convergence visits trees in proportion to their posterior probability. The *posterior probability of a clade* is the fraction of sampled trees that contain it, and the result is summarized as a majority-rule consensus tree or the tree with the highest product of clade probabilities. MrBayes and RevBayes are general programs; BEAST 2 specializes in trees with time scales, combining **molecular clock** models with sampling dates (tip dating) and fossil calibrations, and population models such as the coalescent and birth–death processes. Relaxed clocks let the substitution rate vary among branches, drawn independently from a lognormal distribution or autocorrelated along the tree, which is necessary because strict clocks are rejected for most data.

The advantages are natural measures of uncertainty for all parameters and the ability to integrate over nuisance parameters; the costs are computation, the need to check convergence (several independent chains, effective sample sizes), and sensitivity to priors, especially on branch lengths. Posterior clade probabilities tend to be higher than bootstrap percentages for the same data, and both are overconfident when the model is wrong.

## 6.7. Practice

A standard workflow for a gene family or a set of orthologs runs from sequences to a rooted, annotated tree:

1. Collect homologs (BLAST or profile search, [7.8.4](/7.8.4), [7.8.5](/7.8.5)), include an outgroup and remove fragments and near-identical copies.
2. Align: proteins with MAFFT; coding DNA as protein, then back-translated codon by codon ([7.8.5](/7.8.5#sec-5.3.3)).
3. Trim unreliable columns (trimAl, ClipKIT), which reduces noise but should not remove most of the variable sites.
4. Select the model and infer the ML tree with branch support.
5. Root with the outgroup and visualize; for dating, fit a clock model.

```bash
# Align, trim and infer a maximum-likelihood tree with model selection and branch support
mafft --auto mcm6_orthologs.fa > mcm6.afa
trimal -in mcm6.afa -out mcm6.trim.afa -automated1
iqtree2 -s mcm6.trim.afa -m MFP -B 1000 -alrt 1000 -T AUTO --prefix mcm6
# outputs: mcm6.iqtree (report, selected model), mcm6.treefile (Newick with "SH-aLRT/UFBoot" supports)

# The classic distance pipeline with an explicit bootstrap (PHYLIP); each program reads a parameter file
seqboot < seqboot.par    # 100 resampled alignments
dnadist < dnadist.par    # distances for each replicate (F84 model, transition/transversion ratio)
neighbor < neighbor.par  # one NJ tree per replicate
consense < consense.par  # majority-rule consensus with split frequencies
```

```python
# Reading, rooting and inspecting trees with Biopython
from Bio import Phylo
tree = Phylo.read("mcm6.treefile", "newick")
tree.root_at_midpoint()                              # or root_with_outgroup(...) with a known outgroup
for clade in tree.get_nonterminals():
    if clade.confidence is not None and clade.confidence < 70:
        print("weak clade:", [t.name for t in clade.get_terminals()], clade.confidence)
print(tree.distance("MCM6_HUMAN", "MCM6_YEAST"))      # path length in substitutions per site
Phylo.draw_ascii(tree)
```

A tree of human individuals built from genome-wide variants (an exercise often run with PHYLIP on VCF files) is not a phylogeny in the sense of this chapter: human genomes recombine, so each region has its own genealogy, and a tree of individuals summarizes their genetic similarity, much as a principal component plot does ([7.8.13](/7.8.13)). Such trees group individuals by ancestry but their internal branches do not represent population splits.

## 6.8. Applications

### 6.8.1. The Tree of Life

The universal tree became possible when Woese and Fox (1977) compared the sequences of small-subunit ribosomal RNA, a molecule present in all cellular organisms and conserved enough to be aligned across all of them. The tree of 16S/18S rRNA divided life into three domains, Bacteria, Archaea and Eukarya, revealing that the prokaryotes comprise two groups as distinct from each other as from eukaryotes. Phylogenies of concatenated conserved proteins with mixture models and the discovery of new archaeal lineages by metagenomics ([7.8.14](/7.8.14)), above all the Asgard archaea, now support a tree in which eukaryotes arose from within the archaea, related to the Asgard group, with the mitochondrion contributed by an alphaproteobacterium: two primary domains rather than three. Rooting the tree of life is itself a phylogenetic problem; it uses pairs of paralogous genes that were duplicated before the last universal common ancestor, such as the elongation factors EF-Tu and EF-G, each copy rooting the tree of the other.

### 6.8.2. Horizontal Gene Transfer

**Horizontal gene transfer** moves genes between species by transformation, transduction and conjugation ([7.4](/7.4)) and is common among prokaryotes. It is detected by two kinds of evidence:

- *Phylogenetic*: the gene tree conflicts with the species tree with strong support, for example a bacterial gene nested within a clade of genes from distantly related bacteria, or a eukaryotic gene nested within bacterial or plant sequences.
- *Compositional*: a recently acquired gene still has the GC content, codon usage and $k$-mer statistics of its donor, which differ from the host genome ([7.8.7](/7.8.7)); clusters of such genes flanked by tRNA genes or mobile elements form genomic islands.

Both kinds of evidence can mislead: phylogenetic conflict also arises from hidden paralogy, incomplete lineage sorting and long-branch attraction, and compositional deviation from strong selection on highly expressed genes; reliable claims combine them and exclude contamination of the genome assembly, which has produced spectacular false reports of horizontal transfer in animals. Well-supported transfers into eukaryotes exist: the whitefly *Bemisia tabaci* carries a phenolic glucoside malonyltransferase gene acquired from plants, which it uses to neutralize plant defense compounds (Xia and colleagues 2021). In bacteria, horizontal transfer spreads antibiotic resistance genes on plasmids between species, which is why resistance genes have phylogenies unrelated to those of their hosts.

### 6.8.3. Genomic Epidemiology

For fast-evolving pathogens, phylogenies are made in real time. SARS-CoV-2 accumulates about two substitutions per genome per month, so genomes sampled a few weeks apart differ, and trees of millions of genomes trace transmission between countries and the origin of new variants. Nextstrain builds time-scaled trees of subsampled genomes, estimating the clock rate from the sampling dates (root-to-tip regression, as for HIV in [7.6.41](/7.6.41#sec-41.2.3)); UShER places every newly submitted genome by parsimony on a global tree; and the Pango nomenclature names lineages as clades of that tree (B.1.1.7, BA.2.86), which is why a lineage name encodes its ancestry. The same methods track influenza for vaccine strain selection and the spread of antimicrobial-resistant bacteria in hospitals.

## Summary

| Topic | Key points |
|---|---|
| Trees | rooted/unrooted, branch lengths in substitutions per site (Definition 6.1.1); outgroup rooting (Definition 6.1.2); clades and para- and polyphyletic groups (Definition 6.1.3); Newick (Definition 6.1.4) |
| Counting | $(2n - 5)!!$ unrooted, $(2n - 3)!!$ rooted binary trees (Theorem 6.1.1); exhaustive search only to about $10$ taxa; tree inference NP-hard |
| Gene vs species trees | duplication and speciation vertices, orthologs and paralogs (Definition 6.1.5); conflict from hidden paralogy, incomplete lineage sorting, horizontal transfer |
| Models | continuous-time Markov chain, $P(t) = \mathrm{e}^{Qt}$, reversible, branch length = expected substitutions (Definition 6.2.1, Eq. (6.1)); JC69 → K80 → HKY → GTR (Definition 6.2.2); K80 distance (Formula 6.2.1); gamma rates and the JC + Γ distance (Formula 6.2.2, Example 6.2.1); protein models JTT, WAG, LG |
| Distances | additive and ultrametric (Definition 6.3.1), four-point condition (Theorem 6.3.1); UPGMA assumes a clock (Algorithm 6.3.1, Example 6.3.1); neighbor joining, $O(n^3)$, consistent for additive distances (Algorithm 6.3.2, Theorem 6.3.2, Example 6.3.2) |
| Parsimony | minimum changes (Definition 6.4.1); Fitch $O(n)$ per site, Sankoff for weighted costs (Algorithm 6.4.1, Example 6.4.1); long-branch attraction and inconsistency in the Felsenstein zone (Definition 6.4.2) |
| Likelihood | pruning algorithm $O(ns^2)$ per site, pulley principle (Algorithm 6.5.1, Example 6.5.1); NNI/SPR/TBR search, RAxML-NG, IQ-TREE; model choice by AIC/BIC |
| Uncertainty | bootstrap support (Definition 6.6.1) is not a probability; majority-rule consensus; UFBoot ≥ 95, SH-aLRT ≥ 80; MCM tree: orthologs 100 %, deep paralogy 31–54 % (Example 6.6.1); Bayesian MCMC, posterior clade probabilities, relaxed clocks |
| Practice and applications | align → trim → ModelFinder → ML + support → root; three domains and the archaeal origin of eukaryotes; HGT by phylogenetic and compositional evidence; SARS-CoV-2 trees, Nextstrain, UShER, Pango |

## Questions

1. How many rooted binary trees exist for $8$ taxa, and how many unrooted ones? If a computer evaluates $10^6$ trees per second, how long does an exhaustive search take for $15$ and for $20$ taxa (unrooted)?

   **Answer** Rooted: $(2 \cdot 8 - 3)!! = 13!! = 135\,135$; unrooted: $11!! = 10\,395$. For $15$ taxa, $U = 25!! = 7.9\times10^{12}$ trees, about $7.9\times10^6\,\mathrm{s}$, or $3$ months; for $20$ taxa, $U = 35!! = 2.2\times10^{20}$, about $2.2\times10^{14}\,\mathrm{s}$, some $7$ million years. Exhaustive search is impossible beyond small problems, which is why heuristic search (Section 6.5.2) is used.

2. Two sequences of $500$ sites differ at $225$ sites. Compute the p-distance and the JC69 distance. Why is the JC69 distance for $p = 0.74$ unreliable?

   **Answer** $p = 0.45$; $d = -\frac{3}{4}\ln(1 - \frac{4}{3} \times 0.45) = -\frac{3}{4}\ln 0.4 = 0.687$ substitutions per site, half again as many as the observed differences. For $p = 0.74$, $1 - \frac{4}{3}p = 0.0133$ and $d = -\frac{3}{4}\ln 0.0133 = 3.24$; the curve $p(d)$ is almost flat near its asymptote $3/4$, so a change of $p$ by one standard error ($\sqrt{0.74 \times 0.26/500} = 0.02$) changes $d$ from about $2.4$ to infinity. Sequences this divergent are saturated: they carry almost no information about their distance, and for $p \ge 3/4$ the estimate does not exist.

3. For four taxa with distances $D_{\mathrm{AB}} = 3$, $D_{\mathrm{AC}} = 7$, $D_{\mathrm{AD}} = 8$, $D_{\mathrm{BC}} = 6$, $D_{\mathrm{BD}} = 7$, $D_{\mathrm{CD}} = 5$: (a) check the four-point condition; (b) build the neighbor-joining tree with branch lengths; (c) build the UPGMA tree and compare.

   **Answer** (a) $D_{\mathrm{AB}} + D_{\mathrm{CD}} = 8$, $D_{\mathrm{AC}} + D_{\mathrm{BD}} = 14$, $D_{\mathrm{AD}} + D_{\mathrm{BC}} = 14$: the two largest are equal, so $D$ is additive with the split AB | CD and internal branch $(14 - 8)/2 = 3$. (b) $R = (18, 16, 18, 20)$; $Q_{\mathrm{AB}} = 2 \times 3 - 18 - 16 = -28$, $Q_{\mathrm{CD}} = -28$, the others $-22$. Joining A and B: $b_{\mathrm{A}} = 1.5 + (18 - 16)/4 = 2$, $b_{\mathrm{B}} = 1$; the new vertex $u$ has $D_{u\mathrm{C}} = (7 + 6 - 3)/2 = 5$, $D_{u\mathrm{D}} = 6$, and the three-point fit gives $b_u = (5 + 6 - 5)/2 = 3$, $b_{\mathrm{C}} = 2$, $b_{\mathrm{D}} = 3$: the tree `((A:2,B:1):3,C:2,D:3);`, which reproduces all six distances. (c) UPGMA joins A, B at height $1.5$, then C, D at height $2.5$, then the pairs at height $(7 + 8 + 6 + 7)/4/2 = 3.5$: the same topology, but with equal root-to-tip distances that distort the branch lengths (A and B are made equally distant from the root although B evolves more slowly).

4. Four taxa have the sequences 1: AAGCT, 2: AGGCT, 3: GAATT, 4: GGATC. Compute the parsimony score of each of the three unrooted topologies and name the most parsimonious tree. Which sites are informative?

   **Answer** Site 1 (A, A, G, G) supports 12 | 34; site 2 (A, G, A, G) supports 13 | 24; site 3 (G, G, A, A) and site 4 (C, C, T, T) support 12 | 34; site 5 (T, T, T, C) is uninformative (one change on every tree). An informative site costs $1$ on the tree it supports and $2$ on the others. Scores: ((1, 2), (3, 4)): $1 + 2 + 1 + 1 + 1 = 6$; ((1, 3), (2, 4)): $2 + 1 + 2 + 2 + 1 = 8$; ((1, 4), (2, 3)): $2 + 2 + 2 + 2 + 1 = 9$. The most parsimonious tree is ((1, 2), (3, 4)); sites 1–4 are informative.

5. In Example 6.5.1, compute the likelihood of the same site if leaf 2 also had state A. Explain why the likelihood of a site never exceeds the largest single term $\pi_a\prod$ by much when branches are short.

   **Answer** With all four leaves A: $L_x(\mathrm{A}) = 0.9064 \times P_{\mathrm{AA}}(0.2)$; $P_{\mathrm{AA}}(0.2) = 0.25 + 0.75\mathrm{e}^{-0.2667} = 0.8244$, so $L_x(\mathrm{A}) = 0.747$, and $L_x(b) = 0.0312 \times 0.0585 = 0.0018$ for $b \ne \mathrm{A}$. $L_y(\mathrm{A}) = 0.6823$ as before. With $P_{\mathrm{AA}}(0.05) = 0.9516$, $L_r(\mathrm{A}) \approx (0.9516 \times 0.747)(0.9516 \times 0.682) = 0.462$, and the site likelihood is about $\frac{1}{4} \times 0.462 = 0.116$ (log $-2.16$), fourteen times ($0.116/0.0084 = 13.8$) the likelihood with C at leaf 2. When branches are short, $P_{ab}(t) \approx q_{ab}t$ is small for $a \ne b$, so assignments of internal states that need extra changes contribute terms smaller by factors of $t$; the sum is dominated by the most parsimonious reconstruction. This is why parsimony and likelihood agree for closely related sequences and differ when branches are long.

6. A colleague reports that a clade of four fast-evolving parasite species, which morphology places in different families, receives $100\,\%$ bootstrap support in a parsimony analysis of $20\,000$ sites. What could be wrong, and how would you test it?

   **Answer** The clade unites long branches, the signature of long-branch attraction; with many sites, an inconsistent method gives full bootstrap support to its wrong answer, because the bootstrap measures only sampling variation (Section 6.6.1). Tests: analyze the data with maximum likelihood under a well-fitting model (ModelFinder, gamma rates, a mixture model for proteins); add taxa that break the long branches (slower-evolving relatives of each parasite); remove the fastest-evolving sites or the third codon positions and check whether the clade persists; check compositional heterogeneity (parasites often have biased composition) with nonstationary models; and examine whether each parasite alone, added to a tree without the others, attaches where morphology predicts.

7. Explain why bootstrap support of $70\,\%$ does not mean that the clade is true with probability $0.7$, and give one situation in which a clade with $40\,\%$ support is nevertheless correct.

   **Answer** The bootstrap percentage is the frequency with which a method recovers the clade from data sets resampled from the observed one; it describes the variability of the estimator, not a posterior probability, and it ignores model error. In Hillis and Bull's simulations it was conservative (clades with $70\,\%$ were correct more than $95\,\%$ of the time), but it can be anticonservative for a biased method. A correct clade has low support when the branch defining it is short and few sites changed on it, as for the rapid radiations of Example 6.6.1: the opisthokont clade, accepted from many genes, receives $21\,\%$ in the MCM6 protein tree because a single gene has few informative changes on that branch.

8. A gene tree places a bacterial gene of *E. coli* inside a clade of genes from Bacteroidetes, with $98\,\%$ support. List the alternative explanations to horizontal transfer, and the evidence that would favor transfer.

   **Answer** Alternatives: hidden paralogy (an ancient duplication followed by different losses, so the compared genes are not orthologs); long-branch attraction or compositional attraction of genes with similar base composition; misassembly or contamination of one of the genomes; and a wrong species tree in the reference. Evidence for transfer: the *E. coli* gene has atypical GC content and codon usage relative to the rest of its genome but similar to Bacteroidetes genes ([7.8.7](/7.8.7)); it lies in a genomic island near a tRNA gene, integrase or plasmid sequence; it is absent from close relatives of *E. coli* (patchy distribution); the topology is robust to model choice and site removal; and the gene is physically linked to typical *E. coli* genes in independent assemblies, which excludes contamination.

9. Two nucleotide models are fitted to an alignment of $10$ taxa on the same tree: JC69 with log-likelihood $-10\,234.6$ and HKY + Γ with $-9\,987.2$. Compute the AIC of both models and the likelihood ratio statistic. Which model is chosen?

   **Answer** Free parameters: $2n - 3 = 17$ branch lengths for both, plus $\kappa$, three free frequencies and $\alpha$ for HKY + Γ, $22$ in all. $\mathrm{AIC}_{\mathrm{JC}} = 2 \times 17 + 2 \times 10\,234.6 = 20\,503.2$ and $\mathrm{AIC}_{\mathrm{HKY+\Gamma}} = 44 + 19\,974.4 = 20\,018.4$. The models are nested (HKY + Γ reduces to JC69 for $\kappa = 1$, equal frequencies and $\alpha \to \infty$, a boundary case for $\alpha$), and $2\Delta\ln L = 494.8$ on $5$ degrees of freedom is far beyond any $\chi^2$ critical value ($11.1$ at $5\,\%$). HKY + Γ is chosen by both criteria; a difference of almost $500$ AIC units means that transition bias, unequal frequencies or rate variation are strongly present in the data.

10. (Design) You have the genomes of $60$ strains of a bacterial pathogen from a hospital outbreak, sampled over $18$ months, and want to know whether transmission occurred within the hospital and when the outbreak began. Outline the phylogenetic analysis and its pitfalls.

    **Answer** Map reads of all strains to a closed reference genome of the outbreak lineage ([7.8.10](/7.8.10)) and call single-nucleotide variants ([7.8.12](/7.8.12)); mask mobile elements, phages and repeats, and detect and remove recombined regions (Gubbins, ClonalFrameML), since recombination imports clusters of substitutions that do not follow the clonal tree. Infer a maximum-likelihood tree of the core alignment (GTR + Γ, with an ascertainment correction for variable-site alignments), rooted with an outgroup strain from outside the hospital. Test for a temporal signal by root-to-tip regression on sampling dates and a date-randomization test; if present, fit a time-scaled tree (BEAST 2 or a fast method such as TreeTime) with a relaxed clock to date the most recent common ancestor of the hospital strains, the latest possible start of the outbreak. Within-hospital transmission is supported if hospital strains form a clade separated from community strains and the pairwise SNP distances are below the number expected from the clock rate over the epidemiological time intervals (a few SNPs for most bacteria); combine with ward and admission data to propose transmission links (TransPhylo). Pitfalls: too few substitutions for a resolved tree (many polytomies and low support), within-host diversity (one colony per patient may not represent the infecting population), sampling gaps, and the difference between the dates of tree vertices and the dates of transmission events.
