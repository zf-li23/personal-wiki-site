---
title: Metropolis–Hastings and Gibbs Sampling
description: Markov chain simulation of posterior distributions; the Metropolis–Hastings algorithm and why its acceptance probability works; independence proposals and the role of heavy tails; random walk Metropolis, the tuning parameter, optimal scaling and adaptation; the two- and K-component Gibbs sampler as a special case of Metropolis–Hastings; Metropolis-within-Gibbs, blocked and collapsed samplers for hierarchical models; warm-up, potential scale reduction and effective sample size.
---

The non-iterative methods of [3.7.9](/3.7.9) (grid sampling, the inverse transform, **rejection sampling** and **importance sampling**) produce independent draws, but they need a proposal that resembles the whole posterior, and in more than a few dimensions such a proposal is rarely available. **Markov chain Monte Carlo** (MCMC) gives up independence to gain generality: it constructs a **Markov chain** $\theta^{(1)},\theta^{(2)},\dots$ that only has to make local moves and whose **stationary distribution** is the posterior $p(\theta\mid y)$. After an initial period the states of the chain are (dependent) draws from the posterior, and averages along the chain estimate posterior expectations. This chapter treats the two basic algorithms, the **Metropolis–Hastings algorithm** and the **Gibbs sampler**, in the form in which they are used in Bayesian models: their implementation, the choice and tuning of proposals, their combination in hierarchical models, and the assessment of convergence.

The theory of Markov chains, stationary distributions, the **detailed balance condition** and the basic limit theorem is in [3.5.9](/3.5.9), where both algorithms are also introduced; we use those results and refer to them by explicit links. The examples revisit models of the earlier chapters: the binomial model with **Jeffreys' prior** ([3.7.2](/3.7.2)), the normal model with a semi-conjugate prior ([3.7.5](/3.7.5), §5.2), and the hierarchical models for rat tumors and for normal group means ([3.7.6](/3.7.6)). Throughout, $p(\theta\mid y)=q(\theta\mid y)/p(y)$, where the unnormalized posterior $q(\theta\mid y)=p(y\mid\theta)p(\theta)$ can be evaluated but the normalizing constant $p(y)$ cannot, and $g(\theta^*\mid\theta)$ is the **proposal distribution**. (In [3.5.9](/3.5.9) the target is written $\tilde\pi$ and the proposal $q$.) As in the previous chapters, $\Gamma(\alpha,\beta)$ and $\mathrm{Inv}\text{-}\Gamma(\alpha,\beta)$ have shape $\alpha$ and rate or scale $\beta$.

## 10.1. The Metropolis–Hastings Algorithm

### 10.1.1. The Algorithm

The algorithm was introduced by Metropolis, Rosenbluth, Rosenbluth, Teller and Teller (1953) for symmetric proposals, in a computation of equations of state in statistical physics, and generalized to arbitrary proposals by Hastings (1970). It is widely regarded as one of the most important contributions to statistical computing.

**Algorithm 10.1.1 (Metropolis–Hastings)** Let $p(\theta\mid y)\propto q(\theta\mid y)$ be the target distribution and $\theta^{(t)}$ the current state. One iteration:

1. propose $\theta^*\sim g(\theta\mid\theta^{(t)})$;
2. accept, $\theta^{(t+1)}=\theta^*$, with probability $\min\{1,r\}$, where
   $$
   r=r\big(\theta^{(t)},\theta^*\big)=\frac{p(\theta^*\mid y)/g(\theta^*\mid\theta^{(t)})}{p(\theta^{(t)}\mid y)/g(\theta^{(t)}\mid\theta^*)}=\frac{q(\theta^*\mid y)\,g(\theta^{(t)}\mid\theta^*)}{q(\theta^{(t)}\mid y)\,g(\theta^*\mid\theta^{(t)})};\tag{10.1}
   $$
3. otherwise stay, $\theta^{(t+1)}=\theta^{(t)}$.

The constant $p(y)$ cancels in $r$, so only the unnormalized posterior is needed. Each factor $p(\theta\mid y)/g(\theta\mid\cdot)$ is an importance ratio (a target density over a proposal density), and $r$ is the ratio of the importance ratios at the proposed and the current point. In practice step 2 is carried out on the log scale: draw $u\sim\mathrm{U}(0,1)$ and accept if $\log u<\log r$, where $\log r$ is a difference of log-likelihoods and log-priors. This avoids underflow, since $q(\theta\mid y)$ for a few hundred observations is often smaller than the smallest positive floating-point number.

Two choices of $g$ cover most applications:

- *independence proposals*, $g(\theta^*\mid\theta^{(t)})=g(\theta^*)$, which ignore the current state (§10.2);
- *symmetric proposals*, $g(\theta^*\mid\theta^{(t)})=g(\theta^{(t)}\mid\theta^*)$ for all $\theta^*,\theta^{(t)}$, for which $r=q(\theta^*\mid y)/q(\theta^{(t)}\mid y)$; this is the original **Metropolis algorithm**, and with $\theta^*=\theta^{(t)}+\varepsilon$ for a symmetric increment $\varepsilon$ it is the **random walk Metropolis** algorithm, the most widely used of all (§10.3).

### 10.1.2. Why It Works

For a continuous parameter the Metropolis–Hastings chain has a transition kernel with two parts: a density for moves to $\theta^*\ne\theta$, and a point mass at $\theta$ for rejections. Write

$$
\alpha(\theta,\theta^*)=\min\big\{1,r(\theta,\theta^*)\big\},\qquad\rho(\theta)=1-\int g(\theta^*\mid\theta)\,\alpha(\theta,\theta^*)\,\mathrm{d}\theta^*,
$$
so that $\rho(\theta)$ is the probability of rejecting at $\theta$ and, for a set $A$,

$$
\mathbb{P}(\theta,A)=\mathbb{P}\big(\theta^{(t+1)}\in A\mid\theta^{(t)}=\theta\big)=\int_Ag(\theta^*\mid\theta)\,\alpha(\theta,\theta^*)\,\mathrm{d}\theta^*+\rho(\theta)\boldsymbol{1}_A(\theta).
$$

**Theorem 10.1.1** The Metropolis–Hastings chain satisfies detailed balance with respect to $p(\theta\mid y)$:

$$
p(\theta\mid y)\,g(\theta^*\mid\theta)\,\alpha(\theta,\theta^*)=p(\theta^*\mid y)\,g(\theta\mid\theta^*)\,\alpha(\theta^*,\theta)\quad\text{for all }\theta,\theta^*.
$$
Consequently $p(\theta\mid y)$ is a stationary distribution of the chain: if $\theta^{(t)}\sim p(\theta\mid y)$, then $\theta^{(t+1)}\sim p(\theta\mid y)$.

**Proof** Write $p(\theta)$ for $p(\theta\mid y)$. Multiplying out the minimum,

$$
p(\theta)\,g(\theta^*\mid\theta)\min\Big\{1,\frac{p(\theta^*)g(\theta\mid\theta^*)}{p(\theta)g(\theta^*\mid\theta)}\Big\}=\min\big\{p(\theta)g(\theta^*\mid\theta),\ p(\theta^*)g(\theta\mid\theta^*)\big\},
$$
which is symmetric in $\theta$ and $\theta^*$; this is detailed balance. For stationarity, let $\theta^{(t)}\sim p$ and $A$ be any set. Then

$$
\mathbb{P}\big(\theta^{(t+1)}\in A\big)=\int\!\!\int_Ap(\theta)g(\theta^*\mid\theta)\alpha(\theta,\theta^*)\,\mathrm{d}\theta^*\,\mathrm{d}\theta+\int_Ap(\theta)\rho(\theta)\,\mathrm{d}\theta.
$$
By detailed balance the first term equals $\int_A\int p(\theta^*)g(\theta\mid\theta^*)\alpha(\theta^*,\theta)\,\mathrm{d}\theta\,\mathrm{d}\theta^*=\int_Ap(\theta^*)\big(1-\rho(\theta^*)\big)\,\mathrm{d}\theta^*$. Adding the second term gives $\int_Ap(\theta)\,\mathrm{d}\theta$. $\square$

This is the continuous counterpart of [Theorem 9.4.1](/3.5.9#thm-9.4.1). Stationarity alone does not guarantee that the chain gets there. If, in addition, the chain can reach every set of positive posterior probability from every starting point (for example, $g(\theta^*\mid\theta)>0$ whenever $p(\theta^*\mid y)>0$, as for a normal random walk) and it is aperiodic (which holds as soon as rejections occur with positive probability), then the distribution of $\theta^{(t)}$ converges to $p(\theta\mid y)$ in total variation, and averages along the chain converge to posterior expectations. These are the general-state-space versions of the basic limit theorem and the ergodic theorem ([Theorem 9.3.3](/3.5.9#thm-9.3.3)); see Tierney (1994).

Why the acceptance probability $\min\{1,r\}$? It is the largest choice compatible with detailed balance.

**Proposition 10.1.1** Let $a(\theta,\theta^*)\in[0,1]$ be any acceptance probability for which the chain "propose from $g$, accept with probability $a$" satisfies detailed balance with respect to $p$. Then $a(\theta,\theta^*)\le\min\{1,r(\theta,\theta^*)\}$ for all $\theta\ne\theta^*$, and the Metropolis–Hastings choice attains this bound.

**Proof** Detailed balance for moves $\theta\to\theta^*$ requires $p(\theta)g(\theta^*\mid\theta)a(\theta,\theta^*)=p(\theta^*)g(\theta\mid\theta^*)a(\theta^*,\theta)$, that is, $a(\theta,\theta^*)=r(\theta,\theta^*)\,a(\theta^*,\theta)$. Since $a(\theta^*,\theta)\le1$, we get $a(\theta,\theta^*)\le r(\theta,\theta^*)$, and $a\le1$ by assumption. For the Metropolis–Hastings choice, one of $r(\theta,\theta^*)$ and $r(\theta^*,\theta)=1/r(\theta,\theta^*)$ is at least $1$, so one of the two acceptance probabilities equals $1$ and the other equals $r$, the largest values allowed. $\square$

Other acceptance rules satisfy detailed balance too, for example Barker's rule $a=r/(1+r)$, but they reject more often. Peskun (1973) showed that, for the same proposal, a reversible chain that moves off its current state more often gives Monte Carlo estimates with smaller asymptotic variance, for every function of $\theta$; in this sense $\min\{1,r\}$ is optimal.

## 10.2. Independence Metropolis–Hastings

### 10.2.1. The Algorithm

With an independence proposal $g(\theta^*\mid\theta^{(t)})=g(\theta^*)$ the ratio (10.1) becomes

$$
r=\frac{q(\theta^*\mid y)/g(\theta^*)}{q(\theta^{(t)}\mid y)/g(\theta^{(t)})}=\frac{w(\theta^*)}{w(\theta^{(t)})},\qquad w(\theta)=\frac{q(\theta\mid y)}{g(\theta)}.
$$
The algorithm is also called the **independence sampler**. The weights $w$ are the unnormalized importance weights of **importance sampling** with proposal $g$ ([3.7.9](/3.7.9)): the chain moves to $\theta^*$ for sure if its weight is larger than the current one, and with probability $w(\theta^*)/w(\theta^{(t)})$ otherwise. A good independence proposal is therefore a good importance sampling proposal: close to the posterior, with heavier tails.

**Example 10.2.1 (Normal–Cauchy Model)** Let $y\mid\theta\sim\mathcal{N}(\theta,1)$ with a standard **Cauchy distribution** as prior, $\theta\sim t_1$. The posterior is not of standard form,

$$
p(\theta\mid y)\propto p(y\mid\theta)p(\theta)\propto\frac{\exp\big(-(y-\theta)^2/2\big)}{1+\theta^2}.
$$
Use the likelihood as proposal, $g(\theta)=\mathcal{N}(\theta\mid y,1)$. Then the likelihood cancels and

$$
r=\frac{\exp\big(-(y-\theta^*)^2/2\big)\big/(1+(\theta^*)^2)}{\exp\big(-(y-\theta^{(t)})^2/2\big)\big/(1+(\theta^{(t)})^2)}\cdot\frac{\exp\big(-(\theta^{(t)}-y)^2/2\big)}{\exp\big(-(\theta^*-y)^2/2\big)}=\frac{1+(\theta^{(t)})^2}{1+(\theta^*)^2},
$$
the ratio of the prior densities. For $y=1$ the posterior is shifted toward $0$ relative to the proposal (the prior pulls it in), but the two overlap well. The chain mixes well, and from the poor starting value $\theta=10$ it escapes in one step: a proposal near the posterior has $r=(1+100)/(1+(\theta^*)^2)>1$ and is accepted.

![Independence Metropolis–Hastings for the normal–Cauchy model with y = 1 and proposal N(1, 1). Left: target posterior density and proposal density. Middle and right: the first 100 iterations from θ = 0 and from the poor starting value θ = 10, with the acceptance rates in the titles.](./plots/independence_mh.py)

### 10.2.2. Heavy Tails

Rejection sampling needs a proposal whose tails dominate those of the target, and importance sampling is efficient only if the weights have finite variance ([3.7.9](/3.7.9)). The independence sampler has the same requirement, for a simple reason. Suppose the chain is at a point $\theta^{(t)}$ in the tail where $p(\theta^{(t)}\mid y)\gg g(\theta^{(t)})$, so that $w(\theta^{(t)})$ is huge. A typical proposal $\theta^*$ comes from the bulk of $g$, where $p(\theta^*\mid y)\approx g(\theta^*)$, and

$$
r=\frac{g(\theta^{(t)})\,p(\theta^*\mid y)}{p(\theta^{(t)}\mid y)\,g(\theta^*)}\approx0.
$$
The chain stays at $\theta^{(t)}$ for a long time. Such points are rarely proposed, but when they are, they are accepted and then hold the chain; the long flat stretches compensate for the rarity of proposals in the tail, so the stationary distribution is right, but the convergence is slow and irregular. When the weights are bounded, convergence is fast from every starting point:

**Theorem 10.2.1** Let $w(\theta)=p(\theta\mid y)/g(\theta)\le M$ for all $\theta$ (normalized densities). Then for every starting distribution $\mu$ of $\theta^{(0)}$ the distribution $\mu_t$ of $\theta^{(t)}$ satisfies

$$
\lVert\mu_t-p(\cdot\mid y)\rVert_{\mathrm{TV}}\le\Big(1-\frac1M\Big)^t,
$$
and in stationarity the acceptance rate is at least $1/M$.

**Proof** Since $w(\theta^{(t)})\le M$, the acceptance probability satisfies $\min\{1,w(\theta^*)/w(\theta^{(t)})\}\ge\min\{1,w(\theta^*)/M\}=w(\theta^*)/M$. Hence, for every $\theta$ and every set $A$,

$$
\mathbb{P}(\theta,A)\ge\int_Ag(\theta^*)\frac{w(\theta^*)}{M}\,\mathrm{d}\theta^*=\frac{p(A\mid y)}{M}.
$$
Put $\varepsilon=1/M$. Then $R=(P-\varepsilon\,p)/(1-\varepsilon)$ is again a transition kernel, and $P=\varepsilon\,p+(1-\varepsilon)R$, where $p$ denotes the kernel that ignores the current state and draws from $p(\cdot\mid y)$. Since $p$ is stationary for $P$, $p=pP=\varepsilon p+(1-\varepsilon)pR$, so $pR=p$. For any initial distribution $\mu$, $\mu P=\varepsilon p+(1-\varepsilon)\mu R$, so $\mu P-p=(1-\varepsilon)(\mu-p)R$, and by induction $\mu_t-p=(1-\varepsilon)^t(\mu-p)R^t$. A transition kernel does not increase total variation distance and $\lVert\mu-p\rVert_{\mathrm{TV}}\le1$, which gives the bound. The acceptance rate in stationarity is $\int p(\theta\mid y)\int g(\theta^*)\min\{1,w(\theta^*)/w(\theta)\}\,\mathrm{d}\theta^*\,\mathrm{d}\theta\ge\int g\,w/M=1/M$. $\square$

The constant $M$ is the same as the envelope constant of rejection sampling with proposal $g$, which accepts with probability exactly $1/M$. Conversely, Mengersen and Tweedie (1996) showed that if $w$ is unbounded, the independence sampler does not converge at a geometric rate. Unbounded weights are exactly the situation of a light-tailed proposal for a heavy-tailed target.

**Example 10.2.2 (Tail Matters)** Let the target be $t_1$ and the proposal $\mathcal{N}(0,1)$. Then $\log w(\theta)=\theta^2/2-\log(1+\theta^2)+\text{const}$ grows without bound. In a run of $1000$ iterations about $86\%$ of the proposals are accepted, yet the trace shows flat stretches at $\theta\approx\pm3$: the probability of leaving a state $\theta$ is $\int g(\theta^*)\min\{1,w(\theta^*)/w(\theta)\}\,\mathrm{d}\theta^*$, which is $0.64$ at $\theta=2$, $0.069$ at $\theta=3.2$ and $0.023$ at $\theta=3.6$, so the chain stays on average $14$ iterations at $3.2$ and $44$ at $3.6$. Values beyond $\pm4$, which have target probability $\mathbb{P}(\lvert t_1\rvert>4)=0.156$, are almost never proposed, and the chain represents them by staying very long at the few that are.

![Tail matters: independence sampler for the t1 target with a standard normal proposal. Left: log p(θ)/g(θ) is unbounded in both tails. Right: 1000 iterations; the chain stays for stretches of many iterations at the rare values near ±3.](./plots/tail_matters.py)

## 10.3. Random Walk Metropolis

### 10.3.1. The Algorithm

With a symmetric proposal, such as $\theta^*\sim\mathcal{N}(\theta^{(t)},v^2)$ in one dimension or $\mathcal{N}(\theta^{(t)},S)$ in several, the proposal densities cancel in (10.1) and

$$
r=\frac{q(\theta^*\mid y)}{q(\theta^{(t)}\mid y)}.
$$
The chain always moves uphill and sometimes downhill: a stochastic version of hill climbing, which explores the posterior instead of converging to its mode.

**Example 10.3.1 (Stochastic Hill Climbing)** Let the target be $\mathcal{N}(0,1)$, the current value $\theta^{(t)}=1$ and the proposal $\theta^*\sim\mathcal{N}(1,1)$. Proposals with $\lvert\theta^*\rvert<1$ increase the density and are always accepted; this happens with probability $\Phi(0)-\Phi(-2)=0.477$. A proposal with $\lvert\theta^*\rvert>1$ is accepted with probability $\exp\big((1-(\theta^*)^2)/2\big)$, which is close to $1$ just outside the interval and tiny far out. Altogether the move from $\theta^{(t)}=1$ is accepted with probability

$$
\int\mathcal{N}(\theta^*\mid1,1)\min\Big\{1,\mathrm{e}^{(1-(\theta^*)^2)/2}\Big\}\,\mathrm{d}\theta^*=0.710.
$$

:::

In the normal–Cauchy model of Example 10.2.1 the random walk proposal $\mathcal{N}(\theta^{(t)},v^2)$ gives $r=p(y\mid\theta^*)p(\theta^*)/\big(p(y\mid\theta^{(t)})p(\theta^{(t)})\big)$; the scale $v$ (for example $v=1$) must be chosen by the user.

### 10.3.2. The Tuning Parameter

The proposal scale is a **tuning parameter**: it does not affect the stationary distribution but determines how fast the chain explores it. Suppose the proposal is symmetric with scale $v$ and $\theta^{(t)}$ is (approximately) distributed according to $p(\theta\mid y)$.

- If $v\approx0$, then $\theta^*\approx\theta^{(t)}$ and $r\approx1$: almost all proposals are accepted, but the chain moves in tiny steps, and successive states are highly correlated.
- If $v\to\infty$, then $\theta^*$ is usually far from the mass of the posterior, $q(\theta^*\mid y)\approx0$ and $r\approx0$: almost all proposals are rejected, and the chain stays put for long stretches.

Both extremes are inefficient, so there is an optimal scale in between. A high acceptance rate is not a goal in itself.

![Random walk Metropolis for the normal–Cauchy model with y = 1, started at θ = 0, with proposals N(θ(t), v²). With v = 0.1 almost every proposal is accepted but the chain moves slowly; with v = 10 most are rejected and the trace is flat for long stretches; v = 2.4 mixes well.](./plots/rw_tuning.py)

For a normal target the acceptance rate can be computed exactly.

**Proposition 10.3.1** Let the target be $\mathcal{N}(\mu,\sigma^2)$ and the proposal $\theta^*=\theta^{(t)}+\ell\sigma Z$ with $Z\sim\mathcal{N}(0,1)$. In stationarity the acceptance rate of random walk Metropolis is

$$
\bar a(\ell)=\frac2\pi\arctan\frac2\ell.
$$

**Proof** Standardize, so that $\mu=0$, $\sigma=1$, and let $X=\theta^{(t)}\sim\mathcal{N}(0,1)$, $Y=X+\ell Z$, with density $p$ of the target. The acceptance rate is $\mathbb{E}\min\{1,p(Y)/p(X)\}$. On the event $\{p(Y)\ge p(X)\}$ the integrand is $1$. On the complement, the contribution is $\int\!\!\int_{p(y)<p(x)}p(y)\,\phi_\ell(y-x)\,\mathrm{d}x\,\mathrm{d}y$, where $\phi_\ell$ is the symmetric density of $\ell Z$; renaming $x\leftrightarrow y$ and using $\phi_\ell(y-x)=\phi_\ell(x-y)$, it equals $\mathbb{P}\big(p(Y)>p(X)\big)$. Hence the acceptance rate is $2\,\mathbb{P}\big(p(Y)>p(X)\big)=2\,\mathbb{P}(Y^2<X^2)$. Now $Y^2-X^2=\ell Z(2X+\ell Z)$, and $(Z,\,2X+\ell Z)$ is bivariate normal with correlation $c=\ell/\sqrt{4+\ell^2}$. For a centered bivariate normal pair, $\mathbb{P}(UV<0)=\frac12-\frac1\pi\arcsin c$. Therefore

$$
\bar a(\ell)=1-\frac2\pi\arcsin\frac{\ell}{\sqrt{4+\ell^2}}=1-\frac2\pi\arctan\frac\ell2=\frac2\pi\arctan\frac2\ell.\qquad\square
$$

The acceptance rate decreases from $1$ to $0$ as $\ell$ grows. The efficiency, measured by the **effective sample size** per iteration (§10.6.3), is maximal near $\ell\approx2.4$, where $\bar a=0.44$. For high-dimensional targets there is a general result on *optimal scaling*:

**Theorem 10.3.1 (Roberts, Gelman and Gilks, 1997)** Let the target be a product of $d$ identical smooth one-dimensional densities, and use the proposal $\theta^*\sim\mathcal{N}_d\big(\theta^{(t)},(\ell^2/d)I_d\big)$ in standardized coordinates. As $d\to\infty$, each coordinate of the suitably sped-up chain converges to a diffusion whose speed is maximized at $\ell\approx2.38$, at which the acceptance rate is $0.234$.

For a normal target $\mathcal{N}_d(\boldsymbol{\mu},\Sigma)$ the same result holds after the linear transformation that makes $\Sigma$ the identity, so the recommended proposal is

$$
\theta^*\sim\mathcal{N}_d\Big(\theta^{(t)},\ \frac{2.4^2}{d}\operatorname{Var}(\theta\mid y)\Big),
$$
with acceptance rate about $44\%$ for $d=1$, decreasing to about $23\%$ as $d\to\infty$. Two points matter: the scale shrinks like $1/\sqrt d$, so that random walk Metropolis needs of the order of $d$ iterations per effectively independent draw, and the shape of the proposal should match the posterior covariance, not just its scale.

![Random walk Metropolis for a N(0, 1) target with normal proposals of scale l. Left: exact acceptance rate (2/π) arctan(2/l); the dotted lines mark l = 2.4 and the acceptance rate 0.44. Right: effective sample size per iteration estimated from chains of 40000 iterations, which peaks near l = 2.4.](./plots/rw_scaling.py)

### 10.3.3. Example: The Binomial Model

**Example 10.3.2 (Binomial Model)** Let $y\mid\theta\sim\mathrm{Bin}(n,\theta)$ with the Jeffreys prior $\theta\sim\mathrm{Beta}(\frac12,\frac12)$ ([3.7.2](/3.7.2)). The posterior is

$$
p(\theta\mid y)\propto\theta^{y-1/2}(1-\theta)^{n-y-1/2}\,\boldsymbol{1}\{0<\theta<1\},
$$
which is $\mathrm{Beta}(y+\frac12,n-y+\frac12)$, so the result can be checked. Use the random walk proposal $\theta^*\sim\mathcal{N}(\theta^{(t)},0.4^2)$ and accept with probability $\min\{1,r\}$,

$$
r=\frac{(\theta^*)^{y-1/2}(1-\theta^*)^{n-y-1/2}\,\boldsymbol{1}\{0<\theta^*<1\}}{(\theta^{(t)})^{y-1/2}(1-\theta^{(t)})^{n-y-1/2}\,\boldsymbol{1}\{0<\theta^{(t)}<1\}}.
$$
Proposals outside $(0,1)$ have $r=0$ and are rejected, which is correct: the proposal is still symmetric, and the target is zero there. With artificial data $n=10$, $y=3$, starting value $\theta^{(1)}=0.5$ and $K=10\,000$ iterations:

```r
n <- 10; y <- 3
log_q <- function(theta) {
  if (theta <= 0 || theta >= 1) return(-Inf)
  (y - 0.5) * log(theta) + (n - y - 0.5) * log(1 - theta)
}
K <- 10000
samps <- numeric(K); samps[1] <- 0.5
for (t in 1:(K - 1)) {
  cand <- rnorm(1, samps[t], 0.4)
  if (log(runif(1)) < log_q(cand) - log_q(samps[t])) {   # compare log(r) with log(u)
    samps[t + 1] <- cand
  } else {
    samps[t + 1] <- samps[t]
  }
}
length(unique(samps))/K   # acceptance rate
```

Accepted values of a continuous proposal are distinct with probability $1$, so the number of distinct values counts the acceptances. The acceptance rate is about $0.37$–$0.38$, a little below the $0.44$ of Proposition 10.3.1 because the posterior standard deviation is $0.134$, so the scale $0.4$ corresponds to $\ell\approx3$. The draws have mean $0.319$ and standard deviation $0.132$, against the exact posterior mean $3.5/11=0.318$ and standard deviation $0.134$.

![Random walk Metropolis for the binomial model with n = 10, y = 3 and the Jeffreys prior. Left: the first 1000 iterations. Right: histogram of K = 10000 draws with the exact Beta(3.5, 7.5) posterior density.](./plots/binomial_rw.py)

### 10.3.4. Adapting the Tuning Parameter

The optimal proposal covariance $2.4^2\operatorname{Var}(\theta\mid y)/d$ involves the unknown posterior covariance matrix, which can be estimated from the draws of a preliminary run. This suggests adapting the proposal in rounds.

**Algorithm 10.3.1 (Adaptive Tuning of the Proposal)**

1. Start with a covariance matrix $S_0$ and set $b=0$.
2. Run $M$ iterations of random walk Metropolis with proposal covariance $2.4^2S_b/d$.
3. Set $S_{b+1}$ to the sample covariance matrix of all draws so far.
4. If $b<B$, set $b=b+1$ and return to step 2. Otherwise discard all draws so far and go to step 5.
5. Run $K$ iterations with the fixed proposal covariance $2.4^2S_B/d$; use these draws for inference.

The draws of the adaptation phase are discarded because a chain whose proposal depends on its own past is no longer a Markov chain, and the invariance argument of Theorem 10.1.1 does not apply to it. With the proposal fixed in step 5, the final run is an ordinary Metropolis chain with the correct stationary distribution, however the proposal was found. *Adaptive MCMC* methods that keep adapting forever (Haario, Saksman and Tamminen, 2001) do exist, but they converge to the right distribution only under additional conditions, such as adaptation that diminishes over time (Roberts and Rosenthal, 2009).

**Example 10.3.3 (Normal Model)** Let $y_i\mid\mu,\sigma\overset{\text{iid}}{\sim}\mathcal{N}(\mu,\sigma^2)$ with a flat prior on $\mu$ and a half-Cauchy prior on $\sigma$, $p(\mu,\sigma)\propto\frac{1}{1+\sigma^2}\boldsymbol{1}\{\sigma>0\}$. The posterior

$$
p(\mu,\sigma\mid y)\propto\frac{1}{\sigma^n}\exp\Big(-\frac{1}{2\sigma^2}\Big[\sum_{i=1}^ny_i^2-2\mu n\bar y+n\mu^2\Big]\Big)\frac{1}{1+\sigma^2}\boldsymbol{1}\{\sigma>0\}
$$
is not of standard form. Run random walk Metropolis on $(\mu,\sigma)$ jointly, with proposal $(\mu^*,\sigma^*)\sim\mathcal{N}_2\big((\mu^{(t)},\sigma^{(t)}),\,2.4^2S/2\big)$, and adapt $S$ by Algorithm 10.3.1 with artificial data $n=20$, $y_i\overset{\text{iid}}{\sim}\mathcal{N}(0,1)$, $B=10$, $M=100$, $(\mu^{(1)},\sigma^{(1)})=(0,1)$ and $S_0=I_2$. In our run the acceptance rates of the ten rounds were

$$
0.00,\ 0.98,\ 0.96,\ 0.88,\ 0.61,\ 0.27,\ 0.30,\ 0.26,\ 0.35,\ 0.19.
$$
The initial proposal standard deviation $2.4/\sqrt2=1.7$ is far larger than the posterior standard deviations (about $0.2$ for $\mu$ and $0.15$ for $\sigma$), and in the first round nothing was accepted. The sample covariance of a constant chain is zero, so a small ridge $10^{-6}I_2$ was added to keep $S_1$ positive definite; the second round then took tiny steps, nearly all accepted, and the estimate of the covariance grew with the spread of the draws until it settled. The final $K=10\,000$ iterations have acceptance rate $0.31$, close to the optimum for $d=2$, and the posterior means $\mathbb{E}(\mu\mid y)\approx-0.17$ and $\mathbb{E}(\sigma\mid y)\approx0.91$ are close to the sample mean $\bar y=-0.18$ and standard deviation $s=0.87$, as expected with a flat prior on $\mu$ and a vague prior on $\sigma$. The first round shows that the starting matrix $S_0$ should be on the scale of the posterior, for example from a **normal approximation** at the mode ([3.7.5](/3.7.5)).

![Adaptive random walk Metropolis for the normal model with n = 20 and p(μ, σ) ∝ 1/(1 + σ²). Left and middle: traces of μ and σ during the ten adaptation rounds of 100 iterations (dotted lines). Right: the 10000 draws of the final run.](./plots/normal_adaptive.py)

The same procedure applies to any posterior that can be evaluated pointwise. For the rat tumor model of [3.7.6](/3.7.6) (§6.5), with $y_j\mid\theta_j\sim\mathrm{Bin}(n_j,\theta_j)$, $\theta_j\mid\alpha,\beta\overset{\text{iid}}{\sim}\mathrm{Beta}(\alpha,\beta)$ and $p(\alpha,\beta)\propto(\alpha+\beta)^{-5/2}$, integrating out the $\theta_j$ gives the marginal posterior of the hyperparameters,

$$
p(\alpha,\beta\mid y)\propto\prod_{j=1}^J\frac{\mathrm{B}(\alpha+y_j,\beta+n_j-y_j)}{\mathrm{B}(\alpha,\beta)}\,(\alpha+\beta)^{-5/2}\,\boldsymbol{1}\{\alpha>0,\beta>0\},\tag{10.2}
$$
a two-dimensional target for adaptive random walk Metropolis. Its contours are a long curved ridge in the $(\alpha,\beta)$ plane, so the chain works better on the scale $\big(\log\frac\alpha\beta,\log(\alpha+\beta)\big)$, where the target is closer to normal and unconstrained; the density on that scale includes the Jacobian $\alpha\beta$. Example 10.6.2 compares this sampler with the alternatives of §10.5.

## 10.4. The Gibbs Sampler

The Gibbs sampler was proposed by Geman and Geman (1984) for image restoration, and named after the physicist J. Willard Gibbs because of the analogy between the sampled distributions and the Gibbs distributions of statistical physics. Gelfand and Smith (1990) showed its power for Bayesian computation, and it fundamentally changed the field. The idea is to break a high-dimensional sampling problem into a sequence of low-dimensional ones.

### 10.4.1. The Two-Component Gibbs Sampler

**Algorithm 10.4.1 (Two-Component Gibbs Sampler)** Let $\theta=(\theta_1,\theta_2)$ and suppose we can sample from $p(\theta_1\mid\theta_2,y)$ and $p(\theta_2\mid\theta_1,y)$. Starting from $(\theta_1^{(0)},\theta_2^{(0)})$, iteration $t$ consists of

1. sampling $\theta_1^{(t)}\sim p\big(\theta_1\mid\theta_2^{(t-1)},y\big)$;
2. sampling $\theta_2^{(t)}\sim p\big(\theta_2\mid\theta_1^{(t)},y\big)$.

To run a Gibbs sampler we must derive the **full conditional distribution** of each component, its distribution given everything else. In practice we write down the joint posterior up to a constant, keep the factors that involve the component in question, and recognize the result as a standard distribution.

**Example 10.4.1 (Bivariate Normal with Known Covariance)** Let the target be the **bivariate normal distribution**

$$
\theta\sim\mathcal{N}_2(\boldsymbol{0},\Sigma),\qquad\Sigma=\begin{bmatrix}1&\rho\\\rho&1\end{bmatrix}.
$$
The full conditionals are $\theta_1\mid\theta_2\sim\mathcal{N}(\rho\theta_2,1-\rho^2)$ and $\theta_2\mid\theta_1\sim\mathcal{N}(\rho\theta_1,1-\rho^2)$ ([3.1.15](/3.1.15)), so iteration $t$ draws $\theta_1^{(t)}\sim\mathcal{N}(\rho\theta_2^{(t-1)},1-\rho^2)$ and then $\theta_2^{(t)}\sim\mathcal{N}(\rho\theta_1^{(t)},1-\rho^2)$. Each step moves parallel to a coordinate axis; for $\rho=0.9$ from the starting value $(-3,3)$ the path is a staircase along the narrow ridge of the density (left panel of the figure in §10.5, and [Example 9.5.1](/3.5.9#ex-9.5.1)).

:::

In this example the distribution of the chain can be computed at every iteration.

**Proposition 10.4.1** In Example 10.4.1, for given $\theta_2^{(0)}$ and $t\ge1$,

$$
\begin{bmatrix}\theta_1^{(t)}\\\theta_2^{(t)}\end{bmatrix}\sim\mathcal{N}_2\left(\begin{bmatrix}\rho^{2t-1}\theta_2^{(0)}\\\rho^{2t}\theta_2^{(0)}\end{bmatrix},\begin{bmatrix}1-\rho^{4t-2}&\rho-\rho^{4t-1}\\\rho-\rho^{4t-1}&1-\rho^{4t}\end{bmatrix}\right).
$$
Hence the joint distribution of $(\theta_1^{(t)},\theta_2^{(t)})$ converges to the target as $t\to\infty$, geometrically at rate $\rho^2$.

**Proof** Write $\theta_1^{(t)}=\rho\theta_2^{(t-1)}+\sqrt{1-\rho^2}\,\varepsilon_t$ and $\theta_2^{(t)}=\rho\theta_1^{(t)}+\sqrt{1-\rho^2}\,\eta_t$ with independent standard normal $\varepsilon_t,\eta_t$. Then

$$
\theta_2^{(t)}=\rho^2\theta_2^{(t-1)}+\rho\sqrt{1-\rho^2}\,\varepsilon_t+\sqrt{1-\rho^2}\,\eta_t,
$$
an AR(1) recursion with coefficient $\rho^2$ and innovation variance $(1-\rho^2)(\rho^2+1)=1-\rho^4$. By induction $\theta_2^{(t)}$ is normal with mean $\rho^{2t}\theta_2^{(0)}$ and variance $(1-\rho^4)\sum_{k=0}^{t-1}\rho^{4k}=1-\rho^{4t}$. Next, $\theta_1^{(t)}=\rho\theta_2^{(t-1)}+\sqrt{1-\rho^2}\,\varepsilon_t$ has mean $\rho\cdot\rho^{2t-2}\theta_2^{(0)}=\rho^{2t-1}\theta_2^{(0)}$ and variance $\rho^2(1-\rho^{4t-4})+1-\rho^2=1-\rho^{4t-2}$. Finally $\operatorname{Cov}\big(\theta_1^{(t)},\theta_2^{(t)}\big)=\operatorname{Cov}\big(\theta_1^{(t)},\rho\theta_1^{(t)}\big)=\rho(1-\rho^{4t-2})=\rho-\rho^{4t-1}$. All terms are linear in independent normals, so the vector is bivariate normal. As $t\to\infty$ the mean tends to $\boldsymbol{0}$ and the covariance to $\Sigma$, with errors proportional to $\rho^{2t}$. $\square$

The rate $\rho^2$ is also the lag-1 autocorrelation of each coordinate of the stationary chain. In general, the convergence rate of a two-component Gibbs sampler equals the square of the maximal correlation between $\theta_1$ and $\theta_2$ under the target, that is, the largest correlation between any functions $f(\theta_1)$ and $h(\theta_2)$ (Liu, Wong and Kong, 1994); for the bivariate normal this is $\lvert\rho\rvert$. The stronger the posterior dependence between the components, the slower the convergence, and the more iterations are needed (Example 10.6.1).

### 10.4.2. Example: The Normal Model with a Semi-Conjugate Prior

**Example 10.4.2 (Normal Model with Unknown Mean and Variance)** Let $y_i\mid\mu,\sigma^2\overset{\text{iid}}{\sim}\mathcal{N}(\mu,\sigma^2)$, $i=1,\dots,n$, with independent priors

$$
\mu\sim\mathcal{N}(m,C),\qquad\sigma^2\sim\mathrm{Inv}\text{-}\chi^2(\nu,s^2).
$$
This is not the conjugate prior of [3.7.3](/3.7.3) (there the prior variance of $\mu$ is proportional to $\sigma^2$), and the marginal posteriors are not standard ([3.7.5](/3.7.5), §5.2, treats it on a grid). The joint posterior is

$$
p(\mu,\sigma^2\mid y)\propto(\sigma^2)^{-n/2}\exp\Big(-\frac{1}{2\sigma^2}\sum_{i=1}^n(y_i-\mu)^2\Big)\exp\Big(-\frac{(\mu-m)^2}{2C}\Big)\,(\sigma^2)^{-(\nu/2+1)}\exp\Big(-\frac{\nu s^2}{2\sigma^2}\Big).
$$
*Full conditional of $\mu$.* Keeping the factors that involve $\mu$ and using $\sum_i(y_i-\mu)^2=\sum_i(y_i-\bar y)^2+n(\bar y-\mu)^2$,

$$
p(\mu\mid\sigma^2,y)\propto\exp\Big(-\frac{(\mu-\bar y)^2}{2\sigma^2/n}-\frac{(\mu-m)^2}{2C}\Big)\propto\exp\Big(-\frac12\Big[\Big(\frac{1}{\sigma^2/n}+\frac1C\Big)\mu^2-2\mu\Big(\frac{\bar y}{\sigma^2/n}+\frac mC\Big)\Big]\Big),
$$
so $\mu\mid\sigma^2,y\sim\mathcal{N}(m',C')$ with

$$
C'=\Big(\frac{1}{\sigma^2/n}+\frac1C\Big)^{-1},\qquad m'=C'\Big(\frac{\bar y}{\sigma^2/n}+\frac mC\Big),
$$
the precision-weighted combination of [3.7.2](/3.7.2) (§2.3). *Full conditional of $\sigma^2$.* Keeping the factors that involve $\sigma^2$,

$$
p(\sigma^2\mid\mu,y)\propto(\sigma^2)^{-((\nu+n)/2+1)}\exp\Big(-\frac{1}{2\sigma^2}\Big[\nu s^2+\sum_{i=1}^n(y_i-\mu)^2\Big]\Big),
$$
so $\sigma^2\mid\mu,y\sim\mathrm{Inv}\text{-}\chi^2(\nu',s'^2)$ with $\nu'=\nu+n$ and $\nu's'^2=\nu s^2+\sum_i(y_i-\mu)^2$. Both conditionals are standard, and a draw from the **scaled inverse-chi-square distribution** is $\nu's'^2/X$ with $X\sim\chi^2_{\nu'}$. With $10$ simulated observations from $\mathcal{N}(0,1)$, prior parameters $m=0$, $C=10$, $\nu=1$, $s=1$, starting values $\mu^{(0)}=0$, $\sigma^{2(0)}=1$ and $1000$ iterations:

```r
gibbs_normal <- function(y, m = 0, C = 10, nu = 1, s2 = 1, T = 1000) {
  n <- length(y); ybar <- mean(y)
  mu <- numeric(T + 1); sig2 <- numeric(T + 1)
  mu[1] <- 0; sig2[1] <- 1
  for (t in 2:(T + 1)) {
    Cp <- 1 / (n / sig2[t - 1] + 1 / C)
    mp <- Cp * (n * ybar / sig2[t - 1] + m / C)
    mu[t] <- rnorm(1, mp, sqrt(Cp))                     # mu | sigma^2, y
    sig2[t] <- (nu * s2 + sum((y - mu[t])^2)) / rchisq(1, nu + n)   # sigma^2 | mu, y
  }
  data.frame(mu = mu, sigma2 = sig2)
}
fit <- gibbs_normal(rnorm(10))
```

In our run the sample mean was $\bar y=0.085$, and the chain gave $\mathbb{E}(\mu\mid y)\approx0.086$, a $95\%$ posterior interval $[-0.46,0.66]$ for $\mu$, and $\mathbb{E}(\sigma^2\mid y)\approx0.81$. The vague prior on $\mu$ (variance $10$) hardly shrinks the estimate. The traces show no visible dependence on the starting values: $\mu$ and $\sigma^2$ are nearly independent a posteriori, so the two-component sampler mixes almost as fast as independent sampling.

![Gibbs sampler for the normal model with the semi-conjugate prior μ ~ N(0, 10), σ² ~ Inv-χ²(1, 1) and 10 observations: traces of μ and σ² over 1000 iterations, and the joint draws.](./plots/gibbs_normal.py)

### 10.4.3. The K-Component Gibbs Sampler

**Algorithm 10.4.2 (K-Component Gibbs Sampler)** Let $\theta=(\theta_1,\dots,\theta_K)$, where each $\theta_k$ may be a scalar or a vector. Iteration $t$ consists of the $K$ steps

$$
\begin{aligned}
\theta_1^{(t)}&\sim p\big(\theta_1\mid\theta_2^{(t-1)},\dots,\theta_K^{(t-1)},y\big),\\
\theta_2^{(t)}&\sim p\big(\theta_2\mid\theta_1^{(t)},\theta_3^{(t-1)},\dots,\theta_K^{(t-1)},y\big),\\
&\ \,\vdots\\
\theta_k^{(t)}&\sim p\big(\theta_k\mid\theta_1^{(t)},\dots,\theta_{k-1}^{(t)},\theta_{k+1}^{(t-1)},\dots,\theta_K^{(t-1)},y\big),\\
&\ \,\vdots\\
\theta_K^{(t)}&\sim p\big(\theta_K\mid\theta_1^{(t)},\dots,\theta_{K-1}^{(t)},y\big).
\end{aligned}
$$
Each step conditions on the most recent values of all other components. We write $\theta_{-k}$ for $\theta$ without its $k$-th component, and $p(\theta_k\mid\cdots)$ for $p(\theta_k\mid\theta_{-k},y)$.

**Definition 10.4.1 (Variants of the Gibbs Sampler)** Algorithm 10.4.2, which updates the components in a fixed order, is the **systematic-scan Gibbs sampler**. The **random-scan Gibbs sampler** instead chooses, at each step, a component $k$ at random (for example uniformly) and updates it from $p(\theta_k\mid\theta_{-k},y)$. A **blocked Gibbs sampler** groups several components into one vector and draws the block jointly from its conditional distribution given the rest. A **collapsed Gibbs sampler** integrates some components out of the posterior analytically and runs the sampler on the marginal posterior of the remaining ones; the integrated components, if needed, are drawn afterwards from their conditional distribution.

Blocking and collapsing both reduce the dependence between the components that are updated separately, and therefore usually speed up convergence (Liu, Wong and Kong, 1994). The random scan is easier to analyze, since each step is reversible; the systematic scan is more common in practice.

**Example 10.4.3 (Hierarchical Normal Model)** Let

$$
y_{ij}\mid\mu_i,\sigma^2\overset{\text{iid}}{\sim}\mathcal{N}(\mu_i,\sigma^2),\qquad\mu_i\mid\eta,\tau^2\overset{\text{iid}}{\sim}\mathcal{N}(\eta,\tau^2),\qquad i=1,\dots,I,\ j=1,\dots,n_i,
$$
with $n=\sum_in_i$, a flat prior on $\eta$ and independent inverse-gamma priors on the variances, $p(\eta,\tau^2,\sigma^2)\propto\mathrm{Inv}\text{-}\Gamma(\tau^2\mid a_\tau,b_\tau)\,\mathrm{Inv}\text{-}\Gamma(\sigma^2\mid a_\sigma,b_\sigma)$. (Recall $\mathrm{Inv}\text{-}\chi^2(\nu,s^2)=\mathrm{Inv}\text{-}\Gamma(\nu/2,\nu s^2/2)$, [3.7.2](/3.7.2).) The joint posterior is

$$
p(\mu,\eta,\sigma^2,\tau^2\mid y)\propto\prod_{i=1}^I\prod_{j=1}^{n_i}\mathcal{N}(y_{ij}\mid\mu_i,\sigma^2)\prod_{i=1}^I\mathcal{N}(\mu_i\mid\eta,\tau^2)\,\mathrm{Inv}\text{-}\Gamma(\tau^2\mid a_\tau,b_\tau)\,\mathrm{Inv}\text{-}\Gamma(\sigma^2\mid a_\sigma,b_\sigma),
$$
and each full conditional keeps only the factors that contain the component:

- $\mu_i$ appears in the $n_i$ data factors of group $i$ and in $\mathcal{N}(\mu_i\mid\eta,\tau^2)$. As in Example 10.4.2, with $\bar y_i=\frac1{n_i}\sum_jy_{ij}$,
  $$
  \mu_i\mid\cdots\sim\mathcal{N}\bigg(\Big(\frac{n_i}{\sigma^2}+\frac1{\tau^2}\Big)^{-1}\Big(\frac{n_i\bar y_i}{\sigma^2}+\frac{\eta}{\tau^2}\Big),\ \Big(\frac{n_i}{\sigma^2}+\frac1{\tau^2}\Big)^{-1}\bigg),
  $$
  and the $\mu_i$ are conditionally independent given $(\eta,\sigma^2,\tau^2,y)$, so $p(\mu\mid\eta,\sigma^2,\tau^2,y)=\prod_{i=1}^Ip(\mu_i\mid\eta,\sigma^2,\tau^2,y)$.
- $\eta$ appears only in $\prod_i\mathcal{N}(\mu_i\mid\eta,\tau^2)$, the likelihood of $I$ observations $\mu_i$ with mean $\eta$; with the flat prior, $\eta\mid\cdots\sim\mathcal{N}(\bar\mu,\tau^2/I)$, where $\bar\mu=\frac1I\sum_{i=1}^I\mu_i$.
- $\sigma^2\mid\cdots\sim\mathrm{Inv}\text{-}\Gamma\Big(a_\sigma+\frac n2,\ b_\sigma+\frac12\sum_{i=1}^I\sum_{j=1}^{n_i}(y_{ij}-\mu_i)^2\Big)$.
- $\tau^2\mid\cdots\sim\mathrm{Inv}\text{-}\Gamma\Big(a_\tau+\frac I2,\ b_\tau+\frac12\sum_{i=1}^I(\mu_i-\eta)^2\Big)$.

All full conditionals are standard, and by conditional independence the vector $\mu$ is updated as one block: a blocked Gibbs sampler with the three blocks $\mu$, $\eta$ and $(\sigma^2,\tau^2)$ (the two variances are also conditionally independent).

### 10.4.4. Gibbs Sampling as a Special Case of Metropolis–Hastings

**Proposition 10.4.2** The $k$-th step of iteration $t$ of the Gibbs sampler is a Metropolis–Hastings step with target $p(\theta\mid y)$ and the proposal

$$
g_k\big(\theta^*\mid\theta^{(t-1)}\big)=p\big(\theta_k^*\mid\theta_{-k}^{(t-1)},y\big)\,\boldsymbol{1}\big\{\theta_{-k}^*=\theta_{-k}^{(t-1)}\big\},
$$
where $\theta^{(t-1)}$ denotes the current state before the step. Its acceptance ratio is $r\equiv1$, so every proposal is accepted.

**Proof** The proposal changes only the $k$-th component, so $\theta_{-k}^*=\theta_{-k}^{(t-1)}$ and the reverse proposal is $g_k(\theta^{(t-1)}\mid\theta^*)=p(\theta_k^{(t-1)}\mid\theta_{-k}^*,y)=p(\theta_k^{(t-1)}\mid\theta_{-k}^{(t-1)},y)$. By (10.1),

$$
r=\frac{p(\theta^*\mid y)\big/p\big(\theta_k^*\mid\theta_{-k}^{(t-1)},y\big)}{p(\theta^{(t-1)}\mid y)\big/p\big(\theta_k^{(t-1)}\mid\theta_{-k}^{(t-1)},y\big)}=\frac{p\big(\theta_{-k}^{(t-1)}\mid y\big)}{p\big(\theta_{-k}^{(t-1)}\mid y\big)}\equiv1,
$$
since $p(\theta\mid y)/p(\theta_k\mid\theta_{-k},y)=p(\theta_{-k}\mid y)$ for both $\theta^*$ and $\theta^{(t-1)}$, which share the components $\theta_{-k}$. $\square$

So the Gibbs sampler is exactly the Metropolis–Hastings algorithm with proposals that are always accepted (for two components, [Proposition 9.5.1](/3.5.9#prop-9.5.1)). By Theorem 10.1.1 each step leaves $p(\theta\mid y)$ invariant; a full sweep is the composition of $K$ such steps and therefore leaves it invariant too, although the systematic sweep itself is not reversible. Invariance does not imply convergence: if the support of the posterior is, for example, the union of the two squares $(0,1)^2$ and $(2,3)^2$, then from a point in one square no coordinate-wise move can reach the other, and the Gibbs sampler is not irreducible (Question 8). Such failures are rare for posteriors with connected support and positive density, but strong dependence between components causes the slow mixing of Proposition 10.4.1.

## 10.5. Metropolis-within-Gibbs

### 10.5.1. The Algorithm

The Gibbs sampler assumes that every full conditional $p(\theta_k\mid\theta_{-k},y)$ can be sampled directly. When some of them cannot, a single Metropolis–Hastings step targeting that full conditional can be substituted.

**Algorithm 10.5.1 (Metropolis-within-Gibbs)** In iteration $t$, for $k=1,\dots,K$: if $p(\theta_k\mid\theta_{-k},y)$ is a standard distribution, draw $\theta_k^{(t)}$ from it; otherwise propose $\theta_k^*\sim g_k(\cdot\mid\theta_k^{(t-1)})$ and set $\theta_k^{(t)}=\theta_k^*$ with probability $\min\{1,r_k\}$, where

$$
r_k=\frac{p(\theta_k^*\mid\theta_{-k},y)\,g_k(\theta_k^{(t-1)}\mid\theta_k^*)}{p(\theta_k^{(t-1)}\mid\theta_{-k},y)\,g_k(\theta_k^*\mid\theta_k^{(t-1)})}=\frac{p(\theta_k^*,\theta_{-k}\mid y)\,g_k(\theta_k^{(t-1)}\mid\theta_k^*)}{p(\theta_k^{(t-1)},\theta_{-k}\mid y)\,g_k(\theta_k^*\mid\theta_k^{(t-1)})},
$$
and $\theta_k^{(t)}=\theta_k^{(t-1)}$ otherwise. Here $\theta_{-k}$ holds the most recent values of the other components.

The second form of $r_k$ shows that the full conditional need not be normalized: the unnormalized joint posterior, as a function of $\theta_k$ alone, suffices. A single Metropolis–Hastings step is enough; there is no need to iterate it until it converges to the full conditional, because of the following fact.

**Proposition 10.5.1** Let $K_k(\theta_k\to\theta_k';\theta_{-k})$ be a transition kernel on the $k$-th component that, for each fixed $\theta_{-k}$, leaves the full conditional $p(\theta_k\mid\theta_{-k},y)$ invariant. Then the update of $\theta_k$ by $K_k$, with $\theta_{-k}$ unchanged, leaves the joint posterior $p(\theta\mid y)$ invariant.

**Proof** If $\theta\sim p(\theta\mid y)$ and $\theta_k'$ is drawn from $K_k(\theta_k\to\cdot\,;\theta_{-k})$, then $(\theta_k',\theta_{-k})$ has density

$$
\int p(\theta_{-k}\mid y)\,p(\theta_k\mid\theta_{-k},y)\,K_k(\theta_k\to\theta_k';\theta_{-k})\,\mathrm{d}\theta_k=p(\theta_{-k}\mid y)\,p(\theta_k'\mid\theta_{-k},y)=p(\theta_k',\theta_{-k}\mid y).\qquad\square
$$

Exact draws from the full conditional (Gibbs steps), Metropolis–Hastings steps, and rejection sampling steps all leave the full conditional invariant, so they can be mixed freely within one sweep.

**Example 10.5.1 (Bivariate Normal Revisited)** For the target of Example 10.4.1 with $\rho=0.9$ and starting value $(-3,3)$, update $\theta_1$ by a Gibbs step, $\theta_1^{(t)}\sim\mathcal{N}(\rho\theta_2^{(t-1)},1-\rho^2)$, and $\theta_2$ by a random walk Metropolis step with proposal $\theta_2^*\sim\mathcal{N}\big(\theta_2^{(t-1)},2.4^2(1-\rho^2)\big)$ and target $p(\theta_2\mid\theta_1^{(t)},y)=\mathcal{N}(\rho\theta_1^{(t)},1-\rho^2)$. The proposal scale is the optimal one of §10.3.2 for a normal target with standard deviation $\sqrt{1-\rho^2}$, so the acceptance rate of the $\theta_2$ steps should be about $0.44$; in our run of $1000$ iterations it is $0.45$. A rejected $\theta_2$ step leaves the path with a horizontal segment only, and the chain explores the ridge somewhat more slowly than the Gibbs sampler.

![Bivariate normal target with ρ = 0.9 from the starting value (−3, 3) (square). Lines: the first 20 iterations, each consisting of a move in θ1 and a move in θ2; dots: the remaining draws of 1000 iterations. Left: Gibbs sampler. Right: Metropolis-within-Gibbs with a random walk step for θ2.](./plots/mwg_bivariate.py)

### 10.5.2. Example: Hierarchical Normal Model with Half-Cauchy Priors

**Example 10.5.2** In the hierarchical normal model of Example 10.4.3, replace the inverse-gamma priors by half-Cauchy priors on the standard deviations ([3.7.6](/3.7.6), §6.6, mentions such priors for $\tau$ as weakly informative alternatives),

$$
p(\eta,\tau,\sigma)\propto\frac{1}{1+\sigma^2}\boldsymbol{1}\{\sigma>0\}\cdot\frac{1}{1+\tau^2}\boldsymbol{1}\{\tau>0\}.
$$
The full conditionals of $\mu$ and $\eta$ are unchanged. For the variances, the prior on $\sigma$ corresponds to the density $p(\sigma^2)=p(\sigma)\frac{\mathrm{d}\sigma}{\mathrm{d}\sigma^2}\propto\frac{1}{\sigma(1+\sigma^2)}$ of $\sigma^2$, so with $\mathrm{SS}=\sum_i\sum_j(y_{ij}-\mu_i)^2$,

$$
p(\sigma^2\mid\cdots)\propto(\sigma^2)^{-n/2}\mathrm{e}^{-\mathrm{SS}/(2\sigma^2)}\cdot(\sigma^2)^{-1/2}\frac{1}{1+\sigma^2}\propto\mathrm{Inv}\text{-}\Gamma\Big(\sigma^2\Bigm|\frac{n-1}2,\frac{\mathrm{SS}}2\Big)\frac{1}{1+\sigma^2},
$$
and in the same way

$$
p(\tau^2\mid\cdots)\propto\mathrm{Inv}\text{-}\Gamma\Big(\tau^2\Bigm|\frac{I-1}2,\ \frac12\sum_{i=1}^I(\mu_i-\eta)^2\Big)\frac{1}{1+\tau^2}.
$$
(The extra factor $(\sigma^2)^{-1/2}$ is the Jacobian of the change from $\sigma$ to $\sigma^2$: written as a function of $\sigma$, the conditional density of $\sigma$ is proportional to $\sigma^{-n}\mathrm{e}^{-\mathrm{SS}/(2\sigma^2)}/(1+\sigma^2)$, the inverse-gamma kernel with shape $n/2-1$ evaluated at $\sigma^2$, but a draw of $\sigma^2$ must use the shape $(n-1)/2$.) These are not standard densities. A target of the form $\mathrm{Inv}\text{-}\Gamma(\tau^2\mid a,b)\cdot\frac{1}{1+\tau^2}$ can be sampled in several ways:

1. Rejection sampling with proposal $\tau^{*2}\sim\mathrm{Inv}\text{-}\Gamma(a,b)$. Since $\frac{1}{1+\tau^2}\le1$, the envelope constant is $c=1$, and $\tau^{*2}$ is accepted with probability $\frac{\mathrm{Inv}\text{-}\Gamma(\tau^{*2}\mid a,b)/(1+\tau^{*2})}{c\cdot\mathrm{Inv}\text{-}\Gamma(\tau^{*2}\mid a,b)}=\frac{1}{1+\tau^{*2}}$. This gives an exact draw, so the step is a Gibbs step.
2. An independence Metropolis–Hastings step with the same proposal. The importance weight is $w(\tau^2)=1/(1+\tau^2)$, and the move is accepted with probability $\min\Big\{1,\dfrac{1/(1+\tau^{*2})}{1/(1+\tau^{(t)2})}\Big\}$. The weights are bounded, so by Theorem 10.2.1 the step behaves well.
3. A random walk Metropolis step on $\tau$ (or better on $\log\tau$, with the Jacobian), accepting with probability $\min\{1,q(\tau^*\mid\mu,\eta,\sigma,y)/q(\tau^{(t)}\mid\mu,\eta,\sigma,y)\}$.

The first option fails when $\tau^2$ is usually large, since the acceptance probability $1/(1+\tau^{*2})$ is then small; the second never wastes a proposal; the third needs tuning but requires no recognizable kernel at all.

### 10.5.3. Example: The Beta–Binomial Hierarchical Model

**Example 10.5.3 (Rat Tumors)** Recall the hierarchical model of [3.7.6](/3.7.6) (§6.5) for the $J=71$ rat tumor experiments,

$$
y_j\mid\theta_j\overset{\text{ind}}{\sim}\mathrm{Bin}(n_j,\theta_j),\qquad\theta_j\mid\alpha,\beta\overset{\text{iid}}{\sim}\mathrm{Beta}(\alpha,\beta),\qquad p(\alpha,\beta)\propto(\alpha+\beta)^{-5/2}.
$$
A Gibbs sampler on $(\theta_1,\dots,\theta_J,\alpha,\beta)$ needs the $J+2$ full conditionals. The joint posterior is proportional to $\prod_jp(y_j\mid\theta_j)\prod_jp(\theta_j\mid\alpha,\beta)\,p(\alpha,\beta)$, so

$$
p(\theta_i\mid\cdots)\propto\prod_{j=1}^J\theta_j^{y_j}(1-\theta_j)^{n_j-y_j}\,\theta_j^{\alpha-1}(1-\theta_j)^{\beta-1}\propto\theta_i^{\alpha+y_i-1}(1-\theta_i)^{\beta+n_i-y_i-1},
$$
that is, $\theta_i\mid\cdots\sim\mathrm{Beta}(\alpha+y_i,\beta+n_i-y_i)$. For the hyperparameters, only $p(\theta\mid\alpha,\beta)p(\alpha,\beta)$ involves them:

$$
p(\alpha\mid\cdots)\propto\frac{\prod_{j=1}^J\theta_j^{\alpha-1}}{\mathrm{B}(\alpha,\beta)^J}(\alpha+\beta)^{-5/2},\qquad p(\beta\mid\cdots)\propto\frac{\prod_{j=1}^J(1-\theta_j)^{\beta-1}}{\mathrm{B}(\alpha,\beta)^J}(\alpha+\beta)^{-5/2},
$$
which are not known densities. A Metropolis-within-Gibbs sampler draws each $\theta_j$ by a Gibbs step and updates $\alpha$ and $\beta$ by random walk Metropolis steps, for example with proposals $\mathcal{N}(\alpha^{(t-1)},1)$ and $\mathcal{N}(\beta^{(t-1)},1)$, rejecting non-positive proposals. On the log scale the targets are

$$
\begin{aligned}
\log p(\alpha\mid\cdots)&=(\alpha-1)\sum_{j=1}^J\log\theta_j-J\log\mathrm{B}(\alpha,\beta)-\frac52\log(\alpha+\beta)+\text{const},\\
\log p(\beta\mid\cdots)&=(\beta-1)\sum_{j=1}^J\log(1-\theta_j)-J\log\mathrm{B}(\alpha,\beta)-\frac52\log(\alpha+\beta)+\text{const}.
\end{aligned}
$$
Two refinements are available:

- *Blocking.* The $\theta_j$ are conditionally independent given $(\alpha,\beta)$, $p(\theta\mid\alpha,\beta,y)=\prod_jp(\theta_j\mid\alpha,\beta,y_j)$, so the $J$ Gibbs steps for $\theta_1,\dots,\theta_J$ are in fact a single draw of the block $\theta$ from its joint conditional. The sampler above is a blocked Gibbs sampler with blocks $\theta$, $\alpha$, $\beta$.
- *Collapsing.* The $\theta_j$ can be integrated out analytically, which gives the beta-binomial marginal posterior (10.2) of $(\alpha,\beta)$. A collapsed sampler runs Metropolis on $p(\alpha,\beta\mid y)$ only (§10.3.4) and then draws $\theta_j\sim\mathrm{Beta}(\alpha+y_j,\beta+n_j-y_j)$ for each retained draw of $(\alpha,\beta)$. The chain lives in two dimensions instead of $J+2$, and its moves in $(\alpha,\beta)$ are not held back by the current $\theta$: given $71$ values $\theta_j$, the conditional distribution of $\alpha$ is narrow, so the Metropolis-within-Gibbs chain can move $\alpha$ only a little at each step.

:::

Example 10.6.2 compares the three samplers on these data.

## 10.6. Assessing Convergence

Theorem 10.1.1 and Proposition 10.5.1 guarantee the right stationary distribution, and the basic limit theorem guarantees convergence as $t\to\infty$, but not how many iterations are needed. Two problems must be addressed in practice. Early iterations still reflect the starting values; and even after convergence the draws are correlated, so that a chain of length $n$ carries less information than $n$ independent draws. Inference from iterative simulation therefore follows a routine (Gelman et al., 2013): run several chains from dispersed starting values, discard the first part of each, check that the chains have mixed with each other and within themselves, and estimate how many effectively independent draws they provide.

### 10.6.1. Warm-Up and Multiple Chains

The first part of each chain, during which it moves from its starting point into the region where the posterior has its mass, is discarded: the **burn-in**, also called warm-up. A common default is to discard the first half of each chain; in Example 10.3.3 the whole adaptation phase plays this role. To detect a chain that has not yet converged, run $m\ge2$ chains (typically $4$) from starting values dispersed over, or beyond, the plausible range of the posterior, and compare them. A *trace plot* of the draws against the iteration number shows non-convergence directly: chains that have not mixed occupy different regions, trend, or stick (Figure in Example 10.6.2). Agreement of trace plots is necessary but not sufficient: several chains can agree while all missing a distant mode.

Each chain is also split into its first and second halves, giving $2m$ sequences. Within-chain non-stationarity, for example a slow drift, then shows up as disagreement between the two halves of the same chain.

### 10.6.2. Potential Scale Reduction

For a scalar summary $\psi$ (a parameter or a function of the parameters), let $\psi_{ij}$, $i=1,\dots,n$, $j=1,\dots,m$, be the draws of $m$ sequences of length $n$ after warm-up and splitting.

**Definition 10.6.1 (Potential Scale Reduction Factor)** The between-sequence and within-sequence variances are

$$
B=\frac{n}{m-1}\sum_{j=1}^m\big(\bar\psi_{\cdot j}-\bar\psi_{\cdot\cdot}\big)^2,\qquad W=\frac1m\sum_{j=1}^ms_j^2,\qquad s_j^2=\frac1{n-1}\sum_{i=1}^n\big(\psi_{ij}-\bar\psi_{\cdot j}\big)^2,
$$
where $\bar\psi_{\cdot j}=\frac1n\sum_i\psi_{ij}$ and $\bar\psi_{\cdot\cdot}=\frac1m\sum_j\bar\psi_{\cdot j}$. The marginal posterior variance $\operatorname{Var}(\psi\mid y)$ is estimated by the weighted average

$$
\widehat{\operatorname{var}}^+(\psi\mid y)=\frac{n-1}{n}W+\frac1nB,
$$
and the **potential scale reduction factor** is

$$
\hat R=\sqrt{\frac{\widehat{\operatorname{var}}^+(\psi\mid y)}{W}}.
$$

The motivation is the following pair of facts.

**Proposition 10.6.1** Suppose the $m$ sequences are independent and each is stationary with marginal distribution $p(\psi\mid y)$, variance $\sigma^2=\operatorname{Var}(\psi\mid y)$ and sequence mean $\bar\psi_{\cdot j}$. Then

$$
\mathbb{E}\,\widehat{\operatorname{var}}^+=\sigma^2,\qquad\mathbb{E}\,W=\frac{n}{n-1}\Big(\sigma^2-\operatorname{Var}(\bar\psi_{\cdot j})\Big).
$$
In particular $\mathbb{E}\,W<\sigma^2$ whenever $\operatorname{Var}(\bar\psi_{\cdot j})>\sigma^2/n$, as is the case for a positively autocorrelated chain.

**Proof** Let $\mu=\mathbb{E}\psi_{ij}$. Since $\sum_i(\psi_{ij}-\bar\psi_{\cdot j})^2=\sum_i\psi_{ij}^2-n\bar\psi_{\cdot j}^2$,

$$
\mathbb{E}\sum_{i=1}^n(\psi_{ij}-\bar\psi_{\cdot j})^2=n(\sigma^2+\mu^2)-n\big(\operatorname{Var}(\bar\psi_{\cdot j})+\mu^2\big)=n\big(\sigma^2-\operatorname{Var}(\bar\psi_{\cdot j})\big),
$$
which gives $\mathbb{E}s_j^2$ and hence $\mathbb{E}W$. The sequence means $\bar\psi_{\cdot1},\dots,\bar\psi_{\cdot m}$ are independent and identically distributed, so $B/n$, their sample variance, has expectation $\operatorname{Var}(\bar\psi_{\cdot j})$. Therefore $\mathbb{E}\,\widehat{\operatorname{var}}^+=\frac{n-1}{n}\cdot\frac{n}{n-1}\big(\sigma^2-\operatorname{Var}(\bar\psi_{\cdot j})\big)+\operatorname{Var}(\bar\psi_{\cdot j})=\sigma^2$. For a stationary sequence with autocorrelations $\rho_t$ (Proposition 10.6.2 below), $\operatorname{Var}(\bar\psi_{\cdot j})=\frac{\sigma^2}{n}\big[1+2\sum_{t=1}^{n-1}(1-\frac tn)\rho_t\big]$, which exceeds $\sigma^2/n$ when the $\rho_t$ are positive. $\square$

So even in stationarity $W$ underestimates the posterior variance, because each sequence has not yet explored the whole distribution, while $\widehat{\operatorname{var}}^+$ is unbiased. If the starting values are overdispersed, $\widehat{\operatorname{var}}^+$ overestimates the variance until the chains have forgotten them. Hence $\hat R$ tends to be larger than $1$, and it decreases to $1$ as $n\to\infty$; it estimates the factor by which the scale of the current distribution of $\psi$ might shrink if the simulations were continued. Gelman et al. (2013) treat $\hat R<1.1$ as acceptable; more recent practice (Vehtari, Gelman, Simpson, Carpenter and Bürkner, 2021) uses rank-normalized split-$\hat R$ with the stricter threshold $1.01$. A value of $\hat R$ near $1$ is evidence of mixing for the summary $\psi$ only, so it is computed for all parameters of interest.

### 10.6.3. Effective Sample Size

Once the chains have mixed, the precision of a posterior mean estimated from the draws depends on their autocorrelation.

**Proposition 10.6.2** Let $\psi_1,\psi_2,\dots$ be a stationary sequence with variance $\sigma^2$ and autocorrelations $\rho_t=\operatorname{Corr}(\psi_i,\psi_{i+t})$, and $\bar\psi_n=\frac1n\sum_{i=1}^n\psi_i$. Then

$$
\operatorname{Var}(\bar\psi_n)=\frac{\sigma^2}{n}\Big[1+2\sum_{t=1}^{n-1}\Big(1-\frac tn\Big)\rho_t\Big],
$$
and if $\sum_t\lvert\rho_t\rvert<\infty$, then $n\operatorname{Var}(\bar\psi_n)\to\sigma^2\tau$ with $\tau=1+2\sum_{t=1}^\infty\rho_t$.

**Proof** $\operatorname{Var}\big(\sum_{i=1}^n\psi_i\big)=\sum_{i,k}\operatorname{Cov}(\psi_i,\psi_k)=\sigma^2\big[n+2\sum_{t=1}^{n-1}(n-t)\rho_t\big]$, since there are $n-t$ pairs at lag $t$; divide by $n^2$. The limit follows by dominated convergence. $\square$

The factor $\tau$ is the *integrated autocorrelation time*: $n$ correlated draws estimate the mean as precisely as $n/\tau$ independent ones. This is the Markov chain analog of the effective sample size of weighted samples in importance sampling ([3.7.9](/3.7.9)).

**Definition 10.6.2 (Effective Sample Size of MCMC Draws)** For $m$ sequences of length $n$, the effective number of independent draws is

$$
\hat n_{\mathrm{eff}}=\frac{mn}{1+2\sum_{t=1}^T\hat\rho_t},\qquad\hat\rho_t=1-\frac{V_t}{2\,\widehat{\operatorname{var}}^+},\qquad V_t=\frac{1}{m(n-t)}\sum_{j=1}^m\sum_{i=t+1}^n\big(\psi_{ij}-\psi_{i-t,j}\big)^2,
$$
where the sum is truncated at the first odd $T$ for which $\hat\rho_{T+1}+\hat\rho_{T+2}<0$ (sums of adjacent pairs of autocorrelations of a reversible chain are positive, so a negative pair signals noise). The **Monte Carlo standard error** of the posterior mean estimate $\bar\psi_{\cdot\cdot}$ is $\sqrt{\widehat{\operatorname{var}}^+/\hat n_{\mathrm{eff}}}$.

The estimate $\hat\rho_t$ uses the variogram $V_t$, since $\mathbb{E}(\psi_i-\psi_{i-t})^2=2\sigma^2(1-\rho_t)$, and combines the information of all sequences; using $\widehat{\operatorname{var}}^+$ rather than $W$ makes $\hat n_{\mathrm{eff}}$ small when the chains have not mixed. As a rule of thumb, a few hundred effective draws suffice for posterior means and central intervals, and Vehtari et al. (2021) recommend at least about $400$ (for four chains) before trusting $\hat R$ and the Monte Carlo standard errors. Tail quantiles need more. Keeping only every $k$-th draw (thinning) reduces storage, but it never increases the effective sample size of the retained draws compared with keeping all of them.

**Example 10.6.1 (Gibbs Sampler for the Bivariate Normal)** By the proof of Proposition 10.4.1, each coordinate of the stationary Gibbs chain is an AR(1) process with coefficient $\phi=\rho^2$, so $\rho_t=\phi^t$ and

$$
\tau=1+2\sum_{t=1}^\infty\phi^t=\frac{1+\phi}{1-\phi}=\frac{1+\rho^2}{1-\rho^2}.
$$
For $\rho=0.9$, $\tau=9.53$: $1000$ iterations are worth about $105$ independent draws. For $\rho=0.99$, $\tau=99.5$ and $1000$ iterations are worth about $10$.

**Example 10.6.2 (Comparing Samplers for the Rat Tumors)** We run three samplers for the rat tumor posterior of Example 10.5.3, four chains each from the dispersed starting values $(\alpha,\beta)=(1,1),(5,30),(0.5,10),(4,8)$, with $4000$ iterations per chain, and discard the first $1000$:

1. Metropolis-within-Gibbs: a Gibbs (block) step for $\theta$ and random walk steps $\mathcal{N}(\cdot,1)$ for $\alpha$ and $\beta$;
2. a collapsed sampler with the same componentwise random walk steps, applied to $p(\alpha,\beta\mid y)$ in (10.2);
3. a collapsed sampler with a joint random walk on $\big(\log\frac\alpha\beta,\log(\alpha+\beta)\big)$, whose proposal covariance was adapted by Algorithm 10.3.1 ($B=10$, $M=100$).

The split-$\hat R$ and effective sample sizes of $\alpha$ and $\beta$ from the $4\times3000$ retained draws were:

| sampler | $\hat R(\alpha)$ | $\hat n_{\mathrm{eff}}(\alpha)$ | $\hat R(\beta)$ | $\hat n_{\mathrm{eff}}(\beta)$ |
|---|---|---|---|---|
| Metropolis-within-Gibbs | $1.12$ | $41$ | $1.13$ | $40$ |
| collapsed, componentwise | $1.02$ | $79$ | $1.02$ | $73$ |
| collapsed, joint on transformed scale | $1.001$ | $1998$ | $1.001$ | $1914$ |

All three chains have the correct stationary distribution and concentrate around $\alpha\approx2.4$, $\beta\approx14$, but they differ by a factor of about $50$ in efficiency. The Metropolis-within-Gibbs chain has not converged by the criterion $\hat R<1.1$: its moves in $\alpha$ and $\beta$ are limited both by the current $\theta$ and by the strong posterior correlation of $\alpha$ and $\beta$, whose ridge runs along a nearly constant prior mean $\alpha/(\alpha+\beta)\approx0.14$. Collapsing removes the first limitation and doubles the effective sample size; the joint move on the transformed scale, where the posterior is roughly normal, follows the ridge and removes the second. The lesson is general: transform to unconstrained, roughly normal parameters, integrate out what can be integrated analytically, and update strongly dependent parameters jointly.

![Rat tumor example: traces of α for four chains of each sampler, started at dispersed values; the dotted line marks the end of warm-up. Top: Metropolis-within-Gibbs. Middle: collapsed sampler with componentwise random walk steps. Bottom: collapsed sampler with an adapted joint random walk on (log(α/β), log(α + β)). The titles give split-R-hat and the effective sample size of α.](./plots/rats_samplers.py)

## Summary

| Algorithm | Proposal | Acceptance ratio $r$ | Requirements and pitfalls |
|---|---|---|---|
| Metropolis–Hastings (Algorithm 10.1.1) | any $g(\theta^*\mid\theta^{(t)})$ | $\dfrac{q(\theta^*\mid y)\,g(\theta^{(t)}\mid\theta^*)}{q(\theta^{(t)}\mid y)\,g(\theta^*\mid\theta^{(t)})}$ | unnormalized posterior suffices; compute on the log scale |
| independence sampler (§10.2) | $g(\theta^*)$ | $w(\theta^*)/w(\theta^{(t)})$, $w=q/g$ | $g$ needs heavier tails than the posterior; bounded $w\le M$ gives the rate $(1-1/M)^t$ (Theorem 10.2.1) |
| random walk Metropolis (§10.3) | symmetric, $\mathcal{N}(\theta^{(t)},S)$ | $q(\theta^*\mid y)/q(\theta^{(t)}\mid y)$ | tune $S\approx2.4^2\operatorname{Var}(\theta\mid y)/d$, acceptance $0.44$ ($d=1$) to $0.23$; adapt, then fix (Algorithm 10.3.1) |
| Gibbs sampler (§10.4) | full conditional $p(\theta_k\mid\theta_{-k},y)$ | $\equiv1$ (Proposition 10.4.2) | full conditionals must be standard; slow under strong dependence (rate $\rho^2$, Proposition 10.4.1) |
| Metropolis-within-Gibbs (§10.5) | Gibbs steps where possible, MH steps otherwise | $r_k$ with the full conditional as target | each step leaves the posterior invariant (Proposition 10.5.1) |

- Metropolis–Hastings works because of detailed balance (Theorem 10.1.1), and $\min\{1,r\}$ is the largest acceptance probability compatible with it (Proposition 10.1.1). Independence proposals suffer from the same heavy-tail problems as rejection and importance sampling proposals; random walk proposals require tuning, and neither a very high nor a very low acceptance rate is good.
- The Gibbs sampler breaks a high-dimensional sampling problem into low-dimensional full conditionals. If some of them are not standard, use rejection sampling or a Metropolis–Hastings step for those components. Blocking and collapsing (Definition 10.4.1) reduce the dependence between separately updated components; in hierarchical models the group parameters are conditionally independent given the hyperparameters and can often be integrated out (Example 10.5.3).
- Assess convergence with several overdispersed chains, warm-up, trace plots, split-$\hat R$ (Definition 10.6.1) and the effective sample size (Definition 10.6.2); report Monte Carlo standard errors. In the rat tumor example (Example 10.6.2) the choice of sampler changed the effective sample size by a factor of $50$.

## Questions

1. Show that Barker's acceptance probability $a(\theta,\theta^*)=r/(1+r)$, with $r$ as in (10.1), satisfies detailed balance. Compare it with $\min\{1,r\}$ for $r=0.5$ and $r=2$.

   **Answer** Write $p=p(\theta\mid y)$, $p^*=p(\theta^*\mid y)$, $g=g(\theta^*\mid\theta)$, $g^*=g(\theta\mid\theta^*)$, so $r=p^*g^*/(pg)$. Then $p\,g\,\frac{r}{1+r}=p\,g\,\frac{p^*g^*}{pg+p^*g^*}=\frac{pg\,p^*g^*}{pg+p^*g^*}$, which is symmetric in the two points, so detailed balance holds. For $r=0.5$: $\min\{1,r\}=0.5$ and Barker gives $1/3$. For $r=2$: $1$ against $2/3$. Barker's rule always accepts less often, in agreement with Proposition 10.1.1; by Peskun's theorem it gives larger asymptotic variances.
2. Use the independence sampler with proposal $\mathrm{Exp}(\lambda)$ for the target $\mathrm{Exp}(1)$. For which $\lambda$ are the weights bounded? Give the convergence bound of Theorem 10.2.1, and describe the behavior for $\lambda=2$.

   **Answer** $w(\theta)=\mathrm{e}^{-\theta}/(\lambda\mathrm{e}^{-\lambda\theta})=\lambda^{-1}\mathrm{e}^{(\lambda-1)\theta}$, which is bounded on $(0,\infty)$ if and only if $\lambda\le1$, with $M=1/\lambda$. Then $\lVert\mu_t-p\rVert_{\mathrm{TV}}\le(1-\lambda)^t$ and the stationary acceptance rate is at least $\lambda$. For $\lambda=1$ the proposal is the target and every move is accepted. For $\lambda=2$ the proposal has a lighter tail: $w(\theta)=\frac12\mathrm{e}^{\theta}$ is unbounded, and once the chain is at a large $\theta$ it accepts a proposal $\theta^*$ only with probability $\mathrm{e}^{\theta^*-\theta}$, so it stays there for about $\mathrm{e}^{\theta}/\mathbb{E}_g\mathrm{e}^{\theta^*}=\mathrm{e}^{\theta}/2$ iterations; the convergence is not geometric (Mengersen and Tweedie).
3. For a $\mathcal{N}(\mu,\sigma^2)$ target and the random walk proposal $\mathcal{N}(\theta^{(t)},v^2)$, which proposal standard deviation $v$ gives the acceptance rate $0.44$, and which gives $0.234$? In Example 10.3.2, roughly which acceptance rate would you expect with the proposal scale $0.4$?

   **Answer** By Proposition 10.3.1 the acceptance rate is $\frac2\pi\arctan\frac{2\sigma}{v}$. Solving, $v=2\sigma/\tan(\pi\bar a/2)$: for $\bar a=0.44$, $v=2\sigma/\tan(0.691)=2.42\sigma$; for $\bar a=0.234$, $v=5.19\sigma$. The value $0.234$ is the high-dimensional optimum; in one dimension it corresponds to a proposal more than twice as wide as optimal. In Example 10.3.2 the posterior standard deviation is $0.134$, so $\ell=0.4/0.134\approx3.0$ and the formula gives $\frac2\pi\arctan(0.67)\approx0.37$, close to the observed $0.37$–$0.38$ even though the beta posterior is not normal.
4. For the Gibbs sampler of Example 10.4.1, how many iterations are needed for an effective sample size of $1000$ when $\rho=0.5$, $0.9$ and $0.99$? What is the Monte Carlo standard error of the estimate of $\mathbb{E}\theta_1$ after $10\,000$ iterations with $\rho=0.9$?

   **Answer** By Example 10.6.1, $\tau=(1+\rho^2)/(1-\rho^2)$: $\tau=1.67$, $9.53$ and $99.5$, so about $1700$, $9500$ and $99\,500$ iterations are needed. With $\rho=0.9$ and $10\,000$ iterations, $n_{\mathrm{eff}}\approx10\,000/9.53=1050$, and since $\operatorname{Var}\theta_1=1$ the Monte Carlo standard error is $1/\sqrt{1050}\approx0.031$, against $0.010$ for $10\,000$ independent draws.
5. Let $y_j\mid\theta_j\overset{\text{ind}}{\sim}\mathrm{Poi}(\theta_j)$, $\theta_j\mid\beta\overset{\text{iid}}{\sim}\Gamma(\alpha,\beta)$ with $\alpha$ known, and $\beta\sim\Gamma(a,b)$, $j=1,\dots,J$. Derive the full conditionals and describe the Gibbs sampler. Is it a blocked sampler?

   **Answer** The joint posterior is proportional to $\prod_j\theta_j^{y_j}\mathrm{e}^{-\theta_j}\prod_j\frac{\beta^\alpha}{\Gamma(\alpha)}\theta_j^{\alpha-1}\mathrm{e}^{-\beta\theta_j}\,\beta^{a-1}\mathrm{e}^{-b\beta}$. Keeping the factors with $\theta_i$: $\theta_i^{\alpha+y_i-1}\mathrm{e}^{-(\beta+1)\theta_i}$, so $\theta_i\mid\cdots\sim\Gamma(\alpha+y_i,\beta+1)$. Keeping the factors with $\beta$: $\beta^{a+J\alpha-1}\mathrm{e}^{-(b+\sum_j\theta_j)\beta}$, so $\beta\mid\cdots\sim\Gamma(a+J\alpha,b+\sum_j\theta_j)$. Each iteration draws all $\theta_j$ (conditionally independent given $\beta$, hence one block) and then $\beta$: a two-block Gibbs sampler, with no Metropolis steps needed because both conditionals are conjugate.
6. For the normal model with the non-informative prior $p(\mu,\sigma^2)\propto1/\sigma^2$, derive the two full conditionals. Why is a Gibbs sampler unnecessary for this model?

   **Answer** $p(\mu,\sigma^2\mid y)\propto(\sigma^2)^{-n/2-1}\exp\big(-\frac{1}{2\sigma^2}\sum_i(y_i-\mu)^2\big)$. As a function of $\mu$ this is $\exp\big(-\frac{n(\mu-\bar y)^2}{2\sigma^2}\big)$, so $\mu\mid\sigma^2,y\sim\mathcal{N}(\bar y,\sigma^2/n)$. As a function of $\sigma^2$ it is $(\sigma^2)^{-n/2-1}\exp\big(-\frac{1}{2\sigma^2}\sum_i(y_i-\mu)^2\big)$, so $\sigma^2\mid\mu,y\sim\mathrm{Inv}\text{-}\chi^2\big(n,\frac1n\sum_i(y_i-\mu)^2\big)$. But the marginal posterior is known, $\sigma^2\mid y\sim\mathrm{Inv}\text{-}\chi^2(n-1,s^2)$ ([3.7.3](/3.7.3)), so independent draws are obtained directly by drawing $\sigma^2$ from its marginal and then $\mu$ from $\mathcal{N}(\bar y,\sigma^2/n)$. Factorization into a marginal and a conditional is always preferable to an iterative sampler when it is available.
7. Two chains of length $n=100$ (after warm-up) for a parameter $\psi$ have means $1.0$ and $2.0$ and sample variances $1.0$ and $1.2$. Compute $B$, $W$, $\widehat{\operatorname{var}}^+$ and $\hat R$ (without splitting). What do you conclude?

   **Answer** $\bar\psi_{\cdot\cdot}=1.5$, so $B=\frac{100}{1}\big[(1-1.5)^2+(2-1.5)^2\big]=50$, and $W=\frac12(1.0+1.2)=1.1$. Then $\widehat{\operatorname{var}}^+=\frac{99}{100}\cdot1.1+\frac{50}{100}=1.589$ and $\hat R=\sqrt{1.589/1.1}=1.20$. The two chains disagree by about one within-chain standard deviation; they have not mixed, and the simulations must be continued (or the sampler improved) before any summary of $\psi$ is reported.
8. Let the target be uniform on the union of the open squares $(0,1)^2$ and $(2,3)^2$. Show that the Gibbs sampler is not irreducible. Give two ways to repair it.

   **Answer** If $\theta=(\theta_1,\theta_2)\in(0,1)^2$, then the full conditional of $\theta_1$ given $\theta_2\in(0,1)$ is uniform on $(0,1)$, since the line $\{\theta_2=\text{const}\}$ meets only the first square; likewise for $\theta_2$. So every step stays in the first square, and the second square, which has probability $\frac12$, is never reached: the stationary distribution is not unique and the chain started in one square estimates $\mathbb{P}(\theta\in(2,3)^2)$ as $0$. Repairs: reparametrize, for example with $u=\theta_1+\theta_2$ and $v=\theta_1-\theta_2$, in which the line $v=0$ crosses both squares, so that the conditional of $u$ given $v$ near $0$ connects them; or add Metropolis–Hastings moves that change both coordinates at once, such as an independence proposal uniform on $(0,3)^2$ or a random walk with a large step, which is valid by Proposition 10.5.1 (each move leaves the target invariant).
9. In Algorithm 10.3.1, why are the draws of the adaptation phase discarded? Construct a simple example in which a proposal that depends on the past gives the wrong stationary distribution.

   **Answer** While the proposal depends on earlier draws, $\theta^{(t+1)}$ depends on more than $\theta^{(t)}$, the sequence is not a Markov chain, and Theorem 10.1.1 does not apply. Example: let the target be uniform on $\{1,2,3\}$, and consider two symmetric proposals, $g_a$ "stay where you are" and $g_b$ "move to one of the other two states at random". Each gives a valid Metropolis kernel that leaves the uniform distribution invariant ($g_b$ is always accepted). Now let an adaptive rule choose the proposal from the chain's history, say $g_a$ whenever the chain is at state $1$ (because "the last move into state $1$ was accepted, so do not change a good thing") and $g_b$ otherwise. Every single step is a Metropolis step for the target, yet the chain is absorbed at state $1$, and its long-run frequencies are $(1,0,0)$. Selecting among invariant kernels according to where the chain is or has been destroys invariance. Freezing the proposal before the inference run restores a time-homogeneous Markov chain with the correct stationary distribution; continuous adaptation is valid only under conditions such as diminishing adaptation.
