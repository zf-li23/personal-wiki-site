---
title: Markov Models of Sequence Evolution
description: "The statistical theory of substitution models: continuous-time Markov chains, the Chapman–Kolmogorov equation and P(t) = exp(Qt), stationarity, time reversibility and the spectral decomposition; transition probabilities of JC69 and K80, the structure of F81, HKY85, TN93 and GTR; three definitions of the transition/transversion ratio; distance estimation by moments and maximum likelihood, the delta-method variance, joint estimation of d and κ, likelihood intervals and the likelihood ratio test, with the human–orangutan 12S rRNA data; saturation and the probability that a distance does not exist; LogDet distances and the limits of pairwise comparison; gamma distances, the discrete gamma, invariable sites, covarion, mixture, partition and nonstationary models; amino acid and RNA models; simulating sequence evolution."
---

The substitution models of [7.8.6](/7.8.6#sec-6.2) turn the comparison of sequences into a statistical problem: a **substitution model** is a continuous-time Markov chain on the nucleotides, its transition probabilities $P(t) = \mathrm{e}^{Qt}$ give the probability of what we see at the tips of a tree, and the table of models from JC69 to GTR, the K80 distance ([Formula 6.2.1](/7.8.6#fml-6.2.1) of 7.8.6) and the JC69 + Γ distance ([Formula 6.2.2](/7.8.6#fml-6.2.2) of 7.8.6) were given there. This chapter supplies the theory behind those formulas. It proves the properties of the Markov chain that phylogenetic methods rely on (stationarity, **time reversibility**, real eigenvalues), derives the transition probabilities of the simplest models, and treats the estimation of a distance between two sequences as a problem of statistical inference, with standard errors, likelihood intervals and tests. It then extends the models in the directions that matter in practice: rates that vary among sites, processes that change across the tree, amino acid and RNA sequences, and the simulation of sequence data. The Markov chains of [7.8.7](/7.8.7) run along a sequence, from one position to the next; the chains here run along time, at each site separately.

The running example, from Yang (2014), is a pair of mitochondrial 12S rRNA genes of human and orangutan, $948$ aligned sites with $90$ differences. The likelihood of a whole tree, built on the same transition probabilities, is the subject of [7.10.21](/7.10.21); Bayesian estimation, starting from the same pair of sequences, of [7.10.22](/7.10.22); and the models for codons of [7.10.23](/7.10.23).

## 20.1. The Substitution Process as a Markov Chain

### 20.1.1. Rate Matrix and Transition Probabilities

The models assume that sites evolve independently and that, at each site, the future of the nucleotide depends on its present state only, not on how it got there. In continuous time this is the following object.

**Definition 20.1.1 (Continuous-Time Markov Chain)** A **continuous-time Markov chain** on a finite state space $S$ is a process $\{X(t), t \ge 0\}$ with values in $S$ such that for all $s, t \ge 0$ and states $i, j$,

$$
\mathbb{P}\bigl(X(s + t) = j \mid X(s) = i, \{X(u), u < s\}\bigr) = \mathbb{P}\bigl(X(s + t) = j \mid X(s) = i\bigr) = p_{ij}(t),
$$
independent of $s$ (time homogeneity). The matrix $P(t) = (p_{ij}(t))$ is its *transition probability matrix*, and its *rate matrix* (generator) $Q = (q_{ij})$ is defined by $P(\Delta t) = I + Q\,\Delta t + o(\Delta t)$: $q_{ij} \ge 0$ for $i \ne j$ is the instantaneous rate of change from $i$ to $j$, and $q_{ii} = -\sum_{j \ne i}q_{ij}$, so that each row of $Q$ sums to zero.

The **Markov chain** of [3.5.9](/3.5.9#def-9.3.1) moves in discrete steps; the continuous-time chain can jump at any moment. The two descriptions are linked by the behavior of a single path: the chain stays in state $i$ for an **exponential distribution** of time with rate $-q_{ii}$ (the only memoryless distribution) and then jumps to $j \ne i$ with probability $q_{ij}/(-q_{ii})$. This *jump chain* description is the basis of simulation (Section 20.6).

**Theorem 20.1.1 (Chapman–Kolmogorov Equation and Matrix Exponential)** The transition matrices of a continuous-time Markov chain satisfy $P(s + t) = P(s)P(t)$ for all $s, t \ge 0$, and

$$
\frac{\mathrm{d}P(t)}{\mathrm{d}t} = P(t)\,Q, \qquad P(0) = I, \qquad\text{so that}\qquad P(t) = \mathrm{e}^{Qt} = \sum_{k=0}^\infty\frac{(Qt)^k}{k!}. \tag{20.1}
$$

**Proof** To go from $i$ to $j$ in time $s + t$, the chain is in some state $k$ at time $s$; by the Markov property and homogeneity, $p_{ij}(s + t) = \sum_kp_{ik}(s)p_{kj}(t)$, which is the matrix product. Taking $t = \Delta t$ small, $P(s + \Delta t) - P(s) = P(s)(P(\Delta t) - I) = P(s)Q\,\Delta t + o(\Delta t)$; dividing by $\Delta t$ gives the differential equation (the forward equation). This linear system with constant coefficients has the unique solution $P(t) = \mathrm{e}^{Qt}$ with $P(0) = I$ ([2.1.11](/2.1.11)). $\square$

The **matrix exponential** is computed, for all branch lengths at once, from one eigendecomposition of $Q$ (Section 20.1.3). Because $Q$ and $t$ enter only through the product $Qt$, rate and time cannot be separated from sequence data without external information (a fossil date, a known mutation rate): $Q$ is scaled so that the mean rate is $1$,

$$
-\sum_i\pi_iq_{ii} = 1, \tag{20.2}
$$
and time is then measured by the distance $d$, the expected number of substitutions per site. This is the branch length of every phylogenetic program.

### 20.1.2. Stationarity and Reversibility

If a sequence has base frequencies $\pi^{(0)}$ (a row vector) at time $0$, its frequencies at time $t$ are $\pi^{(t)} = \pi^{(0)}P(t)$. A distribution $\pi$ with $\pi P(t) = \pi$ for all $t$ is a **stationary distribution**; differentiating at $t = 0$, this is equivalent to

$$
\pi Q = 0, \qquad \sum_i\pi_i = 1, \tag{20.3}
$$
the balance of the total flow $\sum_{i \ne j}\pi_iq_{ij}$ into each state $j$ with the flow $-\pi_jq_{jj}$ out of it. The nucleotide chains used in practice can move from any state to any other, so they are irreducible ([Definition 9.3.3](/3.5.9#def-9.3.3) of 3.5.9); such a chain has a unique stationary distribution, which is also the limit of every row of $P(t)$ as $t \to \infty$. The phylogenetic models assume that the sequences are at stationarity: the root sequence has frequencies $\pi$, and so does every other sequence on the tree.

Most models further assume time reversibility, the **detailed balance condition** of [3.5.9](/3.5.9#thm-9.3.1): $\pi_iq_{ij} = \pi_jq_{ji}$ for all $i, j$, or equivalently $\pi_ip_{ij}(t) = \pi_jp_{ji}(t)$ for all $t$. A stationary reversible chain observed backward in time is the same chain.

**Theorem 20.1.2 (Reversible Rate Matrices)** Let $Q$ be the rate matrix of an irreducible chain and $\Pi = \operatorname{diag}(\pi_1, \dots, \pi_s)$ with $\pi_i > 0$.

1. If $\pi_iq_{ij} = \pi_jq_{ji}$ for all $i, j$, then $\pi$ is the stationary distribution.
2. The detailed balance condition holds if and only if $q_{ij} = r_{ij}\pi_j$ ($i \ne j$) with symmetric $r_{ij} = r_{ji}$, which is the parametrization by exchangeabilities of the **GTR model**.
3. If it holds, $B = \Pi^{1/2}Q\,\Pi^{-1/2}$ is symmetric. Hence $Q$ has real eigenvalues $0 = \lambda_1 > \lambda_2 \ge \dots \ge \lambda_s$ and a basis of eigenvectors.

**Proof** (1) $\sum_i\pi_iq_{ij} = \sum_i\pi_jq_{ji} = \pi_j\sum_iq_{ji} = 0$, since rows of $Q$ sum to zero. (2) Given detailed balance, put $r_{ij} = q_{ij}/\pi_j$; then $r_{ij} = \pi_iq_{ij}/(\pi_i\pi_j) = \pi_jq_{ji}/(\pi_i\pi_j) = r_{ji}$. Conversely $\pi_iq_{ij} = \pi_i\pi_jr_{ij}$ is symmetric in $i$ and $j$. (3) $b_{ij} = \pi_i^{1/2}q_{ij}\pi_j^{-1/2} = (\pi_i\pi_j)^{1/2}r_{ij}$ for $i \ne j$, which is symmetric. A real symmetric matrix has real eigenvalues and an orthonormal basis of eigenvectors, and $Q = \Pi^{-1/2}B\,\Pi^{1/2}$ is similar to it. The eigenvalues are not positive: by Gershgorin's theorem each lies in a disc centered at $q_{ii} \le 0$ with radius $-q_{ii}$. The eigenvalue $0$ (eigenvector $\boldsymbol{1}$) is simple for an irreducible chain, by uniqueness of the stationary distribution. $\square$

Reversibility has a direct consequence for two sequences that diverged from an ancestor $k$ on branches of lengths $t_1$ and $t_2$. The probability of observing $i$ and $j$ is

$$
f_{ij} = \sum_k\pi_kp_{ki}(t_1)p_{kj}(t_2) = \sum_k\pi_ip_{ik}(t_1)p_{kj}(t_2) = \pi_ip_{ij}(t_1 + t_2), \tag{20.4}
$$
using $\pi_kp_{ki} = \pi_ip_{ik}$ and the Chapman–Kolmogorov equation. The data depend on $t_1 + t_2$ only: the root can be anywhere on the path between the sequences, and one sequence could as well be the ancestor of the other. The same argument on a tree is the pulley principle of [Felsenstein's pruning algorithm](/7.8.6#alg-6.5.1), and the reason why reversible models infer unrooted trees ([7.10.21](/7.10.21)).

### 20.1.3. The Spectral Decomposition

With $Q = U\Lambda U^{-1}$, $\Lambda = \operatorname{diag}(\lambda_1, \dots, \lambda_s)$, the power series of Eq. (20.1) gives

$$
P(t) = U\mathrm{e}^{\Lambda t}U^{-1}, \qquad p_{ij}(t) = \sum_{k=1}^su_{ik}u^{-1}_{kj}\mathrm{e}^{\lambda_kt} = \pi_j + \sum_{k=2}^sc_{ijk}\mathrm{e}^{\lambda_kt}. \tag{20.5}
$$
The term for $\lambda_1 = 0$ is the stationary frequency $\pi_j$, and the others decay at rates $-\lambda_k$; the slowest, $\lambda_2$, sets the time scale on which sequences forget their ancestor. For a reversible $Q$ the decomposition is computed stably from the symmetric $B$ of Theorem 20.1.2, $B = V\Lambda V^{\mathsf T}$ with orthogonal $V$, so that $U = \Pi^{-1/2}V$ and $U^{-1} = V^{\mathsf T}\Pi^{1/2}$. One decomposition per model serves all branch lengths of a tree, which is why likelihood programs need only $O(s^3)$ work per update of the model parameters and $O(s^2)$ per branch. Nonreversible matrices may have complex eigenvalues and are handled by other methods (scaling and squaring of the series, or Padé approximation).

## 20.2. Closed-Form Models

### 20.2.1. JC69

In JC69 every change happens at the same rate $\lambda$, so $Q = \lambda(J - 4I)$ with $J$ the $4 \times 4$ matrix of ones. Since $J^2 = 4J$, $\mathrm{e}^{\lambda Jt} = I + \frac{1}{4}(\mathrm{e}^{4\lambda t} - 1)J$, and because $J$ and $I$ commute,

$$
P(t) = \mathrm{e}^{-4\lambda t}\mathrm{e}^{\lambda Jt} = \mathrm{e}^{-4\lambda t}I + \tfrac{1}{4}(1 - \mathrm{e}^{-4\lambda t})J.
$$
The total rate is $3\lambda$, so $d = 3\lambda t$, and

$$
p_{ii}(t) = \frac{1}{4} + \frac{3}{4}\mathrm{e}^{-4d/3}, \qquad p_{ij}(t) = \frac{1}{4} - \frac{1}{4}\mathrm{e}^{-4d/3} \quad (i \ne j). \tag{20.6}
$$
The eigenvalues of $Q$ are $0$ and $-4\lambda$ (three times). The probability that two sequences at distance $d$ differ at a site is $p = 3p_{ij} = \frac{3}{4}(1 - \mathrm{e}^{-4d/3})$, which rises from $0$ with slope $1$ and levels off at $3/4$: inverting it gives the **Jukes–Cantor distance** $d = -\frac{3}{4}\ln(1 - \frac{4}{3}p)$.

### 20.2.2. K80

K80 gives transitions rate $\alpha$ and each of the two transversions rate $\beta$. In the order T, C, A, G, the vectors $(1, 1, 1, 1)$, $(1, 1, -1, -1)$, $(1, -1, 0, 0)$ and $(0, 0, 1, -1)$ are eigenvectors of $Q$ with eigenvalues $0$, $-4\beta$, $-2(\alpha + \beta)$ and $-2(\alpha + \beta)$: the second contrasts pyrimidines with purines and decays only by transversions, the last two contrast the two bases within a class and decay by both kinds of change. With $d = (\alpha + 2\beta)t$ and $\kappa = \alpha/\beta$, Eq. (20.5) gives three distinct entries of $P(t)$,

$$
\begin{aligned}
p_0(t) &= \tfrac{1}{4} + \tfrac{1}{4}\mathrm{e}^{-4d/(\kappa + 2)} + \tfrac{1}{2}\mathrm{e}^{-2d(\kappa + 1)/(\kappa + 2)} && \text{(no change)},\\
p_1(t) &= \tfrac{1}{4} + \tfrac{1}{4}\mathrm{e}^{-4d/(\kappa + 2)} - \tfrac{1}{2}\mathrm{e}^{-2d(\kappa + 1)/(\kappa + 2)} && \text{(a given transition)},\\
p_2(t) &= \tfrac{1}{4} - \tfrac{1}{4}\mathrm{e}^{-4d/(\kappa + 2)} && \text{(a given transversion)},
\end{aligned} \tag{20.7}
$$
with $p_0 + p_1 + 2p_2 = 1$ (Kimura 1980). The expected proportions of transitional and transversional differences are $\mathbb{E}(S) = p_1$ and $\mathbb{E}(V) = 2p_2$; solving these two equations for $d$ and $\kappa$ gives the K80 distance ([Formula 6.2.1](/7.8.6#fml-6.2.1) of 7.8.6) and $\hat\kappa = 2\ln(1 - 2S - V)/\ln(1 - 2V) - 1$.

### 20.2.3. Unequal Base Frequencies

JC69 and K80 have a symmetric $Q$ and therefore stationary frequencies $\frac{1}{4}$, which real sequences rarely have. The models with free frequencies (the table of [7.8.6](/7.8.6#sec-6.2.2)) have the following structure:

- F81: $q_{ij} = \mu\pi_j$. Then $Q = \mu(\boldsymbol{1}\pi - I)$, and since $(\boldsymbol{1}\pi)^2 = \boldsymbol{1}\pi$, $P(t) = \mathrm{e}^{-\mu t}I + (1 - \mathrm{e}^{-\mu t})\boldsymbol{1}\pi$: a site either has not been hit, or its state has been redrawn from $\pi$. With $B = 1 - \sum_i\pi_i^2$, the probability of a difference is $p = B(1 - \mathrm{e}^{-d/B})$ and the distance is $d = -B\ln(1 - p/B)$; JC69 is the case $B = 3/4$.
- HKY85 combines F81 frequencies with K80 rates: $q_{ij} = \kappa\pi_j$ for transitions and $\pi_j$ for transversions. TN93 gives the two kinds of transitions (T↔C and A↔G) separate rates. Both still have closed-form $P(t)$, because the eigenvectors separate purines and pyrimidines as in K80.
- GTR has six exchangeabilities; its $P(t)$ is computed numerically through Eq. (20.5). For two sequences there is a distance formula: if $F$ is the symmetrized $4 \times 4$ matrix of proportions of site patterns and $\Pi$ the diagonal of its row sums, then by Eq. (20.4) $\Pi^{-1}F = P(d)$, and $\hat d = -\operatorname{tr}\bigl(\Pi\log(\Pi^{-1}F)\bigr)$, with the matrix logarithm.

All these models are reversible ($q_{ij} = r_{ij}\pi_j$ with symmetric $r$). The most general model, with $12$ free rates, is not; it can in principle identify the root, but two sequences rarely contain enough information to estimate it.

### 20.2.4. The Transition/Transversion Rate Ratio

Transitions outnumber transversions in almost all sequences, and their ratio is a basic descriptor of the substitution process. At least three measures are in use, and they are easily confused.

**Definition 20.2.1 (Transition/Transversion Rate Ratio)** The **transition/transversion rate ratio** $\kappa$ is the ratio of the rate of any one transition to the rate of any one transversion in the rate matrix: $\kappa = \alpha/\beta$ in K80, the factor $\kappa$ in HKY85. It is distinguished from:

- the *observed ratio* $S/V$ of transitional to transversional differences between two sequences, the **transition/transversion ratio** (Ti/Tv) of variant call sets ([7.8.12](/7.8.12#def-12.5.2)), uncorrected for multiple hits;
- the *average ratio* $R$ of the expected numbers of transitional and transversional substitutions, $R = \sum_{\text{ts}}\pi_iq_{ij}\big/\sum_{\text{tv}}\pi_iq_{ij}$, which is $\kappa/2$ under K80.

With no rate difference, $\kappa = 1$ but $R = 1/2$, because each nucleotide has one transition partner and two transversion partners. $\kappa$ is the natural parameter for a test of no difference ($\kappa = 1$ is the JC69 null), while $R$ can be compared across models whose $\kappa$ means different things (in F84, the corresponding parameter is $0$ without a difference). The observed ratio is a poor measure except for very similar sequences: under K80 its expectation $p_1/(2p_2)$ starts at $\kappa/2$ and decays to $1/2$ as divergence grows, whatever $\kappa$ is.

![Transition probabilities under JC69 and K80 and the observed transition/transversion ratio. A: under K80 with κ = 5, the probability p₀ that the two sequences have the same nucleotide, p₁ that they differ by a transition and 2p₂ that they differ by a transversion, against the distance d; dashed: the JC69 probabilities of no difference and of a difference. Transitional differences accumulate first and then saturate at 1/4, while transversional differences keep rising to 1/2. B: the expected observed ratio E(S)/E(V) = p₁/(2p₂) for κ = 1, 2, 5 and 10; it equals κ/2 for very similar sequences (dots) and decays toward 1/2 at saturation, so it measures the rate ratio only at small distances](./plots/ts-tv-ratio.py)

## 20.3. Estimating Distances

### 20.3.1. Moments, Likelihood and the Delta Method

For two sequences under JC69 the data reduce to the number $x$ of differing sites out of $n$, a binomial count with success probability $p(d) = \frac{3}{4}(1 - \mathrm{e}^{-4d/3})$. Two estimators coincide here. The method of moments equates $p(d)$ to the observed $\hat p = x/n$; maximum likelihood maximizes

$$
\ell(d) = x\ln\bigl(\tfrac{1}{4}p_{ij}(d)\bigr) + (n - x)\ln\bigl(\tfrac{1}{4}p_{ii}(d)\bigr), \tag{20.8}
$$
and since $p$ is a one-to-one function of $d$, the **maximum likelihood estimation** of $d$ is the transform of the binomial estimate $\hat p$ (invariance of the MLE), which is the Jukes–Cantor distance. Its variance follows from the **delta method** ([Theorem 14.4.3](/3.1.14#thm-14.4.3) of 3.1.14),

$$
\operatorname{Var}(\hat d) \approx \operatorname{Var}(\hat p)\Bigl(\frac{\mathrm{d}d}{\mathrm{d}p}\Bigr)^2 = \frac{\hat p(1 - \hat p)}{n}\cdot\frac{1}{(1 - \frac{4}{3}\hat p)^2}, \tag{20.9}
$$
the same as the inverse of the **Fisher information** of $d$ (Kimura and Ohta 1972). The factor $(1 - \frac{4}{3}p)^{-2}$ is the price of correcting for multiple hits: at small distances the standard error is that of a proportion, but it grows without bound as $p$ approaches $3/4$.

**Example 20.3.1** In the 12S rRNA genes of human and orangutan, $x = 90$ of $n = 948$ sites differ: $\hat p = 0.0949$, $\hat d = -\frac{3}{4}\ln(1 - \frac{4}{3}\times0.0949) = 0.1015$, and Eq. (20.9) gives the standard error $0.0109$ and the normal-approximation $95\,\%$ interval $(0.0801, 0.1229)$. The maximized log-likelihood is $\ell(\hat d) = -1710.58$. The likelihood interval, the values of $d$ with $\ell(d) \ge \ell(\hat d) - 1.92$ ($1.92 = \chi^2_{1,0.05}/2$), is $(0.0817, 0.1245)$, slightly asymmetric and shifted to the right: the log-likelihood falls more steeply on the left of the maximum. Unlike the normal interval, the likelihood interval is invariant under reparametrization: computed for $p$ and transformed to $d$, it gives the same endpoints.

### 20.3.2. K80: Joint Estimation of $d$ and $\kappa$

Under K80 the data are the counts $n_S$ and $n_V$ of transitional and transversional differences, a trinomial sample with probabilities $p_1$ and $2p_2$ of Eq. (20.7). The likelihood has two parameters, and again the MLE coincides with the moment estimator because the model has as many parameters as free cell probabilities. The variance of $\hat d$ follows from the multivariate delta method with $\operatorname{Var}(S) = S(1 - S)/n$, $\operatorname{Var}(V) = V(1 - V)/n$ and $\operatorname{Cov}(S, V) = -SV/n$:

$$
\operatorname{Var}(\hat d) = \frac{a^2S + b^2V - (aS + bV)^2}{n}, \qquad a = \frac{1}{1 - 2S - V}, \quad b = \frac{1}{2}\Bigl(\frac{1}{1 - 2S - V} + \frac{1}{1 - 2V}\Bigr). \tag{20.10}
$$

**Example 20.3.2** For the 12S genes, $84$ differences are transitions and $6$ transversions: $S = 0.0886$, $V = 0.0063$. The K80 estimates are $\hat d = 0.1046 \pm 0.0116$ and $\hat\kappa = 30.8$, with standard error $13.1$, and $\ell = -1637.90$. The transition rate is some $30$ times the transversion rate, as is typical of animal mitochondrial DNA, but six transversions determine $\hat\kappa$ only roughly. JC69 is the special case $\kappa = 1$, so the two models are nested and the **likelihood ratio test** applies: $2\Delta\ell = 2(-1637.90 + 1710.58) = 145.3$, compared with $\chi^2_1$ (critical value $3.84$ at $5\,\%$), rejects JC69 overwhelmingly. The distance itself changes little, because at $10\,\%$ divergence there are few multiple hits for the model to correct.

When only $d$ is of interest, $\kappa$ is a **nuisance parameter**; the **profile likelihood** $\ell(d, \hat\kappa_d)$, maximized over $\kappa$ at each fixed $d$ ([3.5.4](/3.5.4)), gives a likelihood interval for $d$ that accounts for the uncertainty in $\kappa$. The estimates of the 12S distance under other models illustrate how little the choice matters at this divergence, and how much the assumption about rate variation does:

| Model | $\hat d$ | Notes |
|---|---|---|
| JC69 | $0.1015$ | $\ell = -1710.58$ |
| F81 (Tajima–Nei formula) | $0.1016$ | $B = 1 - \sum\pi_i^2 = 0.740$ |
| K80 | $0.1046$ | $\hat\kappa = 30.8$, $\ell = -1637.90$ |
| GTR (formula of Section 20.2.3) | $0.1059$ | |
| JC69 + Γ, $\alpha = 0.5$ | $0.1166$ | [Formula 6.2.2](/7.8.6#fml-6.2.2) of 7.8.6 |
| K80 + Γ, $\alpha = 0.5$ | $0.1283$ | $\hat\kappa = 37.8$ (Section 20.4.1) |

### 20.3.3. Saturation

Every distance formula inverts a function that levels off: $p(d)$ under JC69 approaches $3/4$, and the information about $d$ disappears as it does.

**Definition 20.3.1 (Substitution Saturation)** Two sequences are saturated (show **substitution saturation**) when so many substitutions have occurred at each site that their observed differences are close to the proportions expected for unrelated sequences with the same composition; their distance can then no longer be estimated with useful precision.

Saturation shows itself in three ways. The standard error of Eq. (20.9) explodes: with $n = 500$ sites it is $0.04$ at $d = 0.5$ and $0.3$ at $d = 2$, and the delta method itself becomes unreliable. The estimate may not exist: if $\hat p \ge 3/4$, the distance formula gives infinity, and for long true distances this happens with substantial probability (Figure). And the estimate is biased upward, because $d(p)$ is convex. In real data the problem appears at smaller distances than these numbers suggest, since rate variation (Section 20.4) concentrates the changes on a few fast sites that saturate early while the others carry little information. The practical rules follow: fast-evolving genes resolve recent divergences and slow genes (or proteins) deep ones; saturated third codon positions are often removed or recoded for deep phylogenies.

![Sampling properties of the JC69 distance. A: log-likelihood of the distance for the human and orangutan mitochondrial 12S rRNA genes (90 differences at 948 sites; data from Yang (2014), Table 1.3); the 95 % likelihood interval, where the log-likelihood is within 1.92 of its maximum, is asymmetric and shifted to the right of the normal interval obtained from the delta-method standard error. B: the standard deviation of the estimated distance among 20 000 simulated pairs of sequences (dots, finite estimates only) and the delta-method standard error (lines) against the true distance, for 500 and 2000 sites; the approximation holds at moderate distances and underestimates the spread as saturation approaches. C: the probability that the estimate is infinite because the observed proportion of differences is at least 3/4, for 100, 500 and 2000 sites](./plots/jc-sampling.py)

### 20.3.4. Nonstationary Composition and LogDet Distances

All models above assume one stationary process. When base composition differs among lineages (for example a GC-rich thermophile and an AT-rich endosymbiont), distances computed under them are biased toward grouping sequences of similar composition, an artifact that is a form of **long-branch attraction**. The *LogDet distance* (Lockhart and colleagues 1994; in the normalized form of the *paralinear distance*, Lake 1994) is designed for this case. If $F$ is the $4 \times 4$ matrix of proportions of site patterns (not symmetrized) with row and column sums $f^{(1)}$ and $f^{(2)}$,

$$
d_{\mathrm{LD}} = -\frac{1}{4}\Bigl[\ln\det F - \frac{1}{2}\sum_i\bigl(\ln f^{(1)}_i + \ln f^{(2)}_i\bigr)\Bigr].
$$
Because the determinant of a product of matrices is the product of determinants, this distance is additive along a tree for any Markov process with a general transition matrix on each branch, stationary or not, as long as the rates are the same at all sites. It equals the JC69 distance for JC69 data; for the 12S genes it is $0.109$. It does not correct for rate variation among sites unless invariable sites are removed first, which limits its use.

### 20.3.5. The Limits of Pairwise Comparison

Distances are the input of distance methods ([7.8.6](/7.8.6#sec-6.3)), but estimating them pair by pair wastes information. Each pair is analyzed as if it were the only one: the parameters of the process ($\kappa$, $\pi$, the gamma shape $\alpha$) are estimated anew from each pair or fixed in advance, although they are common to all sequences; the estimates for different pairs are correlated, since they share branches of the tree, but are treated as independent; and the gamma shape cannot be estimated from two sequences at all, because one pair gives only one observed proportion per kind of difference. A joint analysis of all sequences on a tree by likelihood removes all three problems ([7.10.21](/7.10.21)). Pairwise distances remain useful for large data sets, starting trees and quick summaries.

## 20.4. Rate Variation among Sites

### 20.4.1. Gamma Distances

Sites differ in their rates: the mutation rate varies along the genome, and the strength of **purifying selection** varies with function, so that a catalytic residue barely changes while a third codon position changes often. The standard model draws the relative rate $r$ of each site from a **gamma distribution** with shape $\alpha$ and rate $\alpha$, so that $\mathbb{E}[r] = 1$ and $\operatorname{Var}(r) = 1/\alpha$; branch lengths remain the expected numbers of substitutions per site averaged over sites. A site with rate $r$ evolves along a branch of length $d$ as a site with rate $1$ along a branch of length $rd$. Every transition probability of Eq. (20.5) is a combination of exponentials $\mathrm{e}^{\lambda_kd}$, and the gamma distribution has the Laplace transform

$$
\int_0^\infty\mathrm{e}^{-cr}\frac{\alpha^\alpha}{\Gamma(\alpha)}r^{\alpha - 1}\mathrm{e}^{-\alpha r}\,\mathrm{d}r = \Bigl(1 + \frac{c}{\alpha}\Bigr)^{-\alpha}, \tag{20.11}
$$
so averaging over $r$ replaces each $\mathrm{e}^{\lambda_kd}$ by $(1 - \lambda_kd/\alpha)^{-\alpha}$. Wherever the one-rate distance formula solved for $\ln(y)$, the gamma distance therefore replaces $\ln(y)$ by $-\alpha(y^{-1/\alpha} - 1)$, which tends to $\ln y$ as $\alpha \to \infty$. Under JC69 this gives [Formula 6.2.2](/7.8.6#fml-6.2.2) of 7.8.6; under K80 (Jin and Nei 1990),

$$
\hat d = \frac{\alpha}{2}\Bigl[(1 - 2S - V)^{-1/\alpha} - 1\Bigr] + \frac{\alpha}{4}\Bigl[(1 - 2V)^{-1/\alpha} - 1\Bigr], \qquad \hat\kappa = \frac{2[(1 - 2S - V)^{-1/\alpha} - 1]}{(1 - 2V)^{-1/\alpha} - 1} - 1. \tag{20.12}
$$
For the 12S genes with $\alpha = 0.5$, $\hat d = 0.128$ and $\hat\kappa = 37.8$, against $0.105$ and $30.8$ without rate variation. Ignoring rate variation underestimates both the distance and the transition/transversion ratio, and the underestimation grows with divergence and with the strength of the variation.

### 20.4.2. The Discrete Gamma

On a tree the likelihood of a site is an integral over $r$ of a product of transition probabilities on all branches, which has no closed form. The **discrete gamma model** (Yang 1994) replaces the gamma by $K$ categories of equal probability $1/K$: the category boundaries are the quantiles $b_k$ of the gamma distribution, $\mathbb{P}(r \le b_k) = k/K$, and each category is represented by its mean rate. Because $r\,g(r;\alpha,\alpha)$ is proportional to the gamma density with shape $\alpha + 1$, the category means are

$$
r_k = K\bigl[G(\alpha b_k;\, \alpha + 1) - G(\alpha b_{k-1};\, \alpha + 1)\bigr], \qquad k = 1, \dots, K, \tag{20.13}
$$
with $G(\cdot;\, a)$ the regularized incomplete gamma function, and they average exactly to $1$. The likelihood of site $h$ is the mixture $f(x_h) = \frac{1}{K}\sum_kf(x_h \mid r_k)$, which costs $K$ times the computation of the one-rate model. Four categories approximate the continuous model well for estimating branch lengths and $\alpha$; the shape is estimated jointly with the tree. Once the parameters are estimated, the rate of each site can be estimated by its posterior over the categories, $\mathbb{P}(r_k \mid x_h) \propto f(x_h \mid r_k)/K$, an **empirical Bayes** procedure.

![Gamma rate variation among sites and its discretization. A: gamma densities with mean 1 for shape parameters α = 0.2, 0.5, 1, 2 and 10; for α ≤ 1 the distribution is L-shaped, with most sites nearly invariant and a few evolving fast, while large α approaches a single rate for all sites. B: the discrete gamma for α = 0.5 with K = 4 equiprobable categories; the boundaries are the quartiles of the distribution (dotted lines) and each category is represented by its mean rate (dots), here 0.033, 0.252, 0.820 and 2.894. C: the probability that two sequences differ at a site against the distance, under JC69 with one rate (dashed), with continuous gamma rates of shape 0.5 (line) and with the four-category discrete gamma (dots): rate variation makes the differences saturate much more slowly, and the discrete model follows the continuous one closely](./plots/discrete-gamma.py)

### 20.4.3. Invariable Sites and Covarions

Some sites cannot change at all, because any substitution would be lethal.

**Definition 20.4.1 (Invariable Sites)** The **invariable sites** model ("+I") assumes that a proportion $p_0$ of sites have rate $0$ and the others rates scaled to keep the mean at $1$ (rate $1/(1 - p_0)$ in the one-rate model; a gamma with mean $1/(1 - p_0)$ in the "+I+Γ" model of Gu and colleagues 1995).

The +I+Γ model is the one most often selected by automatic model choice, but it is statistically awkward: a gamma with $\alpha < 1$ already contains many nearly invariant sites, so $p_0$ and $\alpha$ are strongly correlated and hard to estimate separately, and the estimate of $p_0$ falls as more divergent sequences are added (there are fewer constant sites). Its parameters are best not interpreted biologically.

Rate models give each site one rate for the whole tree. Functional constraints, however, change during evolution: a residue that is free to vary in one clade can become essential in another after a change elsewhere in the protein, a pattern called *heterotachy*.

**Definition 20.4.2 (Covarion Model)** A **covarion model** (from "concomitantly variable codons", Fitch 1971) lets each site switch over time between rate classes. In the simplest version (Tuffley and Steel 1998), a site is either "on", evolving under a nucleotide model, or "off", invariable, and switches between the two at rates $s_{01}$ and $s_{10}$; the process is a Markov chain on the $8$ states $\mathrm{T}^+, \dots, \mathrm{G}^+, \mathrm{T}^-, \dots, \mathrm{G}^-$, in which an "off" nucleotide can only become the same nucleotide "on".

Because the observed nucleotide does not reveal whether a site is on or off, the likelihood sums over the hidden on/off states at every vertex, as in a **hidden Markov model** whose hidden state moves along the tree rather than along the sequence. Galtier (2001) extended the idea to switching among discrete gamma categories.

### 20.4.4. Mixture, Partition and Nonhomogeneous Models

Rate variation is one instance of a general strategy, the mixture model: each site belongs to one of several classes with different processes, the class is unknown, and the likelihood of the site averages over the classes. Classes can differ in rate (the gamma and +I), in exchangeabilities, or in stationary frequencies; the profile mixtures for proteins (such as the CAT model and the empirical C10–C60 profiles) give each site class its own amino acid frequencies and capture the fact that a buried site accepts only hydrophobic residues. When it is known in advance which sites behave alike, the classes can instead be fixed.

**Definition 20.4.3 (Partition Model)** A **partition model** divides the sites into predefined partitions (genes, codon positions, stems and loops of an RNA) and gives each partition its own substitution parameters, such as relative rate, $\kappa$, base frequencies and gamma shape, while the partitions share the tree and, usually, proportional branch lengths. Its log-likelihood is the sum over sites of $\ln f(x_h \mid \theta_{I(h)})$, with $I(h)$ the partition of site $h$.

In statistical terms, partitions are fixed effects and mixture classes random effects, and the two can be combined: codon-position partitions with a discrete gamma inside each. The distinction matters for resampling: sites in a mixture model are independent and identically distributed, sites in a partition model are not, so the **bootstrap** should resample within partitions. The most parameter-rich partition model, with nothing shared but the topology, is equivalent to separate analyses with the log-likelihoods summed; the opposite extreme, one model for the concatenated alignment, ignores real heterogeneity. A partitioned analysis of many genes, sometimes with gene-specific topologies, is the standard way of combining loci ([7.10.25](/7.10.25)).

Finally, the process can change across the tree. *Nonhomogeneous* (and nonstationary) models give different branches or clades different stationary frequencies, so that sequences can drift in composition after they diverge from the root (Yang and Roberts 1995; Galtier and Gouy 1998, with one GC-content parameter per branch). They are expensive and parameter-rich, but are the principled remedy for the compositional artifacts that LogDet distances address heuristically, and they can locate the root, since a nonstationary process is not reversible.

## 20.5. Amino Acid and RNA Models, and Testing Models

### 20.5.1. Amino Acid and RNA Models

The theory carries over to $20$ amino acids with a $20 \times 20$ rate matrix, which has $189$ free exchangeabilities and $19$ frequencies in the reversible case, too many to estimate from one alignment. Two approaches exist:

- *Empirical models* estimate the exchangeabilities once from a large database of alignments and use them as fixed: Dayhoff's PAM model (the source of the PAM scoring matrices, [7.8.3](/7.8.3#sec-3.3.2)), JTT, WAG, LG, and specialized matrices such as mtMAM for mammalian mitochondrial proteins. Only the frequencies (often the observed ones, "+F") and the gamma shape are estimated from the data at hand.
- *Mechanistic models* derive the rates from properties of the amino acids or from codon models with a few parameters; they are biologically interpretable but have generally fitted worse than the empirical matrices.

The simplest amino acid model, the Poisson model, is the analogue of JC69: all $19$ changes from an amino acid have the same rate, $p = \frac{19}{20}(1 - \mathrm{e}^{-20d/19})$, so $\hat d = -\frac{19}{20}\ln(1 - \frac{20}{19}\hat p)$, and with gamma rates $\hat d = \frac{19}{20}\alpha[(1 - \frac{20}{19}\hat p)^{-1/\alpha} - 1]$. Under empirical models, distances are found by maximizing the likelihood numerically.

In ribosomal RNA, the two bases of a stem pair change together: a G·C pair becomes A·U by two compensatory changes, with an intermediate (G·U or A·C) that is less stable. Models with $16$ states for the doublets of paired sites capture this, with reduced parameterizations of the $16 \times 16$ rate matrix; the loops, single-stranded and fast-evolving, are modeled as ordinary nucleotides and are often the main source of noise. Codon models, with $61$ states and the ratio of nonsynonymous to synonymous rates, are the subject of [7.10.23](/7.10.23).

### 20.5.2. Testing Substitution Models

The nucleotide models form a nested hierarchy (JC69 ⊂ K80 ⊂ HKY85 ⊂ GTR, with F81 between JC69 and HKY85; each with or without +Γ and +I), so likelihood ratio tests between neighbors (Example 20.3.2) can choose among them. Two technical points arise:

- Models whose null hypothesis lies on the boundary of the parameter space, such as one rate for all sites ($\alpha = \infty$) or $p_0 = 0$, do not give a $\chi^2_1$ statistic; the null distribution is a $50:50$ mixture of $0$ and $\chi^2_1$, so the $5\,\%$ critical value is $2.71$ rather than $3.84$.
- Non-nested models, such as HKY85 + Γ and GTR + I, and long sequences of pairwise tests are better handled by the information criteria AIC and BIC of [7.8.6](/7.8.6#sec-6.5.3) and [3.4.11](/3.4.11).

With long alignments every simple model is rejected; the test of interest is often not whether a model is true but whether its shortcomings affect the conclusions. Tests of the absolute fit of a model, by parametric bootstrap, are in [7.10.21](/7.10.21).

## 20.6. Simulating Sequence Evolution

Simulated data, generated under known trees and models, are how phylogenetic methods are tested and how many of the statistical properties in [7.10.21](/7.10.21) were found; programs such as Seq-Gen and evolver implement the following two algorithms.

**Algorithm 20.6.1 (Simulation by Waiting Times)** To simulate one site along a branch of length $t$ starting in state $i$:

1. Set the clock to $0$.
2. Draw a waiting time from the exponential distribution with rate $-q_{ii}$ and add it to the clock; if the clock exceeds $t$, stop with state $i$.
3. Choose the new state $j \ne i$ with probability $q_{ij}/(-q_{ii})$, set $i \leftarrow j$ and return to step 2.

This is the **Gillespie algorithm** of stochastic chemical kinetics ([4.4.7](/4.4.7)) applied to one molecule with four states. It records the full history of the site, including the multiple hits that the data hide.

**Algorithm 20.6.2 (Simulation by Transition Probabilities)** To simulate an alignment on a tree:

1. Draw the root sequence from the stationary distribution $\pi$ (and, under rate variation, a rate $r_h$ for each site from the gamma or the discrete categories).
2. Visiting the branches from the root to the tips, compute $P(r_ht)$ for each branch of length $t$ and draw the state of the descendant at each site from the row of the ancestral state.
3. Output the states at the tips.

The second algorithm needs one matrix exponential per branch and rate class and one random draw per site and branch, and is the faster for long branches; the first is needed when the history itself is of interest, for example to count the substitutions that occurred, or under models such as covarions where the process is simplest to describe event by event.

![Simulating a continuous-time Markov chain of nucleotide substitution, here HKY85 with κ = 5 and stationary frequencies T 0.1, C 0.2, A 0.3, G 0.4, scaled to one expected substitution per unit time. A: histories of six sites started in A along a branch of length 2, simulated by exponential waiting times and jumps; each colored segment is the nucleotide present, each tick a substitution. Some sites change back to A, which a comparison of the end points would not reveal. B: the proportion of 4000 sites started in A that are in each state at time t, simulated by waiting times (dots) or by drawing the end state directly from the row of P(t) (crosses), and the exact transition probabilities (lines). Transitions to G dominate at first; all curves converge to the stationary frequencies (letters at the right)](./plots/simulate-sites.py)

## Summary

| Topic | Key results |
|---|---|
| Markov chain | rate matrix $Q$, rows summing to $0$, exponential holding times (Definition 20.1.1); Chapman–Kolmogorov and $P(t) = \mathrm{e}^{Qt}$ (Theorem 20.1.1); scaling to mean rate $1$, so branch length = expected substitutions per site, Eq. (20.2) |
| Stationarity, reversibility | $\pi Q = 0$, Eq. (20.3); detailed balance ⇔ $q_{ij} = r_{ij}\pi_j$ with symmetric $r$, real eigenvalues via $\Pi^{1/2}Q\Pi^{-1/2}$ (Theorem 20.1.2); two-sequence data depend on $t_1 + t_2$ only, Eq. (20.4) |
| Spectral decomposition | $p_{ij}(t) = \pi_j + \sum_{k \ge 2}c_{ijk}\mathrm{e}^{\lambda_kt}$, Eq. (20.5) |
| Closed forms | JC69 via $J^2 = 4J$, Eq. (20.6); K80 eigenvalues $0, -4\beta, -2(\alpha + \beta)$, Eq. (20.7); F81 $P(t) = \mathrm{e}^{-\mu t}I + (1 - \mathrm{e}^{-\mu t})\boldsymbol{1}\pi$; GTR distance $-\operatorname{tr}(\Pi\log\Pi^{-1}F)$ |
| Ts/tv | $\kappa$ (Definition 20.2.1) vs observed $S/V$ vs average $R = \kappa/2$ under K80 |
| Distance estimation | JC69 MLE = moment estimator; delta-method variance, Eq. (20.9); K80 variance, Eq. (20.10); 12S rRNA: $0.1015 \pm 0.0109$ (JC69), $0.1046 \pm 0.0116$, $\hat\kappa = 30.8$ (K80), LRT $145.3$ (Examples 20.3.1–20.3.2) |
| Saturation | Definition 20.3.1: variance explodes, estimate may not exist ($\hat p \ge 3/4$), upward bias; LogDet distance for nonstationary composition; pairwise analysis wastes information |
| Rate variation | gamma Laplace transform, Eq. (20.11): $\ln y \to -\alpha(y^{-1/\alpha} - 1)$; K80 + Γ, Eq. (20.12); discrete gamma, Eq. (20.13); +I (Definition 20.4.1) correlated with $\alpha$; covarions (Definition 20.4.2); mixtures vs partitions (Definition 20.4.3); nonhomogeneous models |
| Other alphabets | empirical amino acid matrices (PAM, JTT, WAG, LG), Poisson distance; RNA doublet models; codons in 7.10.23 |
| Testing and simulation | LRT for nested models, $50:50$ boundary mixture; AIC/BIC otherwise; waiting-time (Algorithm 20.6.1) and transition-probability (Algorithm 20.6.2) simulation |

## Questions

1. Show that F81 is reversible, find its stationary distribution, and derive its $P(t)$.

   **Answer** $\pi_iq_{ij} = \mu\pi_i\pi_j$ is symmetric, so detailed balance holds with stationary distribution $\pi$ (Theorem 20.1.2). With $E = \boldsymbol{1}\pi$, $Q = \mu(E - I)$ and $E^2 = E$, so $\mathrm{e}^{\mu Et} = I + (\mathrm{e}^{\mu t} - 1)E$ and $P(t) = \mathrm{e}^{-\mu t}I + (1 - \mathrm{e}^{-\mu t})E$.

2. Two sequences of $1000$ sites differ at $300$. Compute the JC69 distance and its standard error.

   **Answer** $\hat d = -\frac{3}{4}\ln(1 - 0.4) = 0.383$; by Eq. (20.9), $\operatorname{SE} = \sqrt{0.3 \times 0.7/1000}\,/\,0.6 = 0.024$, a factor $1/(1 - \frac{4}{3}p) = 1.67$ larger than the standard error $0.0145$ of the p-distance.

3. Under K80, $500$ sites show $S = 0.20$ and $V = 0.10$. Estimate $d$, $\kappa$ and the standard error of $\hat d$.

   **Answer** $1 - 2S - V = 0.5$, $1 - 2V = 0.8$: $\hat d = 0.347 + 0.056 = 0.402$ and $\hat\kappa = 2\ln 0.5/\ln 0.8 - 1 = 5.21$. In Eq. (20.10), $a = 2$, $b = 1.625$, so $\operatorname{Var}(\hat d) = (0.8 + 0.264 - 0.5625^2)/500 = 0.0015$ and $\operatorname{SE} = 0.039$.

4. Why can the gamma shape parameter not be estimated from two sequences, though it can from many sequences on a tree?

   **Answer** Two sequences give one observed proportion (per kind of difference), and $d$ and $\alpha$ enter only through $p(d, \alpha)$: a continuum of pairs fits any $\hat p$. On a tree, strong rate variation produces an excess both of sites constant on all branches and of sites that vary on many branches; the distribution of site patterns therefore identifies $\alpha$.

5. (Open question) A neighbor-joining tree of bacterial 16S rRNA sequences with GC contents from $40\,\%$ to $70\,\%$ places all GC-rich species in one clade. How would you check whether the clade is real?

   **Answer** Recompute the tree with LogDet distances (after removing invariable sites), fit nonhomogeneous models with branch-specific GC content and compare by likelihood or BIC, test compositional homogeneity of the variable sites, try purine/pyrimidine recoding, and check independent markers with less compositional variation. A clade that dissolves under these analyses reflected shared composition, not ancestry.
