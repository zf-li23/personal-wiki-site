---
title: Diffraction of Light
description: The Huygens–Fresnel principle, Fresnel and Fraunhofer diffraction; single-slit diffraction by half-period zones and by phasors; grating diffraction, missing orders and grating spectra; circular-aperture diffraction, the Rayleigh criterion and the resolving power of optical instruments; X-ray diffraction and the Bragg equation; Fraunhofer diffraction and the Fourier transform.
source_hash: cf7995216985
---

When light meets an obstacle it bends around the edge into the geometric shadow and forms an alternating bright and dark intensity distribution in space; this is the **diffraction** of light. [5.1.7](/5.1.7#sec-7.6) used **Huygens' principle** to explain the direction of diffraction, but the wavelet construction cannot give the intensity, and the previous chapter [5.4.1](/5.4.1) treated the **interference** of a finite number of beams. This chapter combines the two: the coherent superposition of infinitely many wavelets on the **wavefront** determines the intensity of the diffracted field (the Huygens–Fresnel principle, Section 2.1). On this basis we discuss in turn Fraunhofer diffraction by a single slit (Section 2.2), diffraction by many slits, that is, a grating (Section 2.3), diffraction by a circular aperture and the limit it sets on the resolving power of optical instruments (Section 2.4), and finally X-ray diffraction, in which a crystal acts as a three-dimensional grating (Section 2.5). Computationally, the intensity of the single slit is found by adding **phasors** (amplitude vectors), exactly as in the superposition of oscillations of the same frequency in [5.1.6](/5.1.6#sec-6.2.1); mathematically, the amplitude distribution of Fraunhofer diffraction is the **Fourier transform** of the aperture function ([2.5.6](/2.5.6)), and the results for the single slit, the grating and the circular aperture are all special cases of this fact (Section 2.3.7). Diffraction also limits microscopes that use electrons as "light", where the de Broglie wavelength of the electron enters ([5.5.2](/5.5.2)); the spectrum and production of X-rays are discussed in [5.5.5](/5.5.5), and crystal-structure determination has wide applications in biophysics ([7.6](/7.6)) and chemistry.

## 2.1. Diffraction and the Huygens–Fresnel Principle

### 2.1.1. The Phenomenon of Diffraction

A source $S$ illuminates a screen with a small hole or slit (the diffraction screen). On an observation screen behind it we see not the geometric projection of the hole but an alternating bright and dark pattern: light enters the geometric shadow and the intensity is redistributed in space. The closer the linear size $a$ of the obstacle is to the wavelength, the more pronounced the diffraction. The wavelength of visible light is only a few hundred nanometers, so in daily life the diffraction of light is less obvious than that of sound and water waves, and it is generally easy to observe only for $a$ below $10^3\lambda$. Razor edges, thin wires, circular holes and circular disks each have their own diffraction patterns.

In 1818 Fresnel submitted to the French Academy of Sciences a paper that computed diffraction quantitatively from the wave theory. One of the judges, Poisson, deduced from his theory that there should be a bright spot at the center of the shadow of an opaque circular disk, which seemed absurd at the time. Arago promptly performed the experiment and indeed saw the spot. It later became known as the *Poisson spot*, also called the Arago spot, and it became strong evidence for the wave theory.

### 2.1.2. Fresnel Diffraction and Fraunhofer Diffraction

Let the distance from the source to the diffraction screen be $L$ and that from the diffraction screen to the observation screen be $D$.

**Definition 2.1.1** Diffraction in which at least one of $L$ and $D$ is finite is called **Fresnel diffraction** (near-field diffraction); diffraction in which both $L$ and $D$ can be regarded as infinite, that is, in which both the incident and the diffracted light are parallel, is called **Fraunhofer diffraction** (far-field diffraction).

In the laboratory, a point or line source is placed at the focus of a lens $L_1$ to obtain parallel incident light, and a lens $L_2$ focuses the diffracted light of one direction to a point in its focal plane; this realizes Fraunhofer diffraction at finite distances. Since a lens introduces no extra **optical path difference** ([5.4.1](/5.4.1#sec-1.5.2)), the **optical path difference** at the focal point equals that of the parallel light behind the diffraction screen.

Take a circular hole as an example. As the observation screen is moved from near to far, one sees successively: very close, the geometric projection of the hole; a bit farther, alternating bright and dark rings inside the projection, with a center that may be bright or dark, which is Fresnel diffraction; very far, a pattern that only scales in proportion to the distance without changing shape and whose center is always bright, which is Fraunhofer diffraction.

**Remark 2.1.1** The boundary between the two kinds of diffraction can be gauged by the Fresnel number $N_{\mathrm{F}}=a^2/(\lambda D)$ ($a$ is the half-width of the hole, and the incident light is parallel): for $N_{\mathrm{F}}\gg1$ the behavior is close to geometrical optics, for $N_{\mathrm{F}}\sim1$ it is Fresnel diffraction, and for $N_{\mathrm{F}}\ll1$ it is Fraunhofer diffraction. For example, for $a=0.5\,\mathrm{mm}$ and $\lambda=500\,\mathrm{nm}$, $D$ must be much larger than $0.5\,\mathrm{m}$ for the diffraction to be Fraunhofer. Fraunhofer diffraction is much simpler to calculate than Fresnel diffraction and is also the most commonly used, so this chapter discusses only it quantitatively.

### 2.1.3. The Huygens–Fresnel Principle

**Huygens' principle** gives only the position of the new **wave surface**. Fresnel added the idea that the wavelets superpose coherently:

**Property 2.1.1 (Huygens–Fresnel Principle)** Every surface element of a wavefront is a source emitting wavelets, and the light vibration at a point $P$ in space is the coherent superposition at that point of all the wavelets from the wavefront.

Let the amplitude at the surface element $\mathrm{d}S$ at $Q$ on the wavefront $S$ be $a(Q)$, with initial phase taken as zero, let its distance to $P$ be $r$, and let the angle between the normal $\boldsymbol{n}$ of the element and the direction of $r$ be $\theta$. The vibration that the element causes at $P$ is

$$
\mathrm{d}E(P)=C\,\frac{a(Q)K(\theta)}{r}\cos\Big(\omega t-\frac{2\pi r}{\lambda}\Big)\,\mathrm{d}S,
$$
and the resultant vibration at $P$ is

$$
E(P)=C\int_S\frac{a(Q)K(\theta)}{r}\cos\Big(\omega t-\frac{2\pi r}{\lambda}\Big)\,\mathrm{d}S=E_0(P)\cos\big[\omega t+\varphi(P)\big],
$$
with intensity $I(P)\propto E_0^2(P)$. Here $C$ is a constant of proportionality and $K(\theta)$ is called the obliquity factor (directional factor), which decreases as $\theta$ increases and is largest at $\theta=0$. Fresnel assumed $K=0$ for $\theta\ge\pi/2$ to explain why wavelets do not propagate backward.

The Huygens–Fresnel principle was originally a hypothesis. In 1882 Kirchhoff started from the scalar **wave equation** (for a **monochromatic wave**, the **Helmholtz equation**, [2.5.5](/2.5.5#sec-5.1.2)) and used **Green's theorem** to relate the field in the aperture to the field behind it, obtaining the Fresnel–Kirchhoff diffraction formula. It gives the constant $C=1/\lambda$, a phase advance of $\pi/2$ of the wavelets relative to the incident wave, and, for a plane wave at normal incidence, the obliquity factor $K(\theta)=\frac12(1+\cos\theta)$ (which vanishes only at $\theta=\pi$). The Huygens–Fresnel principle thus received a foundation in wave theory. This chapter uses only its qualitative form, "diffraction is the coherent superposition of infinitely many wavelets on the wavefront", and the fact that the obliquity factor is approximately constant in Fraunhofer diffraction.

## 2.2. Fraunhofer Diffraction by a Single Slit

### 2.2.1. Setup and Light Paths

A monochromatic line source $S$ lies on the focal line of a lens $L_1$, and parallel light illuminates a slit $AB$ of width $a$ at normal incidence; the diffracted light is focused by a lens $L_2$ (focal length $f$) onto the observation screen in the focal plane. The angle $\theta$ between the diffracted light and the direction of incidence (the optical axis) is called the diffraction angle, and all light diffracted at angle $\theta$ converges to the same point $P$ on the screen. The optical path difference at $P$ between the light diffracted at angle $\theta$ from the two edges $A$ and $B$ of the slit is

$$
\delta=a\sin\theta,
$$
which is the largest optical path difference between wavelets from the slit.

### 2.2.2. The Half-Period-Zone Method

To judge whether $P$ is bright or dark without integrating, Fresnel proposed the half-period-zone method: for a given diffraction angle, divide the wavefront $AB$ at the slit into a number of long strips of equal width such that the light from corresponding points of adjacent strips has an optical path difference of $\lambda/2$ at $P$; these strips are called half-period zones. The zones have equal areas, so the wavelets they emit have approximately equal amplitudes at $P$, and corresponding points of adjacent zones are in antiphase at $P$ and cancel each other.

- For $\theta=0$ all wavelets have zero optical path difference, and $P$ (the center of the screen) is the center of the central bright fringe.
- For $a\sin\theta=\lambda$ the slit divides into exactly two half-period zones, which cancel completely, and $P$ is a dark fringe.
- For $a\sin\theta=\frac32\lambda$ the slit divides into three half-period zones, two of which cancel, and the remaining one forms a bright fringe.
- For $a\sin\theta=2\lambda$ it divides into four half-period zones, which cancel in pairs, and $P$ is dark again.

In general ($k=1,2,3,\dots$):

- center of the central bright fringe: $a\sin\theta=0$;
- dark fringes: $a\sin\theta=\pm k\lambda$;
- centers of the other bright fringes (approximately): $a\sin\theta=\pm(2k+1)\dfrac{\lambda}{2}$.

When $a\sin\theta$ is not an integer multiple of $\lambda/2$, the slit cannot be divided into an integer number of half-period zones, and the brightness at $P$ lies between bright and dark. The positions of the center of the central bright fringe and of the dark fringes given by the half-period-zone method are exact, while the positions of the centers of the other bright fringes are slightly off (see Section 2.2.3); an exact intensity distribution requires adding all the wavelets from the slit.

**Remark 2.2.1** The dark-fringe condition $a\sin\theta=k\lambda$ of single-slit diffraction has the same form as the bright-fringe condition $d\sin\theta=k\lambda$ of double-slit interference, but there is no contradiction: in the former $a$ is the optical path difference between the two edge rays within one slit, and then the wavelets within the slit cancel in pairs; in the latter $d$ is the optical path difference between the two slits, and then the two beams reinforce each other.

### 2.2.3. The Phasor Method and the Intensity Formula

Divide the slit into $N$ equal narrow strips ($N$ large), each of width $\Delta x=a/N$. The wavelets from the strips have approximately equal amplitudes at $P$, say $\Delta E$, and the phase difference at $P$ between the wavelets of adjacent strips is

$$
\Delta\varphi=\frac{2\pi}{\lambda}\Delta x\sin\theta=\frac{2\pi a\sin\theta}{N\lambda}.
$$
The vibration at $P$ is therefore the superposition of $N$ **simple harmonic motions** of the same direction, frequency and amplitude, whose initial phases differ successively by $\Delta\varphi$, and the resultant amplitude equals the length of the resultant of $N$ **phasors** joined head to tail.

- At the center of the screen, $\theta=0$ and $\Delta\varphi=0$; the phasors lie along a straight line, the resultant amplitude is largest, and $E_0=N\Delta E$.
- At other points $\Delta\varphi\ne0$ and the phasors form a broken line; as $N\to\infty$ the broken line becomes a circular arc of length $E_0$, and the angle between the tangents at its two ends (the central angle) is $\Phi=N\Delta\varphi=2\pi a\sin\theta/\lambda$.

Let the radius of the arc be $R$; then $E_0=R\Phi$, and the resultant amplitude is the chord $E_P=2R\sin(\Phi/2)$. Setting

$$
\alpha=\frac{\Phi}{2}=\frac{\pi a\sin\theta}{\lambda},
$$
we get $E_P=E_0\sin\alpha/\alpha$. The intensity is proportional to the square of the amplitude, so

$$
I=I_0\Big(\frac{\sin\alpha}{\alpha}\Big)^2,\qquad \alpha=\frac{\pi a\sin\theta}{\lambda},
\tag{2.1}
$$
where $I_0$ is the intensity at the center of the central bright fringe.

![Phasor diagram of single-slit diffraction. At α = 0 the wavelet phasors lie along a straight line; at α = π the arc closes exactly once around and the resultant amplitude is zero (first dark fringe); at α ≈ 1.43π the arc goes around about one and a half times and the chord gives the first maximum](./plots/single-slit-phasors.py)

Finding the extrema of Eq. (2.1):

- Principal maximum: at $\alpha=0$, $\sin\alpha/\alpha=1$ and $I=I_0$, the center of the central bright fringe.
- Minima: at $\alpha=\pm k\pi$ ($k=1,2,\dots$), $\sin\alpha=0$ and $I=0$, that is, $a\sin\theta=\pm k\lambda$, exactly the cases in which the slit can be divided into an even number of half-period zones.
- Secondary maxima: $\frac{\mathrm{d}I}{\mathrm{d}\alpha}=0$ gives $\tan\alpha=\alpha$. The nonzero solutions of this transcendental equation can be found graphically (the intersections of the line $y=\alpha$ with the curve $y=\tan\alpha$) or numerically: $\alpha=\pm1.430\pi,\ \pm2.459\pi,\ \pm3.471\pi,\dots$, that is, $a\sin\theta=\pm1.430\lambda,\ \pm2.459\lambda,\ \pm3.471\lambda,\dots$, slightly closer to the center than the $1.5\lambda,\ 2.5\lambda,\ 3.5\lambda$ of the half-period-zone method. The intensities of the successive secondary maxima are $0.0472I_0$, $0.0165I_0$ and $0.0083I_0$, far smaller than the principal maximum: most of the light energy is concentrated in the central bright fringe.

![Relative intensity I/I0 = (sin α / α)² of single-slit Fraunhofer diffraction. The dark fringes are at a sin θ = kλ, and the secondary maxima deviate slightly from (k + 1/2)λ; the right panel magnifies the vertical axis tenfold to show the secondary maxima](./plots/single-slit-intensity.py)

### 2.2.4. Fringe Width

The distance (or angle subtended) between the centers of two adjacent dark fringes is defined as the width (angular width) of a bright fringe. For small diffraction angles, $\sin\theta\approx\tan\theta\approx\theta$.

The central bright fringe lies between the two first-order dark fringes $\theta_1\approx\lambda/a$, and its angular width and linear width are

$$
\Delta\theta_0=2\theta_1\approx\frac{2\lambda}{a},\qquad \Delta x_0=2f\tan\theta_1\approx\frac{2f\lambda}{a}.
$$
Since $a\,\Delta\theta_0=2\lambda$, the narrower the slit the more the diffraction spreads, the two being inversely proportional; this is called the inverse relation of diffraction.

The $k$-th order dark fringe is at $x_k=f\tan\theta_k\approx kf\lambda/a$, so the width of the other bright fringes is

$$
\Delta x=x_{k+1}-x_k\approx\frac{f\lambda}{a}=\frac12\Delta x_0,
$$
that is, for small diffraction angles the central bright fringe is twice as wide as the other bright fringes, which have equal widths.

The fringe width is proportional to $\lambda/a$:

- The longer the wavelength, the wider the fringes. With white light, the center of the central bright fringe is white, and the bright fringes on both sides are colored from violet to red.
- The narrower the slit, the wider the fringes. When $a$ decreases to about $\lambda$ and $\lambda/a\to1$, $\theta_1\to\pi/2$ and only the central bright fringe remains on the screen, a uniform brightness. When $a$ increases so that $\lambda/a\to0$, the fringes of all orders contract toward the center and only one bright line remains, which is the geometrical-optics image of the line source formed by the lens. Geometrical optics is the limit of wave optics for $\lambda/a\to0$.

**Example 2.2.1 (Coverage of a Radar)** A radar of wavelength $\lambda=30\,\mathrm{mm}$ is located at a distance $d=15\,\mathrm{m}$ from a highway; its antenna has width $a=0.20\,\mathrm{m}$, and the center line of the beam makes an angle of $15^\circ$ with the highway. Find the length $L$ of highway within the coverage of the radar.

**Solution** Regard the radar beam as the central bright fringe of single-slit diffraction. The first dark fringe satisfies $a\sin\theta_1=\lambda$, so $\sin\theta_1=0.15$ and $\theta_1=8.63^\circ$. The two edges of the beam make angles $15^\circ+8.63^\circ=23.63^\circ$ and $15^\circ-8.63^\circ=6.37^\circ$ with the highway, so

$$
L=d\,(\cot6.37^\circ-\cot23.63^\circ)=15\times(8.96-2.28)\,\mathrm{m}\approx100\,\mathrm{m}.
$$

### 2.2.5. Interference and Diffraction

Interference and diffraction are both coherent superpositions of waves and are essentially the same: interference is the coherent superposition of a finite number of discrete beams, and diffraction is the coherent superposition of infinitely many wavelets distributed continuously over the wavefront. They often occur in the same phenomenon: strictly speaking, each slit in a double-slit experiment also diffracts, and the double-slit fringes are "two-beam interference modulated by single-slit diffraction" (Section 2.3.4).

| | Double-slit interference | Single-slit diffraction |
|---|---|---|
| Condition | Two beams satisfy the **coherence conditions** | The slit or obstacle is small enough |
| Fringe width | Equal for all orders | The central bright fringe is widest, twice the others |
| Brightness | Bright fringes of all orders are about equally bright | The central bright fringe is brightest, and the intensity falls off quickly on both sides |
| In common | Both are superpositions of waves forming alternating bright and dark fringes | |

## 2.3. Grating Diffraction

### 2.3.1. The Grating

The bright fringes of single-slit diffraction are wide and dim and unsuitable for precise wavelength measurement. Arranging a large number of parallel slits of equal width and equal spacing gives bright, sharp fringes.

**Definition 2.3.1 (Diffraction Grating)** An optical element made of a large number of parallel slits (or reflecting surfaces) of equal width and equal spacing is called a **diffraction grating**. The sum $d=a+b$ of the width $a$ of the transmitting (or reflecting) part and the width $b$ of the opaque (or non-reflecting) part is called the **grating constant**; it is the spatial period of the grating.

Gratings are either transmission gratings or reflection gratings. Ordinary gratings have tens to thousands of lines per millimeter, and ruling with an electron beam can reach tens of thousands per millimeter ($d\sim10^{-7}\,\mathrm{m}$). In a broad sense, any spatially periodic structure made of diffracting units is a grating, for example a crystal for X-rays (Section 2.5) or an antenna array for radio waves (Section 2.3.5). Polychromatic light passing through a grating is spread by wavelength into a spectrum, so the grating is a basic element of spectral analysis (Section 2.4.4).

### 2.3.2. Multiple-Beam Interference and the Grating Equation

Let the grating have $N$ slits, let parallel light be incident normally, and let a lens focus the light diffracted at angle $\theta$ onto the point $P$ of the screen. With only one slit open, the screen shows a single-slit diffraction pattern; because of the focusing action of the lens, the single-slit pattern depends only on the diffraction angle and not on the position of the slit, so the patterns obtained with any one slit open coincide exactly. When all $N$ slits are open, these $N$ beams of the same diffraction angle superpose coherently and undergo multiple-beam interference, and the result of the interference is in turn modulated by single-slit diffraction.

First ignore the effect of single-slit diffraction and look only at the interference of the $N$ beams. The optical path difference and phase difference between light diffracted at angle $\theta$ from two adjacent slits are

$$
\delta=d\sin\theta,\qquad \Delta\varphi=\frac{2\pi}{\lambda}d\sin\theta.
$$
Let the amplitude of the light from each slit at $P$ be $E_1$. When $\Delta\varphi=2k\pi$ the $N$ phasors point the same way, the resultant amplitude is $NE_1$ and the intensity is $N^2$ times that of a single slit; these are the principal maxima:

**Formula 2.3.1 (Grating Equation)** For normally incident parallel light, the condition for the principal maxima of grating diffraction is

$$
d\sin\theta=k\lambda,\qquad k=0,\pm1,\pm2,\dots
\tag{2.2}
$$

The positions of the principal maxima are determined only by the grating constant $d$ and are independent of the slit width $a$; the smaller $d$, the larger the spacing of the principal maxima. Since $\lvert\sin\theta\rvert<1$, the largest visible order satisfies $k_{\max}<d/\lambda$.

### 2.3.3. Dark Fringes, Secondary Maxima and the Half-Angular Width of Principal Maxima

When $P$ is dark, the $N$ phasors joined head to tail form a closed polygon and the resultant is zero. The exterior angles of the polygon sum to an integer multiple of $2\pi$, that is, $N\Delta\varphi=2k'\pi$, where $k'$ is not an integer multiple of $N$ (otherwise we return to a principal maximum). Substituting $\Delta\varphi=2\pi d\sin\theta/\lambda$ gives the dark-fringe condition

$$
d\sin\theta=\frac{k'}{N}\lambda,\qquad k'=\pm1,\pm2,\dots,\ k'\ne Nk,
$$
or equivalently $d\sin\theta=\big(k+\frac{m}{N}\big)\lambda$, $k=0,\pm1,\dots$, $m=1,2,\dots,N-1$. From this:

- the spacing of the dark fringes is $1/N$ of the spacing of the principal maxima, and there are $N-1$ dark fringes between adjacent principal maxima;
- between two adjacent dark fringes lies a secondary maximum, so there are $N-2$ secondary maxima between adjacent principal maxima. Their intensities are very weak (for large $N$ even the strongest is only about $4.7\%$ of a principal maximum) and they are unimportant in gratings.

**Example 2.3.1 (Dark Fringes for Four Slits)** For $N=4$, how many dark fringes lie between the zeroth- and first-order principal maxima? What are the corresponding phase differences between adjacent slits?

**Solution** There are $N-1=3$ dark fringes, corresponding to $k=0$, $m=1,2,3$: $\sin\theta=\frac{\lambda}{4d},\frac{2\lambda}{4d},\frac{3\lambda}{4d}$, with phase differences between adjacent slits $\Delta\varphi=\frac\pi2,\pi,\frac{3\pi}2$. In the phasor diagram, the four phasors successively turn through $90^\circ$, $180^\circ$ and $270^\circ$, forming a square, a broken line of pairwise opposite phasors, and a square traversed in the opposite sense; the resultant vanishes in all cases. Between two dark fringes there are $N-2=2$ secondary maxima.

The half-angular width $\Delta\theta$ of a principal maximum is defined as the difference between the diffraction angle of the center of the principal maximum and that of the adjacent first dark fringe. The $k$-th order principal maximum satisfies $d\sin\theta_k=k\lambda$ and the adjacent dark fringe satisfies $d\sin(\theta_k+\Delta\theta)=k\lambda+\lambda/N$. Subtracting the two and using the smallness of $\Delta\theta$, $\sin(\theta_k+\Delta\theta)-\sin\theta_k\approx\cos\theta_k\,\Delta\theta$, we get

$$
\Delta\theta=\frac{\lambda}{Nd\cos\theta_k}.
\tag{2.3}
$$
$Nd$ is the total width of the grating: the larger it is, the sharper the principal maxima. The more slits, the more the intensity is concentrated at the principal maxima, and the fringes are both sharp and bright, which is the advantage of a grating over a double slit.

### 2.3.4. Modulation by Single-Slit Diffraction and Missing Orders

The amplitude $E_1$ at $P$ of the light diffracted by each slit itself varies with the diffraction angle, as given by Eq. (2.1). The grating diffraction pattern is therefore the result of multiple-beam interference modulated by single-slit diffraction:

1. The positions and half-angular widths of the principal maxima are unchanged and still determined by $d$, but their intensities are no longer equal; they are modulated by the intensity curve of single-slit diffraction (the envelope): the intensity of the $k$-th order principal maximum is $N^2I_1(\theta_k)$, where $I_1(\theta)$ is the single-slit diffraction intensity.
2. *Missing order*: if some diffraction angle satisfies both the interference condition for principal maxima $d\sin\theta=k\lambda$ and the single-slit dark-fringe condition $a\sin\theta=k'\lambda$ ($k'=\pm1,\pm2,\dots$), then the diffracted intensity of each slit vanishes there and the principal maximum that would have appeared is missing. Dividing the two equations, the missing orders are

   $$
   k=\frac{d}{a}k',\qquad k'=\pm1,\pm2,\dots
   $$
   For example, for $d=4a$ the orders $\pm4,\pm8,\dots$ are missing; when $d/a$ is not rational no order is missing.
3. $a$ determines the width of the central bright fringe of the single slit and $d$ determines the spacing of the principal maxima, so $d/a$ determines the number of principal maxima within the central bright fringe of the single slit (when no order is missing, $2d/a-1$ for integer $d/a$). When $a$ is fixed and $d$ decreases, the envelope is unchanged, the principal maxima become sparser, the number of principal maxima within the central bright fringe decreases, and the missing orders become lower; when $d$ is fixed and $a$ decreases, the positions of the principal maxima are unchanged, the envelope widens, and the number of principal maxima within the central bright fringe increases. In the extreme case $a\to\lambda$ the envelope is very flat and all principal maxima have almost the same intensity, but all are very weak, and grating diffraction tends to pure multiple-beam interference.

### 2.3.5. The Intensity Formula for Grating Diffraction

The amplitude at $P$ of the light diffracted by each slit is given by Eq. (2.1): $E_1=E_{10}\frac{\sin\alpha}{\alpha}$, $\alpha=\frac{\pi a\sin\theta}{\lambda}$, where $E_{10}$ is the amplitude at the center of the central bright fringe of a single slit. The $N$ phasors of amplitude $E_1$ whose phases differ successively by $\Delta\varphi$, joined head to tail, form $N$ sides of a regular polygon; let the radius of the circumscribed circle be $R$, so that $E_1=2R\sin\frac{\Delta\varphi}2$ and the resultant amplitude is $E_P=2R\sin\frac{N\Delta\varphi}2$. Setting

$$
\beta=\frac{\Delta\varphi}{2}=\frac{\pi d\sin\theta}{\lambda},
$$
we get $E_P=E_1\frac{\sin N\beta}{\sin\beta}$, and therefore

$$
I=I_{10}\Big(\frac{\sin\alpha}{\alpha}\Big)^2\Big(\frac{\sin N\beta}{\sin\beta}\Big)^2,\qquad \alpha=\frac{\pi a\sin\theta}{\lambda},\quad \beta=\frac{\pi d\sin\theta}{\lambda},
\tag{2.4}
$$
where $I_{10}$ is the intensity at the center of the central bright fringe of single-slit diffraction, $(\sin\alpha/\alpha)^2$ is called the single-slit diffraction factor, and $(\sin N\beta/\sin\beta)^2$ is called the multiple-beam interference factor. At $\beta=k\pi$ the multiple-beam interference factor reaches its maximum $N^2$, which is the grating equation (2.2); at $N\beta=k'\pi$ ($\beta\ne k\pi$) it is zero, giving the dark fringes. For $N=2$ the multiple-beam interference factor is $4\cos^2\beta$, and Eq. (2.4) is the double-slit diffraction intensity including the slit width, the exact form of Young's double-slit fringes, Eq. (1.4) of [5.4.1](/5.4.1#sec-1.2.3).

![Grating diffraction for N = 4 and d = 4a: single-slit diffraction factor (top), multiple-beam interference factor (middle) and their product (bottom). The positions of the principal maxima are determined by d, their intensities are modulated by the single-slit envelope, and orders ±4 fall on dark fringes of the single slit and are missing](./plots/grating-intensity.py)

### 2.3.6. Oblique Incidence and Phased Arrays

When parallel light is incident obliquely at angle of incidence $i$, the light at adjacent slits already has an optical path difference $d\sin i$ before the slits. Measuring both the angle of incidence $i$ and the diffraction angle $\theta$ from the grating normal and taking the same sense as positive, the total optical path difference between light diffracted at angle $\theta$ from adjacent slits is $d(\sin\theta-\sin i)$, and the condition for principal maxima is

$$
d(\sin\theta-\sin i)=k\lambda,\qquad k=0,\pm1,\pm2,\dots
$$
The zeroth-order principal maximum lies along $\theta=i$, the original direction of the incident light. At oblique incidence higher orders can be seen on one side (a higher chromatic resolving power, see Section 2.4.4) and correspondingly fewer on the other, the total number of visible fringes being unchanged; for a transmission grating the intensity is still concentrated near the zeroth order.

For the zeroth-order principal maximum, $\sin\theta=\sin i$, and the phase difference of the incident light at adjacent slits is $\Delta\varphi_0=2\pi d\sin i/\lambda$. Conversely, if instead of oblique incidence one directly applies successive phase differences $\Delta\varphi_0$ to a row of radiating elements, the zeroth-order principal maximum points in the direction

$$
\sin\theta_0=\frac{\lambda\,\Delta\varphi_0}{2\pi d},
$$
and changing the phase difference of the elements (phase-controlled scanning) or the frequency (frequency-controlled scanning) changes the beam direction without rotating the antenna; this is the principle of phased-array radar. Radio-telescope arrays, ultrasonic imaging probes, beamforming of 5G base stations and optical phased arrays are all based on the same principle.

**Example 2.3.2 (A One-Dimensional Radio-Telescope Array)** A one-dimensional radio-telescope array consists of $N=32$ antennas, each of width $a=2\,\mathrm{m}$, with adjacent antennas separated by $d=7\,\mathrm{m}$, working at the $21\,\mathrm{cm}$ line of neutral hydrogen. Find the angular spacing and half-angular width of the principal maxima, and state how many principal maxima lie within the pattern of a single antenna.

**Solution** The principal maxima satisfy $d\sin\theta=k\lambda$, and the angular spacing of adjacent principal maxima is about $\lambda/d=0.21/7=0.030\,\mathrm{rad}\approx1.7^\circ$. The half-angular width of the zeroth-order principal maximum is $\lambda/(Nd)=0.21/224\approx9.4\times10^{-4}\,\mathrm{rad}\approx3.2'$, far smaller than the diffraction angle of a single antenna, $\lambda/a\approx0.1\,\mathrm{rad}$: the resolving ability of the array is equivalent to that of an antenna about $Nd\approx224\,\mathrm{m}$ wide. The central main lobe of a single antenna lies between $\sin\theta=\pm\lambda/a=\pm0.105$ and contains the 7 principal maxima with $\lvert k\rvert\le3$ ($d/a=3.5$, and the missing orders are $k=\pm7,\pm14,\dots$).

### 2.3.7. Fraunhofer Diffraction and the Fourier Transform

The results obtained above with phasors share a unified mathematical form. Let the (complex amplitude) transmittance of the diffraction screen at $x$ be $t(x)$, with parallel light at normal incidence. For light diffracted at angle $\theta$, the wavelet from $x$ has an **optical path** shorter by $x\sin\theta$ than that from $x=0$; representing the vibrations by complex numbers ([5.1.6](/5.1.6#sec-6.1.4)), the complex amplitude at $P$ is

$$
\tilde E(\theta)\propto\int_{\mathbb{R}}t(x)\,\mathrm{e}^{-\mathrm{i}\xi x}\,\mathrm{d}x=\hat t(\xi),\qquad \xi=\frac{2\pi\sin\theta}{\lambda},
$$
that is, the complex amplitude distribution of Fraunhofer diffraction is the **Fourier transform** of the aperture transmittance ([2.5.6](/2.5.6#def-6.2.1)), with the spatial frequency $\xi$ determined by the diffraction angle. The role of the lens is to present this Fourier transform in its focal plane, which is the starting point of Fourier optics and optical information processing.

- Single slit: $t=\boldsymbol{1}_{[-a/2,\,a/2]}$, whose transform is $\hat t(\xi)=a\frac{\sin(\xi a/2)}{\xi a/2}$ ([Example 6.2.1 of 2.5.6](/2.5.6#ex-6.2.1)), and $\xi a/2=\alpha$; squaring gives Eq. (2.1).
- Grating: the transmittance of $N$ slits is the **convolution** of the single-slit transmittance with a sum of $N$ delta functions spaced $d$ apart. By the **convolution theorem** ([2.5.6](/2.5.6#thm-6.2.4)), its transform is the product of the two transforms: the single-slit $\hat t$ times $\sum_{n=0}^{N-1}\mathrm{e}^{-\mathrm{i}n\xi d}$, whose modulus is $\lvert\sin N\beta/\sin\beta\rvert$ with $\beta=\xi d/2$; squaring gives Eq. (2.4). "Single-slit diffraction modulates multiple-beam interference" is the physical statement of the convolution theorem.
- The inverse relation of diffraction: the narrower the aperture, the wider the transform. This is the scaling property of the Fourier transform and also the manifestation in optics of the **uncertainty principle** ([2.5.6](/2.5.6#sec-6.3.4)); the position–momentum uncertainty relation of quantum mechanics has the same mathematical root ([5.5.2](/5.5.2)).
- Circular aperture: Fraunhofer diffraction by a two-dimensional aperture is a two-dimensional Fourier transform ([2.5.6](/2.5.6#sec-6.2.5)), and the transform of a circular aperture is expressed by the first-order **Bessel function of the first kind** (Section 2.4.1).

## 2.4. Resolving Power of Optical Instruments

### 2.4.1. Fraunhofer Diffraction by a Circular Aperture

Parallel light illuminates a circular hole of diameter $D$, and in the focal plane of the lens one obtains a diffraction pattern with a bright circular spot in the center surrounded by alternating bright and dark concentric rings.

**Definition 2.4.1 (Airy Disk)** In the Fraunhofer diffraction pattern of a circular aperture, the central bright spot bounded by the first dark ring is called the **Airy disk**.

It was first calculated by the British astronomer Airy in 1835. Taking the Fourier transform of the two-dimensional aperture, the intensity of circular-aperture diffraction is

$$
I=I_0\Big[\frac{2J_1(u)}{u}\Big]^2,\qquad u=\frac{\pi D\sin\theta}{\lambda},
$$
where $J_1$ is the **Bessel function of the first kind** of order one. The first positive zero of $J_1$ is $u=3.832=1.22\pi$, so the diffraction angle $\theta_1$ of the first dark ring (the edge of the Airy disk) satisfies

$$
\sin\theta_1=1.22\frac{\lambda}{D}.
$$
$\theta_1$ is called the half-angular width of the Airy disk; for focal length $f$ the radius of the Airy disk is $r_1\approx1.22f\lambda/D$. Compared with a single slit of width $a$ ($\sin\theta_1=\lambda/a$), the extra factor $1.22$ comes from the circular aperture. The Airy disk contains about $84\%$ of the diffracted light energy, and its center is the geometrical-optics image of the point source.

**Remark 2.4.1** The Airy disk (bright in the center) and the Poisson spot (Section 2.1.1) are different things: the former is the Fraunhofer diffraction of a circular hole, and the latter is the bright spot of Fresnel diffraction at the center of the shadow of an opaque circular disk.

### 2.4.2. The Rayleigh Criterion

Geometrical optics holds that an object point is imaged by a lens as an image point, and an object (a collection of object points) as an image (a collection of image points). From the viewpoint of wave optics, the rim of the lens is a circular aperture, the image of an object point is an Airy disk, and the image is a collection of Airy disks. When two object points are too close, their Airy disks overlap and cannot be separated, so diffraction limits the ability of optical instruments to resolve detail.

**Definition 2.4.2 (Rayleigh Criterion)** For two incoherent object points of equal intensity, if the center of the image spot of one falls exactly on the first dark ring of the other, the two object points are regarded as just resolved; this is called the **Rayleigh criterion**. If the image spots come closer than this, the points cannot be resolved.

Since the two object points are incoherent, the intensity on the screen is the direct sum (incoherent superposition) of two Airy distributions. When just resolved by the Rayleigh criterion, the combined intensity between the two peaks is about $73.5\%$ of each peak value, a dip that the human eye and ordinary detectors can perceive.

![Images of two incoherent point sources of equal intensity. Left: separation larger than the minimum resolvable angle, resolved; middle: separation equal to the minimum resolvable angle (Rayleigh criterion), the intensity in between drops to about 73.5% of the peak; right: smaller separation, the images merge into one peak and cannot be resolved](./plots/rayleigh-criterion.py)

**Formula 2.4.1 (Minimum Resolvable Angle)** The angle subtended at the center of the lens by two object points that are just resolved is called the minimum resolvable angle (angular resolution). By the Rayleigh criterion it equals the half-angular width of the Airy disk:

$$
\theta_{\min}=\theta_1\approx1.22\frac{\lambda}{D},
\tag{2.5}
$$
and its reciprocal is called the resolving power of the optical instrument:

$$
R=\frac1{\theta_{\min}}=\frac{D}{1.22\lambda}.
$$

### 2.4.3. Telescopes, Microscopes and the Human Eye

By Eq. (2.5), there are only two ways to improve the resolving power: increase the aperture $D$ or decrease the wavelength $\lambda$.

- Telescopes: the observed wavelength is set by the celestial object, so only the aperture can be increased. The largest ground-based optical telescopes have apertures of about $10\,\mathrm{m}$ (assembled from many hexagonal mirror segments), and the European Extremely Large Telescope (ELT) under construction in Chile has a primary mirror of $39\,\mathrm{m}$. The actual resolution of ground-based telescopes is also limited by atmospheric turbulence and requires adaptive-optics correction, so space telescopes (the Hubble telescope with a $2.4\,\mathrm{m}$ aperture, the infrared James Webb telescope launched in December 2021 with $6.5\,\mathrm{m}$) have a distinctive advantage. Radio telescopes work at wavelengths of centimeters to meters and so must be made very large: the 500 m Aperture Spherical Telescope (FAST) in Guizhou has an effective illuminated aperture of about $300\,\mathrm{m}$ in observation, and for the $21\,\mathrm{cm}$ line its minimum resolvable angle is about $1.22\times0.21/300\,\mathrm{rad}\approx3'$. Combining widely separated radio telescopes into an interferometric array (very-long-baseline interferometry, [5.4.1](/5.4.1#sec-1.4.3)) gives an equivalent aperture as large as the diameter of the Earth.
- Microscopes: the objective aperture cannot be very large, but the wavelength can be reduced, for example by illuminating with ultraviolet light or by switching to electron beams. The de Broglie wavelength of electrons accelerated through tens of kilovolts is only of the order of $10^{-3}$–$10^{-2}\,\mathrm{nm}$ ([5.5.2](/5.5.2)), five orders of magnitude shorter than visible light, so electron microscopes have very high resolving power and can image structures on the atomic scale.
- The human eye: under normal illumination the pupil diameter is about $3\,\mathrm{mm}$.

**Example 2.4.1 (Resolving Ability of the Human Eye)** For yellow-green light of $\lambda=550\,\mathrm{nm}$, what is the minimum resolvable angle of the human eye? At what distance can it just resolve two points $2\,\mathrm{mm}$ apart?

**Solution** $\theta_{\min}=1.22\times\frac{550\times10^{-9}}{3\times10^{-3}}\,\mathrm{rad}\approx2.2\times10^{-4}\,\mathrm{rad}\approx0.8'$, about $1'$. For just resolved points, $l=\frac{2\times10^{-3}\,\mathrm{m}}{2.2\times10^{-4}}\approx9\,\mathrm{m}$. This is why the two headlights of a car approaching from far away at night first look like a single bright spot and separate into two only when it comes closer.

### 2.4.4. Grating Spectra, Angular Dispersion and Chromatic Resolving Power

By the grating equation $d\sin\theta=k\lambda$, for a given order $k\ne0$ the principal maxima of different wavelengths lie at different diffraction angles, so polychromatic light is spread by wavelength into a spectrum, called a grating spectrum; the zeroth-order principal maximum, where all wavelengths coincide, remains white. The grating spectrum of white light (about $400$–$760\,\mathrm{nm}$) is a continuous colored band with violet on the inside and red on the outside, and at slightly higher orders the spectra of adjacent orders overlap; the spectra of atomic sources such as mercury and sodium lamps consist of discrete lines (for the origin of atomic spectra see [5.5.4](/5.5.4)). A prism disperses light by **dispersion**, whereas a grating does so by diffraction; the **dispersion** of a grating is approximately linear and the grating can be used in wavelength ranges in which prism materials are opaque.

Whether two spectral lines can be separated depends both on how far apart their centers are and on the widths of the lines themselves.

**Definition 2.4.3** Let the diffraction angles of the same order of two beams of wavelengths $\lambda$ and $\lambda+\delta\lambda$ differ by $\delta\theta$.

1. The **angular dispersion** (dispersive power) is defined as $D_\theta=\dfrac{\delta\theta}{\delta\lambda}$; it expresses how far apart in angle two spectral lines of unit wavelength difference are.
2. If $\delta\lambda$ is the smallest wavelength difference at which two spectral lines are just resolved, then $R=\dfrac{\lambda}{\delta\lambda}$ is called the **chromatic resolving power**.

Differentiating both sides of the grating equation (with $k$ fixed), $d\cos\theta_k\,\delta\theta=k\,\delta\lambda$, so the angular dispersion of the grating is

$$
D_\theta=\frac{k}{d\cos\theta_k}.
$$
Decreasing $d$ or using a higher order increases the angular dispersion, which is independent of the number of slits $N$. The angular dispersion reflects only how far apart the centers of two lines are and cannot tell whether they overlap, because the lines themselves have width.

By the Rayleigh criterion, two spectral lines are just resolved when the difference of their diffraction angles equals the half-angular width (2.3) of a line:

$$
D_\theta\,\delta\lambda=\frac{k\,\delta\lambda}{d\cos\theta_k}=\frac{\lambda}{Nd\cos\theta_k},
$$
which gives the chromatic resolving power of the grating

$$
R=\frac{\lambda}{\delta\lambda}=Nk,\qquad k\ne0.
\tag{2.6}
$$
Large $N$ gives sharp lines and large $k$ gives strong dispersion. The grating constant $d$ does not appear in Eq. (2.6), but the smaller $d$, the lower the highest usable order $d/\lambda$; for a given total grating width $Nd$, the upper limit of $R$ is $Nd/\lambda$ ($\sin\theta\to1$), so a high chromatic resolving power ultimately requires a wide grating.

**Example 2.4.2 (The Sodium Doublet)** The yellow light of sodium atoms consists of two very close spectral lines (the sodium doublet), $\lambda_1=589.0\,\mathrm{nm}$ and $\lambda_2=589.6\,\mathrm{nm}$. How many slits must a grating have at least to resolve them in the second and third order spectra?

**Solution** The required chromatic resolving power is $R=\frac{\lambda}{\delta\lambda}\approx\frac{589.3}{0.6}\approx982$. From $R=Nk$, $N\ge491$ in the second order and $N\ge328$ in the third. Ordinary gratings have tens of thousands of slits, so resolving the sodium doublet is no problem. The origin of the sodium doublet (spin–orbit coupling) is discussed in [5.5.4](/5.5.4).

## 2.5. X-Ray Diffraction

### 2.5.1. X-Rays

In 1895, while studying the discharge in a cathode-ray tube, Röntgen found that the tube emitted an invisible, highly penetrating radiation that made fluorescent materials glow and exposed photographic plates; he called it *X-rays*, the unknown rays. In an X-ray tube, thermal electrons emitted from the cathode are accelerated by a voltage of tens of kilovolts between cathode and anode and strike a metal target such as molybdenum, tungsten or copper, producing X-rays; their spectrum consists of a continuous spectrum and the characteristic lines of the target element, and the mechanism is discussed in [5.5.5](/5.5.5).

The nature of X-rays was at first unclear. If they were waves, their wavelength should be so much shorter than that of visible light that ordinary gratings could not produce observable diffraction. In 1912 Laue realized that the atoms in a crystal are arranged regularly with spacings of the order of $0.1\,\mathrm{nm}$ and could serve as a natural three-dimensional grating for X-rays. His collaborators sent X-rays through a copper sulfate crystal and obtained a regular pattern of spots on a photographic plate, called *Laue spots*. This proved at once that X-rays are very short-wavelength **electromagnetic waves** and that the atoms inside a crystal are arranged periodically. The wavelength of X-rays is about $10^{-2}$–$10\,\mathrm{nm}$ (see the electromagnetic spectrum in [5.3.10](/5.3.10#sec-10.3.2)). Laue received the 1914 Nobel Prize in Physics for this.

### 2.5.2. Crystal Structure and Families of Lattice Planes

A crystal structure can be viewed as the same group of atoms (the basis) placed at each point of a periodic lattice, that is, "crystal structure = lattice + basis". The lattice is a mathematical abstraction reflecting the spatial periodicity of the crystal, and its smallest repeating unit is a parallelepiped (the primitive cell). The atoms of a crystal can be regarded as lying on sets of parallel planes called lattice planes, and the atoms in each plane have two-dimensional periodicity.

**Definition 2.5.1 (Family of Lattice Planes)** A set of parallel lattice planes with the same spatial orientation and equal spacing is called a **family of lattice planes**, and the distance $d$ between two adjacent planes is called the interplanar spacing. The same crystal can be divided into many families of lattice planes of different orientations, with different interplanar spacings.

### 2.5.3. The Bragg Equation

When X-rays strike a crystal, the electrons in the atoms undergo **forced oscillation** under the electric field of the incident wave and radiate electromagnetic waves of the same frequency in all directions (electric dipole radiation, [5.3.10](/5.3.10#sec-10.4.2)); each atom is a source of wavelets. These wavelets are coherent, and X-ray diffraction by a crystal is their interference. In 1913 W. H. Bragg and W. L. Bragg, father and son, proposed a simple treatment in two steps:

1. The interference of the wavelets from the atoms of one lattice plane. This is a diffraction problem for a two-dimensional grating; one can show that the direction of its zeroth-order principal maximum is the direction of reflection with the lattice plane as mirror (the incident and diffracted rays make equal angles with the plane and the diffracted ray lies in the plane of incidence), for which the optical paths from all atoms of the plane are equal. In what follows the diffracted light in this direction is called the "reflected light" of the plane.
2. The interference among the reflected light from a family of parallel lattice planes. Let the angle between the incident X-ray and the lattice planes (the glancing angle) be $\theta$; the optical path difference between the light reflected from two adjacent planes is $2d\sin\theta$.

This gives the condition for the reflected light to reinforce:

**Formula 2.5.1 (Bragg Equation)** For a family of lattice planes with interplanar spacing $d$, the condition for a diffraction principal maximum in the direction of glancing angle $\theta$ is

$$
2d\sin\theta=k\lambda,\qquad k=1,2,3,\dots
\tag{2.7}
$$

Some remarks on the Bragg equation:

- A crystal contains many families of lattice planes with different orientations and interplanar spacings $d_1,d_2,\dots$. Once the relative orientation of the incident X-ray and the crystal is fixed, the glancing angles $\theta_1,\theta_2,\dots$ of the families are determined, and each family has its own Bragg condition $2d_j\sin\theta_j=k_j\lambda$.
- For X-rays of a single wavelength, in a fixed orientation none of these conditions is generally satisfied, and occasionally one or two are. To obtain diffraction spots, either the wavelength or the orientation must vary continuously (Section 2.5.4).
- Diffracted light in the nonzero-order directions between parallel lattice planes can also reinforce, but one can show that these directions of reinforcement are exactly those given by the Bragg condition of another family of lattice planes. The Bragg conditions of all the families therefore describe completely the distribution of principal maxima in X-ray diffraction by a crystal.
- Since $\sin\theta\le1$, only waves with $\lambda<2d$ can undergo Bragg diffraction, which is why visible light cannot be diffracted by crystals while X-rays can.

**Example 2.5.1 (Diffraction Angles for NaCl)** A family of lattice planes of an NaCl crystal has interplanar spacing $d=0.282\,\mathrm{nm}$ and is illuminated with the $\mathrm{K}_\alpha$ line of a copper target ($\lambda=0.154\,\mathrm{nm}$). Find the glancing angles of the successive orders of diffraction.

**Solution** $\sin\theta_k=\frac{k\lambda}{2d}=0.273k$. For $k=1$, $\theta_1=15.8^\circ$; for $k=2$, $\theta_2=33.1^\circ$; for $k=3$, $\theta_3=55.0^\circ$; for $k=4$, $\sin\theta>1$, so there are only three orders. Conversely, measuring $\theta$ with known $\lambda$ gives the interplanar spacing, and measuring $\theta$ with known $d$ of the crystal gives the wavelength of the X-rays, the latter being the basis of X-ray spectroscopy.

**Remark 2.5.1** By Section 2.3.7, the amplitude of Fraunhofer diffraction is the Fourier transform of the aperture function; likewise, the amplitude of X-ray diffraction by a crystal is the three-dimensional Fourier transform of the electron density in the crystal. The Fourier transform of a periodic lattice is nonzero only at the points of another lattice (the reciprocal lattice), and the condition for a diffraction principal maximum is that the difference between the incident and diffracted **wave vectors** equals a reciprocal-lattice vector (the Laue condition), which is equivalent to the Bragg equation. From the intensities of the diffraction spots one can recover the electron density; this is the principle by which X-ray crystallography determines molecular structure (the discovery of the DNA double helix relied on X-ray diffraction patterns).

W. H. Bragg and W. L. Bragg shared the 1915 Nobel Prize in Physics for the analysis of crystal structure with X-rays.

### 2.5.4. Experimental Methods

1. The Laue method: the orientation of the incident X-ray relative to the crystal is fixed, that is, the $d_j$ and $\theta_j$ of the families of lattice planes are fixed, and a single crystal is illuminated with X-rays of continuously distributed wavelength so that each family has some wavelength satisfying the Bragg condition. Each diffraction principal maximum forms a bright spot (Laue spot) on the film, and the photograph is called a Laue pattern. The symmetry of the Laue pattern reflects the symmetry of the crystal and is often used to determine the direction of crystal axes.
2. The powder method (Debye–Scherrer method): a polycrystalline powder is illuminated with X-rays of a single wavelength. The powder consists of a large number of small crystallites with random orientations, and the glancing angles of the families of lattice planes are quasi-continuously distributed over all possible values, so crystallites satisfying the Bragg condition produce diffraction on a cone about the incident ray with half-opening angle $2\theta$, forming a series of concentric rings on the film; the photograph is called a Debye pattern. From the $\theta$ of each ring one finds the interplanar spacings and hence determines the lattice constants and the phases present.

## Summary

| Topic | Key points |
|---|---|
| Huygens–Fresnel principle | Each surface element of the wavefront is a source of wavelets, and the vibration at any point in space is determined by the coherent superposition of the wavelets |
| Classification of diffraction | Fresnel diffraction (near field); Fraunhofer diffraction (far field, parallel light, realized with lenses) |
| Single slit | Dark fringes $a\sin\theta=\pm k\lambda$; $I=I_0(\sin\alpha/\alpha)^2$, $\alpha=\pi a\sin\theta/\lambda$; secondary maxima at $a\sin\theta\approx\pm1.43\lambda,\pm2.46\lambda,\dots$ |
| Fringe width | Central bright fringe $\Delta\theta_0=2\lambda/a$, $\Delta x_0=2f\lambda/a$; the other bright fringes are half as wide |
| Grating | Principal maxima $d\sin\theta=k\lambda$; dark fringes $d\sin\theta=(k+m/N)\lambda$; half-angular width $\Delta\theta=\lambda/(Nd\cos\theta_k)$ |
| Missing orders and intensity | Missing orders $k=(d/a)k'$; $I=I_{10}(\sin\alpha/\alpha)^2(\sin N\beta/\sin\beta)^2$, $\beta=\pi d\sin\theta/\lambda$ |
| Oblique incidence | $d(\sin\theta-\sin i)=k\lambda$; phased array $\sin\theta_0=\lambda\Delta\varphi_0/(2\pi d)$ |
| Fourier transform | The complex amplitude of Fraunhofer diffraction is the Fourier transform of the aperture transmittance; grating = convolution of a single slit with a periodic delta function |
| Resolving power | Airy disk $\sin\theta_1=1.22\lambda/D$; $\theta_{\min}=1.22\lambda/D$, $R=D/(1.22\lambda)$ |
| Grating spectra | Angular dispersion $D_\theta=k/(d\cos\theta_k)$; chromatic resolving power $R=\lambda/\delta\lambda=Nk$ |
| X-ray diffraction | Bragg equation $2d\sin\theta=k\lambda$; Laue method (continuous spectrum, single crystal) and powder method (monochromatic, polycrystal) |

## Questions

1. In a single-slit diffraction experiment, if the slit is translated along the optical axis, does the diffraction pattern move? What if it is translated perpendicular to the optical axis?

   **Answer** in neither case does the pattern move. A Fraunhofer diffraction pattern depends only on the diffraction angle, and parallel light of the same diffraction angle always converges to the same point in the focal plane of the lens, regardless of the position of the slit (this is also why the diffraction patterns of the slits in a grating can coincide).

2. Why must telescopes have especially large apertures?

   **Answer** first for the resolving power, $\theta_{\min}=1.22\lambda/D$; second to collect more light and detect fainter objects, the light-gathering power being proportional to $D^2$.

3. What are the differences among resolving power, angular dispersion and chromatic resolving power?

   **Answer** the resolving power describes the ability of an instrument to resolve two close object points and is determined by the aperture; the angular dispersion describes how far apart in angle the centers of the lines of two wavelengths are, is determined by $k/(d\cos\theta)$ and is independent of $N$; the chromatic resolving power also takes into account the width of the lines themselves, $R=Nk$.

4. How do the angular dispersion and the chromatic resolving power of a grating change when the grating constant $d$ decreases?

   **Answer** the angular dispersion $k/(d\cos\theta_k)$ of a given order increases; the chromatic resolving power $Nk$ is unchanged for fixed $N$ and $k$, but the highest usable order $d/\lambda$ decreases.

5. Sketch the intensity curve of grating diffraction for $N=3$ and $d=4a$.

   **Answer** the principal maxima are at $\sin\theta=k\lambda/d$, with orders $\pm4,\pm8,\dots$ missing; between adjacent principal maxima there are $2$ dark fringes and $1$ secondary maximum, whose intensity is $1/9$ of that of a principal maximum (without the single-slit factor); the whole pattern is modulated by the $(\sin\alpha/\alpha)^2$ envelope.

6. The wavelength of sound is comparable to the size of doors and windows, while visible light has a wavelength far smaller, so we can "hear but not see" a person around a corner. What would the world be like if the wavelength of light were also of the order of meters?

   **Answer** light would bend around houses and people as sound does, shadows would be blurred, the resolution of imaging systems would be extremely low, and an eye would have to be as large as a house to see objects clearly.
