---
title: "Protein Function: Ligand Binding, Oxygen Transport, and Antibodies"
description: Reversible binding, dissociation constants and binding curves; myoglobin and heme; why a carrier must be cooperative; hemoglobin's T and R states, the Hill equation and the MWC and sequential models; the Bohr effect, CO2, BPG, fetal hemoglobin, carbon monoxide and sickle cell anemia; antibodies, immunoassays and ELISA standard curves; actin, myosin and ATP-modulated binding.
---

**Proteins** work by binding other molecules. In **enzymes** the bound molecule is chemically transformed ([7.1.8](/7.1.8)); in this chapter it is not, and the function lies in the binding itself: storing and transporting oxygen, recognizing a pathogen, pulling on a filament. These transient interactions are organized by a few principles that continue the main line of Part I from structure to function. Binding is reversible and can be described by an equilibrium constant; the binding site is chemically complementary to its ligand; proteins are flexible, and binding is often coupled to a conformational change; in a multisubunit protein a conformational change in one **subunit** affects the others; and binding can be regulated. Myoglobin and hemoglobin, the first proteins whose structures were solved ([7.1.5](/7.1.5#sec-5.4.1), [7.1.5](/7.1.5#sec-5.5.1)), illustrate every one of these principles, and their quantitative description (the Hill equation and the concerted model of Monod, Wyman and Changeux) is the template for **allosteric enzymes** ([7.1.9](/7.1.9)) and for cooperative switches throughout biology. Antibodies show how specificity is achieved by complementary surfaces, and the actin–myosin system how chemical energy can modulate binding.

## 7.1. Reversible Binding of a Protein to a Ligand

### 7.1.1. Ligands and Binding Sites

**Definition 7.1.1 (Ligand)** A **ligand** is a molecule bound reversibly by a protein, and the region of the protein where it binds is the **binding site**.

A ligand may be anything from an ion or a small molecule to another protein. The term is wider than the **ligand** of coordination chemistry ([6.1.5](/6.1.5)), an atom or group bonded to a central metal, although the two meet in heme proteins, where $\ce{O2}$ is both. Binding uses only **noncovalent interactions**, which keeps it transient and lets organisms respond rapidly and reversibly to changing conditions. A binding site is complementary to its ligand in size, shape, charge and hydrophobic or hydrophilic character, so it discriminates among thousands of different molecules; a protein may have separate sites for several ligands. Three views of how complementarity arises are now distinguished:

- *lock and key* (Emil Fischer, 1894): binding site and ligand are complementary in advance;
- *induced fit* (Daniel Koshland, 1958): binding induces a conformational change that makes the site more complementary and the binding tighter; both protein and ligand may change;
- *conformational selection*: the free protein already samples several conformations, and the ligand binds preferentially to one of them and shifts the population towards it. The concerted model of §7.3.5 is of this type, and most real interactions combine the last two mechanisms.

### 7.1.2. The Dissociation Constant

For a protein P with one binding site,

$$
\ce{P + L <=>[k_\mathrm{on}][k_\mathrm{off}] PL}, \qquad
K_\mathrm{d} = \frac{[\mathrm{P}][\mathrm{L}]}{[\mathrm{PL}]} = \frac{k_\mathrm{off}}{k_\mathrm{on}} ,
$$
where the association rate constant $k_\mathrm{on}$ (second order, $\mathrm{M^{-1}\,s^{-1}}$) and the dissociation rate constant $k_\mathrm{off}$ (first order, $\mathrm{s^{-1}}$) are equal at equilibrium by the law of mass action ([6.1.7](/6.1.7)).

**Definition 7.1.2 (Dissociation Constant)** The **dissociation constant** $K_\mathrm{d}$ of a protein–ligand complex is the equilibrium constant for its dissociation; it has the dimension of concentration and equals the free ligand concentration at which half of the binding sites are occupied. The **fractional saturation** $\theta$ is the fraction of binding sites occupied by ligand.

**Remark 7.1.1** Many textbooks (including Lehninger) also use the association constant $K_\mathrm{a} = 1/K_\mathrm{d}$, but on this site $K_\mathrm{a}$ is reserved for the **acid dissociation constant** ([6.1.9](/6.1.9)); we always use $K_\mathrm{d}$, for which a smaller value means a tighter binding. Equilibrium constants are written with a capital $K$, rate constants with a lowercase $k$.

Eliminating $[\mathrm{PL}] = [\mathrm{P}][\mathrm{L}]/K_\mathrm{d}$ from $\theta = [\mathrm{PL}]/([\mathrm{PL}] + [\mathrm{P}])$ gives the binding curve.

**Formula 7.1.1 (Binding Curve)** For a single class of independent sites,

$$
\theta = \frac{[\mathrm{L}]}{[\mathrm{L}] + K_\mathrm{d}} ,
$$
where $[\mathrm{L}]$ is the concentration of *free* ligand.

The curve is a rectangular hyperbola with horizontal asymptote $\theta = 1$ (and a vertical asymptote at $[\mathrm{L}] = -K_\mathrm{d}$, outside the physical range). Its form is the same as that of the **Michaelis–Menten equation** ([6.3.17](/6.3.17)) and the **Langmuir isotherm** ([6.3.20](/6.3.20)); all three describe saturation of independent sites. Two practical consequences: occupancy rises from $10\%$ to $90\%$ only when $[\mathrm{L}]$ rises from $K_\mathrm{d}/9$ to $9K_\mathrm{d}$, a factor of $81$; and solving for $[\mathrm{L}]$ gives $[\mathrm{L}] = \theta K_\mathrm{d}/(1 - \theta)$.

**Example 7.1.1** A protein has $K_\mathrm{d} = 2.0\ \mu\mathrm{M}$. The free ligand concentration needed for $\theta = 0.6$ is $[\mathrm{L}] = 0.6 \times 2.0\ \mu\mathrm{M}/0.4 = 3.0\ \mu\mathrm{M}$.

Formula 7.1.1 assumes that binding does not appreciably deplete the free ligand, which holds when the total ligand concentration greatly exceeds the concentration of sites, as for most ligands in cells. When the protein concentration $[\mathrm{P}]_\mathrm{T}$ is comparable to $K_\mathrm{d}$ (typical in titrations of tight binders), the mass balances lead to a quadratic,

$$
[\mathrm{PL}] = \frac{[\mathrm{P}]_\mathrm{T} + [\mathrm{L}]_\mathrm{T} + K_\mathrm{d} - \sqrt{([\mathrm{P}]_\mathrm{T} + [\mathrm{L}]_\mathrm{T} + K_\mathrm{d})^2 - 4[\mathrm{P}]_\mathrm{T}[\mathrm{L}]_\mathrm{T}}}{2} ,
$$
which must be fitted instead. In all cases parameters are best obtained by **nonlinear regression** ([3.3.6](/3.3.6)) of the untransformed data; linearizations such as the Scatchard plot ($[\mathrm{PL}]/[\mathrm{L}]$ against $[\mathrm{PL}]$) distort the errors.

*Thermodynamics and kinetics of binding.* The standard Gibbs energy of binding follows from $K_\mathrm{d}$ referred to the standard concentration $c^\circ = 1\ \mathrm{M}$:

$$
\Delta_{\mathrm{bind}}G^\circ = RT\ln\frac{K_\mathrm{d}}{c^\circ} .
$$
At $25\ ^\circ\mathrm{C}$ ($RT = 2.48\ \mathrm{kJ\,mol^{-1}}$), each factor of $10$ in $K_\mathrm{d}$ is worth $5.7\ \mathrm{kJ\,mol^{-1}}$, and $K_\mathrm{d} = 10^{-10}\ \mathrm{M}$ corresponds to $-57\ \mathrm{kJ\,mol^{-1}}$. On the kinetic side, $k_\mathrm{on}$ cannot exceed the limit set by diffusion, about $10^8$–$10^9\ \mathrm{M^{-1}\,s^{-1}}$ for a protein and a small ligand (a **diffusion-controlled reaction**, [6.3.17](/6.3.17)); most protein–protein associations are slower, $10^5$–$10^7\ \mathrm{M^{-1}\,s^{-1}}$. Tight binding therefore mainly means slow dissociation: the mean lifetime of the complex (residence time) is $\tau = 1/k_\mathrm{off} = 1/(k_\mathrm{on}K_\mathrm{d})$; for $K_\mathrm{d} = 1\ \mathrm{nM}$ and $k_\mathrm{on} = 10^7\ \mathrm{M^{-1}\,s^{-1}}$, $k_\mathrm{off} = 0.01\ \mathrm{s^{-1}}$ and $\tau = 100\ \mathrm{s}$.

The same two constants set how fast binding reaches equilibrium. With the ligand in excess, $[\mathrm{L}]$ stays constant, and $\mathrm{d}[\mathrm{PL}]/\mathrm{d}t = k_\mathrm{on}[\mathrm{P}][\mathrm{L}] - k_\mathrm{off}[\mathrm{PL}]$ is linear in $[\mathrm{PL}]$ (pseudo-first order). Starting from free protein,

$$
\theta(t) = \theta_\mathrm{eq}\left(1 - \mathrm{e}^{-k_\mathrm{obs}t}\right), \qquad k_\mathrm{obs} = k_\mathrm{on}[\mathrm{L}] + k_\mathrm{off} ,
$$
so the approach to equilibrium is always faster than dissociation alone, and the measured $k_\mathrm{obs}$ plotted against $[\mathrm{L}]$ is a straight line with slope $k_\mathrm{on}$ and intercept $k_\mathrm{off}$: this is how stopped-flow and surface plasmon resonance experiments obtain both rate constants.

![Binding kinetics and equilibrium for P + L ⇌ PL with the ligand in excess (illustrative k_on = 10⁷ M⁻¹ s⁻¹, k_off = 0.1 s⁻¹, so K_d = 10 nM). A: fraction of sites occupied after mixing at [L] = 0.3, 1, 3 and 10 K_d; each curve rises exponentially to its equilibrium value (dotted), faster at higher [L]. B: the observed rate constant k_obs = k_on[L] + k_off is linear in [L], with slope k_on and intercept k_off. C: the equilibrium binding curve (Formula 7.1.1) on a logarithmic axis: occupancy rises from 10 % to 90 % over an 81-fold range of [L] (shaded)](./plots/binding-kinetics.py)

| Protein | Ligand | $K_\mathrm{d}$ / M |
|---|---|---|
| Avidin (egg white) | **biotin** | $1 \times 10^{-15}$ |
| **Insulin receptor** (human) | **insulin** | $1 \times 10^{-10}$ |
| Anti-HIV immunoglobulin (human) | gp41 (HIV-1 surface protein) | $4 \times 10^{-10}$ |
| Nickel-binding protein (*E. coli*) | $\mathrm{Ni^{2+}}$ | $1 \times 10^{-7}$ |
| **Calmodulin** (rat), four sites | $\mathrm{Ca^{2+}}$ | $3 \times 10^{-6}$ to $2 \times 10^{-5}$ |

As a rule of thumb, binding with $K_\mathrm{d} < 10\ \mathrm{nM}$ is strong and binding with $K_\mathrm{d} > 10\ \mu\mathrm{M}$ weak; **receptor**–**hormone** and antibody–antigen interactions lie at the strong end, enzyme–**substrate** interactions typically in the micromolar to millimolar range. A reported $K_\mathrm{d}$ holds only for the conditions of its measurement: salt concentration and pH can change it by orders of magnitude.

## 7.2. Myoglobin: Oxygen Storage by Heme

### 7.2.1. Heme

Oxygen is poorly soluble in water, and diffusion is ineffective over distances of more than a few millimeters, so large animals need proteins that carry and store it. No amino acid **side chain** binds $\ce{O2}$ reversibly; certain transition metals (iron, copper) do, but free iron generates highly **reactive oxygen species** (the hydroxyl radical, by the Fenton reaction) that damage **DNA** and other **macromolecules**. The solution is to bind the iron in a protein-bound **prosthetic group**.

**Definition 7.2.1 (Heme)** **Heme** is the prosthetic group of the globins and cytochromes: protoporphyrin IX, a ring of four pyrroles joined by methene bridges, with an iron atom bound by its four nitrogens; in the oxygen-binding globins the iron is in the ferrous ($\mathrm{F\mathrm{e}^{2+}}$) state.

```smiles
CC1=C(CCC(=O)O)C2=CC3=C(CCC(=O)O)C(=C(N3)C=C4C(=C(C(=N4)C=C5C(=C(C(=N5)C=C1N2)C)C=C)C)C=C)C
```

The iron of heme has six coordination positions ([coordination compounds](/6.1.5)): four in the plane of the **porphyrin**, occupied by its nitrogens, and two perpendicular to it. In the globins one axial position is occupied by the imidazole nitrogen of a conserved histidine, the *proximal His*; the other is the binding site for $\ce{O2}$. Only $\mathrm{F\mathrm{e}^{2+}}$ binds $\ce{O2}$ reversibly; the ferric form ($\mathrm{F\mathrm{e}^{3+}}$, as in metmyoglobin) does not. Free heme in oxygenated solution is rapidly oxidized, largely because one $\ce{O2}$ can bridge two hemes and oxidize both irons; the electron-donating porphyrin nitrogens resist oxidation, and burying each heme deep inside the globin prevents the bridging altogether. Oxygen binding changes the electronic structure of the iron and hence its color, from the dark purple of venous blood to the bright red of arterial blood; the intense Soret absorption band moves from about $430\ \mathrm{nm}$ (deoxy) to $414\ \mathrm{nm}$ (oxy), which makes binding easy to follow spectroscopically.

The globins are an ancient family of heme proteins found in all kingdoms, with a conserved **fold** of eight α helices (the globin fold) but much less conserved sequences. The nematode *Caenorhabditis elegans* has $33$ globin **genes**; mammals have at least four kinds: myoglobin in muscle, hemoglobin in erythrocytes, neuroglobin in neurons (protecting against hypoxia and ischemia) and cytoglobin in the walls of blood vessels (involved in regulating nitric oxide).

### 7.2.2. Structure of Myoglobin

Myoglobin (Mb; $M_\mathrm{r}$ $16\,700$, $153$ **residues**, one heme) facilitates $\ce{O2}$ diffusion in muscle and stores $\ce{O2}$; it is particularly abundant in diving mammals such as seals and whales, whose muscles it colors brown. About $78\%$ of its residues are in the eight helices A–H. A residue is named either by its position in the sequence or by its position in a helix: the proximal His is His93 or His F8 (the eighth residue of helix F); the bends between helices are AB, CD, EF, FG and GH. The heme lies in a pocket formed mainly by helices E and F, with His E7 (His64), the *distal His*, on the $\ce{O2}$ side.

### 7.2.3. The Oxygen-Binding Curve

For a gas, the dissolved concentration is proportional to its partial pressure (Henry's law), so the binding curve is written in terms of $p_{\mathrm{O_2}}$, which is easier to control and measure:

$$
\theta = \frac{p_{\mathrm{O_2}}}{p_{\mathrm{O_2}} + p_{50}} ,
$$
where $p_{50}$ is the partial pressure at half-saturation. Myoglobin binds $\ce{O2}$ tightly, with $p_{50} = 0.26\ \mathrm{kPa}$.

### 7.2.4. How the Globin Tunes the Heme: CO and Molecular Breathing

Carbon monoxide has a similar size and shape to $\ce{O2}$ and binds to the same site; it is toxic because it blocks myoglobin, hemoglobin and the heme-containing **cytochrome oxidase** of the **respiratory chain** ([7.1.23](/7.1.23)). Free heme binds CO more than $20\,000$ times more tightly than $\ce{O2}$, but heme in myoglobin only about $40$ times more tightly: the protein selectively increases the affinity for $\ce{O2}$ by a factor of about $500$. The main reason is electrostatic. The $\mathrm{Fe}$–$\ce{O2}$ complex is much more polar than $\mathrm{Fe}$–CO, with partial negative charge on the bound oxygen (partial oxidation of the iron), and it accepts a hydrogen bond from the imidazole N–H of the distal His E7; no such stabilization is available to CO. (In some invertebrate hemoglobins, two hydrogen-bond donors in the pocket even make $\ce{O2}$ bind more tightly than CO.) The older explanation, that the distal His forces CO to bind in a strained, bent geometry, is now considered a minor contribution: spectroscopy and high-resolution structures show that CO in myoglobin is nearly linear and perpendicular to the heme, whereas bound $\ce{O2}$ is naturally bent. The selectivity is physiologically important, because CO is produced in small amounts by heme degradation ([7.1.27](/7.1.27)) and in larger amounts by combustion.

Binding also depends on protein dynamics. The heme is buried, with no permanent channel to the solvent; $\ce{O2}$ enters and leaves through transient cavities created by rapid fluctuations of the side chains ("breathing"), and the distal His swings open and shut a major entry pocket on a nanosecond time scale.

## 7.3. Hemoglobin: Cooperative Oxygen Transport

### 7.3.1. Structure of Hemoglobin

Nearly all the oxygen carried by blood is bound to hemoglobin (Hb) inside erythrocytes, small biconcave cells ($6$–$9\ \mu\mathrm{m}$) that have lost nucleus and mitochondria, live about $120$ days, and contain hemoglobin at about $34\%$ by weight. Adult hemoglobin (HbA; $M_\mathrm{r}$ $64\,500$, diameter about $5.5\ \mathrm{nm}$) is an $\alpha_2\beta_2$ tetramer with one heme per subunit. Both kinds of subunit have the globin fold (the α subunit lacks the short D helix), but fewer than half of their residues are identical, and only $27$ positions are identical in whale myoglobin and the α and β chains of human hemoglobin.

The **quaternary structure** is dominated by contacts between unlike subunits. The $\alpha_1\beta_1$ interface (more than $30$ residues) is so strong that mild urea dissociates the tetramer into αβ dimers that remain intact; the $\alpha_1\beta_2$ interface ($19$ residues) is the one that changes on oxygen binding. Both are stabilized mainly by the **hydrophobic effect**, with many hydrogen bonds and a few ion pairs.

### 7.3.2. The T and R States

**Definition 7.3.1 (T and R States)** Hemoglobin has two major quaternary conformations: the **T state** (originally "tense"), stabilized by a network of ion pairs at the $\alpha_1\beta_2$ and $\alpha_2\beta_1$ interfaces and predominant in deoxyhemoglobin, and the **R state** ("relaxed"), which has a higher affinity for $\ce{O2}$ and is stabilized by $\ce{O2}$ binding.

Oxygen binds to either state, but much more tightly to R. In the $\mathrm{T \to R}$ transition the individual subunits change little; instead the $\alpha\beta$ pairs slide and rotate (by about $15^\circ$) relative to each other, the pocket between the β subunits narrows, and some ion pairs that stabilize T are broken. Among them are the ion pair between His HC3 (His146, the C-terminal residue of the β chain) and Asp FG1 (Asp94) of the same β chain, and the pair between the C-terminal carboxylate of β His HC3 and Lys C5 (Lys40) of the α chain. Max Perutz proposed the trigger: in deoxyhemoglobin the iron (high-spin $\mathrm{F\mathrm{e}^{2+}}$) lies slightly out of the porphyrin plane towards the proximal His and the porphyrin is domed; on $\ce{O2}$ binding the iron becomes low-spin, moves into the plane and pulls the proximal His F8 and the attached helix F with it, and these shifts are transmitted to the $\alpha_1\beta_2$ interface.

### 7.3.3. Why a Transport Protein Must Be Cooperative

Hemoglobin must load $\ce{O2}$ in the lungs, where $p_{\mathrm{O_2}} \approx 13.3\ \mathrm{kPa}$, and unload it in the tissues, where $p_{\mathrm{O_2}} \approx 4\ \mathrm{kPa}$. The fraction of its capacity that a carrier delivers is $\Delta\theta = \theta(p_\mathrm{lung}) - \theta(p_\mathrm{tissue})$. Myoglobin would load fully but release almost nothing: $\Delta\theta = 13.3/13.56 - 4/4.26 = 0.981 - 0.939 = 4\%$. Lowering the affinity of a hyperbolic carrier helps, but only up to a point.

**Proposition 7.3.1 (Best Non-Cooperative Carrier)** Among hyperbolic binding curves $\theta = p/(p + p_{50})$, the delivery between $p_1$ (lungs) and $p_2$ (tissues), $p_1 > p_2$, is maximal for $p_{50} = \sqrt{p_1 p_2}$, and the maximum is

$$
\Delta\theta_{\max} = \frac{\sqrt{p_1} - \sqrt{p_2}}{\sqrt{p_1} + \sqrt{p_2}} .
$$

**Proof** With $K = p_{50}$, $\mathrm{d}\Delta\theta/\mathrm{d}K = -p_1/(p_1 + K)^2 + p_2/(p_2 + K)^2$. Setting it to zero gives $\sqrt{p_2}\,(p_1 + K) = \sqrt{p_1}\,(p_2 + K)$, i.e. $K(\sqrt{p_1} - \sqrt{p_2}) = \sqrt{p_1 p_2}\,(\sqrt{p_1} - \sqrt{p_2})$, so $K = \sqrt{p_1 p_2}$; the derivative is positive below and negative above this value, so it is a maximum. Substituting, $\Delta\theta = \sqrt{p_1}/(\sqrt{p_1} + \sqrt{p_2}) - \sqrt{p_2}/(\sqrt{p_2} + \sqrt{p_1})$. $\square$

For $p_1 = 13.3$ and $p_2 = 4\ \mathrm{kPa}$, the best hyperbolic carrier has $p_{50} = 7.3\ \mathrm{kPa}$ and delivers only $29\%$, and even then it is only $65\%$ saturated in the lungs. Hemoglobin, with $p_{50} \approx 3.5\ \mathrm{kPa}$ but a sigmoid curve, delivers about $36$–$38\%$: in arterial blood it is about $96\%$ saturated, in venous blood about $64\%$, so each $100\ \mathrm{mL}$ of blood releases about one third of its oxygen ($6.5\ \mathrm{mL}$ of $\ce{O2}$). Only a protein whose affinity rises as it becomes loaded, switching from a low-affinity to a high-affinity state over the physiological range, can beat the hyperbolic limit; a single-site protein cannot do this, even if binding changes its conformation, because each molecule binds independently.

![Oxygen binding by myoglobin and hemoglobin. A: saturation curves of myoglobin (hyperbola, p50 = 0.26 kPa) and hemoglobin (sigmoid; concerted model with the illustrative parameters of the next figure, p50 = 3.5 kPa), compared with a hyperbola of the same p50 and the best possible hyperbola (p50 = √(13.3 × 4) = 7.3 kPa, Proposition 7.3.1); dotted lines mark p_O2 in the tissues (4 kPa) and the lungs (13.3 kPa). The bars give the fraction of the binding capacity released between lungs and tissues: myoglobin 4 %, hemoglobin 36 %, the hyperbolas 26 % and 29 %. B: Hill plot: myoglobin is a straight line of slope 1; hemoglobin has slope n_H = 3.0 at half-saturation and approaches slope-1 asymptotes at both ends (dashed), which correspond to binding to the pure T state (low affinity, bottom) and the pure R state (high affinity, top)](./plots/oxygen-binding.py)

### 7.3.4. Allostery, Cooperativity and the Hill Equation

**Definition 7.3.2 (Allosteric Protein)** An **allosteric protein** is one in which the binding of a ligand (a *modulator*) to one site affects the binding properties of another site, by changing the conformation of the protein. The interaction is **homotropic** when the modulator is the same molecule as the normal ligand and **heterotropic** when it is a different molecule.

**Definition 7.3.3 (Cooperativity)** Binding to a protein with several sites is **cooperative** when the binding of one ligand changes the affinity of the remaining sites: positively (**positive cooperativity**, sigmoid binding curve) or negatively (**negative cooperativity**).

Cooperative $\ce{O2}$ binding by hemoglobin is homotropic allostery: $\ce{O2}$ is both ligand and activating modulator. Because each subunit has only one $\ce{O2}$ site, the effect is transmitted from subunit to subunit through their interfaces; the first $\ce{O2}$ binds to a T-state subunit with low affinity, and the last to a molecule that is already in the R state, with much higher affinity. A sigmoid binding curve is diagnostic of positive cooperativity.

A. V. Hill (1910) described cooperative binding by the limiting case in which all $n$ ligands bind at once, $\mathrm{P} + n\,\mathrm{L} \rightleftharpoons \mathrm{PL}_n$, which gives $\theta = [\mathrm{L}]^n/([\mathrm{L}]^n + K)$. Because real proteins are never fully cooperative, the exponent is treated as an empirical parameter.

**Formula 7.3.1 (Hill Equation)**

$$
\theta = \frac{[\mathrm{L}]^{n_\mathrm{H}}}{K_{0.5}^{\,n_\mathrm{H}} + [\mathrm{L}]^{n_\mathrm{H}}}, \qquad
\lg\frac{\theta}{1 - \theta} = n_\mathrm{H}\lg[\mathrm{L}] - n_\mathrm{H}\lg K_{0.5} ,
$$
where $K_{0.5}$ is the ligand concentration at half-saturation (for $\ce{O2}$, $p_{50}$ replaces $K_{0.5}$ and $p_{\mathrm{O_2}}$ replaces $[\mathrm{L}]$) and the *Hill coefficient* $n_\mathrm{H}$ is the slope of the *Hill plot* of $\lg[\theta/(1 - \theta)]$ against $\lg[\mathrm{L}]$ at half-saturation.

The Hill coefficient measures the degree of cooperativity, not the number of sites: $n_\mathrm{H} = 1$ means no cooperativity (as for myoglobin, or for a multisubunit protein whose subunits do not communicate), $n_\mathrm{H} > 1$ positive and $n_\mathrm{H} < 1$ negative cooperativity. Its upper limit is the number of sites $n$, reached only if no partly liganded molecules ever existed; for hemoglobin ($n = 4$) the maximum is about $n_\mathrm{H} \approx 3$ (values of $2.8$–$3.0$ are measured). Real Hill plots are straight only near the middle; at very low and very high saturation they approach slope $1$, the behavior of the T and R states alone (panel B of the figure). Cooperativity sharpens the response: the ratio of ligand concentrations needed to go from $10\%$ to $90\%$ saturation is $81^{1/n_\mathrm{H}}$, that is $81$ for a hyperbola but only $81^{1/3} = 4.3$ for $n_\mathrm{H} = 3$. The same mathematics describes cooperativity and ultrasensitivity in enzymes, receptors and gene regulation ([7.1.9](/7.1.9), [7.9](/7.9)).

### 7.3.5. The Concerted and Sequential Models

Two models, both proposed in the 1960s, explain how cooperativity arises from conformational change.

**Definition 7.3.4 (MWC Model)** In the **concerted model** of Monod, Wyman and Changeux (1965; **MWC model**), the subunits of a cooperative protein are functionally identical, each can exist in two conformations, and all subunits change conformation together, so that only the all-T and all-R molecules exist; the two quaternary states are in equilibrium, and the ligand binds to either, but more tightly to R.

Let $L = [\mathrm{T_0}]/[\mathrm{R_0}]$ be the equilibrium constant between the unliganded states, $K_\mathrm{R}$ and $K_\mathrm{T}$ the dissociation constants of a site in R and T, $c = K_\mathrm{R}/K_\mathrm{T} < 1$, and $\alpha = [\mathrm{L}]/K_\mathrm{R}$. Within each quaternary state the four sites are independent, so the statistical weights of all species, relative to $\mathrm{R_0}$, add up to the binding polynomial (partition function; compare the **partition function** of [6.3.10](/6.3.10))

$$
Z = (1 + \alpha)^4 + L(1 + c\alpha)^4 ,
$$
from which every observable follows: the mean number of bound ligands is $\alpha\,\partial\ln Z/\partial\alpha$, so

**Formula 7.3.2 (MWC Binding Curve)**

$$
\theta = \frac{\alpha(1 + \alpha)^3 + Lc\,\alpha(1 + c\alpha)^3}{(1 + \alpha)^4 + L(1 + c\alpha)^4}, \qquad
\bar R = \frac{(1 + \alpha)^4}{(1 + \alpha)^4 + L(1 + c\alpha)^4} ,
$$
where $\bar R$ is the fraction of molecules in the R state.

Each bound ligand multiplies the T/R ratio by $c$, so binding pulls the population from T to R, and the affinity rises. The model is cooperative only if both states matter: for $L \to 0$ (all R) or $L \to \infty$ (all T) or $c = 1$ (equal affinities) the curve becomes a hyperbola. Cooperativity is greatest when the ligand-induced switch happens near half-saturation, which for a tetramer is at $Lc^2 = 1$. The parameters $K_\mathrm{R} = 0.35\ \mathrm{kPa}$, $c = 0.01$ (so $K_\mathrm{T} = 35\ \mathrm{kPa}$) and $L = 10^4$, used for hemoglobin in the figures of this chapter, are illustrative values that reproduce $p_{50} = 3.5\ \mathrm{kPa}$ and $n_\mathrm{H} = 3.0$. In the MWC picture, heterotropic effectors that bind preferentially to T (protons, $\ce{CO2}$, BPG; §7.3.7–7.3.8) act by increasing $L$, which shifts the curve to the right with little change in shape.

![The concerted (MWC) model for a tetramer. A: species of the model: R states (circles) and T states (squares) with 0 to 4 bound ligands (dots); all four subunits switch together, ligand binds R with dissociation constant K_R and T with K_T = K_R/c, and the binding polynomial Z collects the statistical weights. B: saturation θ (solid) and fraction of molecules in the R state (dashed) against α = [L]/K_R for c = 0.01 and L = 1 to 10⁶: increasing L shifts the curve to higher ligand concentrations and, up to a point, makes it more sigmoid; the conformational switch (dashed) precedes saturation. C: Hill coefficient at half-saturation against L for c = 0.01 and c = 0.1: cooperativity is greatest at Lc² = 1 (here L = 10⁴ and 10²) and never reaches the number of sites, 4; the smaller c (the more different the two states), the stronger the cooperativity](./plots/mwc-model.py)

**Definition 7.3.5 (Sequential Model)** In the **sequential model** of Koshland, Némethy and Filmer (1966; **KNF model**), ligand binding induces a conformational change in the subunit to which it binds, and this change alters the conformation, and thus the affinity, of neighboring subunits through their interfaces; molecules with subunits in different conformations exist.

The sequential model has more intermediate states, and the concerted model can be regarded as its all-or-none limit. A qualitative difference is that the sequential model can produce negative cooperativity, which the MWC model, in which binding always pulls towards the high-affinity state, cannot. The two are difficult to distinguish experimentally. For hemoglobin, the concerted quaternary switch explains most of the data, but the affinity of the T state itself also depends on ligation and effectors; modern descriptions (such as the tertiary **two-state model** of Eaton and colleagues) add tertiary conformational changes within each quaternary state. The same models are used for allosteric enzymes in [7.1.9](/7.1.9).

### 7.3.6. Carbon Monoxide Poisoning

Human hemoglobin binds CO about $250$ times more tightly than $\ce{O2}$ (the discrimination is weaker than in myoglobin because the hydrogen bond from the distal His to $\ce{O2}$ is weaker). The complex, carboxyhemoglobin (COHb), accumulates during prolonged exposure to even low concentrations of CO: healthy nonsmokers have $1\%$ or less, smokers $3$–$8\%$ (up to $15\%$ for heavy smokers), and breathing air with $570\ \mathrm{ppm}$ CO for several hours brings COHb to $50\%$. Symptoms appear above about $10$–$15\%$ (headache), become severe at $20$–$30\%$ (nausea, dizziness, confusion), lead to loss of consciousness near $50\%$, and death usually occurs above $60\%$. Treatment is removal from the source and $\ce{O2}$: the half-time for CO release is $2$–$6.5\ \mathrm{h}$ in air, about four times shorter with $100\%\ \ce{O2}$, and tens of minutes with $\ce{O2}$ at $300\ \mathrm{kPa}$ (hyperbaric chamber). Fetuses are at particular risk because fetal hemoglobin binds CO somewhat more tightly.

Why is $50\%$ COHb lethal when an anemia that removes half of the hemoglobin is tolerated? Because CO does more than occupy sites: a CO-bound subunit acts like a bound $\ce{O2}$ and pulls its tetramer towards the R state, so the remaining sites bind $\ce{O2}$ tightly and release little of it in the tissues (panel C of the next figure).

### 7.3.7. Hemoglobin Also Transports H⁺ and CO₂: The Bohr Effect

Respiration in the tissues produces $\ce{CO2}$, which is hydrated to bicarbonate by carbonic anhydrase, abundant in erythrocytes,

$$
\ce{CO2 + H2O <=> H+ + HCO3-} ,
$$
so the tissues are acidified (the buffer chemistry is in [7.1.2](/7.1.2)). Hemoglobin carries about $40\%$ of the $\mathrm{H^+}$ and $15$–$20\%$ of the $\ce{CO2}$ formed in the tissues to the lungs and kidneys; the rest of the $\mathrm{H^+}$ is taken up by the bicarbonate buffer of the plasma, and the rest of the $\ce{CO2}$ travels as dissolved $\ce{HCO3-}$ and $\ce{CO2}$. Both $\mathrm{H^+}$ and $\ce{CO2}$ bind preferentially to the T state, so their binding is inversely related to that of $\ce{O2}$.

**Definition 7.3.6 (Bohr Effect)** The **Bohr effect** is the decrease in the $\ce{O2}$ affinity of hemoglobin with decreasing pH and increasing $\ce{CO2}$ concentration (Christian Bohr, 1904); conversely, oxygenation releases protons.

The linked equilibrium $\ce{HHb+ + O2 <=> HbO2 + H+}$ summarizes it. Protons bind to several groups whose $\mathrm{p}K_\mathrm{a}$ is higher in T than in R; the largest contribution comes from His HC3 (β His146), which when protonated forms the T-state ion pair with Asp FG1 (Asp94); the N-terminal amino groups of the α chains and other His residues contribute as well. The size of the effect is measured by the Bohr coefficient $\Delta\lg p_{50}/\Delta\mathrm{pH} \approx -0.48$ for human blood. By Wyman's linkage relation, this slope equals (with the opposite sign) the number of protons released per $\ce{O2}$ bound, so about two protons are released per tetramer on full oxygenation.

$\ce{CO2}$ also binds directly, as a carbamate on the uncharged N-terminal amino group of each globin chain (carbaminohemoglobin):

$$
\ce{R-NH2 + CO2 <=> R-NH-COO- + H+} ;
$$
the released proton contributes to the Bohr effect, and the carbamates form additional salt bridges that stabilize T. In the lungs the high $p_{\mathrm{O_2}}$ reverses everything: $\ce{O2}$ binds, $\mathrm{H^+}$ and $\ce{CO2}$ are released, and the $\ce{CO2}$ is exhaled. (The reciprocal effect, that deoxyhemoglobin binds more $\mathrm{H^+}$ and $\ce{CO2}$, is called the Haldane effect.) Through these linked equilibria, communication between subunits lets hemoglobin integrate the transport of $\ce{O2}$, $\ce{CO2}$ and $\mathrm{H^+}$.

Lehninger illustrates the Bohr effect with a blood pH of $7.6$ in the lungs and $7.2$ in the tissues. These are illustrative extremes: at rest, arterial blood has pH $7.40$ and mixed venous blood about $7.36$; larger local differences occur in exercising muscle. The figure below uses the illustrative values to show the direction and potential size of the effect.

### 7.3.8. 2,3-Bisphosphoglycerate

**Definition 7.3.7 (2,3-Bisphosphoglycerate)** **2,3-Bisphosphoglycerate** (BPG) is a heterotropic allosteric effector of hemoglobin, made in erythrocytes from the glycolytic intermediate 1,3-bisphosphoglycerate ([7.1.18](/7.1.18)), that binds to the T state and lowers its $\ce{O2}$ affinity.

BPG ($\sim 5\ \mathrm{mM}$ in erythrocytes at sea level) binds in the central cavity between the two β subunits, which exists only in the T state; its five negative charges interact with positively charged groups lining the cavity (the N-terminal amino groups of the β chains and β His2, Lys82 and His143). Only one BPG binds per tetramer; on oxygenation the cavity narrows and BPG is expelled ($\ce{HbBPG + O2 <=> HbO2 + BPG}$). Stripped of BPG, hemoglobin binds $\ce{O2}$ so tightly ($p_{50} \approx 1.4\ \mathrm{kPa}$, $n_\mathrm{H}$ falling only slightly, from about $3$ to $2.5$) that it would barely release it in the tissues.

BPG adjusts oxygen delivery to altitude and hypoxia. At $4\,500\ \mathrm{m}$ the alveolar $p_{\mathrm{O_2}}$ falls to about $7.5\ \mathrm{kPa}$, and hemoglobin with $5\ \mathrm{mM}$ BPG would deliver only about $30\%$ of its capacity instead of $38\%$; within hours the BPG concentration rises towards $8\ \mathrm{mM}$, lowering the affinity, which costs little loading in the lungs but increases unloading in the tissues, and delivery returns to about $37\%$. BPG also rises in people with hypoxia from lung or circulatory disease, and it is lost from stored blood, which is why stored erythrocytes initially deliver oxygen poorly after transfusion.

*Fetal hemoglobin.* The fetus must extract $\ce{O2}$ from maternal blood, so its hemoglobin must have a higher affinity. Fetal hemoglobin (HbF) is $\alpha_2\gamma_2$; at position 143 the γ chain has Ser instead of the His of the β chain, which removes positive charge from the BPG site. HbF binds BPG weakly and has a higher $\ce{O2}$ affinity ($p_{50} \approx 2.5$ against $3.5\ \mathrm{kPa}$ for HbA under physiological conditions).

![Heterotropic effects in the concerted model (K_R = 0.35 kPa, c = 0.01; each effector condition represented by the L that gives the stated p50). A: Bohr effect, p50 = 3.5 × 10^(−0.48(pH − 7.4)) kPa: at pH 7.4 throughout, 36 % of the capacity is released between 13.3 and 4 kPa; loading at the illustrative pH 7.6 and unloading at pH 7.2 would raise this to 53 %. B: BPG: without BPG (p50 = 1.4 kPa) hemoglobin barely releases oxygen; with 5 mM BPG (p50 = 3.5 kPa) it releases 36 % at sea level but only 29 % at 4500 m (lung p_O2 7.5 kPa); after acclimatization, 8 mM BPG (p50 = 4.3 kPa) restores delivery to 39 %. C: carbon monoxide: oxygen bound per subunit of total hemoglobin for normal blood, for an anaemia with half of the hemoglobin, and for blood in which half of all subunits carry CO (binomially distributed over tetramers): the anaemic blood still delivers 18 %, but CO-bound subunits lock their tetramers in the high-affinity state and delivery falls to 6 %](./plots/hb-effectors.py)

| Ligand | Binding site | Effect on $\ce{O2}$ affinity |
|---|---|---|
| CO | heme iron (same as $\ce{O2}$) | increases (R state stabilized) |
| $\mathrm{H^+}$ | His HC3, α N-termini, other His | decreases (Bohr effect) |
| $\ce{CO2}$ | N-terminal amino groups (carbamates) | decreases |
| BPG | central cavity between the β subunits (T state) | decreases |

### 7.3.9. Sickle Cell Anemia

**Definition 7.3.8 (Sickle Cell Anemia)** **Sickle cell anemia** is an inherited disease of individuals homozygous for hemoglobin S (HbS), in which Glu6 of the β chain is replaced by Val; deoxygenated HbS polymerizes into fibers that deform erythrocytes into sickle shapes.

Of almost $500$ known genetic variants of human hemoglobin, most of them rare single-residue substitutions, HbS is the most important. The Glu6 → Val substitution places a hydrophobic patch on the surface of the β subunit. In deoxyhemoglobin (T state) this patch fits into a hydrophobic pocket formed by β Phe85 and Leu88 of a neighboring molecule, a pocket that is hidden in oxyhemoglobin; deoxy-HbS therefore polymerizes into long fibers of $14$ strands, which align into insoluble bundles. Polymerization is a nucleated process with an extraordinarily steep concentration dependence (the delay before fibers appear varies roughly with the $30$th power of the HbS concentration in vitro), so whether fibers form during the second or so that a cell spends in a capillary depends sensitively on deoxygenation, concentration and the presence of non-polymerizing hemoglobins such as HbF. Sickled cells are fragile and rupture (the hemoglobin content of the blood falls to about half of the normal $15$–$16\ \mathrm{g}$ per $100\ \mathrm{mL}$), and they block capillaries, causing painful crises and organ damage; without treatment, many patients die in childhood.

Two developments build directly on this molecular picture. Hydroxyurea and, since 2023, gene therapies raise the production of fetal hemoglobin, whose γ chains do not join the polymer; one of them (exagamglogene autotemcel) uses **CRISPR–Cas9** editing of the *BCL11A* **enhancer** in the patient's stem cells to switch the γ-globin gene back on ([7.2.24](/7.2.24)). Heterozygotes (sickle cell trait) have only about $1\%$ sickled cells on deoxygenation, live essentially normal lives, and are significantly protected against severe *Plasmodium falciparum* malaria; in malarial regions of Africa this heterozygote advantage maintains the allele at high frequency by balancing selection ([7.10](/7.10)).

## 7.4. Antibodies: Complementary Interactions and Specificity

### 7.4.1. The Immune System in Brief

Most protein–ligand interactions do not involve a prosthetic group; the binding site is a cleft lined with amino acid residues, like the BPG site of hemoglobin, and discrimination between closely related ligands is the norm. The vertebrate adaptive immune system, which evolved about $500$ million years ago, exploits this to recognize virtually any foreign molecule (its biology is the subject of [7.15](/7.15)).

- The *humoral* immune system acts on bacteria, extracellular viruses and foreign molecules in the body fluids, through soluble antibodies (immunoglobulins, Ig, about $20\%$ of blood protein) produced by B lymphocytes.
- The *cellular* immune system destroys infected host cells, some parasites and foreign tissues, through cytotoxic T cells ($\mathrm{T_C}$) that recognize infected cells with T-cell receptors; helper T cells ($\mathrm{T_H}$) secrete cytokines (including interleukins) and stimulate the selective proliferation of the T and B cells that bind a particular antigen (clonal selection). Macrophages and other phagocytes engulf invaders.

Memory cells allow a rapid response to a pathogen met before, which is the basis of vaccination. The depletion of $\mathrm{T_H}$ cells by HIV progressively disables the whole system. Humans can make more than $10^8$ antibodies with different specificities, generated by recombination of immunoglobulin gene segments (**V(D)J recombination**, [7.2.9](/7.2.9)).

**Definition 7.4.1 (Antigen and Epitope)** An **antigen** is any molecule or pathogen capable of eliciting an immune response; the particular molecular structure within an antigen that an individual antibody or T-cell receptor binds is its **epitope** (antigenic determinant). A **hapten** is a small molecule ($M_\mathrm{r} < 5\,000$) that is not antigenic by itself but elicits antibodies when covalently attached to a large carrier protein.

A complex antigen (a virus, a bacterial cell wall, a protein) has many epitopes and is bound by many different antibodies. Antibodies raised against protein-linked haptens also bind the free hapten, which makes them useful as analytical reagents and as ligands in **affinity chromatography** ([6.4.14](/6.4.14)).

### 7.4.2. Structure of Immunoglobulin G

**Definition 7.4.2 (Antibody)** An **antibody** (immunoglobulin) is a protein made by B lymphocytes that binds specifically, and usually with high affinity, to the antigen that elicited its synthesis.

Immunoglobulin G (IgG), the main class of antibody and one of the most abundant proteins of serum, has four chains: two heavy chains ($\sim 50\ \mathrm{kDa}$) and two light chains ($\sim 25\ \mathrm{kDa}$), linked by noncovalent interactions and disulfide bonds into a Y-shaped molecule of $M_\mathrm{r}$ $150\,000$ (Gerald Edelman and Rodney Porter, 1960s). The heavy chains associate at the stem and branch at a flexible hinge to pair with the light chains in the two arms. The protease papain cleaves the hinge into two *Fab* fragments (antigen-binding) and one *Fc* fragment (which crystallizes readily); each Fab carries one antigen-binding site.

Each chain is built of **domains** of about $110$ residues with the *immunoglobulin fold*, a sandwich of two antiparallel **β sheets** in the all-β class ([7.1.5](/7.1.5#sec-5.4.4)). The light chain has one variable (VL) and one constant (CL) domain; the heavy chain of IgG has one variable (VH) and three constant domains (CH1, CH2, CH3), and the Fc carries an **N-linked glycan** on each CH2. The antigen-binding site is formed by VH and VL together, and within them by three hypervariable loops of each chain, the complementarity-determining regions (CDRs), at the tips of the arms.

![Antibodies. A: domain diagram of immunoglobulin G: two heavy chains (yellow; VH, CH1, hinge, CH2, CH3) and two light chains (purple; VL, CL) joined by disulfide bonds (hinge and heavy–light); the hypervariable CDR loops of VH and VL at the tip of each arm form the two antigen-binding sites; papain cleaves in the hinge, giving two Fab fragments and the Fc fragment, which carries a glycan on each CH2 domain. B: sandwich ELISA: a capture antibody adsorbed to the well binds the antigen from the sample; after washing, an enzyme-linked detection antibody against a second epitope is added; the enzyme converts a substrate into a colored product in proportion to the amount of antigen. C: ELISA standard curve: simulated absorbances of a two-fold dilution series of standards (duplicates) fitted with a four-parameter logistic curve (shaded: 95 % confidence band of the mean curve); an unknown sample with absorbance 1.1 is read back as about 100 pg/mL](./plots/igg-structure.py)

Mammals have five classes of immunoglobulins, defined by their heavy chains (α, δ, ε, γ, μ for IgA, IgD, IgE, IgG, IgM); either of two light-chain types, κ or λ, occurs in all classes.

| Class | Structure | Main role |
|---|---|---|
| IgM | membrane monomer on naive B cells; secreted pentamer with J chain | first antibody of a primary response; efficient complement activation |
| IgG | monomer | main serum antibody and main antibody of secondary responses; Fc receptors on macrophages trigger phagocytosis of antibody-coated pathogens; crosses the placenta |
| IgA | monomer, or dimer (trimer) with J chain in secretions | saliva, tears, milk, mucosal surfaces |
| IgE | monomer | allergy and defense against parasites: bound by its Fc to mast cells and basophils, it triggers release of histamine when antigen cross-links it |
| IgD | monomer | on naive B cells together with IgM; function less clear |

### 7.4.3. Antibodies Bind Tightly and Specifically

The specificity of an antibody is determined by the amino acid residues of its variable domains, especially the hypervariable residues that line the binding site; it results from chemical complementarity of shape, charge, hydrogen bonding and hydrophobicity between epitope and site. Antibody–protein interfaces bury large surfaces (typically $\sim 7$–$9\ \mathrm{nm^2}$ in total, as in the classic complexes of Fab fragments with lysozyme). Complementarity is often achieved by induced fit, with conformational changes in the binding site, the antigen or both; in the complex of an Fab with a **peptide** derived from HIV, for example, the hydrophobic cavity of the site enlarges and several groups move on binding. Typical antibody–antigen $K_\mathrm{d}$ values reach $10^{-10}\ \mathrm{M}$, a binding Gibbs energy of about $-57\ \mathrm{kJ\,mol^{-1}}$ at $25\ ^\circ\mathrm{C}$ (§7.1.2), and affinity maturation during an immune response can push them to the picomolar range. Because IgG has two sites, binding to an antigen with repeated epitopes (a virus surface) is much stronger than that of one site (avidity): when one arm lets go, the other keeps the antibody in place, so it rebinds before it can diffuse away.

### 7.4.4. Antibodies as Analytical Reagents

**Definition 7.4.3 (Polyclonal and Monoclonal Antibodies)** **Polyclonal antibodies** are the mixture produced by many different B lymphocytes in response to one antigen, recognizing different epitopes; **monoclonal antibodies** are produced by a population of identical B cells (a clone) grown in culture and all recognize the same epitope.

Polyclonal antisera are easy to obtain but heterogeneous: they often fail to distinguish closely related proteins or the phosphorylated form of a protein, and the specific antibody is only $1$–$5\%$ of the IgG. Monoclonal antibodies became available with the hybridoma technique of Georges Köhler and César Milstein (1975; Nobel Prize 1984), which fuses an antibody-producing B cell with an immortal myeloma cell; today recombinant and humanized monoclonal antibodies are also major drugs (against cancer, autoimmune diseases and infections). In immunoassays an antibody is attached to an easily detected label, usually an enzyme (horseradish peroxidase, alkaline phosphatase) or a fluorophore:

- *Western blot* (immunoblot): proteins separated by **SDS–polyacrylamide gel electrophoresis** ([6.4.14](/6.4.14)) are transferred electrophoretically to a nitrocellulose or PVDF membrane; after blocking the remaining protein-binding sites, the membrane is treated with a primary antibody against the target protein, then with a labeled secondary antibody against the primary one, and finally with a substrate that gives a chemiluminescent or colored product at the band. The method detects a minor component of a complex mixture and gives its approximate molecular mass.
- *ELISA* (enzyme-linked immunosorbent assay): in a *sandwich ELISA* a capture antibody on a plastic well binds the antigen and a second, enzyme-linked antibody against another epitope detects it, so that the color measures the amount of antigen; in an *indirect ELISA* the antigen is adsorbed to the well, and the assay measures the amount of antibody in a sample (for example a patient's serum). ELISAs detect less than a nanogram of protein. Concentrations are read from a standard curve, usually fitted with a four-parameter logistic function (panel C above; the statistics of such fits are in [7.7](/7.7)).
- *Immunoprecipitation* isolates a protein and its binding partners from a cell extract with antibodies bound to beads; *immunohistochemistry* and *immunocytochemistry* locate proteins in tissue sections and cells; *flow cytometry* measures antibody-stained cells one by one, and fluorescence-activated cell sorting (FACS) separates them.

## 7.5. Proteins Powered by Chemical Energy: Actin and Myosin

Motor proteins show how chemical energy can drive cycles of binding and release. In skeletal muscle, contraction results from the interaction of myosin and actin, which together make up more than $80\%$ of muscle protein.

- *Myosin* ($M_\mathrm{r}$ $520\,000$) has two heavy chains ($220\,000$ each), whose C-terminal halves form a long left-handed **coiled coil** (the tail, like α-keratin, [7.1.5](/7.1.5#sec-5.3.2)) and whose N-terminal parts form two globular heads with an ATPase site and an actin-binding site, and four light chains associated with the heads. Hundreds of myosin molecules associate by their tails into bipolar *thick filaments*.
- *Actin* monomers (G-actin, $M_\mathrm{r}$ $42\,000$) polymerize into F-actin, a two-stranded helical filament; each monomer binds ATP and hydrolyzes it after incorporation, which serves filament dynamics, not contraction. F-actin with tropomyosin and troponin forms the *thin filaments*.
- In the *sarcomere*, the contractile unit, thick and thin filaments interdigitate (each thick filament surrounded by six thin filaments) between Z disks; contraction is the sliding of the filaments past each other, which shortens the sarcomere (its mechanics is treated in [7.14](/7.14)).

Each myosin head runs through a cycle in which the chemical state of the bound nucleotide sets its affinity for actin:

1. ATP binds to the head, a cleft in the myosin opens, and the head releases actin (low affinity);
2. ATP is hydrolyzed; the head changes conformation into a "cocked", high-energy state and binds weakly to an actin subunit farther along the thin filament, closer to the Z disk;
3. release of $\mathrm{P_i}$ closes the cleft and strengthens the binding;
4. the power stroke: the head returns to its resting conformation and pulls the thick filament along the thin one; ADP is released, leaving the tightly bound rigor complex until the next ATP binds.

Each cycle produces a force of about $3$–$4\ \mathrm{pN}$ and a displacement of $5$–$10\ \mathrm{nm}$. Only a small fraction of the heads ($1$–$3\%$) are attached at any moment, but because there are many, the filament never slips back. Without ATP the heads stay bound, which is the cause of rigor mortis. Contraction is switched on by $\mathrm{Ca^{2+}}$: in relaxed muscle, tropomyosin (a two-stranded coiled coil lying along the actin filament) and troponin (subunits I, C and T, every $38.5\ \mathrm{nm}$) block the myosin-binding sites; a nerve impulse releases $\mathrm{Ca^{2+}}$ from the sarcoplasmic reticulum, $\mathrm{Ca^{2+}}$ binds troponin C, and the resulting conformational change moves tropomyosin and relieves the inhibition by troponin I. Muscle thus combines the two basic functions of proteins: myosin is both a reversible actin-binding protein, regulated like the other proteins of this chapter, and an ATPase, an enzyme, which leads to the next chapter. The physics of single motors (kinesin steps, optical-trap measurements) is treated in [7.6.27](/7.6.27).

## Summary

| Concept | Key relation | Biological meaning |
|---|---|---|
| Binding (Definitions 7.1.1, 7.1.2) | $K_\mathrm{d} = k_\mathrm{off}/k_\mathrm{on}$; $\theta = [\mathrm{L}]/([\mathrm{L}] + K_\mathrm{d})$ (Formula 7.1.1) | half-saturation at $[\mathrm{L}] = K_\mathrm{d}$; $10\% \to 90\%$ needs $81$-fold more ligand |
| **Binding energy** and kinetics | $\Delta_{\mathrm{bind}}G^\circ = RT\ln(K_\mathrm{d}/c^\circ)$; $5.7\ \mathrm{kJ\,mol^{-1}}$ per decade; $\tau = 1/k_\mathrm{off}$ | $k_\mathrm{on} \le 10^8$–$10^9\ \mathrm{M^{-1}\,s^{-1}}$, so tight binding means slow release |
| Heme (Definition 7.2.1) | $\mathrm{F\mathrm{e}^{2+}}$, 4 porphyrin N + proximal His F8 + $\ce{O2}$ | burying heme prevents oxidation; distal His E7 hydrogen-bonds $\ce{O2}$ and lowers CO preference from $20\,000$ to $40$ |
| Myoglobin | $p_{50} = 0.26\ \mathrm{kPa}$, hyperbolic | storage, not transport (releases $4\%$) |
| Best hyperbolic carrier (Proposition 7.3.1) | $p_{50} = \sqrt{p_1p_2}$, $\Delta\theta_{\max} = (\sqrt{p_1} - \sqrt{p_2})/(\sqrt{p_1} + \sqrt{p_2}) = 29\%$ | transport requires cooperativity |
| Hemoglobin (Definition 7.3.1) | $\alpha_2\beta_2$; T ⇌ R at the $\alpha_1\beta_2$ interface; $p_{50} \approx 3.5\ \mathrm{kPa}$ | delivers $\sim 38\%$ between lungs and tissues |
| Hill equation (Formula 7.3.1) | $\theta = [\mathrm{L}]^{n_\mathrm{H}}/(K_{0.5}^{n_\mathrm{H}} + [\mathrm{L}]^{n_\mathrm{H}})$; $n_\mathrm{H} \approx 3$ for Hb | degree of cooperativity, $n_\mathrm{H} < n$ |
| MWC model (Definition 7.3.4, Formula 7.3.2) | $Z = (1+\alpha)^4 + L(1+c\alpha)^4$; maximal cooperativity at $Lc^2 = 1$ | concerted switch; effectors change $L$ |
| KNF model (Definition 7.3.5) | induced fit subunit by subunit | allows negative cooperativity |
| Bohr effect (Definition 7.3.6) | $\Delta\lg p_{50}/\Delta\mathrm{pH} \approx -0.48$; $\sim 2\ \mathrm{H^+}$ released per tetramer | $\mathrm{H^+}$ and $\ce{CO2}$ (carbamates) favor T and unloading in tissues |
| BPG (Definition 7.3.7) | one per tetramer, central cavity, T only; $5 \to 8\ \mathrm{mM}$ at altitude | restores delivery from $30\%$ to $37\%$ at $4\,500\ \mathrm{m}$; HbF (γ Ser143) binds it weakly |
| CO | $250\times$ the affinity of $\ce{O2}$; stabilizes R | $50\%$ COHb is far worse than $50\%$ anemia |
| Sickle cell anemia (Definition 7.3.8) | β Glu6 → Val; deoxy-HbS polymerizes | balancing selection by malaria; HbF-inducing therapies |
| Antibodies (Definitions 7.4.1–7.4.3) | IgG $\mathrm{H_2L_2}$, $150\ \mathrm{kDa}$; Fab/Fc; V and C domains; CDRs; $K_\mathrm{d}$ to $10^{-10}\ \mathrm{M}$ and below | Western blot, ELISA, immunoprecipitation, flow cytometry |
| Actin–myosin | ATP: release; ADP–$\mathrm{P_i}$: weak binding; $\mathrm{P_i}$ release: power stroke | chemical energy modulates binding; $\mathrm{Ca^{2+}}$–troponin switch |

## Questions

1. A receptor binds its hormone with $K_\mathrm{d} = 1.0\ \mathrm{nM}$. (a) What fraction of receptors is occupied at $0.25\ \mathrm{nM}$ hormone? (b) A **mutation** lowers the binding Gibbs energy by $5.7\ \mathrm{kJ\,mol^{-1}}$ (makes it less negative) at $25\ ^\circ\mathrm{C}$; what is the new $K_\mathrm{d}$ and occupancy? (c) If $k_\mathrm{on} = 5\times 10^6\ \mathrm{M^{-1}\,s^{-1}}$, what is the residence time of the wild-type complex?

   **Answer** (a) $\theta = 0.25/(0.25 + 1.0) = 0.20$. (b) $5.7\ \mathrm{kJ\,mol^{-1}} = RT\ln 10$ at $25\ ^\circ\mathrm{C}$, so $K_\mathrm{d}$ increases tenfold to $10\ \mathrm{nM}$ and $\theta = 0.25/10.25 = 0.024$. (c) $k_\mathrm{off} = k_\mathrm{on}K_\mathrm{d} = 5\times10^6 \times 10^{-9} = 5\times 10^{-3}\ \mathrm{s^{-1}}$, so $\tau = 1/k_\mathrm{off} = 200\ \mathrm{s}$.
2. Using the Hill equation with $p_{50} = 3.5\ \mathrm{kPa}$ and $n_\mathrm{H} = 2.8$, compute the fraction of capacity delivered between $13.3$ and $4\ \mathrm{kPa}$ and compare it with the best non-cooperative carrier.

   **Answer** $\theta(13.3) = 1/[1 + (3.5/13.3)^{2.8}] = 1/(1 + 0.024) = 0.977$; $\theta(4) = 1/[1 + (3.5/4)^{2.8}] = 1/(1 + 0.688) = 0.592$. Delivery is $0.977 - 0.592 = 0.385$, i.e. $38\%$, against $29\%$ for the best hyperbola (Proposition 7.3.1) and $4\%$ for myoglobin.
3. Show that in the MWC model the binding curve is hyperbolic when $c = 1$, and explain in words why cooperativity disappears both for $L \to 0$ and for $L \to \infty$.

   **Answer** For $c = 1$, $Z = (1 + L)(1 + \alpha)^4$ and $\theta = \alpha(1+\alpha)^3(1 + L)/[(1+L)(1+\alpha)^4] = \alpha/(1 + \alpha)$, a hyperbola with $K_\mathrm{d} = K_\mathrm{R}$: if both states bind equally, shifting between them does not change the affinity. For $L \to 0$ all molecules are R before any ligand binds, and for $L \to \infty$ they remain T even when saturated (the term $L(1 + c\alpha)^4$ dominates $Z$ at all accessible $\alpha$); in both limits there is only one conformational state in the relevant range, the sites are independent, and $\theta$ is a hyperbola with $K_\mathrm{R}$ or $K_\mathrm{T}$. Cooperativity requires that binding move the population from the low- to the high-affinity state within the range of ligand concentrations.
4. Why does the Hill coefficient of hemoglobin approach 1 at very low and very high oxygen pressures, and what do the two asymptotes of the Hill plot tell us?

   **Answer** At very low saturation almost all molecules are in the T state, and the first ligand binds to independent T-state sites; at very high saturation almost all are in R, and the last ligand binds to an R-state site. In both limits $\theta/(1 - \theta)$ is proportional to $p_{\mathrm{O_2}}$, so the slope is 1. Extrapolating the lower asymptote to $\lg[\theta/(1-\theta)] = 0$ gives the dissociation constant of the T state ($K_\mathrm{T}$), the upper one that of the R state ($K_\mathrm{R}$); their ratio $c = K_\mathrm{R}/K_\mathrm{T}$ measures the free-energy cost of the cooperativity, $RT\ln(1/c)$ per site ($11\ \mathrm{kJ\,mol^{-1}}$ for $c = 0.01$ at $25\ ^\circ\mathrm{C}$).
5. Explain why fetal hemoglobin has a higher oxygen affinity than adult hemoglobin although its oxygen-binding sites are essentially the same, and predict the effect of removing BPG from both.

   **Answer** The difference lies in the heterotropic effector, not in the heme pockets. At position 143 the γ chains of HbF have Ser instead of the positively charged His of the β chains; the BPG site in the central cavity loses two positive charges and binds BPG more weakly, so in erythrocytes (about $5\ \mathrm{mM}$ BPG) the T state of HbF is less stabilized and its $p_{50}$ is lower. Stripped of BPG, HbA and HbF have nearly the same high affinity, because the difference disappears with the effector.
6. A patient with sickle cell trait (HbA/HbS heterozygote) is advised to avoid extreme exertion at high altitude. Explain the molecular reasons, and why the trait does not cause disease at sea level.

   **Answer** Only deoxygenated HbS polymerizes, because the acceptor pocket for β Val6 is exposed only in the T state, and the delay before polymerization falls steeply with the concentration of deoxy-HbS. In a heterozygote about $40\%$ of the hemoglobin is HbS, diluted by HbA, which joins the polymer poorly, so under normal conditions polymerization is much slower than the transit time through capillaries and only about $1\%$ of cells sickle. At high altitude and during strenuous exercise, low $p_{\mathrm{O_2}}$, acidosis (Bohr effect) and higher BPG all increase the fraction of deoxyhemoglobin, and dehydration raises the hemoglobin concentration; together they shorten the delay time enough for sickling and vaso-occlusion to occur.
7. In a sandwich ELISA, why must the capture and detection antibodies recognize different epitopes, and why are monoclonal antibodies preferred for at least one of them? What determines the useful range of the standard curve?

   **Answer** Both antibodies must bind the same antigen molecule at once; if they competed for one epitope, the bound capture antibody would block the detection antibody and no signal would form. Monoclonal antibodies guarantee a single, defined epitope, so the pair can be chosen not to overlap, and they give reproducible, specific assays; a polyclonal detection antibody is sometimes used because it binds several epitopes and amplifies the signal. The standard curve is sigmoid in $\lg[\text{antigen}]$ (four-parameter logistic): at low concentrations the signal is lost in the background, at high concentrations the capture antibodies are saturated, and concentrations are determined reliably only in the steep middle part around the EC50, where a small change in antigen gives a large change in absorbance.
