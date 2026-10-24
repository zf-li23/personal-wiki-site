---
title: Radical Reactions
description: The structure of organic radicals (planar and pyramidal, σ radicals, heteroatom radicals, radical ions and the SOMO); generation of radicals (homolysis and initiators, single electron transfer, photoredox); stability and bond dissociation energies (hyperconjugation, conjugation, heteroatoms, persistent radicals); autoxidation of ethers and lipid peroxidation; lifetimes and electron paramagnetic resonance; the five elementary steps and radical clocks; the chain mechanism of alkane halogenation, the thermodynamics of the different halogens, regioselectivity and the Hammond postulate, steric control; allylic and benzylic bromination with NBS; combustion, partial oxidation and cracking of alkanes, and ring opening of small rings.
source_hash: 3c1809c79ba5
---

Most of the reactions in the preceding chapters were polar: bonds break heterolytically, and electrons flow in pairs from a **nucleophile** to an **electrophile**. This chapter deals with the other great class of reactions, in which bonds break homolytically, each fragment taking away one electron to give a species with an unpaired electron, a **radical** (defined in [6.3.15](/6.3.15#sec-15.7.1)), and the reaction is passed on from one radical to the next. The three classes of organic reactions compare as follows:

| Type | How bonds break | Intermediates | Typical conditions |
|---|---|---|---|
| Radical reactions | Homolysis | Radicals | Light, heat, initiators |
| Ionic (polar) reactions | Heterolysis | Cations, anions | Acids, bases, polar solvents |
| Concerted reactions | Bond making and bond breaking occur simultaneously | None | Light or heat ([6.5.12](/6.5.12)) |

Alkanes have no functional groups, and their $\ce{C-H}$ and $\ce{C-C}$ bonds are nearly nonpolar, so they hardly undergo ionic reactions; their chemistry is mainly radical chemistry (halogenation, combustion and cracking), and for this reason the reactions of alkanes are treated in this chapter as well. Radical chemistry is also found far beyond organic chemistry. The kinetics of chain reactions was treated in physical chemistry ([6.3.15](/6.3.15#sec-15.7)), and here we look at it again from the viewpoint of structure and selectivity. More than half of all polymerization in the polymer industry is radical polymerization. In living systems the oxidation of drugs by cytochrome P450 and the synthesis of DNA building blocks by ribonucleotide reductase proceed through radical intermediates, and lipid peroxidation and DNA damage caused by reactive oxygen species are part of the chemical basis of aging and many diseases. Radical reactions driven by light and electricity are treated in [6.5.31](/6.5.31).

## 7.1. Structure and Types of Radicals

### 7.1.1. Discovery

In 1900 Gomberg tried to remove chlorine from triphenylmethyl chloride, $\ce{Ph3CCl}$, with zinc (or silver) in order to make hexaphenylethane, $\ce{Ph3C-CPh3}$. He obtained a white solid whose benzene solution was yellow, which reacted rapidly with oxygen in the air to give the peroxide $\ce{Ph3COOCPh3}$ and with iodine to give $\ce{Ph3CI}$. Gomberg proposed that the solution contained the triphenylmethyl radical $\ce{Ph3C.}$ with a trivalent carbon, the first organic radical to be identified. The dogma that "carbon is always tetravalent" was shaken, and radical chemistry was born.

Curiously, the white solid was not hexaphenylethane: six phenyl groups are too bulky, and the two central carbons of the two trityl groups cannot bond to each other. In 1968 Lankamp, Nauta and MacLean showed by NMR that it is a quinoid dimer, in which the central carbon of one trityl group is bonded to the para carbon of a phenyl ring of the other; in solution it dissociates partially into radicals:

```smiles
C1=CC(C=CC1=C(c2ccccc2)c3ccccc3)C(c4ccccc4)(c5ccccc5)c6ccccc6
```

![Formation of Gomberg's dimer. The central carbons of two triphenylmethyl radicals are too hindered to bond; instead the central carbon of one radical pairs with the para carbon of another, where the unpaired electron is also found (resonance form on the right), giving the quinoid dimer, which partly dissociates back into the radicals in solution](./plots/gomberg-dimer.py)

### 7.1.2. Structure of Carbon Radicals

The central carbon of the methyl radical $\ce{.CH3}$ has 7 valence electrons: three bonding pairs and one unpaired electron. According to VSEPR theory and the concept of **hybrid orbitals**, the radical is trigonal planar, the carbon is $\mathrm{sp}^2$ hybridized, and the unpaired electron occupies a p orbital perpendicular to the molecular plane.

**Definition 7.1.1 (Singly Occupied Molecular Orbital)** The molecular orbital of a radical that holds only one electron is called the **singly occupied molecular orbital** (SOMO).

The energy and shape of the SOMO determine the reactivity of the radical, and it plays the part of the **highest occupied molecular orbital** and **lowest unoccupied molecular orbital** of a closed-shell molecule: it can either accept an electron or donate one. A carbon radical is best understood as lying between a **carbocation** (6 valence electrons, planar, empty p orbital) and a **carbanion** (8 valence electrons, pyramidal, lone pair in an $\mathrm{sp}^3$ orbital):

- Simple alkyl radicals are nearly planar. The methyl radical is planar; the ethyl and *tert*-butyl radicals are slightly pyramidal, but the barrier to inversion is only a few $\mathrm{kJ\,mol^{-1}}$ and they invert extremely rapidly at room temperature, so on average they are planar. A stereogenic carbon that becomes a radical therefore loses its stereochemical information: chlorination of (S)-1-chloro-2-methylbutane at C2 gives racemic 1,2-dichloro-2-methylbutane, because $\ce{Cl2}$ attacks the planar radical with equal probability from the two faces.
- Radicals bearing electronegative atoms are pyramidal: $\ce{.CF3}$ is distinctly pyramidal, because F gives the bonding orbitals on carbon more p character, and the orbital containing the unpaired electron correspondingly gains s character.
- Radicals that hold the unpaired electron in a $\sigma$ orbital are called $\sigma$ radicals. In the vinyl, phenyl and acyl radicals the unpaired electron is in an $\mathrm{sp}^2$ orbital in the molecular plane, orthogonal to the $\pi$ system and unable to be delocalized by it, so these radicals are much more reactive than alkyl radicals (the corresponding $\ce{C-H}$ bonds are stronger, Section 7.3).

![Radical chlorination at a stereocenter. A chlorine atom abstracts the tertiary hydrogen at C2 of (S)-1-chloro-2-methylbutane, giving a radical that is planar on average, with the unpaired electron in a p orbital; Cl₂ transfers a chlorine atom to the top and bottom faces with equal probability, giving equal amounts of (R)- and (S)-1,2-dichloro-2-methylbutane (a racemate)](./plots/radical-racemization.py)

Heteroatom radicals have the unpaired electron mainly on N, O, S and similar atoms, as in the alkoxyl radical $\ce{RO.}$, the hydroxyl radical $\ce{.OH}$, the thiyl radical $\ce{RS.}$, the aminyl radical $\ce{R2N.}$, nitroxides $\ce{R2N-O.}$ (such as TEMPO) and the phenoxyl radical $\ce{PhO.}$.

**Definition 7.1.2 (Radical Ion)** A species that carries both an unpaired electron and a charge is called a **radical ion**; it may be a radical cation (formed by removal of an electron from a neutral molecule, such as the molecular ion $\mathrm{M}^{+\bullet}$ in mass spectrometry) or a radical anion (formed by addition of an electron to a neutral molecule).

In a radical cation the electron that was lost came from the HOMO of the neutral molecule, which becomes the SOMO; in a radical anion the electron gained enters the former LUMO. Reduction of benzophenone with sodium metal gives the deep blue benzophenone ketyl radical anion, which is decolorized at once by water or oxygen, so "sodium–benzophenone" is used as an indicator in the preparation of anhydrous, oxygen-free tetrahydrofuran and diethyl ether: a solution that stays blue is dry and free of oxygen. Reduction of naphthalene with sodium gives the dark green naphthalene radical anion, a widely used single-electron reducing agent.

```smiles
[Na+].[O-][C](c1ccccc1)c2ccccc2
```

![Formation of the benzophenone ketyl. Sodium gives one electron (fishhook arrow); it pairs on oxygen with one electron of the C=O pi bond as a lone pair, and the other pi electron stays on carbon, giving a radical anion with the negative charge on oxygen and the unpaired electron on carbon](./plots/ketyl.py)

## 7.2. Generation of Radicals

### 7.2.1. Homolysis

**Definition 7.2.1 (Homolysis and Heterolysis)** The cleavage of a covalent bond in which the bonding pair of electrons is divided equally between the two fragments to give two radicals is called **homolysis**; cleavage in which the bonding pair goes entirely to one fragment to give a pair of oppositely charged ions is called **heterolysis**.

$$
\ce{A-B -> A. + .B},\qquad \ce{A-B -> A+ + :B-}.
$$
The former is homolysis and the latter heterolysis. There are accordingly two kinds of **curly arrow** for showing electron movement ([6.5.1](/6.5.1#def-1.2.2)): a full arrowhead shows the movement of an electron pair, and a half arrowhead, the **fishhook arrow**, shows the movement of a single electron. In homolysis two fishhook arrows are drawn from the midpoint of the bond, one to each atom.

**Definition 7.2.2 (Bond Dissociation Energy)** The standard molar enthalpy change for homolysis of a specified bond of one mole of molecules in the gas phase to give two radicals (or atoms) is called the **bond dissociation energy** (bond dissociation enthalpy, BDE) of that bond and is denoted $D(\ce{A-B})$:

$$
D(\ce{A-B}) = \Delta_{\mathrm{f}}H^\circ(\ce{A.}) + \Delta_{\mathrm{f}}H^\circ(\ce{B.}) - \Delta_{\mathrm{f}}H^\circ(\ce{A-B}),
\tag{7.1}
$$
usually at $298\,\mathrm{K}$.

The bond dissociation energy differs from the mean **bond energy** of inorganic chemistry ([6.1.3](/6.1.3)), which is the average over bonds of the same kind in a polyatomic molecule; the BDE is the energy needed to break one specific bond, and bonds of the same kind in one molecule can differ widely (the BDEs for breaking the four $\ce{C-H}$ bonds of $\ce{CH4}$ in succession are all different). BDEs in the literature are mostly given in $\mathrm{kcal\,mol^{-1}}$ ($1\,\mathrm{kcal} = 4.184\,\mathrm{kJ}$); this wiki converts all of them to $\mathrm{kJ\,mol^{-1}}$. The data used in this chapter ($298\,\mathrm{K}$, from Luo's handbook of bond energies and the review by Blanksby and Ellison) are:

| Bond | $D$ / $(\mathrm{kJ\,mol^{-1}})$ | Bond | $D$ / $(\mathrm{kJ\,mol^{-1}})$ | Bond | $D$ / $(\mathrm{kJ\,mol^{-1}})$ |
|---|---|---|---|---|---|
| $\ce{CH3-H}$ | $439$ | $\ce{CH2=CH-H}$ (vinylic) | $463$ | $\ce{H-F}$ | $570$ |
| $\ce{CH3CH2-H}$ (primary) | $423$ | $\ce{C6H5-H}$ (phenyl) | $472$ | $\ce{H-Cl}$ | $432$ |
| $\ce{(CH3)2CH-H}$ (secondary) | $413$ | $\ce{HC#C-H}$ | $558$ | $\ce{H-Br}$ | $366$ |
| $\ce{(CH3)3C-H}$ (tertiary) | $404$ | $\ce{CH3C(O)-H}$ (aldehydic) | $374$ | $\ce{H-I}$ | $298$ |
| $\ce{CH2=CHCH2-H}$ (allylic) | $372$ | $\ce{HOCH2-H}$ | $402$ | $\ce{F-F}$ / $\ce{Cl-Cl}$ | $159$ / $243$ |
| $\ce{C6H5CH2-H}$ (benzylic) | $375$ | $\ce{HO-H}$ | $497$ | $\ce{Br-Br}$ / $\ce{I-I}$ | $193$ / $151$ |
| $\ce{(C6H5)3C-H}$ | about $339$ | $\ce{CH3O-H}$ | $438$ | $\ce{CH3-F}$ / $\ce{CH3-Cl}$ | about $460$ / $350$ |
| $\ce{C-H}$ of cyclohexa-1,4-diene | $318$ | $\ce{C6H5O-H}$ | about $363$ | $\ce{CH3-Br}$ / $\ce{CH3-I}$ | $294$ / $239$ |
| $\ce{CH3-CH3}$ | $377$ | $\ce{HO-OH}$ / $\ce{(CH3)3CO-OC(CH3)3}$ | $211$ / about $159$ | $\ce{H-H}$ | $436$ |

The energy for homolysis comes from heat or light. The BDEs of $\ce{C-H}$ and $\ce{C-C}$ bonds are $350$–$450\,\mathrm{kJ\,mol^{-1}}$, and appreciable homolysis requires temperatures of several hundred degrees Celsius (cracking of alkanes, Section 7.9.2). The bonds of the halogen molecules are much weaker, and visible or ultraviolet light dissociates them ($\ce{Cl2}$ absorbs at about $330\,\mathrm{nm}$, a photon energy of about $360\,\mathrm{kJ\,mol^{-1}}$), which is the initiation step of halogenation under illumination.

### 7.2.2. Radical Initiators

**Definition 7.2.3 (Radical Initiator)** A compound that contains a particularly weak bond, undergoes homolysis under mild heating or illumination to give radicals, and is used to start radical chain reactions is called a **radical initiator**.

There are two common kinds:

- **Azo compounds**. The $\ce{C-N}$ bonds of azobisisobutyronitrile (AIBN) are not weak in themselves, but homolysis releases the very stable $\ce{N2}$ and at the same time gives two tertiary carbon radicals stabilized by the cyano group; both the enthalpy and the entropy of the reaction are favorable, and AIBN decomposes at a convenient rate at $60$–$80\,^\circ\mathrm{C}$.
- Peroxides. The $\ce{O-O}$ bond is only about $150\,\mathrm{kJ\,mol^{-1}}$. Dibenzoyl peroxide (BPO) cleaves into two benzoyloxyl radicals, which can lose $\ce{CO2}$ to give phenyl radicals; the $\ce{O-O}$ bonds of di-*tert*-butyl peroxide and *tert*-butyl hydroperoxide (TBHP) are somewhat stronger and need higher temperatures.

![Three homolyses that generate radicals (fishhook arrows show the movement of single electrons): (1) light or heat dissociates Cl₂ into two chlorine atoms; (2) AIBN loses N₂ on heating to give two 2-cyanopropan-2-yl radicals; (3) dibenzoyl peroxide breaks at the weak O–O bond, and the benzoyloxyl radical then loses CO₂ to give a phenyl radical](./plots/radical-initiation.py)

The activity of initiators is often compared by the "ten-hour half-life temperature" (the temperature at which the half-life is $10\,\mathrm{h}$): about $65\,^\circ\mathrm{C}$ for AIBN, $73\,^\circ\mathrm{C}$ for BPO, $126\,^\circ\mathrm{C}$ for di-*tert*-butyl peroxide and $165\,^\circ\mathrm{C}$ for TBHP. If the initiator is chosen so that its half-life at the reaction temperature is a few hours, radicals are produced slowly and steadily throughout the reaction.

### 7.2.3. Single Electron Transfer

**Definition 7.2.4 (Single Electron Transfer)** The process in which one electron is transferred from a donor molecule to an acceptor molecule, so that they become a radical cation and a radical anion, respectively (or in which radicals are formed from ions), is called **single electron transfer** (SET).

Single electron transfer is a kind of **redox reaction**; it generates radicals without breaking any chemical bond, and the radical ions formed often fragment at once:

- Single-electron oxidation: a carboxylate loses one electron to give an acyloxyl radical, which rapidly undergoes **decarboxylation** to an alkyl radical, $\ce{RCOO- ->[-e^-] RCOO. -> R. + CO2}$. Coupling of two $\ce{R.}$ radicals in electrolysis is the Kolbe electrolysis ([6.5.18](/6.5.18#sec-18.4.2)); thiols, amines and electron-rich arenes are also readily oxidized by single electron transfer.
- Single-electron reduction: an aryl halide accepts one electron into its $\pi^*$ orbital to give a radical anion, which then loses a halide ion to give an aryl radical; the single-electron reduction of an alkyl halide, on the other hand, is often concerted with cleavage of the $\ce{C-X}$ bond (dissociative electron transfer), $\ce{R-Br ->[+e^-] R. + Br-}$. Sodium, lithium, samarium(II) and electrodes can all serve as electron donors.

![Kolbe electrolysis. Acetate loses one electron at the anode (single electron transfer) to give the acetoxyl radical; in the beta-scission the unpaired electron on oxygen and one electron of the C–CH₃ bond form the second C=O pi bond of CO₂, and the other electron leaves with the methyl group; two methyl radicals couple to ethane](./plots/kolbe-decarboxylation.py)

Light can greatly enhance the single-electron-transfer ability of a molecule: after a photon is absorbed, an electron is promoted to a higher orbital, and the excited molecule both gives up this high-energy electron more easily (it is a stronger reducing agent) and accepts an electron into the vacated low-energy orbital more easily (it is a stronger oxidizing agent). With $\ce{[Ru(bpy)3]^2+}$, iridium complexes or organic dyes as photocatalysts, visible light generates a wide variety of radicals gently at room temperature; this is photoredox catalysis, developed over the last two decades (the photophysics of excited states is in [6.3.17](/6.3.17) and the reactions are treated in detail in [6.5.31](/6.5.31)).

## 7.3. Stability of Radicals and Bond Dissociation Energies

### 7.3.1. Comparing Radical Stabilities by Bond Dissociation Energies

Removing a hydrogen atom from different positions of the same alkane gives different radicals and requires different amounts of energy. For propane, breaking a primary $\ce{C-H}$ bond to give the propyl radical takes about $423\,\mathrm{kJ\,mol^{-1}}$, whereas breaking a secondary $\ce{C-H}$ bond to give the isopropyl radical takes only $413\,\mathrm{kJ\,mol^{-1}}$. The two reactions start from the same molecule and give the same second product (the H atom), so the difference can only come from the energies of the two radicals: the isopropyl radical is about $10\,\mathrm{kJ\,mol^{-1}}$ lower in energy than the propyl radical, that is, more stable. The stability meant here is thermodynamic stability (low energy), which is different from the length of the radical's lifetime (kinetic stability, Section 7.3.4). The $\ce{C-H}$ bond dissociation energies in the table above give the general order of stability of carbon radicals:

$$
\ce{.CH3} < \text{primary} < \text{secondary} < \text{tertiary} < \text{allyl} \approx \text{benzyl}
$$
$\sigma$ radicals such as vinyl and phenyl are even less stable than methyl. Relative to methyl, primary, secondary and tertiary alkyl radicals are stabilized by about $16$, $26$ and $35\,\mathrm{kJ\,mol^{-1}}$, respectively, and allyl and benzyl by about $65\,\mathrm{kJ\,mol^{-1}}$.

It should be noted that the argument "the smaller the BDE, the more stable the radical" tacitly assumes that the energy differences between the $\ce{R-H}$ molecules compared are negligible. For primary, secondary and tertiary $\ce{C-H}$ bonds, branching of the alkane itself also stabilizes the molecule (Section 7.9.1), and some researchers therefore believe that the stabilizing effect of alkyl substitution on radicals is smaller than the BDEs suggest. The trends are also not entirely consistent when different bonds such as $\ce{R-H}$, $\ce{R-CH3}$ and $\ce{R-OH}$ are compared. For the reactivity and selectivity discussed in this chapter, however, the BDE is the quantity that actually matters.

### 7.3.2. Structural Factors That Stabilize Radicals

**Hyperconjugation** ([6.5.2](/6.5.2#def-2.6.1)). A $\ce{C-H}$ (or $\ce{C-C}$) $\sigma$ bond next to the radical center overlaps partly with the half-filled p orbital, and the $\sigma$ electrons can be delocalized into the p orbital. The two bonding $\sigma$ electrons and one p electron make up a three-electron system, in which two electrons enter the lowered bonding combination and one enters the slightly raised combination, so the net result is a lowering of energy. The more $\ce{C-H}$ bonds adjacent to the radical center, the greater this stabilization: the methyl radical has no bonds adjacent to the radical center other than its own, whereas the *tert*-butyl radical has nine adjacent $\ce{C-H}$ bonds. Direct experimental evidence for hyperconjugation comes from EPR: in the ethyl radical the hyperfine coupling constant of the $\beta$ hydrogens ($2.69\,\mathrm{mT}$) is even larger than that of the $\alpha$ hydrogens ($2.24\,\mathrm{mT}$), showing that the unpaired electron is indeed delocalized onto the $\beta$ $\ce{C-H}$ bonds (Section 7.4.2).

Conjugation. The unpaired electron of the allyl and benzyl radicals is conjugated with the adjacent $\pi$ system (p–$\pi$ conjugation) and delocalized over several carbons. In terms of **resonance structures**, the allyl radical is a hybrid of two equivalent resonance structures, with the unpaired electron shared equally between the two terminal carbons; in the benzyl radical the unpaired electron is spread over the methylene carbon and the ortho and para carbons of the ring. Delocalization makes an allylic $\ce{C-H}$ bond about $40\,\mathrm{kJ\,mol^{-1}}$ weaker than an ordinary secondary $\ce{C-H}$ bond. Likewise, a position that can conjugate with more than one $\pi$ bond is weaker still: the methylene group of cyclohexa-1,4-diene lies between two double bonds, the radical obtained by loss of a hydrogen is a five-carbon pentadienyl delocalized system, and the $\ce{C-H}$ bond is only $318\,\mathrm{kJ\,mol^{-1}}$; when this radical loses a further hydrogen atom the product is benzene, and the gain of **aromaticity** ([6.5.13](/6.5.13#sec-13.1.2)) weakens the second $\ce{C-H}$ bond to less than $100\,\mathrm{kJ\,mol^{-1}}$. Cyclohexa-1,4-diene is therefore an excellent hydrogen atom donor.

![Resonance structures of the benzyl radical. In the first structure the unpaired electron and one electron of a ring pi bond form the exocyclic C=C pi bond, and the other pi electron moves to the ortho carbon (fishhook arrows); the unpaired electron is shared by the CH₂ carbon and the two ortho and one para carbons of the ring](./plots/benzyl-resonance.py)

Heteroatoms. O and N at the $\alpha$ position stabilize a carbon radical. The BDE of the $\alpha$-$\ce{C-H}$ bond of tetrahydrofuran is about $385\,\mathrm{kJ\,mol^{-1}}$, smaller than that of cyclopentane (about $400$); the $\alpha$-$\ce{C-H}$ bond of pyrrolidine is about $377\,\mathrm{kJ\,mol^{-1}}$, and open-chain ethers and amines behave similarly. The reason is that the lone pair of the heteroatom (an n orbital) interacts with the half-filled p orbital of the radical: of the three electrons, two enter the lowered combination and one the raised combination, with net stabilization (a three-electron interaction). Before the bond breaks, the lone pair also interacts with the $\sigma^*$ orbital of the **antiperiplanar** $\ce{C-H}$ bond (a stereoelectronic effect), and this $\ce{C-H}$ bond is weakened as well. The lone pair of nitrogen is higher in energy than that of oxygen and closer in energy to the p orbital, so stabilization by an $\alpha$-amino group is the strongest. This is why $N$-aryl-1,2,3,4-tetrahydroisoquinolines are the most commonly used model substrates in photoredox reactions: C1 is both benzylic and $\alpha$ to nitrogen, and after single-electron oxidation it very easily loses a proton and an electron at this position to give an iminium ion.

```smiles
C1Cc2ccccc2CN1c3ccccc3
```

Electron-withdrawing conjugating groups such as carbonyl and cyano also stabilize radicals (the $\ce{C-H}$ of acetone is about $401\,\mathrm{kJ\,mol^{-1}}$), because the unpaired electron can be delocalized onto the carbonyl group. A radical bearing both a donor and an acceptor group is especially stable (the captodative effect). Substituents also change the energy of the SOMO and the "polarity" of the radical. Donor groups raise the SOMO, and such radicals (alkyl, $\alpha$-alkoxyalkyl and $\alpha$-aminoalkyl radicals) tend to donate electrons; they are called nucleophilic radicals and react readily with electron-poor alkenes. Acceptor groups lower the SOMO, and such radicals (such as $\ce{.CH2COR}$, $\ce{.CF3}$, halogen atoms and alkoxyl radicals) are called electrophilic radicals and attack electron-rich sites preferentially. This polar effect plays an important role in the selectivity of radical additions and hydrogen atom transfers.

### 7.3.3. Autoxidation of Ethers and Lipid Peroxidation

The $\ce{C-H}$ bonds at the $\alpha$ position of an oxygen atom are weak, so ethers undergo a slow radical chain reaction with oxygen in air.

**Definition 7.3.1 (Autoxidation)** The radical chain oxidation of an organic compound by atmospheric oxygen that proceeds spontaneously at room temperature is called **autoxidation**; propagation consists of two steps: a carbon radical combines with $\ce{O2}$ to give a peroxyl radical, and the peroxyl radical abstracts a hydrogen atom from another molecule to give a hydroperoxide and regenerate a carbon radical.

$$
\begin{aligned}
&\ce{R. + O2 -> ROO.}\\
&\ce{ROO. + R-H -> ROOH + R.}
\end{aligned}
$$
The first step has almost no barrier ($\ce{O2}$ is a triplet diradical). In the second step the BDE of $\ce{ROO-H}$ is about $365\,\mathrm{kJ\,mol^{-1}}$, so the step is fast enough only when a weaker $\ce{C-H}$ bond is abstracted (allylic, benzylic, $\alpha$ to the oxygen of an ether, or aldehydic). Diethyl ether, tetrahydrofuran and diisopropyl ether accumulate hydroperoxides and peroxides on long standing, and these explode when heated or struck; explosions when ether solvents are distilled almost to dryness are all too common. Ether solvents should therefore be stored away from light and with a stabilizer (such as BHT), and checked for peroxides with potassium iodide–starch paper before use.

![Chain propagation in the autoxidation of diethyl ether. Top: the unpaired electron of the α-ethoxyethyl radical pairs with one of the unpaired electrons of triplet O₂, giving a peroxyl radical. Bottom: the peroxyl radical abstracts the weak α C–H hydrogen of another ether molecule (hydrogen atom transfer), giving the hydroperoxide and regenerating the α-ethoxyethyl radical, which carries the chain](./plots/ether-autoxidation.py)

The same chemistry takes place in cell membranes. In polyunsaturated fatty acids (such as linoleic and arachidonic acids) the methylene group between two double bonds, like that of cyclohexa-1,4-diene, has $\ce{C-H}$ bonds of only about $320\,\mathrm{kJ\,mol^{-1}}$ and is the position most easily attacked by reactive oxygen species. The pentadienyl radical formed combines with oxygen and starts a series of peroxidation chain reactions (lipid peroxidation) that damage the membrane structure; products such as malondialdehyde can also modify proteins and DNA. One line of defense in living organisms is the fat-soluble vitamin E ($\alpha$-tocopherol): its phenolic $\ce{O-H}$ bond is also weak (about $325\,\mathrm{kJ\,mol^{-1}}$, close to the bisallylic $\ce{C-H}$), but what matters is kinetics: transfer of the O–H hydrogen atom has a low intrinsic barrier, so it donates its hydrogen atom to a peroxyl radical much faster than the fatty acid propagates the chain, and the phenoxyl radical formed is stabilized by conjugation with the ring and by the ortho methyl groups and cannot continue the chain, so the chain is "broken". Phenolic antioxidants such as BHT, added to foods and plastics, work on the same principle. These topics are taken up again in biochemistry.

![Lipid peroxidation. Top: a peroxyl radical LOO• abstracts a hydrogen atom from the bis-allylic CH₂ group of a linoleate chain (C–H only about 320 kJ/mol); the resulting pentadienyl radical is delocalized over C1, C3 and C5. Bottom: O₂ adds at a terminal carbon, giving a peroxyl radical with a conjugated diene, which abstracts the next bis-allylic hydrogen and carries the chain](./plots/lipid-peroxidation.py)

![Chain breaking by vitamin E. The lipid peroxyl radical LOO• abstracts the hydrogen atom of the phenolic O–H group of α-tocopherol (the unpaired electron and one O–H electron form the new O–H bond; the other electron stays on the phenolic oxygen), giving the lipid hydroperoxide LOOH and the tocopheroxyl radical, which is delocalized over the ring, protected by the ortho methyl groups and does not carry the chain](./plots/tocopherol-hat.py)

### 7.3.4. Persistent and Stable Radicals

The lifetime of a radical depends on the rate at which it disappears, and not only on its thermodynamic stability.

**Definition 7.3.2 (Persistent Radical)** A radical whose lifetime under ordinary conditions is much longer (minutes, days or even longer) than that of simple alkyl radicals such as methyl is called a **persistent radical**; its long life derives mainly from kinetic factors, above all steric hindrance that prevents the radicals from coupling with one another. A persistent radical that can be isolated and stored like an ordinary compound is called a stable radical.

The triphenylmethyl radical is stabilized by conjugation and, because of the steric hindrance of the three phenyl rings (which are twisted in a propeller shape), dimerizes with difficulty; in solution it is in equilibrium with its quinoid dimer. The pentaarylcyclopentadienyl radical and the Koelsch radical (1,3-bisbiphenylene-2-phenylallyl) are further examples. A radical stabilized only by steric hindrance, with almost no conjugation, can also be persistent: a carbon radical surrounded by several trimethylsilyl groups can exist for days in dilute solution at room temperature, whereas the methyl radical has a half-life of only about $20\,\mu\mathrm{s}$ under the same conditions.

The most important stable radicals are the nitroxides. In 2,2,6,6-tetramethylpiperidin-1-oxyl (TEMPO) the unpaired electron is delocalized over $\ce{N-O}$ (a three-electron $\pi$ bond), and the four $\alpha$-methyl groups prevent dimerization and elimination of an $\alpha$-H; it is an orange-red solid that can be bought and weighed. TEMPO is used as a radical trap (to test whether a reaction goes through radical intermediates), as a catalyst for the selective oxidation of alcohols, and as a spin label for EPR. Other common stable radicals are 2,2-diphenyl-1-picrylhydrazyl (DPPH, used to measure antioxidant capacity) and galvinoxyl.

```smiles
CC1(C)CCCC(C)(C)N1[O] TEMPO
```

## 7.4. Lifetimes of Radicals and Electron Paramagnetic Resonance

### 7.4.1. Why Radicals Are Short-Lived

Most radicals are highly reactive. The main ways in which they disappear are coupling (or disproportionation) of two radicals to give stable molecules, a reaction with almost no barrier and a rate constant of $10^9$–$10^{10}\,\mathrm{L\,mol^{-1}\,s^{-1}}$, close to diffusion control, and reaction with molecules in the environment, such as combination with oxygen or abstraction of a hydrogen atom from the solvent. The rapid disappearance of radicals by mutual coupling is the greatest difference between radicals and ionic intermediates such as **carbocations** and carbanions: two cations repel each other and do not combine. The concentration of radicals in a radical reaction is therefore always low (typically $10^{-8}$–$10^{-6}\,\mathrm{mol\,L^{-1}}$), and observing them directly requires a sensitive and specific method.

### 7.4.2. Electron Paramagnetic Resonance

An unpaired electron has a spin magnetic moment and, like a nucleus, can undergo magnetic resonance in a magnetic field. The method responds only to species containing unpaired electrons (radicals, triplet molecules, many transition-metal ions), so it is particularly suited to detecting radicals without interference from the large amount of closed-shell molecules.

**Definition 7.4.1 (Electron Paramagnetic Resonance)** The phenomenon in which a substance containing unpaired electrons, placed in a static magnetic field $B$, has the two states of the electron spin ($m_s = \pm\frac12$) split in energy and absorbs microwave radiation satisfying the resonance condition

$$
h\nu = g\mu_{\mathrm{B}}B
\tag{7.2}
$$
to make transitions between the two levels is called **electron paramagnetic resonance** (EPR, also called electron spin resonance, ESR); here $\mu_{\mathrm{B}}$ is the Bohr magneton, and the dimensionless proportionality factor $g$ is called the **g-factor**.

EPR works on the same principle as NMR ([6.4.12](/6.4.12)); the magnetic moment of the electron is about $660$ times that of the proton, so the resonance frequency in the same field is much higher: the commonly used X-band spectrometer operates at about $0.34\,\mathrm{T}$ and $9.5\,\mathrm{GHz}$, and the transition energy is only about $4\,\mathrm{J\,mol^{-1}}$. For the free electron $g = 2.0023$; the $g$ values of organic radicals lie between $2.002$ and $2.006$, the deviation from the free-electron value reflecting spin–orbit coupling (radicals containing heavy atoms such as S deviate more), so the $g$ value plays the part of the chemical shift in NMR. EPR spectrometers hold the microwave frequency fixed, sweep the magnetic field, and use field modulation to record the first derivative of the absorption curve, so a line appears as one peak above and one below the baseline, with the center (where the derivative is zero) corresponding to the absorption maximum.

**Definition 7.4.2 (Hyperfine Coupling)** The splitting of EPR lines caused by the magnetic interaction of the unpaired electron with nearby magnetic nuclei ($I \ne 0$) is called **hyperfine coupling**; the spacing between adjacent lines is the hyperfine coupling constant $a$, usually given in $\mathrm{mT}$.

The pattern of hyperfine splitting is the same as that of coupling in NMR ([6.4.12](/6.4.12#sec-12.3.2)): an unpaired electron coupled to $n$ equivalent nuclei of spin $I$ gives $2nI + 1$ lines, whose intensities for $I = \frac12$ nuclei are in the ratio of binomial coefficients. The methyl radical couples to three equivalent protons and gives a quartet with intensity ratio $1:3:3:1$ and $a(\mathrm{H}) = 2.30\,\mathrm{mT}$; the unpaired electron of a nitroxide couples to one $^{14}\mathrm{N}$ ($I = 1$) and gives a $1:1:1$ triplet (for TEMPO $a(\mathrm{N}) \approx 1.6\,\mathrm{mT}$); the ethyl radical couples to 2 $\alpha$-H and 3 $\beta$-H with different values of $a$ and splits into $3\times4 = 12$ lines. From the number, spacing and intensity ratio of the lines one can therefore deduce which magnetic nuclei surround the unpaired electron and how many there are, and thereby the structure of the radical.

![Simulated X-band EPR spectra (first derivative of absorption). Left: absorption curve and first derivative of a single line; center: methyl radical coupled to three equivalent protons, a(H) = 2.30 mT, 1:3:3:1; right: nitroxide coupled to one ¹⁴N (I = 1), 1:1:1](./plots/epr-spectra.py)

In $\pi$ radicals the coupling constant of a proton attached to a carbon is approximately proportional to the unpaired-electron density (spin density) $\rho$ on that carbon, $a(\mathrm{H}) \approx Q\rho$, with $\lvert Q\rvert \approx 2.3\,\mathrm{mT}$ (the McConnell relation). In the benzene radical anion the unpaired electron is spread evenly over the six carbons ($\rho = 1/6$), and the observed $a(\mathrm{H}) = 0.375\,\mathrm{mT}$ agrees with $2.3/6 = 0.38\,\mathrm{mT}$. EPR is thus a direct test of molecular-orbital calculations.

Radicals whose lifetimes are too short and whose concentrations are too low for direct observation can be detected with "spin traps" (such as 5,5-dimethyl-1-pyrroline $N$-oxide, DMPO, and phenyl *tert*-butyl nitrone, PBN), which add rapidly to them to form stable nitroxides; the radical that was trapped is deduced from the hyperfine structure of the adduct. This *spin trapping* is used to detect the superoxide anion and the hydroxyl radical in biological systems. Introducing a nitroxide at a specific position of a protein as a "spin label" and measuring the dipolar coupling between two labels also gives distances of $2$–$8\,\mathrm{nm}$, a common method for studying conformational changes of membrane proteins.

## 7.5. Elementary Steps of Radical Reactions

In radical reactions electrons move one at a time, shown by **fishhook arrows**; in ionic reactions electrons move in pairs, shown by full curly arrows. The multitude of radical reactions can all be broken down into five elementary steps (two pairs of which are the reverse of each other):

1. Homolysis: a single bond absorbs energy and cleaves into two radicals (Section 7.2).
2. Coupling: the unpaired electrons of two radicals pair up to form a covalent bond, the reverse of homolysis. Competing with coupling is disproportionation, in which one radical abstracts a hydrogen atom from the $\beta$ position of another to give an alkane and an alkene ($\ce{2CH3CH2. -> CH3CH3 + CH2=CH2}$).
3. Addition: a radical adds to one end of a $\pi$ bond, leaving the other electron of the $\pi$ bond at the other end to form a new radical.
4. Elimination ($\beta$-scission): the reverse of addition, see below.
5. Atom transfer: a radical abstracts an atom (usually H or a halogen) from another molecule, giving a new molecule and a new radical.

![Two ways in which two ethyl radicals destroy each other. Top: coupling, the two unpaired electrons pair to form the new C–C bond of butane. Bottom: disproportionation, the left radical abstracts a hydrogen atom from the β position of the right one: the unpaired electron and one electron of the C–H bond form the new C–H bond, and the other C–H electron pairs with the unpaired electron of the right radical to form the new pi bond, giving ethane and ethene](./plots/disproportionation.py)

**Definition 7.5.1 (Hydrogen Atom Transfer)** The elementary reaction $\ce{X. + H-R -> X-H + .R}$, in which a radical $\ce{X.}$ reacts with $\ce{R-H}$, the $\ce{R-H}$ bond undergoes homolysis, a hydrogen atom is transferred to X and a new radical $\ce{R.}$ is formed, is called **hydrogen atom transfer** (HAT, also called hydrogen abstraction).

Similarly, $\ce{R. + X-X -> R-X + X.}$ is called halogen atom transfer. The enthalpy change of an atom transfer is determined by the difference between the BDEs of the bond broken and the bond formed: $\Delta H = D(\ce{R-H}) - D(\ce{X-H})$. If the bond formed is stronger than the bond broken, the reaction is exothermic.

**Definition 7.5.2 (β-Scission)** The unimolecular reaction in which a bond at the $\beta$ position of the radical center undergoes homolysis, one electron forming a $\pi$ bond with the unpaired electron of the radical center and the other going with the departing fragment to form a new radical, is called **β-scission**.

The decarboxylation of the benzoyloxyl radical (Section 7.2.2) and the fragmentation of an alkoxyl radical into a carbonyl compound and an alkyl radical ($\ce{(CH3)3CO. -> (CH3)2C=O + .CH3}$) are both $\beta$-scissions.

![Beta-scission of the tert-butoxyl radical. The unpaired electron on oxygen and one electron of a C–CH₃ bond form the C=O pi bond of acetone, and the other electron of that bond leaves with the methyl radical](./plots/alkoxyl-beta-scission.py)

![Elementary steps of radicals (one fishhook arrow represents one electron). (1) Hydrogen atom transfer: a chlorine atom abstracts a hydrogen atom from methane; (2) halogen atom transfer: a methyl radical abstracts a chlorine atom from Cl₂; (1) and (2) together are the propagation of the chlorination of methane; (3) a methyl radical adds to ethene, and the reverse is β-scission](./plots/elementary-steps.py)

The rate constants of unimolecular radical rearrangements have often been measured accurately and can serve as "clocks":

| Rearrangement | $k$ ($25\,^\circ\mathrm{C}$) / $\mathrm{s^{-1}}$ |
|---|---|
| Hex-5-enyl radical → cyclopentylmethyl radical (intramolecular addition, 5-exo cyclization) | $2.3\times10^5$ |
| Cyclopropylmethyl radical → but-3-enyl radical (ring opening, $\beta$-scission) | $9.4\times10^7$ |

```smiles
[CH2]CCCC=C>>[CH2]C1CCCC1
[CH2]C1CC1>>[CH2]CC=C
```

![The two reference reactions of radical clocks. Top: 5-exo cyclization of the 5-hexenyl radical; the unpaired electron on C1 and one electron of the C5=C6 pi bond form the C1–C5 bond, and the other pi electron stays on C6, giving the cyclopentylmethyl radical. Bottom: ring opening of the cyclopropylmethyl radical (beta-scission of a ring bond); the unpaired electron and one electron of the C2–C3 bond form the C1=C2 pi bond, and the other electron goes to C3, giving the 3-butenyl radical](./plots/radical-clock.py)

If a substrate containing a hex-5-enyl or cyclopropylmethyl group is placed in the reaction under study, and a cyclized or ring-opened structure appears in the product, the reaction goes through a radical intermediate whose lifetime is comparable to or longer than $1/k$ in the table. This method is called the *radical clock* and is widely used to study the mechanisms of enzymatic and metal-catalyzed reactions. The ring opening of the cyclopropylmethyl radical is extremely fast because the strain of the three-membered ring (about $115\,\mathrm{kJ\,mol^{-1}}$, [6.5.4](/6.5.4#sec-4.4.1)) is released on ring opening.

## 7.6. The Chain Mechanism of Alkane Halogenation

A mixture of methane and chlorine does not react in the dark at room temperature; irradiated with ultraviolet light or heated to $250$–$400\,^\circ\mathrm{C}$ it reacts quickly to give chloromethane and hydrogen chloride, together with polychlorinated products such as dichloromethane, trichloromethane and tetrachloromethane (all important industrial chemicals):

$$
\ce{CH4 + Cl2 ->[h\nu] CH3Cl + HCl}.
$$
The experimental facts are: (1) the reaction needs light or heat to start it; (2) once started, it continues for some time even after the illumination is stopped, and each photon absorbed can produce thousands of $\ce{CH3Cl}$ molecules; (3) a small amount of ethane is formed as a by-product; (4) a small amount of oxygen prevents the reaction from proceeding during an induction period. All these facts point to a **chain reaction** ([6.3.15](/6.3.15#def-15.7.1)).

**Chain initiation**: the $\ce{Cl2}$ bond is the weakest ($243\,\mathrm{kJ\,mol^{-1}}$) and cleaves homolytically in light; the $\ce{C-H}$ bond of methane ($439$) does not break under these conditions.

$$
\ce{Cl2 ->[h\nu] 2Cl.}\qquad\Delta H = +243\,\mathrm{kJ\,mol^{-1}}
$$

**Chain propagation**: hydrogen atom transfer between a chlorine atom and methane, followed by halogen atom transfer between the methyl radical and chlorine, which regenerates the chlorine atom:

$$
\begin{aligned}
&\ce{Cl. + CH4 -> HCl + .CH3} && \Delta H = 439 - 432 = +7\,\mathrm{kJ\,mol^{-1}}\\
&\ce{.CH3 + Cl2 -> CH3Cl + Cl.} && \Delta H = 243 - 350 = -107\,\mathrm{kJ\,mol^{-1}}
\end{aligned}
$$
The two steps add up exactly to the overall reaction, with $\Delta H = -100\,\mathrm{kJ\,mol^{-1}}$ (the exact value calculated from enthalpies of formation is $-99.6\,\mathrm{kJ\,mol^{-1}}$). The chlorine atom consumed in the first step is regenerated in the second, and the chain is passed on link by link.

**Chain termination**: two radicals couple:

$$
\ce{2Cl. -> Cl2},\qquad \ce{2.CH3 -> CH3CH3},\qquad \ce{.CH3 + Cl. -> CH3Cl}.
$$
Coupling of methyl radicals accounts for the ethane by-product; the combination of oxygen with the methyl radical to give a far less reactive peroxyl radical interrupts the chain and accounts for the inhibiting effect of oxygen. The $\ce{CH3Cl}$ formed has $\ce{C-H}$ bonds of its own and can be attacked by chlorine atoms in turn, so the product is a mixture of polychlorinated compounds; a large excess of methane makes the monochloro compound the main product.

![Chain termination in methane chlorination: two radicals meet and their unpaired electrons pair to form a bond (each fishhook arrow is one electron). Left: a chlorine atom and a methyl radical give chloromethane. Right: O₂, a triplet diradical, traps a methyl radical as the much less reactive methylperoxyl radical, which explains the induction period caused by traces of oxygen](./plots/termination.py)

Why is the main course of the reaction chain propagation when termination releases far more heat ($-243$, $-377$ and $-350\,\mathrm{kJ\,mol^{-1}}$)? The rate is determined not by the heat released but by the concentrations of the reactants: termination requires two radicals to meet, whereas the radical concentration is extremely low ($\sim 10^{-8}\,\mathrm{mol\,L^{-1}}$) and the concentrations of methane and chlorine are more than $10^6$ times larger. A chlorine atom collides with methane molecules thousands of times before it meets another radical. The number of propagation cycles (the chain length) can exceed $10^4$. Applying the **steady-state approximation** ([6.3.15](/6.3.15#def-15.6.1)) to the radicals, the rate of initiation equals the rate of termination, and for photochemical initiation one obtains $v = k_{\mathrm{p}}[\ce{CH4}]\left(\phi I_{\mathrm{abs}}/k_{\mathrm{t}}\right)^{1/2}$: the rate is proportional to the square root of the absorbed light intensity, in exact analogy with the photochemical reaction of $\ce{H2 + Cl2}$ ([6.3.15](/6.3.15#sec-15.7.2)).

## 7.7. Reactivity and Selectivity

### 7.7.1. Reactivity of the Halogens

Extending the halogenation of methane to the four halogens, we calculate the $\Delta H$ of each step from BDEs ($\mathrm{kJ\,mol^{-1}}$):

| Step | Fluorination | Chlorination | Bromination | Iodination |
|---|---|---|---|---|
| $\ce{X2 -> 2X.}$ | $+159$ | $+243$ | $+193$ | $+151$ |
| $\ce{CH4 + X. -> .CH3 + HX}$ | $-131$ | $+7$ | $+73$ | $+141$ |
| $\ce{.CH3 + X2 -> CH3X + X.}$ | $-301$ | $-107$ | $-101$ | $-88$ |
| Overall $\ce{CH4 + X2 -> CH3X + HX}$ | $-432$ | $-100$ | $-28$ | $+53$ |

The trend is plain: the second step is exothermic for all four halogens, and the difference lies in the first step, in which the enthalpy of hydrogen atom transfer is determined by the strength of the $\ce{H-X}$ bond and changes from strongly exothermic to strongly endothermic from F to I. Hence:

- Fluorination is extremely violent; the heat released is enough to break $\ce{C-C}$ bonds and even to cause explosions. In practice it is carried out at low temperature with $\ce{F2}$ diluted with $\ce{N2}$, or other fluorination methods are used.
- Chlorination proceeds smoothly under illumination and is suitable for industrial production.
- In bromination the first step is endothermic by $73\,\mathrm{kJ\,mol^{-1}}$, the activation energy is about $75\,\mathrm{kJ\,mol^{-1}}$, and the reaction is slow and needs heat or strong light.
- Iodination is endothermic overall, so the equilibrium is unfavorable, and the barrier of the first step (about $140\,\mathrm{kJ\,mol^{-1}}$) is also too high; the reaction does not occur, and the reverse reaction (reduction of alkyl iodides by HI) is in fact easy.

The order of halogen reactivity is $\ce{F2} > \ce{Cl2} > \ce{Br2} > \ce{I2}$. Note that what determines reactivity is not the ease of the initiation step (the bonds of both $\ce{F2}$ and $\ce{I2}$ are weak) but the energetics of chain propagation.

### 7.7.2. Regioselectivity

Methane has only one kind of hydrogen, but higher alkanes have primary, secondary and tertiary $\ce{C-H}$ bonds, and halogenation at different positions occurs at different rates; this is the problem of **regioselectivity**. Experimental data ($25\,^\circ\mathrm{C}$, photochlorination):

- Propane: 1-chloropropane $43\%$, 2-chloropropane $57\%$. Propane has 6 primary and 2 secondary hydrogens, so per hydrogen the relative reactivity of secondary to primary is $\frac{57/2}{43/6} \approx 4$.
- 2-Methylpropane: 1-chloro-2-methylpropane $64\%$, 2-chloro-2-methylpropane $36\%$; with 9 primary hydrogens and 1 tertiary hydrogen, the relative reactivity of the tertiary hydrogen is $\frac{36/1}{64/9} \approx 5$.
- 2-Methylbutane: the two primary chlorides $27\%$ and $14\%$ (from the 6 hydrogens on C1 and the 3 on C4, respectively), the secondary $36\%$ (2 hydrogens on C3) and the tertiary $23\%$ (1 hydrogen on C2); per hydrogen this is $\frac{41}{9} : \frac{36}{2} : \frac{23}{1} \approx 1 : 4 : 5$.

The proportion of products is determined by two factors, the number of hydrogens of each kind (a statistical factor) and the relative reactivity $r$ of each hydrogen:

$$
\text{fraction of a given product} = \frac{n_i r_i}{\sum_j n_j r_j}.
\tag{7.3}
$$
The relative reactivities (per hydrogen) of the halogens are:

| Halogen (conditions) | Primary | Secondary | Tertiary |
|---|---|---|---|
| $\ce{F2}$ ($25\,^\circ\mathrm{C}$, gas phase) | $1$ | $1.2$ | $1.4$ |
| $\ce{Cl2}$ ($25\,^\circ\mathrm{C}$, gas phase) | $1$ | $3.9$ | $5.1$ |
| $\ce{Br2}$ ($125\,^\circ\mathrm{C}$, gas phase) | $1$ | $82$ | $1600$ |

The order of reactivity is always tertiary > secondary > primary, consistent with the order of radical stability, but the differences in selectivity are enormous: bromination takes place almost exclusively at the tertiary carbon (in the bromination of 2-methylpropane the tertiary product amounts to $\frac{1600}{1600 + 9} = 99.4\%$), whereas fluorination is almost unselective.

### 7.7.3. Explanation by the Hammond Postulate

Why do reactions that give the more stable radical go faster? Why is bromination so much more selective than chlorination? Selectivity is determined by the step in the propagation that forms the alkyl radical (hydrogen atom transfer). This step is irreversible, and the differences in its activation energy determine the product ratio. The BDE gives only thermodynamic data for the reaction, and to relate it to the activation energy we need the **Hammond postulate** ([6.5.3](/6.5.3#def-3.10.1)): the structure and energy of a **transition state** resemble those of the state (reactants or products) to which it is closer in energy.

- Hydrogen atom transfer in fluorination is strongly exothermic (primary $\ce{C-H}$ $423 - 570 = -147$, tertiary $\ce{C-H}$ $-166\,\mathrm{kJ\,mol^{-1}}$). The transition state is very "early" and resembles the reactants; the $\ce{C-H}$ bond is only slightly stretched and the character of the radical has barely developed. The difference in the stability of the product radicals is hardly transmitted to the transition state, the two activation energies are almost equal, and the selectivity is low.
- Hydrogen atom transfer in bromination is endothermic (primary $+57$, tertiary $+38\,\mathrm{kJ\,mol^{-1}}$). The transition state is very "late" and resembles the products; the $\ce{C-H}$ bond is almost completely broken and the radical center has already formed. Most of the difference in the stability of the product radicals (about $19\,\mathrm{kJ\,mol^{-1}}$) is reflected in the activation energies, and the selectivity is high.
- Chlorination lies between the two (primary $-9$, tertiary $-28\,\mathrm{kJ\,mol^{-1}}$); the transition state is rather early, and the selectivity is moderate.

![Schematic energy profiles for the hydrogen atom transfer R–H + X• → R• + H–X (primary and tertiary C–H). Left: X = F, strongly exothermic, early transition state, with almost equal barriers for the two paths; right: X = Br, endothermic, late transition state, with the difference in barriers close to the energy difference of the product radicals. ΔH is calculated from bond dissociation energies; barrier heights are schematic](./plots/halogenation-energy.py)

This is an example of the *reactivity–selectivity principle*: the more reactive a reagent, the lower its selectivity tends to be. The principle applies in many situations but is not a universal law; it can fail when the reaction is so fast that it approaches diffusion control, or when the transition state is dominated by other factors such as polarity or steric hindrance.

A neat test: a reaction of propane with an equimolar mixture of $\ce{Br2}$ and $\ce{Cl2}$ gives brominated products with a regioselectivity as low as that of chlorination. This is because the hydrogen is abstracted mainly by chlorine atoms (their hydrogen atom transfer is exothermic and several orders of magnitude faster than that of bromine atoms), and the alkyl radicals formed then undergo halogen atom transfer with the much weaker $\ce{Br-Br}$ bond (or $\ce{Br-Cl}$ bond) to give the bromide. Which halogen ends up in the product and what determines the selectivity are different questions: the selectivity is determined by the radical that abstracts the hydrogen.

### 7.7.4. Applications and Control of Selectivity

From the table above, radical halogenation of alkanes is of synthetic value in only two situations: when all hydrogens are equivalent (monochlorination of cyclohexane, 2,2-dimethylpropane or cyclopentane), or when the molecule has one tertiary hydrogen and bromination is used. For example, photobromination of 1,4-dimethylcyclohexane gives almost exclusively 1-bromo-1,4-dimethylcyclohexane, and the main product of the photobromination of 3-methylpentane is 3-bromo-3-methylpentane. Chlorination, although cheap, gives mixtures of alkanes that are hard to separate and is used industrially only where mixtures are acceptable.

Can the less reactive primary and secondary $\ce{C-H}$ bonds be halogenated selectively instead? The tertiary $\ce{C-H}$ bond is the weakest but is also the most hindered, being surrounded by alkyl groups, whereas the $\ce{C-H}$ bonds of a methyl group are the strongest but the most exposed. If the radical that abstracts the hydrogen is bulky, steric hindrance can take over from bond strength as the dominant factor. Alexanian and co-workers (2016) used the $N$-chloro derivative of $N$-*tert*-butyl-3,5-bis(trifluoromethyl)benzamide as the chlorinating reagent. In the amidyl radical formed after initiation, the *tert*-butyl group on nitrogen provides steric bulk and the two trifluoromethyl groups on the ring make the radical more electron-poor. The $\ce{N-H}$ bond of the resulting amide is very strong, so this radical can abstract hydrogen from ordinary $\ce{C-H}$ bonds but cannot easily approach crowded tertiary $\ce{C-H}$ bonds, and chlorination takes place mainly at the less hindered methylene (secondary) carbons remote from electron-withdrawing groups instead of at the tertiary carbons preferred by $\ce{Cl2}$. This idea of "reagent-controlled site selectivity" is one direction of modern $\ce{C-H}$ functionalization.

Nature mastered selective $\ce{C-H}$ oxidation long ago. The active center of cytochrome P450 enzymes is a heme iron; it activates $\ce{O2}$ to give a high-valent iron–oxo species (Fe(IV)=O with a porphyrin radical cation, called compound I), which abstracts a hydrogen atom from the substrate (HAT), and the carbon radical formed then "rebounds" and abstracts the hydroxyl group from $\ce{Fe-OH}$ to give the alcohol (the Groves rebound mechanism). The whole process takes place in the pocket of the enzyme, and the orientation of the substrate determines the position that is oxidized, so P450 can hydroxylate specific $\ce{C-H}$ bonds in complex molecules such as steroids and drugs with high selectivity. P450 enzymes in the human liver are responsible for the metabolism of most drugs, which is the chemical basis of drug–drug interactions.

![Oxygen rebound mechanism of cytochrome P450 (simplified). Top: compound I (an oxo-iron(IV) porphyrin radical cation whose oxygen behaves like an oxyl radical) abstracts a hydrogen atom from cyclohexane, giving Fe(IV)–OH and a cyclohexyl radical. Bottom: the cyclohexyl radical pairs with one electron of the Fe–O bond and takes the hydroxyl group (rebound); the other electron returns to iron, giving cyclohexanol and Fe(III)](./plots/p450-rebound.py)

## 7.8. Allylic and Benzylic Halogenation

Allylic and benzylic $\ce{C-H}$ bonds ($372$ and $375\,\mathrm{kJ\,mol^{-1}}$) are much weaker than ordinary secondary and tertiary $\ce{C-H}$ bonds, so radical halogenation occurs at these positions with high selectivity. The difficulty lies with alkenes: at higher concentrations of $\ce{Br2}$ it undergoes **electrophilic addition** to $\ce{C=C}$ ([6.5.11](/6.5.11#sec-11.4.2)) to give 1,2-dibromides rather than allylic substitution products. The solution is to keep the concentration of bromine very low at all times.

**Definition 7.8.1 (Wohl–Ziegler Reaction)** The bromination of allylic or benzylic $\ce{C-H}$ bonds with $N$-bromosuccinimide (NBS) in the presence of a radical initiator or light is called the **Wohl–Ziegler reaction**.

The solvent used to be carbon tetrachloride (NBS is poorly soluble in it, and the succinimide formed floats on the surface, which signals the end of the reaction); because of its toxicity and its damage to the ozone layer, trifluorotoluene, acetonitrile or ethyl acetate are now generally used instead.

```smiles
C1=CCCCC1.O=C1CCC(=O)N1Br>>BrC1C=CCCC1.O=C1CCC(=O)N1
```

The mechanism now generally accepted was proposed by Goldfinger in 1953: the chain carrier is the bromine atom, and the role of NBS is merely to convert the HBr produced in chain propagation continually into a low concentration of $\ce{Br2}$.

```smiles
O=C1CCC(=O)N1Br.Br>>O=C1CCC(=O)N1.BrBr
```

This is a fast ionic reaction.

The two propagation steps are exactly the same as in alkane halogenation: a bromine atom abstracts the allylic hydrogen to give a resonance-stabilized allyl radical and HBr; the allyl radical abstracts a bromine atom from $\ce{Br2}$, giving the product and regenerating a bromine atom.

![Chain propagation of allylic bromination with NBS (Goldfinger mechanism). (1) A bromine atom abstracts an allylic hydrogen of cyclohexene, and the cyclohex-2-enyl radical formed can be written as two resonance structures; (2) the allyl radical abstracts a bromine atom from Br₂ to give 3-bromocyclohexene and regenerate a bromine atom](./plots/allylic-bromination.py)

Why does a low concentration of $\ce{Br2}$ favor substitution and disfavor addition? The step in which a bromine atom adds to the double bond to give a $\beta$-bromoalkyl radical is reversible: the radical readily loses the bromine atom again by $\beta$-scission and returns to the starting material, and the addition product forms only if the radical meets $\ce{Br2}$ and abstracts a bromine atom before it fragments; the rate of ionic electrophilic addition is also higher than first order in $\ce{Br2}$. Abstraction of an allylic hydrogen atom to give a resonance-stabilized radical, on the other hand, is irreversible. The lower the concentration of $\ce{Br2}$, the less addition can be "completed", and the more substitution predominates. An alternative mechanism proposed early on held that the chain carrier is the succinimidyl nitrogen radical formed by homolysis of NBS; later studies showed that under ordinary conditions the bromination selectivities of NBS and of $\ce{Br2}$ are exactly the same, which indicates that the same bromine atom attacks the $\ce{C-H}$ bond, and the succinimidyl radical chain appears only under special conditions in which $\ce{Br2}$ is removed.

![Reversible addition of a bromine atom to cyclohexene. The unpaired electron of bromine and one pi electron form the C–Br bond, and the other pi electron stays on the neighboring carbon; the β-bromoalkyl radical readily loses the bromine atom again by beta-scission and gives the 1,2-dibromide only if it meets Br₂ first. At very low Br₂ concentration the irreversible abstraction of the allylic hydrogen wins](./plots/bromine-addition.py)

Because the unpaired electron of the allyl radical is distributed over both ends, an unsymmetrical alkene gives two products and the double bond migrates (allylic rearrangement): but-1-ene and NBS give a mixture of 3-bromobut-1-ene and 1-bromobut-2-ene ($E$ and $Z$). Benzylic bromination does not have this problem: toluene and NBS give benzyl bromide, and ethylbenzene is brominated only at the methylene group attached to the ring, giving (1-bromoethyl)benzene, because the benzylic radical is much more stable than a primary carbon radical, and although the unpaired electron is delocalized onto the ring, bond formation on the ring would destroy aromaticity.

```smiles
C=CCC>>C=CC(Br)C.BrC/C=C/C
CCc1ccccc1>>CC(Br)c1ccccc1
```

![Allylic rearrangement in the NBS bromination of 1-butene. Abstraction of the allylic hydrogen gives the 1-methylallyl radical, whose unpaired electron is shared by C1 and C3 (fishhook arrows: the unpaired electron and one pi electron form the new C2=C3 pi bond, and the other pi electron moves to C1); bromine transfer from Br₂ at either end gives 3-bromo-1-butene and 1-bromo-2-butene](./plots/butene-nbs.py)

## 7.9. Other Reactions of Alkanes

Apart from halogenation, alkanes are almost inert to all reagents at room temperature (the Latin origin of the word "paraffin" means "little affinity"). Their important reactions take place at high temperature or with catalysts and form the basis of petrochemistry.

### 7.9.1. Combustion and Partial Oxidation

Complete combustion of alkanes is one of the most important radical chain reactions and releases a large amount of heat, making natural gas, gasoline and diesel the main sources of energy. The **standard enthalpy of combustion** (heat of combustion) can also be used to compare the stabilities of isomers. The following table gives $\Delta_{\mathrm{c}}H^\circ$ for the combustion of gaseous alkanes to $\ce{CO2(g)}$ and $\ce{H2O(l)}$ at $298\,\mathrm{K}$ (calculated from enthalpies of formation in the CRC Handbook):

| Alkane | $\Delta_{\mathrm{c}}H^\circ$ / $(\mathrm{kJ\,mol^{-1}})$ | Alkane | $\Delta_{\mathrm{c}}H^\circ$ / $(\mathrm{kJ\,mol^{-1}})$ |
|---|---|---|---|
| Methane | $-890.6$ | Pentane | $-3535.6$ |
| Ethane | $-1560.5$ | 2-Methylbutane | $-3528.9$ |
| Propane | $-2220.0$ | 2,2-Dimethylpropane | $-3514.5$ |
| Butane | $-2877.6$ | Hexane | $-4195.0$ |
| 2-Methylpropane | $-2869.0$ | Cyclohexane | $-3952.6$ |

Each additional $\ce{CH2}$ in a homologous series increases the heat of combustion by about $658\,\mathrm{kJ\,mol^{-1}}$. Isomers burn to the same products, so the differences in their heats of combustion are the differences in their energies: the more branched the isomer, the smaller the heat of combustion and the more stable the molecule (2-methylpropane is more stable than butane by $8.6\,\mathrm{kJ\,mol^{-1}}$, and 2,2-dimethylpropane than pentane by $21\,\mathrm{kJ\,mol^{-1}}$). Data for the same physical state must be used in comparisons: the heat of combustion of a liquid is smaller than that of the gas by the enthalpy of vaporization (for liquid hexane $-4163\,\mathrm{kJ\,mol^{-1}}$). The heat of combustion of cyclohexane (gas) is almost the same as $6\times658 = 3949\,\mathrm{kJ\,mol^{-1}}$, showing that it has no **ring strain**; per $\ce{CH2}$ group, the heats of combustion of cyclopropane and cyclobutane exceed that of an open chain by about $38$ and $28\,\mathrm{kJ\,mol^{-1}}$, respectively, which is the origin of ring strain ([6.5.4](/6.5.4#sec-4.3.2)).

With catalysts and controlled conditions, alkanes can be partly oxidized to oxygen-containing compounds, which is the production route of many bulk chemicals:

- Cyclohexane is oxidized by air in the presence of cobalt salts to a mixture of cyclohexanol and cyclohexanone ("KA oil"), which is oxidized further to adipic acid, the raw material for nylon-66; the reaction goes through the cyclohexylperoxyl radical and cyclohexyl hydroperoxide.
- Butane can be oxidized by air in the liquid phase with cobalt catalysis to give acetic acid; gas-phase oxidation over a vanadium–phosphorus oxide catalyst gives maleic anhydride.
- In the laboratory, photocatalysts such as the decatungstate ion $\ce{W10O32^4-}$ abstract hydrogen atoms from alkanes under illumination (HAT) and can activate alkane $\ce{C-H}$ bonds at room temperature, a current research focus.

### 7.9.2. Cracking and Reforming

In petroleum refining, the conversion of large hydrocarbon molecules into smaller ones at high temperature is called cracking, and the rearrangement of the carbon skeleton of molecules is called reforming:

- Thermal cracking and steam cracking: heating briefly at $750$–$900\,^\circ\mathrm{C}$ with steam dilution breaks hydrocarbons by the radical chain reactions of the **Rice–Herzfeld mechanism** ([6.3.15](/6.3.15#def-15.8.1)) to give lower alkenes such as ethene and propene, the basic raw materials of the organic chemical industry.
- Catalytic cracking: over an acidic zeolite at about $500\,^\circ\mathrm{C}$, cleavage and rearrangement through **carbocation** intermediates ([6.5.8](/6.5.8#sec-8.3.3)) give many branched alkanes and arenes and a high-octane gasoline.
- Catalytic reforming: over a bifunctional catalyst of platinum (or platinum–rhenium) on alumina, cycloalkanes are dehydrogenated to arenes, and straight-chain alkanes are isomerized to branched alkanes or dehydrocyclized to arenes; it is used to produce high-octane gasoline and benzene, toluene and xylenes, with hydrogen as a by-product.

![Beta-scission in thermal cracking (Rice–Herzfeld chain). The unpaired electron of the 1-hexyl radical and one electron of the C2–C3 bond form the C1=C2 pi bond of ethene; the other electron of the C2–C3 bond stays on C3, giving the 1-butyl radical, which fragments further or abstracts a hydrogen atom from another alkane molecule](./plots/cracking-beta-scission.py)

### 7.9.3. Ring Opening of Small Cycloalkanes

Cyclopropane and cyclobutane have large **ring strain** (about $115$ and $110\,\mathrm{kJ\,mol^{-1}}$), the $\ce{C-C}$ bonds in the rings are weaker than ordinary ones, and the rings can be opened under suitable conditions. The $\ce{C-C}$ bonds of cyclopropane are outward-bent "**bent bonds**" ("banana bonds") with the electron density outside the ring and some $\pi$-like character, and can be attacked by **electrophiles** ([6.5.4](/6.5.4#sec-4.4.1), [6.5.11](/6.5.11#sec-11.3)).

- Catalytic hydrogenation: cyclopropane is hydrogenated over Ni at about $80\,^\circ\mathrm{C}$ with ring opening to propane; cyclobutane needs about $200\,^\circ\mathrm{C}$; cyclopentane and cyclohexane do not open under ordinary hydrogenation conditions. Substituted cyclopropanes cleave at the least hindered $\ce{C-C}$ bond (adsorbed on one side of the catalyst surface), and ethylcyclopropane is hydrogenated to 2-methylbutane. Ring opening of cyclopropane is much slower than hydrogenation of alkenes, so a cyclopropane bearing a vinyl group can be hydrogenated at the double bond only, leaving the three-membered ring intact.
- Reaction with halogens: cyclopropane and $\ce{Br2}$ open the ring at room temperature (slowly, faster with Lewis acid catalysis) to give 1,3-dibromopropane; a substituted cyclopropane opens between the carbons with the most and the fewest hydrogens, the reaction going through a more stable carbocation-like intermediate, as in the formation of 1,3-dibromobutane from methylcyclopropane. Under illumination cyclopropane and $\ce{Cl2}$ undergo radical substitution to give chlorocyclopropane.
- Reaction with hydrogen halides: methylcyclopropane opens with HBr, hydrogen adding to the carbon with more hydrogens and bromine to the carbon that can form the more stable carbocation, to give 2-bromobutane, similar to **Markovnikov's rule** for addition to alkenes ([6.5.11](/6.5.11#sec-11.3.2)).

```smiles
CC1CC1.BrBr>>CC(Br)CCBr
CC1CC1.Br>>CCC(C)Br
```

![Ring opening of methylcyclopropane by HBr (polar, full arrows). The bent C1–C2 bond of the ring acts as the nucleophile: its electron pair takes the proton of HBr, so that H bonds to C2 (the carbon with more hydrogens) and the positive charge stays on C1, which gives the more stable secondary cation; bromide then adds to C1, giving 2-bromobutane (Markovnikov orientation)](./plots/cyclopropane-hbr.py)

Cyclobutane is much less reactive than cyclopropane: it does not undergo ring-opening addition with $\ce{Br2}$ or HBr at room temperature (under illumination it undergoes radical substitution with halogens), and hydrogenative ring opening also requires high temperatures. This difference has two causes. The ring strain of cyclobutane is mainly a combination of **torsional strain** and **angle strain**, and its $\ce{C-C}$ bonds are not bent outward as in cyclopropane and have no $\pi$-like character; and the transition state for ring opening does not release as much strain.

## Summary

| Topic | Key points |
|---|---|
| Structure | Alkyl radicals are nearly planar ($\mathrm{sp}^2$, unpaired electron in a p orbital, the SOMO); a stereogenic center that becomes a radical is racemized; $\sigma$ radicals (vinyl, phenyl, acyl) are more reactive; radical ions (Definition 7.1.2) |
| Generation | Homolysis (Definition 7.2.1): light, heat, initiators (AIBN, BPO, Definition 7.2.3); single electron transfer (Definition 7.2.4); photoredox |
| Stability | Compared by BDE (Definition 7.2.2): methyl < primary < secondary < tertiary < allyl ≈ benzyl; hyperconjugation, conjugation, $\alpha$-heteroatoms, captodative effect; persistent radicals (Definition 7.3.2) rely on steric hindrance |
| Autoxidation | Definition 7.3.1; peroxides of ethers, lipid peroxidation and vitamin E |
| EPR | $h\nu = g\mu_{\mathrm{B}}B$ (Definition 7.4.1); hyperfine splitting into $2nI + 1$ lines (Definition 7.4.2); $\ce{.CH3}$ $1:3:3:1$, $a = 2.30\,\mathrm{mT}$; spin trapping |
| Elementary steps | Homolysis/coupling, addition/$\beta$-scission (Definition 7.5.2), atom transfer (HAT, Definition 7.5.1); radical clocks |
| Mechanism of halogenation | Initiation $\ce{X2 -> 2X.}$; propagation HAT + halogen atom transfer; termination by coupling; $\Delta H$ from BDEs |
| Reactivity | $\ce{F2} > \ce{Cl2} > \ce{Br2} > \ce{I2}$, determined by $\Delta H$ of the HAT step; iodination does not occur |
| Selectivity | Relative reactivity per hydrogen tertiary > secondary > primary: $\ce{Cl2}$ $5 : 4 : 1$, $\ce{Br2}$ $1600 : 82 : 1$; Eq. (7.3); Hammond postulate: late transition state in bromination, high selectivity; bulky radicals can reverse the selectivity |
| Allylic and benzylic positions | Wohl–Ziegler reaction (Definition 7.8.1), Goldfinger mechanism: NBS maintains a low concentration of $\ce{Br2}$; allylic rearrangement |
| Other reactions | Heats of combustion compare isomer stability (branched isomers are more stable); partial oxidation; steam cracking (radical) and catalytic cracking (carbocation); ring opening of cyclopropane (hydrogenation, $\ce{Br2}$, HBr), cyclobutane does not open at room temperature |

## Questions

1. Determine the hybridization and geometry at the radical center of each of the following radicals: methyl, trifluoromethyl, vinyl, *tert*-butoxyl, and the nitroxide of TEMPO.

   **Answer** Methyl: $\mathrm{sp}^2$, planar, unpaired electron in a p orbital. Trifluoromethyl: close to $\mathrm{sp}^3$, pyramidal (electronegative F increases the p character of the bonding orbitals). Vinyl: a $\sigma$ radical, with the unpaired electron in an $\mathrm{sp}^2$ orbital, a bent $\ce{C=C-H}$ unit and rapid inversion. *tert*-Butoxyl: the unpaired electron is in a p orbital on oxygen (oxygen may be regarded as $\mathrm{sp}^3$ or unhybridized, the radical being in a nonbonding p orbital). TEMPO: nitrogen is approximately $\mathrm{sp}^2$ and slightly pyramidal, with the unpaired electron in the $\pi^*$ orbital of $\ce{N-O}$ (a three-electron $\pi$ bond).
2. The first $\ce{C-H}$ BDE of the methylene group of cyclohexa-1,4-diene is $318\,\mathrm{kJ\,mol^{-1}}$, and breaking a further $\ce{C-H}$ bond of the radical formed takes only about $90\,\mathrm{kJ\,mol^{-1}}$. Explain structurally why both are small and why the latter is especially small.

   **Answer** After the first $\ce{C-H}$ bond breaks, the unpaired electron is conjugated with the two $\ce{C=C}$ bonds on either side, forming a pentadienyl radical delocalized over five carbons, with about twice the stabilization of an allyl radical. Breaking the second $\ce{C-H}$ bond gives benzene: besides losing the energy of the radical, the system gains aromatic stabilization (about $150\,\mathrm{kJ\,mol^{-1}}$), so the bond is extremely weak. This makes cyclohexa-1,4-diene a good hydrogen atom donor and also a reagent for trapping aryl diradicals in reactions such as the Bergman cyclization.
3. The mechanism of the Barton–McCombie deoxygenation is as follows. AIBN loses $\ce{N2}$ on heating; the 2-cyanopropan-2-yl radical abstracts the hydrogen atom of $\ce{Bu3SnH}$ to give the tributyltin radical; the tin radical adds to the sulfur atom of the xanthate $\ce{R-O-C(=S)SCH3}$ to give a carbon radical; this carbon radical cleaves the $\ce{C-O}$ bond, releasing the alkyl radical $\ce{R.}$ and $\ce{CH3S-C(=O)-SSnBu3}$; $\ce{R.}$ then abstracts a hydrogen atom from $\ce{Bu3SnH}$ to give $\ce{R-H}$ and a new tin radical. Identify the type of elementary step of each step and which steps make up the chain propagation.

   **Answer** Decomposition of AIBN: homolysis (with loss of $\ce{N2}$). The 2-cyanopropan-2-yl radical with $\ce{Bu3SnH}$: hydrogen atom transfer. The tin radical with $\ce{C=S}$: radical addition. Fragmentation of the carbon radical to give $\ce{R.}$: $\beta$-scission (driven by the formation of a strong $\ce{C=O}$ bond). $\ce{R.}$ with $\ce{Bu3SnH}$: hydrogen atom transfer. The first two steps are chain initiation; the addition of the tin radical, the $\beta$-scission and the hydrogen atom transfer to $\ce{R.}$ make up the chain propagation (the tin radical is regenerated in the last step).
4. In the chain reaction of photochlorination of methane: (a) use the steady-state approximation to write the relationship between the rate of formation of $\ce{CH3Cl}$ and the light intensity and the concentrations of the reactants (assume that termination is mainly $\ce{2Cl. -> Cl2}$); (b) does the reaction stop immediately when the light is switched off?

   **Answer** (a) Let the rate of photoinitiation be $2\phi I_{\mathrm{abs}}$. Applying the steady-state approximation to $\ce{Cl.}$ and $\ce{.CH3}$, the two propagation steps have equal rates and initiation equals termination: $2\phi I_{\mathrm{abs}} = 2k_{\mathrm{t}}[\ce{Cl.}]^2$, so $[\ce{Cl.}] = (\phi I_{\mathrm{abs}}/k_{\mathrm{t}})^{1/2}$ and $v = k_{\mathrm{p}}[\ce{Cl.}][\ce{CH4}] = k_{\mathrm{p}}[\ce{CH4}](\phi I_{\mathrm{abs}}/k_{\mathrm{t}})^{1/2}$, proportional to the square root of the light intensity and to the concentration of methane, and independent of the concentration of $\ce{Cl2}$ (provided that $\ce{Cl2}$ is not too low and all the light is absorbed). (b) No. The chain carriers already present need some time (about the lifetime of the radicals, of the order of milliseconds to seconds) to disappear by termination, and chain propagation continues during that time.
5. Calculate the distribution of the monochloro and monobromo products from photochlorination ($25\,^\circ\mathrm{C}$) and photobromination ($125\,^\circ\mathrm{C}$) of 2-methylbutane.

   **Answer** The types of hydrogen are 6 primary hydrogens on C1, 1 tertiary hydrogen on C2, 2 secondary hydrogens on C3 and 3 primary hydrogens on C4. Chlorination ($1 : 3.9 : 5.1$): $6 : 5.1 : 7.8 : 3$, that is, 1-chloro-2-methylbutane $27\%$, 2-chloro-2-methylbutane $23\%$, 2-chloro-3-methylbutane $36\%$ and 1-chloro-3-methylbutane $14\%$, in agreement with experiment. Bromination ($1 : 82 : 1600$): $6 : 1600 : 164 : 3$, giving 2-bromo-2-methylbutane $90\%$, 2-bromo-3-methylbutane $9\%$, and less than $1\%$ in all of the two primary bromides.
6. An equimolar mixture of $\ce{Br2}$ and $\ce{Cl2}$ reacts with propane under illumination, and the regioselectivity of the bromide formed is far lower than with $\ce{Br2}$ alone and close to that of chlorination. Explain.

   **Answer** The selectivity is determined by the radical that abstracts the hydrogen atom. In the mixture, chlorine atoms abstract hydrogen several orders of magnitude faster than bromine atoms, so almost all alkyl radicals are formed by $\ce{Cl.}$, and the ratio of primary to secondary radicals is that of chlorination. The alkyl radicals then undergo halogen atom transfer with the weaker bond of $\ce{Br2}$ (or $\ce{BrCl}$) to give the bromide and regenerate a halogen atom. The product contains bromine, but the selectivity is that of the chlorine atom.
7. Both carbons of the double bond of cyclohexene are labeled with $^{13}\mathrm{C}$ (the asterisks in the structure below), and the compound is treated with NBS initiated by dibenzoyl peroxide. Write the product and mark the position of the labeled carbons.

   ```smiles
   C1CC[13CH]=[13CH]C1
   ```

   **Answer** A bromine atom abstracts an allylic hydrogen on C3 (or equivalently C6), and in the allyl radical formed the unpaired electron is distributed over C1 and C3. Bromine added at C3 gives 3-bromocyclohexene with the double bond still at C1=C2 and the labels on the two vinylic carbons; bromine added at C1 moves the double bond to C2=C3 and also gives 3-bromocyclohexene, but with the labels on the carbon bearing bromine and the adjacent vinylic carbon (C3 and C2 after renumbering). The product is therefore an approximately $1:1$ mixture of these two isotopic isomers, which is evidence for the symmetric delocalization of the allyl radical.
8. In the EPR spectrum of the ethyl radical, $a(\alpha\text{-H}) = 2.24\,\mathrm{mT}$ and $a(\beta\text{-H}) = 2.69\,\mathrm{mT}$. How many lines does it have, and what are their intensity ratios? What does the fact that the coupling constant of the $\beta$-H is larger than that of the $\alpha$-H show?

   **Answer** First the splitting by the three $\beta$-H gives a $1:3:3:1$ quartet (spacing $2.69\,\mathrm{mT}$), and each line is split by the two $\alpha$-H into a $1:2:1$ triplet (spacing $2.24\,\mathrm{mT}$), giving 12 lines in all, with intensities given by the products of two sets of binomial coefficients (1, 2, 1, 3, 6, 3, 3, 6, 3, 1, 2, 1). The $\beta$-H is separated from the radical center by one carbon but has the larger coupling, which shows that the unpaired electron is substantially delocalized onto the $\beta$ $\ce{C-H}$ bonds by **hyperconjugation**; the coupling of the $\alpha$-H arises from spin polarization and is smaller (with negative sign).
9. Toluene and NBS initiated by AIBN give only benzyl bromide, whereas $\ce{Br2}$ in the presence of $\ce{FeBr3}$ (in the dark) gives ortho- and para-bromotoluene. Explain the difference in the position of reaction under the two conditions.

   **Answer** The former is a radical chain reaction: a bromine atom abstracts the weakest $\ce{C-H}$ bond, the benzylic one ($375\,\mathrm{kJ\,mol^{-1}}$), to give the resonance-stabilized benzyl radical, which abstracts bromine from $\ce{Br2}$, so substitution occurs in the side chain; the aromatic $\ce{C-H}$ ($472\,\mathrm{kJ\,mol^{-1}}$) is not abstracted. The latter is ionic **electrophilic aromatic substitution** ([6.5.14](/6.5.14#sec-14.7)): $\ce{FeBr3}$ polarizes $\ce{Br2}$ into an electrophile that attacks the electron-rich ring, and the methyl group activates the ortho and para positions. The conditions (light and an initiator, or a Lewis acid) determine the mechanism, and the mechanism determines the position.
10. In lipid peroxidation of unsaturated fatty acids, what are the chain carriers of autoxidation? Why can vitamin E "break the chain"? Why does its phenoxyl radical not go on to propagate the chain?

    **Answer** The chain carriers are the lipid carbon radical $\ce{L.}$ and the peroxyl radical $\ce{LOO.}$: $\ce{L. + O2 -> LOO.}$ and $\ce{LOO. + LH -> LOOH + L.}$, in which the bisallylic $\ce{C-H}$ of $\ce{LH}$ (about $320\,\mathrm{kJ\,mol^{-1}}$) is abstracted. The phenolic $\ce{O-H}$ of vitamin E is about as strong as the bisallylic $\ce{C-H}$ (about $325\,\mathrm{kJ\,mol^{-1}}$, no clear thermodynamic advantage); the key is kinetics: it sits in the lipid environment, and its rate constant for transferring the hydrogen atom to $\ce{LOO.}$ is $10^4$–$10^5$ times larger than that for $\ce{LH}$, so the peroxyl radical is converted into $\ce{LOOH}$ without regenerating $\ce{L.}$. The tocopheroxyl radical formed is stabilized by conjugation with the ring and by the steric hindrance of the ortho methyl groups; its abstraction of a hydrogen atom from $\ce{LH}$ is endothermic and extremely slow, and it mainly combines with a second peroxyl radical, which terminates the chain, or is reduced back by vitamin C.
