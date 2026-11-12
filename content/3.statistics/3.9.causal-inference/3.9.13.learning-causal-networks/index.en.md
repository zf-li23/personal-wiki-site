---
title: Learning Causal Bayesian Networks
description: Parameter learning in a Bayesian network of known structure (decomposition of the likelihood, maximum likelihood and Dirichlet posteriors for conditional probability tables, bnlearn); what structure learning can identify (Markov equivalence classes and CPDAGs); search-and-score methods (likelihood, AIC and BIC scores, hill climbing); constraint-based methods (the IC and PC algorithms, Meek's orientation rules, a worked five-variable example, G-squared and Fisher-z tests of conditional independence); Gaussian graphical models, expressive power of directed and undirected graphs, and advanced and current topics.
---

The methods of [3.9.12](/3.9.12) take the causal diagram as given. When it comes from established science, as in an epidemiological study whose variables have a well-understood temporal and biological order, that is reasonable. In many other problems, such as the regulatory relations among thousands of genes or the dependencies among many economic indicators, the graph is unknown and must be learned from data. This chapter treats both halves of learning a Bayesian network: estimating its parameters when the structure is known, which is a standard likelihood problem, and estimating the structure itself, *structure learning*, which is much harder and only partly possible. Under the assumptions of [3.9.11](/3.9.11), Markov compatibility and faithfulness, the observational distribution determines the graph only up to its Markov equivalence class, so the output of structure learning is in general a partially directed graph. The algorithms are implemented in the R package `bnlearn`, which we use throughout (the Bayes Net Toolbox offers similar functions in MATLAB). [7.9.11](/7.9.11) applies the same ideas to gene regulatory networks.

## 13.1. Parameter Learning

### 13.1.1. The Likelihood Factorizes

Suppose the DAG $G$ is known and we observe $M$ independent cases $\boldsymbol{x}^{(1)}, \dots, \boldsymbol{x}^{(M)}$ in which every node is observed; write $D$ for the data, $\pi_i$ for the parents of node $X_i$, and $\boldsymbol{\phi}_i$ for the parameters of its conditional distribution (CPD) $\mathbb{P}(x_i \mid \pi_i, \boldsymbol{\phi}_i)$. As with any statistical model there are two approaches.

- *Bayesian*: treat $\boldsymbol{\phi}$ as random and compute its posterior distribution $p(\boldsymbol{\phi} \mid D)$.
- *Frequentist*: treat $\boldsymbol{\phi}$ as an unknown constant and estimate it, for example by **maximum likelihood estimation** or by penalized likelihood, $\boldsymbol{\phi}^* = \arg\max_{\boldsymbol{\phi}} \{\log \mathbb{P}(D \mid \boldsymbol{\phi}) - \lambda C(\boldsymbol{\phi})\}$, where $C$ measures complexity.

By the factorization (11.2), the log-likelihood is

$$
\ell(\boldsymbol{\phi}) = \sum_{m=1}^M \log \mathbb{P}(\boldsymbol{x}^{(m)} \mid \boldsymbol{\phi}) = \sum_{i=1}^n \underbrace{\sum_{m=1}^M \log \mathbb{P}\bigl(x_i^{(m)} \mid \pi_i^{(m)}, \boldsymbol{\phi}_i\bigr)}_{\ell_i(\boldsymbol{\phi}_i)}.
\tag{13.1}
$$
If the parameters of different CPDs are variationally independent (global parameter independence), the log-likelihood is a sum of terms each involving one node and its parents, and it can be maximized node by node: estimating a Bayesian network reduces to $n$ separate regressions of a node on its parents. The same holds for the posterior if the prior factorizes over the nodes.

### 13.1.2. Conditional Probability Tables

For discrete variables, the CPD of node $i$ is a table: let $X_i$ take values $k = 1, \dots, r_i$ and let $j = 1, \dots, q_i$ index the configurations of its parents, and set $\theta_{ijk} = \mathbb{P}(X_i = k \mid \pi_i = j)$, with $\sum_k \theta_{ijk} = 1$. The sufficient statistics are the counts of family configurations, $N_{ijk} = \#\{m : x_i^{(m)} = k, \pi_i^{(m)} = j\}$, and

$$
\ell(\boldsymbol{\theta}) = \sum_{i=1}^n \sum_{j=1}^{q_i} \sum_{k=1}^{r_i} N_{ijk} \log \theta_{ijk}.
$$

**Theorem 13.1.1 (Maximum Likelihood for Multinomial CPDs)** With complete data, the maximum likelihood estimate of a conditional probability table is the table of observed conditional frequencies,

$$
\hat\theta_{ijk} = \frac{N_{ijk}}{N_{ij}}, \qquad N_{ij} = \sum_{k=1}^{r_i} N_{ijk}.
$$

**Proof** The log-likelihood separates over $(i, j)$, and each part $\sum_k N_{ijk}\log\theta_{ijk}$ is the log-likelihood of a **multinomial distribution**. Using a **Lagrange multiplier** for the constraint $\sum_k \theta_{ijk} = 1$, set the derivative of $\sum_k N_{ijk}\log\theta_{ijk} - \lambda(\sum_k \theta_{ijk} - 1)$ to zero: $N_{ijk}/\theta_{ijk} = \lambda$, so $\theta_{ijk} = N_{ijk}/\lambda$, and the constraint gives $\lambda = N_{ij}$. The function is concave in $\boldsymbol{\theta}$, so this is the maximum. $\square$

With a **Dirichlet distribution** $\mathrm{Dir}(\alpha_{ij1}, \dots, \alpha_{ijr_i})$ as prior for each row of each table, independent across rows, the posterior is $\mathrm{Dir}(\alpha_{ij1} + N_{ij1}, \dots, \alpha_{ijr_i} + N_{ijr_i})$ by the Dirichlet–multinomial conjugacy of [3.7.3](/3.7.3), with posterior mean $(N_{ijk} + \alpha_{ijk})/(N_{ij} + \alpha_{ij})$, $\alpha_{ij} = \sum_k \alpha_{ijk}$. The prior counts smooth the estimates of rows with few observations, which matters because the number of parent configurations $q_i$ grows exponentially with the number of parents.

**Example 13.1.1 (The Sprinkler Network in `bnlearn`)** The structure is set by listing its arcs, and `bn.fit` estimates the tables from a data frame `data` with the five variables as factors. The DAG must be fully directed; in practice it often comes from a structure learning step.

```r
library(bnlearn)
dag <- empty.graph(nodes = c("Season", "Sprinkler", "Rain", "Wet", "Slippery"))
arc.set <- matrix(c("Season", "Sprinkler",
                    "Season", "Rain",
                    "Sprinkler", "Wet",
                    "Rain", "Wet",
                    "Wet", "Slippery"),
                  byrow = TRUE, ncol = 2,
                  dimnames = list(NULL, c("from", "to")))
arcs(dag) <- arc.set
plot(dag)
fitted <- bn.fit(dag, data, method = "mle")
fitted$Wet   # the table P(Wet | Sprinkler, Rain)
```

`method = "bayes"` replaces the maximum likelihood estimates by posterior means under a uniform Dirichlet prior with a chosen imaginary sample size.

:::

## 13.2. What Structure Learning Can Identify

Learning the structure is a model selection problem over DAGs, and it is harder than parameter learning for two reasons. The space is enormous: the number of DAGs on $n$ labeled nodes is $1, 3, 25, 543, 29281$ for $n = 1, \dots, 5$ and grows superexponentially, and finding the highest-scoring DAG is **NP-hard** (Chickering 1996). And the target is only partly identifiable. By Theorem 11.3.2, two DAGs are Markov equivalent if and only if they have the same skeleton and the same v-structures; $X \to Y \to Z$, $X \leftarrow Y \leftarrow Z$ and $X \leftarrow Y \to Z$ encode the same independencies and cannot be distinguished by observational data. A v-structure $X \to Y \leftarrow Z$, by contrast, has a unique statistical signature ($X \perp Z$, but not given $Y$), so some arrow directions can be inferred from passive observation.

**Definition 13.2.1 (Partially Directed Acyclic Graph)** A **partially directed acyclic graph** (PDAG) is a graph with both directed and undirected edges and no directed cycle. The **completed partially directed acyclic graph** (CPDAG, essential graph) of a Markov equivalence class of DAGs has the common skeleton of the class, a directed edge $a \to b$ wherever all DAGs in the class contain $a \to b$ (a compelled edge), and an undirected edge $a - b$ wherever some DAGs in the class contain $a \to b$ and others $b \to a$.

Every DAG obtained from a CPDAG by orienting its undirected edges without creating a new v-structure or a directed cycle belongs to the class. The CPDAG is therefore the most that observational data can reveal, under Markov compatibility and faithfulness. Distinguishing between members of an equivalence class requires interventions or experiments (setting $Y$ and observing whether $X$ changes distinguishes $X \to Y$ from $Y \to X$), or background knowledge such as a temporal order. There are three families of algorithms.

| Family | Idea | Example |
|---|---|---|
| search-and-score | define a score of model quality and search for a graph that maximizes it | hill climbing |
| constraint-based | test conditional independencies and construct a graph consistent with the results | IC, PC |
| hybrid | restrict the search space by tests, then search and score | MMHC (Tsamardinos et al. 2006) |

## 13.3. Search-and-Score Methods

### 13.3.1. Scores

**Definition 13.3.1 (Search-and-Score Method)** A **score-based method** (search-and-score method) of structure learning defines a scoring function $S(G; D)$ that measures how well a DAG $G$ fits the data $D$, and uses a search algorithm to find a graph with a (locally) maximal score.

The Bayesian version treats the graph as random and computes $\mathbb{P}(G \mid D) \propto \mathbb{P}(D \mid G)\,\mathbb{P}(G)$, where the marginal likelihood $\mathbb{P}(D \mid G) = \int \mathbb{P}(D \mid \boldsymbol{\phi}, G)\,p(\boldsymbol{\phi} \mid G)\,\mathrm{d}\boldsymbol{\phi}$ has a closed form for Dirichlet priors (the BDe score). The frequentist version maximizes a penalized likelihood,

$$
G^* = \arg\max_G \bigl\{\log \mathbb{P}(D \mid \hat{\boldsymbol{\phi}}_G, G) - \lambda\,C(G)\bigr\},
$$
with $C(G)$ the number of free parameters. The maximized log-likelihood alone ($\lambda = 0$) is a poor score: adding an arc never decreases it, because the model with the arc contains the model without it, so it always prefers a nearly complete graph. The penalties of the **Akaike information criterion** and the **Bayesian information criterion**, defined in [3.4.11](/3.4.11) and compared in [3.7.8](/3.7.8),

$$
\mathrm{AIC} = -2\log \mathbb{P}(D \mid \hat{\boldsymbol{\phi}}) + 2k, \qquad \mathrm{BIC} = -2\log \mathbb{P}(D \mid \hat{\boldsymbol{\phi}}) + k\log M,
$$
correct this ($k$ is the number of free parameters, $M$ the sample size; smaller is better, and `bnlearn` reports $-\mathrm{BIC}/2$ so that larger is better). They answer different questions: BIC approximates $-2\log \mathbb{P}(D \mid G)$ up to terms of lower order, which is where the prior has gone, and is consistent for selecting the true graph when one of the candidates is true; AIC, like cross-validation, aims at the model that predicts best and tends to keep extra arcs. Both are decomposable, a sum of terms for each node and its parents as in (13.1), so a local change of the graph changes only one or two terms; and both are score equivalent, giving the same value to Markov equivalent DAGs.

### 13.3.2. Hill Climbing

The search is usually greedy. **Hill climbing** ([4.5.2](/4.5.2)) starts from an initial graph, typically the empty one, and repeatedly applies the single arc addition, deletion or reversal that improves the score most, as long as the result is acyclic, until no move improves it. Because the scores are decomposable, each candidate move is evaluated by recomputing one or two local terms.

```r
res <- hc(data, score = "loglik")   # log-likelihood: tends to a dense graph
res <- hc(data, score = "bic")      # also "aic"
plot(res)
data2 <- data[, c(2, 1, 3, 4, 5)]   # permute the columns
plot(hc(data2, score = "bic"))
```

Hill climbing returns a single DAG, not an equivalence class, and the direction of its arcs within the class is arbitrary, decided by the order in which equally good moves are tried. Permuting the columns of the data can therefore change the output; on samples from the sprinkler network it can even lead the search to a local optimum with a spurious arc and a wrong v-structure at the season node. The constraint-based `pc.stable` (Section 13.4) returns the same CPDAG whatever the order of the columns. Random restarts and tabu lists (`tabu` in `bnlearn`) reduce the risk of poor local optima.

| | Search-and-score |
|---|---|
| advantages | easy to incorporate prior knowledge (a prior $\mathbb{P}(G)$, required or forbidden arcs); returns a fully directed DAG of the equivalence class directly; uses all the data in each comparison |
| disadvantages | usually stops at a local optimum; high computational cost when the number of variables, and hence the search space, is large |

## 13.4. Constraint-Based Methods

### 13.4.1. From Independencies to Graphs

**Definition 13.4.1 (Constraint-Based Method)** A **constraint-based method** of structure learning tests conditional independencies $X_i \perp X_j \mid S$ in the data and constructs a graph (an equivalence class) consistent with the results.

It has two parts: conditional independence tests connect data with probability, and the algorithm connects probability with the graph, assuming that all conditional independencies are correctly revealed by the tests. Under Markov compatibility and faithfulness, $I(G) = I(\mathbb{P})$, and two facts drive the algorithms: two nodes are adjacent if and only if no set d-separates them; and if $a$ and $b$ are not adjacent but have a common neighbor $c$, then $a \to c \leftarrow b$ is a v-structure if and only if $c$ is not in any (equivalently, in the found) set that separates $a$ and $b$.

**Algorithm 13.4.1 (IC Algorithm)** The **IC algorithm** (inductive causation; Verma and Pearl 1990) takes a distribution, or the conditional independencies estimated from data, on $n$ variables.

1. *Skeleton.* For each pair $(a, b)$, search for a set $S_{ab}$ such that $a \perp b \mid S_{ab}$. Connect $a - b$ if and only if no such set is found.
2. *v-Structures.* For each pair of nonadjacent nodes $a$, $b$ with a common neighbor $c$, orient $a \to c \leftarrow b$ if $c \notin S_{ab}$.
3. *Propagation.* Orient as many of the remaining undirected edges as possible without creating a new v-structure or a directed cycle, by repeatedly applying Meek's rules.

The output is the CPDAG of the equivalence class of the true DAG. Step 1 may examine, for each of the $n(n - 1)/2$ pairs, all $2^{n-2}$ subsets of the remaining variables, so the worst-case complexity is $O(n^2 2^{n-2})$.

**Definition 13.4.2 (Meek Rules)** In a PDAG containing all v-structures, the **Meek rules** orient an undirected edge $b - c$ as follows:

1. if $a \to b - c$ and $a$, $c$ are not adjacent, orient $b \to c$ (otherwise $a \to b \leftarrow c$ would be a new v-structure);
2. if $b \to a \to c$ and $b - c$, orient $b \to c$ (otherwise $b \to a \to c \to b$ would be a directed cycle);
3. if $b - a_1 \to c$ and $b - a_2 \to c$ with $a_1$, $a_2$ not adjacent, and $b - c$, orient $b \to c$.

Meek (1995) proved that applying rules 1–3 until none applies yields exactly the CPDAG: they are sound (every edge they orient is compelled) and complete (every compelled edge gets oriented). A fourth rule is needed only when background knowledge forces additional orientations.

**Algorithm 13.4.2 (PC Algorithm)** The **PC algorithm** (Spirtes and Glymour 1991) is the IC algorithm with a more economical search for separating sets in step 1. Start from the complete undirected graph. For $\ell = 0, 1, 2, \dots$: for each pair $a - b$ still adjacent, test $a \perp b \mid S$ for all subsets $S$ of size $\ell$ of the current neighbors of $a$ (excluding $b$), and of $b$; if a test accepts independence, delete the edge and record $S_{ab} = S$. Stop when no node has more than $\ell$ neighbors besides the one being tested. Then orient as in steps 2 and 3 of the IC algorithm.

Testing small conditioning sets first, and only among current neighbors, is justified because if $a$ and $b$ are d-separated by some set, they are d-separated by a subset of the parents of $a$ or of the parents of $b$, all of which remain neighbors. The number of tests is polynomial in $n$ when the maximum degree of the true graph is bounded, which makes PC practical for hundreds of variables in sparse graphs. Small conditioning sets also mean more reliable tests. The order-independent variant PC-stable (Colombo and Maathuis 2014) fixes the neighbor sets at the start of each level $\ell$, so that the output does not depend on the order of the variables.

### 13.4.2. A Worked Example

**Example 13.4.1 (PC on Five Variables)** Suppose the data come from the DAG with arrows $X_1 \to X_2$, $X_1 \to X_3$, $X_2 \to X_4$, $X_3 \to X_4$, $X_3 \to X_5$, $X_4 \to X_5$, and the sample is large enough to reveal all conditional independencies exactly.

![The PC algorithm on five variables: the true DAG, the skeleton found in step 1, the v-structure found in step 2 (red), and the CPDAG after Meek's rules (blue arcs oriented in step 3).](./plots/pc_steps.py)

*Step 1: skeleton.* For each of the $10$ pairs we test marginal independence first, then conditional independence given sets of increasing size, stopping at the first set that separates the pair (for $X_1$ and $X_2$, up to the $8$ subsets of $\{X_3, X_4, X_5\}$). The results:

| Pair | Result | $S_{ab}$ |
|---|---|---|
| $X_1, X_2$; $X_1, X_3$; $X_2, X_4$; $X_3, X_4$; $X_3, X_5$; $X_4, X_5$ | dependent given every set | adjacent |
| $X_2, X_3$ | $X_2 \perp X_3 \mid X_1$ | $\{X_1\}$ |
| $X_1, X_4$ | $X_1 \perp X_4 \mid \{X_2, X_3\}$ | $\{X_2, X_3\}$ |
| $X_1, X_5$ | $X_1 \perp X_5 \mid \{X_3, X_4\}$ | $\{X_3, X_4\}$ |
| $X_2, X_5$ | $X_2 \perp X_5 \mid \{X_3, X_4\}$ | $\{X_3, X_4\}$ |

The pair $X_2, X_5$ is not separated by $\{X_1, X_4\}$: conditioning on the collider $X_4$ opens $X_2 \to X_4 \leftarrow X_3 \to X_5$, which only $X_3$ blocks. When several sets separate a pair, as $\{X_3, X_4\}$ and $\{X_2, X_3\}$ both separate $X_1$ and $X_5$, the algorithm keeps the first one found; it need not find all of them. The skeleton has the six edges of the true DAG.

*Step 2: v-structures.* The nonadjacent pairs with common neighbors are: $X_2, X_3$ (common neighbors $X_1$ and $X_4$), $X_1, X_4$ (common neighbors $X_2$, $X_3$), $X_1, X_5$ (common neighbor $X_3$) and $X_2, X_5$ (common neighbor $X_4$). Only $X_4 \notin S_{23} = \{X_1\}$ gives a v-structure: $X_2 \to X_4 \leftarrow X_3$. The other common neighbors belong to the separating sets ($X_1 \in S_{23}$; $X_2, X_3 \in S_{14}$; $X_3 \in S_{15}$; $X_4 \in S_{25}$).

*Step 3: Meek's rules.* Rule 1 applied to $X_2 \to X_4 - X_5$, with $X_2$ and $X_5$ nonadjacent, orients $X_4 \to X_5$ (no new v-structure). Rule 2 applied to $X_3 \to X_4 \to X_5$ and $X_3 - X_5$ orients $X_3 \to X_5$ (no directed cycle). No rule applies to $X_1 - X_2$ and $X_1 - X_3$: either orientation that avoids the v-structure $X_2 \to X_1 \leftarrow X_3$ is possible.

The result is the CPDAG with $X_1 - X_2$, $X_1 - X_3$ undirected and the other four edges directed as in the true DAG. The equivalence class contains three DAGs ($X_1$ as the source; $X_2 \to X_1 \to X_3$; $X_3 \to X_1 \to X_2$). To decide whether the season-like variable $X_1$ is a cause of $X_2$ or an effect, an intervention on $X_1$ or $X_2$, or background knowledge, is needed.

:::

### 13.4.3. Tests of Conditional Independence

An independence test for $X \perp Y \mid S$ tests $H_0\colon \mathbb{P}(x, y \mid s) = \mathbb{P}(x \mid s)\,\mathbb{P}(y \mid s)$. A general choice is the **likelihood ratio test** of [3.2.5](/3.2.5): under $H_0$ the statistic $G^2 = 2\log\Lambda$ is asymptotically $\chi^2$ with degrees of freedom equal to the difference between the dimensions of the alternative and the null models.

**Theorem 13.4.1 (Tests for Discrete Data)** Let $X_i$, $X_j$ and a vector $\boldsymbol{X}_k$ be discrete, with $\#(X)$ the number of categories of $X$, and let $N_{abc}$ be the number of the $N$ cases with $X_i = a$, $X_j = b$, $\boldsymbol{X}_k = c$ (with marginal counts $N_{ac}$, $N_{bc}$, $N_c$). Under $H_0\colon X_i \perp X_j \mid \boldsymbol{X}_k$,

$$
G^2 = 2\sum_{a, b, c} N_{abc}\log\frac{N_{abc}N_c}{N_{ac}N_{bc}} \xrightarrow{d} \chi^2_{\mathrm{df}}, \qquad \mathrm{df} = (\#(X_i) - 1)(\#(X_j) - 1)\prod_{X \in \boldsymbol{X}_k}\#(X),
$$
as $N \to \infty$.

The statistic equals $2N$ times the empirical conditional **mutual information** of $X_i$ and $X_j$ given $\boldsymbol{X}_k$, which is why `bnlearn` calls the test `"mi"`. The degrees of freedom multiply with every conditioning variable, so the test needs many observations per cell; with small samples, a large conditioning set means low power, and an edge is then wrongly removed. (In practice the degrees of freedom are often reduced by the number of empty cells.)

**Theorem 13.4.2 (Tests for Gaussian Data)** If the variables are jointly normal, $X_i \perp X_j \mid \boldsymbol{X}_k$ is equivalent to a zero **partial correlation** $\rho_{ij \cdot k}$. With $\hat\rho_{ij \cdot k}$ the sample partial correlation from $N$ observations,

$$
\sqrt{N - \lvert k\rvert - 3}\;\cdot\;\frac12\log\frac{1 + \hat\rho_{ij \cdot k}}{1 - \hat\rho_{ij \cdot k}} \xrightarrow{d} \mathcal{N}(0, 1) \quad\text{under } H_0,
$$
so its square tends to $\chi^2_1$; $\lvert k\rvert$ is the number of conditioning variables.

The transformation is the **Fisher z-transformation** of the partial correlation. The sample partial correlation is computed from the inverse $P$ of the sample correlation matrix of $(X_i, X_j, \boldsymbol{X}_k)$ as $\hat\rho_{ij \cdot k} = -P_{ij}/\sqrt{P_{ii}P_{jj}}$ (Section 13.5.1).

```r
res <- pc.stable(data, test = "mi")   # PC-stable with mutual information (G-squared) tests
plot(res)                             # the PDAG: undirected edges have no arrowheads
res2 <- pc.stable(data[, c(2, 1, 3, 4, 5)], test = "mi")   # same CPDAG
```

On sprinkler data, `pc.stable` recovers the skeleton, the v-structure Sprinkler $\to$ Wet $\leftarrow$ Rain, the compelled arc Wet $\to$ Slippery, and leaves Season $-$ Sprinkler and Season $-$ Rain undirected, exactly the CPDAG of the true network. To obtain a causal DAG, the undirected edges are oriented by background knowledge (the season is not caused by the sprinkler), for example with `set.arc`.

![Structure recovery by the PC algorithm with Fisher-z tests at level 0.05, for data simulated from a linear Gaussian structural model with the DAG of Example 13.4.1. Left: proportion of 200 replications in which the skeleton and the full CPDAG are recovered exactly. Right: mean number of wrong edges in the skeleton. Simulated data.](./plots/pc_simulation.py)

The simulation shows how much data even five variables need. Errors come from both kinds of test error: with small samples, weak dependencies go undetected and true edges are deleted; at every sample size, a true independence is rejected with probability about $0.05$, which keeps a spurious edge. Orientation errors follow from skeleton errors, because a single wrong separating set changes the v-structures, and Meek's rules then propagate the mistake to other edges. In the chosen model, two paths from $X_1$ to $X_4$ with effects of opposite sign nearly cancel, so the distribution is close to unfaithful and recovery is slow; with exactly cancelling paths it would fail at every sample size.

| | Constraint-based |
|---|---|
| advantages | scales to many variables in sparse graphs; each decision rests on an interpretable test; returns the equivalence class, the honest output of observational data |
| disadvantages | reliable tests are hard to make, especially with small samples (false positives and false negatives); one wrong test can cause several errors in the output, so the method is not very robust to noise; relies on faithfulness |

## 13.5. Discussion and Further Methods

### 13.5.1. Gaussian Graphical Models

**Definition 13.5.1 (Gaussian Graphical Model)** Let $\boldsymbol{X} = (X_1, \dots, X_p)$ be multivariate normal with positive definite covariance matrix $\Sigma$. The matrix $\Omega = \Sigma^{-1}$ is the **precision matrix** (concentration matrix). The **Gaussian graphical model** of $\boldsymbol{X}$ is the undirected graph on $\{1, \dots, p\}$ with an edge $i - j$ if and only if $\Omega_{ij} \neq 0$.

**Theorem 13.5.1** For $\boldsymbol{X} \sim \mathcal{N}_p(\boldsymbol{\mu}, \Sigma)$ and $i \neq j$, $X_i \perp X_j \mid \boldsymbol{X}_{-\{i,j\}}$ if and only if $\Omega_{ij} = 0$. More precisely, the partial correlation of $X_i$ and $X_j$ given all other variables is $-\Omega_{ij}/\sqrt{\Omega_{ii}\Omega_{jj}}$.

**Proof** By the conditional distribution of the **multivariate normal distribution** ([3.1.15](/3.1.15)), the conditional covariance matrix of $(X_i, X_j)$ given the rest is the inverse of the $2 \times 2$ submatrix of $\Omega$ with rows and columns $i, j$ (a Schur complement identity). The inverse of $\begin{bmatrix}\Omega_{ii} & \Omega_{ij}\\ \Omega_{ij} & \Omega_{jj}\end{bmatrix}$ has off-diagonal entry $-\Omega_{ij}/(\Omega_{ii}\Omega_{jj} - \Omega_{ij}^2)$ and diagonal entries $\Omega_{jj}/(\cdot)$, $\Omega_{ii}/(\cdot)$, so the conditional correlation is $-\Omega_{ij}/\sqrt{\Omega_{ii}\Omega_{jj}}$, and for normal variables zero conditional correlation is conditional independence. $\square$

The zeros of the precision matrix encode independence given all other variables, which is different from marginal independence. In the chain $X_1 \to X_2 \to X_3$ the precision matrix is tridiagonal ($\Omega_{13} = 0$) although $X_1$ and $X_3$ are correlated. In the collider $X_1 \to X_3 \leftarrow X_2$ we have $X_1 \perp X_2$ marginally, yet $\Omega_{12} \neq 0$, because they are dependent given $X_3$. For a distribution generated by a DAG and faithful to it, the Gaussian graphical model is the moral graph of the DAG: connect the parents of every common child, then drop the directions. With more variables than observations, $\Omega$ is estimated by the penalized likelihood of the **graphical lasso** ([7.9.11](/7.9.11)).

### 13.5.2. Expressive Power

Directed and undirected graphs cannot always be converted into each other without losing independencies. No DAG on four variables represents exactly the independencies $X \perp Y \mid \{W, Z\}$ and $W \perp Z \mid \{X, Y\}$, those of the undirected four-cycle $X - W - Y - Z - X$: any orientation of the cycle without directed cycles has a collider, which spoils one of the two statements. Conversely, no undirected graph represents exactly the independencies of the v-structure $X \to Z \leftarrow Y$, namely $X \perp Y$ but $X \not\perp Y \mid Z$: an undirected graph either connects $X$ and $Y$ through $Z$, so that they are marginally dependent, or not at all. This asymmetry is why causal discovery works with DAGs and v-structures.

### 13.5.3. Advanced Methods

Hybrid methods combine the two families. Max-min hill climbing (MMHC; Tsamardinos, Brown and Aliferis 2006) first finds, for each variable, a set of candidate parents and children by conditional independence tests, then runs hill climbing restricted to arcs among these candidates; it is available as `mmhc` in `bnlearn`.

Decomposition and local learning reduce a large problem to small ones. The recursive method of Xie and Geng (2008) decomposes the problem of learning a large DAG, using an undirected independence graph, into problems of learning two smaller graphs, recursively, learns the local skeletons of the small problems and combines them, then orients the result; it is a divide-and-conquer approach in which the same conditional independence test is carried out on smaller conditioning sets. When only the causes of a single target variable $T$ are of interest, learning the whole network is unnecessary. The PCD-by-PCD algorithm (Zhou, Wang, Yin and Geng 2010) finds the set $\mathrm{PCD}(T)$ of parents, children and descendants of $T$, then the PCD sets of those variables, and so on outward; an edge $x - z$ is created when each is in the other's PCD set, v-structures found among the explored nodes orient edges locally, and the search stops as soon as all edges at $T$ are oriented. Experiments that manipulate some variables can be designed to orient the remaining undirected edges of a CPDAG with as few interventions as possible (He and Geng 2008).

Current research topics include causal graphs for time series (dynamic Bayesian networks), tests of conditional independence for non-Gaussian continuous data (kernel methods), the stability of learned structures under resampling, latent variables (the FCI algorithm returns a partial ancestral graph instead of a CPDAG), and incorporating prior or domain knowledge into constraint-based methods. Learning from a mixture of observational and interventional data identifies more than the equivalence class.

To evaluate an algorithm, a learned structure is compared with the true one, in simulations or on benchmark networks such as ALARM (a monitoring network for intensive care with 37 nodes and 46 arcs; Beinlich et al. 1989), by the numbers of extra and missing edges and by the *structural Hamming distance* (SHD): the number of edge insertions, deletions and reversals (or orientation changes) needed to turn the learned CPDAG into the true one. In Example 13.4.1, a CPDAG that is correct except for an extra edge $X_2 - X_3$ has SHD $1$.

## Summary

- Parameter learning with a known DAG: the log-likelihood decomposes into one term per family (Eq. (13.1)); for discrete CPDs the maximum likelihood estimates are the conditional frequencies $N_{ijk}/N_{ij}$ (Theorem 13.1.1), and Dirichlet priors give conjugate posteriors. In R: `empty.graph`, `arcs<-`, `bn.fit`.
- Identifiability: data determine at most the Markov equivalence class (same skeleton and v-structures), represented by the CPDAG (Definition 13.2.1); interventions or background knowledge are needed to orient the remaining edges.
- Structure learning:

  | | Search-and-score | Constraint-based |
  |---|---|---|
  | input | a score: log-likelihood (overfits), AIC, BIC, Bayesian marginal likelihood | conditional independence tests: $G^2$ / mutual information, Fisher $z$ |
  | algorithm | hill climbing over arc additions, deletions and reversals | IC / PC: skeleton, v-structures, Meek rules |
  | output | one DAG (a local optimum) | the CPDAG |
  | weakness | local optima, cost | test errors propagate; faithfulness |

- PC in three steps (Algorithm 13.4.2, Example 13.4.1): delete $a - b$ when some set $S$ makes them independent, testing sets of increasing size among current neighbors; orient $a \to c \leftarrow b$ for nonadjacent $a, b$ with common neighbor $c \notin S_{ab}$; orient further edges so as to create no new v-structures and no directed cycles (Definition 13.4.2). At least $\binom{n}{2}$ tests are needed (one for each pair); IC may need $O(n^2 2^{n-2})$.
- Gaussian graphical models: $\Omega_{ij} = 0$ if and only if $X_i \perp X_j$ given all others (Theorem 13.5.1); the undirected graph is the moral graph of the DAG. Directed and undirected graphs have different expressive power.
- Further methods: MMHC, recursive decomposition, local PCD-by-PCD learning, intervention design; evaluation by SHD on benchmarks such as ALARM.

## Questions

1. You learn the structure of a DAG on five variables $X, Y, Z, R, W$ with a constraint-based method. What is the smallest number of conditional independence tests you must carry out?

   **Answer** Every one of the $\binom{5}{2} = 10$ pairs must be tested at least once, with the empty conditioning set first, so at least $10$ tests are needed. The minimum is attained only when every marginal test already accepts independence (the empty graph). Otherwise more tests follow: a nonadjacent pair that is marginally dependent is tested until a separating set is found, and an adjacent pair until all candidate conditioning sets are exhausted.
2. Tests on data for $X, Y, Z, R, W$ give: $X \perp Y$; $X \perp R \mid Z$; $X \perp W \mid Z$; $Y \perp R \mid Z$; $Y \perp W \mid Z$; and no conditional independence for the other pairs. Learn the structure step by step. Which edges remain undirected, and how could they be oriented?

   **Answer** Skeleton: the pairs not separated are $X - Z$, $Y - Z$, $Z - R$, $Z - W$, $R - W$. Separating sets: $S_{XY} = \varnothing$, $S_{XR} = S_{XW} = S_{YR} = S_{YW} = \{Z\}$. v-Structures: $X$ and $Y$ are nonadjacent with common neighbor $Z \notin S_{XY}$, so $X \to Z \leftarrow Y$; the other nonadjacent pairs have $Z$ as common neighbor and $Z$ in their separating set, so no further v-structure. Meek's rule 1: $X \to Z - R$ with $X$, $R$ nonadjacent gives $Z \to R$; likewise $Z \to W$. The edge $R - W$ stays undirected: $Z \to R \to W$ and $Z \to W \to R$ are both acyclic and create no new v-structure (since $Z$ is adjacent to both $R$ and $W$). It can be oriented by an experiment that sets $R$ (if the distribution of $W$ changes, $R \to W$) or by background knowledge such as the time order of measurement.
3. Derive the maximum likelihood estimate of $\mathbb{P}(\text{Wet} \mid \text{Sprinkler}, \text{Rain})$ from complete data, and its posterior mean under independent $\mathrm{Dir}(1, 1)$ priors for each parent configuration.

   **Answer** By Theorem 13.1.1, $\hat{\mathbb{P}}(\text{Wet} = k \mid s, r) = N_{s r k}/N_{s r}$, the proportion of wet pavements among the cases with sprinkler state $s$ and rain state $r$. With a $\mathrm{Dir}(1, 1) = \mathrm{Beta}(1, 1)$ prior for each of the four rows, the posterior is $\mathrm{Beta}(1 + N_{sr,\text{wet}}, 1 + N_{sr,\text{dry}})$ and the posterior mean $(N_{sr,\text{wet}} + 1)/(N_{sr} + 2)$, the Laplace estimate, which stays strictly between $0$ and $1$ even for configurations never observed.
4. Why does hill climbing with the score $\log \mathbb{P}(D \mid \hat{\boldsymbol{\phi}}_G, G)$ tend to return an almost complete graph? How do AIC and BIC change this, and which of the two is consistent?

   **Answer** Adding an arc $a \to b$ enlarges the family of CPDs of $b$ (the old model is the special case in which $b$ does not depend on $a$), so the maximized likelihood cannot decrease; with finite data it almost always increases slightly, so every acyclic addition is accepted. AIC subtracts $2$ and BIC $\log M$ per extra parameter (on the $-2\log$ scale), so an arc is added only if it improves the fit by more than its cost. BIC's penalty grows with $M$ and it selects the true equivalence class with probability tending to one; AIC's penalty is fixed, and it keeps spurious arcs with positive probability even asymptotically.
5. For two binary variables $X_i$, $X_j$ and a conditioning set of two variables with three categories each, how many degrees of freedom does the $G^2$ test have? What does this imply for small samples?

   **Answer** $\mathrm{df} = (2 - 1)(2 - 1)\cdot 3 \cdot 3 = 9$. The data are split into $9$ strata, each with a $2 \times 2$ table; with, say, $100$ observations the tables are sparse, the $\chi^2$ approximation is poor and the power is low. Low power means that dependence is not detected, so true edges are deleted; this is one reason why PC tests small conditioning sets first.
6. Give the CPDAG of the DAG $A \to B$, $B \to C$, $A \to C$, $C \to D$, and of the DAG $A \to C$, $B \to C$, $C \to D$. How many DAGs does each equivalence class contain?

   **Answer** The first DAG has no v-structure ($A$, $B$, $C$ form a triangle, and $D$ has the single parent $C$), so its CPDAG is fully undirected: $A - B$, $B - C$, $A - C$, $C - D$. Its members are the acyclic orientations without a v-structure. If $C \to D$, any of the $3! = 6$ acyclic orientations of the triangle works. If $D \to C$, then $C$ may have no other parent ($A$ and $B$ are not adjacent to $D$), so $C \to A$ and $C \to B$, and $A - B$ can go either way: $2$ more. The class has $8$ DAGs. The second DAG has the v-structure $A \to C \leftarrow B$, and Meek's rule 1 then orients $C \to D$, so the CPDAG is the DAG itself and the class has one member.
7. Let $X_1 \to X_2 \to X_3$ with $X_1 \sim \mathcal{N}(0, 1)$, $X_2 = X_1 + \varepsilon_2$, $X_3 = X_2 + \varepsilon_3$, $\varepsilon_2, \varepsilon_3 \sim \mathcal{N}(0, 1)$ independent. Compute $\Sigma$ and $\Omega = \Sigma^{-1}$ and read off the Gaussian graphical model.

   **Answer** $\operatorname{Var}(X_1) = 1$, $\operatorname{Var}(X_2) = 2$, $\operatorname{Var}(X_3) = 3$, $\operatorname{Cov}(X_1, X_2) = \operatorname{Cov}(X_1, X_3) = 1$, $\operatorname{Cov}(X_2, X_3) = 2$, so $\Sigma = \begin{bmatrix}1 & 1 & 1\\ 1 & 2 & 2\\ 1 & 2 & 3\end{bmatrix}$ and $\Omega = \begin{bmatrix}2 & -1 & 0\\ -1 & 2 & -1\\ 0 & -1 & 1\end{bmatrix}$ (check: $\Sigma\Omega = I_3$). The graphical model is the undirected chain $X_1 - X_2 - X_3$: $\Omega_{13} = 0$ expresses $X_1 \perp X_3 \mid X_2$, although $\operatorname{Corr}(X_1, X_3) = 1/\sqrt 3 \neq 0$.
8. A learned CPDAG for Example 13.4.1 has all edges correct except that $X_3 \to X_5$ is missing and $X_1 - X_2$ is oriented $X_1 \to X_2$. What is its structural Hamming distance from the true CPDAG?

   **Answer** One deletion has to be undone (insert $X_3 \to X_5$) and one orientation changed ($X_1 \to X_2$ back to $X_1 - X_2$), so the SHD is $2$. Note that the missing edge would in practice also change other orientations: without $X_3 - X_5$, rule 2 no longer applies, and the PC output would differ in more places.
