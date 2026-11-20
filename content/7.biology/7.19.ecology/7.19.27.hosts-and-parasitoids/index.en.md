---
title: "Hosts and Parasitoids: Discrete-Time Dynamics and Aggregation"
description: "Host–parasitoid population dynamics in discrete time: the Nicholson–Bailey model derived from Poisson encounters, with a complete proof of its oscillatory instability via the Jury conditions; stabilization by host density dependence, aggregation of risk (May's negative binomial model, k < 1, and the CV² > 1 rule), interference and refuges; spatial persistence in coupled map lattices; and the theory and practice of classical biological control."
---

Parasitoids are the insects whose larvae develop in or on a single host arthropod and kill it ([Definition 39.2.1](/7.17.39#def-39.2.1) of 7.17.39). They are the most species-rich group of natural enemies, the most important agents of biological control, and the best material for population models: generations of host and parasitoid are often synchronized, each parasitized host yields parasitoids instead of hosts, and the number of hosts attacked can be counted directly. These features make discrete-time models natural, and the questions of [7.19.25](/7.19.25) and [7.19.26](/7.19.26) (does the interaction oscillate, and what stabilizes it?) can be answered for them with exact, elementary mathematics.

Section 27.1 sets up the general framework; Section 27.2 analyzes the Nicholson–Bailey model and proves that it is always unstable; Section 27.3 examines the mechanisms that can stabilize the interaction, above all heterogeneity in the risk of parasitism; Section 27.4 adds space; Section 27.5 turns to biological control, where the theory is tested. The natural history of parasitoids (host finding, host regulation, behavioral manipulation, superparasitism) is in [7.17.39](/7.17.39), which also gives a first account of the models below; the stability theory of discrete maps in one variable is in [7.19.12](/7.19.12), and delayed density dependence in [7.19.13](/7.19.13).

## 27.1. The Framework

Let $H_t$ be the number of hosts and $P_t$ the number of adult female parasitoids in generation $t$. A general host–parasitoid model has the form

$$
H_{t+1} = \lambda H_t\,f(H_t, P_t), \qquad P_{t+1} = cH_t\bigl[1 - f(H_t, P_t)\bigr], \tag{27.1}
$$
where

- $\lambda$ is the net rate of increase of unparasitized hosts per generation (the host's **finite rate of increase**, [7.19.10](/7.19.10));
- $f$ is the fraction of hosts that escape parasitism, the *escape function*, which contains all the biology of searching, aggregation and interference;
- $c$ is the number of adult female parasitoids emerging from one parasitized host (for a solitary parasitoid, at most one, times the proportion of females and the survival of the immatures; for a gregarious one, the brood size times the same factors).

The model assumes that parasitism acts before other mortality in the host's life cycle, or that other mortality is density independent and absorbed into $\lambda$; that each parasitized host yields parasitoids regardless of how many eggs it received (superparasitism wastes eggs but not hosts); and that parasitoids have one generation per host generation. The parasitoid's equation contains no birth rate of its own: its reproduction is entirely determined by the hosts it kills, which is what makes the parasitoid model a model of a specialist natural enemy.

A parasitoid is not a hyperparasitoid, although the two terms are sometimes confused: a hyperparasitoid is a parasitoid of other parasitoids ([7.17.39](/7.17.39)), a third trophic level whose dynamics are not described by Eq. (27.1).

## 27.2. The Nicholson–Bailey Model

### 27.2.1. Derivation

Nicholson (1933) and Nicholson and Bailey (1935) assumed that parasitoids search at random and independently of one another, each searching an area $a$ during its lifetime, its *area of discovery*. In a habitat of unit area, the total number of encounters between parasitoids and hosts is then $aP_tH_t$, and these encounters fall on hosts at random. The number of encounters experienced by a particular host is therefore approximately Poisson distributed with mean $aP_t$ (the limit of a binomial distribution with many parasitoid searches, each with a small chance of hitting this host), and the probability that a host is not encountered at all is the zero term of the **Poisson distribution**, $f = \mathrm{e}^{-aP_t}$.

**Definition 27.2.1 (Nicholson–Bailey Model)** The **Nicholson–Bailey model** is Eq. (27.1) with random search, $f = \mathrm{e}^{-aP_t}$:

$$
H_{t+1} = \lambda H_t\,\mathrm{e}^{-aP_t}, \qquad P_{t+1} = cH_t\bigl(1 - \mathrm{e}^{-aP_t}\bigr). \tag{27.2}
$$

The parasitoid's functional response is implicit in the model: each parasitoid's share of the hosts attacked is $H_t(1 - \mathrm{e}^{-aP_t})/P_t$, which tends to $aH_t$ when parasitoids are few. Random search with unlimited eggs and no handling time is the discrete-time equivalent of the type I response of the Lotka–Volterra model ([7.19.25](/7.19.25#sec-25.4)), and the exponential arises because a host that has already been found once cannot be killed twice.

### 27.2.2. The Equilibrium

Setting $H_{t+1} = H_t = H^*$ in the host equation gives $\mathrm{e}^{-aP^*} = 1/\lambda$, and the parasitoid equation then gives $H^*$:

$$
P^* = \frac{\ln\lambda}{a}, \qquad H^* = \frac{\lambda\ln\lambda}{(\lambda - 1)ac}. \tag{27.3}
$$
At equilibrium a fraction $1 - 1/\lambda$ of the hosts is parasitized, exactly the surplus that the host produces. The equilibrium host density is inversely proportional to the parasitoid's searching efficiency $a$ and productivity $c$: a good parasitoid holds its host at low density, which is the point of biological control. As in the Lotka–Volterra model, the equilibrium of each species is set by the parameters of the other.

### 27.2.3. Instability

Stability of a fixed point of a two-dimensional map requires both eigenvalues of the Jacobian matrix to lie inside the unit circle (the generalization of the condition $\lvert F'(N^*)\rvert < 1$ of [Theorem 12.1.1](/7.19.12#thm-12.1.1) of 7.19.12). For $2 \times 2$ matrices this can be checked without computing the eigenvalues.

**Lemma 27.2.1 (Jury Conditions)** Both eigenvalues of a real $2 \times 2$ matrix $J$ with trace $\tau$ and determinant $\Delta$ lie strictly inside the unit circle if and only if

$$
\lvert\tau\rvert < 1 + \Delta \qquad\text{and}\qquad \Delta < 1.
$$

**Proof** The eigenvalues are the roots of $p(z) = z^2 - \tau z + \Delta$. If they are complex conjugates, their common modulus is $\sqrt\Delta$, so they lie inside the circle if and only if $\Delta < 1$; and then $\tau^2 < 4\Delta$ gives $\lvert\tau\rvert < 2\sqrt\Delta \le 1 + \Delta$, so the first condition holds as well. If they are real, $z_1 \le z_2$, the condition $\lvert\tau\rvert < 1 + \Delta$ is the same as $p(1) > 0$ and $p(-1) > 0$, which says that neither $1$ nor $-1$ lies in $[z_1, z_2]$. Under this condition both roots lie in $(-1, 1)$ unless both exceed $1$ or both lie below $-1$, and in either case $\Delta = z_1z_2 > 1$; so $\Delta < 1$ excludes them. Conversely, roots in $(-1, 1)$ give $\Delta = z_1z_2 < 1$ and $p(\pm1) = (1 \mp z_1)(1 \mp z_2) > 0$. $\square$

When the conditions fail because $\Delta$ crosses 1 with complex eigenvalues, the equilibrium loses stability through a pair of complex eigenvalues leaving the unit circle, the discrete counterpart of a Hopf bifurcation (a Neimark–Sacker bifurcation), and the departures from equilibrium oscillate.

**Theorem 27.2.1 (Instability of the Nicholson–Bailey Equilibrium)** For every $\lambda > 1$, $a > 0$ and $c > 0$, the eigenvalues of the linearization of Eq. (27.2) at $(H^*, P^*)$ are complex conjugates of modulus $\sqrt{\lambda\ln\lambda/(\lambda - 1)} > 1$. The equilibrium is unstable, and small perturbations grow into oscillations of increasing amplitude with a period of approximately $2\pi/\theta$ generations, where $\cos\theta = \tau/(2\sqrt\Delta)$.

**Proof** Write $s = \ln\lambda/(\lambda - 1)$. At the equilibrium $\mathrm{e}^{-aP^*} = 1/\lambda$ and $acH^* = \lambda s$, so the partial derivatives of the map $(H, P) \mapsto (\lambda H\mathrm{e}^{-aP},\ cH(1 - \mathrm{e}^{-aP}))$ are

$$
J = \begin{bmatrix} \lambda\mathrm{e}^{-aP^*} & -a\lambda H^*\mathrm{e}^{-aP^*} \\ c(1 - \mathrm{e}^{-aP^*}) & acH^*\mathrm{e}^{-aP^*}\end{bmatrix} = \begin{bmatrix} 1 & -aH^* \\ c(1 - 1/\lambda) & s\end{bmatrix}.
$$
Hence

$$
\tau = 1 + s, \qquad \Delta = J_{11}J_{22} - J_{12}J_{21} = s + acH^*\Bigl(1 - \frac1\lambda\Bigr) = s + \lambda s\,\frac{\lambda - 1}{\lambda} = \lambda s.
$$

Two elementary inequalities finish the proof. For $\lambda > 1$, let $g(\lambda) = \lambda\ln\lambda - (\lambda - 1)$; then $g(1) = 0$ and $g'(\lambda) = \ln\lambda > 0$, so $g > 0$, which is $\Delta = \lambda s > 1$. And $\ln\lambda < \lambda - 1$ gives $s < 1$. Therefore $\tau^2 = (1 + s)^2 < 4 < 4\Delta$, so the eigenvalues are complex, with modulus $\sqrt\Delta > 1$: by Lemma 27.2.1 the equilibrium is unstable, and the linearized solutions are spirals $\Delta^{t/2}(\alpha\cos\theta t + \beta\sin\theta t)$ that grow geometrically while rotating by the angle $\theta$ per generation. $\square$

![The Nicholson–Bailey model, Eq. (27.2), with λ = 2, a = 0.05 and c = 1, started with 5 % more hosts than at equilibrium. A: hosts and parasitoids (log scale) oscillate with growing amplitude around the equilibrium values (dotted), the parasitoid lagging behind the host, until the host population crashes after about 30 generations. B: the same trajectory in the phase plane (log axes), an outward spiral from the equilibrium (open circle). C: the modulus of the complex eigenvalues of the linearization, √(λ ln λ/(λ − 1)), exceeds 1 for every λ > 1 (Theorem 27.2.1), so the equilibrium is always unstable; the dashed curve gives the period 2π/θ of the oscillation, about 8 generations at λ = 2 and decreasing toward 5 for large λ](./plots/nb-dynamics.py)

Two remarks clarify the result. First, the instability is not caused by the discreteness of time alone: it is the discrete counterpart of the neutral Lotka–Volterra cycles made unstable by the one-generation delay between parasitism and the emergence of the next parasitoid generation, a delay that acts like the time lags of [7.19.13](/7.19.13). Second, the mechanism is overexploitation. When hosts are abundant, parasitoids multiply until they find nearly every host; the hosts crash, and the parasitoids crash after them; because the escape fraction $\mathrm{e}^{-aP}$ falls steeply with $P$ and nothing limits the parasitoids except hosts, nothing damps the swings. A stable interaction requires a mechanism that weakens parasitism when parasitoids are abundant.

The model's prediction is clear and wrong: natural host–parasitoid systems are not driven to extinction within a few dozen generations. Laboratory systems do show the predicted behavior in simple arenas: in Nicholson's classic cultures and in the azuki bean weevil *Callosobruchus chinensis* with the braconid *Heterospilus prosopidis* (Utida 1957), the populations oscillated regularly; Utida's system persisted for more than a hundred generations, which already pointed to stabilizing factors not in Eq. (27.2).

## 27.3. Stabilizing Mechanisms

### 27.3.1. Host Density Dependence

The simplest addition is self-limitation of the host. Beddington, Free and Lawton (1975) used the Ricker model ([7.19.12](/7.19.12)) for the host:

$$
H_{t+1} = H_t\exp\Bigl[r\Bigl(1 - \frac{H_t}{K}\Bigr) - aP_t\Bigr], \qquad P_{t+1} = cH_t\bigl(1 - \mathrm{e}^{-aP_t}\bigr). \tag{27.4}
$$
The natural measure of the parasitoid's effect is the depression ratio $q = H^*/K$, the equilibrium host density as a fraction of its carrying capacity. The stability region, computed from the eigenvalues at the equilibrium, has a simple shape (Figure 3A): the equilibrium is stable when $q$ is large enough, roughly $q > 0.35$–$0.6$ depending on $r$, and unstable when the parasitoid depresses the host far below $K$; for large $r$ instability also returns near $q = 1$, where the host's own overcompensating density dependence produces oscillations ([7.19.12](/7.19.12)). Host density dependence therefore stabilizes only a weak parasitoid. An efficient parasitoid, which holds the host at a few percent of $K$, meets hosts that hardly feel their own density, and the Nicholson–Bailey instability reappears. This is the theoretical problem of biological control (Section 27.5.2).

### 27.3.2. Aggregation of Risk: May's Model

The most important stabilizing mechanism is heterogeneity in the risk of parasitism. Parasitoids aggregate in patches with many hosts, some hosts live in places that are hard to search, and searching efficiency varies among parasitoids and over time. May (1978) captured all of this phenomenologically by replacing the Poisson distribution of attacks per host by a **negative binomial distribution** with the same mean $aP_t$ and a clumping parameter $k > 0$.

The negative binomial arises naturally as a mixture. Suppose host $i$ has an individual risk $\varepsilon_i$, a random variable with a **gamma distribution** of mean 1 and shape $k$, so that its squared coefficient of variation is $1/k$, and that, given $\varepsilon_i$, the attacks on host $i$ are Poisson with mean $aP_t\varepsilon_i$. The number of attacks per host is then negative binomial, and the escape probability is the Laplace transform of the gamma distribution:

$$
f = \mathbb{E}\bigl[\mathrm{e}^{-aP_t\varepsilon}\bigr] = \int_0^\infty \mathrm{e}^{-aP_tu}\,\frac{k^ku^{k-1}\mathrm{e}^{-ku}}{\Gamma(k)}\,\mathrm{d}u = \Bigl(1 + \frac{aP_t}{k}\Bigr)^{-k}.
$$
By Jensen's inequality ($\mathrm{e}^{-x}$ is convex), this exceeds $\mathrm{e}^{-aP_t}$: heterogeneous risk always lets more hosts escape than random search with the same mean. As $k \to \infty$ the risk becomes uniform and $f \to \mathrm{e}^{-aP_t}$; for small $k$ attacks are concentrated on a minority of hosts, and the escape fraction falls only slowly as parasitoids increase (Figure 2A).

**Formula 27.3.1 (May's Negative Binomial Model)**

$$
H_{t+1} = \lambda H_t\Bigl(1 + \frac{aP_t}{k}\Bigr)^{-k}, \qquad P_{t+1} = cH_t\Bigl[1 - \Bigl(1 + \frac{aP_t}{k}\Bigr)^{-k}\Bigr]. \tag{27.5}
$$

**Theorem 27.3.1 (May 1978)** For every $\lambda > 1$, Eq. (27.5) has the equilibrium

$$
P^* = \frac{k(\lambda^{1/k} - 1)}{a}, \qquad H^* = \frac{\lambda P^*}{(\lambda - 1)c},
$$
which is locally asymptotically stable if $k < 1$ and unstable if $k > 1$.

**Proof** The equilibrium follows from $(1 + aP^*/k)^k = \lambda$ and $P^* = cH^*(1 - 1/\lambda)$. Write $u = \lambda^{-1/k}$, so that $1 + aP^*/k = 1/u$ and $f(P^*) = 1/\lambda$, and note $f'(P) = -a(1 + aP/k)^{-k-1}$, so $f'(P^*) = -au/\lambda$. The Jacobian of $(H, P) \mapsto (\lambda Hf(P),\ cH(1 - f(P)))$ at the equilibrium is

$$
J = \begin{bmatrix} 1 & \lambda H^*f'(P^*) \\ c(1 - 1/\lambda) & -cH^*f'(P^*)\end{bmatrix} = \begin{bmatrix} 1 & -aH^*u \\ c(1 - 1/\lambda) & acH^*u/\lambda \end{bmatrix}.
$$
With $acH^* = \lambda aP^*/(\lambda - 1) = \lambda k(1/u - 1)/(\lambda - 1)$,

$$
J_{22} = \frac{k(1 - u)}{\lambda - 1}, \qquad -J_{12}J_{21} = acH^*u\Bigl(1 - \frac1\lambda\Bigr) = k(1 - u),
$$
so that

$$
\tau = 1 + \frac{k(1 - u)}{\lambda - 1}, \qquad \Delta = J_{22} - J_{12}J_{21} = \frac{k\lambda(1 - u)}{\lambda - 1}.
$$
The first Jury condition holds: $1 + \Delta - \tau = k(1 - u) > 0$ and $\tau > 0$. So stability is equivalent to $\Delta < 1$, that is, with $\mu = 1/k$,

$$
\varphi(\lambda) := \mu(\lambda - 1) - \lambda + \lambda^{1 - \mu} > 0.
$$
Now $\varphi(1) = 0$ and $\varphi'(\lambda) = \mu - 1 + (1 - \mu)\lambda^{-\mu} = (\mu - 1)(1 - \lambda^{-\mu})$. For $\lambda > 1$ the second factor is positive, so $\varphi$ is increasing if $\mu > 1$ ($k < 1$), giving $\varphi(\lambda) > 0$ and stability, and decreasing if $\mu < 1$ ($k > 1$), giving $\varphi(\lambda) < 0$ and instability. $\square$

The criterion does not depend on $\lambda$, $a$ or $c$: whatever the host's rate of increase, clumping with $k < 1$ stabilizes. As $k \to \infty$, $\Delta \to \lambda\ln\lambda/(\lambda - 1)$, recovering Theorem 27.2.1. At $k = 1$, $\Delta = 1$ exactly, the boundary case.

![Aggregation of risk and May's model. A: the fraction of hosts escaping parasitism as a function of the mean number of attacks per host aP, for random (Poisson) search, e^(−aP), and negative binomial attacks, (1 + aP/k)^(−k), with k = 2, 1 and 0.5: the more clumped the attacks, the larger the fraction of hosts that escape even when parasitoids are abundant. B: May's model, Eq. (27.5), with λ = 2, a = 0.05 and c = 1, started at twice the host and half the parasitoid equilibrium: for k = 0.5 the oscillations are damped (solid), for k = 2 they grow (dashed). C: the determinant of the linearization against λ for k = 0.25, 0.5, 1, 2 and the Nicholson–Bailey limit (dashed); the equilibrium is stable where det J < 1, which holds for all λ if and only if k < 1 (Theorem 27.3.1)](./plots/may-aggregation.py)

Why does aggregation stabilize? Not because parasitoids prefer dense patches as such, but because heterogeneity creates a partial refuge whose effect is density dependent. When parasitoids are few, they find hosts nearly as efficiently as random searchers; when they are many, they pile up on the hosts that are at high risk, attacking them repeatedly (wasting eggs), while low-risk hosts continue to escape. The parasitoid population as a whole thus suffers from what looks like interference: its per capita success declines with its own density. Free, Beddington and Lawton (1977) called this *pseudo-interference*.

### 27.3.3. The CV² > 1 Rule

May's model is phenomenological: $k$ summarizes many possible causes of heterogeneity. Hassell, May, Pacala and Chesson (1991) showed that a wide class of models of parasitoids foraging in patchy environments, with different rules for how parasitoids distribute themselves among patches, shares an approximate stability criterion.

**Proposition 27.3.1 (CV² > 1 Rule)** Let $p_i$ be the density of searching parasitoids in the patch of host $i$ and $\mathrm{CV}^2$ the squared coefficient of variation of $p_i$ over hosts (weighted by host numbers), evaluated at equilibrium. Then, approximately, the host–parasitoid equilibrium is stable if $\mathrm{CV}^2 > 1$.

For May's model the risk has $\mathrm{CV}^2 = 1/k$, and the rule reproduces $k < 1$ exactly. The rule's value is practical: $\mathrm{CV}^2$ can be estimated from field data on the distribution of parasitism among patches. It can also be partitioned into a part due to parasitoids aggregating in response to host density (density-dependent aggregation) and a part independent of host density, and both contribute equally to stability. Analyses of field data (Pacala and Hassell 1991) found $\mathrm{CV}^2 > 1$ in a minority of systems, and the part independent of host density was usually the larger, a surprise for the earlier view that stability comes from parasitoids tracking host-dense patches. The rule is approximate and fails when, for instance, parasitoid aggregation is too strong relative to the host's rate of increase, or when the parasitoid's distribution changes within a generation (Murdoch and Stewart-Oaten 1989).

### 27.3.4. Interference and Refuges

Two further mechanisms complete the classical list (Figure 3).

- Mutual interference. Hassell and Varley (1969) observed that the area of discovery of parasitoids declines with their density, $a = QP^{-m}$, a straight line on log–log axes with slope $-m$, the interference constant. Substituting into Eq. (27.2) gives $f = \exp(-QP_t^{1 - m})$. The equilibrium is stable when interference is strong enough, $m$ above a threshold that increases with $\lambda$ (Figure 3B): a host with a high rate of increase needs a strongly interfering parasitoid. Part of the interference measured in experiments is pseudo-interference caused by aggregation.
- Refuges. A refuge protecting a constant proportion $\beta$ of hosts gives $f = \beta + (1 - \beta)\mathrm{e}^{-aP_t}$. Coexistence requires $\beta\lambda < 1$, otherwise the protected hosts alone increase and escape control; stability requires $\beta$ close to $1/\lambda$ (Figure 3C), a refuge so large that the host's equilibrium is high. A refuge protecting a constant number of hosts is more strongly stabilizing, for the same reason as in continuous time ([7.19.26](/7.19.26#sec-26.1.4)).

A type III functional response, which in continuous time can stabilize ([7.19.26](/7.19.26#sec-26.1.4)), is much less effective in host–parasitoid models: the parasitoid's response to host density within a generation is overwhelmed by the delay between generations. Host stage structure, with only some stages vulnerable, and differences in development time between host and parasitoid can also stabilize, and they turned out to be decisive in the best-studied field system (Section 27.5.2).

![Stability regions of three modified Nicholson–Bailey models, computed from the eigenvalues at the equilibrium (green: stable; red: unstable). A: host density dependence, Eq. (27.4): stable only if the parasitoid holds the host at a large fraction q = H*/K of its carrying capacity; for high host growth rates r the host's own overcompensation destabilizes near q = 1. B: Hassell–Varley interference, a = QP^(−m): stable when the interference constant m exceeds a threshold that rises with λ. C: a refuge for a constant proportion β of hosts: coexistence requires βλ < 1 (gray region excluded), and stability requires β close to 1/λ, that is, a refuge large enough to keep host density high](./plots/stabilizing-mechanisms.py)

## 27.4. Host–Parasitoid Dynamics in Space

Spatial structure can stabilize the regional dynamics even if every local population is unstable, the idea demonstrated with predatory mites by Huffaker ([7.19.26](/7.19.26#sec-26.5.3)). Hassell, Comins and May (1991) formalized it as a coupled map lattice: a grid of patches, in each of which the Nicholson–Bailey model operates, followed in each generation by dispersal of a fraction $\mu_H$ of the hosts and $\mu_P$ of the parasitoids to the neighboring patches. Local dynamics are violently unstable, and the outcome depends on the two dispersal fractions and the size of the grid.

- For intermediate dispersal of both species, patterns of spiral waves develop: hosts spread into empty space, parasitoids follow, and the parasitoids' local overexploitation leaves a trail of empty patches behind the wave front, which the hosts recolonize. The spirals rotate slowly and are self-sustaining (Figure 4A).
- When hosts disperse little and parasitoids moderately, the patterns are irregular in space and time, spatial chaos (Figure 4B).
- When hosts disperse little and parasitoids disperse very widely, the pattern locks into a fixed or slowly changing mosaic, which Hassell and colleagues called a crystal lattice (Figure 4C shows such a checkerboard texture mixed with irregular patches).

The total numbers fluctuate within bounds and persist indefinitely (Figure 4D), although no local population is stable and the spatially homogeneous model goes extinct. Persistence requires a large enough grid: with the parameters of Figure 4, the interaction persisted on a $30 \times 30$ lattice but the parasitoid was lost on $20 \times 20$ and smaller lattices, after which the host, lacking density dependence, increased without limit. The regional population persists as a **metapopulation** ([7.19.16](/7.19.16)) in which local extinctions are balanced by recolonization, and the spatial patterns are the same as those of excitable media in physics and chemistry (the continuous reaction–diffusion version is treated in [7.19.30](/7.19.30)). Field evidence for such self-organized patterns is limited, but traveling waves of abundance have been documented in cyclic populations, including voles in Kielder Forest and larch budmoth outbreaks across the Alps, whose waves travel from southwest to northeast.

![Host–parasitoid dynamics in space: a coupled map lattice after Hassell, Comins and May (1991). On each cell of a 50 × 50 grid the Nicholson–Bailey model runs with λ = 2, a = 1 and c = 1; then a fraction μ_H of the hosts and μ_P of the parasitoids in each cell disperses equally to the eight neighboring cells (individuals leaving the grid are lost). The simulation starts with both species in the central cell. A–C: host density (log scale; background color = few hosts, green = many) after 1500 generations: spiral waves for μ_H = μ_P = 0.5; spatial chaos for μ_H = 0.05, μ_P = 0.3; a checkerboard texture with irregular patches for μ_H = 0.05, μ_P = 0.9. D: the mean number of hosts per cell over generations 1200–1500 in the spiral case: the regional populations fluctuate within bounds and persist, although every local population is unstable](./plots/coupled-map-lattice.py)

## 27.5. Biological Control

### 27.5.1. Classical Successes

Classical **biological control** is the introduction of natural enemies from the native range of an introduced pest, with the aim of a permanent reduction of the pest. Parasitoids are the most frequently used agents. The history of the method is full of instructive cases.

- Cottony cushion scale. The Australian scale insect *Icerya purchasi* threatened the citrus industry of California in the 1880s. In 1888–1889 Albert Koebele sent from Australia a few hundred individuals of the vedalia beetle *Rodolia cardinalis* (a predatory ladybird) and the parasitic fly *Cryptochaetum iceryae*; within two years the scale was controlled throughout the state. The case founded the method, and its later disruption by DDT illustrated the Volterra principle ([7.19.25](/7.19.25#sec-25.2.2)).
- Cassava mealybug. *Phenacoccus manihoti*, a South American pest, reached central Africa in the early 1970s and spread through the cassava belt, causing heavy losses of a staple crop. The encyrtid parasitoid *Anagyrus lopezi* (formerly *Epidinocarsis lopezi*), found in Paraguay, was released from 1981 by the International Institute of Tropical Agriculture under Hans Herren and established in more than twenty-five countries, reducing mealybug densities to low levels across most of the continent; it is one of the largest successes of biological control.
- Coconut moth in Fiji. The zygaenid moth *Levuana iridescens* defoliated coconut palms in Fiji until the tachinid fly *Bessa remota* was introduced from Malaysia in 1925. Within a few years the moth became rare, and it has not been recorded for decades. *Bessa* also attacked other zygaenids, and the native *Heteropan dolens* has also disappeared. The case is often cited as biological control driving a target and a non-target species to extinction; whether *Levuana* was native to Fiji, and whether it is truly extinct, have been debated (Kuris 2003), but it was a central argument for the host-specificity testing now required before releases.
- Winter moth in Nova Scotia, controlled by two introduced parasitoids ([7.17.39](/7.17.39)), and many others; overall, roughly a third of introduced agents establish, and a smaller fraction of introductions achieve substantial control.

### 27.5.2. The Theoretical Problem

The ideal agent, from the farmer's point of view, holds the pest at a density far below its carrying capacity ($q = H^*/K$ small) and keeps it there stably. The models show the tension: the Nicholson–Bailey equilibrium can be made as low as desired by increasing $a$, but it is unstable; host density dependence stabilizes only if $q$ is large (Figure 3A); aggregation stabilizes at any $q$, but only if it is strong ($k < 1$). Two explanations of successful control have been proposed.

1. Stable low equilibria maintained by heterogeneity of risk, refuges or stage structure. The best-studied case is the California red scale *Aonidiella aurantii* on citrus, controlled since the late 1950s by *Aphytis melinus*, an aphelinid introduced from India and Pakistan. Red scale densities are low and remarkably constant. Murdoch and colleagues tested the classical stabilizing mechanisms one by one. Scales on the interior bark of trees form a partial refuge from *Aphytis*, but removing the refuge experimentally did not destabilize the system; parasitism was not aggregated in a way that would satisfy the $\mathrm{CV}^2$ rule; and local populations on single trees were as stable as the regional population, so metapopulation dynamics were not responsible. The most likely explanation lies in the stage structure: *Aphytis* attacks only some scale stages, and it develops much faster than its host, which, in stage-structured models, provides strong stabilization (Murdoch, Briggs and Nisbet 2003).
2. Nonequilibrium control: local populations of pest and enemy go extinct repeatedly, and control is maintained regionally because the enemy finds and destroys pest outbreaks before they spread, as in the spatial models of Section 27.4. Murdoch, Chesson and Chesson (1985) argued that many successful programs look like this rather than like stable equilibria.

Either way, the theory gives practical criteria for choosing agents: high searching efficiency (low $H^*$), host specificity, a generation time no longer than the host's, the ability to persist when hosts are rare, and features (aggregation, stage specificity) that stabilize the interaction. The integration of biological control with other methods is treated in [7.19.53](/7.19.53).

## Summary

- Host–parasitoid models have the form (27.1): hosts escaping with probability $f$ reproduce at rate $\lambda$; each parasitized host yields $c$ parasitoids. Parasitoids are not hyperparasitoids.
- Nicholson–Bailey model (Definition 27.2.1): random search gives Poisson encounters and $f = \mathrm{e}^{-aP_t}$. Equilibrium $P^* = \ln\lambda/a$, $H^* = \lambda\ln\lambda/[(\lambda - 1)ac]$ (Eq. (27.3)).
- Jury conditions (Lemma 27.2.1): a $2 \times 2$ map is stable iff $\lvert\tau\rvert < 1 + \Delta$ and $\Delta < 1$. For Nicholson–Bailey, $\tau = 1 + s$, $\Delta = \lambda s > 1$ with $s = \ln\lambda/(\lambda - 1)$: complex eigenvalues of modulus greater than 1, diverging oscillations for every $\lambda > 1$ (Theorem 27.2.1), caused by overexploitation with a one-generation delay.
- Host density dependence (Beddington model) stabilizes only when the parasitoid depresses the host weakly ($q = H^*/K$ large).
- Aggregation of risk: with gamma-distributed risk the attacks are negative binomial and $f = (1 + aP/k)^{-k}$ (Formula 27.3.1); the equilibrium is stable iff $k < 1$ (Theorem 27.3.1), for any $\lambda$. Generalization: $\mathrm{CV}^2 > 1$ (Proposition 27.3.1); heterogeneity independent of host density contributes as much as aggregation to dense patches. Mechanism: pseudo-interference, a density-dependent partial refuge.
- Interference (Hassell–Varley, $a = QP^{-m}$) stabilizes if $m$ is large enough; a proportional refuge only if $\beta$ is close to $1/\lambda$; a constant-number refuge more strongly.
- In space (coupled map lattices), locally unstable dynamics persist regionally as spirals, spatial chaos or lattice patterns, on grids that are large enough.
- Biological control: *Rodolia* and *Cryptochaetum* against cottony cushion scale, *Anagyrus* against cassava mealybug, *Bessa* against *Levuana* (with non-target loss). Low and stable control may come from stage structure (red scale and *Aphytis*) or from nonequilibrium regional dynamics.

## Questions

1. A host with $\lambda = 4$ is attacked by a parasitoid with $a = 0.02$ and $c = 1$ that searches at random. Find the equilibrium, the eigenvalues of the linearization, and the approximate period of the oscillations. What changes if a parasitoid with $k = 0.5$ and the same $a$ and $c$ is used instead?

   **Answer** $P^* = \ln 4/0.02 \approx 69.3$, $H^* = 4\ln 4/(3 \times 0.02) \approx 92.4$. With $s = \ln 4/3 \approx 0.462$: $\tau = 1.462$, $\Delta = 4s \approx 1.848$. The eigenvalues are $\frac12\tau \pm \mathrm{i}\sqrt{\Delta - \tau^2/4} = 0.731 \pm 1.153\,\mathrm{i}$, of modulus $\sqrt{1.848} \approx 1.36$: deviations grow by 36 % per generation. $\cos\theta = 0.731/1.36 \approx 0.538$, $\theta \approx 1.003$, period $2\pi/\theta \approx 6.3$ generations. With $k = 0.5$: $P^* = 0.5(4^2 - 1)/0.02 = 375$ and $H^* = 4 \times 375/3 = 500$, much higher (aggregated attacks are less efficient), and the equilibrium is stable by Theorem 27.3.1; indeed $u = 4^{-2} = 1/16$ and $\Delta = 0.5 \times 4 \times (15/16)/3 = 0.625 < 1$.
2. Show that heterogeneity of risk always increases the escape fraction, using Jensen's inequality, and explain why this alone does not guarantee stability.

   **Answer** For any random risk $\varepsilon \ge 0$ with $\mathbb{E}\varepsilon = 1$, convexity of $u \mapsto \mathrm{e}^{-aPu}$ gives $\mathbb{E}\mathrm{e}^{-aP\varepsilon} \ge \mathrm{e}^{-aP\mathbb{E}\varepsilon} = \mathrm{e}^{-aP}$, with equality only if $\varepsilon$ is constant. More hosts escape at every parasitoid density, but stability depends on how the escape fraction changes with $P$ near equilibrium, not on its level: it requires that the parasitoids' per capita success decline steeply enough with their density, which for gamma-distributed risk means $\mathrm{CV}^2 = 1/k > 1$. Weak heterogeneity ($k > 1$) raises escapes but leaves the equilibrium unstable.
3. In May's model, what happens to the equilibrium host density as $k$ decreases, at fixed $\lambda$, $a$, $c$? Comment on the implication for biological control.

   **Answer** $H^* = \lambda P^*/[(\lambda - 1)c]$ with $P^* = k(\lambda^{1/k} - 1)/a$. The function $k(\lambda^{1/k} - 1)$ decreases with $k$ (it tends to $\ln\lambda$ as $k \to \infty$ and grows without bound as $k \to 0$), so stronger clumping raises the equilibrium host density. The mechanism that stabilizes the interaction also weakens control: an agent whose attacks are strongly aggregated leaves many hosts untouched. Good agents combine a high searching efficiency $a$ with just enough heterogeneity for stability.
4. Explain in words why the Nicholson–Bailey model oscillates with increasing amplitude, while the continuous-time Lotka–Volterra model has neutral cycles.

   **Answer** Both models lack any self-limitation of either species, so their equilibria are at best neutrally stable. In continuous time, the response of predators to prey is instantaneous, and the system just balances on the edge (closed orbits). In the discrete host–parasitoid model, the parasitoids produced by this generation's hosts search only in the next generation: the response is delayed by one generation, so parasitoids always respond to the host density of the previous generation and overshoot. A delayed negative feedback without damping amplifies oscillations ([7.19.13](/7.19.13)); hence $\Delta > 1$.
5. (Open problem) You are asked to evaluate whether an introduced parasitoid could control a new invasive leaf-miner. List the data you would collect and how you would use the models of this chapter.

   **Answer** In the native range and in quarantine: host specificity tests on related non-target species (to avoid the *Levuana* problem); the parasitoid's area of discovery $a$ and functional response; its fecundity and sex ratio (giving $c$); its generation time relative to the host's; the distribution of parasitism among leaves, plants and sites, from which $k$ or $\mathrm{CV}^2$ is estimated (separating host-density-dependent and independent components); the host's rate of increase $\lambda$ and density dependence. With these estimates, the models predict the equilibrium depression $q = H^*/K$ and whether it is stable (Theorem 27.3.1, Proposition 27.3.1, Figure 3); stage-structured and spatial models refine the prediction. After release, monitoring of host and parasitoid densities on replicated plots, with exclusion cages as controls, tests whether the predicted depression is achieved.
