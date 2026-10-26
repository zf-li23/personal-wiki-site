---
title: Water, Weak Interactions, and Biological Buffers
description: Hydrogen bonding and the properties of water; water as a solvent; the hydrophobic effect and its thermodynamics; van der Waals interactions; the cumulative strength of weak interactions; osmosis; biologically relevant pKa values; phosphate, histidine and the open bicarbonate buffer of blood; acidosis and alkalosis; pH and drug absorption; water as a reactant.
---

Water is the most abundant substance in living systems, 70 % or more of the mass of most organisms. Life arose in water, almost all biochemical reactions take place in it, and water is a reactant in many of them. More important for Part I of the course, water shapes every biomolecule: the hydrogen bonds it forms and breaks, the way it screens charges and the way it excludes nonpolar groups determine how **proteins** fold, how nucleic acids pair, how membranes assemble and how molecules recognize each other. This chapter starts the thread "chemical properties → structure → function" (7.1.1) at its root: the weak, noncovalent interactions in an aqueous environment (2.1), the ionization of water and of weak acids (2.2), and the buffers that hold the pH of cells and body fluids constant (2.3), ending with water as a reactant and as part of macromolecular structure (2.4).

The physical chemistry is taken from the chemistry courses and not derived again: **hydrogen bonds** and **van der Waals forces** in [6.1.4](/6.1.4#sec-4.4), **pH**, weak acids, the **Henderson–Hasselbalch equation** and **buffer solutions** in [6.1.9](/6.1.9) and [6.4.2](/6.4.2#sec-2.4), **osmotic pressure** in [6.3.5](/6.3.5#sec-5.3.4), **micelles** in [6.3.19](/6.3.19#sec-19.7). Here we ask what these facts mean for living matter, and we put numbers on them.

## 2.1. Weak Interactions in Aqueous Systems

### 2.1.1. Hydrogen Bonding Gives Water Its Unusual Properties

The water molecule is bent (H–O–H angle $104.5^\circ$, O–H bond length $0.096\,\mathrm{nm}$); the oxygen, more electronegative, carries a partial negative charge and the two hydrogens partial positive charges, and the four electron pairs around the oxygen are arranged nearly tetrahedrally. Each molecule can therefore donate two **hydrogen bonds** and accept two. In ice every molecule forms four, giving an open hexagonal lattice that is less dense than the liquid, so ice floats and insulates the water below it. In liquid water each molecule forms on average about 3.4 hydrogen bonds at any instant; the bonds have lifetimes of only 1–20 ps, so the liquid is a network of "flickering clusters" that continually break and re-form. The energy required to break a hydrogen bond in liquid water is about $23\,\mathrm{kJ\,mol^{-1}}$, compared with $470\,\mathrm{kJ\,mol^{-1}}$ for the covalent O–H bond.

This network explains why water has a higher melting point, boiling point and enthalpy of vaporization ($44\,\mathrm{kJ\,mol^{-1}}$ at $25\,^\circ\mathrm{C}$) than any other common solvent of similar molecular mass, and a high heat capacity and surface tension. The biological consequences are direct: the heat capacity buffers organisms against temperature changes, and evaporation of water (sweat, transpiration) is an efficient way to lose heat.

Hydrogen bonds are not restricted to water. They form whenever a hydrogen atom covalently bonded to an electronegative atom (the *donor*, usually O or N) faces another electronegative atom with a lone pair (the *acceptor*, usually O or N). They are strongest when the three atoms lie on a straight line, because the electrostatic attraction is then maximal; this directionality gives hydrogen-bonded structures a precise geometry. Hydrogen bonds between **peptide** groups build α helices and **β sheets** (7.1.5), those between bases hold the **DNA** **double helix** together and pair **codons** with **anticodons** (7.1.11), and hydrogen bonds orient **substrates** in **enzyme** **active sites** (7.1.8) and **hormones** in **receptors** (7.1.14).

### 2.1.2. Water as a Solvent

Water is a good solvent for charged and polar compounds and a poor one for nonpolar compounds. Ions and polar groups dissolve because water molecules arrange their dipoles around them, and because water screens electrostatic interactions. By Coulomb's law the force between two charges $q_1$ and $q_2$ at distance $r$ in a medium is

$$
F = \frac{q_1 q_2}{4\pi\varepsilon_0\varepsilon_{\mathrm{r}} r^2},
$$
so the interaction is weakened by the **relative permittivity** $\varepsilon_{\mathrm{r}}$, which is $78.5$ for water at $25\,^\circ\mathrm{C}$ but only about $2$–$4$ in the hydrocarbon interior of a membrane or the core of a protein. A salt bridge that is worth little in water can therefore be strong when buried, and charged molecules cross membranes only through channels and **transporters** (7.1.13). Dissolving a salt crystal also increases entropy, as the ordered lattice gives way to hydrated ions free to move.

Nonpolar gases dissolve poorly: their solution is not helped by polar interactions, and moving them from the gas into the ordered solvent lowers entropy.

| Gas | Polarity | Solubility in water / (g L⁻¹) |
|---|---|---|
| $\ce{N2}$ | nonpolar | 0.018 (40 °C) |
| $\ce{O2}$ | nonpolar | 0.035 (50 °C) |
| $\ce{CO2}$ | nonpolar (polar C=O bonds, no net dipole) | 0.97 (45 °C) |
| $\ce{NH3}$ | polar | 900 (10 °C) |
| $\ce{H2S}$ | polar | 1860 (40 °C) |

This is why organisms need carriers: $\ce{O2}$ is transported bound to hemoglobin and stored bound to myoglobin (7.1.7), and $\ce{CO2}$ travels mainly as the very soluble bicarbonate ion (2.3.3).

Many biomolecules are *amphipathic*: they contain both polar or charged regions and nonpolar regions. **Fatty acids**, phospholipids, **bile salts** and detergents are **amphiphiles**; so, in a sense, are proteins, whose surfaces are mostly polar and whose interiors are mostly nonpolar.

### 2.1.3. The Hydrophobic Effect

When an amphipathic compound is mixed with water, the polar parts interact with the solvent and the nonpolar parts cluster together, forming **micelles** or bilayers in which the smallest possible hydrophobic surface is exposed.

**Definition 2.1.1 (Hydrophobic effect)** The tendency of nonpolar molecules or nonpolar groups in an aqueous solution to associate with one another and minimize their contact with water is called the **hydrophobic effect**. At room temperature it is driven mainly by the increase in the entropy of water, released from the ordered shells that surround the separated nonpolar groups; it does not arise from a special attraction between the nonpolar groups themselves.

The thermodynamics of transfer of a hydrocarbon into water shows this signature. Water cannot hydrogen-bond to the nonpolar solute, and the water molecules around it adopt orientations that preserve their own hydrogen bonds; this restricts their freedom (negative $\Delta S$), while the enthalpy change near room temperature is small. The transfer has a large positive heat capacity change $\Delta C_p$, so $\Delta H$ and $\Delta S$ both depend strongly on temperature:

$$
\Delta H(T) = \Delta C_p\,(T - T_H), \qquad \Delta S(T) = \Delta C_p\ln\frac{T}{T_S}, \qquad \Delta G = \Delta H - T\Delta S,
$$
where $T_H$ and $T_S$ are the temperatures at which $\Delta H$ and $\Delta S$ vanish. For liquid hydrocarbons dissolving in water $T_H \approx 22\,^\circ\mathrm{C}$ and $T_S \approx 112\,^\circ\mathrm{C}$ (Baldwin's convergence temperatures). With $\Delta C_p = +225\,\mathrm{J\,mol^{-1}\,K^{-1}}$ for benzene the model gives $\Delta G(25\,^\circ\mathrm{C}) \approx +18\,\mathrm{kJ\,mol^{-1}}$, close to the value $-RT\ln x = +19\,\mathrm{kJ\,mol^{-1}}$ obtained from the solubility of benzene (mole fraction $x \approx 4 \times 10^{-4}$).

![Thermodynamics of the hydrophobic effect: transfer of benzene from liquid benzene into water, modelled with a constant heat capacity change ΔCp = +225 J mol⁻¹ K⁻¹ and convergence temperatures T_H = 22 °C (ΔH = 0) and T_S = 112 °C (ΔS = 0). Near room temperature the unfavourable ΔG ≈ +18 kJ mol⁻¹ comes almost entirely from −TΔS, the ordering of water; at higher temperatures the entropic term shrinks and ΔH takes over, while ΔG changes little](./plots/hydrophobic-effect.py)

Two consequences recur throughout the course. First, the Gibbs energy of transfer grows roughly in proportion to the nonpolar surface area buried, about $10\,\mathrm{kJ\,mol^{-1}\,nm^{-2}}$, or $3$–$4\,\mathrm{kJ\,mol^{-1}}$ per methylene group; this is the main driving force of protein folding (7.1.6), of the association of **subunits** (7.1.5) and of membrane formation (7.1.12–7.1.13). Second, the large $\Delta C_p$ of exposing nonpolar groups explains why proteins unfold not only on heating but also, less familiarly, on cooling (cold **denaturation**, 7.1.6). Hydrophobic pockets in enzymes and receptors bind nonpolar substrates and **ligands** such as **steroid hormones**; the release of ordered water from both surfaces when they meet favours binding, and drug design exploits this.

### 2.1.4. van der Waals Interactions

When two uncharged atoms come close, the fluctuating electron cloud of each induces a dipole in the other, and the two dipoles attract weakly; at shorter distances the electron clouds repel strongly. These **van der Waals forces** ([6.1.4](/6.1.4#sec-4.4.3)) act between all pairs of atoms, polar or not, and are often described by the Lennard-Jones potential

$$
V(r) = 4\varepsilon_{\mathrm{LJ}}\left[\left(\frac{\sigma}{r}\right)^{12} - \left(\frac{\sigma}{r}\right)^{6}\right],
$$
in which the attractive $r^{-6}$ term dominates beyond the minimum at $r_0 = 2^{1/6}\sigma$ and the repulsive term inside it. The minimum, the van der Waals contact distance, is approximately the sum of the van der Waals radii of the two atoms: H 0.11, O 0.15, N 0.15, C 0.17, S 0.18 and P 0.19 nm (compared with covalent radii of 0.03–0.11 nm). The depth of the minimum is only about $0.4$–$4\,\mathrm{kJ\,mol^{-1}}$ per atom pair, but because the interaction is universal and steep, its total over a well-packed interface is large: the closely packed interiors of proteins, the stacked bases of nucleic acids and the shape complementarity of an enzyme and its substrate all owe much of their stability to it.

### 2.1.5. Weak Interactions Are Weak Individually and Strong Collectively

**Definition 2.1.2** Hydrogen bonds, ionic interactions, the hydrophobic effect and van der Waals interactions are called **noncovalent interactions** ("weak interactions"): attractions between atoms or groups that do not share electron pairs. Unlike covalent bonds they are reversible at physiological temperature, continually forming and breaking.

| Interaction | Typical net Gibbs energy in water / (kJ mol⁻¹) | Distance dependence | Directional? | Examples |
|---|---|---|---|---|
| hydrogen bond | 4–6 (neutral), 6–10 (one partner charged) | short range, $\sim 0.3\,\mathrm{nm}$ donor–acceptor | yes | **α helix**, **base pairs**, substrate binding |
| ionic interaction (salt bridge) | 4–20 (more when buried) | $r^{-1}$ (energy), screened by water and ions | no | Lys–Glu pairs, DNA–**histone** binding |
| hydrophobic effect | 3–4 per buried $\ce{CH2}$ | depends on buried area | no | protein core, **lipid bilayer** |
| van der Waals | 0.4–4 per atom pair | $r^{-6}$ attraction | no | close packing, base stacking |
| covalent bond, for comparison | 350 (C–C), 410 (C–H), 460 (O–H) | | yes | |

![Energies of single interactions on a logarithmic scale. Noncovalent interactions in water (van der Waals contacts, the hydrophobic effect per buried methylene group, hydrogen bonds and ion pairs) are only one to ten times the thermal energy RT = 2.6 kJ mol⁻¹ at 37 °C, so they form and break continually; ATP hydrolysis under cellular conditions releases 50–65 kJ mol⁻¹, and covalent bonds require 350–460 kJ mol⁻¹](./plots/interaction-energies.py)

Each noncovalent interaction is only a few times the **thermal energy** $RT$ ($2.6\,\mathrm{kJ\,mol^{-1}}$ at $37\,^\circ\mathrm{C}$), and in water much of its strength is offset by the interactions with water that must be given up. Their importance lies in their number. A binding equilibrium constant depends exponentially on the binding Gibbs energy, $K = \mathrm{e}^{-\Delta G/RT}$, so every $5.7\,\mathrm{kJ\,mol^{-1}}$ of additional favourable interaction multiplies the affinity by ten; a dozen weak interactions acting together can give **dissociation constants** in the nanomolar range. To dissociate two molecules held by many weak interactions, all of them must break at the same moment, which is very improbable because each fluctuates independently. The most stable (native) structure of a **macromolecule** is accordingly the one in which hydrogen bonding is maximized within the molecule and with the solvent, and in which hydrophobic groups are buried away from water. The same principle governs the binding of an **antigen** to an **antibody** (7.1.7), of a substrate to an enzyme, whose **binding energy** is the main source of catalytic power (7.1.8), and of a hormone to its receptor.

### 2.1.6. Concentrated Solutes Produce Osmotic Pressure

Solutes lower the chemical potential of water ([6.3.5](/6.3.5#sec-5.3.4)). When two solutions are separated by a membrane permeable to water but not to the solutes, water moves towards the side with the higher solute concentration until the **osmotic pressure** difference is balanced. For dilute solutions the osmotic pressure is given by the van 't Hoff equation

$$
\Pi = RT\sum_j i_j c_j,
$$
where $c_j$ is the molar concentration of solute $j$ and $i_j$ its van 't Hoff factor (the number of particles per formula unit: 2 for fully dissociated NaCl, 1 for glucose).

**Definition 2.1.3** The movement of water across a semipermeable membrane driven by a difference in osmotic pressure is called **osmosis**. The sum $\sum_j i_j c_j$ is the **osmolarity** of the solution. A solution with the same osmolarity as the cytosol of a cell is *isotonic* to that cell; one with higher osmolarity is *hypertonic* (the cell shrinks), one with lower osmolarity *hypotonic* (the cell swells and may burst).

The pressures are large. Mammalian plasma and cytosol have about $0.29\,\mathrm{osmol\,L^{-1}}$, so a cell placed in pure water at $37\,^\circ\mathrm{C}$ would experience $\Pi = (290\,\mathrm{mol\,m^{-3}})(8.314\,\mathrm{J\,mol^{-1}\,K^{-1}})(310\,\mathrm{K}) \approx 7.5 \times 10^5\,\mathrm{Pa}$, more than seven atmospheres. Since cells generally contain more solutes than their surroundings, osmosis tends to drive water in, and organisms have evolved several ways to prevent osmotic lysis:

| Organism | Mechanism |
|---|---|
| bacteria, fungi, plants | rigid cell wall resists swelling; in plants the resulting turgor pressure stiffens tissues (wilting = loss of turgor; [Plant Physiology](/7.13)) |
| freshwater protists | contractile vacuoles pump water out |
| multicellular animals | extracellular fluid kept isotonic (plasma proteins such as albumin, salts); $\ce{Na+}$ continually pumped out by the $\ce{Na+}/\ce{K+}$-ATPase (7.1.13) |

Osmolarity counts particles, not mass. One gram of **glycogen** made of 1000 glucose units has the osmotic effect of one milligram of glucose: storing fuel as polysaccharide rather than as free sugar (7.1.10, 7.1.19) avoids a catastrophic rise in the osmotic pressure of the storage cell. Osmosis also matters in the laboratory: organelles bounded by semipermeable membranes swell and burst in hypotonic media, so cell fractionation is done in isotonic sucrose (7.1.4).

**Example 2.1.1** The main solutes of lysosomes are about $0.1\,\mathrm{M}$ KCl and $0.03\,\mathrm{M}$ NaCl. What concentration of sucrose is isotonic with them? The osmolarity is $2(0.1) + 2(0.03) = 0.26\,\mathrm{osmol\,L^{-1}}$; sucrose does not dissociate ($i = 1$), so a $0.26\,\mathrm{M}$ sucrose solution is isotonic. (Real lysosomes also contain other solutes, so somewhat higher sucrose concentrations are used in practice.)

## 2.2. Ionization of Water, Weak Acids, and Weak Bases

### 2.2.1. Water Ionizes, and Protons Move Fast

Water ionizes slightly, $\ce{H2O <=> H+ + OH-}$ (the proton is immediately hydrated, $\ce{H3O+}$ and larger clusters). The **ion product of water** $K_{\mathrm{w}} = [\ce{H+}][\ce{OH-}]$ is $1.0 \times 10^{-14}\,\mathrm{M^2}$ at $25\,^\circ\mathrm{C}$, so pure water has $[\ce{H+}] = 10^{-7}\,\mathrm{M}$, $\mathrm{pH} = 7$ and $\mathrm{pH} + \mathrm{pOH} = 14$ ([6.1.9](/6.1.9#sec-9.2)). $K_{\mathrm{w}}$ increases with temperature: at $37\,^\circ\mathrm{C}$ it is $2.4 \times 10^{-14}\,\mathrm{M^2}$, and the neutral point is pH 6.8, a useful reminder that "pH 7 = neutral" holds only at $25\,^\circ\mathrm{C}$. Only one water molecule in about $5 \times 10^8$ is ionized, which is why pure water conducts electricity so poorly.

Protons nevertheless move through water much faster than other ions of similar size. They do not diffuse as particles: a proton jumps from a hydronium ion to a neighbouring hydrogen-bonded water molecule, which passes another proton on, so that the charge travels along chains of hydrogen bonds (*proton hopping*, the Grotthuss mechanism). Proton hopping makes acid–base reactions in water among the fastest known (rate constants near the diffusion limit), and it is used by proteins: chains of bound water molecules conduct protons through **cytochrome** *f* in **photosynthesis** and through the proton channels of the **respiratory chain** and **ATP synthase** (7.1.23).

The pH of body fluids and compartments spans a wide range:

| Fluid or compartment | pH |
|---|---|
| gastric juice | 1.5–3.0 |
| lysosome, plant vacuole | 4.5–5.5 |
| urine | 5–8 (typically 6) |
| cytosol of animal cells | 7.0–7.4 (typically 7.2) |
| blood plasma, interstitial fluid | 7.35–7.45 |
| mitochondrial matrix | about 7.8–8.0 |
| pancreatic juice | 7.8–8.0 |

### 2.2.2. pKa Is a Property of a Group in Its Environment

Weak acids and bases ionize only partly, to an extent given by the **acid dissociation constant** $K_{\mathrm{a}}$ and $\mathrm{p}K_{\mathrm{a}} = -\lg K_{\mathrm{a}}$ ([6.1.9](/6.1.9#sec-9.3)). The **Henderson–Hasselbalch equation** $\mathrm{pH} = \mathrm{p}K_{\mathrm{a}} + \lg([\ce{A-}]/[\ce{HA}])$ is equivalent to the statement that the fraction of a group in its protonated form is

$$
f_{\ce{HA}} = \frac{1}{1 + 10^{\,\mathrm{pH} - \mathrm{p}K_{\mathrm{a}}}}.
$$
One pH unit above the $\mathrm{p}K_{\mathrm{a}}$ the group is 91 % deprotonated, two units above 99 %; a group is half-protonated exactly at $\mathrm{pH} = \mathrm{p}K_{\mathrm{a}}$. The biologically important values are:

| Conjugate acid / base | $\mathrm{p}K_{\mathrm{a}}$ |
|---|---|
| $\ce{H3PO4}$ / $\ce{H2PO4-}$ | 2.14 |
| α-carboxyl of an amino acid (glycine) | 2.34 |
| $\ce{H2CO3}$ / $\ce{HCO3-}$ | 3.57 |
| acetic acid / acetate | 4.76 |
| side-chain carboxyls of Asp, Glu (free amino acids) | 3.65, 4.25 |
| imidazolium / imidazole of His (free amino acid) | 6.0 |
| $\ce{CO2(d)}$ / $\ce{HCO3-}$ (apparent, plasma at 37 °C) | 6.1 |
| $\ce{H2PO4-}$ / $\ce{HPO4^2-}$ (at physiological ionic strength; thermodynamic value 7.21) | 6.86 |
| HEPES, Tris (laboratory buffers) | 7.5, 8.1 |
| $\ce{NH4+}$ / $\ce{NH3}$ | 9.25 |
| α-amino group (glycine) | 9.60 |
| $\ce{HCO3-}$ / $\ce{CO3^2-}$ | 10.33 |
| $\ce{HPO4^2-}$ / $\ce{PO4^3-}$ | 12.4 |

A $\mathrm{p}K_{\mathrm{a}}$ is not a fixed property of a functional group but of the group *in its environment*. The α-carboxyl group of glycine ($\mathrm{p}K_{\mathrm{a}} = 2.34$) is far more acidic than acetic acid (4.76), because the nearby positively charged α-amino group stabilizes the carboxylate anion (7.1.3). In proteins the shifts can be larger: a group buried in a nonpolar pocket, where the charged form is not stabilized by water, shifts its $\mathrm{p}K_{\mathrm{a}}$ towards the neutral form (the Lys at the active site of acetoacetate decarboxylase has $\mathrm{p}K_{\mathrm{a}} \approx 6$ instead of 10.5, and is therefore nucleophilic at neutral pH), whereas a neighbouring opposite charge shifts it the other way. Enzymes exploit these shifts to tune acid–base catalysts (7.1.8).

### 2.2.3. Buffers in Numbers

A buffer, a mixture of a weak acid and its conjugate base, resists changes in pH because the added $\ce{H+}$ or $\ce{OH-}$ is consumed by converting one buffer form into the other ([6.1.9](/6.1.9#sec-9.5)). Its **buffer capacity** is maximal at $\mathrm{pH} = \mathrm{p}K_{\mathrm{a}}$ and becomes small more than one unit away; the useful range is $\mathrm{p}K_{\mathrm{a}} \pm 1$, between 10 % and 90 % titration of the acid. Two calculations show how much a buffer does.

**Example 2.2.1** A buffer contains $0.042\,\mathrm{M}$ $\ce{NaH2PO4}$ and $0.058\,\mathrm{M}$ $\ce{Na2HPO4}$ ($\mathrm{p}K_{\mathrm{a}} = 6.86$). Its pH is $6.86 + \lg(0.058/0.042) = 7.0$. Adding $1.0\,\mathrm{mL}$ of $10.0\,\mathrm{M}$ NaOH to one litre converts $0.010\,\mathrm{mol}$ of $\ce{H2PO4-}$ into $\ce{HPO4^2-}$: $\mathrm{pH} = 6.86 + \lg(0.068/0.032) = 7.2$. The same amount of NaOH added to a litre of pure water at pH 7.0 gives $[\ce{OH-}] = 0.010\,\mathrm{M}$ and pH 12.

**Example 2.2.2** How much $0.1\,\mathrm{M}$ acetic acid and $0.1\,\mathrm{M}$ sodium acetate must be mixed to make one litre of buffer of pH 5.8? From $5.8 = 4.76 + \lg([\ce{A-}]/[\ce{HA}])$, the ratio $[\ce{A-}]/[\ce{HA}] = 10^{1.04} \approx 11$; hence $1000 \times 10.96/11.96 \approx 916\,\mathrm{mL}$ of acetate and $84\,\mathrm{mL}$ of acetic acid. (The common rounded answer, ratio 10 and 909/91 mL, gives pH 5.76.) Since pH 5.8 lies 1.04 units above the $\mathrm{p}K_{\mathrm{a}}$, at the edge of the buffering range, a buffer with a $\mathrm{p}K_{\mathrm{a}}$ nearer 5.8 (MES, $\mathrm{p}K_{\mathrm{a}} = 6.27$) would be the better choice in practice.

## 2.3. Buffering against pH Changes in Biological Systems

### 2.3.1. Why pH Must Be Controlled

Almost every biological process depends on pH. Enzymes have pH optima that match their environment (pepsin of the stomach near pH 2, trypsin of the small intestine near pH 8, the alkaline phosphatase of bone near pH 10), because the catalytic and binding groups must be in the right state of protonation (7.1.8); the solubility of polar molecules depends on which of their groups carry charges; the binding of $\ce{O2}$ to hemoglobin depends on pH (the **Bohr effect**, 7.1.7). A change of only 0.3 units doubles or halves $[\ce{H+}]$. Cells and organisms therefore keep pH within narrow limits, by buffers on the scale of seconds and by transport and excretion over minutes to hours. Three buffer systems dominate in vivo; in vitro biochemists use **Good's buffers** such as HEPES, PIPES and MES ([6.4.2](/6.4.2#sec-2.4.3)), which have $\mathrm{p}K_{\mathrm{a}}$ values near 7 and interact little with metal ions and membranes.

### 2.3.2. The Phosphate and Histidine Buffers

The phosphate buffer, $\ce{H2PO4- <=> H+ + HPO4^2-}$ with $\mathrm{p}K_{\mathrm{a}} = 6.86$ under physiological conditions, is the main inorganic buffer of the cytoplasm. Cells contain inorganic phosphate at millimolar concentrations and, in addition, many organic phosphates (sugar phosphates, nucleotides) whose phosphate groups have similar $\mathrm{p}K_{\mathrm{a}}$ values.

Proteins are the other main intracellular buffer, chiefly through their histidine **residues**. The imidazolium group of free histidine has $\mathrm{p}K_{\mathrm{a}} = 6.0$, and in proteins the value ranges roughly from 5 to 8; His is the only amino acid **side chain** that is partly protonated near pH 7 and therefore buffers effectively at neutral pH. Hemoglobin, with 38 His residues per tetramer and present in red blood cells at about $5\,\mathrm{mM}$, contributes most of the non-bicarbonate buffering of blood. The same property makes His the most common general acid–base catalyst of enzymes (7.1.8).

### 2.3.3. The Bicarbonate Buffer System Is Open

Blood plasma is buffered mainly by bicarbonate, through three coupled equilibria:

$$
\ce{CO2(g) <=> CO2(d)}, \qquad \ce{CO2(d) + H2O <=> H2CO3}, \qquad \ce{H2CO3 <=> H+ + HCO3-}.
$$
The first is the solution of gaseous $\ce{CO2}$ in the alveolar space of the lungs, governed by Henry's law: in plasma at $37\,^\circ\mathrm{C}$, $[\ce{CO2(d)}] = 0.23\,\mathrm{mM\,kPa^{-1}} \times p_{\ce{CO2}}$. The second, the hydration of $\ce{CO2}$, is slow uncatalysed but very fast in red blood cells, which contain carbonic anhydrase; its equilibrium lies far to the left ($[\ce{H2CO3}]/[\ce{CO2(d)}] \approx 1/600$). The third is the ionization of carbonic acid, a fairly strong acid with $\mathrm{p}K_{\mathrm{a}} = 3.57$. Combining the second and third equilibria gives an apparent $\mathrm{p}K_{\mathrm{a}}' = 6.1$ for the pair $\ce{CO2(d)}/\ce{HCO3-}$:

$$
\mathrm{pH} = 6.1 + \lg\frac{[\ce{HCO3-}]}{0.23\,\mathrm{mM\,kPa^{-1}} \times p_{\ce{CO2}}}.
$$

**Definition 2.3.1** The system of equilibria linking gaseous $\ce{CO2}$ in the lungs, dissolved $\ce{CO2}$, carbonic acid and bicarbonate in the blood, through which the pH of blood plasma is regulated by respiration and by the kidneys, is called the **bicarbonate buffer system**.

With the normal arterial values $[\ce{HCO3-}] = 24\,\mathrm{mM}$ and $p_{\ce{CO2}} = 5.3\,\mathrm{kPa}$ ($[\ce{CO2(d)}] = 1.2\,\mathrm{mM}$), the equation gives pH 7.4 ([6.1.9](/6.1.9#sec-9.5.4)). At first sight this is a poor buffer: pH 7.4 is 1.3 units above the $\mathrm{p}K_{\mathrm{a}}'$, the base-to-acid ratio is 20, and a closed solution of this composition would have a buffer capacity of only $\beta = 2.303\,C K_{\mathrm{a}}[\ce{H+}]/(K_{\mathrm{a}} + [\ce{H+}])^2 \approx 2.6\,\mathrm{mM}$ per pH unit ($C = 25.2\,\mathrm{mM}$). The point is that the system is *open*. The acid form, $\ce{CO2(d)}$, is in near-equilibrium with a large reservoir of gaseous $\ce{CO2}$ in the lungs, and its concentration is set by $p_{\ce{CO2}}$, which the respiratory centre controls. When acid is added, $\ce{HCO3-}$ is converted to $\ce{CO2}$, which is exhaled; $[\ce{CO2(d)}]$ stays constant and only the small relative decrease of $[\ce{HCO3-}]$ changes the pH. At constant $p_{\ce{CO2}}$, $[\ce{HCO3-}] \propto 10^{\mathrm{pH}}$ and

$$
\beta_{\text{open}} = \frac{\mathrm{d}[\ce{HCO3-}]}{\mathrm{dpH}} = 2.303\,[\ce{HCO3-}] \approx 55\,\mathrm{mM\ per\ pH\ unit},
$$
twenty times the closed value, and largest precisely at the high base-to-acid ratio of plasma. Moreover, a fall in pH stimulates breathing, lowering $p_{\ce{CO2}}$ (respiratory compensation, within minutes), and the kidneys excrete $\ce{H+}$ and regenerate $\ce{HCO3-}$ (renal compensation, over hours to days).

![The open bicarbonate buffer. (A) Buffer capacity of the CO₂/HCO₃⁻ pair as a closed system (total 25.2 mM; maximal at pKa′ = 6.1 and only 2.6 mM per pH unit at pH 7.4) and as an open system in which the lungs hold p(CO₂) at 5.3 kPa (β = 2.303[HCO₃⁻], about 55 mM per pH unit at pH 7.4). (B) Plasma pH after adding a strong acid: in a closed system 10 mM acid lowers the pH to 6.2; at constant p(CO₂) only to 7.17; with respiratory compensation (p(CO₂) falling by about 0.2 kPa per mM fall of bicarbonate, Winter's relation) the pH stays near the normal range](./plots/bicarbonate-buffer.py)

### 2.3.4. Acidosis and Alkalosis

The normal pH of arterial blood is 7.35–7.45; values below about 6.8 or above about 7.8 are rapidly fatal. The Henderson–Hasselbalch form of the bicarbonate equation shows that pH depends on the *ratio* $[\ce{HCO3-}]/p_{\ce{CO2}}$, and so classifies the disorders by which term changes first.

**Definition 2.3.2** A pathological decrease of blood pH below 7.35 is called **acidosis**, an increase above 7.45 **alkalosis**. A disorder caused primarily by a change in $p_{\ce{CO2}}$ (ventilation) is *respiratory*; one caused primarily by a change in $[\ce{HCO3-}]$ (gain or loss of nonvolatile acid or base) is *metabolic*.

| Disorder | Primary change | Compensation | Typical causes |
|---|---|---|---|
| respiratory acidosis | $p_{\ce{CO2}}$ ↑ | kidneys retain $\ce{HCO3-}$ | hypoventilation: lung disease, opioid overdose |
| respiratory alkalosis | $p_{\ce{CO2}}$ ↓ | kidneys excrete $\ce{HCO3-}$ | hyperventilation: anxiety, high altitude |
| metabolic acidosis | $[\ce{HCO3-}]$ ↓ | hyperventilation lowers $p_{\ce{CO2}}$ | **ketoacidosis** in uncontrolled **diabetes** (7.1.21, 7.1.29), lactic acidosis, renal failure, diarrhoea |
| metabolic alkalosis | $[\ce{HCO3-}]$ ↑ | hypoventilation raises $p_{\ce{CO2}}$ | vomiting (loss of gastric HCl), diuretics |

**Example 2.3.1** Why does an intravenous infusion of bicarbonate raise the pH of a patient in metabolic acidosis? Bicarbonate is the base form of the buffer. Infusion raises $[\ce{HCO3-}]$ while respiration keeps $p_{\ce{CO2}}$, and thus $[\ce{CO2(d)}]$, roughly constant; the ratio in the Henderson–Hasselbalch equation increases and so does the pH. If, for example, a patient has $[\ce{HCO3-}] = 12\,\mathrm{mM}$ at $p_{\ce{CO2}} = 4.0\,\mathrm{kPa}$, then $\mathrm{pH} = 6.1 + \lg(12/0.92) = 7.22$; raising bicarbonate to $18\,\mathrm{mM}$ at the same $p_{\ce{CO2}}$ gives pH 7.39. (Clinically, bicarbonate is used cautiously, because the extra $\ce{CO2}$ it generates diffuses into cells faster than $\ce{HCO3-}$ and can transiently acidify them.)

### 2.3.5. pH and Drug Absorption

Biological membranes are permeable to uncharged molecules but not to ions (7.1.13), so the absorption of a weakly acidic or basic drug depends on the pH at the site of absorption.

**Example 2.3.2** Aspirin has a carboxyl group with $\mathrm{p}K_{\mathrm{a}} = 3.5$. In the stomach (pH 2.0), $\lg([\ce{A-}]/[\ce{HA}]) = -1.5$, so $[\ce{A-}]/[\ce{HA}] = 0.032$ and the protonated, uncharged form is $1/(1 + 0.032) = 97\,\%$ of the total. At pH 5.0, $[\ce{A-}]/[\ce{HA}] = 31.6$ and only $1/(1 + 31.6) = 3\,\%$ is uncharged; at pH 6.5, typical of the upper small intestine, 0.1 %.

![Fraction of a drug in its uncharged, membrane-permeant form as a function of pH (Henderson–Hasselbalch equation). The weak acid aspirin (pKa 3.5) is mostly uncharged in the stomach (97 % at pH 2) and mostly ionized in the small intestine and in plasma (3 % uncharged at pH 5); the weak base lidocaine (pKa 7.9) is mostly protonated at pH 7.4 and becomes uncharged only above pH 8](./plots/drug-ionization.py)

This *pH-partition* reasoning predicts that weak acids are absorbed from the stomach and weak bases from the intestine, and it explains ion trapping: aspirin that has entered the cells of the gastric mucosa (pH 7) ionizes and cannot leave, which contributes to its irritant effect. The prediction is only part of the story, however: because the small intestine has a surface area several hundred times that of the stomach and a longer residence time, most aspirin is in fact absorbed there despite the low uncharged fraction. Weak bases show the mirror image; for example, local anaesthetics such as lidocaine ($\mathrm{p}K_{\mathrm{a}} = 7.9$) act from inside the nerve cell but must cross its membrane uncharged, which is why they work poorly in inflamed, acidic tissue.

## 2.4. Water as a Reactant and as Part of Structure

Water is not only the medium of biochemical reactions but a participant in many of them. The polymers of the cell are made by **condensation reactions**, which eliminate the elements of water as monomers are joined (peptide, glycosidic and phosphodiester bonds), and broken down by hydrolysis, the reverse reaction. Hydrolysis is thermodynamically favourable for all of them, yet these bonds are kinetically stable: their uncatalysed hydrolysis at pH 7 takes years to millions of years, and cells hydrolyse them only with enzymes (proteases, glycosidases, nucleases). Their synthesis is endergonic and is driven by coupling to the hydrolysis of ATP or other nucleoside triphosphates (7.1.16). Condensation and the hydrolysis of phosphoanhydrides and thioesters are the energetic backbone of **metabolism**.

Water is also a product and a substrate of energy metabolism. The complete oxidation of fuels produces water ($\ce{C6H12O6 + 6 O2 -> 6 CO2 + 6 H2O}$); this *metabolic water* is enough for some desert animals, such as the kangaroo rat, to live without drinking, and the oxidation of 1 g of fat yields about 1.07 g of water. Conversely, photosynthesis uses water as the electron donor and releases its oxygen as $\ce{O2}$ (7.1.24).

Finally, water is part of macromolecular structure. In crystal structures of proteins and nucleic acids some water molecules are so tightly bound that they diffract X-rays as if they were fixed parts of the macromolecule; in hemoglobin dozens of them line the subunit interfaces. Such bound water molecules are not osmotically active, they mediate hydrogen bonds between groups that cannot reach each other directly, and they can form proton paths, like the chain of five water molecules in cytochrome *f* described above (2.2.1). A protein in solution is surrounded by a hydration shell whose structure and dynamics differ from those of bulk water, and the release of this water is part of every binding and folding event (2.1.3).

## Summary

| Structural feature | Chemical property | Biological consequence |
|---|---|---|
| bent, polar $\ce{H2O}$; up to 4 H bonds (3.4 in liquid) | high melting and boiling points, heat capacity, enthalpy of vaporization; ice less dense | thermal buffering, evaporative cooling; ice floats |
| high relative permittivity ($\varepsilon_{\mathrm{r}} = 78.5$) | screens charges; dissolves ions and polar molecules | charged molecules need transporters to cross membranes; buried salt bridges are strong |
| no H bonds to nonpolar solutes | ordered water shell, $\Delta S < 0$, $\Delta C_p > 0$ (Definition 2.1.1) | protein folding, membrane formation, ligand binding; $\ce{O2}$ needs carriers |
| many weak interactions (Definition 2.1.2) | each 0.4–20 kJ mol⁻¹, $K = \mathrm{e}^{-\Delta G/RT}$ | native structures maximize them; specific, reversible binding |
| solutes lower the chemical potential of water | $\Pi = RT\sum i_j c_j$ (Definition 2.1.3) | cell walls, turgor, contractile vacuoles, isotonic plasma; polysaccharide storage |
| ionizable groups | $f_{\ce{HA}} = 1/(1 + 10^{\mathrm{pH} - \mathrm{p}K_{\mathrm{a}}})$; $\mathrm{p}K_{\mathrm{a}}$ depends on the environment | pH optima of enzymes; tuned catalytic groups |
| phosphate (6.86), His (6.0), $\ce{CO2(d)}/\ce{HCO3-}$ (6.1, open) | buffering near pH 7 | cytosolic and blood pH; $\beta_{\text{open}} = 2.303[\ce{HCO3-}] \approx 55\,\mathrm{mM}$ (Definition 2.3.1) |
| pH set by $[\ce{HCO3-}]/p_{\ce{CO2}}$ | respiratory vs metabolic disturbances | acidosis and alkalosis, compensation (Definition 2.3.2) |
| only uncharged forms cross membranes | pH partition | drug absorption, ion trapping (Example 2.3.2) |

Key numbers: hydrogen bond in water $23\,\mathrm{kJ\,mol^{-1}}$ (breaking), net 4–10 between solutes; $RT = 2.6\,\mathrm{kJ\,mol^{-1}}$ at 37 °C; $5.7\,\mathrm{kJ\,mol^{-1}}$ = factor 10 in $K$; $K_{\mathrm{w}} = 10^{-14}$ (25 °C); plasma pH 7.4 = $6.1 + \lg(24/1.2)$; plasma osmolarity $0.29\,\mathrm{osmol\,L^{-1}}$.

## Questions

1. Ethanol and ethane have similar molecular masses, but ethanol is completely miscible with water and ethane is almost insoluble. Explain in terms of enthalpy and entropy.

   **Answer** Ethanol's hydroxyl group donates and accepts hydrogen bonds with water, which compensates for the hydrogen bonds between water molecules disrupted by the solute, and the ethyl group is small; mixing is favoured by the entropy of mixing. Ethane forms no hydrogen bonds with water; to keep their own hydrogen bonds, the surrounding water molecules become more ordered, so $\Delta S$ of solution is strongly negative at room temperature while $\Delta H$ is small. The resulting $\Delta G > 0$ is the hydrophobic effect.

2. Using the model of Section 2.1.3 ($\Delta C_p = 225\,\mathrm{J\,mol^{-1}\,K^{-1}}$, $T_H = 295\,\mathrm{K}$, $T_S = 386\,\mathrm{K}$), compute $\Delta H$, $T\Delta S$ and $\Delta G$ for the transfer of benzene into water at $5\,^\circ\mathrm{C}$ and at $60\,^\circ\mathrm{C}$. What does this suggest about the temperature dependence of hydrophobic interactions in proteins?

   **Answer** At $278\,\mathrm{K}$: $\Delta H = 0.225 \times (278 - 295) = -3.8\,\mathrm{kJ\,mol^{-1}}$, $\Delta S = 0.225\ln(278/386) = -0.0739\,\mathrm{kJ\,mol^{-1}\,K^{-1}}$, $T\Delta S = -20.5$, $\Delta G = +16.7\,\mathrm{kJ\,mol^{-1}}$. At $333\,\mathrm{K}$: $\Delta H = +8.6$, $\Delta S = -0.0332$, $T\Delta S = -11.1$, $\Delta G = +19.6\,\mathrm{kJ\,mol^{-1}}$. The hydrophobic penalty, and hence the strength of hydrophobic association, increases with temperature over the physiological range and changes from entropic to enthalpic. It weakens on cooling, which is one cause of the cold denaturation of proteins.

3. What is the osmotic pressure at $37\,^\circ\mathrm{C}$ of a $0.15\,\mathrm{M}$ NaCl solution ("physiological saline")? Is it isotonic with plasma? What happens to red blood cells placed in $0.15\,\mathrm{M}$ glucose?

   **Answer** Osmolarity $= 2 \times 0.15 = 0.30\,\mathrm{osmol\,L^{-1}}$ (slightly less in reality, since NaCl is not ideally dissociated: osmotic coefficient 0.93, about $0.28\,\mathrm{osmol\,L^{-1}}$), so $\Pi \approx (280\,\mathrm{mol\,m^{-3}})(8.314)(310)\,\mathrm{Pa} \approx 0.72\,\mathrm{MPa}$, about isotonic with plasma ($0.29\,\mathrm{osmol\,L^{-1}}$). A $0.15\,\mathrm{M}$ glucose solution has only $0.15\,\mathrm{osmol\,L^{-1}}$, so it is hypotonic: water enters the cells, which swell and lyse (moreover glucose slowly enters red cells through GLUT1, making the effective tonicity even lower).

4. A patient's arterial blood has $p_{\ce{CO2}} = 8.0\,\mathrm{kPa}$ and $[\ce{HCO3-}] = 26\,\mathrm{mM}$. Calculate the pH and identify the disorder. What compensation is expected?

   **Answer** $[\ce{CO2(d)}] = 0.23 \times 8.0 = 1.84\,\mathrm{mM}$; $\mathrm{pH} = 6.1 + \lg(26/1.84) = 6.1 + 1.15 = 7.25$. The pH is low and $p_{\ce{CO2}}$ high: respiratory acidosis (hypoventilation). The bicarbonate is only slightly raised, as expected from the buffering reaction in the acute phase; over days the kidneys excrete more $\ce{H+}$ and retain $\ce{HCO3-}$, raising $[\ce{HCO3-}]$ and bringing the pH back towards 7.4.

5. A weakly basic drug with $\mathrm{p}K_{\mathrm{a}} = 8.4$ is given orally. Compute the fraction uncharged at pH 2.0 and pH 6.5. Where will it mainly be absorbed? After absorption, what happens to the drug that diffuses into the acidic lumen of the stomach?

   **Answer** For a base, the uncharged fraction is $1/(1 + 10^{\mathrm{p}K_{\mathrm{a}} - \mathrm{pH}})$: at pH 2.0, $1/(1 + 10^{6.4}) = 4 \times 10^{-7}$; at pH 6.5, $1/(1 + 10^{1.9}) = 1.2\,\%$. It is absorbed almost entirely in the intestine. Drug that diffuses from plasma (pH 7.4, 9 % uncharged) into the stomach is protonated there and trapped (ion trapping), which is why basic drugs accumulate in gastric juice.
