---
title: Waves
source_hash: 2250134e989f
---

The propagation of oscillations through space is a wave. The previous chapter ([5.1.6](/5.1.6)) studied a single oscillator; this chapter studies a continuous medium made of innumerable coupled oscillators: the oscillation of one mass element drags its neighbors along through elastic coupling, so that the state of oscillation spreads at a finite speed. We first describe the geometry and characteristic quantities of mechanical waves and write down the wave functions of traveling waves and harmonic waves. We then derive the **wave equation** and the wave speed from the elasticity of the medium and discuss the energy carried by waves, Huygens' principle (reflection, refraction, diffraction), the superposition of waves (interference, standing waves, reflection and transmission at interfaces, normal modes), sound waves, the Doppler effect and group velocity. Mathematically, most of this chapter is a physical reading of [2.5.3](/2.5.3) (d'Alembert's formula) and [2.5.4](/2.5.4) (separation of variables and standing waves), and the derivations are not repeated here; the Doppler effect for electromagnetic waves requires special relativity, and its derivation is given in the next chapter, [5.1.8](/5.1.8#sec-8.5.7). The superposition and diffraction of waves are the basis of wave optics ([5.4](/5.4)), and group velocity and the dispersion relation reappear for matter waves in quantum physics ([5.5.2](/5.5.2)).

## 7.1. Formation and Characteristics of Mechanical Waves

### 7.1.1. Formation of Mechanical Waves

**Definition 7.1.1 (Mechanical Wave)** When a mass element in an elastic medium is disturbed and oscillates, the elastic coupling between the parts of the medium makes the oscillation spread from near to far. This propagation of a state of oscillation through the medium is called a **mechanical wave**.

Two conditions are needed to form a mechanical wave: a source and an elastic medium. The "upstream" mass elements drive the "downstream" ones in turn, so the state of oscillation of an element at one moment appears at some place downstream at a later moment. What propagates is the state of oscillation (and energy), not the medium itself: each element only oscillates about its equilibrium position and does not "go with the flow".

### 7.1.2. Geometric Description of Waves

**Definition 7.1.2** A ray indicating the direction of propagation of a wave is called a **wave ray**; a surface formed by the points of the medium that oscillate with the same **phase** is called a **wave surface** (surface of constant phase); the surface formed by the points reached by the wave at a given instant is called the **wavefront**, which is the foremost wave surface.

In an isotropic medium the wave rays are perpendicular to the wave surfaces. A wave whose wave surfaces are planes is a plane wave, one whose surfaces are spheres is a spherical wave, and one whose surfaces are cylinders is a cylindrical wave; a point source in an isotropic medium emits spherical waves, and a small patch of a spherical wave far from the source can be approximated as a plane wave.

### 7.1.3. Classification of Waves

By physical nature, waves can be divided into mechanical waves, electromagnetic waves ([5.3.10](/5.3.10)), matter waves ([5.5.2](/5.5.2)) and gravitational waves (perturbations of the spacetime metric, first detected directly in 2015). Their physical mechanisms differ, but they obey similar mathematical laws. According to the relation between the direction of oscillation of the elements and the direction of propagation, we have the following classification.

**Definition 7.1.3** A wave in which the elements oscillate perpendicular to the direction of propagation is called a **transverse wave**; a wave in which the elements oscillate parallel to the direction of propagation is called a **longitudinal wave**.

Waves on a string are transverse, and sound waves in air are longitudinal (compression waves). Transverse waves require the medium to sustain shear deformation, so only longitudinal waves can propagate inside a fluid. Water surface waves are neither transverse nor longitudinal: because water flows and is incompressible, the water elements near the surface move both longitudinally and transversely, and in deep water they move approximately in circles.

In addition, waves can be classified by the shape of the wave surface as plane, spherical and cylindrical waves; by complexity as harmonic waves and complex waves ([Section 7.10](#sec-7.10)); by duration as continuous waves and pulses; and by whether the waveform propagates as traveling waves ([Section 7.2](#sec-7.2)) and **standing waves** ([Section 7.7](#sec-7.7)).

### 7.1.4. Characteristic Quantities of Waves

- Wave speed $u$: the **velocity** with which the state of oscillation propagates through the medium. It is generally determined by the properties of the medium and the type of wave, and in a dispersive medium it also depends on frequency ([Section 7.10](#sec-7.10)). The wave speed is not the oscillation velocity of the elements.
- Period $T$: the time for one complete wave to pass a given point on the wave ray. When both source and observer are at rest relative to the medium, it equals the period of oscillation of the source. The frequency is $\nu=1/T$ and the **angular frequency** is $\omega=2\pi\nu$.

**Definition 7.1.4** The distance between two neighboring elements on a wave ray that are in the same state of oscillation is called the **wavelength**, denoted $\lambda$; it is the spatial period of the wave, $\lambda=uT$. The quantity $k=2\pi/\lambda=\omega/u$ is called the **angular wavenumber**, and the vector $\boldsymbol{k}$ of magnitude $k$ pointing in the direction of propagation is called the **wave vector**.

The period is determined by the source and the wave speed by the medium, so the wavelength is determined by both: when the same wave enters another medium its frequency is unchanged, while its speed and wavelength change. The "wavenumber" of spectroscopy means $\tilde\nu=1/\lambda$, which differs from the angular wavenumber by a factor $2\pi$.

## 7.2. Traveling Waves and Harmonic Waves

### 7.2.1. Traveling Waves

**Definition 7.2.1 (Traveling Wave)** The propagation of a disturbance of some physical quantity through space is called a **traveling wave**. If a disturbance $y$ propagates along the $x$ axis with speed $u$, then

$$
y(x,t)=f\Big(t-\frac{x}{u}\Big)\tag{7.1}
$$
represents a traveling wave propagating in the $+x$ direction, and $y=f(t+x/u)$ one propagating in the $-x$ direction. The function $y(x,t)$ is called the wave function.

Indeed, $f\big(t+\Delta t-\frac{x+\Delta x}{u}\big)=f\big(t-\frac{x}{u}\big)$ if and only if $\Delta x=u\Delta t$: the disturbance at $x$ at time $t$ has reached $x+u\Delta t$ at time $t+\Delta t$, and the waveform as a whole translates with speed $u$. For a mechanical wave, the wave function is also the equation of motion of the elements of the medium ($y$ is the **displacement** from equilibrium of the element with coordinate $x$). This is precisely the traveling-wave solution of the one-dimensional **wave equation** ([2.5.3](/2.5.3#sec-3.1.1)).

### 7.2.2. Harmonic Waves

**Definition 7.2.2 (Harmonic Wave)** A wave whose source performs **simple harmonic motion**, with every element of the medium also performing simple harmonic motion of the same frequency, is called a **harmonic wave** (cosine wave, monochromatic wave).

Let a plane harmonic transverse wave propagate in the $+x$ direction with speed $u$ in a uniform, infinite, non-absorbing medium, and let the oscillation of the element at $x=0$ be $y(0,t)=A\cos(\omega t+\varphi_0)$. The element at $x$ repeats the oscillation of the element at $x=0$ with a delay $x/u$; since there is no absorption, the **amplitude** $A$ is unchanged, so

$$
y(x,t)=A\cos\Big[\omega\Big(t-\frac{x}{u}\Big)+\varphi_0\Big]=A\cos(\omega t-kx+\varphi_0).\tag{7.2}
$$
Equivalent forms are $y=A\cos\big[2\pi\big(\frac{t}{T}-\frac{x}{\lambda}\big)+\varphi_0\big]$ and $y=A\cos[k(ut-x)+\varphi_0]$. For a harmonic wave propagating in the $-x$ direction, replace $-kx$ by $+kx$.

The quantity $\varphi(x,t)=\omega t-kx+\varphi_0$ is the phase of the wave; it characterizes the state of oscillation of the element at $x$ at time $t$. For every wavelength advanced along the direction of propagation, the phase lags by $2\pi$. The propagation of a harmonic wave is the propagation of phase.

**Definition 7.2.3 (Phase Velocity)** The velocity with which points of constant phase propagate in a harmonic wave is called the **phase velocity**. From $\omega t-kx=\text{const}$ we get $\omega\,\mathrm{d}t-k\,\mathrm{d}x=0$,

$$
u=\frac{\mathrm{d}x}{\mathrm{d}t}=\frac{\omega}{k}.
$$

Hence the wave speed of a harmonic wave is its phase velocity. The wave function (7.2) can be read in two ways:

| Fixed quantity | $y$ as a function | Meaning |
|---|---|---|
| $x$ | $y(t)$ | Oscillation curve of the element at $x$, with time period $T$ |
| $t$ | $y(x)$ | Distribution of displacements of the elements at time $t$ (waveform), with spatial period $\lambda$ |

In calculations one often uses a complex representation (**complex numbers**, [2.3](/2.3)): $y=\operatorname{Re}\big[\tilde A\,\mathrm{e}^{\mathrm{i}(\omega t-kx)}\big]$ with complex amplitude $\tilde A=A\mathrm{e}^{\mathrm{i}\varphi_0}$. The spatial factor $\tilde A\mathrm{e}^{-\mathrm{i}kx}$ separates from the oscillation factor $\mathrm{e}^{\mathrm{i}\omega t}$, and differentiation becomes multiplication by $\mathrm{i}\omega$ or $-\mathrm{i}k$; this is the same idea as representing simple harmonic motion by a **phasor** in [5.1.6](/5.1.6). The physics literature also often uses $\mathrm{e}^{\mathrm{i}(kx-\omega t)}$; the two conventions differ only by a complex conjugate.

![Plane harmonic wave y = A cos(omega t - k x). Left: waveforms at several instants, the waveform translating to the right with phase velocity u; right: oscillation curves of the elements at x = 0 and x = lambda/4, the latter lagging in phase by pi/2](./plots/harmonic-wave.py)

### 7.2.3. Finding the Wave Function of a Harmonic Wave

By the phase relation, three conditions are needed to find the wave function of a one-dimensional harmonic wave: the equation of oscillation of some reference point (amplitude $A$, angular frequency $\omega$, **initial phase**); the wavelength $\lambda$ (or $k$, $u$); and the direction of propagation.

**Example 7.2.1** The equation of oscillation of a reference point $a$ at $x=d$ is $y_a=A\cos(\omega t+\varphi_a)$, the wavelength is $\lambda$, and the wave propagates in the $+x$ direction. Find the wave function.

**Solution** A point $x$ lies a distance $x-d$ farther along than the reference point $a$, so its phase lags by $\frac{2\pi}{\lambda}(x-d)$ and

$$
y(x,t)=A\cos\Big[\omega t+\varphi_a-\frac{2\pi}{\lambda}(x-d)\Big].
$$
For upstream points with $x<d$, $x-d<0$ and the phase leads; the formula holds in the same way.

**Example 7.2.2** The oscillation at $x=0$ is $y_0=A\cos\omega t$, the wavelength is $\lambda$, and the wave propagates in the $+x$ direction to a reflecting wall $S$ at $x=l$, where it is totally reflected with a phase jump of $\pi$. Find the wave function of the reflected wave.

**Solution** In total reflection the amplitude is unchanged. The path of the reflected wave from $x=0$ via the wall to the point $x$ ($x<l$) is $l+(l-x)=2l-x$, so the phase lags by $\frac{2\pi}{\lambda}(2l-x)$, to which the phase jump $\pi$ on reflection is added:

$$
y'(x,t)=A\cos\Big[\omega t-\frac{2\pi}{\lambda}(2l-x)\pm\pi\Big]=A\cos\Big[\omega t+\frac{2\pi}{\lambda}x-\frac{4\pi l}{\lambda}\pm\pi\Big].
$$
The term $+kx$ shows that it propagates in the $-x$ direction; either sign of $\pm\pi$ may be taken.

## 7.3. Elastic Deformation of Bodies

The wave speed is determined by the elasticity and inertia of the medium. Elasticity is described by elastic moduli: within the elastic limit, stress is proportional to strain (Hooke's law).

**Definition 7.3.1** The internal force per unit cross-sectional area of a body is called the **stress**, and the deformation per unit volume (or unit length) is called the **strain**. For the three basic kinds of deformation:

- Longitudinal deformation (tension or compression): a rod of cross-sectional area $S$ and original length $l_0$ stretches by $\Delta l$ under a tensile force $F$, $\frac{F}{S}=E\frac{\Delta l}{l_0}$, and the coefficient of proportionality $E$ is called **Young's modulus**;
- Shear: a pair of tangential forces of magnitude $F$ acts on two opposite surfaces of area $S$ and displaces them relative to each other through a shear angle $\theta$, $\frac{F}{S}=G\theta$, and the coefficient $G$ is called the **shear modulus**;
- Volume deformation: a uniform increase $\Delta p$ of pressure changes the volume from $V_0$ to $V_0+\Delta V$, $\Delta p=-K\frac{\Delta V}{V_0}$, and the coefficient $K$ is called the **bulk modulus**.

All three moduli have the unit $\mathrm{Pa}$. The stretching of a rod can be written $F=k\Delta l$ with $k=ES/l_0$, so Young's modulus is the force constant "per unit size". An isotropic material has only two independent elastic constants, $E=2G(1+\nu_{\mathrm{P}})$, where $\nu_{\mathrm{P}}$ is Poisson's ratio ($0<\nu_{\mathrm{P}}<\frac12$), so that $G<E$. A fluid has no shear elasticity ($G=0$) and only a bulk modulus. Many textbooks denote Young's modulus by $Y$; here we write $E$ following ISO 80000-4.

## 7.4. The Wave Equation

### 7.4.1. The One-Dimensional Wave Equation

For small-amplitude waves on a stretched string ([2.5.1](/2.5.1#sec-1.2.1)), in an elastic rod or in an air column, applying **Newton's second law** to a small element and using the linear relation between elastic force and deformation always gives the same equation:

$$
\frac{\partial^2y}{\partial x^2}=\frac{1}{u^2}\frac{\partial^2y}{\partial t^2},\tag{7.3}
$$
This is the one-dimensional **wave equation**, with $u$ the wave speed. By [2.5.3](/2.5.3#thm-3.1.1), its general solution is $y=f_1(t-x/u)+f_2(t+x/u)$, the sum of two traveling waves propagating in opposite directions; any function of the form (7.1) is a solution, and so of course is the harmonic wave (7.2). The equation is linear, so by the **superposition principle** any linear superposition of harmonic waves is also a solution; and by the **Fourier transform** ([2.5.6](/2.5.6)), any plane wave can be regarded as a superposition of harmonic waves. In three dimensions the equation is $\Delta y=\frac{1}{u^2}\frac{\partial^2y}{\partial t^2}$ (with the **Laplace operator** $\Delta$).

### 7.4.2. Wave Speed and the Properties of the Medium

Writing the equations of motion in various media in the form (7.3), we read off the wave speed from the coefficients. The common rule is $u=\sqrt{\text{elastic modulus}/\text{density}}$:

**Formula 7.4.1 (Speed of Mechanical Waves)**

| Wave | Wave speed | Remarks |
|---|---|---|
| Transverse wave on a string | $u=\sqrt{F_{\mathrm{T}}/\rho_{\mathrm{l}}}$ | $F_{\mathrm{T}}$ is the tension, $\rho_{\mathrm{l}}$ the linear density |
| Transverse wave in a solid | $u_{\mathrm{t}}=\sqrt{G/\rho}$ | $G$ is the shear modulus |
| Longitudinal wave in a thin rod | $u=\sqrt{E/\rho}$ | $E$ is Young's modulus |
| Longitudinal wave in a bulk solid | $u_{\mathrm{l}}=\sqrt{(K+\frac43G)/\rho}$ | Transverse deformation is constrained by the surrounding material |
| Longitudinal wave in a liquid | $u=\sqrt{K/\rho}$ | $K$ is the bulk modulus |
| Sound wave in a gas | $u=\sqrt{\gamma p/\rho}=\sqrt{\gamma RT/M}$ | Adiabatic process, $\gamma=C_p/C_V$, $M$ is the molar mass |

A sound wave in a gas is a compression wave; compression and expansion are so rapid that there is no time to exchange heat with the surroundings, so the process is adiabatic ([5.2.3](/5.2.3)) and the effective bulk modulus is $K=\gamma p$. Newton originally assumed an isothermal process and obtained $u=\sqrt{p/\rho}$, about 15% smaller than the measured value; Laplace pointed out that the adiabatic process should be used. For air at $20\,{}^\circ\mathrm{C}$ ($\gamma=1.40$, $M=0.029\,\mathrm{kg\,mol^{-1}}$), $u=\sqrt{1.40\times8.314\times293/0.029}\,\mathrm{m\,s^{-1}}\approx343\,\mathrm{m\,s^{-1}}$.

Since $G<K+\frac43G$, transverse waves in solids are slower than longitudinal ones. Of the seismic waves, the longitudinal wave (P wave, primary) arrives first and makes the ground jolt up and down; the transverse wave (S wave, secondary) arrives later and shakes the ground horizontally. The difference in arrival times gives the distance to the source; S waves cannot pass through the Earth's outer core, which is evidence that the outer core is liquid.

## 7.5. Energy of Waves

### 7.5.1. Energy of a Mass Element

An oscillation has energy, and the propagation of an oscillation is accompanied by the propagation of energy. Take a plane harmonic longitudinal wave in a thin rod, $y=A\cos\omega(t-x/u)$ (the derivation for a transverse wave is the same). A mass element of length $\Delta x$ and volume $\Delta V=S\Delta x$ has **kinetic energy**

$$
\Delta E_{\mathrm{k}}=\frac12\rho\Delta V\Big(\frac{\partial y}{\partial t}\Big)^2=\frac12\rho\Delta V\omega^2A^2\sin^2\omega\Big(t-\frac{x}{u}\Big).
$$
The strain of the element is $\partial y/\partial x$; as a "spring" of force constant $ES/\Delta x$ its elastic **potential energy** is $\frac12E\big(\frac{\partial y}{\partial x}\big)^2\Delta V$. Using $E=\rho u^2$ and $\frac{\partial y}{\partial x}=\frac{\omega A}{u}\sin\omega(t-\frac xu)$,

$$
\Delta E_{\mathrm{p}}=\frac12\rho u^2\Big(\frac{\partial y}{\partial x}\Big)^2\Delta V=\frac12\rho\Delta V\omega^2A^2\sin^2\omega\Big(t-\frac{x}{u}\Big)=\Delta E_{\mathrm{k}}.
$$

More generally, for any traveling wave $y=f(t-x/u)$ we have $\partial y/\partial t=-u\,\partial y/\partial x$, so the kinetic and potential energies of each element of a traveling wave are always equal and vary in phase. This is quite different from an isolated oscillator:

| | Isolated oscillator | Element in a wave |
|---|---|---|
| Kinetic and potential energy | One decreases as the other increases, $E_{\mathrm{k}}+E_{\mathrm{p}}=\text{const}$ | Maximal together and zero together, $E_{\mathrm{k}}=E_{\mathrm{p}}$ |
| Total energy | Conserved; no energy exchanged with the surroundings | Varies with time; continually absorbs energy from upstream and gives it to downstream |

At the equilibrium position ($y=0$) the element has maximal velocity and maximal deformation, so its energy is maximal; at maximal displacement ($y=\pm A$) the element is at rest and undeformed, so its energy is zero.

The energy of the wave per unit volume is called the energy density:

$$
w=\frac{\Delta E_{\mathrm{k}}+\Delta E_{\mathrm{p}}}{\Delta V}=\rho\omega^2A^2\sin^2\omega\Big(t-\frac{x}{u}\Big),\qquad \bar w=\frac1T\int_0^Tw\,\mathrm{d}t=\frac12\rho\omega^2A^2.
$$
The distribution of energy density moves forward with speed $u$ together with the waveform; the energy propagates in "packets", with neighboring packets separated by $\lambda/2$.

### 7.5.2. Intensity of a Wave

**Definition 7.5.1** The energy passing per unit time through a unit area perpendicular to the direction of propagation is called the **energy flux density**, of magnitude $wu$. Its average over one period is called the **wave intensity**, denoted $I$:

$$
I=\bar w u=\frac12\rho u\omega^2A^2=\frac12Z\omega^2A^2,\qquad Z=\rho u.\tag{7.4}
$$
The product $Z=\rho u$ of the density of the medium and the wave speed is called the **characteristic impedance** of the medium.

The unit of intensity is $\mathrm{W\,m^{-2}}$. A medium with larger $Z$ is called a wave-denser medium and one with smaller $Z$ a wave-rarer medium; $Z$ determines how the wave distributes energy at an interface ([Section 7.7.4](#sec-7.7.4)). By Eq. (7.4), $I\propto\omega^2$: for equal amplitudes, the intensity of ultrasound ($\nu>20\,\mathrm{kHz}$) is much greater than that of ordinary sound.

In a non-absorbing medium the total energy passing through any wave surface per unit time is constant. For a plane wave the area of the wave surface is constant, so the amplitude $A$ is constant; for a spherical wave $I\cdot4\pi r^2=\text{const}$, so $I\propto1/r^2$ and $A\propto1/r$; for a cylindrical wave $I\cdot2\pi rL=\text{const}$, so $A\propto1/\sqrt r$. The wave function of a spherical harmonic wave is therefore $y=\frac{A_0r_0}{r}\cos\omega(t-r/u)$.

### 7.5.3. Absorption of Waves

Because of irreversible processes such as internal friction, heat conduction and molecular collisions, part of the energy of a wave is absorbed by the medium as it passes through. Suppose the relative decrease of the amplitude over $\mathrm{d}x$ is proportional to $\mathrm{d}x$, $-\mathrm{d}A/A=\alpha\,\mathrm{d}x$, where $\alpha$ is called the absorption coefficient. For constant $\alpha$, the amplitude and intensity of a plane wave decay exponentially:

$$
A=A_0\mathrm{e}^{-\alpha x},\qquad I=I_0\mathrm{e}^{-2\alpha x}.
$$

**Example 7.5.1** The absorption coefficient of air for sound is about $\alpha_{\mathrm{air}}\approx2\times10^{-11}\nu^2\,\mathrm{m^{-1}}$ ($\nu$ in $\mathrm{Hz}$), and that of steel is about $\alpha_{\mathrm{steel}}\approx4\times10^{-7}\nu\,\mathrm{m^{-1}}$. For ultrasound of frequency $\nu=5\times10^6\,\mathrm{Hz}$, the distance over which the intensity falls to $1\%$ is $x=\ln100/(2\alpha)$: in air $\alpha=500\,\mathrm{m^{-1}}$ and $x\approx4.6\,\mathrm{mm}$; in steel $\alpha=2\,\mathrm{m^{-1}}$ and $x\approx1.15\,\mathrm{m}$. Hence low-frequency sound travels far in air while ultrasound does not, but ultrasound can penetrate deep into steel parts and is used for flaw detection.

## 7.6. Huygens' Principle

In propagation, a wave may change its direction, frequency and amplitude. In his *Treatise on Light*, published in 1690, Huygens proposed a general graphical construction for determining the advance of a wave surface.

### 7.6.1. Huygens' Principle

**Property 7.6.1 (Huygens' Principle)** Every point on a wave surface in a medium can be regarded as a point source emitting wavelets (secondary spherical waves); at any later instant, the envelope of the wavelet surfaces is the new wave surface at that instant.

Given the wave surface at time $t$, draw wavelet surfaces of radius $u\Delta t$ centered at each of its points; their envelope is the wave surface at time $t+\Delta t$, the wave rays are perpendicular to the wave surface, and this gives the direction of propagation. In a uniform isotropic medium, the wave surface of a plane wave remains a plane and that of a spherical wave remains a family of concentric spheres.

### 7.6.2. Diffraction of Waves

The phenomenon in which a wave bends around the edge of an obstacle and deviates from rectilinear propagation is called *diffraction*. According to Huygens' principle, the wavelets emitted from points of the wave surface at the edge of an obstacle or at a small aperture propagate in all directions, and the envelope also extends into the geometric shadow. The smaller the size of the obstacle (or aperture) compared with the wavelength, the more pronounced the diffraction.

For example, medium-wave and short-wave radio broadcasts (frequencies from tens of $\mathrm{kHz}$ to tens of $\mathrm{MHz}$, wavelengths from tens of meters to over a thousand meters) easily bend around buildings and hills, whereas television and Wi-Fi signals (hundreds of $\mathrm{MHz}$ to several $\mathrm{GHz}$, wavelengths of the order of decimeters and centimeters) diffract weakly and are easily blocked; for equal intensity, a deep male voice is easier to hear through a wall.

### 7.6.3. Refraction and Total Reflection of Waves

When a wave passes from one medium into another, its direction of propagation changes; this is called refraction. Let a plane wave in medium 1, with wave speed $u_1$, strike the interface at angle of incidence $i$, and let the wave speed in medium 2 be $u_2$. The point $B$ of the incident wave surface $AB$ reaches the point $C$ on the interface after time $\Delta t$, with $BC=u_1\Delta t=AC\sin i$; in the same time the wavelet emitted from $A$ has propagated a distance $AD=u_2\Delta t=AC\sin r$ in medium 2, where $r$ is the angle of refraction. Dividing the two relations gives:

**Theorem 7.6.1 (Law of Refraction)** The angle of incidence $i$ and the angle of refraction $r$ satisfy

$$
\frac{\sin i}{\sin r}=\frac{u_1}{u_2}.
$$
For light, $u=c/n$ with $n$ the refractive index, and the law of refraction is written $n_1\sin i=n_2\sin r$.

The medium of larger refractive index is called the optically denser medium and that of smaller index the optically rarer medium. When light passes from the denser to the rarer medium ($n_1>n_2$), $r>i$; when the angle of incidence reaches the critical angle $i_{\mathrm{C}}$, $\sin i_{\mathrm{C}}=n_2/n_1$, the angle of refraction is $90^\circ$; for angles of incidence larger than $i_{\mathrm{C}}$ there is no refracted wave and the incident wave is entirely reflected, which is *total internal reflection*. Optical fibers use total internal reflection to guide light in the core: a thin optical cable can have a communication capacity exceeding that of a much thicker electric cable.

The same medium has different refractive indices (different wave speeds) for waves of different frequencies, which is called *dispersion*. The refractive index of glass for visible light increases with frequency (normal dispersion) and does the opposite near an absorption band (anomalous dispersion). For X-rays the refractive index of glass is slightly less than 1 ($1-n\sim10^{-6}$), so X-rays incident from vacuum on glass at grazing incidence (at an angle to the surface smaller than a few milliradians) undergo total reflection (external total reflection); multiple grazing reflections in a bundle of capillaries can focus X-rays or turn them into a parallel beam, making an X-ray lens.

### 7.6.4. Limitations of Huygens' Principle

Huygens' principle can explain the directions of reflection, refraction and diffraction of waves, but it is only a geometric construction: it cannot explain why the wavelets do not propagate backward (why there is no backward wave), cannot give the intensity of the wave and its distribution, and cannot explain interference and other phenomena involving phase. Fresnel supplemented it with the idea that wavelets superpose coherently, which gave the [Huygens–Fresnel principle](/5.4.2#sec-2.1) and explained diffraction quantitatively. Mathematically, Kirchhoff's formula for the three-dimensional wave equation shows that sharp signals stay sharp in odd-dimensional space (the strong form of Huygens' principle in [2.5.3](/2.5.3#sec-3.5.1)), which is one rigorous formulation of the wavelet picture.

## 7.7. Superposition of Waves and Standing Waves

### 7.7.1. The Principle of Superposition of Waves

When several waves meet, red light and green light each remain red and green after crossing, and when listening to an orchestra we can still distinguish the timbre and melody of each instrument. This shows that the propagation of waves is independent: several waves can pass through the same medium at the same time, each keeping its own direction of propagation, direction of oscillation, amplitude, wavelength and frequency, without affecting the others.

**Property 7.7.1 (Principle of Superposition of Waves)** In the region where several waves meet, the oscillation at any point is the resultant (vector sum of displacements) of the oscillations that each wave would cause at that point if it propagated alone.

The principle of superposition of waves is the physical expression of the linearity of the wave equation (7.3) (**superposition principle**, [2.5.1](/2.5.1#sec-1.1.2)). When the amplitude or intensity is too large, the deformation and elastic force of the medium are no longer linearly related and the principle of superposition fails; examples are the generation of frequency-doubled light by intense laser light in a crystal (nonlinear optics), and the formation of a **shock wave**, which is also a nonlinear effect.

### 7.7.2. Interference of Waves

When two waves are superposed and a stable pattern of reinforced and weakened oscillation appears in space, the phenomenon is called *interference*.

**Definition 7.7.1 (Coherence Conditions)** The conditions under which two waves produce stable interference are called the **coherence conditions**: the same frequency, the same direction of oscillation (or parallel components), and a constant phase difference. Waves satisfying the coherence conditions are called coherent waves.

Let two coherent sources $S_1$, $S_2$ oscillate as $A_j\cos(\omega t+\varphi_j)$ ($j=1,2$), at distances $r_1$, $r_2$ from the field point $P$. The phase difference of the two component oscillations at $P$ is

$$
\Delta\varphi=\varphi_2-\varphi_1-\frac{2\pi}{\lambda}(r_2-r_1),
$$
and the resultant amplitude is $A=\sqrt{A_1^2+A_2^2+2A_1A_2\cos\Delta\varphi}$ (superposition of collinear oscillations of the same frequency in [5.1.6](/5.1.6)). For $\Delta\varphi=2m\pi$ the interference is constructive, $A=A_1+A_2$; for $\Delta\varphi=(2m+1)\pi$ it is destructive, $A=\lvert A_1-A_2\rvert$ ($m\in\mathbb{Z}$). When the two sources are in phase, the conditions reduce to the path difference $r_2-r_1$ being an integer or half-integer multiple of the wavelength. The cross term $2A_1A_2\cos\Delta\varphi$ in the intensity $I\propto A^2$ is positive where the interference is constructive and negative where it is destructive; the total energy is unchanged and is merely redistributed in space.

### 7.7.3. Standing Waves

When two coherent waves of equal amplitude propagating in opposite directions are superposed, a **standing wave** results; this is the most common kind of interference. Let

$$
y_1=A\cos\Big(\omega t-\frac{2\pi x}{\lambda}\Big),\qquad y_2=A\cos\Big(\omega t+\frac{2\pi x}{\lambda}\Big),
$$
then by the sum-to-product identity,

$$
y=y_1+y_2=2A\cos\frac{2\pi x}{\lambda}\cos\omega t.\tag{7.5}
$$
It no longer has the form $f(t\mp x/u)$: the phase $\omega t$ does not contain $x$, and there is no propagation of phase.

**Definition 7.7.2** The points of a standing wave where the amplitude $2A\lvert\cos\frac{2\pi x}{\lambda}\rvert$ is zero are called **nodes**, and the points where the amplitude is maximal (equal to $2A$) are called **antinodes**.

Features of a standing wave:

- Amplitude: the nodes lie at $x=(2m+1)\frac\lambda4$ and the antinodes at $x=m\frac\lambda2$; neighboring nodes (or neighboring antinodes) are $\lambda/2$ apart, so measuring the spacing of the nodes gives the wavelength of the traveling wave.
- Phase: a standing wave is oscillation in segments, each segment lying between two neighboring nodes; all points in one segment are in phase, and neighboring segments are in antiphase ($\cos\frac{2\pi x}{\lambda}$ changes sign at a node).
- Energy: the energy flux densities of the two waves are equal in magnitude and opposite in direction, so the net energy flux is zero and a standing wave does not transport energy. The energy is "confined" between neighboring nodes and antinodes (an interval of length $\lambda/4$) and converts back and forth within it: when all elements reach maximal displacement at the same time, their velocities are zero, the deformation near the nodes is largest, and the energy is entirely potential energy concentrated near the nodes; when they pass through the equilibrium position at the same time, there is no deformation, and the energy is entirely kinetic energy concentrated near the antinodes.

If the two waves have unequal amplitudes, $A_2=A_1+\Delta A$, then $y=2A_1\cos\frac{2\pi x}{\lambda}\cos\omega t+\Delta A\cos\big(\omega t+\frac{2\pi x}{\lambda}\big)$, the sum of a standing wave and a traveling wave. This can still be called a standing wave, but the nodes now also oscillate, and there is a net energy flow in the direction of the wave of larger amplitude.

![Standing wave y = 2A cos(2 pi x / lambda) cos(omega t). Left: waveforms at several instants within half a period, the nodes (N) at rest and the antinodes (A) of maximal amplitude; right: the first three normal modes of a string fixed at both ends](./plots/standing-waves.py)

### 7.7.4. Reflection and Transmission at an Interface

Let a plane harmonic wave in medium 1, of characteristic impedance $Z_1$, be incident normally on the interface $x=0$ with medium 2, of characteristic impedance $Z_2$. The incident, reflected and transmitted waves are

$$
y_1=A_1\cos(\omega t-k_1x),\qquad y_1'=A_1'\cos(\omega t+k_1x),\qquad y_2=A_2\cos(\omega t-k_2x).
$$
The frequency is unchanged, and the amplitudes $A_1'$, $A_2$ may be negative (a negative sign means a phase jump of $\pi$). Two conditions must hold on the two sides of the interface: continuity of displacement (the two media stay in contact), $[y_1+y_1']_{x=0}=[y_2]_{x=0}$; and continuity of stress (**Newton's third law**), which for a longitudinal wave reads $E_1\big[\frac{\partial(y_1+y_1')}{\partial x}\big]_{x=0}=E_2\big[\frac{\partial y_2}{\partial x}\big]_{x=0}$. Since $E_jk_j=\rho_ju_j^2\cdot\frac{\omega}{u_j}=\omega Z_j$, the two conditions become $A_1+A_1'=A_2$ and $Z_1(A_1-A_1')=Z_2A_2$, with solution

$$
A_1'=\frac{Z_1-Z_2}{Z_1+Z_2}A_1,\qquad A_2=\frac{2Z_1}{Z_1+Z_2}A_1.\tag{7.6}
$$

This gives the phase relations:

- Transmitted wave: $A_2$ has the same sign as $A_1$, so the transmitted wave is always in phase with the incident wave at the interface.
- Reflected wave: for a wave passing from a wave-denser to a wave-rarer medium ($Z_1>Z_2$), $A_1'$ has the same sign as $A_1$, the reflected wave is in phase with the incident wave at the interface, and the interface is an antinode of the standing wave; for a wave passing from a wave-rarer to a wave-denser medium ($Z_1<Z_2$), $A_1'$ has the opposite sign to $A_1$, and the reflected wave has a phase jump of $\pi$ at the interface.

**Definition 7.7.3 (Half-Wave Loss)** When a wave incident normally from a wave-rarer medium on the interface with a wave-denser medium is reflected, the phase of the reflected wave jumps by $\pi$ relative to the incident wave at the interface, equivalent to a gain (or loss) of half a wavelength in path; this is called the **half-wave loss** (a phase change of $\pi$ on reflection).

When there is a half-wave loss, the interface is a node of the standing wave formed by the incident and reflected waves. In the extreme cases, a fixed end ($Z_2\to\infty$, $y=0$) is a node and a free end ($Z_2\to0$) is an antinode. So when a positive pulse travels from a light rope to a heavy one, the reflected pulse is negative and the transmitted pulse is positive; from a heavy rope to a light one, both the reflected and the transmitted pulses are positive. Light reflected at an interface between two media also has a half-wave loss ([5.4.1](/5.4.1)); in that case it is judged by the refractive index, and there is a half-wave loss for light passing from the optically rarer to the optically denser medium.

By Eq. (7.4), $I\propto ZA^2$, so the reflectance and transmittance are

$$
R=\frac{I_1'}{I_1}=\Big(\frac{Z_1-Z_2}{Z_1+Z_2}\Big)^2,\qquad T=\frac{I_2}{I_1}=\frac{Z_2A_2^2}{Z_1A_1^2}=\frac{4Z_1Z_2}{(Z_1+Z_2)^2},\qquad R+T=1,
$$
the last relation being conservation of energy. $R$ and $T$ are symmetric in $Z_1$ and $Z_2$ and independent of the direction of propagation. For $Z_1\gg Z_2$ or $Z_1\ll Z_2$, $R\approx1$ and the wave is almost totally reflected; for $Z_1\approx Z_2$, $R\approx0$ and the wave is almost totally transmitted, which is called impedance matching.

| Medium | $Z/(\mathrm{kg\,m^{-2}\,s^{-1}})$ | Interface | Intensity transmittance $T$ |
|---|---|---|---|
| Air (standard conditions) | $4.2\times10^2$ | Air to water | $0.001$ |
| Water | $1.5\times10^6$ | Air to steel | $0.00004$ |
| Steel (longitudinal wave) | $4.6\times10^7$ | Water to steel | $0.12$ |

Hence in ultrasonic flaw detection there must be no air gap between the probe and the steel part, and a layer of oil is usually applied to the surface of the part as a coupling layer; the coupling gel applied to the skin in ultrasound imaging works for the same reason. Practical transmitters and receivers all include transition layers to match the acoustic impedances.

**Example 7.7.1** Media 1, 2, 3 are arranged in order along the $x$ axis, with characteristic impedances satisfying $Z_1<Z_2>Z_3$; medium 2 is a thin layer of thickness $D$, with interfaces $S_1$ and $S_2$. A harmonic wave is incident normally from medium 1. Neglecting multiple reflections, find the minimum thickness $D$ for which the wave $y_1'$ reflected at $S_1$ and the wave $y_1''$ reflected back into medium 1 from $S_2$ interfere destructively.

**Solution** $y_1'$ is reflected at $S_1$ from a wave-rarer to a wave-denser medium and has a half-wave loss, so its phase lags by an additional $\pi$; $y_1''$ is reflected at $S_2$ from a wave-denser to a wave-rarer medium and has no phase jump, but it travels an extra $2D$ in medium 2, so its phase lags by an additional $\omega\cdot2D/u_2$. Both reflected waves propagate in the $-x$ direction, so their phase difference is independent of $x$:

$$
\varphi_1'-\varphi_1''=-\pi+\frac{2D\omega}{u_2}.
$$
Destructive interference requires $\varphi_1'-\varphi_1''=(2m+1)\pi$, that is, $2D\omega/u_2=2(m+1)\pi$ and $D=(m+1)\frac{\lambda_2}{2}$, so the minimum thickness is $D_{\min}=\lambda_2/2$, where $\lambda_2$ is the wavelength in medium 2. If the two reflected waves also have equal amplitudes, the reflection is completely eliminated, and medium 2 can serve as an anti-reflection ("stealth") coating; mufflers also use the destructive interference of reflected waves. If $Z_1<Z_2<Z_3$, both reflections have a half-wave loss and the minimum thickness becomes $\lambda_2/4$, which is the principle of the anti-reflection coating on optical lenses ([5.4.1](/5.4.1)).

### 7.7.5. Normal Modes

A standing wave can be produced by reflection at an interface; standing waves can exist in any system with boundaries. The vibration of a string is a collective vibration of infinitely many **degrees of freedom**. Just as a system of $n$ coupled oscillators has $n$ specific frequencies of vibration (the **eigenvalues** of its **dynamics** matrix), a bounded wave system has a series of specific stable patterns of vibration.

**Definition 7.7.4 (Normal Mode)** A stable pattern (a standing wave) in which a bounded system vibrates as a whole at a single frequency is called a **normal mode** of the system, and the corresponding frequency is called a normal-mode frequency (**natural frequency**).

The natural frequencies are determined entirely by the system itself (the medium, the dimensions and the boundary conditions) and are independent of external factors. The boundary conditions determine whether an endpoint is a node or an antinode: a fixed end (where the oscillations caused by the incident and reflected waves are opposite and cancel) is a node, and a free end (where they have the same direction and reinforce) is an antinode. For a string or air column of length $L$ and wave speed $u$:

| Boundary | Condition | Wavelength | Normal-mode frequency |
|---|---|---|---|
| Both ends fixed (or both ends free) | $L=n\frac{\lambda_n}{2}$ | $\lambda_n=\frac{2L}{n}$ | $\nu_n=n\frac{u}{2L}$, $n=1,2,3,\dots$ |
| One end fixed, one end free | $L=n\frac{\lambda_n}{4}$, $n$ odd | $\lambda_n=\frac{4L}{n}$ | $\nu_n=n\frac{u}{4L}$, $n=1,3,5,\dots$ |

The mode with $n=1$ is called the fundamental, and the others are the $n$-th harmonics. Mathematically, this is exactly the result obtained by **separation of variables** in [2.5.4](/2.5.4#sec-4.1.3): the natural frequencies come from the eigenvalue problem given by the boundary conditions.

A general vibration is a linear superposition of many normal modes, the proportion of each mode being determined by the initial conditions, namely the coefficients of the **Fourier series** expansion of the initial shape. Different ways of excitation contain different modes: when a string is plucked at its midpoint, the midpoint must be an antinode, so the modes with a node at the midpoint ($n$ even) do not appear. Stringed instruments change their timbre by controlling the content of the harmonics (the harmonic analysis of [5.1.6](/5.1.6)) and change the fundamental by adjusting the string length and tension; when the frequency of an external force equals one of the natural frequencies, **resonance** occurs and can excite that mode alone, which is also the principle of tuning.

**Example 7.7.2** A tuning fork of frequency $248.5\,\mathrm{Hz}$ is held over the mouth of a thin tube containing water. As the water level is varied continuously, resonance occurs successively for air-column heights $L_1=0.34\,\mathrm{m}$ and $L_2=1.03\,\mathrm{m}$. Find the speed of sound in air.

**Solution** At resonance a standing wave forms in the tube, with an antinode at the mouth (open, free end) and a node at the water surface (fixed end), so $L=(2n+1)\frac\lambda4$. The frequency is unchanged, so the wavelengths of the two resonances are the same and $n$ differs by 1: $L_2-L_1=\frac\lambda2$, $\lambda=2(L_2-L_1)=1.38\,\mathrm{m}$, and one can check that $L_1\approx\lambda/4$ ($n=0$). The speed of sound is $u=\lambda\nu=1.38\times248.5\,\mathrm{m\,s^{-1}}\approx343\,\mathrm{m\,s^{-1}}$. The actual antinode lies slightly outside the mouth of the tube (end correction), and computing from the difference of the two resonance lengths cancels this correction exactly.

## 7.8. Sound Waves

Mechanical waves with frequencies between $20\,\mathrm{Hz}$ and $20\,\mathrm{kHz}$, which can produce the sensation of hearing, are called sound waves; those below $20\,\mathrm{Hz}$ are infrasound and those above $20\,\mathrm{kHz}$ are ultrasound. Sound waves in gases and liquids are longitudinal waves (compression waves).

**Definition 7.8.1** The difference $\Delta p=p-p_0$ between the pressure $p$ at a point of the medium in the presence of a sound wave and the pressure $p_0$ in its absence is called the **sound pressure** at that point. Where $\Delta p>0$ the medium is compressed and where $\Delta p<0$ it is rarefied.

For a harmonic sound wave $y=A\cos\omega(t-x/u)$ ($y$ is the longitudinal displacement of the element), the volume strain is $\partial y/\partial x$, so by the definition of the bulk modulus $\Delta p=-K\frac{\partial y}{\partial x}$, and using $K=\rho u^2$,

$$
\Delta p=-\rho u\omega A\sin\omega\Big(t-\frac{x}{u}\Big),\qquad \Delta p_{\mathrm{m}}=\rho u\omega A.
$$
The sound pressure and the displacement differ in phase by $\pi/2$: the medium is most strongly compressed or rarefied where the displacement is zero. The sound intensity is

$$
I=\frac12\rho u\omega^2A^2=\frac{\Delta p_{\mathrm{m}}^2}{2\rho u},
$$
and in experiments the intensity is usually obtained by measuring the amplitude of the sound pressure.

The range of sound intensities perceived by the human ear is enormous: at $1000\,\mathrm{Hz}$ the threshold of hearing is about $10^{-12}\,\mathrm{W\,m^{-2}}$ and the threshold of pain about $1\,\mathrm{W\,m^{-2}}$, while the perceived loudness is roughly proportional to the logarithm of the intensity. A logarithmic scale is therefore used.

**Definition 7.8.2 (Sound Intensity Level)** Taking the reference intensity $I_0=10^{-12}\,\mathrm{W\,m^{-2}}$, the **sound intensity level** of a sound wave of intensity $I$ is

$$
L_I=10\lg\frac{I}{I_0}\ \mathrm{dB}.
$$

Normal conversation is about $60\,\mathrm{dB}$, prolonged exposure to levels above $85\,\mathrm{dB}$ damages hearing, and gunfire or a rock concert can reach $120\,\mathrm{dB}$. Each tenfold increase in intensity raises the level by $10\,\mathrm{dB}$. Human hearing depends not only on intensity but also on frequency: at $50\,\mathrm{dB}$ a $1000\,\mathrm{Hz}$ sound is already loud, while a $50\,\mathrm{Hz}$ sound can hardly be heard. Equal-loudness contours give the intensity level at each frequency for the same loudness.

Infrasound is common in earthquakes, volcanic eruptions, storms and nuclear explosions; it is weakly absorbed and travels very far ([Section 7.5.3](#sec-7.5.3)), and some frequencies are harmful to the human body. Ultrasound has high frequency, short wavelength, concentrated energy and good directivity, and is used for ultrasonic cleaning, underwater positioning and communication (sonar), extracorporeal lithotripsy and medical ultrasound imaging (B-mode, color Doppler).

## 7.9. The Doppler Effect

**Definition 7.9.1 (Doppler Effect)** The phenomenon that the frequency received differs from the frequency of the source because of the motion of the source or of the observer (receiver) is called the **Doppler effect**.

### 7.9.1. Doppler Effect of Mechanical Waves

First distinguish three frequencies: the source frequency $\nu_{\mathrm{S}}$ is the number of oscillations the source makes per unit time (the number of complete waves emitted); the wave frequency $\nu=u/\lambda$ is the number of complete waves passing a point in the medium per unit time; the received frequency $\nu_{\mathrm{R}}$ is the number of complete waves received by the receiver per unit time. Take the medium as the **reference frame**, and let the source S and receiver R move along the line joining them with velocities $v_{\mathrm{S}}$ and $v_{\mathrm{R}}$: $v_{\mathrm{S}}>0$ when the source moves toward the receiver and $v_{\mathrm{R}}>0$ when the receiver moves toward the source, and negative otherwise; the wave speed is $u>0$.

1. Source at rest, receiver moving. The wavelength $\lambda=u/\nu_{\mathrm{S}}$ is unchanged, but the receiver, moving into the waves, receives an additional $v_{\mathrm{R}}/\lambda$ waves per unit time: $\nu_{\mathrm{R}}=\frac{u+v_{\mathrm{R}}}{\lambda}=\frac{u+v_{\mathrm{R}}}{u}\nu_{\mathrm{S}}$.
2. Source moving, receiver at rest. In one period $T_{\mathrm{S}}$ the source follows the preceding wave surface by $v_{\mathrm{S}}T_{\mathrm{S}}$, so the wavelength in the medium ahead is shortened to $\lambda=(u-v_{\mathrm{S}})T_{\mathrm{S}}$, while the number of waves received is unchanged: $\nu_{\mathrm{R}}=\frac{u}{\lambda}=\frac{u}{u-v_{\mathrm{S}}}\nu_{\mathrm{S}}$.
3. Both moving. The motion of the source changes the wavelength in the medium, and the motion of the receiver changes the number of waves received; the two factors multiply.

**Formula 7.9.1 (Doppler Formula for Mechanical Waves)** For a source and receiver moving along the line joining them,

$$
\nu_{\mathrm{R}}=\frac{u+v_{\mathrm{R}}}{u-v_{\mathrm{S}}}\,\nu_{\mathrm{S}}.\tag{7.7}
$$
In general, let $\boldsymbol{v}_{\mathrm{S}}$ make an angle $\theta_{\mathrm{S}}$ with the direction from S to R and $\boldsymbol{v}_{\mathrm{R}}$ make an angle $\theta_{\mathrm{R}}$ with the direction from R to S; only the components of the velocities along the line joining them matter:

$$
\nu_{\mathrm{R}}=\frac{u+v_{\mathrm{R}}\cos\theta_{\mathrm{R}}}{u-v_{\mathrm{S}}\cos\theta_{\mathrm{S}}}\,\nu_{\mathrm{S}}.
$$

The frequency rises when source and receiver approach each other and falls when they recede. Note that the roles of source and receiver are not symmetric: $\nu_{\mathrm{R}}=\nu_{\mathrm{S}}$ only when $v_{\mathrm{S}}=v_{\mathrm{R}}$ (both move with the same velocity, with no relative motion); what matters is the velocity of each relative to the medium, not just the **relative velocity**. When the direction of motion is perpendicular to the line joining them ($\theta_{\mathrm{R}}=\theta_{\mathrm{S}}=\pi/2$), $\nu_{\mathrm{R}}=\nu_{\mathrm{S}}$: mechanical waves have no transverse Doppler effect.

**Example 7.9.1** A stationary sound source S has frequency $\nu_{\mathrm{S}}=300\,\mathrm{Hz}$ and the speed of sound is $u=330\,\mathrm{m\,s^{-1}}$. An observer R, to the right of S, moves to the right with $v_{\mathrm{R}}=60\,\mathrm{m\,s^{-1}}$; a reflecting wall to the right of R also moves to the right with $v=100\,\mathrm{m\,s^{-1}}$. Find the **beat** frequency measured by R.

**Solution** Below all speeds are taken as magnitudes. R moves away from S, so the frequency received directly is $\nu_{\mathrm{R}}=\frac{u-v_{\mathrm{R}}}{u}\nu_{\mathrm{S}}$. The wall, as a receiver moving away from S, receives the frequency $\nu'=\frac{u-v}{u}\nu_{\mathrm{S}}$; it then acts as a source moving away from R with speed $v$, and R, moving toward it, receives the reflected wave with frequency

$$
\nu_{\mathrm{R}}'=\frac{u+v_{\mathrm{R}}}{u+v}\nu'=\frac{u+v_{\mathrm{R}}}{u+v}\cdot\frac{u-v}{u}\nu_{\mathrm{S}}.
$$
The beat frequency is

$$
\lvert\nu_{\mathrm{R}}-\nu_{\mathrm{R}}'\rvert=\frac{2(v-v_{\mathrm{R}})}{u+v}\nu_{\mathrm{S}}=\frac{2\times(100-60)}{330+100}\times300\,\mathrm{Hz}\approx55.8\,\mathrm{Hz}.
$$
Conversely, measuring the beat frequency gives the speed of the reflector, which is the principle of Doppler velocimetry.

### 7.9.2. Doppler Effect of Electromagnetic Waves

The propagation of electromagnetic waves needs no medium, so "velocity relative to the medium" loses its meaning and only the relative velocity $v$ of source and receiver is meaningful; moreover, the time measurements of the two must be related through special relativity. In the frame of the receiver, let the source move with velocity $v$ at angle $\theta$ to the line from the source to the receiver; relativity gives ([5.1.8](/5.1.8#sec-8.5.7))

$$
\nu_{\mathrm{R}}=\frac{\sqrt{1-v^2/c^2}}{1-(v/c)\cos\theta}\,\nu_{\mathrm{S}}.\tag{7.8}
$$

- Longitudinal Doppler effect: on approach ($\theta=0$), $\nu_{\mathrm{R}}=\sqrt{\frac{c+v}{c-v}}\,\nu_{\mathrm{S}}$ and the frequency rises (blueshift); on recession ($\theta=\pi$), $\nu_{\mathrm{R}}=\sqrt{\frac{c-v}{c+v}}\,\nu_{\mathrm{S}}$ and the frequency falls (redshift). The result depends only on the relative velocity: "the source moving toward the receiver" and "the receiver moving toward the source" give the same result. For $v\ll c$ they agree with the formulas for mechanical waves, with a relative frequency shift of about $\pm v/c$.
- Transverse Doppler effect: for $\theta=\pi/2$, $\nu_{\mathrm{R}}=\sqrt{1-v^2/c^2}\,\nu_{\mathrm{S}}<\nu_{\mathrm{S}}$; this is purely the time dilation of the moving source and is a relativistic effect that mechanical waves do not have.

The redshift or blueshift of the spectral lines of celestial objects gives their radial velocities, and radar velocimetry, laser Doppler velocimetry and satellite tracking also use the Doppler effect. The redshift of the spectral lines of distant galaxies increases with distance (Hubble's law) and is evidence of the expansion of the universe; strictly speaking, however, the cosmological redshift comes from the growth of the cosmic scale factor and is approximately equal to the Doppler redshift only when the redshift is small.

### 7.9.3. Shock Waves

When the speed $v_{\mathrm{S}}$ of the source exceeds the wave speed $u$, the source runs ahead of all the wave surfaces it emitted earlier, the later wave surfaces overtake the earlier ones, and the envelope of the wave surfaces is a cone with the source at its apex, called a *Mach cone*. In time $\Delta t$ the source travels $v_{\mathrm{S}}\Delta t$, while the wave surface emitted at the start has radius $u\Delta t$, so the half-angle $\alpha$ of the cone satisfies

$$
\sin\alpha=\frac{u}{v_{\mathrm{S}}}=\frac{1}{\mathit{Ma}},
$$
where $\mathit{Ma}=v_{\mathrm{S}}/u$ is called the *Mach number*. Energy is highly concentrated on the cone, and the pressure and density of the medium jump almost discontinuously across it; this is a **shock wave**. When the shock wave of a supersonic aircraft sweeps over the ground it produces a "sonic boom", which is why supersonic flight is restricted to a minimum altitude. The V-shaped wake at the bow of a supersonic bullet or a speedboat is also a Mach cone.

![Wave surfaces emitted by a moving source (the source moves to the right). Left: Ma = 0.6, the wave surfaces ahead are crowded and the frequency is raised, those behind are sparse; right: Ma = 2, the envelope of the wave surfaces forms a Mach cone with sin alpha = 1/Ma](./plots/moving-source-wavefronts.py)

There is a similar phenomenon in electromagnetism: when a high-energy charged particle moves in a transparent medium with speed $v$ exceeding the speed of light $c/n$ in the medium (but still less than the speed of light $c$ in vacuum), it emits a cone of electromagnetic waves called *Cherenkov radiation*, whose half-angle satisfies $\sin\alpha=\frac{c}{nv}$. Its emission lasts an extremely short time (of the order of $10^{-10}\,\mathrm{s}$), the cone angle gives the speed of the particle, and it is widely used in the detection of high-energy particles and neutrinos; the blue glow in the water pool of a nuclear reactor is Cherenkov radiation.

### 7.9.4. Applications of the Doppler Effect

- Velocity measurement: traffic radar measures the speed of vehicles, laser Doppler velocimeters measure the velocity of fluids, and ultrasound Doppler measures the velocity of blood flow (color Doppler ultrasound).
- Astronomy: the redshift and blueshift of spectral lines give the radial velocities of celestial objects and are used to discover binary stars and exoplanets (the radial-velocity method).
- Satellite tracking and navigation: the change of received frequency determines the position and velocity of a satellite.

## 7.10. Complex Waves and Group Velocity

### 7.10.1. Complex Waves and Amplitude-Modulated Waves

A harmonic wave has a single frequency (it is monochromatic) and extends without limit in time and space; apart from frequency and amplitude it carries no information, and in communication it is called a carrier. A non-harmonic wave made by superposing a finite or infinite number of harmonic waves of different frequencies is called a complex wave. Modulating the amplitude, frequency or phase of a carrier according to some rule (amplitude, frequency or phase modulation) gives a complex wave that can carry and transmit information.

Superposing two harmonic waves $y_1=A\cos(\omega_1t-k_1x)$ and $y_2=A\cos(\omega_2t-k_2x)$ of equal amplitude and nearby frequencies propagating in the same direction gives

$$
y=2A\cos\Big(\frac{\Delta\omega}{2}t-\frac{\Delta k}{2}x\Big)\cos\big(\bar\omega t-\bar kx\big),\tag{7.9}
$$
where $\Delta\omega=\omega_1-\omega_2$, $\Delta k=k_1-k_2$, $\bar\omega=\frac{\omega_1+\omega_2}{2}$ and $\bar k=\frac{k_1+k_2}{2}$. This is an amplitude-modulated wave: the amplitude of each element varies slowly (beats, [5.1.6](/5.1.6)) while the phase varies rapidly. The high-frequency carrier advances with speed $\bar\omega/\bar k$, and the envelope of the amplitude advances with speed $\Delta\omega/\Delta k$.

### 7.10.2. Dispersion and Group Velocity

**Definition 7.10.1** A medium in which harmonic waves of different frequencies have different wave speeds is called a dispersive medium, and otherwise a non-dispersive medium. For a given medium, the dependence $\omega=\omega(k)$ of the angular frequency on the angular wavenumber is called the **dispersion relation** of the medium.

The form of the dispersion relation depends on the specific mechanism of interaction between the wave and the medium, and it is also often expressed as a relation $u(k)$ or $u(\lambda)$. In a non-dispersive medium $\omega=uk$ with $u$ constant; strings and sound waves in air are approximately non-dispersive under ordinary conditions. In a linear medium the frequency of a wave is unchanged when it passes from one medium to another; what changes are the wave speed and wavelength, as when light passes from air into glass.

**Definition 7.10.2 (Group Velocity)** For a wave packet formed by superposing harmonic waves of nearby frequencies, the velocity with which its envelope (the amplitude distribution) propagates is called the **group velocity**:

$$
v_{\mathrm{g}}=\frac{\mathrm{d}\omega}{\mathrm{d}k}.\tag{7.10}
$$

By Eq. (7.9) the envelope of two waves advances with speed $\Delta\omega/\Delta k$, and letting $\Delta k\to0$ gives Eq. (7.10). From $\omega=uk$,

$$
v_{\mathrm{g}}=u+k\frac{\mathrm{d}u}{\mathrm{d}k}=u-\lambda\frac{\mathrm{d}u}{\mathrm{d}\lambda}.
$$
In a non-dispersive medium $v_{\mathrm{g}}=u$ and the wave packet advances without changing shape; in a dispersive medium $v_{\mathrm{g}}\ne u$, the components of different frequencies gradually separate, and the packet broadens and distorts as it propagates ("dispersion makes wave packets unstable"). The energy and information of a wave propagate with the group velocity (in a region of normal dispersion without strong absorption), whereas the phase velocity can exceed the speed of light in vacuum without violating relativity.

**Example 7.10.1** The dispersion relation of deep-water surface gravity waves (water depth much greater than the wavelength) is $\omega=\sqrt{gk}$, with phase velocity $u=\omega/k=\sqrt{g/k}=\sqrt{g\lambda/(2\pi)}$; long waves travel faster. The group velocity is

$$
v_{\mathrm{g}}=\frac{\mathrm{d}\omega}{\mathrm{d}k}=\frac12\sqrt{\frac gk}=\frac u2.
$$
So after a stone is thrown into deep water, the group of waves forming a ring of ripples spreads outward at half the phase velocity: an individual crest appears at the rear of the group, passes through it and disappears at the front. In swell generated by a distant storm, the long waves reach the coast first, which is also a result of dispersion.

![Wave packet of deep-water waves (omega = sqrt(g k)): waveforms at two instants. The envelope advances with the group velocity v_g = u/2, while one crest of the carrier (dot) advances with the phase velocity u, moving from the rear of the packet to the front](./plots/group-velocity.py)

## Summary

| Topic | Key points |
|---|---|
| Traveling waves and harmonic waves | $y=f(t\mp x/u)$; $y=A\cos(\omega t-kx+\varphi_0)$, $k=2\pi/\lambda=\omega/u$, $\lambda=uT$ |
| Wave equation and wave speed | $\frac{\partial^2y}{\partial x^2}=\frac{1}{u^2}\frac{\partial^2y}{\partial t^2}$; $u=\sqrt{\text{modulus}/\text{density}}$, and $u=\sqrt{\gamma p/\rho}$ in a gas |
| Energy | Kinetic and potential energy of an element are equal and in phase; $\bar w=\frac12\rho\omega^2A^2$, $I=\frac12Z\omega^2A^2$, $Z=\rho u$ |
| Huygens' principle | The envelope of wavelets is the new wave surface; explains reflection, refraction ($\sin i/\sin r=u_1/u_2$) and diffraction |
| Superposition and interference | Coherence conditions: same frequency, same direction of oscillation, constant phase difference; $\Delta\varphi=2m\pi$ constructive, $(2m+1)\pi$ destructive |
| Standing waves | $y=2A\cos kx\cos\omega t$, nodes $\lambda/2$ apart, no energy transport; both ends fixed $\nu_n=nu/(2L)$ |
| Interface | $A_1'=\frac{Z_1-Z_2}{Z_1+Z_2}A_1$, $A_2=\frac{2Z_1}{Z_1+Z_2}A_1$; reflection from wave-rarer to wave-denser medium has a half-wave loss |
| Sound waves | $\Delta p_{\mathrm{m}}=\rho u\omega A$, $L_I=10\lg(I/I_0)\,\mathrm{dB}$, $I_0=10^{-12}\,\mathrm{W\,m^{-2}}$ |
| Doppler effect | Mechanical waves $\nu_{\mathrm{R}}=\frac{u+v_{\mathrm{R}}}{u-v_{\mathrm{S}}}\nu_{\mathrm{S}}$; light $\nu_{\mathrm{R}}=\frac{\sqrt{1-\beta^2}}{1-\beta\cos\theta}\nu_{\mathrm{S}}$; Mach cone $\sin\alpha=u/v_{\mathrm{S}}$ |
| Group velocity | $v_{\mathrm{g}}=\mathrm{d}\omega/\mathrm{d}k$; deep-water waves $v_{\mathrm{g}}=u/2$ |

## Questions

1. Why must one often adjust the length of the string (or the tension, or the driving frequency) in standing-wave experiments?

   **Answer** a stable, pronounced standing wave forms only when the driving frequency equals one of the normal-mode frequencies; changing the length or tension changes the normal-mode frequencies.

2. In a plane harmonic wave, what are the kinetic and potential energies of an element as it passes through the equilibrium position? How does this differ from a spring oscillator?

   **Answer** both are maximal at the same time; see [Section 7.5.1](#sec-7.5.1).

3. A sound source and an observer move with the same **speed** $v$, in one case "the source moves toward the observer" and in the other "the observer moves toward the source". Is the received frequency the same? What about light?

   **Answer** for sound the former gives $\frac{u}{u-v}\nu_{\mathrm{S}}$ and the latter $\frac{u+v}{u}\nu_{\mathrm{S}}$, the former being higher; for light only the relative velocity matters and the two are the same.
