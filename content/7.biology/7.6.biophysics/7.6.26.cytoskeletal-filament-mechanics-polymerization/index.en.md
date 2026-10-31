---
title: Mechanics and Polymerization Dynamics of Cytoskeletal Filaments
description: "The physics of actin filaments and microtubules as elastic beams and as polymers that assemble out of equilibrium. Stretching, bending and twisting energies, flexural rigidity and the second moment of area; stiffness of filaments in muscle, stereocilia and axonemes; flexural rigidity from thermal shapes by Fourier modes; Euler buckling and buckling in an elastic medium; equilibrium polymers, the nucleation penalty of multistranded filaments and the critical concentration; rate equations for seeded growth and length diffusion; the cost of treadmilling; cap models of catastrophe and aging; the Dogterom–Leibler steady state and the optimal catastrophe frequency for search and capture; thermodynamic stall force, the ideal Brownian ratchet as a first-passage problem, the elastic Brownian ratchet and the window of free lengths; many filaments sharing a load; strain stiffening of semiflexible networks."
---

The **cytoskeleton** is built from three kinds of protein polymer whose biology was described in [7.3.13](/7.3.13), [7.3.14](/7.3.14) and [7.3.15](/7.3.15): **actin filaments**, **microtubules** and **intermediate filaments**. Two physical facts make them interesting. They are elastic rods, a few nanometers thick and micrometers long, whose stiffness, measured in units of the thermal energy, sets whether they can bear compression, how they fluctuate and how they transmit force. And they assemble and disassemble by adding and losing subunits at their ends, a chemical process that, when coupled to nucleotide hydrolysis, operates away from equilibrium and can do mechanical work. This chapter treats both with the toy models of *Physical Biology of the Cell* and with the estimates of measured parameters. We start with beam theory: the energy of bending, the flexural rigidity of filaments and its measurement from thermal shapes (26.1), and buckling, the instability that limits how hard a filament can push (26.2). We then turn to polymerization: equilibrium polymers and why cytoskeletal filaments are multistranded (26.3), the consequences of hydrolysis for treadmilling and dynamic instability, including the models of the GTP cap and the search of microtubules for their targets (26.4), and the forces that growing filaments exert, from the thermodynamic stall force to the Brownian ratchets and the sharing of a load among many filaments (26.5). Networks of filaments, which stiffen dramatically when deformed, close the chapter (26.6). The **persistence length** and the **worm-like chain** were developed for DNA in [7.6.21](/7.6.21); the rate equations for binding in [7.6.3](/7.6.3); the **first-passage time** in [7.6.5](/7.6.5#sec-5.6). Motors that walk on these filaments are the subject of [7.6.27](/7.6.27) and [7.6.28](/7.6.28), and the mechanics of whole cells of [7.6.31](/7.6.31).

## 26.1. Filaments as Elastic Beams

### 26.1.1. Stretch, Bend and Twist

Filaments, flagella, stereocilia, DNA, even the cantilever of an atomic force microscope, have one dimension much larger than the other two, and such objects deform in three independent ways: they stretch along their axis, bend and twist. When a straight beam is bent into an arc of radius $R$, one line inside it, the neutral axis, keeps its length; a fiber at distance $z$ from it is stretched (or compressed, for $z < 0$) from length $L_0 = R\theta$ to $(R + z)\theta$, so its strain is

$$
\varepsilon(z) = \frac{z}{R}. \tag{26.1}
$$
With **Young's modulus** $E$, the elastic energy per volume is $\frac12E\varepsilon^2$, and integrating over the cross-section and the length gives the bending energy.

**Definition 26.1.1 (Flexural Rigidity)** The *flexural rigidity* of a beam is $EI$, the product of the Young's modulus of its material and the second moment of area of its cross-section, $I = \int z^2\,\mathrm{d}A$. A beam of length $L$ whose local curvature is $1/R(s) = \lvert\mathrm{d}\boldsymbol{t}/\mathrm{d}s\rvert$ has bending energy

$$
G_{\mathrm{bend}} = \frac{EI}{2}\int_0^L\frac{\mathrm{d}s}{R(s)^2} = \frac{EI}{2}\int_0^L\left\lvert\frac{\mathrm{d}\boldsymbol{t}}{\mathrm{d}s}\right\rvert^2\mathrm{d}s, \tag{26.2}
$$
where $\boldsymbol{t}$ is the unit tangent. In the biophysics literature $EI$ is often written $\kappa$ and called the bending stiffness of the filament.

Stretching by a strain $\varepsilon$ costs $\frac12 EA\varepsilon^2 L$ for a cross-section of area $A$, and twisting by an angle per length $\Omega$ costs $\frac12 GJ\Omega^2L$, with the shear modulus $G$ and the polar moment $J = \int r^2\,\mathrm{d}A$. For a solid rod of radius $r$, $A = \pi r^2$ and $I = \pi r^4/4$; for a tube of outer and inner radii $r_{\mathrm{o}}$ and $r_{\mathrm{i}}$, $I = \pi(r_{\mathrm{o}}^4 - r_{\mathrm{i}}^4)/4$. The fourth power is the main lesson: a thick filament is far stiffer to bending than a thin one of the same material, and putting the material at the periphery, as a tube does, maximizes $I$ for a given amount of protein.

**Example 26.1.1 (Why microtubules are tubes)** A microtubule has outer and inner radii $12.5$ and $7.5\,\mathrm{nm}$: $I = \pi(12.5^4 - 7.5^4)/4\,\mathrm{nm^4} = 1.7\times10^4\,\mathrm{nm^4}$. With $E \approx 1.9\,\mathrm{GPa}$, $EI = 3\times10^{-23}\,\mathrm{N\,m^2}$, close to the measured $2.6\times10^{-23}\,\mathrm{N\,m^2}$. A solid rod with the same cross-sectional area ($314\,\mathrm{nm^2}$, radius $10\,\mathrm{nm}$) would have $I = 7.9\times10^3\,\mathrm{nm^4}$, half as much. An actin filament, about $28\,\mathrm{nm^2}$ in cross-section and effectively a solid rod of radius $3\,\mathrm{nm}$, has $I \approx 64\,\mathrm{nm^4}$, 260 times less than a microtubule, which with $E \approx 1$–$2\,\mathrm{GPa}$ gives $EI \approx 0.7$–$1.3\times10^{-25}\,\mathrm{N\,m^2}$. The ratio of the measured rigidities, about 400, is mostly geometry: the two proteins are made of similar material.

| Property | Actin filament | Microtubule | Intermediate filament |
|---|---|---|---|
| Subunit and mass | actin, $42\,\mathrm{kDa}$ | $\alpha\beta$-tubulin dimer, $100\,\mathrm{kDa}$ | $40$–$180\,\mathrm{kDa}$ monomers; tetramers assemble |
| Structure | two-stranded helix ($2.75\,\mathrm{nm}$ rise per subunit along the filament) | 13 protofilaments (9–17 in vitro); $8\,\mathrm{nm}$ per dimer, $0.62\,\mathrm{nm}$ of length per dimer added | ropelike, 8 protofilaments, nonpolar |
| Diameter | $6$–$7\,\mathrm{nm}$ | $25\,\mathrm{nm}$ (lumen $15\,\mathrm{nm}$) | about $10\,\mathrm{nm}$ |
| Young's modulus | $\approx 2\,\mathrm{GPa}$ | $\approx 1.9\,\mathrm{GPa}$ | low in bending (strands slide) |
| Flexural rigidity $EI$ | $\approx 7\times10^{-26}\,\mathrm{N\,m^2}$ ($0.07\,\mathrm{pN\,\mu m^2}$) | $\approx 2.6\times10^{-23}\,\mathrm{N\,m^2}$ ($26\,\mathrm{pN\,\mu m^2}$) | $\sim 4\times10^{-27}\,\mathrm{N\,m^2}$ |
| Persistence length $EI/k_{\mathrm{B}}T$ | $10$–$17\,\mu\mathrm{m}$ | $1$–$6\,\mathrm{mm}$ | $0.5$–$3\,\mu\mathrm{m}$ |

With $\ell_{\mathrm{p}} = EI/k_{\mathrm{B}}T$, these rigidities are the persistence lengths of [Definition 15.3.1](/7.3.15#def-15.3.1) in 7.3.15 and of the worm-like chain of [7.6.21](/7.6.21#sec-21.3). At the scale of a cell, $10\,\mu\mathrm{m}$, a microtubule is a rigid rod, an actin filament a semiflexible polymer and an intermediate filament a flexible rope: strong in tension, useless in compression.

### 26.1.2. Stiffness of Filaments in Cells

Cells in which one kind of filament dominates the mechanics make it possible to estimate the stiffness of filaments in vivo, and the estimates agree with in-vitro measurements.

- Thin filaments of muscle: comparing the compliance of rigor muscle fibers at sarcomere lengths of $1.8$ and $2.4\,\mu\mathrm{m}$, which differ only in the length of the filament region not overlapped by myosin, gives a longitudinal stiffness of about $53\,\mathrm{pN\,nm^{-1}}$ for a $1\,\mu\mathrm{m}$ thin filament, $EA \approx 5\times10^{-8}\,\mathrm{N}$, and with the cross-section of actin and tropomyosin $E \approx 2.4\,\mathrm{GPa}$. Manipulating single filaments with glass microneedles gives $44\,\mathrm{pN\,nm^{-1}}$ per micrometer and $E \approx 2.3\,\mathrm{GPa}$.
- Stereocilia: a hair bundle pivots at the tapered bases of its stereocilia (Example 26.1.2).
- Axonemes: the flexural rigidity of relaxed sperm flagella, in which neighboring doublets are not cross-linked by dynein, divided by the number of microtubules, gives $(2$–$3)\times10^{-23}\,\mathrm{N\,m^2}$ per microtubule, the in-vitro value; in rigor, dynein cross-links the doublets and the axoneme is far stiffer.
- Keratin materials: hair, wool, nail, horn and the stratum corneum consist of keratin intermediate filaments in a protein matrix, with moduli of $1$–$10\,\mathrm{GPa}$ that depend on hydration: dry keratin is stiff because cross-links stop the strands from sliding.

**Example 26.1.2 (The stiffness of a hair bundle)** A bundle of $N = 50$ stereocilia deflected at a height $L = 7\,\mu\mathrm{m}$ has a stiffness of about $0.6\,\mathrm{mN\,m^{-1}}$. Each stereocilium rotates about its base, a taper of length $l \approx 1\,\mu\mathrm{m}$ and radius $a \approx 50\,\mathrm{nm}$ that contains only $n \approx 30$ actin filaments, cross-linked into a solid bundle. A short beam of rigidity $EI_{\mathrm{b}}$ and length $l$ bent through an angle $\phi$ stores $EI_{\mathrm{b}}\phi^2/2l$, so its rotational stiffness is $EI_{\mathrm{b}}/l$, and a force at height $L$ sees a translational stiffness $EI_{\mathrm{b}}/(lL^2)$ per stereocilium. If the filaments are spread over the disc of radius $a$, $I_{\mathrm{b}} = \sum A_{\mathrm{f}}z_i^2 \approx nA_{\mathrm{f}}a^2/4 = 30 \times 28\,\mathrm{nm^2} \times 625\,\mathrm{nm^2} = 5.3\times10^5\,\mathrm{nm^4}$. Then

$$
E = \frac{k_{\mathrm{bundle}}\,lL^2}{NI_{\mathrm{b}}} = \frac{6\times10^{-4} \times 10^{-6} \times 4.9\times10^{-11}}{50 \times 5.3\times10^{-31}}\,\mathrm{Pa} \approx 1\,\mathrm{GPa},
$$
the modulus of actin. Cross-linking is essential: thirty independent filaments would have $I = 30 \times 64\,\mathrm{nm^4}$, three hundred times less.

### 26.1.3. Flexural Rigidity from Thermal Shapes

The most direct measurement is to watch filaments fluctuate. For a filament confined to a plane, write its tangent angle $\theta(s)$ as a **Fourier series** in modes that satisfy the free-end conditions $\theta'(0) = \theta'(L) = 0$ (no torque at free ends).

**Formula 26.1.1 (Mode Analysis of Thermal Shapes)** With $\theta(s) = \sum_n a_n\sqrt{2/L}\cos(n\pi s/L)$, the bending energy (26.2) becomes $\frac{EI}{2}\sum_n a_n^2(n\pi/L)^2$, a sum of independent quadratic terms, and the **equipartition theorem** gives

$$
\langle a_n^2\rangle = \frac{k_{\mathrm{B}}T}{EI}\left(\frac{L}{n\pi}\right)^2 = \frac{L^2}{\ell_{\mathrm{p}}n^2\pi^2}. \tag{26.3}
$$
Each mode gives an independent estimate of $\ell_{\mathrm{p}}$ (Gittes, Mickey, Nettleton and Howard 1993).

The method has two virtues: the modes are statistically independent, so their variances are clean estimates, and it separates the signal from the measurement noise, which adds a variance that grows with $n$ (it is the noise of a derivative). In practice one uses the first few modes whose variance is well above the noise floor, determined by imaging rigid objects. Gittes and colleagues found $\ell_{\mathrm{p}} \approx 5\,\mathrm{mm}$ for taxol-stabilized microtubules and $18\,\mu\mathrm{m}$ for phalloidin-stabilized actin; unlabeled actin filaments are about half as stiff, and the rigidity of microtubules depends on how fast they grew, on bound proteins and on acetylation, which is one way cells regulate it. For microtubules only the first two or three modes are measurable (the figure): a $20\,\mu\mathrm{m}$ microtubule barely bends thermally.

![Flexural rigidity from thermal shapes (Formula 26.1.1). Filaments are simulated as two-dimensional worm-like chains with free ends and imaged by sampling every 0.5 µm with 20 nm localization noise. A: five simulated 10 µm actin filaments (ℓ_p = 17 µm). B: variances of the tangent-angle modes from 400 contours (points) against the prediction L²/(ℓ_p n²π²) (lines) for actin and for 20 µm microtubules (ℓ_p = 5 mm); dotted, the noise floor found by "imaging" straight rods. C: persistence length estimated from each mode, relative to the true value: correct where the signal exceeds the noise (most modes for actin, only n ≤ 3 for microtubules), underestimated where noise dominates](./plots/filament-modes.py)

## 26.2. Buckling

### 26.2.1. The Euler Instability

A filament that pushes, against a membrane or a load, is compressed, and a compressed rod is stable only up to a critical force. Consider a rod of length $L$ along $x$ with hinged ends (free to rotate, not to move sideways), loaded by a compressive force $F$, and let $y(x)$ be a small transverse displacement. Bending costs $\frac{EI}{2}\int(y'')^2\,\mathrm{d}x$, and because the arc length is fixed, a bent rod brings its ends closer by $\frac12\int(y')^2\,\mathrm{d}x$, so the load does work $\frac{F}{2}\int(y')^2\,\mathrm{d}x$.

**Theorem 26.2.1 (Euler Buckling)** A rod of flexural rigidity $EI$ and length $L$ with hinged ends is stable under a compressive force $F$ if and only if

$$
F < F_{\mathrm{c}} = \frac{\pi^2EI}{L^2}, \tag{26.4}
$$
and at $F_{\mathrm{c}}$ it buckles into the half sine wave $y \propto \sin(\pi x/L)$. For one end clamped and the other free, $F_{\mathrm{c}} = \pi^2EI/4L^2$; for both ends clamped, $4\pi^2EI/L^2$.

**Proof** Expand the displacement in the modes allowed by hinged ends, $y = \sum_n b_n\sin(n\pi x/L)$. By orthogonality,

$$
G = \frac{EI}{2}\int_0^L(y'')^2\,\mathrm{d}x - \frac{F}{2}\int_0^L(y')^2\,\mathrm{d}x = \frac{L}{4}\sum_n b_n^2\left(\frac{n\pi}{L}\right)^2\left[EI\left(\frac{n\pi}{L}\right)^2 - F\right].
$$
The straight rod ($b_n = 0$) is a minimum if every coefficient is positive, that is if $F < EI(n\pi/L)^2$ for all $n \ge 1$, the most restrictive being $n = 1$. At $F = F_{\mathrm{c}}$ the first mode costs no energy and for larger $F$ it lowers the energy, so the rod buckles into it. Other end conditions replace $L$ by an effective length: $2L$ for a cantilever (a clamped end and a free end form half of a hinged rod of length $2L$), $L/2$ for two clamped ends. $\square$

**Example 26.2.1 (How long can a filament be and still push?)** The longest hinged rod that bears a force $F$ is $L_{\max} = \pi\sqrt{EI/F}$. For an actin filament ($EI = 0.07\,\mathrm{pN\,\mu m^2}$) pushing with its thermodynamic stall force of about $7\,\mathrm{pN}$ (26.5.1), $L_{\max} = \pi\sqrt{0.01}\,\mu\mathrm{m} = 0.31\,\mu\mathrm{m}$, and at $1\,\mathrm{pN}$, $0.83\,\mu\mathrm{m}$. For a microtubule at $4\,\mathrm{pN}$, $L_{\max} = \pi\sqrt{6.5}\,\mu\mathrm{m} = 8\,\mu\mathrm{m}$. A $10\,\mu\mathrm{m}$ microtubule buckles at $2.6\,\mathrm{pN}$, the force of one motor or one growing end. This is why the cell builds pushing structures from short, branched actin filaments (the free length between branch points in a lamellipodium is $0.1$–$0.2\,\mu\mathrm{m}$) or from bundles, whose rigidity grows with the square of the number of filaments if they are cross-linked (Example 26.1.2), and why microtubules that grow against the cell cortex are seen to bend.

### 26.2.2. Buckling in an Elastic Medium

Microtubules in living cells bear compressive forces far above their Euler force without buckling into one large arc. Instead, they buckle into short wavelengths, a few micrometers, near the point where the force is applied (Brangwynne and colleagues 2006). The surrounding cytoskeleton acts as an elastic foundation: displacing the rod sideways by $y$ costs $\frac{\alpha}{2}y^2$ per unit length, with $\alpha$ of the order of the shear modulus of the medium.

**Formula 26.2.1 (Buckling on an Elastic Foundation)** A long rod on a foundation of stiffness $\alpha$ (force per length per displacement) has mode energies proportional to $EIq^4 - Fq^2 + \alpha$ for wave number $q$. The straight rod is stable for

$$
F < F_{\mathrm{c}} = 2\sqrt{\alpha EI}, \tag{26.5}
$$
independent of length, and it buckles with wavelength $\lambda_{\mathrm{c}} = 2\pi(EI/\alpha)^{1/4}$.

The minimum of $EIq^4 - Fq^2 + \alpha$ over $q$ lies at $q^2 = F/2EI$ with value $\alpha - F^2/4EI$, which becomes negative at $F = 2\sqrt{\alpha EI}$, where $q^* = (\alpha/EI)^{1/4}$. With $\alpha \approx 1\,\mathrm{kPa} = 10^3\,\mathrm{pN\,\mu m^{-2}}$ and $EI = 26\,\mathrm{pN\,\mu m^2}$, $F_{\mathrm{c}} = 2\sqrt{2.6\times10^4}\,\mathrm{pN} \approx 320\,\mathrm{pN}$ and $\lambda_{\mathrm{c}} = 2\pi(0.026)^{1/4}\,\mu\mathrm{m} = 2.5\,\mu\mathrm{m}$: a hundredfold reinforcement, and the wavelength observed in cells. The same reasoning explains why a stiff rod embedded in a softer matrix, such as a microtubule in an axon or a fiber in a composite, can carry loads that would buckle it in isolation, and why the wavelength rather than the length of the rod is then the relevant scale.

![Euler buckling of cytoskeletal filaments (Theorem 26.2.1, Formula 26.2.1; actin EI = 0.07 pN µm², microtubule 26 pN µm²). A: critical compressive force against length for hinged ends (solid) and for a clamped and a free end (dashed); dotted lines mark the stall force of an actin filament at c = 100 C_c (7 pN), the measured stall force of a growing microtubule (about 4 pN) and the threshold of a microtubule in a medium of stiffness α = 1 kPa (320 pN). B: buckled shape of a 20 µm microtubule with hinged ends, free (half a wave) and embedded (wavelength 2.5 µm). C: energy of a bending mode of wave number q, EIq⁴ − Fq² + α in units of α, below, at and above the embedded threshold; the mode that first reaches zero sets the wavelength](./plots/buckling.py)

## 26.3. Polymerization: Equilibrium and Rate Equations

### 26.3.1. Equilibrium Polymers

Before adding hydrolysis, consider passive assembly. Subunits $A_1$ form polymers $A_n$ by adding one subunit at a time, $A_n + A_1 \rightleftharpoons A_{n+1}$. In the simplest single-stranded model every step has the same dissociation constant $K$, because every step forms one identical bond, and the **law of mass action** gives $[A_{n+1}] = [A_n][A_1]/K$, hence $[A_n] = K(c_1/K)^n$ with $c_1 = [A_1]$. Because $c_1 < K$ for the sum to converge, polymers of every length are less abundant than shorter ones, and the length distribution is exponential. This model fails for cytoskeletal filaments in two ways (SH 14.2; PBoC 15.4.1). The mean length grows only as the square root of the total concentration: at a total concentration $100K$, polymers are about 10 subunits long, and filaments thousands of subunits long would need total concentrations millions of times above $K$, whereas cells contain actin at only $100$–$1000$ times its critical concentration. And the end of a single strand is no better a binding site than a free monomer, so oligomers form as readily as filaments grow and there is no distinction between nucleation and elongation.

Multistranded filaments behave differently. In a two-stranded filament each new subunit at the end forms two bonds, one along its protofilament and one to the neighboring protofilament, whereas the first subunits of a nucleus form fewer. The equilibrium constants of the first steps are smaller than those of elongation, which can be summarized by a nucleation penalty.

**Theorem 26.3.1 (Equilibrium Polymer with a Nucleation Penalty)** Let polymers of $n \ge 2$ subunits have concentrations $c_n = \sigma C_{\mathrm{c}}x^n$, where $x = c_1/C_{\mathrm{c}}$, $C_{\mathrm{c}}$ is the dissociation constant of elongation and $\sigma \le 1$ the nucleation penalty ($\sigma = 1$ for the single-stranded polymer). Then $x < 1$, the length distribution is exponential, and for a total subunit concentration $c_{\mathrm{T}}$ well above $C_{\mathrm{c}}$ the number-averaged polymer length is

$$
\langle n\rangle \approx \sqrt{\frac{c_{\mathrm{T}} - C_{\mathrm{c}}}{\sigma C_{\mathrm{c}}}}, \qquad c_1 \to C_{\mathrm{c}} . \tag{26.6}
$$

**Proof** The concentrations of polymers and of subunits in polymers are $\sum_{n\ge2}c_n = \sigma C_{\mathrm{c}}x^2/(1 - x)$ and $\sum_{n\ge2}nc_n = \sigma C_{\mathrm{c}}x^2(2 - x)/(1 - x)^2$, both finite only for $x < 1$. Conservation gives $c_{\mathrm{T}} = C_{\mathrm{c}}x + \sigma C_{\mathrm{c}}x^2(2 - x)/(1 - x)^2$. For $\sigma \ll 1$ the polymer term is negligible unless $1 - x$ is small; then $c_{\mathrm{T}} - C_{\mathrm{c}} \approx \sigma C_{\mathrm{c}}/(1 - x)^2$, so $1 - x \approx \sqrt{\sigma C_{\mathrm{c}}/(c_{\mathrm{T}} - C_{\mathrm{c}})}$ and the mean length, the ratio of the two sums, is $(2 - x)/(1 - x) \approx 1/(1 - x)$, which is Eq. (26.6). For $\sigma = 1$ the same estimate holds for $c_{\mathrm{T}} \gg C_{\mathrm{c}}$. $\square$

A small $\sigma$ thus does two things (the figure). It creates a sharp **critical concentration** ([Definition 13.2.4](/7.3.13#def-13.2.4)): below $C_{\mathrm{c}}$ almost nothing polymerizes, above it nearly every added subunit goes into polymer while the free subunit concentration stays at $C_{\mathrm{c}}$. And it makes polymers long, by the factor $\sigma^{-1/2}$: with $\sigma = 10^{-5}$ (actin, for which the elongation constant is about $0.1\,\mu\mathrm{M}$ and the weak nucleating bonds have dissociation constants of order $10^4\,\mu\mathrm{M}$), $c_{\mathrm{T}} = 10C_{\mathrm{c}}$ gives filaments of about 1000 subunits, $2.7\,\mu\mathrm{m}$. The penalty also explains why filaments grow at their ends. An oligomer of $m$ subunits diffuses so slowly that annealing of long fragments contributes little, and breaking a filament in the middle requires breaking several bonds at once, so changes of length are dominated by the addition and loss of single subunits at the ends. Finally, the penalty is a barrier to **nucleation**: starting from monomers, polymerization shows a lag, whose duration scales as $c^{-n^*/2}$ for a nucleus of $n^*$ subunits (Oosawa and Kasai), and cells control where filaments form by providing nucleators, such as the **Arp2/3 complex**, formins and the γ-tubulin ring complex, that bypass it.

### 26.3.2. Rate Equations

Above the critical concentration, an end grows at net rate $k_{\mathrm{on}}c - k_{\mathrm{off}}$ ([7.6.3](/7.6.3), Eq. (3.22)). In a closed volume the growing filaments deplete the free subunits, and the rate equation must include this.

**Formula 26.3.1 (Seeded Growth with Depletion)** $M$ seeds in a volume $V$ with initial subunit concentration $c_0$, each growing at one end, reach a mean length $n(t)$ (in subunits) with

$$
\frac{\mathrm{d}n}{\mathrm{d}t} = k_{\mathrm{on}}\left(c_0 - \frac{Mn}{V}\right) - k_{\mathrm{off}}, \qquad n(t) = \frac{V}{M}\left(c_0 - C_{\mathrm{c}}\right)\left(1 - \mathrm{e}^{-k_{\mathrm{on}}Mt/V}\right). \tag{26.7}
$$
Growth is linear at first, at $k_{\mathrm{on}}(c_0 - C_{\mathrm{c}})$, and stops when the free concentration reaches $C_{\mathrm{c}}$, after a time of order $V/k_{\mathrm{on}}M$; the final length is the excess subunit concentration divided by the seed concentration.

The rate equation describes the mean. The length of a single filament is a random walk with steps of one subunit: the probability $P_n(t)$ that a filament has $n$ subunits obeys the **master equation** $\dot P_n = k_{\mathrm{on}}c\,P_{n-1} + k_{\mathrm{off}}P_{n+1} - (k_{\mathrm{on}}c + k_{\mathrm{off}})P_n$, from which the mean grows at $(k_{\mathrm{on}}c - k_{\mathrm{off}})a$ and the variance at $(k_{\mathrm{on}}c + k_{\mathrm{off}})a^2$, so that the length diffuses with

$$
D_L = \frac{a^2}{2}\left(k_{\mathrm{on}}c + k_{\mathrm{off}}\right), \tag{26.8}
$$
where $a$ is the length added per subunit. At steady state ($c = C_{\mathrm{c}}$) the mean is constant but the spread keeps growing, and lengths diffuse.

**Example 26.3.1 (Equilibrium is too slow)** How long would an equilibrium filament take to change its length by $1\,\mu\mathrm{m}$ by fluctuations? At $c = C_{\mathrm{c}}$, $D_L = a^2k_{\mathrm{off}}$ per end. For actin, $a = 2.7\,\mathrm{nm}$ and $k_{\mathrm{off}} \approx 1\,\mathrm{s^{-1}}$ at both ends give $D_L \approx 2 \times 7.3\,\mathrm{nm^2\,s^{-1}}$, and $t = L^2/2D_L = 10^6/29\,\mathrm{s} \approx 10\,\mathrm{h}$ (PBoC). For a microtubule ($k_{\mathrm{on}} = 5\,\mu\mathrm{M^{-1}\,s^{-1}}$ per protofilament end, $10\,\mu\mathrm{M}$ tubulin, $a = 0.62\,\mathrm{nm}$), $D_L \approx 18\,\mathrm{nm^2\,s^{-1}}$ and the length wanders by only $\sqrt{2D_Lt} \approx 46\,\mathrm{nm}$ in a minute (SH). In cells, filaments grow and shrink by micrometers in seconds to minutes and their subunits turn over in minutes. Equilibrium polymerization cannot do this; nucleotide hydrolysis does.

![Equilibrium polymers and seeded growth (Theorem 26.3.1, Formula 26.3.1). A: mean length of polymers against total subunit concentration in units of C_c, for a single-stranded polymer (σ = 1) and for nucleation penalties σ = 10⁻³ and 10⁻⁵; dashed, Eq. (26.6). B: fraction of subunits in polymers: a small σ produces a sharp critical concentration. C: growth of 50 seeded actin filaments (plus-end rate constants 11.6 µM⁻¹ s⁻¹ and 1.4 s⁻¹, 2 µM actin, 1 nM seeds) simulated with the Gillespie algorithm (gray: five filaments; red: the mean) and the rate equation with depletion (dashed); once the free actin has fallen to C_c the mean stops growing while individual lengths keep diffusing](./plots/equilibrium-polymer.py)

## 26.4. Hydrolysis, Treadmilling and Dynamic Instability

### 26.4.1. The Cost of Breaking Detailed Balance

Actin is an ATPase and tubulin a GTPase whose activities are switched on by polymerization; the nucleotide cannot be exchanged in the polymer, so disassembly is not the reverse of assembly. [7.3.13](/7.3.13#sec-13.2.4) showed the consequences for actin: the two ends can have different critical concentrations, between which a filament treadmills ([Formula 13.2.2](/7.3.13#fml-13.2.2)). Three further consequences follow from the same broken symmetry (SH 14.2.2). Polarity becomes functional: one end can grow while the other shrinks. Nucleation is suppressed: if the nucleotide is hydrolyzed faster than a nucleus can form, nuclei behave as NDP polymers, whose critical concentration is high, so filaments can elongate from templates at subunit concentrations at which they cannot nucleate spontaneously, and the slowly hydrolyzed analog GMPCPP indeed promotes spontaneous nucleation of microtubules. And the steady state costs energy. **Treadmilling** at a flux $J$ of subunits per second hydrolyzes $J$ ATP, about $J \times 20\,k_{\mathrm{B}}T$ of free energy per second ([7.6.3](/7.6.3), Example 3.2.1). For a lamellipodium with $200$ filaments per micrometer of edge, each adding about a hundred subunits per second, this is $2\times10^4$ ATP per second per micrometer of edge, a modest part of the cell's ATP budget, but it is not free: the cytoskeleton is a dissipative structure, and its rapid turnover is bought with energy.

### 26.4.2. Models of the Cap

Microtubules switch between growth and shrinkage (**dynamic instability**, [Definition 14.2.1](/7.3.14#def-14.2.1)), and the switch is attributed to the loss of the **GTP cap** ([Definition 14.2.2](/7.3.14#def-14.2.2)). What sets the rate of catastrophes?

The simplest toy model (PBoC 15.4.4) lets hydrolysis proceed only at the boundary between the cap and the GDP lattice, at a fixed rate $1/\tau_{\mathrm{h}}$, so the boundary advances at $a/\tau_{\mathrm{h}}$ and a catastrophe occurs when it catches up with the tip. In a closed volume the tip slows as subunits are depleted, $\mathrm{d}x_{\mathrm{tip}}/\mathrm{d}t = a[k_{\mathrm{on}}(c_0 - Mx_{\mathrm{tip}}/aV) - k_{\mathrm{off}}]$ as in Eq. (26.7), and the catastrophe comes when this speed falls to $a/\tau_{\mathrm{h}}$, after a time

$$
t_{\mathrm{cat}} \approx \frac{V}{Mk_{\mathrm{on}}}\ln(\tau_{\mathrm{h}}k_{\mathrm{on}}c_0) \tag{26.9}
$$
(for $k_{\mathrm{off}} \ll k_{\mathrm{on}}c_0$). The model predicts that faster growth delays catastrophes, but also that all microtubules in a solution catastrophe together, which is not observed: neighbors grow and shrink independently.

A stochastic model removes the synchrony. Let every GTP subunit hydrolyze independently at rate $r$ and subunits add at rate $k = v/a$, and suppose that the tip is stable as long as at least one of its $m$ outermost subunits still carries GTP; a catastrophe is the first time all $m$ are GDP. The state of the $m$ terminal subunits is a Markov chain with $2^m$ states, and the mean time to catastrophe follows from its generator by the **first-passage time** methods of [7.6.5](/7.6.5#sec-5.6). For $m = 1$ the catastrophe frequency is simply $r$, independent of growth speed; for $m \ge 2$ it decreases with growth speed, roughly as $v^{-(m-1)}$, because faster growth replenishes the terminal subunits before all of them hydrolyze (the figure, panel A). Measured catastrophe frequencies do fall with growth velocity, but more weakly than such models with a single rate-limiting step predict at large $m$, and the lifetimes of growing microtubules are not exponential: young microtubules rarely catastrophe, and the distribution of lifetimes is fitted by a Gamma distribution with about three steps (Gardner and colleagues 2011). Microtubules age, presumably by accumulating defects at the tip (tapered or curled protofilaments) that each make the next catastrophe step possible. In a stochastic cap model in which the cap is long, catastrophes remain rare, memoryless events, so aging needs an additional slow variable of the tip, and its identity is an active question.

### 26.4.3. Dynamic Instability as a Search Strategy

[Formula 14.2.1](/7.3.14#fml-14.2.1) of 7.3.14 gives the Dogterom–Leibler steady state; its derivation shows where the exponential distribution and the condition for bounded growth come from. At steady state, with $p_{\mathrm{g}}$ and $p_{\mathrm{s}}$ the densities of growing and shrinking ends at length $L > 0$,

$$
-v_{\mathrm{g}}p_{\mathrm{g}}' - f_{\mathrm{cat}}p_{\mathrm{g}} + f_{\mathrm{res}}p_{\mathrm{s}} = 0, \qquad v_{\mathrm{s}}p_{\mathrm{s}}' + f_{\mathrm{cat}}p_{\mathrm{g}} - f_{\mathrm{res}}p_{\mathrm{s}} = 0 .
$$
Adding them gives $(v_{\mathrm{s}}p_{\mathrm{s}} - v_{\mathrm{g}}p_{\mathrm{g}})' = 0$, and since the net flux of length vanishes far away, $v_{\mathrm{s}}p_{\mathrm{s}} = v_{\mathrm{g}}p_{\mathrm{g}}$ everywhere. Substituting into the first equation, $v_{\mathrm{g}}p_{\mathrm{g}}' = -(f_{\mathrm{cat}} - f_{\mathrm{res}}v_{\mathrm{g}}/v_{\mathrm{s}})p_{\mathrm{g}}$: the distribution is exponential with mean $v_{\mathrm{g}}v_{\mathrm{s}}/(v_{\mathrm{s}}f_{\mathrm{cat}} - v_{\mathrm{g}}f_{\mathrm{res}})$ if the bracket is positive, and there is no steady state otherwise.

Why should a cell make its microtubules unstable? In prometaphase microtubules from the two spindle poles must find the kinetochores of every chromosome, small targets at unknown positions ([7.3.21](/7.3.21)). A microtubule that never catastrophed would grow in one direction forever; one that catastrophed too often would never reach a distant target. Holy and Leibler (1994) showed that there is an optimum.

**Theorem 26.4.1 (Optimal Catastrophe Frequency for Search and Capture)** Let $N$ microtubules nucleate from a pole in random directions, grow at $v_{\mathrm{g}}$, catastrophe at rate $f$, shrink back at $v_{\mathrm{s}}$ without rescue and renucleate at once. A target at distance $x$ that subtends a fraction $p$ of all directions is captured by a microtubule that grows toward it and reaches it before catastrophe. The mean capture time is approximately

$$
T(f) = \frac{1 + v_{\mathrm{g}}/v_{\mathrm{s}}}{pNf}\,\mathrm{e}^{fx/v_{\mathrm{g}}}, \tag{26.10}
$$
minimal at $f^* = v_{\mathrm{g}}/x$, where $T^* = \mathrm{e}\,(1 + v_{\mathrm{g}}/v_{\mathrm{s}})\,x/(pNv_{\mathrm{g}})$.

**Proof** A growth phase lasts an exponential time of mean $1/f$, so a microtubule pointing at the target reaches distance $x$ with probability $\mathrm{e}^{-fx/v_{\mathrm{g}}}$, and an attempt succeeds with probability $p\,\mathrm{e}^{-fx/v_{\mathrm{g}}}$. Attempts are independent; each lasts on average a growth phase plus the shrinkage of the length grown, $(1/f)(1 + v_{\mathrm{g}}/v_{\mathrm{s}})$ (neglecting the slightly shorter duration of successful attempts). The number of attempts until success is geometric, with mean $\mathrm{e}^{fx/v_{\mathrm{g}}}/p$, and $N$ microtubules search in parallel, which gives Eq. (26.10). Setting $\mathrm{d}\ln T/\mathrm{d}f = -1/f + x/v_{\mathrm{g}} = 0$ gives $f^*$. $\square$

With $x = 10\,\mu\mathrm{m}$, $v_{\mathrm{g}} = 10\,\mu\mathrm{m\,min^{-1}}$, $v_{\mathrm{s}} = 20\,\mu\mathrm{m\,min^{-1}}$, a kinetochore subtending $p = 4\times10^{-4}$ and $N = 500$, the optimum is one catastrophe per minute, a mean length equal to the distance to the target, and $T^* \approx 20\,\mathrm{min}$, the duration of prometaphase. Cells do raise catastrophe frequencies at mitosis, and the mean length of mitotic microtubules is comparable to the distance from pole to chromosomes. The estimate is marginal, however, for capturing all 46 chromosomes of a human cell, and simulations show that random search alone is too slow; a gradient of Ran-GTP around chromosomes that stabilizes microtubules growing toward them, and nucleation of microtubules at the chromosomes themselves, make capture fast enough (Wollman and colleagues 2005).

![Catastrophe and search (26.4.2–26.4.3). A: catastrophe frequency against growth velocity in stochastic cap models in which the tip catastrophes when its m outermost dimers are all hydrolyzed (dimers add at v/a, a = 8/13 nm; each GTP dimer hydrolyzes at rate r, chosen so that the frequency is 0.01 s⁻¹ at 1.5 µm min⁻¹): independent of velocity for m = 1, decreasing for m = 2 and 3. B: lifetimes of the growth phase with mean 100 s when catastrophe needs one step (exponential) or three sequential steps (Gamma distribution, the aging seen in experiments). C: mean time for 500 microtubules to capture a kinetochore at distance x (Theorem 26.4.1; v_g = 10, v_s = 20 µm min⁻¹, p = 4 × 10⁻⁴) against catastrophe frequency; dots mark the optimum f* = v_g/x](./plots/cap-catastrophe.py)

## 26.5. Force from Polymerization

### 26.5.1. The Thermodynamic Stall Force

A filament that grows against a load $F$ does work $F\delta$ for each subunit that moves the load by $\delta$. At equilibrium with the load, the work enters the free energy of adding a subunit like a Boltzmann factor.

**Formula 26.5.1 (Critical Concentration Under Load)** Against a compressive load $F$, the critical concentration of an end becomes

$$
C_{\mathrm{c}}(F) = C_{\mathrm{c}}\,\mathrm{e}^{F\delta/k_{\mathrm{B}}T}, \qquad\text{so that}\qquad F_{\mathrm{s}} = \frac{k_{\mathrm{B}}T}{\delta}\ln\frac{c}{C_{\mathrm{c}}} \tag{26.11}
$$
is the **stall force** at subunit concentration $c$: the chemical potential difference of a subunit, $k_{\mathrm{B}}T\ln(c/C_{\mathrm{c}})$, balances the mechanical work $F\delta$, as an electrochemical potential balances in the Nernst equation.

For actin, $\delta = 2.7\,\mathrm{nm}$ and $k_{\mathrm{B}}T/\delta = 1.5\,\mathrm{pN}$; at $c = 100C_{\mathrm{c}}$, $F_{\mathrm{s}} \approx 7\,\mathrm{pN}$, more than a myosin II head exerts. For a microtubule, a dimer adds $\delta = 8/13 = 0.62\,\mathrm{nm}$ of length on average, so the same concentration ratio gives about $30\,\mathrm{pN}$. Measured stall forces are smaller: about $3$–$4\,\mathrm{pN}$ for a single growing microtubule pushing a barrier (Dogterom and Yurke 1997), and about $1\,\mathrm{pN}$ per filament for small bundles of actin filaments (Footer and colleagues 2007). The discrepancy has several sources: the load is not shared equally among protofilaments or filaments (26.5.4), a filament stalled by force is more likely to catastrophe, and the measured force is limited by buckling (Example 26.2.1) and by the stiffness of the attachment.

### 26.5.2. The Brownian Ratchet

How does a growing tip push a load that blocks it? The load fluctuates thermally; when a fluctuation opens a gap of at least $\delta$ between the tip and the load, a subunit can enter, and the load cannot return. This is the **Brownian ratchet** of [Definition 13.4.1](/7.3.13#def-13.4.1) (Peskin, Odell and Oster 1993). Its speed has two limits, depending on whether the gap opens much faster than subunits add or much slower.

In the reaction-limited case the load equilibrates in the gap between additions, so the probability that the gap exceeds $\delta$ is the **Boltzmann factor** $\mathrm{e}^{-F\delta/k_{\mathrm{B}}T}$, and

$$
v = \delta\left(k_{\mathrm{on}}c\,\mathrm{e}^{-F\delta/k_{\mathrm{B}}T} - k_{\mathrm{off}}\right), \tag{26.12}
$$
which is [Formula 13.4.1](/7.3.13#fml-13.4.1) of 7.3.13 and vanishes at the thermodynamic stall force (26.11). In the opposite, diffusion-limited case, a subunit enters as soon as the gap reaches $\delta$.

**Theorem 26.5.1 (Ideal Diffusion-Limited Ratchet)** A load with diffusion coefficient $D$ pushed by a force $F$ toward a tip that grows by $\delta$ the instant the gap reaches $\delta$ moves at

$$
v = \frac{D}{\delta}\,\frac{\omega^2}{\mathrm{e}^{\omega} - 1 - \omega}, \qquad \omega = \frac{F\delta}{k_{\mathrm{B}}T}, \tag{26.13}
$$
which tends to $2D/\delta$ at zero load and decays as $\omega^2\mathrm{e}^{-\omega}$ at large load.

**Proof** After each addition the gap $x$ is $0$; it performs overdamped diffusion in the potential $U(x) = Fx$, reflected at $x = 0$ by the tip, until it first reaches $\delta$. By [Theorem 5.6.1](/7.6.5#thm-5.6.1) the mean first-passage time from a reflecting boundary at $0$ to an absorbing one at $\delta$ is

$$
T = \frac{1}{D}\int_0^\delta\mathrm{e}^{\beta U(y)}\int_0^y\mathrm{e}^{-\beta U(z)}\,\mathrm{d}z\,\mathrm{d}y = \frac{1}{D}\int_0^\delta\frac{\mathrm{e}^{\beta Fy} - 1}{\beta F}\,\mathrm{d}y = \frac{\delta^2}{D}\,\frac{\mathrm{e}^{\omega} - 1 - \omega}{\omega^2},
$$
with $\beta = 1/k_{\mathrm{B}}T$. The load advances $\delta$ per cycle, so $v = \delta/T$. As $\omega \to 0$, $\mathrm{e}^{\omega} - 1 - \omega \approx \omega^2/2$ and $v \to 2D/\delta$. $\square$

The ratchet speed is limited by the diffusion of the load: a bead of radius $0.5\,\mu\mathrm{m}$ in a medium thirty times as viscous as water has $D \approx 1.5\times10^{-14}\,\mathrm{m^2\,s^{-1}}$, and $2D/\delta \approx 10\,\mu\mathrm{m\,s^{-1}}$, a hundred times the speed of *Listeria*, so the ideal ratchet is fast enough. But it predicts that larger loads move more slowly, as $1/D$, whereas beads and bacteria of different sizes propelled by actin comet tails move at similar speeds, and the bacterium is attached to its tail rather than free to diffuse away from it. The resolution is that the filament, not the load, fluctuates.

### 26.5.3. The Elastic Brownian Ratchet

**Definition 26.5.1 (Elastic Brownian Ratchet)** In the *elastic Brownian ratchet* (Mogilner and Oster 1996) the gap between a load and the tip of a filament is opened by the thermal bending fluctuations of the filament's free end, not by the diffusion of the load: a filament inclined at an angle $\theta$ to the normal of the load bends away, a subunit adds to its tip, and the filament, straightening, pushes the load forward by $\delta\cos\theta$.

**Formula 26.5.2 (Speed of an Inclined Filament)** If the tip fluctuates fast compared with subunit addition, with an amplitude larger than $\delta$, a filament at angle $\theta$ moves the load at

$$
v(\theta) = \delta\cos\theta\left(k_{\mathrm{on}}c\,\mathrm{e}^{-F\delta\cos\theta/k_{\mathrm{B}}T} - k_{\mathrm{off}}\right), \tag{26.14}
$$
and at a load $F > k_{\mathrm{B}}T/\delta$ the fastest filaments are those at $\cos\theta^* = k_{\mathrm{B}}T/F\delta$ (for $k_{\mathrm{off}} \ll k_{\mathrm{on}}c$).

The inclined filament trades a shorter step for a smaller work per step: maximizing $\cos\theta\,\mathrm{e}^{-\omega\cos\theta}$ gives $\cos\theta = 1/\omega$. At $3\,\mathrm{pN}$ per filament ($\omega = 2$), $\theta^* = 60^\circ$, and in lamellipodia most filaments do point at about $\pm 35^\circ$ to the direction of protrusion, a geometry set by the $70^\circ$ branch angle of the Arp2/3 complex. The conditions of the formula define a window of free lengths $\ell$ (the length of filament between the tip and the last point at which it is attached to the network). The lateral fluctuation of a cantilever of length $\ell$ is $\langle y^2\rangle = k_{\mathrm{B}}T\ell^3/3EI$, which reaches $\delta^2$ at $\ell_{\min} = (3EI\delta^2/k_{\mathrm{B}}T)^{1/3} \approx 70\,\mathrm{nm}$; shorter filaments are too stiff to open a gap. Longer ones buckle: a cantilever bears at most $\pi^2EI/4\ell^2$, so $\ell_{\max} = \frac{\pi}{2}\sqrt{EI/F} \approx 0.4\,\mu\mathrm{m}$ at $1\,\mathrm{pN}$ and $0.19\,\mu\mathrm{m}$ at $5\,\mathrm{pN}$. The relaxation time of the fluctuation, $\zeta_\perp\ell^4/(12.4\,EI)$ with a drag $\zeta_\perp \approx 4\pi\eta/\ln(\ell/d)$ per length, is about a microsecond for $\ell = 100\,\mathrm{nm}$, far faster than subunit addition (every $10\,\mathrm{ms}$), as the formula assumes. The free lengths of filaments at the leading edge of lamellipodia, $50$–$200\,\mathrm{nm}$, lie in this window. Attachment matters too: in the *Listeria* comet tail some filaments are transiently bound to the bacterial surface through ActA and resist its advance, while detached ones push, the "tethered ratchet" (Mogilner and Oster 2003), which explains why the bacterium is held close to its tail while it moves.

![Force from polymerization (26.5). A: velocity against dimensionless load Fδ/k_BT for the reaction-limited ratchet (Eq. (26.12); actin at 10 µM, k_on c = 116 s⁻¹, k_off = 1.4 s⁻¹, stall at ln(c/C_c) = 4.4) and for the ideal diffusion-limited ratchet (Theorem 26.5.1), each normalized by its unloaded velocity. B: elastic Brownian ratchet (Formula 26.5.2): velocity of the load for filaments at four angles to its normal; at small loads perpendicular filaments are fastest, at large loads inclined ones. C: thermal lateral fluctuation of the free tip of an actin filament (clamped base, rms √(k_BTℓ³/3EI)) against free length, the step δ = 2.7 nm, and the lengths beyond which the filament buckles under 1 and 5 pN: the shaded window of free lengths, about 70–400 nm, in which a filament can push](./plots/polymerization-ratchet.py)

### 26.5.4. Many Filaments Sharing a Load

A lamellipodium pushes its membrane with $100$–$200$ filament tips per micrometer of edge, and a bead in a comet tail with hundreds. Membrane tension of $0.1\,\mathrm{mN\,m^{-1}}$ acting on the two membranes of a sheet-like lamellipodium amounts to a load of about $2\tau \times 1\,\mu\mathrm{m} = 0.2\,\mathrm{nN}$ per micrometer of edge, a pN or two per filament. How do filaments share such a load? [7.3.13](/7.3.13#sec-13.4.1) deferred the question to this chapter.

If the load were shared equally and instantly among $N$ filaments, each would feel $F/N$, and

$$
v = \delta\left(k_{\mathrm{on}}c\,\mathrm{e}^{-F\delta/Nk_{\mathrm{B}}T} - k_{\mathrm{off}}\right). \tag{26.15}
$$
In reality the load rests on the leading tips. With fast fluctuations of the load (the reaction-limited case), the gap above the leading tip is exponentially distributed with mean $k_{\mathrm{B}}T/F$, and a filament whose tip lags by $\Delta$ behind the leader can add a subunit without moving the load if $\Delta \ge \delta$, but must otherwise wait for a gap $\delta - \Delta$, with probability $\mathrm{e}^{-F(\delta - \Delta)/k_{\mathrm{B}}T}$. Simulations of this model (the figure) show that equal sharing is an upper bound, that staggered tips (whose lattices are offset by fractions of $\delta$, as for the protofilaments of a microtubule or randomly branched actin) push faster than aligned tips, and that, whatever the arrangement, the system stalls at $N$ times the stall force of one filament.

**Theorem 26.5.2 (Stall Force of $N$ Filaments)** For $N$ filaments that add and lose subunits of length $\delta$ against a common load in equilibrium with them, the stall force is

$$
F_{\mathrm{s}}^{(N)} = N\,\frac{k_{\mathrm{B}}T}{\delta}\ln\frac{c}{C_{\mathrm{c}}}, \tag{26.16}
$$
independent of the offsets between the filaments.

**Proof** Let filament $i$ contain $n_i$ subunits, so its tip is at $x_i = n_i\delta + \phi_i$ with fixed offset $\phi_i$, and let the load be at $h \ge \max_i x_i$. In equilibrium the statistical weight of a configuration is $\prod_i(c/C_{\mathrm{c}})^{n_i}\,\mathrm{e}^{-Fh/k_{\mathrm{B}}T}$; integrating over $h$ gives a weight proportional to $(c/C_{\mathrm{c}})^{\sum n_i}\,\mathrm{e}^{-F\max x_i/k_{\mathrm{B}}T}$. Translating every filament by one subunit increases $\sum n_i$ by $N$ and $\max x_i$ by $\delta$ and multiplies the weight by $(c/C_{\mathrm{c}})^N\mathrm{e}^{-F\delta/k_{\mathrm{B}}T}$. If this factor exceeds 1 the weights grow without bound along the direction of growth and the system advances; if it is less than 1 the distribution is normalizable and the system retreats or stays (the load pushes the filaments back). The boundary, where the factor equals 1, is Eq. (26.16). $\square$

The stall force is a thermodynamic quantity and so cannot depend on how the work is shared; the velocity under a given load, a kinetic quantity, can and does. This is why stall-force measurements on bundles of filaments that report about $1\,\mathrm{pN}$ per filament (26.5.1) indicate that not all filaments were pushing, rather than a failure of the thermodynamics. Branched actin networks reconstituted against a load respond by increasing their filament density, which raises the force they can bear (Bieling and colleagues 2016): the network adapts its number of pushers to the load.

![Several filaments pushing one load: Monte Carlo of the ratchet with rapid equilibration of the load (actin at 10 µM, δ = 2.7 nm). A: load velocity against total force for one filament and for four filaments with staggered (offsets δ/4) or aligned tips, against the equal-sharing formula (26.15) for N = 1 and 4 (lines): staggering helps, equal sharing is an upper bound. B: velocity against force per filament for random arrays of 1, 2, 4 and 8 filaments: all stall at the single-filament stall force per filament (dotted), as Theorem 26.5.2 requires, although at a given force per filament larger arrays move more slowly](./plots/load-sharing.py)

## 26.6. Networks of Semiflexible Filaments

The cell's mechanics is that of filament networks: the cortex, stress fibers, the dendritic network of the lamellipodium and the intermediate-filament cage around the nucleus, with mesh sizes of tens to hundreds of nanometers ([7.6.23](/7.6.23)). Cross-linked networks of semiflexible filaments, which are stiff on the scale of the mesh, have a striking property described qualitatively in [7.3.15](/7.3.15#sec-15.3.3): they stiffen under strain by orders of magnitude. The simplest model attributes this to the entropic elasticity of the segments between cross-links (MacKintosh, Käs and Janmey 1995; Storm and colleagues 2005).

A segment of contour length $\ell_{\mathrm{c}} \ll \ell_{\mathrm{p}}$ held at its ends is nearly straight, but its thermal undulations store some contour length. Expanding the transverse displacement in modes $\sin(n\pi s/\ell_{\mathrm{c}})$ in each of two directions, with energy $\frac{\ell_{\mathrm{c}}}{4}(EIq_n^4 + fq_n^2)$ per squared amplitude under a tension $f$, and applying equipartition gives the following.

**Formula 26.6.1 (Stored Length of a Semiflexible Segment)** Under tension $f$, the contour length stored in the undulations of a segment is

$$
\Delta\ell(f) = \sum_{n\ge1}\frac{k_{\mathrm{B}}T}{EI(n\pi/\ell_{\mathrm{c}})^2 + f} = \frac{\ell_{\mathrm{c}}^2}{\pi^2\ell_{\mathrm{p}}}\sum_{n\ge1}\frac{1}{n^2 + \phi}, \qquad \phi = \frac{f\ell_{\mathrm{c}}^2}{\pi^2EI}, \tag{26.17}
$$
which is $\ell_{\mathrm{c}}^2/6\ell_{\mathrm{p}}$ at zero force (using $\sum n^{-2} = \pi^2/6$) and falls as $\Delta\ell \approx \frac{\ell_{\mathrm{c}}}{2}\sqrt{k_{\mathrm{B}}T/f\ell_{\mathrm{p}}}$ for $\phi \gg 1$. The segment is a nonlinear spring with linear stiffness $-(\partial\Delta\ell/\partial f)^{-1} = 90\,k_{\mathrm{B}}T\ell_{\mathrm{p}}^2/\ell_{\mathrm{c}}^4$ (using $\sum n^{-4} = \pi^4/90$), and it becomes rigid when the stored length is pulled out.

If the network deforms affinely (every segment follows the macroscopic strain), the shear modulus is a sum of the segment stiffnesses projected on the shear direction, and for an isotropic network with filament length $\rho$ per volume the linear modulus is about

$$
G_0 \approx 6\,\frac{\rho\,EI\,\ell_{\mathrm{p}}}{\ell_{\mathrm{c}}^3}, \tag{26.18}
$$
a strong function of the cross-link spacing. Under a shear strain $\gamma$, segments oriented along the stretching diagonal are pulled toward full extension, their tension rises as $f \propto (\Delta\ell)^{-2}$, and the differential modulus $K = \mathrm{d}\sigma/\mathrm{d}\gamma$ rises with stress as $K \propto \sigma^{3/2}$ (the figure). For actin at $1\,\mathrm{mg\,mL^{-1}}$ ($\rho \approx 39\,\mu\mathrm{m}$ of filament per $\mu\mathrm{m}^3$) cross-linked every $1\,\mu\mathrm{m}$, $G_0 \approx 6 \times 39 \times 0.07 \times 17/1\,\mathrm{Pa} \approx 280\,\mathrm{Pa}$, the order of the moduli of reconstituted cross-linked actin networks, and the predicted $\sigma^{3/2}$ stiffening was observed in networks cross-linked by scruin (Gardel and colleagues 2004) and in networks of many biopolymers, including fibrin, collagen and neurofilaments (Storm and colleagues 2005). Real networks stiffen at larger strains (about $10\,\%$) than the affine model predicts ($\sim\ell_{\mathrm{c}}/\ell_{\mathrm{p}}$), because filaments also bend and rearrange non-affinely.

Two consequences matter for cells. A network stiffened by prestress is stiffer at rest: myosin motors that contract a cross-linked actin network prestress it and raise its modulus by up to a hundredfold (Koenderink and colleagues 2009), which is how a cell can tune its stiffness to that of its substrate without changing its composition. And a network that is soft for small deformations and stiff for large ones protects the cell against damage while allowing it to deform easily; intermediate-filament networks, which stiffen most and tolerate the largest strains, are the cell's last line of defense. The rheology of whole cells, with its power-law dependence on frequency, is treated in [7.6.31](/7.6.31).

![Strain stiffening of a cross-linked semiflexible network in the affine thermal model (Formula 26.6.1; actin, ℓ_p = 17 µm, 1 mg mL⁻¹, segments of contour length ℓ_c between cross-links, 3000 orientations). A: shear stress against shear strain for ℓ_c = 0.5, 1 and 2 µm: the stress diverges when the stored length of the most stretched segments is exhausted, at strains of a few percent. B: differential modulus against stress: a linear plateau G₀ ∝ ℓ_c⁻³ (2200, 280 and 35 Pa), then stiffening as K ∝ σ^{3/2} (dotted slope)](./plots/network-stiffening.py)

## Summary

| Topic | Key result |
|---|---|
| Beams (Definition 26.1.1, Eqs. (26.1)–(26.2)) | Strain $z/R$; bending energy $\frac{EI}{2}\int R^{-2}\,\mathrm{d}s$; $I = \pi r^4/4$ (rod), $\pi(r_{\mathrm{o}}^4 - r_{\mathrm{i}}^4)/4$ (tube) |
| Filament stiffness (Example 26.1.1, table, 26.1.2) | $E \approx 2\,\mathrm{GPa}$ for actin and tubulin; $EI$: actin $0.07$, microtubule $26\,\mathrm{pN\,\mu m^2}$; $\ell_{\mathrm{p}}$: $10$–$17\,\mu\mathrm{m}$, $1$–$6\,\mathrm{mm}$; muscle, stereocilia (Example 26.1.2), axonemes agree |
| Thermal shapes (Formula 26.1.1) | $\langle a_n^2\rangle = L^2/(\ell_{\mathrm{p}}n^2\pi^2)$; noise grows with $n$, use the first modes |
| Euler buckling (Theorem 26.2.1, Example 26.2.1) | $F_{\mathrm{c}} = \pi^2EI/L^2$; actin at $7\,\mathrm{pN}$: $L_{\max} = 0.3\,\mu\mathrm{m}$; microtubule $10\,\mu\mathrm{m}$: $2.6\,\mathrm{pN}$ |
| Elastic medium (Formula 26.2.1) | $F_{\mathrm{c}} = 2\sqrt{\alpha EI} \approx 320\,\mathrm{pN}$, $\lambda_{\mathrm{c}} = 2\pi(EI/\alpha)^{1/4} \approx 2.5\,\mu\mathrm{m}$ |
| Equilibrium polymers (Theorem 26.3.1) | $c_n = \sigma C_{\mathrm{c}}x^n$; $\langle n\rangle \approx \sqrt{(c_{\mathrm{T}} - C_{\mathrm{c}})/\sigma C_{\mathrm{c}}}$; small $\sigma$ gives a sharp critical concentration and long filaments |
| Rate equations (Formula 26.3.1, Eq. (26.8), Example 26.3.1) | Seeded growth saturates at $(c_0 - C_{\mathrm{c}})V/M$; $D_L = \frac{a^2}{2}(k_{\mathrm{on}}c + k_{\mathrm{off}})$; equilibrium fluctuations need hours per micrometer |
| Hydrolysis (26.4.1) | Polarity, nucleation suppression, treadmilling at $\sim 20\,k_{\mathrm{B}}T$ per subunit |
| Cap models (Eq. (26.9), 26.4.2) | Deterministic cap: synchronous catastrophes; stochastic $m$-subunit cap: $f_{\mathrm{cat}}$ falls with $v$ for $m \ge 2$; aging needs several steps |
| Search and capture (Theorem 26.4.1) | $T(f) \propto \mathrm{e}^{fx/v_{\mathrm{g}}}/f$, optimum $f^* = v_{\mathrm{g}}/x$; about $20\,\mathrm{min}$ for 500 microtubules |
| Stall force (Formula 26.5.1) | $F_{\mathrm{s}} = (k_{\mathrm{B}}T/\delta)\ln(c/C_{\mathrm{c}})$: actin $7\,\mathrm{pN}$, microtubule $30\,\mathrm{pN}$ at $c = 100C_{\mathrm{c}}$; measured smaller |
| Ratchets (Eq. (26.12), Theorem 26.5.1, Definition 26.5.1, Formula 26.5.2) | Reaction-limited $v = \delta(k_{\mathrm{on}}c\mathrm{e}^{-\omega} - k_{\mathrm{off}})$; ideal $v = (D/\delta)\omega^2/(\mathrm{e}^\omega - 1 - \omega)$; elastic: $\cos\theta^* = 1/\omega$, free lengths $70$–$400\,\mathrm{nm}$ |
| Many filaments (Eq. (26.15), Theorem 26.5.2) | Equal sharing is an upper bound; staggering helps; stall at $NF_{\mathrm{s}}$ for any arrangement |
| Networks (Formula 26.6.1, Eq. (26.18)) | $\Delta\ell = \ell_{\mathrm{c}}^2/6\ell_{\mathrm{p}}$; $G_0 \approx 6\rho EI\ell_{\mathrm{p}}/\ell_{\mathrm{c}}^3$; $K \propto \sigma^{3/2}$; prestress by myosin stiffens |

## Questions

1. Two filaments have the same mass per length; one is a solid rod of radius $3\,\mathrm{nm}$, the other a tube with walls of the same cross-sectional area and outer radius $6\,\mathrm{nm}$. Compare their flexural rigidities.

   **Answer** Area $\pi 3^2 = 28.3\,\mathrm{nm^2} = \pi(6^2 - r_{\mathrm{i}}^2)$ gives $r_{\mathrm{i}} = 5.2\,\mathrm{nm}$. $I_{\mathrm{rod}} = \pi 3^4/4 = 64\,\mathrm{nm^4}$; $I_{\mathrm{tube}} = \pi(6^4 - 5.2^4)/4 = \pi(1296 - 731)/4 = 444\,\mathrm{nm^4}$, seven times larger for the same material, because $I$ weights material by the square of its distance from the axis.

2. In Formula 26.1.1, the first mode of a $20\,\mu\mathrm{m}$ microtubule has $\langle a_1^2\rangle = 8\times10^{-3}\,\mu\mathrm{m}$. What is the root-mean-square sideways displacement of its ends relative to its middle, roughly, and why is the measurement difficult?

   **Answer** $\theta_{\mathrm{rms}} \approx a_1\sqrt{2/L} = \sqrt{8\times10^{-3} \times 2/20} = 0.028\,\mathrm{rad}$; integrated over half the length, the transverse displacement is of order $\theta L/\pi \approx 0.028 \times 20/\pi\,\mu\mathrm{m} \approx 0.2\,\mu\mathrm{m}$. That is comparable to the optical resolution and only a few times the localization error of a contour, so only the first two or three modes stand above the noise (the figure); longer microtubules or many images are needed.

3. A microtubule $15\,\mu\mathrm{m}$ long is clamped at the centrosome and pushes with its free end against the cell cortex. Above what force does it buckle in isolation? In a cell with an elastic cytoplasm of $\alpha = 0.5\,\mathrm{kPa}$?

   **Answer** Clamped–free: $F_{\mathrm{c}} = \pi^2EI/4L^2 = 9.87 \times 26/(4 \times 225)\,\mathrm{pN} = 0.29\,\mathrm{pN}$. In the medium, $F_{\mathrm{c}} = 2\sqrt{\alpha EI} = 2\sqrt{500 \times 26}\,\mathrm{pN} = 230\,\mathrm{pN}$ with wavelength $2\pi(26/500)^{1/4}\,\mu\mathrm{m} = 3.0\,\mu\mathrm{m}$, shorter than the microtubule, so the formula applies. Embedding raises the threshold almost a thousandfold.

4. Using Theorem 26.3.1, how does the mean length of an equilibrium polymer change if the total subunit concentration is doubled from $5C_{\mathrm{c}}$ to $10C_{\mathrm{c}}$, for $\sigma = 10^{-5}$? Why would a cell not control filament length this way?

   **Answer** $\langle n\rangle \approx \sqrt{(c_{\mathrm{T}} - C_{\mathrm{c}})/\sigma C_{\mathrm{c}}}$: $\sqrt{4\times10^5} = 630$ to $\sqrt{9\times10^5} = 950$, a factor 1.5. The length depends weakly on concentration, the distribution is exponential (broad), and the fluctuations are hours long (Example 26.3.1). Cells instead control the number of filaments by nucleation, their lengths by capping, severing and dynamic instability, and their turnover by hydrolysis, all faster and more precise.

5. In a seeded actin polymerization with $2\,\mu\mathrm{M}$ actin and $1\,\mathrm{nM}$ seeds (Formula 26.3.1, plus-end constants of the figure), what final length and what time constant do you expect?

   **Answer** $C_{\mathrm{c}} = 1.4/11.6 = 0.12\,\mu\mathrm{M}$. Final length $(2 - 0.12)\,\mu\mathrm{M}/1\,\mathrm{nM} = 1880$ subunits $\times 2.7\,\mathrm{nm} = 5.1\,\mu\mathrm{m}$. Time constant $1/(k_{\mathrm{on}}c_{\mathrm{seeds}}) = 1/(11.6 \times 10^{-3})\,\mathrm{s} = 86\,\mathrm{s}$, as in the simulation. Doubling the seeds halves both.

6. Prove that in the stochastic cap model with $m = 1$ the catastrophe frequency equals the hydrolysis rate $r$, whatever the growth velocity, and explain why $m = 2$ changes this.

   **Answer** With $m = 1$, the tip is stable while the terminal subunit is GTP. Adding a subunit replaces it with a new GTP subunit, which does not change the state; the only exit is hydrolysis of the terminal subunit, at rate $r$, so the waiting time is exponential with rate $r$, independent of $k$. With $m = 2$, the state "terminal GTP, penultimate GDP" can be rescued by an addition (which makes the old terminal subunit penultimate, still GTP); catastrophe requires both to hydrolyze before the next addition, roughly at rate $r \times r/(k + r)$ for $k \gg r$, which falls as $1/v$.

7. For the search-and-capture model, how does the optimal capture time change if the cell doubles its number of microtubules, and if the kinetochore is twice as far? Discuss what this implies for large cells such as frog eggs.

   **Answer** $T^* = \mathrm{e}(1 + v_{\mathrm{g}}/v_{\mathrm{s}})x/(pNv_{\mathrm{g}})$, and $p$ itself falls as $x^{-2}$ for a target of fixed size. Doubling $N$ halves $T^*$. Doubling $x$ multiplies $T^*$ by $2 \times 4 = 8$. In an egg hundreds of micrometers across, random search from the poles is hopeless; such cells nucleate spindle microtubules around chromosomes (Ran-GTP, augmin-dependent branching) instead of searching for them.

8. A filament grows at $10\,\mu\mathrm{M}$ actin against a load of $4\,\mathrm{pN}$. Compare the speeds of a filament perpendicular to the load and one at the optimal angle (Formula 26.5.2).

   **Answer** $\omega = F\delta/k_{\mathrm{B}}T = 4 \times 2.7/4.1 = 2.63$. Perpendicular: $v = 2.7\,\mathrm{nm}\,(116\,\mathrm{e}^{-2.63} - 1.4)\,\mathrm{s^{-1}} = 2.7 \times (8.4 - 1.4) = 19\,\mathrm{nm\,s^{-1}}$. Optimal: $\cos\theta^* = 1/2.63 = 0.38$ ($\theta^* = 68^\circ$): $v = 2.7 \times 0.38 \times (116\,\mathrm{e}^{-1} - 1.4) = 1.03 \times 41.3 = 42\,\mathrm{nm\,s^{-1}}$, about twice as fast.

9. Why must the stall force of $N$ filaments be $N$ times that of one, even when only the leading filament touches the load at any moment (Theorem 26.5.2)? What does a measured stall force of $1\,\mathrm{pN}$ per filament in a bundle of eight filaments imply?

   **Answer** Stall is an equilibrium: the load and the filaments exchange subunits and work without net motion, and the condition depends only on the free energy of moving the whole array forward by one subunit per filament, $Nk_{\mathrm{B}}T\ln(c/C_{\mathrm{c}}) - F\delta$, not on the order in which filaments add. A measured $8\,\mathrm{pN}$ for eight filaments, compared with a predicted $8 \times 7 = 56\,\mathrm{pN}$ at $c = 100C_{\mathrm{c}}$, means that the system was not at this equilibrium: filaments buckled, slipped, lost contact or stopped growing (the bundle was effectively one filament pushing), so the measurement reports the mechanics of the bundle rather than the thermodynamic limit.

10. (Experimental design) Propose an experiment to test the elastic Brownian ratchet against the original (load-diffusing) ratchet.

    **Answer** Reconstitute actin-based motility of beads coated with an Arp2/3 activator (such as ActA or the VCA domain of N-WASP) in purified proteins, and vary the bead size (hence its diffusion coefficient) by tenfold and the medium viscosity with an inert crowder. The load-diffusing ratchet predicts speeds proportional to $D$, decreasing with size and viscosity; the elastic ratchet predicts speeds nearly independent of $D$ but sensitive to the filament geometry, so vary also the free length of filaments (with capping protein, which shortens them) and their stiffness (with phalloidin). Measure force–velocity curves with an optical trap or a calibrated flexible fiber; the elastic model predicts the shift of optimal filament angles with load (cryo-electron tomography of the network at different loads) and a loss of motility when filaments are too short or too long.
