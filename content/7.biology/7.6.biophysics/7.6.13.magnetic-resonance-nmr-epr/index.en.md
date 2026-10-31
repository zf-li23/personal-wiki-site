---
title: "Magnetic Resonance: Spin Physics, Structure and Dynamics by NMR, and EPR"
description: Magnetic resonance of biological macromolecules. Nuclear spins, Zeeman levels, Larmor frequency, polarization and sensitivity; the Bloch equations, the rotating frame, pulses, T1, T2, the FID and the spin echo; relaxation by molecular motion, correlation functions and spectral densities, BPP theory, 15N relaxation and TROSY; chemical shifts and couplings of proteins and nucleic acids, the density operator and product operators, HSQC and multidimensional spectra, resonance assignment and chemical-shift perturbation; NOE, J couplings, chemical shifts, residual dipolar couplings, PRE and PCS as restraints and structure calculation by simulated annealing; chemical exchange and the Bloch-McConnell equations, model-free analysis and the order parameter, relaxation dispersion, CEST and ZZ exchange, hydrogen-deuterium exchange with EX1 and EX2; EPR, site-directed spin labeling, nitroxide spectra and DEER distance measurements; dynamic nuclear polarization; MRI.
---

Nuclear magnetic resonance (NMR) is the only one of the three high-resolution methods of structural biology that works on molecules in solution, at room temperature, and records not a picture but a set of numbers about pairs of atoms: which nuclei are bonded, which are close in space, how bonds are oriented, how fast each part of the molecule moves and how often it visits other conformations. The structure is computed from these numbers. The price is a steep learning curve and a size limit; the reward is a direct view of flexibility, transient states, weak binding and disordered proteins, which crystallography ([7.6.10](/7.6.10)) and **cryo-electron microscopy** ([7.6.14](/7.6.14)) see poorly or not at all. Electron paramagnetic resonance (EPR) applies the same physics to unpaired electrons and, with spin labels, measures distances of several nanometers in molecules of any size.

The principles of NMR as an analytical method (nuclear spin, the resonance condition, chemical shift, coupling constants and the $n + 1$ rule, the spectrometer, two-dimensional spectra and MRI) are treated in [6.4.12](/6.4.12), and the EPR spectra of organic radicals in [6.5.7](/6.5.7#sec-7.4); they are not repeated here. This chapter follows the physics further, in the direction needed for macromolecules. The spin system is first described classically: the magnetization obeys the Bloch equations, which explain pulses, free induction decay, relaxation and echoes (13.1–13.2). Relaxation is then connected to molecular motion through correlation functions and spectral densities; this explains why NMR becomes difficult for large molecules and how TROSY and deuteration push the limit (13.3). The quantum description by the density operator explains the pulse sequences of multidimensional spectra, with which the signals of a protein are resolved and assigned (13.4). Distances, angles and orientations measured from NOEs, couplings, chemical shifts, residual dipolar couplings and paramagnetic effects become the restraints of a structure calculation (13.5). Relaxation, chemical exchange and hydrogen exchange report motions from picoseconds to months (13.6). EPR, site-directed spin labeling and DEER follow (13.7), and the chapter ends with magnetic resonance imaging, the medical application of the same equations (13.8), and a comparison of the methods (13.9). The rotational diffusion that drives relaxation was treated in [7.6.5](/7.6.5#sec-5.3.2); the two-state kinetics behind chemical exchange in [7.6.3](/7.6.3) and [7.6.4](/7.6.4); the restraint-driven structure calculation uses the **simulated annealing** of [7.6.9](/7.6.9#alg-9.11.1), and the folding and dynamics that NMR measures are the subject of [7.6.16](/7.6.16).

## 13.1. Nuclear Spins in a Magnetic Field

### 13.1.1. A Short History

The history of magnetic resonance is a sequence of physics experiments that turned into a chemical and then a biological method:

| Year | Event |
|---|---|
| 1922 | Stern and Gerlach: space quantization of angular momentum in an atomic beam ([5.5.4](/5.5.4#sec-4.2.2)); in 1933 Stern measures the magnetic moment of the proton |
| 1938 | Rabi: nuclear magnetic resonance in a molecular beam with a radiofrequency field |
| 1944 | Zavoisky: electron paramagnetic resonance in $\ce{CuCl2.2H2O}$ |
| 1946 | Bloch (water) and Purcell (paraffin): NMR in bulk matter |
| 1948 | Bloembergen, Purcell and Pound: relaxation theory (BPP) |
| 1950 | Proctor and Yu: chemical shift (two $^{14}\mathrm{N}$ lines of $\ce{NH4NO3}$); Hahn: the spin echo |
| 1951 | Gutowsky and McCall, Ramsey and Purcell: scalar coupling through bonds |
| 1953–1955 | Overhauser: polarization transfer from electrons to nuclei; Solomon: equations of cross-relaxation |
| 1966 | Ernst and Anderson: pulsed Fourier-transform NMR |
| 1971–1976 | Jeener proposes, Ernst realizes two-dimensional NMR (COSY) |
| 1973 | Lauterbur and Mansfield: imaging with field gradients |
| 1985 | Wüthrich and coworkers: first protein structure in solution from NOE distance restraints |
| 1990s | $^{13}\mathrm{C}/^{15}\mathrm{N}$ labeling, triple-resonance spectra, residual dipolar couplings (1995–1997), TROSY (1997) |
| 2000s | pulsed EPR distance measurements (DEER) in structural biology; dynamic nuclear polarization; relaxation dispersion and CEST for invisible states |

Nobel prizes went to Stern (1943), Rabi (1944), Bloch and Purcell (1952), Ernst (1991), Wüthrich (2002, chemistry) and Lauterbur and Mansfield (2003, physiology or medicine).

### 13.1.2. Nuclear Spin and Magnetic Moment

A nucleus has an intrinsic angular momentum $\boldsymbol{I}$, of magnitude $\hbar\sqrt{I(I + 1)}$, with the **nuclear spin quantum number** $I$ an integer or half-integer, and $z$ component $m\hbar$ with $m = -I, \dots, I$ ([6.4.12](/6.4.12#def-12.1.1)). Its magnetic moment is parallel or antiparallel to it,

$$
\boldsymbol{\mu} = \gamma\boldsymbol{I}, \tag{13.1}
$$
with the **gyromagnetic ratio** $\gamma$ a property of the nucleus. The rule for $I$ follows from the pairing of nucleons: if the numbers of protons and neutrons are both even, $I = 0$ ($^{12}\mathrm{C}$, $^{16}\mathrm{O}$, $^{32}\mathrm{S}$), and the nucleus is invisible to NMR; if both are odd, $I$ is a nonzero integer ($^2\mathrm{H}$, $^{14}\mathrm{N}$); if the mass number is odd, $I$ is half-integral. The value itself is not predicted by this rule and must be looked up.

| Nucleus | $I$ | $\gamma/(10^7\,\mathrm{rad\,s^{-1}\,T^{-1}})$ | $\lvert\nu_0\rvert$ at $14.1\,\mathrm{T}$ / MHz | Natural abundance / % | Use in biomolecular NMR |
|---|---|---|---|---|---|
| $^1\mathrm{H}$ | 1/2 | 26.752 | 600.0 | 99.99 | detection in almost all experiments |
| $^2\mathrm{H}$ | 1 | 4.107 | 92.1 | 0.012 | deuteration to slow relaxation; solvent lock |
| $^{13}\mathrm{C}$ | 1/2 | 6.728 | 150.9 | 1.07 | uniform labeling |
| $^{14}\mathrm{N}$ | 1 | 1.934 | 43.4 | 99.63 | quadrupolar, broad lines; avoided |
| $^{15}\mathrm{N}$ | 1/2 | −2.713 | 60.8 | 0.37 | uniform labeling; backbone amides |
| $^{17}\mathrm{O}$ | 5/2 | −3.628 | 81.4 | 0.038 | quadrupolar, rarely used |
| $^{19}\mathrm{F}$ | 1/2 | 25.18 | 564.7 | 100 | site-specific probe (13.3.5) |
| $^{31}\mathrm{P}$ | 1/2 | 10.84 | 243.1 | 100 | nucleic acid backbone, phospholipids, metabolites |

Nuclei with $I \ge 1$ have an electric quadrupole moment, which couples to electric-field gradients and relaxes them quickly; their lines are broad. Biomolecular NMR therefore uses spin-1/2 nuclei, and since $^{12}\mathrm{C}$, $^{14}\mathrm{N}$ and $^{16}\mathrm{O}$ are useless, proteins and nucleic acids are expressed in media containing $^{13}\mathrm{C}$-glucose and $^{15}\mathrm{NH_4Cl}$ as the sole carbon and nitrogen sources. The negative $\gamma$ of $^{15}\mathrm{N}$ (its moment is antiparallel to its spin) flips several signs below, and the proton's $\gamma$, the largest of all stable nuclei except tritium, is why NMR is detected on $^1\mathrm{H}$ whenever possible.

### 13.1.3. Zeeman Levels and the Larmor Frequency

In a static field $\boldsymbol{B}_0 = B_0\boldsymbol{e}_z$ the energy $-\boldsymbol{\mu}\cdot\boldsymbol{B}_0$ splits the $2I + 1$ states (the nuclear **Zeeman effect**):

$$
E_m = -\gamma\hbar B_0 m, \qquad \Delta E = E_{m-1} - E_m = \hbar\lvert\gamma\rvert B_0 . \tag{13.2}
$$

**Definition 13.1.1 (Larmor Frequency)** The *Larmor frequency* of a nucleus in the field $B_0$ is $\omega_0 = -\gamma B_0$ (angular frequency; $\nu_0 = \omega_0/2\pi$). Its magnitude is the frequency of the photon absorbed or emitted in a transition $\Delta m = \pm 1$, and, as Theorem 13.2.1 shows, it is also the angular velocity with which a magnetic moment precesses about the field; the sign gives the sense of the precession.

For a spin-1/2 nucleus with $\gamma > 0$ the state $m = +\frac12$ (spin up, $\alpha$) is the lower one. Spectrometers are named by the proton frequency: a "600 MHz" magnet has $B_0 = 2\pi\times600\,\mathrm{MHz}/\gamma_{\mathrm{H}} = 14.1\,\mathrm{T}$, a field produced by a superconducting coil in liquid helium and about $3\times10^5$ times the Earth's field ($50\,\mu\mathrm{T}$). In the same magnet $^{13}\mathrm{C}$ resonates at $150.9\,\mathrm{MHz}$ and $^{15}\mathrm{N}$ at $60.8\,\mathrm{MHz}$. The photon energy is minute: $h\nu = 4.0\times10^{-25}\,\mathrm{J} = 2.5\,\mu\mathrm{eV}$, or $10^{-4}\,k_{\mathrm{B}}T$ at room temperature ([7.6.6](/7.6.6)). A classical image is the **Larmor precession** of a magnetic moment in a field ([5.3.8](/5.3.8#sec-8.2.5)): the two pictures, quantum transitions between levels and classical precession of a vector, are reconciled in 13.2.

### 13.1.4. Polarization, Magnetization and Sensitivity

Since $\Delta E \ll k_{\mathrm{B}}T$, the **Boltzmann distribution** leaves the two levels almost equally populated:

$$
\frac{N_\alpha - N_\beta}{N_\alpha + N_\beta} = \tanh\frac{\hbar\gamma B_0}{2k_{\mathrm{B}}T} \approx \frac{\hbar\gamma B_0}{2k_{\mathrm{B}}T}. \tag{13.3}
$$

At $14.1\,\mathrm{T}$ and $298\,\mathrm{K}$ the polarization of protons is $4.8\times10^{-5}$: of every $10^5$ protons, $2.4$ more point with the field than against it, and only this excess gives a signal. Summing the moments of $N$ spins per unit volume gives the equilibrium **magnetization**,

**Formula 13.1.1 (Curie Law for Nuclear Magnetization)**

$$
M_0 = \frac{N\gamma^2\hbar^2 I(I + 1)}{3k_{\mathrm{B}}T}B_0, \qquad M_0 = \frac{N\gamma^2\hbar^2B_0}{4k_{\mathrm{B}}T}\quad\left(I = \tfrac12\right). \tag{13.4}
$$
It is proportional to $\gamma^2$ (polarization $\propto\gamma$, moment per spin $\propto\gamma$) and to $B_0/T$.

The voltage induced in the receiver coil is proportional to $\mathrm{d}M/\mathrm{d}t$, hence to $\omega_0M_0$, while the noise grows more slowly with frequency. A careful analysis gives the signal-to-noise ratio of an experiment that excites one nucleus and detects another,

$$
\frac{S}{N} \propto N\,\gamma_{\mathrm{exc}}\,\gamma_{\mathrm{det}}^{3/2}\,B_0^{3/2}\sqrt{n_{\mathrm{s}}}, \tag{13.5}
$$
where $n_{\mathrm{s}}$ is the number of scans. Three consequences shape every experiment. Excitation and detection on $^1\mathrm{H}$ gain a factor $(\gamma_{\mathrm{H}}/\gamma_{\mathrm{N}})^{5/2} \approx 300$ over direct $^{15}\mathrm{N}$ detection, so polarization is transferred from protons to the heteronucleus and back (13.4.4). The signal grows only as the square root of measuring time: doubling $S/N$ costs four times as long. And a protein sample must be concentrated: typically $0.1$–$1\,\mathrm{mM}$ in $0.3$–$0.5\,\mathrm{mL}$, milligrams of labeled protein. Cryogenically cooled probes (coil and preamplifier near $20\,\mathrm{K}$) gain a factor of three to four; higher fields gain $B_0^{3/2}$; and hyperpolarization by dynamic nuclear polarization (13.7.5) can raise the polarization itself by two orders of magnitude.

## 13.2. The Bloch Equations

### 13.2.1. Precession of the Magnetization

A macroscopic sample contains about $10^{20}$ spins, and what is manipulated and detected is their sum, the magnetization $\boldsymbol{M}$. For non-interacting spins, the expectation value of each spin obeys the classical equation of a magnetic moment in a field, because the torque $\boldsymbol{\mu}\times\boldsymbol{B}$ changes the angular momentum: $\mathrm{d}\boldsymbol{I}/\mathrm{d}t = \boldsymbol{\mu}\times\boldsymbol{B}$. Multiplying by $\gamma$ and summing over a unit volume:

**Theorem 13.2.1 (Precession of the Magnetization)** In a field $\boldsymbol{B}(t)$, and in the absence of relaxation,

$$
\frac{\mathrm{d}\boldsymbol{M}}{\mathrm{d}t} = \gamma\,\boldsymbol{M}\times\boldsymbol{B}. \tag{13.6}
$$
In a static field $B_0\boldsymbol{e}_z$, $M_z$ is constant and the transverse components rotate: $M_x + \mathrm{i}M_y = (M_x + \mathrm{i}M_y)_0\,\mathrm{e}^{\mathrm{i}\omega_0t}$ with $\omega_0 = -\gamma B_0$. The magnetization precesses about the field at the Larmor frequency, clockwise when seen from $+z$ if $\gamma > 0$.

**Proof** With $\boldsymbol{B} = B_0\boldsymbol{e}_z$, Eq. (13.6) gives $\dot M_x = \gamma B_0M_y$, $\dot M_y = -\gamma B_0M_x$, $\dot M_z = 0$. For $m = M_x + \mathrm{i}M_y$, $\dot m = \gamma B_0(M_y - \mathrm{i}M_x) = -\mathrm{i}\gamma B_0m$, whose solution is $m(0)\mathrm{e}^{-\mathrm{i}\gamma B_0t} = m(0)\mathrm{e}^{\mathrm{i}\omega_0t}$. $\square$

The quantum and classical descriptions agree: a spin in a superposition $c_\alpha|\alpha\rangle + c_\beta|\beta\rangle$ has a transverse expectation value that rotates at the frequency $\Delta E/\hbar$, the frequency of the photon in Eq. (13.2). In equilibrium the phases of the individual spins are random, so the transverse components cancel and $\boldsymbol{M} = M_0\boldsymbol{e}_z$, with nothing to precess. Spins are not "parallel or antiparallel" to the field in a literal sense; each spin is in some superposition, and the populations of Eq. (13.3) describe the statistics of a measurement of $I_z$.

### 13.2.2. The Rotating Frame and Radiofrequency Pulses

To turn $\boldsymbol{M}$ away from $z$, a radiofrequency coil produces a field $2B_1\cos(\omega t)\boldsymbol{e}_x$ perpendicular to $\boldsymbol{B}_0$, with $B_1$ of order $10^{-4}$ of $B_0$. A static transverse field would be useless: it would tilt $\boldsymbol{M}$ only while the precessing vector happens to point one way and tilt it back half a period later. The linear oscillating field is the sum of two components of amplitude $B_1$ rotating in opposite senses about $z$; the one rotating with the spins acts, the other is far off resonance and is negligible. Everything becomes simple in a coordinate frame rotating about $z$ at the frequency of the radiofrequency.

**Definition 13.2.1 (Rotating Frame)** The *rotating frame* is the coordinate system $(x', y', z)$ that rotates about $\boldsymbol{B}_0$ at the transmitter frequency $\omega$. In it, the co-rotating radiofrequency component is a static field $B_1$ along $x'$, and the static field is reduced to the residual $\Delta B = B_0 + \omega/\gamma$, so that a spin with Larmor frequency $\omega_0$ precesses about the effective field

$$
\gamma\boldsymbol{B}_{\mathrm{eff}} = (\gamma B_1, 0, -\Omega), \qquad \Omega = \omega_0 - \omega , \tag{13.7}
$$
where $\Omega$ is the offset of the spin's frequency from the transmitter.

On resonance ($\Omega = 0$) the effective field is $B_1$ along $x'$, and $\boldsymbol{M}$ rotates in the $y'z$ plane at the nutation frequency $\omega_1 = \gamma B_1$. A pulse of duration $t_{\mathrm{p}}$ turns it through the flip angle $\beta = \gamma B_1t_{\mathrm{p}}$; a $90^\circ$ pulse ($\pi/2$) puts all of $M_0$ in the transverse plane, a $180^\circ$ pulse ($\pi$) inverts it. With $\omega_1/2\pi = 25\,\mathrm{kHz}$, a $90^\circ$ pulse lasts $10\,\mu\mathrm{s}$. Off resonance the effective field is tilted out of the transverse plane by the angle $\arctan(\Omega/\omega_1)$, and the vector does not reach the transverse plane (Figure below, panel A): a pulse excites uniformly only spins whose offsets are small compared with $\omega_1$, which is why a "hard" pulse must be short and strong, while a long weak pulse excites a narrow band selectively (used for solvent suppression, CEST and slice selection in MRI). The rotating frame also gives the classical meaning of "resonance": only a field that rotates with the spins can turn them, exactly as only a push in phase with a swing builds up its motion. The quantum version of the same statement is that a radiofrequency field drives transitions $\alpha \leftrightarrow \beta$ equally in both directions. A long, weak irradiation therefore equalizes the populations and destroys the magnetization: *saturation*, the basis of solvent presaturation and of saturation-transfer experiments.

### 13.2.3. Relaxation

Eq. (13.6) conserves $\lvert\boldsymbol{M}\rvert$, but after a pulse the magnetization returns to equilibrium. Bloch added two phenomenological rates.

**Definition 13.2.2 (Bloch Equations)** The *Bloch equations* describe the magnetization of an ensemble of non-interacting spins:

$$
\frac{\mathrm{d}\boldsymbol{M}}{\mathrm{d}t} = \gamma\,\boldsymbol{M}\times\boldsymbol{B} - \frac{M_x\boldsymbol{e}_x + M_y\boldsymbol{e}_y}{T_2} - \frac{M_z - M_0}{T_1}\boldsymbol{e}_z . \tag{13.8}
$$
The time constant $T_1$ governs the recovery of $M_z$ towards $M_0$ (**longitudinal relaxation**, [6.4.12](/6.4.12#sec-12.1.5)), and $T_2$ the decay of the transverse magnetization (**transverse relaxation**); $R_1 = 1/T_1$ and $R_2 = 1/T_2$ are the relaxation rates.

After a $90^\circ$ pulse, and in the rotating frame, the solution is

$$
M_{x'} + \mathrm{i}M_{y'} = \mathrm{i}M_0\,\mathrm{e}^{\mathrm{i}\Omega t}\mathrm{e}^{-t/T_2}, \qquad M_z = M_0\left(1 - \mathrm{e}^{-t/T_1}\right). \tag{13.9}
$$

The two processes are physically different. Longitudinal relaxation changes the populations and exchanges energy with the surroundings (historically "the lattice", hence spin–lattice relaxation). Transverse relaxation is the loss of phase coherence among the spins: the transverse magnetization is the vector sum of many precessing moments, and anything that makes their phases diverge destroys it without necessarily changing energy. Transitions that change populations also destroy coherence, so $T_2 \le 2T_1$ always; for macromolecules $T_2 \ll T_1$. The name "spin–spin relaxation" for $T_2$ is historical and misleading: the mutual flip-flops of spins are one cause of dephasing, but transverse relaxation also includes every slow fluctuation of the local field (13.3). In the sample, an inhomogeneous static field adds a reversible dephasing, and the observed decay has the faster constant $T_2^*$, with $1/T_2^* = 1/T_2 + \gamma\Delta B_0/2$ approximately; the spin echo separates the two (13.2.5).

![Numerical solution of the Bloch equations in the rotating frame (convention dM/dt = γM × B with γ > 0, so a field along x′ turns M from z towards +y′). A: during a 90° pulse along x′ the magnetization of a spin on resonance nutates from z to the transverse plane (purple); a spin off resonance by Ω = 0.5 ω₁ precesses about a tilted effective field and misses the plane (orange). After the pulse, free precession at an offset with relaxation makes M spiral back to z (dashed). B: components of M after a 90° pulse for an offset of 5 Hz, T₂ = 0.1 s and T₁ = 0.3 s: the transverse components oscillate at Ω and decay with T₂; M_z recovers with T₁](./plots/bloch.py)

### 13.2.4. The Free Induction Decay and the Lorentzian Line

The precessing transverse magnetization induces a voltage in the coil: the **free induction decay** (FID, [6.4.12](/6.4.12#def-12.4.2)). The receiver mixes it with the transmitter frequency, which is the electronic equivalent of entering the rotating frame, and records two channels $90^\circ$ apart (quadrature detection), whose combination $s(t) = M_{x'} + \mathrm{i}M_{y'}$ distinguishes positive from negative offsets. For one line, $s(t) = s_0\mathrm{e}^{\mathrm{i}\Omega t - R_2t}$ for $t \ge 0$, and its **Fourier transform** is

$$
S(\omega) = \int_0^\infty s(t)\mathrm{e}^{-\mathrm{i}\omega t}\,\mathrm{d}t = s_0\frac{R_2 - \mathrm{i}(\omega - \Omega)}{R_2^2 + (\omega - \Omega)^2}. \tag{13.10}
$$

**Formula 13.2.1 (Lorentzian Line Shape)** The real part of Eq. (13.10), the absorption line, is a Lorentzian of full width at half height $2R_2$ in angular frequency, that is,

$$
\Delta\nu_{1/2} = \frac{R_2}{\pi} = \frac{1}{\pi T_2}, \tag{13.11}
$$
and its area, $\pi s_0$, does not depend on $T_2$. The imaginary part is the dispersion line, which is broader and changes sign at $\Omega$.

A line twice as broad is therefore half as high, and broadening costs signal as well as resolution. A Lorentzian normalized to unit area is the density of the **Cauchy distribution** ([3.1](/3.1)), with heavy tails: overlapping lines interfere far from their centers. In a spectrum of many lines, $s(t)$ is a sum of such terms; it is sampled at intervals $\Delta t$ (the spectral width is $1/\Delta t$, by the sampling theorem) for an acquisition time $t_{\mathrm{acq}}$ (the digital resolution is $1/t_{\mathrm{acq}}$), and transformed with the **fast Fourier transform** ([4.4](/4.4)). Before the transform the FID is usually multiplied by a window function: an exponential improves $S/N$ at the cost of width, a sine bell improves resolution at the cost of $S/N$. The phase of the spectrum must be corrected so that all lines are in pure absorption.

![Free induction decay and spectrum. A: quadrature-detected FID (real and imaginary channels) of two lines at offsets of 50 and 120 Hz with T₂ = 50 ms and 20 ms. B: real (absorption) and imaginary (dispersion) parts of its Fourier transform: Lorentzian lines of width 1/(πT₂) = 6.4 and 15.9 Hz with equal areas, so the broader line is lower. C: simulated amide region of the ¹H spectrum of folded proteins of 8, 25, 50 and 100 kDa at 600 MHz (one amide per 110 Da, shifts drawn at random around 8.2 ppm; τc = 0.5 ns per kDa; line widths from dipolar relaxation by the amide ¹⁵N and two nearby protons in a rigid molecule). The growth of the line width with size, together with the growth of the number of lines, makes the one-dimensional spectrum of large proteins unresolvable](./plots/fid.py)

### 13.2.5. The Spin Echo

In a field that is slightly different in different parts of the sample, spins precess at slightly different frequencies and fan out, and the FID decays faster than $T_2$. Hahn (1950) found that this decay is reversible.

**Definition 13.2.3 (Spin Echo)** A *spin echo* is the refocusing of transverse magnetization produced by a $180^\circ$ pulse applied at time $\tau$ after excitation: each spin's phase $\phi = \Omega\tau$ is changed into $\pi - \phi$ (for a pulse about $x'$, the transverse vector is reflected through the $x'z$ plane), and after a further time $\tau$ every spin, whatever its offset, arrives at the same phase. At $t = 2\tau$ the magnetization is refocused, reduced only by irreversible relaxation, $\mathrm{e}^{-2\tau/T_2}$.

The echo removes every interaction that is static during $2\tau$ and enters linearly in the frequency: field inhomogeneity, chemical-shift offsets and (for heteronuclear pairs, when only one spin is pulsed) scalar couplings. What it does not remove are random fluctuations faster than $\tau$, the true $T_2$, and slower processes that change a spin's frequency between the two halves of the echo, in particular chemical exchange (13.6.2). Varying $\tau$ and recording the echo amplitude measures $T_2$; a train of $180^\circ$ pulses spaced by $2\tau$, the Carr–Purcell–Meiboom–Gill (CPMG) sequence, measures it in one experiment with many echoes and suppresses the effect of pulse errors by applying the refocusing pulses along $y'$. The CPMG train is also the tool of relaxation dispersion (13.6.4). $T_1$ is measured by inversion recovery: a $180^\circ$ pulse inverts $M_z$, which recovers as $M_0(1 - 2\mathrm{e}^{-\tau/T_1})$, and a $90^\circ$ pulse after a variable delay $\tau$ reads it out.

![The Hahn spin echo, simulated with a Gaussian spread of offsets (s.d. 6 Hz) and a true T₂ of 0.15 s. A: transverse magnetization of 15 isochromats in the rotating frame just after the 90°ₓ pulse (all along +y′), at τ (fanned out), just after the 180°ₓ pulse (each vector reflected, so the fastest is now the furthest behind) and at 2τ (refocused along −y′). B: magnitude of the net transverse magnetization for τ = 60 ms: the FID decays with T₂*, the echo at 2τ recovers the signal up to the factor exp(−2τ/T₂), and echo maxima for other τ (dots) trace exp(−t/T₂)](./plots/spin-echo.py)

![Pulse sequences (schematic, not to scale; narrow bars 90° pulses, wide bars 180° pulses). A: inversion recovery for T₁ and the CPMG train for T₂ and relaxation dispersion, with ν_CPMG = 1/(4τ). B: the ¹H–¹⁵N HSQC: an INEPT transfer from ¹H to ¹⁵N, evolution of the ¹⁵N chemical shift during t₁ with a ¹H 180° pulse in its middle to remove the coupling, a reverse INEPT back to ¹H and acquisition during t₂ under ¹⁵N decoupling; the product-operator state at points 1–4 is written above (13.4.4). C: four-pulse DEER: observer pulses π/2–π–π at one microwave frequency generate a refocused echo, and a pump π pulse at a second frequency, stepped through the interval by the time t, inverts the partner spins and modulates the echo at the dipolar frequency (13.7.4)](./plots/pulse-sequences.py)

## 13.3. Relaxation and Molecular Motion

### 13.3.1. Fluctuating Local Fields

The Bloch equations treat $T_1$ and $T_2$ as given; relaxation theory computes them, and in doing so turns relaxation into a probe of motion. A nucleus in a molecule feels, besides $\boldsymbol{B}_0$, small local fields of molecular origin that depend on the orientation of the molecule:

- the dipolar field of a neighboring spin, which for a proton $0.18\,\mathrm{nm}$ away is about $0.5\,\mathrm{mT}$, varying as $(3\cos^2\theta - 1)/r^3$ with the angle $\theta$ between the internuclear vector and $\boldsymbol{B}_0$;
- the chemical-shift anisotropy (CSA): the shielding by the electrons ([6.4.12](/6.4.12#sec-12.2.1)) is a tensor, so the shift depends on the orientation of the molecule; for an amide $^{15}\mathrm{N}$ the anisotropy is about $-170\,\mathrm{ppm}$, with its unique axis nearly along the N–H bond, and its field grows with $B_0$;
- for quadrupolar nuclei, the electric quadrupole coupling; for paramagnetic samples, the field of unpaired electrons (13.5.4).

In solution the molecule tumbles and these fields average to zero: the average of $3\cos^2\theta - 1$ over the sphere vanishes, which is why a solution spectrum shows sharp lines with isotropic shifts and no dipolar splittings. But the fields fluctuate, and a fluctuating field with a component at the Larmor frequency drives transitions just as the radiofrequency field does, while its slow components randomize the precession phases. The rates therefore depend on how much of the fluctuation lies at each frequency.

### 13.3.2. Correlation Functions and the Spectral Density

Let $\boldsymbol{u}(t)$ be the unit vector along an internuclear bond. The relevant orientation function is $P_2(x) = (3x^2 - 1)/2$, the second of the **Legendre polynomials**, because the dipolar and CSA interactions are second-rank tensors.

**Definition 13.3.1 (Spectral Density Function)** The orientational correlation function of a bond vector is $C(t) = \langle P_2(\boldsymbol{u}(0)\cdot\boldsymbol{u}(t))\rangle$, averaged over the ensemble, with $C(0) = 1$. Its cosine transform,

$$
J(\omega) = \frac25\int_0^\infty C(t)\cos(\omega t)\,\mathrm{d}t , \tag{13.12}
$$
is the *spectral density function*: the power of the orientational fluctuations at angular frequency $\omega$ (the factor $2/5$ is a normalization of the spherical harmonics).

For a rigid molecule undergoing isotropic **rotational diffusion** with coefficient $D_{\mathrm{r}}$, the $P_2$ correlation function decays as $\mathrm{e}^{-6D_{\mathrm{r}}t}$ ([7.6.5](/7.6.5#def-5.3.1)), so with the *rotational correlation time* $\tau_{\mathrm{c}} = 1/(6D_{\mathrm{r}})$,

$$
C(t) = \mathrm{e}^{-t/\tau_{\mathrm{c}}}, \qquad J(\omega) = \frac25\,\frac{\tau_{\mathrm{c}}}{1 + \omega^2\tau_{\mathrm{c}}^2}, \qquad \tau_{\mathrm{c}} = \frac{4\pi\eta r_{\mathrm{h}}^3}{3k_{\mathrm{B}}T}, \tag{13.13}
$$
the last by the Stokes–Einstein–Debye relation for a sphere of hydrodynamic radius $r_{\mathrm{h}}$ (the rotational analogue of the **Stokes–Einstein equation**). The spectral density is flat, $J(\omega) \approx \frac25\tau_{\mathrm{c}}$, up to $\omega \approx 1/\tau_{\mathrm{c}}$ and falls as $\omega^{-2}$ beyond. A slower molecule has more power at low frequencies and less at high ones; the total, $\int_0^\infty J\,\mathrm{d}\omega = \pi/5$, is fixed.

**Example 13.3.1 (Correlation Times of Proteins)** Eq. (13.13) with a hydration shell of $0.3\,\mathrm{g}$ of water per gram gives about $0.37\,\mathrm{ns}$ per kDa at $25\,{}^\circ\mathrm{C}$; measured values are larger, about $0.5$–$0.6\,\mathrm{ns}$ per kDa, because real proteins are not spheres and the hydration layer is thicker. Ubiquitin ($8.6\,\mathrm{kDa}$) has $\tau_{\mathrm{c}} \approx 4\,\mathrm{ns}$ in water at $25\,{}^\circ\mathrm{C}$, a $25\,\mathrm{kDa}$ protein $12$–$15\,\mathrm{ns}$, a $100\,\mathrm{kDa}$ protein about $50\,\mathrm{ns}$. Since $\tau_{\mathrm{c}} \propto \eta/T$, cooling a sample from 25 to $5\,{}^\circ\mathrm{C}$ almost doubles $\tau_{\mathrm{c}}$ (the viscosity of water rises from $0.89$ to $1.52\,\mathrm{mPa\,s}$), and $\mathrm{D_2O}$ is 25 % more viscous than $\mathrm{H_2O}$.

### 13.3.3. The BPP Theory

Time-dependent perturbation theory gives each relaxation rate as a sum of spectral densities at the frequencies of the transitions that the fluctuating field can drive. For two identical spins-1/2 at distance $r$ coupled by the dipolar interaction, Bloembergen, Purcell and Pound obtained:

**Theorem 13.3.1 (BPP Relaxation Rates)** With $K = \frac{\mu_0}{4\pi}\frac{\gamma^2\hbar}{r^3}$ and $j(\omega) = \tau_{\mathrm{c}}/(1 + \omega^2\tau_{\mathrm{c}}^2)$,

$$
\frac{1}{T_1} = \frac{3}{10}K^2\left[j(\omega_0) + 4j(2\omega_0)\right], \qquad \frac{1}{T_2} = \frac{3}{20}K^2\left[3j(0) + 5j(\omega_0) + 2j(2\omega_0)\right]. \tag{13.14}
$$

The structure of Eq. (13.14) explains the main facts of NMR of molecules in solution:

- $T_1$ depends only on spectral densities at $\omega_0$ and $2\omega_0$, frequencies at which energy can be exchanged. As a function of $\tau_{\mathrm{c}}$ it passes through a minimum at $\omega_0\tau_{\mathrm{c}} = 0.616$, where the fluctuations are most efficient at the Larmor frequency, and grows again for slow motion.
- $T_2$ contains the zero-frequency term $j(0) = \tau_{\mathrm{c}}$, the "secular" contribution of slow fluctuations that merely randomize phases. It decreases without limit as the motion slows; this is the origin of the size limit of solution NMR.
- In the extreme narrowing limit $\omega_0\tau_{\mathrm{c}} \ll 1$ (small molecules, water), $T_1 = T_2 = (\frac32K^2\tau_{\mathrm{c}})^{-1}$ and both are seconds; for macromolecules $\omega_0\tau_{\mathrm{c}} \gg 1$ (at $600\,\mathrm{MHz}$, $\omega_0\tau_{\mathrm{c}} = 38$ for $\tau_{\mathrm{c}} = 10\,\mathrm{ns}$), and $T_1$ becomes long while $T_2$ becomes short.

For a proton pair $0.18\,\mathrm{nm}$ apart, $K/2\pi = 21\,\mathrm{kHz}$. With $\tau_{\mathrm{c}} = 25\,\mathrm{ns}$ (a $50\,\mathrm{kDa}$ protein), $1/T_2 \approx \frac{9}{20}K^2\tau_{\mathrm{c}} = 200\,\mathrm{s^{-1}}$ and the line would be $60\,\mathrm{Hz}$ wide, before the other neighbors are added. In a protonated protein every proton has several neighbors within $0.3\,\mathrm{nm}$, and the dense network of $^1\mathrm{H}$–$^1\mathrm{H}$ couplings dominates proton relaxation.

### 13.3.4. Relaxation of a Backbone Amide $^{15}\mathrm{N}$

The backbone amide $^{15}\mathrm{N}$ is the workhorse of relaxation studies, because its relaxation is dominated by two interactions with the same geometry: the dipolar coupling to its own proton at the fixed distance $r_{\mathrm{NH}} = 0.102\,\mathrm{nm}$ and its own CSA, whose axis is close to the bond. Both report the reorientation of a single N–H vector, one per residue, observed in the well-resolved $^1\mathrm{H}$–$^{15}\mathrm{N}$ correlation spectrum.

**Formula 13.3.1 (Relaxation of a Backbone Amide $^{15}\mathrm{N}$)** With $d = \frac{\mu_0\hbar\gamma_{\mathrm{H}}\gamma_{\mathrm{N}}}{4\pi r_{\mathrm{NH}}^3}$ and $c = \omega_{\mathrm{N}}\Delta\sigma/\sqrt3$ ($\Delta\sigma \approx -170\,\mathrm{ppm}$), and $J(\omega)$ of Eq. (13.12),

$$
\begin{aligned}
R_1 &= \frac{d^2}{4}\left[J(\omega_{\mathrm{H}} - \omega_{\mathrm{N}}) + 3J(\omega_{\mathrm{N}}) + 6J(\omega_{\mathrm{H}} + \omega_{\mathrm{N}})\right] + c^2J(\omega_{\mathrm{N}}),\\
R_2 &= \frac{d^2}{8}\left[4J(0) + J(\omega_{\mathrm{H}} - \omega_{\mathrm{N}}) + 3J(\omega_{\mathrm{N}}) + 6J(\omega_{\mathrm{H}}) + 6J(\omega_{\mathrm{H}} + \omega_{\mathrm{N}})\right] + \frac{c^2}{6}\left[4J(0) + 3J(\omega_{\mathrm{N}})\right] + R_{\mathrm{ex}},\\
\mathrm{NOE} &= 1 + \frac{\gamma_{\mathrm{H}}}{\gamma_{\mathrm{N}}}\,\frac{d^2}{4R_1}\left[6J(\omega_{\mathrm{H}} + \omega_{\mathrm{N}}) - J(\omega_{\mathrm{H}} - \omega_{\mathrm{N}})\right].
\end{aligned} \tag{13.15}
$$
Here NOE is the steady-state heteronuclear Overhauser enhancement, the ratio of $^{15}\mathrm{N}$ intensities with and without saturation of the protons, and $R_{\mathrm{ex}}$ is the contribution of chemical exchange (13.6.2).

The three rates sample $J(\omega)$ at the frequencies $0$, $\omega_{\mathrm{N}}$, $\omega_{\mathrm{H}}$ and $\omega_{\mathrm{H}} \pm \omega_{\mathrm{N}}$, a crude spectrum analyzer for the motion of each bond. Their sensitivities differ (Figure below): $R_2$ grows linearly with $\tau_{\mathrm{c}}$ through $J(0)$ and reports slow motion and exchange; $R_1$ peaks near $\tau_{\mathrm{c}} \approx 2\,\mathrm{ns}$; the NOE is sensitive to fast motions near $\omega_{\mathrm{H}}$, approaching its rigid-limit value of about $0.8$ for $\tau_{\mathrm{c}} \gtrsim 5\,\mathrm{ns}$ and becoming small or negative (because $\gamma_{\mathrm{N}} < 0$) for flexible termini and loops moving on sub-nanosecond time scales. In practice a low NOE is the simplest sign of disorder. The ratio $R_2/R_1$ of rigid residues gives $\tau_{\mathrm{c}}$ of the whole molecule, which in turn reports the oligomeric state (a dimer tumbles about twice as slowly) and, from its variation among residues, the anisotropy of tumbling.

**Example 13.3.2 (A Small Protein at 600 MHz)** For a residue in a rigid part of ubiquitin ($\tau_{\mathrm{c}} = 4.1\,\mathrm{ns}$) with internal motion described by $S^2 = 0.85$ and $\tau_{\mathrm{e}} = 50\,\mathrm{ps}$ (13.6.3), Eq. (13.15) at $14.1\,\mathrm{T}$ gives $R_1 = 2.2\,\mathrm{s^{-1}}$, $R_2 = 6.1\,\mathrm{s^{-1}}$ and $\mathrm{NOE} = 0.70$, close to measured values. A residue in the flexible C-terminal tail with $S^2 = 0.3$ and $\tau_{\mathrm{e}} = 0.5\,\mathrm{ns}$ gives $R_1 = 1.8\,\mathrm{s^{-1}}$, $R_2 = 3.2\,\mathrm{s^{-1}}$ and $\mathrm{NOE} = -0.56$.

![Relaxation rates against the rotational correlation time (rigid isotropic tumbling unless stated). A: BPP theory for a pair of protons 0.18 nm apart at 600 MHz; T₁ has a minimum at ω₀τc = 0.62 and T₂ falls monotonically; in the extreme-narrowing region T₁ = T₂. The top axis gives the mass of a globular protein at 0.5 ns per kDa. B: ¹⁵N R₁ and R₂ of a backbone amide at 600 MHz and 1 GHz. C: the {¹H}–¹⁵N heteronuclear NOE. D: the Lipari–Szabo model: internal correlation functions C_I(t) = S² + (1 − S²)exp(−t/τe) for three order parameters (solid) and the total C(t) = C_I(t)exp(−t/τm) for τm = 5 ns (dashed)](./plots/relaxation.py)

### 13.3.5. The Size Limit and How It Is Pushed

The size limit of solution NMR has two causes that grow together. Line widths grow in proportion to $\tau_{\mathrm{c}}$, hence to molecular mass, through the $J(0)$ terms; and the number of signals grows in proportion to the mass as well, so that overlap rises quadratically. Every transfer step in a pulse sequence also loses signal as $\mathrm{e}^{-R_2t}$. Routine structure determination is therefore limited to about $25$–$30\,\mathrm{kDa}$, and backbone assignment becomes difficult above about $50\,\mathrm{kDa}$. Four strategies extend the range.

1. Deuteration. Expressing the protein in $\mathrm{D_2O}$ replaces the carbon-bound protons by deuterons, whose $\gamma$ is 6.5 times smaller, so their dipolar fields contribute about 40 times less to relaxation. After purification in $\mathrm{H_2O}$ the exchangeable amide sites are reprotonated, leaving a dilute network of $^1\mathrm{H}^{\mathrm{N}}$ spins with long $T_2$.
2. TROSY. In a $^1\mathrm{H}$–$^{15}\mathrm{N}$ pair, the dipolar field and the $^{15}\mathrm{N}$ CSA field fluctuate with the same molecular motion, and they interfere: for one of the two lines of the $^{15}\mathrm{N}$ doublet split by the coupling to the proton the two fields add, for the other they partly cancel.

   **Definition 13.3.2 (TROSY)** *TROSY* (transverse relaxation-optimized spectroscopy; Pervushin, Riek, Wider and Wüthrich, 1997) is a class of pulse sequences that select, in each dimension, the component of a scalar-coupled multiplet in which the relaxation by dipolar coupling and by chemical-shift anisotropy cancel, instead of averaging the components by decoupling. In the slow-tumbling limit the transverse rates of the two components are approximately $R_{\mathrm{DD}} + R_{\mathrm{CSA}} \pm 2\sqrt{R_{\mathrm{DD}}R_{\mathrm{CSA}}}\,P_2(\cos\beta)$, where $\beta \approx 17^\circ$ is the angle between the bond and the CSA axis.

   Because $R_{\mathrm{CSA}} \propto B_0^2$ and $R_{\mathrm{DD}}$ is independent of the field, the cancellation is best when $\sqrt{R_{\mathrm{CSA}}}P_2(\cos\beta) = \sqrt{R_{\mathrm{DD}}}$, near $1\,\mathrm{GHz}$ for the amide $^{15}\mathrm{N}$. For $\tau_{\mathrm{c}} = 50\,\mathrm{ns}$ at $1\,\mathrm{GHz}$ the decoupled $^{15}\mathrm{N}$ line has $R_2 \approx 104\,\mathrm{s^{-1}}$, the TROSY component about $13\,\mathrm{s^{-1}}$ from these two interactions (remote protons, reduced by deuteration, add to it). With deuteration and TROSY, backbone spectra of proteins above $100\,\mathrm{kDa}$ can be recorded.
3. Methyl-TROSY. In a deuterated protein whose isoleucine, leucine and valine methyl groups are selectively $^{13}\mathrm{CH_3}$-labeled, an analogous cancellation within the methyl group makes half of the methyl signal relax slowly. Methyl groups are numerous in hydrophobic cores and interfaces and rotate rapidly about their axes; with this approach, Kay and coworkers have studied the dynamics and allostery of complexes approaching $1\,\mathrm{MDa}$, such as the 20S proteasome.
4. $^{19}\mathrm{F}$ NMR. A fluorine introduced at a single site (a fluorinated amino acid or a fluorinated tag on a cysteine) gives one line with $83\,\%$ of the sensitivity of $^1\mathrm{H}$, a chemical shift highly sensitive to environment, no background from the biological sample, and no need for assignment; it is used for membrane proteins and large assemblies in cells, at the cost of information at a single site.

Solid-state NMR avoids the problem differently: without tumbling there is no $\tau_{\mathrm{c}}$, and the anisotropic interactions are averaged instead by **magic-angle spinning** ([6.4.12](/6.4.12#def-12.6.1)) and the signal is transferred by **cross polarization**. It is the method of choice for amyloid fibrils, membrane proteins in lipid bilayers and other insoluble assemblies.

## 13.4. Spectra of Biomolecules

### 13.4.1. Chemical Shifts of Proteins and Nucleic Acids

The **chemical shift** $\delta = (\nu - \nu_{\mathrm{ref}})/\nu_{\mathrm{ref}}\times10^6$ ([6.4.12](/6.4.12#def-12.2.2)) is referenced in aqueous biological samples to the methyl signal of DSS (4,4-dimethyl-4-silapentane-1-sulfonic acid), which is water-soluble, rather than to TMS; $^{13}\mathrm{C}$ and $^{15}\mathrm{N}$ shifts are referenced indirectly through fixed ratios of their frequencies to that of DSS protons. In a spectrometer whose proton frequency is $800\,\mathrm{MHz}$, $1\,\mathrm{ppm}$ of $^1\mathrm{H}$ is $800\,\mathrm{Hz}$, so the center of the amide region ($\approx 8.2\,\mathrm{ppm}$) lies about $2.8\,\mathrm{kHz}$ from the water signal at $4.77\,\mathrm{ppm}$ ($25\,{}^\circ\mathrm{C}$). Typical ranges in proteins:

| Protons | $\delta/\mathrm{ppm}$ |
|---|---|
| methyl groups (Ala, Val, Leu, Ile, Thr, Met) | $0$–$1.5$ (ring-current shifted methyls in cores down to $-1$) |
| other aliphatic side chains | $1.5$–$3.5$ |
| $\mathrm{H}^\alpha$ | $3.5$–$5.5$ |
| aromatic ring protons | $6.5$–$7.8$ |
| backbone amides $\mathrm{H}^{\mathrm{N}}$ | $6.5$–$10.5$ in folded proteins; $7.8$–$8.6$ in disordered ones |
| Trp indole $\mathrm{H}^{\varepsilon1}$ | $\approx 10$ |
| nucleic acids: imino protons of base-paired G and U/T | $10$–$15$ |

Shifts are local structural reporters. In a folded protein, hydrogen bonding, the **ring-current effect** of nearby aromatic rings and the local electric field spread the amide signals over $4\,\mathrm{ppm}$; in an **intrinsically disordered protein** each residue rapidly samples many conformations, its shift is averaged towards the random-coil value, and all amides crowd between $7.8$ and $8.6\,\mathrm{ppm}$. A one-dimensional spectrum therefore tells at a glance whether a protein is folded. In nucleic acids, an imino proton is protected from exchange with water only when it is hydrogen bonded in a base pair: the number of signals above $10\,\mathrm{ppm}$ counts the stable base pairs, and their shifts distinguish Watson–Crick G·C ($12$–$13.5\,\mathrm{ppm}$) and A·U ($13$–$15\,\mathrm{ppm}$) pairs from G·U wobble pairs ($10$–$12\,\mathrm{ppm}$). In the 1970s, the imino spectra of tRNA and of oligonucleotide duplexes provided the first direct evidence that Watson–Crick pairs, and not Hoogsteen pairs, form in solution.

The deviation of the backbone shifts $\mathrm{C}^\alpha$, $\mathrm{C}^\beta$, $\mathrm{C}'$ and $\mathrm{H}^\alpha$ from their random-coil values, the *secondary chemical shift*, reports secondary structure: $\mathrm{C}^\alpha$ is shifted downfield (positive) by $2$–$3\,\mathrm{ppm}$ in helices and upfield in strands, $\mathrm{C}^\beta$ the reverse. Programs such as TALOS-N predict the backbone dihedral angles $\phi$, $\psi$ from the shifts of a residue and its neighbors with an accuracy of $10$–$15^\circ$, by comparison with a database of proteins of known structure; the shifts, which every assignment gives for free, are thus the first restraints of a structure.

### 13.4.2. Scalar Coupling and the Karplus Relation

The **spin–spin coupling** through bonds ([6.4.12](/6.4.12#def-12.3.1)) splits lines by the **coupling constant** $J$, independent of $B_0$. In proteins, the one-bond couplings are used to transfer magnetization between bonded nuclei (13.4.4); their sizes set the delays of the pulse sequences:

| Coupling | $^1J(\mathrm{N},\mathrm{H}^{\mathrm{N}})$ | $^1J(\mathrm{C}^\alpha,\mathrm{H}^\alpha)$ | $^1J(\mathrm{C}^\alpha,\mathrm{C}')$ | $^1J(\mathrm{N},\mathrm{C}')$ | $^1J(\mathrm{N},\mathrm{C}^\alpha)$ | $^2J(\mathrm{N},\mathrm{C}^\alpha_{i-1})$ |
|---|---|---|---|---|---|---|
| $\lvert J\rvert/\mathrm{Hz}$ | 92 | 140 | 55 | 15 | 7–11 | 4–9 |

($^1J_{\mathrm{NH}}$ is negative because $\gamma_{\mathrm{N}} < 0$.) The three-bond couplings depend on dihedral angles through the **Karplus equation** ([6.4.12](/6.4.12#def-12.3.2)).

**Formula 13.4.1 (Karplus Relation for the Backbone)** The coupling between the amide proton and the $\alpha$ proton depends on the backbone angle $\phi$:

$$
{}^3J(\mathrm{H}^{\mathrm{N}}, \mathrm{H}^\alpha) = A\cos^2\theta + B\cos\theta + C, \qquad \theta = \phi - 60^\circ, \tag{13.16}
$$
with $A = 6.51\,\mathrm{Hz}$, $B = -1.76\,\mathrm{Hz}$, $C = 1.60\,\mathrm{Hz}$ (Vuister and Bax, 1993, calibrated on proteins of known structure); $\theta$ is the dihedral angle $\mathrm{H}^{\mathrm{N}}$–N–$\mathrm{C}^\alpha$–$\mathrm{H}^\alpha$.

In an $\alpha$ helix ($\phi \approx -57^\circ$) $^3J \approx 4\,\mathrm{Hz}$, in a $\beta$ strand ($\phi \approx -120$ to $-140^\circ$) $8$–$10\,\mathrm{Hz}$; values of $6$–$8\,\mathrm{Hz}$ indicate averaging over conformations. The relation is many-valued (one $J$ corresponds to up to four $\phi$), and it is used together with the restriction of most residues to $\phi < 0$ in the **Ramachandran plot**. Other Karplus relations give $\chi_1$ from $^3J(\mathrm{H}^\alpha,\mathrm{H}^\beta)$ and $^3J(\mathrm{N},\mathrm{H}^\beta)$, the sugar pucker of nucleic acids from $^3J(\mathrm{H}1',\mathrm{H}2')$, and the backbone torsions of RNA from couplings to $^{31}\mathrm{P}$.

### 13.4.3. The Quantum Description: Density Operator and Product Operators

The vector model fails as soon as couplings matter: the magnetization of a coupled spin can be converted into states that have no classical analogue, such as antiphase magnetization and multiple-quantum coherence, which carry the information of all multidimensional experiments. The quantum description is needed, and it is an elegant application of the linear algebra of $2\times2$ matrices.

A single spin-1/2 has the basis states $|\alpha\rangle = (1, 0)^{\mathsf T}$ and $|\beta\rangle = (0, 1)^{\mathsf T}$ and the spin operators (in units of $\hbar$) $\hat{I}_k = \frac12\sigma_k$ with the Pauli matrices,

$$
\hat{I}_x = \frac12\begin{bmatrix}0 & 1\\ 1 & 0\end{bmatrix}, \quad \hat{I}_y = \frac12\begin{bmatrix}0 & -\mathrm{i}\\ \mathrm{i} & 0\end{bmatrix}, \quad \hat{I}_z = \frac12\begin{bmatrix}1 & 0\\ 0 & -1\end{bmatrix}, \tag{13.17}
$$
which are **Hermitian matrices** with eigenvalues $\pm\frac12$ and satisfy the angular-momentum **commutator** relations $[\hat{I}_x, \hat{I}_y] = \mathrm{i}\hat{I}_z$ (cyclically). A sample is not one spin in one state but an ensemble of spins in different states, and it is described by a matrix.

**Definition 13.4.1 (Density Operator)** For an ensemble in which a fraction $p_k$ of the members is in the state $|\psi_k\rangle$, the *density operator* is $\hat\rho = \sum_kp_k|\psi_k\rangle\langle\psi_k|$. The expectation value of an observable $\hat{Q}$ is $\langle\hat{Q}\rangle = \operatorname{tr}(\hat{Q}\hat\rho)$. Its diagonal elements are the populations of the basis states, and its off-diagonal elements, the *coherences*, are nonzero only if the phases of the members are correlated; the transverse magnetization is a coherence between $|\alpha\rangle$ and $|\beta\rangle$.

The density operator evolves under the Schrödinger equation as

$$
\frac{\mathrm{d}\hat\rho}{\mathrm{d}t} = -\mathrm{i}[\hat{H}, \hat\rho] \quad\Longrightarrow\quad \hat\rho(t) = \mathrm{e}^{-\mathrm{i}\hat{H}t}\,\hat\rho(0)\,\mathrm{e}^{\mathrm{i}\hat{H}t} \tag{13.18}
$$
for a Hamiltonian $\hat{H}$ (in angular-frequency units) that is constant during the interval (the Liouville–von Neumann equation; the solution uses the **matrix exponential**). A pulse sequence is a succession of intervals with different constant Hamiltonians, and the final $\hat\rho$ is obtained by applying the "sandwich" of Eq. (13.18) interval by interval. In thermal equilibrium $\hat\rho = \mathrm{e}^{-\hat{H}/k_{\mathrm{B}}T}/Z \approx \frac12\hat{E} + \frac{\hbar\gamma B_0}{2k_{\mathrm{B}}T}\hat{I}_z$, where $\hat{E}$ is the identity; the identity part never changes and gives no signal, so the experiment starts from $\hat\rho(0) \propto \hat{I}_z$.

For several spins the operators are tensor products ($2\hat{I}_x\hat{S}_z$ is a $4\times4$ matrix), and the 16 products $\hat{E}/2$, $\hat{I}_k$, $\hat{S}_k$, $2\hat{I}_k\hat{S}_l$ form a basis for a pair of spins. The *product-operator formalism* (Sørensen, Ernst and coworkers, 1983) writes $\hat\rho$ in this basis and uses the fact that each Hamiltonian of interest rotates the operators within small subspaces, like rotations of a vector. With rotations taken in the positive sense (the usual convention of NMR texts, which reverses the sense of Theorem 13.2.1 for $\gamma > 0$ but affects only signs of phases):

| Hamiltonian | Effect during time $t$ (or pulse of angle $\beta$) |
|---|---|
| pulse about $x$, $\omega_1\hat{I}_x$ | $\hat{I}_z \to \hat{I}_z\cos\beta - \hat{I}_y\sin\beta$; $\hat{I}_y \to \hat{I}_y\cos\beta + \hat{I}_z\sin\beta$ |
| chemical shift, $\Omega\hat{I}_z$ | $\hat{I}_x \to \hat{I}_x\cos\Omega t + \hat{I}_y\sin\Omega t$ |
| scalar coupling, $2\pi J\hat{I}_z\hat{S}_z$ (weak coupling) | $\hat{I}_x \to \hat{I}_x\cos\pi Jt + 2\hat{I}_y\hat{S}_z\sin\pi Jt$; $\hat{I}_y \to \hat{I}_y\cos\pi Jt - 2\hat{I}_x\hat{S}_z\sin\pi Jt$ |

The operator $2\hat{I}_x\hat{S}_z$ is *antiphase* magnetization: $I$ magnetization whose sign depends on the state of $S$, which appears as a doublet with one positive and one negative line. Coupling interconverts in-phase and antiphase magnetization, and a pulse on $S$ converts $2\hat{I}_z\hat{S}_z$-type order into coherence on the other spin: this is how magnetization moves from nucleus to nucleus.

### 13.4.4. Two-Dimensional Spectra and the HSQC

In **two-dimensional NMR** ([6.4.12](/6.4.12#def-12.5.2)) the signal is recorded as a function of two times: an incremented evolution period $t_1$, during which the magnetization is labeled by the frequency of one nucleus, and the acquisition time $t_2$, during which it is detected on another. Fourier transformation in both times gives a spectrum $S(\omega_1, \omega_2)$ with a cross peak at the pair of frequencies of every pair of nuclei between which magnetization was transferred.

**Example 13.4.1 (The HSQC by Product Operators)** In the $^1\mathrm{H}$–$^{15}\mathrm{N}$ heteronuclear single-quantum coherence (HSQC) experiment (Figure of 13.2.5, panel B), with H the amide proton and N its nitrogen:

1. A $90^\circ_x$ pulse on H: $\hat{H}_z \to -\hat{H}_y$.
2. INEPT (insensitive nuclei enhanced by polarization transfer): a delay $\tau = 1/(4J_{\mathrm{NH}}) = 2.7\,\mathrm{ms}$, simultaneous $180^\circ$ pulses on H and N, and a second $\tau$. The $180^\circ$ pulses refocus the chemical shift of H, while the coupling evolves for $2\tau = 1/(2J)$, $\sin(\pi J\cdot2\tau) = 1$: up to sign, $-\hat{H}_y \to 2\hat{H}_x\hat{N}_z$. Then $90^\circ_y$ on H and $90^\circ_x$ on N give $2\hat{H}_z\hat{N}_y$: the coherence now precesses at the $^{15}\mathrm{N}$ frequency.
3. Evolution for $t_1$ with a $180^\circ$ H pulse in its middle, which refocuses the coupling: $2\hat{H}_z\hat{N}_y \to 2\hat{H}_z\hat{N}_y\cos\Omega_{\mathrm{N}}t_1 - 2\hat{H}_z\hat{N}_x\sin\Omega_{\mathrm{N}}t_1$.
4. The reverse INEPT (simultaneous $90^\circ$ pulses and the same delays) converts the cosine term back into in-phase proton magnetization, $\hat{H}_x\cos\Omega_{\mathrm{N}}t_1$, which is detected during $t_2$ while $^{15}\mathrm{N}$ is decoupled. The sine term is selected in a second scan with shifted phases, giving quadrature detection in $t_1$.

The signal $\cos(\Omega_{\mathrm{N}}t_1)\,\mathrm{e}^{\mathrm{i}\Omega_{\mathrm{H}}t_2}$, transformed in $t_1$ and $t_2$, gives one peak at $(\Omega_{\mathrm{N}}, \Omega_{\mathrm{H}})$ for every N–H group: one per residue except proline, plus the side-chain $\mathrm{NH_2}$ of Asn and Gln and the indole NH of Trp. Excitation and detection are both on protons, and the gain over direct $^{15}\mathrm{N}$ observation is the factor of 300 of 13.1.4.

The $^1\mathrm{H}$–$^{15}\mathrm{N}$ HSQC is the "fingerprint" of a protein: it is recorded in minutes to an hour on a $0.1\,\mathrm{mM}$ sample, its dispersion tells whether the protein is folded, and changes of its peaks report binding, mutation, pH, temperature and conformational change. The $^1\mathrm{H}$–$^{13}\mathrm{C}$ HSQC of the methyl region plays the same role for large proteins. Other two-dimensional experiments transfer magnetization differently:

| Experiment | Transfer | Cross peaks between | Use |
|---|---|---|---|
| COSY | $J$ coupling, one step | protons two or three bonds apart | spin systems of small molecules and peptides |
| TOCSY | $J$ coupling, isotropic mixing (spin lock) | all protons of a residue's spin system | identifying residue types |
| NOESY | cross-relaxation (NOE) through space | protons less than about $0.5\,\mathrm{nm}$ apart | sequential assignment, distances |
| HSQC, HMQC | one-bond heteronuclear $J$ | a proton and its directly bonded $^{15}\mathrm{N}$ or $^{13}\mathrm{C}$ | fingerprint, titrations, relaxation |

A three-dimensional experiment inserts a second incremented evolution period and a second transfer; NOESY-HSQC, for example, spreads the crowded NOESY spectrum along the $^{15}\mathrm{N}$ or $^{13}\mathrm{C}$ frequency of the proton that receives the NOE. Sampling a grid in two or three indirect dimensions is slow, a few days per spectrum; non-uniform sampling records a random subset of the grid and reconstructs the spectrum by methods of sparse recovery, cutting the measuring time several-fold.

### 13.4.5. Resonance Assignment

Before anything can be interpreted, each signal must be assigned to its atom. For peptides and small unlabeled proteins, the strategy of Wüthrich uses only proton spectra. TOCSY (or COSY) identifies the spin system of each residue, whose pattern of shifts indicates its type (Gly has two $\mathrm{H}^\alpha$; Ala a methyl coupled to $\mathrm{H}^\alpha$; Glu and Gln are distinguished only by TOCSY patterns of their longer side chains), and NOESY links each residue to its neighbor in sequence by the short distance between $\mathrm{H}^\alpha(i)$ and $\mathrm{H}^{\mathrm{N}}(i + 1)$, $d_{\alpha N}(i, i+1) \le 0.36\,\mathrm{nm}$ whatever the conformation. Matching the chain of spin-system types to the known sequence fixes the assignment.

**Example 13.4.2 (A Heptapeptide with the RGD Motif)** The sequence Arg–Gly–Asp is recognized by integrins, and replacing Asp by Glu (RGE) abolishes binding. In a study of the heptapeptides YGRGDSP and YGRGESP, COSY identified the spin systems of the seven residues, NOESY ordered them along the chain through the $d_{\alpha N}(i, i+1)$ connectivities, and the pattern of additional NOEs between residues two apart indicated a type II $\beta$ turn for the RGD peptide but a type I or III turn for RGE: a difference of local conformation that correlates with the loss of activity.

For proteins above about $10\,\mathrm{kDa}$ the proton spectra are too crowded, and assignment uses triple-resonance experiments on $^{13}\mathrm{C}/^{15}\mathrm{N}$-labeled samples, which transfer magnetization along the backbone through the one-bond couplings of 13.4.2. The HNCACB (or CBCANH) experiment correlates the $\mathrm{H}^{\mathrm{N}}$ and N of residue $i$ with the $\mathrm{C}^\alpha$ and $\mathrm{C}^\beta$ of both residue $i$ (through $^1J_{\mathrm{NC}^\alpha}$) and residue $i - 1$ (through $^2J_{\mathrm{NC}^\alpha}$); the CBCA(CO)NH (or HN(CO)CACB) experiment, routed through the carbonyl, shows only those of residue $i - 1$. For each amide, a "strip" of the three-dimensional spectrum at its $(\mathrm{H}^{\mathrm{N}}, \mathrm{N})$ position shows two pairs of $\mathrm{C}^\alpha/\mathrm{C}^\beta$ peaks, and the strips are chained by matching the "previous residue" pair of one strip with the "own residue" pair of another: a sequential walk. The $\mathrm{C}^\alpha$ and $\mathrm{C}^\beta$ shifts identify residue types (Gly has no $\mathrm{C}^\beta$ and $\mathrm{C}^\alpha \approx 45\,\mathrm{ppm}$; Ala $\mathrm{C}^\beta \approx 19\,\mathrm{ppm}$; Ser and Thr $\mathrm{C}^\beta$ above $60\,\mathrm{ppm}$), which anchors the walk to the sequence. When sensitivity is low, the more sensitive pairs HNCA/HN(CO)CA and HNCO/HN(CA)CO are used instead. Side chains are then assigned with HCCH-TOCSY and NOESY-type spectra. Nucleic acids lack a backbone path of strong couplings through the phosphates and are still assigned largely through NOESY, starting from the imino protons of base pairs.

### 13.4.6. Chemical-Shift Perturbation and Titrations

**Definition 13.4.2 (Chemical Shift Perturbation)** *Chemical shift perturbation* (CSP) is the change of the chemical shifts of a macromolecule on adding a binding partner. In an $^1\mathrm{H}$–$^{15}\mathrm{N}$ HSQC titration it is summarized per residue as the combined change $\Delta\delta = \sqrt{\Delta\delta_{\mathrm{H}}^2 + (\alpha\Delta\delta_{\mathrm{N}})^2}$, with $\alpha \approx 0.14$–$0.2$ compensating the larger range of $^{15}\mathrm{N}$ shifts.

Residues with large $\Delta\delta$, mapped onto the structure, outline the binding site; for the SH3 domain of the adaptor protein Crk and a peptide from Sos, the map coincides with the interface later seen in the crystal structure of the complex. Fitting the shift of a peak against ligand concentration with the binding isotherm of [7.6.3](/7.6.3) gives the dissociation constant, which NMR measures well from about $1\,\mu\mathrm{M}$ to $10\,\mathrm{mM}$, a range that includes the weak interactions most other methods miss; how the peaks move depends on the exchange rate between free and bound states (13.6.2). In fragment-based drug discovery, HSQC spectra or ligand-observed experiments (saturation-transfer difference, WaterLOGSY) screen libraries of small, weakly binding molecules. Titration against pH works in the same way: following the shift of a histidine $\mathrm{C}^{\varepsilon1}$–H or of an Asp or Glu carboxyl $^{13}\mathrm{C}$ through the protonation equilibrium gives the $\mathrm{p}K_{\mathrm{a}}$ of individual groups, which in folded proteins are often shifted by several units from their values in peptides ([7.6.6](/7.6.6)). CSP shows where something changes, which may be an allosteric site far from the contact surface as well as the contact surface itself.

## 13.5. Structure Determination

### 13.5.1. The Nuclear Overhauser Effect

The **nuclear Overhauser effect** (NOE, [6.4.12](/6.4.12#def-12.5.1)) is the transfer of population differences between spins by cross-relaxation, the mutual flip-flop of two spins driven by their fluctuating dipolar coupling. For two protons $I$ and $S$, the longitudinal magnetizations obey the Solomon equations,

$$
\frac{\mathrm{d}I_z}{\mathrm{d}t} = -\rho_I(I_z - I_z^0) - \sigma(S_z - S_z^0), \qquad \frac{\mathrm{d}S_z}{\mathrm{d}t} = -\sigma(I_z - I_z^0) - \rho_S(S_z - S_z^0), \tag{13.19}
$$
in which $\rho$ is the auto-relaxation rate and $\sigma$ the cross-relaxation rate.

**Formula 13.5.1 (Cross-Relaxation Rate)** For two protons at distance $r$ in a molecule tumbling isotropically, with $K$ and $j(\omega)$ as in Theorem 13.3.1,

$$
\sigma = \frac{K^2}{10}\left[6j(2\omega_0) - j(0)\right] \propto \frac{1}{r^6}\,f(\tau_{\mathrm{c}}), \qquad \rho = \frac{K^2}{10}\left[j(0) + 3j(\omega_0) + 6j(2\omega_0)\right]. \tag{13.20}
$$
$\sigma$ is positive for fast tumbling and negative for slow tumbling, and changes sign at $\omega_0\tau_{\mathrm{c}} = \sqrt{5}/2 = 1.12$.

The two terms correspond to the two flip processes: the double-quantum transition $\alpha\alpha \leftrightarrow \beta\beta$ at $2\omega_0$ and the zero-quantum flip-flop $\alpha\beta \leftrightarrow \beta\alpha$ at zero frequency. Small molecules ($\omega_0\tau_{\mathrm{c}} \ll 1$) show positive NOEs of at most $50\,\%$ in steady state; macromolecules are deep in the slow regime ($\omega_0\tau_{\mathrm{c}} \approx 50$ for a $25\,\mathrm{kDa}$ protein at $600\,\mathrm{MHz}$), where $\sigma \approx -K^2\tau_{\mathrm{c}}/10$ is large and negative; molecules of $1$–$2\,\mathrm{kDa}$ near the crossover may show no NOE at all and are measured with the rotating-frame variant ROESY.

In the NOESY experiment, transverse magnetization labeled with the frequency of $I$ during $t_1$ is returned to $z$, allowed to cross-relax during a mixing time $\tau_{\mathrm{m}}$, and read out on $S$. For short mixing times the cross-peak intensity grows linearly, $a_{IS} \propto \sigma\tau_{\mathrm{m}} \propto r^{-6}$ (the initial-rate approximation), which gives distances by calibration against a known pair:

$$
r_{IS} = r_{\mathrm{ref}}\left(\frac{a_{\mathrm{ref}}}{a_{IS}}\right)^{1/6}. \tag{13.21}
$$
The sixth root is forgiving: a factor of two error in intensity gives a 12 % error in distance. Its other side is that the NOE becomes undetectable beyond about $0.5$–$0.6\,\mathrm{nm}$, which is why NMR structures are built from many short contacts. For longer mixing times magnetization moves on to third spins, $I \to K \to S$: this *spin diffusion* makes distant protons appear close and is most severe for large, protonated molecules; it is limited by short mixing times, deuteration or full relaxation-matrix analysis. Because the internuclear vector fluctuates and the average is $\langle r^{-6}\rangle^{-1/6}$, which is dominated by the shortest distances visited, and because internal motion also modulates $\sigma$, NOE distances are used conservatively, as upper bounds in classes (for example strong $\le 0.27\,\mathrm{nm}$, medium $\le 0.33\,\mathrm{nm}$, weak $\le 0.5\,\mathrm{nm}$), not as exact values.

### 13.5.2. NOE Patterns and Other Local Restraints

The pattern of short proton–proton distances identifies secondary structure before any calculation (Figure below): an $\alpha$ helix brings $\mathrm{H}^{\mathrm{N}}(i)$ close to $\mathrm{H}^{\mathrm{N}}(i + 1)$ ($0.28\,\mathrm{nm}$) and $\mathrm{H}^\alpha(i)$ close to $\mathrm{H}^{\mathrm{N}}(i + 3)$ and $\mathrm{H}^\beta(i + 3)$, while a $\beta$ strand has a very short $d_{\alpha N}(i, i + 1)$ ($0.22\,\mathrm{nm}$), and in an antiparallel sheet the $\mathrm{H}^\alpha$ protons of non-hydrogen-bonded cross-strand pairs ($0.23\,\mathrm{nm}$) and the amide protons of hydrogen-bonded pairs ($0.33\,\mathrm{nm}$) face each other. Long-range NOEs between residues far apart in sequence define the fold. Together with these come:

- dihedral-angle restraints from $^3J$ couplings (Formula 13.4.1) and from backbone chemical shifts (13.4.1);
- hydrogen-bond restraints, from amides protected from exchange with the solvent (13.6.5) or from couplings measured directly across hydrogen bonds;
- the restraints of the next two subsections, which are not local.

![Proton–proton distances shorter than 0.5 nm (the NOE range) computed from backbone coordinates of ideal secondary structures built with standard bond lengths and angles (amide, α and one β proton per residue). Each symbol marks the shortest classified distance between residues i and j, its size and color giving the distance: squares d_NN (Hᴺ–Hᴺ), circles d_αN (Hᵅ–Hᴺ), diamonds d_αα (Hᵅ–Hᵅ). A: α helix (φ = −57°, ψ = −47°): strong d_NN(i, i+1) and d_αN(i, i+3), weaker d_αN(i, i+2) and (i, i+4). B: two-stranded antiparallel β sheet (φ = −139°, ψ = 135°) with the second strand numbered 9–15 after an unmodeled turn: very short sequential d_αN(i, i+1), and on the antidiagonal cross-strand d_αα at non-hydrogen-bonded pairs (1–15, 3–13, 5–11, 7–9) and d_NN at hydrogen-bonded pairs (2–14, 4–12, 6–10)](./plots/noe-map.py)

### 13.5.3. Residual Dipolar Couplings

The direct dipolar coupling between two bonded nuclei is enormous (for N–H, $23\,\mathrm{kHz}$ at its maximum) and carries the orientation of the bond, but in isotropic solution it averages exactly to zero. The trick of Tolman and Prestegard (1995) and Tjandra and Bax (1997) is to make the solution very slightly anisotropic.

**Definition 13.5.1 (Residual Dipolar Coupling)** When a macromolecule is weakly aligned with respect to the magnetic field, the dipolar coupling between two nuclei $I$ and $S$ at fixed distance $r$ no longer averages to zero; the remaining average,

$$
D_{IS} = -\frac{\mu_0\gamma_I\gamma_S\hbar}{8\pi^2r^3}\left\langle3\cos^2\theta - 1\right\rangle , \tag{13.22}
$$
in hertz, where $\theta$ is the angle between the internuclear vector and $\boldsymbol{B}_0$ and the brackets average over the molecular orientations and internal motions, is the *residual dipolar coupling* (RDC). It adds to the scalar coupling, so the splitting measured in the aligned sample is $J + D$ and $D$ is obtained as the difference from the isotropic sample.

For a rigid molecule, the average is expressed through the alignment tensor of the molecule as a whole: in its principal frame, for a bond with polar angles $(\theta, \phi)$,

$$
D(\theta, \phi) = D_{\mathrm{a}}\left[(3\cos^2\theta - 1) + \tfrac32R\sin^2\theta\cos2\phi\right], \tag{13.23}
$$
where the magnitude $D_{\mathrm{a}}$ and rhombicity $R$ are fitted together with the orientation of the frame. The prefactor of Eq. (13.22) is $+11.5\,\mathrm{kHz}$ for N–H ($r = 0.102\,\mathrm{nm}$; positive because $\gamma_{\mathrm{N}} < 0$) and $-23.4\,\mathrm{kHz}$ for $\mathrm{C}^\alpha$–$\mathrm{H}^\alpha$ ($0.109\,\mathrm{nm}$). An alignment of order $10^{-3}$ scales these to $\pm10$–$30\,\mathrm{Hz}$, small enough to keep the spectrum simple and large enough to measure to $\pm1\,\mathrm{Hz}$. Alignment is produced by dilute liquid crystals that do not bind the protein: bicelles of DMPC and DHPC, filamentous Pf1 phage ($10$–$20\,\mathrm{mg\,mL^{-1}}$), alkyl–poly(ethylene glycol)/hexanol phases, or stretched and compressed polyacrylamide gels; nucleic acids, with their large magnetic anisotropy, also align weakly by themselves.

An RDC reports the orientation of a bond relative to a frame common to the whole molecule, not the distance to a neighbor: it is a global restraint. It can therefore fix the relative orientation of two domains that make no NOE contacts, test a crystal structure against the solution state (a quality factor $Q$ of the fit), refine structures beyond the precision of NOEs, and, measured in several media or for residues with internal motion, characterize the amplitude and direction of motions slower than $\tau_{\mathrm{c}}$ up to milliseconds. Its weakness is degeneracy: $3\cos^2\theta - 1$ does not distinguish $\theta$ from $180^\circ - \theta$, and a set of RDCs is invariant under $180^\circ$ rotations about the principal axes of the alignment tensor. RDCs also do not suffer from spin diffusion, which makes them valuable for large proteins, and combined with SAXS ([7.6.9](/7.6.9#sec-9.12)) they define the global architecture of RNA.

**Remark 13.5.1 (Signs)** Formulas that write $D \propto 1 - 3\cos^2\theta$ without $\gamma$ assume two positive gyromagnetic ratios, as for C–H: a C–H bond parallel to the principal alignment axis then has $D < 0$. For N–H the product $\gamma_{\mathrm{H}}\gamma_{\mathrm{N}}$ is negative and the sign is reversed, $D > 0$ for a bond along the axis; the one-bond scalar coupling $^1J_{\mathrm{NH}} \approx -92\,\mathrm{Hz}$ is negative for the same reason. Many papers report $^1D_{\mathrm{NH}}$ multiplied by $-1$ or normalize all couplings to the N–H case; the convention must be checked when RDCs from different sources are combined.

![Geometric restraints. A: Karplus relation ³J(Hᴺ, Hᵅ) = 6.51 cos²θ − 1.76 cos θ + 1.60 Hz with θ = φ − 60° (Vuister and Bax); the α helix (φ = −57°) gives about 4 Hz, the β sheet (φ = −139°) about 9 Hz, and most residues lie in the shaded half φ < 0. B: residual dipolar coupling of an N–H bond against the angle θ between bond and alignment axis, D = Dₐ(3cos²θ − 1) with Dₐ = 10 Hz: positive along the axis because γ_N < 0, zero at the magic angle 54.7°. C: approximate distance ranges of NMR and EPR restraints and their distance laws, with FRET for comparison](./plots/restraints.py)

### 13.5.4. Paramagnetic Restraints

A paramagnetic center attached to the molecule extends the reach of NMR far beyond $0.5\,\mathrm{nm}$, because the magnetic moment of an electron is 658 times that of a proton.

**Definition 13.5.2 (Paramagnetic Relaxation Enhancement)** *Paramagnetic relaxation enhancement* (PRE) is the increase of the relaxation rates of nuclei by the fluctuating dipolar field of an unpaired electron. For an electron spin $S$ at distance $r$ from a proton, the transverse enhancement is (Solomon–Bloembergen)

$$
\Gamma_2 = \frac{1}{15}\left(\frac{\mu_0}{4\pi}\right)^2\gamma_{\mathrm{H}}^2g^2\mu_{\mathrm{B}}^2S(S + 1)\,\frac{1}{r^6}\left[4\tau_{\mathrm{c}} + \frac{3\tau_{\mathrm{c}}}{1 + \omega_{\mathrm{H}}^2\tau_{\mathrm{c}}^2}\right], \tag{13.24}
$$
with $\tau_{\mathrm{c}}$ the correlation time of the electron–nucleus vector (including electron relaxation).

PRE has the $r^{-6}$ dependence of the NOE, but a prefactor about $4\times10^5$ times larger, so a nitroxide spin label such as MTSL (methanethiosulfonate spin label, attached to a cysteine introduced by mutation at a chosen site) broadens signals out to $1.5$–$3\,\mathrm{nm}$. It is measured as the ratio of peak intensities with the label in its paramagnetic form and after reduction to the diamagnetic hydroxylamine with ascorbate. Because of the $r^{-6}$ weighting, a minor conformation that brings the label close to a residue dominates the PRE even at a population of a few percent; PRE is therefore the method of choice for transient encounter complexes, for the compact states of intrinsically disordered proteins and for intermolecular contacts (with the label on one partner and the observed nuclei on the other), and solvent PRE with a soluble paramagnetic agent maps the accessible surface.

A lanthanide ion with an anisotropic magnetic susceptibility (Tb³⁺, Dy³⁺, Tm³⁺, Yb³⁺, bound to a tag) shifts the signals of nearby nuclei instead.

**Definition 13.5.3 (Pseudocontact Shift)** The *pseudocontact shift* (PCS) is the change of the chemical shift of a nucleus caused by the anisotropic magnetic susceptibility $\Delta\chi$ of a paramagnetic center at distance $r$:

$$
\Delta\delta^{\mathrm{PCS}} = \frac{1}{12\pi r^3}\left[\Delta\chi_{\mathrm{ax}}(3\cos^2\theta - 1) + \tfrac32\Delta\chi_{\mathrm{rh}}\sin^2\theta\cos2\phi\right], \tag{13.25}
$$
with $(r, \theta, \phi)$ the position of the nucleus in the principal frame of the susceptibility tensor. It is measured as the difference of the shifts of the paramagnetic and a diamagnetic (La³⁺, Lu³⁺, Y³⁺) sample.

Decaying only as $r^{-3}$, PCS reaches $4$–$6\,\mathrm{nm}$ and gives both distance and angular information; the same tensor also aligns the molecule in the field and produces RDCs. PCS and PRE are particularly useful to dock domains and to position ligands.

### 13.5.5. Structure Calculation

The restraints of an NMR structure are hundreds to thousands of bounds on distances and angles, each imprecise, and the structure is the set of conformations that satisfy them together with the known covalent geometry.

**Algorithm 13.5.1 (Restraint-Driven Simulated Annealing)**

1. Represent the molecule with standard covalent geometry and a simplified force field (bonds, angles, planarity, chirality, a purely repulsive van der Waals term).
2. Define a target function $E = E_{\operatorname{Cov}} + E_{\mathrm{rep}} + w_{\mathrm{NOE}}\sum\max(0, r_{ij} - u_{ij})^2 + w_\phi\sum\Delta\phi^2 + w_D\sum(D^{\mathrm{calc}} - D^{\mathrm{obs}})^2 + \cdots$, a flat-bottom penalty for each violated restraint.
3. Starting from random or extended conformations, run molecular dynamics (in Cartesian or torsion-angle coordinates) at high temperature with soft repulsion, so that chains can pass through each other, and cool slowly while raising the weights of the restraints and of the repulsion: **simulated annealing** ([7.6.9](/7.6.9#alg-9.11.1)).
4. Repeat from 50–200 starting conformations; keep the 10–20 of lowest energy, refine them in a more complete force field with explicit or implicit solvent.
5. Validate: restraint violations, Ramachandran statistics, packing, agreement with data not used in the calculation (cross-validated RDCs, chemical shifts).

The output is an ensemble of structures, and its spread, measured by the root-mean-square deviation (RMSD) of the coordinates from their mean, has two meanings that cannot be separated without further data: lack of restraints (loops and termini with few NOEs) and real motion. Well-defined regions of good structures have backbone RMSDs of $0.03$–$0.06\,\mathrm{nm}$. Programs: CYANA (torsion-angle dynamics, with automated NOE assignment), Xplor-NIH and CNS, ARIA; final refinement in Amber, CHARMM or GROMACS force fields. The bottleneck of the whole process, the assignment of thousands of NOESY cross peaks to proton pairs, is done iteratively by software that uses each preliminary structure to resolve ambiguities. Chemical shifts alone, combined with Rosetta fragment assembly (CS-Rosetta) and a few NOEs or RDCs, determine structures of proteins up to about $40\,\mathrm{kDa}$; since 2021, predicted structures ([7.6.15](/7.6.15)) increasingly serve as starting models that NMR data confirm, correct or refine, and NMR contributes where prediction is weakest, in dynamics and alternative states.

## 13.6. Dynamics

### 13.6.1. Time Scales

The distinctive strength of NMR is that it measures motion at atomic resolution over about seventeen orders of magnitude in time, each window with its own experiment (Figure below). Spin relaxation (13.3, 13.6.3) reports motions faster than overall tumbling, picoseconds to nanoseconds. RDCs average over everything up to milliseconds. Chemical exchange, through line shapes, relaxation dispersion, CEST and exchange spectroscopy, covers microseconds to seconds, the time scales of catalysis, allostery, folding of small domains and binding (13.6.2, 13.6.4). Hydrogen exchange reports opening events from milliseconds to months (13.6.5), and real-time NMR follows slow folding and reactions directly. The idea that proteins are dynamic rather than rigid emerged in the 1970s from two directions at once: the first molecular dynamics simulation of a protein (BPTI, 9.2 ps in vacuum; McCammon, Gelin and Karplus, 1977) and NMR observations of ring flips of buried aromatic residues in BPTI, which require transient expansion of the core.

![Time scales of biomolecular motion (gray, upper rows) and the magnetic-resonance methods that report on them (colored, lower rows); ranges are approximate. DEER measures distance distributions in frozen samples, a snapshot of the ensemble rather than a rate](./plots/timescales.py)

### 13.6.2. Chemical Exchange

**Definition 13.6.1 (Chemical Exchange)** In NMR, *chemical exchange* is the interconversion of a nucleus between environments with different resonance frequencies, by a conformational change, a chemical reaction or binding. For two sites $\mathrm{A} \rightleftharpoons \mathrm{B}$ with rate constants $k_{\mathrm{AB}}$, $k_{\mathrm{BA}}$, the exchange rate is $k_{\mathrm{ex}} = k_{\mathrm{AB}} + k_{\mathrm{BA}}$ and the populations are $p_{\mathrm{A}} = k_{\mathrm{BA}}/k_{\mathrm{ex}}$, $p_{\mathrm{B}} = k_{\mathrm{AB}}/k_{\mathrm{ex}}$. With $\Delta\omega$ the difference of the two frequencies, exchange is slow if $k_{\mathrm{ex}} \ll \lvert\Delta\omega\rvert$, intermediate if $k_{\mathrm{ex}} \approx \lvert\Delta\omega\rvert$ and fast if $k_{\mathrm{ex}} \gg \lvert\Delta\omega\rvert$.

McConnell (1958) combined the Bloch equations with first-order kinetics.

**Formula 13.6.1 (Bloch–McConnell Equations)** The transverse magnetizations $m_{\mathrm{A}}$, $m_{\mathrm{B}}$ (complex, $M_x + \mathrm{i}M_y$) of the two sites obey

$$
\frac{\mathrm{d}}{\mathrm{d}t}\begin{bmatrix}m_{\mathrm{A}}\\ m_{\mathrm{B}}\end{bmatrix} = \begin{bmatrix}\mathrm{i}\Omega_{\mathrm{A}} - R_2 - k_{\mathrm{AB}} & k_{\mathrm{BA}}\\ k_{\mathrm{AB}} & \mathrm{i}\Omega_{\mathrm{B}} - R_2 - k_{\mathrm{BA}}\end{bmatrix}\begin{bmatrix}m_{\mathrm{A}}\\ m_{\mathrm{B}}\end{bmatrix} = L\begin{bmatrix}m_{\mathrm{A}}\\ m_{\mathrm{B}}\end{bmatrix}, \tag{13.26}
$$
so that the FID is $s(t) = \boldsymbol{1}^{\mathsf T}\mathrm{e}^{Lt}\boldsymbol{p}$ with $\boldsymbol{p} = (p_{\mathrm{A}}, p_{\mathrm{B}})^{\mathsf T}$, and the spectrum is $\operatorname{Re}\boldsymbol{1}^{\mathsf T}(\mathrm{i}\omega I - L)^{-1}\boldsymbol{p}$.

The eigenvalues of $L$ give the positions and widths of the observed lines, and the three regimes follow (Figure below). In slow exchange there are two lines at $\Omega_{\mathrm{A}}$ and $\Omega_{\mathrm{B}}$ with intensities $p_{\mathrm{A}}$ and $p_{\mathrm{B}}$, each broadened by the rate of leaving its site ($k_{\mathrm{AB}}$ or $k_{\mathrm{BA}}$ added to $R_2$). As $k_{\mathrm{ex}}$ rises the lines broaden, move towards each other and, for equal populations, merge at coalescence, $k_{\mathrm{ex}} = \lvert\Delta\omega\rvert/\sqrt2 = \sqrt2\,\pi\lvert\Delta\nu\rvert$. In fast exchange a single line appears at the population-weighted average $p_{\mathrm{A}}\Omega_{\mathrm{A}} + p_{\mathrm{B}}\Omega_{\mathrm{B}}$, with an exchange contribution to its width

$$
R_{\mathrm{ex}} = \frac{p_{\mathrm{A}}p_{\mathrm{B}}\Delta\omega^2}{k_{\mathrm{ex}}}, \tag{13.27}
$$
which decreases as exchange becomes faster: the motional narrowing of 13.3 in another guise. Temperature-dependent line shapes, which pass through these regimes, give $k_{\mathrm{ex}}$ and its activation energy; the classical example is the rotation about the partial double bond of an amide or the ring flips of Phe and Tyr in a protein core.

**Example 13.6.1 (Binding Titrations and Exchange)** For a protein P binding a ligand L in excess, $\mathrm{P} + \mathrm{L} \rightleftharpoons \mathrm{PL}$, the pseudo-first-order rates are $k_{\mathrm{AB}} = k_{\mathrm{on}}[\mathrm{L}]$ and $k_{\mathrm{BA}} = k_{\mathrm{off}}$, so $k_{\mathrm{ex}} = k_{\mathrm{on}}[\mathrm{L}] + k_{\mathrm{off}}$; at the midpoint of the titration $[\mathrm{L}] = K_{\mathrm{d}}$ and $k_{\mathrm{ex}} = 2k_{\mathrm{off}} = 2k_{\mathrm{on}}K_{\mathrm{d}}$. Association rates are near their diffusion-limited range ($k_{\mathrm{on}} \approx 10^7$–$10^8\,\mathrm{M^{-1}\,s^{-1}}$, [7.6.5](/7.6.5#sec-5.2.3)), so the regime is set essentially by the affinity. For a peak that shifts by $\Delta\nu = 100\,\mathrm{Hz}$ ($\lvert\Delta\omega\rvert = 630\,\mathrm{s^{-1}}$) and $k_{\mathrm{on}} = 10^8\,\mathrm{M^{-1}\,s^{-1}}$: a ligand with $K_{\mathrm{d}} = 100\,\mu\mathrm{M}$ gives $k_{\mathrm{ex}} = 2\times10^4\,\mathrm{s^{-1}}$, fast exchange, and the peak moves smoothly from the free to the bound position; $K_{\mathrm{d}} = 1\,\mu\mathrm{M}$ gives $200\,\mathrm{s^{-1}}$, slow exchange, and the free peak fades while the bound peak grows in place; in between, peaks broaden and may vanish near the midpoint. Weak binders are thus titrated by following shifts, tight binders by following intensities.

**Example 13.6.2 (Catalysis Seen as Exchange)** Cyclophilin catalyzes the cis–trans isomerization of prolyl peptide bonds, a slow step (minutes uncatalyzed) in the folding of many proteins. The model substrate succinyl-Ala-Ala-Pro-Phe-p-nitroanilide shows separate signals for its cis and trans forms, which interconvert too slowly to affect the spectrum. Adding a catalytic amount of cyclophilin accelerates the interconversion into the intermediate regime and broadens the signals; adding the inhibitor cyclosporin A, which blocks the active site, restores the sharp lines. Line shapes of this kind measure the turnover of an enzyme at equilibrium, without any change of concentrations.

![Two-site chemical exchange from the Bloch–McConnell equations (intrinsic R₂ = 10 s⁻¹). A: spectra for equal populations and Δν = 200 Hz as k_ex increases from slow exchange (two lines), through coalescence (k_ex = √2 πΔν = 888 s⁻¹), to fast exchange (one line at the average position). B: a titration in which the population of the bound state rises from 0 to 1 in the slow, intermediate and fast regimes: in slow exchange one peak fades and another grows, in fast exchange one peak moves, in intermediate exchange the peaks broaden almost beyond detection. C: CPMG relaxation dispersion for a minor state of 5 % with Δν = 150 Hz: the effective R₂ falls from R₂⁰ + R_ex towards R₂⁰ as the refocusing pulses become frequent enough to outrun the exchange; the shape of the curve depends on k_ex](./plots/exchange.py)

### 13.6.3. Model-Free Analysis and the Order Parameter

Relaxation rates of $^{15}\mathrm{N}$ (Formula 13.3.1) depend on the motion of each N–H bond, which consists of the tumbling of the whole molecule and of internal motions within it. If the two are independent and the internal motions are faster than tumbling, the correlation function factorizes, $C(t) = C_{\mathrm{O}}(t)C_{\mathrm{I}}(t)$ with $C_{\mathrm{O}} = \mathrm{e}^{-t/\tau_{\mathrm{m}}}$ for isotropic tumbling. The internal correlation function decays, but not to zero, because a bond attached to a folded protein cannot reach all orientations; it levels off at a plateau.

**Definition 13.6.2 (Generalized Order Parameter)** The *generalized order parameter* $S^2$ of a bond vector is the plateau of its internal correlation function, $S^2 = \lim_{t\to\infty}C_{\mathrm{I}}(t) = \frac{4\pi}{5}\sum_{m=-2}^{2}\lvert\langle Y_2^m(\boldsymbol{u})\rangle\rvert^2$, with $Y_2^m$ the second-order **spherical harmonics** and the average over the internal motion. It ranges from $1$ (a bond rigidly fixed in the molecular frame) to $0$ (a bond whose orientation is completely randomized by internal motion).

**Definition 13.6.3 (Model-Free Analysis)** *Model-free analysis* (Lipari and Szabo, 1982) interprets relaxation rates with the internal correlation function $C_{\mathrm{I}}(t) = S^2 + (1 - S^2)\mathrm{e}^{-t/\tau_{\mathrm{e}}}$, characterized by two parameters per bond, the order parameter $S^2$ (amplitude) and the effective internal correlation time $\tau_{\mathrm{e}}$ (speed), without assuming any physical model of the motion. The spectral density becomes

$$
J(\omega) = \frac25\left[\frac{S^2\tau_{\mathrm{m}}}{1 + \omega^2\tau_{\mathrm{m}}^2} + \frac{(1 - S^2)\tau}{1 + \omega^2\tau^2}\right], \qquad \frac1\tau = \frac{1}{\tau_{\mathrm{m}}} + \frac{1}{\tau_{\mathrm{e}}}. \tag{13.28}
$$

With $R_1$, $R_2$ and NOE measured for $n$ residues (preferably at two fields), there are $3n$ data for $2n + 1$ parameters ($S^2$ and $\tau_{\mathrm{e}}$ per residue, and $\tau_{\mathrm{m}}$; four more for anisotropic tumbling), and a fit by **least squares** with model selection (adding $R_{\mathrm{ex}}$ or a second, slower internal motion where needed) gives a profile of $S^2$ along the sequence. The parameters have a simple meaning: for a bond wobbling uniformly in a cone of semi-angle $\theta_0$, $S^2 = [\frac12\cos\theta_0(1 + \cos\theta_0)]^2$, so $S^2 = 0.85$, the typical value of backbone amides in helices and sheets, corresponds to $\theta_0 \approx 19^\circ$, and values below $0.6$ mark flexible loops and termini. The analysis can also be run in reverse, from a molecular dynamics trajectory: superimposing all frames on the first removes the tumbling, the $P_2$ correlation function of each N–H vector gives $C_{\mathrm{I}}(t)$ directly, and comparison of computed and measured $S^2$ tests the force field.

Because $S^2$ measures the width of the distribution of bond orientations, it is related to the conformational entropy of the residue. Changes of side-chain methyl order parameters on binding, measured for calmodulin and other proteins by Wand, Kay and coworkers, show that conformational entropy contributes to binding free energies by amounts comparable to those measured by calorimetry ([7.6.8](/7.6.8)), and that ligands can couple distant sites by changing fluctuations rather than average structure, a form of allostery ([7.6.4](/7.6.4)). The analysis fails, and should not be used, when internal and overall motions are not separable: for intrinsically disordered proteins, for which spectral density mapping (estimating $J(0)$, $J(\omega_{\mathrm{N}})$ and $J(0.87\omega_{\mathrm{H}})$ directly from the rates) or comparison with simulation is preferred, and for flexible multidomain proteins whose domains reorient on the time scale of tumbling.

### 13.6.4. Relaxation Dispersion, CEST and ZZ Exchange

A protein at equilibrium often spends a few percent of its time in a higher-energy conformation: a substrate-binding state, an intermediate of folding, a state on the path of an allosteric transition. These excited states are invisible in the spectrum, because their peaks are weak and broadened, but their exchange with the ground state leaves a trace on the ground-state signals.

**Definition 13.6.4 (Relaxation Dispersion)** *Relaxation dispersion* is the dependence of the effective transverse relaxation rate on the rate of refocusing, in CPMG experiments on the spacing $\tau_{\mathrm{cp}}$ of the $180^\circ$ pulses (expressed as $\nu_{\mathrm{CPMG}} = 1/(2\tau_{\mathrm{cp}})$), or in $R_{1\rho}$ experiments on the strength of a continuous spin-lock field. It arises from exchange on the microsecond-to-millisecond time scale: if pulses refocus the magnetization before a nucleus jumps between sites, the dephasing caused by the jump is suppressed.

At low $\nu_{\mathrm{CPMG}}$ the effective rate is $R_2^0 + R_{\mathrm{ex}}$; at high $\nu_{\mathrm{CPMG}}$ the exchange contribution is quenched and $R_{2,\mathrm{eff}} \to R_2^0$. For fast exchange the curve has the Luz–Meiboom form

$$
R_{2,\mathrm{eff}}(\nu_{\mathrm{CPMG}}) = R_2^0 + \frac{p_{\mathrm{A}}p_{\mathrm{B}}\Delta\omega^2}{k_{\mathrm{ex}}}\left[1 - \frac{4\nu_{\mathrm{CPMG}}}{k_{\mathrm{ex}}}\tanh\frac{k_{\mathrm{ex}}}{4\nu_{\mathrm{CPMG}}}\right], \tag{13.29}
$$
and for general exchange it is computed exactly from the Bloch–McConnell equations (Carver–Richards formula, or numerical propagation as in panel C of the figure of 13.6.2). Fitting dispersion curves of many residues, at two fields, gives $k_{\mathrm{ex}}$, the population $p_{\mathrm{B}}$ of the excited state and, for each nucleus, $\lvert\Delta\omega\rvert$, which is the chemical shift of the invisible state relative to the ground state. Since chemical shifts encode structure (13.4.1), the shifts of excited states have been used to determine their structures, for folding intermediates and for minor conformations of RNA in which base pairs shift register. Applied to the enzyme dihydrofolate reductase and to cyclophilin, relaxation dispersion showed that the enzyme samples conformations resembling the next state of its catalytic cycle even in the absence of the ligand, at rates comparable to turnover (Eisenmesser, Kern and coworkers, 2002–2005; Boehr, Wright and coworkers, 2006). CPMG covers $k_{\mathrm{ex}}$ of about $50$–$5000\,\mathrm{s^{-1}}$, $R_{1\rho}$ up to about $10^5\,\mathrm{s^{-1}}$; the sign of $\Delta\omega$, lost in CPMG, is obtained by comparing shifts at two fields or from $R_{1\rho}$.

For slower exchange ($k_{\mathrm{ex}} \approx 20$–$300\,\mathrm{s^{-1}}$), *chemical exchange saturation transfer* (CEST) applies a weak radiofrequency field for a few hundred milliseconds at a series of offsets: when it hits the frequency of the invisible state, the saturation is carried to the ground state by exchange and the ground-state peak loses intensity, so a plot of intensity against offset shows a dip at the position of the invisible peak. For still slower exchange (hundreds of milliseconds to seconds) between states that are both visible, ZZ-exchange spectroscopy lets longitudinal magnetization exchange during a mixing time and shows cross peaks between the two positions whose growth gives the rates.

### 13.6.5. Hydrogen–Deuterium Exchange

Amide protons exchange with the protons of water, catalyzed by $\mathrm{OH^-}$ (and, below pH 3, by $\mathrm{H^+}$). In an unstructured peptide the intrinsic rate $k_{\mathrm{int}}$ is about $1$–$10\,\mathrm{s^{-1}}$ at pH 7 and $25\,{}^\circ\mathrm{C}$, rises tenfold per pH unit above its minimum near pH $2.5$–$3$, and depends on the neighboring side chains and on temperature in a way that has been calibrated (Bai, Englander and coworkers, 1993). In a folded protein most amides are hydrogen bonded or buried and exchange only when a fluctuation breaks the hydrogen bond and exposes them.

**Definition 13.6.5 (Hydrogen–Deuterium Exchange)** *Hydrogen–deuterium exchange* (HDX) is the replacement of exchangeable hydrogens of a macromolecule, mainly backbone amide hydrogens, by deuterium from $\mathrm{D_2O}$ (or the reverse). In the Linderstrøm-Lang model an amide exchanges only from an open state,

$$
\text{closed (NH)} \underset{k_{\mathrm{cl}}}{\overset{k_{\mathrm{op}}}{\rightleftharpoons}} \text{open (NH)} \overset{k_{\mathrm{int}}}{\longrightarrow} \text{open (ND)}, \qquad k_{\mathrm{obs}} = \frac{k_{\mathrm{op}}k_{\mathrm{int}}}{k_{\mathrm{op}} + k_{\mathrm{cl}} + k_{\mathrm{int}}}. \tag{13.30}
$$

**Definition 13.6.6 (Protection Factor)** The *protection factor* of an amide is $P = k_{\mathrm{int}}/k_{\mathrm{obs}}$, the factor by which the structure slows its exchange.

Two limits make Eq. (13.30) useful. When the structure recloses much faster than the chemical step, $k_{\mathrm{cl}} \gg k_{\mathrm{int}}$ (the usual case under native conditions, the EX2 regime), each opening gives only a small chance of exchange, and $k_{\mathrm{obs}} = K_{\mathrm{op}}k_{\mathrm{int}}$ with $K_{\mathrm{op}} = k_{\mathrm{op}}/k_{\mathrm{cl}} \ll 1$: the protection factor measures the equilibrium constant of opening,

$$
\Delta G_{\mathrm{op}} = -RT\ln K_{\mathrm{op}} = RT\ln P \qquad (\text{EX2}). \tag{13.31}
$$
When the chemical step is faster than reclosing, $k_{\mathrm{int}} \gg k_{\mathrm{cl}}$ (at high pH or with destabilized proteins, the EX1 regime), every opening leads to exchange and $k_{\mathrm{obs}} = k_{\mathrm{op}}$: the rate of the opening reaction itself. The two regimes are distinguished by the pH dependence: in EX2 $k_{\mathrm{obs}}$ follows $k_{\mathrm{int}}$ and rises tenfold per pH unit, in EX1 it is pH independent.

The free energies are large: a protection factor of $10^6$ corresponds to $34\,\mathrm{kJ\,mol^{-1}}$ at $298\,\mathrm{K}$, and the most protected amides of a stable protein exchange over weeks to months. For these slowest amides, $\Delta G_{\mathrm{op}}$ equals the free energy of global unfolding measured by denaturation ([7.6.8](/7.6.8)); others exchange through local fluctuations or subglobal unfolding of cooperative units. Measuring $\Delta G_{\mathrm{op}}$ residue by residue at increasing denaturant concentration led Englander and coworkers to the picture of folding through partially unfolded forms built from cooperative units, foldons, first for cytochrome $c$ ([7.6.16](/7.6.16)).

In NMR, HDX is measured by dissolving a protonated protein in $\mathrm{D_2O}$ and recording HSQC spectra over time (amides that become ND disappear), or, for faster exchange, by magnetization transfer from water (CLEANEX and related saturation-transfer methods), or by pulse-labeling during folding (quench-flow) followed by NMR of the refolded protein. In mass spectrometry (HDX-MS, [6.4.15](/6.4.15)), the protein is labeled in $\mathrm{D_2O}$ for a time, the exchange is quenched by lowering to pH 2.5 and $0\,{}^\circ\mathrm{C}$ (which slows it about $10^4$-fold), the protein is digested by pepsin and the mass increase of each peptide is measured. HDX-MS has lower resolution (peptides of 5–20 residues) but no size limit, and distinguishes the regimes directly from the isotope envelopes: EX2 shifts the envelope gradually, EX1 gives a bimodal envelope of unexchanged and fully exchanged molecules. It is widely used to map epitopes, ligand binding and conformational changes of large complexes and membrane proteins.

![Hydrogen–deuterium exchange in the Linderstrøm-Lang model. A: k_obs as the intrinsic rate is raised by raising the pH, for a site with k_op = 1 s⁻¹ and k_cl = 10³ s⁻¹ (ΔG_op = 17 kJ/mol): EX2 (k_obs = K_op k_int) while k_int ≪ k_cl, EX1 (k_obs = k_op) when k_int ≫ k_cl. B: fraction of amide ¹H remaining in D₂O for protection factors 1 to 10⁶ (k_int = 10 s⁻¹) and the corresponding opening free energies RT ln P. C: simulated mass spectra of a peptide with 12 exchangeable amides after labeling for 1, 10 and 100 s: in EX2 each amide exchanges independently and the envelope shifts; in EX1 the segment exchanges in one cooperative opening, and unexchanged and fully exchanged populations coexist](./plots/hdx.py)

## 13.7. Electron Paramagnetic Resonance

### 13.7.1. Electron Spin Resonance

**Electron paramagnetic resonance** ([6.5.7](/6.5.7#def-7.4.1)) is the magnetic resonance of unpaired electrons, with the resonance condition $h\nu = g\mu_{\mathrm{B}}B$ in which $\mu_{\mathrm{B}}$ is the **Bohr magneton** and the $g$ value ($2.0023$ for the free electron) is shifted by spin–orbit coupling and plays the part of the chemical shift. Because the electron's moment is 658 times the proton's, the resonance lies in the microwave region: commercial spectrometers fix the frequency of a resonant cavity and sweep the field.

| Band | L | S | X | Q | W |
|---|---|---|---|---|---|
| $\nu/\mathrm{GHz}$ | 1.5 | 3.0 | 9.5 | 34 | 95 |
| resonance field for $g = 2.0023$ / mT | 54 | 107 | 339 | 1213 | 3390 |

The X band is the workhorse; Q and W bands resolve $g$ anisotropy better and are used for pulsed experiments. Spectra are recorded with field modulation and appear as the first derivative of the absorption. The electron polarization at $0.34\,\mathrm{T}$ and $298\,\mathrm{K}$ is $7.7\times10^{-4}$, sixteen times that of protons at $14.1\,\mathrm{T}$, and the much larger moment makes EPR sensitive to micromolar concentrations of spins. Unpaired electrons interact with nearby magnetic nuclei by **hyperfine coupling** ([6.5.7](/6.5.7#def-7.4.2)), which splits lines into $2nI + 1$ components; relaxation times are microseconds rather than seconds, which is why pulsed EPR works on a nanosecond time scale and usually at cryogenic temperature.

Biological samples contain native paramagnetic centers: the iron–sulfur clusters, copper sites, flavin and quinone semiquinones and tyrosyl radicals of electron-transfer chains and enzymes, studied by EPR since the 1960s ([7.1.23](/7.1.23) and [7.1.24](/7.1.24) for the respiratory and photosynthetic chains); the tyrosyl radical of ribonucleotide reductase; and free radicals and reactive oxygen species, which are detected by **spin trapping** ([6.5.7](/6.5.7)). Most macromolecules, however, are diamagnetic, and the general use of EPR in structural biology rests on attaching a paramagnetic label.

### 13.7.2. Site-Directed Spin Labeling

**Definition 13.7.1 (Site-Directed Spin Labeling)** *Site-directed spin labeling* (SDSL; Hubbell and coworkers, from 1989) is the covalent attachment of a stable paramagnetic group, a spin label, to a chosen site of a macromolecule, so that EPR reports on its local environment, mobility and distances to other labels.

A good spin label is small, stable, attached specifically with minimal perturbation, and has a simple spectrum that is sensitive to its environment. The standard is the nitroxide MTSL, which reacts with the thiol of a cysteine: native solvent-exposed cysteines are removed by mutation, and a cysteine is introduced at each site of interest, one site at a time, in a "cysteine scan". The resulting side chain, called R1, has a flexible linker of five bonds, which places the electron $0.6$–$0.8\,\mathrm{nm}$ from the backbone and adds a few tenths of a nanometer of uncertainty to distances. Alternatives include rigid labels (the bifunctional RX label tethered to two cysteines, or the double-histidine motif $i, i+4$ in a helix chelating Cu²⁺), Gd³⁺ chelates, which are stable in the reducing interior of cells and are well suited to high-field EPR, trityl radicals, which have long relaxation times at room temperature, and labels introduced as unnatural amino acids or, for RNA, during chemical synthesis or by modified nucleotides.

### 13.7.3. Nitroxide Spectra and Mobility

The unpaired electron of a nitroxide sits mainly in a $\pi$ orbital of the N–O group and couples to the $^{14}\mathrm{N}$ nucleus ($I = 1$), so the spectrum consists of three lines, $m_I = +1, 0, -1$, separated by the isotropic hyperfine coupling $a \approx 1.5\,\mathrm{mT}$. Both the $g$ value and the hyperfine coupling are anisotropic (axial approximately: $A_\parallel \approx 3.5\,\mathrm{mT}$ along the $\pi$ orbital, $A_\perp \approx 0.6\,\mathrm{mT}$; $g_\parallel \approx 2.0027$, $g_\perp \approx 2.0075$), and the anisotropy is averaged by motion exactly as in NMR, but on a time scale set by the anisotropy itself, $(A_\parallel - A_\perp)\gamma_{\mathrm{e}} \approx 5\times10^8\,\mathrm{s^{-1}}$, so that X-band nitroxide spectra are sensitive to rotational correlation times from $0.1$ to about $100\,\mathrm{ns}$:

- for $\tau_{\mathrm{c}} \lesssim 0.1\,\mathrm{ns}$ (a free label in water) the three lines are narrow and nearly equal;
- for $\tau_{\mathrm{c}}$ of about $0.5$–$2\,\mathrm{ns}$ the lines broaden unequally, the high-field line most, because the line width depends on $m_I$ as $A + Bm_I + Cm_I^2$ with $B$ and $C$ proportional to $\tau_{\mathrm{c}}$ (the motional-narrowing theory of Kivelson);
- for slower motion the spectrum changes shape gradually towards the rigid-limit "powder" spectrum of randomly oriented immobile labels, whose outer extrema are separated by about $2A_\parallel$; this region requires the stochastic Liouville equation of Freed for its simulation; saturation-transfer EPR extends the sensitive range to milliseconds.

For a label attached to a protein the effective $\tau_{\mathrm{c}}$ reflects the motion of the side chain relative to the backbone more than the tumbling of the whole protein (which is slowed, when necessary, by sucrose or Ficoll). The mobility thus distinguishes sites on loops (mobile), on helix surfaces (intermediate) and at tertiary contacts or buried positions (immobilized), and the periodicity of mobility along a cysteine scan reveals helices (period 3.6) and strands (period 2). The accessibility of each site to paramagnetic relaxers, $\mathrm{O_2}$ (soluble in membranes) and $\mathrm{NiEDDA}$ (water soluble), measured by power saturation, tells whether it faces lipid or water: SDSL mapped the topology and the conformational changes of membrane proteins such as rhodopsin, the potassium channel KcsA and transporters long before high-resolution structures were available.

![X-band (9.5 GHz) cw-EPR of a nitroxide spin label. A: electron Zeeman levels split by the hyperfine coupling to ¹⁴N (I = 1); the three allowed transitions (Δm_S = ±1, Δm_I = 0) give three lines separated by a. B: first-derivative spectra in the fast-motion regime (τc = 0.1, 0.5 and 1.5 ns, line widths from the motional-narrowing expression for axial g and A tensors; the high-field line broadens most) and in the rigid limit (powder spectrum of immobilized labels, outer extrema separated by about 2A∥). The intermediate regime, 2–100 ns, needs the stochastic Liouville equation and is not computed](./plots/nitroxide.py)

### 13.7.4. Distances by DEER

Two electron spins at distance $r$ interact through their dipolar fields.

**Formula 13.7.1 (Electron–Electron Dipolar Coupling)** For two spins with $g \approx 2.0023$ whose connecting vector makes the angle $\theta$ with $\boldsymbol{B}_0$, in the weak-coupling limit,

$$
\nu_{\mathrm{dd}}(r, \theta) = \frac{\mu_0g_{\mathrm{A}}g_{\mathrm{B}}\mu_{\mathrm{B}}^2}{4\pi h}\,\frac{1}{r^3}\,(3\cos^2\theta - 1) = \frac{52.04\,\mathrm{MHz\,nm^3}}{r^3}\,(3\cos^2\theta - 1). \tag{13.32}
$$

For $r = 3\,\mathrm{nm}$ the perpendicular frequency $\nu_\perp = 52.04/27\,\mathrm{MHz} = 1.93\,\mathrm{MHz}$; in a frozen, randomly oriented sample the distribution of $\theta$ produces a Pake pattern with horns at $\pm\nu_\perp$ and edges at $\pm2\nu_\perp$. Below about $1.5$–$2\,\mathrm{nm}$ the coupling broadens the continuous-wave spectrum visibly and can be extracted from line shapes; above that it is hidden in the inhomogeneous width of the spectrum and must be isolated by a pulse experiment.

**Definition 13.7.2 (Double Electron–Electron Resonance)** *Double electron–electron resonance* (DEER, also called pulsed electron–electron double resonance, PELDOR) measures the dipolar coupling between electron spins by a spin-echo sequence on one set of spins (the observer frequency) during which a pump pulse at a second frequency inverts the partner spins at a variable time $t$; the inversion changes the local field at the observed spins by the dipolar field and modulates the refocused echo as a function of $t$. In the four-pulse version (Pannier, Jeschke and coworkers, 2000) the sequence is $\frac\pi2 - \tau_1 - \pi - (\tau_1 + t) - \pi_{\mathrm{pump}} - (\tau_2 - t) - \pi - \tau_2 - \text{echo}$, which gives a dead-time-free signal starting at $t = 0$.

The DEER signal of a sample of doubly labeled molecules is

$$
V(t) = \left[(1 - \lambda) + \lambda\int_0^\infty P(r)K(t, r)\,\mathrm{d}r\right]B(t), \qquad K(t, r) = \int_0^1\cos\left[(3x^2 - 1)\,2\pi\nu_\perp(r)t\right]\mathrm{d}x, \tag{13.33}
$$
where $P(r)$ is the distribution of distances, the kernel $K$ averages the dipolar oscillation over orientations ($x = \cos\theta$), $\lambda$ is the fraction of partner spins inverted by the pump pulse (the modulation depth, $0.3$–$0.5$ for nitroxides), and $B(t)$ is the background from spins in other molecules, $\exp[-(kt)^{d/3}]$ with $d = 3$ for a homogeneous solution. Recovering $P(r)$ from $V(t)$ is an ill-posed inverse problem of the same kind as the indirect Fourier transform of SAXS ([7.6.9](/7.6.9#sec-9.10.4)): small noise in $V$ produces large oscillations in $P$, and the solution is stabilized by Tikhonov regularization, minimizing $\lVert KP - V\rVert^2 + \alpha^2\lVert LP\rVert^2$ with $L$ a second-derivative operator and $P \ge 0$, with the regularization parameter $\alpha$ chosen by the L-curve or by a statistical criterion. Programs: DeerAnalysis, DeerLab, and neural-network methods (DEERNet).

The measurable range is about $1.8$–$6\,\mathrm{nm}$, set at the lower end by the bandwidth of the pulses (dipolar frequencies above about $10\,\mathrm{MHz}$ are not excited) and at the upper end by the dipolar evolution time that the phase memory time of the electrons allows: to determine a mean distance $r$, the trace must last about $2\,\mu\mathrm{s}\times(r/5\,\mathrm{nm})^3$, and to determine the width of the distribution about twice as long. Deuteration of the protein and the solvent lengthens the phase memory time and extends the range to $8$–$10\,\mathrm{nm}$ and, in favorable cases, beyond. Samples are frozen at $50$–$80\,\mathrm{K}$ in glass-forming buffers (with glycerol), so the distribution is a snapshot of the conformational ensemble at the freezing temperature; sample sizes are tens of microliters at $10$–$100\,\mu\mathrm{M}$, and there is no upper limit on molecular size. The distance between the spin labels is not the distance between backbone atoms: rotamer libraries of the label side chain (MMM, chiLife) are used to translate the measured distribution into a structural restraint.

**Example 13.7.1 (Biased Agonists of a GPCR)** DEER distance distributions between pairs of spin labels on the cytoplasmic side of the angiotensin II type 1 receptor, a G-protein-coupled receptor, measured with ligands of different efficacy, showed that the receptor populates several conformations whose relative populations depend on the ligand, rather than switching between a single inactive and a single active structure; ligands that bias signaling towards G proteins or towards β-arrestin stabilize different sets of conformations (Wingler and coworkers, 2019). Distance distributions of this kind reveal conformational equilibria that a single structure cannot show.

**Example 13.7.2 (In-Cell EPR)** RNA duplexes labeled with reduction-resistant nitroxides and microinjected into *Xenopus laevis* oocytes gave DEER distance distributions slightly shorter than in buffer, close to those measured in concentrated protein solutions, consistent with a modest compaction by crowding ([7.6.23](/7.6.23)) (Collauto and coworkers, 2020). Gd³⁺ and trityl labels, which survive the reducing environment of the cytoplasm, have made such in-cell measurements increasingly common.

![DEER from a distance distribution to the time trace and back. A: a mixture of two conformations at 3.0 nm (60 %) and 4.2 nm (40 %) and the distribution recovered by Tikhonov regularization with a second-derivative penalty and non-negativity. B: the simulated trace V(t) with modulation depth 0.35, a homogeneous background and noise (gray), the background-corrected form factor (purple) with the fit (orange), and the dipolar oscillation of a single 3.0 nm pair (offset). C: the Pake pattern of the 3.0 nm pair, the orientationally averaged dipolar spectrum, with horns at ν⊥ = 1.93 MHz and edges at 2ν⊥](./plots/deer.py)

### 13.7.5. Dynamic Nuclear Polarization

Since an electron is polarized 658 times more strongly than a proton in the same field, transferring electron polarization to nuclei could raise the NMR signal by up to that factor. This was Overhauser's prediction of 1953, verified in metals by Carver and Slichter the same year.

**Definition 13.7.3 (Dynamic Nuclear Polarization)** *Dynamic nuclear polarization* (DNP) is the transfer of the large polarization of electron spins to nuclear spins by microwave irradiation near the electron resonance, through the hyperfine or dipolar coupling between them, increasing the nuclear polarization by up to the ratio $\gamma_{\mathrm{e}}/\gamma_{\mathrm{H}} \approx 658$.

In modern magic-angle-spinning DNP, samples doped with stable biradicals are frozen near $100\,\mathrm{K}$ and irradiated by a gyrotron at the electron frequency ($263$–$527\,\mathrm{GHz}$ at $400$–$800\,\mathrm{MHz}$ proton frequency); enhancements of $20$–$200$ make it possible to study proteins at low concentration, in membranes and in cells. In dissolution DNP, a sample polarized at about $1\,\mathrm{K}$ is rapidly dissolved and injected; the hyperpolarized $^{13}\mathrm{C}$ of pyruvate, imaged within a minute before the polarization relaxes, displays the conversion of pyruvate to lactate in tumors in patients, an application to metabolic imaging (13.8).

## 13.8. Magnetic Resonance Imaging

### 13.8.1. Spatial Encoding

**Magnetic resonance imaging** ([6.4.12](/6.4.12#def-12.6.3)) uses the protons of water (about $80\,\mathrm{M}$ in soft tissue) and of fat. In a homogeneous field all water protons resonate at the same frequency; a linear field gradient makes the frequency depend on position,

$$
\omega(\boldsymbol{x}) = \gamma\left(B_0 + \boldsymbol{G}\cdot\boldsymbol{x}\right) \tag{13.34}
$$
(in magnitude), so that the spectrum recorded under a gradient $G_x$ is the projection of the proton density onto $x$. Lauterbur's first images (1973) reconstructed an object from projections at many angles, the method of computed tomography. Modern MRI encodes position in phase and frequency and reconstructs by Fourier transform.

**Theorem 13.8.1 (k-Space)** After the spins of a slice with density $\rho(\boldsymbol{x})$ are excited, the signal recorded while gradients $\boldsymbol{G}(t)$ are applied is, in the rotating frame and ignoring relaxation,

$$
s(t) = \int\rho(\boldsymbol{x})\,\mathrm{e}^{-\mathrm{i}2\pi\boldsymbol{k}(t)\cdot\boldsymbol{x}}\,\mathrm{d}\boldsymbol{x}, \qquad \boldsymbol{k}(t) = \frac{\gamma}{2\pi}\int_0^t\boldsymbol{G}(t')\,\mathrm{d}t'. \tag{13.35}
$$
The signal is the two-dimensional Fourier transform of the image, evaluated along the trajectory $\boldsymbol{k}(t)$ that the gradient waveform traces in k-space.

**Proof** A spin at $\boldsymbol{x}$ accumulates, relative to the transmitter at $\gamma B_0$, the phase $\int_0^t\gamma\boldsymbol{G}(t')\cdot\boldsymbol{x}\,\mathrm{d}t' = 2\pi\boldsymbol{k}(t)\cdot\boldsymbol{x}$ (with the sign of precession absorbed in the convention), and the coil sums the contributions of all spins weighted by their density. $\square$

An imaging sequence therefore steers $\boldsymbol{k}$ through k-space. In the standard spin-warp sequence, a slice is selected by a shaped radiofrequency pulse applied with a gradient $G_z$: only spins whose frequency lies within the pulse bandwidth $\Delta f$ are excited, a slice of thickness $\Delta z = 2\pi\Delta f/(\gamma G_z)$ (with $\gamma/2\pi = 42.58\,\mathrm{MHz\,T^{-1}}$, $\Delta f = 1\,\mathrm{kHz}$ and $G_z = 10\,\mathrm{mT\,m^{-1}}$, $\Delta z = 2.3\,\mathrm{mm}$). A phase-encoding gradient $G_y$ applied briefly sets $k_y$; the signal is then read out under a constant frequency-encoding gradient $G_x$, which sweeps $k_x$ along a line; the sequence is repeated for each $k_y$, and the two-dimensional inverse FFT gives the image. The sampling of k-space sets the image: the field of view is $1/\Delta k$ and the resolution $1/(2k_{\max})$, so a coarse sampling of k-space folds the image (aliasing) and truncating its outer part blurs it (Figure below). Echo-planar imaging covers the whole of k-space in one excitation in about $50\,\mathrm{ms}$; parallel imaging with arrays of receiver coils and compressed sensing reconstruct images from undersampled k-space, shortening scans several-fold.

### 13.8.2. Contrast

The proton density differs little between soft tissues, but $T_1$ and $T_2$ differ greatly, because water in tissues exchanges with water bound to macromolecules and its relaxation reflects the local composition. In a spin-echo sequence with repetition time TR and echo time TE,

$$
S = \rho\left(1 - \mathrm{e}^{-\mathrm{TR}/T_1}\right)\mathrm{e}^{-\mathrm{TE}/T_2}. \tag{13.36}
$$
Short TR and short TE give $T_1$-weighted images (white matter, with short $T_1$, bright; cerebrospinal fluid dark); long TR and long TE give $T_2$-weighted images (fluid bright), in which edema and many lesions stand out. Contrast agents are Gd³⁺ chelates that shorten the $T_1$ of nearby water by the paramagnetic relaxation enhancement of 13.5.4, making perfused tissue and leaky vessels bright. Other contrasts are physiological. In diffusion-weighted imaging, a pair of strong gradient pulses dephases and rephases spins, and molecules that move between them leave a signal attenuated as $S = S_0\mathrm{e}^{-bD}$ (the Stejskal–Tanner relation, with $b = \gamma^2G^2\delta^2(\Delta - \delta/3)$ for gradient pulses of length $\delta$ separated by $\Delta$): a direct measurement of the **diffusion coefficient** of water ([7.6.5](/7.6.5)), whose drop within minutes signals an ischemic stroke and whose directional dependence traces nerve fiber tracts. In functional MRI, deoxygenated hemoglobin is paramagnetic, and the local increase of blood oxygenation that follows neural activity lengthens $T_2^*$ and raises the signal by about 1 % (the blood-oxygen-level-dependent, BOLD, contrast).

Clinical scanners work at $1.5$ and $3\,\mathrm{T}$ (proton frequencies $64$ and $128\,\mathrm{MHz}$), research scanners at $7\,\mathrm{T}$ and above, with gradients of $40$–$80\,\mathrm{mT\,m^{-1}}$; the absence of ionizing radiation and the soft-tissue contrast make MRI the method of choice for the brain, the spinal cord, joints and many tumors. The same physics, at much higher gradients, gives MR microscopy and the measurement of diffusion in NMR tubes, used to determine the hydrodynamic radii of proteins (DOSY).

![Spatial encoding and contrast in MRI with a 128 × 128 numerical phantom. A: the phantom, T₁-weighted (TR = 0.5 s, TE = 15 ms). B: under a linear gradient the spectrum of the slice is its projection onto x. C: k-space on a logarithmic scale; the recorded signal is the Fourier transform of the image. D: the inverse transform of the central 32 × 32 points of k-space only, a blurred image. E: every second phase-encoding line omitted: the field of view halves and the image folds over. F: spin-echo signal at TR = 3 s against TE for white matter, gray matter and CSF (approximate values at 1.5 T): long TE gives T₂ weighting in which CSF is bright](./plots/mri.py)

## 13.9. Magnetic Resonance among the Structural Methods

| | Solution NMR | Solid-state NMR | EPR (DEER) | X-ray crystallography | Cryo-EM |
|---|---|---|---|---|---|
| sample | $0.1$–$1\,\mathrm{mM}$, $0.3\,\mathrm{mL}$, isotope labeled | mg of solid, fibril or proteoliposome | $10$–$100\,\mu\mathrm{M}$, $20\,\mu\mathrm{L}$, spin labeled | crystals | $\sim1\,\mu\mathrm{M}$, $3\,\mu\mathrm{L}$, vitrified |
| size | best $< 30\,\mathrm{kDa}$; dynamics to $\sim1\,\mathrm{MDa}$ with methyl-TROSY | no limit in principle | no limit | no limit if it crystallizes | best $> 50\,\mathrm{kDa}$ |
| information | atomic restraints, ensembles, dynamics ps–months, weak binding | atomic structure of insoluble assemblies | distance distributions $1.8$–$10\,\mathrm{nm}$ | atomic structure, one dominant state | atomic structure, several states |
| strength | flexibility, disorder, minor states, solution conditions | amyloids, membrane proteins in bilayers | large and membrane proteins, in cells | precision, ligands | large complexes, heterogeneity |

The methods are complementary rather than competing. A typical modern study combines a structure from crystallography, cryo-EM or prediction with NMR measurements of its dynamics and minor states, DEER distributions of its conformational equilibria in membranes, and SAXS of its overall shape in solution ([7.6.9](/7.6.9#sec-9.14)), in an integrative model ([7.6.15](/7.6.15)). The particular contributions of magnetic resonance are the ones that no picture can give: populations and rates of interconversion, amplitudes of motion, and the structural ensembles of molecules that have no single structure.

## Summary

- Spins and sensitivity. $\boldsymbol{\mu} = \gamma\boldsymbol{I}$; Zeeman levels $E_m = -\gamma\hbar B_0m$; Larmor frequency $\omega_0 = -\gamma B_0$ (Definition 13.1.1; $600\,\mathrm{MHz}$ for $^1\mathrm{H}$ at $14.1\,\mathrm{T}$). Polarization $\hbar\gamma B_0/2k_{\mathrm{B}}T \approx 5\times10^{-5}$; Curie magnetization $M_0 \propto N\gamma^2B_0/T$ (Formula 13.1.1); $S/N \propto N\gamma_{\mathrm{exc}}\gamma_{\mathrm{det}}^{3/2}B_0^{3/2}\sqrt{n_{\mathrm{s}}}$, hence proton excitation and detection. Spin-1/2 nuclei ($^1\mathrm{H}$, $^{13}\mathrm{C}$, $^{15}\mathrm{N}$, $^{19}\mathrm{F}$, $^{31}\mathrm{P}$) by isotope labeling; $^{17}\mathrm{O}$ has $I = 5/2$.
- Bloch equations (Theorem 13.2.1, Definitions 13.2.1–13.2.2): precession about $\boldsymbol{B}$; in the rotating frame a pulse of angle $\beta = \gamma B_1t_{\mathrm{p}}$ about $B_1$; $T_1$ recovery of populations, $T_2$ loss of phase coherence, $T_2 \le 2T_1$. FID and Lorentzian lines of width $1/(\pi T_2)$ with constant area (Formula 13.2.1). The spin echo (Definition 13.2.3) refocuses static dephasing; CPMG and inversion recovery measure $T_2$ and $T_1$.
- Relaxation and motion. Spectral density $J(\omega) = \frac25\tau_{\mathrm{c}}/(1 + \omega^2\tau_{\mathrm{c}}^2)$ (Definition 13.3.1), $\tau_{\mathrm{c}} \approx 0.5$–$0.6\,\mathrm{ns/kDa}$. BPP (Theorem 13.3.1): $T_1$ minimum at $\omega_0\tau_{\mathrm{c}} = 0.62$, $T_2 \propto 1/\tau_{\mathrm{c}}$ through $J(0)$: the size limit. $^{15}\mathrm{N}$ $R_1$, $R_2$, NOE (Formula 13.3.1). Deuteration, TROSY (Definition 13.3.2), methyl-TROSY, $^{19}\mathrm{F}$, solid-state NMR.
- Spectra. Shift ranges, folded vs disordered dispersion, imino protons of base pairs, secondary shifts; Karplus relation $^3J(\mathrm{H}^{\mathrm{N}},\mathrm{H}^\alpha) = 6.51\cos^2\theta - 1.76\cos\theta + 1.60\,\mathrm{Hz}$ (Formula 13.4.1). Density operator, $\mathrm{d}\hat\rho/\mathrm{d}t = -\mathrm{i}[\hat{H}, \hat\rho]$ (Definition 13.4.1), product operators; HSQC by INEPT (Example 13.4.1); COSY, TOCSY, NOESY, triple-resonance assignment; chemical shift perturbation (Definition 13.4.2).
- Restraints and structures. NOE: cross-relaxation $\sigma \propto r^{-6}[6j(2\omega_0) - j(0)]$, sign change at $\omega_0\tau_{\mathrm{c}} = 1.12$, distances to $0.5\,\mathrm{nm}$, spin diffusion (Formula 13.5.1). RDC $D = -\frac{\mu_0\gamma_I\gamma_S\hbar}{8\pi^2r^3}\langle3\cos^2\theta - 1\rangle$, global orientations, sign reversed for N–H (Definition 13.5.1, Remark 13.5.1). PRE ($r^{-6}$, to $3\,\mathrm{nm}$) and PCS ($r^{-3}$, to $5\,\mathrm{nm}$) (Definitions 13.5.2–13.5.3). Simulated annealing to an ensemble (Algorithm 13.5.1).
- Dynamics. Chemical exchange and the Bloch–McConnell equations (Definition 13.6.1, Formula 13.6.1): slow, intermediate, fast; $R_{\mathrm{ex}} = p_{\mathrm{A}}p_{\mathrm{B}}\Delta\omega^2/k_{\mathrm{ex}}$; titrations with $k_{\mathrm{ex}} = k_{\mathrm{on}}[\mathrm{L}] + k_{\mathrm{off}}$ (Example 13.6.1). Model-free $S^2$, $\tau_{\mathrm{e}}$ (Definitions 13.6.2–13.6.3). Relaxation dispersion (Definition 13.6.4) for invisible states, CEST, ZZ exchange. HDX: $k_{\mathrm{obs}} = k_{\mathrm{op}}k_{\mathrm{int}}/(k_{\mathrm{op}} + k_{\mathrm{cl}} + k_{\mathrm{int}})$; EX2 $\Delta G_{\mathrm{op}} = RT\ln P$, EX1 $k_{\mathrm{obs}} = k_{\mathrm{op}}$ (Definitions 13.6.5–13.6.6).
- EPR. $h\nu = g\mu_{\mathrm{B}}B$, X band $9.5\,\mathrm{GHz}$ at $0.34\,\mathrm{T}$; SDSL (Definition 13.7.1); nitroxide mobility from line shapes; DEER with $\nu_\perp = 52.04\,\mathrm{MHz\,nm^3}/r^3$ (Formula 13.7.1), distance distributions $1.8$–$6$ (to $10$) nm by regularized inversion (Definition 13.7.2); DNP (Definition 13.7.3).
- MRI. Gradients encode position, the signal is the Fourier transform of the image in k-space (Theorem 13.8.1); contrast from $T_1$, $T_2$, Gd³⁺ (PRE), diffusion and BOLD.

## Questions

1. A protein sample in a $600\,\mathrm{MHz}$ spectrometer is moved to a $1.2\,\mathrm{GHz}$ instrument. By what factors do (a) the proton polarization, (b) the expected signal-to-noise ratio of an HSQC, (c) the separation in hertz of two amide peaks $0.05\,\mathrm{ppm}$ apart and (d) their $^3J(\mathrm{H}^{\mathrm{N}},\mathrm{H}^\alpha)$ splitting change?

   **Answer** (a) Polarization $\propto B_0$: factor 2. (b) Eq. (13.5): $B_0^{3/2}$, factor $2^{3/2} = 2.8$ (in practice somewhat less, because $R_2$ also changes and probes differ); the same $S/N$ is reached in $1/8$ of the time. (c) Shifts in hertz scale with $B_0$: $0.05\,\mathrm{ppm}$ is $30\,\mathrm{Hz}$ at $600\,\mathrm{MHz}$ and $60\,\mathrm{Hz}$ at $1.2\,\mathrm{GHz}$, so peaks become better resolved as long as the line widths grow less than linearly. (d) $J$ couplings are field independent: unchanged.

2. Show that $T_2 \le 2T_1$ for spins relaxed by a fluctuating field (hint: consider what a transition between the two levels does to the phase of a spin), and explain why the difference between $T_1$ and $T_2$ is large for proteins but small for water.

   **Answer** Each spin is a two-level system; a process that changes populations at rate $W$ (up and down) relaxes $M_z$ at $2W$ and destroys the coherence of the transverse component at $W$ (each transition randomizes the phase of one spin), so the population contribution to $R_2$ is $R_1/2$, and secular (zero-frequency) dephasing can only add to it: $R_2 = R_1/2 + R_2'$ with $R_2' \ge 0$, that is, $T_2 \le 2T_1$. (For a dipolar pair, Eq. (13.14) gives $T_2 = T_1$ in extreme narrowing, consistent with this.) In Eq. (13.14) the extra term in $R_2$ is $\frac{9}{20}K^2j(0) \propto \tau_{\mathrm{c}}$, while $R_1$ depends on $j(\omega_0)$ and $j(2\omega_0)$. For water, $\tau_{\mathrm{c}} \approx 3\,\mathrm{ps}$ and $\omega_0\tau_{\mathrm{c}} \approx 10^{-2}$, so all $j$ are equal and $T_1 = T_2$; for a protein with $\tau_{\mathrm{c}} = 10\,\mathrm{ns}$, $\omega_0\tau_{\mathrm{c}} \approx 40$, $j(\omega_0)$ is $1/1600$ of $j(0)$, so $T_1$ is long and $T_2$ short.

3. A protein of $40\,\mathrm{kDa}$ gives a poor $^1\mathrm{H}$–$^{15}\mathrm{N}$ HSQC with broad, overlapping peaks at $600\,\mathrm{MHz}$ and $25\,{}^\circ\mathrm{C}$. List the possible causes and the experiments you would do to distinguish them and to improve the spectrum.

   **Answer** Causes: (i) slow tumbling of a monomer ($\tau_{\mathrm{c}} \approx 20$–$24\,\mathrm{ns}$) or (ii) oligomerization or aggregation (check by SEC–MALS, DLS or $\tau_{\mathrm{c}}$ from $R_2/R_1$; dilute, change salt or pH); (iii) chemical exchange in the intermediate regime, for example a monomer–dimer equilibrium or conformational exchange (temperature dependence of the line widths, relaxation dispersion; adding a ligand or a stabilizing mutation may shift the equilibrium); (iv) partial unfolding or heterogeneity (a narrow cluster near $8.2\,\mathrm{ppm}$ indicates disorder; check by CD, DSC). Improvements: raise the temperature (shorter $\tau_{\mathrm{c}}$), deuterate the protein and record TROSY spectra at the highest available field, use methyl labeling and methyl-TROSY, or study isolated domains; for very large or insoluble systems turn to $^{19}\mathrm{F}$ NMR or solid-state NMR.

4. For a two-spin system, follow the INEPT transfer with product operators, starting from $\hat{I}_z$: a $90^\circ_x$ pulse on $I$, a delay $\tau$, $180^\circ_x$ pulses on $I$ and $S$, a delay $\tau$, then $90^\circ_y$ on $I$ and $90^\circ_x$ on $S$. What is the final state as a function of $\tau$, and why is $\tau = 1/(4J)$ chosen? By what factor does the transfer increase the $S$ ($^{15}\mathrm{N}$) signal compared with direct excitation of $S$?

   **Answer** $90^\circ_x$: $\hat{I}_z \to -\hat{I}_y$. The $\tau$–$180^\circ$–$\tau$ element refocuses the shift of $I$ (and of $S$), and the coupling, unaffected because both spins are inverted, evolves for $2\tau$: $-\hat{I}_y \to -\hat{I}_y\cos(2\pi J\tau) + 2\hat{I}_x\hat{S}_z\sin(2\pi J\tau)$, up to signs set by the inversion. The $90^\circ_y$ on $I$ turns $\hat{I}_x \to -\hat{I}_z$, and $90^\circ_x$ on $S$ turns $\hat{S}_z \to -\hat{S}_y$: the antiphase term becomes $2\hat{I}_z\hat{S}_y\sin(2\pi J\tau)$, an $S$ coherence, maximal for $2\pi J\tau = \pi/2$, $\tau = 1/(4J) = 2.7\,\mathrm{ms}$ for $J = 92\,\mathrm{Hz}$. Its amplitude carries the polarization of $I$, so the $S$ signal is larger by $\gamma_I/\gamma_S = 9.9$ for $^1\mathrm{H} \to {}^{15}\mathrm{N}$ (in magnitude); detection back on $^1\mathrm{H}$ multiplies the gain further (Eq. 13.5).

5. Two proton pairs in a protein give NOESY cross peaks with intensities in the ratio 1 : 0.2 in the same spectrum with a short mixing time. The first pair is a reference at $0.25\,\mathrm{nm}$. Estimate the second distance and discuss why such distances are used only as upper bounds.

   **Answer** Eq. (13.21): $r = 0.25 \times (1/0.2)^{1/6} = 0.25 \times 1.31 = 0.33\,\mathrm{nm}$. Upper bounds because (i) the effective distance is $\langle r^{-6}\rangle^{-1/6}$, weighted to the closest approach; (ii) internal motion changes the effective correlation time of each pair, so intensities do not scale with $r^{-6}$ alone; (iii) spin diffusion through third protons can strengthen cross peaks; (iv) intensities are reduced by differential relaxation and by partial saturation. Errors mostly make a pair look closer or more distant by modest factors, and the sixth root compresses them, so a bound such as $\le 0.35$–$0.4\,\mathrm{nm}$ is safe.

6. Compute the maximum residual dipolar coupling of a $\mathrm{C}^\alpha$–$\mathrm{H}^\alpha$ bond ($r = 0.109\,\mathrm{nm}$) if the alignment makes $\langle3\cos^2\theta - 1\rangle = 2\times10^{-3}$ for a bond along the principal axis, and compare with the one-bond scalar coupling. Why does a single RDC not determine the orientation of a bond, and how is the degeneracy reduced?

   **Answer** Eq. (13.22): $\mu_0\gamma_{\mathrm{H}}\gamma_{\mathrm{C}}\hbar/(8\pi^2r^3) = (1.2566\times10^{-6} \times 2.675\times10^8 \times 6.728\times10^7 \times 1.0546\times10^{-34})/(78.96 \times 1.295\times10^{-30}) = 23.3\,\mathrm{kHz}$, so $D = -23.3\,\mathrm{kHz} \times 2\times10^{-3} = -47\,\mathrm{Hz}$, about a third of $^1J_{\mathrm{CH}} \approx 140\,\mathrm{Hz}$. One RDC constrains the bond to a cone of directions about the principal axis (and its mirror, $\theta$ and $180^\circ - \theta$). The degeneracy is reduced by measuring many bonds with different orientations in the same rigid unit (which also determines the tensor), by several bond types ($\mathrm{N}$–$\mathrm{H}$, $\mathrm{C}^\alpha$–$\mathrm{H}^\alpha$, $\mathrm{C}'$–$\mathrm{N}$), and by a second alignment medium with a differently oriented tensor; the fourfold ambiguity of domain orientations remains unless combined with other data (NOEs, PCS, SAXS).

7. A peak of free protein shifts by $0.5\,\mathrm{ppm}$ of $^{15}\mathrm{N}$ ($60\,\mathrm{MHz}$ for $^{15}\mathrm{N}$) on binding a ligand. If $k_{\mathrm{on}} = 10^8\,\mathrm{M^{-1}\,s^{-1}}$, what is the exchange regime at the midpoint of the titration for $K_{\mathrm{d}} = 10\,\mu\mathrm{M}$? Estimate the exchange contribution to the $^{15}\mathrm{N}$ line width at the midpoint.

   **Answer** $\Delta\nu = 0.5 \times 60 = 30\,\mathrm{Hz}$, $\lvert\Delta\omega\rvert = 188\,\mathrm{s^{-1}}$. At the midpoint $k_{\mathrm{ex}} = 2k_{\mathrm{off}} = 2 \times 10^8 \times 10^{-5} = 2000\,\mathrm{s^{-1}} \approx 10\lvert\Delta\omega\rvert$: fast exchange, the peak moves. Eq. (13.27) with $p_{\mathrm{A}} = p_{\mathrm{B}} = 0.5$: $R_{\mathrm{ex}} = 0.25 \times 188^2/2000 = 4.4\,\mathrm{s^{-1}}$, an extra $1.4\,\mathrm{Hz}$ of width, small. For the same ligand, a proton peak shifting by $0.5\,\mathrm{ppm}$ at $600\,\mathrm{MHz}$ ($\lvert\Delta\omega\rvert = 1885\,\mathrm{s^{-1}}$) would be in intermediate exchange and broaden strongly ($R_{\mathrm{ex}} \approx 440\,\mathrm{s^{-1}}$ by Eq. (13.27), which is only qualitative at this rate).

8. Under native conditions an amide exchanges with $k_{\mathrm{obs}} = 2\times10^{-6}\,\mathrm{s^{-1}}$ at pH 7, where $k_{\mathrm{int}} = 4\,\mathrm{s^{-1}}$; at pH 8, $k_{\mathrm{obs}} = 2\times10^{-5}\,\mathrm{s^{-1}}$. Which regime applies? Compute the protection factor and $\Delta G_{\mathrm{op}}$ at $298\,\mathrm{K}$, and the half-time of exchange. How would you test whether this amide reports global unfolding?

   **Answer** $k_{\mathrm{obs}}$ rises tenfold with pH, as $k_{\mathrm{int}}$ does: EX2. $P = 4/(2\times10^{-6}) = 2\times10^6$; $\Delta G_{\mathrm{op}} = 8.314 \times 298 \times \ln(2\times10^6) = 36\,\mathrm{kJ\,mol^{-1}}$. Half-time $\ln2/k_{\mathrm{obs}} = 3.5\times10^5\,\mathrm{s} = 4\,\mathrm{d}$. Test: compare $\Delta G_{\mathrm{op}}$ with $\Delta G$ of unfolding from chemical or thermal denaturation ([7.6.8](/7.6.8)), and measure $\Delta G_{\mathrm{op}}$ at increasing denaturant concentration: if the amide exchanges by global unfolding, $\Delta G_{\mathrm{op}}$ falls with the same slope ($m$ value) as the global $\Delta G$; amides exchanging by local fluctuations show smaller slopes. Several amides sharing one slope define a cooperative unit (foldon).

9. In a DEER experiment on a doubly spin-labeled protein the dipolar oscillation has a period of $0.95\,\mu\mathrm{s}$ (taken as $1/\nu_\perp$). Estimate the interspin distance. How long must the trace be to determine the width of the distribution, and what would you change to measure a distance of $8\,\mathrm{nm}$?

   **Answer** $\nu_\perp = 1/0.95\,\mu\mathrm{s} = 1.05\,\mathrm{MHz}$; $r = (52.04/1.05)^{1/3}\,\mathrm{nm} = 3.7\,\mathrm{nm}$. The mean distance needs about $2\,\mu\mathrm{s}\times(3.7/5)^3 = 0.8\,\mu\mathrm{s}$, the width about twice that, $1.6\,\mu\mathrm{s}$ or more. For $8\,\mathrm{nm}$, $\nu_\perp = 0.10\,\mathrm{MHz}$ and the trace must last about $8\,\mu\mathrm{s}$ (and $16\,\mu\mathrm{s}$ for the width): deuterate the protein and the solvent (and glycerol) to lengthen the phase memory time, work at low temperature and moderate concentration to reduce the background, and consider Gd³⁺ or trityl labels at higher field.

10. (Design) You want to know whether a 30 kDa enzyme samples, in the absence of substrate, a closed conformation seen in the crystal structure of its complex. Propose an NMR and an EPR approach, state what each would measure, and the expected signatures.

    **Answer** NMR: $^{15}\mathrm{N}$ (or methyl $^{13}\mathrm{C}$) CPMG relaxation dispersion of the free enzyme, preferably deuterated, at two fields. If the free enzyme exchanges with a minor closed state on the μs–ms time scale, residues in the hinge and active-site loops show dispersion; global fitting gives $p_{\mathrm{B}}$, $k_{\mathrm{ex}}$ and $\lvert\Delta\omega\rvert$, and the test is whether $\Delta\omega$ correlates with the shift differences between the free enzyme and the enzyme–substrate (or inhibitor) complex. Residual dipolar couplings would test the average domain orientation, and model-free $S^2$ the fast flexibility of the loops. EPR: place spin labels on the two lobes at positions whose distance changes by more than $0.5\,\mathrm{nm}$ between the open and closed crystal structures (predicted with a rotamer library), and measure DEER distributions without and with substrate analog. A bimodal distribution in the free enzyme, with a minor component at the closed distance that grows with ligand, indicates conformational selection; a single distance that shifts on binding indicates an induced fit. Controls: activity of the labeled mutants; freezing may shift equilibria, so compare with room-temperature data from NMR.
