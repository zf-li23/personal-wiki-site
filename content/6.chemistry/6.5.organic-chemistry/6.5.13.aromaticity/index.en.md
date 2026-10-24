---
title: Aromaticity
description: The structure and heat of hydrogenation of benzene; valence bond and Hückel molecular orbital descriptions (6α + 8β versus 6α + 6.988β for hexatriene); Hückel's rule and Frost circles; energetic, geometric and magnetic criteria of aromaticity (ring current, NMR, NICS); aromatic ions, antiaromaticity and nonaromaticity; annulenes; fused arenes, azulene, fulvene and homoaromaticity; electronic structure of aromatic heterocycles; metalla-aromaticity; nomenclature of arenes.
source_hash: 4fe762623984
---

Benzene and its derivatives are the most important class of compounds in organic chemistry: aromatic rings are found everywhere in drug molecules, dyes, polymers and natural products. Benzene is highly unsaturated ($\ce{C6H6}$, four degrees of unsaturation), yet it does not undergo addition as readily as alkenes do but tends to undergo substitution, and it is far more stable than any "cyclohexatriene" Lewis structure. This chapter explains where this special stability comes from and how to decide whether a system possesses it. [6.5.1](/6.5.1#sec-1.6) described conjugated systems with **resonance theory**, and [6.5.2](/6.5.2#sec-2.2) with the **Hückel molecular orbital method**; here we apply both to cyclic conjugated systems, obtaining Hückel's rule and its geometric representation, the Frost circle, then discuss the experimental criteria of aromaticity (heat of hydrogenation, bond lengths, ring currents in nuclear magnetic resonance, [6.4.12](/6.4.12)), and extend the rule to ions, annulenes, fused rings and heterocycles. Aromaticity determines how arenes react: it makes aromatic rings undergo substitution rather than addition (electrophilic and nucleophilic aromatic substitution, [6.5.14](/6.5.14)), and it also governs the chemistry of benzyne, Birch reduction, polycyclic arenes and phenols ([6.5.15](/6.5.15)); the "aromatic transition state" in pericyclic reactions uses the same set of rules ([6.5.12](/6.5.12)). The reactions of heteroaromatic compounds are treated in [6.5.25](/6.5.25).

## 13.1. Structure and Stability of Benzene

### 13.1.1. From the Kekulé Structure to the Geometry of Benzene

Faraday isolated benzene in 1825 from the oily condensate of illuminating gas and found a carbon-to-hydrogen ratio of 1∶1. Its molecular formula $\ce{C6H6}$ implies a high degree of unsaturation, yet benzene reacts with bromine and with potassium permanganate unlike an alkene; in the presence of $\ce{FeBr3}$ its reaction with bromine gives a substitution product, bromobenzene, and not an addition product. In 1865 Kekulé proposed that benzene is a six-membered ring with alternating single and double bonds; to explain why there is only one ortho-disubstituted benzene (and not two, with the substituents linked by a single or a double bond), he assumed that the two structures with alternating single and double bonds interconvert rapidly.

Modern structure determinations (electron diffraction, X-ray diffraction, rotational spectroscopy) show that:

- benzene is a planar regular hexagon with all bond angles $120^\circ$;
- the six C–C bonds are of equal length, $139\,\mathrm{pm}$, intermediate between a C–C single bond ($154\,\mathrm{pm}$ in ethane; $148\,\mathrm{pm}$ for the central bond of butadiene) and a C=C double bond ($134\,\mathrm{pm}$); the C–H bond length is $109\,\mathrm{pm}$.

Equal bond lengths show that benzene does not consist of two kinds of molecules with alternating single and double bonds, and Kekulé's "oscillation" is not a real process: according to [resonance theory in 6.5.1](/6.5.1#sec-1.6), the two Kekulé structures are two **resonance structures** of the same molecule, and real benzene is their **resonance hybrid**, in which the six π electrons form a **delocalized pi bond** extending over the entire ring.

### 13.1.2. Heat of Hydrogenation and Aromatic Stabilization Energy

The stability of benzene can be compared quantitatively through heats of hydrogenation. Hydrogenation of cyclohexene to cyclohexane releases $119.7\,\mathrm{kJ\,mol^{-1}}$. If benzene were "cyclohexa-1,3,5-triene" with three isolated double bonds, its heat of hydrogenation would be about $3 \times 119.7 = 359\,\mathrm{kJ\,mol^{-1}}$; the heat of hydrogenation of conjugated cyclohexa-1,3-diene, $231.8\,\mathrm{kJ\,mol^{-1}}$, is only $8\,\mathrm{kJ\,mol^{-1}}$ less than that of two isolated double bonds ($239.4$), which shows that ordinary conjugation brings only a small stabilization. The measured heat of hydrogenation of benzene is only $208.4\,\mathrm{kJ\,mol^{-1}}$, about $151\,\mathrm{kJ\,mol^{-1}}$ ($36\,\mathrm{kcal\,mol^{-1}}$) lower than for "cyclohexatriene". (These are the gas-phase data of Kistiakowsky and coworkers at 355 K.)

![Heats of hydrogenation (kJ/mol, forming the same cyclohexane) of cyclohexene, cyclohexa-1,3-diene, benzene and hypothetical cyclohexa-1,3,5-triene. Benzene lies about 151 kJ/mol below the cyclohexatriene with three isolated double bonds, which is the aromatic stabilization energy of benzene; the conjugation in cyclohexadiene brings only about 8 kJ/mol of stabilization](./plots/hydrogenation-energy.py)

The first step of the hydrogenation of benzene (to cyclohexa-1,3-diene) is even endothermic: the difference of the two heats of hydrogenation gives $\Delta_{\mathrm{r}}H = -208.4 - (-231.8) = +23.4\,\mathrm{kJ\,mol^{-1}}$ for $\ce{C6H6 + H2 -> C6H8}$. Catalytic hydrogenation of benzene therefore needs much more severe conditions than that of alkenes, and once begun the intermediate diene and alkene are hydrogenated faster and cannot be stopped at an intermediate stage ([6.5.15](/6.5.15#sec-15.2.1)).

This stabilization energy of benzene is called the aromatic stabilization energy or resonance energy. Its value depends on the reference chosen: "cyclohexatriene" is obtained by extrapolation from the heat of hydrogenation of cyclohexene, and the value obtained by comparing heats of combustion is similar (about $150\,\mathrm{kJ\,mol^{-1}}$; the polycyclic arenes of [6.5.15](/6.5.15#sec-15.6.1) use the same set of data); if a conjugated open-chain polyene is used as the reference instead (subtracting the contribution of ordinary conjugation, the Dewar resonance energy), the stabilization of benzene is reduced to only about $85\,\mathrm{kJ\,mol^{-1}}$. "Resonance energies" in different publications can therefore differ by a factor of two, and the same reference must be used in comparisons. Whichever reference is used, benzene is clearly more stable than an open-chain conjugated system, and this additional stabilization beyond ordinary conjugation is the energetic meaning of "aromaticity".

### 13.1.3. Reluctant Addition, Ready Substitution

The addition product of benzene and $\ce{Br2}$, 5,6-dibromocyclohexa-1,3-diene, has lost aromaticity, and addition is endothermic; the substitution product, bromobenzene, retains the aromatic ring, and substitution is exothermic. Benzene therefore undergoes substitution with bromine under Lewis acid catalysis: the electrophile first adds to the ring, and the intermediate formed loses a proton to restore the aromatic system ([6.5.14](/6.5.14#sec-14.2.1)). "Resistance to addition and ease of substitution", together with the special stability, planar structure and equalized bond lengths, are the classical characteristics of aromatic compounds.

## 13.2. Valence Bond and Molecular Orbital Descriptions of Benzene

### 13.2.1. Valence Bond Description

All six carbon atoms of benzene are sp² hybridized ([6.1.3](/6.1.3)): each carbon uses three sp² **hybrid orbitals** to form σ bonds to two adjacent carbons and one hydrogen, building the planar six-membered ring skeleton; each carbon has one remaining 2p orbital perpendicular to the plane of the ring, and the six p orbitals are parallel in pairs and overlap sideways, forming a ring-shaped π electron cloud above and below the plane of the ring. Valence bond theory describes this delocalization by two equivalent Kekulé resonance structures (plus three Dewar structures with very small contributions); two completely equivalent major resonance structures are precisely the case of greatest resonance stabilization ([6.5.1](/6.5.1#sec-1.6.3)).

In structural formulas, benzene can be written as one Kekulé structure, or with a circle inside the hexagon to represent the six delocalized π electrons. When writing mechanisms with curved arrows, only the Kekulé structure can be used, because the arrows must show which pair of electrons moves.

### 13.2.2. Hückel Molecular Orbitals

In the **Hückel molecular orbital method** ([6.5.2](/6.5.2#sec-2.2)), the energy levels of an $n$-membered cyclic conjugated system are the **eigenvalues** of the adjacency (circulant) matrix ([Eq. (2.3) of 6.5.2](/6.5.2#eq-2.3)):

$$
E_k = \alpha + 2\beta\cos\frac{2\pi k}{n}, \qquad k = 0, 1, \dots, n-1. \tag{13.1}
$$
The six π molecular orbitals of benzene ($n = 6$), in order of increasing energy, are

| Orbital | $k$ | $E$ | Number of nodal planes | Character |
|---|---|---|---|---|
| $\psi_1$ | 0 | $\alpha + 2\beta$ | 0 | Bonding |
| $\psi_2$, $\psi_3$ | $\pm1$ | $\alpha + \beta$ | 1 | Bonding (degenerate) |
| $\psi_4$, $\psi_5$ | $\pm2$ | $\alpha - \beta$ | 2 | Antibonding (degenerate) |
| $\psi_6$ | 3 | $\alpha - 2\beta$ | 3 | Antibonding |

The number of nodal planes increases with energy, as in linear polyenes ([Theorem 2.2.1 of 6.5.2](/6.5.2#thm-2.2.1)); the difference is that in cyclic systems, apart from the lowest level (and the highest level of an even-membered ring), the levels are doubly degenerate. The six π electrons exactly fill the three bonding orbitals to give a closed-shell structure, with a total π electron energy of

$$
E_\pi = 2(\alpha + 2\beta) + 4(\alpha + \beta) = 6\alpha + 8\beta.
$$

Compare open-chain hexa-1,3,5-triene: its three bonding orbitals are $\alpha + 1.802\beta$, $\alpha + 1.247\beta$ and $\alpha + 0.445\beta$, with $E_\pi = 6\alpha + 6.988\beta$. The two **delocalization energies** (relative to $6\alpha + 6\beta$ for three isolated double bonds; for the definition of delocalization energy see [Definition 2.2.2 of 6.5.2](/6.5.2#def-2.2.2)) are $2\beta$ and $0.988\beta$: joining the ends of the chain into a ring lowers the π electron energy by an additional $\lvert\beta\rvert$ or so. This additional stabilization corresponds to the aromatic stabilization energy of Section 13.1.2 with the polyene as the reference. Note that the energy of each occupied orbital in $E_\pi$ must be multiplied by its electron count, 2.

![Hückel π energy levels of benzene (left) and hexa-1,3,5-triene (right) (units of |β|, with α taken as zero). The bonding orbitals of benzene, α + 2β and α + β (doubly degenerate), are lower than all three bonding orbitals of hexatriene, and the total energy of the six π electrons, 6α + 8β, is lower than the 6α + 6.988β of hexatriene by about 1.01|β|; dots are electrons and numbers are numbers of nodal planes](./plots/benzene-hexatriene.py)

## 13.3. Hückel's Rule and the Frost Circle

### 13.3.1. Hückel's Rule

Eq. (13.1) holds for any $n$. The lowest level of a cyclic conjugated system, $\alpha + 2\beta$, can accommodate only 2 electrons, and each level above it is doubly degenerate and accommodates 4 electrons. Thus when the number of π electrons is $2, 6, 10, 14, \dots$, that is, $4n + 2$, the electrons exactly fill a set of levels, all bonding orbitals are full and there is no half-filled degenerate orbital, giving a stable closed shell; when the number of π electrons is $4n$, the highest pair of degenerate orbitals is only half filled, and by Hund's rule the two electrons occupy the two orbitals separately, forming an unstable diradical (or, if the molecule distorts and lifts the degeneracy, a highly reactive closed-shell molecule).

**Definition 13.3.1 (Hückel's Rule)** A planar, monocyclic, continuously conjugated system (every atom of the ring has a p orbital taking part in the conjugation) is aromatic when the number of π electrons is $4n + 2$ ($n = 0, 1, 2, \dots$) and antiaromatic when the number of π electrons is $4n$. This rule is called **Hückel's rule**, also known as the $4n + 2$ rule.

To apply Hückel's rule, three conditions are checked in turn:

1. Cyclic: an open-chain conjugated system has no aromaticity to speak of.
2. Continuous conjugation: every atom of the ring has a p orbital taking part in the conjugation (an sp² or sp hybridized carbon, or an atom with a lone pair or an empty p orbital); a single sp³ carbon in the ring (such as the $\ce{CH2}$ of cyclopentadiene or cycloheptatriene) interrupts the conjugation.
3. Planarity: the p orbitals must be parallel to overlap effectively; when strain or repulsion between H atoms prevents the ring from remaining planar (cyclooctatetraene, [10]annulene), the rule does not apply and the system is nonaromatic.

A system that satisfies the first two conditions and has $4n+2$ π electrons will often adopt a planar geometry to gain aromatic stabilization; a system with $4n$ π electrons, where possible, twists into a nonplanar shape to avoid antiaromaticity (cyclooctatetraene). In counting π electrons, the electrons of an exocyclic double bond (such as the C=O of cycloheptatrienone) are not counted, although its polarization can change the number of electrons in the ring (Section 13.5.1); a lone pair is counted if it is in a p orbital and takes part in conjugation (the N of pyrrole), and is not counted if it is in an sp² orbital in the plane of the ring (the N of pyridine, Section 13.8).

**Definition 13.3.2 (Nonaromaticity)** A cyclic conjugated system that has no significant cyclic delocalization because it is nonplanar or its conjugation is interrupted, and whose stability is similar to that of the corresponding open-chain conjugated system, is called **nonaromatic**.

In order of stability: aromatic systems are much more stable than the corresponding open-chain conjugated systems, nonaromatic systems are similar to open-chain systems, and antiaromatic systems are less stable than open-chain systems.

### 13.3.2. The Frost Circle

**Definition 13.3.3 (Frost Circle)** Draw a circle of radius $2\lvert\beta\rvert$ centered at $\alpha$ on the energy axis, and inscribe in it a regular $n$-gon with one vertex at the lowest point of the circle; the vertical coordinates of the vertices are the Hückel energy levels of an $n$-membered cyclic conjugated system. This construction is called the **Frost circle** (Frost and Musulin, 1953).

The Frost circle is only a geometric representation of Eq. (13.1): starting from the lowest point, the line from the $k$th vertex to the center makes an angle $2\pi k/n$ with the vertical downward direction, and the height of the vertex is $\alpha + 2\lvert\beta\rvert\cdot(-\cos(2\pi k/n))$, which, with energy increasing upward, is $\alpha + 2\beta\cos(2\pi k/n)$ ($\beta < 0$). It can be read from the figure immediately that every ring has a unique lowest level $\alpha + 2\beta$; even-membered rings have a unique highest level $\alpha - 2\beta$ and odd-membered rings have none; vertices on the horizontal line through the center ($E = \alpha$) are nonbonding orbitals, which occur only when $n$ is a multiple of 4.

![Frost circles for n = 3 to 8. The vertices of each inscribed regular polygon give the Hückel energy levels (units of |β|, relative to α); dots show the electron count that makes the system aromatic: cyclopropenyl cation (2), cyclobutadiene dication (2), cyclopentadienyl anion (6), benzene (6), cycloheptatrienyl cation (6), cyclooctatetraene dianion (10). The dashed line is the nonbonding level E = α](./plots/frost-circles.py)

**Example 13.3.1** Use the Frost circle to determine the electronic structure of cyclobutadiene and cyclooctatetraene.

The energy levels of cyclobutadiene ($n = 4$) are $\alpha + 2\beta$, $\alpha$ (doubly degenerate) and $\alpha - 2\beta$. Of the 4 π electrons, two fill the lowest orbital and the other two occupy the two degenerate nonbonding orbitals singly, giving a triplet diradical; $E_\pi = 2(\alpha + 2\beta) + 2\alpha = 4\alpha + 4\beta$, so the delocalization energy is zero, whereas that of open-chain butadiene is $0.472\beta$, and cyclobutadiene is therefore less stable than butadiene by $0.472\lvert\beta\rvert$ and is antiaromatic. Real cyclobutadiene distorts to a rectangle (alternating single and double bonds), the degeneracy is lifted, and it becomes a singlet, but it is still extremely unstable. Planar cyclooctatetraene ($n = 8$) likewise has two half-filled nonbonding orbitals; real cyclooctatetraene folds into a "tub" shape, avoiding antiaromaticity and becoming an ordinary polyene. After taking up two electrons (10 π electrons, $4n + 2$ with $n = 2$), all bonding and nonbonding orbitals are filled, and the cyclooctatetraene dianion is a planar aromatic ion (Section 13.5.1).

## 13.4. Criteria of Aromaticity

**Definition 13.4.1 (Aromaticity)** The property of a planar (or nearly planar) cyclic conjugated system in which π electrons (or other electrons) are delocalized around the ring, so that the system is markedly more stable than the corresponding localized reference structure and shows equalized bond lengths and the ability to sustain a diamagnetic ring current is called **aromaticity**. Compounds that possess aromaticity are called aromatic compounds.

The word "aromatic" originates in the nineteenth century: a class of compounds obtained from fragrant materials such as gum benzoin, bitter almond oil and wintergreen oil (benzoic acid, benzaldehyde, methyl salicylate) all contain a benzene ring, so compounds containing a benzene ring came to be called aromatic compounds. Today the term has nothing to do with odor but is a concept of electronic structure. Aromaticity is not a directly measurable quantity but a set of mutually related properties, for which four classes of criteria are commonly used:

| Criterion | Aromatic systems | Antiaromatic systems | Method of measurement |
|---|---|---|---|
| Energy | Stabilization (positive aromatic stabilization energy) | Destabilization | Heats of hydrogenation and combustion, calculated energies of isodesmic reactions |
| Geometry | Equalized bond lengths | Increased bond length alternation | X-ray and electron diffraction; bond-length indices (HOMA) |
| Magnetism | Diamagnetic ring current: protons outside the ring deshielded ($\delta$ increased), protons inside and above the ring shielded; NICS negative | Paramagnetic ring current: opposite direction; NICS positive | $^1$H NMR, magnetic susceptibility, NICS calculations |
| Reactivity | Tendency toward substitution, retaining the aromatic ring | Extremely reactive, readily dimerize or add | Chemical reactions |

The magnetic criterion is the most commonly used. When an external magnetic field is perpendicular to the plane of the ring, the delocalized π electrons circulate around the ring, and the induced magnetic field opposes the external field inside the ring and has the same direction as the external field outside the ring near the plane of the ring. This is the **ring-current effect** ([6.4.12](/6.4.12#sec-12.2.3)): the protons of benzene appear at $\delta = 7.3$, clearly downfield of the olefinic protons of cyclohexa-1,3-diene (about $5.8$); protons inside the ring or above it are strongly shielded (Section 13.6). The paramagnetic ring current of $4n$ systems has the opposite direction, and protons outside the ring move upfield.

**Definition 13.4.2 (Nucleus-Independent Chemical Shift)** The negative of the magnetic shielding calculated for a "ghost atom" containing no nucleus, placed at the center of the ring (NICS(0)) or $100\,\mathrm{pm}$ above the plane of the ring (NICS(1)), is called the **nucleus-independent chemical shift** (NICS; Schleyer, 1996).

NICS is a magnetic criterion of computational chemistry: the ring current produces shielding at the center of the ring, and a negative NICS indicates aromaticity, a positive value antiaromaticity and a value near zero nonaromaticity. For example, NICS(0) is about $-9.7\,\mathrm{ppm}$ for benzene and about $+27.6\,\mathrm{ppm}$ for cyclobutadiene (Schleyer and coworkers, 1996). NICS(1) and NICS(1)$_{zz}$, which takes only the component perpendicular to the ring plane, are less affected by local σ-bond effects and are now more commonly used.

The four classes of criteria give consistent conclusions for typical aromatic and antiaromatic systems, but they can disagree in borderline cases (large rings, heterocycles, metallacycles), so "the degree of aromaticity" has a definite meaning only when the criterion is specified.

## 13.5. Aromatic Ions and Antiaromaticity

### 13.5.1. Aromatic Ions

Hückel's rule does not require the system to be neutral. The following ions all satisfy the $4n+2$ rule and are much more stable than the corresponding neutral molecules or open-chain ions:

| Ion | Ring size | π electrons | Preparation and evidence |
|---|---|---|---|
| Cyclopropenyl cation | 3 | 2 | 3-Chlorocyclopropene and $\ce{SbCl5}$ give a stable hexachloroantimonate; the triphenylcyclopropenyl cation (Breslow, 1957) was the first aromatic ion to be synthesized |
| Cyclopentadienyl anion | 5 | 6 | Cyclopentadiene and Na or NaH give $\ce{C5H5^- Na+}$; the $\mathrm{p}K_{\mathrm{a}}$ of cyclopentadiene is about 16 (18.0 in DMSO, [Tables 3.2 and 3.3 of 6.5.3](/6.5.3#sec-3.1.4)), comparable to alcohols and $10^{27}$ times stronger than a simple alkene (about 43) |
| Cycloheptatrienyl cation (tropylium ion) | 7 | 6 | Hydride transfer from cycloheptatriene to the trityl cation; tropylium bromide is an ionic solid soluble in water; the $^1$H NMR spectrum is a single peak ($\delta = 9.2$) |
| Cyclooctatetraene dianion | 8 | 10 | Cyclooctatetraene and K; planar regular octagon with equal bond lengths |

```smiles
C1=CCC=C1.[Na+].[H-]>>[cH-]1cccc1.[Na+].[HH]
C1=CC=CCC=C1.c1ccc(cc1)[C+](c1ccccc1)c1ccccc1>>[cH+]1cccccc1.C(c1ccccc1)(c1ccccc1)c1ccccc1
```

![Formation of aromatic ions. Top: hydride (from NaH) removes a proton from the CH₂ group of cyclopentadiene, releasing H₂; the cyclopentadienyl anion has five equivalent resonance structures, and the negative charge and the six π electrons are spread evenly over the five carbons. Bottom: the trityl cation abstracts a hydride from the CH₂ group of cycloheptatriene (the electron pair of the C–H bond moves to the cationic carbon), giving the tropylium ion, with six π electrons over seven carbons](./plots/aromatic-ions.py)

The cyclopentadienyl anion and the cycloheptatrienyl cation are two symmetrical examples: the five-membered ring bears one negative charge and the seven-membered ring one positive charge, each with 6 π electrons. The negative or positive charge is spread evenly over every carbon of the ring, and the five (seven) C–H bonds are completely equivalent. The stability of such ions can also be measured by "$\mathrm{p}K_{\mathrm{R^+}}$" (the $\mathrm{p}K$ of $\ce{R+ + 2H2O <=> ROH + H3O+}$): the $\mathrm{p}K_{\mathrm{R^+}}$ of the tropylium ion is 4.7, that is, half of it exists as the ion in water at pH 4.7, whereas the trityl cation ($-6.6$) is converted almost completely into triphenylmethanol in water. The cyclopentadienyl anion is the ligand of **metallocenes** such as ferrocene, $\ce{Fe(C5H5)2}$ ([6.5.28](/6.5.28#sec-28.5.3)).

Carbonyl groups and aromatic ions: the C=O bond of cycloheptatrienone (tropone) is highly polarized, and in the charge-separated resonance structure $\ce{C^+-O^-}$ the seven-membered ring is equivalent to a tropylium ion, so tropone has a large dipole moment (about $4.2\,\mathrm{D}$, against about $3.1\,\mathrm{D}$ for cyclohexanone), a strongly basic carbonyl group (protonation gives the hydroxytropylium ion), and behaves like an aromatic compound in many reactions; so does 2-hydroxytropone (tropolone). By contrast, in the charge-separated structure of cyclopentadienone the five-membered ring is a 4π cyclopentadienyl cation, which is extremely unstable, and cyclopentadienone dimerizes rapidly at room temperature.

### 13.5.2. Antiaromaticity

**Definition 13.5.1 (Antiaromaticity)** The property of a planar, monocyclic, continuously conjugated system with $4n$ π electrons of being less stable, because of cyclic delocalization, than the corresponding open-chain conjugated system is called **antiaromaticity** (Breslow, 1965).

Typical antiaromatic systems:

- Cyclobutadiene (4π). The parent cyclobutadiene can be kept only in an inert-gas matrix at 8 K (Chapman, Krantz and others, 1973), and at slightly higher temperature it dimerizes immediately to a tricyclic compound; it can be stored as the $\ce{Fe(CO)3}$ complex (Pettit, 1965), and is released by oxidation with Ce(IV) and trapped as a reactive intermediate. Highly hindered derivatives such as methyl 2,3,4-tri-tert-butylcyclobutadienecarboxylate can be isolated, and the X-ray structure shows pronounced alternation of single and double bonds (a rectangle).
- The cyclopentadienyl cation $\ce{C5H5+}$ (4π). Ionization of 5-iodocyclopentadiene in $\ce{SbF5}$ to give it is much slower than formation of an ordinary allyl cation; the ground state of the pentaphenylcyclopentadienyl cation is a triplet (Breslow and coworkers, 1973), consistent with the two half-filled degenerate orbitals predicted by the Frost circle.
- The cyclopropenyl anion (4π). The $\mathrm{p}K_{\mathrm{a}}$ of triphenylcyclopropene is far higher than that of triphenylmethane, showing that this anion is not resonance-stabilized but destabilized.

Antiaromatic systems can reduce their instability by distortion, by becoming nonplanar, or by coordination to metals (as in cyclobutadieneiron tricarbonyl, where the 4π ring obtains electrons from the metal).

The rule for photoexcited states is the opposite of that for the ground state: in the lowest triplet state (and the lowest excited singlet state), rings with $4n$ π electrons are aromatic and those with $4n + 2$ are antiaromatic (Baird's rule, 1972). This "excited-state aromaticity" has recently been used to design photochemical reactions and molecular photoswitches ([6.5.31](/6.5.31)).

## 13.6. Annulenes

**Definition 13.6.1 (Annulene)** A fully conjugated monocyclic polyene $\ce{C_nH_n}$ ($n$ even) consisting of alternating single and double bonds is called an **annulene**, written [$n$]annulene, as in [18]annulene $\ce{C18H18}$. Benzene is [6]annulene, cyclobutadiene is [4]annulene and cyclooctatetraene is [8]annulene.

Whether a large-ring annulene can remain planar depends on ring strain and on repulsion between the hydrogens inside the ring, so the predictions of Hückel's rule must be judged together with the geometry:

| Annulene | π electrons | Prediction of the rule | Actual | Comment |
|---|---|---|---|---|
| [4] | 4 | Antiaromatic | Antiaromatic | Rectangular, extremely unstable |
| [6] (benzene) | 6 | Aromatic | Aromatic | |
| [8] | 8 | Antiaromatic | Nonaromatic | Tub-shaped, bond lengths alternating between $134$ and $147\,\mathrm{pm}$, properties like an ordinary polyene |
| [10] | 10 | Aromatic | Nonaromatic | The angle strain of the all-cis isomer is too great, and in isomers with trans double bonds the two inner H atoms repel each other; none can be planar; isomerizes or cyclizes above $-80\,^\circ\mathrm{C}$ |
| [12] | 12 | Antiaromatic | Antiaromatic (weak) | Unstable; inner H atoms shifted downfield in NMR (paramagnetic ring current) |
| [14] | 14 | Aromatic | Aromatic (weak) | Some repulsion among the four inner H atoms; the ring deviates slightly from planarity |
| [16] | 16 | Antiaromatic | Antiaromatic | Inner H at $\delta \approx 10.3$ and outer H at $\delta \approx 5.3$, opposite to an aromatic ring |
| [18] | 18 | Aromatic | Aromatic | Nearly planar; the 12 outer H at $\delta \approx 9.3$ and the 6 inner H at $\delta \approx -3.0$ (low temperature) |
| [22], [26] | 22, 26 | Aromatic | Aromatic; aromaticity decreases with increasing ring size | |
| [30] | 30 | Aromatic | Nonaromatic | The ring is too large and too flexible to maintain planar delocalization |

The NMR spectrum of [18]annulene is the classical illustration of the magnetic criterion of aromaticity (Sondheimer, 1962; see [6.4.12](/6.4.12#sec-12.2.3)): the **chemical shifts** of the two sets of protons differ by 12 ppm. Because the shielding and deshielding caused by the ring current are opposite in direction, NMR can be used as an "aromaticity probe": when an electrophile or ligand is held above an aromatic ring, the signals of its protons move upfield.

Bridging can hold a large ring planar, so that the "nonaromatic" [10] and [14]annulenes show aromaticity:

- 1,6-Methano[10]annulene (Vogel, 1964) replaces the two mutually repelling inner H atoms by a $\ce{CH2}$ bridge. The 10 π electrons of the periphery are nearly coplanar, the ring protons appear at $\delta = 6.9$–$7.3$, and the protons of the bridging $\ce{CH2}$, which lies above the ring, appear at $\delta = -0.5$; the X-ray structure shows nearly equal peripheral bond lengths.
- trans-15,16-Dimethyldihydropyrene (Boekelheide) is a bridged [14]annulene: the two methyl groups sit above and below the center of the ring at $\delta = -4.25$, while the peripheral protons appear at $\delta = 8$–$8.7$.

## 13.7. Fused Arenes, Fulvene and Homoaromaticity

### 13.7.1. Polycyclic Arenes

Arenes formed by two or more benzene rings sharing two adjacent carbon atoms are called fused (polycyclic) arenes, such as naphthalene ($\ce{C10H8}$), anthracene and phenanthrene ($\ce{C14H10}$). They are not monocyclic, so strictly Hückel's rule does not apply, but they can be judged by the number of π electrons in the periphery (10 for naphthalene, 14 for anthracene and phenanthrene) or by Hückel calculations. The C1–C2 bond of naphthalene ($136\,\mathrm{pm}$) is shorter than the C2–C3 bond ($142\,\mathrm{pm}$), so bond lengths are not completely equalized; two of the three resonance structures have a double bond at C1–C2, in agreement with the pattern of bond lengths. The C9–C10 bond of phenanthrene ($135\,\mathrm{pm}$) is a double bond in four of its five resonance structures and behaves nearly like an isolated olefinic bond. The mean aromatic stabilization energy per ring of fused arenes is lower than that of benzene, and their reactivity is higher than that of benzene; their reactions and orientation are treated in [6.5.15](/6.5.15#sec-15.6).

An empirical method for judging which ring of a polycyclic arene is "more aromatic" is Clar's rule: among all resonance structures, the one with the largest number of mutually non-adjacent "aromatic sextets" (rings with 6 π electrons that can be written as independent benzene rings) is the most important. Phenanthrene can be drawn with two aromatic sextets (the two terminal rings), with the central C9–C10 a localized double bond; anthracene can be drawn with only one, and any one of its three rings can be a benzene ring only in part, so anthracene is more reactive and less stable than phenanthrene (their empirical resonance energies are about $352$ and $381\,\mathrm{kJ\,mol^{-1}}$).

### 13.7.2. A Nonbenzenoid Arene: Azulene

Azulene ($\ce{C10H8}$, an isomer of naphthalene) consists of a five-membered ring fused to a seven-membered ring and forms deep blue crystals. Its dipole moment is $0.80\,\mathrm{D}$, far greater than that of naphthalene (0): in the charge-separated resonance structure the five-membered ring is equivalent to a cyclopentadienyl anion and the seven-membered ring to a tropylium ion, each ring having 6 π electrons. Electrophilic substitution of azulene therefore occurs at C1 and C3 of the five-membered ring. In contrast, pentalene, formed by fusing two five-membered rings (8 π electrons), and heptalene, formed by fusing two seven-membered rings (12 π electrons), are antiaromatic and extremely unstable; the four-membered ring of benzocyclobutadiene also remains antiaromatic, and fusing benzene rings on both sides of it (biphenylene) disperses the antiaromaticity over the whole molecule.

![Charge-separated resonance structures containing aromatic ions. Top: the polarized C=O bond of tropone gives a structure whose seven-membered ring is a tropylium ion (6 π), hence the large dipole moment and the basic carbonyl group (13.5.1). Middle: in the same structure for cyclopentadienone the five-membered ring is a 4π cyclopentadienyl cation (antiaromatic), which contributes little. Bottom: the charge-separated structure of azulene combines a cyclopentadienyl anion (five-membered ring) with a tropylium ion (seven-membered ring), which explains its dipole moment (negative end on the five-membered ring)](./plots/dipolar-resonance.py)

### 13.7.3. Fulvene

Fulvene (5-methylidenecyclopenta-1,3-diene) is an isomer of benzene with an exocyclic C=C double bond. It is not an aromatic compound and behaves like a polyene (readily adds and polymerizes), but its exocyclic double bond can be polarized: in the charge-separated resonance structure the five-membered ring is a 6π cyclopentadienyl anion, so the better a substituent on the exocyclic carbon stabilizes positive charge (as in 6-dimethylaminofulvene), the greater the dipole moment and the more aromatic the ring. By the same reasoning, sesquifulvalene (a five- and a seven-membered ring joined by a double bond between the rings) and calicene (a three- and a five-membered ring joined) both gain the stabilization of two aromatic ions in their charge-separated resonance structures and have large dipole moments.

### 13.7.4. Homoaromaticity

**Definition 13.7.1 (Homoaromaticity)** The property of a cyclic conjugated system that is interrupted by one (or several) $\mathrm{sp^3}$ atoms but whose p orbitals on the two sides overlap through space across that atom, so that $4n + 2$ electrons are still delocalized around the ring and gain stabilization, is called **homoaromaticity** (Winstein, 1959).

The most typical example is the homotropylium ion (cyclooctatrienyl cation, $\ce{C8H9+}$), obtained by protonation of cyclooctatetraene in $\ce{FSO3H}$: its seven sp² carbons form a 6π delocalized system, and the $\ce{CH2}$ bulges out of the plane of the ring. The magnetic evidence is direct: the H of the $\ce{CH2}$ pointing above the inside of the ring appears at $\delta = -0.73$ and the H pointing outward at $\delta = 5.13$, differing by nearly 6 ppm, which shows a strong aromatic ring current. The stabilization of homoaromaticity is much smaller than that of aromaticity, and requires suitable geometry for the bridging C and the carbons on its two sides.

## 13.8. Electronic Structure of Aromatic Heterocycles

Aromatic compounds containing heteroatoms such as N, O and S in the ring are called aromatic heterocycles. The key to judging their aromaticity is to determine in which orbital the lone pair of the heteroatom lies.

- Pyridine ($\ce{C5H5N}$): isostructural with benzene, N is sp² hybridized and uses a p orbital to contribute one electron to the 6π system; the lone pair is in an sp² orbital in the plane of the ring, orthogonal to the π system, and is not counted among the π electrons. This pair can bind a proton without destroying aromaticity, so pyridine is a base (the $\mathrm{p}K_{\mathrm{a}}$ of pyridinium is 5.23), though much weaker than aliphatic amines (about 10–11) because the sp² lone pair has higher s character ([6.5.3](/6.5.3#sec-3.2)).
- Pyrrole ($\ce{C4H4NH}$): N is sp² hybridized, the N–H bond lies in the plane of the ring, and the lone pair is in a p orbital and, together with the 4 p electrons of the four carbons, forms a 6π system. The lone pair of N is part of the aromatic system, and protonation on N would destroy the aromaticity, so pyrrole has almost no basicity and protonation occurs at C2 (the $\mathrm{p}K_{\mathrm{a}}$ of the conjugate acid is $-3.8$); conversely, the N–H bond is weakly acidic ($\mathrm{p}K_{\mathrm{a}}$ about 17.5, 23.0 in DMSO).
- Furan and thiophene: one lone pair of O or S is in a p orbital and takes part in the 6π system, and the other is in an sp² orbital in the plane of the ring.
- Imidazole: it contains two kinds of N, one like that of pyridine (N3, lone pair in the plane, basic) and one like that of pyrrole (N1–H, lone pair in the π system). The $\mathrm{p}K_{\mathrm{a}}$ of imidazolium is 6.99, close to physiological pH, so the imidazole group of histidine can both donate and accept protons in the active sites of enzymes ([6.5.25](/6.5.25#sec-25.3.1)).

![Where aromatic heterocycles are protonated. Top: the nitrogen lone pair of pyridine is in an sp² orbital in the ring plane and is not part of the π system; after it bonds to the proton, the pyridinium ion still has six π electrons. Bottom: the nitrogen lone pair of pyrrole is part of the 6π system, so protonation occurs at C2: the nitrogen lone pair pushes electrons through the ring, giving an iminium ion (C2 becomes an sp³ CH₂), and the aromatic sextet is destroyed](./plots/heterocycle-protonation.py)

The 6 π electrons of five-membered heterocycles are distributed over 5 atoms, so the ring carbons have a higher electron density than those of benzene; these are "electron-rich" aromatic rings and undergo electrophilic substitution much faster than benzene. The N of pyridine withdraws electrons, the ring carbons are electron-poor, electrophilic substitution is more difficult than for benzene, and nucleophilic substitution is on the contrary easy. The aromaticity of heterocycles, by empirical resonance energy, runs benzene (about 150) > thiophene (about 121) > pyrrole (about 88) > furan (about 67 kJ/mol): the more electronegative the heteroatom, the less willing its lone pair is to delocalize into the ring. The direction of the dipole moment reflects the same thing: in pyridine ($2.2\,\mathrm{D}$) the negative end is on N; in pyrrole (about $1.8\,\mathrm{D}$) N is the positive end, opposite to saturated pyrrolidine, because the lone pair is delocalized into the ring. The aromaticity of fused heterocycles (quinoline, indole, purine) and of nucleobases such as pyrimidine and purine is analyzed in the same way, and their reactions and syntheses are treated in [6.5.25](/6.5.25#sec-25.4).

## 13.9. Metalla-Aromaticity

Replacing one CH of an aromatic ring by a transition-metal complex fragment, so that the d orbitals of the metal take part in the π delocalization around the ring, gives compounds called metallaaromatic compounds. Thorn and Hoffmann (1979) predicted metallabenzenes theoretically, and Roper and coworkers (1982) isolated the first osmabenzene. Xia Haiping and coworkers obtained a series of osmapentalynes from osmium carbyne complexes (*Nat. Chem.* 2013): the M≡C–C bond angle in them is far smaller than the ideal carbyne value of 180°, which would ordinarily mean enormous strain, but once the metal takes part, the pentalene skeleton of the organic part, which should be antiaromatic, becomes an aromatic system, and the ring strain is compensated by aromatic stabilization. Such compounds show optical, electrical and magnetic properties that ordinary organic compounds do not have, and they also show that the rules of Hückel and Möbius ([6.5.12](/6.5.12#sec-12.6.1)) remain valid in rings containing d orbitals.

The study of aromaticity continues to expand: cycloparaphenylenes ([$n$]CPP, first synthesized in 2008 by Jasti and Bertozzi) are the shortest fragments of carbon nanotubes, in which the bent benzene rings retain aromaticity yet carry strain, and the smaller the ring, the smaller the HOMO–LUMO gap; the excited-state aromaticity of Baird's rule (Section 13.5.2) is used to design photoswitches and singlet-fission materials; and all-metal aromatic clusters (such as $\ce{Al4^2-}$) extend the concept of aromaticity to systems without carbon.

## 13.10. Nomenclature of Arenes

[6.5.1](/6.5.1#sec-1.4.4) gave the nomenclature of mono- and disubstituted benzenes. A few additional points:

1. Retained names. The following benzene derivatives are retained in the 2013 IUPAC recommendations and can be substituted further as parent structures:

   | Structure | Name | Comment |
   |---|---|---|
   | $\ce{C6H5OH}$ | phenol | Preferred IUPAC name |
   | $\ce{C6H5NH2}$ | aniline | Preferred IUPAC name |
   | $\ce{C6H5COOH}$ | benzoic acid | Preferred IUPAC name |
   | $\ce{C6H5CHO}$ | benzaldehyde | Preferred IUPAC name |
   | $\ce{C6H5CN}$ | benzonitrile | Preferred IUPAC name |
   | $\ce{C6H5CH3}$ | toluene | Used in general nomenclature; the preferred IUPAC name is methylbenzene |
   | $\ce{C6H5OCH3}$ | anisole | Used in general nomenclature; the preferred IUPAC name is methoxybenzene |
   | $\ce{C6H5CH=CH2}$ | styrene | Used in general nomenclature; the preferred IUPAC name is ethenylbenzene |
   | $\ce{C6H5COCH3}$ | acetophenone | Used in general nomenclature; the preferred IUPAC name is 1-phenylethan-1-one |
   | $\ce{C6H4(CH3)2}$ | xylene | Used in general nomenclature ($o$-, $m$-, $p$-) |

2. Polysubstituted benzenes. With three or more substituents only numerical locants are used. When there is a parent with a retained name, the carbon bearing the characteristic group of the parent is C1, the other substituents receive the lowest locants, and the prefixes are cited in alphabetical order: $\ce{HOC6H3BrCl}$ (OH at 1, Cl at 2, Br at 5) is named 5-bromo-2-chlorophenol. The Chinese nomenclature rules of the Chinese Chemical Society (2017) likewise order the substituents alphabetically by their English names; the ordering by atomic number, which would give "2-chloro-5-bromophenol", is that of the old rules.

   ```smiles
   Oc1cc(Br)ccc1Cl 5-bromo-2-chlorophenol
   Brc1cc(Br)cc(O)c1 3,5-dibromophenol
   COc1ccccc1[N+](=O)[O-] 1-methoxy-2-nitrobenzene
   Cc1cccc(N)c1 3-methylaniline
   ```

3. Aryl groups. Benzene as a substituent is phenyl (Ph), and aryl groups in general are written Ar; $\ce{CH3C6H4-}$ is tolyl, $\ce{C6H5CH2-}$ is benzyl (Bn), and $\ce{C6H5CH=}$ is benzylidene.
4. Numbering of fused arenes. Naphthalene is numbered 1–8 starting from a carbon adjacent to a fusion carbon, the fusion carbons being 4a and 8a; positions 1, 4, 5 and 8 are also called $\alpha$ positions and positions 2, 3, 6 and 7 $\beta$ positions. Anthracene is numbered 1–4 and 5–8 on the outer rings, with the two carbons of the middle ring being 9 and 10; phenanthrene is an exception with retained numbering, C9 and C10 being the CH groups of the middle ring. The two rings of biphenyl are numbered 1–6 and 1′–6′. The nomenclature of the various heterocycles is treated in [6.5.25](/6.5.25).

```smiles
c1ccc2ccccc2c1 naphthalene
c1ccc2cc3ccccc3cc2c1 anthracene
c1ccc2c(c1)ccc1ccccc12 phenanthrene
c1ccc(cc1)-c1ccccc1 biphenyl
c1cc2cccccc2c1 azulene
```

## Summary

- Benzene is a planar regular hexagon with all six C–C bonds $139\,\mathrm{pm}$ long; the heat of hydrogenation ($208.4$ against about $359\,\mathrm{kJ\,mol^{-1}}$ for hypothetical cyclohexatriene) gives an aromatic stabilization energy of about $151\,\mathrm{kJ\,mol^{-1}}$; the value of the stabilization energy depends on the reference structure (about half with a polyene as the reference). Benzene resists addition and undergoes substitution readily.
- Hückel levels (Eq. (13.1)): benzene $\alpha + 2\beta$, $\alpha + \beta$ (×2), $\alpha - \beta$ (×2), $\alpha - 2\beta$, with $E_\pi = 6\alpha + 8\beta$, lower than hexatriene ($6\alpha + 6.988\beta$) by about $\lvert\beta\rvert$; in calculating the total energy each occupied orbital is multiplied by the electron count, 2.
- Hückel's rule (Definition 13.3.1): planar, monocyclic, continuously conjugated systems with $4n+2$ π electrons are aromatic and those with $4n$ are antiaromatic (Definition 13.5.1); nonplanar systems or those with interrupted conjugation are nonaromatic (Definition 13.3.2). The Frost circle (Definition 13.3.3) is the geometric picture of Eq. (13.1).
- Criteria (Definition 13.4.1): energy (stabilization), geometry (equalized bond lengths), magnetism (diamagnetic ring current, outer H downfield and inner H upfield; NICS negative, Definition 13.4.2), reactivity (substitution rather than addition).
- Aromatic ions: cyclopropenyl cation (2π), cyclopentadienyl anion (6π, making the $\mathrm{p}K_{\mathrm{a}}$ of cyclopentadiene about 16), tropylium ion (6π), cyclooctatetraene dianion (10π); antiaromatic: cyclobutadiene, cyclopentadienyl cation, cyclopropenyl anion; in excited states the rule is reversed (Baird).
- Annulenes (Definition 13.6.1): [6], [14] and [18] are aromatic, [4], [12] and [16] antiaromatic, and [8], [10] and [30] nonaromatic because they are nonplanar; bridging can restore the aromaticity of [10] and [14]annulenes.
- Fused arenes have incompletely equalized bond lengths (Clar's rule); azulene has a dipole moment (charge separation between the 5- and 7-membered rings); the aromaticity of fulvene comes from polarization of the exocyclic double bond; homoaromaticity (Definition 13.7.1) bridges an sp³ carbon.
- Heterocycles: the lone pair of pyridine N is in the plane (basic, 5.23), the lone pair of pyrrole N is in the π system (not basic, protonation on C at $-3.8$); furan and thiophene each contribute one lone pair to the conjugation; five-membered heterocycles are electron-rich and pyridine is electron-poor. Metal d orbitals can also take part in aromatic delocalization.

## Questions

1. Use Hückel's rule to decide whether each of the following species is aromatic, antiaromatic or nonaromatic: (a) the cyclopropenyl anion; (b) the cyclopentadienyl cation; (c) the cycloheptatrienyl anion; (d) cyclooctatetraene; (e) cycloheptatrienone; (f) 2-hydroxycycloheptatrienone; (g) all-cis [10]annulene and the isomer with two trans double bonds.

   **Answer** (a) Three-membered ring, 4π, planar and continuously conjugated: antiaromatic. (b) Five-membered ring, 4π: antiaromatic (the ground state is even a triplet). (c) Seven-membered ring, 8π: antiaromatic if it remained planar; the real ion distorts to reduce the antiaromaticity, and cycloheptatriene is therefore only very weakly acidic (far weaker than cyclopentadiene). (d) 8π: antiaromatic if planar, but actually tub-shaped and nonaromatic. (e) After polarization of the carbonyl group the seven-membered ring is equivalent to a 6π tropylium ion, with considerable aromaticity (large dipole moment, strongly basic carbonyl group). (f) As (e); tropolone is aromatic, and its OH has an acidity like that of phenol (in fact stronger than phenol, because the negative charge of the conjugate base can be delocalized onto the carbonyl oxygen). (g) Both satisfy $4n+2$ (10π), but the angle strain of the all-cis isomer is too great, and in the isomer with trans double bonds the two inner H atoms repel each other; neither can be planar, so they are nonaromatic.
2. Arrange cyclopenta-1,3-diene, cyclohepta-1,3,5-triene and cyclopentane in order of decreasing acidity and explain.

   **Answer** Cyclopentadiene > cycloheptatriene > cyclopentane. The conjugate base of cyclopentadiene is a 6π aromatic anion, with a $\mathrm{p}K_{\mathrm{a}}$ of about 16 ([6.5.3](/6.5.3#sec-3.1.4)); the conjugate base of cycloheptatriene is an 8π anion (with a tendency to be antiaromatic), and although the negative charge can be delocalized there is no aromatic stabilization, so its acidity is weaker than that of cyclopentadiene by about 20 $\mathrm{p}K_{\mathrm{a}}$ units; the conjugate base of cyclopentane is a **carbanion** localized on an sp³ carbon, the weakest acid (about 50).
3. Calculate the π electron energies of cyclobutadiene (assumed square) and buta-1,3-diene from the Hückel levels, and explain why cyclobutadiene is antiaromatic.

   **Answer** Square cyclobutadiene: $E = \alpha + 2\beta, \alpha, \alpha, \alpha - 2\beta$; with 4 electrons, $2(\alpha + 2\beta) + 2\alpha = 4\alpha + 4\beta$, equal to that of two isolated double bonds, so the delocalization energy is zero, and two electrons occupy the degenerate nonbonding orbitals singly (a diradical). For butadiene, $E_\pi = 4\alpha + 4.472\beta$ ([6.5.2](/6.5.2#def-2.2.2)). On cyclization the energy rises by $0.472\lvert\beta\rvert$, so cyclobutadiene is less stable even than an open-chain conjugated system, which is antiaromaticity.
4. Use the Frost circle to write the π electron configuration of the cyclooctatetraene dianion and explain why cyclooctatetraene becomes a planar molecule on treatment with potassium.

   **Answer** For $n = 8$ the levels are $\alpha + 2\beta$ (1), $\alpha + 1.414\beta$ (2), $\alpha$ (2), $\alpha - 1.414\beta$ (2) and $\alpha - 2\beta$ (1). The 10 electrons fill $\alpha + 2\beta$, $\alpha + 1.414\beta$ and the two nonbonding orbitals $\alpha$, a closed-shell $4n + 2$ system ($n = 2$); in the planar form it gains aromatic stabilization, enough to offset the angle strain of the planar eight-membered ring (bond angles $135^\circ$). Neutral cyclooctatetraene (8π) would have two half-filled nonbonding orbitals if planar (antiaromatic) and therefore bends into a tub shape.
5. Azulene is blue and has a dipole moment ($0.80\,\mathrm{D}$), whereas its isomer naphthalene is colorless and has no dipole moment. Use resonance structures to explain the direction of the dipole moment of azulene and predict at which position an electrophile attacks azulene.

   **Answer** In one charge-separated resonance structure of azulene, one electron of the seven-membered ring is transferred to the five-membered ring, so that the seven-membered ring becomes a 6π tropylium ion and the five-membered ring a 6π cyclopentadienyl anion; both rings are aromatic, so this structure makes a significant contribution, and the negative end of the dipole moment is on the five-membered ring and the positive end on the seven-membered ring. The electrophile attacks C1 (C3) of the electron-rich five-membered ring, and in the intermediate formed the seven-membered ring retains the tropylium structure, which is the most stable. The color arises from the small HOMO–LUMO gap (the coefficients of the HOMO and LUMO are distributed on different carbons, so the electronic interaction is small).
6. The $^1$H NMR spectrum of [18]annulene at low temperature has two sets of peaks, at $\delta \approx 9.3$ (12 H) and $\delta \approx -3.0$ (6 H). (a) Explain the two sets of peaks. (b) How should the chemical shifts of the inner and outer H of [16]annulene appear? (c) What does it show that the two sets of peaks merge into one on raising the temperature?

   **Answer** (a) [18]Annulene is an 18π aromatic system; the diamagnetic ring current deshields outside the ring (the 12 outer H are shifted downfield) and shields inside the ring (the 6 inner H are shifted upfield, even beyond TMS). (b) [16]Annulene is a $4n$ system and the paramagnetic ring current has the opposite direction: the inner H are shifted downfield (about 10.3) and the outer H upfield (about 5.3). (c) Conformational motion (twisting of the double bonds exchanges the positions of inner and outer H) becomes fast on the NMR time scale, and the two sets of H average to a single peak (dynamic NMR, [6.5.6](/6.5.6#sec-6.5.5)).
7. Pyridine and pyrrole both contain N, but pyridine is a base (conjugate acid $\mathrm{p}K_{\mathrm{a}}$ 5.23) and pyrrole is hardly a base ($-3.8$, with protonation on C). Explain in terms of the orbitals in which the lone pairs lie; which N of imidazole (conjugate acid 6.99) is protonated?

   **Answer** The lone pair of pyridine N is in an sp² orbital in the plane of the ring, orthogonal to the π system, and accepting a proton does not affect aromaticity, so pyridine is basic (the high s character of the sp² orbital makes it less basic than amines). The lone pair of pyrrole N is in a p orbital and is part of the 6π aromatic system; protonation on N would destroy the aromaticity, so the basicity is extremely weak, and a proton can add only to C2 (the cation obtained is still resonance-stabilized). In imidazole it is the pyridine-like N3 that is protonated; in the imidazolium ion formed the two N atoms are equivalent and the positive charge is dispersed by resonance, which is also why imidazole is more basic than pyridine.
