---
title: Organic Reactions Driven by Light, Electricity and Mechanical Force
description: Heat, light, electricity and mechanical force as energy inputs and their energy scales; generation and decay of excited states (Franck–Condon principle, El-Sayed's rule, triplet sensitization and Dexter energy transfer); photochemical E/Z isomerization of alkenes and the photostationary state, azobenzene photoswitches, [2+2] photocycloaddition of enones and alkenes; Norrish type I and II reactions of carbonyls, Norrish–Yang cyclization, photoenolization and the Paternò–Büchi reaction; excited-state redox potentials and the Rehm–Weller equation, oxidative and reductive quenching cycles of photoredox catalysis, quenching experiments and mechanistic diagnosis; photocages and photoaffinity labeling; organic electrochemistry (electrode processes, direct and indirect electrolysis, Kolbe electrolysis, adiponitrile electrosynthesis and mediator-catalyzed amidyl radical cyclization); mechanochemistry (ball milling, ultrasound and mechanophores).
source_hash: 93321bea512f
---

Almost all the reactions in the preceding chapters are driven by heating: thermal motion promotes a fraction of the molecules over the barrier according to the **Boltzmann distribution**, and the reaction proceeds on the ground-state **potential energy surface**. This chapter treats three other ways of supplying energy. Light promotes a molecule to an electronically excited state, whose electronic structure and hence reactivity differ from those of the ground state: it abstracts hydrogen atoms and adds to double bonds like a radical, it is a stronger oxidant and a stronger reductant, and it can hand its energy to other molecules. An electrode supplies or removes electrons directly, so that the electrode potential replaces oxidants and reductants. Mechanical force stretches particular bonds along a chosen direction and thereby tilts the potential energy surface.

The emphasis is on organic reactions. The photophysics of excited states was treated in [6.3.17](/6.3.17#sec-17.2.4) (**Jablonski diagram**, **quantum yield**, **quenching**, **photosensitization**) and [6.4.10](/6.4.10) (**fluorescence**), and only the parts relevant to reactivity are recalled here. The photochemical selection rules for **pericyclic reactions** are in [6.5.12](/6.5.12#sec-12.3.4), and **single electron transfer** and the elementary steps of radical reactions are in [6.5.7](/6.5.7#sec-7.2.3). The general principles of electrode processes, **overpotential** and **electrosynthesis** are in [6.3.13](/6.3.13) and [6.3.14](/6.3.14), and **cyclic voltammetry** is in [6.4.6](/6.4.6#sec-6.6.4). Photoswitches, photocages and photoaffinity labels are everyday tools of chemical biology ([6.6](/6.6)), and photoredox and methods of **electrochemistry** are increasingly common in the synthesis of pharmaceuticals.

## 31.1. Energy Inputs and Energy Scales

### 31.1.1. Four Ways of Supplying Energy

The **activation energy** $E_{\mathrm{a}}$ is the energy a molecule needs to go from its ordinary state to one from which reaction is easy. The **Arrhenius equation** $k = A\mathrm{e}^{-E_{\mathrm{a}}/RT}$ shows that raising the temperature increases exponentially the fraction of molecules with energy above $E_{\mathrm{a}}$, which is why heating is the most general way to supply energy. But thermal energy is indiscriminate: it raises the energy of all bonds and all reaction channels at once, and selectivity can come only from differences in barrier heights. The other energy inputs deliver energy to a specific place:

| Energy input | Main effect | Reaction types |
|---|---|---|
| Heat | Changes the energy distribution of the molecules | Conventional (ground-state) reactions |
| Light | Generates electronically excited states, which react, transfer energy or transfer electrons | Photochemical reactions, energy-transfer catalysis, photoredox catalysis |
| Electricity | Generates redox species such as **radical ions** at an electrode | Reactions of **electrochemistry**, electrocatalysis |
| Mechanical force | Changes the forces on chemical bonds and tilts the **potential energy surface** | Mechanochemistry, ultrahigh-pressure chemistry |

The term "photocatalysis" is easily misunderstood. Light is not a catalyst (it is consumed, and is measured in photons); the catalyst is the molecule that absorbs light, takes part in the reaction and is regenerated at the end. The accurate description is a light-promoted catalytic reaction.

### 31.1.2. The Energy of a Photon

The energy of one mole of photons is

$$
E_{\mathrm{m}} = \frac{N_{\mathrm{A}}hc}{\lambda} = \frac{1.196\times10^{5}\,\mathrm{kJ\,mol^{-1}}}{\lambda/\mathrm{nm}}, \qquad E = \frac{1239.84\,\mathrm{eV}}{\lambda/\mathrm{nm}}\ (\text{single photon}).
$$

| Wavelength / nm | 200 | 300 | 400 | 450 | 500 | 600 | 700 | 800 |
|---|---|---|---|---|---|---|---|---|
| $E_{\mathrm{m}}$ / $\mathrm{kJ\,mol^{-1}}$ | 598 | 399 | 299 | 266 | 239 | 199 | 171 | 150 |
| $E_{\mathrm{m}}$ / $\mathrm{kcal\,mol^{-1}}$ | 143.0 | 95.3 | 71.5 | 63.5 | 57.2 | 47.7 | 40.8 | 35.7 |
| $E$ / eV | 6.20 | 4.13 | 3.10 | 2.76 | 2.48 | 2.07 | 1.77 | 1.55 |

(The literature still often uses $\mathrm{kcal\,mol^{-1}}$, with $1\,\mathrm{kcal} = 4.184\,\mathrm{kJ}$; $1\,\mathrm{eV}$ per molecule corresponds to $96.485\,\mathrm{kJ\,mol^{-1}}$.) Compare several energy scales: at room temperature $RT = 2.48\,\mathrm{kJ\,mol^{-1}}$; the activation energies of common reactions are about $50$–$120\,\mathrm{kJ\,mol^{-1}}$; covalent **bond dissociation energies** are about $200$–$450\,\mathrm{kJ\,mol^{-1}}$ ($\ce{Cl-Cl}$ 243, $\ce{C-C}$ about 350, $\ce{C-H}$ about 400–440). An ultraviolet or visible photon carries about as much energy as a chemical bond, two orders of magnitude more than thermal motion, so photoreactions can run at room temperature or below and can drive molecules to thermodynamically unfavorable products ([6.3.17](/6.3.17#sec-17.2.7)).

Photons in the ultraviolet–visible region ($200$–$800\,\mathrm{nm}$) excite valence electrons and constitute the range used in organic photochemistry; infrared photons excite only vibrations. Atmospheric $\ce{O2}$ ($100$–$200\,\mathrm{nm}$) and ozone ($200$–$280\,\mathrm{nm}$) absorb all of UVC and most of UVB, so the ultraviolet part of sunlight reaching the ground is mainly UVA ($315$–$400\,\mathrm{nm}$).

### 31.1.3. Experimental Conditions for Photochemical Reactions

Light sources: mercury lamps give line spectra (low-pressure lamps $254\,\mathrm{nm}$, medium-pressure lamps 313, 366 nm and others), xenon lamps give a continuum from $250$ to $800\,\mathrm{nm}$, and sunlight a continuum from about $290$ to $800\,\mathrm{nm}$. Laboratories now mostly use LEDs, which are monochromatic (full width at half maximum about $20$–$40\,\mathrm{nm}$), generate little heat and can be chosen to match the absorption of the catalyst (for example blue light at $450\,\mathrm{nm}$). Reaction vessels: quartz transmits light above $200\,\mathrm{nm}$, whereas borosilicate glass (Pyrex) transmits only above about $300\,\mathrm{nm}$ and can serve as a filter that blocks short-wavelength ultraviolet light that would destroy the products. According to the **Beer–Lambert law**, light penetrates only a thin layer of a solution of high **absorbance**, so irradiation becomes uneven on scale-up. Pumping the solution through narrow transparent tubing (flow photochemistry) gives every portion of the solution the same illumination and is the usual way to scale up photoreactions.

## 31.2. Generation and Decay of Excited States

### 31.2.1. Absorption and the Franck–Condon Principle

When an organic molecule absorbs an ultraviolet or visible photon, an electron is promoted from an occupied orbital (usually the **highest occupied molecular orbital** or an n orbital holding a lone pair on oxygen or nitrogen) to an empty orbital (usually π\*), giving an electronically excited state. In decreasing order of energy, the common transitions are $\sigma\to\sigma^*$, $\pi\to\pi^*$ and $\mathrm{n}\to\pi^*$; the last two lie in the near-ultraviolet and visible regions and are the main actors in organic photochemistry (**chromophores**, [6.4.9](/6.4.9#sec-9.2.1)).

The time scale determines the nature of absorption. Visible and ultraviolet light are electromagnetic waves with frequencies of order $10^{15}\,\mathrm{Hz}$, and the electron completes its transition within about one optical period ($\lambda/c$, about $1.7\times10^{-15}\,\mathrm{s}$ for $500\,\mathrm{nm}$ light). A $\ce{C-H}$ **stretching vibration** (about $3000\,\mathrm{cm^{-1}}$), in contrast, has a frequency $c\tilde\nu \approx 9\times10^{13}\,\mathrm{s^{-1}}$ and a period of about $1.1\times10^{-14}\,\mathrm{s}$. Electronic transitions are more than one order of magnitude faster than nuclear motion.

**Definition 31.2.1 (Franck–Condon Principle)** An electronic transition is much faster than nuclear motion, so the positions and velocities of the nuclei have no time to change during the transition. In a potential energy diagram the transition is therefore a vertical line (a vertical transition) that ends on the excited-state curve at the same internuclear distance as in the ground state, and the transition probability is largest to the excited-state vibrational level that overlaps best with the ground-state vibrational wavefunction.

The principle was proposed by Franck (1925) and given a quantum-mechanical formulation by Condon (1926, 1928). The equilibrium internuclear distance in the excited state is usually larger than in the ground state (the electron enters an **antibonding orbital**), so the vertical transition reaches higher vibrational levels of the excited state and the absorption band contains a series of vibrational levels. In solution this vibrational structure is further broadened by solvent interactions, which is why the ultraviolet–visible absorption in solution is a broad band rather than a line spectrum.

The intensity of a transition is governed by **selection rules**. Transitions that conserve the **spin multiplicity** are allowed, and those that change it ($\mathrm{S}_0\to\mathrm{T}_1$) are forbidden; transitions between orbitals with large spatial overlap are strong, and those with small overlap are weak. In a $\pi\to\pi^*$ transition both orbitals belong to the same π system, and the **molar absorption coefficient** $\varepsilon$ is about $10^3$–$10^5\,\mathrm{L\,mol^{-1}\,cm^{-1}}$. In an $\mathrm{n}\to\pi^*$ transition the n orbital lies in the molecular plane while π\* is perpendicular to it, the overlap is very small, and $\varepsilon$ is only about $10$–$100$. "Forbidden" means only that the probability is small and the band weak, not that the transition is impossible.

### 31.2.2. Decay of Excited States and Kasha's Rule

The physical processes after excitation are represented by the **Jablonski diagram** ([figure in 6.3.17](/6.3.17#sec-17.2.4)). The time scales relevant to reactions are:

| Process | Typical time |
|---|---|
| Absorption | about $10^{-15}\,\mathrm{s}$ |
| **Vibrational relaxation** | $10^{-13}$–$10^{-11}\,\mathrm{s}$ |
| **Internal conversion** ($\mathrm{S}_n\to\mathrm{S}_1$) | $10^{-13}$–$10^{-11}\,\mathrm{s}$ |
| **Intersystem crossing** ($\mathrm{S}_1\to\mathrm{T}_1$) | $10^{-11}$–$10^{-6}\,\mathrm{s}$ (depends on the molecule; see Definition 31.2.2) |
| **Fluorescence** (radiative lifetime of $\mathrm{S}_1$) | $10^{-10}$–$10^{-7}\,\mathrm{s}$ (nanoseconds for most organic molecules) |
| **Phosphorescence** ($\mathrm{T}_1$) | $10^{-4}\,\mathrm{s}$ to seconds |

Vibrational relaxation and $\mathrm{S}_n\to\mathrm{S}_1$ internal conversion are faster than any emission or bimolecular reaction. Whichever level is excited, emission and photochemical reaction therefore start almost always from the lowest vibrational level of the lowest excited **singlet state** $\mathrm{S}_1$ or the lowest **triplet state** $\mathrm{T}_1$. This is **Kasha's rule**, and it means that only the two states $\mathrm{S}_1$ and $\mathrm{T}_1$ matter in the discussion of photoreactions.

For the same electron configuration, the **triplet state** lies below the **singlet state**: two electrons with parallel spins avoid each other because of the Pauli principle and so repel each other less (**Hund's rule** in atoms). The singlet–triplet gap equals twice the exchange integral. In $\mathrm{n},\pi^*$ states the overlap of the n and π\* orbitals is small and the gap is only about $20$–$40\,\mathrm{kJ\,mol^{-1}}$, whereas in $\pi,\pi^*$ states the gap is larger, often above $100\,\mathrm{kJ\,mol^{-1}}$. Hence $E(\mathrm{S}_0) < E(\mathrm{T}_1) < E(\mathrm{S}_1)$: phosphorescence lies at longer wavelength than fluorescence, and fluorescence in turn lies at longer wavelength than absorption (the **Stokes shift**).

**Definition 31.2.2 (El-Sayed's Rule)** Intersystem crossing is fast between two states of different orbital character (for example $^1(\mathrm{n},\pi^*) \to {}^3(\pi,\pi^*)$) and slow between two states of the same orbital character (for example $^1(\pi,\pi^*) \to {}^3(\pi,\pi^*)$).

Flipping a spin requires **spin–orbit coupling** to supply angular momentum. When an electron moves from an n orbital (a p orbital in the molecular plane) to a perpendicular π orbital, the orbital angular momentum changes and the spin–orbit coupling matrix element is large; between orbitals of the same type the matrix element is close to zero. In aromatic ketones such as benzophenone, $^1(\mathrm{n},\pi^*)$ and $^3(\pi,\pi^*)$ are close in energy, intersystem crossing occurs at about $10^{11}\,\mathrm{s^{-1}}$, and the **quantum yield** approaches 1; $^1(\pi,\pi^*)$ states of arenes undergo slow intersystem crossing and therefore fluoresce strongly. Heavy atoms (Br, I, Ru, Ir) strongly enhance spin–orbit coupling, which is why metal-complex photocatalysts are converted almost completely to the triplet state.

### 31.2.3. Reaction Modes of Excited States

An excited state has two half-filled orbitals and is a highly reactive species. Three kinds of behavior underlie organic photochemical reactions:

1. **Radical** character: an $\mathrm{n},\pi^*$ state has an unpaired electron on oxygen and abstracts hydrogen atoms and adds to double bonds like an alkoxy radical (Section 31.4); in a $\pi,\pi^*$ state the π bond order drops to zero, so rotation about the double bond becomes possible (Section 31.3.1).
2. Redox character: the excited electron sits in a high-energy orbital and is easily given up (a stronger reductant), and a vacancy in a low-energy orbital readily accepts an electron (a stronger oxidant) (Section 31.5).
3. Energy transfer: the excited state hands its excitation energy to another molecule and returns to the ground state, that is, **photosensitization** (Section 31.2.4).

In addition, the orbital symmetry of an excited state differs from that of the ground state, and **pericyclic reactions** obey the opposite selection rules under irradiation ([6.5.12](/6.5.12#sec-12.3.4)).

### 31.2.4. Triplet Sensitization and Dexter Energy Transfer

Many substrates do not absorb at accessible wavelengths (most simple alkenes absorb only below $250\,\mathrm{nm}$), or intersystem crossing after direct excitation is too slow to give the **triplet state**. In such cases a **photosensitizer** can be added: it absorbs light, forms $\mathrm{T}_1$ by intersystem crossing and then passes the triplet energy on to the substrate,

$$
\ce{Sens(S0) ->[h\nu] Sens(S1) ->[ISC] Sens(T1)}, \qquad \ce{Sens(T1) + A(S0) -> Sens(S0) + A(T1)}.
$$
The second step conserves total spin (exchange of two triplet–**singlet** pairs) and is spin-allowed. Triplet–triplet energy transfer requires the triplet energy $E_{\mathrm{T}}$ of the sensitizer to exceed that of the substrate (generally by more than about $10\,\mathrm{kJ\,mol^{-1}}$ for the transfer to approach the diffusion-controlled limit). Common sensitizers:

| Sensitizer | $E_{\mathrm{T}}$ / $\mathrm{kJ\,mol^{-1}}$ |
|---|---|
| Acetophenone | 308 |
| Benzophenone | 287 |
| Thioxanthone | 265 |
| Anthraquinone | 260 |
| Butane-2,3-dione | 230 |

**Definition 31.2.3 (Dexter Energy Transfer)** Energy transfer in which the orbitals of an excited donor and a ground-state acceptor overlap directly, and the transfer is achieved by exchange of electrons (the excited electron of the donor enters the LUMO of the acceptor while an electron from the HOMO of the acceptor returns to the donor), is called **Dexter energy transfer** (electron-exchange mechanism). Its rate constant decays exponentially with the donor–acceptor distance $r$:

$$
k_{\mathrm{EnT}} = KJ\,\mathrm{e}^{-2r/L},
$$
where $J$ is the normalized overlap integral between the **emission spectrum** of the donor and the absorption spectrum of the acceptor, and $L$ is a length related to the size of the orbitals (of order $0.1\,\mathrm{nm}$).

Electron exchange requires only that the total spin of each electron pair be conserved, so triplet–triplet energy transfer is possible; but it requires orbital contact and is negligible beyond about $1\,\mathrm{nm}$. The other mechanism is **Förster resonance energy transfer** ([6.4.10](/6.4.10#sec-10.3.4)): the transition dipoles of donor and acceptor couple through space, the rate decays as $r^{-6}$, and the transfer is effective over $1$–$10\,\mathrm{nm}$, but both transitions must be allowed, so it is used only for singlet states.

![Rate constants of the two energy-transfer mechanisms as functions of the donor–acceptor distance: the Förster mechanism decays as r⁻⁶ (R₀ = 5 nm) and competes with donor decay over several nanometers; the Dexter mechanism decays as exp(−2r/L) (L = 0.1 nm) and is effective only at contact distance (within about 1 nm); the dashed line is the decay rate of a typical triplet, 10⁶ s⁻¹](./plots/energy-transfer-distance.py)

## 31.3. Photochemical Reactions of Alkenes

### 31.3.1. Photochemical E/Z Isomerization and the Photostationary State

**Definition 31.3.1 (Photoisomerization)** A reaction in which a molecule absorbs light, changes its configuration in the excited state and returns to the ground state as an isomer is called **photoisomerization**. The most common case is E/Z (cis–trans) isomerization of a double bond.

Rotation about the $\ce{C=C}$ bond of a ground-state alkene requires breaking the π bond; for simple alkenes the barrier is about $260\,\mathrm{kJ\,mol^{-1}}$ and the cis and trans isomers do not interconvert at room temperature. In a $\pi,\pi^*$ excited state, π and π\* each hold one electron and the π bond order is zero. The molecule twists spontaneously to the conformation in which the two p orbitals are perpendicular (**dihedral angle** about $90^\circ$), where the excited state has its energy minimum and the ground state is just at the top of the barrier. From this twisted geometry (often called the p state) the molecule returns to the ground state without radiation, with nearly equal probability of sliding to either side, and a mixture of E and Z isomers results.

![Potential energy curves of an alkene (stilbene as an example) along the C=C torsion angle (schematic): the ground state S₀ has minima at 0° (Z) and 180° (E) and a barrier at 90°; the π,π* excited states S₁ and T₁ have zero π bond order and minima near 90° (the twisted p state); decay from there to the ground state can give either isomer](./plots/alkene-twisting.py)

Both isomers absorb light, so under irradiation isomerization proceeds in both directions at once and a **photostationary state** is reached. Unlike the situation in [6.3.17](/6.3.17#sec-17.2.7), where the reverse reaction is thermal, here both the forward and reverse reactions are photoreactions. At the stationary state $I\varepsilon_E\Phi_{E\to Z}[E] = I\varepsilon_Z\Phi_{Z\to E}[Z]$, so that

$$
\left(\frac{[Z]}{[E]}\right)_{\mathrm{pss}} = \frac{\varepsilon_E\,\Phi_{E\to Z}}{\varepsilon_Z\,\Phi_{Z\to E}},
$$
where $\varepsilon$ is the **molar absorption coefficient** at the irradiation wavelength and $\Phi$ is the **quantum yield**. Although decay from the twisted geometry gives the two isomers with similar probabilities, the composition of the photostationary state is determined by absorption. (E)-Stilbene is planar and well conjugated and absorbs more strongly at long wavelengths than the twisted Z isomer. Irradiating at such a wavelength excites the E isomer continually and the Z isomer hardly at all, so the Z isomer gradually accumulates. In this way most of a thermodynamically stable E alkene can be converted to the Z isomer, which is one method for preparing Z alkenes.

Alkenes that do not absorb usable light can be isomerized by **triplet** sensitization. "Energy-transfer catalysis", developed in recent years, exploits the same difference: the Z isomers of styrenes deviate from coplanarity for steric reasons and have higher triplet energies than the E isomers. A sensitizer with $E_{\mathrm{T}}$ between the two (such as riboflavin or thioxanthone) transfers energy only to the E isomer, the Z isomer is no longer excited and accumulates, and the E/Z ratio obtained is the opposite of the thermodynamic equilibrium (Gilmour and others).

The first step of vision is a photoisomerization: in rhodopsin, 11-*cis*-retinal, bound to lysine as a protonated **imine**, absorbs a photon and isomerizes to all-*trans* within about $200\,\mathrm{fs}$ (quantum yield about 0.65); the resulting change in protein conformation starts the transmission of the light signal.

### 31.3.2. Azobenzene Photoswitches

The $\ce{N=N}$ bond of **azo compounds** can also isomerize photochemically. The E isomer of azobenzene is converted to the Z isomer on irradiation at about $340\,\mathrm{nm}$ ($\pi\to\pi^*$), and the Z isomer returns to the E form on irradiation at about $440\,\mathrm{nm}$ ($\mathrm{n}\to\pi^*$) or on heating; the two isomers differ greatly in shape and dipole moment ([6.5.5](/6.5.5#sec-5.1.4), [6.5.24](/6.5.24#sec-24.6.1)).

**Definition 31.3.2 (Molecular Photoswitch)** A molecule that can be interconverted reversibly between two (or several) stable states by light of two wavelengths, the structures and properties of the states being clearly different, is called a **molecular photoswitch**. Azobenzenes, diarylethenes (photochemical electrocyclization, [6.5.12](/6.5.12#sec-12.3.5)) and spiropyrans are three widely used classes of photoswitches.

A photoswitch converts a light signal into a change of molecular shape. The E isomer of azobenzene fits into the cavity of α-cyclodextrin and the Z isomer does not, so polymers bearing azobenzene and cyclodextrin polymers can be cross-linked or not by light, switching a gel and a solution reversibly. Attaching azobenzene to an enzyme inhibitor, an ion-channel ligand or a drug molecule makes it possible to switch the activity of the drug on and off with light at a chosen time and place; this field is called *photopharmacology*. Shifting the absorption of azobenzene into the visible or even red region (by ortho-tetrafluoro or tetrachloro substitution) is the key to making it usable in tissue.

### 31.3.3. [2+2] Photocycloaddition of α,β-Unsaturated Ketones and Alkenes

**Definition 31.3.3 (Photocycloaddition)** A cycloaddition between a photoexcited molecule and another unsaturated molecule is called a **photocycloaddition**.

The $[\pi2_{\mathrm{s}}+\pi2_{\mathrm{s}}]$ **cycloaddition**, which is symmetry-forbidden under thermal conditions, is allowed under irradiation (the **Woodward–Hoffmann rules**, [6.5.12](/6.5.12#sec-12.4.2)), and [2+2] photocycloaddition is therefore the main method for making cyclobutanes.

The [2+2] photocycloaddition of cyclic α,β-unsaturated ketones (such as cyclohex-2-en-1-one) with alkenes is the most widely used variant in synthesis (de Mayo, Eaton, Corey, 1960s). The enone undergoes rapid **intersystem crossing** after absorption, and the reaction proceeds from the $^3(\pi,\pi^*)$ state. In the **triplet state**, $\mathrm{C}_\alpha$ and $\mathrm{C}_\beta$ behave like a pair of radicals, one of which bonds first to the alkene to give a triplet 1,4-diradical. This must first undergo intersystem crossing to the **singlet** before it can close to the cyclobutane or fragment back to the starting materials. The reaction is therefore not a concerted **pericyclic reaction**, and the cis or trans configuration of the alkene is not retained in the product (it is not stereospecific).

![[2+2] Photocycloaddition of cyclohex-2-en-1-one with ethylene: the Cβ radical of the triplet (π,π*) state adds to ethylene to give a triplet 1,4-diradical (each fishhook arrow represents one electron); after intersystem crossing the two radical centers bond to give bicyclo[4.2.0]octan-2-one](./plots/enone-cycloaddition.py)

The **regioselectivity** depends on the electronic nature of the alkene. Electron-rich alkenes (enol ethers, 1,1-dialkylalkenes) give mainly the "head-to-tail" (HT) products, in which the substituent is on the side away from the carbonyl, adjacent to $\mathrm{C}_\beta$; electron-poor alkenes (acrylonitrile, acrylates) give mainly the "head-to-head" (HH) products, with the substituent adjacent to $\mathrm{C}_\alpha$:

```smiles
CC1=CC(=O)CCC1.C=COCC>>O=C1CCCC2(C)C(OCC)CC12
CC1=CC(=O)CCC1.C=CC#N>>O=C1CCCC2(C)CC(C#N)C12
```

(3-Methylcyclohex-2-en-1-one with ethyl vinyl ether: HT, greater than 99:1; with acrylonitrile: HH:HT = 84:16.) Corey explained this by **polarity inversion** (umpolung) in the excited state: in the ground state $\mathrm{C}_\beta$ is electron-poor, whereas in the $\pi,\pi^*$ excited state electron density moves toward $\mathrm{C}_\beta$, and the alkene approaches with the opposite dipole orientation (the exciplex model). Later experiments that trapped the intermediates with radical scavengers (Weedon, Schuster) showed that both 1,4-diradicals are formed, and that the regioselectivity is determined mainly by the ratio in which each diradical closes or fragments back to the starting materials.

Simple alkenes do not absorb in the visible region and are difficult to photocycloadd directly. After coordination of $\ce{Cu(I)}$ (such as $\ce{CuOTf}$) to alkenes, a new **charge-transfer transition** appears at $230$–$250\,\mathrm{nm}$ that can catalyze [2+2] photocycloaddition between alkenes (Salomon–Kochi), especially intramolecular reactions that give bicyclo[3.2.0]heptanes.

## 31.4. Photochemical Reactions of Carbonyl Compounds

### 31.4.1. Excited States of Carbonyl Groups

Carbonyl compounds have a weak $\mathrm{n}\to\pi^*$ absorption and a strong $\pi\to\pi^*$ absorption in the near ultraviolet:

| Compound | $\lambda_{\max}(\pi\to\pi^*)$ / nm ($\varepsilon$) | $\lambda_{\max}(\mathrm{n}\to\pi^*)$ / nm ($\varepsilon$) |
|---|---|---|
| Cyclohexanone | 200 (2000) | 285 (14) |
| 4-Methylpent-3-en-2-one | 230 (12 300) | 325 (90) |
| Benzaldehyde | 242 (14 000) | 328 (50) |
| Acetophenone | 238 (13 000) | 320 (40) |

($\varepsilon$ in $\mathrm{L\,mol^{-1}\,cm^{-1}}$.) After excitation the molecule relaxes rapidly to $\mathrm{S}_1(\mathrm{n},\pi^*)$. In aromatic ketones $\mathrm{S}_1(\mathrm{n},\pi^*)$ and $\mathrm{T}_2(\pi,\pi^*)$ are close in energy and, by El-Sayed's rule (Definition 31.2.2), **intersystem crossing** is extremely fast and converts almost all the population to $\mathrm{T}_1$. In aliphatic ketones intersystem crossing is slower (about $10^8\,\mathrm{s^{-1}}$) and $\mathrm{S}_1$ can also react. Carbonyl photochemistry is therefore mainly the chemistry of the $^3(\mathrm{n},\pi^*)$ state.

In an $\mathrm{n},\pi^*$ state the n orbital on oxygen (in the molecular plane) holds only one electron and π\* holds an extra one. The oxygen atom thus behaves like an electrophilic alkoxy radical, and the carbonyl carbon carries a π-type radical electron:

$$
\ce{R2C=O ->[h\nu][ISC] R2\dot{C}-\dot{O}} \quad (^3\mathrm{n},\pi^*).
$$
Its three typical reactions (cleavage of the bond at the α position, hydrogen atom abstraction and addition to alkenes) can all be understood as radical reactions ([6.5.7](/6.5.7#sec-7.5)).

### 31.4.2. The Norrish Type I Reaction

**Definition 31.4.1 (Norrish Type I Reaction)** The homolysis of the bond between the carbonyl carbon and the α carbon of an excited aldehyde or ketone, giving an acyl radical and an alkyl radical, is called the **Norrish type I reaction** (α-cleavage).

For the oxygen radical in the excited state, the $\ce{C(O)-C_\alpha}$ bond that is cleaved lies in the β position, so α-cleavage is a **β-scission**: the unpaired electron on oxygen and one electron of the $\ce{C-C}$ bond form the π bond of $\ce{C=O}$, and the other electron leaves with the alkyl group. The more stable the resulting radical pair (tertiary alkyl, benzyl), the faster the α-cleavage.

![Norrish type I reaction: in the triplet (n,π*) state of pentan-3-one, the unpaired electron on oxygen and one electron of the C(O)–Cα bond form a new C=O π bond, and the other electron stays on the ethyl group, giving a propanoyl radical and an ethyl radical](./plots/norrish-type-1.py)

The radical pair can then recombine (recombination after α-cleavage of cyclic ketones epimerizes the α position); the acyl radical can lose CO to give an alkyl radical that then couples (cyclic ketones undergo ring contraction in this way); or a β-hydrogen can be transferred between the two radicals to give an aldehyde and an alkene (disproportionation). In the polymer industry α-cleavage is used for photoinitiation: 2,2-dimethoxy-2-phenylacetophenone cleaves to two radicals on irradiation at $365\,\mathrm{nm}$ and initiates the **radical** polymerization of acrylates, which is used for light-curing coatings, dental resins and 3D printing.

```smiles
COC(OC)(C(=O)c1ccccc1)c1ccccc1>>O=[C]c1ccccc1.CO[C](OC)c1ccccc1
```

![Norrish type I cleavage of the photoinitiator 2,2-dimethoxy-2-phenylacetophenone (DMPA): on irradiation at 365 nm the C(O)–Cα bond breaks homolytically (fishhook arrows) to give a benzoyl radical and an α,α-dimethoxybenzyl radical; the benzoyl radical adds to the CH₂ terminus of methyl acrylate, giving the radical that starts chain growth](./plots/dmpa-initiator.py)

### 31.4.3. The Norrish Type II Reaction and Norrish–Yang Cyclization

**Definition 31.4.2 (Norrish Type II Reaction)** The abstraction of a γ hydrogen atom by the carbonyl oxygen of an excited aldehyde or ketone through a six-membered cyclic transition state (1,5-hydrogen atom transfer), giving a 1,4-diradical that fragments to an alkene and an enol, is called the **Norrish type II reaction**. Closure of the 1,4-diradical to a cyclobutanol is called the **Norrish–Yang reaction** (Yang cyclization).

The six-membered cyclic transition state places the γ-H in the most favorable position, the same 1,5-HAT on which remote functionalizations such as the Barton reaction rely. One end of the 1,4-diradical formed is an α-hydroxyalkyl radical (the carbonyl carbon) and the other is a γ-carbon radical. There are two fates: **β-scission** of the $\mathrm{C}_\alpha$–$\mathrm{C}_\beta$ bond gives an alkene and an enol (the enol then converts to a methyl ketone by **tautomerism**), or the two radical centers bond to give a cyclobutanol.

![Norrish type II reaction: the triplet of hexan-2-one abstracts the γ-H through a six-membered cyclic transition state (1,5-hydrogen atom transfer) to give a 1,4-diradical; the diradical fragments to prop-1-en-2-ol (which tautomerizes to acetone) and propene, or closes to 1,2-dimethylcyclobutanol (Norrish–Yang cyclization)](./plots/norrish-type-2.py)

The thermodynamic basis of **hydrogen atom transfer** is the bond energy: the energy released on forming the $\ce{O-H}$ bond is enough to compensate for breaking a $\ce{C-H}$ bond, and the excited state supplies an extra $300\,\mathrm{kJ\,mol^{-1}}$ or so, so even primary $\ce{C-H}$ bonds can be abstracted. The **triplet** of benzophenone likewise abstracts hydrogen from a solvent (isopropanol) or other molecules to give the benzhydrol radical, and two such radicals couple to give a pinacol (photochemical **pinacol coupling**).

![Photochemical pinacol coupling: the oxygen radical of the ³(n,π*) state of benzophenone abstracts the hydrogen from the C–H of isopropanol (fishhook arrow) to give the benzhydrol radical (ketyl) and the 2-hydroxy-2-propyl radical, which then passes the hydrogen of its O–H to another benzophenone molecule (giving acetone); two benzhydrol radicals couple to give the pinacol](./plots/photopinacol.py)

Norrish–Yang cyclization is a means of building four-membered rings or introducing hydroxy groups at inert positions in synthesis. In their synthesis of the cardiac glycoside ouabagenin, Baran and coworkers (2013) used a Norrish–Yang reaction to join the steroid C19 methyl group to a ketone carbonyl as a cyclobutanol and then opened the ring, thereby introducing oxygen at an angular methyl group that could not be functionalized directly.

### 31.4.4. Photoenolization

**Definition 31.4.3 (Photoenolization)** The reaction in which an aromatic aldehyde or ketone with an ortho alkyl group abstracts a hydrogen from the ortho alkyl group through the carbonyl oxygen under irradiation (intramolecular 1,5-HAT), giving an o-methylene quinoid enol (a hydroxy-o-quinodimethane), is called **photoenolization**.

```smiles
Cc1ccccc1C(=O)c1ccccc1>>C=C1C=CC=CC1=C(O)c1ccccc1
C=C1C=CC=CC1=C(O)c1ccccc1.O=C1C=CC(=O)O1>>O=C1OC(=O)C2C1Cc1ccccc1C2(O)c1ccccc1
```

![Photoenolization and Diels–Alder trapping: the triplet of 2-methylbenzophenone abstracts a hydrogen from the ortho methyl group (1,5-HAT) to give a 1,4-diradical that relaxes to a hydroxy-o-quinodimethane (photoenol); the long-lived E photoenol acts as an s-cis diene and undergoes a Diels–Alder reaction with maleic anhydride to give a tetralin derivative](./plots/photoenolization.py)

The photoenol formed has Z and E configurations. In the Z form the hydroxy group faces the methylene group and returns rapidly to the starting material by a 1,5-H shift ($k \approx 10^7\,\mathrm{s^{-1}}$, lifetime about $100\,\mathrm{ns}$). The E form cannot return in this way and has a lifetime of up to seconds; it is a reactive 1,3-diene that can be trapped by a dienophile such as maleic anhydride in a **Diels–Alder reaction** to give a tetralin derivative (the second reaction above). This is a way to generate o-quinodimethanes under mild conditions and to build polycyclic skeletons.

### 31.4.5. The Paternò–Büchi Reaction

**Definition 31.4.4 (Paternò–Büchi Reaction)** The formal [2+2] cycloaddition of an excited aldehyde or ketone with an alkene to give an oxetane is called the **Paternò–Büchi reaction**.

The reaction generally starts from the $^3(\mathrm{n},\pi^*)$ state of the carbonyl compound: the electrophilic oxygen radical adds to the alkene to give the 1,4-diradical that is as stable as possible at both ends, which then undergoes **intersystem crossing** and ring closure. The **regioselectivity** can therefore be predicted from radical stabilities. For benzophenone and 2-methylpropene, for example, oxygen adds to the $\ce{CH2}$ terminus to give a diphenylmethyl radical and a tertiary alkyl radical, and the main product is 3,3-dimethyl-2,2-diphenyloxetane.

![Paternò–Büchi reaction: the oxygen radical of the triplet (n,π*) state of benzophenone adds to the CH₂ terminus of 2-methylpropene to give the more stable 1,4-diradical (a diphenylmethyl radical and a tertiary alkyl radical), which closes after intersystem crossing to 3,3-dimethyl-2,2-diphenyloxetane](./plots/paterno-buchi.py)

The reaction requires the **triplet** energy of the alkene to be higher than that of the carbonyl compound (electron-rich simple alkenes, enol ethers and **silyl enol ethers** satisfy this). Otherwise the excited carbonyl compound transfers its energy to the alkene (triplet sensitization, Section 31.2.4) and the alkene isomerizes or dimerizes instead of giving an oxetane. Conjugated dienes have low $E_{\mathrm{T}}$ (about $220\,\mathrm{kJ\,mol^{-1}}$ for cyclohexa-1,3-diene) and cause **quenching** of the triplet of the ketone; aliphatic aldehydes can still form oxetanes with dienes, but this is a reaction of the **singlet** $\mathrm{S}_1(\mathrm{n},\pi^*)$, for which intersystem crossing is slower. The **stereoselectivity** is controlled by the conformation of the diradical intermediate and is often high (for example propanal with cyclohexa-1,3-diene, dr 80:20).

## 31.5. Photoinduced Electron Transfer and Photoredox Catalysis

### 31.5.1. Three Routes to Single Electron Transfer

**Single electron transfer** generates **radical ions**, which often fragment or form bonds immediately and thereby initiate radical reactions ([6.5.7](/6.5.7#sec-7.2.3)). Electrons can be supplied or removed in three ways:

1. Ground-state redox: stoichiometric oxidants ($\ce{Ce^4+}$, $\ce{Mn(OAc)3}$) or reductants (Na, $\ce{SmI2}$).
2. Excited-state redox: a molecule that has absorbed a photon becomes a strong oxidant or reductant and exchanges electrons with the substrate (Sections 31.5.2–31.5.5).
3. **Electrochemistry**: the substrate gains electrons at the cathode (reduction) or loses them at the anode (oxidation) (Section 31.7).

The latter two consume only photons or electrons and produce no stoichiometric metal waste, and over the last two decades they have become important methods in organic synthesis.

### 31.5.2. Redox Potentials of Excited States

An excited state is both a stronger reductant and a stronger oxidant. Consider the reducing power first: for the ground-state molecule PC to lose an electron, the electron must be removed from the HOMO; in the excited state PC\* that electron already sits in an orbital higher by $E_{0,0}$ and is much easier to lose. A thermodynamic cycle (neglecting the entropy difference between excited and ground states) gives:

**Definition 31.5.1 (Excited-State Redox Potential)** The electrode potential of a couple in which one member is an excited-state molecule is called an **excited-state redox potential**. It is related to the ground-state potential and the excited-state energy $E_{0,0}$ by

$$
E(\mathrm{PC}^{\bullet+}/\mathrm{PC}^*) = E(\mathrm{PC}^{\bullet+}/\mathrm{PC}) - E_{0,0}, \qquad E(\mathrm{PC}^*/\mathrm{PC}^{\bullet-}) = E(\mathrm{PC}/\mathrm{PC}^{\bullet-}) + E_{0,0}, \tag{31.1}
$$
where potentials are in V and $E_{0,0}$ is the difference between the lowest vibrational levels of the reacting excited state ($\mathrm{S}_1$ or $\mathrm{T}_1$) and the ground state, in eV (numerically equal to the value in V).

$E_{0,0}$ corresponds to the 0–0 transition between the lowest vibrational levels of the two states in the **Jablonski diagram**. Experimentally, $E_{0,0}$ of a **singlet** state is taken at the intersection of the normalized absorption and **fluorescence spectrum** (the two coincide at the 0–0 transition, and the **Stokes shift** separates the rest); $E_{0,0}$ of a **triplet** state is taken from the 0–0 band at the short-wavelength end of the phosphorescence spectrum in a rigid medium at low temperature (77 K). The conversion is $E_{0,0}/\mathrm{eV} = 1239.84/(\lambda_{0,0}/\mathrm{nm})$.

The zero of **electrode potential** is defined by the **standard hydrogen electrode**, but the literature of organic photochemistry and **electrochemistry** usually reports values relative to the **calomel electrode** (saturated calomel electrode, SCE, $+0.241\,\mathrm{V}$ vs SHE, [6.3.13](/6.3.13#sec-13.5.2)); in nonaqueous solvents the ferrocene–ferrocenium couple is often used as the reference (in acetonitrile $E(\ce{Fc+}/\ce{Fc}) \approx +0.40\,\mathrm{V}$ vs SCE). Potentials must be converted to the same reference and the same solvent before being compared. All potentials in this section are in acetonitrile versus SCE. The more negative the potential of a couple $A_{\mathrm{ox}}/A_{\mathrm{red}}$, the stronger a reductant $A_{\mathrm{red}}$ is; the more positive, the stronger an oxidant $A_{\mathrm{ox}}$ is.

From Eq. (31.1), the **Gibbs energy** of electron transfer from an excited molecule D\* to an acceptor A is:

**Formula 31.5.1 (Rehm–Weller Equation)** The Gibbs energy of photoinduced electron transfer $\ce{D^* + A -> D^{\bullet+} + A^{\bullet-}}$ is

$$
\Delta G_{\mathrm{ET}} = e\left[E(\mathrm{D}^{\bullet+}/\mathrm{D}) - E(\mathrm{A}/\mathrm{A}^{\bullet-})\right] - E_{0,0} - \frac{e^2}{4\pi\varepsilon_0\varepsilon_{\mathrm{r}}r}, \tag{31.2}
$$
where every term is an energy per molecule (in eV, the first term is simply the number of volts separating the two potentials). The last term is the Coulomb energy of the **ion pair** formed ($r$ is the separation of the ions); in polar solvents such as acetonitrile it is only about $0.06\,\mathrm{eV}$ and is often neglected. The equation is the same when the acceptor is excited ($\ce{D + A^* -> D^{\bullet+} + A^{\bullet-}}$), with $E_{0,0}$ taken as the excitation energy of A\*.

When $\Delta G_{\mathrm{ET}} < 0$, electron transfer is usually fast (approaching the diffusion-controlled limit). Rehm and Weller (1970) used this relation to correlate a large body of **quenching** data.

![Ground- and excited-state ([Ru(bpy)₃]²⁺, ³MLCT, E₀,₀ ≈ 2.10 eV) redox potentials (acetonitrile, vs SCE): excitation moves the Ru³⁺/Ru²⁺ couple from +1.29 V to −0.81 V (stronger reducing power) and the Ru²⁺/Ru⁺ couple from −1.33 V to +0.77 V (stronger oxidizing power). Potentials of several substrates are shown on the right: the excited state can reduce diethyl bromomalonate (−0.62 V) and oxidize N-methylacridane (+0.80 V, nearly thermoneutral), but cannot reduce α-bromoacetophenone directly (−1.46 V)](./plots/excited-state-potentials.py)

### 31.5.3. Common Photoredox Catalysts

**Definition 31.5.2 (Photoredox Catalysis)** A catalytic method in which a molecule (a **photoredox catalyst**) that absorbs visible light, has a sufficiently long-lived excited state and is reversibly redox-active generates radicals or radical ions by single electron transfer between its excited state and a substrate, and is regenerated at the end of the cycle, is called **photoredox catalysis**.

$[\ce{Ru(bpy)3}]^{2+}$ (bpy = 2,2′-bipyridine) was the first photoredox catalyst to be used systematically (MacMillan and Yoon, 2008; Stephenson, 2009). It has a strong metal-to-ligand charge-transfer absorption (MLCT, $\varepsilon \approx 1.4\times10^4\,\mathrm{L\,mol^{-1}\,cm^{-1}}$) at $452\,\mathrm{nm}$. After excitation to $^1\mathrm{MLCT}$, the strong spin–orbit coupling of Ru drives complete **intersystem crossing** to $^3\mathrm{MLCT}$ within about $100\,\mathrm{fs}$. This **triplet state** has a lifetime of about $1.1\,\mu\mathrm{s}$ (in acetonitrile), long enough to collide with substrates present at concentrations of only about $10^{-2}\,\mathrm{mol\,L^{-1}}$. In $^3\mathrm{MLCT}$ an electron has moved from a Ru $\mathrm{t_{2g}}$ orbital to a π\* orbital of one bpy, formally "$\mathrm{Ru^{III}}$ and a bpy **radical anion**": the electron on bpy makes it a reductant and Ru(III) makes it an oxidant. Ground-state $[\ce{Ru(bpy)3}]^{2+}$ is hardly reducing at all ($+1.29\,\mathrm{V}$) but becomes a reductant of moderate strength ($-0.81\,\mathrm{V}$) after excitation.

| Catalyst | $\lambda_{\max}$ / nm | $E(\mathrm{PC}^{\bullet+}/\mathrm{PC})$ | $E(\mathrm{PC}^{\bullet+}/\mathrm{PC}^*)$ | $E(\mathrm{PC}^*/\mathrm{PC}^{\bullet-})$ | $E(\mathrm{PC}/\mathrm{PC}^{\bullet-})$ |
|---|---|---|---|---|---|
| $[\ce{Ru(bpy)3}]^{2+}$ | 452 | +1.29 | −0.81 | +0.77 | −1.33 |
| *fac*-$\ce{Ir(ppy)3}$ | 375 | +0.77 | −1.73 | +0.31 | −2.19 |
| 4CzIPN (organic dye) | 435 | +1.52 | −1.04 | +1.35 | −1.21 |
| 9-Mesityl-10-methylacridinium | 430 | — | — | +2.06 | −0.57 |

(Potentials in V, acetonitrile, vs SCE; ppy is the cyclometalated ligand of 2-phenylpyridine and 4CzIPN is 1,2,3,5-tetrakis(carbazol-9-yl)-4,6-dicyanobenzene.) The excited state of the iridium complex is the stronger reductant; carbazole–cyanobenzene organic dyes contain no precious metal; and the excited **singlet** of 9-mesityl-10-methylacridinium (synthesized by Fukuzumi and developed by Nicewicz as a synthetic reagent) is a very strong oxidant ($+2.06\,\mathrm{V}$) that can take electrons from alkenes and arenes, with the mesityl group perpendicular to the acridinium plane preventing attack of **nucleophiles** at C9. The acridinium-catalyzed addition to alkenes contrary to **Markovnikov's rule** is described in [6.5.11](/6.5.11#sec-11.8.5).

The potential of a substrate likewise determines whether it can be oxidized or reduced. Reference values for several classes of substrates (half-peak potentials $E_{p/2}$ in acetonitrile, vs SCE; Roth, Romero and Nicewicz, 2016):

| Easily oxidized ($E(\mathrm{S}^{\bullet+}/\mathrm{S})$ / V) | | Easily reduced ($E(\mathrm{S}/\mathrm{S}^{\bullet-})$ / V) | |
|---|---|---|---|
| 1-(Cyclohex-1-en-1-yl)pyrrolidine (**enamine**) | +0.32 | Diethyl bromomalonate | −0.62 |
| $N$,$N$-Dimethylaniline | +0.74 | 4-Nitrobenzaldehyde | −0.86 |
| Triethylamine | +0.83 | Ethyl bromoacetate | −1.08 |
| Diisopropylamine | +1.09 | α-Bromoacetophenone | −1.46 |
| Styrene | +1.97 | Benzaldehyde | −1.93 |
| Cyclohexene | +2.37 | Cyclohexanecarbaldehyde | −2.28 |

The trends are the same as in ground-state chemistry: the more electron-rich the lone pair or π system and the more stable the radical cation, the easier the oxidation (enamines < arylamines < alkylamines < alkenes); the lower the LUMO (conjugation, electron-withdrawing groups), the easier the reduction; and the reduction of alkyl halides is often accompanied by cleavage of the $\ce{C-X}$ bond (dissociative electron transfer).

### 31.5.4. Two Quenching Cycles

**Definition 31.5.3 (Oxidative and Reductive Quenching)** The mode of quenching in which an excited photocatalyst gives an electron to a substrate (or a sacrificial oxidant) and is itself oxidized is called **oxidative quenching**; the mode in which an excited photocatalyst takes an electron from a substrate (or a sacrificial reductant) and is itself reduced is called **reductive quenching**.

![The two quenching cycles of photoredox catalysis (for [Ru(bpy)₃]²⁺). Left: oxidative quenching, in which *Ru²⁺ gives an electron to the acceptor A (E(Ru³⁺/*Ru²⁺) = −0.81 V) and the Ru³⁺ formed takes an electron back from the donor D. Right: reductive quenching, in which *Ru²⁺ takes an electron from the donor D (E(*Ru²⁺/Ru⁺) = +0.77 V) and the Ru⁺ formed reduces the acceptor A. In both cycles the net result is the transfer of one electron from D to A, with the energy supplied by the photon](./plots/photoredox-cycles.py)

In both cycles the photocatalyst passes through three states in turn, and the net result is the transfer of one electron from the donor D to the acceptor A. According to the roles of D and A, reactions fall into three classes:

1. Reductive: the substrate is the acceptor A, and a sacrificial reductant (an amine, Hantzsch ester) is added as the donor; reductive quenching is common. An example is the reduction of α-bromoacetophenone to acetophenone by $N$-methylacridane catalyzed by $[\ce{Ru(bpy)3}]^{2+}$ (Fukuzumi 1990): $^*\mathrm{Ru}^{2+}$ takes an electron from the acridane ($+0.77$ versus $+0.80\,\mathrm{V}$, nearly thermoneutral), and the $\mathrm{Ru}^+$ formed ($-1.33\,\mathrm{V}$) gives the electron to the bromo ketone ($-1.46\,\mathrm{V}$, slightly endergonic, but the $\ce{C-Br}$ bond breaks immediately and makes this step irreversible), producing a phenacyl radical and $\ce{Br-}$; the radical abstracts a hydrogen atom from the acridane **radical cation** (or from acridane itself), and the acridane ends up as 10-methylacridinium.

   ```smiles
   O=C(CBr)c1ccccc1.CN1c2ccccc2Cc2ccccc21>>CC(=O)c1ccccc1.C[n+]1c2ccccc2cc2ccccc21
   ```

2. Oxidative: the substrate is the donor D, and a sacrificial oxidant ($\ce{O2}$, persulfate, an aryldiazonium salt) is added as the acceptor; oxidative quenching is common. An example is the conversion of thiobenzanilide to 2-phenylbenzothiazole on irradiation in the presence of DBU, $\ce{O2}$ and $[\ce{Ru(bpy)3}]^{2+}$: $^*\mathrm{Ru}^{2+}$ gives an electron to $\ce{O2}$ to form $\ce{O2^{\bullet-}}$, $\mathrm{Ru}^{3+}$ ($+1.29\,\mathrm{V}$) oxidizes the deprotonated thioamide anion to a sulfur radical, which adds to the aromatic ring, and the cyclohexadienyl radical formed is aromatized by loss of a hydrogen atom to $\ce{O2^{\bullet-}}$.

   ```smiles
   S=C(Nc1ccccc1)c1ccccc1>>c1ccc(-c2nc3ccccc3s2)cc1
   ```

3. Redox-neutral: the substrates themselves supply both the part to be oxidized and the part to be reduced, no sacrificial reagent is used, and the catalyst is "first reduced, then oxidized". An example is the atom transfer radical addition (ATRA) of diethyl bromomalonate to alkenes (realized by Stephenson and coworkers in 2011 with an iridium complex; the ruthenium complex is used here to illustrate the same cycle): $^*\mathrm{Ru}^{2+}$ ($-0.81\,\mathrm{V}$) reduces the bromomalonate ($-0.62\,\mathrm{V}$), and the malonyl radical formed adds to the terminal carbon of the alkene. The secondary alkyl radical formed is either oxidized by $\mathrm{Ru}^{3+}$ to a **carbocation** that combines with $\ce{Br-}$ (radical–polar crossover), or abstracts a bromine atom from another molecule of bromomalonate (radical chain). With pent-4-en-1-ol as substrate, about 10% of tetrahydrofuran is formed in addition to the adduct, the product of trapping of the carbocation by the intramolecular hydroxy group; the adduct does not cyclize even on reflux in toluene, which shows that the tetrahydrofuran does not come from the adduct and supports the carbocation intermediate.

   ```smiles
   CCOC(=O)C(Br)C(=O)OCC.C=CCCCO>>CCOC(=O)C(CC(Br)CCCO)C(=O)OCC
   ```

   ![Organic steps of the photoredox ATRA reaction (E = CO₂Et). Top: single-electron reduction by *Ru²⁺ cleaves the C–Br bond (dissociative electron transfer), and the malonyl radical adds to the terminal carbon of pent-4-en-1-ol (fishhook arrows) to give a secondary alkyl radical. Bottom: Ru³⁺ oxidizes it to a carbocation (radical–polar crossover), which is trapped by bromide to give the adduct or by the intramolecular hydroxy group (5-exo cyclization) to give a tetrahydrofuran](./plots/atra-crossover.py)

### 31.5.5. Distinguishing Mechanisms by Quenching Experiments

Several mechanisms can often be written for a photocatalytic reaction. The reduction of α-bromoacetophenone above could also be formulated as an oxidative quenching: $^*\mathrm{Ru}^{2+}$ reduces the bromo ketone directly, and $\mathrm{Ru}^{3+}$ then oxidizes the radical formed from the acridane. There are three tools for deciding:

1. Thermodynamics: estimate $\Delta G$ for each step from Eqs. (31.1) and (31.2) and a table of potentials. The reduction of the bromo ketone ($-1.46\,\mathrm{V}$) by $^*\mathrm{Ru}^{2+}$ ($-0.81\,\mathrm{V}$) is endergonic by $0.65\,\mathrm{eV}$ and cannot compete with decay of the excited state.
2. Luminescence (fluorescence) **quenching**: the quenching of the catalyst emission by each reactant is measured according to the **Stern–Volmer equation** ([6.3.17](/6.3.17#sec-17.2.5)). In the experiment bromoacetophenone does not quench the emission of $^*\mathrm{Ru}^{2+}$ whereas the acridane does, showing that the acridane is what reacts with the excited state and the mechanism is reductive quenching.
3. **Quantum yield**: if more than one product molecule is formed per photon absorbed ($\Phi > 1$), a radical chain must operate; $\Phi < 1$ does not exclude a chain, but the chain is short. In addition, light on/off experiments can show whether the reaction continues after irradiation stops.

Quenching shows only that some reactant interacts with the excited state, not that this is the path leading to product (energy transfer also quenches), so a mechanistic conclusion should be supported by several kinds of evidence.

The importance of photoredox catalysis lies in having brought radical chemistry into the world of polar functional groups: carboxylic acids undergo one-electron oxidation and **decarboxylation** to alkyl radicals ([6.5.18](/6.5.18#sec-18.4.3)), one-electron oxidation of amines gives α-amino radicals, and aryldiazonium salts are reduced to aryl radicals ([6.5.24](/6.5.24#sec-24.4.3)). These radicals are then combined with Ni or Cu catalytic cycles (dual metallaphotoredox catalysis, MacMillan, Doyle and Molander, from 2014) to accomplish **cross-coupling reactions** ([6.5.29](/6.5.29#sec-29.4)) of $\mathrm{sp^3}$ carbons that previously required prior functionalization. Current research frontiers include direct activation of $\ce{C-H}$ bonds with **hydrogen atom transfer** catalysts (decatungstate, quinuclidine **radical cation**), sequential two-photon excitation to obtain stronger reducing power (consecutive photoinduced electron transfer), and photocatalysis with red or near-infrared light to increase penetration depth and for photocatalytic proximity labeling in cells.

## 31.6. Photocages and Photoaffinity Labeling

Photoreactions have two classic uses in chemical biology: releasing an active molecule at a chosen time and place with light, and using light to attach a probe molecule covalently to its binding protein.

**Definition 31.6.1 (Caged Compound)** A compound in which a key functional group of a biologically active molecule is blocked with a photolabile protecting group so that it is inactive, and in which irradiation cleaves the protecting group and rapidly releases the active molecule, is called a **caged compound**.

The most common cage is the o-nitrobenzyl group. The nitro oxygen of the excited state abstracts the hydrogen at the **benzylic position** (the same 1,5-HAT as in photoenolization) to give an *aci*-nitro intermediate; cyclization and ring opening then release the protected carboxylic acid, phosphate or alcohol, with formation of o-nitrosobenzaldehyde:

```smiles
O=C(OCc1ccccc1[N+](=O)[O-])C>>CC(=O)O.O=Cc1ccccc1N=O
```

![Release of acetic acid from an o-nitrobenzyl photocage. Top: the nitro group of the excited state abstracts the benzylic hydrogen (1,5-HAT) to give the aci-nitro tautomer (a quinoid nitronic acid); its oxide adds to the exocyclic carbon, the aromatic ring regains aromaticity, and the ring closes to a 1,3-dihydro-2,1-benzisoxazol-1-ol. Bottom: ring opening gives a nitroso hemiacetal ester, which decomposes to o-nitrosobenzaldehyde and free acetic acid](./plots/nitrobenzyl-uncaging.py)

(o-Nitrobenzyl acetate is shown as the example.) Caged ATP, glutamate and calcium **chelating agents** are used in neuroscience to release signaling molecules at a single synapse on the millisecond time scale. The o-nitrobenzyl group absorbs near $350\,\mathrm{nm}$, whereas cages such as coumarin-4-ylmethyl can be excited with visible light or two-photon (near-infrared) excitation, which damages tissue less.

**Definition 31.6.2 (Photoaffinity Labeling)** A method in which a group that generates a highly reactive intermediate on irradiation is introduced into a ligand, the ligand first binds noncovalently to the target protein, and irradiation then causes the intermediate to react with bonds near the binding site and form a covalent link, so that the target protein and binding site of the ligand can be identified, is called **photoaffinity labeling**.

The three commonly used photoactivatable groups correspond to three classes of reactive intermediates in this course: aryl **azides** lose $\ce{N2}$ on photolysis to give nitrenes ([6.5.24](/6.5.24#sec-24.8.1)); diazirines (three-membered diazacyclopropenes) lose $\ce{N2}$ on irradiation at about $350\,\mathrm{nm}$ to give **carbenes** that insert into nearby $\ce{C-H}$ and $\ce{O-H}$ bonds; and the $^3(\mathrm{n},\pi^*)$ state of benzophenone abstracts hydrogen from nearby amino acid residues, after which the radical pair couples (Section 31.4.3). Diazirines are small and reactive, whereas benzophenone can be excited repeatedly and is not destroyed by water, so each has its advantages. The labeled protein is identified by **mass spectrometry** ([6.4.15](/6.4.15)); this is one of the principal chemical methods for finding the targets of drugs, and it is treated in detail in [6.6](/6.6).

![Photoaffinity labeling groups. Top: on photolysis of an aryl azide, the electron pair of the N–N bond stays with the departing N₂ to give a singlet aryl nitrene, which inserts into a nearby N–H or C–H bond. Bottom: on irradiation at about 350 nm, a 3-aryl-3-(trifluoromethyl)diazirine loses N₂ by cleavage of both C–N bonds to give a singlet carbene, which inserts into an X–H bond of the binding protein and links the probe covalently to the protein](./plots/photoaffinity.py)

## 31.7. Organic Electrochemistry

### 31.7.1. Comparison with Conventional Reactions

The history of the **electrolysis** of organic compounds is older than the discovery of the electron: Faraday (1834) obtained hydrocarbons on electrolyzing acetates, Kolbe (1849) obtained coupled alkanes on electrolyzing carboxylates, and Haber (1898) studied the stepwise electroreduction of nitrobenzene. In industry, tetraethyllead has been made by electrolysis since 1964 and adiponitrile by electroreduction of acrylonitrile since 1965.

**Definition 31.7.1 (Organic Electrochemistry)** A method in which an electrode serves as the donor or acceptor of electrons and organic molecules are converted to products by redox reactions at the electrode (or with reagents generated at the electrode) is called **organic electrochemistry** (organic electrosynthesis), the application of electrosynthesis to organic chemistry.

Organic electrochemistry is the fastest-growing part of **electrosynthesis** ([6.3.14](/6.3.14#sec-14.5.3)).

| | Organic electrochemical reactions | Conventional organic reactions |
|---|---|---|
| Redox reagent | The electrode supplies or accepts electrons | Stoichiometric oxidants and reductants |
| Solvent system | Polar solvent containing a **supporting electrolyte** (conductive) | Water or common organic solvents |
| Reaction site | Electrode surface, heterogeneous | Usually homogeneous solution |
| Means of control | Potential, current density, electrode material, electrocatalyst | Temperature, pressure, catalyst, reagent structure |

The **electrode potential** is a "continuously adjustable reagent strength": by controlling the potential of the **working electrode**, only functional groups with potentials below it are oxidized. In practical synthesis constant-current electrolysis is more common (two electrodes suffice and the equipment is simple), and the progress of the reaction is controlled by the charge passed. According to **Faraday's laws of electrolysis**, converting $n$ mol of substrate with $z$ electrons transferred per molecule requires a charge $Q = nzF$. For example, a two-electron oxidation of 1 mmol of substrate requires $193\,\mathrm{C}$, which takes about $10.7\,\mathrm{h}$ at a current of $5\,\mathrm{mA}$; the charge actually passed is often 1.5–3 times the theoretical value, and the reciprocal of this ratio is the **current efficiency**.

### 31.7.2. Electrode Processes and Electrolysis Cells

The reaction of an organic molecule at an electrode comprises several steps in series ([6.3.14](/6.3.14#sec-14.2.3)): mass transport of the substrate from solution to the electrode surface, adsorption at the surface, electron exchange with the electrode, and **desorption** of the product and mass transport back into solution. The **radical ion** formed reacts further in the thin layer near the electrode (loss of a proton, fragmentation, gain or loss of another electron), so reactions in **electrochemistry** are often written as combinations of E (electron transfer) and C (chemical step), such as ECEC. These steps can be diagnosed by **cyclic voltammetry**: the potential of the oxidation peak tells us how much potential is needed, and disappearance of the reverse peak shows that the radical ion undergoes a fast follow-up reaction ([6.4.6](/6.4.6#sec-6.6.4)).

The simplest apparatus is an undivided **electrolytic cell** in which the **anode** and the **cathode** are immersed in the same solution; the reaction at the **counter electrode** (in an anodic oxidation, usually the reduction of protons or methanol to $\ce{H2}$ at the cathode) must not interfere with the product. If necessary a porous separator or ion-exchange membrane divides the cell into an anode compartment and a cathode compartment. The anode is often reticulated vitreous carbon (RVC) or graphite, with large **specific surface area** and good chemical resistance, and the cathode is often platinum or nickel, which favors hydrogen evolution; typical **supporting electrolytes** are $\ce{n-Bu4NBF4}$ and $\ce{LiClO4}$. Flow cells reduce the electrode gap to a fraction of a millimeter, which lowers the solution resistance, allows little or no supporting electrolyte and also facilitates scale-up.

### 31.7.3. Direct and Indirect Electrolysis

**Definition 31.7.2 (Direct and Indirect Electrolysis)** An electrolysis in which the substrate exchanges electrons directly with the electrode at its surface is called **direct electrolysis**. An electrolysis in which the electrode first oxidizes or reduces a molecule that can gain and lose electrons reversibly (a **redox mediator**), which then exchanges electrons with the substrate in solution and returns to the electrode after being regenerated, is called **indirect electrolysis**.

In indirect electrolysis the mediator is the "carrier" of electrons and reacts with the substrate in solution rather than at the electrode surface. This has several advantages: the potential of the mediator is lower than that of the substrate, so a milder **electrode potential** suffices and overoxidation of other functional groups is avoided; the reaction proceeds homogeneously in solution and avoids passivation of the electrode surface (coating of the electrode by a polymer film); and different mediators change the selectivity (**single electron transfer** or **hydrogen atom transfer**). Common mediators are triarylamines, ferrocene, halide ions ($\ce{I-}$ and $\ce{Br-}$ oxidized to $\ce{I2}$ and $\ce{Br+}$ equivalents), TEMPO (oxidation of alcohols) and $N$-hydroxyphthalimide (HAT). In this sense a photoredox catalyst is a mediator "charged" by light rather than by an electrode.

### 31.7.4. Classical Organic Electrosyntheses

Kolbe electrolysis: a concentrated solution of a carboxylate loses an electron at the **anode**, the acyloxy radical formed rapidly undergoes **decarboxylation**, and the alkyl radicals meet at high concentration at the electrode surface and couple, $\ce{2RCOO- -> R-R + 2CO2 + 2e-}$; water is reduced to $\ce{H2}$ at the cathode. The mechanism and scope are described in [6.5.18](/6.5.18#sec-18.4.2).

The electrosynthesis of adiponitrile (Baizer; commissioned by Monsanto in 1965) is the largest organic electrosynthetic process. Hydrogenation of the product gives hexamethylenediamine, used to make nylon-66:

```smiles
C=CC#N.C=CC#N>>N#CCCCCC#N
```

![Cathodic hydrodimerization of acrylonitrile: acrylonitrile gains an electron at the cathode, the single electron of the radical anion residing mainly on the β carbon and the negative charge mainly on the α carbon and the cyano group; two radical anions couple tail to tail at the β carbon (fishhook arrows), and the dianion formed is protonated twice by water to give adiponitrile](./plots/adiponitrile.py)

At the cathode $\ce{2CH2=CHCN + 2H2O + 2e- -> NC(CH2)4CN + 2OH-}$, and at the anode $\ce{H2O -> 1/2O2 + 2H+ + 2e-}$. Acrylonitrile gains one electron at the cathode to give a **radical anion**, with the negative charge and the single electron mainly on $\mathrm{C}_\beta$ and the cyano group. Two radical anions (or a radical anion and another molecule of acrylonitrile) bond at $\mathrm{C}_\beta$ (tail-to-tail coupling), and the dianion formed is protonated by water. The competing reaction is direct protonation of the radical anion followed by further reduction to propanenitrile (a by-product). The industrial process uses a Pb or Cd cathode with high hydrogen **overpotential** and adds a tetraalkylammonium salt: the quaternary ammonium cations form a hydrophobic layer at the cathode surface, lowering the concentration of water so that coupling wins over protonation ([6.3.14](/6.3.14#sec-14.5.3)).

Another classical reaction is the anodic α-methoxylation of carbamates (Shono oxidation). When $N$-methoxycarbonylpyrrolidine is electrolyzed in methanol, the nitrogen lone pair loses an electron, the radical cation loses an α-H and a further electron to give an $N$-acyliminium ion, and trapping by methanol gives the 2-methoxy product, a general precursor for introducing **nucleophiles** at the α position under the action of a **Lewis acid**.

```smiles
COC(=O)N1CCCC1>>COC(=O)N1CCCC1OC
```

![Shono oxidation: the nitrogen lone pair of N-methoxycarbonylpyrrolidine loses an electron at the anode, the radical cation loses an α-H to give an α-amino radical, and loss of another electron gives an N-acyliminium ion; methanol adds to the carbon of the iminium ion and a proton is lost, giving the 2-methoxy product](./plots/shono.py)

### 31.7.5. Modern Electrosynthesis: Mediator-Catalyzed Amidyl Radical Cyclization

The $\ce{N-H}$ of an $N$-aryl amide or carbamate is deprotonated and oxidized to give a nitrogen-centered amidyl radical, which undergoes 5-exo cyclization onto an intramolecular alkene or alkyne to build nitrogen heterocycles such as pyrrolidinones, oxazolidinones and imidazolidinones (Xu and coworkers, from 2016). Typical conditions: an undivided **electrolytic cell**, an RVC anode and a Pt cathode, constant current of $5\,\mathrm{mA}$, ferrocene (5 mol%) as the mediator, 1,4-cyclohexadiene as the hydrogen atom donor and $\ce{n-Bu4NBF4}$ as the **supporting electrolyte**, in THF/MeOH at reflux.

![Ferrocene-mediated electrochemical amidyl radical cyclization: the anode oxidizes ferrocene to ferrocenium, which oxidizes the deprotonated allyl N-phenylcarbamate to the amidyl radical; the N radical adds to the internal carbon of the intramolecular alkene (5-exo-trig) to give a primary alkyl radical, which abstracts a hydrogen atom from 1,4-cyclohexadiene to give 4-methyl-3-phenyloxazolidin-2-one; at the cathode methanol is reduced to H₂ and methoxide, which serves as the base](./plots/amidyl-cyclization.py)

This design illustrates several advantages of **electrochemistry**: the potential of the mediator ($\ce{Fc+}/\ce{Fc}$) is far below the oxidation potential of the amide itself, so the conditions are mild toward other functional groups; hydrogen evolution at the cathode produces the base at the same time, so no stoichiometric base or oxidant needs to be added; and the primary alkyl radical formed can also be trapped and functionalized further (added to an arene, oxidized to a **carbocation** and so on), constructing polycyclic compounds in one step. The group used this method to make the skeletons of drug molecules such as androgen receptor antagonists. Further frontiers of **electrosynthesis** include alternating current and rapidly alternating polarity electrolysis for improved selectivity (Baran and others), the combination of electrochemistry and photochemistry (electrophotocatalysis) for stronger redox power, and $\ce{CO2}$ reduction driven by renewable electricity and the "electrification" of the chemical industry.

## 31.8. Mechanochemistry

**Definition 31.8.1 (Mechanochemistry)** The field that studies chemical and physicochemical changes induced by mechanical energy (grinding, impact, shear, stretching, ultrasound) is called **mechanochemistry**, and the corresponding reactions are called mechanochemical reactions.

In the 1890s Carey Lea found that grinding $\ce{HgCl2}$ and silver halides decomposes them, whereas heating merely sublimes $\ce{HgCl2}$, showing that chemical changes caused by mechanical energy and by heat can differ. Ostwald (1919) listed mechanochemistry as a branch alongside **thermochemistry**, electrochemistry and photochemistry. The two principal ways of applying mechanical force are:

- Ball milling: solid reactants and balls of steel or zirconia are placed in a closed jar that is shaken at high frequency (about $30\,\mathrm{Hz}$) or rotated, and the impact and shear of the balls repeatedly fracture, mix and locally heat the solids, which react without solvent or with only a little liquid (liquid-assisted grinding). It suits poorly soluble substrates and can greatly reduce solvent use; the preparation of **Grignard reagents** in air by ball milling (Ito and coworkers, 2021) is one example.
- Ultrasound: in an ultrasonically treated polymer solution cavitation bubbles form, and when a bubble collapses the surrounding solvent flows rapidly and stretches the polymer chains. The force is largest at the middle of the chain, so bonds located in the middle of a long chain are cleaved selectively.

**Definition 31.8.2 (Mechanophore)** A molecular unit embedded in a polymer chain that undergoes a specific chemical reaction (ring opening, bond cleavage, isomerization) when stretched by an external force is called a **mechanophore**.

Why does force promote reaction? A tensile force $F$ applied along the **reaction coordinate** $x$ does work $Fx$ on the molecule, which tilts the **potential energy surface** and lowers the barrier by about $F\Delta x^\ddagger$ ($\Delta x^\ddagger$ is the elongation in the direction of the force from the minimum to the transition state), and the rate constant increases according to the Bell model:

$$
k(F) = k_0\exp\left(\frac{F\Delta x^\ddagger}{k_{\mathrm{B}}T}\right).
$$
A force of $1\,\mathrm{nN}$ acting over $0.1\,\mathrm{nm}$ does work $1\times10^{-19}\,\mathrm{J}$ per molecule, that is $60\,\mathrm{kJ\,mol^{-1}}$, enough to make reactions that are impossible at room temperature occur rapidly. Force has a direction: it lowers only the barriers of channels that elongate along the direction of stretching, so it can select pathways that neither thermal nor photochemical reactions follow.

![Lowering of a barrier by mechanical force (Bell model, schematic): forces of 0, 0.5 and 1.0 nN applied along the stretched bond tilt the potential energy curve by subtraction of F·x, and the barrier height decreases successively by about F·Δx‡ (for Δx‡ = 0.1 nm, 1 nN lowers it by about 60 kJ/mol); the transition state also shifts toward the reactant side](./plots/force-tilted-barrier.py)

Representative examples:

- Ring opening of benzocyclobutenes (Moore and coworkers, 2007): in the thermal reaction cis-disubstituted benzocyclobutenes open **conrotatory**, and in the photoreaction **disrotatory** (**electrocyclic reactions**, [6.5.12](/6.5.12#sec-12.3.4)), giving o-quinodimethanes of different configuration. When the benzocyclobutene is embedded in a polymer chain and stretched by ultrasound, both the cis and trans substrates give the same E,E product (shown by trapping with a **Diels–Alder reaction**), showing that the external force changes the potential energy surface and makes the formally "forbidden" pathway possible.
- Mechanochromism: spiropyran opens on stretching to the colored merocyanine, and embedded in a polymeric material it can reveal the distribution of stress (Moore, Sottos and coworkers, 2009); diarylbibenzofuranone (DABBF) undergoes **homolysis** on stretching to two blue **persistent radicals**, the material changes color, and the **electron paramagnetic resonance** signal increases with the extension (Otsuka and coworkers, 2015).
- "Unzipping" of polyladderene: ultrasound opens the cyclobutane rings of the ladder polymer one after another, converting the insulating polyladderene to semiconducting polyacetylene (Xia and coworkers, 2017).
- Mechanical redox of piezoelectric materials: on ball milling, piezoelectric particles such as $\ce{BaTiO3}$ are polarized by impact and, like photoredox catalysts, give electrons to aryldiazonium salts to generate aryl radicals, accomplishing arylation and borylation reactions (Kubota, Ito and coworkers, 2019).

![Ring opening of a spiropyran (by light or mechanical force): the spiro C–O bond cleaves heterolytically, the electron pair staying on the phenoxide oxygen while the lone pair of the indoline nitrogen forms a C=N⁺ bond; cis–trans isomerization of the central double bond gives the planar, conjugated, colored merocyanine zwitterion; heating or visible light closes the ring again](./plots/spiropyran.py)

Current directions in mechanochemistry are the use of mechanophores in self-reporting and self-healing materials and in force-controlled drug release, and the replacement of solution reactions by ball milling for greener synthesis.

## Summary

| Topic | Key points |
|---|---|
| Energy scales | $E_{\mathrm{m}} = 1.196\times10^5/(\lambda/\mathrm{nm})\,\mathrm{kJ\,mol^{-1}}$; $E/\mathrm{eV} = 1239.84/(\lambda/\mathrm{nm})$; ultraviolet–visible photons carry $150$–$600\,\mathrm{kJ\,mol^{-1}}$, comparable to bond energies |
| Excited states (31.2) | Vertical transitions (Definition 31.2.1); **Kasha's rule**: only $\mathrm{S}_1$ and $\mathrm{T}_1$ matter; $E(\mathrm{T}_1) < E(\mathrm{S}_1)$; El-Sayed's rule (Definition 31.2.2): $^1(\mathrm{n},\pi^*)\to{}^3(\pi,\pi^*)$ is fast; three reaction modes: radical, redox, energy transfer |
| Energy transfer | **Triplet** sensitization requires $E_{\mathrm{T}}(\text{sensitizer}) > E_{\mathrm{T}}(\text{substrate})$; Dexter (Definition 31.2.3): exchange mechanism, exponential decay, contact distance; Förster: $r^{-6}$, **singlet** states |
| Alkenes (31.3) | $\pi,\pi^*$ states twist to $90^\circ$; the **photostationary state** is set by the ratio of $\varepsilon\Phi$ and can give the thermodynamically unfavorable Z isomer; azobenzene photoswitches (Definition 31.3.2); [2+2] photocycloaddition of enones proceeds through a triplet 1,4-diradical, HT with electron-rich alkenes and HH with electron-poor alkenes |
| Carbonyls (31.4) | The oxygen of $^3(\mathrm{n},\pi^*)$ acts like an alkoxy radical: Norrish I (Definition 31.4.1, α-cleavage = **β-scission**); Norrish II and Yang cyclization (Definition 31.4.2, 1,5-HAT); photoenolization (Definition 31.4.3); Paternò–Büchi (Definition 31.4.4, via the most stable diradical, requires the alkene to have the higher $E_{\mathrm{T}}$) |
| Photoredox (31.5) | Eq. (31.1): excited-state potential = ground-state potential ∓ $E_{0,0}$; **Rehm–Weller equation** (Formula 31.5.1); $[\ce{Ru(bpy)3}]^{2+}$: $+1.29/-0.81/+0.77/-1.33\,\mathrm{V}$; oxidative and reductive quenching (Definition 31.5.3); reductive, oxidative and redox-neutral classes; **quenching** experiments, thermodynamics and **quantum yield** distinguish mechanisms |
| Biological applications (31.6) | Photocages (o-nitrobenzyl, Definition 31.6.1); photoaffinity labeling (azides, diazirines, benzophenone, Definition 31.6.2) |
| Electrochemistry (31.7) | $Q = nzF$; E/C steps of electrode processes; direct and indirect electrolysis (Definition 31.7.2); Kolbe electrolysis, adiponitrile (tail-to-tail coupling), Shono oxidation, ferrocene-mediated amidyl radical cyclization |
| Mechanochemistry (31.8) | Ball milling and ultrasound; Bell model $k(F) = k_0\mathrm{e}^{F\Delta x^\ddagger/k_{\mathrm{B}}T}$, $1\,\mathrm{nN}\times0.1\,\mathrm{nm} \approx 60\,\mathrm{kJ\,mol^{-1}}$; mechanophores (Definition 31.8.2): benzocyclobutene, spiropyran, DABBF, piezoelectric redox |

## Questions

1. In a **Jablonski diagram**, let the wavelengths of absorption to $\mathrm{S}_1$ and $\mathrm{S}_2$ be $\lambda_2$ and $\lambda_1$, and the wavelengths of fluorescence and phosphorescence be $\lambda_2'$ and $\lambda_3$. Compare $\lambda_1$, $\lambda_2$, $\lambda_2'$ and $\lambda_3$, and $E(\mathrm{S}_0)$, $E(\mathrm{S}_1)$ and $E(\mathrm{T}_1)$, and explain.

   **Answer** $\lambda_1 < \lambda_2 < \lambda_2' < \lambda_3$ and $E(\mathrm{S}_0) < E(\mathrm{T}_1) < E(\mathrm{S}_1)$. $\mathrm{S}_2$ lies above $\mathrm{S}_1$, so its absorption wavelength is shorter. Fluorescence is emitted from the lowest vibrational level of $\mathrm{S}_1$ to the various vibrational levels of $\mathrm{S}_0$, whereas absorption goes from the lowest vibrational level of $\mathrm{S}_0$ to the various vibrational levels of $\mathrm{S}_1$; the two coincide only at the 0–0 transition, so fluorescence is generally at longer wavelength than absorption (the **Stokes shift**). The energy of $\mathrm{T}_1$ lies below that of $\mathrm{S}_1$ (two electrons with parallel spin have a negative exchange energy and avoid each other, the molecular version of Hund's rule), so phosphorescence has the longest wavelength.

2. The **fluorescence spectrum** of many rigid arenes are approximately mirror images of their $\mathrm{S}_0\to\mathrm{S}_1$ absorption bands, and both are broad bands with several peaks. Explain this with the Jablonski diagram and the Franck–Condon principle.

   **Answer** Absorption goes from $v = 0$ of $\mathrm{S}_0$ to $v' = 0, 1, 2, \dots$ of $\mathrm{S}_1$; the peak spacing is the vibrational spacing of $\mathrm{S}_1$ and the relative intensities are set by the Franck–Condon factors (the overlap of the vibrational wavefunctions of the two states). Fluorescence (by **Kasha's rule**) goes from $v' = 0$ of $\mathrm{S}_1$ to $v = 0, 1, 2, \dots$ of $\mathrm{S}_0$, with the vibrational spacing of $\mathrm{S}_0$. In a rigid molecule the potential curves of the two electronic states have similar shapes and similar vibrational frequencies, so the distribution of Franck–Condon factors is symmetric and the two spectra are approximately mirror images about the 0–0 band. Each vibrational peak is further broadened by solvent effects and rotation, giving structured broad bands ([6.4.10](/6.4.10)).

3. Irradiating (E)-stilbene with $313\,\mathrm{nm}$ light finally gives a **photostationary state** containing about 90% of the cis isomer, although decay from the twisted excited state gives the two isomers with similar probabilities. Explain this, and say how a higher proportion of the cis isomer can be obtained.

   **Answer** At the photostationary state $[Z]/[E] = \varepsilon_E\Phi_{E\to Z}/(\varepsilon_Z\Phi_{Z\to E})$. (E)-Stilbene is planar and well conjugated and absorbs much more strongly at $313\,\mathrm{nm}$ than the twisted cis isomer, $\varepsilon_E \gg \varepsilon_Z$, so the trans isomer is continually excited and converted whereas the cis isomer is excited very little and accumulates ("photoextraction"). The proportion of the cis isomer can be raised by choosing a wavelength at which the two absorptions differ more (a longer wavelength at which the cis isomer absorbs even less) or by sensitized isomerization with a sensitizer whose **triplet** energy suffices to sensitize only the trans isomer.

4. Why does the Paternò–Büchi reaction generally require the triplet energy of the alkene to be higher than that of the carbonyl compound? What happens if cyclohexa-1,3-diene ($E_{\mathrm{T}} \approx 220\,\mathrm{kJ\,mol^{-1}}$) and benzophenone ($287\,\mathrm{kJ\,mol^{-1}}$) are irradiated together?

   **Answer** If the $E_{\mathrm{T}}$ of the alkene is lower than that of the ketone, the triplet ketone transfers its energy to the alkene (Dexter energy transfer, exergonic and close to diffusion-controlled) and returns to the ground state without adding; the sensitized alkene undergoes E/Z isomerization or [2+2] dimerization. For benzophenone and cyclohexa-1,3-diene the energy transfer is exergonic by about $67\,\mathrm{kJ\,mol^{-1}}$, the diene causes **quenching** of the triplet of the ketone, and the dimers of cyclohexadiene ([2+2] and [4+2] dimers) are obtained rather than the oxetane. For this reason conjugated dienes are used as triplet quenchers to test whether a photoreaction proceeds through a triplet state.

5. Write the main reaction type and the products on irradiation of the following ketones: (a) 2,2-dimethylcyclohexanone; (b) pentan-2-one; (c) 2-methylbenzophenone in the presence of maleic anhydride.

   **Answer** (a) Norrish type I: α-cleavage occurs on the side that gives a tertiary alkyl radical (the C1–C2 bond), giving an acyl–tertiary alkyl 1,6-diradical. Then: a β-H of the tertiary alkyl radical is transferred to the acyl radical (disproportionation) to give unsaturated aldehydes (6-methylhept-6-enal and 6-methylhept-5-enal); or an α-H of the acyl radical is transferred to the tertiary alkyl radical to give a **ketene**, which is trapped by a solvent such as methanol as an ester; or the acyl radical loses CO and the two alkyl radical centers couple to give 1,1-dimethylcyclopentane. (b) Norrish type II: the hydrogen on the γ position (C5) is transferred to oxygen through a six-membered cyclic transition state, and the 1,4-diradical fragments to ethylene and prop-1-en-2-ol (which tautomerizes to acetone), partly closing to 1-methylcyclobutanol. (c) Photoenolization: a hydrogen of the ortho methyl group is transferred to the carbonyl oxygen to give the E photoenol, which is trapped by maleic anhydride in a **Diels–Alder reaction** to give 1-hydroxy-1-phenyl-1,2,3,4-tetrahydronaphthalene-2,3-dicarboxylic anhydride.

6. Estimate excited-state potentials from absorption and emission spectra. (a) Which transition in the Jablonski diagram corresponds to $E_{0,0}$ of a **singlet** and of a triplet state, and how is each measured? (b) The 0–0 band in the emission spectrum of $[\ce{Ru(bpy)3}]^{2+}$ at 77 K is at about $590\,\mathrm{nm}$, and the ground-state potentials are $E(\mathrm{Ru}^{3+}/\mathrm{Ru}^{2+}) = +1.29\,\mathrm{V}$ and $E(\mathrm{Ru}^{2+}/\mathrm{Ru}^{+}) = -1.33\,\mathrm{V}$ (vs SCE). Estimate the two excited-state potentials.

   **Answer** (a) Singlet: $\mathrm{S}_0(v=0) \leftrightarrow \mathrm{S}_1(v'=0)$, taken at the intersection of the normalized absorption and fluorescence spectra; triplet: $\mathrm{T}_1(v'=0) \to \mathrm{S}_0(v=0)$, taken at the shortest-wavelength vibrational peak (the 0–0 band) of the phosphorescence in a rigid medium at low temperature. (b) $E_{0,0} = 1239.84/590 = 2.10\,\mathrm{eV}$; $E(\mathrm{Ru}^{3+}/^*\mathrm{Ru}^{2+}) = 1.29 - 2.10 = -0.81\,\mathrm{V}$ and $E(^*\mathrm{Ru}^{2+}/\mathrm{Ru}^{+}) = -1.33 + 2.10 = +0.77\,\mathrm{V}$.

7. One paper reports a potential of $-1.00\,\mathrm{V}$ vs SHE and another reports $-1.20\,\mathrm{V}$ vs SCE. Whose reduced form is the stronger reductant?

   **Answer** Converting to the same reference: $-1.20\,\mathrm{V}$ vs SCE $= -1.20 + 0.241 = -0.96\,\mathrm{V}$ vs SHE. The potential $-1.00\,\mathrm{V}$ vs SHE is more negative, so its reduced form is the stronger reductant (the two can be compared directly only if both were measured in aqueous solution; potentials in different solvents also differ in **liquid junction potential** and solvation).

8. $\alpha$-Bromoacetophenone is reduced to acetophenone using $[\ce{Ru(bpy)3}]^{2+}$, visible light and $N$-methylacridane as reductant. (a) Write the two possible catalytic cycles, reductive quenching and oxidative quenching. (b) Decide from the potentials which is feasible. (c) The experiment shows that bromoacetophenone does not quench the emission of the catalyst but the acridane does; which mechanism does this support? (d) What would a measured **quantum yield** of 5 mean?

   **Answer** (a) Reductive quenching: $^*\mathrm{Ru}^{2+}$ + acridane → $\mathrm{Ru}^{+}$ + acridane **radical cation**; $\mathrm{Ru}^{+}$ + bromo ketone → $\mathrm{Ru}^{2+}$ + phenacyl radical + $\ce{Br-}$; the radical abstracts hydrogen to give acetophenone. Oxidative quenching: $^*\mathrm{Ru}^{2+}$ + bromo ketone → $\mathrm{Ru}^{3+}$ + radical + $\ce{Br-}$; the radical abstracts hydrogen from the acridane (the $\ce{C-H}$ bond energy is about $301\,\mathrm{kJ\,mol^{-1}}$ and that of the $\ce{C-H}$ bond formed in acetophenone about $389\,\mathrm{kJ\,mol^{-1}}$, so the step is exothermic) to give an acridinyl radical; $\mathrm{Ru}^{3+}$ oxidizes the acridinyl radical to the acridinium and regenerates the catalyst. (b) In reductive quenching the first step has $\Delta G \approx 0.80 - 0.77 = +0.03\,\mathrm{eV}$ and the second $+0.13\,\mathrm{eV}$ but is made irreversible by cleavage of the $\ce{C-Br}$ bond, so it is feasible; in oxidative quenching the first step has $\Delta G = -0.81 - (-1.46) = +0.65\,\mathrm{eV}$ and is not feasible. (c) It supports reductive quenching. (d) $\Phi > 1$ indicates a radical chain: for example the acridinyl radical (a strong reductant) reduces another molecule of the bromo ketone directly, so that each photon starts several conversions; the photocatalyst then serves only as an initiator.

9. Use **Faraday's laws of electrolysis** to calculate how long a constant current of $5\,\mathrm{mA}$ must flow, in theory, to electrolyze 0.30 mmol of an amide substrate (net transfer of 2 electrons per molecule). If the reaction actually needs 6 h to go to completion, what is the **current efficiency**?

   **Answer** $Q = nzF = 0.30\times10^{-3}\times2\times96485 = 57.9\,\mathrm{C}$ and $t = Q/I = 57.9/0.005 = 1.16\times10^4\,\mathrm{s} = 3.2\,\mathrm{h}$. The charge actually passed is $0.005\times6\times3600 = 108\,\mathrm{C}$, so the current efficiency is $57.9/108 = 54\%$: the actual consumption is about 3.7 F/mol, about 1.7 F/mol more than the theoretical 2 F/mol, and the excess charge is spent on shuttling of the mediator and on side reactions of the solvent and electrolyte.

10. Compare direct electrolysis with indirect electrolysis mediated by ferrocene for oxidizing an $N$-aryl carbamate. Why is the latter milder toward other electron-rich groups in the molecule (such as a $p$-methoxyphenyl group)? What condition must the potential of the mediator satisfy?

    **Answer** Direct electrolysis requires the **electrode potential** to reach the oxidation potential of the substrate itself (often above $+1.5\,\mathrm{V}$), at which other easily oxidized groups are also oxidized, and the electrode surface is easily passivated by polymerization of radical cations. In indirect electrolysis the electrode need only oxidize ferrocene (about $+0.4\,\mathrm{V}$ vs SCE), and $\ce{Fc+}$ is a mild one-electron oxidant that can oxidize only species with lower potentials, namely the deprotonated amide anion (whose oxidation potential is far below that of the neutral amide); electron-rich arenes that are not deprotonated are not oxidized. The oxidized form of the mediator must be able to oxidize the target intermediate (or do so fast enough, driven by a subsequent irreversible step), its potential must be below that of the groups that are not to be oxidized, and it must be redox-reversible with both states stable.

11. Estimate with the Bell model: a ring-opening reaction has a **Gibbs energy of activation** of $110\,\mathrm{kJ\,mol^{-1}}$ and $\Delta x^\ddagger = 0.05\,\mathrm{nm}$. By what factor does the rate constant increase at $25\,^\circ\mathrm{C}$ under a force of $1.5\,\mathrm{nN}$?

    **Answer** $F\Delta x^\ddagger = 1.5\times10^{-9}\times0.05\times10^{-9} = 7.5\times10^{-20}\,\mathrm{J}$, which multiplied by $N_{\mathrm{A}}$ gives $45\,\mathrm{kJ\,mol^{-1}}$. $k(F)/k_0 = \exp(7.5\times10^{-20}/(1.381\times10^{-23}\times298.15)) = \exp(18.2) \approx 8\times10^{7}$. The barrier falls from $110$ to about $65\,\mathrm{kJ\,mol^{-1}}$, so a reaction whose half-life at room temperature is measured in years can be completed within seconds under tension.
