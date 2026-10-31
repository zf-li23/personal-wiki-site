---
title: Random Walks, Diffusion and Brownian Motion
description: The dynamics of thermal motion in the cell. Random walks and the mean squared displacement, persistent walks and the diffusion coefficient; diffusion times from proteins to axons; the diffusion equation and the Fourier-series solution of FRAP; diffusion to capture (4πDac, a/r₀), the diffusion limit of cell size and of reaction rates, and the Péclet number; drift and diffusion, the Smoluchowski equation, the Einstein and Stokes–Einstein relations, the Nernst potential and rotational diffusion; the Langevin equation, the fluctuation–dissipation theorem and the Ornstein–Uhlenbeck process; master equations and the Fokker–Planck equation; mean first-passage times and Kramers' rate of barrier crossing.
---

Everything in a cell jiggles. A protein in the cytoplasm is struck by water molecules about $10^{13}$ times per second, changes its direction of motion every picosecond, and nevertheless wanders across a bacterium in a few hundredths of a second. This chapter derives the laws of that motion and shows why they shape cells. A sequence of independent steps produces a mean squared displacement that grows linearly in time (5.1), which makes diffusion fast over short distances and hopeless over long ones; the diffusion equation turns the same statement into a field theory, solves photobleaching experiments and gives the rate at which molecules find a target (5.2). A force adds drift to diffusion, and the requirement that the drift and diffusion balance into the **Boltzmann distribution** of [7.6.2](/7.6.2) fixes the relation between diffusion and friction (5.3). The Langevin equation describes a single particle and shows that friction and fluctuations are two faces of the same collisions (5.4); the master and Fokker–Planck equations describe probabilities (5.5); and the time to cross a barrier, Kramers' rate, connects diffusion to the rates of conformational change used in [7.6.3](/7.6.3) and [7.6.4](/7.6.4) (5.6). The mathematics of the heat equation is in [2.5.1](/2.5.1) and [2.5.7](/2.5.7), the **Brownian motion** of colloids and Perrin's measurement of the Avogadro constant in [6.3.21](/6.3.21), diffusion-controlled reaction rates in [6.3.17](/6.3.17), and the microscopy of single-particle tracking and FRAP in [7.3.2](/7.3.2); they are used here and not rederived. The results return throughout the course: in hydrodynamic measurements of molecular size ([7.6.8](/7.6.8)), single-molecule methods ([7.6.12](/7.6.12), [7.6.17](/7.6.17)), the crowded cytoplasm ([7.6.23](/7.6.23)), motors ([7.6.27](/7.6.27)), the stochastic kinetics of gene expression ([7.6.32](/7.6.32)) and the physical limits of sensing ([7.6.35](/7.6.35)).

## 5.1. Random Walks

### 5.1.1. The Random Walk and Its Mean Squared Displacement

A Brownian particle, a protein or a bead of a micrometer, is much heavier than the water molecules around it. Each collision changes its velocity only slightly, but the collisions are so frequent and so uncorrelated that after a short time the particle has forgotten its previous direction. On time scales longer than this memory, its motion is a sequence of independent displacements.

**Definition 5.1.1 (Random Walk)** A **random walk** in $d$ dimensions is a sequence of positions $\boldsymbol{r}_N = \boldsymbol{r}_0 + \sum_{i=1}^{N}\Delta\boldsymbol{r}_i$, in which the steps $\Delta\boldsymbol{r}_i$, taken at intervals $\tau$, are independent and identically distributed random vectors. The walk is unbiased if $\langle\Delta\boldsymbol{r}_i\rangle = \boldsymbol{0}$.

**Theorem 5.1.1 (Mean Squared Displacement of a Random Walk)** For an unbiased random walk with step variance $\langle\lvert\Delta\boldsymbol{r}\rvert^2\rangle = a^2$, the displacement after $N$ steps has mean $\boldsymbol{0}$ and

$$
\langle\lvert\boldsymbol{r}_N - \boldsymbol{r}_0\rvert^2\rangle = Na^2 = 2dDt, \qquad D = \frac{a^2}{2d\tau}, \quad t = N\tau,
$$
and for large $N$ each Cartesian component is approximately normally distributed with variance $2Dt$.

**Proof** The mean vanishes because each step has mean zero. Squaring the sum,

$$
\left\lvert\sum_{i=1}^{N}\Delta\boldsymbol{r}_i\right\rvert^2 = \sum_{i=1}^{N}\lvert\Delta\boldsymbol{r}_i\rvert^2 + \sum_{i \ne j}\Delta\boldsymbol{r}_i\cdot\Delta\boldsymbol{r}_j ,
$$
and by independence $\langle\Delta\boldsymbol{r}_i\cdot\Delta\boldsymbol{r}_j\rangle = \langle\Delta\boldsymbol{r}_i\rangle\cdot\langle\Delta\boldsymbol{r}_j\rangle = 0$ for $i \ne j$, so only the $N$ diagonal terms remain. Each component is a sum of $N$ independent identically distributed variables, and the **central limit theorem** ([3.1.13](/3.1.13)) gives the normal limit; by symmetry each of the $d$ components carries $a^2/d$ per step, a variance $Na^2/d = 2Dt$. $\square$

The square root is the essence of diffusion: the typical distance grows as $\sqrt{t}$, so to go ten times further takes a hundred times longer. The constant that connects distance and time is the property that experiments measure.

**Definition 5.1.2 (Diffusion Coefficient)** The **diffusion coefficient** of a particle is

$$
D = \lim_{t \to \infty}\frac{\langle\lvert\boldsymbol{r}(t) - \boldsymbol{r}(0)\rvert^2\rangle}{2dt},
$$
where $d$ is the number of dimensions in which the particle moves; its SI unit is $\mathrm{m^2\,s^{-1}}$, and in cell biology it is usually quoted in $\mu\mathrm{m^2\,s^{-1}}$.

The **mean squared displacement** (MSD, [7.3.2](/7.3.2)) of a tracked particle therefore grows as $2Dt$ in one dimension, $4Dt$ in two and $6Dt$ in three; deviations from linear growth reveal confinement, crowding or directed motion ([7.6.12](/7.6.12), [7.6.23](/7.6.23)). The figure shows that the central limit theorem works quickly: after only ten steps of fixed length the distribution of a coordinate is already close to Gaussian.

![Random walks in two dimensions with steps of length a in a random direction every τ, so that ⟨r²⟩ = Na² = 4Dt with D = a²/4τ. A: five walks of 1000 steps from the origin; the dashed circle has radius √N a. B: mean squared displacement averaged over 2000 walkers (dots), and the time-averaged MSD of three single walks (thin lines), against Na²; single trajectories scatter around the ensemble line, more so at long lags where fewer independent intervals are available. C: distribution of the x coordinate, scaled by √N a, after 10 and 400 steps, compared with the Gaussian of variance 1/2 predicted by the central limit theorem](./plots/random-walk.py)

### 5.1.2. Correlated Steps

If successive steps are correlated, the walk still diffuses at long times, but with a different coefficient. Suppose each step has length $\ell$ and the cosine of the angle between consecutive steps has mean $\alpha$, independently of earlier steps; then $\langle\Delta\boldsymbol{r}_i\cdot\Delta\boldsymbol{r}_{i+k}\rangle = \ell^2\alpha^k$.

**Formula 5.1.1 (Persistent Random Walk)** For $N \gg 1/(1 - \alpha)$ steps,

$$
\langle\lvert\boldsymbol{r}_N - \boldsymbol{r}_0\rvert^2\rangle = N\ell^2 + 2\ell^2\sum_{k=1}^{N-1}(N - k)\alpha^k \approx N\ell^2\frac{1 + \alpha}{1 - \alpha}, \qquad D = \frac{\ell^2}{2d\tau}\cdot\frac{1 + \alpha}{1 - \alpha}.
$$

Positive correlation ($\alpha > 0$, persistent motion) increases $D$; negative correlation ($\alpha < 0$, a restoring tendency) decreases it. The same mathematics describes the shape of a polymer: a chain of $N$ freely jointed segments of length $a$ is a random walk in space, so its end-to-end distance is $\sqrt{\langle R^2\rangle} = \sqrt{N}a$ (the freely jointed chain), and correlations between the directions of successive segments enlarge it by the factor of Formula 5.1.1 ([7.6.21](/7.6.21)).

**Example 5.1.1 (A swimming bacterium)** *E. coli* swims in straight runs at $v \approx 25\,\mu\mathrm{m\,s^{-1}}$ lasting about $\tau = 1\,\mathrm{s}$, separated by tumbles that reorient it by about $68^\circ$ on average, so $\alpha = \cos 68^\circ \approx 0.33$ (Berg and Brown, 1972). Treating each run as a step of $\ell = 25\,\mu\mathrm{m}$ in three dimensions, $D = (25^2/6)(1.33/0.67) \approx 2\times10^{2}\,\mu\mathrm{m^2\,s^{-1}}$. A swimming bacterium thus diffuses like a small molecule, a thousand times faster than a passive particle of its size ($D \approx 0.2\,\mu\mathrm{m^2\,s^{-1}}$ by Eq. (5.3) below). Chemotaxis biases this walk by lengthening runs up a gradient ([7.6.35](/7.6.35)).

### 5.1.3. Diffusion Times

Theorem 5.1.1 turns into the most useful estimate in cell physics: the time to diffuse a distance $L$ is

$$
t \approx \frac{L^2}{2dD}. \tag{5.1}
$$

Typical diffusion coefficients span six orders of magnitude.

| Molecule and medium | $D$ / ($\mu\mathrm{m^2\,s^{-1}}$) |
|---|---|
| $\ce{O2}$ in water, $25\,{}^\circ\mathrm{C}$ | $2\times10^{3}$ |
| Glucose in water | $6\times10^{2}$ |
| GFP ($27\,\mathrm{kDa}$) in water | $87$ |
| GFP in the cytoplasm of mammalian cells | $20$–$30$ |
| GFP in the cytoplasm of *E. coli* (Elowitz and colleagues, 1999) | $8$ |
| Lipid in a fluid bilayer | $1$ |
| Membrane protein in the plasma membrane | $0.01$–$0.1$ |
| mRNA–protein particle in *E. coli* (Golding and Cox, 2006) | $\sim 0.03$ |

A GFP molecule crosses a bacterium ($L = 1\,\mu\mathrm{m}$) in $1/(6 \times 8) \approx 0.02\,\mathrm{s}$ and a mammalian cell ($L = 20\,\mu\mathrm{m}$, $D = 25\,\mu\mathrm{m^2\,s^{-1}}$) in about $3\,\mathrm{s}$, but it would need $(10^6)^2/(6 \times 25)\,\mathrm{s} \approx 7\times10^{9}\,\mathrm{s}$, two centuries, to diffuse along a $1\,\mathrm{m}$ motor axon. Kinesin carrying cargo at $1\,\mu\mathrm{m\,s^{-1}}$ covers the same distance in $10^{6}\,\mathrm{s}$, about twelve days, and fast axonal transport is several times faster still. Directed transport at speed $v$ beats diffusion when $L/v < L^2/(6D)$, that is beyond $L^* = 6D/v$: about $150\,\mu\mathrm{m}$ for a protein carried at $1\,\mu\mathrm{m\,s^{-1}}$. Below this distance cells rely on diffusion; above it they need motors, cytoplasmic streaming or circulation. The same arithmetic explains why bacteria need no transport machinery, why large cells (eggs, neurons, plant cells) have it, and why an organism larger than about a millimeter needs a circulation.

![Spreading by diffusion. A: concentration profiles of molecules released at x = 0 at t = 0 in one dimension, for D = 25 µm² s⁻¹ (a GFP-sized protein in eukaryotic cytoplasm) at t = 0.1, 1, 10 and 30 s; the arrows mark ±√(2Dt), the standard deviation of the Gaussian. B: time to diffuse a distance L, t = L²/6D in three dimensions (L²/4D for the membrane protein in two), for a small molecule (D = 1000 µm² s⁻¹), a protein in the cytoplasm of a eukaryotic cell (25) and of *E. coli* (7.7) and a membrane protein (0.1), compared with directed transport at 1 µm s⁻¹ (a kinesin motor) and 30 µm s⁻¹ (a swimming bacterium); the dotted verticals mark the size of a protein, a bacterium, a eukaryotic cell and a 1 m axon](./plots/diffusion-times.py)

## 5.2. The Diffusion Equation

### 5.2.1. Conservation and Fick's Law

When many particles diffuse, their concentration $c(\boldsymbol{r}, t)$ obeys two laws. Conservation states that the number of particles in any volume changes only by flux through its surface, $\partial c/\partial t + \nabla\cdot\boldsymbol{J} = 0$. **Fick's law** ([2.5.1](/2.5.1)) states that the flux is proportional to the concentration gradient, $\boldsymbol{J} = -D\nabla c$, because more particles step from the crowded side than from the sparse side. A one-dimensional count makes the constant explicit: with $N(x)$ particles in a bin of width $a$ at $x$, half of each bin's particles step right and half step left in time $\tau$, so the net number crossing the boundary between bins is $[N(x) - N(x + a)]/2 \approx -\frac{a}{2}\partial_xN$, and dividing by $\tau$ and the cross-section gives $J = -(a^2/2\tau)\partial_xc = -D\partial_xc$, with the $D$ of Theorem 5.1.1. Combining the two laws gives the **heat equation** ([2.5.1](/2.5.1)), here the diffusion equation

$$
\frac{\partial c}{\partial t} = D\nabla^2c. \tag{5.2}
$$

**Formula 5.2.1 (Point Source)** If $N$ particles are released at the origin at $t = 0$ in unbounded $d$-dimensional space, then

$$
c(\boldsymbol{r}, t) = \frac{N}{(4\pi Dt)^{d/2}}\,\mathrm{e}^{-r^2/4Dt},
$$
the heat kernel of [2.5.7](/2.5.7), a Gaussian whose variance in each direction is $2Dt$.

The concentration field of many independent walkers is the probability density of one walker multiplied by their number: the macroscopic diffusion equation and the microscopic random walk are the same theory ([2.5.7](/2.5.7#sec-7.5.1)).

### 5.2.2. FRAP: Reading $D$ from a Recovery Curve

In **fluorescence recovery after photobleaching** ([7.3.2](/7.3.2#sec-2.6.1)) a region of a cell is bleached and the return of fluorescent molecules is followed. For an elongated cell, a bacterium or a neurite, a one-dimensional model is appropriate, and it has an exact solution that shows what the recovery curve contains.

**Formula 5.2.2 (One-Dimensional FRAP)** Let fluorescent molecules diffuse in $-L \le x \le L$ with reflecting ends, at uniform concentration $c_0$ until the strip $\lvert x\rvert < a$ is bleached at $t = 0$. Then

$$
c(x, t) = c_0\left[1 - \frac{a}{L} - \sum_{n=1}^{\infty}\frac{2}{n\pi}\sin\frac{n\pi a}{L}\cos\frac{n\pi x}{L}\,\mathrm{e}^{-Dn^2\pi^2t/L^2}\right],
$$
and the fluorescence of the bleached strip, relative to its prebleach value $2ac_0$, is

$$
\frac{F(t)}{F_{\mathrm{pre}}} = 1 - \frac{a}{L} - \sum_{n=1}^{\infty}\frac{2L}{a\,n^2\pi^2}\sin^2\frac{n\pi a}{L}\,\mathrm{e}^{-Dn^2\pi^2t/L^2}.
$$

**Proof** The no-flux conditions $\partial_xc = 0$ at $x = \pm L$ and the symmetry of the initial condition select the cosine modes $\cos(n\pi x/L)$, each of which decays under Eq. (5.2) as $\mathrm{e}^{-Dk_n^2t}$ with $k_n = n\pi/L$. The coefficients follow from the initial condition $c(x, 0) = c_0$ for $a < \lvert x\rvert \le L$ and $0$ for $\lvert x\rvert < a$: the mean is $A_0 = c_0(1 - a/L)$ and

$$
A_n = \frac{2}{L}\int_0^Lc(x, 0)\cos\frac{n\pi x}{L}\,\mathrm{d}x = \frac{2c_0}{L}\int_a^L\cos\frac{n\pi x}{L}\,\mathrm{d}x = -\frac{2c_0}{n\pi}\sin\frac{n\pi a}{L}.
$$
Integrating $c(x, t)$ over $\lvert x\rvert < a$, with $\int_{-a}^{a}\cos(n\pi x/L)\,\mathrm{d}x = (2L/n\pi)\sin(n\pi a/L)$, and dividing by $2ac_0$ gives $F/F_{\mathrm{pre}}$. At $t = 0$ the series sums to $1 - a/L$, by the identity $\sum_n\sin^2(n\theta)/n^2 = \theta(\pi - \theta)/2$ for $0 \le \theta \le \pi$, so that $F(0) = 0$ as required. $\square$

Three features of the formula matter in practice. The fluorescence recovers to $1 - a/L$, not to $1$, because the bleached molecules remain in the compartment; a smaller plateau than this indicates an immobile fraction. Each mode decays at the rate $Dn^2\pi^2/L^2$, so the time axis of the recovery curve scales as $1/D$ and $D$ can be read off by fitting (panel C of the figure). And the slowest mode, which sets the final approach to the plateau, is governed by the size of the compartment, $L^2/(\pi^2D)$, not by the size of the bleached region: in a small cell the geometry must be modeled, which is why the formula for a spot in an infinite membrane ([7.3.2](/7.3.2#sec-2.6.1)) does not apply to a bacterium.

A complementary method uses the fluctuations rather than a perturbation. In fluorescence correlation spectroscopy (FCS) a laser is focused to a volume of about $0.3\,\mu\mathrm{m}$ radius and $1\,\mathrm{fL}$, so small that only a few fluorescent molecules are inside at a time; as they diffuse in and out, the fluorescence fluctuates, and its autocorrelation function decays on the time $\tau_{\mathrm{D}} = w^2/4D$ that a molecule needs to cross the beam waist $w$. For a three-dimensional Gaussian volume with axial to lateral ratio $\omega$, $G(\tau) = \frac{1}{\langle N\rangle}\left(1 + \tau/\tau_{\mathrm{D}}\right)^{-1}\left(1 + \tau/\omega^2\tau_{\mathrm{D}}\right)^{-1/2}$: the decay time gives $D$ and the amplitude the mean number $\langle N\rangle$ of molecules in the volume, hence the absolute concentration. FRAP and FCS measure the same diffusion coefficient on different scales, FRAP by following the relaxation of a large perturbation, FCS by watching equilibrium fluctuations relax; that both work is a consequence of the fluctuation–dissipation theorem of 5.4. The derivation and the single-molecule methods built on FCS are in [7.6.12](/7.6.12).

![FRAP in one dimension. A compartment of length 2L = 10 µm with reflecting ends is uniformly fluorescent until the strip |x| < a = 1 µm (shaded) is bleached at t = 0. A: concentration profiles for D = 5 µm² s⁻¹ at t = 0, 0.02, 0.1, 0.5 and 2 s, from the Fourier series of Formula 5.2.2 with 400 terms. B: fluorescence of the bleached strip relative to its prebleach value for D = 1, 5 and 25 µm² s⁻¹ on a logarithmic time axis: the curves are translates of each other, and they level off at 1 − a/L = 0.8. C: synthetic recovery data for D = 5 µm² s⁻¹ with 3 % noise, fitted with the series: the fitted D agrees with the true value within its standard error](./plots/frap.py)

### 5.2.3. Diffusion to Capture

Many biological processes consist of molecules diffusing to an absorber: nutrients to a bacterium, oxygen to a mitochondrion, a ligand to a receptor, an enzyme to its substrate. The simplest case has a closed form, and it sets the scale of all the others.

**Formula 5.2.3 (Diffusion-Limited Flux to a Sphere)** A sphere of radius $a$ that absorbs every molecule reaching its surface, in a medium with concentration $c_0$ far away, has the steady-state concentration field and total flux

$$
c(r) = c_0\left(1 - \frac{a}{r}\right), \qquad J = 4\pi Dac_0 .
$$
A molecule released at distance $r_0 > a$ is eventually captured with probability $a/r_0$. A perfectly absorbing disk of radius $s$ on an otherwise reflecting plane receives $J = 4Dsc_0$.

**Proof** In a steady state $\nabla^2c = 0$; with spherical symmetry, $r^{-2}\,\mathrm{d}(r^2\,\mathrm{d}c/\mathrm{d}r)/\mathrm{d}r = 0$, so $c = B - A/r$. The conditions $c(\infty) = c_0$ and $c(a) = 0$ give $B = c_0$ and $A = c_0a$. The inward flux through the surface is $4\pi a^2D\,(\mathrm{d}c/\mathrm{d}r)_{r=a} = 4\pi Dac_0$. The capture probability $u(r_0)$ also satisfies $\nabla^2u = 0$ (a walker's chance of capture is the average of its chances after one step), with $u(a) = 1$ and $u(\infty) = 0$, so $u = a/r_0$. The result for the disk is the classical solution of the electrostatic problem of a charged disk, the capacitance of a disk being $8\varepsilon_0s$ instead of $4\pi\varepsilon_0a$ for a sphere; it is quoted. $\square$

The flux is proportional to the radius, not to the surface area: a sphere twice as large catches only twice as many molecules, because the concentration gradient near it is shallower. And a molecule released near an absorber is likely, but not certain, to be caught; in three dimensions a random walker escapes to infinity with probability $1 - a/r_0$, whereas in one and two dimensions it always returns. The analysis of how many receptor patches a cell needs to catch molecules almost as efficiently as a fully absorbing surface ($N \approx \pi a/s$ patches suffice for half the maximal flux) and of the precision with which a cell can measure a concentration is the subject of [7.6.35](/7.6.35).

**Example 5.2.1 (How large can a cell be?)** A spherical cell that consumes oxygen at a rate $q$ per unit volume needs $\frac43\pi R^3q \le 4\pi DRc_0$, so its radius cannot exceed $R_{\max} = \sqrt{3Dc_0/q}$ if oxygen reaches it by diffusion alone. An aerobically growing *E. coli* takes up about $15\,\mathrm{mmol}$ of $\ce{O2}$ per gram of dry mass per hour; with $0.3\,\mathrm{pg}$ of dry mass in $1\,\mu\mathrm{m^3}$ this is $q \approx 1\,\mathrm{mM\,s^{-1}}$ (about $7\times10^{5}$ molecules per second per cell). With $D = 2\times10^{-9}\,\mathrm{m^2\,s^{-1}}$ and air-saturated water ($c_0 = 0.25\,\mathrm{mM}$), $R_{\max} = \sqrt{3 \times 2\times10^{-9} \times 0.25/1}\,\mathrm{m} \approx 40\,\mu\mathrm{m}$: a bacterium is far from the limit, and the giant sulfur bacteria that exceed it fill most of their volume with a vacuole. Respiring tissue consumes less, about $0.03\,\mathrm{mM\,s^{-1}}$ for brain, but is supplied by blood whose dissolved oxygen is only about $0.13\,\mathrm{mM}$; then $R_{\max} \approx 150\,\mu\mathrm{m}$, which is why no cell of a metabolically active tissue lies more than about $100\,\mu\mathrm{m}$ from a capillary (Krogh's analysis, 1919).

The same formula gives the fastest possible rate of a bimolecular reaction. If molecules A and B of radii $a_{\mathrm{A}}$, $a_{\mathrm{B}}$ react on contact, then in the frame of A the molecules of B diffuse with the relative diffusion coefficient $D_{\mathrm{A}} + D_{\mathrm{B}}$ to a sphere of radius $a_{\mathrm{A}} + a_{\mathrm{B}}$, and the rate constant is $k = 4\pi(D_{\mathrm{A}} + D_{\mathrm{B}})(a_{\mathrm{A}} + a_{\mathrm{B}})N_{\mathrm{A}}$. With the Stokes–Einstein relation of 5.3 and $a_{\mathrm{A}} = a_{\mathrm{B}}$ this becomes $8RT/3\eta \approx 7\times10^{9}\,\mathrm{M^{-1}\,s^{-1}}$ in water at $25\,{}^\circ\mathrm{C}$, independent of size, the limit of a **diffusion-controlled reaction** ([6.3.17](/6.3.17)). Proteins associate more slowly, $10^5$–$10^7\,\mathrm{M^{-1}\,s^{-1}}$, because only a small patch of each surface is reactive and the molecules must also rotate into register; electrostatic steering can raise the rate above the uncharged estimate ([7.6.17](/7.6.17)).

![Diffusion to capture. A: steady-state concentration c(r)/c0 = 1 − a/r around a perfectly absorbing sphere of radius a (cross-section through its centre, contours at 0.25, 0.5 and 0.75); the depletion zone extends several radii, and the flux into the sphere, J = 4πDac0, grows with the radius rather than the area. B: probability that a molecule released at distance r0 is captured before it wanders beyond R = 50a: a walk-on-spheres Monte Carlo simulation (dots, 4000 molecules per distance; each step jumps to a random point on the largest sphere that touches no boundary, which samples Brownian paths exactly) against the exact result (1/r0 − 1/R)/(1/a − 1/R) and its limit a/r0. C: the largest radius of a spherical cell supplied with oxygen by diffusion alone, R_max = √(3Dc0/q), against the volumetric consumption rate q for D = 2000 µm² s⁻¹ and c0 = 0.25 mM (air-saturated water) or 0.13 mM (arterial plasma); an aerobic bacterium (about 1 mM s⁻¹) is far below the limit, and brain tissue (about 0.03 mM s⁻¹) reaches it at about 150 µm](./plots/capture.py)

### 5.2.4. Chase or Wait: The Péclet Number

Should a bacterium swim to collect food, or sit and let diffusion bring it? Swimming over a distance $L$ takes $L/v$; diffusion of the food over the same distance takes $L^2/D$. Their ratio is a dimensionless number that compares transport by motion or flow with transport by diffusion.

**Definition 5.2.1 (Péclet Number)** For transport over a length $L$ by a flow or motion of speed $v$ and by diffusion with coefficient $D$, the **Péclet number** is $\mathrm{Pe} = vL/D$. Advection dominates for $\mathrm{Pe} \gg 1$ and diffusion for $\mathrm{Pe} \ll 1$.

**Example 5.2.2** For *E. coli* swimming at $30\,\mu\mathrm{m\,s^{-1}}$ through a solution of a small nutrient with $D = 10^3\,\mu\mathrm{m^2\,s^{-1}}$, $\mathrm{Pe} = 1$ at $L = D/v \approx 30\,\mu\mathrm{m}$, fifteen body lengths. On the scale of the cell, $L = 1\,\mu\mathrm{m}$, $\mathrm{Pe} = 0.03$: swimming does not stir the fluid around the cell or increase the flux of nutrient to its surface appreciably, because diffusion replenishes the depleted zone faster than the cell can leave it (Purcell, 1977). Bacteria swim not to increase the local flux but to find regions where the concentration is higher, which requires crossing distances much larger than $30\,\mu\mathrm{m}$. The hydrodynamics behind this argument is the subject of [7.6.22](/7.6.22).

## 5.3. Diffusion in a Force Field

### 5.3.1. Drift, the Smoluchowski Equation and the Einstein Relation

A force $F$ acting on a particle in a viscous medium produces, after the velocity has relaxed, a steady drift velocity $F/\gamma$, where $\gamma$ is the friction coefficient (for a sphere of radius $a$, the Stokes value $\gamma = 6\pi\eta a$). A population then carries a drift flux $cF/\gamma$ in addition to the diffusive flux.

**Formula 5.3.1 (Smoluchowski Equation)** For particles with diffusion coefficient $D$ and friction coefficient $\gamma$ in a potential $U(x)$, with $F = -\mathrm{d}U/\mathrm{d}x$,

$$
\frac{\partial c}{\partial t} = -\frac{\partial J}{\partial x}, \qquad J = -D\frac{\partial c}{\partial x} + \frac{F}{\gamma}c = -D\,\mathrm{e}^{-U/k_{\mathrm{B}}T}\frac{\partial}{\partial x}\left(\mathrm{e}^{U/k_{\mathrm{B}}T}c\right),
$$
where the last form uses the Einstein relation below; it extends to three dimensions with $\nabla$ and to the probability density of one particle.

**Theorem 5.3.1 (Einstein Relation)** If diffusing particles in a potential reach the Boltzmann distribution at equilibrium, then

$$
D\gamma = k_{\mathrm{B}}T.
$$

**Proof** At equilibrium the flux vanishes everywhere, so $D\,\mathrm{d}c/\mathrm{d}x = cF/\gamma$. The Boltzmann distribution $c \propto \mathrm{e}^{-U/k_{\mathrm{B}}T}$ has $\mathrm{d}c/\mathrm{d}x = cF/k_{\mathrm{B}}T$. The two agree for every potential only if $D = k_{\mathrm{B}}T/\gamma$. $\square$

This is the **Einstein–Smoluchowski relation** of [6.3.21](/6.3.21), obtained there from sedimentation equilibrium. It states that a particle's random motion and its response to a force are not independent properties: both come from the same molecular collisions, and knowing one gives the other (5.4). With Stokes' friction it becomes the **Stokes–Einstein equation** ([6.3.17](/6.3.17))

$$
D = \frac{k_{\mathrm{B}}T}{6\pi\eta a}, \tag{5.3}
$$
which gives $D = 4.11\times10^{-21}/(6\pi \times 0.89\times10^{-3} \times 2.4\times10^{-9})\,\mathrm{m^2\,s^{-1}} = 1.0\times10^{2}\,\mu\mathrm{m^2\,s^{-1}}$ for a sphere of the radius of GFP in water at $25\,{}^\circ\mathrm{C}$, close to the measured $87\,\mu\mathrm{m^2\,s^{-1}}$. Since the volume of a globular protein is proportional to its mass, $D \propto M^{-1/3}$: a tenfold heavier protein diffuses only about twofold more slowly. The slower diffusion in cytoplasm (table in 5.1.3) reflects crowding and binding, not a higher viscosity of the water ([7.6.23](/7.6.23)), and the friction coefficients of nonspherical molecules are the basis of hydrodynamic methods ([7.6.8](/7.6.8)).

**Example 5.3.1 (The Nernst potential)** For an ion of charge $ze$ in an electric potential $\varphi$, $U = ze\varphi$, and the zero-flux condition across a membrane permeable only to this ion gives $c_{\mathrm{in}}/c_{\mathrm{out}} = \mathrm{e}^{-ze(\varphi_{\mathrm{in}} - \varphi_{\mathrm{out}})/k_{\mathrm{B}}T}$, the **Nernst equation** ([6.3.13](/6.3.13))

$$
\varphi_{\mathrm{in}} - \varphi_{\mathrm{out}} = \frac{k_{\mathrm{B}}T}{ze}\ln\frac{c_{\mathrm{out}}}{c_{\mathrm{in}}}.
$$
A tenfold concentration ratio of a monovalent ion corresponds to $26.7\,\mathrm{mV} \times \ln 10 = 61\,\mathrm{mV}$ at $37\,{}^\circ\mathrm{C}$ ($59\,\mathrm{mV}$ at $25\,{}^\circ\mathrm{C}$). For $\ce{Na+}$, about ten times more concentrated outside a neuron, the equilibrium potential is about $+61\,\mathrm{mV}$ (inside positive). The Smoluchowski equation with an electric force is the Nernst–Planck equation, from which the Goldman–Hodgkin–Katz equation for several permeant ions is derived in [7.6.30](/7.6.30).

### 5.3.2. Rotational Diffusion

A molecule also tumbles. Its orientation, a unit vector $\boldsymbol{u}$, performs a random walk on the unit sphere, and the orientational memory decays exponentially.

**Definition 5.3.1 (Rotational Diffusion)** **Rotational diffusion** is the random reorientation of a molecule by thermal collisions, described by a rotational diffusion coefficient $D_{\mathrm{r}}$ (unit $\mathrm{rad^2\,s^{-1}}$, usually written $\mathrm{s^{-1}}$) such that a small rotation angle about any axis has variance $2D_{\mathrm{r}}t$, and $D_{\mathrm{r}} = k_{\mathrm{B}}T/\gamma_{\mathrm{r}}$, where $\gamma_{\mathrm{r}}$ is the rotational friction coefficient.

**Formula 5.3.2 (Rotational Diffusion of a Sphere)** For a sphere of radius $a$, $\gamma_{\mathrm{r}} = 8\pi\eta a^3$ and $D_{\mathrm{r}} = k_{\mathrm{B}}T/8\pi\eta a^3$. The orientation correlation functions are

$$
\langle\boldsymbol{u}(t)\cdot\boldsymbol{u}(0)\rangle = \mathrm{e}^{-2D_{\mathrm{r}}t}, \qquad \langle P_2(\boldsymbol{u}(t)\cdot\boldsymbol{u}(0))\rangle = \mathrm{e}^{-6D_{\mathrm{r}}t},
$$
with $P_2(x) = (3x^2 - 1)/2$, and the rotational correlation time measured by fluorescence anisotropy and NMR relaxation is $\tau_{\mathrm{rot}} = 1/6D_{\mathrm{r}} = \eta V/k_{\mathrm{B}}T$, where $V = \frac43\pi a^3$.

The two correlation functions decay differently because they are the first and second spherical harmonics of the orientation, which relax with rates $l(l + 1)D_{\mathrm{r}}$ for $l = 1$ and $2$. Rotational and translational diffusion depend differently on size: translation as $1/a$, rotation as $1/a^3$. A protein of radius $2.5\,\mathrm{nm}$ in water at $25\,{}^\circ\mathrm{C}$ has $\tau_{\mathrm{rot}} = 0.89\times10^{-3} \times 6.5\times10^{-26}/4.11\times10^{-21}\,\mathrm{s} = 14\,\mathrm{ns}$, and its orientation is randomized in tens of nanoseconds, which sets the time window of fluorescence anisotropy ([7.6.11](/7.6.11)) and the line widths of NMR ([7.6.13](/7.6.13)). For the bacterium of Example 5.1.1 ($a \approx 1\,\mu\mathrm{m}$), $1/D_{\mathrm{r}} = 8\pi\eta a^3/k_{\mathrm{B}}T \approx 5\,\mathrm{s}$: Brownian rotation alone would randomize its direction within seconds, so runs much longer than this would be useless, and a bacterium cannot hold a straight course for more than about ten seconds whatever it does (Berg and Purcell, 1977).

Molecules that must meet in a particular orientation are slowed by the need to rotate into register: for the diffusion-limited association of 5.2.3 the reactive patches must find each other, and the rate constant falls by the fraction of the surfaces that is reactive, partly compensated by repeated collisions within the same encounter.

## 5.4. The Langevin Equation

### 5.4.1. Friction and Noise

The diffusion equation describes probabilities; the motion of one particle is described by Newton's equation with the force of the solvent split into a systematic and a random part.

**Definition 5.4.1 (Langevin Equation)** The **Langevin equation** for a particle of mass $m$ in one dimension is

$$
m\frac{\mathrm{d}v}{\mathrm{d}t} = -\gamma v + F(x) + \xi(t), \qquad \langle\xi(t)\rangle = 0, \quad \langle\xi(t)\xi(t')\rangle = \Gamma\,\delta(t - t'),
$$
where $-\gamma v$ is the friction of the solvent, $F(x)$ an external force, and the random force $\xi(t)$ is **white noise**: a stationary Gaussian process whose values at different times are uncorrelated and whose power spectrum is therefore flat.

The friction and the noise are both averages over the same molecular collisions, and their strengths cannot be independent. Equipartition fixes the relation.

**Theorem 5.4.1 (Fluctuation–Dissipation Relation for the Langevin Equation)** For a free particle ($F = 0$) described by Definition 5.4.1 to reach thermal equilibrium at temperature $T$, the noise strength must be

$$
\Gamma = 2\gamma k_{\mathrm{B}}T .
$$
In equilibrium the velocity autocorrelation function is $\langle v(t)v(0)\rangle = (k_{\mathrm{B}}T/m)\,\mathrm{e}^{-\gamma\lvert t\rvert/m}$, the mean squared displacement is

$$
\langle[x(t) - x(0)]^2\rangle = 2Dt - 2D\frac{m}{\gamma}\left(1 - \mathrm{e}^{-\gamma t/m}\right), \qquad D = \int_0^\infty\langle v(t)v(0)\rangle\,\mathrm{d}t = \frac{k_{\mathrm{B}}T}{\gamma},
$$
ballistic, $\langle x^2\rangle \approx (k_{\mathrm{B}}T/m)t^2$, for $t \ll m/\gamma$ and diffusive for $t \gg m/\gamma$.

**Proof** The solution of the linear equation is $v(t) = v(0)\mathrm{e}^{-\gamma t/m} + \frac1m\int_0^t\mathrm{e}^{-\gamma(t - s)/m}\xi(s)\,\mathrm{d}s$. Using the correlation of the noise,

$$
\langle v(t)^2\rangle = \langle v(0)^2\rangle\mathrm{e}^{-2\gamma t/m} + \frac{\Gamma}{m^2}\int_0^t\mathrm{e}^{-2\gamma(t - s)/m}\,\mathrm{d}s \to \frac{\Gamma}{2m\gamma} \quad (t \to \infty).
$$
Equipartition requires $\frac12m\langle v^2\rangle = \frac12k_{\mathrm{B}}T$, so $\Gamma = 2\gamma k_{\mathrm{B}}T$. Multiplying the solution started at $v(0)$ by $v(0)$ and averaging (the noise after time $0$ is independent of $v(0)$) gives the exponential correlation function. Finally $x(t) - x(0) = \int_0^tv(s)\,\mathrm{d}s$, so $\langle[x(t) - x(0)]^2\rangle = \int_0^t\int_0^t\langle v(s)v(s')\rangle\,\mathrm{d}s\,\mathrm{d}s' = 2\int_0^t(t - u)\langle v(u)v(0)\rangle\,\mathrm{d}u$, which evaluates to the stated expression; its long-time slope $2\int_0^\infty\langle v(u)v(0)\rangle\,\mathrm{d}u$ is $2k_{\mathrm{B}}T/\gamma$. $\square$

The theorem derives the Einstein relation a second time, from the dynamics of one particle rather than from the equilibrium of a population, and the formula $D = \int_0^\infty\langle v(t)v(0)\rangle\,\mathrm{d}t$ (a Green–Kubo relation) holds for any equilibrium dynamics, not only for the Langevin model. The time $m/\gamma$ over which velocity is remembered is very short in water: for a protein of $50\,\mathrm{kDa}$ ($m = 8.3\times10^{-23}\,\mathrm{kg}$, $\gamma = 6\pi\eta a = 4\times10^{-11}\,\mathrm{kg\,s^{-1}}$) it is $2\,\mathrm{ps}$, and for a bead of $1\,\mu\mathrm{m}$ diameter about $70\,\mathrm{ns}$. A swimming bacterium that stops its motors coasts for less than a microsecond and over less than a tenth of a nanometer. On all biological time scales inertia is irrelevant, and the Langevin equation is used in its overdamped form, $\gamma\,\mathrm{d}x/\mathrm{d}t = F(x) + \xi(t)$.

The relation between noise and friction is a special case of a general principle.

**Definition 5.4.2 (Fluctuation–Dissipation Theorem)** The **fluctuation–dissipation theorem** states that, for a system in thermal equilibrium, the linear response of a variable $x$ to a weak force $f$ conjugate to it is determined by the spontaneous equilibrium fluctuations of $x$: in classical systems the power spectrum of the fluctuations, $S_x(\omega) = \int_{-\infty}^{\infty}\langle x(t)x(0)\rangle\mathrm{e}^{\mathrm{i}\omega t}\,\mathrm{d}t$, and the response function $\chi(\omega) = \hat x(\omega)/\hat f(\omega)$ satisfy

$$
S_x(\omega) = \frac{2k_{\mathrm{B}}T}{\omega}\operatorname{Im}\chi(\omega).
$$

The theorem is the basis of passive microrheology: watching a bead fluctuate in a material gives the material's viscoelastic response without pushing on it. A system that violates it is not in equilibrium. In living cells, beads and vesicles fluctuate far more at low frequencies than the measured mechanical response predicts, because motors stir the cytoplasm; comparing active and passive measurements quantifies these active forces ([7.6.23](/7.6.23)). Cells also need to break the equilibrium link between response and fluctuation for function: a sensor or motor that should respond strongly but fluctuate little must be driven out of equilibrium ([7.6.38](/7.6.38)).

### 5.4.2. A Particle in a Harmonic Trap

The overdamped Langevin equation with a linear restoring force is the prototype of every measurement with a trapped particle, from optical tweezers to a fluctuating membrane.

**Definition 5.4.3 (Ornstein–Uhlenbeck Process)** The **Ornstein–Uhlenbeck process** is the solution of $\gamma\,\mathrm{d}x/\mathrm{d}t = -\kappa x + \xi(t)$ with white noise of strength $2\gamma k_{\mathrm{B}}T$: a diffusing particle bound to the origin by a spring of stiffness $\kappa$, with relaxation time $\tau = \gamma/\kappa$.

**Formula 5.4.1 (Trapped Brownian Particle)** For the Ornstein–Uhlenbeck process, a particle started at $x(0) = 0$ has $\langle x(t)^2\rangle = (k_{\mathrm{B}}T/\kappa)(1 - \mathrm{e}^{-2t/\tau})$. In equilibrium,

$$
\langle x(t)x(0)\rangle = \frac{k_{\mathrm{B}}T}{\kappa}\mathrm{e}^{-\lvert t\rvert/\tau}, \qquad
\langle[x(t) - x(0)]^2\rangle = \frac{2k_{\mathrm{B}}T}{\kappa}\left(1 - \mathrm{e}^{-t/\tau}\right), \qquad
S_x(\omega) = \frac{2\gamma k_{\mathrm{B}}T}{\kappa^2 + \gamma^2\omega^2}.
$$

At short times ($t \ll \tau$) the particle diffuses freely, $\langle[x(t) - x(0)]^2\rangle \approx 2(k_{\mathrm{B}}T/\gamma)t$; at long times its excursions saturate at the equipartition value $\langle x^2\rangle = k_{\mathrm{B}}T/\kappa$. The power spectrum is a Lorentzian with corner frequency $f_{\mathrm{c}} = \kappa/2\pi\gamma$; with $\chi(\omega) = 1/(\kappa - \mathrm{i}\omega\gamma)$ it satisfies Definition 5.4.2 exactly, as one checks by computing $\operatorname{Im}\chi$.

**Example 5.4.1 (Calibrating an optical trap)** A bead of radius $0.5\,\mu\mathrm{m}$ in water ($\gamma = 6\pi\eta a = 8.4\times10^{-9}\,\mathrm{N\,s\,m^{-1}}$) held in a trap of stiffness $\kappa = 0.05\,\mathrm{pN\,nm^{-1}}$ fluctuates with standard deviation $\sqrt{k_{\mathrm{B}}T/\kappa} = \sqrt{4.1/0.05}\,\mathrm{nm} = 9\,\mathrm{nm}$ and relaxation time $\tau = \gamma/\kappa = 0.17\,\mathrm{ms}$, a corner frequency of $0.95\,\mathrm{kHz}$. Either the variance (equipartition) or the corner frequency of the power spectrum gives $\kappa$; their agreement checks the calibration ([7.6.17](/7.6.17)). To resolve the $8\,\mathrm{nm}$ steps of kinesin ([7.3.14](/7.3.14)) the bead's thermal motion must be reduced by a stiff trap or by averaging over times longer than $\tau$.

![Langevin dynamics (overdamped in A and B, units with γ = kBT = 1). A: trajectory of a free particle and of a particle in a harmonic trap of stiffness κ = 1 (relaxation time τ = γ/κ = 1; the shaded band is ±√(kBT/κ)). B: mean squared displacement from x(0) = 0, averaged over 1000 particles (dots), compared with 2Dt for the free particle and (kBT/κ)(1 − e^−2t/τ) in the trap: both start diffusively, but the trapped particle saturates at the equipartition value kBT/κ. C: with inertia, particles started at rest gain kinetic energy from the noise; the mean kinetic energy settles at kBT/2 only when the noise strength is 2γkBT (Theorem 5.4.1); with half or twice that strength the "temperature" of the particles is wrong (simulation, solid; theory, dashed)](./plots/langevin.py)

## 5.5. Master Equations and the Fokker–Planck Equation

### 5.5.1. The Master Equation

The probability description of a stochastic system with discrete states, a particle hopping between lattice sites, a channel switching between conformations, a motor stepping along a filament or a gene producing molecules, is the master equation.

**Definition 5.5.1 (Master Equation)** For a system with discrete states $i$ and transition rates $w_{ij}$ from state $j$ to state $i$, the **master equation** for the probabilities $p_i(t)$ is

$$
\frac{\mathrm{d}p_i}{\mathrm{d}t} = \sum_{j \ne i}\left(w_{ij}p_j - w_{ji}p_i\right),
$$
the balance of the probability flows into and out of each state.

The master equation describes a continuous-time **Markov chain** ([3.5.9](/3.5.9)): the future depends only on the present state. Its stationary solutions satisfy $\sum_j(w_{ij}p_j - w_{ji}p_i) = 0$ for every $i$; in thermal equilibrium each term vanishes separately, $w_{ij}p_j^{\mathrm{eq}} = w_{ji}p_i^{\mathrm{eq}}$, which is **detailed balance**, and requires $w_{ij}/w_{ji} = \mathrm{e}^{-(G_i - G_j)/k_{\mathrm{B}}T}$ (Eq. (4.2) of [7.6.4](/7.6.4)). A stationary state with nonzero net flows around cycles is a nonequilibrium steady state, the regime of motors and of every process driven by ATP ([7.6.38](/7.6.38)). The two-state channel of [7.6.4](/7.6.4) is the smallest example; the chemical master equation for numbers of molecules is developed in [7.6.32](/7.6.32).

### 5.5.2. From Hops to Drift and Diffusion

A particle on a one-dimensional lattice of spacing $a$ that hops right with rate $k_+$ and left with rate $k_-$ obeys

$$
\frac{\partial p(x, t)}{\partial t} = k_+p(x - a, t) + k_-p(x + a, t) - (k_+ + k_-)p(x, t).
$$
Expanding $p(x \pm a, t)$ to second order in $a$,

$$
\frac{\partial p}{\partial t} = -v\frac{\partial p}{\partial x} + D\frac{\partial^2p}{\partial x^2}, \qquad v = a(k_+ - k_-), \quad D = \frac{a^2(k_+ + k_-)}{2},
$$
a drift–diffusion equation whose coefficients are the mean and half the variance of the displacement per unit time. A biased hopper drifts and spreads at the same time; the ratio $2D/(va) = (k_+ + k_-)/(k_+ - k_-)$ (the randomness parameter) measures how far it is from deterministic stepping and is used to count the hidden steps of a motor's cycle ([7.6.27](/7.6.27)). The general form of such equations is the following.

**Definition 5.5.2 (Fokker–Planck Equation)** The **Fokker–Planck equation** for the probability density $p(x, t)$ of a continuous Markov process is

$$
\frac{\partial p}{\partial t} = -\frac{\partial}{\partial x}\left[A(x)p\right] + \frac12\frac{\partial^2}{\partial x^2}\left[B(x)p\right],
$$
with drift coefficient $A(x) = \lim_{\Delta t \to 0}\langle\Delta x\rangle/\Delta t$ and diffusion coefficient $B(x) = \lim_{\Delta t \to 0}\langle(\Delta x)^2\rangle/\Delta t$, the first two moments of the displacement in a short time starting from $x$.

With $A = F/\gamma$ and $B = 2D$ constant, it is the Smoluchowski equation (Formula 5.3.1). When $B$ depends on $x$, it stands inside the second derivative; writing $\partial_x[\frac12B\,\partial_xp]$ instead, as is sometimes done, adds a spurious drift $-\frac12B'(x)$ unless the noise is reinterpreted. For the Ornstein–Uhlenbeck process, $A = -\kappa x/\gamma$ and $B = 2D$, and the stationary solution is the Gaussian $p \propto \mathrm{e}^{-\kappa x^2/2k_{\mathrm{B}}T}$, the Boltzmann distribution of the spring. The mean obeys $\mathrm{d}\langle x\rangle/\mathrm{d}t = \langle A(x)\rangle$, which equals $A(\langle x\rangle)$ only for linear drift. The same equation, run backwards in time with the drift $\nabla\ln p$, is the principle of the generative diffusion models of machine learning ([4.7](/4.7)), which learn to reverse a process that turns data into noise.

## 5.6. First Passage and Barrier Crossing

### 5.6.1. Mean First-Passage Times

Many biological questions ask not where a particle is but when it first gets somewhere: when a transcription factor reaches its site, when a protein crosses its folding barrier, when a motor completes a step.

**Definition 5.6.1 (First-Passage Time)** The **first-passage time** of a stochastic process started at $x_0$ to a target set is the random time at which the process first enters the target.

**Theorem 5.6.1 (Mean First-Passage Time in One Dimension)** For overdamped motion with diffusion coefficient $D$ in a potential $U(x)$, started at $x_0$ between a reflecting boundary at $x_{\mathrm{r}}$ and an absorbing boundary at $x_{\mathrm{a}} > x_0$, the mean first-passage time to $x_{\mathrm{a}}$ is

$$
T(x_0) = \frac{1}{D}\int_{x_0}^{x_{\mathrm{a}}}\mathrm{d}y\,\mathrm{e}^{U(y)/k_{\mathrm{B}}T}\int_{x_{\mathrm{r}}}^{y}\mathrm{d}z\,\mathrm{e}^{-U(z)/k_{\mathrm{B}}T}.
$$

**Proof** Condition on the first short interval $\Delta t$: $T(x) = \Delta t + \langle T(x + \Delta x)\rangle$, with $\langle\Delta x\rangle = (F/\gamma)\Delta t$ and $\langle\Delta x^2\rangle = 2D\Delta t$. Expanding to first order in $\Delta t$ gives the backward equation $DT'' + (F/\gamma)T' = -1$, with $T(x_{\mathrm{a}}) = 0$ and $T'(x_{\mathrm{r}}) = 0$. With $F = -U'$ and $D\gamma = k_{\mathrm{B}}T$, the left side is $D\,\mathrm{e}^{\beta U}(\mathrm{e}^{-\beta U}T')'$, so $\mathrm{e}^{-\beta U(x)}T'(x) = -\frac1D\int_{x_{\mathrm{r}}}^{x}\mathrm{e}^{-\beta U(z)}\,\mathrm{d}z$; integrating once more from $x_0$ to $x_{\mathrm{a}}$ gives the formula. $\square$

For free diffusion from a reflecting wall at $0$ to an absorber at $L$, $T(0) = L^2/2D$, the one-dimensional version of Eq. (5.1); a particle starting at the centre of a sphere of radius $R$ reaches its surface after a mean time $R^2/6D$. With a constant force pushing towards the target the time falls towards $L/v$ once the Péclet number $vL/D$ exceeds one; with a force pushing away, it grows exponentially with the potential difference, which is the content of the next result.

### 5.6.2. Kramers' Rate

A molecule that has to change conformation, a protein unfolding, a channel opening or a ligand leaving its pocket, sits in a free-energy well and must be carried over a barrier by thermal fluctuations. Kramers (1940) computed the rate for a particle diffusing in a potential.

**Theorem 5.6.2 (Kramers Rate)** For overdamped diffusion in a potential with a minimum at $a$, a barrier top at $b$ and barrier height $\Delta U = U(b) - U(a) \gg k_{\mathrm{B}}T$, the rate of escape from the well is

$$
k = \frac{\sqrt{U''(a)\,\lvert U''(b)\rvert}}{2\pi\gamma}\,\mathrm{e}^{-\Delta U/k_{\mathrm{B}}T}.
$$

**Proof** Take the absorbing point beyond the barrier and $x_0 = a$ in Theorem 5.6.1. For a high barrier, the outer factor $\mathrm{e}^{\beta U(y)}$ is sharply peaked at the barrier top $b$, where the inner integral has already reached its full value, the integral of $\mathrm{e}^{-\beta U}$ over the well, sharply peaked at $a$. Approximating each exponent by its quadratic expansion (Laplace's method),

$$
\int_{\mathrm{well}}\mathrm{e}^{-\beta U(z)}\,\mathrm{d}z \approx \mathrm{e}^{-\beta U(a)}\sqrt{\frac{2\pi k_{\mathrm{B}}T}{U''(a)}}, \qquad
\int_{\mathrm{barrier}}\mathrm{e}^{\beta U(y)}\,\mathrm{d}y \approx \mathrm{e}^{\beta U(b)}\sqrt{\frac{2\pi k_{\mathrm{B}}T}{\lvert U''(b)\rvert}}.
$$
Then $T \approx (2\pi k_{\mathrm{B}}T/D)\,\mathrm{e}^{\beta\Delta U}/\sqrt{U''(a)\lvert U''(b)\rvert}$, and $k = 1/T$ with $D = k_{\mathrm{B}}T/\gamma$ gives the result. $\square$

The rate depends exponentially on the barrier, as in the **Arrhenius equation** ([6.3.17](/6.3.17)), and the barrier is the activation free energy. What Kramers adds is the prefactor: in the overdamped regime it is a curvature divided by the friction, not the universal frequency $k_{\mathrm{B}}T/h = 6.2\times10^{12}\,\mathrm{s^{-1}}$ of **transition state theory** ([6.3.16](/6.3.16)), which assumes that every crossing of the barrier top is final. In a viscous medium the system recrosses the barrier many times before committing, and the rate is smaller and inversely proportional to the friction. The rates of protein folding and of large conformational changes do decrease roughly in inverse proportion to the solvent viscosity when viscogens are added, and their prefactors are estimated at $10^6$–$10^8\,\mathrm{s^{-1}}$, which is why the folding of even the fastest proteins takes microseconds ([7.6.16](/7.6.16)). The Eyring prefactor is appropriate for bond rearrangements of small molecules, not for the motions of macromolecules in water.

**Example 5.6.1** A conformational transition with a barrier of $10\,k_{\mathrm{B}}T$ and a Kramers prefactor of $10^7\,\mathrm{s^{-1}}$ occurs at $10^7\mathrm{e}^{-10} = 450\,\mathrm{s^{-1}}$, a dwell time of about $2\,\mathrm{ms}$, in the range of channel gating ([7.6.4](/7.6.4)). With the transition-state prefactor the same barrier would give $3\times10^{8}\,\mathrm{s^{-1}}$. Each additional $k_{\mathrm{B}}T$ of barrier slows the transition $2.7$-fold, and $2.3\,k_{\mathrm{B}}T$ tenfold; doubling the viscosity halves the rate without changing the equilibrium.

The same picture extends to many coordinates: a protein's conformational dynamics is diffusion on a free-energy landscape over its configuration space, with basins as states and saddles as transition states, and folding is the special case of a funnelled landscape ([7.6.16](/7.6.16)). A force or a membrane potential that tilts the landscape lowers one barrier and raises the other, which is how the rates of channels depend on voltage and the lifetimes of bonds on force (the Bell model, [7.6.17](/7.6.17)); the ratio of forward and backward rates remains fixed by the free-energy difference of the end states, as detailed balance requires.

![Barrier crossing in the double well U(x) = ΔU(x² − 1)² (overdamped Langevin dynamics, γ = kBT = 1). A: the potential for ΔU = 4 kBT, with minima a at x = ±1 (curvature U'' = 8ΔU) and the barrier top b at x = 0 (U'' = −4ΔU). B: a trajectory for ΔU = 4 kBT: long dwells in each well separated by jumps that take a small fraction of the time, the behaviour that justifies a two-state description. C: escape rate, the inverse mean first-passage time from x = −1 to x = +1, from 400 simulated particles per barrier height (dots), from the exact first-passage integral of Theorem 5.6.1 (line) and from Kramers' formula (dashed); the rate falls exponentially with the barrier, and Kramers' approximation becomes accurate once the barrier exceeds a few kBT](./plots/kramers.py)

## Summary

| Topic | Key results |
|---|---|
| Random walk (Definition 5.1.1, Theorem 5.1.1) | $\langle r^2\rangle = Na^2 = 2dDt$, $D = a^2/2d\tau$; Gaussian by the central limit theorem |
| Diffusion coefficient (Definition 5.1.2, Formula 5.1.1, Example 5.1.1) | $D = \lim\langle r^2\rangle/2dt$; persistence multiplies $D$ by $(1 + \alpha)/(1 - \alpha)$; swimming *E. coli* $D \approx 200\,\mu\mathrm{m^2\,s^{-1}}$ |
| Diffusion times (Eq. (5.1), table in 5.1.3) | $t \approx L^2/2dD$; GFP crosses a bacterium in $0.02\,\mathrm{s}$, a 1 m axon in centuries; motors win beyond $L^* = 6D/v$ |
| Diffusion equation (Eq. (5.2), Formula 5.2.1) | Conservation + Fick's law, $\partial_tc = D\nabla^2c$; point source $N(4\pi Dt)^{-d/2}\mathrm{e}^{-r^2/4Dt}$ |
| FRAP (Formula 5.2.2) | Cosine series; plateau $1 - a/L$; time scales as $1/D$; slowest mode $L^2/\pi^2D$ set by the compartment |
| Capture (Formula 5.2.3, Example 5.2.1) | $c = c_0(1 - a/r)$, $J = 4\pi Dac_0$ (disk $4Dsc_0$); capture probability $a/r_0$; $R_{\max} = \sqrt{3Dc_0/q}$; $k_{\mathrm{D}} = 8RT/3\eta \approx 7\times10^9\,\mathrm{M^{-1}\,s^{-1}}$ |
| Péclet number (Definition 5.2.1, Example 5.2.2) | $\mathrm{Pe} = vL/D$; a bacterium does not outrun diffusion below about $30\,\mu\mathrm{m}$ |
| Drift and diffusion (Formula 5.3.1, Theorem 5.3.1, Eq. (5.3)) | $J = -D\partial_xc + cF/\gamma$; $D\gamma = k_{\mathrm{B}}T$; $D = k_{\mathrm{B}}T/6\pi\eta a$; Nernst $61\,\mathrm{mV}$ per decade at $37\,{}^\circ\mathrm{C}$ |
| Rotation (Definition 5.3.1, Formula 5.3.2) | $D_{\mathrm{r}} = k_{\mathrm{B}}T/8\pi\eta a^3$; $\tau_{\mathrm{rot}} = 1/6D_{\mathrm{r}} = \eta V/k_{\mathrm{B}}T \approx 14\,\mathrm{ns}$ for $a = 2.5\,\mathrm{nm}$ |
| Langevin (Definition 5.4.1, Theorem 5.4.1, Definition 5.4.2) | Noise $2\gamma k_{\mathrm{B}}T$; $\langle v(t)v(0)\rangle = (k_{\mathrm{B}}T/m)\mathrm{e}^{-\gamma t/m}$; $D = \int\langle vv\rangle\,\mathrm{d}t$; $m/\gamma \sim$ ps–ns; $S_x = (2k_{\mathrm{B}}T/\omega)\operatorname{Im}\chi$ |
| Trap (Definition 5.4.3, Formula 5.4.1, Example 5.4.1) | $\langle x^2\rangle = k_{\mathrm{B}}T/\kappa$, $\tau = \gamma/\kappa$, Lorentzian with $f_{\mathrm{c}} = \kappa/2\pi\gamma$ |
| Master and Fokker–Planck equations (Definitions 5.5.1–5.5.2) | Probability balance; hopping gives $v = a(k_+ - k_-)$, $D = a^2(k_+ + k_-)/2$; drift $A$ and diffusion $B$ from the first two moments |
| First passage and Kramers (Definition 5.6.1, Theorems 5.6.1–5.6.2, Example 5.6.1) | Double-integral MFPT; free: $L^2/2D$; $k = \sqrt{U''_aU''_b}\,\mathrm{e}^{-\Delta U/k_{\mathrm{B}}T}/2\pi\gamma$, $\propto 1/\eta$; prefactor $10^6$–$10^8\,\mathrm{s^{-1}}$ for proteins |

## Questions

1. GFP diffuses with $D = 8\,\mu\mathrm{m^2\,s^{-1}}$ in *E. coli* and an mRNA–protein particle with $D = 0.03\,\mu\mathrm{m^2\,s^{-1}}$. How long does each take to travel the $2\,\mu\mathrm{m}$ length of the cell (treat this as one-dimensional diffusion)? What does the result imply for where the proteins encoded by an mRNA are made relative to the gene?

   **Answer** $t = L^2/2D$: GFP $4/16 = 0.25\,\mathrm{s}$; the mRNA particle $4/0.06 \approx 67\,\mathrm{s}$, comparable to the lifetime of a bacterial mRNA (a few minutes). Proteins spread through the cell within a second, but an mRNA stays near the place where it was transcribed during much of its life, so translation is localized near the nucleoid region of its gene; in bacteria, transcription and translation are coupled in space as well as time ([7.2.18](/7.2.18)).

2. Estimate the diffusion coefficient and the rotational correlation time of a globular protein of $100\,\mathrm{kDa}$ in water at $25\,{}^\circ\mathrm{C}$ ($\eta = 0.89\,\mathrm{mPa\,s}$, protein density $1.35\,\mathrm{g\,cm^{-3}}$). How would hydration change the estimate?

   **Answer** Volume $V = M/\rho N_{\mathrm{A}} = 10^5/(1.35 \times 6.02\times10^{23})\,\mathrm{cm^3} = 1.23\times10^{-19}\,\mathrm{cm^3} = 1.23\times10^{-25}\,\mathrm{m^3}$, radius $a = (3V/4\pi)^{1/3} = 3.1\,\mathrm{nm}$. $D = k_{\mathrm{B}}T/6\pi\eta a = 4.11\times10^{-21}/(6\pi \times 0.89\times10^{-3} \times 3.1\times10^{-9}) = 7.9\times10^{-11}\,\mathrm{m^2\,s^{-1}} = 79\,\mu\mathrm{m^2\,s^{-1}}$; $\tau_{\mathrm{rot}} = \eta V/k_{\mathrm{B}}T = 0.89\times10^{-3} \times 1.23\times10^{-25}/4.11\times10^{-21} = 27\,\mathrm{ns}$. A hydration shell of about $0.3\,\mathrm{nm}$ and deviations from a sphere increase the hydrodynamic radius by $10$–$20\,\%$, lowering $D$ by the same fraction and raising $\tau_{\mathrm{rot}}$ by $30$–$70\,\%$ (it scales as $a^3$); measured values for proteins of this size are about $60\,\mu\mathrm{m^2\,s^{-1}}$ and $40\,\mathrm{ns}$ ([7.6.8](/7.6.8)).

3. In a FRAP experiment on a bacterium of length $2L = 4\,\mu\mathrm{m}$, a strip of width $2a = 1\,\mu\mathrm{m}$ at the centre is bleached. (a) To what fraction of its prebleach value does the strip recover if all molecules are mobile? (b) The final approach to the plateau is exponential with time constant $0.1\,\mathrm{s}$. What is $D$? (c) If the plateau is only $0.6$, what fraction of the molecules is immobile?

   **Answer** (a) $1 - a/L = 1 - 0.5/2 = 0.75$. (b) The slowest mode decays with rate $D\pi^2/L^2$, so $D = L^2/(\pi^2 \times 0.1\,\mathrm{s}) = 4/(9.87 \times 0.1) = 4.1\,\mu\mathrm{m^2\,s^{-1}}$. (c) If a fraction $f$ is immobile, the bleached immobile molecules never recover and the mobile ones recover to $(1 - f)(1 - a/L)$ of their share; setting $(1 - f) \times 0.75 = 0.6$ gives $f = 0.2$ (neglecting the small depletion of the mobile pool caused by bleaching of the immobile molecules).

4. A spherical cell of radius $R$ consumes oxygen uniformly at rate $q$ per unit volume. (a) Show that if $R > R_{\max} = \sqrt{3Dc_0/q}$ the surface flux cannot keep up. (b) Inside a cell that is not oxygen-limited, the concentration also falls from the surface towards the centre; solve $D\nabla^2c = q$ with $c(R) = c_0$ and find the condition for $c(0) > 0$. Compare with (a).

   **Answer** (a) The diffusive supply to a perfect absorber is at most $4\pi DRc_0$ and the demand is $\frac43\pi R^3q$; supply $\ge$ demand gives $R^2 \le 3Dc_0/q$. (b) The spherically symmetric solution is $c(r) = c_0 - q(R^2 - r^2)/6D$, so $c(0) = c_0 - qR^2/6D > 0$ requires $R < \sqrt{6D_{\mathrm{in}}c_0/q}$ with the internal diffusion coefficient $D_{\mathrm{in}}$. The two limits differ by a factor $\sqrt2$ and by which diffusion coefficient enters: the outside supply and the inside distribution both limit size, and for the same $D$ the external supply is the more stringent.

5. Using the Nernst equation, calculate the equilibrium potential of $\ce{K+}$ for $140\,\mathrm{mM}$ inside and $5\,\mathrm{mM}$ outside at $37\,{}^\circ\mathrm{C}$, and explain why this follows from the Einstein relation without any knowledge of the channel.

   **Answer** $\varphi_{\mathrm{in}} - \varphi_{\mathrm{out}} = (k_{\mathrm{B}}T/e)\ln(c_{\mathrm{out}}/c_{\mathrm{in}}) = 26.7\,\mathrm{mV} \times \ln(5/140) = 26.7 \times (-3.33) = -89\,\mathrm{mV}$. At equilibrium the drift flux driven by the field and the diffusive flux driven by the concentration gradient cancel; their ratio involves $D$ and the mobility $D/k_{\mathrm{B}}T$ only through the Einstein relation, so the channel's permeability (which multiplies both) drops out. Equilibrium properties are independent of kinetics; the permeabilities matter only when several ions carry current (the GHK equation, [7.6.30](/7.6.30)).

6. An optical trap holds a bead whose position has a standard deviation of $10\,\mathrm{nm}$ at $25\,{}^\circ\mathrm{C}$. (a) What is the trap stiffness? (b) For a bead of radius $0.5\,\mu\mathrm{m}$ in water, what is the corner frequency of the power spectrum? (c) With what precision can the bead's mean position be measured by averaging for $10\,\mathrm{ms}$?

   **Answer** (a) $\kappa = k_{\mathrm{B}}T/\langle x^2\rangle = 4.11/100 = 0.041\,\mathrm{pN\,nm^{-1}}$. (b) $\gamma = 8.4\times10^{-9}\,\mathrm{N\,s\,m^{-1}} = 8.4\times10^{-6}\,\mathrm{pN\,s\,nm^{-1}}$, $f_{\mathrm{c}} = \kappa/2\pi\gamma = 0.041/(2\pi \times 8.4\times10^{-6}) = 780\,\mathrm{Hz}$, $\tau = 0.2\,\mathrm{ms}$. (c) Samples separated by more than about $2\tau$ are nearly independent; $10\,\mathrm{ms}$ contains about $10/(2 \times 0.2) = 25$ independent samples, so the standard error is $10/\sqrt{25} = 2\,\mathrm{nm}$ (exactly, the variance of the time average of an Ornstein–Uhlenbeck process is $2\langle x^2\rangle\tau/T_{\mathrm{av}}$ for $T_{\mathrm{av}} \gg \tau$, which gives $10 \times \sqrt{0.4/10} = 2\,\mathrm{nm}$).

7. A protein's unfolding is a barrier crossing with rate $1\,\mathrm{s^{-1}}$ in water. (a) Glycerol is added until the viscosity is three times higher. What rate does Kramers theory predict if the barrier is unchanged? (b) A mutation raises the barrier by $1.4\,k_{\mathrm{B}}T$. What is the new rate in water? (c) Why are both experiments, viscosity and mutation, needed to interpret a folding rate?

   **Answer** (a) In the overdamped regime $k \propto 1/\gamma \propto 1/\eta$: $0.33\,\mathrm{s^{-1}}$ (in practice glycerol also stabilizes proteins, so the barrier must be corrected using the stability measured in the same solvent). (b) $\mathrm{e}^{-1.4} = 0.25$, so $0.25\,\mathrm{s^{-1}}$. (c) A rate is a prefactor times a Boltzmann factor. The viscosity dependence tests whether the dynamics is diffusive and gives access to the prefactor (and to internal friction, if the dependence is weaker than $1/\eta$), while mutations change the barrier; φ-value analysis uses this to map the structure of the transition state ([7.6.16](/7.6.16)).

8. Show from Theorem 5.6.1 that free diffusion from a reflecting wall at $0$ to an absorber at $L$ takes a mean time $L^2/2D$. Then add a constant force $F$ towards the absorber and show that the mean time tends to $L/v$, with $v = F/\gamma$, when $\mathrm{Pe} = vL/D \gg 1$.

   **Answer** With $U = 0$, $T(0) = \frac1D\int_0^L\mathrm{d}y\int_0^y\mathrm{d}z = L^2/2D$. With $U = -Fx$, $\beta U = -vx/D$, and $T(0) = \frac1D\int_0^L\mathrm{e}^{-vy/D}\frac{D}{v}(\mathrm{e}^{vy/D} - 1)\,\mathrm{d}y = \frac{L}{v} - \frac{D}{v^2}(1 - \mathrm{e}^{-vL/D})$. For $\mathrm{Pe} \gg 1$ the second term is $L/v \cdot (1/\mathrm{Pe})$, negligible, so $T \to L/v$; for $\mathrm{Pe} \ll 1$, expanding the exponential to second order gives back $L^2/2D$.

9. (Concept) Explain why a random walker in three dimensions released next to an absorbing sphere may never return, while in one dimension it always returns. What does this imply for a ligand that dissociates from a receptor on a cell surface?

   **Answer** The capture probability $u$ is a harmonic function equal to $1$ on the absorber. In three dimensions $u = a/r_0$ decays to zero at infinity, so the escape probability $1 - a/r_0$ is finite; in one dimension the harmonic functions are linear, and the only bounded one equal to $1$ at the absorber is $u = 1$ (in two dimensions $u$ varies logarithmically and the walk is also recurrent). A ligand that dissociates from a receptor on a cell of radius $a$ starts essentially at $r_0 = a$ and is very likely to hit the cell again; if the surface carries many receptors it may rebind many times before escaping. This rebinding increases the apparent residence time of ligands on cells and affects the precision of concentration sensing ([7.6.35](/7.6.35)).

10. (Design) You want to know whether vesicles in a cell move by diffusion or are carried by motors. Describe how to decide from single-particle trajectories, and what result you would expect for each.

    **Answer** Track many vesicles at a frame rate fast enough to resolve their motion (say $20\,\mathrm{ms}$) and compute the mean squared displacement against lag time ([7.3.2](/7.3.2)). Diffusion gives $\mathrm{MSD} = 4Dt$ in the image plane (slope $1$ on a log–log plot); motor transport gives $\mathrm{MSD} \approx 4Dt + v^2t^2$ (slope approaching $2$) at lags beyond $4D/v^2$, and directed runs show velocity correlations between successive steps; confinement gives a plateau. Further tests: depolymerizing microtubules or depleting ATP should abolish directed runs; the distribution of displacements is Gaussian for diffusion and has long tails for intermittent transport. In living cells MSDs often grow with intermediate exponents because of crowding and active stirring, which must be distinguished from transport by these controls ([7.6.23](/7.6.23)).
