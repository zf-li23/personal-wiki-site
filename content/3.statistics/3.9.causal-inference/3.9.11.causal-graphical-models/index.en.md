---
title: "Causal Graphical Models: Pearl's Framework"
description: Graph terminology for directed acyclic graphs; Bayesian networks, the factorization along parents and Markov compatibility; reading conditional independencies off a graph by d-separation (chains, forks, colliders), faithfulness and observational equivalence; causal Bayesian networks, interventions as graph surgery and the truncated factorization; structural equation models, the three levels of the ladder of causation and the computation of counterfactuals.
---

The potential outcomes framework of [3.9.1](/3.9.1)–[3.9.10](/3.9.10) starts from a given treatment and a given outcome and asks for the effect of the one on the other. Many scientific questions are not of this form. A biologist studying a signaling pathway, an economist studying a market or an epidemiologist studying a disease has many variables, none of which is singled out in advance, and wants to know how they influence one another: which variables are direct causes of which, and which variable one should manipulate to change an outcome of interest. Judea Pearl's framework answers such questions with three ingredients: a graph that represents the causal structure, a probability distribution that is compatible with it, and a notion of intervention that connects the two to causation.

The framework grew out of Bayesian networks, a tool of artificial intelligence. Early AI reasoned by deduction in symbolic logic; from the 1980s, systems that reasoned under uncertainty used probabilistic, inductive inference, and Bayesian networks made such inference tractable by encoding the conditional independencies of a joint distribution in a **directed acyclic graph** ([4.5.1](/4.5.1) tells the history). Causal reasoning adds to this the deductive element of a model of how the data are generated. This chapter builds the framework in three layers: graphs and the vocabulary for them (Section 11.1), graphs together with probability, which gives Bayesian networks and d-separation (Sections 11.2–11.3), and graphs together with probability and causality, which gives causal Bayesian networks, interventions and structural equations (Sections 11.4–11.5). [3.9.12](/3.9.12) uses the framework to compute average causal effects from observational data when the graph is known, and [3.9.13](/3.9.13) learns the graph from data when it is not.

## 11.1. Graph Terminology

A graph $G = (V, E)$ consists of a set $V$ of vertices, here also called nodes or variables, and a set $E$ of edges between pairs of them. The graph theory of [1.4](/1.4) supplies the basic notions of a **directed graph**, a **complete graph** and a **directed acyclic graph** (DAG); causal graphs add a vocabulary of their own, which differs slightly from that of [1.4.2](/1.4.2).

**Definition 11.1.1 (Graph Terminology)** Let $G = (V, E)$ be a graph whose edges are either directed ($X \to Y$) or undirected ($X - Y$).

- Two variables connected by an edge are **adjacent**.
- The **skeleton** of $G$ is the undirected graph obtained by removing the arrowheads from all edges of $G$.
- A **path** between $X$ and $Y$ is a sequence of distinct vertices starting at $X$ and ending at $Y$ in which consecutive vertices are adjacent; the edges may point along or against the direction of travel.
- A **directed path** from $X$ to $Y$ is a path $X \to \cdots \to Y$ in which every edge points from the earlier to the later vertex.
- Two vertices are **connected** if there is a path between them, and disconnected otherwise.

A path in this sense is a path of the skeleton in the sense of [1.4.2](/1.4.2) (no vertex is repeated); a directed path is a directed path of the graph itself. The distinction matters: in $X \to Z \leftarrow Y$ there is a path between $X$ and $Y$ but no directed path in either direction, and we shall see that such paths carry no association unless we condition on $Z$.

**Definition 11.1.2 (Family Relations in a DAG)** In a directed acyclic graph:

- if $X \to Y$, then $X$ is a **parent** of $Y$ and $Y$ is a **child** of $X$; the set of parents of $X_i$ is written $\mathrm{PA}_i$ and a value of it $\mathrm{pa}_i$;
- if there is a directed path from $X$ to $Y$, then $X$ is an **ancestor** of $Y$ and $Y$ is a **descendant** of $X$;
- two variables that have a common child are **spouses**;
- a **root** is a node without parents and a **leaf** (sink) a node without children;
- a **tree** is a connected DAG in which every node has at most one parent, and a **chain** a tree in which every node has at most one child.

We use the convention, common in causal inference, that a variable is not its own ancestor or descendant; when the variable itself is to be included we say so. Throughout the chapter capital letters denote variables or sets of variables and lowercase letters their values; $\mathbb{P}(x_1, \dots, x_n)$ abbreviates $\mathbb{P}(X_1 = x_1, \dots, X_n = x_n)$.

## 11.2. Bayesian Networks

### 11.2.1. Representing a Joint Distribution

A joint distribution of many variables is expensive to represent. Eight binary variables have $2^8 = 256$ joint probabilities, which sum to one, hence $255$ free parameters; a multivariate normal distribution of $n$ variables needs $n$ means and $n(n + 1)/2$ covariances. The number of parameters, and with it the amount of data needed to estimate them and the cost of computing marginal and conditional probabilities, grows quickly. The chain rule of probability writes any joint distribution, for any ordering of the variables, as

$$
\mathbb{P}(x_1, \dots, x_n) = \prod_{j=1}^n \mathbb{P}(x_j \mid x_1, \dots, x_{j-1}).
\tag{11.1}
$$
This identity saves nothing by itself, since the last factor still involves all variables. If all variables were independent, the joint distribution would be the product of the $n$ marginals, with $n$ parameters for binary variables, but independence is too strong to be useful. Bayesian networks sit in between: each variable depends directly on only a few of the others.

**Definition 11.2.1 (Probabilistic Graphical Model)** A **probabilistic graphical model** is a family of joint distributions together with a graph whose nodes are the variables, such that the graph encodes conditional independence assumptions and the joint distribution factorizes into local functions, one for each node or for each group of adjacent nodes. A probabilistic graphical model on an undirected graph is a **Markov random field** (Markov network); one on a directed acyclic graph is a **Bayesian network** (defined precisely below).

Informally, the graph says which parts of the system are directly dependent, and the local functions say how they interact. The two classes are not interchangeable (Section 11.3.4 and [3.9.13](/3.9.13)); causal inference uses DAGs, because the direction of an arrow can express the direction of causation. The name "Bayesian network" was coined by Pearl (1985) to emphasize the subjective nature of the input information, the reliance on Bayes' rule for updating it, and the distinction between causal and evidential modes of reasoning that Bayes' 1763 paper already drew.

### 11.2.2. Markov Parents and the Factorization

**Definition 11.2.2 (Bayesian Network)** Let $X_1, \dots, X_n$ be an ordered set of variables with joint distribution $\mathbb{P}$. A set $\mathrm{PA}_j \subseteq \{X_1, \dots, X_{j-1}\}$ is a set of **Markov parents** of $X_j$ if it is a minimal set of predecessors of $X_j$ that renders $X_j$ independent of all its other predecessors:

$$
\mathbb{P}(x_j \mid x_1, \dots, x_{j-1}) = \mathbb{P}(x_j \mid \mathrm{pa}_j)
$$
for all values, and no proper subset of $\mathrm{PA}_j$ has this property. The DAG with an arrow from each member of $\mathrm{PA}_j$ to $X_j$, for $j = 1, \dots, n$, is a **Bayesian network** of $\mathbb{P}$ (relative to the ordering).

Substituting the definition into the chain rule (11.1) gives the factorization that is the whole point of the construction.

**Theorem 11.2.1 (Factorization)** If $G$ is a Bayesian network of $\mathbb{P}$, then

$$
\mathbb{P}(x_1, \dots, x_n) = \prod_{i=1}^n \mathbb{P}(x_i \mid \mathrm{pa}_i).
\tag{11.2}
$$

**Proof** By the chain rule (11.1) and the defining property of the Markov parents, each factor $\mathbb{P}(x_j \mid x_1, \dots, x_{j-1})$ equals $\mathbb{P}(x_j \mid \mathrm{pa}_j)$. $\square$

The definition is also a recursive recipe for building a network: take the variables in order and, for each new variable $X_j$, select a minimal set of earlier variables that screens it off from the remaining earlier variables. A Bayesian network is thus a carrier of conditional independencies along the order of construction. When $\mathbb{P}$ is strictly positive, the minimal set is unique, so the network is unique given the ordering; different orderings can give different networks for the same distribution, some with many more arrows than others. Orderings that follow the direction of causation, from causes to effects, usually give the sparsest networks, which is why causal intuition is a good guide in practice.

**Example 11.2.1 (The Sprinkler Network)** Five variables describe the state of a pavement: $X_1$ the season, $X_2$ whether it rains, $X_3$ whether the sprinkler is on, $X_4$ whether the pavement is wet and $X_5$ whether it is slippery. Causal intuition suggests the ordering $X_1, \dots, X_5$ and the independencies

$$
X_2 \perp X_3 \mid X_1, \qquad X_4 \perp X_1 \mid (X_2, X_3), \qquad X_5 \perp (X_1, X_2, X_3) \mid X_4.
$$
The season influences both the rain and the use of the sprinkler, but once the season is known, the rain tells us nothing more about the sprinkler; the pavement is wet because of rain or sprinkler, whatever the season; and the pavement is slippery because it is wet. The Markov parents are therefore $\mathrm{PA}_2 = \mathrm{PA}_3 = \{X_1\}$, $\mathrm{PA}_4 = \{X_2, X_3\}$, $\mathrm{PA}_5 = \{X_4\}$, and

$$
\mathbb{P}(x_1, \dots, x_5) = \mathbb{P}(x_1)\,\mathbb{P}(x_2 \mid x_1)\,\mathbb{P}(x_3 \mid x_1)\,\mathbb{P}(x_4 \mid x_2, x_3)\,\mathbb{P}(x_5 \mid x_4).
$$
The network is the left panel of the figure in Section 11.4. With four seasons and binary $X_2, \dots, X_5$ the joint distribution has $4 \cdot 2^4 - 1 = 63$ free parameters, while the factorization needs $3 + 4 + 4 + 4 + 2 = 17$.

### 11.2.3. Markov Compatibility

Definition 11.2.2 constructs a graph from a distribution and an ordering. Conversely, given a graph $G$ and a distribution $\mathbb{P}$, we can check whether $\mathbb{P}$ factorizes as in (11.2) without referring to any ordering. This gives the basic link between graphs and probabilities.

**Definition 11.2.3 (Markov Compatibility)** If a distribution $\mathbb{P}$ admits the factorization (11.2) relative to a DAG $G$, we say that $G$ represents $\mathbb{P}$, that $G$ and $\mathbb{P}$ are **Markov compatible**, or that $\mathbb{P}$ is Markov relative to $G$.

Markov compatibility is a necessary condition for $G$ to be a Bayesian network of $\mathbb{P}$. It restricts $\mathbb{P}$ only through independencies: the factors are arbitrary conditional distributions, and nothing requires $X_i$ to depend on each of its parents. In particular, a complete DAG is compatible with every distribution, and the factorization $\mathbb{P}(x, y, z) = \mathbb{P}(x \mid y)\,\mathbb{P}(y)\,\mathbb{P}(z)$ is compatible with the DAG $X \leftarrow Y \to Z$, because $\mathbb{P}(z \mid y) = \mathbb{P}(z)$ is a special case of a conditional distribution of $Z$ given $Y$. An equivalent characterization uses only local independencies.

**Theorem 11.2.2 (Local Markov Condition)** A distribution $\mathbb{P}$ is Markov compatible with a DAG $G$ if and only if it satisfies the **local Markov condition**: every variable is independent of its nondescendants given its parents,

$$
X_i \perp \bigl(\text{nondescendants of } X_i\bigr) \setminus \mathrm{PA}_i \mid \mathrm{PA}_i \qquad \text{for all } i.
$$

**Proof** Order the variables so that parents precede children (a topological order, which exists because $G$ is acyclic). If the local Markov condition holds, then since all predecessors of $X_i$ in this order are nondescendants, $\mathbb{P}(x_i \mid x_1, \dots, x_{i-1}) = \mathbb{P}(x_i \mid \mathrm{pa}_i)$, and the chain rule gives (11.2). Conversely, suppose (11.2) holds and let $D$ be the set of descendants of $X_i$. Summing (11.2) over the values of the variables in $D$, starting with the leaves, removes their factors one by one (each sums to one), so the marginal of the remaining variables $V \setminus D$ is the product of their own factors. In this product $x_i$ appears only in its own factor $\mathbb{P}(x_i \mid \mathrm{pa}_i)$, because no child of $X_i$ is left; hence the conditional distribution of $X_i$ given all other nondescendants is $\mathbb{P}(x_i \mid \mathrm{pa}_i)$. $\square$

The local Markov condition is sometimes taken as the definition of a Bayesian network. Checking it for the sprinkler network reproduces the three independencies of Example 11.2.1, together with $X_2 \perp X_3 \mid X_1$ read in either order.

## 11.3. d-Separation

### 11.3.1. Three Basic Junctions

A convenient way to characterize the distributions compatible with a DAG is to list the conditional independencies that every such distribution must satisfy. Write $I(\mathbb{P})$ for the set of conditional independence statements $X \perp Y \mid Z$ that hold in $\mathbb{P}$, and $I(G)$ for the set of statements implied by the factorization (11.2) for every $\mathbb{P}$ compatible with $G$. The local Markov condition lists some members of $I(G)$; to read off all of them we need the graphical criterion of d-separation (the "d" stands for directional). It is built from three junctions of three variables.

![Chain, fork and collider. Red arrows mark a path that transmits association between $X$ and $Z$, grey arrows a blocked one; the shaded node is conditioned on. Conditioning on the middle node blocks a chain or a fork and opens a collider.](./plots/junctions.py)

**Definition 11.3.1 (Chain, Fork, Collider)** On a path, a node $Y$ with neighbors $X$ and $Z$ forms

- a **chain** if $X \to Y \to Z$ (or $X \leftarrow Y \leftarrow Z$);
- a **fork** if $X \leftarrow Y \to Z$; $Y$ is then a common cause of $X$ and $Z$;
- an inverted fork if $X \to Y \leftarrow Z$; $Y$ is then a **collider** on the path. If, in addition, $X$ and $Z$ are not adjacent, the triple is a **v-structure**.

Being a collider is a property of a node on a particular path: in the DAG $X \to Y \leftarrow Z$, $Y \to W$, the node $Y$ is a collider on the path $X \to Y \leftarrow Z$ but not on the path $X \to Y \to W$.

The factorization tells us what happens in each case.

- *Chain.* $\mathbb{P}(x, y, z) = \mathbb{P}(x)\,\mathbb{P}(y \mid x)\,\mathbb{P}(z \mid y)$, so $\mathbb{P}(z \mid x, y) = \mathbb{P}(x, y, z)/\mathbb{P}(x, y) = \mathbb{P}(z \mid y)$, that is, $X \perp Z \mid Y$. Think of $X$ as the past, $Y$ as the present and $Z$ as the future: given the present, the past carries no further information about the future (this is the **Markov property** of a **Markov chain**). Marginally, $X$ and $Z$ are in general dependent.
- *Fork.* $\mathbb{P}(x, y, z) = \mathbb{P}(y)\,\mathbb{P}(x \mid y)\,\mathbb{P}(z \mid y)$, so $\mathbb{P}(x, z \mid y) = \mathbb{P}(x \mid y)\,\mathbb{P}(z \mid y)$, again $X \perp Z \mid Y$. Two effects of a common cause are associated, but the association disappears once the cause is held fixed. This is the graphical form of **confounding** ([3.8.2](/3.8.2)).
- *Collider.* $\mathbb{P}(x, y, z) = \mathbb{P}(x)\,\mathbb{P}(z)\,\mathbb{P}(y \mid x, z)$. Summing over $y$ gives $\mathbb{P}(x, z) = \mathbb{P}(x)\,\mathbb{P}(z)$: the two causes are marginally independent. But $\mathbb{P}(x, z \mid y) \propto \mathbb{P}(x)\,\mathbb{P}(z)\,\mathbb{P}(y \mid x, z)$ does not factor in general, so given $Y$ they are dependent.

The third case is the surprising one. Toss two fair coins independently and let $Y$ indicate that at least one shows heads. Unconditionally the coins are independent; given $Y = 1$, learning that the first coin shows tails makes it certain that the second shows heads. The Monty Hall problem has the same structure: the door the contestant picks and the door hiding the car are independent, and the door the host opens depends on both; conditioning on the opened door makes the contestant's door informative about the location of the car, which is why switching helps.

**Definition 11.3.2 (Collider Bias)** The dependence between two causes created by conditioning on a common effect, or on a descendant of it, is **collider bias**. In artificial intelligence it is called explaining away (one cause, once confirmed, explains away the evidence for the other); in statistics it appears as Berkson's paradox and, more generally, as **selection bias**, when the units in a sample are selected on a common effect of the variables being studied.

Berkson's original example concerns hospital patients: two diseases that are independent in the population become negatively associated among hospitalized patients, because having either disease is a reason to be in the hospital. Collider bias is one of the main reasons why "adjusting for more covariates" is not always better; [3.9.12](/3.9.12) returns to it.

### 11.3.2. Blocked Paths and d-Separation

**Definition 11.3.3 (d-Separation)** Two nodes $X$ and $Y$ are **d-separated** by a set of nodes $Z$, written $(X \perp Y \mid Z)_G$, if $Z$ blocks every path between $X$ and $Y$, where a path $p$ is **blocked** by $Z$ if and only if

1. $p$ contains a chain $A \to M \to B$ or a fork $A \leftarrow M \to B$ whose middle node $M$ is in $Z$, or
2. $p$ contains a collider $A \to M \leftarrow B$ such that neither $M$ nor any descendant of $M$ is in $Z$.

The same definition applies to disjoint sets $X$, $Y$, $Z$ of nodes: $Z$ d-separates $X$ from $Y$ if it blocks every path from a node in $X$ to a node in $Y$.

:::

A path is open (it transmits association) when every node on it lets the association pass: every noncollider is outside $Z$ and every collider is in $Z$ or has a descendant in $Z$. The rule for descendants of colliders is natural: a descendant of $Y$ carries information about $Y$, so conditioning on it partly conditions on $Y$; in the sprinkler network, knowing that the pavement is slippery ($X_5$) is evidence that it is wet ($X_4$), and makes rain and sprinkler dependent.

**Theorem 11.3.1 (d-Separation and Conditional Independence)** Let $G$ be a DAG and $X$, $Y$, $Z$ disjoint sets of nodes.

1. If $Z$ d-separates $X$ from $Y$ in $G$, then $X \perp Y \mid Z$ in every distribution Markov compatible with $G$.
2. If $Z$ does not d-separate $X$ from $Y$, then $X$ and $Y$ are dependent given $Z$ in at least one distribution compatible with $G$; in fact, for discrete variables or linear Gaussian models, in all compatible distributions except a set of parameter values of measure zero.

Part 1 is due to Verma and Pearl (1988), part 2 to Geiger and Pearl (1988) and Meek (1995). Thus d-separation reads off exactly $I(G)$, the independencies shared by all distributions compatible with $G$. This property, $(X \perp Y \mid Z)_G \Rightarrow X \perp Y \mid Z$, is also called the global Markov property; for a DAG it is equivalent to the factorization and to the local Markov condition.

**Example 11.3.1** In the sprinkler network (Example 11.2.1):

| Statement | d-separated? | Reason |
|---|---|---|
| $X_2 \perp X_3 \mid X_1$ | yes | $X_2 \leftarrow X_1 \to X_3$ is blocked by the fork $X_1 \in Z$; $X_2 \to X_4 \leftarrow X_3$ is blocked by the collider $X_4 \notin Z$ |
| $X_2 \perp X_3 \mid \{X_1, X_4\}$ | no | conditioning on the collider $X_4$ opens $X_2 \to X_4 \leftarrow X_3$ |
| $X_2 \perp X_3 \mid \{X_1, X_5\}$ | no | $X_5$ is a descendant of the collider $X_4$ |
| $X_1 \perp X_5 \mid X_4$ | yes | both paths $X_1 \to X_2 \to X_4 \to X_5$ and $X_1 \to X_3 \to X_4 \to X_5$ pass through the chain node $X_4$ |
| $X_1 \perp X_4$ | no | $X_1 \to X_2 \to X_4$ is open |

Every "yes" holds in every distribution compatible with the network; every "no" fails in a generic one.

:::

### 11.3.3. Faithfulness

Markov compatibility says that $I(G) \subseteq I(\mathbb{P})$: every independence read off the graph holds in the distribution. The distribution may have more independencies than the graph shows, because its parameters happen to cancel.

**Definition 11.3.4 (Faithfulness)** A distribution $\mathbb{P}$ is **faithful** to a DAG $G$ if $I(\mathbb{P}) \subseteq I(G)$, that is, every conditional independence in $\mathbb{P}$ is implied by d-separation in $G$; there are no spurious independencies that the graph does not sanction. A DAG that is Markov compatible with $\mathbb{P}$ and to which $\mathbb{P}$ is faithful, so that $I(G) = I(\mathbb{P})$, is a perfect map of $\mathbb{P}$.

**Example 11.3.2 (Cancelling Paths)** Let $X = U_X$, $Z = bX + U_Z$ and $Y = aX + cZ + U_Y$ with independent standard normal errors. The DAG has the arrows $X \to Z$, $Z \to Y$, $X \to Y$, and no d-separation holds between $X$ and $Y$. But $\operatorname{Cov}(X, Y) = a + bc$, which vanishes when $a = -bc$: a direct effect and an indirect effect of equal size and opposite sign cancel. The resulting distribution satisfies $X \perp Y$, which the graph does not imply, so it is not faithful.

:::

Such cancellations require exact equalities between parameters and are therefore "unlikely" (part 2 of Theorem 11.3.1), but they are not impossible: a drug that lowers blood pressure directly and raises it through a side effect, or a homeostatic system that is designed to hold an output constant, can come close. Faithfulness is an assumption about the world, not a theorem. Its role is to make the graph recoverable from the distribution: under Markov compatibility and faithfulness, $I(G) = I(\mathbb{P})$, and the independencies estimated from data determine what can be known about $G$. This is the basis of the constraint-based learning algorithms of [3.9.13](/3.9.13).

### 11.3.4. Observational Equivalence

Even with $I(G) = I(\mathbb{P})$ the graph is not always determined by the distribution, because different DAGs can encode the same independencies. The chain $X \to Y \to Z$, the reversed chain $X \leftarrow Y \leftarrow Z$ and the fork $X \leftarrow Y \to Z$ all imply exactly $X \perp Z \mid Y$; only the collider $X \to Y \leftarrow Z$ implies $X \perp Z$ instead.

**Definition 11.3.5 (Markov Equivalence)** Two DAGs are **Markov equivalent** (observationally equivalent) if they imply the same set of conditional independencies, $I(G_1) = I(G_2)$; equivalently, every distribution compatible with one is compatible with the other.

**Theorem 11.3.2 (Verma and Pearl 1990)** Two DAGs are Markov equivalent if and only if they have the same skeleton and the same set of v-structures.

For example, reversing the arrow $X_1 \to X_2$ of the sprinkler network neither creates nor destroys a v-structure (its only v-structure, $X_2 \to X_4 \leftarrow X_3$, is untouched, and $X_2 \to X_1 \to X_3$ is a chain), so the reversed network is equivalent to the original: no amount of observational data can tell whether the season influences the rain or the rain the season. Reversing $X_2 \to X_4$ instead destroys the v-structure at $X_4$ and gives a network with different independencies. Observational equivalence places a limit on our ability to infer the direction of arrows from probabilities alone: from data we can at best learn the equivalence class, represented by the skeleton with the arrows of the v-structures and of whatever edges they force ([3.9.13](/3.9.13)). Distinguishing between members of a class requires interventions or background knowledge.

Directed and undirected graphs also differ in what they can express. The independencies of a v-structure $X \to Z \leftarrow Y$ ($X \perp Y$ but not given $Z$) cannot be represented by any undirected graph, and the independencies of an undirected four-cycle cannot be represented by any DAG ([3.9.13](/3.9.13)). This is one reason why causal inference works with DAGs rather than Markov random fields.

## 11.4. Causal Bayesian Networks and Interventions

### 11.4.1. From Bayesian Networks to Causal Bayesian Networks

So far the arrows of a Bayesian network meant only conditional independence; any ordering of the variables gives some network, and Markov equivalent networks are indistinguishable. A causal Bayesian network adds a claim that can be tested only by acting on the system: each arrow represents a stable mechanism by which a parent influences its child. There are two uses. When the causal structure is known from prior experience or expert knowledge, we want to estimate the effects of interventions and the parameters of the mechanisms; when it is unknown, we want to learn it. The tool for both is the intervention.

In the potential outcomes framework, the causal effect of a treatment compares two worlds, one in which a unit is treated and one in which it is not, and only one of them is observed. Pearl's framework makes the comparison of worlds explicit by modeling what happens to the joint distribution when a variable is set by an outside agent rather than by its usual causes.

**Definition 11.4.1 (Intervention and the do-Operator)** An atomic **intervention** $\operatorname{do}(X = x)$ sets the variable $X$ to the constant $x$ by an external action, overriding the mechanism that normally determines $X$, and leaves every other mechanism unchanged. The resulting distribution of the other variables is written $\mathbb{P}(v \mid \operatorname{do}(X = x))$, or $\mathbb{P}_x(v)$, or briefly $\mathbb{P}(v \mid \operatorname{do}(x))$. The symbol $\operatorname{do}(\cdot)$ is the **do-operator**. For a set of variables, $\operatorname{do}(X = x)$ sets each of them.

The difference between $\mathbb{P}(y \mid x)$ and $\mathbb{P}(y \mid \operatorname{do}(x))$ is the difference between seeing and doing. $\mathbb{P}(y \mid x)$ is the distribution of $Y$ among the units for which $X = x$ happened to occur; $\mathbb{P}(y \mid \operatorname{do}(x))$ is the distribution of $Y$ if every unit were made to have $X = x$.

**Definition 11.4.2 (Causal Bayesian Network)** Let $\mathbb{P}(v)$ be a distribution on a set $V$ of variables, and let $\mathbb{P}_x(v)$ be the distribution resulting from the intervention $\operatorname{do}(X = x)$ that sets a subset $X \subseteq V$ to constants $x$. Denote by $\mathbb{P}_*$ the set of all interventional distributions $\mathbb{P}_x(v)$, $X \subseteq V$, including $\mathbb{P}(v)$ itself ($X = \varnothing$). A DAG $G$ is a **causal Bayesian network** compatible with $\mathbb{P}_*$ if and only if, for every $\mathbb{P}_x \in \mathbb{P}_*$,

1. $\mathbb{P}_x(v)$ is Markov compatible with $G$;
2. $\mathbb{P}_x(v_i) = 1$ for all $V_i \in X$ whenever $v_i$ is consistent with $X = x$;
3. $\mathbb{P}_x(v_i \mid \mathrm{pa}_i) = \mathbb{P}(v_i \mid \mathrm{pa}_i)$ for all $V_i \notin X$ whenever $\mathrm{pa}_i$ is consistent with $X = x$.

The DAG of a causal Bayesian network is called a **causal diagram** (causal DAG).

Condition 3 is the heart of the definition: each conditional distribution $\mathbb{P}(v_i \mid \mathrm{pa}_i)$ is an autonomous module that stays invariant under interventions on other variables. The causal diagram makes a far stronger claim than a Bayesian network: it says not only that the observed distribution factorizes along $G$, but also that it would still factorize, with the same factors, after any intervention.

### 11.4.2. Interventions as Graph Surgery

Condition 2 and condition 3 together say how an intervention acts on the graph: the mechanism of $X$, the factor $\mathbb{P}(x \mid \mathrm{pa}_X)$, is replaced by a point mass at $x$, and all other factors are kept. Graphically, all arrows pointing into $X$ are deleted, because $X$ no longer listens to its parents, and $X$ is fixed at $x$. The result is the manipulated graph, written $G_{\overline{X}}$.

![The sprinkler network as a causal Bayesian network (left) and after the intervention "turn the sprinkler on" (right). The arrow from the season to the sprinkler is removed; all other mechanisms are unchanged.](./plots/sprinkler.py)

**Theorem 11.4.1 (Truncated Factorization)** If $G$ is a causal Bayesian network for $\mathbb{P}_*$, then for every intervention $\operatorname{do}(X = x)$,

$$
\mathbb{P}_x(v) =
\begin{cases}
\displaystyle\prod_{i:\, V_i \notin X} \mathbb{P}(v_i \mid \mathrm{pa}_i), & v \text{ consistent with } x,\\[1ex]
0, & \text{otherwise}.
\end{cases}
\tag{11.3}
$$

**Proof** By condition 1, $\mathbb{P}_x$ factorizes along $G$: $\mathbb{P}_x(v) = \prod_i \mathbb{P}_x(v_i \mid \mathrm{pa}_i)$. For $V_i \in X$ the factor is $1$ if $v_i$ agrees with $x$ (condition 2) and the product is $0$ otherwise; for $V_i \notin X$ it equals $\mathbb{P}(v_i \mid \mathrm{pa}_i)$ (condition 3). $\square$

The truncated factorization expresses an interventional distribution entirely through the factors of the observational distribution. Since $X$ no longer depends on anything, every parent set in the manipulated model is exogenous relative to its child, and once we control a node's direct causes, no other intervention affects its distribution. For a single variable $X_j$ with parents $\mathrm{PA}_j$, dividing (11.2) by the factor of $X_j$ gives

$$
\mathbb{P}(v \mid \operatorname{do}(X_j = x_j')) = \frac{\mathbb{P}(v)}{\mathbb{P}(x_j' \mid \mathrm{pa}_j)} \quad\text{for } v \text{ with } x_j = x_j',
\qquad
\mathbb{P}(y \mid \operatorname{do}(x_j')) = \sum_{\mathrm{pa}_j} \mathbb{P}(y \mid x_j', \mathrm{pa}_j)\,\mathbb{P}(\mathrm{pa}_j),
$$
the second formula being "adjust for the parents"; [3.9.12](/3.9.12) develops it into the backdoor and front-door criteria.

**Example 11.4.1 (Seeing versus Doing)** In the sprinkler network, let the season be dry or rainy with probability $1/2$ each, let it rain with probability $0.7$ in the rainy season and $0.1$ in the dry season, and let the sprinkler be on with probability $0.6$ in the dry season and $0.1$ in the rainy season. Observing that the sprinkler is on is evidence that the season is dry, hence that it is not raining:

$$
\mathbb{P}(X_2 = \text{rain} \mid X_3 = \text{on}) = \frac{0.5 \cdot 0.7 \cdot 0.1 + 0.5 \cdot 0.1 \cdot 0.6}{0.5 \cdot 0.1 + 0.5 \cdot 0.6} = \frac{0.065}{0.35} \approx 0.19.
$$
Turning the sprinkler on changes nothing about the weather. By (11.3), $\mathbb{P}_{X_3 = \text{on}}(x_1, x_2, x_4, x_5) = \mathbb{P}(x_1)\,\mathbb{P}(x_2 \mid x_1)\,\mathbb{P}(x_4 \mid x_2, X_3 = \text{on})\,\mathbb{P}(x_5 \mid x_4)$, and summing over $x_1, x_4, x_5$,

$$
\mathbb{P}(X_2 = \text{rain} \mid \operatorname{do}(X_3 = \text{on})) = \mathbb{P}(X_2 = \text{rain}) = 0.5 \cdot 0.7 + 0.5 \cdot 0.1 = 0.40.
$$
The effect of the intervention on the pavement, in contrast, is computed from the unchanged mechanisms $\mathbb{P}(x_4 \mid x_2, x_3)$ and $\mathbb{P}(x_5 \mid x_4)$ with the rain at its unconditional distribution.

### 11.4.3. A Simulated Example

The difference between conditioning and intervening, and the fact that observational data alone cannot settle it, is clearest in an example where three different causal models produce exactly the same joint distribution.

**Example 11.4.2 (Three Models, One Distribution)** Consider three structural models for two observed variables, with independent normal errors:

| Model | Causal diagram | Equations |
|---|---|---|
| 1 | $X \to Y$ | $X = U_X$, $Y = X + U_Y$, $U_X, U_Y \sim \mathcal{N}(0, 1)$ |
| 2 | $Y \to X$ | $Y = U_Y \sim \mathcal{N}(0, 2)$, $X = Y/2 + U_X$, $U_X \sim \mathcal{N}(0, 1/2)$ |
| 3 | $X \leftarrow Z \to Y$ | $Z \sim \mathcal{N}(0, 1)$, $X = 0.8Z + U_X$, $Y = 1.25Z + U_Y$, $U_X \sim \mathcal{N}(0, 0.36)$, $U_Y \sim \mathcal{N}(0, 0.4375)$ |

In all three, $(X, Y)$ is bivariate normal with $\operatorname{Var}(X) = 1$, $\operatorname{Var}(Y) = 2$ and $\operatorname{Cov}(X, Y) = 1$, so the observational distributions are identical and no data on $(X, Y)$ can distinguish the models; in all three, $Y \mid X = 3 \sim \mathcal{N}(3, 1)$. The interventional distributions differ. Under $\operatorname{do}(X = 3)$ the equation for $X$ is replaced by $X = 3$:

- in model 1, $Y = 3 + U_Y \sim \mathcal{N}(3, 1)$, the same as the conditional distribution;
- in model 2, $Y = U_Y \sim \mathcal{N}(0, 2)$, unaffected, because $Y$ is a cause of $X$, not an effect;
- in model 3, $Y = 1.25Z + U_Y \sim \mathcal{N}(0, 2)$, unaffected, because the association is due to the common cause $Z$.

![Three causal models with the same observational distribution. Top: samples of $(X, Y)$, indistinguishable. Bottom: the distribution of $Y$ under $\operatorname{do}(X = 3)$ (histogram) and the conditional distribution of $Y$ given $X = 3$ (curve). Simulated data.](./plots/intervention_toy.py)

The causal diagram, not the data, determines which answer is right. In model 3 the association is pure **confounding**; if $Z$ is observed, the adjustment formula of [3.9.12](/3.9.12) recovers the correct interventional distribution, and if it is not, the effect cannot be identified from $(X, Y)$.

## 11.5. Structural Equations and the Three Levels of Causation

### 11.5.1. Functional Causal Models

A second, more detailed representation of a causal model writes each variable as a deterministic function of its direct causes and of an unobserved disturbance. It is popular in economics and the social sciences, and it is what allows counterfactual questions about individual units to be asked.

**Definition 11.5.1 (Structural Equation Model)** A **structural equation model** (structural causal model, functional causal model) $M$ consists of a set of endogenous variables $V = \{X_1, \dots, X_n\}$, a set of exogenous variables $U = \{U_1, \dots, U_n\}$ with a distribution $\mathbb{P}(u)$, and a set of equations

$$
x_i = f_i(\mathrm{pa}_i, u_i), \qquad i = 1, \dots, n,
$$
one for each endogenous variable, where $\mathrm{PA}_i \subseteq V \setminus \{X_i\}$ are the direct causes of $X_i$. The causal diagram of $M$ has an arrow from each member of $\mathrm{PA}_i$ to $X_i$. A linear SEM has $x_i = \sum_{k \ne i} \alpha_{ik}x_k + u_i$.

Each equation is a mechanism, read from right to left: it states how nature assigns a value to $X_i$, not a symmetric algebraic relation (we do not solve $Y = bX + U_Y$ for $X$). If the diagram is acyclic and the disturbances $U_i$ are mutually independent (a Markovian model), then the distribution of $V$ induced by $\mathbb{P}(u)$ is Markov compatible with the causal diagram, and replacing the equation of $X$ by $X = x$ yields the truncated factorization (11.3). Thus a Markovian SEM defines a causal Bayesian network. When disturbances are dependent, the dependence is represented by a latent common cause, drawn as a dashed bidirected arc or an explicit unobserved node $U$.

An SEM says more than the causal Bayesian network it induces. The network specifies the conditional distributions $\mathbb{P}(x_i \mid \mathrm{pa}_i)$; the SEM specifies how each unit's value arises from its own disturbance $u_i$, so it determines what would have happened to a particular unit under a different action. Note also what neither representation provides: the causal structure, which variables appear on the right-hand side of which equation, comes from prior experience or expert knowledge, not from the equations themselves. This course mostly works with DAGs because they are more convenient for construction and inference, although less informative about the detailed probabilities.

### 11.5.2. The Ladder of Causation

**Definition 11.5.2 (Ladder of Causation)** Causal questions form a hierarchy of three levels, the **ladder of causation**:

| Level | Activity | Typical question | Quantity |
|---|---|---|---|
| 1. Association | seeing, observing | What if I see $x$? | $\mathbb{P}(y \mid x)$ |
| 2. Intervention | doing | What if I do $x$? How can I make $y$ happen? | $\mathbb{P}(y \mid \operatorname{do}(x))$ |
| 3. Counterfactual | imagining, retrospection | What if I had done $x'$, given that I did $x$ and observed $y$? Why? | $\mathbb{P}(y_{x'} \mid x, y)$ |

Each level answers questions that the levels below cannot. Data on a single distribution answer level 1; a causal Bayesian network answers level 2 through the truncated factorization; level 3 needs a structural model, or assumptions about it. In the sprinkler network:

- *Observation.* Would the pavement be slippery if we find the sprinkler off? $\mathbb{P}(X_5 = \text{slippery} \mid X_3 = \text{off})$, which also takes into account that an inactive sprinkler suggests a rainy season.
- *Intervention.* Would the pavement be slippery if we make sure that the sprinkler is off? $\mathbb{P}(X_5 = \text{slippery} \mid \operatorname{do}(X_3 = \text{off}))$, in which the season keeps its marginal distribution.
- *Counterfactual.* Would the pavement be slippery had the sprinkler been off, given that the pavement is in fact not slippery and the sprinkler is on? The evidence and the hypothetical action contradict each other ($X_3$ is on in the actual world and off in the hypothetical one), so no single $\operatorname{do}$-expression answers it; we need $\mathbb{P}\bigl((X_5)_{X_3 = \text{off}} = \text{slippery} \mid X_3 = \text{on}, X_5 = \text{not slippery}\bigr)$.

### 11.5.3. Computing Counterfactuals

**Definition 11.5.3 (Counterfactual)** Let $M$ be a structural model, $X$ and $Y$ sets of endogenous variables and $u$ a value of the exogenous variables. Let $M_x$ be the modified model in which the equations for $X$ are replaced by $X = x$. The **counterfactual** $Y_x(u)$, read "the value $Y$ would have taken had $X$ been $x$, in situation $u$", is the solution for $Y$ of the equations of $M_x$ with $U = u$.

Since $u$ describes a particular unit, $Y_x(u)$ is the potential outcome of that unit. Given evidence $E = e$ about the unit, the counterfactual is computed in three steps:

1. *Abduction*: use the evidence $E = e$ to determine the value of $U$ (or its conditional distribution $\mathbb{P}(u \mid e)$);
2. *Action*: modify $M$ by replacing the equations of $X$ by $X = x$, obtaining $M_x$;
3. *Prediction*: use $M_x$ and the value of $U$ to compute $Y$.

**Example 11.5.1 (Joe's Study Time)** In a linear SEM for students, $X$ is the time spent in an encouragement program, $H$ the time spent on homework and $Y$ the exam score (all standardized):

$$
X = U_X, \qquad H = aX + U_H, \qquad Y = bX + cH + U_Y,
$$
with $a = 0.5$, $b = 0.7$, $c = 0.4$ and mutually independent disturbances. A student, Joe, is observed with $X = 0.5$, $H = 1$ and $Y = 1.5$. What would Joe's score have been had he doubled his homework time?

*Abduction.* From the equations, $U_X = 0.5$, $U_H = 1 - 0.5 \cdot 0.5 = 0.75$ and $U_Y = 1.5 - 0.7 \cdot 0.5 - 0.4 \cdot 1 = 0.75$.

*Action.* Replace the equation for $H$ by $H = 2$.

*Prediction.* $Y_{H=2}(U_X = 0.5, U_H = 0.75, U_Y = 0.75) = 0.7 \cdot 0.5 + 0.4 \cdot 2 + 0.75 = 1.90$.

The answer is specific to Joe: his large $U_Y$ (he does better than his program and homework predict) is carried over to the hypothetical world. The level-2 quantity $\mathbb{E}[Y \mid \operatorname{do}(H = 2)] = b\,\mathbb{E}[X] + 2c + \mathbb{E}[U_Y]$ refers to the population instead, and equals $0.8$ if all disturbances have mean zero.

:::

In a linear model the abduction step is a matter of solving equations; in general it means computing the posterior $\mathbb{P}(u \mid e)$, and the counterfactual is then a distribution, $\mathbb{P}(y_x \mid e) = \sum_u \mathbb{P}(Y_x(u) = y)\,\mathbb{P}(u \mid e)$.

### 11.5.4. Comparison with the Potential Outcomes Framework

The two frameworks of this course are logically equivalent in their basic objects. The **potential outcomes** $Y_i(1)$, $Y_i(0)$ of Rubin's framework are the counterfactuals $Y_x(u)$ of a structural model, with the unit $i$ corresponding to the value $u$ of the exogenous variables; and the **average treatment effect** is a contrast of interventional distributions,

$$
\mathbb{E}[Y \mid \operatorname{do}(X = 1)] - \mathbb{E}[Y \mid \operatorname{do}(X = 0)] = \mathbb{E}[Y(1)] - \mathbb{E}[Y(0)],
$$
as [3.9.12](/3.9.12) shows in detail. The differences are of emphasis.

| | Potential outcomes (Rubin) | Causal graphs (Pearl) |
|---|---|---|
| Starting point | a treatment and an outcome | a system of variables |
| Basic object | $Y_i(w)$ for each unit | $\mathbb{P}(v \mid \operatorname{do}(x))$, mechanisms $\mathbb{P}(v_i \mid \mathrm{pa}_i)$ |
| Level of description | individual units | the population under intervention ($\operatorname{do}$); individuals via SEMs |
| Assumptions | stated as conditions on the assignment mechanism ($W \perp (Y(0), Y(1)) \mid X$), SUTVA | encoded in the missing arrows of the graph |
| Strengths | precise about assumptions and design; finite-population inference | reasoning about many variables, deriving which adjustments are valid |

The $\operatorname{do}$-operator captures the behavior of a population under intervention, whereas $Y_i(x)$ describes the behavior of a specific individual under it. The potential outcomes notation is more explicit about what is assumed, since every assumption is a stated condition on potential outcomes; the graphical notation is more transparent about why an assumption may hold, since it is derived from a picture of the mechanisms. In practice the two are used together, and [3.9.12](/3.9.12) translates **unconfoundedness** into a graphical condition.

## Summary

- Graphs: the DAG vocabulary of adjacency, skeleton, paths (along or against arrows) and directed paths, parents, children, ancestors, descendants, spouses, roots, leaves (Definitions 11.1.1, 11.1.2).
- Bayesian networks: the Markov parents of each variable give a DAG along which the joint distribution factorizes, $\mathbb{P}(x_1, \dots, x_n) = \prod_i \mathbb{P}(x_i \mid \mathrm{pa}_i)$ (Definition 11.2.2, Theorem 11.2.1). Markov compatibility (Definition 11.2.3) is equivalent to the local Markov condition (Theorem 11.2.2).
- d-Separation:

  | Junction | Marginally | Given the middle node |
  |---|---|---|
  | chain $X \to Y \to Z$ | dependent | independent |
  | fork $X \leftarrow Y \to Z$ (confounding) | dependent | independent |
  | collider $X \to Y \leftarrow Z$ | independent | dependent (collider bias, also given a descendant) |

  A set $Z$ d-separates $X$ and $Y$ if it blocks every path (Definition 11.3.3); d-separation implies conditional independence in every compatible distribution and characterizes $I(G)$ (Theorem 11.3.1).
- Graph and distribution: Markov compatibility means $I(G) \subseteq I(\mathbb{P})$; faithfulness means $I(\mathbb{P}) \subseteq I(G)$ (Definition 11.3.4). Markov equivalent DAGs have the same skeleton and v-structures (Theorem 11.3.2), so data determine at most the equivalence class.
- Causal Bayesian networks: each factor $\mathbb{P}(v_i \mid \mathrm{pa}_i)$ is an invariant mechanism (Definition 11.4.2). The intervention $\operatorname{do}(X = x)$ deletes the arrows into $X$ and gives the truncated factorization $\mathbb{P}_x(v) = \prod_{V_i \notin X} \mathbb{P}(v_i \mid \mathrm{pa}_i)$ (Theorem 11.4.1). Seeing is not doing (Examples 11.4.1, 11.4.2).
- Structural equations: $x_i = f_i(\mathrm{pa}_i, u_i)$ (Definition 11.5.1); a Markovian SEM induces a causal Bayesian network and also defines counterfactuals $Y_x(u)$, computed by abduction, action and prediction (Definition 11.5.3, Example 11.5.1).
- Ladder of causation: association $\mathbb{P}(y \mid x)$, intervention $\mathbb{P}(y \mid \operatorname{do}(x))$, counterfactual $\mathbb{P}(y_{x'} \mid x, y)$ (Definition 11.5.2). The do-operator describes populations, potential outcomes individuals; the two frameworks agree on the basic objects.

## Questions

1. The DAG $X \to Y \to Z$ and the factorization $\mathbb{P}(x, y, z) = \mathbb{P}(z \mid y)\,\mathbb{P}(y \mid x)\,\mathbb{P}(x)$ are given. Is it correct to say that the DAG and the distribution are Markov compatible and that $X$ is a cause of $Y$?

   **Answer** The first half is correct: the distribution factorizes along the DAG. The second half does not follow. Markov compatibility concerns conditional independencies only, and the same distribution is compatible with the Markov equivalent DAGs $X \leftarrow Y \leftarrow Z$ and $X \leftarrow Y \to Z$ (Theorem 11.3.2). A causal reading of the arrows is an additional assumption (Definition 11.4.2), which can be checked only with interventions or background knowledge.
2. Is the distribution $\mathbb{P}(x, y, z) = \mathbb{P}(x \mid y)\,\mathbb{P}(y)\,\mathbb{P}(z)$ Markov compatible with the DAG $X \leftarrow Y \to Z$? Is it faithful to it?

   **Answer** It is compatible: the DAG requires the factorization $\mathbb{P}(y)\,\mathbb{P}(x \mid y)\,\mathbb{P}(z \mid y)$, and $\mathbb{P}(z \mid y) = \mathbb{P}(z)$ is an admissible conditional distribution. It is not faithful: it satisfies $Y \perp Z$ (and $X \perp Z$), which d-separation in the DAG does not imply. A faithful DAG for it is $X \leftarrow Y$ with $Z$ isolated (or $X \to Y$ with $Z$ isolated).
3. If a DAG $G$ and a distribution $\mathbb{P}$ are Markov compatible and $\mathbb{P}$ is faithful to $G$, does $G$ determine $\mathbb{P}$?

   **Answer** No. Compatibility and faithfulness only say that $I(G) = I(\mathbb{P})$. $G$ determines which conditional independencies hold, but the conditional distributions $\mathbb{P}(x_i \mid \mathrm{pa}_i)$ are free (subject to not creating extra independencies), so infinitely many distributions share the same perfect map. Conversely, $\mathbb{P}$ does not determine $G$ either, only its Markov equivalence class.
4. Consider the DAG with arrows $A \to B$, $A \to C$, $B \to D$, $C \to D$, $D \to E$, $C \to F$. Decide whether each statement holds by d-separation: (a) $B \perp C \mid A$; (b) $B \perp C \mid \{A, E\}$; (c) $A \perp E \mid \{B, C\}$; (d) $B \perp F \mid A$; (e) $B \perp F \mid \{A, D\}$.

   **Answer** (a) Yes: $B \leftarrow A \to C$ is blocked by $A$, and $B \to D \leftarrow C$ by the unconditioned collider $D$. (b) No: $E$ is a descendant of the collider $D$, which opens $B \to D \leftarrow C$. (c) Yes: every path from $A$ to $E$ goes through $B$ or $C$ as a chain node ($A \to B \to D \to E$, $A \to C \to D \to E$). (d) Yes: $B \leftarrow A \to C \to F$ is blocked by $A$, and $B \to D \leftarrow C \to F$ by the collider $D$. (e) No: conditioning on $D$ opens $B \to D \leftarrow C \to F$, and $C$ is not conditioned on.
5. For the DAG of Question 4 with binary variables, write the factorization of the joint distribution and count its free parameters. How many does an unrestricted joint distribution of six binary variables have?

   **Answer** $\mathbb{P}(a)\,\mathbb{P}(b \mid a)\,\mathbb{P}(c \mid a)\,\mathbb{P}(d \mid b, c)\,\mathbb{P}(e \mid d)\,\mathbb{P}(f \mid c)$, with $1 + 2 + 2 + 4 + 2 + 2 = 13$ parameters, against $2^6 - 1 = 63$ without restrictions.
6. In Example 11.4.1, compute $\mathbb{P}(\text{dry season} \mid X_3 = \text{on})$ and $\mathbb{P}(\text{dry season} \mid \operatorname{do}(X_3 = \text{on}))$. Explain the difference.

   **Answer** $\mathbb{P}(\text{dry} \mid X_3 = \text{on}) = 0.5 \cdot 0.6/(0.5 \cdot 0.6 + 0.5 \cdot 0.1) = 0.3/0.35 \approx 0.86$. Under the intervention the factor $\mathbb{P}(x_3 \mid x_1)$ is removed, so the season keeps its marginal distribution: $\mathbb{P}(\text{dry} \mid \operatorname{do}(X_3 = \text{on})) = 0.5$. An active sprinkler that was switched on by its usual mechanism is evidence about its cause, the season; one switched on by us is not.
7. In Example 11.3.2 with $b = c = 1$, for which $a$ is the distribution unfaithful? Which independence does it then satisfy that the graph does not imply, and can the same distribution arise from a faithful DAG?

   **Answer** $\operatorname{Cov}(X, Y) = a + bc = a + 1$, so $a = -1$. Then $Y = -X + (X + U_Z) + U_Y = U_Z + U_Y$, so $X \perp Y$ (they are jointly normal and uncorrelated), while $X$ and $Y$ are adjacent in the graph. Since $\operatorname{Cov}(X, Z) = 1$ and $\operatorname{Cov}(Z, Y) = 1$, the pairs $(X, Z)$ and $(Z, Y)$ are dependent, and so are $X$ and $Y$ given $Z$ (the partial correlation is $0 - \frac{1}{\sqrt 2}\cdot\frac12 \neq 0$). Its only independence is $X \perp Y$, and $X \perp Y$ with all other pairs dependent is exactly the independence structure of the collider $X \to Z \leftarrow Y$, which is a perfect map. A learning algorithm assuming faithfulness would therefore return the collider, with the wrong arrow between $Z$ and $Y$.
8. In Example 11.5.1, what would Joe's homework time and score have been had he not taken part in the encouragement program ($X = 0$)?

   **Answer** Abduction gives the same disturbances $U_H = 0.75$, $U_Y = 0.75$. In $M_{X=0}$: $H = 0.5 \cdot 0 + 0.75 = 0.75$ and $Y = 0.7 \cdot 0 + 0.4 \cdot 0.75 + 0.75 = 1.05$. Joe's score would have been lower by $0.45 = b \cdot 0.5 + c \cdot a \cdot 0.5$, the total effect $b + ac = 0.9$ per unit of $X$ times the change $0.5$.
9. A study finds that among patients admitted to a hospital, those with disease A are less likely to have disease B, although the two diseases are independent in the population. Draw the causal diagram and explain the finding.

   **Answer** $A \to H \leftarrow B$, where $H$ indicates hospital admission: each disease is a reason to be admitted. Restricting the sample to admitted patients conditions on the collider $H$, which opens the path $A \to H \leftarrow B$ (Definition 11.3.2). Among admitted patients, a patient without A must have been admitted for some other reason, which makes B more likely; hence the negative association, an example of selection bias (Berkson's paradox).
10. Which level of the ladder of causation does the question "Would the pavement be slippery had the sprinkler been off, given that the pavement is in fact not slippery and the sprinkler is on?" belong to? Is $\mathbb{P}(X_5 = \text{slippery} \mid \operatorname{do}(X_3 = \text{off}))$ the right quantity?

    **Answer** It is a counterfactual (level 3). The interventional probability averages over all situations and ignores the evidence about this particular day; the counterfactual first updates the exogenous variables on the evidence ($X_3 = \text{on}$, $X_5 = \text{not slippery}$, which for instance suggests that it did not rain and that the pavement is hard to wet) and then evaluates the model with the sprinkler off. If the mechanisms are monotone (rain and sprinkler can only make the pavement wetter, and wetness can only make it more slippery), the answer is zero: a pavement that was not slippery with the sprinkler on would not have been slippery with it off, whereas the interventional probability is positive whenever rain can make the pavement slippery.
