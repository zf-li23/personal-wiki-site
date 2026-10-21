---
title: Polarization of Light
description: Linearly, circularly and elliptically polarized light, unpolarized and partially polarized light; polarizers and Malus's law; polarization of reflected and refracted light and Brewster's law; Rayleigh scattering and the polarization of scattered light; birefringence, o and e rays, polarizing prisms; wave plates; interference of polarized light and chromatic polarization; artificial birefringence (photoelastic, Kerr and Pockels effects); optical activity and the Faraday effect.
source_hash: "08e936421843"
---

Interference and **diffraction** show that light is a wave, but they cannot distinguish a **longitudinal wave** from a **transverse wave**; polarization shows that light is a **transverse wave**. Light is an **electromagnetic wave** ([5.3.10](/5.3.10#sec-10.4.3)), and the light vector $\boldsymbol{E}$ is perpendicular to the direction of propagation; within the plane perpendicular to the direction of propagation it can still vibrate in different ways, and this is the polarization of light. This chapter first describes the various states of polarization (Section 3.1) and then discusses several ways to produce and analyze polarized light: polarizers (Section 3.2), reflection and refraction at interfaces (Section 3.3), scattering (Section 3.4) and birefringence in crystals (Section 3.5). We then use crystal plates to convert linearly polarized light into elliptically and circularly polarized light (Section 3.6) and discuss the interference of polarized light (Section 3.7). The last two sections (optional) introduce artificial birefringence caused by applied stress and electric fields (Section 3.8) and optical activity (Section 3.9). Mathematically, the polarization states are just the superposition of two mutually perpendicular **simple harmonic motions** of the same frequency, the same as the case of frequency ratio $1$ of the **Lissajous figures** in [5.1.6](/5.1.6#sec-6.2.3); the optical anisotropy of crystals comes from the tensor nature of the **permittivity** ([5.3.4](/5.3.4#sec-4.2.5)). Polarization is widely used in stereoscopic films, liquid-crystal displays, photography, stress analysis, optical communication and chemical analysis (a polarimeter measures the concentration of sugar).

## 3.1. States of Polarization of Light

### 3.1.1. Transverse Waves and Polarization

The direction of vibration of a longitudinal wave is along the direction of propagation, and the wave is axially symmetric about it; the direction of vibration of a transverse wave is perpendicular to the direction of propagation, and in general it lacks this symmetry. This can be demonstrated with a soft rope passing through a slit: when the slit is parallel to the direction of vibration of the rope, the transverse wave passes; when they are perpendicular, the transverse wave is blocked. A longitudinal wave passes whatever the orientation of the slit.

**Definition 3.1.1 (Polarization)** The property of a transverse wave that its direction of vibration is asymmetric with respect to the direction of propagation is called **polarization**. Only transverse waves can be polarized.

The plane formed by the light vector $\boldsymbol{E}$ and the direction of propagation is called the plane of vibration. In what follows, let light propagate along the $z$ axis, and adopt the convention that the sense of rotation is judged looking toward the source (that is, with the light coming toward the observer), with the $x$ axis pointing to the right and the $y$ axis pointing up.

### 3.1.2. Linearly Polarized Light

**Definition 3.1.2 (Linearly Polarized Light)** Light whose light vector vibrates in one and the same plane at every point of space is called **linearly polarized light** (plane-polarized light), and that plane is its plane of vibration.

In figures, short bars represent light vibrations in the plane of the paper and dots represent light vibrations perpendicular to the paper. Any light vector can be resolved into $x$ and $y$ components:

$$
\boldsymbol{E}(z,t)=\boldsymbol{e}_xE_{0x}\cos(\omega t-kz)+\boldsymbol{e}_yE_{0y}\cos(\omega t-kz+\Delta\varphi),
$$
where $\Delta\varphi$ is the phase difference of the $y$ component relative to the $x$ component. For $\Delta\varphi=0$ or $\pi$,

$$
\boldsymbol{E}(z,t)=(\boldsymbol{e}_xE_{0x}\pm\boldsymbol{e}_yE_{0y})\cos(\omega t-kz),
$$
the direction of the light vector is constant, and the light is linearly polarized. Linearly polarized light can therefore be regarded as the superposition of two linearly polarized beams of the same frequency and direction of propagation, with mutually perpendicular directions of vibration and a phase difference of $0$ or $\pi$.

### 3.1.3. Circularly Polarized Light and Elliptically Polarized Light

For other values of $\Delta\varphi$, at a given $z$ the tip of the light vector traces an ellipse in the plane perpendicular to the direction of propagation: eliminating $t$ gives

$$
\frac{E_x^2}{E_{0x}^2}+\frac{E_y^2}{E_{0y}^2}-\frac{2E_xE_y}{E_{0x}E_{0y}}\cos\Delta\varphi=\sin^2\Delta\varphi,
$$
which is precisely the trajectory of the superposition of two mutually perpendicular simple harmonic motions of the same frequency ([5.1.6](/5.1.6#sec-6.2.3)).

**Definition 3.1.3** Light whose light vector tip traces a circle in the plane perpendicular to the direction of propagation at any point along the propagation direction is called **circularly polarized light**, and light for which it traces an ellipse is called **elliptically polarized light**. Looking toward the source, light whose vector rotates clockwise is called right-handed and light whose vector rotates counterclockwise is called left-handed. Linearly, circularly and elliptically polarized light are collectively called completely polarized light.

From the equation above:

- for $0<\Delta\varphi<\pi$ the light is right-handed, and for $-\pi<\Delta\varphi<0$ it is left-handed;
- for $\Delta\varphi=\pm\pi/2$ the principal axes of the ellipse lie along the coordinate axes (an upright ellipse); if in addition $E_{0x}=E_{0y}=E_0$, the light is circularly polarized:

  $$
  \boldsymbol{E}(z,t)=E_0\Big[\boldsymbol{e}_x\cos(\omega t-kz)+\boldsymbol{e}_y\cos\Big(\omega t-kz\pm\frac\pi2\Big)\Big],
  $$
  with the $+$ sign for right-handed and the $-$ sign for left-handed light;
- for $\Delta\varphi=0,\pi$ the ellipse degenerates to a line, that is, linearly polarized light.

Circularly and elliptically polarized light can therefore be regarded as the superposition of two linearly polarized beams of the same frequency and direction of propagation, with mutually perpendicular directions of vibration and a constant phase difference. Conversely, adding right- and left-handed circularly polarized light:

$$
E_0\Big[\boldsymbol{e}_x\cos(\omega t-kz)+\boldsymbol{e}_y\cos\Big(\omega t-kz+\frac\pi2\Big)\Big]+E_0\Big[\boldsymbol{e}_x\cos(\omega t-kz)+\boldsymbol{e}_y\cos\Big(\omega t-kz-\frac\pi2\Big)\Big]=2E_0\boldsymbol{e}_x\cos(\omega t-kz),
$$
that is, linearly polarized light can also be regarded as the superposition of left- and right-handed circularly polarized beams of equal frequency, phase and amplitude. This decomposition is used in Section 3.9 to explain optical activity.

The light vector of circularly polarized light rotates with angular velocity $\omega$, so at a given instant at two points a distance $\Delta z$ apart along the direction of propagation the directions of the light vector differ by $k\,\Delta z$: at a given moment the tips of the light vectors at the various points lie on a helix whose pitch is one **wavelength**.

![Polarization states from the superposition of two mutually perpendicular components of amplitude ratio 0.6 for various phase differences Δφ, looking toward the source, with x to the right and y up. Δφ = 0 and π give linear polarization; 0 < Δφ < π gives right-handed (clockwise) and π < Δφ < 2π left-handed light; the last panel is right-handed circular polarization with equal amplitudes and Δφ = π/2](./plots/polarization-states.py)

**Remark 3.1.1** The convention for handedness is not uniform. This chapter adopts the traditional convention of optics (looking toward the source, clockwise is right-handed); electrical engineering (IEEE) and much of the particle-physics literature adopt the opposite convention, defining handedness looking along the direction of propagation or by the spin of the photon (helicity). When reading the literature, first find out which convention is used.

### 3.1.4. Unpolarized Light and Partially Polarized Light

In an ordinary source a large number of atoms and molecules emit light independently, and the direction of vibration and phase of each wave train are random, changing rapidly and uncorrelated.

**Definition 3.1.4** Light whose light vector vibrates in randomly distributed directions in the plane perpendicular to the direction of propagation, with equal amplitude in all directions and no preferred direction, is called **unpolarized light** (natural light).

Unpolarized light can be resolved into two mutually perpendicular, equally intense and mutually incoherent linearly polarized beams, $I=I_x+I_y$ with $I_x=I_y=I/2$. Note that these two components have no definite phase relation and cannot be combined into one linearly polarized beam; in figures, alternating short bars and dots represent it.

**Definition 3.1.5** Light that is an (incoherent) mixture of unpolarized light and completely polarized light is called **partially polarized light**. Let the total intensity of partially polarized light be $I_{\mathrm{t}}$, of which the intensity of the completely polarized part is $I_{\mathrm{p}}$ and that of the unpolarized part is $I_{\mathrm{n}}$; then

$$
P=\frac{I_{\mathrm{p}}}{I_{\mathrm{t}}}=\frac{I_{\mathrm{p}}}{I_{\mathrm{n}}+I_{\mathrm{p}}}
$$
is called the **degree of polarization**.

Completely polarized light has $P=1$, unpolarized light has $P=0$, and partially polarized light has $0<P<1$. Scattered light from the sky and light reflected from glass are partially polarized light consisting of unpolarized and linearly polarized parts; for such light, rotating a polarizer through a full turn and measuring the maximum and minimum of the transmitted intensity gives $P=\frac{I_{\max}-I_{\min}}{I_{\max}+I_{\min}}$.

## 3.2. Producing and Analyzing Linearly Polarized Light

### 3.2.1. Polarizers

Obtaining linearly polarized light from unpolarized light is called polarizing, and the device used is called a polarizer; examining the state of polarization of light is called analyzing, and the device used is called an analyzer. The same polarizing device can serve as either a polarizer or an analyzer.

The most common polarizing device is the polarizing sheet. Some substances absorb one of two mutually perpendicular light-vibration components strongly and are almost transparent to the other; this property is called dichroism. Tourmaline plates are dichroic; the commonly used polarizing sheets (molecular type) are made by stretching an iodine-containing polyvinyl alcohol film so that the long-chain molecules line up in one direction. For infrared and microwaves, a wire-grid polarizer of parallel fine metal wires can also be used: the electric field along the wires drives electrons and is absorbed and reflected, while the component perpendicular to the wires is transmitted. The direction of light vibration that a polarizing sheet lets through is called its transmission axis.

After passing through a polarizing sheet, unpolarized light becomes linearly polarized and its intensity is halved, $I=I_0/2$.

### 3.2.2. Malus's Law

**Theorem 3.2.1 (Malus's Law)** After linearly polarized light of intensity $I_0$ passes through a polarizing sheet, the transmitted intensity is

$$
I=I_0\cos^2\alpha,
\tag{3.1}
$$
where $\alpha$ is the angle between the direction of vibration of the incident light and the transmission axis of the polarizing sheet.

**Proof** Let the amplitude of the incident light vector be $A_0$ and resolve it into components parallel and perpendicular to the transmission axis, with amplitudes $A_0\cos\alpha$ and $A_0\sin\alpha$. Only the parallel component passes, so the transmitted amplitude is $A=A_0\cos\alpha$, and since the intensity is proportional to the square of the amplitude, $I=I_0\cos^2\alpha$. $\square$

At $\alpha=0$, $I=I_0$ is largest; at $\alpha=90^\circ$, $I=0$, which is called extinction.

**Example 3.2.1 (Inserting a Third Polarizer)** Two polarizing sheets have mutually perpendicular transmission axes, and unpolarized light (intensity $I_0$) is completely extinguished after passing through them. A third polarizing sheet is inserted between them with its transmission axis at angle $\theta$ to the first. Find the transmitted intensity.

**Solution** After the first sheet $I_1=I_0/2$; by Malus's law, after the middle sheet $I_2=I_1\cos^2\theta$, and after the last sheet

$$
I_3=I_2\cos^2(90^\circ-\theta)=\frac{I_0}{2}\cos^2\theta\sin^2\theta=\frac{I_0}{8}\sin^22\theta.
$$
It is largest at $\theta=45^\circ$, with $I_3=I_0/8$. Inserting a "light-blocking" polarizing sheet actually lets light through, because the middle sheet changes the direction of vibration of the light.

### 3.2.3. Analyzing with a Polarizing Sheet

Let the light to be analyzed pass through a polarizing sheet, rotate the sheet through a full turn about the ray, and observe the transmitted intensity:

| Incident light | Transmitted intensity |
|---|---|
| Unpolarized light | Constant |
| Linearly polarized light | Varies, with two extinctions |
| Circularly polarized light | Constant |
| Elliptically polarized light | Varies, without extinction |
| Unpolarized + linearly polarized light | Varies, without extinction |
| Unpolarized + circularly polarized light | Constant |
| Unpolarized + elliptically polarized light | Varies, without extinction |

With a polarizing sheet alone one can identify linearly polarized light, but one cannot distinguish unpolarized light, circularly polarized light and "unpolarized + circularly polarized light", nor elliptically polarized light and the two kinds of partially polarized light that have a preferred direction. For this a quarter-wave plate is needed (Section 3.6.4).

## 3.3. Polarization of Reflected and Refracted Light

### 3.3.1. The s and p Components

When light is reflected and refracted at the interface of two isotropic media, the light vector is resolved into the s component perpendicular to the plane of incidence and the p component parallel to it (s from the German *senkrecht*, "perpendicular"). The reflectances of the two components differ, so after reflection and refraction unpolarized light generally becomes partially polarized: the s component predominates in the reflected light and the p component in the refracted light, and the degree of polarization varies with the angle of incidence.

The formulas for the reflectances (the Fresnel equations) can be derived from the boundary conditions of **Maxwell's equations**:

**Formula 3.3.1 (Fresnel Equations)** Light passes from a medium of **refractive index** $n_1$ to a medium of refractive index $n_2$ at angle of incidence $i$ with angle of refraction $r$. The intensity reflectances of the s and p components are

$$
R_{\mathrm{s}}=\frac{\sin^2(i-r)}{\sin^2(i+r)},\qquad R_{\mathrm{p}}=\frac{\tan^2(i-r)}{\tan^2(i+r)}.
$$

At normal incidence both equal $\big(\frac{n_1-n_2}{n_1+n_2}\big)^2$, which is about $4\%$ for air–glass ($n_2=1.5$). $R_{\mathrm{s}}$ increases monotonically with the angle of incidence; $R_{\mathrm{p}}$ first decreases to zero and then increases, and at grazing incidence both tend to $1$.

![Reflectances of the s and p components and the degree of polarization of the reflected light for unpolarized light incident from air (n1 = 1) onto glass (n2 = 1.5). At Brewster's angle iB ≈ 56.3° Rp = 0, and the reflected light is completely polarized s light](./plots/fresnel-reflectance.py)

### 3.3.2. Brewster's Law

When $i+r=90^\circ$, $\tan(i+r)\to\infty$ and $R_{\mathrm{p}}=0$: the reflected light contains only the s component and is linearly polarized.

**Theorem 3.3.1 (Brewster's Law)** When the angle of incidence $i_{\mathrm{B}}$ satisfies

$$
\tan i_{\mathrm{B}}=\frac{n_2}{n_1}
\tag{3.2}
$$
the reflected light is linearly polarized with its direction of vibration perpendicular to the plane of incidence, and the reflected and refracted rays are perpendicular to each other. $i_{\mathrm{B}}$ is called *Brewster's angle*, also the polarizing angle.

**Proof** The condition for the reflected light to contain only the s component is $i_{\mathrm{B}}+r_{\mathrm{B}}=90^\circ$. By the **law of refraction**, $n_1\sin i_{\mathrm{B}}=n_2\sin r_{\mathrm{B}}=n_2\cos i_{\mathrm{B}}$, which gives $\tan i_{\mathrm{B}}=n_2/n_1$. The angle of reflection equals $i_{\mathrm{B}}$, so the angle between the reflected and refracted rays is $180^\circ-i_{\mathrm{B}}-r_{\mathrm{B}}=90^\circ$. $\square$

Brewster's law has an intuitive electromagnetic explanation. The electric field of the refracted light drives electrons in the second medium into **forced oscillation**, and they radiate like oscillating **electric dipoles**; the reflected light is the sum of this radiation. The **electric dipoles** driven by the p component oscillate along the p direction of vibration of the refracted light, which is perpendicular to the refracted ray. When the reflected ray is perpendicular to the refracted ray, the direction of reflection lies exactly along the axis of the dipoles, and electric dipole radiation vanishes along the axis ([5.3.10](/5.3.10#sec-10.4.2)), so the reflected light contains no p component.

For air–glass ($n=1.5$), $i_{\mathrm{B}}\approx56.3^\circ$; for air–water ($n=1.33$), $i_{\mathrm{B}}\approx53.1^\circ$. From $\tan r_{\mathrm{B}}=n_1/n_2$, when light from the second medium strikes the interface at $r_{\mathrm{B}}$, $r_{\mathrm{B}}$ is also a Brewster angle, and the reflected light is likewise linearly polarized. Measuring the Brewster angle of an opaque **dielectric** (such as a black glaze) gives its refractive index through Eq. (3.2).

### 3.3.3. Glass-Plate Stacks and Brewster Windows

When unpolarized light is incident at Brewster's angle, the p component is entirely refracted; only a small part of the s component is reflected and most is refracted. So although the reflected light is completely polarized, its intensity is weak, and the refracted light is intense but only partially polarized. For air–glass, $R_{\mathrm{s}}=\sin^2(i_{\mathrm{B}}-r_{\mathrm{B}})\approx0.15$, and only about $7\%$ of the energy of the unpolarized light is reflected.

- Glass-plate stack: many parallel glass plates are stacked and unpolarized light is incident at Brewster's angle. At each surface part of the s component is reflected away while the p component suffers no loss; with enough plates the transmitted light is nearly linearly polarized (p light) and the reflected light is s light.
- Brewster window: the two ends of the discharge tube of an external-cavity gas laser (such as a He–Ne laser) are closed with windows tilted at Brewster's angle. P light passes through the windows without reflection loss, while s light suffers a loss on every round trip and cannot oscillate, so the laser output is linearly polarized.

In the glare reflected from water, roads and shop windows the s component (horizontal vibration) predominates. Polarizing sunglasses and camera polarizing filters, with the transmission axis vertical, greatly weaken such reflections, whereas ordinary sunglasses merely attenuate all light uniformly.

## 3.4. Polarization of Scattered Light

### 3.4.1. Scattering of Light

When light passes through an inhomogeneous medium, part of it leaves its original direction and propagates in all directions; this is called scattering of light. A beam in clear water is hardly visible from the side, but in a suspension containing tiny sulfur particles a bright light path is seen, because the particles scatter light into the observer's eyes. By the size of the scatterers, scattering is of two kinds:

- Particle scattering: scattering of light in emulsions, suspensions and air containing dust or droplets, where the particle size $a$ is comparable to or larger than the wavelength. For $a\gg\lambda$ it can be treated as ordinary reflection and refraction, and diffuse reflection belongs here.
- Molecular scattering: scattering of light in pure gases or liquids, which is very weak. The thermal motion of molecules causes local density **fluctuations**, and these regions of fluctuation, with sizes much smaller than the wavelength ($a\ll\lambda$), cause scattering. Near the **critical point** of a gas–liquid system the density fluctuations become very large and the regions of fluctuation can be comparable in size to the wavelength; the fluid becomes turbid and scatters light strongly, which is called critical opalescence.

### 3.4.2. Rayleigh's Scattering Law

**Theorem 3.4.1 (Rayleigh Scattering Law)** When the size of the scatterer is much smaller than the wavelength (roughly $a<0.1\lambda$), the scattered intensity is inversely proportional to the fourth power of the wavelength:

$$
I\propto\frac1{\lambda^4}.
$$

This kind of scattering is called *Rayleigh scattering*. Its origin is that electrons in the scatterer are set into forced oscillation by the electric field of the incident light and become oscillating electric dipoles, and the power of electric dipole radiation is proportional to $\omega^4$ ([5.3.10](/5.3.10#sec-10.4.2)). When the size of the scatterer exceeds about $0.1\lambda$, the dependence of the scattered intensity on wavelength gradually becomes less pronounced (Mie scattering), and for sizes much larger than the wavelength it is almost independent of wavelength.

By Rayleigh's scattering law, violet light of $\lambda=400\,\mathrm{nm}$ is $(700/400)^4\approx9.4$ times stronger than red light of $\lambda=700\,\mathrm{nm}$. This is why a clear sky is blue (the solar spectrum has relatively little violet and the eye is not sensitive to violet, so the sky looks blue rather than violet). At sunrise and sunset sunlight passes through a thick layer of atmosphere, the short-wavelength components are scattered away, and the remaining light is reddish, so the rising and setting Sun look red. Clouds consist of water droplets much larger than the wavelength of visible light, so their scattering is independent of wavelength and they are white. In space there is no atmospheric scattering, so the sky is black and the Sun does not radiate in all directions as it appears to from the ground.

### 3.4.3. Polarization of Scattered Light

Let light propagate along the $z$ axis. If the incident light is linearly polarized with vibration along $y$, the electric dipoles in the scatterer oscillate along $y$, the scattered light is also linearly polarized, and its intensity follows the angular distribution of dipole radiation,

$$
I=I_0'\sin^2\psi,
$$
where $\psi$ is the angle between the direction of scattering and the $y$ axis and $I_0'$ is merely a reference value; the distribution is rotationally symmetric about the $y$ axis, and there is no scattered light along the $y$ direction.

If the incident light is unpolarized, it can be resolved into two equally intense, incoherent components vibrating along $x$ and $y$, and the scattered intensity as a function of the scattering angle $\theta$ (the angle between the directions of scattering and incidence) is

$$
I=I_0'(1+\cos^2\theta),
$$
a distribution rotationally symmetric about the $z$ axis. The degree of polarization of the scattered light varies with the scattering angle: along the direction of incidence ($\theta=0,\pi$) the scattered light is still unpolarized; perpendicular to the direction of incidence ($\theta=90^\circ$) it is linearly polarized with vibration perpendicular to the scattering plane (the plane formed by the directions of incidence and scattering); in other directions it is partially polarized, with degree of polarization $P=\frac{\sin^2\theta}{1+\cos^2\theta}$.

![Angular distribution of Rayleigh-scattered intensity (polar plot). Left: linearly polarized light with vibration along y incident, I ∝ sin²ψ, no scattering along the direction of vibration; middle: unpolarized light incident along z, I ∝ 1 + cos²θ; right: degree of polarization of the scattered light for unpolarized incident light, P = sin²θ / (1 + cos²θ), equal to 1 at θ = 90°](./plots/rayleigh-scattering.py)

The scattered light from a clear sky is therefore partially polarized, and the degree of polarization is greatest in the part of the sky at $90^\circ$ to the direction of the Sun. Bees and some birds can sense the polarization of skylight and use it to find direction. Multiple scattering scrambles the polarization direction of single scattering and lowers the degree of polarization, so the polarization of skylight is small on overcast days and near the horizon.

## 3.5. Birefringence

### 3.5.1. The Phenomenon of Birefringence

Looking at writing on paper through a calcite crystal, one sees two images; this was discovered by Bartholin in 1669.

**Definition 3.5.1 (Birefringence)** The phenomenon that a beam of light entering an anisotropic crystal splits into two refracted beams is called **birefringence** (double refraction). One of the beams obeys the law of refraction and is called the **ordinary ray** (o ray); the other generally does not obey the law of refraction and is called the **extraordinary ray** (e ray).

- o ray: $n_1\sin i=n_{\mathrm{o}}\sin r_{\mathrm{o}}$; the index $n_{\mathrm{o}}$ is independent of the direction of incidence, and the refracted ray lies in the plane of incidence.
- e ray: $\sin i/\sin r_{\mathrm{e}}$ varies with the direction of incidence, and the refracted ray does not necessarily lie in the plane of incidence; even at normal incidence the e ray is generally deflected.

When the calcite is rotated about the incident ray, the image of the o ray stays fixed and the image of the e ray rotates around it. Observing the two beams through a polarizing sheet and rotating the sheet through a full turn, the two images are extinguished alternately, with the extinction directions differing by $90^\circ$: the o and e rays are both linearly polarized, with mutually perpendicular directions of vibration.

### 3.5.2. Optic Axis and Principal Plane

**Definition 3.5.2 (Optic Axis)** A special direction in a crystal along which light propagates without birefringence is called the **optic axis** of the crystal. A crystal with only one optic-axis direction is called uniaxial (such as calcite, quartz, ice), and one with two optic-axis directions is called biaxial (such as mica, sulfur, gypsum).

The optic axis is a direction, not a line: every line in the crystal parallel to this direction is an optic axis. A calcite crystal is a rhombohedron bounded by six parallelograms (obtuse angle about $102^\circ$, acute angle about $78^\circ$); it has two vertices formed by three obtuse face angles, and the direction drawn from one of these vertices making equal angles with the three edges is the optic axis.

**Definition 3.5.3 (Principal Plane)** The plane formed by the direction of propagation of a ray in a crystal and the optic axis is called the **principal plane** of that ray.

Experiment shows that the direction of vibration of the o ray is perpendicular to its principal plane and that of the e ray lies in its principal plane. The principal planes of the o and e rays generally do not coincide; when the optic axis lies in the plane of incidence, the o-ray principal plane, the e-ray principal plane and the plane of incidence coincide, and the directions of vibration of the o and e rays are then exactly perpendicular.

### 3.5.3. Principal Refractive Indices and Positive and Negative Crystals

Birefringence originates in the anisotropy of the dielectric properties of the crystal. As discussed in [5.3.4](/5.3.4#sec-4.2.5), the **electric susceptibility** of an anisotropic **linear dielectric** is a **symmetric matrix**, which is diagonal in the principal-axis frame of the crystal, and correspondingly the **relative permittivity** also has three principal values (three **eigenvalues**). In a uniaxial crystal two of the principal values are equal: taking the optic axis as the $z$ axis,

$$
\varepsilon_{\mathrm{r}}=\begin{bmatrix}\varepsilon_\perp&0&0\\0&\varepsilon_\perp&0\\0&0&\varepsilon_\parallel\end{bmatrix},
$$
where $\varepsilon_\perp$ and $\varepsilon_\parallel$ are the relative permittivities (at optical frequencies) for the electric field perpendicular and parallel to the optic axis. The speed of light is $v=c/\sqrt{\varepsilon_{\mathrm{r}}}$ (nonmagnetic medium, $\mu_{\mathrm{r}}\approx1$), so the speed of propagation differs for different angles between the light vector and the optic axis. The direction of vibration of the o ray is always perpendicular to the optic axis, and its speed is $v_{\mathrm{o}}=c/\sqrt{\varepsilon_\perp}$ in all directions; the angle between the direction of vibration of the e ray and the optic axis varies with the direction of propagation and so does its speed: for propagation along the optic axis the vibration is perpendicular to the axis and the speed is $v_{\mathrm{o}}$, and for propagation perpendicular to the optic axis the vibration is parallel to the axis and the speed is $v_{\mathrm{e}}=c/\sqrt{\varepsilon_\parallel}$. The three principal values of a biaxial crystal are all different.

**Definition 3.5.4** In a uniaxial crystal, $n_{\mathrm{o}}=c/v_{\mathrm{o}}$ and $n_{\mathrm{e}}=c/v_{\mathrm{e}}$ are called the principal refractive indices of the crystal, where $v_{\mathrm{e}}$ is the speed of the e ray propagating perpendicular to the optic axis. A crystal with $n_{\mathrm{o}}<n_{\mathrm{e}}$ ($v_{\mathrm{o}}>v_{\mathrm{e}}$) is called a **positive crystal**, such as quartz or ice; a crystal with $n_{\mathrm{o}}>n_{\mathrm{e}}$ ($v_{\mathrm{o}}<v_{\mathrm{e}}$) is called a **negative crystal**, such as calcite or ruby.

| Crystal | $n_{\mathrm{o}}$ | $n_{\mathrm{e}}$ | Type |
|---|---|---|---|
| Calcite | $1.6584$ | $1.4864$ | Negative |
| Quartz | $1.5443$ | $1.5534$ | Positive |
| Ice | $1.309$ | $1.313$ | Positive |

(Values for sodium yellow light, $589.3\,\mathrm{nm}$.)

By **Huygens' principle**, in a crystal the **wave surface** of the o-ray wavelets from a point source is a sphere (radius $v_{\mathrm{o}}t$), and the wave surface of the e-ray wavelets is an ellipsoid of revolution about the optic axis; the two touch along the optic axis. For a positive crystal the e-ray ellipsoid lies inside the sphere and for a negative crystal outside it, the semi-axis of the ellipsoid perpendicular to the optic axis being $v_{\mathrm{e}}t$.

### 3.5.4. Huygens Construction in Uniaxial Crystals

The Huygens construction gives the directions of propagation of the o and e rays in a crystal: draw the o and e wavelet surfaces emitted as the incident wave surface reaches the points of the crystal surface; their envelopes are the new wave surfaces of the o and e rays, and the line joining a wavelet source to the point of tangency is the ray direction. Take a negative crystal as an example:

1. Optic axis parallel to the crystal surface, unpolarized light at normal incidence: the wave surfaces of both the o and e rays are parallel to the surface, and the two beams continue in the original direction without separating in direction, but with different speeds ($v_{\mathrm{e}}>v_{\mathrm{o}}$). This is still birefringence, and the wave plates of Section 3.6 make use of it.
2. Optic axis parallel to the crystal surface and perpendicular to the plane of incidence, unpolarized light at oblique incidence: the section of the e-ray wavelet in the plane of incidence is then a circle (radius $v_{\mathrm{e}}t$), and the e ray also obeys the **law of refraction**, $\sin i/\sin r_{\mathrm{o}}=n_{\mathrm{o}}$ and $\sin i/\sin r_{\mathrm{e}}=n_{\mathrm{e}}$ (with air as the incident medium).
3. Optic axis oblique to the crystal surface, unpolarized light at normal incidence: the o ray goes straight on, while for the e ray the common tangent plane of the wavelet ellipsoids is parallel to the surface but the point of tangency is displaced from directly below the wavelet source, so the e ray deviates from the original direction; this is why two images are seen even at normal incidence. The wave surface of the e ray is then no longer perpendicular to its ray.

### 3.5.5. Polarizing Prisms

Birefringence can be used to obtain high-quality linearly polarized light from unpolarized light.

- Glan–Thompson prism: a calcite block is cut along a diagonal plane and cemented with Canada balsam ($n=1.55$). The orientation of the optic axis is such that the e ray obeys the law of refraction at the interface with the corresponding index $n_{\mathrm{e}}$. Since $n_{\mathrm{o}}=1.6584>1.55>n_{\mathrm{e}}=1.4864$, the o ray reaching the balsam layer is incident beyond the critical angle (about $69^\circ$) and undergoes **total internal reflection**, and it is absorbed by an absorbing coating on the side face; the e ray is transmitted and the exiting light is linearly polarized. Its extinction ratio is high, but the balsam absorbs ultraviolet light and cannot withstand intense laser light.
- Wollaston prism: two right-angle calcite prisms with mutually perpendicular optic axes are cemented together. Light at normal incidence on the first prism has its o and e rays traveling in the same direction; on entering the second prism, because the optic axis has turned through $90^\circ$, the o ray of the first becomes the e ray of the second and the e ray becomes the o ray. For a negative crystal, the former passes from $n_{\mathrm{o}}$ to $n_{\mathrm{e}}$ and bends away from the normal, and the latter passes from $n_{\mathrm{e}}$ to $n_{\mathrm{o}}$ and bends toward the normal, so two linearly polarized beams with mutually perpendicular directions of vibration emerge, symmetrically separated. Since the optic axes of both blocks are perpendicular to the ray, both beams refract at the interface according to the ordinary law of refraction.

## 3.6. Elliptically and Circularly Polarized Light

### 3.6.1. Phase Retardation of a Crystal Plate

By Section 3.1.3, two mutually perpendicular linearly polarized beams with a constant phase difference combine into elliptically or circularly polarized light. A crystal plate provides two such beams.

**Definition 3.6.1** A thin slice of a uniaxial crystal whose optic axis is parallel to its surface is called a crystal plate (retardation plate).

Light incident normally on a plate of thickness $d$ behaves as in the first case of Section 3.5.4: the o and e rays travel in the same direction at different speeds. On exit their **optical path difference** is $(n_{\mathrm{o}}-n_{\mathrm{e}})d$ and their phase difference is

$$
\Delta\varphi=\frac{2\pi}{\lambda}(n_{\mathrm{o}}-n_{\mathrm{e}})d,
\tag{3.3}
$$
where $\lambda$ is the vacuum wavelength. After exit the o and e rays merge into one beam whose state of polarization depends on the state of polarization and wavelength of the incident light, and on the thickness, principal refractive indices and optic-axis orientation of the plate.

### 3.6.2. Wave Plates

**Definition 3.6.2 (Wave Plate)** A crystal plate designed for a specific wavelength so as to produce a specific phase difference between the o and e rays is called a **wave plate**.

- **Quarter-wave plate**: $\lvert n_{\mathrm{o}}-n_{\mathrm{e}}\rvert d=\lambda/4$, $\lvert\Delta\varphi\rvert=\pi/2$;
- **Half-wave plate**: $\lvert n_{\mathrm{o}}-n_{\mathrm{e}}\rvert d=\lambda/2$, $\lvert\Delta\varphi\rvert=\pi$;
- **Full-wave plate**: $\lvert n_{\mathrm{o}}-n_{\mathrm{e}}\rvert d=\lambda$, $\lvert\Delta\varphi\rvert=2\pi$.

More generally, a plate with optical path difference $(2k+1)\lambda/4$ also acts as a quarter-wave plate, and similarly for the others. A wave plate with only the minimum thickness is called a zero-order wave plate and is not very sensitive to changes of wavelength and temperature. For calcite $\lvert n_{\mathrm{o}}-n_{\mathrm{e}}\rvert\approx0.17$, so a zero-order quarter-wave plate for $589\,\mathrm{nm}$ would be only about $0.86\,\mu\mathrm{m}$ thick and hard to fabricate; practical wave plates are therefore mostly made of quartz or mica, which have weaker birefringence.

### 3.6.3. Linearly Polarized Light Through a Wave Plate

Let linearly polarized light of amplitude $A$ be incident normally on a wave plate with its direction of vibration at angle $\theta$ to the optic axis (taken as the $x$ axis). The direction of vibration of the e ray is parallel to the optic axis and that of the o ray is perpendicular to it; at the front surface of the plate they are in phase:

$$
A_{\mathrm{e}}=A\cos\theta,\qquad A_{\mathrm{o}}=A\sin\theta.
$$
At the back surface of the plate they have the phase difference of Eq. (3.3).

Quarter-wave plate: $\lvert\Delta\varphi\rvert=\pi/2$, and the two components combine into upright elliptically polarized light with the optic axis as a principal axis. At $\theta=0$ or $90^\circ$ there is only one component and the exiting light is still linearly polarized; at $\theta=45^\circ$, $A_{\mathrm{o}}=A_{\mathrm{e}}$ and the exiting light is circularly polarized. The handedness is determined by the sign of $\theta$ and the sign of the crystal.

| Incident light | Optic-axis orientation | After a quarter-wave plate |
|---|---|---|
| Linearly polarized | Parallel or perpendicular to the direction of vibration | Linearly polarized |
| Linearly polarized | At $45^\circ$ to the direction of vibration | Circularly polarized |
| Linearly polarized | Other orientations | Elliptically polarized |
| Circularly polarized | Any | Linearly polarized (at $45^\circ$ to the optic axis) |
| Elliptically polarized | Parallel to a principal axis of the ellipse | Linearly polarized |
| Elliptically polarized | Other orientations | Elliptically polarized |

The last three rows are the reverse of the first: the principal-axis components of circularly polarized or upright elliptically polarized light already have a phase difference of $\pm\pi/2$, and adding (or subtracting) $\pi/2$ makes the phase difference $0$ or $\pi$, which is linearly polarized light.

Half-wave plate: $\Delta\varphi=\pm\pi$, and on exit the o component is reversed relative to the e component,

$$
\boldsymbol{E}_{\mathrm{in}}\propto A_{\mathrm{e}}\boldsymbol{e}_x+A_{\mathrm{o}}\boldsymbol{e}_y\quad\longrightarrow\quad\boldsymbol{E}_{\mathrm{out}}\propto A_{\mathrm{e}}\boldsymbol{e}_x-A_{\mathrm{o}}\boldsymbol{e}_y,
$$
that is, the exiting light is still linearly polarized, with its direction of vibration reflected about the optic axis and so rotated through the angle $2\theta$. A half-wave plate can therefore turn the plane of vibration of linearly polarized light to any direction (through $90^\circ$ at $\theta=45^\circ$); for circularly polarized light, a half-wave plate turns right-handed into left-handed and vice versa.

### 3.6.4. Analyzing with a Quarter-Wave Plate

Several kinds of light that cannot be distinguished with a polarizing sheet alone (Section 3.2.3) can be distinguished by adding a quarter-wave plate:

- Unpolarized and circularly polarized light: let the light pass first through a quarter-wave plate and then analyze it with a polarizing sheet. Unpolarized light is still unpolarized after the plate, and the intensity does not change as the sheet is rotated; circularly polarized light becomes linearly polarized after the plate, and there is extinction as the sheet is rotated.
- Partially polarized and elliptically polarized light: first find with a polarizing sheet the direction of maximum (or minimum) intensity, place the optic axis of the quarter-wave plate along this direction, and analyze again with the sheet. The principal axes of elliptically polarized light lie along these directions and the light becomes linearly polarized after the plate, with extinction; partially polarized light is still partially polarized after the plate, without extinction.

## 3.7. Interference of Polarized Light

### 3.7.1. Setup and Amplitude Relations

Two beams can interfere only if they satisfy the **coherence conditions**, one of which is that the directions of vibration be the same. The directions of vibration of the o and e rays are mutually perpendicular, so they cannot interfere even with a constant phase difference; only when a polarizing sheet projects them onto the same direction can interference be observed.

The setup places a crystal plate $C$ with its optic axis parallel to the surface between two polarizing sheets $P_1$ and $P_2$. In what follows let the transmission axes of $P_1$ and $P_2$ be crossed and the optic axis of the plate make an angle $\theta$ with the transmission axis of $P_1$. Let the amplitude of the linearly polarized light passing through $P_1$ be $A_1$; on entering the plate it splits into

$$
A_{\mathrm{e}}=A_1\cos\theta,\qquad A_{\mathrm{o}}=A_1\sin\theta.
$$
On passing through $P_2$ only the components along the transmission axis of $P_2$ get through:

$$
A_{2\mathrm{e}}=A_{\mathrm{e}}\sin\theta=A_1\sin\theta\cos\theta,\qquad A_{2\mathrm{o}}=A_{\mathrm{o}}\cos\theta=A_1\sin\theta\cos\theta,
$$
and the two transmitted beams have equal amplitudes, the same direction of vibration and a constant phase difference: they are **coherent light**.

### 3.7.2. Phase Relation and Interference Conditions

The phase difference of the two beams has two parts: $\Delta\varphi_C=\frac{2\pi}{\lambda}(n_{\mathrm{o}}-n_{\mathrm{e}})d$ produced by the plate, and an additional phase difference of $\pi$ that may arise on projection onto $P_2$. When $P_1$ and $P_2$ are crossed, the projections of $\boldsymbol{A}_{\mathrm{o}}$ and $\boldsymbol{A}_{\mathrm{e}}$ onto the direction of $P_2$ are opposite, giving an additional phase difference $\pi$; when $P_1$ and $P_2$ are parallel the two projections point the same way and there is no additional phase difference. For crossed sheets the total phase difference is therefore

$$
\Delta\varphi=\frac{2\pi}{\lambda}(n_{\mathrm{o}}-n_{\mathrm{e}})d+\pi,
$$
and the transmitted intensity is

$$
I=4A_{2\mathrm{o}}^2\cos^2\frac{\Delta\varphi}{2}=I_1\sin^22\theta\,\sin^2\frac{\Delta\varphi_C}{2},\qquad I_1=A_1^2.
$$

- Constructive interference: $\Delta\varphi=2k\pi$, that is, $\lvert n_{\mathrm{o}}-n_{\mathrm{e}}\rvert d=(2k-1)\dfrac\lambda2$, $k=1,2,\dots$ (the plate acts as a half-wave plate);
- Destructive interference: $\Delta\varphi=(2k+1)\pi$, that is, $\lvert n_{\mathrm{o}}-n_{\mathrm{e}}\rvert d=k\lambda$, $k=0,1,2,\dots$ (the plate acts as a full-wave plate, or there is no plate).

Interference is most pronounced at $\theta=45^\circ$. When $P_1$ and $P_2$ are parallel, $I=I_1\big(1-\sin^22\theta\sin^2\frac{\Delta\varphi_C}{2}\big)$, complementary to the intensity for crossed sheets, the two summing to $I_1$.

### 3.7.3. Interference Patterns and Chromatic Polarization

- Plate of uniform thickness: with monochromatic light the intensity is the same everywhere on the screen and there are no fringes; rotating any of $P_1$, $P_2$ or $C$ changes the intensity. With white light, wavelengths satisfying the destructive condition are removed and the transmitted light shows its complementary color; rotating $P_2$ or the plate changes the color, and a rotation of $P_2$ through $90^\circ$ changes the color to its complement.

  **Definition 3.7.1 (Chromatic Polarization)** The phenomenon that white light shows colors after passing through a polarizing sheet, a crystal plate and a polarizing sheet is called **chromatic polarization**.

  Chromatic polarization is very sensitive to the birefringence of the plate, and the polarizing microscope uses it to identify minerals and crystals and to observe ordered structures in biological tissue.
- Plate of nonuniform thickness (for example, a quartz **wedge film**): with monochromatic light, points of equal thickness have the same optical path difference, and bright and dark fringes similar to those of **fringes of equal thickness** appear on the screen; with white light colored fringes appear.

## 3.8. Artificial Birefringence

Isotropic substances can become anisotropic under external action and then show birefringence; this is called artificial birefringence.

### 3.8.1. The Photoelastic Effect

**Definition 3.8.1 (Photoelastic Effect)** The phenomenon that a transparent isotropic material (such as glass, acrylic or epoxy resin) becomes optically anisotropic and birefringent under mechanical stress is called the **photoelastic effect** (stress birefringence).

Within a certain range of stress the material behaves like a uniaxial crystal with its optic axis along the stress, and the difference of the two principal refractive indices is proportional to the stress:

$$
n_{\mathrm{o}}-n_{\mathrm{e}}=k\frac{F}{S},
$$
where $F/S$ is the stress and $k$ is a constant determined by the material. A sample of thickness $d$ placed between crossed polarizing sheets has, by Section 3.7.2, the phase difference $\Delta\varphi=\frac{2\pi}{\lambda}kd\frac{F}{S}+\pi$. The stress differs from place to place in the material and so does the phase difference, giving interference fringes; where the fringes are denser, the stress varies more. In engineering, models of machine parts or building structures are made of transparent material, and the fringes observed under load are used to analyze the stress distribution; this is the photoelastic method. Residual stress in glass products can also be checked this way.

### 3.8.2. The Kerr Effect

**Definition 3.8.2 (Kerr Effect)** The phenomenon that some isotropic transparent media in an applied electric field become uniaxial crystals with the optic axis along the field, the difference of the two principal refractive indices being proportional to the square of the field strength, is called the **Kerr effect** (quadratic electro-optic effect); it was discovered by Kerr in 1875:

$$
n_{\parallel}-n_{\perp}=\lambda KE^2,
$$
where $K$ is called the Kerr constant.

A Kerr cell is a container of liquid (such as nitrobenzene) with a pair of parallel-plate electrodes of separation $d$ and length $l$, placed between two crossed polarizing sheets, with the electric field at $45^\circ$ to the transmission axes of both sheets. With no voltage the liquid is isotropic and $P_2$ transmits no light; with a voltage $U$ the liquid becomes birefringent and $P_2$ transmits light. The phase difference of the o and e rays is

$$
\Delta\varphi_C=\frac{2\pi}{\lambda}(n_{\parallel}-n_{\perp})l=2\pi lK\frac{U^2}{d^2}.
$$
At $\Delta\varphi_C=\pi$ the Kerr cell acts as a half-wave plate and transmits the most light. For nitrobenzene $K\approx2.4\times10^{-12}\,\mathrm{m\,V^{-2}}$; with $l=3\,\mathrm{cm}$ and $d=0.8\,\mathrm{cm}$ the required voltage is $U=d/\sqrt{2lK}\approx2\times10^4\,\mathrm{V}$.

### 3.8.3. The Pockels Effect

**Definition 3.8.3 (Pockels Effect)** The phenomenon that in some crystals in an applied electric field the change in birefringence is proportional to the field strength is called the **Pockels effect** (linear electro-optic effect); it was studied by Pockels in 1893.

The linear electro-optic effect exists only in crystals without a center of symmetry; commonly used ones are potassium dihydrogen phosphate $\ce{KH2PO4}$ (KDP), ammonium dihydrogen phosphate $\ce{NH4H2PO4}$ (ADP) and lithium niobate $\ce{LiNbO3}$. In a Pockels cell, the optic axis of a uniaxial electro-optic crystal lies along the direction of propagation of the light, and the voltage $U$ is applied along this direction to transparent electrodes. With no voltage the light travels along the optic axis, there is no birefringence, and no light passes between crossed polarizing sheets; with a voltage the crystal becomes biaxial and birefringence appears along the original optic-axis direction, with phase difference

$$
\Delta\varphi_C=\frac{2\pi}{\lambda}n_{\mathrm{o}}^3rU,
$$
where $r$ is the electro-optic coefficient. For KDP, $n_{\mathrm{o}}=1.51$ and $r=10.6\times10^{-12}\,\mathrm{m/V}$; for green light of $\lambda=546\,\mathrm{nm}$ the half-wave voltage needed to produce $\Delta\varphi_C=\pi$ is $U=\frac{\lambda}{2n_{\mathrm{o}}^3r}\approx7.5\times10^3\,\mathrm{V}$.

### 3.8.4. Applications of Electro-Optic Effects

The response time of electro-optic effects is extremely short (about $10^{-9}\,\mathrm{s}$ for a Kerr cell and even shorter for a Pockels cell), and a voltage can switch light on and off and control its intensity; they are used as high-speed optical switches and modulators, in high-speed photography, laser ranging and optical communication, and as Q-switches in pulsed lasers. Nitrobenzene is toxic and explosive and a Kerr cell needs a high voltage of tens of thousands of volts, so Kerr cells are rarely used now; Pockels cells and lithium-niobate integrated electro-optic modulators are common devices in laser technology and fiber-optic communication. Liquid-crystal displays use an applied electric field to change the orientation of the liquid-crystal molecules and thereby their effect on polarized light.

## 3.9. Optical Activity

### 3.9.1. Optical Activity of Substances

In 1811 Arago found that after linearly polarized light passes through a quartz crystal along the optic axis, its plane of vibration is rotated through some angle.

**Definition 3.9.1 (Optical Activity)** The property of some substances that the plane of vibration of linearly polarized light is rotated after passing through them is called **optical activity**, and such substances are called optically active.

Experiment shows that the angle $\theta$ through which the plane of vibration turns is proportional to the distance $l$ traveled by the light in the optically active substance,

$$
\theta=\alpha l,
$$
where $\alpha$ is called the specific rotation rate and depends on the substance and the wavelength (roughly inversely proportional to $\lambda^2$, so after white light passes through an optically active substance the planes of vibration of the various colors turn through different angles and colors appear behind the analyzer; this is called optical rotatory **dispersion**). For example, the rotation rate of quartz for sodium yellow light is about $21.7^\circ/\mathrm{mm}$. For solutions the angle is also proportional to the concentration $c$, $\theta=[\alpha]cl$, where $[\alpha]$ is called the specific rotation. A polarimeter that measures the angle can therefore determine the concentration of a solution, for example of sugar solutions in the sugar industry (a saccharimeter).

Common optically active substances are quartz, sodium chlorate, turpentine, lactic acid and aqueous solutions of sugar. The same substance can be left- or right-handed: looking toward the source, a substance that turns the plane of vibration counterclockwise is called levorotatory and one that turns it clockwise is called dextrorotatory. The crystal structures of left- and right-handed quartz are mirror images of each other; the optical activity of molecules comes from the chirality of the molecules themselves, whose left- and right-handed forms are mirror images that cannot be superposed, called enantiomers in chemistry; they have the same molecular composition and chemical bonds, and rotate in opposite directions through equal angles.

### 3.9.2. Fresnel's Phenomenological Explanation

In 1825 Fresnel gave a phenomenological explanation of natural optical activity. By Section 3.1.3, linearly polarized light can be regarded as the superposition of left- and right-handed circularly polarized light of the same frequency and equal amplitude with a definite phase relation. Suppose that in the optically active substance the refractive indices $n_{\mathrm{L}}$ and $n_{\mathrm{R}}$ for left- and right-handed circularly polarized light differ (circular birefringence). After passing through a length $l$ of the substance, the phases of the two lag by

$$
\Delta\varphi_{\mathrm{L}}=\frac{2\pi}{\lambda}n_{\mathrm{L}}l,\qquad \Delta\varphi_{\mathrm{R}}=\frac{2\pi}{\lambda}n_{\mathrm{R}}l.
$$
Looking toward the source, the light vector of the right-handed component rotates clockwise, and a phase lag $\Delta\varphi_{\mathrm{R}}$ means it has turned that much less, that is, it is deflected counterclockwise by $\Delta\varphi_{\mathrm{R}}$ relative to its state at the entrance; the left-handed component is deflected clockwise by $\Delta\varphi_{\mathrm{L}}$. The resultant linearly polarized light lies along the bisector of the two circular light vectors, so the plane of vibration turns counterclockwise through

$$
\theta=\frac12(\Delta\varphi_{\mathrm{R}}-\Delta\varphi_{\mathrm{L}})=\frac{\pi}{\lambda}(n_{\mathrm{R}}-n_{\mathrm{L}})l,
$$
and for $n_{\mathrm{R}}>n_{\mathrm{L}}$ the substance is levorotatory, for $n_{\mathrm{R}}<n_{\mathrm{L}}$ dextrorotatory. The rotation rate $\alpha=\pi(n_{\mathrm{R}}-n_{\mathrm{L}})/\lambda$ both explains optical activity and shows that the rotation rate depends on the substance and the wavelength. For quartz $\lvert n_{\mathrm{R}}-n_{\mathrm{L}}\rvert$ is only about $7\times10^{-5}$, much smaller than its linear birefringence, so it shows only for propagation along the optic axis. Fresnel also used three quartz prisms to split a linearly polarized beam into left- and right-handed circularly polarized beams, confirming this hypothesis.

### 3.9.3. The Faraday Effect

**Definition 3.9.2 (Faraday Effect)** The phenomenon that the plane of vibration of linearly polarized light is rotated when it passes through some transparent substances along the direction of a magnetic field is called the **Faraday effect** (magneto-optical rotation); it was discovered by Faraday in 1845. The angle is proportional to the magnetic flux density $B$ and the distance $l$ traveled by the light in the substance:

$$
\theta=VBl,
$$
where $V$ is called the Verdet constant and depends on the substance and the wavelength.

Glass, water, carbon disulfide, rock salt, ethanol and others show magneto-optical rotation. For visible light the Verdet constants of water and ordinary glass are a few radians per tesla per meter, that of heavy flint glass is tens of radians, and the terbium gallium garnet (TGG) crystal used specifically for magneto-optical devices can reach more than a hundred radians. The Faraday effect was the first experimental evidence connecting light and magnetism; it showed that light is related to electromagnetic phenomena, twenty years before Maxwell's electromagnetic theory.

There is an important difference between natural and magnetic optical rotation:

- The handedness of natural optical rotation is determined by the substance itself and is independent of the direction of propagation of the light (looking toward the source it is always the same sense). Linearly polarized light that passes through a naturally active substance and is reflected back along the same path has the rotations of its plane of vibration cancel and returns to its original direction.
- The handedness of magnetic optical rotation is determined by the direction of the magnetic field: for light propagating along $\boldsymbol{B}$ and against $\boldsymbol{B}$, the senses looking toward the source are opposite, but relative to $\boldsymbol{B}$ the sense of rotation is the same. Linearly polarized light that returns along the same path after passing through does not have its rotation canceled but doubled. Magneto-optical rotation is nonreciprocal.

This nonreciprocity can be used to make an optical isolator: behind a polarizing sheet $P$ place a magneto-optically active substance, with the magnetic field and length chosen so that $\theta=45^\circ$. Linearly polarized light passing through $P$ is turned through $45^\circ$ in the active substance; after being reflected back by a later element it is turned through another $45^\circ$, $90^\circ$ in all, so its direction of vibration is perpendicular to the transmission axis of $P$ and it cannot pass through $P$. Light is thus allowed to pass in one direction only, which removes the interference of reflected light with sources such as lasers. Optical isolators are common devices in laser systems and fiber-optic communication.

## Summary

| Topic | Key points |
|---|---|
| States of polarization | Linear ($\Delta\varphi=0,\pi$), circular ($\Delta\varphi=\pm\pi/2$, equal amplitudes), elliptical; unpolarized light; partially polarized light, degree of polarization $P=I_{\mathrm{p}}/I_{\mathrm{t}}$ |
| Malus's law | $I=I_0\cos^2\alpha$; after a polarizing sheet unpolarized light has $I=I_0/2$ |
| Reflection and refraction | The s component predominates in reflection; Brewster's angle $\tan i_{\mathrm{B}}=n_2/n_1$, $i_{\mathrm{B}}+r_{\mathrm{B}}=90^\circ$, the reflected light is s light |
| Scattering | Rayleigh scattering $I\propto\lambda^{-4}$; for unpolarized incident light $I\propto1+\cos^2\theta$, and light scattered at $90^\circ$ is linearly polarized |
| Birefringence | The o ray obeys the law of refraction, with vibration perpendicular to the principal plane; the e ray generally does not, with vibration in the principal plane; positive crystals $n_{\mathrm{o}}<n_{\mathrm{e}}$, negative crystals $n_{\mathrm{o}}>n_{\mathrm{e}}$ |
| Wave plates | $\Delta\varphi=2\pi(n_{\mathrm{o}}-n_{\mathrm{e}})d/\lambda$; a quarter-wave plate turns $45^\circ$ linearly polarized light into circularly polarized light; a half-wave plate turns the plane of vibration through $2\theta$ |
| Interference of polarized light | Between crossed polarizing sheets $I=I_1\sin^22\theta\sin^2(\Delta\varphi_C/2)$; chromatic polarization with white light |
| Artificial birefringence | Photoelastic effect $n_{\mathrm{o}}-n_{\mathrm{e}}\propto F/S$; Kerr effect $\Delta n=\lambda KE^2$; Pockels effect $\Delta\varphi=2\pi n_{\mathrm{o}}^3rU/\lambda$ |
| Optical rotation | Natural $\theta=\alpha l$, $\alpha=\pi(n_{\mathrm{R}}-n_{\mathrm{L}})/\lambda$, canceled on a round trip; Faraday effect $\theta=VBl$, doubled on a round trip |

## Questions

1. How can one distinguish the two kinds of partially polarized light, "unpolarized + elliptically polarized" and "unpolarized + linearly polarized"? Hint: with a polarizing sheet alone, both show varying intensity without extinction. First find with the sheet the direction of maximum intensity, place the optic axis of a quarter-wave plate along this direction, and rotate the sheet again. For the latter, the direction of vibration of the linearly polarized part lies along the optic axis and is unchanged by the plate, so the direction of maximum intensity does not change; for the former, the major axis of the elliptically polarized part lies along the optic axis and the plate turns it into linearly polarized light oblique to the optic axis, so the direction of maximum intensity turns through some angle.
2. How can one distinguish partially polarized light consisting of "unpolarized + circularly polarized" light from unpolarized light? Hint: first pass it through a quarter-wave plate of any orientation, which turns the circularly polarized part into linearly polarized light, and then rotate a polarizing sheet: the intensity of unpolarized light stays constant, while that of the partially polarized light varies without extinction.
3. What happens when circularly polarized light passes through a half-wave plate? Hint: it is still circularly polarized, but the handedness is reversed.
4. Is there necessarily no birefringence when unpolarized light enters a crystal along the optic axis? Hint: when light propagates along the optic axis inside the crystal, the o and e rays have the same speed and there is no birefringence. But if the light strikes the crystal surface obliquely, after refraction its direction of propagation in the crystal is no longer along the optic axis, and birefringence still occurs. In addition, in an optically active crystal such as quartz there is "circular birefringence" of left- and right-handed circularly polarized light for propagation along the optic axis (Section 3.9.2).
5. Asphalt roads in summer sunlight give a dazzling glare. Can polarizing glasses replace ordinary sunglasses, and what is the advantage? Hint: the s component (horizontal vibration) predominates in the light reflected from the road, and polarizing glasses with a vertical transmission axis selectively weaken the glare, while the diffuse light from other objects is reduced by only about half, so one sees more clearly.
6. Why is the sky blue? Why is the Sun red at sunrise and sunset? Hint: see Section 3.4.2.
