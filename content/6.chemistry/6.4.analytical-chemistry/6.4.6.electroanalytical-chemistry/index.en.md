---
title: Electroanalytical Chemistry
description: Conductometry; potentiometry, ion-selective electrodes and the Nikolsky–Eisenman equation; direct potentiometry, standard addition, Gran plots, and potentiometric titration; electrogravimetry, coulometry, and coulometric titration; polarography, cyclic, pulse, and stripping voltammetry; glucose sensors, biosensors, scanning electrochemical microscopy, patch clamp, and nanopore sequencing.
source_hash: e2a50cc0c594
---

Electroanalytical chemistry relates electrical quantities of a solution (conductance, potential, current, and charge, and the curves of current against potential) to the concentration of the substance to be determined. Its theoretical foundations were laid in physical chemistry: conduction in electrolyte solutions and ionic strength ([6.3.12](/6.3.12)), cell thermodynamics, electrode potentials, and membrane potentials ([6.3.13](/6.3.13)), and electrode kinetics and diffusion-controlled currents ([6.3.14](/6.3.14)). This chapter does not rederive these theories but treats methods, electrodes, instruments, and applications. It follows directly on the chemical analysis of the preceding chapters: the formal potentials and titration curves of redox titration ([6.4.5](/6.4.5)) are the direct prerequisite of potentiometric titration, and potentiometric titration, biamperometric end-point detection, and coulometric titration are instrumental versions of the four classes of titration ([6.4.2](/6.4.2)–[6.4.5](/6.4.5)); calibration curves, standard addition, and the limit of detection follow the definitions of [6.4.1](/6.4.1). Electrochemical methods use simple instruments, are sensitive, can be miniaturized, and can be used directly in living organisms. Blood glucose meters, pH meters, clinical electrolyte analyzers, patch clamp, and nanopore sequencing all belong to this chapter, which is why the later section on biosensing is treated in some detail.

## 6.1. Overview of Electroanalytical Methods

### 6.1.1. Classification of Methods

**Definition 6.1.1 (Electroanalytical Chemistry)** The analytical methods that are based on electrochemical principles and the electrochemical properties of substances and determine the composition and content of a substance by measuring electrical quantities (conductance, potential, current, charge) in an electrochemical cell, or the relations between them, are collectively called **electroanalytical chemistry** (electrochemical analysis).

By purpose, electroanalytical methods fall into three classes: (1) direct quantitative determination from the functional relation between a concentration in solution and an electrical quantity, the most common class; (2) end-point detection in titration by an abrupt change in an electrical quantity (conductometric titration, potentiometric titration, biamperometric end-point detection); and (3) deposition of the analyte as a solid phase by an electrode reaction, which separates it from other components (electrogravimetry, mercury-cathode electrolysis). Classified by the quantity measured, the methods are as follows:

| Method | Quantity measured | Quantitative relation | In this chapter |
|---|---|---|---|
| Conductometry | Conductance $G$ | In dilute solution $\sigma = \sum_{\mathrm{B}}\lambda_{\mathrm{B}}c_{\mathrm{B}}$ | 6.2 |
| Potentiometry | Cell emf $E$ at zero current | Nernst equation: $E$ is linear in $\lg a$ | 6.3–6.4 |
| Electrolysis and coulometry | Mass of deposit, charge $Q$ | Faraday's laws of electrolysis: $n = Q/(zF)$ | 6.5 |
| Voltammetry and polarography | Current–potential curve $I$–$E$ | Diffusion-controlled current $I \propto c$ | 6.6 |
| Electrochemical sensors | Current or potential | Determined by the recognition element and the transduction mode | 6.7 |

Different methods use different electrodes: electrolysis and coulometry use Pt electrodes; potentiometry and potentiometric sensors use ion-selective electrodes; voltammetry and amperometric sensors use the dropping mercury electrode (historically), glassy carbon, and Pt or Au microelectrodes. Common features of electroanalytical methods are simple instruments that cost less than optical instruments and a wide range of sensitivity: about $10^{-6}\,\mathrm{mol\,L^{-1}}$ for direct potentiometry, about $10^{-5}\,\mathrm{mol\,L^{-1}}$ for classical polarography, $10^{-7}$–$10^{-8}\,\mathrm{mol\,L^{-1}}$ for pulse voltammetry, and down to the order of $10^{-9}$–$10^{-11}\,\mathrm{mol\,L^{-1}}$ for stripping voltammetry.

### 6.1.2. Electrochemical Cells and Their Emf

Electroanalysis is carried out in a **galvanic cell** or an **electrolytic cell** ([6.1.11](/6.1.11#sec-11.3.1)). In either, the electrode at which oxidation occurs is called the anode and the electrode at which reduction occurs the cathode. The **cell notation** is described in [6.1.11](/6.1.11#sec-11.3.2) and [6.3.13](/6.3.13#sec-13.1.3); for example,

$$
\ce{Zn} \mid \ce{ZnSO4}(c_1) \parallel \ce{CuSO4}(c_2) \mid \ce{Cu}.
$$
By the IUPAC convention the emf of a cell is always the electrode potential of the right-hand electrode minus that of the left-hand electrode:

$$
E_{\mathrm{cell}} = E_{\mathrm{right}} - E_{\mathrm{left}}.
$$
When the cell is written with the negative electrode on the left and the positive on the right, $E_{\mathrm{cell}} > 0$ and the cell discharges spontaneously. The voltage actually measured contains two further contributions: the **liquid junction potential** $E_{\mathrm{j}}$ at the junction of the two solutions ([6.1.11](/6.1.11#sec-11.4.1), [6.3.13](/6.3.13#sec-13.4.6)), which can be reduced to 1–2 mV with a salt bridge, and the voltage drop $IR$ across the solution resistance $R$ when a current $I$ passes. Potentiometry measures at zero current, so the $IR$ term does not appear, but $E_{\mathrm{j}}$ is one of the main sources of error. In electrolysis and voltammetry the current is not zero, and the $IR$ drop must be accounted for or compensated by a three-electrode system.

In the Cu–Zn cell above, with $c_2$ fixed, $E_{\mathrm{cell}} = E(\ce{Cu^2+}/\ce{Cu}) - E(\ce{Zn^2+}/\ce{Zn})$ varies only with the activity of $\ce{Zn^2+}$; at $25\,^\circ\mathrm{C}$, $E(\ce{Zn^2+}/\ce{Zn}) = E^\circ + \frac{0.0592\,\mathrm{V}}{2}\lg a(\ce{Zn^2+})$, so the activity of $\ce{Zn^2+}$ can be found by measuring the emf. This is the principle of potentiometry: the potential of one electrode varies with the ion to be determined, and the potential of the other is constant.

### 6.1.3. Electrodes

Reversible electrodes are divided into three classes according to the phase of the species taking part in the reaction ([6.3.13](/6.3.13#sec-13.1.4)); in electroanalysis a "zeroth class" and membrane electrodes are usually added:

| Electrode | Example | Electrode potential ($25\,^\circ\mathrm{C}$) |
|---|---|---|
| Inert electrode (zeroth class, i.e., redox electrode) | $\ce{Pt} \mid \ce{Ce^4+}, \ce{Ce^3+}$ | $E = E^{\circ\prime} + 0.0592\,\mathrm{V}\,\lg\dfrac{c(\ce{Ce^4+})}{c(\ce{Ce^3+})}$ |
| First-class electrode (metal electrode) | $\ce{Zn} \mid \ce{Zn^2+}$ | $E = E^\circ + \dfrac{0.0592\,\mathrm{V}}{z}\lg a(\ce{M^{z+}})$ |
| Second-class electrode (metal–sparingly soluble salt) | $\ce{Ag} \mid \ce{AgCl(s)} \mid \ce{Cl-}$ | $E = E^\circ(\ce{AgCl}/\ce{Ag}) - 0.0592\,\mathrm{V}\,\lg a(\ce{Cl-})$ |
| Third-class electrode | $\ce{Ag} \mid \ce{Ag2C2O4(s)} \mid \ce{CaC2O4(s)} \mid \ce{Ca^2+}$ | See below |
| Membrane electrode | Glass electrode, ion-selective electrode | $E = K \pm \dfrac{0.0592\,\mathrm{V}}{z}\lg a$ |

In a third-class electrode the two sparingly soluble salts have an anion in common, and the cation of the second salt is in the solution. Eliminating oxalate by means of $a(\ce{Ag+})^2a(\ce{C2O4^2-}) = K_{\mathrm{sp}}(\ce{Ag2C2O4})$ and $a(\ce{Ca^2+})a(\ce{C2O4^2-}) = K_{\mathrm{sp}}(\ce{CaC2O4})$ gives

$$
E = E^\circ(\ce{Ag+}/\ce{Ag}) + \frac{0.0592\,\mathrm{V}}{2}\lg\frac{K_{\mathrm{sp}}(\ce{Ag2C2O4})}{K_{\mathrm{sp}}(\ce{CaC2O4})} + \frac{0.0592\,\mathrm{V}}{2}\lg a(\ce{Ca^2+}),
$$
so the silver electrode becomes an electrode responsive to $\ce{Ca^2+}$ (with the slope of a divalent ion, 29.6 mV). Such electrodes have now been replaced by ion-selective electrodes. The fundamental difference between a membrane electrode and a metal electrode is that the membrane potential arises from exchange and diffusion of ions, with no electron transfer (Section 6.3.2).

According to their role in the measurement, electrodes are also classified as **indicator electrodes** and **reference electrodes** (potentiometry, zero current) and, in electrolysis and voltammetry (with current), as the **three-electrode system** of **working electrode**, **counter electrode**, and reference electrode ([6.3.14](/6.3.14#sec-14.2.5)). The current flows between the working electrode and the counter electrode, and the potential of the working electrode is measured and controlled relative to the reference electrode, which carries almost no current, so that the error caused by the solution resistance is greatly reduced.

### 6.1.4. Examples of Applications

Four typical applications of electroanalysis run through this chapter. The blood glucose meter uses a glucose oxidase electrode to measure a current proportional to the glucose concentration (Section 6.7.1). The pH electrode is the most widely used ion-selective electrode (6.3.2). Patch clamp uses a glass microelectrode to measure picoampere currents through single ion channels (6.4.6). Nanopore sequencing measures the change in ionic current as DNA passes through a nanopore (6.7.4). The four correspond to measurements of current, potential, current, and conductance, respectively.

## 6.2. Conductometry

### 6.2.1. Principles and Measurement

The **conductance** $G = 1/R$ of a solution is related to its **conductivity** $\sigma$ through the **cell constant** $K_{\mathrm{cell}} = l/A$ by $\sigma = K_{\mathrm{cell}}G$ ([6.3.12](/6.3.12#sec-12.3)). The cell constant is usually determined with a standard $\ce{KCl}$ solution of known conductivity. In dilute solution the conductivity is the sum of contributions from all the ions and is not selective: conductometry can determine only the total amount of ions in a solution, or the concentration of one electrolyte when only that electrolyte changes.

Measuring conductance is in effect measuring resistance, but direct current cannot be used: ions are discharged when a current passes through the electrodes, and the electrolysis products and electrode polarization change the resistance. Conductivity meters therefore use alternating current of sufficiently high frequency (about $1\,\mathrm{kHz}$ for low conductance and higher for high conductance), and the electrodes are coated with platinum black to increase the true surface area and reduce interfacial impedance and polarization. The classical measuring circuit is the Wheatstone bridge: a variable resistor is adjusted until the galvanometer reads zero, and $R_x$ is found from the balance condition of the bridge. Modern conductivity meters measure the ratio of ac voltage to current directly and often use a four-electrode cell to eliminate the effect of electrode polarization. The temperature coefficient of conductivity is about 2% per kelvin, so the measurement must be thermostatted or temperature-compensated (usually converted to $25\,^\circ\mathrm{C}$).

### 6.2.2. Applications

Purity of water: the conductivity of water reflects the total amount of ionic impurities in it and is an important index of water quality. Pure water contains only the $\ce{H+}$ and $\ce{OH-}$ from the self-dissociation of $\ce{H2O}$; at $25\,^\circ\mathrm{C}$ its theoretical conductivity is $5.5\,\mu\mathrm{S\,m^{-1}}$, that is, a resistivity of $18.2\,\mathrm{M\Omega\,cm}$ ([6.3.12](/6.3.12#sec-12.5.3)), which is the criterion for laboratory ultrapure water; ordinary distilled water has only about $1\,\mathrm{M\Omega\,cm}$ because of dissolved $\ce{CO2}$. Conductivity does not respond to nonionic impurities (organic matter, bacteria, suspended particles, dissolved gas molecules), so total organic carbon and microorganisms must be measured separately for ultrapure water.

**Conductometric titration** ([6.3.12](/6.3.12#sec-12.5.4)) needs no indicator and is suitable for colored and turbid solutions and for very dilute or very weak acids and bases. Conductivity detection is also the universal detector of ion chromatography ([6.4.14](/6.4.14#def-14.2.8)). The thermal conductivity cell measures the thermal conductivity of gases and not electrical conductivity; it is a detector of gas chromatography and is described in [6.4.13](/6.4.13#def-13.5.2). Semiconductor gas sensors and nanowire sensors are solid-state sensors and are not discussed in this chapter.

## 6.3. Potentiometry and Ion-Selective Electrodes

### 6.3.1. Indicator and Reference Electrodes

Potentiometry measures, at zero current, the emf of a cell composed of an **indicator electrode** and a **reference electrode**. The potential of the indicator electrode varies with the activity of the ion to be determined according to the Nernst equation, whereas the potential of the reference electrode is constant:

$$
E_{\mathrm{cell}} = E_{\mathrm{ind}} - E_{\mathrm{ref}} + E_{\mathrm{j}} = K \pm S\lg a_i, \qquad S = \frac{RT\ln10}{z_iF}, \tag{6.1}
$$
with the plus sign for cations and the minus sign for anions. At $25\,^\circ\mathrm{C}$ the Nernst slope is $S = 59.16\,\mathrm{mV}/z_i$, and $0.0592\,\mathrm{V}/z_i$ is often used in calculations. $K$ comprises the potential of the reference electrode, the liquid junction potential, and the constant term of the indicator electrode; it is not known in advance and must be calibrated with standard solutions.

The reference electrodes in common use are the **saturated calomel electrode** (SCE), with a potential of $0.2412\,\mathrm{V}$, and the $\ce{Ag}/\ce{AgCl}$ electrode in saturated $\ce{KCl}$ ($0.197\,\mathrm{V}$); data are in [6.3.13](/6.3.13#sec-13.5.2). The mercury-containing calomel electrode is being replaced by the $\ce{Ag}/\ce{AgCl}$ electrode. The reference electrode communicates with the sample solution through a liquid junction of porous ceramic or sintered glass. When the sample contains substances that react with $\ce{Cl-}$ or $\ce{Ag+}$ ($\ce{Ag+}$, $\ce{Hg^2+}$, sulfides, proteins), a double-junction reference electrode must be used, with a noninterfering electrolyte such as $\ce{KNO3}$ in the outer salt bridge. The measuring instrument must have a very high input impedance ($> 10^{12}\,\Omega$), because the resistance of sensing membranes such as glass is of the order of $10^8\,\Omega$, and the measuring current must be much smaller than $10^{-12}\,\mathrm{A}$ for the cell not to be polarized.

### 6.3.2. The pH Glass Electrode

The **glass electrode** ([6.3.13](/6.3.13#sec-13.9.3)) is a glass tube blown into a thin bulb at its lower end (membrane thickness about $0.1\,\mathrm{mm}$), filled with $0.1\,\mathrm{mol\,L^{-1}}$ $\ce{HCl}$ and containing an inner $\ce{Ag}/\ce{AgCl}$ reference electrode:

$$
\ce{Ag} \mid \ce{AgCl(s)} \mid \ce{HCl}(0.1\,\mathrm{mol\,L^{-1}}) \mid \text{glass membrane} \mid \text{sample solution}.
$$
The classical Corning 015 glass contains 22% $\ce{Na2O}$, 6% $\ce{CaO}$, and 72% $\ce{SiO2}$ (mole fractions).

Response mechanism. A membrane made of pure $\ce{SiO2}$ does not respond to $\ce{H+}$, because the network of silicon–oxygen tetrahedra contains no sites for ion exchange. When $\ce{Na2O}$ is added, some Si–O–Si bonds are broken to give $\ce{\equiv Si-O-}$ groups fixed in the network, with $\ce{Na+}$ as mobile counterions. A glass electrode must be soaked in water before use: the $\ce{Na+}$ at the membrane surface is exchanged with $\ce{H+}$ from the water,

$$
\ce{\equiv SiO- Na+ + H+ <=> \equiv SiO- H+ + Na+},
$$
and since this equilibrium lies strongly to the right, the soaked membrane consists of three layers: a very thin hydrated gel layer on each side (about $0.1\,\mu\mathrm{m}$, in which the exchange sites are almost entirely occupied by $\ce{H+}$) and a thick layer of dry glass in between (conduction by migration of $\ce{Na+}$).

In a measurement, $\ce{H+}$ exchange between the surface of each hydrated layer and the solution reaches equilibrium and gives a phase-boundary potential (of the same nature as the potential of the **Donnan equilibrium**, [6.3.21](/6.3.21#sec-21.9.5)), and inside the hydrated layers there is also a diffusion potential caused by the different migration rates of $\ce{H+}$ and $\ce{Na+}$. The membrane potential is the algebraic sum of these terms:

$$
E_{\mathrm{M}} = (E_{\text{b,out}} - E_{\text{b,in}}) + (E_{\text{d,out}} - E_{\text{d,in}}).
$$
If the two hydrated layers are identical, the two diffusion potentials are equal and opposite and cancel; each boundary potential varies as $\frac{RT}{F}\ln\frac{a(\ce{H+},\text{solution})}{a(\ce{H+},\text{gel})}$, and the activity of $\ce{H+}$ in the gel is the same on both sides, so that

$$
E_{\mathrm{M}} = \frac{RT}{F}\ln\frac{a(\ce{H+},\text{out})}{a(\ce{H+},\text{in})} = K' - 0.0592\,\mathrm{V}\times\mathrm{pH}(\text{out}) \quad (25\,^\circ\mathrm{C}). \tag{6.2}
$$
This is the Nernstian form of the **membrane potential** ([6.3.13](/6.3.13#sec-13.9.1)): the membrane does not allow ions to pass through but exchanges $\ce{H+}$ selectively at the two interfaces, and the result is the same as for an ideal membrane permeable only to $\ce{H+}$.

**Definition 6.3.1 (Asymmetry Potential)** When the solutions on the two sides of a glass membrane are identical, the membrane potential is not zero but has a difference of a few millivolts, called the **asymmetry potential**.

It arises from differences between the two surfaces in manufacture, hydration, and history of use (such as wear and contamination of the outer surface) and drifts slowly with time. The asymmetry potential is included in the constant of Eq. (6.2), so a glass electrode must be calibrated regularly with standard buffer solutions (Section 6.4.1).

**Definition 6.3.2 (Alkaline Error and Acid Error)** An ordinary pH glass electrode has a Nernstian response only over a certain pH range (about pH 1–10). In strongly basic solutions that contain a large amount of $\ce{Na+}$, the measured pH is lower than the true value, which is called the **alkaline error** (sodium error); in strongly acidic solutions (about pH < 1) the measured pH is higher than the true value, which is called the **acid error**.

The alkaline error arises because, when the activity of $\ce{H+}$ is very low, $\ce{Na+}$ in the solution also takes part in exchange in the hydrated layer, the electrode mistakes $\ce{Na+}$ for $\ce{H+}$, and the apparent $\ce{H+}$ activity is too high and the pH too low (for the quantitative relation see Section 6.3.3). Lithium glass, in which $\ce{Li2O}$ replaces $\ce{Na2O}$, extends the linear range to pH 12–13. The mechanism of the acid error is not fully understood and is generally thought to be related to the lowered activity of water in strong acid and to anions entering the gel layer. The response of ordinary glass to $\ce{Na+}$ at high pH is an error to be avoided and not a means of determining $\ce{Na+}$; sodium glass electrodes designed for $\ce{Na+}$ use an aluminosilicate glass containing $\ce{Al2O3}$ (for example 11% $\ce{Na2O}$, 18% $\ce{Al2O3}$) and respond selectively to $\ce{Na+}$ when the activity of $\ce{H+}$ is sufficiently low (the sample being adjusted with an alkaline buffer).

Nowadays laboratories almost always use combination pH electrodes, in which a glass electrode and an $\ce{Ag}/\ce{AgCl}$ reference electrode are mounted coaxially in one tube and the reference solution of the outer tube communicates with the sample through a side junction, so that a single electrode forms a complete cell.

### 6.3.3. Selectivity: The Nikolsky–Eisenman Equation

An ion-selective electrode is not specific, and coexisting ions respond more or less. The effect of coexisting ions is described by an empirical, semiquantitative equation.

**Definition 6.3.3 (Nikolsky–Eisenman Equation)** When the ion to be determined, $i$ (charge number $z_i$), and a coexisting ion $j$ (charge number $z_j$) are present together, the potential of an ion-selective electrode is

$$
E = K + \frac{RT\ln10}{z_iF}\lg\Big[a_i + \sum_j K^{\mathrm{pot}}_{i,j}\,a_j^{z_i/z_j}\Big], \tag{6.3}
$$
called the **Nikolsky–Eisenman equation**, where $K^{\mathrm{pot}}_{i,j}$ is the **potentiometric selectivity coefficient** of the electrode for $j$ (the slope has a negative sign for anion electrodes).

$K^{\mathrm{pot}}_{i,j}$ is the activity of $j$ that produces the same response as $i$ at unit activity: $K^{\mathrm{pot}}_{i,j} = 10^{-3}$ means that when the activity of $j$ is 1000 times that of $i$, the two contribute equally to the potential. The smaller the selectivity coefficient, the better the selectivity of the electrode for $i$. The relative error caused by the coexisting ion is

$$
\frac{\Delta a_i}{a_i} = \frac{K^{\mathrm{pot}}_{i,j}\,a_j^{z_i/z_j}}{a_i}\times100\%.
$$
The selectivity coefficient is not a thermodynamic constant and depends on the method of determination, the concentrations, and the state of the membrane. The methods recommended by IUPAC are the separate solution method (measuring solutions containing only $i$ and only $j$ and comparing the activities that give the same potential) and the fixed interference method (varying $a_i$ in a constant background of $j$ and finding the coefficient from the break point of the response curve); literature values are generally used only as a basis for estimating errors.

**Example 6.3.1** A pH glass electrode has $K^{\mathrm{pot}}_{\ce{H},\ce{Na}} = 1\times10^{-12}$. What pH is measured in a solution with $a(\ce{Na+}) = 1.0$ whose true pH is 12.00?

**Solution** By Eq. (6.3), the apparent activity sensed by the electrode is $a(\ce{H+}) + K^{\mathrm{pot}}_{\ce{H},\ce{Na}}a(\ce{Na+}) = 1.0\times10^{-12} + 1.0\times10^{-12} = 2.0\times10^{-12}$, so the measured $\mathrm{pH} = 11.70$ and the alkaline error is $-0.30$. With only 0.01 of $\ce{Na+}$ the error falls to $-0.004$, so the alkaline error is noticeable only when strong base and high salt occur together.

![Response of a pH glass electrode at 25 °C. Left: ideal Nernstian response (dashed) and the response calculated from the Nikolsky–Eisenman equation (K = 10⁻¹²) for three Na⁺ activities; the acid error at the strongly acidic end is schematic. Right: alkaline error (measured pH minus true pH) as a function of pH and Na⁺ activity](./plots/glass-electrode-errors.py)

**Example 6.3.2** The selectivity coefficient of a fluoride ion-selective electrode for $\ce{OH-}$ is about 0.1. For a sample with $a(\ce{F-}) = 1.0\times10^{-5}$, the error due to $\ce{OH-}$ must not exceed 1%. What is the highest permissible pH of the sample?

**Solution** We require $0.1\,a(\ce{OH-}) \le 0.01\times1.0\times10^{-5}$, that is, $a(\ce{OH-}) \le 1.0\times10^{-6}$ and $\mathrm{pH} \le 8.0$. At lower $\ce{F-}$ concentrations the permissible pH is lower, which is one reason the sample is adjusted to pH 5–6 in the determination of fluoride (the limit at the other end is discussed in Section 6.3.4).

### 6.3.4. Types of Ion-Selective Electrodes

According to the nature of the sensing membrane, ion-selective electrodes are classified as follows.

Crystalline membrane electrodes. The sensing membrane of the fluoride electrode is a single-crystal slice of $\ce{LaF3}$ doped with a little $\ce{EuF2}$ (0.1–0.2 mm thick), with an inner filling of $0.1\,\mathrm{mol\,L^{-1}}$ $\ce{NaF}$ and $0.1\,\mathrm{mol\,L^{-1}}$ $\ce{NaCl}$ and an $\ce{Ag}/\ce{AgCl}$ inner reference. A sparingly soluble salt used as a sensing membrane must have very low solubility and conduct at room temperature: after $\ce{Eu^2+}$ replaces $\ce{La^3+}$, $\ce{F-}$ vacancies appear in the lattice, and $\ce{F-}$ conducts by hopping along the vacancies. Exchange of $\ce{F-}$ between the membrane surface and the solution produces the membrane potential, $E = K - S\lg a(\ce{F-})$. The linear range of the fluoride electrode is about $10^{-1}$–$10^{-6}\,\mathrm{mol\,L^{-1}}$ and the detection limit about $10^{-7}\,\mathrm{mol\,L^{-1}}$ (limited by the solubility of $\ce{LaF3}$ itself). The selectivity is very high: $\ce{Cl-}$, $\ce{Br-}$, $\ce{I-}$, $\ce{NO3-}$, $\ce{SO4^2-}$, $\ce{PO4^3-}$, and $\ce{HCO3-}$ do not interfere even at 1000-fold excess, and the only serious interferent is $\ce{OH-}$. The useful pH range is about 5–7. At too high a pH, $\ce{OH-}$, which is close to $\ce{F-}$ in radius and has the same charge, takes part in exchange at the membrane surface (and forms $\ce{La(OH)3}$), giving a positive error (the measured $\ce{F-}$ is too high); at too low a pH, $\ce{F-}$ forms $\ce{HF}$ and $\ce{HF2-}$ ($\mathrm{p}K_{\mathrm{a}}(\ce{HF}) = 3.20$), the activity of free $\ce{F-}$ decreases, and a negative error results. Crystalline membranes based on $\ce{Ag2S}$ (or doped with $\ce{AgCl}$, $\ce{AgI}$, $\ce{CuS}$, or $\ce{PbS}$) can be made into electrodes for $\ce{Ag+}$, $\ce{S^2-}$, halide ions, $\ce{Cu^2+}$, and $\ce{Pb^2+}$.

Liquid membrane electrodes (mobile-carrier electrodes). The sensing membrane is a porous membrane (or a plasticized PVC membrane) soaked with a water-immiscible organic solution that contains an electroactive substance (the carrier) able to bind the ion to be determined. Unlike the exchange sites of a glass electrode, which are fixed in the framework, the carrier can move within the membrane but cannot leave it, and the ion to be determined is exchanged in and out at the membrane–water interface. The carrier of the $\ce{Ca^2+}$ electrode is calcium didecylphosphate dissolved in dioctyl phenylphosphonate, with $0.1\,\mathrm{mol\,L^{-1}}$ $\ce{CaCl2}$ as the inner filling. The linear range is about $10^{-1}$–$10^{-5}\,\mathrm{mol\,L^{-1}}$, $\ce{Ca^2+}$ can be determined in the presence of a 1000-fold excess of $\ce{Na+}$ or $\ce{K+}$, and the useful pH range is about 5.5–11; the drawback is that the organic solution is lost and the lifetime is short. By the charge of the carrier, liquid membrane electrodes are divided into those with negatively charged carriers (the $\ce{Ca^2+}$ electrode), those with positively charged carriers (quaternary ammonium salts, used for $\ce{NO3-}$ and $\ce{ClO4-}$ electrodes), and those with neutral carriers. The typical neutral carrier is valinomycin: the cavity of this cyclic depsipeptide just accommodates the dehydrated $\ce{K+}$, with $K^{\mathrm{pot}}_{\ce{K},\ce{Na}} \approx 10^{-4}$. Clinical blood electrolyte analyzers use a valinomycin $\ce{K+}$ electrode, a crown ether or sodium glass $\ce{Na+}$ electrode, an ionophore $\ce{Ca^2+}$ electrode, and a quaternary ammonium $\ce{Cl-}$ electrode, and a few tens of microliters of whole blood suffice to determine the activities of these ions simultaneously.

**Definition 6.3.4 (Gas-Sensing Electrode)** A complete electrochemical cell composed of an ion-selective electrode (usually a pH glass electrode), a reference electrode, an intermediate solution, and a gas-permeable membrane is called a **gas-sensing electrode**: the gas to be determined passes through a hydrophobic membrane that admits only gas molecules (such as a microporous polytetrafluoroethylene membrane), dissolves in a thin layer of intermediate solution between the membrane and the indicator electrode, and changes the activity of one ion there, which is measured by the indicator electrode.

For example, the intermediate solution of the ammonia gas-sensing electrode is $0.01\,\mathrm{mol\,L^{-1}}$ $\ce{NH4Cl}$, the pH rises when $\ce{NH3}$ permeates the membrane, and $\lg a(\ce{OH-})$ is linear in the partial pressure of $\ce{NH3}$ in the sample; the intermediate solution of the $\ce{CO2}$ electrode is $\ce{NaHCO3}$, and $\ce{CO2}$ lowers the pH. The sample is made basic (for $\ce{NH3}$) or acidic (for $\ce{CO2}$) so that the analyte is entirely in the form of gas molecules. The same principle is used for $\ce{SO2}$, $\ce{NO2}$, $\ce{H2S}$, $\ce{HCN}$, and $\ce{HF}$. The gas-sensing electrode is "not an electrode" but a miniature cell. Because of the selective permeability of the membrane it is free from interference by ions in the sample and can be used for turbid and colored samples.

**Definition 6.3.5 (Enzyme Electrode)** An electrode in which an enzyme is immobilized on the sensing surface of an ion-selective electrode, a gas-sensing electrode, or another electrode, and the enzyme-catalyzed reaction converts the substrate into a product that the electrode can detect (or consumes a reactant that the electrode can detect), so that the substrate is determined, is called an **enzyme electrode**.

Enzymes are highly selective for their substrates and catalyze efficiently at ordinary temperature and pressure, so an enzyme electrode combines the specificity of the enzyme with the simplicity of the electrode. Common products an electrode can detect are $\ce{CO2}$, $\ce{NH3}$, $\ce{NH4+}$, $\ce{H+}$, $\ce{O2}$ (consumption), and $\ce{H2O2}$. For example,

$$
\ce{CO(NH2)2 + H2O ->[\text{urease}] 2NH3 + CO2} \quad\text{(detected by an ammonia gas-sensing electrode, for urea)},
$$

$$
\ce{RCH(NH3+)COO- + O2 + H2O ->[\text{amino acid oxidase}] RCOCOO- + NH4+ + H2O2} \quad\text{(detected by an $\ce{NH4+}$ electrode or by detection of $\ce{H2O2}$)}.
$$
Glucose oxidase (GOx) catalyzes the oxidation of β-D-glucose by $\ce{O2}$ to D-glucono-δ-lactone (which then hydrolyzes to gluconic acid), with formation of $\ce{H2O2}$:

```smiles
OC[C@H]1O[C@@H](O)[C@H](O)[C@@H](O)[C@@H]1O.O=O>>OC[C@H]1OC(=O)[C@H](O)[C@@H](O)[C@@H]1O.OO
```

Either detecting the consumption of $\ce{O2}$ with an $\ce{O2}$ electrode or detecting the $\ce{H2O2}$ formed with a Pt electrode allows glucose to be determined; practical glucose sensors mostly use amperometry rather than potentiometry, see Section 6.7.1.

If tissue slices of animals or plants, which contain the enzymes in their natural state, are used in place of purified enzymes, a tissue electrode results: the enzyme source is plentiful, the enzymes are more stable in the cells and last longer, and the electrode is simple to make; the key is the immobilization of the biological tissue membrane (physical adsorption, covalent attachment, crosslinking, or entrapment). An immunoelectrode, in which an antibody or antigen is immobilized on the electrode surface and the change in potential or current caused by the immune reaction is measured, is another type. All of these are **biosensors** in the sense of Section 6.7.2.

## 6.4. Direct Potentiometry and Potentiometric Titration

### 6.4.1. Direct Potentiometry and the Determination of pH

**Definition 6.4.1 (Direct Potentiometry)** The method in which the emf of a cell composed of an indicator electrode and a reference electrode is measured and the activity (or concentration) of the ion to be determined is obtained directly from Eq. (6.1) is called **direct potentiometry**.

Because $K$ is unknown, direct potentiometry is always a relative measurement: $K$ is first determined with a standard solution and the sample is then measured. The determination of pH is the most important example and uses the IUPAC operational definition ([6.3.13](/6.3.13#sec-13.7.6)):

$$
\mathrm{pH(X)} = \mathrm{pH(S)} - \frac{E_{\mathrm{X}} - E_{\mathrm{S}}}{RT\ln10/F},
$$
where $E$ is the emf of "glass electrode minus reference electrode" and S is a standard buffer solution of known pH. Since the actual slope of a glass electrode is often slightly smaller than the theoretical value, a pH meter is calibrated at two points with two standard buffers (for example pH 4.005 and 6.865, or 6.865 and 9.180): the first determines $K$ (offset) and the second the slope, and the slope of a normal electrode should be 95%–102% of the theoretical value. The pH of the sample should lie between those of the two standards, and the temperature should be the same as in the calibration.

### 6.4.2. Calibration Curve Method and Control of Ionic Strength

An ion-selective electrode responds to the activity $a_i = \gamma_i c_i$, whereas the analysis requires the concentration. If the sample and the standard solutions have the same **ionic strength**, their **activity coefficients** are also the same (Debye–Hückel theory, [6.3.12](/6.3.12#sec-12.7)), $\gamma_i$ can be absorbed into the constant, $E$ is linear in $\lg c_i$, and the determination can be made with a **calibration curve**. There are two ways to control the ionic strength:

1. Constant ionic background: when the main components of the samples are the same and the ionic strength is roughly constant (as in seawater), the standard series is prepared in an artificial solution similar in composition to the sample.
2. Addition of an ionic strength adjuster: equal amounts of a concentrated electrolyte are added to the standards and the samples, so that the ionic strength is determined by it.

**Definition 6.4.2 (Total Ionic Strength Adjustment Buffer)** A solution composed of a large amount of a noninterfering electrolyte, a pH buffer system, and a masking agent, added in a fixed proportion to the standards and the samples to control the ionic strength and the pH and to eliminate interfering ions at the same time, is called a **total ionic strength adjustment buffer** (TISAB).

One TISAB used for the determination of $\ce{F-}$ consists of about $1\,\mathrm{mol\,L^{-1}}$ $\ce{NaCl}$, $0.25\,\mathrm{mol\,L^{-1}}$ $\ce{HAc}$ with $0.75\,\mathrm{mol\,L^{-1}}$ $\ce{NaAc}$, and $0.001\,\mathrm{mol\,L^{-1}}$ sodium citrate, mixed with the sample in equal volumes. The three components each have a function. $\ce{NaCl}$ makes the ionic strength high and constant, so that activity coefficients do not vary from sample to sample. The $\ce{HAc}$–$\ce{NaAc}$ buffer holds the pH at 5.0–5.5 ($\mathrm{p}K_{\mathrm{a}} = 4.76$, [6.4.2](/6.4.2#sec-2.4.2)), which avoids both the formation of $\ce{HF}$ and interference by $\ce{OH-}$ (Section 6.3.4). Citrate (or the stronger CDTA) provides **masking** of $\ce{Al^3+}$ and $\ce{Fe^3+}$ and releases the $\ce{F-}$ bound by them, so that the total fluoride is measured.

### 6.4.3. Standard Addition and the Gran Plot

When the matrix of the sample is complex and it is difficult to prepare standards of similar composition, the **standard addition method** (Definition 1.8.8) is used. For a sample of volume $V_x$ and concentration $c_x$ the measured potential is $E_1 = K + S\lg(\gamma c_x)$; after addition of a volume $V_{\mathrm{s}}$ of a standard solution of concentration $c_{\mathrm{s}}$ ($c_{\mathrm{s}} \gg c_x$ and $V_{\mathrm{s}} \ll V_x$, so that the ionic strength and $\gamma$ do not change), the measured potential is

$$
E_2 = K + S\lg\left[\gamma\,\frac{c_xV_x + c_{\mathrm{s}}V_{\mathrm{s}}}{V_x + V_{\mathrm{s}}}\right].
$$
Subtracting and setting $\Delta E = E_2 - E_1$ and $\Delta c = \dfrac{c_{\mathrm{s}}V_{\mathrm{s}}}{V_x + V_{\mathrm{s}}}$ gives

$$
c_x = \Delta c\left(10^{\Delta E/S} - \frac{V_x}{V_x + V_{\mathrm{s}}}\right)^{-1} \approx \Delta c\left(10^{\Delta E/S} - 1\right)^{-1}. \tag{6.4}
$$
The approximate form holds when $V_{\mathrm{s}} \ll V_x$ (so that $\Delta c \approx c_{\mathrm{s}}V_{\mathrm{s}}/V_x$). For an anion electrode $S$ is negative and so is $\Delta E$, and $\Delta E/S$ remains positive. The slope $S$ is best measured in the same sample solution (for example by diluting the solution two-fold after the addition and measuring the change in potential).

**Example 6.4.1** To $50.0\,\mathrm{mL}$ of a fluoride sample solution (with TISAB already added), $0.50\,\mathrm{mL}$ of $1.00\times10^{-2}\,\mathrm{mol\,L^{-1}}$ $\ce{NaF}$ standard solution is added, and the emf decreases by $17.8\,\mathrm{mV}$. The measured electrode slope is $-58.5\,\mathrm{mV}$. Find the concentration of $\ce{F-}$ in the sample.

**Solution** $\Delta c = 1.00\times10^{-2}\times0.50/50.5 = 9.90\times10^{-5}\,\mathrm{mol\,L^{-1}}$ and $10^{\Delta E/S} = 10^{17.8/58.5} = 2.015$. From the exact form of Eq. (6.4), $c_x = 9.90\times10^{-5}/(2.015 - 0.990) = 9.66\times10^{-5}\,\mathrm{mol\,L^{-1}}$; the approximate form gives $9.85\times10^{-5}\,\mathrm{mol\,L^{-1}}$, 2% too high. The added standard roughly doubles the concentration, so that $\Delta E$ is more than ten millivolts and the reading error has little effect; this is the rule of thumb for choosing the amount added.

A single standard addition is simple and suited to small samples, but it uses only two points and its accuracy is limited. Multiple additions with linearization of the exponential relation give the Gran plot.

**Definition 6.4.3 (Gran Plot)** The Nernst relation is rewritten as $(V_x + V_{\mathrm{s}})\,10^{E/S} = 10^{K/S}\gamma\,(c_xV_x + c_{\mathrm{s}}V_{\mathrm{s}})$. The left-hand side (the Gran function) is plotted against the added volume $V_{\mathrm{s}}$ to give a straight line, which is extrapolated to zero Gran function, and $c_x$ is obtained from the intercept $V_{\mathrm{s}}^0 = -c_xV_x/c_{\mathrm{s}}$ on the horizontal axis. This method is called the **Gran plot** (Gran method).

The Gran plot does not require $K$ to be known, fits a straight line to many points (by **least squares**, [3.3.2](/3.3.2)), and also shows from any curvature of the line whether the slope is correct. Special semilogarithmic Gran paper was once printed for it; software now does the work. The same linearization is used for potentiometric titration (Section 6.4.5).

### 6.4.4. Accuracy of Direct Potentiometry

Differentiating Eq. (6.1) gives $\mathrm{d}E = \frac{RT}{z_iF}\frac{\mathrm{d}c}{c}$, so that the relative error in concentration caused by an error $\Delta E$ in the emf measurement is

$$
\frac{\Delta c}{c} = \frac{z_iF}{RT}\,\Delta E \approx 3.9\%\times z_i \quad(\Delta E = \pm1\,\mathrm{mV},\ 25\,^\circ\mathrm{C}). \tag{6.5}
$$
This is about ±3.9% for a monovalent ion and about ±7.8% for a divalent ion (calculated exactly from the exponential relation, $10^{1/59.16} - 1 = 4.0\%$ for a monovalent ion, usually rounded to 4% and 8%). The error is independent of concentration, so direct potentiometry is suited to rapid determination over a wide concentration range but cannot reach the accuracy of one part per thousand of titrimetric analysis. The 1 mV uncertainty comes mainly from the liquid junction potential and temperature variation and is hard to reduce further. Potentiometric titration is used when high accuracy is required.

### 6.4.5. Potentiometric Titration

**Definition 6.4.4 (Potentiometric Titration)** The method in which the potential of an indicator electrode (against a reference electrode) is measured during a titration and the end point is determined from the jump of the potential as a function of titrant volume is called **potentiometric titration**.

Potentiometric titration measures the relative change of potential and not its absolute value, so uncertainties in the liquid junction potential, the activity coefficients, and the electrode constant do not affect the result, and the accuracy is the same as that of classical titration. It needs no indicator, is suitable for colored and turbid solutions, for titrations in nonaqueous solvents, and for systems for which no suitable indicator exists, and is easily automated (an automatic potentiometric titrator reduces the volume of each addition automatically according to the rate of change of potential). The indicator electrodes for the various types of titration are:

| Type of titration | Indicator electrode | Example |
|---|---|---|
| Acid–base | pH glass electrode | Weak acids, polyprotic acids, nonaqueous titrations |
| Precipitation | Ag electrode or $\ce{Ag2S}$ crystalline membrane electrode | Titration of halide ions with $\ce{AgNO3}$ |
| Complexometric | The corresponding ion-selective electrode, or the $\ce{Hg}\mid\ce{HgY^2-}$ electrode | EDTA titration of $\ce{Ca^2+}$, $\ce{Cu^2+}$ |
| Redox | Pt electrode | Titration of $\ce{Fe^2+}$ with $\ce{Ce^4+}$ |

The potentiometric titration curve of a **redox titration** is the titration curve calculated in [6.4.5](/6.4.5#sec-5.3.1) (for the titration of $\ce{Fe^2+}$ with $\ce{Ce^4+}$, for example, $E$ at 50% titrated equals the **formal potential** of $\ce{Fe^3+}/\ce{Fe^2+}$, the equivalence point is at about 1.06 V, and the jump extends from 0.86 V to 1.26 V). The end point can be determined by:

1. the inflection point of the $E$–$V$ curve (the midline between two tangents);
2. the maximum of the plot of the first derivative $\Delta E/\Delta V$ against $V$;
3. the point at which the second derivative $\Delta^2E/\Delta V^2 = 0$, by linear interpolation between two second derivatives of opposite sign: $V_{\mathrm{ep}} = V_1 + \Delta V\,\dfrac{(\Delta^2E/\Delta V^2)_1}{(\Delta^2E/\Delta V^2)_1 - (\Delta^2E/\Delta V^2)_2}$;
4. the Gran plot: a straight line fitted to the data before (or after) the end point is extrapolated, so that points near the end point are not needed; this suits dilute solutions and weak acids and bases for which the jump is not distinct.

![Titration of 50.00 mL of 0.0500 mol/L NaCl with 0.1000 mol/L AgNO₃ at 25 °C, Ag electrode against a saturated calomel electrode: the titration curve, its first and second derivatives, and the Gran functions before and after the end point (scaled); both Gran lines extrapolate to 25.00 mL](./plots/gran-plot.py)

In the figure, before the end point $[\ce{Cl-}] \approx (c_0V_0 - cV)/(V_0 + V)$ and $E = E^\circ(\ce{Ag+}/\ce{Ag}) + S\lg K_{\mathrm{sp}} - S\lg[\ce{Cl-}] - E_{\mathrm{SCE}}$, so $(V_0 + V)10^{-E/S} \propto c_0V_0 - cV$ decreases linearly with $V$ and is zero at the equivalence point; after the end point $(V_0 + V)10^{E/S} \propto cV - c_0V_0$ increases linearly. The two lines meet at the same point, and the end point obtained in this way is not affected by the dissolution of $\ce{AgCl}$ (which displaces the points near the jump).

### 6.4.6. Patch Clamp and Measurement of Cell Membrane Potential

The difference in ion concentration across a cell membrane produces the resting potential (about $-70\,\mathrm{mV}$, [6.3.13](/6.3.13#sec-13.9.2)), and signals in nerve and muscle cells are changes in membrane potential caused by the opening and closing of ion channels. A glass microelectrode with a tip of about $1\,\mu\mathrm{m}$, filled with electrolyte and containing an $\ce{Ag}/\ce{AgCl}$ wire, is inserted into the cell (a second $\ce{Ag}/\ce{AgCl}$ electrode is placed in the extracellular fluid), and the membrane potential can be measured directly. This is a potential measurement on a living organism.

**Definition 6.4.5 (Patch Clamp)** The technique in which a glass microelectrode with a polished tip is pressed lightly against a cell membrane and gentle suction is applied, so that a high-resistance seal of more than $1\,\mathrm{G\Omega}$ forms between the tip and the membrane, electrically isolating the small piece of membrane (the patch) under the pipette opening from its surroundings, and the ionic current flowing through this patch is measured while the membrane potential is controlled (voltage clamp), is called the **patch clamp**.

The high-resistance seal makes the leakage current and thermal noise extremely small, so that currents of 1–10 pA when a single ion channel opens can be resolved and the channel is seen to jump randomly between its open and closed states. Varying the clamping potential and adding ligands or drugs to the solution allow the conductance, selectivity, and gating kinetics of the channel to be studied. Depending on the operations after sealing, there are the cell-attached, whole-cell (the patch is ruptured and the current of the entire cell measured), inside-out, and outside-out recording configurations; in current-clamp mode the membrane potential itself is measured. Neher and Sakmann received the 1991 Nobel Prize in Physiology or Medicine for inventing the patch clamp technique. The patch clamp took electrochemical measurement to the single-molecule level, and automated planar patch clamp is now used for high-throughput screening of drug toxicity at the cardiac hERG potassium channel. The electrophysiology of neurons is treated in [Neurobiology](/7.16).

## 6.5. Electrolysis and Coulometry

### 6.5.1. Decomposition Voltage and Applied Voltage

Electrolysis and coulometry are based on the mass of substance deposited or the quantity of charge consumed during electrolysis. In an electrolytic cell, when the applied voltage is small, only a feeble residual current flows; when the voltage is increased to a certain value, the current rises rapidly and the electrolysis continues. This voltage is the **decomposition voltage** ([6.1.12](/6.1.12#sec-12.4.2), [6.3.14](/6.3.14#sec-14.1.1)). The actual decomposition voltage is greater than the theoretical decomposition voltage calculated from the Nernst equation (the emf of the galvanic cell formed by the electrolysis products), because both electrodes are polarized when a current passes, the cathode potential becoming more negative than its equilibrium value and the anode potential more positive, and because the $IR$ drop across the solution resistance must also be overcome:

$$
U = (E_{\mathrm{a}} - E_{\mathrm{c}})_{\mathrm{eq}} + \eta_{\mathrm{a}} + \lvert\eta_{\mathrm{c}}\rvert + IR,
$$
where $\eta$ is the **overpotential**.

**Example 6.5.1** A solution of $1.0\,\mathrm{mol\,L^{-1}}$ $\ce{CuSO4}$ and $0.5\,\mathrm{mol\,L^{-1}}$ $\ce{H2SO4}$ is electrolyzed between Pt electrodes ($25\,^\circ\mathrm{C}$, concentrations used in place of activities). Cu is deposited at the cathode and $\ce{O2}$ evolved at the anode. The theoretical decomposition voltage is $E(\ce{O2}/\ce{H2O}) - E(\ce{Cu^2+}/\ce{Cu}) = (1.229 + 0.0592\lg[\ce{H+}]) - (0.342 + 0.0296\lg 1.0) = 1.229 - 0.342 = 0.89\,\mathrm{V}$ ($[\ce{H+}] \approx 1\,\mathrm{mol\,L^{-1}}$). The overpotential of $\ce{O2}$ on Pt is about 0.70 V (the overpotential for deposition of Cu is very small), and for a current of 0.10 A and a solution resistance of 0.50 Ω, $IR = 0.050\,\mathrm{V}$, so that the actual decomposition voltage is about $0.89 + 0.70 + 0.05 = 1.64\,\mathrm{V}$, in agreement with experiment.

### 6.5.2. Electrogravimetry

**Definition 6.5.1 (Electrogravimetry)** The method in which the sample solution is electrolyzed so that the ion to be determined is deposited quantitatively on an electrode as the metal (or as an oxide such as $\ce{PbO2}$), and the content is found from the increase in mass of the electrode, is called **electrogravimetry** (electrogravimetric analysis).

Electrogravimetry requires no standard substance, can reach an accuracy of 0.1%, and is the classical method for major elements such as Cu in alloys. According to which quantity is controlled there are two types.

Constant-current electrolysis: the current (usually 0.5–2 A) is held constant and the electrolysis is fast. As the concentration of the ion to be determined falls, the cathode potential shifts continuously to more negative values until the next electrode reaction (usually hydrogen evolution) begins. It can therefore separate only metals whose deposition potentials lie above that of hydrogen (more positive than hydrogen) from those below it, as in the determination of Cu in acidic solution where $\ce{Ni^2+}$ is not deposited. It cannot separate metals that are both above hydrogen ($\ce{Ag+}$ and $\ce{Cu^2+}$) or both below it ($\ce{Zn^2+}$ and $\ce{Cd^2+}$).

Controlled-potential electrolysis: a three-electrode system (working, counter, and reference electrodes) and a potentiostat hold the cathode potential at a constant value, so that the metal to be determined is deposited completely while coexisting metals are not (for the order of deposition of metals see [6.3.14](/6.3.14#sec-14.5.2)). The selectivity is good, but the current decreases as the concentration falls and the electrolysis takes a long time.

**Example 6.5.2** A solution contains about $0.1\,\mathrm{mol\,L^{-1}}$ each of $\ce{Cd^2+}$ and $\ce{Zn^2+}$ and is to be separated by controlled-cathode-potential electrolysis. $E^\circ(\ce{Cd^2+}/\ce{Cd}) = -0.403\,\mathrm{V}$ and $E^\circ(\ce{Zn^2+}/\ce{Zn}) = -0.762\,\mathrm{V}$. We regard $\ce{Cd^2+}$ as completely deposited when it has fallen to $10^{-6}\,\mathrm{mol\,L^{-1}}$, at which point the cathode potential is $-0.403 + 0.0296\lg10^{-6} = -0.580\,\mathrm{V}$; the potential at which $\ce{Zn}$ begins to deposit is $-0.762 + 0.0296\lg0.1 = -0.791\,\mathrm{V}$. Therefore, if the cathode potential is controlled between $-0.58$ and $-0.79\,\mathrm{V}$ (vs SHE), for example at $-0.70\,\mathrm{V}$, that is, $-0.70 - 0.24 = -0.94\,\mathrm{V}$ (vs SCE), $\ce{Cd}$ is completely deposited and $\ce{Zn}$ is not. The overpotential for hydrogen on Cd is large, so hydrogen evolution does not interfere.

In controlled-potential electrolysis the current decays exponentially. Let the electrode area be $A$, the solution volume $V$, and the diffusion layer thickness under stirring $\delta$; from the **limiting diffusion current** $I = zFADc/\delta$ ([6.3.14](/6.3.14#sec-14.4.1)) and $-V\,\mathrm{d}c/\mathrm{d}t = I/(zF)$,

$$
c(t) = c_0\,\mathrm{e}^{-kt},\qquad I(t) = I_0\,\mathrm{e}^{-kt},\qquad k = \frac{DA}{V\delta}. \tag{6.6}
$$
When the current has fallen to 0.1% of its initial value, 99.9% of the analyte has been deposited, which is the criterion for completeness of electrolysis (a small portion of the solution can also be tested for the ion to be determined); increasing the electrode area, stirring more vigorously (reducing $\delta$), and reducing the solution volume all shorten the electrolysis time.

Mercury-cathode electrolysis, with a mercury pool as cathode, was once used for separations: the overpotential for hydrogen on mercury is large, and many metals dissolve in the mercury as amalgams after deposition. It can remove large amounts of matrix metals (such as Fe in steel samples) so that trace components that do not deposit on mercury (Al, Ti, rare earths, and others) can be determined; because mercury is toxic it is now seldom used.

### 6.5.3. Coulometry

**Definition 6.5.2 (Coulometry)** The method in which the quantity of charge consumed in the complete reaction of the analyte at an electrode is measured and its content is found from Faraday's laws of electrolysis is called **coulometry** (coulometric analysis):

$$
m = \frac{QM}{zF}, \tag{6.7}
$$
where $Q$ is the charge, $M$ the molar mass, $z$ the number of electrons transferred in the electrode reaction, and $F = 96485.33212\,\mathrm{C\,mol^{-1}}$ the Faraday constant.

$F = N_{\mathrm{A}}e$ is an exact value given by two defining constants of the SI. **Faraday's laws of electrolysis** ([6.1.12](/6.1.12#sec-12.4.3)) themselves have no exceptions; the prerequisite for coulometry is 100% **current efficiency**: all of the charge must be used for the electrode reaction of the analyte, with no electrolysis of the solvent, reaction of impurities, or side reactions of the product. Coulometry therefore needs no standard substance or calibration, is an absolute method, and can determine microgram quantities of substances.

Controlled-potential coulometry: the potential of the working electrode is controlled as in controlled-potential electrolysis to ensure selectivity and 100% current efficiency; the current decays according to Eq. (6.6), and the charge $Q = \int_0^t I\,\mathrm{d}t$ is measured by a coulometer in series. Early instruments used chemical coulometers: the silver coulometer (weighing the Ag deposited) and the hydrogen–oxygen gas coulometer, in which a $0.5\,\mathrm{mol\,L^{-1}}$ $\ce{K2SO4}$ solution is electrolyzed and the total volume of $\ce{H2}$ at the cathode and $\ce{O2}$ at the anode is measured. Each coulomb of charge corresponds to $\frac{1}{F}\,\mathrm{mol}$ of electrons and produces $\frac{1}{2F}\,\mathrm{mol}$ of $\ce{H2}$ and $\frac{1}{4F}\,\mathrm{mol}$ of $\ce{O2}$, whose volume at $0\,^\circ\mathrm{C}$ and $101.325\,\mathrm{kPa}$ is

$$
\frac{3}{4F}\times22.414\,\mathrm{L\,mol^{-1}} = 1.742\times10^{-4}\,\mathrm{L} = 0.1742\,\mathrm{mL}.
$$
The measured gas volume is first converted to these conditions with the ideal gas law and then divided by 0.1742 mL to give the charge. Today electronic integrators integrate the current directly.

### 6.5.4. Coulometric Titration

In controlled-potential coulometry the current becomes smaller and smaller and the analysis takes a long time. If constant-current electrolysis is used instead, the charge is simply $Q = It$, but at constant current the potential of the working electrode shifts as the analyte is consumed and eventually causes other electrode reactions, destroying the 100% current efficiency. The remedy is to let the electrode reaction generate a reagent that then reacts chemically with the analyte.

**Definition 6.5.3 (Coulometric Titration)** The method in which an auxiliary electrolyte is electrolyzed at constant current to generate at the working electrode a titrant that reacts rapidly and quantitatively with the analyte, the end point is indicated by chemical or instrumental means, and the amount of analyte is found from the current $I$ and the time $t$ to reach the end point by $Q = It$ is called **coulometric titration** (constant-current coulometry).

Take the determination of $\ce{Fe^2+}$ as an example. When $\ce{Fe^2+}$ is oxidized directly at the anode, the anode potential shifts positively as $\ce{Fe^2+}$ decreases and eventually reaches the potential at which water is oxidized to $\ce{O2}$, so the current efficiency falls below 100%. If a large amount of $\ce{Ce^3+}$ is added to the solution as an auxiliary electrolyte, $\ce{Ce^3+}$ is oxidized when the anode potential reaches the potential of $\ce{Ce^4+}/\ce{Ce^3+}$ (its concentration is large enough to carry the entire current, and the anode potential is "clamped" there), and the $\ce{Ce^4+}$ formed immediately oxidizes $\ce{Fe^2+}$ in the solution:

$$
\ce{Ce^3+ -> Ce^4+ + e-},\qquad \ce{Ce^4+ + Fe^2+ -> Ce^3+ + Fe^3+}.
$$
The overall effect is the same as the direct oxidation of $\ce{Fe^2+}$ at the electrode, and all the charge is attributed to $\ce{Fe^2+}$. Commonly used electrogenerated titrants are:

| Type of titration | Working electrode reaction | Electrogenerated titrant and application |
|---|---|---|
| Acid–base | Cathode $\ce{2H2O + 2e- -> H2 + 2OH-}$; anode $\ce{H2O -> 1/2 O2 + 2H+ + 2e-}$ | $\ce{OH-}$ titrates acids, $\ce{H+}$ titrates bases |
| Precipitation | Anode $\ce{Ag -> Ag+ + e-}$ | $\ce{Ag+}$ titrates $\ce{Cl-}$, $\ce{Br-}$, $\ce{I-}$, thiols |
| Complexometric | Cathode $\ce{HgY^2- + 2e- -> Hg + Y^4-}$ | EDTA ($\ce{Y^4-}$) titrates $\ce{Ca^2+}$, $\ce{Zn^2+}$, and others |
| Redox | Anode $\ce{2Br- -> Br2 + 2e-}$, $\ce{2I- -> I2 + 2e-}$, $\ce{Ce^3+ -> Ce^4+ + e-}$ | $\ce{Br2}$ titrates As(III), Sb(III), phenols, alkenes; $\ce{I2}$ titrates $\ce{S2O3^2-}$, As(III), water (Karl Fischer) |

The end point of a coulometric titration can be detected with an indicator, potentiometrically, or by the following two-electrode current method.

**Definition 6.5.4 (Biamperometric End-Point Detection)** The method in which two identical Pt indicator electrodes are placed in the sample solution, a small constant voltage (about 10–200 mV) is applied between them, and the end point is determined from the sudden appearance or disappearance of the current through the two electrodes at the end point is called **biamperometric end-point detection** (dead-stop end-point detection, double-indicator-electrode current method).

It rests on the different behavior of reversible and irreversible couples at a small voltage. A current requires that one oxidation and one reduction occur at the two electrodes at the same time. When both the oxidized and reduced forms of a reversible couple (such as $\ce{Br2}/\ce{Br-}$, $\ce{I2}/\ce{I-}$, $\ce{Fe^3+}/\ce{Fe^2+}$) are present, the exchange current is large, a very small voltage suffices to reduce the oxidized form at one electrode and oxidize the reduced form at the other, and the current produced is proportional to the concentration of the less abundant form; with only one form present there is no current. An irreversible couple (such as As(V)/As(III) or $\ce{S4O6^2-}/\ce{S2O3^2-}$) does not react at all at such a small voltage. Take the titration of As(III) with electrogenerated $\ce{Br2}$ (in $0.2\,\mathrm{mol\,L^{-1}}$ $\ce{NaBr}$ and $0.1\,\mathrm{mol\,L^{-1}}$ $\ce{H2SO4}$, with 150 mV between the two indicator electrodes). Before the end point the electrogenerated $\ce{Br2}$ is consumed at once by As(III), the solution contains only $\ce{Br-}$ and the irreversible arsenic couple (about 0.9 V would be needed to make it react on Pt), and the indicator current is zero; beyond the end point $\ce{Br2}$ and $\ce{Br-}$ are present together and the current rises abruptly. Conversely, when reversible $\ce{I2}$ is titrated with irreversible $\ce{S2O3^2-}$, the current falls to zero at the end point and stays there, which is the origin of the name "dead stop".

The characteristics of coulometric titration are:

1. No standard solution needs to be prepared or standardized, and current and time can be measured very accurately (relative error about 0.1%–0.2%), so the method is often used to assign values to primary standards.
2. The titrant is generated in situ and reacts at once, so unstable titrants that are hard to store can be used, such as $\ce{Br2}$, $\ce{Cl2}$, $\ce{Cu+}$, and $\ce{Ti^3+}$.
3. The current can be as small as a microampere, which suits the determination of trace substances (of the order of $10^{-5}$–$10^{-9}\,\mathrm{g}$).
4. Automation and continuous monitoring are easy.

*Karl Fischer titration* determines water by the quantitative reaction of $\ce{I2}$ with water; its coulometric form (Karl Fischer coulometry) is the most widely used coulometric titration today and is used for trace water. In an alcoholic solution containing $\ce{I-}$, $\ce{SO2}$, and an organic base (imidazole and others, written RN), $\ce{I2}$ is generated electrolytically at the anode and, in the presence of the base, reacts with water in a 1:1 ratio:

$$
\ce{H2O + I2 + SO2 + CH3OH + 3RN -> [RNH]SO4CH3 + 2[RNH]I}.
$$
One mole of water consumes 1 mol of $\ce{I2}$, that is, a charge of $2F$, so 1 mg of water corresponds to $\frac{10^{-3}}{18.015}\times2\times96485 = 10.71\,\mathrm{C}$. The end point is detected by two Pt electrodes responding to excess $\ce{I2}$ ($\ce{I2}/\ce{I-}$ is a reversible couple). The method needs no standardization of the titer (as the volumetric Karl Fischer method does), can determine micrograms of water, and is used for water in drugs, solvents, lithium-battery electrolytes, and petroleum products.

## 6.6. Voltammetry

### 6.6.1. Voltammetry and Polarographic Waves

**Definition 6.6.1 (Voltammetry)** The analytical methods in which a sample solution is electrolyzed at a working electrode of small area, the potential of the working electrode is varied in a prescribed manner, and the curve of current against potential (the voltammogram) is recorded, with the potential on the curve used for qualitative analysis and the magnitude of the current for quantitative analysis, are collectively called **voltammetry**. When the working electrode is a dropping mercury electrode, the method is called **polarography** ([6.3.14](/6.3.14#sec-14.4.3)).

The current in voltammetry is limited by diffusion of the electroactive substance to the electrode surface, and the theoretical basis is the **limiting diffusion current**, the **Cottrell equation**, and the Ilkovič equation for the dropping mercury electrode in [6.3.14](/6.3.14#sec-14.4); here only the shape of the current–potential curve and its analytical applications are discussed.

Take $\ce{Cd^2+ + 2e- + Hg -> Cd(Hg)}$ as an example. A classical polarogram has three parts. Before the potential has become negative enough to reduce $\ce{Cd^2+}$, only a very small residual current flows (including the reduction current of impurities and the charging current, Section 6.6.3). When the potential becomes negative enough for $\ce{Cd^2+}$ to begin to be reduced, the current rises rapidly. As the potential becomes more negative still, the concentration of $\ce{Cd^2+}$ at the electrode surface falls to zero and the current reaches a plateau determined by the rate of diffusion, the limiting diffusion current $I_{\mathrm{d}}$. $I_{\mathrm{d}}$ is proportional to the bulk concentration and is the basis of quantitative analysis.

**Definition 6.6.2 (Half-Wave Potential)** The potential on a voltammetric curve (polarographic wave) at which the current equals half the limiting diffusion current is called the **half-wave potential**, written $E_{1/2}$.

For a reversible polarographic wave, $E_{1/2}$ is independent of concentration and depends only on the couple and the medium, which is the basis of qualitative analysis. Suppose the reduction $\ce{O + ze- -> R}$ is very fast and the surface concentrations satisfy the Nernst equation (a reversible wave), with the product R dissolving in the mercury or the solution. The relation between surface concentration and current is given by diffusion: the current is $I = k_{\mathrm{O}}[c_{\mathrm{O}}^* - c_{\mathrm{O}}(0)]$, $I_{\mathrm{d}} = k_{\mathrm{O}}c_{\mathrm{O}}^*$, and diffusion of the product away gives $I = k_{\mathrm{R}}c_{\mathrm{R}}(0)$, where $k_{\mathrm{O}}$ and $k_{\mathrm{R}}$ are proportional to $D^{1/2}$. Then $c_{\mathrm{O}}(0) = (I_{\mathrm{d}} - I)/k_{\mathrm{O}}$ and $c_{\mathrm{R}}(0) = I/k_{\mathrm{R}}$, and substitution into the Nernst equation gives

$$
E = E^{\circ\prime} + \frac{RT}{zF}\ln\frac{c_{\mathrm{O}}(0)}{c_{\mathrm{R}}(0)} = E^{\circ\prime} + \frac{RT}{zF}\ln\frac{k_{\mathrm{R}}}{k_{\mathrm{O}}} + \frac{RT}{zF}\ln\frac{I_{\mathrm{d}} - I}{I}.
$$
The last term vanishes at $I = I_{\mathrm{d}}/2$, so that

$$
E = E_{1/2} + \frac{RT}{zF}\ln\frac{I_{\mathrm{d}} - I}{I},\qquad E_{1/2} = E^{\circ\prime} + \frac{RT}{2zF}\ln\frac{D_{\mathrm{R}}}{D_{\mathrm{O}}} \approx E^{\circ\prime}. \tag{6.8}
$$
This is the equation of a reversible polarographic wave. A plot of $E$ against $\lg\frac{I_{\mathrm{d}} - I}{I}$ should be a straight line of slope $59.2/z\,\mathrm{mV}$ ($25\,^\circ\mathrm{C}$), which can be used to test whether the electrode reaction is reversible and to find $z$. If several ions are present in the solution and their $E_{1/2}$ differ by 0.2 V or more, several separate step-shaped waves are obtained, whose heights are proportional to the respective concentrations.

Metal ions that form complexes are harder to reduce and $E_{1/2}$ shifts negatively. For the reversible reduction of $\ce{ML_p}$ (with approximately equal diffusion coefficients), the Lingane relation is

$$
\Delta E_{1/2} = -\frac{RT}{zF}\ln\beta_p - p\,\frac{RT}{zF}\ln c_{\mathrm{L}},
$$
and from the variation of $E_{1/2}$ with ligand concentration the coordination number $p$ and the cumulative stability constant $\beta_p$ can be determined. The table below gives the half-wave potentials of several ions in different media (V vs SCE; NR means not reduced in that medium):

| Ion | Noncoordinating medium | $1\,\mathrm{mol\,L^{-1}}$ $\ce{KCN}$ | $1\,\mathrm{mol\,L^{-1}}$ $\ce{KCl}$ | $1\,\mathrm{mol\,L^{-1}}$ $\ce{NH3}$ + $1\,\mathrm{mol\,L^{-1}}$ $\ce{NH4Cl}$ |
|---|---|---|---|---|
| $\ce{Cd^2+}$ | −0.59 | −1.18 | −0.64 | −0.81 |
| $\ce{Zn^2+}$ | −1.00 | NR | −1.00 | −1.35 |
| $\ce{Pb^2+}$ | −0.40 | −0.72 | −0.44 | −0.67 |
| $\ce{Ni^2+}$ | — | −1.36 | −1.20 | −1.10 |
| $\ce{Co^2+}$ | — | −1.45 | −1.20 | −1.29 |
| $\ce{Cu^2+}$ | +0.02 | NR | +0.04, −0.22 | −0.24, −0.51 |

$\ce{Cu^2+}$ is reduced in two steps in $\ce{Cl-}$ and $\ce{NH3}$ media (Cu(I) is stabilized by the ligand) and gives two waves. Choosing the medium can separate overlapping waves; in $\ce{NH3}$–$\ce{NH4Cl}$, for example, $\ce{Cd^2+}$ and $\ce{Zn^2+}$ differ by 0.54 V.

![Reversible polarographic waves of two metal ions (z = 2, E½ = −0.64 V and −1.00 V vs SCE, corresponding to Cd²⁺ and Zn²⁺ in 1 mol/L KCl) and the corresponding differential pulse voltammogram (pulse −50 mV); the horizontal axis follows the polarographic convention, with negative potential to the right](./plots/polarographic-waves.py)

### 6.6.2. Experimental Conditions in Polarography

Electrodes. Classical polarography uses two electrodes. The working electrode is the dropping mercury electrode, which has a small area and a high current density and is a polarized electrode; the reference electrode is a large-area saturated calomel electrode, which has a small current density and an almost constant potential (a depolarized electrode). The advantages of the dropping mercury electrode are a constantly renewed surface and good reproducibility, and a very high **overpotential** for hydrogen on mercury ([6.3.14](/6.3.14#sec-14.3.5)), which allows metal ions to be determined at quite negative potentials and low pH. Its drawbacks are that mercury is toxic and that mercury is oxidized above about +0.3 V (vs SCE), so it cannot be used in the positive potential region. Modern voltammetric instruments use the three-electrode system throughout, with a potentiostat controlling the potential of the working electrode relative to the reference electrode, and the current flows between the working electrode and the counter electrode.

Mass transport. A substance can reach the electrode surface by diffusion, electromigration, and convection ([6.3.12](/6.3.12#sec-12.2.1)). The theory of polarographic currents considers only diffusion, so the other two must be eliminated: a quiescent solution at constant temperature eliminates convection, and a large amount of supporting electrolyte eliminates electromigration.

**Definition 6.6.3 (Supporting Electrolyte)** An electrolyte added in voltammetric analysis at a concentration much higher than that of the electroactive substance (usually 50–100 times or more) and not itself reacting at the electrode within the potential range of the measurement ($\ce{KCl}$, $\ce{KNO3}$, buffer solutions, and so on) is called a **supporting electrolyte**.

Under an electric field all ions share the current according to their **transport numbers**. The ions of the supporting electrolyte are present at high concentration and carry almost all of the migration current, so the **electromigration** of the electroactive ion can be neglected and the current is determined by diffusion alone. The supporting electrolyte also lowers the solution resistance (reducing the $IR$ drop), fixes the ionic strength, and can serve as a complexing agent or buffer to adjust the half-wave potential.

Removal of oxygen and polarographic maxima. Dissolved oxygen is reduced at a mercury electrode in two steps, $\ce{O2 + 2H+ + 2e- -> H2O2}$ ($E_{1/2} \approx -0.05\,\mathrm{V}$ vs SCE) and $\ce{H2O2 + 2H+ + 2e- -> 2H2O}$ ($E_{1/2} \approx -0.9\,\mathrm{V}$). The two oxygen waves cover most of the commonly used potential range, so oxygen is removed before measurement by bubbling $\ce{N2}$ or Ar through the solution ($\ce{Na2SO3}$ may also be added in neutral or alkaline solution). Sharp peaks much higher than the limiting current sometimes appear on polarographic waves; these polarographic maxima arise from tangential flow of the solution caused by uneven surface tension on the mercury drop and are eliminated by adding a little surfactant (gelatin, Triton X-100).

### 6.6.3. Charging Current

**Definition 6.6.4 (Charging Current)** The current needed to charge the **electric double layer** at the electrode–solution interface (to change its charge) when the electrode potential changes or the electrode area varies is called the **charging current** (capacitive current). It does not involve an electrode reaction in which charge crosses the interface and is a non-faradaic current.

The electrode–solution interface behaves as a capacitor with a specific capacitance of about $10$–$40\,\mu\mathrm{F\,cm^{-2}}$. The area of a dropping mercury electrode grows continuously as the drop grows, so that it must be charged continuously even at constant potential; in classical polarography the charging current is about $10^{-7}\,\mathrm{A}$, equivalent to the diffusion current of about $10^{-5}\,\mathrm{mol\,L^{-1}}$ of analyte, and this is the origin of the detection limit of classical polarography.

Treat the working electrode and solution as a resistance $R$ (the solution resistance) in series with the double-layer capacitance $C$. After a potential step $\Delta E$, $\Delta E = IR + q/C$ and $I = \mathrm{d}q/\mathrm{d}t$, which gives

$$
I_{\mathrm{c}} = \frac{\Delta E}{R}\,\mathrm{e}^{-t/(RC)}. \tag{6.9}
$$
$RC$ is the time constant: at $t = RC$ the charging current has fallen to 36.8% of its initial value, and at $t = 5RC$ only 0.67% remains. With $R = 100\,\Omega$ and $C = 0.2\,\mu\mathrm{F}$, $RC = 20\,\mu\mathrm{s}$. The faradaic current, on the other hand, decays only as $t^{-1/2}$ according to the Cottrell equation, much more slowly. Waiting a few milliseconds after a potential step before sampling therefore eliminates the charging current with almost no loss of faradaic current; this is exactly the principle of pulse voltammetry (Section 6.6.5).

### 6.6.4. Linear-Sweep and Cyclic Voltammetry

Scanning the potential at a constant rate $v = \lvert\mathrm{d}E/\mathrm{d}t\rvert$ (usually $0.01$–$1\,\mathrm{V\,s^{-1}}$) in a quiescent solution is called linear-sweep voltammetry. Unlike the slow scan of polarography, the current is not a plateau but a peak: after the potential passes $E^{\circ\prime}$ the surface concentration quickly falls to zero, and the current then decreases because of the expansion of the diffusion layer with time (for the same reason as in the Cottrell equation). Fast scanning during the late growth of a dropping mercury electrode (when the area is almost constant) is the historical single-sweep oscillographic polarography, with a sensitivity about two orders of magnitude higher than classical polarography.

**Definition 6.6.5 (Randles–Ševčík Equation)** In the linear-sweep voltammogram of a reversible couple at a planar electrode, the peak current is

$$
I_{\mathrm{p}} = 0.4463\,zFAc^*\sqrt{\frac{zFvD}{RT}}, \tag{6.10}
$$
called the **Randles–Ševčík equation**. At $25\,^\circ\mathrm{C}$, $I_{\mathrm{p}} = (2.69\times10^5)\,z^{3/2}AD^{1/2}v^{1/2}c^*$, with $I_{\mathrm{p}}$ in A, $A$ in $\mathrm{cm^2}$, $D$ in $\mathrm{cm^2\,s^{-1}}$, $v$ in $\mathrm{V\,s^{-1}}$, and $c^*$ in $\mathrm{mol\,cm^{-3}}$.

The peak current is proportional to the concentration and to the square root of the scan rate; the peak potential $E_{\mathrm{p}} = E_{1/2} - 1.109\frac{RT}{zF}$ (for a reduction peak, that is, $28.5/z\,\mathrm{mV}$ more negative than $E_{1/2}$) is independent of scan rate. The coefficient 0.4463 comes from the numerical solution of the diffusion equation ([2.5.7](/2.5.7)) with a linearly changing Nernst boundary condition.

**Definition 6.6.6 (Cyclic Voltammetry)** The method in which the potential of the working electrode is scanned with a triangular waveform (linearly from the initial potential to the switching potential and then back at the same rate) and the complete current–potential curve (the cyclic voltammogram) is recorded is called **cyclic voltammetry**.

During the forward scan (toward negative potential, say), O is reduced and a cathodic peak appears; after reversal, the R accumulated near the electrode is reoxidized and an anodic peak appears. The criteria for a reversible couple ($25\,^\circ\mathrm{C}$) are:

1. The difference between the two peak potentials $\Delta E_{\mathrm{p}} = E_{\mathrm{pa}} - E_{\mathrm{pc}} \approx 2.2\frac{RT}{zF} = 57$–$59\,\mathrm{mV}/z$ (depending on the switching potential, often written $59/z\,\mathrm{mV}$) is independent of scan rate.
2. The ratio of peak currents is $I_{\mathrm{pa}}/I_{\mathrm{pc}} = 1$.
3. $I_{\mathrm{p}}$ is proportional to $v^{1/2}$.
4. The formal potential is $E^{\circ\prime} \approx (E_{\mathrm{pa}} + E_{\mathrm{pc}})/2$.

When electron transfer is slow (quasi-reversible), $\Delta E_{\mathrm{p}}$ increases with scan rate, from which the standard rate constant can be determined; for a completely irreversible process the reverse peak disappears and the peak potential shifts with scan rate. If the product R undergoes a subsequent chemical reaction in solution (an EC mechanism), the reverse peak becomes smaller, and the more so the slower the scan, from which the rate of the subsequent reaction can be determined.

![Cyclic voltammogram of a reversible one-electron couple O + e⁻ ⇌ R: numerical solution of semi-infinite linear diffusion at a planar electrode by explicit finite differences (c* = 1 mmol/L, D = 1.0×10⁻⁵ cm² s⁻¹, 25 °C, IUPAC sign convention: cathodic current is negative). Left: voltammograms at three scan rates, with a peak separation of about 59 mV independent of scan rate; right: cathodic peak current proportional to v^(1/2), in agreement with the Randles–Ševčík equation](./plots/cyclic-voltammogram.py)

The numerical solution in the figure uses only the explicit finite-difference scheme for the diffusion equation (at each step the surface concentrations are set by the Nernst equation and the current is found from the concentration gradient at the surface), and a few tens of lines of Python give results that agree with the Randles–Ševčík equation to within 1%. The same method can simulate quasi-reversible systems and coupled chemical reactions (replacing the Nernst boundary by the **Butler–Volmer equation**, [6.3.14](/6.3.14#sec-14.3.2)). Cyclic voltammetry is the most commonly used diagnostic tool for studying electrode processes and is often called "the spectroscopy of electrochemistry": it gives the formal potential of a couple, the number of electrons, the reversibility of the reaction, and information on coupled reactions. It is used, for example, to measure the potentials of biological redox molecules such as cytochrome c, flavins, and quinone coenzymes, and in nonaqueous solvents the $\ce{Fc+}/\ce{Fc}$ couple of ferrocene ($\ce{Fe(C5H5)2}$) serves as an internal reference (recommended by IUPAC). As a quantitative method, cyclic voltammetry is not very sensitive (about $10^{-5}\,\mathrm{mol\,L^{-1}}$, limited by the charging current).

### 6.6.5. Pulse Voltammetry

Pulse voltammetry waits for the charging current to decay after a potential step before sampling the current (Section 6.6.3), and measures a differential current to subtract the background.

**Definition 6.6.7 (Differential Pulse Voltammetry)** The method in which potential pulses of constant amplitude (usually 10–100 mV) and a duration of a few tens of milliseconds are superimposed periodically on a slowly linearly (or stepwise) changing base potential, the current is sampled once just before each pulse is applied and once just before it ends, and the difference of the two currents $\Delta I$ is plotted against the base potential is called **differential pulse voltammetry**.

$\Delta I$ corresponds to the derivative of the polarographic wave, the voltammogram is a peak, the peak potential is $E_{\mathrm{p}} = E_{1/2} - \Delta E/2$ ($\Delta E$ is the signed pulse amplitude), and the peak height is proportional to the concentration. Both samples are taken after the charging current has decayed, and the subtraction also removes the slowly varying part of the residual current, so that the detection limit can reach $10^{-7}$–$10^{-8}\,\mathrm{mol\,L^{-1}}$; a peak-shaped wave also resolves neighboring components more readily than a step-shaped one (peak potentials about 50 mV apart suffice).

**Definition 6.6.8 (Square-Wave Voltammetry)** The method in which a symmetric square wave (one period per step) is superimposed on a staircase potential, the current is sampled at the end of each half-period, and the difference between the forward and reverse currents (the net current) is plotted against the potential is called **square-wave voltammetry**.

The peak in square-wave voltammetry resembles that of differential pulse voltammetry, but the reverse pulse reconverts the product formed in the forward pulse, so that the net current for a reversible system is almost doubled. The square-wave frequency is tens to hundreds of hertz, and one scan takes only a few seconds, much faster than differential pulse voltammetry, with a detection limit of about $10^{-8}\,\mathrm{mol\,L^{-1}}$. Its forerunner was Barker's square-wave polarography (a square wave of about 250 Hz and 10–30 mV superimposed on a dc scan potential, with the ac current measured before each reversal): for the charging current to decay within a half-period the loop resistance $R$ must be very small (< 100 Ω), and a supporting electrolyte of more than $1\,\mathrm{mol\,L^{-1}}$ must be added to the solution, which places high demands on the purity of reagents in trace analysis.

### 6.6.6. Stripping Voltammetry

**Definition 6.6.9 (Stripping Voltammetry)** The method in which the potential of the working electrode is first controlled under stirring so that the analyte is electrolytically preconcentrated on an electrode of small volume (preelectrolysis), and after a rest period the potential is scanned in the reverse direction so that the preconcentrated substance is redissolved, with the potential of the stripping peak used for qualitative analysis and the peak current (or peak area) for quantitative analysis, is called **stripping voltammetry**. When the analyte is reduced during preconcentration and oxidized during stripping, the method is called anodic stripping voltammetry.

Anodic stripping voltammetry is used for elements such as Pb, Cd, Cu, Zn, Tl, and In that form amalgams or deposit as metals. For example, after preelectrolysis for a few minutes at $-1.0\,\mathrm{V}$ (vs SCE), $\ce{Pb^2+}$ and $\ce{Cd^2+}$ are reduced and dissolve in a mercury film, and a positive-going scan (often in the differential pulse or square-wave mode) oxidizes them in turn, giving sharp stripping peaks. Cathodic stripping voltammetry is the reverse: at positive potential, halide ions, sulfide, and other anions form sparingly soluble salts with the electrode material (Hg, Ag) and deposit, and a negative-going scan reduces and strips them; adsorptive stripping voltammetry uses the adsorptive preconcentration of the analyte (or its complex) at the electrode surface.

Preconcentration is a controlled-potential electrolysis, and by Eq. (6.6) the fraction deposited in the preconcentration time $t$ is $x = 1 - \exp\left(-\frac{DAt}{V\delta}\right)$. Stripping voltammetry does not require complete preconcentration (usually only a few percent is deposited); as long as the preconcentration time, the stirring rate, and the electrode area are strictly reproducible, quantitation by standard solutions or standard addition is possible. Because the analyte is preconcentrated from tens of milliliters of solution into a mercury film of about $10^{-4}\,\mathrm{mL}$, its concentration is raised thousands of times and the stripping current is concentrated in a very short time, so that the detection limit can reach the order of $10^{-9}$–$10^{-11}\,\mathrm{mol\,L^{-1}}$ with a very cheap instrument, and several elements can be determined simultaneously. Because of the toxicity of mercury, mercury-film electrodes are being replaced by bismuth-film electrodes, which, like mercury, form "fused alloys" with heavy metals and also have a high overpotential for hydrogen evolution. Disposable screen-printed electrodes and portable stripping voltammetric instruments are used for on-site determination of lead in blood and heavy metals in water.

### 6.6.7. Solid Electrodes and Microelectrodes

Except for some special uses, the dropping mercury electrode has been replaced by solid electrodes: glassy carbon (wide potential window, inert, easy to polish), Pt and Au electrodes (positive potential region, can be modified), boron-doped diamond electrodes (very wide window, low background current), carbon fiber and carbon paste electrodes, and chemically modified electrodes whose surfaces carry catalysts, enzymes, or recognition molecules. Compared with mercury, solid electrodes must have their surfaces renewed by polishing or electrochemical cleaning, and their overpotential for hydrogen is lower than that of mercury, so they are inferior to mercury in the negative potential region, but they are far better in the positive region and in stability, environmental safety, and miniaturization.

Ultramicroelectrodes (microelectrodes) with dimensions smaller than about $25\,\mu\mathrm{m}$ have special advantages: spherical diffusion brings the current quickly to a steady state (the steady-state limiting current of a disk microelectrode is $I = 4zFDc^*r$, with $r$ the radius), the current is so small that the $IR$ drop is negligible, and the double-layer capacitance is small so that the $RC$ time constant is short, which allows work in highly resistive solutions at scan rates of hundreds of volts per second. A carbon fiber microelectrode about $7\,\mu\mathrm{m}$ in diameter is inserted into brain tissue, and fast-scan cyclic voltammetry at 400 V per second is used to measure the subsecond release of neurotransmitters such as dopamine; this is the standard method of neurochemistry.

## 6.7. Electrochemical Sensors and Imaging

### 6.7.1. Amperometric Sensors and Glucose Sensors

**Definition 6.7.1 (Amperometric Sensor)** A sensor that measures, at a constant working potential, the current for oxidation or reduction at an electrode of the analyte (or of a reactant or product related to it), the current being proportional to concentration over a certain range, is called an **amperometric sensor**.

An amperometric sensor measures the diffusion-limited current (the **limiting diffusion current**) and has high sensitivity and a wide linear range; to ensure that the current is determined by diffusion alone, the electrode surface is often covered with a dialysis membrane or diffusion-limiting membrane. Its prototype is the Clark oxygen electrode (1956): a Pt cathode and an $\ce{Ag}/\ce{AgCl}$ anode are immersed in $\ce{KCl}$ solution and separated from the sample by a gas-permeable polymer membrane; $\ce{O2}$ is reduced on Pt at about −0.6 V, and the current is proportional to the partial pressure of oxygen. It is still used for blood gas analysis and the determination of dissolved oxygen.

The glucose sensor is the most successful amperometric sensor. In 1962 Clark and Lyons immobilized glucose oxidase on an oxygen electrode and proposed the "enzyme electrode". According to the way electrons pass from the enzyme to the electrode, there are three generations:

1. First generation: $\ce{O2}$ is the natural electron acceptor, glucose $+\ \ce{O2 ->[GOx]}$ gluconolactone $+\ \ce{H2O2}$, and either the consumption of $\ce{O2}$ is detected (oxygen electrode) or the $\ce{H2O2}$ formed is oxidized on a Pt electrode at about +0.6 V (vs $\ce{Ag}/\ce{AgCl}$): $\ce{H2O2 -> O2 + 2H+ + 2e-}$. The drawback is that a fairly high working potential is needed, at which ascorbic acid, uric acid, acetaminophen, and others are also oxidized and interfere; the result is also affected by the oxygen concentration of the blood.
2. Second generation: an artificial redox mediator (ferrocene derivatives, ferricyanide, osmium complexes) replaces $\ce{O2}$ and transfers electrons between the reduced FAD of the enzyme and the electrode: $\ce{GOx(FADH2) + 2M_{ox} -> GOx(FAD) + 2M_{red} + 2H+}$, and $\ce{M_{red}}$ is reoxidized at the electrode at a lower potential. The working potential is low, interference is small, and the method does not depend on $\ce{O2}$. The first commercial personal blood glucose meter (1987) used a ferrocene mediator.
3. Third generation: direct electron transfer between the active site of the enzyme and the electrode, without a mediator. The FAD of GOx is buried deep inside the protein and direct electron transfer is hard to achieve, so this generation mostly uses nanomaterial-modified electrodes or other enzymes (such as some dehydrogenases) and is still developing.

A household blood glucose test strip is a disposable second-generation sensor: GOx (or FAD-dependent glucose dehydrogenase, which is unaffected by $\ce{O2}$) and a mediator are immobilized on a screen-printed carbon electrode, and after about $1\,\mu\mathrm{L}$ of blood is applied, a voltage of about 0.3 V is applied between the two electrodes; after a few seconds the measured current (or the charge obtained by integration) is proportional to the glucose concentration. The normal range of fasting blood glucose is about $3.9$–$6.1\,\mathrm{mmol\,L^{-1}}$. Continuous glucose monitors implanted under the skin use the same principle to measure glucose in interstitial fluid every few minutes.

### 6.7.2. Biosensors

**Definition 6.7.2 (Biosensor)** An analytical device that combines a biological recognition element (an enzyme, antibody, nucleic acid, aptamer, receptor, cell, or tissue) closely with a physicochemical transducer and converts the biological recognition process into a measurable electrical, optical, mass, or thermal signal is called a **biosensor**.

Biosensors are classified by recognition element into enzyme sensors, immunosensors, nucleic acid sensors, cell and tissue sensors, and so on, and by transducer into electrochemical (potentiometric, amperometric, conductometric, impedimetric), optical (fluorescence, surface plasmon resonance, see [6.4.9](/6.4.9#sec-9.6.2)), piezoelectric mass-sensitive, and thermal types. The recognition element provides selectivity and the transducer provides sensitivity, and the way the two are joined (immobilization) determines the lifetime and reproducibility of the sensor. The **enzyme electrodes** of Section 6.3.4 and the glucose sensors of Section 6.7.1 are enzyme sensors. Immunosensors exploit antigen–antibody binding and often amplify the signal with enzyme labels (electrochemical enzyme-linked immunoassay). In a DNA sensor a single-stranded probe is immobilized on the electrode, and after hybridization with the target sequence the distance of a redox molecule labeled on the probe (such as methylene blue) from the electrode, or its electron-transfer rate, changes and the voltammetric peak current changes with it. They are the main part of point-of-care testing devices and will be used again in [6.6](/6.6) Chemical Biology.

### 6.7.3. Scanning Electrochemical Microscopy

**Definition 6.7.3 (Scanning Electrochemical Microscopy)** An instrument in which an ultramicroelectrode is used as a probe, scanned over a substrate surface (at a distance of the order of the probe radius) in a solution containing a redox mediator, and the faradaic current at the probe is measured as a function of position, giving an image of the topography and local electrochemical activity of the substrate, is called a **scanning electrochemical microscope** (SECM).

The SECM was introduced by Bard in 1989 and consists of a three-electrode system (the probe being the working electrode), a piezoelectric positioner, and a bipotentiostat. The most basic mode is the feedback mode. The mediator O is reduced diffusion-controlled at the probe, and far from the substrate the probe current has the steady-state value $I_{\mathrm{T},\infty} = 4zFDc^*a$ ($a$ being the probe radius). Near an insulating substrate, the substrate blocks the diffusion of O to the probe and the current decreases (negative feedback); near a conducting or redox-active substrate, R is reoxidized to O at the substrate, replenishing O near the probe, and the current increases (positive feedback). The variation of current with probe–substrate distance $d$ (the approach curve) is most pronounced within $d \approx a$, so the resolution is determined by the size of the probe: micrometer probes give micrometer images and nanoelectrodes can reach tens of nanometers.

The SECM has been used for single-cell studies: with the redox activity or respiration of the cell as the signal, the topography and transmembrane electron-transfer rate of single HeLa and PC12 cells have been measured, and scanning of a plant leaf under illumination has shown that single stomata in green leaf regions release $\ce{O2}$ at a much higher rate than white regions (without chloroplasts). Its advantages are that it has little effect on the activity and morphology of cells, can measure in real time on living cells, and is selective because it responds only to electroactive substances; the problems are that the closer the probe is to the cell, the clearer the image but also the greater the disturbance to the cell, that densely packed cells are hard to resolve, and that topography and activity signals are mixed (it is now often combined with atomic force microscopy or ion conductance microscopy, so that the distance is controlled first and the activity measured afterward).

### 6.7.4. Nanopore Sequencing

**Definition 6.7.4 (Nanopore Sequencing)** The method in which only a single nanometer-scale pore is left in an insulating membrane separating two electrolyte reservoirs, a voltage across the membrane drives an ionic current through the nanopore, and a single strand of DNA (or RNA) is driven by the electric field through the pore base by base, the sequence being read from the different degrees to which different combinations of bases in the pore block the ionic current, is called **nanopore sequencing**.

A typical nanopore is a protein pore (α-hemolysin, MspA, CsgG, and others) embedded in a lipid or polymer membrane, with a narrowest diameter of about 1–2 nm that admits only single-stranded nucleic acid. The two sides of the membrane contain $\ce{KCl}$ solution, each with an $\ce{Ag}/\ce{AgCl}$ electrode, and at a voltage of 100–200 mV the ionic current of an open pore is about 100 pA. The negatively charged nucleic acid strand migrates toward the positive electrode in the field (**electrophoresis**, [6.3.21](/6.3.21)) and enters the pore, whereupon the current decreases by an amount that depends on the few bases (the k-mer) located at the narrowest part of the pore at that moment. Free translocation of nucleic acid is too fast (about 1 μs per base), so in practical sequencing a motor protein such as a helicase controls the translocation speed to a few hundred bases per second, and the current signal is decoded into a base sequence by a neural network model (base calling). Nanopore sequencing gives read lengths of tens of thousands to more than a million bases, the instrument can be as small as the palm of a hand, RNA and base modifications (such as 5-methylcytosine) can be read directly, and it has been commercially available since 2014. In terms of measurement principle it is a conductance measurement: the conductance of the nanopore varies with the molecule in the pore. From the electrochemical viewpoint, like the patch clamp it measures picoampere currents through a single ion channel. Other methods of nucleic acid sequencing are described in [6.4.14](/6.4.14#sec-14.5.4) and [6.6](/6.6).

## Summary

| Method | Measurement | Quantitative relation | Typical detection limit (mol/L) | Main applications |
|---|---|---|---|---|
| Conductometry | Conductance | $\sigma = \sum\lambda_{\mathrm{B}}c_{\mathrm{B}}$ | — | Water quality, conductometric titration, ion chromatography detection |
| Direct potentiometry | Zero-current emf | $E = K \pm S\lg a$ | about $10^{-6}$ | pH, ion-selective electrodes, clinical electrolytes |
| Potentiometric titration | $E$–$V$ curve | End point from the jump | Same as titration | Titration of colored, turbid, and nonaqueous solutions |
| Electrogravimetry | Mass deposited | Weighing | Major components | Alloy analysis |
| Coulometry and coulometric titration | Charge | $m = QM/(zF)$ | Microgram level | Value assignment of primary standards, trace water (Karl Fischer) |
| Polarography and linear-sweep voltammetry | $I$–$E$ curve | $I_{\mathrm{d}}$ or $I_{\mathrm{p}} \propto c$ | $10^{-5}$ | Study of electrode processes |
| Pulse voltammetry | Differential current | $\Delta I_{\mathrm{p}} \propto c$ | $10^{-7}$–$10^{-8}$ | Trace analysis |
| Stripping voltammetry | Stripping peak | $I_{\mathrm{p}} \propto c$ (fixed preconcentration conditions) | $10^{-9}$–$10^{-11}$ | Trace heavy metals |
| Amperometric sensors | Current at constant potential | $I \propto c$ | System dependent | Blood glucose, dissolved oxygen |

- Potentiometry measures activities; TISAB or a constant ionic background controls the activity coefficients, and standard addition or the Gran plot handles complex matrices. Potentiometric titration measures only relative changes and is more accurate than direct potentiometry.
- The selectivity of ion-selective electrodes is described by the Nikolsky–Eisenman equation; the alkaline error of the glass electrode is its response to $\ce{Na+}$.
- Coulometry is an absolute method that needs no standard substance, provided the current efficiency is 100%; coulometric titration ensures this by means of an auxiliary electrolyte and an electrogenerated titrant.
- The sensitivity of voltammetry is determined by the ratio of faradaic to charging current, and pulse techniques, stripping preconcentration, and microelectrodes all aim to raise this ratio.
- Bioelectroanalysis: enzyme electrodes and blood glucose meters, clinical electrolyte analysis, patch clamp, SECM single-cell imaging, and nanopore sequencing.

## Questions

1. Why are alternating current and platinized electrodes used to measure the conductance of a solution?

   **Answer** Direct current causes electrolysis at the electrodes, and the products and polarization change the resistance; with high-frequency alternating current the electrolysis in each half-cycle is negligible, and platinum black increases the true surface area and reduces the interfacial impedance.
2. Why must a glass electrode be soaked before use, and is the pH reading too low or too high when a strongly basic, high-sodium solution is measured?

   **Answer** Soaking forms a hydrated gel layer at the membrane surface in which $\ce{H+}$ is the exchanging ion, which is needed for a Nernstian response; in strongly basic solution with high sodium, $\ce{Na+}$ takes part in the exchange, the apparent $\ce{H+}$ activity is too high, and the reading is too low (alkaline error).
3. When a fluoride electrode is used to analyze a water sample containing $\ce{Al^3+}$, is the result too high or too low if citrate is not added?

   **Answer** Too low. $\ce{Al^3+}$ forms stable complexes with $\ce{F-}$, and the electrode responds only to free $\ce{F-}$; citrate masks $\ce{Al^3+}$ and releases the $\ce{F-}$.
4. Why must a large amount of auxiliary electrolyte be added in coulometric titration? Explain with the determination of $\ce{Fe^2+}$ by means of $\ce{Ce^3+}$.

   **Answer** At constant current the electrode potential would shift to the potential of a side reaction once the analyte is depleted; a large amount of $\ce{Ce^3+}$ carries the current and clamps the potential at $\ce{Ce^4+}/\ce{Ce^3+}$, and the $\ce{Ce^4+}$ formed oxidizes $\ce{Fe^2+}$ quantitatively, so the current efficiency remains 100%.
5. Why are a supporting electrolyte added, oxygen removed, and the solution kept quiescent in polarographic analysis?

   **Answer** To eliminate the migration current, the oxygen waves, and the convection current, respectively, so that the current is determined by diffusion alone, in agreement with the Ilkovič equation.
6. What does it show when $\Delta E_{\mathrm{p}}$ in a cyclic voltammogram increases with scan rate?

   **Answer** Electron transfer is not fast enough (quasi-reversible), and the faster the scan, the further the electrode surface departs from Nernst equilibrium; for a reversible system $\Delta E_{\mathrm{p}}$ is about $59/z\,\mathrm{mV}$ independent of scan rate.
7. What is the main difference between first- and second-generation glucose sensors, and why is the second generation more resistant to interference?

   **Answer** The first generation uses $\ce{O2}$ as the electron acceptor and detects $\ce{H2O2}$, which needs a high potential of about +0.6 V; the second generation transfers electrons by a mediator and works at a low potential, at which ascorbic acid and other species are not oxidized, and it is also independent of the oxygen concentration.
