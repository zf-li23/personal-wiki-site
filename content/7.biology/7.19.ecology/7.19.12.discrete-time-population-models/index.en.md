---
title: "Discrete-Time Population Models: Stability, Cycles and Chaos"
description: "Single-species models for populations with nonoverlapping generations (discrete logistic, Ricker, Beverton–Holt, Hassell, Maynard Smith–Slatkin); the stability criterion |F′(N*)| < 1 with proof and the thresholds of each model; cobweb diagrams; the 2-cycle and the period-doubling cascade, bifurcation diagrams and periodic windows; Lyapunov exponents, with λ = ln 2 at μ = 4; universality, the Feigenbaum constants and an approximate renormalization; May's discovery, the parameters of natural insect populations, the Tribolium experiments and the debate about chaos in nature."
---

Many organisms breed once a year in a short season, and their offspring do not overlap with their parents: annual plants, univoltine insects, many fish with a single spawning season. Their population size is naturally recorded once per generation, and a population in which density dependence acts within each generation is described by a difference equation $N_{t+1} = F(N_t)$. Such equations look like discretized versions of the logistic equation of 7.19.10, but they behave very differently. Robert May (1974, 1976) showed that the simplest of them, with a single variable and no randomness, can approach equilibrium smoothly, oscillate with period 2, 4, 8, …, or fluctuate apparently at random, depending only on the reproductive rate. This chapter analyzes these models completely: their equilibria and stability, the cascade of period doublings, the measurement of chaos by the Lyapunov exponent, and the universality of the route to chaos, which makes its quantitative features independent of the details of the model. It ends with the evidence on whether natural populations behave this way. The models of density dependence come from 7.19.11, where the slope $b$ of $k$ against $\log N$ measured whether competition under- or overcompensates; here we see what overcompensation does to dynamics. The same **logistic map** appears in computational neuroscience as the simplest example of chaos ([7.16.31](/7.16.31#sec-31.2)); the general theory of **bifurcation** in differential equations is in [2.4.11](/2.4.11#sec-11.6.4). Time delays in discrete and continuous models follow in 7.19.13.

## 12.1. Density-Dependent Models for Nonoverlapping Generations

### 12.1.1. The Models

A single-species model with discrete generations has the form
$$
N_{t+1} = F(N_t) = N_tg(N_t), \tag{12.1}
$$
where $g(N)$ is the per capita reproductive rate (the number of individuals in the next generation produced per individual in this one, after density-dependent mortality). Without density dependence $g \equiv \lambda$ and growth is geometric (7.19.10). Density dependence makes $g$ decrease with $N$; the shape of $F$ then decides the dynamics. The function $F$ is the *recruitment curve* (in fisheries, the stock–recruitment curve). It rises at low density; if it keeps rising, density dependence is under- or exactly compensating, and if it is humped, with a maximum and a declining arm, density dependence is overcompensating (Definition 11.2.2).

**Formula 12.1.1 (Discrete-Time Models of Density Dependence)** With $\lambda$ (or $\mathrm{e}^r$, or $1 + r$) the per capita rate at low density and $K$ or $N^*$ the positive equilibrium:

| Model | $N_{t+1} = F(N_t)$ | Shape of $F$ | Biological origin |
|---|---|---|---|
| Discrete logistic | $N_t\bigl[1 + r\bigl(1 - N_t/K\bigr)\bigr]$ | parabola, $F < 0$ for $N > K(1 + r)/r$ | linear decline of per capita growth |
| Ricker (1954) | $N_t\exp\bigl[r\bigl(1 - N_t/K\bigr)\bigr]$ | humped, always positive | exponential decline of survival with density (cannibalism, disease) |
| Beverton–Holt (1957) | $\lambda N_t/(1 + aN_t)$, $K = (\lambda - 1)/a$ | saturating | contest for a limited resource |
| Hassell (1975) | $\lambda N_t/(1 + aN_t)^b$ | saturating ($b \leq 1$) or humped ($b > 1$) | general compensation $b$ |
| Maynard Smith–Slatkin (1973) | $\lambda N_t/[1 + (aN_t)^b]$ | saturating ($b \leq 1$) or humped ($b > 1$) | general compensation $b$ |

The Ricker model arises when each newborn independently escapes a density-dependent hazard with probability $\mathrm{e}^{-cN}$, as in fish whose eggs and young are eaten by adults; the Beverton–Holt model when the per capita survival declines hyperbolically, as when a fixed amount of food or space is shared (Question 2 of 7.19.11 gives its exact solution). The discrete logistic is the simplest algebraically, and it is the one that maps onto the standard form studied in mathematics.

**Proposition 12.1.1 (The Discrete Logistic Model and the Logistic Map)** The substitution $x = rN/[(1 + r)K]$ transforms the discrete logistic model $N_{t+1} = N_t[1 + r(1 - N_t/K)]$ into the **logistic map** ([7.16.31](/7.16.31#def-31.2.1))
$$
x_{t+1} = \mu x_t(1 - x_t), \qquad \mu = 1 + r. \tag{12.2}
$$
The equilibrium $N = K$ corresponds to $x^* = 1 - 1/\mu$. The model keeps populations in the interval $0 \leq N \leq K(1 + r)/r$ (equivalently $0 \leq x \leq 1$) if and only if $\mu \leq 4$, that is $r \leq 3$.

**Proof** $N_{t+1} = (1 + r)N_t - rN_t^2/K = (1 + r)N_t[1 - rN_t/((1 + r)K)]$. Multiplying by $r/[(1 + r)K]$ gives $x_{t+1} = (1 + r)x_t(1 - x_t)$. $N = K$ gives $x = r/(1 + r) = 1 - 1/\mu$. The map $x \mapsto \mu x(1 - x)$ sends $[0, 1]$ into $[0, \mu/4]$, the maximum being attained at $x = 1/2$; this lies in $[0, 1]$ iff $\mu \leq 4$. For $\mu > 4$ the points near $1/2$ are mapped above 1 and then to negative values. $\square$

The discrete logistic therefore predicts negative populations if density is high enough, a defect of the model that the Ricker model, with its exponential tail, does not have. The parameterization used in many Chinese textbooks, $N_{t+1} = N_t[1 - B(N_t - N_{\mathrm{eq}})]$ with $L = BN_{\mathrm{eq}}$, is the same model: expanding gives $N_t[1 + L(1 - N_t/N_{\mathrm{eq}})]$, so $L = r$ and $N_{\mathrm{eq}} = K$. Its well-known thresholds ($L = 1$, 2 and about 2.57) are those derived below for $r$.

### 12.1.2. Stability of Fixed Points

An equilibrium of Eq. (12.1) is a **fixed point** $N^* = F(N^*)$ ([3.5.4](/3.5.4)). Near it, a small deviation $n_t = N_t - N^*$ is multiplied in each generation by the slope of the recruitment curve, $F'(N^*)$, which we call the *multiplier* of the fixed point.

**Theorem 12.1.1 (Stability of a Fixed Point of a Map)** Let $F$ be continuously differentiable near a fixed point $N^*$, with multiplier $m = F'(N^*)$.

(a) If $\lvert m\rvert < 1$, then $N^*$ is asymptotically stable: there is $\delta > 0$ such that $\lvert N_0 - N^*\rvert < \delta$ implies $\lvert N_t - N^*\rvert \leq c^t\lvert N_0 - N^*\rvert$ for some $c < 1$, so $N_t \to N^*$ geometrically.

(b) If $\lvert m\rvert > 1$, then $N^*$ is unstable: every orbit that starts near $N^*$ but not at it leaves some neighborhood of $N^*$.

(c) The sign of $m$ decides the manner of approach or departure: for $0 < m < 1$ the deviations decay without changing sign (monotonic damping), for $-1 < m < 0$ they alternate in sign with decreasing amplitude (damped oscillations); for $m > 1$ they grow monotonically and for $m < -1$ they grow with alternating sign. $m = 0$ is called superstable (convergence faster than geometric).

**Proof** (a) Choose $c$ with $\lvert m\rvert < c < 1$. By continuity of $F'$ there is $\delta > 0$ such that $\lvert F'(N)\rvert \leq c$ for $\lvert N - N^*\rvert < \delta$. By the mean value theorem, for such $N$, $\lvert F(N) - N^*\rvert = \lvert F(N) - F(N^*)\rvert = \lvert F'(\xi)\rvert\lvert N - N^*\rvert \leq c\lvert N - N^*\rvert < \delta$ for some $\xi$ between $N$ and $N^*$. So the interval $(N^* - \delta, N^* + \delta)$ is mapped into itself, and by induction $\lvert N_t - N^*\rvert \leq c^t\lvert N_0 - N^*\rvert$.

(b) Choose $c$ with $1 < c < \lvert m\rvert$ and $\delta$ such that $\lvert F'(N)\rvert \geq c$ for $\lvert N - N^*\rvert < \delta$. As long as $N_t$ stays in this neighborhood, $\lvert N_{t+1} - N^*\rvert \geq c\lvert N_t - N^*\rvert$, so $\lvert N_t - N^*\rvert \geq c^t\lvert N_0 - N^*\rvert$, which exceeds $\delta$ after finitely many steps.

(c) By Taylor's theorem, $n_{t+1} = mn_t + o(n_t)$, so for small deviations $n_t \approx m^tn_0$, whose sign alternates iff $m < 0$. $\square$

When $\lvert m\rvert = 1$ the linear terms do not decide stability; these are exactly the parameter values at which the qualitative behavior changes (bifurcations). In terms of the recruitment curve: an equilibrium on the rising arm of $F$ ($m > 0$) is approached monotonically; on the declining arm ($m < 0$) the population overshoots and undershoots alternately, and if the declining arm is steeper than $-1$ the equilibrium cannot hold the population at all. This is the precise version of Begon's statement that overcompensating density dependence combined with a high reproductive rate destabilizes populations. The same criterion, with the product of the multipliers along the cycle, gives the stability of periodic orbits ([7.16.31](/7.16.31#prop-31.2.1)); we derive it for the 2-cycle in Section 12.3.

### 12.1.3. The Thresholds of Each Model

**Proposition 12.1.2 (Multipliers of the Models)** The multipliers at the positive equilibrium are:

| Model | $F'(N^*)$ | Monotonic damping | Damped oscillation | Unstable ($F' < -1$) |
|---|---|---|---|---|
| Discrete logistic, Ricker | $1 - r$ | $0 < r \leq 1$ | $1 < r < 2$ | $r > 2$ |
| Beverton–Holt | $1/\lambda$ | all $\lambda > 1$ | never | never |
| Hassell | $1 - b\bigl(1 - \lambda^{-1/b}\bigr)$ | $b(1 - \lambda^{-1/b}) \leq 1$ | between | $b(1 - \lambda^{-1/b}) > 2$ |
| Maynard Smith–Slatkin | $1 - b(1 - 1/\lambda)$ | $b(1 - 1/\lambda) \leq 1$ | between | $b(1 - 1/\lambda) > 2$ |

**Proof** Discrete logistic: $F'(N) = 1 + r - 2rN/K$, so $F'(K) = 1 - r$. Ricker: $F'(N) = (1 - rN/K)\mathrm{e}^{r(1 - N/K)}$, so $F'(K) = 1 - r$. Beverton–Holt: $F'(N) = \lambda/(1 + aN)^2$, and $1 + aN^* = \lambda$, so $F'(N^*) = 1/\lambda$. Hassell: $F'(N) = \lambda(1 + aN)^{-b}[1 - baN/(1 + aN)]$; at $N^*$, $\lambda(1 + aN^*)^{-b} = 1$ and $aN^*/(1 + aN^*) = 1 - \lambda^{-1/b}$. Maynard Smith–Slatkin: $F'(N) = \lambda[1 + (1 - b)(aN)^b]/[1 + (aN)^b]^2$; at $N^*$, $(aN^*)^b = \lambda - 1$, giving $[1 + (1 - b)(\lambda - 1)]/\lambda = 1 - b(1 - 1/\lambda)$. The classification follows from Theorem 12.1.1. $\square$

Several conclusions follow. The two humped one-parameter models lose stability at the same reproductive rate, $r = 2$, that is a factor $\mathrm{e}^2 = 7.4$ per generation for the Ricker model and $1 + r = 3$ for the discrete logistic. Exact compensation (Beverton–Holt, $b = 1$) gives monotonic damping whatever the reproductive rate: a population with contest competition cannot oscillate in this framework. In the Hassell model, $b(1 - \lambda^{-1/b})$ increases with both $b$ and $\lambda$ and tends to $\ln\lambda$ as $b \to \infty$, so the equilibrium is stable for every $b$ if $\lambda < \mathrm{e}^2$, and stable for every $\lambda$ if $b \leq 2$ (since $1 - \lambda^{-1/b} < 1$). Oscillations require both a high reproductive rate *and* strongly overcompensating density dependence.

![Dynamics of the Hassell model N_{t+1} = λN_t(1 + aN_t)^(−b) in the plane of the low-density reproductive rate λ (log scale) and the compensation parameter b (Proposition 12.1.2), classified by numerical iteration of every parameter pair. Below the dashed curve b(1 − λ^(−1/b)) = 1 the equilibrium is approached monotonically, between it and the solid curve b(1 − λ^(−1/b)) = 2 by damped oscillations; above the solid curve the equilibrium is unstable and the population settles on a 2-cycle (blue), on cycles of period 4 to 32 (yellow), or fluctuates chaotically with a positive Lyapunov exponent (red), interrupted by bands of periodic windows. Exact compensation (b = 1) and any b ≤ 2 give a stable equilibrium for all λ; instability requires λ > e² ≈ 7.4](./plots/stability-regions.py)

## 12.2. Cobweb Diagrams

Theorem 12.1.1 describes the dynamics near equilibrium; the global dynamics of a one-dimensional map can be seen in a single picture.

**Definition 12.2.1 (Cobweb Diagram)** The **cobweb diagram** of a map $x_{t+1} = f(x_t)$ is the graph of $f$ together with the diagonal $x_{t+1} = x_t$, on which the orbit from $x_0$ is drawn as a path: from the point $(x_t, x_t)$ on the diagonal vertically to the graph at $(x_t, f(x_t))$, then horizontally back to the diagonal at $(x_{t+1}, x_{t+1})$, and so on.

The fixed points are the intersections of the graph with the diagonal, and the slope of the graph there is the multiplier. If the graph crosses the diagonal with slope between 0 and 1, the path is a staircase converging to the fixed point; with slope between $-1$ and 0, a spiral converging to it; with slope below $-1$, a spiral moving away from it. Because the path stays on the graph and the diagonal, the cobweb also shows where orbits can go globally: for a humped $F$, an orbit cannot exceed the maximum of $F$, and once there cannot fall below $F(F_{\max})$, so populations are confined between these limits even when they fluctuate chaotically. In this sense, even a chaotic population is regulated.

![Cobweb diagrams of the discrete logistic model x_{t+1} = x_t[1 + r(1 − x_t)] (x = N/K, Definition 12.2.1), started at x₀ = 0.1. Top: the recruitment curve (blue), the diagonal and the orbit (orange; early steps faint in the last three panels). r = 0.8: the equilibrium x = 1 lies on the rising arm and is approached as a staircase. r = 1.6: it lies on the declining arm with slope −0.6 and is approached as an inward spiral (damped oscillation). r = 2.3: slope −1.3, the spiral moves outward onto a stable 2-cycle (a square). r = 2.5: a 4-cycle. r = 2.8: the orbit wanders irregularly over the interval between F(F_max) and F_max (chaos). Bottom: the corresponding time series](./plots/cobweb.py)

## 12.3. Period Doubling and Bifurcation Diagrams

### 12.3.1. The 2-Cycle

We now follow what happens when the equilibrium loses stability. It is convenient to work with the logistic map (12.2), $f(x) = \mu x(1 - x)$; the results translate to the discrete logistic model by $r = \mu - 1$.

The fixed points of $f$ are $0$ (multiplier $\mu$) and $x^* = 1 - 1/\mu$, with multiplier $f'(x^*) = \mu(1 - 2x^*) = 2 - \mu$, so $x^*$ is stable for $1 < \mu < 3$. At $\mu = 3$ the multiplier passes through $-1$.

**Definition 12.3.1 (Period-Doubling Bifurcation)** A **period-doubling bifurcation** (flip bifurcation) of a map occurs when the multiplier of a fixed point (or periodic orbit) passes through $-1$ as a parameter changes: the fixed point loses stability and a periodic orbit of twice the period, initially close to it, appears (or disappears).

**Proposition 12.3.1 (The 2-Cycle of the Logistic Map)** For $\mu > 3$ the logistic map has exactly one orbit of period 2, $\{p, q\}$ with
$$
p, q = \frac{(\mu + 1) \mp\sqrt{(\mu + 1)(\mu - 3)}}{2\mu}. \tag{12.3}
$$
It is stable for $3 < \mu < 1 + \sqrt6 \approx 3.449$ (that is, $2 < r < \sqrt6 \approx 2.449$ in the discrete logistic model), and at $\mu = 1 + \sqrt6$ it loses stability in a period-doubling bifurcation to a 4-cycle.

**Proof** A 2-cycle consists of fixed points of $f^{(2)} = f\circ f$ that are not fixed points of $f$. From $q = f(p)$ and $p = f(q)$: subtracting, $q - p = \mu(p - q) - \mu(p^2 - q^2) = \mu(p - q)[1 - (p + q)]$, and dividing by $q - p \neq 0$ gives $p + q = (\mu + 1)/\mu$. Adding, $p + q = \mu(p + q) - \mu(p^2 + q^2) = \mu(p + q) - \mu[(p + q)^2 - 2pq]$, which with the sum gives $pq = (\mu + 1)/\mu^2$. So $p$ and $q$ are the roots of $\mu^2x^2 - \mu(\mu + 1)x + (\mu + 1) = 0$, which are real and distinct iff the discriminant $\mu^2(\mu + 1)^2 - 4\mu^2(\mu + 1) = \mu^2(\mu + 1)(\mu - 3)$ is positive, that is iff $\mu > 3$; this gives Eq. (12.3).

By the chain rule, $(f^{(2)})'(p) = f'(f(p))f'(p) = f'(q)f'(p)$, and the same value at $q$: the multiplier of the cycle is the product of the multipliers along it. With $f'(x) = \mu(1 - 2x)$,
$$
f'(p)f'(q) = \mu^2[1 - 2(p + q) + 4pq] = \mu^2\Bigl[1 - \frac{2(\mu + 1)}{\mu} + \frac{4(\mu + 1)}{\mu^2}\Bigr] = -\mu^2 + 2\mu + 4.
$$
By Theorem 12.1.1 applied to $f^{(2)}$, the cycle is stable iff $-1 < -\mu^2 + 2\mu + 4 < 1$. The right inequality is $\mu^2 - 2\mu - 3 = (\mu - 3)(\mu + 1) > 0$, true for $\mu > 3$. The left is $\mu^2 - 2\mu - 5 < 0$, i.e. $\mu < 1 + \sqrt6$. At $\mu = 1 + \sqrt6$ the multiplier passes through $-1$. $\square$

At $\mu = 3$ the multiplier of the cycle equals $+1$ and $p = q = x^*$: the cycle is born from the fixed point exactly as Definition 12.3.1 describes. Biologically, the population alternates between a high and a low year: a large generation depresses the survival of its offspring so much that the next generation is small, which then produces a large one. Such alternation is common in laboratory insect populations with strong larval competition.

![The 2-cycle of the logistic map f(x) = μx(1 − x) (Proposition 12.3.1). A–C: f (thin) and the second iterate f(f(x)) (thick) with the diagonal. At μ = 2.8 the only positive intersection is the fixed point x* (open circle), where f(f(x)) has slope (2 − μ)² = 0.64 < 1. At μ = 3.2 the slope at x* is 1.44 and two new intersections p and q (filled) have appeared, where the slope f′(p)f′(q) = −μ² + 2μ + 4 = 0.16: a stable 2-cycle. At μ = 3.5 that slope is −1.25 and the 2-cycle has become unstable. D: the multipliers of the fixed point (2 − μ) and of the 2-cycle (−μ² + 2μ + 4); each orbit is stable while its multiplier is in the shaded band (−1, 1), so the fixed point gives way to the 2-cycle at μ = 3 and the 2-cycle to a 4-cycle at μ = 1 + √6](./plots/period-2.py)

### 12.3.2. The Bifurcation Diagram

The 4-cycle loses stability in turn and gives birth to an 8-cycle, and so on. The bifurcation values of the logistic map are
$$
\mu_1 = 3, \quad \mu_2 = 1 + \sqrt6 = 3.449490, \quad \mu_3 = 3.544090, \quad \mu_4 = 3.564407, \quad \mu_5 = 3.568759, \quad \dots \to \mu_\infty = 3.569946,
$$
and the intervals between them shrink geometrically. The whole sequence is displayed in a *bifurcation diagram*, in which, for each value of the parameter, the attractor (the set of values visited after transients have died out) is plotted. For the discrete logistic model, $r_k = \mu_k - 1$: the cascade accumulates at $r_\infty = 2.5699$; for the Ricker model, period doubling begins at $r = 2$ and continues at $r = 2.526$, $2.656$, … to $r_\infty = 2.6924$.

Beyond $r_\infty$ most parameter values give **chaos** ([7.16.31](/7.16.31#def-31.2.3)): bounded, aperiodic fluctuations with sensitive dependence on initial conditions. The chaotic region is interrupted by *periodic windows*, intervals of parameter in which a stable cycle exists. The largest window of the logistic map begins at $\mu = 1 + \sqrt8 = 3.8284$ ($r = 2.828$) with a stable 3-cycle, born together with an unstable one in a **saddle-node bifurcation** ([7.6.33](/7.6.33)) of $f^{(3)}$, and the 3-cycle then undergoes its own period-doubling cascade (6, 12, 24, …). A theorem of Li and Yorke (1975), "period three implies chaos", states that a continuous map of an interval with a point of period 3 has points of every period and an uncountable set of aperiodic orbits; Sharkovskii's theorem (1964) gives the complete ordering of which periods imply which. Within the chaotic bands, therefore, infinitely many unstable cycles coexist, and in the windows the stable cycle attracts almost all orbits.

![Bifurcation diagrams (A, B) and Lyapunov exponents (C, D) of the discrete logistic model x_{t+1} = x_t[1 + r(1 − x_t)] and the Ricker model x_{t+1} = x_t exp[r(1 − x_t)]. For each r, the values visited after a transient are plotted. Both models show the same sequence: a stable equilibrium (x = 1) up to r = 2, then period doubling (dashed lines: r = 2, 2.449, 2.544 for the logistic; 2, 2.526, 2.656 for the Ricker) accumulating at r∞ (solid line: 2.5699 and 2.6924), followed by chaotic bands with periodic windows (the 3-cycle window at r = 2.83 in the logistic and the wide window near r = 3.1 in the Ricker). The Lyapunov exponent (Definition 12.4.1) is negative on stable cycles, touches zero at each period-doubling bifurcation, plunges to −∞ at superstable parameters and is positive (shaded) in the chaotic regime](./plots/bifurcation-lyapunov.py)

## 12.4. Lyapunov Exponents and the Diagnosis of Chaos

A chaotic orbit is not random: it is generated by a deterministic rule, it stays within bounds, and short-term prediction is possible. What distinguishes it from a stable cycle is that two orbits starting close together separate exponentially fast. Consider two initial values $x_0$ and $x_0 + \delta_0$. After one step their distance is $\lvert f(x_0 + \delta_0) - f(x_0)\rvert \approx \lvert f'(x_0)\rvert\lvert\delta_0\rvert$, and after $n$ steps, by the chain rule,
$$
\lvert\delta_n\rvert \approx \lvert f'(x_{n-1})\cdots f'(x_1)f'(x_0)\rvert\,\lvert\delta_0\rvert, \qquad \frac1n\ln\frac{\lvert\delta_n\rvert}{\lvert\delta_0\rvert} \approx \frac1n\sum_{k=0}^{n-1}\ln\lvert f'(x_k)\rvert.
$$

**Definition 12.4.1 (Lyapunov Exponent of a Map)** The **Lyapunov exponent** ([7.16.31](/7.16.31#def-31.2.2)) of the orbit of $x_0$ under a map $f$ is
$$
\lambda = \lim_{n\to\infty}\frac1n\sum_{k=0}^{n-1}\ln\lvert f'(x_k)\rvert, \tag{12.4}
$$
the mean exponential rate of separation of nearby orbits per step. An orbit is chaotic if it is bounded, not asymptotically periodic, and has $\lambda > 0$.

**Proposition 12.4.1 (Lyapunov Exponents of Cycles)** If the orbit of $x_0$ converges to a periodic orbit $x_1^*, \dots, x_p^*$ (none of which is a critical point of $f$), then
$$
\lambda = \frac1p\ln\Bigl\lvert\prod_{i=1}^pf'(x_i^*)\Bigr\rvert.
$$
In particular $\lambda < 0$ for a stable cycle, $\lambda = 0$ at a period-doubling bifurcation (multiplier $-1$), and $\lambda = -\infty$ for a superstable cycle (multiplier 0, a cycle through the critical point).

**Proof** Along the orbit, $\ln\lvert f'(x_k)\rvert$ converges to the periodic sequence $\ln\lvert f'(x_i^*)\rvert$, so its Cesàro mean converges to the mean over one period, $\frac1p\sum_i\ln\lvert f'(x_i^*)\rvert = \frac1p\ln\lvert\prod_if'(x_i^*)\rvert$. A stable cycle has $\lvert\prod f'\rvert < 1$ (Theorem 12.1.1 applied to $f^{(p)}$), so $\lambda < 0$; a multiplier of absolute value 1 gives $\lambda = 0$; and a cycle through the critical point has a factor $f' = 0$. (At a superstable parameter the orbit converges faster than geometrically and the sum diverges to $-\infty$.) $\square$

For one parameter value the Lyapunov exponent of the logistic map can be computed exactly.

**Proposition 12.4.2 (The Logistic Map at $\mu = 4$)** For $\mu = 4$ the logistic map is conjugate to the tent map $T(\theta) = 1 - \lvert1 - 2\theta\rvert$ on $[0, 1]$ by $x = h(\theta) = \sin^2(\pi\theta/2)$, that is $f\circ h = h\circ T$. Almost every orbit has the invariant density $\rho(x) = 1/\bigl(\pi\sqrt{x(1 - x)}\bigr)$ and the Lyapunov exponent $\lambda = \ln 2$.

**Proof** $f(h(\theta)) = 4\sin^2(\pi\theta/2)\cos^2(\pi\theta/2) = \sin^2(\pi\theta)$. For $\theta \leq 1/2$, $h(T(\theta)) = \sin^2(\pi\theta)$; for $\theta > 1/2$, $h(2 - 2\theta) = \sin^2(\pi - \pi\theta) = \sin^2(\pi\theta)$. So $f\circ h = h\circ T$. The tent map preserves the uniform distribution on $[0, 1]$ (each subinterval has two preimages of half its length) and is ergodic, so almost every orbit of $T$ is uniformly distributed; mapping by $h$, almost every orbit of $f$ is distributed with the density of $x = h(\Theta)$, $\Theta$ uniform: $\rho(x) = \bigl[\frac{\mathrm{d}h}{\mathrm{d}\theta}\bigr]^{-1} = 1/(\pi\sin(\pi\theta/2)\cos(\pi\theta/2)) = 1/\bigl(\pi\sqrt{x(1 - x)}\bigr)$. By Birkhoff's ergodic theorem, the time average in Eq. (12.4) equals the space average:
$$
\lambda = \int_0^1\ln\lvert f'(x)\rvert\rho(x)\,\mathrm{d}x = \int_0^1\ln\lvert4(1 - 2h(\theta))\rvert\,\mathrm{d}\theta = \int_0^1\ln\lvert4\cos(\pi\theta)\rvert\,\mathrm{d}\theta,
$$
using $1 - 2\sin^2(\pi\theta/2) = \cos(\pi\theta)$. Since $\int_0^1\ln\lvert\cos(\pi\theta)\rvert\,\mathrm{d}\theta = \frac{2}{\pi}\int_0^{\pi/2}\ln\cos u\,\mathrm{d}u = \frac2\pi\bigl(-\frac\pi2\ln2\bigr) = -\ln 2$, we get $\lambda = \ln 4 - \ln 2 = \ln 2$. $\square$

At $\mu = 4$, then, an initial uncertainty doubles on average every generation: a measurement error of $10^{-6}$ grows to the size of the attractor in about $\ln(10^6)/\ln 2 \approx 20$ generations. More generally, a positive Lyapunov exponent sets a prediction horizon of order $\lambda^{-1}\ln(L/\delta_0)$ steps for an initial uncertainty $\delta_0$ and attractor size $L$. Within this horizon a chaotic population is predictable (more predictable than a random one); beyond it, knowledge of the present state is useless. This is why the diagnosis of chaos in nature is not an academic question: it determines how far ahead population sizes can be forecast.

Estimating $\lambda$ from data requires a model of $F$, because the derivatives in Eq. (12.4) are not observed. In practice $F$ is estimated nonparametrically (by regression of $N_{t+1}$ on $N_t$, or on several lagged values when the population has hidden structure, using the time-delay embeddings justified by Takens' theorem), and $\lambda$ is computed from the fitted function. Ellner & Turchin (1995) applied such methods to long series of laboratory, field and epidemiological data and found negative or near-zero exponents for most field populations: dynamics close to the edge between stability and chaos, but rarely clearly chaotic. Short and noisy ecological series make any such estimate uncertain (Bjørnstad & Grenfell 2001).

## 12.5. Universality: the Feigenbaum Constants

The bifurcation diagrams of the logistic and Ricker models in the figure above differ in scale but are otherwise strikingly similar. The similarity is quantitative. Feigenbaum (1978) discovered that the sequence of period-doubling bifurcations converges geometrically with a ratio that is the same for all smooth maps with a single quadratic maximum.

**Definition 12.5.1 (Feigenbaum Constants)** For a one-parameter family of unimodal maps with a quadratic maximum, let $\mu_n$ be the parameter of the $n$-th period-doubling bifurcation (from period $2^{n-1}$ to $2^n$), and $d_n$ the distance from the critical point to the nearest point of the $2^n$-cycle at the superstable parameter of that cycle. The **Feigenbaum constants** are
$$
\delta = \lim_{n\to\infty}\frac{\mu_n - \mu_{n-1}}{\mu_{n+1} - \mu_n} = 4.669201\dots, \qquad \alpha = \lim_{n\to\infty}\frac{d_n}{d_{n+1}} = -2.502907\dots. \tag{12.5}
$$
The same limits are obtained with the superstable parameters $R_n$ (at which the $2^n$-cycle passes through the critical point) in place of $\mu_n$.

$\delta$ measures how quickly the bifurcations accumulate in parameter space; $\alpha$, how the attractor shrinks in state space at each doubling, the sign recording that each doubling flips the orientation. For the logistic map, $(\mu_2 - \mu_1)/(\mu_3 - \mu_2) = 0.4495/0.0946 = 4.75$ and $(\mu_3 - \mu_2)/(\mu_4 - \mu_3) = 4.66$; for the Ricker model the corresponding ratios approach the same limit from below. Knowing $\delta$, one can predict the accumulation point from the first few bifurcations: $\mu_\infty \approx \mu_n + (\mu_n - \mu_{n-1})/(\delta - 1)$, which from $\mu_3$ and $\mu_4$ gives 3.56995.

Why should the ratio be universal? Look at the second iterate $f^{(2)}$ near the 2-cycle point closest to the critical point (Figure in Section 12.3.1, panel B): it is a small, inverted copy of the original hump. Period doubling of $f$ corresponds to the loss of stability of a fixed point of $f^{(2)}$, which happens by the same mechanism, at a parameter where the rescaled copy looks like $f$ at its own first bifurcation. Repeating the argument at each level, the doubling cascade is governed by a map from one level to the next, the *renormalization* (doubling) operator $\mathcal{T}[g](x) = \alpha\,g(g(x/\alpha))$, which takes a function to its second iterate, rescaled by $\alpha$. The quantitative features of the cascade are properties of this operator, not of the particular $f$, and hence universal. A crude version of the argument can be carried out by hand.

**Proposition 12.5.1 (An Approximate Renormalization)** Truncating each level at quadratic order, the logistic map near its period doublings has the normal form $\xi_{t+1} = -(1 + \nu)\xi_t - \xi_t^2$ (with $\nu = \mu - 3$), and the second iterate near the 2-cycle point closest to the critical point has, after rescaling by a factor $C(\nu)$, the same form with parameter $\tilde\nu = \nu^2 + 4\nu - 2$. Consequently:
1. the bifurcation parameters satisfy $\nu_k = \nu_{k+1}^2 + 4\nu_{k+1} - 2$, $\nu_1 = 0$, which gives $\mu_2 = 1 + \sqrt6$ exactly and $\mu_3 \approx 3.5396$;
2. they accumulate at the fixed point $\nu^* = (\sqrt{17} - 3)/2$, i.e. $\mu_\infty \approx 3.5616$;
3. $\delta \approx 2\nu^* + 4 = 1 + \sqrt{17} \approx 5.12$ and $\alpha \approx C(\nu^*) \approx -2.24$.

**Proof** Let $x^* = 1 - 1/\mu$ and $\eta = x - x^*$. Because $f$ is quadratic, $f(x^* + \eta) = x^* + f'(x^*)\eta + \tfrac12f''\eta^2 = x^* + (2 - \mu)\eta - \mu\eta^2$ exactly. With $\xi = \mu\eta$ and $\nu = \mu - 3$ this is $\xi_{t+1} = -(1 + \nu)\xi_t - \xi_t^2 =: g_\nu(\xi_t)$, whose fixed point 0 has multiplier $-(1 + \nu)$ and doubles at $\nu = 0$.

The 2-cycle of $g_\nu$: from $g(p) = q$, $g(q) = p$, as in Proposition 12.3.1, $p + q = -\nu$ and $pq = -\nu$, so $p, q = (-\nu \pm\sqrt{\nu^2 + 4\nu})/2$, and the multiplier is $g'(p)g'(q) = [(1 + \nu) + 2p][(1 + \nu) + 2q] = (1 + \nu)^2 + 2(1 + \nu)(p + q) + 4pq = 1 - 4\nu - \nu^2$.

Expand $g^{(2)}$ about $q$ (the root with the minus sign, nearer the critical point $-(1 + \nu)/2$ of $g$). With $g(q + \eta) = p + g'(q)\eta - \eta^2$ and $g(p + \varepsilon) = q + g'(p)\varepsilon - \varepsilon^2$,
$$
g^{(2)}(q + \eta) - q = g'(p)\bigl(g'(q)\eta - \eta^2\bigr) - g'(q)^2\eta^2 + O(\eta^3) = M\eta - C\eta^2 + O(\eta^3),
$$
with $M = g'(p)g'(q)$ and $C = g'(p) + g'(q)^2$. Rescaling $\tilde\xi = C\eta$ and dropping the cubic terms gives $\tilde\xi_{t+2} = M\tilde\xi_t - \tilde\xi_t^2$, the normal form with $-(1 + \tilde\nu) = M = 1 - 4\nu - \nu^2$, that is $\tilde\nu = \nu^2 + 4\nu - 2$.

The $2^k$-cycle doubles when the parameter of its renormalized map reaches the doubling value of the previous level, which gives the recursion in (1). With $\nu_1 = 0$: $\nu_2^2 + 4\nu_2 - 2 = 0$, $\nu_2 = \sqrt6 - 2$, so $\mu_2 = 1 + \sqrt6$, the exact value of Proposition 12.3.1; and $\nu_3 = -2 + \sqrt{6 + \nu_2} = 0.5396$. The recursion $\nu_k = \phi(\nu_{k+1})$ with $\phi(\nu) = \nu^2 + 4\nu - 2$ has the fixed point $\nu^* = \phi(\nu^*)$, $\nu^{*2} + 3\nu^* - 2 = 0$, $\nu^* = (\sqrt{17} - 3)/2 = 0.5616$, to which the inverse iteration converges. Near it, $\nu_k - \nu^* \approx \phi'(\nu^*)(\nu_{k+1} - \nu^*)$, so the ratio of successive intervals tends to $\phi'(\nu^*) = 2\nu^* + 4 = 1 + \sqrt{17} = 5.12$. At $\nu^*$, $p = 0.519$, $q = -1.081$, $g'(p) = -2.600$, $g'(q) = 0.600$, and the length scale changes by $C = -2.600 + 0.360 = -2.24$ per level. $\square$

The approximation is good to about 10% for $\delta$ and $\alpha$, and it already shows where universality comes from: the recursion $\phi$ does not depend on the starting map, only on its quadratic maximum. Feigenbaum and Cvitanović made the argument exact. The universal function is the fixed point of the doubling operator, an even function with $g(0) = 1$ satisfying
$$
g(x) = \alpha\,g\bigl(g(x/\alpha)\bigr), \qquad \alpha = 1/g(1), \tag{12.6}
$$
and $\delta$ is the single eigenvalue greater than 1 of the doubling operator linearized at $g$. Equation (12.6) can be solved numerically by expanding $g(x) = 1 + c_1x^2 + c_2x^4 + \cdots$ and solving for the coefficients ($c_1 = -1.5276$, $c_2 = 0.1048$, …), which gives $\alpha = -2.50291$. Lanford (1982) proved the existence of the fixed point with a computer-assisted proof.

![Universality of period doubling (Definition 12.5.1). A: at the accumulation point of the logistic map, the iterates f^(2ⁿ), centered at the critical point and rescaled so that their value there is 1, for n = 0 to 4 (blue, light to dark), converge to the universal function g (dashed red), the solution of g(x) = αg(g(x/α)) computed with a polynomial of degree 16 (Eq. (12.6)); α = 1/g(1) = −2.50291. B: ratios δₙ of successive intervals between superstable parameters for the logistic map μx(1 − x), the Ricker map x exp(r(1 − x)) and the sine map μ sin(πx): the three sequences start differently and converge to the same δ = 4.6692…, while the accumulation points R∞ (3.56995, 2.69237 and 0.86558) are specific to each map](./plots/feigenbaum.py)

The constants were measured in experiments on convection in liquid helium, nonlinear electrical circuits and lasers, all of which pass to chaos by period doubling with ratios close to 4.67 (Libchaber and colleagues, 1982). For ecology, universality means that the route to chaos predicted by single-species models does not depend on which model is used: any population whose recruitment curve has a single smooth hump (overcompensating density dependence) passes from stable equilibrium through period doubling to chaos as its reproductive rate increases, with the same geometric proportions. What is model dependent is only where on the scale of $r$ or $\lambda$ this happens.

## 12.6. Chaos in Ecology

### 12.6.1. May's Discovery and the Parameters of Natural Populations

May's papers (1974 in *Science*, 1976 in *Nature*) had an influence far beyond ecology, because they showed that the simplest nonlinear models of a biological process can generate behavior indistinguishable from noise. For ecologists the implication was that irregular fluctuations of natural populations need not be caused by fluctuations of weather or other external factors: the internal dynamics of density dependence might be responsible. Density dependence, the force that regulates populations (7.19.11), becomes destabilizing when it overcompensates and acts on a population with a high reproductive rate.

Whether natural populations have such parameters is an empirical question. Hassell, Lawton & May (1976) fitted the Hassell model (Formula 12.1.1) to life-table data for a series of insect populations, both from the field and from the laboratory, and located them in the $(\lambda, b)$ plane of the figure in Section 12.1.3. Most field populations fell in the region of monotonic damping, a few in the region of damped oscillations, and only one field population, the Colorado potato beetle (*Leptinotarsa decemlineata*), beyond the stability boundary; laboratory populations, with abundant food and no enemies, were more often oscillatory. The conclusion that natural single-species dynamics are usually stable was later qualified on several grounds. Single-species models fitted to populations embedded in communities absorb the effects of natural enemies into the parameters; the estimation of $b$ from noisy data is biased; and several important insect populations have oscillatory dynamics generated by interactions with natural enemies (7.19.27) rather than by intraspecific competition.

### 12.6.2. Chaos in a Laboratory Population of Flour Beetles

The most convincing demonstration of chaos in a biological population came from the flour beetle *Tribolium castaneum*, studied for a decade by Costantino, Cushing, Dennis and Desharnais. Its dynamics are dominated by cannibalism: adults eat eggs and pupae, and larvae eat eggs. The LPA model follows larvae $L$, pupae $P$ and adults $A$ in time steps of two weeks:
$$
\begin{aligned}
L_{t+1} &= bA_t\exp(-c_{\mathrm{el}}L_t - c_{\mathrm{ea}}A_t),\\
P_{t+1} &= (1 - \mu_{\mathrm{l}})L_t,\\
A_{t+1} &= P_t\exp(-c_{\mathrm{pa}}A_t) + (1 - \mu_{\mathrm{a}})A_t,
\end{aligned} \tag{12.7}
$$
where $b$ is the number of larval recruits per adult in the absence of cannibalism, $\exp(-c_{\mathrm{el}}L)$ and $\exp(-c_{\mathrm{ea}}A)$ are the probabilities that an egg escapes cannibalism by larvae and adults, $\exp(-c_{\mathrm{pa}}A)$ the probability that a pupa escapes cannibalism by adults, and $\mu_{\mathrm{l}}$, $\mu_{\mathrm{a}}$ the larval and adult death rates. Each cannibalism term is a Ricker-type overcompensation. The model was fitted to laboratory data by maximum likelihood, with stochastic terms for demographic and environmental noise (Dennis et al. 1995, 1997), giving $b = 6.598$, $c_{\mathrm{el}} = 0.01209$, $c_{\mathrm{ea}} = 0.01155$ and $\mu_{\mathrm{l}} = 0.2055$.

The decisive step was experimental. Adult mortality and the rate of cannibalism of pupae by adults can be manipulated by removing or adding adults and pupae at each census. With $\mu_{\mathrm{a}}$ set to 0.96, the model predicts a sequence of dynamics as $c_{\mathrm{pa}}$ increases: a stable equilibrium at $c_{\mathrm{pa}} = 0$, an 8-cycle at 0.05, quasiperiodic motion on an invariant loop at 0.10, chaos at 0.25, 0.35 and 0.50 (largest Lyapunov exponent about 0.1 at 0.35), and a 3-cycle at 1.0. Costantino et al. (1997) imposed these values on replicate cultures for about two years. The observed dynamics followed the predicted sequence, including the chaotic attractor, whose characteristic shape appeared in the data, and the model with its estimated noise explained the observed fluctuations quantitatively.

![The LPA model of the flour beetle *Tribolium castaneum* (Eq. (12.7); parameters of Dennis et al. 1997, adult mortality μₐ = 0.96, time step two weeks). A: bifurcation diagram of adult numbers against the rate of cannibalism of pupae by adults, c_pa; dashed lines mark the values imposed in the experiments of Costantino et al. (1997). Increasing c_pa leads from a stable equilibrium through cycles and quasiperiodic motion to chaos and, above about 0.63, to a stable 3-cycle. B: the largest Lyapunov exponent, computed from products of the Jacobian matrices along the orbit: zero on the invariant loop, positive (shaded) in the chaotic region around 0.25–0.5, negative on the cycles. C: attractors in the plane of larvae L and adults A: an 8-cycle (c_pa = 0.05), an invariant loop (0.10), a chaotic attractor (0.35) and a 3-cycle (1.0)](./plots/tribolium.py)

### 12.6.3. Noise, Chaos and the State of the Debate

The beetle experiments also revealed what complicates the detection of chaos in nature. Real populations are subject to noise, and noise interacts with deterministic dynamics in ways that neither alone predicts. Near a stable equilibrium with a multiplier close to $-1$, noise excites persistent oscillations; near the boundary of a basin, noise switches populations between coexisting attractors; and populations consist of whole individuals, so that the continuous state of a model is replaced by a lattice of integers, on which deterministic chaos turns into long cycles (Henson et al. 2001). In such conditions, the useful question is less "is this population chaotic?" than "how much of its variability is generated internally, and how sensitive is it to perturbations?". The Lyapunov exponent of a fitted stochastic model answers the second question.

Several reasons have been proposed for why chaos, so easy to produce in models, seems rare in field populations. Natural populations are structured in space, and dispersal among local populations fluctuating out of phase stabilizes their total; age and stage structure spread density dependence over the life cycle; generalist predators and parasites add stabilizing density dependence; and selection may disfavor the very high reproductive rates that chaos requires, or favor them only when they are kept in check by contest competition. On the other hand, some populations with strong overcompensation, such as fish with cannibalistic adults, insect outbreaks, and diseases like measles in prevaccination cities, show dynamics consistent with low-dimensional chaos or close to it.

The lasting lessons are those Begon & Townsend draw: time lags, high reproductive rates and overcompensating density dependence can each produce population fluctuations without any external cause; deterministic models can generate unpredictability; and the analysis of models is how ecologists found this out. Ecology aims to be a predictive science, and the possibility of intrinsically chaotic dynamics sets limits to prediction that no improvement in measurement can overcome.

## Summary

- Populations with nonoverlapping generations follow $N_{t+1} = F(N_t)$ (Formula 12.1.1). The discrete logistic model is the logistic map $x_{t+1} = \mu x_t(1 - x_t)$ with $\mu = 1 + r$ (Proposition 12.1.1); the textbook parameter $L$ equals $r$.
- A fixed point is stable if $\lvert F'(N^*)\rvert < 1$ (Theorem 12.1.1); the sign of $F'$ decides between monotonic and oscillatory approach. Thresholds (Proposition 12.1.2):

| Model | Monotonic | Damped oscillation | Cycles begin | Chaos begins |
|---|---|---|---|---|
| Discrete logistic | $r \leq 1$ | $1 < r < 2$ | $r = 2$ | $r_\infty = 2.5699$ |
| Ricker | $r \leq 1$ | $1 < r < 2$ | $r = 2$ | $r_\infty = 2.6924$ |
| Beverton–Holt | all $\lambda$ | never | never | never |
| Hassell | $b(1 - \lambda^{-1/b}) \leq 1$ | up to 2 | $b(1 - \lambda^{-1/b}) = 2$ | high $\lambda$ and $b$ |

- Cobweb diagrams (Definition 12.2.1) show the global dynamics and the bounds within which a population fluctuates.
- The 2-cycle of the logistic map exists for $\mu > 3$ and is stable for $3 < \mu < 1 + \sqrt6$, with multiplier $-\mu^2 + 2\mu + 4$ (Proposition 12.3.1); further period doublings (Definition 12.3.1) accumulate at $\mu_\infty = 3.5699$, beyond which chaos alternates with periodic windows (period 3 at $1 + \sqrt8$).
- The Lyapunov exponent $\lambda = \lim\frac1n\sum\ln\lvert f'(x_k)\rvert$ (Definition 12.4.1) is negative on stable cycles, zero at period doublings (Proposition 12.4.1) and positive in chaos; at $\mu = 4$ it equals $\ln 2$ (Proposition 12.4.2). It sets the prediction horizon.
- The cascade is universal: $\delta = 4.6692$ and $\alpha = -2.5029$ for every smooth unimodal map (Definition 12.5.1), as a quadratic renormalization shows approximately ($\delta \approx 1 + \sqrt{17}$, Proposition 12.5.1) and the Feigenbaum–Cvitanović equation (12.6) exactly.
- Most natural insect populations fitted with the Hassell model lie in the stable region; the *Tribolium* LPA experiments demonstrated predicted bifurcations and chaos in a real population; in the field, noise, spatial and age structure and interactions with other species make chaos hard to detect and probably uncommon, but intrinsic dynamics set real limits to prediction.

## Questions

1. Show that the Ricker model $N_{t+1} = N_t\exp[r(1 - N_t/K)]$ has its maximum recruitment at $N = K/r$, and use this to explain why oscillations require $r > 1$.

   **Answer** $F'(N) = \mathrm{e}^{r(1 - N/K)}(1 - rN/K) = 0$ at $N = K/r$. The equilibrium $K$ lies on the declining arm of the curve, where $F' < 0$ and the approach is oscillatory, exactly when $K > K/r$, that is $r > 1$; for $r < 1$ the hump lies beyond $K$ and the population approaches $K$ monotonically from either side. For $1 < r < 2$ the declining arm at $K$ is less steep than $-1$ (damped oscillations); for $r > 2$, steeper (sustained oscillations).

2. Verify that the multiplier of a fixed point of the Maynard Smith–Slatkin model is $1 - b(1 - 1/\lambda)$ and find the critical value of $b$ for $\lambda = 100$. What does it mean that the critical $b$ tends to 2 as $\lambda \to \infty$?

   **Answer** See Proposition 12.1.2. The equilibrium becomes unstable when $b(1 - 1/\lambda) = 2$, that is $b = 2/(1 - 1/\lambda) = 2.02$ for $\lambda = 100$. As $\lambda \to \infty$ the threshold tends to 2: however high the reproductive rate, the equilibrium remains stable unless the density dependence overcompensates strongly ($k$ rising with slope above 2 against $\log N$). In the Maynard Smith–Slatkin model, unlike the Hassell model, even moderate $\lambda$ suffices for instability once $b > 2$; the two models agree that undercompensating or exactly compensating density dependence ($b \leq 1$) is always stabilizing.

3. A population of an annual insect follows the discrete logistic model with $r = 2.5$. Describe its dynamics. Its habitat is improved so that $K$ doubles while $r$ is unchanged; what changes? Then a parasitoid is introduced that adds a density-independent mortality, reducing the effective $r$ to 1.5; what happens?

   **Answer** At $r = 2.5$ ($\mu = 3.5$, between $\mu_2 = 3.449$ and $\mu_3 = 3.544$) the population settles on a stable 4-cycle. Doubling $K$ only rescales the population: the cycle has the same shape and period, with all values doubled, because the dynamics depend only on $r$ (Proposition 12.1.1). Reducing the effective rate of increase to $r = 1.5$ moves the population into the region of damped oscillations: it converges to a stable equilibrium (at the new, lower $K$ of the combined model). Density-independent mortality, often thought of as destabilizing, here stabilizes the dynamics by lowering the reproductive rate, a counterintuitive consequence of overcompensation.

4. Compute the Lyapunov exponent of the logistic map at $\mu = 3.2$ from the multiplier of its 2-cycle, and explain why the exponent is $-\infty$ at $\mu = 1 + \sqrt5$.

   **Answer** At $\mu = 3.2$ the 2-cycle multiplier is $-\mu^2 + 2\mu + 4 = -10.24 + 6.4 + 4 = 0.16$, so by Proposition 12.4.1, $\lambda = \frac12\ln 0.16 = -0.916$. At $\mu = 1 + \sqrt5$ the multiplier is $-(6 + 2\sqrt5) + 2 + 2\sqrt5 + 4 = 0$: the 2-cycle passes through the critical point $x = 1/2$ (indeed $p = 1/2$ there, since the product $f'(p)f'(q)$ vanishes only if $p$ or $q$ is $1/2$). Deviations are then reduced quadratically rather than by a constant factor, the cycle is superstable, and $\ln\lvert f'(1/2)\rvert = \ln 0 = -\infty$.

5. Use the Feigenbaum constant to predict the accumulation point of the Ricker model from its first two period-doubling bifurcations, $r_1 = 2$ and $r_2 = 2.526$, and compare with the true value 2.692. Why is the prediction poor, and how could it be improved?

   **Answer** If the intervals shrank by the factor $\delta$ from the start, $r_\infty = r_2 + (r_2 - r_1)/(\delta - 1) = 2.526 + 0.526/3.669 = 2.669$, an underestimate by 0.023. The ratio $\delta_n$ converges to 4.669 only asymptotically, and for the Ricker map the early ratios are well below it (the first is about 4.0 for bifurcation points and 3.7 for superstable points, panel B of the figure in Section 12.5): the first intervals shrink more slowly than later ones, so the extrapolation stops too early. Using later bifurcations ($r_3 = 2.656$, $r_4$, …) improves the estimate rapidly: from $r_2$ and $r_3$, $2.656 + 0.130/3.669 = 2.692$.

6. (Open) In the *Tribolium* experiments, the observed populations were close to but not exactly on the predicted attractors. Discuss how demographic noise, environmental noise and the integer nature of populations affect the comparison between a deterministic chaotic model and data, and what kind of evidence is needed to claim that a natural population is chaotic.

   **Answer** Points to cover: a deterministic model predicts an attractor; real counts scatter around it because of demographic noise (random births and deaths, large in small populations), environmental noise (variable temperature, food), and measurement error. Dennis and colleagues therefore fitted stochastic versions of the model and compared predicted and observed one-step-ahead distributions, rather than trajectories, which chaos makes unpredictable beyond a few steps. Because beetles are integers, the state space is a lattice: a deterministic chaotic map on a finite lattice must eventually cycle, so "lattice effects" produce recurrent patterns that a continuous model does not have, and these were seen in the data (Henson et al. 2001). Evidence for chaos in a natural population would require a long time series, a mechanistic or nonparametric model that predicts well out of sample, an estimated Lyapunov exponent with a confidence interval clearly above zero, and ideally experimental manipulation of a parameter that moves the population predictably between regimes, as in *Tribolium*. Without manipulation, alternative explanations (stochastic forcing of a stable but weakly damped system, interactions with unobserved species) are hard to exclude.
