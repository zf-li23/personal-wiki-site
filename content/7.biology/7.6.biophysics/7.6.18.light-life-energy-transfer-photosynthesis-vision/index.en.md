---
title: "Light and Life: Energy Transfer, Photosynthesis and Vision"
description: The physics of light in biology. Photon fluxes and energy scales of sunlight; pigments as particle-in-a-box and Hückel systems, absorption cross-sections and the fates of an excitation; Förster transfer, excitons and the antenna as a random walk to a trap; charge separation, electron tunneling, Marcus theory with its inverted region and the Moser–Dutton ruler; the thermodynamic limit of storing a photon; bacteriorhodopsin, channelrhodopsins, optogenetics and the photoreceptors of plants and microbes; rhodopsin photoisomerization, single-photon detection, the Hecht–Shlaer–Pirenne experiment, dark noise, colour vision and the optics of camera and compound eyes.
---

Light is both the main source of free energy for the biosphere and its richest source of information. In both roles the first step is the same quantum event: a pigment absorbs a photon of about $2\,\mathrm{eV}$, nearly a hundred times the thermal energy, and is left in an excited state that lives for nanoseconds or less. What follows decides the use. In photosynthesis the excitation hops through an antenna of hundreds of pigments to a reaction center, where it drives an electron across a membrane by tunneling; in vision and in the photoreceptors of microbes and plants it twists a chromophore and switches a protein. This chapter treats the physics of these steps with deliberately simple models, in the style of *Physical Biology of the Cell*: photon counting (18.1), pigments as boxes for electrons (18.2), excitation energy transfer and light harvesting (18.3), electron transfer by tunneling and Marcus theory (18.4), retinal proteins and other photoreceptors (18.5) and vision as a photon counter limited by noise and optics (18.6). The biochemistry of photosynthesis (the photosystems, the Z scheme, water splitting and photophosphorylation) is in [7.1.24](/7.1.24), and the signalling cascade of the rod in [7.1.14](/7.1.14#sec-14.4.1); they are used here, not repeated. The quantum mechanics of the particle in a box and of tunneling is in [5.5.3](/5.5.3), the spectroscopy of absorption, fluorescence and Förster transfer in [7.6.11](/7.6.11), and the quantum effects that are still debated, the coherence of energy transfer and the magnetic compass of birds, in [7.6.19](/7.6.19).

## 18.1. Light as Energy and Information

### 18.1.1. Photons from the Sun

The Sun radiates approximately as a black body at $5772\,\mathrm{K}$; above the atmosphere the irradiance is the solar constant, $1361\,\mathrm{W\,m^{-2}}$, and at sea level with the Sun overhead about $1000\,\mathrm{W\,m^{-2}}$, a rule of thumb used throughout this chapter. About $37\,\%$ of the energy lies between $400$ and $700\,\mathrm{nm}$, the band used by oxygenic photosynthesis and by our eyes (photosynthetically active radiation, PAR). Since a pigment absorbs photons one at a time, what matters is the number of photons, not the energy.

**Formula 18.1.1 (Photon Energy and Photon Flux)** A **photon** of wavelength $\lambda$ carries $E = hc/\lambda$, which is

$$
E = \frac{1239.8\,\mathrm{eV\,nm}}{\lambda}, \qquad \frac{E}{k_{\mathrm{B}}T} = \frac{46\,400\,\mathrm{nm}}{\lambda}\quad(T = 310\,\mathrm{K}), \tag{18.1}
$$
and an irradiance $I$ of monochromatic light delivers the photon flux $j = I\lambda/(hc)$ per unit area.

**Example 18.1.1 (Photons per Pigment)** At $\lambda = 500\,\mathrm{nm}$, $E = 2.48\,\mathrm{eV} = 3.97\times10^{-19}\,\mathrm{J} = 93\,k_{\mathrm{B}}T$. Treating $1000\,\mathrm{W\,m^{-2}}$ as $500\,\mathrm{nm}$ light gives $j = 2.5\times10^{21}\,\mathrm{m^{-2}\,s^{-1}}$, that is $2500$ photons per $\mathrm{nm^2}$ per second. A chlorophyll molecule is about $1\,\mathrm{nm}$ across, but its absorption cross-section is much smaller than its geometric area: from the molar absorption coefficient $\varepsilon \approx 10^{5}\,\mathrm{M^{-1}\,cm^{-1}}$ at the peak of its red band, Formula 18.2.2 gives $\sigma \approx 0.04\,\mathrm{nm^2}$, and averaged over the solar spectrum about a quarter of that. A chlorophyll in full sunlight is therefore excited only some $10$–$25$ times per second, once every $40$–$100\,\mathrm{ms}$. In the shade of a canopy, a hundred times less.

The reaction center that converts the excitation into separated charges can work much faster (18.4.1): its slowest steps take about a millisecond. A reaction center fed only by its own pigments would be idle almost all the time. This simple count is the reason for antennas (18.3).

![Sunlight as a supply of photons. A: spectral irradiance above the atmosphere, approximated by a black body at 5772 K scaled to 1361 W m⁻²; the shaded band is photosynthetically active radiation (400–700 nm, 37 % of the energy). B: the same light counted as photons per nanometre; the photon spectrum peaks further to the red than the energy spectrum, because red photons carry less energy each; the upper axis gives the photon energy in units of kBT at 310 K. C: a photon compared with other energies of the cell (logarithmic axis): a visible photon carries 50–100 kBT, two to five times the free energy of ATP hydrolysis in the cell and more than one electron needs to go from water to NADP⁺](./plots/solar-photons.py)

### 18.1.2. Energy Scales

Panel C of the figure fixes the scale of the problem. A visible photon carries $1.8$–$3\,\mathrm{eV}$ ($70$–$110\,k_{\mathrm{B}}T$), far above anything thermal fluctuations can supply: the chance that a pigment is thermally excited to its first singlet state at $310\,\mathrm{K}$ is of order $\mathrm{e}^{-70} \approx 10^{-30}$. That is why light can drive chemistry uphill, and why a photoreceptor can be both very sensitive and very quiet (18.6.4). On the other side, the photon energy is only a few times the free energies that cells must produce: the transfer of one electron from water to $\ce{NADP+}$, $1.14\,\mathrm{eV}$ ($43\,k_{\mathrm{B}}T$, [7.1.24](/7.1.24#sec-24.3.2)), or the $20\,k_{\mathrm{B}}T$ of ATP hydrolysis. Much of the design of photosynthesis is about not wasting the difference while making the products irreversible.

### 18.1.3. The Fates of an Excitation

An excited pigment returns to its ground state by one of several competing routes ([7.6.11](/7.6.11#sec-11.1), [6.3.17](/6.3.17)): emission of **fluorescence**, **internal conversion** to heat, intersystem crossing to the **triplet state**, transfer of the excitation to a neighbouring pigment, or transfer of an electron to an acceptor. Each route is a first-order process with its own rate constant, and the routes compete.

**Formula 18.1.2 (Branching of an Excitation)** If an excited state decays by parallel first-order processes with rate constants $k_i$, its lifetime is $\tau = 1/\sum_i k_i$ and the yield of process $j$ is

$$
\Phi_j = \frac{k_j}{\sum_i k_i} = k_j\tau. \tag{18.2}
$$

Since the intrinsic decay of chlorophyll takes about $5\,\mathrm{ns}$ (fluorescence **quantum yield** $0.3$ in solution), any useful process must take well below a nanosecond to win. Photosynthesis is a sequence of such competitions: energy transfer (femtoseconds to picoseconds) beats decay; charge separation (picoseconds) beats energy transfer back to the antenna; each further electron transfer beats the recombination of the separated charges. The table lists the time scales; they span twenty orders of magnitude, from the absorption of a photon to the growth of a tree.

| Process | Time scale |
|---|---|
| Absorption of a photon | $10^{-15}\,\mathrm{s}$ |
| Vibrational relaxation, excitation transfer between neighbouring pigments | $10^{-13}$–$10^{-12}\,\mathrm{s}$ |
| Transfer through an antenna to the reaction center (trapping) | $10^{-11}$–$10^{-10}\,\mathrm{s}$ |
| Primary charge separation | $10^{-12}\,\mathrm{s}$ |
| Stabilization of the charge by transfer to a quinone | $10^{-10}\,\mathrm{s}$ |
| Fluorescence of isolated chlorophyll | $10^{-8}\,\mathrm{s}$ |
| Quinone exchange, water oxidation, proton translocation | $10^{-4}$–$10^{-3}\,\mathrm{s}$ |
| Carbon fixation by rubisco (turnover) | $1\,\mathrm{s}$ |
| Growth and division of a cell | $10^{4}$–$10^{5}\,\mathrm{s}$ |

## 18.2. Pigments as Boxes for Electrons

### 18.2.1. The Particle-in-a-Box Model of a Conjugated Chain

Biological pigments, the chlorophylls, carotenoids, bilins and retinal, have one feature in common: a large system of conjugated double bonds, in which $\pi$ electrons are delocalized over many atoms. The simplest model treats these electrons as free particles in a one-dimensional box whose length is the length of the conjugated system, the **infinite square well** of [5.5.3](/5.5.3#sec-3.2). Its levels are $E_n = h^2n^2/(8m_{\mathrm{e}}L^2)$; the confinement energy, of order $\hbar^2/(2m_{\mathrm{e}}L^2)$ by the **Heisenberg uncertainty relation**, is a few electronvolts for $L$ of a nanometre, just the energy of visible photons.

**Formula 18.2.1 (Free-Electron Model of a Polyene)** A linear conjugated chain of $N$ atoms ($N$ even) with spacing $a$ has $N$ $\pi$ electrons, which fill the levels $n = 1, \dots, N/2$ in pairs. The lowest absorption, from the highest occupied level (HOMO, $n = N/2$) to the lowest unoccupied one (LUMO, $n = N/2 + 1$), has

$$
\Delta E = \frac{h^2}{8m_{\mathrm{e}}L^2}(N + 1), \qquad \lambda = \frac{hc}{\Delta E} = \frac{8m_{\mathrm{e}}c\,L^2}{h\,(N + 1)}, \qquad L = (N - 1)a. \tag{18.3}
$$

**Example 18.2.1** For $N = 22$, the conjugated length of β-carotene, and $a = 0.14\,\mathrm{nm}$, $L = 2.94\,\mathrm{nm}$, $h^2/(8m_{\mathrm{e}}L^2) = 0.0435\,\mathrm{eV}$ and $\Delta E = 23 \times 0.0435 = 1.00\,\mathrm{eV}$, $\lambda = 1240\,\mathrm{nm}$. β-carotene actually absorbs at $452\,\mathrm{nm}$ ($2.74\,\mathrm{eV}$). With $a = 0.10\,\mathrm{nm}$, the value used in some textbooks, the model gives $632\,\mathrm{nm}$ and seems to work; but the carbon–carbon distance in a polyene is $0.13$–$0.15\,\mathrm{nm}$, and the apparent agreement is fortuitous.

The model gets the main trend right: longer conjugated systems absorb at longer wavelengths, because confinement energies fall as $1/L^2$ while the number of electrons, and with it the index of the HOMO, grows only as $L$; the gap therefore falls as $1/L$. A chain of 15–25 atoms absorbs in the visible, the size of the conjugated systems of all biological pigments. Chlorophyll, whose $\pi$ system is a ring rather than a chain, is better described as a particle on a ring, with the same scaling.

### 18.2.2. Beyond the Box: Bond Alternation and the Protein Environment

The free-electron model fails quantitatively for long polyenes because the bonds are not equal: double bonds are shorter than single bonds, and the alternating coupling opens a gap that stays finite as the chain grows. The **Hückel molecular orbital method** ([6.5.2](/6.5.2)) with two alternating resonance integrals $\beta_{\mathrm{d}}$ and $\beta_{\mathrm{s}}$ captures this: the gap of an infinite chain is $2\lvert\beta_{\mathrm{d}} - \beta_{\mathrm{s}}\rvert$, and with parameters fitted to butadiene and to the long carotenoids the absorption saturates near $580\,\mathrm{nm}$ (the measured optical gap of polyacetylene is about $1.5$–$2\,\mathrm{eV}$). In cyanine dyes, whose positive charge is delocalized so that all bonds are equal, the free-electron model works well, as Hans Kuhn showed in 1948.

![Absorption wavelength of a conjugated chain of N atoms. A: free-electron (particle-in-a-box) model with L = (N − 1)a (solid) or L = (N + 1)a (dashed), a = 0.14 nm, and with a = 0.10 nm (dotted); Hückel model with alternating couplings (4.10 and 3.03 eV, fitted to butadiene and to a 22-atom chain), whose absorption saturates at 578 nm for an infinite chain; points, approximate absorption maxima in hexane of butadiene, hexatriene, β-carotene and lycopene. The shaded band is the visible range. B: levels of the free-electron box for N = 22 (a = 0.14 nm): eleven doubly occupied levels, and the HOMO–LUMO transition](./plots/pigment-box.py)

Proteins tune the absorption of their pigments over a wide range. Retinal bound to a lysine as a protonated Schiff base absorbs at about $440\,\mathrm{nm}$ in methanol, but at $498\,\mathrm{nm}$ in rhodopsin, $560\,\mathrm{nm}$ in the long-wavelength cone pigment and $568\,\mathrm{nm}$ in bacteriorhodopsin (the opsin shift). The positive charge of the Schiff base is partly delocalized along the chain in the excited state; moving the negative counterion away from the nitrogen, placing polar residues along the chain, or flattening the ring–chain torsion all lower the gap. Chlorophyll a absorbs at $662\,\mathrm{nm}$ in ether but at $670$–$680\,\mathrm{nm}$ in light-harvesting proteins and beyond $700\,\mathrm{nm}$ in the "red" pigments of photosystem I, partly by **exciton coupling** with neighbours ([7.6.11](/7.6.11#def-11.2.1)).

### 18.2.3. Why Life Uses Pigments

Proteins themselves absorb only in the ultraviolet, below about $300\,\mathrm{nm}$, through their aromatic side chains; nucleic acids at $260\,\mathrm{nm}$. Sunlight at the surface of the Earth has almost no photons below $300\,\mathrm{nm}$. Every biological photoreceptor that works in visible light therefore carries a **chromophore** with an extended conjugated system, made by a dedicated pathway or taken from food (retinal from vitamin A, flavins from riboflavin). The one exception proves the rule: the plant UV-B receptor UVR8 uses tryptophan side chains as its chromophore (18.5.3), precisely because it is meant to detect ultraviolet.

The strength of absorption is set by the **transition dipole moment** ([7.6.11](/7.6.11#def-11.1.1)), and is conveniently expressed as a cross-section.

**Formula 18.2.2 (Absorption Cross-Section)** A molecule with molar absorption coefficient $\varepsilon$ (in $\mathrm{M^{-1}\,cm^{-1}}$) has the absorption cross-section

$$
\sigma = \frac{\ln 10\;\varepsilon}{N_{\mathrm{A}}} = 3.82\times10^{-21}\,\mathrm{cm^2}\times\frac{\varepsilon}{\mathrm{M^{-1}\,cm^{-1}}}, \tag{18.4}
$$
and in a photon flux $j$ it is excited at the rate $\sigma j$.

**Proof** In a layer of thickness $\mathrm{d}x$ containing $n$ molecules per unit volume, a fraction $\sigma n\,\mathrm{d}x$ of the photons is absorbed, so $I = I_0\mathrm{e}^{-\sigma nx}$. The **Lambert–Beer law** writes the same attenuation as $I = I_0\,10^{-\varepsilon cx}$. With $c$ in $\mathrm{mol\,L^{-1}}$, $n = 1000\,N_{\mathrm{A}}c$ molecules per $\mathrm{m^3}$; equating the exponents, $\sigma n = \ln10\,\varepsilon c$, gives $\sigma = \ln10\,\varepsilon/(1000\,N_{\mathrm{A}})$ in $\mathrm{m^2}$ when $\varepsilon$ is in $\mathrm{L\,mol^{-1}\,m^{-1}}$, that is $\sigma = \ln10\,\varepsilon/N_{\mathrm{A}}$ in $\mathrm{cm^2}$ when $\varepsilon$ is in $\mathrm{L\,mol^{-1}\,cm^{-1}} = 1000\,\mathrm{cm^3\,mol^{-1}\,cm^{-1}}$; numerically $2.303/6.022\times10^{23} \times 1000\,\mathrm{cm^2} = 3.82\times10^{-21}\,\mathrm{cm^2}$ per unit of $\varepsilon$. $\square$

For chlorophyll ($\varepsilon \approx 10^{5}$) $\sigma = 3.8\times10^{-16}\,\mathrm{cm^2} = 0.038\,\mathrm{nm^2}$, about $4\,\%$ of its geometric size; for rhodopsin ($\varepsilon = 40\,600\,\mathrm{M^{-1}\,cm^{-1}}$ at $498\,\mathrm{nm}$) $0.016\,\mathrm{nm^2}$. A rod outer segment, which stacks about $10^8$ rhodopsins in the light path, absorbs some $50$–$70\,\%$ of the photons that enter it along its axis.

## 18.3. Excitation Energy Transfer and Light Harvesting

### 18.3.1. Why Antennas

The count of Example 18.1.1 says that a reaction center needs the help of many pigments. Robert Emerson and William Arnold measured how many in 1932: with saturating flashes short enough that each reaction center works only once, *Chlorella* evolved one $\ce{O2}$ per about $2500$ chlorophylls, and since $8$–$10$ photons are needed per $\ce{O2}$, about $300$ chlorophylls serve each photochemical reaction (the photosynthetic unit, [7.1.24](/7.1.24#sec-24.2.4)). Most pigments are in **light-harvesting complexes**; any of them can absorb a photon and pass the excitation on to the **reaction center**. The antenna is a solid-state device: pigments are held by proteins at distances of $1$–$2\,\mathrm{nm}$ and fixed orientations, and the excitation, not an electron, moves between them.

**Example 18.3.1 (Antenna Size)** If one pigment is excited $10$ times per second in full sunlight and a reaction center can turn over every $2$–$5\,\mathrm{ms}$ (the time needed to exchange its quinone and pass electrons on), it can use $200$–$500$ excitations per second: $20$–$50$ pigments per reaction center would saturate it in full sunlight, and several hundred are needed to keep it busy in the shade. Plants adjust the antenna size to the light they grow in: shade leaves have more LHCII per reaction center than sun leaves, and in strong light the excess excitation is dissipated as heat by nonphotochemical quenching ([7.13](/7.13)).

### 18.3.2. Weak and Strong Coupling

How the excitation moves depends on the ratio of two energies: the electronic coupling $V$ between the transition dipoles of neighbouring pigments, and the width of their absorption bands, which measures how strongly each pigment is coupled to the vibrations of its surroundings (the reorganization energy and the static disorder of site energies).

- Weak coupling ($V$ much smaller than the bandwidths, pigments more than about $2\,\mathrm{nm}$ apart): the excitation hops incoherently from pigment to pigment, at the rate of **Förster resonance energy transfer**, $k = \tau_{\mathrm{D}}^{-1}(R_0/R)^6$ ([7.6.11](/7.6.11#thm-11.5.4)). Between chlorophylls the Förster radius is large, $5$–$8\,\mathrm{nm}$, because the absorption band is intense and the Stokes shift small: at $R = 2\,\mathrm{nm}$ the transfer takes picoseconds.
- Strong coupling ($V$ comparable to or larger than the bandwidths): the excitation is shared coherently by several pigments as an exciton ([7.6.11](/7.6.11#thm-11.2.1)), the absorption bands shift and split, and energy flows between exciton states by relaxation, in tens to hundreds of femtoseconds.
- At very short distances (below about $1\,\mathrm{nm}$) the point-dipole formula itself fails; orbital overlap adds exchange (Dexter) coupling, and the coupling must be computed from the transition densities.

Real antennas contain all three regimes. In the LH2 complex of purple bacteria, 18 bacteriochlorophylls form a tightly coupled ring (B850, $V \approx 300\,\mathrm{cm^{-1}}$) whose excitons are delocalized over several pigments at room temperature, while a second ring of nine more distant pigments (B800) transfers its energy to B850 in about $0.7\,\mathrm{ps}$ by a generalized Förster mechanism. Transfer from LH2 to the larger LH1 ring takes $3$–$5\,\mathrm{ps}$ and from LH1 to the reaction center about $35\,\mathrm{ps}$, the slowest step, because the pigments of LH1 are more than $4\,\mathrm{nm}$ from the special pair. Overall, an excitation absorbed anywhere in the membrane reaches a reaction center in $50$–$100\,\mathrm{ps}$, a hundred times faster than it would decay.

### 18.3.3. The Energy Funnel and Trapping

Seen from a distance, the antenna is a lattice on which the excitation performs a **random walk** ([7.6.5](/7.6.5#sec-5.1)) until it is caught at the reaction center or lost. The questions are those of a **first-passage time** problem ([7.6.5](/7.6.5#sec-5.6)): how long the search takes, and what fraction of excitations is caught.

**Formula 18.3.1 (Random Walk to a Trap)** On a periodic square lattice of $N$ sites with one perfect trap, a random walker starting on a random site needs on average (Montroll 1969)

$$
\langle n\rangle \approx \frac{N}{\pi}\ln N + 0.195\,N \tag{18.5}
$$
steps to reach the trap. If the trap catches the excitation only at a finite rate $k_{\mathrm{cs}}$ and the excitation spreads evenly over the antenna between visits, the mean trapping time is approximately the sum of a migration time and a trap-limited time,

$$
\tau_{\mathrm{trap}} \approx \frac{\langle n\rangle}{z\,k_{\mathrm{h}}} + \frac{N}{k_{\mathrm{cs}}}, \tag{18.6}
$$
where $k_{\mathrm{h}}$ is the hopping rate to each of the $z$ neighbours. The yield of trapping is $\Phi = 1/(1 + \tau_{\mathrm{trap}}/\tau_0)$, with $\tau_0$ the lifetime of the excitation in the antenna.

The $N\ln N$ is the signature of a two-dimensional walk, which revisits sites often (in three dimensions the search time grows only as $N$). With hops of $0.5\,\mathrm{ps}$ and $N = 225$, the migration part is about $50\,\mathrm{ps}$; with $k_{\mathrm{cs}} = (1\,\mathrm{ps})^{-1}$ the trap-limited part is $225\,\mathrm{ps}$, and $\Phi = 0.89$ for $\tau_0 = 2\,\mathrm{ns}$. Measured trapping in photosystem II takes $200$–$300\,\mathrm{ps}$, and analysis of its fluorescence kinetics shows that it is indeed largely trap-limited: the excitation visits the reaction center many times, equilibrating over the antenna before charge separation succeeds.

A shallow energy gradient helps. If pigments farther from the reaction center absorb at shorter wavelengths, downhill hops are favoured over uphill ones by the **Boltzmann factor**, as detailed balance requires ([7.6.3](/7.6.3#sec-3.5)): the excitation is concentrated near the trap. The model in the figure shows that a funnel of a few $k_{\mathrm{B}}T$ raises the yield of a large antenna from $0.6$ to above $0.9$ and shortens the trapping time several-fold. The price is energy: each $k_{\mathrm{B}}T$ of funnel depth is lost as heat. Natural antennas use funnels of only a few $k_{\mathrm{B}}T$ (the B800 → B850 → B875 → P870 cascade of purple bacteria spans about $0.25\,\mathrm{eV}$, $10\,k_{\mathrm{B}}T$; plant LHCII and the core of PSII are nearly isoenergetic, with energy differences of $1$–$2\,k_{\mathrm{B}}T$), a compromise between speed and the free energy delivered to the reaction center.

![The antenna as a random walk to a trap, computed from the master equation (square lattice of N pigments with periodic boundaries; nearest-neighbour hops of 0.5 ps obeying detailed balance; trapping from the central reaction center at (1 ps)⁻¹; decay everywhere at (2 ns)⁻¹; excitation starting on a random site). A: a funnel of depth 3 kBT on a 15 × 15 antenna: contour lines of the site energy and the time-integrated occupation (logarithmic colour scale), concentrated around the reaction center (star); 96.8 % of excitations are trapped. B: trapping yield against antenna size for funnel depths 0–6 kBT. C: mean trapping time of a flat antenna (dots) compared with Montroll's random walk to a trap plus the trap-limited time N/k_cs (Formula 18.3.1), and with a 3-kBT funnel (squares)](./plots/antenna-trapping.py)

### 18.3.4. Is Energy Transfer Coherent?

Between strongly coupled pigments, energy moves as a wave-like exciton for a few hundred femtoseconds before the vibrations of the protein destroy the phase relation. In 2007 two-dimensional electronic spectroscopy of the bacterial FMO complex at $77\,\mathrm{K}$ showed oscillations lasting more than $600\,\mathrm{fs}$, and it was proposed that long-lived electronic coherence makes transfer efficient, perhaps by a quantum search. Later work showed that most long-lived oscillations are vibrational, and that electronic coherence decays within about $100\,\mathrm{fs}$ at physiological temperature; the efficiency of transfer is explained by fast incoherent hopping between exciton states, assisted by the noise of the environment. The debate, and a model that shows why some dephasing helps rather than hurts, is treated in [7.6.19](/7.6.19#sec-19.6).

## 18.4. Electron Transfer

### 18.4.1. Charge Separation in the Reaction Center

In the reaction center, the excitation of the special pair of (bacterio)chlorophylls is converted into separated charges by a chain of electron transfers across the membrane. The structure of the purple bacterial reaction center ([7.1.24](/7.1.24#sec-24.3.1)) shows the cofactors at fixed distances, and ultrafast spectroscopy has timed each step:

| Step (purple bacterial reaction center, room temperature) | Time constant |
|---|---|
| $\mathrm{P}^* \to \mathrm{P}^+\mathrm{B}_{\mathrm{A}}^-$ (special pair to the accessory bacteriochlorophyll) | about $3\,\mathrm{ps}$ |
| $\mathrm{B}_{\mathrm{A}}^- \to \mathrm{H}_{\mathrm{A}}^-$ (to bacteriopheophytin) | below $1\,\mathrm{ps}$ |
| $\mathrm{H}_{\mathrm{A}}^- \to \mathrm{Q}_{\mathrm{A}}^-$ (to the bound quinone) | about $200\,\mathrm{ps}$ |
| $\mathrm{Q}_{\mathrm{A}}^- \to \mathrm{Q}_{\mathrm{B}}^-$ | about $100\,\mu\mathrm{s}$ |
| Reduction of $\mathrm{P}^+$ by cytochrome $c_2$ | $0.3$–$1\,\mu\mathrm{s}$ |
| Recombination $\mathrm{P}^+\mathrm{H}_{\mathrm{A}}^- \to \mathrm{P}$ (if $\mathrm{Q}_{\mathrm{A}}$ is removed) | about $10$–$20\,\mathrm{ns}$ |
| Recombination $\mathrm{P}^+\mathrm{Q}_{\mathrm{A}}^- \to \mathrm{P}$ (if $\mathrm{Q}_{\mathrm{B}}$ is blocked) | about $100\,\mathrm{ms}$ |

Each forward step is $10^2$–$10^6$ times faster than the recombination it competes with, so by Formula 18.1.2 nearly every absorbed photon produces a stable charge separation; the quantum yield of the primary reaction is close to one. The chain moves the electron about $3\,\mathrm{nm}$ across the membrane in $200\,\mathrm{ps}$ while the separated charges live long enough, milliseconds to seconds, for slow chemistry to use them. Two puzzles remain: how an electron jumps between cofactors $1$–$2\,\mathrm{nm}$ apart that are not in contact, and why the recombination of $\mathrm{P}^+\mathrm{Q}_{\mathrm{A}}^-$, which releases more free energy than any forward step, is the slowest of all.

### 18.4.2. Electron Tunneling

The first puzzle is solved by the **tunnel effect** ([5.5.3](/5.5.3#sec-3.3.2)). An electron bound by an energy $V_0 - E$ in a donor does not stop sharply at the edge of its potential well; its wave function decays into the classically forbidden region as $\mathrm{e}^{-x/\xi}$.

**Formula 18.4.1 (Tunneling Length)** For an electron bound by $V_0 - E$, the decay length of the wave function outside the well is

$$
\xi = \frac{\hbar}{\sqrt{2m_{\mathrm{e}}(V_0 - E)}} = \frac{0.195\,\mathrm{nm}}{\sqrt{(V_0 - E)/\mathrm{eV}}}. \tag{18.7}
$$
The overlap of donor and acceptor wave functions, and with it the electronic coupling $H_{\mathrm{DA}}$, falls as $\mathrm{e}^{-R/\xi}$ with the distance $R$, so the transfer rate falls as $\mathrm{e}^{-\beta R}$ with $\beta = 2/\xi$.

For a binding energy of $1$–$4\,\mathrm{eV}$, $\xi = 0.1$–$0.2\,\mathrm{nm}$ and $\beta = 10$–$20\,\mathrm{nm^{-1}}$: the rate falls tenfold for every $0.1$–$0.2\,\mathrm{nm}$. Harry Gray and Jay Winkler measured this directly in the 1990s by attaching ruthenium complexes to histidines at different sites on the surface of the copper protein azurin and timing the transfer after a laser flash: the rate fell from $10^{10}$ to $10^{2}\,\mathrm{s^{-1}}$ as the copper–ruthenium distance grew from $1.2$ to $2.6\,\mathrm{nm}$, with $\beta \approx 11\,\mathrm{nm^{-1}}$ along the β strands of the protein. Tunneling through vacuum is much steeper ($\beta \approx 30\,\mathrm{nm^{-1}}$) and through water intermediate ($16$–$17\,\mathrm{nm^{-1}}$): the bonds of the protein mediate the coupling.

The simplest model of a transfer is a "molecule" of two potential wells, A and B, coupled by $H$. An electron placed in A oscillates to B and back with probability $P_{\mathrm{B}}(t) = [4H^2/(4H^2 + \Delta^2)]\sin^2(\sqrt{4H^2 + \Delta^2}\,t/2\hbar)$, where $\Delta$ is the energy difference between the wells: complete transfer requires resonance, and a mismatch of a few $H$ suppresses it. Two ingredients turn this oscillation into an irreversible rate. The product state is not a single level but a continuum of vibrational states, so the electron, once in B, does not come back; and the levels of donor and acceptor fluctuate with the nuclear motions of the protein and solvent, coming into resonance from time to time. The first ingredient gives Fermi's golden rule for the rate, $k = (2\pi/\hbar)\lvert H_{\mathrm{DA}}\rvert^2\rho$, with $\rho$ the density of final states that conserve energy ([7.6.11](/7.6.11#thm-11.1.2)); the second fixes $\rho$ and is the subject of Marcus theory.

![Electron tunneling between redox cofactors. A: decay length ξ of a bound electron's wave function outside its well against the binding energy (Formula 18.4.1). B: the Moser–Dutton ruler (Formula 18.4.2): the maximal (activationless) transfer rate against the edge-to-edge distance for media of different packing density ρ, β = 9ρ + 28(1 − ρ) nm⁻¹; dotted lines mark time scales, and the shaded band the distances of most physiological electron-transfer steps. C: the two-well model: probability that an electron starting in well A is found in well B, for an energy mismatch Δ of 0, 2 and 6 times the coupling H](./plots/electron-tunneling.py)

### 18.4.3. Marcus Theory

When an electron moves from donor to acceptor, the charges change and the surrounding dipoles, of the protein, of water and of the cofactors themselves, must rearrange. Rudolph Marcus (Nobel Prize in Chemistry 1992) described these nuclear motions by a single collective coordinate $q$ and the free energy of the system with the electron on the donor or on the acceptor as two parabolas of the same curvature.

**Definition 18.4.1 (Reorganization Energy)** Let $G_{\mathrm{D}}(q) = \lambda q^2$ and $G_{\mathrm{A}}(q) = \lambda(q - 1)^2 + \Delta G^\circ$ be the free energies of the reactant (electron on the donor) and product (electron on the acceptor) states along a nuclear coordinate $q$ scaled so that the minima lie at $q = 0$ and $q = 1$. The **reorganization energy** $\lambda$ is the free energy needed to distort the nuclei from the equilibrium configuration of the reactants into that of the products without transferring the electron, $\lambda = G_{\mathrm{D}}(1) - G_{\mathrm{D}}(0)$. It is the sum of an inner part (bond lengths of donor and acceptor) and an outer part (polarization of the medium).

The electron can only jump, by the Franck–Condon principle, at a nuclear configuration where its energy is the same on donor and acceptor: at the crossing point $q^*$ of the two parabolas.

**Theorem 18.4.1 (Marcus Theory)** In the non-adiabatic limit (weak electronic coupling $H_{\mathrm{DA}}$) and with classical nuclear motion, the rate of electron transfer at temperature $T$ is

$$
k_{\mathrm{ET}} = \frac{2\pi}{\hbar}\lvert H_{\mathrm{DA}}\rvert^2\frac{1}{\sqrt{4\pi\lambda k_{\mathrm{B}}T}}\exp\left[-\frac{(\Delta G^\circ + \lambda)^2}{4\lambda k_{\mathrm{B}}T}\right]. \tag{18.8}
$$
The activation free energy is $\Delta G^{\ddagger} = (\Delta G^\circ + \lambda)^2/(4\lambda)$.

**Proof** The parabolas cross where $\lambda q^2 = \lambda(q - 1)^2 + \Delta G^\circ$, at $q^* = (1 + \Delta G^\circ/\lambda)/2$, where $G_{\mathrm{D}}(q^*) = \lambda q^{*2} = (\lambda + \Delta G^\circ)^2/(4\lambda)$; this is $\Delta G^\ddagger$. In the golden-rule rate $k = (2\pi/\hbar)\lvert H_{\mathrm{DA}}\rvert^2\rho$, the density of states $\rho$ is the probability density, per unit energy, that thermal fluctuations bring the energy gap $\varepsilon = G_{\mathrm{A}} - G_{\mathrm{D}} = \lambda(1 - 2q) + \Delta G^\circ$ to zero. In the reactant well $q$ is Gaussian with variance $k_{\mathrm{B}}T/(2\lambda)$ (Boltzmann distribution of $\lambda q^2$), so $\varepsilon$ is Gaussian with mean $\Delta G^\circ + \lambda$ and variance $4\lambda^2\cdot k_{\mathrm{B}}T/(2\lambda) = 2\lambda k_{\mathrm{B}}T$. Its density at $\varepsilon = 0$ is $(4\pi\lambda k_{\mathrm{B}}T)^{-1/2}\exp[-(\Delta G^\circ + \lambda)^2/(4\lambda k_{\mathrm{B}}T)]$, which gives Eq. (18.8). $\square$

The prefactor is the Franck–Condon-weighted density of states; the exponential is a **Boltzmann factor** for reaching the crossing point, as in **transition state theory** ([6.3.16](/6.3.16)). The surprising consequence is in the quadratic dependence on $\Delta G^\circ$.

**Definition 18.4.2 (Inverted Region)** With increasing driving force $-\Delta G^\circ$ the Marcus rate rises (the normal region, $-\Delta G^\circ < \lambda$), reaches its maximum when $-\Delta G^\circ = \lambda$ (activationless transfer), and falls again when $-\Delta G^\circ > \lambda$: this regime is the **Marcus inverted region**, in which the product parabola crosses the reactant parabola on its inner side.

Marcus predicted the inverted region in 1960; it was found experimentally only in 1984, by Closs and Miller in donor–spacer–acceptor molecules, because in solution very exergonic reactions are usually limited by diffusion. In real molecules the inverted region is shallower than Eq. (18.8) predicts: high-frequency vibrations of the products (C=C and C=O stretches, $h\nu \approx 0.15$–$0.2\,\mathrm{eV}$) can absorb the excess energy, opening channels that end in vibrationally excited products (the Marcus–Levich–Jortner extension, dashed in the figure).

**Example 18.4.1** With $\lambda = 0.6\,\mathrm{eV}$ at $298\,\mathrm{K}$ ($k_{\mathrm{B}}T = 25.7\,\mathrm{meV}$), a reaction with $\Delta G^\circ = -0.3\,\mathrm{eV}$ has $\Delta G^\ddagger = 0.3^2/2.4 = 0.0375\,\mathrm{eV} = 1.5\,k_{\mathrm{B}}T$, while one with $\Delta G^\circ = -1.5\,\mathrm{eV}$ has $\Delta G^\ddagger = 0.9^2/2.4 = 0.34\,\mathrm{eV} = 13.1\,k_{\mathrm{B}}T$: although it releases five times more free energy, it is $\mathrm{e}^{11.7} \approx 10^5$ times slower at the same coupling.

![Marcus theory. A: free-energy parabolas along the nuclear coordinate (λ = 0.5 eV) for the donor state and for acceptor states in the normal region (ΔG° = −0.2 eV), activationless (−0.5 eV) and inverted (−1.0 eV); dots mark the crossing points, whose height is the activation free energy. B: logarithm of the rate against the driving force for λ = 0.25, 0.5 and 1 eV (|H_DA| = 1 meV, 298 K), and for λ = 0.5 eV split into a classical solvent part and a quantized vibration (dashed), which makes the inverted region shallower; the points mark a forward step and a recombination with −ΔG° = 0.5 and 1.2 eV. C: temperature dependence for λ = 0.5 eV: the activationless reaction is almost independent of temperature, the others slow down on cooling](./plots/marcus.py)

### 18.4.4. The Moser–Dutton Ruler and the Design of Reaction Centers

Les Dutton and Christopher Moser analysed the rates of dozens of intraprotein electron transfers, in reaction centers and other redox proteins, and found that a single empirical formula, combining the exponential distance dependence with the Marcus factor, describes them within an order of magnitude.

**Formula 18.4.2 (Moser–Dutton Ruler)** For electron transfer between cofactors whose edges are a distance $R$ apart in a protein,

$$
\log_{10}\frac{k_{\mathrm{ET}}}{\mathrm{s^{-1}}} = 13 - 6\,\frac{R - 0.36\,\mathrm{nm}}{\mathrm{nm}} - 3.1\,\frac{(\Delta G^\circ + \lambda)^2}{\lambda\cdot\mathrm{eV}}, \tag{18.9}
$$
where $10^{13}\,\mathrm{s^{-1}}$ is the rate at van der Waals contact and the slope of $6$ decades per nanometre corresponds to $\beta = 14\,\mathrm{nm^{-1}}$ for an average protein packing density; denser regions tunnel with $\beta$ down to $9\,\mathrm{nm^{-1}}$, loose ones up to $28\,\mathrm{nm^{-1}}$ (Page et al. 1999).

The ruler says that in proteins the distance dominates: the details of the protein matter less than one might expect. It also explains the design of the reaction center. Cofactors closer than about $1.4\,\mathrm{nm}$ exchange electrons faster than milliseconds, so a chain of redox centres spaced by less than $1.4\,\mathrm{nm}$ conducts electrons through any protein, the principle of the long respiratory chains ([7.1.23](/7.1.23)); centres farther apart are effectively insulated.

**Example 18.4.2 (Forward Transfer versus Recombination)** Take a forward step over $R = 1.0\,\mathrm{nm}$ with $\Delta G^\circ = -0.5\,\mathrm{eV}$ and $\lambda = 0.5\,\mathrm{eV}$ (activationless): $\log_{10}k = 13 - 6\times0.64 = 9.2$, $k \approx 1.4\times10^{9}\,\mathrm{s^{-1}}$, a time constant of $0.7\,\mathrm{ns}$. The recombination over the same distance releases $1.2\,\mathrm{eV}$; its Marcus term is $3.1\times0.7^2/0.5 = 3.0$, so $\log_{10}k = 6.1$, about one microsecond, $1000$ times slower. The reaction center places its forward steps near the activationless optimum and its recombinations deep in the inverted region, and keeps the low-$\lambda$ environment of a hydrophobic protein interior ($\lambda \approx 0.2$–$0.7\,\mathrm{eV}$, compared with about $1\,\mathrm{eV}$ for small ions in water) so that the inverted region begins early. This is the answer to the second puzzle of 18.4.1. The primary charge separation is in fact activationless: it runs about twice as fast at $10\,\mathrm{K}$ as at room temperature, a striking confirmation of panel C of the figure.

### 18.4.5. How Much of a Photon Can Be Stored

A red photon carries $1.82\,\mathrm{eV}$ (P680) but the separated charges store less, even in an ideal converter, for a reason of statistical thermodynamics. Absorbed light maintains a population of excited pigments far above its thermal value, but far below that of a population in equilibrium with radiation at the temperature of the Sun.

**Formula 18.4.3 (Free Energy of an Excitation)** If light keeps a fraction $f$ of pigments excited, while in the dark (at temperature $T$) the equilibrium fraction is $f_{\mathrm{eq}} = g\,\mathrm{e}^{-E/k_{\mathrm{B}}T}$ ($E$ the excitation energy, $g$ a ratio of degeneracies), the excited state has the chemical potential

$$
\Delta\mu = k_{\mathrm{B}}T\ln\frac{f}{f_{\mathrm{eq}}} = E - k_{\mathrm{B}}T\ln\frac{g}{f}, \tag{18.10}
$$
the maximal work that can be extracted per excitation.

**Example 18.4.3** In full sunlight a chlorophyll is excited about $10$ times per second and the excitation lives about $2\,\mathrm{ns}$, so $f = 2\times10^{-8}$; with $g \approx 3$, $k_{\mathrm{B}}T\ln(g/f) = 0.0257\times18.8 = 0.48\,\mathrm{eV}$, and $\Delta\mu \approx 1.34\,\mathrm{eV}$ of the $1.82\,\mathrm{eV}$. This estimate (Duysens 1958; Ross and Calvin 1967) shows that about a quarter of the photon energy is lost unavoidably, whatever the mechanism; the free energy actually stored by the photosystems ($\mathrm{P680^+}$ and $\mathrm{Q_A^-}$ differ by about $1.2\,\mathrm{V}$) is close to this limit.

Following the energy further, through the losses of the Z scheme, the respiration of the plant and the photorespiration of rubisco, gives the familiar maximal efficiencies of photosynthesis in the field: about $4.6\,\%$ of the total solar energy converted into biomass for C3 plants and $6\,\%$ for C4 plants (Zhu, Long and Ort 2008), achieved only briefly; crops average about $1\,\%$ over a season.

## 18.5. Retinal Proteins and Photoreceptors

### 18.5.1. Bacteriorhodopsin, a Light-Driven Proton Pump

The salt-loving archaeon *Halobacterium salinarum*, which colours salt evaporation ponds purple, harvests light with no chlorophyll, no electron transfer and no reaction center. Its plasma membrane contains patches of a single protein packed in a two-dimensional crystal (the purple membrane), in which each molecule pumps one proton out of the cell per absorbed photon.

**Definition 18.5.1 (Microbial Rhodopsins)** Microbial rhodopsins are seven-transmembrane-helix proteins of archaea, bacteria, algae and fungi that bind all-trans retinal as a protonated Schiff base to a lysine of helix G and are activated by its isomerization to 13-cis. **Bacteriorhodopsin** is a light-driven outward proton pump; **halorhodopsin** a light-driven inward chloride pump; **channelrhodopsins**, from green algae, are light-gated cation channels.

Absorption of a photon at $568\,\mathrm{nm}$ isomerizes the retinal in about $0.5\,\mathrm{ps}$, with a quantum yield of $0.64$. The strained 13-cis chromophore drives the protein through a cycle of intermediates that can be followed by their absorption spectra (K, L, M, N, O) and by time-resolved crystallography with X-ray free-electron lasers ([7.6.10](/7.6.10)). The key steps are changes of the proton affinity of a few groups: after isomerization the Schiff base becomes a weaker base and gives its proton to Asp85 on the extracellular side (L → M), a proton is released to the outside; then Asp96, on the cytoplasmic side, reprotonates the Schiff base through a chain of water molecules (M → N), takes a proton from the cytoplasm as the retinal returns to all-trans (N → O), and Asp85 passes its proton on to the release group (O → bR). The switch in accessibility of the Schiff base, from the extracellular to the cytoplasmic side while it is deprotonated in M, is what makes the pump directional, exactly as in a transporter with alternating access ([7.3.5](/7.3.5)).

![The photocycle of bacteriorhodopsin. Intermediates are named by letters with their absorption maxima in nanometres; arrows carry approximate time constants at room temperature and the proton transfers. Photon absorption isomerizes all-trans retinal to 13-cis (bR → K); the Schiff base (SB) donates its proton to Asp85 and a proton is released to the extracellular side (L → M); Asp96 reprotonates the Schiff base (M → N) and takes up a proton from the cytoplasm as the retinal reisomerizes (N → O); Asp85 returns its proton to the release group (O → bR). One cycle pumps one proton outward and takes about 10–15 ms](./plots/bacteriorhodopsin-cycle.py)

**Example 18.5.1 (Efficiency of the Pump)** A $568\,\mathrm{nm}$ photon carries $2.18\,\mathrm{eV}$. Pumping one proton against a **proton-motive force** of $250\,\mathrm{mV}$ ([7.6.3](/7.6.3#fml-3.4.1)) stores $0.25\,\mathrm{eV}$, and only $64\,\%$ of absorbed photons pump: the efficiency is $0.64\times0.25/2.18 \approx 7\,\%$, several times lower than that of the photosystems, whose electron transfer stores more than half of the photon. The pump is simple, robust and cheap to make, and the proton gradient drives an ordinary **ATP synthase**. Expressed in *Escherichia coli* whose respiration is blocked, a bacteriorhodopsin-like pump alone keeps the flagellar motor turning in green light, and stops it in red light.

Proteorhodopsins, discovered in marine bacteria in 2000 by environmental genome sequencing, are found in a large fraction of the bacteria in the sunlit ocean; by some estimates retinal-based phototrophy captures as much light energy in the sea as chlorophyll-based photosynthesis, although without fixing carbon.

### 18.5.2. Channelrhodopsins, Phototaxis and Optogenetics

Swimming microorganisms use light as information. In 1883 Theodor Engelmann projected a spectrum onto a drop of water with motile purple bacteria and saw them collect in the bands where their pigments absorb, a living spectrometer. The green alga *Chlamydomonas reinhardtii* steers towards moderate light with an eyespot, a patch of carotenoid-filled granules behind a membrane rich in channelrhodopsins. The cell swims along a helix while rotating, so the shaded eyespot sweeps across the light direction and receives a modulated signal whenever the cell is not aligned with the light; the photocurrent through channelrhodopsin depolarizes the membrane, $\ce{Ca^2+}$ entering through voltage-gated channels changes the beating of the two flagella, and the cell turns until the modulation vanishes. Channelrhodopsin is a nonselective cation channel, most permeable to protons; its reversal potential is therefore pH-dependent, about $-20\,\mathrm{mV}$ at pH 7.6 and much more negative at higher external pH, as the **Goldman–Hodgkin–Katz equation** predicts for a channel dominated by protons ([7.6.30](/7.6.30)).

Channelrhodopsin-2, expressed in neurons, makes them fire action potentials on a blue flash within milliseconds (Boyden, Zhang, Bamberg, Nagel and Deisseroth 2005); halorhodopsin silences them in yellow light. This is **optogenetics** ([7.3.2](/7.3.2)): genetically targeted, millisecond control of defined cell types, now a standard tool of neuroscience and, since 2021, the basis of a partial restoration of vision in a blind patient by expressing a red-shifted channelrhodopsin in retinal ganglion cells. The physics of the method is that of this chapter: the light intensity needed follows from the cross-section and quantum yield of the channel, $\sigma\Phi j$ openings per channel per second, and the spatial resolution from the scattering of light in tissue, which limits blue light to a fraction of a millimetre (red-shifted variants penetrate further).

### 18.5.3. Photoreceptors of Plants and Microbes

Plants cannot move away from bad light, but they measure its quality, direction and duration precisely, with several families of photoreceptors that cover the spectrum from UV-B to far red.

**Definition 18.5.2 (Plant Photoreceptors)** **Phytochromes** are red/far-red photoreceptors whose linear tetrapyrrole chromophore (phytochromobilin in plants, biliverdin in bacteria) isomerizes about its C15=C16 double bond, converting the red-absorbing Pr form ($\lambda_{\max} \approx 660\,\mathrm{nm}$) into the far-red-absorbing Pfr form ($\approx 730\,\mathrm{nm}$) and back. **Phototropins** are blue-light receptor kinases whose LOV domains form a covalent cysteinyl adduct with a flavin mononucleotide on excitation. **UVR8** is a UV-B receptor without an external chromophore: absorption by a cluster of tryptophans at its dimer interface breaks the salt bridges that hold the dimer together.

| Receptor | Chromophore | Light | Primary photochemistry | Functions |
|---|---|---|---|---|
| Rhodopsins (animal, microbial) | retinal | UV to red | cis–trans isomerization | vision, pumps, channels, phototaxis |
| Phytochromes | bilin | red / far red | Z–E isomerization at C15 | germination, shade avoidance, flowering |
| Cryptochromes | FAD | blue, UV-A | electron transfer through Trp chain | de-etiolation, circadian clock, magnetoreception? ([7.6.19](/7.6.19)) |
| Phototropins (LOV) | FMN | blue | cysteinyl–flavin adduct | phototropism, chloroplast movement, stomatal opening |
| BLUF proteins | FAD | blue | hydrogen-bond rearrangement | bacterial phototaxis, signalling |
| Photoactive yellow protein | p-coumaric acid | blue | trans–cis isomerization | bacterial negative phototaxis |
| UVR8 | tryptophans | UV-B | dimer dissociation | UV protection |

The phytochrome system is a photochemical ratio meter. Because Pr and Pfr absorb in overlapping bands and both convert, continuous light drives the pair to a photostationary state whose Pfr fraction depends on the ratio of red to far-red light. Under a leaf canopy, chlorophyll removes red light but transmits far red, the Pfr fraction drops, and a seedling responds by elongating its stem to escape the shade. Pfr also reverts slowly to Pr in the dark, so the system measures the length of the night as well; the physiology belongs to plant biology ([7.13](/7.13)).

## 18.6. Vision

### 18.6.1. The Photoisomerization of Rhodopsin

All animal eyes detect light with the same reaction: the **photoisomerization** of 11-cis-retinal bound in an opsin ([6.5.31](/6.5.31#sec-31.3.1)), which in rod **rhodopsin** ([7.1.14](/7.1.14#def-14.4.1)) produces the all-trans form in about $200\,\mathrm{fs}$, one of the fastest chemical reactions known. The excited molecule does not linger in a thermalized excited state; a vibrational wave packet moves along the torsion of the C11=C12 bond and passes through a conical intersection of the excited and ground state surfaces within one vibrational period. The quantum yield, $0.65$–$0.67$, is independent of wavelength across the absorption band and almost independent of temperature. The primary product, bathorhodopsin, stores about $1.4\,\mathrm{eV}$ of the $2.5\,\mathrm{eV}$ photon as strain of the twisted chromophore in its tight pocket. It relaxes through lumirhodopsin and metarhodopsin I to metarhodopsin II (R*) within milliseconds, the state that activates the G protein **transducin**.

The reaction is a molecular switch in the strict sense: the ground state is thermally almost perfectly stable, and one photon flips it with probability two thirds. The cost of this design is that vertebrate rhodopsin bleaches: all-trans retinal is hydrolysed from the opsin and must be regenerated by the visual cycle in the retinal pigment epithelium, which takes minutes and underlies the slow phase of dark adaptation. Invertebrate rhodopsins, like the microbial ones, return to the ground state by absorbing a second photon (they are bistable).

### 18.6.2. A Rod Counts Single Photons

A rod outer segment, $1$–$2\,\mu\mathrm{m}$ in diameter and $20$–$60\,\mu\mathrm{m}$ long, contains about $1000$ disc membranes $25\,\mathrm{nm}$ apart, packed with rhodopsin at about $25\,000$ molecules per $\mu\mathrm{m}^2$: about $10^8$ rhodopsins in a human rod, $2$–$3\times10^9$ in the large rods of toads. (The figure of $10^7$ sometimes quoted is too small by a factor of ten.) A photon travelling along the rod therefore has many chances to be absorbed, without any antenna.

Each photoisomerization produces a current pulse of about $1\,\mathrm{pA}$, a few percent of the dark current of $20$–$30\,\mathrm{pA}$, lasting about $0.2$–$0.5\,\mathrm{s}$ (Baylor, Lamb and Yau 1979, recorded by sucking the outer segment of a single rod into a pipette). Since a single R* can only change one protein, the signal must be amplified, and the cascade does so in two stages ([7.1.14](/7.1.14#sec-14.4.1)): R* activates tens to hundreds of transducins during its lifetime of about $0.1\,\mathrm{s}$, and each transducin-activated phosphodiesterase hydrolyses hundreds of cGMP molecules. The fall in cGMP closes a few hundred of the cooperatively gated channels near the activated disc, blocking the entry of about $10^6$ cations. The energy for this gain comes from the GTP and the ion gradients maintained by the cell, not from the photon: the photon only opens a valve.

A remarkable feature of the single-photon response is its reproducibility. A single active molecule decaying by a first-order process would have an exponentially distributed lifetime, and the integrated response would vary with a coefficient of variation of one; measured responses vary with a coefficient of variation of about $0.2$–$0.3$. The shutoff of R* proceeds by a series of phosphorylations by rhodopsin kinase followed by arrestin binding, and a sequence of $m$ steps of equal rate has a lifetime with coefficient of variation $1/\sqrt m$; with feedback from $\ce{Ca^2+}$ on several steps, the rod turns a random event into a nearly standard pulse.

### 18.6.3. The Hecht–Shlaer–Pirenne Experiment

How many photons does a person need to see a flash? Selig Hecht, Simon Shlaer and Maurice Pirenne answered in 1942 with an experiment that counted photons with probability theory, decades before single-rod recordings. Dark-adapted observers looked at a fixation point so that a test flash of $510\,\mathrm{nm}$ light, $1\,\mathrm{ms}$ long and $10$ arc minutes across, fell on the rod-rich retina $20^\circ$ from the fovea, and reported whether they saw it; the flash intensity was varied and each was presented many times.

**Definition 18.6.1 (Frequency-of-Seeing Curve)** The **frequency-of-seeing curve** of an observer is the probability of reporting a flash as a function of its mean number of photons $\bar n$ at the cornea.

The key observation is that the number of photons in a flash of fixed mean is not fixed: it follows the **Poisson distribution** ([3.1.4](/3.1.4#def-4.1.10)), and so does the number absorbed, with mean $\alpha\bar n$, where $\alpha$ is the fraction of photons at the cornea that are absorbed by rhodopsin.

**Theorem 18.6.1 (Poisson Threshold Model)** If a flash is seen whenever at least $K$ photons are absorbed, the frequency-of-seeing curve is

$$
P_{\mathrm{see}}(\bar n) = 1 - \sum_{k=0}^{K-1}\mathrm{e}^{-\alpha\bar n}\frac{(\alpha\bar n)^k}{k!}. \tag{18.11}
$$
On a logarithmic intensity axis, $\alpha$ only shifts the curve; its shape, in particular its steepness, depends on $K$ alone.

**Proof** The number of absorbed photons is Poisson with mean $m = \alpha\bar n$ (thinning a Poisson process with probability $\alpha$ gives a Poisson process), and the probability of at least $K$ is one minus the probability of $0, \dots, K - 1$. Writing $m = \alpha\bar n$, $\log m = \log\alpha + \log\bar n$, so a change of $\alpha$ translates the curve along the $\log\bar n$ axis without changing its shape. $\square$

The theorem separates what was unknown. The losses in the eye (reflection at the cornea, absorption in the lens and vitreous, photons passing between rods) were known only roughly, but they do not affect the shape of the curve. Fitting the shape gave thresholds of $K = 5$–$7$ absorbed photons for the three authors; independently, the measured energy at threshold, $54$–$148$ photons at the cornea, combined with an estimate that only about $10\,\%$ of them are absorbed by rhodopsin, gave $5$–$14$, in agreement.

The second conclusion concerns single rods. The flash covered about $500$ rods; with five to seven photons absorbed among them, the chance that any rod received two is small. Each rod therefore responded to one photon, and the retina added several such events. Rods are single-photon detectors; perception requires a coincidence of several of them.

![The Hecht–Shlaer–Pirenne analysis. A: frequency-of-seeing curves (Theorem 18.6.1) for thresholds K = 1–10 against the logarithm of the mean number of photons absorbed; the curves steepen with K. B: a simulated observer (α = 0.06, K = 6; seven flash intensities, 50 flashes each) and maximum-likelihood fits of α for K = 2, 6 and 10: the true K gives the best likelihood. C: dark noise; with a mean of 0.6 spontaneous events in the summation pool per integration time, the probability of a hit for a flash of 6 absorbed photons and of a false alarm in darkness against the criterion K; a criterion of 5–7 events (shaded) keeps false alarms below one in a thousand while detecting most flashes](./plots/frequency-of-seeing.py)

### 18.6.4. Dark Noise and the Limits of Sensitivity

Why does the brain demand several photons, if one rod can detect one? Because of noise. In complete darkness rods produce occasional current pulses identical in shape and size to single-photon responses. Baylor, Matthews and Yau (1980) showed in toad rods that their rate rises steeply with temperature, following the **Arrhenius equation** with an apparent activation energy of about $100\,\mathrm{kJ\,mol^{-1}}$: they are thermal isomerizations of single rhodopsins. A toad rod has about one such event per $30$–$50\,\mathrm{s}$; with $2\times10^9$ rhodopsins, each molecule isomerizes spontaneously about once in two thousand years. Primate rods, with $10^8$ rhodopsins at $37\,^\circ\mathrm{C}$, produce about one event per few minutes.

Even this is a lot for a retina of $10^8$ rods: in total darkness about a million false "photons" arrive per second, the "dark light" seen as the grey of a dark room. A flash detected by a pool of $N$ rods in an integration time $t$ competes with $d = N r t$ dark events, Poisson distributed. With $N = 500$, $r = 0.006\,\mathrm{s^{-1}}$ and $t = 0.2\,\mathrm{s}$, $d = 0.6$: a criterion of one event would give false alarms on almost half of the blank trials, and a criterion of $5$–$7$ reduces them below one in a thousand at the cost of missing some real flashes (panel C). Barlow argued in 1956 that the threshold of human vision is set in exactly this way, by the need to distinguish a signal from the thermal noise of rhodopsin. Later analysis of retinal circuits showed that the rod bipolar cells apply a nonlinear threshold that rejects most single-rod noise, at the cost of discarding some genuine single-photon events. Whether a human can detect a single absorbed photon at all remains disputed: an experiment with a heralded single-photon source (Tinsley et al. 2016) found responses only slightly above chance.

Thermal noise also links sensitivity to colour. An isomerization can be driven by heat only if the molecule acquires, from many vibrational modes at once, an energy comparable to that of the photon; pigments that absorb at longer wavelengths need less energy and are noisier. Measurements on pigments from many species confirm that the rate of thermal activation rises steeply with $\lambda_{\max}$ (Barlow 1957; Luo et al. 2011): this is one reason why no visual pigment absorbs much beyond $620\,\mathrm{nm}$, and why the long-wavelength cones are the noisiest.

### 18.6.5. Colour Vision

Cones use opsins with different absorption spectra: in humans the S, M and L cones peak near $420$, $530$ and $560\,\mathrm{nm}$, and rods at $498\,\mathrm{nm}$. Remarkably, all vertebrate visual pigment spectra have nearly the same shape when plotted against $\lambda_{\max}/\lambda$, which allows them to be described by a single template (Govardovskii et al. 2000).

**Definition 18.6.2 (Principle of Univariance)** The output of a photoreceptor depends only on the number of photons it absorbs, not on their wavelength. According to the **principle of univariance**, a single receptor type cannot distinguish a change of wavelength from a change of intensity; wavelength can be recovered only by comparing receptors with different spectra.

A photon of $600\,\mathrm{nm}$ that is absorbed by an M cone produces exactly the same response as one of $530\,\mathrm{nm}$; the M cone absorbs $600\,\mathrm{nm}$ light only $0.22$ times as well, so a light $4.5$ times brighter at $600\,\mathrm{nm}$ is indistinguishable for it. Ratios of cone signals, by contrast, are independent of intensity and vary monotonically with wavelength over wide ranges: the visual system computes opponent signals, L − M (red–green) and S − (L + M) (blue–yellow). With three cone types, any light is matched by a mixture of three primaries, the basis of colour reproduction; most mammals have only two cone types, many birds, reptiles and fishes four, including one sensitive to ultraviolet. Mantis shrimps have twelve, but behavioural tests show that they discriminate wavelengths poorly (Thoen et al. 2014): they seem to recognize colours by the pattern of receptor activation rather than to compare them as we do, so more receptor types do not mean finer colour vision.

The M and L opsins differ in only 15 of 364 amino acids, and three of them, which add or remove hydroxyl groups near the retinal, account for most of the $30\,\mathrm{nm}$ shift: colour tuning is a matter of a few polar groups around the chromophore (18.2.2). Their genes, adjacent on the X chromosome, recombine unequally, the cause of common red–green colour blindness ([7.1.14](/7.1.14#sec-14.4.1)).

![Human photopigments. A: absorbance spectra of the S, M and L cone pigments and of rod rhodopsin from the Govardovskii template (peaks at 420, 530, 560 and 498 nm; without the filtering by lens and macular pigment), normalized to their peaks. B: univariance and opponency; the ratios L/(L + M) and S/(L + M) of cone signals change monotonically with wavelength over wide ranges and are independent of intensity (logarithmic axis); dotted lines mark 530 and 600 nm, where the M cone absorbs 0.22 times as well as at its peak](./plots/cone-spectra.py)

### 18.6.6. The Optics of Eyes

An eye must not only count photons but also tell where they come from. The camera eye of vertebrates and cephalopods forms an image with a lens; its resolution is limited by diffraction at the pupil, and by the **Rayleigh criterion** ([5.4.2](/5.4.2#def-2.4.2)) two points are resolved if their angular separation exceeds $1.22\lambda/D$. For the human eye with $D = 2.5\,\mathrm{mm}$ and $\lambda = 530\,\mathrm{nm}$ this is $2.6\times10^{-4}\,\mathrm{rad}$, about one arc minute, the measured acuity. On the retina, $17\,\mathrm{mm}$ behind the optical centre of the eye, one arc minute is $5\,\mu\mathrm{m}$; foveal cones are $2.5\,\mu\mathrm{m}$ apart, two per resolvable distance, just what the sampling theorem requires: the retina is neither undersampled (which would produce aliasing) nor wastefully oversampled.

Insects use compound eyes, in which each ommatidium has its own small lens and looks in its own direction. Smaller facets sample the visual field more finely but blur more by diffraction, and there is an optimum.

**Formula 18.6.1 (Optimal Facet Size)** A compound eye of radius $r$ with facets of diameter $\delta$ samples the visual field at intervals $\theta_{\mathrm{s}} = \delta/r$ and blurs by diffraction over $\theta_{\mathrm{d}} \approx \lambda/\delta$. Their sum is smallest for

$$
\delta_{\mathrm{opt}} = \sqrt{\lambda r}, \qquad \theta_{\min} = 2\sqrt{\lambda/r}. \tag{18.12}
$$

The argument goes back to Mallock (1894) and was popularized by Feynman; Barlow (1952) found that the facet diameter of bees and wasps indeed grows as the square root of the eye size. For $r = 1\,\mathrm{mm}$ and $\lambda = 0.5\,\mu\mathrm{m}$, $\delta_{\mathrm{opt}} = 22\,\mu\mathrm{m}$, close to the $20$–$25\,\mu\mathrm{m}$ facets of the honeybee, and $\theta_{\min} \approx 2.6^\circ$; bee acuity is about $1^\circ$–$2^\circ$. The square-root law is harsh: to reach the one arc minute of the human eye, a compound eye would need a radius of tens of metres. Lenses are a better solution for large animals; compound eyes win for small ones because they are compact, see a wide field and respond quickly (fast flies resolve flicker above $200\,\mathrm{Hz}$).

![Resolution of compound and camera eyes. A: for a compound eye of radius 1 mm, the sampling angle δ/r and the diffraction angle λ/δ against the facet diameter, and their sum, which is smallest at δ_opt = √(λr) = 22 μm (λ = 0.5 μm). B: the best angular resolution against eye size for compound eyes (2√(λ/r)) and camera eyes (Rayleigh limit 1.22λ/D); the human pupil reaches about one arc minute, which a compound eye would reach only with a radius of about 24 m](./plots/compound-eye.py)

## Summary

| Topic | Key results |
|---|---|
| Photons (18.1) | $E = 1239.8\,\mathrm{eV\,nm}/\lambda$, $93\,k_{\mathrm{B}}T$ at $500\,\mathrm{nm}$ (Formula 18.1.1); $1000\,\mathrm{W\,m^{-2}}$ ≈ $2500$ photons $\mathrm{nm^{-2}\,s^{-1}}$; a chlorophyll is excited only $10$–$25$ times per second (Example 18.1.1); competing decay routes branch as $k_j/\sum k_i$ (Formula 18.1.2) |
| Pigments (18.2) | free-electron box: $\Delta E = h^2(N + 1)/(8m_{\mathrm{e}}L^2)$, gap $\propto 1/L$ (Formula 18.2.1); bond alternation makes the gap saturate (Hückel); proteins tune chromophores (opsin shift); $\sigma = \ln10\,\varepsilon/N_{\mathrm{A}}$ (Formula 18.2.2) |
| Antennas (18.3) | hundreds of pigments per reaction center (Example 18.3.1); weak coupling: Förster hopping; strong coupling: excitons; trapping time ≈ $(N/\pi)\ln N$ steps + $N/k_{\mathrm{cs}}$ (Formula 18.3.1); a shallow funnel trades a few $k_{\mathrm{B}}T$ for speed and yield |
| Electron transfer (18.4) | tunneling length $0.2\,\mathrm{nm}/\sqrt{V_0/\mathrm{eV}}$ (Formula 18.4.1); Marcus rate with $\Delta G^\ddagger = (\Delta G^\circ + \lambda)^2/4\lambda$ (Theorem 18.4.1, Definition 18.4.1); inverted region (Definition 18.4.2); Moser–Dutton: 6 decades per nm (Formula 18.4.2); forward steps activationless, recombinations inverted (Example 18.4.2); at most about $1.3$ of $1.8\,\mathrm{eV}$ storable (Formula 18.4.3) |
| Retinal proteins and photoreceptors (18.5) | bacteriorhodopsin pumps one proton per photon with efficiency ≈ $7\,\%$ (Definition 18.5.1, Example 18.5.1); channelrhodopsins for phototaxis and optogenetics; phytochrome, phototropin, cryptochrome, UVR8 (Definition 18.5.2) |
| Vision (18.6) | 11-cis → all-trans in $200\,\mathrm{fs}$, quantum yield $0.67$; $10^8$ rhodopsins and a gain of $10^6$ per rod; threshold of $5$–$7$ absorbed photons from the Poisson shape of the frequency-of-seeing curve (Definition 18.6.1, Theorem 18.6.1); criterion set by thermal dark events; univariance and colour from cone comparisons (Definition 18.6.2); Rayleigh limit of one arc minute; compound eyes $\delta_{\mathrm{opt}} = \sqrt{\lambda r}$ (Formula 18.6.1) |

## Questions

1. Estimate how many photons per second strike a chlorophyll molecule (cross-sectional area $1\,\mathrm{nm^2}$) in full sunlight, taking all light at $500\,\mathrm{nm}$ and $1000\,\mathrm{W\,m^{-2}}$. If one photon in a hundred is absorbed, how often is the molecule excited, and how does the antenna help?

   **Answer** One photon carries $hc/\lambda = 3.97\times10^{-19}\,\mathrm{J}$, so the flux is $1000/3.97\times10^{-19} = 2.5\times10^{21}\,\mathrm{m^{-2}\,s^{-1}} = 2500\,\mathrm{nm^{-2}\,s^{-1}}$. With an absorption probability of $1/100$ the molecule is excited about $25$ times per second, once every $40\,\mathrm{ms}$. A reaction center can process an excitation every few milliseconds, so it would be idle more than $90\,\%$ of the time; an antenna of $N$ pigments, each passing its excitation on with high yield, multiplies the excitation rate of the reaction center by about $N$ (Example 18.3.1).

2. Using the free-electron model with $a = 0.14\,\mathrm{nm}$ and $L = (N - 1)a$, compute the absorption wavelength of a chain of $N = 10$ atoms. Why does the model predict ever longer wavelengths as $N$ grows, and what limits the real absorption?

   **Answer** $L = 1.26\,\mathrm{nm}$, $h^2/(8m_{\mathrm{e}}L^2) = 0.237\,\mathrm{eV}$, $\Delta E = 11\times0.237 = 2.60\,\mathrm{eV}$, $\lambda = 1240/2.60 \approx 476\,\mathrm{nm}$. In the box the gap falls as $(N + 1)/L^2 \propto 1/N$, without limit. In a real polyene single and double bonds alternate; the alternating coupling opens a gap of $2\lvert\beta_{\mathrm{d}} - \beta_{\mathrm{s}}\rvert$ that remains as $N \to \infty$, so the absorption saturates (near $600$–$700\,\mathrm{nm}$ for polyacetylene), as the Hückel model of 18.2.2 shows. The real decapentaene ($N = 10$) absorbs near $330\,\mathrm{nm}$: the free-electron model overestimates the wavelength.

3. Two chlorophylls are $2\,\mathrm{nm}$ apart with a Förster radius of $6\,\mathrm{nm}$ and a donor lifetime of $5\,\mathrm{ns}$. Compute the Förster transfer time. Why is this estimate unreliable for the nearest neighbours in LH2 ($R \approx 0.9\,\mathrm{nm}$)?

   **Answer** $k = \tau_{\mathrm{D}}^{-1}(R_0/R)^6 = (5\,\mathrm{ns})^{-1}\times3^6 = 729/5\,\mathrm{ns^{-1}} = 146\,\mathrm{ns^{-1}}$, a time of $6.9\,\mathrm{ps}$. At $0.9\,\mathrm{nm}$ the pigments are about as large as their separation, so the point-dipole approximation fails, exchange (Dexter) coupling adds, and the coupling ($\approx 300\,\mathrm{cm^{-1}}$) exceeds the disorder and reorganization energies: the excitation is delocalized as an exciton, and the incoherent-hopping picture underlying the Förster rate no longer applies (18.3.2).

4. Derive the activation free energy of Marcus theory from the two parabolas $G_{\mathrm{D}} = \lambda q^2$ and $G_{\mathrm{A}} = \lambda(q - 1)^2 + \Delta G^\circ$. For $\lambda = 0.6\,\mathrm{eV}$, compare the rates of reactions with $\Delta G^\circ = -0.3$, $-0.6$ and $-1.5\,\mathrm{eV}$ at $298\,\mathrm{K}$ for equal coupling.

   **Answer** The parabolas cross at $q^* = (1 + \Delta G^\circ/\lambda)/2$, where $G_{\mathrm{D}} = (\lambda + \Delta G^\circ)^2/(4\lambda)$. The barriers are $0.0375\,\mathrm{eV}$ ($1.46\,k_{\mathrm{B}}T$), $0$ and $0.3375\,\mathrm{eV}$ ($13.1\,k_{\mathrm{B}}T$). The rates relative to the activationless one are $\mathrm{e}^{-1.46} = 0.23$, $1$ and $\mathrm{e}^{-13.1} = 2\times10^{-6}$: the most exergonic reaction is the slowest (the inverted region), by a factor of about $10^5$ relative to the first.

5. By the Moser–Dutton ruler, how much does the activationless rate change when the edge-to-edge distance between two cofactors grows from $1.0$ to $1.5\,\mathrm{nm}$? What does this imply for the spacing of cofactors in a chain that must deliver electrons within a millisecond?

   **Answer** Six decades per nanometre: $0.5\,\mathrm{nm}$ costs $3$ decades, a factor of $1000$. At $1.0\,\mathrm{nm}$ the maximal rate is $10^{13 - 6\times0.64} = 1.4\times10^9\,\mathrm{s^{-1}}$; at $1.5\,\mathrm{nm}$, $1.4\times10^6\,\mathrm{s^{-1}}$. A rate of $10^3\,\mathrm{s^{-1}}$ is reached at $R = 0.36 + 10/6 = 2.0\,\mathrm{nm}$ for an activationless step, but real steps are not all activationless and some are uphill, so chains of redox centres keep their spacing below about $1.4\,\mathrm{nm}$, as respiratory and photosynthetic chains do.

6. A rod contains about $10^8$ rhodopsins and produces one thermal event every $200\,\mathrm{s}$. What is the mean time between spontaneous isomerizations of one rhodopsin molecule? If thermal isomerization followed the Arrhenius law with a prefactor of $10^{13}\,\mathrm{s^{-1}}$, what activation energy would this imply, and why is the measured activation energy (about $100\,\mathrm{kJ\,mol^{-1}}$) much smaller?

   **Answer** The rate per molecule is $1/(200\times10^8) = 5\times10^{-11}\,\mathrm{s^{-1}}$, a mean time of $2\times10^{10}\,\mathrm{s}$, about $630$ years. With $k = 10^{13}\mathrm{e}^{-E/RT}$, $E = RT\ln(10^{13}/5\times10^{-11}) = RT\times54.9 = 141\,\mathrm{kJ\,mol^{-1}}$ at $310\,\mathrm{K}$ ($55\,k_{\mathrm{B}}T$). The measured temperature dependence gives a smaller apparent activation energy with a correspondingly smaller prefactor: the energy needed to isomerize is collected from many vibrational modes of the chromophore and protein, and the statistics of such multi-mode activation (Hinshelwood) makes the effective barrier and prefactor differ from those of a single-coordinate Arrhenius model. The low rate reflects the large total energy needed, comparable to the photon energy, which is why long-wavelength pigments are noisier.

7. In the Hecht–Shlaer–Pirenne model with $K = 6$, what fraction of flashes is seen when the mean number of absorbed photons is $3$, $6$ and $12$? Why could the authors determine $K$ without knowing the fraction $\alpha$ of photons absorbed?

   **Answer** $P(\ge 6 \mid 3) = 0.084$, $P(\ge 6 \mid 6) = 0.554$, $P(\ge 6 \mid 12) = 0.980$ (cumulative Poisson). Because the absorbed number is Poisson with mean $\alpha\bar n$, changing $\alpha$ only shifts the curve along the $\log\bar n$ axis (Theorem 18.6.1); its steepness depends on $K$ only, so fitting the shape of the measured curve determines $K$, and the position then gives $\alpha$.

8. (Experiment design) You want to know whether a newly discovered photoreceptor protein in a bacterium acts as a single-photon switch, like rhodopsin, or requires several photons. Design an experiment based on the logic of Hecht, Shlaer and Pirenne, and state what would distinguish the two cases.

   **Answer** Deliver brief flashes of calibrated mean photon number to single cells (or to the purified protein in a single-molecule assay), so short that the protein cannot relax between photons, and record the fraction of cells (or molecules) responding against flash intensity. If one photon suffices, the response probability is $1 - \mathrm{e}^{-\alpha\bar n}$, linear in $\bar n$ at low intensity (slope one on a log–log plot of the response probability at low intensity); if $K$ photons are needed, it rises as $\bar n^{K}$ at low intensity and the curve is steeper (Theorem 18.6.1). Controls: verify that the response depends on the number of photons (reciprocity between flash duration and intensity within the integration time), and measure the dark response rate to correct for spontaneous activation.

9. Bacteriorhodopsin absorbs at $568\,\mathrm{nm}$ with a quantum yield of $0.64$ and pumps one proton per cycle against a proton-motive force of $250\,\mathrm{mV}$. Compute its energy efficiency and compare it with the photosystems, which store about $1.2\,\mathrm{eV}$ per $1.8\,\mathrm{eV}$ photon at the reaction center.

   **Answer** Photon energy $1239.8/568 = 2.18\,\mathrm{eV}$; stored per absorbed photon $0.64\times0.25 = 0.16\,\mathrm{eV}$; efficiency $7\,\%$. The photosystems store about $1.2/1.8 = 67\,\%$ in the primary charge separation (with a quantum yield near one), close to the thermodynamic limit of Formula 18.4.3, ten times more. Bacteriorhodopsin trades efficiency for simplicity: one small protein, no cofactors besides retinal, no reaction center or electron carriers.

10. A bee eye has a radius of about $1.5\,\mathrm{mm}$. Estimate the optimal facet diameter for $\lambda = 0.5\,\mu\mathrm{m}$ and the resulting angular resolution. What eye radius would give a resolution of $1^\circ$?

    **Answer** $\delta_{\mathrm{opt}} = \sqrt{0.5\times10^{-6}\times1.5\times10^{-3}}\,\mathrm{m} = 27\,\mu\mathrm{m}$; $\theta_{\min} = 2\sqrt{\lambda/r} = 2\sqrt{3.3\times10^{-4}} = 0.037\,\mathrm{rad} = 2.1^\circ$. For $\theta = 1^\circ = 0.0175\,\mathrm{rad}$, $r = 4\lambda/\theta^2 = 4\times0.5\times10^{-6}/3.05\times10^{-4}\,\mathrm{m} = 6.6\,\mathrm{mm}$, four times larger in radius, sixty times larger in volume; a hard requirement for an insect, which is why insects compromise with acute zones of larger facets in part of the eye.

11. (Open question) The reaction center separates charges in $3\,\mathrm{ps}$ and stabilizes them in $200\,\mathrm{ps}$, but the electron then waits $100\,\mu\mathrm{s}$ to reach $\mathrm{Q_B}$. Why is it advantageous that the early steps are so much faster than the later ones, and what limits how much free energy can be saved by making every step only slightly downhill?

    **Answer** Each step competes with the recombination of the pair it creates (Formula 18.1.2). The first pairs are close together and could recombine fast, so the forward steps must be faster still; once the electron is $2$–$3\,\mathrm{nm}$ from the hole, recombination is slow (the Moser–Dutton ruler and the inverted region), and the later steps can be slow without loss. Making steps less downhill saves free energy but has two costs: in the Marcus picture a step with $-\Delta G^\circ < \lambda$ acquires an activation barrier and slows down, and a small $\Delta G^\circ$ means the back reaction is significant, so the charges are not trapped irreversibly (by detailed balance the equilibrium constant of a step is $\mathrm{e}^{-\Delta G^\circ/k_{\mathrm{B}}T}$, and at least a few $k_{\mathrm{B}}T$ per step are needed to make it effectively one-way). The reaction center spends about $0.5\,\mathrm{eV}$ of the photon on these irreversibility margins.
