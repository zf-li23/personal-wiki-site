---
title: Real Gases and Transport Processes
source_hash: 272b294993d3
---

The **ideal gas** of the previous chapter rests on two idealizations: the molecules have no size, and there is no interaction between molecules apart from collisions. This chapter removes both idealizations and leaves the ideal gas in two directions. The first concerns the **equation of state** of an **equilibrium state**: at high pressure and low temperature, the volume of the molecules and the attraction between them can no longer be neglected, the gas deviates from $pV = nRT$ and eventually liquefies; the van der Waals equation describes this deviation, the liquefaction and the critical point with just two parameters. The second concerns nonequilibrium states: because molecules have size, they collide with one another, and the collisions determine the mean free path, which in turn determines how fast the three transport processes of heat conduction, viscosity and diffusion proceed. The macroscopic laws of transport (Fourier's law and Fick's law) are the physical origin of the heat equation in the partial differential equations course ([2.5.1](/2.5.1)); here we compute their coefficients from the kinetic theory. The next chapter, [5.2.3](/5.2.3), returns to equilibrium states and turns to the methods of thermodynamics.

## 2.1. Isotherms of a Real Gas

At ordinary temperature and pressure a real gas approximately obeys the ideal gas equation of state; at very high pressure or very low **temperature** the deviation becomes significant. In 1869 Andrews measured the isotherms ($p$–$V_{\mathrm{m}}$ curves) of $\ce{CO2}$ at various temperatures, which revealed the whole picture of the gas–liquid transition:

- At higher temperatures (e.g., $48.1\,{}^\circ\mathrm{C}$), the isotherm is close to the hyperbola of an ideal gas, and the gas does not liquefy however it is compressed.
- At lower temperatures (e.g., $13\,{}^\circ\mathrm{C}$, $21\,{}^\circ\mathrm{C}$), the gas begins to liquefy when compressed isothermally to a certain volume; on further compression the pressure stays constant while more and more liquid forms, until all the gas has liquefied; after that the volume hardly changes with pressure (a liquid is hard to compress). The horizontal segment of the isotherm corresponds to the coexistence of vapor and liquid.
- As the temperature rises, the horizontal segment becomes shorter; on the isotherm at $31.1\,{}^\circ\mathrm{C}$ it shrinks to a point, called the critical point.

**Definition 2.1.1** The state at which the horizontal segment of an isotherm shrinks to a point is called the **critical point**, and this isotherm is called the critical isotherm. Its temperature $T_{\mathrm{c}}$ is called the **critical temperature**, and the pressure $p_{\mathrm{c}}$ and molar volume $V_{\mathrm{m,c}}$ at the critical point are called the critical pressure and the critical molar volume. The pressure at which vapor and liquid coexist is called the **saturated vapor pressure** at that temperature.

The critical parameters of $\ce{CO2}$ are $T_{\mathrm{c}} \approx 304.1\,\mathrm{K}$ ($31.0\,{}^\circ\mathrm{C}$), $p_{\mathrm{c}} \approx 7.38\,\mathrm{MPa}$ and $V_{\mathrm{m,c}} \approx 94\,\mathrm{cm^3\,mol^{-1}}$. At the critical point the molar volumes of liquid and gas are equal and the two are no longer distinguishable; near the critical point the density **fluctuations** become very large, and the scattered light turns the substance milky white (critical opalescence).

The $p$–$V_{\mathrm{m}}$ diagram is divided into four regions according to the state:

| Region | Location | Property |
|---|---|---|
| Gas | Above the critical isotherm | Cannot be liquefied by isothermal compression alone |
| Vapor | Below the critical isotherm, to the right of the coexistence region | Can be liquefied by isothermal compression ("vapor" is a gas that can be liquefied) |
| Vapor–liquid coexistence | Inside the bell-shaped coexistence region | The pressure equals the saturated vapor pressure, which depends only on temperature and not on volume |
| Liquid | To the left of the coexistence region | Almost incompressible |

The saturated vapor pressure increases with temperature. When a liquid is heated until its saturated vapor pressure equals the external pressure, bubbles can form inside the liquid as well, which is boiling; hence the higher the external pressure, the higher the boiling point. Heat water at constant pressure at $101.325\,\mathrm{kPa}$: the water begins to boil when its temperature reaches $100\,{}^\circ\mathrm{C}$ (strictly, $99.97\,{}^\circ\mathrm{C}$); on further heating the temperature stays constant as the water absorbs the heat of vaporization until it has all become steam; only then does the temperature of the steam continue to rise. On a high plateau the external pressure is low, water boils below $100\,{}^\circ\mathrm{C}$, and its temperature cannot rise higher; a pressure cooker raises the pressure inside the pot and thereby raises the boiling point.

Gases whose critical temperature is above room temperature ($\ce{CO2}$, $\ce{NH3}$) can be liquefied at room temperature by compression; gases with very low critical temperatures ($155\,\mathrm{K}$ for $\ce{O2}$, $126\,\mathrm{K}$ for $\ce{N2}$) must first be cooled below the critical temperature before they can be liquefied, and such gases were once called "permanent gases". The hardest to liquefy is helium ($T_{\mathrm{c}} \approx 5.2\,\mathrm{K}$); Kamerlingh Onnes first liquefied it in 1908, and in 1911, cooling mercury with liquid helium, he discovered superconductivity: a breakthrough in low-temperature technology led to new physics.

## 2.2. The van der Waals Equation

### 2.2.1. Intermolecular Forces

Intermolecular forces are electromagnetic in origin and complicated in form, but their general character is "attractive at long range, repulsive at short range":

- When the intermolecular distance $r$ is greater than the effective range $s$ (about $10^{-9}\,\mathrm{m}$, a few to ten molecular diameters), the force can be neglected;
- For smaller $r$, the force is attractive;
- At the equilibrium distance $r_0$ (of the same order of magnitude as the effective molecular diameter $d \sim 10^{-10}\,\mathrm{m}$), the net force is zero;
- For $r < r_0$, the repulsion increases sharply as the distance decreases.

A commonly used model is the Lennard-Jones potential
$$
E_{\mathrm{p}}(r) = E_0\left[\left(\frac{r_0}{r}\right)^{12} - 2\left(\frac{r_0}{r}\right)^6\right],
$$
in which the $r^{-6}$ term is the attractive **dispersion** force between the instantaneous dipole of one molecule and the induced dipole of another, and the $r^{-12}$ term is an empirical form for the repulsion due to overlapping electron clouds. The **potential energy** has its minimum $-E_0$ at the equilibrium distance $r_0$, where the force $F = -\mathrm{d}E_{\mathrm{p}}/\mathrm{d}r$ vanishes (for the relation between the **potential energy curve** and the force, see [5.1.4](/5.1.4)).

![Intermolecular potential and force: Lennard-Jones model (left) and the attracting hard-sphere model used by van der Waals (right)](./plots/lennard-jones.py)

### 2.2.2. The van der Waals Gas Model

van der Waals (1873) made two corrections to the ideal gas model, obtaining a hard-sphere model with attraction (right panel):

1. A molecule is a hard sphere of diameter $d$ (the volume of the molecules is taken into account);
2. For $d < r < s$, there is a constant attractive force between molecules (the attraction between molecules is taken into account).

### 2.2.3. The van der Waals Equation

Consider first $1\,\mathrm{mol}$ of gas, with $p$ the measured pressure and $V_{\mathrm{m}}$ the volume of the container.

Volume correction: molecules have size, so the space available to each molecule is less than $V_{\mathrm{m}}$; call it $V_{\mathrm{m}} - b$, so that $p = \frac{RT}{V_{\mathrm{m}} - b}$. The constant $b$ is related to the volume of the molecules themselves: the centers of two hard spheres cannot come closer than $d$, so the volume from which a pair of molecules exclude each other is a sphere of radius $d$, which gives $b = 4N_{\mathrm{A}} \cdot \frac{\pi d^3}{6}$, that is, 4 times the volume of the molecules in $1\,\mathrm{mol}$.

Correction for attraction: a molecule in the interior of the container is attracted by the surrounding molecules equally in all directions, and the attractions cancel; a molecule near the wall (within a distance $s$) experiences a net attraction directed toward the interior, so its **momentum** is reduced when it hits the wall, and the measured pressure is smaller than $\frac{RT}{V_{\mathrm{m}} - b}$ by an internal pressure $p_{\mathrm{in}}$. The internal pressure $p_{\mathrm{in}}$ is proportional both to the number of molecules striking the wall per unit time and to the net attraction on each molecule; both are proportional to the number density, so $p_{\mathrm{in}} \propto n_V^2 \propto 1/V_{\mathrm{m}}^2$, which we write as $p_{\mathrm{in}} = a/V_{\mathrm{m}}^2$.

**Definition 2.2.1 (van der Waals Equation)** The equation of state
$$
\left(p + \frac{a}{V_{\mathrm{m}}^2}\right)(V_{\mathrm{m}} - b) = RT
\tag{2.1}
$$
is called the **van der Waals equation**; for a gas of amount of substance $n$ and volume $V$ it is written $\left(p + \frac{n^2a}{V^2}\right)(V - nb) = nRT$. The constants $a$ (related to the intermolecular attraction) and $b$ (related to the volume of the molecules) differ from gas to gas and are determined by experiment. A gas that obeys it is called a van der Waals gas.

At ordinary temperature and pressure, both $b/V_{\mathrm{m}}$ and $p_{\mathrm{in}}/p$ are only of order $10^{-3}$, so the two corrections can be neglected and the equation reduces to that of an ideal gas. The following table gives experimental data for $\ce{N2}$ at $273\,\mathrm{K}$ ($RT \approx 2271\,\mathrm{J\,mol^{-1}}$):

| $p/\mathrm{MPa}$ | $V_{\mathrm{m}}/(\mathrm{L\,mol^{-1}})$ | $pV_{\mathrm{m}}/(\mathrm{J\,mol^{-1}})$ | $(p + a/V_{\mathrm{m}}^2)(V_{\mathrm{m}} - b)/(\mathrm{J\,mol^{-1}})$ |
|---|---|---|---|
| 0.101 | 22.41 | 2271 | 2271 |
| 10.13 | 0.2224 | 2253 | 2254 |
| 50.66 | 0.06235 | 3159 | 2285 |
| 91.19 | 0.04825 | 4400 | 2265 |

The last column uses $a = 0.079\,\mathrm{Pa\,m^6\,mol^{-2}}$ and $b = 3.0 \times 10^{-5}\,\mathrm{m^3\,mol^{-1}}$ (fitted to this set of data). At $900$ atmospheres $pV_{\mathrm{m}}$ is already nearly twice $RT$, yet the van der Waals equation still differs from $RT$ by less than $1\%$. However, the best values of $a$ and $b$ depend on the range over which they are fitted: the values determined from the critical parameters ($a \approx 0.137\,\mathrm{Pa\,m^6\,mol^{-2}}$ and $b \approx 3.9 \times 10^{-5}\,\mathrm{m^3\,mol^{-1}}$ for $\ce{N2}$) give deviations of tens of percent at such high pressures. The value of the van der Waals equation lies mainly in its qualitative content: with the simplest physical model it yields both the gas–liquid transition and the critical point (§2.2.5); quantitative calculations mostly use the virial expansion or other empirical equations of state.

The attraction of the wall molecules on the gas molecules does not affect the pressure: it accelerates molecules approaching the wall and decelerates molecules leaving it, and the two **impulses** cancel; moreover, pressure is by definition the force exerted by the gas on the wall, and the action of the wall molecules on the gas is not part of it.

### 2.2.4. Internal Energy of a van der Waals Gas

The **internal energy** of an ideal gas depends only on temperature: $U = \frac{i}{2}nRT$. The molecules of a van der Waals gas attract one another, so when the volume increases the internal pressure does negative **work** and the intermolecular potential energy increases. Taking the potential energy to be zero at $V \to \infty$,
$$
E_{\mathrm{p}}(V) = -\int_V^{\infty} p_{\mathrm{in}}\,\mathrm{d}V' = -\int_V^{\infty}\frac{n^2a}{V'^2}\,\mathrm{d}V' = -\frac{n^2a}{V},
$$
$$
U = \frac{i}{2}nRT - \frac{n^2a}{V} = U(T, V).
$$
Hence when a van der Waals gas expands freely into a vacuum (with its internal energy unchanged), its temperature falls ([5.2.3](/5.2.3)).

### 2.2.5. van der Waals Isotherms

Expanding Eq. (2.1) gives a cubic equation in $V_{\mathrm{m}}$, $pV_{\mathrm{m}}^3 - (pb + RT)V_{\mathrm{m}}^2 + aV_{\mathrm{m}} - ab = 0$. At high temperature there is only one real root and the isotherm is monotonic; at low temperature, over a certain range of pressure there are three real roots and the isotherm has a "backward bend". The temperature at which the three roots merge into one is the critical temperature: the critical point is an inflection point of the isotherm, with $\left(\frac{\partial p}{\partial V_{\mathrm{m}}}\right)_T = 0$ and $\left(\frac{\partial^2 p}{\partial V_{\mathrm{m}}^2}\right)_T = 0$, from which we obtain

**Formula 2.2.1**
$$
V_{\mathrm{m,c}} = 3b, \qquad T_{\mathrm{c}} = \frac{8a}{27Rb}, \qquad p_{\mathrm{c}} = \frac{a}{27b^2}, \qquad \frac{p_{\mathrm{c}}V_{\mathrm{m,c}}}{RT_{\mathrm{c}}} = \frac{3}{8}.
$$

For real gases, $p_{\mathrm{c}}V_{\mathrm{m,c}}/(RT_{\mathrm{c}})$ is mostly between $0.23$ and $0.31$, smaller than $0.375$, which again shows that the equation is only qualitatively correct. With the reduced variables $p_{\mathrm{r}} = p/p_{\mathrm{c}}$, $V_{\mathrm{r}} = V_{\mathrm{m}}/V_{\mathrm{m,c}}$ and $T_{\mathrm{r}} = T/T_{\mathrm{c}}$, the equation takes a form containing neither $a$ nor $b$:
$$
\left(p_{\mathrm{r}} + \frac{3}{V_{\mathrm{r}}^2}\right)(3V_{\mathrm{r}} - 1) = 8T_{\mathrm{r}},
$$
that is, different gases at the same reduced temperature and reduced pressure have the same reduced volume (the law of corresponding states), which holds approximately for real gases.

![Van der Waals isotherms in reduced variables; below the critical temperature the horizontal line is drawn by the equal-area rule](./plots/van-der-waals-isotherms.py)

Below the critical temperature, the backward bend of the van der Waals isotherm differs from the horizontal segment seen in experiments. Draw the actual horizontal segment across the bend (the solid line in the figure); it meets the isotherm at two points, one on the vapor side and one on the liquid side:

- The large-volume part to the right of the horizontal segment is the vapor state and the small-volume part to the left is the liquid state, in agreement with experiment;
- Between the minimum and the maximum of the bend, $\left(\frac{\partial p}{\partial V}\right)_T > 0$: the pressure increases as the volume increases, any small disturbance is amplified, and such states are unstable and do not occur in practice;
- Between the intersection on the vapor side and the maximum lies supersaturated vapor (pressure above the saturated vapor pressure without liquefaction), and between the intersection on the liquid side and the minimum lies superheated liquid (temperature above the boiling point without boiling). These are metastable states: without condensation nuclei or vaporization nuclei they can persist for some time, but with a disturbance they quickly turn into vapor–liquid coexistence.

The height of the horizontal segment (the saturated vapor pressure) is determined by Maxwell's equal-area rule: the upper and lower areas enclosed between the horizontal line and the bend are equal (this is equivalent to the equality of the chemical potentials of the two phases, a matter for physical chemistry).

Metastable states have important applications in particle physics. A Wilson cloud chamber contains supersaturated vapor: a charged particle ionizes the gas along its path, the ions act as condensation nuclei, and a trail of droplets is left behind. Glaser's bubble chamber contains superheated liquid: a string of bubbles forms along the track of a particle. By photographing such tracks, one can study the types of particles, their momenta and their interactions.

## 2.3. The Mean Free Path of Gas Molecules

Molecular **speeds** are hundreds of meters per second, yet gases diffuse very slowly (when a perfume bottle is opened, it takes a while before the scent is noticed at a distance), because the molecules collide constantly, each collision changes the direction of motion, and they follow a zigzag path. Collisions are the fundamental reason why nonequilibrium states evolve toward equilibrium.

**Definition 2.3.1** The average number of collisions a molecule makes with other molecules per unit time is called the **mean collision frequency** $\bar z$; the average distance a molecule travels between two successive collisions is called the **mean free path** $\bar\lambda$. Clearly $\bar\lambda = \bar v/\bar z$.

The model for calculating $\bar z$: there is only one kind of molecule, and the molecules are hard spheres of diameter $d$. First suppose that all other molecules are at rest and the molecule under consideration moves with the relative speed: every molecule whose center lies inside the cylinder with the molecule's trajectory as axis and radius $d$ will be hit by it. The cross-sectional area of this cylinder,
$$
\sigma = \pi d^2,
$$
is called the *collision cross section*. The volume swept out by the cylinder per unit time is $\sigma\bar v_{\mathrm{rel}}$, where $\bar v_{\mathrm{rel}}$ is the mean relative speed between molecules, so $\bar z = \sigma\bar v_{\mathrm{rel}}n_V$.

In reality the other molecules are also moving. Each component of the difference $\boldsymbol{v}_1 - \boldsymbol{v}_2$ of the **velocities** of two molecules is the difference of two independent $\mathcal{N}(0, k_{\mathrm{B}}T/m)$ variables and follows $\mathcal{N}(0, 2k_{\mathrm{B}}T/m)$, so the **relative velocity** also follows a Maxwell distribution, with $m$ replaced by the **reduced mass** $m/2$: $\bar v_{\mathrm{rel}} = \sqrt{2}\,\bar v$. (A common heuristic is that the angle between the velocities of two molecules is on average $90^\circ$, so the relative speed is about $\sqrt{2}\,\bar v$.) Hence

**Formula 2.3.1**
$$
\bar z = \sqrt{2}\,\pi d^2\bar v\,n_V, \qquad \bar\lambda = \frac{\bar v}{\bar z} = \frac{1}{\sqrt{2}\,\pi d^2 n_V} = \frac{k_{\mathrm{B}}T}{\sqrt{2}\,\pi d^2 p}.
$$

At a fixed temperature, $\bar\lambda \propto 1/p$:

| $p$ | $\bar\lambda$ (air, $273\,\mathrm{K}$) | Example |
|---|---|---|
| $101\,\mathrm{kPa}$ | $\sim 7 \times 10^{-8}\,\mathrm{m}$ | Atmosphere at ground level |
| $10^{-2}\,\mathrm{Pa}$ | $\sim 0.7\,\mathrm{m}$ | Inside an incandescent bulb |
| $10^{-6}\,\mathrm{Pa}$ | $\sim 7\,\mathrm{km}$ | Altitude of a few hundred kilometers |

**Example 2.3.1** The effective diameter of an oxygen molecule is $d \approx 3.6 \times 10^{-10}\,\mathrm{m}$. Find $\bar z$ and $\bar\lambda$ at $T = 273\,\mathrm{K}$ and $p = 101\,\mathrm{kPa}$.

Solution: $\bar v = \sqrt{8RT/(\pi M)} \approx 425\,\mathrm{m\,s^{-1}}$ and $n_V = p/(k_{\mathrm{B}}T) \approx 2.69 \times 10^{25}\,\mathrm{m^{-3}}$, so
$$
\bar z = \sqrt{2}\,\pi d^2\bar v\,n_V \approx 6.6 \times 10^9\,\mathrm{s^{-1}}, \qquad \bar\lambda = \bar v/\bar z \approx 6.5 \times 10^{-8}\,\mathrm{m}.
$$
The mean free path is about 200 times the molecular diameter and 20 times the mean distance between molecules ($n_V^{-1/3} \approx 3.3 \times 10^{-9}\,\mathrm{m}$); a molecule collides about $10^{10}$ times per second.

**Remark 2.3.1** The free path itself is random. The probability that a molecule is hit while traveling a distance $\mathrm{d}x$ is $\mathrm{d}x/\bar\lambda$, independent of the distance already traveled, so the free path follows an **exponential distribution**: the probability that the free path exceeds $x$ is $\mathrm{e}^{-x/\bar\lambda}$, and its mean is $\bar\lambda$. This is the same mathematical structure as the distribution of lifetimes in radioactive decay.

## 2.4. Transport Processes

When the temperature, flow velocity or density is not uniform across a system, the system is in a nonequilibrium state. Left undisturbed, the system spontaneously evolves toward a uniform equilibrium state, and in the process energy, momentum or mass is transferred from one place to another; such processes are called *transport processes*. The three basic transport processes are:

| Process | Nonuniform quantity | Quantity transported | Macroscopic law | Transport coefficient |
|---|---|---|---|---|
| Heat conduction | Temperature $T$ | Energy of thermal motion | **Fourier's law** | Thermal conductivity $\kappa$ |
| Viscosity (internal friction) | Directed flow velocity $u$ | Momentum of directed motion | Newton's law of viscosity | Viscosity $\eta$ |
| Diffusion | Density $\rho$ | Mass | **Fick's law** | Diffusion coefficient $D$ |

In a gas, all three kinds of transfer are carried out by the **thermal motion** of the molecules and their collisions: a molecule flies from one place to another carrying the energy, momentum or mass of its original location, and hands them over to the local molecules through collisions. A general theory of nonequilibrium states has still not been fully established, and below we use only simplified estimates based on the mean free path.

### 2.4.1. Heat Conduction

Let the temperature of the gas vary along the $x$ direction, $T = T(x)$. Experiments show that the heat passing through an area element $\mathrm{d}S$ perpendicular to the $x$ axis in time $\mathrm{d}t$ is
$$
\delta Q = -\kappa\left(\frac{\mathrm{d}T}{\mathrm{d}x}\right)_{x_0}\mathrm{d}S\,\mathrm{d}t,
\tag{2.2}
$$
where the minus sign indicates that heat flows in the direction of decreasing temperature, and the proportionality coefficient $\kappa$ is called the *thermal conductivity*, with unit $\mathrm{W\,m^{-1}\,K^{-1}}$. In three dimensions the heat flux density is $\boldsymbol{q} = -\kappa\nabla T$; this is **Fourier's law**. Combined with conservation of energy it gives the **heat equation** $\rho c\,\partial_t T = \kappa\Delta T$ ([2.5.1](/2.5.1)), where $\kappa/(\rho c)$ is the thermal diffusivity. The thermal conductivity of gases is small: about $0.026\,\mathrm{W\,m^{-1}\,K^{-1}}$ for air, between $10^{-2}$ and $10^{-1}$ for various gases (largest for the light $\ce{H2}$ and $\ce{He}$), and of order $10^2$ for metals.

Microscopic explanation: for there to be heat conduction without diffusion, the numbers of molecules exchanged across the two sides of $\mathrm{d}S$ in $\mathrm{d}t$ must be equal; call this number $\mathrm{d}N$. Let the mean energy of the molecules coming from the left be $\bar\varepsilon_1$ and that of those coming from the right be $\bar\varepsilon_2$; then the net energy passing through $\mathrm{d}S$ is $\delta Q = (\bar\varepsilon_1 - \bar\varepsilon_2)\,\mathrm{d}N$. We make the following simplifications:

1. In computing $\mathrm{d}N$, we ignore the temperature difference and assume that all molecules move with speed $\bar v$ and that $1/6$ of them move in each of the six directions $\pm x$, $\pm y$, $\pm z$, so that $\mathrm{d}N = \frac{1}{6}n_V\bar v\,\mathrm{d}S\,\mathrm{d}t$;
2. The last collision of a molecule before it crosses $\mathrm{d}S$ occurs at a distance $\bar\lambda$ from $\mathrm{d}S$, and in that collision the molecule acquires the local mean energy.

Then $\bar\varepsilon_1 - \bar\varepsilon_2 = -\frac{\mathrm{d}\bar\varepsilon}{\mathrm{d}T}\left(\frac{\mathrm{d}T}{\mathrm{d}x}\right)_{x_0}\cdot 2\bar\lambda$. For a molecule, $\frac{\mathrm{d}\bar\varepsilon}{\mathrm{d}T} = mc_V$, where $c_V$ is the specific heat capacity of the gas at constant volume ([5.2.3](/5.2.3)). Substituting and writing $\rho = n_Vm$:
$$
\delta Q = -\frac{1}{3}\rho c_V\bar v\bar\lambda\left(\frac{\mathrm{d}T}{\mathrm{d}x}\right)_{x_0}\mathrm{d}S\,\mathrm{d}t.
$$

**Formula 2.4.1** Comparing with Eq. (2.2),
$$
\kappa = \frac{1}{3}\rho c_V\bar v\bar\lambda.
$$

Since $\rho \propto n_V$ and $\bar\lambda \propto 1/n_V$, $\kappa$ is independent of pressure (density) and increases only with temperature ($\bar v \propto \sqrt{T}$). Intuitively, when the pressure is lowered there are fewer molecules to transfer energy, but each molecule travels farther in one flight, and the two effects exactly cancel. Experiments confirm that $\kappa$ is independent of pressure over a wide range of pressures.

At sufficiently low pressure the experimental result is different: $\kappa \propto p$. The reason is that $\bar\lambda$ cannot exceed the linear size $l$ of the container: when $p$ falls below the pressure $p^{*} = \frac{k_{\mathrm{B}}T}{\sqrt{2}\,\pi d^2 l}$ at which $\bar\lambda = l$, $\bar\lambda = l$ no longer changes, and then $\kappa \propto \rho \propto p$.

**Example 2.4.1 (The Vacuum Flask)** The gap in the wall of a vacuum flask has thickness $l = 5\,\mathrm{mm}$. To what pressure must it be evacuated to provide effective insulation?

Solution: Above $p^{*}$, pumping does not reduce the heat conduction; below $p^{*}$, $\kappa \propto p$, and the higher the vacuum, the better the insulation. Take $T = 350\,\mathrm{K}$ and an air molecule diameter $d \approx 3.3 \times 10^{-10}\,\mathrm{m}$:
$$
p^{*} = \frac{k_{\mathrm{B}}T}{\sqrt{2}\,\pi d^2 l} \approx 2\,\mathrm{Pa},
$$
that is, about $2 \times 10^{-5}$ atmosphere; the pressure in the gap must be well below this value.

### 2.4.2. Viscosity

Let the gas flow in the $x$ direction with a flow velocity $u(z)$ that varies with $z$. Between two adjacent layers of gas there is a pair of tangential forces (internal friction) of equal magnitude and opposite direction: the faster layer drags the slower one. Experiments show that the internal friction force on an interface of area $\mathrm{d}S$ is
$$
\mathrm{d}F = -\eta\frac{\mathrm{d}u}{\mathrm{d}z}\,\mathrm{d}S,
$$
which is called Newton's law of viscosity, and $\eta$ is called the *viscosity* (also the dynamic viscosity), with unit $\mathrm{Pa\,s}$. In the molecular picture, internal friction is the transport of directed momentum: molecules flying from the fast layer to the slow layer carry more directed momentum $mu$ with them, and vice versa. The same argument as for heat conduction (replacing the $\bar\varepsilon$ carried by each molecule with $mu$) gives

**Formula 2.4.2**
$$
\eta = \frac{1}{3}\rho\bar v\bar\lambda.
$$

The viscosity $\eta$ is likewise independent of pressure and increases with temperature. This was an unexpected prediction that Maxwell obtained in 1860 (intuition suggests that a dilute gas should be less "viscous"); he soon confirmed it experimentally, and it became one of the strongest early pieces of evidence for the kinetic theory of gases. Note that the viscosity of a liquid decreases as the temperature rises, by a completely different mechanism.

### 2.4.3. Diffusion

Let the density $\rho$ of one component of a gas mixture vary along the $x$ direction (with uniform total pressure and temperature). The mass of that component transported through an area element $\mathrm{d}S$ in time $\mathrm{d}t$ is
$$
\mathrm{d}m = -D\frac{\mathrm{d}\rho}{\mathrm{d}x}\,\mathrm{d}S\,\mathrm{d}t,
$$
which is **Fick's law**, and $D$ is called the diffusion coefficient, with unit $\mathrm{m^2\,s^{-1}}$. Replacing the carried quantity with the mass $m$, the same argument gives

**Formula 2.4.3**
$$
D = \frac{1}{3}\bar v\bar\lambda.
$$

Here $D \propto 1/p$ and $D \propto T^{3/2}$. Combined with conservation of mass, Fick's law also leads to the heat equation (the diffusion equation); microscopically, diffusion is a random walk of the molecules, and the mean square **displacement** grows linearly with time, $\overline{x^2} = 2Dt$.

The three transport coefficients are related by the simple relations $\eta = \rho D$ and $\kappa = \eta c_V$. The mean-free-path theory correctly gives the dependence of each coefficient on pressure and temperature, but the numerical factors are only approximate: the rigorous theory (Chapman–Enskog) gives $\kappa/(\eta c_V)$ of about $2.5$ for a monatomic gas, not 1, because fast molecules both travel farther and carry more energy, a correlation that the simplified model neglects.

## Questions

1. Why does lowering the pressure not reduce the thermal conductivity of a gas at first, while a high vacuum provides very good insulation?
   Hint: in $\kappa = \frac{1}{3}\rho c_V\bar v\bar\lambda$ the product $\rho\bar\lambda$ is independent of pressure until $\bar\lambda$ reaches the linear size of the container (Example 2.4.1).
2. Why do the viscosities of liquids and gases vary with temperature in opposite ways?
   Hint: the internal friction of a gas comes from the transfer of molecules between layers, and the higher the temperature, the larger $\bar v$; the internal friction of a liquid comes from attraction between molecules, and as the temperature rises the molecules break free of their neighbors more easily.
