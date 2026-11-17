---
title: "Reaction–Diffusion Models: Spread, Invasion and Critical Patch Size"
description: "Continuous-space population models: diffusion as the limit of random movement and the estimation of diffusion coefficients; Skellam's analysis of the muskrat; the Fisher–KPP equation, traveling waves and the minimal wave speed with a complete phase-plane proof; spreading speeds, Allee effects and pushed fronts, invasions and long-distance dispersal in integrodifference models; the critical patch size of the KISS model; single species in heterogeneous habitats; advection, the drift paradox and climate-driven moving habitats; finite-difference methods and their stability."
---

The metapopulation models of [7.19.16](/7.19.16) treat space as a set of discrete patches. Many populations, however, live in habitat that is more or less continuous, and their individuals move short distances many times in a lifetime: insects in a field, plankton in a lake, trees spreading by seed across a continent. For them the natural model is a partial differential equation that combines local growth, the "reaction", with random movement, "diffusion". This chapter develops the reaction–diffusion theory of single populations. It starts from the random walk and the estimation of diffusion coefficients (Section 17.1), derives the linear rate of spread found by Skellam for the muskrat (Section 17.2), analyzes the Fisher–KPP equation and its traveling waves, the effects of Allee effects and of long-distance dispersal on the speed of invasions (Section 17.3), and then asks how large a habitat must be for a population to persist (Section 17.4), how spatial heterogeneity changes abundance (Section 17.5) and how populations persist against a current or a moving climate (Section 17.6). Section 17.7 describes the finite-difference methods used for all the simulations. The heat equation and the probabilistic meaning of diffusion are treated in [2.5.7](/2.5.7), the Fisher–KPP equation was introduced as a model of biochemical waves in [7.5.23](/7.5.23), and the spread of favorable genes by the same equation in [7.10.10](/7.10.10). Interactions in space, spatial competition and Turing patterns follow in [7.19.30](/7.19.30), and biological invasions as a threat to biodiversity in [7.19.51](/7.19.51).

## 17.1. From Random Movement to Diffusion

### 17.1.1. The Diffusion Equation

Let $u(x, t)$ be the density of a population (individuals per unit length or area) and let individuals move at random without a preferred direction. Two arguments lead to the same equation. The first is the conservation of individuals: if $J(x, t)$ is the net flux (individuals crossing a point per unit time, positive to the right), the number in a small interval $[x, x + \Delta x]$ changes only by what crosses its ends, so that $u_t = -J_x$. **Fick's law** ([2.5.1](/2.5.1)) states that random movement produces a flux down the density gradient, $J = -Du_x$, because more individuals happen to move from crowded to sparse places than the reverse. Together they give the diffusion equation $u_t = Du_{xx}$, in two dimensions $u_t = D\Delta u$ with $\Delta = \partial_x^2 + \partial_y^2$. The constant $D$ is the **diffusion coefficient**, with units of area per time ($\mathrm{km^2\,yr^{-1}}$ for mammals, $\mathrm{m^2\,d^{-1}}$ for insects).

The second argument starts from individuals. In a **random walk** each individual steps a distance $h$ to the left or to the right with equal probability every $\tau$ units of time. As shown in [2.5.7](/2.5.7) (Section 7.5.1), the probability density of its position satisfies $p_t = Dp_{xx}$ in the limit $h, \tau \to 0$ with $D = h^2/(2\tau)$ fixed, and by the central limit theorem the position after time $t$ is normal with variance $2Dt$. The density of a large population released at one point therefore spreads as the Gaussian heat kernel (Figure 1A). Diffusion is a description of the population, not a claim that individuals move aimlessly: foraging animals turn, pause and respond to their surroundings, but over many moves their displacements add up like a random walk, and only the variance of the displacement per unit time matters on large scales.

When local births and deaths are added, at a rate $f(u)$ per unit area, the result is a **reaction-diffusion equation** ([2.5.7](/2.5.7), Section 7.5.2).

**Definition 17.1.1 (Reaction–Diffusion Model of a Population)** A *reaction–diffusion model* of a single population is

$$
\frac{\partial u}{\partial t} = D\Delta u + f(u),
\tag{17.1}
$$
where $u(\boldsymbol{x}, t)$ is the population density at position $\boldsymbol{x}$ in a region $\Omega$ of the line or the plane, $D$ is the diffusion coefficient and $f(u)$ the net rate of local population growth; typical choices are $f(u) = ru$ (exponential growth), $f(u) = ru(1 - u/K)$ (logistic growth) and growth with an **Allee effect** ([Definition 10.3.2](/7.19.10#def-10.3.2) of 7.19.10). On a bounded region the equation is completed by boundary conditions: $u = 0$ on the boundary (a **Dirichlet boundary condition**: individuals that reach the edge die or leave for good), $\partial u/\partial\boldsymbol{n} = 0$ (a zero-flux **Neumann boundary condition**: the edge reflects individuals), or a mixture of the two.

The model assumes that all individuals move in the same way, independently of density and of position, and that births and deaths at each point depend only on the local density. Section 17.5 relaxes the second assumption, Section 17.6 adds directed movement, and the extension to several interacting species is the subject of [7.19.30](/7.19.30).

### 17.1.2. Estimating Diffusion Coefficients

The diffusion coefficient is measured through the **mean squared displacement** (MSD). If individuals are released at the origin of the plane and move by a two-dimensional random walk, their displacement $\boldsymbol{X}_t$ after time $t$ is normal with variance $2Dt$ in each coordinate, so

$$
\mathbb{E}\lvert\boldsymbol{X}_t\rvert^2 = 4Dt, \qquad \hat D = \frac{\overline{r^2}}{4t},
\tag{17.2}
$$
where $\overline{r^2}$ is the mean squared distance of recaptured or relocated individuals from the release point after time $t$ (in one dimension $\mathbb{E}X_t^2 = 2Dt$). The linearity of the MSD in $t$ is itself a test of the diffusion approximation (Figure 1C). In mark–release–recapture experiments with herbivorous insects, Kareiva (1983) found that simple diffusion described the spread of released individuals of several species reasonably well, with $D$ ranging over orders of magnitude between species and between habitats of different patchiness. Two systematic departures are common. Over short times, animals move in nearly straight lines, so that the MSD grows like $t^2$ before it becomes linear; this is the regime of the *correlated random walk*, whose diffusion coefficient depends on the speed and on the mean time between turns. And the distribution of displacements often has more long moves than a Gaussian, a fat-tailed **dispersal kernel** ([Definition 16.1.1](/7.19.16#def-16.1.1) of 7.19.16), which matters greatly for spread (Section 17.3.5).

For organisms with discrete generations, such as annual plants, dispersal is described per generation by the kernel of distances between parent and offspring. If its variance in one coordinate is $\sigma^2$ and the generation time is $T$, the equivalent diffusion coefficient is $D = \sigma^2/(2T)$.

![From random walks to diffusion. A: 4000 walkers on a line released at x = 0, with steps of ±h every τ (D = h²/(2τ) = 1); histograms of their positions at three times and the Gaussian heat kernel with variance 2Dt (lines). B: tracks of five walkers in the plane, all starting at the square. C: mean squared displacement of 2000 two-dimensional walkers against time (points) and the line 4Dt: the slope divided by 4 estimates the diffusion coefficient, Eq. (17.2)](./plots/random-walk-diffusion.py)

### 17.1.3. Scaling

For the logistic model $u_t = Du_{xx} + ru(1 - u/K)$, the substitutions

$$
\tilde u = \frac{u}{K}, \qquad \tilde t = rt, \qquad \tilde x = x\sqrt{\frac{r}{D}}
$$
give the parameter-free form $\tilde u_{\tilde t} = \tilde u_{\tilde x\tilde x} + \tilde u(1 - \tilde u)$. The model therefore has a natural time scale $1/r$ and a natural length scale $\sqrt{D/r}$, the distance an individual diffuses during one characteristic time of population growth. Every result about lengths in this chapter (the width of a front, the critical size of a habitat, the speed of spread) is a number times $\sqrt{D/r}$ or $\sqrt{rD}$, and its biological content lies in that number. In the following sections we use the scaled form whenever this simplifies the analysis, and state the results in dimensional form.

## 17.2. Skellam's Analysis of Spread

In 1905 five muskrats (*Ondatra zibethicus*), a North American rodent valued for its fur, were released on an estate at Dobříš near Prague. Their descendants spread over much of central Europe within a few decades, and later introductions, for fur farming, extended the range across Europe and into Siberia. Skellam (1951) analyzed maps of the expanding range up to 1927 and noticed that the square root of the occupied area increased linearly with time: the radius of the range grew at a constant speed. He explained this with the simplest reaction–diffusion model, exponential growth with diffusion.

**Proposition 17.2.1 (Skellam's Linear Spread)** Let $N_0$ individuals be released at the origin of the plane at $t = 0$ and let the density follow $u_t = D\Delta u + ru$. Then

$$
u(\boldsymbol{x}, t) = \frac{N_0}{4\pi Dt}\exp\left(rt - \frac{\lvert\boldsymbol{x}\rvert^2}{4Dt}\right),
\tag{17.3}
$$
and the radius $R(t)$ of the circle on which the density equals a detection threshold $u_{\mathrm{c}}$ satisfies

$$
R(t) = 2\sqrt{rD}\,t\left(1 - \frac{1}{rt}\ln\frac{4\pi Dtu_{\mathrm{c}}}{N_0}\right)^{1/2},
\qquad \lim_{t\to\infty}\frac{R(t)}{t} = 2\sqrt{rD}.
$$
The occupied area $\pi R^2$ therefore grows asymptotically as $4\pi rDt^2$, and its square root linearly in $t$.

**Proof** Substituting $u = \mathrm{e}^{rt}w$ gives $w_t = D\Delta w$, whose solution for a point release of $N_0$ individuals is the two-dimensional heat kernel $N_0(4\pi Dt)^{-1}\exp(-\lvert\boldsymbol{x}\rvert^2/(4Dt))$ ([Definition 7.1.1](/2.5.7#def-7.1.1) of 2.5.7); this gives Eq. (17.3). Setting $u = u_{\mathrm{c}}$ and solving for $\lvert\boldsymbol{x}\rvert^2$ gives $R^2 = 4Dt\bigl[rt - \ln(4\pi Dtu_{\mathrm{c}}/N_0)\bigr]$, which is the stated formula. Since $\ln t/t \to 0$, the bracket tends to 1. $\square$

The logarithmic correction shows why the asymptotic speed is reached only slowly: early in an invasion the range grows more slowly than $2\sqrt{rD}$, because the initial population must first build up. In one dimension the same calculation gives the same limit. The model makes a quantitative prediction from two parameters that can be measured independently of the range maps: $r$ from life tables or from the growth of a population at low density ([7.19.10](/7.19.10)), and $D$ from the movement of marked individuals, Eq. (17.2). For the muskrat, the observed radial rates of spread in different directions ranged from about 1 to 25 km per year, depending on the landscape, and predictions from independent estimates of $r$ and $D$ were of the same order (Andow et al. 1990). The same comparison for the small cabbage white butterfly (*Pieris rapae*) in North America gave good agreement, whereas for the cereal leaf beetle (*Oulema melanopus*), which is carried long distances by wind, the agreement was poorer. As a rule of thumb, an observed speed of spread $c$ and a growth rate $r$ imply a diffusion coefficient $D = c^2/(4r)$: a mammal with $r = 0.2\,\mathrm{yr^{-1}}$ spreading at $5\,\mathrm{km\,yr^{-1}}$ requires $D \approx 31\,\mathrm{km^2\,yr^{-1}}$, a root mean squared displacement of $\sqrt{4D} \approx 11\,\mathrm{km}$ per year.

Exponential growth cannot continue behind the front, but this does not change the speed, because the speed is determined at the leading edge, where the density is low. The nonlinear theory in the next section confirms this.

## 17.3. The Fisher–KPP Equation and the Speed of Invasions

### 17.3.1. Traveling Waves

With logistic growth, Eq. (17.1) becomes the **Fisher–KPP equation** ([Definition 23.6.2](/7.5.23#def-23.6.2) of 7.5.23),

$$
\frac{\partial u}{\partial t} = D\frac{\partial^2 u}{\partial x^2} + ru\left(1 - \frac{u}{K}\right),
\tag{17.4}
$$
proposed by Fisher (1937) for the spread of an advantageous gene and analyzed in the same year by Kolmogorov, Petrovsky and Piskunov. In ecology it is the standard model of a population invading empty habitat. Numerical solutions from a local introduction (Figure 2A) show two fronts that move outward at constant speed without changing shape, leaving the population at carrying capacity behind them. Such a solution is a **traveling wave solution**, $u(x, t) = U(z)$ with $z = x - ct$, which connects $U = K$ behind the front ($z \to -\infty$) to $U = 0$ ahead of it ($z \to +\infty$). In scaled variables (Section 17.1.3) the profile satisfies the ordinary differential equation

$$
U'' + cU' + U(1 - U) = 0, \qquad U(-\infty) = 1, \quad U(+\infty) = 0,
\tag{17.5}
$$
where $c$ is the scaled speed (the dimensional speed is $c\sqrt{rD}$).

**Theorem 17.3.1 (Traveling Waves of the Fisher–KPP Equation)** Eq. (17.5) has a solution with $0 < U < 1$ if and only if $c \ge 2$. For each $c \ge 2$ the solution is unique up to translation and strictly decreasing. In dimensional form, Eq. (17.4) has nonnegative traveling fronts exactly for the speeds $c \ge c^* = 2\sqrt{rD}$.

**Proof** Write Eq. (17.5) as the first-order system $U' = V$, $V' = -cV - U(1 - U)$ in the **phase plane** $(U, V)$. A front is an orbit that leaves the equilibrium $(1, 0)$ as $z$ increases from $-\infty$ and enters $(0, 0)$ as $z \to +\infty$. The **Jacobian matrix** at $(U, 0)$ is $\begin{bmatrix}0 & 1\\ -(1 - 2U) & -c\end{bmatrix}$.

*Necessity.* At $(0, 0)$ the eigenvalues are $\mu_\pm = \bigl(-c \pm \sqrt{c^2 - 4}\bigr)/2$. If $0 \le c < 2$ they are complex with negative real part, so the origin is a stable focus and every orbit entering it winds around it, making $U$ negative for arbitrarily large $z$; such a profile is not a population density. Hence $c \ge 2$ (for $c < 0$ the origin is unstable and no orbit enters it from $U > 0$).

*Sufficiency.* At $(1, 0)$ the eigenvalues are $\bigl(-c \pm \sqrt{c^2 + 4}\bigr)/2$, of opposite signs: $(1, 0)$ is a saddle with a one-dimensional unstable manifold, whose branch entering $U < 1$ leaves along the eigenvector $(1, \lambda_+)$, $\lambda_+ = \bigl(-c + \sqrt{c^2 + 4}\bigr)/2 > 0$, that is, into the quadrant $U < 1$, $V < 0$. Let $c \ge 2$, put $\mu = c/2$, and consider the triangle

$$
T = \{(U, V)\colon 0 \le U \le 1,\ -\mu U \le V \le 0\}.
$$
We show that no orbit can leave $T$ except through the origin. On the side $V = 0$, $0 < U < 1$: $V' = -U(1 - U) < 0$, so the flow enters $T$. On the side $U = 1$, $V < 0$: $U' = V < 0$, so the flow enters $T$. On the side $V = -\mu U$, $0 < U \le 1$, the inward normal is $(\mu, 1)$ and

$$
(\mu, 1)\cdot(U', V') = \mu V - cV - U(1 - U) = U\bigl[\mu(c - \mu) - (1 - U)\bigr] \ge U\Bigl[\frac{c^2}{4} - 1\Bigr] \ge 0,
$$
so the flow does not leave $T$ there either. Since $\lambda_+ < \mu$ when $c \ge 2$ (indeed $\lambda_+ < 1/c \le c/2$), the unstable branch of the saddle starts inside $T$ and therefore stays in $T$ for all $z$. In the interior of $T$, $U' = V < 0$, so $U$ decreases monotonically and the orbit converges to an equilibrium in $T$; the only equilibria are $(1, 0)$, which the orbit has left, and $(0, 0)$. Thus the orbit is a heteroclinic connection from $(1, 0)$ to $(0, 0)$: a strictly decreasing front with $0 < U < 1$. Uniqueness up to translation holds because the unstable manifold of the saddle has only one branch entering $U < 1$, and any front must lie on it. $\square$

There is therefore not one wave speed but a half-line of them (Figure 2D). The waves with $c > 2$ decay ahead of the front like $\mathrm{e}^{-\mu_+z}$ with $\mu_+ = \bigl(c - \sqrt{c^2 - 4}\bigr)/2 < 1$, more slowly than the minimal wave. They are realized only from initial densities with such slowly decaying tails; a population introduced in a bounded region selects the minimal speed.

### 17.3.2. The Asymptotic Speed of Spread

**Definition 17.3.1 (Invasion Speed)** The **invasion speed** (asymptotic spreading speed) of a population model in homogeneous space is the number $c^*$ such that, for every initial distribution that is nonnegative, nonzero and confined to a bounded region, and every $\varepsilon > 0$, the density tends to zero uniformly in $\lvert\boldsymbol{x}\rvert \ge (c^* + \varepsilon)t$ and to the positive equilibrium uniformly in $\lvert\boldsymbol{x}\rvert \le (c^* - \varepsilon)t$ as $t \to \infty$: an observer moving outward faster than $c^*$ eventually sees no population, and one moving more slowly sees the population at its equilibrium.

**Theorem 17.3.2 (Spreading Speed of the Fisher–KPP Equation)** For Eq. (17.4) in one or more dimensions, the invasion speed exists and equals the minimal wave speed, $c^* = 2\sqrt{rD}$. More generally, it equals $2\sqrt{f'(0)D}$ for every growth function with $f(0) = f(K) = 0$, $f > 0$ on $(0, K)$ and $f(u) \le f'(0)u$ (Kolmogorov, Petrovsky and Piskunov 1937; Aronson and Weinberger 1978).

**Proof** (Upper bound.) Since $ru(1 - u/K) \le ru$, the solution of Eq. (17.4) is a subsolution of the linear equation $\bar u_t = D\Delta\bar u + r\bar u$ with the same initial data, so by the comparison principle (the **maximum principle** of [2.5.7](/2.5.7)) $u \le \bar u$. For initial data bounded by $A$ and supported in the ball of radius $a$, $\bar u(\boldsymbol{x}, t) \le A'\,t^{-n/2}\exp\bigl(rt - (\lvert\boldsymbol{x}\rvert - a)^2/(4Dt)\bigr)$ in $n$ dimensions, as in Proposition 17.2.1. On $\lvert\boldsymbol{x}\rvert \ge (c^* + \varepsilon)t$ the exponent is at most $rt - (c^* + \varepsilon)^2t/(4D) + O(1) = -\bigl(2\varepsilon c^* + \varepsilon^2\bigr)t/(4D) + O(1) \to -\infty$, because $(c^*)^2/(4D) = r$. Hence $u \to 0$ uniformly there. The lower bound requires constructing subsolutions that move at speeds close to $c^*$ and is omitted. $\square$

The speed is determined by the linearization at $u = 0$: it depends only on the growth rate at low density and on the diffusion coefficient, not on the carrying capacity or on how density dependence acts at high density. Fronts of this kind are called *pulled*: they are pulled along by the growth and spread of the few individuals at the leading edge, which has practical consequences. The fate of an invasion is decided far ahead of the visible front, where densities are too low to detect; control efforts that reduce the population behind the front barely slow it, whereas killing the sparse pioneers, or reducing their growth rate, does. The approach to the asymptotic speed is slow: the position of the front lags behind $c^*t$ by $\frac{3}{2}\sqrt{D/r}\ln t$ (Bramson 1983; [7.5.23](/7.5.23)), so that measured speeds over the first few decades of an invasion are slightly lower than $c^*$ (Figure 2B, C).

![Invasion fronts of the Fisher–KPP equation, Eq. (17.4). A: an introduction (u = 0.5 on |x| < 2, D = r = 1) spreads as two fronts; profiles every 10 time units. B: position of the front (where u = 0.1) against time for three combinations of r and D (points), with lines of slope 2√(rD) (dashed). C: asymptotic speeds measured in simulations for nine combinations of r and D against 2√(rD); the dashed line is the identity. D: the phase plane of the traveling-wave equation (17.5): for c = 2.5 the orbit leaving the saddle (1, 0) stays in the triangle of the proof of Theorem 17.3.1 (shaded) and enters the node (0, 0); for c = 1 the origin is a focus and the orbit makes U negative](./plots/fisher-kpp-fronts.py)

### 17.3.3. Allee Effects and Pushed Fronts

If individuals at low density suffer an **Allee effect** ([7.19.10](/7.19.10)), the growth rate at the leading edge is reduced, or even negative, and the linear argument fails. The standard model of a strong Allee effect is, in scaled variables,

$$
u_t = u_{xx} + u(1 - u)(u - a), \qquad 0 < a < 1,
\tag{17.6}
$$
where $a$ is the Allee threshold as a fraction of the carrying capacity (dimensionally, $f(u) = ru(1 - u/K)(u/K - a)$, with length unit $\sqrt{D/r}$ and time unit $1/r$).

**Proposition 17.3.3 (Front with a Strong Allee Effect)** Eq. (17.6) has the traveling front

$$
U(z) = \frac{1}{1 + \mathrm{e}^{z/\sqrt2}}, \qquad c = \frac{1 - 2a}{\sqrt2},
$$
which in dimensional form moves at the speed $c = (1 - 2a)\sqrt{rD/2}$. The population advances if $a < 1/2$, retreats if $a > 1/2$, and the front is stationary at $a = 1/2$. The front is unique up to translation, and it is the only traveling wave connecting 1 and 0.

**Proof** Let $U = 1/(1 + \mathrm{e}^{\kappa z})$. Then $U' = -\kappa U(1 - U)$ and $U'' = -\kappa U'(1 - 2U) = \kappa^2U(1 - U)(1 - 2U)$. Substituting in $U'' + cU' + U(1 - U)(U - a) = 0$ and dividing by $U(1 - U)$ gives $\kappa^2(1 - 2U) - c\kappa + U - a = 0$ for all $U$, so $1 - 2\kappa^2 = 0$ and $\kappa^2 - c\kappa - a = 0$: $\kappa = 1/\sqrt2$ and $c = (1/2 - a)\sqrt2$. For the uniqueness of the speed, multiply the wave equation by $U'$ and integrate over $\mathbb{R}$: since $U'(\pm\infty) = 0$, $c\int U'^2\,\mathrm{d}z = -\int f(U)U'\,\mathrm{d}z = \int_0^1 f(u)\,\mathrm{d}u = \frac{1 - 2a}{12}$, so the sign of $c$ is the sign of $\int_0^1 f$, and phase-plane arguments (Fife and McLeod 1977) show that the bistable front is unique. $\square$

Unlike the Fisher front, this front is *pushed*: its speed depends on growth in the whole front, including the high densities behind it, because individuals at the leading edge cannot grow on their own. Allee effects therefore slow invasions, can stop them ($a \ge 1/2$), and make the success of an invasion depend on the initial size of the introduced population: introductions below a critical size and extent die out (a spatial version of the establishment threshold of [7.19.15](/7.19.15)). In heterogeneous or patchy landscapes, Allee effects can even pin a front in place over a range of conditions in which a Fisher front would advance (Keitt, Lewis and Holt 2001). The gypsy moth (*Lymantria dispar*), introduced to Massachusetts in 1869, has spread across eastern North America at a rate of the order of 20 km per year, far below the prediction from its growth rate and dispersal, and its spread is pulsed; both features have been attributed to a mate-finding Allee effect in sparse populations at the front (Johnson et al. 2006). The barrier zone management of the gypsy moth (the "Slow the Spread" program) exploits the same theory: by suppressing the isolated low-density colonies ahead of the front with mating disruption, it reinforces the Allee effect and has substantially reduced the rate of spread.

### 17.3.4. Invasions in Nature

Spread at a constant rate, as predicted by Theorem 17.3.2, describes many invasions over parts of their history, but two departures are common. First, many invasions begin with a lag phase, in which the range expands slowly for years or decades before rapid spread begins. Proposition 17.2.1 contributes to this, because the asymptotic speed is reached slowly, and Allee effects, adaptation to the new environment and the time needed to found satellite populations contribute further. Second, the range often expands faster and faster. The western corn rootworm (*Diabrotica virgifera virgifera*), the most important pest of maize in North America, broke out of its stronghold in Nebraska in the 1940s and spread east across the Corn Belt; in Europe it was first found near Belgrade airport in 1992, spread through southeastern Europe at tens of kilometers per year, and appeared in widely separated places in western Europe through several further transatlantic introductions. Zebra mussels (*Dreissena polymorpha*) spread rapidly through the navigable waterways of North America after 1986 but much more slowly to inland lakes, carried on recreational boats (Bossenbroek et al. 2001). Such *stratified dispersal*, local diffusion combined with occasional long-distance jumps that found new foci, produces a range that grows by coalescence of expanding colonies and an accelerating area curve (Shigesada and Kawasaki 1997).

Acceleration can also be evolutionary. The cane toad (*Rhinella marina*), introduced to Queensland in 1935, spread at about 10 km per year in its first decades but more than 50 km per year by the early 2000s; toads at the invasion front have longer legs, move farther and more often than those in older populations (Phillips et al. 2006). This is expected under *spatial sorting*: the fastest dispersers accumulate at the front, where they mate with each other and where low density favors high reproduction, so that dispersal ability evolves upward during the invasion and the front accelerates. In the Fisher–KPP model, this amounts to $D$ (and possibly $r$) increasing over time at the leading edge.

### 17.3.5. Long-Distance Dispersal and Integrodifference Equations

For organisms with discrete generations and a separate dispersal stage, such as annual plants and many insects, the natural model alternates growth and dispersal.

**Definition 17.3.2 (Integrodifference Equation)** An *integrodifference equation* for a population in one-dimensional space is

$$
N_{t+1}(x) = \int_{-\infty}^{\infty} k(x - y)\,F\bigl(N_t(y)\bigr)\,\mathrm{d}y,
\tag{17.7}
$$
where $F(N)$ is the density of propagules produced at a point with density $N$ (for example the **Beverton–Holt model** $F(N) = R_0N/\bigl(1 + (R_0 - 1)N/K\bigr)$ of [7.19.12](/7.19.12)) and $k$ is the dispersal kernel: the density of the displacement of a propagule between its place of production and its place of settlement.

If $F(N) \le R_0N$ with $R_0 = F'(0) > 1$ and the kernel is *exponentially bounded*, meaning that its moment generating function $M(s) = \int k(x)\mathrm{e}^{sx}\,\mathrm{d}x$ is finite for some $s > 0$, the population spreads at the asymptotic speed (Weinberger 1982; Kot, Lewis and van den Driessche 1996)

$$
c^* = \min_{s > 0}\frac{1}{s}\ln\bigl(R_0M(s)\bigr).
\tag{17.8}
$$
The formula is obtained as in Section 17.2 from the linearization at low density: a profile $N_t(x) = \mathrm{e}^{-s(x - ct)}$ of the linear equation $N_{t+1} = R_0\,k * N_t$ moves at speed $c(s) = \ln(R_0M(s))/s$, and, as for the Fisher equation, the minimal speed is selected by initial data of bounded extent. For a Gaussian kernel of variance $\sigma^2$, $M(s) = \mathrm{e}^{\sigma^2s^2/2}$ and the minimum, at $s = \sqrt{2\ln R_0}/\sigma$, is $c^* = \sigma\sqrt{2\ln R_0}$; this is exactly the speed $2\sqrt{rD}$ of the Fisher equation with $r = \ln R_0$ and $D = \sigma^2/2$ per generation. For a Laplace (exponential) kernel with the same variance, the speed is higher (Figure 3B), because the tail of the kernel carries more propagules far ahead of the front.

If the kernel is fat-tailed, decaying more slowly than any exponential (for example as a power of the distance), $M(s)$ is infinite for every $s > 0$ and there is no finite asymptotic speed: the front accelerates indefinitely (Kot et al. 1996). In the example of Figure 3, with a kernel decaying as $\lvert x\rvert^{-4}$, the front position grows roughly exponentially in time. Since the tail of a dispersal kernel is the part hardest to measure, this sensitivity is a serious practical limitation: two kernels that fit the same seed-trap data near the source can predict spread rates differing by orders of magnitude. It is also the theoretical resolution of *Reid's paradox* ([7.19.16](/7.19.16)): after the last glaciation, oaks and other trees with heavy seeds spread northward across Britain and Europe at hundreds of meters per year, far faster than diffusion with their measured seed dispersal distances would allow, and rare long-distance transport by birds (jays caching acorns) and other agents can account for the difference (Clark 1998). Neubert and Caswell (2000) combined Eq. (17.8) with stage-structured matrix models ([7.19.14](/7.19.14)) and found that the spread rates of two perennial plants depended most strongly on the maximum dispersal distances.

![Spread with long-distance dispersal in the integrodifference model (17.7), with Beverton–Holt growth (R₀ = 2) and three dispersal kernels of variance 1. A: the kernels on a log scale: Gaussian, Laplace and a fat-tailed kernel decaying as |x|⁻⁴. B: position of the front (where N = 0.05) over 40 generations, on a log scale; dashed lines have the slopes c* of Eq. (17.8), 1.18 for the Gaussian and 1.34 for the Laplace kernel. With the fat-tailed kernel the front accelerates without limit. C: density profiles after 30 generations](./plots/integrodifference-spread.py)

## 17.4. Critical Patch Size

### 17.4.1. The KISS Model

A population that can grow in a patch of habitat but dies, or is lost, in the surrounding environment faces a balance between local reproduction and the loss of individuals that wander across the edge. Kierstead and Slobodkin (1953), considering how phytoplankton blooms can persist in a patch of water favorable for growth, and Skellam (1951) solved the simplest version of the problem, now known as the KISS model (Kierstead, Slobodkin and Skellam).

**Theorem 17.4.1 (KISS Model)** Let a population grow exponentially at rate $r$ in the patch $0 < x < L$, diffuse with coefficient $D$, and die on reaching its edges:

$$
u_t = Du_{xx} + ru, \qquad u(0, t) = u(L, t) = 0.
\tag{17.9}
$$
Then for every initial density $u(x, 0) = \varphi(x) \ge 0$, $\varphi \not\equiv 0$, the population grows without bound if $L > L_{\mathrm{c}}$ and goes extinct if $L < L_{\mathrm{c}}$, where

$$
L_{\mathrm{c}} = \pi\sqrt{\frac{D}{r}} .
\tag{17.10}
$$

**Proof** By **separation of variables** ([2.5.4](/2.5.4)), the solution is the **Fourier series** $u(x, t) = \sum_{n\ge1}b_n\mathrm{e}^{\sigma_nt}\sin(n\pi x/L)$, where $b_n = \frac{2}{L}\int_0^L\varphi(x)\sin(n\pi x/L)\,\mathrm{d}x$ and

$$
\sigma_n = r - D\frac{n^2\pi^2}{L^2}
$$
are the eigenvalues of the **Sturm–Liouville problem** $D\phi'' + r\phi = \sigma\phi$, $\phi(0) = \phi(L) = 0$. As $t \to \infty$ the first term dominates, because $\sigma_1 > \sigma_n$ for $n \ge 2$, and $b_1 > 0$, because $\varphi \ge 0$, $\varphi \not\equiv 0$ and $\sin(\pi x/L) > 0$ on $(0, L)$. So $u \approx b_1\mathrm{e}^{\sigma_1t}\sin(\pi x/L)$, which grows if $\sigma_1 > 0$ and decays if $\sigma_1 < 0$; $\sigma_1 > 0$ is equivalent to $L > \pi\sqrt{D/r}$. $\square$

**Definition 17.4.1 (Critical Patch Size)** The **critical patch size** of a population is the smallest size of a patch of habitat in which the population can persist, given its growth rate inside the patch, its movement and the conditions in the surrounding environment (the matrix). For the KISS model in one dimension it is $L_{\mathrm{c}} = \pi\sqrt{D/r}$.

The result has a simple interpretation. The rate of loss of individuals across the boundary is, for the slowest-decaying distribution $\sin(\pi x/L)$, $D\pi^2/L^2$ per individual: the inverse of the time needed to diffuse across a distance of order $L/\pi$. A population persists if its growth rate exceeds this loss rate. The critical size grows with the square root of $D/r$: fast-moving species with slow growth need large patches, sedentary species with fast growth can persist in small ones. Doubling the mobility of a species increases its critical patch length by a factor $\sqrt2$.

With density dependence the conclusion is the same, and the population settles to a positive steady state when the patch is large enough.

**Theorem 17.4.2 (KISS Model with Logistic Growth)** For $u_t = Du_{xx} + ru(1 - u/K)$ on $(0, L)$ with $u = 0$ at both ends and initial data $\varphi \ge 0$, $\varphi \not\equiv 0$: if $L \le L_{\mathrm{c}}$, $u \to 0$; if $L > L_{\mathrm{c}}$, there is a unique positive steady state $u^*(x)$, and $u(x, t) \to u^*(x)$.

**Proof** (Sketch.) If $L < L_{\mathrm{c}}$, $u$ is a subsolution of Eq. (17.9) and decays by Theorem 17.4.1; at $L = L_{\mathrm{c}}$ the decay follows from the negative quadratic term. If $L > L_{\mathrm{c}}$, the function $\varepsilon\sin(\pi x/L)$ is a subsolution of the steady-state equation for small $\varepsilon > 0$, because $D(\varepsilon\phi)'' + r\varepsilon\phi(1 - \varepsilon\phi/K) = \varepsilon\phi\bigl(\sigma_1 - r\varepsilon\phi/K\bigr) \ge 0$ when $r\varepsilon/K \le \sigma_1$, and the constant $K$ is a supersolution. By the method of sub- and supersolutions there is a steady state between them, and the uniqueness of positive steady states follows from the concavity of $u(1 - u/K)/u$ in $u$; convergence follows from comparison of $u$ with the solutions starting from the sub- and supersolution, which are monotone in time (Cantrell and Cosner 2003). $\square$

Figure 4A shows steady states for patches of several lengths: in a small patch, even above the threshold, the density is everywhere well below $K$; in a large patch the population fills the interior at $K$, and the edge zones, where the density falls to zero, have a width of a few $\sqrt{D/r}$.

### 17.4.2. Shape, Two Dimensions and a Partially Hostile Matrix

In two dimensions, the same analysis with the Laplace operator gives the critical sizes from the smallest Dirichlet eigenvalue $\lambda_1(\Omega)$ of $-\Delta$ on the patch $\Omega$: the population persists if and only if $r > D\lambda_1(\Omega)$. For a square of side $L$, $\lambda_1 = 2\pi^2/L^2$ and $L_{\mathrm{c}} = \pi\sqrt{2D/r}$ (area $2\pi^2D/r \approx 19.7\,D/r$); for a circular patch of radius $R$, $\lambda_1 = j_{0,1}^2/R^2$, where $j_{0,1} \approx 2.405$ is the first zero of the Bessel function $J_0$ ([2.5.5](/2.5.5)), and $R_{\mathrm{c}} = 2.405\sqrt{D/r}$ (area $\approx 18.2\,D/r$). Among all patches of a given area the disk has the smallest $\lambda_1$ (the Faber–Krahn inequality), so compact patches are the most favorable; long thin patches, with much edge relative to area, need far more area. This is one theoretical basis of the advice, in reserve design, to prefer compact over elongated reserves ([7.19.34](/7.19.34), [7.19.52](/7.19.52)) and of the importance of edge effects in fragmented landscapes ([7.19.48](/7.19.48)).

The surroundings of a patch are rarely completely lethal. Suppose individuals in the matrix die at rate $\mu$ and move with the same diffusion coefficient. A steady state of the linear problem at the threshold of persistence is then $\phi = \cos(kx)$ inside the patch $\lvert x\rvert < L/2$, with $k = \sqrt{r/D}$, and $\phi = A\exp\bigl(-\kappa(\lvert x\rvert - L/2)\bigr)$ outside, with $\kappa = \sqrt{\mu/D}$. Continuity of $\phi$ and of the flux $\phi'$ at $x = L/2$ requires $k\tan(kL/2) = \kappa$, so

$$
L_{\mathrm{c}} = 2\sqrt{\frac{D}{r}}\arctan\sqrt{\frac{\mu}{r}} .
\tag{17.11}
$$
As the matrix becomes lethal ($\mu \to \infty$), $L_{\mathrm{c}} \to \pi\sqrt{D/r}$; as it becomes benign ($\mu \to 0$), $L_{\mathrm{c}} \to 0$ (Figure 4C). Improving the quality of the matrix, so that individuals crossing it survive longer, therefore reduces the area of habitat needed for persistence, an argument for "wildlife-friendly" land use around reserves. Ludwig, Aronson and Weinberger (1979) used a model of this type to ask how large a forest stand must be to support an outbreak of the spruce budworm (*Choristoneura fumiferana*), whose moths disperse widely.

![Critical patch size. A: steady states of the logistic KISS model in patches of length L = 4, 6, 10 and 20 (in units of √(D/r)) with lethal surroundings; patches shorter than π cannot support a population. B: growth rate r − Dπ²/L² of the slowest-decaying mode (line, left axis) and mean density of the steady state (points, right axis): both become positive at L_c = π√(D/r). C: critical length with a partially hostile matrix in which individuals die at rate μ, Eq. (17.11): it rises from 0 to the lethal-matrix value π√(D/r) as μ/r increases](./plots/critical-patch-size.py)

## 17.5. A Single Species in a Heterogeneous Environment

### 17.5.1. Persistence and the Principal Eigenvalue

Habitats are rarely uniform. Let the local growth rate at low density vary in space, $m(x)$, positive in good habitat and negative in poor habitat, and let the population be confined to a region $\Omega$ with reflecting boundaries:

$$
u_t = d\Delta u + u\bigl(m(x) - u\bigr), \qquad \frac{\partial u}{\partial\boldsymbol{n}} = 0 \ \text{on}\ \partial\Omega .
\tag{17.12}
$$
Here $m(x)$ also equals the local carrying capacity, so $m$ can be thought of as the distribution of resources. Persistence is governed by the principal **eigenvalue** $\lambda_1(d, m)$ of the linearized problem $d\Delta\phi + m\phi = \lambda\phi$ with zero-flux boundary conditions, whose eigenfunction is positive; by the variational characterization,

$$
\lambda_1(d, m) = \max_{\phi \ne 0}\frac{\int_\Omega\bigl(m\phi^2 - \mathrm{d}\lvert\nabla\phi\rvert^2\bigr)\,\mathrm{d}x}{\int_\Omega\phi^2\,\mathrm{d}x} .
$$

**Proposition 17.5.1 (Persistence in a Heterogeneous Habitat)** The population (17.12) persists, converging to a unique positive steady state $\theta_d(x)$, if $\lambda_1(d, m) > 0$, and goes extinct if $\lambda_1(d, m) \le 0$. If $m$ is not constant, $\lambda_1$ decreases strictly with $d$, from $\max m$ as $d \to 0$ to the spatial mean $\bar m = \lvert\Omega\rvert^{-1}\int_\Omega m$ as $d \to \infty$. Consequently: if $\bar m \ge 0$, the population persists for every $d$; if $\bar m < 0 < \max m$, it persists if and only if $d < d^*$ for a critical diffusion rate $d^*$; if $\max m \le 0$, it cannot persist.

**Proof** (Sketch.) Persistence for $\lambda_1 > 0$ and extinction for $\lambda_1 \le 0$ follow as in Theorem 17.4.2, using $\varepsilon\phi_1$ as a subsolution (Cantrell and Cosner 1991, 2003). Taking $\phi = 1$ in the variational formula gives $\lambda_1 \ge \bar m$, with strict inequality when $m$ is not constant, because then $1$ is not an eigenfunction. The Rayleigh quotient decreases with $d$ for each $\phi$, so $\lambda_1$ is nonincreasing, and strictly decreasing because the maximizer is not constant. As $d \to 0$, test functions concentrated near the maximum of $m$ give quotients close to $\max m$; as $d \to \infty$, the gradient term forces the maximizer toward a constant and $\lambda_1 \to \bar m$. $\square$

The third case is the most interesting: a habitat that is poor on average, but contains good patches, supports a population only if it moves slowly enough to stay in the good patches (Figure 5C). Slow movement is favored in a spatially heterogeneous but temporally constant environment, which is the starting point of the theory of the evolution of dispersal rates (Hastings 1983; Dockery et al. 1998; [7.19.30](/7.19.30), [7.10.10](/7.10.10)).

### 17.5.2. Does Movement Increase Abundance?

How does the total size of the population depend on movement? Intuition from the logistic equation, in which equilibrium density equals carrying capacity, suggests that the total population should equal the total resource $\int_\Omega m$. This is true only in the limits.

**Theorem 17.5.2 (Total Biomass in a Heterogeneous Habitat)** Let $m$ be nonconstant and let the positive steady state $\theta_d$ of Eq. (17.12) exist. Then

$$
\int_\Omega\theta_d\,\mathrm{d}x - \int_\Omega m\,\mathrm{d}x = \mathrm{d}\int_\Omega\frac{\lvert\nabla\theta_d\rvert^2}{\theta_d^2}\,\mathrm{d}x > 0 :
$$
the total population exceeds the total resource for every $d$. If $m \ge 0$, then $\int\theta_d \to \int m$ both as $d \to 0$ and as $d \to \infty$, so that the total population is a non-monotone function of $d$, maximal at an intermediate rate of movement (Lou 2006).

**Proof** Divide the steady-state equation $d\Delta\theta + \theta(m - \theta) = 0$ by $\theta > 0$ and integrate over $\Omega$:

$$
\mathrm{d}\int_\Omega\frac{\Delta\theta}{\theta}\,\mathrm{d}x + \int_\Omega(m - \theta)\,\mathrm{d}x = 0 .
$$
By the divergence theorem with $\partial\theta/\partial\boldsymbol{n} = 0$, $\int_\Omega\frac{\Delta\theta}{\theta} = \int_\Omega\nabla\cdot\Bigl(\frac{\nabla\theta}{\theta}\Bigr) + \int_\Omega\frac{\lvert\nabla\theta\rvert^2}{\theta^2} = \int_\Omega\frac{\lvert\nabla\theta\rvert^2}{\theta^2}$, which gives the identity. The right side is positive unless $\theta$ is constant, and a constant steady state would have to satisfy $m = \theta$, contrary to the assumption that $m$ is not constant. For the limits: as $d \to 0$, $\theta_d \to m^+ = \max(m, 0)$, the solution of the equation without movement; as $d \to \infty$, $\theta_d$ tends to a constant, which must be $\bar m$ (integrate the equation and use $\theta \to$ const). If $m \ge 0$ both limits have integral $\int m$. $\square$

When $d$ is small, individuals stay where they are born and the population matches the resource exactly, $\theta \approx m$: this is the **ideal free distribution** ([7.18.25](/7.18.25)), in which per capita growth is zero everywhere. When $d$ is large, individuals are spread evenly at the mean resource level. In between, movement carries individuals from rich to poor places, where they are at low density and therefore grow faster than they would at home; the gain in poor places outweighs the loss in rich ones. For the resource $m(x) = 2 + \sin(2\pi x)$ on $(0, 1)$, the total population is largest, about 2.5 % above the total resource, at $d \approx 0.15$ (Figure 5B). Larger effects are possible for more strongly varying resources: in one dimension the ratio $\int\theta_d/\int m$ can approach, but not exceed, 3 (Bai, He and Li 2016), whereas in higher dimensions it is unbounded. If $m$ changes sign, the limit as $d \to 0$ is $\int m^+ > \int m$: sedentary individuals simply ignore the poor patches. The practical implication is that the relation between abundance and habitat quality depends on movement, so that populations of species with different mobilities in the same landscape cannot be compared through local densities alone.

![A single species in a heterogeneous environment, Eq. (17.12) on (0, 1). A: resource m(x) = 2 + sin(2πx) (dashed) and steady states for three diffusion rates: slow dispersers match the resource, fast dispersers are almost uniform. B: total population against the diffusion rate d: it exceeds the total resource (2) for every d (Theorem 17.5.2), is largest at d ≈ 0.15 and returns to 2 in both limits. C: a habitat that is poor on average, m(x) = −0.2 + cos(2πx): the principal eigenvalue λ₁ (line) falls from about max m to mean m as d increases, and the population (points: total population of the steady state) persists only for d < d*](./plots/heterogeneous-environment.py)

## 17.6. Advection: Rivers, the Drift Paradox and Moving Habitats

### 17.6.1. The Drift Paradox

Many stream organisms, from algae and insect larvae to fish larvae, spend part of their life drifting in the current. Each individual is carried downstream on average, yet populations persist in the upper reaches of rivers for many generations.

**Definition 17.6.1 (Drift Paradox)** The **drift paradox** (Müller 1954, 1982) is the question of how populations of stream organisms that are continually displaced downstream by the current can persist in the upstream parts of a river without being washed out.

Müller's own answer, the *colonization cycle*, was that adults of aquatic insects compensate by flying upstream to lay their eggs, and upstream flight of adult mayflies has been documented (Hershey et al. 1993). But the paradox can be resolved even without directed upstream movement, as a reaction–diffusion model with advection shows. Let individuals in a river reach $0 < x < L$ (flow toward increasing $x$) diffuse with coefficient $D$, drift downstream at mean speed $v$ and grow at rate $r$ at low density:

$$
u_t = Du_{xx} - vu_x + ru\left(1 - \frac{u}{K}\right).
\tag{17.13}
$$

**Theorem 17.6.1 (Persistence Against a Current)** (a) On an unbounded river, a population introduced at a point spreads upstream at the asymptotic speed $2\sqrt{rD} - v$ and downstream at $2\sqrt{rD} + v$. It persists at every fixed point, and invades the whole river, if and only if $v < 2\sqrt{rD}$; if $v > 2\sqrt{rD}$, both edges move downstream and the population is washed out of every fixed location.

(b) In a reach of length $L$ with lethal ends, $u(0) = u(L) = 0$, the population persists if and only if

$$
v < 2\sqrt{rD} \quad\text{and}\quad L > L_{\mathrm{c}} = \frac{2\pi D}{\sqrt{4rD - v^2}} .
\tag{17.14}
$$

**Proof** (a) In the frame moving with the current, $\xi = x - vt$, the advection term disappears and the equation is the Fisher–KPP equation (17.4), whose fronts move at $\pm2\sqrt{rD}$ relative to the water (Theorem 17.3.2). Adding the velocity of the frame gives the stated speeds; the upstream edge advances if and only if $2\sqrt{rD} - v > 0$. (b) The linearization is $u_t = Du_{xx} - vu_x + ru$. Substituting $u = \mathrm{e}^{vx/(2D)}w$ gives $u_x = \mathrm{e}^{vx/(2D)}\bigl(w_x + \frac{v}{2D}w\bigr)$ and $u_{xx} = \mathrm{e}^{vx/(2D)}\bigl(w_{xx} + \frac{v}{D}w_x + \frac{v^2}{4D^2}w\bigr)$, so that

$$
w_t = Dw_{xx} + \left(r - \frac{v^2}{4D}\right)w, \qquad w(0) = w(L) = 0 .
$$
The advection is absorbed into a reduced growth rate $r - v^2/(4D)$, and by Theorem 17.4.1 the population grows from low density if and only if $r - v^2/(4D) > D\pi^2/L^2$, which is equivalent to Eq. (17.14). Persistence of the logistic model then follows as in Theorem 17.4.2. $\square$

Advection thus has two effects: it requires the population to grow fast enough to spread against the current ($v < 2\sqrt{rD}$, a condition on the organism and the river, independent of the size of the reach), and it increases the critical length of habitat, which becomes infinite as $v \to 2\sqrt{rD}$ (Figure 6A). Random movement is essential: without diffusion ($D \to 0$) no population could persist against any current, whereas diffusion allows some individuals to move upstream against the mean drift, and growth amplifies them (Speirs and Gurney 2001). Other boundary conditions (a reflecting upstream end, an outflow at the downstream end) change $L_{\mathrm{c}}$ but not the qualitative picture (Lutscher, Pachepsky and Lewis 2005). More realistic models distinguish a drifting stage from a stationary benthic stage: if individuals spend only a fraction of their time in the water column, the effective drift speed is reduced in proportion, and populations can persist even when the current is fast, provided that most reproduction happens on the bottom (Pachepsky et al. 2005). The models explain why persistence is most difficult for organisms that spend their whole life in the plankton of a river, and why river plankton develops mainly in slow, wide or regulated reaches. River regulation, which changes flow speeds, can therefore change which species can persist in a river.

![Persistence in a river, Eq. (17.13) in scaled units (D = r = 1). A: the region of persistence in a reach with lethal ends (shaded), bounded by the critical length of Eq. (17.14) and by the washout speed v = 2√(rD) (red); the dashed line is the critical length π√(D/r) without flow. B: an introduction at x = 0 in an unbounded river (flow to the right), profiles at t = 0, 10, 20, 30 and 40 (darker later): for v = 1 the population spreads both upstream and downstream; for v = 2.5 the whole population is carried downstream. C: upstream advance of the upstream edge against time for four flow speeds (points) and the predicted speed 2√(rD) − v (dashed lines)](./plots/drift-paradox.py)

### 17.6.2. Moving Habitats and Climate Change

The same mathematics applies when it is the habitat, rather than the medium, that moves. As the climate warms, the zone of suitable conditions for a species (its "climate envelope") shifts poleward and upward at a rate $q$. If the suitable zone has length $L$ and the population grows at rate $r$ inside it and dies outside, then in coordinates that move with the zone, $\xi = x - qt$, the model becomes $u_t = Du_{\xi\xi} + qu_\xi + ru(1 - u/K)$: an advection of speed $q$ away from the leading edge of the zone. By the proof of Theorem 17.6.1, the population keeps pace with the climate if and only if

$$
q < 2\sqrt{rD}\sqrt{1 - \frac{L_0^2}{L^2}}, \qquad L_0 = \pi\sqrt{\frac{D}{r}},
$$
and for a wide zone ($L \gg L_0$) if and only if $q < 2\sqrt{rD}$, or equivalently $D > D_{\mathrm{c}} = q^2/(4r)$ (Potapov and Lewis 2004; Berestycki et al. 2009). A species must be both productive and mobile enough: the speed of the climate sets a minimum for the invasion speed of the species. Leroux et al. (2013) estimated $D_{\mathrm{c}}$ from the predicted rate of shift of the climate envelopes and the growth rates of 12 North American butterfly species, and compared it with experts' assessments of their mobility, to rank the species by their risk of failing to track the climate. The condition also shows why climate change threatens species whose dispersal is limited by barriers or by fragmented habitat ([7.19.49](/7.19.49)), which effectively reduce $D$, and why the rate of climate change, not only its magnitude, matters for biodiversity.

### 17.6.3. Directed Movement Along Resource Gradients

Advection need not be imposed by the environment. Animals that move toward better habitat can be modeled by a drift up the gradient of the resource, as proposed by Belgacem and Cosner (1995):

$$
u_t = \nabla\cdot\bigl(d\nabla u - \alpha u\nabla m\bigr) + u(m - u), \qquad d\frac{\partial u}{\partial\boldsymbol{n}} - \alpha u\frac{\partial m}{\partial\boldsymbol{n}} = 0 \ \text{on}\ \partial\Omega,
$$
where $\alpha > 0$ measures the tendency to move toward higher $m$ and the boundary condition states that no individuals cross the boundary. One might expect directed movement always to help a population. In a convex habitat it does: sufficiently strong movement up the gradient guarantees persistence even when the habitat is poor on average. In a non-convex habitat, however, it can concentrate individuals at a local maximum of $m$ on the boundary and reduce the principal eigenvalue, so that "moving toward better environments" may harm persistence (Cosner and Lou 2003). Movement rules, not only habitat quality, determine the distribution and abundance of a population; the consequences of directed movement for competition are examined in [7.19.30](/7.19.30).

## 17.7. Numerical Methods

Most reaction–diffusion models have no closed-form solutions, and all the figures of this chapter were computed by the **finite difference method** ([4.4.4](/4.4.4)), which replaces derivatives by difference quotients on a grid.

### 17.7.1. Discretization

Let $x_i = i\Delta x$ and $t_n = n\Delta t$, and let $u_i^n \approx u(x_i, t_n)$. The second derivative is approximated by the central difference

$$
u_{xx}(x_i, t_n) \approx \frac{u_{i+1}^n - 2u_i^n + u_{i-1}^n}{(\Delta x)^2},
$$
with error $O\bigl((\Delta x)^2\bigr)$; in two dimensions with $\Delta x = \Delta y = h$ the Laplacian is replaced by the five-point formula $(u_{i+1,j} + u_{i-1,j} + u_{i,j+1} + u_{i,j-1} - 4u_{i,j})/h^2$. For $u_t = Du_{xx} + f(u)$ the simplest time-stepping schemes are:

| Scheme | Update | Accuracy | Stability (diffusion part) |
|---|---|---|---|
| explicit (forward Euler) | $u_i^{n+1} = u_i^n + \lambda\bigl(u_{i+1}^n - 2u_i^n + u_{i-1}^n\bigr) + \Delta t\,f(u_i^n)$ | $O(\Delta t + \Delta x^2)$ | $\lambda = D\Delta t/(\Delta x)^2 \le \frac12$ (in 2-D, $\le \frac14$) |
| implicit (backward Euler) | $u_i^{n+1} - \lambda\bigl(u_{i+1}^{n+1} - 2u_i^{n+1} + u_{i-1}^{n+1}\bigr) = u_i^n + \Delta t\,f(u_i^{n+1})$ | $O(\Delta t + \Delta x^2)$ | unconditional |
| Crank–Nicolson | average of the explicit and implicit right-hand sides | $O(\Delta t^2 + \Delta x^2)$ | unconditional |
| IMEX (implicit–explicit) | diffusion implicit, reaction explicit: $(I - \lambda A)\boldsymbol{u}^{n+1} = \boldsymbol{u}^n + \Delta t\,f(\boldsymbol{u}^n)$ | $O(\Delta t + \Delta x^2)$ | unconditional for diffusion; $\Delta t$ limited by the reaction |

Here $A$ is the tridiagonal matrix with $-2$ on the diagonal and $1$ on the off-diagonals. Implicit schemes require the solution of a linear system at each step, but for a tridiagonal matrix this costs only $O(N)$ operations (the Thomas algorithm, or a banded solver). Boundary conditions are imposed through the first and last rows: $u_0 = u_N = 0$ for Dirichlet conditions; for zero-flux conditions a "ghost point" $u_{-1} = u_1$, or a finite-volume grid of cells whose end cells exchange individuals with only one neighbor (the diagonal entry of the end rows of $A$ is then $-1$). Advection $-vu_x$ is discretized by the *upwind* difference $-v(u_i - u_{i-1})/\Delta x$ for $v > 0$, which is stable if $v\Delta t/\Delta x \le 1$ (the Courant–Friedrichs–Lewy condition); central differences for advection produce spurious oscillations.

![Finite differences. A: the space-time grid with the stencils of the explicit scheme (u at t_{n+1} computed from three values at t_n) and of the implicit scheme (three unknowns at t_{n+1} coupled to one known value). B: von Neumann amplification factors G of one time step for a Fourier mode with wave number k, against kΔx: explicit scheme for λ = 0.25, 0.5 and 0.6 (only λ ≤ 1/2 keeps |G| ≤ 1, shaded band), implicit and Crank–Nicolson schemes for λ = 2. C: the explicit scheme applied to the heat equation from a step with 1 % noise, after 60 steps: λ = 0.48 gives a smooth profile, whereas for λ = 0.52 the shortest wavelength grows by a factor |G| = 1.08 per step](./plots/finite-difference-scheme.py)

### 17.7.2. Stability

**Proposition 17.7.1 (Von Neumann Stability of the Explicit Scheme)** For the heat equation $u_t = Du_{xx}$, the explicit scheme multiplies the Fourier mode $u_i^n = G^n\mathrm{e}^{\mathrm{i}ki\Delta x}$ by the amplification factor

$$
G(k) = 1 - 4\lambda\sin^2\frac{k\Delta x}{2}, \qquad \lambda = \frac{D\Delta t}{(\Delta x)^2},
$$
and is stable ($\lvert G\rvert \le 1$ for all $k$) if and only if $\lambda \le 1/2$. In two dimensions with the five-point formula the condition is $\lambda \le 1/4$. The implicit scheme has $G = 1/\bigl(1 + 4\lambda\sin^2(k\Delta x/2)\bigr)$ and the Crank–Nicolson scheme $G = \bigl(1 - 2\lambda\sin^2(k\Delta x/2)\bigr)/\bigl(1 + 2\lambda\sin^2(k\Delta x/2)\bigr)$, both of modulus at most 1 for every $\lambda > 0$.

**Proof** Substituting the mode into the explicit scheme gives $G = 1 + \lambda(\mathrm{e}^{\mathrm{i}k\Delta x} - 2 + \mathrm{e}^{-\mathrm{i}k\Delta x}) = 1 + 2\lambda(\cos k\Delta x - 1) = 1 - 4\lambda\sin^2(k\Delta x/2)$. Its minimum over $k$ is $1 - 4\lambda$, at $k\Delta x = \pi$, so $\lvert G\rvert \le 1$ for all $k$ if and only if $1 - 4\lambda \ge -1$. In two dimensions $G = 1 - 4\lambda\bigl(\sin^2(k_x h/2) + \sin^2(k_y h/2)\bigr)$ with minimum $1 - 8\lambda$. For the implicit and Crank–Nicolson schemes, the same substitution gives the stated factors, which lie in $(0, 1]$ and $[-1, 1]$ respectively. $\square$

The unstable mode is the shortest one the grid can represent, a zigzag from point to point, which grows by $\lvert 1 - 4\lambda\rvert$ per step: with $\lambda = 0.52$ by 8 % per step, so that rounding errors become visible within a few dozen steps (Figure 7C). The reaction term adds the condition that $\Delta t$ be small relative to the time scale of local dynamics: near an equilibrium $u^*$ the scheme multiplies perturbations by $1 + \Delta t f'(u^*)$, which must lie in $(-1, 1)$ for stable equilibria (for the logistic equation $\Delta t < 2/r$), and much smaller steps are needed for accuracy. Resolution in space matters as well: a Fisher front has width of order $\sqrt{D/r}$, and the grid must resolve it ($\Delta x \ll \sqrt{D/r}$), otherwise the computed speed is wrong and, with Allee effects, fronts can stop artificially (the discrete pinning of Section 17.3.3). A standard check is to halve $\Delta x$ and $\Delta t$ and confirm that the results do not change.

The IMEX scheme used in this chapter takes a few lines with a banded solver:

```python
import numpy as np
from scipy.linalg import solve_banded


def fisher_imex(u, D, r, dx, dt, steps):
    """Fisher-KPP u_t = D u_xx + r u (1 - u), zero-flux ends; implicit diffusion, explicit growth."""
    n = u.size
    lam = D * dt / dx**2
    ab = np.zeros((3, n))                  # banded form of (I - lam * A)
    ab[0, 1:] = -lam
    ab[1, :] = 1 + 2 * lam
    ab[2, :-1] = -lam
    ab[1, 0] = ab[1, -1] = 1 + lam         # zero flux: end cells have one neighbour
    for _ in range(steps):
        u = solve_banded((1, 1), ab, u + dt * r * u * (1 - u))
    return u
```

For two- and three-dimensional problems, the same idea is implemented with sparse matrices or, on periodic domains, with fast Fourier transforms, in which the Laplacian is diagonal (pseudospectral methods; [7.19.30](/7.19.30)). Integrodifference equations (17.7) are computed by fast convolution with the kernel, as in Figure 3.

## Summary

| Model | Equation | Key result |
|---|---|---|
| diffusion | $u_t = D\Delta u$ | random walk limit; MSD $= 4Dt$ in the plane, Eq. (17.2) |
| reaction–diffusion | $u_t = D\Delta u + f(u)$ (Definition 17.1.1) | natural scales $1/r$ and $\sqrt{D/r}$ |
| Skellam | $u_t = D\Delta u + ru$ | range radius $\sim 2\sqrt{rD}\,t$, $\sqrt{\text{area}}$ linear (Proposition 17.2.1) |
| Fisher–KPP | $u_t = Du_{xx} + ru(1 - u/K)$ | fronts for $c \ge 2\sqrt{rD}$ (Theorem 17.3.1); invasion speed $2\sqrt{rD}$, pulled front (Definition 17.3.1, Theorem 17.3.2) |
| strong Allee effect | $f = ru(1 - u)(u - a)$ | pushed front, $c = (1 - 2a)\sqrt{rD/2}$; retreat if $a > 1/2$ (Proposition 17.3.3) |
| integrodifference | $N_{t+1} = k * F(N_t)$ (Definition 17.3.2) | $c^* = \min_s \ln(R_0M(s))/s$, Eq. (17.8); fat tails: accelerating spread |
| KISS | $u_t = Du_{xx} + ru$, $u = 0$ at edges | $L_{\mathrm{c}} = \pi\sqrt{D/r}$ (Theorems 17.4.1, 17.4.2; Definition 17.4.1); disk $R_{\mathrm{c}} = 2.405\sqrt{D/r}$; matrix mortality, Eq. (17.11) |
| heterogeneous habitat | $u_t = d\Delta u + u(m - u)$ | persistence iff $\lambda_1(d, m) > 0$ (Proposition 17.5.1); total population exceeds total resource (Theorem 17.5.2) |
| river | $u_t = Du_{xx} - vu_x + f(u)$ | upstream speed $2\sqrt{rD} - v$; persistence iff $v < 2\sqrt{rD}$ and $L > 2\pi D/\sqrt{4rD - v^2}$ (Theorem 17.6.1) |
| moving climate | advection $q$ in the frame of the habitat | track the climate iff $q < 2\sqrt{rD}$, $D_{\mathrm{c}} = q^2/(4r)$ |
| numerics | explicit, implicit, Crank–Nicolson, IMEX | explicit stable iff $D\Delta t/\Delta x^2 \le 1/2$ (Proposition 17.7.1) |

- Diffusion describes the population consequences of random movement; its coefficient is estimated from mean squared displacements, Eq. (17.2), and every length in the theory scales with $\sqrt{D/r}$.
- Invasions without Allee effects advance at $2\sqrt{rD}$, set at the low-density leading edge (muskrat, cabbage white); Allee effects slow or stop them (gypsy moth). Long-distance jumps, fat-tailed kernels and spatial sorting make spread accelerate (corn rootworm, zebra mussel, cane toad, Reid's paradox).
- A habitat patch must exceed a critical size that grows with mobility and shrinks with growth rate and matrix quality (the drift paradox, Definition 17.6.1, is the analog for rivers); compact patches are most efficient.
- In heterogeneous habitats, slow movement allows persistence in habitats that are poor on average, and intermediate movement maximizes total abundance; a moving climate requires the invasion speed of a species to exceed the speed of the climate.

## Questions

1. A beetle released at the center of a uniform field is recaptured after 10 days; the mean squared distance of the recaptured beetles from the release point is $800\,\mathrm{m^2}$. Estimate $D$. If the beetle population grows at $r = 0.05\,\mathrm{d^{-1}}$ at low density, at what rate would an established population spread, and how large must a square field surrounded by hostile habitat be for a population to persist?

   **Answer** By Eq. (17.2), $\hat D = 800/(4 \times 10) = 20\,\mathrm{m^2\,d^{-1}}$. The invasion speed is $2\sqrt{rD} = 2\sqrt{0.05 \times 20} = 2\,\mathrm{m\,d^{-1}}$, about 0.4 km in a 200-day season. The critical side of a square is $L_{\mathrm{c}} = \pi\sqrt{2D/r} = \pi\sqrt{800} \approx 89\,\mathrm{m}$, an area of about 0.8 ha. In practice the estimate of $D$ should be checked by recapturing at several times (the MSD should increase linearly), and losses of marked beetles by emigration bias $\overline{r^2}$ downward if far-dispersing individuals leave the trapping grid.

2. Show that $u(x, t) = U(x - ct)$ with $c < 0$ cannot be a front of Eq. (17.5) connecting 1 at $-\infty$ to 0 at $+\infty$, and give a biological interpretation.

   **Answer** Multiply Eq. (17.5) by $U'$ and integrate over $\mathbb{R}$: $\int U''U' = \frac12[U'^2]_{-\infty}^{\infty} = 0$, so $c\int U'^2\,\mathrm{d}z = -\int U(1 - U)U'\,\mathrm{d}z = \int_0^1 u(1 - u)\,\mathrm{d}u = \frac16 > 0$, and $c > 0$. A population with positive growth at all densities below carrying capacity can never retreat in homogeneous space: individuals that move ahead of the front always increase. Retreat requires negative growth at low density, as with a strong Allee effect ($a > 1/2$ in Proposition 17.3.3), or a deteriorating habitat.

3. Compare the invasion speeds of an annual plant with $R_0 = 20$ seeds per plant surviving to reproduce and a Gaussian dispersal kernel with $\sigma = 5\,\mathrm{m}$ per generation, and of a plant with the same kernel but $R_0 = 5$. What does this imply for weed control that halves seed production?

   **Answer** $c^* = \sigma\sqrt{2\ln R_0}$: for $R_0 = 20$, $c^* = 5\sqrt{2 \times 3.00} = 12.2\,\mathrm{m}$ per year; for $R_0 = 5$, $c^* = 5\sqrt{2 \times 1.61} = 9.0\,\mathrm{m}$ per year. Because the speed depends on $\sqrt{\ln R_0}$, halving seed production from 20 to 10 reduces the speed only from 12.2 to $5\sqrt{2\ln 10} = 10.7\,\mathrm{m}$ per year, by 12 %. Reducing dispersal distance (for example by preventing seed transport by machinery, which also cuts the fat tail of the kernel) is far more effective, since $c^*$ is proportional to $\sigma$, and removal of outlying plants ahead of the front attacks the part of the population that determines the speed.

4. A nature reserve is a circular forest of radius 2 km surrounded by farmland that is lethal for a forest-dwelling rodent with $r = 0.5\,\mathrm{yr^{-1}}$. What is the largest diffusion coefficient for which the rodent can persist? How does the answer change if farmland is not lethal but individuals die there at rate $\mu = 2\,\mathrm{yr^{-1}}$ (use the one-dimensional formula as an approximation)?

   **Answer** Persistence requires $R > 2.405\sqrt{D/r}$, i.e. $D < r(R/2.405)^2 = 0.5 \times 0.69 = 0.35\,\mathrm{km^2\,yr^{-1}}$. With matrix mortality, Eq. (17.11) with the diameter $L = 4\,\mathrm{km}$: $L = 2\sqrt{D/r}\arctan\sqrt{\mu/r} = 2\sqrt{D/r}\arctan 2 = 2.21\sqrt{D/r}$, compared with $\pi\sqrt{D/r}$ for a lethal matrix; so the admissible $D$ increases by the factor $(\pi/2.21)^2 \approx 2.0$. A less hostile matrix roughly doubles the mobility the species can afford, or halves the area of reserve it needs.

5. Explain, using Theorem 17.5.2, why a species that moves at an intermediate rate can be more abundant in a patchy landscape than either a sedentary or a highly mobile species with the same local demography. Does this mean that intermediate dispersal evolves?

   **Answer** Sedentary individuals match the local resource ($\theta = m$), so the total equals the total resource; very mobile individuals are spread evenly at the mean resource level, again with total $\int m$. At intermediate rates, movement transfers individuals into poor sites, where they are below the local carrying capacity and grow faster per capita, so the net gain there exceeds the loss from rich sites, and the total exceeds $\int m$ by $d\int\lvert\nabla\theta\rvert^2/\theta^2$. Abundance is not fitness, however: in a constant heterogeneous environment, a rare mutant that disperses more slowly can invade a resident at its steady state, because the resident overshoots in poor sites and undershoots in rich ones relative to the ideal free distribution; selection then favors ever slower dispersal (Dockery et al. 1998), even though the population size declines. Faster dispersal is favored by temporal variability, kin competition and the colonization of empty habitat ([7.10.10](/7.10.10), [7.19.16](/7.19.16)).

6. A planktonic rotifer in a river grows at $r = 0.3\,\mathrm{d^{-1}}$ and is mixed along the river with an effective diffusion coefficient $D = 0.5\,\mathrm{km^2\,d^{-1}}$. Up to what mean current speed can it persist? A dam reduces the current in a 30 km reservoir from $1.0$ to $0.2\,\mathrm{km\,d^{-1}}$; can the rotifer persist in the reservoir if the river above and below is unsuitable?

   **Answer** Washout occurs at $v = 2\sqrt{rD} = 2\sqrt{0.15} = 0.77\,\mathrm{km\,d^{-1}}$, so in the free-flowing river ($v = 1.0$) the population cannot maintain itself. In the reservoir, $4rD - v^2 = 0.6 - 0.04 = 0.56$ and $L_{\mathrm{c}} = 2\pi \times 0.5/\sqrt{0.56} = 4.2\,\mathrm{km}$, far shorter than the 30 km reservoir: the rotifer persists. This illustrates how impoundment converts riverine into lake-like plankton communities.

7. (Open question) Discuss which assumptions of the Fisher–KPP model are most likely to fail when it is used to predict the spread of an invasive plant across China, and how the model could be modified.

   **Answer** Points to cover: dispersal is not diffusive but stratified, with human-mediated long-distance jumps along roads, rivers and trade routes, which calls for fat-tailed kernels, integrodifference or network models with transport data (as in the zebra mussel gravity model); the landscape is heterogeneous (climate, land use, unsuitable areas), so $r$ and $D$ depend on location (Section 17.5) and the range may be limited by climatic suitability (species distribution models, [7.19.49](/7.19.49)); Allee effects in sparse populations may cause lags and pinning; the invader evolves (spatial sorting, adaptation to new climates), so $r$ and $D$ change at the front; and management (eradication of outliers, quarantine) changes the dynamics. A useful modified model combines a spatially explicit growth map with a kernel that includes rare jumps, is calibrated on the observed spread history, and is used to rank areas by risk of arrival rather than to predict a single front.
