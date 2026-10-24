---
title: Molecular Orbitals and Electronic Effects
description: LCAO and Hückel molecular orbital theory (secular equations, analytic solutions for ethene and the allyl system, general solutions for chain and ring conjugated systems, eigenvalues with numpy, delocalization energy and bond order); the origin, strength and experimental evidence of the inductive effect, polarizability, the conjugation effect, hyperconjugation and the field effect, and how they show up in acidity, carbocation stability and alkene stability.
source_hash: 71c63beacdc7
---

[6.5.1](/6.5.1) described organic molecules with Lewis structures and **resonance structures**; in this chapter we reexamine the distribution of electrons from the viewpoint of molecular orbitals and classify the ways in which substituents influence electron distribution into several electronic effects. The first half treats Hückel molecular orbital theory, which reduces the π-electron problem of a conjugated system to the eigenvalue problem of a real symmetric matrix ([2.1.7](/2.1.7)) and can be solved with numpy in a few lines ([4.4.3](/4.4.3)). Its results (energy levels, nodes, delocalization stabilization, charge distribution) are the common basis for understanding resonance ([6.5.1](/6.5.1)), pericyclic reactions ([6.5.12](/6.5.12)), aromaticity ([6.5.13](/6.5.13)) and ultraviolet absorption ([6.5.6](/6.5.6)). The second half treats the inductive effect, polarizability, the conjugation effect, hyperconjugation and the field effect. These explain the strength of acids ([6.5.3](/6.5.3)), the stability of carbocations and radicals ([6.5.7](/6.5.7), [6.5.8](/6.5.8)), the stability of alkenes and directing effects on aromatic rings ([6.5.14](/6.5.14)), and are the main tools of qualitative reasoning throughout the course. Atomic orbitals and the molecular orbitals of diatomic molecules were covered in [6.1.3](/6.1.3#sec-3.6) and are only reviewed here.

## 2.1. Review of Molecular Orbital Theory and LCAO

Valence bond theory regards a chemical bond as an electron pair shared between two atoms and repairs its shortcomings with hybridization and resonance. **Molecular orbital theory**, in contrast, holds that each electron in a molecule moves in the average field of all the nuclei and the other electrons, and that its state is described by a molecular orbital spread over the whole molecule. Molecular orbital theory includes delocalization naturally, at the cost of the intuitive picture of "a bond belonging to two atoms".

The Schrödinger equation of a many-electron molecule cannot be solved exactly. The **linear combination of atomic orbitals** (LCAO) approximation writes a molecular orbital as a linear combination of atomic orbitals $\varphi_1, \dots, \varphi_n$,

$$
\psi_k = \sum_{r=1}^{n} c_{rk}\,\varphi_r, \qquad k = 1, \dots, n,
$$
so that $n$ atomic orbitals give $n$ molecular orbitals. The coefficients $c_{rk}$ form a matrix $C$; if the atomic orbitals are orthonormal, the orthonormality of the molecular orbitals is equivalent to $C^{\mathsf T}C = I$, that is, $C$ is an orthogonal matrix, and $c_{rk}^2$ is the probability that an electron in the $k$th molecular orbital is on atom $r$.

The simplest example is $\ce{H2}$: the in-phase combination of the two 1s orbitals is the lower-energy **bonding orbital**, the out-of-phase combination is the higher-energy **antibonding orbital**, and the two electrons occupy the bonding orbital, lowering the energy of the system. When overlap is taken into account, the antibonding orbital is raised more than the bonding orbital is lowered, which is why $\ce{He2}$ (two electrons each in the bonding and antibonding orbitals) is unstable. For organic molecules the most useful orbitals are the highest occupied and the lowest unoccupied ones, the **frontier orbitals**: electrons in the **highest occupied molecular orbital** (HOMO) are the easiest to give up, and the **lowest unoccupied molecular orbital** (LUMO) is the easiest to accept electrons.

## 2.2. Hückel Theory

### 2.2.1. Basic Approximations

In a planar conjugated molecule (alkene, polyene, arene) the $2p_z$ orbital of each sp² carbon is perpendicular to the molecular plane and orthogonal to the σ-bond orbitals in the plane. Hückel (1931) therefore treated only the π electrons, regarding the σ framework as a fixed background (σ–π separation), and made further simplifications.

**Definition 2.2.1 (Hückel Molecular Orbital Method)** The method of finding π molecular orbitals with one p orbital on each atom of a conjugated system as the basis, under the following approximations, is called the **Hückel molecular orbital method** (HMO):

1. the overlap integral $S_{rs} = \int\varphi_r\varphi_s\,\mathrm{d}\tau = \delta_{rs}$ (the atomic orbitals are orthonormal);
2. the diagonal matrix element $H_{rr} = \alpha$, called the *Coulomb integral*, represents the energy of an electron in an isolated $2p$ orbital;
3. between two adjacent (directly bonded) atoms $H_{rs} = \beta$, called the *resonance integral*, and between nonadjacent atoms $H_{rs} = 0$.

Both $\alpha$ and $\beta$ are negative and are treated as empirical parameters.

By the variational principle, the coefficients satisfy the secular equations

$$
\sum_{s=1}^{n}\left(H_{rs} - ES_{rs}\right)c_s = 0, \qquad r = 1, \dots, n,
$$
which have a nonzero solution if the secular determinant $\det(H - EI) = 0$. Let $E = \alpha + x\beta$. The Hückel matrix can then be written $H = \alpha I + \beta A$, where the elements of $A$ are 1 if atoms $r$ and $s$ are adjacent and 0 otherwise, so that $A$ is the **adjacency matrix** of the graph of the π skeleton. The secular equations become

$$
A\boldsymbol{c} = x\boldsymbol{c}. \tag{2.1}
$$
That is, the Hückel energy levels are the eigenvalues of the adjacency matrix of the molecular skeleton, and the coefficients are the corresponding unit eigenvectors. $A$ is a real symmetric matrix, so by the spectral theorem ([Theorem 7.1.1 of 2.1.7](/2.1.7#thm-7.1.1)) its $n$ eigenvalues are all real and the eigenvectors can be chosen orthonormal, which guarantees that the LCAO coefficient matrix above is orthogonal. Because $\beta < 0$, an orbital with $x > 0$ lies below $\alpha$ and is bonding; one with $x < 0$ is antibonding; one with $x = 0$ is nonbonding.

### 2.2.2. Ethene and the Allyl System

The two carbons of ethene are adjacent, $A = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$, and the eigenvalues are $x = \pm1$:

$$
\psi_1 = \tfrac{1}{\sqrt2}(\varphi_1 + \varphi_2),\ E_1 = \alpha + \beta; \qquad \psi_2 = \tfrac{1}{\sqrt2}(\varphi_1 - \varphi_2),\ E_2 = \alpha - \beta.
$$
The two π electrons occupy $\psi_1$, and the energy of the π bond is $2(\alpha + \beta)$, lower by $2\lvert\beta\rvert$ than that of two isolated p electrons.

The allyl system $\ce{CH2=CH-CH2}$ has three adjacent p orbitals (C1–C2–C3):

$$
\det\begin{bmatrix} -x & 1 & 0 \\ 1 & -x & 1 \\ 0 & 1 & -x \end{bmatrix} = -x^3 + 2x = 0, \qquad x = \sqrt2,\ 0,\ -\sqrt2.
$$
Substituting back into Eq. (2.1) and normalizing gives

| Orbital | $E$ | $c_1$ | $c_2$ | $c_3$ | Number of nodes |
|---|---|---|---|---|---|
| $\psi_1$ (bonding) | $\alpha + \sqrt2\beta$ | $1/2$ | $1/\sqrt2$ | $1/2$ | 0 |
| $\psi_2$ (nonbonding) | $\alpha$ | $1/\sqrt2$ | $0$ | $-1/\sqrt2$ | 1 (at C2) |
| $\psi_3$ (antibonding) | $\alpha - \sqrt2\beta$ | $1/2$ | $-1/\sqrt2$ | $1/2$ | 2 |

The allyl cation, radical and anion have 2, 3 and 4 π electrons, respectively, and they differ only in the number of electrons in the nonbonding orbital $\psi_2$. The coefficient of $\psi_2$ on the central carbon is zero, so the missing electron of the cation, the unpaired electron of the radical and the extra pair of the anion are all located on the two terminal carbons, each with $(1/\sqrt2)^2 = 1/2$. This agrees exactly with the **resonance structures** ([6.5.1](/6.5.1#sec-1.6)): each terminal carbon of the allyl cation carries a charge of $+\frac12$, and the central carbon is uncharged. The π-bond energy of all three is $2(\alpha + \sqrt2\beta)$ plus $\alpha$ for any nonbonding electron, and each is stabilized by $2(\sqrt2 - 1)\lvert\beta\rvert \approx 0.83\lvert\beta\rvert$ relative to "an isolated double bond plus an isolated p orbital".

![Resonance structures of the allyl radical and the allyl anion. Radical: the two electrons of the π bond go separate ways (fishhook arrows); one pairs with the unpaired electron on C3 to form the new C2=C3 π bond and the other stays on C1. Anion: the lone pair on C3 forms the new π bond and the old π pair moves onto C1. The unpaired electron or the negative charge sits only on the two end carbons, in agreement with the zero coefficient of the nonbonding orbital ψ₂ on C2](./plots/allyl-resonance.py)

### 2.2.3. Chain and Ring Conjugated Systems

For a linear polyene of $n$ atoms the adjacency matrix is tridiagonal with ones beside the diagonal, and the eigenproblem has a closed-form solution.

**Theorem 2.2.1** The Hückel energy levels and coefficients of a linear conjugated system of $n$ atoms are

$$
x_k = 2\cos\frac{k\pi}{n+1}, \qquad c_{rk} = \sqrt{\frac{2}{n+1}}\,\sin\frac{rk\pi}{n+1}, \qquad k, r = 1, \dots, n. \tag{2.2}
$$

**Proof** Row $r$ of Eq. (2.1) is $c_{r-1} + c_{r+1} = x c_r$, with the boundary conditions $c_0 = c_{n+1} = 0$ (no atoms beyond the chain). Let $c_r = \sin r\theta$. From $\sin(r-1)\theta + \sin(r+1)\theta = 2\cos\theta\sin r\theta$, all interior rows are satisfied with $x = 2\cos\theta$; $c_0 = 0$ holds automatically, and $c_{n+1} = \sin(n+1)\theta = 0$ requires $\theta = k\pi/(n+1)$, where $k = 1, \dots, n$ gives $n$ distinct eigenvalues. The normalization constant follows from $\sum_{r=1}^{n}\sin^2\frac{rk\pi}{n+1} = \frac{n+1}{2}$. $\square$

Several general rules can be read off Eq. (2.2):

- The levels are distributed symmetrically about $\alpha$, all between $\alpha + 2\beta$ and $\alpha - 2\beta$; when $n$ is odd there is one nonbonding orbital ($k = (n+1)/2$).
- The coefficients $\sin(rk\pi/(n+1))$ of the $k$th orbital change sign $k-1$ times along the chain, so the orbital has $k - 1$ nodes: the higher the energy, the more nodes. The lowest orbital has no node, with all atoms in phase; in the highest orbital all neighboring atoms are out of phase.
- For a neutral polyene with even $n$, the HOMO–LUMO gap is $\Delta x = 4\sin\frac{\pi}{2(n+1)}$, which decreases with chain length (ethene 2, butadiene 1.236, hexatriene 0.890): the longer the conjugation, the longer the wavelength of absorption. This agrees with the one-dimensional particle-in-a-box model ([5.5.3](/5.5.3)); the ultraviolet absorption of polyenes is treated in [6.5.6](/6.5.6#sec-6.8.3).

For a ring of $n$ atoms the adjacency matrix is a circulant matrix (each row is a cyclic shift of the previous one), the eigenvectors are $c_r = \mathrm{e}^{2\pi\mathrm{i}kr/n}/\sqrt{n}$, and the levels are

$$
x_k = 2\cos\frac{2\pi k}{n}, \qquad k = 0, 1, \dots, n-1. \tag{2.3}
$$
The lowest level $x_0 = 2$ is nondegenerate, and the others (except the highest level of an even-membered ring) are pairwise degenerate. For benzene ($n = 6$) the levels are $x = 2, 1, 1, -1, -1, -2$. This is the origin of the Hückel rule for aromaticity and of the **Frost circle**; see [6.5.13](/6.5.13#sec-13.3).

### 2.2.4. Calculation with numpy

For a general skeleton (branched, fused, with heteroatoms) there is no closed-form solution, but Eq. (2.1) is only the eigenvalue problem of a symmetric matrix and can be solved numerically with `numpy.linalg.eigh` ([4.4.3](/4.4.3#sec-3.2.3)):

```python
import numpy as np


def huckel(edges, n):
    """Hueckel levels x (E = alpha + x*beta, most bonding first) and coefficients (columns)."""
    a = np.zeros((n, n))
    for r, s in edges:
        a[r, s] = a[s, r] = 1.0
    x, c = np.linalg.eigh(a)  # ascending eigenvalues, orthonormal eigenvectors
    return x[::-1], c[:, ::-1]


def pi_properties(x, c, electrons):
    """Total pi energy (in units of beta, alpha = 0), charges and Coulson bond-order matrix."""
    occ = np.zeros(len(x))
    for k in range(len(x)):
        occ[k] = min(2, electrons - occ.sum())
    energy = occ @ x
    p = (c * occ) @ c.T  # p_rs = sum_k n_k c_rk c_sk
    charge = 1 - np.diag(p)  # one pi electron per carbon in the neutral reference
    return energy, charge, p


butadiene = huckel([(0, 1), (1, 2), (2, 3)], 4)
energy, charge, p = pi_properties(*butadiene, electrons=4)
print(np.round(butadiene[0], 3))  # [ 1.618  0.618 -0.618 -1.618]
print(round(energy, 3))  # 4.472
print(np.round([p[0, 1], p[1, 2]], 3))  # [0.894 0.447]
```

![Hückel π molecular orbitals of ethene, allyl, butadiene and hexatriene: each orbital is drawn at its energy, the area of a circle is proportional to the square of the coefficient and the color indicates the sign; the dots on the left are the electrons in the neutral molecule (the radical for allyl). The higher the energy, the more nodes](./plots/huckel-polyenes.py)

From the levels and coefficients one can calculate several quantities that can be compared with experiment:

- The total π-electron energy $E_\pi = \sum_k n_k(\alpha + x_k\beta)$, where $n_k$ is the number of electrons in the $k$th orbital.
- Charge: the number of π electrons on atom $r$ is $q_r = \sum_k n_k c_{rk}^2$. In the neutral molecules of alternant hydrocarbons (conjugated hydrocarbons whose atoms can be divided into two sets with no two atoms of the same set adjacent, such as all linear polyenes and benzene), $q_r = 1$ on every carbon, so the π electrons are uniformly distributed.
- The π **bond order** (Coulson bond order) $p_{rs} = \sum_k n_k c_{rk}c_{sk}$: it is 1 for ethene and $2/3$ for each bond of benzene; the greater the bond order, the shorter the bond.

**Definition 2.2.2 (Delocalization Energy)** The difference between the π-electron energy of a conjugated system and that of a hypothetical localized structure made of isolated double bonds (and isolated p orbitals) is called the **delocalization energy**.

| System | π electrons | $E_\pi - n_\pi\alpha$ | Localized structure | Delocalization energy | Bond orders |
|---|---|---|---|---|---|
| Ethene | 2 | $2\beta$ | 1 double bond | 0 | 1 |
| Allyl (cation, radical, anion) | 2, 3, 4 | $2\sqrt2\beta = 2.828\beta$ | 1 double bond + isolated p orbital | $0.828\beta$ | 0.707, 0.707 |
| Buta-1,3-diene | 4 | $4.472\beta$ | 2 double bonds | $0.472\beta$ | 0.894, 0.447, 0.894 |
| Hexa-1,3,5-triene | 6 | $6.988\beta$ | 3 double bonds | $0.988\beta$ | 0.871, 0.483, 0.785 |
| Benzene | 6 | $8\beta$ | 3 double bonds | $2\beta$ | 0.667 |

The delocalization energy of benzene ($2\beta$) is twice that of the open-chain hexatriene ($0.988\beta$), which is how **aromaticity** shows up in Hückel theory ([6.5.13](/6.5.13#sec-13.2.2)). The bond orders 0.894 and 0.447 of butadiene explain its alternating bond lengths (C1–C2 $134\,\mathrm{pm}$, C2–C3 $146\,\mathrm{pm}$).

The limitations of the Hückel method are also clear. It neglects overlap and electron repulsion, and the value of $\beta$ depends on the property used for calibration: calibration with the stabilization energy of benzene (about $150\,\mathrm{kJ\,mol^{-1}}$, [6.5.13](/6.5.13#sec-13.1.2)) gives $\beta \approx -75\,\mathrm{kJ\,mol^{-1}}$, and calibration with ultraviolet absorption energies gives about $-2.5\,\mathrm{eV}$ (about $-240\,\mathrm{kJ\,mol^{-1}}$). Systems with heteroatoms need additional parameters ($\alpha_{\mathrm{X}} = \alpha + h_{\mathrm{X}}\beta$, $\beta_{\mathrm{CX}} = k_{\mathrm{CX}}\beta$). Quantitative structures and energies are obtained today by ab initio methods such as density functional theory, but the orbital shapes, nodes and symmetry given by the Hückel method remain the language in which frontier orbitals and pericyclic reactions are discussed ([6.5.12](/6.5.12#sec-12.2)).

## 2.3. The Inductive Effect

Substituents change the electron distribution in a molecule in two ways: the inductive effect, transmitted through σ bonds, and the conjugation effect, transmitted through the π system (2.5).

**Definition 2.3.1 (Inductive Effect)** Because the bonded atoms differ in electronegativity, the electron cloud of a σ bond is displaced toward the more electronegative atom; the effect by which this polarization is transmitted from bond to bond along the σ framework and shifts the electron distribution in the molecule is called the **inductive effect**, denoted I. Taking the C–H bond as the standard, a substituent that draws electrons away from carbon has an electron-withdrawing inductive effect ($-$I), and one that pushes electrons toward carbon has an electron-donating inductive effect ($+$I).

The inductive effect is represented by straight arrows or by $\delta^+$ and $\delta^-$, the arrow pointing in the direction of the electron shift: in 1-chloropropane $\ce{CH3-CH2-CH2-Cl}$, C1 carries $\delta^+$, C2 a smaller $\delta\delta^+$ and C3 a still smaller $\delta\delta\delta^+$. Its characteristics are:

1. It is an intrinsic property of the molecule (the static inductive effect) and exists without an external field.
2. The electron pair is only displaced, not transferred; what changes is the polarity of the bond.
3. It decays rapidly along the carbon chain, weakening to between one half and one third with each bond, and is generally negligible after three bonds.

The strength of the inductive effect is determined mainly by the attached atom (the "key atom"):

- Within a period, the greater the electronegativity, the stronger the $-$I effect: $-\mathrm{F} > -\mathrm{OR} > -\mathrm{NR_2}$; within a group it weakens from top to bottom: $-\mathrm{F} > -\mathrm{Cl} > -\mathrm{Br} > -\mathrm{I}$.
- For the same key atom, a positively charged group is a much stronger electron acceptor: $-\overset{+}{\mathrm{N}}\mathrm{R_3} \gg -\mathrm{NR_2}$, $-\overset{+}{\mathrm{O}}\mathrm{R_2} > -\mathrm{OR}$.
- The greater the s character of a carbon atom, the greater its electronegativity: $-\mathrm{C{\equiv}CR} > -\mathrm{CH{=}CR_2} > -\mathrm{CR_3}$.
- Negatively charged groups ($-\mathrm{O^-}$, $-\mathrm{COO^-}$) and atoms less electronegative than carbon (B, Si, Mg, metals such as Li) are $+$I groups.

The $-$I order of common groups is roughly $-\overset{+}{\mathrm{N}}\mathrm{R_3} > -\mathrm{NO_2} > -\mathrm{CN} > -\mathrm{F} > -\mathrm{Cl} > -\mathrm{Br} > -\mathrm{I} > -\mathrm{C{\equiv}CH} > -\mathrm{OR} \approx -\mathrm{OH} > -\mathrm{C_6H_5} > -\mathrm{CH{=}CH_2} > -\mathrm{H}$; the order varies slightly with the parent molecule and the medium. Alkyl groups are often listed as $+$I groups relative to H ($(\mathrm{CH_3})_3\mathrm{C}- > (\mathrm{CH_3})_2\mathrm{CH}- > \mathrm{CH_3CH_2}- > \mathrm{CH_3}-$), but this statement needs caution: the electronegativities of C(sp³) and H are close, and the inductive effect of alkyl groups is weak. Alkyl groups stabilize **carbocations** mainly by hyperconjugation (2.6); in the gas phase alkyl groups can also stabilize negative charge through their polarizability (tert-butyl alcohol is more acidic than methanol in the gas phase), and the opposite acidity order of alcohols in solution comes from solvation ([6.5.3](/6.5.3#sec-3.3)).

Evidence for the inductive effect:

| Observable | Data | Explanation |
|---|---|---|
| $\mathrm{p}K_{\mathrm{a}}$ of chloroacetic acids | $\ce{CH3COOH}$ 4.76, $\ce{ClCH2COOH}$ 2.87, $\ce{Cl2CHCOOH}$ 1.35, $\ce{Cl3CCOOH}$ 0.66 | The more chlorine, the more stable the carboxylate and the stronger the acid |
| $\mathrm{p}K_{\mathrm{a}}$ of chlorobutanoic acids (water, 25 °C, CRC) | Butanoic acid 4.82, 2-chloro 2.86, 3-chloro 4.05, 4-chloro 4.52 | The farther the chlorine from the carboxyl group, the weaker the effect |
| ¹H chemical shift $\delta$ of $\ce{CH3X}$ | F 4.26, Cl 3.05, Br 2.68, I 2.16, H 0.23 | The greater the electronegativity, the lower the electron density around H ([6.4.12](/6.4.12)) |
| ¹H $\delta$ of chloromethanes | $\ce{CH3Cl}$ 3.05, $\ce{CH2Cl2}$ 5.30, $\ce{CHCl3}$ 7.26 | The effect is approximately additive |
| Dipole moment of $\ce{CH3X}$ (gas phase) | F 1.86, Cl 1.89, Br 1.82, I 1.62, CN 3.92, $\ce{NO2}$ 3.46 D | The dipole moment also depends on bond length and does not follow electronegativity exactly |

The inductive effect can also be produced temporarily by external factors. When a reagent approaches, its electric field temporarily polarizes the electron cloud of the substrate, which is called the dynamic inductive effect; for example, when $\ce{Br2}$ approaches the π electrons of an alkene, the Br–Br bond is polarized to $\mathrm{Br^{\delta+}{-}Br^{\delta-}}$, with the end nearer the alkene partially positive ([6.5.11](/6.5.11#sec-11.4.2)). The size of the dynamic inductive effect depends on the polarizability of the molecule (2.4); it acts only at the instant of reaction and often matters more for the reaction rate than the static effect.

![Dynamic induction: as Br₂ approaches the π electrons of ethene, the Br–Br bond is polarized, with the near bromine partly positive and the far one partly negative; the π electrons then attack the near bromine while the Br–Br bonding pair leaves as bromide, giving a cyclic bromonium ion](./plots/dynamic-induction.py)

## 2.4. Polarization and Polarizability

The ability of a molecule to have its electron cloud deformed in an external electric field and to acquire an induced dipole is called its **polarizability** (in organic chemistry often called polarizability or deformability). The more loosely the electrons are bound by the nuclei, the greater the polarizability:

- Atoms become larger down a group and polarizability increases: $\ce{R-I} > \ce{R-Br} > \ce{R-Cl} > \ce{R-F}$; S is more easily polarized than O, and P more than N.
- Lone pairs are more easily polarized than bonding electrons, and π electrons more easily than σ electrons.

Polarizability is closely related to reactivity: a molecule or group that is easily polarized can adjust its electron distribution to the reaction as a reagent approaches, and therefore reacts more readily. The bond dissociation energies of the halomethanes are $\ce{CH3-F}$ $460$, $\ce{CH3-Cl}$ $350$, $\ce{CH3-Br}$ $294$ and $\ce{CH3-I}$ $239\,\mathrm{kJ\,mol^{-1}}$; the C–I bond is the weakest and the most polarizable, so alkyl iodides react fastest in nucleophilic substitution, even though the C–F bond is the most polar ([6.5.8](/6.5.8#sec-8.6)). Reagents of high polarizability such as $\ce{I-}$ and $\ce{RS-}$ are good nucleophiles, which is what "soft" means in the principle of **hard and soft acids and bases** ([6.5.3](/6.5.3#sec-3.4)). The **London dispersion forces** between molecules of high polarizability are also strong, and alkyl iodides boil much higher than alkyl chlorides with the same number of carbons.

## 2.5. The Conjugation Effect

### 2.5.1. Conjugation and Delocalization

In a conjugated system, adjacent p orbitals are parallel and overlap sideways, and the π electrons (together with conjugated lone pairs, empty orbitals or single electrons) are delocalized over the whole system. Delocalization has three observable consequences.

Structurally, the atoms taking part in conjugation are coplanar and the bond lengths tend to equalize. The C2–C3 single bond of buta-1,3-diene ($146\,\mathrm{pm}$) is shorter than the C–C bond of ethane ($153\,\mathrm{pm}$), and the C=C bond ($134\,\mathrm{pm}$) is slightly longer than that of ethene ($133\,\mathrm{pm}$). Note that a considerable part of the shortening of the C2–C3 bond arises because both carbons are sp² hybridized (the covalent radius of an sp² carbon is smaller than that of an sp³ carbon) and not only from conjugation.

Energetically, conjugated systems have lower internal energy. Compare the enthalpies of hydrogenation (gas phase, $\mathrm{kJ\,mol^{-1}}$):

| Compound | Hydrogenation product | $\Delta_{\mathrm{hyd}}H$ |
|---|---|---|
| Pent-1-ene (one monosubstituted C=C) | Pentane | $-126$ |
| Penta-1,4-diene (two isolated monosubstituted C=C) | Pentane | $-254$ |
| $(E)$-Penta-1,3-diene (conjugated) | Pentane | $-226$ |

The conjugated diene releases $28\,\mathrm{kJ\,mol^{-1}}$ less heat than the isolated diene. About $11\,\mathrm{kJ\,mol^{-1}}$ of this comes from one double bond of the 1,3-diene being disubstituted (the more substituted a double bond, the more stable it is, 2.6); after subtracting it, the stabilization from conjugation itself is about $17\,\mathrm{kJ\,mol^{-1}}$, in agreement with the estimate for buta-1,3-diene ($2 \times 126.8 - 236.7 \approx 17\,\mathrm{kJ\,mol^{-1}}$). This value is far smaller than the stabilization energy of benzene (about $150\,\mathrm{kJ\,mol^{-1}}$), roughly in the ratio of the Hückel delocalization energies $0.47\beta$ and $2\beta$.

In electron distribution, a substituent pushes electrons into or pulls them out of the π system by conjugation; the effect is transmitted along the conjugated chain with almost no decay and appears alternately along the chain (the charge appears on every second atom).

**Definition 2.5.1 (Conjugation Effect)** In a conjugated system, the effect by which delocalization of π electrons (and of lone pairs and empty orbitals conjugated with them) changes the electron distribution and properties of the molecule is called the **conjugation effect**, also called the mesomeric effect, denoted M (or C). A substituent that supplies electrons to the conjugated system has an electron-donating conjugation effect ($+$M), and one that attracts electrons from it has an electron-withdrawing conjugation effect ($-$M).

![Electron-donating and electron-withdrawing conjugation: (a) in methoxyethene the lone pair on oxygen is delocalized onto the C=C bond (+M) and the terminal carbon is electron-rich; (b) in propenal the π electrons of the C=C bond are delocalized toward the carbonyl oxygen (−M) and the terminal carbon is electron-poor. On the right are the minor, charge-separated resonance structures](./plots/mesomeric-effects.py)

According to the orbitals taking part in delocalization, conjugation is π–π conjugation (butadiene, propenal) or p–π conjugation (the allyl cation, radical and anion; the lone pairs of the heteroatom in chloroethene and methoxyethene). According to the relation between the number of electrons and the number of atoms involved, conjugation is isoelectronic (as in butadiene, 4 electrons over 4 atoms), electron-rich (as in the allyl anion and chloroethene, 4 electrons over 3 atoms) or electron-poor (as in the allyl cation, 2 electrons over 3 atoms).

The strength of the conjugation effect follows these rules:

- $-$M groups ($-\mathrm{CH{=}O}$, $-\mathrm{COR}$, $-\mathrm{COOR}$, $-\mathrm{CN}$, $-\mathrm{NO_2}$, $-\mathrm{SO_2R}$): the greater the electronegativity of the atom at the other end of the double bond, the stronger the electron withdrawal, $=\mathrm{O} > =\mathrm{NR} > =\mathrm{CR_2}$; within a group $=\mathrm{O} > =\mathrm{S}$, because the p orbitals of C and S do not match in size and overlap poorly.
- $+$M groups ($-\mathrm{NR_2}$, $-\mathrm{OR}$, $-\mathrm{OH}$, halogens): within a period, the smaller the electronegativity, the more easily the lone pair is donated, $-\mathrm{NR_2} > -\mathrm{OR} > -\mathrm{F}$; within a group, the closer the size to the carbon 2p orbital, the better the overlap and the stronger the donation, $-\mathrm{F} > -\mathrm{Cl} > -\mathrm{Br} > -\mathrm{I}$, $-\mathrm{OR} > -\mathrm{SR}$; a negatively charged group donates more strongly, $-\mathrm{O^-} > -\mathrm{OR}$.

### 2.5.2. Competition between the Inductive and Conjugation Effects

The same substituent often has both an inductive effect and a conjugation effect, and the two may act in the same direction or in opposite directions:

| Substituent | Inductive effect | Conjugation effect | Net effect (on a conjugated system) |
|---|---|---|---|
| $-\mathrm{NO_2}$, $-\mathrm{CN}$, $-\mathrm{COR}$, $-\mathrm{COOR}$ | $-$I | $-$M | Strongly electron-withdrawing |
| $-\overset{+}{\mathrm{N}}\mathrm{R_3}$, $-\mathrm{CF_3}$ | $-$I | None | Electron-withdrawing |
| $-\mathrm{NR_2}$, $-\mathrm{OR}$, $-\mathrm{OH}$ | $-$I | $+$M (strong) | Electron-donating (conjugation dominates) |
| $-\mathrm{F}$, $-\mathrm{Cl}$, $-\mathrm{Br}$, $-\mathrm{I}$ | $-$I (strong) | $+$M (weak) | Electron-withdrawing (induction dominates), but conjugation enriches the *ortho* and *para* positions |
| $-\mathrm{O^-}$ | $+$I | $+$M | Strongly electron-donating |
| Alkyl | Weak $+$I | Hyperconjugation (2.6) | Weakly electron-donating |

The relative importance of the two effects can be separated quantitatively by Hammett **substituent constants** ([6.5.3](/6.5.3#sec-3.5)): a methoxy group in the *meta* position of benzoic acid can act only inductively, $\sigma_m = +0.12$ (electron-withdrawing); in the *para* position conjugation acts, $\sigma_p = -0.27$ (electron-donating). For the halogens both $\sigma_m$ and $\sigma_p$ are positive, but $\sigma_p < \sigma_m$. That halobenzenes are "deactivated but *ortho*, *para*-directing" in **electrophilic aromatic substitution** ([6.5.14](/6.5.14#sec-14.3.2)) is a result of this competition.

![The +M effect of chlorine in chlorobenzene: a lone pair on chlorine moves into the ring, and the negative charge is passed on to the two ortho carbons and the para carbon. These charge-separated structures are minor contributors (the −I effect dominates overall), but they explain why electron density builds up at the ortho and para positions](./plots/chlorobenzene-resonance.py)

The stabilization of **carbocations** by p–π conjugation can be seen from the gas-phase hydride ion affinity ($\mathrm{HIA}$, the $-\Delta H$ of the reaction $\ce{R+ + H- -> RH}$): the smaller the HIA, the more stable the carbocation. The HIA values of the propyl, allyl and benzyl cations are about $266$, $256$ and $234\,\mathrm{kcal\,mol^{-1}}$ ($1113$, $1071$ and $979\,\mathrm{kJ\,mol^{-1}}$): the empty p orbital of the allyl and benzyl cations is conjugated with the adjacent π system, and the positive charge is delocalized. The same conjugation stabilizes the allyl and benzyl radicals ([6.5.7](/6.5.7#sec-7.3.2)).

## 2.6. Hyperconjugation

The more alkyl substituents a **carbocation** has, the more stable it is, and the more substituted an alkene, the more stable it is, yet alkyl groups have neither π electrons nor a strong inductive effect. The explanation is the delocalization of σ-bond electrons.

**Definition 2.6.1 (Hyperconjugation)** The effect by which the bonding electrons of a C–H (or C–C) σ bond next to a p orbital or π system are delocalized into that p orbital or into a π* orbital, stabilizing the system, is called **hyperconjugation**. That between a σ bond and an empty p orbital (or a singly occupied p orbital) is called σ–p hyperconjugation, and that between a σ bond and a π bond is called σ–π hyperconjugation.

![Hyperconjugation in the ethyl cation. Left: a C–H bond of the methyl group is parallel to the empty p orbital of the cationic carbon, and the σ(C–H) orbital overlaps with the p orbital; right: the interaction of the two orbitals, in which the occupied σ orbital is lowered in energy (stabilized), the empty p orbital is raised, and the two electrons are partially delocalized onto the cationic carbon](./plots/hyperconjugation.py)

Hyperconjugation requires the σ bond and the p orbital to be approximately parallel and therefore depends on conformation: a C–H bond perpendicular to the p orbital (lying in the nodal plane of the p orbital) does not contribute. Each $\alpha$ C–H (and $\alpha$ C–C) bond of a carbocation can rotate into a suitable orientation, and the more bonds that can provide hyperconjugation, the greater the stabilization. The evidence:

| Evidence | Data | Conclusion |
|---|---|---|
| Gas-phase HIA of carbocations / (kcal mol⁻¹) | $\ce{CH3+}$ 312, $\ce{CH3CH2+}$ 273, $\ce{(CH3)2CH+}$ 246, $\ce{(CH3)3C+}$ 231 | Stability $\mathrm{CH_3^+} < 1^\circ < 2^\circ < 3^\circ$, parallel to the number of $\alpha$ C–H bonds (0, 3, 6, 9) |
| Enthalpies of hydrogenation of butenes (gas phase) / (kJ mol⁻¹) | But-1-ene $-126.8$, $(Z)$-but-2-ene $-119.7$, $(E)$-but-2-ene $-115.5$ | Internal alkenes are more stable than terminal ones; the $Z$ isomer is slightly less stable because of steric repulsion between the two methyl groups ([6.5.9](/6.5.9#sec-9.1)) |
| Structure of carbocations | The C–C bonds of the tert-butyl cation ($144\,\mathrm{pm}$) are shorter than ordinary C–C single bonds | σ electrons partly enter the p orbital between the carbons |

($\mathrm{1\,kcal\,mol^{-1}} = 4.184\,\mathrm{kJ\,mol^{-1}}$, so $312\,\mathrm{kcal\,mol^{-1}}$ for $\ce{CH3+}$ corresponds to $1305\,\mathrm{kJ\,mol^{-1}}$; data in $\mathrm{kJ\,mol^{-1}}$ are in [6.5.8](/6.5.8#sec-8.3.2).)

The direction of hyperconjugation is usually electron donation. It also stabilizes radicals, but less than carbocations: the p orbital of a radical already has one electron, and when the σ orbital interacts with the singly occupied p orbital, one of the three electrons must go into the raised orbital, so the net stabilization is about half that for the carbocation; the stability order of radicals ($3^\circ > 2^\circ > 1^\circ$) is therefore the same but the differences are smaller ([6.5.7](/6.5.7#sec-7.3.1)). The p orbital of a **carbanion** is already filled, and interaction with an occupied σ orbital is destabilizing, so alkyl groups destabilize carbanions.

σ-Bond electrons can also act as acceptors: the interaction in which a lone pair or π electrons enter an adjacent σ* antibonding orbital is called **negative hyperconjugation**, which explains phenomena such as the anomeric effect of sugars ([6.5.32](/6.5.32)).

![Hyperconjugation in curved-arrow language: (a) σ–p hyperconjugation in the ethyl cation written as "no-bond resonance": the electrons of a C–H bond next to the cationic carbon move into the C–C region, so that in the minor structure the proton is detached and a C=C bond has formed; (b) negative hyperconjugation in chloromethyl methyl ether: an oxygen lone pair enters the C–Cl σ* orbital, written as an O=C double bond and a chloride ion. Neither minor structure is a real species; they show where the electron density goes](./plots/hyperconjugation-arrows.py)

## 2.7. The Field Effect

**Definition 2.7.1 (Field Effect)** The electronic effect in which the electric field produced by the dipole or charge of a substituent acts directly through space (or solvent) on another reaction center in the molecule, without transmission through chemical bonds, is called the **field effect**.

The field effect and the inductive effect usually coexist, because a polar bond both transmits polarization along the bonds and creates an electric field in space; they can be separated only where their predictions differ. The second ionization of dicarboxylic acids is an example of a field effect: malonic acid has $\mathrm{p}K_{\mathrm{a1}} = 2.85$ and $\mathrm{p}K_{\mathrm{a2}} = 5.70$, succinic acid $4.21$ and $5.64$ (water, 25 °C, CRC, consistent with [6.5.18](/6.5.18#sec-18.2.4)). After the first carboxyl group has ionized, the negatively charged $\ce{-COO-}$ repels the departure of the second proton through space and makes the second ionization more difficult, the more so the closer the two carboxyl groups are. (About 0.6 of the difference between $\mathrm{p}K_{\mathrm{a1}}$ and $\mathrm{p}K_{\mathrm{a2}}$ comes from a statistical factor: a dicarboxylic acid has two ionizable protons, and its conjugate base has two sites that can accept a proton, $\lg 4 \approx 0.6$.)

Clearer evidence comes from rigid molecules: two stereoisomers of identical constitution that differ only in the spatial orientation of the C–Cl bond relative to the carboxyl group, with the same path for transmission of the inductive effect, have $\mathrm{p}K_{\mathrm{a}}$ values of 5.67 and 6.07 in aqueous ethanol. The isomer in which the negative end of the C–Cl dipole points toward the carboxyl group is the weaker acid: the field of the negative end of the dipole destabilizes the negative charge of the carboxylate, contrary to the prediction of the inductive effect, in which the electron-withdrawing chlorine atom should strengthen the acid.

## 2.8. Comparison of Electronic Effects

| Effect | Origin | Path of transmission | Variation with distance | Typical manifestation |
|---|---|---|---|---|
| Inductive effect | Polarization of σ bonds by electronegativity differences | Along σ bonds | Decays rapidly, negligible after about three bonds | Acidity of haloacetic acids; chemical shifts of $\ce{CH3X}$ |
| Conjugation effect | Delocalization of π electrons and lone pairs in parallel p orbitals | Along the conjugated π system | Essentially no decay, alternating | Acidity of phenols and carboxylic acids; directing effects on aromatic rings; equalization of bond lengths |
| Hyperconjugation | Overlap of an adjacent σ bond with a p or π* orbital | The one adjacent bond | Acts only at the adjacent position, depends on conformation | Stability of carbocations, radicals and alkenes |
| Field effect | Electric field of a dipole or charge | Space and solvent | Decreases with distance and dielectric constant | Second ionization of dicarboxylic acids; orientation effects in rigid molecules |
| Polarizability | Looseness with which electrons are bound | Induced by an external field (the reagent) | Acts only during reaction | Reactivity of alkyl iodides; soft nucleophiles |

Together with steric hindrance (steric effects), these effects make up the basic content of "structure–activity relationships" in organic chemistry: how substituents change the acidity and basicity, the rate and the selectivity of reactions. The **Hammett equation** of [6.5.3](/6.5.3#sec-3.5) turns the inductive and conjugation effects in aromatic systems into measurable numbers.

## Summary

- LCAO writes a molecular orbital as a combination of atomic orbitals; the Hückel method (Definition 2.2.1) considers only π electrons, takes $S_{rs} = \delta_{rs}$, $H_{rr} = \alpha$ and $H_{rs} = \beta$ for adjacent atoms, so that $x$ in the π levels $E = \alpha + x\beta$ is an eigenvalue of the adjacency matrix of the skeleton (Eq. (2.1)) and the coefficients are the orthonormal eigenvectors.
- Chain: $x_k = 2\cos\frac{k\pi}{n+1}$, $c_{rk} = \sqrt{\frac{2}{n+1}}\sin\frac{rk\pi}{n+1}$ (Theorem 2.2.1); the $k$th orbital has $k-1$ nodes and the HOMO–LUMO gap decreases with chain length; ring: $x_k = 2\cos\frac{2\pi k}{n}$ (Eq. (2.3)).
- The nonbonding orbital of allyl is zero on the central carbon, so the charge or spin of the cation, radical and anion lies on the two terminal carbons, in agreement with the resonance structures; delocalization energies (Definition 2.2.2): allyl $0.83\beta$, butadiene $0.47\beta$, hexatriene $0.99\beta$, benzene $2\beta$.
- The inductive effect (Definition 2.3.1) is transmitted along σ bonds and decays rapidly, with strength set by electronegativity, charge and hybridization; the dynamic inductive effect and polarizability act at the instant of reaction. Polarizability increases with atomic size, and lone pairs and π electrons are more easily polarized.
- The conjugation effect (Definition 2.5.1) is transmitted along the π system without decay and alternates; $-$M: $=\mathrm{O} > =\mathrm{NR} > =\mathrm{CR_2}$; $+$M: $-\mathrm{NR_2} > -\mathrm{OR} > -\mathrm{F}$, $-\mathrm{F} > -\mathrm{Cl} > -\mathrm{Br} > -\mathrm{I}$, $-\mathrm{O^-} > -\mathrm{OR}$. For halogens $-$I dominates, for $\mathrm{OR}$ and $\mathrm{NR_2}$ $+$M dominates.
- Hyperconjugation (Definition 2.6.1) explains the stability of carbocations ($3^\circ > 2^\circ > 1^\circ > \mathrm{CH_3^+}$), radicals and polysubstituted alkenes; it depends on conformation, acts more weakly on radicals and is unfavorable for carbanions.
- The field effect (Definition 2.7.1) is transmitted through space and shows in the second ionization of dicarboxylic acids and in orientation effects in rigid molecules.

## Questions

1. Use the Hückel method to find the number of π electrons on each carbon of the allyl anion, and compare with the resonance structures.

   **Answer** The anion has 4 π electrons, which occupy $\psi_1$ and $\psi_2$. Terminal carbons: $q_1 = 2\cdot(1/2)^2 + 2\cdot(1/\sqrt2)^2 = 1.5$; central carbon: $q_2 = 2\cdot(1/\sqrt2)^2 + 2\cdot 0 = 1$. Each terminal carbon carries a charge of $-\frac12$ and the central carbon is uncharged, in agreement with the two resonance structures $\mathrm{CH_2{=}CH{-}\overset{-}{C}H_2} \leftrightarrow \mathrm{\overset{-}{C}H_2{-}CH{=}CH_2}$.
2. What are the Hückel energy levels of cyclobutadiene? How are the 4 π electrons distributed? What is its delocalization energy, and what does a comparison with benzene show?

   **Answer** From Eq. (2.3) with $n = 4$: $x = 2, 0, 0, -2$. Two electrons fill the orbital with $x = 2$, and the other two go one each into the two degenerate nonbonding orbitals (Hund's rule, parallel spins), so $E_\pi = 4\alpha + 4\beta$, the same as for two isolated double bonds; the delocalization energy is zero and the molecule is a diradical. The delocalization energy of benzene is $2\beta$. A cyclic system with $4n$ π electrons has no delocalization stabilization (real cyclobutadiene distorts to a rectangle to remove the degeneracy and is very unstable); this is **antiaromaticity** ([6.5.13](/6.5.13#sec-13.5.2)).
3. Are the allyl and benzyl radicals more stable than the propyl radical? Why?

   **Answer** Yes. The p orbital carrying the unpaired electron of the allyl radical is conjugated in parallel with the adjacent C=C π orbital (p–π conjugation), and the unpaired electron is delocalized onto the two terminal carbons (Hückel: the nonbonding orbital has coefficients only on the terminal carbons); in the benzyl radical the unpaired electron is delocalized onto the *ortho* and *para* positions of the benzene ring. Delocalization stabilizes the radical and lowers the bond dissociation energy of the corresponding C–H bond: about $372\,\mathrm{kJ\,mol^{-1}}$ for the allylic C–H bond of propene and about $375\,\mathrm{kJ\,mol^{-1}}$ for the benzylic C–H bond of toluene, against about $423\,\mathrm{kJ\,mol^{-1}}$ for the primary C–H bond of propane (table in [6.5.7](/6.5.7#def-7.2.2)).
4. Decide whether each statement is true or false, and explain: (a) electron-withdrawing conjugation effect $=\mathrm{O} > =\mathrm{NR} > =\mathrm{CR_2}$; (b) electron-withdrawing conjugation effect $=\mathrm{O} < =\mathrm{S}$; (c) electron-donating conjugation effect $-\mathrm{NR_2} < -\mathrm{OR} < -\mathrm{F}$; (d) electron-donating conjugation effect $-\mathrm{O^-} > -\mathrm{OR}$.

   **Answer** (a) True: within a period, the greater the electronegativity, the more the π electrons are drawn toward that atom. (b) False: the 3p orbital of S overlaps poorly with the 2p orbital of C, so the electron-withdrawing conjugation effect of $=\mathrm{S}$ is weaker than that of $=\mathrm{O}$. (c) False, the order is the reverse: the smaller the electronegativity, the more easily the lone pair is donated, $-\mathrm{NR_2} > -\mathrm{OR} > -\mathrm{F}$. (d) True: negatively charged oxygen is a stronger donor.
5. Sketch the orbitals of σ–p hyperconjugation in the 2-methylpropan-2-yl (*tert*-butyl) cation, and explain why a similar but weaker stabilization is present in the *tert*-butyl radical.

   **Answer** The cationic carbon is sp² and has an empty p orbital perpendicular to the $\ce{C3}$ plane; each of the three methyl groups has one C–H bond that can rotate into a position parallel to the p orbital, and the σ(C–H) orbital combines in phase with the empty p orbital to give a lower-energy bonding combination into which the two σ electrons go (the interaction diagram on the right of the figure). The p orbital of the radical already contains one electron; of the two combinations formed by σ and p interaction, the lower holds two electrons and the higher holds one, so the net stabilization is only a fraction of that in the cation, and alkyl groups stabilize radicals less.
6. Why does $\mathrm{p}K_{\mathrm{a2}} - \mathrm{p}K_{\mathrm{a1}}$ of the dicarboxylic acids $\ce{HOOC(CH2)_nCOOH}$ decrease as $n$ increases? What value does it approach for large $n$?

   **Answer** The $\ce{-COO-}$ formed by ionization of the first carboxyl group makes the dissociation of the second proton more difficult through the inductive effect (along the bonds) and the field effect (through space), and the farther apart the two carboxyl groups, the weaker the effect: oxalic acid ($n = 0$) $1.25$, $3.81$; malonic acid $2.85$, $5.70$; succinic acid $4.21$, $5.64$; adipic acid about $4.4$, $5.4$. For large $n$ the two carboxyl groups do not affect each other, and only the statistical factor $\lg 4 \approx 0.6$ remains.
7. Use `numpy` to calculate the π-electron energies of the penta-2,4-dien-1-yl (pentadienyl) cation and of benzene, verify that the positive charge of the cation is located on C1, C3 and C5, and find the delocalization energy of benzene.

   **Answer** Use the functions of 2.2.4: for the pentadienyl chain `huckel([(0, 1), (1, 2), (2, 3), (3, 4)], 5)`, $x = 1.732, 1, 0, -1, -1.732$; the cation has 4 electrons filling the first two orbitals, $E_\pi - 4\alpha = 2(1.732 + 1)\beta = 5.464\beta$, and `charge` is $(+\frac13, 0, +\frac13, 0, +\frac13)$. For benzene `huckel([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0)], 6)`, $x = 2, 1, 1, -1, -1, -2$, $E_\pi - 6\alpha = 2(2 + 1 + 1)\beta = 8\beta$, and the delocalization energy is $8\beta - 6\beta = 2\beta$.
