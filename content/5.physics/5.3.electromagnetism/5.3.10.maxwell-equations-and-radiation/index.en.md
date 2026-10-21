---
title: Maxwell's Equations and Electromagnetic Radiation
description: The displacement current and the symmetry of the electromagnetic field; Maxwell's equations in integral form, differential form and as boundary conditions; the electromagnetic wave equation, properties of plane electromagnetic waves, energy density, the Poynting vector and Poynting's theorem, momentum and radiation pressure; radiation from an oscillating electric dipole; light as an electromagnetic wave.
source_hash: aab28d607aab
---

This chapter is a summary of electromagnetism. The previous nine chapters established, one by one, the electrostatic **Gauss's law** and circulation theorem ([5.3.1](/5.3.1), [5.3.2](/5.3.2)), $\boldsymbol{D}$ and $\boldsymbol{H}$ in media ([5.3.4](/5.3.4), [5.3.8](/5.3.8)), the flux and circulation theorems of the magnetic field ([5.3.6](/5.3.6)), and the law of **electromagnetic induction** ([5.3.9](/5.3.9)). In 1865 Maxwell generalized them to time-dependent situations, supplied the crucial displacement-current term, and wrote them as one complete set of equations. These equations show that a changing electric field and a changing magnetic field excite each other and can propagate as a wave, detached from charges and currents, with a speed exactly equal to the speed of light. Electricity, magnetism and light are thereby unified in a single theory. This chapter first reviews the displacement current and writes Maxwell's equations in integral and differential form (using the **divergence**, the **curl**, the **divergence theorem** and **Stokes' theorem** of [2.2.14](/2.2.14)); it then derives from them the **wave equation** ([2.5.3](/2.5.3)), discusses the properties, energy and momentum of plane electromagnetic waves, and finally discusses how an oscillating electric dipole radiates electromagnetic waves. The general concepts of a **mechanical wave** are given in [5.1.7](/5.1.7); the conclusion of this chapter, "light is an electromagnetic wave", is the starting point of wave optics ([5.4](/5.4)).

## 10.1. Displacement Current

[5.3.6](/5.3.6) showed that Ampère's circuital law for **steady currents** leads to a contradiction when applied to nonsteady situations such as the charging and discharging of a **capacitor**: of two surfaces bounded by the same loop, one pierced by the wire and one passing between the two plates of the capacitor, the currents computed are different. Maxwell's solution was to introduce the **displacement current**: the rate of change of the **electric displacement field** flux, $I_{\mathrm{d}}=\frac{\mathrm{d}\Phi_D}{\mathrm{d}t}$, that is, the displacement current density

$$
\boldsymbol{J}_{\mathrm{d}}=\frac{\partial\boldsymbol{D}}{\partial t}=\varepsilon_0\frac{\partial\boldsymbol{E}}{\partial t}+\frac{\partial\boldsymbol{P}}{\partial t}.
$$
In the capacitor example the conduction current in the wire is $I_0=\frac{\mathrm{d}q_0}{\mathrm{d}t}$, and by Gauss's law for $\boldsymbol{D}$ the displacement current between the plates, $\iint\frac{\partial\boldsymbol{D}}{\partial t}\cdot\mathrm{d}\boldsymbol{S}=\frac{\mathrm{d}q_0}{\mathrm{d}t}$, is equal to it, so the **total current**, the sum of conduction current and displacement current, is continuous everywhere. The displacement current excites a magnetic field just as the conduction current does, but in essence it is a changing electric field (the second term $\partial\boldsymbol{P}/\partial t$ corresponds to the small displacements of **bound charge** in the medium); it involves no directed motion of free charge and produces no Joule heat. Displacement current exists wherever the electric field changes, not only inside capacitors, and at one point conduction current and displacement current may be present together.

With the displacement current introduced, the laws of the electric and magnetic fields display a symmetry. In a region without conduction current,

$$
\oint_L\boldsymbol{E}\cdot\mathrm{d}\boldsymbol{l}=-\iint_S\frac{\partial\boldsymbol{B}}{\partial t}\cdot\mathrm{d}\boldsymbol{S},\qquad \oint_L\boldsymbol{H}\cdot\mathrm{d}\boldsymbol{l}=\iint_S\frac{\partial\boldsymbol{D}}{\partial t}\cdot\mathrm{d}\boldsymbol{S}:
$$
a changing magnetic field excites an **induced electric field**, and a changing electric field excites a vortex magnetic field. The two equations differ by a minus sign, which is required by energy conservation: if the two had the same sign, a strengthening magnetic field would produce an induction that strengthens the electric field, and the strengthening electric field would in turn produce an induction that strengthens the magnetic field, so that energy would grow out of nothing.

## 10.2. Maxwell's Equations

### 10.2.1. Integral Form

Suppose that in space there are free charges and conduction currents, changing electric and magnetic fields, and also **dielectrics** and **magnetic materials**. Combining the **circulation theorem for the electrostatic field** with the circulation theorem for the **induced electric field** (the total electric field is the sum of the two), extending Gauss's law for $\boldsymbol{D}$ and **Gauss's law for magnetism** to changing fields, and supplementing the circulation theorem for $\boldsymbol{H}$ with the displacement current, we obtain the fundamental equations of the electromagnetic field.

**Theorem 10.2.1 (Maxwell's Equations)** For any closed surface $S$ (enclosing the volume $V$) and any closed circuit $L$ (bounding the surface $S$, whose normal is related to $L$ by the right-hand rule),

$$
\begin{aligned}
&\oiint_S\boldsymbol{D}\cdot\mathrm{d}\boldsymbol{S}=\iiint_V\rho_0\,\mathrm{d}V, &&\text{(1)}\\
&\oint_L\boldsymbol{E}\cdot\mathrm{d}\boldsymbol{l}=-\iint_S\frac{\partial\boldsymbol{B}}{\partial t}\cdot\mathrm{d}\boldsymbol{S}, &&\text{(2)}\\
&\oiint_S\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{S}=0, &&\text{(3)}\\
&\oint_L\boldsymbol{H}\cdot\mathrm{d}\boldsymbol{l}=\iint_S\Big(\boldsymbol{J}_0+\frac{\partial\boldsymbol{D}}{\partial t}\Big)\cdot\mathrm{d}\boldsymbol{S}. &&\text{(4)}
\end{aligned}
$$
Here $\rho_0$ and $\boldsymbol{J}_0$ are the free **charge density** and the conduction **current density**.

The four equations are, in turn: Gauss's law for the electric field (charge is the source of the electric field), **Faraday's law of induction** (a changing magnetic field excites an electric field), Gauss's law for magnetism (there is no magnetic charge, and **magnetic field lines** close on themselves), and Ampère's circuital law with the total current (current and a changing electric field excite a magnetic field). The equations are not completely symmetric between the electric and magnetic fields because no isolated magnetic charge, and hence no corresponding "magnetic current", has been found in nature.

The equations must be supplemented by constitutive relations describing the properties of the medium. For an isotropic linear medium,

$$
\boldsymbol{D}=\varepsilon\boldsymbol{E},\qquad\boldsymbol{B}=\mu\boldsymbol{H},\qquad\boldsymbol{J}_0=\sigma\boldsymbol{E},
$$
and by the action of the electromagnetic field on charge, namely the **Lorentz force** law $\boldsymbol{F}=q\boldsymbol{E}+q\boldsymbol{v}\times\boldsymbol{B}$ of [5.3.7](/5.3.7#sec-7.2). Maxwell's equations, the constitutive relations and the Lorentz force law form the complete foundation of classical electrodynamics and have been confirmed by a vast number of experiments in the macroscopic domain. In the microscopic domain the electromagnetic field itself must be quantized, and the corresponding theory is quantum electrodynamics, whose predictions (such as the deviation of the electron $g$-factor from 2, [5.3.8](/5.3.8)) agree with experiment to a precision of $10^{-12}$.

**Example 10.2.1 (Deriving Charge Conservation from Maxwell's Equations)** Take an arbitrary closed surface $S$ and divide it into two parts $S_1$ and $S_2$ by a closed curve $L$. Apply equation (4) to $S_1$ and $S_2$ separately; if both normals are taken as the outward normal of $S$, the senses of traversal of their common boundary $L$ are opposite, and the sum of the two circulations is zero, so

$$
\oiint_S\Big(\boldsymbol{J}_0+\frac{\partial\boldsymbol{D}}{\partial t}\Big)\cdot\mathrm{d}\boldsymbol{S}=0\quad\Longrightarrow\quad\oiint_S\boldsymbol{J}_0\cdot\mathrm{d}\boldsymbol{S}=-\frac{\mathrm{d}}{\mathrm{d}t}\oiint_S\boldsymbol{D}\cdot\mathrm{d}\boldsymbol{S}=-\frac{\mathrm{d}}{\mathrm{d}t}\iiint_V\rho_0\,\mathrm{d}V,
$$
where the last step used equation (1). This is exactly the integral form of the **law of conservation of charge** (the **charge continuity equation** of [5.3.5](/5.3.5)): the current flowing out of a closed surface equals the rate of decrease of the charge inside. Without the displacement-current term, equation (4) would contradict charge conservation, which was the theoretical ground for Maxwell's introduction of the displacement current.

### 10.2.2. Differential Form

Apply **Stokes' theorem** to equations (2) and (4) and the **divergence theorem** to (1) and (3) ([2.2.14](/2.2.14#sec-14.2.1), [2.2.14](/2.2.14#sec-14.3.1)); since the surfaces and volumes are arbitrary, the integrands must be equal:

**Theorem 10.2.2 (Maxwell's Equations in Differential Form)**

$$
\nabla\cdot\boldsymbol{D}=\rho_0,\qquad\nabla\times\boldsymbol{E}=-\frac{\partial\boldsymbol{B}}{\partial t},\qquad\nabla\cdot\boldsymbol{B}=0,\qquad\nabla\times\boldsymbol{H}=\boldsymbol{J}_0+\frac{\partial\boldsymbol{D}}{\partial t}.
$$

The differential form describes the relation at each point between the field, the sources at that point and the rate of change of the field at that point, and is a system of first-order linear partial differential equations. Taking the divergence of the fourth equation, with $\nabla\cdot(\nabla\times\boldsymbol{H})=0$ ([2.2.14](/2.2.14#sec-14.1.4)) and the first equation, immediately gives the continuity equation $\nabla\cdot\boldsymbol{J}_0+\partial\rho_0/\partial t=0$, which is the differential form of Example 10.2.1.

### 10.2.3. Boundary Conditions

At the interface between two media the fields may be discontinuous and the differential form does not hold, so boundary conditions must be derived from the integral form (the derivation is the same as in [5.3.4](/5.3.4) and [5.3.8](/5.3.8): take a flat cylindrical surface and a flat rectangular loop straddling the interface and let their thickness tend to zero; $\partial\boldsymbol{B}/\partial t$ and $\partial\boldsymbol{D}/\partial t$ are finite, so their contributions tend to zero). Let $\boldsymbol{e}_{\mathrm{n}}$ be the unit normal vector pointing from medium 2 into medium 1, and $\sigma_0$ and $\boldsymbol{K}_0$ the free surface charge density and conduction surface current density on the interface:

$$
\boldsymbol{e}_{\mathrm{n}}\cdot(\boldsymbol{D}_1-\boldsymbol{D}_2)=\sigma_0,\qquad\boldsymbol{e}_{\mathrm{n}}\times(\boldsymbol{E}_1-\boldsymbol{E}_2)=\boldsymbol{0},\qquad\boldsymbol{e}_{\mathrm{n}}\cdot(\boldsymbol{B}_1-\boldsymbol{B}_2)=0,\qquad\boldsymbol{e}_{\mathrm{n}}\times(\boldsymbol{H}_1-\boldsymbol{H}_2)=\boldsymbol{K}_0.
$$
That is, $D_{1n}-D_{2n}=\sigma_0$, $E_{1t}=E_{2t}$, $B_{1n}=B_{2n}$, and the tangential component of $\boldsymbol{H}$ jumps by $\boldsymbol{K}_0$ (it is continuous when $\boldsymbol{K}_0=\boldsymbol{0}$). The differential equations together with the boundary conditions form a complete system: given initial and boundary conditions, the electromagnetic field is uniquely determined.

## 10.3. Electromagnetic Waves

### 10.3.1. The Electromagnetic Wave Equation

Consider a region of an infinite homogeneous, isotropic, linear medium without free charge or conduction current ($\rho_0=0$, $\boldsymbol{J}_0=\boldsymbol{0}$). With the constitutive relations, Maxwell's equations become

$$
\nabla\times\boldsymbol{E}=-\mu\frac{\partial\boldsymbol{H}}{\partial t},\qquad\nabla\times\boldsymbol{H}=\varepsilon\frac{\partial\boldsymbol{E}}{\partial t},\qquad\nabla\cdot\boldsymbol{E}=0,\qquad\nabla\cdot\boldsymbol{H}=0,
$$
and $\boldsymbol{E}$ and $\boldsymbol{H}$ play completely symmetric roles. Take the **curl** of the first equation, use the vector identity $\nabla\times(\nabla\times\boldsymbol{A})=\nabla(\nabla\cdot\boldsymbol{A})-\Delta\boldsymbol{A}$ ($\Delta$ is the **Laplace operator**, acting on each Cartesian component) and $\nabla\cdot\boldsymbol{E}=0$, and substitute the second equation:

$$
-\Delta\boldsymbol{E}=-\mu\frac{\partial}{\partial t}(\nabla\times\boldsymbol{H})=-\varepsilon\mu\frac{\partial^2\boldsymbol{E}}{\partial t^2}.
$$
The same holds for $\boldsymbol{H}$.

**Theorem 10.3.1 (Electromagnetic Wave Equation)** In a source-free homogeneous linear medium, every Cartesian component of $\boldsymbol{E}$ and $\boldsymbol{H}$ satisfies the three-dimensional **wave equation**

$$
\Delta\boldsymbol{E}=\frac{1}{u^2}\frac{\partial^2\boldsymbol{E}}{\partial t^2},\qquad\Delta\boldsymbol{H}=\frac{1}{u^2}\frac{\partial^2\boldsymbol{H}}{\partial t^2},\qquad u=\frac{1}{\sqrt{\varepsilon\mu}}.
$$

The electromagnetic field can therefore propagate as a wave, called an *electromagnetic wave*, with wave speed $u=1/\sqrt{\varepsilon\mu}$. The wave speed in vacuum is

$$
c=\frac{1}{\sqrt{\varepsilon_0\mu_0}}=299\,792\,458\,\mathrm{m/s}
$$
(the defined value in the SI). The wave speed that Maxwell computed from the values of $\varepsilon_0\mu_0$ obtained from electrical measurements at the time agreed with the speed of light measured by Fizeau and others; from this he predicted electromagnetic waves in 1865 and asserted that light is an electromagnetic wave. In 1886–1888 Hertz produced and detected electromagnetic waves experimentally (Section 10.4), confirming the prediction.

The ratio of the speed of light in vacuum to the wave speed in a medium is called the *refractive index* of the medium. From the wave-speed formula,

$$
n=\frac cu=\sqrt{\varepsilon_{\mathrm{r}}\mu_{\mathrm{r}}}\approx\sqrt{\varepsilon_{\mathrm{r}}}\qquad(\text{nonferromagnetic},\ \mu_{\mathrm{r}}\approx1).
$$
In optics one usually takes $n=c/u$ directly as the definition of the refractive index (it is also the origin of the ratio of the wave speeds of two media in the **law of refraction** of [5.1.7](/5.1.7)), while $n=\sqrt{\varepsilon_{\mathrm{r}}\mu_{\mathrm{r}}}$ connects this optical constant with electrical constants. The $\varepsilon_{\mathrm{r}}$ here must be taken at the corresponding frequency: the static **relative permittivity** of water is about 80 and $\sqrt{80}\approx9$, whereas the refractive index of visible light is only 1.33, because the **orientation polarization** of the molecules cannot follow the change at optical frequencies. The variation of $\varepsilon_{\mathrm{r}}$ with frequency is exactly the origin of **dispersion**.

The general theory of the wave equation is given in [2.5.3](/2.5.3): in three dimensions Kirchhoff's formula shows that a signal propagates with speed $u$ and keeps a sharp front (the strong form of **Huygens' principle** holds only in spaces of odd dimension).

### 10.3.2. Plane Electromagnetic Waves

The simplest solutions of the wave equation are plane **harmonic waves** propagating along the $x$ direction. Electromagnetic waves are **transverse waves**: for a plane wave $\boldsymbol{E}=\boldsymbol{E}(x,t)$, $\nabla\cdot\boldsymbol{E}=\partial E_x/\partial x=0$, and the $x$ component of $\nabla\times\boldsymbol{H}=\varepsilon\partial\boldsymbol{E}/\partial t$ gives $\partial E_x/\partial t=0$, so there is no oscillating component along the direction of propagation; the same holds for $\boldsymbol{H}$. Take $\boldsymbol{E}$ along the $y$ direction,

$$
E_y=E_0\cos\omega\Big(t-\frac xu\Big),
$$
and from the $z$ component of $\nabla\times\boldsymbol{E}=-\mu\partial\boldsymbol{H}/\partial t$, $\frac{\partial E_y}{\partial x}=-\mu\frac{\partial H_z}{\partial t}$, integration gives

$$
H_z=\sqrt{\frac\varepsilon\mu}\,E_0\cos\omega\Big(t-\frac xu\Big),
$$
with $H_x=H_y=0$.

**Property 10.3.1 (Properties of Plane Electromagnetic Waves)**

1. Transverse wave: $\boldsymbol{E}\perp\boldsymbol{u}$, $\boldsymbol{H}\perp\boldsymbol{u}$, and $\boldsymbol{E}\perp\boldsymbol{H}$; $\boldsymbol{E}\times\boldsymbol{H}$ is along the direction of propagation, and the three form a right-handed system.
2. $\boldsymbol{E}$ and $\boldsymbol{H}$ are in phase, with a fixed ratio of amplitudes: $\sqrt\varepsilon\,E=\sqrt\mu\,H$, that is, $E=uB$, and $E=cB$ in vacuum.
3. The wave speed $u=1/\sqrt{\varepsilon\mu}$ is independent of frequency (when $\varepsilon$ and $\mu$ are independent of frequency).

An electromagnetic wave in which $\boldsymbol{E}$ oscillates in a fixed plane is called a linearly polarized wave; the case in which the direction of $\boldsymbol{E}$ rotates with time is treated in [5.4.3](/5.4.3).

![A linearly polarized plane electromagnetic wave propagating along the $x$ direction at one instant: $\boldsymbol{E}$ oscillates along the $y$ direction and $\boldsymbol{B}$ along the $z$ direction, the two are in phase, and $\boldsymbol{E}\times\boldsymbol{B}$ points in the direction of propagation (for ease of viewing, the amplitude of $B$ is drawn equal to that of $E$)](./plots/plane-wave.py)

Electromagnetic waves arranged by wavelength (or frequency) form the electromagnetic spectrum. The physical nature of all bands is the same and only the wavelengths differ, with correspondingly different methods of production and detection and different interactions with matter (the boundaries are conventional and approximate):

| Band | Wavelength range | Main sources and uses |
|---|---|---|
| Radio waves | $>1\,\mathrm{m}$ | oscillating currents in circuits; broadcasting, communication |
| Microwaves | $1\,\mathrm{mm}$–$1\,\mathrm{m}$ | radar, mobile communication, microwave ovens, the cosmic microwave background |
| Infrared | $760\,\mathrm{nm}$–$1\,\mathrm{mm}$ | molecular vibration and rotation, thermal radiation; infrared imaging and spectroscopy |
| Visible light | about $380$–$760\,\mathrm{nm}$ | transitions of outer electrons in atoms and molecules |
| Ultraviolet | $10$–$380\,\mathrm{nm}$ | atomic excitation; disinfection, photolithography |
| X-rays | $0.01$–$10\,\mathrm{nm}$ | inner-shell electron transitions, bremsstrahlung of fast electrons ([5.5.5](/5.5.5)); crystal diffraction ([5.4.2](/5.4.2)), medical imaging |
| $\gamma$-rays | $<0.01\,\mathrm{nm}$ | nuclear transitions, particle annihilation |

### 10.3.3. Energy of Electromagnetic Waves and the Poynting Vector

The energy density of the electromagnetic field is the sum of the **energy density of the electric field** and that of the magnetic field ([5.3.4](/5.3.4), [5.3.9](/5.3.9)):

$$
w=w_{\mathrm{e}}+w_{\mathrm{m}}=\frac12\boldsymbol{E}\cdot\boldsymbol{D}+\frac12\boldsymbol{B}\cdot\boldsymbol{H}=\frac12\varepsilon E^2+\frac12\mu H^2.
$$
For a plane electromagnetic wave $\sqrt\varepsilon E=\sqrt\mu H$, so $w_{\mathrm{e}}=w_{\mathrm{m}}$: the electric and magnetic fields each carry half of the energy, and $w=\varepsilon E^2=\sqrt{\varepsilon\mu}\,EH$. When an electromagnetic wave propagates, energy propagates with it. As for mechanical waves ([5.1.7](/5.1.7#sec-7.5.2)), the energy passing per unit time through a unit area perpendicular to the direction of propagation is called the **energy flux density**; its magnitude is $wu=\varepsilon E^2/\sqrt{\varepsilon\mu}=EH$, and its direction is the direction of propagation, that is, the direction of $\boldsymbol{E}\times\boldsymbol{H}$.

**Definition 10.3.1 (Poynting Vector)** The energy flux density vector of the electromagnetic field,

$$
\boldsymbol{S}=\boldsymbol{E}\times\boldsymbol{H}
$$
is called the **Poynting vector**, in $\mathrm{W/m^2}$.

$\boldsymbol{S}=\boldsymbol{E}\times\boldsymbol{H}$ holds not only for plane waves but is part of a general energy conservation relation:

**Theorem 10.3.2 (Poynting's Theorem)** In a linear medium, for the volume $V$ enclosed by any closed surface $S$,

$$
-\frac{\mathrm{d}}{\mathrm{d}t}\iiint_Vw\,\mathrm{d}V=\oiint_S\boldsymbol{S}\cdot\mathrm{d}\boldsymbol{S}+\iiint_V\boldsymbol{J}_0\cdot\boldsymbol{E}\,\mathrm{d}V.
$$
The rate of decrease of the electromagnetic energy in the volume equals the sum of the energy flowing out through the boundary and the power of the work done by the electromagnetic field on the charges in the volume (for a resistive **conductor**, the Joule heating power).

**Proof** By the vector identity $\nabla\cdot(\boldsymbol{E}\times\boldsymbol{H})=\boldsymbol{H}\cdot(\nabla\times\boldsymbol{E})-\boldsymbol{E}\cdot(\nabla\times\boldsymbol{H})$ and Maxwell's equations in differential form,

$$
\nabla\cdot\boldsymbol{S}=-\boldsymbol{H}\cdot\frac{\partial\boldsymbol{B}}{\partial t}-\boldsymbol{E}\cdot\frac{\partial\boldsymbol{D}}{\partial t}-\boldsymbol{E}\cdot\boldsymbol{J}_0=-\frac{\partial w}{\partial t}-\boldsymbol{J}_0\cdot\boldsymbol{E},
$$
where we used $\boldsymbol{H}\cdot\partial_t\boldsymbol{B}=\partial_t(\frac12\boldsymbol{B}\cdot\boldsymbol{H})$ and $\boldsymbol{E}\cdot\partial_t\boldsymbol{D}=\partial_t(\frac12\boldsymbol{E}\cdot\boldsymbol{D})$ in a linear medium. Integrating over $V$ and using the divergence theorem gives the result. $\square$

For a plane harmonic wave, the average of the energy flux density over one period is the **wave intensity**:

$$
I=\overline S=\frac12E_0H_0=\frac12\sqrt{\frac\varepsilon\mu}\,E_0^2,\qquad\text{in vacuum}\quad I=\frac12c\varepsilon_0E_0^2.
$$
The intensity is proportional to the square of the electric field amplitude. For example, the solar irradiance at the Earth's orbit is about $1361\,\mathrm{W/m^2}$, corresponding to an electric field amplitude $E_0=\sqrt{2I/(c\varepsilon_0)}\approx1.0\,\mathrm{kV/m}$ and a magnetic field amplitude $B_0=E_0/c\approx3.4\,\mu\mathrm{T}$, which is even smaller than the Earth's magnetic field (about $50\,\mu\mathrm{T}$).

**Example 10.3.1 (Where Does the Energy Dissipated in a Wire Come From?)** A cylindrical conductor of length $L$, radius $r$ and **electrical conductivity** $\sigma$ carries a steady current $I$. Find the flow of electromagnetic energy into it through its lateral surface.

**Solution** The electric field in the conductor is along the axis, $E=J/\sigma=\frac{I}{\sigma\pi r^2}$; the tangential electric field is continuous at the interface, so just outside the surface of the conductor there is the same axial electric field. The magnetic field at the surface follows from Ampère's circuital law, $H=\frac{I}{2\pi r}$, in the circumferential direction. $\boldsymbol{S}=\boldsymbol{E}\times\boldsymbol{H}$ points radially toward the axis, with magnitude $S=EH=\frac{I^2}{2\sigma\pi^2r^3}$. The total power flowing in through the lateral surface is

$$
2\pi rL\cdot S=\frac{I^2L}{\sigma\pi r^2}=I^2R,\qquad R=\frac{L}{\sigma\pi r^2},
$$
exactly equal to the Joule heating power in the conductor. The energy does not "flow" along the current inside the wire; it is delivered by the field from the space outside the wire. The same is true of ordinary transmission lines: besides the tangential component $E_t$, the electric field at the surface of a wire has a normal component $E_n$ produced by the charge on the wire, and $\boldsymbol{E}_n\times\boldsymbol{H}$ is parallel to the wires and carries energy from the **source of electromotive force** to the load through the space between the two wires, while $\boldsymbol{E}_t\times\boldsymbol{H}$ points radially inward and supplies the Joule loss of the wires. The role of the wires is to guide the flow of energy.

### 10.3.4. Momentum of Electromagnetic Waves and Radiation Pressure

Electromagnetic waves carry momentum as well as energy. By the **mass–energy equivalence** and the energy–momentum relation of the photon $p=E/c$ ([5.1.8](/5.1.8#sec-8.9.4)), the momentum density of an electromagnetic wave of energy density $w$ in vacuum has magnitude $w/c=S/c^2$ and points along the direction of propagation:

$$
\boldsymbol{g}=\frac{\boldsymbol{S}}{c^2}=\frac{\boldsymbol{E}\times\boldsymbol{H}}{c^2}.
$$
This can also be derived directly from Maxwell's equations and the Lorentz force (the electric field makes the charges in the body oscillate, and the Lorentz force of the magnetic field on the oscillating charges is along the direction of propagation). When an electromagnetic wave falls on a body, the transfer of momentum appears as a pressure, called *radiation pressure*, also light pressure for light. For an electromagnetic wave of intensity $I$ in vacuum incident perpendicularly on the surface of a body, the momentum incident per unit time per unit area is $gc=I/c$. If it is completely absorbed, the pressure is $p_{\mathrm{r}}=I/c$; if it is perfectly reflected, the change of momentum is doubled and $p_{\mathrm{r}}=2I/c$.

Radiation pressure is usually very small: sunlight at the Earth's orbit exerts a pressure of about $1361/(3\times10^8)\,\mathrm{Pa}\approx4.5\,\mu\mathrm{Pa}$ on a perfectly absorbing surface; even if the entire power of a $100\,\mathrm{W}$ bulb were counted as light, the intensity at a distance of $1\,\mathrm{m}$ would be only $100/(4\pi)\approx8\,\mathrm{W/m^2}$ and the light pressure about $3\times10^{-8}\,\mathrm{Pa}$. In 1899–1901 Lebedev, and Nichols and Hull, first measured light pressure with a torsion balance holding small light mirrors suspended in vacuum.

Effects of radiation pressure: the dust tail of a comet is pushed away by the radiation pressure of sunlight and always extends away from the Sun (the ion tail is pushed mainly by the solar wind and is straighter); in the interior of massive stars, radiation pressure together with gas pressure resists gravity, and it limits the maximum luminosity of a star (the Eddington limit), while stars like the Sun are supported mainly by gas pressure; solar sails use light pressure for propulsion (IKAROS of Japan, 2010); the radiation pressure of lasers can trap and manipulate microscopic particles (optical tweezers, Ashkin, Nobel Prize in Physics 2018) and is also used in the laser cooling of atoms.

## 10.4. Electromagnetic Radiation

### 10.4.1. Production of Electromagnetic Waves and Hertz's Experiment

Producing electromagnetic waves requires changing currents and charges. The LC circuit of [5.3.9](/5.3.9) oscillates with angular frequency $\omega_0=1/\sqrt{LC}$, but the electric field is concentrated in the capacitor and the magnetic field in the coil, so little energy is radiated outward. To radiate effectively one must first raise the frequency (the radiated power is proportional to $\omega^4$, see below), that is, reduce $L$ and $C$; and second open the circuit so that the electric and magnetic fields spread into the surrounding space. Pulling the plates of the capacitor apart and straightening the coil gradually turns the LC circuit into a single straight wire in which the current oscillates back and forth and the charges at its two ends alternately change sign; this is an oscillating electric dipole, and it is the simplest antenna.

In 1886–1888 Hertz used an induction coil to excite two straight wires with metal balls (with a small spark gap between them) as an oscillating dipole, and detected the waves a few meters away with a metal ring with a spark gap: when sparks occurred at the transmitter, faint sparks also jumped across the gap of the receiving ring. He measured the standing waves and the wavelength of the electromagnetic waves, calculated from the known oscillation frequency that the wave speed equals the speed of light, and showed that electromagnetic waves, like light, can be reflected, refracted and polarized, thereby confirming Maxwell's theory.

### 10.4.2. Radiation from an Oscillating Electric Dipole

Let the **electric dipole moment** of an electric dipole at the origin undergo **simple harmonic motion** along the $z$ axis, $\boldsymbol{p}=p_0\cos\omega t\,\boldsymbol{e}_z$, with the length $l$ of the dipole much smaller than the wavelength $\lambda=2\pi c/\omega$. The field it produces in the surrounding space can be found from Maxwell's equations (the derivation requires retarded potentials and goes beyond this course). In the radiation zone $r\gg\lambda$, in spherical coordinates $(r,\theta,\varphi)$ with $\theta$ the angle between the direction of the field point and the $z$ axis, the field is

$$
\boldsymbol{E}=\frac{\ddot p(t-r/c)\sin\theta}{4\pi\varepsilon_0c^2r}\,\boldsymbol{e}_\theta,\qquad\boldsymbol{H}=\sqrt{\frac{\varepsilon_0}{\mu_0}}\,E_\theta\,\boldsymbol{e}_\varphi,\qquad\ddot p(t)=-\omega^2p_0\cos\omega t.
$$
These expressions show that:

- The value of the radiation field at time $t$ is determined by the state of the dipole at time $t-r/c$; the disturbance propagates outward at the speed of light.
- $\boldsymbol{E}$, $\boldsymbol{H}$ and the radial direction $\boldsymbol{e}_r$ are mutually perpendicular, $\boldsymbol{E}$ and $\boldsymbol{H}$ are in phase, and $\sqrt{\varepsilon_0}E=\sqrt{\mu_0}H$: in a small region far away, the radiation field is a plane electromagnetic wave propagating along $\boldsymbol{e}_r$ (in fact a spherical wave).
- The **electric field strength** is proportional to $1/r$, not to $1/r^3$ as in the field of a static dipole, so the radiation can reach far away; the field strength is proportional to the second derivative of the dipole moment, so only accelerated charges radiate.

The corresponding Poynting vector is

$$
\boldsymbol{S}=\boldsymbol{E}\times\boldsymbol{H}=\frac{\ddot p^2\sin^2\theta}{16\pi^2\varepsilon_0c^3r^2}\,\boldsymbol{e}_r,
$$
which is proportional to $1/r^2$, so the power through any concentric sphere is the same and the energy is indeed radiated away. The radiation is rotationally symmetric about the axis of the dipole: it is strongest in the direction perpendicular to the axis ($\theta=90^\circ$) and zero along the axis. Integrating over the whole sphere ($\int_0^\pi\sin^3\theta\,\mathrm{d}\theta=\frac43$), the radiated power is

$$
P=\frac{\ddot p^2}{6\pi\varepsilon_0c^3},\qquad\overline P=\frac{p_0^2\omega^4}{12\pi\varepsilon_0c^3}.
$$

![Left: the electric field lines of an oscillating electric dipole (the short line at the center) at one instant. Near the dipole the field lines connect its two ends, as for a static dipole; as the oscillation proceeds the field lines break off, form closed loops, and leave the dipole, propagating outward at the speed of light; right: the angular distribution $\sin^2\theta$ of the radiation intensity, with $\theta$ measured from the axis of the dipole (the vertical direction in the figure)](./plots/dipole-radiation.py)

**Remark 10.4.1 (Radiation of an Accelerated Charge)** For a single **point charge** $q$ moving with acceleration $a$ ($v\ll c$), $\ddot p=qa$ and the radiated power is

$$
P=\frac{q^2a^2}{6\pi\varepsilon_0c^3}\qquad(\text{Larmor formula}).
$$
This result has many important consequences. The average radiated power is proportional to $\omega^4$, which is why the sky is blue: air molecules in the electric field of sunlight perform **forced oscillations** and scatter light in all directions, and short-wavelength blue light is scattered most strongly (Rayleigh scattering, [5.4.3](/5.4.3)). Fast electrons decelerating sharply near an atomic nucleus emit a continuous X-ray spectrum (bremsstrahlung, [5.5.5](/5.5.5)); high-energy electrons moving on circular orbits in a ring accelerator emit very intense synchrotron radiation along the tangent, which has become an important light source for studying the structure of matter. In classical theory an electron orbiting a nucleus has a **centripetal acceleration**, would radiate continuously, and would fall into the nucleus within about $10^{-11}\,\mathrm{s}$, which contradicts the stability of atoms and is one of the signs of the failure of classical physics at the atomic scale ([5.5.4](/5.5.4)).

### 10.4.3. Light as an Electromagnetic Wave

One of the most important consequences of Maxwell's theory is that light is an electromagnetic wave with wavelength between about $380$ and $760\,\mathrm{nm}$. Many quantities in wave optics thereby acquire an electromagnetic meaning:

- The speed of light is $c=1/\sqrt{\varepsilon_0\mu_0}$, and the refractive index of a medium is $n=\sqrt{\varepsilon_{\mathrm{r}}\mu_{\mathrm{r}}}$.
- In a light wave it is mainly the electric field that acts on the human eye, photographic emulsions and photoelectric detectors (the force of the magnetic field on a charge is smaller than the electric force by a factor $v/c$), so $\boldsymbol{E}$ in a light wave is called the light vector, and the direction of vibration of light means the direction of $\boldsymbol{E}$.
- The intensity of light is the average energy flux density and is proportional to the square of the amplitude of the light vector, $I\propto E_0^2$. In wave optics only relative intensities need to be compared, and one often simply writes $I=E_0^2$.
- Light is a transverse wave and hence shows polarization ([5.4.3](/5.4.3)).

When two light waves meet in space, since Maxwell's equations are linear, the resultant light vector is the sum of the individual light vectors (the **superposition principle**) and the intensity is the square of the resultant amplitude; this is the basis of **interference** ([5.4.1](/5.4.1)) and **diffraction** ([5.4.2](/5.4.2)) of light. On the other hand, in the photoelectric effect and blackbody radiation light shows particle properties that classical electromagnetic theory cannot explain, which led to the quantum theory of light ([5.5.1](/5.5.1)).

## Summary

| Equation | Integral form | Differential form | Physical meaning |
|---|---|---|---|
| (1) | $\oiint\boldsymbol{D}\cdot\mathrm{d}\boldsymbol{S}=q_0$ | $\nabla\cdot\boldsymbol{D}=\rho_0$ | charge excites an electric field |
| (2) | $\oint\boldsymbol{E}\cdot\mathrm{d}\boldsymbol{l}=-\iint\partial_t\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{S}$ | $\nabla\times\boldsymbol{E}=-\partial_t\boldsymbol{B}$ | a changing magnetic field excites an electric field |
| (3) | $\oiint\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{S}=0$ | $\nabla\cdot\boldsymbol{B}=0$ | there is no magnetic charge |
| (4) | $\oint\boldsymbol{H}\cdot\mathrm{d}\boldsymbol{l}=I_0+\iint\partial_t\boldsymbol{D}\cdot\mathrm{d}\boldsymbol{S}$ | $\nabla\times\boldsymbol{H}=\boldsymbol{J}_0+\partial_t\boldsymbol{D}$ | current and a changing electric field excite a magnetic field |

- In source-free regions $\boldsymbol{E}$ and $\boldsymbol{H}$ satisfy the wave equation, with wave speed $u=1/\sqrt{\varepsilon\mu}$, equal to $c$ in vacuum. A plane electromagnetic wave is transverse, $\boldsymbol{E}$ and $\boldsymbol{H}$ are in phase, $\boldsymbol{E}\times\boldsymbol{H}$ is along the direction of propagation, and $E=uB$.
- Energy density $w=\frac12(\boldsymbol{E}\cdot\boldsymbol{D}+\boldsymbol{B}\cdot\boldsymbol{H})$, Poynting vector $\boldsymbol{S}=\boldsymbol{E}\times\boldsymbol{H}$, intensity $I=\frac12\sqrt{\varepsilon/\mu}\,E_0^2$; momentum density $\boldsymbol{S}/c^2$, radiation pressure $I/c$ (absorption) or $2I/c$ (reflection).
- Accelerated charges radiate electromagnetic waves; the radiation field of an oscillating electric dipole is proportional to $1/r$, its intensity is distributed as $\sin^2\theta$, and the total power is proportional to $\omega^4$.

## Questions

1. When a parallel-plate capacitor is being charged, the displacement current between the plates equals the conduction current in the wire. How does the magnetic field between the plates differ from that around the wire?
   Hint: By the Ampère–Maxwell law, for circular plates the field between the plates is circumferential and, at radius $r$ smaller than the plate radius $R$, proportional to $r$; for $r>R$ it is the same as the field around the wire, $\frac{\mu_0I}{2\pi r}$.
2. How does energy enter a capacitor while it is being charged?
   Hint: The electric field between the plates increases along the axis, the magnetic field at the edge is circumferential, and the Poynting vector points radially from the lateral side into the capacitor; the power flowing in equals the rate of increase of the electric field energy.
3. Why is the antenna of a radio broadcast station raised high, while the magnetic antenna in a radio receiver (a coil wound on a magnetic rod) is very small?
   Hint: A transmitting antenna must have dimensions comparable to the wavelength to radiate effectively; a receiving antenna only needs to pick up the magnetic field of the wave, and the high **permeability** of the magnetic rod concentrates the flux and raises the induced **electromotive force**.
4. Why do neither a charge at rest nor a charge in uniform motion radiate electromagnetic waves?
   Hint: The radiation field is proportional to the acceleration. In its rest frame a charge in uniform motion has only an electrostatic field, and there is no outward flow of energy.
