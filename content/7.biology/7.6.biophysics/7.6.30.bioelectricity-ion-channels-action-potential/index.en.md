---
title: "Bioelectricity: Ion Channels and the Action Potential"
description: "The physics of electrical signaling in cells: the charge state of the cell and the membrane as a capacitor, the Nernst equation and Donnan equilibrium, the energetics of the Na⁺/K⁺ pump, the Nernst–Planck equation and the constant-field derivation of the Goldman–Hodgkin–Katz equations, patch clamp and single-channel currents, barrier models of permeation, the K⁺ selectivity filter, voltage sensors, gating charge and gating currents, single-channel kinetics, the NMDA receptor, the membrane as a bistable circuit, the cable equation, the Hodgkin–Huxley model and its simulation, conduction velocity, myelin and saltatory conduction, electric organs and the electrocardiogram."
---

Nerve, muscle and many other cells signal with electricity, but their currents are carried by ions in water, not by electrons in metal, and their batteries are concentration differences maintained by pumps. Within a millisecond a patch of membrane can switch its potential by a tenth of a volt, and the switch can travel along an axon at a hundred meters per second. This chapter builds the physics of this machinery from the bottom up: how much charge a cell holds and why it is so little (30.1); how ions cross membranes, through the Nernst–Planck equation, the Goldman–Hodgkin–Katz equations, rate-theory models of pores and the structure of the K⁺ selectivity filter (30.2); how channels sense voltage, through gating charge, gating currents and their single-channel kinetics (30.3); how a membrane with voltage-gated channels becomes a bistable switch (30.4) and how a cable of such membrane conducts signals passively and actively (30.5); the Hodgkin–Huxley model, its derivation from voltage-clamp data and its simulation (30.6); myelin and saltatory conduction (30.7); and two organ-level applications, electric organs and the electrocardiogram (30.8–30.9).

Much of the background is in place. The electrochemistry of membrane potentials, the **Nernst equation** and the **Donnan equilibrium** are in [6.3.13](/6.3.13) and [6.3.21](/6.3.21); the patch clamp as an analytical technique in [6.4.6](/6.4.6); the cell biology of pumps, the pump–leak model, the resting potential and the **Goldman–Hodgkin–Katz equation** in [7.3.5](/7.3.5#sec-5.6); the families of channels and transporters and their structures in [7.1.13](/7.1.13) and [7.1.14](/7.1.14#sec-14.5); and the statistical mechanics of two-state gating by tension and voltage, the **gating charge** and the MWC model of the nicotinic receptor in [7.6.4](/7.6.4). Here these pieces are derived and assembled into a quantitative theory of excitability. Capacitors and currents are those of [5.3.4](/5.3.4) and [5.3.5](/5.3.5); the cable equation is a reaction–diffusion equation of the type studied in [2.5](/2.5). Mechanosensitive channels are treated in [7.6.25](/7.6.25). The simplified neuron models (FitzHugh–Nagumo, integrate-and-fire), synaptic dynamics and networks belong to [7.16](/7.16), and the electrophysiology of the heart to [7.14](/7.14); this chapter provides their physical basis.

## 30.1. The Charge State of the Cell

### 30.1.1. Ions, Membranes and Capacitance

Cells manipulate gradients of four small ions: $\ce{K+}$, $\ce{Na+}$, $\ce{Ca^2+}$ and $\ce{Cl-}$. Most of the negative charge that balances intracellular $\ce{K+}$ is carried by impermeant macromolecules (nucleic acids, proteins, metabolites such as phosphates), which cannot leave. Typical values for a mammalian skeletal-muscle fiber, with resting potential $-90\,\mathrm{mV}$, are (Hille):

| Ion | Inside / mM | Outside / mM | Nernst potential at $37\,{}^\circ\mathrm{C}$ / mV |
|---|---|---|---|
| $\ce{K+}$ | 155 | 4 | $-98$ |
| $\ce{Na+}$ | 12 | 145 | $+67$ |
| $\ce{Ca^2+}$ | $10^{-4}$ | 1.5 | $+129$ |
| $\ce{Cl-}$ | 4 | 120 | $-91$ |

The plasma membrane separates these solutions with a lipid bilayer whose hydrocarbon core, about $4\,\mathrm{nm}$ thick with relative permittivity $\varepsilon_{\mathrm{r}} \approx 2$–$3$, is an excellent insulator, studded with pumps that separate charge and channels that let it flow back. Electrically, a patch of membrane is a **capacitance** $C$ in parallel with conductances, each in series with a battery whose voltage is set by a concentration ratio.

The parallel-plate estimate $C/A = \varepsilon_0\varepsilon_{\mathrm{r}}/d = (8.85\times10^{-12})(2.1)/(4\times10^{-9}) \approx 5\times10^{-3}\,\mathrm{F\,m^{-2}}$, that is $0.5\,\mu\mathrm{F\,cm^{-2}}$, is within a factor of two of the value measured for almost all biological membranes, about $0.9$–$1\,\mu\mathrm{F\,cm^{-2}}$ (the polar head groups and bound water add to the effective permittivity). We use $c_{\mathrm{m}} = 1\,\mu\mathrm{F\,cm^{-2}} = 10^{-2}\,\mathrm{F\,m^{-2}}$.

**Example 30.1.1 (How much charge makes a membrane potential?)** A membrane potential of $70\,\mathrm{mV}$ across a capacitance of $10^{-2}\,\mathrm{F\,m^{-2}}$ requires a surface charge density $\sigma = c_{\mathrm{m}}V = 7\times10^{-4}\,\mathrm{C\,m^{-2}}$, or $4.4\times10^{15}$ elementary charges per square meter: about 4400 ions per square micrometer, one ion per $(15\,\mathrm{nm})^2$. A spherical cell of radius $5\,\mu\mathrm{m}$ has an area of $3.1\times10^{-10}\,\mathrm{m^2}$ and needs $1.4\times10^6$ uncompensated ions. It contains $0.155\,\mathrm{M} \times 5.2\times10^{-13}\,\mathrm{L} \times N_{\mathrm{A}} \approx 4.9\times10^{10}$ potassium ions, so the charge separation involves only $3\times10^{-5}$ of them. Two consequences follow. The bulk solutions on both sides stay electroneutral to high accuracy, the excess charge sitting within a **Debye length** (below $1\,\mathrm{nm}$) of the membrane; and a membrane potential can be set up or reversed without measurable changes of concentration. The field in the membrane, however, is enormous: $70\,\mathrm{mV}/4\,\mathrm{nm} \approx 2\times10^7\,\mathrm{V\,m^{-1}}$, six times the dielectric strength of air ($3\times10^6\,\mathrm{V\,m^{-1}}$, that is $3\,\mathrm{kV}$ per millimeter). Bilayers break down only at transmembrane voltages of about $0.5$–$1\,\mathrm{V}$, fields above $10^8\,\mathrm{V\,m^{-1}}$, which is exploited in electroporation.

### 30.1.2. Electrochemical Equilibrium

Consider a membrane permeable to a single ion species of valence $z$. In equilibrium the probability of finding an ion where the electric potential is $\varphi$ is proportional to the **Boltzmann distribution**, $\exp(-ze\varphi/k_{\mathrm{B}}T)$, so the concentrations on the two sides satisfy $c_{\mathrm{in}}/c_{\mathrm{out}} = \exp[-ze(\varphi_{\mathrm{in}} - \varphi_{\mathrm{out}})/k_{\mathrm{B}}T]$, which is the Nernst equation,
$$
E_{\mathrm{ion}} = \varphi_{\mathrm{in}} - \varphi_{\mathrm{out}} = \frac{k_{\mathrm{B}}T}{ze}\ln\frac{c_{\mathrm{out}}}{c_{\mathrm{in}}}. \tag{30.1}
$$
Equivalently, the **electrochemical potential** $\tilde\mu = \mu^\circ + k_{\mathrm{B}}T\ln c + ze\varphi$ is the same on both sides. The scale $k_{\mathrm{B}}T/e$ is $25.7\,\mathrm{mV}$ at $25\,{}^\circ\mathrm{C}$ and $26.7\,\mathrm{mV}$ at $37\,{}^\circ\mathrm{C}$: membrane potentials are a few times the thermal voltage, so thermal fluctuations, entropy and electrical energy compete on equal terms. A tenfold concentration ratio corresponds to $61.5\,\mathrm{mV}$ for a monovalent ion at $37\,{}^\circ\mathrm{C}$.

If all permeant ions were in equilibrium with the same membrane potential while impermeant charged macromolecules were confined inside, the cell would be in Donnan equilibrium ([6.3.21](/6.3.21)): the diffusible ions distribute so that $[\ce{K+}]_{\mathrm{in}}/[\ce{K+}]_{\mathrm{out}} = [\ce{Cl-}]_{\mathrm{out}}/[\ce{Cl-}]_{\mathrm{in}}$, and the excess of diffusible ions inside makes the interior hyperosmotic. An animal cell in Donnan equilibrium would swell and burst. The table shows that cells are not in equilibrium: $\ce{K+}$ and $\ce{Cl-}$ are close to it in muscle, but the Nernst potentials of $\ce{Na+}$ and $\ce{Ca^2+}$ do not even have the sign of the membrane potential. The cell is a steady state maintained by pumping, the **pump–leak model** of [7.3.5](/7.3.5).

### 30.1.3. The Energetics of the Na⁺/K⁺ Pump

The **Na⁺/K⁺-ATPase** moves three $\ce{Na+}$ out and two $\ce{K+}$ in per ATP hydrolyzed. Because it moves one net positive charge outward per cycle it is electrogenic, adding a few millivolts to the resting potential directly; its main contribution is indirect, by maintaining the gradients through which the channels set the potential. Gradients of other ions are maintained by **cotransporters** that use the $\ce{Na+}$ gradient: the $\ce{Na+}/\ce{Ca^2+}$ exchanger (three $\ce{Na+}$ in per $\ce{Ca^2+}$ out) keeps cytoplasmic $\ce{Ca^2+}$ near $100\,\mathrm{nM}$, and the $\ce{K+}/\ce{Cl-}$ cotransporter KCC2 lowers intracellular $\ce{Cl-}$ in mature neurons, which makes $\mathrm{GABA_A}$ receptors inhibitory.

**Example 30.1.2 (Is the pump efficient?)** In the muscle fiber of the table ($V = -90\,\mathrm{mV}$, $37\,{}^\circ\mathrm{C}$), moving three $\ce{Na+}$ out costs $3k_{\mathrm{B}}T\ln(145/12) = 7.5\,k_{\mathrm{B}}T$ against the concentration gradient and $3e\times90\,\mathrm{mV} = 3 \times 90/26.7\,k_{\mathrm{B}}T = 10.1\,k_{\mathrm{B}}T$ against the field. Moving two $\ce{K+}$ in costs $2\ln(155/4) = 7.3\,k_{\mathrm{B}}T$ against the gradient but gains $6.7\,k_{\mathrm{B}}T$ from the field. The total, $18.2\,k_{\mathrm{B}}T$, is to be compared with the free energy of ATP hydrolysis in the cytoplasm, $-\Delta G \approx 50$–$60\,\mathrm{kJ\,mol^{-1}} = 19$–$23\,k_{\mathrm{B}}T$ at $37\,{}^\circ\mathrm{C}$ ([7.6.3](/7.6.3)). The pump works at 80–95 % of its thermodynamic limit, and almost all of its work is spent on sodium, which is far from equilibrium; potassium is nearly at its Nernst potential.

## 30.2. Permeation

### 30.2.1. The Nernst–Planck Equation

An ion in solution moves by diffusion down its concentration gradient and drifts in an electric field. In the field $E$ it experiences the force $zeE$; in water its inertia is negligible on time scales above picoseconds ([7.6.22](/7.6.22)), and its mean drift velocity is the force divided by its friction coefficient $\zeta$. Microscopically, a collision randomizes the velocity, the field accelerates the ion by $a = zeE/m$ between collisions, and the mean drift velocity is $a\tau_{\mathrm{c}}$, with $\tau_{\mathrm{c}}$ the velocity relaxation time, so $\zeta = m/\tau_{\mathrm{c}}$. The **Einstein–Smoluchowski relation** $D = k_{\mathrm{B}}T/\zeta$ ([7.6.5](/7.6.5)) connects the friction to the **diffusion coefficient**.

**Definition 30.2.1 (Nernst–Planck Equation)** The flux density of an ion of valence $z$, concentration $c$ and diffusion coefficient $D$ in a potential $\varphi(\boldsymbol{r})$ is given by the **Nernst–Planck equation**
$$
\boldsymbol{J} = -D\left(\nabla c + \frac{ze}{k_{\mathrm{B}}T}c\nabla\varphi\right) = -\frac{Dc}{k_{\mathrm{B}}T}\nabla\tilde\mu, \tag{30.2}
$$
the sum of a Fickian diffusion flux and a drift flux $c\,(zeE)/\zeta$ with $\boldsymbol{E} = -\nabla\varphi$; equivalently the flux is proportional to the gradient of the electrochemical potential $\tilde\mu$.

Setting $\boldsymbol{J} = 0$ in one dimension gives $\mathrm{d}\ln c/\mathrm{d}x = -(ze/k_{\mathrm{B}}T)\,\mathrm{d}\varphi/\mathrm{d}x$, whose integral across the membrane is the Nernst equation (30.1): equilibrium is the absence of flux, not the absence of gradients.

### 30.2.2. Constant-Field Theory: The GHK Equations

To compute the current through a membrane carrying a potential $V = \varphi_{\mathrm{in}} - \varphi_{\mathrm{out}}$, Goldman (1943) and Hodgkin and Katz (1949) assumed that ions move independently, that the field inside the membrane is uniform, and that the concentrations just inside the membrane faces are $\beta c_{\mathrm{in}}$ and $\beta c_{\mathrm{out}}$, with $\beta$ the partition coefficient into the membrane.

**Theorem 30.2.1 (Goldman–Hodgkin–Katz Current Equation)** Under these assumptions the outward current density carried by an ion of valence $z$ is
$$
I = P\,\frac{z^2\mathrm{e}^2V}{k_{\mathrm{B}}T}\,\frac{c_{\mathrm{in}} - c_{\mathrm{out}}\,\mathrm{e}^{-u}}{1 - \mathrm{e}^{-u}}, \qquad u = \frac{zeV}{k_{\mathrm{B}}T}, \tag{30.3}
$$
with concentrations in particles per volume and permeability $P = \beta D/d$ for a membrane of thickness $d$. The current vanishes at the Nernst potential, and for several monovalent ions the zero-current potential is
$$
V_{\mathrm{rev}} = \frac{k_{\mathrm{B}}T}{e}\ln\frac{P_{\mathrm{K}}[\ce{K+}]_{\mathrm{out}} + P_{\mathrm{Na}}[\ce{Na+}]_{\mathrm{out}} + P_{\mathrm{Cl}}[\ce{Cl-}]_{\mathrm{in}}}{P_{\mathrm{K}}[\ce{K+}]_{\mathrm{in}} + P_{\mathrm{Na}}[\ce{Na+}]_{\mathrm{in}} + P_{\mathrm{Cl}}[\ce{Cl-}]_{\mathrm{out}}}. \tag{30.4}
$$

**Proof** Measure $x$ from the inner face ($x = 0$) to the outer face ($x = d$). With a constant field, $\varphi(x) = V(1 - x/d)$ relative to the outside, and Eq. (30.2) becomes the linear ordinary differential equation $\mathrm{d}c/\mathrm{d}x - (u/d)c = -J/D$, where $J$ is the outward flux, constant in steady state. Multiplying by the integrating factor $\mathrm{e}^{-ux/d}$ and integrating from $0$ to $d$,
$$
c(d)\,\mathrm{e}^{-u} - c(0) = -\frac{Jd}{Du}\left(1 - \mathrm{e}^{-u}\right).
$$
With $c(0) = \beta c_{\mathrm{in}}$ and $c(d) = \beta c_{\mathrm{out}}$, $J = (\beta D/d)\,u\,(c_{\mathrm{in}} - c_{\mathrm{out}}\mathrm{e}^{-u})/(1 - \mathrm{e}^{-u})$, and $I = zeJ$ gives Eq. (30.3). For one ion, $I = 0$ requires $c_{\mathrm{in}} = c_{\mathrm{out}}\mathrm{e}^{-u}$, the Nernst equation. For several ions, the total current vanishes when $\sum_jP_jz_j^2(c_{\mathrm{in},j} - c_{\mathrm{out},j}\mathrm{e}^{-u_j}) = 0$ (the common factor $V/(1 - \mathrm{e}^{-u})$ cancels for ions of equal $\lvert z\rvert$, noting that for $\ce{Cl-}$, $u$ changes sign); solving for $\mathrm{e}^{eV/k_{\mathrm{B}}T}$ gives Eq. (30.4). $\square$

Equation (30.4), the GHK voltage equation, is the one used in cell biology ([7.3.5](/7.3.5#sec-5.6.2)): the potential lies closest to the Nernst potential of the most permeant ion. At rest, $P_{\mathrm{K}}:P_{\mathrm{Na}}:P_{\mathrm{Cl}} \approx 1:0.04:0.45$ in the squid axon, giving about $-60$ to $-70\,\mathrm{mV}$, and the resting chloride permeability of skeletal muscle is even larger than that of potassium; at the peak of an action potential $P_{\mathrm{Na}}$ rises several hundredfold and the potential approaches $E_{\mathrm{Na}}$.

The current equation (30.3) has a second lesson. Linearizing it about the reversal potential gives the ohmic approximation used in circuit models,
$$
I = g\,(V - E_{\mathrm{ion}}), \tag{30.5}
$$
with slope conductance $g = \partial I/\partial V$ at $E_{\mathrm{ion}}$, which depends on concentrations as well as on $P$. Away from $E_{\mathrm{ion}}$ the GHK current is not linear: current flowing out of the concentrated compartment is larger than the linear prediction, current flowing in from the dilute one smaller. This Goldman rectification is a property of the concentration asymmetry, not of the channel.

![Current–voltage relations. A, B: GHK current equation (30.3) for K⁺- and Na⁺-selective membranes with the concentrations of the table (37 °C), compared with the linear approximation (30.5) tangent at the reversal potential: Goldman rectification bends each curve toward larger current when ions flow from the concentrated side. C: the NMDA receptor, a ligand-gated cation channel with reversal potential near 0 mV, blocked by external Mg²⁺ in a voltage-dependent way (Woodhull model with the Jahr–Stevens parameters, Formula 30.3.2): at 1 mM Mg²⁺ the current is suppressed at negative potentials and appears on depolarization, a J-shaped curve](./plots/ghk-iv.py)

### 30.2.3. Single Channels and the Patch Clamp

The **patch clamp** (Neher and Sakmann, 1976; gigaohm seals, Hamill and colleagues 1981) records the current through single channels. A fire-polished glass pipette with a tip of about $1\,\mu\mathrm{m}$ is pressed against a cell; gentle suction forms a seal of resistance $10$–$100\,\mathrm{G\Omega}$ between glass and membrane. The current noise of a resistance $R$ over a bandwidth $B$ is $\sqrt{4k_{\mathrm{B}}TB/R}$; for $R = 10\,\mathrm{G\Omega}$ and $B = 1\,\mathrm{kHz}$ it is $0.04\,\mathrm{pA}$, small enough to resolve the picoampere steps of single channels. Four configurations are used (figure below): cell-attached, whole-cell, and the excised inside-out and outside-out patches, which give control over the solution on either face.

A single open channel passes a current $i = \gamma(V - E_{\mathrm{rev}})$, where $\gamma$ is its single-channel conductance. One picoampere is $6.2\times10^6$ elementary charges per second. Conductances range from a few picosiemens (some $\ce{Ca^2+}$-release-activated channels, below 1 pS) through $10$–$20\,\mathrm{pS}$ for voltage-gated $\ce{K+}$ and $\ce{Na+}$ channels to $250\,\mathrm{pS}$ for the large-conductance $\ce{Ca^2+}$-activated $\ce{K+}$ channel BK; a BK channel at $100\,\mathrm{mV}$ driving force passes $25\,\mathrm{pA}$, $1.6\times10^8$ ions per second. Diffusion limits the rate: ions reach a capture hemisphere of radius $a$ at the pore mouth at a rate $2\pi Dac$, about $4\times10^8\,\mathrm{s^{-1}}$ for $D = 2\times10^{-9}\,\mathrm{m^2\,s^{-1}}$, $a = 0.3\,\mathrm{nm}$ and $c = 150\,\mathrm{mM}$. The fastest channels operate near this limit.

![Two schematics. A: the four patch-clamp configurations: cell-attached (gigaseal on an intact cell), whole-cell (patch ruptured by suction), inside-out (patch excised from a cell-attached seal, cytoplasmic face to the bath) and outside-out (patch pulled from the whole-cell configuration, which reseals with the extracellular face to the bath). B: the selectivity filter of a K⁺ channel (two of four subunits): the carbonyl oxygens of TVGYG form four sites S1–S4, each a cage of eight oxygens; ions occupy alternate sites separated by water and move by knock-on (30.2.5)](./plots/channel-schematics.py)

### 30.2.4. Rate-Theory Models of Permeation

Electrodiffusion in a uniform membrane cannot explain two facts: single-channel conductance saturates with concentration, and the current through some channels depends on the concentration on the other side in a way that violates independence. Both follow if the pore contains binding sites separated by barriers, with transitions over each barrier given by the **Eyring equation**, $k = \nu\exp(-\Delta G^\ddagger/k_{\mathrm{B}}T)$ ([6.3.16](/6.3.16)). The membrane potential tilts the free-energy profile: an ion at fractional electrical distance $\delta$ from the inside has electrical energy $ze V(1 - \delta)$ relative to the outside, so each rate depends exponentially on $V$ through the fraction of the field crossed between the well and the barrier.

**Formula 30.2.1 (One-Site, Two-Barrier Pore)** For a pore with one site that holds at most one ion, entered from the inside with rate $k_1c_{\mathrm{in}}$ and from the outside with rate $k_{-2}c_{\mathrm{out}}$, and left to the inside and the outside with rates $k_{-1}$ and $k_2$, the probability of occupancy is $p = (k_1c_{\mathrm{in}} + k_{-2}c_{\mathrm{out}})/(k_1c_{\mathrm{in}} + k_{-2}c_{\mathrm{out}} + k_{-1} + k_2)$ and the outward ion flux is
$$
J = p\,k_2 - (1 - p)\,k_{-2}c_{\mathrm{out}},
$$
each rate constant carrying the voltage dependence $\exp(\pm ze\,\Delta\delta\,V/k_{\mathrm{B}}T)$ of the electrical distance between site and barrier.

At low concentration the pore is mostly empty and the conductance grows linearly with $c$; at high concentration it is mostly occupied and the conductance saturates with Michaelis–Menten form, as Hille and colleagues measured for $\ce{Na+}$ and $\ce{K+}$ channels. An asymmetric profile rectifies even with identical solutions. Multi-ion pores, in which two or more ions are present at once and repel each other, explain the anomalous mole-fraction effect (the conductance in mixtures of two permeant ions falls below that of either alone) and flux-ratio exponents larger than 1 (Hodgkin and Keynes, 1955), which reveal single-file movement.

![Rate-theory model of permeation (Formula 30.2.1). A: free-energy profile of a pore with one well between two barriers at 0 and +60 mV; the field tilts the profile. B: I–V curves with 100 mM on both sides for a symmetric pore (nearly linear) and for an asymmetric pore with the site near the inside and a higher outer barrier, which rectifies although the solutions are identical. C: single-channel conductance at 0 mV against concentration: the one-site pore saturates, free electrodiffusion does not](./plots/barrier-model.py)

### 30.2.5. Selectivity: The K⁺ Channel Filter

A $\ce{K+}$ channel conducts $\ce{K+}$ at nearly $10^8$ ions per second while excluding the smaller $\ce{Na+}$ by a factor of more than a hundred, often a thousand. Size alone cannot explain this.

The first clue came from pharmacology. Tetraethylammonium (TEA) blocks $\ce{K+}$ channels, and Armstrong showed in the 1960s and 1970s that it acts competitively from the inside, although it resembles $\ce{K+}$ in neither size nor shape. His explanation was that $\ce{K+}$ enters the channel's inner vestibule hydrated, and that TEA, with its ethyl groups covalently fixed around the nitrogen, mimics a $\ce{K+}$ ion with its first shell of water, but one that can never be dehydrated. With TEA derivatives carrying hydrophobic tails of increasing length he inferred a hydrophobic region in the inner pore, and he proposed that the narrow part of the pore strips the water and replaces it with oxygen atoms of the protein. The gene of the *Drosophila* $\ce{K+}$ channel Shaker was cloned in 1987 (Jan and colleagues), and the crystal structure of the bacterial channel KcsA (Doyle, MacKinnon and colleagues, 1998) confirmed and sharpened the picture.

**Definition 30.2.2 (Selectivity Filter)** The **selectivity filter** is the narrowest part of a channel pore, where permeating ions lose most of their hydration water and interact directly with the protein, and whose geometry and chemistry determine which ions pass.

In $\ce{K+}$ channels the filter is formed by the signature sequence TVGYG of the four subunits, $1.2\,\mathrm{nm}$ long. The backbone carbonyl oxygens (and the threonine hydroxyl at the bottom) point into the pore and form four sites, S1–S4, each a square antiprism of eight oxygens like the eight water oxygens around a hydrated $\ce{K+}$. The filter is held rigidly at the right size for $\ce{K+}$: a $\ce{Na+}$ ion, $0.4\,\text{Å}$ smaller in radius ($0.95$ versus $1.33\,\text{Å}$), cannot be contacted by all eight oxygens at once, so the energy it gains in the filter does not pay for its larger dehydration cost (snug fit; the electrostatic field strength of the carbonyls also matters). Below the filter a water-filled cavity and the hydrophobic inner pore of Armstrong's experiments keep a $\ce{K+}$ ion hydrated at the center of the membrane, where helix dipoles pointing at the cavity stabilize it.

Conduction is concerted. Crystal structures at high and low $\ce{K+}$ and anomalous scattering of $\ce{Tl+}$ and $\ce{Rb+}$ showed two ions in the filter at a time, in the configurations S1–S3 and S2–S4 alternating with water molecules (Morais-Cabral, Zhou and MacKinnon, 2001). A third ion entering from one side pushes the queue forward by one step (knock-on), and the mutual repulsion of the ions offsets their strong binding, so the filter can bind $\ce{K+}$ selectively and still release it fast. Calcium channels select by a different mechanism: a ring of four glutamates (EEEE in $\mathrm{Ca_V}$ channels) binds $\ce{Ca^2+}$ with micromolar affinity; a single $\ce{Ca^2+}$ blocks monovalent flow and two $\ce{Ca^2+}$ repel each other through the pore. Voltage-gated $\ce{Na+}$ channels have a DEKA ring and a wider filter that passes partially hydrated $\ce{Na+}$.

## 30.3. Gating

### 30.3.1. Voltage Sensors

Channels open and close (gate) in response to voltage, ligands, mechanical force or temperature. The statistical mechanics of two-state gating, with the **gating charge** $ze$ as the variable conjugate to voltage, is in [7.6.4](/7.6.4#sec-4.2.2): for a **two-state system** the open probability is a Boltzmann function of $V$, changing $\mathrm{e}$-fold per $k_{\mathrm{B}}T/ze$, and the gating charge of Shaker is about $13\,e$.

**Definition 30.3.1 (Voltage Sensor)** The **voltage sensor** (voltage-sensing domain) of a voltage-gated channel is the domain formed by the transmembrane helices S1–S4 of each subunit or repeat, in which the S4 helix carries positively charged residues (arginines, occasionally lysines, at every third position) that move across the membrane field when the membrane depolarizes and pull on the pore through the S4–S5 linker.

The architecture is modular. A voltage-gated $\ce{K+}$ channel ($\mathrm{K_V}$) is a tetramer of subunits with six transmembrane helices; S5 and S6 of the four subunits form the pore domain with the filter, and S1–S4 of each form a sensor at the periphery. Voltage-gated $\ce{Na+}$ and $\ce{Ca^2+}$ channels ($\mathrm{Na_V}$, $\mathrm{Ca_V}$) are single polypeptides with four homologous repeats (I–IV), the four subunits of a $\mathrm{K_V}$ channel fused into one gene. At rest, the electric field holds the S4 arginines toward the inside; a gating charge transfer center of conserved residues (two polar or acidic residues and a phenylalanine in S2, an aspartate in S3) forms a hydrophobic constriction through which the arginines pass one after another, exchanging ion pairs, while S4 moves outward by roughly $1$–$1.5\,\mathrm{nm}$ and partly rotates (a sliding helix, with a $3_{10}$-helical stretch that keeps the arginines facing the same way). In the closed pore, hydrophobic side chains at the bundle crossing of the four S6 helices block the inner entrance; outward movement of the sensors pulls the S4–S5 linkers and lets the S6 helices splay apart. Each of the four sensors of a $\mathrm{K_V}$ channel moves independently, and the pore opens only when all four have moved: the structural basis of the $n^4$ of the Hodgkin–Huxley model (30.6).

$\mathrm{Na_V}$ channels add fast inactivation. Within 1–2 ms of opening, a short hydrophobic motif (IFM in human channels, LFM in the eel channel $\mathrm{Na_V1.4}$ whose structure first showed it) in the intracellular linker between repeats III and IV binds in a pocket next to the S6 helices and S4–S5 linkers of repeats III and IV and closes the pore allosterically (rather than plugging it as Armstrong's "ball and chain" model of Shaker inactivation did). Sensors I–III control activation, and the slower movement of sensor IV is rate-limiting for inactivation: the three $m$ gates and one $h$ gate of Hodgkin and Huxley.

### 30.3.2. Gating Currents

The movement of gating charge is itself a current, small but measurable. When the ionic currents are blocked (with tetrodotoxin for $\mathrm{Na_V}$, internal $\ce{Cs+}$ or TEA for $\mathrm{K_V}$) and the linear capacitive current is subtracted (by scaling the response to small hyperpolarizing steps, the P/4 protocol), a brief outward transient remains on depolarization and an inward one on repolarization (Armstrong and Bezanilla, 1973; Schneider and Chandler, 1973).

**Definition 30.3.2 (Gating Current)** The **gating current** of a population of voltage-gated channels is the displacement current carried by the movement of charged groups of their voltage sensors within the membrane field; its time integral after a voltage step is the gating charge $Q$ moved, and the curve $Q(V)$ is the charge–voltage relation.

Gating currents answer questions that ionic currents cannot. The total charge per channel is $Q_{\max}/N$, where the number $N$ of channels is counted by toxin binding or by noise analysis; for Shaker, $12$–$14\,e$ (Schoppa and colleagues 1992; Aggarwal and MacKinnon 1996), in agreement with the four sensors carrying about $3.3\,e$ each. The charge–voltage curve lies to the left of the conductance–voltage curve and is shallower, because most of the charge moves in transitions among closed states before the final opening step. A single Boltzmann fit to the conductance therefore underestimates the gating charge (by more than half in the model of the figure); the reliable estimate is the limiting slope of $\ln p_{\mathrm{o}}$ at very negative potentials, where $p_{\mathrm{o}} \propto \exp(z_{\mathrm{tot}}eV/k_{\mathrm{B}}T)$ (Almers 1978).

![Gating charge in a model channel with four independent two-state sensors of 3.25 e each and a pore that opens when all four are activated. A: normalized Q–V (∝ n) and G–V (∝ n⁴) curves: the conductance is steeper and right-shifted, and a single Boltzmann fit to it gives an apparent charge of about 4 e instead of the 13 e that move. B: gating currents after steps from −100 mV: fast transients whose integrals are the moved charge. C: the ionic currents rise with a sigmoidal delay after most of the charge has moved](./plots/gating-currents.py)

### 30.3.3. Single-Channel Kinetics

A single channel switches stochastically among its conformations, and its record is a random telegraph signal. With discrete states and rate constants for each transition, the probabilities obey a **master equation** ([7.6.5](/7.6.5)), $\mathrm{d}\boldsymbol{p}/\mathrm{d}t = \boldsymbol{p}Q$, where $Q$ is the matrix of transition rates (rows sum to zero).

**Theorem 30.3.1 (Dwell-Time Distributions)** Partition the states into open ($\mathcal{O}$) and closed ($\mathcal{C}$) classes and let $Q_{\mathcal{CC}}$ be the submatrix of rates among closed states. The duration of a closed interval has density
$$
f_{\mathcal{C}}(t) = \boldsymbol{\pi}_{\mathcal{C}}\,\mathrm{e}^{Q_{\mathcal{CC}}t}\,Q_{\mathcal{CO}}\boldsymbol{1}, \tag{30.6}
$$
where $\boldsymbol{\pi}_{\mathcal{C}}$ is the distribution over closed states at the start of a closed interval and $Q_{\mathcal{CO}}\boldsymbol{1}$ the vector of exit rates to the open class; the same holds for open intervals. The density is a sum of $n_{\mathcal{C}}$ exponentials, where $n_{\mathcal{C}}$ is the number of closed states, with time constants equal to minus the inverses of the eigenvalues of $Q_{\mathcal{CC}}$.

**Proof** During a closed interval the channel evolves within $\mathcal{C}$ with generator $Q_{\mathcal{CC}}$ (transitions out of $\mathcal{C}$ end the interval), so the probability of being in each closed state at time $t$ without having left is $\boldsymbol{\pi}_{\mathcal{C}}\mathrm{e}^{Q_{\mathcal{CC}}t}$; the density of leaving at $t$ multiplies this by the exit rates. Diagonalizing $Q_{\mathcal{CC}}$ gives the sum of exponentials. $\square$

Counting exponential components in dwell-time histograms thus counts states (Colquhoun and Hawkes). Histograms are best displayed with logarithmic time bins and a square-root ordinate (Sigworth and Sine 1987): each exponential component then appears as a peak at its time constant. Single-channel records are simulated exactly with the **Gillespie algorithm** ([4.4.7](/4.4.7)), drawing each dwell time from an exponential distribution with the total exit rate of the current state; hidden-Markov methods fit models directly to noisy records.

![Single-channel kinetics of the scheme C1 ⇌ C2 ⇌ O (rates per ms: 0.2, 1.0, 2.0, 0.5) simulated with the Gillespie algorithm. A: 200 ms of a simulated patch-clamp record (−2 pA when open, 0.25 pA rms noise): openings come in bursts. B: open dwell times (log bins, square-root ordinate) follow one exponential with τ = 2 ms. C: closed dwell times show two components, brief closures within bursts and long gaps between bursts; the curve is Eq. (30.6)](./plots/single-channel.py)

### 30.3.4. Ligand-Gated Channels and the NMDA Receptor

Ligand-gated channels convert a chemical signal into a current. The nicotinic acetylcholine receptor of the neuromuscular junction, a pentamer that opens when two acetylcholine molecules bind, is the textbook example of the MWC model ([7.6.4](/7.6.4#sec-4.5.2)). Glutamate receptors are tetramers that pass $\ce{Na+}$ and $\ce{K+}$ (and, for some, $\ce{Ca^2+}$) with a reversal potential near $0\,\mathrm{mV}$ and therefore depolarize neurons at rest.

The NMDA-type glutamate receptor (activated by N-methyl-D-aspartate) has two unusual properties, which Mayer, Westbrook and Guthrie (1984) and Nowak and colleagues (1984) showed to be one: it is blocked by external $\ce{Mg^2+}$, and it conducts little at negative potentials even when glutamate is bound. $\ce{Mg^2+}$ enters the pore from outside and binds at a site deep in the field, from which it rarely permeates; hyperpolarization pulls it in, depolarization expels it.

**Formula 30.3.2 (Voltage-Dependent Block)** For a blocker of valence $z$ that binds at a site a fraction $\delta$ of the electrical distance into the membrane from the outside (Woodhull, 1973), the fraction of unblocked channels is
$$
\frac{1}{1 + [\mathrm{B}]/K(V)}, \qquad K(V) = K(0)\exp\left(\frac{z\delta eV}{k_{\mathrm{B}}T}\right). \tag{30.7}
$$
For $\ce{Mg^2+}$ block of NMDA receptors, $K(V) \approx 3.57\,\mathrm{mM}\,\mathrm{e}^{0.062V/\mathrm{mV}}$ (Jahr and Stevens, 1990), corresponding to $z\delta \approx 1.6$.

The NMDA receptor therefore opens only when glutamate is present (presynaptic activity) and the postsynaptic membrane is depolarized (postsynaptic activity): it is a molecular coincidence detector. Its $\ce{Ca^2+}$ influx activates the $\ce{Ca^2+}$/calmodulin-dependent kinase CaMKII and strengthens the synapse, the mechanism behind Hebb's postulate ("cells that fire together wire together") and long-term potentiation. The voltage dependence here does not come from a sensor but from a permeating ion: the physics of Eq. (30.7) is the same barrier tilting as in Formula 30.2.1.

## 30.4. The Membrane as an Excitable Circuit

### 30.4.1. The Equivalent Circuit

Conservation of charge for a patch of membrane with capacitance $C$ per area, conductances $g_j$ and Nernst potentials $E_j$ for each ion, and an applied current $I_{\mathrm{app}}$ (all per area) gives
$$
C\frac{\mathrm{d}V}{\mathrm{d}t} = -\sum_jg_j(V, t)\,(V - E_j) + I_{\mathrm{app}}. \tag{30.8}
$$
With constant conductances, the steady state is the conductance-weighted mean of the Nernst potentials, $V^* = \sum_jg_jE_j/\sum_jg_j$, the linear counterpart of Eq. (30.4), and a small perturbation relaxes with the membrane time constant
$$
\tau_{\mathrm{m}} = \frac{C}{g} = R_{\mathrm{m}}c_{\mathrm{m}}, \tag{30.9}
$$
where $R_{\mathrm{m}} = 1/g$ is the specific membrane resistance. Since $c_{\mathrm{m}}$ is nearly universal, $\tau_{\mathrm{m}}$ measures the resting conductance: $R_{\mathrm{m}} \approx 1\,\mathrm{k\Omega\,cm^2}$ in the squid axon gives $1\,\mathrm{ms}$, $R_{\mathrm{m}} \approx 20\,\mathrm{k\Omega\,cm^2}$ in cortical neurons gives $20\,\mathrm{ms}$.

### 30.4.2. A Bistable Patch

Let the $\ce{K+}$ conductance be constant and the $\ce{Na+}$ conductance follow the two-state gating of [7.6.4](/7.6.4), $g_{\mathrm{Na}}(V) = \bar g_{\mathrm{Na}}/[1 + \exp(-z_{\mathrm{g}}e(V - V_{1/2})/k_{\mathrm{B}}T)]$. The right side of Eq. (30.8) is then a nonlinear function of $V$ alone, and its zeros are the steady states.

**Proposition 30.4.1 (Bistability)** If $\bar g_{\mathrm{Na}} \gg g_{\mathrm{K}} \gg g_{\mathrm{Na}}(E_{\mathrm{K}})$ and the gating midpoint lies between $E_{\mathrm{K}}$ and $E_{\mathrm{Na}}$, the patch has three steady states: a stable one near $E_{\mathrm{K}}$, a stable one near $E_{\mathrm{Na}}$, and an unstable one in between, which acts as a threshold.

**Proof** Write $\dot V = h(V)/C$ with $h = -g_{\mathrm{K}}(V - E_{\mathrm{K}}) - g_{\mathrm{Na}}(V)(V - E_{\mathrm{Na}})$. Slightly above $E_{\mathrm{K}}$, $g_{\mathrm{Na}}$ is negligible and $h < 0$; slightly below, $h > 0$: a stable zero near $E_{\mathrm{K}}$. Near $E_{\mathrm{Na}}$, $g_{\mathrm{Na}} \approx \bar g_{\mathrm{Na}} \gg g_{\mathrm{K}}$, and the same argument gives a stable zero just below $E_{\mathrm{Na}}$. A continuous function that is negative above the first zero and positive below the second must cross zero once more in between, upward, which is an unstable fixed point. $\square$

A depolarization that crosses the threshold sends the patch to the sodium state; one that falls short decays back with time constant $\tau_{\mathrm{m}}$. This bistability, the all-or-none character of excitation, is the first ingredient of the action potential. The second is recovery: if $g_{\mathrm{Na}}$ inactivates and $g_{\mathrm{K}}$ increases with delay, the sodium state is lost and the patch returns to rest, so that a bistable switch becomes a pulse (30.6).

## 30.5. The Cable Equation

### 30.5.1. Derivation

An axon or dendrite is a thin cylinder of conducting cytoplasm surrounded by membrane. Let it have radius $a$, cytoplasmic resistivity $R_{\mathrm{i}}$, specific membrane resistance $R_{\mathrm{m}}$ and capacitance $c_{\mathrm{m}}$, and neglect the resistance of the extracellular fluid. The resistance of the core per length is $r_{\mathrm{i}} = R_{\mathrm{i}}/\pi a^2$, and the membrane per length has resistance $r_{\mathrm{m}} = R_{\mathrm{m}}/2\pi a$ and capacitance $2\pi ac_{\mathrm{m}}$.

**Theorem 30.5.1 (Cable Equation)** Let $V(x, t)$ be the deviation of the membrane potential from rest in a passive cylinder. Then
$$
\lambda^2\frac{\partial^2V}{\partial x^2} = \tau_{\mathrm{m}}\frac{\partial V}{\partial t} + V, \qquad \lambda = \sqrt{\frac{r_{\mathrm{m}}}{r_{\mathrm{i}}}} = \sqrt{\frac{aR_{\mathrm{m}}}{2R_{\mathrm{i}}}}, \qquad \tau_{\mathrm{m}} = R_{\mathrm{m}}c_{\mathrm{m}}. \tag{30.10}
$$

**Proof** Ohm's law for the axial current $I_{\mathrm{a}}$ gives $\partial V/\partial x = -r_{\mathrm{i}}I_{\mathrm{a}}$. Conservation of charge in a slice of length $\mathrm{d}x$: the axial current lost, $-(\partial I_{\mathrm{a}}/\partial x)\mathrm{d}x$, flows through the membrane as capacitive and resistive current, $(2\pi ac_{\mathrm{m}}\partial_tV + V/r_{\mathrm{m}})\mathrm{d}x$. Eliminating $I_{\mathrm{a}}$, $(1/r_{\mathrm{i}})\partial_x^2V = 2\pi ac_{\mathrm{m}}\partial_tV + V/r_{\mathrm{m}}$; multiplying by $r_{\mathrm{m}}$ and noting $2\pi ac_{\mathrm{m}}r_{\mathrm{m}} = R_{\mathrm{m}}c_{\mathrm{m}}$ gives Eq. (30.10). $\square$

**Definition 30.5.1 (Cable Equation and Length Constant)** Equation (30.10) is the **cable equation** of a passive neurite (Kelvin's equation for the transatlantic telegraph cable, applied to nerve by Hermann, Hodgkin and Rushton), and $\lambda$ is its **length constant**: the distance over which a steady voltage decays by the factor $\mathrm{e}$.

In the steady state a voltage $V_0$ clamped at $x = 0$ of a long cable decays as $V_0\mathrm{e}^{-x/\lambda}$. In time, the equation is the **heat equation** with a decay term: substituting $V = \mathrm{e}^{-t/\tau_{\mathrm{m}}}U$ gives $\tau_{\mathrm{m}}\partial_tU = \lambda^2\partial_x^2U$, so a brief, local charge injection spreads as a Gaussian whose width grows as $\lambda\sqrt{2t/\tau_{\mathrm{m}}}$ while its area decays as $\mathrm{e}^{-t/\tau_{\mathrm{m}}}$. Passive signals therefore travel only a few length constants, and their "speed" (about $2\lambda/\tau_{\mathrm{m}}$ for the peak) is not that of a wave.

**Example 30.5.1 (Length constants)** For the squid giant axon ($a = 250\,\mu\mathrm{m}$, $R_{\mathrm{m}} = 0.1\,\mathrm{\Omega\,m^2}$, $R_{\mathrm{i}} = 0.3\,\mathrm{\Omega\,m}$), $\lambda = \sqrt{(2.5\times10^{-4})(0.1)/0.6} = 6.5\,\mathrm{mm}$. For a thin dendrite ($a = 1\,\mu\mathrm{m}$, $R_{\mathrm{m}} = 2\,\mathrm{\Omega\,m^2}$, $R_{\mathrm{i}} = 1\,\mathrm{\Omega\,m}$), $\lambda = 1\,\mathrm{mm}$. A signal could not travel a meter along any axon passively: after $1\,\mathrm{m} = 150\lambda$ of the squid axon it would be attenuated by $\mathrm{e}^{-150}$. Long-distance signaling requires regeneration.

![The membrane as circuit and cable. A: steady passive spread V = V0 exp(−x/λ) in a dendrite (λ = 1 mm) and the squid giant axon (λ = 6.5 mm) (Example 30.5.1). B: spread of a brief local charge injection in a passive cable at three times: a Gaussian (heat kernel) decaying with the membrane time constant. C: phase line of a patch with constant K⁺ conductance and a two-state voltage-gated Na⁺ conductance: two stable steady states near E_K and E_Na (filled) and an unstable threshold between them (open), Proposition 30.4.1](./plots/cable.py)

### 30.5.2. Regenerative Waves

Add the voltage-gated conductances of the bistable patch to the cable, and Eq. (30.10) becomes a reaction–diffusion equation, $\lambda^2\partial_x^2V = \tau\partial_tV + F(V)$, with $F$ the dimensionless ionic current of Proposition 30.4.1. A region pushed above threshold pulls its neighbors above threshold by axial current, and the sodium state invades the resting state as a traveling front of fixed shape and speed (Luther's autocatalytic waves; Fisher–Kolmogorov fronts for monostable $F$, trigger waves of [7.6.36](/7.6.36) for bistable $F$).

**Proposition 30.5.1 (Front Speed)** For the bistable cable $\tau\partial_tV = \lambda^2\partial_x^2V + f(V)$ with the cubic $f(V) = kV(1 - V)(V - \alpha)$, $0 < \alpha < 1/2$ (in units of the voltage span), a front from the resting to the excited state travels at
$$
v = \frac{\lambda}{\tau}\sqrt{\frac{k}{2}}\,(1 - 2\alpha). \tag{30.11}
$$
In general, dimensional analysis gives $v = (\lambda/\tau)\,\Phi$ with a dimensionless $\Phi$ depending only on the shape of $F$; since $\lambda \propto \sqrt a$ and $\tau$ does not depend on $a$, the conduction velocity of an unmyelinated axon grows as the square root of its diameter.

**Proof** Look for $V = U(\xi)$, $\xi = x - vt$: $\lambda^2U'' + v\tau U' + f(U) = 0$. Try $U' = -BU(1 - U)$ (a logistic front with $U \to 1$ behind it and $U \to 0$ ahead). Then $U'' = B^2U(1 - U)(1 - 2U)$, and substituting, $U(1 - U)[\lambda^2B^2(1 - 2U) - v\tau B + k(U - \alpha)] = 0$ for all $U$ requires $2\lambda^2B^2 = k$ and $\lambda^2B^2 - v\tau B - k\alpha = 0$. Hence $B = \sqrt{k/2}/\lambda$ and $v\tau B = k(1/2 - \alpha)$, which gives Eq. (30.11). $\square$

The front moves into the resting state when $\alpha < 1/2$ (the excited state is "more stable"); a front alone, however, leaves the axon depolarized. In an axon, sodium inactivation and delayed potassium activation restore rest behind the front, turning it into a pulse: the action potential.

## 30.6. The Hodgkin–Huxley Model

### 30.6.1. The Voltage Clamp

Hodgkin and Huxley's analysis of the squid giant axon (five papers, 1952) is the founding example of quantitative cellular biophysics. The axon, up to $1\,\mathrm{mm}$ across, admitted a silver wire along its axis that made its interior isopotential (space clamp), and a feedback amplifier held the membrane potential at a command value.

**Definition 30.6.1 (Voltage Clamp)** In a **voltage clamp** a feedback amplifier measures the membrane potential and injects whatever current is needed to hold it at a command value; after the brief capacitive transient of a step, the injected current equals the total ionic current at that fixed potential, which can thus be measured as a function of time and voltage.

The current after a depolarizing step is first inward and then outward. Replacing most external $\ce{Na+}$ by choline removed the early inward component, separating $I_{\mathrm{Na}}$ from $I_{\mathrm{K}}$. Dividing each current by its driving force gave conductances, $g_{\mathrm{Na}} = I_{\mathrm{Na}}/(V - E_{\mathrm{Na}})$ and $g_{\mathrm{K}} = I_{\mathrm{K}}/(V - E_{\mathrm{K}})$, and the conductances, not the currents, turned out to be simple: $g_{\mathrm{K}}$ rises with a sigmoidal delay and stays; $g_{\mathrm{Na}}$ rises quickly and then falls (inactivation) even though the voltage is held.

### 30.6.2. The Gating Variables

**Definition 30.6.2 (Hodgkin–Huxley Model)** The **Hodgkin–Huxley model** describes the membrane current of an excitable patch as
$$
C\frac{\mathrm{d}V}{\mathrm{d}t} = -\bar g_{\mathrm{Na}}m^3h\,(V - E_{\mathrm{Na}}) - \bar g_{\mathrm{K}}n^4(V - E_{\mathrm{K}}) - g_{\mathrm{L}}(V - E_{\mathrm{L}}) + I_{\mathrm{app}}, \tag{30.12}
$$
where each gating variable $x \in \{m, h, n\}$ obeys first-order kinetics
$$
\frac{\mathrm{d}x}{\mathrm{d}t} = \alpha_x(V)(1 - x) - \beta_x(V)x = \frac{x_\infty(V) - x}{\tau_x(V)}, \qquad x_\infty = \frac{\alpha_x}{\alpha_x + \beta_x}, \quad \tau_x = \frac{1}{\alpha_x + \beta_x}, \tag{30.13}
$$
with voltage-dependent rate constants fitted to voltage-clamp data. For the squid axon at $6.3\,{}^\circ\mathrm{C}$ in the modern convention (rest at $-65\,\mathrm{mV}$; $V$ in mV, rates in $\mathrm{ms^{-1}}$): $\alpha_m = 0.1(V + 40)/[1 - \mathrm{e}^{-(V + 40)/10}]$, $\beta_m = 4\mathrm{e}^{-(V + 65)/18}$, $\alpha_h = 0.07\mathrm{e}^{-(V + 65)/20}$, $\beta_h = 1/[1 + \mathrm{e}^{-(V + 35)/10}]$, $\alpha_n = 0.01(V + 55)/[1 - \mathrm{e}^{-(V + 55)/10}]$, $\beta_n = 0.125\mathrm{e}^{-(V + 65)/80}$; $\bar g_{\mathrm{Na}} = 120$, $\bar g_{\mathrm{K}} = 36$, $g_{\mathrm{L}} = 0.3\,\mathrm{mS\,cm^{-2}}$, $E_{\mathrm{Na}} = 50$, $E_{\mathrm{K}} = -77$, $E_{\mathrm{L}} = -54.4\,\mathrm{mV}$, $C = 1\,\mu\mathrm{F\,cm^{-2}}$.

The exponents were chosen to fit the shapes of the conductance curves: a single first-order variable would rise exponentially, without the observed delay, while $n^4$ rises as $(1 - \mathrm{e}^{-t/\tau_n})^4$, sigmoidally. Hodgkin and Huxley interpreted each variable as the probability that one of several independent gating particles is in its permissive position, four for the $\ce{K+}$ conductance, three activating particles and one inactivating particle for $\ce{Na+}$. Forty years later the four independent voltage sensors of $\mathrm{K_V}$ channels and the three activating sensors plus sensor-IV-coupled inactivation of $\mathrm{Na_V}$ channels (30.3.1) gave these particles a structural meaning, a remarkable confirmation of a phenomenological model. The rate constants have the exponential voltage dependence expected for transitions over barriers in a field, which is how Hodgkin and Huxley motivated their form (they had considered, and rejected, a model of charged carriers crossing the membrane).

### 30.6.3. Simulating the Action Potential

**Algorithm 30.6.1 (Integration of the Hodgkin–Huxley Equations)** Represent the state as $(V, m, h, n)$ and integrate Eqs. (30.12)–(30.13) with a fourth-order Runge–Kutta method and a step of $0.01$–$0.02\,\mathrm{ms}$, starting from rest with each gate at $x_\infty(-65\,\mathrm{mV})$. For a voltage-clamp simulation hold $V$ fixed: each gate then relaxes exponentially to $x_\infty(V)$ with time constant $\tau_x(V)$, and the conductances follow in closed form. For propagation along an axon, discretize $x$ and add the axial term $(a/2R_{\mathrm{i}})\partial_x^2V$ (30.6.4).

The simulations reproduce the phenomena: an all-or-none spike above a threshold of a few millivolts of depolarization; an overshoot to about $+40\,\mathrm{mV}$, short of $E_{\mathrm{Na}}$ because $g_{\mathrm{K}}$ has started to rise and $g_{\mathrm{Na}}$ to inactivate; an afterhyperpolarization toward $E_{\mathrm{K}}$ while $n$ is still high; an absolute refractory period of about $2\,\mathrm{ms}$, during which $h$ is too small for any stimulus to elicit a spike, followed by a relative refractory period; and, for a steady current above about $6\,\mu\mathrm{A\,cm^{-2}}$, repetitive firing that starts abruptly at a nonzero frequency. The last property, the onset of oscillation through a **Hopf bifurcation** ([2.4.11](/2.4.11)), classifies the squid axon as a "type II" excitable system; the reduction of the four-dimensional model to two-dimensional phase-plane models is in [7.16](/7.16).

![The Hodgkin–Huxley model (Definition 30.6.2, Algorithm 30.6.1). A: steady states (solid) and time constants (dashed) of m, h and n against V. B: simulated voltage clamp, steps from −65 mV: g_Na (solid) rises and inactivates, g_K (dashed) rises with a sigmoidal delay. C: responses to 0.5 ms current pulses: two subthreshold pulses decay, a suprathreshold one triggers the all-or-none spike. D: gates and ionic currents during the spike: m follows V within a fraction of a millisecond, h and n lag and terminate the spike. E: firing rate for steady currents: firing begins abruptly at about 60 Hz above threshold](./plots/hh-model.py)

**Example 30.6.1 (The cost of a spike)** The minimum charge that must enter to depolarize a membrane by $100\,\mathrm{mV}$ is $c_{\mathrm{m}}\Delta V = 10^{-3}\,\mathrm{C\,m^{-2}}$, $6.2\times10^{15}$ $\ce{Na+}$ per square meter, about 6000 per square micrometer. In the squid axon at low temperature the $\ce{Na+}$ and $\ce{K+}$ currents overlap strongly and about four times this minimum enters; in mammalian unmyelinated axons and in many cortical axons the overlap is small and the excess is only 30 % (Alle, Roth and Geiger 2009; Carter and Bean 2009). Each $\ce{Na+}$ is pumped out at the cost of one third of an ATP. For a cortical axon of $0.5\,\mu\mathrm{m}$ diameter and $4\,\mathrm{cm}$ of total length, the area is $6\times10^{-8}\,\mathrm{m^2}$, and one spike costs $1.3 \times 6.2\times10^{15} \times 6\times10^{-8}/3 \approx 1.6\times10^8$ ATP. With billions of neurons firing a few times per second, signaling consumes a large part of the brain's energy, which in humans is about 20 % of the body's resting metabolism.

### 30.6.4. Propagation

Coupling Eqs. (30.12)–(30.13) to the cable gives the propagated action potential,
$$
\frac{a}{2R_{\mathrm{i}}}\frac{\partial^2V}{\partial x^2} = C\frac{\partial V}{\partial t} + I_{\mathrm{ion}}(V, m, h, n). \tag{30.14}
$$
Hodgkin and Huxley solved for a traveling wave on a mechanical calculator: assuming a constant speed $\theta$, $V(x, t) = V(t - x/\theta)$ turns Eq. (30.14) into an ordinary differential equation with $\partial_x^2V = \theta^{-2}\partial_t^2V$, and only one value of $\theta$ gives a solution that returns to rest. They found $18.8\,\mathrm{m\,s^{-1}}$ at $18.5\,{}^\circ\mathrm{C}$, against $21.2\,\mathrm{m\,s^{-1}}$ measured. The inactivation of $\ce{Na+}$ channels behind the pulse makes it refractory, so a spike initiated in the middle of an axon travels in both directions but never turns back, and two spikes colliding annihilate.

![Propagation in the Hodgkin–Huxley cable (Eq. 30.14, R_i = 35.4 Ω cm, 6.3 °C). A: membrane potential in space and time in the squid giant axon after a stimulus at one end: a pulse travels at constant speed (12 m/s at this temperature). B: snapshots of V(x): the refractory tail behind the spike. C: conduction velocity from simulations of axons of different diameters follows v ∝ √d (Proposition 30.5.1); the dashed line is the empirical velocity of myelinated mammalian fibers, about 6 m/s per µm of outer diameter, proportional to d (30.7)](./plots/hh-propagation.py)

## 30.7. Myelin and Saltatory Conduction

An unmyelinated axon conducts at $v \propto \sqrt d$; to reach $25\,\mathrm{m\,s^{-1}}$ the squid needs an axon half a millimeter thick, and a human with thousands of such fast fibers would need a spinal cord meters across. Vertebrates solved the problem with myelin: Schwann cells (in peripheral nerves) and oligodendrocytes (in the central nervous system) wrap tens to a hundred layers of their membrane around the axon, leaving gaps about $1\,\mu\mathrm{m}$ wide, the nodes of Ranvier, every $0.2$–$2\,\mathrm{mm}$ (about 100 times the fiber diameter).

**Definition 30.7.1 (Saltatory Conduction)** **Saltatory conduction** is the propagation of an action potential along a myelinated axon in which voltage-gated $\ce{Na+}$ channels are concentrated at the nodes of Ranvier and the insulated internodes conduct passively, so that excitation jumps from node to node.

Myelin with $N$ wraps adds $2N$ membranes in series: it multiplies the specific resistance of the internodal membrane by about $2N$ and divides its capacitance by the same factor. The length constant of the internode grows by $\sqrt{2N}$, so the current from one active node depolarizes the next one above threshold, and the charge needed to depolarize an internode falls by $2N$, which saves energy and time. The time a node needs to reach threshold, about $20$–$50\,\mu\mathrm{s}$, does not depend on the diameter, while the internodal distance grows in proportion to it; hence the velocity of myelinated fibers is proportional to the diameter, about $6\,\mathrm{m\,s^{-1}}$ per micrometer of outer diameter (Hursh, 1939). Since unmyelinated conduction grows only as $\sqrt d$, myelin pays above a crossover diameter of about $1\,\mu\mathrm{m}$ (Rushton, 1951), roughly the diameter below which axons in mammals are unmyelinated. Rushton also showed that the velocity at given outer diameter is maximal for a ratio of axon to fiber diameter (g-ratio) of about $0.6$, close to the measured values of $0.6$–$0.7$. Demyelinating diseases such as multiple sclerosis slow or block conduction because the exposed internodal membrane has too few $\ce{Na+}$ channels to regenerate the spike and its higher capacitance shunts the current from the nodes.

## 30.8. Electric Organs

Several groups of fish generate electric discharges with organs made of electrocytes, modified muscle (in most species) or nerve cells. An electrocyte is a flat cell, innervated on one face only. At rest both faces have the resting potential and their potentials cancel along the axis of the cell; when the innervated face fires an action potential (or, in some species, both faces fire in sequence), the potential across the cell becomes the difference between the action potential on one face and the resting potential on the other, about $0.15\,\mathrm{V}$. Thousands of electrocytes stacked in columns act as batteries in series, and many columns act in parallel.

**Definition 30.8.1 (Electric Organ)** An **electric organ** is an organ of electrocytes arranged in series and parallel whose synchronous, asymmetric excitation adds their transcellular potentials and drives current through the surrounding water, for communication and electrolocation (weak discharges) or for predation and defense (strong discharges).

The arrangement is an impedance-matching problem. Let $N_{\mathrm{tot}}$ electrocytes, each of emf $\varepsilon$ and internal resistance $r$, be arranged as $N$ in series and $M = N_{\mathrm{tot}}/N$ columns in parallel, discharging into a load $R_L$ (the water and the prey). The organ has emf $N\varepsilon$ and internal resistance $Nr/M = N^2r/N_{\mathrm{tot}}$, and the power delivered is
$$
P = \frac{(N\varepsilon)^2R_L}{(R_L + N^2r/N_{\mathrm{tot}})^2},
$$
maximal when the internal resistance equals the load, at $N^* = \sqrt{N_{\mathrm{tot}}R_L/r}$, where $P_{\max} = N_{\mathrm{tot}}\varepsilon^2/(4r)$ is independent of the load. Fresh water is a poor conductor, and the electric eel *Electrophorus* has about 6000 electrocytes in series in each of its main organs and produces up to $600\,\mathrm{V}$ ($860\,\mathrm{V}$ in *Electrophorus voltai*, de Santana and colleagues 2019); sea water conducts well, and the marine electric rays *Torpedo* have short columns of a few hundred electrocytes, many in parallel, producing $50$–$60\,\mathrm{V}$ (up to about $200\,\mathrm{V}$ in the largest species) at currents of tens of amperes. The African electric catfish *Malapterurus* reaches about $350\,\mathrm{V}$. The electrocytes of *Torpedo*, densely packed with nicotinic acetylcholine receptors, were the source from which these receptors were first purified.

![Electric organs. A: a column of electrocytes innervated on their posterior faces; when the innervated faces fire, each cell contributes about 0.15 V and the cells in series add. B: power delivered to the load by 2 × 10⁵ electrocytes (emf 0.15 V, internal resistance 5 Ω each, illustrative) against the number in series, for fresh water (1 kΩ) and sea water (2 Ω): the optimum N* = (N_tot R_L/r)^(1/2) is thousands of cells in series in fresh water (eels) and a few hundred in sea water (rays), at the same maximal power](./plots/electric-organ.py)

## 30.9. The Electrocardiogram as a Dipole Field

The heart is a syncytium of excitable cells through which a wave of depolarization spreads from the sinoatrial node through the atria, is delayed in the atrioventricular node, and spreads rapidly through the ventricles via the His–Purkinje system. At each instant the boundary between depolarized and resting tissue carries a layer of current sources and sinks; seen from a distance large compared with the heart, it is a current dipole $\boldsymbol{p}(t)$ (units $\mathrm{A\,m}$) in a volume conductor.

**Proposition 30.9.1 (Potential of a Current Dipole)** In an infinite homogeneous conductor of conductivity $\sigma$, a current dipole $\boldsymbol{p}$ at the origin produces the potential
$$
\varphi(\boldsymbol{r}) = \frac{\boldsymbol{p}\cdot\boldsymbol{r}}{4\pi\sigma r^3}. \tag{30.15}
$$
A lead measuring the potential difference between two electrodes far from the source therefore records $\boldsymbol{p}(t)\cdot\boldsymbol{l}$, the projection of the dipole on a lead vector $\boldsymbol{l}$ fixed by the electrode positions and the geometry of the body.

**Proof** In a conductor with current source density $s$, current conservation and Ohm's law $\boldsymbol{j} = -\sigma\nabla\varphi$ give Poisson's equation $\sigma\nabla^2\varphi = -s$, solved by $\varphi = \int s(\boldsymbol{r}')/(4\pi\sigma\lvert\boldsymbol{r} - \boldsymbol{r}'\rvert)\,\mathrm{d}V'$. For a source $+I$ at $\boldsymbol{d}/2$ and a sink $-I$ at $-\boldsymbol{d}/2$, expanding to first order in $d/r$ gives Eq. (30.15) with $\boldsymbol{p} = I\boldsymbol{d}$, the same algebra as for an **electric dipole moment** in electrostatics ([5.3.1](/5.3.1)). The potential is linear in $\boldsymbol{p}$, so any lead records a fixed linear combination of its components. $\square$

Einthoven (1903–1912) placed electrodes on the right arm, left arm and left leg, at roughly the corners of an equilateral triangle in the frontal plane with the heart at its center. Lead I (left arm minus right arm) projects the dipole on the horizontal axis, lead II (left leg minus right arm) on the axis $60^\circ$ below it, lead III (left leg minus left arm) on the axis at $120^\circ$; since the three potential differences around a loop sum to zero, $\mathrm{II} = \mathrm{I} + \mathrm{III}$ at every instant (Einthoven's law). The sequence of the normal electrocardiogram follows the excitation: the P wave (atrial depolarization, under $0.12\,\mathrm{s}$), the PR interval ($0.12$–$0.20\,\mathrm{s}$, mostly atrioventricular delay), the QRS complex (ventricular depolarization, under $0.12\,\mathrm{s}$, large because of the ventricular mass), and the T wave of ventricular repolarization, upright in most leads although repolarization is the reverse of depolarization, because the ventricle repolarizes from outside to inside. The mean QRS axis, normally between $-30^\circ$ and $+90^\circ$, gives the orientation of the heart and of ventricular hypertrophy. The QT interval shortens with heart rate and is corrected, for example as $\mathrm{QT_c} = \mathrm{QT}/\sqrt{\mathrm{RR}}$ (Bazett, RR in seconds), with upper normal values of about $0.44$–$0.46\,\mathrm{s}$; a resting sinus rate above $100$ per minute is tachycardia. The physiology of the heart is the subject of [7.14](/7.14).

![The electrocardiogram as a projection of the cardiac dipole (Proposition 30.9.1; synthetic dipole, one beat at 75 per minute). A: the loop traced by the tip of the dipole in the frontal plane (P, QRS and T loops; mean QRS axis about +60°) and the axes of limb leads I, II and III (downward positive, as in the hexaxial system). B: the lead signals are projections of the dipole; the dotted curve I + III coincides with II (Einthoven's law)](./plots/ecg-dipole.py)

## Summary

| Topic | Key results | Where |
|---|---|---|
| Charge state | $c_{\mathrm{m}} \approx 1\,\mu\mathrm{F\,cm^{-2}}$; 4400 ions per $\mu\mathrm{m^2}$ for $70\,\mathrm{mV}$, $3\times10^{-5}$ of cellular $\ce{K+}$; field $2\times10^7\,\mathrm{V\,m^{-1}}$ | 30.1.1, Example 30.1.1 |
| Equilibrium | Nernst $E = (k_{\mathrm{B}}T/ze)\ln(c_{\mathrm{out}}/c_{\mathrm{in}})$, $26.7\,\mathrm{mV}$ at $37\,{}^\circ\mathrm{C}$; Donnan equilibrium would swell the cell | Eq. (30.1), 30.1.2 |
| Pump | 3 Na⁺ out, 2 K⁺ in: $18\,k_{\mathrm{B}}T$ of $19$–$23\,k_{\mathrm{B}}T$ from ATP | Example 30.1.2 |
| Electrodiffusion | Nernst–Planck $\boldsymbol{J} = -D(\nabla c + zec\nabla\varphi/k_{\mathrm{B}}T)$; constant field → GHK current and voltage equations; Goldman rectification | Definition 30.2.1, Theorem 30.2.1, Eqs. (30.3)–(30.5) |
| Single channels | Gigaseal noise $\sqrt{4k_{\mathrm{B}}TB/R}$; $i = \gamma(V - E)$, $1\,\mathrm{pA} = 6.2\times10^6\,e\,\mathrm{s^{-1}}$; diffusion limit $2\pi Dac$ | 30.2.3 |
| Barrier models | One-site pore: saturation, rectification by asymmetry; multi-ion pores | Formula 30.2.1 |
| Selectivity | TVGYG filter, four sites of eight carbonyl oxygens, two ions with knock-on; EEEE in $\mathrm{Ca_V}$, DEKA in $\mathrm{Na_V}$ | Definition 30.2.2, 30.2.5 |
| Voltage gating | S4 arginines, charge transfer center, four sensors; $\mathrm{Na_V}$ IFM inactivation; gating currents, Q–V left of G–V; limiting slope | Definitions 30.3.1–30.3.2 |
| Kinetics | Dwell times = sums of exponentials, one per state (Eq. 30.6); Gillespie simulation | Theorem 30.3.1 |
| Block | Woodhull $K(V) = K(0)\mathrm{e}^{z\delta eV/k_{\mathrm{B}}T}$; NMDA $\ce{Mg^2+}$ block → coincidence detection | Formula 30.3.2 |
| Circuit | $C\dot V = -\sum g_j(V - E_j) + I$; $\tau_{\mathrm{m}} = R_{\mathrm{m}}c_{\mathrm{m}}$; bistability with gated Na⁺ | Eqs. (30.8)–(30.9), Proposition 30.4.1 |
| Cable | $\lambda^2V'' = \tau\dot V + V$, $\lambda = \sqrt{aR_{\mathrm{m}}/2R_{\mathrm{i}}}$; fronts $v = (\lambda/\tau)\sqrt{k/2}(1 - 2\alpha)$, $v \propto \sqrt d$ | Theorem 30.5.1, Proposition 30.5.1 |
| Hodgkin–Huxley | $m^3h$, $n^4$ gates; voltage clamp; threshold, refractoriness, Hopf onset of firing; $18.8$ vs $21.2\,\mathrm{m\,s^{-1}}$; cost $\sim 10^8$ ATP per cortical spike | Definitions 30.6.1–30.6.2, Algorithm 30.6.1, Example 30.6.1 |
| Myelin | $R_{\mathrm{m}}\times2N$, $c_{\mathrm{m}}/2N$; $v \approx 6\,\mathrm{m\,s^{-1}}$ per $\mu\mathrm{m}$, ∝ d; crossover $\sim 1\,\mu\mathrm{m}$; g-ratio $0.6$ | Definition 30.7.1 |
| Organs | Electric organs: impedance matching $N^* = \sqrt{N_{\mathrm{tot}}R_L/r}$; ECG = projection of a current dipole, Einthoven II = I + III | Definition 30.8.1, Proposition 30.9.1 |

## Questions

1. Show that a cell needs to separate only a tiny fraction of its ions to set up its membrane potential, using a spherical neuron of radius $10\,\mu\mathrm{m}$ at $-70\,\mathrm{mV}$ with $[\ce{K+}]_{\mathrm{in}} = 140\,\mathrm{mM}$. What would be the potential if the cell lost $1\,\%$ of its $\ce{K+}$ without any compensating ion movement?

   **Answer** Charge $Q = c_{\mathrm{m}}AV = 10^{-2}\times4\pi(10^{-5})^2\times0.07 = 8.8\times10^{-13}\,\mathrm{C}$, $5.5\times10^6$ ions. The cell contains $0.14 \times 4.19\times10^{-12}\,\mathrm{L} \times 6.02\times10^{23} = 3.5\times10^{11}$ $\ce{K+}$, so the fraction is $1.6\times10^{-5}$. Losing $1\,\%$ ($3.5\times10^9$ ions, $5.6\times10^{-10}\,\mathrm{C}$) uncompensated would change the potential by $Q/C = 5.6\times10^{-10}/1.26\times10^{-11}\,\mathrm{F} \approx 45\,\mathrm{V}$, which is impossible: long before, the field would drive other ions to compensate. Electroneutrality holds in bulk to about one part in $10^5$.

2. Derive the Nernst equation from the Nernst–Planck equation, and compute the Nernst potentials of $\ce{K+}$, $\ce{Na+}$, $\ce{Ca^2+}$ and $\ce{Cl-}$ for the table at $37\,{}^\circ\mathrm{C}$.

   **Answer** $J = 0$ gives $\mathrm{d}\ln c/\mathrm{d}x = -(ze/k_{\mathrm{B}}T)\mathrm{d}\varphi/\mathrm{d}x$; integrating across the membrane, $\varphi_{\mathrm{in}} - \varphi_{\mathrm{out}} = (k_{\mathrm{B}}T/ze)\ln(c_{\mathrm{out}}/c_{\mathrm{in}})$. With $k_{\mathrm{B}}T/e = 26.7\,\mathrm{mV}$: $E_{\mathrm{K}} = 26.7\ln(4/155) = -98\,\mathrm{mV}$, $E_{\mathrm{Na}} = 26.7\ln(145/12) = +67\,\mathrm{mV}$, $E_{\mathrm{Ca}} = 13.35\ln(1.5/10^{-4}) = +128\,\mathrm{mV}$, $E_{\mathrm{Cl}} = -26.7\ln(120/4) = -91\,\mathrm{mV}$.

3. Using the GHK voltage equation with $P_{\mathrm{K}}:P_{\mathrm{Na}}:P_{\mathrm{Cl}} = 1:0.04:0.45$ and squid-axon concentrations (inside $\ce{K+}$ 400, $\ce{Na+}$ 50, $\ce{Cl-}$ 40 mM; outside 20, 440, 560 mM; $k_{\mathrm{B}}T/e = 25.2\,\mathrm{mV}$ at $20\,{}^\circ\mathrm{C}$), compute the resting potential, and the peak potential if $P_{\mathrm{Na}}$ rises to 20.

   **Answer** Rest: numerator $20 + 0.04\times440 + 0.45\times40 = 55.6$, denominator $400 + 0.04\times50 + 0.45\times560 = 654$; $V = 25.2\ln(55.6/654) = -62\,\mathrm{mV}$. Peak: numerator $20 + 8800 + 18 = 8838$, denominator $400 + 1000 + 252 = 1652$; $V = 25.2\ln(5.35) = +42\,\mathrm{mV}$, close to the observed overshoot.

4. A $\ce{K+}$ channel has a conductance of $20\,\mathrm{pS}$. How many ions pass per millisecond of opening at $-40\,\mathrm{mV}$ with $E_{\mathrm{K}} = -90\,\mathrm{mV}$? How does this compare with the turnover of the Na⁺/K⁺ pump, about 100 cycles per second?

   **Answer** $i = 20\,\mathrm{pS}\times50\,\mathrm{mV} = 1\,\mathrm{pA}$, $6.2\times10^6$ ions per second, 6200 per millisecond. A pump moves 200 $\ce{K+}$ per second: one channel opening for a millisecond undoes 30 s of pumping by one pump. Channels are 4–5 orders of magnitude faster than carriers because they need no conformational change per ion.

5. Why does the K⁺ channel exclude Na⁺, which is smaller? Design an experiment that would test whether two ions occupy the filter simultaneously.

   **Answer** In the filter the ions are dehydrated and coordinated by eight carbonyl oxygens held at the geometry of a hydrated $\ce{K+}$; $\ce{Na+}$ is too small to be contacted by all of them, so it gains less energy from the protein than it loses by dehydration (about $70\,\mathrm{kJ\,mol^{-1}}$ more for $\ce{Na+}$ than for $\ce{K+}$), and its transfer is unfavorable. Tests of multi-occupancy: measure the unidirectional flux ratio with radioactive tracers (Ussing's ratio exponent $n' > 1$ indicates single-file movement of several ions, Hodgkin and Keynes found about 2.5); look for the anomalous mole-fraction effect in $\ce{K+}/\ce{Tl+}$ mixtures; determine ion positions crystallographically with anomalous scatterers ($\ce{Tl+}$, $\ce{Rb+}$) at different concentrations.

6. A channel has a Boltzmann G–V curve with an apparent charge of $4\,e$, but gating-current measurements give $13\,e$ per channel. Explain the discrepancy with a model, and state how to measure the true charge from ionic currents alone.

   **Answer** If four independent sensors must all move before the pore opens, the open probability is $n^4$ with $n$ a Boltzmann function of charge $3.25\,e$; $n^4$ looks like a Boltzmann function of lower apparent charge over the range where $p_{\mathrm{o}}$ is appreciable, because most charge moves among closed states. At very negative potentials, however, $p_{\mathrm{o}} \approx \exp(4 \times 3.25\,eV/k_{\mathrm{B}}T)$ up to a constant: the limiting slope of $\ln p_{\mathrm{o}}$ against $V$ gives the total charge, which requires measuring very small open probabilities, for example by single-channel recording in patches with many channels.

7. For the scheme C1 ⇌ C2 ⇌ O with the rates of the figure, compute the open-time constant, the two closed-time constants, and the mean number of openings per burst.

   **Answer** Open: $1/k_{\mathrm{O}\to\mathrm{C2}} = 2\,\mathrm{ms}$. Closed: eigenvalues of $Q_{\mathcal{CC}} = \begin{bmatrix}-0.2 & 0.2\\ 1.0 & -3.0\end{bmatrix}$: $\lambda^2 + 3.2\lambda + 0.4 = 0$, $\lambda = -0.130$ and $-3.07\,\mathrm{ms^{-1}}$, time constants $7.7\,\mathrm{ms}$ and $0.33\,\mathrm{ms}$. From C2 the channel opens with probability $2/3$ and goes to C1 (ending a burst) with probability $1/3$, so the number of openings per burst is geometric with mean $1/(1/3) = 3$.

8. The squid giant axon has $R_{\mathrm{m}} = 1\,\mathrm{k\Omega\,cm^2}$, $c_{\mathrm{m}} = 1\,\mu\mathrm{F\,cm^{-2}}$, $R_{\mathrm{i}} = 30\,\Omega\,\mathrm{cm}$ and radius $250\,\mu\mathrm{m}$. Compute $\tau_{\mathrm{m}}$, $\lambda$, and the scale $\lambda/\tau_{\mathrm{m}}$ of conduction velocity. How does $\lambda/\tau_{\mathrm{m}}$ change for a $1\,\mu\mathrm{m}$ axon with the same membrane?

   **Answer** $\tau_{\mathrm{m}} = 10^3 \times 10^{-6} = 1\,\mathrm{ms}$. $\lambda = \sqrt{aR_{\mathrm{m}}/2R_{\mathrm{i}}} = \sqrt{0.025\times1000/60}\,\mathrm{cm} = 0.65\,\mathrm{cm}$. $\lambda/\tau_{\mathrm{m}} = 6.5\,\mathrm{m\,s^{-1}}$, of the order of the measured $21\,\mathrm{m\,s^{-1}}$ (the dimensionless factor is about 3 because during the upstroke the active membrane conductance is much larger than at rest). For $a = 0.5\,\mu\mathrm{m}$ (diameter 1), $\lambda$ falls by $\sqrt{500} = 22$, giving $0.29\,\mathrm{m\,s^{-1}}$ for the scale, consistent with the $\sim 1\,\mathrm{m\,s^{-1}}$ of thin unmyelinated C fibers at body temperature.

9. Verify Proposition 30.5.1 numerically: simulate $\partial_tu = \partial_x^2u + u(1 - u)(u - \alpha)$ for $\alpha = 0.2$ and compare the front speed with the prediction.

   **Answer** Prediction with $k = 1$, $\lambda = \tau = 1$: $v = (1/\sqrt2)(1 - 0.4) = 0.424$. A finite-difference simulation (grid $\Delta x = 0.2$, $\Delta t = 0.01$, initial step $u = 1$ for $x < 10$) gives a front whose position grows linearly; fitting from $t = 20$ to $t = 100$ gives $v \approx 0.42$, within discretization error:

   ```python
   import numpy as np
   dx, dt, a = 0.2, 0.01, 0.2
   x = np.arange(0, 200, dx); u = (x < 10).astype(float)
   pos = []
   for step in range(10001):
       lap = np.roll(u, 1) - 2 * u + np.roll(u, -1); lap[0] = lap[-1] = 0
       u = u + dt * (lap / dx**2 + u * (1 - u) * (u - a))
       if step % 1000 == 0: pos.append(x[np.argmin(np.abs(u - 0.5))])
   print(np.polyfit(np.arange(len(pos))[2:] * 10.0, pos[2:], 1)[0])   # about 0.42
   ```

10. Estimate the conduction time from toe to spinal cord ($1\,\mathrm{m}$) for an unmyelinated C fiber ($1\,\mathrm{m\,s^{-1}}$) and a myelinated $\mathrm{A\alpha}$ fiber of $15\,\mu\mathrm{m}$. What diameter would an unmyelinated axon need to match the myelinated one, if $v = 1\,\mathrm{m\,s^{-1}}$ at $1\,\mu\mathrm{m}$ and $v \propto \sqrt d$?

    **Answer** C fiber: $1\,\mathrm{s}$. $\mathrm{A\alpha}$: $v \approx 6 \times 15 = 90\,\mathrm{m\,s^{-1}}$, $11\,\mathrm{ms}$. An unmyelinated axon needs $\sqrt{d/1\,\mu\mathrm{m}} = 90$, $d = 8100\,\mu\mathrm{m} \approx 8\,\mathrm{mm}$; myelin saves a factor of 500 in diameter, $2.5\times10^5$ in cross-sectional area.

11. An electric eel delivers $500\,\mathrm{V}$ into a fish of resistance $1\,\mathrm{k\Omega}$ for $2\,\mathrm{ms}$. What energy is delivered, and how many ATP molecules must be hydrolyzed at minimum to restore the gradients (take $-\Delta G_{\mathrm{ATP}} = 9\times10^{-20}\,\mathrm{J}$)? Why do eels discharge in short pulses?

    **Answer** Power $V^2/R = 250\,\mathrm{W}$, energy $0.5\,\mathrm{J}$ per pulse; at least $0.5/(9\times10^{-20}) \approx 6\times10^{18}$ ATP, about $10\,\mu\mathrm{mol}$, and several times more given the internal losses (at impedance matching half the energy is dissipated in the organ). Pulses of a few milliseconds, repeated at a few hundred hertz, suffice to excite the prey's motor neurons and muscles (the eel's discharge acts like a remote taser) while limiting the energy spent and the run-down of the electrocytes' gradients.

12. The mean QRS vector of a patient points at $-60^\circ$ in the frontal plane. What are the signs of the QRS complex in leads I, II and III, and what does this suggest?

    **Answer** Projections: lead I, $\cos(-60^\circ) = +0.5$ (positive); lead II, $\cos(-120^\circ) = -0.5$ (negative); lead III, $\cos(-180^\circ) = -1$ (strongly negative); check II = I + III: $-0.5 = 0.5 - 1$. An axis more negative than $-30^\circ$ is left axis deviation, seen for example in a block of the left anterior fascicle or in left ventricular hypertrophy.
