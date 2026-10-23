---
title: Electrolyte Solutions
description: Ionic conductors and Faraday's laws of electrolysis; electric mobility, transport numbers and the Hittorf method; conductivity, molar conductivity and Kohlrausch's law; the law of independent migration of ions and applications of conductometry; the chemical potential of electrolytes, mean ionic activity coefficients and ionic strength; Debye–Hückel theory from the linearized Poisson–Boltzmann equation, and the Debye–Hückel–Onsager theory of conductivity.
source_hash: 828f8cb72437
---

Electrochemistry studies the interconversion of chemical and electrical energy. Its history is almost as long as that of electricity itself: Galvani (1791) observed "animal electricity" in a frog's leg; Volta (1800) built the first sustained source of current from a pile of zinc and copper disks separated by brine-soaked cardboard; Faraday (1833–1834) found that the amount of product in electrolysis is proportional to the quantity of electricity passed; Kohlrausch (1875–1879) measured the conductivity of a great many solutions; Arrhenius (1884–1887) proposed the theory of electrolytic dissociation; Nernst (1889) related the cell potential to the Gibbs energy of the cell reaction; and Tafel (1905) gave the empirical relation between overpotential and current. An electrochemical system consists of an electrolyte, two electrodes and an external circuit. These correspond to this chapter, to [6.3.13](/6.3.13) (the equilibrium at the electrode–solution interface at zero current) and to [6.3.14](/6.3.14) (the kinetics of electrode processes when current flows).

This chapter studies the electrolyte solution itself. It has two kinds of properties. The transport properties concern the migration of ions in an electric field (12.2) and the conduction of current by the solution (12.3–12.5). The thermodynamic properties concern the deviation from ideality: electrostatic interactions between ions make an electrolyte solution markedly nonideal even when it is very dilute (12.6), and the Debye–Hückel theory explains this deviation quantitatively from electrostatics and statistical mechanics (12.7). The former is the specialization to ionic conductors of the **electrical conductivity** and **Ohm's law** of [5.3.5](/5.3.5); the latter extends the **activity** and **activity coefficient** of [6.3.6](/6.3.6) to electrolytes. Mathematically, 12.7 uses the **Poisson equation** of [2.5.1](/2.5.1), the **Boltzmann distribution** of [5.2.1](/5.2.1), and the solution of a second-order ordinary differential equation in **spherical coordinates** ([2.4.9](/2.4.9)). These results also underlie biophysics: intracellular and body fluids are electrolyte solutions with an ionic strength of about $0.15\,\mathrm{mol\,kg^{-1}}$, and the ionic atmosphere and Debye screening around proteins and nucleic acids govern the electrostatic interactions between biomacromolecules.

## 12.1. Electrochemical Systems and Faraday's Laws

### 12.1.1. Two Kinds of Conductors and Electrolytes

**Definition 12.1.1** A conductor in which current is carried by the directed motion of free electrons (or holes) is called an **electronic conductor** (conductor of the first kind), for example a metal, graphite or certain metal oxides. A conductor in which current is carried by the directed motion of ions is called an **ionic conductor** (conductor of the second kind), for example an electrolyte solution, a molten salt or a solid electrolyte.

The conductivities of the two kinds of conductors depend on temperature in opposite ways. The resistivity of a metal increases with temperature (lattice vibrations scatter electrons more strongly), whereas the conductivity of an electrolyte solution increases with temperature (the viscosity of the solvent falls and the ions move faster; the increase is about 2% per kelvin). When current passes from an electronic conductor into an ionic conductor, the charge carriers must be converted at the interface, and this can happen only through an electrode reaction. This is the distinguishing feature of electrochemistry.

**Definition 12.1.2** A substance that dissociates completely or partially into ions when dissolved in a solvent (or melted) is called an **electrolyte**. One that is completely dissociated in solution (over the usual concentration range) is called a **strong electrolyte**, for example $\ce{HCl}$, $\ce{NaOH}$ and most salts. One that is only partially dissociated, so that a dissociation equilibrium exists between ions and undissociated molecules, is called a **weak electrolyte**, for example $\ce{CH3COOH}$ and $\ce{NH3(aq)}$.

Strong and weak are not intrinsic properties of a substance but also depend on the solvent: $\ce{HCl}$ is a strong electrolyte in water and a weak one in glacial acetic acid. The extent of dissociation of a weak electrolyte is described by the **degree of ionization** ([6.1.9](/6.1.9)). The fundamental thermodynamic difference between electrolyte and nonelectrolyte solutions is the long-range electrostatic interaction between ions: a $0.01\,\mathrm{mol\,kg^{-1}}$ sucrose solution is almost ideal, whereas the mean activity coefficient of $\ce{CaCl2}$ at the same molality is only 0.73 (12.6).

### 12.1.2. Naming of Electrodes and the Mechanism of Conduction

By IUPAC convention, the electrode at which oxidation occurs is called the **anode** and the electrode at which reduction occurs is called the **cathode** ([6.1.11](/6.1.11)). A second naming scheme is based on potential: the electrode at the higher potential is the positive electrode and the one at the lower potential is the negative electrode. The two schemes correspond in opposite ways in a **galvanic cell** and in an **electrolytic cell**: the negative electrode of a galvanic cell is its anode, whereas the positive electrode of an electrolytic cell is its anode. In this course, anode and cathode are used when electrode reactions are discussed, and positive and negative electrodes when the output of a cell is discussed.

Consider the electrolysis of a $\ce{CuCl2}$ solution with a Pt anode and a Cu cathode. In the external circuit, electrons flow from the negative terminal of the power supply to the Cu electrode, where $\ce{Cu^2+ + 2e- -> Cu}$. In the solution, $\ce{Cu^2+}$ migrates toward the cathode and $\ce{Cl-}$ toward the anode. At the Pt electrode, $\ce{2Cl- -> Cl2 + 2e-}$, and the electrons return through the external circuit to the positive terminal of the power supply. The whole circuit can be written

$$
\text{source}(-) \xrightarrow{\ \mathrm{e}^-\ } \ce{Cu} \xrightarrow{\ \text{reduction}\ } \text{solution (ion migration)} \xrightarrow{\ \text{oxidation}\ } \ce{Pt} \xrightarrow{\ \mathrm{e}^-\ } \text{source}(+).
$$

Conduction through an electrolyte solution therefore consists of three processes in series: the electromigration of ions in the solution (a physical process), the electrode reactions at the two electrodes (chemical processes), and the motion of electrons in the electrodes and the external circuit (a physical process). Being in series, the three carry the same current everywhere; when several electrolytic cells are connected in series, the same quantity of electricity passes through every electrode. This is the starting point of Faraday's law below and of the Hittorf method.

### 12.1.3. Faraday's Laws of Electrolysis

An electrode reaction links a quantity of electricity to an amount of substance. Write the electrode reaction as

$$
0 = \sum_{\mathrm{B}}\nu_{\mathrm{B}}\mathrm{B} + z\,\mathrm{e}^-\ (\text{or} - z\,\mathrm{e}^-),
$$
so that $z\,\mathrm{mol}$ of electrons pass through the electrode when the extent of reaction is $1\,\mathrm{mol}$.

**Theorem 12.1.1 (Faraday's Laws of Electrolysis)** The quantity of electricity $Q$ passing through an electrode is proportional to the **extent of reaction** $\xi$ of the electrode reaction:

$$
Q = zF\xi, \qquad n_{\mathrm{B}} = \lvert\nu_{\mathrm{B}}\rvert\,\frac{Q}{zF}, \qquad m_{\mathrm{B}} = \lvert\nu_{\mathrm{B}}\rvert\,\frac{M_{\mathrm{B}}Q}{zF},
$$
where $F$ is the **Faraday constant** and $Q = \int_0^t I\,\mathrm{d}t$ ($Q = It$ for a constant current).

[6.1.12](/6.1.12) gave the elementary form $n_{\mathrm{B}} = Q/(zF)$ of this law; written in terms of the extent of reaction, it holds for any stoichiometric equation. Faraday established the law step by step in the third, fifth and seventh series of his *Experimental Researches in Electricity* (1833–1834), more than sixty years before the discovery of the electron. Today it is seen to be nothing more than conservation of charge together with the fact that each ion gains or loses an integer number of electrons. The constant is $F = N_{\mathrm{A}}e = 96\,485.332\,12\,\mathrm{C\,mol^{-1}}$, with $e = 1.602\,176\,634\times10^{-19}\,\mathrm{C}$ and $N_{\mathrm{A}} = 6.022\,140\,76\times10^{23}\,\mathrm{mol^{-1}}$; since 2019 all three are exact.

Faraday's law is subject to no restriction on temperature, pressure, concentration or electrode material; it applies to electrolytic and galvanic cells alike, and does not depend on whether the electrode reaction is reversible. If an actual electrolysis yields less product than the theoretical amount, the cause is side reactions or loss of product, not a failure of the law; the ratio of the two is the **current efficiency**. A device that measures a quantity of electricity on the basis of this law is called a coulometer. In a silver coulometer, $\ce{Ag}$ is deposited at the cathode, and each gram deposited corresponds to $96\,485/107.868 = 894.5\,\mathrm{C}$.

The energy required for electrolysis is determined by thermodynamics. For the chlor-alkali process $\ce{2NaCl + 2H2O -> 2NaOH + H2 + Cl2}$ (in aqueous solution), $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = 422\,\mathrm{kJ\,mol^{-1}}$ (298 K, $z = 2$), and the electrical work $W' = QU$ done on the system ($U$ is the cell voltage) must be at least $\xi\Delta_{\mathrm{r}}G_{\mathrm{m}}$ ([6.3.13](/6.3.13)). The quantity of electricity is given by Faraday's law, the cell voltage by thermodynamics and electrode kinetics ([6.3.14](/6.3.14)), and the product of the two is the electrical energy consumed.

### 12.1.4. Elementary Entities Carrying One Elementary Charge

The amount of substance $n = N/N_{\mathrm{A}}$ depends on the elementary entity chosen: $18\,\mathrm{g}$ of water is $n(\ce{H2O}) = 1\,\mathrm{mol}$ and also $n(\tfrac12\ce{H2O}) = 2\,\mathrm{mol}$. In discussing the conduction of electrolyte solutions it is customary to take as the elementary entity a particle that carries one elementary charge:

- for the ions $\ce{M^{z+}}$ and $\ce{A^{z-}}$, take $\tfrac{1}{z_+}\ce{M^{z+}}$ and $\tfrac{1}{\lvert z_-\rvert}\ce{A^{z-}}$, for example $\ce{H+}$, $\tfrac12\ce{Cu^2+}$, $\tfrac13\ce{Fe^3+}$, $\tfrac12\ce{SO4^2-}$;
- for a substance taking part in an electrode reaction, take the amount that gains or loses one electron, for example $\tfrac12\ce{Cu}$ and $\tfrac12\ce{Cl2}$ in the electrolysis of $\ce{CuCl2}$;
- for an electrolyte $\ce{M_{\nu_+}A_{\nu_-}}$, take $\tfrac{1}{\nu_+z_+}\ce{M_{\nu_+}A_{\nu_-}}$, for example $\ce{KCl}$, $\tfrac12\ce{Na2SO4}$, $\tfrac13\ce{AlCl3}$.

With this choice, $1\,\mathrm{mol}$ of any such entity corresponds to $1\,\mathrm{mol}$ of elementary charge, that is, a quantity of electricity $F$; the amounts of the entities reacting at the two electrodes are equal; and for complete dissociation $n(\tfrac12\ce{Na2SO4}) = n(\ce{Na+}) = n(\tfrac12\ce{SO4^2-})$. In older literature this entity was called the "equivalent". Its advantage is that every $z$ in the formulas becomes 1; the price is that the entity must always be stated: $\Lambda_{\mathrm{m}}(\ce{CuSO4}) = 2\Lambda_{\mathrm{m}}(\tfrac12\ce{CuSO4})$ (12.3.2).

## 12.2. Electromigration of Ions

### 12.2.1. Three Modes of Mass Transport in Solution

Species B is transported in solution in three ways, each of which can be expressed through the flux density $\boldsymbol{J}_{\mathrm{B}}$ (the amount of substance crossing unit area per unit time, in $\mathrm{mol\,m^{-2}\,s^{-1}}$):

| Mode | Driving force | Flux density |
|---|---|---|
| Convection | Bulk motion of the solution (stirring, density differences) | $\boldsymbol{J} = c_{\mathrm{B}}\boldsymbol{v}$, with $\boldsymbol{v}$ the flow velocity |
| Diffusion | Concentration gradient (chemical potential gradient) | $\boldsymbol{J} = -D_{\mathrm{B}}\nabla c_{\mathrm{B}}$ (**Fick's law**, [5.2.2](/5.2.2), [2.5.1](/2.5.1)) |
| Electromigration | Electric field | $\boldsymbol{J} = \operatorname{sgn}(z_{\mathrm{B}})\,c_{\mathrm{B}}u_{\mathrm{B}}\boldsymbol{E}$ |

The sum of the three terms is the Nernst–Planck equation for dilute solutions. This chapter treats electromigration, driven by the electric field. The role of diffusion near an electrode (concentration polarization) is treated in [6.3.14](/6.3.14); in nonequilibrium thermodynamics, diffusion and electromigration are unified as being driven by the gradient of the electrochemical potential ([6.3.18](/6.3.18)).

### 12.2.2. Electric Mobility

**Definition 12.2.1** The directed motion of ions in a solution under an electric field is called the **electromigration** of the ions. At a given temperature, pressure and solution composition, the magnitude $v_{\mathrm{B}}$ of the migration velocity of ion B is proportional to the electric field strength $E$, and the proportionality coefficient

$$
u_{\mathrm{B}} = \frac{v_{\mathrm{B}}}{E}
$$
is called the **electric mobility** of ion B (formerly the ionic mobility), with unit $\mathrm{m^2\,V^{-1}\,s^{-1}}$: the migration velocity of the ion in a unit field.

Here $v_{\mathrm{B}}$ is the **drift velocity** of the ion. In solution an ion is accelerated by the electric force $\lvert z_{\mathrm{B}}\rvert eE$ and at the same time experiences the viscous drag of the solvent; when the two balance, the ion moves at constant speed. Approximating the ion as a rigid sphere of radius $r$, the drag is given by Stokes' formula $6\pi\eta rv$ ([5.1.2](/5.1.2); $\eta$ is the **viscosity** of the solvent), so that

$$
u_{\mathrm{B}} = \frac{\lvert z_{\mathrm{B}}\rvert e}{6\pi\eta r}. \tag{12.1}
$$
The mobility thus increases with the charge number and decreases with the ionic radius and the solvent viscosity; when the temperature rises, $\eta$ falls and $u_{\mathrm{B}}$ increases.

The mobility $u_{\mathrm{B}}$ is not a characteristic constant of ion B: it also depends on the solvent, the temperature and the concentration, and the higher the concentration, the more the electrostatic interaction between ions slows the migration (12.7.6). The limiting value $u^\infty_{\mathrm{B}}$ as the concentration tends to zero is called the limiting electric mobility; at that point the interaction between ions vanishes and strong and weak electrolytes no longer differ. In a given solvent at a given temperature, $u^\infty_{\mathrm{B}}$ is a characteristic parameter of ion B, independent of the other ions present, and can be looked up in tables. In solutions of weak electrolytes and sparingly soluble salts the ion concentrations are low, and one may approximate $u_{\mathrm{B}} \approx u^\infty_{\mathrm{B}}$.

| Ion ($25\,^\circ\mathrm{C}$, water) | $\ce{H+}$ | $\ce{Li+}$ | $\ce{Na+}$ | $\ce{K+}$ | $\ce{Ag+}$ | $\ce{Ca^2+}$ | $\ce{OH-}$ | $\ce{Cl-}$ | $\ce{NO3-}$ | $\ce{CH3COO-}$ | $\ce{SO4^2-}$ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| $u^\infty/(10^{-8}\,\mathrm{m^2\,V^{-1}\,s^{-1}})$ | 36.24 | 4.01 | 5.19 | 7.62 | 6.42 | 6.16 | 20.5 | 7.91 | 7.40 | 4.24 | 8.29 |

(Converted from the limiting ionic molar conductivities in the CRC Handbook by $u^\infty = \lambda^\infty/(\lvert z\rvert F)$; see 12.4.2.) In a field of $1\,\mathrm{V\,cm^{-1}}$, a $\ce{K+}$ ion moves only about $8\,\mu\mathrm{m}$ per second, far less than the speed of its thermal motion; electromigration is a small drift superimposed on random thermal motion.

**Example 12.2.1** From Eq. (12.1) and $\eta(\ce{H2O}, 25\,^\circ\mathrm{C}) = 0.890\,\mathrm{mPa\,s}$, estimate the effective radii of $\ce{Li+}$, $\ce{Na+}$ and $\ce{K+}$ and compare them with the crystal ionic radii (0.076, 0.102 and 0.138 nm).

**Solution** $r = e/(6\pi\eta u^\infty)$. For $\ce{Na+}$,

$$
r = \frac{1.602\times10^{-19}\,\mathrm{C}}{6\pi \times 0.890\times10^{-3}\,\mathrm{Pa\,s}\times5.19\times10^{-8}\,\mathrm{m^2\,V^{-1}\,s^{-1}}} = 1.84\times10^{-10}\,\mathrm{m} = 0.184\,\mathrm{nm};
$$
similarly, 0.238 nm for $\ce{Li+}$ and 0.125 nm for $\ce{K+}$. The smaller the crystal radius, the larger the effective ("Stokes") radius: the order is completely reversed. A small ion has a strong electric field, binds many water molecules, and moves through the solution dragging a large hydration shell. The estimate is only qualitative, because Stokes' formula was derived for macroscopic spheres and gives only the order of magnitude for ions as small as solvent molecules. $\square$

### 12.2.3. Transport Numbers

In a solution, current is carried by positive and negative ions together, each carrying a different share.

**Definition 12.2.2** The fraction of the total charge $Q$ passing through the solution that is carried by ion B,

$$
t_{\mathrm{B}} = \frac{Q_{\mathrm{B}}}{Q} = \frac{I_{\mathrm{B}}}{I},
$$
is called the **transport number** of ion B. The transport numbers of all the ions in a solution sum to 1.

**Theorem 12.2.1** In a solution containing a single electrolyte (dissociating into $\ce{M^{z+}}$ and $\ce{A^{z-}}$),

$$
t_+ = \frac{u_+}{u_+ + u_-}, \qquad t_- = \frac{u_-}{u_+ + u_-}.
$$
More generally, in a solution containing several ions, $t_{\mathrm{B}} = \lvert z_{\mathrm{B}}\rvert c_{\mathrm{B}}u_{\mathrm{B}}\big/\sum_i \lvert z_i\rvert c_i u_i$.

**Proof** Consider the solution between two parallel electrodes of cross-sectional area $A$ separated by a distance $l$, with a voltage $U$ between them, so that the field strength is $E = U/l$. The amount of positive ions crossing any cross section per unit time is $c_+v_+A$, and each mole of positive ions carries a charge $z_+F$, so the current carried by the positive ions is $I_+ = z_+Fc_+u_+EA$. Likewise $I_- = \lvert z_-\rvert Fc_-u_-EA$ (the negative ions move in the opposite direction, but the current they carry has the same direction as that of the positive ions). By electroneutrality, $z_+c_+ = \lvert z_-\rvert c_-$, hence

$$
t_+ = \frac{I_+}{I_+ + I_-} = \frac{z_+c_+u_+}{z_+c_+u_+ + \lvert z_-\rvert c_-u_-} = \frac{u_+}{u_+ + u_-}.
$$
With several kinds of ions the factors $\lvert z_i\rvert c_i$ no longer cancel, and the general expression follows directly. $\square$

Like the mobility, the transport number depends on concentration, temperature and solvent, and also on the other ions present; it can be determined only by experiment (12.2.4 and 12.2.5, and the potentiometric method of [6.3.13](/6.3.13)). It directly determines the concentration changes near the two electrodes during electrolysis, and also the liquid junction potential ([6.3.13](/6.3.13)): $\ce{KCl}$ has $t_+ \approx t_- \approx 0.5$, which is why it is used in salt bridges.

### 12.2.4. The Hittorf Method

Imagine an electrolytic cell divided into an anode compartment, a middle compartment and a cathode compartment, each containing $5\,\mathrm{mol}$ (in terms of the elementary entity) of a 1-1 electrolyte. The mobility of the cation is three times that of the anion, and a quantity of electricity of $4\,\mathrm{mol}$ of elementary charge ($4F$) is passed. The electrodes do not dissolve and take no part in the ionic equilibrium (for example, only the anion is oxidized at the anode and only the cation is reduced at the cathode). The same quantity of electricity $4F$ passes through any cross section, of which $3F$ is carried by cations migrating toward the cathode and $1F$ by anions migrating toward the anode:

| | Anode compartment | Middle compartment | Cathode compartment |
|---|---|---|---|
| Electrode reaction | Anion oxidized, $4\,\mathrm{mol}$ | — | Cation reduced, $4\,\mathrm{mol}$ |
| Migration in | Anion $+1$ | Unchanged | Cation $+3$ |
| Migration out | Cation $-3$ | Unchanged | Anion $-1$ |
| Change in electrolyte | $5 \to 2$ (decrease of 3, equal to the cations leaving) | $5$ | $5 \to 4$ (decrease of 1, equal to the anions leaving) |

We see that the concentration in the middle compartment is unchanged; for each ion, the amount transported differs from the amount reacting at the electrode; and the decrease of electrolyte in each electrode compartment equals the amount of ions leaving it (conservation of matter plus electroneutrality). Measuring the change in the amount of electrolyte in one electrode compartment therefore gives the transport number.

**Definition 12.2.3** The method in which a solution of an electrolyte of known concentration is electrolyzed in a transference tube, the change in composition of the solution in the cathode (or anode) compartment is analyzed after the current has passed, and the transport number is calculated from it and from the quantity of electricity measured by a coulometer in series, is called the **Hittorf method**.

For ion B in the cathode compartment (a cation reduced at the cathode), the material balance is

$$
n_{\text{final}} = n_{\text{initial}} + n_{\text{migr}} - n_{\text{el}}, \qquad t_{\mathrm{B}} = \frac{n_{\text{migr}}}{n_{\text{el}}},
$$
where $n_{\text{el}} = Q/F$ is expressed in terms of the elementary entity carrying one elementary charge. For an ion that does not take part in the electrode reaction, drop the $n_{\text{el}}$ term and take the amount migrating out with a negative sign.

**Example 12.2.2** In a Hittorf transference tube, a $\ce{CuSO4}$ solution is electrolyzed between Cu electrodes. After some time, $0.0405\,\mathrm{g}$ of Ag has been deposited in a silver coulometer connected in series. The cathode compartment contained $1.1276\,\mathrm{g}$ of $\ce{CuSO4}$ before electrolysis and $1.1090\,\mathrm{g}$ after (in the same mass of water). Find $t(\ce{Cu^2+})$ and $t(\ce{SO4^2-})$.

**Solution** Take $\tfrac12\ce{Cu^2+}$ and $\tfrac12\ce{CuSO4}$ as the elementary entities, with $M(\tfrac12\ce{CuSO4}) = 79.80\,\mathrm{g\,mol^{-1}}$:

$$
n_{\text{el}} = \frac{0.0405}{107.87} = 3.754\times10^{-4}\,\mathrm{mol}, \quad n_{\text{initial}} = \frac{1.1276}{79.80} = 1.4130\times10^{-2}\,\mathrm{mol}, \quad n_{\text{final}} = \frac{1.1090}{79.80} = 1.3897\times10^{-2}\,\mathrm{mol}.
$$
The cathode reaction $\tfrac12\ce{Cu^2+ + e- -> 1/2Cu}$ decreases the amount of $\ce{Cu^2+}$, and migration increases it: $n_{\text{migr}} = n_{\text{final}} - n_{\text{initial}} + n_{\text{el}} = (-2.33 + 3.754)\times10^{-4} = 1.42\times10^{-4}\,\mathrm{mol}$, so

$$
t(\ce{Cu^2+}) = \frac{1.42\times10^{-4}}{3.754\times10^{-4}} = 0.38, \qquad t(\ce{SO4^2-}) = 1 - 0.38 = 0.62. \qquad \square
$$

The errors of the Hittorf method come mainly from convection and diffusion, which mix the electrode compartments, and from solvation: ions carry water of hydration as they migrate, so the measured transport number is an "apparent" one referred to the solvent.

### 12.2.5. The Moving Boundary Method

**Definition 12.2.4** The method in which two electrolyte solutions with a common ion form a sharp boundary in a vertical narrow tube (for example $\ce{CdCl2}$ below and $\ce{HCl}$ above), the distance moved by the boundary in a given time is measured after current is passed, and the transport number is calculated from it, is called the **moving boundary method**.

Let the concentration of the ion under study, $\ce{H+}$, in the upper solution be $c$, and let the volume swept by the boundary when a quantity of electricity $Q$ has passed be $V$. All the $\ce{H+}$ in this volume has then crossed a fixed cross section, carrying a charge $z_+cVF$, so that

$$
t_+ = \frac{z_+cVF}{Q}.
$$
The boundary stays sharp if the mobility of the indicator ion ($\ce{Cd^2+}$) is smaller than that of the ion under study. If the indicator ion lags behind, the resistance below the boundary and hence the field there increase, so that it speeds up and catches up; if it gets ahead, it enters a region of smaller field and slows down. This automatic "sharpening" makes the moving boundary method more accurate than the Hittorf method, and most modern transport number data are measured this way.

## 12.3. Conductance, Conductivity and Molar Conductivity

### 12.3.1. Conductance and Conductivity

For metallic conductors the resistance $R$ is customarily used to express the ability to conduct; for electrolyte solutions its reciprocal, the **electrical conductance** $G = 1/R$ (unit S), is customary. For a uniform conductor of cross-sectional area $A$ and length $l$, $G = \sigma A/l$, where $\sigma$ is the **electrical conductivity** of [5.3.5](/5.3.5) (unit $\mathrm{S\,m^{-1}}$). It is the reciprocal of the **resistivity** and equals the conductance of a cube of solution with $1\,\mathrm{m}$ edges between two opposite faces. The chemical literature often denotes the conductivity by $\kappa$; this book follows physics and writes $\sigma$.

The relation between conductivity and mobility follows from the expression for the current in 12.2.3: $I = \sum_{\mathrm{B}}\lvert z_{\mathrm{B}}\rvert Fc_{\mathrm{B}}u_{\mathrm{B}}EA$. Comparing with $I = \sigma EA$ (the differential form of **Ohm's law**, $\boldsymbol{J} = \sigma\boldsymbol{E}$) gives

$$
\sigma = F\sum_{\mathrm{B}}\lvert z_{\mathrm{B}}\rvert c_{\mathrm{B}}u_{\mathrm{B}}. \tag{12.2}
$$
This has exactly the same structure as $\sigma = ne\mu_{\mathrm{e}}$ for metals: conductivity = carrier concentration × charge × mobility, except that a solution has two or more kinds of carriers. The conductivity thus depends on the number of ions and on how fast they move. The conductivity of a strong electrolyte first increases with concentration (more ions) and then decreases (interactions between ions reduce $u$, and in concentrated solutions ion association also occurs), passing through a maximum at some concentration (about 30% by mass for $\ce{H2SO4}$). The conductivity of a weak electrolyte is small and changes little with concentration, because the degree of ionization falls as the concentration increases.

| Conductor | $\sigma/(\mathrm{S\,m^{-1}})$ (room temperature, order of magnitude) |
|---|---|
| Pure water | $5.5\times10^{-6}$ (from the self-dissociation of water only) |
| Natural water, drinking water | $10^{-3}$–$10^{-1}$ |
| Aqueous electrolytes ($0.01$–$1\,\mathrm{mol\,L^{-1}}$ salts, acids, bases) | $10^{-1}$–$10^{2}$; seawater about 5 |
| Organic electrolyte of lithium-ion batteries ($\ce{LiPF6}$ in carbonate solvents) | about 1 |
| Ionic liquids | $10^{-2}$–$1$ |
| Polymer electrolytes (e.g., PEO–lithium salt, room temperature) | $10^{-5}$–$10^{-2}$ |
| Inorganic solid electrolytes ($\alpha$-$\ce{AgI}$, sulfide lithium-ion conductors, YSZ at high temperature) | $10^{-2}$–$10^{2}$ |
| Molten salts (e.g., molten $\ce{KCl}$) | $10^{2}$ |
| Metals | $10^{6}$–$10^{8}$ |

### 12.3.2. Molar Conductivity

The conductivity varies with concentration and is therefore inconvenient for comparing the conducting power of different electrolytes. We reduce it to $1\,\mathrm{mol}$ of electrolyte:

**Definition 12.3.1** The ratio of the conductivity of an electrolyte solution to the amount concentration of the electrolyte,

$$
\Lambda_{\mathrm{m}} = \frac{\sigma}{c},
$$
is called the **molar conductivity** of the electrolyte, with unit $\mathrm{S\,m^2\,mol^{-1}}$ ($c$ in $\mathrm{mol\,m^{-3}}$). It is the conductance of a solution containing $1\,\mathrm{mol}$ of electrolyte placed between two large parallel plate electrodes $1\,\mathrm{m}$ apart.

The value of $\Lambda_{\mathrm{m}}$ depends on the elementary entity chosen, which must be stated: $\Lambda_{\mathrm{m}}(\ce{CuSO4}) = 2\Lambda_{\mathrm{m}}(\tfrac12\ce{CuSO4})$. To compare electrolytes of different valence types, one usually takes entities carrying one elementary charge (12.1.4). Tabulated data are often given in $\mathrm{S\,cm^2\,mol^{-1}}$, with $1\,\mathrm{S\,cm^2\,mol^{-1}} = 10^{-4}\,\mathrm{S\,m^2\,mol^{-1}}$; in conversions, mind the unit of $c$: $c = 0.01\,\mathrm{mol\,L^{-1}} = 10\,\mathrm{mol\,m^{-3}}$.

By Eq. (12.2), for an electrolyte $\ce{M_{\nu_+}A_{\nu_-}}$ with degree of dissociation $\alpha$, $c_+ = \nu_+\alpha c$ and $c_- = \nu_-\alpha c$; taking $\tfrac{1}{\nu_+z_+}\ce{M_{\nu_+}A_{\nu_-}}$ as the entity, $\nu_+z_+ = 1$ and

$$
\Lambda_{\mathrm{m}} = \alpha(u_+ + u_-)F. \tag{12.3}
$$
Here $\alpha$ reflects the number of ions and $u_+ + u_-$ how fast they migrate. For a strong electrolyte $\alpha = 1$ and the variation of $\Lambda_{\mathrm{m}}$ with concentration comes entirely from $u$; for a weak electrolyte the variation comes mainly from $\alpha$. The common statement that "molar conductivity is the conductance of a solution containing $1\,\mathrm{mol}$ each of positive and negative ions" holds only for 1-1 strong electrolytes.

### 12.3.3. Measurement of Conductance

Conductance is measured with a conductivity cell: two parallel platinum electrodes are immersed in the solution under study, and its resistance is measured with a Wheatstone bridge or a conductivity meter. Alternating current must be used (usually about $1\,\mathrm{kHz}$): direct current would cause electrolysis and polarization at the electrodes ([6.3.14](/6.3.14)) and generate a back emf between them. Coating the platinum with platinum black increases the true surface area and lowers the current density, which further reduces polarization.

**Definition 12.3.2** The ratio $K_{\mathrm{cell}} = l/A$ of the distance $l$ between the two electrodes of a conductivity cell to the electrode area $A$ is called the **cell constant**. Since $\sigma = K_{\mathrm{cell}}/R$, measuring the resistance gives the conductivity.

The effective electrode area and the distribution of field lines are hard to measure directly, so $K_{\mathrm{cell}}$ is calibrated with a standard solution of known conductivity, usually $\ce{KCl}$ (at $25\,^\circ\mathrm{C}$, a $0.0100\,\mathrm{mol\,L^{-1}}$ $\ce{KCl}$ solution has $\sigma = 0.1413\,\mathrm{S\,m^{-1}}$). Modern conductivity meters have built-in calibration and temperature compensation and read $\sigma$ directly.

**Example 12.3.1** At $25\,^\circ\mathrm{C}$, a conductivity cell filled with $0.0100\,\mathrm{mol\,L^{-1}}$ $\ce{KCl}$ has a resistance of $484.0\,\Omega$. Filled with a $0.00500\,\mathrm{mol\,L^{-1}}$ solution of $\tfrac12\ce{K2SO4}$ (that is, $0.00250\,\mathrm{mol\,L^{-1}}$ $\ce{K2SO4}$), its resistance is $1101\,\Omega$. Find the cell constant and $\Lambda_{\mathrm{m}}(\tfrac12\ce{K2SO4})$.

**Solution** $K_{\mathrm{cell}} = \sigma R = 0.1413 \times 484.0\,\mathrm{m^{-1}} = 68.39\,\mathrm{m^{-1}}$. For the solution under study, $\sigma = 68.39/1101\,\mathrm{S\,m^{-1}} = 0.06212\,\mathrm{S\,m^{-1}}$, so

$$
\Lambda_{\mathrm{m}}(\tfrac12\ce{K2SO4}) = \frac{0.06212\,\mathrm{S\,m^{-1}}}{5.00\,\mathrm{mol\,m^{-3}}} = 1.242\times10^{-2}\,\mathrm{S\,m^2\,mol^{-1}} = 124.2\,\mathrm{S\,cm^2\,mol^{-1}},
$$
while $\Lambda_{\mathrm{m}}(\ce{K2SO4}) = 248.4\,\mathrm{S\,cm^2\,mol^{-1}}$. (At infinite dilution $\lambda^\infty(\ce{K+}) + \lambda^\infty(\tfrac12\ce{SO4^2-}) = 153.5\,\mathrm{S\,cm^2\,mol^{-1}}$; the value at finite concentration is smaller, for the reason given in 12.7.6.) $\square$

### 12.3.4. Dependence of Molar Conductivity on Concentration

Kohlrausch measured the molar conductivity of many electrolytes at different concentrations and found that strong and weak electrolytes behave quite differently (figure below).

**Theorem 12.3.1 (Kohlrausch's Square-Root Law)** In dilute solutions of strong electrolytes (roughly $c < 0.01\,\mathrm{mol\,L^{-1}}$), the molar conductivity is a linear function of the square root of the concentration:

$$
\Lambda_{\mathrm{m}} = \Lambda^\infty_{\mathrm{m}} - \mathcal{A}\sqrt{c},
$$
where $\mathcal{A}$ is a constant depending on the electrolyte, the solvent and the temperature.

This was originally an empirical law; its theoretical explanation, including the value of $\mathcal{A}$, is given by the Debye–Hückel–Onsager theory (12.7.6): the appearance of $\sqrt c$ reflects the radius of the ionic atmosphere, $\lambda_{\mathrm{D}} \propto c^{-1/2}$.

**Definition 12.3.3** The limit of the molar conductivity of an electrolyte as the concentration tends to zero, $\Lambda^\infty_{\mathrm{m}} = \lim_{c\to0}\Lambda_{\mathrm{m}}$, is called the **limiting molar conductivity** (molar conductivity at infinite dilution) of the electrolyte.

$\Lambda^\infty_{\mathrm{m}}$ is the conducting power of $1\,\mathrm{mol}$ of electrolyte when there is no interaction between ions, and in a given solvent at a given temperature it is a characteristic parameter of the electrolyte. For a strong electrolyte, one plots data for dilute solutions against $\sqrt c$, fits a straight line by **least squares** ([3.3](/3.3)) and extrapolates to $c = 0$ to obtain $\Lambda^\infty_{\mathrm{m}}$. This fails for a weak electrolyte: its $\Lambda_{\mathrm{m}}$ rises steeply in dilute solution as $c$ decreases (the degree of ionization tends to 1), and in the concentration range that can be measured accurately it is nowhere near the limit, so extrapolation has no basis. The $\Lambda^\infty_{\mathrm{m}}$ of a weak electrolyte must be obtained from the law of independent migration of ions (12.4).

![Molar conductivity of aqueous solutions at 25 °C. Left: experimental values (CRC) for HCl, KCl and NaCl divided by the extrapolated limiting values and plotted against √c; points with c ≤ 0.01 mol/L are extrapolated by a least-squares line (solid), and the dashed lines are the limiting slopes of Onsager's theory. Right: the molar conductivity of acetic acid (computed from Ostwald's dilution law) rises steeply in dilute solution, far from the limiting value of 390.6 S cm² mol⁻¹, and cannot be extrapolated](./plots/molar-conductivity.py)

## 12.4. The Law of Independent Migration of Ions

### 12.4.1. Ionic Molar Conductivity and Independent Migration

Kohlrausch compared the limiting molar conductivities of electrolytes with a common ion and found that their differences do not depend on the common ion:

| Electrolyte pair | $\Lambda^\infty_{\mathrm{m}}/(\mathrm{S\,cm^2\,mol^{-1}})$ | Difference | Electrolyte pair | $\Lambda^\infty_{\mathrm{m}}/(\mathrm{S\,cm^2\,mol^{-1}})$ | Difference |
|---|---|---|---|---|---|
| $\ce{KCl}$ / $\ce{LiCl}$ | 149.8 / 115.0 | 34.8 | $\ce{HCl}$ / $\ce{HNO3}$ | 426.0 / 421.1 | 4.9 |
| $\ce{KNO3}$ / $\ce{LiNO3}$ | 144.9 / 110.1 | 34.8 | $\ce{KCl}$ / $\ce{KNO3}$ | 149.8 / 144.9 | 4.9 |
| $\ce{KClO4}$ / $\ce{LiClO4}$ | 140.8 / 106.0 | 34.8 | $\ce{LiCl}$ / $\ce{LiNO3}$ | 115.0 / 110.1 | 4.9 |

Whatever the anion, the difference between $\ce{K+}$ and $\ce{Li+}$ is always 34.8; whatever the cation, the difference between $\ce{Cl-}$ and $\ce{NO3-}$ is always 4.9. This shows that in infinitely dilute solutions each ion makes an independent contribution to the conduction.

**Definition 12.4.1** The ratio of the contribution $\sigma_{\mathrm{B}} = \lvert z_{\mathrm{B}}\rvert Fc_{\mathrm{B}}u_{\mathrm{B}}$ of ion B to the conductivity of an electrolyte solution to its concentration,

$$
\lambda_{\mathrm{B}} = \frac{\sigma_{\mathrm{B}}}{c_{\mathrm{B}}} = \lvert z_{\mathrm{B}}\rvert Fu_{\mathrm{B}},
$$
is called the **ionic molar conductivity** of ion B; its value at infinite dilution, $\lambda^\infty_{\mathrm{B}}$, is called the limiting ionic molar conductivity. Expressed for an entity carrying one elementary charge, $\lambda(\tfrac{1}{\lvert z\rvert}\mathrm{B}) = Fu_{\mathrm{B}}$.

From $\sigma = \sum\sigma_{\mathrm{B}}$ we immediately obtain the additivity of molar conductivities: for a completely dissociated $\ce{M_{\nu_+}A_{\nu_-}}$, $\Lambda_{\mathrm{m}} = \nu_+\lambda_+ + \nu_-\lambda_-$. This holds at any concentration, except that at finite concentration $\lambda_{\mathrm{B}}$ depends on the other ions in the solution; at infinite dilution this dependence disappears.

**Theorem 12.4.1 (Law of Independent Migration of Ions)** In a given solvent at a given temperature, the ions in an infinitely dilute solution migrate independently without affecting one another: the limiting molar conductivity $\lambda^\infty_{\mathrm{B}}$ of each ion is a fixed value independent of the other ions present, and the limiting molar conductivity of an electrolyte $\ce{M_{\nu_+}A_{\nu_-}}$ is

$$
\Lambda^\infty_{\mathrm{m}} = \nu_+\lambda^\infty_+ + \nu_-\lambda^\infty_-.
$$

The contributions of the individual ions can be separated by means of the transport numbers. For a strong electrolyte, by Theorem 12.2.1,

$$
t_+ = \frac{u_+}{u_+ + u_-} = \frac{\nu_+\lambda_+}{\Lambda_{\mathrm{m}}}, \qquad \lambda_+ = \frac{t_+\Lambda_{\mathrm{m}}}{\nu_+}, \quad \lambda_- = \frac{t_-\Lambda_{\mathrm{m}}}{\nu_-}.
$$
Hence, from the $\Lambda^\infty_{\mathrm{m}}$ of one electrolyte and the limiting transport numbers one obtains the $\lambda^\infty$ of both ions, and by the law of independent migration those of other electrolytes follow.

### 12.4.2. Limiting Ionic Molar Conductivities

| Cation | $\lambda^\infty/(\mathrm{S\,cm^2\,mol^{-1}})$ | Anion | $\lambda^\infty/(\mathrm{S\,cm^2\,mol^{-1}})$ |
|---|---|---|---|
| $\ce{H+}$ | 349.65 | $\ce{OH-}$ | 198.0 |
| $\ce{Li+}$ | 38.66 | $\ce{Cl-}$ | 76.31 |
| $\ce{Na+}$ | 50.08 | $\ce{Br-}$ | 78.1 |
| $\ce{K+}$ | 73.48 | $\ce{I-}$ | 76.8 |
| $\ce{NH4+}$ | 73.5 | $\ce{NO3-}$ | 71.42 |
| $\ce{Ag+}$ | 61.9 | $\ce{CH3COO-}$ | 40.9 |
| $\tfrac12\ce{Mg^2+}$ | 53.0 | $\ce{HCO3-}$ | 44.5 |
| $\tfrac12\ce{Ca^2+}$ | 59.47 | $\tfrac12\ce{SO4^2-}$ | 80.0 |
| $\tfrac12\ce{Cu^2+}$ | 53.6 | $\tfrac12\ce{CO3^2-}$ | 69.3 |

(Aqueous solutions at $25\,^\circ\mathrm{C}$, CRC Handbook.)

**Example 12.4.1** Find $\Lambda^\infty_{\mathrm{m}}$ of acetic acid at $25\,^\circ\mathrm{C}$.

**Solution** Look it up directly: $\Lambda^\infty_{\mathrm{m}}(\ce{CH3COOH}) = \lambda^\infty(\ce{H+}) + \lambda^\infty(\ce{CH3COO-}) = 349.65 + 40.9 = 390.6\,\mathrm{S\,cm^2\,mol^{-1}}$. If only electrolyte data are available, three strong electrolytes can be combined, since their $\Lambda^\infty_{\mathrm{m}}$ can all be obtained by extrapolation:

$$
\Lambda^\infty_{\mathrm{m}}(\ce{CH3COOH}) = \Lambda^\infty_{\mathrm{m}}(\ce{HCl}) + \Lambda^\infty_{\mathrm{m}}(\ce{CH3COONa}) - \Lambda^\infty_{\mathrm{m}}(\ce{NaCl}) = 426.0 + 91.0 - 126.4 = 390.6\,\mathrm{S\,cm^2\,mol^{-1}}. \qquad \square
$$

### 12.4.3. Anomalous Mobility of the Proton and Hydroxide

In the table, the $\lambda^\infty$ of $\ce{H+}$ and $\ce{OH-}$ are 3–7 times those of the other ions. Back-calculation from Eq. (12.1) gives an effective radius of only 0.026 nm for $\ce{H+}$, smaller than a hydrogen atom, which shows that it does not drift through water as a single entity. The accepted explanation is the Grotthuss mechanism (proposed in 1806; its modern form was established by molecular dynamics simulations): a hydronium ion $\ce{H3O+}$ passes a proton along a **hydrogen bond** to a neighboring water molecule, which passes another proton to the next, so that the positive charge is relayed along the hydrogen-bond network while each atom moves only a short distance. $\ce{OH-}$ is a vacancy relay in the opposite direction. The rate-limiting step is the rearrangement of the hydrogen-bond network (about 1 ps). The same mechanism allows rapid proton conduction in ice, in the proton channels of proteins (such as ATP synthase and bacteriorhodopsin) and in the proton-exchange membranes of fuel cells.

### 12.4.4. Walden's Rule

By Eq. (12.1), the limiting mobility is inversely proportional to the solvent viscosity; if the effective radius of an ion does not change with the solvent, $\lambda^\infty\eta$ is independent of the solvent.

**Property 12.4.1 (Walden's Rule)** The product of the limiting molar conductivity of an electrolyte in different solvents and the solvent viscosity is approximately constant: $\Lambda^\infty_{\mathrm{m}}\eta \approx \text{constant}$.

Walden's rule holds fairly well for large, weakly solvated ions (such as tetraalkylammonium ions) and deviates considerably for small ions, whose degree of solvation varies with the solvent; for $\ce{H+}$ and $\ce{OH-}$ in water it does not apply at all (the Grotthuss mechanism is independent of viscosity). In a given solvent, $\lambda^\infty\eta$ is also approximately constant when the temperature changes, which explains the temperature coefficient of conductivity of about 2% per kelvin: the viscosity of water falls by about 2% per kelvin. In research on ionic liquids the "Walden plot" ($\lg\Lambda_{\mathrm{m}}$ against $\lg\eta^{-1}$) is often used to judge the degree of ion dissociation in an ionic liquid.

### 12.4.5. Relations Among the Conduction Quantities

| Level | Quantity | Intrinsic (tabulable) |
|---|---|---|
| Electrolyte solution | Conductance $G$, conductivity $\sigma$ | No (depends on concentration and cell) |
| Electrolyte | Molar conductivity $\Lambda_{\mathrm{m}} = \sigma/c$ | No (depends on concentration) |
| | Limiting molar conductivity $\Lambda^\infty_{\mathrm{m}} = \sum\nu_{\mathrm{B}}\lambda^\infty_{\mathrm{B}}$ | Yes |
| Ion | Mobility $u_{\mathrm{B}}$, ionic molar conductivity $\lambda_{\mathrm{B}} = \lvert z_{\mathrm{B}}\rvert Fu_{\mathrm{B}}$, transport number $t_{\mathrm{B}}$ | No (depends on concentration and coexisting ions) |
| | Limiting mobility $u^\infty_{\mathrm{B}}$, limiting ionic molar conductivity $\lambda^\infty_{\mathrm{B}}$ | Yes |
| | Limiting transport number $t^\infty_{\mathrm{B}}$ | No (also depends on the other ion of the electrolyte) |

## 12.5. Applications of Conductometry

### 12.5.1. Degree of Ionization and Ionization Constant of a Weak Electrolyte

In a solution of a weak electrolyte the ion concentrations are low and the interaction between ions is weak, so we may take $u_{\mathrm{B}} \approx u^\infty_{\mathrm{B}}$. By Eq. (12.3), $\Lambda_{\mathrm{m}} = \alpha(u_+^\infty + u_-^\infty)F$, whereas $\Lambda^\infty_{\mathrm{m}} = (u_+^\infty + u_-^\infty)F$, hence

$$
\alpha = \frac{\Lambda_{\mathrm{m}}}{\Lambda^\infty_{\mathrm{m}}}.
$$
For a 1-1 weak electrolyte $\ce{HA <=> H+ + A-}$, substitution into the **dilution law** ([6.1.9](/6.1.9)) gives

$$
K_c = \frac{c\alpha^2}{c^\circ(1-\alpha)} = \frac{c\,\Lambda_{\mathrm{m}}^2}{c^\circ\Lambda^\infty_{\mathrm{m}}(\Lambda^\infty_{\mathrm{m}} - \Lambda_{\mathrm{m}})}.
$$
This was the experimental basis on which Arrhenius proposed the theory of electrolytic dissociation.

**Example 12.5.1** At $25\,^\circ\mathrm{C}$, a $0.0100\,\mathrm{mol\,L^{-1}}$ acetic acid solution has a conductivity of $1.63\times10^{-2}\,\mathrm{S\,m^{-1}}$ (the contribution of water already subtracted). Find the degree of ionization and the ionization constant.

**Solution** $\Lambda_{\mathrm{m}} = 1.63\times10^{-2}/10.0 = 1.63\times10^{-3}\,\mathrm{S\,m^2\,mol^{-1}} = 16.3\,\mathrm{S\,cm^2\,mol^{-1}}$, $\alpha = 16.3/390.6 = 0.0417$, and

$$
K_c = \frac{0.0100 \times 0.0417^2}{1 - 0.0417} = 1.82\times10^{-5}.
$$
Strictly speaking, this is the equilibrium constant expressed in concentrations. The **ionic strength** of the solution is $c\alpha \approx 4.2\times10^{-4}\,\mathrm{mol\,L^{-1}}$, and the Debye–Hückel limiting law (Theorem 12.7.1) gives $\lg\gamma_\pm = -0.509\sqrt{4.2\times10^{-4}} = -0.0104$. The thermodynamic ionization constant is $K_{\mathrm{a}} = K_c\gamma_\pm^2 = 1.82\times10^{-5}\times0.953 = 1.73\times10^{-5}$, within about 1% of the $1.75\times10^{-5}$ used in [6.1.9](/6.1.9). (The remaining difference is mainly because at finite concentration the $\lambda$ of the ions is slightly smaller than $\lambda^\infty$.) $\square$

### 12.5.2. Solubility and Solubility Product of Sparingly Soluble Salts

A saturated solution of a sparingly soluble salt is very dilute, so we may take $\Lambda_{\mathrm{m}} \approx \Lambda^\infty_{\mathrm{m}}$; the contribution of the water itself (of the same order of magnitude here) must be subtracted from the conductivity of the solution:

$$
c = \frac{\sigma(\text{solution}) - \sigma(\ce{H2O})}{\Lambda^\infty_{\mathrm{m}}}.
$$
From the solubility $c$ one obtains the **solubility product** ([6.1.10](/6.1.10)).

**Example 12.5.2** At $25\,^\circ\mathrm{C}$, a saturated $\ce{AgCl}$ solution has a conductivity of $1.90\times10^{-4}\,\mathrm{S\,m^{-1}}$ and the water used has a conductivity of $0.05\times10^{-4}\,\mathrm{S\,m^{-1}}$. Find $K_{\mathrm{sp}}(\ce{AgCl})$.

**Solution** $\Lambda^\infty_{\mathrm{m}}(\ce{AgCl}) = 61.9 + 76.31 = 138.2\,\mathrm{S\,cm^2\,mol^{-1}} = 1.382\times10^{-2}\,\mathrm{S\,m^2\,mol^{-1}}$,

$$
c = \frac{(1.90 - 0.05)\times10^{-4}}{1.382\times10^{-2}}\,\mathrm{mol\,m^{-3}} = 1.34\times10^{-2}\,\mathrm{mol\,m^{-3}} = 1.34\times10^{-5}\,\mathrm{mol\,L^{-1}},
$$
and $K_{\mathrm{sp}} = (c/c^\circ)^2 = 1.79\times10^{-10}$, in agreement with the $1.8\times10^{-10}$ of [6.1.10](/6.1.10). $\square$

### 12.5.3. Purity of Water and Solution Concentration

The conductivity of pure water is determined by the **ion product** of $\ce{H2O <=> H+ + OH-}$: $\sigma = [\lambda^\infty(\ce{H+}) + \lambda^\infty(\ce{OH-})]\sqrt{K_{\mathrm{w}}}\,c^\circ = 547.7\times10^{-4}\,\mathrm{S\,m^2\,mol^{-1}}\times1.0\times10^{-4}\,\mathrm{mol\,m^{-3}} = 5.5\times10^{-6}\,\mathrm{S\,m^{-1}}$ (resistivity $18.2\,\mathrm{M\Omega\,cm}$). Ultrapure water in the laboratory is judged by whether it reaches this theoretical value; ordinary distilled water, which has absorbed $\ce{CO2}$, has a conductivity of about $10^{-4}\,\mathrm{S\,m^{-1}}$.

Over a certain range, conductivity is a single-valued function of concentration and can therefore be used for on-line monitoring. The salinity of seawater is defined in oceanography through conductivity (the practical salinity scale). Atmospheric $\ce{SO2}$ can be absorbed in a $\ce{H2O2}$ solution and oxidized to $\ce{H2SO4}$ ($\ce{SO2 + H2O2 -> H2SO4}$, which in solution is $\ce{SO3^2- + H2O2 -> SO4^2- + H2O}$), and the amount of $\ce{SO2}$ is found from the increase in conductivity.

### 12.5.4. Conductometric Titration

**Definition 12.5.1** The method of determining the end point of a titration from the variation of the conductance (or conductivity) of the solution with the volume of titrant is called **conductometric titration**. The titration reaction replaces ions of different conducting power in the solution, so the conductance–volume curve consists of straight segments of different slopes, and the break is the end point.

When $\ce{HCl}$ is titrated with $\ce{NaOH}$, before the end point $\ce{H+}$ ($\lambda^\infty = 349.65$) is replaced by $\ce{Na+}$ (50.08), and the conductance falls linearly; after the end point, the excess $\ce{OH-}$ (198.0) makes it rise linearly. In the titration of acetic acid the initial conductance is very small; after $\ce{NaOH}$ is added, the $\ce{CH3COONa}$ formed is completely dissociated and the conductance rises gradually (with a slight initial dip because the common-ion effect suppresses the dissociation of acetic acid), and after the end point it rises more steeply. Conductometric titration needs no indicator and is suitable for colored or turbid solutions and for very dilute or very weak acids and bases (for which the jump in the pH titration curve is not distinct). For the segments to be straight, the titrant should be more than ten times as concentrated as the solution being titrated, or the dilution effect should be corrected by the factor $(V_0 + V)/V_0$.

![Conductometric titration curves for 100 mL of 0.0100 mol/L HCl and acetic acid titrated with 0.100 mol/L NaOH at 25 °C (computed from the limiting ionic molar conductivities and the equilibrium composition, corrected for dilution by (V₀+V)/V₀); both curves break at 10 mL](./plots/conductometric-titration.py)

## 12.6. Mean Activity and Activity Coefficient of Strong Electrolytes

### 12.6.1. Chemical Potential of an Electrolyte

By the general method of [6.3.6](/6.3.6), the **chemical potential** of electrolyte B in solution is written $\mu_{\mathrm{B}} = \mu^\circ_{\mathrm{B}} + RT\ln a_{\mathrm{B}}$ (at $p^\circ$, with Henry's law on the molality scale as reference), and $a_{\mathrm{B}}$ is called the overall activity of the electrolyte. But a strong electrolyte $\ce{M_{\nu_+}A_{\nu_-}}$ does not exist as molecules in solution; the real species are the ions:

$$
\mu_+ = \mu^\circ_+ + RT\ln a_+, \quad a_+ = \gamma_+\frac{b_+}{b^\circ}; \qquad \mu_- = \mu^\circ_- + RT\ln a_-, \quad a_- = \gamma_-\frac{b_-}{b^\circ},
$$
where $b_+ = \nu_+b$ and $b_- = \nu_-b$ are the **molalities** of the ions, $b^\circ = 1\,\mathrm{mol\,kg^{-1}}$, and the standard state is the hypothetical state with $b = b^\circ$ that still obeys Henry's law.

The relation between the two descriptions follows from the Gibbs energy. Let the solution consist of $n$ mol of $\ce{M_{\nu_+}A_{\nu_-}}$ and $n_{\mathrm{A}}$ mol of water. Then $G = n\mu_{\mathrm{B}} + n_{\mathrm{A}}\mu_{\mathrm{A}}$, which can also be written $G = \nu_+n\mu_+ + \nu_-n\mu_- + n_{\mathrm{A}}\mu_{\mathrm{A}}$ (the additivity formula for partial molar quantities, [6.3.4](/6.3.4)). Both hold for arbitrary $n$, so

$$
\mu_{\mathrm{B}} = \nu_+\mu_+ + \nu_-\mu_-. \tag{12.4}
$$
One mole of electrolyte contributes to the Gibbs energy of the system in the same way as $\nu_+$ mol of cations plus $\nu_-$ mol of anions. Taking $\mu^\circ_{\mathrm{B}} = \nu_+\mu^\circ_+ + \nu_-\mu^\circ_-$ and substituting gives $a_{\mathrm{B}} = a_+^{\nu_+}a_-^{\nu_-}$.

The difficulty is that the chemical potential and activity of a single ion cannot be measured: the solution must remain electrically neutral, and one cannot add cations without anions (the chemical potential of a single ion always involves the electrostatic work of moving charge into the phase, [6.3.13](/6.3.13)). Only electrically neutral combinations such as $\mu_{\mathrm{B}}$ are measurable.

### 12.6.2. Mean Activity, Mean Activity Coefficient and Mean Molality

**Definition 12.6.1** For a strong electrolyte $\ce{M_{\nu_+}A_{\nu_-}}$, let $\nu = \nu_+ + \nu_-$. The geometric means of the ionic activities, activity coefficients and molalities,

$$
a_\pm = \left(a_+^{\nu_+}a_-^{\nu_-}\right)^{1/\nu}, \qquad \gamma_\pm = \left(\gamma_+^{\nu_+}\gamma_-^{\nu_-}\right)^{1/\nu}, \qquad b_\pm = \left(b_+^{\nu_+}b_-^{\nu_-}\right)^{1/\nu} = \left(\nu_+^{\nu_+}\nu_-^{\nu_-}\right)^{1/\nu}b
$$
are called the **mean ionic activity**, the **mean ionic activity coefficient** and the **mean ionic molality**, respectively. They satisfy

$$
a_\pm = \gamma_\pm\frac{b_\pm}{b^\circ}, \qquad a_{\mathrm{B}} = a_+^{\nu_+}a_-^{\nu_-} = a_\pm^\nu.
$$

The mean activity preserves the original meaning of activity as a "corrected concentration", and $\gamma_\pm$, being an electrically neutral combination, can be determined experimentally: colligative properties such as vapor pressure and freezing-point depression give the activity of the solvent, and $\gamma_\pm$ then follows by integrating the **Gibbs–Duhem equation** ([6.3.6](/6.3.6)); or it can be determined directly from cell potentials ([6.3.13](/6.3.13)). When the activity of a single ion is needed, one usually takes the approximation $\gamma_+ \approx \gamma_- \approx \gamma_\pm$.

For a 1-1 electrolyte $b_\pm = b$; for $\ce{CaCl2}$ ($\nu_+ = 1$, $\nu_- = 2$) $b_\pm = 4^{1/3}b = 1.587b$; the same holds for $\ce{Na2SO4}$; for $\ce{LaCl3}$, $b_\pm = 27^{1/4}b = 2.280b$.

**Example 12.6.1** At $25\,^\circ\mathrm{C}$, a $0.0100\,\mathrm{mol\,kg^{-1}}$ $\ce{CaCl2}$ solution has $\gamma_\pm = 0.732$. Find $b_\pm$, $a_\pm$, $a(\ce{CaCl2})$ and the approximate $a_+$ and $a_-$.

**Solution** $b_+ = 0.0100$ and $b_- = 0.0200\,\mathrm{mol\,kg^{-1}}$, so $b_\pm = (0.0100 \times 0.0200^2)^{1/3} = 0.01587\,\mathrm{mol\,kg^{-1}}$;

$$
a_\pm = 0.732 \times 0.01587 = 0.01162, \qquad a(\ce{CaCl2}) = a_\pm^3 = 1.57\times10^{-6};
$$
taking $\gamma_+ \approx \gamma_- \approx \gamma_\pm$, $a_+ \approx 0.00732$ and $a_- \approx 0.01464$. Check: $a_+a_-^2 = 1.57\times10^{-6}$. $\square$

### 12.6.3. Data and Regularities of Mean Activity Coefficients

| $b/(\mathrm{mol\,kg^{-1}})$ | $\ce{HCl}$ | $\ce{NaCl}$ | $\ce{CaCl2}$ | $\ce{Na2SO4}$ | $\ce{CuSO4}$ |
|---|---|---|---|---|---|
| 0.001 | 0.965 | 0.965 | 0.888 | 0.886 | 0.74 |
| 0.01 | 0.905 | 0.903 | 0.732 | 0.714 | 0.44 |
| 0.1 | 0.796 | 0.778 | 0.518 | 0.445 | 0.150 |
| 0.5 | 0.757 | 0.681 | 0.448 | 0.267 | 0.062 |
| 1.0 | 0.809 | 0.657 | 0.500 | 0.204 | 0.042 |

(Aqueous solutions at $25\,^\circ\mathrm{C}$, CRC Handbook, values compiled by Robinson and Stokes.) The table shows:

1. For a given electrolyte, the lower the concentration, the closer $\gamma_\pm$ is to 1; $\gamma_\pm \to 1$ as $b \to 0$. Even at $0.001\,\mathrm{mol\,kg^{-1}}$ the $\gamma_\pm$ of $\ce{CuSO4}$ is only 0.74: an electrolyte solution deviates appreciably from ideality at a concentration that a nonelectrolyte would regard as "very dilute".
2. In dilute solutions, electrolytes of the same valence type have almost equal $\gamma_\pm$ ($\ce{HCl}$ and $\ce{NaCl}$; $\ce{CaCl2}$ and $\ce{Na2SO4}$); the larger the product of the charge numbers $\lvert z_+z_-\rvert$, the larger the deviation.
3. In concentrated solutions $\gamma_\pm$ passes through a minimum and rises again, even exceeding 1 ($\ce{HCl}$ above about $2\,\mathrm{mol\,kg^{-1}}$), the pattern depending on the electrolyte: the hydration shells of the ions take up a large part of the water, so there is less "free" solvent and the effective concentration is increased.

Regularities 1 and 2 show that in dilute solution the deviation of $\gamma_\pm$ from 1 is due to the electrostatic interaction between ions: the lower the concentration, the larger the distance between ions and the weaker the interaction; the higher the charge, the stronger it is. It is determined by the concentrations and charges of all the ions in the solution, which leads to the ionic strength.

### 12.6.4. Ionic Strength

**Definition 12.6.2** One half of the sum of the products of the molality of each ion in the solution and the square of its charge number,

$$
I_b = \frac12\sum_{\mathrm{B}}b_{\mathrm{B}}z_{\mathrm{B}}^2,
$$
is called the **ionic strength** of the solution (Lewis and Randall, 1921). When calculated from amount concentrations it is written $I_c = \frac12\sum c_{\mathrm{B}}z_{\mathrm{B}}^2$; in dilute aqueous solutions $I_c/(\mathrm{mol\,L^{-1}}) \approx 0.997\,I_b/(\mathrm{mol\,kg^{-1}})$.

The sum runs over every ion actually present in the solution (whichever electrolyte it comes from), using the actual ion concentrations. Lewis and Randall found empirically that in dilute solutions the $\gamma_\pm$ of an electrolyte is determined only by the ionic strength and does not depend on the kinds of the other ions. The theory of 12.7 proves this and explains the origin of $z^2$: the screening strength of the ionic atmosphere is proportional to $\sum c_{\mathrm{B}}z_{\mathrm{B}}^2$.

**Example 12.6.2** Find the ionic strength of the following solutions: (1) a mixture of $0.10\,\mathrm{mol\,kg^{-1}}$ $\ce{NaCl}$ and $0.20\,\mathrm{mol\,kg^{-1}}$ $\ce{CaCl2}$; (2) $\ce{CuSO4}$ at molality $b$; (3) $0.10\,\mathrm{mol\,kg^{-1}}$ acetic acid with a degree of ionization of 0.013.

**Solution** (1) $b(\ce{Na+}) = 0.10$, $b(\ce{Ca^2+}) = 0.20$, $b(\ce{Cl-}) = 0.10 + 2\times0.20 = 0.50$, so $I_b = \frac12(0.10 + 4\times0.20 + 0.50) = 0.70\,\mathrm{mol\,kg^{-1}}$. (2) $I_b = \frac12(4b + 4b) = 4b$; in general, for 1-1, 2-1 (or 1-2), 2-2 and 3-1 electrolytes, $I_b$ is $b$, $3b$, $4b$ and $6b$, respectively. (3) Only the dissociated part counts: $b(\ce{H+}) = b(\ce{CH3COO-}) = 0.0013$, so $I_b = 0.0013\,\mathrm{mol\,kg^{-1}}$. $\square$

The **salt effect** of [6.1.10](/6.1.10) is now explained quantitatively: when an unrelated strong electrolyte is added to a saturated solution of a sparingly soluble salt, the ionic strength increases and $\gamma_\pm$ decreases; the solubility product $K_{\mathrm{sp}} = \gamma_\pm^2(b_+/b^\circ)(b_-/b^\circ)$ stays constant, so the solubility increases. The "salting in" of proteins is the same effect; at high ionic strength proteins are "salted out" again, which results from the lowered activity of water and the strengthened hydrophobic interaction and lies beyond the theory of dilute solutions.

## 12.7. Theory of Strong Electrolyte Solutions

### 12.7.1. The Debye–Hückel Model

In 1923 Debye and Hückel proposed the first quantitative theory of strong electrolyte solutions. Its starting point is that in dilute solution the nonideality of an electrolyte solution is entirely due to the electrostatic interaction between ions.

**Definition 12.7.1** The theory that calculates the activity coefficients of ions in dilute solutions of strong electrolytes on the basis of the following assumptions is called the **Debye–Hückel theory**:

1. The strong electrolyte is completely dissociated; the ions are point charges (or rigid spheres) carrying charges $z_ie$, and the only interaction between ions is the Coulomb interaction;
2. The solvent is a continuous medium of permittivity $\varepsilon = \varepsilon_0\varepsilon_{\mathrm{r}}$, with $\varepsilon_{\mathrm{r}}$ taken as the value of the pure solvent;
3. One ion is chosen as the central ion; the distribution of the other ions in its field obeys the Boltzmann distribution, and the charge density and the potential are related by the Poisson equation;
4. The electrostatic potential energy of an ion is much smaller than its thermal energy, $\lvert z_ie\psi\rvert \ll k_{\mathrm{B}}T$.

Under these assumptions, ions of opposite sign are more likely than ions of the same sign to be found around the central ion, and the time average is a spherically symmetric charge cloud whose total charge is equal in magnitude and opposite in sign to that of the central ion; it is called the *ionic atmosphere*.

The ionic atmosphere is not a fixed shell of ions: each ion is itself a member of the ionic atmospheres of other ions, the ions in the atmosphere are continually exchanged, and the atmosphere is only a charge distribution in the statistical-average sense. The attraction between the central ion and its atmosphere lowers the energy of the central ion, so its chemical potential is lower than in an ideal solution, and hence $\gamma < 1$. We now make this picture quantitative.

### 12.7.2. The Linearized Poisson–Boltzmann Equation

Let the central ion $j$ carry a charge $z_je$ and let the mean potential around it be $\psi(\boldsymbol{r})$. The potential energy of ion $i$ at a point of potential $\psi$ is $z_ie\psi$, so by the Boltzmann distribution its number density there is $n_i = n_i^0\exp(-z_ie\psi/k_{\mathrm{B}}T)$, where $n_i^0$ is the number density in the bulk solution (where $\psi = 0$). The charge density is $\rho = \sum_i z_ien_i$, and the **electric potential** satisfies the Poisson equation $\Delta\psi = -\rho/\varepsilon$ ([5.3.2](/5.3.2#sec-2.4.2), [5.3.4](/5.3.4)), whence

$$
\Delta\psi = -\frac{1}{\varepsilon}\sum_i z_ien_i^0\exp\left(-\frac{z_ie\psi}{k_{\mathrm{B}}T}\right). \tag{12.5}
$$

**Definition 12.7.2** The nonlinear partial differential equation (12.5) satisfied by the mean potential $\psi$ in an electrolyte solution is called the **Poisson–Boltzmann equation**.

It combines electrostatics (the Poisson equation) with statistical mechanics (the Boltzmann distribution) and is a "mean-field" approximation: the mean potential replaces the instantaneous positions of the other ions. Equation (12.5) generally has no analytical solution. By assumption 4, we expand the exponential to first order:

$$
\Delta\psi = -\frac{e}{\varepsilon}\sum_i z_in_i^0 + \frac{e^2}{\varepsilon k_{\mathrm{B}}T}\sum_i z_i^2n_i^0\,\psi.
$$
By electroneutrality of the bulk solution, $\sum_i z_in_i^0 = 0$, the first term vanishes, and we obtain the linearized Poisson–Boltzmann equation

$$
\Delta\psi = \kappa^2\psi, \qquad \kappa^2 = \frac{e^2}{\varepsilon k_{\mathrm{B}}T}\sum_i n_i^0z_i^2 = \frac{2F^2I_c}{\varepsilon RT}, \tag{12.6}
$$
where the last step used $n_i^0 = N_{\mathrm{A}}c_i$, $e^2N_{\mathrm{A}}^2 = F^2$ and $k_{\mathrm{B}}N_{\mathrm{A}} = R$, with $I_c$ in $\mathrm{mol\,m^{-3}}$. This is where the ionic strength enters: the screening depends only on $\sum c_iz_i^2$.

**Definition 12.7.3** The reciprocal of $\kappa$ in Eq. (12.6),

$$
\lambda_{\mathrm{D}} = \frac{1}{\kappa} = \sqrt{\frac{\varepsilon RT}{2F^2I_c}},
$$
is called the **Debye length** (Debye screening length); it is the characteristic thickness of the ionic atmosphere.

Substituting $\varepsilon_{\mathrm{r}} = 78.4$ for water at $25\,^\circ\mathrm{C}$ and using $I_c \approx 997\,\mathrm{kg\,m^{-3}}\times I_b$, we obtain

$$
\lambda_{\mathrm{D}} = \frac{0.304\,\mathrm{nm}}{\sqrt{I_b/b^\circ}}, \qquad \kappa = B\sqrt{I_b/b^\circ}, \quad B = 3.29\,\mathrm{nm^{-1}}. \tag{12.7}
$$
For $I_b = 0.001$, $0.01$ and $0.1\,\mathrm{mol\,kg^{-1}}$, $\lambda_{\mathrm{D}}$ is 9.6, 3.0 and 0.96 nm, respectively; in physiological saline (about $0.15\,\mathrm{mol\,kg^{-1}}$) it is about 0.8 nm, so electrostatic interactions inside cells are strongly screened beyond 1 nm, and the electrostatic interaction between proteins is short-ranged. The same screening occurs in plasmas and semiconductors, and in the theory of the electric double layer of colloids $\lambda_{\mathrm{D}}$ is the thickness of the diffuse layer ([6.3.21](/6.3.21)).

### 12.7.3. Potential and Charge Distribution of the Ionic Atmosphere

The potential around the central ion is spherically symmetric, $\psi = \psi(r)$. In spherical coordinates the **Laplace operator** acting on a radial function is ([2.5.5](/2.5.5))

$$
\Delta\psi = \frac{1}{r^2}\frac{\mathrm{d}}{\mathrm{d}r}\left(r^2\frac{\mathrm{d}\psi}{\mathrm{d}r}\right) = \frac1r\frac{\mathrm{d}^2(r\psi)}{\mathrm{d}r^2}.
$$
Setting $w = r\psi$ turns Eq. (12.6) into the linear equation with constant coefficients $w'' = \kappa^2w$, with general solution $w = A\mathrm{e}^{-\kappa r} + A'\mathrm{e}^{\kappa r}$ ([2.4.9](/2.4.9)). The potential must be bounded as $r \to \infty$, so $A' = 0$:

$$
\psi(r) = \frac{A\,\mathrm{e}^{-\kappa r}}{r}.
$$
For the point-charge model the effect of the atmosphere is negligible as $r \to 0$, and $\psi$ must tend to the Coulomb potential of the central ion itself, $z_je/(4\pi\varepsilon r)$, so $A = z_je/(4\pi\varepsilon)$ and

$$
\psi(r) = \frac{z_je}{4\pi\varepsilon}\frac{\mathrm{e}^{-\kappa r}}{r}. \tag{12.8}
$$
This is the screened Coulomb potential (called the Yukawa potential in nuclear physics): for $r \ll \lambda_{\mathrm{D}}$ it equals the potential of the bare charge, and for $r \gg \lambda_{\mathrm{D}}$ it decays exponentially; the field of the central ion has been "screened" by the ionic atmosphere.

The charge density of the ionic atmosphere is recovered from the Poisson equation: $\rho(r) = -\varepsilon\Delta\psi = -\varepsilon\kappa^2\psi = -\dfrac{z_je\kappa^2}{4\pi}\dfrac{\mathrm{e}^{-\kappa r}}{r}$. The charge in a spherical shell between radii $r$ and $r + \mathrm{d}r$ is $4\pi r^2\rho\,\mathrm{d}r = -z_je\kappa^2r\mathrm{e}^{-\kappa r}\,\mathrm{d}r$, and integrating over $r$ from 0 to $\infty$ gives exactly $-z_je$: the total charge of the atmosphere is equal in magnitude and opposite in sign to that of the central ion. The shell charge is greatest at $r = 1/\kappa = \lambda_{\mathrm{D}}$, which is why $\lambda_{\mathrm{D}}$ is called the thickness of the ionic atmosphere.

Eq. (12.8) can be split into the potential of the central ion itself and the potential produced by the atmosphere:

$$
\psi(r) = \frac{z_je}{4\pi\varepsilon r} + \psi_{\text{atm}}(r), \qquad \psi_{\text{atm}}(r) = \frac{z_je}{4\pi\varepsilon}\frac{\mathrm{e}^{-\kappa r} - 1}{r} \xrightarrow{r\to0} -\frac{z_je\kappa}{4\pi\varepsilon}. \tag{12.9}
$$
The potential produced by the ionic atmosphere at the central ion equals that produced by the charge $-z_je$ distributed uniformly over a spherical surface of radius $\lambda_{\mathrm{D}}$.

![Debye–Hückel ionic atmosphere of a monovalent ion in water at 25 °C (point-charge model). Left: the screened potential around a central cation compared with the bare Coulomb potential; right: the radial distribution of the atmosphere charge in each spherical shell, with unit area under the curve and the maximum at r = λ_D (dashed)](./plots/ionic-atmosphere.py)

### 12.7.4. The Debye–Hückel Limiting Law

**Theorem 12.7.1 (Debye–Hückel Limiting Law)** In the point-charge approximation of the Debye–Hückel model, the activity coefficient of ion $j$ and the mean activity coefficient of a strong electrolyte are

$$
\ln\gamma_j = -\frac{z_j^2e^2\kappa}{8\pi\varepsilon k_{\mathrm{B}}T}, \qquad \lg\gamma_\pm = -A\lvert z_+z_-\rvert\sqrt{I_b/b^\circ},
$$
where $A = \dfrac{e^2B}{8\pi\varepsilon k_{\mathrm{B}}T\ln10}$; in aqueous solution at $25\,^\circ\mathrm{C}$, $A = 0.509$.

**Proof** The difference between an ideal and a real solution lies only in the electrostatic interaction between ions, so the nonideal part $k_{\mathrm{B}}T\ln\gamma_j$ (per ion) of the chemical potential of ion $j$ equals the part, contributed by the ionic atmosphere, of the electrostatic work of "charging" the ion from neutral to $z_je$ in the presence of the atmosphere (the Coulomb self-energy of the ion is present in an ideal solution as well and cancels). Imagine the ion carrying a charge $q$ ($0 \le q \le z_je$) while the other ions in the solution stay unchanged. By Eq. (12.9), the potential of the atmosphere at the position of the ion is $-q\kappa/(4\pi\varepsilon)$, and moving a charge $\mathrm{d}q$ there requires work $\psi_{\text{atm}}\,\mathrm{d}q$, so

$$
k_{\mathrm{B}}T\ln\gamma_j = \int_0^{z_je}\left(-\frac{q\kappa}{4\pi\varepsilon}\right)\mathrm{d}q = -\frac{z_j^2e^2\kappa}{8\pi\varepsilon}.
$$
(If all the ions are instead charged simultaneously in the same proportion, $\kappa$ also changes, but the integral gives the same result; this is Güntelberg's treatment.) This is the first formula. By Definition 12.6.1,

$$
\ln\gamma_\pm = \frac{\nu_+\ln\gamma_+ + \nu_-\ln\gamma_-}{\nu} = -\frac{e^2\kappa}{8\pi\varepsilon k_{\mathrm{B}}T}\cdot\frac{\nu_+z_+^2 + \nu_-z_-^2}{\nu_+ + \nu_-}.
$$
By electroneutrality $\nu_+z_+ = -\nu_-z_-$, $\nu_+z_+^2 + \nu_-z_-^2 = \nu_+z_+(z_+ - z_-) = \lvert z_+z_-\rvert(\nu_+ + \nu_-)$ (for example $\ce{CaCl2}$: $4 + 2 = 2\times3$), so $\ln\gamma_\pm = -\lvert z_+z_-\rvert e^2\kappa/(8\pi\varepsilon k_{\mathrm{B}}T)$. Substituting $\kappa = B\sqrt{I_b/b^\circ}$ and converting to common logarithms gives the second formula. Numerically, $e^2/(4\pi\varepsilon k_{\mathrm{B}}T)$ is the Bjerrum length, $0.715\,\mathrm{nm}$ in water at $25\,^\circ\mathrm{C}$, so $A = 0.715\times3.29/(2\ln10) = 0.51$; a more accurate $\varepsilon_{\mathrm{r}}$ gives the standard value $0.509$. $\square$

The content of the limiting law is as follows.

- $\ln\gamma_\pm$ is proportional to $\sqrt{I_b}$, with a slope determined by the valence type $\lvert z_+z_-\rvert$ and the solvent and independent of the individuality of the ions. This is exactly regularities 1 and 2 of 12.6.3 and the Lewis–Randall ionic strength rule.
- The square-root dependence comes from $\kappa \propto \sqrt{I}$, that is, the radius of the ionic atmosphere shrinks as the square root of the concentration. The slope is infinite at $b = 0$, which shows that the electrostatic interaction is long-ranged and that an electrolyte at any finite concentration is not an ideal solution.
- $A \propto (\varepsilon_{\mathrm{r}}T)^{-3/2}$: the smaller the permittivity of the solvent, the larger the deviation. In ethanol ($\varepsilon_{\mathrm{r}} \approx 25$), $A$ is about 5.6 times its value in water.

The range of validity is about $I_b \lesssim 0.01\,\mathrm{mol\,kg^{-1}}$ (narrower for 2-2 electrolytes). The law also applies to ions in solutions of weak electrolytes and sparingly soluble salts (Example 12.5.1), provided that the ionic strength is calculated from the actual ion concentrations in the solution. It is also often written $\ln\gamma_\pm = -1.172\lvert z_+z_-\rvert\sqrt{I_b/b^\circ}$ with $1.172 = 0.509\ln10$; the two are equivalent, but the constant must match the logarithm used.

### 12.7.5. The Extended Debye–Hückel Equation and Its Range of Validity

The point-charge approximation fails when the distance between ions approaches the size of the ions. Let the ions be rigid spheres of diameter (distance of closest approach) $a$. For $r < a$ there are no other ions and the potential is $\dfrac{z_je}{4\pi\varepsilon r} + C$; for $r \ge a$ it is still $A\mathrm{e}^{-\kappa r}/r$. Requiring the potential and the field to be continuous at $r = a$ gives $C = -\dfrac{z_je\kappa}{4\pi\varepsilon(1 + \kappa a)}$; that is, the potential of the ionic atmosphere is smaller than in the point-charge model by a factor $1 + \kappa a$. Repeating the charging process gives

$$
\lg\gamma_\pm = -\frac{A\lvert z_+z_-\rvert\sqrt{I_b/b^\circ}}{1 + Ba\sqrt{I_b/b^\circ}}. \tag{12.10}
$$
For $a \approx 0.3\,\mathrm{nm}$, $Ba \approx 1$, and the commonly used form is $\lg\gamma_\pm = -A\lvert z_+z_-\rvert\sqrt{I}/(1 + \sqrt{I})$ ($I = I_b/b^\circ$), valid for $I \lesssim 0.1$. Adding an empirical linear term gives the Davies equation

$$
\lg\gamma_\pm = -A\lvert z_+z_-\rvert\left(\frac{\sqrt{I}}{1 + \sqrt{I}} - 0.30\,I\right), \tag{12.11}
$$
which has no adjustable parameter and for most electrolytes has errors of a few percent over $I \lesssim 0.1$–$0.5$; it is widely used for chemical equilibrium calculations in natural waters and physiological solutions. The linear term represents short-range interactions at close distance (ion hydration and the formation of ion pairs), and it makes $\gamma_\pm$ rise again in concentrated solutions. More concentrated solutions require models such as the Pitzer equations, which contain ion-specific parameters, or molecular simulation.

![Mean activity coefficients of aqueous solutions at 25 °C (CRC data points) compared with the Debye–Hückel theory: the dash-dotted line is the limiting law, the dashed line the extended equation (Ba = 1), and the solid line the Davies equation. The left panel shows the dilute region, where the data for all three valence types approach their respective limiting slopes; the right panel extends to concentrated solutions, where the extended equation and the Davies equation successively extend the range of validity, but neither describes 2-2 electrolytes at high concentration](./plots/activity-coefficients.py)

**Example 12.7.1** Estimate $\gamma_\pm$ of $0.0100\,\mathrm{mol\,kg^{-1}}$ $\ce{CaCl2}$ at $25\,^\circ\mathrm{C}$ with the limiting law, the extended equation and the Davies equation, and compare with the experimental value 0.732.

**Solution** $I = 3\times0.0100 = 0.0300$, $\sqrt I = 0.1732$, $A\lvert z_+z_-\rvert = 1.018$.

$$
\begin{aligned}
\text{Limiting law:}&\ \lg\gamma_\pm = -1.018\times0.1732 = -0.1763, && \gamma_\pm = 0.666;\\
\text{Extended equation:}&\ \lg\gamma_\pm = -0.1763/1.1732 = -0.1503, && \gamma_\pm = 0.707;\\
\text{Davies:}&\ \lg\gamma_\pm = -1.018\times(0.1476 - 0.0090) = -0.1411, && \gamma_\pm = 0.723.
\end{aligned}
$$
For a 2-1 electrolyte, $I = 0.03$ is already outside the range of validity of the limiting law, with an error of about 9%; the Davies equation has an error of about 1%. $\square$

**Example 12.7.2** For a mixture of $0.1\,\mathrm{mol\,kg^{-1}}$ $\ce{NaCl}$ and $0.2\,\mathrm{mol\,kg^{-1}}$ $\ce{CaCl2}$, use the limiting law to find $\gamma_\pm(\ce{NaCl})$, obtaining $\lg\gamma_\pm = -0.509\sqrt{0.70} = -0.426$ and $\gamma_\pm = 0.375$. What is wrong with this calculation?

**Solution** By Example 12.6.2, $I_b = 0.70\,\mathrm{mol\,kg^{-1}}$, about two orders of magnitude above the range of validity of the limiting law, so the result is meaningless. The Davies equation gives $\lg\gamma_\pm = -0.509\times(0.8367/1.8367 - 0.21) = -0.125$, $\gamma_\pm \approx 0.75$; even this value is only a rough estimate ($I$ is already beyond the reliable range of the Davies equation), and reliable values require experimental data or the Pitzer model. According to the limiting law, $\gamma_\pm$ would decrease without bound as $\sqrt I$ increases, whereas in reality the $\gamma_\pm$ of 1-1 electrolytes has already passed through a minimum near $I \approx 0.5$–$1$ (the table of 12.6.3). $\square$

### 12.7.6. The Debye–Hückel–Onsager Theory of Conductivity

The ionic atmosphere not only lowers the chemical potential of an ion but also slows its migration, which is why the $\Lambda_{\mathrm{m}}$ of a strong electrolyte decreases with concentration.

**Definition 12.7.4** The two retarding effects of the ionic atmosphere on the motion of an ion migrating in an electric field are as follows. As the central ion moves, a new ionic atmosphere has to build up ahead of it and the old one behind it has to decay, which takes a certain time (the relaxation time, about $10^{-10}$–$10^{-8}\,\mathrm{s}$, of the same order as $\varepsilon/\sigma$); the atmosphere thus becomes asymmetric, with more opposite charge behind, which pulls the central ion backward. This is called the **relaxation effect**. The ions of opposite sign in the atmosphere move in the opposite direction in the field, carrying their solvent with them, so that the central ion in effect moves against a counterflow and experiences a larger viscous drag. This is called the **electrophoretic effect**.

Both effects are proportional to the "strength" of the ionic atmosphere, $\kappa \propto \sqrt c$, which explains Kohlrausch's square-root law. Onsager (1927) calculated the proportionality coefficients on the basis of the Debye–Hückel model.

**Theorem 12.7.2 (Debye–Hückel–Onsager Theory of Conductivity)** In dilute solutions of a 1-1 strong electrolyte,

$$
\Lambda_{\mathrm{m}} = \Lambda^\infty_{\mathrm{m}} - \left(a + b\Lambda^\infty_{\mathrm{m}}\right)\sqrt{c},\qquad a = \frac{eF^2}{3\pi\eta}\sqrt{\frac{2}{\varepsilon RT}},\qquad b = \frac{2q}{1 + \sqrt q}\cdot\frac{eF^2}{24\pi\varepsilon RT}\sqrt{\frac{2}{\varepsilon RT}},
$$
where $c$ is in $\mathrm{mol\,m^{-3}}$, $\eta$ is the viscosity of the solvent, and $q = 1/2$ (for a symmetric electrolyte), so that $2q/(1 + \sqrt q) = 0.586$. The first term comes from the electrophoretic effect and the second from the relaxation effect. In aqueous solution at $25\,^\circ\mathrm{C}$,

$$
\frac{\Lambda_{\mathrm{m}}}{\mathrm{S\,cm^2\,mol^{-1}}} = \frac{\Lambda^\infty_{\mathrm{m}}}{\mathrm{S\,cm^2\,mol^{-1}}} - \left(60.20 + 0.2289\,\frac{\Lambda^\infty_{\mathrm{m}}}{\mathrm{S\,cm^2\,mol^{-1}}}\right)\sqrt{\frac{c}{\mathrm{mol\,L^{-1}}}}.
$$

(Many textbooks write the two coefficients in the Gaussian system and use $D$ for the dielectric constant; the SI form is given here.) This is the theoretical value of Kohlrausch's empirical coefficient $\mathcal{A}$, with no adjustable parameter. For $\ce{KCl}$, $\mathcal{A} = 60.20 + 0.2289\times149.8 = 94.5$; the prediction at $c = 0.001\,\mathrm{mol\,L^{-1}}$ is $\Lambda_{\mathrm{m}} = 149.8 - 94.5\times0.0316 = 146.8$, against an experimental value of 146.9. As the dashed lines in the figure of 12.3.4 show, the theoretical slope agrees with experiment for $c \lesssim 0.001\,\mathrm{mol\,L^{-1}}$; at higher concentrations the experimental points deviate above the line, because the finite size of the ions (the factor $1 + \kappa a$) can no longer be neglected.

Both effects depend on the ionic atmosphere having time to form. In a high-frequency alternating field (frequency above the reciprocal of the relaxation time, above about $10^8\,\mathrm{Hz}$), the atmosphere has no time to develop an asymmetric structure, the relaxation effect disappears, and the conductivity increases (the Debye–Falkenhagen effect). In a very strong field (about $10^7\,\mathrm{V\,m^{-1}}$), the ions move so fast that the atmosphere has no time to form, and the conductivity also increases (the Wien effect). These two effects directly confirm the existence of the ionic atmosphere.

## Summary

| Topic | Key points |
|---|---|
| Mechanism of conduction | Ionic electromigration + electrode reactions + external circuit, in series with equal current; oxidation at the anode, reduction at the cathode |
| Faraday's laws of electrolysis | $Q = zF\xi$; $F = N_{\mathrm{A}}e = 96\,485.332\,12\,\mathrm{C\,mol^{-1}}$ (exact); use entities carrying one elementary charge |
| Mobility and transport numbers | $u = v/E$, Stokes estimate $u = \lvert z\rvert e/(6\pi\eta r)$; $t_+ = u_+/(u_+ + u_-)$; Hittorf method, moving boundary method |
| Conductivity and molar conductivity | $\sigma = F\sum\lvert z_{\mathrm{B}}\rvert c_{\mathrm{B}}u_{\mathrm{B}}$; $\Lambda_{\mathrm{m}} = \sigma/c = \alpha(u_+ + u_-)F$; cell constant $l/A$ calibrated with $\ce{KCl}$ |
| Kohlrausch's law | Strong electrolytes $\Lambda_{\mathrm{m}} = \Lambda^\infty_{\mathrm{m}} - \mathcal{A}\sqrt c$; $\Lambda^\infty_{\mathrm{m}} = \nu_+\lambda^\infty_+ + \nu_-\lambda^\infty_-$ (independent migration); $\lambda_{\mathrm{B}} = \lvert z_{\mathrm{B}}\rvert Fu_{\mathrm{B}} = t_{\mathrm{B}}\Lambda_{\mathrm{m}}/\nu_{\mathrm{B}}$ |
| Conductometry | Weak electrolytes $\alpha = \Lambda_{\mathrm{m}}/\Lambda^\infty_{\mathrm{m}}$; sparingly soluble salts $c = [\sigma - \sigma(\ce{H2O})]/\Lambda^\infty_{\mathrm{m}}$; conductometric titration |
| Mean activity | $\mu_{\mathrm{B}} = \nu_+\mu_+ + \nu_-\mu_-$; $a_{\mathrm{B}} = a_\pm^\nu$, $a_\pm = \gamma_\pm b_\pm/b^\circ$, geometric means |
| Ionic strength | $I_b = \frac12\sum b_{\mathrm{B}}z_{\mathrm{B}}^2$ |
| Debye–Hückel theory | Linearized PB equation $\Delta\psi = \kappa^2\psi$; $\lambda_{\mathrm{D}} = 0.304\,\mathrm{nm}/\sqrt{I_b/b^\circ}$ (water, $25\,^\circ\mathrm{C}$); $\lg\gamma_\pm = -0.509\lvert z_+z_-\rvert\sqrt{I}$ ($I \lesssim 0.01$), the extended equation divides by $1 + \sqrt I$, and the Davies equation adds $0.30I$ |
| Theory of conductivity | Relaxation effect + electrophoretic effect; for 1-1 electrolytes in water $\Lambda_{\mathrm{m}} = \Lambda^\infty_{\mathrm{m}} - (60.20 + 0.2289\Lambda^\infty_{\mathrm{m}})\sqrt c$ |

## Questions

1. True or false: the electric mobility of an ion in an electrolyte solution is a property of the ion itself.

   **Answer** False. The mobility depends on the concentration and on the other ions present; only the limiting mobility is a characteristic parameter of the ion in a given solvent at a given temperature.

2. Why is alternating current used to measure conductance, whereas the measurement of the cell potential requires the current to tend to zero?

   **Answer** The former avoids electrode reactions and polarization; the latter keeps the electrodes at equilibrium, [6.3.13](/6.3.13).

3. In a solution of a weak electrolyte, what do $\Lambda_{\mathrm{m}} = \sigma/c$ and $\sigma/(c\alpha)$ represent?

   **Answer** The former is the molar conductivity calculated from the total concentration of the electrolyte; the latter is calculated from the actual ion concentration and is approximately equal to $\Lambda^\infty_{\mathrm{m}}$.

4. The Hittorf method gives $t(\ce{H+}) \approx 0.82$ in $\ce{HCl}$. Is this consistent with the $\lambda^\infty$ values in the table?

   **Answer** Yes: $349.65/(349.65 + 76.31) = 0.821$.

5. What kind of electrolyte solution can be called "ideal"? Must $\gamma_\pm$ be considered in solutions of sparingly soluble salts and weak electrolytes?

   **Answer** Only an infinitely dilute solution is ideal; in calculating thermodynamic equilibrium constants one must still correct with the Debye–Hückel equation according to the actual ionic strength, Example 12.5.1.

6. Why is the charge number squared in the definition of ionic strength?

   **Answer** The screening comes from the linear expansion of the Boltzmann factor: each kind of ion contributes $z_i \times z_i$, one factor $z_i$ from its charge and the other from its response to the potential.
