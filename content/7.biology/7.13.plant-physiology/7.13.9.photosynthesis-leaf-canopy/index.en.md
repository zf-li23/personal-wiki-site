---
title: Photosynthesis in the Leaf and the Canopy
description: Definition and measurement of photosynthetic rate (open gas exchange, the half-leaf method, fluorescence); light-response curves, light compensation and saturation points, the physiology of sun and shade leaves, sunflecks and induction; CO2 response curves and the Farquhar–von Caemmerer–Berry model (Rubisco, RuBP regeneration and triose phosphate utilization limitations) with parameter estimation; stomatal and mesophyll conductance, supply–demand curves and stomatal limitation; the temperature response and the crossover of C3 and C4 quantum yields; water stress and the midday depression of photosynthesis; light distribution in the canopy, leaf area index and canopy photosynthesis; radiation-use efficiency, the Monteith equation and the theoretical upper limit of light conversion; effects of elevated CO2 and ways to raise radiation-use efficiency.
source_hash: d2b188c2f66b
---

The previous two chapters described how the chloroplast absorbs light energy ([7.13.7](/7.13.7)) and how it fixes $\ce{CO2}$ ([7.13.8](/7.13.8)). This chapter puts these processes back into the complete leaf and canopy: how the net photosynthetic rate of a leaf varies with light intensity, $\ce{CO2}$ concentration, temperature and water; at any moment whether photosynthesis is limited by the light reactions, Rubisco, the stomata or product export; and how much solar energy a field or forest as a whole can convert to biomass, and how far this is from the theoretical upper limit. There is a standard set of quantitative tools for these questions: the nonrectangular hyperbola for the light response (introduced in [7.12.32](/7.12.32#sec-32.3.2)), the Farquhar–von Caemmerer–Berry model for the $\ce{CO2}$ response, **Fick's law** for stomatal diffusion, and Beer's law for the distribution of light in the canopy. They are also the basis for computing primary production in ecology (7.19) and in Earth system models. The mechanism of stomatal opening and closing is covered in [7.13.10](/7.13.10).

## 9.1. Photosynthetic Rate and Its Measurement

### 9.1.1. Net and Gross Photosynthesis

The photosynthetic rate is the amount of $\ce{CO2}$ fixed (or $\ce{O2}$ evolved, or dry matter accumulated) per unit time per unit leaf area; the usual unit for leaves is $\mathrm{\mu mol\,CO_2\,m^{-2}\,s^{-1}}$. A leaf in the light carries out photosynthesis, **photorespiration** and mitochondrial respiration at the same time, and what is measured directly is their algebraic sum, the net photosynthetic rate (apparent photosynthetic rate) $A$:

$$
A = V_{\mathrm{c}} - 0.5\,V_{\mathrm{o}} - R_{\mathrm{d}},
$$
where $V_{\mathrm{c}}$ and $V_{\mathrm{o}}$ are the carboxylation and oxygenation rates of Rubisco and $R_{\mathrm{d}}$ is mitochondrial respiration in the light (day respiration, often somewhat lower than dark respiration). Chinese textbooks call $V_{\mathrm{c}}$ the true (gross) photosynthetic rate, that is, "apparent photosynthesis = true photosynthesis − photorespiration − dark respiration".

### 9.1.2. Methods of Measurement

| Method | Principle | Characteristics |
|---|---|---|
| Open gas exchange (infrared $\ce{CO2}$ analyzer) | the leaf is clamped in a chamber and the difference in $\ce{CO2}$ and water vapor concentration between air entering and leaving the chamber is measured | gives $A$, transpiration rate, stomatal conductance and intercellular $\ce{CO2}$ together, with control of light, $\ce{CO2}$, temperature and humidity; the standard method of modern physiological ecology |
| Oxygen electrode | a Clark electrode measures $\ce{O2}$ evolved by leaf discs or chloroplast suspensions | suited to measuring maximum quantum yield and photosynthetic capacity |
| Modified half-leaf method | one half of the leaf is removed and dried and weighed at the start, the other half after a few hours of light (girdling or scalding the petiole prevents export of assimilates); the difference in dry weight is the dry matter accumulated by photosynthesis | simple and suited to the field, but gives only a mean over a period |
| Isotopes | $^{14}\ce{CO2}$ pulse labeling, or $^{13}\mathrm{C}$/$^{18}\mathrm{O}$ tracing | distinguishes gross fixation from re-release, and measures photorespiration and product partitioning |
| Chlorophyll fluorescence | electron transport rate estimated from $\Phi_{\mathrm{PSII}}$ ([7.13.7](/7.13.7#sec-7.4.2)) | fast and nondestructive, can be imaged; must be calibrated against gas exchange |
| Remote sensing | canopy reflectance spectra (vegetation indices), solar-induced chlorophyll fluorescence | regional and global scales |

In an open system, let air flow at molar flow rate $u$ ($\mathrm{mol\,s^{-1}}$) through a chamber of leaf area $s$, with $\ce{CO2}$ mole fractions $c_{\mathrm{e}}$ entering and $c_{\mathrm{o}}$ leaving; neglecting the change in flow caused by transpiration,

$$
A = \frac{u\,(c_{\mathrm{e}} - c_{\mathrm{o}})}{s}. \tag{9.1}
$$

**Example 9.1.1** The chamber area is $6\,\mathrm{cm^2}$, the air flow $500\,\mathrm{\mu mol\,s^{-1}}$, and $\ce{CO2}$ is $420$ in the inlet air and $397\,\mathrm{\mu mol\,mol^{-1}}$ in the outlet air. $A = 500\times10^{-6}\,\mathrm{mol\,s^{-1}} \times 23\times10^{-6}/(6\times10^{-4}\,\mathrm{m^2}) = 1.92\times10^{-5}\,\mathrm{mol\,m^{-2}\,s^{-1}} = 19.2\,\mathrm{\mu mol\,m^{-2}\,s^{-1}}$. If this rate were kept up for 10 h, each square meter of leaf would fix $0.69\,\mathrm{mol}$ of $\ce{CO2}$, about 21 g of carbohydrate as $\ce{CH2O}$.

## 9.2. The Light Response

### 9.2.1. The Light-Response Curve

The change of net photosynthetic rate of a leaf with light intensity (the light-response curve) has three segments: in weak light $A$ rises linearly with light intensity and is limited by the light reactions; at moderate light intensity the increase slows; in strong light the curve approaches saturation, and the limitation shifts to the carboxylation capacity of Rubisco, the capacity of the electron-transport chain or product export (Section 9.3). The curve is often described by a nonrectangular hyperbola ([7.12.32](/7.12.32#sec-32.3.2)): gross photosynthesis $A_{\mathrm{g}}$ is the smaller root of $\theta A_{\mathrm{g}}^2 - (\phi I + A_{\max})A_{\mathrm{g}} + \phi I A_{\max} = 0$, and $A = A_{\mathrm{g}} - R_{\mathrm{d}}$, where $\phi$ is the apparent quantum efficiency (initial slope), $A_{\max}$ is light-saturated gross photosynthesis, and $\theta$ describes the curvature of the curve. Two characteristic points of the curve can then be defined.

**Definition 9.2.1 (Light Compensation Point)** The light intensity at which the $\ce{CO2}$ taken up by photosynthesis equals the $\ce{CO2}$ released by respiration (including photorespiration), so that the net photosynthetic rate is zero, is called the **light compensation point**. In the nonrectangular hyperbola, setting $A_{\mathrm{g}} = R_{\mathrm{d}}$ gives

$$
I_{\mathrm{c}} = \frac{R_{\mathrm{d}}\,(A_{\max} - \theta R_{\mathrm{d}})}{\phi\,(A_{\max} - R_{\mathrm{d}})} \approx \frac{R_{\mathrm{d}}}{\phi}. \tag{9.2}
$$

**Definition 9.2.2 (Light Saturation Point)** The light intensity beyond which the net photosynthetic rate no longer increases appreciably and begins to reach its maximum is called the **light saturation point**. The nonrectangular hyperbola saturates only asymptotically, and in practice the light intensity at which $A_{\mathrm{g}}$ reaches 90% of $A_{\max}$ is often taken: solving the equation gives $I_{90} = 10A_{\max}(0.9 - 0.81\theta)/\phi$.

**Example 9.2.1** Take the parameters of the sun leaf in 7.12.32 ($A_{\max} = 25$, $R_{\mathrm{d}} = 2\,\mathrm{\mu mol\,m^{-2}\,s^{-1}}$, $\phi = 0.05$, $\theta = 0.8$): by Eq. (9.2), $I_{\mathrm{c}} = 2 \times (25 - 1.6)/(0.05 \times 23) = 41\,\mathrm{\mu mol\,m^{-2}\,s^{-1}}$, and the approximation $R_{\mathrm{d}}/\phi$ gives 40; $I_{90} = 10 \times 25 \times 0.252/0.05 = 1260\,\mathrm{\mu mol\,m^{-2}\,s^{-1}}$. For a shade leaf ($A_{\max} = 7$, $R_{\mathrm{d}} = 0.4$): $I_{\mathrm{c}} = 8.1$ and $I_{90} = 353\,\mathrm{\mu mol\,m^{-2}\,s^{-1}}$. The light compensation point is determined mainly by the ratio of respiration rate to quantum efficiency, and the light saturation point mainly by photosynthetic capacity.

The apparent quantum efficiency $\phi$ is the slope in weak light per incident photon; per absorbed photon and measured in low $\ce{O2}$ it approaches the maximum **quantum yield** in [7.13.7](/7.13.7#sec-7.3.2). In today's air the quantum yield of C3 and C4 leaves per absorbed photon is 0.04–0.07, falling with rising temperature in C3 leaves and rising to about 0.09 in 2% $\ce{O2}$ (Section 9.4.1).

Light compensation and saturation points vary with species, leaf age and growth environment. The light compensation point of sun plants is about 10–20 (for typical dark respiration, and sometimes higher) and that of shade plants about 1–5 $\mathrm{\mu mol\,m^{-2}\,s^{-1}}$; single leaves of most C3 crops saturate at about 1000–1500 $\mathrm{\mu mol\,m^{-2}\,s^{-1}}$, one half to two thirds of full sunlight, shade plants saturate at 100–300, and C4 plants are often still unsaturated in full sunlight. A canopy differs from a single leaf: when leaves in the upper canopy saturate, leaves below are still in weak light, so canopy photosynthesis seldom saturates even in full sunlight (Section 9.5).

### 9.2.2. Sun Leaves and Shade Leaves

The morphological and anatomical differences between sun and shade leaves were compared in [7.12.32](/7.12.32#sec-32.3.2). Their physiological differences are in essence how a leaf divides limited nitrogen between capturing light and using it:

| | Sun leaf | Shade leaf |
|---|---|---|
| Rubisco, electron-transport chain and $A_{\max}$ per unit area | high | low |
| Chlorophyll per unit area | higher | lower or similar |
| Rubisco and reaction centers per unit chlorophyll | more | fewer; large antenna (more LHCII, low chlorophyll a/b) |
| Respiration rate $R_{\mathrm{d}}$, light compensation point | high | low |
| Quantum yield | similar to shade leaf | similar to sun leaf |
| Xanthophyll cycle pool, antioxidant capacity | large | small; easily suffers **photoinhibition** when moved into strong light |
| Leaf mass per area (dry weight per unit area) | large | small; large area expanded per unit dry weight |

The quantum yield is determined by the stoichiometry of photochemistry and the Calvin cycle and is the same in both kinds of leaf; what changes is the part beyond saturation. The strategy of the shade leaf is to spread the largest light-capturing area with the least investment and to lower maintenance respiration; the sun leaf invests nitrogen in the enzymes that use light. Adaptation of a leaf to the light environment during development is plastic: upper and lower leaves of the same plant, and the same species grown under different light intensities, show such differences; the adjustment takes days to weeks and is mostly determined as the leaf expands.

Light on the forest floor is not uniform: gaps between upper leaves cast sunflecks on the understory, lasting from seconds to minutes and possibly accounting for more than half of the daily light of understory plants. The use of sunflecks is limited by two dynamic processes: on transfer from weak to strong light, activation of Rubisco (Rubisco activase) and stomatal opening take several minutes and over ten minutes respectively ("induction"), and an already induced leaf uses a sunfleck far more efficiently; on transfer from strong to weak light, relaxation of **nonphotochemical quenching** again takes several minutes. Understory plants keep the induced state longer, which is one way they are adapted to sunflecks.

## 9.3. The CO₂ Response and the Farquhar Model

### 9.3.1. The CO₂ Response Curve

When the $\ce{CO2}$ concentration in the chamber is varied at saturating light, the curve of net photosynthesis against intercellular $\ce{CO2}$ concentration $c_{\mathrm{i}}$ is obtained (the $A/c_{\mathrm{i}}$ curve, Figure 1): at low $c_{\mathrm{i}}$, $A$ is negative and it is zero at the **CO₂ compensation point** $\Gamma$ ([7.13.8](/7.13.8#sec-8.2.2)); above this $A$ rises approximately linearly, the slope being called the carboxylation efficiency and mainly reflecting the amount of active Rubisco; at still higher $c_{\mathrm{i}}$ the curve flattens and saturates, and the $\ce{CO2}$ concentration at which saturation begins is called the $\ce{CO2}$ saturation point. The $\ce{CO2}$ saturation point of C3 leaves is usually $800\text{–}1500\,\mathrm{\mu mol\,mol^{-1}}$, far above today's atmosphere, so photosynthesis of C3 plants is $\ce{CO2}$-limited in today's atmosphere and $\ce{CO2}$ enrichment in greenhouses can raise yield; C4 leaves are already nearly saturated at a $c_{\mathrm{i}}$ of about $100\text{–}200\,\mathrm{\mu mol\,mol^{-1}}$.

### 9.3.2. The Farquhar–von Caemmerer–Berry Model

In 1980 Graham Farquhar, Susanne von Caemmerer and Joseph Berry combined the kinetics of Rubisco with the stoichiometry of the light reactions into a biochemical model of photosynthesis in C3 leaves. It remains the core of photosynthesis calculations at leaf and global scales.

**Definition 9.3.1 (Farquhar Model)** The **Farquhar model** (FvCB model) holds that the net photosynthetic rate of a C3 leaf is determined by the most severe of three possible limitations:

$$
A = \min(A_{\mathrm{c}},\,A_{\mathrm{j}},\,A_{\mathrm{p}}),
$$
where the rate limited by Rubisco carboxylation (Rubisco saturated with RuBP, following the **Michaelis–Menten equation** with competition between the two substrates) is

$$
A_{\mathrm{c}} = \frac{V_{\mathrm{cmax}}\,(c_{\mathrm{c}} - \Gamma^*)}{c_{\mathrm{c}} + K_{\mathrm{c}}(1 + O/K_{\mathrm{o}})} - R_{\mathrm{d}}, \tag{9.3}
$$
the rate limited by RuBP regeneration (electron transport) is

$$
A_{\mathrm{j}} = \frac{J\,(c_{\mathrm{c}} - \Gamma^*)}{4c_{\mathrm{c}} + 8\Gamma^*} - R_{\mathrm{d}}, \tag{9.4}
$$
and the rate limited by triose phosphate utilization (TPU) is

$$
A_{\mathrm{p}} = 3\,\mathrm{TPU} - R_{\mathrm{d}}. \tag{9.5}
$$
Here $c_{\mathrm{c}}$ is the $\ce{CO2}$ concentration in the chloroplast ($c_{\mathrm{i}}$ is used instead when mesophyll resistance is ignored), $O$ is the $\ce{O2}$ concentration, $V_{\mathrm{cmax}}$ is the maximum carboxylation rate of Rubisco, $J$ is the electron transport rate, and $\mathrm{TPU}$ is the rate of triose phosphate utilization.

Each of the three equations has a stoichiometric basis. The factor $(c_{\mathrm{c}} - \Gamma^*)$ in Eq. (9.3) comes from the loss of half a $\ce{CO2}$ per oxygenation: $A + R_{\mathrm{d}} = V_{\mathrm{c}}(1 - 0.5\phi) = V_{\mathrm{c}}(1 - \Gamma^*/c_{\mathrm{c}})$ ([7.13.8](/7.13.8#sec-8.2.1)). Equation (9.4) assumes that electron flow is enough to regenerate only a certain amount of RuBP: each carboxylation requires 2 NADPH (4 electrons) and each oxygenation also requires 2 NADPH equivalents, so $J = 4V_{\mathrm{c}} + 4V_{\mathrm{o}} = 4V_{\mathrm{c}}(1 + 2\Gamma^*/c_{\mathrm{c}})$, whence $V_{\mathrm{c}} = J c_{\mathrm{c}}/(4c_{\mathrm{c}} + 8\Gamma^*)$ (if calculated on the basis of ATP limitation the coefficients in the denominator are 4.5 and 10.5). Equation (9.5) expresses that each triose phosphate exported releases one $\mathrm{P_i}$ back to the chloroplast, and three $\ce{CO2}$ make one triose phosphate: when synthesis of sucrose and starch cannot keep up, shortage of $\mathrm{P_i}$ limits photophosphorylation, $A$ no longer increases with $\ce{CO2}$, and at high $\ce{CO2}$ it even declines slightly as $\ce{O2}$ is lowered.

The electron transport rate saturates with light intensity as a nonrectangular hyperbola:

$$
\theta_J J^2 - (\alpha I + J_{\max})J + \alpha I J_{\max} = 0, \tag{9.6}
$$
where $J_{\max}$ is the maximum electron transport rate, $\alpha$ is the number of electrons produced per incident photon (about 0.3, that is absorptance 0.84 × 0.5 allocated to PSII × PSII efficiency of about 0.8), and $\theta_J \approx 0.7$. In weak light, therefore, $A_{\mathrm{j}}$ is limiting and the whole $A/c_{\mathrm{i}}$ curve is lowered (Figure 1B).

Typical values of the model parameters (25 °C):

| Parameter | Meaning | Typical value | Source |
|---|---|---|---|
| $K_{\mathrm{c}}$ | Michaelis constant of Rubisco for $\ce{CO2}$ | $404.9\,\mathrm{\mu mol\,mol^{-1}}$ | Bernacchi et al., 2001 (tobacco, measured in vivo) |
| $K_{\mathrm{o}}$ | Michaelis constant of Rubisco for $\ce{O2}$ | $278.4\,\mathrm{mmol\,mol^{-1}}$ | same |
| $\Gamma^*$ | photorespiratory compensation point | $42.75\,\mathrm{\mu mol\,mol^{-1}}$ | same |
| $V_{\mathrm{cmax}}$ | maximum carboxylation rate | 20–150 $\mathrm{\mu mol\,m^{-2}\,s^{-1}}$ (crops 60–120) | varies with species and leaf nitrogen content |
| $J_{\max}$ | maximum electron transport rate | about $1.5\text{–}2\,V_{\mathrm{cmax}}$ | |
| $\mathrm{TPU}$ | rate of triose phosphate utilization | about $V_{\mathrm{cmax}}/8$ | |
| $R_{\mathrm{d}}$ | day respiration | about $0.01\text{–}0.02\,V_{\mathrm{cmax}}$ | |

![CO₂ response of C3 photosynthesis (Farquhar–von Caemmerer–Berry model). Kinetic constants are the 25 °C values of Bernacchi et al. (2001): $K_{\mathrm{c}}$ = 404.9 µmol mol⁻¹, $K_{\mathrm{o}}$ = 278.4 mmol mol⁻¹, Γ* = 42.75 µmol mol⁻¹, O = 210 mmol mol⁻¹. A: the A/cᵢ curve (thick line) for $V_{\mathrm{cmax}}$ = 80, $J$ = 150, TPU = 9 and $R_{\mathrm{d}}$ = 1 µmol m⁻² s⁻¹ is the lowest of the three limiting curves: at low cᵢ it is limited by Rubisco carboxylation (Eq. (9.3), red dashed line) and above about cᵢ = 430 by triose phosphate utilization (Eq. (9.5), yellow dashed line); with these parameters the RuBP-regeneration rate at saturating light (Eq. (9.4), blue dashed line) always stays above the lower of the other two curves and is never limiting; the open circle is the operating point at atmospheric CO₂ of 420 µmol mol⁻¹ with cᵢ = 0.7cₐ, and the intersection of the curve with the zero line is the CO₂ compensation point. B: the same leaf at three light intensities, with $J$ saturating with light according to Eq. (9.6) ($J_{\max}$ = 150, α = 0.3, θ = 0.7); in weak light the limitation by RuBP regeneration lowers the whole curve](./plots/aci.py)

The $A/c_{\mathrm{i}}$ curve is the standard method for estimating $V_{\mathrm{cmax}}$ and $J_{\max}$: data in the low-$c_{\mathrm{i}}$ segment determine $V_{\mathrm{cmax}}$ and the high-$c_{\mathrm{i}}$ segment determines $J$; in practice the whole curve is fitted to the model by nonlinear least squares (Sharkey et al., 2007).

**Example 9.3.1** A tobacco leaf at saturating light and 25 °C gives $A = 4.65$ at $c_{\mathrm{i}} = 100\,\mathrm{\mu mol\,mol^{-1}}$ and $A = 12.82\,\mathrm{\mu mol\,m^{-2}\,s^{-1}}$ at $c_{\mathrm{i}} = 200$, both points in the Rubisco-limited segment. Let $f = (c_{\mathrm{i}} - \Gamma^*)/(c_{\mathrm{i}} + K)$ with $K = 404.9 \times (1 + 210/278.4) = 710.3$: $f_1 = 57.25/810.3 = 0.07065$ and $f_2 = 157.25/910.3 = 0.17273$. By Eq. (9.3), $V_{\mathrm{cmax}}f_1 - R_{\mathrm{d}} = 4.65$ and $V_{\mathrm{cmax}}f_2 - R_{\mathrm{d}} = 12.82$; subtracting gives $V_{\mathrm{cmax}} = 8.17/0.10208 = 80.0\,\mathrm{\mu mol\,m^{-2}\,s^{-1}}$, and substituting back gives $R_{\mathrm{d}} = 80.0 \times 0.07065 - 4.65 = 1.0$. Real measurements have errors and a two-point estimate is unstable, so more points should be used in a fit. If mesophyll conductance is finite and $c_{\mathrm{i}}$ is used in place of $c_{\mathrm{c}}$, the result is an "apparent" $V_{\mathrm{cmax}}$, lower than the true value.

### 9.3.3. Stomatal Conductance, Mesophyll Conductance and Supply–Demand Curves

$\ce{CO2}$ passes through three stages from the atmosphere to Rubisco: the boundary layer at the leaf surface, the stomata, and the liquid-phase path from the substomatal cavity through the cell wall, plasma membrane and chloroplast envelope to the stroma. By Fick's law, the flux through each stage equals conductance times concentration difference. The first two stages are together called the total conductance $g_{\mathrm{c}}$; when **stomatal conductance** is expressed as the conductance to water vapor $g_{\mathrm{s}}$, the conductance to $\ce{CO2}$ is $g_{\mathrm{s}}/1.6$ (the diffusion coefficient of $\ce{CO2}$ in air is 1/1.6 that of water vapor). Thus

$$
A = g_{\mathrm{c}}\,(c_{\mathrm{a}} - c_{\mathrm{i}}), \tag{9.7}
$$

$$
A = g_{\mathrm{m}}\,(c_{\mathrm{i}} - c_{\mathrm{c}}), \tag{9.8}
$$
where $g_{\mathrm{m}}$ is the *mesophyll conductance*, the diffusive conductance of $\ce{CO2}$ from the substomatal cavity to the chloroplast carboxylation site. The $g_{\mathrm{m}}$ of C3 crops is about 0.1–0.5 $\mathrm{mol\,m^{-2}\,s^{-1}\,bar^{-1}}$, of the same order as stomatal conductance, and at high photosynthetic rates makes $c_{\mathrm{c}}$ lower than $c_{\mathrm{i}}$ by 50–100 $\mathrm{\mu mol\,mol^{-1}}$. Mesophyll conductance depends on the surface area of mesophyll cells facing the intercellular air spaces, the thickness and porosity of the cell wall, how closely chloroplasts abut the plasma membrane, and the aquaporins and carbonic anhydrase in the plasma membrane and chloroplast envelope; leaves of sclerophyllous evergreens have thick cell walls and small $g_{\mathrm{m}}$.

Equation (9.7) is a "supply line": on the $A$–$c_{\mathrm{i}}$ plot it starts from $c_{\mathrm{a}}$ on the horizontal axis with slope $-g_{\mathrm{c}}$; the Farquhar model gives the "demand curve". The actual operating point of the leaf is their intersection (Figure 2).

![Supply and demand of CO₂. A: the demand curve is the Farquhar model of Figure 1 (thick line); the supply lines follow Eq. (9.7), starting from $c_{\mathrm{a}}$ = 420 µmol mol⁻¹, with total conductance $g_{\mathrm{c}}$ = 0.05, 0.15 and 0.30 mol m⁻² s⁻¹; the intersection is the operating point (cᵢ and stomatal limitation $l$ are marked). The dashed line $A_0$ is the photosynthetic rate at infinite conductance (cᵢ = cₐ), and the stomatal limitation is $l = 1 - A/A_0$ (Farquhar and Sharkey, 1982). Stomatal closure flattens the supply line, and cᵢ and A fall together. B: with mesophyll conductance $g_{\mathrm{m}}$ = 0.2 mol m⁻² s⁻¹ bar⁻¹, photosynthesis of the same leaf plotted against chloroplast CO₂ $c_{\mathrm{c}}$ (solid line) and against intercellular CO₂ $c_{\mathrm{i}}$ (dashed line); the difference is $A/g_{\mathrm{m}}$ (Eq. (9.8))](./plots/supply-demand.py)

**Example 9.3.2** Using the demand curve of Figure 2 with $g_{\mathrm{c}} = 0.15\,\mathrm{mol\,m^{-2}\,s^{-1}}$ (that is $g_{\mathrm{s}} \approx 0.24$), the $c_{\mathrm{i}}$ of the operating point is solved from $0.15(420 - c_{\mathrm{i}}) = 80(c_{\mathrm{i}} - 42.75)/(c_{\mathrm{i}} + 710.3) - 1$: multiplying both sides by $c_{\mathrm{i}} + 710.3$ and rearranging gives the quadratic equation $0.15c_{\mathrm{i}}^2 + 122.5c_{\mathrm{i}} - 48\,879 = 0$ with positive root $c_{\mathrm{i}} = 294\,\mathrm{\mu mol\,mol^{-1}}$, $A = 0.15 \times 126 = 18.9\,\mathrm{\mu mol\,m^{-2}\,s^{-1}}$ and $c_{\mathrm{i}}/c_{\mathrm{a}} = 0.70$. At $c_{\mathrm{i}} = c_{\mathrm{a}}$, $A_0 = 25.7$ and the stomatal limitation is $l = 1 - 18.9/25.7 = 0.26$. When stomatal conductance falls to one third ($g_{\mathrm{c}} = 0.05$), $c_{\mathrm{i}} = 186$, $A = 11.7$ and $l = 0.54$. A two-thirds reduction in conductance reduces photosynthesis by only about 38%, whereas transpiration falls roughly in proportion to conductance, so water-use efficiency rises; this is the gain to a plant from partial stomatal closure in drought.

Supply–demand analysis also gives a criterion for distinguishing stomatal from nonstomatal limitation (Farquhar and Sharkey, 1982): if $c_{\mathrm{i}}$ falls together with photosynthesis, stomatal closure is mainly responsible (the supply line flattens); if $A$ falls while $c_{\mathrm{i}}$ is unchanged or rises, the photosynthetic capacity of the mesophyll has fallen (the demand curve is lowered), for example when severe drought, high temperature or senescence inactivates Rubisco or damages the photosynthetic apparatus.

## 9.4. Temperature and Water

### 9.4.1. The Temperature Response

The temperature response curve of leaf photosynthesis is unimodal. At low temperature enzymatic reactions are slow and $V_{\mathrm{cmax}}$, $J_{\max}$ and triose phosphate utilization all fall (the $\mathrm{P_i}$ limitation caused by slower sucrose synthesis in the cold is especially marked); at high temperature photorespiration increases, Rubisco activase is inactivated above about 35 °C, and electron transport in the thylakoid membrane becomes unstable. The temperature dependence of model parameters is generally written as the **Arrhenius equation**:

$$
k(T) = k_{25}\exp\!\left[\frac{E_{\mathrm{a}}\,(T - 298.15\,\mathrm{K})}{298.15\,\mathrm{K}\cdot R\,T}\right], \tag{9.9}
$$
The activation energies $E_{\mathrm{a}}$ measured by Bernacchi et al. (2001) are $65.3$ for $V_{\mathrm{cmax}}$, $79.4$ for $K_{\mathrm{c}}$, $36.4$ for $K_{\mathrm{o}}$ and $37.8\,\mathrm{kJ\,mol^{-1}}$ for $\Gamma^*$; $J_{\max}$ must in addition be multiplied by a deactivation term at higher temperature so that it has a peak. $K_{\mathrm{c}}$ and $\Gamma^*$ increase with temperature as fast as, or faster than, $V_{\mathrm{cmax}}$, so the optimum temperature of photosynthesis of C3 leaves at today's $\ce{CO2}$ is only about 20–30 °C; in C4 leaves Rubisco is at saturating $\ce{CO2}$ and escapes this offsetting, with an optimum of 30–40 °C. The optimum temperature also acclimates to growth temperature: plants grown at higher temperature have a higher optimum. Most plants photosynthesize normally between 10 and 35 °C, polar and alpine plants still show net photosynthesis near 0 °C, and desert C4 plants (such as *Tidestromia oblongifolia*) photosynthesize fastest at about 47 °C.

The effect of temperature on quantum yield distinguishes C3 from C4 most clearly (Ehleringer and Björkman, 1977). Under light limitation $A = (J/4)(c_{\mathrm{c}} - \Gamma^*)/(c_{\mathrm{c}} + 2\Gamma^*)$ (Eq. (9.4)), so the quantum yield of C3 leaves falls as $\Gamma^*$ rises; the quantum yield of C4 leaves is lower because the C4 cycle consumes additional ATP, but hardly changes with temperature. The temperature of crossover between the two varies with $\ce{CO2}$ concentration (Figure 3).

![Quantum yield of C3 and C4 leaves as a function of leaf temperature. C3: $\phi = \phi_0(c_{\mathrm{i}} - \Gamma^*)/(c_{\mathrm{i}} + 2\Gamma^*)$ with $\phi_0$ = 0.093 (yield without photorespiration), Γ* from Eq. (8.1) and $c_{\mathrm{i}} = 0.7c_{\mathrm{a}}$; in 2% O₂ Γ* is about one tenth (dotted line). C4: about 0.054, independent of temperature. Parameters follow the measured values of Ehleringer and Björkman (1977) (both about 0.052 near 30 °C). The crossover temperatures in the preindustrial (280), present (420) and future (700 µmol mol⁻¹) atmosphere are about 23, 31 and 42 °C: below the crossover temperature C3 is more efficient and above it C4 is more efficient](./plots/qy-temperature.py)

Quantum yield determines the carbon gain under light limitation, and most leaves in a canopy are light-limited, so the crossover temperature predicts well the distribution of C3 and C4 grasses along latitude and elevation: on the North American Great Plains, the south with its high growing-season temperatures is dominated by C4 grasses and the north by C3; on tropical mountains C4 grasses decrease with elevation. Figure 3 also shows that a rise in atmospheric $\ce{CO2}$ raises the crossover temperature, favoring C3 plants if other conditions are unchanged.

### 9.4.2. Water and the Midday Depression of Photosynthesis

Water deficit first closes the stomata and lowers $c_{\mathrm{i}}$ (stomatal limitation); under moderate drought most of the fall in photosynthesis can be explained by the fall in $c_{\mathrm{i}}$, and recovery after rewatering is quick. In severe drought the photosynthetic capacity of the mesophyll itself falls: ATP synthesis and RuBP regeneration are impaired, Rubisco activity decreases and export of photosynthate slows; at the same time $\ce{CO2}$ supply is insufficient while the light is unchanged, excess light energy increases and photoinhibition worsens ([7.13.7](/7.13.7#sec-7.5.4)).

The response of stomatal conductance to the environment is often described by empirical models, of which the most widely used is the Ball–Berry model and the form derived from optimization theory by Medlyn et al. (2011):

$$
g_{\mathrm{s}} = g_0 + 1.6\left(1 + \frac{g_1}{\sqrt{D}}\right)\frac{A}{c_{\mathrm{a}}},
$$
where $D$ is the leaf-to-air vapor pressure deficit (kPa) and $g_1$ is a parameter reflecting the water-use strategy of the plant ($g_1$ is small for conservative water users). It links the demand curve of Section 9.3 with the supply line: the stronger the photosynthesis, the wider the stomata open; the drier the air, the more the stomata close.

On a clear summer day the diurnal course of leaf photosynthetic rate takes one of two forms. With moderate light and temperature and ample water, photosynthesis follows light intensity through the day in a single-peak curve, highest around noon. On days of strong light, high temperature and dry air, the photosynthetic rate falls markedly around noon and recovers somewhat in the afternoon, giving a double-peak curve; this phenomenon is called the midday depression of photosynthesis. It has several causes that usually act together:

| Cause | Mechanism | Evidence |
|---|---|---|
| Partial stomatal closure | at noon the leaf-to-air vapor pressure deficit is greatest and leaf water potential falls; ABA and hydraulic signals close the stomata ([7.13.10](/7.13.10)) | $c_{\mathrm{i}}$ falls; irrigation or raising air humidity relieves it |
| Excessive leaf temperature | photorespiration and dark respiration increase, near or above the optimum temperature of photosynthesis | more marked on hot days |
| Photoinhibition | $F_{\mathrm{v}}/F_{\mathrm{m}}$ falls and nonphotochemical quenching increases in strong light | partial recovery in the afternoon |
| Product feedback | sugars and starch accumulated in the morning inhibit photosynthesis | sink-removal or shading control experiments |
| Circadian clock | photosynthesis and stomatal conductance have an endogenous daily rhythm | the rhythm persists in constant conditions |

In agriculture, the midday depression greatly reduces photosynthesis in the few hours of strongest light in the day; timely irrigation, cooling by sprinkling and rational planting density to improve the field microclimate can all relieve it.

### 9.4.3. Other Internal and External Factors

The photosynthetic capacity of a leaf is closely related to its nitrogen content per unit area: about half of leaf nitrogen is in the photosynthetic apparatus, and in C3 leaves Rubisco alone makes up 30%–50% of soluble leaf protein, so $A_{\max}$ is roughly proportional to leaf nitrogen content, one of the central relationships of the global "leaf economics spectrum" of plants (Wright et al., 2004). The effect of leaf age is unimodal: in young leaves chloroplasts and enzymes are incomplete and respiration is high, the maximum is reached after expansion, and it declines in senescence ([7.13.24](/7.13.24)). Export of assimilates also affects photosynthesis: removing **sinks** such as fruits, or girdling the petiole to prevent export, causes sugars and starch to accumulate in the leaf and photosynthesis to fall; strengthening sinks (for example by removing some leaves) raises photosynthesis in the remaining leaves. This feedback arises from the limitation by triose phosphate utilization (Eq. (9.5)) and from the repression of photosynthetic gene expression by sugar signals ([7.13.11](/7.13.11)).

## 9.5. Canopy Photosynthesis and Radiation-Use Efficiency

### 9.5.1. Leaf Area Index and Light in the Canopy

**Definition 9.5.1 (Leaf Area Index)** The ratio of the total (one-sided) area of plant leaves per unit ground area to the ground area is called the **leaf area index** (LAI), a dimensionless quantity.

Light in the canopy declines with depth approximately according to Beer's law (Monsi and Saeki, 1953; the **Lambert–Beer law** applied to the canopy):

$$
I(L) = I_0\,\mathrm{e}^{-kL}, \tag{9.10}
$$
where $L$ is the cumulative leaf area index from the top of the canopy downward, $I_0$ is the light intensity at the top of the canopy and $k$ is the extinction coefficient. $k$ depends on leaf inclination and arrangement: when leaves are nearly horizontal $k$ is about 0.7–1.0 and light is absorbed almost completely in the top few layers of leaves; when leaves are erect $k$ is about 0.3–0.5 and light penetrates deeper. The fraction of light intercepted by the canopy is $1 - \mathrm{e}^{-k\,\mathrm{LAI}}$: for $k = 0.5$, an LAI of 4 intercepts 86%, and intercepting 95% requires an LAI of $\ln 20/0.5 = 6.0$.

Canopy photosynthesis is the sum of photosynthesis of leaves in all layers. Upper leaves are exposed to strong light and nearly saturated, whereas lower leaves are in weak light and photosynthesize roughly in proportion to light intensity. Because the light response of a single leaf is convex, spreading light over more leaves produces more photosynthesis than concentrating it on a few: in a canopy of erect leaves, although the top leaves receive less light, more leaves work on the linear segment of high quantum efficiency, and canopy photosynthesis at high LAI is higher (Figure 4). This is one basis for selecting "plant type" in modern high-yield rice and wheat cultivars: erect, narrow and thick upper leaves and more spreading lower leaves.

![Light and photosynthesis in the canopy (layered model based on Beer's law). Light intensity at the top of the canopy $I_0$ = 1800 µmol m⁻² s⁻¹, extinction coefficient $k$ = 0.4 (erect leaves, green) or 0.8 (horizontal leaves, orange); light absorbed per unit leaf area at depth $L$ is $kI(L)$, and leaves in each layer photosynthesize according to a nonrectangular hyperbola (φ = 0.05, $A_{\max}$ = 30, θ = 0.7, $R_{\mathrm{d}}$ = 1.5 µmol m⁻² s⁻¹); for simplicity leaves in all layers have the same photosynthetic capacity. A: relative light intensity $I/I_0$ (dashed line) and relative net photosynthesis of a single leaf (solid line) against depth: in a canopy of horizontal leaves light declines rapidly and leaves below an LAI of about 5 are already below the light compensation point. B: canopy net photosynthesis (integrated over layers, less respiration of nonleaf organs such as stems and roots taken as 1 µmol m⁻² s⁻¹ per unit LAI) against LAI; the canopy of horizontal leaves is highest at an LAI of about 4.2 and the canopy of erect leaves at about 6.6, with a higher maximum. Parameters are schematic values](./plots/canopy.py)

When LAI is too large, lower leaves are below the light compensation point and their respiration instead consumes carbon, so that canopy net photosynthesis falls (Figure 4B); lower leaves also senesce early, ventilation and light penetration in the field are poor, disease worsens and lodging is more likely. The optimum LAI of most field crops is about 4–6 (Chinese textbooks often give 5–7, depending on crop and plant type). The aim of rational planting density is to bring LAI as quickly as possible to a level that intercepts most of the light, and to maintain it in the late growth period without letting it become too large.

### 9.5.2. Radiation-Use Efficiency

**Definition 9.5.2 (Radiation-Use Efficiency)** The ratio of the chemical energy contained in the organic matter accumulated by a plant through photosynthesis over a period to the solar radiation falling on the same ground area in the same period is called the **radiation-use efficiency**. Crop physiology also often uses another definition, the dry matter produced per unit photosynthetically active radiation intercepted (radiation-use efficiency in the sense of $\mathrm{g\,MJ^{-1}}$).

Monteith (1977) found that, in a crop without water or nutrient shortage, dry matter accumulation is proportional to the cumulative radiation intercepted by the canopy, with a proportionality coefficient that is fairly stable within a crop type. This gives a simple decomposition of crop yield:

$$
Y = \varepsilon_{\mathrm{c}}\,\sum_t f_{\mathrm{i}}(t)\,S(t) \times \mathrm{HI}, \tag{9.11}
$$
where $S(t)$ is the daily photosynthetically active radiation, $f_{\mathrm{i}}$ is the fraction intercepted by the canopy (determined by LAI and Eq. (9.10)), $\varepsilon_{\mathrm{c}}$ is the radiation-use efficiency, and $\mathrm{HI}$ is the **harvest index**, the fraction of grain in aboveground dry matter, also called the economic coefficient in Chinese textbooks. Per unit PAR intercepted, $\varepsilon_{\mathrm{c}}$ is about 2.5–3 $\mathrm{g\,MJ^{-1}}$ for C3 crops and about 3.3–4 $\mathrm{g\,MJ^{-1}}$ for C4 crops. Equation (9.11) shows that yield has only four levers: radiation (season and place), interception (the speed and duration of canopy establishment), conversion efficiency (photosynthesis itself) and partitioning (harvest index).

**Example 9.5.1** A wheat season lasts 100 d with a mean daily total radiation of $20\,\mathrm{MJ\,m^{-2}}$, PAR 48% of it, and mean canopy interception of 80%. The PAR intercepted is $100 \times 20 \times 0.48 \times 0.80 = 768\,\mathrm{MJ\,m^{-2}}$; taking $\varepsilon_{\mathrm{c}} = 2.8\,\mathrm{g\,MJ^{-1}}$, aboveground dry matter is $2150\,\mathrm{g\,m^{-2}}$ (21.5 t/ha); with a harvest index of 0.45 grain is about 9.7 t/ha, near the level of high-yielding wheat. Taking the heat of combustion of dry matter as $17.5\,\mathrm{kJ\,g^{-1}}$, the energy contained in the biomass is $37.6\,\mathrm{MJ\,m^{-2}}$ against a total radiation of $2000\,\mathrm{MJ\,m^{-2}}$ in the same period, so the radiation-use efficiency is only 1.9%; calculated on the radiation of a whole year it is much lower, because for much of the year the field has no green canopy.

### 9.5.3. The Theoretical Upper Limit of Light Conversion

Why is the radiation-use efficiency so low? Zhu, Long and Ort (2008) calculated item by item the energy losses from solar radiation to biomass (Figure 5). At 30 °C and $380\,\mathrm{\mu mol\,mol^{-1}}$ $\ce{CO2}$ the theoretical maximum efficiency is 4.6% for C3 crops and 6.0% for C4 crops. The two largest losses are physically and chemically unavoidable: more than half of solar energy lies outside PAR and cannot be absorbed by photosynthetic pigments; even in the ideal case of only 8–10 photons per $\ce{CO2}$, the gap between the energy of a 690 nm photon and the chemical energy in carbohydrate costs about one quarter in carbohydrate synthesis. The difference between C3 and C4 lies in the last two items: C3 loses to photorespiration, C4 to the extra ATP of the C4 cycle.

![Energy losses from solar energy to biomass (calculated after Zhu, Long and Ort, 2008, at 30 °C and CO₂ of 380 µmol mol⁻¹). From the solar energy intercepted by the canopy (100%) are subtracted in turn: radiation outside 400–700 nm (51.3%), reflection and transmission (4.9%), photochemical inefficiency (thermal relaxation of the part of photon energy above what the reaction center needs, 6.6%), carbohydrate synthesis (24.6% for C3 and 28.8% for C4, including the C4 cycle), photorespiration (6.1% for C3, none for C4) and respiration (1.9% and 2.5%). What remains is the maximum conversion efficiency: 4.6% for C3 and about 6% for C4 (5.9% by subtracting the items in the figure). Bars show the energy remaining after each step](./plots/energy-losses.py)

The efficiencies actually achieved in the field are far below this upper limit: the highest values measured over a whole growing season are about 2.4% for C3 crops and 3.7% for C4 crops, and ordinary fields reach only about 1% or less. The statement in Chinese textbooks that "the radiation-use efficiency of plants is generally about 5%" refers to the theoretical upper limit and not to actual field values; another common breakdown of losses ("60% lost in wavelengths that cannot be absorbed, 8% in reflection and transmission, 8% in heat dissipation, 19% in metabolic consumption, 5% stored") is also a rough estimate of the upper limit. The gap between actual values and the upper limit arises from light lost before canopy establishment and after harvest, light saturation (excess light in strong light is dissipated, [7.13.7](/7.13.7#sec-7.4.3)), photoinhibition and stress, and the lag of nonphotochemical quenching in fluctuating light.

### 9.5.4. Ways to Raise Radiation-Use Efficiency

According to the decomposition of Eq. (9.11):

| Approach | Measures | Principle |
|---|---|---|
| Lengthen photosynthetic time | raise the multiple cropping index (ratio of area harvested over a year to arable area; rotation, intercropping, relay cropping); earlier sowing and prolonged leaf functional life; supplementary artificial light in protected cultivation | reduces light lost when there is no canopy |
| Increase photosynthetic area | rational planting density, bringing LAI quickly to and keeping it in the suitable range; improved plant type (dwarf stature, erect leaves, compact tillering) | raises the fraction intercepted and improves light distribution in the canopy |
| Raise photosynthetic efficiency | $\ce{CO2}$ enrichment (about $1000\,\mathrm{\mu mol\,mol^{-1}}$ in greenhouses) and rational nitrogen application; molecular improvement: smaller antenna in upper leaves, faster relaxation of nonphotochemical quenching, engineering of Rubisco and RuBP regeneration (overexpressing sedoheptulose-1,7-bisphosphatase), photorespiratory bypasses, introduction of $\ce{CO2}$-concentrating mechanisms and C4 photosynthesis ([7.13.8](/7.13.8#sec-8.7.2)) | raises $\varepsilon_{\mathrm{c}}$ |
| Reduce losses | lower photorespiration and excessive maintenance respiration; prevent early senescence, pests and diseases and lodging | increases net accumulation |
| Improve partitioning | raise the harvest index; promote transport of assimilates from **source** to **sink** ([7.13.11](/7.13.11)) | the Green Revolution raised harvest index mainly through dwarf cultivars |

Yield increases in the twentieth century came mainly from interception (fertilization, dense planting) and partitioning (harvest index raised from about 0.3 to more than 0.5); these two are near their biological limits, and further increases depend more and more on raising conversion efficiency itself, which is why research on photosynthesis has regained the attention of agriculture. Several molecular improvements have shown effects in the field: accelerating NPQ relaxation raised tobacco biomass by about 15% (Kromdijk et al., 2016), and a photorespiratory bypass inside the chloroplast raised tobacco biomass by 25%–40% (South et al., 2019).

## 9.6. Effects of Elevated Atmospheric CO₂

Atmospheric $\ce{CO2}$ has risen from about $280\,\mathrm{\mu mol\,mol^{-1}}$ before industrialization to about $420\,\mathrm{\mu mol\,mol^{-1}}$ and is expected to exceed $500$ by the middle of this century. For C3 plants $\ce{CO2}$ is the substrate of photosynthesis, so that when it rises carboxylation speeds up and oxygenation is suppressed, and the Farquhar model gives direct predictions.

**Example 9.6.1** Use the leaf of Figure 1 with $c_{\mathrm{i}} = 0.7c_{\mathrm{a}}$. When $c_{\mathrm{a}}$ rises from 420 to $550\,\mathrm{\mu mol\,mol^{-1}}$, $c_{\mathrm{i}}$ rises from 294 to 385. In saturating light: $A_{\mathrm{c}}(294) = 80 \times 251.25/1004.3 - 1 = 19.0$ and $A_{\mathrm{c}}(385) = 80 \times 342.25/1095.3 - 1 = 24.0$, while $A_{\mathrm{j}}(385) = 26.3$ and $A_{\mathrm{p}} = 26$, so the leaf is still Rubisco-limited and photosynthesis rises by 26%. In weak light ($J = 86$): $A_{\mathrm{j}}(294) = 86 \times 251.25/(1176 + 342) - 1 = 13.2$ and $A_{\mathrm{j}}(385) = 86 \times 342.25/(1540 + 342) - 1 = 14.6$, a rise of only 11%. The increase is larger when Rubisco is limiting than when RuBP regeneration is, because the latter benefits only from the reduction in photorespiration.

Free-air $\ce{CO2}$ enrichment (FACE) experiments raise $\ce{CO2}$ around crops and forests in the field to about $550\text{–}600\,\mathrm{\mu mol\,mol^{-1}}$, and the results broadly agree with the model predictions: light-saturated photosynthesis of C3 plants rises by about 30%, stomatal conductance falls by about 20% and water-use efficiency rises; but the increase in yield is clearly smaller than the increase in photosynthesis, while photosynthesis and yield of C4 crops hardly increase and benefit only in drought through stomatal closure and water saving (Ainsworth and Long, 2005). There are several reasons for the smaller increase: under long-term high $\ce{CO2}$ the Rubisco and nitrogen content of leaves decrease (downregulation or acclimation of photosynthesis, partly from sugar feedback when sink capacity is insufficient, and partly from nitrogen dilution); insufficient nitrogen and phosphorus limit growth; and simultaneously rising temperature and ozone offset part of the gain. High $\ce{CO2}$ also lowers the protein, zinc and iron content of grain of many C3 crops by a few percent (Myers et al., 2014), with adverse effects on the nutrition of people who rely on cereals as staples.

## Summary

| Topic | Key points | Quantities |
|---|---|---|
| Photosynthetic rate | $A = V_{\mathrm{c}} - 0.5V_{\mathrm{o}} - R_{\mathrm{d}}$; gas exchange, half-leaf method, fluorescence, remote sensing | open system $A = u(c_{\mathrm{e}} - c_{\mathrm{o}})/s$, Eq. (9.1) |
| Light response | linear segment (light-limited) → saturation; nonrectangular hyperbola (7.12.32) | light compensation point $I_{\mathrm{c}} \approx R_{\mathrm{d}}/\phi$, Eq. (9.2) (Definition 9.2.1); light saturation point $I_{90} = 10A_{\max}(0.9 - 0.81\theta)/\phi$ (Definition 9.2.2) |
| Sun and shade leaves | same quantum yield; sun leaves have more Rubisco and higher $A_{\max}$ and $R_{\mathrm{d}}$; shade leaves have large antenna and low a/b | compensation points 10–20 and 1–5; C3 crops saturate at 1000–1500 |
| Farquhar model (Definition 9.3.1) | $A = \min(A_{\mathrm{c}}, A_{\mathrm{j}}, A_{\mathrm{p}})$: Rubisco, RuBP regeneration, triose phosphate utilization | Eqs. (9.3)–(9.6); Bernacchi 2001: $K_{\mathrm{c}} = 404.9$, $K_{\mathrm{o}} = 278.4$, $\Gamma^* = 42.75$ |
| $\ce{CO2}$ response | compensation point, carboxylation efficiency, $\ce{CO2}$ saturation point; C3 is $\ce{CO2}$-limited in today's atmosphere | C3 saturation point about 800–1500 µmol mol⁻¹ |
| Supply and demand | operating point = intersection of supply line and demand curve; stomatal limitation $l = 1 - A/A_0$; $c_{\mathrm{i}}$ criterion distinguishes stomatal from nonstomatal limitation | $A = g_{\mathrm{c}}(c_{\mathrm{a}} - c_{\mathrm{i}}) = g_{\mathrm{m}}(c_{\mathrm{i}} - c_{\mathrm{c}})$, Eqs. (9.7), (9.8) |
| Temperature | Arrhenius parameters; C3 optimum 20–30 °C, C4 30–40 °C; C3 quantum yield falls with temperature | Eq. (9.9); quantum-yield crossover about 31 °C in today's atmosphere |
| Water and midday depression | stomatal closure → lower $c_{\mathrm{i}}$; mesophyll damaged in severe cases; midday depression: stomata, high temperature, photoinhibition, feedback, clock | Medlyn stomatal model |
| Canopy (leaf area index, Definition 9.5.1) | Beer's law; erect leaves even out the light distribution; optimum LAI | $I = I_0\mathrm{e}^{-kL}$, Eq. (9.10); suitable LAI about 4–6 |
| Radiation-use efficiency (Definition 9.5.2) | Monteith: dry matter ∝ intercepted radiation; yield = radiation × interception × conversion × partitioning | Eq. (9.11); theoretical limit C3 4.6%, C4 6.0%; field about 1%, highest 2.4% and 3.7% |
| Elevated $\ce{CO2}$ | C3 photosynthesis about +30%, stomatal conductance about −20%, smaller yield increase; C4 basically unchanged; grain nutrition declines | Example 9.6.1 |

Main equations:

- Nonrectangular hyperbola and light compensation point, Eq. (9.2); Farquhar model $A_{\mathrm{c}}$, $A_{\mathrm{j}}$, $A_{\mathrm{p}}$ and $J(I)$, Eqs. (9.3)–(9.6).
- Diffusion: $A = g_{\mathrm{c}}(c_{\mathrm{a}} - c_{\mathrm{i}})$, $A = g_{\mathrm{m}}(c_{\mathrm{i}} - c_{\mathrm{c}})$, Eqs. (9.7), (9.8).
- Temperature: $k(T) = k_{25}\exp[E_{\mathrm{a}}(T - 298.15)/(298.15RT)]$, Eq. (9.9).
- Canopy: $I(L) = I_0\mathrm{e}^{-kL}$, Eq. (9.10); Monteith equation $Y = \varepsilon_{\mathrm{c}}\sum f_{\mathrm{i}}S \times \mathrm{HI}$, Eq. (9.11).

## Questions

1. An understory plant leaf has $R_{\mathrm{d}} = 0.3$, $A_{\max} = 6\,\mathrm{\mu mol\,m^{-2}\,s^{-1}}$, $\phi = 0.055$ and $\theta = 0.8$. Find the light compensation point and the light saturation point (90%). If the mean light intensity on the forest floor is $15\,\mathrm{\mu mol\,m^{-2}\,s^{-1}}$, what is its net daytime photosynthesis approximately? What would happen if it were moved into full sunlight?

   **Answer** By Eq. (9.2), $I_{\mathrm{c}} = 0.3 \times (6 - 0.24)/(0.055 \times 5.7) = 1.728/0.3135 = 5.5\,\mathrm{\mu mol\,m^{-2}\,s^{-1}}$; $I_{90} = 10 \times 6 \times 0.252/0.055 = 275\,\mathrm{\mu mol\,m^{-2}\,s^{-1}}$. At 15, photosynthesis is on the linear segment, $A_{\mathrm{g}} \approx \phi I = 0.83$ (about 0.80 by exact solution of the equation), and net photosynthesis is about $0.5\,\mathrm{\mu mol\,m^{-2}\,s^{-1}}$, positive, so the plant can survive on the forest floor. Moved into full sunlight, photosynthesis could reach at most $A_{\max} - R_{\mathrm{d}} \approx 5.7$ and the great majority of the light absorbed would be excess; with a small xanthophyll cycle pool and limited D1 repair capacity it would suffer severe photoinhibition and photobleaching, the leaf might be damaged within days, and it could adapt only by growing new sun leaves in the new light environment.

2. For the leaf of Example 9.3.1 ($V_{\mathrm{cmax}} = 80$, $R_{\mathrm{d}} = 1$, 25 °C), if the mesophyll conductance is $g_{\mathrm{m}} = 0.15\,\mathrm{mol\,m^{-2}\,s^{-1}}$, what is the actual photosynthetic rate when the measured $c_{\mathrm{i}}$ is $294\,\mathrm{\mu mol\,mol^{-1}}$? By how much is it lower than the estimate that ignores mesophyll conductance?

   **Answer** Eq. (9.3) (in terms of $c_{\mathrm{c}}$) and Eq. (9.8) must both be satisfied: $A = 80(c_{\mathrm{c}} - 42.75)/(c_{\mathrm{c}} + 710.3) - 1 = 0.15(294 - c_{\mathrm{c}})$. By trial: at $c_{\mathrm{c}} = 175$ the left side is $80 \times 132.25/885.3 - 1 = 10.95$ and the right side is $17.85$; at $c_{\mathrm{c}} = 200$ the left side is $12.82$ and the right side $14.10$; at $c_{\mathrm{c}} = 206$ the left side is $13.25$ and the right side $13.20$. Interpolation gives $c_{\mathrm{c}} \approx 206$ and $A \approx 13.2\,\mathrm{\mu mol\,m^{-2}\,s^{-1}}$. Ignoring mesophyll conductance gives $A = A_{\mathrm{c}}(294) = 19.0$, so the actual photosynthesis is about 30% lower, and $c_{\mathrm{i}} - c_{\mathrm{c}} = 13.2/0.15 = 88\,\mathrm{\mu mol\,mol^{-1}}$. Conversely, fitting a measured $A/c_{\mathrm{i}}$ curve with $c_{\mathrm{i}}$ underestimates the true $V_{\mathrm{cmax}}$.

3. The extinction coefficient of a crop canopy is $k = 0.6$. How much of the incident light does the canopy intercept at LAI of 2, 4 and 6? What is the minimum LAI to intercept 90%? Why is a larger LAI not always pursued in production?

   **Answer** The intercepted fraction is $1 - \mathrm{e}^{-k\,\mathrm{LAI}}$: at LAI = 2, $1 - \mathrm{e}^{-1.2} = 70\%$; at 4, $1 - \mathrm{e}^{-2.4} = 91\%$; at 6, $1 - \mathrm{e}^{-3.6} = 97\%$. Intercepting 90% requires $\mathrm{LAI} = \ln 10/0.6 = 3.8$. Increasing LAI from 4 to 6 intercepts only 6% more light, and the added leaves are mostly in the lower canopy near or below the light compensation point; their respiration, construction cost and nutrient demand exceed their photosynthetic gain, so canopy net photosynthesis may even fall (Figure 4B); at the same time a closed canopy is humid and poorly ventilated, disease worsens, lower leaves senesce early, and the stems are thin and prone to lodging.

4. Estimate with the Monteith equation: a maize season lasts 120 d with daily PAR of $10\,\mathrm{MJ\,m^{-2}}$, mean canopy interception of 75%, radiation-use efficiency of $3.5\,\mathrm{g\,MJ^{-1}}$ and harvest index of 0.5. Find the grain yield (t/ha). How much would yield increase if improved plant type raised mean interception to 85%, or if molecular improvement raised $\varepsilon_{\mathrm{c}}$ by 15%?

   **Answer** Intercepted PAR $= 120 \times 10 \times 0.75 = 900\,\mathrm{MJ\,m^{-2}}$, dry matter $900 \times 3.5 = 3150\,\mathrm{g\,m^{-2}}$, grain $1575\,\mathrm{g\,m^{-2}} = 15.75\,\mathrm{t/ha}$. With interception raised to 85%, dry matter and yield increase in the ratio 85/75, by 13.3%, to 17.85 t/ha (a gain of 2.1 t/ha). With $\varepsilon_{\mathrm{c}}$ raised by 15%, yield increases by 15%, to 18.1 t/ha (a gain of 2.4 t/ha). The effects are comparable and can be combined; but in high-yielding fields interception is often already above 85%–90% and there is little room to raise it further, whereas $\varepsilon_{\mathrm{c}}$ is still far from the theoretical upper limit (Figure 5), which is the rationale for current research on improving photosynthesis.

5. Explain: (a) how can the measured $c_{\mathrm{i}}$ be used to decide whether the main cause of the midday depression of photosynthesis is the stomata or the mesophyll? (b) why is the yield-raising effect of elevated atmospheric $\ce{CO2}$ on C3 crops smaller in weak light and low nitrogen? (c) why can $\ce{CO2}$ enrichment in greenhouses raise yields of tomato and cucumber but is seldom used for maize?

   **Answer** (a) If $c_{\mathrm{i}}$ also falls as $A$ falls at midday, $\ce{CO2}$ supply has decreased, mainly because of partial stomatal closure (the supply line flattens); if $A$ falls while $c_{\mathrm{i}}$ is unchanged or even rises, the ability of the mesophyll to use $\ce{CO2}$ has decreased (the demand curve is lowered), for example through photoinhibition, inactivation of Rubisco by high temperature, or product feedback. (b) In weak light photosynthesis is limited by RuBP regeneration (electron transport), and by Eq. (9.4) elevated $\ce{CO2}$ acts only by reducing photorespiration, so the increase is small (11% against 26% in Example 9.6.1); at low nitrogen the amounts of Rubisco and of the whole photosynthetic apparatus are small, growth and sink capacity are also limited by nitrogen, the extra carbon fixed has nowhere to go, and sugar accumulation downregulates photosynthesis. (c) Tomato and cucumber are C3 plants whose photosynthesis is $\ce{CO2}$-limited in today's atmosphere, and raising $\ce{CO2}$ in the greenhouse to about $1000\,\mathrm{\mu mol\,mol^{-1}}$ markedly raises photosynthesis and yield, and a closed greenhouse by day often has $\ce{CO2}$ below atmospheric because of photosynthetic consumption; maize is a C4 plant whose bundle sheath Rubisco is already near $\ce{CO2}$ saturation, so $\ce{CO2}$ enrichment hardly raises its photosynthesis, and maize is also seldom produced in greenhouses.
