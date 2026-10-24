---
title: Pericyclic Reactions
source_hash: 1996a001309b
---

The reactions of the preceding chapters all proceed through ionic or radical intermediates. This chapter treats a third class of mechanism: concerted reactions in which bond breaking and bond making occur together, through a cyclic transition state and without an intermediate. The Diels–Alder reaction, the Claisen rearrangement and the cyclization of polyenes all belong to this class. They are barely affected by solvent polarity, acids and bases, or radical initiators, yet they show extremely high stereospecificity, and heating and irradiation give products of opposite stereochemistry. In the 1960s Woodward and Hoffmann explained these regularities through the symmetry of molecular orbitals, and Fukui's **frontier orbital** theory provided an equivalent and simpler method of analysis; this is one of the most successful applications of **molecular orbital theory** in organic chemistry. We use directly the Hückel orbitals of linear and cyclic conjugated systems from [6.5.2](/6.5.2#sec-2.2); the excited states involved in photochemical reactions are described in [6.3.17](/6.3.17); and the theory of aromatic transition states (Section 12.6) anticipates the next chapter on aromaticity ([6.5.13](/6.5.13)). Applications and variants of pericyclic reactions reappear in the chapter on rearrangements ([6.5.30](/6.5.30)), and the inverse-electron-demand Diels–Alder reaction of tetrazines is one of the most important bioorthogonal reactions in chemical biology ([6.6](/6.6)).

## 12.1. Characteristics and Classification of Pericyclic Reactions

### 12.1.1. A Class of "Mechanismless" Reactions

In the early twentieth century several reactions were discovered that were hard to classify: allyl phenyl ether rearranges on heating to o-allylphenol (Claisen, 1912), and cyclopentadiene adds to maleic anhydride at room temperature to give a bicyclic product (Diels and Alder, 1928). They do not resemble ionic reactions (their rates are almost independent of solvent polarity, acids and bases) or radical reactions (they are neither accelerated by initiators nor inhibited by radical inhibitors), and they are stereospecific: stereoisomeric reactants give specific stereoisomeric products. In the 1950s and 1960s it was further found that when the same polyene is cyclized by heat and by light, the stereochemistry of the products is exactly opposite.

**Definition 12.1.1 (Pericyclic Reaction)** A reaction in which the breaking of old bonds and the formation of new bonds proceed in a concerted manner (in one step, without an intermediate) through a cyclic transition state is called a **pericyclic reaction**.

| Type | Mode of bond cleavage | Intermediate | Typical conditions |
|---|---|---|---|
| Radical reaction | Homolysis | **Radical** | Initiators, light, heat |
| Ionic reaction | Heterolysis | Cations, anions | Acids, bases, polar solvents |
| Pericyclic reaction | Concerted | None | Heat or light |

The characteristics of pericyclic reactions: they occur in one step (only one **transition state**); no ionic or radical intermediates are formed; stereospecificity is high; and heat and light give opposite selectivity. "Concerted" does not mean "synchronous": the two new bonds may be formed to different extents in the transition state (asynchronous), as long as there is no energy minimum in between.

### 12.1.2. Three Types

Pericyclic reactions all occur in conjugated π systems and are classified by the change in bonding into three types (besides minor types such as the ene reaction of Section 12.7 and cheletropic reactions):

| Type | Change | Example |
|---|---|---|
| Electrocyclic reaction (12.3) | Ring closure between the termini of a conjugated polyene: one π bond is lost and one σ bond is gained; the reverse reaction is ring opening | Hexatriene → cyclohexadiene |
| Cycloaddition (12.4) | Two σ bonds are formed between the termini of two π systems, forming a ring; the reverse reaction is called cycloreversion (retro-cycloaddition) | Diels–Alder reaction |
| Sigmatropic rearrangement (12.5) | A σ bond migrates along a π system to a new position, with the π bonds shifting accordingly; the numbers of σ and π bonds do not change | Cope and Claisen rearrangements |

## 12.2. Frontier Molecular Orbital Theory

### 12.2.1. Frontier Orbitals

A chemical reaction is a redistribution of electrons, and to study a reaction we must know which orbitals' electrons take part. In 1952 Fukui proposed (*J. Chem. Phys.*):

**Definition 12.2.1 (Frontier Molecular Orbital Theory)** The theory which holds that the reactivity of a molecule is determined mainly by its **highest occupied molecular orbital** (HOMO) and **lowest unoccupied molecular orbital** (LUMO), and which analyzes whether a reaction can occur, and its selectivity, in terms of the interaction of the frontier orbitals of the two reacting molecules (the HOMO of one and the LUMO of the other in a bimolecular reaction), is called **frontier molecular orbital theory** (FMO theory).

A radical has an orbital occupied by a single electron (the **SOMO**), which acts as both HOMO and LUMO. In unimolecular concerted reactions (electrocyclization, sigmatropic shifts) there is no second molecule, and FMO theory looks only at the phases of the reactant's HOMO. The theory is not restricted to pericyclic reactions: for example, the **SN2 reaction** is the interaction of the nucleophile HOMO (a lone pair) with the C–X σ* orbital (the LUMO), and backside attack serves precisely to overlap in phase with the large lobe of σ* ([6.5.8](/6.5.8#sec-8.4.1)).

### 12.2.2. Rules of Orbital Interaction

Two orbitals $\phi_a$ and $\phi_b$ (energies $E_a < E_b$, interaction integral $h_{ab}$) mix to give an in-phase combination of lower energy and an out-of-phase combination of higher energy. By second-order perturbation theory the lower combination is stabilized by approximately

$$
\Delta E \approx \frac{h_{ab}^2}{E_b - E_a},
$$

and therefore:

- Phase: in-phase overlap is bonding (energy is lowered) and out-of-phase overlap is antibonding (energy is raised); in diagrams the two signs of the orbital wavefunction are shown by shading and blank (or two colors, or "+/−").
- Energy: the smaller $E_b - E_a$, the stronger the interaction. Of the two molecules, the HOMO–LUMO pair closest in energy plays the dominant role.
- Overlap: $h_{ab}$ is proportional to the overlap, and orbitals that cannot approach each other in space do not interact; in pericyclic reactions it is further required that the two pairs of bonding atoms can overlap simultaneously on the same face (or on opposite faces).
- Electron count: when a filled orbital interacts with an empty one, two electrons enter the lowered combination and there is net stabilization; when two filled orbitals interact, the raising of the antibonding combination slightly exceeds the lowering of the bonding combination, and there is net repulsion (the orbital origin of steric repulsion). The stabilizing interaction is therefore HOMO–LUMO, not HOMO–HOMO.
- Symmetry: under a symmetry element that is maintained throughout the reaction, only orbitals of the same symmetry can mix (Section 12.3.3).

### 12.2.3. Orbitals of Conjugated Systems

A linear conjugated system of $n$ p orbitals has $n$ π molecular orbitals $\psi_1, \dots, \psi_n$, whose Hückel energies and coefficients are found in [6.5.2](/6.5.2#sec-2.2). Only a few rules need to be remembered for the analysis of pericyclic reactions:

- $\psi_k$ has $k - 1$ **nodal planes** perpendicular to the chain, and the more nodal planes, the higher the energy;
- the relative sign of the coefficients at the two ends is determined by the number of nodes: for an even number of nodal planes ($\psi_1, \psi_3, \dots$) the two ends have the same sign, and for an odd number ($\psi_2, \psi_4, \dots$) opposite signs;
- in neutral polyenes with an even number of carbons (ethene, butadiene, hexatriene) the HOMO is $\psi_{n/2}$ and the LUMO is $\psi_{n/2+1}$; in allyl and pentadienyl systems with an odd number of carbons, the nonbonding orbital $\psi_{(n+1)/2}$ is the LUMO in the cation, the SOMO in the radical and the HOMO in the anion.

| System | π electrons | HOMO | Phases of the ends |
|---|---|---|---|
| Ethene | 2 | $\psi_1$ | Same sign |
| Butadiene | 4 | $\psi_2$ | Opposite sign |
| Hexatriene | 6 | $\psi_3$ | Same sign |
| Allyl cation | 2 | $\psi_1$ | Same sign |
| Allyl anion (1,3-dipole) | 4 | $\psi_2$ | Opposite sign |
| Pentadienyl cation | 4 | $\psi_2$ | Opposite sign |

Photoexcitation promotes an electron from the HOMO to the LUMO, and in the excited state the orbital that acts as HOMO is the former LUMO (denoted HOMO\*); the phase relationship of the two ends is exactly reversed, which is the origin of the opposite selectivity of light and heat. The initially excited state is a **singlet state**, in which the two electrons have opposite spins; it can also pass by **intersystem crossing** to a **triplet state** (the **Jablonski diagram** in [6.3.17](/6.3.17)), and triplet reactions are often stepwise.

The orbitals of cyclic conjugated systems (benzene, the cyclopentadienyl ion, etc.) are given by Frost circles ([6.5.2](/6.5.2#sec-2.2), [6.5.13](/6.5.13)), which are needed in Section 12.6.

### 12.2.4. Three Equivalent Methods of Analysis

| Method | Proposed by | What is examined |
|---|---|---|
| Frontier orbital theory | Fukui (1952) | Whether the phases of the HOMO (and LUMO) match at the bonding positions |
| Conservation of orbital symmetry (correlation diagrams) | Woodward, Hoffmann (1965) | Whether all orbitals of reactants and products are correlated one to one by symmetry, and whether all occupied orbitals correlate with bonding orbitals of the product |
| Aromatic transition state theory | Dewar, Zimmerman (1966–1971) | Whether the cyclic transition state is aromatic or antiaromatic |

The three methods rest on the same molecular-orbital concepts and judge the energy of the transition state from different angles, with consistent conclusions. The FMO method suffices for everyday analysis. Fukui and Hoffmann received the 1981 Nobel Prize in Chemistry for this work (Woodward had died in 1979).

## 12.3. Electrocyclic Reactions

### 12.3.1. Conrotatory and Disrotatory Modes

**Definition 12.3.1 (Electrocyclic Reaction)** A reaction in which, on heating or irradiation, the terminal carbon atoms of a conjugated polyene bond through their π electrons and close to a cycloalkene, together with the reverse reaction (ring opening of a cycloalkene to a conjugated polyene), is called an **electrocyclic reaction**.

In ring closure, each terminal p orbital must rotate by $90^\circ$ in order to overlap head-on and form a σ bond; there are two modes of rotation:

**Definition 12.3.2 (Conrotatory and Disrotatory)** In an electrocyclic reaction, rotation of the two terminal groups about their respective C–C bonds in the same direction (both clockwise or both counterclockwise) is called **conrotatory**; rotation in opposite directions is called **disrotatory**.

The two modes place the terminal substituents in different relative positions, so the stereochemistry of the product is determined entirely by the mode of rotation. Experimentally, (2E,4Z,6E)-octa-2,4,6-triene on heating gives only cis-5,6-dimethylcyclohexa-1,3-diene, and on irradiation only the trans isomer; cis-3,4-dimethylcyclobutene on heating opens only to (2E,4Z)-hexa-2,4-diene.

```smiles
C/C=C/C=C\C=C\C>>C[C@@H]1C=CC=C[C@@H]1C heat
C[C@@H]1C=C[C@@H]1C>>C/C=C/C=C\C heat
```

### 12.3.2. Frontier Orbital Analysis

FMO theory holds that a unimolecular electrocyclization is determined by the phases at the two ends of the polyene HOMO: when the two lobes that approach each other after rotation are in phase (both shaded or both blank), bonding stabilizes the transition state and the reaction is allowed.

![Frontier orbital analysis of electrocyclization (Hückel coefficients computed with numpy). Top: butadiene. For the thermal reaction we look at the HOMO $\psi_2$ (ends of opposite sign), and only conrotation brings the meeting lobes in phase; for the photochemical reaction we look at the excited-state HOMO\* $\psi_3$ (ends of the same sign), and disrotation is allowed. Bottom: hexatriene. The thermal HOMO $\psi_3$ has ends of the same sign, and disrotation is allowed; the photochemical $\psi_4$ has ends of opposite sign, and conrotation is allowed](./plots/electrocyclic-fmo.py)

Thus butadiene (4 π electrons) is conrotatory thermally and disrotatory photochemically, and hexatriene (6 π electrons) is disrotatory thermally and conrotatory photochemically. This explains the experiments of Section 12.3.1: on ring opening, cis-3,4-dimethylcyclobutene rotates conrotatorily, one methyl turning outward and one inward, to give the (E,Z)-diene; ring closure of the (E,Z,E)-octatriene is thermally disrotatory, the two outer methyl groups turn to the same side of the ring, and the cis product results.

![6-Electron electrocyclization of (Z)-hexa-1,3,5-triene: the three π bonds shift around the ring, and a σ bond forms between C1 and C6 (the curved arrows show only where the electrons go; the stereochemistry is determined by orbital symmetry)](./plots/electrocyclic-arrows.py)

Electrocyclic ring opening is awkward to treat by FMO (the HOMO of cyclobutene is a π orbital, but it is a σ bond that breaks) and is usually judged by the principle of microscopic reversibility from the corresponding ring closure: forward and reverse directions along the same path have the same selectivity. Ring opening of cyclobutenes has an additional selectivity: conrotation can occur in two ways (both substituents turning outward or both inward), and the substituents generally turn outward (torquoselectivity), since turning inward would cause a clash with the hydrogen at the other end.

### 12.3.3. Correlation Diagrams

**Definition 12.3.3 (Correlation Diagram)** A diagram in which all the molecular orbitals of reactant and product that are involved in bond breaking and bond making are arranged by energy, each orbital is labeled symmetric (S) or antisymmetric (A) with respect to a symmetry element that is maintained throughout the reaction, and orbitals of the same symmetry are connected one to one (lowest with lowest, with no crossing of correlation lines between orbitals of the same symmetry), is called a **correlation diagram** (orbital correlation diagram).

The procedure:

1. List all relevant orbitals of reactant and product: $\psi_1$–$\psi_4$ of butadiene; σ, π, π\* and σ\* of cyclobutene (σ is the newly formed bond).
2. Choose a symmetry element present throughout the reaction: conrotation maintains a twofold rotation axis $C_2$ (lying in the molecular plane and perpendicularly bisecting the C2–C3 bond), and disrotation maintains a mirror plane σ (perpendicular to the molecular plane and perpendicularly bisecting the C2–C3 bond).
3. Label each orbital S or A with respect to this symmetry element (the same orbital may be labeled differently for different symmetry elements: $\psi_1$ of butadiene is A for $C_2$ and S for σ).
4. Orbitals of the same symmetry are correlated. If all occupied orbitals of the reactant correlate with bonding orbitals of the product, the reaction is symmetry-allowed in the ground state (thermal reaction); if an occupied orbital correlates with an antibonding orbital of the product (the correlation line crosses the HOMO–LUMO boundary), the ground-state reaction is symmetry-forbidden, has a very high activation energy, and can proceed only in the excited state (under light).

![Correlation diagrams for butadiene and cyclobutene. Left: conrotation (maintaining $C_2$), $\psi_1 \to \pi$, $\psi_2 \to \sigma$, allowed in the ground state. Right: disrotation (maintaining σ), $\psi_2$ correlates with $\pi^*$ (red line), so the ground-state reactant would become a doubly excited product, and the thermal reaction is forbidden](./plots/correlation-diagram.py)

The correlation diagram expresses the conservation of orbital symmetry: the orbitals of the reactant must change continuously into those of the product in a way that preserves symmetry. It applies to both ring opening and ring closure, and its conclusions agree with the FMO analysis. Its drawbacks are that it is laborious and can be used only for parent systems that have symmetry (when substituents destroy the symmetry, the judgment is still made for the parent system).

### 12.3.4. Selection Rules

| Reactant | π electrons | Thermal reaction (ground state) | Photochemical reaction (excited state) |
|---|---|---|---|
| Allyl cation → cyclopropyl cation | 2 | Disrotatory | Conrotatory |
| Butadiene → cyclobutene | 4 | Conrotatory | Disrotatory |
| Pentadienyl cation → cyclopentenyl cation | 4 | Conrotatory | Disrotatory |
| Hexatriene → cyclohexadiene | 6 | Disrotatory | Conrotatory |
| General: $4n$ electrons | $4n$ | Conrotatory | Disrotatory |
| General: $4n+2$ electrons | $4n+2$ | Disrotatory | Conrotatory |

What determines the selectivity is the number of electrons involved, not the number of atoms: the pentadienyl cation has 5 carbons and 4 π electrons and belongs, like butadiene, to the $4n$ systems.

### 12.3.5. Applications

6π Electrocyclizations are common in natural product synthesis. All-cis cyclodecapentaene ([10]annulene) is extremely unstable and closes disrotatorily below room temperature to give cis-9,10-dihydronaphthalene: the reacting unit is one hexatriene unit of the molecule (6 electrons), not the whole 10-electron system. Photochemical conrotatory ring opening and closure occur in the biosynthesis of vitamin D: in skin, 7-dehydrocholesterol undergoes a 6π conrotatory ring opening under ultraviolet light to give previtamin D₃, which is converted by a thermal [1,7]-hydrogen shift (Section 12.5.4) into vitamin D₃.

The Nazarov cyclization: a divinyl ketone cyclizes to a cyclopentenone under protic acids ($\ce{H3PO4}$, $\ce{H2SO4}$) or Lewis acids ($\ce{BF3*OEt2}$, $\ce{Sc(OTf)3}$) (Nazarov, 1940s). The acid binds to the carbonyl group to form a 3-hydroxypentadienyl cation (5 carbons, 4 π electrons), which closes by thermal conrotation to give an oxyallyl cation; loss of a proton and tautomerization of the enol gives the ketone. Some regard this as a 4π system and others analyze it with the orbitals of the pentadienyl cation; both views give the same conclusion: conrotation.

![The Nazarov cyclization: the protonated divinyl ketone is a pentadienyl cation with 4 π electrons, which closes by thermal conrotation to an oxyallyl cation; loss of a proton and tautomerization give the cyclopentenone](./plots/nazarov.py)

Since the thermal reaction is conrotatory, the 4π electrocyclization under photoexcitation should instead be disrotatory (by the selection rules of Section 12.3.4, or Definition 12.6.2).

## 12.4. Cycloaddition Reactions

### 12.4.1. Suprafacial and Antarafacial Modes

**Definition 12.4.1 (Cycloaddition)** A reaction in which two (or more) molecules containing π systems bond simultaneously through their termini to form a cyclic compound, without an intermediate, is called a **cycloaddition**. When the two components contain $m$ and $n$ π electrons, it is denoted an $[m+n]$ cycloaddition.

| Reaction | Name |
|---|---|
| Two alkenes → cyclobutane | [2+2] Cycloaddition |
| Conjugated diene + alkene → cyclohexene | [4+2] Cycloaddition (Diels–Alder reaction) |
| 1,3-Dipole + alkene → five-membered heterocycle | [3+2] (1,3-dipolar) cycloaddition |

**Definition 12.4.2 (Suprafacial and Antarafacial)** When the two bonds newly formed (or broken) at one component in a pericyclic reaction lie on the same face of that π system, the component is said to participate in a **suprafacial** (s) manner; when the two bonds lie on opposite faces, the mode is **antarafacial** (a).

The complete notation gives the type, electron count and mode of each component; for example, the dimerization of ethene is written $[\pi 2_{\mathrm{s}} + \pi 2_{\mathrm{s}}]$ and the Diels–Alder reaction $[\pi 4_{\mathrm{s}} + \pi 2_{\mathrm{s}}]$. The antarafacial mode requires twisting of the π system and is almost impossible for short π systems, so the great majority of cycloadditions are suprafacial–suprafacial, and the stereochemistry of the reactants is therefore retained in the product: a cis dienophile gives a cis-substituted product.

For bimolecular reactions, FMO analysis examines the HOMO of one component and the LUMO of the other: the reaction is allowed when both pairs of bonding atoms overlap in phase.

![Frontier orbital analysis of suprafacial cycloadditions (the two components face each other, one above the other, with dashed lines joining the termini that will bond). [2+2]: the HOMO of one alkene and the LUMO of the other are in phase at only one end, and the thermal reaction is forbidden; the HOMO\* of the excited alkene (the former π\*) and the LUMO of the ground-state alkene are in phase at both ends, and the photochemical reaction is allowed. [4+2]: both combinations, diene HOMO with dienophile LUMO and diene LUMO with dienophile HOMO, are in phase at both ends, and the thermal reaction is allowed](./plots/cycloaddition-fmo.py)

Selection rule for suprafacial–suprafacial cycloaddition: $m + n = 4q + 2$ (such as [4+2], [2+2+2]) is thermally allowed; $m + n = 4q$ (such as [2+2], [4+4]) is photochemically allowed.

### 12.4.2. [2+2] Photocycloaddition

The [2+2] cycloaddition of alkenes is symmetry-forbidden thermally but proceeds under ultraviolet irradiation, and is the main method for synthesizing strained four-membered rings. Irradiation of norbornadiene gives quadricyclane (the two double bonds approach in parallel and add intramolecularly). Irradiation of cycloocta-1,5-diene in the presence of $\ce{CuCl}$ gives the "crossed" tricyclo[3.3.0.0²,⁶]octane, not the "parallel" addition product with three fused four-membered rings (Question 4). The [2+2] **photocycloaddition** of α,β-unsaturated ketones with alkenes often proceeds through the triplet state by a stepwise diradical mechanism and is less stereospecific ([6.5.31](/6.5.31#sec-31.3.3)).

### 12.4.3. The Diels–Alder Reaction

**Definition 12.4.3 (Diels–Alder Reaction)** The reaction in which a conjugated diene (the 4π component) and an alkene or alkyne (the 2π component, called the dienophile) undergo suprafacial–suprafacial [4+2] cycloaddition to give a cyclohexene (or cyclohexa-1,4-diene) derivative is called the **Diels–Alder reaction**.

Diels and Alder received the 1950 Nobel Prize in Chemistry for this reaction. It forms two C–C bonds and one six-membered ring in a single step, its stereochemistry is predictable, and it is the most useful method for constructing six-membered carbocycles.

![Curved arrows for the Diels–Alder reaction: the two π bonds of s-cis-buta-1,3-diene and the π bond of ethene shift around the six-membered ring, forming two σ bonds at C1 and C4 and a new π bond between C2 and C3](./plots/diels-alder-arrows.py)

Thermodynamics. For the formation of cyclohexene from butadiene and ethene, the CRC gas-phase data ($\Delta_{\mathrm{f}}H^\circ$: butadiene $110.0$, ethene $52.4$, cyclohexene $-5.0\,\mathrm{kJ\,mol^{-1}}$; $S^\circ$: $278.7$, $219.3$, $310.5\,\mathrm{J\,K^{-1}\,mol^{-1}}$) give $\Delta_{\mathrm{r}}H^\circ \approx -167\,\mathrm{kJ\,mol^{-1}}$ and $\Delta_{\mathrm{r}}S^\circ \approx -188\,\mathrm{J\,K^{-1}\,mol^{-1}}$. The reaction is exothermic because two π bonds are converted into two stronger σ bonds; the entropy decreases because two molecules combine into one and the cyclic transition state freezes rotations. Low temperatures therefore favor addition, and high temperatures (above $\Delta_{\mathrm{r}}H^\circ/\Delta_{\mathrm{r}}S^\circ \approx 900\,\mathrm{K}$) favor the retro-Diels–Alder reaction. Cyclopentadiene slowly dimerizes to dicyclopentadiene at room temperature, and on distillation (about $170\,^\circ\mathrm{C}$) cleaves back to the monomer: a pair of reversible Diels–Alder reactions. For the retro-Diels–Alder fragmentation of cyclohexene-type ions in mass spectrometry see [6.4.15](/6.4.15).

Conformation of the diene. Only a diene in the s-cis **conformation** has its termini close enough to bond simultaneously to the dienophile. Open-chain dienes exist mainly as s-trans ([6.5.11](/6.5.11#sec-11.1.2)) and must first convert to s-cis before reaction; cyclic dienes locked in the s-cis form (cyclopentadiene, furan, cyclohexa-1,3-diene) react particularly fast, and dienes locked in the s-trans form (such as certain fused dienes whose two double bonds lie in two different rings) do not react at all. The inner substituent of a (Z)-1-substituted diene hinders the s-cis conformation, and the reaction is very slow.

Electronic effects. By Section 12.2.2, the pair of frontier orbitals with the smaller energy difference plays the dominant role:

- Normal electron demand: the HOMO of an electron-rich diene (bearing $\ce{-OR}$, $\ce{-NR2}$, $\ce{-OSiR3}$ or alkyl groups) interacts with the LUMO of an electron-poor dienophile (bearing $\ce{-CHO}$, $\ce{-COR}$, $\ce{-CO2R}$, $\ce{-CN}$ or $\ce{-NO2}$). Highly reactive dienes include Danishefsky's diene ((E)-1-methoxy-3-(trimethylsilyloxy)buta-1,3-diene) and 2-aminodienes; highly reactive dienophiles include maleic anhydride, benzoquinone, propiolates and tetracyanoethene. Butadiene reacts very slowly with unactivated ethene itself and requires high temperature and pressure.
- Inverse electron demand (IEDDA): the LUMO of an electron-poor diene (1,2,4,5-tetrazine, 1,2,4-triazine, 2-pyranone) interacts with the HOMO of an electron-rich or strained dienophile (enol ethers, enamines, trans-cyclooctene, norbornene, cyclopropene).

![Energies of the frontier orbitals in Diels–Alder reactions (schematic): the bold arrow marks the pair with the smaller energy gap, which plays the dominant role. Normal electron demand is diene HOMO with dienophile LUMO; a Lewis acid coordinates to the carbonyl group of the dienophile and lowers its LUMO further; inverse electron demand is diene LUMO with dienophile HOMO](./plots/da-electron-demand.py)

Catalysis. When the dienophile contains C=O or C=N, a Lewis acid ($\ce{AlCl3}$, $\ce{BF3}$, $\ce{TiCl4}$) or a protic acid coordinates to the carbonyl oxygen and lowers the energy of the LUMO while increasing the LUMO coefficient on the β carbon, accelerating the reaction by several orders of magnitude and improving the regioselectivity and endo selectivity. The iminium ions formed by condensation of secondary amines with α,β-unsaturated aldehydes likewise lower the LUMO, and chiral secondary amine catalysts thereby achieve asymmetric Diels–Alder reactions (MacMillan, 2000; **organocatalysis** was recognized by the 2021 Nobel Prize in Chemistry).

Regioselectivity. In the reaction of an unsymmetrical diene with a dienophile, 1-substituted dienes give mainly the 1,2-disubstituted ("ortho") product, and 2-substituted dienes mainly the 1,4-disubstituted ("para") product. One explanation is charge distribution: an electron-donating group places partial negative charge at one end of the diene, which bonds to the partially positive β carbon of the dienophile. The more general explanation is in terms of orbital coefficients: bonding is stronger between the two atoms with the largest frontier orbital coefficients, so the bonding positions are determined by the atoms with the largest coefficients in the two components.

```smiles
COC=CC=C.C=CC=O>>COC1C=CCCC1C=O
```

1-Methoxybutadiene and acrolein give 2-methoxycyclohex-3-ene-1-carbaldehyde, with the methoxy and aldehyde groups on adjacent carbons ("ortho").

![Explaining regioselectivity with Hückel orbital coefficients (heteroatom parameters are in the figure script): the HOMO of 1-methoxybutadiene has its largest coefficient at C4 and the LUMO of acrolein has its largest coefficient at Cβ, and bonding between them gives the "ortho" adduct; the HOMO of 2-methoxybutadiene has its largest coefficient at C1, giving the "para" adduct](./plots/da-regiochemistry.py)

Stereospecificity. The Diels–Alder reaction is suprafacial with respect to both components: two substituents that are cis in the dienophile remain cis in the product, and trans remain trans; the two "outside" substituents at the ends of the diene lie on the same side of the ring in the product.

```smiles
C=CC=C.COC(=O)/C=C\C(=O)OC>>COC(=O)[C@@H]1CC=CC[C@@H]1C(=O)OC cis
C=CC=C.COC(=O)/C=C/C(=O)OC>>COC(=O)[C@@H]1CC=CC[C@H]1C(=O)OC trans
```

The endo rule. When a cyclic diene (such as cyclopentadiene) reacts with a dienophile bearing an unsaturated substituent, the substituent can point under the diene (endo) or away from it (exo), giving two diastereomers. On steric grounds the exo transition state should be more favorable and its product more stable, yet experiment shows that the kinetic product is mainly the endo one.

**Definition 12.4.4 (Endo Rule)** In the Diels–Alder reaction, an unsaturated (especially carbonyl) substituent on the dienophile tends to lie beneath the π system of the diene in the transition state, so that the endo adduct is formed mainly. This empirical regularity is called the **endo rule** (Alder rule).

```smiles
C1=CCC=C1.O=C1OC(=O)C=C1>>O=C1OC(=O)[C@H]2[C@H]3C=C[C@H](C3)[C@H]12 endo
```

The classical explanation is secondary orbital interaction: in the endo transition state the LUMO lobe on the carbonyl carbon of the dienophile lies just below the HOMO lobe on C2 (or C3) of the diene, and the two overlap in phase; although no new bond is formed, the transition state is additionally stabilized. Modern calculations show that the contribution of secondary orbital interactions is smaller than originally thought, and that endo selectivity also arises from electrostatic interactions, dispersion and the geometry of the transition state, varying from system to system; as a predictive rule, however, the endo rule is quite reliable for cyclic dienes and electron-poor dienophiles, and Lewis acid catalysis usually raises the endo selectivity.

![Endo and exo transition states (oblique projection, diene above, acrolein below): the dotted lines are the main orbital interactions forming the two σ bonds; in the endo transition state the LUMO lobe on the carbonyl carbon is in phase with the HOMO lobe at C3 of the diene (red dashed line, secondary orbital interaction)](./plots/da-endo-exo.py)

Kinetic versus thermodynamic control. The endo product is the kinetic product, and the exo product is usually more stable. If the retro-Diels–Alder reaction is fast enough under the reaction conditions, a longer reaction time or a higher temperature converts the product to the exo form: furan and maleic anhydride react at room temperature to give mainly the endo adduct after 1 hour, and almost entirely the exo adduct after one day. Furan is an aromatic diene ([6.5.13](/6.5.13#sec-13.8)); addition loses the aromatic stabilization, the adduct is unstable, and the reverse reaction occurs already at room temperature (for a general discussion of **kinetic control** and **thermodynamic control** see [6.5.3](/6.5.3#sec-3.9.2)).

Steps for predicting a Diels–Alder product: (1) identify the diene (s-cis) and the dienophile that take part; (2) draw the new six-membered ring, with the new double bond between C2 and C3 of the diene; (3) determine the regioselectivity from the orbital coefficients (the "ortho, para" rule); (4) retain the cis or trans relationship of the dienophile according to suprafacial–suprafacial addition; (5) for cyclic dienes, determine the orientation of the substituent relative to the bridge by the endo rule.

### 12.4.4. The Inverse-Electron-Demand Diels–Alder Reaction and Bioorthogonal Chemistry

Tetrazines are extremely electron-poor dienes with very low LUMOs, and they undergo inverse-electron-demand [4+2] cycloaddition with strained alkenes (trans-cyclooctene, norbornene) or alkynes; the bicyclic adduct formed immediately loses $\ce{N2}$ by a retro-[4+2] reaction to give a 4,5-dihydropyridazine (which then isomerizes or is oxidized to a pyridazine). The loss of $\ce{N2}$ makes the whole process irreversible.

![Inverse-electron-demand Diels–Alder reaction of a tetrazine: [4+2] cycloaddition gives a bridged bicyclic adduct, which loses $\ce{N2}$ by a retro-[4+2] reaction to give a 4,5-dihydropyridazine](./plots/tetrazine-iedda.py)

This reaction has several unusual properties: it needs no catalyst; it proceeds in water at physiological pH and $37\,^\circ\mathrm{C}$; it does not react with any functional group present in organisms (amines, thiols, carboxylic acids); and its second-order rate constant with trans-cyclooctene can reach $10^3$–$10^6\,\mathrm{L\,mol^{-1}\,s^{-1}}$, making it the fastest bioorthogonal reaction known. It is therefore widely used to label proteins, glycans and drugs in living cells and even in animals, and for "pretargeted" imaging. Ordinary Diels–Alder adducts can undergo the reverse reaction under certain conditions, and some need a catalyst and react slowly, so they are not suitable for biological conjugation. For the general concept of bioorthogonal reactions and other reactions such as CuAAC and strain-promoted azide–alkyne cycloaddition see [6.5.33](/6.5.33) and [6.6](/6.6).

### 12.4.5. 1,3-Dipolar Cycloaddition

A 1,3-dipole is a three-atom, four-π-electron system a–b–c that has among its resonance structures one with formal charges of opposite sign at the two ends (the a⁺–b–c⁻ type; in the structure with complete octets the charges sit on the central atom and one terminus). Common examples are ozone, diazo compounds ($\ce{R2C=N+=N-}$), azides ($\ce{RN=N+=N-}$), nitrones ($\ce{R2C=N+(R)-O-}$) and nitrile oxides ($\ce{RC#N+-O-}$). Its π orbitals resemble those of the allyl anion, and its HOMO has the same symmetry as the HOMO of butadiene (opposite signs at the ends), so suprafacial–suprafacial cycloaddition of [4+2] type (written [3+2] by atom count) to alkenes and alkynes (called dipolarophiles) is thermally allowed.

**Definition 12.4.5 (1,3-Dipolar Cycloaddition)** The reaction in which a 1,3-dipole and a dipolarophile such as an alkene or alkyne undergo concerted suprafacial–suprafacial cycloaddition to form a five-membered heterocycle is called **1,3-dipolar cycloaddition** (Huisgen cycloaddition).

The reaction may proceed through the interaction of the HOMO of the dipole with the LUMO of the dipolarophile, or the reverse, depending on the electronic character of the two. It is stereospecific: diazomethane gives the cis pyrazoline with dimethyl maleate and the trans product with dimethyl fumarate. The cycloaddition of nitrones with alkenes gives isoxazolidines, and reductive cleavage of the N–O bond gives 1,3-amino alcohols, which is useful in alkaloid synthesis. The first step of **ozonolysis** is also a 1,3-dipolar cycloaddition ([6.5.11](/6.5.11#sec-11.8.3)).

![Huisgen 1,3-dipolar cycloaddition of an azide with an alkyne: the four π electrons of the azide and the two π electrons of the alkyne shift around the five-membered ring, giving a 1,2,3-triazole in one step; the thermal reaction gives a mixture of the 1,4- and 1,5-isomers](./plots/dipolar-cycloaddition.py)

The copper(I)-catalyzed azide–alkyne cycloaddition (CuAAC, Sharpless and Meldal, 2002) gives only the 1,4-disubstituted triazole by a stepwise mechanism through copper acetylides and is no longer a pericyclic reaction; it is the representative "click chemistry" reaction and, together with bioorthogonal chemistry, was recognized by the 2022 Nobel Prize in Chemistry (Bertozzi, Meldal, Sharpless; [6.5.24](/6.5.24#sec-24.8.5), [6.5.33](/6.5.33)).

### 12.4.6. [2+2] Cycloaddition of Ketenes

**Ketenes** $\ce{R2C=C=O}$ undergo [2+2] cycloaddition with alkenes on heating to give cyclobutanones, without the need for light, and the reaction is stereospecific (the cis or trans relationship of the alkene is retained). It is traditionally explained as a $[\pi 2_{\mathrm{s}} + \pi 2_{\mathrm{a}}]$ process: the ketene participates antarafacially, which is sterically feasible because the carbonyl carbon of the ketene bears only two atoms and so is little hindered. The current understanding is more specific: the two sets of π orbitals of the ketene, C=C and C=O, are perpendicular to each other, and the HOMO of the alkene interacts mainly with the π* orbital of the ketene C=O (which lies in the molecular plane and has a large coefficient on the central carbon); this pathway, orthogonal to the "forbidden" C=C π* orbital, makes a concerted but highly asynchronous cycloaddition possible, and it can be regarded as a six-electron $[\pi 2_{\mathrm{s}} + (\pi 2_{\mathrm{s}} + \pi 2_{\mathrm{s}})]$ process. The highly reactive dichloroketene (generated in situ from trichloroacetyl chloride and zinc) is often used to synthesize cyclobutanones; the [2+2] addition of ketenes with imines gives **β-lactams** (the Staudinger reaction, [6.5.25](/6.5.25#sec-25.9.2)), but that is a stepwise reaction through a zwitterionic intermediate.

![[2+2] Cycloaddition of dichloroketene (from trichloroacetyl chloride and zinc) with cyclopentene: the π electrons of the alkene attack the central carbonyl carbon of the ketene (using the in-plane C=O π* orbital), and the π electrons of the ketene C=C close the second bond; one concerted but highly asynchronous step gives cis-fused 7,7-dichlorobicyclo[3.2.0]heptan-6-one](./plots/ketene-cycloaddition.py)

## 12.5. Sigmatropic Rearrangements

### 12.5.1. Nomenclature

**Definition 12.5.1 (Sigmatropic Rearrangement)** A concerted reaction in which a σ bond (together with the atom or group attached to it) migrates along a conjugated π system from one position to a new position, with the π bonds shifting at the same time, is called a **sigmatropic rearrangement**. The atoms are numbered from the two ends of the migrating σ bond toward each side (both ends are numbered 1, one side 1, 2, 3, … and the other side 1′, 2′, 3′, …); when the two ends of the new σ bond after migration lie on atoms $i$ and $j$, the reaction is called an $[i,j]$ sigmatropic shift.

- Migration of H or an atom along a π system, with the migrating end unchanged ($i = 1$): [1,3], [1,5] and [1,7] shifts.
- Migration of a σ bond between two allyl units: the [3,3] shift (Cope and Claisen rearrangements); there is also the [2,3] shift (Section 12.7).
- The shift of H from C5 to C1 in cyclopentadiene is a [1,5] shift and not a [1,2] shift: the numbering must be counted along the π system to the position of the new bond (C5–C4=C3–C2=C1). Shifts such as [1,2] and [1,4] are counted for π systems with an even number of atoms and are not common pericyclic processes (a [1,2] shift is a carbocation rearrangement, [6.5.30](/6.5.30)).

### 12.5.2. Thermodynamics

The product of a sigmatropic shift can in principle return to the starting material by the same kind of shift, so the reaction is reversible, and its direction is determined by the stability of reactant and product: formation of a more substituted double bond, a conjugated double bond or a strong C=O bond is favorable. The Claisen rearrangement of an enol ether gives a carbonyl compound (C=O is much stronger than C=C) and is practically irreversible; in the Cope rearrangement of hexa-1,5-dienes that gives a polysubstituted double bond, the equilibrium lies on the more substituted side.

### 12.5.3. Frontier Orbital Analysis

The migrating σ bond is imagined to undergo homolysis into two radicals, and the frontier orbitals of the two fragments are analyzed:

- $[1,j]$ shift: a hydrogen atom (1s orbital) or a carbon atom (p orbital, or $\mathrm{sp^3}$ orbital) with the SOMO of a conjugated radical with an odd number of carbons;
- $[i,j]$ shift: the SOMOs of two conjugated radicals with odd numbers of carbons are combined.

The SOMO of an odd-carbon radical is a nonbonding orbital, and the phases at its ends are: allyl (3 carbons) opposite, pentadienyl (5 carbons) the same, heptatrienyl (7 carbons) opposite, alternating regularly. The migrating group must bond to both ends simultaneously, and therefore:

![Frontier orbital analysis of sigmatropic shifts: (a) [1,5]-H: the pentadienyl SOMO has ends of the same sign, and migration of H on the same face (suprafacial) is allowed. (b) [1,3]-H: the allyl SOMO has ends of opposite sign, suprafacial migration is forbidden, and antarafacial migration is geometrically impossible. (c) [1,3]-C: the migrating carbon bonds to the two ends with the two lobes of its p orbital, suprafacial migration is allowed, but the configuration of the migrating carbon is inverted. (d) [3,3]: the SOMOs of the two allyl groups face each other one above the other, both ends are in phase, and suprafacial–suprafacial migration is allowed](./plots/sigmatropic-fmo.py)

### 12.5.4. [1,j] Hydrogen Shifts

| Shift | Thermal reaction | Photochemical reaction |
|---|---|---|
| [1,3]-H | Antarafacial (geometrically impossible, does not occur in practice) | Suprafacial |
| [1,5]-H | Suprafacial | Antarafacial |
| [1,7]-H | Antarafacial (a large conjugated system is flexible enough to achieve this) | Suprafacial |

The most common is the thermal suprafacial [1,5]-H shift, which passes through a six-membered cyclic transition state and occurs in both open-chain and cyclic systems. 5-Methylcyclopentadiene is converted at room temperature by successive [1,5]-H shifts into a mixture of 1-methyl- and 2-methylcyclopentadiene, so substituted cyclopentadienes are usually mixtures of isomers. The [1,5]-H shift of open-chain dienes requires higher temperatures, and deuterium labeling and chiral substrates have shown that it is suprafacial: the migrating H (or D) leaves from one face of the diene plane and adds on the same face at the other end, and the two possible conformations (differing in the orientation of the substituents of the substrate) give products of different configuration (Question 7).

![Suprafacial [1,5]-H shift of (Z)-penta-1,3-diene: the C5–H bond, the two π bonds and the C1–H bond being formed make up a six-membered cyclic transition state (here the reaction is degenerate and can be observed only with deuterium labeling)](./plots/hydrogen-shift.py)

```smiles
CC1C=CC=C1>>CC1=CCC=C1.CC1=CC=CC1
```

The thermal [1,7]-H shift should be antarafacial by FMO analysis; a triene with seven carbons can twist into a helical shape so that H leaves from one face and adds to the other. In the biosynthesis of vitamin D₃, previtamin D₃ is converted into vitamin D₃ by just such an antarafacial [1,7]-H shift (Section 12.3.5).

### 12.5.5. [1,j] Carbon Shifts

A migrating carbon atom can bond to the two ends with the two lobes of its p orbital (inversion of configuration) or with the same lobe (retention of configuration):

| Shift | Suprafacial pathway of the thermal reaction | Configuration of the migrating carbon |
|---|---|---|
| [1,3]-C | Allowed (using the two lobes) | Inversion |
| [1,5]-C | Allowed (using the same lobe) | Retention |
| [1,7]-C | Allowed (using the two lobes) | Inversion |

Berson used deuterium-labeled bicyclo[3.2.0]heptene to show that the migrating carbon undergoes inversion of configuration in the thermal [1,3]-C shift, in agreement with the Woodward–Hoffmann prediction. Care must be taken in the analysis to identify the symmetry of the reactant: the same shift in a symmetrical molecule may give **enantiomers** as the products of retention and inversion. The [1,5]-C shift is rare in open-chain systems ([1,5]-H shifts are much faster and occur first) but very common in cyclic systems, for example the alkyl shifts in spiro[4.4]nonatetraene and in substituted cyclopentadienes. When several groups can migrate, the approximate order of migratory preference is acyl > hydrogen > phenyl, vinyl > alkyl.

### 12.5.6. The Cope and Claisen Rearrangements

The most common $[i,j]$ shift is the [3,3]-sigmatropic shift. By FMO analysis, the SOMOs of the two allyl radicals face each other one above the other with both ends in phase, so the suprafacial–suprafacial thermal reaction is allowed.

**Definition 12.5.2 (Cope Rearrangement)** The isomerization of hexa-1,5-dienes and their derivatives to another 1,5-diene by a [3,3]-sigmatropic shift is called the **Cope rearrangement**.

**Definition 12.5.3 (Claisen Rearrangement)** The reaction in which an allyl vinyl ether (or allyl aryl ether) undergoes a [3,3]-sigmatropic shift to give a γ,δ-unsaturated carbonyl compound (or an o-allylphenol) is called the **Claisen rearrangement**.

![[3,3]-Sigmatropic shifts. Top: Cope rearrangement of 3-methylhexa-1,5-diene to the more substituted (E)-hepta-1,5-diene. Middle: Claisen rearrangement of an allyl vinyl ether to pent-4-enal; the strong C=O bond makes the reaction irreversible. Bottom: aromatic Claisen rearrangement of allyl phenyl ether, which first gives a cyclohexadienone that tautomerizes to 2-allylphenol](./plots/cope-claisen.py)

Stereochemistry: the chair transition state. The six-atom cyclic transition state can adopt a chair or a boat form, like cyclohexane. Doering and Roth (1962) showed with meso-3,4-dimethylhexa-1,5-diene that the chair is preferred: at $180\,^\circ\mathrm{C}$ it gives 99.7% of (2E,6Z)-octa-2,6-diene and 0.3% of the (2E,6E) isomer. In the chair transition state the two methyl groups of the meso compound are one pseudo-equatorial and one pseudo-axial, the former becoming an E double bond and the latter a Z double bond; only a boat transition state could place both methyl groups equatorial and give the (E,E) product. The racemic (3R,4R)/(3S,4S) isomer, by contrast, has both methyl groups equatorial (or both axial) in the chair and gives mainly the (E,E) product (about 90%) with a little (Z,Z). The chair transition state is lower than the boat by about $25\,\mathrm{kJ\,mol^{-1}}$.

![Chair and boat transition states of the Cope rearrangement (idealized three-dimensional projection; dashed lines are the C3–C4 bond being broken and the C1–C6 bond being formed): meso-3,4-dimethylhexa-1,5-diene gives (E,Z)-octa-2,6-diene through the chair transition state (one methyl equatorial, one axial) and gives the (E,E) isomer only through the boat transition state](./plots/cope-chair-boat.py)

Because the geometry of the transition state is predictable, the [3,3] shift can transfer the information of one stereogenic center to a new stereogenic center with high selectivity, and it is widely used in synthesis. Variants of the Claisen rearrangement (Johnson, Ireland–Claisen, Eschenmoser) and of the Cope rearrangement (the oxy-anion Cope rearrangement, in which an alkoxide accelerates the reaction by a factor of $10^{10}$ or more; the aza-Cope rearrangement) are treated in [6.5.30](/6.5.30). A Claisen rearrangement also occurs in living organisms: chorismate mutase catalyzes the rearrangement of chorismate to prephenate, a step in the biosynthesis of phenylalanine and tyrosine and one of the few known enzyme-catalyzed pericyclic reactions.

![Anionic oxy-Cope rearrangement: the [3,3] shift of the potassium salt of hexa-1,5-dien-3-ol (KH, 18-crown-6) is about 10¹⁰ times faster than that of the neutral alcohol: the C3–C4 bond, weakened by the adjacent alkoxide, breaks as the C1–C6 bond forms; the product is an enolate, which is protonated at work-up to give hex-5-enal, and the strong C=O bond makes the reaction irreversible](./plots/oxy-cope.py)

The aromatic Claisen rearrangement. Allyl phenyl ether rearranges at about $200\,^\circ\mathrm{C}$: the [3,3] shift first gives a cyclohexadienone whose aromaticity has been destroyed, and this rapidly tautomerizes to the more stable aromatic phenol (o-allylphenol), which drives the reaction toward the product. When both ortho positions are substituted, the cyclohexadienone cannot tautomerize, and the allyl group moves to the para position by a further Cope rearrangement (another [3,3] shift) and then tautomerizes to the p-allylphenol. This can be distinguished by labeling the terminal allyl carbon with ¹⁴C: in the ortho product the allyl group is "inverted" (the labeled terminal carbon is attached to the ring), and in the para product, after two inversions, the labeled carbon is again terminal.

### 12.5.7. Bullvalene: A Rapid Reversible Cope Rearrangement

Bullvalene (tricyclo[3.3.2.0²,⁸]deca-3,6,9-triene) has a 1,5-diene unit attached to a cyclopropane, and its degenerate Cope rearrangement is rapid even at room temperature; each rearrangement gives an equivalent structure, and through a series of rearrangements the ten carbon atoms can be arranged in $10!/3 = 1\,209\,600$ equivalent structures, each carbon taking all positions in turn. At about $100\,^\circ\mathrm{C}$ the interconversion is far faster than the NMR time scale, and the ¹H spectrum shows only one sharp singlet ($\delta$ 4.2) and the ¹³C spectrum only one peak; at low temperature the interconversion slows and the spectrum splits into groups of peaks for the olefinic hydrogens ($\delta$ about 5.7), the cyclopropane hydrogens ($\delta$ about 2.1) and the bridgehead hydrogen, whose weighted average over the number of hydrogens is exactly the $\delta$ 4.2 of the high-temperature spectrum (for averaging and exchange of **chemical shifts** see [6.4.12](/6.4.12)). Bullvalene is the classic example of a fluxional molecule.

## 12.6. Aromatic Transition State Theory

### 12.6.1. Hückel Systems and Möbius Systems

Dewar and Zimmerman pointed out that the transition state of a pericyclic reaction is a cyclic arrangement of the atomic orbitals taking part in the reaction, and that the rules for judging whether it is stable are the same as the rules for judging **aromaticity** ([6.5.13](/6.5.13#sec-13.3.1)):

- When the orbitals in the cyclic arrangement all have the same phase relationship (zero or an even number of sign changes between neighboring orbitals), the arrangement is called a Hückel system, with the same energy levels as a cyclic conjugated molecule (Frost circle); with $4n + 2$ electrons it is a closed shell and the transition state is aromatic (stable), and with $4n$ electrons it is antiaromatic;
- when the phase changes an odd number of times (as in a Möbius strip with a twist), the arrangement is called a Möbius system, whose energy levels are different; with $4n$ electrons it is aromatic, and with $4n + 2$ electrons it is antiaromatic.

![Aromatic transition state theory. Left: Hückel orbital arrangement (no phase change) and Möbius arrangement (one phase change, red circle). Middle and right: energy levels of cyclic arrangements computed with numpy (Hückel: $2\cos(2\pi k/N)$; Möbius: $2\cos((2k+1)\pi/N)$, in units of $\lvert\beta\rvert$), filled with 4 or 6 electrons: the Hückel arrangement is a closed shell with 6 electrons, and the Möbius arrangement is a closed shell with 4 electrons](./plots/huckel-mobius.py)

**Definition 12.6.1 (Aromatic Transition State)** In a pericyclic reaction, when the cyclic arrangement of the participating orbitals is a Hückel system with $4n+2$ electrons, or a Möbius system with $4n$ electrons, the transition state is aromatic and stabilized; such a transition state is called an **aromatic transition state**. A pericyclic reaction with an aromatic transition state is thermally allowed, and one whose transition state is antiaromatic is thermally forbidden (photochemically allowed).

To apply the method, draw the atomic orbitals taking part in the reaction (choosing any set of phases), count the number of phase changes around the ring to decide whether it is a Hückel or a Möbius system, and then count the electrons. For example, in the conrotatory closure of butadiene, after rotation of the terminal p orbitals the ring of four orbitals has one phase change; it is a Möbius system with 4 electrons, aromatic, and thermally allowed; the disrotatory mode is a Hückel system with 4 electrons, antiaromatic, and thermally forbidden. The transition state of the Diels–Alder reaction is a Hückel system with 6 electrons, like benzene, and is thermally allowed. This method needs neither symmetry elements nor knowledge of the HOMO, and is especially convenient for systems without symmetry.

### 12.6.2. The Woodward–Hoffmann Rules

The conclusions of the three methods can be summarized in one general selection rule:

**Definition 12.6.2 (Woodward–Hoffmann Rules)** A pericyclic reaction is decomposed into components (π bonds, σ bonds, lone pairs, etc.), and each component is classified by electron count and mode of participation (suprafacial s or antarafacial a). If the total number of $(4q+2)_{\mathrm{s}}$ and $(4r)_{\mathrm{a}}$ components is odd, the reaction is thermally allowed; if it is even, the reaction is thermally forbidden and photochemically allowed. This rule is called the **Woodward–Hoffmann rules**.

Examples: the Diels–Alder reaction $[\pi 4_{\mathrm{s}} + \pi 2_{\mathrm{s}}]$ has one $(4q+2)_{\mathrm{s}}$ component ($\pi 2_{\mathrm{s}}$) and no $(4r)_{\mathrm{a}}$ component, a total of 1, and is thermally allowed; the dimerization of ethene $[\pi 2_{\mathrm{s}} + \pi 2_{\mathrm{s}}]$ has a total of 2 and is thermally forbidden; the conrotatory closure of butadiene can be written $[\pi 4_{\mathrm{a}}]$, with one $(4r)_{\mathrm{a}}$ component, and is thermally allowed. The disrotatory mode is written $[\pi 4_{\mathrm{s}}]$, with a total of 0, and is thermally forbidden.

| Type of reaction | Thermally allowed | Photochemically allowed |
|---|---|---|
| Electrocyclic, $4n$ electrons | Conrotatory | Disrotatory |
| Electrocyclic, $4n+2$ electrons | Disrotatory | Conrotatory |
| Cycloaddition, $m+n = 4q+2$ | Suprafacial–suprafacial | Suprafacial–antarafacial |
| Cycloaddition, $m+n = 4q$ | Suprafacial–antarafacial | Suprafacial–suprafacial |
| Sigmatropic, $i+j = 4q+2$ | Suprafacial–suprafacial | Suprafacial–antarafacial |
| Sigmatropic, $i+j = 4q$ | Suprafacial–antarafacial | Suprafacial–suprafacial |

"Forbidden" means that the activation energy of the concerted pathway is very high, not that the reaction cannot occur at all: the reaction may take a stepwise radical or ionic route (such as triplet photochemical [2+2] or the Staudinger reaction of ketenes with imines), or occur at high temperature.

## 12.7. The Ene Reaction and the [2,3]-Sigmatropic Shift

The ene reaction (Alder-ene reaction): an alkene containing an allylic hydrogen (the ene) reacts with an electron-poor double or triple bond (the enophile) through a six-membered cyclic transition state; the double bond shifts, the allylic hydrogen is transferred to the enophile, and a new C–C bond is formed at the same time. It can be viewed as a combination of a [1,5]-H shift and a [4+2] cycloaddition (six electrons, Hückel transition state) and is thermally allowed, but it needs higher temperatures, or activation of the enophile by a Lewis acid. The "carbonyl–ene reaction", with a carbonyl compound (such as formaldehyde or a glyoxylate) as the enophile, gives homoallylic alcohols; the ene reaction with singlet oxygen $^1\mathrm{O_2}$ as the enophile gives allylic hydroperoxides (the Schenck reaction), one of the pathways of lipid peroxidation; the first step of the allylic oxidation with $\ce{SeO2}$ is also an ene reaction ([6.5.11](/6.5.11#sec-11.8.4)).

The [2,3]-sigmatropic shift: when an allyl group is attached to a negatively charged atom (or an atom with a lone pair), a [2,3] shift occurs through a five-membered cyclic transition state (six electrons, thermally allowed). Rearrangement of the α-carbanion of an allyl ether to a homoallylic alkoxide is called the [2,3]-Wittig rearrangement; the [2,3] shift between allylic sulfoxides and sulfenates (the Mislow–Evans rearrangement), the [2,3] shift of allylic seleninic acids (the second step of $\ce{SeO2}$ oxidation), and the [2,3] shifts of sulfur ylides and ammonium ylides all belong to this class and are treated in detail in [6.5.30](/6.5.30).

![Top: the ene reaction (the allylic hydrogen is transferred to the enophile, the double bond shifts, and a new C–C bond is formed at the same time); bottom: [2,3]-Wittig rearrangement of an allyl ether carbanion to give a homoallylic alkoxide](./plots/ene-wittig.py)

## Summary

A pericyclic reaction (Definition 12.1.1) is a concerted reaction through a cyclic transition state, with no intermediate, stereospecific, and with opposite selectivity under heat and light. The three main types are electrocyclic reactions (Definition 12.3.1), cycloadditions (Definition 12.4.1) and sigmatropic rearrangements (Definition 12.5.1).

Three methods of analysis (with consistent conclusions):

| Method | Criterion | Use |
|---|---|---|
| Frontier orbitals (Definition 12.2.1) | The HOMO (in bimolecular reactions, the HOMO and the other component's LUMO) is in phase at the bonding positions | Simplest |
| Correlation diagram (Definition 12.3.3) | All occupied orbitals correlate with bonding orbitals of the product | Parent systems with symmetry |
| Aromatic transition state (Definition 12.6.1) | Hückel system with $4n+2$ or Möbius system with $4n$ electrons | No symmetry needed |

Summarized as the Woodward–Hoffmann rules (Definition 12.6.2): if the total number of $(4q+2)_{\mathrm{s}}$ and $(4r)_{\mathrm{a}}$ components is odd, the reaction is thermally allowed.

Quick guide to the selection rules: electrocyclic reactions with $4n$ electrons are thermally conrotatory and photochemically disrotatory, and with $4n+2$ electrons thermally disrotatory and photochemically conrotatory (Definition 12.3.2); cycloadditions with $4q+2$ electrons are thermally suprafacial–suprafacial (Diels–Alder, 1,3-dipolar), and with $4q$ electrons photochemically suprafacial–suprafacial ([2+2]); for sigmatropic shifts, [1,5]-H is thermally suprafacial, [1,3]-C is thermally suprafacial with inversion, and [3,3] is thermally suprafacial–suprafacial through a chair transition state.

The Diels–Alder reaction (Definition 12.4.3): s-cis diene; normal electron demand (electron-rich diene + electron-poor dienophile, accelerated by Lewis acids) and inverse electron demand (tetrazine + strained alkene, bioorthogonal); the "ortho, para" regioselectivity comes from orbital coefficients; it is suprafacial for both components and retains cis–trans relationships; the endo rule (Definition 12.4.4) gives the kinetic product, and when the reaction is reversible the thermodynamic exo product is obtained.

Others: 1,3-dipolar cycloaddition (Definition 12.4.5) gives five-membered heterocycles; ketenes undergo thermal [2+2] to give cyclobutanones; the Cope and Claisen rearrangements (Definitions 12.5.2, 12.5.3) proceed through chair transition states and have predictable stereochemistry; the ene reaction and the [2,3]-sigmatropic shift are six-electron thermally allowed processes.

## Questions

1. Use the FMO method to determine the products of ring closure of (2E,4Z,6E)-octa-2,4,6-triene on heating and on irradiation, and state what the (2E,4Z,6Z) isomer gives on thermal ring closure.

   **Answer** Octatriene is a 6π system; for the thermal reaction we look at the HOMO $\psi_3$ (ends of the same sign), and disrotation is allowed; for the photochemical reaction we look at $\psi_4$ (ends of opposite sign), and conrotation is allowed. In the (E,Z,E) isomer both methyl groups at the ends are "outside", and on disrotation the two outer groups turn to the same face of the ring, giving cis-5,6-dimethylcyclohexa-1,3-diene; irradiation (conrotation) gives the trans isomer. In the (E,Z,Z) isomer one methyl group is outside and one inside, and thermal disrotation gives trans-5,6-dimethylcyclohexa-1,3-diene (racemic).

2. Draw the correlation diagram for the electrocyclization of hexa-1,3,5-triene (disrotation maintains the mirror plane σ, conrotation maintains the $C_2$ axis) and state the mode of ring closure in the ground state and in the excited state.

   **Answer** The orbitals to be correlated are $\psi_1$–$\psi_6$ of hexatriene, and σ and σ\* (the new bond) and $\pi_1$–$\pi_4$ of the butadiene unit of cyclohexadiene. With respect to the mirror plane σ: $\psi_1, \psi_3, \psi_5$ of hexatriene are S and $\psi_2, \psi_4, \psi_6$ are A; in the product σ is S and σ\* is A, and $\pi_1$ and $\pi_3$ of the butadiene unit are S and $\pi_2$ and $\pi_4$ are A. The three bonding orbitals of the product in order of energy are σ (S), $\pi_1$ (S) and $\pi_2$ (A), and the three occupied orbitals of the reactant are $\psi_1$ (S), $\psi_2$ (A) and $\psi_3$ (S); the symmetry composition is the same (two S and one A), all correlate with bonding orbitals, and disrotation is allowed in the ground state. With respect to the $C_2$ axis: $\psi_1, \psi_3, \psi_5$ are A and $\psi_2, \psi_4, \psi_6$ are S, so the occupied orbitals are two A and one S, whereas the bonding orbitals of the product, σ (S), $\pi_1$ (A) and $\pi_2$ (S), are two S and one A; one occupied orbital must therefore correlate with an antibonding orbital, and conrotation is forbidden in the ground state and allowed in the excited state. Conclusion: thermally disrotatory and photochemically conrotatory, in agreement with the FMO analysis.

3. What does all-cis cyclodecapentaene rapidly give on heating? Should it be regarded as a $4n$ or a $4n+2$ system?

   **Answer** It undergoes a disrotatory electrocyclization of 6π electrons to give cis-9,10-dihydronaphthalene (the two bridgehead hydrogens cis). The reacting unit is one hexatriene unit of the molecule (6 electrons, $4n+2$), not all 10 π electrons: the other two double bonds in the ring take no part in bonding and are simply carried into the new six-membered ring. In disrotation the two bridgehead hydrogens turn to the same side, so the product is cis-fused.

4. Irradiation of cycloocta-1,5-diene in the presence of $\ce{CuCl}$ gives mainly tricyclo[3.3.0.0²,⁶]octane (two five-membered rings and one four-membered ring), not tricyclo[4.2.0.0²,⁵]octane with three fused four-membered rings. Explain.

   **Answer** There are two ways of [2+2] reaction between the double bonds C1=C2 and C5=C6: formation of the C1–C6 and C2–C5 bonds ("parallel") gives three fused four-membered rings with very large strain; formation of the C1–C5 and C2–C6 bonds ("crossed") forms only one four-membered ring, the other two being five-membered, with much less strain. In the boat conformation of cyclooctadiene the two double bonds face each other in a crossed arrangement, and Cu(I) coordinates to both double bonds simultaneously and holds them still more firmly in the crossed position, so the crossed addition product is formed. This is a photochemical [2+2] cycloaddition (suprafacial–suprafacial, photochemically allowed).

5. Write the major products of the following Diels–Alder reactions (pay attention to regiochemistry and stereochemistry): (a) 2-methylbuta-1,3-diene and methyl acrylate; (b) (E)-penta-1,3-diene and acrolein; (c) cyclopentadiene and methyl (E)-but-2-enoate.

   **Answer** (a) The 2-substituted diene gives the "para" product: methyl 4-methylcyclohex-3-ene-1-carboxylate (racemic). (b) The 1-substituted diene gives the "ortho" product: 2-methylcyclohex-3-ene-1-carbaldehyde; endo selectivity places the methyl and aldehyde groups cis (mainly the cis racemate). (c) Methyl 3-methylbicyclo[2.2.1]hept-5-ene-2-carboxylate; the dienophile is trans, so the ester and methyl groups are trans in the product; by the endo rule the ester group is mainly endo and the methyl group exo.

6. Furan and maleic anhydride give mainly the endo adduct after 1 hour at room temperature and mainly the exo adduct after 1 day. Explain this, and state how the result differs if cyclopentadiene is used.

   **Answer** The endo transition state is lower (secondary orbital interaction, etc.), so the endo adduct forms faster and is the kinetic product; the exo adduct is less hindered and more stable and is the thermodynamic product. Furan is an aromatic diene; addition loses the aromatic stabilization, the adduct is not very stable, and the retro-Diels–Alder reaction can occur already at room temperature, so the endo adduct dissociates and re-adds continually and gradually accumulates as the more stable exo adduct (thermodynamic control). Cyclopentadiene is not aromatic, its adducts are much more stable, and the reverse reaction is very slow at room temperature; the endo product can be isolated and stored, and is converted only on prolonged heating at higher temperature.

7. C5 of a 1,3-diene is a stereogenic center bearing H, D and an ethyl group ($\ce{EtCHD-}$), and undergoes a [1,5]-H (or D) shift on heating. Explain why the stereochemistry of the migration can prove that the reaction is suprafacial.

   **Answer** Of the three groups H, D and Et on C5 before migration, the migrating atom must lie parallel to the π system (perpendicular to the plane of the diene), so there are two conformations from which migration can occur: H above the plane with D and Et elsewhere, or D above. In suprafacial migration, the migrating atom leaves from the upper face of the plane and adds to C1 on the same face; at the same time C5 becomes an sp² carbon, and the orientation of the ethyl group and the remaining H/D on it (E/Z) is determined by the conformation chosen, while C1 becomes a new stereogenic center whose configuration is determined by the face on which the hydrogen adds. The experimentally observed product shows a fixed correspondence between the absolute configuration of the new stereogenic center and the E/Z configuration of the new double bond, and only suprafacial migration can give this correspondence; antarafacial migration would give the opposite combination. (This is how Roth's experiments proved that the [1,5]-H shift is suprafacial.)

8. Decide the direction of equilibrium of the following [3,3] shifts: (a) 3,3-dimethylhexa-1,5-diene ⇌ 1,1-dimethylhexa-1,5-diene; (b) 3-phenylhexa-1,5-diene ⇌ 1-phenylhexa-1,5-diene; (c) allyl vinyl ether ⇌ pent-4-enal.

   **Answer** (a) To the right: a trisubstituted double bond $\ce{(CH3)2C=CH-}$ is formed, more stable than the original monosubstituted double bond. (b) To the right: the phenyl group is conjugated with the new double bond (styrene type). (c) Almost entirely toward the aldehyde: the C=O bond (about $745\,\mathrm{kJ\,mol^{-1}}$) is much stronger than the C=C bond (about $610\,\mathrm{kJ\,mol^{-1}}$), the difference between C–O and C–C single bonds is small, and the overall reaction is exothermic by about $70$–$80\,\mathrm{kJ\,mol^{-1}}$, so it is practically irreversible.

9. 2,6-Dimethylphenyl allyl ether on heating gives 4-allyl-2,6-dimethylphenol. Write the mechanism and predict the position of the label when the terminal allyl carbon is labeled with ¹⁴C.

   **Answer** The first [3,3] shift (Claisen) moves the allyl group to one ortho position, giving 6-allyl-2,6-dimethylcyclohexa-2,4-dienone; this carbon already carries a methyl group and no hydrogen, so the dienone cannot tautomerize to the phenol. The second [3,3] shift (Cope, of the 1,5-diene unit in the dienone) moves the allyl group from the ortho carbon to the para carbon, giving 4-allylcyclohexa-2,5-dienone, whose C4 carries a hydrogen and which tautomerizes to the aromatic 4-allyl-2,6-dimethylphenol. Each [3,3] shift "inverts" the allyl group (the original terminal carbon bonds to the new position), and after two shifts the labeled carbon is again at the allyl terminus: $\ce{ArCH2CH=^{14}CH2}$.

10. The [2+2] cycloaddition of a ketene with an alkene occurs on heating, whereas the [2+2] of two alkenes requires light. Explain the difference in terms of orbitals.

    **Answer** For two ordinary alkenes the suprafacial–suprafacial [2+2] has HOMO–LUMO in phase at only one end and is forbidden; the antarafacial mode requires one alkene to twist and is geometrically infeasible. A ketene has two mutually perpendicular π systems, C=C and C=O. The C=O π\* orbital on the central carbon lies in the molecular plane and has a large coefficient and low energy, and the HOMO of the alkene can interact with it on the same face without being subject to the phase prohibition; at the same time the central carbon of the ketene bears only two atoms and is little hindered, which makes the "suprafacial–antarafacial" or equivalent concerted asynchronous pathway feasible. The [2+2] of ketenes is therefore a thermally allowed concerted reaction and retains the stereochemistry of the alkene.
