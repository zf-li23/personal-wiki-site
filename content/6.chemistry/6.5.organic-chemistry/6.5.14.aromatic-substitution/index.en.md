---
title: Electrophilic and Nucleophilic Aromatic Substitution
description: The addition–elimination mechanism of electrophilic aromatic substitution (σ complex, evidence from isotope effects, energy diagram); activation and deactivation by substituents, resonance analysis of the σ complex, partial rate factors and σ⁺; directing rules, polysubstituted benzenes and the design of synthetic routes (order of introduction, functional group interconversion, blocking groups); nitration, halogenation, sulfonation and desulfonation, Friedel–Crafts alkylation and acylation, formylation and chloromethylation; the addition–elimination mechanism of nucleophilic aromatic substitution, Meisenheimer complexes, the order of leaving groups and the synthesis of ofloxacin.
source_hash: 2d8d74d57b7d
---

The delocalized π electrons of an aromatic ring make it a nucleophile: it reacts with sufficiently strong electrophiles, but the outcome is not addition, as with alkenes, but replacement of one H on the ring, with the aromatic system retained ([6.5.13](/6.5.13#sec-13.1.3)). This type of reaction is called electrophilic aromatic substitution (SEAr), and it is the basic method for introducing functional groups into aromatic rings: nitro, halogen, sulfonic acid, alkyl and acyl groups are all introduced in this way and can be converted further into amines, phenols, carboxylic acids and so on ([6.5.15](/6.5.15), [6.5.24](/6.5.24#sec-24.4)). In this chapter we first treat the mechanism common to SEAr, then how substituents determine the rate and position of reaction and how to design syntheses of polysubstituted arenes accordingly, and then discuss each type of reaction in turn. The last section deals with the opposite situation: when the ring carries strongly electron-withdrawing groups, the aromatic ring can be attacked by nucleophiles, giving nucleophilic aromatic substitution (SNAr); another nucleophilic aromatic substitution proceeds through a benzyne intermediate and is treated in [6.5.15](/6.5.15). For the energy diagrams, the **Hammond postulate**, the **kinetic isotope effect** and the **Hammett equation** used here see [6.5.3](/6.5.3), for the electronic effects of substituents see [6.5.2](/6.5.2#sec-2.8), and for transition-metal-catalyzed arylation (**cross-coupling reactions**) see [6.5.29](/6.5.29#sec-29.4).

## 14.1. General Features of Electrophilic Aromatic Substitution

**Definition 14.1.1 (Electrophilic Aromatic Substitution)** The reaction in which an electrophile $\ce{E+}$ attacks an aromatic ring and replaces one H on the ring (which leaves as $\ce{H+}$) is called **electrophilic aromatic substitution** (SEAr): $\ce{ArH + E+ -> ArE + H+}$.

The five most important types of SEAr and their electrophiles:

| Reaction | Reagents | Electrophile | Product |
|---|---|---|---|
| Nitration (14.6) | Conc. $\ce{HNO3}$ + conc. $\ce{H2SO4}$ | $\ce{NO2+}$ (nitronium ion) | $\ce{ArNO2}$ |
| Halogenation (14.7) | $\ce{Cl2}$/$\ce{FeCl3}$, $\ce{Br2}$/$\ce{FeBr3}$ | $\ce{X2}$–Lewis acid complex ("$\ce{X+}$") | $\ce{ArCl}$, $\ce{ArBr}$ |
| Sulfonation (14.8) | Fuming sulfuric acid ($\ce{SO3}$ + $\ce{H2SO4}$) | $\ce{SO3}$ or $\ce{HSO3+}$ | $\ce{ArSO3H}$ |
| Friedel–Crafts alkylation (14.9) | $\ce{RCl}$/$\ce{AlCl3}$; alkene or alcohol/acid | $\ce{R+}$ or $\ce{R-Cl-AlCl3}$ complex | $\ce{ArR}$ |
| Friedel–Crafts acylation (14.9) | $\ce{RCOCl}$/$\ce{AlCl3}$ | $\ce{RC#O+}$ (acylium ion) | $\ce{ArCOR}$ |

The electrophile in these reactions must be sufficiently strong: the π electrons of benzene are stabilized by aromaticity, and benzene is a much weaker nucleophile than an alkene. $\ce{Br2}$ adds to cyclohexene rapidly at room temperature but reacts with benzene only with the help of a **Lewis acid** ($\ce{FeBr3}$). The general strategy of these reactions is therefore "activation of the electrophile by acid": a Brønsted acid ($\ce{H2SO4}$) or Lewis acid ($\ce{FeX3}$, $\ce{AlCl3}$) converts a neutral molecule into a cation or a highly polarized complex.

## 14.2. Mechanism

### 14.2.1. The Two-Step Addition–Elimination Mechanism

SEAr proceeds in two steps (taking nitration as the example):

1. Electrophilic attack: a pair of π electrons of the ring attacks $\ce{E+}$ to form a new C–E bond, giving a carbocation intermediate. The attacked carbon becomes sp³ and the aromaticity is temporarily destroyed; this step is endothermic and rate-determining.
2. Loss of a proton: a base ($\ce{H2O}$, $\ce{HSO4-}$, etc.) removes the H on the sp³ carbon, the electron pair of the C–H bond returns to the ring, and the aromatic system is restored. This step is fast and strongly exothermic.

![Mechanism of SEAr (nitration as the example). Top: the π electrons of benzene attack the nitronium ion (slow) to give the σ complex; the positive charge is distributed over the two ortho positions and the para position relative to the sp³ carbon, and three resonance structures can be written. Bottom: a base removes the proton from the sp³ carbon (fast), restoring the aromatic ring and giving nitrobenzene](./plots/sear-mechanism.py)

**Definition 14.2.1 (σ Complex)** The cyclohexadienyl cation intermediate formed in SEAr when the electrophile forms a σ bond to one carbon of the aromatic ring is called the **σ complex**, also called the arenium ion or Wheland intermediate (Wheland, 1942).

The positive charge of the σ complex is not localized: it is a pentadienyl cation spanning five sp² carbons, with the positive charge mainly on the two ortho positions and the para position relative to the sp³ carbon ([Eq. (2.2) of 6.5.2](/6.5.2#eq-2.2): in a chain of five atoms the nonbonding orbital has coefficients on atoms 1, 3 and 5). This is the key to understanding directing effects (14.3.3). The σ complex is not aromatic, but because of resonance delocalization it is much more stable than an ordinary secondary carbocation.

Why is the second step loss of a proton and not combination with a nucleophile (as in the electrophilic addition of alkenes)? The addition product would be a nonaromatic cyclohexadiene, higher in energy than the reactant; the product of loss of a proton regains the aromatic stabilization energy of about $150\,\mathrm{kJ\,mol^{-1}}$. The two endpoints differ so greatly that the σ complex almost always chooses loss of a proton.

![Energy diagram of SEAr (schematic). Left: the first transition state, leading to the σ complex, is the highest and is rate-determining; loss of a proton from the σ complex gives the substitution product (exothermic), whereas combination with a nucleophile would give a nonaromatic addition product of higher energy. Right: an electron-donating group (OCH₃, para attack) lowers the σ complex and the transition state leading to it, whereas an electron-withdrawing group (NO₂, meta attack) raises both](./plots/sear-energy.py)

### 14.2.2. Evidence for the Mechanism

Isotope effects. If cleavage of the C–H bond occurred in the rate-determining step, replacing C–H by C–D would lower the rate markedly (a primary **kinetic isotope effect**, $k_{\mathrm{H}}/k_{\mathrm{D}}$ about 2–8, [6.5.3](/6.5.3#sec-3.11.4)). Melander (1950) found that benzene and tritiated benzene, and benzene and $\ce{C6D6}$, are nitrated at the same rate ($k_{\mathrm{H}}/k_{\mathrm{D}} \approx 1$), and the same holds for bromination. This rules out a one-step mechanism in which C–E bond formation and C–H bond cleavage are simultaneous and shows that the C–H bond is broken in a fast step after the rate-determining step, consistent with the two-step mechanism. A few reactions show measurable isotope effects (such as sulfonation, and very hindered substrates), which indicates that in these reactions the rate at which the σ complex returns to starting material is comparable to the rate of loss of a proton, so the second step partly determines the rate.

Isolation of the intermediate. Olah and coworkers observed σ complexes in superacids at low temperature: mesitylene with fluoroethane and $\ce{BF3}$ at $-80\,^\circ\mathrm{C}$ gives 1-ethyl-2,4,6-trimethylbenzenium tetrafluoroborate, an orange solid that can be isolated and loses a proton on heating to give ethylmesitylene; the NMR spectrum of the benzenium ion $\ce{C6H7+}$ obtained by protonation of benzene in $\ce{HF}$–$\ce{SbF5}$ has also been measured. Olah received the 1994 Nobel Prize in Chemistry "for his contribution to carbocation chemistry".

The **Hammond postulate**. The step forming the σ complex is strongly endothermic, and its transition state resembles the σ complex ([Definition 3.10.1 of 6.5.3](/6.5.3#def-3.10.1)). Any factor that stabilizes the σ complex therefore stabilizes this transition state and speeds up the reaction, which lets us use the resonance structures of the σ complex to judge reaction rates and positions (14.3). Before the σ complex is formed, a weak π complex (charge-transfer complex) can also form between the electrophile and the π electron cloud of the ring, but it does not usually determine the rate or selectivity of the reaction.

## 14.3. Substituent Effects

### 14.3.1. Reaction Rate: Activation and Deactivation

A substituent already on the ring affects both the rate of SEAr and the position at which the new group enters. A substituent that makes the reaction faster than for benzene is an *activating group*, and one that makes it slower is a *deactivating group*.

| Substrate (nitration) | Relative rate (benzene = 1) | Product distribution: ortho / meta / para (%) |
|---|---|---|
| Anisole | about $10^4$ | Mainly ortho and para, very little meta |
| Toluene | about 25 | 58 / 5 / 37 |
| Benzene | 1 | — |
| Chlorobenzene | 0.03 | 30 / 1 / 69 |
| Ethyl benzoate | 0.004 | 28 / 68 / 4 |
| Nitrobenzene | about $10^{-7}$ | 6 / 93 / 1 |

(Relative rates are values of competition experiments in acetic anhydride or mixed acid, taken from the data of Ingold and coworkers; the product distribution varies slightly with conditions.)

The effect of a substituent comes from two kinds of electronic effects ([6.5.2](/6.5.2#sec-2.8)): the **inductive effect** acts through σ bonds, and the **conjugation effect** acts through the π system; the latter appears only when a lone pair, π bond or empty orbital of the substituent can conjugate with the ring, and it affects the ortho and para positions much more than the meta positions.

| Class | Substituents | Electronic effect | Orientation |
|---|---|---|---|
| Strongly activating | $\ce{-O-}$, $\ce{-NH2}$, $\ce{-NHR}$, $\ce{-NR2}$, $\ce{-OH}$, $\ce{-OR}$ | The $+$M effect of the lone pair is far greater than the $-$I effect | ortho, para |
| Moderately activating | $\ce{-NHCOR}$, $\ce{-OCOR}$ | The lone pair is simultaneously conjugated with the acyl group, so $+$M is weakened but still greater than $-$I | ortho, para |
| Weakly activating | Alkyl; $\ce{-Ph}$, $\ce{-CH=CH2}$ | Alkyl: **hyperconjugation** and weak $+$I; aryl and alkenyl: conjugation of the π system ($+$M) | ortho, para |
| Weakly deactivating | $\ce{-F}$, $\ce{-Cl}$, $\ce{-Br}$, $\ce{-I}$ | $-$I greater than $+$M | ortho, para |
| Moderately deactivating | $\ce{-CHO}$, $\ce{-COR}$, $\ce{-COOR}$, $\ce{-COOH}$, $\ce{-CONH2}$ | $-$M and $-$I | meta |
| Strongly deactivating | $\ce{-CN}$, $\ce{-SO3H}$, $\ce{-NO2}$ | Strong $-$M and $-$I | meta |
| Strongly deactivating | $\ce{-CF3}$, $\ce{-CCl3}$, $\ce{-NR3+}$ | Only strong $-$I ($\ce{-CF3}$ also has **negative hyperconjugation**) | meta |

The pattern can be summarized in two rules: all activating groups are ortho, para directors; apart from the halogens, all deactivating groups are meta directors. Groups with a lone pair on the atom attached directly to the ring ($\ce{-OR}$, $\ce{-NR2}$, halogens) are ortho, para directors; groups in which the atom attached to the ring carries a positive or partial positive charge (the carbon or nitrogen of $\ce{C=O}$, $\ce{C#N}$, $\ce{N+}$) are meta directors.

### 14.3.2. Directing Effects

**Definition 14.3.1 (Directing Effect)** The effect by which a substituent already on an aromatic ring determines the position (ortho, meta or para) at which a new group enters in SEAr is called the **directing effect**; substituents that direct the new group mainly to the ortho and para positions are called ortho, para directors, and those that direct it mainly to the meta position are called meta directors.

Statistically the meta product accounts for 2/5 (two ortho, two meta, one para), so "meta directing" does not mean that the meta position is faster than benzene but that the other positions are deactivated much more strongly. For a deactivating meta director, all three positions are slower than benzene, and the meta position is merely slowed less.

### 14.3.3. Resonance Analysis of the σ Complex

Using the Hammond postulate, comparing the stabilities of the σ complexes formed on attack at each position lets us decide the directing effect. The positive charge of the σ complex falls on the ortho and para positions relative to the sp³ carbon, so:

- on attack ortho or para to the existing substituent, one resonance structure places the positive charge on the carbon bearing the substituent (C1);
- on meta attack, no resonance structure places the positive charge on C1.

Everything then depends on the relationship between the positive charge on C1 and the substituent:

1. The substituent has a lone pair ($\ce{-OCH3}$, $\ce{-NR2}$): it can donate the lone pair to the adjacent positive charge, giving a fourth resonance structure (an onium ion) in which every atom satisfies the octet rule and which is the most important resonance structure. The σ complexes of ortho and para attack are therefore particularly stable, and the reaction is fast and mainly ortho and para.
2. The substituent is electron-withdrawing ($\ce{-NO2}$, $\ce{-C=O}$, $\ce{-CF3}$): the positive charge on C1 sits right next to an atom with a positive or partial positive charge, this resonance structure is very high in energy, and the σ complexes of ortho and para attack are strongly destabilized; meta attack avoids it and is relatively favorable.
3. Alkyl groups: the positive charge on C1 is on a tertiary carbon and is stabilized by the hyperconjugation and inductive effect of the alkyl group, so methyl is a weak ortho, para director.

![Resonance structures of the σ complex in bromination. First figure: para attack on anisole (top) has four resonance structures, one of which puts the positive charge on C1 and is further shared by the lone pair of oxygen (an onium ion, all atoms satisfying the octet rule); meta attack (bottom) has only three resonance structures, and the positive charge never falls on C1. Second figure: para attack on nitrobenzene (top) has one resonance structure in which the positive charge sits right next to the positively charged N, which is very unstable; meta attack (bottom) avoids this resonance structure](./plots/directing-resonance.py)

The halogens are the only exception: their electronegativity is large, and the $-$I effect makes the ring as a whole electron-poor, so they are deactivating groups; but the halogens also have lone pairs, and on ortho or para attack they can stabilize the σ complex through a halonium resonance structure (although overlap of the C 2p orbital with the Cl 3p or Br 4p orbital is poor, so this stabilization is weak), so they are still ortho, para directors. The rate is determined by the inductive effect and the orientation by the conjugation effect. Fluorobenzene is the most special case: the F 2p orbital is similar in size to the C 2p orbital, the $+$M effect is strongest, and the reactivity of fluorobenzene at the para position is even slightly higher than that of benzene (partial rate factor greater than 1).

![σ complexes for the other two kinds of ortho, para directors (para bromination). Top: one resonance structure of toluene puts the positive charge on C1, which bears the methyl group, giving a tertiary carbocation stabilized by hyperconjugation with the methyl group. Bottom: one resonance structure of chlorobenzene likewise puts the positive charge on C1, and a chlorine lone pair then shares it as a chloronium ion (all atoms with octets); this is why halogens direct ortho and para even though they deactivate the ring](./plots/directing-alkyl-halogen.py)

### 14.3.4. Partial Rate Factors and σ⁺

The reactivity of each position can be compared quantitatively through the partial rate factor.

**Definition 14.3.2 (Partial Rate Factor)** The ratio of the rate of reaction at one position of a substituted benzene $\ce{C6H5X}$ to the rate at one position of benzene is called the **partial rate factor** $f$ of that position:

$$
f_o = \frac{6k_{\mathrm{X}}}{2k_{\mathrm{H}}}x_o, \qquad f_m = \frac{6k_{\mathrm{X}}}{2k_{\mathrm{H}}}x_m, \qquad f_p = \frac{6k_{\mathrm{X}}}{k_{\mathrm{H}}}x_p,
$$
where $k_{\mathrm{X}}/k_{\mathrm{H}}$ is the rate of the substituted benzene relative to benzene, $x_o$, $x_m$ and $x_p$ are the fractions of ortho, meta and para isomers in the product, and 6, 2 and 1 are the numbers of the corresponding positions in benzene and in the substituted benzene.

Nitration of toluene: relative rate about 25 and product distribution 58 / 5 / 37 give $f_o \approx 44$, $f_m \approx 4$ and $f_p \approx 56$ (Ingold's measured values are 42, 2.5 and 58). Methyl activates the ortho and para positions about 50-fold and the meta position by only a few-fold.

Partial rate factors are related to the **Hammett equation** ([Definition 3.5.1 of 6.5.3](/6.5.3#def-3.5.1)). The transition state of SEAr carries a positive charge, and a para substituent can conjugate directly with the center of positive charge, so $\sigma_p^+$ should be used:

$$
\lg f_p = \rho\,\sigma_p^+ . \tag{14.1}
$$
For toluene: $\lg 58 = 1.76$ and $\sigma_p^+(\ce{CH3}) = -0.31$ give $\rho \approx -5.7$. The $\rho$ values of various SEAr reactions are all large negative numbers (about $-6$ for nitration, about $-12$ for uncatalyzed bromination), which shows that a large amount of positive charge accumulates on the ring in the rate-determining step, consistent with the σ complex mechanism. The larger $\lvert\rho\rvert$ is, the more sensitive the reaction to substituents and the higher its selectivity: the weaker (more "gentle") the electrophile, the later the transition state and the more it resembles the σ complex, and the better the positional selectivity, which is another manifestation of the Hammond postulate.

### 14.3.5. Steric Effects

The ortho/para ratio is also affected by steric hindrance. In the nitration of alkylbenzenes, the larger the alkyl group, the less ortho product:

| Substrate | ortho / meta / para (%) |
|---|---|
| Toluene | 58 / 5 / 37 |
| Ethylbenzene | 45 / 7 / 48 |
| Isopropylbenzene | 30 / 8 / 62 |
| tert-Butylbenzene | 16 / 11 / 73 |

The larger the electrophile, the less ortho product: Friedel–Crafts isopropylation or tert-butylation of toluene gives almost only the para product (with a little meta).

## 14.4. Directing Rules for Polysubstituted Benzenes

When the benzene ring already carries two or more substituents, the position of a new group is judged by the following empirical rules:

1. When the directing effects of the groups agree, the position they jointly point to is taken. For example, in 4-nitrotoluene $\ce{CH3}$ points to its ortho positions and $\ce{NO2}$ to its meta positions, and these are the same positions.
2. When they disagree, the group with the strongest activating effect decides. By directing power the groups fall roughly into three classes: $\ce{-NR2}$, $\ce{-OR}$, $\ce{-OH}$ (strongly activating) > alkyl, halogens > meta directors; when groups of the same class compete, mixtures result.
3. When two groups are meta to each other, the position between them is seldom substituted because of steric hindrance.
4. If the ortho position of a strongly activating group is already occupied by a large group, substitution shifts to its para position or its other ortho position.

```smiles
Cc1ccc(cc1)[N+](=O)[O-] 1
Oc1ccc(C)cc1 2
Nc1ccccc1C(=O)O 3
COc1ccccc1Br 4
Cc1ccccc1CC 5
O=C(O)c1cccc(c1)[N+](=O)[O-] 6
```

| No. | Compound | Main position of reaction | Reason |
|---|---|---|---|
| 1 | 4-Nitrotoluene | Ortho to methyl (meta to nitro) | The two agree |
| 2 | 4-Methylphenol | Ortho to OH | OH is stronger than $\ce{CH3}$ |
| 3 | 2-Aminobenzoic acid | Para (and ortho) to $\ce{NH2}$ | $\ce{NH2}$ decides |
| 4 | 2-Bromoanisole | Para to $\ce{OCH3}$ | $\ce{OCH3}$ decides, and one ortho position is occupied |
| 5 | 1-Ethyl-2-methylbenzene | Mixture | The two alkyl groups have similar directing power |
| 6 | 3-Nitrobenzoic acid | C5 (meta to both) | The two meta directors agree; the reaction is very slow |

## 14.5. Design of Synthetic Routes

In the synthesis of polysubstituted benzenes by SEAr, the order in which substituents are introduced determines their relative positions. The following points are considered in design:

1. Directing principle: the group introduced first determines the position of the group introduced later. 1-Chloro-2-nitrobenzene is made by first chlorinating and then nitrating (Cl is an ortho, para director) and separating the ortho and para isomers; if nitration came first, subsequent chlorination would give only the meta product.
2. Deactivating groups are introduced as late as possible: a strongly deactivated ring does not undergo Friedel–Crafts reactions, and nitration and halogenation also become slower. 1-Chloro-4-methylbenzene is obtained by chlorination of toluene (toluene is more reactive than chlorobenzene).
3. Functional group interconversions change the directing effect:
   - $\ce{-NO2}$ (meta) is reduced to $\ce{-NH2}$ (ortho, para) and then converted through the **diazonium salt** to $\ce{-OH}$, $\ce{-X}$, $\ce{-CN}$, or removed ([6.5.24](/6.5.24#sec-24.4.5));
   - $\ce{-COR}$ (meta) is reduced to $\ce{-CH2R}$ (ortho, para), see 14.9.3;
   - $\ce{-CH3}$ (ortho, para) is oxidized to $\ce{-COOH}$ (meta, [6.5.15](/6.5.15#sec-15.4.4)). For example, 2,4-dinitrobenzoic acid: toluene is nitrated twice to 2,4-dinitrotoluene, and the methyl group is then oxidized.
4. Blocking groups: reversible sulfonation (14.8) or Friedel–Crafts tert-butylation (14.9.2) is used to occupy the para position temporarily and is removed after the reaction, so that the ortho product is obtained.
5. Tuning the strength of activating groups: aniline and phenol are so reactive that bromination gives the tribromo compound, and they are also oxidized during nitration; acetylation of $\ce{-NH2}$ to $\ce{-NHCOCH3}$ (moderately activating and bulkier, giving mainly the para product) followed by hydrolytic removal of the acetyl group after reaction solves this ([6.5.23](/6.5.23#sec-23.6)).

For example, in the synthesis of 2-chlorotoluene from toluene: direct chlorination of toluene gives a mixture of ortho and para isomers; first sulfonation (mainly para), then chlorination (entering ortho to methyl, which is also meta to the sulfonic acid group), and finally removal of the sulfonic acid group by heating with dilute acid.

```smiles
Cc1ccccc1>>Cc1ccc(cc1)S(=O)(=O)O
Cc1ccc(cc1)S(=O)(=O)O>>Cc1ccc(cc1Cl)S(=O)(=O)O
Cc1ccc(cc1Cl)S(=O)(=O)O>>Cc1ccccc1Cl
```

## 14.6. Nitration

Benzene reacts with a mixture of concentrated nitric and sulfuric acids ("mixed acid", commonly in a volume ratio of about 1∶2) at $50$–$60\,^\circ\mathrm{C}$ to give nitrobenzene. The electrophile is the nitronium ion $\ce{NO2+}$: sulfuric acid protonates the OH of nitric acid, which loses water to give $\ce{NO2+}$.

$$
\ce{HNO3 + 2H2SO4 <=> NO2+ + H3O+ + 2HSO4-}
$$
Evidence for this equation: the freezing-point depression of nitric acid in pure sulfuric acid corresponds to 4 particles per $\ce{HNO3}$; the symmetric stretching vibration of $\ce{NO2+}$ appears in the Raman spectrum (about $1400\,\mathrm{cm^{-1}}$); and nitronium salts such as $\ce{NO2+BF4-}$ can be isolated and are strong reagents for the nitration of arenes.

![Generation of electrophiles. (1) Br₂ donates a lone pair to FeBr₃; in the complex formed the Br–Br bond is highly polarized, the aromatic ring attacks the terminal Br, and the Br–Br bond breaks heterolytically, FeBr₄⁻ leaving; (2) sulfuric acid protonates the OH of nitric acid, which loses water to give the nitronium ion; (3) the Cl of an acyl chloride coordinates to AlCl₃, and the C–Cl bond breaks to give a resonance-stabilized acylium ion; (4) the complex of 1-chloropropane with AlCl₃ undergoes a 1,2-hydride shift as it dissociates, giving a secondary carbocation, so that mainly isopropylbenzene is obtained](./plots/electrophiles.py)

The nitro group is a strongly deactivating group, so mononitration is easily controlled; dinitration requires fuming nitric acid and a higher temperature (about $95\,^\circ\mathrm{C}$, giving 1,3-dinitrobenzene), and trinitration is more difficult still. Toluene, activated by the methyl group, can be nitrated successively to 2,4,6-trinitrotoluene (TNT). The main use of nitration products is reduction to aromatic amines ([6.5.23](/6.5.23#sec-23.5.5), [6.5.24](/6.5.24#sec-24.7.4)), which is the industrial route to aniline.

## 14.7. Halogenation

Chlorination and bromination are catalyzed by Lewis acids such as $\ce{FeCl3}$, $\ce{FeBr3}$ and $\ce{AlCl3}$ and are carried out at room temperature or with gentle warming (in the laboratory iron powder is often added directly, and forms $\ce{FeX3}$ with the halogen). The Lewis acid coordinates to the halogen molecule and polarizes the X–X bond; the aromatic ring attacks the terminal halogen atom while the X–X bond breaks heterolytically (see (1) in the figure above); free $\ce{X+}$ is not formed.

$$
\ce{C6H6 + Br2 ->[FeBr3] C6H5Br + HBr}
$$

The halogens differ greatly:

- Fluorine is too reactive and reacts violently and uncontrollably with arenes; aryl fluorides are usually obtained by the **Balz–Schiemann reaction** of diazonium salts ([6.5.24](/6.5.24#sec-24.4.3)) or with electrophilic fluorinating reagents ([6.5.27](/6.5.27#sec-27.6.4), such as Selectfluor and $\ce{XeF2}$).
- Iodine is too unreactive, and the HI formed in the reaction is a strong reducing agent that reverses the reaction; an oxidant ($\ce{HNO3}$, $\ce{H2O2}$, $\ce{HIO3}$) must be added to oxidize the HI and generate a more strongly electrophilic iodine species, or ICl is used.

Reactive arenes such as phenol, aniline and anisole are halogenated in water or acetic acid without a catalyst and are difficult to stop at the monohalo stage ([6.5.15](/6.5.15#sec-15.8.1)).

Haloarenes are themselves important synthetic intermediates: they can be converted into **Grignard reagents** and **organolithium reagents** ([6.5.10](/6.5.10#sec-10.3)) and are substrates of Pd-catalyzed **cross-coupling reactions** ([6.5.29](/6.5.29#sec-29.4)). Electrophilic halogenation of aromatic rings also occurs in organisms: thyroid peroxidase uses $\ce{H2O2}$ to oxidize iodide to an electrophilic iodine species that iodinates tyrosine residues of thyroglobulin, giving precursors of the thyroid hormones.

## 14.8. Sulfonation and Desulfonation

Benzene reacts with fuming sulfuric acid (a solution of $\ce{SO3}$ in sulfuric acid) at room temperature to $40\,^\circ\mathrm{C}$, or with concentrated sulfuric acid on heating, to give benzenesulfonic acid. The electrophile is $\ce{SO3}$ (or protonated $\ce{HSO3+}$): the ring attacks the sulfur atom of $\ce{SO3}$ to give a σ complex bearing a sulfonate group (a zwitterion), which loses a proton to give the benzenesulfonate and is then protonated.

```smiles
c1ccccc1.O=S(=O)=O>>OS(=O)(=O)c1ccccc1
```

Sulfonation is reversible: when benzenesulfonic acid is heated with dilute sulfuric acid (or superheated steam is passed through, $100$–$175\,^\circ\mathrm{C}$), the σ complex forms at the protonated ipso position (the carbon bearing the sulfonic acid group), loses $\ce{SO3}$ and returns to benzene. A high concentration of $\ce{SO3}$ shifts the equilibrium toward sulfonation, and a large amount of water shifts it toward desulfonation. Reversibility makes the sulfonic acid group a useful blocking group (14.5) and also lets the position of sulfonation be under thermodynamic control (sulfonation of naphthalene, [6.5.15](/6.5.15#sec-15.6.2); for **thermodynamic control** see [6.5.3](/6.5.3#def-3.9.3)).

![Mechanism of sulfonation and desulfonation. Top: the π electrons of benzene attack the sulfur of SO₃ and an S=O π bond moves onto oxygen, giving a zwitterionic σ complex; a base (water or HSO₄⁻) removes the proton from the sp³ carbon to give the benzenesulfonate ion, which is protonated to benzenesulfonic acid. Bottom: desulfonation is the reverse process: in hot dilute acid the ring is protonated at the ipso carbon, and the C–S bond breaks to release SO₃ (taken up by water as sulfuric acid), returning benzene](./plots/sulfonation.py)

Applications of sulfonation:

- Sodium alkylbenzenesulfonates (such as sodium dodecylbenzenesulfonate) are among the synthetic detergents used in the largest quantities. The long alkyl chain is lipophilic and the sulfonate hydrophilic; such amphiphilic molecules are **surfactants** and aggregate in water into **micelles** ([6.3.19](/6.3.19)).
- Sodium arenesulfonates fused with NaOH give phenols ([6.5.15](/6.5.15#sec-15.9)); sulfonyl chlorides and amines give sulfonamides (sulfa drugs, [6.5.26](/6.5.26#sec-26.10.2)); p-toluenesulfonic acid (TsOH) is a commonly used strong organic acid.

## 14.9. The Friedel–Crafts Reaction

**Definition 14.9.1 (Friedel–Crafts Reaction)** An SEAr in which, under catalysis by a Lewis acid ($\ce{AlCl3}$, etc.) or a strong Brønsted acid, the aromatic ring is attacked by a carbocation or its equivalent to form a new C–C bond is called a **Friedel–Crafts reaction**; introduction of an alkyl group is called Friedel–Crafts alkylation, and introduction of an acyl group is called Friedel–Crafts acylation.

In 1877, Friedel and Crafts, working in Friedel's laboratory, tried to prepare amyl iodide from amyl chloride with iodine and aluminum and obtained a large amount of HCl and hydrocarbons; they found that aluminum chloride was the active agent and that benzene could be alkylated with alkyl halides.

### 14.9.1. Alkylation

An alkyl halide coordinates to $\ce{AlCl3}$; tertiary and secondary alkyl halides dissociate into carbocations, whereas primary alkyl halides react as polarized $\ce{R-Cl-AlCl3}$ complexes. Other reagents that can generate carbocations can also be used: alkenes with HF, $\ce{H2SO4}$, $\ce{H3PO4}$ or acidic zeolites (industrially, benzene and ethene give ethylbenzene, which is dehydrogenated to styrene; benzene and propene give isopropylbenzene, used for the production of phenol and acetone, [6.5.15](/6.5.15#sec-15.9)), alcohols with acid or $\ce{BF3}$, and oxirane with $\ce{AlCl3}$ (giving 2-phenylethanol).

```smiles
c1ccccc1.CC(C)(C)Cl>>CC(C)(C)c1ccccc1
c1ccccc1.C=C>>CCc1ccccc1
```

![Mechanism of Friedel–Crafts alkylation (tert-butyl chloride). First figure: a chlorine lone pair is donated to AlCl₃, and the C–Cl bond ionizes to give the tert-butyl cation and AlCl₄⁻. Second figure: the π electrons of benzene attack the carbocation (slow) to give the σ complex, and a chlorine of AlCl₄⁻ removes the proton (fast), giving tert-butylbenzene and HCl and regenerating AlCl₃. Third figure: the reversibility of alkylation (14.9.2): in strong acid the ring is protonated at the ipso carbon bearing the alkyl group, and the C–C bond breaks to release the tert-butyl cation](./plots/fc-alkylation.py)

Friedel–Crafts alkylation has four limitations that must be kept in mind in designing syntheses:

1. Carbocation rearrangement. The electrophilic species undergoes hydride or alkyl shifts to become a more stable **carbocation** ([6.5.8](/6.5.8#sec-8.3.3)). Benzene and 1-chloropropane give mainly isopropylbenzene, with propylbenzene as the minor product (see (4) in the figure above); 1-chlorobutane gives mainly sec-butylbenzene.
2. Polyalkylation. The alkyl group introduced activates the ring, and the product is more readily alkylated further than the starting material, so polyalkylbenzenes are often obtained; this can be suppressed by a large excess of the arene.
3. Deactivated rings do not react. A ring bearing a group more strongly deactivating than a halogen ($\ce{-NO2}$, $\ce{-COR}$, $\ce{-CN}$, $\ce{-SO3H}$, $\ce{-NR3+}$) does not react, and nitrobenzene can even be used as the solvent of Friedel–Crafts reactions. $\ce{-NH2}$, $\ce{-NHR}$ and $\ce{-NR2}$ combine with $\ce{AlCl3}$ to form positively charged complexes, which likewise deactivate the ring.
4. Aryl and vinyl halides cannot be used as alkylating agents: a halogen on an sp² carbon cannot dissociate to a carbocation.

### 14.9.2. Reversibility

Alkylation is reversible in strong acid: the σ complex can also be protonated at the ipso position bearing the alkyl group and lose a carbocation (most easily the tert-butyl cation). On prolonged reaction or at high temperature the product therefore isomerizes to the thermodynamically more stable isomer; xylenes treated for a long time with $\ce{AlCl3}$–HCl give mainly 1,3-dimethylbenzene, and polyalkylation can give 1,3,5-trialkylbenzenes. The tert-butyl group can serve as a removable blocking group: after introduction it occupies the para position, and after other reactions are complete it is "transferred" away with $\ce{AlCl3}$ in benzene or toluene.

### 14.9.3. Acylation

An acyl chloride or anhydride and $\ce{AlCl3}$ form the acylium ion $\ce{RC#O+}$, which is stabilized by resonance (the structure with the positive charge on carbon and the structure in which O satisfies the octet rule) and does not rearrange; attack by the aromatic ring gives an aryl ketone.

```smiles
c1ccccc1.CC(=O)Cl>>CC(=O)c1ccccc1
c1ccccc1.CC(=O)OC(C)=O>>CC(=O)c1ccccc1.CC(=O)O
```

Acylation has three advantages over alkylation: the acylium ion does not rearrange; the carbonyl group of the product aryl ketone deactivates the ring, so the reaction stops at monoacylation; and the carbonyl group of the product can be reduced to a methylene group (**Clemmensen reduction**, Zn(Hg)/HCl, [6.5.17](/6.5.17#sec-17.3.4); **Wolff–Kishner reduction**, $\ce{H2NNH2}$/KOH, [6.5.16](/6.5.16#sec-16.9.4)), which indirectly introduces a primary alkyl group without rearrangement. For example, propylbenzene cannot be obtained by alkylation with 1-chloropropane but is obtained by acylation with propanoyl chloride followed by reduction.

```smiles
c1ccccc1.CCC(=O)Cl>>CCC(=O)c1ccccc1
CCC(=O)c1ccccc1>>CCCc1ccccc1
```

The amount of $\ce{AlCl3}$: the aryl ketone formed is a Lewis base, and its carbonyl oxygen forms a stable 1∶1 complex with $\ce{AlCl3}$, which deactivates the catalyst, so at least 1 equivalent of $\ce{AlCl3}$ must be used (usually a slight excess), and the complex is decomposed with water after the reaction; with an anhydride the carboxylic acid formed also consumes 1 equivalent, so 2 or more equivalents are needed in all. Intramolecular acylation can close a ring: for example, 4-phenylbutanoic acid cyclizes in polyphosphoric acid to α-tetralone, a common method of synthesizing fused-ring compounds (the Haworth synthesis).

An exception: the pivaloyl cation formed from pivaloyl chloride and $\ce{AlCl3}$ loses CO to become the tert-butyl cation, and tert-butylbenzene is obtained mainly.

![Mechanism of Friedel–Crafts acylation. First figure: the π electrons of benzene attack the carbon of the acylium ion and one C–O π bond moves onto oxygen; AlCl₄⁻ removes the proton from the σ complex, giving acetophenone. Second figure: the carbonyl oxygen of the aryl ketone product donates a lone pair to AlCl₃, forming a stable 1∶1 complex that deactivates the catalyst, so at least one equivalent of AlCl₃ is needed, and water decomposes the complex at work-up. Third figure: the exception: the pivaloyl cation loses CO to give the more stable tert-butyl cation, so tert-butylbenzene is the main product](./plots/fc-acylation.py)

## 14.10. Formylation and Chloromethylation

Formyl chloride, HCOCl, is unstable, so Friedel–Crafts acylation cannot be used directly to introduce an aldehyde group.

- The *Gattermann–Koch reaction*: benzene or alkylbenzenes react with CO and HCl in the presence of $\ce{AlCl3}$ and a little CuCl to give aromatic aldehydes, which can be regarded as in situ generation of "HCOCl". The electrophile is the formylium ion $\ce{HC#O+}$ (or, in superacid, a further protonated superelectrophilic species, Shudo and coworkers, 1995); CuCl helps CO to be absorbed at atmospheric pressure. Toluene gives mainly 4-methylbenzaldehyde. The reaction is not suitable for phenols and phenol ethers.
- Electron-rich arenes (phenol ethers, aromatic amines, pyrroles, indoles) are formylated by the Vilsmeier–Haack reaction: the chloroiminium ion formed from DMF and $\ce{POCl3}$ is a weaker electrophile, and hydrolysis after the reaction gives the aldehyde ([6.5.25](/6.5.25#sec-25.4)).
- Chloromethylation (the Blanc reaction): arenes with formaldehyde and HCl in the presence of $\ce{ZnCl2}$ give benzyl chlorides $\ce{ArCH2Cl}$. Protonated formaldehyde ($\ce{H2C=OH+}$) attacks the ring to give a benzyl alcohol, which is converted to the benzyl chloride in HCl. The reaction forms the byproduct bis(chloromethyl) ether, a strong carcinogen, so the operation must be carried out in a fume hood. Benzyl chlorides are very useful intermediates and can be converted to $\ce{ArCH2OH}$, $\ce{ArCH2CN}$, $\ce{ArCHO}$ and so on.

```smiles
Cc1ccccc1.[C-]#[O+]>>Cc1ccc(C=O)cc1
c1ccccc1.C=O>>ClCc1ccccc1
```

![Generation of the electrophile in the Gattermann–Koch reaction: the lone pair on the carbon of CO takes the proton of HCl (AlCl₃ accepts the chloride as AlCl₄⁻), giving the formylium ion HC≡O⁺; it attacks toluene mainly at the para position, and loss of the proton gives 4-methylbenzaldehyde](./plots/gattermann-koch.py)

![Mechanism of chloromethylation (the Blanc reaction). Top: the π electrons of the ring attack the carbon of protonated formaldehyde and the C=O π bond moves onto oxygen; the σ complex loses a proton to give benzyl alcohol. Bottom: the hydroxy group of benzyl alcohol is protonated in HCl, water leaves to give the resonance-stabilized benzyl cation, and chloride combines with it to give benzyl chloride](./plots/chloromethylation.py)

## 14.11. Nucleophilic Aromatic Substitution

### 14.11.1. The Addition–Elimination Mechanism

Haloarenes do not undergo **SN1** or **SN2** reactions under ordinary conditions: the aryl cation is extremely unstable (the empty orbital is an sp² orbital that is not conjugated with the π system), and backside attack is blocked by the ring ([6.5.8](/6.5.8#sec-8.5.3)). Bromobenzene does not react on reflux with aqueous NaOH, and neither does vinyl chloride. But 1-bromo-4-nitrobenzene reacts with aqueous NaOH at $70\,^\circ\mathrm{C}$ to give 4-nitrophenol, whereas 1-bromo-3-nitrobenzene does not react under the same conditions.

**Definition 14.11.1 (Nucleophilic Aromatic Substitution)** The reaction in which a nucleophile attacks the carbon of an aromatic ring that bears a leaving group and replaces that leaving group is called **nucleophilic aromatic substitution** (SNAr). When the ring carries strongly electron-withdrawing groups, it proceeds by the addition–elimination mechanism.

1. Addition (rate-determining): the nucleophile attacks the carbon bearing the leaving group, which becomes sp³, giving a negatively charged cyclohexadienyl anion intermediate.
2. Elimination (fast): the leaving group departs with its pair of electrons, and the aromaticity is restored.

**Definition 14.11.2 (Meisenheimer Complex)** The cyclohexadienyl anion intermediate formed by addition of a nucleophile to the aromatic ring in the addition–elimination mechanism of SNAr is called the **Meisenheimer complex**.

Meisenheimer (1902) obtained the same red salt from 2,4,6-trinitroanisole with potassium ethoxide and from 2,4,6-trinitrophenetole with potassium methoxide, which proved the existence of the intermediate: in both reactions the intermediate is a Meisenheimer complex bearing both $\ce{OCH3}$ and $\ce{OC2H5}$ on an sp³ carbon.

![Meisenheimer's evidence: 2,4,6-trinitroanisole with ethoxide (left) and 2,4,6-trinitrophenetole with methoxide (right) give the same Meisenheimer complex, whose sp³ carbon bears both OCH₃ and OC₂H₅ (drawn as the major resonance structure, with the negative charge on the para nitro group)](./plots/meisenheimer-evidence.py)

![Addition–elimination mechanism of SNAr: sodium methoxide and 1-fluoro-4-nitrobenzene. Top: methoxide adds to the fluorine-bearing carbon (slow) to give a Meisenheimer complex, the negative charge being distributed over C2, C4 and C6 and delocalized through the para nitro group onto oxygen (nitrate-type resonance structure). Bottom: fluoride leaves (fast) and the aromatic ring is restored](./plots/snar.py)

The negative charge is distributed over the ortho and para positions relative to the sp³ carbon (the same positions as the positive charge of the σ complex). The electron-withdrawing group must therefore be ortho or para to the leaving group so that, by resonance, it can accept the negative charge onto an electronegative atom; a meta electron-withdrawing group acts only through the inductive effect, which is much less effective. The more electron-withdrawing groups there are, the easier the reaction:

| Substrate | Conditions for forming the phenol with $\ce{OH-}$ |
|---|---|
| Chlorobenzene | No addition–elimination (at high temperature and pressure through the benzyne mechanism, [6.5.15](/6.5.15#sec-15.1.1)) |
| 1-Chloro-4-nitrobenzene | Aqueous NaOH, about $130\,^\circ\mathrm{C}$ |
| 1-Chloro-2,4-dinitrobenzene | Aqueous $\ce{Na2CO3}$, about $100\,^\circ\mathrm{C}$ |
| 1-Chloro-2,4,6-trinitrobenzene (picryl chloride) | Warm water |

### 14.11.2. Leaving Groups and Activating Groups

The order of leaving groups in SNAr is the opposite of that in **SN2**: $\ce{F} \gg \ce{Cl} \approx \ce{Br} > \ce{I}$. In the reaction of 1-halo-2,4-dinitrobenzenes with piperidine in methanol, the fluoro compound is about $10^3$ times faster than the chloro compound (Bunnett and coworkers). The reason is that the rate-determining step is the addition, in which the C–X bond is not broken: the electronegativity of fluorine is the greatest, its $-$I effect makes the attacked carbon the most electron-poor and stabilizes the negatively charged intermediate and the transition state leading to it; the strength of the C–F bond affects only the subsequent fast elimination. $\ce{NO2-}$, $\ce{RSO2-}$ and even $\ce{OR-}$ can also leave from suitable substrates.

![Free-energy profiles for SNAr of 1-halo-2,4-dinitrobenzenes (schematic). The rate-determining step is the addition (TS1): fluorine, the most electronegative halogen, lowers TS1 and the Meisenheimer complex the most; the strong C–F bond only raises TS2 of the elimination, which still lies below TS1. The iodo compound has the highest TS1, so the leaving-group order is F ≫ Cl ≈ Br > I, the reverse of SN2](./plots/snar-leaving-group.py)

The activating power of groups is roughly $\ce{-N2+}$ ([6.5.24](/6.5.24#sec-24.4)) > $\ce{-NO2}$ > $\ce{-SO2R}$ ≈ $\ce{-CN}$ > $\ce{-COR}$ > $\ce{-CF3}$. A ring N atom also activates: 2-chloropyridine and 4-chloropyridine undergo SNAr much more readily than chlorobenzene, because the negative charge can be delocalized onto the ring N ([6.5.25](/6.5.25#sec-25.5.2)). "Nitro groups ortho and para, a halogen as the leaving group" is thus only the most common case and not a requirement.

Applications of SNAr:

- Sanger treated the N-terminal amino group of peptides with 1-fluoro-2,4-dinitrobenzene (Sanger's reagent) in an SNAr reaction and identified the N-terminal amino acid after hydrolysis, thereby determining the amino acid sequence of insulin (1958 Nobel Prize in Chemistry, [6.5.33](/6.5.33)). Glutathione S-transferase catalyzes the SNAr reaction of the thiol of glutathione with 1-chloro-2,4-dinitrobenzene, the standard assay for the activity of this detoxifying enzyme.
- Drug synthesis: in the synthesis of fluoroquinolone antibiotics (ciprofloxacin, ofloxacin), several C–N and C–O bonds are formed by SNAr (Question 6).

Recent studies of kinetic isotope effects and computations (Kwan, Jacobsen and coworkers, *Nat. Chem.* 2018) show that many SNAr reactions of weakly activated substrates (with only one electron-withdrawing group, or heterocycles) do not proceed through a stable Meisenheimer intermediate but are concerted; only strongly activated substrates (with several nitro groups) have a true intermediate. There are other mechanisms of nucleophilic substitution on aromatic rings: elimination–addition through **benzyne** ([6.5.15](/6.5.15#sec-15.1)), substitution of diazonium salts ([6.5.24](/6.5.24#sec-24.4)), and transition-metal-catalyzed coupling (the **Buchwald–Hartwig amination**, [6.5.29](/6.5.29#sec-29.4.6)).

## Summary

- SEAr (Definition 14.1.1) proceeds in two steps: the π electrons attack the electrophile to give the σ complex (Definition 14.2.1, rate-determining), and loss of a proton then restores aromaticity; $k_{\mathrm{H}}/k_{\mathrm{D}} \approx 1$ and the isolation of σ complexes are the evidence. Substitution rather than addition occurs because the substitution product retains the aromatic stabilization energy.
- Electrophiles are generated by acid activation: $\ce{NO2+}$ (mixed acid), $\ce{X2}$–$\ce{FeX3}$, $\ce{SO3}$ (fuming sulfuric acid), $\ce{R+}$ or $\ce{R-Cl-AlCl3}$, $\ce{RC#O+}$, $\ce{HC#O+}$ (Gattermann–Koch).
- Substituent effects: all activating groups are ortho, para directors; halogens deactivate but are ortho, para directing ($-$I > $+$M); the other deactivating groups are meta directors (Definition 14.3.1). The reason lies in the σ complex: on ortho or para attack the positive charge falls on C1, where it is stabilized by lone pairs or destabilized by electron-withdrawing groups; meta attack does not pass through C1.
- Partial rate factors (Definition 14.3.2): in nitration of toluene $f_o \approx 42$, $f_m \approx 2.5$ and $f_p \approx 58$; $\lg f_p = \rho\sigma_p^+$ (Eq. (14.1)), and $\rho$ for SEAr is a large negative number (about $-6$ for nitration). The larger the alkyl group and the electrophile, the less ortho product.
- Synthetic design: arrange the order by the directing principle, introduce deactivating groups late, change the directing effect by $\ce{NO2 -> NH2}$, $\ce{COR -> CH2R}$, $\ce{CH3 -> COOH}$, block the para position with a sulfonic acid or tert-butyl group, and tune the reactivity of aniline by acetylation.
- Friedel–Crafts (Definition 14.9.1) alkylation: rearrangement, polyalkylation, no reaction of deactivated rings and amines, no reaction of aryl halides, reversible; acylation: no rearrangement, monosubstitution only, stoichiometric $\ce{AlCl3}$ required, and subsequent reduction gives primary alkylarenes. Sulfonation is reversible and can serve as a blocking group.
- SNAr (Definition 14.11.1): strongly electron-withdrawing groups ortho and para to the leaving group; addition to give the Meisenheimer complex (Definition 14.11.2) is rate-determining, and the leaving group order is $\ce{F} \gg \ce{Cl} \approx \ce{Br} > \ce{I}$; weakly activated substrates often react by a concerted mechanism.

## Questions

1. For each of the following reactions, write the main product and give the reason: (a) bromination of anisole; (b) nitration of benzoic acid; (c) nitration of chlorobenzene; (d) nitration of tert-butylbenzene; (e) nitration of 4-methylacetanilide.

   **Answer** (a) Mainly 4-bromoanisole (with a little 2-bromo); $\ce{OCH3}$ is strongly activating and ortho, para directing, and the para position is less hindered; no catalyst is needed. (b) 3-Nitrobenzoic acid; COOH is deactivating and meta directing, and stronger conditions are needed. (c) Mainly 1-chloro-4-nitrobenzene (about 69%), with some 2-chloro (about 30%); the halogen deactivates but is ortho, para directing. (d) Mainly 4-nitro-tert-butylbenzene (about 73%); the tert-butyl group is bulky, and the ortho product is only about 16%. (e) The nitro group enters ortho to $\ce{NHCOCH3}$ (that is, meta to methyl): the para positions are mutually occupied, and the activating effect of $\ce{NHCOCH3}$ is stronger than that of $\ce{CH3}$, giving 4-methyl-2-nitroacetanilide.
2. Starting from benzene, synthesize: (a) 1-chloro-2-nitrobenzene; (b) 1-chloro-3-nitrobenzene; (c) 1-chloro-4-methylbenzene; (d) propylbenzene; (e) 3-bromoacetophenone.

   **Answer** (a) $\ce{Cl2}$/$\ce{FeCl3}$ gives chlorobenzene, which is nitrated with mixed acid; the ortho isomer is separated (para is the main product, ortho about 30%). (b) First nitrate (nitrobenzene) and then chlorinate with $\ce{Cl2}$/$\ce{FeCl3}$; the nitro group directs chlorine to the meta position. (c) Friedel–Crafts methylation of benzene ($\ce{CH3Cl}$/$\ce{AlCl3}$, with controlled amounts) gives toluene, which is then chlorinated and the para isomer separated; if chlorination came first, chlorobenzene is less reactive, and polyalkylation and isomerization are worse in the subsequent methylation. (d) Acylation with propanoyl chloride/$\ce{AlCl3}$ gives propiophenone, which is reduced by the Clemmensen or Wolff–Kishner method; direct alkylation with 1-chloropropane cannot be used (rearrangement to isopropylbenzene). (e) First acetylate to acetophenone (meta directing), then brominate with $\ce{Br2}$/$\ce{FeBr3}$, with bromine entering meta to the acetyl group; in the reverse order, bromination followed by acylation would give the para product.
3. Use 3-methylaniline as an example to illustrate "functional group interconversion": how can it be obtained from toluene?

   **Answer** Direct nitration of toluene gives ortho and para products, not the meta product. One route: nitrate toluene and separate 4-nitrotoluene; reduce to 4-methylaniline and acetylate to 4-methylacetanilide; nitrate, the nitro group entering ortho to the acetylamino group (meta to methyl); hydrolyze to 4-methyl-2-nitroaniline, and after **diazotization** remove the amino group with $\ce{H3PO2}$ ([6.5.24](/6.5.24#sec-24.4.4)) to give 3-nitrotoluene; finally reduce the nitro group to give 3-methylaniline. Here the amino group serves as a temporary strong directing group and is removed after its task is done.
4. In Friedel–Crafts acylation: (a) why must at least 1 equivalent of $\ce{AlCl3}$ be used with acetyl chloride? What about with acetic anhydride? (b) Why does acylation give only monosubstitution products, whereas alkylation often gives polysubstitution products? (c) Benzene with pivaloyl chloride and $\ce{AlCl3}$ gives mainly tert-butylbenzene; explain.

   **Answer** (a) The carbonyl oxygen of the product acetophenone forms a stable complex with $\ce{AlCl3}$, so the catalyst is "consumed" and at least 1 equivalent is needed; with acetic anhydride the acetic acid formed as the other half (in the form of $\ce{CH3COOAlCl2}$, etc.) binds another equivalent, so 2 or more equivalents are needed in all. (b) The acyl group (which is also coordinated to $\ce{AlCl3}$ during the reaction) is a deactivating group, so the product is less reactive than the starting material; the alkyl group is an activating group, so the product is more reactive than the starting material. (c) The pivaloyl cation $\ce{(CH3)3C-C#O+}$ loses CO to give the stable tert-butyl cation, and decarbonylation is faster than attack on the aromatic ring.
5. Write the formation of the electrophile in the Gattermann–Koch reaction and explain why HCOCl cannot be used for Friedel–Crafts formylation.

   **Answer** $\ce{CO + HCl + AlCl3 -> HC#O+ AlCl4-}$: the proton of HCl adds to the carbon of CO (the HOMO of CO is mainly on carbon) to give the formylium ion, which, like the acylium ion, is stabilized by the resonance $\ce{H-C#O+ <-> H-C+=O}$; CuCl coordinates to CO so that the reaction can proceed at atmospheric pressure. HCOCl decomposes to CO and HCl at room temperature and cannot be stored as a reagent; the Gattermann–Koch reaction amounts to generating its equivalent in situ.
6. In the synthesis of ofloxacin, compound A (ethyl 2-(2,3,4,5-tetrafluorobenzoyl)-3-[(1-hydroxypropan-2-yl)amino]acrylate) gives the tricyclic B on treatment with NaH ($70$–$90\,^\circ\mathrm{C}$); B is heated with $N$-methylpiperazine in toluene to give C, and C is hydrolyzed to ofloxacin. Write the key points of the mechanisms A → B and B → C, and explain which F of B is replaced by piperazine.

   **Answer** A → B consists of two intramolecular SNAr reactions: NaH deprotonates the N–H of the enamine (a vinylogous amide, fairly acidic), and N attacks the C–F on the ring adjacent to the carbonyl group (ortho to the carbonyl group), losing $\ce{F-}$ through a Meisenheimer complex (the negative charge being delocalized onto the carbonyl oxygen) and closing the ring to the quinolone; the alcoholic hydroxy group is deprotonated, and the alkoxide attacks the next adjacent C–F (this carbon is now ortho to the N of the pyridone ring and activated inductively by the adjacent F), closing the six-membered oxazine ring to give B. B → C: two F atoms remain in B, and the secondary amine N of piperazine replaces the F para to the C4 carbonyl group (on the carbon adjacent to the one bearing the oxazine O), because the negative charge of the Meisenheimer complex formed by attack there can be delocalized onto the carbonyl oxygen of the quinolone; the other F is meta to the carbonyl group and gets no such stabilization. Finally the ester is hydrolyzed in aqueous NaOH, and acidification gives the carboxylic acid.
7. 4-Bromo-1-fluoro-2-nitrobenzene reacts with sodium methoxide. Which halogen is replaced, and why?

   **Answer** F is replaced, giving 4-bromo-2-nitroanisole. F is ortho to the nitro group, and the negative charge of the Meisenheimer complex formed by addition can be delocalized onto the nitro group; moreover, the rate-determining step of SNAr is the addition, and the strong $-$I effect of F makes the carbon bearing F the most electron-poor, so F is the best leaving group in SNAr. Br is meta to the nitro group, so it gets no resonance activation, and its leaving ability is lower than that of F.
8. Use the resonance structures of the σ complex to explain: (a) why trifluoromethyl is a meta director; (b) why the activating effect of $\ce{-NHCOCH3}$ is weaker than that of $\ce{-NH2}$.

   **Answer** (a) On attack ortho or para to $\ce{CF3}$, one resonance structure places the positive charge on the carbon attached to $\ce{CF3}$, and the strongly electron-withdrawing $\ce{CF3}$ (the inductive effect of three F atoms) makes this resonance structure very high in energy; on meta attack the positive charge does not fall on this carbon, which is relatively favorable. (b) The lone pair of the amide N is simultaneously conjugated with the carbonyl group (amide resonance) and can be donated to the ring to a lesser extent, so the iminium resonance structure formed on ortho or para attack contributes less; the lone pair of aniline is conjugated only with the ring, and the stabilization is much greater.
