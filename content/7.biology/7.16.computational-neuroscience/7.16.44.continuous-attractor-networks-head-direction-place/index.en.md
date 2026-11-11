---
title: "Continuous Attractor Networks: Head Direction, Place and Grid"
description: "Population codes for continuous variables; continuous attractor neural networks with Mexican-hat or local-excitation, global-inhibition connectivity; the stationary bump and its analytic solution; the spectrum of the interaction kernel, motion modes, diffusion and the M-shaped correlation signature; moving the bump and path integration; the head direction ring of the fly; two-dimensional networks for place and grid cells; a multi-ring model of context switching in CA3; adaptation, traveling waves, oscillatory tracking, theta sweeps and anticipative tracking."
---

The discrete attractors of [7.16.43](/7.16.43) store items: a face, a word, an episode. Many variables the brain must hold are continuous: the direction the head points, the position of the body in a room, the location of a remembered target, the orientation of an edge. A network that stores a continuous variable needs a continuum of stable states, one for each value, arranged so that neighboring values are neighboring states. Such continuous attractors can be built from a simple, translation-invariant connectivity, and they have properties that discrete attractors lack: the stored value can be moved smoothly by an input, which makes the network an integrator of velocity, and it drifts under noise, which limits the precision of memory. This chapter develops the theory of continuous attractor neural networks (CANNs) and its evidence: the head direction system, where a ring attractor has been observed almost literally in the fly, the place and grid cells of the hippocampal formation ([7.16.42](/7.16.42#sec-42.4)), and the dynamics that adaptation adds, traveling waves, theta sweeps and the anticipation of moving stimuli. The rate-network tools come from [7.16.15](/7.16.15), the population codes and decoders from [7.16.26](/7.16.26), the toroidal manifold of grid cells from [7.16.28](/7.16.28#sec-28.5); the oculomotor integrator, a line attractor, is treated in [7.16.33](/7.16.33), and the use of continuous attractors as a working memory in [7.16.45](/7.16.45).

## 44.1. Continuous Variables and Population Codes

A head direction cell ([Definition 42.4.2](/7.16.42#def-42.4.2)) has a bell-shaped **tuning curve** around its preferred direction $z_i$,
$$
r_i(x) = A\exp\Bigl(-\frac{d(x, z_i)^2}{2a^2}\Bigr), \tag{44.1}
$$
where $d$ is the distance on the circle and $a$ the tuning width. Because many cells with different preferred directions tile the circle, the direction is represented by a **population code**: if the cells are arranged by preferred direction, the population activity at any moment is a localized hill whose position is the current direction. Such hills are decoded by the **population vector**, the center of mass of the activities on the circle, or by maximum likelihood ([7.16.26](/7.16.26)). The same scheme represents the direction of arm movements in motor cortex (Georgopoulos et al., 1986), the remembered location of a target in prefrontal cortex ([7.16.45](/7.16.45)) and, for cells tuned to the views of a familiar object in inferotemporal cortex, the viewing angle (Logothetis, Pauls and Poggio, 1995).

For a memory the hill must persist when the input disappears, and it must be able to sit at any position. A network whose stationary states are hills at all positions, with no preferred one, does both. Two requirements follow. The excitatory and inhibitory interactions must be balanced so that a localized hill sustains itself without spreading or dying; and the connections must be *translation invariant*, depending only on the difference of preferred values, so that a hill at one position can be shifted to any other without changing its stability.

## 44.2. The Activity Bump

### 44.2.1. Mexican-Hat Connectivity

The classical construction (Amari, 1977; Ben-Yishai, Bar-Or and Sompolinsky, 1995; Zhang, 1996) arranges neurons by preferred value $x$ and connects them with weights that are excitatory between neurons with similar preferences and inhibitory between neurons with different preferences, for example the difference of two Gaussians
$$
w(x - x') = k_{\mathrm{ex}}\mathrm{e}^{-(x - x')^2/2\sigma_{\mathrm{ex}}^2} - k_{\mathrm{in}}\mathrm{e}^{-(x - x')^2/2\sigma_{\mathrm{in}}^2}, \qquad k_{\mathrm{ex}} > k_{\mathrm{in}},\ \sigma_{\mathrm{ex}} < \sigma_{\mathrm{in}}, \tag{44.2}
$$
whose shape gives it the name "Mexican hat". Local excitation recruits neighbors into the hill, and broader inhibition keeps it from spreading; in the limit $\sigma_{\mathrm{in}} \to \infty$ the inhibition becomes global, proportional to the total activity, which is the version used below. The difference-of-Gaussians form is the same as the center–surround receptive field of the retina and the **lateral inhibition** of sensory maps, now applied to recurrent connections.

**Definition 44.2.1 (Continuous Attractor Neural Network)** A **continuous attractor neural network** (CANN) is a recurrent network whose stationary states form a continuous manifold, each point of which is a stable state against perturbations that leave the manifold and neutrally stable along it; with translation-invariant connections $w(x - x')$ on a space of preferred values, the stationary states are localized hills of activity, *activity bumps*, at all positions. When the preferred values lie on a circle, the network is a **ring attractor**; on a line, a line attractor; on a plane or torus, a two-dimensional CANN.

### 44.2.2. An Analytically Solvable Model

A model whose bump can be found in closed form uses Gaussian excitation and divisive global inhibition (Deneve, Latham and Pouget, 1999; Wu, Hamaguchi and Amari, 2008), a form of **divisive normalization** ([7.16.23](/7.16.23)).

**Formula 44.2.1 (CANN with Divisive Global Inhibition)** Let $u(x, t)$ be the synaptic input and $r(x, t)$ the firing rate of the neurons with preferred value $x$, with density $\rho$. Then
$$
\tau\frac{\partial u(x, t)}{\partial t} = -u(x, t) + \rho\int w(x - x')\,r(x', t)\,\mathrm{d}x' + I_{\mathrm{ext}}(x, t), \qquad r(x, t) = \frac{[u(x, t)]_+^2}{1 + k\rho\int[u(x', t)]_+^2\,\mathrm{d}x'}, \tag{44.3}
$$
with excitatory kernel $w(x) = \frac{J_0}{\sqrt{2\pi}\,a}\mathrm{e}^{-x^2/2a^2}$, global inhibition strength $k$ and time constant $\tau$ of a few milliseconds.

**Proposition 44.2.1 (Stationary Bump)** Without external input, and with $x$ ranging over an interval much longer than $a$, Eq. (44.3) has, for every $z$, the stationary solution
$$
\bar u(x \mid z) = U_0\,\mathrm{e}^{-(x - z)^2/4a^2}, \qquad \bar r(x \mid z) = R_0\,\mathrm{e}^{-(x - z)^2/2a^2}, \qquad U_0 = \frac{J_0\bigl(1 + \sqrt{1 - k/k_{\mathrm{c}}}\bigr)}{4\sqrt{\pi}\,a\,k}, \quad R_0 = \frac{\sqrt2\,U_0}{\rho J_0}, \tag{44.4}
$$
which exists if and only if $k \le k_{\mathrm{c}} = \rho J_0^2/(8\sqrt{2\pi}\,a)$.

**Proof** Insert $u = U_0\mathrm{e}^{-x^2/4a^2}$ (take $z = 0$). Then $\int u^2\,\mathrm{d}x = U_0^2\sqrt{2\pi}\,a$, so $r = R_0\mathrm{e}^{-x^2/2a^2}$ with $R_0 = U_0^2/B$, $B = 1 + k\rho\sqrt{2\pi}\,aU_0^2$. The convolution of two Gaussians gives $\rho\int w(x - x')R_0\mathrm{e}^{-x'^2/2a^2}\,\mathrm{d}x' = \frac{\rho J_0R_0}{\sqrt2}\mathrm{e}^{-x^2/4a^2}$, which has the same shape as $u$: the ansatz is consistent if $U_0 = \rho J_0R_0/\sqrt2 = \rho J_0U_0^2/(\sqrt2B)$, that is $k\rho\sqrt{2\pi}\,aU_0^2 - \frac{\rho J_0}{\sqrt2}U_0 + 1 = 0$. This quadratic has real roots if and only if $\rho^2J_0^2/2 \ge 4k\rho\sqrt{2\pi}\,a$, i.e. $k \le k_{\mathrm{c}}$, and the larger root is $U_0$ in Eq. (44.4). Since the equation is invariant under $x \to x - z$, every shifted bump is also a solution. $\square$

The bump persists after the input that created it is removed, and its position $z$ is a free parameter: the network has a one-parameter family of attractors, a line (or, on a ring, a circle) in its $N$-dimensional state space. Inhibition limits the amplitude, and if it is too strong ($k > k_{\mathrm{c}}$) no bump exists and the network returns to silence: memory requires that recurrent excitation be strong enough relative to inhibition. The smaller root of the quadratic is an unstable bump, the threshold that an input must exceed to ignite the memory.

![A ring CANN (Formula 44.2.1, discretized on 256 neurons with $a = 0.3\,\mathrm{rad}$, $k = 1$, time in units of $\tau$). A: firing rates against preferred value and time. A stimulus at $x = 0$ creates a bump that persists after the stimulus is removed at $t = 50\tau$ (dotted line). A weak stimulus that appears at $x = -1.5$ at $t = 150\tau$ and then moves (dashed line) attracts the bump, which moves to it and tracks it. B: the stationary bump without input (dots) and the profile of Proposition 44.2.1 (line). C: path integration: adding to the weights an antisymmetric component $-\gamma\,w'(x - x')$, a rotation signal of strength $\gamma$, makes the bump move without input at a speed proportional to $\gamma$ (here equal to $\gamma$ radians per $\tau$, because $w(d) - \gamma w'(d) \approx w(d - \gamma)$ shifts the kernel by $\gamma$).](./plots/cann-bump.py)

A simulation needs only the discretized form of Eq. (44.3):

```python
import numpy as np

N, tau, a, k, dt = 256, 1.0, 0.3, 1.0, 0.1
x = -np.pi + 2 * np.pi * np.arange(N) / N
d = np.angle(np.exp(1j * (x[:, None] - x[None, :])))   # distance on the ring
W = np.exp(-d**2 / (2 * a**2)) / (np.sqrt(2 * np.pi) * a)

u = np.zeros(N)
for step in range(5000):
    t = step * dt
    I = 0.5 * np.exp(-np.angle(np.exp(1j * x))**2 / (4 * a**2)) if t < 50 else 0.0
    u2 = np.maximum(u, 0) ** 2
    r = u2 / (1 + k * u2.sum())                  # divisive global inhibition
    u += dt / tau * (-u + W @ r + I)
z = np.angle(np.sum(r * np.exp(1j * x)))         # decoded bump position
```

## 44.3. Theory of the Bump: Modes, Noise and Signatures

### 44.3.1. The Spectrum of Perturbations

The stability of the bump follows from linearization. A small perturbation $\delta u(x)$ of the stationary state obeys
$$
\tau\frac{\partial\,\delta u(x)}{\partial t} = -\delta u(x) + \int F(x, x')\,\delta u(x')\,\mathrm{d}x', \qquad F(x, x') = \rho\int w(x - x'')\frac{\partial\bar r(x'')}{\partial\bar u(x')}\,\mathrm{d}x'', \tag{44.5}
$$
and its eigenfunctions $v_n$ with eigenvalues $\lambda_n$ of the kernel $F$ decay with time constants $\tau/(1 - \lambda_n)$; the bump is stable if all $\lambda_n < 1$. For the model of Formula 44.2.1, the eigenfunctions are, to good approximation, the bump multiplied by Hermite polynomials, the wave functions of the quantum harmonic oscillator (Fung, Wong and Wu, 2010), and they have an intuitive meaning as *motion modes* of the bump:

| Mode | Eigenfunction | Eigenvalue | Meaning |
|---|---|---|---|
| $n = 0$ | $\propto\bar u(x)$ | $< 1$ | Change of height, decays |
| $n = 1$ | $\propto\partial\bar u/\partial z$ | exactly $1$ | Shift of position, neutral |
| $n \ge 2$ | Higher Hermite functions | $\approx 2^{1-n}$ | Changes of width and shape, decay quickly |

The eigenvalue $\lambda_1 = 1$ is exact: differentiating the stationary equation with respect to $z$ shows that $\partial\bar u/\partial z$ solves the linearized equation with zero decay. This neutral direction is the continuous attractor itself, the tangent to the line of fixed points. All other modes decay, and the higher ones quickly. The dynamics of a CANN is therefore dominated by a few modes, and projecting it onto the position mode reduces the $N$-dimensional network to a one-dimensional equation for the bump position $z(t)$. With an external input of strength $\alpha$ centered at $z_0$, the projection gives (Wu, Hamaguchi and Amari, 2008)
$$
\tau\frac{\mathrm{d}z}{\mathrm{d}t} = -\kappa\alpha\,(z - z_0)\,\mathrm{e}^{-(z - z_0)^2/8a^2} + \xi(t), \tag{44.6}
$$
with a constant $\kappa$ and a noise term $\xi$: the input pulls the bump toward itself with a force that is linear for small displacements and vanishes for distant inputs, which is why the bump in the figure jumps to a nearby stimulus but would ignore a distant one, and why the network behaves as a robust estimator that discounts outliers.

### 44.3.2. Diffusion, Drift and Precision

Without input the restoring force vanishes and Eq. (44.6) is a random walk: noise in the neurons, which in a network of $N$ spiking neurons is of order $1/\sqrt N$ per unit, makes the bump diffuse along the attractor with a diffusion coefficient proportional to $1/N$ (Burak and Fiete, 2012). A memory stored in a CANN therefore degrades with time as $\operatorname{Var}(z) = Dt$, the standard deviation growing as $\sqrt t$, a prediction that matches the growth of errors with delay in spatial working memory ([7.16.45](/7.16.45)). Imperfections of the connectivity, any breaking of translation invariance, add systematic drift toward a few preferred positions: the continuous attractor becomes a set of discrete attractors with shallow barriers between them. The need for precise symmetry is the main theoretical objection to CANNs, as the need for precise tuning ($\lambda = 1$) is for line attractors ([7.16.15](/7.16.15#sec-15.2)); learning rules that keep the connectivity homogeneous, the large number of neurons, and the anchoring of the bump to sensory landmarks are the proposed answers.

### 44.3.3. The Correlation Signature

How can one recognize a CANN in recorded data? Because noise moves the bump as a whole, the fluctuations of different neurons are correlated in a characteristic way. If the bump at position $z$ shifts by $\delta z$, the rate of a neuron with preferred value $x$ changes by $\delta r(x) \approx -\bar r'(x - z)\,\delta z \propto (x - z)\mathrm{e}^{-(x - z)^2/2a^2}\,\delta z$, so the covariance of two neurons at $x$ and $y$ is
$$
\operatorname{Cov}\bigl(r(x), r(y)\bigr) \propto (x - z)(y - z)\,\mathrm{e}^{-(x - z)^2/2a^2}\mathrm{e}^{-(y - z)^2/2a^2}. \tag{44.7}
$$
Neurons on the same side of the bump fluctuate together, neurons on opposite sides in opposition. As a function of the stored value $z$, the correlation of a fixed pair of neurons is positive when $z$ lies outside the pair, negative when it lies between their preferred values: an M-shaped curve. These are **information-limiting correlations** ([Definition 26.5.2](/7.16.26#def-26.5.2)) along the direction of a shift of the stimulus, which no decoder can average away. The M-shaped pattern was found in pairs of prefrontal neurons during the delay of a spatial working memory task (Wimmer, Nykamp, Constantinidis and Compte, 2014), where moreover the drift of the bump predicted the direction of the monkey's errors, and in area MT during motion viewing (Ponce-Alvarez, Thiele, Albright, Stoner and Deco, 2013).

## 44.4. Moving the Bump: Path Integration and the Head Direction Ring

### 44.4.1. Path Integration

A head direction system must update its estimate when the head turns, also in darkness.

**Definition 44.4.1 (Path Integration)** **Path integration** (dead reckoning) is the estimation of one's current position or heading by integrating self-motion signals, linear and angular velocity from the vestibular system, proprioception and motor efference copies, over time, without reference to external landmarks.

A CANN integrates naturally. A velocity input that is excitatory on one flank of the bump and inhibitory on the other pushes the bump sideways at a speed proportional to the input. In the classical model (Skaggs, Knierim, Kudrimoti and McNaughton, 1995; Zhang, 1996), two populations of "rotation" cells are conjunctive for head direction and angular velocity, and each projects back onto the ring with connections offset in one direction; the offset adds an antisymmetric component to the effective weights, and the bump moves at a speed set by the angular velocity signal. Since $w(d - \gamma) \approx w(d) - \gamma w'(d)$, an antisymmetric component of strength $\gamma$ shifts the bump by $\gamma$ per time constant (figure in Section 44.2, C), and if $\gamma$ is proportional to angular velocity, the bump position is the integral of velocity. Landmark inputs, acting as in Eq. (44.6), correct the accumulating error.

### 44.4.2. The Fly's Head Direction Ring

The most direct evidence for a ring attractor comes from the central complex of *Drosophila*. Seelig and Jayaraman (2015) imaged with **calcium imaging** the "E-PG" (compass) neurons, whose processes tile the ring-shaped ellipsoid body in 16 wedges, in head-fixed flies walking on a ball in a virtual-reality arena. At any moment a single bump of activity occupied one or two adjacent wedges; its position rotated as the fly turned, tracking the fly's heading relative to a visual landmark, and it persisted and kept rotating with the fly's turns in darkness, with gradual drift: path integration with error. The ring of neurons in the brain matches the ring of the model: the anatomy is laid out as the state space.

Kim, Rouault, Druckmann and Jayaraman (2017) then tested the attractor properties directly. Optogenetic stimulation of E-PG neurons at a wedge away from the bump created a new bump there, and the old bump disappeared: only one bump can exist, as global inhibition requires. The new bump persisted after the stimulation ended and was updated by the fly's turns as the natural bump was. When stimulation was weak and close to the bump, the bump moved to it smoothly; when distant, it jumped. Comparison with models favored local excitation and global inhibition over the Mexican hat. Green et al. (2017) and Turner-Evans et al. (2017) identified the integrator: "P-EN" neurons in the protocerebral bridge receive angular-velocity input and project onto the ellipsoid body with an offset of one wedge, clockwise for one hemisphere and counterclockwise for the other, exactly the offset connections of the model; turning one way activates one population, which pushes the bump in the corresponding direction. The complete wiring diagram from the hemibrain connectome (Hulse et al., 2021) confirmed the ring structure, the offsets and the inhibitory interneurons that provide global inhibition.

In rodents, the head direction cells of the anterodorsal thalamus keep their relative preferred directions in sleep, when there is no head turning (Peyrache, Lacroix, Petersen and Buzsáki, 2015), and the population activity in both wake and sleep lies on a one-dimensional ring, found by nonlinear dimensionality reduction (Chaudhuri, Gerçek, Pandey, Peyrache and Fiete, 2019): the ring is an intrinsic property of the circuit, not imposed by the input. Anterior thalamic cells anticipate the future head direction by about $25\,\mathrm{ms}$, whereas postsubicular cells encode the current direction (Blair and Sharp, 1995), a property explained in Section 44.7.

## 44.5. Two-Dimensional Networks: Place and Grid Cells

A CANN on a two-dimensional sheet, with neurons arranged by preferred location and connected by local excitation and broader inhibition, has a stationary bump at every location of the plane. Samsonovich and McNaughton (1997) proposed such a network as a model of the hippocampal place map: each environment is a "chart", an arrangement of the place cells on a sheet according to the positions of their fields, and different environments are different random charts stored in the same recurrent weights. Path integration moves the bump on the active chart, and the multiple charts explain global remapping ([7.16.42](/7.16.42#sec-42.4)) as a switch between attractors. Recurrent excitation strong enough for this exists in CA3 but hardly in CA1, so the model places the attractor in CA3 or upstream.

Grid cells suggested a different solution. If the connectivity on the sheet is a Mexican hat whose inhibition dominates at intermediate distances, the uniform state becomes unstable at a nonzero spatial frequency: linearizing a rate network $\tau\dot{\boldsymbol{r}} = -\boldsymbol{r} + F(W\boldsymbol{r} + \boldsymbol{h})$ around the uniform state, a perturbation $\mathrm{e}^{\mathrm{i}\boldsymbol{q}\cdot\boldsymbol{x}}$ grows when $F'\hat w(q) > 1$, where $\hat w$ is the Fourier transform of the kernel, so the fastest-growing wavelength is $2\pi/q^*$ with $q^*$ the maximum of $\hat w$. With rectifying neurons, the nonlinearity selects a superposition of three plane waves at $60^\circ$, a hexagonal pattern of bumps, the same structure as Formula 42.4.1 (Fuhs and Touretzky, 2006; Burak and Fiete, 2009). The pattern lives on the neural sheet; velocity inputs, through neurons with offset connections as in the head direction ring, move it, and each neuron, at a fixed position on the sheet, then fires whenever a bump of the moving pattern passes over it, at locations that form a triangular lattice in space. This is a **Turing pattern**, the same instability that generates periodic patterns in morphogenesis ([7.5.12](/7.5.12#sec-12.3)), here in neural activity rather than in chemical concentrations.

The model makes predictions that have been confirmed. The cells of a module must share spacing and orientation, since they are driven by the same pattern, and their phase relations must be invariant across environments and in sleep, since they are set by the connectivity (Yoon et al., 2013; Gardner et al., 2019). With periodic boundary conditions the neural sheet is a torus, and the population activity of a module lies on a two-dimensional torus, as topological data analysis of hundreds of simultaneously recorded grid cells showed (Gardner et al., 2022; [7.16.28](/7.16.28#sec-28.5)). Discrete modules with different spacings would then be separate attractor networks.

## 44.6. Context Switching in CA3: A Multi-Ring Model

The intracellular recordings of Zhao, Wang, Spruston and Magee (2020) in CA3 of mice running on a virtual linear track allow a more detailed test of attractor dynamics in the hippocampus. The membrane potential of a CA3 cell showed, besides its place field, a broad subthreshold depolarization by visual cues along the track, which produced firing only when the cell was near the current position of the activity bump. When a cue was shifted along the track, the place field followed it only if the shift was small; and when the virtual environment was switched (a "teleport" between two contexts), the population switched abruptly between two maps.

A model with three assumptions reproduces these observations:

1. Several attractor rings (one per familiar context) are stored in the same population; each neuron has a place field on each ring at an unrelated position, and the excitatory weights are the superposition of the ring connectivities, as in the charts of Section 44.5.
2. Inhibition is global, proportional to the summed rate of all pyramidal cells, and it enforces a single bump on a single ring.
3. The visual input is weak but broad: alone it is subthreshold, and it can drive a neuron to fire only together with recurrent excitation from an existing bump.

Assumption 3 explains why cue responses are gated by the bump: visual input biases where the bump sits but cannot create firing elsewhere. A small shift of a cue moves the bump with it, by the restoring force of Eq. (44.6); a large shift places the input outside the reach of the bump and is ignored. At a context switch, the visual input of the new context no longer matches the active ring; the bump shrinks, total activity falls, and because inhibition is proportional to total activity, the network is disinhibited. The weak input then ignites a bump on the ring that it matches, and the old one dies out. In the language of the energy landscape, the well of the old attractor becomes shallow through disinhibition and the system settles in the new well, which deepens as its bump grows. The model also answers the question of how a weak, subthreshold input can ever start a bump: through the global disinhibition that follows the collapse of the old one.

## 44.7. Adaptation: Traveling Waves, Oscillatory Tracking and Anticipation

### 44.7.1. The Adaptive CANN

Neurons adapt: their firing rate declines during sustained stimulation through calcium-activated potassium currents and other slow mechanisms, **spike-frequency adaptation** ([7.16.8](/7.16.8)). Adding adaptation to a CANN destabilizes the stationary bump, because the neurons at its center are the ones most suppressed, and gives the network an intrinsic mobility.

**Formula 44.7.1 (Adaptive CANN)** The adaptive CANN adds to Eq. (44.3) a slow negative feedback $V(x, t)$ that follows the synaptic input with time constant $\tau_v \gg \tau$ and strength $m$:
$$
\tau\frac{\partial u}{\partial t} = -u + \rho\int w(x - x')\,r(x', t)\,\mathrm{d}x' - V + I_{\mathrm{ext}}, \qquad \tau_v\frac{\partial V}{\partial t} = -V + m\,u, \tag{44.8}
$$
that is, $V(x, t) = \frac{m}{\tau_v}\int_{-\infty}^{t}\mathrm{e}^{-(t - t')/\tau_v}u(x, t')\,\mathrm{d}t'$ (Mi, Fung, Wong and Wu, 2014).

The same equations describe other slow negative feedbacks, such as short-term synaptic depression ([7.16.12](/7.16.12)) or inhibitory feedback from another layer. Their behavior depends on the competition between adaptation, which pushes the bump away from where it has been, and the external input, which pins it (figure below).

**Definition 44.7.1 (Traveling Wave)** A **traveling wave** in a CANN is a bump that moves along the attractor at constant speed without external drive, because adaptation suppresses the activity where the bump has been and the bump escapes toward unadapted neurons.

Without input, the stationary bump becomes unstable and a traveling wave appears when the adaptation is strong enough relative to its slowness, $m > \tau/\tau_v$; the speed of the wave increases slowly with $m\tau_v/\tau$. Fluctuating adaptation strength turns the regular wave into a walk with occasional long jumps, a Lévy flight, which is a more efficient search strategy than Brownian motion when targets are sparse (Dong et al., 2021); trajectories decoded from hippocampal replay events in rats contain such jumps (Pfeiffer and Foster, 2015). With a moving input of intermediate strength, the bump neither escapes nor follows smoothly: it oscillates around the stimulus, running ahead of it, falling back and running ahead again (oscillatory tracking); with a strong input it tracks smoothly.

![The three dynamical regimes of the adaptive CANN (Formula 44.7.1; 256 neurons on a ring, $a = 0.3$, $k = 1$, $\tau_v = 50\tau$); left, firing rate against preferred value and time; right, the bump position or its displacement from the stimulus. A: traveling wave ($m = 0.9$, weak input $\alpha = 0.03$ at $x = 0$, removed at $t = 30\tau$): once adaptation has built up, the bump moves on its own at a constant speed of about $0.05\,\mathrm{rad}$ per $\tau$, wrapping around the ring. B: oscillatory tracking ($m = 0.334$, $\alpha = 0.2$, stimulus moving slowly at $0.0012\,\mathrm{rad}$ per $\tau$, white dots): the bump sweeps back and forth around the stimulus with an amplitude of about $0.35\,\mathrm{rad}$ and a period of about $80\tau$. C: smooth tracking ($m = 0.05$, $\alpha = 0.2$, speed $0.004$): after a transient the bump follows the stimulus with a constant small lead.](./plots/adaptive-cann.py)

### 44.7.2. Theta Sweeps and Phase Precession

Oscillatory tracking offers a mechanism for the theta-timescale dynamics of the hippocampus ([7.16.42](/7.16.42#sec-42.5)). If the place-cell map is a CANN with adaptation, driven by the animal's position, the bump sweeps from behind the animal to ahead of it and back at a frequency set by the adaptation and the input strength. Decoded from place cells, such theta sweeps are observed: within each theta cycle the decoded position moves from behind the animal to ahead of it (Foster and Wilson, 2007), sweeping alternately into future and past paths (Wang, Foster and Pfeiffer, 2020), and in the entorhinal grid system the sweeps alternate left and right of the direction of travel from one cycle to the next (Vollan, Gardner, Moser and Moser, 2025). A single cell sees the bump pass over it at progressively earlier phases of each forward sweep as the animal moves through its field: phase precession; the backward part of the sweep produces the weaker phase procession reported in some recordings (Chu et al., 2024). In this view, phase precession, theta sequences and the lookahead used in planning are consequences of the same oscillatory dynamics of an adaptive attractor.

**Definition 44.7.2 (Theta Sweep)** A **theta sweep** is the movement, within one cycle of the theta rhythm, of the position decoded from a population of place or grid cells from behind the animal's current location to ahead of it.

### 44.7.3. Anticipative Tracking

Neural signals are slow. Visual signals reach V1 about $50\,\mathrm{ms}$ after an event, enough for a tennis ball served at $200\,\mathrm{km\,h^{-1}}$ to travel almost $3\,\mathrm{m}$. A representation that merely followed its input would always lag behind a moving object. In a CANN without adaptation, the bump indeed lags a moving input by a constant time; with adaptation, the trailing side of the bump is suppressed more than the leading side, which pushes the bump forward, and the lag decreases and becomes a lead.

**Definition 44.7.3 (Anticipative Tracking)** **Anticipative tracking** is the representation of a moving stimulus at a position ahead of its current input, so that the neural estimate leads the delayed sensory signal and compensates, partly or fully, for transmission delays.

In the simulation below, a bump that lags a moving stimulus by a constant time of about $3\tau$ without adaptation leads it when the adaptation strength exceeds a value close to the traveling-wave threshold $\tau/\tau_v$: the network is then near the instability at which it would move by itself, and it uses this mobility to run ahead of its input. The anticipative head direction cells of the anterior thalamus, which lead the current heading by about $25\,\mathrm{ms}$, are a candidate case. The same principle, a slow negative feedback that converts a lagging response into a leading one, has been proposed for the compensation of delays in motion perception (Mi et al., 2014); it is the network counterpart of the high-pass filtering by adaptation of single neurons.

![Anticipative tracking in the adaptive CANN (Formula 44.7.1; 128 neurons, $a = 0.3$, $k = 1$, $\tau_v = 50\tau$, strong input $\alpha = 0.5$ moving at constant speed; steady state measured after $400\tau$). A: displacement of the bump center from the stimulus against the adaptation strength $m$ for three speeds: without adaptation the bump lags (negative displacement), and the displacement increases with $m$, crossing zero near $m \approx 0.02$–$0.035$, close to the traveling-wave threshold $\tau/\tau_v = 0.02$. B: the same data as an anticipation time (displacement divided by speed). Without adaptation all speeds lag by the same time, about $2.8\tau$; with adaptation the bump leads by up to several $\tau$, more for slower stimuli.](./plots/anticipative-tracking.py)

## Summary

- Continuous variables are represented by population codes whose activity is a hill on the map of preferred values; a CANN (Definition 44.2.1) stores such a hill as one of a continuum of stable bumps, using translation-invariant connections with local excitation and broader or global inhibition.
- The model with Gaussian excitation and divisive global inhibition (Formula 44.2.1) has an exact Gaussian bump at every position (Proposition 44.2.1) if inhibition is below $k_{\mathrm{c}}$.
- The perturbation spectrum has one neutral mode, the shift of position, and decaying modes for height and shape; the dynamics reduces to the bump position (Eq. (44.6)). Noise makes the bump diffuse, imperfections make it drift, and the shared shifts produce M-shaped, information-limiting correlations (Eq. (44.7)) seen in prefrontal cortex.
- Offset connections driven by velocity move the bump, implementing path integration (Definition 44.4.1); the E-PG and P-EN neurons of the fly central complex realize a ring attractor with exactly this anatomy, and rodent head direction cells keep their ring structure in sleep.
- Two-dimensional CANNs model place maps as multiple charts and grid cells as hexagonal Turing patterns moved by velocity; grid modules have toroidal population activity.
- A multi-ring model with global inhibition and weak, broad sensory input explains the gated cue responses and abrupt context switching of CA3 cells.
- Adaptation (Formula 44.7.1) produces traveling waves (Definition 44.7.1) above $m = \tau/\tau_v$, oscillatory tracking that generates theta sweeps (Definition 44.7.2) and phase precession, and anticipative tracking (Definition 44.7.3) that compensates neural delays.

| Regime of the adaptive CANN | Condition | Behavior | Proposed function |
|---|---|---|---|
| Static bump | $m < \tau/\tau_v$, no input | Persistent, diffusing bump | Working memory |
| Traveling wave | $m > \tau/\tau_v$, weak or no input | Self-propelled bump | Search, replay, Lévy flights |
| Oscillatory tracking | Strong $m$, intermediate input | Bump sweeps around input | Theta sweeps, phase precession |
| Smooth tracking | Strong input | Bump follows input, may lead | Anticipation of moving stimuli |

## Questions

1. Why does a CANN require translation-invariant weights? Describe what happens to the bump if the weights near $x = 0$ are slightly stronger than elsewhere.

   **Answer** Translation invariance makes every shifted bump a solution with the same stability, so the stationary states form a continuum with a neutral direction ($\lambda_1 = 1$). If the weights are stronger near $x = 0$, a bump there receives more recurrent excitation and is more stable than elsewhere; the energy landscape along the attractor tilts toward $x = 0$, and a bump placed elsewhere drifts toward it, slowly if the inhomogeneity is small. The continuous memory degrades into a single discrete attractor (or several, for several inhomogeneities), and a remembered value is biased toward the favored positions, which is one explanation of systematic biases in spatial working memory.

2. Using Proposition 44.2.1, show that there is a minimal strength of recurrent excitation for a persistent bump, and give the amplitude $U_0$ at the critical inhibition $k = k_{\mathrm{c}}$.

   **Answer** The condition $k \le k_{\mathrm{c}} = \rho J_0^2/(8\sqrt{2\pi}a)$ can be read as $J_0 \ge \sqrt{8\sqrt{2\pi}\,ak/\rho}$: for given inhibition, excitation must exceed a minimum. At $k = k_{\mathrm{c}}$ the square root vanishes and $U_0 = J_0/(4\sqrt{\pi}ak_{\mathrm{c}}) = 2\sqrt{2}/(\rho J_0)$, using $k_{\mathrm{c}}$; the stable and unstable bumps merge there in a saddle-node bifurcation, and for $k > k_{\mathrm{c}}$ the only attractor is the silent state.

3. In a ring attractor of $N$ neurons, the bump diffuses with a coefficient $D = c/N\,\mathrm{rad^2\,s^{-1}}$. If a fly's head direction estimate drifts with a standard deviation of $30^\circ$ after $60\,\mathrm{s}$ in darkness, what is $D$? How would the drift change if the network had four times as many neurons?

   **Answer** $\operatorname{Var}(z) = Dt$, so $D = (\pi/6)^2/60 = 0.274/60 \approx 4.6\times10^{-3}\,\mathrm{rad^2\,s^{-1}}$. With four times as many neurons, $D$ falls by a factor of 4, and the standard deviation after the same time by a factor of 2, to $15^\circ$. Real drift also contains systematic components from imperfect connectivity and from errors in the velocity input, which do not decrease with $N$; the fly's E-PG network has only about 50 neurons, so noise averaging alone cannot make it precise, and landmarks must recalibrate it often.

4. Explain qualitatively why adaptation can make a bump lead a moving stimulus rather than lag behind it.

   **Answer** A bump driven by a moving input lags because the network needs time (of order $\tau$) to build up activity at the new position. With adaptation, neurons that have been active for a while are suppressed. As the stimulus moves, the neurons on the trailing side of the bump have been active longest and are most adapted, the neurons on the leading side least. The asymmetry acts like a force pushing the bump forward, its strength growing with $m$; near the threshold $m = \tau/\tau_v$ the bump would move on its own, and with the input it moves faster than its delay would allow, settling ahead of the input by a distance that grows with $m$.

5. (Open question) The head direction system of the fly and that of the rat use different anatomy. What experiments would test whether the rat's head direction network is a ring attractor in the same sense, rather than a set of cells driven by a common input?

   **Answer** Tests could include: (a) recording many anterodorsal thalamic or postsubicular cells simultaneously in sleep and anesthesia, without head movement, and showing that the population state stays on a ring, with fixed phase relations, and moves along it continuously (done by Peyrache et al. and Chaudhuri et al.); (b) perturbing the network locally, for example optogenetically exciting cells with a particular preferred direction, and testing whether the bump jumps there and persists after the stimulation, as in the fly; (c) testing the correlation signature: M-shaped noise correlations and errors in darkness that diffuse as $\sqrt t$; (d) identifying the connectivity, for example the inhibitory interneurons and the cells with angular-velocity offsets, in the lateral mammillary and dorsal tegmental nuclei, where lesions abolish head direction tuning; (e) showing that removing landmark input changes drift but not the ring structure, whereas removing vestibular input abolishes updating but not the bump.
