---
title: "Biological Membranes: Elasticity and Shape"
description: "The physics of lipid bilayers: the thermodynamics of self-assembly and the critical micelle concentration, the packing parameter and lipid polymorphism (gel, fluid, liquid-ordered, hexagonal and cubic phases), the geometry of curved surfaces and the elastic energies of stretching, bending, thickness change and Gaussian curvature, micropipette aspiration, undulation spectra and tether pulling, the energetics of vesicles and three models of budding, fusion and fission through stalks and hemifusion, the shapes of organelles and red blood cells, and surface tension in the lung."
---

A lipid bilayer is five nanometers thick and can be tens of micrometers across: on the scale of a cell it is a two-dimensional elastic sheet, and a fluid one, which resists stretching strongly, bending weakly and shearing not at all. These three facts, together with the hydrophobic effect that assembles the sheet in the first place, explain much of what membranes do. They set how much energy a cell must spend to make a vesicle, why vesicles of all sizes cost the same, why membranes fluctuate visibly under a microscope, what force pulls a tube out of a membrane, how coats, domains and viruses bud membranes, why fusion and fission need protein machines, and why a red blood cell is a biconcave disc. This chapter develops the physics in the style of the rest of the course: geometry first, then the energy as a functional of the shape, then measurements, estimates and minimal models.

The biochemistry of membrane lipids is in [7.1.12](/7.1.12) and that of membranes and transport in [7.1.13](/7.1.13); the cell biology of membranes, including a first account of the bending energy and of tether forces, is in [7.3.4](/7.3.4#sec-4.7), and the coats, **SNAREs** and fission machines of vesicle traffic in [7.3.8](/7.3.8) and [7.3.10](/7.3.10). Surface tension, the **Young–Laplace equation**, **surfactants** and **micelles** come from [6.3.19](/6.3.19), and the calorimetry of the main phase transition from [7.6.8](/7.6.8#sec-8.5). The membrane proteins that deform and sense the bilayer, in particular mechanosensitive channels, are the subject of the next chapter, [7.6.25](/7.6.25); whole-cell mechanics follows in [7.6.31](/7.6.31).

## 24.1. Self-Assembly of Amphiphiles

### 24.1.1. The Thermodynamics of Aggregation

Phospholipids, cholesterol, detergents and soaps are amphiphiles: a polar head attached to one or two hydrocarbon chains. In water the chains are hidden from the solvent by assembly into aggregates, driven by the **hydrophobic effect** ([7.1.2](/7.1.2), [7.6.6](/7.6.6)), opposed by the repulsion of the head groups (steric, electrostatic and hydration forces) and by the entropy of mixing, which favors free molecules. Let $\mu_N^\circ$ be the standard chemical potential per molecule in an aggregate of $N$ molecules and $X_N$ the mole fraction of molecules in such aggregates. Equilibrium between free molecules and aggregates requires equal chemical potentials per molecule,

$$
\mu_1^\circ + k_{\mathrm{B}}T\ln X_1 = \mu_N^\circ + \frac{k_{\mathrm{B}}T}{N}\ln\frac{X_N}{N}, \qquad\text{so}\qquad X_N = N\left[X_1\,\mathrm{e}^{(\mu_1^\circ - \mu_N^\circ)/k_{\mathrm{B}}T}\right]^N, \tag{24.1}
$$
the law of mass action for $N$ monomers forming one aggregate. Define $X_{\mathrm{c}} = \mathrm{e}^{-(\mu_1^\circ - \mu_N^\circ)/k_{\mathrm{B}}T}$. Then $X_N = N(X_1/X_{\mathrm{c}})^N$, and since $X_N$ cannot exceed the total concentration, $X_1$ cannot exceed $X_{\mathrm{c}}$ appreciably: for large $N$, the term $(X_1/X_{\mathrm{c}})^N$ is negligible for $X_1 < X_{\mathrm{c}}$ and explosive above it.

**Proposition 24.1.1 (Critical Micelle Concentration)** For aggregates of a preferred size $N \gg 1$, the free monomer concentration saturates at $X_{\mathrm{c}} = \exp[-(\mu_1^\circ - \mu_N^\circ)/k_{\mathrm{B}}T]$: below this concentration nearly all amphiphiles are free; above it the monomer concentration stays nearly constant and all added molecules enter aggregates. $X_{\mathrm{c}}$ is the **critical micelle concentration** ([6.3.19](/6.3.19#def-19.7.2)), and the transition sharpens as $N$ grows.

The free-energy gain $\mu_1^\circ - \mu_N^\circ$ is proportional to the hydrophobic area buried, so the critical micelle concentration falls exponentially with chain length (Klevens' rule): about twofold per $\ce{CH2}$ group for ionic detergents, and threefold for lipids. A second chain doubles the hydrophobic surface. Sodium dodecyl sulfate, with one $\mathrm{C}_{12}$ chain, has a critical micelle concentration of $8.2\,\mathrm{mM}$; dipalmitoylphosphatidylcholine (DPPC), with two $\mathrm{C}_{16}$ chains, about $0.5\,\mathrm{nM}$. This difference of seven orders of magnitude has two biological consequences. A phospholipid bilayer is not in equilibrium with a significant concentration of free lipid: spontaneous exchange of phospholipids between membranes through the water takes hours, and cells move lipids between organelles with transfer proteins at membrane contact sites and by vesicles. And detergents, whose monomers are abundant, can partition into membranes and dissolve them into mixed micelles, the basis of membrane protein purification ([7.3.4](/7.3.4#sec-4.3)).

![Self-assembly of amphiphiles. A: mass-action model of micellization (Eq. (24.1)) for aggregates of N = 60 molecules: below the critical micelle concentration almost all molecules are free; above it the free monomer concentration saturates and every added molecule joins a micelle. B: measured critical micelle concentrations against chain length for single-chain sodium alkyl sulfates and two-chain diacylphosphatidylcholines: each added CH₂ lowers the CMC two- to threefold, and two chains instead of one lower it by many orders of magnitude, to 0.5 nM for DPPC](./plots/cmc.py)

### 24.1.2. The Packing Parameter

Why do detergents form micelles and phospholipids bilayers? Geometry decides. In an aggregate the head groups sit at the water interface with an optimal area $a_0$ per molecule (set by the balance between the interfacial free energy, which favors small areas, and head-group repulsion), and the chains fill the interior without leaving voids, while no chain can stretch beyond its maximal length $l$.

**Definition 24.1.1 (Packing Parameter)** The **packing parameter** of an amphiphile is $P = v/(a_0l)$, where $v$ is the volume of its hydrocarbon chains, $l$ their maximal (critical) length and $a_0$ the optimal head-group area at the aggregate surface (Israelachvili, Mitchell and Ninham 1976).

**Proposition 24.1.2** An aggregate of radius (or half-thickness) $R \le l$ can be filled by amphiphiles with head-group area $a_0$ only if $P \le 1/3$ for spheres, $P \le 1/2$ for cylinders and $P \le 1$ for bilayers.

**Proof** For a sphere of $N$ molecules, the volume and area are $Nv = \frac43\pi R^3$ and $Na_0 = 4\pi R^2$, so $R = 3v/a_0$; the condition $R \le l$ gives $v/(a_0l) \le 1/3$. For a cylinder of length $L$: $Nv = \pi R^2L$, $Na_0 = 2\pi RL$, $R = 2v/a_0 \le l$. For a bilayer of half-thickness $R$ and area $A$: $Nv = 2RA$ (both leaflets), $Na_0 = 2A$, $R = v/a_0 \le l$. $\square$

Single-chain amphiphiles with large heads (SDS, lysophospholipids, $P < 1/3$) form spherical micelles; with screened charges (SDS in high salt) or smaller heads, cylindrical micelles ($1/3 < P < 1/2$); two-chain lipids with heads of matching size (phosphatidylcholine, sphingomyelin, phosphatidylserine) form bilayers ($1/2 < P \le 1$). Lipids with small heads relative to their chains, $P > 1$, such as phosphatidylethanolamine, diacylglycerol and cardiolipin (especially with $\ce{Ca^2+}$, which neutralizes and dehydrates its head), cannot fill a flat bilayer comfortably and form inverted phases in which the heads line water channels. The shape of a lipid is also its tendency to curve a monolayer: cone-shaped lipids favor positive curvature (towards the tails), inverted cones negative curvature (towards the heads). This is the molecular origin of the **spontaneous curvature** of a monolayer and, when the two leaflets differ, of a bilayer ([7.3.4](/7.3.4#sec-4.7.2)).

![Molecular shape and aggregate geometry (schematic; packing parameter P = v/(a₀l), Definition 24.1.1). Cone-shaped amphiphiles with one chain and a large head (P < 1/3) pack into spherical micelles; cylindrical lipids (1/2 < P < 1) into bilayers; inverted cones with small heads (P > 1) into the inverted hexagonal phase H_II, in which the head groups line water channels. Increasing P changes the preferred curvature of a monolayer from positive (bending away from the heads) to negative](./plots/packing-shapes.py)

### 24.1.3. Lipid Polymorphism

Hydrated lipids form a variety of phases, named in the notation of Luzzati: a capital letter for the lattice (L lamellar, H hexagonal, Q cubic, M micellar), a subscript I for normal (oil in water) and II for inverted (water in oil) topology, and a Greek subscript for the chain state (β ordered gel, α liquid).

| Phase | Structure | Chains | Examples |
|---|---|---|---|
| $\mathrm{L_c}$ (crystalline) | stacked bilayers, three-dimensional order | crystalline | dry lipids, low temperature |
| $\mathrm{L_\beta}$, $\mathrm{L_{\beta'}}$ (gel) | bilayers | extended, all-*trans*, hexagonally packed; tilted in $\mathrm{L_{\beta'}}$ | saturated PC below $T_{\mathrm{m}}$ |
| $\mathrm{P_{\beta'}}$ (ripple) | periodically corrugated bilayers | partly ordered | PC between pretransition and $T_{\mathrm{m}}$ |
| $\mathrm{L_\alpha}$ (fluid, liquid-disordered $\mathrm{L_d}$) | bilayers | disordered, many *gauche* bonds, fast lateral diffusion | biological membranes |
| $\mathrm{L_o}$ (liquid-ordered) | bilayers | ordered like a gel, mobile like a fluid | sphingomyelin or saturated PC with $\ge 30\,\%$ cholesterol |
| $\mathrm{H_I}$, $\mathrm{H_{II}}$ | hexagonally packed cylinders (normal or inverted) | liquid | lysolipids and detergents ($\mathrm{H_I}$); PE, DAG, cardiolipin with $\ce{Ca^2+}$ ($\mathrm{H_{II}}$) |
| $\mathrm{Q_{II}}$ (bicontinuous cubic: $Ia3d$, $Pn3m$, $Im3m$) | a bilayer folded into a periodic minimal surface separating two water networks | liquid | monoolein; prolamellar bodies of etioplasts; crystallization of membrane proteins in "lipidic cubic phase" |

With rising temperature a lipid passes through the sequence $\mathrm{L_c} \to \mathrm{L_\beta} \to \mathrm{L_\alpha} \to \mathrm{Q_{II}} \to \mathrm{H_{II}}$; with rising hydration from inverted to lamellar to normal phases and finally micelles. The main (gel to fluid) transition is a weak **first-order phase transition** ([6.3.8](/6.3.8)) in which the area per lipid increases by about $25\,\%$, the hydrophobic thickness decreases by about $15\,\%$ and the volume increases by about $4\,\%$; its cooperativity is read from the width of the calorimetric peak ([7.6.8](/7.6.8#sec-8.5)).

| Lipid | Chains | $T_{\mathrm{m}}$ / $^\circ\mathrm{C}$ |
|---|---|---|
| DLPC | 12:0 / 12:0 | $-2$ |
| DMPC | 14:0 / 14:0 | $24$ |
| DPPC | 16:0 / 16:0 | $41$ |
| DSPC | 18:0 / 18:0 | $55$ |
| DOPC | 18:1 / 18:1 (*cis*) | $-17$ |
| DMPE | 14:0 / 14:0 | $50$ |
| DPPE | 16:0 / 16:0 | $63$ |

Longer chains raise $T_{\mathrm{m}}$ (more van der Waals contact), *cis* double bonds lower it drastically, especially near the middle of the chain, and smaller head groups raise it: PE melts about $20\,\mathrm{K}$ higher than PC with the same chains, because its amine forms hydrogen bonds with the phosphate of its neighbors. This is the physical basis of the regulation of membrane fluidity by chain length and unsaturation in bacteria, plants and cold-blooded animals ([7.1.13](/7.1.13#sec-13.2.1), [7.3.4](/7.3.4#sec-4.5.4)).

**Definition 24.1.2 (Liquid-Ordered Phase)** The **liquid-ordered phase** ($\mathrm{L_o}$) is a fluid bilayer phase, formed by saturated lipids or sphingomyelin with about $30\,\%$ or more of cholesterol, in which the acyl chains are nearly as extended and ordered as in the gel phase while the lipids keep the lateral mobility of a liquid (diffusion only a few times slower than in the liquid-disordered phase).

Cholesterol has a dual effect. Its rigid ring system orders and stretches the chains of fluid lipids, thickening and stiffening the bilayer and lowering its permeability; between the chains of a gel it disrupts their crystalline packing and fluidizes it. Above about $30\,\mathrm{mol}\,\%$ the main transition disappears from the calorimeter ([7.6.8](/7.6.8#sec-8.5)). Ternary mixtures of a high-melting lipid, a low-melting lipid and cholesterol separate into coexisting $\mathrm{L_o}$ and $\mathrm{L_d}$ phases, visible as micrometer domains in giant vesicles; in the plasma membrane, which lies close to a miscibility critical point at physiological temperature, the corresponding structures are small and transient, the **lipid rafts** of [7.1.13](/7.1.13#sec-13.2.4). The line tension at the boundary between two phases, a few piconewtons, is what lets such domains bud (24.4.3).

Nonlamellar phases matter even though biological membranes are bilayers. Lipids with $P > 1$ make up a large fraction of many membranes (PE is a third of the inner membrane of mitochondria and most of the *E. coli* inner membrane), store curvature stress that modulates membrane proteins, and promote the highly curved intermediates of fusion (24.5). Cubic membranes have been seen in the ER of some cells, in starved amoebae and in the prolamellar bodies of dark-grown plastids, which convert to thylakoid sheets within minutes of illumination.

## 24.2. The Geometry and Energy of a Membrane

### 24.2.1. Describing a Curved Surface

To assign an energy to a shape we first need numbers that describe it. Over a nearly flat patch, the membrane is a height function $h(x, y)$ above a reference plane. At any point, choose local coordinates with the plane tangent to the membrane; to second order,

$$
h(x_1, x_2) = \frac12\sum_{i,j = 1}^{2}C_{ij}x_ix_j, \qquad C_{ij} = \frac{\partial^2h}{\partial x_i\,\partial x_j},
$$
and the symmetric curvature matrix $C$ captures the bending. Its eigenvalues $c_1$ and $c_2$ are the principal curvatures, the largest and smallest curvatures of the curves in which planes through the normal cut the surface, and its eigenvectors their directions ([2.2](/2.2) for the eigenvalue problem).

**Definition 24.2.1 (Mean and Gaussian Curvature)** The **mean curvature** of a surface at a point is $H = \frac12(c_1 + c_2) = \frac12\operatorname{tr}C$ and its **Gaussian curvature** $K = c_1c_2 = \det C$, where $c_1$ and $c_2$ are the principal curvatures.

A sphere of radius $R$ has $H = 1/R$ and $K = 1/R^2$; a cylinder of radius $r$ has $H = 1/2r$ and $K = 0$; a saddle, curved in opposite directions, has $K < 0$, and a minimal surface such as the cubic phases or a catenoid neck has $H = 0$ everywhere with $K < 0$. Both quantities are invariant under rotations of the coordinates, as an energy density must be. Their integrals have different characters: $\oint H^2\,\mathrm{d}A$ depends on the shape, while by the Gauss–Bonnet theorem $\oint K\,\mathrm{d}A = 2\pi\chi = 4\pi(1 - g)$ for a closed surface of genus $g$ (Euler characteristic $\chi$) depends only on its topology.

### 24.2.2. Four Ways to Deform a Membrane

A patch of membrane can be stretched (its area changed), bent (its curvature changed), compressed in thickness, or sheared (deformed at constant area). Each costs an elastic energy quadratic in the deformation, with its own modulus.

**Definition 24.2.2 (Area Expansion Modulus)** The **area expansion modulus** (area stretch modulus) $K_A$ of a membrane relates its tension to its areal strain: $\sigma = K_A\,\Delta A/A_0$, with stretching energy $G_{\mathrm{stretch}} = \frac{K_A}{2}\frac{(\Delta A)^2}{A_0}$.

**Definition 24.2.3 (Helfrich Bending Energy)** The **Helfrich bending energy** of a fluid membrane surface $S$ is

$$
G_{\mathrm{bend}} = \int_S\left[\frac{\kappa}{2}(2H - c_0)^2 + \bar\kappa K\right]\mathrm{d}A, \tag{24.2}
$$
with **bending rigidity** $\kappa$, **spontaneous curvature** $c_0$ ([7.3.4](/7.3.4#def-4.7.1)) and Gaussian curvature modulus $\bar\kappa$ (Helfrich 1973; Canham 1970 and Evans 1974 for red cells). It is the most general energy quadratic in the curvatures that is invariant under rotations and translations of the surface.

**Definition 24.2.4 (Gaussian Curvature Modulus)** The **Gaussian curvature modulus** (saddle-splay modulus) $\bar\kappa$ is the coefficient of the Gaussian curvature in the Helfrich energy. By the Gauss–Bonnet theorem its contribution, $2\pi\bar\kappa\chi$ for a closed surface, changes only when the topology changes (fusion, fission, pore formation); for lipid bilayers $\bar\kappa \approx -(0.8$–$1)\kappa$.

[Formula 4.7.1](/7.3.4#fml-4.7.1) and [Proposition 4.7.1](/7.3.4#prop-4.7.1) of 7.3.4 give the first consequences: a sphere costs $8\pi\kappa$ whatever its radius, and a coat of spontaneous curvature $c_0$ makes vesicles of radius $2/c_0$ free. A negative $\bar\kappa$ means that the Gaussian term favors many separate spheres ($\chi = 2$ each) over a connected network with handles ($\chi < 0$); a positive $\bar\kappa$ would favor saddles and the bicontinuous cubic phases, which form when the lipids' monolayer curvature makes $\bar\kappa$ effectively positive.

The thickness of a bilayer also costs energy to change. If the half-thickness $w$ deviates from its equilibrium value $w_0$ (around a membrane protein whose hydrophobic belt is thicker or thinner than the bilayer),

$$
G_{\mathrm{thick}} = \frac{K_t}{2}\int\left(\frac{w - w_0}{w_0}\right)^2\mathrm{d}A, \tag{24.3}
$$
with $K_t \approx 60\,k_{\mathrm{B}}T\,\mathrm{nm^{-2}}$; this term governs hydrophobic mismatch and the gating of mechanosensitive channels by tension ([7.6.25](/7.6.25)). A pure bilayer is a two-dimensional liquid and has no shear modulus; a cell membrane attached to a protein network, such as the spectrin skeleton of the red cell, acquires one.

| Modulus | Symbol | Typical value | Measured by |
|---|---|---|---|
| Bending rigidity | $\kappa$ | $10$–$25\,k_{\mathrm{B}}T$ ($4$–$10\times10^{-20}\,\mathrm{J}$) for fluid PC; $2$–$3$ times larger with $30\,\%$ cholesterol | undulation spectra, aspiration at low tension, tether force |
| Area expansion modulus | $K_A$ | $0.2$–$0.25\,\mathrm{N\,m^{-1}}$ ($55$–$70\,k_{\mathrm{B}}T\,\mathrm{nm^{-2}}$); about $0.6\,\mathrm{N\,m^{-1}}$ with cholesterol | aspiration at high tension |
| Lysis tension and strain | $\sigma_{\mathrm{lys}}$ | $5$–$10\,\mathrm{mN\,m^{-1}}$ at $2$–$5\,\%$ areal strain | aspiration |
| Thickness modulus | $K_t$ | about $60\,k_{\mathrm{B}}T\,\mathrm{nm^{-2}}$ | X-ray, molecular simulation |
| Gaussian modulus | $\bar\kappa$ | about $-\kappa$ | phase behavior, simulation |
| Shear modulus (red cell, from the skeleton) | $\mu_{\mathrm{s}}$ | about $6\,\mu\mathrm{N\,m^{-1}}$ | aspiration, optical tweezers |

The moduli are connected. If the bilayer is modeled as an elastic slab of thickness $d$, bending compresses one face and stretches the other, and $\kappa = K_Ad^2/\beta$ with $\beta = 12$ for a slab and $\beta \approx 48$ for two leaflets that can slide past each other (a polymer-brush model). With $K_A = 0.24\,\mathrm{N\,m^{-1}}$ and a hydrophobic thickness $d = 4\,\mathrm{nm}$, $\beta = 48$ gives $\kappa = 0.24 \times 16\times10^{-18}/48\,\mathrm{J} = 8\times10^{-20}\,\mathrm{J} = 20\,k_{\mathrm{B}}T$, as measured: the softness of membranes to bending is a consequence of their thinness. The ratio $\kappa/K_A \approx (0.6\,\mathrm{nm})^2$ means that a membrane under any realistic tension bends rather than stretches: changing its area by $1\,\%$ costs $K_A \times 10^{-4}/2 \approx 3\times10^{-3}\,k_{\mathrm{B}}T\,\mathrm{nm^{-2}}$, while bending it to a radius of $1\,\mu\mathrm{m}$ costs $2\kappa/R^2 = 4\times10^{-5}\,k_{\mathrm{B}}T\,\mathrm{nm^{-2}}$.

**Definition 24.2.5 (Membrane Tension)** The **membrane tension** $\sigma$ is the force per unit length in the plane of the membrane, the derivative of its free energy with respect to its area at fixed shape. In a closed vesicle it is set by the pressure difference through the Young–Laplace law $\Delta p = 2\sigma/R$; in a cell it combines the tension of the bilayer with the adhesion of the bilayer to the cortex, and it is the coupling through which mechanical forces act on membrane proteins.

The tension of a membrane has two origins. At low tension a fluid membrane fluctuates, and pulling on it first pulls out the thermal undulations, an entropic elasticity analogous to that of a polymer chain ([7.6.21](/7.6.21)); only at higher tensions does the area per lipid increase, against $K_A$ (24.3.2).

## 24.3. Measuring Membrane Mechanics

### 24.3.1. Micropipette Aspiration

A giant unilamellar vesicle (radius $R_{\mathrm{v}}$ of $10$–$30\,\mu\mathrm{m}$) is held in a glass pipette of inner radius $R_{\mathrm{p}}$ by suction $\Delta p$, and its projection of length $l$ into the pipette is measured as $\Delta p$ is stepped up (Evans and colleagues). The membrane tension is uniform (the membrane is fluid), and the Young–Laplace law applied to the spherical outer part and the hemispherical cap in the pipette, $p_{\mathrm{in}} - p_{\mathrm{out}} = 2\sigma/R_{\mathrm{v}}$ and $p_{\mathrm{in}} - p_{\mathrm{pip}} = 2\sigma/R_{\mathrm{p}}$, gives

$$
\sigma = \frac{\Delta p\,R_{\mathrm{p}}}{2(1 - R_{\mathrm{p}}/R_{\mathrm{v}})}. \tag{24.4}
$$
The volume of the vesicle is fixed by its impermeable solutes on the time scale of the experiment, so an increase of the projection length is an increase of area: $\Delta A \approx 2\pi R_{\mathrm{p}}\Delta l(1 - R_{\mathrm{p}}/R_{\mathrm{v}})$. Plotting $\sigma$ against $\Delta A/A_0$ gives $K_A$ from the slope at high tension and $\kappa$ from the logarithmic regime at low tension (Formula 24.3.2).

**Example 24.3.1** A vesicle of $R_{\mathrm{v}} = 20\,\mu\mathrm{m}$ in a pipette of $R_{\mathrm{p}} = 4\,\mu\mathrm{m}$ under $\Delta p = 50\,\mathrm{Pa}$ has, by Eq. (24.4), $\sigma = 50 \times 4\times10^{-6}/(2 \times 0.8)\,\mathrm{N\,m^{-1}} = 0.125\,\mathrm{mN\,m^{-1}}$. Raising $\Delta p$ to $2\,\mathrm{kPa}$ raises $\sigma$ to $5\,\mathrm{mN\,m^{-1}}$, near the lysis tension; the elastic strain at that tension is $\sigma/K_A = 5\times10^{-3}/0.24 = 2\,\%$, which for a vesicle of area $5\times10^3\,\mu\mathrm{m^2}$ pulls an extra $100\,\mu\mathrm{m^2}$ of membrane into the pipette, a projection of about $5\,\mu\mathrm{m}$, easily measured.

### 24.3.2. Thermal Undulations

Fluid membranes flicker visibly under a microscope; the flicker of red blood cells was described in the nineteenth century and analyzed by Brochard and Lennon (1975). For a nearly flat patch of area $A$ under tension $\sigma$, write $h(\boldsymbol{r}) = \sum_{\boldsymbol{q}}h_{\boldsymbol{q}}\mathrm{e}^{\mathrm{i}\boldsymbol{q}\cdot\boldsymbol{r}}$. To quadratic order, the mean curvature is $H \approx \frac12\nabla^2h$ and the excess area over the projected area is $\frac12\int\lvert\nabla h\rvert^2\,\mathrm{d}A$, so (with $c_0 = 0$ and ignoring the topological Gaussian term)

$$
G = \int\left[\frac{\kappa}{2}(\nabla^2h)^2 + \frac{\sigma}{2}\lvert\nabla h\rvert^2\right]\mathrm{d}A = \frac A2\sum_{\boldsymbol{q}}(\kappa q^4 + \sigma q^2)\lvert h_{\boldsymbol{q}}\rvert^2, \tag{24.5}
$$
a sum of independent quadratic terms, one for each Fourier mode.

**Formula 24.3.1 (Undulation Spectrum)** By the **equipartition theorem** applied to each mode,

$$
\langle\lvert h_{\boldsymbol{q}}\rvert^2\rangle = \frac{k_{\mathrm{B}}T}{A(\kappa q^4 + \sigma q^2)}.
$$
Bending dominates for $q > q_{\mathrm{c}} = \sqrt{\sigma/\kappa}$, where $\langle\lvert h_q\rvert^2\rangle \propto q^{-4}$, and tension for $q < q_{\mathrm{c}}$, where $\propto q^{-2}$. Fitting measured spectra (flicker spectroscopy of vesicles and cells) gives $\kappa$ and $\sigma$ separately.

The mean square amplitude of a tensionless patch of size $L$, $\langle h^2\rangle = \sum_q\langle\lvert h_q\rvert^2\rangle \approx \frac{k_{\mathrm{B}}T}{4\pi\kappa}\,q_{\min}^{-2} = \frac{k_{\mathrm{B}}TL^2}{16\pi^3\kappa}$ (with $q_{\min} = 2\pi/L$), is dominated by the longest wavelengths and grows with the size of the patch: with $\kappa = 20\,k_{\mathrm{B}}T$ a $10\,\mu\mathrm{m}$ patch fluctuates by about $100\,\mathrm{nm}$, visible in reflection interference microscopy; a tension of only $10^{-6}\,\mathrm{N\,m^{-1}}$ cuts this severalfold, since it replaces $q_{\min}^{-2}$ by about $(\kappa/\sigma)\ln(1 + \sigma/\kappa q_{\min}^2)$. The persistence length of a fluid membrane, over which thermal fluctuations destroy its orientation, is $\xi_{\mathrm{p}} \approx a\exp(4\pi\kappa/3k_{\mathrm{B}}T)$, astronomically large for $\kappa = 20\,k_{\mathrm{B}}T$: biological membranes are flat on all scales unless forces bend them.

**Formula 24.3.2 (Entropic and Elastic Area Strain)** Under tension, the undulations are pulled out and the projected area increases. Summing the excess area $\frac12\sum q^2\langle\lvert h_q\rvert^2\rangle$ over modes, the apparent areal strain of a vesicle relative to a reference tension $\sigma_0$ is

$$
\alpha = \frac{k_{\mathrm{B}}T}{8\pi\kappa}\ln\frac{\sigma}{\sigma_0} + \frac{\sigma}{K_A}
$$
(Helfrich and Servuss 1984; Evans and Rawicz 1990). The logarithmic, entropic term dominates below about $0.5\,\mathrm{mN\,m^{-1}}$ and gives $\kappa$ from the slope of $\ln\sigma$ against $\alpha$, $8\pi\kappa/k_{\mathrm{B}}T$; the linear term dominates above and gives $K_A$.

![Thermal undulations of a fluid membrane (κ = 20 k_BT). A: mean squared amplitude of the Fourier modes (Formula 24.3.1) for tensions from zero to 10⁻⁴ N/m: bending dominates at short wavelengths (slope −4), tension at long wavelengths (slope −2), with the crossover at q_c = (σ/κ)^½. B, C: height fields of a 4 µm × 4 µm patch synthesized from the spectrum with the same random phases at tensions of 10⁻⁷ and 10⁻⁴ N/m: tension suppresses the long-wavelength undulations, from 23 to 3 nm rms. D: tension against apparent area strain in micropipette aspiration (Formula 24.3.2, K_A = 0.24 N/m): at low tension the undulations are pulled out (logarithmic, entropic regime, which gives κ), at high tension the bilayer stretches (which gives K_A) until it ruptures near 10 mN/m](./plots/fluctuations.py)

### 24.3.3. Pulling Tethers

A point force applied to a membrane, by an optical trap holding a bead stuck to it or by motors walking along a microtubule, pulls out a long thin tube rather than deforming the vesicle as a whole. Model a vesicle of radius $R$ under internal excess pressure $\Delta p$ and tension $\sigma = K_A(A - A_0)/A_0$, from which a cylindrical tether of radius $r$ and length $L$ is pulled by a force $f$. With the bending energies of a sphere ($8\pi\kappa$), a cylinder ($\pi\kappa L/r$, from $(2H)^2 = 1/r^2$ over area $2\pi rL$) and a hemispherical end cap ($4\pi\kappa$), the free energy is

$$
G = 12\pi\kappa + \frac{\pi\kappa L}{r} + \frac{K_A}{2}\frac{(A - A_0)^2}{A_0} - \Delta p\left(\frac43\pi R^3 + \pi r^2L\right) - fL, \qquad A = 4\pi R^2 + 2\pi rL.
$$

**Definition 24.3.1 (Membrane Tether)** A **membrane tether** is a thin cylindrical tube of membrane pulled from a vesicle or cell by a localized force, whose radius and force are set by the balance of bending rigidity and membrane tension.

**Formula 24.3.3 (Tether Radius and Force)** Minimizing $G$ with respect to $R$, $r$ and $L$ (using $\partial G_{\mathrm{stretch}}/\partial R = 8\pi R\sigma$, $\partial G_{\mathrm{stretch}}/\partial r = 2\pi L\sigma$, $\partial G_{\mathrm{stretch}}/\partial L = 2\pi r\sigma$) gives the Young–Laplace law $\Delta p = 2\sigma/R$ and, neglecting terms of relative order $r/R$,

$$
r = \sqrt{\frac{\kappa}{2\sigma}}, \qquad f = 2\pi\sqrt{2\kappa\sigma} = \frac{2\pi\kappa}{r}.
$$
The force is independent of the tether length: membrane flows from the vesicle into the tether at constant tension.

**Proof** $\partial G/\partial R = 8\pi R\sigma - 4\pi R^2\Delta p = 0$ gives $\Delta p = 2\sigma/R$. $\partial G/\partial r = -\pi\kappa L/r^2 + 2\pi L\sigma - 2\pi rL\Delta p = 0$; the last term is $2\pi rL\cdot2\sigma/R$, smaller than the second by $2r/R$, and dropping it gives $r^2 = \kappa/2\sigma$. $\partial G/\partial L = \pi\kappa/r + 2\pi r\sigma - \pi r^2\Delta p - f = 0$; dropping the pressure term again, $f = \pi\kappa/r + 2\pi r\sigma = \pi\kappa/r + \pi\kappa/r = 2\pi\kappa/r = 2\pi\sqrt{2\kappa\sigma}$. $\square$

**Example 24.3.2** Tethers pulled from ER and Golgi membranes, or formed by kinesin motors on microtubules in vitro, require about $10\,\mathrm{pN}$ (Koster and colleagues 2003). With $\kappa = 20\,k_{\mathrm{B}}T = 8.2\times10^{-20}\,\mathrm{J}$, the tension is $\sigma = f^2/(8\pi^2\kappa) = 10^{-22}/(6.5\times10^{-18})\,\mathrm{N\,m^{-1}} = 1.5\times10^{-5}\,\mathrm{N\,m^{-1}}$, a thousandth of the lysis tension, and the tether radius $\sqrt{\kappa/2\sigma} = 52\,\mathrm{nm}$, as seen in electron micrographs of ER tubules. A single kinesin, with a stall force of $6\,\mathrm{pN}$, cannot pull a tube; a few motors acting together can, and tubes start abruptly once a threshold number of motors is reached. In cells, tether forces of $10$–$50\,\mathrm{pN}$ report effective tensions of $10^{-5}$–$10^{-4}\,\mathrm{N\,m^{-1}}$ that include the adhesion of the plasma membrane to the cortex ([7.3.4](/7.3.4#sec-4.7.1)).

The tether is also a tool for measuring how proteins respond to curvature. Stepping the tension with the pipette sets the tube radius through $r = \sqrt{\kappa/2\sigma} = f/4\pi\sigma$. Dynamin injected into such an experiment polymerizes into a helix only on tubes thinner than a critical radius of about $10\,\mathrm{nm}$, and, once polymerized, holds the tube by itself, relaxing the force on the bead (Roux and colleagues 2010): curvature sensing and force generation of a fission protein measured in one setup.

## 24.4. Vesicles and Budding

### 24.4.1. The Cost of Vesicles

Cells make vesicles all the time: for endocytosis, for secretion and for traffic between compartments ([7.3.8](/7.3.8), [7.3.10](/7.3.10)). The bending energy of a spherical vesicle, $8\pi\kappa \approx 250$–$500\,k_{\mathrm{B}}T$ for $\kappa = 10$–$20\,k_{\mathrm{B}}T$, is independent of its size, and must be supplied by the proteins and lipids that bud it.

**Example 24.4.1 (A vesicle budget)** A fibroblast internalizes the equivalent of its whole plasma membrane, about $2000\,\mu\mathrm{m^2}$, in about an hour. If the vesicles are $100\,\mathrm{nm}$ in diameter (area $3\times10^4\,\mathrm{nm^2}$, probably an overestimate of their size), that is $6\times10^4$ vesicles per hour, $1000$ per minute. At $500\,k_{\mathrm{B}}T$ each, the bending energy alone is the free energy of about $25$ ATP per vesicle, or $2.5\times10^4$ ATP per minute, a negligible fraction of the ATP turnover of a mammalian cell ($10^7$–$10^9$ per second). The cost of traffic lies not in bending but in the machinery: coat assembly and disassembly (the uncoating ATPase Hsc70 must at least undo the binding energy that drove budding), GTP hydrolysis by Arf, Sar1, Rab and dynamin, and SNARE recycling by NSF.

A synaptic vesicle of $40\,\mathrm{nm}$ diameter has an internal volume of about $2\times10^4\,\mathrm{nm^3}$; with a neurotransmitter such as acetylcholine at the measured $0.1$–$0.5\,\mathrm{M}$ in the lumen, it holds a few thousand molecules, the quantum of synaptic transmission ([7.6.30](/7.6.30)).

### 24.4.2. Making Curvature

The mechanisms by which cells bend membranes, lipid asymmetry, wedging by amphipathic helices, scaffolding by curved proteins such as BAR domains and coats, crowding of proteins on one face, and pulling or pushing by the cytoskeleton, are listed in [7.3.4](/7.3.4#sec-4.7.2). Two physical points are added here. First, sensing and generating curvature are the same interaction seen from two sides: a protein that lowers its energy on a curved membrane will, at high surface density, impose that curvature. At low density BAR proteins accumulate on tethers of matching radius; above a threshold coverage they tubulate flat membranes. Second, a single mechanism rarely supplies enough energy: a scaffold of rigidity much greater than the membrane's must bind with an energy per area exceeding $2\kappa/R^2$ (about $0.04\,k_{\mathrm{B}}T\,\mathrm{nm^{-2}}$ for $R = 30\,\mathrm{nm}$, [7.3.8](/7.3.8#sec-8.2.5)), and the various mechanisms usually act together.

### 24.4.3. Three Models of Budding

Consider a patch of membrane of fixed area $A$ that deforms from a flat disc into a spherical cap of radius $r$ and opening angle $\theta$, with $A = 2\pi r^2(1 - \cos\theta)$; $\theta = 0$ is flat and $\theta = \pi$ a complete bud connected to the membrane by an infinitesimal neck. Gaussian curvature terms are ignored (they change only at scission). The bending energy of the cap with $c_0 = 0$ is $\frac{\kappa}{2}(2/r)^2A = 4\pi\kappa(1 - \cos\theta)$, which increases monotonically from $0$ to $8\pi\kappa$: budding is spontaneous only if another term decreases faster.

**Formula 24.4.1 (Budding of a Domain by Line Tension)** If the patch is a domain of different composition with line tension $\gamma$ along its boundary of radius $a = r\sin\theta$, then

$$
\frac{E(\theta)}{4\pi\kappa} = (1 - \cos\theta) + \lambda\sqrt{\frac{1 + \cos\theta}{2}}, \qquad \lambda = \frac{\gamma}{2\kappa}\sqrt{\frac A\pi}.
$$
The complete bud ($\theta = \pi$, $E = 8\pi\kappa$) has lower energy than the flat domain ($E = 4\pi\kappa\lambda$) when $\lambda > 2$; budding is barrier-free (the energy decreases monotonically with $\theta$) when $\lambda > 4$ (Lipowsky 1992).

**Proof** The line energy is $2\pi a\gamma$ with $a = r\sin\theta$ and $r = \sqrt{A/2\pi(1 - \cos\theta)}$, so $a = \sqrt{A/2\pi}\,\sin\theta/\sqrt{1 - \cos\theta} = \sqrt{A/2\pi}\sqrt{1 + \cos\theta}$, and $2\pi a\gamma/4\pi\kappa = \lambda\sqrt{(1 + \cos\theta)/2}$. In terms of $u = \cos\theta$, $\mathrm{d}(E/4\pi\kappa)/\mathrm{d}u = -1 + \lambda/[4\sqrt{(1 + u)/2}]$; the energy decreases with $\theta$ (increases with $u$) for all $u \in (-1, 1)$ if and only if $\lambda/4 \ge \sqrt{(1 + u)/2}$ for all $u$, that is $\lambda \ge 4$. $\square$

Larger domains need less line tension to bud ($\gamma > 8\kappa\sqrt{\pi/A}$): a domain of $1\,\mu\mathrm{m^2}$ with $\kappa = 20\,k_{\mathrm{B}}T$ buds spontaneously if $\gamma > 8 \times 8.2\times10^{-20}\sqrt{\pi}/10^{-6}\,\mathrm{N} = 1.2\,\mathrm{pN}$, within the range of line tensions measured between $\mathrm{L_o}$ and $\mathrm{L_d}$ domains in giant vesicles ($0.5$–$5\,\mathrm{pN}$), where domains are indeed seen to bud.

**Formula 24.4.2 (Budding by Spontaneous Curvature)** If a coat imposes a spontaneous curvature $c_0$ on the patch, its energy is

$$
E(\theta) = \frac{\kappa}{2}\left(\frac2r - c_0\right)^2A = \frac\kappa2\left[2\sqrt{2\pi(1 - \cos\theta)} - c_0\sqrt A\right]^2,
$$
minimal where $2/r = c_0$, that is at $c_0\sqrt A = 4\sqrt\pi\sin(\theta/2)$. A complete bud forms when $c_0\sqrt A \ge 4\sqrt\pi \approx 7.1$, that is when the coat area equals that of a sphere of radius $2/c_0$; a coat with smaller area forms a shallow cap whose curvature matches $c_0$.

This is the physics of the clathrin-coated pit: its lattice of a well-defined curvature first grows as a shallow cap and becomes a closed bud only when enough coat has been added, which is why flat clathrin lattices and shallow pits accumulate when membrane tension is high (tension adds $\sigma A_{\mathrm{total}}$, which opposes the deformation of the surrounding membrane) and why actin is then recruited to complete the bud.

**Formula 24.4.3 (Wrapping of an Adhesive Particle)** A spherical particle of radius $R$ adhering to the membrane with energy $\mu$ per unit area is wrapped over a cap of area $A(\theta) = 2\pi R^2(1 - \cos\theta)$. With tension $\sigma$ and $c_0 = 0$, and neglecting the deformation of the free membrane near the edge,

$$
E(\theta) = \left(\frac{2\kappa}{R^2} + \sigma - \mu\right)A(\theta),
$$
linear in the wrapped area: the particle stays at the surface if $\mu < \mu^* = 2\kappa/R^2 + \sigma$ and is wrapped completely, without a barrier, if $\mu > \mu^*$ (Deserno 2003 includes the edge, which adds a small barrier and partial wrapping near the threshold).

**Example 24.4.2 (Viruses)** For a virus of radius $50\,\mathrm{nm}$, $\kappa = 20\,k_{\mathrm{B}}T$ and $\sigma = 10^{-5}\,\mathrm{N\,m^{-1}}$ ($0.0024\,k_{\mathrm{B}}T\,\mathrm{nm^{-2}}$), $\mu^* = 2 \times 20/2500 + 0.0024 = 0.018\,k_{\mathrm{B}}T\,\mathrm{nm^{-2}}$: about $2\,k_{\mathrm{B}}T$ per $100\,\mathrm{nm^2}$. A few receptor–ligand bonds of $10$–$20\,k_{\mathrm{B}}T$ each per $100\,\mathrm{nm^2}$ easily exceed this, so receptor binding alone can drive the engulfment of a virus. The threshold scales as $1/R^2$: particles smaller than about $20\,\mathrm{nm}$ need much stronger adhesion, which is one reason why the uptake of nanoparticles by cells is most efficient at diameters of $40$–$60\,\mathrm{nm}$. Enveloped viruses use the same physics in reverse when they bud from the cell, their matrix and envelope proteins supplying adhesion and spontaneous curvature, with ESCRT-III recruited for the final scission.

![Three ways to bud a vesicle (bud: a spherical cap of fixed area with opening angle θ from flat, θ = 0, to a complete bud, θ = π). A: domain with line tension (Formula 24.4.1): for λ = 2 the bud and the flat state have equal energy but are separated by a barrier; for λ ≥ 4 budding is downhill. B: a coat with spontaneous curvature (Formula 24.4.2): the energy minimum moves from flat to a complete bud as c₀√A grows to 4√π. C: wrapping of a particle of radius 50 nm by a membrane with κ = 20 k_BT and tension 10⁻⁵ N/m (Formula 24.4.3): the energy is linear in the wrapped area, so the particle is either not wrapped or wrapped completely, depending on whether the adhesion energy per area is below or above μ* = 2κ/R² + σ](./plots/budding.py)

## 24.5. Fusion and Fission

### 24.5.1. Fusion Through Hemifusion

Fusion merges two membranes into one, and fission splits one into two. Both change the topology of the membrane, and both must pass through intermediates in which the bilayer structure is locally disrupted. The flat bilayer and the closed vesicle are each stable; it is the intermediate that costs energy. Theory (Kozlov and Markin 1983, Chernomordik and Kozlov), simulations and experiments agree on a pathway: close apposition of the two membranes, which requires removing the water and overcoming the hydration repulsion at separations below about $2\,\mathrm{nm}$; a stalk, an hourglass-shaped connection of the two proximal leaflets; its expansion into a hemifusion diaphragm; and the opening of a fusion pore through the diaphragm, which then expands.

**Definition 24.5.1 (Hemifusion)** **Hemifusion** is the intermediate state of membrane fusion in which the proximal (contacting) leaflets of two bilayers have merged through a stalk or a hemifusion diaphragm, so that lipids of these leaflets mix, while the distal leaflets remain separate and the aqueous contents do not mix.

The stalk has strongly negative curvature in its proximal leaflets: lipids with $P > 1$ (PE, diacylglycerol, cholesterol) in the contacting leaflets favor it, while lipids with $P < 1/3$ (lysophosphatidylcholine) inhibit it there but favor pore opening when added to the distal leaflets, a characteristic signature of the stalk pathway used to probe it experimentally. Kinetic analysis of the fusion of small vesicles by polyethylene glycol gave activation energies of about $60\,k_{\mathrm{B}}T$ for stalk formation and about $40\,k_{\mathrm{B}}T$ for pore opening; without proteins, the barriers would make fusion of cellular membranes take far longer than the milliseconds of exocytosis.

The protein machines supply the energy. Zippering of a SNARE complex, from the membrane-distal N-terminal end towards the membranes ([7.1.13](/7.1.13#def-13.2.4), [7.3.8](/7.3.8#sec-8.4.2)), releases about $35\,k_{\mathrm{B}}T$ in the first, N-terminal half and about $65\,k_{\mathrm{B}}T$ in total, as measured by surface-force apparatus, optical and magnetic tweezers; estimates of the total barrier for fusing two bilayers are $100$–$150\,k_{\mathrm{B}}T$, so a few SNARE complexes, cooperating, can drive fusion. Liposome experiments show that one complex suffices for lipid mixing, at least three for efficient content mixing; estimates in cells range from two to eight. The cis-SNARE complex that remains after fusion is extremely stable and is disassembled by the ATPase NSF with its adaptor α-SNAP. Viral fusion proteins, such as influenza hemagglutinin, do the same job in one molecule: a large conformational change, triggered by the low pH of the endosome, inserts fusion peptides into the target membrane and folds back into a hairpin that pulls the two membranes together.

The topology change has its own energy. Fusing two vesicles into one changes the Euler characteristic of the surface from $4$ to $2$, and the Gaussian term of Eq. (24.2) by $2\pi\bar\kappa\Delta\chi = -4\pi\bar\kappa \approx +4\pi\kappa$ for $\bar\kappa \approx -\kappa$, about $250\,k_{\mathrm{B}}T$; the bending energy of the vesicles decreases by $8\pi\kappa$, so the fusion of small vesicles is still downhill overall. Fission of one vesicle into two costs the same Gaussian energy in reverse, and a negative $\bar\kappa$ thus favors fission over fusion.

### 24.5.2. Fission

Fission is not simply fusion backwards: the neck that connects a bud to its parent must first be constricted until the inner leaflets meet (to below about $3\,\mathrm{nm}$ in a clathrin-coated bud), without opening a pore that would let the contents leak. The pathway runs through a hemifission intermediate analogous to the stalk; its energy barrier, estimated at tens of $k_{\mathrm{B}}T$ (a barrier of up to about $40\,k_{\mathrm{B}}T$ allows fission within seconds), falls steeply as the neck narrows, and once hemifission is reached completion is spontaneous. Two machines are known in detail ([7.3.8](/7.3.8#sec-8.2.4), [7.3.10](/7.3.10#sec-10.4.2)). Dynamin polymerizes as a helix around the outside of the neck and, by GTP hydrolysis, constricts and twists it; the tether experiments of 24.3.3 measured its curvature dependence and force. ESCRT-III polymerizes as spirals inside necks that lead away from the cytoplasm (multivesicular body formation, cytokinetic abscission, budding of HIV) and constricts them with the help of the ATPase Vps4. Many fission events in the Golgi and endosomes have no identified machine; there, mechanisms such as line tension at domain boundaries, friction of a pulled tube and insertion of amphipathic helices are thought to suffice.

## 24.6. The Shapes of Organelles and Cells

### 24.6.1. Organelles

Many organelles are far from spherical: the ER is a network of tubules and sheets, the Golgi a stack of flattened cisternae, the inner mitochondrial membrane folded into cristae joined to the boundary membrane by narrow crista junctions. Their membranes contain far more area than the plasma membrane suggests.

**Example 24.6.1 (Membrane area in a mitochondrion)** Model a mitochondrion as a spherocylinder of diameter $0.8\,\mu\mathrm{m}$ and length $1\,\mu\mathrm{m}$ (cylindrical part $0.2\,\mu\mathrm{m}$). Its volume is $\frac43\pi(0.4)^3 + \pi(0.4)^2 \times 0.2 = 0.37\,\mu\mathrm{m^3}$ and its outer membrane area $4\pi(0.4)^2 + 2\pi \times 0.4 \times 0.2 = 2.5\,\mu\mathrm{m^2}$. If the inner membrane forms $15$ disc-shaped cristae of radius $0.4\,\mu\mathrm{m}$, each a flattened sac with two faces, the inner membrane has $2.5 + 2 \times 15 \times \pi(0.4)^2 \approx 17\,\mu\mathrm{m^2}$, seven times the outer. A fibroblast with a few hundred mitochondria therefore has several thousand square micrometers of inner mitochondrial membrane, more than its plasma membrane of about $2000\,\mu\mathrm{m^2}$; with the ER, intracellular membranes exceed the plasma membrane tenfold or more.

The shapes of these membranes are held by proteins rather than by lipid elasticity alone: reticulons and DP1 (Yop1) insert wedge-shaped hairpins that stabilize the high curvature of ER tubules, atlastins fuse tubules into a network, ATP synthase dimers bend the rims of cristae and the MICOS complex holds the crista junctions, whose saddle shape has negative Gaussian curvature. The elastic energies of 24.2 set the forces these proteins must exert; the proteins themselves and their interaction with the bilayer are the subject of [7.6.25](/7.6.25).

### 24.6.2. The Red Blood Cell

The mammalian red cell has no nucleus and no organelles: its shape is the shape of its membrane, a bilayer bound to the spectrin–actin skeleton ([7.3.4](/7.3.4#sec-4.6.4)). The human discocyte is $7.8\,\mu\mathrm{m}$ across, about $2.6\,\mu\mathrm{m}$ thick at the rim and $0.8\,\mu\mathrm{m}$ at the center, with an area of about $135\,\mu\mathrm{m^2}$ and a volume of about $94\,\mathrm{fL}$.

The shape problem is to minimize the Helfrich energy at fixed area $A$ and volume $V$, the two quantities the cell cannot change quickly (its area by the near-inextensibility of the bilayer, its volume by osmotic balance). The constraints reduce to one dimensionless number, the reduced volume $v = V/(\frac43\pi R_0^3)$ with $R_0 = \sqrt{A/4\pi}$: $v = 1$ for a sphere, $v = 0.64$ for the red cell. Minimizing the bending energy alone (with $c_0 = 0$) at $v \approx 0.6$ gives prolate, oblate (discocyte-like) or stomatocyte shapes depending on $v$ (Seifert, Berndl and Lipowsky 1991); spontaneous curvature shifts the boundaries. A model that reproduces the whole sequence of red-cell shapes needs two further ingredients (Lim, Wortis and Mukhopadhyay 2002).

**Definition 24.6.1 (Area-Difference Elasticity)** The **area-difference elasticity** model adds to the Helfrich energy a term

$$
G_{\mathrm{ADE}} = \frac{\alpha\kappa\pi}{2Ad^2}(\Delta A - \Delta A_0)^2, \qquad \Delta A = \mathrm{d}\oint 2H\,\mathrm{d}A,
$$
which penalizes deviations of the difference $\Delta A$ between the areas of the outer and inner leaflets (whose neutral surfaces are a distance $d$ apart) from its relaxed value $\Delta A_0$, set by the numbers of lipids in the two leaflets; $\alpha$ is a dimensionless constant of order one. It interpolates between the spontaneous-curvature model and the bilayer-couple model, in which $\Delta A$ is fixed.

The bilayer-couple hypothesis of Sheetz and Singer (1974) explained a classic observation: amphipathic drugs that insert preferentially into the outer leaflet (anionic ones, repelled by the negatively charged inner leaflet) expand it and turn discocytes into echinocytes, spiculated cells; drugs that enter the inner leaflet produce cup-shaped stomatocytes. With the shear and stretch elasticity of the spectrin skeleton added, the ADE model reproduces the sequence stomatocyte–discocyte–echinocyte as $\Delta A_0$ changes by about $\pm1$–$2\,\%$; the skeleton's elasticity is what stabilizes the spicules of echinocytes and prevents the cell from budding vesicles, which bare vesicles of the same area and volume would do.

![Geometry and bending energy of the human red blood cell. A: the measured biconcave profile (Evans and Fung 1972) with the spheres of equal area (dashed) and equal volume (dotted): area 134 µm², volume 94 fL, reduced volume 0.64; the cell has about 40 % more membrane than a sphere of its volume. B: mean curvature along the upper face computed from the profile: positive in the dimple, negative around the rim; the bending energy of the discocyte is about 1.9 × 8πκ. C: osmotic swelling at constant area (Boyle–van 't Hoff relation with an osmotically inactive fraction of 0.4): the volume rises as the medium is diluted until it reaches the volume of the sphere of the cell's area, near 0.47 % NaCl, where the cell becomes a sphere and lyses](./plots/rbc-shape.py)

The excess area of the discocyte is functional. A red cell must pass through capillaries narrower than itself and through slits of $1$–$2\,\mu\mathrm{m}$ in the spleen; with fixed area and volume, it can deform into a bullet or a parachute only because $v < 1$. A sphere of the same volume would need an area $40\,\%$ smaller, and could not deform at all without stretching its membrane, which ruptures beyond a few percent. This is the reason why spherocytes, which have lost membrane area ([Example 4.6.1](/7.3.4#ex-4.6.1) of 7.3.4), are trapped in the spleen, and why the osmotic fragility test reads area loss: a cell swells in hypotonic saline until it becomes a sphere and then lyses, at a tonicity that rises as the reduced volume increases. With a volume of $94\,\mathrm{fL}$ and an area of $134\,\mu\mathrm{m^2}$ (sphere volume $146\,\mathrm{fL}$), the Boyle–van 't Hoff relation with an osmotically inactive fraction of $0.4$ places lysis near $0.47\,\%$ NaCl, as observed for normal cells ($0.45$–$0.5\,\%$).

## 24.7. Surface Tension in the Lung

The membranes of this chapter have tensions of micronewtons per meter; an air–water interface has a tension of $70\,\mathrm{mN\,m^{-1}}$. The lung, with $70$–$100\,\mathrm{m^2}$ of alveolar surface covered by a thin liquid lining, is the organ in which surface tension matters most. An alveolus of radius $r$ lined by liquid of tension $\gamma$ is held open against the **Laplace pressure** ([6.3.19](/6.3.19#thm-19.2.1))

$$
\Delta p = \frac{2\gamma}{r}, \tag{24.6}
$$
one interface, unlike a soap bubble with two interfaces and $\Delta p = 4\gamma/r$. With $\gamma = 50\,\mathrm{mN\,m^{-1}}$, the tension of plasma, and $r = 100\,\mu\mathrm{m}$, $\Delta p = 1\,\mathrm{kPa}$, a sizable fraction of the pressures the respiratory muscles generate in quiet breathing (about $0.5\,\mathrm{kPa}$).

**Proposition 24.7.1 (Instability of Connected Alveoli)** Two alveoli of radii $r_1 < r_2$ connected through a common airway, lined by a liquid of constant surface tension, are not in stable equilibrium: the smaller has the higher pressure, empties into the larger and collapses. If the tension rises with the alveolar area fast enough that $\gamma(r)/r$ increases with $r$ (for $\gamma \propto r^m$, $m > 1$), equal sizes are stable.

**Proof** Air flows from higher to lower pressure. With constant $\gamma$, $\Delta p_1 = 2\gamma/r_1 > 2\gamma/r_2 = \Delta p_2$, so air leaves the smaller alveolus, which shrinks, which raises its pressure further: positive feedback. If $\mathrm{d}(\gamma/r)/\mathrm{d}r > 0$, a smaller alveolus has the lower pressure and receives air until the sizes equalize: negative feedback. $\square$

**Pulmonary surfactant** ([7.5.30](/7.5.30#def-30.7.2)), secreted by alveolar type II cells, is mainly DPPC with phosphatidylglycerol and the hydrophobic proteins SP-B and SP-C. It spreads as a monolayer at the air–liquid interface. On expiration, as the alveolar area shrinks, the monolayer is compressed, its fluid components are squeezed out into multilayer reservoirs, and a nearly pure, gel-like DPPC film remains whose tension falls to near zero (below $2\,\mathrm{mN\,m^{-1}}$); on inspiration the film expands and the tension rises towards $25\,\mathrm{mN\,m^{-1}}$. The tension thus increases steeply with area, satisfying the stability condition of Proposition 24.7.1, and its low value at small volumes reduces the work of breathing. DPPC is the right lipid for this because its main transition lies above body temperature ([7.6.8](/7.6.8#sec-8.5)): a compressed gel film does not collapse or flow. Premature infants born before surfactant production begins, at about $28$–$32$ weeks, develop neonatal respiratory distress syndrome, in which alveoli collapse at each expiration; instillation of natural or synthetic surfactant into the airways is the treatment.

![Surface tension and the stability of alveoli. A: Laplace pressure 2γ/r against alveolar radius for a constant tension of 50 mN/m (no surfactant), which rises as the alveolus shrinks, and for a lining with pulmonary surfactant whose tension falls on compression (modeled as γ ∝ r⁴, 25 mN/m at 120 µm), for which the pressure falls. B: two alveoli connected through an airway, starting at radii of 95 and 105 µm, exchanging air at a rate proportional to their pressure difference (Proposition 24.7.1): without surfactant the smaller collapses and the larger expands; with surfactant both return to the same radius](./plots/alveoli.py)

## 24.8. Towards Membrane Proteins

Throughout this chapter proteins have entered only as sources of curvature and adhesion. Membrane proteins also feel the bilayer: a protein whose hydrophobic belt does not match the bilayer thickness deforms it over a few nanometers at a cost set by $K_t$ and $\kappa$ (Eq. (24.3)); proteins that change shape when they switch conformations do work against membrane tension; and proteins that deform the bilayer interact through it over distances of several nanometers. These effects turn the elastic moduli measured here into gating energies, most clearly in the mechanosensitive channel MscL, whose opening by tension was introduced as a two-state system in [7.6.4](/7.6.4#sec-4.2) and whose elastic theory is the subject of [7.6.25](/7.6.25).

## Summary

| Topic | Key result | Reference |
|---|---|---|
| Self-assembly | mass action $X_N = N(X_1/X_{\mathrm{c}})^N$; CMC $X_{\mathrm{c}} = \mathrm{e}^{-(\mu_1^\circ - \mu_N^\circ)/k_{\mathrm{B}}T}$; SDS $8\,\mathrm{mM}$, DPPC $0.5\,\mathrm{nM}$ | Eq. (24.1), Proposition 24.1.1 |
| Packing parameter | $P = v/a_0l$: spheres $< 1/3$, cylinders $< 1/2$, bilayers $\le 1$, inverted phases $> 1$ | Definition 24.1.1, Proposition 24.1.2 |
| Polymorphism | $\mathrm{L_\beta}$, $\mathrm{P_{\beta'}}$, $\mathrm{L_\alpha}$, $\mathrm{L_o}$, $\mathrm{H_{II}}$, $\mathrm{Q_{II}}$; $T_{\mathrm{m}}$ rises with chain length and small heads, falls with *cis* double bonds; cholesterol makes $\mathrm{L_o}$ | Definition 24.1.2 |
| Geometry | principal curvatures; $H = (c_1 + c_2)/2$, $K = c_1c_2$; $\oint K\,\mathrm{d}A = 2\pi\chi$ | Definition 24.2.1 |
| Elastic energies | stretch $K_A \approx 0.24\,\mathrm{N\,m^{-1}}$; Helfrich bending $\kappa \approx 20\,k_{\mathrm{B}}T$, $\bar\kappa \approx -\kappa$; thickness $K_t$; $\kappa \approx K_Ad^2/48$; tension | Definitions 24.2.2–24.2.5, Eq. (24.2), Eq. (24.3) |
| Aspiration | $\sigma = \Delta pR_{\mathrm{p}}/2(1 - R_{\mathrm{p}}/R_{\mathrm{v}})$; lysis at $5$–$10\,\mathrm{mN\,m^{-1}}$, a few percent strain | Eq. (24.4), Example 24.3.1 |
| Undulations | $\langle\lvert h_q\rvert^2\rangle = k_{\mathrm{B}}T/A(\kappa q^4 + \sigma q^2)$; entropic and elastic area strain | Formula 24.3.1, Formula 24.3.2 |
| Tethers | $r = \sqrt{\kappa/2\sigma}$, $f = 2\pi\sqrt{2\kappa\sigma}$; $10\,\mathrm{pN}$ ER tethers: $\sigma \approx 10^{-5}\,\mathrm{N\,m^{-1}}$, $r \approx 50\,\mathrm{nm}$ | Formula 24.3.3, Example 24.3.2 |
| Vesicles | $8\pi\kappa$ for any size; 1000 vesicles per minute cost $2.5\times10^4$ ATP-equivalents of bending | Example 24.4.1 |
| Budding | line tension: downhill for $\lambda > 4$; spontaneous curvature: complete for $c_0\sqrt A \ge 4\sqrt\pi$; adhesion: wrap for $\mu > 2\kappa/R^2 + \sigma$ | Formulas 24.4.1–24.4.3, Example 24.4.2 |
| Fusion and fission | stalk, hemifusion, pore; barriers $40$–$150\,k_{\mathrm{B}}T$; SNARE zippering $\approx 65\,k_{\mathrm{B}}T$ per complex; Gaussian term $-4\pi\bar\kappa$ per topology change; dynamin and ESCRT-III | Definition 24.5.1 |
| Organelles | inner mitochondrial membrane several times the outer; intracellular membranes exceed the plasma membrane | Example 24.6.1 |
| Red cell | $A = 134\,\mu\mathrm{m^2}$, $V = 94\,\mathrm{fL}$, $v = 0.64$; ADE and bilayer couple; skeleton shear; lysis near $0.47\,\%$ NaCl | Definition 24.6.1 |
| Lung | $\Delta p = 2\gamma/r$; constant tension unstable; surfactant makes $\gamma$ rise with area | Eq. (24.6), Proposition 24.7.1 |

## Questions

1. The critical micelle concentration of sodium octyl sulfate is $0.13\,\mathrm{M}$ and that of sodium dodecyl sulfate $8.2\,\mathrm{mM}$. Estimate the free-energy gain per $\ce{CH2}$ group on transfer from water into a micelle, and predict the CMC of sodium hexadecyl sulfate.

   **Answer** By Proposition 24.1.1, $\ln X_{\mathrm{c}} = -(\mu_1^\circ - \mu_N^\circ)/k_{\mathrm{B}}T$. Four $\ce{CH2}$ groups lower the CMC by $0.13/0.0082 = 15.9$, so each contributes $\ln(15.9)/4 = 0.69\,k_{\mathrm{B}}T$ (about $1.7\,\mathrm{kJ\,mol^{-1}}$), a factor of $2.0$ per group. For $\mathrm{C_{16}}$: $8.2\,\mathrm{mM}/15.9 = 0.52\,\mathrm{mM}$, as measured. The value per $\ce{CH2}$ is smaller than the free energy of transfer of a $\ce{CH2}$ group from water to a bulk hydrocarbon (about $1.5\,k_{\mathrm{B}}T$) because the charged head groups repel each other and part of each chain remains in contact with water at the micelle surface.

2. Calculate the packing parameter of a phosphatidylcholine with two $\mathrm{C_{16}}$ chains using Tanford's formulas for a saturated chain of $n$ carbons, $v = (27.4 + 26.9n)\times10^{-3}\,\mathrm{nm^3}$ and $l = 0.154 + 0.1265n\,\mathrm{nm}$, and $a_0 = 0.64\,\mathrm{nm^2}$. Which structure does it form? How does $P$ change for the corresponding lysophospholipid with one chain?

   **Answer** One chain: $v = 0.0274 + 0.430 = 0.458\,\mathrm{nm^3}$, $l = 0.154 + 2.024 = 2.18\,\mathrm{nm}$. Two chains: $v = 0.916\,\mathrm{nm^3}$, $P = 0.916/(0.64 \times 2.18) = 0.66$: between $1/2$ and $1$, a bilayer (Proposition 24.1.2). The lysolipid has half the chain volume with a similar head area: $P = 0.33$, at the boundary between spherical and cylindrical micelles; lysophosphatidylcholine is indeed a detergent that dissolves membranes at high concentration.

3. A vesicle of radius $15\,\mu\mathrm{m}$ is aspirated into a pipette of radius $3\,\mu\mathrm{m}$. At $\Delta p = 10\,\mathrm{Pa}$ the projection length is $5.0\,\mu\mathrm{m}$, and at $\Delta p = 1000\,\mathrm{Pa}$ it is $14.0\,\mu\mathrm{m}$. Assuming the high-pressure step is in the elastic regime, estimate $K_A$.

   **Answer** Eq. (24.4): $1 - R_{\mathrm{p}}/R_{\mathrm{v}} = 0.8$; $\sigma = \Delta p \times 3\times10^{-6}/1.6$: $1.9\times10^{-5}$ and $1.9\times10^{-3}\,\mathrm{N\,m^{-1}}$. $\Delta A = 2\pi R_{\mathrm{p}}\Delta l(1 - R_{\mathrm{p}}/R_{\mathrm{v}}) = 2\pi \times 3 \times 9 \times 0.8 = 136\,\mu\mathrm{m^2}$; $A_0 = 4\pi \times 15^2 = 2830\,\mu\mathrm{m^2}$; $\Delta A/A_0 = 4.8\,\%$. Then $K_A \approx \Delta\sigma/(\Delta A/A_0) = 1.9\times10^{-3}/0.048 = 0.04\,\mathrm{N\,m^{-1}}$, six times smaller than the true elastic modulus: most of this area change is entropic (the low tension of the first step leaves undulations to be pulled out, about $\frac{k_{\mathrm{B}}T}{8\pi\kappa}\ln(100) = 0.9\,\%$ for $\kappa = 20\,k_{\mathrm{B}}T$, and probably more for a softer membrane or excess area stored in folds). The assumption fails; one must measure several tensions above about $0.5\,\mathrm{mN\,m^{-1}}$ and fit the slope there.

4. Using Formula 24.3.1, estimate the root-mean-square amplitude of the undulation with wavelength $2\,\mu\mathrm{m}$ of a membrane patch of $10\times10\,\mu\mathrm{m^2}$ with $\kappa = 20\,k_{\mathrm{B}}T$ at $\sigma = 0$ and at $\sigma = 10^{-4}\,\mathrm{N\,m^{-1}}$.

   **Answer** $q = 2\pi/2\,\mu\mathrm{m} = 3.14\times10^6\,\mathrm{m^{-1}}$, $q^4 = 9.7\times10^{25}\,\mathrm{m^{-4}}$, $q^2 = 9.9\times10^{12}\,\mathrm{m^{-2}}$. $\kappa q^4 = 8.2\times10^{-20} \times 9.7\times10^{25} = 8.0\times10^6\,\mathrm{J\,m^{-4}}$; $\sigma q^2 = 10^{-4} \times 9.9\times10^{12} = 9.9\times10^8$. With $A = 10^{-10}\,\mathrm{m^2}$: at $\sigma = 0$, $\langle\lvert h_q\rvert^2\rangle = 4.1\times10^{-21}/(10^{-10} \times 8.0\times10^6) = 5.1\times10^{-18}\,\mathrm{m^2}$, an amplitude of $2.3\,\mathrm{nm}$ per mode (with several modes of this wavelength, a few nanometers); at $\sigma = 10^{-4}\,\mathrm{N\,m^{-1}}$ the denominator is $125$ times larger and the amplitude $0.2\,\mathrm{nm}$. The crossover wavelength $2\pi\sqrt{\kappa/\sigma} = 2\pi \times 29\,\mathrm{nm} = 0.18\,\mu\mathrm{m}$: at this tension all optically visible undulations are tension-dominated.

5. A cell has a plasma membrane tension of $3\times10^{-5}\,\mathrm{N\,m^{-1}}$ and an effective bending rigidity of $20\,k_{\mathrm{B}}T$. What force is needed to pull a tether, and what is its radius? If the tension doubles after osmotic swelling, how do they change?

   **Answer** $f = 2\pi\sqrt{2\kappa\sigma} = 2\pi\sqrt{2 \times 8.2\times10^{-20} \times 3\times10^{-5}}\,\mathrm{N} = 2\pi \times 2.2\times10^{-12}\,\mathrm{N} = 14\,\mathrm{pN}$; $r = \sqrt{\kappa/2\sigma} = \sqrt{8.2\times10^{-20}/6\times10^{-5}}\,\mathrm{m} = 37\,\mathrm{nm}$. Doubling $\sigma$ multiplies $f$ by $\sqrt2$ (to $20\,\mathrm{pN}$) and divides $r$ by $\sqrt2$ (to $26\,\mathrm{nm}$). Tether force measurements in this way monitor tension changes during spreading, swelling and migration.

6. Show that for the line-tension model (Formula 24.4.1) the bud has lower energy than the flat domain for $\lambda > 2$, and find the opening angle of the energy maximum (the barrier) for $\lambda = 3$.

   **Answer** $E(\pi)/4\pi\kappa = 2$ and $E(0)/4\pi\kappa = \lambda$, so the bud is lower for $\lambda > 2$. With $u = \cos\theta$, $f(u) = 1 - u + \lambda\sqrt{(1 + u)/2}$; $f'(u) = -1 + \lambda/(4\sqrt{(1 + u)/2}) = 0$ at $\sqrt{(1 + u)/2} = \lambda/4 = 0.75$, $u = 2 \times 0.5625 - 1 = 0.125$, $\theta = 83^\circ$. There $f = 0.875 + 3 \times 0.75 = 3.125$, a barrier of $0.125 \times 4\pi\kappa = 31\,k_{\mathrm{B}}T$ above the flat state for $\kappa = 20\,k_{\mathrm{B}}T$: large enough to keep domains with $\lambda = 3$ flat for a long time. Barriers vanish at $\lambda = 4$.

7. Why must a spherical vesicle of DOPC swell in a hypotonic solution only by a few percent of its area before rupturing, while a red blood cell can increase its volume by more than half? Calculate the volume increase that brings a discocyte with $A = 134\,\mu\mathrm{m^2}$ and $V = 94\,\mathrm{fL}$ to a sphere.

   **Answer** A spherical vesicle already encloses the maximal volume for its area; any swelling must stretch the bilayer, which ruptures at $2$–$5\,\%$ areal strain (a volume increase of $1.5$ times that, $3$–$8\,\%$). The red cell has a reduced volume of $0.64$: it can increase its volume at constant area until it becomes a sphere of $V = \frac43\pi(A/4\pi)^{3/2} = \frac43\pi(3.27\,\mu\mathrm{m})^3 = 146\,\mathrm{fL}$, an increase of $55\,\%$, before any stretching is needed. The biconcave shape is thus an osmotic safety margin as well as a reserve of deformability.

8. In respiratory distress syndrome, the surface tension of the alveolar lining remains near $50\,\mathrm{mN\,m^{-1}}$ even at small volumes. Compute the pressure needed to reopen a collapsed alveolus of radius $30\,\mu\mathrm{m}$ and compare it with that needed to hold open one of $100\,\mu\mathrm{m}$ with surfactant at $5\,\mathrm{mN\,m^{-1}}$.

   **Answer** Eq. (24.6): $2 \times 0.05/30\times10^{-6} = 3.3\,\mathrm{kPa}$ (about $34\,\mathrm{cm}$ of water) to reopen the small alveolus, against $2 \times 0.005/10^{-4} = 0.1\,\mathrm{kPa}$ for the normal one: a thirtyfold difference, and more than an infant's respiratory muscles can generate at every breath. This is why affected infants struggle to breathe, why their lungs are stiff, and why surfactant replacement or continuous positive airway pressure, which keeps alveoli from collapsing, is effective.

9. (Experimental design) You want to test whether a protein you have purified senses membrane curvature, generates it, or both. Design experiments with giant vesicles and tethers.

   **Answer** Sensing: pull a tether from a giant vesicle containing a fluorescent lipid, add the labeled protein at low concentration, and measure the ratio of protein to lipid fluorescence on the tether relative to the vesicle while stepping the tension (and hence the tether radius $r = \sqrt{\kappa/2\sigma}$); enrichment that increases as $r$ decreases indicates curvature sensing, and a sharp dependence identifies a preferred curvature. Generation: at higher concentrations, measure the tether force at fixed tension (a protein that imposes curvature changes $f$, Formula 24.3.3 with a spontaneous curvature, and can even hold the tube without force, as dynamin does), and observe whether the protein tubulates or buds flat membranes of giant vesicles or supported bilayers spontaneously. Controls: inert proteins of similar size (to exclude crowding effects on the membrane), lipid compositions with and without the protein's binding lipid (for example PI(4,5)P₂), and mutants of the putative curved or amphipathic domain.

10. (Open question) Membranes of cells have bending rigidities of $10$–$50\,k_{\mathrm{B}}T$. Discuss what would change for cells if bilayers were ten times stiffer, or ten times softer.

    **Answer** Ten times stiffer ($\kappa \approx 200\,k_{\mathrm{B}}T$): each vesicle would cost $5000\,k_{\mathrm{B}}T$, beyond what coat binding of reasonable strength could supply at physiological tensions, so small transport vesicles and tubules ($r \approx 30$–$50\,\mathrm{nm}$) would be energetically prohibitive; tether forces would triple ($\propto\sqrt\kappa$), making motor-driven tubulation of ER harder; fluctuations would be suppressed, slowing processes that rely on thermal deformation such as the initiation of fusion; and the curvature-induced sorting of proteins and lipids would change. Ten times softer ($\kappa \approx 2\,k_{\mathrm{B}}T$): thermal fluctuations would crumple the membrane on micrometer scales (the persistence length $\exp(4\pi\kappa/3k_{\mathrm{B}}T)$ would be only a few times molecular size), vesicles would form spontaneously and membranes would fragment, compartments would be unstable and vesicular traffic would lose its control. The value of $\kappa$, set by the thickness of a bilayer of two $\mathrm{C_{16}}$–$\mathrm{C_{18}}$ chains ($\kappa \approx K_Ad^2/48$), sits in the range where proteins can shape membranes with a few $k_{\mathrm{B}}T$ per molecule while thermal motion alone cannot.
