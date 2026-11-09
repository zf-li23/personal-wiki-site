---
title: Transcription Networks and Network Motifs
description: "Transcription networks as signed directed graphs and the dynamics of their building blocks: separation of time scales, input functions and their logic approximations, multi-dimensional input functions, the response time and mathematically controlled comparisons; network motifs by comparison with randomized networks (expected subgraph counts in random digraphs, z-scores, degree-preserving ensembles, the global structure of transcription networks); autoregulation; the eight types of feed-forward loops, the coherent type-1 FFL as a sign-sensitive delay (arabinose and flagella systems), the incoherent type-1 FFL as pulse generator, response accelerator and biphasic dose response, fold-change detection by scalar symmetry; single-input modules and last-in-first-out order, multi-output FFLs and first-in-first-out order, bi-fans and dense overlapping regulons, and interlocked FFLs in sporulation."
---

A cell responds to its environment by changing which proteins it makes, and the decisions are made by transcription factors that regulate genes, among them the genes of other transcription factors. The set of these interactions is a network, and the earlier chapters of this course inferred such networks from binding and expression data ([7.9.11](/7.9.11)) and analyzed their large-scale statistics ([7.9.12](/7.9.12)). This chapter asks a different question: what does a transcription network compute, and can its function be understood from small parts? The answer developed by Alon and colleagues since 2002 is that transcription networks are built from a few recurring circuit patterns, the **network motifs** ([1.4.7](/1.4.7#def-7.8.4)), each of which performs a definite information-processing task that can be read off from simple differential equations: negative autoregulation speeds responses, the coherent feed-forward loop filters out brief signals, the incoherent feed-forward loop generates pulses and detects fold changes, single-input modules and multi-output feed-forward loops order genes in time.

The chapter starts with the elements of transcription networks and their dynamics (15.1), defines motifs statistically (15.2), and then analyzes autoregulation (15.3), the feed-forward loop (15.4) and the larger motifs that make temporal programs and the global structure of sensory networks (15.5). It uses three earlier results without repeating them: the production–removal equation and the **response time** of a gene product in [7.2.22](/7.2.22#sec-22.3), the **gene regulation function** and its Hill form in [7.2.22](/7.2.22#sec-22.4), and the one-dimensional analysis of autoregulation and the toggle switch as dynamical systems in [7.6.33](/7.6.33). The kinetic modeling of networks in general, with numerical solution and parameter fitting, is in [7.9.14](/7.9.14); the motifs with feedback, which make decisions and oscillations, are the subject of [7.9.16](/7.9.16), and the propagation of noise through motifs and their evolution that of [7.9.17](/7.9.17).

## 15.1. The Elements of Transcription Networks

### 15.1.1. Genes, Factors and Signed Arrows

**Definition 15.1.1 (Transcription Network)** A **transcription network** of a cell is the directed graph whose vertices are genes (or operons) and which has an arc $X \to Y$ when the protein encoded by $X$ is a transcription factor that binds the regulatory region of $Y$ and changes its rate of transcription. Each arc carries a sign: $+$ if $X$ activates $Y$ (written $X \to Y$) and $-$ if it represses it ($X \dashv Y$).

A transcription network is the directly measured core of a **gene regulatory network** ([7.9.11](/7.9.11)): its arcs are physical regulatory interactions established by binding and by genetics, not statistical associations. The inputs of the network are signals, small molecules or modifications that change the activity of a factor $X$ to its active form $X^*$ within seconds or less; the outputs are the proteins made from the regulated genes, most of which are not transcription factors but enzymes, transporters and structural proteins. In *Escherichia coli* about $60\,\%$ of the arcs are activations, in yeast about $80\,\%$. The signs of the arcs leaving a factor are strongly correlated, since most factors act mainly as activators or mainly as repressors, while the signs of the arcs entering a gene are mixed: a typical gene is activated by some factors and repressed by others.

The dynamics of the network rests on a strong separation of time scales. In *E. coli*:

| Process | Typical time |
|---|---|
| A signal molecule binds a transcription factor and changes its activity | about $1\,\mathrm{ms}$ |
| An active factor binds or leaves its site on DNA | about $1\,\mathrm{s}$ |
| Transcription and translation of a gene | minutes |
| A $50\,\%$ change in the concentration of a stable protein | about one cell generation ($30$–$60\,\mathrm{min}$ in rich medium) |

Because binding equilibrates much faster than protein levels change, the production rate of a gene can be written as a function of the current active concentrations of its regulators, the **input function** of [7.2.22](/7.2.22#def-22.4.1), and the network becomes a system of ordinary differential equations of the form
$$
\frac{\mathrm{d}Y}{\mathrm{d}t} = f(X_1^*, \dots, X_m^*) - \alpha Y, \qquad \alpha = \alpha_{\mathrm{deg}} + \alpha_{\mathrm{dil}}, \tag{15.1}
$$
with a removal rate $\alpha$ that is the sum of active degradation and dilution by growth. Signaling proteins, whose interactions take seconds to minutes, can be treated as being at steady state on this slow scale (and are the subject of [7.9.16](/7.9.16#sec-16.2)).

### 15.1.2. Input Functions and Their Logic Approximation

For a single regulator, the Hill functions $\beta X^{*n}/(K^n + X^{*n})$ for an activator and $\beta K^n/(K^n + X^{*n})$ for a repressor, with **Hill coefficients** $n$ typically between $1$ and $4$, describe most measured input functions ([7.2.22](/7.2.22#def-22.4.1); their derivation from binding equilibria is in [7.6.4](/7.6.4#sec-4.3)). Each arc of the network thus carries at least three numbers, the maximal rate $\beta$, the threshold $K$ and the steepness $n$, all of which can be changed by point mutations in the promoter: $K$ by mutations in the binding site, $\beta$ by mutations in the RNA polymerase site. To see the logic of a circuit, it is useful to replace the Hill function by its limit $n \to \infty$.

**Formula 15.1.1 (Logic Input Functions)** With the step function $\theta(\cdot)$, equal to $1$ if its argument is true and $0$ otherwise, the logic approximations of activation and repression are
$$
f(X^*) = \beta\,\theta(X^* > K), \qquad f(X^*) = \beta\,\theta(X^* < K). \tag{15.2}
$$
For a gene with two regulators, the common logic functions are AND, $f = \beta\,\theta(X^* > K_X)\,\theta(Y^* > K_Y)$, OR, $f = \beta\,\theta(X^* > K_X \lor Y^* > K_Y)$, and the graded SUM function $f = \beta_XX^* + \beta_YY^*$.

With logic input functions, Eq. (15.1) is linear between threshold crossings and can be solved by hand: the variable relaxes exponentially toward $\beta/\alpha$ or toward $0$, and the only nonlinearity is the times at which thresholds are crossed. Most results of this chapter are derived in this way, and the figures check that they hold for smooth input functions too.

Multi-dimensional input functions follow from the same statistical mechanics as one-dimensional ones.

**Formula 15.1.2 (An Activator and a Repressor Binding Independently)** Let an activator $X$ (dissociation constant $K_1$) and a repressor $Y$ ($K_2$) bind two separate sites of a promoter independently, and let transcription occur at rate $\beta$ when $X$ is bound and $Y$ is not, and at the reduced rate $\beta'$ when both are bound. The promoter has the four states free, $X$, $Y$ and $XY$, with statistical weights $1$, $X/K_1$, $Y/K_2$ and $XY/K_1K_2$, so
$$
f(X, Y) = \frac{\beta X/K_1 + \beta' XY/(K_1K_2)}{1 + X/K_1 + Y/K_2 + XY/(K_1K_2)}. \tag{15.3}
$$
For $\beta' = 0$ the denominator factorizes, $f = \beta\,\frac{X/K_1}{1 + X/K_1}\cdot\frac{1}{1 + Y/K_2}$, a smooth version of the logic function $X \land \lnot Y$; for $\beta' > 0$ the function has three plateaus, $0$, $\beta$ and $\beta'$.

More generally, input functions of several factors are ratios of polynomials in the active concentrations, and interactions between the factors (cooperative binding, competition for overlapping sites) add cross terms. The measured input function of the *lac* promoter of *E. coli* as a function of cAMP and IPTG lies between AND and OR, and a few point mutations move it toward either (Setty, Mayo, Surette and Alon, 2003; Example 33.1.1 of [7.6.33](/7.6.33)). For most genes, however, the multi-dimensional input function has not been measured, which limits the analysis of the motifs with many inputs (15.5.3).

### 15.1.3. The Response Time and Fair Comparisons

The simplest arc, $X \to Y$ with no other regulation, already has the property that limits every transcriptional response. After a step of production from $0$ to $\beta$, $Y(t) = (\beta/\alpha)(1 - \mathrm{e}^{-\alpha t})$, and after production stops, $Y(t) = Y_{\mathrm{st}}\mathrm{e}^{-\alpha t}$; in both directions the response time is $T_{1/2} = \ln 2/\alpha$, independent of $\beta$ ([Definition 22.3.1 of 7.2.22](/7.2.22#def-22.3.1)). For a stable protein, $\alpha = \alpha_{\mathrm{dil}}$ and $T_{1/2}$ is one cell generation: a bacterium that must respond to a nutrient or a stress in minutes cannot do it with stable proteins and simple regulation. The motifs of this chapter can be read as solutions to this problem, but to say that one circuit is faster or more robust than another, the two must be compared fairly.

**Definition 15.1.2 (Mathematically Controlled Comparison)** A **mathematically controlled comparison** of two alternative circuit designs fixes all parameters that the designs share, and sets the remaining parameters so that both designs have the same steady state (or other reference behavior) that the cell is assumed to need; only then are other properties, such as response times or sensitivities to parameters, compared (Savageau, 1976).

Without this control, a circuit could appear faster simply because it makes more protein. The comparisons below always fix the removal rate $\alpha$ and the steady-state output.

## 15.2. Network Motifs

### 15.2.1. Randomized Networks as a Null Model

A transcription network is under constant mutational pressure. A single base change in a binding site can delete an arc, and new sites arise by mutation, duplication and horizontal transfer; a bacterial culture of $10^{10}$ cells, at about $10^{-9}$ mutations per base per replication, contains for every base of the genome about ten cells with a mutation in that base. Patterns that occur much more often than in randomized versions of the network must therefore be maintained by selection. This is the reasoning behind the definition of a **network motif** in [1.4.7](/1.4.7#def-7.8.4): a subgraph is a motif if its count in the real network exceeds its count in an ensemble of randomized networks by many standard deviations. The simplest ensemble is the directed **random graph** ([1.4.7](/1.4.7#def-7.2.1)), in which arcs are placed independently.

**Proposition 15.2.1 (Subgraph Counts in a Random Digraph)** Let a random digraph on $N$ vertices contain each of the $N^2$ possible arcs (self-arcs included) independently with probability $p = A/N^2$, where $A$ is the number of arcs of the real network, and let $\lambda = A/N$ be the mean degree. Then the expected numbers of self-arcs, feed-forward loops ($X \to Y$, $X \to Z$, $Y \to Z$ with $X, Y, Z$ distinct) and three-node feedback cycles ($X \to Y \to Z \to X$) are
$$
\langle N_{\mathrm{self}}\rangle = \lambda, \qquad \langle N_{\mathrm{FFL}}\rangle = N(N - 1)(N - 2)p^3 \approx \lambda^3, \qquad \langle N_{\mathrm{FBL}}\rangle = \tfrac13N(N - 1)(N - 2)p^3 \approx \frac{\lambda^3}{3}, \tag{15.4}
$$
and the number of self-arcs is approximately Poisson, with standard deviation $\sqrt{\lambda}$.

**Proof** There are $N$ possible self-arcs, each present with probability $p$, so $\langle N_{\mathrm{self}}\rangle = Np = \lambda$, and the count is binomial, $\mathrm{Bin}(N, p)$, close to $\mathrm{Poi}(\lambda)$ for small $p$. A feed-forward loop is specified by an ordered triple of distinct vertices $(X, Y, Z)$, since the three roles are different, and needs three specific arcs, present with probability $p^3$; there are $N(N - 1)(N - 2)$ triples. A three-cycle is specified by a cyclic order of three vertices, and each cycle corresponds to three ordered triples (its rotations). For $N \gg 1$, $N^3p^3 = \lambda^3$. $\square$

Two features matter. The expected counts depend on the network only through the mean degree, which for sparse biological networks is small, and the feed-forward loop and the feedback cycle, which have the same number of arcs, are expected in the ratio $3 : 1$.

**Example 15.2.1** The *E. coli* transcription network compiled by Shen-Orr, Milo, Mangan and Alon (2002) has $N = 424$ operons and $A = 519$ arcs, so $\lambda = 1.22$. It contains $40$ self-arcs ($34$ of them negative autoregulation), against $\lambda = 1.2 \pm 1.1$ in the random digraph: $z = (40 - 1.22)/1.11 = 35$. It contains $42$ feed-forward loops, against $\lambda^3 = 1.8$, and no three-node feedback cycle at all, against $0.6$. Autoregulation and the feed-forward loop are motifs; the feedback cycle is not. Of the $13$ connected three-vertex digraphs, only the feed-forward loop is a motif of this network and of the transcription network of yeast (Milo and colleagues, 2002; Lee and colleagues, 2002).

:::

The Erdős–Rényi ensemble ignores the very unequal degrees of real networks. Transcription networks have a few global regulators with hundreds of targets and many factors with one or two, and hubs alone create many triangles. The stricter null model keeps every vertex's in- and out-degree, using **degree-preserving randomization** ([Algorithm 7.4.2 of 1.4.7](/1.4.7#alg-7.4.2)). Against it, the feed-forward loop of *E. coli* remains a strong motif ($40$ observed, $7 \pm 3$ in randomized networks, $z \approx 10$; Milo and colleagues, 2002), with a much smaller z-score than against the Erdős–Rényi model.

**Algorithm 15.2.1 (Motif Detection)** Input: a directed network $G$ and a subgraph size $k$ (usually $3$ or $4$).

1. Enumerate all connected induced subgraphs of $G$ with $k$ vertices (for example with the ESU algorithm, [1.4.7](/1.4.7#sec-7.8.4)) and classify each up to **graph isomorphism**; for $k = 3$ there are $13$ classes of connected digraphs, for $k = 4$ there are $199$.
2. Generate $R$ randomized networks (typically $R = 100$–$1000$) by degree-preserving switching, keeping self-arcs and, if wanted, mutual arcs as separate fixed features; count the subgraph classes in each.
3. For each class $H$ compute $z(H) = (N_{\mathrm{real}} - \bar N_{\mathrm{rand}})/s_{\mathrm{rand}}$ and the empirical p-value; call $H$ a motif if $p < 0.01$, $N_{\mathrm{real}} \ge 4$ and $N_{\mathrm{real}} - \bar N_{\mathrm{rand}} > 0.1\bar N_{\mathrm{rand}}$.
4. Optionally normalize the vector of z-scores to unit length to obtain the *significance profile*, which can be compared between networks of different sizes.

The cost is dominated by step 1, proportional to the number of connected $k$-subgraphs, which grows rapidly with $k$ in networks with hubs; this is why motif analyses rarely go beyond five vertices.

**Example 15.2.2** The figure applies the algorithm to a simulated network of $400$ genes, $60$ of them transcription factors, wired hierarchically with heavy-tailed out-degrees and a tendency to close feed-forward loops and to share targets ($256$ arcs). It has $18$ feed-forward loops; Erdős–Rényi networks with the same numbers of vertices and arcs have $0.20 \pm 0.42$ ($z = 42$) and degree-preserving randomizations $0.87 \pm 0.89$ ($z = 19$). It has $116$ bi-fans (two regulators sharing two targets, 15.5.3) against $0.04 \pm 0.22$ and $12.4 \pm 4.0$ ($z = 526$ and $26$). It has no three-cycles, and neither have the degree-preserving randomizations, which keep the hierarchy of out-degrees; the Erdős–Rényi networks have $0.12$ on average. Both ensembles identify the same motifs, but the Erdős–Rényi z-scores are inflated by the degree heterogeneity that the stricter ensemble accounts for.

![Motif detection in a simulated hierarchical transcription network (400 genes, 60 factors, 256 arcs). A: the number of feed-forward loops in 200 Erdős–Rényi digraphs with the same numbers of vertices and arcs (gray) and in 200 degree-preserving randomizations (violet), and in the network itself (red line, 18). B: z-scores of the feed-forward loop, the three-node feedback cycle and the bi-fan against the two ensembles, on a compressed scale (the numbers are the z-scores): the feed-forward loop and the bi-fan are motifs against both ensembles, with smaller z-scores against the degree-preserving one; three-cycles are absent from the network and from the degree-preserving ensemble](./plots/motif_zscore.py)

```python
import numpy as np

def counts(A):
    """FFLs, three-cycles and bi-fans of a 0/1 adjacency matrix without self-arcs."""
    A2 = A @ A
    M = A @ A.T
    np.fill_diagonal(M, 0)
    return np.sum(A2 * A), np.trace(A2 @ A) / 3, np.sum(M * (M - 1) / 2) / 2

def degree_preserving(src, dst, rng, n_swaps):
    """Double-edge swaps a->b, c->d  =>  a->d, c->b that keep all in- and out-degrees."""
    src, dst = src.copy(), dst.copy()
    present = set(zip(src.tolist(), dst.tolist()))
    for _ in range(n_swaps):
        i, j = rng.integers(len(src), size=2)
        a, b, c, d = src[i], dst[i], src[j], dst[j]
        if a == d or c == b or (a, d) in present or (c, b) in present:
            continue                          # would create a self-arc or a double arc
        present -= {(a, b), (c, d)}
        present |= {(a, d), (c, b)}
        dst[i], dst[j] = d, b
    return src, dst
```

### 15.2.2. Motifs Across Networks

The same analysis applied to networks from other fields shows three regularities (Milo and colleagues, 2002 and 2004): most networks are built of a small set of motifs; networks from the same field share their motifs; and different fields have different motifs. The transcription networks of *E. coli* and yeast share the feed-forward loop and the bi-fan; the neuronal network of *Caenorhabditis elegans* has the same two and, among four-vertex patterns, the bi-parallel (diamond); food webs have three-chains and the diamond but not the feed-forward loop; and electronic circuits of different kinds have their own motifs, feedback loops in some, feed-forward patterns in others. The coincidence of motifs between transcription networks and neuronal networks, which work on very different scales of space and time, is discussed in [7.9.16](/7.9.16#sec-16.3). Motifs also generalize: in human cells, transcription networks among $475$ factors reconstructed from DNase I footprints in $41$ cell types differed in most of their arcs but were all enriched in feed-forward loops ([7.9.11](/7.9.11#sec-11.2.2); Neph and colleagues, 2012).

### 15.2.3. Global Structure

The motifs sit inside networks with characteristic global statistics:

- *Sparseness.* Of the $N^2$ possible arcs, typically less than $0.1\,\%$ are present; the mean degree $\lambda$ is a few arcs per vertex.
- *Asymmetric degree distributions.* The out-degree distribution is long-tailed: many factors regulate a few genes, a few global regulators (CRP, which senses glucose starvation, or the stress **σ factor** RpoS) regulate hundreds; it is roughly a power law over a limited range. The in-degree distribution is compact, close to Poisson: no bacterial gene has tens of inputs, partly because a bacterial promoter has room for only a few binding sites; animal genes, regulated through distant enhancers, have more. The **degree distribution** alone does not justify the label of a **scale-free network** ([1.4.7](/1.4.7#sec-7.4.5) for the statistics), and **preferential attachment** is not a plausible mechanism for a network whose arcs are selected one by one for function.
- *Clustering from motifs.* The undirected **clustering coefficient** is higher than in randomized networks, and almost all the triangles are feed-forward loops. The decline of the clustering coefficient with degree, $C(k) \sim 1/k$, follows from the way feed-forward loops are combined into multi-output feed-forward loops (15.5.2; [7.9.12](/7.9.12#sec-12.3.3)).
- *Hierarchy and modularity.* Apart from self-arcs, sensory transcription networks of bacteria are nearly **directed acyclic graphs**: factors are arranged in layers, and long feedback cycles are rare. They are modular: the normalized modularity measure $Q_m = (Q_{\mathrm{real}} - Q_{\mathrm{rand}})/(Q_{\max} - Q_{\mathrm{rand}})$, with $Q$ the Newman–Girvan **modularity** ([1.4.7](/1.4.7#def-7.7.3)) and the reference values from degree-preserving randomizations, is about $0.54$ for the transcription network of *E. coli* (Kashtan and Alon, 2005). Why evolution produces **modularity** is discussed in [7.9.17](/7.9.17).

## 15.3. Autoregulation

Self-arcs are the most significant pattern of Example 15.2.1, and most of them are repressions. The dynamics of a negatively autoregulated gene was analyzed in [7.2.22](/7.2.22#sec-22.6) and, as a one-dimensional dynamical system, in [7.6.33](/7.6.33#sec-33.2.3); here it is restated as a design principle with a controlled comparison.

**Proposition 15.3.1 (Negative Autoregulation Speeds Responses)** Let $X$ repress its own promoter with the logic input function $\beta\,\theta(X < K)$, with $K < \beta/\alpha$, and let it start at $X = 0$. Then $X$ settles at $X_{\mathrm{st}} = K$, and if removal is negligible while $X < K$ its response time is $T_{1/2}^{\mathrm{NAR}} \approx K/(2\beta)$. Compared with a simply regulated gene with the same removal rate and the same steady state ($\beta_{\mathrm{s}}/\alpha = K$),
$$
\frac{T_{1/2}^{\mathrm{NAR}}}{T_{1/2}^{\mathrm{simple}}} = \frac{1}{2\ln 2}\,\frac{\beta_{\mathrm{s}}}{\beta}. \tag{15.5}
$$
More generally, for any decreasing input function $f$ with the same steady state and the same $\alpha$, the autoregulated gene approaches its steady state faster than the simple gene from any initial state below it.

**Proof** Below $K$, $\dot X = \beta - \alpha X \approx \beta$, so $X \approx \beta t$ reaches $K/2$ at $t = K/(2\beta)$; at $X = K$ production stops whenever $X$ exceeds $K$, which pins $X$ at $K$. With $T_{1/2}^{\mathrm{simple}} = \ln 2/\alpha$ and $\alpha = \beta_{\mathrm{s}}/K$, Eq. (15.5) follows. For a general decreasing $f$ with $f(X_{\mathrm{st}}) = \alpha X_{\mathrm{st}} = \beta_{\mathrm{s}}$, $f(X) > \beta_{\mathrm{s}}$ for $X < X_{\mathrm{st}}$, so the rate $\dot X = f(X) - \alpha X$ exceeds the rate $\beta_{\mathrm{s}} - \alpha X$ of the simple gene at every level below the steady state. Comparing the two solutions from the same initial value, the autoregulated one stays above the simple one (where they would meet, its derivative is larger), so it crosses every level below $X_{\mathrm{st}}$ earlier. $\square$

A promoter ten times stronger than the simple design gives, by Eq. (15.5), a response $0.072$ times as long, fourteen-fold faster; Rosenfeld, Elowitz and Alon (2002) measured about fivefold for an autoregulated TetR. A strong motor needs good brakes: the strong promoter gives the fast rise, the self-repression stops it at the desired level. Turning off is not accelerated, because when production stops both designs decay at rate $\alpha$. Negative autoregulation has a second benefit: its steady state $X_{\mathrm{st}} = K$ depends on the binding affinity, which is fixed in the DNA, rather than on the production rate, which fluctuates from cell to cell, and with a steep input function it depends only weakly on $\alpha$, hence on growth rate (Becskei and Serrano, 2000; Klumpp, Zhang and Hwa, 2009; the effect on noise is in [7.9.17](/7.9.17)).

Positive autoregulation does the opposite: by the same comparison argument with an increasing input function, it slows the response, and with a cooperative input function it can make the gene bistable. It is rare in sensory networks and common in developmental networks, where slow responses and memory are useful; it is treated in [7.9.16](/7.9.16#sec-16.1).

## 15.4. The Feed-Forward Loop

### 15.4.1. Eight Types

**Definition 15.4.1 (Feed-Forward Loop)** A **feed-forward loop** (FFL) is a three-vertex subgraph in which a transcription factor $X$ regulates a second factor $Y$ and both regulate a gene $Z$: the arcs $X \to Y$, $X \to Z$ and $Y \to Z$. The gene $Z$ thus receives a direct path from $X$ and an indirect path through $Y$.

With a sign on each of the three arcs there are $2^3 = 8$ types of FFL. The sign of a path is the product of the signs of its arcs.

**Definition 15.4.2 (Coherent and Incoherent Feed-Forward Loops)** A **coherent feed-forward loop** is an FFL in which the sign of the direct path $X \to Z$ equals the sign of the indirect path $X \to Y \to Z$; an **incoherent feed-forward loop** is one in which the two signs differ. The coherent type 1 (C1-FFL) has three activations; the incoherent type 1 (I1-FFL) has $X$ activating $Y$ and $Z$ and $Y$ repressing $Z$.

![The eight types of feed-forward loops (open arrowheads: activation; bars: repression). The coherent types C1–C4 have an even number of repressions and the incoherent types I1–I4 an odd number. In the transcription networks of *E. coli* and yeast, C1 and I1 together account for most feed-forward loops](./plots/ffl_types.py)

If signs were assigned at random, with about $60\,\%$ activations as in *E. coli*, all eight types would occur with comparable frequencies. Instead, two types dominate: C1-FFLs and I1-FFLs make up more than $80\,\%$ of the FFLs of *E. coli* and yeast (Mangan and Alon, 2003; Ma and colleagues, 2004). To understand an FFL one needs, besides the signs, the input function of $Z$, AND or OR, and the external signals $S_X$ and $S_Y$ that activate $X$ and $Y$. The analysis below assumes that $S_Y$ is present, so that $Y^* = Y$, and follows the response to steps of $S_X$.

### 15.4.2. The Coherent Type-1 FFL Is a Sign-Sensitive Delay

**Formula 15.4.1 (C1-FFL with an AND Gate)** With logic input functions, the C1-FFL with an AND gate at the promoter of $Z$ obeys
$$
\frac{\mathrm{d}Y}{\mathrm{d}t} = \beta_Y\,\theta(X^* > K_{XY}) - \alpha_YY, \qquad \frac{\mathrm{d}Z}{\mathrm{d}t} = \beta_Z\,\theta(X^* > K_{XZ})\,\theta(Y > K_{YZ}) - \alpha_ZZ. \tag{15.6}
$$

**Proposition 15.4.1 (Delay of the C1-FFL)** Let $S_X$ appear at $t = 0$, so that $X^*$ jumps above both thresholds, with $Y(0) = Z(0) = 0$, and let $Y_{\mathrm{st}} = \beta_Y/\alpha_Y > K_{YZ}$. Then $Z$ starts to be produced only after the delay
$$
T_{\mathrm{ON}} = \frac{1}{\alpha_Y}\ln\frac{1}{1 - K_{YZ}/Y_{\mathrm{st}}}. \tag{15.7}
$$
If $S_X$ disappears, the production of $Z$ stops at once. A pulse of $S_X$ shorter than $T_{\mathrm{ON}}$ produces no $Z$ at all.

**Proof** After the step, $Y(t) = Y_{\mathrm{st}}(1 - \mathrm{e}^{-\alpha_Yt})$, which reaches $K_{YZ}$ at the time (15.7); before that, the AND gate is closed. When $S_X$ is removed, $\theta(X^* > K_{XZ}) = 0$ and the gate closes whatever the level of $Y$. A pulse of duration $D < T_{\mathrm{ON}}$ ends before $Y$ reaches $K_{YZ}$, after which $Y$ decays, so the two conditions of the gate are never fulfilled together. $\square$

The delay is tuned by two quantities, the lifetime of $Y$ and the ratio of its threshold to its steady state: for $K_{YZ}/Y_{\mathrm{st}} = 0.5$ it is $\ln 2/\alpha_Y$, one response time of $Y$, for $0.9$ it is $2.3/\alpha_Y$, and it diverges as $K_{YZ} \to Y_{\mathrm{st}}$. A robust design keeps $K_{YZ}$ well below $Y_{\mathrm{st}}$, since $Y_{\mathrm{st}}$ varies from cell to cell.

**Definition 15.4.3 (Sign-Sensitive Delay)** A circuit is a **sign-sensitive delay** element if its output responds after a delay to steps of the input in one direction (ON or OFF) and without delay to steps in the other direction. Such an element is a *persistence detector*: it ignores input pulses in the delayed direction that are shorter than the delay.

![The coherent type-1 FFL with logic input functions (all production and removal rates 1, thresholds K = 0.5 of the steady state). A: AND gate: after the ON step of Sx at t = 0 (shaded: Sx present), Y rises like a simply regulated gene, and Z starts only when Y crosses K_YZ, after T_ON = ln 2; after the OFF step at t = 5, Z falls at once, like a simply regulated gene. B: the peak of Z after pulses of Sx of duration D: simple regulation responds to every pulse, the C1-FFL with AND gate only to pulses longer than T_ON. C: OR gate: no delay at the ON step, a delay T_OFF = ln 2 at the OFF step, during which Y alone keeps Z on](./plots/c1ffl.py)

Why would a cell want this? Engineers use sign-sensitive delays when the costs of the two errors are asymmetric. In the arabinose system of *E. coli*, the genes for arabinose uptake and breakdown are activated by CRP–cAMP (which signals the absence of glucose; **catabolite activator protein**, [7.2.11](/7.2.11)) and by AraC (which senses arabinose); CRP also activates *araC*, and the *araBAD* promoter needs both, a C1-FFL with an AND-like gate (Example 15.4.1). Making the arabinose enzymes in response to a brief glucose dip would waste resources, whereas stopping too early costs little, because the enzymes already made persist for a generation.

**Example 15.4.1 (The Arabinose System)** Mangan, Zaslaver and Alon (2003) followed the activity of the *araBAD* promoter with a GFP reporter after steps of cAMP in the presence of arabinose. After ON steps the promoter switched on with a delay of about $20\,\mathrm{min}$ relative to the *lac* promoter, which responds to the same signal without an FFL; after OFF steps neither showed a delay. The delay is of the order of the duration of the spurious drops in glucose that *E. coli* experiences when growth conditions change, so the FFL appears tuned to filter them. The circuit behaves as predicted even though it is embedded in other interactions, such as the feedback through the transport of arabinose.

:::

With an OR gate the signs of the delay are reversed.

**Proposition 15.4.2 (The OR-Gate C1-FFL)** With $\theta(X^* > K_{XZ} \lor Y > K_{YZ})$ in Eq. (15.6), $Z$ is produced immediately after an ON step of $S_X$, and after an OFF step from the steady state it continues to be produced for
$$
T_{\mathrm{OFF}} = \frac{1}{\alpha_Y}\ln\frac{Y_{\mathrm{st}}}{K_{YZ}}. \tag{15.8}
$$

**Proof** After the ON step one input of the OR gate is satisfied at once. After the OFF step $X^*$ falls below $K_{XZ}$ at once, but $Y(t) = Y_{\mathrm{st}}\mathrm{e}^{-\alpha_Yt}$ stays above $K_{YZ}$ until the time (15.8). $\square$

The flagellar system of *E. coli* contains such a loop: the master regulator FlhDC activates the **σ factor** FliA, and both activate the operons of the flagellar motor with a SUM-like input function. When FlhDC activity is lost, FliA keeps the motor genes on for about one cell generation, comparable to the time needed to finish assembling a motor; deleting *fliA* removes the delay (Kalir, Mangan and Alon, 2005). Of the four coherent types, each acts as a sign-sensitive delay, for ON or OFF steps according to its signs and gate.

### 15.4.3. The Incoherent Type-1 FFL: Pulses, Acceleration and Biphasic Responses

In the I1-FFL, $X$ activates $Z$ directly and indirectly represses it through $Y$. With complete repression, $Z$ rises after an ON step until $Y$ crosses its repression threshold and then decays: the circuit generates a pulse. With partial repression it settles at a reduced level, and the rise to that level is faster than for a simple gene.

**Proposition 15.4.3 (Response of the I1-FFL)** Let $Z$ be produced at rate $\beta_Z$ while $Y < K_{YZ}$ and at the reduced rate $\beta_Z/F$ ($F > 1$) while $Y > K_{YZ}$, and let $Y$ rise as in Proposition 15.4.1. After an ON step of $S_X$ at $t = 0$:

1. repression starts at $T_{\mathrm{rep}} = \alpha_Y^{-1}\ln[1/(1 - K_{YZ}/Y_{\mathrm{st}})]$, at which $Z$ has reached $(\beta_Z/\alpha_Z)(1 - \mathrm{e}^{-\alpha_ZT_{\mathrm{rep}}})$;
2. after $T_{\mathrm{rep}}$, $Z$ relaxes to $Z_{\mathrm{st}} = \beta_Z/(F\alpha_Z)$; for $F \to \infty$ the response is a pulse;
3. if $Z$ reaches $Z_{\mathrm{st}}/2$ before $T_{\mathrm{rep}}$, the response time is
$$
T_{1/2}^{\mathrm{I1}} = \frac{1}{\alpha_Z}\ln\frac{1}{1 - 1/(2F)}, \tag{15.9}
$$
smaller than the response time $\ln 2/\alpha_Z$ of a simple gene with the same steady state and removal rate, by a factor that grows with the repression factor $F$.

**Proof** Before $T_{\mathrm{rep}}$, $Z(t) = (\beta_Z/\alpha_Z)(1 - \mathrm{e}^{-\alpha_Zt})$; solving $Z = Z_{\mathrm{st}}/2 = \beta_Z/(2F\alpha_Z)$ gives Eq. (15.9). After $T_{\mathrm{rep}}$ the equation is $\dot Z = \beta_Z/F - \alpha_ZZ$, whose solution relaxes to $Z_{\mathrm{st}}$. For $F = 5$, (15.9) gives $0.105/\alpha_Z$, against $0.693/\alpha_Z$. $\square$

If $T_{\mathrm{rep}}$ is long compared with $T_{1/2}^{\mathrm{I1}}$, $Z$ overshoots its steady state before repression sets in; a large speed-up without overshoot needs the repressor to act early, at a low threshold. With smooth input functions and repression by $Y$ at a low threshold, the I1-FFL of the figure (panel B) reaches half its steady state 4.4 times faster than simple regulation, with an overshoot of less than $0.1\,\%$. The I1-FFL is the third way of speeding up a transcriptional response, besides fast degradation, which costs a futile cycle of synthesis and breakdown, and negative autoregulation, which works only for transcription factors (Proposition 15.3.1); the I1-FFL can speed up the response of any gene.

![The incoherent type-1 FFL. A: logic input functions and complete repression (rates 1, K_YZ = 0.5): after the ON step, Z rises until the repressor Y crosses its threshold at t = ln 2 and then decays: a pulse. B: Hill input functions and partial repression, dZ/dt = βg(Y) − Z with g(Y) = 1/F + (1 − 1/F)/(1 + (Y/K)²), F = 5 and K = 0.1 (in units of the steady state of Y), β chosen so that Z_st = 1: the I1-FFL (green) reaches half of its steady state at t = 0.16, a simply regulated gene with the same steady state and removal rate (dashed) at t = 0.69. C: steady-state dose response when X activates Z at a lower threshold than Y (Z_st = [X/(0.1 + X)]/[1 + (Y/0.3)²] with Y = X/(10 + X)): the output first rises and then falls with the input (biphasic, inverse-U shape); without the repressor site (dashed) it rises monotonically](./plots/i1ffl.py)

Three experimental systems illustrate the three behaviors. In the galactose system of *E. coli*, CRP activates the *gal* genes and the repressor GalS, which represses them: the response to glucose starvation is faster than for simply regulated genes, and deleting the GalS site in the target promoter abolishes the acceleration (Mangan and colleagues, 2006); the same loop makes the steady-state response to cAMP biphasic, which becomes monotonic when *galS* is deleted (Kaplan and colleagues, 2008). A synthetic I1-FFL built in *E. coli* from the activator LuxR, the λ repressor CI and a GFP output produced pulses in response to steps of the LuxR inducer (Basu, Mehreja, Thiberge, Chen and Weiss, 2004). In mammalian cells stimulated with EGF, immediate-early genes are induced in a pulse, terminated by a set of repressors (KLF2, ATF3 and others) that the same stimulus induces (Amit and colleagues, 2007). A biphasic response is useful when an intermediate dose of the input is optimal, and a pulse when a transient program, such as the first wave of a stress response, should end on its own.

### 15.4.4. Adaptation and Fold-Change Detection

A pulse that returns exactly to the prestimulus level is **perfect adaptation**, and the I1-FFL is one of the two network cores that achieve it robustly, the other being **integral feedback** ([7.6.35](/7.6.35#sec-35.7.1); the two circuits as equations in [Formula 18.4.2 of 7.3.18](/7.3.18#fml-18.4.2)). It can also achieve **fold-change detection** ([Definition 35.6.4 of 7.6.35](/7.6.35#def-35.6.4)), a response that depends only on relative changes of the input. A general criterion shows when.

**Proposition 15.4.4 (Fold-Change Detection by Scalar Symmetry)** Let a system with input $u(t) > 0$, internal variable $x$ and output $z$ obey $\dot x = g(x, z, u)$, $\dot z = h(x, z, u)$, with a unique stable steady state for each constant input, and let
$$
g(px, z, pu) = p\,g(x, z, u), \qquad h(px, z, pu) = h(x, z, u) \quad \text{for all } p > 0. \tag{15.10}
$$
Then the output after an input $pu(t)$, starting from the steady state for $pu(0)$, is the same as the output after $u(t)$ starting from the steady state for $u(0)$: the system shows fold-change detection (Shoval and colleagues, 2010).

**Proof** Let $(x(t), z(t))$ solve the system with input $u(t)$. Then $(\tilde x, \tilde z) = (px, z)$ satisfies $\dot{\tilde x} = p\,g(x, z, u) = g(px, z, pu)$ and $\dot{\tilde z} = h(x, z, u) = h(px, z, pu)$, so it solves the system with input $pu$. If $(x_0, z_0)$ is the steady state for $u(0)$, then $(px_0, z_0)$ is a steady state for $pu(0)$ by (15.10), and by uniqueness it is the steady state; the two solutions start from corresponding initial conditions and therefore have the same output for all times. $\square$

In an I1-FFL, take $x = Y$ with $\dot Y = \beta_YX - \alpha_YY$, and let the promoter of $Z$ be in the regime in which the activator binds weakly and the repressor strongly, so that by Formula 15.1.2 its activity is approximately $\beta_Z(X/K_1)/(Y/K_2)$: then $\dot Z = \beta'X/Y - \alpha_ZZ$. Under $X \to pX$, $Y \to pY$ the first equation scales by $p$ and the second is invariant, so Eq. (15.10) holds: the I1-FFL responds identically to a step from $1$ to $2$ and from $10$ to $20$. Goentoro, Shoval, Kirschner and Alon (2009) derived the parameter regime in which the I1-FFL is a fold-change detector, and β-catenin signaling, whose target genes respond to the fold change rather than the absolute level of nuclear β-catenin, is one case in which it operates (Goentoro and Kirschner, 2009). The chemotaxis network of *E. coli* reaches fold-change detection through a different core, integral feedback with logarithmic sensing ([Proposition 35.6.1 of 7.6.35](/7.6.35#prop-35.6.1)), and the same proposition covers it with $x = \exp(\alpha m)$.

### 15.4.5. Why These Two Types

All four coherent types can act as sign-sensitive delays, and all four incoherent types can produce pulses and non-monotonic dose responses; why C1 and I1 dominate is not settled. One observation is that in both, $X$ acts as an activator on both of its targets, as most factors of these activator-rich networks do. A clearer fact is evolutionary: when homologous target genes in two species are both regulated by FFLs, the regulators $X$ and $Y$ are usually not homologous, often from different families of transcription factors (Conant and Wagner, 2003; Babu, Luscombe, Aravind, Gerstein and Teichmann, 2004). The FFL has been rediscovered by convergent evolution rather than inherited, which supports the view that it is selected for its function; the conditions under which an FFL pays for itself in a fluctuating environment are discussed in [7.9.17](/7.9.17).

## 15.5. Temporal Programs and the Global Structure of Sensory Networks

### 15.5.1. Single-Input Modules

**Definition 15.5.1 (Single-Input Module)** A **single-input module** (SIM) is a motif in which one transcription factor $X$ regulates a group of genes $Z_1, \dots, Z_n$ that have no other transcriptional input, all with the same sign; $X$ is usually autoregulated.

Single-input modules control sets of genes with a common function: the enzymes of a metabolic pathway (the arginine biosynthesis genes under ArgR), the genes of a stress response, the subunits of a protein machine. Their role is not only coordination: different promoters have different thresholds $K_i$ for $X$, and a gradually changing activity of $X$ crosses them at different times. The order of activation follows from [Proposition 20.6.1 of 7.6.20](/7.6.20#prop-20.6.1); the order of deactivation follows as well.

**Proposition 15.5.1 (Last In, First Out)** Let the activity of $X$ rise as $X(t) = X_{\mathrm{st}}(1 - \mathrm{e}^{-\alpha t})$ and later, from the level $X_1$ reached when its production stops at $t_1$, decay as $X_1\mathrm{e}^{-\alpha(t - t_1)}$, and let gene $Z_i$ be on while $X > K_i$, with $K_1 < K_2 < \dots < K_n < X_1$. Then gene $i$ switches on at $t_i = \alpha^{-1}\ln[1/(1 - K_i/X_{\mathrm{st}})]$ and off at $t_i' = t_1 + \alpha^{-1}\ln(X_1/K_i)$: the genes switch on in the order $1, 2, \dots, n$ and off in the order $n, \dots, 2, 1$.

**Proof** Both $t_i$ and $t_i'$ solve $X(t) = K_i$ on the rising and the falling branch; $t_i$ increases with $K_i$ and $t_i'$ decreases with $K_i$. $\square$

In the arginine system the genes are expressed in the order of the reactions of the pathway, with delays of several minutes between them, so that no enzyme is made before the one that supplies its substrate (Zaslaver and colleagues, 2004): *just-in-time* production. Temporal order can be changed by mutations in the binding sites, which change the thresholds. In the SOS response, all genes are induced quickly when LexA is cleaved, and as the damage is repaired they are switched off in an order set by their affinities, those for mild repair first and those for drastic repair (error-prone polymerases) last (Ronen and colleagues, 2002; the graded affinities of the LexA regulon are discussed in [7.2.8](/7.2.8)). Like the FFL, SIMs have evolved convergently: SIMs controlling homologous genes in different organisms have unrelated master regulators.

### 15.5.2. Multi-Output Feed-Forward Loops

For assembly processes, last in, first out is the wrong order: when the process stops, the early parts should be stopped first. Among the $199$ connected four-vertex digraphs, only two are motifs of the sensory transcription networks of *E. coli* and yeast, the two-output FFL and the bi-fan (15.5.3), and the first generalizes to the following.

**Definition 15.5.2 (Multi-Output Feed-Forward Loop)** A **multi-output feed-forward loop** is a motif in which a transcription factor $X$ regulates a second factor $Y$, and both regulate each of a set of output genes $Z_1, \dots, Z_m$. It contains one FFL for every output.

Neither multiple inputs nor multiple middle nodes generalize the FFL into motifs of these networks (Kashtan, Itzkovitz, Milo and Alon, 2004); the multi-output FFL is the way FFLs are combined, which, as noted in 15.2.3, produces the scaling $C(k) \sim 1/k$ of the clustering coefficient.

**Proposition 15.5.2 (First In, First Out)** In a multi-output FFL with OR gates, $Z_i$ on while $X > K_i$ or $Y > K_i'$, let $X$ rise and fall as in Proposition 15.5.1 with $K_1 < \dots < K_m$, and let $Y$, activated by $X$, lag behind $X$ on the way up and outlast it on the way down, so that each gene is switched on by $X$ (or by $Y$ at a time that preserves the order) and switched off when $Y$ falls below $K_i'$. If the thresholds of $Y$ are in the opposite order, $K_1' > \dots > K_m'$, the genes switch on in the order $1, \dots, m$ and off in the order $1, \dots, m$.

**Proof** The onsets are the threshold crossings of the rising $X$, in increasing order of $K_i$ (Proposition 15.5.1). The offsets are the crossings of the decaying $Y$, which on its falling branch passes the highest threshold first; since $K_1'$ is the highest, gene $1$ goes off first, then gene $2$, and so on. $\square$

![Temporal programs from graded thresholds (logic input functions; the master regulator X is produced for 0 < t < 4 and removed at rate 1). A: single-input module with thresholds 0.3, 0.5 and 0.7 for Z1, Z2, Z3 (dotted): the bars show when each gene is on; they switch on in the order 1, 2, 3 and off in the order 3, 2, 1. B: multi-output FFL with OR gates: Y is made while X > 0.2 and removed at half the rate of X; Y thresholds are in the reverse order (0.7, 0.5, 0.3). The genes switch on in the order 1, 2, 3 (at t = 0.36, 0.69 and 0.94) and, held on by the slowly decaying Y, off in the same order (at t = 6.2, 6.8 and 7.9)](./plots/sim_order.py)

The flagellar genes of *E. coli* show exactly this pattern. FlhDC ($X$) activates FliA ($Y$), and both activate several operons of the motor and hook with SUM-like input functions. As FlhDC rises, the operons are switched on one by one, about a tenth of a generation apart, in the order in which the motor is assembled, from the ring in the inner membrane outward (Kalir and colleagues, 2001; [7.6.20](/7.6.20#sec-20.6.2)); when flagella are no longer needed, they are switched off in the same order. Kalir and Alon (2004) measured the thresholds of each promoter for FlhDC and FliA and found them in opposite orders, and rewired the order by mutations in the binding sites. Each output also inherits the persistence detection of the OR-gate C1-FFL (Proposition 15.4.2): a brief loss of FlhDC, when the cell swims briefly into better conditions, does not stop flagellar synthesis.

### 15.5.3. Bi-Fans and Dense Overlapping Regulons

**Definition 15.5.3 (Bi-Fan)** A **bi-fan** is a four-vertex motif in which two transcription factors $X_1$ and $X_2$ both regulate two genes $Z_1$ and $Z_2$.

**Definition 15.5.4 (Dense Overlapping Regulons)** A set of **dense overlapping regulons** (DOR) is a motif made of a layer of transcription factors $X_1, \dots, X_n$ and a layer of output genes $Z_1, \dots, Z_m$ in which each output is regulated by several of the factors, with arcs much denser than in randomized networks but not necessarily complete. (A **regulon** is the set of genes regulated by one factor.)

The bi-fan is the smallest DOR. A DOR is an array of gates: each output computes its own function of the inputs, and the function of the DOR is the set of its multi-dimensional input functions, mostly unknown (15.1.2). The *E. coli* and yeast networks have several large DORs, each controlling tens to hundreds of genes with a shared global function: carbon utilization, stress responses, biosynthesis of a class of molecules. Often a global regulator controls most genes of the DOR and specific regulators control subsets: CRP, signaling glucose starvation, together with factors that each sense one sugar, decides which sugar-utilization operons are expressed.

### 15.5.4. The Global Picture

The four motif families, autoregulation, FFLs, SIMs and DORs, cover nearly all the genes of the sensory transcription networks studied so far, from bacteria to mammals (Harbison and colleagues, 2004; Boyer and colleagues, 2005; Odom and colleagues, 2006). Their arrangement is simple. If each SIM, multi-output FFL and DOR is replaced by a single symbol (a coarse-graining of the network; Itzkovitz and colleagues, 2005), the network of *E. coli* appears as a single layer of DORs, with no DOR feeding another; FFLs and SIMs lie within the DORs, and negative autoregulation decorates the master regulators of SIMs and the factors of FFLs. Most of the computation is done at one layer of promoters.

The patterns that are absent are as informative. Three-node feedback cycles are anti-motifs, and longer cycles are rare: a negative loop tends to oscillate and a positive loop to be bistable, both undesirable for networks that must give reliable, reversible responses to the environment, and the motifs that do occur are dynamically very stable (Prill, Iglesias and Levchenko, 2005). Feedback, memory and oscillation belong to developmental and signaling networks ([7.9.16](/7.9.16)). Because motifs are connected so that each keeps its function, the dynamics of the whole can be understood from the dynamics of the parts.

### 15.5.5. Interlocked Feed-Forward Loops in Sporulation

When *Bacillus subtilis* starves, it forms a spore, and the mother cell, which engulfs and nourishes the forespore, expresses hundreds of genes in successive waves. The network that controls them is built of linked FFLs (Eichenberger and colleagues, 2004). The **σ factor** $\sigma^{\mathrm{E}}$ activates a set of early genes and the factor SpoIIID, which represses some of them: an I1-FFL, a pulse of early genes. $\sigma^{\mathrm{E}}$ and SpoIIID together are needed for the production of $\sigma^{\mathrm{K}}$: a C1-FFL with an AND-like gate, which ensures that $\sigma^{\mathrm{K}}$ appears only if the $\sigma^{\mathrm{E}}$ program persists. $\sigma^{\mathrm{K}}$ in turn activates a second set of genes and the factor GerE, which represses some of them (a second I1-FFL), and $\sigma^{\mathrm{K}}$ and GerE together activate the late genes, which encode the spore coat (a second C1-FFL).

**Example 15.5.1** With logic input functions, all rates $1$ and all thresholds $0.5$ (figure), the network produces three waves. The early genes rise from $t = 0$ and are shut off by SpoIIID at $t = \ln 2 = 0.69$; $\sigma^{\mathrm{K}}$ starts at $0.69$ and crosses its threshold at $\ln 4 = 1.39$, when the middle genes start; GerE crosses its threshold at $3\ln 2 = 2.08$, which ends the middle wave and starts the late genes. Each FFL in this network is in fact a multi-output FFL, since each output is a group of genes, and finer temporal order arises within each group.

![Three waves of gene expression from two interlocked pairs of feed-forward loops in the mother cell of sporulating *B. subtilis* (logic input functions, all rates 1, thresholds 0.5). A: the early genes Z1 (activated by σE and repressed by SpoIIID), the middle genes Z2 (activated by σK and repressed by GerE) and the late genes Z3 (activated by σK AND GerE). B: the regulators: σE (X1) is active from t = 0; SpoIIID (Y1) crosses its threshold at t = 0.69, which shuts off Z1 and, together with σE, starts σK (X2); GerE (Y2) crosses its threshold at t = 2.08](./plots/sporulation.py)

The linkage keeps each FFL autonomous, so that the dynamics of the network follows from that of its parts. Of the many ways in which FFLs could be linked, most would not allow such a decomposition, and the observation that real networks are built this way suggests that understandability, a central property of engineered systems, may be a property of evolved networks as well.

## Summary

- A transcription network (Definition 15.1.1) is a signed directed graph whose dynamics, thanks to the separation of time scales, is $\dot Y = f(X^*) - \alpha Y$ (Eq. (15.1)); input functions are Hill functions, approximated by logic functions (Formula 15.1.1), and multi-dimensional input functions follow from binding statistics (Formula 15.1.2). The response time of simple regulation is $\ln 2/\alpha$, one generation for stable proteins; designs are compared at equal steady state and removal rate (Definition 15.1.2).
- A network motif is a subgraph much more frequent than in randomized networks. In a random digraph the expected counts are $\lambda$ self-arcs, $\lambda^3$ FFLs and $\lambda^3/3$ three-cycles (Proposition 15.2.1); *E. coli* has $40$ self-arcs and $42$ FFLs against $1.2$ and $1.8$ (Example 15.2.1). Degree-preserving ensembles are the stricter null model (Algorithm 15.2.1, Example 15.2.2). Transcription networks are sparse, with long-tailed out-degrees, compact in-degrees, few cycles and high modularity.

| Motif | Function | Key result | Example |
|---|---|---|---|
| Negative autoregulation | faster response, robust level | $T^{\mathrm{NAR}}/T^{\mathrm{simple}} = \beta_{\mathrm{s}}/(2\beta\ln 2)$ (Proposition 15.3.1) | TetR, most autoregulated factors |
| C1-FFL, AND | sign-sensitive delay at ON, persistence detection | $T_{\mathrm{ON}} = \alpha_Y^{-1}\ln[1/(1 - K_{YZ}/Y_{\mathrm{st}})]$ (Proposition 15.4.1) | arabinose (CRP, AraC) |
| C1-FFL, OR | delay at OFF | $T_{\mathrm{OFF}} = \alpha_Y^{-1}\ln(Y_{\mathrm{st}}/K_{YZ})$ (Proposition 15.4.2) | flagella (FlhDC, FliA) |
| I1-FFL | pulse, acceleration, biphasic dose response, fold-change detection | $T_{1/2} = \alpha_Z^{-1}\ln[1/(1 - 1/2F)]$ (Proposition 15.4.3); scalar symmetry (Proposition 15.4.4) | galactose (CRP, GalS), EGF early genes |
| Single-input module | coordinated control, LIFO order, just-in-time production | Proposition 15.5.1 | arginine, SOS |
| Multi-output FFL | FIFO order, persistence detection for each output | opposite threshold hierarchies (Proposition 15.5.2) | flagella |
| Bi-fan, DOR | combinatorial decisions | input functions of each output | CRP with sugar-specific regulators |

- Most FFLs are of types C1 and I1, and FFLs and SIMs have evolved convergently. Sensory networks are a single layer of DORs containing FFLs and SIMs, without feedback cycles; linked motifs keep their functions, as in the three-wave program of sporulation (Example 15.5.1).

## Questions

1. Why do the expected numbers of FFLs and of three-node feedback cycles in a random digraph differ by a factor of three, although both subgraphs have three arcs?

   **Answer** An FFL has three distinguishable roles (source $X$, middle $Y$, target $Z$), so each ordered triple of distinct vertices defines a different FFL: $N(N - 1)(N - 2)$ candidates. A three-cycle has rotational symmetry: the ordered triples $(X, Y, Z)$, $(Y, Z, X)$ and $(Z, X, Y)$ describe the same cycle, so there are only $N(N - 1)(N - 2)/3$ candidates. Each candidate needs three specific arcs, with probability $p^3$, which gives $\lambda^3$ and $\lambda^3/3$.

2. A network has $N = 1000$ genes and $A = 2000$ arcs, $60$ self-arcs and $150$ FFLs. Compute the z-scores against the Erdős–Rényi model, and explain why the FFL z-score should not be trusted without a degree-preserving ensemble.

   **Answer** $\lambda = 2$. Self-arcs: mean $2$, standard deviation $\sqrt2 = 1.41$, $z = 58/1.41 = 41$. FFLs: mean $\lambda^3 = 8$; the standard deviation is roughly $\sqrt8 = 2.8$, so $z \approx 142/2.8 = 50$. Self-arcs are not affected by hubs, but triangles are: a hub with $k$ targets has $\binom{k}{2}$ pairs of targets, each of which closes an FFL if one regulates the other, so heavy-tailed out-degrees alone raise the expected FFL count far above $\lambda^3$. The degree-preserving ensemble keeps the hubs and gives the relevant baseline (in Example 15.2.2 the z-score falls from $42$ to $19$).

3. In a C1-FFL with an AND gate, $Y$ is a stable protein in bacteria with a doubling time of $40\,\mathrm{min}$, and $K_{YZ} = 0.3\,Y_{\mathrm{st}}$. What is $T_{\mathrm{ON}}$? How could the cell double the delay without changing the steady state of $Y$?

   **Answer** $\alpha_Y = \ln 2/40\,\mathrm{min} = 0.0173\,\mathrm{min^{-1}}$, and $T_{\mathrm{ON}} = \alpha_Y^{-1}\ln(1/0.7) = 0.357/0.0173 = 20.6\,\mathrm{min}$. To double it, raise the threshold so that $\ln[1/(1 - K/Y_{\mathrm{st}})] = 0.713$, that is $K/Y_{\mathrm{st}} = 1 - \mathrm{e}^{-0.713} = 0.51$, by weakening the binding site of $Y$ in the promoter of $Z$. (Making $Y$ more stable is not possible for a protein already removed only by dilution; making it less stable shortens the delay.)

4. Show that a C1-FFL with an AND gate responds to an input $S_X$ that is switched off for a short time $D$ after a long ON period with a delay that depends on $D$, and explain in what sense this is a short-term memory.

   **Answer** During the OFF period $Y$ decays from $Y_{\mathrm{st}}$ as $Y_{\mathrm{st}}\mathrm{e}^{-\alpha_YD}$. If this is still above $K_{YZ}$, that is $D < \alpha_Y^{-1}\ln(Y_{\mathrm{st}}/K_{YZ})$, then $Z$ responds without delay when $S_X$ returns. Otherwise $Y$ must climb back from $Y_{\mathrm{st}}\mathrm{e}^{-\alpha_YD}$ to $K_{YZ}$, which takes $\alpha_Y^{-1}\ln[(1 - \mathrm{e}^{-\alpha_YD})/(1 - K_{YZ}/Y_{\mathrm{st}})]$, growing toward $T_{\mathrm{ON}}$ as $D \to \infty$. The level of $Y$ stores, for about one lifetime of $Y$, the information that $S_X$ was present recently, so a recently stimulated cell responds faster.

5. For the I1-FFL of Proposition 15.4.3 with $F = 10$, compute $T_{1/2}$ and the speed-up over simple regulation. What condition on $T_{\mathrm{rep}}$ is required, and what goes wrong if it fails badly?

   **Answer** $T_{1/2} = \alpha_Z^{-1}\ln[1/(1 - 0.05)] = 0.0513/\alpha_Z$, against $0.693/\alpha_Z$: $13.5$-fold faster. The formula needs $Z$ to reach $Z_{\mathrm{st}}/2$ before repression sets in, $T_{\mathrm{rep}} \ge 0.0513/\alpha_Z$. If repression comes much later, $Z$ keeps rising toward $\beta_Z/\alpha_Z = 10Z_{\mathrm{st}}$ and overshoots its target several-fold before $Y$ brings it down: the circuit becomes a pulse generator rather than a clean accelerator. Good acceleration needs a fast or low-threshold repressor.

6. Use Proposition 15.4.4 to decide which of the following systems show fold-change detection: (a) $\dot y = u - y$, $\dot z = u/y - z$; (b) $\dot y = u - y$, $\dot z = u - y - z$; (c) $\dot y = u - y$, $\dot z = u - z$.

   **Answer** Test the symmetry $u \to pu$, $y \to py$. (a) $g = u - y$ scales by $p$ and $h = u/y - z$ is invariant: fold-change detection; after a step from $u_0$ to $2u_0$ the transient of $z$ is the same for every $u_0$. (b) $g$ scales, but $h = u - y - z$ becomes $p(u - y) - z$: not invariant. The system adapts perfectly ($z \to 0$ at every steady state), but the size of its transient is proportional to the absolute size of the step, $u_1 - u_0$, not to the ratio. (c) $h = u - z$ is not invariant and the system does not even adapt: $z_{\mathrm{st}} = u$. Adaptation is necessary for fold-change detection, but not sufficient.

7. In a single-input module, the master regulator rises as $X_{\mathrm{st}}(1 - \mathrm{e}^{-t/T})$ with $T = 30\,\mathrm{min}$, and four genes have thresholds $0.2, 0.4, 0.6, 0.8$ of $X_{\mathrm{st}}$. When does each gene switch on? If $X$ stops being produced at $t = 120\,\mathrm{min}$, when does each switch off?

   **Answer** $t_i = -T\ln(1 - K_i)$: $6.7$, $15.3$, $27.5$ and $48.3\,\mathrm{min}$. At $t_1 = 120\,\mathrm{min}$, $X_1 = 1 - \mathrm{e}^{-4} = 0.982$; then $t_i' = 120 + T\ln(0.982/K_i)$: $167.7$, $146.9$, $134.8$ and $126.1\,\mathrm{min}$ for genes $1$ to $4$. On in the order $1, 2, 3, 4$, off in the order $4, 3, 2, 1$: last in, first out.

8. Why are three-node feedback cycles rare in sensory transcription networks, although they occur in synthetic biology (the **repressilator**) and developmental networks contain feedback loops?

   **Answer** A negative feedback cycle of three transcriptional steps is a delayed negative loop that can oscillate ([7.6.33](/7.6.33#sec-33.5)), and a positive cycle (zero or two repressions) can be bistable. A sensory network must make a graded, reversible response to the current environment and return to its original state when the signal disappears; oscillation or locking would make the response depend on phase or history. Developmental networks, by contrast, must make irreversible decisions and keep a memory, for which positive loops are useful ([7.9.16](/7.9.16)); the repressilator was built precisely to oscillate.

9. (Design) You suspect that a C1-FFL with an AND gate controls a gene $Z$ in a bacterium. Design experiments that test (a) the delay at ON steps, (b) the absence of a delay at OFF steps, (c) that the delay is due to $Y$, and (d) the filtering of short pulses.

   **Answer** Fuse the promoter of $Z$ (and, as a control, a simply regulated promoter responding to the same signal) to a fast-folding fluorescent reporter, and measure promoter activity (the time derivative of fluorescence divided by cell density) in a plate reader or microfluidic device with controlled inputs. (a) Apply ON steps of $S_X$ and compare the onset of $Z$ activity with the control; (b) apply OFF steps and check that $Z$ activity stops as fast as the control; (c) delete $Y$ or its binding site in the $Z$ promoter (expect loss of $Z$ expression for an AND gate) and, better, express $Y$ constitutively at its steady-state level before the step (the delay should disappear) or change the $Y$ threshold by mutating its site (the delay should change according to Eq. (15.7)); (d) in a microfluidic device, apply pulses of $S_X$ of increasing duration and find the minimal duration that produces $Z$, which should be close to $T_{\mathrm{ON}}$.

10. A gene is regulated by an activator $X$ ($K_1 = 1$) and a repressor $Y$ ($K_2 = 0.1$) binding independently, with $\beta = 1$ and $\beta' = 0.2$ (Formula 15.1.2). Compute $f$ at $(X, Y) = (10, 0)$, $(10, 1)$ and $(10, 10)$, and describe the logic function it approximates.

    **Answer** $f = (10 + 0.2\cdot10\cdot Y/0.1)/(1 + 10 + Y/0.1 + 10Y/0.1)$. At $Y = 0$: $10/11 = 0.909$. At $Y = 1$: numerator $10 + 20 = 30$, denominator $11 + 10 + 100 = 121$, $f = 0.248$. At $Y = 10$: numerator $10 + 200 = 210$, denominator $11 + 100 + 1000 = 1111$, $f = 0.189$, close to the plateau $\beta' X/K_1/(1 + X/K_1) = 0.2\cdot 10/11 = 0.182$. The function approximates "$X$ AND NOT $Y$" with a leak: high when only $X$ is present, about $\beta'$ when both are, zero without $X$.
