---
title: Cell Adhesion and Cell Sorting
description: "How cells that adhere selectively build tissues: reaggregation and sorting experiments, the thermodynamics of differential adhesion (tissue surface tension, the conditions for mixing, separation and engulfment, transitivity), site models and Bell's receptor–ligand kinetics, measurement of tissue surface tension, kinetic models of sorting, Smoluchowski coagulation and continuum adhesion models (Cahn–Hilliard), sorting in monolayers, the sol–gel transition of matrix networks, and epithelial–mesenchymal transitions."
---

Embryos are not only patterned; they are built. Before cells can move as sheets in gastrulation (7.5.9) or condense into somites (7.5.23), they must stick to some neighbours more than to others, and this selective adhesion has a striking consequence: cells taken out of their tissues and mixed at random find their way back into tissue-like arrangements. This chapter treats that self-organization quantitatively. The **differential adhesion hypothesis** was introduced in [7.3.23](/7.3.23#def-23.3.4) together with **cadherins** and the **cellular Potts model**; here we derive its consequences (when two tissues mix, separate or engulf one another, and when the engulfment hierarchy is transitive), connect it to molecular binding through site models and Bell's receptor–ligand kinetics, describe how tissue surface tension is measured, and ask how cells actually reach the predicted configurations (kinetic sorting rules, coagulation equations, continuum models). The chapter ends with the matrix that cells adhere to, treated as a random network that can gel, and with the epithelial–mesenchymal transitions that switch cells between cohesive sheets and migratory mesenchyme. The mechanics of the resulting tissue flows is the subject of 7.5.8.

## 7.1. Reaggregation and Sorting Out

The experiments that started the subject were made on sponges. H. V. Wilson (1907) pressed sponges through fine silk cloth: the dissociated cells crawled together, formed clumps, and the clumps reorganized into small functional sponges. When cells of two species were mixed, they largely segregated by species, a selectivity later traced to species-specific aggregation factors (large proteoglycan complexes). Whether the cells move by directed migration (for example, chemotaxis) or by random motion with selective sticking cannot be told from the final result alone; the distinction matters for the models of 7.6 and 7.7.

Johannes Holtfreter extended the approach to amphibian embryos in the 1940s, dissociating tissues by raising the pH of the medium and letting the cells reaggregate at normal pH. Townes and Holtfreter (1955) showed that mixed aggregates do not stay mixed: the cells sort out into an arrangement that resembles the embryo (Figure 1A). Presumptive epidermis moves to the outside, neural plate cells move inside and form vesicles reminiscent of a neural tube; mesoderm mixed with endoderm and ectoderm ends up between them. Two conclusions follow. First, the cells retain tissue-specific surface properties after dissociation: the arrangement is regenerated from a random start, so it is not a memory of the embryonic path. Second, the affinities change with stage: in the early amphibian gastrula, ectoderm sorts inside mesoderm, and a fragment of mesoderm spreads over a fragment of ectoderm (as mesoderm spreads on the inner face of the blastocoel roof), while early endoderm and ectoderm fuse only transiently and then separate until a narrow bridge joins them. By the neurula, epidermis ends up outside mesoderm.

**Definition 7.1.1 (Cell Sorting)** *Cell sorting* (sorting out) is the spontaneous segregation of a random mixture of two or more cell types into domains of single type, with a reproducible arrangement of the domains (which type is inside, which outside).

Malcolm Steinberg (1962–1970) turned these observations into a test. He used tissues of chick embryos (dissociated with trypsin) and compared two kinds of starting configuration: a random mixture of the two cell types, and two intact fragments pressed together (Figure 1B), or threaded on a glass fibre so that they could not drift apart (the "shish kebab" experiment, Figure 1C). Both starts led to the same end state: one tissue spreads over the other and envelops it.

**Definition 7.1.2 (Engulfment)** Tissue $B$ *engulfs* (envelops) tissue $A$, written $B \succ A$, if in the end state of a mixed aggregate or of two fragments in contact $B$ covers $A$ completely; $B$ engulfs $A$ partially if it covers only part of the surface of $A$.

The inference from "same end state from different starts" is the key step of the argument. A configuration reached from opposite initial conditions behaves like an equilibrium of a system with a potential: the path does not matter, only the final minimum. Steinberg found moreover that engulfment was transitive: if $C \succ B$ and $B \succ A$ then $C \succ A$. A transitive order is exactly what one expects if each tissue is characterized by a single number, as a liquid is by its surface tension, and the tissue with the larger number goes inside. Measured tissue surface tensions (7.5) bear this out: for chick tissues the order inside → outside is limb bud mesoderm, pigmented retinal epithelium, heart ventricle, liver, neural retina.

![Three classical sorting experiments. A: dissociation and reaggregation (Townes and Holtfreter 1955): presumptive epidermis (blue) and neural plate (orange) of an amphibian neurula are dissociated, mixed and reaggregated; within hours the mixed aggregate sorts out with epidermis outside and neural tissue inside. B: fusion of two intact fragments (Steinberg): the less cohesive tissue (liver, yellow) spreads over the more cohesive one (limb bud mesoderm, red) and envelops it, the same end state as from a mixture. C: the "shish kebab" variant, with the two aggregates threaded on a glass fibre](./plots/reaggregation-experiments.py)

Sorting also occurs in normal development, though it is rarely the only mechanism. In the mouse blastocyst, epiblast and primitive endoderm precursors are first specified in a salt-and-pepper pattern in the inner cell mass and then sort into two layers (7.5.5); neural crest cells change cadherin expression as they leave the neural tube and as they condense into ganglia ([7.3.23](/7.3.23#sec-23.3.2), 7.5.20); and the boundary between notochord and paraxial mesoderm forms where cadherin adhesion is reduced and actomyosin cables accumulate (7.5).

## 7.2. The Thermodynamics of Differential Adhesion

We now make the liquid analogy precise, following Steinberg's formulation as developed by Percus and Childress. Consider cell types $A, B, \dots$ of equal size and shape in a medium $\mathrm{O}$ to which they do not adhere. Let $E_{ij}$ be the adhesive energy released per unit area of contact between a cell of type $i$ and one of type $j$ (so a large $E_{ij}$ is strong adhesion), with $E_{i\mathrm{O}} = 0$.

Exchange an interior $A$ cell of a pure $A$ region with an interior $B$ cell of a pure $B$ region, and count unit contacts. The exchange replaces one $A$–$A$ and one $B$–$B$ contact by two $A$–$B$ contacts, so the adhesive energy changes by

$$
\Delta E_{\mathrm{ad}} = 2E_{AB} - E_{AA} - E_{BB}.
$$
If $\Delta E_{\mathrm{ad}} \ge 0$, exchanges continue until $A$–$B$ contacts are maximized: the types intermix. If $\Delta E_{\mathrm{ad}} < 0$, like cells gather with like: the types sort out.

**Definition 7.2.1 (Tissue Surface Tension)** The **tissue surface tension** $\gamma_{A\mathrm{O}}$ of a tissue $A$ is the work needed to increase the free surface of the tissue (its interface with the medium) by unit area, at mechanical equilibrium and slowly enough that no energy is dissipated; the interfacial tension $\gamma_{AB}$ between two tissues is the corresponding work per unit area of $A$–$B$ interface.

To relate the tensions to the adhesive energies, stretch a sheet of $A$ tissue (thicker than one cell) slowly by an area $\Delta X$ on each face. The free surface grows by $2\Delta X$, and $\Delta X$ worth of $A$–$A$ contact must be broken: $2\gamma_{A\mathrm{O}}\Delta X = E_{AA}\Delta X$. Extending an $A$–$B$ interface by $\Delta X$ breaks $\Delta X/2$ of $A$–$A$ and of $B$–$B$ contact and forms $\Delta X$ of $A$–$B$ contact. Hence

$$
\gamma_{A\mathrm{O}} = \tfrac12 E_{AA}, \qquad
\gamma_{AB} = \tfrac12\bigl(E_{AA} + E_{BB}\bigr) - E_{AB} = \gamma_{A\mathrm{O}} + \gamma_{B\mathrm{O}} - E_{AB}.
\tag{7.1}
$$
These are the relations of the physical chemistry of liquids: $E_{AA} = 2\gamma_{A\mathrm{O}}$ is the **work of cohesion** of tissue $A$ and Eq. (7.1) is the Dupré relation for the **work of adhesion** $E_{AB}$ ([6.3.19](/6.3.19#def-19.6.2)). The sorting criterion $\Delta E_{\mathrm{ad}} < 0$ is $\gamma_{AB} > 0$.

When the types sort ($\gamma_{AB} > 0$) and the cells are small compared with the aggregates, the problem becomes one of coalescing liquid drops. As for soap bubbles, the interfaces are spherical caps (constant mean curvature, by the **Young–Laplace equation**), and where the three interfaces $A$–$\mathrm{O}$, $B$–$\mathrm{O}$, $A$–$B$ meet, the three tension vectors must balance: they form a closed triangle, the Neumann triangle. Such a triangle exists only if each tension is smaller than the sum of the other two. When one tension reaches the sum of the others, the corresponding interface disappears from the equilibrium.

**Theorem 7.2.1 (Configurations of Two Tissues)** Suppose $E_{AA} \ge E_{BB}$. Then a mixed aggregate of $A$ and $B$ cells reaches one of four states:

| Condition | State |
|---|---|
| $E_{AB} > \frac12(E_{AA} + E_{BB})$ | the cells intermix |
| $E_{BB} \le E_{AB} \le \frac12(E_{AA} + E_{BB})$ | $B$ engulfs $A$ completely |
| $0 < E_{AB} < E_{BB}$ | $B$ engulfs $A$ partially |
| $E_{AB} \le 0$ | the two tissues separate |

**Proof** The first line is the criterion $\gamma_{AB} < 0$. Otherwise the tissues form two drops. Complete engulfment of $A$ by $B$ means that the $A$–$\mathrm{O}$ interface is absent at equilibrium, which happens when replacing it by an $A$–$B$ plus a $B$–$\mathrm{O}$ interface lowers the energy: $\gamma_{A\mathrm{O}} \ge \gamma_{AB} + \gamma_{B\mathrm{O}}$, that is, by Eq. (7.1), $\tfrac12 E_{AA} \ge \tfrac12 E_{AA} + E_{BB} - E_{AB}$, or $E_{AB} \ge E_{BB}$. Separation means that the $A$–$B$ interface is absent: $\gamma_{AB} \ge \gamma_{A\mathrm{O}} + \gamma_{B\mathrm{O}}$, or $E_{AB} \le 0$. The reverse engulfment of $B$ by $A$ would need $E_{AB} \ge E_{AA}$, which together with $E_{AA} \ge E_{BB}$ contradicts $\gamma_{AB} > 0$. In the remaining case all three triangle inequalities hold strictly, the Neumann triangle exists, and the drops meet along a contact circle at finite angles: partial engulfment. $\square$

The theorem refines the qualitative statement found in many textbooks ("sorting if $A$–$A$ adhesion exceeds $A$–$B$ and $B$–$B$"): what matters is the comparison of $E_{AB}$ with the *mean* of the homotypic adhesions (for sorting) and with the weaker of them (for complete engulfment). Figure 2 shows the four regions and computed equilibrium shapes. Two further points deserve notice. The cohesive tissue always goes inside, so in a hierarchy of complete engulfment the inner tissues are the ones with high surface tension. And after complete engulfment the surface energy does not depend on where the inner drop sits: differential adhesion alone implies no centring, and Steinberg indeed observed eccentric inner masses.

![Equilibrium configurations of two tissues predicted by differential adhesion. A: regions in the plane of the adhesive energies E_BB/E_AA and E_AB/E_AA (tissue A more cohesive): mixing above the line E_AB = (E_AA + E_BB)/2, complete engulfment of A by B between it and the line E_AB = E_BB, partial engulfment for 0 < E_AB < E_BB, separation for E_AB ≤ 0 (Theorem 7.2.1). B: computed equilibrium shapes of two equal volumes of A (red) and B (blue) for E_BB/E_AA = 0.5 (the dots in A): for E_AB/E_AA = 0.02, 0.15, 0.3 and 0.45 the shapes minimize the total interfacial energy over three spherical caps meeting on a contact circle, and B covers more and more of A; at E_AB/E_AA = 0.6 the engulfment is complete (the position of the inner drop is not fixed by surface energy); at 0.9 the cells mix](./plots/two-tissue-configurations.py)

By Theorem 7.2.1, $B \succ A$ (complete engulfment) holds if and only if

$$
\tfrac12\bigl(E_{AA} + E_{BB}\bigr) > E_{AB} \ge E_{BB}.
\tag{7.2}
$$

**Proposition 7.2.2 (When Engulfment Is Transitive)** If $C \succ B$ and $B \succ A$, then $E_{AA} > E_{BB} > E_{CC}$. The relations $C \succ B$ and $B \succ A$ do not, however, imply $C \succ A$: transitivity holds only within a set of cell types of which every pair shows complete engulfment.

**Proof** From Eq. (7.2), $0 < \frac12(E_{AA} + E_{BB}) - E_{AB} \le \frac12(E_{AA} + E_{BB}) - E_{BB} = \frac12(E_{AA} - E_{BB})$, so $E_{AA} > E_{BB}$; likewise $E_{BB} > E_{CC}$. Finally, $C \succ B$ and $B \succ A$ give $E_{AA} > E_{CC}$, but they say nothing about $E_{AC}$, which may lie anywhere; if $A$ and $C$ are known to show complete engulfment at all, the order $E_{AA} > E_{CC}$ forces $C \succ A$. $\square$

The experimental transitivity of Steinberg's hierarchies is therefore not automatic. It suggests that heterotypic adhesion is tied to homotypic adhesion in a regular way, which is the subject of the site models of 7.3.

For aggregates of finitely many cells, let $N_i$ be the number of $i$-cells, $S_i$ the surface area of one $i$-cell, $N_{ij} = N_{ji}$ the number of $i$–$j$ contacts and $S_{ij}$ the area of one such contact. The adhesive energy is $E_{\mathrm{ad}} = \sum_{i \ge j} N_{ij}S_{ij}E_{ij}$, and the surface of each type is shared out among its contacts: $N_iS_i = 2N_{ii}S_{ii} + \sum_{j \ne i} N_{ij}S_{ij}$ (contacts with the medium included as $j = \mathrm{O}$).

**Formula 7.2.1 (Adhesive Energy and Surface Potential)** Eliminating $N_{ii}S_{ii}$ with the area balance gives

$$
E_{\mathrm{ad}} = K - \sum_{i > j} N_{ij}S_{ij}\gamma_{ij}, \qquad K = \tfrac12\sum_i N_iS_iE_{ii}, \qquad \gamma_{ij} = \tfrac12\bigl(E_{ii} + E_{jj}\bigr) - E_{ij},
$$
where $K$ does not depend on the arrangement. Maximizing adhesion is therefore the same as minimizing the surface potential $V_{\mathrm{s}} = \sum_{i>j} N_{ij}S_{ij}\gamma_{ij} = \sum_{i>j}\int_{I_{ij}}\gamma_{ij}\,\mathrm{d}S$, the total interfacial energy of the interfaces $I_{ij}$. This is the energy that the cellular Potts model samples ([Algorithm 23.3.1](/7.3.23#alg-23.3.1)).

A configuration in which $E_{\mathrm{ad}}$ cannot be increased by any small deformation need not be optimal. Two separate inclusions of $A$ inside a $B$ aggregate are locally stable when $B \succ A$: merging them would lower the surface potential, but no small change of shape does so; the inclusions must interact over a distance. Kinetic arguments (7.6) are needed to say which of the many local minima is reached.

## 7.3. Site Models of Adhesion

Theory becomes much simpler, and testable, if the heterotypic energy $E_{AB}$ can be predicted from properties of $A$ and $B$ separately. Steinberg proposed that adhesion is mediated by sites of one kind, present on all cell types at different densities.

If the sites are sparse with densities $\eta_i$ and each contact energy is proportional to the chance that two sites meet, $E_{ij} = k\eta_i\eta_j$. Then

$$
\gamma_{ij} = \tfrac{k}{2}\bigl(\eta_i - \eta_j\bigr)^2 > 0, \qquad
\tfrac12\bigl(E_{AA} + E_{BB}\bigr) > \sqrt{E_{AA}E_{BB}} = E_{AB} > E_{BB} \quad (\eta_A > \eta_B),
$$
so any two types sort, the one with more sites is completely engulfed, and engulfment is transitive. The surface potential is minimized for many types by an "onion": nested layers, all interfaces spherical though not necessarily concentric, ordered from the highest site density inside to the lowest outside.

**Definition 7.3.1 (Floating-Site Model)** In the **floating-site model** (Percus and Childress) each cell type $A$ carries sites of density $N_A$ per unit area with energy $k_A$ per site, all sites on the sparser of two apposed membranes are used, and a bond between sites of types $A$ and $B$ releases $k_A + k_B$:

$$
E_{AA} = 2k_AN_A, \qquad E_{AB} = \bigl(k_A + k_B\bigr)\min\bigl(N_A, N_B\bigr),
$$
so that $\gamma_{AB} = k_A(N_A - N_B)$ if $N_A > N_B$ and $\gamma_{AB} = k_B(N_B - N_A)$ if $N_B > N_A$.

The sparse-site rule requires one universal energy per site and gives transitivity; surprisingly, the floating-site rule gives transitivity for any assignment of site energies.

**Theorem 7.3.1 (Unconditional Transitivity)** In the floating-site model, $C \succ B$ and $B \succ A$ imply $C \succ A$, whatever the $k_i$ and $N_i$.

**Proof** Since $\gamma \ge 0$ always, $B \succ A$ means $E_{AA} \ge E_{BB}$ and $E_{AB} \ge E_{BB}$, that is, $k_AN_A \ge k_BN_B$ and $(k_A + k_B)\min(N_A, N_B) \ge 2k_BN_B$; similarly for $C \succ B$. We must show $k_AN_A \ge k_CN_C$, which is immediate, and $(k_A + k_C)\min(N_A, N_C) \ge 2k_CN_C$.

First, $k_A \ge k_B$: if $N_B \le N_A$ the hypothesis reads $(k_A + k_B)N_B \ge 2k_BN_B$; if $N_B \ge N_A$, then $2k_BN_B \le (k_A + k_B)N_A \le (k_A + k_B)N_B$. In the same way $k_B \ge k_C$. If $N_A \ge N_C$, then $(k_A + k_C)N_C \ge 2k_CN_C$ and we are done, so let $N_A < N_C$. Three orders remain.

(i) $N_A \le N_B \le N_C$: the hypotheses are $(k_A + k_B)N_A \ge 2k_BN_B$ and $(k_B + k_C)N_B \ge 2k_CN_C$. Adding them, $k_AN_A + k_BN_A - k_BN_B + k_CN_B \ge 2k_CN_C$, and therefore $(k_A + k_C)N_A \ge 2k_CN_C + (k_B - k_C)(N_B - N_A) \ge 2k_CN_C$.

(ii) $N_B \le N_A \le N_C$: $2k_CN_C \le (k_B + k_C)N_B \le (k_A + k_C)N_A$, since $k_A \ge k_B$ and $N_A \ge N_B$.

(iii) $N_A \le N_C \le N_B$: from $(k_A + k_B)N_A \ge 2k_BN_B$,
$(k_A + k_C)N_A \ge 2k_BN_B - k_BN_A + k_CN_A = 2k_CN_C + (k_B - k_C)(2N_B - N_A) + 2k_C(N_B - N_C) \ge 2k_CN_C$.

In every case $(k_A + k_C)\min(N_A, N_C) \ge 2k_CN_C$. $\square$

For a continuum of cell types with nearly equal site energies $k$, the floating-site tension between neighbouring types is $\gamma \approx k\lvert\Delta N\rvert$: it is a difference of a single function of cell type, $\mathrm{d}\phi = k\,\mathrm{d}N$. This "volume potential" $\phi$ is what a continuum theory of layered tissue needs (7.5.8, §8.6), and the sparse-site model, whose tension $\frac{k}{2}(\Delta\eta)^2$ is not a difference, does not provide it.

The two models also differ in a measurable way. The tension of a tissue against the medium is $\gamma_{A\mathrm{O}} = \frac12E_{AA}$, which is quadratic in site density for sparse sites ($\frac k2\eta_A^2$) and linear for floating sites ($k_AN_A$). Foty and Steinberg (2005) varied the number of cadherin molecules per cell in otherwise identical cell lines and found aggregate surface tension *linearly* proportional to cadherin number, consistent with the saturating rule and not with the product rule. Section 7.4 shows how both rules arise as limits of one binding model.

## 7.4. Receptor–Ligand Binding Between Membranes

Adhesion molecules such as cadherins and integrins diffuse in the plane of the membrane. George Bell (1978) treated bond formation between two apposed membranes as a two-step reaction: diffusion brings a receptor $R$ and a ligand $L$ within an encounter distance $\Delta$ to form a complex $C$, which then becomes a bond $B$:

$$
\ce{R + L <=>[d_+][d_-] C <=>[\rho_+][\rho_-] B}.
$$
With $r, \ell, c, b$ the surface densities (number per unit area),

$$
\frac{\mathrm{d}r}{\mathrm{d}t} = \frac{\mathrm{d}\ell}{\mathrm{d}t} = -d_+r\ell + d_-c, \qquad
\frac{\mathrm{d}c}{\mathrm{d}t} = d_+r\ell - (d_- + \rho_+)c + \rho_-b, \qquad
\frac{\mathrm{d}b}{\mathrm{d}t} = \rho_+c - \rho_-b.
$$
Since $r\ell$ is a product of two areal densities, $d_+$ has the dimension of area per time, that of a diffusion coefficient, and $d_-$ that of a diffusion coefficient per area. If the diffusion coefficients $D_R, D_L$ and the encounter distance are the only parameters, $d_+$ must be $D_R + D_L$ times a function of $D_RD_L/(D_R + D_L)^2$, and $d_-$ must be $(D_R + D_L)\Delta^{-2}$ times such a function; Bell's calculation gives $d_+ = 2\pi(D_R + D_L)$ and $d_- = 2(D_R + D_L)\Delta^{-2}$.

When the encounter complex is rare and short-lived, $\mathrm{d}c/\mathrm{d}t \approx 0$ (the quasi-steady-state approximation used for Michaelis–Menten kinetics, [7.1](/7.1)), and the scheme reduces to $\ce{R + L <=>[k_+][k_-] B}$ with

$$
k_+ = \frac{d_+\rho_+}{d_- + \rho_+}, \qquad k_- = \frac{d_-\rho_-}{d_- + \rho_+}, \qquad
\frac{\mathrm{d}b}{\mathrm{d}t} = k_+(r_0 - b)(\ell_0 - b) - k_-b,
$$
where $r_0 = r + b$ and $\ell_0 = \ell + b$ are the densities before bonding (with $c$ neglected). Bonds form fastest when the membranes first meet, at the rate $k_+r_0\ell_0$.

**Proposition 7.4.1 (Equilibrium Bond Density)** With the two-dimensional affinity $K = k_+/k_-$, the stable equilibrium is

$$
b_{\mathrm{eq}}(r_0, \ell_0) = \frac12\Bigl[\Bigl(r_0 + \ell_0 + \frac1K\Bigr) - \sqrt{\Bigl(r_0 + \ell_0 + \frac1K\Bigr)^2 - 4r_0\ell_0}\Bigr].
$$
For $K(r_0 + \ell_0) \ll 1$, $b_{\mathrm{eq}} \approx Kr_0\ell_0$ (the product rule of sparse sites); for $K(r_0 + \ell_0) \gg 1$, $b_{\mathrm{eq}} \approx \min(r_0, \ell_0)$ (the saturation rule of floating sites).

**Proof** Setting $\mathrm{d}b/\mathrm{d}t = 0$ gives $b^2 - (r_0 + \ell_0 + 1/K)b + r_0\ell_0 = 0$, whose smaller root is the formula (the larger root exceeds $\min(r_0, \ell_0)$ and is not admissible). For small $K$ expand the square root: $\sqrt{s^2 - 4r_0\ell_0} \approx s - 2r_0\ell_0/s$ with $s \approx 1/K$, so $b \approx r_0\ell_0K$. For large $K$, $s \to r_0 + \ell_0$ and the root tends to $\frac12(r_0 + \ell_0 - \lvert r_0 - \ell_0\rvert) = \min(r_0, \ell_0)$. $\square$

Take the adhesive energy of a contact to be proportional to its bond density, and let cell types differ in their site densities $r_0$ and $\ell_0$ (each cell carrying sites that can bind sites of the partner). The interfacial tension between the two types is then, from Eq. (7.1) in units of the bond energy,

$$
2K\gamma_{r\ell} = \sqrt{(1 + Kr_0 + K\ell_0)^2 - 4K^2r_0\ell_0} - \tfrac12\sqrt{1 + 4Kr_0} - \tfrac12\sqrt{1 + 4K\ell_0}.
$$
It is never negative: with $\rho = \frac12\sqrt{1 + 4Kr_0}$ and $\lambda = \frac12\sqrt{1 + 4K\ell_0}$, the radicand equals $(\rho + \lambda)^2 + (\rho - \lambda)^2 + (\rho^2 - \lambda^2)^2 \ge (\rho + \lambda)^2$, so $2K\gamma_{r\ell} \ge 0$. Cells that differ only in the amount of one adhesion molecule therefore always sort, as Steinberg and Takeichi (1994) found with cell lines expressing different levels of P-cadherin. Whether $\gamma$ behaves as a difference of a volume potential, $\Delta\phi \approx \lvert\Delta N\rvert$ between types of site densities $N$ and $N + \Delta N$, depends on the regime: expanding the formula shows this requires $\sqrt{KN} \ll K\lvert\Delta N\rvert$ in addition to $\lvert\Delta N\rvert \ll N$, i.e. very high affinity (Figure 4B).

![Bell's receptor–ligand model. A: equilibrium bond density b_eq (Proposition 7.4.1) against the two-dimensional affinity K for receptor and ligand densities r0 = 1 and l0 = 0.4 (arbitrary units); dashed, the low-affinity limit K r0 l0 (product rule of sparse sites); dotted, the high-affinity limit min(r0, l0) (floating sites). B: interfacial tension between two cell types with site densities N and n, normalized by its value at n = 0, against n/N for K N = 0.01, 1, 100 and 10^4: the parabola (1 − n/N)² of the product rule turns, at very high affinity, into the straight line 1 − n/N of the saturation rule, the form needed for a volume potential](./plots/bell-binding.py)

Other bonding schemes are easily added: both membranes may carry both receptor and ligand (two independent contributions to $b_{\mathrm{eq}}$); bivalent ligands may bridge receptors on the same or on adjacent membranes, with monovalent ligands competing for receptors; or bridges may be formed enzymatically. Each defines a reaction scheme whose equilibrium can be computed in the same way. What such calculations do not give is the energy per bond, and the additive energies assumed in site models are only an ansatz. Modern measurements of cadherins show why: a single cadherin trans dimer has a low affinity (micromolar or weaker), adhesion strength comes from clustering of many bonds into junctions and from their link to the actin cortex, and the cortex itself contributes to the tension of each interface (7.5).

## 7.5. Molecular Basis and Measurement

The adhesion molecules that make sorting tissue-specific are mainly classical cadherins ([7.3.23](/7.3.23#sec-23.3.1)). The experimental logic runs through a series of gain-of-function and dose experiments. Mouse L fibroblasts, which express no cadherin and adhere poorly, become cohesive when transfected with a cadherin gene, and cells expressing different cadherins (E, P, N) sort from each other (Nose, Nagafuchi and Takeichi 1988): cadherin type is sufficient for selectivity. Cells expressing the same cadherin at different levels also sort, the high expressers inside (Steinberg and Takeichi 1994): amount alone is sufficient, as the site models predict. Cells expressing R- or B-cadherin at equal levels form two mounds with a single shared boundary (Duguay, Foty and Steinberg 2003), the partial-engulfment state of Theorem 7.2.1 with a weak heterotypic bond. In embryos, cells destined for the neural tube switch from E- to N-cadherin; if epidermis is made to express N-cadherin, or N-cadherin is removed from the neural plate, the neural tube fails to separate cleanly from the surface ectoderm. N-cadherin also appears transiently in limb mesenchyme just before it condenses into cartilage nodules, and blocking antibodies prevent condensation. A cadherin binds its partner through its extracellular domains but adheres stably only when its cytoplasmic tail is linked through catenins to actin: in *Xenopus* blastulas, E-cadherin lacking the cytoplasmic domain weakens adhesion and the ectoderm comes apart during gastrulation.

If tissues behave as liquids, a tension can be measured as for a drop. In the parallel-plate method (Foty, Forgacs, Pfleger and Steinberg 1994) a spherical aggregate is compressed between two plates; it first responds elastically, then flows, and after some hours reaches a new equilibrium shape. At equilibrium, the force on the plate is balanced by the Laplace pressure of the curved free surface.

**Formula 7.5.1 (Parallel-Plate Compression)** With $F$ the force on the plate, $R_3$ the radius of the contact disc, $R_1$ the radius of curvature of the free profile in a meridional plane and $R_2$ the equatorial radius,

$$
\frac{F}{\pi R_3^2} = \gamma\Bigl(\frac1{R_1} + \frac1{R_2}\Bigr).
$$

The test of liquid-like behaviour is internal: the same $\gamma$ must be obtained at different compressions, and it is. The measured values for chick tissues (Foty et al. 1996) range from about $1.6\,\mathrm{mN\,m^{-1}}$ for neural retina to $20\,\mathrm{mN\,m^{-1}}$ for limb bud mesoderm, and their order predicts the sorting order of every pair tested (Figure 3). The same agreement was found for the germ layers of the amphibian gastrula (Davis et al. 1997). Aggregate surface tension increases linearly with the number of cadherins per cell (Foty and Steinberg 2005).

![Tissue surface tension. A: parallel-plate compression: at mechanical equilibrium the force F on the plate balances the Laplace pressure of the free surface, F/(π R3²) = γ(1/R1 + 1/R2), with R3 the radius of the contact disc, R1 the meridional radius of curvature of the profile and R2 the equatorial radius (Formula 7.5.1). B: surface tensions of chick embryonic tissue aggregates measured in this way (Foty et al. 1996) and the observed sorting order: in each pair the tissue of higher tension ends up inside, enveloped by the tissue below it in the chart](./plots/tissue-surface-tension.py)

The interpretation of $\gamma$ as adhesion alone has been revised. Cells are bounded by a contractile actomyosin cortex (7.5.8, §8.9), and the tension of a cell–cell contact is the cortical tension on both sides of the contact minus the adhesion energy, $\gamma_{\mathrm{cc}} = 2\sigma_{\mathrm{c}} - \omega$, where $\sigma_{\mathrm{c}}$ is the cortical tension at the contact and $\omega$ the adhesion energy per area. Adhesion molecules also signal to the cortex to relax at contacts. Measurements on zebrafish germ-layer progenitors (Krieg et al. 2008; Maître et al. 2012) showed that differences in cortical tension, regulated by cadherin adhesion, contribute more to sorting than adhesion energy itself, and that cadherin's main mechanical role is to couple the cortices of neighbouring cells (the differential interfacial tension hypothesis). The boundary between notochord and paraxial mesoderm in *Xenopus* is an example: C-cadherin is reduced and actomyosin cables accumulate along the boundary, raising its tension (Fagotto et al. 2013). None of this changes the thermodynamic results of 7.2, which only require that each interface has a tension; it changes what the tensions mean molecularly. The force balance at the edge of a contact between two equal cells (free cortical tension $\sigma_{\mathrm{f}}$, contact tension $\gamma_{\mathrm{cc}}$) gives $\gamma_{\mathrm{cc}} = 2\sigma_{\mathrm{f}}\cos\theta$, where $\theta$ is the angle between each free surface and the plane of the contact at its rim; measuring $\theta$ in cell doublets is how these tensions are compared.

Wolpert's caution applies to all such in vitro experiments: they reveal the adhesive properties of tissues in isolation, not where a tissue will be in the embryo, because in the embryo tissues also adhere to matrix and to other tissues and are constrained by earlier development.

## 7.6. The Kinetics of Sorting

Thermodynamics tells where a system can end, not how it gets there or whether it gets there at all. The kinetic question can be studied on a lattice, treating each cell as a square that may exchange places with its neighbours, and asking which local rules reproduce the observed sequence of states.

Antonelli, Rogers and Willard (1973) let neighbouring cells exchange whenever the exchange does not decrease $E_{\mathrm{ad}}$. Such a deterministic local rule only partially sorts the cells: after a while every remaining move leaves $E_{\mathrm{ad}}$ unchanged, and convoluted clusters of $A$ remain trapped among $B$ (Figure 5A). The missing ingredient is long-range interaction. It could come from chemotaxis (7.5.13) or from random collisions, but there is a simpler source: tissue is nearly incompressible, so a local rearrangement creates a pressure field that moves cells far away. In a lattice rule this corresponds to allowing an $A$ cell to become $B$ while a distant $B$ cell becomes $A$.

**Algorithm 7.6.1 (Goel–Rogers Sorting)** (Goel and Rogers 1978) Cells occupy a square lattice; cell types $1, \dots, M$ have adhesive energies $E_{ij}$; $D$ is the range of interaction and $K_1, \dots, K_D$ are weights.

1. For each cell $i$ compute $E_i = \sum_{j=1}^{D}\sum_{k=1}^{8j}K_jE_{ijk}$, where $E_{ijk}$ is the adhesion of cell $i$ with the $k$-th of the $8j$ cells of the $j$-th square ring around it.
2. Consider only cells within distance $D$ of a cell of another type, i.e. near an interface $I_{AB}$. For each such $A$ cell compute the increment $\Delta E_i$ of $E_i$ if it became a $B$ cell, and for each $B$ cell the increment if it became $A$.
3. Sort the $A \to B$ list and the $B \to A$ list in decreasing order of $\Delta E_i$, add the lists entry by entry, and carry out the paired conversions whose sum is positive (each pair is an exchange of an $A$ and a $B$ cell, possibly far apart along the interface).
4. Treat the interfaces in decreasing order of their tension $\gamma_{ij}$, and repeat.

**Example 7.6.1** Take $D = K_1 = 1$, $E_{AA} = 3$, $E_{BB} = 2$, $E_{AB} = 1$. An $A$ cell with $N_{AA}$ $A$-neighbours and $N_{AB}$ $B$-neighbours (among its eight) that becomes $B$ changes its energy by

$$
\Delta E = (N_{AA} - N_{AB})E_{AB} + N_{AB}E_{BB} - N_{AA}E_{AA}.
$$
For $N_{AA} = 7$, $N_{AB} = 1$ this is $6 + 2 - 21 = -13$; such a cell on a flat interface will not move. A $B$ cell with seven $A$ neighbours that becomes $A$ gains $7(3 - 1) + 1\cdot(1 - 2) = 13$, so the pair can be exchanged with net gain $0$ and the move is not made, while a $B$ cell surrounded by more $A$ cells would be. The lists favour the conversion of cells that protrude into the other type: the rule smooths interfaces as a surface tension does.

Goel and Rogers reproduced the rounding of a square clump, engulfment with an eccentric inner mass ($D = 1$), engulfment with a centred inner mass and coalescence of nearby clusters ($D = 3$), and the sequential engulfment in a three-fragment shish kebab. The rules are not a fluid model, however: increasing $D$ enhances both rounding and centring, and only rounding is a property of liquids (7.2). Their realism was in any case limited by the square cells.

![Kinetics of sorting on a lattice. Each site of a 40 × 40 lattice holds an A cell (red), a B cell (blue) or medium; the initial disk is a random 50:50 mixture; adhesive energies per contact E_AA = 4, E_BB = 1, E_AB = 1.5 (eight neighbours), so the cells should sort with B engulfing A. A: the start; rule 1, neighbouring cells exchange only if the exchange does not decrease the adhesion: sorting stops after a few tens of sweeps with convoluted clusters; rule 2, exchanges that lose adhesion dE are also accepted with probability exp(dE/T), T = 0.7: coarsening continues but slowly; rule 3, as rule 2 with half of the attempts exchanging an A and a B cell anywhere in the aggregate (long-range rearrangement): A ends up inside, enveloped by B, after 3000 sweeps. B: fraction of the contacts of A cells that are with B cells](./plots/sorting-kinetics.py)

Two developments made lattice models realistic. One is finite temperature: accepting unfavourable moves with probability $\mathrm{e}^{\Delta E/T}$ (the **Metropolis algorithm**, [3.5.9](/3.5.9)) lets the system leave local minima, as membrane fluctuations do in real cells (Figure 5, rule 2). The other is to give cells shape. In the cellular Potts model ([Algorithm 23.3.1](/7.3.23#alg-23.3.1); Graner and Glazier 1992) each cell is a domain of many lattice sites held near a target area, and moves are copies of single sites across cell boundaries; with the interfacial tensions of Formula 7.2.1 it reproduces sorting and engulfment and, with extra terms, chemotaxis, growth and division. In the Voronoi model of Sulsky, Childress and Percus (1984), cells are the regions of a **Voronoi diagram** of moving points ("nuclei"): each cell consists of the points closer to its nucleus than to any other, and as the nuclei move, boundaries shift and contacts break and form. It gives reasonable polygonal cell shapes but no realistic membranes. Subcellular models (each cell a cluster of subcells, the boundary subcells playing the membrane) and the vertex models of 7.5.8 (§8.10) are the current tools. All of them remain caricatures of the cell, which deforms, extends protrusions, breaks and forms contacts and moves actively; a satisfactory model of cell deformation and motility within aggregates does not yet exist.

## 7.7. Aggregation and Condensation

Reaggregation itself, before any sorting, is a coagulation process: single cells form pairs, $k$-cell clusters meet $l$-cell clusters to form $(k + l)$-cell clusters, and so on. Treat all cells as equivalent and let $p_k(t)$ be the number of $k$-cell clusters divided by the total number of cells.

**Definition 7.7.1 (Smoluchowski Coagulation Equation)** With a collision kernel $f(k, l) = f(l, k)$ giving the rate at which a $k$-cluster and an $l$-cluster merge, the **Smoluchowski coagulation equation** is

$$
\frac{\mathrm{d}p_k}{\mathrm{d}t} = \frac12\sum_{l=1}^{k-1}f(k - l, l)\,p_{k-l}\,p_l - p_k\sum_{l=1}^{\infty}f(k, l)\,p_l, \qquad k = 1, 2, \dots
\tag{7.3}
$$
The first sum counts mergers that produce a $k$-cluster (the factor $\frac12$ avoids counting each pair twice), the second those that consume one. Multiplying by $k$ and summing, the two sums cancel: $\sum_k k\,\dot p_k = 0$, so $\sum_k kp_k = 1$ (cells are conserved).

The kernel encodes the mechanism. If every cell of one cluster attracts every cell of the other (through a soluble mediator, for example), $f \propto kl$; if only surface cells interact, $f \propto (kl)^{2/3}$; if clusters capture each other at a fixed rate, independent of size, as when sponge cells make contact by long filopodia that then shorten, $f$ is constant.

**Theorem 7.7.1 (Constant Kernel)** For $f \equiv 1$ (after scaling time) and single cells at $t = 0$,

$$
p_k(t) = \frac{4}{(2 + t)^2}\Bigl(\frac{t}{2 + t}\Bigr)^{k-1}, \qquad k \ge 1.
$$

**Proof** Let $G(x, t) = \sum_{k \ge 1}p_k(t)x^k$, the generating function of the cluster sizes (cf. the **probability generating function**, [3.1.11](/3.1.11)); $G(x, 0) = x$ and $\partial_xG(1, t) = 1$. Multiplying Eq. (7.3) by $x^k$ and summing, the convolution becomes a square:

$$
\frac{\partial G}{\partial t} = \frac12G(x, t)^2 - G(x, t)\,G(1, t).
$$
At $x = 1$, $\dot G(1, t) = -\frac12G(1, t)^2$ with $G(1, 0) = 1$, so $G(1, t) = 2/(2 + t)$: this is the number of clusters per cell. Then $\dot G = \frac12G^2 - \frac{2}{2 + t}G$, a Bernoulli equation; for $H = 1/G$ it becomes $\dot H - \frac{2}{2 + t}H = -\frac12$, with solution $H = \frac{2 + t}{2} + a(x)(2 + t)^2$. From $H(x, 0) = 1/x$, $a(x) = \frac{1}{4x} - \frac14$. Hence

$$
G(x, t) = \frac{4x/(2 + t)^2}{1 - xt/(2 + t)},
$$
and expanding the geometric series in $x$ gives the coefficients $p_k$. $\square$

The size distribution is geometric at every time, the number of clusters falls as $2/(2 + t)$ and the mean cluster size grows linearly, as $1 + t/2$. Percus and Childress noted that this kernel, rather than the size-dependent ones, best matches the cluster statistics of sponge reaggregation. The kernels differ qualitatively. For the product kernel $f = kl$ the weight-average cluster size $\sum_kk^2p_k$ obeys $\mathrm{d}S/\mathrm{d}t = S^2$ and diverges at $t = 1$: in finite time a cluster containing a finite fraction of all cells appears, a gelation transition like that of 7.9 (Figure 6B). In a finite population this is a giant aggregate.

![Reaggregation as coagulation. A: constant kernel: lines, the exact solution p_k = 4t^(k−1)/(2 + t)^(k+1) of the Smoluchowski equation (Theorem 7.7.1) for clusters of k = 1 to 4 cells; dots, a stochastic simulation of 3000 cells in which every pair of clusters merges at the same rate. B: weight-average cluster size S = Σ k² p_k from stochastic simulations for the constant kernel (exact 1 + t), the surface kernel (kl)^(2/3) and the product kernel kl, whose S diverges at the gel point t = 1 (exact 1/(1 − t), dashed)](./plots/coagulation.py)

When cells are numerous, describe them by a density $n(\boldsymbol{r}, t)$ obeying a conservation law $\partial_tn + \nabla\cdot\boldsymbol{j} = 0$. Cell motion is overdamped: inertia is negligible (7.5.8, §8.5), so a force $\boldsymbol{f}$ on a cell produces a velocity $\boldsymbol{f}/\zeta$, $\zeta$ a friction coefficient, rather than an acceleration. Adding random motility with diffusion coefficient $D$,

$$
\frac{\partial n}{\partial t} = \nabla\cdot\Bigl[D\nabla n - \frac{1}{\zeta}n\boldsymbol{f}\Bigr].
$$
Four models of the force are useful.

1. Pairwise adhesion: with an intercellular potential $\varphi(\boldsymbol{r})$, $\boldsymbol{f}(\boldsymbol{r}) = -\int n(\boldsymbol{r}')\nabla\varphi(\boldsymbol{r} - \boldsymbol{r}')\,\mathrm{d}\boldsymbol{r}'$. For an adhesive trap of depth $\varphi_0$ and range $a$, $\varphi(\boldsymbol{r}) = -\varphi_0(a - \lvert\boldsymbol{r}\rvert)$ for $\lvert\boldsymbol{r}\rvert < a$ and $0$ beyond, the force pulls each cell towards the neighbours within reach:
   $$
   \frac{\partial n}{\partial t} = \nabla\cdot\Bigl[D\nabla n - \frac{\varphi_0}{\zeta}\,n\int_{\lvert\boldsymbol{r}'\rvert \le a}n(\boldsymbol{r} + \boldsymbol{r}')\,\hat{\boldsymbol{r}}'\,\mathrm{d}\boldsymbol{r}'\Bigr].
   $$
   Numerically, a nearly uniform density breaks up into sharper and sharper condensations.
2. Crowding: cells cannot overlap: replacing $n$ in the drift term by $n(1 - n/n_{\max})$ keeps the density below close packing $n_{\max}$. The condensations then become aggregates of finite density, which coarsen slowly (Figure 7); with two cell types the same model sorts them (Armstrong, Painter and Sherratt 2006).
3. Free energy and the Cahn–Hilliard equation: if the cells are near local equilibrium with a free energy $F[n]$, the force is the gradient of the chemical potential $\mu = \delta F/\delta n$ (the functional derivative), $\boldsymbol{f} = -\nabla\mu$. For the van der Waals form $F[n] = \int\bigl[\phi(n) + \frac b2\lvert\nabla n\rvert^2\bigr]\mathrm{d}\boldsymbol{r}$, $\mu = \phi'(n) - b\nabla^2n$.
4. Gradient flow without conservation: postulating instead $\partial_tn = -\Gamma\,\delta F/\delta n$ gives $\partial_tn = -\Gamma\phi'(n) + \Gamma b\nabla^2n$, which looks like a reaction–diffusion equation; it does not conserve cells and is appropriate for a non-conserved order parameter, such as the fraction of cells in one state.

**Definition 7.7.2 (Cahn–Hilliard Equation)** The **Cahn–Hilliard equation** is the conserved gradient flow of a free energy with a gradient penalty,

$$
\frac{\partial n}{\partial t} = \nabla\cdot\Bigl[M(n)\,\nabla\bigl(\phi'(n) - b\nabla^2n\bigr)\Bigr],
$$
with mobility $M(n) = n/\zeta$ here (a constant in the original theory of phase separation in alloys). The non-conserved flow of model 4 is the *Allen–Cahn equation*.

**Proposition 7.7.2 (Free Energy Decreases)** Along solutions of either equation (with no flux through the boundary), $\mathrm{d}F/\mathrm{d}t \le 0$, with equality only at equilibria.

**Proof** By the chain rule, $\frac{\mathrm{d}F}{\mathrm{d}t} = \int\mu\,\partial_tn\,\mathrm{d}\boldsymbol{r}$. For Cahn–Hilliard, integrating by parts, $\int\mu\nabla\cdot(M\nabla\mu)\,\mathrm{d}\boldsymbol{r} = -\int M\lvert\nabla\mu\rvert^2\mathrm{d}\boldsymbol{r} \le 0$, zero only if $\mu$ is constant. For Allen–Cahn, $\int\mu(-\Gamma\mu)\,\mathrm{d}\boldsymbol{r} = -\Gamma\int\mu^2\,\mathrm{d}\boldsymbol{r} \le 0$. $\square$

$F$ is a **Lyapunov function** ([2.4.11](/2.4.11#sec-11.4)) and the dynamics carries out the minimization that the static theory of 7.2 assumed. A uniform density $n_0$ is unstable when $\phi''(n_0) < 0$, that is, when the effective diffusion coefficient $D + n_0\phi''(n_0)/\zeta$ of the linearized equation is negative (the ideal-mixing part of $\phi$ gives the $D$; adhesion makes $\phi$ concave): the cells undergo **spinodal decomposition**, and the gradient term $b$ sets the scale of the first aggregates. For the trap model with crowding, the same linearization gives the growth rate of Figure 7C.

![Condensation of cells by adhesion in a continuum model with crowding (one dimension, periodic). The density u (u = 1 is close packing) moves by diffusion (D = 1) and by adhesive drift towards neighbours within range R = 1, reduced by the crowding factor 1 − u; mean density 0.3, adhesion strength α = 12. A: kymograph: the uniform state breaks up within t ≈ 2 into aggregates near close packing, which later merge and coarsen. B: density profiles at t = 2, 6 and 25. C: growth rate of a perturbation exp(ikx) of the uniform state, s(k) = −Dk² + 2αu0(1 − u0)(1 − cos kR)/R, for α = 4 (stable) and α = 12 (unstable)](./plots/adhesion-continuum.py)

## 7.8. Sorting in Monolayers

Embryonic cells spread on a flat substrate and form monolayers, which allow sorting to be watched cell by cell. Cells with access to free substrate ruffle and extend pseudopods; cells surrounded by other cells tend to stop moving (**contact inhibition** of locomotion). That cells spread into a monolayer instead of rounding up already shows that their adhesion to the substrate is strong.

Strong substrate adhesion reverses the predictions of 7.2. Treat the substrate as a further "cell type" $S$ with an adhesion to every cell type that exceeds all cell–cell adhesions. In a monolayer each cell has two faces that matter, the free top surface and the face bonded to the substrate, and the surface energy of the island is dominated by the substrate contact, whose tension acts in the opposite sense to the free-surface tension. If, in three dimensions, $C \succ B \succ A$, then in a monolayer the order of engulfment is reversed: $A$ surrounds $B$ and $B$ surrounds $C$. Steinberg and Garrod (1975) observed exactly this with chick cells: in three-dimensional aggregates liver engulfs limb bud mesoderm, but in monolayers islands of liver are surrounded by limb bud cells, which are also the flatter cells after sorting. A continuum model of the monolayer predicts that islands shrink as far as possible; their rounding depends on the weak cell–cell contacts around their edges, and indeed rounding is not prominent in monolayer sorting. The same reversal of the sign of the surface stress, by strong adhesion to an underlying substrate, appears at the dorsal lip of the amphibian blastopore (7.5.9).

## 7.9. The Extracellular Matrix as a Network

Cells adhere not only to each other but to the **extracellular matrix**, whose components (collagens, proteoglycans, **fibronectin**, laminin and the **basal lamina**) and receptors (**integrins**, binding the RGD motif of fibronectin) were described in [7.3.23](/7.3.23#sec-23.2). In development the matrix does three things. It is a substrate and a track: in *Xenopus* gastrulation, mesoderm migrates on a fibronectin network secreted by the blastocoel roof, and precardiac mesoderm in the chick migrates to the midline on fibronectin, so that injected anti-fibronectin antibodies give two separate hearts (cardia bifida; 7.5.28). It presents signals: heparan sulfate proteoglycans bind and concentrate paracrine factors of the FGF, Wnt, Hedgehog and BMP families, and mutations in proteoglycan synthesis disturb migration and patterning in *Drosophila*, *C. elegans* and mice. And it instructs differentiation: chondrocytes survive only when attached to matrix through integrins (detached epithelial cells die by anoikis), and mammary epithelial cells stop dividing and express milk protein genes only on a basal lamina.

The matrix is assembled from molecules with a fixed number of binding sites, which raises a question that adhesion theory also faces: when does a population of binding units form a connected network? Percus and Childress treat a minimal case.

**Definition 7.9.1 (Sol–Gel Transition)** A population of molecules that bind each other through a fixed number of sites forms a sol when all connected clusters are finite and a gel when a cluster spanning the system (an infinite network) exists. The *sol–gel transition* is the change from one to the other as the probability of bonding increases.

Take bivalent molecules $A$ that bind only trivalent molecules $B$, and vice versa, with excess $A$ and $B$ at concentrations $[\ce{A}]$, $[\ce{B}]$. A free site of a $B$ binds an $A$ with probability $p = k[\ce{A}]/(1 + k[\ce{A}])$ (from the equilibrium of $\ce{A + X <=> X'}$ with constant $k$), and a free end of an $A$ binds a $B$ with probability $p' = k'[\ce{B}]/(1 + k'[\ce{B}])$; write $q = 1 - p$, $q' = 1 - p'$. Assume that clusters are trees: as in the theory of Flory and Stockmayer, loops are neglected, which is reasonable early in network growth because sites inside a cluster are geometrically hard to reach.

The cluster composition is encoded by generating functions in marker variables $A$ and $B$. Let $Q_s(A, B)$ be the generating function of the subtrees of depth $s$ hanging from a bond to an internal $A$ (which has one free end), and $R_s(A, B)$ that for an internal $B$ (two free sites). Each free end of $A$ is empty with probability $q'$ or carries a $B$-subtree with probability $p'$, and so on:

$$
Q_s = A\bigl(q' + p'R_{s-1}\bigr), \qquad R_s = B\bigl(q + pQ_{s-1}\bigr)^2, \qquad
R_\infty = B\bigl[q + pA\bigl(q' + p'R_\infty\bigr)\bigr]^2.
$$
A tree grown from an $A$ molecule, with its two free ends, has the generating function $G_A(A, B) = A\bigl(q' + p'R_\infty\bigr)^2$. In the sol, $G_A(1, 1) = R_\infty(1, 1) = 1$.

**Theorem 7.9.1 (Gel Point)** The mean number of $A$ molecules in the tree grown from an $A$ molecule is

$$
\langle n_A\rangle = 1 + \frac{4pp'}{1 - 2pp'},
$$
which diverges at the gel point $2pp' = 1$. More generally, if $\eta_A$ and $\eta_B$ are the mean numbers of new molecules added per molecule of each kind per generation ($\eta_A = 2p$: the two free sites of a $B$ each binding an $A$; $\eta_B = p'$), the gel point is $\eta_A\eta_B = 1$.

**Proof** $\langle n_A\rangle = \partial_AG_A(1, 1)$. Differentiating the fixed-point equation for $R_\infty$ with respect to $A$ at $A = B = R_\infty = 1$ (where $q + p = q' + p' = 1$) gives $\partial_AR_\infty = 2\bigl(p + pp'\,\partial_AR_\infty\bigr)$, so $\partial_AR_\infty = 2p/(1 - 2pp')$. Then $\partial_AG_A = 1 + 2p'\,\partial_AR_\infty = 1 + 4pp'/(1 - 2pp')$. Equivalently, the tree is a branching process in which each $A$ produces on average $\eta_A\eta_B = 2pp'$ $A$-descendants two generations later, and the expected total size of a branching process is finite exactly when the mean offspring number is below 1 (7.5.36). $\square$

Beyond the gel point the generating function has a second fixed point: the probability $f_A$ that the subtree behind a bond to an $A$ is finite satisfies $f_A = q' + p'f_B$, $f_B = (q + pf_A)^2$, and the fraction of $A$ molecules in the infinite network is $1 - f_A^2$, which rises continuously from zero at the gel point (Figure 8). Gelation by such percolation is the reason matrix gels form abruptly once concentrations of the components cross a threshold, and the coagulation of 7.7 with the product kernel is its kinetic counterpart. Real matrices have more site types, loops and enzymatic cross-linking, but the threshold behaviour persists.

![The sol–gel transition of a matrix network. A: a tree of bivalent A molecules (rods) and trivalent B molecules (Y-nodes, here round) grown from a central A; dashed stubs are free sites. B: mean number of A molecules in a tree grown from an A, ⟨n_A⟩ = 1 + 4pp′/(1 − 2pp′), for p = p′ (line; dots: Monte Carlo trees), diverging at the gel point 2pp′ = 1; right axis, the gel fraction, the probability that an A molecule belongs to the infinite network (Theorem 7.9.1)](./plots/sol-gel.py)

## 7.10. Epithelial–Mesenchymal Transitions

Animal tissues come in two architectures. An epithelium is a sheet of polarized cells joined by adherens and tight junctions and resting on a basal lamina; it moves as a unit. A mesenchyme is a loose population of cells embedded in matrix, connected by thin processes and gap junctions, each cell an independent unit of behaviour. The first morphogenetic event in most embryos is the formation of an epithelium, and much of later morphogenesis consists of switching between the two states.

In the **epithelial–mesenchymal transition** ([7.3.23](/7.3.23#sec-23.3.1)) paracrine signals (TGF-β family members, Wnt, FGF) activate transcription factors of the Snail/Slug, Twist and Zeb families, which repress E-cadherin and other epithelial genes; cells lose apical–basal polarity, dismantle their junctions, reorganize the actin cytoskeleton, express mesenchymal markers (N-cadherin, vimentin), secrete matrix metalloproteinases that open the basal lamina, and migrate (Figure 9). In the language of 7.2, EMT lowers cohesion with the epithelium and raises adhesion to matrix, so the cell's preferred neighbour changes from its sister cells to the substrate. Developmental examples are the ingression of primary mesenchyme cells in the sea urchin (7.5.6, 7.5.9), the delamination of mesoderm in *Drosophila* after ventral furrow formation, the passage of epiblast cells through the primitive streak in chick and mouse (7.5.9), the emigration of **neural crest** cells from the dorsal neural tube (7.5.20) and the formation of sclerotome from the ventral somite (7.5.23). In adults EMT occurs in wound healing and, pathologically, in the invasion and metastasis of carcinomas, which reactivate the embryonic programme. EMT is often partial: cells may lose apical–basal polarity but keep some junctions and migrate collectively.

**Definition 7.10.1 (Mesenchymal–Epithelial Transition)** The **mesenchymal–epithelial transition** (MET) is the reverse change, in which mesenchymal cells acquire apical–basal polarity and form junctions and a basal lamina, condensing into an epithelium.

The presomitic mesoderm condenses into epithelial somites (7.5.23), the metanephric mesenchyme forms the epithelial renal vesicle that becomes the nephron (7.5.25), and somites in turn undergo EMT again as sclerotome and muscle precursors leave them: cells may cross the boundary between the two architectures several times in one lineage.

![Epithelial–mesenchymal transition. Left: an epithelium of polarized columnar cells joined near their apical ends by E-cadherin adherens junctions (pink) and resting on a basal lamina. Middle: during EMT, Snail/Slug, Twist and Zeb repress E-cadherin; a cell loses apical–basal polarity and leaves the sheet through a gap in the basal lamina opened by matrix metalloproteinases (MMPs). Right: mesenchymal cells, loosely connected, with protrusions, migrating through a fibronectin-rich matrix (N-cadherin, vimentin). The reverse change (MET, dashed arrow) forms somites and the renal vesicle](./plots/emt.py)

## Summary

| Topic | Key results |
|---|---|
| Sorting experiments (7.1) | Holtfreter, Townes–Holtfreter: dissociated cells sort into embryo-like arrangements (Definition 7.1.1); Steinberg: same end state from mixtures and from fused fragments, transitive engulfment hierarchies (Definition 7.1.2) |
| Thermodynamics (7.2) | $\gamma_{A\mathrm{O}} = E_{AA}/2$, $\gamma_{AB} = (E_{AA}+E_{BB})/2 - E_{AB}$ (Eq. (7.1), Definition 7.2.1); mixing, complete or partial engulfment, separation (Theorem 7.2.1); transitivity not automatic (Proposition 7.2.2); $E_{\mathrm{ad}} = K - \sum N_{ij}S_{ij}\gamma_{ij}$ (Formula 7.2.1); local minima |
| Site models (7.3) | sparse sites $E_{ij} = k\eta_i\eta_j$: onion, transitive; floating sites (Definition 7.3.1): unconditionally transitive (Theorem 7.3.1), $\gamma = k\lvert\Delta N\rvert$, volume potential $\mathrm{d}\phi = k\,\mathrm{d}N$; linear γ–cadherin data favour saturation |
| Bell kinetics (7.4) | $d_+ = 2\pi(D_R + D_L)$, $d_- = 2(D_R + D_L)/\Delta^2$; $b_{\mathrm{eq}}$ from product ($K r_0\ell_0$) to minimum rule (Proposition 7.4.1); $\gamma_{r\ell} \ge 0$ |
| Measurement (7.5) | parallel-plate compression (Formula 7.5.1); tensions 1.6–20 mN/m predict sorting order; γ ∝ cadherin number; cortical tension and differential interfacial tension, $\gamma_{\mathrm{cc}} = 2\sigma_{\mathrm{f}}\cos\theta$ |
| Kinetics (7.6) | local exchange rules stall; long-range moves (Goel–Rogers, Algorithm 7.6.1, Example 7.6.1), fluctuations (Metropolis), cell shape (cellular Potts, Voronoi, vertex models) |
| Aggregation (7.7) | Smoluchowski equation (Definition 7.7.1); constant kernel $p_k = 4t^{k-1}/(2+t)^{k+1}$ (Theorem 7.7.1); product kernel gels at $t = 1$; adhesive drift with crowding; Cahn–Hilliard (Definition 7.7.2) and Allen–Cahn as gradient flows (Proposition 7.7.2) |
| Monolayers (7.8) | strong substrate adhesion reverses engulfment order (Steinberg–Garrod: liver vs limb bud) |
| Matrix (7.9) | substrate, signal presentation, differentiation; A₂B₃ tree network: $\langle n_A\rangle = 1 + 4pp'/(1 - 2pp')$, gel point $2pp' = 1$ (Definition 7.9.1, Theorem 7.9.1) |
| EMT/MET (7.10) | Snail/Twist/Zeb repress E-cadherin; gastrulation, neural crest, sclerotome, cancer; MET in somites and nephrons (Definition 7.10.1) |

## Questions

1. Two tissues have adhesive energies $E_{AA} = 6$, $E_{BB} = 2$ and $E_{AB} = 3$ (arbitrary units), and the medium does not adhere. Compute the three interfacial tensions and predict the end state of a mixed aggregate. What happens if $E_{AB}$ is lowered to 1? Raised to 4.5?

   **Answer** From Eq. (7.1), $\gamma_{A\mathrm{O}} = 3$, $\gamma_{B\mathrm{O}} = 1$, $\gamma_{AB} = 4 - 3 = 1$. Since $\gamma_{AB} > 0$ the cells sort; $E_{AB} = 3 \ge E_{BB} = 2$, so $B$ engulfs $A$ completely (equivalently $\gamma_{A\mathrm{O}} = 3 \ge \gamma_{AB} + \gamma_{B\mathrm{O}} = 2$). With $E_{AB} = 1$: $\gamma_{AB} = 3$; now $0 < E_{AB} < E_{BB}$, so engulfment is partial (all three triangle inequalities hold: $3 < 3 + 1$, $1 < 3 + 3$). With $E_{AB} = 4.5 > \frac12(6 + 2) = 4$: $\gamma_{AB} = -0.5 < 0$, and the cells intermix.

2. Using the parallel-plate equation, estimate the surface tension of an aggregate compressed to an equatorial radius $R_2 = 200\,\mu\mathrm{m}$ with profile radius $R_1 = 120\,\mu\mathrm{m}$ and contact radius $R_3 = 150\,\mu\mathrm{m}$, if the equilibrium force is $F = 4\,\mu\mathrm{N}$. Which tissue of Figure 3 might it be? How would you check that the aggregate behaves as a liquid?

   **Answer** $F/(\pi R_3^2) = 4\times10^{-6}/(\pi\cdot2.25\times10^{-8}) \approx 56.6\,\mathrm{Pa}$; $1/R_1 + 1/R_2 = 8333 + 5000 = 13333\,\mathrm{m^{-1}}$; $\gamma \approx 56.6/13333 \approx 4.2\times10^{-3}\,\mathrm{N\,m^{-1}} = 4.2\,\mathrm{mN\,m^{-1}}$, close to liver (4.6). For a liquid, $\gamma$ must not depend on the degree of compression: repeat at two or three different plate separations, waiting each time for the force to relax to a steady value, and check that the computed $\gamma$ is the same; also check that the aggregate rounds up again when released only slowly (viscous) rather than springing back (elastic).

3. Prove that in the sparse-site model the arrangement of $M$ cell types that minimizes the surface potential is an onion with site density decreasing outwards, at least in the sense that every pair of types shows complete engulfment of the higher-density type. Then explain why the onion layers need not be concentric.

   **Answer** With $E_{ij} = k\eta_i\eta_j$, for $\eta_A > \eta_B$: $\gamma_{AB} = \frac k2(\eta_A - \eta_B)^2 > 0$ (sorting) and $E_{AB} = k\eta_A\eta_B > k\eta_B^2 = E_{BB}$, so by Theorem 7.2.1 $B$ engulfs $A$ completely. Every pair satisfies complete engulfment, so by Proposition 7.2.2 the relation is transitive and orders the types by $\eta$; nesting the types in this order puts the highest density innermost. The surface energy depends only on the areas of the interfaces, and spherical interfaces of given enclosed volumes have the same areas whatever their relative position, so shifting an inner sphere inside its envelope costs nothing: concentricity is not selected (some other mechanism must centre the layers).

4. (Experimental design) You suspect that two cell populations of the early embryo sort because of a difference in the amount of N-cadherin rather than in its type. Design experiments, with cell lines or embryonic cells, that would distinguish the two possibilities and would test whether sorting is driven by adhesion energy or by cortical tension.

   **Answer** Dose: express N-cadherin from an inducible promoter in a cadherin-free line (L cells) and make subclones with different measured surface levels; mix pairs and see whether the higher expresser goes inside (amount sufficient), and measure aggregate surface tension by plate compression to check the linear γ–cadherin relation. Type: give two subclones different cadherins at equal levels; separation into two mounds indicates type specificity. In embryonic cells, knock down N-cadherin or replace it by another cadherin and test sorting. To separate adhesion from cortex: express a cadherin lacking its catenin-binding tail (adhesion without cortical coupling), or inhibit myosin II (blebbistatin) or Rho kinase; measure contact angles of cell doublets ($\gamma_{\mathrm{cc}} = 2\sigma_{\mathrm{f}}\cos\theta$) and cortical tension by micropipette aspiration or AFM. If sorting tracks cortical tension when adhesion is held constant, the interfacial-tension view is supported.

5. In the lattice model of Figure 5, explain why rule 1 stops with convoluted clusters, and why adding long-range exchanges (rule 3) completes engulfment much faster than temperature alone (rule 2).

   **Answer** Rule 1 accepts only exchanges that do not decrease adhesion. Smoothing a convoluted interface generally requires passing through intermediate configurations of lower adhesion (moving a cell out of a pocket first breaks bonds), so the system becomes trapped in a local maximum of $E_{\mathrm{ad}}$ where only neutral moves remain. Temperature allows such uphill moves with probability $\mathrm{e}^{\Delta E/T}$, but coarsening then proceeds by local diffusion of cells along interfaces, which is slow (domain size grows roughly as a low power of time). Long-range exchanges let an $A$ cell stranded among $B$ cells jump to the $A$ core in one move, the lattice analogue of the long-range pressure-driven flows of an incompressible tissue, so the system reaches the global minimum quickly.

6. For the Smoluchowski equation with constant kernel, find the time at which the number of clusters has fallen to one tenth of the number of cells, and the fraction of cells that are still single at that time. With $N$ cells and a merger rate $\kappa$ per pair of clusters (per unit volume, with cell density $n_0$), what is the dimensional time?

   **Answer** Clusters per cell $G(1, t) = 2/(2 + t) = 0.1$ gives $t = 18$. Single cells per cell: $p_1 = 4/(2 + t)^2 = 4/400 = 0.01$, i.e. 1% of cells are still single. Time was scaled as $t = \kappa n_0 t_{\mathrm{dim}}$ (each cluster meets others at rate $\kappa$ times their density, which is $n_0$ times the cluster number per cell), so $t_{\mathrm{dim}} = 18/(\kappa n_0)$.

7. In the bivalent–trivalent network, suppose $[\ce{A}]$ is fixed so that $p = 0.8$. What is the smallest $p'$ at which a gel forms? What is the mean number of $A$ molecules per tree when $p' = 0.5$? Show also that the gel fraction is zero below the gel point.

   **Answer** Gel point $2pp' = 1$: $p' = 1/1.6 = 0.625$. For $p' = 0.5$: $2pp' = 0.8$, $\langle n_A\rangle = 1 + 4(0.4)/(0.2) = 1 + 8 = 9$. Below the gel point, $f_A = 1$ is a solution of $f_A = q' + p'(q + pf_A)^2$; the map $h(f) = q' + p'(q + pf)^2$ is increasing and convex with $h(1) = 1$ and $h'(1) = 2pp' < 1$, so the smallest fixed point in $[0, 1]$ is $f = 1$ and the gel fraction $1 - f_A^2$ is zero; when $2pp' > 1$ a second, smaller fixed point appears and the gel fraction becomes positive.

8. Why do monolayer cultures of liver and limb bud cells show the reverse engulfment order of three-dimensional aggregates? Predict what would happen to the monolayer order if the substrate were coated with a molecule to which neither cell type adhered.

   **Answer** In a monolayer most of each cell's surface energy is in its contact with the substrate, which is strongly adhesive for all types; the interfacial stress at the substrate acts in the opposite direction to the free-surface tension and dominates it, so the order set by cell–cell adhesion is inverted: the type that is enveloped in three dimensions (limb bud) now surrounds islands of the other (liver). If the substrate were non-adhesive, cells would not spread; the "monolayer" would round up into three-dimensional aggregates and the three-dimensional order (liver outside, limb bud inside) would return.

9. (Open question) The neural tube separates from the epidermis when neural cells switch from E- to N-cadherin. Using Theorem 7.2.1, explain why this switch is sufficient in principle for separation, and list two additional mechanisms that could make the separation robust in the embryo.

   **Answer** Before the switch both tissues express E-cadherin, so $E_{AB}$ between neural plate and epidermis is comparable to the homotypic energies and the tissues stay joined (or even mix). After the switch, E-cadherin and N-cadherin bind each other weakly, so $E_{AB}$ falls towards zero while each tissue keeps strong homotypic adhesion; by Theorem 7.2.1, $E_{AB} \le 0$ (or close to it) leads to separation and small $E_{AB}$ to partial contact only. Additional mechanisms: actomyosin cables raising the tension of the boundary (as at the notochord boundary); repulsive Eph–ephrin signalling across the boundary; differential adhesion to the basal lamina and underlying mesoderm; and the folding movements of neurulation themselves, which pull the tissues apart (7.5.18).

10. Show that for an equal-tension liquid ($\gamma_{AB} = \gamma_{A\mathrm{O}} = \gamma_{B\mathrm{O}}$, as for two soap bubbles of equal tension) the three phases meet at $120^\circ$, and compute the angles for the case of Question 1 with $E_{AB} = 1$.

    **Answer** At the contact line the three tension vectors, each pointing along its interface away from the line, sum to zero. The angle $\theta_{ij}$ between the vectors of tensions $\gamma_i$ and $\gamma_j$ satisfies $\gamma_k^2 = \gamma_i^2 + \gamma_j^2 + 2\gamma_i\gamma_j\cos\theta_{ij}$, and it is the opening angle of the phase bounded by those two interfaces. With equal tensions, $\cos\theta = -\frac12$, $\theta = 120^\circ$ for all three phases. For $\gamma_{A\mathrm{O}} = 3$, $\gamma_{B\mathrm{O}} = 1$, $\gamma_{AB} = 3$: phase $A$ (between the $A$–$\mathrm{O}$ and $A$–$B$ interfaces), $\cos\theta = (1 - 9 - 9)/18 = -17/18$, $\theta \approx 160.8^\circ$; phase $B$, $\cos\theta = (9 - 1 - 9)/6 = -1/6$, $\theta \approx 99.6^\circ$; the medium, $\cos\theta = (9 - 9 - 1)/6$, again $\approx 99.6^\circ$. The angles add up to $360^\circ$. The wide angle of $A$ means that $A$ is barely flattened at the contact, while $B$ bends over it: a weak partial engulfment.
