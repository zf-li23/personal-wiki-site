---
title: Polymer Physics of DNA and Chromatin
description: "The statistical mechanics of DNA and chromatin as polymers. The freely jointed chain, the Gaussian distribution, the radius of gyration and the Kuhn length; entropic elasticity and the Langevin force–extension law; the worm-like chain, the persistence length, the Kratky–Porod crossover from rod to coil and the Marko–Siggia force–extension law; mechanical parameters of nucleic acids; excluded volume, the Flory argument and the Flory exponent; the size and overlap of genomes and chromosomes; looping, cyclization and the J factor with bending, entropy and helical phasing; contact probability and Hi-C, the equilibrium and fractal globules; the packing of DNA in phage capsids and the energetics and site exposure of the nucleosome."
---

A molecule of DNA is a few nanometers thick and up to centimeters long. At the scale of a gene it is a stiff rod; at the scale of a genome it is a random coil whose shape is set not by its chemistry but by counting: of all the conformations open to it, nearly all are crumpled. This chapter develops the statistical mechanics of such a chain. The simplest model, a random walk of rigid segments, already gives the size of a genome in solution, the entropic spring that resists stretching and the probability that two distant sites meet (21.1–21.2). Bending stiffness adds a length scale, the persistence length, and turns the walk into the worm-like chain, which describes DNA from a nucleosome to a chromosome and explains its force–extension curve (21.3). Excluded volume swells real chains and introduces the Flory exponent (21.4). The rest of the chapter applies these results to biology: the free energy and effective concentration of DNA loops that regulate genes (21.5), the scaling of contacts measured by Hi-C and what it says about chromosome folding (21.6), and the packing of DNA into phage capsids and nucleosomes, where bending energies of tens of $k_{\mathrm{B}}T$ must be paid (21.7). The random walk is the one of [7.6.5](/7.6.5); the persistence length and the worm-like chain were introduced for cytoskeletal filaments in [7.3.15](/7.3.15#sec-15.3.1), and the biology of chromatin is in [7.2.4](/7.2.4) and [7.3.17](/7.3.17). The measurement of force–extension curves with optical and magnetic tweezers, and the overstretching and unzipping of DNA, are the subject of [7.6.17](/7.6.17); the filaments of the cytoskeleton, which are the same model at larger stiffness, return in [7.6.26](/7.6.26).

## 21.1. Polymers as Random Walks

### 21.1.1. Structure as a Statistical Description

For a folded protein, "the structure" means a set of atomic coordinates, the content of a PDB file ([7.6.10](/7.6.10)). For a long DNA molecule in solution there is no such structure: thermal motion rearranges it continually, and two molecules never have the same shape. What is reproducible is the distribution of shapes, characterized by a few averages: the mean squared end-to-end distance $\langle R^2\rangle$, the **radius of gyration** $R_{\mathrm{g}}$ (the size measured by scattering, [7.6.9](/7.6.9#def-9.4.1)) and the probability that two points of the chain are close. Two lengths specify the chain: its contour length $L$ (for B-DNA $0.34\,\mathrm{nm}$ per base pair, so $L = 16.5\,\mu\mathrm{m}$ for the 48.5 kb genome of phage λ) and a length over which it stays straight. A statistical description is not a confession of ignorance: for a coil of thousands of segments, the averages are sharp and are what experiments measure.

### 21.1.2. The Freely Jointed Chain

**Definition 21.1.1 (Freely Jointed Chain)** A **freely jointed chain** is a chain of $N$ rigid segments of length $b$, joined so that the direction $\boldsymbol{u}_i$ ($\lvert\boldsymbol{u}_i\rvert = 1$) of each segment is independent of all others and uniformly distributed over the sphere. Its end-to-end vector is $\boldsymbol{R} = b\sum_{i=1}^{N}\boldsymbol{u}_i$ and its contour length $L = Nb$.

The end-to-end vector is the position of a **random walk** of $N$ steps of length $b$ ([7.6.5](/7.6.5#def-5.1.1)), so the results for random walks carry over.

**Proposition 21.1.1 (Size and Shape of the Freely Jointed Chain)** For a freely jointed chain,

$$
\langle\boldsymbol{R}\rangle = \boldsymbol{0}, \qquad \langle R^2\rangle = Nb^2 = Lb, \qquad R_{\mathrm{g}}^2 = \frac{Nb^2}{6} \quad (N \gg 1), \tag{21.1}
$$
and for large $N$ the end-to-end vector is distributed as

$$
P(\boldsymbol{R}) = \left(\frac{3}{2\pi Nb^2}\right)^{3/2}\exp\left(-\frac{3R^2}{2Nb^2}\right). \tag{21.2}
$$

**Proof** Since $\langle\boldsymbol{u}_i\cdot\boldsymbol{u}_j\rangle = \delta_{ij}$, $\langle R^2\rangle = b^2\sum_{i,j}\langle\boldsymbol{u}_i\cdot\boldsymbol{u}_j\rangle = Nb^2$. Each Cartesian component of $\boldsymbol{R}$ is a sum of $N$ independent terms of mean 0 and variance $b^2/3$, so by the **central limit theorem** ([3.1.13](/3.1.13)) it is normal with variance $Nb^2/3$; the three components are uncorrelated and asymptotically independent, which gives Eq. (21.2). For the radius of gyration, write $R_{\mathrm{g}}^2 = \frac{1}{N^2}\sum_{i<j}\langle r_{ij}^2\rangle$, where $r_{ij}$ is the distance between joints $i$ and $j$ (the identity $\frac1N\sum_i\lvert\boldsymbol{r}_i - \boldsymbol{r}_{\mathrm{cm}}\rvert^2 = \frac{1}{N^2}\sum_{i<j}r_{ij}^2$ holds for any set of points). The stretch between $i$ and $j$ is itself a freely jointed chain, $\langle r_{ij}^2\rangle = \lvert j - i\rvert b^2$, and $\sum_{i<j}(j - i) \approx N^3/6$, so $R_{\mathrm{g}}^2 \approx Nb^2/6$. $\square$

A chain whose statistics are those of Eq. (21.2) on all scales larger than a segment is called an ideal or Gaussian chain. Two features matter for biology. First, size grows as $\sqrt{N}$, not as $N$: a coil is mostly solvent, and doubling the length enlarges it only by $\sqrt2$. Second, the most probable end-to-end vector is $\boldsymbol{R} = \boldsymbol{0}$; the most probable *distance* $R = \lvert\boldsymbol{R}\rvert$ is not zero only because of the factor $4\pi R^2$ in the radial distribution, which counts the directions.

### 21.1.3. Real Chains and the Kuhn Length

Real polymers are not freely jointed. Successive bonds of a carbon chain meet at fixed angles; successive base pairs of DNA are stacked almost parallel. But correlations between directions decay along the chain, and a chain whose correlations have a finite range is, on scales much longer than that range, again a random walk with larger effective steps. For a chain of $N$ bonds of length $\ell$ in which each bond makes a fixed angle with the previous one, $\langle\boldsymbol{u}_i\cdot\boldsymbol{u}_{i+k}\rangle = \alpha^k$ with $\alpha = \cos\theta$, and the calculation of the persistent random walk ([7.6.5](/7.6.5#sec-5.1.2)) gives $\langle R^2\rangle \approx N\ell^2(1 + \alpha)/(1 - \alpha)$. Every such chain is characterized at large scales by one number.

**Definition 21.1.2 (Kuhn Length)** For a long chain of contour length $L$ with mean squared end-to-end distance $\langle R^2\rangle$, the **Kuhn length** is $b = \lim_{L\to\infty}\langle R^2\rangle/L$. A freely jointed chain of $N = L/b$ segments of length $b$ has the same contour length and the same $\langle R^2\rangle$; it is the equivalent freely jointed chain of the polymer.

For DNA at physiological salt, $b \approx 100\,\mathrm{nm} \approx 300\,\mathrm{bp}$ (21.3); for single-stranded DNA and RNA, about $1.5$–$3\,\mathrm{nm}$; for an unfolded polypeptide, about $0.8\,\mathrm{nm}$, roughly two residues. The coarse-graining that replaces a chemically detailed chain by Kuhn segments is the first example in this course of **coarse-graining** in its original sense ([7.6.1](/7.6.1)): the details below the Kuhn length change $b$ but not the form of the large-scale laws.

### 21.1.4. The Size of a Genome in Solution

**Example 21.1.1 (Genomes released from a phage and a bacterium)** Electron micrographs of an osmotically shocked phage T2 show its DNA spread around the empty head. The genome has about $1.5\times10^5\,\mathrm{bp}$, $L = 51\,\mu\mathrm{m}$, or $N = L/b \approx 500$ Kuhn segments. By Eq. (21.1) with $b = 2\ell_{\mathrm{p}}$ (21.3),

$$
R_{\mathrm{g}} = \sqrt{\frac{Lb}{6}} = \sqrt{\frac{L\ell_{\mathrm{p}}}{3}} = \sqrt{\frac{5.1\times10^4\,\mathrm{nm}\times50\,\mathrm{nm}}{3}} \approx 0.9\,\mu\mathrm{m},
$$
the scale of the tangle in the micrographs, compared with a head $0.1\,\mu\mathrm{m}$ across. The $4.6\times10^6\,\mathrm{bp}$ chromosome of *E. coli* ($L = 1.6\,\mathrm{mm}$) would occupy a coil with $R_{\mathrm{g}} \approx 5\,\mu\mathrm{m}$, larger than the cell. Both genomes are therefore compressed by their containers, by factors of about $10^3$ (phage) and $10^2$ (nucleoid) in volume, and much of this chapter is about the cost of that compression.

The Gaussian distribution also says how unlikely it is for the coil to be extended. For the *E. coli* genome ($N \approx 1.6\times10^4$), the probability density of a one-dimensional end-to-end distance $500b$ relative to zero is $\mathrm{e}^{-500^2/2N} \approx 4\times10^{-4}$, and for $1000b$ it is $\mathrm{e}^{-31} \approx 3\times10^{-14}$: almost all conformations are compact relative to the contour length, and pulling the ends apart means selecting from a vanishing fraction of them. This is the origin of entropic elasticity.

## 21.2. Entropic Elasticity

### 21.2.1. The Entropic Spring

Hold the ends of an ideal chain at a separation $\boldsymbol{R}$. The number of conformations compatible with this constraint is proportional to $P(\boldsymbol{R})$, so the conformational entropy is $S(\boldsymbol{R}) = k_{\mathrm{B}}\ln P(\boldsymbol{R}) + \mathrm{const}$. For a freely jointed chain the energy does not depend on the conformation, and the free energy is purely entropic.

**Proposition 21.2.1 (Entropic Spring)** An ideal chain with end-to-end vector $\boldsymbol{R}$ has free energy and restoring force

$$
F(\boldsymbol{R}) = -TS(\boldsymbol{R}) = \frac{3k_{\mathrm{B}}T}{2Nb^2}R^2 + \mathrm{const}, \qquad \boldsymbol{f} = -\frac{\partial F}{\partial\boldsymbol{R}} = -\frac{3k_{\mathrm{B}}T}{Nb^2}\boldsymbol{R}, \tag{21.3}
$$
a Hookean spring of stiffness $k = 3k_{\mathrm{B}}T/(Lb)$.

This is the prototype of an **entropic force** ([7.6.2](/7.6.2#def-2.3.1)). Its signature is that the stiffness is proportional to temperature: a heated rubber band, a network of such chains, contracts. The stiffness is also inversely proportional to the length, so long chains are extremely soft. For λ DNA, $k = 3\times4.1\,\mathrm{pN\,nm}/(1.65\times10^4\,\mathrm{nm}\times100\,\mathrm{nm}) \approx 7\times10^{-6}\,\mathrm{pN\,nm^{-1}} = 7\,\mathrm{fN}\,\mu\mathrm{m}^{-1}$: a force of $0.01\,\mathrm{pN}$ stretches it by over a micrometer. This is why DNA tethers in single-molecule experiments must be pulled with at least a few tenths of a piconewton before their extension is well defined.

### 21.2.2. The Freely Jointed Chain under Tension

Eq. (21.3) predicts that a constant force extends the chain without limit, which cannot be true: the extension cannot exceed $L$. The Gaussian distribution holds only near $R = 0$. The exact response of the freely jointed chain to a force $\boldsymbol{F} = F\boldsymbol{e}_z$ is obtained by adding the work term to the energy: each conformation has energy $-\boldsymbol{F}\cdot\boldsymbol{R} = -Fb\sum_i\cos\theta_i$, and the segments are independent.

**Theorem 21.2.1 (Force–Extension of the Freely Jointed Chain)** A freely jointed chain of $N$ segments of length $b$ under a force $F$ along $z$ has mean extension

$$
\langle z\rangle = Nb\,\mathcal{L}\!\left(\frac{Fb}{k_{\mathrm{B}}T}\right), \qquad \mathcal{L}(u) = \coth u - \frac{1}{u}, \tag{21.4}
$$
where $\mathcal{L}$ is the Langevin function. In one dimension (segments pointing along $\pm z$ only), $\langle z\rangle = Nb\tanh(Fb/k_{\mathrm{B}}T)$.

**Proof** The partition function factorizes, $Z = Z_1^N$, with

$$
Z_1 = \int_0^{2\pi}\!\mathrm{d}\varphi\int_0^{\pi}\mathrm{e}^{\beta Fb\cos\theta}\sin\theta\,\mathrm{d}\theta = 2\pi\int_{-1}^{1}\mathrm{e}^{\beta Fbx}\,\mathrm{d}x = \frac{4\pi\sinh(\beta Fb)}{\beta Fb},
$$
$\beta = 1/k_{\mathrm{B}}T$. The mean extension is $\langle z\rangle = k_{\mathrm{B}}T\,\partial\ln Z/\partial F = Nk_{\mathrm{B}}T\,\partial\ln Z_1/\partial F = Nb\left[\coth(\beta Fb) - 1/(\beta Fb)\right]$. In one dimension $Z_1 = 2\cosh(\beta Fb)$ and the same differentiation gives $\tanh$. $\square$

At small force $\mathcal{L}(u) \approx u/3$, and $\langle z\rangle = Nb^2F/(3k_{\mathrm{B}}T)$ is the linear spring of Eq. (21.3); at large force $\mathcal{L}(u) \approx 1 - 1/u$, and the chain approaches its contour length as $1 - \langle z\rangle/L \approx k_{\mathrm{B}}T/(Fb)$. The crossover occurs at $F \approx k_{\mathrm{B}}T/b$: about $0.04\,\mathrm{pN}$ for double-stranded DNA ($b = 100\,\mathrm{nm}$), but about $3\,\mathrm{pN}$ for single-stranded DNA ($b \approx 1.5\,\mathrm{nm}$). The stiff duplex is thus easier to extend at low force than the flexible single strand of the same number of bases, and the two curves cross at a few piconewtons, a fact used to follow the unwinding of DNA by helicases in single-molecule experiments ([7.6.17](/7.6.17)). Measured curves for double-stranded DNA follow Eq. (21.4) at low force but approach full extension more slowly, as $F^{-1/2}$ rather than $F^{-1}$; explaining this requires replacing the free joints by continuous bending.

## 21.3. The Worm-Like Chain

### 21.3.1. Bending Energy and the Persistence Length

A double helix is better described as a thin elastic rod that bends smoothly. Let $\boldsymbol{r}(s)$ be its axis, parametrized by the arc length $s \in [0, L]$, and $\boldsymbol{t}(s) = \mathrm{d}\boldsymbol{r}/\mathrm{d}s$ the unit tangent. The curvature is $\lvert\mathrm{d}\boldsymbol{t}/\mathrm{d}s\rvert = 1/R_{\mathrm{c}}$, where $R_{\mathrm{c}}$ is the local **radius of curvature**. For small deformations of a rod with Young's modulus $E$ and second moment of area $I$ of its cross-section, elasticity theory gives the bending energy

$$
E_{\mathrm{bend}} = \frac{\kappa}{2}\int_0^L\left\lvert\frac{\mathrm{d}\boldsymbol{t}}{\mathrm{d}s}\right\rvert^2\mathrm{d}s, \qquad \kappa = EI, \tag{21.5}
$$
with flexural rigidity $\kappa$ (units of energy times length). The **worm-like chain** is the chain with this energy and no other interaction, at temperature $T$ ([7.3.15](/7.3.15#sec-15.3.1)). Bending a length $\ell$ of it into a circular arc of radius $R_{\mathrm{c}}$ costs $\kappa\ell/(2R_{\mathrm{c}}^2)$; in particular, closing a length $L$ into a circle ($R_{\mathrm{c}} = L/2\pi$) costs

$$
E_{\mathrm{circle}} = \frac{2\pi^2\kappa}{L}. \tag{21.6}
$$
The competition between this energy and thermal energy defines the length below which the chain is straight.

**Proposition 21.3.1 (Tangent Correlations of the Worm-Like Chain)** In three dimensions, the tangents of a worm-like chain at equilibrium satisfy

$$
\langle\boldsymbol{t}(s)\cdot\boldsymbol{t}(s')\rangle = \mathrm{e}^{-\lvert s - s'\rvert/\ell_{\mathrm{p}}}, \qquad \ell_{\mathrm{p}} = \frac{\kappa}{k_{\mathrm{B}}T}. \tag{21.7}
$$

**Proof** Write $g(s) = \langle\boldsymbol{t}(0)\cdot\boldsymbol{t}(s)\rangle$. Because the energy (21.5) is a sum of independent contributions of successive pieces of the chain, the bending of the piece $[s_1, s_1 + s_2]$ is statistically independent of the direction at $s_1$. Choose axes with $\boldsymbol{t}(s_1)$ along $z$; then $\boldsymbol{t}(0)\cdot\boldsymbol{t}(s_1 + s_2)$ averages over the azimuth of the second piece to $(\boldsymbol{t}(0)\cdot\boldsymbol{t}(s_1))(\boldsymbol{t}(s_1)\cdot\boldsymbol{t}(s_1 + s_2))$, so $g(s_1 + s_2) = g(s_1)g(s_2)$ and $g$ is an exponential, $g(s) = \mathrm{e}^{-s/\ell_{\mathrm{p}}}$. To find $\ell_{\mathrm{p}}$, consider a short piece of length $\Delta s$ bent through a small angle $\theta$, with energy $\kappa\theta^2/(2\Delta s)$. The angle has two independent components (the bending can occur in two planes), each with a quadratic energy, so by the **equipartition theorem** $\langle\theta^2\rangle = 2k_{\mathrm{B}}T\Delta s/\kappa$, and $g(\Delta s) = \langle\cos\theta\rangle \approx 1 - \langle\theta^2\rangle/2 = 1 - \Delta s\,k_{\mathrm{B}}T/\kappa$. Comparing with $\mathrm{e}^{-\Delta s/\ell_{\mathrm{p}}} \approx 1 - \Delta s/\ell_{\mathrm{p}}$ gives $\ell_{\mathrm{p}} = \kappa/k_{\mathrm{B}}T$. $\square$

The **persistence length** $\ell_{\mathrm{p}}$ is thus the length whose bending into a gentle arc costs about one $k_{\mathrm{B}}T$. For DNA, $\ell_{\mathrm{p}} \approx 50\,\mathrm{nm} \approx 150\,\mathrm{bp}$ and $\kappa = \ell_{\mathrm{p}}k_{\mathrm{B}}T \approx 200\,\mathrm{pN\,nm^2}$; with a radius of $1\,\mathrm{nm}$ ($I = \pi r^4/4$) this corresponds to $E \approx 0.3\,\mathrm{GPa}$, a modulus like that of a stiff plastic. Actin filaments ($\ell_{\mathrm{p}} \approx 17\,\mu\mathrm{m}$) and microtubules (millimeters) are the same model at much larger $\kappa$, because $I$ grows as the fourth power of the radius ([7.3.15](/7.3.15#sec-15.3.1)). The figure checks Proposition 21.3.1 by simulating a discrete chain.

![Monte Carlo conformations of a discrete worm-like chain in three dimensions (segments of 0.1 ℓp, bending angles drawn from the Boltzmann distribution of the bending energy). A: one conformation each of contour length 2, 20 and 200 ℓp, each drawn at its own scale with a bar of length ℓp (for DNA, 300 bp, 3 kb and 30 kb): a gently bent rod, a meandering filament and a random coil. B: distribution of the end-to-end distance R, scaled by the root-mean-square value, for chains of 1, 5 and 50 ℓp (4000 chains each) against the Gaussian distribution with the same mean square: short chains are nearly straight and their distances are concentrated near the contour length; for L ≫ ℓp the Gaussian chain is recovered](./plots/wlc-conformations.py)

### 21.3.2. From Rod to Coil

**Formula 21.3.1 (Kratky–Porod)** The worm-like chain of contour length $L$ and persistence length $\ell_{\mathrm{p}}$ has

$$
\langle R^2\rangle = 2\ell_{\mathrm{p}}L - 2\ell_{\mathrm{p}}^2\left(1 - \mathrm{e}^{-L/\ell_{\mathrm{p}}}\right), \tag{21.8}
$$
which is $L^2$ (a rod) for $L \ll \ell_{\mathrm{p}}$ and $2\ell_{\mathrm{p}}L$ (a coil) for $L \gg \ell_{\mathrm{p}}$, and

$$
R_{\mathrm{g}}^2 = \frac{\ell_{\mathrm{p}}L}{3} - \ell_{\mathrm{p}}^2 + \frac{2\ell_{\mathrm{p}}^3}{L} - \frac{2\ell_{\mathrm{p}}^4}{L^2}\left(1 - \mathrm{e}^{-L/\ell_{\mathrm{p}}}\right). \tag{21.9}
$$

**Proof** Since $\boldsymbol{R} = \int_0^L\boldsymbol{t}(s)\,\mathrm{d}s$, Proposition 21.3.1 gives

$$
\langle R^2\rangle = \int_0^L\!\!\int_0^L\mathrm{e}^{-\lvert s - s'\rvert/\ell_{\mathrm{p}}}\,\mathrm{d}s\,\mathrm{d}s' = 2\int_0^L\mathrm{d}s\int_0^{L-s}\mathrm{e}^{-u/\ell_{\mathrm{p}}}\,\mathrm{d}u = 2\ell_{\mathrm{p}}\int_0^L\left(1 - \mathrm{e}^{-(L-s)/\ell_{\mathrm{p}}}\right)\mathrm{d}s,
$$
which is Eq. (21.8). Eq. (21.9) follows from $R_{\mathrm{g}}^2 = \frac{1}{L^2}\int_0^L\!\int_0^{s'}\langle\lvert\boldsymbol{r}(s') - \boldsymbol{r}(s)\rvert^2\rangle\,\mathrm{d}s\,\mathrm{d}s'$, inserting Eq. (21.8) for the stretch of length $s' - s$ and integrating. $\square$

Eq. (21.8) is the worm-like-chain formula quoted for filaments in [7.3.15](/7.3.15#sec-15.3.1), now derived. Comparing its long-chain limit with Definition 21.1.2 gives the relation used throughout this chapter:

$$
b = 2\ell_{\mathrm{p}}. \tag{21.10}
$$
The Kuhn length of DNA is about $100\,\mathrm{nm}$. The crossover is gradual: at $L = \ell_{\mathrm{p}}$, $\langle R^2\rangle = 0.74L^2$ and the chain is still rodlike; the coil limit is approached only beyond about $10\ell_{\mathrm{p}}$ (1.5 kb of DNA). DNA segments of the size of a nucleosome or of a regulatory loop of a few hundred base pairs are therefore neither rods nor coils, and their mechanics must be computed with the full worm-like chain.

![Tangent correlations and the rod-to-coil crossover. A: tangent correlation along simulated worm-like chains of 4 ℓp (20,000 chains, dots) against exp(−s/ℓp) (Proposition 21.3.1); on the semilogarithmic axis the decay is a straight line of slope −1/ℓp. B: mean squared end-to-end distance relative to the rod value L² and to the coil value 2ℓpL against L/ℓp, from simulation (dots) and from Eq. (21.8) (lines); the top axis converts to base pairs of DNA (ℓp = 50 nm = 147 bp), with the length of DNA in a nucleosome, the lac O1–O2 loop and the λ genome marked](./plots/wlc-crossover.py)

The persistence length can be measured in several independent ways, which agree for DNA at moderate salt: from the shapes of molecules adsorbed on a surface and imaged by electron or atomic force microscopy (in two dimensions $\ell_{\mathrm{p}}$ in Eq. (21.7) is replaced by $2\ell_{\mathrm{p}}$), from light scattering and hydrodynamics of fragments of different lengths (through Eq. (21.9) and the **hydrodynamic radius**, [7.6.8](/7.6.8)), from cyclization rates (21.5) and from force–extension curves (21.3.3).

### 21.3.3. The Worm-Like Chain under Tension

A force $F$ along $z$ adds $-F\int_0^L t_z\,\mathrm{d}s$ to the energy (21.5). The exact solution maps the problem onto a quantum rotor (the tangent performs a random walk on the unit sphere, and the force acts like a field), and the extension is the ground-state expectation of $\cos\theta$; it has to be computed numerically. Its two limits, however, follow from simple arguments.

At small force, linear response gives $\langle z\rangle = F\langle R_z^2\rangle/k_{\mathrm{B}}T$ with $\langle R_z^2\rangle = \langle R^2\rangle/3 = 2\ell_{\mathrm{p}}L/3$ for a long chain, so

$$
\langle z\rangle = \frac{2\ell_{\mathrm{p}}L}{3k_{\mathrm{B}}T}F, \tag{21.11}
$$
the entropic spring (21.3) with $b = 2\ell_{\mathrm{p}}$. At large force the chain is nearly straight, $\boldsymbol{t} \approx (t_x, t_y, 1 - t_\perp^2/2)$, and the energy is, to quadratic order in the small transverse components,

$$
E = \int_0^L\left[\frac{\kappa}{2}\left(\frac{\mathrm{d}\boldsymbol{t}_\perp}{\mathrm{d}s}\right)^2 + \frac{F}{2}t_\perp^2\right]\mathrm{d}s - FL.
$$
Expanding $\boldsymbol{t}_\perp$ in **Fourier series** modes of wavenumber $q$, each of the two components of each mode has energy $\frac{L}{2}(\kappa q^2 + F)\lvert t_q\rvert^2$, and equipartition gives $\langle\lvert t_q\rvert^2\rangle = k_{\mathrm{B}}T/[L(\kappa q^2 + F)]$. Summing over modes (an integral $L\int\mathrm{d}q/2\pi$),

$$
\langle t_\perp^2\rangle = 2\int_{-\infty}^{\infty}\frac{\mathrm{d}q}{2\pi}\frac{k_{\mathrm{B}}T}{\kappa q^2 + F} = \frac{k_{\mathrm{B}}T}{\sqrt{\kappa F}},
\qquad
\frac{\langle z\rangle}{L} = 1 - \frac{\langle t_\perp^2\rangle}{2} = 1 - \frac12\sqrt{\frac{k_{\mathrm{B}}T}{F\ell_{\mathrm{p}}}}. \tag{21.12}
$$
The slow $F^{-1/2}$ approach to full extension is the signature of continuous bending: a force $F$ suppresses only the thermal undulations longer than $\sqrt{\kappa/F}$, and shorter ones survive. Marko and Siggia (1995) combined the two limits into a single formula.

**Formula 21.3.2 (Marko–Siggia Interpolation)** The relative extension $z = \langle z\rangle/L$ of a worm-like chain under a force $F$ is approximately given by

$$
\frac{F\ell_{\mathrm{p}}}{k_{\mathrm{B}}T} = z + \frac{1}{4(1 - z)^2} - \frac14, \tag{21.13}
$$
which reduces to Eq. (21.11) for $z \ll 1$ and to Eq. (21.12) for $1 - z \ll 1$, and deviates from the exact solution by at most about 10 % near $z \approx 0.5$.

![Force–extension of ideal chains. A: relative extension against the dimensionless force Fℓp/kBT for the one- and three-dimensional freely jointed chains (Theorem 21.2.1, Kuhn length b = 2ℓp), the exact worm-like chain (ground state of the rotor problem) and the Marko–Siggia interpolation (Formula 21.3.2); all share the linear response z = 2Fℓp/3kBT at small force, but at large force the freely jointed chain approaches full extension as 1/F and the worm-like chain as F^(−1/2). B: λ DNA (16.5 µm, ℓp = 50 nm) in physical units, force on a logarithmic axis: below 0.1 pN the molecule is a soft entropic spring, between 1 and 10 pN it approaches its contour length, above about 10 pN it is stretched elastically (extensible worm-like chain, stretch modulus S = 1000 pN), and near 65 pN it overstretches (7.6.17); the freely jointed chain fits the low-force data but not the approach to full extension](./plots/force-extension.py)

The first measurements of DNA elasticity (Smith, Finzi and Bustamante, 1992, with magnetic beads; later with **optical tweezers**) were fitted by Eq. (21.13) with $\ell_{\mathrm{p}} \approx 50\,\mathrm{nm}$, which made the persistence length one of the best-measured numbers in molecular biophysics. Above about $10\,\mathrm{pN}$ the duplex itself stretches, and the extensible worm-like chain adds $F/S$ to Eq. (21.12) with a stretch modulus $S \approx 1000\,\mathrm{pN}$. How the curve is measured, and what happens beyond (the overstretching plateau and the unzipping of the strands), is treated with the instruments in [7.6.17](/7.6.17). The same formulas give the work of stretching: the free energy stored in a chain extended to $z$ is $\Delta G = \int_0^{F}\langle z\rangle\,\mathrm{d}F'$ at constant force, and a protein whose binding shortens or lengthens a DNA or protein tether changes its affinity by the factor $\mathrm{e}^{\pm\beta\Delta G}$, which is how force regulates binding (a theme of [7.6.17](/7.6.17) and [7.6.31](/7.6.31)).

### 21.3.4. Mechanical Parameters of Nucleic Acids

| Quantity | Double-stranded DNA | Single-stranded DNA | Remark |
|---|---|---|---|
| Rise per unit | $0.34\,\mathrm{nm}$ per bp | about $0.6$–$0.7\,\mathrm{nm}$ per nucleotide | ss contour longer for the same number of bases |
| Persistence length $\ell_{\mathrm{p}}$ | $45$–$50\,\mathrm{nm}$ (above $\sim 10\,\mathrm{mM}$ monovalent salt) | about $1\,\mathrm{nm}$ (salt dependent) | dsRNA about $60\,\mathrm{nm}$ |
| Kuhn length $b = 2\ell_{\mathrm{p}}$ | about $100\,\mathrm{nm} = 300\,\mathrm{bp}$ | about $2\,\mathrm{nm}$ | |
| Bending rigidity $\kappa = \ell_{\mathrm{p}}k_{\mathrm{B}}T$ | about $200\,\mathrm{pN\,nm^2}$ | | |
| Stretch modulus $S$ | about $1000\,\mathrm{pN}$ | | elastic regime $10$–$50\,\mathrm{pN}$ |
| Torsional rigidity $C$ | $410$–$450\,\mathrm{pN\,nm^2}$ (twist persistence $C/k_{\mathrm{B}}T \approx 100\,\mathrm{nm}$) | none (free rotation) | relevant for **supercoiled** DNA ([7.2.3](/7.2.3)) |
| Characteristic forces | overstretching about $65\,\mathrm{pN}$; unzipping $10$–$15\,\mathrm{pN}$ | | measured in [7.6.17](/7.6.17) |

The persistence length of a charged polymer contains an electrostatic part. The phosphates repel each other along the backbone, and bending brings them closer; the repulsion is screened over the Debye length $\kappa_{\mathrm{D}}^{-1}$, and the theory of Odijk and of Skolnick and Fixman gives an additional persistence length $\ell_{\mathrm{el}} = 1/(4\kappa_{\mathrm{D}}^2\ell_{\mathrm{B}})$ for a chain at the Manning charge density (**counterion condensation**, [7.6.6](/7.6.6)), with the **Bjerrum length** $\ell_{\mathrm{B}} = 0.7\,\mathrm{nm}$. At $10\,\mathrm{mM}$ salt ($\kappa_{\mathrm{D}}^{-1} \approx 3\,\mathrm{nm}$) this is only about $3\,\mathrm{nm}$, which is why the measured $\ell_{\mathrm{p}}$ of DNA is nearly constant at physiological salt and rises only at very low salt. For single-stranded nucleic acids and unfolded proteins, whose intrinsic stiffness is small, electrostatic stiffening and excluded volume matter much more.

## 21.4. Excluded Volume and the Flory Exponent

### 21.4.1. Self-Avoiding Chains

Ideal chains can cross themselves: two segments far apart along the contour may occupy the same point in space. Real chains cannot, and in a good solvent, where segments prefer contact with solvent to contact with each other, they repel at short range. A random walk forbidden to revisit sites, the self-avoiding walk, is more extended than the ideal walk, and the swelling grows with length because longer walks have more opportunities to intersect themselves. The size is then described by a different power of $N$.

**Definition 21.4.1 (Flory Exponent)** If the size of a polymer of $N$ segments scales as $R \propto N^{\nu}$ for large $N$, the exponent $\nu$ is its **Flory exponent**: $\nu = 1/2$ for an ideal chain, $\nu = 3/5$ in Flory's approximation (exactly $\nu = 0.588$ in three dimensions) for a self-avoiding chain in a good solvent, and $\nu = 1/3$ for a compact globule in a poor solvent.

**Proposition 21.4.1 (Flory Argument)** A chain of $N$ segments of length $b$ with excluded volume $v$ per pair of segments, confined to a coil of radius $R$, has free energy

$$
\frac{F(R)}{k_{\mathrm{B}}T} \approx \frac{3R^2}{2Nb^2} + \frac{vN^2}{2R^3}, \tag{21.14}
$$
which is minimal at $R^5 = vb^2N^3/2$, so that $R \propto N^{3/5}$.

**Proof** The first term is the entropic spring of Proposition 21.2.1, which resists swelling. The second is a mean-field estimate of the repulsion: the $N$ segments fill a volume of order $R^3$ at concentration $N/R^3$; each of the $N^2/2$ pairs overlaps with probability $v/R^3$, at a cost of order $k_{\mathrm{B}}T$. Setting $\partial F/\partial R = 3R/(Nb^2) - \frac32 vN^2/R^4 = 0$ gives $R^5 = vb^2N^3/2$. $\square$

The argument overestimates both terms (the elastic term by ignoring the correlations created by the repulsion, the repulsive term by ignoring that the segment density is not uniform) by similar amounts, so that the exponent comes out close to the exact value. The sign of $v$ depends on the solvent. In a poor solvent, where segments attract, $v < 0$, the chain collapses into a globule with $R \propto N^{1/3}$, the scaling of a dense object. At the $\theta$ temperature the attraction and the hard-core repulsion cancel ($v = 0$), and the chain is ideal; a polymer in its own melt, or a chromosome among other chromosomes, is also nearly ideal, because the repulsion between its segments is screened by the other chains (Flory's theorem).

![Excluded volume and the Flory exponent. A: mean squared end-to-end distance of random walks and of self-avoiding walks on the simple cubic lattice (sampled with the pivot algorithm) against the number of steps; the random walk follows N¹, the self-avoiding walk N^1.176 (ν = 0.588), and the ratio grows with length. B: the Flory free energy of Eq. (21.14) for N = 100, 300 and 1000 (b = 1, v = 1): the minimum (dots) moves outward as N^(3/5)](./plots/flory.py)

### 21.4.2. Proteins and Disordered Chains

The exponents can be measured. Chemically denatured proteins follow $R_{\mathrm{g}} \approx 0.2\,\mathrm{nm}\times N^{0.59}$ for $N$ residues (Kohn and colleagues, 2004, from SAXS, [7.6.9](/7.6.9)), the scaling of a self-avoiding chain in a good solvent, whereas folded proteins follow $R_{\mathrm{g}} \approx 0.22\,\mathrm{nm}\times N^{0.38}$, close to the compact exponent $1/3$. **Intrinsically disordered proteins** lie in between, with $\nu$ from about $0.45$ to $0.6$ set by their charge and hydrophobicity; their exponents, measured by SAXS and single-molecule FRET, are a compact summary of how the sequence controls the ensemble ([7.6.16](/7.6.16)). For DNA, excluded volume is weak, because the duplex is thin ($2\,\mathrm{nm}$) compared with its Kuhn length ($100\,\mathrm{nm}$): the swelling becomes noticeable only for chains of more than about $10^3$–$10^4$ Kuhn lengths, so genomes of viruses and the shorter fragments used in experiments are close to ideal.

## 21.5. Looping and the J Factor

### 21.5.1. The Probability That Two Ends Meet

Many processes require two sites on the same DNA molecule to come into contact: a repressor bound at two operators ([7.2.11](/7.2.11)), an enhancer meeting a promoter ([7.2.14](/7.2.14)), the two ends of a fragment ligated into a circle, recombination sites brought together by a recombinase. The relevant quantity is the probability that the ends of a chain of contour length $L$ are within a small distance $\delta$ of each other. For an ideal chain and $\delta \ll \sqrt{Lb}$, the Gaussian (21.2) is nearly constant over the small sphere, and

$$
p(\delta) \approx \frac{4\pi\delta^3}{3}P(\boldsymbol{0}) = \frac{4\pi\delta^3}{3}\left(\frac{3}{2\pi Lb}\right)^{3/2} \propto L^{-3/2}. \tag{21.15}
$$
The decay with length depends on dimension: in one dimension the fraction of walks of $N$ steps returning to the origin is $\binom{N}{N/2}2^{-N} \approx \sqrt{2/\pi N}$, which falls only as $N^{-1/2}$, as **Stirling's approximation** shows. In three dimensions long loops are rare because the ends have room to wander apart. The probability density $P(\boldsymbol{0})$ has units of inverse volume, and it is natural to express it as a concentration.

**Definition 21.5.1 (J Factor)** The **J factor** of a DNA segment is the effective molar concentration of one of its ends in the vicinity of the other, $J = P(\boldsymbol{R} = \boldsymbol{0})/N_{\mathrm{A}}$, where $P$ is the probability density of the end-to-end vector (with additional factors for the required relative orientation of the ends when it matters). It is the ratio of the equilibrium constant of an intramolecular association (cyclization, looping) to that of the same association between separate molecules.

The second sentence explains why $J$ is the measured quantity. In a cyclization experiment (Shore and Baldwin, 1983), fragments with complementary single-stranded ends are joined by **DNA ligase** either into circles (a reaction whose rate is proportional to $J$) or into dimers (proportional to the concentration of other fragments); the ratio of circles to dimers gives $J$ directly. In gene regulation, a repressor bound at one operator sees the second operator at concentration $J$: if its dissociation constant from that site is $K_{\mathrm{d}}$, the statistical weight of the looped state relative to the singly bound one is $J/K_{\mathrm{d}}$. A loop is favorable when $J$ exceeds $K_{\mathrm{d}}$, which for nanomolar repressors requires $J$ of tens to hundreds of nanomolar.

For a Gaussian chain, Eq. (21.15) gives

$$
J_{\mathrm{G}}(L) = \frac{1}{N_{\mathrm{A}}}\left(\frac{3}{2\pi Lb}\right)^{3/2} \approx 0.53\,\mu\mathrm{M}\times n^{-3/2}, \qquad n = L/b, \tag{21.16}
$$
about $0.5\,\mu\mathrm{M}$ for a loop one Kuhn length (300 bp) long if DNA were flexible on that scale. It is not, and short loops must be bent.

### 21.5.2. Bending versus Entropy

**Proposition 21.5.1 (Optimal Loop Length in the Circle Model)** Approximate the free energy of a loop of length $L$ by the bending energy of a circle, Eq. (21.6), plus the entropic cost of bringing the ends together, $-k_{\mathrm{B}}T\ln P(\boldsymbol{0})$ from Eq. (21.15):

$$
\frac{\Delta G_{\mathrm{loop}}(L)}{k_{\mathrm{B}}T} = \frac{2\pi^2\ell_{\mathrm{p}}}{L} + \frac32\ln L + \mathrm{const}. \tag{21.17}
$$
$\Delta G_{\mathrm{loop}}$ is minimal, and $J \propto \mathrm{e}^{-\Delta G_{\mathrm{loop}}/k_{\mathrm{B}}T}$ maximal, at $L^* = 4\pi^2\ell_{\mathrm{p}}/3 \approx 13\ell_{\mathrm{p}}$.

**Proof** $\mathrm{d}\Delta G_{\mathrm{loop}}/\mathrm{d}L = k_{\mathrm{B}}T(-2\pi^2\ell_{\mathrm{p}}/L^2 + 3/2L) = 0$ at $L = 4\pi^2\ell_{\mathrm{p}}/3$; the second derivative is positive there. $\square$

For DNA, $2\pi^2\ell_{\mathrm{p}}/L \approx 3000/N_{\mathrm{bp}}$: closing 150 bp into a circle costs about $20\,k_{\mathrm{B}}T$, 1.5 kb only $2\,k_{\mathrm{B}}T$. The model predicts an optimum near $1900\,\mathrm{bp}$. Cyclization measurements place it near $500\,\mathrm{bp}$, with a maximal $J$ of about $10^{-7}\,\mathrm{M}$. The discrepancy has a simple origin: a loop of a few persistence lengths need not be a circle. Its ends can meet through teardrop and other shapes that bend less where it matters, and the full worm-like chain, which sums over all closed shapes, has a much larger closure probability at intermediate lengths. Numerical results for the worm-like chain are well represented by the interpolation (Rippe, 2001)

$$
J(L) \approx 0.53\,\mu\mathrm{M}\times n^{-3/2}\exp\left(-\frac{2.66}{n^2}\right), \qquad n = L/b, \tag{21.18}
$$
which tends to Eq. (21.16) for long loops and peaks at $n \approx 1.9$, about $550\,\mathrm{bp}$, at $J \approx 100\,\mathrm{nM}$.

![The J factor of DNA looping. A: J against loop length for DNA (ℓp = 50 nm): the Gaussian chain (Eq. (21.16)), falling as L^(−3/2); the circle model, the Gaussian value times the Boltzmann factor of bending a circle, with its maximum near 1900 bp (Proposition 21.5.1); and the worm-like chain (interpolation (21.18)), which peaks near 550 bp at about 100 nM and agrees with the Gaussian chain beyond a few kilobases; the lengths of the lac O1–O3 and O1–O2 loops are marked. B: helical phasing for loops that must bring two sites to the same face of the helix, with a twist persistence length of 100 nm: J oscillates with the 10.5 bp helical repeat, between the value without a phasing requirement and a minimum that rises as long loops absorb a fractional turn of twist more easily](./plots/j-factor.py)

### 21.5.3. Twist, Phasing and Looping in the Cell

Proteins bind to one face of the double helix. To loop DNA between two sites on the same face, the segment must be twisted by the fractional excess $\delta = N_{\mathrm{bp}}/10.5 - \operatorname{round}(N_{\mathrm{bp}}/10.5)$ of a helical turn, at a cost $2\pi^2C\delta^2k_{\mathrm{B}}T/L$ for a twist persistence length $C \approx 100\,\mathrm{nm}$, analogous to Eq. (21.6). Short loops are therefore sensitive to the helical phase of their sites, and the sensitivity fades as $1/L$. Together with the bending and entropic terms, this is the three-term loop free energy used for the lac operon in [7.2.11](/7.2.11#sec-11.6.4); the oscillation of repression with a 10–11 bp period, strongest near 70–80 bp, is the experimental signature.

Two observations show where the bare worm-like chain fails. First, lac repression with loops of 60–90 bp, where Eq. (21.18) predicts $J$ well below $1\,\mathrm{nM}$, is strong in vivo: architectural proteins such as HU and IHF bend DNA sharply, negative supercoiling brings distant sites together, and the repressor tetramer is itself flexible, so that in vivo loops are much easier to form than in naked DNA (Boedicker, Garcia and Phillips, 2013, measured the in vivo loop free energies systematically). Second, the cyclization of naked fragments shorter than about 100 bp was reported to be far more frequent than the worm-like chain allows (Cloutier and Widom, 2004), while repeated measurements found agreement down to about 105 bp (Du and colleagues, 2005), and single-molecule FRET looping again found enhanced looping below 100 bp (Vafabakhsh and Ha, 2012). Whether highly bent DNA relieves stress by transient kinks or bubbles, which would make its bending energy grow more slowly than Eq. (21.5) at large curvature, is still debated; the answer matters for nucleosomes, where DNA is bent to a radius of $4\,\mathrm{nm}$.

## 21.6. Chromosomes as Polymers

### 21.6.1. Overlap and Territories

A genome in a nucleus is far denser than a free coil. Chromatin has a different linear packing density and stiffness from naked DNA: for a nucleosomal fiber, about $\nu_{\ell} \approx 8\,\mathrm{bp\,nm^{-1}}$ (if it is a chain of nucleosomes) or $\nu_{\ell} \approx 100\,\mathrm{bp\,nm^{-1}}$ (if it is folded into a 30 nm fiber in vitro), with Kuhn lengths of order $60$–$400\,\mathrm{nm}$. A stretch of $N_{\mathrm{bp}}$ base pairs then has $\langle R^2\rangle = N_{\mathrm{bp}}b/\nu_{\ell}$, and $b/\nu_{\ell}$ is the single material parameter of chromatin at large scales.

**Example 21.6.1 (Do yeast chromosomes overlap?)** The budding yeast nucleus, $2\,\mu\mathrm{m}$ across, holds 16 chromosomes of 12 Mb in total, a density of $3\,\mathrm{Mb}\,\mu\mathrm{m}^{-3}$. An average chromosome of 750 kb as a free nucleosomal fiber ($\nu_{\ell} = 8\,\mathrm{bp\,nm^{-1}}$, $L = 94\,\mu\mathrm{m}$, $\ell_{\mathrm{p}} \approx 30\,\mathrm{nm}$) has $R_{\mathrm{g}} = \sqrt{L\ell_{\mathrm{p}}/3} \approx 1\,\mu\mathrm{m}$ and a density within its own coil of $750\,\mathrm{kb}/(\frac43\pi R_{\mathrm{g}}^3) \approx 0.2\,\mathrm{Mb}\,\mu\mathrm{m}^{-3}$, more than ten times below the nuclear density. Free coils would have to interpenetrate strongly, like spaghetti in a bowl. For human chromosomes the same estimate gives $R_{\mathrm{g}} \approx 7\,\mu\mathrm{m}$ for an average chromosome in a nucleus $10\,\mu\mathrm{m}$ across.

That interphase chromosomes nevertheless occupy distinct **chromosome territories** ([7.3.17](/7.3.17#def-17.7.1)) is therefore not a consequence of equilibrium polymer statistics; it requires tethering to the nuclear envelope and the nucleolus, a slow, nonequilibrium history (chromosomes decondense from compact mitotic rods and have no time to mix), or both. Polymer physics also reads the positions of tagged loci. In *Caulobacter crescentus* each locus has a well-defined position along the cell, with a standard deviation of about $0.2\,\mu\mathrm{m}$ independent of its genomic position. If the scatter is that of a free loop of DNA of $N_{\mathrm{bp}}$ base pairs anchored at its ends, $\sigma_x^2 = \langle R^2\rangle/3 = N_{\mathrm{bp}}b/(3\nu_{\ell})$ with $b = 100\,\mathrm{nm}$ and $\nu_{\ell} = 3\,\mathrm{bp\,nm^{-1}}$ gives $N_{\mathrm{bp}} \approx 4\,\mathrm{kb}$ (about twice that for a closed loop): the chromosome behaves as a chain of domains of about 10 kb tied down along the cell, consistent with the topological domains of bacterial chromosomes measured in other ways.

### 21.6.2. Contact Probability and Hi-C

**Chromosome conformation capture** and its genome-wide version Hi-C ([7.2.4](/7.2.4#sec-4.3)) measure, for every pair of loci, how often they are crosslinked together in a population of cells. Averaged over the genome, this gives the contact probability $P(s)$ as a function of the genomic separation $s$: a direct test of polymer models, since Eq. (21.15) is a contact probability.

**Definition 21.6.1 (Contact Probability)** The **contact probability** $P(s)$ of a polymer is the probability that two monomers separated by $s$ along the chain are within a fixed capture distance of each other, averaged over all such pairs and over conformations.

**Proposition 21.6.1 (Mean-Field Contact Scaling)** If a stretch of $s$ monomers has size $R(s) \propto s^{\nu}$ and its ends are distributed over a volume of order $R(s)^3$, then

$$
P(s) \propto s^{-3\nu}: \qquad s^{-3/2}\ \text{for an ideal chain}, \qquad s^{-1}\ \text{for a chain compact on all scales}. \tag{21.19}
$$

**Proof** The probability that one end lies within a capture volume $v_{\mathrm{c}}$ of the other is $v_{\mathrm{c}}$ times the density of the end-to-end distribution at contact, which is of order $1/R(s)^3$. For an ideal chain this is exact by Eq. (21.15). For a compact stretch, $\nu = 1/3$. $\square$

The scaling distinguishes models of chromatin. An ideal chain confined in a nucleus, the equilibrium globule, follows $s^{-3/2}$ until a stretch fills the available volume and then levels off: distant loci meet as often as any. Yeast chromosomes up to about 100 kb follow $s^{-3/2}$. Human interphase chromosomes do not: Lieberman-Aiden and colleagues (2009) found $P(s) \propto s^{-1.08}$ over $0.5$–$7\,\mathrm{Mb}$, close to the prediction for a fractal globule.

**Definition 21.6.2 (Fractal Globule)** A **fractal globule** (crumpled globule, Grosberg, Nechaev and Shakhnovich, 1988) is a compact, unknotted, nonequilibrium conformation of a long polymer in which every stretch of the chain is itself compact, $R(s) \propto s^{1/3}$, and occupies its own region of space, as when a chain collapses hierarchically, first into small globules and then into globules of globules.

The fractal globule has properties attractive for a genome: each locus can be decondensed for transcription without disentangling its neighbors, because the stretches do not interpenetrate, and the territorial organization of whole chromosomes is the same property on the largest scale. The model is not the final word. Higher-resolution Hi-C revealed loops and **topologically associating domains** formed by **loop extrusion** by **cohesin** stopped at CTCF sites ([7.2.4](/7.2.4#sec-4.3)), and polymer simulations with extrusion reproduce both the domains and an exponent near $-1$ over intermediate scales; mitotic chromosomes, compacted by condensin into arrays of loops around an axis, have a shallower $P(s) \propto s^{-0.5}$ up to about 10 Mb. Contact maps are now routinely interpreted by simulations of polymers with such active and specific constraints, a direct application of the models of this chapter.

![Contact probability and chromosome folding. A: two compact folds on a 16 × 16 lattice, colored from one end of the chain to the other: a Hilbert curve, an idealized fractal globule in which every stretch occupies its own compact region, and a confined random walk (an equilibrium globule), whose stretches interpenetrate. B: contact probability against separation along the chain from simulations of 300 random walks of 4096 steps on a cubic lattice: free walks follow s^(−3/2) (Proposition 21.6.1); walks confined to a cube follow s^(−3/2) until a stretch fills the cube and then reach a plateau. The fractal-globule prediction s^(−1) and the slope measured by Hi-C for human chromosomes over 0.5–7 Mb (−1.08) are shown for comparison](./plots/contact-probability.py)

## 21.7. Packing DNA: Viruses and Nucleosomes

### 21.7.1. How Tightly Is DNA Packed?

The ratio of contour length to container size overstates compaction. A better measure is the packing fraction $\phi$, the volume of the DNA itself (about $1\,\mathrm{nm}^3$ per base pair for a cylinder of $2\,\mathrm{nm}$ diameter) divided by the volume of its container. Phage λ packs 48.5 kb into a capsid of inner radius about $27\,\mathrm{nm}$: $\phi \approx 4.85\times10^4\,\mathrm{nm}^3/(\frac43\pi\times27^3\,\mathrm{nm}^3) \approx 0.6$, a density approaching that of DNA crystals. The *E. coli* nucleoid (5 Mb in a region of radius about $0.25\,\mu\mathrm{m}$) has $\phi \approx 0.1$; a human sperm head (protamine-packed, $5\,\mu\mathrm{m}$ across) $\phi \approx 0.02$; a human somatic nucleus ($6\times10^9\,\mathrm{bp}$ in a sphere of radius $5\,\mu\mathrm{m}$) $\phi \approx 0.01$. Only in the phage is the DNA so dense that its packing is a problem of elasticity and electrostatics at the scale of the double helix.

### 21.7.2. Packing a Phage Capsid

Tailed phages and herpesviruses assemble an empty capsid first and then pump their genome into it through a portal by an ATP-driven motor, a ring of five ATPases of the ASCE family in phage φ29. Optical-tweezers measurements (Smith and colleagues, 2001) showed that the φ29 motor packages about 100 bp per second at low filling, slows as the capsid fills, and works against a resisting force that rises to tens of piconewtons near completion; the motor stalls at about $57\,\mathrm{pN}$, which makes it one of the strongest molecular motors known. Its kinetics (2.5 bp per ATP, bursts of 10 bp per cycle of the ring) are a subject of [7.6.28](/7.6.28). Here we compute the force it must overcome.

**Formula 21.7.1 (Inverse-Spool Model)** Suppose the packed DNA is wound as a spool of hoops from the capsid wall inward, hexagonally packed with interaxial spacing $d_{\mathrm{s}}$, in a cylindrical capsid of inner radius $R$ and height $z$. When a length $L$ has been packed, the bending energy of the hoops and the interaction energy of neighboring helices are

$$
G_{\mathrm{bend}} = -\frac{\pi\ell_{\mathrm{p}}k_{\mathrm{B}}Tz}{\sqrt3\,d_{\mathrm{s}}^2}\ln\left(1 - \frac{\sqrt3\,d_{\mathrm{s}}^2L}{2\pi zR^2}\right), \qquad G_{\mathrm{int}} = \sqrt3\,F_0\left(c^2 + cd_{\mathrm{s}}\right)L\,\mathrm{e}^{-d_{\mathrm{s}}/c}, \tag{21.20}
$$
the spacing at each $L$ minimizes $G = G_{\mathrm{bend}} + G_{\mathrm{int}}$, and the resisting force is $F(L) = \mathrm{d}G/\mathrm{d}L$.

The bending energy follows by summing the hoop energy $\pi\ell_{\mathrm{p}}k_{\mathrm{B}}T/R_i$ (Eq. (21.6) with $L = 2\pi R_i$) over hoops: a layer at radius $R'$ holds $z/d_{\mathrm{s}}$ hoops, layers are $\sqrt3 d_{\mathrm{s}}/2$ apart, and the spool fills from the outer radius down to an inner radius set by the packed length. The interaction term integrates the measured osmotic pressure of hexagonally packed DNA, $\Pi(d_{\mathrm{s}}) = F_0\mathrm{e}^{-d_{\mathrm{s}}/c}$, with decay length $c \approx 0.27\,\mathrm{nm}$ over a wide range of salt (Rau and Parsegian, 1984); the repulsion at these separations of a few nanometers comes from the structured water and ions between the helices, a hydration force that the mean-field electrostatics of [7.6.6](/7.6.6) does not capture. The two terms compete: bending favors loose packing, so that the inner hoops are not too tight; repulsion favors uniform spacing. The model gives spacings that decrease from about $4$ to $2.5\,\mathrm{nm}$ during packaging, matching X-ray and cryo-EM measurements, forces of tens of piconewtons and internal pressures of tens of atmospheres at full packing.

![Packing DNA into a phage capsid (inverse-spool model, Formula 21.7.1, with ℓp = 50 nm, F0 = 55,000 pN nm⁻² and c = 0.27 nm). A: DNA packing fraction in a λ capsid, the *E. coli* nucleoid, a human sperm head and a human nucleus (logarithmic axis). B: the interaxial spacing that minimizes the free energy, against the fraction of the genome packaged, for φ29 (19.3 kb) and λ (48.5 kb, a cylinder of the volume of its capsid); it falls to about 2.5 nm, as measured by X-ray scattering. C: the resisting force on the motor, rising steeply in the last third of packaging, with the internal pressure at full packing; the dotted line marks the stall force of the φ29 motor (about 57 pN)](./plots/phage-packing.py)

The stored energy has consequences for infection. Phage λ ejects its genome into a cell within about a minute, and in vitro, ejection into vesicles or after triggering by the receptor LamB is partially or completely suppressed by an external osmotic pressure of a few tens of atmospheres (Evilevitch and colleagues, 2003): the pressure inside the capsid drives the first part of ejection, and the last part is pulled in by processes in the host, such as transcription, binding proteins and the osmotic gradient of the cytoplasm.

### 21.7.3. The Nucleosome

The nucleosome core particle wraps 147 bp in 1.65 left-handed turns around the histone octamer at a radius of about $4.2\,\mathrm{nm}$ ([7.2.4](/7.2.4)). The bending energy is, from Eq. (21.5) with uniform curvature,

$$
G_{\mathrm{bend}} = \frac{\ell_{\mathrm{p}}k_{\mathrm{B}}T}{2R^2}L = \frac{50\,\mathrm{nm}}{2\times(4.2\,\mathrm{nm})^2}\times50\,\mathrm{nm}\times k_{\mathrm{B}}T \approx 70\,k_{\mathrm{B}}T, \tag{21.21}
$$
about $0.5\,k_{\mathrm{B}}T$ per base pair. It is paid by the contacts between the phosphate backbone and the arginines and lysines of the histones at the 14 sites where the minor groove faces the octamer; the net wrapping free energy is the small difference between two large numbers, a few tenths of $k_{\mathrm{B}}T$ per base pair. The bending cost depends on sequence: AA/TT steps in phase with the helical repeat, where the minor groove faces inward, make some sequences bend more easily, which underlies the sequence preferences of **nucleosome positioning** ([7.2.4](/7.2.4)).

The small net free energy makes the nucleosome dynamic. Thermal fluctuations transiently peel DNA from the ends, exposing sites inside it to proteins: the site-exposure model (Polach and Widom, 1995).

**Proposition 21.7.1 (Site Exposure)** Let a protein bind a site inside a nucleosome only when the DNA has unwrapped from the nearer end up to the site, $x$ base pairs from the entry point, and let unwrapping cost a free energy $g$ per base pair beyond an initial unwrapping equilibrium $K_0$. Then the site is exposed with equilibrium constant $K_{\mathrm{exp}}(x) = K_0\mathrm{e}^{-gx/k_{\mathrm{B}}T}$, and a protein at concentration $c$ with dissociation constant $K_{\mathrm{d}}$ for naked DNA occupies the site with probability

$$
p = \frac{K_{\mathrm{exp}}c/K_{\mathrm{d}}}{1 + K_{\mathrm{exp}}c/K_{\mathrm{d}}}, \tag{21.22}
$$
that is, with an apparent dissociation constant $K_{\mathrm{d}}/K_{\mathrm{exp}}$ (assuming $K_{\mathrm{exp}} \ll 1$).

**Proof** The states are wrapped (weight 1), unwrapped to the site and empty (weight $K_{\mathrm{exp}}$), and unwrapped and bound (weight $K_{\mathrm{exp}}c/K_{\mathrm{d}}$); the bound fraction is the ratio of the last weight to the sum, which is Eq. (21.22) when $K_{\mathrm{exp}} \ll 1$. $\square$

Restriction-enzyme digestion of sites at known positions gave equilibrium constants falling from about $10^{-2}$ near the entry to about $10^{-4}$–$10^{-5}$ in the middle of the nucleosome, consistent with $g \approx 0.1$–$0.2\,k_{\mathrm{B}}T$ per base pair. Single-molecule FRET showed the kinetics: a nucleosome stays fully wrapped for about $250\,\mathrm{ms}$ and then unwraps transiently for $10$–$50\,\mathrm{ms}$ (Li, Levitus, Bustamante and Widom, 2005). The site-exposure equilibrium is also a mechanism of cooperativity: two transcription factors binding sites in the same nucleosome share the cost of unwrapping, so the binding of one raises the occupancy of the other without any contact between them. Under force, the outer turn unwraps gradually at a few piconewtons and the inner turn abruptly at 20–30 pN ([7.6.17](/7.6.17)), the forces at which polymerases and remodelers ([7.2.15](/7.2.15)) work.

![Energetics of the nucleosome and the accessibility of wrapped DNA. A: free-energy budget per base pair of nucleosomal DNA: bending at a radius of 4.2 nm costs about +0.48 kBT per bp (Eq. (21.21)), adhesion to the histones gains about −0.6 kBT per bp, and the net is a small fraction of either. B: the site-exposure model (Proposition 21.7.1): equilibrium constant of exposing a site against its distance from the entry point, for net unwrapping costs of 0.1, 0.15 and 0.2 kBT per bp, with the approximate band of values measured by restriction-enzyme accessibility. C: occupancy of a site by a protein against its concentration relative to its dissociation constant for naked DNA, for sites 10, 30 and 60 bp inside the nucleosome (g = 0.15 kBT per bp): wrapping shifts the binding curve by the factor 1/K_exp, up to five orders of magnitude for central sites](./plots/nucleosome-accessibility.py)

## Summary

| Model | Key result | Where |
|---|---|---|
| Freely jointed chain | $\langle R^2\rangle = Nb^2$, Gaussian $P(\boldsymbol{R})$, $R_{\mathrm{g}}^2 = Nb^2/6$ | Proposition 21.1.1 |
| Real chain at large scales | Kuhn length $b = \langle R^2\rangle/L$; DNA $b \approx 100\,\mathrm{nm}$ | Definition 21.1.2 |
| Entropic spring | $k = 3k_{\mathrm{B}}T/(Lb)$, proportional to $T$ | Proposition 21.2.1 |
| FJC under force | $\langle z\rangle = L\,\mathcal{L}(Fb/k_{\mathrm{B}}T)$, $1 - z \propto F^{-1}$ | Theorem 21.2.1 |
| Worm-like chain | $\langle\boldsymbol{t}(s)\cdot\boldsymbol{t}(0)\rangle = \mathrm{e}^{-s/\ell_{\mathrm{p}}}$, $\ell_{\mathrm{p}} = \kappa/k_{\mathrm{B}}T$; $b = 2\ell_{\mathrm{p}}$ | Proposition 21.3.1, Eq. (21.10) |
| Rod to coil | $\langle R^2\rangle = 2\ell_{\mathrm{p}}L - 2\ell_{\mathrm{p}}^2(1 - \mathrm{e}^{-L/\ell_{\mathrm{p}}})$ | Formula 21.3.1 |
| WLC under force | linear $2\ell_{\mathrm{p}}LF/3k_{\mathrm{B}}T$; $1 - z = \frac12(k_{\mathrm{B}}T/F\ell_{\mathrm{p}})^{1/2}$; Marko–Siggia | Eqs. (21.11)–(21.12), Formula 21.3.2 |
| Excluded volume | $R \propto N^{\nu}$: $\nu = 1/2$ ideal, $0.588$ good solvent, $1/3$ globule | Definition 21.4.1, Proposition 21.4.1 |
| Looping | $J = P(\boldsymbol{0})/N_{\mathrm{A}}$; circle model optimum $13\ell_{\mathrm{p}}$; WLC optimum $\approx 550\,\mathrm{bp}$, $J \approx 100\,\mathrm{nM}$; phasing with 10.5 bp period | Definition 21.5.1, Proposition 21.5.1, Eq. (21.18) |
| Chromosomes | free coils would overlap (territories need tethering or history); $P(s) \propto s^{-3\nu}$: $s^{-3/2}$ ideal, $s^{-1}$ fractal globule, human Hi-C $s^{-1.08}$ | Example 21.6.1, Proposition 21.6.1, Definition 21.6.2 |
| Phage packing | bending plus hydration repulsion; $d_{\mathrm{s}} \to 2.5\,\mathrm{nm}$, forces of tens of pN, pressures of tens of atm | Formula 21.7.1 |
| Nucleosome | bending $\approx 70\,k_{\mathrm{B}}T$, net wrapping a few tenths of $k_{\mathrm{B}}T$ per bp; site exposure $K_0\mathrm{e}^{-gx}$ | Eq. (21.21), Proposition 21.7.1 |

The numbers to remember for DNA: $0.34\,\mathrm{nm}$ per bp, $\ell_{\mathrm{p}} = 50\,\mathrm{nm} = 150\,\mathrm{bp}$, $b = 100\,\mathrm{nm}$, $k_{\mathrm{B}}T/\ell_{\mathrm{p}} \approx 0.08\,\mathrm{pN}$ (the force scale at which DNA begins to straighten), bending a full circle of length $L$ costs $3000/N_{\mathrm{bp}}$ in units of $k_{\mathrm{B}}T$.

## Questions

1. A protein is denatured into a chain of 200 residues with a Kuhn length of $0.8\,\mathrm{nm}$ and $0.38\,\mathrm{nm}$ per residue. Estimate its radius of gyration as an ideal chain and as a self-avoiding chain using $R_{\mathrm{g}} \approx 0.2\,\mathrm{nm}\times N^{0.59}$, and compare with the folded protein ($R_{\mathrm{g}} \approx 0.22\,\mathrm{nm}\times N^{0.38}$).

   **Answer** Contour length $L = 76\,\mathrm{nm}$, ideal $R_{\mathrm{g}} = \sqrt{Lb/6} = \sqrt{76\times0.8/6} = 3.2\,\mathrm{nm}$. Self-avoiding: $200^{0.59} = 22.8$, $R_{\mathrm{g}} \approx 4.6\,\mathrm{nm}$. Folded: $200^{0.38} = 7.5$, $R_{\mathrm{g}} \approx 1.7\,\mathrm{nm}$. The denatured chain in a good solvent (urea, guanidinium) is swollen beyond ideal by excluded volume, and about 2.7 times larger than the native protein, which is what SAXS measures on unfolding.

2. Show that the stiffness of the entropic spring of λ DNA is about $7\,\mathrm{fN}\,\mu\mathrm{m}^{-1}$, and estimate the root-mean-square thermal fluctuation of its end-to-end distance along one axis. Why is a stretching force of at least $0.1\,\mathrm{pN}$ needed for a well-defined extension?

   **Answer** $k = 3k_{\mathrm{B}}T/(Lb) = 3\times4.1/(1.65\times10^4\times100)\,\mathrm{pN\,nm^{-1}} = 7.5\times10^{-6}\,\mathrm{pN\,nm^{-1}} = 7.5\,\mathrm{fN}\,\mu\mathrm{m}^{-1}$. By equipartition $\langle x^2\rangle = k_{\mathrm{B}}T/k = Lb/3$, so $\sigma_x = \sqrt{1.65\times10^4\times100/3}\,\mathrm{nm} \approx 0.74\,\mu\mathrm{m}$. A force must extend the chain by much more than this, i.e. into the nonlinear regime where $Fb \gtrsim k_{\mathrm{B}}T$, $F \gtrsim 0.04\,\mathrm{pN}$; at $0.1\,\mathrm{pN}$ the WLC extension is about 53 % of $L$ (Formula 21.3.2) and the fluctuations are a fraction of it.

3. From Formula 21.3.2, what force is needed to extend DNA to 90 % of its contour length? Compare with the freely jointed chain prediction with $b = 100\,\mathrm{nm}$.

   **Answer** With $z = 0.9$: $F\ell_{\mathrm{p}}/k_{\mathrm{B}}T = 0.9 + 1/(4\times0.01) - 0.25 = 25.65$, $F = 25.65\times4.1/50 \approx 2.1\,\mathrm{pN}$. For the FJC, $\mathcal{L}(u) = 0.9$ requires $u \approx 10$, $F = 10k_{\mathrm{B}}T/b \approx 0.41\,\mathrm{pN}$. The FJC reaches high extension five times too easily, because it lacks the short-wavelength undulations that only large forces suppress.

4. Derive Eq. (21.10), $b = 2\ell_{\mathrm{p}}$, and explain why the Kuhn length is longer than the persistence length.

   **Answer** For $L \gg \ell_{\mathrm{p}}$, Eq. (21.8) gives $\langle R^2\rangle \to 2\ell_{\mathrm{p}}L$, and Definition 21.1.2 gives $b = \langle R^2\rangle/L = 2\ell_{\mathrm{p}}$. The persistence length is the decay length of correlations in one direction from a point; a Kuhn segment must replace the correlated stretches on both sides, and the integral of $\mathrm{e}^{-\lvert s\rvert/\ell_{\mathrm{p}}}$ over all $s$ is $2\ell_{\mathrm{p}}$.

5. A repressor binds an auxiliary operator with $K_{\mathrm{d}} = 10\,\mathrm{nM}$. Using Eq. (21.18), for which loop lengths of naked DNA does looping dominate over the unlooped singly bound state? What does the strong repression by the 92 bp lac O1–O3 loop in vivo imply?

   **Answer** Looping dominates when $J > K_{\mathrm{d}} = 10\,\mathrm{nM}$. Solving Eq. (21.18) gives $J = 10\,\mathrm{nM}$ at $n \approx 0.78$ (about 230 bp) on the short side and $n \approx 14$ (about 4 kb) on the long side, with a maximum of about 100 nM near 550 bp; between these lengths the looped state wins. At 92 bp ($n = 0.31$) the naked-DNA value carries the factor $\mathrm{e}^{-2.66/0.31^2} \approx 10^{-12}$ and is negligible. The strong O1–O3 loop in vivo therefore requires help: bending by HU and IHF, supercoiling and the flexibility of the repressor tetramer raise the in vivo J factor by many orders of magnitude above the naked-DNA value.
6. Show that a one-dimensional random walk of $N$ steps returns to the origin with probability approximately $\sqrt{2/(\pi N)}$, and explain why cyclization in three dimensions falls faster with length.

   **Answer** Returning requires $N/2$ steps each way: $\binom{N}{N/2}2^{-N}$. With Stirling's approximation $n! \approx \sqrt{2\pi n}(n/\mathrm{e})^n$, $\binom{N}{N/2} \approx 2^N\sqrt{2/(\pi N)}$. In $d$ dimensions the end-to-end density at the origin scales as $\langle R^2\rangle^{-d/2} \propto N^{-d/2}$, because the ends spread over a volume $R^d$; in three dimensions $N^{-3/2}$.

7. Use the Flory argument to find the exponent $\nu$ in $d$ dimensions, and evaluate it for $d = 1, 2, 3, 4$. What does the result for $d = 4$ suggest?

   **Answer** $F/k_{\mathrm{B}}T \sim R^2/(Nb^2) + vN^2/R^d$; minimizing, $R^{d+2} \propto N^3$, $\nu = 3/(d + 2)$: $1$ in one dimension (exact: a self-avoiding walk on a line is straight), $3/4$ in two (exact), $3/5$ in three (exact value $0.588$) and $1/2$ in four. Above four dimensions the ideal value $1/2$ is reached: random walks rarely intersect themselves in high dimensions, so excluded volume becomes irrelevant (four is the upper critical dimension).

8. In the yeast nucleus (Example 21.6.1), what Kuhn length and packing density of chromatin would make a free chromosome's coil as dense as the nucleus? Is this plausible?

   **Answer** Require $N_{\mathrm{bp}}/(\frac43\pi R_{\mathrm{g}}^3) = 3\,\mathrm{Mb}\,\mu\mathrm{m}^{-3}$ for $N_{\mathrm{bp}} = 750\,\mathrm{kb}$, i.e. $R_{\mathrm{g}} \approx 0.39\,\mu\mathrm{m}$, $R_{\mathrm{g}}^2 = N_{\mathrm{bp}}b/(6\nu_{\ell}) = 0.15\,\mu\mathrm{m}^2$, so $b/\nu_{\ell} \approx 1.2\,\mathrm{nm^2\,bp^{-1}}$. A nucleosomal fiber has $b/\nu_{\ell} \approx 60/8 = 7.5\,\mathrm{nm^2\,bp^{-1}}$; even a 30 nm fiber ($400/100 = 4$) is too stiff or too extended. Chromosomes would need to be several times more compact than any free fiber, which supports confinement-driven overlap or specific compaction (loops, tethering) rather than free coils.

9. (Design) You want to test whether a DNA-bending protein facilitates looping. Propose a cyclization or tethered-particle experiment, the DNA lengths you would use and the expected signature.

   **Answer** Prepare fragments of 100–600 bp with cohesive ends and measure J by ligase-dependent cyclization relative to dimerization, with and without the protein (or use single-molecule FRET between dyes at the ends, or tethered-particle motion with a looping protein). Choose lengths around and below the WLC optimum (150–300 bp) and vary the length in single base pairs to probe helical phasing. A bending protein should raise J most at short lengths (where bending dominates), shift the optimum to shorter loops and reduce the phasing oscillation if it introduces flexibility; at long lengths (several kb), where J is entropic, it should have little effect. Controls: a non-bending DNA-binding protein of similar size, and measurement of J in the absence of protein against Eq. (21.18).

10. Estimate the bending energy per base pair and in total for DNA wrapped in the nucleosome, and the equilibrium constant for exposing a site 40 bp inside if $g = 0.15\,k_{\mathrm{B}}T$ per bp and $K_0 = 0.1$. By what factor does a transcription factor with naked-DNA $K_{\mathrm{d}} = 1\,\mathrm{nM}$ need higher concentration to occupy that site half the time?

    **Answer** Per bp: $\ell_{\mathrm{p}}\times0.34\,\mathrm{nm}/(2R^2) = 50\times0.34/(2\times17.6) = 0.48\,k_{\mathrm{B}}T$; for 147 bp about $71\,k_{\mathrm{B}}T$. $K_{\mathrm{exp}} = 0.1\,\mathrm{e}^{-6} = 2.5\times10^{-4}$. Half occupancy needs $c = K_{\mathrm{d}}/K_{\mathrm{exp}} = 4\,\mu\mathrm{M}$, 4000 times more than on naked DNA, unless another factor or a remodeler unwraps the DNA.

11. Using Formula 21.7.1, explain qualitatively why the force resisting packaging rises steeply only in the last third of filling, and how increasing the concentration of $\ce{Mg^2+}$ (which lowers $F_0$ and can make packed DNA attractive) would change the force.

    **Answer** Early in packaging the DNA is loosely packed ($d_{\mathrm{s}} \approx 4\,\mathrm{nm}$): the repulsion decays as $\mathrm{e}^{-d_{\mathrm{s}}/c}$ with $c = 0.27\,\mathrm{nm}$ and is negligible, and the outer hoops have large radii, so the bending energy per added length is small. As the spool fills, the inner radius shrinks (bending cost per hoop $\propto 1/R_i$) and the spacing must fall towards $2.5\,\mathrm{nm}$, where the exponential repulsion rises by a factor of $\mathrm{e}$ for every $0.27\,\mathrm{nm}$, so the force grows steeply. Lower $F_0$ (more $\ce{Mg^2+}$, or polyamines) lowers the interaction term and hence the force and the internal pressure; with net attraction, DNA condenses and the motor works mainly against bending. Experiments indeed show lower resisting forces and slower ejection with multivalent ions.
