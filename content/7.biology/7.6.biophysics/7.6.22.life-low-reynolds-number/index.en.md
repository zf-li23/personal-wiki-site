---
title: Life at Low Reynolds Number
description: "The mechanics of water for cells: continuum description, viscosity and the Navier–Stokes equations, Poiseuille flow and leukocyte rolling, the Reynolds number, Stokes flow and Stokes' law, drag on slender bodies, the scallop theorem and Purcell's swimmer, resistive-force theory of helical flagella and beating cilia, the torque–speed curve of the bacterial flagellar motor, sedimentation and buoyancy, and viscoelastic media."
---

Every cell lives in water, and every movement of a cell or of anything inside it is a movement through water. Our intuition about water comes from swimming and stirring, where pushing off and gliding work because the water and the swimmer carry momentum. For a bacterium this intuition is wrong by ten orders of magnitude: when its motor stops it comes to rest within a fraction of a nanometer, a stroke that is undone in reverse achieves nothing, and the only way forward is a shape change that is not symmetric in time. This chapter develops the mechanics of water from Newton's law for a fluid element, identifies the dimensionless number that separates our world from the cell's, and works out what follows: Stokes' law for drag, the scallop theorem, the propulsion of helical flagella and beating cilia, the operating point of the bacterial flagellar motor, sedimentation, and the viscoelastic media in which many cells actually swim.

The chapter builds on several earlier ones. The **frictional coefficient** and Stokes' law were used in [7.6.8](/7.6.8#sec-8.7) to read molecular size and shape from hydrodynamic measurements, and the overdamped Langevin equation of [7.6.5](/7.6.5#sec-5.4) assumes the inertia-free world derived here. The structure of cilia and the bacterial flagellum is in [7.3.14](/7.3.14#sec-14.6); here only their physics is treated. Embryonic tissues flow at even smaller Reynolds number, and the **Stokes flow** of tissues with surface tension is the subject of [7.5.8](/7.5.8#sec-8.5). The rotary mechanism of the flagellar motor is in [7.6.28](/7.6.28), the use of swimming for **chemotaxis** in [7.6.35](/7.6.35), and the collective motion of many swimmers in [7.6.37](/7.6.37). The partial differential equations used here are those of [2.5](/2.5), and the mechanics of [5.1](/5.1).

## 22.1. Water as a Continuum

### 22.1.1. The Velocity Field and the Material Derivative

A drop of water is $10^{21}$ molecules jostling at a few hundred meters per second. For the flows that matter to cells we do not need their positions: on any scale larger than a few nanometers the average velocity of the molecules in a small volume element varies smoothly from place to place. The fluid is then described by a density $\rho(\boldsymbol{r}, t)$ and a velocity field $\boldsymbol{u}(\boldsymbol{r}, t)$, the velocity of the fluid element that happens to be at $\boldsymbol{r}$ at time $t$. The continuum description fails only within a nanometer or so of a molecular surface, where the structure of water itself matters ([7.6.6](/7.6.6)); even the friction on a single protein is predicted well by it ([7.6.8](/7.6.8#sec-8.7)).

The acceleration of a fluid element is not $\partial\boldsymbol{u}/\partial t$, because the element moves: in a time $\Delta t$ it travels to $\boldsymbol{r} + \boldsymbol{u}\Delta t$, where the field is different. Expanding $\boldsymbol{u}(\boldsymbol{r} + \boldsymbol{u}\Delta t, t + \Delta t)$ to first order gives the acceleration

$$
\boldsymbol{a} = \frac{\mathrm{D}\boldsymbol{u}}{\mathrm{D}t} = \frac{\partial\boldsymbol{u}}{\partial t} + (\boldsymbol{u}\cdot\nabla)\boldsymbol{u}. \tag{22.1}
$$
The operator $\mathrm{D}/\mathrm{D}t = \partial/\partial t + \boldsymbol{u}\cdot\nabla$ is the material derivative, the rate of change seen by an observer riding with the fluid. The second, convective term is nonlinear in $\boldsymbol{u}$; it is present even in a steady flow, as in water circulating at constant speed around a bend, whose elements accelerate towards the center of curvature.

Conservation of mass, $\partial\rho/\partial t + \nabla\cdot(\rho\boldsymbol{u}) = 0$, is the **continuity equation** of the fluid. Water is nearly incompressible: its density changes by $5\times10^{-5}$ per atmosphere, and the pressures and speeds in biological flows change it negligibly. With constant $\rho$ the continuity equation becomes

$$
\nabla\cdot\boldsymbol{u} = 0, \tag{22.2}
$$
which states that the volume of every fluid element is conserved: the rate of change of the volume of a small box, $\Delta x\,\Delta y\,\Delta z\,(\partial_x u_x + \partial_y u_y + \partial_z u_z)$, must vanish.

### 22.1.2. Viscosity

A fluid differs from a solid in that it offers no resistance to a deformation held fixed, only to the rate of deformation. Shear a layer of fluid of thickness $d$ between two plates of area $A$ by moving one plate at speed $v$ relative to the other. For simple fluids the force needed is

$$
\frac{F}{A} = \eta\,\frac{v}{d}, \tag{22.3}
$$
Newton's law of viscous flow (in the *Principia*), with the **viscosity** $\eta$ ([5.2.2](/5.2.2)) as material constant. The fluid in contact with each plate moves with the plate, and the velocity varies linearly across the gap.

**Definition 22.1.1 (Newtonian Fluid)** A **Newtonian fluid** is a fluid whose viscous stress is proportional to the rate of strain, with a viscosity $\eta$ independent of the rate and history of the deformation. For an incompressible Newtonian fluid the stress tensor is

$$
\sigma_{ij} = -p\,\delta_{ij} + \eta\left(\frac{\partial u_i}{\partial x_j} + \frac{\partial u_j}{\partial x_i}\right),
$$
where $p$ is the pressure.

The microscopic origin of viscosity is the transport of momentum by thermal motion: molecules that jump from a faster to a slower layer carry their extra momentum with them and drag the slower layer along, as cars changing from a fast to a slow lane of a highway slow down the fast lane. Water, plasma and the cytosol around small molecules are Newtonian; blood, mucus, the cytoplasm on the scale of organelles and the extracellular matrix are not (22.7).

| Fluid | Viscosity $\eta$ / $\mathrm{mPa\,s}$ |
|---|---|
| Water, $20\,^\circ\mathrm{C}$ / $25\,^\circ\mathrm{C}$ / $37\,^\circ\mathrm{C}$ | $1.00$ / $0.89$ / $0.69$ |
| Blood plasma, $37\,^\circ\mathrm{C}$ | $1.2$–$1.3$ |
| Whole blood in large vessels (hematocrit $45\,\%$) | $3$–$4$ |
| Cytosol for small molecules and GFP (fluid-phase viscosity) | about $1$–$3$ |
| Glycerol, $20\,^\circ\mathrm{C}$ | $1.4\times10^3$ |
| Honey | about $10^4$ |
| Embryonic tissues on hour time scales ([7.5.8](/7.5.8)) | $10^8$–$10^9$ |

### 22.1.3. The Navier–Stokes Equations

Newton's second law for a fluid element of volume $\Delta V$ balances its mass times acceleration against the forces exerted by the surrounding fluid. The pressure pushes on opposite faces of the element with forces that differ by $-(\partial p/\partial x)\Delta V$ along $x$, so the net pressure force is $-\nabla p\,\Delta V$. The viscous forces on opposite faces differ by the second derivative of the velocity: for a shear flow $\boldsymbol{u} = u_z(x)\boldsymbol{e}_z$, Eq. (22.3) gives a force $\eta(\partial u_z/\partial x)$ per area on each face perpendicular to $x$, and the difference across the element is $\eta(\partial^2u_z/\partial x^2)\Delta V$. For a general flow, isotropy allows only two vector combinations of two derivatives and $\boldsymbol{u}$, namely $\nabla^2\boldsymbol{u}$ and $\nabla(\nabla\cdot\boldsymbol{u})$, and the second vanishes by Eq. (22.2).

**Definition 22.1.2 (Navier–Stokes Equations)** The **Navier–Stokes equations** for an incompressible Newtonian fluid of density $\rho$ and viscosity $\eta$, subject to a body force $\boldsymbol{f}$ per volume, are

$$
\rho\left(\frac{\partial\boldsymbol{u}}{\partial t} + (\boldsymbol{u}\cdot\nabla)\boldsymbol{u}\right) = -\nabla p + \eta\nabla^2\boldsymbol{u} + \boldsymbol{f}, \qquad \nabla\cdot\boldsymbol{u} = 0. \tag{22.4}
$$
Dividing by $\rho$ shows that the viscosity enters through the kinematic viscosity $\nu = \eta/\rho$, the diffusion coefficient of momentum ($10^{-6}\,\mathrm{m^2\,s^{-1}}$ for water).

The equations are four equations for four unknown fields, $\boldsymbol{u}$ and $p$; the pressure is not an independent thermodynamic variable but whatever is needed to keep the flow divergence-free. All the phenomena of Newtonian flow, from the creeping of a bacterium to the turbulent wake of a whale, are contained in Eq. (22.4); the convective term makes it nonlinear and, at large speeds, chaotic.

A partial differential equation needs boundary conditions. At a solid wall the fluid cannot pass through, so the normal velocity of the fluid equals that of the wall. The tangential velocity also matches.

**Definition 22.1.3 (No-Slip Condition)** The **no-slip condition** states that at a solid boundary the velocity of the fluid equals the velocity of the boundary.

The no-slip condition is an empirical law, very well satisfied for water on hydrophilic surfaces down to a nanometer; on strongly hydrophobic surfaces slip lengths of a few nanometers have been measured, too small to matter for cells. The dust that remains on a running fan blade is the everyday evidence.

## 22.2. The River Within: Flow in Vessels

### 22.2.1. Poiseuille Flow

The simplest exact solution of Eq. (22.4) is steady flow through a straight pipe of diameter $d$ and length $l$ driven by a pressure drop $\Delta p$. By symmetry the velocity is $\boldsymbol{u} = u(r)\boldsymbol{e}_z$, with $r$ the distance from the axis. Then $(\boldsymbol{u}\cdot\nabla)\boldsymbol{u} = u\,\partial_z\boldsymbol{u} = \boldsymbol{0}$: the nonlinear term vanishes identically, whatever the speed, as long as the flow stays laminar.

**Formula 22.2.1 (Hagen–Poiseuille Law)** For steady laminar flow of a Newtonian fluid through a circular pipe,

$$
u(r) = \frac{\Delta p}{4\eta l}\left(\frac{d^2}{4} - r^2\right), \qquad \bar u = \frac{\Delta p\,d^2}{32\eta l}, \qquad Q = \frac{\pi\,\Delta p\,d^4}{128\,\eta l}, \tag{22.5}
$$
where $\bar u$ is the mean velocity and $Q$ the volume flow rate.

**Proof** Balance the forces on a cylindrical shell of radius $r$, thickness $\Delta r$ and length $\Delta z$. The pressure force along $z$ is $-(\mathrm{d}p/\mathrm{d}z)\,2\pi r\,\Delta r\,\Delta z$; the viscous force is the difference of the shear stresses $\eta u'$ on its outer and inner surfaces, $\eta\,\frac{\mathrm{d}}{\mathrm{d}r}(2\pi r u')\Delta r\,\Delta z$. Their sum vanishes in steady flow:

$$
\frac{1}{r}\frac{\mathrm{d}}{\mathrm{d}r}\left(r\frac{\mathrm{d}u}{\mathrm{d}r}\right) = \frac{1}{\eta}\frac{\mathrm{d}p}{\mathrm{d}z} = -\frac{\Delta p}{\eta l},
$$
the Navier–Stokes equation in cylindrical coordinates. Integrating twice, $u = -\Delta p\,r^2/(4\eta l) + C_1\ln r + C_2$. Finiteness on the axis requires $C_1 = 0$, and the no-slip condition $u(d/2) = 0$ gives $C_2 = \Delta p\,d^2/(16\eta l)$. Integrating $u$ over the cross-section gives $Q = \int_0^{d/2}u\,2\pi r\,\mathrm{d}r = \pi\Delta p\,d^4/(128\eta l)$ and $\bar u = Q/(\pi d^2/4)$. $\square$

The fourth power is the striking result: at a fixed pressure difference, a vessel narrowed by $20\,\%$ carries $0.8^4 = 41\,\%$ of the flow. Arterioles, whose smooth muscle changes their diameter by tens of percent, therefore control the distribution of blood among organs, and the resistance of the circulation lies mostly in arterioles and capillaries, not in the large arteries.

![Poiseuille flow. A: the parabolic velocity profile in a pipe, normalized by the mean velocity: the fluid at the wall is at rest (no slip), and the center moves at twice the mean. B: flow rate at fixed pressure drop against the diameter of the vessel: Q ∝ d⁴, so a vessel narrowed by 20 % carries only 41 % of the flow; a plug flow at fixed speed would scale only as d²](./plots/pipe-flow.py)

**Example 22.2.1 (Blood in a capillary)** A capillary has a diameter of about $6\,\mu\mathrm{m}$ and a length of about $1\,\mathrm{mm}$, and the blood pressure falls across it by about $2.7\,\mathrm{kPa}$ ($20\,\mathrm{mmHg}$, from about $4.7$ to $2.0\,\mathrm{kPa}$). With the viscosity of whole blood, $\eta = 3.5\,\mathrm{mPa\,s}$, Formula 22.2.1 gives $\bar u = 2.7\times10^3 \times (6\times10^{-6})^2/(32 \times 3.5\times10^{-3} \times 10^{-3})\,\mathrm{m\,s^{-1}} = 0.9\,\mathrm{mm\,s^{-1}}$, in the measured range of $0.3$–$1\,\mathrm{mm\,s^{-1}}$. The agreement is partly fortuitous: red cells, $8\,\mu\mathrm{m}$ across, pass through capillaries in single file, deformed into bullet shapes, and blood is not a Newtonian fluid on this scale. In tubes narrower than about $300\,\mu\mathrm{m}$ the apparent viscosity of blood falls with diameter, because the cells crowd towards the axis and leave a cell-free, low-viscosity layer at the wall (the Fåhræus–Lindqvist effect); in the narrowest capillaries it rises again.

The Reynolds number of the flow (22.3) is $\rho\bar u d/\eta = 10^3 \times 10^{-3} \times 6\times10^{-6}/3.5\times10^{-3} \approx 2\times10^{-3}$: blood in a capillary flows like honey. In the aorta, $2\,\mathrm{cm}$ across with a mean velocity of about $0.2\,\mathrm{m\,s^{-1}}$, the Reynolds number is about $10^3$, and at the peak of systole it approaches the range where turbulence appears.

### 22.2.2. Leukocyte Rolling

White blood cells use the bloodstream to reach any tissue quickly and must leave it where an infection or injury calls them. Inflamed endothelium expresses P- and E-**selectin**, which bind carbohydrate ligands on the leukocyte surface with bonds that form and break within a fraction of a second. A leukocyte that touches the wall is then neither swept away nor stuck: it rolls along the wall at a few to tens of micrometers per second, much slower than the surrounding blood, until stronger, integrin-mediated adhesion arrests it and it crawls out between the endothelial cells ([7.3.23](/7.3.23)).

**Example 22.2.2 (The force on a rolling leukocyte)** A sphere of radius $a$ resting on a wall in a shear flow with wall shear stress $\tau_{\mathrm{w}}$ feels a drag force $F = 1.70 \times 6\pi a^2\tau_{\mathrm{w}} \approx 32\,a^2\tau_{\mathrm{w}}$ and a torque $0.94 \times 4\pi a^3\tau_{\mathrm{w}}$ (Goldman, Cox and Brenner 1967; the factors correct the Stokes drag of 22.4 for the presence of the wall). For a leukocyte, $a \approx 4\,\mu\mathrm{m}$, in a postcapillary venule with $\tau_{\mathrm{w}} \approx 0.2\,\mathrm{Pa}$, $F \approx 32 \times 1.6\times10^{-11} \times 0.2\,\mathrm{N} \approx 100\,\mathrm{pN}$. Single selectin bonds survive forces of tens of piconewtons for a fraction of a second ([7.6.17](/7.6.17)), so the cell is held by a few bonds at a time at the rear of its contact zone, each pulled while new bonds form at the front: the rolling velocity is set by bond kinetics, not by hydrodynamics. Selectin bonds are **catch bonds** ([7.3.23](/7.3.23)) whose lifetime first increases with force; leukocytes therefore roll only above a threshold shear stress and roll more stably at higher shear, a mechanical "brake" that keeps them from sticking in stagnant blood.

## 22.3. The Reynolds Number

### 22.3.1. Inertial Against Viscous Forces

Consider a body of size $L$ moving at speed $U$ through a fluid. The fluid velocity changes by about $U$ over distances of about $L$, so the inertial term of Eq. (22.4) is of order $\rho U^2/L$ and the viscous term of order $\eta U/L^2$. Their ratio is a single dimensionless number.

**Definition 22.3.1 (Reynolds Number)** The **Reynolds number** of a flow with characteristic speed $U$ and length $L$ is

$$
\operatorname{Re} = \frac{\rho UL}{\eta} = \frac{UL}{\nu},
$$
the ratio of inertial to viscous forces. Flows with $\operatorname{Re} \ll 1$ are dominated by viscosity; flows with $\operatorname{Re} \gg 1$ by inertia.

Two other readings of the same number are useful. The kinetic energy of a fluid parcel of size $L$, about $\rho L^3U^2$, compared with the work done against viscous stresses $\eta U/L$ over an area $L^2$ while the parcel moves a distance $L$, $\eta UL^2$, gives $\operatorname{Re}$ again: at low Reynolds number the kinetic energy is dissipated before the parcel has moved its own size. Equivalently, $\operatorname{Re}$ is the ratio of the viscous time $\tau_\nu = \rho L^2/\eta$, the time for momentum to diffuse across the body, to the time $L/U$ to travel its length.

**Example 22.3.1** For *E. coli*, $L = 2\,\mu\mathrm{m}$ and $U = 30\,\mu\mathrm{m\,s^{-1}}$: $\operatorname{Re} = 30\times10^{-6} \times 2\times10^{-6}/10^{-6} = 6\times10^{-5}$. A vesicle of $200\,\mathrm{nm}$ carried by kinesin at $1\,\mu\mathrm{m\,s^{-1}}$ has $\operatorname{Re} = 2\times10^{-7}$, and a person swimming at $1.5\,\mathrm{m\,s^{-1}}$ about $3\times10^6$. A person who wanted to swim at the Reynolds number of a bacterium would have to swim in a fluid $10^{10}$ to $10^{11}$ times more viscous than water, a pool of tar, and move his arms at a centimeter per minute. The pitch-drop experiment at the University of Queensland, where a drop of bitumen falls about once a decade, is a demonstration of this world on our scale.

![Reynolds numbers in biology. A: Re = vL/ν of swimmers against their body length (typical speeds): microorganisms live below Re = 1 (shaded), where viscosity dominates, while fish and whales live at Re of 10⁴–10⁸, where inertia does; the copepod's escape jumps and the larvae of fish cross the transition. B: distance a sphere of the density of water coasts after its propulsion stops, started at a speed of two body radii per second and slowed by Stokes drag (valid while Re ≪ 1): a bacterium stops within 10⁻³ nm, far less than the size of a water molecule](./plots/reynolds-scales.py)

### 22.3.2. The Overdamped Limit

The disappearance of inertia can be seen in the simplest mechanical system, a damped oscillator $m\ddot x + \gamma\dot x + kx = 0$. Its solutions are $\mathrm{e}^{\lambda_\pm t}$ with $\lambda_\pm = [-\gamma \pm \sqrt{\gamma^2 - 4km}]/2m$. When the viscous time $m/\gamma$ is much shorter than the relaxation time $\gamma/k$, that is $km/\gamma^2 \ll 1$, the roots are $\lambda_+ \approx -k/\gamma$ and $\lambda_- \approx -\gamma/m$. The second mode decays within $m/\gamma$ and carries the memory of the initial velocity; afterwards

$$
x(t) = x_0\,\mathrm{e}^{-kt/\gamma},
$$
the solution of $\gamma\dot x + kx = 0$, the equation without the inertial term. In the overdamped limit force determines velocity, not acceleration: $\gamma\dot x = F$, the mechanics of Aristotle rather than Newton. The overdamped Langevin equation of [7.6.5](/7.6.5#sec-5.4.2) and the models of motors in [7.6.27](/7.6.27) rest on this limit.

**Example 22.3.2 (Coasting)** A bacterium of radius $a = 1\,\mu\mathrm{m}$ and the density of water has a viscous time $\tau = m/6\pi\eta a = 2\rho a^2/9\eta = 2 \times 10^3 \times 10^{-12}/(9\times10^{-3})\,\mathrm{s} = 0.2\,\mu\mathrm{s}$. If its motor stops while it swims at $30\,\mu\mathrm{m\,s^{-1}}$, it coasts $30\times10^{-6} \times 2\times10^{-7}\,\mathrm{m} \approx 0.007\,\mathrm{nm}$, a few percent of the diameter of a hydrogen atom (Purcell, 1977). Its Brownian motion carries it farther in the same time: $\sqrt{2Dt}$ with $D = 0.2\,\mu\mathrm{m^2\,s^{-1}}$ is $0.3\,\mathrm{nm}$ in $0.2\,\mu\mathrm{s}$.

## 22.4. Stokes Flow

### 22.4.1. The Stokes Equations and Their Symmetries

When $\operatorname{Re} \ll 1$ the left-hand side of Eq. (22.4) can be dropped, leaving the equations of **Stokes flow** ([Definition 8.5.1](/7.5.8#def-8.5.1) of 7.5.8)

$$
\eta\nabla^2\boldsymbol{u} = \nabla p - \boldsymbol{f}, \qquad \nabla\cdot\boldsymbol{u} = 0. \tag{22.6}
$$
The time derivative has also disappeared, because the viscous time $\rho L^2/\eta$, a microsecond for a bacterium, is shorter than any time on which the boundaries move. Three properties follow, and they govern everything in the rest of this chapter.

**Proposition 22.4.1 (Properties of Stokes Flow)** Let the fluid occupy a region bounded by surfaces whose velocities are prescribed.

1. (Instantaneity) The flow at time $t$ is determined by the boundary velocities and forces at the same instant; it has no memory.
2. (Linearity) If the boundary velocities are multiplied by a constant $c$, the velocity field and the forces on the boundaries are multiplied by $c$; solutions for different boundary motions add.
3. (Reversibility) If all boundary velocities are reversed, the velocity field and all forces are reversed.

**Proof** Eq. (22.6) contains no time derivative, so $\boldsymbol{u}$ and $p$ at time $t$ are the solution of a boundary value problem posed with the boundary data at $t$ (the solution is unique, since the difference of two solutions with the same data has zero dissipation, $\eta\int\lvert\nabla\boldsymbol{u}\rvert^2\,\mathrm{d}V = 0$). The equations and the no-slip boundary condition are linear in $(\boldsymbol{u}, p)$, which gives 2, and 3 is the case $c = -1$. $\square$

Reversibility has a famous demonstration (G. I. Taylor): a drop of dye in glycerol between two concentric cylinders is smeared into a thin streak by turning the inner cylinder a few times and reassembles almost perfectly into a drop when the cylinder is turned back the same number of times, at any speed. Only the slow diffusion of the dye spoils the reconstruction.

### 22.4.2. Stokes' Law

The drag on a sphere follows, up to a numerical factor, from linearity and dimensions alone. A sphere of radius $a$ moving at velocity $\boldsymbol{U}$ creates velocity gradients of order $U/a$, hence viscous stresses and pressures of order $\eta U/a$ over an area of order $a^2$: the force is $C\eta aU$. Linearity demands that it be proportional to $U$, and $\eta a$ is the only combination of the remaining parameters with the units of a friction coefficient ($\mathrm{N\,s\,m^{-1}}$). The density does not appear: the drag at low Reynolds number does not depend on the mass of the fluid.

**Theorem 22.4.2 (Stokes' Law)** A rigid sphere of radius $a$ translating with velocity $\boldsymbol{U}$ through an unbounded fluid at rest at infinity, at $\operatorname{Re} \ll 1$, experiences the drag force

$$
\boldsymbol{F} = -6\pi\eta a\,\boldsymbol{U}. \tag{22.7}
$$
In the frame of the sphere, with uniform flow $U$ along $z$ at infinity and polar angle $\theta$ measured from $z$, the velocity field is

$$
u_r = U\cos\theta\left(1 - \frac{3a}{2r} + \frac{a^3}{2r^3}\right), \qquad u_\theta = -U\sin\theta\left(1 - \frac{3a}{4r} - \frac{a^3}{4r^3}\right),
$$
with pressure $p = p_\infty - \frac{3}{2}\eta aU\cos\theta/r^2$.

**Proof** The field satisfies $\nabla\cdot\boldsymbol{u} = 0$ (it derives from the stream function $\psi = \frac12 Ur^2\sin^2\theta\,(1 - 3a/2r + a^3/2r^3)$), vanishes on $r = a$ and tends to $U\boldsymbol{e}_z$ at infinity; substitution shows that it satisfies $\eta\nabla^2\boldsymbol{u} = \nabla p$ with the stated pressure, and the solution is unique (Proposition 22.4.1). On the surface the normal viscous stress vanishes, and the traction is $\boldsymbol{t} = -p\,\boldsymbol{e}_r + \eta\,(\partial u_\theta/\partial r)\,\boldsymbol{e}_\theta$ with $\partial u_\theta/\partial r = -\frac{3U}{2a}\sin\theta$ at $r = a$. The $z$ component of the traction is $\frac{3\eta U}{2a}\cos^2\theta + \frac{3\eta U}{2a}\sin^2\theta = \frac{3\eta U}{2a}$, uniform over the sphere (the pressure contributes one third and the shear stress two thirds of the total). Multiplying by the area $4\pi a^2$ gives $6\pi\eta aU$ in the direction of the flow, the force on a sphere at rest in a stream $U$, equivalent to Eq. (22.7). $\square$

The flow carries two lessons for cells. The disturbance decays as $a/r$ (the leading terms of $u_r$ and $u_\theta$ beyond the uniform flow), so a moving particle drags fluid along over many times its own size; potential flow around a sphere, the large-Reynolds-number idealization, decays as $(a/r)^3$. The $a/r$ field, the flow of a point force, is the Stokeslet. Hydrodynamic interactions between swimming cells, between a cell and a nearby wall, and between proteins in concentrated solutions are therefore long-ranged ([7.6.23](/7.6.23), [7.6.37](/7.6.37)). And the flow is symmetric fore and aft: nothing distinguishes the front of the sphere from its back, unlike the wake behind a moving boat.

![Stokes flow past a sphere (exact solution, Theorem 22.4.2). A: streamlines in the frame of the sphere, shaded by speed: the flow is symmetric fore and aft and slowed over several radii. B: the same flow seen from the distant fluid, with the sphere moving to the right at U: fluid is dragged along with the sphere and returns around it. C: the disturbance velocity along the axis and in the equatorial plane falls as a/r, the field of a point force, compared with (a/r)³ for inviscid potential flow](./plots/stokes-flow.py)

Theorem 22.4.2 underlies the **Stokes–Einstein equation** $D = k_{\mathrm{B}}T/6\pi\eta a$ ([6.3.17](/6.3.17)) and the hydrodynamic analysis of macromolecules ([7.6.8](/7.6.8#sec-8.7)). The rotational analog, the torque $8\pi\eta a^3\Omega$ on a sphere rotating at angular velocity $\Omega$, follows from the same dimensional argument and gives the **rotational diffusion** coefficient ([7.6.5](/7.6.5#sec-5.3.2)).

### 22.4.3. Slender Bodies

Flagella, cilia, cytoskeletal filaments and many bacteria are long and thin. Repeating the dimensional argument for a rod of length $L$ and radius $b \ll L$, the gradients are of order $U/b$ over an area $2\pi bL$, so the drag is of order $\eta UL$: the largest dimension of a body sets its drag, not its volume or cross-section. The ratio $L/b$ is dimensionless, so dimensions alone leave room for a function of it, which turns out to be only logarithmic.

**Formula 22.4.1 (Drag on a Slender Rod)** A straight rod of length $L$ and radius $b$ with $L \gg b$ translating along its axis or perpendicular to it experiences the drag forces $F_\parallel = \gamma_\parallel U$ and $F_\perp = \gamma_\perp U$, with

$$
\gamma_\parallel \approx \frac{2\pi\eta L}{\ln(L/b) - 0.2}, \qquad \gamma_\perp \approx \frac{4\pi\eta L}{\ln(L/b) + 0.84},
$$
so that $\gamma_\perp \approx 2\gamma_\parallel$ for very slender rods (the constants are those of the numerical solutions of Tirado and García de la Torre for cylinders). A rod moving obliquely is pulled sideways: the drag is not parallel to the velocity.

The factor of two between the two drag coefficients, an exact result in the limit of infinite slenderness, is the basis of flagellar propulsion (22.5.3) and of the orientation dependence of the friction and **rotational diffusion** of rod-like molecules ([7.6.8](/7.6.8#sec-8.7.3)).

### 22.4.4. Drag in Single-Molecule Experiments

**Example 22.4.1 (Is the bead a burden?)** In an optical-trap experiment a motor such as kinesin or myosin carries a polystyrene bead of radius $0.5\,\mu\mathrm{m}$ at about $1\,\mu\mathrm{m\,s^{-1}}$ (**optical tweezers**, [7.6.17](/7.6.17)). The bead's Stokes drag is $6\pi \times 10^{-3} \times 0.5\times10^{-6} \times 10^{-6}\,\mathrm{N} \approx 0.01\,\mathrm{pN}$, a five-hundredth of the motor's **stall force** of about $5$–$7\,\mathrm{pN}$. Viscous drag on the bead does not perturb the motor; the load is applied by the trap. The bead's drag matters only for the time resolution: with a trap of stiffness $\kappa$ the bead follows the motor with relaxation time $6\pi\eta a/\kappa$, about $0.1\,\mathrm{ms}$ for $\kappa = 0.1\,\mathrm{pN\,nm^{-1}}$ ([7.6.5](/7.6.5#sec-5.4.2)).

**Example 22.4.2 (A rotating actin filament on F₁)** The opposite case is the experiment that showed that the F₁ part of the **ATP synthase** rotates (Noji, Yasuda, Yoshida and Kinosita 1997): an α₃β₃γ complex is fixed to a surface, and a fluorescent actin filament of length $L$ attached to the γ subunit is seen to rotate when ATP is added. The rotational drag coefficient of a thin rod rotating about one end is $\zeta = \frac{4\pi\eta L^3}{3[\ln(L/2b) - 0.45]}$; for $L = 1\,\mu\mathrm{m}$ and $b = 4\,\mathrm{nm}$, $\zeta \approx 1.0\times10^{-21}\,\mathrm{N\,m\,s}$. Here the drag is the whole load. The measured rotation rate, about $6$ revolutions per second for a $1\,\mu\mathrm{m}$ filament and falling as $L^{-3}$ for longer filaments, gives the torque $\zeta\omega \approx 1.0\times10^{-21} \times 2\pi \times 6\,\mathrm{N\,m} \approx 40\,\mathrm{pN\,nm}$, and the work per $120^\circ$ step, $40 \times 2\pi/3 \approx 80\,\mathrm{pN\,nm}$, close to the free energy of hydrolysis of one ATP under the conditions of the experiment: the motor is nearly perfectly efficient ([7.6.28](/7.6.28)). Measuring a torque by the drag of a known object is the low-Reynolds-number dynamometer.

## 22.5. Swimming Without Inertia

### 22.5.1. The Scallop Theorem

A swimmer at low Reynolds number exerts no net force or torque on the fluid at any instant: there is no inertia to absorb an impulse, so the propulsive force of its moving parts and the drag on its body balance exactly at every moment. Its motion is therefore determined by the sequence of shapes it adopts, not by how fast it adopts them.

**Theorem 22.5.1 (Scallop Theorem)** A body swimming at zero Reynolds number in a Newtonian fluid whose shape changes go through a sequence of shapes and then return through the same sequence in reverse order (a reciprocal stroke) has zero net displacement and rotation after one stroke, whatever the rates of the two half-strokes (Purcell, 1977).

**Proof** Describe the shape by a parameter $s(t)$ that runs from $s_0$ to $s_1$ and back. By instantaneity and linearity (Proposition 22.4.1), the velocity of the body at time $t$ is linear in the rate of shape change at the same instant and depends otherwise only on the current shape: $\dot X = V(s)\,\dot s$ for the position (and similarly for the orientation, for which the argument is the same with rotations composed). Then the displacement over a stroke is $\int V(s)\dot s\,\mathrm{d}t = \int_{s_0}^{s_1}V(s)\,\mathrm{d}s + \int_{s_1}^{s_0}V(s)\,\mathrm{d}s = 0$, independent of the time course $s(t)$. $\square$

A scallop that opens slowly and claps shut quickly swims at high Reynolds number, where the fast clap expels a jet whose momentum the slow opening does not undo. At low Reynolds number the same stroke leaves it where it started. The theorem rules out every one-parameter swimming stroke: a swimmer needs at least two independent shape variables, changed out of phase, so that its stroke traces a closed loop of nonzero area in shape space. The theorem assumes a Newtonian fluid and a single swimmer: in a viscoelastic fluid, whose stress depends on the rate of deformation (22.7), or near another swimmer, reciprocal strokes can produce net motion.

### 22.5.2. Purcell's Three-Link Swimmer

Purcell's minimal swimmer has three rigid links joined by two hinges, with hinge angles $\alpha_1$ and $\alpha_2$. Moving first one arm, then the other, then the first back and then the second back traces a square in the $(\alpha_1, \alpha_2)$ plane. The motion of the body follows from two conditions at every instant, zero total force and zero total torque, with the drag on each element of each link given by the anisotropic friction of Formula 22.4.1 (the local drag approximation of 22.5.3).

**Algorithm 22.5.1 (Swimming by Force-Free Shape Changes)** For a swimmer whose shape is given by internal coordinates $\boldsymbol{\alpha}(t)$ and whose position and orientation are $\boldsymbol{X}$ and $\phi$:

1. Write the velocity of each point of the body as a linear function of $(\dot{\boldsymbol{X}}, \dot\phi, \dot{\boldsymbol{\alpha}})$.
2. Compute the local drag on each element, $\mathrm{d}\boldsymbol{F} = -[\gamma_\parallel\boldsymbol{t}\boldsymbol{t}^{\mathsf T} + \gamma_\perp(I - \boldsymbol{t}\boldsymbol{t}^{\mathsf T})]\boldsymbol{v}\,\mathrm{d}s$, with $\boldsymbol{t}$ the local tangent.
3. Impose $\sum\mathrm{d}\boldsymbol{F} = \boldsymbol{0}$ and $\sum\boldsymbol{r}\times\mathrm{d}\boldsymbol{F} = \boldsymbol{0}$: three linear equations (in two dimensions) that give $(\dot{\boldsymbol{X}}, \dot\phi)$ in terms of $\dot{\boldsymbol{\alpha}}$.
4. Integrate along the prescribed path in shape space.

The simulation in the figure shows the theorem at work. The square stroke moves the swimmer forward by a fixed fraction of its length per stroke, whatever the speed of the stroke; the reciprocal stroke in which both arms flap together goes back and forth along a line and returns exactly to its starting point. For small amplitudes the displacement per stroke is proportional to the area enclosed by the loop in shape space, the square of the amplitude: swimming at low Reynolds number is a geometric phase, and the efficiency of a stroke is a question of geometry.

![Purcell's three-link swimmer simulated with Algorithm 22.5.1 (γ⊥ = 2γ∥, links of length l). A: the four shapes at the corners of the square stroke: the front arm swings first, then the rear arm, then the front arm back, then the rear arm back. B: path of the center of the middle link over three strokes (hinge amplitude ±45°): the square stroke advances along the body axis by about 0.13 l per stroke, with large sideways excursions within each stroke, while reciprocal flapping of both arms together moves the swimmer sideways and back along the same line, with no net displacement (scallop theorem). C: net displacement per stroke against the hinge amplitude: it grows as the square of the amplitude, the area of the loop in shape space, and more slowly at large amplitudes](./plots/purcell-swimmer.py)

### 22.5.3. Resistive-Force Theory and the Helical Flagellum

The drag on a flexible filament can be computed by treating each short segment as a piece of a straight rod, neglecting the flow created by distant parts of the filament.

**Definition 22.5.1 (Resistive-Force Theory)** **Resistive-force theory** (Gray and Hancock, 1955) approximates the force per length on a slender filament moving through a viscous fluid by the drag of a straight rod with the local tangent $\boldsymbol{t}$:

$$
\boldsymbol{f} = -\gamma_\parallel(\boldsymbol{v}\cdot\boldsymbol{t})\boldsymbol{t} - \gamma_\perp[\boldsymbol{v} - (\boldsymbol{v}\cdot\boldsymbol{t})\boldsymbol{t}],
$$
where $\boldsymbol{v}$ is the local velocity of the filament relative to the fluid and $\gamma_\parallel$, $\gamma_\perp$ are drag coefficients per length, with $\gamma_\perp/\gamma_\parallel$ close to $2$ (Formula 22.4.1, with $L$ replaced by a length of the order of the wavelength).

Consider a helix of radius $R$ and pitch angle $\theta$ (the angle between the filament and the helix axis, $\tan\theta = 2\pi R/\lambda$ for a pitch $\lambda$) rotating about its axis at angular velocity $\omega$. Each segment moves sideways at $v = \omega R$ in the azimuthal direction. Its velocity has a component $v\sin\theta$ along the filament and $v\cos\theta$ across it, and the corresponding drag forces, $\gamma_\parallel v\sin\theta$ and $\gamma_\perp v\cos\theta$, have components along the axis of $\gamma_\parallel v\sin\theta\cos\theta$ and $-\gamma_\perp v\cos\theta\sin\theta$. They do not cancel.

**Formula 22.5.1 (Propulsion by a Rotating Helix)** A helix of length $L$ rotating at $\omega$ and translating along its axis at speed $U$ experiences, by resistive-force theory, the axial force

$$
F = (\gamma_\perp - \gamma_\parallel)\,\omega R\,L\sin\theta\cos\theta - (\gamma_\parallel\cos^2\theta + \gamma_\perp\sin^2\theta)\,LU.
$$
A cell body of drag coefficient $\zeta_{\mathrm{b}}$ (for a sphere $6\pi\eta a$) pushed by the helix swims, by the force balance $F = \zeta_{\mathrm{b}}U$, at

$$
U = \frac{(\gamma_\perp - \gamma_\parallel)\,\omega R\,L\sin\theta\cos\theta}{(\gamma_\parallel\cos^2\theta + \gamma_\perp\sin^2\theta)L + \zeta_{\mathrm{b}}}. \tag{22.8}
$$

Thrust requires $\gamma_\perp \neq \gamma_\parallel$: a helix of spheres that each had isotropic drag would not swim. It is largest near $\theta = 45^\circ$, where $\sin\theta\cos\theta$ is maximal, and vanishes for a straight rod ($\theta = 0$) and for a ring ($\theta = 90^\circ$). The torque that turns the helix must be balanced by an opposite torque on the body, which therefore counter-rotates; this is why a swimming *E. coli* rolls slowly about its long axis.

**Example 22.5.1 (*E. coli*)** The normal flagellar filament of *E. coli* has a helix radius of about $0.2\,\mu\mathrm{m}$, a pitch of $2.3\,\mu\mathrm{m}$ ($\theta \approx 29^\circ$), a diameter of $20\,\mathrm{nm}$ and a length of about $7\,\mu\mathrm{m}$, and the bundle of several filaments turns at about $100\,\mathrm{Hz}$ relative to the fluid. With $\gamma_\parallel \approx 2\pi\eta/[\ln(0.18\lambda/b) - 0.5] \approx 2\times10^{-3}\,\mathrm{Pa\,s}$ (Lighthill's coefficient for a helix), $\gamma_\perp = 2\gamma_\parallel$ and a body of effective radius $0.8\,\mu\mathrm{m}$, Eq. (22.8) gives $U \approx 23\,\mu\mathrm{m\,s^{-1}}$, close to the measured $20$–$30\,\mu\mathrm{m\,s^{-1}}$. The pitch angle of the natural filament lies near the optimum of the propulsive efficiency, which is nevertheless only about $2\,\%$.

![Resistive-force theory of a rotating helical flagellum (Formula 22.5.1; helix radius 0.2 µm, pitch angle θ, length 7 µm, 100 Hz; body of effective radius 0.8 µm). A: swimming speed against the pitch angle for γ⊥/γ∥ = 1, 1.5 and 2: with isotropic drag there is no thrust, and with the slender-body ratio of 2 the natural pitch angle of *E. coli* (dotted) gives about 23 µm/s. B: propulsive efficiency, the power needed to drag the body at speed U, 6πηaU², divided by the power dissipated by the rotating helix: at most about 2 %, near θ = 45°](./plots/flagellum-rft.py)

### 22.5.4. Bending Waves: Sperm, Cilia and Metachronal Waves

Eukaryotic flagella and cilia do not rotate; they bend, driven by axonemal **dynein** ([7.3.14](/7.3.14#sec-14.6.2)). A planar wave $y = b\sin(kx - \omega t)$ traveling along a flagellum is nonreciprocal, because its time reverse is a wave traveling the other way. Resistive-force theory applied to a long flagellum gives, to second order in the amplitude,

$$
U \approx \frac12\left(\frac{\gamma_\perp}{\gamma_\parallel} - 1\right)(kb)^2\,\frac{\omega}{k}, \tag{22.9}
$$
directed opposite to the wave: a wave traveling from head to tail pushes the cell head first. For $\gamma_\perp = 2\gamma_\parallel$ this coincides with G. I. Taylor's exact result for an infinite waving sheet, $U = \frac12\omega kb^2$ (1951), the first calculation of swimming at low Reynolds number. For a human sperm, with a beat frequency of about $20\,\mathrm{Hz}$, a wavelength of about $40\,\mu\mathrm{m}$ and an amplitude of about $4\,\mu\mathrm{m}$ ($kb \approx 0.6$), Eq. (22.9) gives about $150\,\mu\mathrm{m\,s^{-1}}$; the drag of the head and the finite length of the flagellum reduce this to the observed $50$–$100\,\mu\mathrm{m\,s^{-1}}$.

A motile **cilium** ([7.3.14](/7.3.14#sec-14.6)) beats asymmetrically: an effective stroke with the cilium extended, which moves much fluid, and a recovery stroke with the cilium bent close to the cell surface, which moves less, because a rod moving perpendicular to itself has twice the drag of one moving along its length. The two strokes are different shapes, so the beat is not reciprocal. Neighboring cilia beat with a constant phase lag, forming metachronal waves that sweep over ciliated surfaces like wind over a field of wheat; hydrodynamic coupling between cilia is enough to synchronize them. On the airway epithelium such waves move a layer of mucus towards the pharynx at a few millimeters per minute, clearing inhaled particles; in the embryonic node a few hundred rotating cilia, tilted towards the posterior, drive a leftward flow that breaks the left–right symmetry of the body ([7.5](/7.5)).

### 22.5.5. The Bacterial Flagellar Motor

The flagellar filament is turned by a rotary motor in the cell envelope, powered by the **proton-motive force** (or a sodium gradient in some species) through stator units that push on a rotor ring; its structure and mechanism are in [7.3.14](/7.3.14#sec-14.6.5) and [7.6.28](/7.6.28). From the point of view of hydrodynamics, the motor is characterized by its torque–speed curve, measured by attaching beads of different sizes to filament stubs and observing their rotation, the dynamometer of Example 22.4.2.

At low speeds the torque of the *E. coli* motor is nearly constant, about $1300\,\mathrm{pN\,nm}$ near room temperature, up to a knee near $170\,\mathrm{Hz}$, and then falls nearly linearly to zero at about $300\,\mathrm{Hz}$ (Chen and Berg 2000). Each load is a straight line through the origin, torque $= \zeta\omega$; the motor runs at the intersection. The plateau region is nearly independent of temperature and of isotopic substitution of the protons, and the steep region depends on both: at high load the motor is close to equilibrium with its energy source, at low load its speed is limited by the rates of proton transfer. Driving a flagellar bundle, the motor works near the knee at $100$–$150\,\mathrm{Hz}$. The motor's output is the subject of [7.6.28](/7.6.28), which builds kinetic models that reproduce this curve.

![Torque–speed curve of the bacterial flagellar motor (*E. coli*, about 23 °C; schematic of bead measurements). A: the torque is nearly constant up to a knee near 170 Hz and then falls linearly to zero near 300 Hz. Each load is a line through the origin, torque = ζω, with ζ = 8πηr³ for a bead of radius r plus the drag of the stub; the motor runs at the intersection (dots). Large beads load the motor on its plateau, small gold particles probe the steep region; swimming cells operate near the knee (band). B: the mechanical power output τω, at most about 1 fW, against the useful power of about 0.01 fW needed to drag the cell body at 25 µm/s](./plots/motor-torque-speed.py)

**Example 22.5.2 (The energy budget of swimming)** The power needed to drag a body of effective radius $1\,\mu\mathrm{m}$ at $U = 25\,\mu\mathrm{m\,s^{-1}}$ is $6\pi\eta aU^2 = 6\pi \times 10^{-3} \times 10^{-6} \times (25\times10^{-6})^2\,\mathrm{W} \approx 1.2\times10^{-17}\,\mathrm{W}$, the free energy of hydrolysis of about $150$ ATP per second ($20\,k_{\mathrm{B}}T = 8\times10^{-20}\,\mathrm{J}$ each). Each motor delivers about $1300\,\mathrm{pN\,nm} \times 2\pi \times 120\,\mathrm{Hz} \approx 1\times10^{-15}\,\mathrm{W}$ and consumes, at about $1200$ protons per revolution and a proton-motive force of $150\,\mathrm{mV}$, about $3\times10^{-15}\,\mathrm{W}$. With five or so motors, swimming uses about $1.5\times10^{-14}\,\mathrm{W}$, the equivalent of some $2\times10^5$ ATP per second: a few percent of the energy budget of a growing *E. coli*, which hydrolyzes several million ATP per second ([7.6.20](/7.6.20)). Swimming is cheap for a bacterium, although its hydrodynamic efficiency is about $1\,\%$.

### 22.5.6. Why Swim?

Swimming does not help a bacterium feed by stirring its surroundings. Over the size of the cell the **Péclet number** $\mathrm{Pe} = UL/D$ for a nutrient of diffusion coefficient $D = 10^3\,\mu\mathrm{m^2\,s^{-1}}$ is about $0.03$ (Example 5.2.2 of [7.6.5](/7.6.5#sec-5.2.4)): diffusion replenishes the depleted zone around the cell faster than swimming carries the cell out of it, and the uptake rises by only a few percent. Swimming pays only over distances where it outruns diffusion. A cell that swims a distance $\ell$ in time $\ell/U$ beats a nutrient molecule that spreads $\sqrt{2D\ell/U}$ in the same time only if $\ell > 2D/U$, about $70\,\mu\mathrm{m}$ for $U = 30\,\mu\mathrm{m\,s^{-1}}$, some thirty body lengths. A bacterium must swim to find richer water, not to drink faster where it is: this is why it reads gradients over distances of tens of micrometers, by comparing concentrations in time while it runs ([7.6.35](/7.6.35)). Larger organisms are different: a ciliate or a sessile *Vorticella* of $100\,\mu\mathrm{m}$ with feeding currents of $1\,\mathrm{mm\,s^{-1}}$ has $\mathrm{Pe} \approx 100$ for small molecules and $10^5$ for bacteria, its prey, and its currents bring food it could never wait for.

## 22.6. Sedimentation and Buoyancy

### 22.6.1. Separation by Centrifugation

A particle of mass $m$ and volume $V$ in a centrifuge at angular velocity $\omega$ and radius $r$ feels the centrifugal force $(m - \rho V)\omega^2r$ corrected for buoyancy (Archimedes), and drifts at the velocity at which it is balanced by the drag. This is **sedimentation** ([6.3.21](/6.3.21)); its use to measure the **sedimentation coefficient** $s = v/\omega^2r$ and molar mass by the **Svedberg equation** is the subject of [7.6.8](/7.6.8#sec-8.8). For a sphere of density $\rho_{\mathrm{p}}$ in a field of acceleration $g_{\mathrm{c}}$ (gravity or $\omega^2r$), Stokes' law gives

$$
v_{\mathrm{drift}} = \frac{(\rho_{\mathrm{p}} - \rho)\frac43\pi a^3g_{\mathrm{c}}}{6\pi\eta a} = \frac{2(\rho_{\mathrm{p}} - \rho)g_{\mathrm{c}}a^2}{9\eta}, \tag{22.10}
$$
quadratic in the radius. This dependence is what separates particles in the preparative centrifuge.

**Formula 22.6.1 (Time to Separate Two Species)** Two species that start in a thin band and drift at $v_1$ and $v_2$ with diffusion coefficients $D_1$ and $D_2$ are resolved (centers farther apart than the sum of the band half-widths $\sqrt{2D_it}$) after

$$
t > t_{\mathrm{sep}} = \frac{\left(\sqrt{2D_1} + \sqrt{2D_2}\right)^2}{(v_1 - v_2)^2}.
$$
Since the bands separate as $t$ and broaden as $\sqrt t$, separation always succeeds given time; it must happen before the faster band reaches the bottom of the tube, $v_1t_{\mathrm{sep}} < L$, which sets the minimum acceleration of the centrifuge.

In rate-zonal centrifugation (**velocity sedimentation**) the sample is layered on top of a shallow sucrose gradient, which stabilizes the bands against convection, and the run is stopped before the bands reach the bottom. In isopycnic (equilibrium density-gradient) centrifugation the gradient spans the densities of the particles, each drifts until it reaches the density equal to its own, where $v_{\mathrm{drift}} = 0$ by Eq. (22.10), and the bands are equilibrium states whose width is set by diffusion; this is how Meselson and Stahl separated DNA labeled with $^{15}\mathrm{N}$ from DNA with $^{14}\mathrm{N}$ ([7.6.8](/7.6.8#sec-8.9.3)).

### 22.6.2. Gravity Against Thermal Motion

In a gravitational field, particles of buoyant mass $\Delta m = \Delta\rho V$ reach a Boltzmann distribution in height, $c(z) \propto \mathrm{e}^{-\Delta m gz/k_{\mathrm{B}}T}$, with the sedimentation length $\ell_g = k_{\mathrm{B}}T/\Delta m\,g$. Gravity matters for a particle when $\ell_g$ is smaller than its own size, that is when the energy released by its sinking one radius exceeds $k_{\mathrm{B}}T$: for $\Delta\rho = 100\,\mathrm{kg\,m^{-3}}$ this happens at $a^* = (3k_{\mathrm{B}}T/4\pi\Delta\rho\,g)^{1/4} \approx 1\,\mu\mathrm{m}$. Proteins and ribosomes never settle in a cell; bacteria settle slowly; the starch-filled amyloplasts (statoliths) of plant root cells, several micrometers across and much denser than the cytoplasm, sediment within minutes, which is how roots sense gravity. A bacterium of $1\,\mu\mathrm{m}$ with $\Delta\rho = 100\,\mathrm{kg\,m^{-3}}$ sinks at $0.2\,\mu\mathrm{m\,s^{-1}}$ by Eq. (22.10), a hundredth of its swimming speed.

Phytoplankton must stay in the sunlit surface layer. Many cyanobacteria and haloarchaea do so with gas vesicles, hollow protein shells of $50$–$250\,\mathrm{nm}$ diameter and up to a micrometer long, made of a single amphipathic protein (GvpA) whose hydrophobic inner surface excludes water while gas diffuses freely through the wall. With an effective density of about $120\,\mathrm{kg\,m^{-3}}$, a few percent of the cell volume in gas vesicles makes a cell neutrally buoyant. Cells regulate their depth by making vesicles in the dark and losing buoyancy when photosynthesis accumulates dense carbohydrate, or when turgor rises enough to collapse the vesicles; the speed of the resulting vertical migration grows as the square of the radius, so colonies migrate meters per hour while single cells hardly move.

![Gravity, buoyancy and thermal motion. A: sedimentation length k_BT/(Δm g) of spheres with a density excess of 100 kg/m³ against their radius: it equals the radius at about 1 µm (dot), below which thermal motion keeps particles suspended over heights much larger than themselves. B: Stokes settling speed (Eq. (22.10)) of a cyanobacterial cell (radius 2.5 µm) and of a colony (radius 50 µm) against the volume fraction of gas vesicles (effective density about 120 kg/m³, cytoplasm 1050 kg/m³): about 5.6 % makes the cells neutrally buoyant (dotted); negative speeds mean floating. Colonies move four hundred times faster than single cells](./plots/sedimentation.py)

## 22.7. Viscoelastic Media

### 22.7.1. Springs and Dashpots

Many of the media in which cells live and move are neither solids nor Newtonian liquids. Mucus, biofilm matrix, the cytoplasm on the scale of organelles, the actin cortex and the extracellular matrix resist deformation elastically on short time scales and flow on long ones.

**Definition 22.7.1 (Viscoelasticity)** A material is **viscoelastic** when its stress depends both on its strain and on its rate of strain, so that its response to a deformation depends on time. Linear viscoelasticity is characterized, for oscillatory strain $\varepsilon = \varepsilon_0\mathrm{e}^{\mathrm{i}\omega t}$, by the complex modulus $G^*(\omega) = \sigma/\varepsilon = G'(\omega) + \mathrm{i}G''(\omega)$, where the storage modulus $G'$ measures the elastic energy stored and the loss modulus $G''$ the energy dissipated per cycle.

The simplest models combine an elastic spring of modulus $E$ (stress $E\varepsilon$, compare **Young's modulus**, [5.1.7](/5.1.7)) with a viscous dashpot of viscosity $\eta$ (stress $\eta\dot\varepsilon$), with relaxation time $\tau = \eta/E$:

| Model | Elements | Constitutive equation | Response to a step stress | $G^*(\omega)$ |
|---|---|---|---|---|
| Voigt (Kelvin–Voigt) solid | spring and dashpot in parallel | $\sigma = E\varepsilon + \eta\dot\varepsilon$ | creeps to $\sigma_0/E$, recovers fully | $E + \mathrm{i}\omega\eta$ |
| **Maxwell viscoelastic liquid** ([7.5.8](/7.5.8#def-8.1.1)) | in series | $\dot\varepsilon = \dot\sigma/E + \sigma/\eta$ | jumps to $\sigma_0/E$, then flows at $\sigma_0/\eta$ | $E\,\dfrac{\mathrm{i}\omega\tau}{1 + \mathrm{i}\omega\tau}$ |
| Standard linear solid | spring $E_1$ in series with a Voigt element $(E_2, \eta)$ | $\sigma + \dfrac{\eta}{E_1 + E_2}\dot\sigma = \dfrac{E_1E_2}{E_1 + E_2}\varepsilon + \dfrac{E_1\eta}{E_1 + E_2}\dot\varepsilon$ | jumps to $\sigma_0/E_1$, relaxes to $\sigma_0(E_1 + E_2)/E_1E_2$ | |

A Maxwell material is elastic for processes faster than $\tau$ ($G' > G''$ for $\omega\tau > 1$) and liquid for slower ones. Its storage and loss moduli, $G' = E\omega^2\tau^2/(1 + \omega^2\tau^2)$ and $G'' = E\omega\tau/(1 + \omega^2\tau^2)$, cross at $\omega = 1/\tau$.

![Linear viscoelastic models (relaxation time τ = η/E). A: creep and recovery after a stress σ₀ is applied at t = 0 and removed at t = 3τ (shaded): the Voigt solid creeps towards σ₀/E and recovers completely, the Maxwell liquid responds elastically and then flows without limit, keeping the flowed strain, and the standard linear solid (E₁ = E₂ = E) jumps to σ₀/2E and relaxes to σ₀/E. B: storage and loss moduli of a Maxwell liquid in oscillatory shear: elastic above the crossover frequency 1/τ, viscous below. C: the weak power law G*(ω) ∝ (iω)^0.2 typical of living cells, with G' ≈ 3G'' over five decades: no single relaxation time](./plots/viscoelastic.py)

### 22.7.2. The Rheology of Cells

Measured by twisting magnetic beads bound to the cortex, by atomic force microscopy or by tracking particles in the cytoplasm, the moduli of living cells are of the order of $10^2$–$10^4\,\mathrm{Pa}$ at $1\,\mathrm{Hz}$ and depend on frequency as a weak power law, $G^* \propto (\mathrm{i}\omega)^\beta$ with $\beta = 0.1$–$0.3$, over many decades (Fabry and colleagues 2001). A power law has no characteristic time: the cytoskeleton behaves like a soft glassy material with a broad distribution of relaxation times, from the turnover of crosslinks and filaments to the remodeling of the network by motors. The exponent increases when myosin is activated and decreases when it is inhibited; active stresses fluidize the network. The passive and active fluctuations that coexist in this medium, and the transport of particles through it, are the subject of [7.6.23](/7.6.23); the mechanics of whole cells and their sensing of stiffness are in [7.6.31](/7.6.31).

Swimming in viscoelastic fluids differs from swimming in water. Bacteria such as *Leptospira* and *Helicobacter pylori* swim faster in polymer solutions and mucus than in water, and the elastic stresses of the fluid can rectify reciprocal strokes into net motion, evading the scallop theorem (Theorem 22.5.1). *H. pylori* additionally liquefies the gastric mucus around itself by raising the local pH with urease, and the gel–sol transition of the mucin network lets it through.

## Summary

| Topic | Key result | Reference |
|---|---|---|
| Continuum mechanics | acceleration $\mathrm{D}\boldsymbol{u}/\mathrm{D}t = \partial_t\boldsymbol{u} + (\boldsymbol{u}\cdot\nabla)\boldsymbol{u}$; incompressibility $\nabla\cdot\boldsymbol{u} = 0$; Newtonian stress $-p\delta_{ij} + \eta(\partial_iu_j + \partial_ju_i)$ | Eq. (22.1), Eq. (22.2), Definition 22.1.1 |
| Navier–Stokes | $\rho\,\mathrm{D}\boldsymbol{u}/\mathrm{D}t = -\nabla p + \eta\nabla^2\boldsymbol{u} + \boldsymbol{f}$ with no slip at walls | Definition 22.1.2, Definition 22.1.3 |
| Pipe flow | $Q = \pi\Delta p\,d^4/128\eta l$; capillary blood flow about $1\,\mathrm{mm\,s^{-1}}$ | Formula 22.2.1, Example 22.2.1 |
| Leukocyte rolling | wall drag $\approx 32a^2\tau_{\mathrm{w}} \approx 100\,\mathrm{pN}$, held by a few selectin bonds | Example 22.2.2 |
| Reynolds number | $\operatorname{Re} = \rho UL/\eta$: $10^{-5}$ for bacteria, $10^7$ for whales; overdamped motion $\gamma\dot x = F$, coasting $< 0.01\,\mathrm{nm}$ | Definition 22.3.1, Example 22.3.2 |
| Stokes flow | instantaneous, linear, reversible; Stokes' law $6\pi\eta aU$; $a/r$ wake | Proposition 22.4.1, Theorem 22.4.2 |
| Slender bodies | drag $\propto \eta L/\ln(L/b)$, $\gamma_\perp \approx 2\gamma_\parallel$ | Formula 22.4.1 |
| Drag in experiments | negligible on a bead pulled by a motor; the whole load on F₁'s actin filament ($40\,\mathrm{pN\,nm}$) | Example 22.4.1, Example 22.4.2 |
| Scallop theorem | reciprocal strokes produce no net motion; displacement $\propto$ area of the stroke in shape space | Theorem 22.5.1, Algorithm 22.5.1 |
| Flagella | thrust $\propto(\gamma_\perp - \gamma_\parallel)\sin\theta\cos\theta$; *E. coli* about $25\,\mu\mathrm{m\,s^{-1}}$, efficiency $\approx 2\,\%$; bending waves $U \approx \frac12(kb)^2\omega/k$ | Formula 22.5.1, Eq. (22.9) |
| Flagellar motor | torque plateau $\approx 1300\,\mathrm{pN\,nm}$, knee $170\,\mathrm{Hz}$, zero torque $300\,\mathrm{Hz}$; swimming costs a few percent of the cell's ATP budget | Example 22.5.2 |
| Why swim | stirring does not help ($\mathrm{Pe} \ll 1$); outrunning diffusion needs $\ell > 2D/U \approx 70\,\mu\mathrm{m}$ | 22.5.6 |
| Sedimentation | $v = 2\Delta\rho g a^2/9\eta$; separation time; gravity matters above $a \approx 1\,\mu\mathrm{m}$; gas vesicles | Eq. (22.10), Formula 22.6.1 |
| Viscoelasticity | Voigt, Maxwell and standard linear models; $G' + \mathrm{i}G''$; cells $G^* \propto (\mathrm{i}\omega)^{0.1\text{–}0.3}$ | Definition 22.7.1 |

## Questions

1. A spermatozoon and a sea urchin larva of $300\,\mu\mathrm{m}$ swimming at $1\,\mathrm{mm\,s^{-1}}$: compute their Reynolds numbers. If the larva stops beating its cilia, how far does it coast?

   **Answer** Sperm: $L = 50\,\mu\mathrm{m}$, $U = 60\,\mu\mathrm{m\,s^{-1}}$: $\operatorname{Re} = 6\times10^{-5} \times 5\times10^{-5}/10^{-6} = 3\times10^{-3}$. Larva: $\operatorname{Re} = 10^{-3} \times 3\times10^{-4}/10^{-6} = 0.3$. Treating the larva as a sphere of radius $a = 150\,\mu\mathrm{m}$ with Stokes drag, $\tau = 2\rho a^2/9\eta = 2 \times 10^3 \times (1.5\times10^{-4})^2/(9\times10^{-3})\,\mathrm{s} = 5\,\mathrm{ms}$ and the coasting distance is $U\tau = 5\,\mu\mathrm{m}$, a sixtieth of its length. At $\operatorname{Re} = 0.3$ inertia is still a correction, not negligible; such larvae live at the edge of the viscous world.

2. A red blood cell passes a capillary of $6\,\mu\mathrm{m}$ diameter and $0.8\,\mathrm{mm}$ length. If the arterioles feeding a capillary bed dilate by $15\,\%$ while the pressure drop across them stays the same, by what factor does their flow change? Why is the distribution of blood controlled at the arterioles rather than the capillaries?

   **Answer** By Formula 22.2.1, $Q \propto d^4$: $1.15^4 = 1.75$, a $75\,\%$ increase. Arterioles have smooth muscle and contribute the largest share of the resistance of the circulation (resistance $\propto l/d^4$ per vessel, and their number is small compared with the capillaries in parallel), so changes in their diameter change the flow into a capillary bed most strongly. Capillaries have no muscle, and their large number in parallel makes their collective resistance smaller than that of the arterioles. The transit time of the red cell through the capillary at $\bar u \approx 0.9\,\mathrm{mm\,s^{-1}}$ is about $1\,\mathrm{s}$, long enough for oxygen to equilibrate.

3. Using only dimensional analysis, show that the drag on a body at very large Reynolds number, where viscosity no longer matters, scales as $\rho U^2L^2$. Two paper cones, one twice the size of the other, are dropped; which reaches the higher terminal speed?

   **Answer** Without $\eta$, the only force built from $\rho$, $U$ and $L$ is $C\rho U^2L^2$. A paper cone of size $L$ has a weight proportional to its area, $\propto L^2$ (the thickness of the paper is fixed). Balancing $C\rho U^2L^2$ against $\propto L^2$ gives a terminal speed independent of size: both fall at the same speed (in practice they land together). At low Reynolds number the drag is $\propto\eta UL$ and the terminal speed would be $\propto L$: the larger cone would fall twice as fast.

4. A swimmer consists of two spheres joined by a rod whose length it can change (a "dumbbell"). Can it swim at low Reynolds number? What if it has three spheres joined by two rods whose lengths it changes in turn?

   **Answer** The dumbbell has one shape variable, the length, so any stroke is reciprocal and the scallop theorem (Theorem 22.5.1) forbids net motion. The three-sphere swimmer (Najafi and Golestanian 2004) has two shape variables. Changing them in the sequence: shorten the first rod, shorten the second, lengthen the first, lengthen the second, traces a loop of nonzero area in shape space, and the swimmer advances. The net motion arises from the hydrodynamic interaction between the spheres (the $a/r$ flow of Theorem 22.4.2), which makes the drag on each sphere depend on the distances to the others; without it, the swimmer would not move.

5. Show that the magnitude of the propulsive force of a rotating helix (first term of Formula 22.5.1) is maximal at $\theta = 45^\circ$. If the cell body were much larger, so that $\zeta_{\mathrm{b}}$ dominates the denominator of Eq. (22.8), how would the swimming speed depend on the viscosity of the medium if the motor runs at constant torque?

   **Answer** The thrust is proportional to $\sin\theta\cos\theta = \frac12\sin2\theta$, maximal at $\theta = 45^\circ$. At constant torque $\tau_{\mathrm{m}}$, the rotation rate is set by the rotational drag of the helix, $\omega = \tau_{\mathrm{m}}/\zeta_{\mathrm{r}}$, with $\zeta_{\mathrm{r}} \propto \eta$; so $\omega \propto 1/\eta$. With $\zeta_{\mathrm{b}} \propto \eta$ dominant, $U \propto (\gamma_\perp - \gamma_\parallel)\omega/\zeta_{\mathrm{b}} \propto \eta\cdot\eta^{-1}\cdot\eta^{-1} = \eta^{-1}$. Doubling the viscosity halves the speed, and the power $\tau_{\mathrm{m}}\omega$ also halves. If instead the motor ran at constant speed (as in the steep region of the torque–speed curve), the speed would be independent of viscosity and the power would double.

6. In Example 22.4.2, an actin filament of $2\,\mu\mathrm{m}$ is attached to F₁ instead of $1\,\mu\mathrm{m}$. Predict its rotation rate, and explain how plotting rotation rate against filament length tests whether the torque is constant.

   **Answer** $\zeta \propto L^3/[\ln(L/2b) - 0.45]$: for $L = 2\,\mu\mathrm{m}$, $\ln(250) - 0.45 = 5.07$ against $\ln(125) - 0.45 = 4.38$, so $\zeta$ increases by $8 \times 4.38/5.07 = 6.9$ and the rate falls from $6$ to about $0.9$ revolutions per second. If the torque is independent of load, $\omega\zeta$ is constant: a plot of $\omega$ against $1/\zeta(L)$ is a straight line through the origin with slope equal to the torque, as observed for F₁ (about $40\,\mathrm{pN\,nm}$). Deviations at short filaments, where the motor would run fast, reveal its kinetic limit (the motor's own torque–speed curve).

7. Estimate the time needed to separate, by rate-zonal centrifugation at $g_{\mathrm{c}} = 10^5g$, two globular proteins of the same density ($1.35\,\mathrm{g\,cm^{-3}}$) with diameters of $4$ and $5\,\mathrm{nm}$, and check whether they separate before reaching the bottom of a $1\,\mathrm{cm}$ tube.

   **Answer** Eq. (22.10) with $\Delta\rho = 350\,\mathrm{kg\,m^{-3}}$, $\eta = 10^{-3}\,\mathrm{Pa\,s}$, $g_{\mathrm{c}} = 9.8\times10^5\,\mathrm{m\,s^{-2}}$: $v = 2 \times 350 \times 9.8\times10^5a^2/(9\times10^{-3}) = 7.6\times10^{10}a^2$; $a = 2\,\mathrm{nm}$: $v_2 = 3.0\times10^{-7}\,\mathrm{m\,s^{-1}}$; $a = 2.5\,\mathrm{nm}$: $v_1 = 4.8\times10^{-7}\,\mathrm{m\,s^{-1}}$. Stokes–Einstein: $D_2 = 1.1\times10^{-10}$, $D_1 = 8.7\times10^{-11}\,\mathrm{m^2\,s^{-1}}$. Formula 22.6.1: $t_{\mathrm{sep}} = (\sqrt{2.2\times10^{-10}} + \sqrt{1.75\times10^{-10}})^2/(1.8\times10^{-7})^2 = (1.48\times10^{-5} + 1.32\times10^{-5})^2/(1.7\times10^{-7})^2\,\mathrm{s} = 2.7\times10^4\,\mathrm{s}$, about $7.5\,\mathrm{h}$. In that time the faster band travels $4.8\times10^{-7} \times 2.7\times10^4 = 1.3\,\mathrm{cm}$, beyond the end of the tube: the separation fails at this speed and needs a larger $g_{\mathrm{c}}$ (by Formula 22.6.1, $v_1t_{\mathrm{sep}} \propto 1/g_{\mathrm{c}}$, so $1.5\times10^5g$ suffices) or a longer tube. Real separations of proteins this close in size use other methods.

8. (Experimental design) You suspect that a ciliate swims more slowly in a solution of a high-molecular-weight polymer because the polymer makes the medium viscoelastic, not just more viscous. Design an experiment to distinguish the two possibilities.

   **Answer** Prepare two media with the same zero-shear viscosity: one with a small, Newtonian thickener (Ficoll or a sugar at suitable concentration) and one with the long polymer (polyacrylamide or polyethylene oxide), and characterize both by oscillatory rheology ($G'$, $G''$ at the beat frequency of the cilia, about $20$–$30\,\mathrm{Hz}$) to confirm that only the second has an appreciable $G'$ and a relaxation time comparable to the beat period. Measure swimming speed, beat frequency and waveform (high-speed video) in both. If the cell's speed in the two media is the same when their viscosities match, viscosity alone explains the slowing; if the speeds differ, the elasticity matters, and the dimensionless Deborah number (relaxation time times beat frequency) should predict the effect when the polymer concentration or molecular weight is varied.

9. (Open question) Why are there no swimming organisms of intermediate size, around $\operatorname{Re} \approx 1$, that use reciprocal strokes? Discuss what happens to the scallop theorem as the Reynolds number increases from $10^{-3}$ to $10$.

   **Answer** The scallop theorem holds exactly only at $\operatorname{Re} = 0$; at small but finite $\operatorname{Re}$ a reciprocal stroke produces net motion only at order $\operatorname{Re}$, and the swimming speed of a reciprocal swimmer, starting from zero, becomes appreciable only around $\operatorname{Re} \approx 1$–$10$ (theoretical and robotic studies of flapping bodies show a transition to forward flight near $\operatorname{Re} \approx 10$–$100$). Small organisms therefore must use nonreciprocal strokes, and do (rotating helices, traveling waves, asymmetric ciliary beats). Organisms near $\operatorname{Re} \approx 1$, such as copepod nauplii and the smallest insects that fly (thrips, with bristled wings), use both: strokes asymmetric in shape and inertial effects such as the unsteady flow created by rapid flicks. The intermediate regime is hard for swimmers because neither viscous nor inertial mechanisms work efficiently, and it is crossed rapidly during the growth of many larvae.

10. A cyanobacterial colony of radius $50\,\mu\mathrm{m}$ with $3\,\%$ of its volume in gas vesicles, and an excess carbohydrate ballast that adds $20\,\mathrm{kg\,m^{-3}}$ to the density of its cytoplasm after a day of photosynthesis: does it sink or float, and how fast?

    **Answer** Cytoplasm $1050 + 20 = 1070\,\mathrm{kg\,m^{-3}}$; colony density $0.97 \times 1070 + 0.03 \times 120 = 1041.5\,\mathrm{kg\,m^{-3}}$, $\Delta\rho = 43.5\,\mathrm{kg\,m^{-3}}$ above water. It sinks at $v = 2 \times 43.5 \times 9.8 \times (5\times10^{-5})^2/(9\times10^{-3})\,\mathrm{m\,s^{-1}} = 2.4\times10^{-4}\,\mathrm{m\,s^{-1}}$, about $0.9\,\mathrm{m\,h^{-1}}$. Overnight the carbohydrate is respired and new vesicles are made, and the colony rises again: a daily vertical migration of meters, possible only for colonies, because single cells move four hundred times slower ($\propto a^2$).
