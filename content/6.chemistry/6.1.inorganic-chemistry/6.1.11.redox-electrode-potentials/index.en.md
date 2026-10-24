---
title: Redox Reactions and Electrode Potentials
source_hash: 292ace7871d8
---

The acid–base, complexation, and precipitation reactions of the preceding chapters are all recombinations of ions or protons, and the charge state of each element is unchanged by the reaction. Another large class of reactions involves the transfer of electrons from one substance to another: redox reactions. Combustion, the smelting and corrosion of metals, photosynthesis and respiration, batteries and electrolysis are all redox reactions. In this chapter we first use oxidation numbers to describe electron transfer and to balance equations (11.1, 11.2). We then let the oxidizing and reducing agents react at two separate electrodes, so that electron transfer becomes a current in an external circuit; this is the galvanic cell (11.3). The electromotive force of a galvanic cell can be measured precisely, and this gives the standard electrode potential, a measure of the oxidizing or reducing power of a redox couple (11.4). Its relation to the **Gibbs energy** of [6.1.6](/6.1.6) is $\Delta_{\mathrm{r}}G_{\mathrm{m}} = -zFE_{\mathrm{cell}}$, and translating the **reaction isotherm** of [6.1.8](/6.1.8) into electrical language gives the Nernst equation, treated in 11.5, which treats in a unified way the effects of concentration, acidity, precipitation, and complexation on the electrode potential. Applications of electrode potentials, Latimer diagrams, electrolysis, and electrochemical power sources are found in [6.1.12](/6.1.12). Cell thermodynamics, the rigorous form of activities and the Nernst equation, and the kinetics of electrode processes are found in [Physical Chemistry](/6.3); potentiometric analysis and redox titration are found in [Analytical Chemistry](/6.4).

## 11.1. Redox Reactions

### 11.1.1. Oxidation and Reduction

Chemical reactions can be divided into two classes according to whether electrons are transferred. In $\ce{Zn + Cu^2+ -> Zn^2+ + Cu}$ a zinc atom loses two electrons and a copper ion gains two, whereas in $\ce{HCl + NaOH -> NaCl + H2O}$ the charge state of every element is unchanged.

**Definition 11.1.1 (Redox Reaction)** The process in which a substance loses electrons is called **oxidation**, and the process in which it gains electrons is called **reduction**. A reaction in which electrons are transferred (or in which the oxidation numbers of elements change, Definition 11.1.2) is called a **redox reaction**; a reaction without electron transfer is called a non-redox reaction.

In reactions that form covalent compounds, such as $\ce{C + O2 -> CO2}$, electrons are not transferred completely; the shared electron pairs are merely displaced toward the oxygen atoms. To treat ionic and covalent reactions in the same way, the oxidation number is introduced.

**Definition 11.1.2 (Oxidation Number)** The formal charge of an atom obtained by assigning all the bonding electrons in a compound to the more **electronegative** atom ([6.1.2](/6.1.2)) is called the **oxidation number** of that atom in the compound.

The IUPAC (2016) definition of oxidation state is consistent with this: it is the charge an atom would have after the bonding electrons of each bond are assigned entirely to the more electronegative partner under the "ionic approximation" (bonds between atoms of the same element are divided equally). The rules for assigning oxidation numbers are:

1. The oxidation number of an element in its elemental form is zero.
2. Oxygen is $-2$ in ordinary oxides, $-1$ in peroxides (such as $\ce{H2O2}$ and $\ce{Na2O2}$), $-\tfrac{1}{2}$ in superoxides (such as $\ce{KO2}$), and $+2$ in $\ce{OF2}$.
3. Hydrogen is $+1$ in ordinary compounds and $-1$ in hydrides of reactive metals (such as $\ce{NaH}$ and $\ce{CaH2}$).
4. The algebraic sum of the oxidation numbers in a neutral molecule is zero; in a polyatomic ion it equals the charge of the ion.

| Substance | Oxidation number | Remark |
|---|---|---|
| $\ce{K2Cr2O7}$ | Cr: $+6$ | $2(+1) + 2x + 7(-2) = 0$ |
| $\ce{KO2}$ | O: $-\tfrac{1}{2}$ | superoxide ion $\ce{O2^-}$ |
| $\ce{Fe3O4}$ | Fe: $+\tfrac{8}{3}$ | average oxidation number; actually $\ce{FeO*Fe2O3}$, containing one Fe(II) and two Fe(III) |
| $\ce{Na2S2O3}$ | S: $+2$ | average oxidation number; structurally the central S is $+6$ and the terminal S is $-2$ |

Oxidation numbers can thus be positive, negative, or fractional. Fractional values occur only in average oxidation numbers obtained from the rules; each atom in the structure still has an integer oxidation number. The oxidation number is a bookkeeping device and is not the real charge of the atom: the real charge on Cr in $\ce{K2Cr2O7}$ is far smaller than $+6$.

### 11.1.2. Oxidizing and Reducing Agents

**Definition 11.1.3 (Oxidizing and Reducing Agents)** In a redox reaction, the substance containing an element whose oxidation number decreases is called the **oxidizing agent**; it causes another substance to be oxidized and is itself reduced, and its product is called the reduction product. The substance containing an element whose oxidation number increases is called the **reducing agent**; it causes another substance to be reduced and is itself oxidized, and its product is called the oxidation product.

For example, in

$$
\ce{NaClO + 2FeSO4 + H2SO4 -> NaCl + Fe2(SO4)3 + H2O}
$$
$\ce{NaClO}$ (Cl: $+1 \to -1$) is the oxidizing agent and $\ce{NaCl}$ is the reduction product; $\ce{FeSO4}$ (Fe: $+2 \to +3$) is the reducing agent and $\ce{Fe2(SO4)3}$ is the oxidation product; $\ce{H2SO4}$ merely provides the acidic medium, and the oxidation numbers of its elements do not change.

When an element has several oxidation numbers, substances in which it has a high oxidation number generally act as oxidizing agents, those with a low oxidation number generally act as reducing agents, and those with an intermediate oxidation number can act as either. An example is $\ce{SO2}$ (S: $+4$):

$$
\ce{SO2 + 2H2S -> 3S + 2H2O}, \qquad \ce{Cl2 + SO2 + 2H2O -> H2SO4 + 2HCl}.
$$
$\ce{SO2}$ is the oxidizing agent in the first reaction and the reducing agent in the second. The same is true of $\ce{H2O2}$ (O: $-1$):

$$
\ce{H2O2 + 2FeCl2 + 2HCl -> 2FeCl3 + 2H2O}, \qquad \ce{5H2O2 + 2KMnO4 + 3H2SO4 -> 2MnSO4 + K2SO4 + 5O2 + 8H2O}.
$$
In the former $\ce{H2O2}$ is reduced to $\ce{H2O}$; in the latter it is oxidized to $\ce{O2}$ by the strong oxidizing agent $\ce{KMnO4}$. Whether a substance is an oxidizing or reducing agent is thus relative and depends on its reaction partner.

### 11.1.3. Disproportionation and Comproportionation

**Definition 11.1.4 (Disproportionation)** A reaction in which, within the same substance, the oxidation number of some atoms of an element in a given oxidation state increases while that of others decreases is called a **disproportionation** reaction.

| Type | Examples |
|---|---|
| Disproportionation of elements | $\ce{Cl2 + H2O <=> HClO + HCl}$; $\ce{X2 + 2OH- -> X- + XO- + H2O}$ (X = Cl, Br, I; cold dilute base); $\ce{3S + 6OH- -> 2S^2- + SO3^2- + 3H2O}$; $\ce{P4 + 3OH- + 3H2O -> PH3 + 3H2PO2-}$ |
| Disproportionation of oxoanions | $\ce{4ClO3- ->[\Delta] 3ClO4- + Cl-}$; $\ce{3ClO- -> ClO3- + 2Cl-}$; $\ce{3MnO4^2- + 2H2O -> MnO2 + 2MnO4- + 4OH-}$ |
| Disproportionation of oxoacids | $\ce{3HXO -> HXO3 + 2HX}$ (X = Cl, Br, I); $\ce{2HNO2 -> NO + NO2 + H2O}$ |

The reaction of white phosphorus with concentrated base, written in terms of formulas, is $\ce{P4 + 3NaOH + 3H2O -> PH3 + 3NaH2PO2}$; the product is sodium hypophosphite (P: $+1$), not sodium dihydrogen phosphate. The disproportionating element is in an intermediate oxidation state, so an element that can disproportionate has at least three oxidation states. Whether disproportionation can occur is judged from the Latimer diagram of [6.1.12](/6.1.12).

**Definition 11.1.5 (Comproportionation)** A reaction in which the higher and lower oxidation states of the same element react with each other to give an intermediate oxidation state is called **comproportionation**; it is the reverse of disproportionation.

An example is $\ce{SO2 + 2H2S -> 3S + 2H2O}$ (S: $+4$ and $-2 \to 0$). The thermal decomposition of $\ce{NH4NO3}$ is also a comproportionation of N:

$$
\ce{2NH4NO3 -> 2N2 + O2 + 4H2O}\ (\text{above } 300\,^\circ\mathrm{C}), \qquad \ce{5NH4NO3 -> 4N2 + 2HNO3 + 9H2O}.
$$
The reducing agent is the N in $\ce{NH4+}$ ($-3$) and the oxidizing agent is the N in $\ce{NO3-}$ ($+5$); they are not in the same oxidation state, so this is not a disproportionation. In the first reaction O is also partly oxidized ($-2 \to 0$).

### 11.1.4. Redox Couples and Half-Reactions

The product of the reduction of an oxidizing agent is reducing, and the product of the oxidation of a reducing agent is oxidizing. This is completely analogous to the relation of a **conjugate acid–base pair** ([6.1.9](/6.1.9)): acid–base reactions transfer protons, and redox reactions transfer electrons.

**Definition 11.1.6 (Redox Couple)** The oxidized form and the corresponding reduced form of the same element constitute a **redox couple**, written "oxidized form/reduced form", such as $\ce{Cu^2+}/\ce{Cu}$, $\ce{Zn^2+}/\ce{Zn}$, and $\ce{MnO4-}/\ce{Mn^2+}$.

The reaction $\ce{Zn + Cu^2+ -> Zn^2+ + Cu}$ involves two couples: $\ce{Cu^2+}$ (oxidizing agent 1)/$\ce{Cu}$ (reducing agent 1) and $\ce{Zn^2+}$ (oxidizing agent 2)/$\ce{Zn}$ (reducing agent 2). Within a couple, the stronger the oxidizing power of the oxidized form, the weaker the reducing power of its conjugate reduced form, and vice versa: $\ce{MnO4-}/\ce{Mn^2+}$ is a strong oxidizing agent paired with a weak reducing agent, and $\ce{Sn^4+}/\ce{Sn^2+}$ is a weak oxidizing agent paired with a strong reducing agent. A redox reaction always proceeds from the stronger oxidizing agent and stronger reducing agent to the weaker reducing agent and weaker oxidizing agent; the quantitative scale of "strong" and "weak" is the electrode potential of 11.4.

**Definition 11.1.7 (Half-Reaction)** The equation that expresses the interconversion of the oxidized and reduced forms within a couple is called a **half-reaction**, and by convention it is written in the reduction direction: oxidized form $+\, z\ce{e-} \ce{<=>}$ reduced form.

For example,

$$
\ce{Cu^2+ + 2e- <=> Cu}, \qquad \ce{MnO4- + 8H+ + 5e- <=> Mn^2+ + 4H2O}, \qquad \ce{SO4^2- + 2H+ + 2e- <=> SO3^2- + H2O}.
$$
In the last two half-reactions, $\ce{H+}$ and $\ce{H2O}$ are also part of the couple, and their concentrations affect its oxidizing and reducing power (11.5.3). Any redox reaction can be regarded as the difference of two half-reactions: $\ce{Zn + Cu^2+ -> Zn^2+ + Cu}$ = $(\ce{Cu^2+ + 2e- -> Cu}) - (\ce{Zn^2+ + 2e- -> Zn})$.

## 11.2. Balancing Redox Equations

Balancing a redox equation requires two conditions to be satisfied simultaneously: the number of electrons gained by the oxidizing agent equals the number lost by the reducing agent (equivalently, the total decrease in oxidation number equals the total increase), and the number of atoms of each element, and for ionic equations the charge, is the same on both sides.

### 11.2.1. The Oxidation Number Method

Take the oxidation of concentrated hydrochloric acid by $\ce{KMnO4}$ as an example:

1. Write the reactants and the main products: $\ce{KMnO4 + HCl -> MnCl2 + Cl2}$.
2. Mark the changes in oxidation number: Mn decreases from $+7$ to $+2$ (a decrease of 5); Cl increases from $-1$ to $0$, an increase of 2 for each $\ce{Cl2}$ formed.
3. Equalize the increases and decreases using the least common multiple 10: $\ce{2KMnO4 + 10HCl -> 2MnCl2 + 5Cl2}$.
4. Balance the atoms whose oxidation numbers do not change: K goes to $\ce{KCl}$, then add the $\ce{HCl}$ taking part as an acid, and finally determine $\ce{H2O}$ from the numbers of H and O:

$$
\ce{2KMnO4 + 16HCl -> 2KCl + 2MnCl2 + 5Cl2 + 8H2O}.
$$

The difficulty usually lies in the last step, balancing the atoms whose oxidation numbers do not change, especially H and O. In aqueous solution, $\ce{H+}$, $\ce{OH-}$, or $\ce{H2O}$ is added according to the medium:

| Medium | Side with excess O | Side with deficient O |
|---|---|---|
| Acidic | add $\ce{H+}$; the excess O forms $\ce{H2O}$ | add $\ce{H2O}$; this forms $\ce{H+}$ |
| Basic | add $\ce{H2O}$; the excess O forms $\ce{OH-}$ | add $\ce{OH-}$; this forms $\ce{H2O}$ |
| Neutral | add $\ce{H2O}$; this forms $\ce{OH-}$ | add $\ce{H2O}$; this forms $\ce{H+}$ |

$\ce{OH-}$ should not appear in an acidic medium, nor $\ce{H+}$ in a basic medium.

**Example 11.2.1** The products of the reaction of $\ce{KMnO4}$ with $\ce{K2SO3}$ differ in different media (Mn is reduced to $+2$, $+6$, and $+4$, respectively). Balance each reaction.

**Solution** In every case S increases from $+4$ to $+6$ (an increase of 2).

- Acidic (product $\ce{Mn^2+}$, Mn decreases by 5): $\ce{2KMnO4 + 5K2SO3 + H2SO4 -> 2MnSO4 + K2SO4}$; first balance K (12 on the left, so $\ce{K2SO4}$ on the right must be 6), then $\ce{SO4^2-}$ (8 on the right, so three $\ce{H2SO4}$ are needed on the left), and finally add $\ce{H2O}$:

$$
\ce{2KMnO4 + 5K2SO3 + 3H2SO4 -> 2MnSO4 + 6K2SO4 + 3H2O}.
$$

- Basic (product $\ce{MnO4^2-}$, Mn decreases by 1):

$$
\ce{2KMnO4 + K2SO3 + 2KOH -> 2K2MnO4 + K2SO4 + H2O}.
$$

- Neutral (product $\ce{MnO2}$, Mn decreases by 3):

$$
\ce{2KMnO4 + 3K2SO3 + H2O -> 2MnO2 + 3K2SO4 + 2KOH}.
$$

The advantage of the oxidation number method is that it is not restricted to aqueous solutions and also applies to nonaqueous systems, high-temperature reactions, and solid-state reactions.

### 11.2.2. The Ion–Electron Method

**Definition 11.2.1 (Ion–Electron Method)** The balancing method in which a redox reaction is split into an oxidation half-reaction and a reduction half-reaction, each is balanced for atoms and charge, and the two are then added with equal numbers of electrons gained and lost, so that the electrons cancel, is called the **ion–electron method** (half-reaction method).

Take the oxidation of $\ce{Cl-}$ by $\ce{MnO4-}$ in acidic solution as an example:

1. Write the reactants and products in ionic form: $\ce{MnO4- + Cl- -> Mn^2+ + Cl2}$.
2. Split into two half-reactions: $\ce{MnO4- -> Mn^2+}$ and $\ce{Cl- -> Cl2}$.
3. Balance the atoms of each, then add electrons to balance charge. In acidic medium $\ce{MnO4-}$ has four extra O, and adding $8\ce{H+}$ produces $4\ce{H2O}$:

$$
\ce{MnO4- + 8H+ + 5e- -> Mn^2+ + 4H2O} \quad (\times 2), \qquad \ce{2Cl- -> Cl2 + 2e-} \quad (\times 5).
$$

4. Add them using the least common multiple 10 of the numbers of electrons gained and lost:

$$
\ce{2MnO4- + 10Cl- + 16H+ -> 2Mn^2+ + 5Cl2 + 8H2O}.
$$

**Example 11.2.2** Balance: (1) $\ce{MnO4- + SO3^2- -> Mn^2+ + SO4^2-}$ in acidic medium; (2) $\ce{ClO- + Cr(OH)4- -> Cl- + CrO4^2-}$ in basic medium; (3) the oxidation of propanol $\ce{C3H7OH}$ to propanoic acid $\ce{C2H5COOH}$ by $\ce{MnO4-}$ in acidic medium.

**Solution** (1) $\ce{MnO4- + 8H+ + 5e- -> Mn^2+ + 4H2O}$ ($\times 2$) and $\ce{SO3^2- + H2O -> SO4^2- + 2H+ + 2e-}$ ($\times 5$); adding and canceling $\ce{H+}$ and $\ce{H2O}$ on both sides gives

$$
\ce{2MnO4- + 5SO3^2- + 6H+ -> 2Mn^2+ + 5SO4^2- + 3H2O}.
$$

(2) In basic medium, $\ce{OH-}$ is added on the side deficient in O: $\ce{ClO- + H2O + 2e- -> Cl- + 2OH-}$ ($\times 3$) and $\ce{Cr(OH)4- + 4OH- -> CrO4^2- + 4H2O + 3e-}$ ($\times 2$); adding gives

$$
\ce{3ClO- + 2Cr(OH)4- + 2OH- -> 3Cl- + 2CrO4^2- + 5H2O}.
$$
Checking the charge: left side $-3 - 2 - 2 = -7$, right side $-3 - 4 = -7$.

(3) For half-reactions of organic compounds we need not find the oxidation number of carbon; we balance atoms and charge directly: $\ce{C3H7OH + H2O -> C2H5COOH + 4H+ + 4e-}$ ($\times 5$) and $\ce{MnO4- + 8H+ + 5e- -> Mn^2+ + 4H2O}$ ($\times 4$), giving

$$
\ce{4MnO4- + 5C3H7OH + 12H+ -> 4Mn^2+ + 5C2H5COOH + 11H2O}. \qquad \square
$$

The ion–electron method does not require the oxidation number of each atom and is particularly suited to ionic reactions in aqueous solution; the half-reactions it produces are exactly the reactions that actually occur at the electrodes in 11.4.

### 11.2.3. Balancing and Systems of Linear Equations

Balancing is essentially finding a positive integer solution of a homogeneous system of linear equations. Suppose the reaction involves $n$ species, with the coefficients of the products taken as negative and the coefficient of the $j$th species denoted $\nu_j$ (the **stoichiometric number**, [6.1.6](/6.1.6)). Conservation of each element and of charge each gives an equation $\sum_j a_{ij}\nu_j = 0$, where $a_{ij}$ is the number of atoms of the $i$th element (or the charge) in the $j$th species. The coefficient vector $\boldsymbol{\nu}$ therefore belongs to the **null space** ([2.1.3](/2.1.3)) of the matrix $A = (a_{ij})$. When the null space is one-dimensional, the balanced equation is unique (up to a multiple), and it suffices to take the smallest positive integer vector in it:

```python
from fractions import Fraction
from math import lcm

import numpy as np
from scipy.linalg import null_space

# Columns: MnO4-, Cl-, H+, Mn2+, Cl2, H2O (products enter with a minus sign)
# Rows: Mn, O, H, Cl, charge
A = np.array([
    [1, 0, 0, -1, 0, 0],
    [4, 0, 0, 0, 0, -1],
    [0, 0, 1, 0, 0, -2],
    [0, 1, 0, 0, -2, 0],
    [-1, -1, 1, -2, 0, 0],
])
N = null_space(A)
print(N.shape[1])                                   # dimension of the null space: 1
v = N[:, 0] / N[0, 0]                               # scale so that MnO4- has coefficient 1
fr = [Fraction(x).limit_denominator(100) for x in v]
m = lcm(*(f.denominator for f in fr))
print([int(f * m) for f in fr])                     # smallest integer coefficients
```

```text
1
[2, 10, 16, 2, 5, 8]
```

That is, $\ce{2MnO4- + 10Cl- + 16H+ -> 2Mn^2+ + 5Cl2 + 8H2O}$. When the dimension of the null space exceeds 1, conservation of atoms alone cannot determine the equation. For example, the six species $\ce{MnO4-}$, $\ce{H2O2}$, $\ce{H+}$, $\ce{Mn^2+}$, $\ce{O2}$, and $\ce{H2O}$ have only four conservation equations (Mn, O, H, charge), and the null space is two-dimensional: $\ce{2MnO4- + 5H2O2 + 6H+ -> 2Mn^2+ + 5O2 + 8H2O}$ plus any multiple of $\ce{2H2O2 -> 2H2O + O2}$ is also "balanced". What fixes the actual coefficients is chemical information: all the $\ce{O2}$ comes from the oxidation of $\ce{H2O2}$, so the electron gain and loss must balance between $\ce{MnO4-}$ and $\ce{H2O2}$ (5 : 2). The half-reaction method includes this information automatically.

## 11.3. Galvanic Cells

### 11.3.1. Galvanic Cells and Electrolytic Cells

When a zinc strip is placed directly in $\ce{CuSO4}$ solution, the zinc dissolves, copper deposits on its surface, and the temperature of the solution rises: oxidizing and reducing agents are in direct contact, electrons are transferred at random on the atomic scale, and all the chemical energy of the reaction becomes heat. If oxidation and reduction are made to occur in two separate places, the electrons can only flow in a directed way through an external circuit, and chemical energy is converted into electrical energy. The discipline that studies electrical phenomena in chemical reactions and the interconversion of electrical and chemical energy is called *electrochemistry*. The core of electrochemistry is the conversion between chemical energy and electrical work (a kind of **non-expansion work**, [6.1.6](/6.1.6)), which can go in two directions.

**Definition 11.3.1 (Galvanic Cell and Electrolytic Cell)** A device in which the oxidizing and reducing agents are not in direct contact and reduction and oxidation occur at two separate electrodes, so that chemical energy is converted into electrical energy, is called a **galvanic cell** (voltaic cell); a device in which an applied direct-current source forces oxidation and reduction to occur at the two electrodes, converting electrical energy into chemical energy, is called an **electrolytic cell**.

In a galvanic cell, the spontaneous reaction ($\Delta_{\mathrm{r}}G_{\mathrm{m}} < 0$) delivers electrical work to the surroundings; in an electrolytic cell, the surroundings do electrical work on the system and drive a reaction with $\Delta_{\mathrm{r}}G_{\mathrm{m}} > 0$ ([6.1.12](/6.1.12)).

In the Cu–Zn galvanic cell (Daniell cell), a zinc strip is immersed in $\ce{ZnSO4}$ solution and a copper strip in $\ce{CuSO4}$ solution; the two solutions are joined by a salt bridge, and the two electrodes are connected by wires through a galvanometer. When the circuit is closed, the galvanometer needle deflects, the zinc strip gradually dissolves, and copper deposits on the copper strip: zinc is more reactive than copper, loses electrons to become $\ce{Zn^2+}$ in solution, the electrons flow along the wire to the copper strip, and $\ce{Cu^2+}$ in solution gains electrons there and is deposited.

![Schematic of the Cu–Zn galvanic cell: electrons flow in the external circuit from the zinc electrode to the copper electrode; in the salt bridge, Cl⁻ moves toward the solution on the zinc side and K⁺ toward the solution on the copper side, keeping both solutions electrically neutral](./plots/daniell-cell.py)

As the reaction proceeds, $\ce{Zn^2+}$ increases in the solution on the zinc side, giving an excess of positive charge, while $\ce{Cu^2+}$ decreases on the copper side, leaving $\ce{SO4^2-}$ in relative excess. If this were not promptly neutralized, the electric field of the excess charge would prevent the reaction from continuing.

**Definition 11.3.2 (Salt Bridge)** A U-shaped tube that connects the two electrolyte solutions of a galvanic cell and contains a saturated solution of $\ce{KCl}$ (or $\ce{NH4NO3}$, $\ce{KNO3}$) gelled with agar is called a **salt bridge**.

The salt bridge has two functions: its anions and cations migrate into the solutions on either side, keeping them electrically neutral so that the electrode reactions can continue; and it reduces the liquid junction potential between the two solutions to a very small value (11.4.1). $\ce{KCl}$ or $\ce{NH4NO3}$ is chosen because their anions and cations have similar mobilities and do not react with the electrode materials ($\ce{KNO3}$ is used instead when the solution contains $\ce{Ag+}$).

### 11.3.2. Half-Cells, Electrode Reactions, and Cell Diagrams

**Definition 11.3.3 (Half-Cell)** A galvanic cell consists of two **half-cells**, each comprising a redox couple and a conducting electrode material (such as a $\ce{Zn}$ strip and $\ce{Zn^2+}$ solution); the half-reaction taking place in a half-cell is called the electrode reaction.

The electrode from which electrons flow out is called the negative electrode and the one into which they flow the positive electrode; in the external circuit electrons flow from the negative to the positive electrode, and current flows from the positive to the negative electrode. By the IUPAC definition, the electrode at which oxidation occurs is the *anode* and the electrode at which reduction occurs is the *cathode*. In a galvanic cell the negative electrode is the anode and the positive electrode is the cathode; in an electrolytic cell the opposite holds, and oxidation occurs at the anode, which is connected to the positive terminal of the power source ([6.1.12](/6.1.12)). The electrode reactions and cell reaction of the Cu–Zn galvanic cell are

$$
\begin{aligned}
&\text{negative electrode (anode, oxidation):} && \ce{Zn -> Zn^2+ + 2e-},\\
&\text{positive electrode (cathode, reduction):} && \ce{Cu^2+ + 2e- -> Cu},\\
&\text{cell reaction:} && \ce{Zn + Cu^2+ -> Zn^2+ + Cu}.
\end{aligned}
$$
The cell reaction is the positive-electrode reaction minus the negative-electrode reaction (both written as reductions). The positive electrode of a galvanic cell consists of the couple containing the oxidizing agent, and the negative electrode of the couple containing the reducing agent.

**Definition 11.3.4 (Cell Diagram)** The way of representing the composition of a galvanic cell by symbols is called the **cell diagram** (cell notation). By the IUPAC convention, the negative electrode, where oxidation occurs, is written on the left and the positive electrode, where reduction occurs, on the right; $|$ denotes a phase boundary, $\Vert$ denotes a salt bridge (a liquid–liquid junction with the liquid junction potential eliminated), and several substances in the same phase are separated by commas; concentrations are given for solutions, partial pressures for gases, and states for solids and liquids.

The cell diagram of the Cu–Zn galvanic cell is

$$
(-)\ \ce{Zn(s)} \mid \ce{ZnSO4}(c_1) \parallel \ce{CuSO4}(c_2) \mid \ce{Cu(s)}\ (+).
$$
The cell diagram corresponds one to one with the cell reaction: the reaction can be written from the diagram (oxidation on the left, reduction on the right), and vice versa.

Different oxidation states of the same element or ion, such as $\ce{Fe^3+}/\ce{Fe^2+}$, $\ce{Sn^4+}/\ce{Sn^2+}$, and $\ce{Cl2}/\ce{Cl-}$, can also form half-cells. The couple itself cannot conduct electricity, so an inert conductor that does not take part in the reaction, such as Pt or graphite, is used as the electrode, so that the reaction occurs at its surface and the wire is led out from it. For example, the cell corresponding to $\ce{2Fe^3+ + Cu -> 2Fe^2+ + Cu^2+}$ is

$$
(-)\ \ce{Cu(s)} \mid \ce{Cu^2+}(c_1) \parallel \ce{Fe^3+}(c_2), \ce{Fe^2+}(c_3) \mid \ce{Pt}\ (+).
$$

### 11.3.3. Types of Electrodes

| Type | Electrode reaction (reduction form) | Electrode notation | Remark |
|---|---|---|---|
| Metal–metal ion electrode | $\ce{Zn^2+ + 2e- <=> Zn}$ | $\ce{Zn(s)} \mid \ce{Zn^2+}$ | a metal immersed in a solution of its salt |
| Gas–ion electrode | $\ce{2H+ + 2e- <=> H2}$; $\ce{Cl2 + 2e- <=> 2Cl-}$ | $\ce{Pt} \mid \ce{H2(g)} \mid \ce{H+}$; $\ce{Pt} \mid \ce{Cl2(g)} \mid \ce{Cl-}$ | an inert electrode adsorbs the gas |
| Metal–sparingly soluble salt–anion electrode | $\ce{AgCl(s) + e- <=> Ag(s) + Cl-}$ | $\ce{Ag(s)} \mid \ce{AgCl(s)} \mid \ce{Cl-}$ | the metal surface is coated with its sparingly soluble salt (or oxide) and immersed in a solution containing the same anion |
| Redox electrode | $\ce{Fe^3+ + e- <=> Fe^2+}$; $\ce{Cr2O7^2- + 14H+ + 6e- <=> 2Cr^3+ + 7H2O}$ | $\ce{Pt} \mid \ce{Fe^3+}, \ce{Fe^2+}$; $\ce{Pt} \mid \ce{Cr2O7^2-}, \ce{Cr^3+}, \ce{H+}$ | an inert electrode immersed in a solution containing two oxidation states of the same element |

The electrode reactions of the $\ce{AgCl}/\ce{Ag}$ electrode and the $\ce{Ag+}/\ce{Ag}$ electrode are in essence both the interconversion of $\ce{Ag+}$ and $\ce{Ag}$; the difference is that the potential of the latter depends on $[\ce{Ag+}]$ in solution, whereas in the former $[\ce{Ag+}]$ is fixed by the dissolution equilibrium of $\ce{AgCl}$ and is therefore controlled by $[\ce{Cl-}]$ (11.5.4).

## 11.4. Electrode Potentials

### 11.4.1. The Electric Double Layer and the Origin of the Electrode Potential

In the Cu–Zn galvanic cell, why do electrons transfer from Zn to $\ce{Cu^2+}$ and not from Cu to $\ce{Zn^2+}$? Nernst (1889) gave a qualitative explanation using the picture of the electric double layer. When a metal is immersed in a solution of its salt, two opposing tendencies exist. Atoms at the metal surface may leave their electrons on the metal and enter the solution as ions ($\mathrm{M} \to \mathrm{M}^{n+} + n\,\mathrm{e}^-$); this tendency is greater the more reactive the metal and the more dilute the solution. Metal ions in solution may gain electrons from the metal surface and deposit ($\mathrm{M}^{n+} + n\,\mathrm{e}^- \to \mathrm{M}$); this tendency is greater the less reactive the metal and the more concentrated the solution. When the two reach equilibrium, if the tendency to dissolve prevails the metal is negatively charged and positive ions accumulate in the solution near its surface; otherwise the metal is positively charged.

**Definition 11.4.1 (Electric Double Layer)** The two layers of opposite charge on either side of the interface between a metal and a solution are called the **electric double layer**: on the metal side is the excess charge at the surface, and on the solution side are a compact layer in contact with the surface and a diffuse layer that gradually spreads out into the solution.

There is a **potential difference** across the double layer, which reflects the ability of the metal and its ions to gain and lose electrons: the metal side of a zinc electrode is more negative than that of a copper electrode. But the potential difference at a single metal–solution interface (the absolute electrode potential) cannot be measured: to measure it, a second wire must be inserted into the solution, which introduces a new metal–solution interface. Only the potential difference of a galvanic cell composed of two electrodes can be measured precisely, so the electrode potential can only be defined relative to a chosen reference electrode (11.4.2).

There are two other interfacial potential differences in a galvanic cell:

- Contact potential: the potential difference formed where two metals touch, because their **work functions** ([5.5.1](/5.5.1)) differ. In a measurement, leads of the same metal are used at both ends, and it can then be neglected.
- Liquid junction potential: see the definition below.

**Definition 11.4.2 (Liquid Junction Potential)** The potential difference formed on the two sides of the interface when two electrolyte solutions of different composition or concentration are in contact, because the ions diffuse at different rates, is called the **liquid junction potential** (diffusion potential).

For example, when an $\ce{HCl}$ solution is in contact with water, $\ce{H+}$ diffuses faster than $\ce{Cl-}$ and the water side of the interface becomes positively charged. Liquid junction potentials can reach tens of millivolts and are hard to calculate accurately. In a salt bridge, the high concentrations of $\ce{K+}$ and $\ce{Cl-}$ have similar mobilities and carry most of the ion transport at the two ends of the bridge, which reduces the liquid junction potential to below 1–2 mV, so it can usually be neglected.

When the current in the circuit tends to zero, the voltage drop across the internal resistance of the cell also tends to zero, and the potential difference measured between the two electrodes is the electromotive force of the galvanic cell. In IUPAC notation it is written

$$
E_{\mathrm{cell}} = E_+ - E_- = E_{\mathrm{right}} - E_{\mathrm{left}},
$$
where $E_+$ and $E_-$ are the electrode potentials of the positive and negative electrodes. $E_{\mathrm{cell}}$ is the **electromotive force** $\mathcal{E}$ of a source in [5.3.5](/5.3.5#def-5.4.2): the nonelectrostatic force that drives the charges in a galvanic cell comes from the chemical driving force of the two electrode reactions. In a cell diagram the positive electrode is written on the right, so $E_{\mathrm{cell}} = E_{\mathrm{right}} - E_{\mathrm{left}}$; if the cell as written gives $E_{\mathrm{cell}} < 0$, the actual positive and negative electrodes are the reverse of those written, and the reverse cell reaction is spontaneous.

### 11.4.2. The Standard Hydrogen Electrode and Standard Electrode Potentials

**Definition 11.4.3 (Standard Hydrogen Electrode)** The electrode $\ce{Pt} \mid \ce{H2}(p^\circ) \mid \ce{H+}(a = 1)$, formed by immersing a platinum plate coated with platinum black in an acid solution in which the activity of $\ce{H+}$ is 1 (approximately, $[\ce{H+}] = 1\,\mathrm{mol\,L^{-1}}$) and bubbling pure hydrogen at a partial pressure $p^\circ = 100\,\mathrm{kPa}$ over it, is called the **standard hydrogen electrode** (SHE); its electrode reaction is $\ce{2H+ + 2e- <=> H2}$. By convention the electrode potential of the standard hydrogen electrode is zero at every temperature: $E^\circ(\ce{H+}/\ce{H2}) = 0$.

Platinum black adsorbs hydrogen, so that the electron exchange between $\ce{H2}$ and $\ce{H+}$ rapidly reaches equilibrium at the platinum surface.

**Definition 11.4.4 (Electrode Potential)** The electromotive force of the galvanic cell composed of the standard hydrogen electrode as the negative electrode (left) and the electrode under study as the positive electrode (right) is called the **electrode potential** of the electrode under study, denoted $E(\text{ox}/\text{red})$. When all substances in the electrode are in their **standard states** ([6.1.6](/6.1.6): concentration $c^\circ = 1\,\mathrm{mol\,L^{-1}}$ for species in solution, partial pressure $p^\circ$ for gases, and pure substances for solids and liquids), its electrode potential is called the **standard electrode potential**, denoted $E^\circ$.

By this definition, an electrode potential always corresponds to the electrode reaction written in the reduction form (a "reduction potential"), and its sign is unambiguous: a negative electrode potential means that the electrode is actually the negative electrode when combined with the standard hydrogen electrode in a cell. Older textbooks use $\varphi$ for the electrode potential and $E$ for the electromotive force; this wiki follows IUPAC in using $E$ and $E_{\mathrm{cell}}$, and reserves $\varphi$ for the **electric potential** of an electrostatic field. Where the temperature is not stated, tabulated data refer to $298.15\,\mathrm{K}$.

**Example 11.4.1** At $298.15\,\mathrm{K}$ the electromotive force of the galvanic cell

$$
(-)\ \ce{Zn} \mid \ce{Zn^2+}(1\,\mathrm{mol\,L^{-1}}) \parallel \ce{H+}(1\,\mathrm{mol\,L^{-1}}) \mid \ce{H2}(p^\circ) \mid \ce{Pt}\ (+)
$$
is measured as $0.762\,\mathrm{V}$, with cell reaction $\ce{Zn + 2H+ -> Zn^2+ + H2}$. The electromotive force of $(-)\ \ce{Pt} \mid \ce{H2}(p^\circ) \mid \ce{H+}(1\,\mathrm{mol\,L^{-1}}) \parallel \ce{Cu^2+}(1\,\mathrm{mol\,L^{-1}}) \mid \ce{Cu}\ (+)$ is measured as $0.342\,\mathrm{V}$. Find $E^\circ(\ce{Zn^2+}/\ce{Zn})$, $E^\circ(\ce{Cu^2+}/\ce{Cu})$, and the standard electromotive force of the Cu–Zn galvanic cell.

**Solution** From $E^\circ_{\mathrm{cell}} = E^\circ_+ - E^\circ_-$: $0.762\,\mathrm{V} = 0 - E^\circ(\ce{Zn^2+}/\ce{Zn})$, so $E^\circ(\ce{Zn^2+}/\ce{Zn}) = -0.762\,\mathrm{V}$; and $0.342\,\mathrm{V} = E^\circ(\ce{Cu^2+}/\ce{Cu}) - 0$, so $E^\circ(\ce{Cu^2+}/\ce{Cu}) = +0.342\,\mathrm{V}$. $\ce{Zn}$ has a greater tendency to lose electrons than $\ce{H2}$, and $\ce{Cu}$ a smaller one. In the Cu–Zn galvanic cell the electrons must flow from Zn to Cu, and

$$
E^\circ_{\mathrm{cell}} = E^\circ(\ce{Cu^2+}/\ce{Cu}) - E^\circ(\ce{Zn^2+}/\ce{Zn}) = 0.342 - (-0.762) = 1.104\,\mathrm{V}. \qquad \square
$$

### 11.4.3. The Table of Standard Electrode Potentials

Arranging the standard electrode potentials of couples in order of magnitude gives the table of standard electrode potentials. The table below excerpts commonly used data ($298.15\,\mathrm{K}$, CRC Handbook):

| Couple | Electrode reaction | $E^\circ/\mathrm{V}$ |
|---|---|---|
| $\ce{Li+}/\ce{Li}$ | $\ce{Li+ + e- <=> Li}$ | $-3.040$ |
| $\ce{Na+}/\ce{Na}$ | $\ce{Na+ + e- <=> Na}$ | $-2.71$ |
| $\ce{Zn^2+}/\ce{Zn}$ | $\ce{Zn^2+ + 2e- <=> Zn}$ | $-0.762$ |
| $\ce{Fe^2+}/\ce{Fe}$ | $\ce{Fe^2+ + 2e- <=> Fe}$ | $-0.447$ |
| $\ce{Ni^2+}/\ce{Ni}$ | $\ce{Ni^2+ + 2e- <=> Ni}$ | $-0.257$ |
| $\ce{Sn^2+}/\ce{Sn}$ | $\ce{Sn^2+ + 2e- <=> Sn}$ | $-0.138$ |
| $\ce{Pb^2+}/\ce{Pb}$ | $\ce{Pb^2+ + 2e- <=> Pb}$ | $-0.126$ |
| $\ce{H+}/\ce{H2}$ | $\ce{2H+ + 2e- <=> H2}$ | $0$ |
| $\ce{AgCl}/\ce{Ag}$ | $\ce{AgCl + e- <=> Ag + Cl-}$ | $0.222$ |
| $\ce{Hg2Cl2}/\ce{Hg}$ | $\ce{Hg2Cl2 + 2e- <=> 2Hg + 2Cl-}$ | $0.268$ |
| $\ce{Cu^2+}/\ce{Cu}$ | $\ce{Cu^2+ + 2e- <=> Cu}$ | $0.342$ |
| $\ce{I2}/\ce{I-}$ | $\ce{I2 + 2e- <=> 2I-}$ | $0.536$ |
| $\ce{Fe^3+}/\ce{Fe^2+}$ | $\ce{Fe^3+ + e- <=> Fe^2+}$ | $0.771$ |
| $\ce{Ag+}/\ce{Ag}$ | $\ce{Ag+ + e- <=> Ag}$ | $0.800$ |
| $\ce{Br2}/\ce{Br-}$ | $\ce{Br2(l) + 2e- <=> 2Br-}$ | $1.066$ |
| $\ce{O2}/\ce{H2O}$ | $\ce{O2 + 4H+ + 4e- <=> 2H2O}$ | $1.229$ |
| $\ce{Cr2O7^2-}/\ce{Cr^3+}$ | $\ce{Cr2O7^2- + 14H+ + 6e- <=> 2Cr^3+ + 7H2O}$ | $1.36$ |
| $\ce{Cl2}/\ce{Cl-}$ | $\ce{Cl2 + 2e- <=> 2Cl-}$ | $1.358$ |
| $\ce{MnO4-}/\ce{Mn^2+}$ | $\ce{MnO4- + 8H+ + 5e- <=> Mn^2+ + 4H2O}$ | $1.507$ |
| $\ce{S2O8^2-}/\ce{SO4^2-}$ | $\ce{S2O8^2- + 2e- <=> 2SO4^2-}$ | $2.010$ |
| $\ce{F2}/\ce{F-}$ | $\ce{F2 + 2e- <=> 2F-}$ | $2.866$ |

Points to note in using the table:

1. Electrode reactions are always written in the reduction form: oxidized form $+\, z\ce{e-} \ce{<=>}$ reduced form.
2. The larger $E^\circ$ is, the stronger the oxidizing power of the oxidized form and the weaker the reducing power of the reduced form; the smaller $E^\circ$ is, the stronger the reducing power of the reduced form. The table is arranged in order of increasing $E^\circ$: the strongest reducing agent ($\ce{Li}$) is the reduced form of the couple at the top, and the strongest oxidizing agent ($\ce{F2}$) is the oxidized form of the couple at the bottom.
3. In principle any two electrodes in the table can form a galvanic cell, with the one of larger $E^\circ$ as the positive electrode. The positive-electrode reaction minus the negative-electrode reaction is the cell reaction: the oxidized form of the couple with larger $E^\circ$ can oxidize the reduced form of the couple with smaller $E^\circ$.
4. $E^\circ$ is an **intensive quantity**; it depends on the nature of the couple and is independent of the stoichiometric coefficients of the electrode reaction: $\ce{Cl2 + 2e- <=> 2Cl-}$ and $\ce{1/2Cl2 + e- <=> Cl-}$ both have $E^\circ = 1.358\,\mathrm{V}$. (By contrast, $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}$ and $K^\circ$ change with the stoichiometric coefficients; see 11.4.5 and [6.1.12](/6.1.12).)
5. The table is divided into an acidic table and a basic table. When $\ce{H+}$ appears in the electrode reaction, consult the acidic table ($[\ce{H+}] = 1\,\mathrm{mol\,L^{-1}}$); when $\ce{OH-}$ appears, consult the basic table ($[\ce{OH-}] = 1\,\mathrm{mol\,L^{-1}}$). When neither appears, decide according to the form in which the species exists: for example $\ce{Fe^3+}/\ce{Fe^2+}$ and $\ce{Zn^2+}/\ce{Zn}$ exist only in acidic solution and are found in the acidic table, whereas $\ce{ZnO2^2-}/\ce{Zn}$ exists only in basic solution and is found in the basic table.
6. The data in the table are standard values in aqueous solution at $298.15\,\mathrm{K}$. $E^\circ$ varies little with temperature (usually less than 1 mV per kelvin), so the values can be used directly around room temperature; they do not apply to nonaqueous solvents, high temperatures, or solid-state reactions.

### 11.4.4. Reference Electrodes

The standard hydrogen electrode requires pure hydrogen and strictly standard conditions and is inconvenient to use. In practical measurements, an electrode whose potential is stable and has been accurately determined against the standard hydrogen electrode serves as the reference.

**Definition 11.4.5 (Reference Electrode)** An electrode whose electrode potential is known, stable, and reproducible, and which is combined with the electrode under study to form a cell for determining the latter's electrode potential, is called a **reference electrode**.

**Definition 11.4.6 (Calomel Electrode)** The electrode $\ce{Pt} \mid \ce{Hg(l)} \mid \ce{Hg2Cl2(s)} \mid \ce{Cl-}(aq)$, formed by contacting a platinum wire successively with metallic mercury and a paste of calomel ($\ce{Hg2Cl2}$) and mercury, and immersing it in $\ce{KCl}$ solution, is called the **calomel electrode**; when the $\ce{KCl}$ solution is saturated it is called the saturated calomel electrode (SCE). The electrode reaction is $\ce{Hg2Cl2(s) + 2e- <=> 2Hg(l) + 2Cl-}$.

The potential of the calomel electrode depends only on $[\ce{Cl-}]$ (11.5.4). $E^\circ(\ce{Hg2Cl2}/\ce{Hg}) = 0.268\,\mathrm{V}$; in saturated $\ce{KCl}$, $[\ce{Cl-}]$ is fixed, and at $298.15\,\mathrm{K}$, $E(\text{SCE}) = 0.241\,\mathrm{V}$. Another commonly used reference electrode is $\ce{Ag} \mid \ce{AgCl(s)} \mid \ce{KCl}$ (saturated), with $E = 0.197\,\mathrm{V}$; it contains no mercury and is now more widely used. Potentials measured against a reference electrode can be converted to the standard hydrogen electrode scale: $E(\text{vs SHE}) = E(\text{vs SCE}) + 0.241\,\mathrm{V}$.

### 11.4.5. Cell Electromotive Force and Gibbs Energy

A galvanic cell converts chemical energy into electrical work, and the limit of the conversion is determined by thermodynamics. [6.1.6](/6.1.6#sec-6.4.7) showed that at constant temperature and pressure the change in the Gibbs energy of a system and the non-expansion work $W'$ done on the system by the surroundings satisfy $\Delta G \le W'$, with equality for a reversible process. In other words, the non-expansion work $-W'$ done by the system on its surroundings does not exceed $-\Delta G$.

Suppose that when the cell reaction advances by 1 mol of extent of reaction in the stoichiometric equation, $z$ mol of electrons pass through the external circuit ($z$ is the number of electrons transferred in the cell reaction, a dimensionless number). The charge of 1 mol of electrons is

$$
F = N_{\mathrm{A}}e = 6.022\,140\,76\times10^{23}\,\mathrm{mol^{-1}} \times 1.602\,176\,634\times10^{-19}\,\mathrm{C} = 96\,485.332\,12\,\mathrm{C\,mol^{-1}},
$$
the **Faraday constant**. Since 2019, when the International System of Units came to be defined by fixed constants, $N_{\mathrm{A}}$ and $e$ are exact values, so $F$ is also exact; in calculations we take $F = 96\,485\,\mathrm{C\,mol^{-1}}$.

When the cell operates with the current tending to zero, the process is reversible and the potential difference between the electrodes equals the electromotive force $E_{\mathrm{cell}}$. When a charge $zF$ passes through a potential difference $E_{\mathrm{cell}}$, the electrical work done by the system on the surroundings is $zFE_{\mathrm{cell}}$, that is, $W' = -zFE_{\mathrm{cell}}$. From $\Delta G = W'$ (reversible),

$$
\Delta_{\mathrm{r}}G_{\mathrm{m}} = -zFE_{\mathrm{cell}}. \tag{11.1}
$$
When all substances are in their standard states, $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = -zFE^\circ_{\mathrm{cell}}$. When a cell actually discharges, a current flows, the internal resistance generates heat, and the electrode reactions deviate from equilibrium, so the electrical work delivered is less than $zFE_{\mathrm{cell}}$, that is, $-W' < -\Delta_{\mathrm{r}}G_{\mathrm{m}}$, which is just the irreversible case $\Delta G < W'$.

Equation (11.1) translates the criterion for the direction of reaction into electrical language:

| $\Delta_{\mathrm{r}}G_{\mathrm{m}}$ | $E_{\mathrm{cell}}$ | Cell reaction as written in the cell diagram |
|---|---|---|
| $< 0$ | $> 0$ | forward direction spontaneous; the cell can do work on the surroundings as a galvanic cell |
| $= 0$ | $= 0$ | equilibrium |
| $> 0$ | $< 0$ | reverse direction spontaneous; an applied voltage is needed for the forward reaction (electrolysis) |

$\Delta_{\mathrm{r}}G_{\mathrm{m}}$ is extensive (it changes in proportion to the stoichiometric coefficients of the equation), and $z$ changes proportionally with it, while $E_{\mathrm{cell}} = -\Delta_{\mathrm{r}}G_{\mathrm{m}}/(zF)$ is the ratio of the two and is independent of how the equation is written. This is the reason for item 4 of 11.4.3. The electromotive force can be measured very precisely (to the order of $10^{-5}\,\mathrm{V}$), so electrochemical measurement is an accurate method of determining $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}$ and $K^\circ$; measuring the variation of $E_{\mathrm{cell}}$ with temperature also gives $\Delta_{\mathrm{r}}S_{\mathrm{m}} = zF(\partial E_{\mathrm{cell}}/\partial T)_p$ and $\Delta_{\mathrm{r}}H_{\mathrm{m}}$; this part of cell thermodynamics is found in [Physical Chemistry](/6.3).

**Example 11.4.2** Find $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}$ for the Cu–Zn galvanic cell reaction at $298.15\,\mathrm{K}$.

**Solution** For $\ce{Zn + Cu^2+ -> Zn^2+ + Cu}$, $z = 2$, and from Example 11.4.1, $E^\circ_{\mathrm{cell}} = 1.104\,\mathrm{V}$, so

$$
\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = -2 \times 96\,485\,\mathrm{C\,mol^{-1}} \times 1.104\,\mathrm{V} = -2.13\times10^5\,\mathrm{J\,mol^{-1}} = -213\,\mathrm{kJ\,mol^{-1}}.
$$
Calculating from the **standard molar Gibbs energy of formation**, $\Delta_{\mathrm{f}}G^\circ(\ce{Zn^2+}) = -147.1$ and $\Delta_{\mathrm{f}}G^\circ(\ce{Cu^2+}) = 65.5\,\mathrm{kJ\,mol^{-1}}$, with elements at zero, gives $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = -147.1 - 65.5 = -212.6\,\mathrm{kJ\,mol^{-1}}$, in agreement. $\square$

**Example 11.4.3** The cell reaction of the zinc–mercuric oxide cell is $\ce{Zn(s) + HgO(s) -> ZnO(s) + Hg(l)}$. From $\Delta_{\mathrm{f}}G^\circ(\ce{HgO}, \text{red}) = -58.5\,\mathrm{kJ\,mol^{-1}}$ and $\Delta_{\mathrm{f}}G^\circ(\ce{ZnO}) = -320.5\,\mathrm{kJ\,mol^{-1}}$, find the standard electromotive force of the cell at $298.15\,\mathrm{K}$.

**Solution** $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = -320.5 - (-58.5) = -262.0\,\mathrm{kJ\,mol^{-1}}$. Zn rises from 0 to $+2$, so $z = 2$ and

$$
E^\circ_{\mathrm{cell}} = -\frac{\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}}{zF} = \frac{262.0\times10^3}{2 \times 96\,485}\,\mathrm{V} = 1.358\,\mathrm{V}.
$$
The voltage of an actual zinc–mercuric oxide cell is about $1.35\,\mathrm{V}$ and is almost constant during discharge: reactants and products are all pure solids or liquids, so $Q = 1$ and the electromotive force does not change with the depth of discharge (see 11.5.1). Such cells have been phased out because they contain mercury. $\square$

Similarly, for $\ce{H2(g) + 1/2O2(g) -> H2O(l)}$ in [6.1.6](/6.1.6#sec-6.4.7), $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = -237.1\,\mathrm{kJ\,mol^{-1}}$ and $z = 2$, which corresponds to $E^\circ_{\mathrm{cell}} = 237.1\times10^3/(2\times96\,485)\,\mathrm{V} = 1.229\,\mathrm{V}$, exactly the value of $E^\circ(\ce{O2}/\ce{H2O})$ in the table.

## 11.5. Factors Affecting the Electrode Potential: The Nernst Equation

### 11.5.1. The Nernst Equation

Besides depending on the nature of the couple, the electrode potential also depends on the concentrations of the species in solution, on gas partial pressures, and on temperature. This relation can be derived directly from thermodynamics.

**Theorem 11.5.1 (Nernst Equation)** At temperature $T$, the electromotive force of a cell reaction is related to the concentrations (partial pressures) of the species by

$$
E_{\mathrm{cell}} = E^\circ_{\mathrm{cell}} - \frac{RT}{zF}\ln Q, \tag{11.2}
$$
where $Q$ is the **reaction quotient** of the cell reaction. For an electrode reaction oxidized form $+\, z\ce{e-} \ce{<=>}$ reduced form,

$$
E = E^\circ + \frac{RT}{zF}\ln\frac{[\text{ox}]}{[\text{red}]} = E^\circ + \frac{0.05916\,\mathrm{V}}{z}\lg\frac{[\text{ox}]}{[\text{red}]} \quad (298.15\,\mathrm{K}). \tag{11.3}
$$

**Proof** By the **reaction isotherm** (Eq. (8.2)), $\Delta_{\mathrm{r}}G_{\mathrm{m}} = \Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} + RT\ln Q$. Substituting Eq. (11.1) and $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = -zFE^\circ_{\mathrm{cell}}$ gives $-zFE_{\mathrm{cell}} = -zFE^\circ_{\mathrm{cell}} + RT\ln Q$, and dividing both sides by $-zF$ gives Eq. (11.2).

The electrode potential is the electromotive force of a cell with the standard hydrogen electrode as the negative electrode. The reaction of this cell is oxidized form $+\, \tfrac{z}{2}\ce{H2} \to$ reduced form $+\, z\ce{H+}$, and in the standard hydrogen electrode $[\ce{H+}] = 1$ and $p_{\ce{H2}}/p^\circ = 1$, so $Q = [\text{red}]/[\text{ox}]$ and $E^\circ_{\mathrm{cell}} = E^\circ - 0 = E^\circ$. Substituting into Eq. (11.2) gives the first equality of Eq. (11.3). At $298.15\,\mathrm{K}$

$$
\frac{RT\ln 10}{F} = \frac{8.314 \times 298.15 \times 2.3026}{96\,485}\,\mathrm{V} = 0.05916\,\mathrm{V},
$$
and replacing $\ln$ by $\lg$ gives the second equality. $\square$

Conventions for the symbols in the equation:

- $[\text{ox}]$ and $[\text{red}]$ denote the products of the relative concentrations $c_{\mathrm{B}}/c^\circ$ (relative partial pressures $p_{\mathrm{B}}/p^\circ$ for gases) of all species on the oxidized-form side and the reduced-form side of the electrode reaction, each raised to the power of its stoichiometric coefficient; pure solids, pure liquids, and the solvent water do not appear. Species whose oxidation state does not change, such as $\ce{H+}$ and $\ce{OH-}$, must also be included whenever they appear in the electrode reaction.
- Strictly, it is the **activities** ([6.1.8](/6.1.8)) that appear in the isotherm, and the Nernst equation should also be expressed in activities. In dilute solutions relative concentrations are a good approximation; in more concentrated electrolyte solutions the two can differ greatly, and the treatment of activity coefficients is found in [Physical Chemistry](/6.3).
- The electrode potential depends only on the ratio $[\text{ox}]/[\text{red}]$; by definition it is a reduction potential, and Eq. (11.3) is used for it whether the electrode acts as the positive or negative electrode in the cell, after which the electromotive force is obtained from $E_{\mathrm{cell}} = E_+ - E_-$.

The Nernst equations of several electrodes ($298.15\,\mathrm{K}$):

$$
\begin{aligned}
\ce{Fe^3+ + e- <=> Fe^2+}:&\quad E = 0.771\,\mathrm{V} + 0.05916\,\mathrm{V}\,\lg\frac{[\ce{Fe^3+}]}{[\ce{Fe^2+}]},\\
\ce{2H+ + 2e- <=> H2}:&\quad E = \frac{0.05916\,\mathrm{V}}{2}\lg\frac{[\ce{H+}]^2}{p_{\ce{H2}}/p^\circ},\\
\ce{Cr2O7^2- + 14H+ + 6e- <=> 2Cr^3+ + 7H2O}:&\quad E = 1.36\,\mathrm{V} + \frac{0.05916\,\mathrm{V}}{6}\lg\frac{[\ce{Cr2O7^2-}][\ce{H+}]^{14}}{[\ce{Cr^3+}]^2}.
\end{aligned}
$$

For the Cu–Zn galvanic cell, the reaction quotient is $Q = [\ce{Zn^2+}]/[\ce{Cu^2+}]$, and

$$
E_{\mathrm{cell}} = 1.104\,\mathrm{V} - \frac{0.05916\,\mathrm{V}}{2}\lg\frac{[\ce{Zn^2+}]}{[\ce{Cu^2+}]}.
$$
As the cell discharges, $[\ce{Zn^2+}]$ increases and $[\ce{Cu^2+}]$ decreases, and the electromotive force falls gradually; when $E_{\mathrm{cell}} = 0$ the reaction is at equilibrium, and the concentration ratio at that point is the **standard equilibrium constant**: $\lg K^\circ = 2 \times 1.104/0.05916 = 37.3$, so $K^\circ \approx 2\times10^{37}$. An equilibrium constant this large means that $[\ce{Cu^2+}]$ at equilibrium is too small to detect, and the reaction effectively goes to completion. The relation $\lg K^\circ = zE^\circ_{\mathrm{cell}}/(0.05916\,\mathrm{V})$ is the basis of the calculation of redox equilibrium constants in [6.1.12](/6.1.12).

![The Nernst equation (298.15 K). Left: the electrode potential of Fe³⁺/Fe²⁺ varies linearly with the logarithm of the concentration ratio, rising 0.0592 V per tenfold change; middle: the electromotive force of the Cu–Zn cell falls with lg([Zn²⁺]/[Cu²⁺]) and reaches zero at lg K° = 37.3; right: for [Cr₂O₇²⁻] = [Cr³⁺] = 1 mol L⁻¹, the electrode potential of Cr₂O₇²⁻/Cr³⁺ falls with pH, and above pH about 2 it can no longer oxidize Br⁻ to Br₂](./plots/nernst-dependence.py)

### 11.5.2. Concentration and Gas Partial Pressure

For the $\ce{Fe^3+}/\ce{Fe^2+}$ electrode, each tenfold increase of $[\ce{Fe^3+}]/[\ce{Fe^2+}]$ raises $E$ by $0.0592\,\mathrm{V}$. Raising $[\ce{Fe^3+}]$ or lowering $[\ce{Fe^2+}]$ raises the electrode potential and strengthens the oxidizing power of $\ce{Fe^3+}$. In general, increasing the concentration of the oxidized form or decreasing that of the reduced form raises the electrode potential; since concentrations enter through a logarithm, a change of one order of magnitude in concentration changes $E$ by only $0.0592/z\,\mathrm{V}$, and the electrode potential changes appreciably only when the concentration changes by many orders of magnitude (for example, through the formation of a precipitate or a complex, 11.5.4).

**Example 11.5.1** Find the electrode potential of a chlorine electrode at $298.15\,\mathrm{K}$ with $[\ce{Cl-}] = 0.100\,\mathrm{mol\,L^{-1}}$ and $p_{\ce{Cl2}} = 300\,\mathrm{kPa}$.

**Solution** The electrode reaction is $\ce{Cl2(g) + 2e- <=> 2Cl-}$ with $E^\circ = 1.358\,\mathrm{V}$, so

$$
E = E^\circ + \frac{0.05916\,\mathrm{V}}{2}\lg\frac{p_{\ce{Cl2}}/p^\circ}{[\ce{Cl-}]^2} = 1.358\,\mathrm{V} + 0.02958\,\mathrm{V} \times \lg\frac{3.00}{(0.100)^2} = 1.431\,\mathrm{V}. \qquad \square
$$

### 11.5.3. Acidity

When $\ce{H+}$ or $\ce{OH-}$ takes part in the electrode reaction, the acidity of the solution is often the main factor affecting the electrode potential. Take $\ce{Cr2O7^2-}/\ce{Cr^3+}$ as an example, with $[\ce{Cr2O7^2-}] = [\ce{Cr^3+}] = 1\,\mathrm{mol\,L^{-1}}$ fixed:

$$
E = 1.36\,\mathrm{V} + \frac{0.05916\,\mathrm{V}}{6}\lg[\ce{H+}]^{14} = 1.36\,\mathrm{V} - 0.138\,\mathrm{V}\times\mathrm{pH}.
$$
At $[\ce{H+}] = 1\,\mathrm{mol\,L^{-1}}$, $E = 1.36\,\mathrm{V}$; at $[\ce{H+}] = 10^{-3}\,\mathrm{mol\,L^{-1}}$, $E = 0.95\,\mathrm{V}$. When an oxoanion acts as the oxidizing agent, the electrode reaction consumes a large amount of $\ce{H+}$ to combine with O and form water, so the oxidizing power of $\ce{K2Cr2O7}$ and $\ce{KMnO4}$ increases markedly with acidity, and in experiments their oxidizing power is adjusted by adjusting the acidity.

**Example 11.5.2** Given $K_{\mathrm{a}}(\ce{HAc}) = 1.75\times10^{-5}$, hydrogen at $p_{\ce{H2}} = 100\,\mathrm{kPa}$ is bubbled through a $0.10\,\mathrm{mol\,L^{-1}}$ acetic acid solution. Find the electrode potential of the hydrogen electrode.

**Solution** From the **acid dissociation constant** ([6.1.9](/6.1.9)) and $c/K_{\mathrm{a}} > 400$, the approximation $[\ce{H+}] = \sqrt{K_{\mathrm{a}}c} = \sqrt{1.75\times10^{-5}\times0.10} = 1.32\times10^{-3}$ can be used, so

$$
E(\ce{H+}/\ce{H2}) = \frac{0.05916\,\mathrm{V}}{2}\lg\frac{[\ce{H+}]^2}{p_{\ce{H2}}/p^\circ} = 0.05916\,\mathrm{V}\times\lg(1.32\times10^{-3}) = -0.170\,\mathrm{V}.
$$
In general the potential of a hydrogen electrode is $E = -0.05916\,\mathrm{V}\times\mathrm{pH}$ ($p_{\ce{H2}} = p^\circ$): the weaker the acidity, the more negative. This is the principle of measuring **pH** with a hydrogen electrode; modern pH meters use a glass electrode instead, whose principle is found in [Analytical Chemistry](/6.4). $\square$

### 11.5.4. Formation of Precipitates and Complexes

Adding $\ce{NaCl}$ to the solution of an $\ce{Ag+}/\ce{Ag}$ electrode produces an $\ce{AgCl}$ precipitate. Suppose that at equilibrium $[\ce{Cl-}] = 1\,\mathrm{mol\,L^{-1}}$; from the **solubility product** ([6.1.10](/6.1.10)) $K_{\mathrm{sp}}(\ce{AgCl}) = 1.8\times10^{-10}$, $[\ce{Ag+}] = K_{\mathrm{sp}}/[\ce{Cl-}] = 1.8\times10^{-10}$, and

$$
E(\ce{Ag+}/\ce{Ag}) = 0.7996\,\mathrm{V} + 0.05916\,\mathrm{V}\times\lg(1.8\times10^{-10}) = 0.223\,\mathrm{V}.
$$
The electrode has now become a metal–sparingly soluble salt–anion electrode $\ce{Ag} \mid \ce{AgCl(s)} \mid \ce{Cl-}(1\,\mathrm{mol\,L^{-1}})$, with all substances in their standard states, so this value is the standard electrode potential $E^\circ(\ce{AgCl}/\ce{Ag})$ of the new couple (tabulated value $0.2223\,\mathrm{V}$). In general, for $\ce{MX(s) + e- <=> M + X-}$,

$$
E^\circ(\ce{MX}/\ce{M}) = E^\circ(\ce{M+}/\ce{M}) + 0.05916\,\mathrm{V}\times\lg K_{\mathrm{sp}}(\ce{MX}).
$$

| Couple | $K_{\mathrm{sp}}$ | $E^\circ/\mathrm{V}$ |
|---|---|---|
| $\ce{Ag+}/\ce{Ag}$ | — | $0.800$ |
| $\ce{AgCl}/\ce{Ag}$ | $1.8\times10^{-10}$ | $0.222$ |
| $\ce{AgBr}/\ce{Ag}$ | $5.4\times10^{-13}$ | $0.071$ |
| $\ce{AgI}/\ce{Ag}$ | $8.5\times10^{-17}$ | $-0.152$ |

The smaller the solubility product of the silver halide, the lower the equilibrium concentration of $\ce{Ag+}$ and the lower the standard electrode potential of $\ce{AgX}/\ce{Ag}$: formation of a precipitate of the oxidized form lowers the electrode potential. Since $E^\circ(\ce{AgI}/\ce{Ag}) < 0$, silver can displace hydrogen from hydroiodic acid (Example 12.1.2 of [6.1.12](/6.1.12)) but not from hydrochloric acid. Conversely, formation of a precipitate of the reduced form raises the electrode potential.

Formation of a complex of the oxidized form likewise lowers the electrode potential. Adding aqueous ammonia to a $\ce{Cu^2+}/\ce{Cu}$ electrode produces $[\ce{Cu(NH3)4}]^{2+}$ (**stability constant** $\lg\beta_4 = 13.32$, [6.1.9](/6.1.9)). When $[\ce{Cu(NH3)4}^{2+}] = [\ce{NH3}] = 1\,\mathrm{mol\,L^{-1}}$, $[\ce{Cu^2+}] = 1/\beta_4$, and

$$
E^\circ([\ce{Cu(NH3)4}]^{2+}/\ce{Cu}) = E^\circ(\ce{Cu^2+}/\ce{Cu}) - \frac{0.05916\,\mathrm{V}}{2}\lg\beta_4 = 0.342 - 0.02958\times13.32 = -0.052\,\mathrm{V}.
$$
Complexation greatly weakens the oxidizing power of Cu(II). The changes in the stability of oxidation states of the copper-group and iron-group elements in the presence of complexing agents (for example, $\ce{Co^3+}$ is a strong oxidizing agent in water, whereas $[\ce{Co(NH3)6}]^{3+}$ is very stable) can all be analyzed quantitatively in this way ([6.1.15](/6.1.15)).

### 11.5.5. Concentration Cells

**Definition 11.5.1 (Concentration Cell)** A galvanic cell whose two electrodes have the same couple and differ only in the concentration of the electrolyte solution (or the partial pressure of the gas) is called a **concentration cell**.

**Example 11.5.3** Find the electromotive force of the following cell at $298.15\,\mathrm{K}$:

$$
(-)\ \ce{Pt} \mid \ce{H2}(p^\circ) \mid \ce{H+}(10^{-3}\,\mathrm{mol\,L^{-1}}) \parallel \ce{H+}(10^{-2}\,\mathrm{mol\,L^{-1}}) \mid \ce{H2}(p^\circ) \mid \ce{Pt}\ (+).
$$

**Solution** Both electrodes involve $\ce{2H+ + 2e- <=> H2}$, and $E^\circ_{\mathrm{cell}} = 0$, so

$$
E_{\mathrm{cell}} = \frac{0.05916\,\mathrm{V}}{2}\left[\lg(10^{-2})^2 - \lg(10^{-3})^2\right] = 0.0592\,\mathrm{V}.
$$
The cell reaction is $\ce{H+}(10^{-2}) \to \ce{H+}(10^{-3})$, that is, ions are "transferred" from the concentrated solution to the dilute one, and the driving force comes entirely from the concentration difference (the entropy of mixing). $\square$

The electromotive force of a concentration cell depends only on the concentration ratio; at $298.15\,\mathrm{K}$, each tenfold concentration difference corresponds to $0.0592/z\,\mathrm{V}$. Membrane potentials produced by differences in ion concentration on the two sides of a biological membrane arise in the same way; the resting potential of cells and nerve impulses both start from the Nernst equation, as discussed in [Cell Biology](/7.3) and [Computational Neuroscience](/7.16).

## Summary

| Topic | Key points |
|---|---|
| Oxidation number | Formal charge after assigning the bonding electrons to the more electronegative atom; an increase of oxidation number is oxidation, a decrease is reduction |
| Balancing | Equal numbers of electrons gained and lost, plus conservation of atoms and charge; oxidation number method, ion–electron method; the coefficient vector lies in the null space of the composition matrix |
| Galvanic cells | Negative electrode (anode): oxidation; positive electrode (cathode): reduction; the salt bridge maintains electroneutrality and lowers the liquid junction potential; in a cell diagram, negative on the left and positive on the right |
| Electrode potential | Reduction potential defined relative to the standard hydrogen electrode ($E^\circ = 0$); $E_{\mathrm{cell}} = E_+ - E_-$; $E^\circ$ is an intensive quantity |
| Thermodynamics | $\Delta_{\mathrm{r}}G_{\mathrm{m}} = -zFE_{\mathrm{cell}}$, $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = -zFE^\circ_{\mathrm{cell}}$, $F = N_{\mathrm{A}}e = 96\,485\,\mathrm{C\,mol^{-1}}$ |
| Nernst equation | $E_{\mathrm{cell}} = E^\circ_{\mathrm{cell}} - \frac{RT}{zF}\ln Q$; $E = E^\circ + \frac{0.05916\,\mathrm{V}}{z}\lg\frac{[\text{ox}]}{[\text{red}]}$ (298.15 K) |
| Influencing factors | Concentration and partial pressure ($0.0592/z\,\mathrm{V}$ per tenfold change); acidity (the oxidizing power of oxoanions increases with acidity); formation of a precipitate or complex of the oxidized form lowers $E$ |

## Questions

1. Why can the electrode potential of a single electrode not be measured, whereas the electromotive force of a cell can be measured precisely?

   **Answer** Measuring the potential difference at a single interface requires introducing another metal–solution interface, so what is measured is always a combination of two interfacial potential differences; the electromotive force of a cell is the potential difference between two metal terminals and can be measured with leads of the same metal.

2. If the equation of the Cu–Zn galvanic cell is written $\ce{2Zn + 2Cu^2+ -> 2Zn^2+ + 2Cu}$, how do $E^\circ_{\mathrm{cell}}$, $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}$, and $K^\circ$ change?

   **Answer** $E^\circ_{\mathrm{cell}}$ is unchanged (intensive quantity); $z$ becomes 4 and $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}$ doubles; $K^\circ$ becomes the square of its former value.

3. Why is $\ce{KMnO4}$ reduced to $\ce{Mn^2+}$ in acidic solution, only to $\ce{MnO2}$ in neutral solution, and only to $\ce{MnO4^2-}$ in strongly basic solution?

   **Answer** The reduction of $\ce{MnO4-}$ to $\ce{Mn^2+}$ consumes 8 $\ce{H+}$, and its electrode potential falls rapidly as pH rises (by about $0.095\,\mathrm{V}$ per pH unit); in basic solution $\ce{Mn^2+}$ cannot exist either. Lower-oxidation-state reduction products that require no $\ce{H+}$, or less of it, are favored under basic conditions (see the Latimer diagram of Mn in [6.1.12](/6.1.12)).
