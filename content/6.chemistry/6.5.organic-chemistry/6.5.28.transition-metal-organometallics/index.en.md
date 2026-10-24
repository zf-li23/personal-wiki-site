---
title: Transition-Metal Organometallic Compounds and Elementary Reactions
description: Definition and history of organometallic compounds; ligand notation (η, μ, κ), the L/X classification, oxidation states and dⁿ, the 18-electron rule and its exceptions; σ donation and π back-donation in CO, Tolman parameters of phosphine ligands, the Dewar–Chatt–Duncanson model of alkenes; the six classes of elementary reactions (ligand substitution and the trans effect, oxidative addition, reductive elimination, migratory insertion, β-hydride elimination, transmetalation, and attack on ligands); σ-alkyl, allyl, metallocene, arene, carbene and hydride complexes.
source_hash: 151fdf31162e
---

Main-group organometallic compounds (**organolithium reagents**, **Grignard reagents**, **Gilman reagents**, [6.5.10](/6.5.10), [6.5.27](/6.5.27)) are essentially sources of **carbanions**: the C–M bond is strongly polarized, carbon attacks the substrate as a **nucleophile** or base, and the metal is merely the counterion. Transition metals are different. Their d orbitals can both accept electrons from ligands and donate electrons back into empty ligand orbitals, so transition metals bind firmly to CO, alkenes, arenes and $\ce{H2}$, which have no lone pairs or only weak electron donation, and change their reactivity within the coordination sphere: H–H, C–X and even C–H bonds can add to the metal and be broken, and two ligands can couple on the metal to form new C–C, C–H and C–N bonds and leave. This chapter first presents the language that describes these compounds, namely ligands, electron counting and the 18-electron rule, and then the nature of the metal–ligand bond; it then treats the six classes of elementary reactions that make up every catalytic cycle and finally gives a brief introduction to several common types of complexes. The next chapter, [6.5.29](/6.5.29), assembles these elementary reactions into catalytic reactions such as hydrogenation, **cross-coupling** and **olefin metathesis**. The fundamentals of coordination chemistry (composition and nomenclature of complexes, **crystal field theory**) are in [6.1.5](/6.1.5), and the general properties of the d-block elements in [6.1.15](/6.1.15); they are not repeated here.

## 28.1. Organometallic Compounds

### 28.1.1. Definition and Classification

**Definition 28.1.1 (Organometallic Compound)** A compound containing a metal–carbon bond (M–C) is called an **organometallic compound**. By convention, hydrides of transition metals and compounds in which metalloids such as boron, silicon and arsenic are bonded directly to carbon are also counted as organometallic compounds; metal alkoxides (ROM), thiolates (RSM) and carboxylates contain no M–C bond and are not organometallic compounds; $\ce{CaC2}$, $\ce{NaCN}$ and the like, although containing M–C bonds, are usually treated as inorganic compounds; metal carbonyls are customarily classed as organometallic compounds.

According to the nature of the M–C bond they can be divided into four classes, the nature of the bond varying continuously with the **electronegativity** of the metal ([6.5.10](/6.5.10#sec-10.3.1)):

| Type | Metals | M–C bond | Examples |
|---|---|---|---|
| Ionic | Na, K, Cs | approximately ionic $\ce{M+ R-}$ | $\ce{PhCH2K}$ |
| Polar covalent | Li, Mg, Al, Zn | strongly polarized σ bond, often forming aggregates or electron-deficient multicenter bonds | $\ce{(MeLi)4}$, $\ce{Al2Me6}$ |
| Covalent | B, Si, Sn, Hg, Pb | weakly polarized σ bond | $\ce{SiMe4}$, $\ce{SnBu4}$ |
| Transition-metal | d-block metals | σ bond plus π back-donation, able to form π complexes with unsaturated ligands | $\ce{Fe(CO)5}$, ferrocene |

The organometallic compounds of the **lanthanoids** and **actinoids** form a fifth class: $\ce{Ln^3+}$ is a hard acid, the Ln–C bond is predominantly ionic, no stable complexes are formed with soft bases such as CO, phosphines and alkenes (the **HSAB principle**), the coordination numbers are high, the 18-electron rule is not obeyed, and the compounds are extremely sensitive to air and water; among the actinoids thorium and uranium have been studied most, as in the sandwich compound $\ce{U(C8H8)2}$ (uranocene). This chapter treats only d-block metals.

Most organometallic compounds are sensitive to oxygen and water, and their synthesis and handling must be carried out under an inert atmosphere: with a double manifold (one line for vacuum, one for nitrogen or argon) and Schlenk flasks, or in a glove box. This air-free technique goes back to Frankland's synthesis of diethylzinc (1849) and Schlenk's preparation of organolithium compounds (1917).

### 28.1.2. A Brief History

| Year | Event |
|---|---|
| 1827 | Zeise prepares $\ce{K[PtCl3(C2H4)]*H2O}$ (Zeise's salt), the first transition-metal organometallic compound, with π coordination at M–C |
| 1849 | Frankland synthesizes $\ce{ZnEt2}$, the first organometallic compound with a σ bond |
| 1890 | Mond synthesizes $\ce{Ni(CO)4}$, used to purify nickel (the Mond process) |
| 1900 | Grignard discovers RMgX (shared the Nobel Prize with Sabatier in 1912) |
| 1951 | Kealy and Pauson, and Miller and coworkers, independently obtain ferrocene; in 1952 Wilkinson, Woodward and Fischer propose the sandwich structure (Nobel Prize to Wilkinson and Fischer, 1973) |
| 1953–1955 | Ziegler and Natta: coordination polymerization of alkenes (Nobel Prize 1963, [6.5.11](/6.5.11#sec-11.11)) |
| 1956 | Hodgkin determines the crystal structure of vitamin B₁₂, the first natural organometallic compound (Co–C bond, Section 28.5.6) |
| 1961 | Vaska reports $\ce{IrCl(CO)(PPh3)2}$, which adds $\ce{O2}$ and $\ce{H2}$ reversibly |
| 1964 | Fischer synthesizes the first metal carbene complex; Banks and Bailey discover **olefin metathesis** |
| 1965 | Wilkinson and Coffey independently find that $\ce{RhCl(PPh3)3}$ catalyzes alkene hydrogenation in **homogeneous catalysis** |
| 1971 | Chauvin proposes the metal carbene mechanism of olefin metathesis |
| 2001 | Knowles, Noyori, Sharpless: hydrogenation and oxidation by **asymmetric catalysis** |
| 2005 | Chauvin, Grubbs, Schrock: olefin metathesis |
| 2010 | Heck, Negishi, Suzuki: palladium-catalyzed **cross-coupling** |

## 28.2. Ligands, Oxidation States and Electron Counting

### 28.2.1. Ligand Notation

A ligand may bind to the metal through more than one atom, or to several metals at once, and three Greek letters are used in names and structural formulas to describe this.

**Definition 28.2.1 (Hapticity)** The number of contiguous carbon atoms (or other atoms) of a ligand directly bonded to the metal is called the **hapticity**, written $\eta^n$ (read hapto-$n$).

For example, in $\ce{Fe(C5H5)2}$ all five carbons of each ring are bonded to iron, written $\ce{Fe}(\eta^5\text{-}\ce{C5H5})_2$; in Zeise's salt ethylene is an $\eta^2$ ligand; an allyl group can be $\eta^1$ (σ bonded through one carbon only) or $\eta^3$ (bonded through all three carbons). When the bonded atoms are not contiguous, their positions are given, as in $(1\text{–}2{:}5\text{–}6\text{-}\eta)$-cycloocta-1,5-diene (cod). Two further symbols:

- $\mu$ denotes a bridging ligand, and $\mu_n$ a ligand bridging $n$ metals, such as the two bridging carbonyls in $\ce{Co2(CO)6}(\mu\text{-}\ce{CO})_2$;
- $\kappa$ denotes through which heteroatoms a **polydentate ligand** is coordinated (hapticity $\eta$ is used for contiguous carbon atoms, $\kappa$ for noncontiguous **donor atoms**); for example $\kappa^2P,P'$ means that both P atoms of a bisphosphine ligand are coordinated.

**Ligands** are divided into two classes by Green's method, which is the basis of electron counting and of determining the **oxidation state**:

**Definition 28.2.2** A ligand that is a neutral molecule and coordinates to the metal with an electron pair is called an **L-type ligand**, such as CO, $\ce{PR3}$, $\ce{NR3}$, $\ce{H2O}$, $\ce{H2}$ and alkenes; a ligand that, counted as a neutral atom, supplies one electron and forms an ordinary covalent bond to the metal is called an **X-type ligand**, such as H, alkyl, aryl, acyl and halogens (counted as ions, they are anions carrying one negative charge and supplying two electrons).

More complex ligands can be written as combinations of L and X: $\eta^3$-allyl is LX, $\eta^4$-butadiene is $\ce{L2}$, $\eta^5$-cyclopentadienyl (Cp) is $\ce{L2X}$, and $\eta^6$-benzene is $\ce{L3}$. Below, to avoid confusion, the halogens are written with element symbols such as Cl and Br, and X is used only to denote a ligand type or a halogen generically.

### 28.2.2. Two Methods of Electron Counting

There are two conventions for counting the valence electrons of a metal, which give the same result and differ only in whether ligands are regarded as neutral groups or as anions.

1. The covalent (neutral-ligand) method: each ligand is treated as a neutral atom or molecule and the metal as zero-valent, so the number of valence electrons equals the group number (Fe 8, Rh 9, Pd 10); an X-type ligand supplies 1 electron and an L-type ligand 2.
2. The ionic method: X-type ligands are first regarded as anions ($\ce{H-}$, $\ce{R-}$, $\ce{Cl-}$, $\ce{Cp-}$), the oxidation state and $\mathrm{d}^n$ of the metal are determined, and each anionic ligand supplies 2 electrons.

| Ligand | Type | Covalent count | Ionic count (ligand charge) |
|---|---|---|---|
| H, R, Ar, RCO, Cl (terminal) | X | 1 | 2 (−1) |
| CO, $\ce{PR3}$, $\ce{NR3}$, RCN, RNC, $\eta^2$-alkene, $\eta^2$-$\ce{H2}$ | L | 2 | 2 (0) |
| $\eta^3$-Allyl | LX | 3 | 4 (−1) |
| Linear NO | none | 3 | 2 ($\ce{NO+}$) |
| $\eta^4$-Butadiene, $\eta^4$-cyclobutadiene | $\ce{L2}$ | 4 | 4 (0) |
| $\eta^5$-$\ce{C5H5}$ (Cp), $\eta^5$-$\ce{C5Me5}$ (Cp*) | $\ce{L2X}$ | 5 | 6 (−1) |
| $\eta^6$-Benzene | $\ce{L3}$ | 6 | 6 (0) |
| $\eta^7$-Cycloheptatrienyl cation | none | 7 | 6 (+1) |
| $\eta^8$-Cyclooctatetraene | $\ce{L4}$ | 8 | 10 (−2, as $\ce{C8H8^2-}$) |
| Bridging $\mu$-Cl, $\mu$-SR | LX | 3 (shared between two metals: 1 + 2) | 4 (−1) |
| Bridging $\mu$-CO | none | 2 (1 for each metal) | 2 |
| Metal–metal single bond | none | 1 for each metal | 1 for each metal |

These assignments are somewhat artificial: the same $\eta^5$-Cp is a 5-electron ligand in the covalent count and a 6-electron ligand carrying one negative charge in the ionic count, and the two methods must not be mixed.

### 28.2.3. Oxidation State, dⁿ and Coordination Number

The formal oxidation state of the metal in an organometallic compound is the charge the metal carries when all X-type ligands are regarded as anions and L-type ligands as neutral molecules: oxidation state = charge of the complex − (sum of the charges of the ligands). The number of d electrons of the metal is

$$
n(\mathrm{d}) = \text{group number} - \text{oxidation state}.
$$

In complexes the valence electrons of the metal are always counted as d electrons: zero-valent Fe is written $\mathrm{d}^8$, not the $3\mathrm{d}^6 4\mathrm{s}^2$ of the free atom, because after bonding to ligands the $3\mathrm{d}$ orbitals are more stable than the $4\mathrm{s}$ orbital ([6.1.2](/6.1.2)). $\mathrm{d}^n$ is more useful than the oxidation state itself: it determines the geometry and magnetism of the complex ($\mathrm{d}^8$ Rh(I), Pd(II) and Pt(II) are mostly square planar, $\mathrm{d}^6$ mostly octahedral, $\mathrm{d}^{10}$ mostly tetrahedral or linear), and also whether the metal can still be oxidized (a $\mathrm{d}^0$ metal cannot undergo oxidative addition).

Three points should be kept in mind when using oxidation states.

1. The formal oxidation state is not the true charge: Fe in ferrocene is +2, but ferrocene contains no $\ce{Fe^2+}$ ion, and the Fe–Cp bond has considerable covalent character.
2. The formal oxidation state does not predict chemical properties: in $\ce{HCo(CO)4}$ by convention H is −1 and Co +1, yet this hydride is a strong acid in water and H leaves as $\ce{H+}$, because back-donation to the four CO ligands makes the **conjugate base** $\ce{[Co(CO)4]-}$ very stable.
3. Some ligands themselves can be oxidized or reduced (non-innocent ligands), so that the oxidation state is ambiguous: a butadiene complex can be written as M(0) coordinated by an $\ce{L2}$ ligand or as an M(II) metallacyclopentene ($\ce{LX2}$, Section 28.3.4); both resonance forms contribute to the true structure.

The **coordination number** of the metal in a complex equals the number of σ bonds to the metal, that is, the sum of the coordination sites occupied by the ligands: an $\eta^2$-alkene occupies 1, an $\eta^3$-allyl 2, and $\eta^5$-Cp and $\eta^6$-benzene 3 each. A d-block metal has only 9 valence orbitals and the coordination number generally does not exceed 9; the size of the ligands often makes it smaller.

### 28.2.4. The 18-Electron Rule

Stable compounds of the **main-group elements** obey the **octet rule**: the four valence orbitals, s and p, can hold at most 8 electrons, and electron-deficient $\ce{AlMe3}$ and $\ce{BH3}$ make up the octet by dimerization (**three-center two-electron bonds**) or by binding to **Lewis bases**. A d-block metal has 9 valence orbitals (five $(n-1)\mathrm{d}$, one $n\mathrm{s}$, three $n\mathrm{p}$), and the corresponding rule is:

**Definition 28.2.3 (18-Electron Rule)** In thermodynamically stable transition-metal organometallic compounds, the sum of the valence electrons of the metal (covalent count) and the electrons supplied by the ligands is usually 18, that is, the metal reaches the electron configuration of the next noble gas. A complex with a total of 18 valence electrons is called **coordinatively saturated**, and one with fewer than 18 is said to show **coordinative unsaturation**.

The origin of the number 18 can be seen from the **molecular orbital theory** of octahedral **coordination compounds**: the σ orbitals of the six ligands combine with the $\mathrm{s}$, $\mathrm{p}$ and $\mathrm{d}_{z^2}$, $\mathrm{d}_{x^2-y^2}$ ($e_g$) orbitals of the metal into six **bonding orbitals**; the $t_{2g}$ orbitals of the metal do not interact with the ligand σ orbitals and are nonbonding, and with π-acceptor ligands (CO) they become π bonding orbitals; the 6 + 3 = 9 low-energy orbitals are filled by exactly 18 electrons, and further electrons can only enter the antibonding $e_g^*$ orbitals. This is the $t_{2g}$–$e_g$ splitting of **crystal field theory** ([6.1.5](/6.1.5#sec-5.5.2)) as it appears in the covalent picture. The stronger the π acceptors and the more the $t_{2g}$ orbitals are stabilized by back-donation, the more reliable the 18-electron rule, so it is most accurate for carbonyl, phosphine and Cp complexes and often fails for classical complexes such as $\ce{[Co(NH3)6]^3+}$.

| Complex | Covalent count | Ionic count | Total |
|---|---|---|---|
| $\ce{Fe(CO)5}$ | Fe 8 + 5 × 2 | Fe(0) $\mathrm{d}^8$ + 10 | 18 |
| $\ce{Ni(CO)4}$ | Ni 10 + 4 × 2 | Ni(0) $\mathrm{d}^{10}$ + 8 | 18 |
| $\ce{Cr}(\eta^6\text{-}\ce{C6H6})_2$ | Cr 6 + 2 × 6 | Cr(0) $\mathrm{d}^6$ + 12 | 18 |
| Ferrocene $\ce{Cp2Fe}$ | Fe 8 + 2 × 5 | Fe(II) $\mathrm{d}^6$ + 2 × 6 | 18 |
| $\ce{Mn2(CO)10}$ (per Mn) | Mn 7 + 5 × 2 + 1 (Mn–Mn) | Mn(0) $\mathrm{d}^7$ + 10 + 1 | 18 |
| $\ce{Co2(CO)6}(\mu\text{-}\ce{CO})_2$ (per Co) | Co 9 + 3 × 2 + 2 × 1 + 1 (Co–Co) | Co(0) | 18 |
| $\ce{RhCl(PPh3)3}$ | Rh 9 + 1 + 3 × 2 | Rh(I) $\mathrm{d}^8$ + 2 + 6 | 16 |
| $\ce{Ni}(\eta^3\text{-}\ce{C3H5})_2$ | Ni 10 + 2 × 3 | Ni(II) $\mathrm{d}^8$ + 2 × 4 | 16 |
| $\ce{Cp2ZrCl2}$ | Zr 4 + 2 × 5 + 2 × 1 | Zr(IV) $\mathrm{d}^0$ + 12 + 4 | 16 |
| Cobaltocene $\ce{Cp2Co}$ | Co 9 + 2 × 5 | Co(II) $\mathrm{d}^7$ + 12 | 19 |

The role of metal–metal bonds is precisely to make up the electrons: $\ce{Mn(CO)5}$ and $\ce{CpW(CO)3}$ are each 17-electron species on their own, and on dimerization to form M–M bonds each reaches 18 electrons.

The exceptions to the 18-electron rule follow patterns:

- Complexes with more than 18 electrons are rare and lose electrons easily: 19-electron cobaltocene is a strong reducing agent and loses one electron from an **antibonding orbital** to become the 18-electron cobaltocenium cation $\ce{[Cp2Co]+}$.
- $\mathrm{d}^8$ metals of Groups 8–10 (and Au(III) of Group 11) often form 16-electron square-planar complexes, such as Rh(I), Ir(I), Ni(II), Pd(II) and Pt(II): in the square-planar field the $\mathrm{d}_{x^2-y^2}$ orbital is very high in energy, the ninth orbital ($p_z$) is far above it, and the 17th and 18th electrons have no suitable orbitals. Fe(0) and Ru(0) of Group 8 still tend to have 18 electrons.
- Early transition metals (Groups 3–5) have few valence electrons, and ligands are limited by steric hindrance, so they often stay at 16 electrons or fewer, as in $\ce{Cp2ZrCl2}$ (16), $\ce{TiCl4}$ (8) and $\ce{WMe6}$ (12).
- The active species in catalytic cycles are often coordinatively unsaturated 14- or 16-electron species (Section 6.5.29), and it is their "dissatisfaction" with 18 electrons that allows them to bind substrates.

## 28.3. Metal–Ligand Bonding

### 28.3.1. σ Donation and Multicenter Bonds

The simplest metal–ligand bond is the σ **coordinate bond** formed when an electron pair of the ligand enters an empty metal orbital (L-type), or the covalent σ bond formed when the metal and an X-type ligand each contribute one electron: alkyl, aryl, hydride and halide complexes all belong to this class. For some σ bonds the electron donor is itself a σ bond: $\ce{H2}$ coordinates to the metal through the bonding electron pair of the H–H bond, forming dihydrogen complexes (Section 28.5.5); a C–H bond can likewise bind to an electron-deficient metal (the agostic interaction, Section 28.5.5). These are all **three-center two-electron bonds**, of the same kind as the B–H–B bridge in $\ce{B2H6}$.

### 28.3.2. Carbon Monoxide: σ Donation and π Back-Donation

CO has almost no Brønsted basicity and hardly binds to main-group **Lewis acids** such as $\ce{BF3}$, yet it forms very stable **metal carbonyls** with zero-valent and even negatively charged transition metals. The reason is that there are two electron flows between it and the metal, in opposite directions (**π back-bonding**, [6.1.5](/6.1.5#sec-5.1.4)):

1. σ donation (C → M): the **highest occupied molecular orbital** of CO, 5σ, is located mainly on carbon and is the lone pair at the carbon end; it enters an empty metal $\mathrm{d}_\sigma$ orbital (in the $e_g$ direction in an octahedron) to form a σ bond.
2. π back-donation (M → C): the filled $\mathrm{d}_\pi$ orbitals of the metal ($t_{2g}$ direction) have the right symmetry to match the **lowest unoccupied molecular orbital** of CO, 2π*, and donate electrons back into the π* **antibonding orbital** of CO.

![Bonding of CO to a transition metal. Left: the 5σ lone pair at the carbon end enters an empty metal d orbital (σ donation); right: a filled metal dπ orbital overlaps the π* orbital of CO (π back-donation). Gray indicates orbitals containing electrons; + and − denote phase](./plots/co-bonding.py)

The two interactions reinforce each other: σ donation makes the metal electron-rich and strengthens its back-donation, and back-donation removes excess charge from the metal and strengthens σ donation (synergic bonding). The result is a higher M–C bond order (a shorter M–C bond) and a lower C–O bond order. The wavenumber of the C–O **stretching vibration** is a direct measure of the strength of back-donation (**infrared spectroscopy**, [6.4.11](/6.4.11)):

| | CO | $\ce{Ni(CO)4}$ | $\ce{[Co(CO)4]-}$ | $\ce{[Fe(CO)4]^2-}$ |
|---|---|---|---|---|
| $\tilde\nu(\mathrm{CO})/\mathrm{cm^{-1}}$ | 2143 | 2057 | 1886 | 1786 |

The three complexes are isoelectronic; the more negative charge the metal carries, the stronger the back-donation and the lower $\tilde\nu(\mathrm{CO})$. Bridging carbonyls have still lower $\tilde\nu(\mathrm{CO})$ (about $1700$–$1860\,\mathrm{cm^{-1}}$), and infrared spectra can distinguish terminal from bridging CO.

Coordination changes the polarity of CO: σ donation removes electrons from carbon, and π back-donation puts electrons into the π* orbital, which is mainly on carbon and also distributed on oxygen; the net result is a partial positive charge on carbon and a partial negative charge on oxygen. The carbon of coordinated CO is therefore electrophilic and can be attacked by $\ce{R-}$ and $\ce{H-}$ (Section 28.4.7), and the oxygen can bind to Lewis acids.

### 28.3.3. Phosphine Ligands: Electronic and Steric Effects

Tertiary phosphines $\ce{PR3}$ are the most commonly used ligands in **homogeneous catalysis**. Like $\ce{NH3}$ they are σ donors through the lone pair, and they are also π acceptors: what accepts back-donation from the metal is not a d orbital (the 3d orbitals of phosphorus are too high in energy, [6.5.26](/6.5.26#sec-26.3.2)) but the σ* orbitals of the P–R bonds. The higher the electronegativity of R, the lower the σ* orbital and the stronger the π acidity:

$$
\ce{PMe3} \approx \ce{P(NR2)3} < \ce{PAr3} < \ce{P(OMe)3} < \ce{P(OAr)3} < \ce{PCl3} < \ce{CO} \approx \ce{PF3}
$$

The value of phosphines lies in the fact that electronic and steric effects can be tuned separately, and Tolman (1977) quantified them as two parameters.

**Definition 28.3.1** The wavenumber of the $A_1$-symmetric C–O stretching vibration of the complex $\ce{Ni(CO)3L}$ is called the **Tolman electronic parameter** (TEP) of the ligand L: the stronger the electron-donating ability of L, the stronger the back-donation from the metal and the lower $\tilde\nu(\mathrm{CO})$. The apex angle of the cone with the metal at its vertex that is tangent to the van der Waals surfaces of the outermost atoms of the ligand is called the **Tolman cone angle** $\theta$ of L (calculated for an M–P distance of $2.28\,\text{Å}$) and measures the size of the ligand.

![Tolman map of common phosphine and phosphite ligands: the abscissa is the cone angle and the ordinate the Tolman electronic parameter (electron-donating ability increases downward). Data from Tolman, Chem. Rev. 1977](./plots/tolman-map.py)

The two parameters can be varied separately: replacing $\ce{PBu3}$ by $\ce{P(O^{i}Pr)3}$ (similar cone angles, about $130^\circ$) changes the electronic properties greatly; replacing $\ce{PMe3}$ by $\ce{P}(o\text{-tolyl})_3$ (similar electronic parameters) raises the cone angle from $118^\circ$ to $194^\circ$. The general rules are:

- Strongly electron-donating ligands make the metal electron-rich and favor high oxidation states, and so promote oxidative addition (Section 28.4.2);
- Bulky ligands make the metal prefer low coordination numbers, dissociate easily and leave vacant sites for substrates, and also promote reductive elimination (Section 28.4.3).

The $\ce{P(t-Bu)3}$, Buchwald's dialkylbiaryl phosphines (SPhos, XPhos) and N-heterocyclic carbenes (NHCs) commonly used in modern **cross-coupling** are all both "bulky" and "electron-rich" (Section 6.5.29). For ligands that are not cone-shaped, such as NHCs, the "buried volume" (%$V_{\mathrm{bur}}$, the fraction of the volume of a sphere of given radius around the metal that is occupied by the ligand) is now mostly used in place of the cone angle.

### 28.3.4. Alkenes and Alkynes: The Dewar–Chatt–Duncanson Model

Alkenes have no lone pair, but their π electrons and π* orbitals can interact with a metal just as the 5σ and 2π* orbitals of CO do.

**Definition 28.3.2 (Dewar–Chatt–Duncanson Model)** The bonding of an alkene to a transition metal has two parts: the π bonding orbital of the alkene donates electrons to an empty metal $\mathrm{d}_\sigma$ orbital (σ donation), and a filled metal $\mathrm{d}_\pi$ orbital donates electrons back into the π* orbital of the alkene (π back-donation). This description is called the **Dewar–Chatt–Duncanson model** (DCD model).

Both interactions weaken the C=C bond (σ donation removes bonding electrons, π back-donation fills the **antibonding orbital**); the stronger the back-donation, the longer the C=C bond, the more the substituents bend away from the metal, and the closer the carbons come to $\mathrm{sp}^3$. The two limits are:

| | Dominated by σ donation | Dominated by π back-donation |
|---|---|---|
| Description | the alkene is an L-type ligand, the oxidation state of the metal is unchanged | metallacyclopropane, the alkene is an $\ce{X2}$-type ligand, the metal oxidation state is +2 |
| Example | Zeise's salt, $d(\ce{C=C}) = 1.37\,\text{Å}$ | $\ce{Pt(PPh3)2(C2H4)}$, $d(\ce{C=C}) = 1.43\,\text{Å}$; tetracyanoethylene complexes approach $1.5\,\text{Å}$ |
| Favorable conditions | electron-poor metal (high oxidation state, cationic) | electron-rich metal (low oxidation state, strongly electron-donating ligands), alkene with electron-withdrawing groups |

(For free ethylene $d(\ce{C=C}) = 1.34\,\text{Å}$, and the C–C bond of ethane is $1.54\,\text{Å}$.)

When σ donation dominates, the carbons of the coordinated alkene carry a partial positive charge and can be attacked by **nucleophiles**, whereas free alkenes react only with **electrophiles** ([6.5.11](/6.5.11#sec-11.3)). This is an **umpolung** caused by the metal, and it is the basis of the **Wacker oxidation** ([6.5.29](/6.5.29#sec-29.3.3)) and the **Tsuji–Trost reaction** (Section 28.4.7).

Conjugated dienes coordinated in an $\eta^4$ fashion likewise have two descriptions: the $\ce{L2}$ type (two independent C=C bonds coordinated) and the $\ce{LX2}$ type (a $\sigma^2,\pi$-metallacyclopentene). $\ce{Fe}(\eta^4\text{-butadiene})(\ce{CO})_3$ lies between the two, with the three C–C bond lengths almost equal (about $1.46\,\text{Å}$): $\psi_2$ of butadiene (HOMO, C1–C2 bonding, C2–C3 antibonding) donates electrons and $\psi_3$ (LUMO, C1–C2 antibonding, C2–C3 bonding) accepts back-donation, and both lengthen C1–C2 and shorten C2–C3 ([6.5.12](/6.5.12#sec-12.2.3)). Cyclobutadiene, antiaromatic when free and existing only in low-temperature matrices, can be stored stably in $\ce{Fe}(\eta^4\text{-}\ce{C4H4})(\ce{CO})_3$ ([6.5.13](/6.5.13#sec-13.5.2)).

Alkynes have two mutually perpendicular sets of π orbitals and can act as 2-electron ligands (one set of π orbitals coordinated) or as 4-electron ligands (both sets donating), and can also bridge two metals at once, as in $\ce{Co2(CO)6}(\mu\text{-}\eta^2{:}\eta^2\text{-}\ce{PhC#CPh})$. On coordination $\tilde\nu(\ce{C#C})$ drops from about $2200\,\mathrm{cm^{-1}}$ to $1700$–$2000\,\mathrm{cm^{-1}}$, and with strong back-donation the complex can be regarded as a metallacyclopropene. Cyclohexyne and **benzyne** ([6.5.15](/6.5.15#sec-15.1.2)), extremely unstable in the free state, can also be stabilized by coordination to a metal: the alkyne carbons change from sp to nearly sp², and the strain is partly relieved.

## 28.4. Elementary Reactions

The mechanisms of **homogeneous catalysis** can all be broken down into a few classes of elementary reactions: an organic molecule "enters" the metal by coordination, oxidative addition, insertion or transmetalation, changes its connectivity within the coordination sphere, and then "leaves" the metal by reductive elimination, β-hydride elimination or dissociation. The table below gives the change in the valence electron count, oxidation state and coordination number of the metal in each class of reaction, which are discussed in the following sections:

| Elementary reaction | Δ valence electrons | Δ oxidation state | Δ coordination number | Reverse reaction |
|---|---|---|---|---|
| Association of L (Section 28.4.1) | +2 | 0 | +1 | dissociation |
| Oxidative addition (Section 28.4.2) | +2 | +2 | +2 | reductive elimination (Section 28.4.3) |
| 1,1- or 1,2-Migratory insertion (Section 28.4.4) | −2 | 0 | −1 | deinsertion (α- or β-elimination, Section 28.4.5) |
| Transmetalation (Section 28.4.6) | 0 | 0 | 0 | none |
| Nucleophilic or electrophilic attack on a ligand (Section 28.4.7) | varies | varies | varies | none |

### 28.4.1. Ligand Dissociation and Association

Ligand dissociation and association are the simplest elementary reactions, and almost every catalytic cycle begins with them: an 18-electron precursor (such as $\ce{Pd(PPh3)4}$, or the 16-electron $\ce{RhCl(PPh3)3}$) first loses a ligand to give a coordinatively unsaturated species that can bind the substrate. Ligand substitution (L replaced by L′) has two limiting mechanisms, much like the **SN1 reaction** and **SN2 reaction** at saturated carbon ([6.5.8](/6.5.8#sec-8.2)).

- The dissociative mechanism (D): dissociation first, then association; the **rate-determining step** is the unimolecular cleavage of the M–L bond, and the coordination number of the intermediate is lower by 1. 18-electron complexes ($\mathrm{d}^{10}$ tetrahedral, $\mathrm{d}^6$ octahedral) substitute in this way, because the intermediate is a 16-electron species whereas association would pass through an unstable 20-electron species. The rate is independent of the concentration of L′, and the **enthalpy of activation** is close to the M–L bond energy.
- The associative mechanism (A): association first, then dissociation; the rate-determining step is the bimolecular attack of L′ on the metal, and the coordination number of the intermediate is higher by 1. 16-electron square-planar $\mathrm{d}^8$ complexes (Pt(II), Pd(II), Ni(II), Rh(I)) substitute in this way: L′ approaches the empty $p_z$ orbital from above the plane, passes through an 18-electron five-coordinate (square-pyramidal or trigonal-bipyramidal) intermediate, and then expels the original ligand.

![Two mechanisms of ligand substitution. Top: the 18-electron Ni(CO)₄ first dissociates a CO to give the 16-electron Ni(CO)₃, which then binds L; bottom: a 16-electron square-planar Pt(II) complex is attacked by Y⁻ from above the plane and, through an 18-electron five-coordinate intermediate, the leaving group Cl⁻ departs with retention of configuration](./plots/ligand-substitution.py)

The larger the ligand, the faster the dissociation. Tolman measured the dissociation constants of $\ce{NiL4 <=> NiL3 + L}$ in benzene ($25\,^\circ\mathrm{C}$):

| L | Cone angle $\theta$ | $K_{\mathrm{d}}/(\mathrm{mol\,L^{-1}})$ |
|---|---|---|
| $\ce{P(OEt)3}$ | $109^\circ$ | $< 10^{-10}$ |
| $\ce{P(O-}p\ce{-tolyl)3}$ | $128^\circ$ | $6 \times 10^{-10}$ |
| $\ce{P(O^{i}Pr)3}$ | $130^\circ$ | $2.7 \times 10^{-5}$ |
| $\ce{P(O-}o\ce{-tolyl)3}$ | $141^\circ$ | $4 \times 10^{-2}$ |
| $\ce{PPh3}$ | $145^\circ$ | almost completely dissociated to $\ce{NiL3}$ in solution |

For phosphites with almost the same electronic effects, a difference of only $30^\circ$ in cone angle changes the dissociation constant by more than eight orders of magnitude.

The rate of associative substitution is affected by four factors: the metal (in a group, Ni(II) > Pd(II) ≫ Pt(II); substitution at Pt(II) is about $10^5$ times slower, so substitution reactions of Pt(II) complexes can be studied at leisure); the entering ligand (Pt(II) is a soft acid and soft **nucleophiles** attack quickly, the **HSAB principle**); the leaving ligand (ligands that accept back-donation and bind strongly to the metal are hard to displace); and steric hindrance (association is slow when the metal is crowded, and a very hindered complex may react by the dissociative mechanism instead). The most characteristic is the influence of the ligand trans to the leaving group:

**Definition 28.4.1 (Trans Effect)** In a square-planar complex, the effect of one ligand on the rate of substitution of the ligand trans to it is called the **trans effect**.

For Pt(II) the trans effect increases roughly in the following order:

$$
\ce{H2O}, \ce{OH-}, \ce{NH3}, \text{py} < \ce{Cl-} < \ce{Br-} < \ce{I-}, \ce{SCN-}, \ce{NO2-} < \ce{C6H5-} < \ce{CH3-} < \ce{H-}, \ce{PR3} < \ce{C2H4}, \ce{CN-}, \ce{CO}
$$

Ligands with a strong trans effect are of two kinds. Strong σ donors ($\ce{H-}$, $\ce{CH3-}$, $\ce{PR3}$) form strong σ bonds to the metal and weaken the trans M–X bond that shares the same metal orbital: this is a ground-state thermodynamic effect, called the trans influence, and can be seen in the trans bond lengths. Strong π acceptors (CO, $\ce{C2H4}$, $\ce{CN-}$) lower the activation energy by delocalizing, through back-donation, the extra electron density in the five-coordinate transition state: this is a purely kinetic effect.

The trans effect is a tool for the directed synthesis of square-planar isomers. The anticancer drug cisplatin, cis-$\ce{[PtCl2(NH3)2]}$, is synthesized from $\ce{[PtCl4]^2-}$ and $\ce{NH3}$: the first $\ce{NH3}$ replaces any Cl; in the second step the Cl displaced is the one trans to Cl (not the one trans to $\ce{NH3}$), because the trans effect of $\ce{Cl-}$ is greater than that of $\ce{NH3}$, and the two $\ce{NH3}$ ligands end up cis. Conversely, in the reaction of $\ce{[Pt(NH3)4]^2+}$ with $\ce{Cl-}$ the second Cl enters trans to the first Cl, giving the trans isomer (with no anticancer activity).

![The trans effect ($\ce{Cl-}$ > $\ce{NH3}$) controls the two isomers of $\ce{[PtCl2(NH3)2]}$ (* marks the ligand displaced in the next step). Top: starting from $\ce{[PtCl4]^2-}$, the first $\ce{NH3}$ replaces any Cl and the second replaces the Cl trans to Cl, so the two $\ce{NH3}$ are cis, giving cisplatin; bottom: starting from $\ce{[Pt(NH3)4]^2+}$, the second $\ce{Cl-}$ enters trans to the first Cl, giving the trans isomer without anticancer activity](./plots/trans-effect-cisplatin.py)

### 28.4.2. Oxidative Addition

**Definition 28.4.2 (Oxidative Addition)** The reaction in which the σ bond of a molecule A–B is broken and both A and B bond to a coordinatively unsaturated low-valent metal, increasing both the oxidation state and the coordination number of the metal by 2, is called **oxidative addition**:

$$
\ce{L_nM^{(m)} + A-B -> L_nM^{(m+2)}(A)(B)}.
$$

(In dinuclear complexes each of the two metals is oxidized by 1, as in $\ce{2 [Co(CN)5]^3- + H2 -> 2 [CoH(CN)5]^3-}$.)

A metal that undergoes oxidative addition must satisfy two conditions at once: it must be coordinatively unsaturated (with two vacant sites, or able to dissociate to create them), and it must have a usable nonbonding d electron pair and be able to raise its **oxidation state** ($\mathrm{d}^0$ Ti(IV) and Zr(IV) cannot undergo oxidative addition). Electron-rich, low-valent metals react fastest: Pd(0), Pt(0), Ni(0) ($\mathrm{d}^{10}$), Rh(I) and Ir(I) ($\mathrm{d}^8$). Depending on the substrate, there are four mechanisms of oxidative addition.

1. Concerted addition: A–B first coordinates to the metal through its σ bond (a σ complex), the metal then donates d electrons back into the σ* orbital of A–B, A–B breaks, and A and B bond to the metal simultaneously through a three-center transition state; in the product A and B are cis, and the configuration at a carbon bonded to A is retained. Nonpolar H–H, C–H, Si–H and B–H bonds, and the addition of aryl and alkenyl halides to Pd(0), follow this mechanism. For example, Vaska's complex adds $\ce{H2}$ (bond energy $436\,\mathrm{kJ\,mol^{-1}}$) rapidly at room temperature to give a dihydride in which the two H atoms are cis; the two H atoms are trans to Cl and CO, respectively, so two sets of signals appear in the ¹H NMR spectrum, which is evidence for cis addition. Oxidative addition of C–C bonds is rare (the C–C σ orbital is strongly directional and surrounded by substituents) and needs the help of **ring strain** (cyclopropanes, biphenylene) or chelation (a pincer ligand first pulls the metal close to the C–C bond).
2. SN2-type addition: the nonbonding d electron pair of the low-valent metal acts as a **nucleophile** and attacks the carbon of an alkyl halide from the back, the halide ion leaves to give an **ion pair**, and the halide ion then binds to the metal. As in the organic **SN2 reaction**, the configuration at carbon is inverted, the reaction is fast at primary carbon and does not occur at tertiary carbon, and a good **leaving group** helps; halomethanes and allylic, benzylic and acyl halides react by this mechanism. In the product R and X can be cis or trans: for example, $\ce{CH3I}$ and Vaska's complex in a nonpolar solvent give a product in which $\ce{CH3}$ and I are trans, because $\ce{CH3}$ has a strong trans effect: in the 16-electron five-coordinate cation formed in the first step, $\ce{CH3}$ lies trans to the vacant site, and $\ce{I-}$ then enters this vacant site. The first step changes only the oxidation state (+2), the second only the electron count (+2), and together the two steps constitute the complete oxidative addition.
3. Radical mechanism: the metal transfers one electron to the σ* orbital of R–X (**single electron transfer**) or abstracts a halogen atom from R–X to give $\ce{R*}$, which then combines with the metal. The reactions of secondary and tertiary alkyl halides with metals such as Ni(0) and Co(II) often follow this mechanism, which can be nonchain (radical pairs recombining in the solvent cage) or chain. The evidence is loss of stereochemistry and the cyclized, rearranged products given by **radical clock** ([6.5.7](/6.5.7#sec-7.5)) substrates such as 6-bromohex-1-ene.
4. Ionic mechanism: a strong acid HX dissociates in a polar solvent, and the metal is first protonated (the metal acting as a Brønsted base) and then binds $\ce{X-}$, or first binds $\ce{X-}$ and is then protonated; the result is the same as for oxidative addition.

![Two oxidative additions. Top: H₂ first coordinates through its σ bond to the 16-electron Vaska's complex, d electrons of the metal are donated back into the σ* orbital of H–H, and through a three-center transition state cis-dihydrido Ir(III) forms; bottom: SN2-type oxidative addition of CH₃I, the d electron pair of Ir(I) attacks the methyl carbon from the back, I⁻ leaves and then binds to the metal](./plots/oxidative-addition.py)

Oxidative addition of aryl halides to Pd(0) is the first step of **cross-coupling** (Section 6.5.29), and the rate decreases in the order ArI > ArOTf ≈ ArBr ≫ ArCl, consistent with the order of C–X bond energies (about $272$, $337$ and $400\,\mathrm{kJ\,mol^{-1}}$ for $\ce{C6H5-I}$, $\ce{C6H5-Br}$ and $\ce{C6H5-Cl}$); aryl chlorides are cheap and readily available, but need bulky, electron-rich phosphines or NHCs to react smoothly (Section 28.3.3).

### 28.4.3. Reductive Elimination

**Definition 28.4.3 (Reductive Elimination)** The reaction in which two X-type ligands A and B on a metal bond to each other and leave the metal as A–B, decreasing both the oxidation state and the coordination number of the metal by 2, is called **reductive elimination**; it is the reverse of oxidative addition.

In catalytic cycles, reductive elimination is usually the last step, forming the product, and at the same time returns the metal to a low oxidation state so that it can reenter the cycle. Its features are:

- A and B must be cis. A trans dialkyl complex must first isomerize to the cis form (often through ligand dissociation) before elimination.
- It is concerted, passing through a nonpolar three-center transition state, with retention of configuration at the migrating carbon.
- Elimination involving H (C–H, Si–H) is much faster than C–C elimination: the 1s orbital of H is spherical and can overlap the orbitals of two atoms simultaneously in the transition state, whereas the orbitals of an $\mathrm{sp}^3$ carbon are directional; the C–H bond formed can also stay on the metal for a while as a σ complex.
- Metals that undergo reductive elimination readily are those of high oxidation state whose products are stable: $\mathrm{d}^8$ Ni(II), Pd(II), Au(III), and $\mathrm{d}^6$ Pt(IV), Pd(IV), Ir(III), Rh(III).

![Reductive elimination from cis-dimethylpalladium(II): the two methyl groups bond directly on the metal and leave as ethane, and Pd(II) is reduced to Pd(0)](./plots/reductive-elimination.py)

The driving force of reductive elimination is opposite to that of oxidative addition: the more electron-poor and the more crowded the metal, the faster the elimination. Common ways to promote it are: adding an electron-poor alkene (maleic anhydride, acrylonitrile), which coordinates to the metal and accepts back-donation, lowering the electron density of the metal and weakening the M–C bond; allowing ligands to dissociate, lowering the coordination number (three-coordinate T-shaped Pd(II) eliminates much faster than four-coordinate); and using bulky monophosphines or bisphosphines with a large bite angle (P–M–P angle), such as Xantphos, to squeeze the two groups to be eliminated together.

### 28.4.4. Migratory Insertion

**Definition 28.4.4 (Migratory Insertion)** The reaction in which an X-type ligand R adjacent (cis) on the metal migrates to an unsaturated ligand A=B (or A), so that A=B formally "inserts" between the M–R bond, is called **migratory insertion**. According to which atom of the unsaturated ligand the new metal–ligand bond is attached to, it is classified as 1,1-insertion (M and R attached to the same atom: CO, isocyanides, carbenes, $\ce{M-C(=O)R}$) or 1,2-insertion (M and R attached to adjacent atoms: alkenes, alkynes, aldehydes and ketones, $\ce{M-CH2CH2R}$).

The features of migratory insertion are:

- The two reacting ligands must be cis to each other;
- The oxidation state of the metal is unchanged; the 1-electron R and the 2-electron A=B (3 electrons in all) become one 1-electron new ligand, so the valence electron count decreases by 2 and a coordination site is vacated;
- The reverse reaction (deinsertion, that is, α-elimination and β-elimination) requires a vacant site first.

The classic case is insertion of CO into an M–C bond to give an acyl complex (carbonylation):

$$
\ce{CH3Mn(CO)5 + L -> CH3C(=O)Mn(CO)4L}.
$$

This reaction raises two questions: is the CO in the acyl group the originally coordinated CO or the newly added CO? And did CO insert into the Mn–CH₃ bond, or did the methyl group migrate to an adjacent CO? A set of isotope experiments with ¹³CO (Noack and Calderazzo, 1967) answered both questions.

1. When $\ce{CH3Mn(CO)5}$ reacts with ¹³CO, the ¹³C in the product is not in the acyl group but in a terminal carbonyl cis to the acyl group: the acyl group comes from the original CO cis to the methyl, and the incoming CO merely fills the vacated coordination site.
2. By the **principle of microscopic reversibility**, the forward and reverse reactions pass through the same path, so the forward reaction can be studied through the reverse reaction (decarbonylation). With ¹³CO placed cis to the acyl group, cis-$\ce{CH3C(O)Mn(CO)4(^{13}CO)}$ is decarbonylated on heating: if CO deinsertion occurred ("back to the original position"), the methyl would not move and the ¹³CO in the product could only be cis to the methyl; if the methyl migrated back to the metal, it could land on any of the four positions adjacent to the acyl group, and the product should be 25% free of ¹³C (the CO lost being exactly the ¹³CO), 50% with methyl cis to ¹³CO and 25% trans. Both cis and trans products are observed, in proportions consistent with the latter prediction. Hence "CO insertion" is in fact alkyl migration, with retention of configuration at the migrating carbon.

![Methyl migratory insertion: the methyl group in CH₃Mn(CO)₅ migrates with the electron pair of the Mn–C bond to the carbon of the adjacent CO, forming a 16-electron acyl complex, and the vacated coordination site is filled by L](./plots/co-insertion.py)

1,2-Insertion of an alkene into an M–H bond gives a metal alkyl, a key step in homogeneous hydrogenation, alkene isomerization and hydroformylation:

- The alkene first coordinates to the metal; M, H and the two alkene carbons are coplanar in the transition state, which is four-centered, and H and M add to the same face of the double bond (syn addition);
- The reverse reaction is β-hydride elimination (Section 28.4.5), and the two are often in equilibrium. For ethylene ($\ce{CH2=CH2}$) the equilibrium lies on the side of the alkene and hydride; for tetrafluoroethylene it lies completely on the side of the insertion product: the high **electronegativity** of F strengthens back-donation from the metal into the C–F σ*, and the M–$\ce{CF2CF2H}$ bond is especially strong;
- The **regioselectivity** is determined mainly by steric hindrance: the metal tends to attach to the less substituted carbon, giving a primary alkyl (formally anti-Markovnikov). With alkenes bearing electron-withdrawing groups (acrylates), the metal tends to attach to the α carbon of the electron-withdrawing group, because the M–C bond formed is stronger (the M–C bond strength increases with electron-withdrawing groups on carbon). Simple α-olefins show low selectivity.

![1,2-Migratory insertion of an alkene into an M–H bond: coordinated ethylene and the adjacent hydride pass through a four-center transition state, hydrogen migrates to one alkene carbon and the metal bonds to the other, giving an ethyl complex (syn addition)](./plots/alkene-insertion.py)

Hydrozirconation is a useful example: Schwartz's reagent $\ce{Cp2Zr(H)Cl}$ reacts with terminal alkenes with Zr adding to the terminal carbon; internal alkenes (such as oct-2-ene, oct-3-ene and oct-4-ene) all finally give the same primary alkylzirconium $\ce{Cp2Zr(Cl)(CH2)7CH3}$, for the reason given in Question 4. The alkylzirconium then reacts with halogens and **electrophiles**, which amounts to an anti-Markovnikov functionalization of the alkene.

![Zirconium "walking" along the carbon chain ([Zr] = $\ce{Cp2ZrCl}$, R is n-hexyl, taking oct-2-ene as example): the secondary alkyl with Zr on C2 undergoes β-H elimination toward the methyl side, the electron pair of the C–H bond moving to zirconium to form Zr–H and the electrons of the Zr–C bond forming a C=C bond, giving the hydride complex of oct-1-ene; the alkene reinserts into Zr–H with the opposite regioselectivity, and zirconium attaches to the less hindered terminal carbon. Repeated elimination and reinsertion move the metal along the chain, and the least crowded primary alkylzirconium accumulates](./plots/chain-walking.py)

Insertion of alkenes into M–C bonds lengthens the carbon chain, and repeated insertion is coordination polymerization (the Cossee–Arlman mechanism, **Ziegler–Natta catalysts**, [6.5.11](/6.5.11#sec-11.11)): the alkene coordinates to a vacant site on Ti and inserts into the Ti–C bond, the position originally occupied by the chain becomes vacant again, and the next monomer coordinates and inserts.

### 28.4.5. β-Hydride Elimination and Other Eliminations

**Definition 28.4.5 (β-Hydride Elimination)** The reaction in which, in a metal alkyl, the metal abstracts a hydrogen from the β carbon of the alkyl group, giving a metal hydride and a coordinated alkene, is called **β-hydride elimination**; it is the reverse of 1,2-insertion of an alkene into an M–H bond:

$$
\ce{L_nM-CH2CH2R <=> L_nM(H)(CH2=CHR)}.
$$

The requirements for β-hydride elimination are:

1. The β carbon of the alkyl group carries a hydrogen;
2. M–C–C–H can adopt an approximately syn-coplanar arrangement (a **torsion angle** near 0°), so that the β-H approaches the metal;
3. The metal has a vacant coordination site cis to the alkyl group (after the reaction the metal has one more ligand: the valence electron count increases by 2), so an 18-electron complex must first dissociate a ligand;
4. The alkene formed is sufficiently stable.

![β-Hydride elimination: in a coordinatively unsaturated alkylpalladium the β-H and Pd are syn-coplanar, the electron pair of the C–H bond moves to the metal, and the electron pair of the Pd–C bond becomes the π bond of C=C, giving a palladium hydride and a coordinated alkene](./plots/beta-hydride-elimination.py)

β-Hydride elimination is the main decomposition pathway of metal alkyls. In the **Heck reaction** it is the key product-forming step, in **cross-coupling** it is the main side reaction of alkyl substrates (Section 6.5.29), and repeated insertion and elimination isomerize alkenes and make the metal "walk" along the carbon chain. Ways of suppressing β-hydride elimination are described in Section 28.5.1.

Other eliminations:

- α-Hydride elimination: the metal abstracts a hydrogen from the α carbon to give a metal carbene and hydride, common in high-oxidation-state early transition-metal alkyls with no hydrogen on the β carbon (formation of Schrock carbenes, Section 28.5.4).
- β-Heteroatom elimination: a group such as OR, halogen or $\ce{OAc}$ at the β position is transferred to the metal, giving an alkene, for example the elimination of a β-alkoxyalkylpalladium to an alkene and $\ce{Pd-OR}$; it competes with β-hydride elimination and is important in the Tsuji–Trost and some Heck reactions.
- β-Carbon elimination: cleavage of a β C–C bond (the reverse of insertion into M–C), mostly seen in strained cyclobutanols and cyclopropylmethylmetal compounds.

### 28.4.6. Transmetalation

**Definition 28.4.6 (Transmetalation)** The reaction in which an organic group is transferred from one metal to another is called **transmetalation**, usually from the more electropositive metal to the less electropositive one:

$$
\ce{M-R + M'-X -> M-X + M'-R}.
$$

Transmetalation can occur between main-group metals ($\ce{2 RLi + CuI -> R2CuLi + LiI}$, the preparation of **Gilman reagents**, [6.5.10](/6.5.10#sec-10.4.2); $\ce{RLi + ZnCl2 -> RZnCl + LiCl}$), and can also transfer a group from a main-group organometallic reagent to a halide of a transition metal: this is the general method for preparing σ-alkyl and aryl transition-metal compounds and is the second step of **cross-coupling** (Section 6.5.29). Different coupling reactions use different main-group organometallic reagents, which differ mainly in the balance between **nucleophilicity** and functional-group tolerance:

| Coupling reaction | Transmetalating reagent | Features |
|---|---|---|
| Kumada | RMgX (RLi: Murahashi) | most reactive, does not tolerate functional groups such as carbonyl, ester and nitrile |
| Negishi | RZnX | high reactivity, much better functional-group tolerance |
| Stille | $\ce{RSnR'3}$ | neutral, stable to air and water, tolerates almost all functional groups; tin compounds are toxic |
| Suzuki–Miyaura | $\ce{RB(OH)2}$, $\ce{RB(OR')2}$, R–9-BBN | stable and of low toxicity, must be activated with base |
| Hiyama | $\ce{RSiR'3}$ | must be activated with $\ce{F-}$ or base to a five-coordinate silicate |
| Sonogashira | copper acetylide (formed in situ from a terminal alkyne and Cu(I)) | for terminal alkynes only |

The driving force of transmetalation is thermodynamic: the more electropositive metal forms the stronger (more ionic) M–X bond, and carbon is transferred to the metal with which it can form a more covalent bond; the **standard molar enthalpy of formation** of lithium and magnesium halides makes the reaction strongly exothermic. Boron and silicon are not electropositive enough and their C–B and C–Si bonds are of low polarity, so they must first be combined with base or $\ce{F-}$ into a four-coordinate borate or five-coordinate silicate, raising the nucleophilicity of the group to be transferred (Section 6.5.29). Transmetalation generally passes through a four-center bridged transition state, with retention of configuration at carbon.

![Transmetalation: the electron pair of the Zn–C bond of an arylzinc reagent attacks Pd(II) while the Pd–Br bond breaks and Br is transferred to zinc; through a four-center bridged transition state the aryl group is transferred from zinc to palladium (the second step of the Negishi coupling)](./plots/transmetalation.py)

### 28.4.7. Nucleophilic and Electrophilic Attack on Ligands

In the elementary reactions above, the new bonds are formed within the coordination sphere of the metal; another class of reactions is direct attack of an external reagent on a ligand without first bonding to the metal ("outer-sphere" attack).

- **Nucleophilic addition**: an electron-poor metal fragment (positively charged, or carrying strong π acceptors such as CO, that is, a weak π base and strong σ acid) gives the ligand a partial positive charge, and a **nucleophile** adds directly to the ligand: coordinated CO is attacked by $\ce{R-}$ to give an acyl anion and then a Fischer carbene (Section 28.5.4); a coordinated alkene is attacked by water (the **Wacker oxidation**), a coordinated $\eta^3$-allyl by malonate anions (the **Tsuji–Trost reaction**), and a coordinated arene by a **carbanion** (Section 28.5.3). Outer-sphere attack occurs on the face opposite the metal, so the nucleophile and the metal are on opposite sides of the ligand (anti addition).
- Nucleophilic abstraction: a nucleophile removes a whole ligand or part of one from the metal, as when a $\ce{CO}$ ligand loses its oxygen atom to an amine oxide (giving $\ce{CO2}$ and a vacant site, often used to remove CO).
- **Electrophilic addition** and abstraction: an electron-rich metal fragment (a strong π base) gives the ligand a partial negative charge, and **electrophiles** attack the ligand: $\ce{H+}$ protonates and cleaves an M–C bond (protonolysis), $\ce{X2}$ halogenolyzes an M–C bond, the trityl cation $\ce{Ph3C+}$ abstracts $\ce{H-}$ from an alkyl to give a cationic alkene complex or carbene complex, and the Meerwein salt $\ce{Me3O+BF4-}$ methylates the oxygen of an acyl anion (Section 28.5.4). Electrophilic attack is used somewhat less in organic synthesis.

A typical example of nucleophilic attack on coordinated CO is the reaction of the 18-electron cation $\ce{[CpRe(CO)2(NO)]+}$ with $\ce{H-}$ (from $\ce{NaBH4}$): hydride does not attack the metal (the metal already has 18 electrons, and accepting another electron pair would give 20) but attacks the partially positive carbonyl carbon, giving the neutral formyl complex $\ce{CpRe(CO)(NO)(CHO)}$.

![Nucleophilic addition to coordinated CO and the formation of a Fischer carbene: the carbanion of phenyllithium attacks the carbon of one CO in W(CO)₆, one π pair of C≡O moving onto oxygen to give an acyltungstate; methylation of oxygen with a Meerwein salt then gives the Fischer carbene complex (CO)₅W=C(OMe)Ph](./plots/fischer-carbene.py)

## 28.5. Common Transition-Metal Organometallic Compounds

This section briefly introduces several important classes of complexes by ligand type, with emphasis on their bonding features and uses in synthesis; preparations and reactions are listed only in outline.

### 28.5.1. σ-Alkyl and Acyl Complexes

Alkyls of transition metals were long considered "unstable"; the first isolable example, $\ce{(CH3)3PtI}$ (Pope and Peachey, 1907), appeared more than half a century later than $\ce{ZnEt2}$. This instability is kinetic and not thermodynamic: the M–C bond energies of transition metals, about $120$–$270\,\mathrm{kJ\,mol^{-1}}$, are comparable to those of main-group metals ($\ce{Pb-C}$ is about $150\,\mathrm{kJ\,mol^{-1}}$, and tetraethyllead can be distilled and was used in large quantities as a gasoline antiknock agent); transition-metal alkyls decompose readily because there are concerted decomposition pathways of very low activation energy, β-hydride elimination and reductive elimination. Simple titanium alkyls such as $\ce{TiMe4}$ decompose below room temperature.

Following the four conditions of Section 28.4.5, stable metal alkyls can be designed:

1. The alkyl has no β-H: methyl, benzyl $\ce{CH2Ph}$, neopentyl $\ce{CH2CMe3}$, trimethylsilylmethyl $\ce{CH2SiMe3}$, perfluoroalkyl, as in $\ce{WMe6}$ and $\ce{Ti(CH2Ph)4}$;
2. The β-H cannot approach the metal: as in $\ce{Cr(CMe3)4}$, where steric hindrance keeps the β-H away from the metal;
3. The elimination product would be an unstable alkene: elimination from 1-norbornyl would give a bridgehead alkene violating Bredt's rule, so compounds such as tetrakis(1-norbornyl)cobalt are quite stable to heat and air;
4. The metal has no vacant site: in 18-electron complexes such as $\ce{CpFe(CO)2Et}$, Cp and CO are tightly bound, and a CO must dissociate before β-hydride elimination can occur.

The preparation of σ-alkyl complexes uses the elementary reactions described above: transmetalation with main-group organometallic reagents; insertion of alkenes into M–H; **nucleophilic substitution** of alkyl halides by metal anions (**SN2**-type oxidative addition, $\ce{Na[CpFe(CO)2] + CH3I -> CpFe(CO)2CH3 + NaI}$); and oxidative addition. Their reactions include cleavage of the M–C bond by halogens and HX, and insertion of small molecules such as CO and $\ce{SO2}$. σ-Alkenyl, aryl and alkynyl complexes are more stable than alkyls, because the M–C bonds to $\mathrm{sp}^2$ and $\mathrm{sp}$ carbons are stronger and β-hydride elimination cannot occur.

Acyl complexes are obtained by CO insertion (Section 28.4.4), by reaction of metal anions with acyl chlorides, or by attack of **nucleophiles** on coordinated CO. The $\tilde\nu(\ce{C=O})$ of an acyl group is about $1600$–$1680\,\mathrm{cm^{-1}}$, lower than that of a ketone, showing electron donation from the metal. Formyl complexes $\ce{M-CHO}$ are very unstable and readily decarbonylate to $\ce{M(H)(CO)}$, and can be isolated only in 18-electron cations such as that of Section 28.4.7; higher acyl complexes are much more stable, and their decarbonylation and CO insertion are the reverse of each other. The lone pair of the acyl oxygen can be attacked by **electrophiles** to give Fischer carbenes.

### 28.5.2. η³-Allyl Complexes

An allyl group can coordinate as $\eta^1$ (X-type, 1 electron) or $\eta^3$ (LX-type, 3 electrons), and the two modes interconvert readily. The three carbons of an $\eta^3$-allyl are at roughly equal distances from the metal, and substituents on the terminal carbons occupy syn (on the same side as the central C–H) or anti positions; the change $\eta^3 \to \eta^1 \to \eta^3$ (with rotation about the C–C single bond in the $\eta^1$ form) interchanges syn and anti substituents, which appears as coalescence of peaks in the NMR spectrum.

$\eta^3$-Allyl complexes can be obtained by oxidative addition of allylic halides or allyl acetates to Pd(0) (in this step the configuration at the carbon losing the **leaving group** is inverted), by activation of an allylic C–H bond by Pd(II), or by protonation of diene complexes. The commonly used precursor $\ce{[(\eta^3-C3H5)PdCl]2}$ (allylpalladium chloride dimer) is prepared from $\ce{Na2PdCl4}$, allyl chloride and CO in water. The most important reaction of $\eta^3$-allylpalladium is attack at a terminal carbon, from the face opposite the metal, by soft carbon **nucleophiles** (Section 28.4.7); this is the **Tsuji–Trost reaction** ([6.5.29](/6.5.29#sec-29.5)).

### 28.5.3. Metallocenes and Arene Complexes

**Definition 28.5.1 (Metallocene)** A complex in which a metal is sandwiched between two parallel (or tilted) $\eta^5$-cyclopentadienyl rings is called a **metallocene**, such as ferrocene $\ce{Cp2Fe}$; complexes in which a metal is sandwiched between two aromatic rings are collectively called sandwich compounds.

The cyclopentadienyl anion is a 6π aromatic ion ([6.5.13](/6.5.13#sec-13.5.1)) and one of the most important ligands in organometallic chemistry: as an $\ce{L2X}$ ligand it occupies three coordination sites, is bound tightly and seldom takes part in reactions, which suits it as a "spectator ligand"; pentamethylcyclopentadienyl, Cp*, is more electron-donating and bulkier.

Ferrocene is an orange crystalline solid, mp $173\,^\circ\mathrm{C}$, stable in air and not decomposing up to about $400\,^\circ\mathrm{C}$, with 18 electrons and diamagnetic. Its rings have **aromaticity** like benzene but are much more electron-rich: Friedel–Crafts acetylation (the **Friedel–Crafts reaction**, [6.5.14](/6.5.14#sec-14.9.3)) is about $10^6$ times faster than for benzene and can be carried out under mild conditions; it is easily and reversibly oxidized by one electron to the blue ferrocenium cation $\ce{[Cp2Fe]+}$, and the $\ce{[Cp2Fe]+}/\ce{Cp2Fe}$ **redox couple** is recommended by IUPAC as the internal standard of nonaqueous electrochemistry ([6.1.11](/6.1.11), [6.4.6](/6.4.6)).

Metallocenes of other metals in the same period deviate from 18 electrons, and their properties change accordingly: 19-electron cobaltocene is a strong reducing agent (the $\ce{[Cp2Co]+}/\ce{Cp2Co}$ couple is about $1.33\,\mathrm{V}$ more negative than the ferrocene couple, in dichloromethane); 20-electron nickelocene is paramagnetic and easily oxidized; manganocene is high-spin and the only ionic one among the d-block metallocenes. Metallocenes of Group 4 metals have a bent sandwich structure, in which two or three further ligands can bind between the two Cp rings, as in $\ce{Cp2TiCl2}$ and $\ce{Cp2ZrCl2}$; activated with methylaluminoxane (MAO), they are highly active alkene polymerization catalysts (metallocene catalysts, [6.5.11](/6.5.11#sec-11.11)), and varying the substitution and bridging of the Cp rings allows precise control of the stereoregularity of polypropylene.

Arenes usually coordinate in the $\eta^6$ mode (6 electrons, $\ce{L3}$) and may also coordinate as $\eta^4$ or $\eta^2$. Bis(benzene)chromium $\ce{Cr}(\eta^6\text{-}\ce{C6H6})_2$ was made by Fischer and Hafner in 1955 from $\ce{CrCl3}$, Al, $\ce{AlCl3}$ and benzene (the Fischer–Hafner method). More useful in synthesis are $(\eta^6\text{-arene})\ce{Cr(CO)3}$ complexes: the three CO ligands accept back-donation from Cr, making $\ce{Cr(CO)3}$ a strongly electron-withdrawing group comparable to a para nitro group (the acidity of coordinated benzoic acid is close to that of 4-nitrobenzoic acid), so the coordinated arene no longer undergoes **electrophilic aromatic substitution** but readily undergoes **nucleophilic aromatic substitution** (Cl in coordinated chlorobenzene is displaced by $\ce{MeO-}$) and **nucleophilic addition** of **carbanions**; the acidity of ring H and **benzylic position** H is increased; the bulky $\ce{Cr(CO)3}$ shields one face of the arene so that reagents can attack only from the other face, which allows control of stereochemistry. After the reaction the metal is removed by light or mild oxidants.

![Nucleophilic aromatic substitution of (η⁶-chlorobenzene)tricarbonylchromium: $\ce{Cr(CO)3}$ is strongly electron-withdrawing; methoxide adds to the ipso carbon from the face opposite chromium, the π electrons of the ring move into the cyclohexadienyl system coordinated to the metal, giving a negatively charged η⁵-cyclohexadienyl complex (a Meisenheimer-type intermediate); chloride leaves, giving the η⁶ complex of anisole, from which the metal is removed by light or mild oxidation](./plots/arene-chromium-snar.py)

### 28.5.4. Metal Carbenes and Carbynes

Metal carbenes are formally compounds $\ce{L_nM=CR2}$ in which a metal is bonded to a **carbene** ([6.5.11](/6.5.11#sec-11.10)) by a double bond, and metal carbynes are compounds $\ce{L_nM#CR}$ with a triple bond. Free carbenes exist in two electronic states, the **singlet state** and the **triplet state**, and coordinated carbenes correspondingly have two extreme types.

**Definition 28.5.2 (Fischer Carbene)** A metal carbene derived from a singlet carbene, in which the carbene carbon carries a π-donating heteroatom such as OR or $\ce{NR2}$, bound to a middle or late transition metal of low oxidation state (Cr, Mo, W, Mn, Fe, and so on) that carries π-acceptor ligands such as CO, is called a **Fischer carbene**, for example $\ce{(CO)5W=C(OMe)Ph}$. The carbene carbon is electrophilic.

**Definition 28.5.3 (Schrock Carbene)** A metal carbene derived from a triplet carbene, in which the carbene carbon carries only H or alkyl groups, bound to an early transition metal of high oxidation state (Ta, Nb, Ti, Mo, W, and so on) that carries electron-donating ligands such as alkyl, Cp and alkoxide, is called a **Schrock carbene** (an alkylidene complex), for example $\ce{Cp2Ta(CH3)(=CH2)}$. The carbene carbon is nucleophilic.

| | Fischer carbene | Schrock carbene |
|---|---|---|
| Origin of the carbene | singlet, neutral 2-electron L-type ligand | triplet, $\ce{X2}$-type ligand (ionic count $\ce{CR2^2-}$, 4 electrons) |
| Bonding | σ donation C → M + π back-donation M → C (like CO) | two covalent bonds (σ + π), the M=C bond polarized toward carbon |
| Substituents on the carbene carbon | heteroatoms such as OR, $\ce{NR2}$ (π donors) | H, alkyl |
| Metal | low **oxidation state**, middle and late transition metals (Cr, Mo, W, Mn, Fe), $\mathrm{d}^6$, 18 electrons | high oxidation state, early transition metals (Ta, Nb, Ti, Mo, W), $\mathrm{d}^0$ or $\mathrm{d}^2$, 10–16 electrons |
| Other ligands | π acids such as CO | donors such as alkyl, Cp, alkoxide |
| Reactivity of the carbene carbon | electrophilic (attacked by **nucleophiles**, like the carbonyl carbon of an ester) | nucleophilic (attacks **Lewis acids** and carbonyl groups, like a phosphorus ylide) |

(Grubbs's ruthenium carbene $\ce{L2Cl2Ru=CHPh}$ is a neutral late-transition-metal carbene with no heteroatom on the carbene carbon, intermediate in properties between the two classes, and is usually not assigned to either.)

In Fischer carbenes the empty p orbital of the carbene carbon accepts both back-donation from the metal and donation from the heteroatom lone pair, and the two compete: X-ray structures show considerable double-bond character in the C–O bond and an M=C bond order much lower than 2, the true structure being closer to the resonance form $\ce{M^- - C(=O^+Me)Ph}$. Fischer carbenes therefore resemble esters: the carbene carbon is attacked by nucleophiles such as amines and alcohols, with substitution (for example OMe replaced by $\ce{NR2}$), and the C–H at the α position of the carbene carbon is distinctly acidic (like the α-H of an ester, it can be deprotonated by base and alkylated). Its classical preparation is the two steps of Section 28.4.7: attack of an organolithium on a CO of $\ce{W(CO)6}$, followed by O-methylation with a Meerwein salt.

The classical preparation of Schrock carbenes is α-hydride elimination: $\ce{Ta(CH2CMe3)5}$ cannot exist, because steric crowding forces an α-H of one neopentyl group to be taken by an adjacent neopentyl group, which leaves as neopentane, giving $\ce{(Me3CCH2)3Ta=CHCMe3}$. The carbon of a Schrock carbene carries a partial negative charge and, like an **ylide**, reacts with aldehydes and ketones to give alkenes (similar to the **Wittig reaction**, [6.5.16](/6.5.16#sec-16.8.1)), driven by the strong M=O bond; the titanium Tebbe reagent $\ce{Cp2Ti(\mu-Cl)(\mu-CH2)AlMe2}$ releases $\ce{Cp2Ti=CH2}$, which can methylenate even esters and amides without causing **keto–enol tautomerism** (enolization) of aldehydes and ketones, which phosphorus ylides cannot do. High-valent molybdenum and tungsten alkylidene complexes undergo [2+2] **cycloaddition** with alkenes to give metallacyclobutanes, the basis of **olefin metathesis** (Section 6.5.29).

![Formation of a Schrock carbene by α-hydrogen abstraction (Np is neopentyl $\ce{CH2CMe3}$): steric crowding in $\ce{Ta(CH2CMe3)5}$ brings two neopentyl groups together, the electrons of the Ta–C bond of one neopentyl group take the α-H of the adjacent neopentyl group (Ta, C, H and C form a four-center transition state), and the C–H electrons of the latter form the π bond of Ta=C; neopentane leaves, giving a tantalum(V) alkylidene complex, with no change in the oxidation state of tantalum](./plots/alpha-elimination.py)

![Methylenation of an ester by the Tebbe reagent: the $\ce{Cp2Ti=CH2}$ released (a Schrock carbene) undergoes [2+2] cycloaddition with C=O, the nucleophilic carbene carbon bonding to the carbonyl carbon and the carbonyl oxygen to titanium, giving an oxatitanacyclobutane; the four-membered ring cleaves in the other direction (retro-[2+2]), driven by the strong Ti=O bond, giving the enol ether and $\ce{Cp2Ti=O}$](./plots/tebbe-olefination.py)

Metal carbynes also include Fischer types (such as the $\ce{I(CO)4W#CMe}$ obtained by Fischer in 1973) and Schrock types (such as $\ce{(t-BuO)3W#C(t-Bu)}$, used in alkyne metathesis), but the distinction is less clear than for carbenes.

### 28.5.5. Metal Hydrides and Agostic Bonds

The M–H bond of transition-metal hydrides takes part in many catalytic reactions such as hydrogenation, hydroformylation and isomerization. The first transition-metal hydride, $\ce{H2Fe(CO)4}$, was made by Hieber in 1931. Their characterization has several features:

- ¹H NMR: hydrogen on a metal usually appears at high field, with **chemical shifts** $\delta$ of about $0$ to $-25$ (in a few cases to $-60$), which is the most convenient way of recognizing metal hydrides ([6.4.12](/6.4.12)); **coupling constants** to ³¹P reflect the stereochemistry, with trans $^2J_{\mathrm{PH}}$ about $90$–$150\,\mathrm{Hz}$ and cis about $15$–$30\,\mathrm{Hz}$; coupling to spin-active metal nuclei such as ¹⁰³Rh, ¹⁸³W and ¹⁹⁵Pt also occurs.
- Infrared: $\tilde\nu(\ce{M-H})$ is about $1500$–$2200\,\mathrm{cm^{-1}}$, with weak intensity.
- Crystal structure: H scatters X-rays very weakly and its position is hard to determine; reliable H positions require neutron diffraction.

The hydrogen of an M–H bond is −1 by convention, yet it can actually react in three ways: it can be removed by a base as $\ce{H+}$ ($\ce{HCo(CO)4}$ is a strong acid); it can be transferred as $\ce{H-}$ to an **electrophile** or inserted into an unsaturated bond (Section 28.4.4); and it can be transferred as an H atom to a radical or alkene (**hydrogen atom transfer**; the M–H bond of $\ce{CpCr(CO)3H}$ is weak, and in recent years HAT from Fe, Co and Mn hydrides has been used for Markovnikov hydrofunctionalization of alkenes).

$\ce{H2}$ can also coordinate without bond cleavage: Kubas obtained the first dihydrogen complex, $\ce{W(CO)3(P^{i}Pr3)2}(\eta^2\text{-}\ce{H2})$, in 1984. $\ce{H2}$ donates the electron pair of the H–H σ bond to the metal (a 2-electron L-type ligand) and accepts back-donation from the metal into σ*; the stronger the back-donation, the longer the H–H bond, until it breaks to give a dihydride, which is precisely the path of concerted oxidative addition (Section 28.4.2). Coordination greatly increases the acidity of $\ce{H2}$ (it can be deprotonated by weak bases), because its **conjugate base** $\ce{H-}$ binds to the metal much more strongly than $\ce{H2}$ does. The hydrogen of M–H carries a partial negative charge and can also form "dihydrogen bonds" with protons of N–H and O–H ($\ce{M-H^{\delta-}\cdots{}^{\delta+}H-N}$, H···H about $1.8\,\text{Å}$).

**Definition 28.5.4 (Agostic Interaction)** The three-center two-electron M···H–C interaction formed by the σ electron pair of a C–H bond of a ligand with a coordinatively unsaturated metal is called an **agostic interaction** (Brookhart and Green, 1983).

An agostic interaction lengthens the C–H bond, decreases $^1J_{\mathrm{CH}}$ (about $75$–$100\,\mathrm{Hz}$, against about $125\,\mathrm{Hz}$ for a normal $\mathrm{sp}^3$ C–H) and moves the ¹H chemical shift to high field. A β-agostic alkyl complex is an intermediate "frozen" on the way to β-hydride elimination; in coordination polymerization an α-agostic bond can stabilize the transition state of insertion and help control the stereochemistry of polymerization.

### 28.5.6. Organometallic Compounds in Living Systems and Research Frontiers

Metal–carbon bonds also exist in living systems. In the coenzyme form of vitamin B₁₂ (adenosylcobalamin), Co(III) is bonded directly to the $\ce{CH2}$ of 5′-deoxyadenosine; the Co–C bond is very weak (about $130\,\mathrm{kJ\,mol^{-1}}$), and enzymatic **homolysis** produces the 5′-deoxyadenosyl **radical**, which initiates carbon-skeleton rearrangements catalyzed by enzymes such as methylmalonyl-CoA mutase; methylcobalamin transfers a methyl group to homocysteine in methionine synthase. The active sites of [FeFe]- and [NiFe]-hydrogenases contain CO and $\ce{CN-}$ ligands, and the FeMo cofactor of nitrogenase has a central carbide. These systems use exactly the concepts of this chapter: back-donation to CO and $\tilde\nu(\mathrm{CO})$, hydrides and dihydrogen complexes, homolysis of metal–carbon bonds. Research frontiers focus on three directions: replacing precious metals such as Pd, Rh and Ir by abundant Fe, Co, Ni and Cu (these 3d metals more often follow single-electron pathways, opening new radical-type reactions); C–H activation without preactivation (under new mechanisms such as concerted metalation–deprotonation, the C–H bond "oxidatively adds" directly to the metal or is cleaved); and the combination of metal **organocatalysis** with photoredox catalysis and electrochemistry (for example the dual Ni/photoredox catalysis, in which changing the oxidation state of the metal, Ni(I)/Ni(III), achieves difficult reductive eliminations, [6.5.31](/6.5.31#sec-31.5)).

![Radical chemistry of coenzyme B₁₂ (adenosylcobalamin, Ado is the rest of 5′-deoxyadenosine): the enzyme causes homolysis of the very weak Co–C bond (about 130 kJ/mol), each atom taking one electron, giving Co(II) cobalamin and the 5′-deoxyadenosyl radical; the latter abstracts a hydrogen atom from the substrate (for example methylmalonyl-CoA, written R–H), giving 5′-deoxyadenosine and a substrate radical, which then undergoes carbon-skeleton rearrangement](./plots/b12-homolysis.py)

## Summary

The language for describing organometallic compounds:

| Concept | Key points |
|---|---|
| Ligand notation | $\eta^n$ number of contiguously bonded atoms, $\mu$ bridging, $\kappa$ coordinating heteroatoms (Definition 28.2.1) |
| L- and X-type ligands | L: neutral 2-electron donors (CO, phosphines, alkenes); X: 1 electron as neutral (H, R, halogens); Cp = $\ce{L2X}$, allyl = LX (Definition 28.2.2) |
| Oxidation state and dⁿ | oxidation state = charge of the complex + number of X-type ligands (each X is −1); $n(\mathrm{d})$ = group number − oxidation state |
| 18-electron rule | all 9 valence orbitals filled; $\mathrm{d}^8$ square-planar complexes (Rh(I), Pd(II), Pt(II)) are often 16-electron, early transition metals often have fewer than 18, and 19- and 20-electron species are easily oxidized (Definition 28.2.3) |
| CO and alkenes | σ donation + π back-donation; the stronger the back-donation, the lower $\tilde\nu(\mathrm{CO})$ and the longer C=C; coordinated alkenes are attacked by nucleophiles (DCD model, Definition 28.3.2) |
| Phosphines | Tolman electronic parameter and cone angle (Definition 28.3.1); bulky, electron-rich ligands promote oxidative addition and reductive elimination |

The six classes of elementary reactions:

| Reaction | Conditions and stereochemistry | Role in catalysis |
|---|---|---|
| Dissociation and association | 18-electron complexes by the dissociative mechanism, 16-electron square-planar complexes by the associative mechanism; trans effect (Definition 28.4.1) | creates vacant sites, binds substrates |
| Oxidative addition (Definition 28.4.2) | low-valent, electron-rich, coordinatively unsaturated metal; four mechanisms: concerted (cis, retention), **SN2** (inversion), radical, ionic | activates H–H, C–X and C–H bonds |
| Reductive elimination (Definition 28.4.3) | cis; retention of configuration; favored by high-valent, electron-poor, crowded metals | forms the product, regenerates the low-valent catalyst |
| Migratory insertion (Definition 28.4.4) | cis; R migrates with retention of configuration; 1,1- (CO) and 1,2- (alkenes, syn addition) | forms C–C and C–H bonds; carbonylation, polymerization |
| β-Hydride elimination (Definition 28.4.5) | needs a β-H, syn-coplanar M–C–C–H, and a vacant site | product formation in the **Heck reaction**; side reaction of alkyl coupling |
| Transmetalation (Definition 28.4.6) | the organic group moves from a more electropositive to a less electropositive metal; B and Si need activation by base or $\ce{F-}$ | introduces the second group in **cross-coupling** |

There is also outer-sphere nucleophilic and electrophilic attack (Wacker, Tsuji–Trost, formation of Fischer carbenes). Common complexes: the instability of σ-alkyls is kinetic (β-hydride elimination); $\eta^3$-allyls are attacked by **nucleophiles** from the face opposite the metal; ferrocene is an electron-rich aromatic system; $\ce{Cr(CO)3}$ makes an arene electron-poor; Fischer carbenes (Definition 28.5.2) are electrophilic and Schrock carbenes (Definition 28.5.3) nucleophilic; metal hydrides appear at high field, and the agostic interaction (Definition 28.5.4) is a prelude to β-hydride elimination.

## Questions

1. Calculate the oxidation state, $\mathrm{d}^n$ and total valence electron count of the metal in the following complexes (checking with both counting methods): (a) $\ce{Mo(CO)3}(\eta^6\text{-}\ce{C6H6})$; (b) $\ce{[CpFe(CO)3]+}$; (c) $\ce{IrCl(CO)(PPh3)2}$ (Vaska's complex) and its adduct with $\ce{H2}$; (d) $\ce{Fe2(CO)6}(\mu\text{-SMe})_2$ (with an Fe–Fe bond, for each Fe).

   **Answer** (a) Mo(0), $\mathrm{d}^6$; covalent count 6 + 6 + 3 × 2 = 18. (b) Cp is −1 and the complex +1, so Fe(II), $\mathrm{d}^6$; ionic count 6 + 6 ($\ce{Cp-}$) + 6 = 18; covalent count 8 + 5 + 6 − 1 (positive charge) = 18. (c) Ir(I), $\mathrm{d}^8$, 9 + 1 + 2 + 4 = 16 electrons, square planar; after addition of $\ce{H2}$, Ir(III), $\mathrm{d}^6$, 16 + 2 = 18 electrons, octahedral. (d) Both SMe groups are X-type (−1 each) and shared by the two Fe atoms, so each Fe is +1, Fe(I), $\mathrm{d}^7$. Covalent count: Fe 8 + 3 × 2 (CO) + 3 (the two bridging SMe groups together give each Fe 1 + 2) + 1 (Fe–Fe) = 18.

2. Cobaltocene $\ce{Cp2Co}$ is a commonly used one-electron reducing agent, whereas ferrocene is very hard to reduce. Explain with the 18-electron rule and molecular orbitals.

   **Answer** Ferrocene has 18 electrons, with all bonding and nonbonding orbitals exactly filled; an additional electron would have to enter the high-energy **antibonding orbital** $e_{1g}^*$, so it is very hard to reduce and can only be oxidized (losing an electron from a nonbonding orbital to give the 17-electron $\ce{[Cp2Fe]+}$). Cobaltocene has 19 electrons, and the extra electron is already in the antibonding $e_{1g}^*$ orbital, high in energy and easily lost; losing it gives the 18-electron $\ce{[Cp2Co]+}$, isoelectronic with ferrocene, so cobaltocene is a strong reducing agent.

3. How does an experiment with ¹³CO labeling prove that the "CO insertion" of $\ce{CH3Mn(CO)5}$ is actually methyl migration? Write the product distributions predicted by the two mechanisms for decarbonylation of cis-$\ce{CH3C(O)Mn(CO)4(^{13}CO)}$.

   **Answer** By microscopic reversibility it suffices to study decarbonylation (the reverse reaction). Let ¹³CO be at one position cis to the acyl group. Decarbonylation first creates a vacancy by loss of one CO cis to the acyl group (the probability that exactly the ¹³CO is lost is 1/4). If the mechanism is CO "deinsertion", the CO of the acyl group returns to its original place, the methyl does not move, and the CO on the vacancy is the CO of the acyl group, so the methyl position is unchanged: the product is 1/4 unlabeled, 3/4 with methyl cis to ¹³CO, and none trans. If the methyl migrates, it moves from the acyl carbon to whichever of the four cis positions has just been vacated: when the vacancy is adjacent to the ¹³CO (2/4), the product is cis, when it is opposite the ¹³CO (1/4), trans, and when the vacancy is the original position of the ¹³CO (1/4), the product is unlabeled. The experiment gives cis and trans products in a ratio of about 2 : 1 together with unlabeled product, consistent with the prediction for methyl migration; CO deinsertion cannot give trans product.

4. Oct-1-ene, oct-2-ene and oct-4-ene each react with Schwartz's reagent $\ce{Cp2Zr(H)Cl}$ and are then treated with $\ce{Br2}$, and all give 1-bromooctane. Explain this result.

   **Answer** 1,2-Insertion of an alkene into Zr–H is reversible. After insertion of an internal alkene a secondary alkylzirconium forms, which can undergo β-hydride elimination to give the alkene complex of another position and Zr–H, and insert again in the other direction; repeated cycles make zirconium "walk" along the carbon chain. The $\ce{Cp2ZrCl}$ fragment is bulky, and a primary alkyl is much more stable than a secondary alkyl (steric hindrance), so the equilibrium finally shifts completely to the terminal primary alkylzirconium $\ce{Cp2Zr(Cl)(CH2)7CH3}$. The Zr–C bond is cleaved by $\ce{Br2}$ with retention of configuration at carbon, giving 1-bromooctane. All three alkenes give the same product.

5. The cation $\ce{[CpRe(CO)2(NO)]+}$ reacts with $\ce{NaBH4}$ to give the formyl complex $\ce{CpRe(CO)(NO)(CHO)}$. Why does hydride attack the carbon of CO rather than rhenium?

   **Answer** Counting: Cp 5 + Re 7 + 2 × 2 (CO) + 3 (linear NO) − 1 (positive charge) = 18 electrons, so the complex is coordinatively saturated, and the metal has no empty orbital to accept the electron pair of $\ce{H-}$ (otherwise it would have 20 electrons). The positive charge and the strong π acceptors NO and CO make the metal electron-poor and weaken back-donation, so the carbon of the coordinated CO carries a larger partial positive charge, and $\ce{H-}$ attacks the carbonyl carbon as a **nucleophile** (**nucleophilic addition** to a ligand), the electron pair moving to oxygen, finally giving a neutral 18-electron formyl complex. Conversely, an electron-rich 18-electron metal can react with $\ce{H+}$, because protonation does not increase the valence electron count.

6. Which of the following alkyl complexes can exist stably at room temperature? Explain: (a) $\ce{Ti(CH2CH2CH3)4}$; (b) $\ce{Ti(CH2Ph)4}$; (c) $\ce{CpFe(CO)2CH2CH3}$; (d) tetrakis(1-norbornyl)cobalt.

   **Answer** (a) Unstable: it has β-H, and Ti(IV) has only 8 electrons and many vacant sites, so β-hydride elimination is fast. (b) Stable: benzyl has no β-H (the β position is an aromatic ring carbon carrying no eliminable H). (c) Fairly stable: although it has β-H, the metal has 18 electrons and no vacant site, Cp and CO are tightly bound, and a CO must dissociate (requiring heat or light) before β-hydride elimination can occur. (d) Stable: β-hydride elimination would give a bridgehead alkene violating Bredt's rule, an unstable product, and the β-H can hardly become coplanar with Co.

7. The Tebbe reagent (the source of $\ce{Cp2Ti=CH2}$) and the phosphorus ylide $\ce{Ph3P=CH2}$ can both convert a carbonyl group into a methylene group. Compare their bonding and scope.

   **Answer** In both, the methylene carbon carries a partial negative charge and is nucleophilic, both react with the carbonyl group through a four-membered ring intermediate (an oxatitanacyclobutane or an oxaphosphetane) to give the alkene, driven by the strong Ti=O and P=O bonds, respectively. The differences: $\ce{Cp2Ti=CH2}$ is a Schrock carbene, Ti(IV) is a $\mathrm{d}^0$, highly oxophilic **Lewis acid**, and Ti=C is a genuine covalent σ + π double bond; the P=C "double bond" of a phosphorus ylide is really a $\ce{P+-C-}$ inner salt and strongly basic. The Tebbe reagent can therefore methylenate esters, lactones and amides (giving enol ethers and **enamines**), which phosphorus ylides do not react with, and it is only weakly basic, so it does not cause enolization or **epimerization** of easily enolized ketones; phosphorus ylides react essentially only with aldehydes and ketones.

8. Why can stable β-agostic bonds often be observed in $\mathrm{d}^0$ Ti(IV) and Zr(IV) alkyl complexes, whereas Pd(II) undergoes β-hydride elimination rapidly?

   **Answer** A β-agostic structure is a state on the way to β-hydride elimination; completing elimination requires forming an alkene–hydride complex, and stabilizing such a complex depends on back-donation from the metal into the alkene π* (the DCD model). A $\mathrm{d}^0$ metal has no d electrons, cannot back-donate, and forms only a very weak alkene complex, so β-hydride elimination is thermodynamically unfavorable and the C–H bond stays in the agostic state, donating electrons but not breaking. Pd(II) ($\mathrm{d}^8$), with d electrons, can back-donate, the alkene complex is stable, and elimination is fast. For the same reason, in Ziegler–Natta and metallocene polymerization, the $\mathrm{d}^0$ Ti and Zr centers allow the chain to grow many times without premature β-hydride elimination (chain transfer).
