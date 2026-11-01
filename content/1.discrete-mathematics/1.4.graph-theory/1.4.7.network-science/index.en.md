---
title: Network Science
description: "The statistics and models of large real networks: degree distributions, path lengths, clustering and assortativity; the Erdős–Rényi random graph and its giant-component phase transition; small worlds and the Watts–Strogatz model; scale-free networks, power-law fitting and its current debate, the configuration model and degree-preserving randomization; growth with preferential attachment (Barabási–Albert model, fitness, aging) and citation networks; centrality and PageRank; community structure, modularity, Louvain and Leiden; percolation and attack, epidemic thresholds, diffusion and network motifs."
---

The previous chapters asked what a given graph is like: whether it is connected, planar or Hamiltonian, how many spanning trees it has, how large a matching or a flow it supports. *Network science* asks a different question: what do the very large graphs that occur in nature and society look like, why do they look like that, and how does their structure shape the processes that run on them? Its objects are *complex networks*, graphs with thousands to billions of vertices whose edges were not drawn by a designer but grew through many local events: the World Wide Web, the Internet, friendships, coauthorships and citations, power grids, and the interaction networks of genes, proteins and metabolites. Such graphs cannot be described vertex by vertex; they are described statistically, by distributions and averages, and compared with random models that serve as null hypotheses. This chapter develops that language. Section 7.1 defines the basic measures (degree distribution, path length, clustering, degree correlations); Section 7.2 studies the random graph of Erdős and Rényi, the reference model of the field, and its sudden phase transition to a giant component; Sections 7.3–7.5 introduce the three empirical regularities that distinguish real networks from random ones (short paths with high clustering, heavy-tailed degree distributions, growth by preferential attachment) and the models that explain them; Sections 7.6 and 7.7 treat the two most common analyses of a given network, ranking vertices by centrality and dividing it into communities; Section 7.8 studies processes on networks: failures and attacks, the spreading of epidemics, diffusion, and the statistics of recurring subgraphs.

The basic notions come from earlier chapters and are used without repetition: **degree**, the **adjacency matrix** and the handshaking lemma (Property 1.3.1), **walks**, **paths** and **connected components** (Definition 2.1.4), counting walks with powers of the adjacency matrix (Theorem 2.2.1), **breadth-first search** and **Dijkstra's algorithm** (Algorithm 2.7.1), the **Laplacian matrix** and the **Fiedler vector** (Definition 6.5.2). The probability is that of [3.1](/3.1): binomial and Poisson distributions, generating functions, and the Markov chains of [3.5.9](/3.5.9). The methods of this chapter are applied to biological networks, interactomes, regulatory networks and their motifs, in [systems biology](/7.9); the stochastic block model is treated as a statistical model in [3.4.12](/3.4.12#sec-12.6).

## 7.1. Networks and Their Basic Measures

### 7.1.1. From Real Systems to Graphs

A network is a graph together with an interpretation: the vertices are the components of a system (web pages, routers, people, proteins) and the edges the interactions between them (hyperlinks, cables, acquaintances, physical binding). The literature of network science often says *node* and *link* where graph theory says vertex and edge; we keep the graph-theoretic terms. The choice of what counts as an edge decides what can be studied: joining people who work together gives a professional network, joining those who exchanged e-mails a communication network, and the two have different structure on the same vertex set.

Edges may be directed (hyperlinks, citations, phone calls, metabolic reactions, regulation of one gene by another) or undirected (coauthorship, protein binding), weighted (the number of calls, the strength of an interaction) or unweighted. Many systems are naturally a **bipartite graph** between two kinds of objects: actors and films, authors and papers, diseases and the genes associated with them (the human disease network of Goh and colleagues, 2007), recipes and their ingredients, or ingredients and the flavor compounds they contain (Ahn and colleagues, 2011). A bipartite graph is usually analyzed through its two *projections*: two diseases are joined if they share a gene, two ingredients if they share a flavor compound. Projections are convenient but lossy, and every vertex of degree $d$ on the other side becomes a clique of $d$ vertices, which inflates the clustering of Section 7.1.4.

We write $N$ for the number of vertices and $M$ for the number of edges (the letter $L$ is reserved for the Laplacian matrix), $k_i$ for the degree of vertex $i$, and $\langle k\rangle = 2M/N$ for the average degree of an undirected network (Property 1.3.1); for a digraph $\langle k_{\mathrm{in}}\rangle = \langle k_{\mathrm{out}}\rangle = M/N$. Averages over the vertices of one network are written with angle brackets, $\langle f(k)\rangle = N^{-1}\sum_i f(k_i)$.

Real networks are *sparse*: $M$ is a tiny fraction of the $\binom{N}{2}$ possible edges, and $\langle k\rangle$ stays small as $N$ grows. Metcalfe's law, the claim that the value of a communication network grows like $N^2$, implicitly assumes a **complete graph**, which no large network is. The table below lists ten networks that recur in this chapter; $p = \langle k\rangle/(N-1)$ is the fraction of possible edges present.

| Network | Type | $N$ | $M$ | $\langle k\rangle$ | $p$ |
|---|---|---|---|---|---|
| Internet (routers) | undirected | 192,244 | 609,066 | 6.34 | $3.3\times10^{-5}$ |
| World Wide Web (one domain) | directed | 325,729 | 1,497,134 | 4.60 | $1.4\times10^{-5}$ |
| Power grid (western US) | undirected | 4,941 | 6,594 | 2.67 | $5.4\times10^{-4}$ |
| Mobile-phone calls | directed | 36,595 | 91,826 | 2.51 | $6.9\times10^{-5}$ |
| E-mail | directed | 57,194 | 103,731 | 1.81 | $3.2\times10^{-5}$ |
| Science collaboration | undirected | 23,133 | 93,439 | 8.08 | $3.5\times10^{-4}$ |
| Film actors | undirected | 702,388 | 29,397,908 | 83.71 | $1.2\times10^{-4}$ |
| Citations | directed | 449,673 | 4,689,479 | 10.43 | $2.3\times10^{-5}$ |
| *E. coli* metabolism | directed | 1,039 | 5,802 | 5.58 | $5.4\times10^{-3}$ |
| Yeast protein interactions | undirected | 2,018 | 2,930 | 2.90 | $1.4\times10^{-3}$ |

(Data: Barabási, *Network Science*, 2016, Table 2.1; for directed networks $\langle k\rangle$ is the mean in-degree $M/N$.) Sparsity is why networks are stored as edge lists or adjacency lists rather than as adjacency matrices, and why algorithms whose cost is linear in $N + M$ matter.

### 7.1.2. Degree Distribution

The first statistic of a network is how its edges are shared among the vertices.

**Definition 7.1.1 (Degree Distribution)** Let $N_k$ be the number of vertices of degree $k$ in a network with $N$ vertices. The **degree distribution** of the network is $p_k = N_k/N$, $k = 0, 1, 2, \dots$, the probability that a vertex chosen uniformly at random has degree $k$. Its moments are $\langle k^n\rangle = \sum_k k^np_k$; in particular the mean degree $\langle k\rangle$ and the variance $\langle k^2\rangle - \langle k\rangle^2$. For a digraph the **in-degree** and **out-degree** distributions are defined in the same way. The *complementary cumulative distribution* is $P_k = \sum_{k' \geq k}p_{k'}$.

The degree distribution forgets which vertex has which degree and who is joined to whom, but many properties of a network (the size of its largest component, its robustness, its epidemic threshold) turn out to depend mainly on it, and above all on its first two moments $\langle k\rangle$ and $\langle k^2\rangle$. The ratio

$$
\kappa = \frac{\langle k^2\rangle}{\langle k\rangle}
$$

will appear repeatedly. It has a simple meaning: if we pick an edge at random and follow it to one of its ends, we reach a vertex of degree $k$ with probability $kp_k/\langle k\rangle$, because a vertex of degree $k$ is the end of $k$ edges; the mean degree of the vertex reached is therefore $\sum_k k\cdot kp_k/\langle k\rangle = \kappa \geq \langle k\rangle$. This is the *friendship paradox* (Feld, 1991): on average, your friends have more friends than you do, because people with many friends are overrepresented among friends.

### 7.1.3. Distances

The distance $d(i, j)$ between two vertices is the length of a shortest path between them, computed by **breadth-first search** in $O(N + M)$ time from each source, or by Dijkstra's algorithm when edges have lengths ([1.4.2](/1.4.2#sec-2.7), [4.3.10](/4.3.10)).

**Definition 7.1.2 (Average Path Length)** For a connected network, the **average path length** is the mean distance over all pairs of distinct vertices,

$$
\langle d\rangle = \frac{2}{N(N-1)}\sum_{i<j}d(i, j),
$$

and the *diameter* is $d_{\max} = \max_{i,j}d(i, j)$. For a disconnected network both are computed within the largest component, or the harmonic mean of distances is used, with $1/d(i, j) = 0$ for unreachable pairs.

Exact computation needs a breadth-first search from every vertex, $O(N(N + M))$ in total; for networks with millions of vertices $\langle d\rangle$ is estimated from a random sample of sources. The diameter is sensitive to a single long chain, so $\langle d\rangle$ is the more informative statistic.

### 7.1.4. Clustering

In social networks two friends of the same person are often friends of each other. Clustering measures how often this happens.

**Definition 7.1.3 (Clustering Coefficient)** Let vertex $i$ of an undirected simple graph have $k_i \geq 2$ neighbors, and let $T_i$ be the number of edges among them, that is, the number of triangles through $i$. The local **clustering coefficient** of $i$ is

$$
C_i = \frac{T_i}{\binom{k_i}{2}} = \frac{2T_i}{k_i(k_i-1)},
$$

the fraction of pairs of neighbors of $i$ that are adjacent ($C_i = 0$ when $k_i < 2$). The average clustering coefficient is $\langle C\rangle = N^{-1}\sum_iC_i$. The global clustering coefficient, also called the transitivity of the network, is

$$
C_\Delta = \frac{3 \times (\text{number of triangles})}{\text{number of connected triples}} = \frac{\sum_iT_i}{\sum_i\binom{k_i}{2}},
$$
where a connected triple is a path of length two (a vertex with two of its neighbors).

The two global versions weight the vertices differently: $\langle C\rangle$ gives each vertex the same weight, $C_\Delta$ weights vertex $i$ by its number of neighbor pairs, so it is dominated by the high-degree vertices. They can differ greatly, and a paper must say which one it reports.

**Proposition 7.1.1** Let $A$ be the adjacency matrix of a simple undirected graph. Then $T_i = \frac12(A^3)_{ii}$, the number of triangles of the graph is $\frac16\operatorname{tr}(A^3)$, and $\sum_i\binom{k_i}{2} = \frac12\sum_{i \neq j}(A^2)_{ij}$.

**Proof** By Theorem 2.2.1, $(A^3)_{ii}$ is the number of closed walks of length $3$ from $i$. In a simple graph such a walk $i \to j \to l \to i$ has $j \neq i$, $l \neq j$ and $l \neq i$, so it traverses a triangle through $i$; each triangle through $i$ is traversed by exactly two such walks, one in each direction. Hence $(A^3)_{ii} = 2T_i$. Each triangle has three vertices, so $\sum_i T_i$ counts it three times and the number of triangles is $\frac13\sum_iT_i = \frac16\operatorname{tr}(A^3)$. Finally $(A^2)_{ij}$ for $i \neq j$ is the number of common neighbors of $i$ and $j$, so $\sum_{i\neq j}(A^2)_{ij}$ counts every connected triple with center $v$ and ends $\{i, j\}$ twice, once as $(i,j)$ and once as $(j,i)$. $\square$

![The example graph G0 used throughout this chapter: two groups of four vertices joined by the edge 4–5 (red). Each vertex shows its degree k and local clustering coefficient C; the fill encodes betweenness centrality (Example 7.6.1), which is largest at the two ends of the bridge](./plots/example_graph.py)

**Example 7.1.1** The graph $G_0$ in the figure has $N = 8$ vertices and $M = 11$ edges, so $\langle k\rangle = 2.75$; its degrees are $3, 2, 3, 3, 4, 2, 3, 2$, so $p_2 = 3/8$, $p_3 = 4/8$, $p_4 = 1/8$. There are four triangles, $\{1,2,3\}$, $\{1,3,4\}$, $\{5,6,7\}$ and $\{5,7,8\}$, in agreement with $\operatorname{tr}(A^3) = 24$. Vertex $4$ has neighbors $1, 3, 5$, among which only $1$–$3$ is an edge, so $C_4 = 1/3$; similarly $C_1 = C_3 = C_7 = 2/3$, $C_2 = C_6 = C_8 = 1$, $C_5 = 1/3$, and $\langle C\rangle = 17/24 \approx 0.708$. The number of connected triples is $\sum_i\binom{k_i}{2} = 21$, so $C_\Delta = 3\cdot4/21 = 4/7 \approx 0.571$, smaller than $\langle C\rangle$ because the low-degree vertices $2, 6, 8$ have $C_i = 1$. Breadth-first search from each vertex gives $\langle d\rangle = 58/28 \approx 2.07$ and $d_{\max} = 4$ (for example between $2$ and $6$).

### 7.1.5. Degree Correlations and Assortativity

The degree distribution does not say whether high-degree vertices tend to be joined to each other or to low-degree vertices. Let $k_{\mathrm{nn}}(k)$ be the average degree of the neighbors of vertices of degree $k$. If it increases with $k$ the network is *assortative*: hubs link to hubs; if it decreases, *disassortative*: hubs link to vertices of low degree.

**Definition 7.1.4 (Assortativity)** The **assortativity coefficient** of an undirected network (Newman, 2002) is the Pearson correlation coefficient of the degrees at the two ends of an edge, with each edge counted in both directions:

$$
r = \frac{\sum_{(i,j)}k_ik_j/M - \left[\sum_{(i,j)}\frac12(k_i + k_j)/M\right]^2}{\sum_{(i,j)}\frac12(k_i^2 + k_j^2)/M - \left[\sum_{(i,j)}\frac12(k_i + k_j)/M\right]^2},
$$

the sums running over the $M$ edges. Then $-1 \leq r \leq 1$, with $r > 0$ for assortative and $r < 0$ for disassortative networks.

Social networks are typically assortative (coauthorship networks have $r$ between about $0.1$ and $0.4$), while technological and biological networks are disassortative, with $r$ between about $-0.07$ (the Web) and $-0.28$ (food webs); the Internet and protein interaction networks have $r \approx -0.2$ (Newman, 2002). Part of the disassortativity of networks with hubs is structural: in a simple graph a hub of degree $k$ cannot have more than a few other hubs among its neighbors once $k^2$ exceeds the number of edges available, which forces $r < 0$ even under random wiring with no multiple edges (Maslov, Sneppen and Zaliznyak, 2004). The graph $G_0$ is strongly disassortative, $r = -23/54 \approx -0.426$: its two degree-$2$ vertices in each group are attached to the high-degree vertices.

The measures of this section can be computed with the Python library networkx:

```python
import networkx as nx

G = nx.Graph([(1, 2), (1, 3), (1, 4), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (5, 8), (6, 7), (7, 8)])
print(nx.degree_histogram(G))                    # [0, 0, 3, 4, 1]: N_k for k = 0, 1, 2, 3, 4
print(nx.average_shortest_path_length(G))        # 2.0714...
print(nx.diameter(G))                            # 4
print(nx.clustering(G))                          # local C_i
print(nx.average_clustering(G))                  # 0.7083...
print(nx.transitivity(G))                        # 0.5714...
print(nx.degree_assortativity_coefficient(G))    # -0.4259...
```

## 7.2. Random Graphs

A network property means little in isolation: a clustering coefficient of $0.1$ is large or small depending on what one would expect by chance. The random graph is the simplest model of "chance", and almost every claim about a real network is a comparison with it or with one of its generalizations (Section 7.4.6).

### 7.2.1. Two Models

**Definition 7.2.1 (Random Graph)** Let $N \geq 2$. Each of the following two models of a random simple graph on the labeled vertex set $\{1, \dots, N\}$ is called a **random graph**.

1. The **Erdős–Rényi model** $G(N, M)$ (Erdős and Rényi, 1959) is the uniform distribution on the $\binom{\binom{N}{2}}{M}$ simple graphs on the labeled vertex set $\{1, \dots, N\}$ with exactly $M$ edges.
2. The model $G(N, p)$ (Gilbert, 1959) is the random simple graph on $\{1, \dots, N\}$ in which each of the $\binom{N}{2}$ pairs is joined by an edge independently with probability $p$.

$G(N, p)$ is easier to compute with, and for $M \approx p\binom{N}{2}$ the two models have the same asymptotic properties.

In $G(N, p)$ the number of edges is the number of successes in $\binom{N}{2}$ independent trials, so it has the **binomial distribution** $\mathrm{Bin}\left(\binom{N}{2}, p\right)$:

$$
\mathbb{P}(M = m) = \binom{\binom{N}{2}}{m}p^m(1-p)^{\binom{N}{2}-m}, \qquad \mathbb{E}M = p\binom{N}{2}, \qquad \operatorname{Var}(M) = p(1-p)\binom{N}{2}.
$$

The relative fluctuation $\sqrt{\operatorname{Var}(M)}/\mathbb{E}M = \sqrt{(1-p)/(p\binom N2)}$ vanishes as $N \to \infty$ for fixed mean degree $c = p(N-1)$, since $p\binom{N}{2} = cN/2$: a large random graph has, with high probability, very nearly its expected number of edges. Throughout this section the mean degree $c$ is held fixed as $N \to \infty$, which is the sparse regime of real networks.

### 7.2.2. The Degree Distribution

**Theorem 7.2.1** In $G(N, p)$ the degree of a given vertex has the distribution $\mathrm{Bin}(N-1, p)$. If $N \to \infty$ with $p = c/(N-1)$ for a fixed $c > 0$, then for each $k = 0, 1, 2, \dots$,

$$
\mathbb{P}(k_i = k) = \binom{N-1}{k}p^k(1-p)^{N-1-k} \to \mathrm{e}^{-c}\frac{c^k}{k!},
$$

the **Poisson distribution** $\mathrm{Poi}(c)$. Moreover the fraction $N_k/N$ of vertices of degree $k$ converges in probability to $\mathrm{e}^{-c}c^k/k!$.

**Proof** Vertex $i$ is joined to each of the other $N-1$ vertices independently with probability $p$, which gives the binomial distribution; since $(N-1)p = c$, the limit is the **Poisson limit theorem** ([Theorem 4.1.4](/3.1.4#thm-4.1.4)). For the second claim, $\mathbb{E}[N_k/N] = \mathbb{P}(k_1 = k)$ converges to the Poisson probability, and the degrees of two different vertices depend on each other only through the single pair joining them, so $\operatorname{Var}(N_k/N) = O(1/N)$ and Chebyshev's inequality gives convergence in probability. $\square$

The Poisson distribution has a sharp peak at $c$ and a tail that falls faster than exponentially: $p_{k+1}/p_k = c/(k+1)$. Large random networks therefore have no hubs. The largest degree of $G(N, p)$ grows only like $\ln N/\ln\ln N$, and for realistic parameters the degrees are confined to a narrow band.

**Example 7.2.1** Model the acquaintances of $N = 10^9$ people as a random graph with $c = 1000$. The largest degree $k_{\max}$ is roughly the value at which $N\,\mathbb{P}(K \geq k_{\max}) = 1$, and the smallest the value at which $N\,\mathbb{P}(K \leq k_{\min}) = 1$; with $K \sim \mathrm{Poi}(1000)$ this gives $k_{\max} \approx 1196$ and $k_{\min} \approx 815$. The probability that a given person has more than $2000$ acquaintances is $\mathbb{P}(K > 2000) \approx 1.5 \times 10^{-170}$. In a random society everyone would have between about 800 and 1200 acquaintances. Real social networks are nothing like this: Facebook limits a user to 5000 friends, a limit that many users reach, while many other people have only a handful of contacts.

### 7.2.3. The Emergence of the Giant Component

The most striking property of the random graph concerns its components. When $c$ is small, $G(N, p)$ is a dust of small trees; when $c$ is large, almost all vertices belong to one component. The change happens abruptly, at $c = 1$.

**Definition 7.2.2 (Giant Component)** A sequence of graphs with $N \to \infty$ vertices has a **giant component** if its largest connected component contains a fraction $S > 0$ of the vertices that stays bounded away from $0$, that is, a number of vertices proportional to $N$.

**Theorem 7.2.2 (Erdős–Rényi, 1960)** Let $p = c/N$ with $c > 0$ fixed. With probability tending to $1$ as $N \to \infty$:

1. if $c < 1$, every component of $G(N, p)$ has $O(\ln N)$ vertices, and all components are trees or contain at most one cycle;
2. if $c > 1$, there is a unique giant component, containing $(S + o(1))N$ vertices, where $S \in (0, 1)$ is the unique positive solution of
   $$
   S = 1 - \mathrm{e}^{-cS}, \tag{7.1}
   $$
   and every other component has $O(\ln N)$ vertices;
3. if $c = 1$, the largest component has order $N^{2/3}$ vertices.

**Proof** (idea) We give the heuristic argument behind $S$; the rigorous proof controls the error terms of the same exploration (see Bollobás, *Random Graphs*, or Janson, Łuczak and Ruciński, *Random Graphs*).

Explore the component of a vertex $v$ by breadth-first search. Each vertex removed from the queue has, among the vertices not yet seen, a number of new neighbors with distribution $\mathrm{Bin}(N - n, p)$, where $n$ is the number of vertices already seen; as long as $n = o(N)$ this is approximately $\mathrm{Poi}(c)$, and the numbers for different vertices are nearly independent. The exploration therefore looks like a **Galton–Watson process** with $\mathrm{Poi}(c)$ offspring, and the component of $v$ is small exactly when this **branching process** dies out. Let $u$ be the probability of extinction. A process dies out if and only if the processes started by each of the children die out, so $u = \mathbb{E}[u^K]$ with $K \sim \mathrm{Poi}(c)$, that is, $u$ is a fixed point of the **probability generating function** $G(x) = \mathbb{E}x^K = \mathrm{e}^{c(x-1)}$:

$$
u = \mathrm{e}^{-c(1-u)}.
$$

By the extinction theorem for branching processes, $u$ is the smallest root of this equation in $[0, 1]$, and $u < 1$ if and only if the mean number of offspring $c$ exceeds $1$. A vertex lies in the giant component when its exploration does not die out, so the fraction of such vertices is $S = 1 - u$, which turns the equation into Eq. (7.1). That the surviving explorations all meet in a single component follows because two sets of $\varepsilon N$ vertices are joined by some edge with probability $1 - (1-p)^{\varepsilon^2N^2} \to 1$. $\square$

The function $f(S) = 1 - \mathrm{e}^{-cS}$ is increasing and concave with $f(0) = 0$ and $f'(0) = c$, and $f(1) < 1$. Hence $f(S) = S$ has a root in $(0, 1)$ if and only if the slope at the origin exceeds the diagonal, $c > 1$. Near the threshold, expanding $\mathrm{e}^{-cS} = 1 - cS + \frac12c^2S^2 + O(S^3)$ in Eq. (7.1) gives $S \approx 2(c - 1)/c^2 \approx 2(c-1)$: the giant component grows continuously from zero, with a slope that jumps at $c = 1$. In the language of statistical physics this is a **second-order phase transition**, with $c$ as the control parameter and $S$ as the order parameter. Numerical solutions of Eq. (7.1):

| $c$ | $1.5$ | $2$ | $3$ | $4$ | $5$ |
|---|---|---|---|---|---|
| $S$ | $0.583$ | $0.797$ | $0.941$ | $0.980$ | $0.993$ |

![The giant component of random graphs with M = cN/2 random edges. A: the fraction S of vertices in the largest component against the mean degree c, averaged over realizations, for N = 100 (40 realizations), N = 1000 (20) and N = 100,000 (3); the black curve is the solution of Eq. (7.1). For small N the transition is smeared out; for large N the simulation is indistinguishable from the theory. B: at the critical point c = 1, the probability p_s that a random vertex belongs to a component of s vertices (logarithmic bins, N = 200,000, 5 realizations), with the Borel distribution and its power-law tail s^(-3/2)](./plots/giant_component.py)

The sizes of the small components are also known exactly in the limit. For $c \leq 1$, the total progeny of a Galton–Watson process with $\mathrm{Poi}(c)$ offspring has the Borel distribution, so the probability that a random vertex lies in a component of $s$ vertices is

$$
p_s = \frac{\mathrm{e}^{-cs}(cs)^{s-1}}{s!} \approx \frac{1}{c\sqrt{2\pi}}\,s^{-3/2}\,\mathrm{e}^{-(c - 1 - \ln c)s},
$$

the approximation following from **Stirling's approximation**. Since $c - 1 - \ln c > 0$ for $c \neq 1$, the component sizes have an exponential cutoff away from the critical point; at $c = 1$ the cutoff disappears and $p_s \approx s^{-3/2}/\sqrt{2\pi}$, a power law (figure, panel B).

As $c$ increases further, the last isolated vertices are absorbed. The expected number of isolated vertices is $N(1-p)^{N-1} \approx N\mathrm{e}^{-pN}$, which tends to $\mathrm{e}^{-x}$ when $p = (\ln N + x)/N$.

**Theorem 7.2.3 (Connectivity Threshold)** Let $p = (\ln N + x)/N$ with $x \in \mathbb{R}$ fixed. Then the number of isolated vertices of $G(N, p)$ converges in distribution to $\mathrm{Poi}(\mathrm{e}^{-x})$, and $\mathbb{P}(G(N, p) \text{ is connected}) \to \exp(-\mathrm{e}^{-x})$ (Erdős and Rényi, 1959).

In particular the random graph is connected with high probability when $c - \ln N \to \infty$ and disconnected when $c - \ln N \to -\infty$. Its evolution as $c$ increases thus passes through four regimes:

| Regime | Mean degree | Structure |
|---|---|---|
| Subcritical | $c < 1$ | only small components, the largest of order $\ln N$; mostly trees |
| Critical | $c = 1$ | largest component of order $N^{2/3}$; component sizes $p_s \sim s^{-3/2}$ |
| Supercritical | $1 < c < \ln N$ | one giant component with a fraction $S$ of the vertices, containing cycles; small tree components and isolated vertices outside it |
| Connected | $c > \ln N$ | a single component |

![Three realizations of G(N, p) with N = 60 and mean degree c = 0.5 (subcritical), 1 (critical) and 3 (supercritical); the largest component is red. Layouts by a force-directed algorithm](./plots/er_evolution.py)

Every network in the table of Section 7.1.1 has $\langle k\rangle > 1$, and all except the film actors have $\langle k\rangle < \ln N$ (for the Internet $\ln N = 12.2$, for the yeast protein network $7.6$). If they were random graphs they would therefore consist of one giant component with small fragments around it, which is indeed what is observed: the protein interaction network, for example, has a giant component and many small clusters.

### 7.2.4. Distances and Clustering

In the supercritical regime the neighborhood of a vertex looks locally like a tree: a vertex has about $c$ neighbors, about $c^2$ vertices at distance $2$, and about $c^d$ at distance $d$, as long as $c^d \ll N$. Setting $c^{d} \approx N$ gives the order of magnitude of distances:

$$
\langle d\rangle \approx \frac{\ln N}{\ln c}.
$$

This logarithmic growth is the mathematical content of the phrase "small world": distances grow like $\ln N$, not like $N$ or $\sqrt{N}$ as in a lattice. Denser networks have shorter paths, through the factor $1/\ln c$.

The clustering coefficient of a random graph is computed even more easily. Two neighbors of a vertex are joined independently of everything else with probability $p$, so

$$
\langle C\rangle = C_\Delta = p = \frac{c}{N-1}
$$

in expectation, which tends to $0$ for sparse networks. Once $N$ and $\langle k\rangle$ are given, the random graph predicts every other statistic: Poisson degrees, $\langle d\rangle \approx \ln N/\ln\langle k\rangle$, and $C \approx \langle k\rangle/N$. For the networks of Section 7.1.1 the predicted distances $\ln N/\ln\langle k\rangle$ range from $3.0$ (film actors) to $18.5$ (e-mail), the same order as the measured ones; the prediction for clustering, in contrast, is far too small, and the prediction for degrees fails in the tail. These two failures are the subjects of the next two sections.

## 7.3. Small Worlds

### 7.3.1. Six Degrees of Separation

The idea that any two people are linked by a short chain of acquaintances appeared in a 1929 short story, "Chains", by the Hungarian writer Frigyes Karinthy. In 1967 the psychologist Stanley Milgram tested it: he asked residents of Nebraska and Kansas to forward a letter towards a target person in Massachusetts, each time to an acquaintance on a first-name basis whom they thought closer to the target. In the best-documented version of the experiment (Travers and Milgram, 1969), 64 of 296 chains arrived, with on average $5.2$ intermediaries; John Guare's 1990 play made "six degrees of separation" a phrase. Since many chains were lost, these numbers are rough, but later studies on a much larger scale confirmed the order of magnitude. Dodds, Muhamad and Watts (2003) asked more than 60,000 e-mail users to reach one of 18 targets in 13 countries; correcting for the chains that were abandoned, they estimated median chain lengths of five to seven. On the complete Facebook graph of 2011, with 721 million users, the average distance was $4.74$ (Backstrom and colleagues, 2012), and it had fallen to $4.57$ by 2016. A random graph with the world population $N \approx 7 \times 10^9$ and $\langle k\rangle \approx 1000$ acquaintances would give $\ln N/\ln\langle k\rangle \approx 3.3$.

The experiments also showed what the distance alone does not: participants found short chains with only local information, mostly through acquaintances of intermediate strength rather than through hubs, and most chains failed because people stopped forwarding, not because no short path existed.

### 7.3.2. The Watts–Strogatz Model

Random graphs explain short paths but not clustering; regular lattices have clustering but long paths. Watts and Strogatz (1998) interpolated between them.

**Definition 7.3.1 (Watts–Strogatz Model)** Let $N$ and an even integer $K$ with $2 \leq K < N$ be given, and $0 \leq p \leq 1$. Place $N$ vertices on a cycle and join each vertex to its $K$ nearest neighbors, $K/2$ on each side. Then visit each edge $(i, i + j)$, $1 \leq j \leq K/2$, once and, with probability $p$, replace it by an edge $(i, l)$ with $l$ chosen uniformly among the vertices that are neither $i$ nor already adjacent to $i$. The resulting random graph is the **Watts–Strogatz model** with parameters $N$, $K$, $p$.

At $p = 0$ the graph is a regular ring lattice. Its clustering coefficient is

$$
C(0) = \frac{3(K-2)}{4(K-1)},
$$

which is $2/3$ for $K = 10$ and approaches $3/4$ for large $K$, and its average path length is $\ell(0) \approx N/(2K)$, proportional to $N$. At $p = 1$ the graph is close to a random graph with $\langle k\rangle = K$: $C \approx K/N$ and $\ell \approx \ln N/\ln K$. The surprise is what happens in between. A rewired edge is a shortcut that can join distant parts of the ring, and a few shortcuts suffice to make $\ell(p)$ drop to near its random-graph value; the triangles, on the other hand, are destroyed only one by one. A triangle of the lattice survives if none of its three edges is rewired, so $C(p) \approx C(0)(1-p)^3$ (Barrat and Weigt, 2000). For $10^{-3} \lesssim p \lesssim 10^{-1}$ the network has short paths and high clustering at the same time.

![The Watts–Strogatz model. A: rings of 20 vertices with K = 4, for p = 0 (regular), p = 0.1 (a few shortcuts) and p = 1 (random). B: for N = 1000 and K = 10, the clustering coefficient C(p) and the average path length ℓ(p) relative to the ring (each point the average of 4 realizations), with the approximation (1 − p)³ for C. In the shaded range of p the path length has fallen to a fraction of its ring value while the clustering is almost unchanged: a small world](./plots/small_world.py)

**Definition 7.3.2 (Small-World Network)** A network is a **small-world network** if its average path length is comparable to that of a random graph with the same numbers of vertices and edges, growing at most logarithmically with $N$, while its clustering coefficient is much larger than that of the random graph, $C \gg \langle k\rangle/N$.

The three networks studied by Watts and Strogatz all have this property (data from Watts and Strogatz, 1998; $\ell_{\mathrm{rand}}$ and $C_{\mathrm{rand}}$ are the values of random graphs of the same size and mean degree):

| Network | $\ell$ | $\ell_{\mathrm{rand}}$ | $C$ | $C_{\mathrm{rand}}$ |
|---|---|---|---|---|
| Film actors | $3.65$ | $2.99$ | $0.79$ | $0.00027$ |
| Power grid | $18.7$ | $12.4$ | $0.080$ | $0.005$ |
| *C. elegans* neurons | $2.65$ | $2.25$ | $0.28$ | $0.05$ |

The definition is comparative and somewhat loose; a common quantitative version is the small-world coefficient $\sigma = (C/C_{\mathrm{rand}})/(\ell/\ell_{\mathrm{rand}})$, with $\sigma \gg 1$ for a small world. The Watts–Strogatz model explains how short paths and clustering coexist, but its degree distribution is narrow, like that of the random graph. It cannot produce hubs.

## 7.4. Scale-Free Networks

### 7.4.1. Power Laws

When the degree distribution of the Web was measured (Albert, Jeong and Barabási, 1999), it did not look Poisson at all: on log–log axes it was close to a straight line over several orders of magnitude, $p_k \sim k^{-\gamma}$ with $\gamma \approx 2.1$ for in-degrees.

**Definition 7.4.1 (Power-Law Distribution)** A discrete random variable $K$ with values $k \geq k_{\min} \geq 1$ has a **power-law distribution** with exponent $\gamma > 1$ if

$$
p_k = \frac{k^{-\gamma}}{\zeta(\gamma, k_{\min})}, \qquad \zeta(\gamma, k_{\min}) = \sum_{k = k_{\min}}^\infty k^{-\gamma},
$$
where $\zeta(\gamma, k_{\min})$ is the Hurwitz zeta function (the Riemann zeta function $\zeta(\gamma)$ when $k_{\min} = 1$). In the continuous approximation, used in calculations, $K \geq k_{\min} > 0$ has density $p(k) = (\gamma - 1)k_{\min}^{\gamma - 1}k^{-\gamma}$ and complementary cumulative distribution $\mathbb{P}(K \geq k) = (k/k_{\min})^{-(\gamma - 1)}$. More generally a distribution has a *power-law tail* if $p_k \sim Ck^{-\gamma}$ as $k \to \infty$.

A power law decays much more slowly than an exponential $\mathrm{e}^{-\lambda k}$: for large $k$ it is larger by an arbitrarily large factor, so extreme values that would be impossible under an exponential or Poisson distribution become common. The continuous form with $k_{\min} = x_{\min}$ is the Pareto distribution of economics. Pareto's observation that a minority holds most of the wealth is a statement about its exponent: if a fraction $P$ of the population with the largest values holds a fraction $W$ of the total, then $W = P^{(\alpha - 1)/\alpha}$ with $\alpha = \gamma - 1 > 1$, and the "80/20 rule" ($W = 0.8$ for $P = 0.2$) corresponds to $\alpha = \ln 5/\ln 4 \approx 1.16$, that is, $\gamma \approx 2.16$.

Power laws have a unique symmetry. Rescaling the variable, $k \to ak$, multiplies a power law by a constant, $p(ak) = a^{-\gamma}p(k)$, so the shape of the distribution is the same at every scale; no other distribution has this property.

**Proposition 7.4.1** Let $p\colon (0, \infty) \to (0, \infty)$ be differentiable and suppose that for every $a > 0$ there is a number $g(a)$ with $p(ak) = g(a)p(k)$ for all $k > 0$. Then $p(k) = p(1)k^{-\gamma}$ for some real $\gamma$.

**Proof** Setting $k = 1$ gives $g(a) = p(a)/p(1)$, so $p(ak)p(1) = p(a)p(k)$. Differentiating with respect to $a$ and setting $a = 1$ gives $kp'(k)p(1) = p'(1)p(k)$, that is, $\mathrm{d}\ln p/\mathrm{d}\ln k = p'(1)/p(1) =: -\gamma$, a constant. Integrating, $\ln p(k) = \ln p(1) - \gamma\ln k$. $\square$

### 7.4.2. Hubs

In a network with a power-law degree distribution, a few vertices have degrees far above the mean. These *hubs* are the defining feature of such networks.

**Example 7.4.1** Take a network with $N = 10^{12}$ vertices (the order of the number of Web documents) and compare a Poisson degree distribution with mean $4.6$ with a power law with $\gamma = 2.1$ and $k_{\min} = 1$. The expected number of vertices of degree at least $100$ is $10^{12}\,\mathbb{P}(K \geq 100) \approx 10^{-82}$ under the Poisson distribution, that is, none, and $10^{12}\,\zeta(2.1, 100)/\zeta(2.1) \approx 3.7 \times 10^9$ under the power law.

How large is the largest hub of a finite network? The largest of $N$ independent degrees is, in order of magnitude, the value $k_{\max}$ above which one expects a single vertex.

**Proposition 7.4.2 (Natural Cutoff)** For $N$ vertices with the continuous power-law density of Definition 7.4.1, the solution of $N\,\mathbb{P}(K \geq k_{\max}) = 1$ is

$$
k_{\max} = k_{\min}N^{1/(\gamma - 1)}.
$$

For an exponential density $\lambda\mathrm{e}^{-\lambda(k - k_{\min})}$, $k \geq k_{\min}$, the same condition gives $k_{\max} = k_{\min} + \ln N/\lambda$.

**Proof** $N(k_{\max}/k_{\min})^{-(\gamma - 1)} = 1$ and $N\mathrm{e}^{-\lambda(k_{\max} - k_{\min})} = 1$. $\square$

The largest hub of a scale-free network thus grows polynomially with its size, that of an exponential network only logarithmically. For the Web sample of Section 7.1.1 ($N = 325{,}729$, in-degree exponent $\gamma = 2.1$, $k_{\min} = 1$) the power law predicts $k_{\max} \approx N^{1/1.1} \approx 1.0 \times 10^5$, and an exponential distribution with the same mean in-degree $4.60$ (so $1/\lambda = 3.60$) predicts $k_{\max} \approx 1 + 3.60\ln N \approx 47$; the largest in-degree actually observed is $10{,}721$. The power-law estimate is too large because real hubs saturate, but it is the right order of magnitude, and the exponential estimate is off by a factor of two hundred. For $\gamma > 2$, $k_{\max}/N \to 0$; for $\gamma = 2$ the largest hub is of order $N$, and for $\gamma < 2$ the formula would give $k_{\max} > N$, which is impossible in a simple graph (Section 7.4.4).

### 7.4.3. Scale-Free Networks and the Divergence of Moments

**Definition 7.4.2 (Scale-Free Network)** A **scale-free network** is a network whose degree distribution has a power-law tail, $p_k \sim Ck^{-\gamma}$ for large $k$. The exponent $\gamma$ is the **degree exponent** of the network; for directed networks the in- and out-degree distributions have separate exponents $\gamma_{\mathrm{in}}$ and $\gamma_{\mathrm{out}}$.

The name refers to the moments. For the continuous power law cut off at $k_{\max}$,

$$
\langle k^n\rangle = \int_{k_{\min}}^{k_{\max}}k^np(k)\,\mathrm{d}k = \frac{\gamma - 1}{n - \gamma + 1}\,k_{\min}^{\gamma - 1}\left(k_{\max}^{n - \gamma + 1} - k_{\min}^{n - \gamma + 1}\right)
$$

for $n \neq \gamma - 1$. As $N \to \infty$, $k_{\max} \to \infty$ by Proposition 7.4.2: the moments with $n < \gamma - 1$ converge, and those with $n > \gamma - 1$ diverge like $k_{\max}^{n - \gamma + 1}$. Most measured exponents lie between $2$ and $3$, where the mean is finite but the second moment, and with it the variance, diverges:

$$
\langle k^2\rangle \sim k_{\max}^{3 - \gamma} \sim N^{(3-\gamma)/(\gamma - 1)}.
$$

In a random graph, the degree of a random vertex is $\langle k\rangle \pm \sqrt{\langle k\rangle}$, and $\langle k\rangle$ is the scale of the network. In a scale-free network with $2 < \gamma < 3$ the fluctuations are unbounded: a randomly chosen vertex may have degree $2$ or $20{,}000$, and the mean is not a typical value. The quantity $\kappa = \langle k^2\rangle/\langle k\rangle$ of Section 7.1.2 diverges with $N$, which is the source of the anomalous robustness and epidemic properties of Section 7.8.

### 7.4.4. Three Regimes of the Degree Exponent

The value of $\gamma$ divides scale-free networks into three regimes.

*$\gamma < 2$: no large simple networks.* The natural cutoff $N^{1/(\gamma-1)}$ exceeds $N - 1$, and the mean degree diverges. Not every sequence of integers is the degree sequence of a simple graph, and the Erdős–Gallai theorem says which are.

**Theorem 7.4.1 (Erdős–Gallai, 1960)** A sequence of integers $d_1 \geq d_2 \geq \cdots \geq d_N \geq 0$ with even sum is the degree sequence of a simple graph if and only if for every $r = 1, \dots, N$,

$$
\sum_{i=1}^r d_i \leq r(r-1) + \sum_{i = r+1}^N\min(d_i, r).
$$

For large $N$, degree sequences drawn from a power law with $\gamma < 2$ violate this condition with probability tending to $1$ (Del Genio, Gross and Bassler, 2011): the hubs need more distinct partners than exist. Such distributions can occur only in multigraphs or in networks whose size is bounded.

*$2 < \gamma < 3$: ultra-small worlds.* The hubs connect to each other and act as a backbone through which most short paths run. In random networks with such degree distributions the average distance grows only like $\ln\ln N$ (Cohen and Havlin, 2003; Chung and Lu, 2002), a regime called the *ultra-small world*. At $\gamma = 3$ the growth is $\ln N/\ln\ln N$.

*$\gamma > 3$: close to random.* The second moment is finite, the network behaves in most respects like a random graph with the same mean degree, and $\langle d\rangle \sim \ln N/\ln\langle k\rangle$. A large $\gamma$ is also hard to detect: to see a power law over two decades, $k_{\max}/k_{\min} \approx 10^2$, Proposition 7.4.2 requires $N \approx 10^{2(\gamma - 1)}$ vertices, $10^8$ for $\gamma = 5$.

| Exponent | $\langle k\rangle$ | $\langle k^2\rangle$ | Distances | Behavior |
|---|---|---|---|---|
| $\gamma < 2$ | diverges | diverges | — | not graphical for large $N$ |
| $\gamma = 2$ | $\sim \ln N$ | diverges | constant | largest hub of order $N$ |
| $2 < \gamma < 3$ | finite | diverges | $\sim \ln\ln N$ | ultra-small world |
| $\gamma = 3$ | finite | $\sim \ln N$ | $\sim \ln N/\ln\ln N$ | critical |
| $\gamma > 3$ | finite | finite | $\sim \ln N$ | like a random graph |

### 7.4.5. Measuring a Power Law

Deciding whether a degree distribution follows a power law, and estimating $\gamma$, is a statistical problem, and the common graphical methods are biased.

The naive method is to plot $p_k = N_k/N$ against $k$ on log–log axes and fit a straight line by least squares. With linear bins of width $1$, most bins in the tail contain zero or one vertex: the points of the tail form a plateau at $1/N$ and the zeros cannot be plotted, so the fitted slope is wrong. Logarithmic bins (widths growing geometrically, counts divided by the bin width) and the complementary cumulative distribution $P_k$, which needs no binning and has a slope $-(\gamma - 1)$, give much clearer pictures. But even a well-made plot does not justify a least-squares fit: the residuals are neither independent nor equally variable, the estimate is biased, and the reported $R^2$ says nothing about whether the power law is the right model (Clauset, Shalizi and Newman, 2009). The estimator with good properties is the maximum-likelihood estimator.

**Algorithm 7.4.1 (Fitting a Power Law)** (Clauset, Shalizi and Newman, 2009) Given observed degrees $k_1, \dots, k_n$:

1. For each candidate lower bound $k_{\min}$, take the $n_{\mathrm{tail}}$ observations with $k_i \geq k_{\min}$ and estimate the exponent by **maximum likelihood estimation**. For the continuous power law the log-likelihood is $\ell(\gamma) = n_{\mathrm{tail}}\ln(\gamma - 1) - n_{\mathrm{tail}}\ln k_{\min} - \gamma\sum\ln(k_i/k_{\min})$, maximized at
   $$
   \hat\gamma = 1 + n_{\mathrm{tail}}\left[\sum_{k_i \geq k_{\min}}\ln\frac{k_i}{k_{\min}}\right]^{-1},
   $$
   with standard error $(\hat\gamma - 1)/\sqrt{n_{\mathrm{tail}}}$ from the Fisher information $n_{\mathrm{tail}}/(\gamma - 1)^2$. For integer data one maximizes the discrete likelihood with $\zeta(\gamma, k_{\min})$ numerically, or uses the continuous formula with $k_{\min}$ replaced by $k_{\min} - \frac12$, which is accurate for $k_{\min} \gtrsim 6$.
2. Choose $k_{\min}$ to minimize the Kolmogorov–Smirnov distance $D = \max_{k \geq k_{\min}}\lvert F_n(k) - F(k; \hat\gamma)\rvert$ between the empirical and the fitted distribution functions of the tail.
3. Test goodness of fit by a semiparametric **bootstrap**: generate many synthetic data sets of size $n$ (the part below $k_{\min}$ resampled from the data, the tail drawn from the fitted power law), repeat steps 1–2 on each, and take as **p-value** the fraction of synthetic data sets whose distance $D$ exceeds the observed one. The power law is rejected if $p \leq 0.1$.
4. Compare with alternative heavy-tailed distributions (log-normal, stretched exponential, power law with exponential cutoff) by a **likelihood ratio test**, normalized as in Vuong's test, since a power law that is not rejected may still be worse than an alternative.

The **Kolmogorov–Smirnov test** cannot be used with its standard tables in step 3, because the parameters were estimated from the same data; this is why the bootstrap is needed.

![Degree distributions of an Erdős–Rényi graph (N = 50,000, mean degree 6, blue) and a Barabási–Albert graph (N = 50,000, m = 3, red), plotted three ways. A: linear bins on log–log axes; the tail of the power law dissolves into a plateau of single vertices. B: logarithmic bins, with the Poisson distribution (blue line) and the exact Barabási–Albert distribution of Theorem 7.5.1 (dashed). C: the complementary cumulative distribution P(K ≥ k), with the maximum-likelihood power law fitted above the k_min chosen by the Kolmogorov–Smirnov criterion (Algorithm 7.4.1): γ̂ = 2.96, k_min = 51](./plots/degree_distributions.py)

**Example 7.4.2** For the Barabási–Albert graph of the figure, whose exact degree distribution has $\gamma = 3$ asymptotically (Theorem 7.5.1), Algorithm 7.4.1 selects $k_{\min} = 51$, leaving $233$ of the $50{,}000$ vertices in the tail, and gives $\hat\gamma = 2.96 \pm 0.13$. The selected $k_{\min}$ is large because $2m(m+1)/[k(k+1)(k+2)]$ approaches $k^{-3}$ only slowly; the price is a small tail sample and a wide confidence interval. The largest degree is $715$, close to $mN^{1/2} \approx 671$ (Section 7.5.2), while the largest degree of the random graph with the same number of vertices is $18$.

How common are scale-free networks? In the years after 1999 power laws were reported for the Web, the Internet, citations, collaborations, protein interactions and metabolism, usually from straight lines on log–log plots. Broido and Clauset (2019) applied Algorithm 7.4.1 to nearly a thousand networks from many domains and found the strongest evidence for a power-law tail in only about 4% of them, while about half showed only the weakest evidence; social networks were at best weakly scale free, a few technological and biological networks strongly so, and log-normal distributions often fitted as well or better. The response was that the conclusion depends on the definition: Voitalov and colleagues (2019) argued that a scale-free network should be defined by a regularly varying tail $p_k = \ell(k)k^{-\gamma}$ with a slowly varying factor $\ell$ rather than by a pure power law above $k_{\min}$, and with consistent estimators for that definition found heavy tails with $2 < \gamma < 3$ to be common. The current consensus (Holme, 2019) is that degree distributions of real networks are almost always heavy-tailed, far broader than Poisson, but that "scale free" is a hypothesis to be tested on each network with explicit statistics, not a universal law; the consequences in Section 7.8 depend mainly on the size of $\langle k^2\rangle$, not on the exact form of the tail.

### 7.4.6. Generating Networks with a Given Degree Sequence

To ask whether a property of a real network, say its clustering or the frequency of some subgraph, is explained by its degree distribution alone, we need random networks with the same degrees and otherwise random wiring.

**Definition 7.4.3 (Configuration Model)** Let $k_1, \dots, k_N$ be nonnegative integers with even sum $2M$. Give vertex $i$ exactly $k_i$ *stubs* (half-edges) and pair the $2M$ stubs uniformly at random, every perfect matching of the stubs being equally likely; each pair of stubs becomes an edge. The resulting random multigraph is the **configuration model** with degree sequence $(k_i)$ (Bender and Canfield, 1978; Bollobás, 1980; Molloy and Reed, 1995).

A given stub of vertex $i$ is paired with one of the $k_j$ stubs of vertex $j \neq i$ with probability $k_j/(2M - 1)$, so the expected number of edges between $i$ and $j$ is

$$
\frac{k_ik_j}{2M - 1} \approx \frac{k_ik_j}{2M},
$$

which will reappear as the null model of modularity (Section 7.7.2). The configuration model can produce self-loops and multiple edges. Summing the probabilities over vertices and pairs gives expected numbers of about $(\kappa - 1)/2$ self-loops and $(\kappa - 1)^2/4$ pairs of parallel edges, $\kappa = \langle k^2\rangle/\langle k\rangle$; when $\langle k^2\rangle$ is finite these are $O(1)$, a vanishing fraction of the $M$ edges, and they can be discarded. For heavy-tailed degrees they grow with $N$, and one uses instead the following procedure, which preserves simplicity.

**Algorithm 7.4.2 (Degree-Preserving Randomization)** (Maslov and Sneppen, 2002) Start from the observed simple graph. Repeat many times (a common choice is $10M$ times): choose two edges $\{a, b\}$ and $\{c, d\}$ uniformly at random; if $a, b, c, d$ are distinct and neither $\{a, d\}$ nor $\{c, b\}$ is an edge, replace the two edges by $\{a, d\}$ and $\{c, b\}$. For directed networks, swap the heads of two arcs $a \to b$, $c \to d$ to $a \to d$, $c \to b$, which preserves every in- and out-degree.

**Definition 7.4.4 (Degree-Preserving Randomization)** The ensemble of simple graphs produced by Algorithm 7.4.2 from a network, all of which have exactly its degree sequence, is the **degree-preserving randomization** of the network; it is the standard null model for testing whether a structural property goes beyond what the degrees imply.

Each swap preserves all degrees, and the swap chain is a **Markov chain** on the simple graphs with the given degree sequence. For undirected graphs any two such graphs are connected by a sequence of swaps (Taylor, 1981), and since rejected swaps leave the graph unchanged the chain is symmetric, so with enough swaps it samples nearly uniformly from all simple graphs with the observed degrees. (For digraphs, swaps alone may not connect all realizations; reversals of directed triangles must be added.) Comparing an observed statistic $X$ with its distribution over randomized networks gives a z-score $z = (X - \bar X_{\mathrm{rand}})/s_{\mathrm{rand}}$ and an empirical p-value; this is how network motifs are detected (Section 7.8.4).

A third construction gives a prescribed degree distribution in expectation rather than exactly. In the *hidden-parameter model* (Caldarelli and colleagues, 2002; Chung and Lu, 2002) each vertex receives a weight $\eta_i$ drawn from a distribution $\rho(\eta)$, and each pair is joined independently with probability $p_{ij} = \eta_i\eta_j/(N\langle\eta\rangle)$, which requires $\eta_{\max}^2 \leq N\langle\eta\rangle$. The expected degree of $i$ is then $\eta_i$, and the graph is simple by construction.

```python
from collections import Counter
import networkx as nx
import numpy as np

N = 10_000
er = nx.gnp_random_graph(N, 4 / (N - 1), seed=1)        # G(N, p) with mean degree 4
ba = nx.barabasi_albert_graph(N, 2, seed=1)             # BA model with m = 2 (Section 7.5)
for name, g in [("ER", er), ("BA", ba)]:
    k = np.array([d for _, d in g.degree()])
    giant = max(nx.connected_components(g), key=len)
    print(name, k.mean(), (k**2).mean() / k.mean(), k.max(), len(giant) / N)
# ER 4.014 5.015 14 0.9826     (Eq. (7.1) with c = 4 gives S = 0.980)
# BA 3.999 14.67 264 1.0

# Configuration model with the degree sequence of the BA graph: count self-loops and parallel edges
cm = nx.configuration_model([d for _, d in ba.degree()], seed=1)
mult = Counter(tuple(sorted(e)) for e in cm.edges())
loops = sum(c for (u, v), c in mult.items() if u == v)
pairs = sum(c * (c - 1) // 2 for (u, v), c in mult.items() if u != v)
print(loops, pairs)    # 10 47     (expected: (kappa - 1)/2 = 6.8 and (kappa - 1)^2/4 = 46.7)

# Degree-preserving randomization (Algorithm 7.4.2)
rnd = ba.copy()
nx.double_edge_swap(rnd, nswap=10 * rnd.number_of_edges(), max_tries=10**7, seed=1)
```

## 7.5. Growing Networks: Preferential Attachment

### 7.5.1. The Barabási–Albert Model

Why should the Web, citations and protein interactions share heavy-tailed degree distributions? Barabási and Albert (1999) pointed to two features that random graphs lack. Real networks grow: the Web gains pages, the literature gains papers, genomes gain genes by duplication; the random graph has a fixed set of vertices. And new edges are not placed at random: a new page links preferably to well-known pages, a new paper cites papers that are already much cited. Together these produce a power law.

**Definition 7.5.1 (Preferential Attachment)** In a growing network, new edges attach by **preferential attachment** if the probability that a new edge ends at an existing vertex $i$ is proportional to its degree,

$$
\Pi(k_i) = \frac{k_i}{\sum_jk_j}.
$$

More generally, *nonlinear* preferential attachment has $\Pi(k_i) \propto k_i^\alpha$ with $\alpha > 0$.

**Definition 7.5.2 (Barabási–Albert Model)** Fix an integer $m \geq 1$. Start from a small connected graph with $m_0 \geq m$ vertices. At each time step $t = 1, 2, \dots$, add one new vertex with $m$ edges joining it to $m$ distinct existing vertices, each chosen by preferential attachment (Definition 7.5.1). The resulting sequence of growing random graphs is the **Barabási–Albert model** (BA model).

After $t$ steps the network has $N \approx t$ vertices and $M \approx mt$ edges, so $\langle k\rangle \to 2m$. Preferential attachment is easy to simulate without computing $\Pi$: keep a list in which every vertex appears once for each of its edge ends; a uniformly random entry of this list is a vertex chosen with probability proportional to its degree.

### 7.5.2. Degree Dynamics

Treat the degree $k_i(t)$ of the vertex added at time $t_i$ as a continuous variable that changes at its expected rate. Each new vertex brings $m$ edges, each landing on $i$ with probability $k_i/\sum_jk_j = k_i/(2mt)$, since the total degree is $2mt$.

**Proposition 7.5.1** In the continuum approximation, the degree of the vertex added at time $t_i$ satisfies

$$
\frac{\mathrm{d}k_i}{\mathrm{d}t} = m\,\frac{k_i}{2mt} = \frac{k_i}{2t}, \qquad k_i(t_i) = m,
$$

so that $k_i(t) = m(t/t_i)^{1/2}$.

**Proof** Separate the variables: $\mathrm{d}\ln k_i = \frac{1}{2}\mathrm{d}\ln t$; integrate from $t_i$ to $t$. $\square$

All vertices gain edges according to the same power of time, with *dynamical exponent* $\beta = 1/2$, and the rate $\mathrm{d}k_i/\mathrm{d}t = \frac{m}{2}(t\,t_i)^{-1/2}$ decreases with time. The vertices that differ are those that arrived early: a vertex added at $t_i = 10$ has, at $t = 10^5$, about $\sqrt{10^4} = 100$ times the degree of one added at $t_i = 10^5$. This *first-mover advantage* is the mechanism that produces hubs in the BA model.

![Growth with and without preferential attachment, m = 3 edges per new vertex, N = 100,000. A: in the Barabási–Albert model, the degree k_i(t) of the vertices added at t_i = 10, 100, 1000 and 10,000 (averaged over the vertices t_i, …, t_i + t_i/20 and four realizations), with the prediction m(t/t_i)^(1/2) of Proposition 7.5.1. B: the degree distribution with preferential attachment follows the power law of Theorem 7.5.1 (red line); with growth but uniform attachment it is geometric (blue line), with no hubs](./plots/ba_growth.py)

### 7.5.3. The Degree Distribution

The continuum approximation already gives the exponent. The vertices are added uniformly in time, so at time $t$ the arrival time $t_i$ of a random vertex is approximately uniform on $[0, t]$, and

$$
\mathbb{P}(k_i(t) < k) = \mathbb{P}\!\left(t_i > \frac{m^2t}{k^2}\right) = 1 - \frac{m^2}{k^2},
$$

whose derivative is the density $p(k) = 2m^2k^{-3}$. The exact stationary distribution follows from a rate equation.

**Theorem 7.5.1** In the Barabási–Albert model the expected fraction of vertices of degree $k$ converges, as $t \to \infty$, to

$$
p_k = \frac{2m(m+1)}{k(k+1)(k+2)}, \qquad k \geq m, \tag{7.2}
$$

so $p_k \sim 2m^2k^{-3}$ and $\gamma = 3$, independently of $m$.

**Proof** Let $N_k(t)$ be the expected number of vertices of degree $k$ at time $t$. A new vertex attaches each of its $m$ edges to a given vertex of degree $k$ with probability $k/(2mt)$, so the expected number of degree-$k$ vertices that gain an edge is $m \cdot kN_k/(2mt) = kN_k/(2t)$ (the probability that one vertex receives two of the $m$ edges is of smaller order). Vertices of degree $k$ are created by edges landing on vertices of degree $k-1$, and lost by edges landing on vertices of degree $k$; in addition each step creates one vertex of degree $m$:

$$
N_k(t+1) - N_k(t) = \frac{(k-1)N_{k-1}(t) - kN_k(t)}{2t} + \delta_{km},
$$

with $N_{m-1} = 0$. Suppose that $N_k(t) = tp_k + o(t)$, which can be justified a posteriori. Then the left side tends to $p_k$, and

$$
p_k = \frac{(k-1)p_{k-1} - kp_k}{2} + \delta_{km}.
$$

For $k = m$ this gives $p_m = 1 - mp_m/2$, that is, $p_m = 2/(m+2)$. For $k > m$ it gives $p_k = \frac{k-1}{k+2}p_{k-1}$, and the product telescopes:

$$
p_k = p_m\prod_{j=m+1}^k\frac{j-1}{j+2} = \frac{2}{m+2}\cdot\frac{m(m+1)(m+2)}{k(k+1)(k+2)} = \frac{2m(m+1)}{k(k+1)(k+2)}. \qquad \square
$$

As a check, the distribution is normalized and has mean $2m$: from $\frac{1}{k(k+1)(k+2)} = \frac12\left[\frac{1}{k(k+1)} - \frac{1}{(k+1)(k+2)}\right]$ the sum $\sum_{k \geq m}p_k$ telescopes to $1$, and $\sum_{k\geq m}kp_k = 2m(m+1)\sum_{k\geq m}\left[\frac{1}{k+1} - \frac{1}{k+2}\right] = 2m$. The exponent $\gamma = 3$ does not depend on $m$, and the distribution does not depend on $t$ or $N$: the network reaches a stationary, scale-free state. A rigorous version of Theorem 7.5.1, for a precisely specified model, was proved by Bollobás, Riordan, Spencer and Tusnády (2001).

### 7.5.4. Both Ingredients Are Necessary

*Growth without preferential attachment.* If each new vertex joins $m$ existing vertices chosen uniformly, a given vertex receives an edge with probability $m/t$ per step. The rate equation becomes $p_k = m(p_{k-1} - p_k) + \delta_{km}$, with solution

$$
p_k = \frac{1}{m+1}\left(\frac{m}{m+1}\right)^{k-m}, \qquad k \geq m,
$$

a geometric distribution, which decays exponentially (figure above, panel B). Older vertices still have higher degree, $k_i(t) \approx m + m\ln(t/t_i)$, but only logarithmically higher.

*Preferential attachment without growth.* If $N$ is fixed and edges are added between existing vertices with preferential attachment, the degree distribution looks like a power law at first, but since the number of edges increases while $N$ does not, all degrees grow linearly in time, the distribution becomes Gaussian around its increasing mean, and after about $N^2/2$ steps the network is complete.

Both ingredients are therefore necessary for a stationary power law.

### 7.5.5. Measuring Preferential Attachment and Nonlinear Attachment

Whether a real network grows by preferential attachment can be measured if the times at which edges appear are known. Compare two snapshots of the network: $\Pi(k) \approx \Delta k_i/\Delta t$ as a function of the earlier degree $k_i$. The estimates are noisy, so one plots the cumulative function $\pi(k) = \sum_{k' < k}\Pi(k')$, which grows like $k^{\alpha+1}$ if $\Pi(k) \sim k^\alpha$: like $k^2$ for linear preferential attachment and like $k$ for none. Measurements on the Internet and on citation networks gave $\alpha \approx 1$; on coauthorship and actor networks, $\alpha \approx 0.8$ (Jeong, Néda and Barabási, 2003).

The exponent $\alpha$ matters (Krapivsky, Redner and Leyvraz, 2000):

| Attachment | Degree distribution | Largest hub |
|---|---|---|
| $\alpha = 0$ (uniform) | exponential | $\sim \ln t$ |
| $0 < \alpha < 1$ (sublinear) | stretched exponential, $p_k \sim k^{-\alpha}\exp\!\left(-bk^{1-\alpha}\right)$ | $\sim (\ln t)^{1/(1-\alpha)}$ |
| $\alpha = 1$ (linear) | power law, $\gamma = 3$ | $\sim t^{1/2}$ |
| $\alpha > 1$ (superlinear) | one vertex acquires a finite fraction of all edges ("winner takes all") | $\sim t$ |

A power law requires preferential attachment that is asymptotically linear; any sublinearity bends the distribution down, any superlinearity concentrates the edges on a single hub.

### 7.5.6. Where Preferential Attachment Comes From

Preferential attachment seems to assume that a new vertex knows the degrees of all vertices. Two kinds of mechanism explain how it can arise without this knowledge.

*Local random mechanisms.* In the link-selection model, a new vertex picks an existing edge uniformly at random and attaches to one of its two ends. A vertex of degree $k$ is an end of $k$ edges, so it is chosen with probability proportional to $k$: exactly the size-biased sampling of Section 7.1.2, $\Pi(k) = kp_k/\langle k\rangle$ per degree class. In the copying model (Kleinberg and colleagues, 1999), a new vertex chooses a random existing vertex $u$; with probability $\beta$ it links to $u$, and with probability $1 - \beta$ it copies one of $u$'s edges, linking to its endpoint. The second option reaches a vertex of degree $k$ with probability proportional to $k$, so $\Pi(k) = \beta/N + (1 - \beta)k/(2M)$, linear preferential attachment with an offset. Copying describes many real processes: we befriend the friends of our friends, authors copy references from the papers they read, and a duplicated gene inherits the interaction partners of its parent; the duplication–divergence model of protein interaction networks and its biological evidence are discussed in [7.9.17](/7.9.17).

*Optimization.* In the model of Fabrikant, Koutsoupias and Papadimitriou (2002), vertices arrive at random positions in the plane and each joins the existing vertex $j$ that minimizes $\delta d_{ij} + h_j$, a weighted sum of the cable length $d_{ij}$ and the network distance $h_j$ from $j$ to a central vertex. For small $\delta$ the network becomes a star; for $\delta$ of order $\sqrt{N}$ or larger the distance cost dominates and the degrees are exponentially distributed; in between the degree distribution is heavy-tailed. Here hubs arise from a global trade-off, not from chance.

### 7.5.7. Diameter and Clustering of the BA Model

For $m \geq 2$ the BA network is connected, and its diameter grows like $\ln N/\ln\ln N$ (Bollobás and Riordan, 2004), shorter than a random graph's, as expected from Section 7.4.4 for $\gamma = 3$. Its average clustering coefficient decreases like $(\ln N)^2/N$ (Klemm and Eguíluz, 2002), slower than the $1/N$ of a random graph but still vanishing, whereas the clustering of most real networks does not decrease with size. The BA model is a minimal model. It explains why heavy-tailed degrees arise, but it fixes $\gamma = 3$, it has no clustering and no communities, and its first-mover advantage contradicts the many late arrivals that became hubs.

### 7.5.8. Evolving Networks and Fitness

Google appeared years after the first search engines and overtook them. To let latecomers win, Bianconi and Barabási (2001) gave each vertex an intrinsic attractiveness.

**Definition 7.5.3 (Bianconi–Barabási Model)** Each new vertex $i$ receives a *fitness* $\eta_i > 0$ drawn independently from a distribution $\rho(\eta)$, and its $m$ edges attach to existing vertices with probability proportional to the product of fitness and degree,

$$
\Pi_i = \frac{\eta_ik_i}{\sum_j\eta_jk_j}.
$$
This growing network is the **Bianconi–Barabási model**, or fitness model.

In the continuum approximation one finds $k_i(t) = m(t/t_i)^{\beta(\eta_i)}$ with a fitness-dependent exponent $\beta(\eta) = \eta/C$, where the constant $C$ is determined by $\int\rho(\eta)\frac{\eta}{C - \eta}\,\mathrm{d}\eta = 1$; a fitter vertex grows faster and eventually overtakes older but less fit vertices ("fit get richer"). For uniform fitness on $[0, 1]$ the condition becomes $C\ln\frac{C}{C-1} = 2$, so $C \approx 1.255$, and the degree distribution is $p_k \sim k^{-(1+C)}/\ln k \approx k^{-2.255}/\ln k$. Measuring fitness is possible because $\ln k_i(t) = \beta(\eta_i)\ln t + \text{const}$: the slope of each vertex's degree trajectory on log–log axes estimates its fitness.

Writing $\eta_i = \mathrm{e}^{-\varepsilon_i/\tau}$, with $\tau$ playing the role of a temperature, maps the model onto a Bose gas, each vertex becoming an energy level $\varepsilon_i$ and each edge end a particle occupying that level. For some fitness distributions the equation for $C$ has no solution; then a finite fraction of all edges condenses onto the fittest vertex, the analogue of **Bose–Einstein condensation**, and the network becomes star-like (Bianconi and Barabási, 2001).

Real networks also change in ways that the BA model ignores. Each mechanism below has been added to the model and its effect on the degree distribution computed:

| Mechanism | Model | Effect on the degree distribution |
|---|---|---|
| Initial attractiveness | $\Pi(k) \propto A + k$ | $\gamma = 3 + A/m$: power law with a saturated low-degree part |
| Internal links | each step also adds $n$ edges between existing vertices, both ends by preferential attachment | $\gamma = 2 + m/(m + 2n)$, between $2$ and $3$ |
| Node deletion | vertices removed at random | power law preserved with increased $\gamma$, unless deletion outpaces growth |
| Aging | $\Pi \propto k\,(t - t_i)^{-\nu}$ | $\gamma$ increases with $\nu$; for $\nu > 1$ the power law is lost (Dorogovtsev and Mendes, 2000) |

The first two entries follow from Proposition 7.5.1 with modified rates. With initial attractiveness, $\mathrm{d}k_i/\mathrm{d}t = m(k_i + A)/[(2m + A)t]$, so $k_i + A \sim t^{\beta}$ with $\beta = m/(2m + A)$ and $\gamma = 1 + 1/\beta = 3 + A/m$. With $n$ internal edges per step, a vertex gains $(m + 2n)k_i/[2(m+n)t]$ edge ends per step, so $\beta = (m + 2n)/[2(m+n)]$ and $\gamma = 1 + 1/\beta = 2 + m/(m + 2n)$.

### 7.5.9. Example: Citation Networks

Citation networks are the best-measured growing networks: every paper is a vertex that arrives at a known time and never changes its references. Two studies of the Web of Science illustrate the methods of this chapter.

*Being cited.* Wang, Song and Barabási (2013) modeled the probability that paper $i$ receives a new citation at time $t$ after publication as $\Pi_i(t) \propto \eta_ic_i^tP_i(t)$: preferential attachment to its current citation count $c_i^t$, an intrinsic fitness $\eta_i$, and an aging factor $P_i(t)$, a log-normal density in $t$ with parameters $\mu_i$ (immediacy) and $\sigma_i$ (decay). Solving the resulting rate equation gives the cumulative citations

$$
c_i^t = m\left[\exp\!\left(\lambda_i\,\Phi\!\left(\frac{\ln t - \mu_i}{\sigma_i}\right)\right) - 1\right],
$$
where $\Phi$ is the standard normal distribution function, $\lambda_i$ is the relative fitness and $m$ a constant of the whole literature (about $30$). The ultimate impact $c_i^\infty = m(\mathrm{e}^{\lambda_i} - 1)$ depends only on $\lambda_i$, not on how quickly the paper was noticed, so long-term impact can be estimated from the early citation history once $\lambda_i$, $\mu_i$, $\sigma_i$ are fitted. The model also explains why the citations of a paper and the impact factor of its journal are poorly correlated: the impact factor counts only the first two years.

*Citing.* Uzzi, Mukherjee, Stringer and Jones (2013) asked whether influential papers combine prior work in unusual ways. For each pair of journals cited together in the reference lists of about 17.9 million papers, they compared the observed number of co-citations with its distribution in randomized citation networks in which each citation was moved to a paper of the same year, a degree-preserving randomization (Algorithm 7.4.2). The resulting z-score measures how conventional ($z \gg 0$) or atypical ($z < 0$) each combination is. Each paper is summarized by the median z-score of its pairs (conventionality) and its 10th percentile (novelty). Papers that combined a highly conventional core with a small number of atypical combinations were the most likely to be among the most cited of their field and year, and teams were more likely than single authors to produce such papers.

## 7.6. Centrality

Which vertices of a network are the most important? There is no single answer; each centrality measure formalizes a different notion of importance, and each is the solution of a specific question about paths or walks.

### 7.6.1. Degree, Closeness and Betweenness

**Definition 7.6.1 (Centrality)** A **centrality** is a function that assigns to each vertex of a network a nonnegative number measuring its importance in the network structure. For a connected network:

1. the *degree centrality* of $i$ is its degree $k_i$ (often divided by $N - 1$);
2. the **closeness centrality** of $i$ is the reciprocal of its mean distance to the other vertices,
   $$
   C_{\mathrm{c}}(i) = \frac{N - 1}{\sum_{j \neq i}d(i, j)};
   $$
   for disconnected networks the *harmonic centrality* $\frac{1}{N-1}\sum_{j \neq i}1/d(i, j)$ is used instead.

Degree centrality is local; closeness measures how quickly information from $i$ can reach everyone. The third classical measure counts how often a vertex lies between others.

**Definition 7.6.2 (Betweenness Centrality)** Let $\sigma_{st}$ be the number of shortest paths from $s$ to $t$ and $\sigma_{st}(v)$ the number of them that pass through $v$. The **betweenness centrality** of $v$ is

$$
C_{\mathrm{B}}(v) = \sum_{s \neq v \neq t}\frac{\sigma_{st}(v)}{\sigma_{st}},
$$

the sum running over unordered pairs $\{s, t\}$ of vertices different from $v$ in an undirected network (Freeman, 1977). The *edge betweenness* of an edge is defined in the same way with paths through the edge.

A vertex of high betweenness controls the flow between parts of the network: removing it lengthens many shortest paths. Computing $\sigma_{st}(v)$ for all triples naively costs $O(N^3)$ or more; Brandes found a much faster way.

**Algorithm 7.6.1 (Brandes, 2001)** For each source $s$:

1. Run a breadth-first search from $s$, recording the distance $d(s, v)$, the number $\sigma_{sv}$ of shortest paths from $s$ to $v$ (with $\sigma_{ss} = 1$ and $\sigma_{sw} = \sum_{v \in P_s(w)}\sigma_{sv}$, where $P_s(w)$ is the set of predecessors of $w$, the neighbors at distance $d(s, w) - 1$), and the order in which vertices are reached.
2. Process the vertices in order of decreasing distance and accumulate the *dependencies*
   $$
   \delta_s(v) = \sum_{w\colon v \in P_s(w)}\frac{\sigma_{sv}}{\sigma_{sw}}\bigl(1 + \delta_s(w)\bigr).
   $$
3. Add $\delta_s(v)$ to $C_{\mathrm{B}}(v)$ for every $v \neq s$.

Finally divide by $2$ for an undirected network. The running time is $O(NM)$ and the memory $O(N + M)$; with Dijkstra's algorithm in place of breadth-first search it handles weighted networks in $O(NM + N^2\ln N)$.

The recursion in step 2 holds because a shortest path from $s$ to some $t$ that passes through $v$ continues through exactly one successor $w$ of $v$, and the fraction of shortest $s$–$w$ paths that pass through $v$ is $\sigma_{sv}/\sigma_{sw}$.

### 7.6.2. Eigenvector and Katz Centrality

Degree counts neighbors, but a link from an important vertex should count more than one from an unimportant vertex. Defining the importance $x_i$ of $i$ as proportional to the sum of the importances of its neighbors gives $\lambda x_i = \sum_jA_{ij}x_j$, an **eigenvector** equation. Which eigenvector? The following classical theorem guarantees a meaningful choice.

**Theorem 7.6.1 (Perron–Frobenius)** Let $A$ be a nonnegative square matrix that is irreducible, that is, the digraph with an arc $i \to j$ whenever $A_{ij} > 0$ is strongly connected. Then the **spectral radius** $\rho(A)$ is a simple eigenvalue of $A$, it has an eigenvector with all components positive, and no other eigenvalue has a nonnegative eigenvector.

For the adjacency matrix of a connected undirected graph the theorem applies, and $\rho(A) = \lambda_1$ is the largest eigenvalue.

**Definition 7.6.3 (Eigenvector Centrality)** The **eigenvector centrality** of the vertices of a connected undirected network is the positive eigenvector $\boldsymbol{x}$ of its adjacency matrix belonging to the largest eigenvalue $\lambda_1$, $A\boldsymbol{x} = \lambda_1\boldsymbol{x}$, normalized (for example so that $\max_ix_i = 1$) (Bonacich, 1972).

It is computed by the **power method**: $\boldsymbol{x}^{(t+1)} = A\boldsymbol{x}^{(t)}/\lVert A\boldsymbol{x}^{(t)}\rVert$ converges to it from any positive start if $G$ is also not bipartite. For directed networks eigenvector centrality fails: a vertex with no incoming arcs gets $0$, and so does every vertex reached only from such vertices. Katz (1953) added a constant to every vertex,

$$
\boldsymbol{x} = \alpha A\boldsymbol{x} + \boldsymbol{1}, \qquad \boldsymbol{x} = (I - \alpha A)^{-1}\boldsymbol{1} = \sum_{n=0}^\infty\alpha^nA^n\boldsymbol{1}, \qquad 0 < \alpha < 1/\rho(A).
$$

By Theorem 2.2.1, $(A^n\boldsymbol{1})_i$ is the number of walks of length $n$ starting at $i$ (or ending at $i$, using $A^{\mathsf T}$), so the Katz centrality counts all walks with weight $\alpha^n$ for length $n$. As $\alpha \to 1/\rho(A)$ it approaches eigenvector centrality, and as $\alpha \to 0$, after subtracting $1$ and dividing by $\alpha$, degree centrality.

### 7.6.3. PageRank

A web page that links to a thousand others should not pass a thousand votes. PageRank (Brin and Page, 1998) divides each vertex's importance among its outgoing links and adds random jumps, so that it is defined for every directed network.

**Definition 7.6.4 (PageRank)** Let $A$ be the adjacency matrix of a digraph ($A_{ij} = 1$ if $i \to j$) and $k_i^{\mathrm{out}}$ the out-degree of $i$. Let $P$ be the row-stochastic matrix with $P_{ij} = A_{ij}/k_i^{\mathrm{out}}$ if $k_i^{\mathrm{out}} > 0$ and $P_{ij} = 1/N$ if $i$ has no outgoing arcs (a *dangling* vertex). For a damping factor $0 < \alpha < 1$, the **PageRank** vector is the probability vector $\boldsymbol{\pi}$ satisfying

$$
\boldsymbol{\pi} = \alpha P^{\mathsf T}\boldsymbol{\pi} + \frac{1 - \alpha}{N}\boldsymbol{1}. \tag{7.3}
$$

The usual choice is $\alpha = 0.85$.

Eq. (7.3) describes a random surfer: at each step, with probability $\alpha$ follow a random outgoing link of the current page (or jump to a random page from a dangling one), and with probability $1 - \alpha$ jump to a page chosen uniformly. The PageRank $\pi_i$ is the long-run fraction of time spent at page $i$, the **stationary distribution** of the **Markov chain** with transition matrix $\alpha P + (1 - \alpha)\boldsymbol{1}\boldsymbol{1}^{\mathsf T}/N$. That chain is irreducible and aperiodic, since all its entries are positive, so the stationary distribution exists, is unique and is the limit from any start ([Theorem 9.3.3](/3.5.9#thm-9.3.3)). A direct argument also gives the rate of convergence.

**Proposition 7.6.1** Eq. (7.3) has a unique solution in the set $\Delta$ of probability vectors, and for every $\boldsymbol{\pi}^{(0)} \in \Delta$ the iteration $\boldsymbol{\pi}^{(t+1)} = \alpha P^{\mathsf T}\boldsymbol{\pi}^{(t)} + (1 - \alpha)\boldsymbol{1}/N$ satisfies $\lVert\boldsymbol{\pi}^{(t)} - \boldsymbol{\pi}\rVert_1 \leq \alpha^t\lVert\boldsymbol{\pi}^{(0)} - \boldsymbol{\pi}\rVert_1 \leq 2\alpha^t$.

**Proof** Let $T(\boldsymbol{x}) = \alpha P^{\mathsf T}\boldsymbol{x} + (1 - \alpha)\boldsymbol{1}/N$. Since $P^{\mathsf T}$ is nonnegative with columns summing to $1$, $T$ maps $\Delta$ into $\Delta$, and for any vector $\boldsymbol{y}$, $\lVert P^{\mathsf T}\boldsymbol{y}\rVert_1 \leq \sum_j\sum_iP_{ij}\lvert y_i\rvert = \lVert\boldsymbol{y}\rVert_1$. Hence $\lVert T\boldsymbol{x} - T\boldsymbol{x}'\rVert_1 = \alpha\lVert P^{\mathsf T}(\boldsymbol{x} - \boldsymbol{x}')\rVert_1 \leq \alpha\lVert\boldsymbol{x} - \boldsymbol{x}'\rVert_1$: $T$ is a contraction of the closed set $\Delta$, and by the Banach fixed-point theorem it has a unique fixed point $\boldsymbol{\pi}$, approached at the stated rate. Two probability vectors are at $\ell^1$ distance at most $2$. $\square$

With $\alpha = 0.85$ the bound guarantees an error below $10^{-8}$ after $\ln(10^{-8})/\ln 0.85 \approx 113$ iterations, whatever the size of the network; each iteration costs $O(N + M)$ because $P^{\mathsf T}\boldsymbol{\pi}$ is a sparse matrix–vector product. This is why PageRank could be computed for the whole Web (the numerical side is in [3.5.3](/3.5.3#ex-3.3.3)). The damping factor is also a modeling choice: as $\alpha \to 1$, PageRank approaches the stationary distribution of the plain random walk, which for an undirected connected network is proportional to degree (Section 7.8.3).

**Example 7.6.1** Four pages link as follows: $\mathrm{A} \to \mathrm{B}, \mathrm{C}, \mathrm{D}$; $\mathrm{B} \to \mathrm{A}, \mathrm{D}$; $\mathrm{C} \to \mathrm{A}$; $\mathrm{D} \to \mathrm{B}, \mathrm{C}$. Starting from $\boldsymbol{\pi}^{(0)} = \frac14\boldsymbol{1}$, the undamped iteration ($\alpha = 1$) gives $\boldsymbol{\pi}^{(1)} = \frac{1}{24}(9, 5, 5, 5)$, $\boldsymbol{\pi}^{(2)} = \frac{1}{24}(7.5, 5.5, 5.5, 5.5)$, $\boldsymbol{\pi}^{(3)} = \frac{1}{24}(8.25, 5.25, 5.25, 5.25)$, converging to $(\frac{3}{9}, \frac{2}{9}, \frac{2}{9}, \frac{2}{9})$: A, which receives the whole vote of C and half of B's, ranks first. With $\alpha = 0.85$ the solution of Eq. (7.3) is $(\frac{37}{114}, \frac{77}{342}, \frac{77}{342}, \frac{77}{342}) \approx (0.325, 0.225, 0.225, 0.225)$; damping pulls the scores towards uniform. The iteration reaches an $\ell^1$ change below $10^{-10}$ after 27 steps, much faster than the bound, because the other eigenvalues of this small chain are small.

```python
import numpy as np

P = np.array([[0, 1/3, 1/3, 1/3],    # A -> B, C, D
              [1/2, 0, 0, 1/2],      # B -> A, D
              [1, 0, 0, 0],          # C -> A
              [0, 1/2, 1/2, 0]])     # D -> B, C
alpha, x = 0.85, np.full(4, 1/4)
for t in range(1000):
    y = alpha * P.T @ x + (1 - alpha) / 4
    if np.abs(y - x).sum() < 1e-10:
        break
    x = y
print(t + 1, y)    # 27 [0.3246 0.2251 0.2251 0.2251]
```

**Example 7.6.2** The centralities of the example graph $G_0$ (Example 7.1.1):

| Vertex | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ | $8$ |
|---|---|---|---|---|---|---|---|---|
| degree $k_i$ | $3$ | $2$ | $3$ | $3$ | $4$ | $2$ | $3$ | $2$ |
| closeness $C_{\mathrm{c}}$ | $0.500$ | $0.368$ | $0.500$ | $0.636$ | $0.636$ | $0.438$ | $0.467$ | $0.438$ |
| betweenness $C_{\mathrm{B}}$ | $2.5$ | $0$ | $2.5$ | $12$ | $12.5$ | $0$ | $0.5$ | $0$ |
| eigenvector ($\max = 1$) | $0.726$ | $0.505$ | $0.726$ | $0.854$ | $1$ | $0.620$ | $0.780$ | $0.620$ |
| PageRank ($\alpha = 0.85$) | $0.135$ | $0.095$ | $0.135$ | $0.133$ | $0.176$ | $0.095$ | $0.137$ | $0.095$ |

All twelve shortest paths between $\{1, 2, 3\}$ and $\{5, 6, 7, 8\}$ pass through vertex $4$, so $C_{\mathrm{B}}(4) = 12$; vertex $5$ lies on the twelve paths between $\{1, 2, 3, 4\}$ and $\{6, 7, 8\}$ and on one of the two shortest paths $6$–$5$–$8$ and $6$–$7$–$8$, so $C_{\mathrm{B}}(5) = 12.5$. Betweenness and closeness single out the two ends of the bridge. Eigenvector centrality and PageRank rank vertex $5$ first because it has the most neighbors, but they rank vertex $4$ below or level with vertices $1$, $3$ and $7$: they reward being well connected, not being a bottleneck. The choice of centrality must follow the question.

### 7.6.4. Example: Reputation in the Art World

Fraiberger, Sinatra, Resch, Riedl and Barabási (2018) reconstructed the exhibition and auction histories of 496,354 artists in 143 countries over 36 years. They built a network whose vertices are galleries and museums, with an edge weighted by the number of artists who exhibited at both, and ranked the institutions by eigenvector centrality, a measure of prestige that comes only from the movement of artists. The ranking predicted careers: of the artists whose first five exhibitions were at the most central institutions, most continued to exhibit at the top for the rest of their careers, while artists who started at the periphery mostly stopped exhibiting within a few years, and the few who rose did so through the network's central institutions. The early network position of an artist, computed from exhibitions only, predicted later auction prices. The analogy with science, galleries as journals and exhibitions as citations, is one reason why such analyses are applied to scientific careers as well.

## 7.7. Community Structure

### 7.7.1. What Is a Community

Many networks are made of groups of vertices with many edges inside and few between: circles of friends, research fields, functional modules of proteins. Finding them simplifies a large network into a few interpretable parts. The task has no single correct formulation, and the methods differ in what they assume.

**Definition 7.7.1 (Community Structure)** A network has **community structure** if its vertices can be divided into groups, called communities, such that the density of edges within groups is significantly higher than between groups, compared with a null model of random wiring.

Finding such a division is **community detection**, a form of **cluster analysis** for relational data.

The strictest local notion of a group is a clique.

**Definition 7.7.2 (Clique and $k$-Core)** A **clique** of a graph is a set of vertices any two of which are adjacent, that is, a vertex set inducing a complete **subgraph**; it is a *maximal clique* if no vertex can be added to it. The **$k$-core** of a graph is the largest **induced subgraph** in which every vertex has degree at least $k$; it is obtained by repeatedly deleting vertices of degree less than $k$.

**Algorithm 7.7.1 (Bron–Kerbosch Algorithm with Pivoting)** List all maximal cliques by calling $\mathrm{BK}(\varnothing, V, \varnothing)$, where $\mathrm{BK}(R, P, X)$ is: if $P = X = \varnothing$, report $R$; otherwise choose a pivot $u \in P \cup X$ with the most neighbors in $P$, and for each $v \in P \setminus N(u)$: call $\mathrm{BK}(R \cup \{v\}, P \cap N(v), X \cap N(v))$, then move $v$ from $P$ to $X$. Here $R$ is the current clique, $P$ the vertices that can extend it, and $X$ the vertices already tried, which prevents reporting a clique twice.

A graph on $N$ vertices can have $3^{N/3}$ maximal cliques (Moon and Moser, 1965), and the pivoting version runs in $O(3^{N/3})$ time in the worst case (Tomita, Tanaka and Takahashi, 2006), which is therefore optimal; on sparse real networks it is fast. Cliques are too strict to be communities, however: one missing edge breaks a clique, while real communities are dense but not complete.

### 7.7.2. Modularity

Newman and Girvan (2004) proposed to measure a partition by how many more edges it has inside the communities than expected under the configuration model, which preserves the degrees.

**Definition 7.7.3 (Modularity)** Let $A$ be the adjacency matrix of a network with $M$ edges and degrees $k_i$, and let $g_i$ be the community of vertex $i$ in a partition. The **modularity** of the partition is

$$
Q = \frac{1}{2M}\sum_{i,j}\left(A_{ij} - \frac{k_ik_j}{2M}\right)\delta(g_i, g_j), \tag{7.4}
$$
where $\delta(g_i, g_j) = 1$ if $g_i = g_j$ and $0$ otherwise. The matrix $B$ with entries $B_{ij} = A_{ij} - k_ik_j/(2M)$ is the *modularity matrix*.

**Proposition 7.7.1** Let $M_c$ be the number of edges inside community $c$ and $D_c = \sum_{i \in c}k_i$ its total degree. Then

$$
Q = \sum_c\left[\frac{M_c}{M} - \left(\frac{D_c}{2M}\right)^2\right],
$$

and $-\frac12 \leq Q < 1$. The partition into a single community has $Q = 0$.

**Proof** $\sum_{i,j \in c}A_{ij} = 2M_c$ and $\sum_{i,j \in c}k_ik_j = D_c^2$, which gives the formula. Write $e = \sum_cM_c/M \leq 1$ for the fraction of internal edges and $x_c = D_c/(2M)$, so that $\sum_cx_c = 1$ and $Q = e - \sum_cx_c^2$. Since $M > 0$, some $x_c > 0$, hence $Q < e \leq 1$. For the lower bound, the degree sum $D_c$ counts each of the $M_c$ internal edges twice and each other edge at an end in $c$ at most once, so $D_c \leq 2M_c + (M - M_c)$ and $x_c \leq \frac12 + \frac{M_c}{2M} \leq \frac12 + e$. Therefore $\sum_cx_c^2 \leq \max_cx_c\sum_cx_c \leq \frac12 + e$, and $Q \geq -\frac12$. The bound is attained by the complete bipartite graph $K_{n,n}$ divided into its two sides ($M_c = 0$, $x_c = \frac12$). For a single community, $M_c = M$ and $D_c = 2M$, so $Q = 0$. $\square$

The first term is the fraction of edges inside communities, the second its expected value when the edges are rewired at random with the same degrees. A positive $Q$ means more internal edges than chance; values above about $0.3$ are usually taken as evidence of community structure, although random graphs can have partitions with surprisingly high $Q$ (Guimerà, Sales-Pardo and Amaral, 2004).

**Example 7.7.1** In the graph $G_0$ (Example 7.1.1) the partition $\{1, 2, 3, 4\}$, $\{5, 6, 7, 8\}$ has $M_c = 5$ and $D_c = 11$ for both communities and $M = 11$, so $Q = 2\left[\frac{5}{11} - \left(\frac{11}{22}\right)^2\right] = \frac{9}{22} \approx 0.409$.

Modularity has a *resolution limit* (Fortunato and Barthélemy, 2007): its null model compares each community with the whole network, so in a large network it prefers to merge small communities even when they are obviously separate.

**Example 7.7.2** Join $n$ copies of the complete graph $K_5$ in a ring, each copy linked to the next by one edge, so $M = 11n$ and every vertex set of one clique has $M_c = 10$, $D_c = 22$. The partition into the $n$ cliques has $Q_1 = n\left[\frac{10}{11n} - \left(\frac{1}{n}\right)^2\right] = \frac{10}{11} - \frac1n$. The partition into $n/2$ pairs of adjacent cliques has $M_c = 21$ and $D_c = 44$, so $Q_2 = \frac{n}{2}\left[\frac{21}{11n} - \left(\frac{2}{n}\right)^2\right] = \frac{21}{22} - \frac{2}{n}$. Then $Q_2 > Q_1$ if and only if $n > 22$: in a ring of more than 22 cliques, the partition of maximal modularity merges cliques that are joined by a single edge.

### 7.7.3. Algorithms

Finding the partition of maximum modularity is NP-hard (Brandes and colleagues, 2008), so all practical methods are heuristics.

**Algorithm 7.7.2 (Girvan–Newman Algorithm)** (Girvan and Newman, 2002) Repeat until no edges remain: compute the edge betweenness of all edges (Algorithm 7.6.1) and delete an edge of largest betweenness. The components after each deletion form a hierarchy of partitions; report the level of largest modularity.

Edges between communities carry the shortest paths between them and so have high betweenness; removing them disconnects the communities. Each recomputation costs $O(NM)$, and up to $M$ edges are removed, so the total $O(NM^2)$ limits the method to a few thousand vertices.

*Spectral methods.* For a division into two groups, write $s_i = \pm1$ for the group of $i$. Since $\delta(g_i, g_j) = \frac12(s_is_j + 1)$ and $\sum_{i,j}B_{ij} = 0$,

$$
Q = \frac{1}{4M}\sum_{i,j}B_{ij}s_is_j = \frac{1}{4M}\boldsymbol{s}^{\mathsf T}B\boldsymbol{s}.
$$

Relaxing $\boldsymbol{s}$ to a real vector of fixed length, the maximum is attained at the eigenvector of $B$ for its largest eigenvalue; rounding its components to their signs gives the division (Newman, 2006), and if the largest eigenvalue is not positive the network is indivisible. This is the counterpart of **spectral bisection** with the **Fiedler vector** (Theorem 6.5.4), which minimizes the number of edges cut but needs the sizes of the parts to be fixed in advance; modularity chooses the sizes itself. For $G_0$ the leading eigenvector of $B$ (eigenvalue $2.37$) has positive components exactly on $\{1, 2, 3, 4\}$, recovering the partition of Example 7.7.1. The Kernighan–Lin algorithm (1970) improves a given bisection locally, by swapping pairs of vertices between the parts while the cut decreases; it is often used to refine spectral divisions.

**Algorithm 7.7.3 (Louvain Algorithm)** (Blondel, Guillaume, Lambiotte and Lefebvre, 2008) Start with each vertex in its own community and repeat two phases.

1. *Local moving.* Visit the vertices in random order. For vertex $i$, remove it from its community and compute, for each community $c$ containing a neighbor of $i$, the gain in modularity from adding $i$ to $c$,
   $$
   \Delta Q = \frac{k_{i,c}}{M} - \frac{k_iD_c}{2M^2},
   $$
   where $k_{i,c}$ is the number of edges from $i$ to $c$; put $i$ into the community of largest positive gain (or back into its own). Repeat until no move increases $Q$.
2. *Aggregation.* Build a new weighted network whose vertices are the communities, with edge weights equal to the numbers of edges between them and self-loops carrying the internal edges, and return to phase 1.

Stop when phase 1 makes no move; the communities of the last network, expanded to the original vertices, are the result.

The gain formula follows from Proposition 7.7.1: adding $i$ to $c$ adds $k_{i,c}$ internal edges, and changes the penalty by $\left[(D_c + k_i)^2 - D_c^2 - k_i^2\right]/(4M^2) = D_ck_i/(2M^2)$. Each pass of phase 1 costs $O(M)$, and the number of levels is small, so Louvain handles networks with hundreds of millions of edges. Its weakness was found later: a vertex that served as a bridge inside a community may be moved out, leaving the rest of the community internally disconnected, and the aggregation then freezes the defect. In experiments on real networks up to a quarter of the communities found by Louvain were badly connected and up to 16% disconnected (Traag, Waltman and van Eck, 2019).

**Algorithm 7.7.4 (Leiden Algorithm)** (Traag, Waltman and van Eck, 2019) Repeat three phases: (1) fast local moving as in Louvain, visiting only vertices whose neighborhood has changed; (2) *refinement*: within each community, start from singletons and merge vertices only with subsets of the same community to which they are well connected, possibly splitting the community into several well-connected parts; (3) aggregation of the refined partition, with the communities of phase 1 used as the initial partition at the next level.

The refinement guarantees that every community is connected, and that at convergence every community is well connected internally, while the speed remains that of Louvain or better. Leiden is the standard clustering method of single-cell genomics (the default of the scanpy library), where it is applied to a nearest-neighbor graph of cells ([7.9.5](/7.9.5)). Both algorithms accept a resolution parameter $\gamma_{\mathrm{r}}$, replacing $k_ik_j/(2M)$ by $\gamma_{\mathrm{r}}k_ik_j/(2M)$ in Eq. (7.4), which shifts the preferred community size and so mitigates the resolution limit. A much simpler heuristic is *label propagation* (Raghavan, Albert and Kumara, 2007): every vertex starts with its own label and repeatedly adopts the label most frequent among its neighbors, until no label changes; it runs in nearly linear time but its result depends on the order of updates.

![A network of 30 vertices drawn from a planted three-group model (edge probability 0.45 within groups, 0.03 between), coloured by the communities found by the Louvain algorithm (Algorithm 7.7.3); 10 of the 80 edges run between communities (grey). Louvain recovers the three planted groups exactly, with modularity Q = 0.530](./plots/modularity_example.py)

**Example 7.7.3** Zachary (1977) recorded the friendships among the 34 members of a university karate club, 78 edges, during a conflict between the instructor (vertex 1) and the administrator (vertex 34) that ended with the club splitting in two. The network has $\langle d\rangle = 2.41$, $\langle C\rangle = 0.571$, $C_\Delta = 0.256$ and $r = -0.476$: the two leaders are hubs with $16$ and $17$ friends, most of whom have few friends. The two leaders also have the largest betweenness and PageRank. The actual split has modularity $Q = 0.358$. The first edge removals of the Girvan–Newman algorithm divide the network into groups of $15$ and $19$ that differ from the actual split in two members, and the sign of the leading eigenvector of $B$ errs on one member. The Louvain algorithm always finds four communities, with $Q$ between $0.4151$ and $0.4198$ depending on the random order of the moves; the best of these runs reaches $0.4198$, the maximum modularity of this network (Brandes and colleagues, 2008). Each faction is split into two parts: the partition with highest $Q$ is not the one the club actually chose.

```python
import networkx as nx

G = nx.Graph(nx.karate_club_graph().edges())    # drop the edge weights stored by networkx
for seed in range(10):                          # the result depends on the order of the vertex moves
    parts = nx.community.louvain_communities(G, seed=seed)
    print(seed, len(parts), nx.community.modularity(G, parts))   # 4 communities, Q from 0.4151 to 0.4198
gn = nx.community.girvan_newman(G)
print([sorted(c) for c in next(gn)])                 # the first split into two groups
```

### 7.7.4. Statistical Inference and Evaluation

Modularity maximization finds partitions but cannot tell whether they are real: it finds high-$Q$ partitions even in random graphs. The statistical alternative is to fit a generative model. In the **stochastic block model** ([Definition 12.6.1](/3.4.12#def-12.6.1)) each vertex has a hidden group, and two vertices are joined with a probability that depends only on their groups; communities are inferred by maximum likelihood or Bayesian methods, and the number of groups can be chosen by model selection. Real networks need the *degree-corrected* version (Karrer and Newman, 2011), in which the edge probability is also proportional to the degrees, since otherwise the model groups vertices by degree rather than by community. Modularity maximization is in fact equivalent to maximum likelihood in a particular degree-corrected planted-partition model (Newman, 2016).

The block model also shows that detection has a limit. For two groups of equal size with mean degrees $c_{\mathrm{in}}$ to the vertex's own group and $c_{\mathrm{out}}$ to the other, no algorithm can find the groups better than chance in the sparse limit unless

$$
(c_{\mathrm{in}} - c_{\mathrm{out}})^2 > 2(c_{\mathrm{in}} + c_{\mathrm{out}}),
$$

a threshold conjectured from statistical physics (Decelle, Krzakala, Moore and Zdeborová, 2011) and proved by Mossel, Neeman and Sly and by Massoulié (2014–2018).

Community-detection algorithms are compared on benchmark graphs with planted communities. The LFR benchmark (Lancichinetti, Fortunato and Radicchi, 2008) generates networks with power-law distributions of degrees and community sizes and a mixing parameter $\mu$, the fraction of each vertex's edges that leave its community; the communities become harder to find as $\mu$ grows. The agreement between a found partition $X$ and the planted one $Y$ is measured by the normalized **mutual information**

$$
\operatorname{NMI}(X, Y) = \frac{2I(X; Y)}{H(X) + H(Y)},
$$
where $H$ is the entropy of the distribution of community sizes and $I$ the mutual information of the joint distribution of labels; it equals $1$ for identical partitions and is near $0$ for independent ones.

## 7.8. Processes on Networks

### 7.8.1. Robustness and Percolation

How many vertices can fail before a network falls apart? Removing vertices at random is a percolation process.

**Definition 7.8.1 (Percolation)** In *site percolation* on a graph, each vertex is kept independently with probability $\phi$ and removed (together with its edges) with probability $f = 1 - \phi$; in *bond percolation* the edges are kept with probability $\phi$. **Percolation** theory asks for the critical value $f_{\mathrm{c}}$ above which the kept graph has no giant component.

For the configuration model the existence of a giant component is decided by the first two moments of the degree distribution.

**Theorem 7.8.1 (Molloy–Reed Criterion)** Let a sequence of configuration models have degree distributions converging to $p_k$, with $\sum_kk^2p_k < \infty$ and suitable regularity conditions. Then with probability tending to $1$ there is a giant component if

$$
\sum_kk(k-2)p_k > 0, \quad\text{that is,}\quad \kappa = \frac{\langle k^2\rangle}{\langle k\rangle} > 2, \tag{7.5}
$$

and none if $\kappa < 2$ (Molloy and Reed, 1995).

**Proof** (idea) Explore a component as in Theorem 7.2.2. Following an edge to a new vertex, we reach a vertex of degree $k$ with probability $kp_k/\langle k\rangle$ (Section 7.1.2), and it has $k - 1$ further edges, its *excess degree*. The exploration is approximately a branching process whose offspring is the excess degree, with mean

$$
\sum_k(k - 1)\frac{kp_k}{\langle k\rangle} = \frac{\langle k^2\rangle - \langle k\rangle}{\langle k\rangle} = \kappa - 1.
$$

The process survives with positive probability if and only if $\kappa - 1 > 1$. $\square$

With the generating functions $G_0(x) = \sum_kp_kx^k$ and $G_1(x) = G_0'(x)/G_0'(1)$, the probability $u$ that an edge does not lead to the giant component solves $u = G_1(u)$, and the giant component contains the fraction $S = 1 - G_0(u)$ of the vertices. For Poisson degrees $G_0 = G_1 = \mathrm{e}^{c(x-1)}$, and this reduces to Eq. (7.1).

**Proposition 7.8.1** If each vertex of a configuration model with $\kappa = \langle k^2\rangle/\langle k\rangle$ is removed independently with probability $f$, the giant component disappears at

$$
f_{\mathrm{c}} = 1 - \frac{1}{\kappa - 1}
$$

(Cohen, Erez, ben-Avraham and Havlin, 2000).

**Proof** A surviving vertex of original degree $k$ keeps each of its edges independently with probability $1 - f$, so its new degree $k'$ satisfies $\mathbb{E}[k'] = (1-f)k$ and $\mathbb{E}[k'^2] = (1-f)^2k^2 + f(1-f)k$. The kept graph is again a configuration model, with $\langle k'\rangle = (1-f)\langle k\rangle$ and $\langle k'^2\rangle = (1-f)^2\langle k^2\rangle + f(1-f)\langle k\rangle$. The criterion of Eq. (7.5) for it reads $(1-f)\kappa + f > 2$, that is, $1 - f > 1/(\kappa - 1)$. $\square$

For a random graph, $\langle k^2\rangle = c + c^2$, so $\kappa = c + 1$ and $f_{\mathrm{c}} = 1 - 1/c$: with $c = 4$, three quarters of the vertices must fail. For a scale-free network with $2 < \gamma < 3$, $\kappa$ diverges with $N$ (Section 7.4.3) and $f_{\mathrm{c}} \to 1$: in the limit, a giant component survives the random failure of almost all vertices, because random failures rarely hit the hubs that hold it together. The other side of this robustness is fragility under attack: removing the vertices of highest degree first destroys the hubs and with them the network, and for $\gamma$ between $2$ and $3$ the removal of a few percent of the vertices suffices (Albert, Jeong and Barabási, 2000; Callaway and colleagues, 2000; Cohen and colleagues, 2001). A random graph, which has no hubs, responds to failures and attacks much more similarly.

![Robustness of an Erdős–Rényi graph (N = 10,000, mean degree 4, blue) and a Barabási–Albert graph (N = 10,000, m = 2, mean degree 4, red) to the removal of a fraction f of the vertices, at random (solid) or in decreasing order of degree (dashed): size of the largest component relative to N, averaged over 5 realizations. The black line is the theory for random removal from the random graph, which predicts breakdown at f_c = 1 − 1/c = 0.75. Under attack the Barabási–Albert graph falls apart after the removal of about 15% of its vertices, the random graph after about 36%](./plots/percolation_attack.py)

In the simulation, the largest component of the random graph drops below 5% of the vertices at $f \approx 0.73$, close to the predicted $0.75$; that of the BA graph only at $f \approx 0.77$, and it keeps a small connected core up to $f \approx 0.84$. The degree sequence of this BA graph has $\langle k^2\rangle = 59.3$, $\kappa = 14.8$, for which Proposition 7.8.1 predicts $f_{\mathrm{c}} = 0.93$; the BA graph breaks down earlier because it is not a configuration model (its degrees are correlated with the age of the vertices) and because for $\gamma = 3$ the divergence of $\kappa \propto \ln N$ is very slow. Under attack, the BA graph drops below 5% after the removal of the $15\%$ highest-degree vertices, the random graph after $36\%$.

### 7.8.2. Epidemic Spreading

An infection spreading through contacts is a process on a network. The simplest models describe each individual by a state: susceptible (S), infected and infectious (I), or recovered and immune (R).

**Definition 7.8.2 (SIR Model)** In the **SIR model** with homogeneous mixing, a population with fractions $s(t)$, $i(t)$, $r(t)$ of susceptible, infected and recovered individuals evolves by

$$
\frac{\mathrm{d}s}{\mathrm{d}t} = -\beta si, \qquad \frac{\mathrm{d}i}{\mathrm{d}t} = \beta si - \mu i, \qquad \frac{\mathrm{d}r}{\mathrm{d}t} = \mu i,
$$
where $\beta$ is the transmission rate and $\mu$ the recovery rate. The **basic reproduction number** $R_0 = \beta/\mu$ is the expected number of secondary infections caused by one infected individual in a fully susceptible population. In the SIS model recovered individuals become susceptible again ($\mathrm{d}i/\mathrm{d}t = \beta i(1 - i) - \mu i$), and in the SI model nobody recovers.

At the start, $s \approx 1$ and $\mathrm{d}i/\mathrm{d}t \approx (\beta - \mu)i$, so the infection grows if and only if $R_0 > 1$. Dividing the first equation by the third gives $\mathrm{d}s/\mathrm{d}r = -R_0s$, so $s = \mathrm{e}^{-R_0r}$ when $s(0) \approx 1$, $r(0) = 0$. At the end of the epidemic $i = 0$ and $s + r = 1$, so the final fraction infected solves

$$
r_\infty = 1 - \mathrm{e}^{-R_0r_\infty},
$$

which is Eq. (7.1) with $c$ replaced by $R_0$. The coincidence is not accidental: whether an infection becomes an epidemic is a branching-process question, like the existence of a giant component. For the SIS model the infection persists at the endemic level $i^* = 1 - 1/R_0$ if $R_0 > 1$.

On a network, an infected vertex transmits along each of its edges at rate $\beta$, and the heterogeneity of degrees changes the threshold. In the heterogeneous **mean-field approximation** (Pastor-Satorras and Vespignani, 2001), let $\rho_k(t)$ be the fraction of infected vertices among those of degree $k$, measure time in units of $1/\mu$ and put $\lambda = \beta/\mu$. The SIS dynamics becomes

$$
\frac{\mathrm{d}\rho_k}{\mathrm{d}t} = -\rho_k + \lambda k(1 - \rho_k)\Theta, \qquad \Theta = \frac{\sum_kkp_k\rho_k}{\langle k\rangle},
$$
where $\Theta$ is the probability that an edge leads to an infected vertex (again size-biased). In a steady state $\rho_k = \lambda k\Theta/(1 + \lambda k\Theta)$, and substituting into the definition of $\Theta$ gives the self-consistency equation $\Theta = F(\Theta) = \langle k\rangle^{-1}\sum_kkp_k\lambda k\Theta/(1 + \lambda k\Theta)$. Since $F$ is concave with $F(0) = 0$ and $F(1) < 1$, a positive solution exists if and only if $F'(0) = \lambda\langle k^2\rangle/\langle k\rangle > 1$.

**Definition 7.8.3 (Epidemic Threshold)** The **epidemic threshold** of a spreading model on a network is the critical value of the transmission parameter above which an infection starting from a few vertices reaches a finite fraction of the network (SIR) or persists in it (SIS). In the heterogeneous mean-field approximation of the SIS model it is

$$
\lambda_{\mathrm{c}} = \frac{\langle k\rangle}{\langle k^2\rangle}.
$$

For SIR, the probability $T$ that an infected vertex transmits along a given edge before recovering (the *transmissibility*) maps the final outbreak onto bond percolation with $\phi = T$ (Newman, 2002), and by the argument of Theorem 7.8.1 a large outbreak is possible if and only if $T > T_{\mathrm{c}} = 1/(\kappa - 1) = \langle k\rangle/(\langle k^2\rangle - \langle k\rangle)$.

For a random graph with $c = 4$ ($\langle k^2\rangle = 20$) the thresholds are $\lambda_{\mathrm{c}} = 0.2$ and $T_{\mathrm{c}} = 0.25$; for the BA graph of the previous figure ($\langle k\rangle = 4$, $\langle k^2\rangle = 59.3$) they are $\lambda_{\mathrm{c}} = 0.068$ and $T_{\mathrm{c}} = 0.072$, more than three times lower. For scale-free networks with $\gamma \leq 3$ both thresholds tend to $0$ as $N \to \infty$: an infection however weak can spread, because hubs are both easily infected and highly infectious. This explains the persistence of computer viruses with low infection rates. Later work refined the picture: for the SIS model the threshold vanishes on power-law random graphs for every $\gamma$, also $\gamma > 3$, because a hub and its neighbors can sustain the infection locally (Chatterjee and Durrett, 2009), while for SIR the threshold is finite for $\gamma > 3$.

Heterogeneity also determines how to immunize. Random immunization of a fraction $g$ of the vertices removes them as in Proposition 7.8.1, and in a scale-free network almost all vertices would have to be immunized. Immunizing the hubs is far more effective but requires knowing them. *Acquaintance immunization* (Cohen, Havlin and ben-Avraham, 2003) needs no global knowledge: choose random individuals and immunize a random acquaintance of each. By the friendship paradox, the acquaintance has degree $k$ with probability $kp_k/\langle k\rangle$, so the hubs are found with high probability.

### 7.8.3. Random Walks and Diffusion

Let a quantity $x_i$ (a concentration, an opinion, a probability) sit on each vertex and flow along each edge at a rate proportional to the difference between its ends. Then

$$
\frac{\mathrm{d}x_i}{\mathrm{d}t} = D\sum_jA_{ij}(x_j - x_i) = -D\sum_jL_{ij}x_j, \qquad \frac{\mathrm{d}\boldsymbol{x}}{\mathrm{d}t} = -DL\boldsymbol{x},
$$

with $L = \operatorname{diag}(k_i) - A$ the Laplacian matrix: the network analogue of the **diffusion equation**, the Laplacian of the graph playing the role of $-\Delta$. Expanding in the orthonormal eigenvectors $\boldsymbol{q}_j$ of $L$ with eigenvalues $0 = \mu_1 \leq \mu_2 \leq \cdots \leq \mu_N$ (Proposition 6.5.1),

$$
\boldsymbol{x}(t) = \sum_j\mathrm{e}^{-D\mu_jt}(\boldsymbol{q}_j^{\mathsf T}\boldsymbol{x}(0))\boldsymbol{q}_j.
$$

On a connected network every mode except the constant one decays, and $\boldsymbol{x}(t)$ approaches the average of $\boldsymbol{x}(0)$ on every vertex; the slowest mode decays at the rate $D\mu_2$, so the **algebraic connectivity** $\mu_2 = a(G)$ (Definition 6.5.1) sets the relaxation time $1/(D\mu_2)$, and the slow mode is the Fiedler vector, which is nearly constant on each community. For $G_0$, $\mu_2 = 0.319$: mixing within each group of four is fast, mixing between the groups through the single bridge takes about $3/D$.

A random walker that moves at each step to a uniformly chosen neighbor has transition matrix $P = K^{-1}A$, with $K = \operatorname{diag}(k_i)$ the **degree matrix**.

**Proposition 7.8.2** On a connected undirected network the random walk has the unique stationary distribution $\pi_i = k_i/(2M)$. It satisfies **detailed balance**, $\pi_iP_{ij} = \pi_jP_{ji}$, and if the network is not bipartite the distribution of the walker converges to $\boldsymbol{\pi}$ from any start.

**Proof** $\pi_iP_{ij} = \frac{k_i}{2M}\cdot\frac{A_{ij}}{k_i} = \frac{A_{ij}}{2M}$, which is symmetric in $i$ and $j$; summing over $i$ gives $\sum_i\pi_iP_{ij} = \pi_j\sum_iP_{ji} = \pi_j$, and $\sum_i\pi_i = 1$ by the handshaking lemma. The chain is irreducible because the network is connected, so the stationary distribution is unique; it is aperiodic if and only if the network is not bipartite (a connected graph has a closed walk of odd length exactly when it is not bipartite), and the convergence follows from [Theorem 9.3.3](/3.5.9#thm-9.3.3). $\square$

A random walker thus visits each vertex in proportion to its degree, and returns to vertex $i$ on average every $2M/k_i$ steps. Random walks underlie PageRank (Section 7.6.3), the community-detection method Infomap (Rosvall and Bergstrom, 2008), which finds partitions in which a random walker stays long within each community, and the propagation of signals in biological networks. The physics of diffusion and random walks in continuous space is the subject of [7.6.5](/7.6.5).

### 7.8.4. The Statistics of Network Motifs

Section 7.4.6 introduced random networks with the observed degrees as a null model. Applied to small subgraphs, it reveals the local building blocks of a network.

**Definition 7.8.4 (Network Motif)** Let $H$ be a small connected graph (directed or undirected), and let $N_{\mathrm{real}}(H)$ be the number of induced subgraphs of a network isomorphic to $H$. Let $\bar N_{\mathrm{rand}}(H)$ and $s_{\mathrm{rand}}(H)$ be the mean and standard deviation of this number over an ensemble of degree-preserving randomizations of the network (Algorithm 7.4.2). $H$ is a **network motif** of the network if it occurs significantly more often than in the randomized networks, as measured by the z-score

$$
z = \frac{N_{\mathrm{real}}(H) - \bar N_{\mathrm{rand}}(H)}{s_{\mathrm{rand}}(H)}
$$

or by the empirical p-value, the fraction of randomized networks with $N_{\mathrm{rand}}(H) \geq N_{\mathrm{real}}(H)$ (Milo and colleagues, 2002). Subgraphs that occur significantly less often are *anti-motifs*.

Milo and colleagues also required $p < 0.01$ over 1000 randomizations, at least four occurrences, and $N_{\mathrm{real}} - \bar N_{\mathrm{rand}} > 0.1\bar N_{\mathrm{rand}}$, to exclude effects that are statistically significant but tiny. There are $13$ connected directed graphs on three vertices up to isomorphism and $199$ on four, so motif analyses usually stop at four or five vertices. For undirected graphs there are only two connected subgraphs on three vertices, the path and the triangle, and their counts are $\sum_i\binom{k_i}{2} - 3t$ and $t$, with the number $t$ of triangles from Proposition 7.1.1.

Counting requires two steps. First, all connected induced subgraphs with $k$ vertices are enumerated. The ESU algorithm (Wernicke, 2006) does this without duplicates: starting from each vertex $v$, it extends a set of chosen vertices one vertex at a time, adding only vertices with label larger than $v$ that are neighbors of the newly added vertex but not of the earlier chosen ones, so each connected set is generated exactly once, along a unique branch of a search tree; the cost is proportional to the number of subgraphs. Second, each subgraph is classified up to **graph isomorphism**, usually by computing a canonical labeling with McKay's algorithm (the program nauty, 1981). For a few vertices this is cheap. In general, no polynomial algorithm for graph isomorphism is known, but the problem is not known to be NP-complete either, and since Babai (2015) it can be solved in quasipolynomial time $\exp\bigl((\ln N)^{O(1)}\bigr)$.

**Example 7.8.1** The karate-club network of Example 7.7.3 contains $45$ triangles. Over 1000 degree-preserving randomizations the number of triangles has mean $39.2$ and standard deviation $4.5$, so $z = 1.29$ and the empirical p-value is $0.13$: the triangles are not a motif. The high clustering $\langle C\rangle = 0.571$ of this network, about four times its density $p = 0.139$, is largely a consequence of its degree sequence, two hubs and many vertices of low degree, rather than of a tendency to close triangles. In contrast, the transcriptional regulatory network of *E. coli* contains 40 feed-forward loops (regulator $X$ regulates $Y$, and both regulate $Z$), against $7 \pm 3$ in randomized networks, $z \approx 10$ (Milo and colleagues, 2002). What such motifs compute, and why evolution selected them, is the subject of [7.9.15](/7.9.15).

```python
import networkx as nx
import numpy as np

G = nx.Graph(nx.karate_club_graph().edges())
t_real = sum(nx.triangles(G).values()) // 3                  # 45
rng = np.random.default_rng(0)
t_rand = []
for _ in range(1000):
    H = G.copy()
    nx.double_edge_swap(H, nswap=10 * H.number_of_edges(), max_tries=10**6, seed=int(rng.integers(1e9)))
    t_rand.append(sum(nx.triangles(H).values()) // 3)
t_rand = np.array(t_rand)
z = (t_real - t_rand.mean()) / t_rand.std(ddof=1)
p = (np.sum(t_rand >= t_real) + 1) / (len(t_rand) + 1)
print(t_rand.mean(), t_rand.std(ddof=1), z, p)               # 39.17 4.51 1.29 0.126
```

## Summary

A network is described by its degree distribution $p_k$ (Definition 7.1.1), especially $\langle k\rangle$ and $\kappa = \langle k^2\rangle/\langle k\rangle$, the mean degree of a vertex reached along an edge; by its average path length (Definition 7.1.2); by its clustering coefficient (Definition 7.1.3), computable from $A^3$ (Proposition 7.1.1); and by its degree correlations (Definition 7.1.4). Every statistic must be compared with a null model: the random graph for a given $N$ and $M$ (Definition 7.2.1), the configuration model (Definition 7.4.3) or degree-preserving randomization (Algorithm 7.4.2) for a given degree sequence.

The three models of this chapter compare as follows.

| | Random graph $G(N, p)$ | Watts–Strogatz | Barabási–Albert |
|---|---|---|---|
| Degree distribution | Poisson (Theorem 7.2.1) | narrow, peaked at $K$ | $2m(m+1)/[k(k+1)(k+2)] \sim k^{-3}$ (Theorem 7.5.1) |
| Largest degree | $\sim \ln N/\ln\ln N$ | $\approx K$ | $\sim mN^{1/2}$ |
| Average path length | $\ln N/\ln\langle k\rangle$ | $\sim N/2K$ at $p = 0$, $\sim\ln N$ for $p \gtrsim 1/(NK)$ | $\ln N/\ln\ln N$ |
| Clustering | $\langle k\rangle/N \to 0$ | $\approx \frac{3(K-2)}{4(K-1)}(1-p)^3$, high | $\sim (\ln N)^2/N \to 0$ |
| Random failures | $f_{\mathrm{c}} = 1 - 1/\langle k\rangle$ | — | $f_{\mathrm{c}} \to 1$ slowly |
| Attack on hubs | similar to failures | — | fragile |
| Epidemic threshold | $\lambda_{\mathrm{c}} = 1/(\langle k\rangle + 1)$ | finite | $\to 0$ |
| Explains | giant component, short paths | short paths with clustering | hubs, heavy tails |

The main results are the following.

- The giant component of $G(N, c/N)$ appears at $c = 1$ in a continuous phase transition, with size given by $S = 1 - \mathrm{e}^{-cS}$ (Theorem 7.2.2, Eq. (7.1)); the graph is connected for $c > \ln N$ (Theorem 7.2.3).
- Real networks are small worlds (Definition 7.3.2) and have heavy-tailed degree distributions; in a scale-free network (Definition 7.4.2) with $2 < \gamma < 3$, $\langle k^2\rangle$ diverges, the largest hub grows like $N^{1/(\gamma - 1)}$ (Proposition 7.4.2), and distances grow like $\ln\ln N$.
- Power laws are fitted by maximum likelihood with a Kolmogorov–Smirnov choice of $k_{\min}$ and a bootstrap test (Algorithm 7.4.1), never by least squares on log–log plots; many claimed power laws are better described as heavy tails of unspecified form.
- Growth plus linear preferential attachment gives $\gamma = 3$ (Theorem 7.5.1); without either ingredient there is no power law; fitness, initial attractiveness, internal links and aging modify the exponent.
- Centralities answer different questions: closeness and betweenness (Definitions 7.6.1, 7.6.2; Algorithm 7.6.1) find bottlenecks, eigenvector centrality and PageRank (Definitions 7.6.3, 7.6.4; Proposition 7.6.1) find well-connected vertices.
- Modularity (Definition 7.7.3) compares internal edges with the configuration model; it is maximized heuristically by Louvain and Leiden (Algorithms 7.7.3, 7.7.4), has a resolution limit (Example 7.7.2), and finds structure even in random graphs, which the stochastic block model and its detectability threshold address.
- Whether a giant component survives random failures, and whether an epidemic spreads, both depend on $\kappa$: the Molloy–Reed criterion $\kappa > 2$ (Theorem 7.8.1), $f_{\mathrm{c}} = 1 - 1/(\kappa - 1)$ (Proposition 7.8.1), $\lambda_{\mathrm{c}} = \langle k\rangle/\langle k^2\rangle$ and $T_{\mathrm{c}} = 1/(\kappa - 1)$ (Definition 7.8.3). Diffusion relaxes at the rate of the algebraic connectivity, and a random walk visits vertices in proportion to their degree (Proposition 7.8.2).
- Network motifs (Definition 7.8.4) are subgraphs overrepresented relative to degree-preserving randomization; high clustering alone does not make triangles a motif (Example 7.8.1).

## Questions

1. Let $A$ be the adjacency matrix of the graph $G_0$ of Example 7.1.1. Compute $(A^2)_{14}$ and $(A^3)_{14}$, and compare with the number of paths of length $2$ and $3$ from vertex $1$ to vertex $4$. Why do powers of $A$ count walks and not paths?

   **Answer** By Theorem 2.2.1, $(A^n)_{ij}$ is the number of walks of length $n$ from $i$ to $j$. The neighbors of $1$ are $2, 3, 4$ and those of $4$ are $1, 3, 5$; the only common neighbor is $3$, so $(A^2)_{14} = 1$, the path $1$–$3$–$4$. The walks of length $3$ from $1$ to $4$ are $1$–$2$–$1$–$4$, $1$–$2$–$3$–$4$, $1$–$3$–$1$–$4$, $1$–$4$–$1$–$4$, $1$–$4$–$3$–$4$ and $1$–$4$–$5$–$4$, so $(A^3)_{14} = 6$; only one of them, $1$–$2$–$3$–$4$, is a path. Matrix multiplication sums over all intermediate vertices without remembering which vertices were visited, so walks that go back and forth along an edge, or revisit a vertex, are counted as well. Counting the paths between two vertices is a #P-complete problem in general (Valiant, 1979); for $n = 2$ walks and paths coincide (in a simple graph, a walk $i$–$v$–$j$ with $i \neq j$ is a path).

2. Show that the expected local clustering coefficient of a vertex of degree $k \geq 2$ in $G(N, p)$ is exactly $p$, and compute $C$ for $G(N, p)$ with $N = 10^6$ and $\langle k\rangle = 10$. Compare with a social network of the same size with $C = 0.2$.

   **Answer** Condition on the set of $k$ neighbors of vertex $i$. The edges among them are independent of the edges at $i$, each present with probability $p$, so the number $T_i$ of edges among the neighbors is $\mathrm{Bin}\left(\binom{k}{2}, p\right)$ and $\mathbb{E}[C_i \mid k_i = k] = \mathbb{E}T_i/\binom k2 = p$. With $p = \langle k\rangle/(N - 1) \approx 10^{-5}$, the random graph has $C \approx 10^{-5}$; a social network with $C = 0.2$ has $20{,}000$ times more clustering, which no random graph of the same density can produce. This is the gap that the Watts–Strogatz model addresses.

3. For the graph $G_0$, verify that the partition $\{1, 2, 3, 4\}$, $\{5, 6, 7, 8\}$ has modularity $9/22$, and compute the modularity of the partition $\{1, 2, 3\}$, $\{4, 5, 6, 7, 8\}$. Which does modularity prefer?

   **Answer** With $M = 11$: the first partition has $M_c = 5, 5$ and $D_c = 11, 11$, so $Q = 2(5/11 - 1/4) = 9/22 \approx 0.409$ (Example 7.7.1). For the second, $\{1, 2, 3\}$ has internal edges $12, 13, 23$, so $M_c = 3$, and $D_c = 3 + 2 + 3 = 8$; $\{4, \dots, 8\}$ has internal edges $45, 56, 57, 58, 67, 78$, so $M_c = 6$, and $D_c = 3 + 4 + 2 + 3 + 2 = 14$. Then $Q = 3/11 - (8/22)^2 + 6/11 - (14/22)^2 = 9/11 - (64 + 196)/484 = 0.8182 - 0.5372 = 0.281$. Modularity prefers the first partition: moving vertex $4$ to the right loses the two edges $14, 34$ inside the left group and gains only the edge $45$.

4. Estimate the largest in-degree of the Web sample of Section 7.1.1 ($N = 325{,}729$) if the in-degrees followed (a) a power law with $\gamma = 2.1$ and $k_{\min} = 1$, (b) an exponential distribution with the same mean $4.60$. The observed value is $10{,}721$. What does the comparison show?

   **Answer** By Proposition 7.4.2: (a) $k_{\max} = N^{1/(\gamma - 1)} = 325{,}729^{1/1.1} = \exp(12.69/1.1) = \exp(11.54) \approx 1.0 \times 10^5$; (b) for $\lambda\mathrm{e}^{-\lambda(k - 1)}$ the mean is $1 + 1/\lambda = 4.60$, so $1/\lambda = 3.60$ and $k_{\max} = 1 + 3.60\ln N = 1 + 3.60 \times 12.69 \approx 47$. The observed maximum lies between, an order of magnitude below the power-law estimate and more than two orders above the exponential one. The power law captures the existence of huge hubs, while the overestimate reflects that the tail is not a pure power law up to the largest degrees (and that $k_{\max}$ fluctuates strongly for $\gamma$ near 2). An exponential model is ruled out.

5. In the BA model with $m = 3$, what is the expected degree, at the time the network has $10^5$ vertices, of the vertex added at time $t_i = 100$? How many vertices in total have degree at least $50$ according to Eq. (7.2)?

   **Answer** By Proposition 7.5.1, $k_i = m(t/t_i)^{1/2} = 3\sqrt{1000} \approx 95$, which agrees with the simulation (panel A of the figure in Section 7.5.2). For the tail, $\sum_{k \geq K}\frac{2m(m+1)}{k(k+1)(k+2)} = \frac{m(m+1)}{K(K+1)}$ by the telescoping identity used after Theorem 7.5.1, so the fraction with degree at least $50$ is $12/(50 \cdot 51) = 0.0047$, about $470$ of the $10^5$ vertices. Equivalently, in the continuum approximation $k_i(t) \geq 50$ requires $t_i \leq m^2t/2500 = 360$: roughly the first few hundred vertices. Old vertices are the hubs.

6. Derive the Molloy–Reed criterion for a network in which every vertex has degree $1$ or $3$, a fraction $q$ of them degree $3$. For which $q$ is there a giant component? What is the critical fraction of random failures for $q = 1$?

   **Answer** $\langle k\rangle = (1 - q) + 3q = 1 + 2q$ and $\langle k^2\rangle = (1 - q) + 9q = 1 + 8q$. By Theorem 7.8.1 a giant component exists iff $\sum_kk(k - 2)p_k = 1 \cdot (-1)(1 - q) + 3 \cdot 1 \cdot q = 4q - 1 > 0$, that is, $q > 1/4$. Equivalently $\kappa = (1 + 8q)/(1 + 2q) > 2 \iff 1 + 8q > 2 + 4q \iff q > 1/4$. For $q = 1$ (a random $3$-regular graph) $\kappa = 3$, and Proposition 7.8.1 gives $f_{\mathrm{c}} = 1 - 1/(3 - 1) = 1/2$: half of the vertices can fail at random before the giant component disappears. The intuition: a path entering a degree-$3$ vertex can continue along two edges, entering a degree-$1$ vertex it stops; the average number of continuations must exceed one.

7. An infection with transmissibility $T = 0.15$ spreads by SIR on (a) a random graph with $\langle k\rangle = 4$, (b) a network with the degree sequence of the BA graph of Section 7.8.1 ($\langle k\rangle = 4$, $\langle k^2\rangle = 59.3$). Can it cause a large outbreak? What fraction of the vertices must be immunized at random to prevent one?

   **Answer** The threshold is $T_{\mathrm{c}} = \langle k\rangle/(\langle k^2\rangle - \langle k\rangle)$. (a) $\langle k^2\rangle = c + c^2 = 20$, $T_{\mathrm{c}} = 4/16 = 0.25 > 0.15$: no large outbreak, no immunization needed. (b) $T_{\mathrm{c}} = 4/55.3 = 0.072 < 0.15$: a large outbreak is possible. Random immunization of a fraction $g$ removes vertices as in site percolation; an outbreak requires a giant cluster of non-immune vertices connected by transmitting edges, that is, site percolation with $1 - g$ combined with bond percolation with $T$, which by the argument of Proposition 7.8.1 gives the condition $(1 - g)T(\kappa - 1) > 1$. Hence $g_{\mathrm{c}} = 1 - T_{\mathrm{c}}/T = 1 - 0.072/0.15 = 0.52$: more than half of the population must be immunized at random. Acquaintance immunization or immunization of the hubs would need a much smaller fraction.

8. Show that the stationary distribution of PageRank with $\alpha \to 1$ on a connected undirected network is proportional to degree, and explain why PageRank on undirected networks is therefore close to degree centrality. What changes for directed networks?

   **Answer** On an undirected network with no isolated vertices there are no dangling vertices, $P = K^{-1}A$, and at $\alpha = 1$ Eq. (7.3) is the stationary equation of the random walk, whose solution is $\pi_i = k_i/(2M)$ (Proposition 7.8.2). By continuity of the unique solution in $\alpha$, PageRank tends to $k_i/(2M)$ as $\alpha \to 1$, and for $\alpha = 0.85$ it remains strongly correlated with degree (in Example 7.6.2 the ranking by PageRank agrees with the ranking by degree except for ties). In a directed network the stationary distribution of the walk on the links is not determined by in-degrees: a page receives the rank of the pages that link to it, divided by their out-degrees, so one link from an important page can outweigh many from unimportant ones, and pages that are not reachable from the rest would get no rank without the random jumps. That is where PageRank differs essentially from counting links.

9. Explain why the Louvain gain formula $\Delta Q = k_{i,c}/M - k_iD_c/(2M^2)$ is positive for a vertex attached to a community only if it has "more edges to $c$ than expected", and apply it to vertex $4$ of $G_0$ when $\{1, 2, 3\}$ and $\{5, 6, 7, 8\}$ are already communities and $4$ is alone.

   **Answer** $\Delta Q > 0 \iff k_{i,c} > k_iD_c/(2M)$, and $k_iD_c/(2M)$ is the expected number of edges between $i$ and $c$ in the configuration model (Section 7.4.6). For vertex $4$, $k_4 = 3$ and $M = 11$. Joining $\{1, 2, 3\}$: $k_{4,c} = 2$ (edges $14, 34$), $D_c = 8$, so $\Delta Q = 2/11 - 3 \cdot 8/242 = 0.1818 - 0.0992 = 0.083$. Joining $\{5, 6, 7, 8\}$: $k_{4,c} = 1$, $D_c = 11$, so $\Delta Q = 1/11 - 33/242 = 0.0909 - 0.1364 = -0.045$. Louvain moves $4$ into $\{1, 2, 3\}$, producing the partition of Example 7.7.1.

10. (Open question) Design an analysis to decide whether a given protein interaction network contains more triangles than its degree sequence implies, and discuss what could bias the answer.

    **Answer** A possible design: (i) take the largest connected component, remove self-loops and duplicate edges, and count triangles $t$ with Proposition 7.1.1; (ii) generate 1000 networks by degree-preserving randomization (Algorithm 7.4.2) with at least $10M$ accepted swaps each, checking convergence by tracking $t$ along the swap chain; (iii) compute the z-score and the empirical p-value $(1 + \#\{t_{\mathrm{rand}} \geq t\})/1001$, as in Example 7.8.1, and report the effect size $t/\bar t_{\mathrm{rand}}$, not only $z$; (iv) repeat with stricter null models, for example preserving degrees and the assignment of proteins to cellular compartments, since proteins in the same compartment interact more often. Possible biases: experimental methods produce different topologies (affinity purification followed by mass spectrometry reports complexes, which, if converted into all pairwise edges, creates cliques and thus triangles artificially; yeast two-hybrid reports binary interactions); incomplete and literature-biased sampling inflates the degrees of well-studied proteins; and for heavy-tailed degrees the randomization must avoid multiple edges, which the swap algorithm guarantees but the configuration model does not. The biological interpretation of over-represented subgraphs is taken up in [7.9.15](/7.9.15).
