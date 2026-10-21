---
title: Steady Currents
description: Current and current density, the charge continuity equation, steady currents and steady electric fields, Kirchhoff's current law, Ohm's law in integral and differential form and the computation of resistance, electromotive force and thermoelectricity, the Ohm's law of a complete circuit and Kirchhoff's voltage law, joint solution of steady current fields and electrostatic fields, the Drude model and Joule's law, and charging and discharging of RC circuits.
source_hash: 9c77ddac8c5d
---

The previous chapters studied the electric field of stationary charges. Charges in organized motion form a current; a current whose distribution does not change with time is called a steady current, and this is the first step from electrostatics toward electrodynamics. In a steady current the charge distribution is constant, and the electric field it produces still satisfies the two basic theorems of the electrostatic field. Unlike in electrostatics, however, the **electric field strength** inside a **conductor** is not zero: the field does work on the charges and converts energy into heat, and maintaining it requires the non-electrostatic force supplied by a source. This chapter first describes current by the vector field of current density and writes the current continuity equation from the **law of conservation of charge**. It then discusses the relation between current and field strength in a conductor (Ohm's law), the electromotive force of a source and the two laws for circuits (Kirchhoff's laws). Finally it gives a classical microscopic picture of current and discusses the charging and discharging of a **capacitor**, the simplest nonsteady process.

The chapter uses many tools from earlier courses: the current is the **flux** of the current density, and the differential form of the **continuity equation** comes from the **divergence theorem** ([2.2.14](/2.2.14)) and has the same form as the **continuity equation** of fluid flow ([5.1.4](/5.1.4)) and the **conservation laws** of partial differential equations ([2.5.2](/2.5.2)); the differential form of Ohm's law parallels **Fourier's law** of heat conduction ([5.2.2](/5.2.2)); a complex circuit is a **system of linear equations**, whose number of independent equations is determined by the **fundamental cycles** of graph theory ([1.4.3](/1.4.3)); and the transient of an RC circuit is a first-order **linear differential equation** ([2.2.15](/2.2.15#sec-15.3)). The next chapter, [5.3.6](/5.3.6), studies the magnetic field produced by currents.

In this chapter $\rho$ denotes resistivity and $\sigma$ conductivity; to avoid confusion, the volume and surface densities of charge are written $\rho_q$ and $\sigma_q$. Section 5.6 (a classical microscopic picture of current) is optional.

## 5.1. Current and Current Density

Charges in organized motion form a current. The charged particles that make up a current are called charge carriers: free electrons in metals, positive and negative ions (and electrons) in electrolytes and ionized gases, and electrons and holes in semiconductors ([5.5.6](/5.5.6)).

**Definition 5.1.1 (Electric Current)** The charge passing through a cross section of a conductor per unit time,

$$
I = \frac{\mathrm{d}q}{\mathrm{d}t},
$$
is called the **electric current** through that section. The SI unit of current is the ampere ($\mathrm{A}$), one of the seven base units; since 2019 the ampere has been defined by fixing the numerical value of the **elementary charge**, $e = 1.602\,176\,634\times10^{-19}\,\mathrm{C}$ (exact) ([5.3.7](/5.3.7)).

Current describes only the total charge passing through a whole cross section, not how the current is distributed in a bulk conductor (for example in the ground in resistivity prospecting). For this we introduce a vector field:

### 5.1.1. Current Density

**Definition 5.1.2 (Current Density)** The **current density** $\boldsymbol{J}$ at a point of a conductor is a vector. Its magnitude is the charge passing per unit time through a unit area perpendicular to the direction of motion of the charges near that point, $J = \dfrac{\mathrm{d}I}{\mathrm{d}S_\perp}$; its direction is the direction of motion of positive carriers at that point (opposite to the motion of negative carriers). Its unit is $\mathrm{A\,m^{-2}}$.

Let the carriers have charge $q$ (an algebraic quantity), number density $n$ and drift velocity $\boldsymbol{v}$. The carriers passing through an area element $\Delta S$ perpendicular to $\boldsymbol{v}$ in time $\Delta t$ lie in a cylinder with base $\Delta S$ and length $v\Delta t$, so

$$
\boldsymbol{J} = nq\boldsymbol{v} = \rho_q\boldsymbol{v} .
$$
With several kinds of carriers, $\boldsymbol{J} = \sum_in_iq_i\boldsymbol{v}_i$.

**Definition 5.1.3 (Drift Velocity)** The free electrons in a metal move randomly with thermal motion and at the same time have, under an electric field, an average directed velocity $\boldsymbol{v}_{\mathrm{d}}$ (the average over the velocities of all free electrons), called the **drift velocity**, with $\boldsymbol{J} = -ne\boldsymbol{v}_{\mathrm{d}}$.

Without an external field $\boldsymbol{v}_{\mathrm{d}} = \boldsymbol{0}$ and there is no current. The drift velocity is very small: in copper $n \approx 8.5\times10^{28}\,\mathrm{m^{-3}}$, and for a current of $1\,\mathrm{A}$ in a copper wire of cross section $1\,\mathrm{mm^2}$, $v_{\mathrm{d}} = \dfrac{I}{neS} \approx 7\times10^{-5}\,\mathrm{m\,s^{-1}}$, less than $0.1\,\mathrm{mm}$ per second and far below the thermal speed of the electrons ($10^5$–$10^6\,\mathrm{m\,s^{-1}}$).

The current through any surface $S$ equals the **flux** of the current density through it:

$$
\mathrm{d}I = \boldsymbol{J}\cdot\mathrm{d}\boldsymbol{S},\qquad I = \int_S\boldsymbol{J}\cdot\mathrm{d}\boldsymbol{S} .
$$
Like **electric field lines**, current lines can be used to picture the distribution of current: the tangent of a current line at each point gives the direction of $\boldsymbol{J}$ there, and the number of current lines crossing a unit area perpendicular to $\boldsymbol{J}$ equals $J$.

### 5.1.2. The Current Continuity Equation

Charge can be neither created nor destroyed. For any closed surface $S$, the net charge flowing out of $S$ per unit time equals the decrease of the charge inside $S$:

**Theorem 5.1.1 (Charge Continuity Equation)**

$$
\oint_S\boldsymbol{J}\cdot\mathrm{d}\boldsymbol{S} = -\frac{\mathrm{d}q_{\mathrm{enc}}}{\mathrm{d}t},\qquad
\nabla\cdot\boldsymbol{J} + \frac{\partial\rho_q}{\partial t} = 0 .
$$

The differential form follows from the **divergence theorem**. The continuity equation is the mathematical statement of the **law of conservation of charge** and gives the general relation between the distribution of current and that of charge:

- $\oint_S\boldsymbol{J}\cdot\mathrm{d}\boldsymbol{S} > 0$: current lines emerge from inside the surface and the charge inside decreases;
- $\oint_S\boldsymbol{J}\cdot\mathrm{d}\boldsymbol{S} < 0$: current lines end inside the surface and the charge inside increases;
- $\oint_S\boldsymbol{J}\cdot\mathrm{d}\boldsymbol{S} = 0$: current lines pass through continuously and the charge inside is unchanged.

Current lines can begin and end only where the charge changes with time.

## 5.2. Steady Currents and Steady Electric Fields

**Definition 5.2.1 (Steady Current)** A current whose current density $\boldsymbol{J}$ does not change with time is called a **steady current**.

When $\boldsymbol{J}$ is constant in time, so is the charge distribution: whenever charge flows away from a place, an equal amount must flow in to replace it. Otherwise the accumulation of charge would change the electric field and hence the current. By the continuity equation, a steady current satisfies

**Theorem 5.2.1 (Steady-State Condition)**

$$
\oint_S\boldsymbol{J}\cdot\mathrm{d}\boldsymbol{S} = 0,\qquad \nabla\cdot\boldsymbol{J} = 0 .
$$
The current lines of a steady current are closed curves, and $\boldsymbol{J}$ is a **solenoidal vector field**. In an unbranched steady circuit the current is the same at every cross section.

**Definition 5.2.2 (Steady Electric Field)** The charge distribution of a steady current does not change with time, and the electric field it produces does not change with time either; it is called a **steady electric field**.

The steady electric field resembles the electrostatic field in that it is produced by a time-independent charge distribution, and therefore satisfies **Gauss's law** and the circulation theorem

$$
\oint_S\boldsymbol{E}\cdot\mathrm{d}\boldsymbol{S} = \frac{q_{\mathrm{enc}}}{\varepsilon_0},\qquad \oint_L\boldsymbol{E}\cdot\mathrm{d}\boldsymbol{l} = 0,
$$
and the concepts of **electric potential** and **potential difference** still apply; by custom the steady electric field is also called an electrostatic field. The differences are:

| | Electrostatic field | Steady electric field |
|---|---|---|
| Source | Stationary charges | Moving charges, with a time-independent distribution |
| Inside a conductor | Electrostatic equilibrium, field zero | Field nonzero, driving the current |
| Energy | Maintaining the field requires no energy conversion | The field does work on moving charges, always accompanied by energy conversion |

Applying the steady-state condition to a node of a circuit (a junction of three or more branches) gives:

**Theorem 5.2.2 (Kirchhoff's Current Law)** At any node of a steady circuit, the algebraic sum of the currents leaving the node is zero:

$$
\sum_iI_i = 0,
$$
with currents leaving the node counted as positive and those entering as negative. Equivalently, the sum of the currents entering a node equals the sum of the currents leaving it (the node equation).

## 5.3. Ohm's Law and Resistance

In 1826 Ohm discovered experimentally that the current through a conductor is proportional to the voltage across its ends.

### 5.3.1. Integral Form

**Theorem 5.3.1 (Ohm's Law)** The voltage $U = \varphi_a - \varphi_b$ across a conductor is proportional to the current $I$ through it:

$$
U = IR,
$$
and the potential drops by $IR$ in passing through a resistor along the direction of the current.

**Definition 5.3.1 (Resistance and Conductance)** The proportionality coefficient $R = U/I$ in Ohm's law is called the **resistance** of the conductor, with unit the ohm ($\Omega = \mathrm{V\,A^{-1}}$); its reciprocal $G = 1/R$ is called the **conductance**, with unit the siemens ($\mathrm{S} = \Omega^{-1}$).

**Definition 5.3.2 (Resistivity and Conductivity)** The resistance of a uniform conductor of length $L$ and cross-sectional area $S$ is

$$
R = \rho\frac{L}{S},
$$
where $\rho$ is called the **resistivity** of the material, with unit $\Omega\,\mathrm{m}$; its reciprocal $\sigma = 1/\rho$ is called the **conductivity**, with unit $\mathrm{S\,m^{-1}}$.

| Material ($20^\circ\mathrm{C}$) | $\rho/(\Omega\,\mathrm{m})$ | Material | $\rho/(\Omega\,\mathrm{m})$ |
|---|---|---|---|
| Silver | $1.6\times10^{-8}$ | Nichrome | $1.1\times10^{-6}$ |
| Copper | $1.7\times10^{-8}$ | Seawater | about $0.2$ |
| Aluminum | $2.7\times10^{-8}$ | Pure silicon | about $2\times10^3$ |
| Iron | $9.7\times10^{-8}$ | Glass | $10^{10}$–$10^{14}$ |

The resistivities of conductors, semiconductors and insulators differ by more than twenty orders of magnitude, which requires band theory to explain ([5.5.6](/5.5.6)). Near room temperature the resistivity of a metal increases approximately linearly with temperature, $\rho \approx \rho_0(1 + \alpha t)$, with $\alpha \approx 4\times10^{-3}\,\mathrm{K^{-1}}$ for copper; the resistivity of a semiconductor decreases rapidly as the temperature rises.

### 5.3.2. Differential Form

In a bulk conductor take a small cylinder along a current line, of length $\mathrm{d}l$ and cross section $\mathrm{d}S$, with potential difference $\mathrm{d}U = -\mathrm{d}\varphi$ between its ends and resistance $\mathrm{d}R = \rho\,\mathrm{d}l/\mathrm{d}S$. From $\mathrm{d}U = \mathrm{d}I\,\mathrm{d}R$,

$$
J = \frac{\mathrm{d}I}{\mathrm{d}S} = \frac1\rho\Big(-\frac{\mathrm{d}\varphi}{\mathrm{d}l}\Big) = \sigma E .
$$
In an isotropic conductor $\boldsymbol{J}$ and $\boldsymbol{E}$ are parallel, and we obtain:

**Theorem 5.3.2 (Differential Form of Ohm's Law)**

$$
\boldsymbol{J} = \sigma\boldsymbol{E} .
$$

The differential form is a local relation and applies more widely than the integral form: it holds for nonuniform conductors and also for nonsteady currents that do not vary too fast. It has exactly the same form as **Fourier's law** of heat conduction $\boldsymbol{q} = -\kappa\nabla T$ and **Fick's law** of diffusion: current flows in the direction of decreasing potential, and heat flows in the direction of decreasing temperature.

Ohm's law is not a universal law. The current–voltage characteristics of ionized gases and of semiconductor devices (such as diodes) are nonlinear; in very strong fields, even in metals, $\boldsymbol{J}$ departs from linearity in $\boldsymbol{E}$. An "ideal conductor" means the limit $\sigma \to \infty$ and differs from a superconductor: besides zero resistance, a superconductor has perfect diamagnetism ([5.3.9](/5.3.9)).

### 5.3.3. Computing Resistance

When the cross section or the direction of the current in a conductor is not uniform, divide the conductor into thin layers in series along the current, $R = \int\rho\,\dfrac{\mathrm{d}l}{S(l)}$.

**Example 5.3.1 (Leakage Resistance of a Cable)** A coaxial cable has a core of radius $R_1$, an outer conductor of inner radius $R_2$ and length $l$, with an insulating layer of resistivity $\rho$ between them. Find the radial leakage resistance, and the leakage current if the voltage between core and outer conductor is $U$.

**Solution** The current flows radially. For a thin cylindrical layer from radius $r$ to $r + \mathrm{d}r$, of length $\mathrm{d}r$ and cross-sectional area $2\pi rl$,

$$
R = \int_{R_1}^{R_2}\rho\frac{\mathrm{d}r}{2\pi rl} = \frac{\rho}{2\pi l}\ln\frac{R_2}{R_1},\qquad
I = \frac UR = \frac{2\pi lU}{\rho\ln(R_2/R_1)} .
$$
The longer the cable, the smaller the leakage resistance.

## 5.4. Electromotive Force

### 5.4.1. Non-Electrostatic Force and Sources

A circuit carrying a steady current must be closed. If the circuit is not closed, charge accumulates at the break and destroys the steady-state condition. But the electrostatic field alone cannot maintain a steady current in a closed loop: the electrostatic field is a **conservative vector field**, $\oint\boldsymbol{E}\cdot\mathrm{d}\boldsymbol{l} = 0$, so the total work done by the electrostatic field on a positive charge going once around the loop is zero, whereas the current continually converts energy into heat in the resistors. Hence there must be a segment of the loop in which the carriers experience a force opposite to the electrostatic force and are pushed back from low to high potential.

**Definition 5.4.1 (Non-Electrostatic Force and Source)** A force that can move a positive charge from low to high potential against the electrostatic field is called a **non-electrostatic force** $\boldsymbol{F}_{\mathrm{ne}}$; a device that supplies a non-electrostatic force is called a **source of electromotive force** (source for short).

Non-electrostatic forces have many origins: chemical action in a battery, electromagnetic induction in a generator ([5.3.9](/5.3.9)), thermal diffusion in a thermocouple, and the interaction of light with a semiconductor in a photovoltaic cell. A source does not create charge; it is only a "carrier" of charge, converting other forms of energy into electrical energy.

### 5.4.2. Electromotive Force

Following the **electric field strength**, define the non-electrostatic field strength $\boldsymbol{E}_{\mathrm{ne}} = \boldsymbol{F}_{\mathrm{ne}}/q$.

**Definition 5.4.2 (Electromotive Force)** The work done by the non-electrostatic force in moving a unit positive charge inside the source from the negative to the positive terminal,

$$
\mathcal{E} = \int_{-}^{+}\boldsymbol{E}_{\mathrm{ne}}\cdot\mathrm{d}\boldsymbol{l} = \frac{A_{\mathrm{ne}}}{q}
$$
(the integral taken through the interior of the source), is called the **electromotive force** (emf) of the source, with unit the volt. The direction of the emf is the direction inside the source from the negative to the positive terminal. If $\boldsymbol{E}_{\mathrm{ne}}$ is distributed over the whole loop $L$ (as in induced emf, [5.3.9](/5.3.9)), the emf of the loop is

$$
\mathcal{E} = \oint_L\boldsymbol{E}_{\mathrm{ne}}\cdot\mathrm{d}\boldsymbol{l} .
$$

Voltage and emf must be distinguished. Voltage is determined by the electrostatic field, and $U_{12} = \int_1^2\boldsymbol{E}\cdot\mathrm{d}\boldsymbol{l}$ is path independent; the emf from point 1 to point 2 along the loop $L$, $\mathcal{E}_{12} = \int_{1(L)}^{2}\boldsymbol{E}_{\mathrm{ne}}\cdot\mathrm{d}\boldsymbol{l}$, depends on the path. The emf is the "potential rise" caused by the non-electrostatic force and reflects the ability of the source to convert other forms of energy into electrical energy.

### 5.4.3. Thermoelectric Phenomena

**Definition 5.4.3 (Seebeck Effect)** When two different metals (such as copper and iron) are joined into a closed loop and the two junctions are at different temperatures, an emf and a current appear in the loop. This phenomenon is called the **Seebeck effect** (discovered in 1821), and such an emf is called a thermoelectric emf.

The thermoelectric emf has two sources. Within one metal, the temperature **gradient** makes free electrons diffuse from the hot end to the cold end, producing the Thomson emf; at a junction of two metals, the different free-electron concentrations lead to mutual diffusion and a temperature-dependent contact emf, the Peltier emf.

Put one junction of the two metals at the temperature $T_1$ to be measured and the other at a known constant temperature $T_2$; measuring the thermoelectric emf of the loop (typically a few millivolts per $100^\circ\mathrm{C}$) determines $T_1$. This is the thermocouple. It has small heat capacity and high sensitivity (down to $10^{-3}\,^\circ\mathrm{C}$), can measure temperature changes point by point over very small regions, covers a wide range (about $-200^\circ\mathrm{C}$ to $2000^\circ\mathrm{C}$), and is convenient for automatic control. A scanning thermal microscope forms a thermocouple of tungsten and nickel at the probe tip; as the distance between probe and surface varies, the heat dissipated from the tip, and hence its temperature, varies, and an image of the surface topography is obtained.

## 5.5. Circuits with Electromotive Force

### 5.5.1. Features of Steady Circuits

**Property 5.5.1** There is no net charge inside a uniform conductor carrying a steady current; net charge is distributed only on the surface of the conductor and where it is nonuniform (electrodes, wire surfaces, interfaces between different conductors, bends, and so on).

**Proof** For a uniform conductor $\sigma$ is constant. By the steady-state condition and Ohm's law, $\nabla\cdot\boldsymbol{J} = \sigma\nabla\cdot\boldsymbol{E} = 0$, and then from the differential form of **Gauss's law**, $\rho_q = \varepsilon_0\nabla\cdot\boldsymbol{E} = 0$. $\square$

Inside the wires of the external circuit, current lines and field lines point in the same direction and are necessarily parallel to the wire surface: otherwise the current would flow onto the surface, where surface charge would pile up and destroy the steady state. When a wire bends, it is the charge distribution on the wire surface that produces the field that makes the carriers "turn the corner".

Inside a source the carriers are acted on by both the electrostatic force and the non-electrostatic force, and Ohm's law generalizes to

$$
\boldsymbol{J} = \sigma(\boldsymbol{E} + \boldsymbol{E}_{\mathrm{ne}}) .
$$

### 5.5.2. Ohm's Law for a Complete Circuit

Integrate $\boldsymbol{J}/\sigma = \boldsymbol{E} + \boldsymbol{E}_{\mathrm{ne}}$ through the source from the negative to the positive terminal. Let the internal resistance of the source be $r$, and take the positive direction of the current $I$ to be from the negative to the positive terminal inside the source:

$$
\int_-^+\frac{\boldsymbol{J}}{\sigma}\cdot\mathrm{d}\boldsymbol{l} = Ir,\qquad
\int_-^+\boldsymbol{E}\cdot\mathrm{d}\boldsymbol{l} = \varphi_- - \varphi_+ = -U,\qquad
\int_-^+\boldsymbol{E}_{\mathrm{ne}}\cdot\mathrm{d}\boldsymbol{l} = \mathcal{E},
$$
where $U = \varphi_+ - \varphi_-$ is the terminal voltage of the source. Thus $Ir = -U + \mathcal{E}$, that is, $U = \mathcal{E} - Ir$. With external resistance $R$, $U = IR$, and we obtain:

**Theorem 5.5.1 (Ohm's Law for a Complete Circuit)**

$$
I = \frac{\mathcal{E}}{R + r} .
$$

### 5.5.3. Kirchhoff's Voltage Law

A complex circuit consists of many branches, each of which may contain resistors and sources.

**Theorem 5.5.2 (Ohm's Law for a Section of a Circuit with Sources)** On a section of circuit from $a$ to $b$ containing sources, let the $i$-th element carry current $I_i$ and have resistance $R_i$, source emf $\mathcal{E}_i$ and internal resistance $r_i$, with $I_i$ and $\mathcal{E}_i$ counted as positive when directed from $a$ to $b$. Then

$$
U_{ab} = \varphi_a - \varphi_b = \sum_i\big[I_i(R_i + r_i) - \mathcal{E}_i\big] .
$$

The potential drops by $IR$ in passing through a resistor along the current, and rises by $\mathcal{E}$ in passing through a source along the direction of its emf. Setting $b = a$ gives:

**Theorem 5.5.3 (Kirchhoff's Voltage Law)** Going once around any closed loop of a complex circuit,

$$
\sum_i\mathcal{E}_i = \sum_iI_i(R_i + r_i),
$$
where $I_i$ and $\mathcal{E}_i$ are counted as positive when they agree with the direction of traversal and negative when opposite (the loop equation).

The first law comes from conservation of charge (the steady-state condition), and the second from the **circulation theorem for the electrostatic field** (conservation of energy). For a connected circuit with $n$ nodes and $b$ branches there are $n - 1$ independent node equations and $b - n + 1$ independent loop equations, which correspond exactly to the **fundamental cycles** determined by the $b - n + 1$ edges outside a **spanning tree** of the circuit graph ([1.4.3](/1.4.3)). Together they form a **system of linear equations** in the $b$ branch currents, with a unique solution. When Kirchhoff studied the solutions of such equations in 1847, he expressed the branch currents in terms of spanning trees of the circuit graph, and thereby obtained the **matrix-tree theorem** of graph theory.

**Example 5.5.1 (Infinite Ladder Network)** An infinite ladder network is made of identical resistors $R$: each stage is a series resistor (on the top rail) and a shunt resistor (a rung). An ideal source of emf $\mathcal{E}$ is connected at the input. Find: (1) the equivalent resistance $R_x$ of the network; (2) the currents in the $n$-th series resistor and the $n$-th rung.

**Solution** (1) After removing the first stage, the remaining network is again the same infinite network, with equivalent resistance still $R_x$. So the first rung is in parallel with $R_x$, and the combination is in series with the first series resistor:

$$
R_x = R + \frac{RR_x}{R + R_x}\quad\Longrightarrow\quad R_x^2 - RR_x - R^2 = 0,\qquad R_x = \frac{1 + \sqrt5}{2}R .
$$
(2) Let $I_i$ be the current in the $i$-th series resistor; it divides between the $i$-th rung and the rest of the network $R_x$ in inverse proportion to the resistances:

$$
I_{i+1} = \frac{R}{R + R_x}I_i,\qquad I_i' = \frac{R_x}{R + R_x}I_i .
$$
Let $\phi = \frac{1 + \sqrt5}{2}$ (the golden ratio, $\phi^2 = \phi + 1$). Then $\frac{R}{R + R_x} = \frac{1}{1 + \phi} = \phi^{-2}$, $\frac{R_x}{R + R_x} = \phi^{-1}$ and $I_1 = \frac{\mathcal{E}}{R_x} = \frac{\mathcal{E}}{\phi R}$, so

$$
I_n = \phi^{-(2n-1)}\frac{\mathcal{E}}{R},\qquad I_n' = \phi^{-2n}\frac{\mathcal{E}}{R} .
$$
The current decays geometrically along the network, by a factor $\phi^{-2} \approx 0.38$ per stage.

**Example 5.5.2 (Infinite Square Grid)** An infinite square grid has resistance $r$ in every edge. Find the equivalent resistance between two adjacent nodes $A$ and $B$.

**Solution** Use the **superposition principle**. First let a current $I$ enter at $A$ and leave at infinity: by symmetry each of the four edges from $A$ carries $I/4$, so the current in edge $AB$ is $I/4$ (from $A$ to $B$). Next let a current $I$ enter from infinity and leave at $B$: the current in edge $AB$ is again $I/4$ (from $A$ to $B$). Their superposition is a current $I$ entering at $A$ and leaving at $B$ with no net current at infinity; the current in edge $AB$ is then $I/2$ and $U_{AB} = \frac I2r$, so

$$
R_{AB} = \frac r2 .
$$
Superposition works here because the circuit equations are linear.

**Example 5.5.3 (Solving a Circuit with Kirchhoff's Laws)** Three branches are connected in parallel between two nodes $a$ (top) and $b$ (bottom). The left branch is a source $\mathcal{E}_1 = 10\,\mathrm{V}$ (internal resistance $r_1 = 1\,\Omega$) in series with a resistor $R_1 = 1\,\Omega$; the middle branch is a source $\mathcal{E}_3 = 12\,\mathrm{V}$ ($r_3 = 1\,\Omega$) with $R_3 = 3\,\Omega$; the right branch is a source $\mathcal{E}_2 = 16\,\mathrm{V}$ ($r_2 = 1\,\Omega$) with $R_2 = 1\,\Omega$. The positive terminals of all three sources face $a$. Find the currents in the three branches.

**Solution** Take the currents $I_1$, $I_2$, $I_3$ in the three branches as positive when flowing from $b$ to $a$. By Ohm's law for a section of circuit with sources,

$$
\varphi_a - \varphi_b = \mathcal{E}_1 - I_1(R_1 + r_1) = \mathcal{E}_2 - I_2(R_2 + r_2) = \mathcal{E}_3 - I_3(R_3 + r_3),
$$
and the current equation at node $a$ is $I_1 + I_2 + I_3 = 0$. Writing $U = \varphi_a - \varphi_b$ and substituting the numbers,

$$
\frac{10 - U}{2} + \frac{16 - U}{2} + \frac{12 - U}{4} = 0\quad\Longrightarrow\quad U = 12.8\,\mathrm{V},
$$
so $I_1 = -1.4\,\mathrm{A}$, $I_2 = 1.6\,\mathrm{A}$, $I_3 = -0.2\,\mathrm{A}$: current flows from the right branch to $a$ and returns to $b$ through the left and middle branches; the $16\,\mathrm{V}$ source is "charging" the other two.

This method with the node potentials as unknowns is called the node-potential method. Larger networks are written directly in matrix form and solved by numerical linear algebra ([4.4.3](/4.4.3)):

```python
import numpy as np

# unknowns: I1, I2, I3 (from b to a in each branch) and U = phi_a - phi_b
A = np.array([
    [1.0, 1.0, 1.0, 0.0],   # node a: I1 + I2 + I3 = 0
    [2.0, 0.0, 0.0, 1.0],   # E1 = I1 (R1 + r1) + U
    [0.0, 2.0, 0.0, 1.0],   # E2 = I2 (R2 + r2) + U
    [0.0, 0.0, 4.0, 1.0],   # E3 = I3 (R3 + r3) + U
])
b = np.array([0.0, 10.0, 16.0, 12.0])
print(np.linalg.solve(A, b))  # [-1.4  1.6 -0.2 12.8]
```

### 5.5.4. Joint Solution of the Steady Current Field and the Electric Field

When a steady current flows in a conducting **dielectric**, there is always an accompanying electric field. The basic equations determining the current and field distributions are

$$
\oint_S\boldsymbol{J}\cdot\mathrm{d}\boldsymbol{S} = 0,\qquad \oint_L\boldsymbol{E}\cdot\mathrm{d}\boldsymbol{l} = 0,\qquad \boldsymbol{J} = \sigma\boldsymbol{E} .
$$
The three equations are closed and completely determine the steady current field and electric field in the conducting medium. Taking small flat cylinders and small rectangular loops as in [5.3.4](/5.3.4), the first two give the interface conditions at the boundary of two conducting media:

**Theorem 5.5.4 (Interface Conditions for the Steady Current Field)**

$$
J_{1\mathrm{n}} = J_{2\mathrm{n}},\qquad E_{1\mathrm{t}} = E_{2\mathrm{t}} .
$$

It follows that:

- The steady current field and electric field in a conducting medium are determined entirely by the conductivity $\sigma$ and are independent of the polarization properties of the medium (its **permittivity** $\varepsilon$).
- Gauss's law for $\boldsymbol{E}$ gives the distribution of the total charge (free plus **bound charge**), which also depends only on $\sigma$.
- From $\boldsymbol{D} = \varepsilon\boldsymbol{E}$ and Gauss's law for $\boldsymbol{D}$ we obtain the distribution of free charge; how the total divides between free and bound charge depends on $\varepsilon$.

**Example 5.5.4 (Two Layers of Conducting Medium)** A parallel-plate capacitor is filled with two layers of conducting medium whose thickness, permittivity and conductivity are $(d_1, \varepsilon_1, \sigma_1)$ and $(d_2, \varepsilon_2, \sigma_2)$. Medium 1 is in contact with the plate at higher potential, and the voltage between the plates is $U$. Find: (1) the current density and field strength in the two layers; (2) the total surface charge density $\sigma_q$ and the free surface charge density $\sigma_{q,0}$ on the interface between the layers.

**Solution** (1) By symmetry the current and field are perpendicular to the plates, and the interface condition gives $J_1 = J_2 = J$. Then $E_1 = J/\sigma_1$, $E_2 = J/\sigma_2$, and with $U = E_1d_1 + E_2d_2$,

$$
J = \frac{\sigma_1\sigma_2}{\sigma_1d_2 + \sigma_2d_1}U,\qquad
E_1 = \frac{\sigma_2U}{\sigma_1d_2 + \sigma_2d_1},\qquad
E_2 = \frac{\sigma_1U}{\sigma_1d_2 + \sigma_2d_1} .
$$
For $\sigma_1 \ne \sigma_2$ the field is discontinuous at the interface, and charge accumulates there.

(2) Take a small flat cylinder on the interface with its normal pointing from medium 1 to medium 2 (along the current), and apply Gauss's law for $\boldsymbol{E}$ and for $\boldsymbol{D}$:

$$
\sigma_q = \varepsilon_0(E_2 - E_1) = \frac{\varepsilon_0(\sigma_1 - \sigma_2)U}{\sigma_1d_2 + \sigma_2d_1},\qquad
\sigma_{q,0} = \varepsilon_2E_2 - \varepsilon_1E_1 = \frac{(\varepsilon_2\sigma_1 - \varepsilon_1\sigma_2)U}{\sigma_1d_2 + \sigma_2d_1} .
$$
Even if $\sigma_1 = \sigma_2$ (zero total charge), as long as $\varepsilon_1 \ne \varepsilon_2$ there is still free charge on the interface, exactly canceled by bound charge.

**Example 5.5.5 (Spherical Grounding Electrode)** A metal sphere of radius $a$ is buried as a grounding electrode at depth $h \gg a$ in soil of conductivity $\sigma$. Find the grounding resistance.

**Solution** Let the ground current be $I$. For $h \gg a$ the effect of the ground surface can be neglected and the current flows out uniformly in the radial direction,

$$
\boldsymbol{J} = \frac{I}{4\pi r^2}\boldsymbol{e}_r,\qquad \boldsymbol{E} = \frac{\boldsymbol{J}}{\sigma} = \frac{I}{4\pi\sigma r^2}\boldsymbol{e}_r .
$$
The voltage of the electrode relative to infinity and the grounding resistance are

$$
U = \varphi_a - \varphi_\infty = \int_a^\infty\frac{I\,\mathrm{d}r}{4\pi\sigma r^2} = \frac{I}{4\pi\sigma a},\qquad R = \frac UI = \frac{1}{4\pi\sigma a} \propto \frac{1}{\sigma a} .
$$
The conductivity of the earth is about $10^{-3}$–$10^{-1}\,\mathrm{S\,m^{-1}}$; with $\sigma = 10^{-2}\,\mathrm{S\,m^{-1}}$ and $a = 0.5\,\mathrm{m}$ we get $R \approx 16\,\Omega$. Actual grounding resistances are generally of the order of $1$–$10\,\Omega$ (power systems usually require no more than $4\,\Omega$ or $10\,\Omega$), so methods such as connecting several electrodes in parallel and using resistance-reducing agents are employed to reduce it.

How can the grounding resistance be reduced? The potential at distance $r$ from the center is

$$
\varphi(r) = \int_r^\infty\frac{I\,\mathrm{d}r'}{4\pi\sigma r'^2} = \frac{I}{4\pi\sigma r} = U\frac ar,
$$
and at $r = 10a$, $\varphi = 0.1U$: $90\%$ of the potential drop occurs within $r < 10a$. Improving the conductivity of the soil near the electrode is therefore the key to reducing the whole grounding resistance. Because the potential also changes sharply near the grounding point, when a large current enters the ground (a lightning strike, a fallen high-voltage line), a person nearby can experience a dangerous "step voltage" between the two feet.

![Potential around a spherical grounding electrode, φ(r) = φ_a a/r: 90% of the potential drop occurs within r < 10a](./plots/grounding-electrode.py)

## 5.6. A Classical Microscopic Picture of Current

The differential form of Ohm's law says that the current density (determined by the electron velocity) is proportional to the field strength (which determines the electron acceleration). Why does the velocity not grow ever larger? The *Drude model*, proposed by Drude in 1900, gives a classical explanation: electrons accelerate in the field but keep "colliding" with the ions of the lattice, and after each collision the direction of the velocity becomes completely random, so the directed velocity imparted by the field is lost.

Let there be $n$ free electrons per unit volume. The velocity of the $i$-th electron after a time $t_i$ since its last collision is

$$
\boldsymbol{v}_i = \boldsymbol{v}_{0i} - \frac{e}{m_{\mathrm{e}}}\boldsymbol{E}t_i ,
$$
where $\boldsymbol{v}_{0i}$ is its velocity just after that collision. The current density is the sum over all electrons:

$$
\boldsymbol{J} = -e\sum_{i=1}^n\boldsymbol{v}_i = -e\sum_{i=1}^n\boldsymbol{v}_{0i} + \frac{e^2}{m_{\mathrm{e}}}\boldsymbol{E}\sum_{i=1}^nt_i .
$$
The directions of the velocities after collisions are random, so the first term vanishes; in the second, $\frac1n\sum t_i = \tau$ is the average time elapsed since the last collision. If collisions occur at random, the free-flight time follows an **exponential distribution**, and by its **memorylessness** this average equals the mean free-flight time between collisions, that is, the **relaxation time**. Then $\boldsymbol{J} = \dfrac{ne^2\tau}{m_{\mathrm{e}}}\boldsymbol{E}$, giving:

**Formula 5.6.1 (Drude Conductivity)**

$$
\sigma = \frac{ne^2\tau}{m_{\mathrm{e}}} .
$$

For copper, $\sigma \approx 6.0\times10^7\,\mathrm{S\,m^{-1}}$ and $n \approx 8.5\times10^{28}\,\mathrm{m^{-3}}$ give $\tau \approx 2.5\times10^{-14}\,\mathrm{s}$. The electron speed multiplied by $\tau$ is the **mean free path** ([5.2.2](/5.2.2#sec-2.3)).

The collision rates of different scattering mechanisms add; this is called *Matthiessen's rule*: $\dfrac1\tau = \dfrac1{\tau_{\mathrm{imp}}} + \dfrac1{\tau_{\mathrm{ph}}} + \dfrac1{\tau_{\mathrm{ee}}}$, arising from scattering by impurities and defects, by lattice vibrations (phonons) and among electrons, respectively, so that $\rho = \rho_{\mathrm{imp}} + \rho_{\mathrm{ph}}(T) + \cdots$. Lattice vibrations strengthen with temperature, so the resistance of a metal increases as the temperature rises; at low temperature only the temperature-independent impurity scattering remains, and the resistivity tends to a constant (the residual resistivity).

**Remark** The classical model agrees approximately with experiment over a certain range but has fundamental difficulties: if the **mean free path** is computed with the classical thermal speed $\propto\sqrt T$, the resistivity comes out $\propto\sqrt T$, whereas experiment gives $\propto T$; and the mean free path obtained is much larger than the ion spacing, contradicting the picture of electrons colliding with ions. The correct explanation requires quantum theory: the conduction electrons move at the Fermi speed, the periodic lattice itself does not scatter electrons, and scattering comes from lattice vibrations and impurities ([5.5.6](/5.5.6)).

### 5.6.1. Joule's Law

In collisions, the work done by the field on the electrons is converted into the thermal motion energy of the lattice, that is, **internal energy**. In the model above, the directed velocity gained by an electron between two collisions is $\frac{eE}{m_{\mathrm{e}}}t$, and the corresponding kinetic energy $\frac{e^2E^2}{2m_{\mathrm{e}}}t^2$ is handed to the lattice at the next collision. The free-flight time $t$ follows an exponential distribution with parameter $1/\tau$, so $\langle t^2\rangle = 2\tau^2$, and each electron makes $1/\tau$ collisions per unit time. The internal energy converted per unit time and per unit volume is therefore

$$
p = n\cdot\frac1\tau\cdot\frac{e^2E^2}{2m_{\mathrm{e}}}\cdot2\tau^2 = \frac{ne^2\tau}{m_{\mathrm{e}}}E^2 = \sigma E^2 .
$$

**Theorem 5.6.1 (Joule's Law)** The thermal power per unit volume in a conductor is

$$
p = \boldsymbol{J}\cdot\boldsymbol{E} = \sigma E^2,
$$
and for a conductor of length $l$ and cross section $S$ carrying current $I$, the heating **power** is $P = plS = \dfrac{(JS)^2}{\sigma S}l = I^2R$.

The expression $p = \boldsymbol{J}\cdot\boldsymbol{E}$ is the general expression for the work done by the field on the current, independent of the microscopic model; the integral form is $P = UI = I^2R = U^2/R$.

## 5.7. Charging and Discharging of a Capacitor

A resistor $R$ and a **capacitance** $C$ are connected in series and joined through a switch to a source of emf $\mathcal{E}$ (the internal resistance is absorbed into $R$). With the switch connected to the source the capacitor charges; with the switch connecting $R$ and $C$ directly into a loop the capacitor discharges.

Let the charge on the capacitor plates be $q$ and the current in the loop $i = \mathrm{d}q/\mathrm{d}t$. By Kirchhoff's voltage law, during charging

$$
R\frac{\mathrm{d}q}{\mathrm{d}t} + \frac qC = \mathcal{E},
$$
and the right-hand side is zero during discharging. This is a first-order **linear differential equation** with constant coefficients ([2.2.15](/2.2.15#sec-15.3), [2.4.3](/2.4.3#sec-3.2)). Setting $q' = q - C\mathcal{E}$ turns the charging equation into the homogeneous equation $\dfrac{\mathrm{d}q'}{\mathrm{d}t} = -\dfrac{q'}{RC}$, whose solution decays exponentially.

**Definition 5.7.1 (Time Constant)** The quantity $\tau = RC$ has the dimension of time and is called the **time constant** of the RC circuit.

**Formula 5.7.1 (Charging and Discharging of an RC Circuit)** For charging ($q|_{t=0} = 0$) and discharging ($q|_{t=0} = Q_0$),

$$
q = C\mathcal{E}\big(1 - \mathrm{e}^{-t/\tau}\big),\quad i = \frac{\mathcal{E}}{R}\mathrm{e}^{-t/\tau};\qquad\qquad
q = Q_0\mathrm{e}^{-t/\tau},\quad i = -\frac{Q_0}{RC}\mathrm{e}^{-t/\tau} .
$$

After one time constant, charging reaches $1 - \mathrm{e}^{-1} \approx 63\%$ of its final value and discharging leaves $\mathrm{e}^{-1} \approx 37\%$ of the initial value; after $5\tau$ the process is essentially over (within $1\%$). The voltage across the capacitor $u_C = q/C$ is continuous and cannot jump, whereas the current can.

![Capacitor voltage and current versus time during charging and discharging of an RC circuit; the open circles are the result of numerical integration of the differential equation](./plots/rc-charge-discharge.py)

Energy during charging: the source does work $\int_0^\infty\mathcal{E}i\,\mathrm{d}t = C\mathcal{E}^2$, the capacitor stores $\frac12C\mathcal{E}^2$ (Formula 4.5.1 in [5.3.4](/5.3.4)), and the resistor dissipates $\int_0^\infty i^2R\,\mathrm{d}t = \frac12C\mathcal{E}^2$ as heat. However large or small $R$ may be, half of the work done by the source always becomes heat.

**Remark** Charging and discharging are nonsteady (transient) processes, and the electric field in them is a nonsteady field. As long as the size $l$ of the circuit is much smaller than the distance traveled by the electromagnetic field during the characteristic time of the process, $l \ll c\tau$ (for alternating current, $l \ll c/\nu$, that is, much smaller than the wavelength of the electromagnetic wave), the current is approximately equal everywhere at any instant. Such a field is called a quasi-steady field, and Kirchhoff's laws still apply; this is called the quasi-steady condition. For example, the wavelength of $50\,\mathrm{Hz}$ alternating current is $6000\,\mathrm{km}$, and ordinary circuits satisfy the quasi-steady condition.

## Summary

| Law | Integral form | Differential form |
|---|---|---|
| Current | $I = \int_S\boldsymbol{J}\cdot\mathrm{d}\boldsymbol{S}$ | $\boldsymbol{J} = nq\boldsymbol{v}$ |
| Continuity equation | $\oint_S\boldsymbol{J}\cdot\mathrm{d}\boldsymbol{S} = -\dfrac{\mathrm{d}q_{\mathrm{enc}}}{\mathrm{d}t}$ | $\nabla\cdot\boldsymbol{J} + \partial_t\rho_q = 0$ |
| Steady-state condition, Kirchhoff's current law | $\oint_S\boldsymbol{J}\cdot\mathrm{d}\boldsymbol{S} = 0$, $\sum I_i = 0$ | $\nabla\cdot\boldsymbol{J} = 0$ |
| Ohm's law | $U = IR$, $R = \rho L/S$ | $\boldsymbol{J} = \sigma\boldsymbol{E}$; inside a source $\boldsymbol{J} = \sigma(\boldsymbol{E} + \boldsymbol{E}_{\mathrm{ne}})$ |
| Emf, Kirchhoff's voltage law | $\mathcal{E} = \int_-^+\boldsymbol{E}_{\mathrm{ne}}\cdot\mathrm{d}\boldsymbol{l}$, $\sum\mathcal{E}_i = \sum I_i(R_i + r_i)$ | |
| Joule's law | $P = I^2R$ | $p = \boldsymbol{J}\cdot\boldsymbol{E} = \sigma E^2$ |
| Drude model | | $\sigma = ne^2\tau/m_{\mathrm{e}}$ |
| RC circuit | $\tau = RC$, $q = C\mathcal{E}(1 - \mathrm{e}^{-t/\tau})$ | |

## Questions

1. What force drives the carriers along a wire? When a wire bends, how do the carriers "turn the corner"?
   Hint: the driving force is the electric field, produced jointly by the two terminals of the source and by the charges on the wire surface. The instant the circuit is closed, charge accumulates on the wire surface (especially at bends) until the field inside the wire points along the wire everywhere; the field of these surface charges makes the carriers turn, while the hand bending the wire acts only as a "constraint".
2. The drift velocity of electrons in a conductor is only $0.01$–$0.1\,\mathrm{mm\,s^{-1}}$. Why does the bulb light immediately when the switch is pressed, even with a very long wire?
   Hint: what is needed to establish the current is the field in the wire, which is established along the wire at nearly the speed of light (through the redistribution of surface charge), so electrons everywhere begin to drift almost simultaneously; the electrons do not need to travel from the switch to the bulb.
3. By Ohm's law, electrons in a wire must move against the field lines, whereas electrons in vacuum need not. Why?
   Hint: electrons in a wire collide constantly and have no "memory", so the average velocity is determined by the local, instantaneous field ($\boldsymbol{v}_{\mathrm{d}} \propto -\boldsymbol{E}$); electrons in vacuum do not collide, the field determines their acceleration, and the velocity also depends on the initial velocity and past forces, just as the velocity of a projectile need not point along gravity.
4. The steady electric field also satisfies the circulation theorem, so the work done by the steady field on an electron going once around the circuit is zero. How is electrical energy converted into other forms?
   Hint: in the external circuit the steady field does positive work on the electrons, which hand the energy to the lattice through collisions (Joule heat); inside the source the electrons move against the electrostatic force, the electrostatic field does negative work, and this energy is supplied by the non-electrostatic force. The steady field only serves to transmit energy; the source of the energy is the non-electrostatic force in the source.
