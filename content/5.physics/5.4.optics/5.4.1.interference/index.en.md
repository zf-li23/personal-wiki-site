---
title: Interference of Light
description: The branches of optics and the debate over the nature of light; Young's double-slit interference, coherent light and fringe visibility, temporal and spatial coherence, optical path length, fringes of equal thickness (wedge, Newton's rings) and of equal inclination, anti-reflection coatings, and the Michelson interferometer.
source_hash: 029734f46965
---

Optics studies the production and propagation of light and its interaction with matter. It is usually divided into three parts. Geometrical optics rests on the rectilinear propagation of light, reflection and the **law of refraction**, and treats imaging instruments. Wave optics studies the wave nature of light: interference, **diffraction** and polarization. Quantum optics builds on the quantum theory of light and studies how light interacts with matter. The nature of light was debated for a long time from the seventeenth century on. Newton favored the corpuscular theory, explaining reflection and refraction by forces acting on light particles and deriving that light travels faster in water than in air. In his *Treatise on Light* of 1690, Huygens proposed the wave theory and explained reflection and refraction with a construction of secondary wavelets (**Huygens' principle**), concluding that light travels more slowly in water. Grimaldi observed diffraction in the middle of the seventeenth century (his book appeared in 1665), and in 1676 Rømer inferred from the timing of the eclipses of Jupiter's moons that the speed of light is finite. In the early nineteenth century Young demonstrated the interference of light with his double-slit (double-pinhole) experiment, and Fresnel combined the principle of interference with the wavelet construction to explain diffraction quantitatively. In 1818 Poisson deduced from Fresnel's theory that a bright spot should appear at the center of the shadow of a circular disk, and Arago promptly observed it. In 1850 Foucault measured a lower speed of light in water than in air, which settled the debate. In 1865 Maxwell predicted **electromagnetic waves** from his electromagnetic theory, computed that their speed equals the speed of light, and concluded that light is an **electromagnetic wave**; Hertz produced such waves experimentally in 1887–1888. At the beginning of the twentieth century, blackbody radiation and the photoelectric effect revealed the particle nature of light ([5.5.1](/5.5.1)): light has both wave and particle aspects.

This chapter and the next two deal only with wave optics. Light is an electromagnetic wave, and it is mainly the electric field that causes vision and photosensitive effects, so the **electric field strength** $\boldsymbol{E}$ is called the light vector. The vacuum **wavelength** of visible light is about $400$–$760\,\mathrm{nm}$ and its frequency is about $10^{15}\,\mathrm{Hz}$. No detector (eye, film, photocell) can follow oscillations this fast; what is measured is only the time average of the **wave intensity** (light intensity), $I\propto\overline{E^2}$, which we write $I=E_0^2$ when only relative intensities in the same medium are compared. Interference is a property common to all waves, and [5.1.7](/5.1.7#sec-7.7) has already treated the superposition principle, **interference**, the **coherence conditions** and **standing waves**. Optical interference deserves a chapter of its own because the light of ordinary sources hardly satisfies the **coherence conditions**, which raises new questions of temporal and spatial coherence. We begin with Young's double-slit interference (Section 1.1), then discuss how to obtain coherent light (1.2) and how the monochromaticity and width of the source limit interference (1.3, 1.4). Next we introduce optical path length (1.5) and use it to analyze fringes of equal thickness and of equal inclination in thin films (1.6, 1.7) and the Michelson interferometer (1.8). Mathematically, computing interference means superposing oscillations of the same frequency, which is most convenient with **phasors** or **complex numbers** ([5.1.6](/5.1.6#sec-6.2)), and the relation between coherence and the spectrum is a physical manifestation of the **Fourier transform**. Diffraction in the next chapter, [5.4.2](/5.4.2), is the interference of infinitely many wavelets, and [5.4.3](/5.4.3) discusses the direction of the light vector (polarization).

## 1.1. Young's Double-Slit Interference

### 1.1.1. Setup and Path Difference

A monochromatic source $S$ illuminates a narrow slit, and the light leaving it falls on two parallel slits $S_1$ and $S_2$. On a distant screen we obtain alternating bright and dark straight fringes. Let the slit separation be $d$, the distance from the slits to the screen $D$, the distance from a point $P$ on the screen to the center $O$ of the screen $x$, and the angle that $P$ subtends at the midpoint of the slits $\theta$. In real setups $d\sim10^{-4}\,\mathrm{m}$ and $D\sim1\,\mathrm{m}$, so $\lambda\ll d\ll D$. The slits $S_1$ and $S_2$ are two parts of the same **wave surface** and oscillate in phase, so the phase difference at $P$ is determined solely by the path difference:

$$
r_2-r_1\approx d\sin\theta\approx d\tan\theta=\frac{d\,x}{D},\qquad \Delta\varphi=\frac{2\pi}{\lambda}(r_2-r_1).
$$

### 1.1.2. Conditions for Bright and Dark Fringes

By the conditions for constructive and destructive interference of two waves satisfying the **coherence conditions** ([5.1.7](/5.1.7#sec-7.7.2)), the centers of the bright and dark fringes satisfy (the first line is for bright fringes, the second for dark fringes)

$$
\begin{aligned}
d\,\frac{x}{D}&=k\lambda, & x_k&=k\frac{D}{d}\lambda,\\
d\,\frac{x}{D}&=(2k+1)\frac{\lambda}{2}, & x_k&=(2k+1)\frac{D}{2d}\lambda,
\end{aligned}
\qquad k\in\mathbb{Z},
\tag{1.1}
$$
where the integer $k$ is called the interference order. The spacing between adjacent bright (or dark) fringes is

$$
\Delta x=\frac{D}{d}\lambda.
\tag{1.2}
$$

The fringes have the following features.

- They are a series of alternating bright and dark straight fringes parallel to the slits; for $\theta$ not too large they are equally spaced.
- The center ($x=0$) is the zeroth-order bright fringe; going to either side, the order $\lvert k\rvert$ and the corresponding path difference increase.
- $\Delta x\propto\lambda$ and $\Delta x\propto 1/d$: the smaller the slit separation and the farther the screen, the wider the fringes. From $\Delta x$, $d$ and $D$ one can measure the wavelength of light; Young was the first to estimate the wavelengths of the various colors from interference.
- For white light, the zeroth-order bright fringes of all wavelengths lie at $x=0$, so the central fringe is white, which fixes the position of the zeroth order. The other bright fringes are spread by wavelength into colored bands, violet on the inside and red on the outside, and they overlap one another at slightly higher orders.

**Example 1.1.1 (Double-Slit Fringes with White Light)** In a double-slit experiment with white light of wavelength range $400$–$760\,\mathrm{nm}$, from which order on do the colored bright fringes of adjacent orders overlap?

**Solution** The $k$-th order red ($\lambda_{\mathrm{r}}=760\,\mathrm{nm}$) bright fringe lies at $k\lambda_{\mathrm{r}}D/d$, and the $(k+1)$-th order violet ($\lambda_{\mathrm{v}}=400\,\mathrm{nm}$) bright fringe lies at $(k+1)\lambda_{\mathrm{v}}D/d$. They overlap when $k\lambda_{\mathrm{r}}\ge(k+1)\lambda_{\mathrm{v}}$, that is, $k\ge\lambda_{\mathrm{v}}/(\lambda_{\mathrm{r}}-\lambda_{\mathrm{v}})\approx1.1$. Hence the first-order spectrum is complete, and from the second order on, the red end of the second order overlaps the violet end of the third.

## 1.2. Coherent Light

### 1.2.1. Ordinary Sources and Lasers

**Definition 1.2.1 (Coherent Light)** Two light beams that satisfy the **coherence conditions** (same frequency, same direction of vibration, constant phase difference) are called **coherent light**; when they meet, they form a stable intensity distribution in space. Equal frequency and equal direction of vibration ensure that fringes can form, and a constant phase difference ensures that the fringes are stable.

The basic emitters in a light source are atoms and molecules. Ordinary sources (incandescent lamps and the Sun as thermal radiators, electroluminescence, photoluminescence, chemiluminescence, and so on) emit mainly by spontaneous emission: an atom in an excited state $E_2$ spontaneously jumps to a lower state $E_1$ and emits a wave train of finite length with frequency $\nu=(E_2-E_1)/h$; the mean lifetime of the excited state is about $10^{-8}\,\mathrm{s}$. When different atoms emit is completely random, and their frequencies, directions of vibration, initial phases and directions of propagation may all differ; even two successive wave trains from the same atom have no fixed phase relation. Light from two independent ordinary sources, or from different parts of the same source, is therefore incoherent: when it is superposed, the phase difference changes rapidly and randomly within the response time of the detector, and no interference fringes are seen.

A laser, by contrast, emits mainly by stimulated emission: an atom in an excited state, acted on by an external photon of frequency $\nu=(E_2-E_1)/h$, jumps to the lower state and simultaneously emits a photon identical to the external one in frequency, phase, direction of vibration and direction of propagation, so that the light is amplified. Laser light is highly monochromatic and consists of very long wave trains, so its coherence is far better than that of ordinary sources (for the principles of stimulated emission and lasers see [5.5.5](/5.5.5)).

**Remark 1.2.1** Synchrotron radiation is often listed beside lasers as a modern intense light source, but it is not stimulated emission. It is the electromagnetic radiation emitted by relativistic charged particles moving along curved paths in a magnetic field, that is, classical radiation from accelerated charges ([5.3.10](/5.3.10)); it is neither spontaneous emission by atoms nor stimulated emission. It is bright and has a broad spectrum, but its temporal coherence is generally far inferior to that of lasers.

### 1.2.2. Methods of Obtaining Coherent Light

Since light emitted from any two points of an ordinary source is incoherent, interference with an ordinary source can be observed only by splitting a wave train emitted by one atom in one event into two parts and letting them meet again after traveling different paths.

**Definition 1.2.2** The method of taking two parts from the same wave surface of the light emitted by a source (such as two slits) and bringing them together is called **division of wavefront**; the method of splitting the amplitude of a single beam into two parts (such as the parts reflected from the upper and lower surfaces of a thin film) and bringing them together is called **division of amplitude**.

Young's double slit is division of wavefront, and for an ordinary source its first slit (the single slit) is indispensable: only if it is narrow enough do $S_1$ and $S_2$ lie on the same wave surface ([Section 1.4](#sec-1.4)). Other division-of-wavefront setups include Fresnel's double mirror (two plane mirrors at a very small angle form two virtual images of the source, which serve as coherent sources) and Lloyd's mirror (the source and its virtual image in a plane mirror serve as the two coherent sources). In Lloyd's mirror, when the screen is moved to touch the edge of the mirror, the contact point is dark rather than bright, which shows that light reflected from air onto glass suffers a **half-wave loss**. Thin-film interference ([Section 1.6](#sec-1.6), [Section 1.7](#sec-1.7)) and the Michelson interferometer ([Section 1.8](#sec-1.8)) use division of amplitude.

### 1.2.3. Intensity Formula and Fringe Visibility

Let the vibrations of two beams of the same frequency and the same direction of vibration at $P$ be

$$
E_1=E_{10}\cos\Big(\omega t-\frac{2\pi r_1}{\lambda}+\varphi_{10}\Big),\qquad E_2=E_{20}\cos\Big(\omega t-\frac{2\pi r_2}{\lambda}+\varphi_{20}\Big).
$$
The resultant $E=E_1+E_2=E_0\cos(\omega t+\varphi)$ is again a **simple harmonic motion** of the same frequency, with amplitude satisfying

$$
E_0^2=E_{10}^2+E_{20}^2+2E_{10}E_{20}\cos\Delta\varphi,\qquad \Delta\varphi=\varphi_{20}-\varphi_{10}-\frac{2\pi}{\lambda}(r_2-r_1).
$$
Averaging over the response time of the detector (denoted by an overbar) and writing the relative intensity as $I=E_0^2$, we obtain

$$
I=I_1+I_2+2\sqrt{I_1I_2}\;\overline{\cos\Delta\varphi},
\tag{1.3}
$$
whose last term is called the interference term.

- Incoherent superposition: the initial phase difference of the two beams varies randomly, $\overline{\cos\Delta\varphi}=0$ and $I=I_1+I_2$; the intensities simply add everywhere and there are no fringes.
- Fully coherent superposition: $\Delta\varphi$ is constant and $\overline{\cos\Delta\varphi}=\cos\Delta\varphi$. For $\Delta\varphi=2k\pi$ the interference is constructive, $I_{\max}=I_1+I_2+2\sqrt{I_1I_2}$; for $\Delta\varphi=(2k+1)\pi$ it is destructive, $I_{\min}=I_1+I_2-2\sqrt{I_1I_2}$ ($k\in\mathbb{Z}$).

If $I_1=I_2=I_0$, then

$$
I=2I_0(1+\cos\Delta\varphi)=4I_0\cos^2\frac{\Delta\varphi}{2},\qquad \Delta\varphi=\frac{2\pi}{\lambda}d\sin\theta
\tag{1.4}
$$
(double slit), with $I=4I_0$ at bright fringes and $I=0$ at dark fringes. Interference neither creates nor destroys energy; it only redistributes it in space: the average of $I$ over one fringe period is still $2I_0$.

**Definition 1.2.3 (Fringe Visibility)** The **fringe visibility** (also called contrast or simply visibility) of interference fringes is defined as

$$
V=\frac{I_{\max}-I_{\min}}{I_{\max}+I_{\min}},\qquad 0\le V\le1.
$$

For two fully coherent beams, $V=\dfrac{2\sqrt{I_1I_2}}{I_1+I_2}$, and $V=1$ only if $I_1=I_2$. Hence if an attenuator is placed behind one of the two slits, the fringe spacing is unchanged but the visibility drops. Three factors determine the visibility: the amplitude ratio of the two beams, the monochromaticity of the source ([Section 1.3](#sec-1.3)), and the width of the source ([Section 1.4](#sec-1.4)). The positions of the fringes record the phase difference, while their visibility records the amplitude ratio and the degree of coherence, so interference fringes contain information about both the **wave intensity** and the phase of the light wave (holography makes use of this).

![Intensity of two-beam interference, I = I1 + I2 + 2√(I1 I2) cos Δφ. When the two intensities are equal the visibility is V = 1; the more unequal the intensities, the fainter the fringes, but the positions of the bright fringes do not change](./plots/two-beam-intensity.py)

## 1.3. Temporal Coherence

### 1.3.1. Quasi-Monochromatic Light and Spectral Linewidth

Strictly monochromatic light is an infinitely long **harmonic wave**, but real sources emit wave trains of finite length, whose frequency is not single-valued.

**Definition 1.3.1 (Quasi-Monochromatic Light)** Light whose frequencies (wavelengths) are concentrated in a very narrow range around a central value is called **quasi-monochromatic light**. The width $\Delta\lambda$ of the curve of intensity versus wavelength, measured where the intensity falls to half its maximum, is called the **spectral linewidth**; the smaller $\Delta\lambda/\lambda$, the better the monochromaticity of the light.

There are three main causes of line broadening:

| Cause | Mechanism | Line shape | Dependence |
|---|---|---|---|
| Natural linewidth | The excited state has a finite lifetime $\tau$, so the wave train has finite length | Lorentzian | $\Delta\nu\approx1/(2\pi\tau)$ |
| Doppler broadening | Thermal motion of the emitting atoms; the **Doppler effect** differs from atom to atom | Gaussian | $\Delta\nu\propto\sqrt{T/m}$ |
| Collision broadening | Collisions between atoms interrupt the wave trains | Lorentzian | $\Delta\nu\propto p$ at fixed temperature |

The Gaussian line shape is the density curve of the **normal distribution** (a component of the atomic velocity follows a **normal distribution**; see the **Maxwell velocity distribution** in 5.2); the Lorentzian line shape is the density curve of the **Cauchy distribution**, which is the spectrum of an exponentially decaying oscillation (the squared modulus of its **Fourier transform**).

### 1.3.2. Maximum Order of Coherence

In a double-slit experiment with quasi-monochromatic light, each wavelength component forms its own set of fringes, and these sets superpose incoherently. The zeroth-order bright fringe is at $x=0$ for all wavelengths; the higher the order, the more the fringes of different wavelengths are displaced from one another, the worse the visibility becomes, and the fringes of high order finally become invisible. Let the wavelengths be distributed between $\lambda-\Delta\lambda/2$ and $\lambda+\Delta\lambda/2$. When the $k_{\mathrm{M}}$-th order bright fringe of wavelength $\lambda+\Delta\lambda/2$ coincides with the $(k_{\mathrm{M}}+1)$-th order bright fringe of wavelength $\lambda-\Delta\lambda/2$, the fringes disappear completely:

$$
k_{\mathrm{M}}\Big(\lambda+\frac{\Delta\lambda}{2}\Big)=(k_{\mathrm{M}}+1)\Big(\lambda-\frac{\Delta\lambda}{2}\Big)\quad\Longrightarrow\quad k_{\mathrm{M}}=\frac{\lambda}{\Delta\lambda}-\frac12\approx\frac{\lambda}{\Delta\lambda}.
$$
$k_{\mathrm{M}}$ is called the maximum order of coherence.

More precisely, let the intensity be uniformly distributed in wavenumber $\sigma=1/\lambda$ over an interval of width $\Delta\sigma=\Delta\lambda/\lambda^2$. Averaging the two-beam intensity $1+\cos(2\pi\sigma\delta)$ of each component over $\sigma$ ($\delta$ is the optical path difference) gives

$$
I(\delta)\propto1+\frac{\sin u}{u}\cos\frac{2\pi\delta}{\lambda},\qquad u=\pi\Delta\sigma\,\delta=\frac{\pi\,\delta\,\Delta\lambda}{\lambda^2},
$$
and the visibility $V=\lvert\sin u/u\rvert$ falls with increasing optical path difference, first reaching zero at $\delta=\lambda^2/\Delta\lambda$, in agreement with the estimate above. Real spectral lines have Gaussian or Lorentzian shapes, for which the visibility decreases monotonically without the small revivals that the rectangular band in the figure below produces, but it falls on the same scale.

![Interference fringes of quasi-monochromatic light (Δλ/λ = 0.1). Top: fringes of three wavelength components, increasingly displaced at higher orders; bottom: intensity after incoherent superposition of the components, with the visibility falling to zero at the optical path difference λ²/Δλ = 10λ](./plots/quasi-monochromatic-fringes.py)

### 1.3.3. Coherence Length and Coherence Time

**Definition 1.3.2** The largest optical path difference at which two beams can still interfere is called the **coherence length**, denoted $\delta_{\mathrm{M}}$; the time light needs to travel the coherence length is called the **coherence time**, denoted $\tau_{\mathrm{c}}$:

$$
\delta_{\mathrm{M}}=k_{\mathrm{M}}\lambda=\frac{\lambda^2}{\Delta\lambda},\qquad \tau_{\mathrm{c}}=\frac{\delta_{\mathrm{M}}}{c}=\frac{1}{\Delta\nu}.
\tag{1.5}
$$

The second equality uses $\Delta\nu=c\Delta\lambda/\lambda^2$, and $\lambda$ here is the central wavelength.

The physical meaning of the coherence length can be understood from wave trains. Only the two parts into which a single wave train has been split can interfere when they meet again after traveling different distances. If the optical path difference of the two parts exceeds the length of the wave train, the leading part of a wave train no longer meets its own trailing part; what meets are two incoherent wave trains, and the fringes disappear. The coherence length is thus the effective length of the wave train, and the coherence time is its duration. This kind of coherence of light, determined by its monochromaticity, is called *temporal coherence*: the better the monochromaticity, the longer the coherence length and coherence time, and the better the temporal coherence.

The relation $\tau_{\mathrm{c}}\Delta\nu=1$ in Eq. (1.5) is a general result of Fourier analysis: a wave train of duration $\tau_{\mathrm{c}}$ has a spectral width of about $1/\tau_{\mathrm{c}}$. This is exactly the **uncertainty principle** of the **Fourier transform** in [2.5.6](/2.5.6#sec-6.3.4): a function and its Fourier transform cannot both be concentrated. More generally, the dependence of the fringe visibility on the optical path difference equals the modulus of the Fourier transform of the spectrum (the Wiener–Khinchin theorem). The Fourier-transform spectrometer in [Section 1.8](#sec-1.8) exploits this.

Some orders of magnitude (for $\lambda\approx550\,\mathrm{nm}$):

| Source | $\Delta\lambda$ | Coherence length $\delta_{\mathrm{M}}$ |
|---|---|---|
| White light ($400$–$700\,\mathrm{nm}$) | $\sim300\,\mathrm{nm}$ | $\sim1\,\mu\mathrm{m}$; only a few colored fringes near the zeroth order are visible |
| Ordinary monochromatic source (low-pressure gas discharge lamp) | $10^{-3}$–$10^{-1}\,\mathrm{nm}$ | $10^{-3}$–$10^{-1}\,\mathrm{m}$ |
| Ordinary He–Ne laser (multimode) | $\sim10^{-3}\,\mathrm{nm}$ | $\sim0.1$–$0.3\,\mathrm{m}$ |
| Frequency-stabilized single-mode laser | $10^{-9}$–$10^{-6}\,\mathrm{nm}$ | $10^{2}$–$10^{5}\,\mathrm{m}$ |

**Remark 1.3.1** If one estimates the wave-train length $L=\tau c\approx3\,\mathrm{m}$ from an excited-state lifetime $\tau\approx10^{-8}\,\mathrm{s}$, one obtains only the coherence length corresponding to the natural linewidth. In ordinary sources the atoms collide frequently, which interrupts the wave trains, and the Doppler shifts of the individual atoms differ, so the spectral lines are far wider than the natural width and the actual coherence length is only of the order of millimeters to centimeters. The "length of the wave train" should be understood as the effective length $\lambda^2/\Delta\lambda$ determined by the actual linewidth.

## 1.4. Spatial Coherence

### 1.4.1. Effect of Source Width on the Fringes

Ordinary sources always have some width. Let the source in the double-slit experiment be a strip of width $b$ (with no first slit), at distance $R$ from the double slit. The points of the source emit light that is mutually incoherent; each point forms its own set of fringes through the double slit, and the intensity on the screen is the incoherent superposition of these sets. The zeroth-order bright fringe of the source midpoint $M$ is at the center of the screen; a source point displaced by $s$ from the midpoint already has a path difference $s\,d/R$ on reaching $S_1$ and $S_2$, and its fringes are shifted as a whole. The wider the source, the more the sets of fringes are displaced from one another and the lower the visibility.

When the fringes of the edge point $L$ of the source are displaced relative to those of the midpoint $M$ by exactly half a fringe spacing (the first-order bright fringe of $L$ falls exactly midway between the zeroth- and first-order bright fringes of $M$), the fringes of the points from one end of the source to the other are displaced by a full fringe spacing, fill the screen uniformly, and the fringes vanish. The point $L$ is displaced by $b_0/2$ from the midpoint, and its path difference to the two slits is $\frac{b_0}{2}\cdot\frac{d}{R}$, which must equal half a wavelength:

$$
\frac{b_0}{2}\cdot\frac{d}{R}=\frac{\lambda}{2}\quad\Longrightarrow\quad b_0=\frac{R}{d}\lambda.
\tag{1.6}
$$
$b_0$ is called the limiting width of the source; fringes can be observed only for $b<b_0$. The exact calculation is completely parallel to [Section 1.3](#sec-1.3): averaging the fringes of the source points, $1+\cos\big(\frac{2\pi d}{\lambda}(\frac{x}{D}+\frac{s}{R})\big)$, over $s\in[-b/2,b/2]$ gives the visibility

$$
V=\Big\lvert\frac{\sin u}{u}\Big\rvert,\qquad u=\frac{\pi b\,d}{\lambda R},
$$
which first vanishes at $b=b_0$. Because the points of the source are incoherent, the fringes add in intensity, and the visibility is the Fourier transform of the intensity distribution of the source (the van Cittert–Zernike theorem); this is the same mathematical structure as the visibility in temporal coherence being the Fourier transform of the spectrum.

### 1.4.2. Transverse Coherence Length and Coherence Aperture Angle

Conversely, if the source width $b$ and distance $R$ are given, the slit separation must satisfy $d<R\lambda/b$ for fringes to be observed.

**Definition 1.4.1** For a source of width $b$ at distance $R$, the largest distance between two secondary sources in a plane facing the source that can still produce interference,

$$
d_0=\frac{R}{b}\lambda
$$
is called the **transverse coherence length**, and the angle

$$
\theta_0=\frac{d_0}{R}=\frac{\lambda}{b}
$$
that it subtends at the center of the source is called the **coherence aperture angle**.

Within the coherence aperture angle, the light vibrations at any two points of the plane facing the source are coherent; beyond it they are incoherent. This kind of coherence in the light field, determined by the width of the source, is called *spatial coherence*: the larger $d_0$ or $\theta_0$, the better the spatial coherence.

- For division-of-wavefront interference with an ordinary source, the width of the source is limited: to raise the visibility one must make the source (the first slit) narrow, but this weakens the brightness of the fringes, and the two requirements conflict. The first slit of the double-slit experiment is therefore indispensable for an ordinary source; its width affects the visibility but not the fringe spacing.
- In a laser (single transverse mode), the light is coherent across the whole beam cross section and can illuminate the double slit directly, with no first slit.
- The limiting width $b_0=R\lambda/d$ increases with wavelength and with the distance of the source. The angular diameter of the Sun is about $0.53^\circ\approx9.3\times10^{-3}\,\mathrm{rad}$, so the transverse coherence length of sunlight is only $\lambda/\theta\approx60\,\mu\mathrm{m}$; a distant star has a tiny angular diameter, and the transverse coherence length of its light at the ground can reach several meters.

### 1.4.3. Michelson's Stellar Interferometer

Spatial coherence can be turned around to measure the angular diameter $\varphi=b/R$ of a distant star: with the star as the source, increase the slit separation $d$ gradually; the fringes vanish at $d=d_0$, so $\varphi=\lambda/d_0$. A star is a disk rather than a strip source; the same calculation for a uniform disk changes the result to

$$
\varphi=1.22\frac{\lambda}{d_0},
$$
where the factor $1.22$ has the same origin as in the Airy disk of circular-aperture diffraction ([5.4.2](/5.4.2)): both come from the Fourier transform of a disk.

For stars $d_0$ can reach several to a dozen meters, and the aperture of a telescope cannot accommodate a double slit that large. Michelson mounted a crossbeam in front of the telescope and used four mirrors $M_1$–$M_4$ to reflect two widely separated beams of starlight into the two small apertures $S_1$ and $S_2$ of the telescope. The fringe spacing on the screen is determined by $S_1S_2$, while the fringe visibility is determined by the separation of the two outer mirrors $M_1$ and $M_4$; adjusting $M_1M_4$ until the fringes vanish gives $d_0$.

**Example 1.4.1 (Angular Diameter of Betelgeuse)** In December 1920, Michelson and Pease observed $\alpha$ Orionis (Betelgeuse) with this interferometer, using an effective wavelength $\lambda\approx570\,\mathrm{nm}$; the fringes vanished at $d_0\approx3.07\,\mathrm{m}$. Find its angular diameter.

**Solution**

$$
\varphi=1.22\frac{\lambda}{d_0}=1.22\times\frac{570\times10^{-9}}{3.07}\,\mathrm{rad}\approx2.3\times10^{-7}\,\mathrm{rad}\approx0.047''.
$$
This was the first measurement of the angular diameter of a star other than the Sun. Modern optical interferometer arrays and very-long-baseline interferometry (VLBI) with radio telescopes are based on the same principle.

## 1.5. Optical Path Length

### 1.5.1. Optical Path Length and Optical Path Difference

In a medium of **refractive index** $n$ light travels at speed $u=c/n$ with unchanged frequency, so the wavelength in the medium is $\lambda_n=u/\nu=\lambda/n$ ($\lambda$ is the vacuum wavelength). After traveling a distance $r$ in the medium, the phase lags by

$$
\Delta\varphi=\frac{2\pi}{\lambda_n}r=\frac{2\pi}{\lambda}\,nr.
$$
Thus traveling $r$ in a medium causes the same phase change as traveling $nr$ in vacuum; in terms of time, the time $r/u=nr/c$ for light to travel $r$ in the medium also equals the time to travel $nr$ in vacuum.

**Definition 1.5.1 (Optical Path Length)** The product $nr$ of the geometric path $r$ that light travels in a medium of refractive index $n$ and $n$ is called the **optical path length**; when light passes through several media, the optical path length is $\sum_i n_ir_i$ (or $\int n\,\mathrm{d}l$). The difference between the optical path lengths of two beams is called the **optical path difference**, denoted $\delta$, and it is related to the phase difference by

$$
\Delta\varphi=\frac{2\pi}{\lambda}\delta,
\tag{1.7}
$$
where $\lambda$ is the vacuum wavelength.

With optical path length, phase differences of light in different media can all be computed with the vacuum wavelength. The conditions for constructive and destructive interference become $\delta=k\lambda$ and $\delta=(2k+1)\lambda/2$. If exactly one of the two beams suffers a **half-wave loss** on reflection, an extra $\lambda/2$ must be added to the optical path difference (adding or subtracting both work; this only changes the labeling of the order $k$).

**Example 1.5.1 (Fringe Shift Caused by a Mica Sheet)** In a double-slit experiment, the upper slit $S_1$ is covered with a mica sheet of refractive index $n=1.58$ and thickness $l=6.6\,\mu\mathrm{m}$, and the incident wavelength is $\lambda=550\,\mathrm{nm}$. How do the fringes change?

**Solution** The optical path difference of the two beams reaching the point $P$ on the screen is

$$
\delta=r_2-\big[(r_1-l)+nl\big]=(r_2-r_1)-(n-1)l.
$$
The zeroth-order bright fringe ($\delta=0$) moves from $x=0$ to the position where $r_2-r_1=(n-1)l>0$, that is, toward the covered slit $S_1$; every fringe shifts by the same distance, and the fringe spacing $\Delta x=D\lambda/d$ is unchanged. The number of fringes that have moved past is

$$
N=\frac{(n-1)l}{\lambda}=\frac{0.58\times6.6\times10^{-6}}{5.5\times10^{-7}}\approx7,
$$
that is, the position of the original seventh-order bright fringe becomes the zeroth-order bright fringe. Conversely, counting the fringes that have moved past gives the thickness or refractive index of the sheet.

### 1.5.2. Lenses Introduce No Extra Optical Path Difference

In optical experiments lenses are often used to focus beams. Experiment shows that when light from an object point $S$ is focused by a lens onto the image point $S'$, the image point is bright, so all the rays superpose in phase at $S'$; that is, all rays from the object point to the image point have equal optical path lengths. Likewise, when parallel light is focused to the focal point, all points of one wave surface of the incident light (a plane perpendicular to the rays) have equal optical path lengths to the focus.

**Property 1.5.1 (Equal Optical Path Through a Lens)** A thin lens introduces no extra optical path difference: all rays from an object point to its image point have equal optical path lengths, and all points of a plane wave surface perpendicular to the rays have equal optical path lengths to the focal point.

Geometrically, a ray through the edge of the lens travels a longer path in air and a ray through the center travels a longer path in glass, and the two exactly compensate. This is a manifestation of Fermat's principle (light travels along paths of extremal optical path length) in imaging: in ideal imaging, all rays from the object point to the image point are extremal paths of the optical path length and therefore have the same optical path length. Hence in interference and diffraction setups, adding a lens in the light path only changes where the rays converge, not the optical path differences among them.

## 1.6. Thin-Film Interference (I): Fringes of Equal Thickness

The colors of soap bubbles, oil films on water, insect wings and the feathers of some birds are all due to thin-film interference. Thin-film interference is division of amplitude: the incident light is reflected partly from the upper and partly from the lower surface of the film, and the two reflected beams come from the same wave train and are coherent. The film must be "thin" because the optical path difference of the two beams is about twice the film thickness and must be smaller than the coherence length of the light; thin and thick are relative and depend on the monochromaticity of the light. In general, thin-film interference is complicated; two limiting cases are of practical importance: fringes of equal thickness produced by a film of nonuniform thickness and localized near the film surface (this section), and fringes of equal inclination produced by a film of uniform thickness and localized at infinity ([Section 1.7](#sec-1.7)).

### 1.6.1. Optical Path Difference of a Thin Film

Let a thin film of refractive index $n_2$ lie between media of refractive indices $n_1$ (above) and $n_3$ (below), with film thickness $e$. Light is incident on the upper surface of the film at angle of incidence $i$; part of it is reflected at the point $A$ (beam 1), and part is refracted into the film (angle of refraction $r$), reflected at the point $B$ on the lower surface, and leaves through the upper surface (beam 2). From the geometry $AB=BC=e/\cos r$, the distance between $A$ and $C$ is $2e\tan r$, and by the **law of refraction** $n_1\sin i=n_2\sin r$, for a very thin film the optical path difference of the two beams is

$$
\delta=2n_2\frac{e}{\cos r}-n_1\cdot2e\tan r\,\sin i+\delta'=2n_2e\cos r+\delta'=2e\sqrt{n_2^2-n_1^2\sin^2 i}+\delta'.
\tag{1.8}
$$
Here $\delta'$ is the extra optical path difference caused by the **half-wave loss** in the two reflections: when exactly one of the two reflections goes from the optically thinner to the optically denser medium ($n_1<n_2>n_3$ or $n_1>n_2<n_3$), $\delta'=\lambda/2$; when both or neither does ($n_1<n_2<n_3$ or $n_1>n_2>n_3$), $\delta'=0$.

**Remark 1.6.1** The **half-wave loss** of light is analogous to the case of a string wave in [5.1.7](/5.1.7#sec-7.7.4) and is determined by the refractive indices on the two sides of the interface; the rigorous basis is the boundary conditions of the electromagnetic field (the Fresnel equations, [5.4.3](/5.4.3)). At oblique incidence the phase of the reflected light also depends on the polarization (the reflection coefficient of the p component changes sign on the two sides of Brewster's angle), so the rule above strictly holds only for normal or small-angle incidence and for the s component, whose vibration is perpendicular to the plane of incidence; thin-film interference usually deals with exactly these cases.

Eq. (1.8) shows that the optical path difference generally depends on both the film thickness $e$ and the angle of incidence $i$.

### 1.6.2. Fringes of Equal Thickness

In practice one often illuminates with monochromatic parallel light at normal incidence ($i=r=0$). Then

$$
\delta=2n_2e+\delta',
$$
and for fixed $n_2$ and $\lambda$, $\delta$ is determined by the film thickness $e$ alone: points of the film with the same thickness lie on the same fringe.

**Definition 1.6.1 (Equal-Thickness Interference)** When a film of nonuniform thickness is illuminated by monochromatic parallel light, the reflected light has the same optical path difference wherever the film thickness is the same, and the interference fringes are contour lines of the thickness of the film. This interference is called equal-thickness interference, and the resulting fringes are called **fringes of equal thickness**.

The fringes are localized near the surface of the film and are observed by focusing the eye or a microscope on the film surface. The difference in film thickness between adjacent bright (or dark) fringes is

$$
\Delta e=\frac{\lambda}{2n_2},
$$
so fringes of equal thickness are like a topographic map with a contour interval of $\lambda/(2n_2)$: when the thickness varies linearly the fringes are equally spaced, and when it varies nonlinearly they are not. When a soap film is illuminated by white light, a vertical soap film is thinner at the top and thicker at the bottom because of gravity and shows horizontal colored bands; the patterns on a soap bubble change as the film thickness flows.

### 1.6.3. Wedge Film

**Definition 1.6.2 (Wedge Film)** A thin film between two planes forming a very small angle is called a **wedge film**; the angle $\theta$ is typically $10^{-5}$–$10^{-4}\,\mathrm{rad}$.

Take an air wedge between two glass plates ($n_2=1$, glass above and below). The reflection at the lower surface is from air onto glass and has a half-wave loss, while the reflection at the upper surface does not, so

$$
\delta=2e+\frac{\lambda}{2}.
$$
Bright fringes satisfy $\delta=k\lambda$ ($k=1,2,3,\dots$) and dark fringes satisfy $\delta=(2k+1)\lambda/2$ ($k=0,1,2,\dots$). In general, for a film of refractive index $n$, replace $2e$ by $2ne$. The fringes are equally spaced alternating bright and dark straight fringes parallel to the edge; at the edge $e=0$ and $\delta=\lambda/2$, so the edge is dark, which is direct evidence of the half-wave loss. If the spacing of adjacent bright fringes is $L$, then $L\sin\theta=\Delta e=\lambda/(2n)$, and since $\theta$ is very small,

$$
L=\frac{\lambda}{2n\theta}.
\tag{1.9}
$$
The smaller $\theta$ is, the wider the fringes are spread and the easier they are to measure.

Applications of the wedge:

- Measurement: with $\theta$ and $n$ known, measuring $L$ gives the wavelength $\lambda$; with $\lambda$ and $\theta$ known, measuring $L$ gives the refractive index $n$. A thin wire or sheet clamped at one end between two flat glass plates can be measured for its diameter or thickness. A wedge formed by a standard gauge block, the block to be tested and optical flats allows a precise comparison of lengths. In an interference dilatometer, the thickness of the wedge changes as the sample lengthens on heating, and counting the number of fringes that move past gives the expansion (each fringe corresponds to a thickness change of $\lambda/2$).
- Testing surface flatness: a standard optical flat is placed on the workpiece to be tested, and an air wedge forms between them. If the workpiece surface is flat, the fringes are equally spaced straight lines. If at some place the fringes bend toward the edge (the side where the film is thinner), the air layer there is thicker than on either side, so the workpiece has a depression; if the fringes bend away from the edge, there is a bump. The ratio of the amount of bending to the fringe spacing, multiplied by $\lambda/2$, is the depth of the depression or bump.

**Example 1.6.1 (Measuring the Diameter of a Thin Wire)** Two flat glass plates touch at one end and a thin wire is clamped at the other end, forming an air wedge. The wedge is illuminated at normal incidence with sodium yellow light of wavelength $\lambda=589.3\,\mathrm{nm}$, and from the edge (the $0$-th dark fringe) to the wire there are exactly $30$ dark fringes, the last being the $30$-th. Find the diameter of the wire.

**Solution** At the $k$-th dark fringe $2e+\lambda/2=(2k+1)\lambda/2$, that is, $e=k\lambda/2$. The diameter of the wire is

$$
D_{\mathrm{w}}=30\times\frac{\lambda}{2}=30\times\frac{589.3\,\mathrm{nm}}{2}\approx8.84\,\mu\mathrm{m}.
$$

### 1.6.4. Newton's Rings

Place a plano-convex lens of very large radius of curvature $R$ on a flat glass plate (an optical flat); between them is an air layer whose thickness is zero at the center and increases gradually outward. With monochromatic parallel light at normal incidence, one sees in reflected light a set of concentric rings centered on the contact point, called *Newton's rings*. They are fringes of equal thickness, whose contours are circles centered on the contact point.

At radius $r$ the air layer has thickness $e$; from the geometry $r^2=R^2-(R-e)^2=2Re-e^2\approx2Re$, so $e=r^2/(2R)$. The optical path difference is $\delta=2e+\lambda/2=r^2/R+\lambda/2$, and the dark-ring condition $\delta=(2k+1)\lambda/2$ gives the radius of the $k$-th dark ring

$$
r_k=\sqrt{kR\lambda},\qquad k=0,1,2,\dots;
\tag{1.10}
$$
the radius of the bright rings is $r_k=\sqrt{(2k-1)R\lambda/2}$, $k=1,2,\dots$. If the space between the lens and the flat is filled with a liquid of refractive index $n$, all radii are divided by $\sqrt{n}$.

- The center ($r=0$) is a dark spot, the dark ring with $k=0$; the inner rings have low order and the outer rings high order.
- $r_1:r_2:r_3=1:\sqrt2:\sqrt3$, and the spacing between adjacent dark rings decreases with increasing $r$: the fringes are sparse inside and dense outside, because the thickness of the air layer grows as $r^2$ and increases faster farther out.
- Newton's rings can also be seen in transmitted light; they are complementary to the rings in reflected light (the center is bright) but have very low visibility, because the light that has been reflected twice is much weaker than the directly transmitted light.
- When the plano-convex lens is slowly raised, the air layer becomes thicker everywhere and a fringe of given order moves toward where the thickness is smaller, that is, toward the center: the rings shrink toward the center and disappear there one after another.
- With white light, colored rings form, and only a few orders near the center can be seen.

![Newton's rings in reflected light (R = 1 m, sodium yellow light). Left: the interference pattern, with a dark center; right: intensity along a radius, with dark-ring radii r_k = √(kRλ), fringes sparse inside and dense outside](./plots/newton-rings.py)

In practice, because of dust or deformation at the contact point, the exact order of the $k$-th ring is hard to determine. Taking two dark rings $m$ orders apart,

$$
r_{k+m}^2-r_k^2=mR\lambda,
$$
one can measure the radius of curvature $R$ of the lens from a known wavelength, or the wavelength from a known $R$, without knowing $k$. Newton's rings are also used to test the spherical quality of lenses: the lens to be tested is placed on a standard test plate of the same curvature; if the two fit perfectly no fringes are seen. Rings indicate an error in the radius, with each ring corresponding to a thickness difference of $\lambda/2$; rings that are not circular indicate an irregular surface. Pressing lightly on the test plate and watching whether the rings contract toward the center or expand outward tells whether the radius of curvature of the lens is too large or too small.

**Example 1.6.2 (Measuring the Radius of Curvature of a Lens)** Newton's rings are observed with sodium yellow light ($\lambda=589.3\,\mathrm{nm}$). A dark ring has radius $1.50\,\mathrm{mm}$, and the fifth dark ring counting outward from it has radius $2.30\,\mathrm{mm}$. Find the radius of curvature of the lens.

**Solution**

$$
R=\frac{r_{k+5}^2-r_k^2}{5\lambda}=\frac{(2.30^2-1.50^2)\times10^{-6}}{5\times589.3\times10^{-9}}\,\mathrm{m}\approx1.03\,\mathrm{m}.
$$

## 1.7. Thin-Film Interference (II): Fringes of Equal Inclination

### 1.7.1. Formation of Fringes of Equal Inclination

When a film of uniform thickness $e$ is illuminated by a point source (or an extended source), the two beams 1 and 2 obtained from a single incident ray by reflection at the upper and lower surfaces are parallel and meet only at infinity. Observed in the focal plane of a lens $L$, the two beams converge at the same point, and since the lens introduces no extra optical path difference (Property 1.5.1), the optical path difference is Eq. (1.8):

$$
\delta=2e\sqrt{n_2^2-n_1^2\sin^2 i}+\delta'.
$$
For fixed $n_1$, $n_2$, $e$ and $\lambda$, $\delta$ is determined by the angle of incidence $i$ alone.

**Definition 1.7.1 (Equal-Inclination Interference)** When a film of uniform thickness is illuminated, light incident at the same angle has the same optical path difference after reflection from the upper and lower surfaces and converges onto the same fringe in the focal plane of the lens. This interference is called equal-inclination interference, and the resulting fringes are called **fringes of equal inclination**.

For a film in air ($n_1<n_2$, air below as well, $\delta'=\lambda/2$), the conditions for bright and dark fringes are

$$
2e\sqrt{n_2^2-n_1^2\sin^2 i}+\frac{\lambda}{2}=k\lambda\quad(k=1,2,3,\dots),\qquad
2e\sqrt{n_2^2-n_1^2\sin^2 i}+\frac{\lambda}{2}=(2k+1)\frac{\lambda}{2}\quad(k=0,1,2,\dots).
$$

### 1.7.2. Features of Fringes of Equal Inclination

1. Shape: when the optical axis of the lens is perpendicular to the film, rays of the same inclination form a cone about the axis, and the fringes are alternating bright and dark concentric rings; the radius of the ring of order $k$ is $R_k=f\tan i_k$ ($f$ is the focal length of the lens).
2. Distribution of orders: the larger $i$ is, the smaller $\delta$ is, so the smaller the radius of a ring, the higher its order, and the center has the highest order. This is opposite to Newton's rings (lowest order at the center).
3. Distribution of spacing: differentiating the bright-fringe condition gives $\mathrm{d}i/\mathrm{d}k\propto-1/\sin2i$ (approximately $\propto 1/i$ for small angles), so rings near the center are farther apart: the fringes are sparse inside and dense outside.
4. Change of film thickness: at a fixed observation position $R$ (fixed inclination $i$), increasing the film thickness $e$ increases the optical path difference and hence the order there, that is, a ring of higher order that was farther inside moves to this position. As the film gets thicker, the rings expand outward and new bright rings keep "emerging" from the center; as the film gets thinner, the rings contract toward the center and "sink" into it and disappear. At the center $i=0$ and $2n_2e+\lambda/2=k_{\mathrm{c}}\lambda$, and each ring that emerges or sinks corresponds to a thickness change $\Delta e=\lambda/(2n_2)$.
5. Wavelength: for the same order $k$ and the same film thickness, the larger $\lambda$ is, the larger $\sqrt{n_2^2-n_1^2\sin^2i}$ is and the smaller $i$ is, so rings of longer wavelength have smaller radii. With white light, each order of ring is red on the inside and violet on the outside.

In practice an extended surface source is often used: the light from the source reaches the film via a half-silvered mirror, and the reflected light passes through the half-silvered mirror and is focused onto a screen by a lens. By the discussion of spatial coherence, an extended source might seem to lower the visibility, but in equal-inclination interference the light from different points of the source with the same inclination $i$ converges onto the same ring in the focal plane, and the fringes formed by the individual points coincide exactly (only their intensities add incoherently). Equal-inclination interference therefore has no conflict between source width and visibility, and an extended source even makes the fringes brighter.

### 1.7.3. Comparison of Equal-Thickness and Equal-Inclination Interference

| | Equal-thickness interference | Equal-inclination interference |
|---|---|---|
| Film | Nonuniform thickness | Uniform thickness |
| Illumination | Parallel light (fixed inclination) | All inclinations (point or extended source) |
| Fringes are the locus of | Points of equal thickness | Rays of equal angle of incidence |
| Localization | Near the film surface | At infinity (focal plane of the lens) |
| Typical examples | Wedge: parallel straight fringes, equally spaced; Newton's rings: lowest order at the center, sparse inside and dense outside | Concentric rings, highest order at the center, sparse inside and dense outside |
| As the film thickens | Fringes move toward the thinner side of the film | Rings expand outward, new rings emerge at the center |

Features common to both: the fringes are loci of points of equal optical path difference; the interference patterns in reflected and transmitted light are complementary; with white light the fringes are colored and blurred; when the film thickness grows so that the optical path difference exceeds the coherence length, the fringes vanish; whether there is a half-wave loss must be analyzed case by case.

### 1.7.4. Anti-Reflection and High-Reflection Coatings

The surfaces of optical elements such as camera lenses and spectacle lenses are coated with a transparent dielectric film so that the light reflected from the upper and lower surfaces of the film interferes destructively, which reduces reflection and increases transmission; such a film is called an *anti-reflection coating*. Take the refractive index $n$ of the film between that of air ($n_0=1$) and that of glass ($n_{\mathrm{s}}$). Both reflections have a half-wave loss, so $\delta'=0$, and at normal incidence the condition for destructive interference is

$$
2ne=(2k+1)\frac{\lambda}{2},\qquad e_{\min}=\frac{\lambda}{4n},
$$
that is, the optical thickness $ne$ of the film is a quarter wavelength. If we further require the two reflected beams to have equal amplitudes so that the reflection is eliminated completely, we need $n=\sqrt{n_0n_{\mathrm{s}}}$.

**Example 1.7.1 ($\ce{MgF2}$ Anti-Reflection Coating)** Glass of refractive index $n_{\mathrm{s}}=1.52$ is coated with a layer of $\ce{MgF2}$ ($n=1.38$) so that normally reflected light of wavelength $550\,\mathrm{nm}$ (the yellow-green light to which the eye is most sensitive) interferes destructively. Find the minimum thickness of the film and estimate the change in reflectance.

**Solution** Since $1<1.38<1.52$, both reflections have a half-wave loss, and the minimum thickness is

$$
e_{\min}=\frac{\lambda}{4n}=\frac{550\,\mathrm{nm}}{4\times1.38}\approx99.6\,\mathrm{nm}.
$$
The reflectance at normal incidence without a coating is $\big(\frac{n_{\mathrm{s}}-1}{n_{\mathrm{s}}+1}\big)^2\approx4.3\%$. With the quarter-wave coating, taking multiple reflections within the film into account, the reflectance at $550\,\mathrm{nm}$ is $\big(\frac{n_0n_{\mathrm{s}}-n^2}{n_0n_{\mathrm{s}}+n^2}\big)^2\approx1.3\%$. The ideal $n=\sqrt{1.52}\approx1.23$ has no suitable durable material, and $\ce{MgF2}$ is a common compromise. For red light and blue-violet light, which are away from $550\,\mathrm{nm}$, the cancellation is incomplete, so light reflected from coated lenses looks blue-violet.

![Reflectance of glass at normal incidence versus wavelength: about 4.3% uncoated; about 1.3% with a quarter-wave MgF₂ film for 550 nm; an ideal film of refractive index √1.52 has zero reflectance at 550 nm](./plots/antireflection-coating.py)

Conversely, if films of high and low refractive index, each of optical thickness $\lambda/4$, are deposited alternately, the light reflected from the various interfaces interferes constructively, and with enough layers the reflectance can exceed $99\%$; this is called a high-reflection coating (dielectric mirror) and is used in the resonator mirrors of lasers and in interference filters. The outer surface of the Hubble Space Telescope is covered with a highly reflective film to reduce the temperature variation as it passes between sunlight and Earth's shadow in orbit.

## 1.8. The Michelson Interferometer

### 1.8.1. Structure and Principle

The *Michelson interferometer* is a precision instrument that produces two-beam interference by division of amplitude. Light from the source $S$ falls on a beam splitter $G_1$ placed at $45^\circ$ to the light path; the back of $G_1$ carries a half-silvered coating that splits the light into two beams. The reflected beam 1 goes to the plane mirror $M_1$ and the transmitted beam 2 goes to the plane mirror $M_2$; the two beams are reflected back and recombined at $G_1$, then go to the observation device $E$ (a telescope or screen). Beam 1 passes through the glass of $G_1$ three times and beam 2 only once; a compensating plate $G_2$ of the same material and thickness as $G_1$ is placed in the path of beam 2 so that the optical paths in glass are equal in the two arms, compensating all wavelengths at once (necessary for white-light interference).

Seen from the observation device, the virtual image $M_2'$ of $M_2$ formed by the half-silvered coating of $G_1$ lies near $M_1$, and the interference of the two beams is equivalent to that of the thin air film between $M_1$ and $M_2'$. The thickness and inclination of this "film" can be adjusted at will, and the two arms are completely separated in space, which makes it convenient to insert a sample in one arm.

- When $M_1$ and $M_2'$ are parallel, the air film has uniform thickness and fringes of equal inclination (concentric rings) are obtained.
- When $M_1$ and $M_2'$ form a small angle, fringes of equal thickness of an air wedge (parallel straight fringes) are obtained.

### 1.8.2. Movement of the Mirror and Fringe Counting

$M_1$ is mounted on a precision lead screw and can be translated along the light path. When $M_1$ moves by $\Delta d$, the thickness of the air film changes by $\Delta d$ and the optical path difference by $2\Delta d$. Each time the optical path difference changes by one wavelength, one fringe moves across the field of view (for fringes of equal inclination, one ring emerges from or sinks into the center). If $N$ fringes are counted passing by, then

$$
\Delta d=N\frac{\lambda}{2}.
\tag{1.11}
$$
With a reading microscope one can judge $1/10$ of a fringe, so displacements of $\lambda/20$ (about $30\,\mathrm{nm}$) can be measured. With $\lambda$ known one can measure length, and with $\Delta d$ known one can measure wavelength. Historically, Michelson calibrated the international prototype meter with the wavelength of the red cadmium line ($643.8\,\mathrm{nm}$); in 1960 the meter was redefined by the wavelength of a $\ce{^{86}Kr}$ line, and since 1983 it has been defined through the fixed value of the speed of light, with laser interferometry remaining the main way of realizing the meter.

If a transparent medium of length $l$ and refractive index $n$ (for example, a gas cell open at one end that can be evacuated) is inserted in one arm, the optical path of that arm increases by $2(n-1)l$. If $N$ fringes move correspondingly, then

$$
2(n-1)l=N\lambda,
$$
which yields the refractive index.

**Example 1.8.1 (Measuring the Refractive Index of Air)** A glass gas cell of length $l=10.0\,\mathrm{cm}$ is placed in one arm of a Michelson interferometer, illuminated by a He–Ne laser of wavelength $\lambda=632.8\,\mathrm{nm}$. As the cell is evacuated from air-filled to vacuum, $N=92$ fringes are counted passing by. Find the refractive index of air.

**Solution**

$$
n=1+\frac{N\lambda}{2l}=1+\frac{92\times632.8\times10^{-9}}{2\times0.100}\approx1+2.91\times10^{-4}=1.000291.
$$
This method can measure refractive indices that differ from $1$ by a few parts in ten thousand, which is hard to do by other methods.

### 1.8.3. Applications and History

- The Michelson–Morley experiment (1887): a Michelson interferometer whose arm length was extended to about $11\,\mathrm{m}$ by multiple reflections was used to look for the "ether wind"; rotating the instrument was expected to shift the fringes by about $0.4$ of a fringe, but the observed shift was much smaller. This null result is one of the experimental foundations of special relativity; see [5.1.8](/5.1.8#sec-8.1.3).
- Spectroscopy: with a Michelson interferometer, record the intensity as a function of optical path difference (the interferogram), which is the Fourier transform of the spectrum ([Section 1.3](#sec-1.3)); an inverse transform then gives the spectrum. This is the principle of the Fourier-transform infrared spectrometer (numerically a fast Fourier transform is used). The variation of the fringe visibility with the displacement of the moving mirror can also be used directly to measure the linewidth, and this is how Michelson discovered the fine structure of spectral lines.
- Gravitational-wave detection: LIGO is a Michelson interferometer with arms $4\,\mathrm{km}$ long in which light travels back and forth hundreds of times; in 2015 it made the first direct detection of gravitational waves from a binary black hole merger, measuring a relative change in arm length of about $10^{-21}$.

Michelson received the 1907 Nobel Prize in Physics for his precision optical instruments and the spectroscopic and metrological investigations carried out with them, and he also measured the speed of light accurately several times.

## Summary

| Topic | Key points |
|---|---|
| Double-slit interference | Bright fringes $d\,x/D=k\lambda$, dark fringes $d\,x/D=(2k+1)\lambda/2$; $\Delta x=D\lambda/d$; $I=4I_0\cos^2(\Delta\varphi/2)$ |
| Coherent light | Same frequency, same direction of vibration, constant phase difference; ordinary sources obtain coherent light by division of wavefront or of amplitude |
| Intensity and visibility | $I=I_1+I_2+2\sqrt{I_1I_2}\,\overline{\cos\Delta\varphi}$; $V=(I_{\max}-I_{\min})/(I_{\max}+I_{\min})$ |
| Temporal coherence | $k_{\mathrm{M}}=\lambda/\Delta\lambda$; coherence length $\delta_{\mathrm{M}}=\lambda^2/\Delta\lambda$; coherence time $\tau_{\mathrm{c}}=\delta_{\mathrm{M}}/c=1/\Delta\nu$ |
| Spatial coherence | Limiting width $b_0=R\lambda/d$; transverse coherence length $d_0=R\lambda/b$; coherence aperture angle $\theta_0=\lambda/b$; stellar diameter $\varphi=1.22\lambda/d_0$ |
| Optical path length | Optical path length $nr$; $\Delta\varphi=2\pi\delta/\lambda$ (vacuum wavelength); lenses introduce no extra optical path difference |
| Thin-film interference | $\delta=2e\sqrt{n_2^2-n_1^2\sin^2i}+\delta'$, with $\delta'$ determined by half-wave loss |
| Equal-thickness interference | Wedge $L=\lambda/(2n\theta)$; Newton's rings, dark rings $r_k=\sqrt{kR\lambda}$, $r_{k+m}^2-r_k^2=mR\lambda$ |
| Equal-inclination interference | Concentric rings, highest order at the center; rings expand outward as the film thickens, $\Delta e=\lambda/(2n_2)$ per ring emerging |
| Anti-reflection coating | Optical thickness $\lambda/4$; ideal refractive index $\sqrt{n_0n_{\mathrm{s}}}$ |
| Michelson interferometer | Equivalent air film; $\Delta d=N\lambda/2$; $2(n-1)l=N\lambda$ |

To analyze an interference problem, first identify which two beams interfere; then compute their optical path difference (paying attention to refractive indices and half-wave loss); then determine the shape, position, distribution of orders and motion of the fringes; and if necessary write down the intensity formula and sketch the intensity curve.

## Questions

1. A thin lens is cut in two along a line through its center, and the two halves are displaced by a small distance $h$ perpendicular to the cut (a Billet split lens). A point source $S$ is placed at $2f$ in front of the lens, and the screen is at $10f$ behind it. Are interference fringes seen on the screen? What is the fringe spacing?

   **Answer** each half-lens images $S$ at $2f$ behind the lens with magnification $-1$; the two real images are $2h$ apart and are two coherent point sources, equivalent to a double slit with slit separation $d=2h$ and slit-to-screen distance $D=8f$, so $\Delta x=4f\lambda/h$.

2. In double-slit interference, how do the fringes change when the slit separation $d$ increases? What if the source $S$ is moved down perpendicular to the axis?

   **Answer** as $d$ increases the fringes become denser; when the source moves down, the zeroth-order bright fringe (where the optical path difference is zero) moves up and the whole set of fringes shifts upward with unchanged spacing.

3. When a soap bubble is blown, colors first appear on it, then change continually everywhere as the bubble expands, and finally it turns black and immediately bursts. Explain.

   **Answer** as the bubble expands the film gets thinner, and the wavelengths satisfying the constructive condition change accordingly; when the film thickness is much smaller than the wavelength, $\delta\approx\lambda/2$ (only the reflection from the outer surface has a half-wave loss), all wavelengths cancel and the film appears black; the film is by then extremely thin and bursts soon.

4. In double-slit interference, a thin mica sheet is placed over one slit. Do the fringe spacing and the position of the central fringe change?

   **Answer** the spacing is unchanged and the central bright fringe moves toward the side with the mica (Example 1.5.1).

5. Why is the edge of an air wedge dark? How can one tell on which side the edge lies?

   **Answer** at the edge $e=0$, only the $\lambda/2$ from the half-wave loss remains, and the two reflected beams cancel. Raise the upper plate slightly in parallel: the thickness increases everywhere and the fringes move toward the edge as a whole. Alternatively, use white light: the edge is dark, outside it are colored fringes whose colors fade at higher orders, and the side where the fringes are sharper is nearer the edge.

6. Observe Newton's rings and fringes of equal inclination with the same monochromatic light. Both are concentric rings; how do they differ?

   **Answer** Newton's rings have the lowest order at the center, are fringes of equal thickness and are localized at the film surface; fringes of equal inclination have the highest order at the center and are localized at infinity; both are sparse inside and dense outside.

7. Can fringes still be seen in a Michelson interferometer without the compensating plate, with monochromatic light? With white light?

   **Answer** with monochromatic light they can still be seen, only the position of zero optical path difference shifts; glass has **dispersion**, so the extra optical path difference differs for different wavelengths, and without the compensating plate the zeroth-order fringes of different wavelengths do not coincide, so white-light fringes are not seen.
