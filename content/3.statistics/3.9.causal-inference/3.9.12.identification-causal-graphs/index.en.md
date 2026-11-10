---
title: Identifying Causal Effects from Causal Graphs
description: The average causal effect defined by interventions; Simpson's paradox revisited and the adjustment formula, with its inverse-propensity form and a dictionary between the notations of Rubin and Pearl; backdoor paths, the backdoor criterion and the backdoor adjustment theorem with proof; the front-door criterion (smoking, tar and lung cancer); the controlled direct effect, the three rules of the do-calculus, their completeness and the identification algorithm.
---

In [3.9.11](/3.9.11) a causal Bayesian network was defined by what happens under interventions: each mechanism $\mathbb{P}(v_i \mid \mathrm{pa}_i)$ stays the same, and the intervention $\operatorname{do}(X = x)$ removes the mechanism of $X$. With such a model, the average causal effect of $X$ on $Y$ is a property of interventional distributions. But data usually come from observing the system, not from intervening on it, and the variables that would make the computation easy are often not measured. This chapter asks when an interventional distribution $\mathbb{P}(y \mid \operatorname{do}(x))$ can be computed from the observational distribution of the measured variables, given the causal diagram, and gives the formulas. The answers are graphical criteria: the backdoor criterion, which tells us which covariates to adjust for and is the graphical counterpart of the **unconfoundedness** of [3.9.2](/3.9.2) and [3.9.8](/3.9.8); the front-door criterion, which can identify an effect even with an unmeasured confounder of treatment and outcome; and the do-calculus, which handles every identifiable case. [3.9.13](/3.9.13) turns to the problem of finding the graph itself.

## 12.1. The Average Causal Effect

**Definition 12.1.1 (Average Causal Effect in a Causal Graph)** Let $G$ be a causal Bayesian network containing the variables $X$ and $Y$. The average causal effect of changing $X$ from $x_2$ to $x_1$ on $Y$ is

$$
\mathrm{ACE} = \mathbb{E}[Y \mid \operatorname{do}(X = x_1)] - \mathbb{E}[Y \mid \operatorname{do}(X = x_2)]
= \sum_y y\,\mathbb{P}(Y = y \mid \operatorname{do}(X = x_1)) - \sum_y y\,\mathbb{P}(Y = y \mid \operatorname{do}(X = x_2)).
$$
For binary $X$ and $Y$ it is $\mathbb{P}(Y = 1 \mid \operatorname{do}(X = 1)) - \mathbb{P}(Y = 1 \mid \operatorname{do}(X = 0))$.

The definition imagines two hypothetical interventions on the whole population: give everyone $X = x_1$, then give everyone $X = x_2$, and compare the mean outcomes. It is the **average treatment effect** of [3.9.1](/3.9.1) in the super-population sense (Section 12.2.3). If we could carry out the interventions, as in a randomized experiment, we would estimate the two interventional distributions directly. With observational data we have only $\mathbb{P}(v)$, and the question is whether $\mathbb{P}(y \mid \operatorname{do}(x))$ is determined by $\mathbb{P}(v)$ and $G$. When it is, for every distribution compatible with $G$ (positive on the relevant values), the effect is said to be identifiable from $G$; the formula expressing it through observational quantities is the identifying formula, and estimation then reduces to estimating the observational quantities in it.

## 12.2. Simpson's Paradox Revisited

### 12.2.1. The Example

**Example 12.2.1 (A Drug, Recovery and Gender)** In a study of a new drug, $X = 1$ means taking the drug, $Y = 1$ recovering and $Z = 1$ being male. Among 700 patients (a classic illustration of **Simpson's paradox**):

| | Drug ($X = 1$) | No drug ($X = 0$) |
|---|---|---|
| Men ($Z = 1$) | 81 of 87 recovered (93%) | 234 of 270 recovered (87%) |
| Women ($Z = 0$) | 192 of 263 recovered (73%) | 55 of 80 recovered (69%) |
| Combined | 273 of 350 recovered (78%) | 289 of 350 recovered (83%) |

The drug is better for men and better for women, but worse for the combined population. Which conclusion should a doctor act on? Suppose we know that gender affects both the decision to take the drug (women were more likely to take it) and the chance of recovery (women recover less often, with or without the drug), and that the drug does not change one's gender: the causal diagram is $Z \to X$, $Z \to Y$, $X \to Y$. The combined comparison then mixes the effect of the drug with the effect of gender, since the drug group is mostly female. The answer depends on the causal story, not on the table: with the same numbers but $Z$ a post-treatment variable such as blood pressure, the combined comparison would be the right one.

### 12.2.2. The Adjustment Formula

To compute $\mathbb{P}(Y = 1 \mid \operatorname{do}(X = x))$, consider the manipulated model $\mathbb{P}_m(\cdot) = \mathbb{P}(\cdot \mid \operatorname{do}(X = x))$, whose graph $G_{\overline{X}}$ has lost the arrow $Z \to X$. Two of its components are unchanged mechanisms, and one independence can be read off the new graph:

1. $\mathbb{P}_m(Y = y \mid X = x, Z = z) = \mathbb{P}(Y = y \mid X = x, Z = z)$: the mechanism of $Y$ is untouched;
2. $\mathbb{P}_m(Z = z) = \mathbb{P}(Z = z)$: the mechanism of $Z$ is untouched;
3. in $G_{\overline{X}}$, $Z$ and $X$ are d-separated, so $\mathbb{P}_m(Z = z \mid X = x) = \mathbb{P}_m(Z = z)$.

Hence, by the law of total probability in the manipulated model,

$$
\mathbb{P}(y \mid \operatorname{do}(x)) = \sum_z \mathbb{P}_m(y \mid x, z)\,\mathbb{P}_m(z \mid x) = \sum_z \mathbb{P}(y \mid x, z)\,\mathbb{P}(z).
\tag{12.1}
$$
This is the *adjustment formula*: compute the effect within each level of $Z$ and average the levels with the population weights $\mathbb{P}(z)$, not with the weights $\mathbb{P}(z \mid x)$ of the treated or untreated group. The same result follows in one line from the truncated factorization (11.3): $\mathbb{P}(y, z \mid \operatorname{do}(x)) = \mathbb{P}(z)\,\mathbb{P}(y \mid x, z)$.

**Example 12.2.2** In Example 12.2.1, $\mathbb{P}(Z = 1) = 357/700 = 0.51$. With the exact within-group rates,

$$
\begin{aligned}
\mathbb{P}(Y = 1 \mid \operatorname{do}(X = 1)) &= \tfrac{81}{87}(0.51) + \tfrac{192}{263}(0.49) \approx 0.4748 + 0.3577 = 0.833,\\
\mathbb{P}(Y = 1 \mid \operatorname{do}(X = 0)) &= \tfrac{234}{270}(0.51) + \tfrac{55}{80}(0.49) \approx 0.4420 + 0.3369 = 0.779,
\end{aligned}
$$
so $\mathrm{ACE} \approx 0.054$ (with the rounded percentages $0.93$, $0.73$, $0.87$, $0.69$ one gets $0.832 - 0.782 = 0.050$). Under the stated causal story, taking the drug raises the probability of recovery by about five percentage points, in contrast with the naive comparison $0.78 - 0.83 = -0.05$.

:::

The adjustment in (12.1) was over the parents of $X$. The argument holds in any causal Bayesian network.

**Theorem 12.2.1 (Adjustment for Direct Causes)** Let $\mathrm{PA}_X$ be the set of parents of $X$ in a causal Bayesian network and $Y$ a variable not in $\mathrm{PA}_X \cup \{X\}$. Then

$$
\mathbb{P}(y \mid \operatorname{do}(x)) = \sum_{\mathrm{pa}} \mathbb{P}(y \mid x, \mathrm{pa})\,\mathbb{P}(\mathrm{pa}),
$$
where the sum runs over the values of $\mathrm{PA}_X$.

**Proof** By the truncated factorization (11.3), $\mathbb{P}(v \mid \operatorname{do}(x)) = \mathbb{P}(v)/\mathbb{P}(x \mid \mathrm{pa}_X)$ for $v$ consistent with $x$, that is, $\mathbb{P}(v \mid \operatorname{do}(x)) = \mathbb{P}(v \setminus \{x, \mathrm{pa}_X\} \mid x, \mathrm{pa}_X)\,\mathbb{P}(\mathrm{pa}_X)$. Summing over all variables except $Y$ and $\mathrm{PA}_X$ gives $\mathbb{P}(y, \mathrm{pa} \mid \operatorname{do}(x)) = \mathbb{P}(y \mid x, \mathrm{pa})\,\mathbb{P}(\mathrm{pa})$, and summing over $\mathrm{pa}$ gives the claim. $\square$

### 12.2.3. Connection with the Potential Outcomes Framework

Multiplying and dividing (12.1) by $\mathbb{P}(x \mid z)$ gives an equivalent form,

$$
\mathbb{P}(y \mid \operatorname{do}(x)) = \sum_z \frac{\mathbb{P}(x, y, z)}{\mathbb{P}(x \mid z)},
\tag{12.2}
$$
in which each observation with $X = x$ is weighted by the inverse of the probability of the treatment it actually received given $Z$. $\mathbb{P}(X = 1 \mid z)$ is the **propensity score**, and the sample version of (12.2) is the **inverse probability weighting** (Horvitz–Thompson) estimator of [3.9.8](/3.9.8) and [3.9.10](/3.9.10): $\mathbb{E}[Y \mid \operatorname{do}(X = 1)] = \mathbb{E}[W Y / e(X)]$ in Rubin's notation. The weighted form is useful when $Z$ is high-dimensional and the propensity score can be modeled more easily than the outcome.

The two frameworks use different letters for the same roles.

| Role | Rubin (3.9.1–3.9.10, 3.9.14) | Pearl (3.9.11–3.9.13) |
|---|---|---|
| treatment | $W$ | $X$ |
| pre-treatment covariates | $X$ | $Z$ |
| outcome | $Y^{\mathrm{obs}}$, with potential outcomes $Y(0)$, $Y(1)$ | $Y$; $Y_x$ in a structural model |
| average effect | $\tau_{\mathrm{sp}} = \mathbb{E}[Y(1) - Y(0)]$ | $\mathbb{E}[Y \mid \operatorname{do}(X = 1)] - \mathbb{E}[Y \mid \operatorname{do}(X = 0)]$ |
| no unmeasured confounding | $W \perp (Y(0), Y(1)) \mid X$ | $Z$ satisfies the backdoor criterion |
| adjustment | stratification, weighting by $e(X)$ | $\sum_z \mathbb{P}(y \mid x, z)\,\mathbb{P}(z)$ |

For binary $W$ and $Y$, $\mathbb{P}(Y = 1 \mid \operatorname{do}(W = 1)) - \mathbb{P}(Y = 1 \mid \operatorname{do}(W = 0)) = \mathbb{E}[Y(1)] - \mathbb{E}[Y(0)] = \tau_{\mathrm{sp}}$, because $Y(w)$ is the outcome a unit would have under $\operatorname{do}(W = w)$. In Example 12.2.1 the adjustment formula is the stratified estimator with gender as the stratum; equivalently, the weighting estimator with propensity scores $\mathbb{P}(X = 1 \mid Z = 1) = 87/357$ and $\mathbb{P}(X = 1 \mid Z = 0) = 263/343$.

## 12.3. The Backdoor Criterion

### 12.3.1. The Criterion

Adjusting for the parents of $X$ (Theorem 12.2.1) is the most natural choice, but the parents may be unmeasured (a doctor's reasons for prescribing), or there may be many of them. We need other sets of variables that are equally good. The guiding principle, visible in Example 12.2.1, is threefold: block every spurious path between $X$ and $Y$, leave every directed path from $X$ to $Y$ unperturbed, and create no new spurious paths.

**Definition 12.3.1 (Backdoor Path)** A **backdoor path** from $X$ to $Y$ is a path between $X$ and $Y$ whose first edge points into $X$, that is, a path of the form $X \leftarrow \cdots\, Y$.

Backdoor paths are the non-causal routes along which association flows between $X$ and $Y$: they reach $X$ "through the back door", from its causes. Directed paths $X \to \cdots \to Y$ carry the effect we want to measure. Other paths leaving $X$ forward and reaching $Y$ through a collider ($X \to M \leftarrow \cdots\, Y$) carry no association unless we condition on the collider.

**Definition 12.3.2 (Backdoor Criterion)** A set of variables $Z$ satisfies the **backdoor criterion** relative to an ordered pair of variables $(X, Y)$ in a DAG $G$ if

1. no node in $Z$ is a descendant of $X$, and
2. $Z$ blocks every path between $X$ and $Y$ that contains an arrow into $X$.

Condition 2 removes the spurious association; condition 1 keeps the causal paths intact (conditioning on a descendant of $X$ that lies on a directed path, a mediator, would block part of the effect) and prevents new spurious associations (conditioning on a common descendant of $X$ and $Y$, or on a descendant of such a collider, would open a path). The parents of $X$ always satisfy the criterion: they are not descendants of $X$, and every backdoor path starts $X \leftarrow P$ with $P$ a parent that is a chain or fork node on the path.

**Theorem 12.3.1 (Backdoor Adjustment)** If a set of observed variables $Z$ satisfies the backdoor criterion relative to $(X, Y)$, then the causal effect of $X$ on $Y$ is identifiable and is given by

$$
\mathbb{P}(y \mid \operatorname{do}(x)) = \sum_z \mathbb{P}(y \mid x, z)\,\mathbb{P}(z).
\tag{12.3}
$$

**Proof** We first treat the case that appears most often in practice, a single discrete confounder: the diagram is $Z \to X$, $Z \to Y$, $X \to Y$ (possibly with further variables that are not ancestors of $X$ or $Y$). Then $\mathbb{P}(x, y, z) = \mathbb{P}(z)\,\mathbb{P}(x \mid z)\,\mathbb{P}(y \mid x, z)$, and by the truncated factorization the intervention removes the factor $\mathbb{P}(x \mid z)$:

$$
\mathbb{P}(y \mid \operatorname{do}(x)) = \sum_z \mathbb{P}(y, z \mid \operatorname{do}(x)) = \sum_z \mathbb{P}(z)\,\mathbb{P}(y \mid x, z).
$$

For the general case, represent the intervention by an extra parent $F$ of $X$: $F = \text{idle}$ leaves the mechanism of $X$ in place and $F = x$ sets $X = x$, so that $\mathbb{P}(\cdot \mid \operatorname{do}(x)) = \mathbb{P}(\cdot \mid F = x)$ and $\mathbb{P}(\cdot) = \mathbb{P}(\cdot \mid F = \text{idle})$. In the augmented graph:

- $Z \perp F$. Every path from $F$ starts $F \to X$. If it continues $X \to \cdots$, it either is a directed path from $X$, which cannot end in $Z$ (no member of $Z$ is a descendant of $X$), or it contains a collider; that collider and its descendants are descendants of $X$, so none is in the (empty) conditioning set. If it continues $X \leftarrow \cdots$, then $X$ is a collider and we do not condition on $X$ or on any of its descendants.
- $Y \perp F \mid (X, Z)$. A path $F \to X \to \cdots\, Y$ is blocked by $X$, a chain node in the conditioning set. A path $F \to X \leftarrow \cdots\, Y$ continues as a backdoor path from $X$ to $Y$; condition 2 says that $Z$ blocks it in $G$, and one checks that adding $X$ to the conditioning set cannot reopen it: a collider on it that is an ancestor of $X$ yields another backdoor path from $X$ to $Y$ through that collider's parents, which $Z$ must also block.

Therefore

$$
\mathbb{P}(y \mid \operatorname{do}(x)) = \sum_z \mathbb{P}(y \mid x, z, F = x)\,\mathbb{P}(z \mid F = x) = \sum_z \mathbb{P}(y \mid x, z, F = \text{idle})\,\mathbb{P}(z \mid F = \text{idle}),
$$
which is (12.3). $\square$

The backdoor criterion is the graphical form of unconfoundedness: if $Z$ satisfies it, then $X \perp \{Y_x\}$ given $Z$, that is, $W \perp (Y(0), Y(1)) \mid Z$ in Rubin's notation. The DAG makes this assumption checkable against a stated causal story, whereas in Rubin's framework it is postulated directly. With $Z = \varnothing$ the criterion says that $X$ has no backdoor paths, as in a randomized experiment, where $X$ has no parents; then $\mathbb{P}(y \mid \operatorname{do}(x)) = \mathbb{P}(y \mid x)$.

### 12.3.2. Examples

![Four causal diagrams. (a) The unmeasured $Z$ (dashed arrows) confounds $X$ and $Y$, but the measured $W$ blocks the backdoor path. (b) Every adjustment set must contain the collider $Z$, together with $E$ or $A$. (c) The front-door setting: $U$ is unmeasured and $Z$ mediates the whole effect. (d) The direct effect of $X$ on $Y$ requires holding $Z$ fixed.](./plots/adjustment_dags.py)

**Example 12.3.1 (Adjusting for a Proxy)** In panel (a), $X$ is a new drug, $Y$ recovery, $W$ the patient's weight and $Z$ the unmeasured socioeconomic status, which influences both who receives the drug and the patient's weight, and weight affects recovery. The only backdoor path is $X \leftarrow Z \to W \to Y$, and the measured $W$ blocks it; $W$ is not a descendant of $X$. So $W$ satisfies the backdoor criterion and

$$
\mathbb{P}(y \mid \operatorname{do}(x)) = \sum_w \mathbb{P}(y \mid x, w)\,\mathbb{P}(w).
$$
We do not need to measure the confounder itself, only a variable that intercepts its influence on the outcome.

**Example 12.3.2 (Adjusting for a Collider)** In panel (b), the backdoor paths from $X$ to $Y$ are $X \leftarrow Z \to Y$, $X \leftarrow Z \leftarrow A \to Y$, $X \leftarrow E \to Z \to Y$ and $X \leftarrow E \to Z \leftarrow A \to Y$. The first requires $Z$ in the adjustment set. But $Z$ is a collider on the last path, which conditioning on $Z$ opens; it must then be blocked again by $E$ or $A$. The sets satisfying the criterion are $\{E, Z\}$, $\{A, Z\}$ and $\{E, Z, A\}$; $\{Z\}$ alone does not. Sometimes we have to adjust for a collider, and then we must also adjust for something else.

:::

Two lessons follow. First, adjusting for "all pre-treatment variables" is not automatically safe: in the diagram with arrows $E \to X$, $E \to M$, $A \to M$, $A \to Y$ and $X \to Y$ (so-called M-bias), the empty set satisfies the criterion and adjusting for the pre-treatment variable $M$ alone creates **collider bias**. Second, when several sets satisfy the criterion, all of them give the same $\mathbb{P}(y \mid \operatorname{do}(x))$. We can therefore choose the set that is cheapest to measure or gives the most precise estimate; and if two different adjustment sets are both observed, the equality $\sum_{z_1} \mathbb{P}(y \mid x, z_1)\,\mathbb{P}(z_1) = \sum_{z_2} \mathbb{P}(y \mid x, z_2)\,\mathbb{P}(z_2)$ is a testable consequence of the causal diagram, much like the independencies implied by d-separation. In panel (b), adjusting for $\{E, Z\}$ and for $\{A, Z\}$ must give the same answer.

## 12.4. The Front-Door Criterion

### 12.4.1. Smoking, Tar and Lung Cancer

When the confounder of $X$ and $Y$ is unmeasured and no other variable blocks the backdoor paths, the backdoor criterion fails. This was the situation in the debate about smoking and lung cancer in the 1950s and 1960s: R. A. Fisher argued that a genotype might cause both a craving for nicotine and cancer, which no observational study could rule out. Suppose, however, that smoking ($X$) affects cancer ($Y$) only through the tar deposited in the lungs ($Z$), that the unmeasured genotype $U$ does not affect tar directly, and that the confounding acts on $X$ and $Y$ only (panel (c)). Then the effect can be identified by two consecutive applications of the backdoor criterion.

- *Effect of $X$ on $Z$.* The only backdoor path from $X$ to $Z$ is $X \leftarrow U \to Y \leftarrow Z$, which is blocked by the collider $Y$. Hence $\mathbb{P}(z \mid \operatorname{do}(x)) = \mathbb{P}(z \mid x)$.
- *Effect of $Z$ on $Y$.* The backdoor path $Z \leftarrow X \leftarrow U \to Y$ is blocked by $X$, which is not a descendant of $Z$. Hence $\mathbb{P}(y \mid \operatorname{do}(z)) = \sum_{x'} \mathbb{P}(y \mid x', z)\,\mathbb{P}(x')$.
- *Chaining.* Since $X$ affects $Y$ only through $Z$, $\mathbb{P}(y \mid \operatorname{do}(x)) = \sum_z \mathbb{P}(z \mid \operatorname{do}(x))\,\mathbb{P}(y \mid \operatorname{do}(z))$.

### 12.4.2. The Criterion and the Formula

**Definition 12.4.1 (Front-Door Criterion)** A set of variables $Z$ satisfies the **front-door criterion** relative to an ordered pair of variables $(X, Y)$ if

1. $Z$ intercepts all directed paths from $X$ to $Y$;
2. there is no unblocked backdoor path from $X$ to $Z$; and
3. all backdoor paths from $Z$ to $Y$ are blocked by $X$.

**Theorem 12.4.1 (Front-Door Adjustment)** If $Z$ satisfies the front-door criterion relative to $(X, Y)$ and $\mathbb{P}(x, z) > 0$, then the causal effect of $X$ on $Y$ is identifiable and

$$
\mathbb{P}(y \mid \operatorname{do}(x)) = \sum_z \mathbb{P}(z \mid x) \sum_{x'} \mathbb{P}(y \mid x', z)\,\mathbb{P}(x').
\tag{12.4}
$$

**Proof** We prove it for the diagram of panel (c): $U \to X$, $U \to Y$, $X \to Z$, $Z \to Y$ with $U$ unobserved. The joint distribution of all four variables factorizes as $\mathbb{P}(u)\,\mathbb{P}(x \mid u)\,\mathbb{P}(z \mid x)\,\mathbb{P}(y \mid z, u)$, and the truncated factorization gives

$$
\mathbb{P}(y \mid \operatorname{do}(x)) = \sum_z \mathbb{P}(z \mid x) \sum_u \mathbb{P}(y \mid z, u)\,\mathbb{P}(u).
$$
It remains to express the inner sum through observed quantities. Write $\mathbb{P}(u) = \sum_{x'} \mathbb{P}(u \mid x')\,\mathbb{P}(x')$. The graph implies $Y \perp X \mid (Z, U)$ (both paths from $X$ to $Y$ pass through $Z$ or the fork $U$) and $U \perp Z \mid X$ (the paths $U \to X \to Z$ and $U \to Y \leftarrow Z$ are blocked by the chain node $X$ and the collider $Y$). Hence $\mathbb{P}(y \mid z, u) = \mathbb{P}(y \mid x', z, u)$ and $\mathbb{P}(u \mid x') = \mathbb{P}(u \mid x', z)$, and

$$
\sum_u \mathbb{P}(y \mid z, u)\,\mathbb{P}(u) = \sum_{x'} \mathbb{P}(x') \sum_u \mathbb{P}(y \mid x', z, u)\,\mathbb{P}(u \mid x', z) = \sum_{x'} \mathbb{P}(x')\,\mathbb{P}(y \mid x', z).
$$
Substituting gives (12.4). In a general DAG the three conditions of Definition 12.4.1 give the same two independencies (with $U$ replaced by the variables on the backdoor paths), and the same computation applies; it can also be derived from the rules of the do-calculus in Section 12.5. $\square$

The formula has a clear reading: $\mathbb{P}(z \mid x)$ is the effect of smoking on tar, and the inner sum is the effect of tar on cancer, adjusted for smoking with the population weights $\mathbb{P}(x')$; adjusting for $X$ there removes the confounding by the genotype, because the genotype reaches tar only through smoking.

**Example 12.4.1 (Hypothetical Data)** Suppose a study of 800 000 people, half smokers, gives the following group sizes and cancer rates.

| Group | $\mathbb{P}(x, z)$ (% of population) | $\mathbb{P}(Y = 1 \mid x, z)$ (% with cancer) |
|---|---|---|
| $X = 0$, $Z = 0$: nonsmokers, no tar | 47.5 | 10 |
| $X = 1$, $Z = 0$: smokers, no tar | 2.5 | 90 |
| $X = 0$, $Z = 1$: nonsmokers, tar | 2.5 | 5 |
| $X = 1$, $Z = 1$: smokers, tar | 47.5 | 85 |

So $\mathbb{P}(X = 1) = 0.5$, $\mathbb{P}(Z = 1 \mid X = 1) = 0.95$ and $\mathbb{P}(Z = 1 \mid X = 0) = 0.05$. The inner sums are $0.10(0.5) + 0.90(0.5) = 0.50$ for $z = 0$ and $0.05(0.5) + 0.85(0.5) = 0.45$ for $z = 1$, and

$$
\begin{aligned}
\mathbb{P}(Y = 1 \mid \operatorname{do}(X = 1)) &= 0.05(0.50) + 0.95(0.45) = 0.4525,\\
\mathbb{P}(Y = 1 \mid \operatorname{do}(X = 0)) &= 0.95(0.50) + 0.05(0.45) = 0.4975.
\end{aligned}
$$
Although smokers have far more cancer than nonsmokers ($0.8525$ against $0.0975$), under the front-door model smoking would lower the cancer rate by $4.5$ percentage points, because within each smoking group tar is associated with less cancer. The numbers are invented to show that the formula can reverse a naive comparison; they say nothing about real smoking. The example also shows how strong the assumptions are: that smoking acts only through tar and that tar shares no unmeasured cause with cancer are claims about biology, not about the data.

:::

## 12.5. The do-Calculus

### 12.5.1. Beyond Backdoor and Front Door

**Definition 12.5.1 (Controlled Direct Effect)** The **controlled direct effect** of changing $X$ from $x'$ to $x$ on $Y$, with a mediator $Z$ held fixed at $z$, is

$$
\mathrm{CDE}(z) = \mathbb{P}(Y = y \mid \operatorname{do}(X = x), \operatorname{do}(Z = z)) - \mathbb{P}(Y = y \mid \operatorname{do}(X = x'), \operatorname{do}(Z = z)),
$$
or the corresponding difference of expectations.

**Example 12.5.1 (Gender and Hiring)** Does an employer discriminate by gender? In panel (d), gender $X$ affects hiring $Y$ directly and through qualification $Z$, and the applicant's family income $I$ affects both qualification and hiring. The total effect of gender includes the legitimate route through qualification; discrimination is the direct effect, the effect of gender among applicants with the same qualification. Conditioning on $Z$ does not give it: $Z$ is a collider on $X \to Z \leftarrow I \to Y$, so comparing men and women of equal qualification opens a spurious path through income. Neither the backdoor nor the front-door criterion applies to the joint intervention on $X$ and $Z$; a general tool is needed.

:::

### 12.5.2. The Three Rules

For a DAG $G$ and a set of nodes $X$, let $G_{\overline{X}}$ be the graph obtained by deleting all arrows pointing into nodes of $X$, and $G_{\underline{X}}$ the graph obtained by deleting all arrows emerging from nodes of $X$; $G_{\overline{X}\underline{Z}}$ deletes both kinds. Write $\hat x$ for $\operatorname{do}(X = x)$.

**Theorem 12.5.1 (do-Calculus)** Let $G$ be a causal diagram and $X$, $Y$, $Z$, $W$ disjoint sets of variables. For every distribution compatible with $G$:

1. *Insertion or deletion of observations:* $\mathbb{P}(y \mid \hat x, z, w) = \mathbb{P}(y \mid \hat x, w)$ if $(Y \perp Z \mid X, W)_{G_{\overline{X}}}$.
2. *Action–observation exchange:* $\mathbb{P}(y \mid \hat x, \hat z, w) = \mathbb{P}(y \mid \hat x, z, w)$ if $(Y \perp Z \mid X, W)_{G_{\overline{X}\underline{Z}}}$.
3. *Insertion or deletion of actions:* $\mathbb{P}(y \mid \hat x, \hat z, w) = \mathbb{P}(y \mid \hat x, w)$ if $(Y \perp Z \mid X, W)_{G_{\overline{X}\,\overline{Z(W)}}}$, where $Z(W)$ is the set of $Z$-nodes that are not ancestors of any $W$-node in $G_{\overline{X}}$.

The rules, due to Pearl (1995), follow from the truncated factorization and Theorem 11.3.1 applied to the manipulated graph. Each has a simple meaning.

- Rule 1 is d-separation in the world after the intervention on $X$: once the arrows into $X$ are cut, an observation $Z$ that is d-separated from $Y$ given $X$ and $W$ can be ignored.
- Rule 2 says when observing $Z = z$ is as good as setting it: when $X$ and $W$ block all backdoor paths from $Z$ to $Y$, which are exactly the paths left in $G_{\overline{X}\underline{Z}}$ between $Z$ and $Y$. It is the backdoor criterion in rule form.
- Rule 3 says when an action has no effect: when there is no directed path from $Z$ to $Y$ left after cutting the arrows into $Z$ (with a correction, $Z(W)$, for $Z$-nodes that are ancestors of observed $W$-nodes, since conditioning on their descendants would reintroduce their influence).

An interventional quantity is identified when a sequence of rule applications, together with ordinary probability calculus, transforms it into an expression without hats.

**Example 12.5.2 (Gender and Hiring, Continued)** In panel (d),

$$
\begin{aligned}
\mathbb{P}(y \mid \hat x, \hat z)
&= \mathbb{P}(y \mid x, \hat z) && \text{Rule 2: } (Y \perp X \mid Z)_{G_{\overline{Z}\underline{X}}}\\
&= \sum_i \mathbb{P}(y \mid x, \hat z, i)\,\mathbb{P}(i \mid x, \hat z) && \text{total probability}\\
&= \sum_i \mathbb{P}(y \mid x, z, i)\,\mathbb{P}(i \mid x, \hat z) && \text{Rule 2: } (Y \perp Z \mid X, I)_{G_{\underline{Z}}}\\
&= \sum_i \mathbb{P}(y \mid x, z, i)\,\mathbb{P}(i \mid x) && \text{Rule 3: } (I \perp Z \mid X)_{G_{\overline{Z}}}\\
&= \sum_i \mathbb{P}(y \mid x, z, i)\,\mathbb{P}(i) && \text{Rule 1: } (I \perp X)_G.
\end{aligned}
$$
Each condition can be checked on the graph. In $G_{\overline{Z}\underline{X}}$ both arrows out of $X$ and the arrow $I \to Z$ are removed, so $X$ is isolated. In $G_{\underline{Z}}$ the paths from $Z$ to $Y$ are $Z \leftarrow X \to Y$ and $Z \leftarrow I \to Y$, blocked by $X$ and $I$. In $G_{\overline{Z}}$ (here $Z(W) = Z$ because $Z$ is not an ancestor of $X$) the only path between $I$ and $Z$ is $I \to Y \leftarrow Z$, blocked by the unconditioned collider $Y$. In $G$, the paths from $I$ to $X$ all pass through a collider ($Z$ or $Y$), so $I \perp X$ holds by the graph. Hence

$$
\mathrm{CDE}(z) = \sum_i \bigl[\mathbb{P}(y \mid x, z, i) - \mathbb{P}(y \mid x', z, i)\bigr]\mathbb{P}(i):
$$
compare men and women of the same qualification and the same family income, and average over income. Income must be measured; qualification alone is not enough.

:::

### 12.5.3. Completeness and Further Applications

The three rules are complete: if an interventional distribution $\mathbb{P}(y \mid \operatorname{do}(x))$ is identifiable from a causal diagram with latent variables, then it can be reduced to an observational expression by some finite sequence of rule applications, and if no such sequence exists, the effect is not identifiable (Shpitser and Pearl 2006; Huang and Valtorta 2006). Finding the sequence is not a matter of trial and error. Tian and Pearl (2002) gave a graphical characterization of identifiable effects in terms of so-called c-components (sets of variables connected by latent confounding), and Shpitser and Pearl (2006) and Huang and Valtorta (2006) turned it into the ID algorithm, which decides for any causal diagram and any interventional distribution whether it is identifiable and, if it is, returns the formula; completeness of the do-calculus was proved through this algorithm. In the simplest non-identifiable case, $X \to Y$ with an unobserved common cause of $X$ and $Y$ and nothing else, the algorithm reports failure, as it should: Example 11.4.2 exhibited models with the same observational distribution and different effects.

Beyond single effects, the same machinery addresses other questions: mediation analysis, the decomposition of an effect into direct and indirect parts ([3.9.15](/3.9.15)); transportability, whether an effect estimated in one population can be carried to another population whose causal diagram differs in known ways; and the combination of several experimental and observational studies (data fusion, meta-synthesis). Software implements these criteria: in R, the package `pcalg` has a function `backdoor` that finds adjustment sets, and the package `causaleffect` implements the ID algorithm.

## Summary

- The average causal effect is defined by interventions, $\mathbb{E}[Y \mid \operatorname{do}(x_1)] - \mathbb{E}[Y \mid \operatorname{do}(x_2)]$ (Definition 12.1.1); it is identifiable if it can be written in terms of the observational distribution and the graph.
- Adjustment: for a set $Z$ satisfying the backdoor criterion (no descendants of $X$; blocks every path into $X$; Definition 12.3.2),

  $$
  \mathbb{P}(y \mid \operatorname{do}(x)) = \sum_z \mathbb{P}(y \mid x, z)\,\mathbb{P}(z) = \sum_z \frac{\mathbb{P}(x, y, z)}{\mathbb{P}(x \mid z)}
  $$
  (Theorems 12.2.1, 12.3.1; Eq. (12.2)). The first form is stratification, the second inverse probability weighting with the propensity score; the backdoor criterion is the graphical form of unconfoundedness. Simpson's paradox is resolved by the causal diagram, not by the data (Examples 12.2.1, 12.2.2).
- Choosing covariates: adjust to block backdoor paths, never for descendants of $X$; a collider may have to be adjusted together with a variable that re-blocks the opened path (Example 12.3.2); all valid sets give the same answer.
- Front door: if $Z$ intercepts all directed paths from $X$ to $Y$, has no unblocked backdoor path from $X$, and $X$ blocks its backdoor paths to $Y$ (Definition 12.4.1), then $\mathbb{P}(y \mid \operatorname{do}(x)) = \sum_z \mathbb{P}(z \mid x)\sum_{x'}\mathbb{P}(y \mid x', z)\,\mathbb{P}(x')$ even with an unmeasured confounder of $X$ and $Y$ (Theorem 12.4.1).
- do-Calculus: three rules (insert or delete observations; exchange actions and observations; insert or delete actions) checked by d-separation in mutilated graphs (Theorem 12.5.1). They identify, for example, the controlled direct effect $\sum_i[\mathbb{P}(y \mid x, z, i) - \mathbb{P}(y \mid x', z, i)]\mathbb{P}(i)$ (Example 12.5.2), and they are complete; the ID algorithm decides identifiability and finds the formula systematically.

| Tool | Graphical condition | Formula |
|---|---|---|
| adjust for parents | always valid | $\sum_{\mathrm{pa}} \mathbb{P}(y \mid x, \mathrm{pa})\,\mathbb{P}(\mathrm{pa})$ |
| backdoor | $Z$ non-descendants of $X$ blocking all backdoor paths | $\sum_z \mathbb{P}(y \mid x, z)\,\mathbb{P}(z)$ |
| front door | $Z$ mediates all of the effect, no confounding of $X$–$Z$, $X$ blocks $Z$–$Y$ | $\sum_z \mathbb{P}(z \mid x)\sum_{x'}\mathbb{P}(y \mid x', z)\,\mathbb{P}(x')$ |
| do-calculus | three rules | any identifiable effect |

## Questions

1. In the diagram $Z \to X$, $Z \to Y$, $X \to Y$ with binary variables, a study of 200 patients gives the following counts.

   | | $Z = 0$, $X = 0$ | $Z = 0$, $X = 1$ | $Z = 1$, $X = 0$ | $Z = 1$, $X = 1$ |
   |---|---|---|---|---|
   | $Y = 1$ | 30 | 15 | 5 | 40 |
   | $Y = 0$ | 50 | 5 | 15 | 40 |

   Compute the naive difference $\mathbb{P}(Y = 1 \mid X = 1) - \mathbb{P}(Y = 1 \mid X = 0)$ and the average causal effect.

   **Answer** Naive: $\mathbb{P}(Y = 1 \mid X = 1) = (15 + 40)/100 = 0.55$ and $\mathbb{P}(Y = 1 \mid X = 0) = (30 + 5)/100 = 0.35$, difference $0.20$. With $\mathbb{P}(Z = 1) = 100/200 = 0.5$ and the within-stratum rates $0.75$, $0.375$ ($Z = 0$) and $0.5$, $0.25$ ($Z = 1$): $\mathbb{P}(Y = 1 \mid \operatorname{do}(X = 1)) = 0.5(0.75) + 0.5(0.5) = 0.625$ and $\mathbb{P}(Y = 1 \mid \operatorname{do}(X = 0)) = 0.5(0.375) + 0.5(0.25) = 0.3125$, so $\mathrm{ACE} = 0.3125$. The naive comparison understates the effect, because $Z = 1$ makes treatment more likely and recovery less likely.
2. A fraction $r$ of patients has a syndrome ($Z = 1$). Patients without the syndrome take the drug ($X = 1$) with probability $q_1$, those with it with probability $q_2$. The probability of death ($Y = 1$) is $p_1$ ($Z = 0$, $X = 0$), $p_2$ ($Z = 0$, $X = 1$), $p_3$ ($Z = 1$, $X = 0$), $p_4$ ($Z = 1$, $X = 1$). The diagram is $Z \to X$, $Z \to Y$, $X \to Y$. Find $\mathbb{P}(Y = 1 \mid X = 1) - \mathbb{P}(Y = 1 \mid X = 0)$ and the average causal effect, and state and prove the criterion used.

   **Answer** $\mathbb{P}(x, y, z) = \mathbb{P}(z)\,\mathbb{P}(x \mid z)\,\mathbb{P}(y \mid x, z)$, for example $\mathbb{P}(X = 1, Y = 1, Z = 1) = r q_2 p_4$. Then
   $$
   \mathbb{P}(Y = 1 \mid X = 1) = \frac{(1 - r) q_1 p_2 + r q_2 p_4}{(1 - r) q_1 + r q_2}, \qquad
   \mathbb{P}(Y = 1 \mid X = 0) = \frac{(1 - r)(1 - q_1) p_1 + r(1 - q_2) p_3}{(1 - r)(1 - q_1) + r(1 - q_2)}.
   $$
   $Z$ is a parent of $X$, hence satisfies the backdoor criterion, and $\mathrm{ACE} = [(1 - r)p_2 + r p_4] - [(1 - r)p_1 + r p_3]$. The criterion and its proof for this diagram are the first part of the proof of Theorem 12.3.1: the truncated factorization deletes the factor $\mathbb{P}(x \mid z)$, giving $\mathbb{P}(y \mid \operatorname{do}(x)) = \sum_z \mathbb{P}(z)\,\mathbb{P}(y \mid x, z)$.
3. In panel (b) of the figure, list all backdoor paths from $X$ to $Y$ and verify that $\{E\}$, $\{A\}$ and $\{Z\}$ fail the backdoor criterion while $\{A, Z\}$ satisfies it.

   **Answer** The paths are $X \leftarrow Z \to Y$, $X \leftarrow Z \leftarrow A \to Y$, $X \leftarrow E \to Z \to Y$ and $X \leftarrow E \to Z \leftarrow A \to Y$. $\{E\}$ and $\{A\}$ leave $X \leftarrow Z \to Y$ open. $\{Z\}$ blocks the first three ($Z$ is a fork or chain node) but opens the fourth, on which $Z$ is a collider. $\{A, Z\}$ blocks the first three through $Z$ and the fourth through $A$, a fork node; neither is a descendant of $X$.
4. For the front-door diagram, suppose the data are: $\mathbb{P}(X = 1) = 0.5$; among $X = 0$, 60% have $Z = 0$ with cancer rate $0.2$ and 40% have $Z = 1$ with rate $0.5$; among $X = 1$, 20% have $Z = 0$ with rate $0.3$ and 80% have $Z = 1$ with rate $0.6$. Compute the ACE by the front-door formula and compare it with the naive difference.

   **Answer** Inner sums: $z = 0$: $0.5(0.2) + 0.5(0.3) = 0.25$; $z = 1$: $0.5(0.5) + 0.5(0.6) = 0.55$. Then $\mathbb{P}(Y = 1 \mid \operatorname{do}(X = 1)) = 0.2(0.25) + 0.8(0.55) = 0.49$ and $\mathbb{P}(Y = 1 \mid \operatorname{do}(X = 0)) = 0.6(0.25) + 0.4(0.55) = 0.37$, so $\mathrm{ACE} = 0.12$. Naively, $\mathbb{P}(Y = 1 \mid X = 1) = 0.2(0.3) + 0.8(0.6) = 0.54$ and $\mathbb{P}(Y = 1 \mid X = 0) = 0.6(0.2) + 0.4(0.5) = 0.32$, a difference of $0.22$; part of the observed association is due to the unmeasured confounder.
5. Derive the front-door formula with the do-calculus, starting from $\mathbb{P}(y \mid \hat x) = \sum_z \mathbb{P}(y \mid \hat x, z)\,\mathbb{P}(z \mid \hat x)$, for the diagram of panel (c).

   **Answer** (i) $\mathbb{P}(z \mid \hat x) = \mathbb{P}(z \mid x)$ by Rule 2, since $(Z \perp X)_{G_{\underline{X}}}$ (the remaining path $X \leftarrow U \to Y \leftarrow Z$ has the collider $Y$). (ii) $\mathbb{P}(y \mid \hat x, z) = \mathbb{P}(y \mid \hat x, \hat z)$ by Rule 2, since $(Y \perp Z \mid X)_{G_{\overline{X}\underline{Z}}}$. (iii) $\mathbb{P}(y \mid \hat x, \hat z) = \mathbb{P}(y \mid \hat z)$ by Rule 3, since in $G_{\overline{Z}\,\overline{X}}$ the arrows $U \to X$ and $X \to Z$ are removed, $X$ is isolated and $(Y \perp X \mid Z)$ holds. (iv) $\mathbb{P}(y \mid \hat z) = \sum_{x'} \mathbb{P}(y \mid x', \hat z)\,\mathbb{P}(x' \mid \hat z) = \sum_{x'} \mathbb{P}(y \mid x', z)\,\mathbb{P}(x')$, using Rule 2 ($(Y \perp Z \mid X)_{G_{\underline{Z}}}$) and Rule 3 ($(X \perp Z)_{G_{\overline{Z}}}$). Combining gives (12.4).
6. Treatments are given at two times: $X$ at the first visit and $U$ at the second. Between the visits a risk factor $Z$ is measured; $Z$ is affected by $X$ and by an unmeasured health status $H$, which also affects the outcome $Y$; the second treatment $U$ is chosen on the basis of $Z$; and $X$, $Z$, $U$ all affect $Y$. $X$ is randomized. Is $\mathbb{P}(y \mid \operatorname{do}(x), \operatorname{do}(u))$ identifiable? Why does adjusting for $Z$ in the usual way fail?

   **Answer** The arrows are $X \to Z$, $H \to Z$, $H \to Y$, $Z \to U$, and $X, Z, U \to Y$. It is identifiable:
   $$
   \mathbb{P}(y \mid \hat x, \hat u) = \sum_z \mathbb{P}(y \mid x, z, u)\,\mathbb{P}(z \mid x),
   $$
   the g-formula of Robins (1986). Derivation: $\mathbb{P}(y \mid \hat x, \hat u) = \sum_z \mathbb{P}(y \mid \hat x, \hat u, z)\,\mathbb{P}(z \mid \hat x, \hat u)$; $\mathbb{P}(z \mid \hat x, \hat u) = \mathbb{P}(z \mid \hat x)$ by Rule 3 ($U$ is not an ancestor of $Z$) and $= \mathbb{P}(z \mid x)$ by Rule 2 ($X$ has no parents); $\mathbb{P}(y \mid \hat x, \hat u, z) = \mathbb{P}(y \mid \hat x, u, z)$ by Rule 2 (in $G_{\overline{X}\underline{U}}$ the only paths from $U$ to $Y$ go through $Z$ as a chain or fork node), and $= \mathbb{P}(y \mid x, u, z)$ by Rule 2 (in $G_{\underline{X}}$, $X$ is isolated). The naive formula $\sum_z \mathbb{P}(y \mid x, z, u)\,\mathbb{P}(z)$ is wrong: $Z$ is a descendant of $X$ (it lies on the path $X \to Z \to Y$) and a collider on $X \to Z \leftarrow H \to Y$, so it must be weighted by $\mathbb{P}(z \mid x)$, its distribution under the first treatment, and not held at its marginal.
7. Explain why, in a randomized experiment, one should not adjust for a variable measured after treatment, using the language of this chapter.

   **Answer** A post-treatment variable $M$ is a descendant of $X$, so it violates condition 1 of the backdoor criterion. If $M$ lies on a directed path $X \to M \to Y$, adjusting for it blocks part of the effect we want (we would estimate something like a direct effect, and even that incorrectly if $M$ and $Y$ share causes). If $M$ is a common effect of $X$ and some cause of $Y$, $X \to M \leftarrow V \to Y$, conditioning on it opens a spurious path. In a randomized experiment $X$ has no backdoor paths at all, so the empty set already satisfies the criterion and $\mathbb{P}(y \mid \operatorname{do}(x)) = \mathbb{P}(y \mid x)$.
8. In the diagram $X \to Y$ with an unobserved $U$ such that $U \to X$ and $U \to Y$, show by an example that $\mathbb{P}(y \mid \operatorname{do}(x))$ is not determined by $\mathbb{P}(x, y)$.

   **Answer** Take binary variables. Model A: $U$ absent, $X \sim \mathrm{Ber}(1/2)$, $Y = X$. Model B: $U \sim \mathrm{Ber}(1/2)$, $X = U$, $Y = U$ (no effect of $X$). Both give $\mathbb{P}(X = Y = 0) = \mathbb{P}(X = Y = 1) = 1/2$, but $\mathbb{P}(Y = 1 \mid \operatorname{do}(X = 1))$ equals $1$ in model A and $1/2$ in model B. Both models are compatible with the diagram, so the effect is not identifiable.
