---
title: Single-Molecule Mechanics and Molecular Recognition
description: "Forces and recognition at the scale of single molecules. Force scales in pN nm; optical tweezers from ray optics and the Rayleigh limit, calibration by equipartition, power spectra and drag, resolution and clamps; magnetic tweezers, the pendulum calibration and supercoiling; atomic force microscopy and acoustic force spectroscopy. Entropic elasticity: freely jointed and worm-like chains, the Marko–Siggia interpolation, the extensible WLC and overstretching; unzipping, RNA hairpins and proteins under force; force-dependent equilibria. Bond rupture: the Bell model as a tilted Kramers problem, dynamic force spectroscopy and the Evans–Ritchie law, slip, catch and ideal bonds. Work and free energy: the Jarzynski equality and the Crooks theorem. Molecular recognition: affinity, hot spots and double-mutant cycles, structural modules, position weight matrices and the statistical mechanics of specificity, induced fit versus conformational selection, diffusion-limited association and electrostatic steering, facilitated diffusion and the optimal target search, the speed–stability problem, kinetic proofreading as an energy–accuracy–speed trade-off and in T-cell recognition; measuring interactions by SPR with mass transport, BLI, fluorescence anisotropy, MST and ITC."
---

Biological molecules are machines that push, pull and grip, and they recognize their partners among thousands of look-alikes. This chapter treats both capabilities at the level of single molecules. The first half is mechanics: how forces of piconewtons are applied to and measured on single molecules (17.1–17.3), how polymers respond to them (17.4), how bonds break under load (17.5), and how equilibrium free energies can be obtained from irreversible pulling (17.6). The second half is recognition: what determines the affinity and specificity of molecular binding (17.7), how fast partners find each other, including a protein's search for one site in a genome (17.8), how cells beat the limits of equilibrium specificity by spending energy (17.9), and how interactions are measured (17.10). The two halves meet in force-dependent binding, in catch bonds and in the kinetic view of specificity: in both, what matters is a free-energy landscape and the rates of crossing its barriers.

The chapter uses the **Langevin equation**, the **Ornstein–Uhlenbeck process** and **Kramers rate** ([7.6.5](/7.6.5)), the two-state systems of [7.6.4](/7.6.4) and the binding statistics of [7.6.3](/7.6.3). The cell-biological uses of these methods appear elsewhere: optical traps measuring the steps of kinesin and myosin in [7.3.13](/7.3.13) and [7.3.14](/7.3.14) (whose motors are analysed physically in [7.6.27](/7.6.27)), the mechanics of adhesions and the definition of catch bonds in [7.3.23](/7.3.23), DNA supercoiling in [7.2.3](/7.2.3). The biochemistry of target search and of proofreading in translation is in [7.2.22](/7.2.22) and [7.2.19](/7.2.19); here their general theory is derived. The statistical mechanics of polymer chains, from which the force–extension relations below follow, is developed in [7.6.21](/7.6.21), and the general theory of fluctuation relations in [7.6.38](/7.6.38).

## 17.1. Forces at the Molecular Scale

The natural unit of energy for a molecule in water is $k_{\mathrm{B}}T = 4.1\,\mathrm{pN\,nm}$ at $25\,^\circ\mathrm{C}$ ($4.3\,\mathrm{pN\,nm}$ at $37\,^\circ\mathrm{C}$). Molecular displacements are nanometres, so the natural unit of force is $k_{\mathrm{B}}T/(1\,\mathrm{nm}) \approx 4\,\mathrm{pN}$. A force much smaller than this barely biases thermal motion over molecular distances; a force much larger does work of many $k_{\mathrm{B}}T$ per nanometre and reshapes the energy landscape. Motors produce a few piconewtons, which is why their steps of a few nanometres correspond to the free energy of one ATP ($\approx 80$–$100\,\mathrm{pN\,nm}$ under cellular conditions); breaking noncovalent structures takes tens to hundreds of piconewtons, and a covalent bond about $2\,\mathrm{nN}$.

![Characteristic forces of molecular biology (above) and the ranges of single-molecule force instruments (below), on a logarithmic scale: the thermal force k_BT/1 nm; stall forces of kinesin, myosin II, RNA polymerase and the phage packaging motor; the entropic regime of DNA stretching, DNA unzipping, RNA hairpin unfolding and DNA overstretching near 65 pN; mechanical unfolding of titin immunoglobulin domains and rupture of streptavidin–biotin in the AFM (loading-rate dependent); rupture of a covalent bond. Optical and magnetic tweezers and acoustic force spectroscopy cover 0.01–100 pN, the AFM 10 pN–10 nN; DNA-based tension probes report forces of a few to tens of piconewtons inside living cells](./plots/force-scales.py)

**Example 17.1.1 (How Much Force Does a Cell Exert?)** A muscle fibre of cross-section $(50\,\mu\mathrm{m})^2$ generates a tension of about $300\,\mathrm{kPa}$, that is $0.75\,\mathrm{mN}$. Its myofibrils contain thick filaments in a hexagonal lattice of spacing about $40\,\mathrm{nm}$, about $6\times10^{14}\,\mathrm{m^{-2}}$ in cross-section, so roughly $1.3\times10^6$ filaments work in parallel in this fibre and each carries about $0.6\,\mathrm{nN}$. Each half of a thick filament has about $300$ heads; if about a third of them are attached during isometric contraction, each attached head bears about $6\,\mathrm{pN}$, the force measured for single myosin molecules in optical traps. Macroscopic forces are sums of piconewton forces in parallel.

## 17.2. Optical Tweezers

### 17.2.1. The Trapping Force

A transparent bead with a refractive index $n_{\mathrm{p}}$ higher than that of the medium $n_{\mathrm{m}}$ is pulled towards the focus of a strongly focused laser beam (Ashkin 1970, 1986; Nobel Prize in Physics 2018). **Optical tweezers** ([7.3.14](/7.3.14)) hold beads of $0.2$–$2\,\mu\mathrm{m}$ in a nearly harmonic potential and use them as handles on single molecules.

Two limits make the origin of the force transparent. For a bead much larger than the wavelength (the ray-optics or Mie regime), each ray is refracted twice on passing through the bead and leaves with a changed direction; the change in photon momentum $\Delta\boldsymbol{p}$ per unit time is a force on the bead, equal and opposite. If the bead is displaced from the beam axis, the more intense rays near the axis are refracted more strongly and the net reaction force points back towards the region of highest intensity: the gradient force. Reflection and absorption push the bead along the beam (the scattering force). A stable three-dimensional trap requires the axial gradient force to exceed the scattering force, which needs a high numerical aperture, in practice an oil- or water-immersion objective with $\mathrm{NA} \ge 1.2$.

**Formula 17.2.1 (Optical Forces in the Rayleigh Regime)** For a sphere of radius $a \ll \lambda$ with relative index $m = n_{\mathrm{p}}/n_{\mathrm{m}}$, which behaves as an induced dipole of polarizability $\alpha = 4\pi\varepsilon_0n_{\mathrm{m}}^2a^3(m^2 - 1)/(m^2 + 2)$, the gradient and scattering forces in a beam of intensity $I$ are

$$
\boldsymbol{F}_{\mathrm{grad}} = \frac{2\pi n_{\mathrm{m}}a^3}{c}\,\frac{m^2 - 1}{m^2 + 2}\,\nabla I, \qquad
F_{\mathrm{scat}} = \frac{n_{\mathrm{m}}}{c}\,\sigma_{\mathrm{s}}I, \quad \sigma_{\mathrm{s}} = \frac{128\pi^5a^6}{3\lambda^4}\left(\frac{m^2 - 1}{m^2 + 2}\right)^2,
$$
with $\lambda$ the wavelength in the medium. The gradient force grows as $a^3$, the scattering force as $a^6$; small particles are trapped by the gradient force alone.

The trap is a potential well $U = -\frac12\alpha\langle E^2\rangle$, deepest at the focus. Near the focus it is harmonic, $F = -\kappa x$, with a stiffness proportional to the laser power: typical values are $0.01$–$1\,\mathrm{pN\,nm^{-1}}$ for $100\,\mathrm{mW}$ to $1\,\mathrm{W}$ in the specimen plane, so that forces up to about $100\,\mathrm{pN}$ are applied over displacements of $100$–$200\,\mathrm{nm}$ before the bead leaves the linear region. Near-infrared lasers ($1064\,\mathrm{nm}$) are used because water and biomolecules absorb little there; even so the focus is heated by about $1$–$2\,\mathrm{K}$ per $100\,\mathrm{mW}$, and photodamage, mediated by reactive oxygen species, limits long experiments.

### 17.2.2. Calibration

The bead in the trap is a Brownian particle in a harmonic potential, the Ornstein–Uhlenbeck process of [7.6.5](/7.6.5#def-5.4.3). Its fluctuations calibrate the trap.

**Formula 17.2.2 (Calibration of an Optical Trap)** For a bead with friction coefficient $\gamma = 6\pi\eta a$ in a trap of stiffness $\kappa$:

1. Equipartition: $\kappa = k_{\mathrm{B}}T/\langle x^2\rangle$, from the variance of the position (the **equipartition theorem**).
2. Power spectrum: the one-sided power spectral density of the position is the Lorentzian
$$
S(f) = \frac{k_{\mathrm{B}}T}{\pi^2\gamma\left(f_{\mathrm{c}}^2 + f^2\right)}, \qquad f_{\mathrm{c}} = \frac{\kappa}{2\pi\gamma},
$$
so that a fit gives $f_{\mathrm{c}}$ and the diffusion coefficient $D = k_{\mathrm{B}}T/\gamma$, hence $\kappa = 2\pi\gamma f_{\mathrm{c}}$ without knowing the detector's conversion factor in advance (the plateau $S(0) = 4\gamma k_{\mathrm{B}}T/\kappa^2$ fixes it).
3. Drag: moving the stage at speed $v$ displaces the bead by $x = \gamma v/\kappa$ (Stokes' law).

**Proof** (2) The overdamped Langevin equation $\gamma\dot x = -\kappa x + \xi(t)$ with white noise $\langle\xi(t)\xi(t')\rangle = 2\gamma k_{\mathrm{B}}T\delta(t - t')$ is linear; in Fourier space $\hat x(\omega) = \hat\xi(\omega)/(\kappa - \mathrm{i}\gamma\omega)$, so the two-sided spectrum is $S_x(\omega) = 2\gamma k_{\mathrm{B}}T/(\kappa^2 + \gamma^2\omega^2)$ ([7.6.5](/7.6.5#fml-5.4.1)). With the normalization $\langle x^2\rangle = \int_{-\infty}^{\infty}S_x(\omega)\,\mathrm{d}\omega/2\pi$, the one-sided density in frequency, defined by $\int_0^\infty S(f)\,\mathrm{d}f = \langle x^2\rangle$, is $S(f) = 2S_x(2\pi f) = 4\gamma k_{\mathrm{B}}T/(\kappa^2 + 4\pi^2\gamma^2f^2)$, the Lorentzian; its integral is $k_{\mathrm{B}}T/\kappa$, consistent with (1). $\square$

![Calibrating an optical trap from the Brownian motion of the bead (simulation: radius 0.5 µm in water at 25 °C, γ = 8.4 × 10⁻⁶ pN s nm⁻¹, κ = 0.05 pN nm⁻¹, sampled at 100 kHz for 2 s). A: the bead position fluctuates by about ±9 nm and relaxes in τ = γ/κ = 0.17 ms. B: the position histogram is the Boltzmann distribution of the harmonic well; equipartition gives κ = k_BT/⟨x²⟩. C: the power spectrum averaged over 50 segments and a Lorentzian fit: the corner frequency f_c = κ/(2πγ) ≈ 1 kHz and κ = 2πγf_c agree with equipartition within a few percent; above about 20 kHz the measured spectrum flattens because frequencies above half the sampling rate are folded back (aliasing), one of the corrections applied in practice](./plots/trap-calibration.py)

Each method has its systematic errors. Equipartition requires an accurate conversion from detector signal to nanometres and is biased by drift and by the finite bandwidth of the detector. The power-spectrum method needs the correct friction: near a surface, the drag on a sphere increases (Faxén's law, $\gamma/\gamma_\infty \approx [1 - \frac{9}{16}(a/h) + \frac18(a/h)^3]^{-1}$ at a height $h$ of the centre above the surface), and aliasing, filtering by the photodiode and the hydrodynamic memory of water must be corrected at high frequency. Position is detected by back-focal-plane interferometry: the forward-scattered light from the bead interferes with the unscattered beam, and a quadrant photodiode in a plane conjugate to the back focal plane of the condenser measures the displacement with sub-nanometre resolution at up to $100\,\mathrm{kHz}$.

### 17.2.3. Measurement Modes and Resolution

A single trap holds one bead attached to a molecule whose other end is fixed to the coverslip or to a pipette; in the dual-trap ("dumbbell") geometry the molecule is suspended between two trapped beads far from any surface, which decouples it from stage drift. Two modes dominate. In a position clamp the trap moves at constant speed and the force rises as the molecule stretches (force–extension curves, 17.4). In a force clamp a feedback loop moves the trap to keep the bead's displacement, and hence the force, constant, and the extension is recorded as a function of time (motor steps, hopping of a hairpin, 17.4.3); a passive force clamp exploits the flat region near the edge of the trap where the force is independent of displacement.

The resolution is set by thermal noise. Averaged over a bandwidth $B$, the position noise of a bead in a trap of total stiffness $\kappa$ (trap plus tether) is $\delta x = \sqrt{4k_{\mathrm{B}}T\gamma B}/\kappa$ for $B \ll f_{\mathrm{c}}$. For $\gamma = 8.4\times10^{-6}\,\mathrm{pN\,s\,nm^{-1}}$, $\kappa = 0.3\,\mathrm{pN\,nm^{-1}}$ and $B = 100\,\mathrm{Hz}$, $\delta x \approx 0.4\,\mathrm{nm}$; stiffer traps and tethers, smaller beads and averaging over longer times push the noise down to about $0.1\,\mathrm{nm}$. At that level Abbondanzieri, Block and colleagues (2005) resolved the steps of $0.34\,\mathrm{nm}$, one base pair, of single RNA polymerase molecules in a dual trap with passive force clamp and helium atmosphere, which reduces refractive-index fluctuations of the air in the optical path. Kinesin's $8.2\,\mathrm{nm}$ steps and its **stall force** of about $6$–$7\,\mathrm{pN}$ ([7.3.14](/7.3.14)) and the $36\,\mathrm{nm}$ hand-over-hand steps of myosin V were the first prominent results; translocation of the ribosome, packaging of DNA into phage capsids and the folding landscapes of proteins and nucleic acids followed.

## 17.3. Magnetic Tweezers, Atomic Force Microscopy and Other Force Probes

### 17.3.1. Magnetic Tweezers

**Definition 17.3.1 (Magnetic Tweezers)** In *magnetic tweezers* a superparamagnetic bead ($0.5$–$5\,\mu\mathrm{m}$) attached to one end of a molecule, whose other end is fixed to a surface, is pulled and rotated by a magnetic field gradient from permanent magnets or electromagnets above the sample; the bead's three-dimensional position is measured by video microscopy from its diffraction rings.

The bead acquires a moment $\boldsymbol{m}(\boldsymbol{B})$ aligned with the field, and the force is $\boldsymbol{F} = \frac12\nabla(\boldsymbol{m}\cdot\boldsymbol{B})$. Because the field gradient decays over millimetres while the molecule changes length by micrometres, the force is constant to a very good approximation: magnetic tweezers are a natural force clamp, from about $0.01$ to $100\,\mathrm{pN}$ depending on bead and magnets. The force is set by the distance of the magnets and is calibrated from the bead's Brownian motion.

**Formula 17.3.1 (Pendulum Calibration)** A bead pulled with force $F$ on a tether of extension $l$ is an inverted pendulum: a transverse displacement $\delta x$ tilts the tether and produces a restoring force $F\delta x/l$. By equipartition,

$$
F = \frac{k_{\mathrm{B}}T\,l}{\langle\delta x^2\rangle}.
$$

The higher the force, the smaller the fluctuations and the more precisely the extension is measured; at low forces the transverse fluctuations of a micrometre-long tether are hundreds of nanometres and slow, and long recordings and drift correction (for instance by Fourier filtering of low frequencies, as for optical traps) are needed. Because one field covers the whole field of view, hundreds of tethers can be measured in parallel, and illumination by an LED avoids photodamage.

The unique ability of magnetic tweezers is rotation: turning the magnets rotates the bead by any number of turns, which changes the **linking number** of a torsionally constrained DNA and allows supercoiling to be controlled and measured ([7.2.3](/7.2.3)). Twisting first stores torque in the double helix, $\tau = 2\pi n\,k_{\mathrm{B}}TC/L$ for $n$ turns with twist persistence length $C \approx 100\,\mathrm{nm}$ (torsional modulus $C k_{\mathrm{B}}T \approx 410\,\mathrm{pN\,nm^2}$); at a buckling torque of the order $\sqrt{2Ak_{\mathrm{B}}TF}$ ($A$ the bending persistence length) the molecule forms a plectoneme, and each further turn shortens the tether by a loop. The rotation–extension curve then falls linearly on both sides of a plateau: the "hat curve". Above about $0.5\,\mathrm{pN}$, negative turns are absorbed by local melting of the duplex instead of plectonemes, and above about $3\,\mathrm{pN}$ positive turns convert B-DNA into a strongly overwound form (P-DNA); the torques at these transitions, about $-10$ and $+34\,\mathrm{pN\,nm}$, were measured directly with rotor beads and magnetic torque tweezers (Bryant, Bustamante and colleagues 2003).

![Magnetic tweezers on a 10 kbp DNA (contour length 3.4 µm, A = 50 nm, C = 100 nm). A: transverse fluctuations of the bead against force, from the pendulum relation ⟨δx²⟩ = k_BT l/F with the extension l(F) of the worm-like chain: fluctuations of hundreds of nanometres at 0.01 pN fall to about 30 nm at 10 pN. B: extension against turns added (simplified model): twisting does not change the extension until the buckling torque is reached (n_b ≈ 13, 19, 27 and 46 turns at 0.25, 0.5, 1 and 3 pN), after which each turn shortens the tether by about 2π√(Ak_BT/2F), 90 nm at 0.5 pN; above 0.5 pN negative turns melt the duplex and the extension stays constant on that side; the model neglects the slight shortening before buckling and the bending fluctuations of the plectoneme](./plots/magnetic-tweezers.py)

**Example 17.3.1 (Watching a Promoter Open)** Revyakin, Strick, Ebright and colleagues (2004, 2006) held a positively supercoiled DNA containing a promoter in magnetic tweezers at $0.3\,\mathrm{pN}$, where one turn changes the extension by about $56\,\mathrm{nm}$. When RNA polymerase unwound about $12$–$14\,\mathrm{bp}$ to form the open complex, the DNA lost about $1.3$ turns of twist, compensated by the removal of $1.3$ positive supercoils, and the extension jumped by about $70\,\mathrm{nm}$. Opening of a single base pair corresponds to about $1/10.5$ turn, or about $5\,\mathrm{nm}$ of extension. This made promoter unwinding, scrunching during initial transcription and promoter escape visible on single molecules in real time ([7.2.10](/7.2.10)).

### 17.3.2. Atomic Force Microscopy

**Definition 17.3.2 (Atomic Force Microscope)** An *atomic force microscope* (AFM; Binnig, Quate and Gerber 1986) measures the force between a sharp tip at the end of a flexible cantilever and a sample from the deflection of the cantilever, detected by a laser reflected from its back onto a split photodiode. Scanned over a surface, it images topography with sub-nanometre vertical resolution; used as a force probe, it pulls on molecules tethered between tip and surface.

The cantilever is a spring of stiffness $k_{\mathrm{c}} = 0.01$–$1\,\mathrm{N\,m^{-1}}$ ($10$–$1000\,\mathrm{pN\,nm^{-1}}$), calibrated, like a trap, from its thermal fluctuations, $k_{\mathrm{c}} = k_{\mathrm{B}}T/\langle z^2\rangle$, using the fundamental mode of its vibration spectrum ([5.1.6](/5.1.6)). Its stiffness makes the AFM a high-force instrument: forces from about $10\,\mathrm{pN}$ to nanonewtons, with a noise floor of a few piconewtons set by the thermal force $\sqrt{4k_{\mathrm{B}}T\gamma B}$ of the cantilever in water. It is suited to strong interactions: mechanical unfolding of proteins, rupture of receptor–ligand bonds and of covalent bonds. Imaging in liquid at video rate (high-speed AFM, Ando and colleagues 2008) has filmed myosin V walking on actin and the rotation of the F₁-ATPase subunits.

**Example 17.3.2 (The Sawtooth of Titin)** Rief, Gaub and colleagues (1997) pulled on the giant muscle protein titin and on engineered polyproteins of eight identical immunoglobulin domains (I27). The force–extension curve is a sawtooth: the force rises along a worm-like-chain curve of the unfolded parts, a domain unfolds at $150$–$300\,\mathrm{pN}$ (at about $1\,\mu\mathrm{m\,s^{-1}}$), the contour length increases by $28\,\mathrm{nm}$ ($89$ residues at $0.38$–$0.4\,\mathrm{nm}$ each, minus the $4\,\mathrm{nm}$ the folded domain spanned), the force drops, and the cycle repeats once for each domain. The unfolding force increases logarithmically with the pulling speed, as the Bell model predicts (17.5), with $k_0 \approx 3\times10^{-4}\,\mathrm{s^{-1}}$ and $x^\ddagger \approx 0.25\,\mathrm{nm}$: the barrier lies very close to the native state, where a cluster of backbone hydrogen bonds between two β-strands must break at once. In muscle, the unfolding of titin domains under extreme stretch protects sarcomeres from damage.

![Mechanical unfolding of single molecules (simulations). A: AFM sawtooth of an (I27)₈ polyprotein pulled at 400 nm/s with a cantilever of 50 pN/nm: the force follows worm-like-chain curves (dashed; persistence length 0.4 nm) whose contour lengths increase by 28 nm at each unfolding, and domains unfold stochastically at 180–240 pN by the Bell rate with k₀ = 3.3 × 10⁻⁴ s⁻¹ and x‡ = 0.25 nm; the last rise is the fully unfolded chain. B: an RNA hairpin held at constant force near its midpoint, F_1/2 = 15.0 pN, hops between folded and unfolded states (extension change 18 nm, 2 nm noise); a change of only 0.2 pN shifts the open fraction from 0.13 to 0.62. C: the open probability is a sigmoid of width k_BT/Δx = 0.23 pN, and ln(k_open/k_close) is linear in force with slope Δx/k_BT](./plots/mechanical-unfolding.py)

### 17.3.3. Comparison

| Method | Force range | Spatial and temporal resolution | Strengths | Limitations |
|---|---|---|---|---|
| Optical tweezers | $0.1$–$100\,\mathrm{pN}$ | $0.1\,\mathrm{nm}$, $\mu\mathrm{s}$–$\mathrm{ms}$ | highest resolution; position and force clamps; dual traps; combination with fluorescence | one molecule at a time; heating and photodamage; no torque with spherical beads (birefringent particles give rotation) |
| Magnetic tweezers | $0.01$–$100\,\mathrm{pN}$ | $\sim 1\,\mathrm{nm}$, $\mathrm{ms}$ | constant force; torque and supercoiling; hundreds of molecules in parallel; no photodamage | lower bandwidth at low force; force calibration by fluctuations |
| AFM | $10\,\mathrm{pN}$–$10\,\mathrm{nN}$ | $0.1\,\mathrm{nm}$, $\mu\mathrm{s}$ (small cantilevers) | strong interactions; imaging; works on surfaces and cells | high stiffness, so low-force regime is noisy; tip chemistry |
| Acoustic force spectroscopy | $0.1$–$100\,\mathrm{pN}$ | $\sim 1\,\mathrm{nm}$, $\mathrm{ms}$ | standing acoustic waves push thousands of beads to the pressure nodes; parallel; non-contact | calibration per bead; newer method |
| Molecular tension probes | $\sim 4$–$60\,\mathrm{pN}$ thresholds | digital (ruptured or not) or FRET | forces inside living cells (DNA tension gauge tethers, hairpin probes, FRET tension sensors in vinculin or talin) | calibrated only through rupture statistics; integrate over time |

DNA-based probes use the dependence of duplex rupture on geometry: a short duplex pulled from the same end (unzipping) breaks at about $12\,\mathrm{pN}$, the same duplex pulled from opposite ends (shearing) at about $56\,\mathrm{pN}$ on the time scale of seconds, so a set of tension gauge tethers with different geometries measures the forces that integrins and Notch receptors exert on their ligands (Wang and Ha 2013): integrin activation requires about $40\,\mathrm{pN}$, Notch activation about $12\,\mathrm{pN}$ ([7.3.23](/7.3.23#sec-23.4.4)).

## 17.4. Elasticity of Single Molecules

### 17.4.1. Entropic Springs

A flexible polymer resists extension because extended conformations are few. In the simplest description, the freely jointed chain, $N$ segments of length $b$ (the Kuhn length) point in independent random directions; the mean extension under a force $F$ follows from the **partition function** of independent segments,

$$
\frac{\langle x\rangle}{L} = \coth\frac{Fb}{k_{\mathrm{B}}T} - \frac{k_{\mathrm{B}}T}{Fb}, \qquad L = Nb,
$$
the Langevin function, which at small force gives a Hookean spring $F = (3k_{\mathrm{B}}T/Lb)\langle x\rangle$ and at large force approaches full extension as $1 - k_{\mathrm{B}}T/Fb$. The spring constant is proportional to temperature: the elasticity is entropic, an **entropic force** ([7.6.2](/7.6.2)).

DNA is better described as a **worm-like chain**, a continuously flexible rod with bending stiffness $\kappa_{\mathrm{b}} = Ak_{\mathrm{B}}T$, whose tangent correlations decay over the **persistence length** $A$ ([7.3.15](/7.3.15#def-15.3.1)); for long chains it is equivalent to a freely jointed chain with $b = 2A$, but at high force the two differ, because a worm-like chain straightens by suppressing many small bending fluctuations rather than by aligning a few stiff segments. The derivation of its statistics belongs to [7.6.21](/7.6.21); here the result needed for single-molecule experiments is used.

**Formula 17.4.1 (Marko–Siggia Interpolation)** The force–extension relation of a worm-like chain of contour length $L$ and persistence length $A$ is, to within $10\,\%$ over the whole range (Marko and Siggia 1995; Bustamante and colleagues 1994),

$$
\frac{FA}{k_{\mathrm{B}}T} = \frac{x}{L} + \frac{1}{4\left(1 - x/L\right)^2} - \frac14 .
$$
It is exact in both limits: $F = (3k_{\mathrm{B}}T/2AL)x$ at small extension, and $1 - x/L = \frac12\sqrt{k_{\mathrm{B}}T/FA}$ at high force. When the backbone itself stretches, $x/L$ is replaced by $x/L - F/S$ with the stretch modulus $S$ (the extensible worm-like chain, Odijk 1995; Wang and colleagues 1997).

**Definition 17.4.1 (Force–Extension Curve)** A *force–extension curve* is the relation between the force applied to the ends of a single molecule and its mean end-to-end extension along the force, measured in equilibrium (slow pulling) or at a given pulling rate; its shape identifies the elastic regimes and structural transitions of the molecule.

### 17.4.2. DNA under Tension

The force–extension curve of double-stranded DNA, measured first with magnetic beads (Smith, Finzi and Bustamante 1992) and then with optical tweezers, has four regimes.

1. Below about $5\,\mathrm{pN}$, entropic elasticity with $A \approx 50\,\mathrm{nm}$ ($150\,\mathrm{bp}$) at physiological salt, rising to about $60\,\mathrm{nm}$ at low salt because unscreened phosphate repulsion stiffens the chain.
2. From $5$ to about $50\,\mathrm{pN}$, the chain is nearly straight and the backbone stretches elastically, $S \approx 1000$–$1500\,\mathrm{pN}$; the contour length is $0.34\,\mathrm{nm}$ per base pair.
3. Near $65\,\mathrm{pN}$, the overstretching transition: the length increases by about $70\,\%$ within $1$–$2\,\mathrm{pN}$, a highly cooperative transition. Its nature was debated for twenty years. It is now understood (Williams, Rouzina, van Mameren, Wuite, Peterman, Yan and colleagues) as a competition between three structures: peeling of one strand from a free end or nick, melting into internal bubbles of two parallel single strands, and a base-paired, elongated S-DNA; which one occurs depends on salt, temperature, sequence and on whether the ends are free.
4. Beyond overstretching, single-stranded DNA, an extensible freely jointed chain with a Kuhn length of about $1.5\,\mathrm{nm}$ (strongly salt-dependent) and a contour length of about $0.56\,\mathrm{nm}$ per nucleotide; at forces below about $6$–$7\,\mathrm{pN}$ the same number of nucleotides is shorter as a single strand than as a duplex, and above it longer, which is how single-molecule experiments detect the conversion of duplex to single strand by helicases and polymerases.

![Force–extension curves of λ DNA (48.5 kbp, contour length 16.5 µm, 25 °C). A: the freely jointed chain with b = 2A = 100 nm and the worm-like chain (Marko–Siggia, A = 50 nm) agree at low force but differ in how they approach full extension; the extensible WLC (S = 1200 pN) lets the molecule stretch beyond its contour length; near 65 pN the length increases to about 1.7 L in the overstretching transition; single-stranded DNA (extensible FJC, b = 1.5 nm, 0.56 nm per nucleotide) is shorter than duplex below about 6 pN and longer above. B: simulated optical-tweezers data between 2 and 50 pN fitted with the extensible WLC recover A, S and L; the inextensible WLC (dotted) fails above about 10 pN](./plots/force-extension.py)

Pulling the two strands apart from the same end, unzipping, opens one base pair at a time at forces of $10$–$15\,\mathrm{pN}$, higher for GC-rich and lower for AT-rich stretches (Essevaz-Roulet, Bockelmann and Heslot 1997). The force signal reads out the sequence-dependent base-pairing free energy, about $2$–$3\,k_{\mathrm{B}}T$ per base pair, against the elastic work of stretching the released single strands; it is the basis of mechanical mapping of protein–DNA contacts along a sequence.

### 17.4.3. Two-State Structures under Force

A hairpin, a protein domain or any structure that unfolds in one step and lengthens by $\Delta x$ along the force is a two-state system in which force is the control parameter, as voltage is for an ion channel ([7.6.4](/7.6.4)).

**Formula 17.4.2 (Two-State Equilibrium under Force)** If the unfolded state is longer by $\Delta x$ along the pulling direction, the equilibrium constant depends on force as

$$
K(F) = \frac{p_{\mathrm{U}}}{p_{\mathrm{F}}} = \mathrm{e}^{-[\Delta G(0) - F\Delta x]/k_{\mathrm{B}}T}, \qquad p_{\mathrm{U}}(F) = \frac{1}{1 + \mathrm{e}^{-(F - F_{1/2})\Delta x/k_{\mathrm{B}}T}},
$$
with $F_{1/2} = \Delta G(0)/\Delta x$. If the transition state lies at a distance $x_{\mathrm{u}}^\ddagger$ from the folded and $x_{\mathrm{f}}^\ddagger = \Delta x - x_{\mathrm{u}}^\ddagger$ from the unfolded state, the rates are $k_{\mathrm{u}}(F) = k_{\mathrm{u}}(0)\mathrm{e}^{Fx_{\mathrm{u}}^\ddagger/k_{\mathrm{B}}T}$ and $k_{\mathrm{f}}(F) = k_{\mathrm{f}}(0)\mathrm{e}^{-Fx_{\mathrm{f}}^\ddagger/k_{\mathrm{B}}T}$.

Here $\Delta G(0)$ is the free energy of unfolding at zero force including the cost of stretching the released chain to the extension it has at $F_{1/2}$; corrections for the compliance of handles and beads are made with the elastic models above. Because $\Delta x$ is large for nucleic-acid hairpins ($18\,\mathrm{nm}$ for a $20$-bp hairpin with a short loop), the transition is extraordinarily sharp in force, $k_{\mathrm{B}}T/\Delta x \approx 0.2\,\mathrm{pN}$.

**Example 17.4.1 (The P5ab Hairpin)** Liphardt, Tinoco, Bustamante and colleagues (2001) held the P5ab hairpin of the *Tetrahymena* group I intron in a dual optical trap. Near $14.5\,\mathrm{pN}$ it hopped between folded and unfolded states every few seconds, with $\Delta x \approx 18\,\mathrm{nm}$; from the force dependence of the populations they obtained the folding free energy, in agreement with the nearest-neighbour prediction ([7.6.16](/7.6.16#sec-16.7.2)), and from the rates the location of the transition state. Woodside, Block and colleagues (2006) later reconstructed full one-dimensional energy landscapes of DNA hairpins from such constant-force trajectories, by inverting the extension histogram, $G(x) = -k_{\mathrm{B}}T\ln p(x)$, after deconvolving the instrument's response.

Force also changes binding. If a ligand binds one conformation of a mechanically loaded protein, the affinity becomes force dependent, $K_{\mathrm{d}}(F) = K_{\mathrm{d}}(0)\mathrm{e}^{-\Delta\Phi(F)/k_{\mathrm{B}}T}$, where $\Delta\Phi(F) = \int_0^F[x_{\mathrm{o}}(f) - x_{\mathrm{c}}(f)]\,\mathrm{d}f$ is the difference of the elastic free energies of the two conformations, computed from their force–extension curves. Talin's rod domains, which unfold at $5$–$25\,\mathrm{pN}$ and expose cryptic vinculin-binding sites, are the best-characterized example of such mechanochemical coupling (Yan and colleagues; [7.3.23](/7.3.23#sec-23.4.4)).

## 17.5. Bond Rupture under Force

### 17.5.1. The Bell Model

A noncovalent bond under constant force has no equilibrium bound state in the long run: pulled far enough, every bond breaks. Its lifetime is a kinetic quantity.

**Definition 17.5.1 (Bell Model)** In the **Bell model** (Bell 1978) a force $F$ applied across a bond lowers the barrier to dissociation by $Fx^\ddagger$, where $x^\ddagger$ is the distance from the bound state to the transition state along the force, so that the dissociation rate is

$$
k(F) = k_0\,\mathrm{e}^{Fx^\ddagger/k_{\mathrm{B}}T}, \qquad \tau(F) = \tau_0\,\mathrm{e}^{-Fx^\ddagger/k_{\mathrm{B}}T}.
$$

The Bell formula follows from Kramers' rate ([7.6.5](/7.6.5#thm-5.6.2)) for a potential tilted by $-Fx$, if the force is small enough that the positions of the well and the barrier do not move. At higher forces the barrier approaches the well and finally disappears; for a cubic potential the theory of Dudko, Hummer and Szabo (2006) gives

$$
k(F) = k_0\left(1 - \frac{\nu Fx^\ddagger}{\Delta G^\ddagger}\right)^{1/\nu - 1}\exp\left\{\frac{\Delta G^\ddagger}{k_{\mathrm{B}}T}\left[1 - \left(1 - \frac{\nu Fx^\ddagger}{\Delta G^\ddagger}\right)^{1/\nu}\right]\right\},
$$
with $\nu = 2/3$ (linear-cubic potential) or $1/2$ (cusp), which reduces to Bell's formula for $\nu = 1$ and yields the barrier height $\Delta G^\ddagger$ as well as $x^\ddagger$. The force sensitivity of a bond is characterized by the force $k_{\mathrm{B}}T/x^\ddagger$ that shortens its lifetime $\mathrm{e}$-fold: $8\,\mathrm{pN}$ for $x^\ddagger = 0.5\,\mathrm{nm}$.

### 17.5.2. Dynamic Force Spectroscopy

In most experiments the force is not constant but increases at a loading rate $r = \mathrm{d}F/\mathrm{d}t$, the product of the pulling speed and the stiffness of probe and linkers. The bond then breaks at a random force whose distribution depends on $r$.

**Definition 17.5.2 (Dynamic Force Spectroscopy)** *Dynamic force spectroscopy* (Evans and Ritchie 1997) is the measurement of the distribution of rupture forces of a bond over a range of loading rates, usually several decades, from which the parameters of its energy landscape along the pulling direction are extracted.

**Theorem 17.5.1 (Evans–Ritchie Law)** For a Bell bond under a constant loading rate $r$, the rupture force has the probability density

$$
p(F) = \frac{k(F)}{r}\exp\left[-\frac{k_0k_{\mathrm{B}}T}{rx^\ddagger}\left(\mathrm{e}^{Fx^\ddagger/k_{\mathrm{B}}T} - 1\right)\right],
$$
and its most probable value is

$$
F^* = \frac{k_{\mathrm{B}}T}{x^\ddagger}\ln\frac{rx^\ddagger}{k_0k_{\mathrm{B}}T}
$$
for $rx^\ddagger > k_0k_{\mathrm{B}}T$ (and $0$ otherwise).

**Proof** The survival probability $S$ of the bond obeys $\mathrm{d}S/\mathrm{d}t = -k(F(t))S$; with $F = rt$, $\mathrm{d}S/\mathrm{d}F = -(k(F)/r)S$, so $S(F) = \exp[-\int_0^Fk(f)\,\mathrm{d}f/r]$, and the integral of $k_0\mathrm{e}^{fx^\ddagger/k_{\mathrm{B}}T}$ gives the exponent. The density is $p = -\mathrm{d}S/\mathrm{d}F = (k/r)S$. Its maximum satisfies $\mathrm{d}\ln p/\mathrm{d}F = x^\ddagger/k_{\mathrm{B}}T - k(F)/r = 0$, i.e. $k(F^*) = rx^\ddagger/k_{\mathrm{B}}T$, which gives $F^*$. $\square$

Plotting $F^*$ against $\ln r$ gives a line of slope $k_{\mathrm{B}}T/x^\ddagger$ whose intercept gives $k_0$: the "strength" of a bond is not a property of the bond alone but of the time scale on which it is probed. A bond with several barriers in series shows a spectrum of linear segments with increasing slopes at higher loading rates, as the inner, sharper barriers become rate-limiting. Merkel, Evans and colleagues (1999) found such segments for streptavidin–biotin over six decades of loading rate with the biomembrane force probe, rupture forces rising from about $5$ to $170\,\mathrm{pN}$.

![Dynamic force spectroscopy and catch bonds. A: rupture-force histograms of 2000 simulated Bell bonds (k₀ = 0.1 s⁻¹, x‡ = 0.5 nm) at loading rates from 10 to 10⁴ pN/s, with the densities of Theorem 17.5.1: the distribution shifts by k_BT/x‡ ln 10 = 19 pN per decade and becomes narrower relative to its mean. B: most probable rupture force against loading rate: a straight line of slope k_BT/x‡ for a single barrier (zero below r = k₀k_BT/x‡); a second, inner barrier (x′ = 0.12 nm, k₀′ = 10 s⁻¹) becomes rate-limiting above about 10³ pN/s and steepens the spectrum. C: lifetime against force for a slip bond (Bell), an ideal bond, and a catch–slip bond in the two-pathway model (k_c = 2 s⁻¹, x_c = 1.0 nm; k_s = 0.02 s⁻¹, x_s = 0.4 nm): its lifetime rises from 0.5 s without force to about 7 s at 16 pN before force-driven rupture takes over](./plots/bond-rupture.py)

### 17.5.3. Slip, Catch and Ideal Bonds

Bonds that follow the Bell model, whose lifetime decreases with force, are **slip bonds**; **catch bonds**, whose lifetime increases with force over some range ([7.3.23](/7.3.23#def-23.4.4)), were predicted by Dembo and colleagues (1988) and first demonstrated for P-selectin binding PSGL-1 on leukocytes (Marshall, Zhu and colleagues 2003). Bonds whose lifetime is independent of force are ideal bonds. Catch bonds are now known for the bacterial adhesin FimH binding mannose, for integrins, for cadherins in the X-dimer state, for actin binding vinculin and the cadherin–catenin complex (directionally: stronger when pulled towards the pointed end of actin), for myosin and kinesin under backward load, and for the T-cell receptor binding agonist peptide–MHC, whose lifetime increases with force up to about $10\,\mathrm{pN}$, while antagonist ligands form slip bonds (Liu, Zhu and colleagues 2014).

The simplest description has two dissociation pathways, one inhibited and one accelerated by force, $k(F) = k_{\mathrm{c}}\mathrm{e}^{-Fx_{\mathrm{c}}/k_{\mathrm{B}}T} + k_{\mathrm{s}}\mathrm{e}^{Fx_{\mathrm{s}}/k_{\mathrm{B}}T}$ ([7.3.23](/7.3.23#eq-23.5)); structurally, force often converts the bond from a weakly to a tightly bound conformation, an allosteric mechanism in which force plays the role of the effector. Catch bonds serve adhesion under shear: leukocytes roll on selectins in the bloodstream and stop rolling, paradoxically, when the flow is too low; bacteria with FimH stick better at high flow. They also serve discrimination: a receptor whose bond is reinforced by force can test the identity of a ligand mechanically.

## 17.6. Free Energies from Irreversible Work

In single-molecule pulling experiments, the work done on a molecule fluctuates from one realization to the next. The **second law of thermodynamics** constrains only its average, $\langle W\rangle \ge \Delta F$, with equality for reversible (infinitely slow) pulling. Two exact relations show that the fluctuations carry more information.

**Theorem 17.6.1 (Jarzynski Equality)** Let a system start in equilibrium at temperature $T$ with a control parameter $\lambda = \lambda_0$ (for example the position of a trap), and let $\lambda$ be changed according to a fixed protocol to $\lambda_1$ in a finite time, with the system coupled to a heat bath. Then the work $W$ done on the system satisfies

$$
\left\langle \mathrm{e}^{-W/k_{\mathrm{B}}T}\right\rangle = \mathrm{e}^{-\Delta F/k_{\mathrm{B}}T},
$$
where the average is over repetitions of the protocol and $\Delta F = F(\lambda_1) - F(\lambda_0)$ is the equilibrium free-energy difference, whether or not the system is in equilibrium at the end (Jarzynski 1997).

**Proof** (For a Markov process with discrete time steps.) Write the work as $W = \sum_k[H_{\lambda_{k+1}}(x_k) - H_{\lambda_k}(x_k)]$: at each step $\lambda$ is first changed at fixed $x_k$ (work) and then $x$ evolves at fixed $\lambda_{k+1}$ by a transition probability that satisfies detailed balance with respect to $\mathrm{e}^{-\beta H_{\lambda_{k+1}}}$ ($\beta = 1/k_{\mathrm{B}}T$). Define the unnormalized density $\rho_k(x)$ as the average of $\mathrm{e}^{-\beta W_k}$ over trajectories ending at $x$ after $k$ steps. Initially $\rho_0 = \mathrm{e}^{-\beta H_{\lambda_0}}/Z_0$. If $\rho_k = \mathrm{e}^{-\beta H_{\lambda_k}}/Z_0$, the work increment multiplies it by $\mathrm{e}^{-\beta(H_{\lambda_{k+1}} - H_{\lambda_k})}$, giving $\mathrm{e}^{-\beta H_{\lambda_{k+1}}}/Z_0$, and the subsequent relaxation leaves this distribution unchanged because it is stationary for the transition probability. By induction, $\rho_n = \mathrm{e}^{-\beta H_{\lambda_1}}/Z_0$, and integrating over $x$, $\langle\mathrm{e}^{-\beta W}\rangle = Z_1/Z_0 = \mathrm{e}^{-\beta\Delta F}$. $\square$

By Jensen's inequality, $\langle\mathrm{e}^{-\beta W}\rangle \ge \mathrm{e}^{-\beta\langle W\rangle}$, so the equality implies the second law $\langle W\rangle \ge \Delta F$. But it also implies that trajectories with $W < \Delta F$, which locally "violate" the second law, must occur; the exponential average is dominated by these rare trajectories, which is why it converges slowly and is biased for small samples when the dissipated work $\langle W\rangle - \Delta F$ exceeds a few $k_{\mathrm{B}}T$.

**Theorem 17.6.2 (Crooks Fluctuation Theorem)** Under the same conditions, let $P_{\mathrm{F}}(W)$ be the distribution of work in the forward protocol and $P_{\mathrm{R}}(W)$ that of the time-reversed protocol, started in equilibrium at $\lambda_1$. Then

$$
\frac{P_{\mathrm{F}}(W)}{P_{\mathrm{R}}(-W)} = \mathrm{e}^{(W - \Delta F)/k_{\mathrm{B}}T}.
$$
The two distributions cross at $W = \Delta F$. Integrating $P_{\mathrm{R}}(-W) = P_{\mathrm{F}}(W)\mathrm{e}^{-\beta(W - \Delta F)}$ over $W$ gives the Jarzynski equality.

The proof compares the probability of each forward trajectory with that of its time reverse; the ratio is $\mathrm{e}^{\beta(W - \Delta F)}$ by detailed balance at each step (Crooks 1999). It is the prototype of the fluctuation theorems of stochastic thermodynamics, developed in [7.6.38](/7.6.38).

![Free energies from irreversible pulling (simulation: a double-well molecule, barrier 3 k_BT, held by a harmonic trap of stiffness 5 k_BT per unit length squared that moves from −1.5 to 2.0 in two time units, overdamped Langevin dynamics, 3000 trajectories each way). A: the work distributions of forward pulling and of minus the reverse work are broad and far apart, the mean dissipation being about 5.5 k_BT, but they cross at the exact ΔF = 1.67 k_BT. B: the logarithm of their ratio is a straight line of slope 1 through ΔF, as the Crooks theorem states. C: the Jarzynski estimate from N forward trajectories (median and 10–90 % range of resamplings) starts near the mean work for a single trajectory and approaches ΔF only slowly, still biased by about 0.3 k_BT at N = 3000: the exponential average is dominated by rare low-work trajectories](./plots/jarzynski.py)

**Example 17.6.1 (Testing the Theorems with RNA)** Liphardt and colleagues (2002) unfolded the P5abc domain of the *Tetrahymena* intron in optical tweezers, reversibly at low pulling rates and irreversibly at high ones (dissipated work up to several $k_{\mathrm{B}}T$), and recovered the reversible free energy from the irreversible trajectories with the Jarzynski equality to within $k_{\mathrm{B}}T/2$. Collin and colleagues (2005) tested the Crooks theorem with an RNA three-helix junction and a destabilized mutant, and obtained the folding free energy of a structure that cannot be unfolded reversibly; the difference between wild type and mutant, $\Delta\Delta G$, agreed with bulk measurements. The method is now used to obtain free-energy landscapes from fast pulling, including in molecular simulations (steered molecular dynamics, [7.6.15](/7.6.15)).

## 17.7. Molecular Recognition: Affinity and Specificity

### 17.7.1. The Free Energy of Binding

Proteins, nucleic acids and small molecules recognize each other through many weak interactions, hydrogen bonds, salt bridges, van der Waals contacts and the hydrophobic effect ([7.6.6](/7.6.6)), arranged over complementary surfaces. A typical protein–protein interface buries $1200$–$2000\,\text{Å}^2$ of accessible surface in total. The standard binding free energy $\Delta G^\circ = RT\ln K_{\mathrm{d}}/c^\circ$ ranges widely:

| Interaction | $K_{\mathrm{d}}$ | $\Delta G^\circ$ at $25\,^\circ\mathrm{C}$ / $(\mathrm{kJ\,mol^{-1}})$ |
|---|---|---|
| Enzyme–substrate | $10^{-6}$–$10^{-3}\,\mathrm{M}$ | $-17$ to $-34$ |
| Signalling domain–peptide (SH2, SH3, PDZ) | $10^{-7}$–$10^{-5}\,\mathrm{M}$ | $-29$ to $-40$ |
| Transcription factor–specific site | $10^{-12}$–$10^{-9}\,\mathrm{M}$ | $-51$ to $-68$ |
| Antibody–antigen (after affinity maturation) | $10^{-12}$–$10^{-8}\,\mathrm{M}$ | $-46$ to $-68$ |
| Barnase–barstar | $10^{-14}\,\mathrm{M}$ | $-79$ |
| Streptavidin–biotin | $10^{-14}\,\mathrm{M}$ | $-79$ |

These numbers result from a balance. The favourable terms (contacts and hydrophobic burial) are opposed by the loss of translational and rotational entropy of two molecules that become one, estimated at $15$–$40\,\mathrm{kJ\,mol^{-1}}$ at $1\,\mathrm{M}$ standard state, by the loss of side-chain and backbone flexibility, and by the desolvation of polar groups that are buried. Calorimetry separates enthalpy from entropy ([7.6.8](/7.6.8#sec-8.4.4)) and shows widespread **enthalpy–entropy compensation**.

The free energy is not spread evenly over an interface. Clackson and Wells (1995) mutated each contact residue of human growth hormone and of its receptor to alanine (alanine scanning) and found that a few residues near the centre of the interface, largely tryptophans, tyrosines and arginines, contributed most of the binding free energy, while most contact residues contributed little: hot spots, surrounded by a rim that excludes water. Interactions between residues are measured by double-mutant cycles: if mutations at positions $i$ and $j$ change the binding free energy by $\Delta\Delta G_i$ and $\Delta\Delta G_j$ separately and by $\Delta\Delta G_{ij}$ together, the coupling energy $\Delta\Delta G_{\mathrm{int}} = \Delta\Delta G_{ij} - \Delta\Delta G_i - \Delta\Delta G_j$ is nonzero only if the two residues interact, directly or through structure (Horovitz and Fersht 1990). Nonadditivity of this kind is also what makes binding specificity evolvable and, in proteins, epistatic ([7.6.41](/7.6.41)).

### 17.7.2. Structural Modules of Recognition

Recognition is organized in a limited set of modular domains, each with a characteristic chemistry.

| Target | Modules (examples) | Recognition principle |
|---|---|---|
| DNA, major groove | **helix–turn–helix** (λ repressor), **homeodomain**, **zinc finger** (Zif268: three residues of each finger's helix read three bases), **leucine zipper** (GCN4: a coiled-coil dimer whose basic regions grip two major-groove half-sites) | hydrogen bonds from Asn, Gln, Arg, Lys to base edges in the major groove (direct readout); a recognition helix inserted into the groove; nonspecific salt bridges to phosphates ([7.2.14](/7.2.14#sec-14.2)) |
| DNA, minor groove and shape | TATA-binding protein (a β-sheet saddle that bends DNA by about $80^\circ$ and intercalates two Phe), p53 core domain | indirect readout of sequence-dependent DNA shape and deformability |
| RNA | RRM (RNP1, RNP2 motifs; $2$–$8$ nt), KH (GXXG loop; about $4$ nt, $\mu\mathrm{M}$ affinity), dsRBD (A-form helix, $2'$-OH), YTH (aromatic cage for $\mathrm{m^6A}$) | stacking on aromatic residues, $2'$-hydroxyl contacts (about $20\,\%$ of contacts), shape of loops; multiple domains combine weak sites |
| Peptides and modifications | **SH2 domain** (phosphotyrosine), SH3 (proline-rich PPII helix), **bromodomain** (acetyl-lysine), PHD and chromodomains (aromatic cage for methyl-lysine) | a pocket for the modified residue plus flanking residues for specificity |
| Small molecules, carbohydrates, lipids | GPCR orthosteric pockets, lectins and carbohydrate-binding modules, C1, C2, PH domains | deep pockets with shape and charge complementarity; avidity of multiple sites |

Many recognition events involve conformational change. In **induced fit** binding occurs first and the protein then changes conformation; in **conformational selection** the protein already samples the bound-like conformation, and the ligand binds and stabilizes it. Both are thermodynamically equivalent descriptions of the same cycle and can coexist; kinetically they differ, which allows them to be distinguished.

**Formula 17.7.1 (Kinetic Signatures of Binding Mechanisms)** With ligand $L$ in excess and the binding step fast, the observed rate constant of the slow, conformational relaxation is

$$
k_{\mathrm{obs}} = k_{-2} + k_2\frac{[L]}{K_1 + [L]} \quad\text{(induced fit, } \mathrm{P} + \mathrm{L} \rightleftharpoons \mathrm{PL} \rightleftharpoons \mathrm{PL}^*),
$$

$$
k_{\mathrm{obs}} = k_+ + k_-\frac{K_{\mathrm{d}}}{K_{\mathrm{d}} + [L]} \quad\text{(conformational selection, } \mathrm{P}' \rightleftharpoons \mathrm{P},\ \mathrm{P} + \mathrm{L} \rightleftharpoons \mathrm{PL}).
$$
Induced fit gives a rate that increases hyperbolically with $[L]$; conformational selection, a rate that decreases (when the conformational exchange is fast compared with binding, it may also increase, so a decreasing $k_{\mathrm{obs}}$ is the unambiguous signature).

**Proof** Induced fit: if binding equilibrates fast, the fraction of P that is bound is $[L]/(K_1 + [L])$, the forward conformational flux per protein is $k_2$ times this fraction, and the relaxation rate of the two-state slow step is the sum of forward and backward effective rates. Conformational selection: the active state P is depleted by fast binding, so the effective rate from P back to P′ is $k_-$ times the fraction of active-state protein that is free, $K_{\mathrm{d}}/(K_{\mathrm{d}} + [L])$, while $\mathrm{P}' \to \mathrm{P}$ is unaffected. $\square$

![Association kinetics. A: electrostatic steering in the Debye–Hückel form ln k_on = ln k_basal − (U/k_BT)/(1 + κa), with basal rate 5 × 10⁵ M⁻¹ s⁻¹ and contact distance 0.6 nm: oppositely charged proteins (U = −6 k_BT) associate up to 300 times faster at low ionic strength, about 30 times faster at physiological ionic strength (150 mM), still far below the Smoluchowski limit for spheres of 2 nm radius (dotted); like charges slow association. B: the relaxation rate after mixing a protein with excess ligand rises hyperbolically with ligand concentration for induced fit and falls for conformational selection (both with half-saturation at 50 µM, conformational rates 10 and 200 s⁻¹)](./plots/association-kinetics.py)

### 17.7.3. Sequence Specificity: The Energy-Matrix Model

How does a transcription factor's affinity depend on the sequence of its site? To a first approximation, each base pair of the site contributes independently.

**Definition 17.7.1 (Position Weight Matrix)** A *position weight matrix* (energy matrix) of a DNA-binding protein with a site of $\ell$ base pairs assigns to each position $i$ and base $b$ an energy $\varepsilon_i(b)$, usually relative to the consensus base; the binding energy of a site $\boldsymbol{s} = (s_1, \dots, s_\ell)$ is approximated as

$$
E(\boldsymbol{s}) = \sum_{i=1}^{\ell}\varepsilon_i(s_i),
$$
and the probability that the site is occupied, at a protein chemical potential $\mu$ set by the free protein concentration, is the Fermi function

$$
p_{\mathrm{bound}}(\boldsymbol{s}) = \frac{1}{1 + \mathrm{e}^{(E(\boldsymbol{s}) - \mu)/k_{\mathrm{B}}T}}.
$$

The occupancy has the form of the **Fermi–Dirac distribution** because each site holds at most one protein; it is the single-site version of the **thermodynamic model** of promoter occupancy ([7.2.11](/7.2.11)). Berg and von Hippel (1987) connected the matrix to sequence statistics: if the natural sites of a factor are a sample from a Boltzmann-like distribution of sequences of similar binding energy, the frequencies of bases at each position satisfy $p_i(b)/p_i(\mathrm{cons}) = \mathrm{e}^{-[\varepsilon_i(b) - \varepsilon_i(\mathrm{cons})]/k_{\mathrm{B}}T}$, so the energy matrix can be estimated as $\varepsilon_i(b) - \varepsilon_i(\mathrm{cons}) \approx -k_{\mathrm{B}}T\ln[p_i(b)/p_i(\mathrm{cons})]$ from an alignment of known sites, and the information content of a sequence logo ([7.8](/7.8)) is a measure of the energy discrimination at each position. In practice the effective temperature of this relation is not $T$; energy matrices are measured directly by high-throughput methods (protein-binding microarrays, SELEX-seq, Sort-Seq, in which a mutagenized promoter library is sorted by expression level and the mutual information between each base and expression maps the sites, Kinney and colleagues 2010).

![Sequence specificity in the energy-matrix model (hypothetical 10-bp site; penalties of 1–4 k_BT per mismatch, largest in the centre). A: the logo of sites drawn from the Boltzmann distribution p_i(b) ∝ e^−ε_i(b)/kT: the information at each position reflects the energy penalties. B: the binding energy along 600 bp of random sequence containing one consensus site at position 300 (blue) and the occupancy at μ = 2 k_BT (orange): only the consensus site is bound. C: the energies of all 4.6 × 10⁶ positions of a random genome form a broad, nearly Gaussian distribution centred near 15 k_BT; the number of occupied sites, the overlap of this distribution with the Fermi occupancy, grows from about 200 to 34 000 as the chemical potential rises from 0 to 6 k_BT: with too high a protein concentration, the factor binds thousands of near-consensus sites](./plots/pwm-specificity.py)

The model shows the problem of specificity in a genome. A random genome of $G = 4.6\times10^6\,\mathrm{bp}$ contains, for a site of $\ell$ bp, about $G/4^{\ell}$ exact consensus matches: one for $\ell \approx 11$. To find one site among millions, a factor needs a site long enough that consensus matches are rare and an energy gap between specific and nonspecific binding large enough ($\gtrsim 15$–$25\,k_{\mathrm{B}}T$) that the specific site competes with millions of weak ones; but the more base pairs contribute to the energy, the more binding energy is spent on discrimination and the rougher the landscape the protein encounters while searching, which slows the search (17.8.3).

## 17.8. Association and Target Search

### 17.8.1. Diffusion-Limited Association

Two molecules must first meet. For spheres of radii $R_{\mathrm{A}}$ and $R_{\mathrm{B}}$ that react on every contact, the Smoluchowski rate constant is $k_{\mathrm{D}} = 4\pi(D_{\mathrm{A}} + D_{\mathrm{B}})(R_{\mathrm{A}} + R_{\mathrm{B}})N_{\mathrm{A}}$ (a **diffusion-controlled reaction**, [6.3.17](/6.3.17); derivation in [7.6.5](/7.6.5#fml-5.2.3)), and with the Stokes–Einstein diffusion coefficients it becomes $8k_{\mathrm{B}}TN_{\mathrm{A}}/3\eta \approx 7\times10^9\,\mathrm{M^{-1}\,s^{-1}}$ in water, independent of size. Protein–protein association is much slower, typically $10^5$–$10^7\,\mathrm{M^{-1}\,s^{-1}}$, because only collisions with the binding sites properly aligned succeed: if each partner's site occupies a small fraction of its surface and orientations must match within a few degrees, the geometric factor is $10^{-4}$–$10^{-6}$. Rotational diffusion during a collision, in which the molecules stay close and reorient many times before separating, raises the rate by one to two orders of magnitude over this estimate (Northrup and Erickson 1992), to the observed range.

**Definition 17.8.1 (Electrostatic Steering)** *Electrostatic steering* is the acceleration of association by long-range electrostatic attraction between complementary charge distributions of two molecules, which raises the frequency of encounters and guides them into productive orientations. In a Debye–Hückel approximation, $\ln k_{\mathrm{on}} = \ln k_{\mathrm{on}}^{\mathrm{basal}} - (U/k_{\mathrm{B}}T)/(1 + \kappa a)$, with $U$ the electrostatic energy of the complex at contact in the absence of salt, $1/\kappa$ the **Debye length** and $a$ the contact distance.

Barnase and barstar associate at about $10^8\,\mathrm{M^{-1}\,s^{-1}}$ at $50\,\mathrm{mM}$ salt and approach $10^{10}$ at very low ionic strength, while uncharged mutants associate at about $10^5$–$10^6$ (Schreiber and Fersht 1996). Engineering charge complementarity has accelerated association of protein pairs by two orders of magnitude without changing $k_{\mathrm{off}}$. Enzymes of very high catalytic efficiency, superoxide dismutase and acetylcholinesterase, use electrostatic funnels to bring their small charged substrates into the active site at rates near the diffusion limit.

### 17.8.2. Facilitated Diffusion and the Optimal Search

Riggs, Bourgeois and Cohn (1970) found that the lac repressor finds its operator faster than three-dimensional diffusion to a site of molecular size allows; the resolution, sliding along nonspecific DNA, and the experiments on living cells are described in [7.2.22](/7.2.22#sec-22.2). Here the search time is derived.

**Definition 17.8.2 (Facilitated Diffusion)** In facilitated diffusion (Berg, Winter and von Hippel 1981) a protein searching for a site alternates rounds of three-dimensional diffusion in solution, of mean duration $\tau_{3\mathrm{D}}$ per round, with rounds of nonspecific binding to DNA, of mean duration $\tau_{1\mathrm{D}}$, during which it slides along the DNA with a one-dimensional diffusion coefficient $D_1$ and scans $n$ new base pairs. The *sliding length* is the distance $\ell_{\mathrm{sl}} \sim \sqrt{D_1\tau_{1\mathrm{D}}}$ covered in one round of sliding.

**Theorem 17.8.1 (Optimal Search Time)** If successive rounds land at uncorrelated positions on DNA of total length $M$ base pairs, the mean time to find one site is

$$
\tau_{\mathrm{s}} = \frac{M}{n}\left(\tau_{1\mathrm{D}} + \tau_{3\mathrm{D}}\right), \qquad n = \frac{1}{b}\sqrt{\frac{8D_1\tau_{1\mathrm{D}}}{\pi}},
$$
with $b = 0.34\,\mathrm{nm}$ per base pair. At fixed $\tau_{3\mathrm{D}}$, $\tau_{\mathrm{s}}$ is minimal for $\tau_{1\mathrm{D}} = \tau_{3\mathrm{D}}$: the protein should spend equal times on and off DNA, and then $\tau_{\mathrm{s}}^* = 2M\tau_{3\mathrm{D}}/n(\tau_{3\mathrm{D}})$, a speed-up by the factor $n/2$ over a purely three-dimensional search that tests one site per round.

**Proof** Each round scans $n$ new sites, so about $M/n$ rounds are needed to cover the DNA once when landing positions are uncorrelated, and each round lasts $\tau_{1\mathrm{D}} + \tau_{3\mathrm{D}}$ on average. The number of distinct sites visited by a one-dimensional random walk in time $t$ is its range, whose mean is $\sqrt{8D_1t/\pi}$ in length units (the expected maximum minus minimum of Brownian motion). Minimizing $(\tau_{1\mathrm{D}} + \tau_{3\mathrm{D}})/\sqrt{\tau_{1\mathrm{D}}}$ over $\tau_{1\mathrm{D}}$: the derivative $\frac12\tau_{1\mathrm{D}}^{-1/2} - \frac12\tau_{3\mathrm{D}}\tau_{1\mathrm{D}}^{-3/2}$ vanishes at $\tau_{1\mathrm{D}} = \tau_{3\mathrm{D}}$. $\square$

![Facilitated diffusion: the search time of one protein for one site in a 4.6 Mbp genome, with τ₃D = 1 ms per three-dimensional excursion. A: search time against the fraction of time bound nonspecifically for three one-dimensional diffusion coefficients: each curve has its minimum at equal times on and off DNA (dots), where each round scans n* = 15–66 bp; at 0.046 µm²/s, the value measured for lac repressor in *E. coli*, the optimal search takes about 5 min for one molecule, versus 77 min (dotted) if each round tested a single site; spending too much time sliding is as costly as spending too little. B: the speed–stability problem: a nonspecific landscape of roughness σ slows sliding as D₁ = D₀e^−(σ/kT)² (dashed, right axis; D₀ = 1 µm²/s) and the optimal search time rises steeply once σ exceeds 1–2 k_BT (shaded)](./plots/target-search.py)

**Example 17.8.1 (The lac Repressor in a Cell)** With $D_1 = 0.046\,\mu\mathrm{m^2\,s^{-1}}$ and $\tau_{1\mathrm{D}} = \tau_{3\mathrm{D}} = 1\,\mathrm{ms}$, $n = \sqrt{8\times4.6\times10^4\times10^{-3}/\pi}/0.34 \approx 32\,\mathrm{bp}$ and $\tau_{\mathrm{s}} = (4.6\times10^6/32)\times2\,\mathrm{ms} \approx 290\,\mathrm{s}$: about five minutes for one repressor, of the order measured in living *E. coli* by Hammar, Elf and colleagues (2012), and tens of seconds for the roughly ten repressors in a cell. The measured fraction of time bound nonspecifically, about $90\,\%$ (Elf, Li and Xie 2007), is higher than the optimum of the simple theory; correlated rebinding (hops to nearby sites that are rescanned), crowding, intersegment transfer and the large amount of DNA-bound protein that competes for the same DNA modify the optimum in vivo.

### 17.8.3. The Speed–Stability Problem

Sliding requires a smooth landscape. A protein that reads the sequence while sliding experiences an energy that varies from base pair to base pair with a standard deviation $\sigma$ (for an energy matrix, the spread of the distribution in panel C of the energy-matrix figure). Diffusion in a random potential of Gaussian roughness is slowed by the factor $\mathrm{e}^{-(\sigma/k_{\mathrm{B}}T)^2}$ (Zwanzig 1988), so fast sliding needs $\sigma \lesssim 1$–$2\,k_{\mathrm{B}}T$, while a stable specific complex needs an energy gap of $15$–$25\,k_{\mathrm{B}}T$, which for an additive matrix implies a roughness of several $k_{\mathrm{B}}T$. Slutsky and Mirny (2004) proposed the resolution: the protein has two conformations, a search mode bound loosely to DNA that is nearly insensitive to sequence, and a recognition mode that reads the bases and binds tightly, with fast switching between them. The p53 core domain, Cas9 and the *E. coli* repressors show features of such two-mode searches ([7.2.22](/7.2.22#sec-22.2.3)); the lac repressor often slides over its operator without binding, as the two-mode model predicts.

## 17.9. Kinetic Proofreading

### 17.9.1. The Equilibrium Limit

At equilibrium, a single binding step discriminates between a correct substrate C and a wrong one D, present at equal concentrations, only by the ratio of their affinities: the error is at least $f_0 = K_{\mathrm{d},C}/K_{\mathrm{d},D} = \mathrm{e}^{-\Delta\Delta G/k_{\mathrm{B}}T}$, a **Boltzmann factor**. For a codon–anticodon pair differing by one base pair, $\Delta\Delta G \approx 3$–$5\,k_{\mathrm{B}}T$ and $f_0 \approx 10^{-2}$, while translation makes about $10^{-4}$ errors per codon and DNA replication, with mismatches costing $\sim 9\,k_{\mathrm{B}}T$ ($f_0 \approx 10^{-4}$), achieves $10^{-9}$–$10^{-10}$ with proofreading and repair. **Kinetic proofreading** (Hopfield 1974; Ninio 1975) closes the gap by repeating the selection after an irreversible, energy-consuming step; its scheme for translation and its derivation are in [7.2.19](/7.2.19#fml-19.8.2), where the error is shown to approach $f_0^2$ for one proofreading step and $f_0^{n+1}$ for $n$ steps.

### 17.9.2. Energy, Accuracy and Speed

The proofreading scheme is a cycle, E → EX → EX\* → E, driven by the hydrolysis of a nucleoside triphosphate. Its thermodynamic force is the cycle affinity

$$
\Delta\mu = k_{\mathrm{B}}T\ln\frac{k_{\mathrm{on}}m\,l}{k_{\mathrm{off}}m_{\mathrm{r}}l_{\mathrm{on}}},
$$
the product of forward over reverse rate constants around the cycle, equal to the free energy released by one hydrolysis. If the cycle were at equilibrium ($\Delta\mu = 0$), the intermediate EX\* would be in equilibrium with free E and X and the discrimination would not multiply: the error would be $f_0$. Only a driven cycle proofreads.

**Proposition 17.9.1 (Limits of Proofreading)** In Hopfield's scheme with a wrong substrate that dissociates from both bound states $q = 1/f_0$ times faster than the correct one, the steady-state error $f$ satisfies $f_0^2 \lesssim f \le f_0$: $f = f_0$ at $\Delta\mu = 0$ and $f \to f_0^2$ only when $\Delta\mu \gg k_{\mathrm{B}}T\ln q^2$, the activation step is slow compared with dissociation and the product step slow compared with discard. Achieving the full gain requires both energy (several tens of $k_{\mathrm{B}}T$ per cycle for $q = 100$) and slowness, and every correct substrate discarded at the proofreading step is a hydrolysis wasted.

**Proof** At $\Delta\mu = 0$ all fluxes vanish around the cycle and the populations of EC\* and ED\* are Boltzmann-distributed relative to free E; the product fluxes $W[\mathrm{EX^*}]$ then stand in the ratio of the equilibrium constants, $f_0$. For $\Delta\mu \to \infty$ the reverse steps vanish and the flux expression of [7.2.19](/7.2.19#fml-19.8.2) applies, whose limit is $f_0^2$. Intermediate values follow by continuity of the steady state in the rates, and the steady-state error is monotonic in $\Delta\mu$ for this scheme, as the numerical solution in the figure shows. $\square$

![Kinetic proofreading. A: steady-state error of Hopfield's scheme with thermodynamically consistent reverse rates (correct substrate: k_on = 1, k_off = 1, activation m = 0.01, discard l = 1, product W = 10⁻³; wrong substrate discarded 100 times faster from both bound states), solved exactly as a five-state Markov chain: the error falls from the equilibrium value f₀ = 10⁻² at zero driving force to near f₀² = 10⁻⁴ when the cycle is driven by more than about 20 k_BT. B: at full driving, varying the activation rate m trades speed (the steady-state fraction of enzyme in the productive state EC*) against accuracy: slow activation gives more time for wrong substrates to leave and lowers the error but slows production; at very slow activation the product step competes with discard and the error rises again. C: kinetic proofreading in T-cell activation: a T-cell receptor bound to a peptide–MHC ligand must complete N modification steps at k_p = 1 s⁻¹ before signalling; the probability of reaching the signalling state, (k_p/(k_p + k_off))^N, separates ligands with dwell times of 2 s and 0.2 s by 4-fold for N = 1 but 4096-fold for N = 6](./plots/proofreading.py)

Studies of the ribosome (Banerjee, Kolomeisky and Igoshin 2017) and of DNA polymerase show that natural proofreading operates far from its maximal accuracy, near the optimum of speed: the observed rates make translation fast at a modest energetic cost, with an error of $10^{-4}$, well above what the energy spent could buy. This is consistent with the trade-offs described for gene expression in [7.2.22](/7.2.22#sec-22.7) and with the growth-rate cost of hyperaccurate ribosomes.

**Example 17.9.1 (T-Cell Recognition)** A T cell must respond to a few agonist peptide–MHC complexes among $10^4$–$10^5$ self-peptide complexes on an antigen-presenting cell, which differ in their dwell time on the T-cell receptor by perhaps a factor of ten (seconds against tenths of a second) rather than in affinity by orders of magnitude. McKeithan (1995) proposed that the receptor must complete a series of $N$ modifications (phosphorylation of its ITAMs, recruitment of ZAP-70 and so on) before it signals, each reversed when the ligand leaves: the fraction of engagements that signal, $(k_{\mathrm{p}}/(k_{\mathrm{p}} + k_{\mathrm{off}}))^N$, amplifies a tenfold difference in dwell time into a difference of $10^N$ at long dwell times. The kinetic-proofreading model explains why T-cell activation correlates with ligand dwell time; catch bonds, which lengthen the dwell time of agonists under the forces of the immunological synapse, add a mechanical layer of proofreading ([7.15](/7.15)).

## 17.10. Measuring Interactions

### 17.10.1. Surface Plasmon Resonance and Mass Transport

**Surface plasmon resonance** ([6.4.9](/6.4.9); basic kinetics in [7.3.3](/7.3.3#sec-3.6.3)) records the binding of an analyte flowing over a sensor surface with an immobilized ligand in real time, as a change in refractive index within about $200\,\mathrm{nm}$ of a gold film. Fitting association and dissociation phases at several concentrations with the 1:1 model gives $k_{\mathrm{on}}$, $k_{\mathrm{off}}$ and $K_{\mathrm{D}}$. The most common systematic error is mass transport: when binding to the surface is fast, the analyte near the surface is depleted during association and rebinds during dissociation, so both phases are slowed.

**Formula 17.10.1 (Two-Compartment Model)** If transport from the bulk to the surface is described by a transport coefficient $k_{\mathrm{t}}$ (in response units per molar per second) and the concentration at the surface is in quasi-steady state,

$$
\frac{\mathrm{d}R}{\mathrm{d}t} = \frac{k_{\mathrm{on}}C(R_{\max} - R) - k_{\mathrm{off}}R}{1 + k_{\mathrm{on}}(R_{\max} - R)/k_{\mathrm{t}}} ,
$$
(Myszka and colleagues 1998), where $k_{\mathrm{t}}$ grows with the flow rate as $(\text{flow})^{1/3}$ (Lévêque's solution of the convection–diffusion problem in a thin channel). Transport limitation is significant when the Damköhler number $\mathrm{Da} = k_{\mathrm{on}}R_{\max}/k_{\mathrm{t}}$ approaches or exceeds $1$.

![Surface plasmon resonance with mass-transport limitation (simulation; k_on = 10⁶ M⁻¹ s⁻¹, k_off = 10⁻³ s⁻¹, R_max = 100 RU; analyte injected for 300 s at 3, 10 and 30 nM). A: in the reaction-limited case (k_t = 10¹⁰ RU M⁻¹ s⁻¹, solid) binding follows the 1:1 model; with transport limitation (k_t = 10⁸ RU M⁻¹ s⁻¹, Damköhler number 1, dashed) association is slower and dissociation is slowed by rebinding. B: fitting the transport-limited data globally with the simple 1:1 model gives an apparently good fit, but k_on and k_off are both underestimated (by about 40 % and 25 %) and the residuals are systematic, several times the noise; K_D, the ratio, is less affected. Remedies are low ligand densities, high flow rates, global fits with the two-compartment model and a check that the rates do not depend on flow](./plots/spr-transport.py)

### 17.10.2. Other Methods

| Method | Principle | Measures | Notes |
|---|---|---|---|
| Biolayer interferometry (BLI) | White light reflected from the two surfaces of a biolayer on a fibre-optic tip interferes; binding increases the optical thickness $n d$ and shifts the interference spectrum by $\Delta\lambda \propto \Delta(nd)$ | $k_{\mathrm{on}}$, $k_{\mathrm{off}}$, $K_{\mathrm{D}}$, label-free | dip-and-read in plates, no microfluidics; less sensitive than SPR for small analytes |
| Fluorescence anisotropy | A small labelled ligand tumbles fast (low anisotropy); bound to a large protein it tumbles slowly (high anisotropy, the Perrin equation, [7.6.11](/7.6.11#sec-11.5.5)) | equilibrium binding in solution, competition assays | the measured anisotropy is the brightness-weighted average, $r = (f_{\mathrm{b}}Qr_{\mathrm{b}} + (1 - f_{\mathrm{b}})r_{\mathrm{f}})/(f_{\mathrm{b}}Q + 1 - f_{\mathrm{b}})$ with $Q$ the brightness ratio |
| Microscale thermophoresis (MST) | An infrared laser creates a temperature gradient; molecules move along it with a Soret coefficient $S_{\mathrm{T}}$ that changes on binding, $c_{\mathrm{hot}}/c_{\mathrm{cold}} = \mathrm{e}^{-S_{\mathrm{T}}\Delta T}$ | $K_{\mathrm{D}}$ in solution, small sample volumes | sensitive to size, charge and hydration; one partner labelled or intrinsically fluorescent |
| Isothermal titration calorimetry | Heat of binding during a titration ([7.6.8](/7.6.8#sec-8.4)) | $K$, $\Delta H$, $n$, hence $\Delta S$ | the thermodynamic reference method; needs large amounts |
| Single-molecule fluorescence and force | Dwell times of single complexes ([7.6.12](/7.6.12)), force-dependent lifetimes (17.5) | $k_{\mathrm{off}}$ distributions, heterogeneity, force dependence | the only methods that see heterogeneity and mechanochemistry |

## Summary

| Topic | Key relations |
|---|---|
| Force scale (17.1) | $k_{\mathrm{B}}T = 4.1\,\mathrm{pN\,nm}$; $k_{\mathrm{B}}T/\mathrm{nm} \approx 4\,\mathrm{pN}$; motors $1$–$10\,\mathrm{pN}$, unfolding $10$–$300\,\mathrm{pN}$, covalent $\sim 2\,\mathrm{nN}$ |
| Optical tweezers (17.2) | $F_{\mathrm{grad}} \propto a^3\nabla I$ (Formula 17.2.1); $\kappa = k_{\mathrm{B}}T/\langle x^2\rangle$, $S(f) = k_{\mathrm{B}}T/[\pi^2\gamma(f_{\mathrm{c}}^2 + f^2)]$, $f_{\mathrm{c}} = \kappa/2\pi\gamma$ (Formula 17.2.2); $\delta x = \sqrt{4k_{\mathrm{B}}T\gamma B}/\kappa$ |
| Magnetic tweezers, AFM (17.3) | constant force, $F = k_{\mathrm{B}}Tl/\langle\delta x^2\rangle$ (Formula 17.3.1); torque and supercoiling; AFM $k_{\mathrm{c}} = k_{\mathrm{B}}T/\langle z^2\rangle$, sawtooth of polyproteins |
| Elasticity (17.4) | FJC Langevin function; WLC Marko–Siggia (Formula 17.4.1); DNA: $A = 50\,\mathrm{nm}$, $S \approx 1000$–$1500\,\mathrm{pN}$, overstretching at $65\,\mathrm{pN}$; two-state under force $K(F) = K(0)\mathrm{e}^{F\Delta x/k_{\mathrm{B}}T}$ (Formula 17.4.2) |
| Rupture (17.5) | Bell $k = k_0\mathrm{e}^{Fx^\ddagger/k_{\mathrm{B}}T}$ (Definition 17.5.1); $F^* = (k_{\mathrm{B}}T/x^\ddagger)\ln(rx^\ddagger/k_0k_{\mathrm{B}}T)$ (Theorem 17.5.1); slip, catch, ideal bonds |
| Fluctuation theorems (17.6) | $\langle\mathrm{e}^{-W/k_{\mathrm{B}}T}\rangle = \mathrm{e}^{-\Delta F/k_{\mathrm{B}}T}$ (Theorem 17.6.1); $P_{\mathrm{F}}(W)/P_{\mathrm{R}}(-W) = \mathrm{e}^{(W - \Delta F)/k_{\mathrm{B}}T}$ (Theorem 17.6.2) |
| Affinity (17.7) | hot spots; double-mutant cycles; induced fit vs conformational selection by $k_{\mathrm{obs}}([L])$ (Formula 17.7.1) |
| Specificity | energy matrix $E(\boldsymbol{s}) = \sum_i\varepsilon_i(s_i)$, $p = 1/(1 + \mathrm{e}^{(E - \mu)/k_{\mathrm{B}}T})$ (Definition 17.7.1); genomic background |
| Association, search (17.8) | Smoluchowski $\approx 7\times10^9\,\mathrm{M^{-1}\,s^{-1}}$; electrostatic steering (Definition 17.8.1); $\tau_{\mathrm{s}} = (M/n)(\tau_{1\mathrm{D}} + \tau_{3\mathrm{D}})$, optimum $\tau_{1\mathrm{D}} = \tau_{3\mathrm{D}}$ (Theorem 17.8.1); speed–stability, two-mode search |
| Proofreading (17.9) | $f_0 = \mathrm{e}^{-\Delta\Delta G/k_{\mathrm{B}}T}$; $f_0 \ge f \gtrsim f_0^2$ only with driving $\Delta\mu$ (Proposition 17.9.1); speed–accuracy trade-off; T-cell receptor $(k_{\mathrm{p}}/(k_{\mathrm{p}} + k_{\mathrm{off}}))^N$ |
| Measurement (17.10) | SPR with transport limitation (Formula 17.10.1); BLI, anisotropy, MST, ITC |

## Questions

1. A bead in an optical trap fluctuates with a standard deviation of $6\,\mathrm{nm}$ at $25\,^\circ\mathrm{C}$. What is the trap stiffness, and what force does a displacement of $80\,\mathrm{nm}$ correspond to? If the bead has radius $0.5\,\mu\mathrm{m}$, what is the corner frequency?

   **Answer** $\kappa = k_{\mathrm{B}}T/\langle x^2\rangle = 4.11/36 = 0.114\,\mathrm{pN\,nm^{-1}}$; $F = 0.114\times80 = 9.1\,\mathrm{pN}$. With $\gamma = 6\pi\eta a = 8.4\times10^{-6}\,\mathrm{pN\,s\,nm^{-1}}$, $f_{\mathrm{c}} = \kappa/2\pi\gamma = 0.114/(5.28\times10^{-5}) = 2.2\,\mathrm{kHz}$.

2. Why is the power-spectrum calibration preferred to equipartition when the detector sensitivity (volts per nanometre) is not known precisely?

   **Answer** Equipartition needs the variance in nm², so an error in the conversion factor enters squared. The Lorentzian's corner frequency $f_{\mathrm{c}} = \kappa/2\pi\gamma$ is independent of the conversion; with $\gamma$ from Stokes' law (corrected by Faxén's law near a surface) it gives $\kappa$ directly, and the plateau then calibrates the detector, $S(0) = 4\gamma k_{\mathrm{B}}T/\kappa^2$.

3. A magnetic-tweezers tether has extension $2.0\,\mu\mathrm{m}$ and transverse fluctuations of standard deviation $90\,\mathrm{nm}$. What is the force? Compare with the force predicted for a $3.4\,\mu\mathrm{m}$ DNA at this extension by the worm-like chain.

   **Answer** $F = k_{\mathrm{B}}Tl/\langle\delta x^2\rangle = 4.11\times2000/8100 = 1.0\,\mathrm{pN}$. For $x/L = 0.59$, Formula 17.4.1 gives $FA/k_{\mathrm{B}}T = 0.59 + 1/(4\times0.168) - 0.25 = 1.83$, so $F = 1.83\times4.11/50 = 0.15\,\mathrm{pN}$; at $1\,\mathrm{pN}$ the WLC predicts $x/L \approx 0.85$ ($2.9\,\mu\mathrm{m}$). The discrepancy means the tether is not a $3.4\,\mu\mathrm{m}$ DNA: for example it is shorter, or partly supercoiled or bound by proteins.

4. Using Formula 17.4.1, what force is needed to extend DNA to $90\,\%$ of its contour length, and how does this compare with the freely jointed chain with $b = 2A$?

   **Answer** WLC: $FA/k_{\mathrm{B}}T = 0.9 + 1/(4\times0.01) - 0.25 = 25.65$, $F = 25.65\times4.11/50 = 2.1\,\mathrm{pN}$. FJC: solve $\coth u - 1/u = 0.9$, i.e. approximately $u = 10$, so $F = 10k_{\mathrm{B}}T/b = 41.1/100 = 0.41\,\mathrm{pN}$. The FJC underestimates the force at high extension by about fivefold because it lacks the many short-wavelength bending modes of a continuous chain.

5. A hairpin has $F_{1/2} = 14.0\,\mathrm{pN}$ and $\Delta x = 20\,\mathrm{nm}$. What is the free energy of unfolding at $F_{1/2}$ in $k_{\mathrm{B}}T$, and at what force is it open $90\,\%$ of the time?

   **Answer** $\Delta G = F_{1/2}\Delta x = 280\,\mathrm{pN\,nm} = 68\,k_{\mathrm{B}}T$ (this includes the work of stretching the released strand). $p_{\mathrm{U}} = 0.9$ requires $(F - F_{1/2})\Delta x/k_{\mathrm{B}}T = \ln 9 = 2.20$, $F = 14.0 + 2.20\times4.11/20 = 14.45\,\mathrm{pN}$.

6. Rupture forces of a receptor–ligand bond are $40\,\mathrm{pN}$ at $100\,\mathrm{pN\,s^{-1}}$ and $59\,\mathrm{pN}$ at $10^4\,\mathrm{pN\,s^{-1}}$. Find $x^\ddagger$ and $k_0$ in the Bell model, and the lifetime at $10\,\mathrm{pN}$.

   **Answer** Slope $= 19/\ln 100 = 4.13\,\mathrm{pN}$ per e-fold $= k_{\mathrm{B}}T/x^\ddagger$, so $x^\ddagger = 1.0\,\mathrm{nm}$. From $F^* = (k_{\mathrm{B}}T/x^\ddagger)\ln(rx^\ddagger/k_0k_{\mathrm{B}}T)$ at $r = 100$: $40/4.13 = 9.69 = \ln(100\times1.0/(4.11k_0))$, so $k_0 = 24.3/\mathrm{e}^{9.69} = 1.5\times10^{-3}\,\mathrm{s^{-1}}$. At $10\,\mathrm{pN}$, $k = 1.5\times10^{-3}\mathrm{e}^{10/4.11} = 1.7\times10^{-2}\,\mathrm{s^{-1}}$, lifetime about $60\,\mathrm{s}$.

7. (Design) How would you show that a bond is a catch bond rather than a slip bond with two bound states of different lifetime?

   **Answer** Measure lifetimes at constant force (force clamp in a biomembrane force probe, AFM or optical trap) over a range of forces and repeated cycles on the same molecule. A catch bond shows a mean lifetime that increases with force over some range; a mixture of two slip-bond populations shows lifetimes that decrease with force for each population, with biexponential lifetime distributions whose fractions do not depend on force in the way required for catch behaviour. Force-ramp experiments alone are ambiguous; complementary tests are mutations or ligands that lock the protein in one conformation (for FimH or selectins), which should abolish the catch regime, and force-jump experiments that show the transition to the long-lived state after force is applied.

8. Pulling a molecule irreversibly gives works of $W = 12.1, 10.4, 15.3, 11.0$ and $13.6\,k_{\mathrm{B}}T$ in five trials. Estimate $\Delta F$ by the Jarzynski equality and comment on the estimate.

   **Answer** $\langle\mathrm{e}^{-W}\rangle = (\mathrm{e}^{-12.1} + \mathrm{e}^{-10.4} + \mathrm{e}^{-15.3} + \mathrm{e}^{-11.0} + \mathrm{e}^{-13.6})/5$; relative to $\mathrm{e}^{-10.4}$ the terms are $0.183, 1, 0.0074, 0.549, 0.041$, sum $1.78$, so $\langle\mathrm{e}^{-W}\rangle = 1.78\mathrm{e}^{-10.4}/5$ and $\Delta F = 10.4 - \ln(1.78/5) = 10.4 + 1.03 = 11.4\,k_{\mathrm{B}}T$, below the mean work $12.5\,k_{\mathrm{B}}T$. With five samples and a work spread of several $k_{\mathrm{B}}T$, the estimate is biased upwards (it is dominated by the lowest observed work and rarer, lower works have not been sampled); the true $\Delta F$ is probably lower. More trajectories, slower pulling or the Crooks method with reverse trajectories would be needed.

9. A transcription factor binds a $12$-bp site. How many exact matches to its consensus are expected in a random genome of $4.6\times10^6\,\mathrm{bp}$, counting both strands? If each mismatch costs $3\,k_{\mathrm{B}}T$, how many sites lie within $6\,k_{\mathrm{B}}T$ of the consensus, and why does this matter?

   **Answer** Exact matches: $2\times4.6\times10^6/4^{12} = 9.2\times10^6/1.68\times10^7 = 0.55$. Sites with one mismatch: $12\times3$ variants, $2\times4.6\times10^6\times36/4^{12} = 20$; with two: $\binom{12}{2}\times9 = 594$ variants, about $330$ sites. So about $350$ sites lie within $6\,k_{\mathrm{B}}T$ of the best site; if the protein concentration (chemical potential) is high enough to occupy the consensus site strongly, many of these will be occupied too, and nonspecific near-consensus sites compete for the protein (the background of panel C). Specificity requires either a longer site, larger mismatch penalties or regulation of the protein's concentration.

10. Using Theorem 17.8.1 with $D_1 = 0.05\,\mu\mathrm{m^2\,s^{-1}}$ and $\tau_{3\mathrm{D}} = 0.5\,\mathrm{ms}$, compute the optimal sliding time, the number of base pairs scanned per round and the search time in a $4.6\,\mathrm{Mbp}$ genome. How does the search time change if the protein spends $95\,\%$ of its time on DNA?

    **Answer** Optimum $\tau_{1\mathrm{D}} = 0.5\,\mathrm{ms}$; $n = \sqrt{8\times5\times10^4\times5\times10^{-4}/\pi}/0.34 = \sqrt{63.7}/0.34 = 23.5\,\mathrm{bp}$; $\tau_{\mathrm{s}} = (4.6\times10^6/23.5)\times10^{-3}\,\mathrm{s} = 196\,\mathrm{s}$. With $95\,\%$ bound, $\tau_{1\mathrm{D}} = 19\times0.5 = 9.5\,\mathrm{ms}$, $n = 23.5\sqrt{19} = 102\,\mathrm{bp}$, $\tau_{\mathrm{s}} = (4.6\times10^6/102)\times10\,\mathrm{ms} = 450\,\mathrm{s}$, about $2.3$ times longer.

11. An enzyme discriminates two substrates by $\Delta\Delta G = 4\,k_{\mathrm{B}}T$ in binding. What error does equilibrium selection give, and with one and two ideal proofreading steps? Why can the cell not achieve the latter at no cost?

    **Answer** $f_0 = \mathrm{e}^{-4} = 1.8\times10^{-2}$; one step $f_0^2 = 3.4\times10^{-4}$; two steps $f_0^3 = 6.1\times10^{-6}$. Each proofreading step requires an irreversible, energy-driven transition (the driving force must be large compared with $k_{\mathrm{B}}T\ln q^2$, Proposition 17.9.1), discards some correct substrates (each costing a hydrolysis), and requires slow forward steps so that wrong substrates have time to leave, which reduces speed. Accuracy is traded against energy and speed.

12. In an SPR experiment, the apparent $k_{\mathrm{on}}$ increases by $40\,\%$ when the flow rate is raised from $10$ to $100\,\mu\mathrm{L\,min^{-1}}$. What does this indicate, and how would you obtain the true rate constants?

    **Answer** Rates that depend on flow indicate mass-transport limitation: the transport coefficient grows as $(\text{flow})^{1/3}$, by $10^{1/3} = 2.2$-fold, and the apparent association approaches the true one as $k_{\mathrm{t}}$ grows. Remedies: lower the ligand density on the chip (smaller $R_{\max}$, hence smaller Damköhler number), use higher flow, fit globally with the two-compartment model (Formula 17.10.1) including $k_{\mathrm{t}}$ as a parameter, and confirm that the fitted $k_{\mathrm{on}}$ and $k_{\mathrm{off}}$ no longer depend on flow or density; for dissociation, inject a competitor or soluble ligand to block rebinding.
