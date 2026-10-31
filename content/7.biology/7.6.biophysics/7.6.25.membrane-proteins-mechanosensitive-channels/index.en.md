---
title: Membrane Proteins and Mechanosensitive Channels
description: How the elasticity of the lipid bilayer acts on the proteins embedded in it. Hydrophobic thickness and mismatch; the thickness-deformation energy, its Euler–Lagrange equation and the decaying, oscillating profile around an inclusion; the line tension of a protein and its two-dimensional correction; gramicidin, lipid-chain length and the sorting of transmembrane segments; membrane-mediated interactions between inclusions; MscL as a two-state channel whose gating energy comes from tension and mismatch (Wiggins–Phillips model, Perozo data), spontaneous curvature and the lateral pressure profile; bacterial channels as osmotic safety valves; eukaryotic mechanosensitive channels, the elastic dome of Piezo, and tethered channels in hair cells and NOMPC.
---

The **lipid bilayer** is a two-dimensional fluid with elastic moduli, and the proteins embedded in it are not floating passengers. A transmembrane protein presents a belt of hydrophobic surface that must be covered by lipid tails; if the belt is thicker or thinner than the bilayer, the lipids around it stretch or compress, and the protein pays an elastic energy that depends on its shape. When the protein changes conformation, its shape and with it the elastic energy change, so the membrane takes part in the protein's free-energy balance: membrane tension, thickness, lipid composition and curvature become controls of protein function. This chapter develops that idea quantitatively. The elastic moduli and the Helfrich energy of membranes were introduced in [7.6.24](/7.6.24#sec-24.2); here they are applied to a membrane containing an inclusion. We first compute the deformation around a single protein and its energy, a line tension along the protein's boundary (25.1–25.2), then the interaction of two proteins through the deformed bilayer (25.3). The mechanosensitive channel of large conductance, MscL, whose gating by tension was introduced as a **two-state system** in [7.6.4](/7.6.4#sec-4.2.1), is the test case: its gating energy and critical tension follow from the same elastic theory and depend on lipid chain length as predicted (25.4). Bacterial channels act as osmotic safety valves, a function that a simple model of osmotic shock makes quantitative (25.5). Eukaryotic mechanosensitive channels use the same physics in larger form, the curved dome of Piezo, or transmit force through protein tethers, as in hair cells (25.6). The cell biology of **mechanosensitive channels** is in [7.3.5](/7.3.5#sec-5.7); their electrophysiology and permeation in [7.6.30](/7.6.30), and mechanosensation by whole cells, including the gating spring of the hair bundle, in [7.6.31](/7.6.31).

## 25.1. Membrane Proteins in an Elastic Bilayer

### 25.1.1. Proteins as Inclusions

Membranes are crowded with proteins. In the plasma membrane of a mammalian cell proteins and lipids are present in roughly equal masses, and proteins occupy about a quarter to a third of the area; in the inner membrane of mitochondria and in the thylakoid membrane they occupy more than half ([7.6.23](/7.6.23)). Most integral proteins cross the bilayer with α-helices of $20$–$25$ hydrophobic residues ($0.15\,\mathrm{nm}$ per residue, so $3$–$3.7\,\mathrm{nm}$) or with β-barrels, and the hydrophobic core of a bilayer of phosphatidylcholine with two 18-carbon chains is about $3$–$3.5\,\mathrm{nm}$ thick. The match is good but never exact, and the numbers vary from one membrane to another: the plasma membrane, enriched in cholesterol and sphingolipids, is thicker than the membranes of the endoplasmic reticulum.

**Definition 25.1.1 (Hydrophobic Mismatch)** The *hydrophobic thickness* of a bilayer, $2w_0$, is the thickness of its hydrocarbon core; that of a transmembrane protein, $W$, is the height of the belt of hydrophobic residues on its surface. Their difference, written per leaflet as $U = W/2 - w_0$, is the *hydrophobic mismatch*: positive when the protein is thicker than the bilayer, negative when it is thinner.

Why does the bilayer deform rather than leave part of the protein's belt, or of its own tails, exposed to water? The **hydrophobic effect** costs about $25$–$40\,\mathrm{cal\,mol^{-1}}$ per $\text{Å}^2$ of exposed hydrocarbon, $4$–$7\,k_{\mathrm{B}}T\,\mathrm{nm^{-2}}$. Leaving a strip $0.3\,\mathrm{nm}$ high exposed around a protein of radius $2.5\,\mathrm{nm}$ would cost $20$–$30\,k_{\mathrm{B}}T$, a cost proportional to the mismatch, whereas the elastic cost of deforming the lipids grows as its square (25.2) and is the cheaper response for small mismatches, comparable for mismatches of a few tenths of a nanometer. The bilayer therefore adjusts its thickness near the protein, the lipid tails stretching next to a thick protein and compressing next to a thin one, and for larger mismatches the protein also tilts its helices, changes its conformation or moves to a region of the membrane with a better-matched thickness. All three responses are seen.

### 25.1.2. The Energy of Membrane Deformation

Describe the two leaflets near a protein by the heights $h_+(x)$ and $h_-(x)$ of the interfaces between the hydrocarbon core and the head groups (panel A of the first figure of 25.2). Their mean $h = (h_+ + h_-)/2$ is the midplane, and their half-difference $w = (h_+ - h_-)/2$ the local half-thickness; a protein can bend the midplane, change the thickness, or both. Each leaflet has bending rigidity $\kappa/2$, so bending the two interfaces costs

$$
G_{\mathrm{bend}} = \frac{\kappa}{4}\int\left[(\nabla^2 h_+)^2 + (\nabla^2 h_-)^2\right]\mathrm{d}A = \frac{\kappa}{2}\int\left[(\nabla^2 h)^2 + (\nabla^2 w)^2\right]\mathrm{d}A, \tag{25.1}
$$
so that the midplane and the thickness modes decouple. The midplane term is the small-slope form of the Helfrich energy of [7.6.24](/7.6.24#def-24.2.3) with $2H \approx \nabla^2 h$. Changing the thickness compresses or stretches the tails, at the cost of Eq. [(24.3)](/7.6.24#eq-24.3) of 7.6.24, with the thickness modulus $K_t \approx 60\,k_{\mathrm{B}}T\,\mathrm{nm^{-2}}$, close to the area expansion modulus because a fluid bilayer conserves volume: thinning by a fraction $\varepsilon$ increases the area per lipid by the same fraction. The membrane tension $\tau$ (written $\sigma$ in [7.6.24](/7.6.24#def-24.2.5); here $\tau$, as in [7.6.4](/7.6.4#sec-4.2.1)) adds $-\tau$ times the area that the protein's conformational change takes from the membrane. A protein with a symmetric, cylindrical hydrophobic belt does not bend the midplane, and only the thickness mode is excited; we treat this case first.

## 25.2. The Deformation Around a Single Protein

### 25.2.1. The Euler–Lagrange Equation

Let $u = w - w_0$ be the change of half-thickness. In one dimension, for a straight wall of protein at $x = R$ and membrane in $x > R$, the energy per unit length of wall is a functional of $u(x)$.

**Formula 25.2.1 (Thickness-Deformation Energy)** The free energy per unit length of the bilayer deformed by a straight inclusion is

$$
G_{\mathrm{h}}[u] = \int_R^\infty\left[\frac{\kappa}{2}\left(\frac{\mathrm{d}^2u}{\mathrm{d}x^2}\right)^2 + \frac{K_t}{2w_0^2}u^2\right]\mathrm{d}x , \tag{25.2}
$$
with the gluing conditions $u(R) = U$ (the bilayer matches the protein's hydrophobic belt) and $u'(R) = 0$ (both leaflets meet the protein symmetrically), and $u, u' \to 0$ far away.

The profile that minimizes $G_{\mathrm{h}}$ is found by the **calculus of variations** ([2.4.13](/2.4.13)). Replace $u$ by $u + \varepsilon\eta$ with $\eta(R) = \eta'(R) = 0$; the first variation $\int[\kappa u''\eta'' + (K_t/w_0^2)u\eta]\,\mathrm{d}x$ must vanish for all $\eta$. Integrating the first term twice by parts (the boundary terms vanish because $\eta$ and $\eta'$ vanish at $R$ and $u$ decays at infinity) gives $\int[\kappa u'''' + (K_t/w_0^2)u]\eta\,\mathrm{d}x = 0$, and so the **Euler–Lagrange equation** of fourth order

$$
\kappa\frac{\mathrm{d}^4u}{\mathrm{d}x^4} + \frac{K_t}{w_0^2}u = 0 . \tag{25.3}
$$

### 25.2.2. The Profile and the Line Tension

**Theorem 25.2.1 (Line Tension of a Mismatched Inclusion)** Let $\lambda = \left(K_t/\kappa w_0^2\right)^{1/4}$. The minimizer of Formula 25.2.1 is

$$
u(x) = U\,\mathrm{e}^{-y}(\cos y + \sin y), \qquad y = \frac{\lambda(x - R)}{\sqrt2}, \tag{25.4}
$$
and its energy per unit length of wall is

$$
f = \frac{K_tU^2}{\sqrt2\,\lambda w_0^2} = \frac12\mathcal{K}U^2, \qquad \mathcal{K} = \sqrt2\left(\frac{K_t^3\kappa}{w_0^6}\right)^{1/4}. \tag{25.5}
$$
One quarter of this energy is bending and three quarters is compression or stretching of the tails.

**Proof** Trying $u = \mathrm{e}^{zx}$ in Eq. (25.3) gives $z^4 = -\lambda^4$, whose four roots are $\lambda\mathrm{e}^{\mathrm{i}\pi(2k+1)/4}$, $k = 0, \dots, 3$. The two with negative real part, $\lambda(-1 \pm \mathrm{i})/\sqrt2$, decay; their real combinations are $\mathrm{e}^{-y}\cos y$ and $\mathrm{e}^{-y}\sin y$. Writing $u = \mathrm{e}^{-y}(a\cos y + b\sin y)$, $u(R) = U$ gives $a = U$ and $u'(R) \propto b - a = 0$ gives $b = U$. For the energy let $g(y) = \mathrm{e}^{-y}(\cos y + \sin y)$; then $g'' = -2\mathrm{e}^{-y}(\cos y - \sin y)$, and with $\int_0^\infty\mathrm{e}^{-2y}\,\mathrm{d}y = \frac12$, $\int_0^\infty\mathrm{e}^{-2y}\sin 2y\,\mathrm{d}y = \frac14$,

$$
\int_0^\infty g^2\,\mathrm{d}y = \tfrac34, \qquad \int_0^\infty (g'')^2\,\mathrm{d}y = 1 .
$$
Since $\mathrm{d}x = \sqrt2\,\mathrm{d}y/\lambda$ and $u'' = (\lambda^2/2)Ug''$, the bending term is $\frac{\kappa}{2}\frac{\lambda^4}{4}U^2\frac{\sqrt2}{\lambda} = \frac{\sqrt2}{8}\frac{K_tU^2}{\lambda w_0^2}$ (using $\kappa\lambda^4 = K_t/w_0^2$) and the thickness term is $\frac{K_t}{2w_0^2}U^2\frac{\sqrt2}{\lambda}\frac34 = \frac{3\sqrt2}{8}\frac{K_tU^2}{\lambda w_0^2}$. Their sum is Eq. (25.5), in the ratio $1 : 3$. $\square$

The deformation decays over $\lambda^{-1}$ with a slight overshoot: the bilayer that has been thickened next to a thick protein becomes slightly thinner than normal about $3\lambda^{-1}$ away, because a fourth-order equation cannot relax monotonically under the condition $u'(R) = 0$. The energy is proportional to the length of the protein's boundary, so a mismatched protein behaves like a two-dimensional droplet with a line tension $f$, and it is quadratic in the mismatch, so it does not matter for the energy whether the protein is too thick or too thin.

**Example 25.2.1 (Numbers for a PC bilayer)** With $\kappa = 20\,k_{\mathrm{B}}T$, $K_t = 60\,k_{\mathrm{B}}T\,\mathrm{nm^{-2}}$ and $w_0 = 1.75\,\mathrm{nm}$, $\lambda^{-1} = (\kappa w_0^2/K_t)^{1/4} = (1.02\,\mathrm{nm^4})^{1/4} = 1.0\,\mathrm{nm}$ and $\mathcal{K} = \sqrt2\,(60^3 \times 20/1.75^6)^{1/4}\,k_{\mathrm{B}}T\,\mathrm{nm^{-3}} = 28\,k_{\mathrm{B}}T\,\mathrm{nm^{-3}}$. A mismatch of $U = 0.3\,\mathrm{nm}$ (two carbons per lipid chain, at about $0.13\,\mathrm{nm}$ per carbon, each side) gives $f = \frac12 \times 28 \times 0.09 = 1.3\,k_{\mathrm{B}}T\,\mathrm{nm^{-1}}$, about $5\,\mathrm{pN}$. Around a protein of radius $2.5\,\mathrm{nm}$ the deformed annulus, a single layer of lipids or two wide, costs $2\pi R f \approx 20\,k_{\mathrm{B}}T$. This is large compared with the thermal energy and comparable to the free-energy differences between conformations of membrane proteins, which is why lipid composition can switch them.

### 25.2.3. Two Dimensions

A real protein is a cylinder, not a wall. In polar coordinates around a cylinder of radius $R$, Eq. (25.3) becomes $(\nabla^2)^2u + \lambda^4u = 0$, which factors as $(\nabla^2 - \mathrm{i}\lambda^2)(\nabla^2 + \mathrm{i}\lambda^2)u = 0$. The decaying axisymmetric solutions are the modified Bessel functions $K_0(\mu r)$ with $\mu^2 = \pm\mathrm{i}\lambda^2$ (Kelvin functions), and the real solution is $u = \operatorname{Re}[C\,K_0(\lambda\mathrm{e}^{\mathrm{i}\pi/4}r)]$ with a complex constant $C$ fixed by the same two gluing conditions. The profile is almost that of Eq. (25.4) (panel B), but the energy per unit length of boundary is larger, because the deformed area grows faster than the circumference: by about $30\,\%$ for $\lambda R \approx 2$ and by less for larger proteins (panel C). The line-tension picture, $G = 2\pi Rf$, is thus a fair approximation whose error is itself a decreasing function of radius; this matters for gating, which compares two radii.

![Hydrophobic mismatch: the deformation of a bilayer around a membrane protein. A: profiles of the hydrocarbon core (beige) and head-group layers (orange) around a protein whose hydrophobic belt (dotted lines) is thicker (top, U = +0.5 nm) or thinner (bottom, U = −0.5 nm) than the bilayer, computed from Theorem 25.2.1 with κ = 20 k_BT, K_t = 60 k_BT nm⁻² and w₀ = 1.75 nm (1/λ = 1.0 nm). B: the thickness change u/U against distance from the protein in the one-dimensional model (Eq. (25.4)) and around a cylinder of radius 2.5 nm (Kelvin-function solution); both decay over about 3/λ with a small overshoot. C: the energy of the deformed annulus around a cylinder divided by the line-tension estimate 2πRf, against λR; the dots mark the closed and open radii of MscL](./plots/mismatch-deformation.py)

### 25.2.4. Experimental Tests

The antibiotic gramicidin A is a pentadecapeptide of alternating L- and D-amino acids that folds into a narrow β-helix about $1.1\,\mathrm{nm}$ long. A conducting channel forms when two monomers, one in each leaflet, meet head to head; its hydrophobic length (about $2.2\,\mathrm{nm}$) is shorter than that of most bilayers, so the dimer must pull the surrounding lipids inward. The single-channel lifetime, the time until the dimer dissociates, therefore falls as the bilayer gets thicker, steeply and roughly as $\mathrm{e}^{-\Delta f/k_{\mathrm{B}}T}$ with $\Delta f \propto U^2$ (Elliott and colleagues 1983; Huang 1986, who formulated the elastic theory used here). Because it is so sensitive, gramicidin has been used to measure the effect of drugs, detergents and cholesterol on bilayer elasticity (Lundbæk and Andersen): amphiphiles that soften the bilayer prolong channel lifetimes, and the same compounds change the gating of many unrelated membrane proteins, which suggests that part of their pharmacology acts through the membrane.

The same holds for MscL. Reconstituted in phosphatidylcholines with chains of $16$, $18$ and $20$ carbons, MscL needs more tension to open the thicker the bilayer, and the free energy of opening at zero tension rises from about $4$ to $24\,k_{\mathrm{B}}T$ (Perozo and colleagues 2002), a dependence that the model of 25.4 explains.

Hydrophobic matching also acts in sorting along the secretory pathway. Transmembrane segments of proteins that reside in the plasma membrane are on average several residues longer than those of proteins of the endoplasmic reticulum and the Golgi apparatus, in fungi as in vertebrates (Sharpe, Stevens and Munro 2010), and lengthening the segment of a Golgi protein moves it to the plasma membrane. The thickness of the membranes increases along the pathway as cholesterol and sphingolipids accumulate, and hydrophobic matching contributes to keeping proteins in the right compartment; it is one of the forces, with sorting signals read by coat proteins, that shape the composition of organelles. The same mismatch energy contributes to the partitioning of proteins into ordered domains (**lipid rafts**, [7.6.24](/7.6.24#def-24.1.2)).

## 25.3. Interactions Through the Membrane

### 25.3.1. Overlapping Deformations

Two mismatched proteins close to each other interact because the bilayer between them cannot relax. In the one-dimensional model, the strip of width $d$ between two walls with mismatches $U_1$ and $U_2$ satisfies Eq. (25.3) with the gluing conditions at both ends, and its energy minus the energy $2f$ of two isolated faces is the interaction per unit length of contact.

**Formula 25.3.1 (Mismatch-Mediated Interaction)** For two parallel inclusions at distance $d$, the interaction energy per unit length is

$$
\Delta G(d) = \min_u\int_0^d\left[\frac{\kappa}{2}(u'')^2 + \frac{K_t}{2w_0^2}u^2\right]\mathrm{d}x - \frac{\mathcal{K}}{4}\left(U_1^2 + U_2^2\right), \tag{25.6}
$$
with $u(0) = U_1$, $u(d) = U_2$ and $u'(0) = u'(d) = 0$. For like inclusions ($U_1 = U_2$) it tends to $-2f$ at contact and oscillates with period $2\sqrt2\pi/\lambda$ as it decays; for opposite mismatches it is repulsive at short range.

At contact the bilayer between two like proteins is squeezed out and the two deformed faces disappear, so the attraction is the line tension times the length of contact, a few $k_{\mathrm{B}}T$ for $U \approx 0.3\,\mathrm{nm}$ and a contact of a nanometer or two. A protein thicker than the bilayer and one thinner than it repel each other, because the bilayer between them would have to change thickness by $2U$ over a short distance. The oscillation produces a small barrier at about $4.4/\lambda$, about $4\,\mathrm{nm}$, and a weak secondary minimum for unlike proteins. These forces favor clustering of proteins with similar hydrophobic thickness and their separation from proteins of different thickness, a physical mechanism for the lateral organization of membranes that requires no binding interface at all. Clusters of MscL and of other mechanosensitive channels have been observed in reconstituted membranes, and the model predicts that clustering changes gating, because the line tension that opposes opening (25.4) is shared between neighbors (Ursell, Huang, Peterson and Phillips 2007).

![Interaction between two mismatched inclusions through the bilayer (Formula 25.3.1, same constants as the previous figure). A: interaction energy per unit length of contact, in units of the line tension f of one face, against λd: equal mismatches attract at short range (−2f at contact), with a small barrier near λd = 4.4; opposite mismatches repel strongly at short range and attract weakly near λd = 4.4. B: thickness profiles between equal inclusions at three separations: at λd = 1 the bilayer stays at the protein's thickness everywhere between them, at λd = 6 it relaxes almost to its own thickness in the middle](./plots/membrane-mediated-interaction.py)

### 25.3.2. Curvature and Fluctuations

Proteins that bend the midplane, because their hydrophobic belt is conical or because they insert an amphipathic helix into one leaflet, interact through the curvature they impose. Two conical inclusions in a flat, tensionless membrane repel each other with an energy proportional to $\kappa$ times the squares of their contact angles, decaying as $r^{-4}$, and fluctuations of the membrane add an attraction of order $k_{\mathrm{B}}T(a/r)^4$ for inclusions of radius $a$ (Goulian, Bruinsma and Pincus 1993, with later corrections of the prefactors). These pairwise forces are weaker than mismatch forces at contact but act at larger distances, and many curvature-inducing proteins together can lower their elastic energy collectively by bending the membrane as a whole into a bud or tube, the cooperative mechanism behind the budding of [7.6.24](/7.6.24#sec-24.4). Crowding by other proteins adds an entropic two-dimensional pressure and line tension that favor compact conformations ([7.6.23](/7.6.23), Eq. (23.6)).

## 25.4. MscL: Gating by Tension and Mismatch

### 25.4.1. Structure and Measurement

MscL is a homopentamer of subunits of about 136 residues in *Escherichia coli*. Each subunit has two transmembrane helices: TM1 lines the pore and TM2 faces the lipids, and an amphipathic N-terminal helix lies along the cytoplasmic surface. The crystal structure of the closed channel of *Mycobacterium tuberculosis* (Chang and colleagues 1998) shows a constriction lined by hydrophobic residues; opening tilts the helices like the blades of an iris, widens the pore to about $3\,\mathrm{nm}$, gives a conductance of about $3\,\mathrm{nS}$ and increases the channel's area in the plane of the membrane by about $20\,\mathrm{nm^2}$. In the model below, the closed channel is a cylinder of radius $R_{\mathrm{c}} \approx 2.3\,\mathrm{nm}$ and the open one of radius $R_{\mathrm{o}} \approx 3.5\,\mathrm{nm}$, so that $\Delta A = \pi(R_{\mathrm{o}}^2 - R_{\mathrm{c}}^2) = 22\,\mathrm{nm^2}$. As the helices tilt, the hydrophobic thickness of the channel also decreases.

Gating is measured by **patch clamp**: a pipette sucks a patch of membrane (a spheroplast of *E. coli*, or liposomes with purified channel) into a dome, and a pressure difference $\Delta p$ sets its tension through the **Young–Laplace equation**, $\tau = \Delta p\,r_{\mathrm{c}}/2$, where $r_{\mathrm{c}}$ is the radius of curvature of the patch, measured by imaging. The open probability is read from the current, which rises in steps of one channel conductance.

**Example 25.4.1 (From pressure to tension)** In Perozo's experiments MscL in a PC18 bilayer was half open at $\Delta p = 42\,\mathrm{mmHg} = 5.6\,\mathrm{kPa}$. For a patch of radius of curvature $r_{\mathrm{c}} = 1\,\mu\mathrm{m}$, $\tau = 5.6\times10^3 \times 10^{-6}/2\,\mathrm{N\,m^{-1}} = 2.8\,\mathrm{mN\,m^{-1}}$; for $3\,\mu\mathrm{m}$, $8.4\,\mathrm{mN\,m^{-1}}$. Converting a pressure into a tension is the largest source of uncertainty in such measurements, which is why ratios of tensions, for example between two lipids or between MscL and MscS in the same patch, are more reliable than absolute values.

### 25.4.2. The Elastic Model of Gating

Treat the channel as a cylinder of variable radius $R$ whose hydrophobic mismatch $U$ is the same in both states (Wiggins and Phillips 2004). Its free energy is the protein's own conformational energy, the line energy of Theorem 25.2.1 and the work of the tension.

**Formula 25.4.1 (Elastic Gating Free Energy)** A channel of radius $R$ in a bilayer under tension $\tau$ has

$$
G(R) = G_{\mathrm{p}}(R) + 2\pi Rf - \pi R^2\tau, \qquad f = \frac12\mathcal{K}U^2 . \tag{25.7}
$$

If the protein term $G_{\mathrm{p}}$ is the same for the two states, as the model assumes, the membrane alone decides: the line energy grows linearly with $R$ and favors the closed state, the tension term grows quadratically and favors the open one (panel A of the figure).

**Theorem 25.4.1 (Critical Tension of the Elastic Channel)** In Formula 25.4.1 with $G_{\mathrm{p}}(R_{\mathrm{c}}) = G_{\mathrm{p}}(R_{\mathrm{o}})$, the open and closed states have equal free energies at

$$
\tau^* = \frac{2f}{R_{\mathrm{o}} + R_{\mathrm{c}}} = \frac{\mathcal{K}U^2}{R_{\mathrm{o}} + R_{\mathrm{c}}}, \tag{25.8}
$$
the zero-tension free energy of opening is $\Delta G_0 = 2\pi f(R_{\mathrm{o}} - R_{\mathrm{c}}) = \pi\mathcal{K}U^2(R_{\mathrm{o}} - R_{\mathrm{c}})$, and the open probability is that of the two-state channel of [Formula 4.2.1](/7.6.4#fml-4.2.1) with $\Delta\varepsilon = \Delta G_0$ and $\Delta A = \pi(R_{\mathrm{o}}^2 - R_{\mathrm{c}}^2)$.

**Proof** $G(R_{\mathrm{o}}) - G(R_{\mathrm{c}}) = 2\pi f(R_{\mathrm{o}} - R_{\mathrm{c}}) - \pi\tau(R_{\mathrm{o}}^2 - R_{\mathrm{c}}^2)$, which vanishes at $\tau = 2f/(R_{\mathrm{o}} + R_{\mathrm{c}})$ after division by $\pi(R_{\mathrm{o}} - R_{\mathrm{c}})$. At $\tau = 0$ the difference is $\Delta G_0$, and for general $\tau$ it is $\Delta G_0 - \tau\Delta A$, the form of Formula 4.2.1. $\square$

Both $\tau^*$ and $\Delta G_0$ scale as $U^2$. For PC lipids the half-thickness grows by about $0.065\,\mathrm{nm}$ per carbon, and if MscL matches a 12-carbon bilayer, $U = 0.065(12 - n)\,\mathrm{nm}$ for chains of $n$ carbons. With $\mathcal{K} = 20\,k_{\mathrm{B}}T\,\mathrm{nm^{-3}}$ (the lower end of the range in Example 25.2.1), the model gives:

| Chain length $n$ | $U$ / nm | $\tau^*$ / ($k_{\mathrm{B}}T\,\mathrm{nm^{-2}}$) | $\tau^*$ / ($\mathrm{mN\,m^{-1}}$) | $\Delta G_0$ (model) / $k_{\mathrm{B}}T$ | $\Delta G_0$ (Perozo 2002) / $k_{\mathrm{B}}T$ | $p_{1/2}$ measured / mmHg |
|---|---|---|---|---|---|---|
| 16 | $-0.26$ | $0.23$ | $1.0$ | $5.1$ | $4.0$ | $24$ |
| 18 | $-0.39$ | $0.52$ | $2.2$ | $11.5$ | $9.4$ | $42$ |
| 20 | $-0.52$ | $0.93$ | $3.8$ | $20.4$ | $23.5$ | $72$ |

The model reproduces the magnitude and the steep, quadratic rise of the gating energy with chain length, and the measured half-activation pressures rise threefold, close to the predicted fourfold rise of $\tau^*$, without any change in the protein. The free energies are lower than the roughly $50\,k_{\mathrm{B}}T$ found for MscL in native *E. coli* membranes ([Example 4.2.1](/7.6.4#ex-4.2.1)), where the protein term, lipid composition and the 2D correction of 25.2.3 add to the line energy. The model also explains a puzzle: MscL needs a large tension although its area change is large, because the line energy that resists opening grows with the radius. The protein's structure sets $\Delta A$; the membrane sets most of $\Delta G_0$.

![The elastic model of MscL gating (Formula 25.4.1, Theorem 25.4.1; K = 20 k_BT nm⁻³, closed radius 2.3 nm, open radius 3.5 nm, U = 0.065(12 − n) nm). A: free energy against channel radius in a PC18 bilayer at zero tension, at the critical tension τ* (open and closed states equal) and above it; shaded regions are inaccessible (steric overlap of the helices below R_c, separation of the helices above R_o). B: open probability against membrane tension for PC16, PC18 and PC20 (k_BT = 4.1 pN nm): the thicker the bilayer, the higher the tension needed. C: the zero-tension free energy of opening from the model (line, squares) and from the patch-clamp gating curves of Perozo and colleagues (2002, circles)](./plots/mscl-gating.py)

### 25.4.3. Beyond Thickness: Curvature and the Lateral Pressure Profile

Thickness is not the only property of the bilayer that MscL feels. Perozo and colleagues (2002) opened MscL without any tension by adding lysophosphatidylcholine, a lipid with a single chain and a large head group (an inverted cone, positive spontaneous curvature), to one leaflet; added to both leaflets, it had no such effect. The asymmetric addition changes the **spontaneous curvature** of one monolayer and the profile of stresses across the bilayer rather than its mean tension.

A bilayer under zero tension is not free of stress inside. The head groups repel each other, the interface between hydrocarbon and water pulls inward with a large interfacial tension, and the chains push outward with their entropic pressure; the lateral pressure $p(z)$ varies across the bilayer by hundreds of atmospheres, and only its integral vanishes, $\int p(z)\,\mathrm{d}z = -\tau$ (with the sign convention that a pulling tension is positive). A protein whose cross-section $A(z)$ changes with depth in a conformational change exchanges work with this profile (Cantor 1997).

**Formula 25.4.2 (Lateral Pressure and Conformational Free Energy)** If a membrane protein's cross-sectional area at depth $z$ changes by $\Delta A(z)$ in a transition, the bilayer contributes

$$
\Delta G_{\mathrm{lat}} = -\int p(z)\,\Delta A(z)\,\mathrm{d}z \tag{25.9}
$$
to its free energy; for a uniform area change this reduces to $-\tau\Delta A$ as in Formula 25.4.1. The first moment of the profile of each monolayer, $\int z\,p(z)\,\mathrm{d}z$, equals (up to sign convention) the product of its bending rigidity and spontaneous curvature.

A channel that widens more on one side of the membrane than on the other, as MscL does on opening, is therefore sensitive to the asymmetry of the profile, and lipids that change the spontaneous curvature of one leaflet shift its gating at constant tension. Lipids also act locally: molecular dynamics and structures of MscS show lipid chains occupying pockets between its helices, which leave on opening, so that the channel senses the lipid's free energy in the pocket ("force from lipids"; Pliotas and colleagues 2015). In every case the free energy of the transition contains terms set by the state of the membrane, and the protein is a sensor of membrane mechanics.

## 25.5. The Active Membrane: Safety Valves

When a bacterium is moved from a concentrated medium to fresh water, the osmotic difference across its membrane, $RT\Delta c \approx 0.9\,\mathrm{MPa}$ for $350\,\mathrm{mM}$, drives water in. The cell wall carries most of the turgor, but the cytoplasmic membrane is stretched, and a bilayer breaks at an areal strain of only $2$–$5\,\%$, at $5$–$15\,\mathrm{mN\,m^{-1}}$ ([7.6.24](/7.6.24#sec-24.3.1)). MscS and MscL open close to these tensions and release small solutes; cells lacking both channels (and the related MscK) lyse after a downshock that wild-type cells survive (Levina and colleagues 1999). How many channels does a cell need, and how fast must they act?

**Formula 25.5.1 (Solute Release Through Open Channels)** If $N$ channels with open probability $p_{\mathrm{o}}(\tau)$ each pass a solute with permeability $P_{\mathrm{ch}}$ (volume per time), the internal amount $n$ of the solute in a cell of volume $V$ changes as

$$
\frac{\mathrm{d}n}{\mathrm{d}t} = -N p_{\mathrm{o}}(\tau)P_{\mathrm{ch}}\left(\frac{n}{V} - c_{\mathrm{out}}\right), \qquad P_{\mathrm{ch}} \approx \frac{D\pi a^2}{\ell} \tag{25.10}
$$
for a pore of radius $a$ and length $\ell$, with the solute diffusion coefficient $D$ (diffusion through a cylinder, Fick's first law).

**Example 25.5.1 (One open MscL empties a cell in a second)** For a pore of radius $1.5\,\mathrm{nm}$ and length $5\,\mathrm{nm}$ and $D = 10^{-9}\,\mathrm{m^2\,s^{-1}}$, $P_{\mathrm{ch}} = 10^{-9} \times \pi(1.5\times10^{-9})^2/5\times10^{-9} = 1.4\times10^{-18}\,\mathrm{m^3\,s^{-1}}$, or $1.4\,\mathrm{fL\,s^{-1}}$. A cell of $1\,\mathrm{fL}$ with $350\,\mathrm{mM}$ excess osmolyte holds $2\times10^8$ excess solute molecules, and one open MscL releases them at $1.4\times10^{-18} \times 350 \times 6\times10^{23} \approx 3\times10^8$ per second. The time constant $V/NP_{\mathrm{ch}}$ is about $0.7\,\mathrm{s}$ for one channel and $7\,\mathrm{ms}$ for a hundred, short enough to compete with the entry of water, which swells the cell by a few percent in tens of milliseconds. The large conductance of MscL, about $3\,\mathrm{nS}$, is the electrical face of the same large pore.

**Example 25.5.2 (An osmotic downshock)** Combine Eq. (25.10) with water entry, $\mathrm{d}V/\mathrm{d}t = L_{\mathrm{p}}A\,(RT\Delta c - 2\tau/r)$, a membrane with $\tau = K_A(A/A_0 - 1)$, $K_A = 0.2\,\mathrm{N\,m^{-1}}$ ([Definition 24.2.2](/7.6.24#def-24.2.2)), and two-state gating of MscS and MscL (Formula 4.2.1). For a wall-less cell of $1\,\mathrm{fL}$ moved from $400$ to $50\,\mathrm{mM}$ (the figure), the membrane without channels reaches the rupture tension in about $80\,\mathrm{ms}$. Twenty MscS channels open at $5$–$6\,\mathrm{mN\,m^{-1}}$ but release solute too slowly, and the cell still lyses. With a hundred MscL in addition, the tension rises to the gating tension of MscL, stops there as the channels open, and the internal osmolyte falls to the external level within about $100\,\mathrm{ms}$: the channels clamp the tension just below rupture. The hierarchy of thresholds makes sense: MscS opens first, at moderate tensions and with a small pore, and MscL opens only in an emergency, losing almost all small metabolites, which the cell must then replace.

Measurements in single *E. coli* cells that relate survival of a downshock to the number of MscL per cell, counted by fluorescence, find that survival becomes likely only with of the order of a hundred or more channels (Chure and colleagues 2018), the number the estimate suggests. The cell has a few hundred, which costs little: MscL is about one protein in ten thousand.

![A toy model of an osmotic downshock (Example 25.5.2). A wall-less spherical cell of 1 fL, with 400 mM internal osmolyte, is moved at t = 0 into 50 mM. Water enters with hydraulic conductivity 3 × 10⁻¹³ m s⁻¹ Pa⁻¹; tension follows the areal strain with K_A = 0.2 N m⁻¹; the bilayer ruptures at 12 mN m⁻¹. Channels open as two-state systems (MscS: τ½ = 5.5 mN m⁻¹, ΔA = 8 nm², permeability 0.3 fL s⁻¹; MscL: τ½ = 10 mN m⁻¹, ΔA = 20 nm², 1.4 fL s⁻¹) and release osmolyte by Formula 25.5.1. A: membrane tension against time for a cell without channels and with 20 MscS (both lyse, crosses) and with 20 MscS and 100 MscL, whose opening clamps the tension below rupture. B: internal osmolyte concentration](./plots/osmotic-downshock.py)

## 25.6. Mechanosensitive Channels in Eukaryotes

### 25.6.1. Two Ways to Deliver Force

Animals and plants use mechanosensitive channels for touch, hearing, balance, proprioception, the sensing of blood flow and pressure, the regulation of cell volume and the gravitropism of roots. Two mechanisms deliver the force to the gate. In the lipid-tension model ("force from lipids"), tension in the bilayer acts directly on a channel whose area or shape changes on opening, as for MscL. In the tether model ("force from filament"), the channel is connected by a protein to the cytoskeleton or the extracellular matrix, and force is transmitted through that connection.

| Channel | Organism and role | Gating | Notes |
|---|---|---|---|
| MscS, MscL | bacteria, osmotic safety valves | lipid tension | 25.4–25.5 |
| Piezo1, Piezo2 | vertebrates: Piezo2 touch and proprioception, Piezo1 blood flow, red-cell volume, vascular development | lipid tension (dome, 25.6.2), modulated by the cytoskeleton | nonselective cation channels |
| K2P (TREK-1, TREK-2, TRAAK) | neurons; hyperpolarize the cell | lipid tension | $\ce{K+}$ channels |
| OSCA / TMEM63 | plants (OSCA, dimer) and animals (TMEM63, monomer) | lipid tension, high threshold | cation channels |
| NOMPC (TRPN) | *Drosophila* touch and hearing | tether: ankyrin-repeat spring to microtubules | 25.6.3 |
| MET channel (TMC1/2 complex) | vertebrate hair cells, hearing and balance | tether: tip link | 25.6.3, [7.6.31](/7.6.31) |
| MEC-4 (DEG/ENaC) | *Caenorhabditis elegans* touch neurons | needs cytoskeleton and matrix | |

### 25.6.2. Piezo: An Elastic Dome

Piezo channels, discovered by Patapoutian and colleagues in 2010 ([7.3.5](/7.3.5#sec-5.7.1)), are trimers of very large subunits: 38 transmembrane helices and about 2500 residues each (Piezo2 more than 2800), about $0.9\,\mathrm{MDa}$ in total. The cryo-electron microscopy structures (Guo and MacKinnon 2017; Saotome and colleagues 2018; Wang and colleagues 2019 for Piezo2) show three curved blades of helix bundles arranged like a propeller around a central pore, with an extracellular cap. The blades do not lie in a plane: they bend the membrane into a bowl about $24\,\mathrm{nm}$ across and $9\,\mathrm{nm}$ deep that bulges into the cytoplasm, with a radius of curvature of about $10$–$12\,\mathrm{nm}$. Long beam helices under the blades run toward the pore and act as levers that couple the large movement of the blades to a modest opening of the gate. In liposomes under tension Piezo1 flattens, and the projected area of the channel and the membrane it bends increases by about $300\,\mathrm{nm^2}$ (Yang and colleagues 2022).

A projected-area change of this size explains the sensitivity of Piezo. By the two-state formula, $\tau_{1/2} = \Delta G_0/\Delta A$; with $\Delta A$ ten times that of MscL, a channel that resists opening by tens of $k_{\mathrm{B}}T$ is half open at tensions ten times lower, $1$–$3\,\mathrm{mN\,m^{-1}}$, which occur in physiology. From the measured elastic response of the Piezo1–membrane system, flattening by $10\,\mathrm{nm}$ needs about $90\,\mathrm{pN}$ and $570\,\mathrm{pN\,nm}$ of work, and $W/\Delta A = 570/300 \approx 1.9\,\mathrm{pN\,nm^{-1}} = 1.9\,\mathrm{mN\,m^{-1}}$, close to the measured half-activation tension of about $1.4\,\mathrm{mN\,m^{-1}}$ (Lewis and Grandl 2015). The membrane around the dome, its "footprint", is part of the elastic object: the deformation extends tens of nanometers beyond the protein, so the area that changes is larger than the protein itself (Haselwandter and MacKinnon 2018). A toy model shows how such a dome responds to tension.

**Theorem 25.6.1 (Flattening of an Elastic Dome)** Let a channel and the membrane it deforms form a spherical cap of fixed area $A_{\mathrm{d}}$ and mean curvature $c$, with bending energy $2\kappa A_{\mathrm{d}}(c - c_i)^2$ about a preferred curvature $c_i$. Its projected area is $A_{\mathrm{p}} = A_{\mathrm{d}}(1 - A_{\mathrm{d}}c^2/4\pi)$. Under tension $\tau$, the curvature that minimizes $G = 2\kappa A_{\mathrm{d}}(c - c_i)^2 - \tau A_{\mathrm{p}}$ is

$$
c^* = \frac{c_i}{1 + \tau/\tau_{\mathrm{d}}}, \qquad \tau_{\mathrm{d}} = \frac{8\pi\kappa}{A_{\mathrm{d}}}, \tag{25.11}
$$
and the minimum free energy is $G^*(\tau) = 2\kappa A_{\mathrm{d}}c_i^2\,\dfrac{\tau/\tau_{\mathrm{d}}}{1 + \tau/\tau_{\mathrm{d}}} - \tau A_{\mathrm{d}}$.

**Proof** For a cap of radius $R = 1/c$ and half-angle $\theta$, $A_{\mathrm{d}} = 2\pi R^2(1 - \cos\theta)$ and $A_{\mathrm{p}} = \pi R^2\sin^2\theta$. Eliminating $\cos\theta = 1 - A_{\mathrm{d}}c^2/2\pi$ gives $A_{\mathrm{p}} = (\pi/c^2)[1 - (1 - A_{\mathrm{d}}c^2/2\pi)^2] = A_{\mathrm{d}} - A_{\mathrm{d}}^2c^2/4\pi$. The energy $G = A_{\mathrm{d}}[2\kappa(c - c_i)^2 + \tau A_{\mathrm{d}}c^2/4\pi] - \tau A_{\mathrm{d}}$ is quadratic in $c$, $a(c - c_i)^2 + bc^2$ with $a = 2\kappa$, $b = \tau A_{\mathrm{d}}/4\pi$; its minimum is at $c^* = ac_i/(a + b)$ with value $abc_i^2/(a + b)$, which are the stated expressions since $b/a = \tau/\tau_{\mathrm{d}}$. $\square$

The dome flattens gradually, halfway at $\tau_{\mathrm{d}}$: with $\kappa = 20\,k_{\mathrm{B}}T$ and $A_{\mathrm{d}} = 700\,\mathrm{nm^2}$, $\tau_{\mathrm{d}} = 0.72\,k_{\mathrm{B}}T\,\mathrm{nm^{-2}} = 2.9\,\mathrm{mN\,m^{-1}}$, in the physiological range, and flattening it completely from $c_i = (12\,\mathrm{nm})^{-1}$ releases $A_{\mathrm{d}}^2c_i^2/4\pi = 270\,\mathrm{nm^2}$ of projected area against $2\kappa A_{\mathrm{d}}c_i^2 \approx 190\,k_{\mathrm{B}}T$ ($800\,\mathrm{pN\,nm}$) of bending energy, numbers of the size estimated from experiment. If the open state is a flatter dome ($c_i = (25\,\mathrm{nm})^{-1}$) and the closed state a more curved one, the gating free energy $\Delta G(\tau) = \Delta G_0 + G^*_{\mathrm{o}}(\tau) - G^*_{\mathrm{c}}(\tau)$ is not linear in tension: the effective area change $\Delta A_{\mathrm{eff}} = -\mathrm{d}\Delta G/\mathrm{d}\tau$ is about $210\,\mathrm{nm^2}$ at zero tension and falls to about $100\,\mathrm{nm^2}$ at $1.4\,\mathrm{mN\,m^{-1}}$, because the closed dome flattens partway before the channel opens. The model is steeper than measured gating curves of Piezo1 in cells, which are broadened by the heterogeneity of local tension, by the cytoskeleton that shields or focuses stress, and by fast inactivation (within tens of milliseconds); but it shows why a curved channel is a sensitive tension sensor, and why its sensitivity depends on the shape and stiffness of the membrane around it.

![A toy elastic dome for Piezo (Theorem 25.6.1; dome area 700 nm², κ = 20 k_BT, closed preferred curvature 1/(12 nm), open 1/(25 nm), gating free energy chosen to give half opening at 1.4 mN m⁻¹). A: profile of the closed dome, bulging into the cytoplasm, at three tensions: 9.3, 6.3 and 3.4 nm deep. B: projected area gained by each state relative to zero tension, and the effective area change of gating, which shrinks as both states flatten (τ_d = 8πκ/A_d = 2.9 mN m⁻¹ marked). C: log-odds of opening: curved for the dome model, whose slope ΔA_eff/k_BT decreases with tension, straight for a two-state channel with constant area change](./plots/piezo-dome.py)

### 25.6.3. Tethered Channels: Hair Cells and NOMPC

The mechano-electrical transduction channel of the hair cells of the inner ear is the classic tethered channel. Each hair cell carries a bundle of stereocilia (actin-filled microvilli, [7.6.26](/7.6.26)) in rows of increasing height. The tip of each stereocilium is connected to the side of its taller neighbor by a tip link, a filament of two cadherins, cadherin-23 above and protocadherin-15 below, each a parallel dimer. Deflecting the bundle toward the tall edge stretches the tip links and opens channels at their lower ends within microseconds, far faster than any second-messenger pathway. The pore-forming subunits are thought to be TMC1 and TMC2 (transmembrane channel-like proteins, identified as deafness genes in 2002), assembled with TMIE, LHFPL5 (TMHS), CIB2 and protocadherin-15; the structure of the homologous complex of *C. elegans* (TMC-1 with TMIE and the calcium-binding protein CALM-1) has been determined by cryo-electron microscopy (Jeong and colleagues 2022). How the tip link pulls on the gate is not yet known. Mechanically, the tip link and whatever lies in series with it act as a gating spring, and the opening of the channel shortens the spring, so that channel gating feeds back on the stiffness of the bundle and even makes it negative over a range of displacements; this, the amplification it allows and the active oscillations of the bundle are treated with the mechanics of whole cells in [7.6.31](/7.6.31).

NOMPC, a TRP channel required for gentle touch in *Drosophila*, makes the tether visible. Its cryo-EM structure (Jin and colleagues 2017) shows each of the four subunits with 29 ankyrin repeats that together form a helical bundle connecting the channel to the microtubules beneath the membrane. The bundle behaves like a compression spring: pushing the membrane toward the microtubules compresses it and rotates the channel's gate. Both examples follow the same logic as MscL and Piezo: a conformational change of the channel moves an element on which an external force does work, and the open probability is a Boltzmann function of that work. They differ in where the force comes from, the bilayer or a protein in series.

## Summary

| Topic | Key result |
|---|---|
| Mismatch (Definition 25.1.1) | Hydrophobic belts of proteins and bilayer cores are both about $3$–$3.5\,\mathrm{nm}$; $U = W/2 - w_0$; exposing hydrophobic surface costs far more than deforming lipids |
| Energy (Eq. (25.1), Formula 25.2.1) | Midplane and thickness modes decouple; thickness costs $\frac{\kappa}{2}(u'')^2 + \frac{K_t}{2w_0^2}u^2$ per area |
| Profile and line tension (Theorem 25.2.1) | $\kappa u'''' + (K_t/w_0^2)u = 0$; $u = U\mathrm{e}^{-y}(\cos y + \sin y)$, decay length $\lambda^{-1} = (\kappa w_0^2/K_t)^{1/4} \approx 1\,\mathrm{nm}$; $f = \frac12\mathcal{K}U^2$, $\mathcal{K} \approx 20$–$30\,k_{\mathrm{B}}T\,\mathrm{nm^{-3}}$; bending:compression $= 1:3$ |
| Numbers (Example 25.2.1, 25.2.3) | $U = 0.3\,\mathrm{nm}$: $f \approx 1.3\,k_{\mathrm{B}}T\,\mathrm{nm^{-1}}$, $\approx 20\,k_{\mathrm{B}}T$ around a $2.5\,\mathrm{nm}$ protein; the 2D energy exceeds $2\pi Rf$ by $\sim 30\,\%$ at $\lambda R \approx 2$ |
| Tests (25.2.4) | Gramicidin lifetimes fall with bilayer thickness; MscL gating rises with chain length; plasma-membrane TMDs are longer than ER/Golgi TMDs |
| Interactions (Formula 25.3.1, 25.3.2) | Like inclusions attract ($-2f$ per contact length), unlike repel; oscillation with period $2\sqrt2\pi/\lambda$; curvature forces $\propto r^{-4}$, fluctuation attraction |
| MscL model (Formula 25.4.1, Theorem 25.4.1) | $G = G_{\mathrm{p}} + 2\pi Rf - \pi R^2\tau$; $\tau^* = \mathcal{K}U^2/(R_{\mathrm{o}} + R_{\mathrm{c}})$, $\Delta G_0 = \pi\mathcal{K}U^2(R_{\mathrm{o}} - R_{\mathrm{c}})$; PC16→PC20: $5 \to 20\,k_{\mathrm{B}}T$ (measured $4 \to 24$) |
| Pressure to tension (Example 25.4.1) | $\tau = \Delta p\,r_{\mathrm{c}}/2$; the radius of curvature of the patch dominates the error |
| Lateral pressure (Formula 25.4.2) | $\Delta G_{\mathrm{lat}} = -\int p(z)\Delta A(z)\,\mathrm{d}z$; asymmetric lipids (LPC) open MscL at zero tension |
| Safety valves (Formula 25.5.1, Examples 25.5.1–25.5.2) | $P_{\mathrm{ch}} = D\pi a^2/\ell \approx 1.4\,\mathrm{fL\,s^{-1}}$ per MscL: one channel empties $1\,\mathrm{fL}$ in $\sim 1\,\mathrm{s}$; $\sim 100$ channels clamp the tension below rupture within $\sim 100\,\mathrm{ms}$ |
| Eukaryotic channels (25.6.1) | Lipid tension (Piezo, K2P, OSCA/TMEM63) or tethers (hair-cell MET, NOMPC) |
| Piezo dome (Theorem 25.6.1) | $c^* = c_i/(1 + \tau/\tau_{\mathrm{d}})$, $\tau_{\mathrm{d}} = 8\pi\kappa/A_{\mathrm{d}} \approx 3\,\mathrm{mN\,m^{-1}}$; $\Delta A \sim 10^2\,\mathrm{nm^2}$, so $\tau_{1/2} \approx 1$–$2\,\mathrm{mN\,m^{-1}}$; the effective area change falls with tension |

## Questions

1. How does the decay length $\lambda^{-1}$ of the thickness deformation change if the bending rigidity doubles, for example by adding cholesterol, and by how much does the line tension change, at fixed $K_t$ and $w_0$?

   **Answer** $\lambda^{-1} = (\kappa w_0^2/K_t)^{1/4} \propto \kappa^{1/4}$, so it grows by $2^{1/4} = 1.19$, from $1.0$ to $1.2\,\mathrm{nm}$. The line tension $f = \frac12\mathcal{K}U^2$ with $\mathcal{K} \propto \kappa^{1/4}$ also grows by $19\,\%$. Cholesterol in fact also thickens the bilayer and raises $K_A$ and $K_t$, so its net effect on a given protein depends on how it changes $U$, which enters squared.

2. Show from the proof of Theorem 25.2.1 that the bending energy is one quarter of the total. Why is the deformation not simply exponential?

   **Answer** With $g = \mathrm{e}^{-y}(\cos y + \sin y)$, the bending term is $\frac{\sqrt2}{8}K_tU^2/\lambda w_0^2$ and the compression term $\frac{3\sqrt2}{8}K_tU^2/\lambda w_0^2$, a ratio $1:3$, so bending is one quarter. A pure exponential $U\mathrm{e}^{-x/x_0}$ would violate the condition $u'(R) = 0$; the fourth-order equation admits two decaying solutions, and satisfying both gluing conditions requires a combination that oscillates. A trial exponential (with $u'(R) \ne 0$) gives a higher energy, as a variational calculation confirms.

3. By what factor should the critical tension of MscL change between PC16 and PC20 according to Theorem 25.4.1, and how does this compare with the measured half-activation pressures?

   **Answer** $\tau^* \propto U^2 \propto (12 - n)^2$: $(8/4)^2 = 4$, from $0.23$ to $0.93\,k_{\mathrm{B}}T\,\mathrm{nm^{-2}}$. The measured pressures rise from $24$ to $72\,\mathrm{mmHg}$, a factor 3; if the patch geometry is the same, tension is proportional to pressure, so the model overestimates the dependence somewhat, plausibly because the open channel is thinner than the closed one (its mismatch changes on opening), which the model ignores.

4. In a patch-clamp experiment MscL in PC18 is half open at $42\,\mathrm{mmHg}$. What radius of curvature of the patch would make this agree with $\tau^* = 2.2\,\mathrm{mN\,m^{-1}}$? Is it plausible?

   **Answer** $r_{\mathrm{c}} = 2\tau/\Delta p = 2 \times 2.2\times10^{-3}/5.6\times10^3\,\mathrm{m} = 0.8\,\mu\mathrm{m}$. Patch pipettes have tip radii of about $0.5$–$1\,\mu\mathrm{m}$, and a patch sucked into the pipette has a radius of curvature of the same order or somewhat larger, so the agreement is reasonable; a radius of $3\,\mu\mathrm{m}$ would give $8\,\mathrm{mN\,m^{-1}}$, closer to native MscL. The example shows why absolute tensions from patch clamp are uncertain by a factor of 2–3.

5. Two identical proteins with $U = 0.4\,\mathrm{nm}$ in the bilayer of Example 25.2.1 come into contact over an effective length of $1.5\,\mathrm{nm}$. Estimate the attraction. Would a protein with $U = -0.4\,\mathrm{nm}$ join their cluster?

   **Answer** $f = \frac12 \times 28 \times 0.16 = 2.2\,k_{\mathrm{B}}T\,\mathrm{nm^{-1}}$; at contact the interaction is $-2f$ per unit length (Formula 25.3.1), $-2 \times 2.2 \times 1.5 \approx -7\,k_{\mathrm{B}}T$, enough to hold the pair together for a long time at room temperature. A protein of opposite mismatch is repelled at short range (the bilayer would have to change thickness by $0.8\,\mathrm{nm}$ over a nanometer), so it stays outside the cluster; mismatch thus sorts proteins by hydrophobic thickness.

6. Estimate how many MscL channels must be open to release, within $20\,\mathrm{ms}$, $90\,\%$ of the excess osmolyte of a $1\,\mathrm{fL}$ cell.

   **Answer** Eq. (25.10) gives exponential decay of the excess with time constant $T = V/NP_{\mathrm{ch}}$; $90\,\%$ release needs $t = T\ln 10 = 2.3T \le 20\,\mathrm{ms}$, so $T \le 8.7\,\mathrm{ms}$ and $N \ge V/(P_{\mathrm{ch}}T) = 10^{-18}/(1.4\times10^{-18} \times 8.7\times10^{-3}) \approx 80$. Of the order of a hundred open channels are needed, consistent with the copy numbers needed for survival.

7. Why can Piezo1 be half activated at about $1.4\,\mathrm{mN\,m^{-1}}$ while MscL needs about $10\,\mathrm{mN\,m^{-1}}$, even if both resist opening by similar free energies?

   **Answer** For a two-state channel $\tau_{1/2} = \Delta G_0/\Delta A$. MscL changes its in-plane area by about $20\,\mathrm{nm^2}$; flattening the Piezo dome and its membrane footprint changes the projected area by hundreds of square nanometers. With $\Delta G_0 \approx 50\,k_{\mathrm{B}}T$, $\Delta A = 150\,\mathrm{nm^2}$ gives $\tau_{1/2} = 0.33\,k_{\mathrm{B}}T\,\mathrm{nm^{-2}} = 1.4\,\mathrm{mN\,m^{-1}}$, whereas $20\,\mathrm{nm^2}$ gives $10\,\mathrm{mN\,m^{-1}}$. The large curved structure is a lever that collects work from a large area; MscL, an emergency valve, must not open at ordinary tensions.

8. In Theorem 25.6.1, how does the tension at which the dome is half flattened depend on the dome's area and on the bending rigidity? What would happen to the sensitivity of Piezo in a stiffer membrane, for example one rich in cholesterol?

   **Answer** $\tau_{\mathrm{d}} = 8\pi\kappa/A_{\mathrm{d}}$: proportional to $\kappa$ and inversely proportional to the area of the dome and its footprint. In a stiffer membrane the dome flattens at higher tension, so the channel becomes less sensitive (unless the stiffer membrane also enlarges the footprint, which grows with $\sqrt{\kappa/\tau}$). Cholesterol depletion and stiffening lipids do modulate Piezo1 in experiments, in the directions such arguments suggest, although cholesterol also acts on the channel directly.

9. (Experimental design) Propose an experiment, using gramicidin A, to test whether a new drug changes the elastic properties of bilayers rather than binding a specific target.

   **Answer** Form planar bilayers of defined lipid composition (for example DOPC with and without the drug in the aqueous phase or in the membrane), add gramicidin A at very low concentration, and record single-channel events under voltage clamp. Measure the mean channel lifetime and the frequency of channel appearances, which reflect the dimerization free energy. A drug that softens the bilayer or thins it toward the length of the dimer reduces the deformation energy and prolongs lifetimes and raises appearance rates; the effect should scale with the drug's membrane partitioning and appear with enantiomeric gramicidin (all chiralities inverted), which excludes stereospecific binding. Controls: a thicker or thinner lipid (changing $U$) should shift the response as predicted by $f \propto U^2$, and a second, structurally unrelated reporter (such as MscL in liposomes) should show a change of gating in the direction predicted by the same elastic changes.

10. Adding lysophosphatidylcholine to one leaflet opens MscL without tension, but adding it to both leaflets does not. Explain with the lateral pressure profile.

    **Answer** Lysophosphatidylcholine has a large head group and one chain, so it gives a monolayer positive spontaneous curvature and changes the pressure profile on its own side: more head-group repulsion, less chain pressure. Inserted asymmetrically, it makes the profile asymmetric; MscL widens more on one side on opening, so by Formula 25.4.2 the asymmetric change in $p(z)$ does net work on the transition, $-\int p(z)\Delta A(z)\,\mathrm{d}z$, and can favor the open state at zero mean tension. In both leaflets the changes are symmetric, the monolayer curvatures cancel for the bilayer, and the first moments that couple to the channel's asymmetric shape change cancel too; what remains (a slightly thinner, softer bilayer) is not enough to open the channel.
