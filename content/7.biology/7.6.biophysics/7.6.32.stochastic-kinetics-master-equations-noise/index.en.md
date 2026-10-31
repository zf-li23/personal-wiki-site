---
title: "Stochastic Kinetics: Master Equations and Noise"
description: "The probabilistic description of chemistry in cells: the Poisson process and waiting times, the chemical master equation and propensities, the birth–death process solved exactly with generating functions, moment equations, the two-state promoter and the Fano factor as a fingerprint of mechanism, protein bursts and the gamma distribution, the Gillespie algorithm, the chemical Langevin equation and the linear noise approximation, noise-induced switching between stable states, and the Luria–Delbrück distribution from its generating function."
---

The rate equations of the earlier chapters treat concentrations as smooth functions of time. In a bacterium, a gene exists in one or two copies, its mRNA in a handful, and many regulators in tens; each event of binding, transcription, translation and degradation is a random encounter, and the numbers of molecules jump by one at random times. Two genetically identical cells in the same medium then differ, and the differences carry information: their size and their statistics reflect the rates and the architecture of the processes that produce them. This chapter develops the mathematics of chemistry with small numbers. It starts from the simplest random process, the arrival of independent events (32.1), writes the general **master equation** for reacting molecules (32.2), solves the problems that can be solved exactly with generating functions and moment equations (32.2–32.4), turns to exact simulation (32.5) and to the Gaussian approximations that hold when numbers are moderately large (32.6), and uses these tools to treat noise-induced switching between stable states (32.7) and the inference of kinetics from fluctuations, ending with the classical case of the Luria–Delbrück distribution (32.8).

The chapter builds on several others. The master equation in general, the Fokker–Planck equation, first-passage times and Kramers' rate were introduced in [7.6.5](/7.6.5#sec-5.5); the biology of stochastic gene expression, with the results of the telegraph model, protein bursts, intrinsic and extrinsic noise and the three-stage noise formula ([7.2.22](/7.2.22#sec-22.5)), is in molecular biology, and here those results are derived and used rather than restated. The distributions and generating functions come from [probability theory](/3.1), Markov chains from [3.5.9](/3.5.9), and the implementation of the Gillespie algorithm from [4.4.7](/4.4.7). The deterministic dynamics of feedback circuits, switches and oscillators is the subject of the next chapter, [7.6.33](/7.6.33); the propagation and control of noise through networks belongs to [systems biology](/7.9).

## 32.1. Randomness from Small Numbers

### 32.1.1. How Small Is Small

The volume of an *E. coli* cell is about $1\,\mathrm{fL}$, so one molecule per cell corresponds to a concentration of $1/(N_{\mathrm{A}} \times 10^{-15}\,\mathrm{L}) \approx 1.7\,\mathrm{nM}$ ([7.6.20](/7.6.20)). A typical gene is present in one or two copies, and in the single-molecule census of Taniguchi and colleagues (2010) most *E. coli* genes had fewer than one mRNA per cell on average and between $0.1$ and $10^4$ proteins. If molecules were made and destroyed independently, the relative fluctuation of a number $N$ would be of order $N^{-1/2}$: $30\,\%$ for ten molecules and $3\,\%$ for a thousand. These are the numbers at which a cell takes decisions: whether to express an operon, to sporulate, to lyse.

The first direct demonstration was the two-color experiment of Elowitz, Levine, Siggia and Swain (2002), in which two copies of the same promoter driving cyan and yellow fluorescent proteins were placed at equivalent positions of the *E. coli* chromosome. Without randomness every cell would be equally cyan and yellow; in fact cells ranged from green to red, the signature of **intrinsic noise** that is uncorrelated between the two copies, superposed on **extrinsic noise** that affects both equally ([7.2.22](/7.2.22#sec-22.5.4)). To predict such variability we need a description of chemistry in terms of probabilities.

### 32.1.2. The Poisson Process

The simplest random sequence of events is one in which events occur independently at a constant rate: transcription initiations from a constitutive promoter, the arrival of photons from a steady source, the decay of radioactive nuclei.

**Definition 32.1.1 (Poisson Process)** A **Poisson process** with rate $\lambda$ is a counting process $N(t)$, the number of events in $[0, t]$, with $N(0) = 0$, whose increments over disjoint intervals are independent and which in a short interval $\mathrm{d}t$ increases by one with probability $\lambda\,\mathrm{d}t + o(\mathrm{d}t)$ and by more than one with probability $o(\mathrm{d}t)$.

**Theorem 32.1.1 (Counts and Waiting Times of a Poisson Process)** For a Poisson process with rate $\lambda$:

1. $N(t)$ has the **Poisson distribution** with mean $\lambda t$, $\mathbb{P}(N(t) = n) = (\lambda t)^n\mathrm{e}^{-\lambda t}/n!$;
2. the waiting times between successive events are independent and have the **exponential distribution** with rate $\lambda$, $\mathbb{P}(\tau > t) = \mathrm{e}^{-\lambda t}$;
3. the time $T_k$ of the $k$-th event has the **gamma distribution** $\Gamma(k, \lambda)$, with density $\lambda(\lambda t)^{k-1}\mathrm{e}^{-\lambda t}/(k-1)!$, mean $k/\lambda$ and variance $k/\lambda^2$.

**Proof** Let $p_n(t) = \mathbb{P}(N(t) = n)$. Conditioning on the last interval $\mathrm{d}t$ gives $p_n(t + \mathrm{d}t) = p_n(t)(1 - \lambda\,\mathrm{d}t) + p_{n-1}(t)\lambda\,\mathrm{d}t$, so $\mathrm{d}p_n/\mathrm{d}t = \lambda(p_{n-1} - p_n)$ with $p_{-1} \equiv 0$. Multiplying by $z^n$ and summing, the **probability generating function** $G(z, t) = \sum_n z^np_n(t)$ ([3.1.11](/3.1.11)) obeys $\partial G/\partial t = \lambda(z - 1)G$ with $G(z, 0) = 1$, so $G = \mathrm{e}^{\lambda t(z - 1)}$, the generating function of the Poisson distribution with mean $\lambda t$. The probability that no event occurs in an interval of length $t$ is $p_0(t) = \mathrm{e}^{-\lambda t}$; by the independence of increments this holds after every event, which gives (2). Finally $\mathbb{P}(T_k > t) = \mathbb{P}(N(t) < k) = \sum_{n<k}(\lambda t)^n\mathrm{e}^{-\lambda t}/n!$, and differentiating with respect to $t$ the sum telescopes to the gamma density in (3). $\square$

The exponential waiting time is memoryless: having waited $s$ without an event does not change the distribution of the remaining wait, $\mathbb{P}(\tau > s + t \mid \tau > s) = \mathrm{e}^{-\lambda t}$. A process whose next event depends on hidden intermediate steps is not memoryless, and this is the first way in which fluctuations reveal mechanism. If each event requires $k$ sequential steps of equal rate, the waiting time is $\Gamma(k, \lambda)$, and its squared coefficient of variation $\operatorname{Var}(\tau)/\mathbb{E}[\tau]^2 = 1/k$ counts the steps: this is the randomness parameter used to count the hidden steps of a molecular motor's cycle ([7.6.27](/7.6.27)). For unequal rates the ratio lies between $1/k$ and $1$, so its inverse is a lower bound on the number of steps.

![The birth–death process of mRNA (production k = 20, degradation γ = 1 per molecule; time in units of the mRNA lifetime), simulated with the Gillespie algorithm. A: five trajectories started with no mRNA, the exact mean k(1 − e^{−γt}) (dark line) and the band of one standard deviation around it; by Theorem 32.2.1 the distribution is Poisson at every time. B: stationary distribution from a long simulation (bars) and the Poisson distribution with mean k/γ (points); the simulated Fano factor is 0.99. C: waiting times between successive production events (orange) follow the exponential distribution with rate k, and waiting times between every fourth event (violet) the gamma distribution Γ(4, k), as in Theorem 32.1.1](./plots/birth-death.py)

## 32.2. The Chemical Master Equation

### 32.2.1. States, Reactions and Propensities

Consider $S$ molecular species in a well-mixed volume $V$, with copy numbers $\boldsymbol{n} = (n_1, \dots, n_S)$, and $R$ reactions. Reaction $j$ changes the state by a fixed vector $\boldsymbol{\nu}_j$, its column of the stoichiometric matrix (for $\ce{A + B -> C}$, $\boldsymbol{\nu} = (-1, -1, +1)$).

**Definition 32.2.1 (Propensity Function)** The **propensity function** $a_j(\boldsymbol{n})$ of reaction $j$ is defined by the statement that, given the state $\boldsymbol{n}$ at time $t$, the probability that reaction $j$ occurs once in $[t, t + \mathrm{d}t)$ is $a_j(\boldsymbol{n})\,\mathrm{d}t$.

For elementary reactions the propensities follow from counting the distinct groups of reactant molecules, the stochastic form of the **law of mass action**:

| Reaction | Propensity | Relation to the deterministic rate constant $k$ |
|---|---|---|
| $\varnothing \to \ce{A}$ (synthesis) | $c$ | $c = kN_{\mathrm{A}}V$ for a rate $k$ in $\mathrm{M\,s^{-1}}$; in molecules per unit time, $c = k$ |
| $\ce{A} \to \cdots$ (first order) | $c\,n_{\mathrm{A}}$ | $c = k$, independent of volume |
| $\ce{A + B} \to \cdots$ | $c\,n_{\mathrm{A}}n_{\mathrm{B}}$ | $c = k/(N_{\mathrm{A}}V)$ |
| $\ce{2A} \to \cdots$ | $c\,n_{\mathrm{A}}(n_{\mathrm{A}} - 1)/2$ | $c = 2k/(N_{\mathrm{A}}V)$ for the reaction rate $v = k[\ce{A}]^2$ |

A bimolecular rate constant of $10^8\,\mathrm{M^{-1}\,s^{-1}}$ (diffusion-limited, [7.6.5](/7.6.5#sec-5.2.3)) in $V = 1\,\mathrm{fL}$ gives $c = 0.17\,\mathrm{s^{-1}}$ per pair of molecules: a single transcription factor finds a single site in about $6\,\mathrm{s}$ by three-dimensional diffusion alone.

**Definition 32.2.2 (Chemical Master Equation)** The **chemical master equation** is the master equation (Definition 5.5.1 of [7.6.5](/7.6.5)) for the probability $P(\boldsymbol{n}, t)$ of the copy numbers of a reacting mixture:
$$
\frac{\partial P(\boldsymbol{n}, t)}{\partial t} = \sum_{j=1}^{R}\Bigl[a_j(\boldsymbol{n} - \boldsymbol{\nu}_j)\,P(\boldsymbol{n} - \boldsymbol{\nu}_j, t) - a_j(\boldsymbol{n})\,P(\boldsymbol{n}, t)\Bigr]. \tag{32.1}
$$
The first term is the flow into $\boldsymbol{n}$ from the state that reaction $j$ converts into $\boldsymbol{n}$, the second the flow out of $\boldsymbol{n}$ by reaction $j$.

Gillespie (1992) derived Eq. (32.1) from the physics of a dilute, well-mixed gas or solution: it is exact when nonreactive collisions, or diffusion, mix the molecules much faster than they react, so that the positions of the molecules are forgotten between reactions. When diffusion is not fast, as for reactions on membranes or in gradients, the volume must be divided into compartments with hopping between them (the reaction–diffusion master equation), and the spatial patterns of [7.6.36](/7.6.36) appear.

**Remark 32.2.1** Multiplying Eq. (32.1) by $\boldsymbol{n}$ and summing gives the exact equation for the means,
$$
\frac{\mathrm{d}\langle\boldsymbol{n}\rangle}{\mathrm{d}t} = \sum_j\boldsymbol{\nu}_j\,\langle a_j(\boldsymbol{n})\rangle .
$$
If every propensity is a linear function of $\boldsymbol{n}$, $\langle a_j(\boldsymbol{n})\rangle = a_j(\langle\boldsymbol{n}\rangle)$ and the means obey the deterministic rate equations exactly. For a bimolecular reaction $\langle n_{\mathrm{A}}n_{\mathrm{B}}\rangle = \langle n_{\mathrm{A}}\rangle\langle n_{\mathrm{B}}\rangle + \operatorname{Cov}(n_{\mathrm{A}}, n_{\mathrm{B}})$: the mean depends on the second moments, these on the third, and the hierarchy does not close. The rate equations are then the limit of large volume at fixed concentrations (Kurtz, 1972), in which the covariances are smaller than the products of the means by a factor of order $1/V$.

### 32.2.2. The Birth–Death Process

The simplest chemical master equation describes the mRNA of a constitutive gene: synthesis at a constant rate $k$, degradation of each molecule with rate constant $\gamma$. It is a **birth–death process** on the copy number $m$:
$$
\frac{\mathrm{d}P(m)}{\mathrm{d}t} = k\bigl[P(m - 1) - P(m)\bigr] + \gamma\bigl[(m + 1)P(m + 1) - mP(m)\bigr], \tag{32.2}
$$
with $P(-1) \equiv 0$.

**Theorem 32.2.1 (Solution of the Birth–Death Process)** Starting from $m_0$ molecules at $t = 0$, the generating function of Eq. (32.2) is
$$
G(z, t) = \bigl[1 + (z - 1)\mathrm{e}^{-\gamma t}\bigr]^{m_0}\exp\Bigl[\frac{k}{\gamma}(z - 1)\bigl(1 - \mathrm{e}^{-\gamma t}\bigr)\Bigr]. \tag{32.3}
$$
The number of molecules is the sum of two independent parts, the survivors of the initial molecules, binomial with $m_0$ trials and survival probability $\mathrm{e}^{-\gamma t}$, and the molecules made since $t = 0$, Poisson with mean $(k/\gamma)(1 - \mathrm{e}^{-\gamma t})$. In the steady state $m$ has the Poisson distribution with mean $k/\gamma$.

**Proof** Multiplying Eq. (32.2) by $z^m$ and summing over $m$, the synthesis terms give $k(z - 1)G$ and the degradation terms $\gamma\sum_m[(m+1)P(m+1) - mP(m)]z^m = \gamma(1 - z)\,\partial G/\partial z$. Hence
$$
\frac{\partial G}{\partial t} + \gamma(z - 1)\frac{\partial G}{\partial z} = k(z - 1)G,
$$
a first-order linear partial differential equation. Along the characteristics $\mathrm{d}z/\mathrm{d}t = \gamma(z - 1)$, that is $z - 1 = (z_0 - 1)\mathrm{e}^{\gamma t}$, it becomes $\mathrm{d}\ln G/\mathrm{d}t = k(z_0 - 1)\mathrm{e}^{\gamma t}$, so $\ln G = \ln G(z_0, 0) + (k/\gamma)(z_0 - 1)(\mathrm{e}^{\gamma t} - 1)$. With $G(z_0, 0) = z_0^{m_0}$ and $z_0 - 1 = (z - 1)\mathrm{e}^{-\gamma t}$ this is Eq. (32.3). The first factor is the generating function of $\mathrm{Bin}(m_0, \mathrm{e}^{-\gamma t})$, the second that of a Poisson distribution, and a product of generating functions is the generating function of a sum of independent variables. As $t \to \infty$ the first factor tends to one. $\square$

The stationary distribution also follows without generating functions. A birth–death chain has no cycles, so in the steady state the net flow between neighboring states vanishes: $kP(m) = (m + 1)\gamma P(m + 1)$, and iterating from $P(0)$ gives $P(m) = P(0)(k/\gamma)^m/m!$. The same argument gives the stationary distribution of any one-dimensional chain with production $f(m)$ and degradation $g(m)$,
$$
P(m) = P(0)\prod_{i=1}^{m}\frac{f(i - 1)}{g(i)}, \tag{32.4}
$$
which we use in 32.6 and 32.7.

### 32.2.3. Moment Equations and the Fano Factor

Most master equations cannot be solved, but equations for the low moments can be derived by multiplying by powers of $\boldsymbol{n}$ and summing. For Eq. (32.2), multiplying by $m$ and by $m^2$ and shifting the summation indices,
$$
\frac{\mathrm{d}\langle m\rangle}{\mathrm{d}t} = k - \gamma\langle m\rangle, \qquad \frac{\mathrm{d}\operatorname{Var}(m)}{\mathrm{d}t} = k + \gamma\langle m\rangle - 2\gamma\operatorname{Var}(m). \tag{32.5}
$$
The variance equation has a simple reading: every reaction event, synthesis or degradation, adds one unit of variance (the source $k + \gamma\langle m\rangle$), and degradation relaxes deviations at rate $\gamma$, which reduces the variance at rate $2\gamma$. In the steady state $\operatorname{Var}(m) = \langle m\rangle = k/\gamma$ and the **Fano factor** $F = \operatorname{Var}/\langle m\rangle$ ([7.2.22](/7.2.22#sec-22.5.2)) equals one. Measured Fano factors of mRNA counts differ from one in characteristic ways, and the rest of the chapter is largely about what the deviations mean.

**Example 32.2.1** A typical *E. coli* gene makes about $10$ mRNAs per minute and its mRNA lives a little more than a minute (PBoC 19.3.1). Equation (32.5) gives a steady state of about $10$ mRNAs per cell with a standard deviation of $\sqrt{10} \approx 3$, and relaxation to it with time constant $1/\gamma$, about $1\,\mathrm{min}$. Since elongation at about $50\,\mathrm{nt\,s^{-1}}$ takes $20\,\mathrm{s}$ for a $1\,\mathrm{kb}$ gene, about three polymerases are transcribing the gene at any time.

## 32.3. Promoter States and the Fano Fingerprint

### 32.3.1. The Two-State Promoter

A promoter that switches between an active state A, in which it makes mRNA at rate $r$, and an inactive state I, in which it is silent, is the telegraph model of [7.2.22](/7.2.22#sec-22.5.2). Let $k_+$ be the rate of activation (I $\to$ A) and $k_-$ of inactivation (A $\to$ I). The state is now the pair (promoter state, $m$), and it is convenient to collect the two probabilities into a vector $\boldsymbol{p}(m) = (p_{\mathrm{A}}(m), p_{\mathrm{I}}(m))^{\mathsf T}$ (Sanchez and colleagues, 2011; PBoC 19.3.3). With
$$
K = \begin{bmatrix} -k_- & k_+ \\ k_- & -k_+ \end{bmatrix}, \qquad R = \begin{bmatrix} r & 0 \\ 0 & 0 \end{bmatrix}, \qquad \Gamma = \gamma I_2,
$$
the master equation is
$$
\frac{\mathrm{d}\boldsymbol{p}(m)}{\mathrm{d}t} = (K - R - m\Gamma)\,\boldsymbol{p}(m) + R\,\boldsymbol{p}(m - 1) + (m + 1)\Gamma\,\boldsymbol{p}(m + 1). \tag{32.6}
$$
The same form describes any promoter architecture: more states enlarge $K$, $R$ and $\Gamma$, and regulators enter through the rates in $K$.

**Theorem 32.3.1 (Moments of the Two-State Promoter)** In the steady state of Eq. (32.6), with $\lambda = k_+ + k_-$,
$$
\langle m\rangle = \frac{r}{\gamma}\,\frac{k_+}{\lambda}, \qquad F = \frac{\operatorname{Var}(m)}{\langle m\rangle} = 1 + \frac{r\,k_-}{\lambda(\lambda + \gamma)}. \tag{32.7}
$$

**Proof** Define the partial moments $\boldsymbol{\mu}_j = \sum_m m^j\boldsymbol{p}(m)$ and $\boldsymbol{u} = (1, 1)$, so that $\langle m^j\rangle = \boldsymbol{u}\cdot\boldsymbol{\mu}_j$. Multiplying Eq. (32.6) by $1$, $m$ and $m^2$, summing, and setting the time derivatives to zero gives
$$
K\boldsymbol{\mu}_0 = \boldsymbol{0}, \qquad (K - \Gamma)\boldsymbol{\mu}_1 + R\boldsymbol{\mu}_0 = \boldsymbol{0}, \qquad (K - 2\Gamma)\boldsymbol{\mu}_2 + (2R + \Gamma)\boldsymbol{\mu}_1 + R\boldsymbol{\mu}_0 = \boldsymbol{0}.
$$
The first equation with $\boldsymbol{u}\cdot\boldsymbol{\mu}_0 = 1$ gives the occupancies $\boldsymbol{\mu}_0 = (k_+, k_-)/\lambda$. Since $\boldsymbol{u}K = \boldsymbol{0}$ (columns of $K$ sum to zero), applying $\boldsymbol{u}$ to the second equation gives $\gamma\langle m\rangle = r\mu_{0,\mathrm{A}}$, the mean. Its A component reads $-(k_- + \gamma)\mu_{1,\mathrm{A}} + k_+\mu_{1,\mathrm{I}} + rk_+/\lambda = 0$; with $\mu_{1,\mathrm{A}} + \mu_{1,\mathrm{I}} = \langle m\rangle$ this gives $\mu_{1,\mathrm{A}} = (k_+\langle m\rangle + rk_+/\lambda)/(\lambda + \gamma)$. Applying $\boldsymbol{u}$ to the third equation gives $2\gamma\langle m^2\rangle = 2r\mu_{1,\mathrm{A}} + \gamma\langle m\rangle + r\mu_{0,\mathrm{A}}$, that is $\langle m^2\rangle = \langle m\rangle + (r/\gamma)\mu_{1,\mathrm{A}}$. Substituting and using $r k_+/\lambda = \gamma\langle m\rangle$,
$$
\operatorname{Var}(m) = \langle m\rangle + \frac{r}{\gamma}\,\frac{k_+\langle m\rangle + \gamma\langle m\rangle}{\lambda + \gamma} - \langle m\rangle^2 = \langle m\rangle\Bigl[1 + \frac{r}{\gamma}\,\frac{k_+ + \gamma}{\lambda + \gamma} - \frac{r}{\gamma}\,\frac{k_+}{\lambda}\Bigr],
$$
and the bracket simplifies to $1 + rk_-/(\lambda(\lambda + \gamma))$. $\square$

This is the telegraph-model result quoted in [7.2.22](/7.2.22#sec-22.5.2), now derived. The derivation shows why moments are the practical tool: the full distribution of Eq. (32.6) is a confluent hypergeometric function (Peccoud and Ycart, 1995), but the first two moments, which are what experiments measure most reliably, need only linear algebra.

**Example 32.3.1** Golding, Paulsson, Zawilski and Cox (2005) followed mRNAs labeled with MS2–GFP in single *E. coli* cells. The labeled transcripts were stabilized by the bound MS2 proteins and were removed only by dilution, $\gamma = 0.014\,\mathrm{min^{-1}}$ (a lifetime of $70\,\mathrm{min}$, the cell cycle); the promoter switched on with $k_+ = 0.03\,\mathrm{min^{-1}}$ and off with $k_- = 0.2\,\mathrm{min^{-1}}$, so it was active $13\,\%$ of the time in episodes of about $5\,\mathrm{min}$; the mean was $\langle m\rangle = 10$. Then $r = \gamma\langle m\rangle\lambda/k_+ = 1.1\,\mathrm{min^{-1}}$ and Eq. (32.7) gives $F = 1 + 1.1 \times 0.2/(0.23 \times 0.244) \approx 4.8$, close to the Fano factor of about $4$ obtained from the variance of the counts.

### 32.3.2. Three Limits

The two-state promoter has three regimes, set by the switching rates relative to $\gamma$ and $r$ (figure below, panel B).

| Regime | Condition | Distribution of $m$ | Fano factor |
|---|---|---|---|
| Fast switching | $k_\pm \gg \gamma$, $rk_-/\lambda^2 \ll 1$ | Poisson with mean $(r/\gamma)k_+/\lambda$: the promoter is averaged over | $\approx 1$ |
| Slow switching | $k_\pm \ll \gamma$ | mixture: Poisson with mean $r/\gamma$ with probability $k_+/\lambda$, zero otherwise | $\approx 1 + (r/\gamma)k_-/\lambda$ |
| Bursts | $k_- \gg k_+, \gamma$ | negative binomial with burst size $b = r/k_-$ and frequency $k_+$ | $\approx 1 + b$ |

In the slow-switching limit the distribution of $m$ is a zero-inflated Poisson distribution:
$$
P(0) = \frac{k_-}{\lambda} + \frac{k_+}{\lambda}\,\mathrm{e}^{-r/\gamma}, \qquad P(m) = \frac{k_+}{\lambda}\,\frac{(r/\gamma)^m\mathrm{e}^{-r/\gamma}}{m!}\quad (m \geq 1).
$$
A measured distribution of this shape gives the two ratios $r/\gamma$ and $k_+/\lambda$ directly from the position of the Poisson peak and the excess of zeros.

Chong, Chen, Ge and Xie (2014) used this logic to find the cause of transcriptional bursting in *E. coli*. Transcription overwinds the DNA ahead of the polymerase and underwinds it behind ([7.2.3](/7.2.3)); in the chromosome, which is anchored into topologically closed domains, the positive supercoils accumulate. Topoisomerase I removes the negative supercoils efficiently, but gyrase, which removes the positive ones, is scarce, of the order of one molecule per domain. In single-molecule experiments in vitro and in cells, transcription from a domain stopped as positive supercoils built up and resumed when a gyrase bound: the ON and OFF states of the bursting gene are the gyrase-bound and gyrase-free states of its domain. Raising the gyrase concentration increased the burst frequency as the two-state model predicts.

### 32.3.3. Reading Mechanism from Noise

The mean of gene expression is set by the product of rates; the Fano factor depends on how the activity is distributed in time, and different architectures with the same mean have different Fano factors (Sanchez and colleagues, 2011; Jones, Brewster and Phillips, 2014). In simple repression, a repressor binds the operator with rate $k_{\mathrm{on}}$, proportional to its concentration, and leaves with rate $k_{\mathrm{off}}$; the promoter is active when the operator is free, so $k_- = k_{\mathrm{on}}$ and $k_+ = k_{\mathrm{off}}$. The fold change, the expression relative to the unrepressed promoter, is $\mathrm{FC} = k_{\mathrm{off}}/(k_{\mathrm{off}} + k_{\mathrm{on}})$, the quantity predicted by the thermodynamic model of [7.2.11](/7.2.11). Substituting $\lambda = k_{\mathrm{off}}/\mathrm{FC}$ and $k_{\mathrm{on}} = k_{\mathrm{off}}(1 - \mathrm{FC})/\mathrm{FC}$ into Eq. (32.7),

$$
F = 1 + \frac{r\,\mathrm{FC}(1 - \mathrm{FC})}{k_{\mathrm{off}} + \gamma\,\mathrm{FC}}. \tag{32.8}
$$
For a fixed fold change, the noise depends on the operator through $k_{\mathrm{off}}$ alone: a strong operator, which the repressor leaves rarely, gives long silent periods and large Fano factors; a weak one, which the repressor leaves in a fraction of a second, gives nearly Poissonian expression. Measuring the mean and the Fano factor of mRNA counts across repressor concentrations therefore distinguishes models that equilibrium measurements cannot, and the residual Fano factor of an unregulated promoter, slightly above one, has been attributed largely to the doubling of gene copies during the cell cycle rather than to promoter kinetics (Jones and colleagues, 2014).

![The Fano factor as a fingerprint of promoter kinetics. A: simple repression with mRNA made at r = 0.33 s⁻¹ from the free promoter and degraded at γ = 0.011 s⁻¹: Fano factor against fold change for three lac operators of different strength, from which the repressor dissociates on average after 7 min (Oid), 2.4 min (O1) and 0.47 s (O3). Lines: Eq. (32.8); points: Gillespie simulations for O1. At the same mean expression, a strong operator produces long silent periods and a large Fano factor; a weak one gives nearly Poisson statistics. B: steady-state distributions of the two-state promoter in the three regimes of 32.3.2 (bars: simulations; points: the limiting distributions): fast switching (k₊ = k₋ = 50γ) gives a Poisson distribution, slow switching (k₊ = k₋ = 0.02γ) a zero-inflated Poisson distribution with nearly half of the cells empty, and short active periods (k₋ = 19k₊ = 38γ) a negative binomial; all three have means near 20](./plots/promoter-fano.py)

## 32.4. Bursts and the Gamma Distribution

### 32.4.1. The Proteins Made from One mRNA

The protein bursts of [7.2.22](/7.2.22#sec-22.5.3) follow from two exponentials. An mRNA lives for an exponentially distributed time $T$ with rate $\gamma_m$; while it lives, it is translated as a Poisson process with rate $k_p$. Given $T$, the number of proteins is Poisson with mean $k_pT$; averaging over $T$,
$$
\mathbb{P}(n) = \int_0^\infty\gamma_m\mathrm{e}^{-\gamma_m t}\,\frac{(k_pt)^n\mathrm{e}^{-k_pt}}{n!}\,\mathrm{d}t = \frac{\gamma_m}{k_p + \gamma_m}\Bigl(\frac{k_p}{k_p + \gamma_m}\Bigr)^n, \qquad n = 0, 1, 2, \dots,
$$
a **geometric distribution** with mean $b = k_p/\gamma_m$, the burst size. The intuition is that of a race: each next event is a translation with probability $q = k_p/(k_p + \gamma_m)$ and the death of the mRNA otherwise, and the burst ends at the first death.

### 32.4.2. A Master Equation with Jumps

When mRNA is short-lived compared with protein ($\gamma_m \gg \gamma_p$), each mRNA can be replaced by an instantaneous burst. Proteins then arrive in bursts at rate $k_m$ (the transcription rate), with geometric sizes $\mathbb{P}(j) = (1 - q)q^j$, and are degraded or diluted with rate constant $\gamma_p$:
$$
\frac{\partial P(n)}{\partial t} = \gamma_p\bigl[(n + 1)P(n + 1) - nP(n)\bigr] + k_m\sum_{j=0}^{n}(1 - q)q^j P(n - j) - k_mP(n). \tag{32.9}
$$

**Theorem 32.4.1 (Bursty Production Gives the Negative Binomial)** The steady state of Eq. (32.9) is the **negative binomial distribution** with generating function
$$
G(z) = \Bigl(\frac{1 - q}{1 - qz}\Bigr)^{a}, \qquad a = \frac{k_m}{\gamma_p}, \qquad \langle n\rangle = ab, \qquad F = 1 + b. \tag{32.10}
$$

**Proof** The burst-size generating function is $\sum_j(1 - q)q^jz^j = (1 - q)/(1 - qz)$, and the sum in Eq. (32.9) is a convolution, whose generating function is the product. Hence, in the steady state, $0 = \gamma_p(1 - z)G'(z) + k_m[(1 - q)/(1 - qz) - 1]G(z)$. Since $(1 - q)/(1 - qz) - 1 = -q(1 - z)/(1 - qz)$, the factor $(1 - z)$ cancels and $G'/G = aq/(1 - qz)$, so $\ln G = -a\ln(1 - qz) + C$, and $G(1) = 1$ fixes $C = a\ln(1 - q)$. The mean is $G'(1) = aq/(1 - q) = ab$, and $G''(1) = a(a + 1)q^2/(1 - q)^2$ gives $\operatorname{Var}(n) = ab(1 + b)$. $\square$

The parameters have direct meanings: $a$ is the number of bursts per protein lifetime and $b$ the number of proteins per burst. When proteins are stable and removed only by dilution, $1/\gamma_p$ is the cell cycle divided by $\ln 2$, and $a$ is about the number of mRNAs made per cell cycle.

### 32.4.3. The Continuous Limit and Feedback

When $b$ is large, the protein number can be treated as a continuous variable $x$ that decays deterministically, $\dot x = -\gamma_px$, and jumps at rate $k_m$ by an exponentially distributed amount with mean $b$ (the continuous version of the geometric distribution). Friedman, Cai and Xie (2006) wrote the corresponding equation for the density $p(x, t)$,
$$
\frac{\partial p}{\partial t} = \frac{\partial}{\partial x}\bigl[\gamma_p x\,p\bigr] + k_m\int_0^x w(x - x')\,p(x')\,\mathrm{d}x' - k_m\,p(x), \qquad w(y) = \frac{1}{b}\,\mathrm{e}^{-y/b}. \tag{32.11}
$$

**Theorem 32.4.2 (Gamma Distribution of Bursty Expression)** The steady state of Eq. (32.11) is the gamma distribution with shape $a = k_m/\gamma_p$ and scale $b$,
$$
p(x) = \frac{x^{a-1}\mathrm{e}^{-x/b}}{\Gamma(a)\,b^a}, \qquad \langle x\rangle = ab, \qquad \eta^2 = \frac{\operatorname{Var}(x)}{\langle x\rangle^2} = \frac{1}{a}. \tag{32.12}
$$
If the burst frequency depends on the protein level, $k_m = k(x)$, as in transcriptional autoregulation, the steady state is
$$
p(x) = \frac{A}{x}\,\mathrm{e}^{-x/b}\exp\Bigl[\int^x\frac{k(x')}{\gamma_px'}\,\mathrm{d}x'\Bigr], \tag{32.13}
$$
with $A$ fixed by normalization.

**Proof** For constant $k_m$, take the **Laplace transform** $L(s) = \int_0^\infty\mathrm{e}^{-sx}p(x)\,\mathrm{d}x$. The drift term transforms, after integration by parts, into $-\gamma_psL'(s)$; the convolution into $k_mL(s)/(1 + bs)$, since the transform of $w$ is $1/(1 + bs)$. The steady state requires $-\gamma_psL' - k_mbs\,L/(1 + bs) = 0$, so $L'/L = -ab/(1 + bs)$ and $L(s) = (1 + bs)^{-a}$, the Laplace transform of the gamma density (32.12). For variable $k(x)$, integrate Eq. (32.11) from $0$ to $x$: the steady state says that the downward probability flux through $x$ by decay, $\gamma_pxp(x)$, equals the upward flux by bursts that start below $x$ and end above it, $\int_0^xk(x')p(x')\mathrm{e}^{-(x - x')/b}\,\mathrm{d}x'$. Writing $J(x)$ for this integral, $J' = k(x)p(x) - J/b$ and $J = \gamma_pxp$, so $J'/J = k(x)/(\gamma_px) - 1/b$; integrating gives $J$, and $p = J/(\gamma_px)$ is Eq. (32.13). $\square$

For negative autoregulation of the burst frequency, $k(x) = k_0/(1 + (x/K)^h)$, the integral is elementary and Eq. (32.13) becomes $p(x) \propto x^{a_0 - 1}\mathrm{e}^{-x/b}(1 + (x/K)^h)^{-a_0/h}$, with $a_0 = k_0/\gamma_p$: the feedback cuts off the upper tail (figure, panel B).

### 32.4.4. Inference from Distributions

Theorem 32.4.2 turns a measured steady-state distribution into kinetic parameters: $b = \operatorname{Var}(x)/\langle x\rangle$ and $a = \langle x\rangle^2/\operatorname{Var}(x)$. Cai, Friedman and Xie (2006) and Yu, Xiao, Ren, Lao and Xie (2006) measured burst sizes and frequencies directly, by counting newly made molecules one at a time, and the values agreed with those obtained by fitting gamma distributions to the steady-state levels ([7.2.22](/7.2.22#sec-22.5.1)). In the census of Taniguchi and colleagues (2010), the protein distributions of almost all of about $1000$ *E. coli* genes fitted gamma distributions; their noise followed $\eta^2 \propto 1/\langle n\rangle$ at low expression, the intrinsic term of Eq. (32.12), and approached a floor of $\eta^2 \approx 0.1$ at high expression, the extrinsic noise shared by all genes. A protein distribution is a time average of a stochastic process, and with a model it reveals the kinetics without any time-resolved measurement; without a model it reveals nothing, since many mechanisms produce gamma-like distributions.

![Protein bursts and the gamma distribution (time in protein lifetimes). A: bursts at frequency a = 3 with geometric sizes of mean b = 8, simulated with the Gillespie algorithm (bars), against the negative binomial of Theorem 32.4.1 (points) and its continuous limit, the gamma distribution of Theorem 32.4.2 (line). B: negative autoregulation of the burst frequency, a(n) = a₀/(1 + (n/K)²) with a₀ = 10, b = 10, K = 30: simulation (bars) and the formula of Friedman, Cai and Xie, Eq. (32.13) (line); the dashed line is the distribution without feedback. C: noise against mean for 300 simulated genes with random burst sizes and frequencies, each cell multiplied by a factor with squared coefficient of variation 0.1 shared by all genes: at low expression η² = (1 + b)/⟨n⟩ (lines for b = 1 and 30), at high expression the extrinsic floor (horizontal line), the two regimes seen in the *E. coli* census](./plots/burst-gamma.py)

## 32.5. Exact Simulation: The Gillespie Algorithm

When no analytical solution exists, the master equation can be sampled exactly. Gillespie (1976, 1977) observed that, in state $\boldsymbol{n}$, the time to the next reaction and its identity have a simple joint distribution. Let $a_0 = \sum_ja_j(\boldsymbol{n})$. The probability that no reaction occurs in $[t, t + \tau)$ satisfies $P_0(\tau + \mathrm{d}\tau) = P_0(\tau)(1 - a_0\,\mathrm{d}\tau)$, so $P_0(\tau) = \mathrm{e}^{-a_0\tau}$, and the probability density that the next reaction occurs at $t + \tau$ and is reaction $j$ is
$$
p(\tau, j) = a_j\,\mathrm{e}^{-a_0\tau} = \underbrace{a_0\mathrm{e}^{-a_0\tau}}_{\text{when}}\cdot\underbrace{\frac{a_j}{a_0}}_{\text{which}}. \tag{32.14}
$$
The two factors are independent: the waiting time is exponential with the total rate, and the reaction is chosen in proportion to its propensity.

**Algorithm 32.5.1 (Gillespie's Direct Method)** Given the initial state $\boldsymbol{n}$ at $t = 0$:

1. Compute all propensities $a_j(\boldsymbol{n})$ and their sum $a_0$; stop if $a_0 = 0$.
2. Draw two independent uniform random numbers $u_1, u_2 \in (0, 1)$.
3. Set $\tau = \ln(1/u_1)/a_0$, an exponential random number with rate $a_0$.
4. Choose the reaction $j$ as the smallest index with $\sum_{i \le j}a_i > u_2a_0$.
5. Update $t \leftarrow t + \tau$ and $\boldsymbol{n} \leftarrow \boldsymbol{n} + \boldsymbol{\nu}_j$, record, and return to step 1.

```python
import numpy as np

def gillespie(n0, nu, propensities, t_max, rng=np.random.default_rng()):
    """Exact stochastic simulation of a reaction network.

    n0: initial copy numbers (length S); nu: stoichiometric changes (R x S);
    propensities: function n -> array of R propensities.
    Returns the jump times and the states after each jump.
    """
    t, n = 0.0, np.array(n0, dtype=int)
    times, states = [t], [n.copy()]
    while t < t_max:
        a = propensities(n)
        a0 = a.sum()
        if a0 == 0:
            break
        t += rng.exponential(1.0 / a0)               # when: exponential with total rate
        j = np.searchsorted(np.cumsum(a), rng.random() * a0)   # which: in proportion to a_j
        n += nu[j]
        times.append(t)
        states.append(n.copy())
    return np.array(times), np.array(states)

# birth-death process of mRNA: production k, degradation gamma per molecule
k, gamma = 20.0, 1.0
nu = np.array([[1], [-1]])
times, states = gillespie([0], nu, lambda n: np.array([k, gamma * n[0]]), t_max=50.0)
```

Each trajectory is one possible history of one cell. Averages over the stationary state can be taken either over many trajectories or, for an ergodic system, over time along one long trajectory, weighting each state by the time spent in it (the waiting times $\tau$), not by the number of visits. The algorithm is exact but costs one step per reaction event, which is prohibitive when some species are abundant and react often. Two families of refinements are standard: the next-reaction method of Gibson and Bruck (2000), which updates only the propensities affected by each reaction and uses a priority queue for the next times; and τ-leaping (Gillespie, 2001), which advances by a fixed interval $\tau$ in which every reaction $j$ fires a Poisson-distributed number of times with mean $a_j\tau$, valid when no propensity changes appreciably in $\tau$. Hybrid methods treat abundant species by the Langevin equation of the next section and rare ones exactly. The performance of the direct method in Python, with compiled and parallel versions, is measured in [4.4.7](/4.4.7#sec-7.3).

## 32.6. The Chemical Langevin Equation and the Linear Noise Approximation

### 32.6.1. From Jumps to Gaussian Noise

If, in a time $\mathrm{d}t$, every reaction fires many times while the propensities change little, the number of firings of reaction $j$ is Poisson with a large mean $a_j\,\mathrm{d}t$, and therefore approximately Gaussian with that mean and variance. Adding the changes of all reactions gives a stochastic differential equation.

**Definition 32.6.1 (Chemical Langevin Equation)** The **chemical Langevin equation** for the copy numbers $\boldsymbol{X}(t)$, treated as continuous, is
$$
\mathrm{d}\boldsymbol{X} = \sum_{j=1}^{R}\boldsymbol{\nu}_j\,a_j(\boldsymbol{X})\,\mathrm{d}t + \sum_{j=1}^{R}\boldsymbol{\nu}_j\sqrt{a_j(\boldsymbol{X})}\,\mathrm{d}W_j(t), \tag{32.15}
$$
where the $W_j$ are independent Wiener processes, one for each reaction (Gillespie, 2000).

The drift is the deterministic rate equation; each reaction adds its own **white noise** of strength equal to its propensity. The equivalent **Fokker–Planck equation** (Definition 5.5.2 of [7.6.5](/7.6.5)) has drift $\boldsymbol{A}(\boldsymbol{x}) = \sum_j\boldsymbol{\nu}_ja_j$ and diffusion matrix $B(\boldsymbol{x}) = \sum_j\boldsymbol{\nu}_j\boldsymbol{\nu}_j^{\mathsf T}a_j$; it is the Kramers–Moyal expansion of Eq. (32.1) truncated at second order. Equation (32.15) is the chemical counterpart of the **Langevin equation** of Brownian motion, with one difference of principle: the noise is not added from outside with a strength fixed by temperature, but generated by the reactions themselves, so that it vanishes where the reactions stop and is larger where the system is more active.

### 32.6.2. The Linear Noise Approximation

The chemical Langevin equation is nonlinear and rarely solvable, but in a large volume the fluctuations are small compared with the means and can be linearized. Van Kampen's system-size expansion writes $\boldsymbol{n} = \Omega\boldsymbol{\phi}(t) + \Omega^{1/2}\boldsymbol{\xi}$, where $\Omega$ is the volume (or any measure of the typical copy number), $\boldsymbol{\phi}$ the concentrations and $\boldsymbol{\xi}$ the fluctuations, and collects powers of $\Omega$. At the leading order $\boldsymbol{\phi}$ obeys the rate equations; at the next order $\boldsymbol{\xi}$ obeys a linear Langevin equation, a multivariate **Ornstein–Uhlenbeck process**.

**Definition 32.6.2 (Linear Noise Approximation)** The **linear noise approximation** describes the fluctuations of copy numbers around a stable steady state $\boldsymbol{x}^*$ of the rate equations $\dot{\boldsymbol{x}} = \sum_j\boldsymbol{\nu}_ja_j(\boldsymbol{x})$ as a Gaussian process with mean zero whose covariance matrix $C$ satisfies
$$
\frac{\mathrm{d}C}{\mathrm{d}t} = JC + CJ^{\mathsf T} + D, \qquad J = \frac{\partial}{\partial\boldsymbol{x}}\sum_j\boldsymbol{\nu}_ja_j\Big|_{\boldsymbol{x}^*}, \qquad D = \sum_j\boldsymbol{\nu}_j\boldsymbol{\nu}_j^{\mathsf T}a_j(\boldsymbol{x}^*), \tag{32.16}
$$
and in the steady state the Lyapunov equation $JC + CJ^{\mathsf T} + D = 0$; the stationary autocovariance is $\langle\delta\boldsymbol{x}(t + \tau)\,\delta\boldsymbol{x}(t)^{\mathsf T}\rangle = \mathrm{e}^{J\tau}C$ for $\tau \geq 0$.

Equation (32.16) is a balance between the dissipation of fluctuations by the deterministic relaxation ($J$, whose eigenvalues have negative real parts at a stable state) and their creation by the reactions ($D$), the chemical analog of the fluctuation–dissipation relation of [7.6.5](/7.6.5#sec-5.4). For networks with linear propensities it is exact for the second moments at any size, since then the moment hierarchy closes (Remark 32.2.1); the proof of the three-stage noise formula in [7.2.22](/7.2.22#sec-22.5) is precisely the solution of such a Lyapunov equation. For nonlinear networks it is the first correction to the rate equations and fails near bifurcations, where $J$ becomes singular, and for molecules present in a few copies.

**Example 32.6.1 (mRNA and Protein)** Let mRNA $m$ be made at rate $k_m$ and degraded with $\gamma_m$, and protein $p$ be made at rate $k_pm$ and degraded with $\gamma_p$. With $\boldsymbol{x} = (m, p)$,
$$
J = \begin{bmatrix} -\gamma_m & 0 \\ k_p & -\gamma_p\end{bmatrix}, \qquad D = \begin{bmatrix} 2\gamma_m\langle m\rangle & 0 \\ 0 & 2\gamma_p\langle p\rangle\end{bmatrix},
$$
since in the steady state synthesis and degradation of each species occur at equal rates. The three independent entries of the Lyapunov equation are solved in turn: $C_{mm} = \langle m\rangle$; $k_pC_{mm} - (\gamma_m + \gamma_p)C_{mp} = 0$, so $C_{mp} = k_p\langle m\rangle/(\gamma_m + \gamma_p)$; and $2k_pC_{mp} - 2\gamma_pC_{pp} + 2\gamma_p\langle p\rangle = 0$, so
$$
\frac{\operatorname{Var}(p)}{\langle p\rangle^2} = \frac{1}{\langle p\rangle} + \frac{1}{\langle m\rangle}\,\frac{\gamma_p}{\gamma_m + \gamma_p}, \qquad F_p = 1 + \frac{k_p}{\gamma_m + \gamma_p},
$$
the result of Thattai and van Oudenaarden (2001). For $\gamma_m \gg \gamma_p$ the Fano factor is $1 + b$, as in Theorem 32.4.1. The mRNA–protein correlation coefficient is $C_{mp}/\sqrt{C_{mm}C_{pp}} = \sqrt{\gamma_p/(\gamma_m + \gamma_p)}\cdot\sqrt{b'/(1 + b')}$ with $b' = k_p/(\gamma_m + \gamma_p)$: when mRNA is short-lived the protein level is poorly correlated with the instantaneous mRNA level, because the protein integrates the history of mRNA over its own lifetime. This is one reason why single-cell mRNA and protein counts of the same gene correlate weakly (Taniguchi and colleagues, 2010).

### 32.6.3. Feedback and the Fano Factor

For a single species made with rate $f(x)$ and degraded with $\gamma x$, Eq. (32.16) has $J = f'(x^*) - \gamma$ and $D = f(x^*) + \gamma x^* = 2\gamma x^*$, so
$$
F = \frac{\operatorname{Var}(x)}{x^*} = \frac{\gamma}{\gamma - f'(x^*)} = \frac{1}{1 + H}, \qquad H = -\frac{f'(x^*)}{\gamma}. \tag{32.17}
$$
The dimensionless gain $H$ is the logarithmic sensitivity of production to the level, relative to that of removal. Negative autoregulation ($H > 0$) suppresses the noise below the Poisson level; positive autoregulation ($H < 0$) amplifies it, and as $H \to -1$, the point at which the steady state loses stability and the system becomes bistable ([7.6.33](/7.6.33)), the variance diverges together with the relaxation time $1/(\gamma(1 + H))$. Both signatures, large fluctuations and slow relaxation, announce an approaching bifurcation. Becskei and Serrano (2000) observed the reduction of cell-to-cell variation by negative autoregulation of a synthetic TetR circuit in *E. coli*. When proteins are made in bursts the noise sources are larger, but the attenuation factor of Eq. (32.17) applies to the slow fluctuations in the same way; negative feedback cannot, however, remove noise faster than it can respond, and Lestas, Vinnicombe and Paulsson (2010) showed that there are information-theoretic lower bounds on how far any feedback can suppress noise that originates in a few molecules.

![The linear noise approximation for an autoregulated gene, a birth–death chain with production f(n) and degradation n, whose exact stationary distribution is Eq. (32.4). A: Fano factor against the feedback gain H = −f′(x*)/γ at the deterministic steady state, exact values (points) for negative autoregulation f = β/(1 + (n/20)⁴) with increasing β (H > 0) and for positive autoregulation f = 2 + β₁n/(40 + n) with increasing β₁ (H < 0), and the prediction of the linear noise approximation, F = 1/(1 + H), Eq. (32.17) (line). B: exact distributions for strong negative feedback (violet, H = 3.9) and for positive feedback with H = −0.6 (red), with Poisson distributions of the same means (lines): negative feedback narrows the distribution below the Poisson width, positive feedback broadens it](./plots/lna.py)

## 32.7. Switching Between Stable States

### 32.7.1. Bistability Plus Noise

A gene that activates its own transcription cooperatively can have two stable steady states, off and on (the positive feedback module of [7.3.18](/7.3.18#sec-18.4.3); the deterministic analysis is in [7.6.33](/7.6.33)). With noise, a cell in one state eventually crosses to the other, and a clonal population becomes a mixture: the stationary distribution is bimodal, and the deterministic **bistability** becomes a statement about two long-lived states and the rates of jumping between them. For a one-dimensional chain the stationary distribution is exact, Eq. (32.4), and it defines an effective potential $\Phi(n) = -\ln P(n)$ whose minima are the stable states and whose maximum lies near the deterministic threshold. The mean waiting time to switch is also exact.

**Theorem 32.7.1 (Mean First-Passage Time of a Birth–Death Chain)** For a chain with birth rates $f(n)$ and death rates $g(n)$, reflecting at $0$, with stationary distribution $P_{\mathrm{s}}(n)$ from Eq. (32.4), the mean first-passage time from $n_0$ to $n_1 > n_0$ is
$$
T(n_0 \to n_1) = \sum_{k=n_0}^{n_1 - 1}\frac{1}{f(k)P_{\mathrm{s}}(k)}\sum_{i=0}^{k}P_{\mathrm{s}}(i). \tag{32.18}
$$

**Proof** Let $T_k$ be the mean time to go from $k$ to $k + 1$ for the first time. From $k$, the next event occurs after a mean time $1/(f(k) + g(k))$ and is a birth with probability $f(k)/(f(k) + g(k))$; after a death the chain must return to $k$ first. Hence $T_k = 1/(f(k) + g(k)) + [g(k)/(f(k) + g(k))](T_{k-1} + T_k)$, that is $f(k)T_k = 1 + g(k)T_{k-1}$, with $T_0 = 1/f(0)$. Multiplying by $P_{\mathrm{s}}(k)$ and using $g(k)P_{\mathrm{s}}(k) = f(k-1)P_{\mathrm{s}}(k-1)$ from Eq. (32.4), the quantity $y_k = f(k)P_{\mathrm{s}}(k)T_k$ obeys $y_k = P_{\mathrm{s}}(k) + y_{k-1}$, so $y_k = \sum_{i \le k}P_{\mathrm{s}}(i)$. Summing $T_k$ from $n_0$ to $n_1 - 1$ gives Eq. (32.18). $\square$

The sum is dominated by the states near the barrier, where $P_{\mathrm{s}}$ is smallest, and the switching time is approximately $\mathrm{e}^{\Delta\Phi}$ times a prefactor, the discrete counterpart of the Kramers rate (Theorem 5.6.2 of [7.6.5](/7.6.5)). In the potential of a chemical system the barrier $\Delta\Phi$ is not an energy divided by $k_{\mathrm{B}}T$ but grows in proportion to the system size: if all copy numbers scale with $\Omega$, $\Phi(n) \approx \Omega\,\phi(n/\Omega)$ with a quasi-potential $\phi$ independent of $\Omega$, and the switching time grows as $\mathrm{e}^{\Omega\Delta\phi}$. A switch built from tens of molecules flips in a few lifetimes; one built from hundreds may be stable for longer than the organism lives. The chemical Langevin equation reproduces the exponential dependence but generally with the wrong barrier, because the rare paths over the barrier are made of large deviations of the jump process that a Gaussian approximation does not represent; switching rates must be computed from the master equation itself or by large-deviation methods.

![Stochastic switching of a bistable self-activating gene: a birth–death chain with production f(n) = Ω[0.05 + s⁴/(1 + s⁴)], s = n/(0.4Ω), and degradation n (time in protein lifetimes), so that the system size Ω sets the number of molecules in the on state. A: a Gillespie trajectory for Ω = 30, with long dwells near n ≈ 1 (off) and n ≈ 30 (on) and rapid transitions between them. B: the exact stationary distribution, Eq. (32.4) (line), and the time-weighted distribution of the trajectory in A (bars); the effective potential −ln P(n) (dashed, right axis) has a barrier near the deterministic threshold. C: mean time to switch from off to on against Ω, from 30 simulated switches per point (points) and from Theorem 32.7.1 (line): the switching time grows exponentially with the size of the system](./plots/switching.py)

### 32.7.2. Examples

**Example 32.7.1 (The lac Operon)** At intermediate concentrations of a non-metabolizable inducer, a clonal population of *E. coli* splits into fully induced and uninduced cells, because the permease LacY, made from the operon, imports its own inducer (the deterministic bistability is analyzed in [7.6.33](/7.6.33)). Choi, Cai, Frieda and Xie (2008) asked what makes an uninduced cell switch. By counting single LacY molecules they found two kinds of bursts: frequent small bursts, of one or a few molecules, produced when the tetrameric LacI repressor briefly releases one of the two operators of its DNA loop and rebinds at once; and rare large bursts, of tens of molecules, produced when the repressor dissociates completely from the DNA and must find the operator again. Only the large bursts produce enough permease to cross the threshold of the positive feedback. The switch is thus triggered by a single-molecule event, the complete dissociation of one repressor, and the rate of switching is set by the rate of that event and by the threshold, not by the average expression level.

**Example 32.7.2 (Lysogeny)** The prophage state of phage λ is maintained by the repressor CI activating its own promoter and repressing Cro ([7.2.11](/7.2.11)). It is extraordinarily stable: in cells lacking RecA, which cannot induce the SOS response that destroys CI, spontaneous switching to lysis was measured to occur in fewer than one in $10^7$ cells per generation (Little, Shepley and Wert, 1999). With a few hundred CI molecules per cell, this stability is consistent with the exponential dependence of the switching time on the number of molecules, and it is a classic test case for stochastic models of genetic switches (Aurell and Sneppen, 2002).

**Example 32.7.3 (Single Channels)** A **two-state system** such as a channel with a closed and an open state is the smallest switch ([7.6.4](/7.6.4)). Its open and closed dwell times are exponential, with means equal to the inverse rates. If the closed class contains several states connected by transitions, the closed-time distribution becomes a sum of exponentials, one for each state of the class (Colquhoun and Hawkes, 1981), so the number of components in a measured dwell-time histogram is a lower bound on the number of hidden states, which is how gating schemes are inferred from single-channel recordings ([7.6.30](/7.6.30)).

## 32.8. Fluctuations as a Source of Kinetic Information

### 32.8.1. What the Statistics Reveal

The examples of this chapter use the same principle: a deterministic model predicts averages from which only combinations of rates can be inferred, while the statistics of fluctuations depend on the rates separately and on the order of the steps.

| Statistic | Model | What it reveals |
|---|---|---|
| Fano factor of mRNA counts | two-state promoter, Theorem 32.3.1 | burst size; switching relative to degradation; operator strength at fixed mean (Eq. (32.8)) |
| Shape of protein distributions | bursty production, Theorems 32.4.1–32.4.2 | burst frequency $a$ and size $b$ from a snapshot |
| Waiting-time distributions | sequential steps, Theorem 32.1.1 | number of rate-limiting steps ($1/k$ from the squared coefficient of variation) |
| Dwell-time histograms of single molecules | Markov chain of conformations | number of hidden states (number of exponentials) |
| Autocorrelation of fluctuations in one cell | linear noise approximation, $\mathrm{e}^{J\tau}C$ | lifetimes and feedback without perturbing the cell |
| Cross-correlation of two reporters | two-color experiment | intrinsic and extrinsic noise ([7.2.22](/7.2.22#sec-22.5.4)); direction of regulation from the time lag |
| Distribution of mutants among cultures | Luria–Delbrück | that mutation precedes selection; the **mutation rate** |

For a birth–death process the autocorrelation of the fluctuations decays as $\mathrm{e}^{-\gamma\tau}$, and a gene under negative feedback relaxes faster, at $\gamma(1 + H)$: Austin and colleagues (2006) used the frequency content of the noise of a synthetic autoregulated gene to measure the effect of feedback, and Dunlop, Cox, Levine, Murray and Elowitz (2008) used the time lags in the cross-correlation of fluctuations between genes to infer which regulates which. These methods treat noise as a natural perturbation applied by the cell to itself.

### 32.8.2. The Luria–Delbrück Distribution from Its Generating Function

The first and most consequential use of fluctuations to decide a biological question was the **fluctuation test** of Luria and Delbrück (1943), whose design, history and estimators are described in [7.4.12](/7.4.12#sec-12.4): if resistance to phage arises by mutation during growth, the number of resistant cells in parallel cultures has a variance far greater than its mean, whereas resistance induced by exposure gives Poisson statistics. Here we derive the distribution itself as a stochastic process, which is an exercise in generating functions.

Let the wild-type population grow deterministically, $N(u) = N_0\mathrm{e}^u$ (time in units of the inverse growth rate), and let mutations occur as a Poisson process with rate $\mu N(u)$, $\mu$ per cell per unit time. Each mutant founds a clone that grows as a pure birth (Yule) process; a clone that started at age $s$ before the end has a geometric size, $\mathbb{P}(k) = x(1 - x)^{k-1}$ for $k \geq 1$, with $x = \mathrm{e}^{-s}$ (Lea and Coulson, 1949).

**Theorem 32.8.1 (Generating Function of the Luria–Delbrück Distribution)** In the limit $N_0/N_t \to 0$, with $m = \mu N_t$ the expected number of mutations, the number $r$ of mutants in a culture has the generating function
$$
G(z) = \exp\Bigl[m\,\frac{1 - z}{z}\,\ln(1 - z)\Bigr]. \tag{32.19}
$$
Its probabilities obey the recursion $p_0 = \mathrm{e}^{-m}$, $p_r = \frac{m}{r}\sum_{k=0}^{r-1}\frac{p_k}{r - k + 1}$, and for large $r$, $p_r \approx m/r^2$.

**Proof** The number of mutants is a compound Poisson sum: mutations occur at times $u$ with rate $\mu N_0\mathrm{e}^u$, and each contributes an independent clone with generating function $g_s(z) = xz/(1 - (1 - x)z)$, $x = \mathrm{e}^{-s}$, $s = t - u$. For such a sum $\ln G = \int(\text{rate})\,(g - 1)\,\mathrm{d}u$. With $\mu N_0\mathrm{e}^{u} = m\mathrm{e}^{-s}$ and $\mathrm{d}s = -\mathrm{d}x/x$,
$$
\ln G = \int_{\mathrm{e}^{-t}}^{1}m\,(g - 1)\,\mathrm{d}x \to -m(1 - z)\int_0^1\frac{\mathrm{d}x}{1 - z + zx} = m\,\frac{1 - z}{z}\ln(1 - z),
$$
since $g - 1 = -(1 - z)/(1 - z + zx)$. The change of variable shows a simple structure: a mutant clone is geometric with a success parameter $x$ uniformly distributed on $(0, 1)$, because the number of cells, and with it the number of mutation opportunities, grows exactly as fast as clones started earlier outgrow later ones. For the recursion, write $\ln G = m\,h(z)$ with $h(z) = \frac{1 - z}{z}\ln(1 - z) = -1 + \sum_{k\geq1}\frac{z^k}{k(k + 1)}$; then $G' = mh'G$, and comparing coefficients of $z^{r-1}$ with $h'(z) = \sum_{k\geq1}z^{k-1}/(k + 1)$ gives $rp_r = m\sum_{k=0}^{r-1}p_k/(r - k + 1)$. The singularity of $h$ at $z = 1$, $h \approx -(1 - z)\ln(1 - z)$, implies a tail $p_r \approx m/r^2$ by standard singularity analysis, so that $\mathbb{P}(R \geq r) \approx m/r$. $\square$

The tail $m/r^2$ has an infinite mean in the limit of an infinite culture: in a finite culture the mean is $m\ln(N_t/N_0)$ ([7.4.12](/7.4.12#sec-12.4.2)), dominated by jackpots from the earliest mutations, which is why the sample mean is useless as an estimator of $m$ and the maximum-likelihood method based on the recursion is the standard. The model's assumptions, deterministic growth of the wild type, equal growth of mutants, Poisson mutations, and no phenotypic lag, can each be relaxed (Zheng, 1999), and direct observation of mutations in single cells by microfluidics has shown that mutations indeed occur as a Poisson process in time (Robert and colleagues, 2018).

![The Luria–Delbrück distribution from its generating function, Eq. (32.19). A: exact probabilities from the recursion of Theorem 32.8.1 for m = 1 (blue) and m = 4 (red) expected mutations per culture (lines), and frequencies from 10⁵ simulated cultures (points), in which each of a Poisson number of mutations founds a clone of geometric size with a success probability drawn uniformly from (0, 1), as in the proof; the dashed lines are the asymptote m/r², the dotted curves Poisson distributions with mean m, which an induced mechanism with comparable numbers would give. B: the probability of at least r mutants and its heavy tail m/r (dashed): a culture with hundreds or thousands of mutants is not rare](./plots/luria-delbruck.py)

## Summary

- Poisson process (Definition 32.1.1, Theorem 32.1.1): counts Poisson, waiting times exponential and memoryless, the $k$-th event gamma; $\operatorname{Var}(\tau)/\mathbb{E}[\tau]^2 = 1/k$ counts sequential steps.
- Chemical master equation (Definitions 32.2.1–32.2.2, Eq. (32.1)): propensities from the stochastic law of mass action; exact for well-mixed systems; the means obey the rate equations exactly only for linear propensities (Remark 32.2.1).

| Tool | Result | Where |
|---|---|---|
| Generating function | birth–death: binomial survivors + Poisson newcomers, stationary Poisson | Theorem 32.2.1 |
| Detailed balance of a chain | $P(m) \propto \prod f(i - 1)/g(i)$ | Eq. (32.4) |
| Moment equations | $F = 1$ for birth–death; two-state promoter $F = 1 + rk_-/(\lambda(\lambda + \gamma))$ | Eq. (32.5), Theorem 32.3.1 |
| Fano fingerprint | simple repression $F = 1 + r\,\mathrm{FC}(1 - \mathrm{FC})/(k_{\mathrm{off}} + \gamma\mathrm{FC})$ | Eq. (32.8) |
| Burst master equation | negative binomial, $\langle n\rangle = ab$, $F = 1 + b$ | Theorem 32.4.1 |
| Continuous bursts | gamma $(a, b)$; with feedback Eq. (32.13) | Theorem 32.4.2 |
| Exact simulation | exponential waiting time with $a_0$, reaction with probability $a_j/a_0$ | Algorithm 32.5.1 |
| Gaussian approximation | chemical Langevin equation; linear noise approximation $JC + CJ^{\mathsf T} + D = 0$ | Definitions 32.6.1–32.6.2 |
| Feedback | $F = 1/(1 + H)$: negative feedback sub-Poissonian, positive feedback diverging at the bifurcation | Eq. (32.17) |
| First passage | exact switching time of a chain, $\propto \mathrm{e}^{\Omega\Delta\phi}$ | Theorem 32.7.1 |
| Compound Poisson | Luria–Delbrück $G(z) = \exp[m(1 - z)z^{-1}\ln(1 - z)]$, tail $m/r^2$ | Theorem 32.8.1 |

- Fluctuations carry kinetic information that averages do not: burst parameters, numbers of hidden steps and states, lifetimes and feedback, and the order of mutation and selection (32.8.1).

## Questions

1. A protein made from a constitutive gene has $\langle p\rangle = 50$ and $\operatorname{Var}(p) = 500$ in a population of *E. coli*. Interpret these numbers with the burst model, and estimate how many mRNAs per cell cycle the gene makes. What measurement would test the interpretation?

   **Answer** With Theorem 32.4.1, $F = 1 + b = 10$ gives a burst size $b = 9$ proteins per mRNA and a burst frequency $a = \langle p\rangle/b \approx 5.6$ bursts per protein lifetime. If the protein is stable and removed only by dilution, the lifetime is $T_{\mathrm{cycle}}/\ln 2$, so the gene makes about $5.6\ln 2 \approx 3.9$ mRNAs per cell cycle. Extrinsic noise also contributes to the variance, so this $b$ is an upper bound. A direct test is to count newly made molecules in time-lapse (as Yu and colleagues did), which gives $a$ and $b$ independently, or to measure the mRNA distribution by smFISH (mean about $a\gamma_p/\gamma_m$ per cell, Poisson for a constitutive promoter).

2. Show that for the birth–death process the stationary autocorrelation of the mRNA number is $\langle\delta m(t + \tau)\delta m(t)\rangle = (k/\gamma)\mathrm{e}^{-\gamma\lvert\tau\rvert}$, and explain how this allows the mRNA lifetime to be measured in unperturbed cells.

   **Answer** Conditioning on $m(t)$, the mean of $m(t + \tau)$ obeys Eq. (32.5): $\mathbb{E}[m(t + \tau)\mid m(t)] = k/\gamma + (m(t) - k/\gamma)\mathrm{e}^{-\gamma\tau}$. Multiplying by $\delta m(t)$ and averaging gives $\operatorname{Var}(m)\mathrm{e}^{-\gamma\tau} = (k/\gamma)\mathrm{e}^{-\gamma\tau}$, and the function is even in $\tau$ for a stationary process. This is $\mathrm{e}^{J\tau}C$ of Definition 32.6.2 with $J = -\gamma$. The decay time of the autocorrelation of the fluctuations in a single cell's time course is therefore the mRNA lifetime, obtained without blocking transcription with drugs (which disturb the cell). In practice the measured signal is filtered by the reporter's own lifetime, which must be accounted for.

3. Derive Eq. (32.5) from Eq. (32.2), and generalize it to the variance equation of a species made at rate $f(x)$ and removed at rate $g(x)$, treated in the linear noise approximation.

   **Answer** Multiplying Eq. (32.2) by $m$ and summing, shifted sums give $\sum mP(m-1) = \langle m\rangle + 1$ and $\sum m(m+1)P(m+1) = \langle m^2\rangle - \langle m\rangle$, so $\mathrm{d}\langle m\rangle/\mathrm{d}t = k - \gamma\langle m\rangle$. With $m^2$: $\sum m^2P(m-1) = \langle m^2\rangle + 2\langle m\rangle + 1$ and $\sum m^2(m+1)P(m+1) = \langle m^3\rangle - 2\langle m^2\rangle + \langle m\rangle$, so $\mathrm{d}\langle m^2\rangle/\mathrm{d}t = k(2\langle m\rangle + 1) + \gamma(\langle m\rangle - 2\langle m^2\rangle)$; subtracting $\mathrm{d}\langle m\rangle^2/\mathrm{d}t = 2\langle m\rangle(k - \gamma\langle m\rangle)$ gives the variance equation. In general, $\mathrm{d}\operatorname{Var}/\mathrm{d}t = 2(f'(x^*) - g'(x^*))\operatorname{Var} + f(x^*) + g(x^*)$, the one-dimensional Eq. (32.16).

4. A transcription factor is present at $20$ molecules in an *E. coli* cell ($1\,\mathrm{fL}$) and binds its operator with a diffusion-limited rate constant of $10^8\,\mathrm{M^{-1}\,s^{-1}}$ and $K_{\mathrm{D}} = 1\,\mathrm{nM}$. Compute the propensities of binding and unbinding, the fraction of time the operator is occupied, and the mean durations of the bound and free periods. Would the promoter appear bursty if it makes mRNA when free at $r = 0.5\,\mathrm{min^{-1}}$ and the mRNA lifetime is $3\,\mathrm{min}$?

   **Answer** $c_{\mathrm{on}} = k_{\mathrm{on}}/(N_{\mathrm{A}}V) = 10^8/(6.0\times10^{8}) = 0.17\,\mathrm{s^{-1}}$ per molecule, so the binding propensity is $20 \times 0.17 = 3.3\,\mathrm{s^{-1}}$; $k_{\mathrm{off}} = k_{\mathrm{on}}K_{\mathrm{D}} = 0.1\,\mathrm{s^{-1}}$. Occupancy $= 3.3/(3.3 + 0.1) = 0.97$ (equivalently, $20$ molecules is $33\,\mathrm{nM}$, and $33/(33 + 1) = 0.97$). Bound periods last $10\,\mathrm{s}$ on average, free periods $0.3\,\mathrm{s}$. Both are much shorter than the mRNA lifetime ($\lambda = 3.4\,\mathrm{s^{-1}} \gg \gamma = 0.0056\,\mathrm{s^{-1}}$), and $rk_-/(\lambda(\lambda+\gamma)) = (0.0083 \times 3.3)/(3.4 \times 3.4) \approx 0.002$, so $F \approx 1$: the switching is averaged out and expression is Poissonian with mean $(r/\gamma)\times 0.03 = 1.5 \times 0.029 \approx 0.04$ mRNA per cell. A bursty appearance requires bound periods comparable to or longer than the mRNA lifetime, that is much smaller $k_{\mathrm{off}}$ (a stronger operator, as in Eq. (32.8)).

5. Implement Algorithm 32.5.1 for the dimerization reaction $\ce{2A <=> A2}$ with $N = 20$ monomers in total, $c_1 = 0.05$ (association propensity $c_1n_{\mathrm{A}}(n_{\mathrm{A}} - 1)/2$) and $c_2 = 1$ (dissociation propensity $c_2n_{\mathrm{A_2}}$). Compare the stationary mean number of dimers with the deterministic prediction and explain the difference.

   **Answer** Detailed balance between states with $d$ and $d + 1$ dimers gives the exact stationary distribution: $P(d + 1)/P(d) = c_1(N - 2d)(N - 2d - 1)/(2c_2(d + 1))$, from which (or from the simulation) $\langle d\rangle \approx 3.76$. The deterministic equation $c_1n_{\mathrm{A}}^2/2 = c_2d$ with $n_{\mathrm{A}} = N - 2d$ treats $n(n-1)$ as $n^2$ and ignores fluctuations; it gives $d \approx 3.82$. The stochastic mean is lower because a molecule cannot dimerize with itself, which the factor $n(n-1)$ counts and $n^2$ does not, an effect of relative size $1/n_{\mathrm{A}}$; for nonlinear propensities $\langle a(n)\rangle \neq a(\langle n\rangle)$ (Remark 32.2.1). The difference disappears as $N \to \infty$ at fixed concentration.

   ```python
   import numpy as np
   N, c1, c2 = 20, 0.05, 1.0
   w = [1.0]
   for d in range(N // 2):
       nA = N - 2 * d
       w.append(w[-1] * c1 * nA * (nA - 1) / (2 * c2 * (d + 1)))
   w = np.array(w) / sum(w)
   print((np.arange(w.size) * w).sum())      # exact stochastic mean, about 3.76
   from scipy.optimize import brentq
   print(brentq(lambda d: c1 * (N - 2 * d) ** 2 / 2 - c2 * d, 0, N / 2))   # deterministic, about 3.82
   ```

6. Use the linear noise approximation to show that negative autoregulation with gain $H$ speeds up the relaxation of fluctuations by the factor $1 + H$ and reduces their variance by the same factor. Why can both not be achieved by simply increasing the degradation rate of an unregulated protein at the same mean level?

   **Answer** With $J = -\gamma(1 + H)$ the autocorrelation decays at $\gamma(1 + H)$, and $C = D/(2\gamma(1 + H)) = x^*/(1 + H)$. For an unregulated protein, increasing $\gamma$ at fixed mean requires increasing the synthesis rate in proportion: the relaxation speeds up by the same factor, but the variance stays equal to the mean (Poisson), because the noise source $D = 2\gamma x^*$ grows as fast as the dissipation. Feedback differs because it increases dissipation (the restoring slope) without increasing the number of reaction events, which are the source of the noise. The price is the cost of making and maintaining the regulatory circuit, and the attenuation is limited for noise faster than the feedback loop.

7. In a fluctuation test with $50$ cultures of $10^8$ cells each, $18$ cultures have no resistant mutants. Estimate $m$ and the mutation rate, and use the asymptote of Theorem 32.8.1 to estimate how many cultures you expect to contain more than $100$ mutants.

   **Answer** $p_0 = 18/50 = 0.36 = \mathrm{e}^{-m}$ gives $m = 1.02$, and $\mu = m/N_t = 1.0 \times 10^{-8}$ per cell per generation. The tail $\mathbb{P}(R \geq r) \approx m/r$ gives $\mathbb{P}(R > 100) \approx 0.01$, so about $0.5$ of the $50$ cultures, one jackpot in every two such experiments. (The exact recursion gives a similar value; the finite culture size truncates the tail only near $r \sim N_t/N_0$.)

8. (Open question) A gene's protein shows a bimodal distribution in a clonal population. List three different mechanisms that could produce bimodality, and design measurements that distinguish them using the ideas of this chapter.

   **Answer** (1) Bistability from positive feedback (32.7): the two states are long-lived; sorting cells from each peak and regrowing them shows memory, followed by slow relaxation to the bimodal mixture at a rate that depends on the inducer and on the number of molecules; the bimodality disappears if the feedback loop is broken (for example by expressing the feedback component constitutively). (2) Slow promoter switching without feedback (the slow-switching limit of 32.3.2, with long-lived protein replaced by a fast reporter): bimodality appears in mRNA counts as a zero-inflated Poisson distribution; time-lapse shows ON and OFF periods whose durations are exponential and independent of the expression level, and breaking feedback does not remove it. (3) Extrinsic heterogeneity, for example two subpopulations differing in cell-cycle stage, growth rate or a regulator controlled elsewhere: a second reporter of a different, unrelated promoter co-varies with the first (two-color correlation, 32.8.1), and conditioning on cell size or stage removes the bimodality. Distinguishing (1) from (2) uses the dependence of the dwell times on the protein level and the effect of the feedback; distinguishing both from (3) uses the intrinsic–extrinsic decomposition.

9. For the two-state promoter, show directly from Theorem 32.3.1 that, at fixed mean $\langle m\rangle$ and fixed fraction of active time $f = k_+/\lambda$, the Fano factor decreases monotonically as the switching rate $\lambda$ increases, and find its limits.

   **Answer** With $r = \gamma\langle m\rangle/f$ and $k_- = (1 - f)\lambda$, $F = 1 + \gamma\langle m\rangle(1 - f)/(f(\lambda + \gamma))$, which decreases monotonically with $\lambda$. As $\lambda \to 0$, $F \to 1 + \langle m\rangle(1 - f)/f = 1 + (r/\gamma)(1 - f)$, the slow-switching (zero-inflated) limit; as $\lambda \to \infty$, $F \to 1$, the Poisson limit. The switching rate at which noise is halved between the limits is $\lambda = \gamma$: promoter kinetics affect the noise when the promoter switches on the time scale of the mRNA lifetime or more slowly.
