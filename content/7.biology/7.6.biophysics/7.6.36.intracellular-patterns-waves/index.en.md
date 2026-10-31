---
title: Intracellular Patterns and Waves
description: "How cells and simple tissues make spatial order: a classification of pattern-forming mechanisms and their length scales, linear stability and dispersion relations, the Swift–Hohenberg equation, the Min system of E. coli and its reconstitution on membranes, mass-conserved reaction–diffusion and cell polarity, trigger waves and the speed of bistable and Fisher fronts, heterocyst spacing in growing cyanobacterial filaments, seashell patterns as space–time records, and lateral inhibition between two cells."
---

Living matter is not uniform. A bacterium marks its middle before it divides, a yeast cell picks one site on its surface for its bud, a frog egg activates mitosis in a wave that crosses a millimeter in minutes, a cyanobacterial filament spaces its nitrogen-fixing cells evenly, and a mollusc draws triangles on its shell. In each case a spatial pattern arises from local chemistry coupled by transport, and in each case the pattern has a characteristic length or speed that can be predicted from rates and diffusion coefficients. This chapter develops the physics of such patterns, starting at the subcellular scale where molecules diffuse over micrometers in seconds. We classify the mechanisms (36.1), recall how linear stability analysis turns a reaction–diffusion system into a dispersion relation and introduce the Swift–Hohenberg equation as the simplest model of a finite-wavelength instability (36.2), study the Min oscillator that finds the middle of *Escherichia coli* (36.3) and the mass-conserved systems that polarize cells (36.4), derive the speed of trigger waves (36.5), and then turn to patterns in growing fields, the heterocysts of *Anabaena* and the pigment of seashells (36.6), and to patterns made by direct contact between cells (36.7).

The mathematics of **reaction-diffusion equations**, Turing's diffusion-driven instability and the minimal speed of the **Fisher–KPP equation** are in [2.5.7](/2.5.7#sec-7.5.2); this chapter uses them without rederiving. The developmental biology of **morphogen** gradients, the **French flag model** and the precision of their readout is in [7.5.11](/7.5.11), with the physical limit of the readout in [7.6.35](/7.6.35#sec-35.1.5); Turing's condition, the Gierer–Meinhardt model, multistability and mode selection in [7.5.12](/7.5.12); segmentation by the **clock-and-wavefront model** in [7.5.23](/7.5.23); chemotactic aggregation and the **Keller–Segel model** in [7.5.13](/7.5.13). The cell biology of **cell polarity** and **Cdc42**, with the **wave-pinning model**, is in [7.3.15](/7.3.15#sec-15.4), and lateral inhibition by Notch signaling in [7.3.24](/7.3.24) and [7.5.12](/7.5.12#sec-12.10). Phase separation, the other main route to intracellular compartments, is the subject of [7.6.29](/7.6.29); the patterns formed by self-propelled particles and active stresses follow in [7.6.37](/7.6.37).

## 36.1. Rules for Making Patterns

### 36.1.1. Four Mechanisms

A pattern is a breaking of symmetry: a uniform field of molecules or cells acquires spatial structure. The structure may be imposed from outside, by a localized source or an external cue, or arise spontaneously from an instability of the uniform state. Four mechanisms account for most biological patterns.

| Mechanism | Spatial information comes from | Length scale set by | Examples | Where |
|---|---|---|---|---|
| Morphogen gradient | a localized source; cells read concentration thresholds | decay length $\lambda = \sqrt{D/k}$ | Bicoid, Dpp, Shh | [7.5.11](/7.5.11) |
| Clock and wavefront | an oscillator in each cell frozen by a moving front | front speed $\times$ clock period | somites | [7.5.23](/7.5.23) |
| Reaction–diffusion instability | local self-enhancement with longer-range inhibition or depletion | ratio of diffusion lengths, conserved mass | Min proteins, Cdc42, digits, hair follicles | 36.2–36.4, [7.5.12](/7.5.12) |
| Contact-dependent signaling | direct signaling between neighbors | the range of contact | neural precursors, bristles, ommatidia | 36.7, [7.3.24](/7.3.24) |

To these one should add phase separation ([7.6.29](/7.6.29)), excitable and bistable media that carry trigger waves (36.5), and mechanochemical feedback between active stresses and chemistry ([7.6.37](/7.6.37)). Real patterns often combine mechanisms: a gradient biases where a self-organizing system breaks symmetry, and a growing tissue inserts new elements into an existing pattern (36.6).

### 36.1.2. Length Scales

The diffusion length $\ell = \sqrt{D/k}$ of a molecule with diffusion coefficient $D$ and lifetime $1/k$ sets the scale of any pattern built from it. Cytoplasmic proteins have $D \approx 1$–$10\,\mu\mathrm{m^2\,s^{-1}}$, membrane-bound ones $0.01$–$1\,\mu\mathrm{m^2\,s^{-1}}$; modification and binding cycles turn over in $0.1$–$100\,\mathrm{s}$. Intracellular reaction–diffusion patterns therefore have lengths of $0.1$–$10\,\mu\mathrm{m}$: the size of a cell. A secreted morphogen with $D \approx 10\,\mu\mathrm{m^2\,s^{-1}}$ and a lifetime of an hour has $\ell \approx 200\,\mu\mathrm{m}$, the size of an embryonic field. The stripes of a zebra or the spots of a leopard, centimeters apart, cannot be laid down by molecular diffusion in the adult; they are formed early in development, when the skin is small, and grow with it, or arise from interactions between migrating pigment cells (as in the zebrafish), which follow the same mathematics with cells instead of molecules.

## 36.2. Instabilities and Dispersion Relations

### 36.2.1. Two Cells

The essence of Turing's mechanism can be seen with two compartments. Let an activator $X$ and an inhibitor $Y$ react according to

$$
\dot X = 5X - 6Y + 1, \qquad \dot Y = 6X - 7Y + 1 .
$$
The fixed point $X = Y = 1$ has Jacobian $J = \begin{bmatrix} 5 & -6 \\ 6 & -7\end{bmatrix}$, with trace $-2$ and determinant $1$: both eigenvalues are $-1$ and a single compartment is stable.

**Example 36.2.1 (Turing Instability of Two Cells)** Couple two such compartments by exchange with rates $D_X$ and $D_Y$. The symmetric deviation ($\delta X_1 = \delta X_2$) is unaffected by exchange and decays. The antisymmetric deviation ($\delta X_1 = -\delta X_2$) obeys $J - 2\operatorname{diag}(D_X, D_Y)$, with determinant $(5 - 2D_X)(-7 - 2D_Y) + 36 = 1 + 14D_X - 10D_Y + 4D_XD_Y$. For $D_X = 0$ and $D_Y > 0.1$ the determinant is negative and one eigenvalue positive: exchange of the inhibitor alone destabilizes the uniform state, and the two cells become different. The condition is that the inhibitor be exchanged faster than the activator, the essence of Turing's condition ([7.5.12](/7.5.12#thm-12.3.1)): a self-enhancing activator ($J_{11} = 5 > 0$) whose inhibitor leaks away to the neighbor, where it suppresses activation.

### 36.2.2. The Dispersion Relation

For a continuum, perturbations of a uniform steady state $\boldsymbol{u}^*$ of $\partial_t\boldsymbol{u} = \boldsymbol{f}(\boldsymbol{u}) + D\nabla^2\boldsymbol{u}$ can be decomposed into Fourier modes $\mathrm{e}^{\mathrm{i}\boldsymbol{q}\cdot\boldsymbol{x} + \sigma t}$ (**Fourier transform**, [2.5.6](/2.5.6)), and each mode grows or decays according to the eigenvalues of $J - q^2D$. The largest real part as a function of $q = \lvert\boldsymbol{q}\rvert$, $\sigma(q)$, is the **dispersion relation** of the system, and its shape classifies the instability.

| Type | $\sigma(q)$ first becomes positive | What forms | Examples |
|---|---|---|---|
| Stationary, finite wavelength | at $q_{\mathrm{c}} > 0$, $\sigma$ real | stationary periodic pattern | Turing patterns, Swift–Hohenberg |
| Oscillatory, $q = 0$ | at $q = 0$, $\sigma$ complex | uniform oscillation (Hopf) | glycolytic and cell-cycle oscillations |
| Oscillatory, finite wavelength | at $q_{\mathrm{c}} > 0$, $\sigma$ complex | traveling or standing waves | Min waves |
| Long-wavelength, conserved | in a band $0 < q < q_{\max}$ with $\sigma(0) = 0$ | coarsening domains | phase separation, mass-conserved polarity |

The last row deserves emphasis. If a quantity is conserved, a uniform change of it is not a perturbation that can decay, so $\sigma(0) = 0$, and instabilities start at long wavelengths. The resulting domains then tend to coarsen, often until a single domain remains: this is why phase separation and the polarity systems of 36.4 produce one droplet or one cap rather than a periodic array.

Beyond the linear stage, the pattern that is selected depends on the nonlinearities. A domain also restricts the admissible modes: with no-flux boundaries on a square of side $L$, the modes are $\cos(m\pi x/L)\cos(n\pi y/L)$ with $q^2 = \pi^2(m^2 + n^2)/L^2$. A small domain admits only the lowest unstable mode, often a single stripe ($m = 1$, $n = 0$); a larger domain admits many, and two-dimensional spots become possible. This is the classical explanation of why a cat's tail, a narrow domain, carries rings while its body carries spots (Murray, 1981).

### 36.2.3. The Swift–Hohenberg Equation

Near the onset of a stationary finite-wavelength instability, all systems behave alike, and the simplest equation with this behavior, a single field with a band of unstable modes around $q_{\mathrm{c}}$, serves as a universal model.

**Definition 36.2.1 (Swift–Hohenberg Equation)** The **Swift–Hohenberg equation** for a scalar field $u(\boldsymbol{x}, t)$ is

$$
\partial_tu = \varepsilon u - (\nabla^2 + q_{\mathrm{c}}^2)^2u + \gamma u^2 - gu^3 ,
\tag{36.1}
$$
with control parameter $\varepsilon$, critical wave number $q_{\mathrm{c}}$, and coefficients $\gamma$ and $g > 0$ of the nonlinear terms.

Linearizing about $u = 0$ and substituting $\mathrm{e}^{\mathrm{i}qx + \sigma t}$ gives

$$
\sigma(q) = \varepsilon - (q_{\mathrm{c}}^2 - q^2)^2 .
\tag{36.2}
$$
For $\varepsilon < 0$ all modes decay; at $\varepsilon = 0$ the mode $q = q_{\mathrm{c}}$ becomes marginal, and for small $\varepsilon > 0$ the band $\lvert q - q_{\mathrm{c}}\rvert \lesssim \sqrt\varepsilon/(2q_{\mathrm{c}})$ grows. The fourth-order derivative is the simplest term that penalizes both long and short wavelengths: it plays the role that the combination of short-range activation and long-range inhibition plays in a two-component system. Swift and Hohenberg (1977) derived it for convection rolls; it describes stripes of Turing systems, wrinkling of elastic sheets and the patterns of vegetation in drylands alike.

**Theorem 36.2.1 (Amplitude of Stripes)** For $\gamma = 0$ and small $\varepsilon > 0$, Eq. (36.1) has stripe solutions $u \approx A\cos(q_{\mathrm{c}}x)$ with

$$
A = \sqrt{\frac{4\varepsilon}{3g}} .
\tag{36.3}
$$

**Proof** Substitute $u = A\cos(q_{\mathrm{c}}x)$, for which $(\nabla^2 + q_{\mathrm{c}}^2)u = 0$. With $\cos^3\theta = \frac34\cos\theta + \frac14\cos 3\theta$, the cubic term contributes $-\frac34gA^3\cos(q_{\mathrm{c}}x)$ to the first harmonic and a third harmonic, which is strongly damped (its linear growth rate is $\varepsilon - 64q_{\mathrm{c}}^4$) and only slightly corrects the shape. Balancing the first harmonic in the steady state gives $\varepsilon A - \frac34gA^3 = 0$. $\square$

The amplitude grows as $\sqrt\varepsilon$, the behavior of a supercritical (pitchfork) **bifurcation** ([2.4.11](/2.4.11)). The quadratic term breaks the symmetry $u \to -u$ and favors hexagonal arrays of spots, which can appear even slightly below onset (a subcritical transition with hysteresis). Spots versus stripes in Turing systems ([7.5.12](/7.5.12#sec-12.11)) reflect the same symmetry.

![The Swift–Hohenberg equation, Eq. (36.1), with q_c = 1. A: growth rate σ(q) = ε − (q_c² − q²)² for ε = −0.1, 0 and 0.2: above threshold a band of wave numbers around q_c is unstable. B: pattern grown from small random noise for ε = 0.2 and γ = 0: stripes with defects, in a periodic box sixteen wavelengths wide. C: with a quadratic term, ε = 0.1 and γ = 1: hexagonally packed spots. Pseudo-spectral simulation on a 128 × 128 grid](./plots/swift-hohenberg.py)

## 36.3. The Min System: How a Bacterium Finds Its Middle

### 36.3.1. Biology

*E. coli* divides at its middle with an error of a few percent of its length. The division ring is built by FtsZ, the bacterial tubulin homolog ([7.3.15](/7.3.15#def-15.2.1)), and two systems keep it away from the wrong places: nucleoid occlusion, which prevents ring assembly over the chromosomes, and the Min system, which prevents it near the poles. Mutants without the Min proteins divide near a pole as often as at the middle and produce small anucleate minicells, after which the system is named. Three proteins are involved:

- MinC inhibits FtsZ polymerization; it has no localization of its own and rides on MinD.
- MinD is an ATPase that binds the membrane as an ATP-bound dimer through an amphipathic helix, cooperatively: MinD-ATP on the membrane recruits more MinD-ATP.
- MinE binds membrane MinD, stimulates its ATP hydrolysis and releases it into the cytoplasm as MinD-ADP, which must exchange ADP for ATP before it can bind again; MinE itself leaves shortly after.

Fluorescence microscopy shows that MinD and MinC do not sit at the poles but oscillate between them: they accumulate on the membrane in one half of the cell, a ring of MinE forms at the edge of this zone and moves towards the pole while the MinD is released, and the MinD reassembles in the opposite half (Raskin and de Boer, 1999; Hu and Lutkenhaus, 1999). The period is about $40\,\mathrm{s}$ to $2\,\mathrm{min}$, much shorter than the cell cycle. Averaged over time, the concentration of MinC is lowest at midcell, which is therefore the only place where an FtsZ ring can assemble. In filamentous cells that cannot divide, the oscillation becomes a pattern of several bands with a spacing of about $8$–$10\,\mu\mathrm{m}$.

**Definition 36.3.1 (Min Oscillation)** The **Min oscillation** is the self-organized pole-to-pole oscillation of the proteins MinD and MinE (and the passenger MinC) between the membrane and the cytoplasm of rod-shaped bacteria, driven by ATP hydrolysis, whose time average places the minimum of the FtsZ inhibitor MinC at midcell.

### 36.3.2. A Reaction–Diffusion Model

The Min oscillation is an intracellular reaction–diffusion pattern: proteins diffuse quickly in the cytoplasm ($D \approx 2$–$10\,\mu\mathrm{m^2\,s^{-1}}$) and slowly on the membrane, and the reactions are cycles of binding and release. Several models reproduce it; the simplest, one-dimensional one is that of Howard, Rutenberg and de Vet (2001).

**Formula 36.3.1 (A Min Oscillator)** Let $\rho_D$, $\rho_E$ be the line densities of cytoplasmic MinD and MinE along the cell, and $\rho_d$, $\rho_e$ those on the membrane. With no-flux ends,

$$
\begin{aligned}
\partial_t\rho_D &= D_D\partial_x^2\rho_D - \frac{\sigma_1\rho_D}{1 + \sigma_1'\rho_e} + \sigma_2\rho_e\rho_d, &
\partial_t\rho_d &= \frac{\sigma_1\rho_D}{1 + \sigma_1'\rho_e} - \sigma_2\rho_e\rho_d, \\
\partial_t\rho_E &= D_E\partial_x^2\rho_E - \sigma_3\rho_D\rho_E + \frac{\sigma_4\rho_e}{1 + \sigma_4'\rho_D}, &
\partial_t\rho_e &= \sigma_3\rho_D\rho_E - \frac{\sigma_4\rho_e}{1 + \sigma_4'\rho_D} .
\end{aligned}
\tag{36.4}
$$
MinD binds the membrane where MinE is scarce and is released by membrane MinE; MinE is recruited where MinD is abundant. The total numbers of MinD and MinE are conserved.

The model is a two-species activator–inhibitor system with conservation: MinD favors MinE recruitment, MinE removes MinD, and the cytoplasmic pools couple distant parts of the cell. More detailed models add MinD's cooperative recruitment to the membrane and the delay of nucleotide exchange in the cytoplasm (Huang, Meir and Wingreen, 2003); this delay turned out to be essential in three dimensions, because released MinD-ADP cannot rebind immediately and diffuses away from the zone that MinE has just cleared. The simulation in the figure shows the pole-to-pole oscillation, the minimum of the time-averaged MinD at midcell, and the breakup of the pattern in a long filament.

![Pole-to-pole oscillation in the one-dimensional Min model of Formula 36.3.1 (Howard, Rutenberg and de Vet, 2001; mean densities 1500 MinD and 85 MinE per µm, rates and diffusion coefficients of the published model multiplied by 2.5, which only speeds up the dynamics). A: kymograph of membrane MinD in a 2.5 µm cell: MinD accumulates in one half, is removed from the midcell side by MinE, and reassembles in the other half, with a period of about 60 s. B: membrane MinD averaged over 400 s (MinC rides on it): the minimum is at midcell, where the FtsZ ring can assemble. C: in an 8 µm filament the pole-to-pole pattern is lost; bands of MinD form in the interior and travel over a few micrometers, the beginning of the multiple bands seen in long cells](./plots/min-oscillation.py)

### 36.3.3. Waves on a Membrane

Loose, Fischer-Friedrich, Ries, Kruse and Schwille (2008) reconstituted the system from purified MinD, MinE and ATP on a supported lipid bilayer. The proteins formed traveling waves and spirals with wavelengths of tens of micrometers and speeds of $0.3$–$0.8\,\mu\mathrm{m\,s^{-1}}$; the bands of MinD had a sharp leading edge and a rear where MinE accumulated, and adding more MinE shortened the wavelength. No other cellular component is required: two proteins, ATP and a membrane form a pattern-generating machine.

The speed of the waves can be estimated from a treadmilling picture. Bound proteins hardly move; the band advances because MinD attaches at its front and detaches at its back, as actin treadmills ([7.6.26](/7.6.26)).

**Formula 36.3.2 (Speed of a Treadmilling Band)** If molecules of size $d$ attach at the front of a band with a diffusion-limited rate $k_{\mathrm{on}} \approx Ddc$ from a solution of concentration $c$ and diffusion coefficient $D$, and the band keeps constant length by losing molecules at the back at the same rate, the band moves at

$$
v \approx k_{\mathrm{on}}d = Dd^2c .
\tag{36.5}
$$

**Example 36.3.1** With $D = 60\,\mu\mathrm{m^2\,s^{-1}}$ for MinD in buffer, $c = 1\,\mu\mathrm{M} = 600\,\mu\mathrm{m^{-3}}$ and $d = 5\,\mathrm{nm}$, $v = 60 \times (5\times10^{-3})^2 \times 600 = 0.9\,\mu\mathrm{m\,s^{-1}}$, the observed order of magnitude. In the cell, cytoplasmic diffusion is slower and the standing wave of wavelength $\lambda \approx 2L \approx 5\,\mu\mathrm{m}$ (a half-wavelength fits the cell) and period $T \approx 50\,\mathrm{s}$ corresponds to two counter-propagating waves of speed $\lambda/T \approx 0.1\,\mu\mathrm{m\,s^{-1}}$.

The tenfold larger wavelength in vitro long puzzled modelers. It is explained by geometry: on a flat bilayer the bulk solution above the membrane is millimeters deep, whereas in a cell the ratio of cytoplasmic volume to membrane area is about $0.2\,\mu\mathrm{m}$; in vitro systems confined to compartments of cellular dimensions recover the in vivo patterns (Halatek and Frey, 2018). The Min system has since been used to build synthetic, programmable patterns: tuning the expression of MinD and MinE in engineered cells changes the frequency and wavelength of the oscillation, and Min waves can position other proteins fused to MinD.

## 36.4. Mass-Conserved Reaction–Diffusion and Cell Polarity

### 36.4.1. The Slope Criterion

Many intracellular patterns are made by proteins that cycle between a slowly diffusing membrane-bound state and a fast-diffusing cytosolic state, conserving their total number on the time scale of the pattern: Min proteins, Rho GTPases such as Cdc42 in budding yeast, PAR proteins in the *Caenorhabditis elegans* zygote.

**Definition 36.4.1 (Mass-Conserved Reaction–Diffusion System)** A **mass-conserved reaction–diffusion system** of two components is a system $\partial_ta = D_a\nabla^2a + f(a, b)$, $\partial_tb = D_b\nabla^2b - f(a, b)$, in which the reaction only interconverts the two forms (typically membrane-bound $a$ and cytosolic $b$), so that the total amount $\int(a + b)\,\mathrm{d}\boldsymbol{x}$ is conserved.

The local reactions have a line of steady states, the nullcline $f(a, b) = 0$ in the $(a, b)$ plane, and each total density $n = a + b$ picks a point on it. Whether the uniform state with that density is stable to spatial perturbations depends on the slope of the nullcline.

**Theorem 36.4.1 (Lateral Instability of Mass-Conserved Systems)** Let the uniform state $(a^*, b^*)$ be locally stable ($f_a - f_b < 0$, with $f_b > 0$). It is unstable to spatial perturbations if and only if

$$
D_bf_a > D_af_b, \quad\text{equivalently}\quad \frac{\mathrm{d}b^*}{\mathrm{d}a^*}\bigg|_{f = 0} = -\frac{f_a}{f_b} < -\frac{D_a}{D_b} ,
\tag{36.6}
$$
and then the modes with $0 < q^2 < (D_bf_a - D_af_b)/(D_aD_b)$ grow.

**Proof** For a mode $\mathrm{e}^{\mathrm{i}qx + \sigma t}$ the linearized system has the matrix $\begin{bmatrix} f_a - D_aq^2 & f_b \\ -f_a & -f_b - D_bq^2\end{bmatrix}$, with trace $f_a - f_b - (D_a + D_b)q^2 < 0$ and determinant $q^2\left[D_aD_bq^2 - (D_bf_a - D_af_b)\right]$. With negative trace, an eigenvalue is positive exactly when the determinant is negative, which happens for some $q > 0$ if and only if $D_bf_a - D_af_b > 0$, for the stated band. At $q = 0$ the determinant vanishes: the zero eigenvalue belongs to the conserved total. $\square$

Since $D_a \ll D_b$ for membrane-bound and cytosolic forms, the criterion essentially requires $f_a > 0$: the reaction must be self-enhancing in $a$ at fixed $b$, so that the nullcline bends back with negative slope. Brauns, Halatek and Frey (2020) developed this geometric picture into a general theory of mass-conserved patterns: local equilibria shift along the nullcline as mass is redistributed by cytosolic diffusion, and a region of negative slope produces a mass-redistribution instability. The theory explains why such systems coarsen to a single domain: two domains compete for the same cytosolic pool, and the larger, which depletes the pool more effectively, wins.

### 36.4.2. Polarity With and Without a Threshold

The wave-pinning model of Mori, Jilkine and Edelstein-Keshet (2008) ([7.3.15](/7.3.15#fml-15.4.1)), $f(a, b) = b(k_0 + \gamma a^2/(K^2 + a^2)) - \delta a$, has an S-shaped nullcline (panel A of the figure). Depending on the total amount of GTPase, two behaviors occur.

- If the uniform state lies on the part of the nullcline with negative slope, Theorem 36.4.1 applies: noise alone is amplified, and the cell polarizes spontaneously, a Turing-type mechanism for a single cap (panel B).
- If the uniform state lies on a stable branch, but the local kinetics is bistable over a range of $b$, small perturbations decay; a sufficiently strong local stimulus switches a region to the high state, and the front between high and low states travels until the depletion of the cytosolic pool stops it (panel C). The front stops when the cytosolic concentration $b$ reaches the value at which the two stable branches have "equal strength", $\int_{a_-}^{a_+}f(a, b)\,\mathrm{d}a = 0$ (the equal-area rule of Theorem 36.5.1 below, and of [7.5.12](/7.5.12#thm-12.5.1)). This is wave pinning: polarity with a threshold and with memory.

Budding yeast appears to use both mechanisms, with additional positive feedback through actin-directed vesicle delivery of Cdc42. In the *C. elegans* zygote, mutually inhibiting anterior and posterior PAR proteins form two mass-conserved domains, and the boundary between them is positioned by the cortical flow that the sperm-donated centrosome triggers: an advective cue, not a chemical gradient, breaks the symmetry (Goehring and colleagues, 2011).

![Polarity from a mass-conserved reaction–diffusion system: the wave-pinning model of a small GTPase (as in 7.3.15, k₀ = 0.067, γ = δ = K = 1), active membrane form a (D_a = 0.02 µm²/s) and inactive cytosolic form b (D_b = 10 µm²/s), in a 10 µm cell. A: the nullcline f(a, b) = 0 and lines of constant total density a + b (dashed); on the thick segment the slope is below −D_a/D_b and the uniform state is laterally unstable (Theorem 36.4.1). The dots mark the uniform states of B (total 2.5) and C (total 2.2). B: from small noise around the unstable uniform state, a single domain of active GTPase forms without any cue. C: around the stable uniform state, noise decays (thin line, final profile) but a transient local stimulus at the left end (activation 0.5 b s⁻¹ for 20 s) leaves a pinned polar domain (thick line): polarization then requires a threshold](./plots/mass-conserved-polarity.py)

## 36.5. Trigger Waves

### 36.5.1. Fronts in Bistable and Excitable Media

Diffusion is too slow to carry signals across large cells: a molecule with $D = 10\,\mu\mathrm{m^2\,s^{-1}}$ needs $L^2/2D \approx 5\,\mathrm{h}$ to diffuse across a $1.2\,\mathrm{mm}$ frog egg. Yet the egg enters mitosis everywhere within minutes, and its fertilization is signaled across it by a calcium wave in a few minutes. The solution is a wave that regenerates itself.

**Definition 36.5.1 (Trigger Wave)** A **trigger wave** is a self-regenerating front or pulse that propagates at constant speed and constant shape through a bistable or excitable medium: each region, switched to the excited state, raises its neighbors above their threshold by diffusion (or another coupling), so that the signal is renewed at every point rather than diluted.

The distance covered grows linearly with time instead of as $\sqrt t$, and the amplitude does not decay. Trigger waves are the spatial counterpart of switches and oscillators ([7.6.33](/7.6.33)); the action potential is the best-known example ([7.6.30](/7.6.30)).

| Trigger wave | Bistable or excitable module | Speed |
|---|---|---|
| Calcium wave at fertilization ([7.5.4](/7.5.4)) | calcium-induced calcium release through IP₃ receptors | $5$–$30\,\mu\mathrm{m\,s^{-1}}$ |
| Mitotic wave in *Xenopus* egg extracts | Cdk1 activation by positive feedback through Cdc25 and Wee1 ([7.3.20](/7.3.20)) | about $60\,\mu\mathrm{m\,min^{-1}}$ (Chang and Ferrell, 2013) |
| Apoptotic wave in *Xenopus* extracts | caspase activation with positive feedback | about $30\,\mu\mathrm{m\,min^{-1}}$ (Cheng and Ferrell, 2018) |
| cAMP waves in *Dictyostelium* ([7.5.13](/7.5.13)) | excitable cAMP relay | $\sim 0.3\,\mu\mathrm{m\,s^{-1}}$ |
| Action potential ([7.6.30](/7.6.30)) | voltage-gated Na⁺ channels | $1$–$100\,\mathrm{m\,s^{-1}}$ |

### 36.5.2. Front Speed

A one-component bistable medium is described by $\partial_tu = D\partial_x^2u + f(u)$, with stable states $u = 0$ and $u = 1$ and an unstable threshold between them. A front is a solution $u = U(x - vt)$.

**Theorem 36.5.1 (Direction of a Bistable Front)** If a front connects $u = 1$ at $x \to -\infty$ to $u = 0$ at $x \to +\infty$, its speed satisfies

$$
v\int_{-\infty}^{\infty}U'(\xi)^2\,\mathrm{d}\xi = \int_0^1f(u)\,\mathrm{d}u ,
\tag{36.7}
$$
so the front invades the state $u = 0$ ($v > 0$) if and only if $\int_0^1f\,\mathrm{d}u > 0$, and stalls when the two states have equal "potential".

**Proof** The profile satisfies $DU'' + vU' + f(U) = 0$, with $U' \to 0$ at both ends. Multiply by $U'$ and integrate over $\xi$: $\int DU''U'\,\mathrm{d}\xi = [DU'^2/2] = 0$, and $\int f(U)U'\,\mathrm{d}\xi = \int_1^0f(u)\,\mathrm{d}u = -\int_0^1f\,\mathrm{d}u$. Hence $v\int U'^2\,\mathrm{d}\xi = \int_0^1f\,\mathrm{d}u$. $\square$

For the cubic $f(u) = ku(1 - u)(u - a)$ the front can be found exactly, $U = [1 + \mathrm{e}^{\xi\sqrt{k/2D}}]^{-1}$, and its speed is $v = \sqrt{Dk/2}\,(1 - 2a)$ ([Formula 4.3.2 of 7.5.4](/7.5.4#fml-4.3.2)): it reverses at $a = 1/2$, as Theorem 36.5.1 requires. For the Fisher–KPP nonlinearity $f = ku(1 - u)$, in which $u = 0$ is unstable rather than stable, fronts from localized initial conditions travel at the minimal speed $v = 2\sqrt{Dk}$ ([2.5.7](/2.5.7#sec-7.5.2), [7.5.23](/7.5.23#def-23.6.2)).

The two cases differ in a way that matters for biology. A Fisher front is *pulled*: its speed is set by the linear growth of small amplitudes far ahead of the front, so it is sensitive to fluctuations at the leading edge (with few molecules or cells the speed is reduced, and the approach to the asymptotic speed is slow, with a correction $\propto 1/t$). A bistable front is *pushed*: its speed is set by the nonlinear region of the front itself, it has a threshold (a small perturbation does not start it), and it is robust. Cells use bistable switches for trigger waves when the wave must start only on a real signal and propagate reliably.

**Example 36.5.1** For mitotic waves in *Xenopus* extracts, Chang and Ferrell (2013) measured about $60\,\mu\mathrm{m\,min^{-1}}$. With $v \sim \sqrt{D/\tau}$, an effective diffusion coefficient of $D \approx 600\,\mu\mathrm{m^2\,min^{-1}}$ ($10\,\mu\mathrm{m^2\,s^{-1}}$) and a switching time of the Cdk1 positive feedback loop of $\tau \approx D/v^2 \approx 0.2\,\mathrm{min}$ reproduce the speed; the wave crosses a $1.2\,\mathrm{mm}$ egg in about $20\,\mathrm{min}$, where diffusion alone would need hours. In the egg, the mitotic wave becomes visible as the surface contraction waves that precede each cleavage.

![Trigger waves in one dimension (lengths in units of √(D/k), times in 1/k). A: profiles every 10 time units of a bistable front, ∂ₜu = ∂ₓ²u + u(1 − u)(u − a) with a = 0.25 (solid), and of a Fisher–KPP front, ∂ₜu = ∂ₓ²u + u(1 − u) (dashed), both started from a step. B: front positions against time; lines have the slopes √(1/2)(1 − 2a) and 2: the bistable front moves at its predicted speed at once, the Fisher front approaches its speed slowly from below; the point at which a step spreading by diffusion alone reaches u = 0.1 advances only as √t (dotted). C: speed of the bistable front against the threshold a, from simulations (points) and the exact formula (line): the front reverses at a = 1/2 (Theorem 36.5.1)](./plots/trigger-waves.py)

## 36.6. Patterns in Growing Fields

### 36.6.1. Heterocysts in *Anabaena*

The filamentous cyanobacterium *Anabaena* (*Nostoc*) fixes carbon by photosynthesis and nitrogen in specialized cells. Nitrogenase is destroyed by oxygen, so nitrogen fixation is confined to heterocysts, cells with thick envelopes that turn off photosystem II and supply fixed nitrogen to their neighbors in exchange for sugars.

**Definition 36.6.1 (Heterocyst)** A **heterocyst** is a terminally differentiated, non-dividing cell of a filamentous cyanobacterium that fixes atmospheric nitrogen in a micro-oxic interior and exchanges fixed nitrogen for fixed carbon with the vegetative cells of the filament.

When nitrogen becomes scarce, about one cell in ten differentiates into a heterocyst, at intervals that are more regular than random. The decision is controlled by the transcription factor HetR, which activates its own gene and the genes of differentiation, and by the small peptides PatS and HetN, induced by HetR in differentiating cells, whose processed product (the pentapeptide RGSGR) moves to neighboring cells and promotes the degradation of HetR there. A differentiating cell thus inhibits its neighbors: local self-activation and lateral inhibition, the elements of a Turing mechanism, along a one-dimensional chain of cells. As the filament grows, the intervals between heterocysts lengthen, the inhibitor level in their middle falls, and a new heterocyst differentiates there, keeping the spacing roughly constant.

A minimal model shows the essential behavior: heterocysts as point sources of an inhibitor that decays with distance, vegetative cells that commit stochastically when the inhibitor falls below a threshold, and growth and division of vegetative cells. It produces new heterocysts midway between existing ones and a distribution of intervals with a peak near ten cells, far narrower than the geometric distribution expected from random placement. Real filaments deviate in instructive ways: mutants lacking PatS form heterocysts in clusters but still not at random, and differentiation is restricted to cells at particular stages of the cell cycle, so lateral inhibition is one of several layers of control.

![A minimal model of heterocyst patterning in a growing Anabaena filament: vegetative cells grow (doubling time 20 h) and divide; heterocysts neither grow nor divide and produce an inhibitor whose level in each cell is a sum of exponentials, exp(−d/λ) with λ = 2.5 cells; a vegetative cell commits at rate 0.2 h⁻¹ when the inhibitor is below 0.15. A: positions of heterocysts (dots) along a filament of initially 30 cells after nitrogen step-down; new heterocysts appear in the middle of intervals that have grown. B: number of vegetative cells between neighboring heterocysts after 60 h in 200 filaments (bars), compared with the geometric distribution with the same mean, expected for random placement (line)](./plots/heterocyst-spacing.py)

### 36.6.2. Seashells: Patterns in Space and Time

A mollusc enlarges its shell by adding material at the growing edge, and pigment is deposited in the new strip according to the activity of cells in the mantle along the margin. The pattern on the shell is therefore a space–time record of a one-dimensional dynamical system: position along the margin is space, distance from the margin back to the apex is time. Meinhardt (1995) showed that reaction–diffusion systems along the margin reproduce the diversity of shell patterns.

- A stationary Turing pattern along the margin draws lines perpendicular to the margin, along the direction of growth.
- A uniform oscillation draws bands parallel to the margin.
- Traveling waves, initiated at random places and annihilating when they meet, as in an excitable medium, draw oblique lines, chevrons and triangles, as on the shells of *Conus* and *Oliva* species.

The model makes testable predictions: after a local injury to the margin, the pattern regenerates in a way determined by the dynamics. And because small changes of parameters switch between pattern types, closely related species often have very different patterns. The overall shape of the shell, the logarithmic spiral of coiling, is set by a few geometric growth parameters in Raup's model ([7.10](/7.10)).

![Shell patterns as space–time records of the dynamics along the growing margin (each row is the pigment laid down at one time; time runs downwards). A and B: the Gierer–Meinhardt activator–inhibitor system ([7.5.12](/7.5.12)) on a ring of 150 cells. A: fast, far-reaching inhibitor (D_h = 0.4, ν = 0.07, μ = 0.05, D_a = 0.005): stationary peaks draw lines along the direction of growth. B: inhibitor slower than the activator (ν = 0.02 < μ) with little spread: the margin oscillates in synchrony and draws bands parallel to it. C: an excitable margin (Barkley's model) in which resting regions fire at random: pairs of waves travel along the margin and annihilate when they meet, drawing oblique lines, chevrons and triangles](./plots/seashell-patterns.py)

## 36.7. Patterns by Contact: Lateral Inhibition

### 36.7.1. Two Cells

When neighboring cells must adopt different fates, the inhibitory signal can pass by direct contact rather than diffusion. In **lateral inhibition** ([7.3.24](/7.3.24#def-24.3.3)) through the **Notch signaling pathway** ([7.3.19](/7.3.19)), the ligand Delta on one cell activates the receptor Notch on its neighbor, and Notch activity represses Delta in the receiving cell. The double-negative loop between two cells amplifies a small difference. A two-cell version of the model of Collier, Monk, Lewis and Lewis (1996) shows how.

**Proposition 36.7.1 (Symmetry Breaking Between Two Cells)** Let Notch activities $N_i$ and Delta activities $D_i$ of cells $i = 1, 2$ obey

$$
\frac{\mathrm{d}N_1}{\mathrm{d}t} = f(D_2) - N_1, \quad \frac{\mathrm{d}D_1}{\mathrm{d}t} = v[g(N_1) - D_1], \quad\text{and likewise for cell 2},
\tag{36.8}
$$
with $f$ increasing and $g$ decreasing. If Delta is fast ($v \gg 1$), $D_i = g(N_i)$, and the symmetric state $N_1 = N_2 = N^*$, $N^* = f(g(N^*))$, is unstable if and only if

$$
\lvert f'(g(N^*))\,g'(N^*)\rvert > 1 .
\tag{36.9}
$$
The cells then go to one of two asymmetric states, one with low Notch and high Delta (the primary fate), the other with high Notch.

**Proof** With $D_i = g(N_i)$, $\dot N_1 = f(g(N_2)) - N_1$ and $\dot N_2 = f(g(N_1)) - N_2$. Let $\mu = f'(g(N^*))g'(N^*) < 0$. The Jacobian at the symmetric state is $\begin{bmatrix} -1 & \mu \\ \mu & -1\end{bmatrix}$, with eigenvalue $-1 + \mu < 0$ for the symmetric mode $(1, 1)$ and $-1 - \mu = -1 + \lvert\mu\rvert$ for the antisymmetric mode $(1, -1)$, which is positive exactly when $\lvert\mu\rvert > 1$. $\square$

The condition is a loop gain larger than one, the same criterion as for the toggle switch ([7.6.33](/7.6.33)): two cells coupled by lateral inhibition are a genetic toggle switch distributed over two cells. Steep functions $f$ and $g$ (high **Hill coefficients**) make it easy to satisfy. On a sheet, the same mechanism gives salt-and-pepper patterns whose spacing is set by the range of contact, the subject of [7.5.12](/7.5.12#sec-12.10) and [7.3.24](/7.3.24); Sprinzak and colleagues (2010) found that Delta also inactivates Notch in the same cell (cis-inhibition), which sharpens the switch further, by measuring Notch activity in cells on surfaces coated with defined amounts of Delta.

![Lateral inhibition between two cells (Proposition 36.7.1) with f(x) = x²/(0.01 + x²) and g(x) = 1/(1 + 100x²), time in units of the Notch lifetime. A: for fast Delta the dynamics reduces to the (N₁, N₂) plane: nullclines N₁ = f(g(N₂)) and N₂ = f(g(N₁)), the flow (grey streamlines), the unstable symmetric state (open circle), and trajectories of the full four-variable model (v = 10) started 2 % away from it, which end in one of the two asymmetric stable states (filled). B: time courses from Notch levels differing by 1 %: the difference is amplified until cell 2 has low Notch and high Delta (primary fate) and cell 1 high Notch](./plots/notch-delta.py)

### 36.7.2. Cascades of Contacts: The Fly Eye

The compound eye of *Drosophila* consists of about $800$ ommatidia, each of about twenty cells in a nearly crystalline arrangement, all derived from a uniform epithelium. A wave of differentiation, the morphogenetic furrow, sweeps across the eye disc, driven by Hedgehog secreted by cells just behind it. In the furrow, the proneural protein Atonal is first expressed broadly and then restricted, by lateral inhibition with a range of a few cells, to evenly spaced single cells that become the R8 photoreceptors, one per future ommatidium in a hexagonal array. Each R8 then recruits its neighbors in a fixed sequence of contact-dependent signals (R2/R5, R3/R4, R1/R6, R7, cone and pigment cells), each step a binary decision of the kind of Proposition 36.7.1. The final geometry is also mechanical: in mutants with abnormal numbers of cone cells, the cells pack in the same configurations as soap bubbles of equal number, which shows that adhesion and surface tension minimize the interfacial energy of the cluster (Hayashi and Carthew, 2004; [7.5.8](/7.5.8)). A sequence of local binary decisions, each made by contact, builds a complex pattern without a global coordinate system.

A related problem, the regular arrangement of leaves and flowers around a plant shoot (phyllotaxis), arises from the polar transport of auxin, which concentrates the hormone at points away from existing primordia; it is treated with plant development in [7.12](/7.12).

## Summary

| Mechanism | Key equation or criterion | Where |
|---|---|---|
| Two-cell Turing instability | antisymmetric mode of $J - 2\operatorname{diag}(D_X, D_Y)$ | Example 36.2.1 |
| Dispersion relation | $\sigma(q)$: stationary, oscillatory, finite-$q$, conserved ($\sigma(0) = 0$) | 36.2.2 |
| Swift–Hohenberg | $\sigma = \varepsilon - (q_{\mathrm{c}}^2 - q^2)^2$; stripes $A = \sqrt{4\varepsilon/3g}$, hexagons with $\gamma \ne 0$ | Definition 36.2.1, Theorem 36.2.1 |
| Min oscillation | membrane–cytosol cycling with conservation; MinC minimum at midcell; band speed $v \approx Dd^2c$ | Definition 36.3.1, Formulas 36.3.1–36.3.2 |
| Mass-conserved polarity | unstable where nullcline slope $< -D_a/D_b$; one domain; wave pinning with threshold | Definition 36.4.1, Theorem 36.4.1 |
| Trigger waves | $v\int U'^2 = \int_0^1f\,\mathrm{d}u$; bistable $v = \sqrt{Dk/2}(1 - 2a)$ (pushed), Fisher $2\sqrt{Dk}$ (pulled) | Definition 36.5.1, Theorem 36.5.1 |
| Growing fields | heterocysts inserted at midpoints by lateral inhibition; shells as space–time records | Definition 36.6.1, 36.6.2 |
| Lateral inhibition | symmetric state unstable if $\lvert f'g'\rvert > 1$ | Proposition 36.7.1 |

- Intracellular patterns have micrometer scales because cytoplasmic diffusion and reaction cycles have the corresponding $\sqrt{D/k}$.
- Conservation of protein number makes patterns coarsen to a single domain and couples their size to the amount of protein; this suits a cell that needs one division site or one bud.
- Trigger waves let cells send signals over millimeters at constant speed; bistability gives them a threshold and robustness.

## Questions

1. For the two-cell model of Example 36.2.1, find the smallest $D_Y$ that destabilizes the uniform state when $D_X = 0.05$, and explain why the instability disappears if both species are exchanged equally fast.

   **Answer** The determinant of the antisymmetric mode is $1 + 14D_X - 10D_Y + 4D_XD_Y = 1.7 - 9.8D_Y$, negative for $D_Y > 0.173$. With $D_X = D_Y = D$, the matrix is $J - 2DI$, whose eigenvalues are those of $J$ shifted by $-2D$: $-1 - 2D < 0$. Equal exchange cannot destabilize a stable state; the instability needs the inhibitor to spread faster, so that it reaches the neighbor while the activator stays.

2. Show that in the Swift–Hohenberg equation the band of unstable wave numbers for small $\varepsilon$ is $\lvert q - q_{\mathrm{c}}\rvert < \sqrt\varepsilon/(2q_{\mathrm{c}})$, and estimate how many wavelengths a domain must contain for more than one mode to be unstable when $\varepsilon = 0.04$ and $q_{\mathrm{c}} = 1$.

   **Answer** $\sigma > 0$ requires $\lvert q_{\mathrm{c}}^2 - q^2\rvert < \sqrt\varepsilon$; with $q = q_{\mathrm{c}} + \delta$, $q_{\mathrm{c}}^2 - q^2 \approx -2q_{\mathrm{c}}\delta$, so $\lvert\delta\rvert < \sqrt\varepsilon/(2q_{\mathrm{c}})$. For $\varepsilon = 0.04$, the band is $\lvert\delta\rvert < 0.1$, width $0.2$. In a domain of length $L$ with no-flux ends the modes are spaced $\pi/L$; two fit into the band if $\pi/L < 0.2$, $L > 16$, that is more than $16/(2\pi) \approx 2.5$ wavelengths. Smaller domains select a single mode, larger ones allow competition and defects.

3. In the Min system, what would happen to the time-averaged MinC profile if MinE were absent, and if MinD could not bind the membrane cooperatively? Relate your answer to the minicell phenotypes.

   **Answer** Without MinE, MinD (with MinC) coats the whole membrane uniformly and stays there; FtsZ rings are inhibited everywhere and cells grow into filaments, as observed for *minE* mutants overexpressing MinCD. Without self-recruitment (no self-enhancement, $f_a < 0$ in the language of Theorem 36.4.1), the uniform state is stable and no oscillation forms; MinC is spread evenly, and division sites are not excluded from the poles, which gives minicells, as when the whole *min* locus is deleted.

4. Using Formula 36.3.2, how would the in vitro wave speed change if the MinD concentration were doubled, and if a crowding agent reduced the diffusion coefficient in solution threefold? Why might the measured speed respond less than predicted?

   **Answer** $v \propto Dc$: doubling $c$ doubles the speed, and dividing $D$ by three divides it by three. The estimate assumes attachment limited by diffusion at the front and detachment at the back balancing it; in reality attachment is reaction-limited in part, MinE recruitment rises with MinD, and wave speed and wavelength are set jointly by the whole dynamics (more MinD also recruits MinE faster, shortening bands), so the response is expected to be weaker than linear.

5. Prove that for the cubic $f(u) = ku(1 - u)(u - a)$ the profile $U(\xi) = [1 + \exp(\xi\sqrt{k/2D})]^{-1}$ solves $DU'' + vU' + f(U) = 0$ with $v = \sqrt{Dk/2}(1 - 2a)$.

   **Answer** Let $s = \sqrt{k/2D}$. Then $U' = -sU(1 - U)$ and $U'' = -s(1 - 2U)U' = s^2U(1 - U)(1 - 2U)$. Substituting, $U(1 - U)[Ds^2(1 - 2U) - vs + k(U - a)] = 0$. The bracket is linear in $U$: the coefficient of $U$, $-2Ds^2 + k = 0$ because $s^2 = k/2D$; the constant, $Ds^2 - vs - ka = k/2 - ka - vs = 0$ gives $v = k(1 - 2a)/(2s) = \sqrt{Dk/2}(1 - 2a)$.

6. A Fisher front is pulled by its leading edge. Explain why a population of only a few cells per unit length invades more slowly than $2\sqrt{Dk}$, and why a bistable (Allee-type) front is less affected.

   **Answer** The Fisher speed comes from exponential growth of tiny densities far ahead of the front. With discrete individuals, density cannot be smaller than one individual per volume; the leading edge is cut off, and the speed is reduced, logarithmically in the number $N$ of individuals per front volume, $v \approx 2\sqrt{Dk}[1 - \pi^2/(2\ln^2N)]$ (Brunet and Derrida, 1997). A bistable front is pushed by the region where $u$ is of order one, which contains many individuals, so cutting off the tail changes little; its speed is set by $\int f\,\mathrm{d}u$, Theorem 36.5.1.

7. In the heterocyst model, how should the mean spacing depend on the decay length $\lambda$ and the threshold $\theta$ of the inhibitor? Check your answer with an estimate.

   **Answer** A new heterocyst forms in the middle of an interval of length $\ell$ when the inhibitor there, about $2\mathrm{e}^{-\ell/2\lambda}$ from the two flanking heterocysts, falls below $\theta$, that is when $\ell > 2\lambda\ln(2/\theta)$. With $\lambda = 2.5$ cells and $\theta = 0.15$, $\ell \approx 2 \times 2.5 \times 2.6 = 13$ cells at the moment of insertion; intervals range from about half of this (just after insertion) to $13$, so the mean is about $9$–$10$ cells, as in the simulation. The spacing is proportional to $\lambda$ and grows logarithmically as the threshold is lowered.

8. Derive the instability condition of Proposition 36.7.1 for the functions of the figure, $f(x) = x^2/(0.01 + x^2)$, $g(x) = 1/(1 + 100x^2)$, at the symmetric state $N^* \approx 0.35$, and say whether lateral inhibition would work with hyperbolic instead of sigmoidal functions.

   **Answer** $D^* = g(0.35) = 1/(1 + 12.25) = 0.0755$. $g'(N) = -200N/(1 + 100N^2)^2 = -70/175.6 = -0.399$. $f'(x) = 0.02x/(0.01 + x^2)^2$; at $x = 0.0755$, $0.01 + x^2 = 0.0157$, $f' = 0.00151/2.47\times10^{-4} = 6.1$. The gain is $6.1 \times 0.399 = 2.4 > 1$: unstable. With hyperbolic functions the loop gain cannot exceed one. At the fixed point $f(D^*) = N^*$ and $g(N^*) = D^*$, so $\lvert f'(D^*)g'(N^*)\rvert = \lvert\mathrm{d}\ln f/\mathrm{d}\ln D\rvert\,\lvert\mathrm{d}\ln g/\mathrm{d}\ln N\rvert$, the product of the logarithmic sensitivities of the two steps; for $f = x/(K_f + x)$ and $g = 1/(1 + N/K_g)$ each is smaller than one. Lateral inhibition therefore requires cooperativity (or another source of **ultrasensitivity**) somewhere in the loop, as the toggle switch does.

9. (Open) A colleague proposes that a stripe of protein localization in a cell is a Turing pattern. What measurements would support or refute this?

   **Answer** Test the signatures. A Turing (or mass-conserved) pattern forms spontaneously from a uniform state without a prepattern: look for symmetry breaking in cells or reconstituted systems lacking upstream cues. Its wavelength is intrinsic: in longer cells it should form more stripes rather than stretch, and changing diffusion or reaction rates (expression levels, as for MinD/MinE) should change the spacing predictably. The components should show the required interactions: self-enhancement and a faster-spreading inhibitor or a shared depleted pool, measurable by FRAP of membrane and cytosolic forms and by perturbing feedback. A pattern that follows an external template, scales with cell length while keeping one stripe, or persists when the dynamics are blocked is more likely templated (by a landmark, curvature or the cytoskeleton).
