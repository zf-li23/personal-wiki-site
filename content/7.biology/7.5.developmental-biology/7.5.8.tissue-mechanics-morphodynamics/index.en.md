---
title: Tissue Mechanics and Morphodynamics
description: "Embryonic tissues as very viscous liquids: Maxwell viscoelasticity, adhesion-site membrane models of tissue rheology (sliding on a substrate as a Stefan problem, interstitial membranes and their effective elastic constant and viscosity), the continuum equations of morphodynamics, surface forces (Laplace and Marangoni), dimensional analysis and Stokes flow, dissipation and the energy balance for layered tissues with a volume potential, Rayleigh's dissipation principle, the stability of onion-like layering, surfactant instabilities and the mechanics of cleavage, cortical tension and actomyosin, and vertex models of the fluid–solid transition of tissues."
---

The sorting experiments of 7.5.7 showed that embryonic tissues behave like immiscible liquids: they round up, fuse and engulf one another as if driven by surface tension. This chapter takes the analogy literally and builds the mechanics that goes with it. We ask what kind of material a tissue is (a viscoelastic liquid with an enormous viscosity), how its viscosity and elasticity can arise from adhesive contacts between cells, what equations govern the slow flow of such a material when surface tensions act on its boundaries and internal interfaces, how fast such flows are (so slow that inertia plays no role at all), and what follows from the fact that the flow dissipates the surface energy that drives it. The same framework, applied to the surface of a single cell, gives a mechanical model of **cleavage**; the molecular source of the tensions is the actomyosin cortex; and at the scale of individual cells the current tools are vertex models, which also explain how tissues switch between fluid and solid behaviour. The mathematics used here (first-order linear equations, the heat equation, the Laplace transform, the divergence theorem, spherical harmonics) is taken from the mathematics courses and linked rather than re-derived; the applications to **gastrulation**, **epiboly** and **invagination** follow in 7.5.9.

## 8.1. Tissues as Viscoelastic Liquids

Several observations show that tissues flow. Irregular fragments of embryonic tissue round up into spheres; two spherical aggregates pressed together fuse into one, the neck between them widening as two liquid drops coalesce; an aggregate flattens under its own weight when centrifuged, and its equilibrium shape gives its surface tension (7.5.7). Fitting such deformations with the equations of viscous flow gives effective viscosities of about $10^5$–$10^7\,\mathrm{Pa\,s}$ ($10^6$–$10^8$ poise), comparable with pitch and some $10^5$ times the viscosity of glycerol (the **viscosity** of [5.2.2](/5.2.2)). But a tissue is not a simple liquid: compressed suddenly, it responds elastically, and only after minutes does the stress relax and the material flow. Elastic on short time scales, viscous on long ones: this is the behaviour of a Maxwell liquid.

**Definition 8.1.1 (Maxwell Viscoelastic Liquid)** A **Maxwell viscoelastic liquid** is a material whose shear stress $\tau$ and shear strain $\varepsilon$ obey

$$
\frac{\mathrm{d}\tau}{\mathrm{d}t} + \frac{\tau}{t_{\mathrm{r}}} = G\,\frac{\mathrm{d}\varepsilon}{\mathrm{d}t}, \qquad t_{\mathrm{r}} = \frac{\eta}{G},
\tag{8.1}
$$
where $G$ is a shear modulus, $\eta$ a viscosity and $t_{\mathrm{r}}$ the relaxation time. Its mechanical analogue is a massless spring of stiffness $G$ in series with a dashpot of viscosity $\eta$: the strain rates add, $\dot\varepsilon = \dot\tau/G + \tau/\eta$.

Eq. (8.1) is a first-order linear equation for $\tau$ ([2.2.15](/2.2.15)). Three standard experiments (Figure 1): after a step strain $\varepsilon_0$ the stress relaxes as $\tau = G\varepsilon_0\mathrm{e}^{-t/t_{\mathrm{r}}}$; under a step stress $\tau_0$ the strain jumps to $\tau_0/G$ and then grows linearly, $\varepsilon = \tau_0/G + \tau_0t/\eta$ (creep); and in a Couette layer, between two walls of which one starts to move at constant speed, the shear rate $\dot\varepsilon = \mathrm{d}u/\mathrm{d}y$ is uniform in the absence of inertia and

$$
\tau = \eta\,\frac{\mathrm{d}u}{\mathrm{d}y}\bigl(1 - \mathrm{e}^{-t/t_{\mathrm{r}}}\bigr).
$$
For $t \gg t_{\mathrm{r}}$ this is the Newtonian law $\tau = \eta\,\mathrm{d}u/\mathrm{d}y$; for $t \ll t_{\mathrm{r}}$, $\tau \approx \eta\dot\varepsilon\,t/t_{\mathrm{r}} = G\varepsilon$, Hooke's law. Morphogenetic movements last hours, much longer than the relaxation times of minutes, which is why the liquid analogy works for them.

![The Maxwell viscoelastic liquid (Definition 8.1.1). A: mechanical analogue, a spring of shear modulus G in series with a dashpot of viscosity η, with relaxation time t_r = η/G. B: stress relaxation after a step strain, τ = Gε0 exp(−t/t_r). C: creep under a step stress: an elastic jump τ0/G followed by viscous flow at rate τ0/η. D: start-up of shear at constant rate: the stress grows as η(dε/dt)(1 − exp(−t/t_r)), elastic (τ ≈ Gε, dashed) for t ≪ t_r and Newtonian for t ≫ t_r](./plots/maxwell.py)

Where do the elasticity and the viscosity come from? A natural view is that the high viscosity reflects the adhesive contacts that cells must slide, break and remake when the tissue flows, and that the short-time elasticity reflects the stretching of cell membranes and cortices. The next section makes this concrete with a model in which adhesion is concentrated in discrete sites, so that site density measures both membrane extension and local adhesive energy.

## 8.2. An Adhesion-Site Model of Tissue Rheology

Work in two dimensions (rows of cells along the ignorable direction of a Couette layer act as two-dimensional cells). Along a membrane with arc length $s$, let $n(s, t)$ be the number density of adhesion sites, $u(s, t)$ their tangential velocity and $T(s, t)$ the membrane tension. Conservation of sites on a segment $(s, s + \Delta s)$ gives

$$
\frac{\partial n}{\partial t} + \frac{\partial(un)}{\partial s} = q,
$$
with $q$ a source of sites (zero below; it would describe sites inserted from inside the cell). Sites are integral parts of an extensible membrane, so the tension is a function of their density, $T = g(n, t)$, decreasing in $n$ (a stretched membrane has sparser sites and higher tension); the explicit time dependence could describe hardening or softening of adhesion with age. The model is closed by a law for the friction that sites experience, $\partial T/\partial s = F(u, n, t)$.

### 8.2.1. Sliding on a Substrate

Pull a membrane segment of initial length $L_0$ and site density $n_0$ along a flat substrate by applying at its right end, from $t = 0$, the tension corresponding to a density $n_1 < n_0$; the left end is free, $g(n_0) = 0$. If sites respond independently to the substrate, the friction is $n$ times a function of the site velocity. In the linearized model

$$
T = -k(n - n_0), \qquad \frac{\partial T}{\partial s} = n\,n_{\mathrm{s}}fu,
$$
with $k$ an elastic constant, $f$ a friction factor and $n_{\mathrm{s}}$ the density of binding sites on the substrate. Then $nu = -K\,\partial n/\partial s$ with $K = k/(n_{\mathrm{s}}f)$, and conservation of sites gives the heat equation

$$
\frac{\partial n}{\partial t} = K\frac{\partial^2n}{\partial s^2}, \qquad s_0(t) < s < s_1(t),
$$
on a segment whose ends $s_0(t), s_1(t)$ move with the sites: $-K\,\partial n/\partial s = \dot s_0n_0$, $n = n_0$ at $s = s_0$, and $-K\,\partial n/\partial s = \dot s_1n_1$, $n = n_1$ at $s = s_1$. This is a moving-boundary problem for the **heat equation** ([2.5.7](/2.5.7)) of Stefan type. In the variables $s/L_0$, $tK/L_0^2$, $n/n_0$ the only parameter left is $n_1/n_0$: the segment relaxes to steady sliding on the time scale $L_0^2/K$.

**Proposition 8.2.1 (Steady Sliding)** At long times all sites move with a common speed $U$, the density profile is $n = n_0\mathrm{e}^{-Us'/K}$ in the frame moving with the trailing end ($s' = s - s_0(t)$), and

$$
U = \frac{K}{L_0}\Bigl(1 - \frac{n_1}{n_0}\Bigr), \qquad L = L_0\,\frac{\ln(n_0/n_1)}{1 - n_1/n_0}.
$$

**Proof** With $u = U$, $nu = -Kn'$ gives $n' = -(U/K)n$, $n = n_0\mathrm{e}^{-Us'/K}$, and $n(L) = n_1$ gives $UL/K = \ln(n_0/n_1)$. Sites are conserved, $n_0L_0 = \int_0^Ln\,\mathrm{d}s' = (n_0K/U)(1 - n_1/n_0)$, which gives $U$; then $L = (K/U)\ln(n_0/n_1)$. $\square$

No elementary solution of the transient problem exists. At small times, near the pulled end, the solution is the error-function profile of a suddenly changed boundary value, $n \approx n_0 + 2(n_1 - n_0)\pi^{-1/2}\int_{-\infty}^{(s - s_1)/2\sqrt{Kt}}\mathrm{e}^{-z^2}\mathrm{d}z$, so the leading end moves as $s_1 - L_0 = O(\sqrt t)$, while the trailing end starts with zero gradient and does not move at first. The problem becomes simple in a Lagrangian coordinate that labels sites (Figure 2). The behaviour is not quite that of a Maxwell element: when a force is applied suddenly to a spring and dashpot in series, the spring stretches at once and the dashpot starts moving at once, whereas here the extension diffuses in from the pulled end.

![An adhesion-site membrane pulled along a substrate (8.2.1): linear site model with n_1 = n_0/2 applied at the right end at t = 0, solved in a Lagrangian coordinate (number of sites to the left), in which the moving ends become fixed. A: site density against position at t = 0.02, 0.1, 0.3, 1 and 4 (units L0²/K): the stretch diffuses in from the pulled end while the whole segment starts to slide. B: segment length and trailing-end speed approach the steady sliding values L = 1.386 L0 and U = 0.5 K/L0 of Proposition 8.2.1 (dashed) on the time scale L0²/K](./plots/membrane-sliding.py)

### 8.2.2. Interstitial Membranes

A model closer to tissue rheology considers a Couette layer filled with cells, which can be pictured as sticky elastic bags of viscous fluid rolling over each other in horizontal laminae. Because neighbouring laminae move at different speeds, the membranes of adjacent cells slide past each other in their regions of contact. Model one contact region as two membranes pressed together over $\lvert s\rvert < L(t)/2$, symmetric under $s \to -s$, with relative motion driven by enhanced tensions $T_1 = T_0 + k(n_0 - n)$ at diagonally opposite edges. Let $n, u$ refer to the lower membrane. If the site densities of both membranes create friction independently (as in Steinberg's sparse-site rule of 7.5.7) and linearly in the relative velocity,

$$
-k\frac{\partial n}{\partial s} = f\,n(s, t)\,n(-s, t)\bigl[u(s, t) + u(-s, t)\bigr].
$$
The right-hand side is even in $s$, so $\partial n/\partial s$ is even and $n(s, t) + n(-s, t)$ does not depend on $s$; evaluated at the edges it equals $n_0 + n_1(t)$, where $n_1$ is the density at the stretched edge. Counting both membranes, sites are conserved: $(n_0 + n_1)L(t) = 2n_0L_0$, so the contact length is known explicitly, $L(t) = 2n_0L_0/(n_0 + n_1(t))$.

For constant $n_1$ the steady state has $un = u_0n_0 = u_1n_1$ (with $u_0, u_1$ the edge velocities), so $-k\,\partial n/\partial s = f(n_0 + n_1)n_0u_0$ is constant, the profile is linear, and

$$
u_0 = \frac{K}{2L_0}\Bigl(1 - \frac{n_1}{n_0}\Bigr), \qquad u_1 = \frac{n_0u_0}{n_1}, \qquad K = \frac{k}{fn_0}.
$$
For the transients, conservation and symmetry give $u(-s)n(-s) = u(s)n(s) + s\dot n_1$, and eliminating $u$,

$$
f(n_0 + n_1)\frac{\partial n}{\partial t} - k\frac{\partial^2n}{\partial s^2} = f\dot n_1\frac{\partial(sn)}{\partial s}.
$$
For small deviations, $n = n_0(1 - g)$ and $n_1 = n_0(1 - \nu)$ with $\lvert g\rvert, \lvert\nu\rvert \ll 1$, this becomes

$$
2\frac{\partial g}{\partial t} - K\frac{\partial^2g}{\partial s^2} - \dot\nu = 0, \qquad g\Bigl(\frac{L_0}{2}, t\Bigr) = \nu, \quad g\Bigl(-\frac{L_0}{2}, t\Bigr) = 0.
\tag{8.2}
$$

**Theorem 8.2.2 (Effective Maxwell Constants)** Let $\nu$ and $g$ vanish at $t = 0$, and define the shear stress by $\tau = kn_0\nu/L_0$ and the shear rate as the edge velocities plus the elastic extension, $\dot\varepsilon = (u_0 + u_1)/L_0 + \dot\nu/2$. Then the Laplace transforms ([2.5.6](/2.5.6)) satisfy

$$
\frac{\hat\varepsilon}{\hat\tau} = \frac{L_0\sigma}{2kn_0} + \frac{1}{2n_0^2f}\sqrt{\frac{2\sigma}{K}}\coth\Bigl(\sqrt{\frac{\sigma L_0^2}{2K}}\Bigr)
= \frac{1}{L_0n_0^2f} + \frac{2L_0}{3kn_0}\,\sigma + O(\sigma^2),
$$
so at long times (small $\sigma$) the contact behaves as a Maxwell liquid, $\hat\varepsilon/\hat\tau = \sigma/k_{\mathrm{eff}} + 1/\eta_{\mathrm{eff}}$, with

$$
k_{\mathrm{eff}} = \frac{3kn_0}{2L_0}, \qquad \eta_{\mathrm{eff}} = L_0n_0^2f, \qquad t_{\mathrm{r}} = \frac{\eta_{\mathrm{eff}}}{k_{\mathrm{eff}}} = \frac{2L_0^2}{3K}.
$$

**Proof** Transforming Eq. (8.2) with zero initial data, $2\sigma\hat g - K\hat g'' = \sigma\hat\nu$. A particular solution is $\hat\nu/2$; adding $A\sinh\lambda s + B\cosh\lambda s$ with $\lambda = \sqrt{2\sigma/K}$ and imposing the boundary conditions gives $B = 0$ and

$$
\hat g = \frac{\hat\nu}{2}\Bigl[1 + \frac{\sinh\lambda s}{\sinh(\lambda L_0/2)}\Bigr].
$$
Linearizing the friction law, $kn_0\,\partial_sg = fn_0^2\bigl[u(s) + u(-s)\bigr]$, so at the edges $u_0 + u_1 = K\,\partial_sg(L_0/2) = \frac K2\bigl[\partial_sg(L_0/2) + \partial_sg(-L_0/2)\bigr]$, and in transformed form $\hat u_0 + \hat u_1 = \frac K2\hat\nu\lambda\coth(\lambda L_0/2)$. Hence $\hat\varepsilon = \frac{K\lambda}{2L_0}\coth(\lambda L_0/2)\hat\nu + \frac\sigma2\hat\nu$, and dividing by $\hat\tau = kn_0\hat\nu/L_0$ (with $K = k/fn_0$) gives the first expression. Expanding $\coth z = 1/z + z/3 + O(z^3)$ with $z = \lambda L_0/2$: $\lambda\coth z = 2/L_0 + \lambda^2L_0/6 + \dots = 2/L_0 + \sigma L_0/(3K) + \dots$, which gives the constant term $1/(L_0n_0^2f)$ and the coefficient $L_0/(2kn_0) + L_0/(6kn_0) = 2L_0/(3kn_0)$ of $\sigma$. $\square$

The model therefore predicts Newtonian viscous behaviour of aggregates for movements slower than $t_{\mathrm{r}} \sim L_0^2/K$, with a viscosity set by the friction of adhesion sites. It is more than a Maxwell element: at large $\sigma$ (short times) the compliance tends to $L_0/(2kn_0)$, stiffer than $1/k_{\mathrm{eff}}$, because the diffusion of stretch along the contact introduces a whole spectrum of relaxation times (Figure 3). Measured aggregate viscosities ($10^5$–$10^7\,\mathrm{Pa\,s}$) fix $\eta_{\mathrm{eff}}$, and $k_{\mathrm{eff}}$ could be measured from the elastic response; what the model cannot do is relate $k$ and $f$ to the adhesive energy that sets the surface tension. A stochastic version allowing correlations between sites is a natural extension.

![Creep of the interstitial-membrane model (8.2.2). A: two cell membranes in contact over a length L(t), sliding past each other; adhesion sites near the leading edges are stretched, and friction is proportional to the product of the site densities on the two membranes and to their relative velocity. B: creep compliance after a step stress, computed exactly from Eq. (8.2) by a Fourier series (solid), and the Maxwell approximation 1/k_eff + t/η_eff of Theorem 8.2.2 (dashed): the two agree for t ≫ L0²/K, while at short times the exact compliance tends to the smaller value L0/(2kn0) (dotted)](./plots/interstitial-membrane.py)

## 8.3. Continuum Equations of Morphodynamics

On scales much larger than cells, and on times longer than $t_{\mathrm{r}}$, the tissue can be treated as a Newtonian viscous liquid. This is a crude approximation: cells are not isotropic (a cell with a polarity axis makes the material locally anisotropic, more like a liquid crystal, so that "cell state" should in general be a tensor), and they are active. But it is the right first step.

**Definition 8.3.1 (Morphodynamics)** *Morphodynamics* is the description of morphogenetic movements by the equations of continuum mechanics: conservation laws for the mass and the momentum of the tissue, a constitutive law relating stress to deformation, and boundary conditions expressing the forces exerted by surface and interfacial tensions.

There are two descriptions of a moving continuum. The Eulerian one gives fields at fixed points of space, such as the density $\rho(\boldsymbol{x}, t)$ and velocity $\boldsymbol{u}(\boldsymbol{x}, t)$; the Lagrangian one follows each particle, $\boldsymbol{x} = \boldsymbol{X}(\boldsymbol{b}, t)$ with $\boldsymbol{X}(\boldsymbol{b}, 0) = \boldsymbol{b}$ (summation over repeated indices below).

Mass. For a fixed small volume $V'$ inside the tissue with outward normal $\boldsymbol{n}$, and a rate $q$ at which matter is created by growth (density per time), $\frac{\mathrm{d}}{\mathrm{d}t}\int\rho\,\mathrm{d}V' = -\oint\rho u_in_i\,\mathrm{d}S' + \int q\,\mathrm{d}V'$. By the **divergence theorem** ([2.2.14](/2.2.14)) and the arbitrariness of $V'$,

$$
\frac{\partial\rho}{\partial t} + \frac{\partial(\rho u_i)}{\partial x_i} = q,
\tag{8.3}
$$
the **continuity equation**. With the material derivative $\frac{\mathrm{d}}{\mathrm{d}t} = \frac{\partial}{\partial t} + u_j\frac{\partial}{\partial x_j}$, the rate of change following a particle, Eq. (8.3) reads $\mathrm{d}\rho/\mathrm{d}t + \rho\,\partial_iu_i = q$. "Incompressible" ($\partial_iu_i = q/\rho$) does not mean that $\rho$ is constant: it means $\mathrm{d}\rho/\mathrm{d}t = 0$, density constant along each particle path but possibly different between particles (cell types of different density). Without sources, incompressibility is $\partial_iu_i = 0$ in Eulerian form and $\det(\partial X_i/\partial b_j) = 1$ in Lagrangian form: the flow map preserves volume.

Momentum. The acceleration of a particle is $a_i = \ddot X_i = \partial_tu_i + u_j\partial_ju_i = \mathrm{d}u_i/\mathrm{d}t$, and Newton's law is $\rho a_i = \partial_j\sigma_{ij} + f_i$, with $\sigma_{ij}$ the stress tensor ($\sigma_{ij}n_j$ is the force per area exerted across a surface element of normal $\boldsymbol{n}$ by the material on the side into which $\boldsymbol{n}$ points) and $f_i$ a body force. For a Newtonian liquid of viscosity $\eta$ with traceless viscous stress,

$$
\sigma_{ij} = -p\,\delta_{ij} + \eta\Bigl(\frac{\partial u_i}{\partial x_j} + \frac{\partial u_j}{\partial x_i} - \frac23\frac{\partial u_k}{\partial x_k}\delta_{ij}\Bigr),
$$
with $p$ the pressure: viscous stress is generated by velocity gradients, as elastic stress is by displacement gradients. Inserting it,

$$
\rho\Bigl(\frac{\partial u_i}{\partial t} + u_j\frac{\partial u_i}{\partial x_j}\Bigr) + \frac{\partial p}{\partial x_i} - \eta\nabla^2u_i = f_i + \frac{\eta}{3\rho}\frac{\partial q}{\partial x_i},
\tag{8.4}
$$
the Navier–Stokes equations with a growth term; the Laplacian term describes diffusion of momentum with diffusivity $\eta/\rho$ (the kinematic viscosity). For a Maxwell liquid the viscous stress $\tau_{ij}$ obeys $t_{\mathrm{r}}\,\mathrm{d}\tau_{ij}/\mathrm{d}t + \tau_{ij} = \eta(\partial_ju_i + \partial_iu_j - \frac23\partial_ku_k\delta_{ij})$; for large deformations the material derivative must be replaced by a frame-invariant (upper-convected) one, a refinement not needed for the slow flows below.

## 8.4. Surface Forces

Let the tissue occupy a region $V$ bounded by a smooth surface $S$ with outward normal $\boldsymbol{n}$, and let a surface tension $\gamma(\boldsymbol{x}, t)$ act on $S$, the outside exerting no stress.

**Theorem 8.4.1 (Surface Force)** The traction exerted on the tissue at its surface is

$$
f_i^{\mathrm{s}} = \sigma_{ij}n_j = -\gamma\Bigl(\frac1{R_1} + \frac1{R_2}\Bigr)n_i + \Bigl(\frac{\partial\gamma}{\partial x_i} - n_in_j\frac{\partial\gamma}{\partial x_j}\Bigr),
$$
where $R_1, R_2$ are the principal radii of curvature (positive for a convex surface). The normal part is the Laplace pressure of the **Young–Laplace equation** ([Theorem 19.2.1](/6.3.19#thm-19.2.1)); the tangential part is the gradient of $\gamma$ within the surface, which pulls the surface towards regions of higher tension (the Marangoni force).

**Proof** Normal part: displace $S$ along its normal by $\delta\zeta(\boldsymbol{x})$. An area element $\mathrm{d}\xi_1\mathrm{d}\xi_2$ along the principal directions becomes $\mathrm{d}\xi_1(1 + \delta\zeta/R_1)\,\mathrm{d}\xi_2(1 + \delta\zeta/R_2)$, so $\delta(\mathrm{d}S) \approx (1/R_1 + 1/R_2)\delta\zeta\,\mathrm{d}S$. The virtual work of the stress and the surface energy change must balance: $\int\delta\zeta\bigl[\sigma_{ij}n_in_j + \gamma(1/R_1 + 1/R_2)\bigr]\mathrm{d}S = 0$ for all $\delta\zeta$, so $\sigma_{ij}n_in_j = -\gamma(1/R_1 + 1/R_2)$. Tangential part: on a small, nearly planar patch $S'$ bounded by a curve $C'$, the tension pulls on the boundary with force $\oint_{C'}\gamma\boldsymbol{t}\,\mathrm{d}s$, $\boldsymbol{t}$ the outward unit normal to $C'$ within the surface; by the divergence theorem in the tangent plane this equals $\int_{S'}\nabla_{\mathrm{s}}\gamma\,\mathrm{d}S'$, with $\nabla_{\mathrm{s}}\gamma = \nabla\gamma - \boldsymbol{n}(\boldsymbol{n}\cdot\nabla\gamma)$ the surface gradient. $\square$

**Proposition 8.4.2** If the unit normals of $S$ are extended to a smooth unit vector field $\boldsymbol{n}(\boldsymbol{x})$ near $S$, then $\nabla\cdot\boldsymbol{n} = 1/R_1 + 1/R_2$ on $S$ (twice the mean **curvature**).

**Proof** Consider the thin region $\{\boldsymbol{x} + r\boldsymbol{n}(\boldsymbol{x}) : 0 \le r \le \delta\zeta, \boldsymbol{x} \in \mathrm{d}S\}$. Integrating $\partial_in_i$ over it, the divergence theorem leaves only the two caps (on the sides $\boldsymbol{n}$ is tangent), whose areas differ by $(1/R_1 + 1/R_2)\,\mathrm{d}S\,\delta\zeta$; the integral is also $\approx\partial_in_i\,\mathrm{d}S\,\delta\zeta$. $\square$

![Surface forces on a tissue (Theorem 8.4.1). A: a curved patch of the tissue surface, shaded by the local tension (darker is higher): the normal force −γ(1/R1 + 1/R2)n points towards the centre of curvature (Laplace pressure), and the tangential force ∇sγ points along the surface towards higher tension (Marangoni force). B: consequence for an aggregate whose tension is highest at one pole: the surface is pulled towards that pole and the interior circulates in two loops (schematic Stokes flow)](./plots/surface-forces.py)

## 8.5. Dimensional Analysis and Stokes Flow

Let $\gamma_0$ be a typical surface tension, $U_0$ a typical speed and $L_0$ the size of the aggregate. Viscous stresses on $S$ balance surface tension when $\eta U_0/L_0 \sim \gamma_0/L_0$, i.e. $U_0 \sim \gamma_0/\eta$. With $\gamma_0 \approx 15\,\mathrm{mN\,m^{-1}}$ and $\eta \approx 10^6\,\mathrm{Pa\,s}$ (values for cell aggregates), $U_0 \approx 1.5\times10^{-8}\,\mathrm{m\,s^{-1}}$, so that an aggregate $1\,\mathrm{mm}$ across deforms appreciably in $L_0/U_0 \approx 7\times10^4\,\mathrm{s}$, about a day. These numbers were themselves obtained by assuming the liquid analogy, but it is encouraging that the time that emerges is the time scale of developmental movements.

Inertia compares with viscous force as $\rho U_0^2/L_0$ to $\eta U_0/L_0^2$, their ratio being the Reynolds number $\operatorname{Re} = \rho U_0L_0/\eta \approx 10^3\times1.5\times10^{-8}\times10^{-3}/10^6 \approx 10^{-14}$. Inertia is utterly negligible: the flow is set up instantaneously by the current surface forces and stops the moment they vanish (compare $\operatorname{Re} \sim 10^{-5}$ for a swimming bacterium, [7.3.14](/7.3.14)).

Scale $\boldsymbol{x}$ by $L_0$, $t$ by $\eta L_0/\gamma_0$, $\boldsymbol{u}$ by $\gamma_0/\eta$, $p$ by $\gamma_0/L_0$, $\gamma$ by $\gamma_0$, $R_i$ by $L_0$, $\boldsymbol{f}$ by $\gamma_0/L_0^2$ and $q$ by a typical growth rate $q_0$. Dropping inertia, the dimensionless equations are

$$
\frac{\partial p}{\partial x_i} - \nabla^2u_i = f_i + \frac{\Pi}{3}\frac{\partial q}{\partial x_i}, \qquad \frac{\partial u_i}{\partial x_i} = \Pi q, \qquad
\sigma_{ij}n_j = -\gamma\Bigl(\frac1{R_1} + \frac1{R_2}\Bigr)n_i + \nabla_{\mathrm{s}}\gamma \ \text{on } S,
$$
with the growth number $\Pi = (q_0/\rho)(\eta L_0/\gamma_0)$, the ratio of the time scale of tension-driven flow to that of growth. When $\Pi$ is small, shape changes are independent of growth. The system is closed by the kinematic condition that the boundary moves with the material: if $S$ is the level set $\Sigma(\boldsymbol{x}, t) = 0$, then $\mathrm{d}\Sigma/\mathrm{d}t = \partial_t\Sigma + u_i\partial_i\Sigma = 0$ on $S$, and by a law for $\gamma$ (7.5.7 and 8.6, 8.8).

**Definition 8.5.1 (Stokes Flow)** **Stokes flow** (creeping flow) is flow at vanishing Reynolds number, governed by $\nabla p - \eta\nabla^2\boldsymbol{u} = \boldsymbol{f}$ and $\nabla\cdot\boldsymbol{u} = 0$ (without growth): the equations are linear and contain no time derivative, so time enters only through the moving boundary and the changing forces on it.

The problem is nevertheless nonlinear, because the domain on which the linear equations are solved changes with the solution. Two classical solutions give the time scales of tissue rounding and fusion. A small ellipsoidal deformation of a sphere of radius $R$ decays exponentially at the rate $\frac{20}{19}\gamma/(\eta R)$ when the surrounding medium is much less viscous (the limit of Rallison's result for a drop in another liquid), and a short surface wave of wavenumber $k$ decays at the rate $\gamma k/(2\eta)$, so small wrinkles disappear first. Two spheres of radius $a$ in contact fuse by viscous sintering: in Frenkel's analysis the neck radius $x$ grows as $(x/a)^2 = 3\gamma t/(2\eta a)$. Fitting this law to aggregate fusion is one way tissue viscosities have been estimated.

**Example 8.5.1** For $\gamma = 10\,\mathrm{mN\,m^{-1}}$, $\eta = 2\times10^5\,\mathrm{Pa\,s}$ and $a = 200\,\mu\mathrm{m}$, the time unit $\eta a/\gamma$ is $4\times10^3\,\mathrm{s}$; the neck reaches half the radius when $3\gamma t/(2\eta a) = 1/4$, $t = \frac16\eta a/\gamma \approx 670\,\mathrm{s}$, about 11 minutes, and a deformed aggregate of the same size rounds up with time constant $\frac{19}{20}\eta a/\gamma \approx 1\,\mathrm{h}$. With $\eta = 10^7\,\mathrm{Pa\,s}$ the times are fifty times longer.

![Tension-driven Stokes flow of aggregates. A: decay of a small ellipsoidal (l = 2) deformation of a very viscous drop at the rate (20/19)γ/(ηR) (solid), and of a short surface wave with kR = 6 at the planar rate γk/(2η) (dashed). B: early fusion of two spheres of radius a by viscous sintering (Frenkel): (x/a)² = 3γt/(2ηa); upper axis in hours for γ = 10 mN/m, η = 2 × 10⁵ Pa s, a = 200 µm. C: outlines of two fusing spheres at neck radii x/a = 0.2, 0.5 and 0.8](./plots/aggregate-rounding.py)

## 8.6. Dissipation and the Energy Balance

Multiplying the Stokes equations by $u_i$ and integrating over $V$, using the divergence theorem and the surface traction of Theorem 8.4.1, gives an energy balance. Combined with the rate of change of the surface energy, $\frac{\mathrm{d}}{\mathrm{d}t}\int_S\gamma\,\mathrm{d}S = \int_S\partial_t\gamma\,\mathrm{d}S + \int_S\gamma(1/R_1 + 1/R_2)u_in_i\,\mathrm{d}S$ (the second term is the change of area under normal motion, Proposition 8.4.2), one obtains:

**Theorem 8.6.1 (Energy Balance)** For Stokes flow of a tissue with surface tension $\gamma$, body force $\boldsymbol{f}$ and growth $q$,

$$
\frac{\mathrm{d}}{\mathrm{d}t}\int_S\gamma\,\mathrm{d}S - \int_S\Bigl(\frac{\partial\gamma}{\partial t} + u_i\frac{\partial\gamma}{\partial x_i} - u_in_in_j\frac{\partial\gamma}{\partial x_j}\Bigr)\mathrm{d}S = \int_Vu_if_i\,\mathrm{d}V + \Pi\int_Vpq\,\mathrm{d}V - \Phi,
$$
where the viscous dissipation (dimensionless) is

$$
\Phi = \frac12\int_V\Bigl[\Bigl(\frac{\partial u_i}{\partial x_j} + \frac{\partial u_j}{\partial x_i}\Bigr)^2 - \frac43\Pi^2q^2\Bigr]\mathrm{d}V \ge 0.
$$
The free surface energy is raised by the work of body forces and of growth and lowered by viscous dissipation. The integral on the left vanishes when the tension is a material property of the surface ($\gamma$ constant along the motion of surface particles, apart from normal motion).

Now let $V$ be divided into regions $V_\alpha$ of single cell types, with constant tensions $\gamma_{\alpha\beta}$ on the interfaces $S_{\alpha\beta}$ and viscosities $\eta_\alpha$. The interfaces are material ($\mathrm{d}\Sigma_{\alpha\beta}/\mathrm{d}t = 0$), and across them the stress jumps by the Laplace term: $(\sigma^\beta_{ij} - \sigma^\alpha_{ij})n_j = \gamma_{\alpha\beta}(\partial_jn_j)n_i$ on $S_{\alpha\beta}$. The same calculation gives

$$
\frac{\mathrm{d}}{\mathrm{d}t}\sum_{\alpha<\beta}\int_{S_{\alpha\beta}}\gamma_{\alpha\beta}\,\mathrm{d}S = \sum_\alpha\int_{V_\alpha}\bigl(\boldsymbol{u}\cdot\boldsymbol{f}_\alpha + p\tilde q_\alpha\bigr)\mathrm{d}V - \sum_\alpha\Phi_\alpha.
$$
Without sources and body forces the total interfacial energy decreases monotonically, at a rate equal to the total viscous dissipation. This is the dynamical counterpart of the minimization of the surface potential in **cell sorting** (Formula 7.2.1): since kinetic energy is negligible, the first law says that the rate of work of the surface tensions equals the rate of heat production. It does not by itself fix the flow; the variational principle below does.

Next suppose the tissue is layered, with cell type constant on surfaces, and the layers so numerous that cell type is a smooth function. Let $\phi$ be a function with jumps $\phi_\alpha - \phi_\beta = \gamma_{\alpha\beta} \ge 0$ across the interfaces between successive layers (normal $\boldsymbol{n}$ pointing from $\alpha$ to $\beta$). For a virtual displacement $\delta\boldsymbol{\xi}$ supported in a small volume $V'$ containing many layers, summing the interfacial forces and passing to a smooth $\phi$, the interfacial tensions act as a body force

$$
f_i = \frac{\partial\phi}{\partial x_i}\frac{\partial n_j}{\partial x_j}, \qquad \boldsymbol{n} = \frac{\nabla\phi}{\lvert\nabla\phi\rvert}.
$$
Here $\phi$ is a smooth approximation, built from the adhesive energies ($2\gamma_{\alpha\beta} = E_{\alpha\alpha} + E_{\beta\beta} - 2E_{\alpha\beta}$) and the initial layering; thereafter it is a cell property and is carried by the cells, $\mathrm{d}\phi/\mathrm{d}t = 0$. Whether a $\phi$ defined on cell types themselves exists, with $\gamma_{\alpha\beta} = \phi_\alpha - \phi_\beta$ for every pair, is not automatic: since $E_{\alpha\beta}$ cannot in general be predicted from $E_{\alpha\alpha}$ and $E_{\beta\beta}$, interfacial tensions cannot be predicted from properties of isolated cell types. The sparse-site model gives tensions determined by cell properties but not as differences; the **floating-site model** gives $\mathrm{d}\phi = k\,\mathrm{d}N$ (7.5.7, Definition 7.3.1).

**Theorem 8.6.2 (Volume Free Energy)** If part $V'$ of the tissue consists of continuously distributed cell types with volume potential $\phi$ (taken constant near the boundary of $V'$), then without body forces and growth

$$
\frac{\mathrm{d}}{\mathrm{d}t}\Bigl[\int_{V'}\lvert\nabla\phi\rvert\,\mathrm{d}V + V_{\mathrm{fs}}\Bigr] = -\Phi,
$$
where $V_{\mathrm{fs}}$ is the free energy of all discrete surfaces and interfaces and $\int\lvert\nabla\phi\rvert\,\mathrm{d}V$ is the *volume free energy* of the continuous layering.

**Proof** (outline) At the surface, the layers beneath pull along the lines of constant $\phi$, so the surface traction acquires the term $-\lvert\nabla\phi\rvert(\boldsymbol{n} - \gamma_{\boldsymbol{n}}\tilde{\boldsymbol{n}})$, with $\tilde{\boldsymbol{n}}$ the normal to the layers and $\gamma_{\boldsymbol{n}} = \boldsymbol{n}\cdot\tilde{\boldsymbol{n}}$. Since $\phi$ is material, $\partial_t\phi = -\boldsymbol{u}\cdot\nabla\phi$, and

$$
\frac{\mathrm{d}}{\mathrm{d}t}\int\lvert\nabla\phi\rvert\,\mathrm{d}V' = -\int\frac{\nabla\phi\cdot\nabla(\boldsymbol{u}\cdot\nabla\phi)}{\lvert\nabla\phi\rvert}\mathrm{d}V' + \int\boldsymbol{u}\cdot\boldsymbol{n}\lvert\nabla\phi\rvert\,\mathrm{d}S'.
$$
Integrating by parts, the volume term becomes $\int\nabla\cdot\bigl(\nabla\phi/\lvert\nabla\phi\rvert\bigr)\,\boldsymbol{u}\cdot\nabla\phi\,\mathrm{d}V' = -\int\boldsymbol{u}\cdot\boldsymbol{f}\,\mathrm{d}V'$ plus a surface term; combining with the energy balance including the modified traction, all surface terms cancel. $\square$

The balance $\mathrm{d}E/\mathrm{d}t = -\Phi$, with $E$ the total surface (and volume) free energy, is one scalar equation and does not determine the flow. A variational principle does. For a system with coordinates $r_i$ and velocities $u_i = \dot r_i$:

**Definition 8.6.1 (Rayleigh Dissipation Function)** The **Rayleigh dissipation function** $\Phi(\boldsymbol{u})$ of a system is its rate of energy dissipation expressed as a function of the velocities; for linear friction and viscosity it is a positive quadratic form, homogeneous of degree two in the velocities. For a viscous liquid, $\Phi = \frac\eta2\int(\partial_ju_i + \partial_iu_j)^2\,\mathrm{d}V$ (the shear part reduces to $\eta\int\sum_{ij}(\partial_ju_i)^2\,\mathrm{d}V$ for incompressible flow with suitable boundary conditions).

**Theorem 8.6.3 (Rayleigh's Principle)** Suppose that at each instant the motion makes the free energy $E(\boldsymbol{r})$ decrease as fast as possible among all velocity fields with the same dissipation, subject to the energy balance $\dot E + \Phi = 0$. Then the velocities satisfy

$$
\delta\Bigl(\dot E + \tfrac12\Phi\Bigr) = 0, \qquad\text{that is,}\qquad \frac{\partial E}{\partial r_i} + \frac12\frac{\partial\Phi}{\partial u_i} = 0,
$$
the variation being over the velocities at fixed configuration.

**Proof** Maximizing $-\dot E$ at fixed $\Phi$ with a Lagrange multiplier $\lambda(t)$ (the **method of Lagrange multipliers**) gives $\delta(\dot E + \lambda\Phi) = 0$. With $\dot E = \sum_i(\partial E/\partial r_i)u_i$ and $\delta = \partial/\partial u_i$, $\partial E/\partial r_i + \lambda\,\partial\Phi/\partial u_i = 0$. Multiply by $u_i$ and sum: since $\Phi$ is a **homogeneous function** of degree two, Euler's theorem gives $\sum_iu_i\,\partial\Phi/\partial u_i = 2\Phi$, so $\dot E + 2\lambda\Phi = 0$. The energy balance $\dot E = -\Phi$ then forces $\lambda = \frac12$. $\square$

**Example 8.6.1** Let the configuration be described by a few coordinates $\boldsymbol{q}$ and $\Phi = \sum_{ij}C_{ij}\dot q_i\dot q_j$ with $C$ symmetric positive definite (a friction or drag matrix). Rayleigh's principle gives $\partial E/\partial q_i + \sum_jC_{ij}\dot q_j = 0$, i.e. $\dot{\boldsymbol{q}} = -C^{-1}\nabla E$: overdamped motion is a gradient flow of the free energy with mobility $C^{-1}$, and $\dot E = -\nabla E\cdot C^{-1}\nabla E = -\Phi \le 0$. This is the "quasi-static dynamics with a drag matrix" whose singularities are classified in 7.5.10 (§10.2–10.3). For Stokes flow the principle is equivalent to the classical theorem of Helmholtz that the Stokes solution minimizes the dissipation among all incompressible flows with the same boundary velocities, and it allows tissue flows to be computed variationally from a few shape parameters; the shape changes of a columnar cell on a substrate and the invagination of an epithelial ring treated in this way are in 7.5.9.

## 8.7. Stability of Layered Aggregates

The fluid analogy has a limitation that shows up clearly in a stability problem. Take three cell types arranged as an onion, $A$ inside, then $B$, then $C$. Discrete cells of $A$ can break through the $B$ layer and touch $C$ directly. Homogeneous fluid layers subject to smooth deformations cannot: a fluid layer thins but never breaks. So even an onion that is "wrong" (with $B$ beneath $A$ although $B$ engulfs $A$) need not be uncovered by small fluid perturbations, much as local kinetic sorting rules fail to reach the global minimum (7.5.7, §7.6). How does this show up in a linear stability analysis?

Discrete fluid layers with spherical interfaces are only neutrally stable: the interfaces must be spheres but need not stay concentric. For a continuous layering, let the volume potential at equilibrium be $\phi = \Psi(r)$, $r$ the radial coordinate, $r = 1$ on $S$. If $\Psi(1) \ne 0$ there is a surface tension on $S$ and any deformation of $S$ costs energy, so consider deformations that leave $S$ fixed, generated by a solenoidal velocity $\boldsymbol{u}$ tangent to $S$: $\boldsymbol{X} \approx \boldsymbol{b} + t\boldsymbol{u}(\boldsymbol{b})$, displacement $\delta\boldsymbol{X} \approx t\boldsymbol{u}$.

**Theorem 8.7.1 (Neutral Stability of Continuous Onions)** If $\Psi'$ has no zeros, the change of the volume free energy is, to second order in the displacement,

$$
\delta\int\lvert\nabla\phi\rvert\,\mathrm{d}V = \frac12\int\lvert\Psi'\rvert\Bigl[\lvert\nabla_{\mathrm{s}}\delta X_r\rvert^2 - 2\Bigl(\frac{\delta X_r}{r}\Bigr)^2\Bigr]\mathrm{d}V \ge 0,
$$
with equality for nontrivial displacements, where $\delta X_r$ is the radial component of the displacement and $\nabla_{\mathrm{s}}$ the gradient on the sphere of radius $r$: continuous layering is at most neutrally stable. If $\Psi'$ vanishes at radii $r_\alpha$, an additional term $-\sum_\alpha\lvert\Psi''(r_\alpha)\rvert\int(\delta X_r)^2\,\mathrm{d}S_{r_\alpha}$ appears, which is destabilizing.

**Proof** (outline) Because $\phi$ is material, $\partial_t\delta\phi = -\boldsymbol{u}\cdot\nabla\Psi - \boldsymbol{u}\cdot\nabla\delta\phi$, which integrates to $\delta\phi = -\delta\boldsymbol{X}\cdot\nabla\Psi + \frac12\delta\boldsymbol{X}\cdot\nabla(\delta\boldsymbol{X}\cdot\nabla\Psi) + O(\delta X^3)$. Expanding $\lvert\nabla\Psi + \nabla\delta\phi\rvert$ to second order and using that $\Psi$ depends on $r$ only,

$$
\lvert\nabla\phi\rvert = \lvert\Psi'\rvert\Bigl[1 - \frac{1}{\Psi'}\frac{\partial}{\partial r}(\delta X_r\Psi') + \frac{1}{2\Psi'}\frac{\partial}{\partial r}\bigl[\delta\boldsymbol{X}\cdot\nabla(\delta X_r\Psi')\bigr] + \frac12\lvert\nabla_{\mathrm{s}}\delta X_r\rvert^2\Bigr] + O(\delta X^3).
$$
The first-order term integrates (in spherical coordinates, with $\delta X_r = 0$ on $S$) to $\int(2/r)\lvert\Psi'\rvert\delta X_r\,\mathrm{d}V$, which vanishes because a solenoidal field has zero flux through every sphere $r = \mathrm{const}$ inside $S$. If $\Psi'$ has one sign, the first quadratic term becomes, after integration by parts, $-\int\lvert\Psi'\rvert(\delta X_r/r)^2\,\mathrm{d}V$, giving the stated form. On a sphere of radius $r$ every function $\psi$ with zero mean satisfies $\int\lvert\nabla_{\mathrm{s}}\psi\rvert^2\,\mathrm{d}S \ge (2/r^2)\int\psi^2\,\mathrm{d}S$, because the smallest nonzero eigenvalue of the Laplacian on the sphere is $l(l + 1)/r^2$ with $l = 1$ (spherical harmonics, [2.5.5](/2.5.5)), with equality for $\psi \propto x_1$; $\delta X_r$ has zero mean on each sphere, so the integrand is nonnegative after integration over each sphere. When $\Psi'$ changes sign the integration by parts produces boundary terms at its zeros, which give the destabilizing contribution. $\square$

The equality case $l = 1$ is a shift of the layers relative to each other, the continuous counterpart of non-concentric spheres. The instability at a zero of $\Psi'$ has a clear meaning: near such a radius the local tension increases outwards, and the free energy can be lowered by interchanging two layers. Since the fluid picture is no better than local kinetic sorting at undoing internalized layering, one should not expect it to explain the final arrangement of complex structures. Fortunately the early movements of vertebrate development (gastrulation) are largely concerned with internalization itself, and the structures harder to describe come later; in practice embryos tend to show centring of onion-like structures rather than their breakup, which differential adhesion alone does not explain (7.5.7, §7.2).

## 8.8. The Mechanics of a Single Cell: Surface Instabilities and Cleavage

The same equations apply to a single cell, whose surface carries molecules that control its tension. Let $c(\boldsymbol{x}, t)$ be the concentration of a surface species ("surfactant") on $S$, and let $\gamma = \gamma(c)$. If $c$ is conserved on a patch $S'$ moving with the surface, $\frac{\mathrm{d}}{\mathrm{d}t}\int_{S'}c\,\mathrm{d}S' = F$, the flux across its boundary. The rate of change contains the local change and the change of area, $\int(\partial_tc + c\,(\nabla\cdot\boldsymbol{n})\,\boldsymbol{u}\cdot\boldsymbol{n})\,\mathrm{d}S'$; the flux due to tangential flow is computed by Stokes' theorem. Adding surface diffusion and sources gives

**Formula 8.8.1 (Surfactant Conservation on a Moving Surface)**

$$
\frac{\partial c}{\partial t} + \boldsymbol{u}_{\mathrm{t}}\cdot\nabla_{\mathrm{s}}c + c\,\Gamma = D\nabla_{\mathrm{s}}^2c + r(c), \qquad
\Gamma = (\boldsymbol{u}\cdot\boldsymbol{n})\,\nabla\cdot\boldsymbol{n} + \nabla_{\mathrm{s}}\cdot\boldsymbol{u}_{\mathrm{t}},
$$
where $\boldsymbol{u}_{\mathrm{t}} = \boldsymbol{u} - (\boldsymbol{u}\cdot\boldsymbol{n})\boldsymbol{n}$ is the tangential velocity, $\Gamma$ the rate of dilation of surface area (from normal motion of a curved surface and from divergence of the tangential flow), $\nabla_{\mathrm{s}}^2$ the Laplacian on the surface, $D$ the surface diffusivity (dimensionless, $\eta D_{\mathrm{dim}}/(\gamma_0L_0)$) and $r$ a reaction term. With $r \ne 0$ this is a reaction–diffusion system on a moving surface (7.5.12); for several species $c$ and $D$ become a vector and a diagonal matrix.

The coupling between tension and transport makes a uniform state unstable. Greenspan (1977) analysed a viscous sphere covered uniformly by a conserved surfactant that raises surface tension ($\gamma'(c) > 0$) and showed that the uniform state becomes unstable when the surfactant diffusivity is small enough. The mechanism is a positive feedback: a local excess of $c$ raises $\gamma$ there; the Marangoni force (Theorem 8.4.1) pulls surface towards the high-tension region; the flow carries more surfactant there. Diffusion opposes the accumulation. As $D$ decreases, the $P_1$ mode (a polarized cap) is excited first and the $P_2$ mode second; the $P_2$ mode concentrates tension in an equatorial belt and constricts the cell there, a mechanical model of cleavage, although by the symmetry of linear theory the opposite sign (dimpling at the poles) is equally possible.

A minimal model shows the mechanism and the order of the modes. Consider a thin contractile surface layer on a meridian of a spherical cell of radius $R$ (arc length $s$), with a species $c$ that raises the tension, $T(c)$, a friction $\xi$ with the cell interior and a surface viscosity $\eta_{\mathrm{s}}$:

$$
\xi v - \eta_{\mathrm{s}}\frac{\partial^2v}{\partial s^2} = \frac{\partial T(c)}{\partial s}, \qquad
\frac{\partial c}{\partial t} = -\frac{\partial(cv)}{\partial s} + D\frac{\partial^2c}{\partial s^2} + k(c_0 - c),
\tag{8.5}
$$
with turnover rate $k$ towards a uniform level $c_0$. Linearizing about $c = c_0$ with $c - c_0 \propto \mathrm{e}^{\mathrm{i}qs + st}$, the force balance gives $\hat v = \mathrm{i}qT'(c_0)\hat c/(\xi + \eta_{\mathrm{s}}q^2)$, and the growth rate is

$$
s(q) = q^2\Bigl[\frac{c_0T'(c_0)}{\xi + \eta_{\mathrm{s}}q^2} - D\Bigr] - k.
$$
On a closed meridian $q = n/R$. Since the first term in brackets decreases with $q$, the threshold diffusivity $c_0T'(c_0)/(\xi + \eta_{\mathrm{s}}n^2/R^2)$ is largest for $n = 1$ and next for $n = 2$, as in Greenspan's result; surface viscosity and diffusion suppress short waves. Mode $n = 2$ on a meridian puts two opposite maxima on the circle, which on the cell is a ring at the equator (Figure 6).

![A contractile surface layer is unstable (Eq. (8.5)). A: growth rate of modes cos(ns/R) on a meridian for three diffusivities (ξ = 1, η_s = 0.25, c0T′(c0) = 2, k = 0.1): as D falls, mode 1 (a polar cap) and mode 2 (two opposite maxima) become unstable first, short waves stay stable. B: simulation for D = 0.5 from 1% noise: the concentration collects into two opposite peaks that saturate. C: the final pattern on the cell outline, rotated so that one peak lies at the equator: a ring of high tension, the geometry of a cleavage furrow](./plots/cortical-instability.py)

How does this compare with real cleavage? The modern view of **cytokinesis** ([7.3.21](/7.3.21)) keeps the mechanics and changes the cause of the pattern. The surface layer is the actomyosin cortex, the tension-raising species is active **myosin** II, and Eq. (8.5) is a one-dimensional version of active-gel models of cortical flow (Bois, Jülicher and Grill 2011), which reproduce the flows towards the equator seen during cytokinesis and the polarizing flow that sets up PAR polarity in the *C. elegans* zygote (7.5.6). But the position of the **contractile ring** is not chosen by a spontaneous instability: it is specified by the **mitotic spindle**, whose central spindle and astral **microtubules** deliver the activator of RhoA (centralspindlin and its partner Ect2) to an equatorial zone and inhibit contractility at the poles. The self-reinforcing flow then sharpens and maintains a pattern that the spindle has seeded. Greenspan's model was therefore right about the mechanics of a tension-raising, advected surface species and wrong to the extent that it took the instability as the cause of furrow position.

At the scale of the embryo the same idea appears in another form: Turing's late work on reaction–diffusion patterns on a growing spherical shell suggests that a mode can be excited when the shell grows past a critical size, and if the **morphogen** raises surface tension, the resulting tension pattern drives tissue flow; this, and the nonlinear steepening of tension profiles advected by the flow they cause, is taken up for amphibian gastrulation in 7.5.9.

## 8.9. Active Forces: The Actomyosin Cortex

The tensions in the models above are not passive. The surface of an animal cell is lined by the **cell cortex**, a thin network of **actin filaments** cross-linked and contracted by **myosin II** ([7.3.13](/7.3.13)). Its contraction puts the cell surface under tension, which in round cells balances an internal hydrostatic pressure.

**Definition 8.9.1 (Cortical Tension)** The **cortical tension** of a cell is the tension (force per unit length) in its surface, generated mainly by myosin II contraction of the actin cortex and to a lesser extent by membrane tension; it plays the role of the surface tension of a liquid drop.

Cortical tension is measured by micropipette aspiration: a cell of radius $R_{\mathrm{c}}$ is aspirated into a pipette of radius $R_{\mathrm{p}}$, and at the pressure difference $\Delta P$ at which the aspirated tongue reaches length $R_{\mathrm{p}}$ (a hemisphere), the Young–Laplace equation applied to the two curved surfaces gives $\sigma_{\mathrm{c}} = \Delta P/\bigl[2(1/R_{\mathrm{p}} - 1/R_{\mathrm{c}})\bigr]$. Values range from about $10^{-5}$ to $10^{-3}\,\mathrm{N\,m^{-1}}$ depending on the cell type, well below the $10^{-3}$–$2\times10^{-2}\,\mathrm{N\,m^{-1}}$ of **tissue surface tensions**, which are not single-cell tensions but properties of the tissue.

The cortex also explains how adhesion acts (7.5.7, §7.5): the tension of a contact is the cortical tension on both sides minus the adhesion energy, and **cadherin** junctions signal locally to lower cortical contractility. Gradients of contractility within a tissue produce the active forces of morphogenesis. In apical constriction, contraction of the apical cortex narrows the apical surface of epithelial cells and wedges them, bending the sheet: in the *Drosophila* ventral furrow, under the control of the transcription factors Twist and Snail, the apical actomyosin network contracts in pulses, and a ratchet stabilizes each step (Martin, Kaschube and Wieschaus 2009); in vertebrate **neural plate** cells the protein Shroom recruits Rho kinase to the apical junctions (7.5.18). Planar polarized contractility of the junctions themselves drives neighbour exchange (8.10) and tissue elongation in **convergent extension** (7.5.9). Mechanical feedback (tension stabilizing myosin, stretch activating signalling) links the mechanics of this chapter to cell signalling.

## 8.10. Vertex Models and the Fluid–Solid Transition

Between continuum mechanics and cell-based simulation lie vertex models of epithelia, in which each cell is a polygon and the degrees of freedom are the positions of its vertices.

**Algorithm 8.10.1 (Vertex Model)** (Farhadifar et al. 2007; Bi et al. 2015) An epithelium is a tiling of the plane by polygons $\alpha$ with areas $A_\alpha$ and perimeters $P_\alpha$.

1. Define the energy $E = \sum_\alpha\bigl[K_A(A_\alpha - A_0)^2 + K_P(P_\alpha - P_0)^2\bigr]$: the area term expresses resistance of cell volume and height to change, the perimeter term the competition between cortical contractility (favouring small $P$) and adhesion (favouring long contacts), with a preferred perimeter $P_0$.
2. Move the vertices by overdamped dynamics, $\zeta\,\dot{\boldsymbol{r}}_i = -\partial E/\partial\boldsymbol{r}_i$ (a gradient flow, Example 8.6.1), possibly with active and random forces.
3. When a junction becomes shorter than a threshold, carry out a T1 transition: the junction shrinks to a four-fold vertex, which resolves into a new junction in the perpendicular direction, so two cells lose contact and two others gain it (Figure 7A).
4. Optionally add cell division and extrusion.

A T1 transition is the elementary step by which cells exchange neighbours and a tissue flows. In the dimensionless form of the model the key parameter is the target shape index $p_0 = P_0/\sqrt{A_0}$. Bi, Lopez, Schwarz and Manning (2015) showed that the energy barriers to T1 transitions vanish when $p_0$ exceeds a critical value $p_0^* \approx 3.81$: below it the tissue is a solid (cells are caged by their neighbours), above it a fluid. The observed shape index $q = P/\sqrt{A}$ of the cells is the experimental order parameter: cells are roughly isotropic and compact (low $q$) in solid-like tissue, elongated and irregular in fluid-like tissue (Figure 7B). This has been used to show that airway epithelia unjam during asthma-related stress (Park et al. 2015) and that the vertebrate body axis elongates by a jamming transition, fluid-like tissue in the tailbud becoming solid-like in the presomitic **mesoderm** (Mongera et al. 2018, zebrafish). Statistical physics of such active materials is now a main approach to tissue mechanics, and it returns to the question raised by the supplementary notes of Percus and Childress: cells do much more than adhere. They deform, extend protrusions, break and form contacts, move relative to each other and generate stresses in their **cytoskeleton**, and an adequate model of cell deformation and motility in aggregates is still being built.

![Vertex models. A: a T1 transition: the junction shared by cells 1 and 3 shrinks to a four-fold vertex and a new junction forms between cells 2 and 4, so neighbours are exchanged; T1 transitions are how a tissue flows and how convergent extension narrows and lengthens it. B: the shape index p = P/√A of single regular shapes (circle 3.545, regular hexagon 3.722, square 4.0) and the rigidity transition of the vertex model at a target shape index p0* ≈ 3.81: tissues with lower values behave as solids, with higher values as fluids](./plots/vertex-t1.py)

## Summary

| Topic | Key results |
|---|---|
| Tissues as liquids (8.1) | viscosity $10^5$–$10^7\,\mathrm{Pa\,s}$, elastic at short times: Maxwell liquid (Definition 8.1.1, Eq. (8.1)), $t_{\mathrm{r}} = \eta/G$; relaxation, creep, start-up |
| Site model (8.2) | site conservation $n_t + (un)_s = q$, $T = g(n)$; sliding: heat equation with moving ends, $U$ and $L$ (Proposition 8.2.1), time scale $L_0^2/K$; interstitial membrane: $L = 2n_0L_0/(n_0 + n_1)$, Laplace-transform solution, $k_{\mathrm{eff}} = 3kn_0/2L_0$, $\eta_{\mathrm{eff}} = L_0n_0^2f$, $t_{\mathrm{r}} = 2L_0^2/3K$ (Theorem 8.2.2) |
| Continuum equations (8.3) | morphodynamics (Definition 8.3.1); continuity with growth (Eq. (8.3)); Newtonian stress, Navier–Stokes (Eq. (8.4)); material derivative; incompressibility ≠ constant density; Maxwell fluid |
| Surface forces (8.4) | traction $-\gamma(1/R_1 + 1/R_2)\boldsymbol{n} + \nabla_{\mathrm{s}}\gamma$ (Theorem 8.4.1); $\nabla\cdot\boldsymbol{n} = 1/R_1 + 1/R_2$ (Proposition 8.4.2) |
| Scales (8.5) | $U_0 \sim \gamma_0/\eta \sim 10^{-8}\,\mathrm{m\,s^{-1}}$, a day per millimetre; $\operatorname{Re} \sim 10^{-14}$: Stokes flow (Definition 8.5.1); growth number $\Pi$; rounding rate $\frac{20}{19}\gamma/\eta R$, fusion $(x/a)^2 = 3\gamma t/2\eta a$ (Example 8.5.1) |
| Energy (8.6) | surface energy falls at the rate of dissipation (Theorem 8.6.1); volume potential $\phi$, body force $\nabla\phi\,\nabla\cdot\boldsymbol{n}$, volume free energy $\int\lvert\nabla\phi\rvert$ (Theorem 8.6.2); Rayleigh dissipation function (Definition 8.6.1) and principle $\delta(\dot E + \Phi/2) = 0$ (Theorem 8.6.3) → gradient flow with drag matrix (Example 8.6.1) |
| Stability (8.7) | fluid layers thin but never break; continuous onions neutrally stable (sphere inequality, $l = 1$), unstable at zeros of $\Psi'$ (Theorem 8.7.1) |
| Single cell (8.8) | surfactant conservation with dilation term (Formula 8.8.1); Greenspan instability for $\gamma'(c) > 0$, small $D$; $s(q) = q^2[c_0T'/(\xi + \eta_{\mathrm{s}}q^2) - D] - k$ (Eq. (8.5)): modes 1 then 2 (equatorial ring); in cells the spindle positions the RhoA zone |
| Active forces (8.9) | cortical tension (Definition 8.9.1), micropipette aspiration; apical constriction (pulsed, ratcheted), Shroom, planar polarized contractility |
| Vertex models (8.10) | $E = \sum K_A(A - A_0)^2 + K_P(P - P_0)^2$, T1 transitions (Algorithm 8.10.1); rigidity transition at $p_0^* \approx 3.81$; jamming in airway epithelia and the zebrafish tailbud |

## Questions

1. A tissue aggregate is compressed suddenly, and the force needed to hold the compression falls to $1/\mathrm{e}$ of its initial value in $4\,\mathrm{min}$. The instantaneous shear modulus is estimated at $G = 500\,\mathrm{Pa}$. What is the viscosity, and would the aggregate behave as an elastic solid or as a liquid during a gastrulation movement lasting $2\,\mathrm{h}$?

   **Answer** The decay time is the relaxation time, $t_{\mathrm{r}} = 240\,\mathrm{s}$, so $\eta = Gt_{\mathrm{r}} = 500 \times 240 = 1.2\times10^5\,\mathrm{Pa\,s}$, in the measured range. Two hours is $t/t_{\mathrm{r}} = 30$, so the elastic stress has relaxed completely and the tissue responds as a viscous liquid; only movements faster than a few minutes would feel its elasticity.

2. Using Proposition 8.2.1, find the steady sliding speed and length of a membrane segment with $L_0 = 10\,\mu\mathrm{m}$, $K = 10^{-14}\,\mathrm{m^2\,s^{-1}}$ pulled to $n_1/n_0 = 0.8$, and the time needed to reach this state.

   **Answer** $U = (K/L_0)(1 - 0.8) = (10^{-14}/10^{-5})\times0.2 = 2\times10^{-10}\,\mathrm{m\,s^{-1}}$ (about $0.7\,\mu\mathrm{m}$ per hour); $L = L_0\ln(1.25)/0.2 = 10\times0.223/0.2 \approx 11.2\,\mu\mathrm{m}$. The relaxation time is of order $L_0^2/K = 10^{-10}/10^{-14} = 10^4\,\mathrm{s}$, about 3 hours (Figure 2 shows that the steady state is reached at $tK/L_0^2 \approx 1$).

3. In the interstitial-membrane model, how do the effective viscosity and relaxation time depend on the contact length $L_0$ and on the site density $n_0$? What does this predict for cells that increase their cadherin expression?

   **Answer** $\eta_{\mathrm{eff}} = L_0n_0^2f$ grows linearly with the contact length and quadratically with site density; $t_{\mathrm{r}} = 2L_0^2/(3K) = 2L_0^2fn_0/(3k)$ grows as $L_0^2$ and linearly with $n_0$. Cells with more adhesion sites (more cadherin) should form tissue that is more viscous and slower to relax (and larger contacts, from stronger adhesion, increase both further), consistent with the qualitative observation that strongly cohesive tissues move slowly; the model gives no link between $f$ and adhesion energy, so the surface tension is not predicted.

4. Show that for a sphere of radius $R$ with uniform tension, Theorem 8.4.1 gives the familiar pressure jump, and that a uniform tension produces no flow in a spherical aggregate. What happens if the tension is higher at one pole?

   **Answer** On a sphere $R_1 = R_2 = R$ and $\nabla_{\mathrm{s}}\gamma = 0$, so the traction is $-2\gamma/R$ times the outward normal: the pressure inside exceeds the outside by $2\gamma/R$. A uniform interior pressure $p = 2\gamma/R$ with $\boldsymbol{u} = \boldsymbol{0}$ satisfies the Stokes equations and the boundary condition, and by uniqueness of Stokes flows it is the solution: no flow. With tension higher at one pole, the tangential traction $\nabla_{\mathrm{s}}\gamma$ points towards that pole all over the surface, dragging surface material towards it; the interior returns the material in two circulating loops (Figure 4B); the sphere also deforms, flattening where the tension is high if the tension gradient is strong.

5. Estimate the Reynolds number for the movement of mesoderm cells migrating at $1\,\mu\mathrm{m\,min^{-1}}$ through tissue of viscosity $10^5\,\mathrm{Pa\,s}$ over a distance of $100\,\mu\mathrm{m}$. What is the practical consequence for modelling?

   **Answer** $U = 1.7\times10^{-8}\,\mathrm{m\,s^{-1}}$, $L = 10^{-4}\,\mathrm{m}$, $\rho = 10^3\,\mathrm{kg\,m^{-3}}$: $\operatorname{Re} = 10^3\times1.7\times10^{-8}\times10^{-4}/10^5 \approx 1.7\times10^{-14}$. Inertia can be dropped entirely: forces balance at every instant (Stokes flow, overdamped cell motion), velocities are proportional to forces, and history enters only through the changing geometry and through the viscoelastic memory of the material.

6. Using Rayleigh's principle, derive the equation of motion for a single shape coordinate $q$ with free energy $E(q) = \frac12\kappa(q - q_0)^2$ and dissipation $\Phi = c\,\dot q^2$. What is the relaxation time? Relate the result to Example 8.5.1.

   **Answer** $\partial E/\partial q + \frac12\partial\Phi/\partial\dot q = \kappa(q - q_0) + c\dot q = 0$, so $q - q_0 \propto \mathrm{e}^{-t\kappa/c}$ with relaxation time $c/\kappa$. For a deformed drop, $\kappa \sim \gamma$ (surface energy per squared deformation amplitude, up to geometric factors) and $c \sim \eta R$ (dissipation of a flow of velocity $\dot q$ over a volume $R^3$ with gradients $\dot q/R$, per squared amplitude rate, again up to factors), giving a time $\sim\eta R/\gamma$, as in the exact rate $\frac{20}{19}\gamma/(\eta R)$.

7. Explain physically why, in Theorem 8.7.1, the displacement with $\delta X_r \propto x_1$ (that is, $l = 1$) costs no energy to second order, and why a zero of $\Psi'$ is destabilizing. What experiment on mixed aggregates could test the prediction that internal layering is not undone by fluid-like motion?

   **Answer** The $l = 1$ displacement is, layer by layer, a rigid shift of each spherical layer relative to its neighbours: interface areas and hence surface energies do not change to second order, just as non-concentric spherical interfaces cost no extra energy. At a zero of $\Psi'$ the ordering of tensions reverses: locally, higher-tension material lies outside lower-tension material, which is the wrong order for **engulfment**, and swapping neighbouring layers lowers the energy, so perturbations grow. Test: build an aggregate in the "wrong" order (for example, coat a cohesive core with a shell of a less cohesive tissue, then add a third tissue that should be inside) and follow whether the wrong-order layer breaks up (discrete cells can break through) or merely thins and persists; compare with cell-tracking to see whether cells cross the layer individually.

8. In Eq. (8.5) with $\xi = 1$, $\eta_{\mathrm{s}} = 0.25$, $c_0T'(c_0) = 2$, $k = 0.1$ and $R = 1$, find the range of diffusivities $D$ for which mode $n = 2$ (an equatorial ring) is unstable, and the range for which $n = 2$ is the fastest-growing mode.

   **Answer** $s_2 = 4[2/(1 + 1) - D] - 0.1 = 3.9 - 4D > 0$ for $D < 0.975$. For mode comparisons, $s_n = n^2[2/(1 + 0.25n^2) - D] - 0.1$; $s_2 > s_1$ requires $4 - 4D > 1.6 - D$, i.e. $D < 0.8$; $s_2 > s_3$ requires $4 - 4D > 9(2/3.25) - 9D = 5.54 - 9D$, i.e. $D > 0.308$. So $n = 2$ is fastest for $0.31 < D < 0.8$ (at $D = 0.5$: $s_1 = 1.0$, $s_2 = 1.9$, $s_3 = 0.94$, as in Figure 6A); at smaller $D$, higher modes take over.

9. (Experimental design) How would you test whether the position of the cleavage furrow is set by a spontaneous cortical instability (as in Greenspan's model) or by a signal from the spindle?

   **Answer** Displace the spindle (micromanipulation, or centrifugation of eggs as in Rappaport's experiments, or optogenetic pulling) and ask whether the furrow follows it: if it forms over the new spindle midzone, the spindle specifies position. Rappaport's torus experiment, in which a furrow forms between two asters that are not linked by a spindle, shows that astral microtubules suffice. Conversely, optogenetic activation of RhoA at an ectopic position on the cortex of a cell without a spindle signal tests whether cortical feedback alone can produce and maintain a furrow. Measuring cortical flows (by tracking myosin particles) tests the advective feedback of Eq. (8.5): flows should converge on the furrow, and reducing them (lower myosin activity) should broaden the band.

10. A sheet of polygonal cells has mean perimeter $P = 16\,\mu\mathrm{m}$ and mean area $A = 16\,\mu\mathrm{m^2}$; after an experimental treatment the values become $P = 15\,\mu\mathrm{m}$, $A = 18\,\mu\mathrm{m^2}$. Using the vertex model criterion, is the tissue fluid-like or solid-like before and after? What cell-level change could the treatment have produced?

    **Answer** Before: $q = 16/\sqrt{16} = 4.0 > 3.81$, fluid-like. After: $q = 15/\sqrt{18} \approx 3.54 < 3.81$, solid-like (nearly circular, below the regular hexagon value 3.72). The cells have become more compact: increased cortical (junctional) contractility or reduced adhesion lowers the preferred perimeter $P_0$ relative to $\sqrt{A_0}$, which in the vertex model raises the energy barriers to T1 transitions and jams the tissue. One would check by measuring neighbour exchange rates (T1 events per cell per hour), which should fall.
