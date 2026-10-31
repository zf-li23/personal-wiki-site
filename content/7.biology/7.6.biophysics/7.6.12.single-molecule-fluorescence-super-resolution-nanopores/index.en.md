---
title: Single-Molecule Fluorescence, Super-Resolution and Nanopores
description: "The physics of observing single biological molecules by light and by ionic current. What ensembles hide: discrete states, dwell-time distributions, static and dynamic heterogeneity, single-molecule enzymology. The photon budget: excitation rate, saturation, photobleaching, blinking and signal-to-noise. Image formation as Fourier optics: point spread function, optical transfer function, Rayleigh and Abbe limits, Nyquist sampling; total internal reflection and the evanescent field; confocal detection. Localization precision and the Cramér–Rao bound, FIONA and the hand-over-hand walk of myosin V, single-particle tracking and MSD estimators, counting subunits by photobleaching steps. Super-resolution: STED and the saturated depletion law, single-molecule localization microscopy and the labeling-density limit, MINFLUX, structured illumination. Single-molecule FRET: corrections, shot-noise width of FRET histograms, burst analysis, hidden Markov models of trajectories. Fluorescence correlation spectroscopy: derivation of the diffusion autocorrelation, kinetics, triplets, cross-correlation. Nanopores: access and channel resistance, blockades, voltage-driven capture, translocation as first passage, nanopore sequencing."
---

Ensemble measurements report averages. A solution of $10^{14}$ identical enzymes gives one Michaelis–Menten curve, one CD spectrum and one melting temperature, and the individual molecules, each of which binds, reacts, changes shape and occasionally misbehaves at random times, are invisible behind the average. Since the 1970s, first with the current through a single ion channel and then with fluorescence, force and ionic current through nanopores, it has become possible to follow one molecule at a time. Single-molecule measurements see discrete states and the stochastic switching between them, the distribution of the times spent in each state, the differences between molecules, and transient intermediates that never accumulate enough to appear in an ensemble.

This chapter treats the optical and electrical single-molecule methods; mechanical ones (optical and magnetic tweezers, atomic force microscopy) follow in [7.6.17](/7.6.17), and the patch clamp, the first single-molecule method, in [7.6.30](/7.6.30). It starts from what single molecules reveal and from the photon budget that limits every fluorescence experiment (12.1). The optics of the microscope, Fourier optics, the diffraction limit and total internal reflection, set the stage (12.2). A single emitter can be located far more precisely than the diffraction limit, which gives nanometer tracking of motors, the analysis of trajectories and the counting of subunits (12.3), and super-resolution microscopy, whose physical limits are derived (12.4). Single-molecule FRET turns the spectroscopic ruler of [7.6.11](/7.6.11#sec-11.5.7) into a probe of conformational dynamics (12.5). Fluorescence correlation spectroscopy extracts diffusion and kinetics from the fluctuations of a few molecules (12.6). Nanopores read molecules electrically as they pass through a hole a few nanometers wide (12.7). A comparison closes the chapter (12.8).

The photophysics of fluorophores ([7.6.11](/7.6.11)), the theory of random walks, first passage and master equations ([7.6.5](/7.6.5)) and the statistics of estimation (the **Fisher information** and the **Cramér–Rao inequality** of mathematical statistics) are used throughout. The practical microscopy of cells, with fluorescent proteins, FRAP and the overview of super-resolution methods, is in [7.3.2](/7.3.2), and the fluorescence microscope and super-resolution in analytical chemistry in [6.4.10](/6.4.10#sec-10.4); here the emphasis is on the physical limits and on how quantitative information is extracted from single-molecule data. Nanopore sequencing as a genomic technology is in [7.2.6](/7.2.6).

## 12.1. Why Single Molecules

### 12.1.1. What Ensembles Hide

A single molecule observed by a signal that depends on its state (fluorescence, FRET efficiency, current, extension) shows a trajectory that jumps between discrete levels at random times. Four kinds of information follow that ensembles do not give directly.

- *Discreteness and stochasticity*: transitions are instantaneous jumps, not gradual changes; the ensemble relaxation $[A](t) = [A]_0\mathrm{e}^{-kt}$ is the average of exponentially distributed waiting times.
- *Dwell-time distributions*: the time a molecule spends in a state before leaving it has a distribution whose shape reveals hidden steps (12.1.2).
- *Heterogeneity*: different molecules may have different rates (static heterogeneity), and one molecule may change its rate over time (dynamic heterogeneity or dynamic disorder).
- *Unsynchronized dynamics at equilibrium*: a single molecule at equilibrium still fluctuates between its states, so rates and equilibrium constants can be measured without perturbing the system, and detailed balance can be tested directly; irreversible, nonequilibrium processes (a motor stepping, a ribosome translating) can be followed without the need to synchronize a population.

The connection between single-molecule and ensemble descriptions is the **master equation** ([7.6.5](/7.6.5#sec-5.5.1)): the ensemble populations obey the same linear rate equations whose stochastic realizations are the single-molecule trajectories. For an ergodic system, averaging one long trajectory over time gives the same result as averaging many molecules at one time; heterogeneity that persists longer than the observation breaks this equivalence and is precisely what single-molecule measurements detect.

### 12.1.2. Dwell Times and Hidden Steps

**Proposition 12.1.1 (Dwell-Time Distributions)** (a) If a molecule leaves a state by a single first-order step of rate $k$, its dwell time $t$ in that state has the density $f(t) = k\mathrm{e}^{-kt}$, with mean $1/k$ and standard deviation $1/k$. The maximum-likelihood estimate of $k$ from $n$ observed dwell times is $\hat k = n/\sum_it_i$. (b) If leaving the observed state requires two sequential irreversible steps with rates $k_1 \ne k_2$ (both within the same observable state), the dwell-time density is

$$
f(t) = \frac{k_1k_2}{k_2 - k_1}\left(\mathrm{e}^{-k_1t} - \mathrm{e}^{-k_2t}\right),
$$
which vanishes at $t = 0$, rises to a maximum and then decays; its mean is $1/k_1 + 1/k_2$ and its squared coefficient of variation is $(k_1^2 + k_2^2)/(k_1 + k_2)^2 < 1$.

**Proof** (a) The survival probability of the state obeys $\mathrm{d}S/\mathrm{d}t = -kS$, so $S = \mathrm{e}^{-kt}$ and $f = -\mathrm{d}S/\mathrm{d}t$. The log-likelihood $n\ln k - k\sum t_i$ is maximal at $\hat k = n/\sum t_i$. (b) The total time is the sum of two independent exponential times, and its density is the convolution $\int_0^tk_1\mathrm{e}^{-k_1s}k_2\mathrm{e}^{-k_2(t - s)}\,\mathrm{d}s$, which gives the formula. Means add, and variances $1/k_1^2 + 1/k_2^2$ add. $\square$

A dwell-time distribution that is not a single exponential therefore reveals either more than one step within the observed state (a rising phase, as in (b)) or more than one population or pathway (a sum of exponentials). The ratio of the variance to the squared mean, the *randomness parameter*, bounds the number of hidden steps from below: for $N$ equal sequential steps it is $1/N$. It is used again for motors in [7.6.27](/7.6.27).

**Example 12.1.1 (Single-Molecule Enzymology)** The FAD cofactor of cholesterol oxidase is fluorescent when oxidized and dark when reduced. Lu, Xun and Xie (1998) immobilized single enzyme molecules in a gel and recorded on–off fluorescence trajectories as each molecule cycled between the oxidized form, which binds and oxidizes cholesterol, and the reduced form, which is reoxidized by $\ce{O2}$. The distribution of on times rose and then fell, as in Proposition 12.1.1(b), revealing the binding step before the chemical step; the turnover rates of different molecules differed by a factor of several, and the rate of one molecule fluctuated on a time scale of about a second, a memory effect attributed to slow conformational fluctuations of the protein (dynamic disorder). English and colleagues (2006) showed with β-galactosidase that the mean turnover time of a single enzyme still obeys a single-molecule Michaelis–Menten law, $1/\langle\tau\rangle = k_{\mathrm{cat}}[\ce{S}]/([\ce{S}] + K_{\mathrm{M}})$, even when the distribution of turnover times is far from exponential: the **Michaelis–Menten equation** of [7.1.9](/7.1.9) is a statement about mean rates that survives heterogeneity.

![What a single enzyme shows (simulated cycle bright E → bright ES → dark E* → E with k1 = 20 s⁻¹, k2 = 30 s⁻¹, k3 = 10 s⁻¹). A: the fluorescence of one molecule switches between on and off at random times (photon counts per millisecond with shot noise). B: the distribution of on times rises from zero and then decays, matching the two-step density of Proposition 12.1.1(b) and not a single exponential with the same mean: the binding step hidden within the bright state becomes visible. C: the average of 2000 unsynchronized molecules started in the bright state relaxes smoothly to the steady-state bright fraction (dotted), and neither step can be read from it](./plots/single-molecule-kinetics.py)

### 12.1.3. The Photon Budget

Everything in single-molecule fluorescence is limited by the number of photons a molecule emits and the fraction of them that is detected. A fluorophore of molar absorption coefficient $\varepsilon$ has the cross-section $\sigma = 3.82\times10^{-21}\varepsilon\,\mathrm{cm^2}$ (Theorem 11.1.1 of [7.6.11](/7.6.11#thm-11.1.1)); in light of intensity $I$ and photon energy $h\nu$ it is excited at the rate $k_{\mathrm{ex}} = \sigma I/(h\nu)$, and as long as $k_{\mathrm{ex}}\tau \ll 1$ it emits $\Phi k_{\mathrm{ex}}$ photons per second.

**Formula 12.1.1 (Saturation)** For a two-level fluorophore with lifetime $\tau$, the emission rate saturates as

$$
k_{\mathrm{em}} = \Phi\,\frac{k_{\mathrm{ex}}}{1 + k_{\mathrm{ex}}\tau} = \frac{\Phi}{\tau}\,\frac{I/I_{\mathrm{s}}}{1 + I/I_{\mathrm{s}}}, \qquad I_{\mathrm{s}} = \frac{h\nu}{\sigma\tau}.
$$
With intersystem crossing, molecules accumulate in the long-lived triplet state at high intensity, which lowers the maximal emission rate further.

**Example 12.1.2 (A Cyanine Dye)** For Cy3 ($\varepsilon = 1.5\times10^5\,\mathrm{L\,mol^{-1}\,cm^{-1}}$, $\sigma = 5.7\times10^{-16}\,\mathrm{cm^2}$) at $532\,\mathrm{nm}$ ($h\nu = 3.73\times10^{-19}\,\mathrm{J}$) and $1\,\mathrm{kW\,cm^{-2}}$, typical of TIRF illumination, $k_{\mathrm{ex}} = 5.7\times10^{-16}\times10^3/3.73\times10^{-19} = 1.5\times10^6\,\mathrm{s^{-1}}$, far below saturation ($I_{\mathrm{s}} \approx 3\times10^5\,\mathrm{W\,cm^{-2}}$ for $\tau = 2\,\mathrm{ns}$). With $\Phi = 0.2$ the molecule emits $3\times10^5$ photons per second, and a detection efficiency of about $10\,\%$ (objective collection $\approx 30\,\%$, filters, camera quantum efficiency) gives $3000$ detected photons in a $100\,\mathrm{ms}$ frame.

The total number of photons is limited by photobleaching. If each excitation leads to irreversible photochemistry with probability $\Phi_{\mathrm{b}}$, the molecule emits on average $\Phi/\Phi_{\mathrm{b}}$ photons before it bleaches: about $10^5$–$10^6$ for good organic dyes under oxygen depletion, $10^4$–$10^5$ for fluorescent proteins. Bleaching occurs mostly through the triplet state, whose reaction with oxygen produces singlet oxygen; removing oxygen enzymatically (glucose oxidase with catalase, or protocatechuate dioxygenase) and adding triplet-state quenchers (Trolox, cyclooctatetraene) extends the photon budget by one to two orders of magnitude and suppresses blinking, the dark intervals spent in the triplet or in radical states. The experimenter then distributes the fixed budget between time resolution and precision: more photons per frame give better localization or FRET precision (12.3, 12.5), more frames give longer trajectories.

Detection of one molecule also requires that its signal exceed the background from everything else in the observed volume: Raman scattering of water, autofluorescence, out-of-focus fluorophores. The shot-noise-limited signal-to-noise ratio in a measurement interval is

$$
\mathrm{SNR} = \frac{N_{\mathrm{s}}}{\sqrt{N_{\mathrm{s}} + N_{\mathrm{b}} + N_{\mathrm{d}}}},
$$
with $N_{\mathrm{s}}$, $N_{\mathrm{b}}$ and $N_{\mathrm{d}}$ the numbers of signal, background and detector-noise counts. Since the background is proportional to the illuminated volume, single-molecule methods shrink it: to about $1\,\mathrm{fL}$ in a confocal spot and to a layer about $100\,\mathrm{nm}$ thick in total internal reflection (12.2.3); zero-mode waveguides, holes of about $100\,\mathrm{nm}$ in a metal film, reduce it to zeptoliters and allow single fluorophores to be observed against micromolar concentrations of labeled substrate, as in real-time single-molecule sequencing. The final proof that a signal comes from one emitter is photophysical: it bleaches in one step (12.3.4), and its photon stream shows antibunching (an emitter that has just emitted a photon must be re-excited before it can emit another, so two photons are never detected at the same time).

## 12.2. Imaging Optics and the Diffraction Limit

### 12.2.1. Image Formation as Fourier Optics

An objective lens collects light from the object plane and focuses it. In Abbe's theory of image formation, the field in the back focal plane of the objective is the **Fourier transform** of the field in the object plane, each point of the back focal plane corresponding to one direction of propagation, and the image plane carries a second transform of it ([5.4.2](/5.4.2)). The finite aperture of the objective admits only directions within the cone of half-angle $\alpha$, with **numerical aperture** $\mathrm{NA} = n\sin\alpha$, and so cuts off high spatial frequencies.

**Definition 12.2.1 (Point Spread Function)** The *point spread function* (PSF) of an imaging system is the image of a point source. For fluorescence, whose emitters are mutually incoherent, the image of an object with emitter density $\rho(\boldsymbol{r})$ is the **convolution** $I = \rho * \mathrm{PSF}$, and by the **convolution theorem** its Fourier transform is the product of the object spectrum with the optical transfer function $\mathrm{OTF} = \mathscr{F}\{\mathrm{PSF}\}$.

**Formula 12.2.1 (Airy Pattern and Its Gaussian Approximation)** For an aberration-free circular aperture, the lateral PSF in the focal plane at emission wavelength $\lambda$ is

$$
\mathrm{PSF}(r) = \left[\frac{2J_1(v)}{v}\right]^2, \qquad v = \frac{2\pi\,\mathrm{NA}\,r}{\lambda},
$$
the **Airy disk**, with the first zero at $r = 0.61\lambda/\mathrm{NA}$ and full width at half maximum $0.51\lambda/\mathrm{NA}$. Its central peak is well approximated by a Gaussian of standard deviation $s \approx 0.21\lambda/\mathrm{NA}$. The incoherent OTF is nonzero only for spatial frequencies below the cutoff $k_{\mathrm{c}} = 2\mathrm{NA}/\lambda$ (in cycles per unit length).

![Image formation in a diffraction-limited microscope (emission 600 nm, NA 1.4). A: the Airy PSF and its Gaussian approximation with σ = 0.21 λ/NA = 90 nm; the first zero lies at the Rayleigh distance 0.61 λ/NA = 261 nm. B: images of two point sources at the Rayleigh distance (a dip of 26 % between the peaks) and at half of it (a single peak): unresolved. C: the optical transfer function of the circular pupil, which falls to zero at the cutoff 2NA/λ = 4.7 µm⁻¹; finer periodic detail (period below 214 nm) is not transmitted at all](./plots/psf-otf.py)

The two classical resolution criteria are two ways of reading the same cutoff. The **Rayleigh criterion** declares two points resolved when the maximum of one image falls on the first zero of the other, $d = 0.61\lambda/\mathrm{NA}$; Abbe's limit is the finest period the OTF transmits, $d = \lambda/(2\mathrm{NA})$. For $\lambda = 600\,\mathrm{nm}$ and $\mathrm{NA} = 1.4$ they are $261$ and $214\,\mathrm{nm}$. Along the optical axis the PSF is elongated, with an axial extent of about $2n\lambda/\mathrm{NA}^2 \approx 900\,\mathrm{nm}$. These limits concern the ability to separate *simultaneously* emitting point sources; they say nothing about how precisely a single, isolated emitter can be located, which is limited by photons, not by diffraction (12.3). Super-resolution methods exploit exactly this distinction (12.4).

### 12.2.2. Sampling the Image

A camera records the image on a grid of pixels. By the sampling theorem, a signal whose spectrum is limited to frequencies below $k_{\mathrm{c}}$ is fully determined by samples spaced at most $1/(2k_{\mathrm{c}}) = \lambda/(4\mathrm{NA})$ apart in the object plane (the Nyquist criterion); with $\lambda/(4\mathrm{NA}) \approx 100\,\mathrm{nm}$, a $100\times$ objective with camera pixels of $10$–$16\,\mu\mathrm{m}$ gives effective pixels of $100$–$160\,\mathrm{nm}$. Coarser pixels lose information, finer ones divide the photons of each emitter over more pixels and add read noise. For single-molecule localization the best pixel size is close to the width $s$ of the PSF (12.3.1). The sampling theorem also governs the labeling of structures: a structure is resolved only if the labels on it are spaced closer than half the desired resolution (12.4.3).

### 12.2.3. Total Internal Reflection Illumination

When light passes from glass ($n_1 \approx 1.52$) into water ($n_2 = 1.33$) at an angle of incidence $\theta$ larger than the critical angle $\theta_{\mathrm{c}} = \arcsin(n_2/n_1) = 61.4^\circ$, it is totally reflected (**total internal reflection**). The field does not end abruptly at the interface: Maxwell's equations require an evanescent wave that propagates along the surface and decays exponentially into the second medium.

**Formula 12.2.2 (Evanescent Field)** Beyond the critical angle, the intensity in the medium of lower index decays with the distance $z$ from the interface as $I(z) = I_0\mathrm{e}^{-z/d}$, with the penetration depth

$$
d = \frac{\lambda_0}{4\pi\sqrt{n_1^2\sin^2\theta - n_2^2}},
$$
where $\lambda_0$ is the vacuum wavelength. ($d$ for the intensity is half the decay length of the amplitude used for ATR in [7.6.11](/7.6.11#sec-11.4.5).)

**Example 12.2.1** At $488\,\mathrm{nm}$ and $\theta = 65^\circ$, $n_1^2\sin^2\theta - n_2^2 = 2.304\times0.821 - 1.777 = 0.115$, so $d = 488/(4\pi\times0.339) = 115\,\mathrm{nm}$. In objective-type TIRF the beam is focused at the edge of the back focal plane of an objective with $\mathrm{NA} > n_2$; with $\mathrm{NA} = 1.49$ angles up to $\arcsin(1.49/1.518) = 79^\circ$ are reachable, and $d$ can be tuned between about $60$ and several hundred nanometers.

![Total internal reflection at a glass/water interface. A: penetration depth of the evanescent intensity against the angle of incidence for four laser wavelengths; it diverges at the critical angle (61.4°, dotted) and falls to 50–70 nm near the largest angle reachable with an NA 1.49 objective (dashed). B: intensity profiles at 488 nm for three angles: molecules on the coverslip or in the basal membrane of a cell are excited, whereas the bulk solution, a few hundred nanometers away, receives almost no light, in contrast to a confocal section of about 600 nm](./plots/tirf-depth.py)

**Total internal reflection fluorescence microscopy** ([7.3.2](/7.3.2)) uses this field to excite only molecules within about $100\,\mathrm{nm}$ of the surface. A molecule bound to the surface gives a bright, stationary spot; molecules diffusing in solution pass through the thin excited layer in microseconds and contribute only a weak, uniform background, so binding events of labeled ligands can be watched one by one even at nanomolar concentrations. This is why TIRF, with electron-multiplying CCD or scientific CMOS cameras, became the workhorse of single-molecule imaging in vitro (DNA replication and repair, translation, motors on surface-attached filaments) and at the basal membrane of cells (endocytosis, exocytosis, receptor clustering). Highly inclined illumination (HILO), just below the critical angle, illuminates a thin oblique sheet a few micrometers deep and extends single-molecule imaging into the nucleus.

### 12.2.4. Confocal Detection Volumes

In confocal detection a laser is focused to a diffraction-limited spot and a pinhole in the image plane rejects light from outside the focus ([6.4.10](/6.4.10#sec-10.4.2)). The product of the excitation intensity and the detection probability, the molecule detection function, is approximately a three-dimensional Gaussian,

$$
W(\boldsymbol{r}) = \exp\left(-\frac{2(x^2 + y^2)}{w_0^2} - \frac{2z^2}{z_0^2}\right),
$$
with a lateral $1/\mathrm{e}^2$ radius $w_0 \approx 0.2$–$0.3\,\mu\mathrm{m}$ and an axial radius $z_0 \approx 1$–$1.5\,\mu\mathrm{m}$ (aspect ratio $\omega = z_0/w_0 \approx 4$–$6$). Its effective volume, $V_{\mathrm{eff}} = (\int W)^2/\int W^2 = \pi^{3/2}w_0^2z_0$, is about $0.2$–$1\,\mathrm{fL}$. At $1\,\mathrm{nM}$ it contains on average $0.6\times V_{\mathrm{eff}}/\mathrm{fL}$ molecules. Confocal volumes are used for single-molecule detection of freely diffusing molecules at picomolar concentrations (12.5.4) and for correlation spectroscopy at nanomolar concentrations (12.6), with single-photon avalanche diodes that time every photon with sub-nanosecond precision.

## 12.3. Localization, Tracking and Counting

### 12.3.1. Localization Precision

A single, isolated emitter produces a spot whose shape, the PSF, is known. Its center can be estimated with a precision much better than the width of the spot, because each detected photon is an independent sample from the PSF.

**Theorem 12.3.1 (Photon-Limited Localization)** Let $N$ photons be detected from an emitter at position $x_0$, each landing at a position drawn independently from a Gaussian PSF of standard deviation $s$, with no pixelation and no background. Then no unbiased estimator of $x_0$ has a variance smaller than $s^2/N$, and the mean of the photon positions attains this bound.

**Proof** One photon at $x$ has log-likelihood $\ell(x_0) = -(x - x_0)^2/(2s^2) + \text{const}$, with Fisher information $\mathbb{E}[(\partial\ell/\partial x_0)^2] = 1/s^2$. For $N$ independent photons the information is $N/s^2$, and by the Cramér–Rao inequality every unbiased estimator has variance at least $s^2/N$. The sample mean is unbiased with variance $s^2/N$. $\square$

**Definition 12.3.1 (Localization Precision)** The **localization precision** of a single-emitter measurement is the standard deviation $\sigma_{\mathrm{loc}}$ of the estimated position about the true one, in each coordinate.

Real images are pixelated and carry background, which add terms to the bound.

**Formula 12.3.1 (Localization Precision with Pixels and Background)** For pixels of size $a$ and a background of $b^2$ photons per pixel (Poisson, so $b$ is its standard deviation), least-squares fitting of a Gaussian gives approximately (Thompson, Larson and Webb, 2002)

$$
\sigma_{\mathrm{loc}}^2 \approx \frac{s^2 + a^2/12}{N} + \frac{8\pi s^4b^2}{a^2N^2},
$$
and maximum-likelihood fitting, which reaches the Cramér–Rao bound for this model, $\sigma_{\mathrm{loc}}^2 = (s_a^2/N)[1 + 4\tau + \sqrt{2\tau/(1 + 4\tau)}]$ with $s_a^2 = s^2 + a^2/12$ and $\tau = 2\pi s_a^2b^2/(Na^2)$ (Mortensen and colleagues, 2010). An electron-multiplying camera adds excess noise equivalent to halving $N$.

The first term is the photon-limited bound broadened by pixelation (a uniform distribution within a pixel has variance $a^2/12$); the second is the background, which dominates for dim emitters and makes the precision fall as $1/N$ rather than $1/\sqrt N$. With $s = 100\,\mathrm{nm}$, $a = 100\,\mathrm{nm}$ and $b = 5$, $N = 1000$ photons give $\sigma_{\mathrm{loc}} = 4.1\,\mathrm{nm}$ and $N = 10^4$ photons $1.1\,\mathrm{nm}$. The optimum pixel size is about $s$: smaller pixels spread the signal over more background, larger ones lose position information.

![Localization of single emitters (simulation: Gaussian PSF with s = 130 nm, 100 nm pixels, background 4 photons per pixel). A: one spot with N = 500 photons. B: 400 maximum-likelihood localizations of an emitter at the origin with N = 500: σ = 7.6 nm, about 1/17 of the PSF width. C: localization error against photon number for the maximum-likelihood estimator (circles), which follows the Mortensen formula and approaches the photon-limited bound s/√N at high N, and for the simple centroid (squares), which is pulled towards the center of the region by the uniform background and gains little from more photons](./plots/localization-precision.py)

In practice the precision achieved is limited further by drift of the stage (corrected with fiducial markers), by the fixed dipole orientation of immobilized fluorophores, which shifts the apparent position by up to tens of nanometers unless polarization or PSF models account for it, and by the size and flexibility of the label itself (a primary and secondary antibody place the dye up to $20\,\mathrm{nm}$ from the target). Three-dimensional positions are encoded in the PSF shape: a cylindrical lens makes the spot elliptical above and below focus (astigmatism), giving $z$ with about twice the lateral error.

### 12.3.2. FIONA: Nanometer Steps of Molecular Motors

Fluorescence imaging with one-nanometer accuracy (FIONA; Yildiz and colleagues, 2003) applied Theorem 12.3.1 to the motor myosin V, a two-headed **myosin** that carries cargo along actin filaments in steps of $36\,\mathrm{nm}$ of its center of mass ([7.3.13](/7.3.13)). Two models were debated. In an inchworm mechanism one head always leads and every part of the molecule moves $36\,\mathrm{nm}$ per step. In a hand-over-hand mechanism the heads alternate in the lead, like walking: the trailing head swings forward by $72\,\mathrm{nm}$ past the leading one. A dye on one light-chain domain, at a distance $x$ from the midpoint between the heads along the filament, then moves alternately $36 + 2x$ and $36 - 2x$; a dye near one motor domain moves $72\,\mathrm{nm}$ every second step and stays still on the other. With a Cy3 label, $5000$–$10\,000$ photons per $0.5\,\mathrm{s}$ frame and oxygen scavengers, the dye positions were determined to $1.5\,\mathrm{nm}$, and the steps were $74 \pm 5\,\mathrm{nm}$, or alternating $42$ and $32\,\mathrm{nm}$ for labels off center: hand over hand. The same approach showed that **kinesin** and cytoplasmic **dynein** also walk hand over hand, the latter with variable steps.

### 12.3.3. Single-Particle Tracking

Localizing a particle in successive frames gives its trajectory. The **mean squared displacement** of a trajectory, estimated as the time average over all pairs of frames separated by $n\Delta t$, distinguishes modes of motion ([7.3.2](/7.3.2#sec-2.6.4), [7.6.5](/7.6.5#sec-5.1.1)). Two experimental effects distort it.

**Formula 12.3.2 (MSD with Localization Error and Motion Blur)** For free diffusion in $d$ dimensions with coefficient $D$, frames of interval $\Delta t$ with exposure $t_{\mathrm{E}}$ and localization precision $\sigma_{\mathrm{loc}}$ per coordinate,

$$
\mathrm{MSD}(n\Delta t) = 2dD\,n\Delta t + 2d\sigma_{\mathrm{loc}}^2 - \frac{2d}{3}Dt_{\mathrm{E}},
$$
the second term from localization error, which adds an offset, and the third from averaging the position during the exposure (motion blur), which subtracts one.

The time-averaged MSD of one trajectory of $M$ frames has strongly correlated errors at different lags, and its variance grows with the lag; estimates of $D$ from fits over the first few lags are nearly optimal, and the optimal number of points depends on the ratio $\sigma_{\mathrm{loc}}^2/(D\Delta t)$ (Michalet, 2010). Unbiased alternatives use the covariance of successive displacements, whose expectation is $-\sigma_{\mathrm{loc}}^2 + Dt_{\mathrm{E}}/3$ per coordinate, or maximum-likelihood estimators of the whole trajectory. For anomalous diffusion, $\mathrm{MSD} \propto t^\alpha$, the exponent is best estimated from many trajectories; the physical mechanisms of subdiffusion in crowded cells are treated in [7.6.23](/7.6.23). Tracking of single receptors, lipids, transcription factors and viruses has shown hop diffusion between membrane compartments, transient confinement in nanodomains and the search of transcription factors along chromatin ([7.2.22](/7.2.22)).

### 12.3.4. Counting Subunits by Photobleaching Steps

A complex of $n$ subunits, each labeled with one fluorophore, bleaches in up to $n$ discrete steps, one for each fluorophore (Ulbrich and Isacoff, 2007). Not every label is fluorescent: fluorescent proteins fail to mature, dyes fail to attach, some are bleached before recording.

**Formula 12.3.3 (Binomial Step Counting)** If each of the $n$ labels is fluorescent independently with probability $p$, the number $k$ of bleaching steps of the spots that are seen ($k \ge 1$) follows the truncated binomial distribution

$$
\mathbb{P}(k) = \frac{\binom{n}{k}p^k(1 - p)^{n - k}}{1 - (1 - p)^n}, \qquad k = 1, \dots, n.
$$

![Counting subunits by photobleaching (simulation of a tetramer, each subunit fused to GFP that is fluorescent with probability 0.75). A: intensity traces of three spots, with 4, 3 and 2 bleaching steps (the black staircase is the true number of active fluorophores). B: the distribution of step numbers in 300 spots matches the truncated binomial distribution for n = 4 and not that for n = 3 with the same p](./plots/photobleaching-steps.py)

The value of $p$ is calibrated with a protein of known stoichiometry under the same conditions. The method identified the tetrameric assembly of voltage-gated potassium channels and of the Orai calcium channel in membranes and the number of subunits in bacterial flagellar motors; it fails when the number of fluorophores exceeds about $10$, because steps then become smaller than the noise and overlap in time, and for larger assemblies the total intensity is calibrated against a single fluorophore.

## 12.4. Super-Resolution Microscopy: Physical Limits

### 12.4.1. Two Strategies

**Super-resolution fluorescence microscopy** ([6.4.10](/6.4.10#def-10.4.2)) breaks the diffraction limit of 12.2.1 by ensuring that emitters closer than the limit do not emit at the same time, or not in the same way. There are two strategies. *Deterministic* methods (STED, RESOLFT) shape the region in which molecules can fluoresce, by switching off molecules everywhere except near a zero of a light pattern, and scan this region over the sample; the information that separates two emitters is the time at which the scanning region passes over each. *Stochastic* methods (PALM, STORM, PAINT) switch on a sparse, random subset of molecules in each camera frame, localize each one (12.3.1) and accumulate the localizations; the information is the time at which each molecule happens to be on. In both, the separating "distance" between molecules is a difference in state, which light can control, rather than a difference in position, which diffraction blurs. Both rely on a fluorophore with two states of different emission and a light-driven transition between them: stimulated emission (STED), photoswitching between isomers (RESOLFT, PALM, STORM) or reversible binding (PAINT).

### 12.4.2. STED: Saturated Depletion

In stimulated emission depletion (Hell and Wichmann, 1994; Klar and colleagues, 2000) an excitation pulse is followed within picoseconds by a red-shifted depletion pulse with a doughnut-shaped profile, zero intensity at the center. In the doughnut, excited molecules are driven back to the ground state by **stimulated emission** before they fluoresce spontaneously; the stimulated photons travel with the depletion beam and are filtered out. Let $I_{\mathrm{s}}$ be the depletion intensity at which the probability that an excited molecule survives the pulse falls to $1/\mathrm{e}$; then the survival is $\eta(I) = \mathrm{e}^{-I/I_{\mathrm{s}}}$.

**Proposition 12.4.1 (Resolution of STED)** Let the excitation PSF be a Gaussian of full width $d_0$ at half maximum, $\exp(-4\ln2\,x^2/d_0^2)$, and the depletion intensity near its zero be $I(x) = 4\ln2\,I_{\max}x^2/d_0^2$. Then the effective PSF is a Gaussian of full width

$$
d = \frac{d_0}{\sqrt{1 + I_{\max}/I_{\mathrm{s}}}}, \qquad d_0 \approx \frac{\lambda}{2\,\mathrm{NA}}.
$$

**Proof** The probability of fluorescence from position $x$ is the product $\exp(-4\ln2\,x^2/d_0^2)\exp(-4\ln2\,I_{\max}x^2/(I_{\mathrm{s}}d_0^2)) = \exp[-4\ln2\,x^2(1 + I_{\max}/I_{\mathrm{s}})/d_0^2]$, a Gaussian whose full width at half maximum is $d_0/\sqrt{1 + I_{\max}/I_{\mathrm{s}}}$. $\square$

The square-root law shows that there is no fundamental limit to the resolution, only a practical one: halving the spot size needs four times more depletion intensity. The saturation intensity is $I_{\mathrm{s}} \approx h\nu/(\sigma_{\mathrm{STED}}\tau)$ with the stimulated emission cross-section $\sigma_{\mathrm{STED}}$ at the red edge of the emission band; for $\sigma_{\mathrm{STED}} \approx 10^{-17}\,\mathrm{cm^2}$, $\tau = 3\,\mathrm{ns}$ and $775\,\mathrm{nm}$ light, $I_{\mathrm{s}} \approx 9\,\mathrm{MW\,cm^{-2}}$, so a resolution of $25\,\mathrm{nm}$ from $d_0 = 250\,\mathrm{nm}$ needs $I_{\max} \approx 100I_{\mathrm{s}}$, about $1\,\mathrm{GW\,cm^{-2}}$ in the pulse. The intensity drives photobleaching and limits STED to robust dyes and modest exposure of living cells. RESOLFT uses photoswitchable proteins with long-lived on and off states, whose switching saturates at intensities lower by about six orders of magnitude, at the price of slower imaging.

### 12.4.3. Single-Molecule Localization Microscopy

In **single-molecule localization microscopy** ([7.3.2](/7.3.2#def-2.4.1)) the image is rebuilt from localizations of molecules switched on sparsely: photoactivatable or photoconvertible fluorescent proteins (PALM; Betzig and colleagues, 2006), photoswitchable dyes that cycle between dark and bright states in a reducing buffer (STORM; Rust, Bates and Zhuang, 2006), or labeled DNA strands that bind transiently to complementary docking strands on the target (DNA-PAINT, whose emitters are replenished from solution and therefore do not bleach). Each frame must contain at most one emitting molecule per diffraction-limited area, so the duty cycle (the fraction of time a molecule is on) must be below the inverse of the number of labels within one PSF area; dyes with duty cycles of about $10^{-3}$ allow densities of thousands of labels per square micrometer.

The resolution of the final image combines two limits. One is the localization precision $\sigma_{\mathrm{loc}}$, which blurs each label into a Gaussian of full width $2.355\sigma_{\mathrm{loc}}$. The other is the density of labels: by the sampling theorem, a structure is resolved at resolution $R$ only if labels are spaced at most $R/2$ along it, which in two dimensions needs a density of at least $(2/R)^2$. A common estimate of the effective resolution is $R \approx \sqrt{(2.355\sigma_{\mathrm{loc}})^2 + (2/\sqrt{\rho})^2}$ for label density $\rho$; a resolution of $20\,\mathrm{nm}$ thus needs $\sigma_{\mathrm{loc}} < 8\,\mathrm{nm}$ and more than $10^4$ labels per square micrometer, which are rarely achieved together. Further limits are the size of the labels (antibodies are $10\,\mathrm{nm}$ long, nanobodies and small tags $2$–$4\,\mathrm{nm}$), multiple counting of blinking molecules, and drift; the resolution actually attained is measured with the Fourier ring correlation between two independent halves of the data, the two-dimensional analog of the Fourier shell correlation of cryo-electron microscopy ([7.6.14](/7.6.14)).

![Physical limits of super-resolution. A: STED: the effective PSF width falls as d0/√(1 + I/Is) (d0 = 250 nm; 75 nm at I/Is = 10, 25 nm at 100); inset: one-dimensional fluorescence profiles for no depletion and for I/Is = 10 and 100, computed with a doughnut sin² profile. B: SMLM: the resolution combines the localization precision with the Nyquist requirement on label density; at low density it is limited by sampling (dotted), at high density by precision (5, 10 and 20 nm). C: precision per detected photon: camera localization with s = 100 nm (Theorem 12.3.1) and MINFLUX with the doughnut zero probed over a range L = 100, 50 and 20 nm (Proposition 12.4.2): MINFLUX reaches nanometer precision with tens to hundreds of photons](./plots/superres-limits.py)

### 12.4.4. MINFLUX: Localization with a Zero of Light

Camera localization extracts position information from the photons of an emitter excited uniformly; the information per photon is limited by the width $s$ of the PSF (Theorem 12.3.1). MINFLUX (Balzarotti and colleagues, 2017) instead excites the molecule with a doughnut whose zero is placed at a few known positions close to the molecule and infers its position from the ratio of the photon counts. Near the zero, the excitation grows quadratically with the distance, so photon counts become very sensitive to small displacements.

**Proposition 12.4.2 (One-Dimensional MINFLUX Precision)** Let a molecule at position $x$ near the origin be excited alternately by a doughnut with its zero at $-L/2$ and at $+L/2$, with intensity proportional to the squared distance from the zero, and let $N$ photons be detected in total. Then the position estimated from the fraction of photons in the first exposure has, at $x = 0$, the standard deviation

$$
\sigma_x = \frac{L}{4\sqrt N}.
$$

**Proof** The probability that a detected photon comes from the first exposure is $p(x) = (x + L/2)^2/[(x + L/2)^2 + (x - L/2)^2]$. At $x = 0$, $p = 1/2$ and $\mathrm{d}p/\mathrm{d}x = 2/L$. The fraction $\hat p$ of $N$ photons in the first exposure is binomial with variance $p(1 - p)/N = 1/(4N)$, and propagating it through $x = p^{-1}(\hat p)$ gives $\sigma_x = \sqrt{1/(4N)}/(2/L) = L/(4\sqrt N)$. $\square$

The precision is set by the probing range $L$, which the experimenter chooses, rather than by the PSF width: with $L = 50\,\mathrm{nm}$, $100$ photons give $1.25\,\mathrm{nm}$, for which camera localization with $s = 100\,\mathrm{nm}$ would need $6400$ photons. Iterative MINFLUX first localizes the molecule coarsely and then shrinks $L$ around it. With this photon efficiency, single molecules have been tracked with nanometer precision at sub-millisecond intervals, resolving the $16\,\mathrm{nm}$ substeps of kinesin under physiological ATP concentrations, and fixed structures such as the nuclear pore complex have been imaged with $1$–$3\,\mathrm{nm}$ precision. The cost is a small field of view and the need for molecules that are individually on, as in SMLM.

### 12.4.5. Structured Illumination and Other Approaches

In structured illumination microscopy (SIM) the sample is illuminated with a sinusoidal pattern of spatial frequency $k_{\mathrm{i}}$. The emission is the product of the sample density and the illumination, so its spectrum contains copies of the sample spectrum shifted by $\pm k_{\mathrm{i}}$ (moiré fringes): object frequencies up to $k_{\mathrm{c}} + k_{\mathrm{i}}$ are moved into the passband of the OTF and can be recovered computationally from images with several phases and orientations of the pattern. Since the illumination is itself diffraction limited, $k_{\mathrm{i}} \le k_{\mathrm{c}}$ and the resolution improves at most twofold, to about $100\,\mathrm{nm}$; with nonlinear (saturated) excitation, harmonics of the pattern extend it further. SIM uses ordinary fluorophores and low intensities and is fast, the method of choice for live cells in three dimensions. Image scanning microscopy and Airyscan reach the same twofold gain by replacing the confocal pinhole with an array detector; super-resolution optical fluctuation imaging (SOFI) uses the statistics of blinking rather than individual localization; and expansion microscopy enlarges the sample itself about fourfold to twentyfold in a swellable hydrogel. The table in [7.3.2](/7.3.2#sec-2.4.1) compares the methods for cell biology.

## 12.5. Single-Molecule FRET

### 12.5.1. Measuring FRET Efficiency on One Molecule

**Definition 12.5.1 (Single-Molecule FRET)** **Single-molecule FRET** (smFRET) is the measurement of the Förster transfer efficiency between a donor and an acceptor attached to one molecule (or to two molecules of one complex), from the photon counts of the two dyes, as a function of time.

Single-molecule FRET was first demonstrated on surface-immobilized DNA by Ha and colleagues in 1996. It measures distances of $3$–$10\,\mathrm{nm}$ through the Förster law $E = 1/[1 + (R/R_0)^6]$ ([7.6.11](/7.6.11#fml-11.5.3)), but in contrast to ensemble FRET it measures the distribution of distances and the rates of change between them. From donor and acceptor counts $I_{\mathrm{D}}$ and $I_{\mathrm{A}}$ under donor excitation, the apparent efficiency (proximity ratio) $E_{\mathrm{app}} = I_{\mathrm{A}}/(I_{\mathrm{A}} + I_{\mathrm{D}})$ suffices for following dynamics. Accurate distances need corrections:

$$
E = \frac{I_{\mathrm{A}} - \beta I_{\mathrm{D}} - \delta I_{\mathrm{A}}^{\mathrm{dir}}}{I_{\mathrm{A}} - \beta I_{\mathrm{D}} - \delta I_{\mathrm{A}}^{\mathrm{dir}} + \gamma I_{\mathrm{D}}}, \qquad \gamma = \frac{\eta_{\mathrm{A}}\Phi_{\mathrm{A}}}{\eta_{\mathrm{D}}\Phi_{\mathrm{D}}},
$$
with $\beta$ the leakage of donor emission into the acceptor channel, the term $\delta I_{\mathrm{A}}^{\mathrm{dir}}$ the acceptor emission due to direct excitation, and $\gamma$ the ratio of detection efficiencies $\eta$ and quantum yields. Alternating laser excitation (ALEX), which excites the acceptor directly in alternate pulses, sorts molecules by stoichiometry, removes those lacking an active acceptor and determines the correction factors from the data. A blind study of the same DNA samples in twenty laboratories obtained FRET efficiencies that agreed to $\pm0.02$–$0.05$ and distances to about $\pm2\,\%$ when these corrections were applied (Hellenkamp and colleagues, 2018). Remaining uncertainties are the orientation factor $\kappa^2$, which is close to $2/3$ when the anisotropies of the dyes are low ([7.6.11](/7.6.11#sec-11.5.7)), and the position of the dyes on their flexible linkers, which is modeled by computing the accessible volume of each dye on a structural model.

The good dye pairs for smFRET have high quantum yields, well-separated absorption and emission spectra, and similar brightness. Cy3–Cy5 ($R_0 \approx 5.5\,\mathrm{nm}$), Alexa 555–Alexa 647, Atto 550–Atto 647N and Alexa 488–Alexa 594 are common.

### 12.5.2. Shot Noise and the Width of FRET Histograms

**Proposition 12.5.1 (Shot-Noise Width)** If a molecule has a fixed efficiency $E$ during a measurement in which $N$ photons are detected and each photon is independently an acceptor photon with probability $E$ (corrected data, no background), the measured $\hat E = N_{\mathrm{A}}/N$ is binomial with

$$
\mathbb{E}[\hat E] = E, \qquad \operatorname{Var}(\hat E) = \frac{E(1 - E)}{N}.
$$

For $E = 0.5$ and $N = 100$ the standard deviation is $0.05$, and the width of a FRET histogram built from many such measurements, each with its own $N$, is the average of these binomial widths. A histogram broader than this shot-noise limit means that $E$ itself varies: because molecules differ in conformation (static heterogeneity) or because they change conformation during the measurement (dynamics). Comparing the measured width with the shot-noise prediction, computed from the actual photon numbers by probability distribution analysis, therefore separates heterogeneity from noise. For a molecule that switches between two states with efficiencies $E_1$ and $E_2$ much faster than the measurement time, the histogram is a single shot-noise-limited peak at the population-weighted mean; for switching much slower than the measurement, two peaks; for comparable times, a broad distribution bridging the two.

![Single-molecule FRET histograms of freely diffusing molecules (simulated bursts of about 1 ms with at least 40 photons; two states with E = 0.30 and 0.75, equally populated). A: without interconversion, two peaks whose widths agree with the binomial shot-noise limit (red). B: exchange much faster than the burst duration (2 × 10⁴ s⁻¹ each way): a single peak at the mean, again shot-noise limited. C: exchange on the time scale of the burst (10³ s⁻¹): the distribution fills the region between the states and is much broader than shot noise, the signature of millisecond dynamics](./plots/smfret-histograms.py)

### 12.5.3. Freely Diffusing Molecules: Burst Analysis

In confocal smFRET, molecules diffuse through the focus one at a time. The concentration is kept at $50$–$100\,\mathrm{pM}$, so that the probability of two molecules in a femtoliter volume, from the **Poisson distribution** with mean $\langle n\rangle = cN_{\mathrm{A}}V_{\mathrm{eff}} \approx 0.05$, is about $10^{-3}$. Each passage takes about a millisecond ($\tau_{\mathrm{D}} = w_0^2/4D$, 12.6.2) and yields a burst of $50$–$200$ photons, from which one efficiency is computed. Minutes of recording give thousands of bursts and a histogram; the molecules are never perturbed by a surface, and the method is suited to proteins that are difficult to immobilize, to intrinsically disordered proteins and to folding studies under equilibrium denaturant conditions ([7.6.16](/7.6.16)). The time window is limited above by the burst duration, but within a burst the photon arrival times, recorded with picosecond resolution, contain information on dynamics from nanoseconds to milliseconds, extracted by burst-variance analysis, by maximum-likelihood analysis of the photon sequences or by correlation (12.6). Microfluidic mixers bring molecules into nonequilibrium conditions and follow folding after a jump of denaturant.

### 12.5.4. Immobilized Molecules: Trajectories and Hidden Markov Models

Molecules tethered to a passivated surface (polyethylene glycol, biotin–streptavidin linkage) and imaged by TIRF give trajectories of seconds to minutes with $1$–$100\,\mathrm{ms}$ frames, until one of the dyes bleaches. Anticorrelated changes of donor and acceptor intensity are the signature of FRET changes; simultaneous loss of both signals or a change of only one indicates photophysics. To extract states and rates, the trajectory is modeled as a **hidden Markov model**: the conformational state is a hidden Markov chain with transition probabilities $a_{ij}$ per frame, and each frame emits an observed efficiency drawn from a distribution, often Gaussian, characteristic of the state.

**Algorithm 12.5.1 (Kinetic Analysis of an smFRET Trajectory)**

1. Choose a number of states $K$ and initial guesses for their mean efficiencies, widths and the transition matrix.
2. Fit the parameters by maximizing the likelihood of the observed trajectory, computed by the forward–backward algorithm, with the Baum–Welch (expectation–maximization) iteration; for several trajectories, fit them jointly or with a hierarchical model.
3. Find the most probable state sequence with the **Viterbi algorithm**.
4. Collect the dwell times of each state from the state sequence; fit their distributions (Proposition 12.1.1) or convert the transition probabilities directly into rates, $k_{ij} \approx a_{ij}/\Delta t$ for $a_{ij} \ll 1$.
5. Select $K$ by a penalized likelihood (Bayesian information criterion) or a Bayesian model comparison, and check with simulated data that the analysis recovers known rates.

![Kinetics from one smFRET trajectory (simulation: two states with E = 0.30 and 0.75, k12 = 2 s⁻¹, k21 = 1 s⁻¹, 20 ms frames, 150 photons per frame, acceptor bleaching at 200 s). A: donor and acceptor intensities are anticorrelated until the acceptor bleaches, after which the donor alone is bright. B: the efficiency trace (first 25 s) and the Viterbi path of a two-state Gaussian hidden Markov model fitted by Baum–Welch, which recovers E = 0.31 and 0.74. C: dwell-time histograms from the Viterbi path with exponential densities: the rates recovered from one trajectory (1.6 and 0.9 s⁻¹) are within the statistical error of about 10–15 % of the true values; dwells shorter than a few frames are missed, which biases rates near the frame rate](./plots/smfret-hmm.py)

Since rates are recovered from the stochastic dynamics at equilibrium, smFRET measures both the equilibrium constant, as the ratio of rates or of occupancies, and the kinetics without any perturbation. Classic results include the spontaneous fluctuation of the ribosome between classical and hybrid states of its tRNAs before translocation, the conformational dynamics of the Holliday junction between its stacked forms, the folding of ribozymes through intermediates, the unwinding of DNA by helicases in steps of a few base pairs, and the activation of **G protein–coupled receptors** through an ensemble of interconverting conformations. Multicolor smFRET with three or four dyes measures several distances at once, and smFRET combined with optical tweezers ([7.6.17](/7.6.17)) correlates conformation with force.

## 12.6. Fluorescence Correlation Spectroscopy

### 12.6.1. Fluctuations of a Few Molecules

When a confocal volume contains on average a few molecules, their number fluctuates as molecules diffuse in and out. For independent molecules the number in the volume is Poisson distributed, $\operatorname{Var}(n) = \langle n\rangle$, so the relative fluctuation is $1/\sqrt{\langle n\rangle}$: large for few molecules, negligible for many. The fluctuations decay on the time it takes a molecule to cross the volume, and any process that changes the brightness of a molecule (blinking, binding, conformational change) adds its own fluctuations on its own time scale.

**Definition 12.6.1 (Fluorescence Correlation Spectroscopy)** **Fluorescence correlation spectroscopy** (FCS; Magde, Elson and Webb, 1972) is the determination of concentrations, diffusion coefficients and rate constants from the normalized autocorrelation function of the fluorescence intensity $F(t)$ recorded from a small volume,

$$
G(\tau) = \frac{\langle\delta F(t)\,\delta F(t + \tau)\rangle}{\langle F\rangle^2}, \qquad \delta F = F - \langle F\rangle,
$$
with the average taken over $t$. (Some authors define $G$ as $1$ plus this quantity.)

FCS is related to **dynamic light scattering** ([7.6.8](/7.6.8)), which correlates the fluctuations of scattered light, but it works at concentrations a million times lower, selects the labeled species, and its amplitude has a direct meaning: the inverse of the number of molecules.

### 12.6.2. The Diffusion Autocorrelation

**Theorem 12.6.1 (FCS for Free Diffusion)** Let identical, independent molecules of brightness $q$ (detected photons per unit time per molecule at the center) diffuse with coefficient $D$ at mean concentration $\bar c$ through a Gaussian detection profile $W(\boldsymbol{r})$ with radii $w_0$ and $z_0$ (12.2.4). Then

$$
G(\tau) = \frac{1}{\langle N\rangle}\left(1 + \frac{\tau}{\tau_{\mathrm{D}}}\right)^{-1}\left(1 + \frac{\tau}{\omega^2\tau_{\mathrm{D}}}\right)^{-1/2}, \qquad \tau_{\mathrm{D}} = \frac{w_0^2}{4D}, \quad \omega = \frac{z_0}{w_0}, \tag{12.1}
$$
where $\langle N\rangle = \bar cV_{\mathrm{eff}}$ is the mean number of molecules in the effective volume $V_{\mathrm{eff}} = \pi^{3/2}w_0^2z_0$.

**Proof** The intensity is $F(t) = q\int W(\boldsymbol{r})c(\boldsymbol{r}, t)\,\mathrm{d}^3\boldsymbol{r}$, so $\langle F\rangle = q\bar c\int W$ and

$$
\langle\delta F(0)\delta F(\tau)\rangle = q^2\iint W(\boldsymbol{r})W(\boldsymbol{r}')\langle\delta c(\boldsymbol{r}, 0)\,\delta c(\boldsymbol{r}', \tau)\rangle\,\mathrm{d}^3\boldsymbol{r}\,\mathrm{d}^3\boldsymbol{r}'.
$$
For independent particles the equal-time concentration fluctuations are uncorrelated in space with Poisson amplitude, $\langle\delta c(\boldsymbol{r}, 0)\delta c(\boldsymbol{r}', 0)\rangle = \bar c\,\delta(\boldsymbol{r} - \boldsymbol{r}')$, and each fluctuation then spreads by diffusion with the Gaussian propagator of the **heat equation** ([7.6.5](/7.6.5#fml-5.2.1)), so $\langle\delta c(\boldsymbol{r}, 0)\delta c(\boldsymbol{r}', \tau)\rangle = \bar c(4\pi D\tau)^{-3/2}\exp(-\lvert\boldsymbol{r} - \boldsymbol{r}'\rvert^2/4D\tau)$. All integrals factorize into one-dimensional Gaussian integrals. For the $x$ coordinate, with $W_x = \mathrm{e}^{-2x^2/w_0^2}$,

$$
\iint\mathrm{e}^{-2x^2/w_0^2}\mathrm{e}^{-2x'^2/w_0^2}\frac{\mathrm{e}^{-(x - x')^2/4D\tau}}{\sqrt{4\pi D\tau}}\,\mathrm{d}x\,\mathrm{d}x' = \frac{\sqrt{\pi}\,w_0}{2}\left(1 + \frac{4D\tau}{w_0^2}\right)^{-1/2},
$$
the convolution of three Gaussians, whose variances $w_0^2/4$, $w_0^2/4$ and $2D\tau$ add. The same holds for $y$, and for $z$ with $z_0$. Dividing by $\langle F\rangle^2 = q^2\bar c^2(\pi/2)^3w_0^4z_0^2$ and using $(\sqrt\pi w_0/2)^2(\sqrt\pi z_0/2)/(\pi/2)^3w_0^4z_0^2 = 1/(\pi^{3/2}w_0^2z_0)$ gives Eq. (12.1). $\square$

The amplitude $G(0) = 1/\langle N\rangle$ gives the absolute concentration once $V_{\mathrm{eff}}$ is calibrated with a dye of known diffusion coefficient (rhodamine 6G, $D = 414\,\mu\mathrm{m^2\,s^{-1}}$ at $25\,^\circ\mathrm{C}$), and the decay time gives $D$ and, through the **Stokes–Einstein equation**, the hydrodynamic radius. Since $\tau_{\mathrm{D}} \propto 1/D \propto R_{\mathrm{h}} \propto M^{1/3}$ for globular molecules, binding of a small labeled ligand to a large protein is easily seen, but an eightfold increase in mass only doubles $\tau_{\mathrm{D}}$, so complexes of similar size are hard to distinguish by diffusion alone. Uncorrelated background $B$ reduces the amplitude by $(1 - B/\langle F\rangle)^2$.

**Example 12.6.1** With $w_0 = 0.25\,\mu\mathrm{m}$ and $\omega = 5$, free rhodamine has $\tau_{\mathrm{D}} = 0.0625/(4\times414)\,\mathrm{s} = 38\,\mu\mathrm{s}$, GFP ($D = 87\,\mu\mathrm{m^2\,s^{-1}}$) $180\,\mu\mathrm{s}$, and an antibody-sized complex ($40\,\mu\mathrm{m^2\,s^{-1}}$) $390\,\mu\mathrm{s}$. $V_{\mathrm{eff}} = \pi^{3/2}\times0.0625\times1.25\,\mu\mathrm{m^3} = 0.43\,\mathrm{fL}$, so $G(0) = 0.2$ ($\langle N\rangle = 5$) corresponds to $5/(0.43\times10^{-15}\,\mathrm{L}\times6.02\times10^{23}\,\mathrm{mol^{-1}}) = 19\,\mathrm{nM}$.

![Fluorescence correlation spectroscopy. A: autocorrelation curves for a confocal volume with w0 = 0.25 µm and ω = 5 at ⟨N⟩ = 5: a free dye, GFP and an antibody-sized complex; the dye curve with a 15 % triplet fraction (2 µs) shows an extra fast decay; GFP at ⟨N⟩ = 3 and 10 (dotted) shows that the amplitude is the inverse number of molecules. B: Brownian dynamics simulation of 720 particles (D = 10 µm² s⁻¹) in a periodic box around a Gaussian detection volume (w0 = 0.3 µm, z0 = 1.5 µm): the autocorrelation of the simulated intensity agrees with Eq. (12.1) for ⟨N⟩ = 5.0 and τ_D = 2.25 ms within the statistical error of a 5 s record. C: the simulated intensity, which fluctuates by tens of percent about its mean](./plots/fcs-curves.py)

### 12.6.3. Kinetics, Triplets and Cross-Correlation

If molecules also switch between a bright state and a dark state (triplet, protonated form, quenched conformation) with relaxation time $\tau_{\mathrm{R}} = 1/(k_+ + k_-)$ and dark fraction $F_{\mathrm{dark}}$, and the switching is independent of position, the correlation function factorizes:

$$
G(\tau) = G_{\mathrm{diff}}(\tau)\,\frac{1 - F_{\mathrm{dark}} + F_{\mathrm{dark}}\mathrm{e}^{-\tau/\tau_{\mathrm{R}}}}{1 - F_{\mathrm{dark}}}.
$$
Only processes faster than diffusion through the volume appear as separate components; slower ones are averaged out because a molecule leaves before it switches. Every dye shows a triplet component of microseconds that must be included in fits. Using this, FCS measures the photophysics of fluorescent proteins, protonation kinetics of GFP chromophores, and conformational fluctuations of DNA hairpins and proteins on microsecond scales when a dye–quencher pair (for example tryptophan quenching of an oxazine dye by photoinduced electron transfer) reports contact formation.

In fluorescence cross-correlation spectroscopy (FCCS; Schwille and colleagues, 1997) two differently labeled species are detected in overlapping volumes of two colors, and the cross-correlation $G_{\times}(\tau) = \langle\delta F_1(t)\delta F_2(t + \tau)\rangle/(\langle F_1\rangle\langle F_2\rangle)$ is nonzero only if particles carrying both labels move together. For a sample with $N_1$, $N_2$ and $N_{12}$ molecules of the single-labeled and double-labeled species in the volume, $G_\times(0) = N_{12}/[(N_1 + N_{12})(N_2 + N_{12})]$ (for perfectly overlapping volumes), and the bound fraction, hence the dissociation constant, follows without any separation step. FCCS has measured protein interactions and enzyme cleavage in solution and in living cells.

### 12.6.4. FCS in Membranes and Cells

In a membrane, diffusion is two-dimensional and $G(\tau) = \langle N\rangle^{-1}(1 + \tau/\tau_{\mathrm{D}})^{-1}$. Varying the size of the observation spot tests the mode of diffusion: for free diffusion $\tau_{\mathrm{D}}$ is proportional to $w_0^2$ with zero intercept; diffusion hindered by a meshwork of barriers gives a negative intercept, and partitioning into small domains a positive one (the FCS diffusion law of Wawrezinieck and colleagues, 2005). In cells FCS measures absolute concentrations of fluorescent-protein fusions in the nanomolar range, their mobility and their binding to immobile structures, provided photobleaching is minimized: a molecule that bleaches during its passage shortens the apparent $\tau_{\mathrm{D}}$ and depletes the reservoir. Scanning FCS, raster image correlation spectroscopy and number-and-brightness analysis extend the approach to images, and the brightness of each diffusing particle reports its oligomeric state.

## 12.7. Nanopores

### 12.7.1. Ionic Current through a Pore

A nanopore is a hole of nanometer diameter in an insulating membrane separating two salt solutions. A voltage across the membrane drives an ionic current through the pore, and a molecule that enters the pore blocks part of it.

**Definition 12.7.1 (Nanopore)** A **nanopore** sensor is a pore of diameter about $1$–$20\,\mathrm{nm}$, either a protein pore inserted into a lipid or polymer membrane (biological nanopore: α-hemolysin, MspA, CsgG, aerolysin) or a hole drilled in a thin solid membrane (solid-state nanopore: silicon nitride, graphene, molybdenum disulfide), through which molecules are detected one at a time by the change of the ionic current as they pass.

**Formula 12.7.1 (Conductance of a Cylindrical Pore)** In a solution of conductivity $\sigma$, a cylindrical pore of diameter $d$ and length $L$ has the conductance

$$
G = \sigma\left[\frac{4L}{\pi d^2} + \frac{1}{d}\right]^{-1},
$$
the first term being the resistance of the channel and the second the access resistance of the two hemispherical regions in which the current converges onto the entrance and spreads from the exit (each $1/(2\sigma d)$, Hall 1975).

**Example 12.7.1** In $1\,\mathrm{M}$ $\ce{KCl}$ ($\sigma \approx 11\,\mathrm{S\,m^{-1}}$) a pore with $d = 4\,\mathrm{nm}$ and $L = 10\,\mathrm{nm}$ has a channel resistance of $4L/(\pi d^2\sigma) = 72\,\mathrm{M\Omega}$ and an access resistance of $1/(d\sigma) = 23\,\mathrm{M\Omega}$, so $G = 10.5\,\mathrm{nS}$ and $3.2\,\mathrm{nA}$ flow at $300\,\mathrm{mV}$. α-Hemolysin, with a constriction of $1.4\,\mathrm{nm}$, conducts about $1\,\mathrm{nS}$ ($100$–$120\,\mathrm{pA}$ at $120\,\mathrm{mV}$). A double-stranded DNA of diameter $2.2\,\mathrm{nm}$ in the $4\,\mathrm{nm}$ pore removes a fraction of about $(2.2/4)^2 = 0.30$ of the channel cross-section; with the access resistance unchanged the current drops by about $23\,\%$.

The simple model describes high salt concentrations, where the current is carried by the bulk electrolyte. At low salt the surface charge of the pore and of the DNA dominate: the counterions of the DNA can carry more current than the ions they displace, and translocation then increases the current. Pores are also not passive cylinders: protein pores have charged constrictions and asymmetric shapes that select ions and orient molecules, and their current is rectified.

### 12.7.2. Capture and Translocation

A charged molecule far from the pore diffuses freely; close to it, the electric field that funnels the current into the pore also pulls the molecule in. In the access region the field falls off as $1/r^2$, like the current density spreading from a point, so electrophoretic drift with mobility $\mu_{\mathrm{e}}$ overcomes diffusion within a capture radius.

**Proposition 12.7.1 (Diffusion-Limited Capture)** For a pore with the access field $E(r) = I/(2\pi\sigma r^2)$ (hemispherical spreading of the current $I$), the radius at which the drift time equals the diffusion time, $r^* = d^2\mu_{\mathrm{e}}V/(8LD)$ (for a pore whose resistance is dominated by the channel), defines a hemispherical absorbing surface, and the capture rate at concentration $c$ is the diffusion-limited flux to it,

$$
R = 2\pi Dr^*c = \frac{\pi c\,d^2\mu_{\mathrm{e}}V}{4L},
$$
proportional to the voltage and the concentration and independent of the diffusion coefficient (Wanunu and colleagues, 2010).

The independence of $D$ means that long and short DNA molecules are captured at the same rate per molecule in this regime. With $d = 4\,\mathrm{nm}$, $L = 10\,\mathrm{nm}$, $\mu_{\mathrm{e}} = 3.2\times10^{-8}\,\mathrm{m^2\,V^{-1}\,s^{-1}}$ and $V = 300\,\mathrm{mV}$, $R \approx 7$ events per second per nanomolar DNA. Capture can be increased by a salt gradient across the pore, which strengthens the field on the capture side. Short molecules and weakly charged ones face an entropic or energetic barrier at the pore entrance, and their capture rate rises exponentially with voltage (a barrier-limited regime, Kramers' theory of [7.6.5](/7.6.5#thm-5.6.2)).

Once inside, a polymer translocates under the electric force on its charges, opposed by friction and by fluctuations. In the simplest model, the position $x$ of the molecule relative to the pore performs a one-dimensional biased random walk with velocity $v$ and diffusion coefficient $D_{\mathrm{t}}$, and the translocation time is the **first-passage time** to $x = l$ for a molecule of length $l$.

**Formula 12.7.2 (Translocation Time Distribution)** For drift–diffusion started at $x = 0$, the first-passage time to $x = l$ has the inverse Gaussian density

$$
f(t) = \frac{l}{\sqrt{4\pi D_{\mathrm{t}}t^3}}\exp\left[-\frac{(l - vt)^2}{4D_{\mathrm{t}}t}\right], \qquad \langle t\rangle = \frac{l}{v}, \qquad \operatorname{Var}(t) = \frac{2D_{\mathrm{t}}l}{v^3},
$$
with relative width $\sqrt{2/\mathrm{Pe}}$, where $\mathrm{Pe} = vl/D_{\mathrm{t}}$ is the **Péclet number** of the translocation.

![Translocation of DNA through a solid-state nanopore (model: 4 nm × 10 nm pore in 1 M KCl, 5 kbp dsDNA). A: ionic current at 300 mV and 10 nM DNA: a 3.2 nA open-pore current interrupted by short blockades of about 23 % (sampled every 10 µs, with noise); overlapping events give deeper spikes. B: scatter plot of relative blockade against dwell time at 200 and 400 mV: the depth reflects the cross-section of the molecule, the dwell time its length and the driving force. C: dwell-time histogram at 300 mV with the inverse-Gaussian first-passage density (Péclet number 20); inset: the capture rate rises linearly with voltage, as predicted for diffusion-limited capture](./plots/nanopore-events.py)

Measured dwell times of dsDNA in solid-state pores scale with length somewhat faster than linearly ($t \propto N^{1.2}$–$N^{1.4}$), because the part of the coil outside the pore must be dragged along, and they are short: about $0.01$–$0.1\,\mu\mathrm{s}$ per base pair at a few hundred millivolts in thin pores. Single-stranded DNA moves through α-hemolysin at $1$–$20\,\mu\mathrm{s}$ per nucleotide. Both are far too fast to resolve individual bases with the current noise of a $1$–$10\,\mathrm{kHz}$ bandwidth, a central obstacle that sequencing solved with motor enzymes.

### 12.7.3. Nanopore Sequencing and Molecular Sensing

The idea of reading the bases of a single DNA strand from the current through a pore was proposed by Deamer, Branton, Church and Kasianowicz around 1989–1996. Three advances made **nanopore sequencing** practical ([7.2.6](/7.2.6)). A motor enzyme (a DNA polymerase or a helicase) bound to the top of the pore ratchets the strand through it one nucleotide at a time, at a few hundred nucleotides per second instead of a million, so that each position produces a current plateau lasting milliseconds. Engineered pores with a short, narrow constriction (MspA, CsgG) concentrate the sensitivity on a few nucleotides. Because the current of a plateau depends on the $k$-mer of about $3$–$6$ nucleotides in the constriction, not on a single base, the sequence is decoded from the series of current levels by a basecaller, now a recurrent or transformer neural network trained on known sequences. Homopolymer runs are difficult, because successive plateaus are identical and only their total duration reveals the length; pores with two constrictions (CsgG with its partner CsgF) and improved motors have reduced these errors. Single reads exceed a million bases, accuracies above $99\,\%$ per read have been reached, and base modifications such as 5-methylcytosine are read directly from the current.

Beyond sequencing, nanopores detect and characterize single proteins, folded or unfolded, and their complexes; peptides and amino acids with engineered pores, a step towards protein sequencing; small molecules bound to adapters inside the pore; and the forces needed to unzip DNA hairpins or unfold proteins pulled through the pore by the electric field, a form of single-molecule force spectroscopy without tethers ([7.6.17](/7.6.17)). The biological original of the method is the patch-clamp recording of single ion channels ([7.6.30](/7.6.30)), and natural nanopores, pore-forming toxins and protein translocases, are themselves objects of biophysics.

## 12.8. The Single-Molecule Toolbox

| Method | Signal | Spatial precision | Time resolution | Concentration | Typical questions |
|---|---|---|---|---|---|
| Patch clamp ([7.6.30](/7.6.30)) | current through one channel | — | $10\,\mu\mathrm{s}$ | — | gating kinetics, conductance |
| TIRF imaging | presence, intensity of spots | diffraction-limited spots; nm by fitting | $1$–$100\,\mathrm{ms}$ | pM–nM labeled ligand | binding, assembly order, stoichiometry by bleaching |
| FIONA, SPT | position of one emitter | $1$–$20\,\mathrm{nm}$ | ms | low labeling density | motor steps, diffusion modes |
| MINFLUX | position of one emitter | $1$–$3\,\mathrm{nm}$ | $< 1\,\mathrm{ms}$ | sparse emitters | substeps of motors, nanoscale structure |
| SMLM, STED | images | $10$–$50\,\mathrm{nm}$ | s–min per image | dense labeling | nanoscale organization of cells |
| smFRET, TIRF | distance within one molecule | $\approx 0.1$–$0.5\,\mathrm{nm}$ changes at $3$–$8\,\mathrm{nm}$ | $1$–$100\,\mathrm{ms}$, minutes of record | immobilized | conformational dynamics, kinetics |
| smFRET, confocal bursts | distance distributions | as above | ns–ms within bursts | $50$–$100\,\mathrm{pM}$ | heterogeneity, folding, disordered proteins |
| FCS, FCCS | intensity fluctuations | — (ensemble of few) | $\mu\mathrm{s}$–$\mathrm{s}$ | $0.1$–$100\,\mathrm{nM}$ | concentration, diffusion, binding in cells |
| Nanopores | ionic current blockade | sub-nm in constriction | $\mu\mathrm{s}$–ms | pM–nM | sequencing, sizing, unfolding |
| Force spectroscopy ([7.6.17](/7.6.17)) | extension, force | $0.1$–$1\,\mathrm{nm}$ | $\mu\mathrm{s}$–ms | tethered | mechanics, motors, unfolding |

The methods share their logic and their limits. Each measures a quantity that depends on the state of one molecule, collects a finite number of photons or charges, and must separate the signal of the molecule from noise and background; each turns trajectories into states and rates with the same statistics of dwell times and hidden Markov models. Their combinations, fluorescence with force, FRET with tracking, nanopores with fluorescence, are the frontier of the field, and the stochastic kinetics they reveal are the subject of [7.6.32](/7.6.32).

## Summary

Single molecules and photons (12.1):

- Single molecules show discrete states, random dwell times, heterogeneity and equilibrium fluctuations; a single-step exit gives an exponential dwell distribution with $\hat k = n/\sum t_i$, two hidden steps give a rising and falling density (Proposition 12.1.1; Example 12.1.1).
- Excitation $k_{\mathrm{ex}} = \sigma I/h\nu$, saturation at $I_{\mathrm{s}} = h\nu/\sigma\tau$ (Formula 12.1.1); a dye emits $\Phi/\Phi_{\mathrm{b}} \approx 10^5$–$10^6$ photons before bleaching; background is minimized by small volumes (confocal, TIRF, zero-mode waveguides).

Optics (12.2):

- Image = object $*$ PSF (Definition 12.2.1); Airy PSF, Gaussian width $s \approx 0.21\lambda/\mathrm{NA}$, Rayleigh $0.61\lambda/\mathrm{NA}$, OTF cutoff $2\mathrm{NA}/\lambda$ (Formula 12.2.1); Nyquist sampling at $\lambda/4\mathrm{NA}$.
- TIRF: evanescent intensity with depth $d = \lambda_0/(4\pi\sqrt{n_1^2\sin^2\theta - n_2^2}) \approx 60$–$200\,\mathrm{nm}$ (Formula 12.2.2); confocal volume $V_{\mathrm{eff}} = \pi^{3/2}w_0^2z_0 \approx 0.2$–$1\,\mathrm{fL}$.

Localization and super-resolution (12.3–12.4):

| Quantity | Result |
|---|---|
| Photon-limited localization | $\sigma_{\mathrm{loc}} \ge s/\sqrt N$, the Cramér–Rao bound (Theorem 12.3.1, Definition 12.3.1) |
| With pixels and background | $\sigma^2 \approx (s^2 + a^2/12)/N + 8\pi s^4b^2/(a^2N^2)$; MLE reaches the bound (Formula 12.3.1) |
| Tracking | $\mathrm{MSD} = 2dDt + 2d\sigma_{\mathrm{loc}}^2 - (2d/3)Dt_{\mathrm{E}}$ (Formula 12.3.2) |
| Counting | truncated $\mathrm{Bin}(n, p)$ of bleaching steps (Formula 12.3.3) |
| STED | $d = d_0/\sqrt{1 + I_{\max}/I_{\mathrm{s}}}$ (Proposition 12.4.1) |
| SMLM | $R \approx \sqrt{(2.355\sigma_{\mathrm{loc}})^2 + (2/\sqrt\rho)^2}$ |
| MINFLUX | $\sigma = L/(4\sqrt N)$ (Proposition 12.4.2) |
| SIM | at most twofold, $k_{\mathrm{c}} + k_{\mathrm{i}} \le 2k_{\mathrm{c}}$ |

FRET, FCS and nanopores (12.5–12.7):

- smFRET (Definition 12.5.1) needs leakage, direct-excitation and $\gamma$ corrections; histograms have the binomial shot-noise width $\sqrt{E(1 - E)/N}$ (Proposition 12.5.1), and excess width signals heterogeneity or dynamics; trajectories are analyzed with hidden Markov models (Algorithm 12.5.1).
- FCS (Definition 12.6.1): $G(\tau) = \langle N\rangle^{-1}(1 + \tau/\tau_{\mathrm{D}})^{-1}(1 + \tau/\omega^2\tau_{\mathrm{D}})^{-1/2}$, $\tau_{\mathrm{D}} = w_0^2/4D$ (Theorem 12.6.1); amplitude gives concentration, decay gives $D$; fast kinetics multiply $G$; FCCS measures binding.
- Nanopores (Definition 12.7.1): $G = \sigma[4L/\pi d^2 + 1/d]^{-1}$ (Formula 12.7.1); capture $R = \pi cd^2\mu_{\mathrm{e}}V/4L$ independent of $D$ (Proposition 12.7.1); dwell times are inverse-Gaussian first-passage times (Formula 12.7.2); sequencing needs a motor enzyme and $k$-mer decoding.

## Questions

1. Why does the photon-limited localization precision $s/\sqrt N$ not contradict the diffraction limit? What exactly does each of them limit?

   **Answer** The diffraction limit concerns the separation of two point sources that emit simultaneously: their images overlap, and the OTF transmits no spatial frequencies above $2\mathrm{NA}/\lambda$, so two emitters closer than about $\lambda/2\mathrm{NA}$ give an image indistinguishable from other close pairs or from a single extended source. Localization concerns the position of a single emitter known to be alone: each photon is a sample from a PSF of known shape, and the position estimate improves as $1/\sqrt N$ (Theorem 12.3.1). Super-resolution methods convert the first problem into the second by making nearby emitters emit at different times (SMLM) or in different states (STED).
2. A single molecule switches between conformations A and B. Dwell times in A follow a single exponential with mean $80\,\mathrm{ms}$, and dwell times in B have a mean of $200\,\mathrm{ms}$ and a standard deviation of $120\,\mathrm{ms}$. What can you infer?

   **Answer** Leaving A is a single rate-limiting step with $k_{\mathrm{AB}} = 12.5\,\mathrm{s^{-1}}$. For B the squared coefficient of variation is $(120/200)^2 = 0.36 < 1$, so leaving B involves at least $1/0.36 \approx 3$ sequential steps of comparable rates (the randomness parameter bounds the number of steps from below), hidden within the B signal: B is a set of substates connected irreversibly or nearly so, for example a series of conformational or chemical steps. A non-exponential, rising dwell-time distribution in a cycle also implies that the process is driven, since at equilibrium with detailed balance the observed transitions would still be reversible; the next steps are to fit the distribution with a gamma or sequential model and to vary conditions (substrate, force) to see which step changes.
3. Estimate the penetration depth of TIRF illumination at $640\,\mathrm{nm}$ through glass ($n_1 = 1.518$) into a cell ($n_2 = 1.38$) at $\theta = 68^\circ$, and explain why the angle must be larger for cells than for water.

   **Answer** $n_1^2\sin^2\theta = 2.304\times0.8597 = 1.981$ and $n_2^2 = 1.904$, so $\sqrt{0.0766} = 0.277$ and $d = 640/(4\pi\times0.277) = 184\,\mathrm{nm}$. The critical angle for $n_2 = 1.38$ is $\arcsin(1.38/1.518) = 65.4^\circ$, larger than $61.4^\circ$ for water, because the cytoplasm has a higher refractive index; at angles that would give total reflection against water, light may still enter a cell. A higher angle, close to the limit of an $\mathrm{NA} = 1.49$ objective, is needed for thin, well-defined excitation of the basal membrane.
4. In a localization experiment with $s = 110\,\mathrm{nm}$, pixels of $108\,\mathrm{nm}$ and a background of $9$ photons per pixel ($b = 3$), how many photons are needed for $\sigma_{\mathrm{loc}} = 5\,\mathrm{nm}$ according to Formula 12.3.1? What changes with an EMCCD camera?

   **Answer** With $s^2 + a^2/12 = 12\,100 + 972 = 13\,072\,\mathrm{nm^2}$ and $8\pi s^4b^2/a^2 = 25.13\times1.464\times10^8\times9/11\,664 = 2.84\times10^6\,\mathrm{nm^2}$, we need $13\,072/N + 2.84\times10^6/N^2 = 25$. Solving the quadratic $25N^2 - 13\,072N - 2.84\times10^6 = 0$ gives $N = [13\,072 + \sqrt{1.709\times10^8 + 2.84\times10^8}]/50 = (13\,072 + 21\,330)/50 \approx 690$ photons. The excess noise of electron multiplication effectively halves the number of photons, so about $1400$ detected photons are needed with an EMCCD (or a camera with lower noise is preferable at these signal levels).
5. Show that the doughnut-based MINFLUX precision $L/(4\sqrt N)$ is better than camera localization whenever $L < 4s$, and discuss what limits $L$ in practice.

   **Answer** Camera localization at best gives $s/\sqrt N$ (Theorem 12.3.1) and MINFLUX $L/(4\sqrt N)$ (Proposition 12.4.2), so MINFLUX is better for $L < 4s \approx 400\,\mathrm{nm}$; with $L = 50\,\mathrm{nm}$ the gain is a factor of $8$ in precision, or $64$ in photons. $L$ cannot be made arbitrarily small: the molecule must lie within the probed range, which requires a prior localization (hence the iterative scheme); background and an imperfect zero of the doughnut add photons that carry no position information, and their relative weight grows as $L$ shrinks because the signal near the zero is weak; finally, the dye's linker and orientation and mechanical drift limit the accuracy at about $1\,\mathrm{nm}$.
6. In confocal smFRET, bursts of $60$ photons are recorded from a protein. The histogram shows a peak at $E = 0.45$ with standard deviation $0.10$. Is the protein conformationally homogeneous?

   **Answer** The shot-noise width for $N = 60$ is $\sqrt{0.45\times0.55/60} = 0.064$. The measured $0.10$ is larger, so there is extra variance $0.10^2 - 0.064^2 = 0.0059$, a standard deviation of $0.077$ in $E$ beyond shot noise. Before concluding heterogeneity, instrumental contributions must be excluded: background, variation of $\gamma$ between molecules, acceptor blinking and photobleaching within bursts, and the distribution of burst sizes (which should be used in the prediction, not a single $N$). If the excess remains, the protein either has a distribution of static conformations or interconverts on the time scale of the burst ($\sim$ ms); burst-variance analysis, or recomputing $E$ in time windows of different length, distinguishes the two, because dynamic broadening decreases with shorter windows relative to the shot-noise expectation.
7. FCS of a GFP-tagged protein in the cytoplasm, with $w_0 = 0.22\,\mu\mathrm{m}$ and $\omega = 5$, gives $G(0) = 0.08$ and $\tau_{\mathrm{D}} = 1.1\,\mathrm{ms}$. Compute the concentration and the diffusion coefficient. Free GFP in the same cells gives $\tau_{\mathrm{D}} = 0.5\,\mathrm{ms}$. What do you conclude about the size of the complex?

   **Answer** $\langle N\rangle = 1/0.08 = 12.5$, $V_{\mathrm{eff}} = \pi^{3/2}\times0.0484\times1.1\,\mu\mathrm{m^3} = 0.30\,\mathrm{fL}$, so $c = 12.5/(0.30\times10^{-15}\times6.02\times10^{23})\,\mathrm{M} = 69\,\mathrm{nM}$. $D = w_0^2/(4\tau_{\mathrm{D}}) = 0.0484/(4\times1.1\times10^{-3}) = 11\,\mu\mathrm{m^2\,s^{-1}}$. The ratio of diffusion times is $2.2$, so the hydrodynamic radius of the tagged protein is about $2.2$ times that of GFP, and for globular particles its mass about $2.2^3 \approx 11$ times larger, roughly $300\,\mathrm{kDa}$, if the cytoplasmic viscosity affects both equally. This is a crude estimate: elongated molecules diffuse more slowly than spheres of the same mass, and transient binding to immobile structures also lengthens $\tau_{\mathrm{D}}$ (which would be revealed by a deviation from the one-component model or by varying $w_0$). Background autofluorescence, if present, would make the true concentration smaller than computed.
8. A $3\,\mathrm{nm}$ pore in a $20\,\mathrm{nm}$ silicon nitride membrane in $1\,\mathrm{M}$ $\ce{KCl}$ ($11\,\mathrm{S\,m^{-1}}$) is used at $200\,\mathrm{mV}$. Compute the open-pore current, the expected blockade by dsDNA, and the capture rate at $5\,\mathrm{nM}$ DNA ($\mu_{\mathrm{e}} = 3.2\times10^{-8}\,\mathrm{m^2\,V^{-1}\,s^{-1}}$).

   **Answer** Channel resistance $4L/(\pi d^2\sigma) = 8\times10^{-8}/(\pi\times9\times10^{-18}\times11) = 257\,\mathrm{M\Omega}$; access resistance $1/(d\sigma) = 30\,\mathrm{M\Omega}$; $G = 1/(287\,\mathrm{M\Omega}) = 3.5\,\mathrm{nS}$, and $I = 0.70\,\mathrm{nA}$. DNA blocks a fraction $(2.2/3)^2 = 0.54$ of the channel cross-section; the channel resistance rises to $257/(1 - 0.54) = 560\,\mathrm{M\Omega}$ and the current falls to $0.2/(590\times10^6) = 0.34\,\mathrm{nA}$, a blockade of about $50\,\%$ (the simple model is crude for a pore barely wider than the DNA). Capture rate $R = \pi cd^2\mu_{\mathrm{e}}V/(4L)$ with $c = 5\times6.02\times10^{17}\,\mathrm{m^{-3}}$: $\pi\times3.01\times10^{18}\times9\times10^{-18}\times3.2\times10^{-8}\times0.2/(8\times10^{-8}) = 6.8\,\mathrm{s^{-1}}$.
9. Explain why the translocation of single-stranded DNA through α-hemolysin is too fast for sequencing, how motor enzymes solve the problem, and why homopolymers remain hard to read.

   **Answer** Under $100$–$200\,\mathrm{mV}$ ssDNA moves through α-hemolysin at about $1$–$20\,\mu\mathrm{s}$ per nucleotide, while resolving current levels that differ by a few picoamperes against noise requires averaging for milliseconds (the noise of a measurement of bandwidth $B$ grows roughly as $\sqrt B$ or faster). Moreover, the long β barrel of α-hemolysin holds about $10$ nucleotides, so each current level reflects many bases. A motor enzyme (polymerase or helicase) on the pore controls the DNA and advances it one nucleotide per catalytic step, at a few hundred nucleotides per second, so that each $k$-mer produces a plateau of milliseconds, while a short constriction (MspA, CsgG) limits the $k$-mer to a few nucleotides. In a homopolymer run successive $k$-mers are identical and so are their currents; the run length must be inferred from the total duration of the plateau, which is stochastic (enzyme steps have exponential dwell times, Proposition 12.1.1), so insertions and deletions in homopolymers are the main error mode, reduced by pores with two reading heads and better models of the dwell times.
10. (Open) Design a single-molecule experiment to test whether a transcription factor finds its site on DNA by sliding along the DNA ([7.2.22](/7.2.22)). Which method, labels, geometry and analysis would you use, and what observations would distinguish sliding from three-dimensional diffusion alone?

    **Answer** One approach stretches long DNA molecules (λ-DNA, $48.5\,\mathrm{kbp}$) between two surface-attached points or along a lipid-coated surface by flow ("DNA curtains") and images a dye- or quantum-dot-labeled transcription factor by TIRF at frame rates of $10$–$100\,\mathrm{Hz}$. Each binding event gives a trajectory along the DNA: sliding appears as one-dimensional diffusion with an MSD linear in time (Formula 12.3.2, with localization error and motion blur corrected), a diffusion coefficient that can be compared with the rotation-coupled sliding prediction for a protein tracking the helix, and residence times whose distribution gives the dissociation rate. The sliding length $\sqrt{2D_1\tau}$ follows from $D_1$ and the mean residence time. Controls: salt dependence (sliding residence times shorten with ionic strength), a nonbinding mutant, and a target site at a known position to measure the fraction of arrivals that come from sliding versus direct binding from solution. Alternative methods are smFRET between a labeled protein and DNA (repeated FRET bursts as the protein slides past the acceptor) and single-particle tracking in live cells with photoactivatable labels, where the fraction of time bound nonspecifically and the search time can be compared with facilitated-diffusion theory.
