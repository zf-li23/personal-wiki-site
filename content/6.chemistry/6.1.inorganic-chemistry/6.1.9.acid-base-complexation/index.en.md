---
title: Acid–Base and Complexation Equilibria
source_hash: aa58d0c168cb
---

Most inorganic reactions take place in aqueous solution, where acids, bases, and salts dissociate into ions and the reactions between ions give rise to the four main types of equilibrium in solution: acid–base equilibria and complexation equilibria (this chapter), precipitation–dissolution equilibria ([6.1.10](/6.1.10)), and redox equilibria ([6.1.11](/6.1.11)). All of them are specific forms of the **chemical equilibrium** of [6.1.8](/6.1.8) in solution: the equilibrium constants are all **standard equilibrium constants**, the direction of reaction is always decided by comparing the **reaction quotient** with the equilibrium constant, and every equilibrium constant can be linked to thermodynamic data through $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = -RT\ln K^\circ$. We first compare the three theories of acids and bases (9.1), then treat the equilibrium calculations for water and pH (9.2), weak acids and bases (9.3), salt solutions (9.4), and buffer solutions (9.5). Acid–base titration is introduced briefly (9.6), and the chapter ends with the dissociation equilibria of complexes in solution (9.7). The common method of calculation is to write down all the equilibria, identify the dominant one, make a reasonable approximation, and finally check that the approximation holds; if it does not, we write the equations of charge balance and mass balance and solve them numerically. A systematic treatment of the proton condition and distribution fractions, titration curves and end-point errors, and EDTA and conditional stability constants are found in [Analytical Chemistry](/6.4); activity coefficients and ionic strength are found in [Physical Chemistry](/6.3).

Throughout this chapter, $[\mathrm{B}]$ in an equilibrium-constant expression denotes the equilibrium concentration of species B divided by $c^\circ = 1\,\mathrm{mol\,L^{-1}}$ (numerically equal to the concentration in $\mathrm{mol\,L^{-1}}$), so $K_{\mathrm{a}}$, $K_{\mathrm{b}}$, $K_{\mathrm{w}}$, $\beta_n$, and so on are dimensionless standard equilibrium constants. Strictly speaking, the concentrations should be replaced by **activities** ([6.1.8](/6.1.8)); here we treat solutions as ideal and dilute. Unless stated otherwise, all data refer to $25\,^\circ\mathrm{C}$ ($298.15\,\mathrm{K}$), and the acid–base constants are taken from the CRC Handbook of Chemistry and Physics.

## 9.1. Theories of Acids and Bases

Why do acids as a class, and bases as a class, share common properties? Early on, the common character of acids was attributed to oxygen (Lavoisier); in the early nineteenth century it was attributed to hydrogen instead. The ionization theory of the late nineteenth century gave the first quantitative modern theory of acids and bases, and the proton theory and the electron theory followed. The scope of the three theories widens in that order.

### 9.1.1. The Arrhenius Theory

**Definition 9.1.1 (Arrhenius Theory of Acids and Bases)** According to the **Arrhenius theory of acids and bases** (Arrhenius, 1884), a substance is an acid if the only cation it releases in aqueous solution is $\ce{H+}$, and a base if the only anion it releases is $\ce{OH-}$; the essence of neutralization is $\ce{H+ + OH- -> H2O}$.

Examples are $\ce{H2SO4 -> H+ + HSO4-}$ and $\ce{NaOH -> Na+ + OH-}$. The strength of an acid or base is measured by its extent of ionization.

**Definition 9.1.2** At ionization equilibrium, the percentage of the original molecules of a weak electrolyte that have ionized is called the **degree of dissociation**, denoted $\alpha$.

The Arrhenius theory was the first to explain the properties of acids and bases from the composition of substances, and it allows the strengths of acids and bases to be compared quantitatively through the degree of dissociation and the equilibrium constant; Arrhenius received the 1903 Nobel Prize in Chemistry for this work. Its limitation is that it confines acids and bases to aqueous solution and restricts bases to hydroxides. An aqueous solution of $\ce{NH3}$ is basic, yet it contains no $\ce{NH4OH}$ molecules, and the direct reaction of gaseous $\ce{HCl}$ with $\ce{NH3}$ to give $\ce{NH4Cl}$ cannot be classified as an acid–base reaction. (Chinese textbooks often write aqueous ammonia as $\ce{NH3*H2O}$; the solution actually contains hydrated $\ce{NH3}$ molecules, which this wiki writes as $\ce{NH3(aq)}$.)

### 9.1.2. The Brønsted–Lowry Theory

**Definition 9.1.3 (Brønsted–Lowry Theory)** According to the **Brønsted–Lowry theory** of acids and bases (Brønsted and Lowry, 1923), any molecule or ion that can donate a proton ($\ce{H+}$) is an acid (proton donor), and any molecule or ion that can accept a proton is a base (proton acceptor).

An acid becomes a base after donating a proton, and a base becomes an acid after accepting one, so the two are unified through their relation to the proton:

$$
\text{acid} \ce{<=>} \text{base} + \ce{H+}: \qquad \ce{HAc <=> Ac- + H+}, \quad \ce{NH4+ <=> NH3 + H+}, \quad \ce{H2PO4- <=> HPO4^2- + H+}.
$$

**Definition 9.1.4 (Conjugate Acid–Base Pair)** An acid and a base that differ by exactly one proton and are interconverted by donating or accepting it form a **conjugate acid–base pair**; the acid is called the conjugate acid of the base, and the base the conjugate base of the acid.

**Definition 9.1.5 (Amphiprotic Substance)** A substance that can donate a proton under some conditions and accept one under others is called an **amphiprotic substance**, for example $\ce{H2O}$, $\ce{HCO3-}$, $\ce{H2PO4-}$, and $\ce{HS-}$.

In the Brønsted–Lowry theory, acids and bases may be molecules, cations, or anions. There is no concept of a "salt": the constituent ions of a salt are separately ionic acids or ionic bases, as in $\ce{NH4Cl}$, where $\ce{NH4+}$ is an ionic acid and $\ce{Cl-}$ is an (extremely weak) ionic base.

The half-reaction "acid ⇌ base + H⁺" cannot occur by itself, because free protons do not exist in solution. A real acid–base reaction is a proton transfer between two conjugate acid–base pairs:

$$
\text{acid}_1 + \text{base}_2 \ce{<=>} \text{base}_1 + \text{acid}_2.
$$

The various reactions of the Arrhenius theory are all unified as proton transfers:

| Arrhenius description | Proton-transfer reaction | Acid$_1$ / base$_1$ | Base$_2$ / acid$_2$ |
|---|---|---|---|
| Ionization of an acid | $\ce{HAc + H2O <=> H3O+ + Ac-}$ | $\ce{HAc}$ / $\ce{Ac-}$ | $\ce{H2O}$ / $\ce{H3O+}$ |
| Ionization of a base | $\ce{H2O + NH3 <=> NH4+ + OH-}$ | $\ce{H2O}$ / $\ce{OH-}$ | $\ce{NH3}$ / $\ce{NH4+}$ |
| Neutralization | $\ce{H3O+ + OH- <=> H2O + H2O}$ | $\ce{H3O+}$ / $\ce{H2O}$ | $\ce{OH-}$ / $\ce{H2O}$ |
| Neutralization | $\ce{HAc + OH- <=> H2O + Ac-}$ | $\ce{HAc}$ / $\ce{Ac-}$ | $\ce{OH-}$ / $\ce{H2O}$ |
| Hydrolysis of a salt | $\ce{Ac- + H2O <=> HAc + OH-}$ | $\ce{H2O}$ / $\ce{OH-}$ | $\ce{Ac-}$ / $\ce{HAc}$ |
| Hydrolysis of a salt | $\ce{NH4+ + H2O <=> NH3 + H3O+}$ | $\ce{NH4+}$ / $\ce{NH3}$ | $\ce{H2O}$ / $\ce{H3O+}$ |
| Hydrolysis of a hydrated ion | $\ce{[Cu(H2O)4]^2+ + H2O <=> [Cu(OH)(H2O)3]+ + H3O+}$ | $\ce{[Cu(H2O)4]^2+}$ / $\ce{[Cu(OH)(H2O)3]+}$ | $\ce{H2O}$ / $\ce{H3O+}$ |
| Gas-phase reaction | $\ce{HCl(g) + NH3(g) -> NH4Cl(s)}$ | $\ce{HCl}$ / $\ce{Cl-}$ | $\ce{NH3}$ / $\ce{NH4+}$ |

Water acts here as both an acid and a base and is the most important amphiprotic substance. For brevity, we often write $\ce{H3O+}$ as $\ce{H+}$ below.

Next we discuss how the strength of acids and bases depends on the solvent. The stronger an acid, the weaker its conjugate base, and the stronger a base, the weaker its conjugate acid (Section 9.3.1 gives the quantitative relation $K_{\mathrm{a}}K_{\mathrm{b}} = K_{\mathrm{w}}$):

$$
\text{acidity: }\ce{HClO4} > \ce{H2SO4} > \ce{H3PO4} > \ce{HAc} > \ce{H2CO3} > \ce{NH4+} > \ce{H2O}; \qquad \text{basicity: }\ce{ClO4-} < \ce{HSO4-} < \ce{H2PO4-} < \ce{Ac-} < \ce{HCO3-} < \ce{NH3} < \ce{OH-}.
$$

A proton-transfer reaction always proceeds from the stronger acid and stronger base toward the weaker acid and weaker base. The strength of an acid or base depends first on the intrinsic ability of the substance to donate or accept protons, and second on the ability of the solvent to accept or donate protons: the more basic the solvent, the stronger a given acid appears.

**Definition 9.1.6** The action of a solvent that converts acids (or bases) of different strengths completely into the solvated proton $\ce{H3O+}$ (or the conjugate base of the solvent), so that they all appear equally strong, is called the **leveling effect**; the action that distinguishes the relative strengths of acids (or bases) is called the **differentiating effect**.

$\ce{HClO4}$, $\ce{HCl}$, $\ce{HNO3}$, and $\ce{H2SO4}$ (first step) are all converted completely to $\ce{H3O+}$ in water: the strongest acid that can exist in water is $\ce{H3O+}$, and water is a leveling solvent for these strong acids. In glacial acetic acid, which is less basic than water, they dissociate only partially and the order of strength $\ce{HClO4} > \ce{H2SO4} > \ce{HCl} > \ce{HNO3}$ can be resolved, so glacial acetic acid is a differentiating solvent for them. Conversely, in strongly basic liquid ammonia, $\ce{HCl}$ and $\ce{HAc}$ are both converted completely to $\ce{NH4+}$ and are both strong acids; in water, $\ce{HCl}$ is a strong acid while $\ce{HAc}$ is weak, so water is a differentiating solvent for these two acids. For most weak acids, water is an excellent differentiating solvent.

The Brønsted–Lowry theory widens the range of acids and bases (to nonaqueous systems and gas-phase reactions), shows that the essence of acid–base reactions is proton transfer, retains the constants that measure acid and base strength quantitatively in the Arrhenius theory, and explains the solvent dependence of the strength of strong acids. Its limitation is that reactions between substances without hydrogen (such as $\ce{BF3 + F- -> BF4-}$ and $\ce{CaO + SO3 -> CaSO4}$) cannot be classified as acid–base reactions.

### 9.1.3. The Lewis Theory

**Definition 9.1.7 (Lewis Acids and Bases)** Lewis (1923) proposed that any molecule, ion, or atom that can accept an electron pair is a **Lewis acid** (electron-pair acceptor), such as $\ce{H+}$, $\ce{Fe^3+}$, $\ce{Ag+}$, and $\ce{BF3}$; and any molecule or ion that can donate an electron pair is a **Lewis base** (electron-pair donor), such as $\ce{NH3}$, $\ce{H2O}$, $\ce{CO}$, $\ce{F-}$, and $\ce{OH-}$.

The essence of a Lewis acid–base reaction is the formation of a **coordinate bond** ([6.1.3](/6.1.3)), and the product is called an acid–base adduct. A **coordination compound** ([6.1.5](/6.1.5)) is a typical acid–base adduct: in $\ce{Cu^2+ + 4NH3 -> [Cu(NH3)4]^2+}$, $\ce{Cu^2+}$ is the acid and $\ce{NH3}$ is the base. All bases of the Brønsted–Lowry theory are Lewis bases (they accept protons with a **lone pair**), and $\ce{H+}$ is a Lewis acid, so the Brønsted–Lowry theory is a special case of the Lewis theory. Whether a substance is an acid or a base must be decided in the context of a specific reaction: $\ce{H2O}$ is a base when it combines with $\ce{H+}$, but when it interacts with $\ce{NH3}$ it provides $\ce{H+}$ and so acts as an acid.

**Example 9.1.1** Identify the Lewis acid and base in each of the following reactions: (1) $\ce{BrF3 + F- -> [BrF4]-}$; (2) $\ce{(CH3)2CO + I2 -> (CH3)2CO*I2}$; (3) $\ce{KH + H2O -> KOH + H2}$.

**Solution** (1) $\ce{BrF3}$ is the acid and $\ce{F-}$ is the base. (2) Acetone is the base and $\ce{I2}$ is the acid: a lone pair on the carbonyl O of acetone enters the empty σ* antibonding orbital of $\ce{I2}$ to form a charge-transfer complex (this is why $\ce{I2}$ is brown in acetone but violet in $\ce{CCl4}$). (3) The ionic hydride supplies the base $\ce{H-}$, which combines with the acid $\ce{H+}$ of water to give $\ce{H2}$.

The Lewis theory frees acids and bases from the requirement that they contain a particular element or be in a particular solvent, and reveals their essence in terms of electron-pair donation and acceptance; it has the widest scope. Its limitation is that it is too general: almost every compound can be regarded as an acid–base adduct, and there is no unified quantitative scale of strength, since the order of strength of one Lewis base toward different Lewis acids can differ. The principle of hard and soft acids and bases partly remedies this shortcoming.

### 9.1.4. Hard and Soft Acids and Bases

Both Lewis acids and Lewis bases can be divided into hard and soft types, according to the **polarizability** ([6.1.4](/6.1.4)) of the atom that accepts or donates the electron pair:

- Hard bases have donor atoms of high electronegativity and small radius that are difficult to oxidize and not easily deformed, such as $\ce{F-}$, $\ce{OH-}$, and $\ce{H2O}$. Soft bases have donor atoms of low electronegativity and large radius that are easily oxidized and readily deformed, such as $\ce{I-}$, $\ce{S^2-}$, and $\ce{CN-}$.
- Hard acids are cations of high charge and small radius whose outer electrons are tightly held and not easily deformed, such as $\ce{H+}$, $\ce{Al^3+}$, and $\ce{Fe^3+}$. Soft acids are cations of low charge and large radius whose outer electrons (especially d electrons) are loosely held and easily deformed, such as $\ce{Cu+}$, $\ce{Ag+}$, and $\ce{Hg^2+}$.
- Those in between are called borderline acids and borderline bases.

| | Hard | Borderline | Soft |
|---|---|---|---|
| Acids | $\ce{H+}$, $\ce{Li+}$, $\ce{Na+}$, $\ce{K+}$, $\ce{Be^2+}$, $\ce{Mg^2+}$, $\ce{Ca^2+}$, $\ce{Al^3+}$, $\ce{Cr^3+}$, $\ce{Fe^3+}$, $\ce{Ti^4+}$, $\ce{BF3}$, $\ce{SO3}$ | $\ce{Fe^2+}$, $\ce{Co^2+}$, $\ce{Ni^2+}$, $\ce{Cu^2+}$, $\ce{Zn^2+}$, $\ce{Pb^2+}$, $\ce{SO2}$, $\ce{BBr3}$ | $\ce{Cu+}$, $\ce{Ag+}$, $\ce{Au+}$, $\ce{Tl+}$, $\ce{Hg2^2+}$, $\ce{Hg^2+}$, $\ce{Cd^2+}$, $\ce{Pd^2+}$, $\ce{Pt^2+}$, $\ce{BH3}$ |
| Bases | $\ce{F-}$, $\ce{OH-}$, $\ce{H2O}$, $\ce{O^2-}$, $\ce{NH3}$, $\ce{CO3^2-}$, $\ce{NO3-}$, $\ce{SO4^2-}$, $\ce{ClO4-}$, $\ce{NCS-}$ (N-bound) | $\ce{NO2-}$, $\ce{SO3^2-}$, $\ce{Br-}$, $\ce{N3-}$, $\ce{N2}$, $\ce{C5H5N}$ | $\ce{H-}$, $\ce{I-}$, $\ce{S^2-}$, $\ce{CN-}$, $\ce{CO}$, $\ce{SCN-}$ (S-bound), $\ce{R2S}$, $\ce{R3P}$, $\ce{C6H6}$ |

(Thiocyanate is an ambidentate ligand: it is a hard base when bound through N and a soft base when bound through S, so it appears in two places in the table. Mercury(I) exists as the dinuclear ion $\ce{Hg2^2+}$.)

**Definition 9.1.8 (Hard and Soft Acids and Bases)** The principle of **hard and soft acids and bases** (HSAB), formulated by Pearson (1963), states that hard acids preferentially combine with hard bases and soft acids preferentially combine with soft bases ("hard likes hard, soft likes soft"); the adducts so formed are relatively stable. Borderline acids and bases show little preference between soft and hard partners.

Broadly, the interaction between a hard acid and a hard base is mainly electrostatic (ionic bonding), while that between a soft acid and a soft base is mainly covalent. The principle is a qualitative empirical rule, but it explains many observations:

- When $\ce{NCS-}$ binds the hard acid $\ce{Fe^3+}$ it coordinates through N ($\ce{[Fe(NCS)]^2+}$, blood red); when it binds the soft acid $\ce{Hg^2+}$ it coordinates through S ($\ce{[Hg(SCN)4]^2-}$).
- $\ce{AgF}$ is readily soluble while $\ce{AgI}$ is extremely insoluble ([6.1.4](/6.1.4) explained the same fact through **ionic polarization**); the complexes of $\ce{Ag+}$ with $\ce{I-}$ and $\ce{CN-}$ are far more stable than that with $\ce{F-}$.

**Example 9.1.2** The common minerals of Ni and Cu are sulfides (pentlandite, chalcopyrite), whereas those of Al and Ca are oxides and carbonates (bauxite, limestone). Explain this with the HSAB principle.

**Solution** $\ce{O^2-}$ and $\ce{CO3^2-}$ are hard bases and $\ce{S^2-}$ is a soft base. $\ce{Al^3+}$ and $\ce{Ca^2+}$ are hard acids, whereas $\ce{Ni^2+}$ and $\ce{Cu^2+}$ are borderline acids and much softer than these ($\ce{Cu+}$ is even a soft acid). Hard acids combine with hard bases to form oxides and carbonates, and the softer acids combine with the soft base to form sulfides. Geochemistry uses this to classify the elements as lithophile or chalcophile.

## 9.2. Acidity and Basicity of Solutions

### 9.2.1. The Dissociation Equilibrium of Water

Pure water conducts electricity weakly, which shows that water undergoes autoionization (autoprotolysis):

$$
\ce{H2O(l) + H2O(l) <=> H3O+(aq) + OH-(aq)}, \qquad \text{abbreviated} \quad \ce{H2O <=> H+ + OH-}.
$$

**Definition 9.2.1** The standard equilibrium constant of the autoionization of water,

$$
K_{\mathrm{w}} = [\ce{H+}][\ce{OH-}]
$$
is called the **ion product of water** (the ion-product constant of water).

Pure water is the solvent; its activity is 1 and it does not appear in the expression. At $25\,^\circ\mathrm{C}$, $K_{\mathrm{w}} = 1.0 \times 10^{-14}$ ($\mathrm{p}K_{\mathrm{w}} = 14.00$), and in pure water $[\ce{H+}] = [\ce{OH-}] = 1.0 \times 10^{-7}$. This value can be calculated from thermodynamic data. With $\Delta_{\mathrm{f}}G^\circ(\ce{H2O}, \mathrm{l}) = -237.1\,\mathrm{kJ\,mol^{-1}}$ and $\Delta_{\mathrm{f}}G^\circ(\ce{OH-}, \mathrm{aq}) = -157.2\,\mathrm{kJ\,mol^{-1}}$ (by the convention $\Delta_{\mathrm{f}}G^\circ(\ce{H+}, \mathrm{aq}) = 0$), we have $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = 79.9\,\mathrm{kJ\,mol^{-1}}$, and by Eq. (8.3)

$$
K_{\mathrm{w}} = \exp\left(-\frac{79.9 \times 10^3}{8.314 \times 298.15}\right) = 1.0 \times 10^{-14}.
$$

The dissociation of water is the reverse of neutralization and is endothermic ($\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}} = 55.8\,\mathrm{kJ\,mol^{-1}}$), so by the **van 't Hoff equation** $K_{\mathrm{w}}$ increases with temperature:

| $t/{}^\circ\mathrm{C}$ | 0 | 10 | 25 | 37 | 50 | 100 |
|---|---|---|---|---|---|---|
| $\mathrm{p}K_{\mathrm{w}}$ | 14.94 | 14.53 | 14.00 | 13.62 | 13.26 | 12.26 |
| pH of a neutral solution | 7.47 | 7.27 | 7.00 | 6.81 | 6.63 | 6.13 |

$K_{\mathrm{w}}$ is a constraint linking $[\ce{H+}]$ and $[\ce{OH-}]$: in any aqueous solution their product equals $K_{\mathrm{w}}$, so knowing one gives the other. The acidity or basicity of a solution is determined by their relative magnitudes: the solution is acidic if $[\ce{H+}] > [\ce{OH-}]$, neutral if $[\ce{H+}] = [\ce{OH-}]$, and basic if $[\ce{H+}] < [\ce{OH-}]$. The statement that "neutral means $[\ce{H+}] = 10^{-7}$ and pH = 7" holds only at $25\,^\circ\mathrm{C}$: at body temperature, $37\,^\circ\mathrm{C}$, the pH of a neutral solution is 6.81, and blood at pH 7.4 is slightly basic.

### 9.2.2. pH

$[\ce{H+}]$ varies over a wide range (of order $1$ to $10^{-14}$), so a logarithmic scale is more convenient.

**Definition 9.2.2 (pH)** The **pH** of a solution is defined as the negative common logarithm of the hydrogen ion activity:

$$
\mathrm{pH} = -\lg a_{\ce{H+}} \approx -\lg\frac{[\ce{H+}]}{c^\circ}.
$$
Similarly, $\mathrm{pOH} = -\lg a_{\ce{OH-}}$ and $\mathrm{p}K = -\lg K$.

The approximate expression on the right (Sørensen's original definition of 1909) holds in dilute solution. The activity of a single ion cannot be measured rigorously, and in practice pH is obtained by an operational definition using standard buffer solutions and a pH meter ([Analytical Chemistry](/6.4)). Taking logarithms of $K_{\mathrm{w}} = [\ce{H+}][\ce{OH-}]$ gives

$$
\mathrm{pH} + \mathrm{pOH} = \mathrm{p}K_{\mathrm{w}} = 14.00 \quad (25\,^\circ\mathrm{C}).
$$
Each decrease of one pH unit multiplies $[\ce{H+}]$ by 10. The usual range of pH is 0–14, but it is not limited to this range: the pH of a $1\,\mathrm{mol\,L^{-1}}$ strong acid is about 0, and more concentrated strong acids have negative pH. In concentrated solutions activities and concentrations differ greatly and the approximate expression no longer applies.

### 9.2.3. Acid–Base Indicators

**Definition 9.2.3** An organic weak acid or weak base whose acid and base forms differ in structure and therefore show different colors over a certain pH range, so that it can be used to indicate the pH of a solution, is called an **acid–base indicator**.

Let HIn denote the acid form of the indicator and $\ce{In-}$ the base form:

$$
\ce{HIn <=> H+ + In-}, \qquad K_{\mathrm{a}}(\ce{HIn}) = \frac{[\ce{H+}][\ce{In-}]}{[\ce{HIn}]}, \qquad \frac{[\ce{In-}]}{[\ce{HIn}]} = \frac{K_{\mathrm{a}}(\ce{HIn})}{[\ce{H+}]}.
$$
The color of the solution depends on $[\ce{In-}]/[\ce{HIn}]$, that is, on pH. The human eye generally sees only the color of one form once its concentration reaches about ten times that of the other: the acid color is seen when $[\ce{In-}]/[\ce{HIn}] \le 1/10$, the base color when the ratio is $\ge 10$, and a mixed color in between.

**Definition 9.2.4** The pH interval over which an indicator changes from its acid color to its base color is called the **transition range**; theoretically it is $\mathrm{pH} = \mathrm{p}K_{\mathrm{a}}(\ce{HIn}) \pm 1$, and the point $\mathrm{pH} = \mathrm{p}K_{\mathrm{a}}(\ce{HIn})$ is called the theoretical transition point.

The actual transition range is determined by visual observation; because the eye is not equally sensitive to different colors, it is often not exactly $\mathrm{p}K_{\mathrm{a}} \pm 1$, and its width is usually less than 2 pH units:

| Indicator | Transition range | Acid color → base color |
|---|---|---|
| Methyl orange | 3.1–4.4 | red → yellow |
| Methyl red | 4.4–6.2 | red → yellow |
| Litmus | 5.0–8.0 | red → blue |
| Bromothymol blue | 6.0–7.6 | yellow → blue |
| Phenolphthalein | 8.0–10.0 | colorless → red |

The color change reflects a change in structure. In acidic and neutral solutions phenolphthalein exists as the colorless lactone form (1), in which the three benzene rings are not conjugated; in basic solution the ring opens to the quinoid dianion (2), forming a conjugated system that extends through the whole molecule, so the absorption shifts into the visible region and the solution appears red. The base form (3) of methyl orange is a yellow azo compound; in acid the N of the azo group is protonated to give the quinoid structure (4) with a longer conjugated system, which is red:

```smiles
O=C1OC(c2ccccc12)(c1ccc(O)cc1)c1ccc(O)cc1 1
[O-]C(=O)c1ccccc1C(=C1C=CC(=O)C=C1)c1ccc([O-])cc1 2
```

```smiles
CN(C)c1ccc(cc1)N=Nc1ccc(cc1)S(=O)(=O)[O-] 3
C[N+](C)=C1C=CC(C=C1)=NNc1ccc(cc1)S(=O)(=O)[O-] 4
```

Mixing several indicators with different transition ranges gives a mixed indicator that shows different colors at different pH values; soaked into paper it becomes pH test paper.

## 9.3. Dissociation Equilibria of Weak Acids and Bases

### 9.3.1. Dissociation Constants

**Definition 9.3.1** The standard equilibrium constant of the dissociation of a weak acid HA in water, $\ce{HA + H2O <=> H3O+ + A-}$ (abbreviated $\ce{HA <=> H+ + A-}$),

$$
K_{\mathrm{a}} = \frac{[\ce{H+}][\ce{A-}]}{[\ce{HA}]}
$$
is called the **acid dissociation constant**; the standard equilibrium constant of the dissociation of a weak base B, $\ce{B + H2O <=> BH+ + OH-}$,

$$
K_{\mathrm{b}} = \frac{[\ce{BH+}][\ce{OH-}]}{[\ce{B}]}
$$
is called the **base dissociation constant**.

For example, $K_{\mathrm{a}}(\ce{HAc}) = 1.75 \times 10^{-5}$ and $K_{\mathrm{b}}(\ce{NH3}) = 1.8 \times 10^{-5}$. Like $K^\circ$, a dissociation constant depends only on temperature and not on concentration. At the same temperature, the larger $K_{\mathrm{a}}$ is, the stronger the acid. Acids with $K_{\mathrm{a}}$ between $10^{-2}$ and $10^{-7}$ are generally called weak acids, and those with $K_{\mathrm{a}} < 10^{-7}$ very weak acids.

**Theorem 9.3.1** The dissociation constants of a conjugate acid–base pair HA–$\ce{A-}$ satisfy

$$
K_{\mathrm{a}}(\ce{HA})\,K_{\mathrm{b}}(\ce{A-}) = K_{\mathrm{w}}, \qquad \mathrm{p}K_{\mathrm{a}} + \mathrm{p}K_{\mathrm{b}} = \mathrm{p}K_{\mathrm{w}}. \tag{9.1}
$$

**Proof** The dissociation of $\ce{A-}$ as a base is $\ce{A- + H2O <=> HA + OH-}$, with $K_{\mathrm{b}} = \frac{[\ce{HA}][\ce{OH-}]}{[\ce{A-}]}$. Adding it to $\ce{HA <=> H+ + A-}$ gives $\ce{H2O <=> H+ + OH-}$, so by the **rule of multiple equilibria** (Theorem 8.2.1), $K_{\mathrm{a}}K_{\mathrm{b}} = K_{\mathrm{w}}$. Multiplying the two expressions directly gives the same result. $\square$

Equation (9.1) makes the statement "the stronger the acid, the weaker its conjugate base" quantitative, so a table needs to list only $K_{\mathrm{a}}$ or $\mathrm{p}K_{\mathrm{a}}$:

| Acid | $\mathrm{p}K_{\mathrm{a}}$ | $K_{\mathrm{a}}$ | Acid | $\mathrm{p}K_{\mathrm{a}}$ | $K_{\mathrm{a}}$ |
|---|---|---|---|---|---|
| $\ce{H2C2O4}$ | 1.25, 3.81 | $5.6\times10^{-2}$, $1.5\times10^{-4}$ | $\ce{H2CO3}$ | 6.35, 10.33 | $4.5\times10^{-7}$, $4.7\times10^{-11}$ |
| $\ce{H3PO4}$ | 2.16, 7.21, 12.32 | $6.9\times10^{-3}$, $6.2\times10^{-8}$, $4.8\times10^{-13}$ | $\ce{H2S}$ | 7.05, about 19 | $8.9\times10^{-8}$, about $10^{-19}$ |
| HF | 3.20 | $6.3\times10^{-4}$ | $\ce{HCN}$ | 9.21 | $6.2\times10^{-10}$ |
| $\ce{HNO2}$ | 3.25 | $5.6\times10^{-4}$ | $\ce{NH4+}$ | 9.25 | $5.6\times10^{-10}$ |
| HCOOH | 3.75 | $1.8\times10^{-4}$ | $\ce{H3BO3}$ | 9.27 | $5.4\times10^{-10}$ |
| $\ce{HAc}$ | 4.76 | $1.75\times10^{-5}$ | $\ce{H2O}$ | 14.00 | $1.0\times10^{-14}$ (that is, $K_{\mathrm{w}}$) |

(HAc is acetic acid $\ce{CH3COOH}$ and Ac stands for the acetate group; for $\ce{NH4+}$, $K_{\mathrm{a}} = K_{\mathrm{w}}/K_{\mathrm{b}}(\ce{NH3})$.) The structures of acetic acid, acetate, and phosphoric acid are shown below (the hydrogen that dissociates is the one bound to the electronegative O; the hydrogens of the methyl group do not dissociate):

```smiles
CC(=O)O HAc
CC(=O)[O-] Ac-
OP(=O)(O)O H3PO4
```

### 9.3.2. The pH of Solutions of Monoprotic Weak Acids and Bases

**Example 9.3.1** Calculate $[\ce{H+}]$, the pH, and the degree of dissociation of a $0.10\,\mathrm{mol\,L^{-1}}$ HAc solution.

**Solution** The solution contains two equilibria: $\ce{HAc <=> H+ + Ac-}$ ($K_{\mathrm{a}} = 1.75 \times 10^{-5}$) and $\ce{H2O <=> H+ + OH-}$ ($K_{\mathrm{w}} = 10^{-14}$). Since $K_{\mathrm{a}}c \gg K_{\mathrm{w}}$, the $\ce{H+}$ produced by the dissociation of water can be neglected. Let $[\ce{H+}] = x$:

| | $\ce{HAc}$ | $\ce{H+}$ | $\ce{Ac-}$ |
|---|---|---|---|
| Initial | 0.10 | 0 | 0 |
| Equilibrium | $0.10 - x$ | $x$ | $x$ |

$$
K_{\mathrm{a}} = \frac{x^2}{0.10 - x} = 1.75 \times 10^{-5}.
$$
Solving the quadratic equation $x^2 + K_{\mathrm{a}}x - K_{\mathrm{a}}c = 0$ gives $x = 1.31 \times 10^{-3}$. If we assume $x \ll 0.10$ and $0.10 - x \approx 0.10$, then $x = \sqrt{K_{\mathrm{a}}c} = 1.32 \times 10^{-3}$, which differs by only 0.7%. Thus $\mathrm{pH} = 2.88$ and the degree of dissociation is $\alpha = x/c = 1.3\%$.

In general, for a monoprotic weak acid of concentration $c$, when the dissociation of water can be neglected,

$$
[\ce{H+}] = \frac{-K_{\mathrm{a}} + \sqrt{K_{\mathrm{a}}^2 + 4K_{\mathrm{a}}c}}{2} \approx \sqrt{K_{\mathrm{a}}c}; \qquad \text{monoprotic weak base: }\ [\ce{OH-}] \approx \sqrt{K_{\mathrm{b}}c}. \tag{9.2}
$$

Under what conditions is the approximation usable? Let $r = c/K_{\mathrm{a}}$. The exact solution is $[\ce{H+}]/K_{\mathrm{a}} = \frac{1}{2}(\sqrt{1 + 4r} - 1)$, and the approximate solution is $\sqrt r$. For large $r$, $\sqrt{1 + 4r} = 2\sqrt r\sqrt{1 + 1/(4r)} \approx 2\sqrt r + \frac{1}{4\sqrt r}$, so the exact solution is $\approx \sqrt r - \frac{1}{2}$, and the relative error of the approximation is

$$
\varepsilon = \frac{\sqrt r}{\sqrt r - 1/2} - 1 \approx \frac{1}{2\sqrt r} \approx \frac{\alpha}{2}.
$$
The approximation always overestimates, with an error of about half the degree of dissociation. The criterion $c/K_{\mathrm{a}} \ge 400$ commonly given in textbooks corresponds to $\sqrt r \ge 20$: the error is about 2.5% (a difference of only 0.01 in pH) and the degree of dissociation is about 5%. Hence "$c/K_{\mathrm{a}} \ge 400$" and "degree of dissociation below 5%" are the same condition. When it is not satisfied, the quadratic equation must be solved.

![Relative error of [H⁺] from the √(Ka c) approximation for a monoprotic weak acid, and the degree of dissociation, as functions of c/Ka: the error is about half the degree of dissociation; at c/Ka = 400 the error is 2.5% and the degree of dissociation is 4.9%](./plots/weak-acid-approximation.py)

Neglecting the dissociation of water also requires a condition. By electroneutrality, $[\ce{H+}] = [\ce{A-}] + [\ce{OH-}]$; when the acid dissociates only slightly, $[\ce{A-}] \approx K_{\mathrm{a}}c/[\ce{H+}]$, and substitution gives $[\ce{H+}] \approx \sqrt{K_{\mathrm{a}}c + K_{\mathrm{w}}}$. When $K_{\mathrm{a}}c \ge 20K_{\mathrm{w}}$, the error from dropping $K_{\mathrm{w}}$ does not exceed 2.5%. Very dilute or very weak acids (such as $10^{-6}\,\mathrm{mol\,L^{-1}}$ $\ce{HCN}$) do not satisfy this condition, and the dissociation of water must be included.

### 9.3.3. Degree of Dissociation and the Dilution Law

Both the degree of dissociation $\alpha$ and $K_{\mathrm{a}}$ express the extent of dissociation of a weak acid, but $K_{\mathrm{a}}$ depends only on temperature, whereas $\alpha$ also varies with concentration. From $K_{\mathrm{a}} = \frac{c\alpha^2}{1 - \alpha}$, for small $\alpha$:

**Theorem 9.3.2 (Dilution Law)** For a monoprotic weak acid (weak base), the degree of dissociation is inversely proportional to the square root of the concentration and directly proportional to the square root of the dissociation constant:

$$
\alpha \approx \sqrt{\frac{K_{\mathrm{a}}}{c}} \qquad \left(\text{weak base: }\ \alpha \approx \sqrt{\frac{K_{\mathrm{b}}}{c}}\right).
$$

This law was derived by Ostwald (1888) from the law of mass action, and it was an early confirmation of the Arrhenius theory. The more dilute the solution, the larger the degree of dissociation; but $[\ce{H+}] = c\alpha \approx \sqrt{K_{\mathrm{a}}c}$ still decreases on dilution. So "the higher the concentration, the smaller the degree of dissociation" does not mean that $[\ce{H+}]$ is smaller.

### 9.3.4. The Common-Ion Effect

When NaAc is added to a HAc solution, $[\ce{Ac-}]$ increases, $Q > K_{\mathrm{a}}$, the equilibrium $\ce{HAc <=> H+ + Ac-}$ shifts to the left, and the degree of dissociation of HAc decreases.

**Definition 9.3.2 (Common-Ion Effect)** The lowering of the degree of dissociation of a weak electrolyte by the addition of a strong electrolyte that contains an ion in common with it, in a solution where dissociation equilibrium is already established, is called the **common-ion effect**.

**Example 9.3.2** Solid NaAc is added to a $0.10\,\mathrm{mol\,L^{-1}}$ HAc solution until the NaAc concentration is $0.10\,\mathrm{mol\,L^{-1}}$ (neglect the volume change). Find $[\ce{H+}]$ and the degree of dissociation of HAc.

**Solution** Let $[\ce{H+}] = x$. Then $[\ce{HAc}] = 0.10 - x \approx 0.10$ and $[\ce{Ac-}] = 0.10 + x \approx 0.10$ (the common-ion effect makes $x$ even smaller, so the approximation is better):

$$
K_{\mathrm{a}} = \frac{x \times 0.10}{0.10} \quad\Longrightarrow\quad x = K_{\mathrm{a}} = 1.75 \times 10^{-5}, \qquad \alpha = \frac{x}{0.10} = 0.018\%.
$$
Compared with Example 9.3.1, $[\ce{H+}]$ falls from $1.3 \times 10^{-3}$ to $1.75 \times 10^{-5}$ and the degree of dissociation falls to about 1/75 of its former value; the more NaAc is added, the greater the decrease. This solution is the buffer solution of 9.5. The common-ion effect also lowers the solubility of sparingly soluble electrolytes ([6.1.10](/6.1.10)).

### 9.3.5. Polyprotic Acids

A weak acid that can donate two or more protons dissociates stepwise.

**Definition 9.3.3** A weak acid whose molecule can donate two or more protons is called a **polyprotic acid**; its protons dissociate stepwise, and the successive dissociation constants are denoted $K_{\mathrm{a1}}, K_{\mathrm{a2}}, \dots$.

Take $\ce{H2S}$ as an example:

$$
\ce{H2S <=> H+ + HS-}, \quad K_{\mathrm{a1}} = \frac{[\ce{H+}][\ce{HS-}]}{[\ce{H2S}]}; \qquad \ce{HS- <=> H+ + S^2-}, \quad K_{\mathrm{a2}} = \frac{[\ce{H+}][\ce{S^2-}]}{[\ce{HS-}]}.
$$
Adding the two gives $\ce{H2S <=> 2H+ + S^2-}$, with $K = K_{\mathrm{a1}}K_{\mathrm{a2}} = \frac{[\ce{H+}]^2[\ce{S^2-}]}{[\ce{H2S}]}$. The successive dissociation constants decrease markedly from step to step: it is much harder to remove another proton from the negatively charged $\ce{HS-}$ than from the neutral molecule. The concentrations of all species in solution must satisfy all the equilibria simultaneously (including the dissociation of water), but one equilibrium usually dominates.

**Example 9.3.3** In a saturated aqueous solution of $\ce{H2S}$ at room temperature, $[\ce{H2S}] \approx 0.10\,\mathrm{mol\,L^{-1}}$. Calculate $[\ce{H+}]$, $[\ce{HS-}]$, $[\ce{S^2-}]$, and $[\ce{OH-}]$. Take $K_{\mathrm{a1}} = 8.9 \times 10^{-8}$.

**Solution** Since $K_{\mathrm{a1}} \gg K_{\mathrm{a2}}$, the $\ce{H+}$ from the second dissociation can be neglected and the acid treated as monoprotic; since $c/K_{\mathrm{a1}} > 400$,

$$
[\ce{H+}] \approx [\ce{HS-}] \approx \sqrt{K_{\mathrm{a1}}c} = \sqrt{8.9 \times 10^{-8} \times 0.10} = 9.4 \times 10^{-5}, \qquad \mathrm{pH} = 4.02.
$$
From the second dissociation, $K_{\mathrm{a2}} = [\ce{H+}][\ce{S^2-}]/[\ce{HS-}]$ and $[\ce{H+}] \approx [\ce{HS-}]$, we obtain $[\ce{S^2-}] \approx K_{\mathrm{a2}}$; and $[\ce{OH-}] = K_{\mathrm{w}}/[\ce{H+}] = 1.1 \times 10^{-10}$.

Two general rules follow:

1. When $K_{\mathrm{a1}} \gg K_{\mathrm{a2}} \gg \cdots$ (differing by more than $10^3$) for a polyprotic acid, $[\ce{H+}]$ can be calculated by treating the acid as monoprotic, and $K_{\mathrm{a1}}$ can serve as the measure of its acid strength.
2. In a solution of a diprotic acid, the concentration of the acid anion is approximately equal to $K_{\mathrm{a2}}$, independent of the concentration of the acid.

**Remark 9.3.1** The $K_{\mathrm{a2}}$ of $\ce{H2S}$ is very hard to measure. Many textbooks still use $K_{\mathrm{a2}} \approx 10^{-13}$–$10^{-14}$; these values are out of date. $\ce{S^2-}$ is an extremely strong base and in water is converted almost completely to $\ce{HS-}$. Raman and ultraviolet spectroscopic measurements of recent decades give $\mathrm{p}K_{\mathrm{a2}} \approx 17$–$19$, and the CRC Handbook takes 19. With this value, $[\ce{S^2-}] \approx 10^{-19}\,\mathrm{mol\,L^{-1}}$ in Example 9.3.3, so that one liter of solution contains only about $6 \times 10^4$ $\ce{S^2-}$ ions: in aqueous solution, $\ce{S^2-}$ is effectively not a meaningful species. For this reason [6.1.10](/6.1.10) treats the dissolution and precipitation of sulfides without going through $[\ce{S^2-}]$, using an equilibrium constant that is independent of $K_{\mathrm{a2}}$.

The equilibrium constant of the overall reaction also shows how pH controls the concentration of the acid anion. For any diprotic acid $\ce{H2A}$,

$$
[\ce{A^2-}] = \frac{K_{\mathrm{a1}}K_{\mathrm{a2}}[\ce{H2A}]}{[\ce{H+}]^2}: \tag{9.3}
$$
for a given $[\ce{H2A}]$, the anion concentration is inversely proportional to $[\ce{H+}]^2$, so adjusting the pH controls $[\ce{A^2-}]$ and hence the effective concentration of precipitants such as $\ce{CO3^2-}$, $\ce{C2O4^2-}$, and $\ce{PO4^3-}$ ([6.1.10](/6.1.10)).

### 9.3.6. Distribution Fractions

**Definition 9.3.4** The fraction of the total concentration $c$ of a weak acid that is present as a given species at equilibrium is called the **distribution fraction** of that species, denoted $\delta$.

For a monoprotic weak acid, $c = [\ce{HA}] + [\ce{A-}]$, and from the expression for $K_{\mathrm{a}}$,

$$
\delta(\ce{HA}) = \frac{[\ce{H+}]}{[\ce{H+}] + K_{\mathrm{a}}}, \qquad \delta(\ce{A-}) = \frac{K_{\mathrm{a}}}{[\ce{H+}] + K_{\mathrm{a}}}.
$$
For a diprotic weak acid, let $D = [\ce{H+}]^2 + K_{\mathrm{a1}}[\ce{H+}] + K_{\mathrm{a1}}K_{\mathrm{a2}}$; then

$$
\delta(\ce{H2A}) = \frac{[\ce{H+}]^2}{D}, \qquad \delta(\ce{HA-}) = \frac{K_{\mathrm{a1}}[\ce{H+}]}{D}, \qquad \delta(\ce{A^2-}) = \frac{K_{\mathrm{a1}}K_{\mathrm{a2}}}{D}.
$$
Distribution fractions are functions of pH only and are independent of the total concentration. At $\mathrm{pH} = \mathrm{p}K_{\mathrm{a}}$, the two forms of a conjugate acid–base pair are present in equal amounts; at a pH one unit below $\mathrm{p}K_{\mathrm{a}}$, the acid form accounts for 91%, and at two units below, 99%.

![Distribution fractions of the species of acetic acid, carbonic acid, and phosphoric acid as functions of pH: the curves of adjacent forms cross at pH = pKa](./plots/distribution-fractions.py)

The figure shows directly that at the blood pH of 7.4, carbonic acid exists mainly as $\ce{HCO3-}$ and phosphoric acid mainly as $\ce{H2PO4-}$ and $\ce{HPO4^2-}$ (both facts are used in 9.5); $\ce{PO4^3-}$ becomes significant only in strongly basic solution. The distribution fractions of polyprotic acids and the systematic treatment of amphiprotic substances are found in [Analytical Chemistry](/6.4).

## 9.4. Acid–Base Equilibria in Salt Solutions

### 9.4.1. Hydrolysis of Salts

A $\ce{NaAc}$ solution is basic, an $\ce{NH4Cl}$ solution is acidic, and a $\ce{NaCl}$ solution is neutral. The Arrhenius theory calls this the hydrolysis of salts.

**Definition 9.4.1** The reaction in which the constituent ions of a salt dissolved in water undergo proton transfer with water to form a weak acid or weak base, thereby shifting the dissociation equilibrium of water so that $[\ce{H+}]$ and $[\ce{OH-}]$ are no longer equal, is called **salt hydrolysis**.

In the Brønsted–Lowry theory, hydrolysis of a salt is simply the dissociation of an ionic acid or ionic base, and no separate theory is needed:

- $\ce{Ac- + H2O <=> HAc + OH-}$ is the dissociation of the base $\ce{Ac-}$, and its equilibrium constant is $K_{\mathrm{b}}(\ce{Ac-}) = K_{\mathrm{w}}/K_{\mathrm{a}}(\ce{HAc})$;
- $\ce{NH4+ + H2O <=> NH3 + H3O+}$ is the dissociation of the acid $\ce{NH4+}$, and its equilibrium constant is $K_{\mathrm{a}}(\ce{NH4+}) = K_{\mathrm{w}}/K_{\mathrm{b}}(\ce{NH3})$.

Chinese textbooks often introduce a separate "hydrolysis constant $K_{\mathrm{h}}$", which is simply the $K_{\mathrm{b}}$ of the conjugate base (or the $K_{\mathrm{a}}$ of the conjugate acid); this wiki does not use that symbol. By Eq. (9.1), the weaker the parent acid (or base), the stronger the hydrolysis. The ions of salts of strong acids and strong bases (salts formed by alkali and alkaline-earth metals with $\ce{HClO4}$, $\ce{HCl}$, $\ce{HNO3}$, and $\ce{H2SO4}$) are extremely weak acids or bases; they do not hydrolyze, and the solution is neutral. The extent of hydrolysis can be expressed by the degree of hydrolysis $h$ (the percentage of the initial salt concentration that has hydrolyzed), which is the degree of dissociation of the ionic acid or base, $h \approx \sqrt{K_{\mathrm{b}}/c}$.

### 9.4.2. Salts of Weak Acids with Strong Bases and of Strong Acids with Weak Bases

**Example 9.4.1** Calculate the pH of a $0.10\,\mathrm{mol\,L^{-1}}$ NaAc solution.

**Solution** $K_{\mathrm{b}}(\ce{Ac-}) = \frac{K_{\mathrm{w}}}{K_{\mathrm{a}}(\ce{HAc})} = \frac{1.0 \times 10^{-14}}{1.75 \times 10^{-5}} = 5.7 \times 10^{-10}$. Since $c/K_{\mathrm{b}} > 400$, Eq. (9.2) gives

$$
[\ce{OH-}] = \sqrt{K_{\mathrm{b}}c} = \sqrt{5.7 \times 10^{-10} \times 0.10} = 7.6 \times 10^{-6}, \qquad \mathrm{pOH} = 5.12, \quad \mathrm{pH} = 8.88.
$$

**Example 9.4.2** Calculate the pH of a $0.10\,\mathrm{mol\,L^{-1}}$ $\ce{NH4Cl}$ solution and the degree of dissociation (degree of hydrolysis) of $\ce{NH4+}$.

**Solution** $K_{\mathrm{a}}(\ce{NH4+}) = \frac{K_{\mathrm{w}}}{K_{\mathrm{b}}(\ce{NH3})} = 5.6 \times 10^{-10}$ and $c/K_{\mathrm{a}} > 400$, so $[\ce{H+}] = \sqrt{5.6 \times 10^{-10} \times 0.10} = 7.5 \times 10^{-6}$, $\mathrm{pH} = 5.13$; and $h = 7.5 \times 10^{-6}/0.10 = 0.0075\%$.

Salts of polyprotic weak acids with strong bases ($\ce{Na2CO3}$, $\ce{Na3PO4}$, $\ce{Na2S}$) hydrolyze stepwise. For $\ce{PO4^3-}$, the three values of $K_{\mathrm{b}}$ are obtained from Eq. (9.1) by pairing in reverse order with the three $K_{\mathrm{a}}$ values of phosphoric acid:

$$
K_{\mathrm{b1}} = \frac{K_{\mathrm{w}}}{K_{\mathrm{a3}}} = 2.1 \times 10^{-2}, \qquad K_{\mathrm{b2}} = \frac{K_{\mathrm{w}}}{K_{\mathrm{a2}}} = 1.6 \times 10^{-7}, \qquad K_{\mathrm{b3}} = \frac{K_{\mathrm{w}}}{K_{\mathrm{a1}}} = 1.4 \times 10^{-12}.
$$
Since $K_{\mathrm{b1}} \gg K_{\mathrm{b2}}$, only the first step is usually considered.

**Example 9.4.3** Calculate the pH of a $0.10\,\mathrm{mol\,L^{-1}}$ $\ce{Na3PO4}$ solution.

**Solution** Here $c/K_{\mathrm{b1}} = 4.8 < 400$: $\ce{PO4^3-}$ is a fairly strong base, and the approximate formula cannot be used. Let $[\ce{OH-}] = x$:

$$
\frac{x^2}{0.10 - x} = 2.1 \times 10^{-2}, \qquad x^2 + 0.021x - 2.1 \times 10^{-3} = 0, \qquad x = 0.036.
$$
Then $\mathrm{pOH} = 1.44$ and $\mathrm{pH} = 12.56$. About 36% of the $\ce{PO4^3-}$ is converted to $\ce{HPO4^2-}$; had we misused $\sqrt{K_{\mathrm{b1}}c}$, we would have obtained $x = 0.046$, about 25% too large. The strong basicity of $\ce{Na3PO4}$ solutions makes them useful as detergents and boiler-water treatment agents.

### 9.4.3. Amphiprotic Substances: Charge Balance, Mass Balance, and the Proton Condition

The anions of acid salts such as $\ce{NaHCO3}$, $\ce{NaH2PO4}$, and $\ce{Na2HPO4}$ can both donate and accept protons:

$$
\ce{HCO3- <=> H+ + CO3^2-}\quad (K_{\mathrm{a2}} = 4.7 \times 10^{-11}), \qquad \ce{HCO3- + H2O <=> H2CO3 + OH-}\quad \left(K_{\mathrm{b}} = \frac{K_{\mathrm{w}}}{K_{\mathrm{a1}}} = 2.2 \times 10^{-8}\right).
$$
The two equilibria proceed simultaneously to comparable extents, and we cannot take just one of them. The general method for such problems is to write down the conservation relations that the solution must satisfy.

**Definition 9.4.2** The relation stating that the analytical (total) concentration of a component of a solution equals the sum of the equilibrium concentrations of all its forms in solution is called the **mass balance**; the relation stating that the solution remains electrically neutral, so that the total concentration of positive charge carried by the cations equals the total concentration of negative charge carried by the anions, is called the **charge balance** (the concentration of each ion multiplied by its charge number).

**Definition 9.4.3** At acid–base equilibrium, the total amount of protons gained by the species that gain protons equals the total amount of protons lost by the species that lose protons; the equation expressing this is called the **proton condition**. To write it, we choose as the reference level the original species present in large amounts that take part in proton transfer (together with the solvent water); species with more protons than the reference level are written on one side and species with fewer protons on the other, each concentration multiplied by the number of protons gained or lost.

For a $\ce{NaHCO3}$ solution of concentration $c$:

- mass balance: $c = [\ce{H2CO3}] + [\ce{HCO3-}] + [\ce{CO3^2-}]$, and $[\ce{Na+}] = c$;
- charge balance: $[\ce{Na+}] + [\ce{H+}] = [\ce{HCO3-}] + 2[\ce{CO3^2-}] + [\ce{OH-}]$;
- subtracting the two, which eliminates $[\ce{Na+}]$ and $[\ce{HCO3-}]$, gives the proton condition

$$
[\ce{H+}] + [\ce{H2CO3}] = [\ce{CO3^2-}] + [\ce{OH-}].
$$
Taking $\ce{HCO3-}$ and $\ce{H2O}$ as the reference level gives the same result directly: $\ce{H2CO3}$ and $\ce{H3O+}$ each have one proton more than the reference level, and $\ce{CO3^2-}$ and $\ce{OH-}$ each have one fewer.

Substituting $[\ce{H2CO3}] = \frac{[\ce{H+}][\ce{HCO3-}]}{K_{\mathrm{a1}}}$, $[\ce{CO3^2-}] = \frac{K_{\mathrm{a2}}[\ce{HCO3-}]}{[\ce{H+}]}$, and $[\ce{OH-}] = \frac{K_{\mathrm{w}}}{[\ce{H+}]}$ into the proton condition and rearranging gives

$$
[\ce{H+}] = \sqrt{\frac{K_{\mathrm{a2}}[\ce{HCO3-}] + K_{\mathrm{w}}}{1 + [\ce{HCO3-}]/K_{\mathrm{a1}}}}.
$$
No approximation has been made in this step. The reaction of $\ce{HCO3-}$ proceeds only slightly in either direction, so $[\ce{HCO3-}] \approx c$; and if in addition $K_{\mathrm{a2}}c \gg K_{\mathrm{w}}$ and $c \gg K_{\mathrm{a1}}$ (true unless the solution is very dilute), then

$$
[\ce{H+}] \approx \sqrt{K_{\mathrm{a1}}K_{\mathrm{a2}}}, \qquad \mathrm{pH} \approx \tfrac{1}{2}(\mathrm{p}K_{\mathrm{a1}} + \mathrm{p}K_{\mathrm{a2}}). \tag{9.4}
$$

**Example 9.4.4** Estimate the pH of $0.10\,\mathrm{mol\,L^{-1}}$ solutions of $\ce{NaHCO3}$, $\ce{NaH2PO4}$, and $\ce{Na2HPO4}$.

**Solution** By Eq. (9.4): for $\ce{NaHCO3}$, $\mathrm{pH} = \frac{1}{2}(6.35 + 10.33) = 8.34$ (the formula without approximation gives the same value); in $\ce{NaH2PO4}$, $\ce{H2PO4-}$ lies between $\ce{H3PO4}$ and $\ce{HPO4^2-}$, and $\mathrm{pH} = \frac{1}{2}(2.16 + 7.21) = 4.69$; for $\ce{Na2HPO4}$, $\mathrm{pH} = \frac{1}{2}(7.21 + 12.32) = 9.77$. The acidity or basicity of an amphiprotic substance depends on which is larger, its tendency to act as an acid or as a base: for $\ce{H2PO4-}$, $K_{\mathrm{a2}} = 6.2 \times 10^{-8}$ exceeds $K_{\mathrm{b}} = K_{\mathrm{w}}/K_{\mathrm{a1}} = 1.4 \times 10^{-12}$, so the solution is acidic; for $\ce{HCO3-}$ and $\ce{HPO4^2-}$ the opposite holds. (The concentration of $\ce{NaH2PO4}$ is not large enough relative to $K_{\mathrm{a1}}$; the more accurate result is about 4.7, a very small difference.)

### 9.4.4. Salts of Weak Acids with Weak Bases

In $\ce{NH4Ac}$ and $\ce{NH4CN}$ the cation is a weak acid and the anion a weak base, and both react with water. Taking $\ce{NH4+}$, $\ce{A-}$, and $\ce{H2O}$ as the reference level, the proton condition is $[\ce{H+}] + [\ce{HA}] = [\ce{NH3}] + [\ce{OH-}]$. The derivation is exactly the same as for amphiprotic substances, and at ordinary concentrations one obtains

$$
[\ce{H+}] \approx \sqrt{K_{\mathrm{a}}(\ce{HA})K_{\mathrm{a}}(\ce{NH4+})} = \sqrt{\frac{K_{\mathrm{w}}K_{\mathrm{a}}(\ce{HA})}{K_{\mathrm{b}}(\ce{NH3})}}.
$$
The pH of the solution is approximately independent of the salt concentration and depends only on the dissociation constants of the weak acid and weak base: the solution is neutral when $K_{\mathrm{a}}(\ce{HA}) = K_{\mathrm{b}}(\ce{NH3})$ ($\ce{NH4Ac}$, pH 7.0), acidic when $K_{\mathrm{a}} > K_{\mathrm{b}}$ ($\ce{NH4F}$, $\ce{HCOONH4}$), and basic when $K_{\mathrm{a}} < K_{\mathrm{b}}$ ($\ce{NH4CN}$, $\ce{(NH4)2CO3}$).

### 9.4.5. Patterns of Acidity and Basicity of Salt Solutions and Influencing Factors

| Solution | Type of salt | Criterion | Examples |
|---|---|---|---|
| Neutral | Strong acid and strong base | No hydrolysis | $\ce{NaCl}$, $\ce{KNO3}$, $\ce{BaI2}$ |
| | Weak acid and weak base | $K_{\mathrm{a}} \approx K_{\mathrm{b}}$ | $\ce{NH4Ac}$ |
| Acidic | Strong acid and weak base | Cation is a weak acid | $\ce{NH4Cl}$, $\ce{AlCl3}$, $\ce{FeCl3}$ |
| | Acid salt | Anion has $K_{\mathrm{a}} > K_{\mathrm{b}}$ | $\ce{NaH2PO4}$, $\ce{NaHSO4}$ |
| | Weak acid and weak base | $K_{\mathrm{a}} > K_{\mathrm{b}}$ | $\ce{NH4F}$, $\ce{HCOONH4}$ |
| Basic | Weak acid and strong base | Anion is a weak base | $\ce{NaAc}$, $\ce{NaCN}$, $\ce{Na2CO3}$ |
| | Acid salt | Anion has $K_{\mathrm{a}} < K_{\mathrm{b}}$ | $\ce{Na2HPO4}$, $\ce{NaHCO3}$ |
| | Weak acid and weak base | $K_{\mathrm{a}} < K_{\mathrm{b}}$ | $\ce{NH4CN}$, $\ce{(NH4)2CO3}$ |

The hydrated ions of highly charged metal ions such as $\ce{Al^3+}$ and $\ce{Fe^3+}$ are fairly strong acids ($\mathrm{p}K_{\mathrm{a}} \approx 2.2$ for $\ce{[Fe(H2O)6]^3+}$, comparable to the first step of phosphoric acid): the higher the charge and the smaller the radius of the central ion, the more strongly it polarizes the coordinated water molecules and the more readily the protons of the O–H bonds leave.

Factors affecting the extent of hydrolysis:

1. Concentration: from $h \approx \sqrt{K_{\mathrm{b}}/c}$, dilution increases the degree of hydrolysis.
2. Temperature: hydrolysis is the reverse of neutralization and is endothermic, so raising the temperature increases the hydrolysis constant (**van 't Hoff equation**) and the degree of hydrolysis. This is why a $\ce{FeCl3}$ solution darkens on heating and deposits hydroxide.
3. pH of the solution: hydrolysis produces $\ce{H+}$ (or $\ce{OH-}$), and adding acid (or base) shifts the hydrolysis equilibrium backward. Solutions of $\ce{FeCl3}$, $\ce{SnCl2}$, and $\ce{Bi(NO3)3}$ are prepared by first dissolving the salt in the corresponding acid, to suppress hydrolysis and precipitation.
4. Mutual promotion (double hydrolysis): when a weakly basic cation meets a weakly acidic anion, one produces $\ce{H+}$ and the other consumes it, and if the products are a precipitate or a gas, hydrolysis can go to completion. Foam fire extinguishers use $\ce{Al^3+ + 3HCO3- -> Al(OH)3 v + 3CO2 ^}$; $\ce{Al2S3}$ cannot exist in water: $\ce{2Al^3+ + 3S^2- + 6H2O -> 2Al(OH)3 v + 3H2S ^}$.

## 9.5. Buffer Solutions

### 9.5.1. Buffer Action and Its Principle

When one drop (about $0.05\,\mathrm{mL}$) of $1\,\mathrm{mol\,L^{-1}}$ HCl or NaOH is added to $50\,\mathrm{mL}$ of pure water, the pH changes from 7 to 3 or 11; when the same drop is added to $50\,\mathrm{mL}$ of a solution containing $0.10\,\mathrm{mol\,L^{-1}}$ HAc and $0.10\,\mathrm{mol\,L^{-1}}$ NaAc, the pH changes only from 4.76 to 4.75 or 4.77.

**Definition 9.5.1** A solution that resists changes in pH on the addition of small amounts of strong acid or strong base, or on moderate dilution, is called a **buffer solution**, and this property is called buffer action.

A buffer solution generally consists of a conjugate acid–base pair, both at fairly high concentration, such as HAc–NaAc, $\ce{NH3}$–$\ce{NH4Cl}$, $\ce{NaH2PO4}$–$\ce{Na2HPO4}$, and $\ce{H2CO3}$–$\ce{NaHCO3}$. For the HAc–$\ce{Ac-}$ pair, from

$$
[\ce{H+}] = K_{\mathrm{a}}\frac{[\ce{HAc}]}{[\ce{Ac-}]},
$$
$[\ce{H+}]$ is determined by the ratio of the two concentrations. The large amount of $\ce{Ac-}$ in the solution is the acid-resisting component: added $\ce{H+}$ combines with it to form HAc, so $[\ce{HAc}]$ rises slightly and $[\ce{Ac-}]$ falls slightly, and the ratio changes very little. The large amount of HAc is the base-resisting component: added $\ce{OH-}$ is neutralized by HAc. Because both concentrations are much larger than those of the added acid or base, the ratio, and hence the pH, hardly changes. On dilution the ratio is unchanged, and so the pH also remains essentially constant.

### 9.5.2. The pH of a Buffer Solution

Let the concentration of the weak acid HA be $c_{\mathrm{a}}$ and that of its conjugate base $\ce{A-}$ be $c_{\mathrm{b}}$. By the common-ion effect, the dissociation of HA and the hydrolysis of $\ce{A-}$ suppress each other, and when $c_{\mathrm{a}}$ and $c_{\mathrm{b}}$ are both much larger than $[\ce{H+}]$ and $[\ce{OH-}]$, $[\ce{HA}] \approx c_{\mathrm{a}}$ and $[\ce{A-}] \approx c_{\mathrm{b}}$.

**Theorem 9.5.1 (Henderson–Hasselbalch Equation)** For a buffer solution composed of a weak acid HA (concentration $c_{\mathrm{a}}$) and its conjugate base $\ce{A-}$ (concentration $c_{\mathrm{b}}$), when $c_{\mathrm{a}}, c_{\mathrm{b}} \gg [\ce{H+}], [\ce{OH-}]$,

$$
\mathrm{pH} = \mathrm{p}K_{\mathrm{a}} + \lg\frac{c_{\mathrm{b}}}{c_{\mathrm{a}}}. \tag{9.5}
$$

**Proof** Taking the negative logarithm of $K_{\mathrm{a}} = [\ce{H+}][\ce{A-}]/[\ce{HA}]$ gives $\mathrm{pH} = \mathrm{p}K_{\mathrm{a}} + \lg([\ce{A-}]/[\ce{HA}])$; then substitute the approximation above. $\square$

A buffer composed of a weak base B and its conjugate acid $\ce{BH+}$ (such as $\ce{NH3}$–$\ce{NH4Cl}$) is treated in the same way: $\mathrm{pOH} = \mathrm{p}K_{\mathrm{b}} + \lg(c_{\mathrm{BH^+}}/c_{\mathrm{B}})$, or one can treat $\ce{BH+}$ directly as the acid and use Eq. (9.5) with $\mathrm{p}K_{\mathrm{a}}(\ce{NH4+}) = 9.25$; the two are equivalent. When $K_{\mathrm{a}}$ is too large ($\gtrsim 10^{-2}$) or the concentration too low, the approximation conditions fail and the exact equilibrium equations must be solved.

**Example 9.5.1** To $50.00\,\mathrm{mL}$ of a buffer solution containing $0.150\,\mathrm{mol\,L^{-1}}$ $\ce{NH3}$ and $0.200\,\mathrm{mol\,L^{-1}}$ $\ce{NH4Cl}$ is added $0.100\,\mathrm{mL}$ of $1.00\,\mathrm{mol\,L^{-1}}$ HCl. Calculate the pH before and after the addition.

**Solution** Before the addition: $\mathrm{pOH} = \mathrm{p}K_{\mathrm{b}} + \lg\frac{0.200}{0.150} = 4.74 + 0.12 = 4.87$, so $\mathrm{pH} = 9.13$.

The added $\ce{H+}$ amounts to $1.00 \times 10^{-4}\,\mathrm{mol}$; we may assume that it reacts completely with $\ce{NH3}$ to give $\ce{NH4+}$, after which equilibrium is reestablished with the new composition. $\ce{NH3}$ changes from $7.50 \times 10^{-3}$ to $7.40 \times 10^{-3}\,\mathrm{mol}$, and $\ce{NH4+}$ from $1.000 \times 10^{-2}$ to $1.010 \times 10^{-2}\,\mathrm{mol}$. Since both are in the same solution, the ratio of concentrations equals the ratio of amounts:

$$
\mathrm{pOH} = 4.74 + \lg\frac{1.010 \times 10^{-2}}{7.40 \times 10^{-3}} = 4.88, \qquad \mathrm{pH} = 9.12.
$$
The pH drops by only 0.01. The same amount of HCl added to $50\,\mathrm{mL}$ of pure water would lower the pH from 7.00 to 2.70.

### 9.5.3. Buffer Capacity and Buffer Range

The ability of a buffer solution to resist acids and bases is limited.

**Definition 9.5.2** The amount of strong base (or strong acid) that must be added to $1\,\mathrm{L}$ of a buffer solution to change its pH by one unit is called the **buffer capacity**: $\beta = \frac{\mathrm{d}c_{\mathrm{B}}}{\mathrm{d}\,\mathrm{pH}} = -\frac{\mathrm{d}c_{\mathrm{A}}}{\mathrm{d}\,\mathrm{pH}}$, where $c_{\mathrm{B}}$ and $c_{\mathrm{A}}$ are the concentrations of added strong base and strong acid.

For an HA–$\ce{A-}$ system of total concentration $c = [\ce{HA}] + [\ce{A-}]$ to which strong base NaOH (concentration $c_{\mathrm{B}}$) is added, the charge balance $c_{\mathrm{B}} + [\ce{H+}] = [\ce{A-}] + [\ce{OH-}]$ gives

$$
c_{\mathrm{B}} = \frac{cK_{\mathrm{a}}}{K_{\mathrm{a}} + [\ce{H+}]} + \frac{K_{\mathrm{w}}}{[\ce{H+}]} - [\ce{H+}].
$$
Writing $h = [\ce{H+}]$, with $\mathrm{d}\,\mathrm{pH} = -\frac{\mathrm{d}h}{h\ln 10}$, differentiation with respect to $h$ gives

$$
\beta = \ln 10\left(h + \frac{K_{\mathrm{w}}}{h} + \frac{cK_{\mathrm{a}}h}{(K_{\mathrm{a}} + h)^2}\right).
$$
The first two terms are the contribution of water itself and matter only in strongly acidic or strongly basic regions; the third term is the contribution of the buffer pair, and reaches its maximum $\beta_{\max} = \frac{\ln 10}{4}c = 0.576c$ at $h = K_{\mathrm{a}}$ (that is, $\mathrm{pH} = \mathrm{p}K_{\mathrm{a}}$ and $c_{\mathrm{a}} = c_{\mathrm{b}}$). It follows that:

1. The buffer capacity is proportional to the total concentration of the buffer pair: the higher the total concentration, the stronger the buffering (commonly $0.05$–$0.5\,\mathrm{mol\,L^{-1}}$).
2. The buffer capacity is greatest at a concentration ratio $c_{\mathrm{b}}/c_{\mathrm{a}} = 1$; at a ratio of 10 or 1/10 ($\mathrm{pH} = \mathrm{p}K_{\mathrm{a}} \pm 1$), the third term falls to $\frac{4 \times 10}{11^2} = 33\%$ of its maximum. The effective buffer range is therefore $\mathrm{pH} = \mathrm{p}K_{\mathrm{a}} \pm 1$.

![Buffer capacity of the HAc–Ac⁻ system (total concentrations 0.10 and 0.05 mol/L) as a function of pH: the maximum, about 0.576c, is at pH = pKa, and the effective range is pKa ± 1; the rise at both ends comes from water itself (strong acids and bases also have a "buffering action")](./plots/buffer-capacity.py)

### 9.5.4. Choosing a Buffer and Biological Buffer Systems

To prepare a buffer of a given pH, choose a weak acid whose $\mathrm{p}K_{\mathrm{a}}$ is as close as possible to the desired pH, and then adjust the concentration ratio using Eq. (9.5); the buffer substances should also not react with other components of the system. Commonly used buffer systems are:

| Weak acid | Conjugate base | $\mathrm{p}K_{\mathrm{a}}$ | Buffer range (pH) |
|---|---|---|---|
| Phthalic acid | Potassium hydrogen phthalate | 2.94 | 1.9–3.9 |
| HAc | NaAc | 4.76 | 3.8–5.8 |
| $\ce{NaH2PO4}$ | $\ce{Na2HPO4}$ | 7.21 | 6.2–8.2 |
| $\ce{NH4Cl}$ | $\ce{NH3}$ | 9.25 | 8.3–10.3 |
| $\ce{Na2HPO4}$ | $\ce{Na3PO4}$ | 12.32 | 11.3–13.3 |

Biochemical experiments also frequently use organic buffers such as Tris (tris(hydroxymethyl)aminomethane, $\mathrm{p}K_{\mathrm{a}} = 8.07$) and HEPES ($\mathrm{p}K_{\mathrm{a}} \approx 7.5$), which coordinate metal ions only weakly and do not readily form precipitates as phosphates do.

**Example 9.5.2** The pH of human blood is maintained at $7.35$–$7.45$, and the main buffer system is $\ce{CO2(aq)}$–$\ce{HCO3-}$. At $37\,^\circ\mathrm{C}$ the apparent $\mathrm{p}K_{\mathrm{a}}$, which combines dissolved $\ce{CO2}$ with a small amount of $\ce{H2CO3}$, is 6.1. In arterial blood, $[\ce{HCO3-}] = 24\,\mathrm{mmol\,L^{-1}}$, the partial pressure of $\ce{CO2}$ is $5.3\,\mathrm{kPa}$, and the solubility of $\ce{CO2}$ in plasma is $0.23\,\mathrm{mmol\,L^{-1}\,kPa^{-1}}$. Find the pH of the blood.

**Solution** $[\ce{CO2(aq)}] = 0.23 \times 5.3 = 1.2\,\mathrm{mmol\,L^{-1}}$, and by Eq. (9.5),

$$
\mathrm{pH} = 6.1 + \lg\frac{24}{1.2} = 6.1 + 1.30 = 7.40.
$$
The concentration ratio is 20, far from the ratio of 1 at which the buffer capacity is greatest, so by the analysis of 9.5.3 this buffer pair is not very efficient. It is effective because it is an open system: acids produced by metabolism increase $\ce{CO2}$, and the excess $\ce{CO2}$ is exhaled through the lungs, while the concentration of $\ce{HCO3-}$ is regulated by the kidneys. The pH is therefore maintained jointly by respiration and kidney function, and hyperventilation or hypoventilation leads to respiratory alkalosis or acidosis. Inside cells, the main buffer systems are phosphate ($\mathrm{p}K_{\mathrm{a2}} = 7.21$; in the distribution diagram of 9.3.6, $\ce{H2PO4-}$ and $\ce{HPO4^2-}$ each account for a substantial fraction near pH 7.4) and proteins. (See [Biochemistry](/7.1) and [Animal Physiology](/7.15).)

## 9.6. Introduction to Acid–Base Titration

### 9.6.1. Basic Concepts of Titrimetric Analysis

**Definition 9.6.1** The method in which a reagent solution of accurately known concentration (a **standard solution**) is added dropwise to a solution of the substance to be determined until the two have reacted exactly in the stoichiometric ratio, and the content of the substance is calculated from the volume and concentration of the standard solution consumed, is called **titration** (titrimetric analysis).

By reaction type, titrations are classified as acid–base, complexometric, redox, and precipitation titrations.

**Definition 9.6.2** The point at which titrant and analyte have reacted exactly completely according to the stoichiometry of the reaction equation is called the **stoichiometric point**; the point at which the titration is stopped in practice on the basis of the sudden color change of an indicator is called the **end point**; the error caused by the difference between the end point and the stoichiometric point is called the **titration error** (end-point error).

A reaction used in titrimetric analysis must satisfy the following: it proceeds quantitatively according to a definite equation, with a completeness above 99.9%; it is fast, or can be speeded up simply by heating or a catalyst; there is a simple and reliable way of determining the end point (such as an indicator); and interference from coexisting substances can be eliminated.

There are two ways to prepare a standard solution.

**Definition 9.6.3** A substance that can be used directly to prepare a standard solution or to standardize the concentration of a solution is called a **primary standard**. It must be of high purity (above 99.9%); its composition must correspond exactly to its chemical formula (including water of crystallization); it must be stable, neither decomposing, absorbing moisture, efflorescing, nor absorbing $\ce{CO2}$; and it should preferably have a large molar mass, to reduce the relative error of weighing.

**Definition 9.6.4** The operation in which a solution of approximate concentration is prepared first and its accurate concentration is then determined by titration against a primary standard or another standard solution is called **standardization**.

- Direct method: a primary standard is weighed accurately, dissolved, and made up to volume in a volumetric flask, and the concentration is calculated directly from the mass and volume.
- Indirect method (standardization): reagents that do not meet the requirements of a primary standard are prepared roughly and then standardized. NaOH readily absorbs moisture and $\ce{CO2}$, and is standardized against the primary standard potassium hydrogen phthalate ($\ce{KHC8H4O4}$); concentrated hydrochloric acid is volatile, and HCl solutions are standardized against anhydrous $\ce{Na2CO3}$ or borax ($\ce{Na2B4O7*10H2O}$). In redox titration, $\ce{Na2S2O3}$ solutions are standardized against $\ce{KIO3}$ or $\ce{K2Cr2O7}$ ([6.1.12](/6.1.12)).

### 9.6.2. Titration Curves and the Titration Jump

**Definition 9.6.5** The curve obtained by plotting the pH of the solution (ordinate) against the volume of titrant added (or the fraction titrated) (abscissa) is called the acid–base **titration curve**.

**Definition 9.6.6** The sharp change in the pH of the solution within $\pm 0.1\%$ (relative error) of the stoichiometric point is called the **titration jump**, and the pH interval over which it occurs is called the jump range.

**Example 9.6.1** $20.00\,\mathrm{mL}$ of $0.1000\,\mathrm{mol\,L^{-1}}$ HCl is titrated with $0.1000\,\mathrm{mol\,L^{-1}}$ NaOH. Find the range of the titration jump. What if both concentrations are $0.01000\,\mathrm{mol\,L^{-1}}$?

**Solution** At 0.1% before the stoichiometric point, $19.98\,\mathrm{mL}$ of NaOH has been added, $0.02\,\mathrm{mL} \times 0.1000\,\mathrm{mol\,L^{-1}}$ of HCl remains, and the total volume is $39.98\,\mathrm{mL}$, so

$$
[\ce{H+}] = \frac{0.02 \times 0.1000}{39.98} = 5.0 \times 10^{-5}, \qquad \mathrm{pH} = 4.30.
$$
At the stoichiometric point, pH = 7.00. At 0.1% past it, $20.02\,\mathrm{mL}$ has been added, the excess NaOH gives $[\ce{OH-}] = 5.0 \times 10^{-5}$, and $\mathrm{pH} = 9.70$. The jump range is 4.30–9.70: with only about half a drop ($0.04\,\mathrm{mL}$) more titrant, the pH changes by 5.4 units. At a concentration of $0.01000\,\mathrm{mol\,L^{-1}}$, $[\ce{H+}]$ and $[\ce{OH-}]$ before and after the stoichiometric point are both reduced to 1/10, and the jump range is 5.30–8.70, narrowed by 2 pH units.

The significance of the jump is that if an indicator changes color within the jump range, the end point differs from the stoichiometric point by no more than 0.1%. This gives the principle for choosing an indicator: the transition range of the indicator should lie wholly or partly within the jump range. For a $0.1\,\mathrm{mol\,L^{-1}}$ strong acid–strong base titration, methyl red and phenolphthalein can be used (methyl orange also, with somewhat larger error); at $0.01\,\mathrm{mol\,L^{-1}}$ methyl orange is no longer suitable.

The whole titration curve can be calculated point by point from the charge balance. When NaOH (concentration $c$, volume added $V$) is used to titrate HCl (concentration $c$, volume $V_0$), $[\ce{Na+}] + [\ce{H+}] = [\ce{Cl-}] + [\ce{OH-}]$, that is,

$$
f(h) = h - \frac{K_{\mathrm{w}}}{h} + \frac{c(V - V_0)}{V + V_0} = 0.
$$
$f$ is a monotonically increasing function of $h$ with a unique root in $(0, 1)$, which can be found by the **bisection method** ([3.5.4](/3.5.4)) or Brent's method (`scipy.optimize.brentq`, [4.4.4](/4.4.4#sec-4.2.2)). When NaOH is used to titrate a weak acid HA, the charge balance becomes $[\ce{Na+}] + [\ce{H+}] = [\ce{A-}] + [\ce{OH-}]$ with $[\ce{A-}] = c_{\mathrm{HA}}\,\delta(\ce{A-})$ (9.3.6), and the method is the same. Because $h$ spans more than ten orders of magnitude, solving for pH rather than $h$ is numerically more stable.

![Left: titration curves of HCl by 0.1000 and 0.01000 mol/L NaOH at equal concentrations, with colored bands at left showing the transition ranges of three indicators; right: comparison of the titration of HAc and HCl by 0.1000 mol/L NaOH](./plots/titration-curves.py)

Titrating a weak acid differs from titrating a strong acid in three ways (right panel). The starting pH is higher (2.88 for HAc). Before the stoichiometric point the solution is an HAc–$\ce{Ac-}$ buffer and the curve is flat, and at half-titration $\mathrm{pH} = \mathrm{p}K_{\mathrm{a}}$ (one method of measuring $\mathrm{p}K_{\mathrm{a}}$). At the stoichiometric point the solution is $0.05000\,\mathrm{mol\,L^{-1}}$ NaAc and is basic ($\mathrm{pH} = 8.73$), and the jump range narrows to 7.76–9.70, so only phenolphthalein, which changes color in the basic region, can be used. The weaker the acid and the more dilute the solution, the smaller the jump; in general $cK_{\mathrm{a}} \ge 10^{-8}$ is required for an accurate titration. The stepwise titration of polyprotic acids, the calculation of end-point errors, and the theory of indicator selection are found in [Analytical Chemistry](/6.4).

## 9.7. Complexation Equilibria

### 9.7.1. Stability Constants

Adding excess aqueous ammonia to a $\ce{CuSO4}$ solution produces the deep-blue $\ce{[Cu(NH3)4]^2+}$ ([6.1.5](/6.1.5)). Adding a little NaOH to this solution does not precipitate $\ce{Cu(OH)2}$, yet adding $\ce{Na2S}$ gives a black precipitate of CuS: the solution therefore still contains a little free $\ce{Cu^2+}$, and the formation and dissociation of the complex ion are in equilibrium.

**Definition 9.7.1 (Complexation Equilibrium)** The equilibrium in solution between the reaction in which a central ion and ligands form a complex ion and the reaction in which the complex ion dissociates is called the **complexation equilibrium**.

**Definition 9.7.2** The standard equilibrium constant of the reaction $\mathrm{M} + n\mathrm{L} \ce{<=>} \mathrm{ML}_n$ in which a central ion M and ligands L form a complex ion $\ce{ML_n}$,

$$
\beta_n = \frac{[\mathrm{ML}_n]}{[\mathrm{M}][\mathrm{L}]^n}
$$
is called the **stability constant** (formation constant, overall stability constant) of the complex ion; its reciprocal $1/\beta_n$, which is the equilibrium constant of the dissociation reaction $\mathrm{ML}_n \ce{<=>} \mathrm{M} + n\mathrm{L}$, is called the **instability constant** (dissociation constant).

For example, for $\ce{Cu^2+ + 4NH3 <=> [Cu(NH3)4]^2+}$, $\beta_4 = \frac{[\ce{[Cu(NH3)4]^2+}]}{[\ce{Cu^2+}][\ce{NH3}]^4} = 2.1 \times 10^{13}$ ($\lg\beta_4 = 13.32$). (Chinese textbooks often write $\beta_n$ as $K_{\mathrm{f}}$ or as a stability constant $K_{\mathrm{stab}}$ and the instability constant as $K_{\mathrm{d}}$ or $K_{\mathrm{unstab}}$; this wiki follows IUPAC and writes $\beta_n$.) For complex ions of the same type (the same number of ligands), the larger $\beta_n$ is, the more stable the complex:

| Complex ion | $\lg\beta_n$ | Complex ion | $\lg\beta_n$ |
|---|---|---|---|
| $\ce{[Ag(NH3)2]+}$ | 7.22 | $\ce{[Cu(NH3)4]^2+}$ | 13.32 |
| $\ce{[Ag(S2O3)2]^3-}$ | 13.46 | $\ce{[Zn(NH3)4]^2+}$ | 9.46 |
| $\ce{[Ag(CN)2]-}$ | 21.1 | $\ce{[Cd(NH3)4]^2+}$ | 7.12 |

The order of stability of the three complex ions of $\ce{Ag+}$, $\ce{NH3} < \ce{S2O3^2-} < \ce{CN-}$, is exactly "soft likes soft" (9.1.4): $\ce{CN-}$ and $\ce{S2O3^2-}$ (S-bound) are softer than $\ce{NH3}$.

Complex ions form and dissociate stepwise.

**Definition 9.7.3** The equilibrium constant of each step in which a complex ion adds ligands one at a time, $\mathrm{ML}_{k-1} + \mathrm{L} \ce{<=>} \mathrm{ML}_k$,

$$
K_k = \frac{[\mathrm{ML}_k]}{[\mathrm{ML}_{k-1}][\mathrm{L}]}, \qquad k = 1, 2, \dots, n
$$
is called the **stepwise stability constant**.

By the **rule of multiple equilibria**, the overall stability constant is the product of the stepwise stability constants:

$$
\beta_k = K_1K_2\cdots K_k, \qquad \lg\beta_k = \sum_{j=1}^{k}\lg K_j.
$$
The stepwise instability constants are the reciprocals of the stepwise stability constants, in reverse order: the constant of the first dissociation step $\ce{[Cu(NH3)4]^2+ <=> [Cu(NH3)3]^2+ + NH3}$ is $1/K_4$. For the $\ce{Cu^2+}$–$\ce{NH3}$ system, $\lg K_1, \dots, \lg K_4 = 4.31, 3.67, 3.04, 2.30$: stepwise stability constants generally decrease in turn, because of statistical factors (the more ligands already bound, the fewer water molecules remain to be replaced and the more ligands are available to leave) and because of the electrostatic and steric repulsion of the ligands already bound.

The distribution of species is entirely analogous to the distribution fractions of polyprotic acids (9.3.6), with $[\ce{H+}]$ replaced by the free ligand concentration $[\mathrm{L}]$: the fraction of $\mathrm{ML}_k$ is $\beta_k[\mathrm{L}]^k\big/\sum_{j=0}^{n}\beta_j[\mathrm{L}]^j$ ($\beta_0 = 1$).

![Fractions of the Cu(II)–NH₃ complex ions as functions of the free ammonia concentration (the abscissa is −lg[NH₃]; ammonia concentration increases to the right; dashed lines mark lg K₁ … lg K₄): the stepwise constants differ little, so several intermediate complexes coexist over a wide range, and almost all the copper is present as [Cu(NH₃)₄]²⁺ only in large excess of ammonia](./plots/copper-ammine-distribution.py)

### 9.7.2. Applications of Stability Constants

Stability constants can first be used to decide the direction of conversion between complex ions.

**Example 9.7.1** Determine the direction of the reaction $\ce{[Ag(NH3)2]+ + 2CN- <=> [Ag(CN)2]- + 2NH3}$.

**Solution** By the rule of multiple equilibria (multiplying numerator and denominator by $[\ce{Ag+}]$),

$$
K^\circ = \frac{[\ce{[Ag(CN)2]-}][\ce{NH3}]^2}{[\ce{[Ag(NH3)2]+}][\ce{CN-}]^2} = \frac{\beta_2(\ce{[Ag(CN)2]-})}{\beta_2(\ce{[Ag(NH3)2]+})} = \frac{1.3 \times 10^{21}}{1.7 \times 10^{7}} = 7.6 \times 10^{13}.
$$
$K^\circ$ is very large, and the reaction proceeds very completely to the right: a complex ion always converts into the more stable complex ion.

Stability constants can also be used to calculate the concentration of free metal ion in solution.

**Example 9.7.2** To $1\,\mathrm{mL}$ of $0.040\,\mathrm{mol\,L^{-1}}$ $\ce{AgNO3}$ solution is added $1\,\mathrm{mL}$ of $2.0\,\mathrm{mol\,L^{-1}}$ aqueous ammonia. Calculate $[\ce{Ag+}]$ and $[\ce{[Ag(NH3)]+}]$ at equilibrium. Take $\beta_2 = 1.7 \times 10^{7}$ and $K_1 = 2.0 \times 10^{3}$.

**Solution** After mixing, $c(\ce{Ag+}) = 0.020$ and $c(\ce{NH3}) = 1.0\,\mathrm{mol\,L^{-1}}$. Since $\beta_2$ is very large and ammonia is in large excess, we may first assume that all the $\ce{Ag+}$ is converted to $\ce{[Ag(NH3)2]+}$ (0.020), which consumes 0.040 of $\ce{NH3}$ and leaves 0.96; then $[\ce{Ag+}] = x$ is found from the dissociation of a small amount of the complex ion:

| | $\ce{Ag+}$ | $\ce{NH3}$ | $\ce{[Ag(NH3)2]+}$ |
|---|---|---|---|
| After complete reaction | 0 | 0.96 | 0.020 |
| Equilibrium | $x$ | $0.96 + 2x$ | $0.020 - x$ |

$$
\beta_2 = \frac{0.020 - x}{x(0.96 + 2x)^2} \approx \frac{0.020}{x \times 0.96^2} = 1.7 \times 10^{7}, \qquad x = 1.3 \times 10^{-9}\,\mathrm{mol\,L^{-1}}.
$$
$[\ce{[Ag(NH3)]+}] = K_1[\ce{Ag+}][\ce{NH3}] = 2.0 \times 10^{3} \times 1.3 \times 10^{-9} \times 0.96 = 2.5 \times 10^{-6}\,\mathrm{mol\,L^{-1}}$, only 0.013% of the total silver, so the assumption that everything forms $\ce{[Ag(NH3)2]+}$ holds. The concentration of free $\ce{Ag+}$ has been lowered by seven orders of magnitude; this is why complexation can dissolve precipitates and change electrode potentials.

Finally, complexation equilibria often coexist with other equilibria, and the equilibrium constant of the overall reaction is obtained by combining them by the rule of multiple equilibria:

- With acid–base equilibria: ligands are mostly weak bases ($\ce{NH3}$, $\ce{CN-}$, $\ce{F-}$, EDTA); adding acid protonates the ligand, lowering the free ligand concentration and causing the complex ion to dissociate. When acid is added to a $\ce{[Cu(NH3)4]^2+}$ solution, the deep-blue color fades because $\ce{NH3 + H+ -> NH4+}$ removes the ligand. Conversely, hydrolysis of the metal ion also competes with complexation. The quantitative treatment of such side reactions (side-reaction coefficients, conditional stability constants) is found in [Analytical Chemistry](/6.4).
- With precipitation equilibria: complexation dissolves sparingly soluble salts (for example $\ce{AgCl + 2NH3 <=> [Ag(NH3)2]+ + Cl-}$, $K = K_{\mathrm{sp}}\beta_2$), and a precipitant can in turn destroy a complex ion (CuS forms when $\ce{Na2S}$ is added to $\ce{[Cu(NH3)4]^2+}$); see [6.1.10](/6.1.10).
- With redox equilibria: complexation lowers the concentration of the metal ion and thereby changes the electrode potential of the couple; for example, $\ce{Au}$ can be oxidized and dissolved by $\ce{O2}$ in the presence of $\ce{CN-}$; see [6.1.11](/6.1.11).

## Questions

1. In liquid ammonia, is HAc a strong or a weak acid? In glacial acetic acid, is $\ce{NH3}$ a strong or a weak base?
   Answer: Liquid ammonia is more basic than water, and HAc transfers its proton completely to $\ce{NH3}$ there, so it is a strong acid (liquid ammonia is a leveling solvent). Glacial acetic acid is more acidic than water, and $\ce{NH3}$ accepts a proton completely in it, so it is a strong base.
2. Is the pH of a $10^{-8}\,\mathrm{mol\,L^{-1}}$ HCl solution equal to 8?
   Answer: No. The dissociation of water cannot be neglected here. The charge balance $[\ce{H+}] = 10^{-8} + K_{\mathrm{w}}/[\ce{H+}]$ gives $[\ce{H+}] = 1.05 \times 10^{-7}$ and $\mathrm{pH} = 6.98$: however dilute an acid solution is, it remains acidic.
3. Why are hydrochloric acid and tin granules added when a $\ce{SnCl2}$ solution is prepared?
   Answer: The hydrochloric acid suppresses hydrolysis ($\ce{SnCl2 + H2O <=> Sn(OH)Cl v + HCl}$); the tin reduces any $\ce{Sn^4+}$ formed by air oxidation back to $\ce{Sn^2+}$ ([6.1.11](/6.1.11)).
4. Does the pH of an HAc–NaAc buffer change when it is diluted tenfold with water? Does the buffer capacity change?
   Answer: The concentration ratio is unchanged, so by Eq. (9.5) the pH is essentially unchanged (it changes only when the solution is so dilute that the approximation fails); the buffer capacity is proportional to the total concentration and falls to about 1/10.

## Summary

| Topic | Key points |
|---|---|
| Acid–base theories | Arrhenius theory: $\ce{H+}$ / $\ce{OH-}$ released in water; Brønsted–Lowry theory: proton donor / acceptor, conjugate acid–base pairs, acid–base reactions are proton transfers, strength depends on the solvent (leveling and differentiating effects); Lewis theory: electron-pair acceptor / donor, reaction forms a coordinate bond |
| Hard and soft acids and bases | Classified by polarizability; hard likes hard, soft likes soft |
| Water and pH | $K_{\mathrm{w}} = [\ce{H+}][\ce{OH-}] = 1.0\times10^{-14}$ (25 °C, increases with temperature); $\mathrm{pH} = -\lg a_{\ce{H+}}$; indicator transition range about $\mathrm{p}K_{\mathrm{a}} \pm 1$ |
| Weak acids and bases | $K_{\mathrm{a}}K_{\mathrm{b}} = K_{\mathrm{w}}$; $[\ce{H+}] \approx \sqrt{K_{\mathrm{a}}c}$ ($c/K_{\mathrm{a}} \ge 400$, error about $\alpha/2$; $K_{\mathrm{a}}c \ge 20K_{\mathrm{w}}$); dilution law $\alpha \approx \sqrt{K_{\mathrm{a}}/c}$; common-ion effect; polyprotic acids treated as monoprotic, $[\ce{A^2-}] \approx K_{\mathrm{a2}}$ |
| Salt solutions | Hydrolysis is the dissociation of ionic acids and bases; amphiprotic substances $\mathrm{pH} \approx \frac{1}{2}(\mathrm{p}K_{\mathrm{a1}} + \mathrm{p}K_{\mathrm{a2}})$, the proton condition follows from charge balance and mass balance |
| Buffer solutions | $\mathrm{pH} = \mathrm{p}K_{\mathrm{a}} + \lg(c_{\mathrm{b}}/c_{\mathrm{a}})$; buffer capacity greatest at $c_{\mathrm{a}} = c_{\mathrm{b}}$ ($0.576c$), effective range $\mathrm{p}K_{\mathrm{a}} \pm 1$ |
| Acid–base titration | The sharp pH change within ±0.1% of the stoichiometric point is the titration jump (0.1 mol/L strong acid–strong base: 4.30–9.70); the indicator transition range should lie within the jump range |
| Complexation equilibria | Overall stability constant $\beta_n = K_1\cdots K_n$, instability constant $1/\beta_n$; complex ions convert toward the more stable one; competition with acid–base, precipitation, and redox equilibria |
