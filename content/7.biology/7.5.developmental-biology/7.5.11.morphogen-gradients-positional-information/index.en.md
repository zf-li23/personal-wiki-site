---
title: Morphogen Gradients and Positional Information
description: How cells learn where they are. Wolpert's positional information and the French flag problem; the definition and tests of a morphogen; one-component reaction-diffusion (Fick's law, boundary conditions, a Lyapunov functional, why an isolated tissue cannot hold a pattern with one substance, the energy integral and absolute versus relative regulation, the Fick-Jacobs equation); the synthesis-diffusion-degradation model, decay length and accumulation time; the Bicoid gradient and the precision of its readout; robustness and scaling (self-enhanced degradation, expansion-repression, opposing gradients); reading a gradient (cooperativity, bistable and sequential switches, contour control); and the limits of the simple threshold picture.
---

The previous chapters described how cells become different by inheriting different cytoplasm and by signaling to their neighbours. This chapter asks a sharper question: how does a field of initially equivalent cells produce a pattern whose parts lie in the right places and in the right proportions? The classical answer, formulated by Lewis Wolpert in 1969, is that cells first acquire a value that records their position and then interpret it, and that the value is often provided by the local concentration of a diffusing substance, a morphogen. We develop this idea quantitatively. A single diffusing substance, made at a source and removed in the tissue, gives an exponential gradient whose length is set by diffusion and degradation; we compute how fast it forms, how much information it can carry and how its readout can be made sharp, irreversible and robust. The *Drosophila* Bicoid gradient, the first morphogen to be visualized, serves as the running example; its biology is described in [7.5.14](/7.5.14), and the genetics of the segmentation genes it controls in [7.4.20](/7.4.20). The mathematics of diffusion is that of the **heat equation** ([2.5.7](/2.5.7)); the next chapter ([7.5.12](/7.5.12)) shows how two interacting substances can create a pattern without any source at all.

## 11.1. Positional Information and the French Flag Problem

Consider a line of cells, each of which can become blue, white or red, and suppose that the line always develops one third blue, one third white and one third red, whatever its length. This is Wolpert's French flag problem: the embryo must not only make different cell types but arrange them in proportion to the size of the tissue, as embryos that regulate do after the removal or addition of cells.

**Definition 11.1.1 (Positional Information)** A cell has **positional information** when it carries a **positional value**, a state that specifies its position relative to boundaries of the tissue (a source and a sink, or two ends), and interprets this value, according to its genetic program and developmental history, by choosing a fate. Patterning by positional information has two separable steps: the specification of positional values and their interpretation.

The separation has consequences that can be tested. The same positional values can be interpreted differently by different tissues, so that a common coordinate system yields different structures: a dorsal and a ventral imaginal disc of the fly use the same signals to make a wing and a leg. Conversely, a cell transplanted to a new position should change its positional value but keep its interpretation, and a cell transplanted to a different tissue should keep its value but interpret it in the new way. The regeneration of insect and amphibian limbs, in which missing positional values are restored by intercalation, provides the most direct evidence ([7.5.35](/7.5.35)).

**Definition 11.1.2 (French Flag Model)** In the **French flag model**, a morphogen is kept at a fixed concentration at one end of a line of cells and removed at the other; each cell reads the local concentration, its positional value, and adopts the first fate above a threshold $T_1$, the second between $T_1$ and $T_2$ and the third below $T_2$.

With a source held at $C_0$ at $x=0$, a sink held at $0$ at $x=L$ and no degradation in between, the steady concentration is linear, $C(x)=C_0(1-x/L)$, and the boundaries lie at $x_i=L(1-T_i/C_0)$: they are fixed fractions of $L$, and the flag scales with the tissue. If the tissue is cut, and the cut end becomes a new source or sink, the pattern also regenerates. If instead the morphogen is degraded throughout the tissue, the gradient has its own length scale and the boundaries are fixed distances from the source (Section 11.4): the flag does not scale.

![The French flag problem for two tissues of length 1 and 1.6 (dashed rows). Left: a source and a sink at the two ends give a linear gradient, and the thresholds T1 and T2 cut every tissue into thirds. Right: a source and degradation give an exponential gradient with a fixed decay length (here 0.4); the blue and white bands keep their absolute widths and the extra tissue becomes red](./plots/french-flag-scaling.py)

Positional information is one of several ways to make a pattern, and it is worth keeping the alternatives apart:

| Mechanism | How a stripe of red cells arises | Typical example |
|---|---|---|
| Cytoplasmic determinants | localized in the egg and inherited by particular cells | germ plasm, *C. elegans* P granules ([7.5.6](/7.5.6)) |
| Positional information | cells read the level of a graded signal | Bicoid, Dpp, Shh in the neural tube and limb |
| Self-organization | interactions among equivalent cells create a periodic pattern | Turing patterns, **lateral inhibition** ([7.5.12](/7.5.12)) |
| Sorting out | cells differentiate at random and then segregate by adhesion | **differential adhesion hypothesis** ([7.5.7](/7.5.7)) |

Real tissues combine them. In the fly embryo a maternal determinant (*bicoid* mRNA) gives rise to a gradient, which positional readout converts into domains, which cross-regulation then sharpens.

**Example 11.1.1** The logic of positional information explains a classical result with the *bicoid* mutant (a **maternal-effect gene**): eggs from mutant mothers develop no head or thorax, and anterior cytoplasm from wild-type eggs injected into the middle of a mutant egg induces head structures at the injection site, flanked on both sides by thoracic segments in mirror image. The injected cytoplasm acts as a new source: positions close to it receive high positional values (head), positions farther away lower ones (thorax), on both sides. A determinant that simply made cells "head" would give a head at the site but no mirror-image thorax.

## 11.2. Morphogens

**Definition 11.2.1 (Morphogen)** A **morphogen** is a substance whose concentration specifies cell fate in a dose-dependent manner: it is produced by a localized source, forms a graded distribution in the tissue, acts directly on the cells at a distance from the source, and elicits at least two different responses at different concentrations.

A morphogen is analog ("more or less"), a cytoplasmic determinant digital ("present or absent"). Each part of the definition corresponds to an experiment.

1. Graded distribution: The protein is visualized (antibody staining, GFP fusions) and its profile measured.
2. Dose dependence: Changing the amount of morphogen shifts the boundaries in the predicted direction: doubling the *bicoid* gene dose moves the anterior boundary of *hunchback* expression posteriorly; activin released from beads in *Xenopus* animal cap cells induces *goosecoid* at about 300 molecules per cell and *Xbra* at about 100.
3. Direct action at a distance: Clones of cells unable to receive the signal (lacking a receptor or an intracellular component) are made in the responding field. If the morphogen acts directly, only the mutant cells lose their response, wherever they are; if it acts through a relay, cells farther from the source, beyond a mutant clone, also lose it. Clones lacking the Dpp receptor Thickveins in the wing disc behave in the first way, which showed that Dpp acts directly over many cell diameters.

Morphogens now identified include transcription factors that diffuse in a syncytium (Bicoid, the nuclear gradient of Dorsal in the fly embryo), secreted proteins of the TGF-β family (Dpp and the BMPs, Nodal, activin), Wnt and Wingless, Hedgehog and Sonic hedgehog, FGFs, and small molecules such as retinoic acid. Secreted morphogens rarely diffuse freely: they bind heparan sulfate proteoglycans, receptors and extracellular partners, and may be carried by cytonemes ([7.5.3](/7.5.3)). The simplest description, which nevertheless explains most measured gradients, treats all of this as diffusion with an effective coefficient and an effective rate of removal.

## 11.3. One-Component Reaction–Diffusion

### 11.3.1. Fick's Law and Boundary Conditions

Let $A(\boldsymbol{r},t)$ be the concentration of a substance, $\boldsymbol{J}$ its flux (amount crossing unit area per unit time) and $f(A)$ its net local production. Conservation in a small volume gives $A_t=f(A)-\nabla\cdot\boldsymbol{J}$. If molecules hop between neighbouring volume elements of side $\mathrm{d}x$ at rate $\gamma$ in each direction, the net flux across a face is $\gamma\,\mathrm{d}x\,[A(\boldsymbol{r})-A(\boldsymbol{r}+\boldsymbol{e}_x\mathrm{d}x)]\to-\gamma(\mathrm{d}x)^2\,\partial_xA$, which is **Fick's law** $\boldsymbol{J}=-D\nabla A$ with $D=\gamma(\mathrm{d}x)^2$ (the random-walk derivation of [2.5.7](/2.5.7#sec-7.5.1)).

**Formula 11.3.1 (One-Component Reaction–Diffusion)** A substance with diffusion coefficient $D$ and net production $f(A)$ in a region $\Omega$ obeys

$$
A_t=f(A)+D\Delta A\quad\text{in }\Omega,\qquad \boldsymbol{n}\cdot\nabla A=-\alpha A\quad\text{on }\partial\Omega .
\tag{11.1}
$$
The boundary condition represents conversion of $A$, at rate $\gamma'$, into a species on the other side of the boundary, with $\alpha=\gamma'\mathrm{d}x/D$: a leaky boundary is a **Robin boundary condition**, $\alpha=0$ (no flux, an isolated tissue) the **Neumann boundary condition**, and $\alpha\to\infty$ an absorbing boundary $A=0$. A boundary source of strength $\beta$ is written $\boldsymbol{n}\cdot\nabla A=\beta$ (flux into the tissue).

### 11.3.2. A Lyapunov Functional

Scale $D=1$ and let $\varphi$ be an antiderivative of the production, $\varphi'(A)=f(A)$.

**Theorem 11.3.1** For (11.1) with $D=1$, the functional

$$
\mathcal{L}[A]=\int_\Omega\Big(\tfrac12\lvert\nabla A\rvert^2-\varphi(A)\Big)\mathrm{d}V+\frac\alpha2\oint_{\partial\Omega}A^2\,\mathrm{d}S
$$
satisfies $\frac{\mathrm{d}\mathcal{L}}{\mathrm{d}t}=-\int_\Omega\big(f(A)+\Delta A\big)^2\mathrm{d}V\le0$. If $\varphi$ is bounded above and $\Omega$ is bounded, $\mathcal{L}$ is bounded below, and every solution approaches the set of steady states.

**Proof** Differentiating under the integral, $\dot{\mathcal{L}}=\int_\Omega(\nabla A\cdot\nabla A_t-fA_t)+\alpha\oint AA_t$. By the **divergence theorem**, $\int_\Omega\nabla A\cdot\nabla A_t=\oint A_t\,\boldsymbol{n}\cdot\nabla A-\int_\Omega A_t\Delta A$, and the boundary term equals $-\alpha\oint AA_t$, which cancels the last term. Hence $\dot{\mathcal{L}}=-\int_\Omega A_t(f+\Delta A)=-\int_\Omega(f+\Delta A)^2$. $\square$

$\mathcal{L}$ is a **Lyapunov function** for the PDE ([2.4.11](/2.4.11)), and the dynamics is a gradient flow: the concentration slides downhill until $f(A)+\Delta A=0$. If that steady state is unique, a closed, bounded tissue always reaches it. In an unbounded domain $\mathcal{L}$ need not be bounded below, and the solution need not settle: the **traveling wave solutions** of the Fisher–KPP equation ([2.5.7](/2.5.7#sec-7.5.2)) are an example.

### 11.3.3. An Isolated Tissue Cannot Hold a Pattern

With no-flux boundaries there is always a uniform steady state $A_0$ with $f(A_0)=0$, stable if $f'(A_0)<0$: perturbations $\cos(p\pi x/L)\mathrm{e}^{\lambda t}$ decay with $\lambda=f'(A_0)-(p\pi/L)^2<0$. Nonuniform steady states may exist as well, but none can be stable.

**Theorem 11.3.2** On $0<x<L$ with $A_x(0)=A_x(L)=0$, every nonconstant steady state $A_1(x)$ of $A_t=f(A)+A_{xx}$ is unstable.

**Proof** A perturbation $A_1+\varepsilon g(x)\mathrm{e}^{\lambda t}$ requires $\lambda g=f'(A_1)g+g''$ with $g'(0)=g'(L)=0$. This is a Sturm–Liouville problem, whose largest **eigenvalue** is the maximum of the **Rayleigh quotient**,

$$
\lambda_{\max}=\max_{g}\int_0^L\big[f'(A_1)g^2-g'^2\big]\mathrm{d}x\quad\text{over }\int_0^Lg^2\,\mathrm{d}x=1,
$$
the maximum being taken over all smooth $g$ (the maximizer satisfies the natural boundary condition $g'=0$ automatically). Differentiating $f(A_1)+A_1''=0$ gives $f'(A_1)A_1'+A_1'''=0$, so $g_1=A_1'/\lVert A_1'\rVert$ satisfies $f'(A_1)g_1+g_1''=0$ with $g_1(0)=g_1(L)=0$. Multiplying by $g_1$ and integrating by parts (the boundary terms vanish because $g_1$ does), $\int_0^L[f'(A_1)g_1^2-g_1'^2]\,\mathrm{d}x=0$. Thus $\lambda_{\max}\ge0$. Equality would make $g_1$ a maximizer, hence a Neumann **eigenfunction** with $g_1'(0)=0$; together with $g_1(0)=0$ this forces $g_1\equiv0$ by uniqueness for the ODE, contradicting $\lVert g_1\rVert=1$. So $\lambda_{\max}>0$. $\square$

The same conclusion holds in several dimensions when the domain is convex (Casten and Holland; Matano), but stable patterns of one substance exist in non-convex domains such as two bulbs joined by a narrow neck. The biological lesson is general: a single substance in an isolated tissue cannot make a stable pattern. A pattern needs leakage at a boundary ($\alpha>0$), an explicit position dependence of production (a source), or a second substance (Chapter [7.5.12](/7.5.12)).

### 11.3.4. The Energy Integral: Absolute and Relative Regulation

In one dimension the steady state of $A''+\varphi'(A)=0$ can be found exactly. Multiplying by $A'$ and integrating once,

$$
\tfrac12A'^2+\varphi(A)=K,\qquad x=\int_{A(0)}^{A}\frac{\mathrm{d}A}{\sqrt{2(K-\varphi(A))}},\qquad L=\int_{A(0)}^{A(L)}\frac{\mathrm{d}A}{\sqrt{2(K-\varphi(A))}},
\tag{11.2}
$$
the analogue of a particle of unit mass moving in the potential $\varphi$ with "time" $x$ and energy $K$; with leaky boundaries the conditions $A'=\pm\alpha A$ become $\frac{\alpha^2}2A^2+\varphi(A)=K$ at both ends, and with $\alpha\to0$ simply $\varphi(A(0))=\varphi(A(L))=K$. The profile oscillates between the turning points $\varphi^{-1}(K)$, and the length $L$ fixes $K$. The form of $\varphi$ decides how the pattern responds to the size of the tissue.

**Proposition 11.3.1 (Absolute and Relative Regulation)** (a) Near a smooth minimum, $\varphi=\varphi_0+\frac{\omega^2}2(A-A_0)^2$, the steady state is $A=A_0+C\cos\omega x$: its wavelength $2\pi/\omega$ is set by the kinetics and does not change with $L$ (absolute regulation). (b) If $\varphi$ has a kink at $A_0$, $\varphi=\omega_1(A-A_0)$ for $A\ge A_0$ and $-\omega_2(A-A_0)$ for $A\le A_0$, then with $\frac12A'^2+\varphi=K^2$ the profile consists of two parabolas, $A=A_0+\sqrt2Kx-\frac{\omega_1}2x^2$ for $x\ge0$ and $A=A_0+\sqrt2Kx+\frac{\omega_2}2x^2$ for $x\le0$, between turning points at $x=\sqrt2K/\omega_1$ and $-\sqrt2K/\omega_2$. Hence

$$
L=\sqrt2K\Big(\frac1{\omega_1}+\frac1{\omega_2}\Big),
$$
and the point where $A=A_0$ divides every tissue in the fixed ratio $\omega_2:\omega_1$ (relative regulation).

**Proof** (a) $A''=-\omega^2(A-A_0)$ with $A'(0)=A'(L)=0$. (b) On each side $A''=-\varphi'(A)$ is constant, $-\omega_1$ or $+\omega_2$; the solutions pass through $A_0$ at $x=0$ with slope $\sqrt{2K^2}$ and stop where $A'=0$. $\square$

The kinked potential is not a curiosity: it is what a switch between two branches of production produces, and it reappears as the switch point of the Gierer–Meinhardt model ([7.5.12](/7.5.12)). In the smooth case, departures from constant curvature allow $L$ to differ from $n\pi/\omega$, but the shape $\cos\omega x$ persists.

![Steady patterns of one substance in tissues of two lengths. A: a smooth potential gives a fixed wavelength, so a tissue twice as long carries two half-cycles instead of one. B: a potential with a kink gives two parabolic pieces whose junction lies at the same fraction of the tissue for L = 1 and L = 2 (curves normalized by their amplitude coincide)](./plots/regulation-potentials.py)

### 11.3.5. Tissues of Varying Cross-Section: the Fick–Jacobs Equation

A one-dimensional description is natural for an elongated embryo or tube, but its cross-sectional area $a(x)$ usually varies. If the iso-concentration surfaces are nearly perpendicular to the axis, as they are for no-flux walls and a slowly varying cross-section, define the amount per unit length $P(x)=\int_{a(x)}\rho\,\mathrm{d}a=a(x)\rho$ and the axial current $J(x)=-Da(x)\rho_x$. Integrating $\rho_t+\nabla\cdot\boldsymbol{j}=S(\rho)$ over a slab and using the divergence theorem with no flux through the wall:

**Definition 11.3.1 (Fick–Jacobs Equation)** The **Fick–Jacobs equation** is the reduced reaction-diffusion equation

$$
P_t=\frac{\partial}{\partial x}\Big[Da(x)\frac{\partial}{\partial x}\frac{P}{a(x)}\Big]+a(x)S\Big(\frac{P}{a(x)}\Big)
\tag{11.3}
$$
for the amount $P$ per unit length in a channel of cross-section $a(x)$.

Writing $Da\,\partial_x(P/a)=D\partial_xP-D(\ln a)'P$ shows that the geometry acts as a drift towards the wider parts, an entropic force: at equilibrium without reaction, $P\propto a(x)$ and the concentration is uniform. Tapering ends of an embryo therefore modify the shape of a gradient even if the kinetics are uniform.

## 11.4. The Synthesis–Diffusion–Degradation Model

**Definition 11.4.1 (Synthesis–Diffusion–Degradation Model)** In the **synthesis–diffusion–degradation model** a morphogen enters the tissue at $x=0$ with flux $j$, diffuses with coefficient $D$ and is removed at a first-order rate $k$:

$$
C_t=DC_{xx}-kC,\qquad -DC_x(0,t)=j .
$$
Its steady state on a long tissue is $C_\infty(x)=\dfrac{j\lambda}{D}\mathrm{e}^{-x/\lambda}$, where the **decay length** $\lambda=\sqrt{D/k}$ is the distance over which the concentration falls by the factor $\mathrm{e}$. On a tissue of length $L$ with no flux at $x=L$,

$$
C_\infty(x)=\frac{j\lambda}{D}\,\frac{\cosh\big((L-x)/\lambda\big)}{\sinh(L/\lambda)} .
\tag{11.4}
$$

The decay length is set by how far a molecule diffuses in one lifetime: it lives on average for $1/k$ and in that time spreads a root-mean-square distance $\sqrt{2D/k}$ along the axis, so $\lambda = \sqrt{D/k}$ is this distance divided by $\sqrt 2$. In a syncytium the "degradation" may be binding: Bicoid entering nuclei, whose density $B$ grows at each division, is removed from the cytoplasm at rate $\gamma B$, so that $\lambda=\sqrt{D/\gamma B}$ shrinks as nuclei multiply unless the bound protein is released again. Boundaries then lie at

$$
x_i=\lambda\ln\frac{C_\infty(0)}{T_i},
\tag{11.5}
$$
and changing the source by a factor $m$ moves every boundary by $\lambda\ln m$ (see the robustness figure in Section 11.6). A gradient also has to be built before it can be read.

**Theorem 11.4.1 (Local Accumulation Time)** Starting from $C(x,0)=0$, define the local accumulation time $\tau(x)=\int_0^\infty\big[1-C(x,t)/C_\infty(x)\big]\mathrm{d}t$. On the half-line,

$$
\tau(x)=\frac1{2k}\Big(1+\frac x\lambda\Big).
$$

**Proof** Let $\tilde C(x,s)$ be the **Laplace transform** in $t$ ([2.5.6](/2.5.6)). Then $D\tilde C''=(s+k)\tilde C$ with $-D\tilde C'(0)=j/s$, so $\tilde C=\dfrac{j}{s\sqrt{D(s+k)}}\mathrm{e}^{-x\sqrt{(s+k)/D}}$. Since $\int_0^\infty[C_\infty-C]\,\mathrm{d}t=\lim_{s\to0}[C_\infty/s-\tilde C]$, we get $\tau=-\frac{\mathrm{d}}{\mathrm{d}s}\ln\big(s\tilde C\big)\big|_{s=0}=\frac1{2k}+\frac{x}{2\sqrt{Dk}}$. $\square$

The gradient forms from the source outward, and cells far away must wait several lifetimes; a cell three decay lengths away needs twice the lifetime, four times as long as a cell at the source.

![Formation of a synthesis-diffusion-degradation gradient (units: decay length 1, lifetime 1). A: profiles after the source is switched on approach the exponential steady state, near the source first. B: the local accumulation time computed from the simulation agrees with Theorem 11.4.1](./plots/sdd-buildup.py)

**Example 11.4.1** The Bicoid gradient has $\lambda\approx100\,\mathrm{\mu m}$, about 20 % of the $500\,\mathrm{\mu m}$ egg, and is read within about 2 h of fertilization. If $D$ were $0.3\,\mathrm{\mu m^2\,s^{-1}}$, the value first obtained by photobleaching, then $k=D/\lambda^2=3\times10^{-5}\,\mathrm{s^{-1}}$, a lifetime of 9 h, and by Theorem 11.4.1 the middle of the egg ($x=2.5\lambda$) would need $\tau=1.75/k\approx16\,\mathrm{h}$: the gradient could not form in time. Fluorescence correlation measurements later gave $D\approx7\,\mathrm{\mu m^2\,s^{-1}}$ for the mobile fraction, and photoconvertible tags a lifetime of the order of 30–60 min. With $D=4\,\mathrm{\mu m^2\,s^{-1}}$ and $1/k=40\,\mathrm{min}$, $\lambda=\sqrt{4\times2400}\,\mathrm{\mu m}\approx98\,\mathrm{\mu m}$ and $\tau(2.5\lambda)\approx70\,\mathrm{min}$: consistent. Simple order-of-magnitude checks of this kind resolved a long-standing paradox.

## 11.5. The Bicoid Gradient

*bicoid* mRNA is localized at the anterior pole during oogenesis and translated after egg activation; the protein moves through the syncytial embryo and enters the nuclei, where it acts as a transcription factor ([7.5.14](/7.5.14)). Three quantitative facts make it the reference morphogen.

1. The profile is exponential and the readout is threshold-like. Driever and Nüsslein-Volhard (1988) showed that the protein forms an exponential gradient and that increasing the maternal dose shifts the *hunchback* boundary and the cephalic furrow posteriorly. By (11.5) a doubling should move a threshold by $\lambda\ln2\approx0.14$ egg lengths; the *hunchback* boundary moves roughly this way, but later landmarks such as the cephalic furrow move less, because gap gene cross-regulation buffers the pattern ([7.5.15](/7.5.15)).
2. The readout is precise. Gregor, Tank, Wieschaus and Bialek (2007) measured Bicoid–GFP in living embryos: neighbouring nuclei at the *hunchback* boundary differ in Bicoid by only about 10 %, yet the boundary is placed with an error of about 1 % of egg length, one nuclear spacing.
3. The gradient scales between species. In flies with eggs of different length (*Lucilia*, *Calliphora*), $\lambda$ is roughly proportional to egg length, while Bicoid proteins from these species expressed in *D. melanogaster* form a *D. melanogaster*-sized gradient: scaling is a property of the egg, not of the protein.

**Formula 11.5.1 (Positional Error)** If the concentration at a cell fluctuates with standard deviation $\sigma_C$, the position inferred from it has error

$$
\sigma_x=\frac{\sigma_C}{\lvert C'(x)\rvert}=\lambda\,\frac{\sigma_C}{C}\quad\text{(exponential gradient)} .
$$

A relative error of 10 % thus corresponds to $0.1\lambda\approx10\,\mathrm{\mu m}$, about one nucleus; a steeper gradient (smaller $\lambda$) or a less noisy readout is more precise. How small can $\sigma_C/C$ be? A receptor (here a binding site of size $a$) that counts molecules diffusing with coefficient $D$ at concentration $c$ for a time $\tau$ cannot do better than the Berg–Purcell limit $\sigma_C/C\gtrsim(Dac\tau)^{-1/2}$. With $D=1\,\mathrm{\mu m^2\,s^{-1}}$, $a=3\,\mathrm{nm}$ and $c\approx3\,\mathrm{molecules\,\mu m^{-3}}$ (about 5 nM, the Bicoid level at the boundary), reaching 10 % takes $\tau\approx100/(1\times0.003\times3)\,\mathrm{s}\approx3\,\mathrm{h}$, longer than the interphases of the syncytium. Nuclei must therefore average over many binding sites, over time across divisions, or over their neighbours (through the diffusion of Hunchback mRNA and protein), and the measured precision is close to what the physics allows.

## 11.6. Robustness and Scaling

A gradient that shifts every boundary by $\lambda\ln2$ when the source doubles is fragile; real embryos tolerate halving of many morphogen genes. Two kinds of property are needed. A gradient is robust if its readout is insensitive to the source strength and other parameters; it scales if its readout keeps the same proportions in tissues of different size.

**Definition 11.6.1 (Self-Enhanced Degradation)** A morphogen shows **self-enhanced degradation** when its own signaling increases its rate of removal, so that the effective degradation rate grows with concentration, $C_t=DC_{xx}-kC^n$ with $n\ge2$.

Hedgehog induces its receptor Patched, which binds and internalizes it, and Wingless lowers the levels of a receptor that stabilizes it: both are examples.

**Proposition 11.6.1** For $n=2$ and influx $j$ at $x=0$ on the half-line, the steady state is

$$
C(x)=\frac{6D}{k(x+\varepsilon)^2},\qquad \varepsilon=\Big(\frac{12D^2}{kj}\Big)^{1/3} .
$$
A threshold $T$ is crossed at $x_T=\sqrt{6D/kT}-\varepsilon$, and doubling $j$ moves it by $\varepsilon(1-2^{-1/3})\approx0.21\varepsilon$.

**Proof** Try $C=B(x+\varepsilon)^{-m}$: $DC''=DBm(m+1)(x+\varepsilon)^{-m-2}$ must equal $kB^2(x+\varepsilon)^{-2m}$, so $m=2$ and $B=6D/k$. The flux condition $-DC'(0)=2DB\varepsilon^{-3}=j$ gives $\varepsilon$. $\square$

Far from the source the power-law tail $6D/(kx^2)$ forgets the source altogether: a strong source only shortens $\varepsilon$. With linear degradation the shift is $\lambda\ln2\approx0.69\lambda$, with self-enhanced degradation a fraction of $\varepsilon$, which is small whenever the source is strong. Robustness against the source is bought at the price of a gradient that is shallow at a distance, and hence less precise there (Formula 11.5.1).

Other robust designs use a second molecule. An antagonist secreted from the opposite side, or from the source itself but diffusing farther, binds the ligand and adds a removal term that increases with distance: the gradient becomes steeper away from the source, as Sog does for Dpp and Chordin for BMP. When the antagonist is cleaved only after carrying the ligand, the ligand is shuttled and concentrated at a distance from where it is made ([7.5.14](/7.5.14), [7.5.16](/7.5.16)).

Scaling requires that the decay length be tied to the size of the tissue. In the expansion–repression mechanism of Ben-Zvi and Barkai (2010), the morphogen represses the production of a long-lived, widely diffusing "expander" that, in turn, slows the removal of the morphogen. The expander accumulates as long as some part of the tissue lies below the repression threshold $T$, and stops when the far end reaches it; if the expander is nearly uniform, the condition $C_\infty(L)=T$ in (11.4) fixes

$$
\frac{j\lambda/D}{\sinh(L/\lambda)}=T ,
$$
so $\lambda$ grows with $L$ (for $L\gg\lambda$, $L/\lambda\approx\ln(2j\lambda/DT)$, a slowly varying ratio). The model makes a testable prediction: the gradient in a large tissue should take longer to form, because the expander must accumulate. The BMP gradient of the *Xenopus* embryo, in which the BMP-like ADMP and the antagonist Chordin play these roles, and the Dpp gradient of the growing wing disc are the best-studied cases ([7.5.16](/7.5.16), [7.5.33](/7.5.33)).

![Robustness and scaling (D = 1). A: with linear degradation, doubling the influx shifts the threshold position by ln 2 decay lengths. B: with self-enhanced degradation and a strong source, the far part of the profile hardly depends on the influx, and the shift is about a tenth as large. C: expansion-repression in the quasi-steady limit: the decay length grows with the tissue (lambda / L from 0.31 to 0.23 as L grows from 2 to 8), so profiles plotted against x / L remain similar, whereas a fixed decay length (dashed) gives a pattern compressed towards the source](./plots/robustness.py)

A third design uses two gradients from opposite ends, $C_1=\mathrm{e}^{-x/\lambda}$ and $C_2=\mathrm{e}^{-(L-x)/\lambda}$, and a readout of their ratio. The boundary $C_1/C_2=r$ lies at $x^*=\frac L2-\frac\lambda2\ln r$: it stays near the middle in tissues of any size, and in the middle the position error is halved because the ratio changes twice as fast as either gradient. In the fly, Bicoid from the anterior and maternal Caudal and Nanos activities from the posterior provide such a pair.

## 11.7. Reading the Gradient

### 11.7.1. Cooperativity and Sharp Boundaries

A target gene whose enhancer binds $n$ morphogen molecules cooperatively responds as a **Hill equation** $C^n/(C^n+K^n)$ ([7.1.7](/7.1.7)). Along an exponential gradient, with $x_T=\lambda\ln(C_0/K)$, this becomes

$$
\frac{C^n}{C^n+K^n}=\frac1{1+\mathrm{e}^{n(x-x_T)/\lambda}},
$$
a logistic function of position whose width (from 90 % to 10 %) is $4.4\,\lambda/n$: **cooperativity** compresses the boundary by the factor $n$. The proximal *hunchback* enhancer has six or seven Bicoid binding sites, and the measured input–output relation corresponds to $n\approx5$, so a boundary of a few nuclei arises from a gradient that decays over a fifth of the egg. Such **ultrasensitivity** ([7.3.18](/7.3.18)) sharpens a boundary but does not make it irreversible: when the morphogen falls, the target turns off.

![Reading a gradient. A: target activity along an exponential gradient for Hill coefficients 1, 2 and 5. B: stepwise binding P + S to PS and PS + S to PSS with K1 = 10 and K2 = 0.1; the singly bound state peaks at S* = 1, marking an internal contour. C: boundary position as a fraction of tissue length for a single gradient and for the ratio of two opposing gradients](./plots/readout.py)

### 11.7.2. A Two-Level Switch

A gene that should stay on after a transient signal needs **bistability** ([7.3.18](/7.3.18)). Consider a product $g$ (a derepressor of the target gene) that activates its own production cooperatively and is degraded, with an input $s=\gamma a$ proportional to the activator $a$:

$$
\dot g=s+\frac{g^2}{1+g^2}-\frac g{2K},\qquad K\ge1 .
\tag{11.6}
$$

**Proposition 11.7.1** For $s=0$, (11.6) has steady states $g=0$ and $g=K\pm\sqrt{K^2-1}$; $0$ and $K+\sqrt{K^2-1}$ are stable, $K-\sqrt{K^2-1}$ unstable. Let $s^*=\max_{0\le g\le K-\sqrt{K^2-1}}\big[g/2K-g^2/(1+g^2)\big]$. For $s>s^*$ the only steady state is the high one; once reached, it persists when $s$ returns to $0$.

**Proof** Steady states satisfy $g/2K=g^2/(1+g^2)$, i.e. $g=0$ or $g^2-2Kg+1=0$. The derivative of the right side at $g$ is $2g/(1+g^2)^2-1/2K$, which is $-1/2K<0$ at $0$. At the two other roots, using $1+g^2=2Kg$, it equals $\frac1{2Kg}-\frac1{2K}=\frac{1-g}{2Kg}$: positive at $K-\sqrt{K^2-1}<1$ and negative at $K+\sqrt{K^2-1}>1$. With $s>0$ the steady states are the solutions of $s=g/2K-g^2/(1+g^2)$; the low branch exists only while $s\le s^*$. After $s$ is removed, the system is in the basin of the high state. $\square$

The switch converts a graded, transient input into an all-or-none, permanent output: cells that have once seen activator above the threshold remember it. Development uses such memory everywhere, from the maintenance of *engrailed* expression to the Polycomb-dependent silencing of *Hox* genes ([7.5.15](/7.5.15)).

### 11.7.3. Multilevel Switches

How can one gradient specify several states, each with a single gene on? Suppose genes $g_i$ are autocatalytic and share a common repressor $r$ that all of them produce:

$$
\dot g_i=\frac{c_ig_i^2}{r}-\gamma g_i,\qquad \dot r=\sum_ic_ig_i^2-\beta r,\qquad \beta>\gamma .
$$
Steady states have each $g_i$ either $0$ or $\gamma r/c_i$. If gene $i$ alone is on, $g_i=\beta/\gamma$ and $r=\beta c_i/\gamma^2$; the Jacobian (rows $g$ and $r$) has $\partial\dot g_j/\partial g_j=-\gamma<0$ for the silent genes, while for the active gene and $r$ the block $\begin{bmatrix}\gamma&-\gamma^2/c_i\\2\beta&-\beta\end{bmatrix}$ has trace $\gamma-\beta<0$ and determinant $\gamma\beta>0$. Every state with exactly one gene on is stable: the common repressor enforces mutual exclusion, and the system can store as many states as there are genes. A graded activator must now select among them. In Meinhardt's version of this "analog–digital converter", graded levels of a signal $h$ act through

$$
\dot q_i=c_i\frac{q_i^2}{r}\Big(1+\frac hr\Big)-\frac{\alpha q_i}{1+\gamma q_i^2},\qquad \dot r=\sum_ic_iq_i^2-\beta r,
$$
and as $h$ rises, successive $q_i$ are switched on and then off, leaving one gene active at each level. A transparent way to obtain this behaviour is a ratchet: let gene $i-1$, when on, activate gene $i$ at a rate $e_i(m)$ that rises steeply with the morphogen $m$ above a threshold $\theta_i$. With $c=\beta=\gamma=1$ and $r$ fast, an active gene $g_{i-1}=1$ holds a small level of $g_i$, given by $g_i^2-g_i+e_i=0$, as long as $e_i<\frac14$; beyond that the small root disappears, $g_i$ grows, takes over the repressor and silences $g_{i-1}$. A cell exposed to a rising morphogen thus climbs the sequence of states up to the highest threshold it has passed and stays there when the morphogen declines (panels C and D of the figure below).

![Switches that read a gradient. A: steady states of the two-level switch (11.6) with K = 2 (solid stable, dashed unstable); above s* only the high state exists. B: a transient input above s* switches the gene on permanently. C: a sequential switch of four genes sharing a repressor, in cells along an exponential gradient: each cell ends in the state set by the highest threshold it has passed, a four-coloured French flag. D: the hand-over from gene to gene in one cell as the morphogen rises](./plots/switches.py)

### 11.7.4. Contour Control

A gradient can also mark an internal line rather than a boundary between two halves. Let a regulatory protein $P$ bind the morphogen $S$ in two steps, $P+S\rightleftharpoons PS$ and $PS+S\rightleftharpoons PSS$, with association constants $K_1$, $K_2$. At equilibrium the fractions of $P$, $PS$ and $PSS$ are proportional to $1:K_1S:K_1K_2S^2$, so

$$
\frac{[PS]}{[P]_{\mathrm{tot}}}=\frac{K_1S}{1+K_1S+K_1K_2S^2},
$$
which is maximal at $S^*=(K_1K_2)^{-1/2}$ with peak value $\sqrt{K_1/K_2}/(1+2\sqrt{K_1/K_2})$. If $PS$ is the active complex, a monotone gradient produces a stripe of activity around the contour $S=S^*$, the sharper the larger $K_1/K_2$. With two morphogens $S$ and $T$ and an active complex $PST$, the activity peaks on a surface defined by a balance of $S$ and $T$; MacWilliams used such rules to generate bone-like shapes with sockets from simple sources. Many enhancers combine activator and repressor sites in the same way: the *even-skipped* stripe 2 enhancer is activated by Bicoid and Hunchback and repressed by Giant and Krüppel on either side ([7.5.15](/7.5.15)).

### 11.7.5. Time as Well as Concentration

Cells integrate a signal over time as well as read its level. In the vertebrate neural tube, progenitors exposed to Sonic hedgehog adopt progressively more ventral identities the higher the concentration and the longer the exposure, and they adapt by upregulating Patched, so that the duration of signaling, not only its peak, encodes position ([7.5.18](/7.5.18)). Since a gradient forms from the source outward (Theorem 11.4.1), concentration and duration are correlated, and a time-integrating readout makes distant cells less sensitive to the transient.

## 11.8. Beyond the Simple Readout

When the French flag model was proposed, morphogens were hypothetical. They are no longer: Bicoid, Dorsal, Dpp, Wingless, Hedgehog, Nodal and retinoic acid have been identified, imaged and manipulated, and the general picture is that morphogen molecules are released from a local but dynamic source, interact with themselves and other molecules, and move by hindered diffusion, so that the shape of a gradient is set by the flux from the source, the effective diffusivity and the kinetics of clearance (Rogers and Schier, 2011). The models of this chapter are thus quantitatively relevant.

The simplest picture of interpretation, in which each fate corresponds to a range of the local concentration of one morphogen, has, however, not survived intact. When Ochoa-Espinosa and colleagues (2009) flattened the Bicoid gradient and set its level to a chosen value, target genes were expressed at concentrations well below those at which they are expressed in the wild-type gradient: cells do not simply look up the local concentration. The boundaries of Bicoid targets are positioned in part by repressor gradients (Runt, Krüppel and Capicua) that act on the same enhancers, and the gap genes refine their own boundaries by cross-repression. Taken together, the four gap genes of a single embryo specify position to about 1 % of egg length, better than any of them alone (Dubuis and colleagues, 2013): positional information is distributed over a network rather than carried by one molecule. Nor are positional values always set once: in growing tissues such as the wing disc and the limb bud, the gradient expands with the tissue, and growth itself feeds back on it.

## Summary

| Topic | Key results |
|---|---|
| Positional information | Definition 11.1.1: specify positional values, then interpret them; French flag model (Definition 11.1.2): source–sink linear gradient scales, $x_i=L(1-T_i/C_0)$ |
| Morphogen | Definition 11.2.1: graded, dose-dependent, direct action, ≥ 2 responses; tested by imaging, dose changes, receptor-mutant clones |
| One component | Formula 11.3.1; Lyapunov functional $\mathcal{L}$, $\dot{\mathcal{L}}=-\int(f+\Delta A)^2$ (Theorem 11.3.1); no stable nonuniform steady state with no flux (Theorem 11.3.2) |
| Energy integral | $\frac12A'^2+\varphi=K$; smooth $\varphi$: fixed wavelength (absolute regulation); kinked $\varphi$: boundary at a fixed fraction (Proposition 11.3.1); Fick–Jacobs equation (11.3) |
| SDD model | Definition 11.4.1: $C=(j\lambda/D)\mathrm{e}^{-x/\lambda}$, $\lambda=\sqrt{D/k}$; boundaries $\lambda\ln(C_0/T)$; accumulation time $(1+x/\lambda)/2k$ (Theorem 11.4.1) |
| Bicoid | $\lambda\approx0.2$ egg length; dose shifts boundaries; positional error $\sigma_x=\lambda\sigma_C/C$ (Formula 11.5.1), about one nucleus; Berg–Purcell limit requires averaging |
| Robustness | Self-enhanced degradation: $C=6D/k(x+\varepsilon)^2$, shift $0.21\varepsilon$ on doubling (Proposition 11.6.1); antagonists steepen, shuttles relocate |
| Scaling | Expansion–repression ties $\lambda$ to $L$; opposing gradients: $x^*=L/2-(\lambda/2)\ln r$ |
| Readout | Hill readout: logistic boundary of width $\approx4.4\lambda/n$; bistable switch with memory (Proposition 11.7.1); common-repressor switches store one-gene-on states; contour control peaks at $S^*=(K_1K_2)^{-1/2}$ |
| Status | Morphogens are real; interpretation is combinatorial and network-based (repressor gradients, gap gene cross-regulation) |

## Questions

1. Why does Wolpert's source–sink model scale while the synthesis–diffusion–degradation model does not? What would have to change in the SDD model for it to scale?

   **Answer** In the source–sink model the concentration is pinned at both ends and nothing is degraded, so the steady profile $C_0(1-x/L)$ is a function of $x/L$ only: thresholds fall at fixed fractions. In the SDD model the profile $\mathrm{e}^{-x/\lambda}$ contains an intrinsic length $\lambda=\sqrt{D/k}$ independent of $L$, so boundaries sit at fixed distances $\lambda\ln(C_0/T)$. To scale, $\lambda$ must become proportional to $L$, which requires that $D$ or $k$ depend on the size of the tissue, for instance through a feedback such as expansion–repression, in which a long-lived expander accumulates until the far end of the tissue reaches a threshold.

2. You make clones of cells lacking the receptor for a candidate morphogen in the middle of its gradient. Describe the results that would show (a) direct action at a distance and (b) action through a relay.

   **Answer** (a) Only the mutant cells lose the concentration-dependent target genes; wild-type cells on the far side of the clone, farther from the source, still express targets appropriate to their position. The response is cell-autonomous and the morphogen passes through or around the clone. (b) If the candidate induces a second signal in the cells nearest the source, which in turn induces the next cells, a clone of non-responding cells interrupts the chain: wild-type cells beyond the clone also lose their response (a "shadow" behind the clone). Clones lacking the Dpp receptor Thickveins give result (a).

3. Prove that for the SDD model on the half-line the total amount of morphogen at steady state is $j/k$, and explain why this is obvious.

   **Answer** $\int_0^\infty\frac{j\lambda}{D}\mathrm{e}^{-x/\lambda}\,\mathrm{d}x=\frac{j\lambda^2}{D}=\frac jk$. At steady state, input equals removal: the influx $j$ (per unit cross-section) is balanced by degradation $k\int C\,\mathrm{d}x$, independent of $D$. Diffusion only redistributes the amount.

4. Bicoid has $\lambda=100\,\mathrm{\mu m}$ and a *hunchback* boundary at $x=250\,\mathrm{\mu m}$ in an embryo with two copies of *bicoid*. Where does the threshold model put the boundary in embryos with one, four and six copies? Compare with the egg length of $500\,\mathrm{\mu m}$.

   **Answer** $x(m)=x_2+\lambda\ln(m/2)$: one copy $250-69=181\,\mathrm{\mu m}$ (36 % EL), four copies $250+69=319\,\mathrm{\mu m}$ (64 %), six copies $250+110=360\,\mathrm{\mu m}$ (72 %). The measured shifts of the *hunchback* boundary are of this order; the observed shifts of later landmarks are smaller, indicating buffering by downstream cross-regulation.

5. Using Theorem 11.4.1, by how much does the time to establish the gradient at $x=3\lambda$ change if the morphogen is made twice as stable (half the degradation rate), and what happens to $\lambda$? Is stabilization a good way to extend the range of a morphogen in a fast-developing embryo?

   **Answer** $\lambda$ grows by $\sqrt2$, so the point at the fixed distance $x=3\lambda_0$ now lies at $x/\lambda=3/\sqrt2=2.12$ new decay lengths. Then $\tau=\frac{1}{2k'}(1+2.12)$ with $k'=k/2$: $\tau=3.12/k$, compared with $\tau=2/k$ before, an increase by 56 %. A longer range from stability costs time, because both the lifetime and the distance grow; in an embryo with little time, a higher diffusivity (which lowers $\tau$ at a fixed position) is the better way to extend range.

6. Show that the logistic readout of a Hill function along an exponential gradient has a 90 %–10 % width of $2\ln9\,\lambda/n\approx4.4\lambda/n$. How large must $n$ be to produce a boundary two nuclei wide (about $16\,\mathrm{\mu m}$) from the Bicoid gradient?

   **Answer** $u=1/(1+\mathrm{e}^{n(x-x_T)/\lambda})=0.9$ at $n(x-x_T)/\lambda=-\ln9$ and $0.1$ at $+\ln9$, so the width is $2\ln9\,\lambda/n=4.39\lambda/n$. With $\lambda=100\,\mathrm{\mu m}$: $n=439/16\approx27$. Cooperative binding with $n\approx5$ gives about $90\,\mathrm{\mu m}$; the much sharper observed *hunchback* boundary in late cycle 14 requires additional mechanisms, such as positive autoregulation of *hunchback* (a bistable switch) and repression by posterior gap genes.

7. In Proposition 11.7.1 take $K=2$. Compute the three steady states at $s=0$ and estimate $s^*$ numerically. Why is it important that the low steady state at $s=0$ is exactly $g=0$?

   **Answer** $g=0$, $2-\sqrt3=0.268$ (unstable) and $2+\sqrt3=3.73$ (stable). The function $g/4-g^2/(1+g^2)$ on $[0,0.268]$ has its maximum where $\frac14=\frac{2g}{(1+g^2)^2}$, at $g\approx0.13$, giving $s^*\approx0.0325-0.0166=0.016$. Because the off state is exactly $0$, a cell that has never seen the activator produces none of the derepressor and leaves the target silent; any basal production would shift the off state and, if too large, push it across the unstable threshold, switching all cells on.

8. (Experimental design) How would you test whether a tissue scales its gradient by an expansion–repression mechanism, rather than by a mechanism in which the source strength grows with tissue size?

   **Answer** Expansion–repression predicts that (i) in mutants lacking the expander the gradient is short and does not scale; (ii) uniform overexpression of the expander lengthens the gradient regardless of size; (iii) the expander is repressed by morphogen signaling and so is expressed at the far end; (iv) in a larger tissue the gradient takes longer to reach its final shape. A source-strength mechanism predicts instead that the decay length is constant and only the amplitude changes with size, so a plot of $\ln C$ against $x$ has the same slope in small and large tissues. Measuring the slope of $\ln C$ in tissues of different size (for example by surgically reducing a *Xenopus* embryo or using wing discs of different size) distinguishes the two.

9. Two opposing exponential gradients with the same $\lambda$ have relative noise $\sigma_C/C=0.1$ each, independently. Compare the positional error of a boundary read from their ratio with that of a boundary read from one of them.

   **Answer** $\ln(C_1/C_2)=(L-2x)/\lambda$, so $\partial_x\ln(C_1/C_2)=-2/\lambda$. The variance of $\ln(C_1/C_2)$ is the sum of the two variances, $2\times0.1^2$, so $\sigma_x=\frac{\lambda}{2}\sqrt2\times0.1=0.071\lambda$, compared with $0.1\lambda$ for one gradient: an improvement by $\sqrt2$. If the two noises were perfectly correlated (a common fluctuation in, say, nuclear size) they would cancel in the ratio.

10. Why is the one-component Theorem 11.3.2 consistent with the existence of the Bicoid gradient, which is a stable nonuniform pattern of one substance?

    **Answer** The theorem assumes no-flux boundaries and production depending only on concentration. The Bicoid system violates the first assumption: there is a localized source at the anterior pole (a flux boundary condition $-DC_x(0)=j$, or equivalently a position-dependent production term). A gradient set up by a source is not self-organized; it is imposed by the asymmetry of the egg. The theorem says that a single substance cannot break symmetry by itself; it does not forbid gradients that reflect an asymmetry already present.
