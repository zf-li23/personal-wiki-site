---
title: The Quantum Nature of Light
description: Thermal radiation and black bodies, Kirchhoff's law, the Stefan–Boltzmann law and Wien's displacement law, the ultraviolet catastrophe, Planck's law and the energy quantum; the photoelectric effect, Einstein's photon theory and the photoelectric equation; photon energy and momentum, wave–particle duality of light; Compton scattering and the Compton wavelength.
source_hash: 630f55ebd1cd
---

By the end of the nineteenth century classical physics seemed nearly complete: Newtonian and analytical mechanics handled mechanical problems, Maxwell's theory unified electricity, magnetism and light, and thermodynamics and statistical mechanics explained thermal phenomena. Yet one of the "two clouds" that Kelvin saw on the horizon, the distribution of thermal radiation over frequency, could not be explained correctly by classical theory (the other led to special relativity, see [5.1.8](/5.1.8)). In 1900 Planck proposed the energy quantum hypothesis to solve this problem, and quantum theory was born. In 1905 Einstein introduced the light quantum; in 1913 Bohr applied quantization to the atom; in 1923 Compton scattering confirmed the momentum of the photon. In 1924 de Broglie proposed matter waves; in 1925–1926 Heisenberg's matrix mechanics and Schrödinger's wave mechanics were established one after the other, and Born gave the statistical interpretation of the wave function. In 1927 electron **diffraction** confirmed matter waves and Heisenberg stated the uncertainty relation, and in 1928 Dirac wrote down the relativistic **wave equation** of the electron. Together with relativity, quantum mechanics forms one of the two pillars of modern physics; it underlies atomic, molecular, solid-state and nuclear physics, as well as the theory of the chemical bond and physical chemistry.

The quantum world is at odds with everyday experience, and trying to understand it with classical concepts often leads to difficulties. The basic postulates of quantum mechanics can only be tested by experiment: accepting them and using them to analyze problems is the first step toward understanding quantum physics. This chapter discusses three experiments that reveal the particle nature of light. Blackbody radiation (Section 1.1) requires that electromagnetic radiation exchange energy in units of $h\nu$; the photoelectric effect (Section 1.2) shows that light is absorbed in units of $h\nu$, from which Einstein proposed the photon (Section 1.3); Compton scattering (Section 1.4) shows that the photon also carries momentum $h/\lambda$ and obeys energy and momentum conservation in a single collision. The tools come from earlier courses: the **equipartition theorem** and the **Boltzmann distribution** from the kinetic theory of gases ([5.2.1](/5.2.1)), **standing waves** and **normal modes** from the study of waves ([5.1.7](/5.1.7#sec-7.7)), and the energy–momentum relation of special relativity ([5.1.8](/5.1.8#sec-8.9.3)). The next chapter, [5.5.2](/5.5.2), extends wave–particle duality to massive particles such as electrons and introduces probability waves and the uncertainty relation.

## 1.1. Blackbody Radiation

The study of thermal radiation has practical motivations (improving the efficiency of lighting, measuring high temperatures, determining the surface temperatures of stars) as well as theoretical significance: it lies where thermodynamics meets electromagnetic theory. Laue once remarked that the union of these two disciplines would produce a child "destined to cause the greatest revolution in physics."

### 1.1.1. Thermal Radiation

Heat a piece of iron and at first it does not appear to glow; as its temperature rises it turns dull red, orange, yellow-white and then blue-white. Both the intensity and the frequency distribution of the **electromagnetic waves** a body radiates depend on its temperature.

**Definition 1.1.1 (Thermal Radiation)** Electromagnetic radiation determined by the temperature of a body is called **thermal radiation**. Thermal radiation in which the energy a body radiates per unit time equals the energy it absorbs, so that its temperature stays constant, is called equilibrium thermal radiation.

Every body (gas, liquid or solid) emits thermal radiation at every temperature. The spectrum of thermal radiation is continuous: it contains all frequencies, with different intensities. The higher the temperature, the larger the share of short wavelengths: the human body (about $310\,\mathrm{K}$) radiates mainly in the infrared, a glowing hot object emits visible light, and an extremely hot object emits ultraviolet light. Infrared imaging and infrared thermometry both make use of thermal radiation. The light from lasers, fluorescent lamps and fluorescence, in contrast, is not thermal radiation: it comes from transitions of atoms between particular energy levels and has no direct relation to the temperature of the body ([5.5.5](/5.5.5)).

**Definition 1.1.2 (Spectral Exitance)** Let $\mathrm{d}M$ be the energy of electromagnetic waves with frequencies between $\nu$ and $\nu+\mathrm{d}\nu$ emitted per unit time from a unit area of a body at temperature $T$. Then

$$
M_\nu(T)=\frac{\mathrm{d}M}{\mathrm{d}\nu}
$$
is called the **spectral exitance** (spectral radiant exitance) of the body, with unit $\mathrm{W\,m^{-2}\,Hz^{-1}}$. Its integral over all frequencies

$$
M(T)=\int_0^\infty M_\nu(T)\,\mathrm{d}\nu
$$
is called the total exitance, with unit $\mathrm{W\,m^{-2}}$.

Besides frequency and temperature, $M_\nu(T)$ also depends on the material and the surface condition of the body. The spectral exitance can also be defined per unit wavelength, $M_\lambda=\mathrm{d}M/\mathrm{d}\lambda$; since $\nu=c/\lambda$, we have $M_\lambda\,\lvert\mathrm{d}\lambda\rvert=M_\nu\,\lvert\mathrm{d}\nu\rvert$, that is, $M_\lambda=\frac{c}{\lambda^2}M_\nu$.

### 1.1.2. Black Bodies and Kirchhoff's Law of Thermal Radiation

Besides radiating, a body absorbs and reflects the electromagnetic waves that fall on its surface. The fraction of incident energy near frequency $\nu$ that is absorbed is denoted $\alpha_\nu(T)$ and called the spectral absorptance.

**Definition 1.1.3 (Black Body)** A body that completely absorbs electromagnetic waves of every frequency without reflecting any, that is, a body with $\alpha_\nu(T)=1$, is called an (ideal) **black body**.

A black body is an idealized model: even soot and black enamel absorb less than $99\%$ of sunlight. The model designed by Wien is a cavity with a small hole: an electromagnetic wave entering the hole is reflected many times inside, losing part of its energy at each reflection, and has almost no chance of leaving through the hole again, so the hole behaves approximately like the surface of a black body. When the cavity walls are kept at temperature $T$, the radiation emerging from the hole is blackbody radiation.

**Theorem 1.1.1 (Kirchhoff's Law of Thermal Radiation)** In equilibrium thermal radiation, the ratio of the spectral exitance to the spectral absorptance is the same for every body and equals the spectral exitance of a black body at the same temperature:

$$
\frac{M_{1\nu}(T)}{\alpha_{1\nu}(T)}=\frac{M_{2\nu}(T)}{\alpha_{2\nu}(T)}=\cdots=M_{\mathrm{B}\nu}(T),\tag{1.1}
$$
where $M_{\mathrm{B}\nu}(T)$ is a universal function independent of the material.

Kirchhoff (1859–1860) justified this result thermodynamically: if some body radiated more than it absorbed at some frequency, then placing it together with other bodies in an isothermal closed cavity would make it cool spontaneously and the others warm spontaneously, in violation of the **second law of thermodynamics**. Theorem 1.1.1 has the following consequences:

- The spectral exitance of a black body is the largest possible, because $\alpha_\nu\le1$.
- A good absorber is also a good emitter. Viewed by reflected light at room temperature, a porcelain plate with a black pattern on a white background shows a dark pattern on a bright ground; heated to about $1100\,\mathrm{K}$ and viewed in the dark by its own radiation, the black pattern is brighter than the white background.
- Once $M_{\mathrm{B}\nu}(T)$ and the $\alpha_\nu$ of a body are known, its radiation is known. Studying the black body therefore allows us to set aside the particular properties of materials and study the laws of thermal radiation itself.

In what follows, $M_\nu(T)$ denotes the spectral exitance of a black body.

### 1.1.3. Experimental Laws of Blackbody Radiation

Heat a cavity black body, separate the radiation from the hole by frequency with a **diffraction grating** spectrometer, and measure the exitance at each frequency with a thermocouple; this gives the blackbody spectrum $M_\nu(T)$. The left panel of the figure below shows the curves at three temperatures (the curves drawn here are in fact the theoretical curves from Planck's law below, which agree with experiment to within the measurement accuracy). The area under a curve is the total exitance $M(T)$. Experiment yields two laws.

**Theorem 1.1.2 (Stefan–Boltzmann Law)** The total exitance of a black body is proportional to the fourth power of the thermodynamic temperature:

$$
M(T)=\sigma T^4,\qquad\sigma=5.670\times10^{-8}\,\mathrm{W\,m^{-2}\,K^{-4}}.\tag{1.2}
$$

Here $\sigma$ is called the Stefan–Boltzmann constant. Stefan obtained this law from experiment in 1879, and Boltzmann proved it theoretically in 1884 from thermodynamics and the relation to electromagnetic **radiation pressure**.

**Theorem 1.1.3 (Wien's Displacement Law)** The peak frequency $\nu_{\mathrm{m}}$ of the spectral exitance $M_\nu(T)$ of a black body is proportional to the temperature:

$$
\nu_{\mathrm{m}}=C_\nu T,\qquad C_\nu=5.879\times10^{10}\,\mathrm{Hz/K};\tag{1.3}
$$
the peak wavelength $\lambda_{\mathrm{m}}$ of the spectral exitance per unit wavelength $M_\lambda(T)$ is inversely proportional to the temperature:

$$
\lambda_{\mathrm{m}}T=b,\qquad b=2.898\times10^{-3}\,\mathrm{m\,K}.
$$

Wien derived this law from thermodynamics in 1893. Note that $M_\nu$ and $M_\lambda$ are two different densities, so their peaks do not correspond to the same place in the spectrum: $c/\lambda_{\mathrm{m}}=c\,T/b\approx0.57\,\nu_{\mathrm{m}}$, which is not equal to $\nu_{\mathrm{m}}$.

The two laws are the physical basis of high-temperature measurement, remote sensing and infrared tracking. Treating the Sun as a black body and measuring the peak wavelength of its radiation spectrum, $\lambda_{\mathrm{m}}\approx510\,\mathrm{nm}$, Wien's displacement law gives a surface temperature $T\approx5700\,\mathrm{K}$ (the effective temperature determined from the total exitance is $5772\,\mathrm{K}$). For the human body $\lambda_{\mathrm{m}}\approx9.3\,\mu\mathrm{m}$; the cosmic microwave background is nearly ideal blackbody radiation at a temperature of $2.725\,\mathrm{K}$, with $\lambda_{\mathrm{m}}\approx1.06\,\mathrm{mm}$.

![Blackbody spectra. Left: spectral exitance $M_\nu$ (Planck's law) at T = 3000 K, 4500 K and 6000 K; the peak frequency shifts linearly with temperature and the area under the curve grows as T⁴. Right: Planck's law compared with Wien's formula and the Rayleigh–Jeans formula at T = 1600 K; the latter diverges at high frequency](./plots/blackbody-spectrum.py)

### 1.1.4. The Failure of Classical Theory: The Ultraviolet Catastrophe

How can the functional form of $M_\nu(T)$ be derived theoretically? There were two well-known attempts at the end of the nineteenth century.

**Formula 1.1.1 (Wien's Formula)** From thermodynamic arguments and experimental data, Wien obtained in 1896

$$
M_\nu(T)=\alpha\nu^3\mathrm{e}^{-\beta\nu/T},
$$
where $\alpha$ and $\beta$ are constants. It agrees with experiment at high frequencies but is clearly too low at low frequencies.

Rayleigh (1900) and Jeans (1905) instead regarded the radiation in the cavity as electromagnetic **standing waves** with **nodes** at the walls, treated each **normal mode** as a harmonic oscillator, and computed its average energy by classical statistics. Let the cavity be a cube of side $L$ whose walls are perfect **conductors**. By separation of variables in the wave equation ([2.5.4](/2.5.4)), the **wave vector** of a standing wave can only take the values $\boldsymbol{k}=\frac{\pi}{L}(n_x,n_y,n_z)$ with $n_x,n_y,n_z$ positive integers, and the frequency is $\nu=\frac{c}{2\pi}\lvert\boldsymbol{k}\rvert$. In $(n_x,n_y,n_z)$ space the modes with frequency below $\nu$ correspond to the lattice points in the first octant of a sphere of radius $2L\nu/c$, and each lattice point carries two independent **polarization** directions, so the number of modes is

$$
N(\nu)=2\cdot\frac18\cdot\frac{4\pi}{3}\Big(\frac{2L\nu}{c}\Big)^3=\frac{8\pi L^3\nu^3}{3c^3}.
$$
The number of modes per unit volume with frequencies between $\nu$ and $\nu+\mathrm{d}\nu$ is $\frac{1}{L^3}\frac{\mathrm{d}N}{\mathrm{d}\nu}\mathrm{d}\nu=\frac{8\pi\nu^2}{c^3}\mathrm{d}\nu$ (this result does not depend on the shape of the cavity). If the average energy of a mode is $\bar\varepsilon$, the spectral energy density of the radiation in the cavity is $u_\nu=\frac{8\pi\nu^2}{c^3}\bar\varepsilon$. The radiation in the cavity is isotropic and propagates at the speed of light $c$, so the energy leaving a unit area of the hole per unit time is $M_\nu=\frac{c}{4}u_\nu$ (the derivation is the same as for the rate $\frac14n\bar v$ at which gas molecules hit a wall, [5.2.1](/5.2.1#sec-1.6.2)), and therefore

$$
M_\nu(T)=\frac{2\pi\nu^2}{c^2}\,\bar\varepsilon.\tag{1.4}
$$
The energy of each oscillator contains two quadratic terms (kinetic and potential), so by the **equipartition theorem** ([Theorem 1.4.1](/5.2.1#thm-1.4.1)), $\bar\varepsilon=k_{\mathrm{B}}T$.

**Formula 1.1.2 (Rayleigh–Jeans Formula)**

$$
M_\nu(T)=\frac{2\pi\nu^2}{c^2}k_{\mathrm{B}}T.
$$

It agrees very well with experiment at low frequencies, but $M_\nu$ grows without bound as $\nu^2$, so the total exitance $\int_0^\infty M_\nu\,\mathrm{d}\nu$ diverges. Classical theory predicts that a cavity at any temperature radiates unlimited energy into the high-frequency (ultraviolet) region, an absurd conclusion that Ehrenfest later called the *ultraviolet catastrophe*. The derivation of the Rayleigh–Jeans formula used only classical electromagnetism and classical statistical mechanics; the error lies not in the calculation but in classical physics itself.

### 1.1.5. Planck's Law and the Energy Quantum Hypothesis

On October 7, 1900, Rubens told Planck his latest measurements. That very evening Planck "interpolated" a formula between Wien's formula and Rayleigh's formula and reported it to the German Physical Society on October 19; Rubens soon found that it agreed with experiment remarkably well over the whole spectrum. Planck was not satisfied with this "lucky guess" and within a few weeks found its physical basis: he still regarded the vibrating atoms of the cavity wall as charged harmonic oscillators exchanging energy with the radiation, but made an assumption completely incompatible with classical physics.

**Definition 1.1.4 (Energy Quantum)** Planck (December 1900) assumed that the energy of a harmonic oscillator of frequency $\nu$ can only take a series of discrete values

$$
E_n=n\varepsilon,\qquad\varepsilon=h\nu,\qquad n=0,1,2,\dots,
$$
that is, an oscillator can exchange energy with radiation only in units of $\varepsilon=h\nu$. Here $\varepsilon$ is called the **energy quantum** and $h$ the **Planck constant**.

**Formula 1.1.3 (Planck's Law)**

$$
M_\nu(T)=\frac{2\pi h\nu^3}{c^2}\,\frac{1}{\mathrm{e}^{h\nu/(k_{\mathrm{B}}T)}-1}.\tag{1.5}
$$

**Proof** By Eq. (1.4) it suffices to find the average energy of an oscillator. By the **Boltzmann distribution** ([Theorem 1.7.1](/5.2.1#thm-1.7.1)), the probability of the state with energy $E_n=n\varepsilon$ is proportional to $\mathrm{e}^{-n\varepsilon/(k_{\mathrm{B}}T)}$. Write $x=\varepsilon/(k_{\mathrm{B}}T)$ and $Z=\sum_{n=0}^\infty\mathrm{e}^{-nx}=\frac{1}{1-\mathrm{e}^{-x}}$. Then

$$
\bar\varepsilon=\frac{\sum_{n=0}^\infty n\varepsilon\,\mathrm{e}^{-nx}}{\sum_{n=0}^\infty\mathrm{e}^{-nx}}=-\varepsilon\frac{\mathrm{d}\ln Z}{\mathrm{d}x}=\frac{\varepsilon\,\mathrm{e}^{-x}}{1-\mathrm{e}^{-x}}=\frac{h\nu}{\mathrm{e}^{h\nu/(k_{\mathrm{B}}T)}-1}.
$$
Substituting into Eq. (1.4) gives Eq. (1.5). $\square$

The classical result $\bar\varepsilon=k_{\mathrm{B}}T$ rests on the assumption that the energy can take continuous values ([Remark 1.7.1](/5.2.1#rem-1.7.1)). Once the energy is discrete, a high-frequency mode with $h\nu\gg k_{\mathrm{B}}T$ can hardly be excited even by a single energy quantum (the probability is about $\mathrm{e}^{-h\nu/(k_{\mathrm{B}}T)}$); such modes are "frozen out", and the ultraviolet catastrophe disappears. All the earlier laws of thermal radiation can be derived from Planck's law:

| Operation | Result |
|---|---|
| Low frequency $h\nu\ll k_{\mathrm{B}}T$: $\mathrm{e}^{x}-1\approx x$ | Rayleigh–Jeans formula |
| High frequency $h\nu\gg k_{\mathrm{B}}T$: $\mathrm{e}^{x}-1\approx\mathrm{e}^{x}$ | Wien's formula, $\alpha=\frac{2\pi h}{c^2}$, $\beta=\frac{h}{k_{\mathrm{B}}}$ |
| Integrate over $\nu$, $\int_0^\infty\frac{x^3}{\mathrm{e}^x-1}\mathrm{d}x=\frac{\pi^4}{15}$ | Stefan–Boltzmann law, $\sigma=\frac{2\pi^5k_{\mathrm{B}}^4}{15c^2h^3}$ |
| Maximize, $x=3(1-\mathrm{e}^{-x})$, $x\approx2.821$ | Wien's displacement law, $C_\nu=2.821\,k_{\mathrm{B}}/h$ |
| Maximize $M_\lambda$, $x=5(1-\mathrm{e}^{-x})$, $x\approx4.965$ | $b=\frac{hc}{4.965\,k_{\mathrm{B}}}$ |

From the measured $\sigma$ and $C_\nu$ one can determine both $h$ and $k_{\mathrm{B}}$; in this way Planck obtained the most accurate values of the **Boltzmann constant** and Avogadro's constant of his time. In 1921, Ye Qisun, together with Duane and Palmer, measured $h=(6.556\pm0.009)\times10^{-34}\,\mathrm{J\,s}$ from the short-wavelength limit of the continuous **X-ray** spectrum, a result that remained in international use for more than a decade. Since 2019 the International System of Units has defined the kilogram through the fixed numerical value of the Planck constant:

$$
h=6.626\,070\,15\times10^{-34}\,\mathrm{J\,s}\quad(\text{exact}),
$$
and in calculations we usually take $h\approx6.63\times10^{-34}\,\mathrm{J\,s}$.

The energy quantum hypothesis was heretical from the point of view of classical physics, and Planck himself found it hard to accept; for many years afterward he tried, without success, to understand it within the framework of classical theory. He received the 1918 Nobel Prize in Physics for the discovery of energy quanta.

**Remark 1.1.1** Quantum mechanics gives the oscillator energy levels $E_n=(n+\frac12)h\nu$ ([5.5.3](/5.5.3)), which differ from Planck's assumption by the zero-point energy $\frac12h\nu$. The zero-point energy is the same for all states, does not change energy differences and does not take part in the energy exchange with radiation, so Planck's law is unaffected.

## 1.2. The Photoelectric Effect

**Definition 1.2.1 (Photoelectric Effect)** The phenomenon in which electrons are emitted from a metal surface when light shines on it is called the **photoelectric effect**, and the emitted electrons are called photoelectrons.

In 1887, while experimenting with electromagnetic waves, Hertz found that ultraviolet light shining on the electrodes made sparks easier to produce. After J. J. Thomson discovered the electron in 1897, Lenard showed that the charged particles emitted by a metal under illumination are electrons.

### 1.2.1. Experimental Results

The apparatus is an evacuated phototube: monochromatic light passes through a quartz window and falls on the cathode K, a voltage $U$ is applied between the anode A and the cathode ($U>0$ when the anode is at the higher **electric potential**), and a galvanometer measures the photocurrent $i$. Varying the intensity, the frequency and the voltage gives the following results (see the figure below).

**Definition 1.2.2** The reverse voltage $U_{\mathrm{c}}$ at which the photocurrent just drops to zero is called the **stopping voltage** (cutoff voltage). The lowest frequency $\nu_0$ of incident light that can produce the photoelectric effect is called the **cutoff frequency** (threshold frequency) of the metal, and the corresponding wavelength $\lambda_0=c/\nu_0$ is called the threshold wavelength.

**Property 1.2.1 (Experimental Laws of the Photoelectric Effect)**

1. Saturation current: for fixed intensity and frequency, the photocurrent increases with $U$ and finally reaches a saturation value $i_{\mathrm{m}}$, at which all the photoelectrons emitted by the cathode reach the anode. At fixed frequency, $i_{\mathrm{m}}$ is proportional to the light intensity $I$; that is, the number of photoelectrons emitted per unit time is proportional to the intensity.
2. Stopping voltage: the photocurrent is still nonzero at $U=0$ and even at $U<0$, which shows that photoelectrons leave the surface with initial kinetic energy; it vanishes when the reverse voltage reaches $U_{\mathrm{c}}$, so the maximum initial kinetic energy of the photoelectrons is $\frac12m_{\mathrm{e}}v_{\mathrm{m}}^2=eU_{\mathrm{c}}$. $U_{\mathrm{c}}$ is independent of the intensity and linear in the frequency, $U_{\mathrm{c}}=K\nu-U_0$, where the slope $K$ is a universal constant independent of the metal and $U_0$ depends on the metal.
3. Cutoff frequency: the effect occurs only if $\nu\ge\nu_0=U_0/K$; for $\nu<\nu_0$ no photoelectrons are emitted, however intense the light is and however long it shines.
4. Promptness: as long as $\nu>\nu_0$, the time from illumination to emission of photoelectrons does not exceed $10^{-9}\,\mathrm{s}$, however weak the light.

![The photoelectric effect. Left: photocurrent versus voltage (schematic); at fixed frequency the saturation current is proportional to the intensity, the stopping voltage is independent of the intensity, and the higher the frequency the larger the stopping voltage. Right: the stopping voltage of two metals with different work functions varies linearly with frequency; both slopes equal h/e, and the intercept with the horizontal axis is the cutoff frequency](./plots/photoelectric-effect.py)

### 1.2.2. The Difficulty with the Wave Theory

According to the electromagnetic wave theory of light, the electrons in a metal undergo **forced oscillations** under the electric field of the light wave, gradually accumulate energy, and escape once they have accumulated enough. This picture contradicts experimental laws 2–4:

- The more intense the light, the larger the amplitude of the electric field and the more energy the electrons gain, so the maximum initial kinetic energy of the photoelectrons and the stopping voltage should increase with intensity, whereas experiment shows that both are independent of intensity.
- However low the frequency, if the light is intense enough or shines long enough the electrons should always be able to accumulate enough energy, so there should be no cutoff frequency.
- For very weak light the electrons would need a long time to accumulate the energy required for escape, so the photoelectric effect should not be prompt (Example 1.2.1).

Only law 1 (photocurrent proportional to intensity) can be understood qualitatively by the wave theory.

**Example 1.2.1 (Delay Time Estimated from the Wave Theory)** A point source of power $1\,\mathrm{W}$ radiates uniformly in all directions. At a distance of $1\,\mathrm{m}$ lies a metal with work function (see Definition 1.3.2) $2\,\mathrm{eV}$. According to the wave theory, an electron can absorb at most the energy falling on an area of about one atomic cross section (take $(0.1\,\mathrm{nm})^2$). How long does it take to escape?

**Solution** The intensity there is $I=\frac{1\,\mathrm{W}}{4\pi(1\,\mathrm{m})^2}\approx0.080\,\mathrm{W\,m^{-2}}$, and the power on one atomic cross section is $P=I\times10^{-20}\,\mathrm{m^2}\approx8\times10^{-22}\,\mathrm{W}$. Accumulating $2\,\mathrm{eV}=3.2\times10^{-19}\,\mathrm{J}$ takes $t=3.2\times10^{-19}/(8\times10^{-22})\,\mathrm{s}\approx400\,\mathrm{s}$, about 7 minutes; the weaker the source, the longer the time. In experiments, however, no measurable delay is observed.

## 1.3. Photons and the Duality of Light

### 1.3.1. Einstein's Light Quantum Hypothesis

While Planck was still looking for a classical origin of the energy quantum, Einstein, in his 1905 paper "On a Heuristic Point of View Concerning the Production and Transformation of Light", took the concept of the energy quantum a long step further: not only is the energy exchange between oscillators and radiation quantized, but the radiation itself consists of energy quanta. He wrote that the energy of a light ray emitted from a point source is not distributed continuously over an ever-increasing volume but consists of a finite number of energy quanta, each localized in a small region of space, moving without dividing, and able to be produced or absorbed only as a whole.

**Definition 1.3.1 (Photon)** Einstein's light quantum hypothesis: electromagnetic radiation consists of energy quanta that move at the speed of light $c$ and are localized in a small region of space, called **photons** (light quanta). The energy of a photon of frequency $\nu$ is

$$
\varepsilon=h\nu.\tag{1.6}
$$
A photon is indivisible: light is emitted, propagates and is absorbed in units of photons.

In the photon picture, a beam of monochromatic light is a stream of photons moving at speed $c$. If $N$ is the number of photons crossing a unit area perpendicular to the direction of propagation per unit time, the intensity is

$$
I=Nh\nu.
$$
For example, a He–Ne laser of power $1\,\mathrm{mW}$ ($\lambda=632.8\,\mathrm{nm}$, $h\nu=1.96\,\mathrm{eV}$) emits about $3.2\times10^{15}$ photons per second. Everyday light contains so many photons that it appears continuous.

### 1.3.2. The Photoelectric Equation

**Definition 1.3.2 (Work Function)** The minimum energy needed to remove an electron from the surface of a given metal is called the **work function** of the metal, denoted $W_0$.

The work functions of several metals are approximately: cesium $2.1\,\mathrm{eV}$, sodium $2.3\,\mathrm{eV}$, aluminum $4.2\,\mathrm{eV}$, zinc $4.3\,\mathrm{eV}$, platinum $5.6\,\mathrm{eV}$ (the values depend on the surface condition). According to the photon theory, an electron in the metal absorbs the whole energy $h\nu$ of one photon at a time; part of it is used to overcome the binding of the metal and the rest becomes the kinetic energy of the electron. An electron near the surface, where the binding is weakest, leaves with the largest kinetic energy:

**Theorem 1.3.1 (Photoelectric Equation)**

$$
\frac12m_{\mathrm{e}}v_{\mathrm{m}}^2=h\nu-W_0.\tag{1.7}
$$

It explains all the experimental laws of the photoelectric effect:

- A photon knocks out a photoelectron in a single event, with no need to accumulate energy, so the photoelectric effect is prompt.
- The greater the intensity $I=Nh\nu$, the more photons arrive per unit time and the more photoelectrons are ejected, so the saturation current $i_{\mathrm{m}}\propto I$.
- The maximum initial kinetic energy is determined by the energy of a single photon and is independent of the intensity: $eU_{\mathrm{c}}=h\nu-W_0$; comparing with the experimental law $U_{\mathrm{c}}=K\nu-U_0$ gives $K=h/e$ and $U_0=W_0/e$.
- The effect can occur only if $h\nu\ge W_0$, so the cutoff frequency is $\nu_0=W_0/h$.

Electrons from different depths and in different energy states lose different amounts of energy on escaping, so the photoelectron speeds have a distribution, and Eq. (1.7) gives the maximum.

The light quantum hypothesis was not accepted by the physics community at the time. When Planck and others recommended Einstein for membership of the Prussian Academy of Sciences in 1913, they wrote that he "may sometimes have gone too far in his speculations, as for example in his hypothesis of light quanta." Millikan, who wanted to refute the photon theory, spent about ten years measuring the $U_{\mathrm{c}}$–$\nu$ relation of several metals with great precision, yet his results, published in 1916, completely confirmed Eq. (1.7): the slope of the straight line, $K=h/e$, gave $h=6.56\times10^{-34}\,\mathrm{J\,s}$, in agreement with the value determined from thermal radiation. Einstein received the 1921 Nobel Prize in Physics "for his services to theoretical physics, and especially for his discovery of the law of the photoelectric effect."

**Example 1.3.1 (Photoelectric Effect in Aluminum)** Ultraviolet light of wavelength $\lambda=200\,\mathrm{nm}$ shines on an aluminum surface with work function $W_0=4.2\,\mathrm{eV}$. Find the maximum initial kinetic energy of the photoelectrons, the stopping voltage and the cutoff frequency of aluminum.

**Solution** Using $hc=1239.8\,\mathrm{eV\,nm}$, the photon energy is $h\nu=\frac{hc}{\lambda}=\frac{1239.8}{200}\,\mathrm{eV}=6.20\,\mathrm{eV}$. The maximum initial kinetic energy is $E_{\mathrm{k,max}}=h\nu-W_0=2.0\,\mathrm{eV}$, and the stopping voltage is $U_{\mathrm{c}}=E_{\mathrm{k,max}}/e=2.0\,\mathrm{V}$. The cutoff frequency is

$$
\nu_0=\frac{W_0}{h}=\frac{4.2\times1.602\times10^{-19}}{6.626\times10^{-34}}\,\mathrm{Hz}=1.0\times10^{15}\,\mathrm{Hz},
$$
and the threshold wavelength is $\lambda_0=c/\nu_0\approx295\,\mathrm{nm}$, so visible light cannot produce the photoelectric effect in aluminum.

The photoelectric effect has many applications: phototubes and photomultiplier tubes convert weak light signals into electrical signals and can detect single photons; photoelectron spectroscopy (including angle-resolved photoemission spectroscopy, [5.5.6](/5.5.6)) measures the energy and momentum of electrons in solids from the energy and direction of the photoelectrons. Photoconductivity (a change in the electrical **conductance**) in semiconductors and the photovoltaic effect (solar cells) are internal photoelectric effects, in which electrons absorb photons and make transitions inside the solid.

### 1.3.3. Energy and Momentum of the Photon

A photon moves at the speed of light, so by special relativity its mass must be zero, and its energy and momentum satisfy $\varepsilon=pc$ ([5.1.8](/5.1.8#sec-8.9.4)). Hence for a photon of frequency $\nu$ and wavelength $\lambda$,

$$
\varepsilon=h\nu,\qquad p=\frac{\varepsilon}{c}=\frac{h\nu}{c}=\frac{h}{\lambda},\qquad m=0.\tag{1.8}
$$
In vector form $\boldsymbol{p}=\hbar\boldsymbol{k}$, where $\boldsymbol{k}$ is the wave vector and $\hbar=h/(2\pi)$. Older textbooks call $h\nu/c^2$ the "moving mass" of the photon; it is merely another name for $\varepsilon/c^2$ and is not the mass of the photon ([Remark 8.7.1](/5.1.8#rem-8.7.1)). The electromagnetic theory of light also predicts the momentum of light, namely the radiation pressure ([5.3.10](/5.3.10#sec-10.3.4)): light with **energy flux density** $S$ incident normally on a perfectly absorbing surface exerts a pressure $S/c$, which is exactly the sum of the momenta $Nh\nu/c$ of the $N$ photons arriving per second.

### 1.3.4. The Duality of Light

On the left of Eq. (1.8), $\varepsilon$ and $p$ describe the particle nature; on the right, $\nu$ and $\lambda$ describe the wave nature; the Planck constant connects the two. Light shows its wave nature in **interference**, diffraction and polarization, and its particle nature in thermal radiation, the photoelectric effect and Compton scattering; this is called the *wave–particle duality* of light. In general the wave nature is prominent when the wavelength is long and the obstacles are small, and the particle nature is prominent when the wavelength is short and the obstacles are large.

As an electromagnetic wave, light is spread out and continuous in space; as a particle, a photon is concentrated and discrete. The two are unified through probability: the probability of finding a photon at a point is proportional to the light intensity there, that is, to the square of the light amplitude. A point source radiates with equal probability in all directions, so the intensity at distance $r$ is $I\propto1/r^2$; in single-slit diffraction the probability of finding a photon is large at the bright fringes and zero at the dark fringes. In the double-slit experiment, the splitting of the **wavefront** by the two slits does not mean that the photon is divided: the probability that a photon passes through slit 1 is proportional to $I_1$, and through slit 2 to $I_2$, while the distribution on the screen is determined by the square of the sum of the light amplitudes coming from the two slits. The next chapter, [5.5.2](/5.5.2#sec-2.2), extends this probabilistic interpretation to all microscopic particles.

## 1.4. Compton Scattering

### 1.4.1. Experimental Results

In 1923 Compton irradiated light elements such as graphite with X-rays and studied the wavelength of the scattered radiation. The molybdenum $\mathrm{K}_\alpha$ line ($\lambda_0=0.0709\,\mathrm{nm}$) from an X-ray tube was collimated onto graphite, and a crystal X-ray spectrometer measured the intensity of the scattered radiation, as a function of wavelength, at scattering angle $\theta$ to the incident direction.

**Definition 1.4.1 (Compton Scattering)** The phenomenon in which, after X-rays are scattered by matter, the scattered radiation contains, besides the original wavelength $\lambda_0$, a component of wavelength $\lambda>\lambda_0$ is called **Compton scattering** (the Compton effect).

The experimental results are:

1. Besides the original wavelength $\lambda_0$, a new spectral line with wavelength $\lambda>\lambda_0$ appears in the scattered radiation.
2. The wavelength shift $\Delta\lambda=\lambda-\lambda_0$ increases with the scattering angle $\theta$ and is independent of the scattering material and of the incident wavelength:

   $$
   \Delta\lambda=\lambda_{\mathrm{C}}(1-\cos\theta)=2\lambda_{\mathrm{C}}\sin^2\frac{\theta}{2},
   $$
   where the experimental value of the constant $\lambda_{\mathrm{C}}$ is $2.41\times10^{-3}\,\mathrm{nm}$.
3. As the scattering angle increases, the intensity of the line at the original wavelength decreases and that of the line at the new wavelength increases.

In classical electromagnetic theory, an electron is driven by the electric field of the incident wave to oscillate at the frequency of the incident wave and emits scattered waves of the same frequency (Thomson scattering), so scattered radiation with $\lambda\ne\lambda_0$ cannot occur.

### 1.4.2. Explanation by the Photon Theory

Compton explained the phenomenon with the photon theory: an X-ray photon undergoes an **elastic collision** with a "free" electron at "rest". The energy of an X-ray photon with wavelength of the order of $0.1\,\mathrm{nm}$ is about $10^4\,\mathrm{eV}$, whereas the binding energy of the outer electrons in light elements is only a few $\mathrm{eV}$ and the thermal energy at room temperature is $k_{\mathrm{B}}T\sim10^{-2}\,\mathrm{eV}$, so these electrons can be regarded as free electrons at rest. In the collision the electron takes part of the photon's energy and recoils, and the photon loses energy, its frequency decreases and its wavelength increases. Energy and momentum are conserved in the collision; the recoil electron can move very fast, so the problem must be treated relativistically.

**Formula 1.4.1 (Compton Formula)** After a photon of wavelength $\lambda_0$ collides with a free electron at rest and is scattered at an angle $\theta$ to its original direction, the wavelength of the scattered photon is

$$
\lambda=\lambda_0+\frac{h}{m_{\mathrm{e}}c}(1-\cos\theta).\tag{1.9}
$$

**Proof** Let the momenta of the incident and scattered photons be $\boldsymbol{p}_0$ and $\boldsymbol{p}$, with magnitudes $p_0=h/\lambda_0$ and $p=h/\lambda$ and energies $p_0c$ and $pc$; let the momentum and energy of the recoil electron be $\boldsymbol{p}_{\mathrm{e}}$ and $E_{\mathrm{e}}$. By **conservation of momentum** and **conservation of energy**,

$$
\boldsymbol{p}_{\mathrm{e}}=\boldsymbol{p}_0-\boldsymbol{p},\qquad E_{\mathrm{e}}=(p_0-p)c+m_{\mathrm{e}}c^2.
$$
The energy and momentum of the electron satisfy $E_{\mathrm{e}}^2-p_{\mathrm{e}}^2c^2=m_{\mathrm{e}}^2c^4$ (Eq. [(8.13)](/5.1.8#eq-8.13)), and $p_{\mathrm{e}}^2=p_0^2+p^2-2p_0p\cos\theta$. Substituting and cancelling $m_{\mathrm{e}}^2c^4$ gives

$$
c^2(p_0-p)^2+2(p_0-p)m_{\mathrm{e}}c^3-c^2\big(p_0^2+p^2-2p_0p\cos\theta\big)=0,
$$
that is, $(p_0-p)m_{\mathrm{e}}c=p_0p(1-\cos\theta)$. Dividing both sides by $p_0p\,m_{\mathrm{e}}c$ yields $\frac1p-\frac1{p_0}=\frac{1-\cos\theta}{m_{\mathrm{e}}c}$, and multiplying by $h$ gives Eq. (1.9). $\square$

**Definition 1.4.2 (Compton Wavelength)** The quantity $\lambda_{\mathrm{C}}=\dfrac{h}{m_{\mathrm{e}}c}$ is called the **Compton wavelength** of the electron,

$$
\lambda_{\mathrm{C}}=\frac{6.626\times10^{-34}}{9.109\times10^{-31}\times2.998\times10^8}\,\mathrm{m}=2.426\times10^{-12}\,\mathrm{m}=2.426\,\mathrm{pm}.
$$

The theoretical value agrees well with the experimental one. $\lambda_{\mathrm{C}}$ is the wavelength at which the photon energy equals the rest energy of the electron, $m_{\mathrm{e}}c^2=0.511\,\mathrm{MeV}$, and the maximum wavelength shift is $2\lambda_{\mathrm{C}}$ (backscattering). The relative shift $\Delta\lambda/\lambda_0$ is significant only when the incident wavelength is comparable to $\lambda_{\mathrm{C}}$, which is why X-rays or $\gamma$-rays are needed to observe the Compton effect.

![Compton scattering. Left: wavelength shift Δλ = λ_C(1 - cos θ) versus scattering angle; at 90° it equals the Compton wavelength. Right: spectrum of molybdenum Kα radiation scattered by graphite (schematic); as the scattering angle increases, the shifted line moves farther and grows stronger while the line at the original wavelength weakens](./plots/compton-shift.py)

**Example 1.4.1 (Kinetic Energy of the Recoil Electron)** The molybdenum $\mathrm{K}_\alpha$ line ($\lambda_0=0.0709\,\mathrm{nm}$) is scattered by graphite. Find the wavelength of the radiation scattered at $\theta=90^\circ$ and the kinetic energy of the corresponding recoil electron.

**Solution** $\Delta\lambda=\lambda_{\mathrm{C}}(1-\cos90^\circ)=2.43\,\mathrm{pm}$ and $\lambda=\lambda_0+\Delta\lambda=0.0733\,\mathrm{nm}$. By conservation of energy, the kinetic energy of the recoil electron equals the energy lost by the photon:

$$
E_{\mathrm{k}}=\frac{hc}{\lambda_0}-\frac{hc}{\lambda}=\frac{hc}{\lambda_0}\cdot\frac{\Delta\lambda}{\lambda}=17.49\,\mathrm{keV}\times\frac{2.43}{73.3}\approx0.58\,\mathrm{keV}.
$$
The photon gives only about $3\%$ of its energy to the electron. The higher the energy of the incident photon, the larger the fraction transferred: for a $\gamma$ photon of energy $0.6\,\mathrm{MeV}$ whose wavelength increases by $20\%$ after scattering, the recoil electron receives $0.6\,\mathrm{MeV}\times(1-\frac{1}{1.2})=0.1\,\mathrm{MeV}$.

### 1.4.3. Some Questions

1. Why does the scattered radiation also contain a component at the original wavelength $\lambda_0$? The photon also collides with inner-shell electrons that are tightly bound to the nucleus. The binding energy of inner-shell electrons is $10^3$–$10^4\,\mathrm{eV}$, so they cannot be regarded as free, and the photon in effect collides with the whole atom. Replacing $m_{\mathrm{e}}$ in Eq. (1.9) by the mass of the atom makes $\Delta\lambda$ smaller by a factor of several thousand to several hundred thousand, which is unmeasurable.
2. Why can a free electron not absorb a photon as in the photoelectric effect, but only scatter it? Suppose a free electron at rest absorbs a photon of energy $h\nu$. The energy and momentum of the system are $E=h\nu+m_{\mathrm{e}}c^2$ and $p=h\nu/c$, so $E^2-p^2c^2=m_{\mathrm{e}}^2c^4+2h\nu m_{\mathrm{e}}c^2>m_{\mathrm{e}}^2c^4$. But $E^2-p^2c^2$ is a Lorentz invariant, and the single electron left after absorption must satisfy $E^2-p^2c^2=m_{\mathrm{e}}^2c^4$, a contradiction. Hence a free electron cannot absorb a photon, because energy and momentum cannot both be conserved. In quantum electrodynamics, Compton scattering is a second-order process in which the photon is first absorbed and then emitted (or first emitted and then absorbed); the intermediate state is a virtual state that does not satisfy $E^2=p^2c^2+m^2c^4$, which does not contradict the conclusion above.
3. Why is momentum conservation not considered in the analysis of the photoelectric effect? The electrons in the photoelectric effect are bound to the metal (to atoms or the lattice), and the incident visible or ultraviolet photons have low energy, so the electrons cannot be regarded as free. The atoms take part in the momentum exchange, so the momentum of the photon–electron system is not conserved; but the atoms are massive and the kinetic energy they receive is negligible, so the energy of the photon–electron system can still be regarded as conserved. This also shows that the photoelectric effect can occur only on bound electrons.
4. Why can the Compton effect not be observed with visible light? On the one hand, the energy of a visible photon is only a few $\mathrm{eV}$, comparable to the binding energy of the electrons, so the electrons cannot be regarded as free; on the other hand, even for free electrons $\Delta\lambda\le2\lambda_{\mathrm{C}}\approx4.9\,\mathrm{pm}$, only $10^{-5}$ of $500\,\mathrm{nm}$, which is hard to resolve.
5. Why is the wavelength shift independent of the scattering material? The outer electrons in all materials can be regarded as free electrons, and only the electron mass appears in Eq. (1.9).

### 1.4.4. The Work of Wu Youxun and the Significance of Compton Scattering

From 1923 Wu Youxun took part in the study of the Compton effect in Compton's laboratory. In 1925–1926 he used the silver $\mathrm{K}_\alpha$ line ($\lambda_0=0.0562\,\mathrm{nm}$) as the incident radiation and 15 elements, light and heavy, as scatterers, and measured the spectrum of the scattered radiation at the same scattering angle $\theta=120^\circ$. The results showed that $\Delta\lambda$ is independent of the scatterer and depends only on the scattering angle; in light elements the shifted line is more intense than the line at the original wavelength, whereas in heavy elements the opposite holds. This confirmed the universality of the Compton effect and the mechanisms producing the two kinds of scattered lines: the shifted line comes from outer (approximately free) electrons, and the line at the original wavelength from inner electrons (the whole atom). In his 1935 book *X-Rays in Theory and Experiment*, Compton cited Wu Youxun's work in 19 places.

The significance of Compton scattering:

- It supported the concept of the photon and further confirmed $\varepsilon=h\nu$.
- It was the first experimental confirmation that the photon has momentum $p=h/\lambda$.
- It confirmed that energy conservation and momentum conservation still hold in a single microscopic collision. In 1925 Bothe and Geiger used the coincidence method to show that the recoil electron and the scattered photon appear simultaneously, which ruled out the idea that energy is conserved only in a statistical average sense (the Bohr–Kramers–Slater theory).

Compton received the 1927 Nobel Prize in Physics for this work. Today Compton scattering is one of the dominant interactions in $\gamma$-ray spectroscopy and medical radiotherapy.

## Summary

| Topic | Key points |
|---|---|
| Thermal radiation | Spectral exitance $M_\nu(T)$, total exitance $M(T)=\int M_\nu\,\mathrm{d}\nu$; black body $\alpha_\nu=1$; Kirchhoff's law $M_\nu/\alpha_\nu=M_{\mathrm{B}\nu}(T)$ |
| Experimental laws | $M=\sigma T^4$, $\sigma=5.67\times10^{-8}\,\mathrm{W\,m^{-2}\,K^{-4}}$; $\nu_{\mathrm{m}}=C_\nu T$, $\lambda_{\mathrm{m}}T=b=2.898\times10^{-3}\,\mathrm{m\,K}$ |
| Classical difficulty | Mode density $\frac{8\pi\nu^2}{c^3}$, $M_\nu=\frac{2\pi\nu^2}{c^2}\bar\varepsilon$; equipartition gives the Rayleigh–Jeans formula and the ultraviolet catastrophe |
| Planck | Energy quantum $\varepsilon=h\nu$, $\bar\varepsilon=\frac{h\nu}{\mathrm{e}^{h\nu/(k_{\mathrm{B}}T)}-1}$, $M_\nu=\frac{2\pi h\nu^3}{c^2}\frac{1}{\mathrm{e}^{h\nu/(k_{\mathrm{B}}T)}-1}$ |
| Photoelectric effect | Saturation current $\propto I$; $U_{\mathrm{c}}$ independent of intensity and increasing linearly with $\nu$; cutoff frequency; promptness |
| Photon | $\varepsilon=h\nu$, $p=h/\lambda$, $m=0$; $I=Nh\nu$; photoelectric equation $\frac12m_{\mathrm{e}}v_{\mathrm{m}}^2=h\nu-W_0$, $\nu_0=W_0/h$ |
| Compton scattering | $\Delta\lambda=\lambda_{\mathrm{C}}(1-\cos\theta)$, $\lambda_{\mathrm{C}}=h/(m_{\mathrm{e}}c)=2.426\,\mathrm{pm}$; elastic collision of a photon with a free electron, energy and momentum conserved |
| Duality | The probability of finding a photon is proportional to the intensity; the wave nature dominates at long wavelengths and the particle nature at short wavelengths |

## Questions

1. When an iron block is heated, why does its color change from dull red to orange, yellow-white and blue-white?

   **Answer** by Wien's displacement law, the peak of the radiation spectrum moves toward shorter wavelengths as the temperature rises, while by the Stefan–Boltzmann law the total radiation increases sharply. At about $800\,\mathrm{K}$ only the long-wavelength tail enters the visible region, and we see dull red; at higher temperatures the proportions of the visible wavelengths become more even, the color turns white, and finally bluish.

2. Why do some people in the African deserts wear black robes?

   **Answer** a black robe absorbs more sunlight and its outer surface becomes very hot, but it is held at some distance from the skin and the heat is carried away mainly by air convecting between the robe and the body; black is also a good emitter in the infrared (Kirchhoff's law) and blocks more ultraviolet light.

3. What is the role of the accelerating voltage in the photoelectric experiment? Why is there still a photocurrent at zero or even reverse voltage?

   **Answer** the accelerating voltage collects the emitted photoelectrons at the anode; photoelectrons leave with initial kinetic energy, so as long as the reverse voltage is less than the stopping voltage, some of them still reach the anode.

4. When light of a given wavelength shines on a metal, why do the emitted photoelectrons have different speeds?

   **Answer** the electrons in the metal are in different energy states and at different depths, and the work done to overcome the binding differs when they escape; $h\nu-W_0$ is only the maximum initial kinetic energy.

5. Are the bright colors of bird feathers thermal radiation?

   **Answer** no. The colors of feathers come from selective absorption of sunlight (pigments) or from interference caused by microstructures (structural color, [5.4.1](/5.4.1)); at room temperature the thermal radiation of the feathers themselves lies in the infrared.

6. In Compton scattering, the shorter the wavelength of the incident photon, the larger the fraction of the incident energy that the recoil electron receives. Why?

   **Answer** $\frac{E_{\mathrm{k}}}{h\nu_0}=\frac{\Delta\lambda}{\lambda_0+\Delta\lambda}$, and $\Delta\lambda$ is independent of $\lambda_0$, so the smaller $\lambda_0$ is, the larger the fraction.
