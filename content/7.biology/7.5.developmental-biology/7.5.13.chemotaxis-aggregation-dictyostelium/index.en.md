---
title: "Chemotaxis and Aggregation: Dictyostelium"
description: Multicellularity by aggregation in the social amoeba Dictyostelium discoideum. The life cycle; proportion regulation of prestalk and prespore cells, its allometry and a reaction-diffusion reading of it; cAMP signaling and relay, the Cohen–Robertson pulse model, critical density and wave speed, the continuum limit, target and spiral waves; the Keller–Segel model, its derivation, linear instability at infinite wavelength and the territory-size problem; chemotaxis-augmented Turing systems; nonlinear theory (amplitude equation, elliptic-function steady states, subcritical bifurcation, solitary aggregates and sech² clusters); dimension-dependent collapse and the critical mass in two dimensions; and chemotaxis in animal embryos.
---

The embryos of the preceding chapters arise from one cell by division. *Dictyostelium discoideum* reaches multicellularity the other way round: up to about $10^5$ free-living amoebae, starving, gather into one organism that moves, differentiates into two cell types in fixed proportion, and builds a fruiting body. It is a member of the Amoebozoa, a social amoeba, and not a fungus, although its traditional name "cellular slime mould" and its spore-bearing fruiting bodies once placed it with the fungi; its classification and ecology belong to [7.11](/7.11). For developmental biology it offers what few embryos do: a pattern whose cells can be counted, a signal (**cyclic AMP**) that was identified early, and aggregation driven by **chemotaxis** ([7.3.15](/7.3.15)), which the Keller–Segel model turned into one of the most studied equations of mathematical biology. The chapter follows the life cycle: proportion regulation (Section 13.2) applies the reaction-diffusion ideas of [7.5.12](/7.5.12); relay waves (13.3) are an excitable medium; the Keller–Segel model (13.4–13.7) describes aggregation as an instability; Section 13.8 points to chemotaxis in animal embryos.

## 13.1. The Life Cycle

Spores germinate in moist soil into amoebae that feed on bacteria by phagocytosis and divide. When food runs out, the cells change their programme over a few hours: they begin to emit and relay pulses of **cyclic AMP** (cAMP), move towards its source, and stream along the paths of their neighbours into aggregation centres. The aggregate forms a mound, which develops a tip and elongates into a slug, a few millimetres long, that migrates towards light and warmth on a sheath of slime it secretes. About the front fifth of the slug consists of prestalk cells and the rest of prespore cells. At culmination the prestalk cells move down through the mass in a reverse fountain, secrete a cellulose tube and become the stalk, a column of dead, vacuolated cells, which lifts the prespore cells into the sorus at its top, where they become spores. A sexual cycle, through giant cells (macrocysts), also exists.

![The asexual life cycle of *Dictyostelium discoideum*. Spores germinate into amoebae that feed and divide; starvation triggers cAMP signaling and aggregation in streams; the mound develops a tip, forms a migrating slug with prestalk cells (red) in front and prespore cells (blue) behind, and culminates in a fruiting body in which prestalk cells form the stalk and prespore cells the spores](./plots/life-cycle.py)

Aggregation makes the stalk an act of cooperation: stalk cells die so that others disperse as spores. This raises questions of social evolution (cheater mutants that preferentially become spores, kin discrimination) that belong to [7.10](/7.10). It also makes the organism a clean case of cell-type proportioning, because cells of different lineages are mixed at the start: the pattern cannot have been laid down in an egg.

## 13.2. Proportion Regulation

The ratio of prespore to prestalk tissue is regulated: it is about the same at the start of slug migration and at culmination, and when a slug is cut, each fragment readjusts its proportions. The regulation is not exact but allometric,

$$
\frac{\text{prespore volume}}{\text{prestalk volume}}=KV^\lambda,\qquad\lambda\approx0.2,
$$
so that smaller slugs have relatively more prestalk tissue. Conversion of prespore to prestalk cells is fast, the reverse slower; longer migration raises the prespore fraction at the rear; light, glucose and temperature shift the ratio towards spores, and lithium ions towards stalk. The slug is also polarized cell by cell: each cell carries its contractile **vacuole** behind the nucleus.

How cells choose their type is now understood better than when these observations were first modelled. The choice is biased by each cell's history: cells that were at a particular phase of the **cell cycle** when starvation began, or that had grown on glucose, tend to become prestalk or prespore. Prestalk and prespore cells first appear scattered in a salt-and-pepper pattern in the mound and then sort out, prestalk cells moving to the tip by stronger chemotaxis to cAMP and different adhesion (the **differential adhesion hypothesis**, [7.5.7](/7.5.7)). Proportions are adjusted by diffusible signals: the chlorinated polyketide DIF-1, made mainly by prespore cells, induces a subtype of prestalk cells and inhibits prespore differentiation, and prestalk cells degrade it, a negative feedback that restores the ratio after the removal of either part. Sorting out of cells that differentiated at random is therefore the primary mechanism; a reaction-diffusion **prepattern** in the slug, which the model below assumes, is not.

The reaction-diffusion model nevertheless captures the quantitative regularities, and it does so with the switch-point mathematics of [7.5.12](/7.5.12). Assume (i) a weak source density of activator decreasing from the front of the slug, (ii) activated tissue becomes prestalk and unactivated prespore, and (iii) the transition layer of constant thickness $d$ between them is phenotypically prestalk. Let the activated region be a fixed fraction $\alpha$ of the slug apart from the transition layer (relative regulation at a switch point, Proposition 12.5.1), and let the volume of the layer be a fraction $1/(\beta V^{1/3})$ of the slug volume $V$ (its cross-section scales as $V^{2/3}$). Then

$$
\frac{\text{stalk}}{\text{spore}}=\frac{\alpha(1-v_t)+v_t}{(1-\alpha)(1-v_t)}=\frac\alpha{1-\alpha}\Big(1+\frac1\alpha\,\frac1{\beta V^{1/3}-1}\Big),\qquad v_t=\frac1{\beta V^{1/3}},
$$
which is larger in small slugs and approaches $\alpha/(1-\alpha)$ in large ones. Over a range of volumes the curve is close to a power law with an exponent near $0.2$.

In this model, regeneration is controlled by inhibitor diffusion. Cut off the front of a slug of length $L$ at $x=\ell$. The old inhibitor profile $h_0$ no longer satisfies the no-flux condition at the new end; the missing flux acts as a sink $\nu h_0'(\ell)\delta(x-\ell)$ switched on at $t=0$, and the change $\Delta h$ obeys the diffusion equation with $\Delta h'(\ell)=-h_0'(\ell)$. In the Laplace domain ([2.5.6](/2.5.6)), $\nu\Delta\tilde h''=\Omega\Delta\tilde h$ with $\Delta\tilde h'(\ell)=-h_0'(\ell)/\Omega$, so

$$
\Delta\tilde h(x,\Omega)=-\sqrt\nu\,h_0'(\ell)\,\frac{\mathrm{e}^{-(\Omega/\nu)^{1/2}(\ell-x)}}{\Omega^{3/2}},\qquad
\Delta h(x,t)=-\sqrt\nu\,h_0'(\ell)\Big[2\sqrt{\frac t\pi}\,\mathrm{e}^{-z^2}-\frac{\ell-x}{\sqrt\nu}\operatorname{erfc}z\Big],
$$
with $z=(\ell-x)/(2\sqrt{\nu t})$. For $(\ell-x)^2\gg\nu t$ the asymptotic expansion of erfc gives

$$
\Delta h(x,t)\approx-\frac4{\sqrt\pi}\,h_0'(\ell)\,\frac{(\nu t)^{3/2}}{(\ell-x)^2}\,\mathrm{e}^{-(\ell-x)^2/4\nu t}:
$$
the perturbation reaches the old switch point $x_s$ after a time of order $(\ell-x_s)^2/\nu$, the characteristic diffusional dependence. Regulation is slower, as the square of the distance, in larger fragments, which is testable by timing the re-expression of prestalk markers in fragments of different size.

![A: prespore-to-prestalk ratio in the reaction-diffusion model of the slug (alpha = 0.15) against volume, compared with a power law of exponent 0.2 (dashed); the ratio saturates at (1 - alpha) / alpha in large slugs. B: after truncation, the change of inhibitor at distances 1, 2 and 3 from the cut (units with nu = 1, normalized); the time to reach 1 % of the late value (dots) grows as the square of the distance](./plots/proportion.py)

## 13.3. cAMP Signaling and Relay

The chemoattractant, first called acrasin, was identified as 3′,5′-cyclic AMP in 1967. Starving cells express the **G protein–coupled receptor** cAR1 and the **adenylyl cyclase** ACA; binding of cAMP activates the cyclase through G proteins, the cell synthesizes cAMP and secretes it, and a few minutes later it adapts and becomes refractory. An extracellular **cyclic nucleotide phosphodiesterase** (PdsA), regulated by a secreted inhibitor, destroys the signal. Early in aggregation, cells near the centres fire about every 6 min; the period later shortens to 2–3 min.

**Definition 13.3.1 (cAMP Relay)** **cAMP relay** is the response of a *Dictyostelium* cell to a rise in extracellular cAMP above a threshold by synthesizing and secreting a pulse of cAMP, followed by adaptation and a refractory period, so that a signal is amplified and propagated from cell to cell as a wave.

Each cell moves towards the source during the rising phase of each wave, about $20\,\mathrm{\mu m}$ per pulse, and does not follow the attractant back on the falling phase, even though the gradient then points away: the "back-of-the-wave problem", solved by the adaptation of the polarity machinery ([7.3.15](/7.3.15)).

**Formula 13.3.1 (Cohen–Robertson Relay)** Let cells at density $a$ (per unit area) have mean spacing $R$, $a^{-1}=\pi R^2/4$, and let a firing cell release an instantaneous pulse of strength $s$ that diffuses in the plane with coefficient $\nu$. A neighbour at distance $R$ sees

$$
\rho(R,t)=\frac s{4\pi\nu t}\,\mathrm{e}^{-R^2/4\nu t}=\frac{sa}4\,g(\tau),\qquad g(\tau)=\frac{\mathrm{e}^{-1/\tau}}\tau,\quad\tau=\frac{4\nu t}{R^2}.
$$
Since $g\le g(1)=1/\mathrm{e}$, a neighbour with firing threshold $\rho_c$ is reached only if

$$
a>a_c=\frac{4\mathrm{e}\rho_c}s ;
$$
above this density it fires at $T_p=\frac{R^2}{4\nu}\tau_p$, where $\tau_p$ is the smaller root of $g(\tau_p)=4\rho_c/(sa)$, plus a relay delay $T_d$, and the wave travels at

$$
v(a)=\frac R{T_p+T_d}=\frac{(4/\pi a)^{1/2}}{\tau_p/(\pi\nu a)+T_d}.
$$

**Proof** The heat kernel in two dimensions is $(4\pi\nu t)^{-1}\mathrm{e}^{-r^2/4\nu t}$ ([2.5.7](/2.5.7)); substituting $4\pi\nu t=4\tau/a$ gives $\rho$. $g'(\tau)=\mathrm{e}^{-1/\tau}(1-\tau)/\tau^3$ vanishes at $\tau=1$. $\square$

There is a critical density below which relay fails, and the speed depends on density. With the estimates $T=300\,\mathrm{s}$ (period), $T_d=15\,\mathrm{s}$ and a movement duration $T_c=100\,\mathrm{s}$ per pulse, and $\nu\approx400\,\mathrm{\mu m^2\,s^{-1}}$ for cAMP, diffusion over the spacing $R\approx30$–$60\,\mathrm{\mu m}$ takes a fraction of a second: the speed is set by the relay delay, $v\approx R/T_d$, of the order of $100$–$200\,\mathrm{\mu m\,min^{-1}}$, the order of the measured speeds of a few hundred micrometres per minute.

![Cohen-Robertson relay. A: the cAMP signal seen by the nearest neighbour as a function of the scaled time tau; a neighbour fires where the curve crosses its threshold, which is possible only above the critical density (the curve's maximum is 1/e), and fires sooner at higher density (a / a_c = 1.2, 2 and 5). B: wave speed against density for a relay delay of 15 s: the delay dominates, and the speed follows R / T_d](./plots/relay-waves.py)

The model also yields a continuum description of aggregation in one dimension. Let the $n$th wave pass at positions $x_n(t)$ with speed $\mathrm{d}x_n/\mathrm{d}t=v(a_n)$, and let each wave move every cell a distance $\Delta(a)$ towards the centre at $x=0$, which in the early stages is a constant and vanishes at close packing. If the movement is brief compared with the period ($T_c\ll T$), one wave maps the density $a_{n-1}$ into $a_n$, and conservation of cells (the cells in $[x,x+\mathrm{d}x]$ after the wave were in $[x+\Delta,\,x+\mathrm{d}x+\Delta(a)+\Delta'a_x\mathrm{d}x]$ before it) gives, for small $\Delta$ and $a(x,nT)=a_n(x)$,

$$
a_t+\frac{\partial Q(a)}{\partial x}=0,\qquad Q(a)=-\frac{a\,\Delta(a)}T .
$$
This is a kinematic wave equation: density disturbances move along characteristics with speed $Q'(a)$, compress towards the centre, and form a shock; since there is no random motion, the cells collect at $x=0$ in a delta function of growing weight. The pulsatile waves themselves move through this changing density along $\dot x=v(a)\propto a^{-1/2}$ (for $T_p\ll T_d$): the organizing waves create the chemotactic pattern, and the pattern changes the waves.

Fields of aggregating cells show concentric target waves around periodically firing centres and, more often, rotating spirals. Both are generic for excitable media, in which a supra-threshold stimulus triggers a pulse followed by refractoriness. The relay is now modelled by receptor-desensitization models (Martiel and Goldbeter, 1987) and by coarse-grained excitable dynamics; collective oscillations arise when the density passes a threshold, a form of dynamical quorum sensing (Gregor and colleagues, 2010). Spirals need no special pacemaker cell: any broken wave front curls into one.

![Excitable waves in a generic excitable medium (Barkley model). Left: a periodically stimulated centre emits concentric target waves; the refractory zone behind each front prevents back-propagation. Right: a broken front curls into a self-sustained spiral](./plots/spiral-waves.py)

## 13.4. The Keller–Segel Model

Keller and Segel (1970) described the onset of aggregation as an instability of a uniform field of cells, smoothing over the pulses. Let $a(\boldsymbol{r},t)$ be the density of amoebae, $\rho$ the attractant, $\eta$ the degrading enzyme and $c$ the enzyme–attractant complex, with $\rho+\eta\rightleftharpoons c\to\eta+\text{product}$ (rate constants $k_1$, $k_{-1}$, $k_2$). With production proportional to the density of cells,

$$
\rho_t=-k_1\rho\eta+k_{-1}c+af(\rho)+\nu_0\Delta\rho,\quad \eta_t=-k_1\rho\eta+(k_{-1}+k_2)c+aF(\rho,\eta)+\delta\Delta\eta,\quad c_t=k_1\rho\eta-(k_{-1}+k_2)c+\lambda_c\Delta c .
$$
If the enzymatic step is fast and the total enzyme $\eta+c=\eta_0$ is fixed, Michaelis–Menten elimination ([7.5.12](/7.5.12#sec-12.2.4)) gives $\eta=\eta_0/(1+K\rho)$ with $K=k_1/(k_{-1}+k_2)$, and the attractant obeys

$$
\rho_t=af(\rho)-g(\rho)+\nu_0\Delta\rho,\qquad g(\rho)=\frac{\eta_0k_2K\rho}{1+K\rho}.
$$
Cells are conserved, $a_t+\nabla\cdot\boldsymbol{J}=0$, and their flux has a chemotactic part up the gradient of $\rho$ and a random-motility part down the gradient of $a$.

**Definition 13.4.1 (Keller–Segel Model)** The **Keller–Segel model** is the system

$$
a_t=\nabla\cdot\big(\mu(a,\rho)\nabla a-\kappa(a,\rho)\nabla\rho\big),\qquad \rho_t=af(\rho)-g(\rho)+\nu\Delta\rho,
\tag{13.1}
$$
for the density $a$ of cells with random motility $\mu$ and chemotactic sensitivity $\kappa$, and an attractant $\rho$ produced by the cells at rate $f$ per cell and removed at rate $g$.

Linearize about a uniform state $(a_0,\rho_0)$ with $a_0f(\rho_0)=g(\rho_0)$. With $\alpha_0=a_0f'(\rho_0)-g'(\rho_0)$, $f_0=f(\rho_0)$, $\mu_0$, $\kappa_0$ the values at the uniform state,

$$
\rho'_t=\alpha_0\rho'+f_0a'+\nu_0\Delta\rho',\qquad a'_t=-\kappa_0\Delta\rho'+\mu_0\Delta a' .
$$
For perturbations $\mathrm{e}^{\sigma t+\mathrm{i}\boldsymbol{k}\cdot\boldsymbol{r}}$, $\sigma^2+A\sigma+B=0$ with

$$
A=(\mu_0+\nu_0)k^2-\alpha_0,\qquad B=\mu_0\nu_0k^4-(\mu_0\alpha_0+\kappa_0f_0)k^2 .
$$

**Theorem 13.4.1** (a) The growth rates are real: $A^2-4B=\big((\mu_0-\nu_0)k^2+\alpha_0\big)^2+4\kappa_0f_0k^2\ge0$, so chemotactic aggregation does not oscillate in this model. (b) At $k=0$, $\sigma\in\{0,\alpha_0\}$, and $\alpha_0<0$ is required for the attractant to be stable without cells moving. (c) A mode $k$ grows if and only if $B<0$, that is $\mu_0\alpha_0+\kappa_0f_0>\mu_0\nu_0k^2$, and some mode grows if and only if

$$
\Delta\equiv\mu_0\alpha_0+\kappa_0f_0>0\iff\mu_0a_0f'(\rho_0)+\kappa_0f_0>\mu_0g'(\rho_0).
$$
(d) Near onset ($0<\Delta\ll1$), $\sigma\approx(\Delta k^2-\mu_0\nu_0k^4)/\lvert\alpha_0\rvert$, maximal at $k^2_{\max}=\Delta/(2\mu_0\nu_0)$ with $\sigma_{\max}=\Delta^2/(4\lvert\alpha_0\rvert\mu_0\nu_0)$.

**Proof** (a) Expand: $A^2-4B=(\mu_0+\nu_0)^2k^4-2\alpha_0(\mu_0+\nu_0)k^2+\alpha_0^2-4\mu_0\nu_0k^4+4(\mu_0\alpha_0+\kappa_0f_0)k^2$, which regroups as stated. (b), (c) With $A>0$ (since $\alpha_0<0$), the product of the roots is $B$; one root is positive exactly when $B<0$. (d) For small $\sigma$, $\sigma\approx-B/A\approx-B/\lvert\alpha_0\rvert$ with $k^2=O(\Delta)$, so $\sigma=O(\Delta^2)$; maximize over $k^2$. $\square$

The condition says that the uniform state is unstable when attractant production or the chemotactic response is strong compared with attractant destruction: a small cluster makes more attractant, which draws more cells. The striking feature is (d): the marginal mode is $k=0$, infinite wavelength. As $\Delta$ passes zero, the longest waves are excited first, and the preferred wavelength $2\pi/k_{\max}\propto\Delta^{-1/2}$ depends on how far beyond threshold the system is. Real aggregation fields, however, break up into territories of a definite size. Segel and Stoeckley discussed modifications: identifying territory size with the fastest wavelength makes it depend on the initial $\Delta$; a threshold for signaling makes the problem nonlinear and predicts a maximal spacing; an enlarged chemical system can give a finite wavelength, but then the length scale is chemical (a diffusive instability) and the cells follow it. A "true" chemotactic instability tends to have zero critical wave number. The resolution in the real organism is that territories are set by the relay waves of Section 13.3, which the smooth model averages out.

![A: growth rate of the Keller-Segel model for Delta = -0.2, 0.1, 0.4 and 1: the unstable band always starts at k = 0. B: a chemotaxis-augmented Turing system whose chemistry alone is stable at every wave number (dashed, off the bottom of the scale) becomes unstable in a band of finite wave numbers when cells that make both chemicals move up the gradient of the first; the example of Section 13.5 (kappa1 = 1) is just past threshold, kappa1 = 1.5 well past it](./plots/ks-dispersion.py)

## 13.5. Chemotaxis-Augmented Turing Systems

Is infinite critical wavelength typical of patterning by directed movement? Consider $n$ chemicals produced by the cells and reacting among themselves, linearized:

$$
\rho_{i,t}=f_ia+\sum_j\alpha_{ij}\rho_j+\nu_i\Delta\rho_i,\qquad a_t=-\sum_i\kappa_i\Delta\rho_i+\mu\Delta a,
$$
with some $\kappa_i$ possibly zero. For a mode $\mathrm{e}^{\mathrm{i}\boldsymbol{k}\cdot\boldsymbol{r}+\sigma t}$, the second equation gives $a=k^2\kappa^{\mathsf T}\rho/(\sigma+\mu k^2)$, and eliminating $a$,

$$
\big[\sigma^2I+\sigma(P+k^2Q)+\mu k^2(k^2S-R)\big]\hat\rho=0,\qquad P=-\alpha,\ Q=\operatorname{diag}(\mu+\nu_i),\ S=\operatorname{diag}(\nu_i),\ R=\alpha+\frac{f\kappa^{\mathsf T}}\mu .
$$
At the onset of a non-oscillatory instability ($\sigma\to0$) the problem reduces to $\det(k^2S-R)=0$: a Turing problem ([7.5.12](/7.5.12), Theorem 12.3.1) for the augmented matrix $R$ in place of $\alpha$. If $R$ can produce a diffusive instability with a finite chemical wavelength even though $\alpha$ cannot, the critical wavelength is finite although the mechanism involves chemotaxis. With one chemical this is impossible (a $1\times1$ "Turing" problem has its critical mode at $k=0$), but with two chemicals it can happen.

**Example 13.5.1** Take $\nu_1=1$, $\nu_2=4$, $f_1/\mu=f_2/\mu=1$, $\kappa_1=1$, $\kappa_2=0$ and $\alpha=\begin{bmatrix}2&-3\\5&-5\end{bmatrix}$. Then $\operatorname{tr}\alpha=-3$ and $\det\alpha=5$, but $\nu_1\alpha_{22}+\nu_2\alpha_{11}=3<2\sqrt{\nu_1\nu_2\det\alpha}=2\sqrt{20}=8.94$: the chemicals alone have no Turing instability. With chemotaxis, $R=\begin{bmatrix}3&-3\\6&-5\end{bmatrix}$, $\det R=3$, and $\nu_1R_{22}+\nu_2R_{11}=7>2\sqrt{12}=6.93$: a finite band of wave numbers is unstable, if only just.

Chemotaxis can thus realize a capacity for diffusive instability that the chemistry already has (a destabilizing tendency at long wavelengths) but cannot express alone. At the other extreme, if $\alpha$ is symmetric negative definite ("absolutely stable") with a nondegenerate leading eigenvector $\boldsymbol{v}$, and $f$, $\kappa$ are both parallel to $\boldsymbol{v}$ with the product of their lengths chosen to make the largest eigenvalue of $R$ zero, then $\rho^{\mathsf T}B\rho>0$ for all $k\ne0$ and the instability sets in at infinite wavelength. In a real tissue the size and shape of the domain decide which of these limits applies.

## 13.6. Nonlinear Theory

### 13.6.1. An Amplitude Equation

Near onset, $\sigma\sim k^4\sim\Delta^2$. Write $\Delta=\mu_0\alpha_0+\kappa_0f_0=\varepsilon r$, expand $a=a_0+\varepsilon a_1+\varepsilon^2a_2+\cdots$, $\rho=\rho_0+\varepsilon\rho_1+\cdots$ in the slow variables $\tilde{\boldsymbol{x}}=\varepsilon^{1/2}\boldsymbol{x}$, $\tilde t=\varepsilon^2t$. At order $\varepsilon$ the attractant equation gives $f_0a_1+\alpha_0\rho_1=0$, and since $f_0/\lvert\alpha_0\rvert=\mu_0/\kappa_0+O(\varepsilon)$, $\rho_1=\mu_0a_1/\kappa_0$: the attractant follows the cells. Adding $\kappa_0\tilde\nabla^2$ times the attractant equation to $\alpha_0$ times the cell equation eliminates the leading terms and, at the next order,

$$
-\alpha_0\frac{\partial a_1}{\partial\tilde t}+r\tilde\nabla^2a_1+\nu\mu_0\tilde\nabla^4a_1+q\tilde\nabla^2a_1^2=0,
$$
where $q$ collects the quadratic terms (from $f'(\rho_0)$, $g''(\rho_0)$ and the derivatives of $\mu$ and $\kappa$). With $\alpha_0<0$ and $\nu\mu_0>0$, the rescaling $\tilde\nabla^2=\nabla^{*2}/(\nu\mu_0)$, $\partial_{\tilde t}=\partial_{t^*}/(-\alpha_0\nu\mu_0)$, $a_1=a^*/q$ gives (dropping stars)

$$
a_t+r\Delta a+\Delta^2a+\Delta(a^2)=0 .
\tag{13.2}
$$
Its linear part gives $\sigma=rk^2-k^4$: long-wave instability for $r>0$, as in Theorem 13.4.1. The same equation arises locally in a general chemotaxis-augmented Turing system.

### 13.6.2. Periodic Steady States and a Subcritical Bifurcation

In one dimension, seek steady solutions of (13.2) with period 1 and $a_x=a_{xxx}=0$ at $x=0,1$. Integrating twice, $a_{xx}+ra+a^2=C$, and multiplying by $a_x$ and integrating again,

$$
a_x^2=-\tfrac23a^3-ra^2+2Ca+D .
$$
Shifting $a=A+h$ to put the middle root of the cubic at the origin, $A_x^2=\frac23(A+A_1)A(A_0-A)$ with $A_0,A_1>0$ and $0\le A\le A_0$. Conservation of cells requires the mean of $a$ to vanish, so $h=-\bar A$, and comparing the sum of the roots, $r=2\bar A+\frac23(A_1-A_0)$.

**Proposition 13.6.1** The periodic steady states are

$$
A=A_0\frac{(1-m)\,\operatorname{sn}^2(\xi,m)}{1-m\operatorname{sn}^2(\xi,m)},\qquad m=\frac{A_0}{A_0+A_1},\qquad\xi=x\sqrt{\frac{A_0}{6m}},
$$
where $\operatorname{sn}$ is the Jacobi elliptic function with parameter $m=k^2$ and the integral $\pm\sqrt{3/2}\,x=\int_0^A[s(A_0-s)(s+A_1)]^{-1/2}\mathrm{d}s$ has been inverted. Period 1 requires $A_0=24K^2m$, and then

$$
r=48K\Big(E+\frac m3K-\frac23K\Big),
$$
with $K(m)$, $E(m)$ the complete elliptic integrals of the first and second kind.

As $m\to0$, $K,E\to\pi/2$ and $r\to48\cdot\frac\pi2\cdot\frac\pi6=4\pi^2$, the linear threshold for the period-1 mode ($rk^2=k^4$ at $k=2\pi$). As $m$ grows, the amplitude $A_0$ grows but $r$ decreases: steady patterns exist for $r<4\pi^2$, where the uniform state is linearly stable. The **bifurcation** is subcritical, in part because it branches from infinite wavelength. These patterns are expected to be unstable, and they mark a threshold: when the uniform state is only just stable, a perturbation of finite amplitude can still trigger aggregation. The theory does not say where the system goes then, only that it ends far from uniformity.

### 13.6.3. Solitary Aggregates and Collapse

To follow the branch further, take the simplest nonlinear system (constant coefficients, $\alpha$ normalized to $-1$):

$$
fa-\rho+\nu\rho_{xx}=0,\qquad\mu a_{xx}-\kappa(a\rho_x)_x=0 .
$$
For stationary patterns with no cell flux at the boundary, the flux vanishes everywhere: $a_x=\lambda a\rho_x$ with $\lambda=\kappa/\mu$, so $a=\frac{A\lambda}{2f}\mathrm{e}^{\lambda\rho}$. Substituting and integrating once,

$$
\nu\rho_x^2+V(\rho)=E,\qquad V(\rho)=A\mathrm{e}^{\lambda\rho}-\rho^2 .
$$
Near the subcritical bifurcation the pattern oscillates in a shallow well of $V$. A highly nonlinear case is the solitary bump, a homoclinic orbit leaving and returning to a background $\rho_1$: a double root of $E-V$ at $\rho_1$ requires $E=-\rho_1^2+A\mathrm{e}^{\lambda\rho_1}$ and $2\rho_1=\lambda A\mathrm{e}^{\lambda\rho_1}$, hence $A=\frac{2\rho_1}\lambda\mathrm{e}^{-\lambda\rho_1}$, $E=-\rho_1^2+\frac{2\rho_1}\lambda$, and far away $a=a_1=\rho_1/f$. With $\rho_1=1$, the peak $\rho_2$ satisfies

$$
\rho_2^2-\frac2\lambda\mathrm{e}^{\lambda(\rho_2-1)}=1-\frac2\lambda .
$$
At $\lambda=1$ the only solution is $\rho_2=1$ (no bump); $\rho_2$ increases as $\lambda$ decreases, and as $\lambda\to0$, $\mathrm{e}^{\lambda\rho_2}\approx\lambda\rho_2^2/2$ gives $\rho_2\sim\lvert\ln\lambda\rvert/\lambda$ and a peak density

$$
a_2=\frac1f\mathrm{e}^{\lambda(\rho_2-1)}\sim\frac{(\ln\lambda)^2}{2\lambda f}
$$
to leading order. If these solutions are unstable, as seems likely, an isolated cluster supplied by the surrounding cells grows and contracts without limit: the time-dependent singular solutions envisaged by Nanjundiah (1973). For radially symmetric clusters a further instability makes the angular distribution of cells uneven, which may be related to the thin streams that converge on centres late in aggregation.

With fully periodic solutions the number of cells available to each centre is finite. With $\rho_0=1$, periodic solutions of infinitesimal amplitude appear when $-V''(1)=2(1-\lambda)<0$, so they branch from the uniform state for $\lambda>1$ with wavelength

$$
L_0=\int\frac{\mathrm{d}\rho}{\sqrt{(E-(\lambda-1)(\rho-1)^2)/\nu}}\Big|_{\text{one period}}=\frac{\pi}{\sqrt{\lambda-1}}\quad(\nu=1),
$$
and a branch is fixed by this wavelength and the number of cells per territory, $L_0a_0=L_0/f$. A second, stable branch of steady solutions may exist, which would make aggregation with a finite territory size a finite-amplitude transition through the unstable branch to a stable cluster; this has not been shown for this model. Some evidence comes from an asymptotic solution for large $\lambda$. Write $\frac{A\lambda}{2f}=\lambda B\mathrm{e}^{-\lambda\rho_m}$ with $\rho_m$ the maximum of $\rho$, at $x=\pm L_0/2$. Away from the maxima chemotaxis can be neglected, and $\rho^*(x)=\dfrac{\cosh(x/\sqrt\nu)}{2f\sqrt\nu\sinh(L_0/2\sqrt\nu)}$, whose periodic extension has a corner at the maxima. In the boundary layer $\xi=(x-L_0/2)\lambda/\sqrt\nu$, $w=(\rho-\rho_m)\lambda$, the equation becomes $B\mathrm{e}^w+w_{\xi\xi}=0$ as $\lambda\to\infty$, with $w_\xi=0$ at $\xi=0$, so $B\mathrm{e}^w+\frac12w_\xi^2=B$ and

$$
w=\ln\operatorname{sech}^2\Big(\sqrt{\tfrac B2}\,\xi\Big),\qquad B=\frac1{8f^2\nu},\qquad a=\lambda B\operatorname{sech}^2\Big(\sqrt{\tfrac B2}\,\xi\Big)
$$
(check: $w_{\xi\xi}=-B\operatorname{sech}^2$ and $B\mathrm{e}^w=B\operatorname{sech}^2$). The composite approximation is $\rho=\frac1\lambda\big[w\big(\frac\lambda{\sqrt\nu}(x-\frac{L_0}2)\big)+w\big(\frac\lambda{\sqrt\nu}(x+\frac{L_0}2)\big)\big]+\rho^*(x)$. The cell density is exponentially small except near the aggregation points.

![Nonlinear steady states. A: periodic solutions of the amplitude equation leave the uniform state at r = 4 pi^2 and bend back to smaller r as their amplitude grows, a subcritical bifurcation; inset: profiles for elliptic parameters 0.5 and 0.99. B: peak cell density of the solitary aggregate against lambda = kappa / mu, growing without bound as lambda decreases (dashed: leading-order asymptote). C: the boundary-layer aggregate for large lambda is a sech^2 cluster whose height grows with lambda](./plots/ks-nonlinear.py)

## 13.7. Collapse Depends on Dimension

Following Nanjundiah's conjecture that aggregates collapse into delta functions, Childress and Percus (1981) showed that the answer depends on the dimension of space. In one dimension the constant-coefficient Keller–Segel model cannot form a singularity. In two dimensions a critical number of cells must be gathered before a delta function forms in finite time. In three or more dimensions self-similar collapsing aggregates of any size exist.

**Definition 13.7.1 (Chemotactic Collapse)** **Chemotactic collapse** is the formation, in finite time, of a singularity in the cell density of a chemotaxis model, a concentration of a finite number of cells at a point.

The two-dimensional threshold can be made precise for the parabolic–elliptic simplification $a_t=\mu\Delta a-\kappa\nabla\cdot(a\nabla\rho)$, $-\Delta\rho=a$ in $\mathbb{R}^2$, in which the attractant diffuses fast and is not degraded.

**Theorem 13.7.1 (Critical Mass)** Let $M=\int a\,\mathrm{d}\boldsymbol{x}$ be the total number of cells. For a smooth solution with finite second moment,

$$
\frac{\mathrm{d}}{\mathrm{d}t}\int\lvert\boldsymbol{x}\rvert^2a\,\mathrm{d}\boldsymbol{x}=4\mu M\Big(1-\frac{\kappa M}{8\pi\mu}\Big).
$$
Hence if $M>8\pi\mu/\kappa$ the solution cannot exist for all time: the cells collapse in finite time.

**Proof** Integrating by parts, $\frac{\mathrm{d}}{\mathrm{d}t}\int\lvert\boldsymbol{x}\rvert^2a=\mu\int a\,\Delta\lvert\boldsymbol{x}\rvert^2+\kappa\int a\,\nabla\lvert\boldsymbol{x}\rvert^2\cdot\nabla\rho=4\mu M+2\kappa\int a\,\boldsymbol{x}\cdot\nabla\rho$. With $\rho=-\frac1{2\pi}\ln\lvert\cdot\rvert*a$, $\nabla\rho(\boldsymbol{x})=-\frac1{2\pi}\int\frac{\boldsymbol{x}-\boldsymbol{y}}{\lvert\boldsymbol{x}-\boldsymbol{y}\rvert^2}a(\boldsymbol{y})\,\mathrm{d}\boldsymbol{y}$, and symmetrizing in $\boldsymbol{x}$ and $\boldsymbol{y}$,

$$
\int a\,\boldsymbol{x}\cdot\nabla\rho=-\frac1{4\pi}\iint a(\boldsymbol{x})a(\boldsymbol{y})\frac{(\boldsymbol{x}-\boldsymbol{y})\cdot(\boldsymbol{x}-\boldsymbol{y})}{\lvert\boldsymbol{x}-\boldsymbol{y}\rvert^2}=-\frac{M^2}{4\pi}.
$$
So the second moment changes at the constant rate $4\mu M-\kappa M^2/2\pi$. If this is negative, the nonnegative second moment would become negative in finite time, which is impossible for a smooth solution. $\square$

Below the critical mass solutions exist globally (Jäger and Luckhaus, 1992; Blanchet, Dolbeault and Perthame, 2006), so $8\pi\mu/\kappa$ is sharp. Real cells cannot be compressed indefinitely: if the chemotactic flux is reduced as space fills, $\kappa\to\kappa(1-a/a_{\max})$, collapse is prevented and aggregates become plateaus of bounded density that coarsen slowly (Painter and Hillen, 2002), in the same spirit as the volume-exclusion terms in models of adhesion-driven movement ([7.5.7](/7.5.7)).

![Two-dimensional aggregation in the Keller-Segel model with volume filling, from a nearly uniform field of cells: small clusters appear (t = 6), grow by drawing cells from their surroundings (t = 15) and become a few aggregates whose density saturates at the packing limit (t = 40)](./plots/ks-aggregation-2d.py)

## 13.8. Chemotaxis in Animal Embryos

Chemotaxis was once proposed as a mechanism of vertebrate **gastrulation** by analogy with slime moulds. It is now known to guide many embryonic migrations, though rarely alone.

| Migration | Attractant and receptor | Notes | Chapter |
|---|---|---|---|
| Primordial germ cells (zebrafish, mouse, fly) | SDF-1 (CXCL12) and CXCR4 | cells follow a moving stripe of SDF-1 to the gonad; in the fly, lipid signals from the gonad | [7.5.27](/7.5.27) |
| Mesoderm in the chick primitive streak | FGF8 (repulsion) and FGF4 (attraction) | cells leaving the streak are pushed and pulled | [7.5.9](/7.5.9) |
| Neural crest | SDF-1, complement C3a (co-attraction) | combined with contact inhibition of locomotion | [7.5.20](/7.5.20) |
| Lateral line primordium (zebrafish) | SDF-1 and CXCR4, with the scavenger receptor CXCR7 at the rear | the cells create their own gradient by removing the attractant | [7.5.20](/7.5.20) |
| Axons | netrin, Slit, semaphorins (growth cone guidance) | attraction and repulsion of a part of a cell | [7.5.21](/7.5.21) |

The lateral line primordium recalls the degradation term $g(\rho)$ of the Keller–Segel model: a group of cells that both responds to and destroys an attractant spread uniformly in the tissue makes a gradient across itself and migrates up it, a self-generated gradient that needs no localized source. *Dictyostelium* cells do the same with folate and cAMP in dense populations.

## Summary

| Topic | Key results |
|---|---|
| Organism | Social amoeba (Amoebozoa, not a fungus); starvation → cAMP signaling → aggregation of ≈ $10^5$ cells → slug (prestalk front, prespore rear) → fruiting body |
| Proportions | Prespore/prestalk $=KV^\lambda$, $\lambda\approx0.2$; current mechanism: biased random choice, sorting out, DIF-1 feedback; reaction-diffusion model with a constant transition layer reproduces the allometry; regulation after truncation takes $\sim(\ell-x_s)^2/\nu$ |
| Relay | Definition 13.3.1; pulse seen by a neighbour $(sa/4)\mathrm{e}^{-1/\tau}/\tau$; critical density $a_c=4\mathrm{e}\rho_c/s$; speed $R/(T_p+T_d)\approx R/T_d$ (Formula 13.3.1); continuum limit $a_t+Q(a)_x=0$ with $Q=-a\Delta(a)/T$; target and spiral waves of an excitable medium |
| Keller–Segel | Definition 13.4.1; real growth rates; instability iff $\mu_0\alpha_0+\kappa_0f_0>0$; marginal mode $k=0$, $k^2_{\max}=\Delta/2\mu_0\nu_0$, $\sigma_{\max}=\Delta^2/4\lvert\alpha_0\rvert\mu_0\nu_0$ (Theorem 13.4.1); territory-size problem |
| Augmented Turing | $R=\alpha+f\kappa^{\mathsf T}/\mu$ replaces $\alpha$; chemotaxis can create a finite wavelength with two chemicals (Example 13.5.1) |
| Nonlinear | Amplitude equation (13.2); elliptic-function steady states, $r=48K(E+mK/3-2K/3)$, $A_0=24K^2m$, subcritical (Proposition 13.6.1); solitary aggregates with $a_2\sim(\ln\lambda)^2/2\lambda f$; sech² clusters for large $\lambda$ |
| Collapse | Definition 13.7.1; none in 1D, critical mass $8\pi\mu/\kappa$ in 2D (Theorem 13.7.1), any mass in 3D; volume filling prevents collapse |
| Embryos | SDF-1/CXCR4 for germ cells and neural crest, FGF in the streak, self-generated gradients |

## Questions

1. Why is *Dictyostelium* studied in developmental biology although it is not an animal, and why is it not a fungus?

   **Answer** It solves developmental problems in a simple form: multicellularity, cell-type proportioning and regulation after cutting, sorting out, morphogenetic movement and signal relay, with a known signal (cAMP) and counted cells; and because its cells come together from different lineages, patterning cannot be inherited from an egg. Molecular phylogeny places it in the Amoebozoa, with amoeboid protists, not with the fungi (which belong to the Opisthokonta together with animals); its walled spores and fruiting body are convergent with those of fungi.

2. In the Cohen–Robertson model, show that the trigger time $\tau_p$ tends to $1$ as the density approaches $a_c$ from above, and to $0$ as $a\to\infty$. What happens to wave speed, and is this realistic?

   **Answer** The trigger condition is $g(\tau_p)=a_c/(\mathrm{e}a)$. As $a\to a_c^+$ the right side approaches the maximum $1/\mathrm{e}$ of $g$, reached at $\tau=1$, so $\tau_p\to1$. As $a\to\infty$ the right side tends to zero, and the smaller root of $\mathrm{e}^{-1/\tau}/\tau=\varepsilon$ tends to zero (roughly $\tau_p\approx1/\ln(1/\varepsilon)$). The speed $R/(R^2\tau_p/4\nu+T_d)$ approaches $R/T_d$, which decreases as $a^{-1/2}$. In real cells the relay delay and excitability change with density and with development, so speeds do not follow this simple rule; the model's lesson is that relay waves are delay-limited, not diffusion-limited.

3. Estimate the time for a cAMP pulse to diffuse between neighbouring amoebae ($R=40\,\mathrm{\mu m}$, $\nu=400\,\mathrm{\mu m^2\,s^{-1}}$) and over a territory of $5\,\mathrm{mm}$. What does this imply for long-range signaling?

   **Answer** $R^2/4\nu=1600/1600=1\,\mathrm{s}$ between neighbours; $(5000)^2/(4\times400)\approx1.6\times10^4\,\mathrm{s}\approx4.3\,\mathrm{h}$ across the territory, and the pulse would be diluted to nothing. Diffusion alone cannot organize a territory within one period of 5 min; relay, in which each cell regenerates the signal, makes waves travel the territory in a few minutes, at the cost of a fixed delay per cell.

4. Verify the identity $A^2-4B=((\mu_0-\nu_0)k^2+\alpha_0)^2+4\kappa_0f_0k^2$ and explain biologically why the Keller–Segel instability is not oscillatory, whereas the cAMP signaling of real cells is.

   **Answer** Expanding as in the proof of Theorem 13.4.1. Since $\kappa_0f_0>0$ (cells move up gradients of an attractant they make), the discriminant is positive, so the roots are real. The model has no delayed negative feedback: attractant attracts cells, which make more attractant, a purely positive loop. Real cells adapt (receptor **desensitization** and adaptation of the cyclase) and become refractory, a delayed negative feedback that makes the signaling system excitable or oscillatory, which the averaged model leaves out.

5. With $\mu_0=\nu_0=1$, $\alpha_0=-1$ and $\Delta=0.1$, compute the fastest-growing wavelength and its growth rate. How does the wavelength change if $\Delta$ is doubled, and why is this a problem for explaining territory size?

   **Answer** $k^2_{\max}=\Delta/(2\mu_0\nu_0)=0.05$, $k_{\max}=0.224$, wavelength $2\pi/k_{\max}=28$; $\sigma_{\max}=\Delta^2/(4\lvert\alpha_0\rvert\mu_0\nu_0)=0.0025$. Doubling $\Delta$ gives $k^2_{\max}=0.1$ and wavelength $19.9$, smaller by $\sqrt2$. The wavelength depends on how far beyond threshold the system happens to be when aggregation starts, so territory size would vary with initial conditions; observed territories have a characteristic size, which points to the relay dynamics rather than the smooth instability.

6. Check Example 13.5.1: compute $R$ and the Turing quantities with and without chemotaxis. By what factor does the example clear the threshold?

   **Answer** $f\kappa^{\mathsf T}/\mu=\begin{bmatrix}1&0\\1&0\end{bmatrix}$, so $R=\begin{bmatrix}3&-3\\6&-5\end{bmatrix}$ with $\det R=-15+18=3$. Without chemotaxis: $\nu_1\alpha_{22}+\nu_2\alpha_{11}=-5+8=3$ versus $2\sqrt{4\cdot5}=8.94$ (stable). With chemotaxis: $-5+12=7$ versus $2\sqrt{4\cdot3}=6.93$: unstable by a margin of about 1 %. (Stated with $2\sqrt5$ and $2\sqrt3$ the thresholds would be too low by the factor $\sqrt{\nu_1\nu_2}=2$; the conclusion holds, barely.) A stronger response, $\kappa_1=1.5$, gives $R_{11}=3.5$, $R_{21}=6.5$, $\det R=2$, and $-5+14=9>2\sqrt8=5.66$, comfortably unstable.

7. Show that the periodic steady states of Proposition 13.6.1 have $r\to4\pi^2$ as their amplitude vanishes, and explain why the branch bending to smaller $r$ implies **hysteresis** in aggregation.

   **Answer** As $m\to0$, $K=E=\pi/2$ and $r=48\cdot\frac\pi2\big(\frac\pi2-\frac\pi3\big)=4\pi^2$, the point where the linear growth rate $rk^2-k^4$ of the mode $k=2\pi$ changes sign. For $r$ slightly below $4\pi^2$ the uniform state is stable but an unstable patterned state exists nearby; a perturbation larger than this state can push the system into a large-amplitude aggregated state. Once aggregated, lowering $r$ below threshold does not restore uniformity (the aggregated state persists), whereas raising $r$ above $4\pi^2$ destabilizes uniformity: the transition depends on the direction of change, a hysteresis typical of subcritical bifurcations.

8. Prove that in one dimension the solitary aggregate exists only for $\lambda<1$ and estimate its peak cell density at $\lambda=0.1$ from the leading-order formula and from the exact equation.

   **Answer** At $\lambda=1$ the background $\rho_1=1$ is a degenerate (triple) root and the bump has zero amplitude; for $\lambda>1$ the background is a minimum of $V$ ($V''(1)=2(\lambda-1)>0$), around which only periodic, not homoclinic, orbits exist. At $\lambda=0.1$, the leading-order formula gives $a_2\approx(\ln0.1)^2/(2\times0.1)=26.5$. The exact equation $\rho_2^2-20\mathrm{e}^{0.1(\rho_2-1)}=-19$ has the root $\rho_2\approx48.9$, so $a_2=\mathrm{e}^{0.1\times47.9}\approx121$: the asymptotic formula has the right trend but converges slowly, because the corrections are of order $\ln\lvert\ln\lambda\rvert$.

9. (Experimental design) How would you distinguish, in a slug, a reaction-diffusion prepattern that converts cells according to their position from sorting out of cells that chose their fates at random?

   **Answer** Label a subpopulation of cells before aggregation (for example by a fluorescent marker) and follow them. Under sorting out, cells that express prestalk markers first appear scattered throughout the mound and then move to the tip; labelled cells change position more than they change fate. Under a positional prepattern, cells would adopt fates according to where they are, and transplanted cells (or cells moved by cutting and rejoining slugs) would switch fate to match their new position without moving. Both happen: initial differentiation is salt-and-pepper with subsequent sorting, while after cutting, cells at the new boundary do convert, a regulative response that diffusible signals such as DIF-1 mediate.

10. Use Theorem 13.7.1 to compute the critical number of cells for collapse when $\mu=10\,\mathrm{\mu m^2\,min^{-1}}$ and $\kappa$ is such that $\kappa/\mu=10^{-3}\,\mathrm{\mu m^2}$ per cell (in the normalization $-\Delta\rho=a$). Why do real aggregates not collapse to a point?

    **Answer** $M_c=8\pi\mu/\kappa=8\pi\times10^3\approx2.5\times10^4$ cells. Real aggregates of $10^5$ cells exceed it, yet they do not collapse because cells have finite volume: the packing limit, cell–cell adhesion and the mechanics of the mound (modelled by volume filling, $\kappa(1-a/a_{\max})$) replace the singularity by a dense mound of bounded density, which then develops a tip and a slug.
