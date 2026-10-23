---
title: Theories of Reaction Rates
source_hash: 9ef37e4b498f
---

[6.3.15](/6.3.15) treated rate constants as parameters determined by experiment. A theory of reaction rates must answer the question whether rate constants can be calculated from the properties of molecules (size, mass, structure, interaction potential energy). A satisfactory theory must at least yield the **law of mass action** and the **Arrhenius equation**, and explain the physical meaning of the activation energy and of the **pre-exponential factor**. [6.1.7](/6.1.7#sec-7.2) gave qualitative pictures of **collision theory** and **transition state theory**; this chapter makes them quantitative.

Collision theory (16.1) regards molecules as hard spheres and integrates the collision cross section over the **Maxwell speed distribution** of [5.2.1](/5.2.1); the result is intuitive, but it cannot calculate the critical energy or the **steric factor**. Transition state theory regards a reaction as the crossing of a saddle point on a potential energy surface (16.2), assumes equilibrium between the reactants and the activated complex, and uses the **partition function** and statistical thermodynamics of [6.3.10](/6.3.10)–[6.3.11](/6.3.11) to calculate this "equilibrium constant" (16.3); it can thus in principle calculate rate constants from molecular structure, and gives the enthalpy and entropy of activation, thermodynamic quantities that can be compared with experiment. The theory of unimolecular reactions (16.4) explains how a molecule that decomposes "by itself" acquires its energy, and is a classic application of the steady-state approximation of [6.3.15](/6.3.15). Finally we briefly introduce molecular reaction dynamics (16.5), which studies reactions through single collisions. Reactions in solution and catalysis are treated in [6.3.17](/6.3.17).

## 16.1. Collision Theory

### 16.1.1. Basic Assumptions and the Collision Number

The main points of collision theory are:

1. Reactant molecules must collide in order to react.
2. Molecules are hard spheres without internal structure; collisions are classified as elastic (only momentum is exchanged), inelastic (internal motion is excited) and reactive, and only sufficiently violent collisions are **effective collisions**.
3. The violence of a collision is measured by the relative translational energy, and reaction occurs only when it exceeds a critical value independent of temperature.
4. Molecular speeds obey the Maxwell–Boltzmann distribution, which the reaction does not disturb.

**Definition 16.1.1** Regard molecules A and B as hard spheres of diameters $d_{\mathrm{A}}$ and $d_{\mathrm{B}}$; the minimum distance to which the centers of the two spheres can approach, $d_{\mathrm{AB}} = \frac12(d_{\mathrm{A}} + d_{\mathrm{B}})$, is called the **collision diameter**. The total number of collisions of A and B molecules per unit volume per unit time, $Z_{\mathrm{AB}}$, is called the **collision density** (collision frequency factor), in $\mathrm{m^{-3}\,s^{-1}}$.

An A molecule moving at relative speed $v_{\mathrm{rel}}$ with respect to B sweeps out in unit time a cylinder of cross section equal to the **collision cross section** $\sigma = \pi d_{\mathrm{AB}}^2$ and length $v_{\mathrm{rel}}$, and every B molecule whose center falls in it collides with it (the same method as for the **mean collision frequency** of [5.2.2](/5.2.2#def-2.3.1)). Averaging over the distribution of relative speeds (16.1.3),

$$
Z_{\mathrm{AB}} = \pi d_{\mathrm{AB}}^2\bar v_{\mathrm{rel}}n_{\mathrm{A}}n_{\mathrm{B}}, \qquad \bar v_{\mathrm{rel}} = \sqrt{\frac{8k_{\mathrm{B}}T}{\pi\mu}} = \sqrt{\frac{8RT}{\pi M_\mu}},
$$
where $n_{\mathrm{A}}, n_{\mathrm{B}}$ are number densities, $\mu = \frac{m_{\mathrm{A}}m_{\mathrm{B}}}{m_{\mathrm{A}} + m_{\mathrm{B}}}$ is the **reduced mass**, and $M_\mu = N_{\mathrm{A}}\mu$ is the reduced molar mass. The elementary derivation takes the mean speeds of the two molecules "colliding at $90^\circ$" and obtains $\bar v_{\mathrm{rel}} = (\bar v_{\mathrm{A}}^2 + \bar v_{\mathrm{B}}^2)^{1/2}$, with the same result; the rigorous derivation is that the relative velocity also obeys a Maxwell distribution, with the mass replaced by $\mu$ (16.1.3). For collisions between molecules of the same kind each collision is counted twice, so $Z_{\mathrm{AA}} = \frac12\pi d_{\mathrm{A}}^2\bar v_{\mathrm{rel}}n_{\mathrm{A}}^2$ with $\mu = m_{\mathrm{A}}/2$, that is, $Z_{\mathrm{AA}} = 2d_{\mathrm{A}}^2n_{\mathrm{A}}^2\sqrt{\pi RT/M_{\mathrm{A}}}$.

If every collision led to reaction, a gas-phase bimolecular reaction at ordinary temperature and pressure would be completed in about $10^{-9}\,\mathrm{s}$ (for the order-of-magnitude estimate see [6.1.7](/6.1.7#sec-7.2.1)); only a very small fraction of collisions is effective.

### 16.1.2. Impact Parameter and Reaction Cross Section

The total kinetic energy of two molecules can be split into the kinetic energy of the motion of the center of mass and that of the relative motion:

$$
\frac12m_{\mathrm{A}}v_{\mathrm{A}}^2 + \frac12m_{\mathrm{B}}v_{\mathrm{B}}^2 = \frac12(m_{\mathrm{A}} + m_{\mathrm{B}})v_{\mathrm{g}}^2 + \frac12\mu v_{\mathrm{rel}}^2.
$$
The motion of the **center of mass** is unchanged in the collision and makes no contribution to the reaction; only the relative translational energy $\varepsilon = \frac12\mu v_{\mathrm{rel}}^2$ can be used to overcome the energy barrier. But even if $\varepsilon$ is large enough, a glancing collision does not cause reaction.

**Definition 16.1.2** Draw through the center of A a straight line parallel to the relative velocity $\boldsymbol{v}_{\mathrm{rel}}$; the distance $b$ between it and the line of motion of the center of B is called the **impact parameter**. $b = 0$ is a head-on collision, and for $b \ge d_{\mathrm{AB}}$ there is no collision.

Let the angle between the line of centers at the moment of collision and $\boldsymbol{v}_{\mathrm{rel}}$ be $\theta$, so that $b = d_{\mathrm{AB}}\sin\theta$. In a hard-sphere collision, the component $v_{\mathrm{rel}}\cos\theta$ of the relative velocity along the line of centers determines the violence of the impact, and the corresponding kinetic energy is

$$
\varepsilon' = \frac12\mu(v_{\mathrm{rel}}\cos\theta)^2 = \varepsilon\left(1 - \frac{b^2}{d_{\mathrm{AB}}^2}\right).
$$
Integration over all $b$, $\int_0^{d_{\mathrm{AB}}}2\pi b\,\mathrm{d}b = \pi d_{\mathrm{AB}}^2$, gives the collision cross section.

**Definition 16.1.3** Only collisions in which the relative translational energy along the line of centers, $\varepsilon'$, exceeds a critical value $\varepsilon_{\mathrm{c}}$ can cause reaction; $\varepsilon_{\mathrm{c}}$ is called the **threshold energy** (critical energy), and per mole $E_{\mathrm{c}} = N_{\mathrm{A}}\varepsilon_{\mathrm{c}}$. For a relative translational energy $\varepsilon$, the impact parameters that can cause reaction satisfy $b < b_{\mathrm{r}}$, with $\varepsilon(1 - b_{\mathrm{r}}^2/d_{\mathrm{AB}}^2) = \varepsilon_{\mathrm{c}}$, and the area

$$
\sigma_{\mathrm{r}}(\varepsilon) = \pi b_{\mathrm{r}}^2 = \begin{cases}\pi d_{\mathrm{AB}}^2\left(1 - \dfrac{\varepsilon_{\mathrm{c}}}{\varepsilon}\right), & \varepsilon > \varepsilon_{\mathrm{c}},\\[2mm] 0, & \varepsilon \le \varepsilon_{\mathrm{c}}\end{cases}
$$
is called the **reaction cross section**.

The reaction cross section increases from zero at the threshold energy and tends to the collision cross section as $\varepsilon \to \infty$. It is a microscopic quantity that can be measured directly at definite relative energy with crossed molecular beams (16.5); the hard-sphere model is only its simplest form.

### 16.1.3. Rate Constant from the Reaction Cross Section

Consider a beam of A molecules of relative speed $v_{\mathrm{rel}}$ entering B. The number of reactions of A with B per unit volume per unit time is $\sigma_{\mathrm{r}}(v_{\mathrm{rel}})v_{\mathrm{rel}}n_{\mathrm{A}}n_{\mathrm{B}}$, so for a definite relative speed the microscopic rate constant is $k(v_{\mathrm{rel}}) = v_{\mathrm{rel}}\sigma_{\mathrm{r}}(v_{\mathrm{rel}})$. The macroscopic rate constant is its average over the distribution of relative speeds:

$$
k(T) = \int_0^\infty v_{\mathrm{rel}}\sigma_{\mathrm{r}}(v_{\mathrm{rel}})f(v_{\mathrm{rel}})\,\mathrm{d}v_{\mathrm{rel}}, \qquad f(v) = 4\pi\left(\frac{\mu}{2\pi k_{\mathrm{B}}T}\right)^{3/2}v^2\mathrm{e}^{-\mu v^2/2k_{\mathrm{B}}T}.
$$

**Theorem 16.1.1 (Rate Constant of Hard-Sphere Collision Theory)** Under the assumptions above, the rate constant of the bimolecular reaction $\ce{A + B -> P}$ is

$$
k(T) = \pi d_{\mathrm{AB}}^2\sqrt{\frac{8k_{\mathrm{B}}T}{\pi\mu}}\,\mathrm{e}^{-\varepsilon_{\mathrm{c}}/k_{\mathrm{B}}T} \quad(\text{per pair of molecules}), \qquad k = N_{\mathrm{A}}\pi d_{\mathrm{AB}}^2\sqrt{\frac{8RT}{\pi M_\mu}}\,\mathrm{e}^{-E_{\mathrm{c}}/RT} \quad(\text{per mole}). \tag{16.1}
$$

**Proof** Take the relative translational energy $\varepsilon = \frac12\mu v^2$ as the variable of integration: $\mathrm{d}\varepsilon = \mu v\,\mathrm{d}v$, $v^3\,\mathrm{d}v = \frac{2\varepsilon}{\mu^2}\mathrm{d}\varepsilon$, so

$$
vf(v)\,\mathrm{d}v = 4\pi\left(\frac{\mu}{2\pi k_{\mathrm{B}}T}\right)^{3/2}\frac{2\varepsilon}{\mu^2}\mathrm{e}^{-\varepsilon/k_{\mathrm{B}}T}\,\mathrm{d}\varepsilon = \left(\frac{8}{\pi\mu}\right)^{1/2}(k_{\mathrm{B}}T)^{-3/2}\varepsilon\,\mathrm{e}^{-\varepsilon/k_{\mathrm{B}}T}\,\mathrm{d}\varepsilon.
$$
Substituting the reaction cross section,

$$
k(T) = \left(\frac{8}{\pi\mu}\right)^{1/2}(k_{\mathrm{B}}T)^{-3/2}\pi d_{\mathrm{AB}}^2\int_{\varepsilon_{\mathrm{c}}}^\infty(\varepsilon - \varepsilon_{\mathrm{c}})\mathrm{e}^{-\varepsilon/k_{\mathrm{B}}T}\,\mathrm{d}\varepsilon.
$$
Let $\varepsilon - \varepsilon_{\mathrm{c}} = k_{\mathrm{B}}Tu$; the integral equals $(k_{\mathrm{B}}T)^2\mathrm{e}^{-\varepsilon_{\mathrm{c}}/k_{\mathrm{B}}T}\int_0^\infty u\mathrm{e}^{-u}\,\mathrm{d}u = (k_{\mathrm{B}}T)^2\mathrm{e}^{-\varepsilon_{\mathrm{c}}/k_{\mathrm{B}}T}$ ($\int_0^\infty u\mathrm{e}^{-u}\,\mathrm{d}u$ is the **gamma function** $\Gamma(2) = 1$). Collecting terms gives Eq. (16.1); multiplication by $N_{\mathrm{A}}$ converts the rate constant per pair of molecules ($\mathrm{m^3\,s^{-1}}$) into the rate constant per mole ($\mathrm{m^3\,mol^{-1}\,s^{-1}}$). $\square$

For $\varepsilon_{\mathrm{c}} = 0$, $k = \pi d_{\mathrm{AB}}^2\bar v_{\mathrm{rel}}$, that is, every collision leads to reaction, and we return to the collision density of 16.1.1; thus $\mathrm{e}^{-E_{\mathrm{c}}/RT}$ is the fraction of effective collisions. It is noteworthy that this fraction is not "the fraction of molecular pairs whose relative translational energy exceeds $E_{\mathrm{c}}$". Let $x = E_{\mathrm{c}}/RT$: the fraction of pairs with relative translational energy exceeding $E_{\mathrm{c}}$ is $2\sqrt{x/\pi}\,\mathrm{e}^{-x} + \operatorname{erfc}\sqrt{x}$; weighted by collision flux (fast molecules collide more often, by a factor $v$), the fraction of collisions with energy exceeding $E_{\mathrm{c}}$ is $(1 + x)\mathrm{e}^{-x}$; only after the glancing collisions are also removed (the factor $1 - \varepsilon_{\mathrm{c}}/\varepsilon$ of the reaction cross section) do we obtain exactly the simple **Boltzmann factor** $\mathrm{e}^{-x}$.

![Hard-sphere model: left, the reaction cross section as a function of relative translational energy; right, the flux-weighted distribution of relative translational energy ε exp(−ε/kBT) (blue) and its product with the reaction cross section, the integrand (red); for εc = 4kBT numerical integration gives the reacting fraction e⁻⁴, in agreement with Theorem 16.1.1](./plots/collision-cross-section.py)

For molecules of the same kind, $\ce{2A -> P}$, with the rate defined by $v = -\frac12\frac{\mathrm{d}c_{\mathrm{A}}}{\mathrm{d}t} = kc_{\mathrm{A}}^2$, $k = \frac12N_{\mathrm{A}}\pi d_{\mathrm{A}}^2\sqrt{\frac{16RT}{\pi M_{\mathrm{A}}}}\mathrm{e}^{-E_{\mathrm{c}}/RT} = 2N_{\mathrm{A}}d_{\mathrm{A}}^2\sqrt{\frac{\pi RT}{M_{\mathrm{A}}}}\mathrm{e}^{-E_{\mathrm{c}}/RT}$.

### 16.1.4. Comparison with the Arrhenius Equation

Equation (16.1) can be written $k = BT^{1/2}\mathrm{e}^{-E_{\mathrm{c}}/RT}$ with $B$ independent of temperature. From the definition of the activation energy,

$$
E_{\mathrm{a}} = RT^2\frac{\mathrm{d}\ln k}{\mathrm{d}T} = E_{\mathrm{c}} + \frac12RT, \qquad A = N_{\mathrm{A}}\pi d_{\mathrm{AB}}^2\sqrt{\frac{8RT}{\pi M_\mu}}\,\mathrm{e}^{1/2}.
$$
At $298\,\mathrm{K}$, $\frac12RT = 1.2\,\mathrm{kJ\,mol^{-1}}$, and $E_{\mathrm{a}}$ for a typical reaction is much larger, so $E_{\mathrm{c}} \approx E_{\mathrm{a}}$. Because $E_{\mathrm{c}}$ is assumed constant, both $E_{\mathrm{a}}$ and $A$ vary slowly with temperature.

The pre-exponential factors calculated by collision theory are roughly right for simple reactions but are often too large for complex molecules, so the **steric factor** $P$ is introduced ([6.1.7](/6.1.7#def-7.2.2)), $k = PN_{\mathrm{A}}\pi d_{\mathrm{AB}}^2\bar v_{\mathrm{rel}}\mathrm{e}^{-E_{\mathrm{c}}/RT}$. The pre-exponential factors of several reactions (in $\mathrm{L\,mol^{-1}\,s^{-1}}$; data from Atkins's textbook) are:

| Reaction | $A_{\text{exp}}$ | $A_{\text{theor}}$ | $P$ |
|---|---|---|---|
| $\ce{2NOCl -> 2NO + 2Cl}$ | $9.4 \times 10^9$ | $5.9 \times 10^{10}$ | 0.16 |
| $\ce{2ClO -> Cl2 + O2}$ | $6.3 \times 10^7$ | $2.5 \times 10^{10}$ | $2.5 \times 10^{-3}$ |
| $\ce{H2 + C2H4 -> C2H6}$ | $1.24 \times 10^6$ | $7.3 \times 10^{11}$ | $1.7 \times 10^{-6}$ |
| $\ce{K + Br2 -> KBr + Br}$ | $1.0 \times 10^{12}$ | $2.1 \times 10^{11}$ | 4.8 |

**Example 16.1.1** Taking the collision cross sections of $\ce{H2}$ and $\ce{C2H4}$ as $0.27$ and $0.64\,\mathrm{nm^2}$, estimate the theoretical pre-exponential factor of $\ce{H2 + C2H4}$ at $628\,\mathrm{K}$ (without the factor $\mathrm{e}^{1/2}$).

**Solution** $d_{\ce{H2}} = (0.27/\pi)^{1/2}\,\mathrm{nm} = 0.293\,\mathrm{nm}$, $d_{\ce{C2H4}} = 0.451\,\mathrm{nm}$, $d_{\mathrm{AB}} = 0.372\,\mathrm{nm}$, and $\sigma = \pi d_{\mathrm{AB}}^2 = 0.435\,\mathrm{nm^2}$. $M_\mu = \frac{2.016 \times 28.05}{30.07}\,\mathrm{g\,mol^{-1}} = 1.881\,\mathrm{g\,mol^{-1}}$,

$$
\bar v_{\mathrm{rel}} = \sqrt{\frac{8 \times 8.314 \times 628}{\pi \times 1.881 \times 10^{-3}}}\,\mathrm{m\,s^{-1}} = 2.66 \times 10^3\,\mathrm{m\,s^{-1}},
$$

$$
\sigma\bar v_{\mathrm{rel}}N_{\mathrm{A}} = 0.435 \times 10^{-18} \times 2.66 \times 10^3 \times 6.022 \times 10^{23}\,\mathrm{m^3\,mol^{-1}\,s^{-1}} = 7.0 \times 10^{11}\,\mathrm{L\,mol^{-1}\,s^{-1}},
$$
in agreement with the theoretical value in the table; comparison with the experimental value gives $P \approx 2 \times 10^{-6}$: hydrogenation requires the two H atoms of $\ce{H2}$ to interact with the C=C double bond simultaneously, and the geometric requirement is extremely strict.

The case $P > 1$ for $\ce{K + Br2}$ is explained by the "harpoon mechanism": the K atom "throws" its valence electron to $\ce{Br2}$ at a distance much larger than the hard-sphere collision diameter, and the $\ce{K+}$ and $\ce{Br2-}$ formed are pulled together by Coulomb attraction, so the effective reaction cross section is much larger than the geometric cross section.

The success of collision theory lies in giving intuitively the forms of the law of mass action and of the Arrhenius equation and in estimating correctly the order of magnitude of the pre-exponential factor; its fundamental defect is that neither the threshold energy nor the steric factor can be calculated theoretically, and the hard-sphere model says nothing about how chemical bonds change. Overcoming these two defects requires the potential energy surface and transition state theory.

## 16.2. Potential Energy Surfaces and the Reaction Coordinate

### 16.2.1. Potential Energy Curve of a Diatomic Molecule

In the Born–Oppenheimer approximation, the motion of electrons is much faster than that of the nuclei, and the nuclei move in the potential energy $E_{\mathrm{p}}$ provided by the electrons, a function of the nuclear coordinates. The potential energy of a diatomic molecule depends only on the internuclear distance $r$.

**Definition 16.2.1 (Morse Potential)** The empirical potential energy function

$$
E_{\mathrm{p}}(r) = D_{\mathrm{e}}\left[\mathrm{e}^{-2a(r - r_{\mathrm{e}})} - 2\mathrm{e}^{-a(r - r_{\mathrm{e}})}\right]
$$
is called the **Morse potential**, where $r_{\mathrm{e}}$ is the equilibrium internuclear distance, $D_{\mathrm{e}}$ is the depth of the well (taking the separated atoms as the zero of energy), and $a$ is a constant related to the width of the well.

Expanding near $r_{\mathrm{e}}$, $E_{\mathrm{p}} \approx -D_{\mathrm{e}} + D_{\mathrm{e}}a^2(r - r_{\mathrm{e}})^2$, and comparing with the harmonic oscillator $\frac12\mu\omega^2(r - r_{\mathrm{e}})^2$ gives $a = \omega\sqrt{\mu/2D_{\mathrm{e}}}$, where $\omega = 2\pi\nu$ is the harmonic frequency. $D_{\mathrm{e}}$ is the depth of the well, not an energy barrier: as $r \to \infty$ the potential energy tends monotonically to zero, and dissociation has no barrier. The actual dissociation energy is measured from the vibrational ground state, $D_0 = D_{\mathrm{e}} - \frac12h\nu$ (the **zero-point energy**, see the vibrational levels of [5.5.5](/5.5.5#sec-5.3.3)). The Morse potential describes large-amplitude vibrations better than the harmonic oscillator: the level spacing decreases with vibrational quantum number and converges at $D_{\mathrm{e}}$.

### 16.2.2. Potential Energy Surface of a Three-Atom Reaction

Take $\ce{A + B-C -> A-B + C}$ as an example (such as $\ce{H + H2}$ and $\ce{H + Br2 -> HBr + Br}$). The potential energy of a three-atom system is a function of three internal coordinates, $E_{\mathrm{p}}(r_{\mathrm{AB}}, r_{\mathrm{BC}}, \angle\mathrm{ABC})$. If A attacks along the axis of BC (a collinear collision, $\angle\mathrm{ABC} = 180^\circ$), the potential energy depends only on the two internuclear distances and can be drawn as a surface.

**Definition 16.2.2** The surface (a hypersurface for polyatomic systems) formed in coordinate space by the potential energy as a function of the nuclear coordinates is called the **potential energy surface**. Reactants and products lie in two valleys of the surface, and the path connecting the two valleys, every point of which is an energy minimum in the direction perpendicular to the path, is called the **minimum energy path**; it passes through the lowest point on the ridge between the two valleys, the **saddle point** of the surface ([2.2.11](/2.2.11#def-11.5.2)).

The saddle point is a maximum along the path and a minimum in the perpendicular direction, and the configuration it corresponds to is the **transition state** $[\mathrm{A\cdots B\cdots C}]^{\ddagger}$. The arc length measured along the minimum energy path is the **reaction coordinate** ([6.1.7](/6.1.7#def-7.2.3)), and the variation of the potential energy along it (the potential energy profile) is the potential energy diagram of [6.1.7](/6.1.7#sec-7.2.2). The minimum energy path should be calculated in mass-weighted coordinates: the steepest-descent path so defined is the path actually followed by a system moving infinitely slowly.

Some characteristic regions of the potential energy surface:

- the reactant valley ($r_{\mathrm{BC}} \approx r_{\mathrm{e}}$, $r_{\mathrm{AB}}$ very large) and the product valley;
- near the origin both internuclear distances are very small, the nuclei repel each other, and the potential energy rises sharply;
- when $r_{\mathrm{AB}}$ and $r_{\mathrm{BC}}$ are both very large, there are three isolated atoms, and the potential energy rises gently to a plateau.

![LEPS potential energy surface for the collinear reaction H + H2 → H2 + H (Sato form: Morse parameters of H2 De = 4.747 eV, a = 19.42 nm⁻¹, re = 0.0742 nm, and Sato parameter 0.135, which makes the saddle-point height agree with the accurate quantum-chemical value of about 40 kJ/mol). Left: contours and the minimum energy path in mass-weighted coordinates, with the saddle point at rAB = rBC = 0.093 nm; right: the potential energy profile along the path](./plots/leps-surface.py)

Potential energy surfaces are obtained by quantum-chemical calculation (solving the electronic Schrödinger equation for a series of nuclear configurations). In 1931 Eyring and Polanyi constructed the first potential energy surface for $\ce{H + H2}$ by a semiempirical method; the LEPS (London–Eyring–Polanyi–Sato) method used for the figure above expresses the energy of the three-atom system in terms of the Coulomb and exchange integrals of the three diatomic pairs, with parameters taken from spectroscopic data of the diatomic molecules, and is the simplest model that still has quantitative meaning. Today's ab initio calculations give a saddle-point height of about $40\,\mathrm{kJ\,mol^{-1}}$ for $\ce{H + H2}$ and $r = 0.0930\,\mathrm{nm}$ at the saddle point.

### 16.2.3. Barrier Height and Zero-Point Energy

The difference $E_{\mathrm{b}}$ between the potential energy at the saddle point and at the bottom of the reactant valley on the potential energy profile is the classical barrier, which can be calculated by quantum chemistry. Molecules always have zero-point vibrational energy, and the energy really required is the difference between the zero-point levels of the activated complex and of the reactants:

$$
E_0 = E_{\mathrm{b}} + N_{\mathrm{A}}\left[\sum_i\tfrac12h\nu_i^{\ddagger} - \sum_j\tfrac12h\nu_j(\text{reactants})\right],
$$
where the sum for the activated complex excludes the "vibration" along the reaction coordinate (an imaginary frequency at the saddle point, 16.3.1). $E_0$ is the activation energy at 0 K, and isotopic substitution changes $E_0$ through the zero-point energy, which is the main source of the **kinetic isotope effect** ([6.1.13](/6.1.13)); light atoms (H) can also pass through the barrier by the **tunnel effect** without having to climb over it.

## 16.3. Transition State Theory

### 16.3.1. Basic Assumptions and the Eyring Equation

Transition state theory (also called activated complex theory) was proposed by Eyring, Evans and Polanyi in 1935. The basic assumptions are:

1. The reactants cross the saddle point along the minimum energy path to form products, and the configuration near the saddle point is the activated complex $\mathrm{X}^{\ddagger}$;
2. The activated complex is in thermodynamic equilibrium (quasi-equilibrium) with the reactants, and its concentration can be calculated by statistical thermodynamics;
3. An activated complex that has crossed the saddle point does not return, and the rate at which it decomposes into products is the reaction rate.

For $\ce{A + B-C <=> [A\cdots B\cdots C]^{\ddagger} -> A-B + C}$, a linear three-atom activated complex has 3 translational, 2 rotational and 4 vibrational degrees of freedom. Of the four vibrations, the two bending vibrations and the symmetric stretching vibration do not lead to decomposition; the asymmetric stretching vibration (B–C lengthens as A–B approaches) lies along the reaction coordinate, and a single "vibration" of it makes the complex decompose into products.

By statistical thermodynamics (the last section of [6.3.11](/6.3.11), equilibrium constants from partition functions), the equilibrium constant expressed in number densities is

$$
K_c^{\ddagger} = \frac{[\mathrm{X}^{\ddagger}]}{[\ce{A}][\ce{BC}]} = \frac{q^{\ddagger}/V}{(q_{\ce{A}}/V)(q_{\ce{BC}}/V)}\,\mathrm{e}^{-\varepsilon_0/k_{\mathrm{B}}T},
$$
where $q$ is the **molecular partition function** with the respective ground states as the zero of energy, and $\varepsilon_0 = E_0/N_{\mathrm{A}}$. Separating from $q^{\ddagger}$ the vibration along the reaction coordinate (frequency $\nu$), its **vibrational partition function**, for $h\nu \ll k_{\mathrm{B}}T$ (this mode is very "soft"), is

$$
q_\nu = \frac{1}{1 - \mathrm{e}^{-h\nu/k_{\mathrm{B}}T}} \approx \frac{k_{\mathrm{B}}T}{h\nu}, \qquad q^{\ddagger} = \frac{k_{\mathrm{B}}T}{h\nu}q^{\ddagger\prime}.
$$
The complex decomposes with frequency $\nu$, $v = \nu[\mathrm{X}^{\ddagger}] = \nu K_c^{\ddagger}[\ce{A}][\ce{BC}]$, and $\nu$ cancels:

$$
k = \frac{k_{\mathrm{B}}T}{h}\,\frac{q^{\ddagger\prime}/V}{(q_{\ce{A}}/V)(q_{\ce{BC}}/V)}\,\mathrm{e}^{-E_0/RT}.
$$

**Definition 16.3.1 (Eyring Equation)** Denote by $K^{\ddagger}$ the equilibrium constant after the degree of freedom along the reaction coordinate has been removed; the rate constant of transition state theory

$$
k = \kappa\frac{k_{\mathrm{B}}T}{h}K^{\ddagger} \tag{16.2}
$$
is called the **Eyring equation**. $\kappa$ is the transmission coefficient, which accounts for trajectories that turn back after crossing the saddle point (making $\kappa < 1$) and for tunneling (which can make $\kappa$ larger than 1); for simple reactions $\kappa = 1$ is often taken.

The universal factor $k_{\mathrm{B}}T/h$ is $6.21 \times 10^{12}\,\mathrm{s^{-1}}$ at $298\,\mathrm{K}$; it is the frequency scale at which the activated complex crosses the barrier and is independent of any specific molecular property. For a general elementary reaction, $k = \frac{k_{\mathrm{B}}T}{h}\frac{q^{\ddagger\prime}/V}{\prod_{\mathrm{B}}(q_{\mathrm{B}}/V)}\mathrm{e}^{-E_0/RT}$, and in terms of molar concentrations there is an extra factor $N_{\mathrm{A}}$ for each reactant molecule (a bimolecular reaction is multiplied by $N_{\mathrm{A}}$).

Treating the "vibration" as the reaction coordinate is not rigorous (the limit $h\nu \ll k_{\mathrm{B}}T$ is artificial). A more rigorous derivation regards a segment of the reaction coordinate of length $\delta$ near the saddle point as a one-dimensional translation: its partition function is $(2\pi m^{\ddagger}k_{\mathrm{B}}T)^{1/2}\delta/h$, the mean speed of the complex toward the products is $(k_{\mathrm{B}}T/2\pi m^{\ddagger})^{1/2}$, and the rate constant for passing through this distance is $(k_{\mathrm{B}}T/2\pi m^{\ddagger})^{1/2}/\delta$; on multiplication, both $\delta$ and $m^{\ddagger}$ cancel, and $k_{\mathrm{B}}T/h$ is obtained again.

**Example 16.3.1 (Collision Theory as a Special Case)** Two atoms A and B react, and the activated complex is a diatomic molecule with internuclear distance $d$. Atoms have only the translational partition function $q_{\mathrm{t}}/V = (2\pi mk_{\mathrm{B}}T)^{3/2}/h^3$; the complex has translation with mass $m_{\mathrm{A}} + m_{\mathrm{B}}$ and rotation with moment of inertia $I = \mu d^2$, $q_{\mathrm{r}} = 8\pi^2Ik_{\mathrm{B}}T/h^2$, and its only vibration is the reaction coordinate. Substituting,

$$
k = \frac{k_{\mathrm{B}}T}{h}\cdot\frac{8\pi^2\mu d^2k_{\mathrm{B}}T}{h^2}\cdot\frac{h^3}{(2\pi\mu k_{\mathrm{B}}T)^{3/2}}\,\mathrm{e}^{-E_0/RT} = \pi d^2\sqrt{\frac{8k_{\mathrm{B}}T}{\pi\mu}}\,\mathrm{e}^{-E_0/RT},
$$
exactly the result of hard-sphere collision theory, Eq. (16.1). For polyatomic molecules, rotational degrees of freedom of the reactants become vibrations in the complex, and the vibrational partition function (about 1–10) is much smaller than the rotational partition function (about $10$–$100$ per degree of freedom), so transition state theory gives a smaller pre-exponential factor than collision theory; a rough estimate for the reaction between nonlinear molecules is $P \sim (q_{\mathrm{v}}/q_{\mathrm{r}})^5 \sim 10^{-5}$: the steric factor thus receives a statistical interpretation.

### 16.3.2. Thermodynamic Form

From $K^{\ddagger}$ thermodynamic quantities of activation can be defined. For an $n$-molecular reaction, $K^{\ddagger}$ is expressed in concentrations, and its relation to the dimensionless standard equilibrium constant is $K^{\ddagger} = K^{\ddagger\circ}(c^\circ)^{1-n}$.

**Definition 16.3.2** The quantity defined by $\Delta^{\ddagger}G^\circ = -RT\ln K^{\ddagger\circ}$ is called the (standard molar) **Gibbs energy of activation**; the quantities $\Delta^{\ddagger}H^\circ$ and $\Delta^{\ddagger}S^\circ$ separated out by $\Delta^{\ddagger}G^\circ = \Delta^{\ddagger}H^\circ - T\Delta^{\ddagger}S^\circ$ are called the **enthalpy of activation** and the **entropy of activation**, respectively. They are the standard molar changes from the reactants to the activated complex (with the reaction coordinate removed).

Substituting into the Eyring equation ($\kappa = 1$),

$$
k = \frac{k_{\mathrm{B}}T}{h}(c^\circ)^{1-n}\exp\left(-\frac{\Delta^{\ddagger}G^\circ}{RT}\right) = \frac{k_{\mathrm{B}}T}{h}(c^\circ)^{1-n}\exp\left(\frac{\Delta^{\ddagger}S^\circ}{R}\right)\exp\left(-\frac{\Delta^{\ddagger}H^\circ}{RT}\right). \tag{16.3}
$$
If a gas-phase reaction takes $p^\circ$ as the standard state, $(c^\circ)^{1-n}$ is replaced by $(p^\circ/RT)^{1-n}$ and the corresponding quantities of activation have different values; the standard state must be stated when they are quoted.

The relation between activation energy and enthalpy of activation is found as follows: taking the logarithm of Eq. (16.2) and differentiating, $E_{\mathrm{a}} = RT^2\frac{\mathrm{d}\ln k}{\mathrm{d}T} = RT + RT^2\frac{\mathrm{d}\ln K^{\ddagger}}{\mathrm{d}T}$. An equilibrium constant expressed in concentrations satisfies $\frac{\mathrm{d}\ln K_c}{\mathrm{d}T} = \frac{\Delta U}{RT^2}$ (ideal systems), so

$$
E_{\mathrm{a}} = \Delta^{\ddagger}U + RT = \Delta^{\ddagger}H - \Delta^{\ddagger}(pV) + RT.
$$
In condensed phases $\Delta^{\ddagger}(pV) \approx 0$ and $E_{\mathrm{a}} = \Delta^{\ddagger}H^\circ + RT$; for ideal gases $\Delta^{\ddagger}(pV) = \Delta^{\ddagger}\nu RT = (1 - n)RT$ and $E_{\mathrm{a}} = \Delta^{\ddagger}H^\circ + nRT$. Substituting back into Eq. (16.3) and comparing with the Arrhenius equation gives the pre-exponential factor

$$
A = \frac{\mathrm{e}\,k_{\mathrm{B}}T}{h}(c^\circ)^{1-n}\mathrm{e}^{\Delta^{\ddagger}S^\circ/R}\ \ (\text{condensed phase}), \qquad A = \frac{\mathrm{e}^n k_{\mathrm{B}}T}{h}(c^\circ)^{1-n}\mathrm{e}^{\Delta^{\ddagger}S^\circ/R}\ \ (\text{gas phase}).
$$

The pre-exponential factor is determined by the entropy of activation: when the activated complex is more "ordered" than the reactants (bimolecular association, ring closure, solvent polarized and oriented), $\Delta^{\ddagger}S^\circ < 0$ and the pre-exponential factor is small; when bonds loosen and rotations become free in a unimolecular decomposition, $\Delta^{\ddagger}S^\circ > 0$. For bimolecular association reactions in solution (such as the Diels–Alder reaction), $\Delta^{\ddagger}S^\circ$ is often between $-100$ and $-150\,\mathrm{J\,mol^{-1}\,K^{-1}}$; one of the actions of enzymes is to bind and orient the substrates beforehand, reducing the loss of entropy on reaction ([6.3.17](/6.3.17)).

**Example 16.3.2** The first-order decomposition of $\ce{N2O5}$ in $\ce{CCl4}$ has $k = 4.69 \times 10^{-5}\,\mathrm{s^{-1}}$ at $298.15\,\mathrm{K}$ and $E_{\mathrm{a}} = 102\,\mathrm{kJ\,mol^{-1}}$ ([Example 7.3.10 of 6.1.7](/6.1.7#ex-7.3.10)). Find the Gibbs energy, enthalpy and entropy of activation.

**Solution** For a unimolecular reaction $n = 1$ and $(c^\circ)^{1-n} = 1$:

$$
\Delta^{\ddagger}G^\circ = RT\ln\frac{k_{\mathrm{B}}T}{hk} = 8.314 \times 298.15 \times \ln\frac{6.21 \times 10^{12}}{4.69 \times 10^{-5}}\,\mathrm{J\,mol^{-1}} = 97.7\,\mathrm{kJ\,mol^{-1}},
$$

$$
\Delta^{\ddagger}H^\circ = E_{\mathrm{a}} - RT = 99.5\,\mathrm{kJ\,mol^{-1}}, \qquad \Delta^{\ddagger}S^\circ = \frac{\Delta^{\ddagger}H^\circ - \Delta^{\ddagger}G^\circ}{T} = +6\,\mathrm{J\,mol^{-1}\,K^{-1}}.
$$
The entropy of activation is small, close to zero and slightly positive, consistent with a unimolecular decomposition in which the structure of the activated complex is similar to that of the reactant and only one bond begins to loosen.

### 16.3.3. Comparison of the Three Treatments

| | Arrhenius equation | Collision theory | Transition state theory |
|---|---|---|---|
| Rate constant | $A\mathrm{e}^{-E_{\mathrm{a}}/RT}$ | $PN_{\mathrm{A}}\pi d_{\mathrm{AB}}^2\bar v_{\mathrm{rel}}\mathrm{e}^{-E_{\mathrm{c}}/RT}$ | $\frac{k_{\mathrm{B}}T}{h}(c^\circ)^{1-n}\mathrm{e}^{\Delta^{\ddagger}S^\circ/R}\mathrm{e}^{-\Delta^{\ddagger}H^\circ/RT}$ |
| Energy parameter | $E_{\mathrm{a}}$ (empirical) | $E_{\mathrm{c}} = E_{\mathrm{a}} - \frac12RT$ | $\Delta^{\ddagger}H^\circ = E_{\mathrm{a}} - RT$ (condensed phase) or $E_{\mathrm{a}} - nRT$ (gas phase) |
| Origin of the pre-exponential factor | Empirical | Collision density × steric factor | Entropy of activation (partition functions) |
| What can be calculated | Only a fit | Order of magnitude for structureless molecules | In principle everything, from the potential energy surface and molecular constants |

The merits of transition state theory: it describes the course of an elementary reaction vividly; it can in principle calculate rate constants from molecular structure and spectroscopic data; it gives a statistical interpretation of the pre-exponential factor (the entropy of activation); and it explains why a reaction needs an activation energy. Its shortcomings and improvements: the assumptions of quasi-equilibrium and "no return" do not always hold (the transmission coefficient; variational transition state theory places the dividing surface where the rate is a minimum); it ignores quantum effects (tunneling makes $k$ at low temperature larger than predicted, especially in the transfer of light atoms); and potential energy surfaces of polyatomic systems are hard to compute. Nevertheless, transition state theory remains the basic language for discussing reaction rates, and the activation parameters, the Hammond postulate and transition state analog inhibitors in organic chemistry and enzymology are all based on it.

## 16.4. Theory of Unimolecular Reactions

### 16.4.1. Experimental Facts

**Definition 16.4.1** An elementary reaction in which only one reactant molecule takes part and products are formed by decomposition or isomerization is called a **unimolecular reaction**, such as the isomerization of cyclopropane to propene, $\ce{C2H5F -> C2H4 + HF}$ and the decomposition of $\ce{N2O5}$.

Gas-phase unimolecular reactions are first order at high pressure but become second order at low pressure, with the rate constant falling gradually in the intermediate pressure region (the fall-off region). The activation energies of these reactions are generally above $150\,\mathrm{kJ\,mol^{-1}}$, and a theoretical explanation is needed of where such large amounts of energy come from and why the order changes with pressure.

### 16.4.2. The Lindemann Mechanism

**Definition 16.4.2 (Lindemann Mechanism)** In 1922 Lindemann proposed that a reactant molecule A is activated into an energized molecule $\ce{A^*}$ by collision with another molecule M (which may be A itself or an inert gas), and $\ce{A^*}$ either is deactivated in the next collision or, after a time lag, decomposes into products:

$$
\ce{A + M <=>[k_1][k_{-1}] A^* + M}, \qquad \ce{A^* ->[k_2] P}.
$$

The time lag is the time that $\ce{A^*}$ needs to redistribute the energy it has acquired within the molecule and concentrate it on the bond to be broken. Applying the **steady-state approximation** ([6.3.15](/6.3.15#def-15.6.1)) to $\ce{A^*}$:

$$
\frac{\mathrm{d}[\ce{A^*}]}{\mathrm{d}t} = k_1[\ce{A}][\ce{M}] - k_{-1}[\ce{A^*}][\ce{M}] - k_2[\ce{A^*}] = 0, \qquad [\ce{A^*}] = \frac{k_1[\ce{A}][\ce{M}]}{k_{-1}[\ce{M}] + k_2},
$$

$$
v = k_2[\ce{A^*}] = k_{\mathrm{uni}}[\ce{A}], \qquad k_{\mathrm{uni}} = \frac{k_1k_2[\ce{M}]}{k_{-1}[\ce{M}] + k_2}. \tag{16.4}
$$

- High pressure ($k_{-1}[\ce{M}] \gg k_2$): $k_{\mathrm{uni}} \to k_\infty = \frac{k_1k_2}{k_{-1}}$, a first-order reaction. Activation and deactivation are fast, $\ce{A^*}$ and A are in pre-equilibrium, and the decomposition is rate-determining.
- Low pressure ($k_{-1}[\ce{M}] \ll k_2$): $k_{\mathrm{uni}} \to k_1[\ce{M}]$; when M is A itself, $v = k_1[\ce{A}]^2$, a second-order reaction. Almost every activated molecule has time to decompose, and the activating collision is rate-determining.

A unimolecular reaction is therefore not "spontaneous"; the molecule must still acquire energy by collisions. Equation (16.4) can be written

$$
\frac{k_{\mathrm{uni}}}{k_\infty} = \frac{1}{1 + k_2/(k_{-1}[\ce{M}])} = \frac{1}{1 + p_{1/2}/p}, \qquad \frac{1}{k_{\mathrm{uni}}} = \frac{1}{k_\infty} + \frac{1}{k_1[\ce{M}]},
$$
where the pressure $p_{1/2}$ at which $k_{\mathrm{uni}} = k_\infty/2$ satisfies $k_{-1}[\ce{M}]_{1/2} = k_2$. The second form shows that $1/k_{\mathrm{uni}}$ against $1/p$ should be a straight line (the Lindemann plot), with intercept $1/k_\infty$ and a slope that gives $k_1$.

![Lindemann mechanism: left, the fall-off curve kuni/k∞ against p/p1/2 (second order at low pressure, first order at high pressure); right, the Lindemann plot, in which 1/kuni against 1/[M] is a straight line](./plots/lindemann-falloff.py)

The thermal decomposition of azomethane at $603\,\mathrm{K}$, the isomerization of cyclopropane and others show this fall-off. The efficiency of the third body depends on its molecular size: a polyatomic molecule can exchange more energy in one collision. The recombination of two atoms, $\ce{I + I + M -> I2 + M}$, is its reverse: the energy released when two atoms combine must be carried away by a third body, otherwise the newly formed molecule dissociates again within one vibration.

### 16.4.3. RRK and RRKM Theories

The Lindemann mechanism is qualitatively correct but has two quantitative problems: estimating $k_1$ by collision theory (considering only the energy in two squared terms along the line of centers) gives a $p_{1/2}$ several orders of magnitude larger than the experimental value; and the experimental plot of $1/k_{\mathrm{uni}}$ against $1/p$ is not a straight line. The key to the improvement is to recognize that the energy of a molecule can be stored in many vibrational modes:

- Hinshelwood pointed out that when the energy is distributed among $s$ vibrational modes, the probability that the molecular energy exceeds $E_0$ is approximately $\frac{1}{(s-1)!}\left(\frac{E_0}{k_{\mathrm{B}}T}\right)^{s-1}\mathrm{e}^{-E_0/k_{\mathrm{B}}T}$, much larger than when only two squared terms are considered, and $k_1$ increases accordingly.
- Rice, Ramsperger and Kassel (RRK, 1927–1928) pointed out further that $k_2$ depends on the energy $E$ of $\ce{A^*}$: with the energy flowing randomly among $s$ oscillators, the probability that more than $E_0$ is concentrated in the reaction coordinate is $(1 - E_0/E)^{s-1}$, and $k_2(E) = \nu(1 - E_0/E)^{s-1}$. The higher the energy of a molecule, the faster it decomposes, and the fall-off curve is therefore broader than predicted by Lindemann.

**Definition 16.4.3** Marcus (1952) combined the RRK idea with transition state theory and calculated the microscopic rate constant as the ratio of the number of quantum states accessible to the activated complex at energy $E$ to the density of states of the reactant, $k_2(E) = \frac{N^{\ddagger}(E - E_0)}{h\rho(E)}$, and then integrated over the energy distribution of $\ce{A^*}$ to obtain $k_{\mathrm{uni}}(p, T)$; this theory is called **RRKM theory** (Rice–Ramsperger–Kassel–Marcus theory).

The central assumption of RRKM theory is that the redistribution of energy within the molecule is much faster than the reaction (the statistical assumption); it can predict fall-off curves quantitatively, and it remains the standard method for calculating pressure-dependent rate constants in combustion and atmospheric chemistry, and is also used in the analysis of ion fragmentation in mass spectrometry.

## 16.5. Introduction to Molecular Reaction Dynamics

**Definition 16.5.1** The discipline that studies, starting from a single molecular collision, how the probability of reaction depends on the collision energy and orientation, how energy is exchanged and partitioned in the reaction, and the distribution of the products over translational, rotational and vibrational states is called **molecular reaction dynamics**. The reaction of A in a definite quantum state $i$ with BC in a definite quantum state $j$ to give products in definite quantum states $m$ and $n$,

$$
\mathrm{A}(i) + \mathrm{BC}(j) \to \mathrm{AB}(m) + \mathrm{C}(n),
$$
is called a **state-to-state reaction**.

The macroscopic rate constant is the average of state-to-state reaction cross sections over all energies and states (16.1.3 is the simplest example), and averaging loses most of the microscopic information. The main experimental methods for studying state-to-state reactions are:

**Definition 16.5.2** The method in which two molecular beams selected in speed and quantum state are crossed in high vacuum (about $10^{-4}\,\mathrm{Pa}$, with a mean free path of tens of meters) so that the molecules undergo only a single collision, and the flux and speed distribution of the products at different scattering angles are measured with a rotatable mass-spectrometric detector, is called **crossed molecular beams**.

Transforming from the laboratory frame to the center-of-mass frame gives contour maps of the product "flux–speed–angle", which directly show the dynamics of the collision:

- Stripping model: in $\ce{K + I2 -> KI + I}$, K strips an I atom from $\ce{I2}$ at a large impact parameter and continues forward, and the product KI is scattered forward (this is also the harpoon mechanism, with a very large reaction cross section).
- Rebound model: in $\ce{K + CH3I -> KI + CH3}$ only nearly head-on collisions react, and KI rebounds backward.
- Complex model: in $\ce{Cs + RbCl -> CsCl + Rb}$ the intermediate complex formed lives several rotational periods, loses its "memory" of the direction of incidence after several rotations, and the products are scattered symmetrically forward and backward in the center-of-mass frame.

In a direct reaction the collision time is shorter than the rotational period (about $10^{-12}\,\mathrm{s}$), and the energy has no time to redistribute within the molecule, which is exactly contrary to the statistical assumption of RRKM. Two other methods are infrared chemiluminescence (vibrationally and rotationally excited products formed in the reaction emit infrared radiation at low pressure, from whose spectrum the initial energy-state distribution of the products is deduced) and laser-induced fluorescence (a tunable laser excites products in a given vibrational–rotational level to the upper electronic state, and the fluorescence is measured).

These experiments gave the connection between the dynamics of reactions and the shape of the potential energy surface, known as the *Polanyi rules*: for an exothermic reaction whose barrier lies on the reactant side (an early barrier), translational energy is more effective in crossing the barrier and the energy released appears mostly as vibrational energy of the products (which can therefore be used in chemical lasers); when the barrier lies on the product side (a late barrier), the vibrational energy of the reactants is more effective. Herschbach, Y. T. Lee (crossed molecular beams) and Polanyi (infrared chemiluminescence) received the 1986 Nobel Prize in Chemistry for this work; Zewail used femtosecond lasers to observe directly the breaking of chemical bonds and the motion in the region of the transition state (femtochemistry), for which he received the 1999 Nobel Prize in Chemistry.

## Summary

| Topic | Key points |
|---|---|
| Collision density | $Z_{\mathrm{AB}} = \pi d_{\mathrm{AB}}^2\bar v_{\mathrm{rel}}n_{\mathrm{A}}n_{\mathrm{B}}$, $\bar v_{\mathrm{rel}} = \sqrt{8k_{\mathrm{B}}T/\pi\mu}$ |
| Reaction cross section | $\sigma_{\mathrm{r}} = \pi d_{\mathrm{AB}}^2(1 - \varepsilon_{\mathrm{c}}/\varepsilon)$; integration over the Maxwell–Boltzmann distribution gives $k = \pi d_{\mathrm{AB}}^2\bar v_{\mathrm{rel}}\mathrm{e}^{-E_{\mathrm{c}}/RT}$ |
| Collision theory and Arrhenius | $E_{\mathrm{a}} = E_{\mathrm{c}} + \frac12RT$; $P$ cannot be calculated |
| Potential energy surface | Reactant valley, product valley, saddle point, minimum energy path; $E_0 = E_{\mathrm{b}} + \Delta(\text{zero-point energy})$ |
| Eyring equation | $k = \kappa\frac{k_{\mathrm{B}}T}{h}K^{\ddagger}$, with $K^{\ddagger}$ calculated from partition functions (reaction coordinate removed) |
| Thermodynamic form | $k = \frac{k_{\mathrm{B}}T}{h}(c^\circ)^{1-n}\mathrm{e}^{\Delta^{\ddagger}S^\circ/R}\mathrm{e}^{-\Delta^{\ddagger}H^\circ/RT}$; $E_{\mathrm{a}} = \Delta^{\ddagger}H^\circ + RT$ (condensed phase), $+nRT$ (gas phase) |
| Unimolecular reactions | Lindemann: $k_{\mathrm{uni}} = \frac{k_1k_2[\ce{M}]}{k_{-1}[\ce{M}] + k_2}$, first order at high pressure and second order at low pressure; RRKM accounts for the distribution of energy among vibrational modes |
| Molecular reaction dynamics | State-to-state reactions; crossed molecular beams (stripping, rebound, complex), infrared chemiluminescence, laser-induced fluorescence |

## Questions

1. Why is the fraction of effective collisions in collision theory $\mathrm{e}^{-E_{\mathrm{c}}/RT}$, and not the fraction of molecular pairs whose relative translational energy exceeds $E_{\mathrm{c}}$?

   **Answer** See 16.1.3: flux weighting and the energy dependence of the reaction cross section together give exactly the Boltzmann factor.

2. What is the physical meaning of $k_{\mathrm{B}}T/h$ in the rate constant of transition state theory? Why is it independent of the kind of molecule?

   **Answer** It is the frequency scale at which the activated complex crosses the saddle point along the reaction coordinate; in the derivation the frequency (or mass) of the reaction coordinate cancels exactly.

3. A unimolecular reaction becomes second order at low pressure. Does this mean that it has become a bimolecular reaction?

   **Answer** No. The rate-determining step changes from the decomposition to the activating collision, the latter being bimolecular; the decomposition step is always unimolecular.
