---
title: "Course Summary: The Plant as an Integrated System"
description: "Four threads that tie the whole course together: the unified framework flux = conductance × driving force; water–carbon coupling with the stoma as the hub; whole-plant budgets of carbon, water and nitrogen with a worked one-day wheat-field example; the network of signals, hormones and development and the seed-to-seed developmental program; responses to the environment and the trade-offs among them; a table of the main equations of the course with typical values; and links to other courses."
source_hash: a7b557495e32
---

The previous 29 chapters took the plant apart into many processes: how water enters a cell, how ions cross the plasma membrane, how photons become ATP and NADPH, how sucrose flows in sieve tubes, how hormones are synthesized, transported and perceived, how day length is measured, how a seed decides to germinate, how a leaf senesces, and how plants cope with drought, salt, cold, pathogens and herbivores. In a real plant these processes run at the same time and constrain one another. A leaf loses hundreds of water molecules for every $\ce{CO2}$ molecule it takes up; the nitrogen absorbed by roots is carried up in the transpiration stream and assimilated only with energy from photosynthesis; a substantial part of the nitrogen and carbon that fill a grain comes from senescing leaves; and the signals that decide when all this happens travel through the same vascular system. This chapter introduces no new material. It reorganizes the course along a few threads: a unified quantitative framework (Section 30.2), the coupling of water and carbon with the stoma as hub (Section 30.3), whole-plant budgets of carbon, water and nitrogen (Section 30.4), the network of signals, hormones and development (Section 30.5), the seed-to-seed developmental program (Section 30.6), and responses to the environment and their trade-offs (Section 30.7). Section 30.8 collects the main equations of the course in one table, and Section 30.9 lists the links of this course to other courses.

The integrative character of plant physiology is clearest here: the same phenomenon often has to be understood at several scales at once, from molecule to cell, organ, whole plant and population. Take "drought reduces wheat yield." At the molecular scale it is the synthesis of ABA and the activation of SnRK2; at the cellular scale, solute efflux and loss of turgor in guard cells; at the organ scale, a drop in stomatal conductance and the cessation of leaf expansion; at the whole-plant scale, a larger root:shoot ratio and a redistribution of assimilates; at the population scale, lower canopy photosynthesis and a lower harvest index. The tables and figures below are organized in this multiscale way.

## 30.1. Structure of the Course

The 30 chapters fall into nine blocks. Each block answers one central question and comes with a standard set of quantitative tools:

| Block | Chapters | Central question | Main quantitative tools |
|---|---|---|---|
| Introduction | [7.13.1](/7.13.1) | How does a rooted organism carry out its life processes? | Physiological components of yield, Eq. (1.1); flux = conductance × driving force, Eq. (1.2) |
| Water and minerals | [7.13.2](/7.13.2)–[7.13.6](/7.13.6) | How do water and minerals pass from the soil into the plant, reach the leaves and get assimilated? | Water potential, Hagen–Poiseuille, series resistances of the SPAC; electrochemical potential and the Nernst equation; Michaelis–Menten; stoichiometry of assimilation |
| Photosynthesis and carbon metabolism | [7.13.7](/7.13.7)–[7.13.12](/7.13.12) | How is light energy converted into chemical energy, and how is carbon fixed, transported and consumed? | Quantum yield and chlorophyll fluorescence; Farquhar model; Fick diffusion; Beer's law and the Monteith equation; Münch pressure flow; McCree respiration equation |
| Hormones and light signals | [7.13.13](/7.13.13)–[7.13.16](/7.13.16) | How do plants pass information between organs and how do they perceive light? | Synthesis–degradation steady state; Hill dose–response; ion trapping; advection–diffusion; photostationary state $\varphi$ |
| Growth and development | [7.13.17](/7.13.17)–[7.13.20](/7.13.20) | How do cells expand, where do organs arise, how is direction sensed, and when does a seed germinate? | Lockhart equation; RGR decomposition and logistic growth; thermal time; Douady–Couder phyllotaxis model; sine law; hydrotime |
| Reproduction and senescence | [7.13.21](/7.13.21)–[7.13.24](/7.13.24) | When does a plant flower, how do fertilization and seed set occur, and how do plants senesce and shed organs? | Day-length formula and external coincidence model; vernalization dose; logistic grain filling; bistability of the ethylene switch; remobilization efficiency |
| Plants and the environment | [7.13.25](/7.13.25)–[7.13.27](/7.13.27) | How do plants respond to pathogens, herbivores, neighbors and abiotic stress? | van der Plank epidemic model; cascades of induced defense and optimal defense allocation; osmotic adjustment; Maas–Hoffman; water potential of ice |
| Agricultural topics | [7.13.28](/7.13.28)–[7.13.29](/7.13.29) | How does physiological knowledge become crop and breeding technology? | Breeder's equation; domestication bottleneck; heterosis; bending moment of lodging |
| Summary | 7.13.30 | How do these processes form a whole? | This chapter |

The order of the nine blocks is the order in which matter and information flow through the plant: water and minerals must be supplied before photosynthesis and carbon allocation can proceed; hormones and light signals translate environmental information into decisions about growth and development; the developmental program runs through a life cycle in reproduction and senescence; the chapters on plants and the environment ask how this system responds to perturbation; and the two agricultural chapters ask how humans reshape it. Figure 1 draws the main material and signal flows on a single plant.

![Material and signal flows in the whole plant (schematic). Left, matter: water and mineral ions rise through the xylem down a stepwise decreasing water potential (soil about $-0.3\,\mathrm{MPa}$, root about $-0.5\,\mathrm{MPa}$, leaf about $-1.2\,\mathrm{MPa}$, air at 20 °C and 50% relative humidity about $-93\,\mathrm{MPa}$, [7.13.3](/7.13.3)); water vapor leaves and $\ce{CO2}$ enters through the stomata (Eqs. (3.5), (9.7)); sucrose moves in the phloem from source leaves to sinks such as shoot tips, fruits and roots ([7.13.11](/7.13.11)); $\ce{K+}$, $\ce{NO3-}$ and phosphate are taken up by roots from the soil solution ([7.13.4](/7.13.4), [7.13.5](/7.13.5)). Right, signals: ABA, trans-zeatin-type cytokinins and ACC move up from the roots in the xylem ([7.13.14](/7.13.14), [7.13.15](/7.13.15)), florigen FT protein moves from leaves to the shoot apex in the phloem ([7.13.21](/7.13.21)), auxin is transported polarly from the shoot apex toward the base and maintains apical dominance ([7.13.13](/7.13.13), [7.13.18](/7.13.18)), phytochromes, cryptochromes and phototropins perceive light in the leaf ([7.13.16](/7.13.16)), and strigolactones made in the roots inhibit axillary bud outgrowth ([7.13.15](/7.13.15)). The same vascular system carries both matter and signals](./plots/plant-flows.py)

## 30.2. A Unified Quantitative Framework: Flux = Conductance × Driving Force

### 30.2.1. Transport Processes

Eq. (1.2) of Chapter 1, $J = g\,\Delta X = \Delta X/r$, is the first quantitative principle that runs through the whole course: any flow of matter or energy can be written as a driving force divided by a resistance, where the driving force is a difference in some potential (water potential, concentration, electrochemical potential, pressure) and the resistance is set by the geometry and material properties of the pathway. Resistances of pathway segments in series add, so the flux is controlled by the largest resistance; conductances of parallel pathways add. The table below places the transport processes of the course in this framework:

| Process | Flux | Driving force | Determinant of conductance (or resistance) | Equation | Typical values |
|---|---|---|---|---|---|
| Water across membranes | Volume flux $J_V$ | Water potential difference $\Delta\Psi_{\mathrm{w}}$ | Membrane hydraulic conductivity $L_p$ (aquaporins) | Eq. (2.7); with osmotic solutes Eq. (2.3) | $L_p \sim 10^{-7}$–$10^{-6}\,\mathrm{m\,s^{-1}\,MPa^{-1}}$; cell $t_{1/2}$ 1–10 s, Eq. (2.8) |
| Water in soil and root | Liquid flow | $\Psi_{\mathrm{soil}} - \Psi_{\mathrm{root}}$ | Soil hydraulic conductivity (falls steeply on drying); endodermis and aquaporins | Eq. (3.7) | Field capacity $-0.01$ to $-0.033\,\mathrm{MPa}$; wilting point about $-1.5\,\mathrm{MPa}$ |
| Xylem bulk flow | Volume flow rate $Q$ | Pressure gradient $\Delta\Psi_{\mathrm{p}}/\Delta x$ | Vessel radius ($Q \propto r^4$), pits and perforation plates | Eq. (3.2) | About $0.02\,\mathrm{MPa\,m^{-1}}$ at $r = 40\,\mu\mathrm{m}$ and $4\,\mathrm{mm\,s^{-1}}$ |
| Liquid phase of the whole plant | Transpiration stream $E$ | $\Psi_{\mathrm{soil}} - \Psi_{\mathrm{leaf}} - \rho_{\mathrm{w}}gh$ | Whole-plant hydraulic conductance $K_{\mathrm{plant}}$ (leaf about 30%) | Eqs. (3.7), (27.3) | Leaf water potential $-0.2$ to $-2.5\,\mathrm{MPa}$ |
| Transpiration (gas phase) | $E$ | Water vapor mole fraction difference $\Delta w$ | Stomatal and boundary layer conductances in series | Eq. (3.5); single-pore diffusion Eqs. (10.1), (10.2) | $E \sim 1$–$10\,\mathrm{mmol\,m^{-2}\,s^{-1}}$ |
| $\ce{CO2}$ diffusion | Net photosynthesis $A$ | $c_{\mathrm{a}} - c_{\mathrm{i}}$, $c_{\mathrm{i}} - c_{\mathrm{c}}$ | Stomatal conductance $g_{\mathrm{c}} = g_{\mathrm{s}}/1.6$, mesophyll conductance $g_{\mathrm{m}}$ | Eqs. (9.7), (9.8) | $A \sim 10$–$30\,\mu\mathrm{mol\,m^{-2}\,s^{-1}}$ |
| Sieve-tube bulk flow | Velocity $u$ | Source–sink turgor difference | Sieve-tube radius and sieve plates ($u \propto a^2$) | Eqs. (11.1)–(11.3) | About $0.08\,\mathrm{MPa\,m^{-1}}$ at $a = 10\,\mu\mathrm{m}$; about $1\,\mathrm{m\,h^{-1}}$ |
| Ion transport across membranes | Ion flux | $V_{\mathrm{m}} - E_j$ (electrochemical potential difference) | Number and gating of channels and carriers | Eqs. (5.1)–(5.4) | $V_{\mathrm{m}}$ $-100$ to $-200\,\mathrm{mV}$; $\Delta p \approx -250\,\mathrm{mV}$ |
| Nutrient arrival at the root surface | Mass flow $J_{\mathrm{w}}C$ and diffusion | Transpiration stream; concentration gradient at the root surface | Effective diffusion coefficient and buffer power $b$ of the soil | Example 4.5.1; $L \approx \sqrt{2D_{\mathrm{e}}t/b}$ | Depletion zone 0.2–2 mm |
| Polar auxin transport | Auxin flux | Concentration gradient + directed PIN efflux | Polarly localized PIN and ABCB | Eq. (13.6); Péclet number $vL/D$ | About 5–20 mm/h |
| $\ce{O2}$ in aerenchyma | Diffusive flux | $C_0 - C(z)$ | Porosity $\varphi$; root respiration $Q$ | Eq. (27.4) | $\ce{O2}$ diffuses about $10^4$ times more slowly in water than in air |
| Cell expansion | Relative volume growth rate | Turgor in excess of the yield threshold, $P - Y$ | Wall extensibility $\phi$ (expansins, acid growth) | Eqs. (17.2)–(17.4) | $Y$ about 0.1–0.5 MPa |

Three points deserve emphasis. First, long-distance transport has to be bulk flow: diffusion time grows with the square of distance ($t \sim L^2/D$), so glucose diffuses $50\,\mu\mathrm{m}$ in only about 2.5 s but 1 m in about 32 years ([7.13.2](/7.13.2)); cells therefore rely on diffusion and membrane transport, while organs and the whole plant rely on pressure-driven bulk flow in xylem and phloem. Second, the conductance of bulk flow is extremely sensitive to conduit radius (xylem $r^4$, sieve tube $a^2$), which gives wide vessels an enormous advantage in hydraulic efficiency and is the source of the efficiency–safety trade-off of Section 30.7. Third, in the gas phase the largest adjustable resistance is the stoma: it controls both $E$ and $A$, and so becomes the hub of water–carbon coupling (Section 30.3).

Cell expansion is also written as "flux = conductance × driving force": in the Lockhart equation the relative rate of volume increase equals extensibility times effective turgor, and effective turgor in turn depends on whether water can enter the cell (Eqs. (17.3), (17.4)), so growth itself is a water transport problem. This ties the chapters on water relations to those on growth and development.

### 30.2.2. Recurring Mathematical Forms

Besides the transport equations, a few mathematical forms recur throughout the course. Recognizing them lets us see the models of different chapters as the same kind of problem:

| Mathematical form | Equation | Where it appears | Meaning of the parameters |
|---|---|---|---|
| Saturation kinetics | $v = V_{\max}S/(K + S)$ | Biphasic uptake Eq. (5.5); $A_{\mathrm{c}}$ in the Farquhar model, Eq. (9.3); non-rectangular hyperbola of the light response | $K$: half-saturation concentration, a measure of affinity; $V_{\max}$: capacity |
| Hill dose–response | $\theta = c^n/(K^n + c^n)$ | Hormone dose–response Eq. (13.2); GID1 occupancy Eq. (14.1); triple response Eq. (15.3); auxin gradient in abscission Eq. (24.3) | $\mathrm{EC}_{50}$ or $K$: sensitivity; $n$: steepness |
| Bell-shaped dose–response | Promotion term × inhibition term | Auxin Eq. (13.7), $c_{\mathrm{opt}} = \sqrt{K_1K_2}$ | Optimal concentrations of root, bud and stem differ by several orders of magnitude |
| First-order kinetics and steady state | $\mathrm{d}c/\mathrm{d}t = s - kc$ | Hormone homeostasis Eq. (13.1), Example 15.2.1; photoinhibition Eq. (7.9); dark decay of Pfr Eq. (16.4); pollen viability Eq. (23.1); storage life Eq. (24.5) | Steady state $s/k$; half-life $\ln 2/k$; steady state reached in about $3/k$ |
| Logistic and S-shaped curves | $\dot W = rW(1 - W/K)$ | Grand period of growth Eqs. (17.9), (17.10); grain filling Eqs. (23.3), (23.4); leaf senescence Eq. (24.1); disease epidemics Eqs. (25.1)–(25.4) | Inflection at $K/2$, maximum rate $rK/4$ |
| Bistable switch | Positive feedback + degradation | Ethylene system 2, Eq. (23.5); LFY–AP1; digital silencing of *FLC* | A saddle-node bifurcation makes the decision irreversible |
| Oscillator and delayed negative feedback | Cyclic repression | Circadian clock Eq. (16.8); pollen tube growth oscillation Eq. (23.2); root clock $\lambda = vT$ | Period set by the delay and the degradation rate |
| Threshold accumulation | $\sum$ effective amount $\ge$ threshold | Thermal time Eq. (17.12); vernalization dose Eq. (22.1); hydrotime and hydrothermal time Eqs. (20.1)–(20.3); number of cycles for photoperiodic induction | Developmental rate = 1/required accumulated amount |
| Optimization | Marginal benefit = marginal cost | Cowan–Farquhar condition for stomata Eq. (10.6); optimal defense allocation Eqs. (26.5), (26.6); economically optimal fertilizer rate (Eq. (4.1)) | Lagrange multiplier $\lambda$: marginal carbon price of water |

These forms are related to models elsewhere in biology: saturation kinetics comes from enzyme kinetics ([7.1](/7.1)), logistic and epidemic models from population dynamics, the dynamics of switches and oscillators is in [7.6.33](/7.6.33), the statistics of probit and threshold models is in [7.7](/7.7), and ordinary differential equations themselves are in [2.4](/2.4).

![Time scales of plant processes (logarithmic time axis; values taken from the chapters). Movement: the Venus flytrap closes in about a tenth of a second and the sensitive plant droops in about 1 s ([7.13.19](/7.13.19)). Water: half-time for a cell to equilibrate its water potential with the surroundings 1–10 s (Eq. (2.8)), stomata open and close within minutes ([7.13.10](/7.13.10)), glucose diffusion over 1 m about 32 years ([7.13.2](/7.13.2)). Signals: the flg22-induced reactive oxygen burst starts after 2–5 min and peaks at 10–15 min ([7.13.25](/7.13.25)), phytochrome-mediated transcriptional changes appear within about 5 min at the fastest ([7.13.16](/7.13.16)), ABA in drought-stressed leaves rises about 50-fold within 4–8 h ([7.13.15](/7.13.15)), the free-running circadian period is about 24.7 h. Growth: the lag of acid growth after auxin addition 10–15 min ([7.13.17](/7.13.17)), root gravitropic bending about 1 h to several hours. Carbon: phloem transport of sucrose at about $0.3$–$1.5\,\mathrm{m\,h^{-1}}$ ([7.13.11](/7.13.11)). Biotic stress: systemic acquired resistance is established within 1–2 d. Development: photoperiodic induction needs 1 to about 12 cycles ([7.13.21](/7.13.21)), vernalization needs a few days to two or three months of cold ([7.13.22](/7.13.22)), the life cycle of an annual crop is a few months, the longevity of orthodox seeds ranges from a few years to a thousand years ([7.12.19](/7.12.19)), and the oldest bristlecone pines exceed 4800 years ([7.13.24](/7.13.24)). Plant life spans about 12 orders of magnitude in time](./plots/timescales.py)

## 30.3. Coupling of Water and Carbon: The Stoma as Hub

### 30.3.1. Why Water Is Lost in Much Greater Amounts than Carbon Is Gained

**Photosynthesis** requires the moist cell surfaces inside the leaf to be connected to the atmosphere, and any pathway through which $\ce{CO2}$ can enter is one through which water vapor can leave. Eq. (3.6) gives this exchange ratio quantitatively:

$$
\frac{A}{E} = \frac{c_{\mathrm{a}}(1 - c_{\mathrm{i}}/c_{\mathrm{a}})}{1.6\,\Delta w}.
$$

Take $c_{\mathrm{a}} = 420\,\mu\mathrm{mol\,mol^{-1}}$, $c_{\mathrm{i}}/c_{\mathrm{a}} = 0.7$ and a leaf-to-air vapor pressure deficit $D = 1.5\,\mathrm{kPa}$ ($\Delta w = D/p \approx 0.015$). Then $A/E \approx 126\times10^{-6}/0.024 \approx 5.3\times10^{-3}$, that is, about 190 water molecules are transpired for each $\ce{CO2}$ fixed; with drier air or a warmer leaf, $\Delta w$ increases and this number rises above 400. There are three reasons ([7.13.3](/7.13.3)): the vapor concentration difference for water is about 50 times that for $\ce{CO2}$; the diffusion coefficient of $\ce{CO2}$ is about 1.6 times smaller than that of water vapor; and $\ce{CO2}$ must also cross the liquid-phase resistance of the mesophyll. **Transpiration** is therefore not a by-product of photosynthesis but its unavoidable cost, and **water-use efficiency** (Definition 3.4.2) is the central measure of how well a plant performs under this cost.

### 30.3.2. Three Photosynthetic Types: Three Solutions to the Same Dilemma

C3, C4 and CAM plants can be seen as three solutions to this dilemma, differing in $c_{\mathrm{i}}/c_{\mathrm{a}}$, energy cost and timing:

| | C3 (Definition 8.1.1) | C4 (Definition 8.3.1) | CAM (Definition 8.4.1) |
|---|---|---|---|
| Solution | No $\ce{CO2}$ concentration; a larger stomatal conductance maintains $c_{\mathrm{i}}$ | Spatial separation of two carboxylations, concentrating $\ce{CO2}$ in the bundle sheath to 8–10 times the atmospheric level | Temporal separation: stomata open at night to fix $\ce{CO2}$ and close by day while the acid is decarboxylated |
| $c_{\mathrm{i}}/c_{\mathrm{a}}$ | About 0.7 | About 0.3–0.4 | Low at night, very high by day (with stomata closed) |
| Photorespiration | 15%–30% of carbon | 2%–3% | Low |
| ATP per $\ce{CO2}$ | 3 (without photorespiration), Eq. (8.4) | $3 + 2/(1 - \varphi)$, Eq. (8.5) | About 6.5 |
| $\ce{CO2}$ compensation point / $\mu\mathrm{mol\,mol^{-1}}$ | 40–100, Eq. (8.2) | 0–10 | 0–5 in the dark |
| Transpiration ratio (molar, Definition 3.4.2) | About 400 | About 150 | About 50 |
| $\delta^{13}\mathrm{C}$ | About −28‰ | About −14‰ | Between the two |
| Optimum temperature | 20–30 °C | 30–40 °C | — |
| Examples | Wheat, rice, soybean | Maize, sugarcane, sorghum | Pineapple, cacti, stonecrops |

The common principle of C4 and CAM is to spend extra ATP to saturate Rubisco at a lower $c_{\mathrm{i}}$, so that the same photosynthetic rate is obtained with a smaller stomatal conductance. They dominate under high temperature, strong light and drought, and have no advantage under low temperature and weak light, because the quantum yield of C3 falls below that of C4 only at high temperature (the crossover is at about 31 °C in today's atmosphere, [7.13.9](/7.13.9)). Carbon isotope discrimination $\Delta$ records the mean $c_{\mathrm{i}}/c_{\mathrm{a}}$ during growth (Eq. (8.8)) and hence also water-use efficiency (Eq. (8.10)), which makes low $\Delta$ a selection criterion for water-saving breeding.

### 30.3.3. How Stomata Make the Trade-off

For a C3 leaf, combining the demand curve of the Farquhar model (Eqs. (9.3)–(9.6)) with the diffusional supply line $A = g_{\mathrm{c}}(c_{\mathrm{a}} - c_{\mathrm{i}})$ (Eq. (9.7)) gives the operating point at any stomatal conductance. Figure 2 shows that as the stomata open wider, $A$ approaches saturation (limited by Rubisco and RuBP regeneration) while $E$ rises almost linearly, so water-use efficiency falls as stomata open; the drier the air, the lower the efficiency at a given conductance. The optimal behavior of a stoma is therefore a marginal trade-off between "one more unit of carbon gained" and "one more unit of water lost." The Cowan–Farquhar condition $\partial E/\partial A = \lambda$ (Eq. (10.6)) requires that the carbon gained per additional unit of water lost stay constant through the day, and the Medlyn model derived from it (Eqs. (10.4), (10.5)) predicts $c_{\mathrm{i}}/c_{\mathrm{a}} = g_1/(g_1 + \sqrt{D})$: the drier the air, the more the stomata close and the lower $c_{\mathrm{i}}/c_{\mathrm{a}}$ becomes.

![The stoma as the hub of water–carbon coupling (C3 leaf; Farquhar model with $V_{\mathrm{cmax}} = 80$, $J = 150$, $R_{\mathrm{d}} = 1\,\mu\mathrm{mol\,m^{-2}\,s^{-1}}$, 25 °C constants of Bernacchi 2001, $c_{\mathrm{a}} = 420\,\mu\mathrm{mol\,mol^{-1}}$, mesophyll resistance neglected; boundary layer conductance $3\,\mathrm{mol\,m^{-2}\,s^{-1}}$). A: net photosynthesis $A$ (solid line) and transpiration $E$ (dashed line, right axis) as functions of stomatal conductance $g_{\mathrm{s}}$ at $D = 1.5\,\mathrm{kPa}$: as $g_{\mathrm{s}}$ increases from 0.25 to $0.5\,\mathrm{mol\,m^{-2}\,s^{-1}}$, $A$ rises only from about 19.2 to 22.1 while $E$ rises from about 3.4 to $6.4\,\mathrm{mmol\,m^{-2}\,s^{-1}}$. B: $c_{\mathrm{i}}/c_{\mathrm{a}}$ at the operating point, about 0.7, typical of a C3 leaf, at $g_{\mathrm{s}} \approx 0.25$. C: water-use efficiency $A/E$ at three vapor pressure deficits: it falls as stomata open and is approximately inversely proportional to $D$. This is the physiological basis for stomata partly closing at a dry noon and opening fully on a humid morning (Eqs. (10.4)–(10.6))](./plots/stomatal-hub.py)

Stomata receive signals from the whole plant and are the endpoint of integration:

| Signal | Source | Effect | Main molecules | Chapter |
|---|---|---|---|---|
| Blue light | Environment (sensed directly by guard cells) | Opening | phot1/2 → BLUS1 → PP1 → H⁺-ATPase | [7.13.10](/7.13.10), [7.13.16](/7.13.16) |
| Low $c_{\mathrm{i}}$ / high $c_{\mathrm{i}}$ | Mesophyll photosynthesis | Opening / closing | βCA1/4, HT1 | [7.13.10](/7.13.10) |
| High VPD, lower leaf water potential | Atmosphere, xylem tension | Closing | Hydraulic signal and ABA made in the leaf | [7.13.10](/7.13.10), [7.13.15](/7.13.15) |
| Soil drought | Roots | Closing | Xylem ABA and pH alkalinization, Tardieu–Davies model Eq. (15.1) | [7.13.15](/7.13.15) |
| Bacterial PAMPs | Pathogens | Closing (stomatal immunity) | FLS2 → OST1; coronatine reopens stomata | [7.13.25](/7.13.25) |
| High $\ce{CO2}$ during growth | Atmosphere | Lower stomatal density | EPF, STOMAGEN | [7.13.10](/7.13.10) |
| Circadian clock | Endogenous | Opening in anticipation of dawn | CCA1/LHY, TOC1 | [7.13.16](/7.13.16) |

At the whole-plant scale the same trade-off appears as two strategies, isohydric and anisohydric (Definition 27.4.2): the former closes stomata early and protects leaf water potential and xylem safety, the latter lets leaf water potential fall to keep photosynthesizing, at the cost of a risk of cavitation ($P_{50}$ and safety margin, Eq. (3.3)). About 70% of tree species have a safety margin of less than 1 MPa ([7.13.3](/7.13.3)), which shows that plants generally operate close to their hydraulic limits.

## 30.4. Whole-Plant Budgets of Carbon, Water and Nitrogen

### 30.4.1. Carbon: From Photons to Grain

The physiological components of yield (Eqs. (1.1), (9.11)) decompose yield into four factors: radiation, interception, conversion and partitioning. Chaining the efficiencies of the chapters gives a full account of how solar energy becomes grain:

| Step | Loss or efficiency | Basis | Chapter |
|---|---|---|---|
| Total solar radiation → photosynthetically active radiation | PAR is only about 48% | 400–700 nm | [7.13.7](/7.13.7) |
| Canopy interception | 85%–90% or more at LAI 4–6; far lower as an annual mean | Beer's law, Eq. (9.10) | [7.13.9](/7.13.9) |
| Leaf absorption | About 85% of PAR is absorbed | Reflection and transmission | [7.13.7](/7.13.7) |
| Photons → fixed $\ce{CO2}$ | Theoretical quantum requirement 8, measured about 9.4; excess energy of blue photons is lost in internal conversion | Eq. (7.2) | [7.13.7](/7.13.7) |
| Photorespiration (C3) | Loses 15%–30% of carbon | $\phi = 2\Gamma^*/c_{\mathrm{c}}$, Eq. (8.1) | [7.13.8](/7.13.8) |
| Heat dissipation in strong light | More than half of the absorbed light becomes heat in full sun | NPQ, Eqs. (7.5), (7.8) | [7.13.7](/7.13.7) |
| Respiration | 30%–60% of the carbon fixed each day (growth + maintenance respiration) | Eqs. (12.2), (12.3) | [7.13.12](/7.13.12) |
| Partitioning to harvested organs | Harvest index: about 0.3 in traditional varieties, about 0.5 in semidwarf varieties | Source–sink relations and sink strength, Eq. (11.4) | [7.13.11](/7.13.11), [7.13.14](/7.13.14), [7.13.28](/7.13.28) |
| Total | Theoretical upper limit: C3 4.6%, C4 6.0%; in the field about 1%, at most 2.4% and 3.7% | **Light-use efficiency** (Definition 9.5.2) | [7.13.9](/7.13.9) |

This account explains why different routes to improvement have different potential. The Green Revolution raised the harvest index from about 0.3 to 0.5 through semidwarfing ([7.13.28](/7.13.28)), a lever that is nearly exhausted in high-yielding varieties; canopy interception in high-yield fields is already above 85%–90%; the largest remaining room is in the conversion efficiency itself, that is, photorespiration, the relaxation rate of photoprotection and the properties of Rubisco ([7.13.8](/7.13.8), [7.13.9](/7.13.9)).

Carbon moves through the plant as a source-to-sink network: mature leaves are sources; shoot tips, young leaves, root tips, fruits and seeds are sinks ([7.13.11](/7.13.11)). The pressure-flow hypothesis links loading at the source, unloading at the sink and bulk flow in the sieve tubes into one whole: loading at the source lowers water potential and raises turgor, unloading at the sink lowers turgor, and the turgor difference drives bulk flow (Definition 11.6.1). Assimilate partitioning is therefore determined mainly by the sink: **sink strength** = sink size × sink activity (Eq. (11.4)), and sink activity is in turn regulated by hormones (cytokinins, auxin, gibberellins, ABA) and sugar signals. Correlative growth (Definition 18.8.1), the sugar supply to buds in apical dominance ([7.13.18](/7.13.18)), the filling of seeds and fruits ([7.13.23](/7.13.23)) and whole-plant senescence in monocarpic plants ([7.13.24](/7.13.24)) are all manifestations of the same source–sink network at different stages.

### 30.4.2. Water

The water budget is highly asymmetric: about 97% of the water taken up by roots is lost by evaporation from the leaves, about 2% stays in the plant for growth, and only about 1% takes part in metabolism ([7.13.2](/7.13.2)). The energy for transpiration comes from the sun, and the plant spends almost no metabolic energy on it; the cost to the plant is building and maintaining the pipes that carry the water (xylem) and the photosynthesis lost when stomata close under water shortage. The transpiration stream is at the same time a conveyor belt for nutrients (mass flow), a coolant for the leaf (heat of vaporization $44\,\mathrm{kJ\,mol^{-1}}$) and a channel for root-derived signals (ABA, cytokinins, ACC). So reducing transpiration is not always beneficial: too little transpiration raises leaf temperature and reduces the nitrogen supplied by mass flow.

### 30.4.3. Nitrogen and Minerals

| Step | Key points | Quantity | Chapter |
|---|---|---|---|
| Arrival at the root surface | Mass flow ($\ce{NO3-}$, part of $\ce{K+}$) and diffusion (phosphorus, potassium); continued root growth and mycorrhizae reach beyond depletion zones | Example 4.5.1: mass flow supplies a substantial fraction of nitrogen but less than 1% of the phosphorus required | [7.13.4](/7.13.4) |
| Entry into cells | Secondary active transport driven by the proton motive force; biphasic uptake by HATS and LATS | Eqs. (5.4), (5.5); HATS for $\ce{NO3-}$ about $50\,\mu\mathrm{M}$ | [7.13.5](/7.13.5) |
| Assimilation | Nitrate reductase → nitrite reductase → GS–GOGAT | About 12 ATP equivalents per nitrate incorporated into glutamine | [7.13.6](/7.13.6) |
| Symbiotic nitrogen fixation | Nitrogenase 16 ATP/$\ce{N2}$; host supplies malate | More than about 4 g of carbon per gram of nitrogen (6–7 g including nodule maintenance) | [7.13.6](/7.13.6), [7.13.26](/7.13.26) |
| Transport within the plant and reuse | Xylem upward; phloem bidirectional; N, P, K, Mg are reutilizable, Ca, B, Fe are not | Deficiency site: mobile elements show first in old leaves | [7.13.4](/7.13.4), [7.13.5](/7.13.5) |
| Remobilization during senescence | Rubisco degraded by plastid proteases and autophagy, amino acids exported to seeds in the phloem | Remobilization efficiency about 50%, Eq. (24.2) | [7.13.24](/7.13.24) |
| Root–shoot coordination | The plant grows the organs that acquire what is lacking | Functional balance, Eq. (17.13); root:shoot ratio rises under N or P deficiency | [7.13.17](/7.13.17), [7.13.18](/7.13.18) |
| Use efficiency | Nitrogen-use efficiency = uptake efficiency × internal utilization efficiency | Crops usually take up less than half of the applied fertilizer | [7.13.4](/7.13.4), [7.13.6](/7.13.6) |

Nitrogen is tightly coupled to carbon: a large part of leaf nitrogen is in the photosynthetic machinery (Rubisco is the most abundant protein in the leaf), so photosynthetic capacity rises with leaf nitrogen content; the ATP, reducing power and carbon skeletons needed to assimilate nitrogen in turn come from photosynthesis and respiration. Over the life of a plant the same nitrogen first builds the photosynthetic machinery of leaves during vegetative growth and then is transferred from senescing leaves to the seeds during grain filling; this is the trade-off between early senescence and grain protein (*NAM-B1*, [7.13.24](/7.13.24)).

### 30.4.4. A Wheat Field on One Sunny Day

**Example 30.4.1** Estimate the carbon, water and nitrogen budgets per square meter of ground for a high-yielding wheat field on one sunny day after heading. Let the daily total radiation be $20\,\mathrm{MJ\,m^{-2}}$ with PAR 48% of it; leaf area index $L = 5$ and extinction coefficient $k = 0.5$; radiation-use efficiency per unit intercepted PAR $\varepsilon_{\mathrm{c}} = 2.8\,\mathrm{g\,MJ^{-1}}$ ([7.13.9](/7.13.9), Example 9.5.1); dry matter contains 45% carbon and 1.5% nitrogen ([7.13.4](/7.13.4)); and the soil solution contains $2\,\mathrm{mmol\,L^{-1}}$ of $\ce{NO3-}$ (Example 4.5.1).

Carbon: the fraction intercepted is $1 - \mathrm{e}^{-kL} = 1 - \mathrm{e}^{-2.5} = 0.92$ (Eq. (9.10)), so intercepted PAR $= 20 \times 0.48 \times 0.92 = 8.8\,\mathrm{MJ\,m^{-2}}$; the dry matter increment is $8.8 \times 2.8 \approx 25\,\mathrm{g\,m^{-2}\,d^{-1}}$, containing $11.1\,\mathrm{g}$ of carbon, that is, $0.93\,\mathrm{mol\,C}$. The value $\varepsilon_{\mathrm{c}}$ is an efficiency after respiration; if respiration consumes 40% of the carbon fixed (the midpoint of the 30%–60% of [7.13.12](/7.13.12)), the canopy assimilated a total of $0.93/0.6 = 1.54\,\mathrm{mol\,CO_2\,m^{-2}}$ that day, which averaged over a 12 h day is about $36\,\mu\mathrm{mol\,m^{-2}\,s^{-1}}$ (per unit ground area). A single leaf photosynthesizes at about $20\,\mu\mathrm{mol\,m^{-2}\,s^{-1}}$, and with light decreasing through five layers of leaves in the canopy this order of magnitude is reasonable.

Water: the transpiration ratio varies with the dryness of the air: at $D = 1.5\,\mathrm{kPa}$ and $c_{\mathrm{i}}/c_{\mathrm{a}} = 0.7$ it is about 190 (Section 30.3.1, Figure 2), and in hot dry weather it can reach 400. The canopy therefore transpires 290–620 mol of water for the $1.54\,\mathrm{mol}$ of $\ce{CO2}$ assimilated, that is, 5–11 kg, equivalent to a 5–11 mm layer of water. About 97% of this water merely passes through the plant. The transpiration coefficient of wheat (500–800 g of water per gram of dry matter, Definition 3.4.2) gives 12–20 kg: the two estimates differ by about a factor of two, showing that such coefficients vary strongly with weather and growth stage and give only the order of magnitude.

Nitrogen: the dry matter increment contains $25 \times 0.015 = 0.37\,\mathrm{g}$ of nitrogen, that is, $26\,\mathrm{mmol\,N}$. The 5–11 L of transpired water brings 10–22 mmol of $\ce{NO3-}$ by mass flow, about 40%–85% of the requirement, and the rest comes from diffusion and root growth ([7.13.4](/7.13.4)). Assimilating this nitrate needs about $26 \times 12 \approx 0.32\,\mathrm{mol}$ of ATP equivalents, while fixing $\ce{CO2}$ in the Calvin cycle that day requires at least $1.54 \times 3 \approx 4.6\,\mathrm{mol}$ of ATP: the energy cost of nitrogen assimilation is about 7% of that of carbon fixation, and in leaves it is largely supplied directly by the light reactions (photoassimilation, [7.13.6](/7.13.6)).

This example puts numbers from three chapters in the same field: carbon gain is limited by interception and conversion efficiency, water consumption is set by the stomata and the dryness of the air, and the nitrogen supply in turn depends on the same transpiration stream.

## 30.5. The Network of Signals, Hormones and Development

### 30.5.1. Hormones

The nine classes of **plant hormones** share the same logic of action: concentration is set by the steady state of synthesis, transport, conjugation and degradation (Eq. (13.1)), the effect depends on concentration and tissue sensitivity (Eq. (13.2)), and receptors mostly act by derepression ([7.1.15](/7.1.15)). The table below is organized by where each hormone is made, how it is transported, what it does and what it antagonizes:

| Hormone | Main sites of synthesis | Transport | Receptor and derepression | Main actions | Main antagonists or synergists | Chapter |
|---|---|---|---|---|---|---|
| Auxin | Shoot apex, young leaves, developing seeds | Polar transport (PIN, AUX1), also in the phloem | TIR1/AFB → Aux/IAA degradation | Cell elongation, vascular differentiation, lateral and adventitious roots, apical dominance, tropisms, fruit set | Cytokinin (root–shoot differentiation); ethylene (sensitivity of the abscission zone) | [7.13.13](/7.13.13) |
| Gibberellin | Young buds and leaves, developing seeds | Nonpolar; GA₁₂ is the main mobile form | GID1 → DELLA degradation | Stem elongation, germination, bolting and flowering, parthenocarpy | ABA (dormancy and germination); ethylene (sex expression in cucurbits) | [7.13.14](/7.13.14) |
| Cytokinin | Mainly root tips, also shoots | tZ type up in the xylem, iP type down in the phloem | AHK → AHP → type-B ARR | Cell division, shoot differentiation, release of apical dominance, delay of senescence | Auxin (Skoog–Miller ratio); ABA (stomata, senescence) | [7.13.14](/7.13.14) |
| Abscisic acid | Vascular tissue and leaves; in drought both roots and leaves | Xylem and phloem; pH determines distribution | PYR/PYL → PP2C inhibited → SnRK2 | Stomatal closure, seed maturation and dormancy, stress responses | GA (dormancy and germination); cytokinin | [7.13.15](/7.13.15) |
| Ethylene | Nearly all tissues; strongly increased during ripening, senescence, wounding and flooding | Gas diffusion; precursor ACC in the xylem | ETR → CTR1 inactivated → EIN2 | Triple response, fruit ripening, senescence and abscission, aerenchyma | Auxin (abscission); cytokinin (senescence) | [7.13.15](/7.13.15) |
| Brassinosteroid | Most tissues, acts locally | Essentially no long-distance transport | BRI1–BAK1 → BIN2 inactivated | Elongation and division, xylem differentiation, skotomorphogenic growth | Synergistic with auxin and gibberellin | [7.13.15](/7.13.15) |
| Jasmonate | Wound sites (chloroplasts and peroxisomes) | Systemic signal and volatile MeJA | COI1 → JAZ degradation | Defense against herbivores and necrotrophs, anther dehiscence | Antagonized by salicylic acid; JAZ–DELLA links growth and defense | [7.13.15](/7.13.15), [7.13.26](/7.13.26) |
| Salicylic acid | Infected tissue | NHP, MeSA and others take part in systemic signaling | NPR1 and NPR3/4 | Defense against biotrophs, hypersensitive response, systemic acquired resistance | Antagonized by jasmonate | [7.13.15](/7.13.15), [7.13.25](/7.13.25) |
| Strigolactone | Mainly roots | Up in the xylem | D14–MAX2 → D53/SMXL degradation | Inhibition of branching, promotion of mycorrhizae, induction of parasitic plant germination | Auxin and cytokinin (apical dominance) | [7.13.15](/7.13.15), [7.13.18](/7.13.18) |

Apart from ethylene and cytokinin, nearly all hormones and photoreceptors use the logic of "degrading or inhibiting an inhibitor": Aux/IAA, DELLA, PP2C, JAZ, D53/SMXL and the substrates of PIF and COP1 in the dark are all brakes that are removed. This logic has two advantages: with no signal the default state is safe (no growth, no flowering, no germination), and when the signal arrives, degrading a single protein quickly switches on a large set of genes.

### 30.5.2. Perception of Environmental Signals

| Signal | Main receptor or sensor | Main output | Chapter |
|---|---|---|---|
| Red and far-red light (light quality, photoperiod, shade) | **Phytochrome** (phyA, phyB), photostationary state $\varphi$, Eqs. (16.3), (16.7) | De-etiolation, germination of light-requiring seeds, **shade avoidance**, photoperiodism | [7.13.16](/7.13.16), [7.13.20](/7.13.20), [7.13.21](/7.13.21) |
| Blue light and UV-A | Cryptochromes, phototropins, ZTL | Inhibition of elongation, phototropism, stomatal opening, chloroplast movement, circadian clock | [7.13.16](/7.13.16), [7.13.19](/7.13.19) |
| UV-B | UVR8 | Sunscreen pigments, DNA repair | [7.13.16](/7.13.16) |
| Temperature | Thermal reversion of phyB, ELF3 phase separation, *PIF7* RNA thermometer; COLD1 and others for cold | Thermomorphogenesis, flowering time, cold acclimation | [7.13.16](/7.13.16), [7.13.22](/7.13.22), [7.13.27](/7.13.27) |
| Prolonged cold | Epigenetic silencing of the *FLC* locus | Vernalization | [7.13.22](/7.13.22) |
| Gravity | Sedimentation of amyloplasts in statocytes, Eq. (19.2) | Gravitropism | [7.13.19](/7.13.19) |
| Touch | Mechanosensitive channels, action potentials | Thigmotropism, seismonasty, Venus flytrap closure | [7.13.19](/7.13.19) |
| Water and osmotic conditions | OSCA1 and others; turgor and wall integrity | ABA synthesis, hydrotropism | [7.13.19](/7.13.19), [7.13.27](/7.13.27) |
| Nutrients | NRT1.1 (nitrate transceptor), phosphate starvation signals | Local plasticity of root architecture | [7.13.5](/7.13.5), [7.13.18](/7.13.18) |
| Microbes and herbivores | PRRs (PAMPs, DAMPs, HAMPs), NLRs (effectors) | PTI, ETI, induced defense | [7.13.25](/7.13.25), [7.13.26](/7.13.26) |
| Time of day | Circadian clock (CCA1/LHY–PRR–evening complex) | Gating of light signals, photoperiod measurement, anticipatory stomatal opening | [7.13.16](/7.13.16), [7.13.21](/7.13.21) |

### 30.5.3. Long-Distance Signals

| Signal | Pathway | Speed or time | Function | Chapter |
|---|---|---|---|---|
| Hydraulic signal | Transmission of xylem tension | Almost instantaneous | Rapid stomatal response to soil drought | [7.13.10](/7.13.10), [7.13.15](/7.13.15) |
| Electrical signal | GLR3.3/3.6, phloem | Up to about $9\,\mathrm{cm\,min^{-1}}$; action potential of the sensitive plant 2–3 cm/s | Wound alarm, seismonastic movement | [7.13.19](/7.13.19), [7.13.26](/7.13.26) |
| Reactive oxygen and calcium waves | Cell-to-cell relay of RBOH and calcium channels | About $8.4\,\mathrm{cm\,min^{-1}}$ | Systemic stress acclimation | [7.13.27](/7.13.27) |
| Auxin | Polar cell-to-cell transport | About 5–20 mm/h | Apical dominance, tropisms, vascular patterning | [7.13.13](/7.13.13) |
| ABA, cytokinin, ACC, strigolactone | Xylem (root → shoot) | With the transpiration stream | Report on root water and nutrient status | [7.13.14](/7.13.14), [7.13.15](/7.13.15) |
| Florigen (FT protein) | Phloem (leaf → shoot apex) | With assimilates, about $1\,\mathrm{m\,h^{-1}}$ | Carries the day length measured in the leaf to the shoot apex | [7.13.21](/7.13.21) |
| Sucrose, mRNA, small RNA | Phloem | With assimilates | Nutritional and developmental signals; miR399 reports phosphate deficiency | [7.13.11](/7.13.11), [7.13.18](/7.13.18) |
| Systemic acquired resistance signals | NHP, MeSA, AzA, G3P and others | About $3\,\mathrm{cm\,h^{-1}}$, established in 1–2 d | Priming of uninfected parts | [7.13.25](/7.13.25) |
| Volatiles | Air | Diffusion and convection | Attraction of natural enemies, early warning of neighbors | [7.13.26](/7.13.26) |

Fast signals (hydraulic, electrical, reactive oxygen waves) give the "alarm" and spread through the whole plant within minutes; slow signals (hormones, proteins, RNA) give the "instructions," travel with the bulk flow of xylem or phloem, and determine development and acclimation that last from days to months.

## 30.6. The Developmental Program from Seed to Seed

The life cycle of an annual seed plant is a series of decisions: when to germinate, when to become adult, when to flower, which pollen grain to accept, when to mature, when to senesce. Each decision integrates environmental signals and internal state, and most decisions are irreversible once made.

| Stage | Decision | Main environmental signals | Internal switches | Quantitative description | Chapter |
|---|---|---|---|---|---|
| Seed | Dormancy or germination | Light (R:FR), alternating temperatures, cold stratification, nitrate, smoke (karrikins) | ABA/GA balance (content × sensitivity); DOG1; phyB–PIF1 | Hydrotime and hydrothermal time Eqs. (20.1)–(20.3); Pfr threshold; seed longevity equation ([7.12.19](/7.12.19#eq-19.1)) | [7.13.20](/7.13.20) |
| Germination and seedling establishment | Emergence, de-etiolation | Light, soil resistance | phy and cry inhibit COP1 and PIF; ethylene + auxin maintain the hook | Three phases of water uptake; stoichiometry of reserve mobilization | [7.13.16](/7.13.16), [7.13.20](/7.13.20) |
| Vegetative growth | How fast to grow, where to form organs, how much to branch | Light, temperature, water, nutrients | Auxin maxima, cytokinin/auxin ratio, strigolactone; miR156–SPL timer | Lockhart, RGR, logistic, thermal time, phyllotaxis model | [7.13.17](/7.13.17), [7.13.18](/7.13.18), [7.13.22](/7.13.22) |
| Floral induction | Flower now? | Day length, prolonged cold, ambient temperature | *CO* → *FT*; epigenetic silencing of *FLC*; integrators *SOC1*, *LFY* | Day-length formula Eqs. (21.1), (21.2); external coincidence model Eq. (21.3); vernalization dose Eq. (22.1); photothermal model Eq. (22.2) | [7.13.21](/7.13.21), [7.13.22](/7.13.22) |
| Flowering and fertilization | Which pollen grain to accept | Temperature, humidity, pollinators | Self-incompatibility at the S locus; pollen tube guidance (LURE–PRK6) | Rejection probability $2/n$; pollen viability Eq. (23.1); pollen tube oscillation Eq. (23.2) | [7.13.23](/7.13.23) |
| Seed and fruit development | How much to fill, when to mature | Temperature, water | Sink strength; LEC/ABI3 and ABA; ethylene system 2 | Logistic grain filling Eq. (23.3); ethylene switch Eq. (23.5) | [7.13.11](/7.13.11), [7.13.23](/7.13.23) |
| Senescence and abscission | Recycle nutrients, discard organs | Shortening days, drought, shade, disease | Ethylene, ABA, jasmonate promote, cytokinin delays; NAC transcription factors | Sigmoid decline of senescence Eq. (24.1); remobilization efficiency Eq. (24.2); abscission-zone breakstrength Eq. (24.4) | [7.13.24](/7.13.24) |

![From seed to seed: the developmental program of an annual seed plant (schematic curves, not data). The upper columns give the decisions to be made in the seven stages (italic) and the environmental signals and hormones that control them; below, on the same time axis, are several quantities: seed reserves are exhausted rapidly after germination (dashed line), shoot dry weight grows along a logistic curve (Eq. (17.9)), green leaf area first increases and then falls with senescence during grain filling, and grain dry weight grows along a later logistic filling curve (Eq. (23.3)), with a substantial part of its nitrogen and carbon remobilized from senescing leaves. The three dotted lines mark irreversible transitions: radicle emergence (completion of germination), the floral transition and double fertilization](./plots/life-cycle.py)

Two mechanisms recur in this table. The first is threshold accumulation: seeds accumulate hydrotime, the shoot apex accumulates cycles of photoperiodic induction and the effective cold of vernalization, and developmental rate accumulates thermal time; only when a threshold is reached is the decision made, which makes the plant insensitive to brief, accidental signals. The second is irreversibility produced by positive feedback: mutual activation of LFY and AP1 makes the decision to flower irrevocable, autocatalysis of ethylene system 2 means that ripening of a climacteric fruit cannot be stopped once begun (the saddle-node bifurcation of Eq. (23.5)), and H3K27me3 at the *FLC* locus keeps the vernalized state in memory after warming. Accumulation makes a decision robust and positive feedback makes it complete; together they allow a rooted plant to make seasonally synchronized decisions in a fluctuating environment.

## 30.7. Responses to the Environment and Trade-offs

### 30.7.1. Stresses

| Stress | Primary effects | Main perception and signals | Main responses | Quantity | Chapter |
|---|---|---|---|---|---|
| Drought | Lower water potential, loss of turgor, cessation of expansion | Osmotic sensing, ABA rises about 50-fold | Stomatal closure, **osmotic adjustment**, larger root:shoot ratio, LEA, CAM | Leaf water potential Eq. (27.3); osmotic adjustment generally 0.2–0.8 MPa, Eq. (27.1) | [7.13.27](/7.13.27), [7.13.15](/7.13.15) |
| Flooding | Root hypoxia, energy crisis, toxic reduced compounds in the soil | Oxygen sensing by ERF-VII, ethylene accumulation | Fermentation, aerenchyma, adventitious roots; rice *SUB1A* quiescence or *SNORKEL* escape | Maximum root length in aerenchyma Eq. (27.4) | [7.13.27](/7.13.27), [7.13.12](/7.13.12) |
| Salt | Osmotic stress + ion toxicity | Osmotic and ionic phases; GIPC–MOCA1 | SOS efflux, HKT1 retrieval, NHX vacuolar compartmentation | $\Psi_{\mathrm{s}} \approx -0.036\,\mathrm{MPa}\times\mathrm{EC}$, Eq. (27.5); Maas–Hoffman Eq. (27.6) | [7.13.27](/7.13.27), [7.13.5](/7.13.5) |
| Low temperature (chilling) | Membrane phase transition, enzyme imbalance, low-temperature photoinhibition | Membrane fluidity, COLD1 | Desaturases, highly unsaturated membrane lipids | Double-bond index Eq. (27.2) | [7.13.27](/7.13.27) |
| Freezing | Extracellular ice dehydrates cells | ICE1–CBF–COR | Cold acclimation, sugars and antifreeze proteins | Water potential of ice about $-1.2\,\mathrm{MPa}$ per °C, Eqs. (27.7), (27.8) | [7.13.27](/7.13.27) |
| High temperature | Protein denaturation, Rubisco activase inactivation, sterility at flowering | HSF | HSPs, acquired thermotolerance | Rubisco activase inactivated from about 35 °C | [7.13.27](/7.13.27) |
| Strong light | D1 damage in PSII, reactive oxygen species | $\Delta\mathrm{pH}$, PsbS, xanthophyll cycle | NPQ, state transitions, D1 repair | Steady state of photoinhibition Eq. (7.9) | [7.13.7](/7.13.7) |
| Heavy metals | Displacement of essential elements, binding to thiols | — | Exclusion, phytochelatins, vacuolar compartmentation; hyperaccumulation | — | [7.13.27](/7.13.27) |
| Pathogens | Loss of nutrients and tissue | PRRs and NLRs | PTI, ETI, hypersensitive response, **systemic acquired resistance** | van der Plank Eqs. (25.1)–(25.5) | [7.13.25](/7.13.25) |
| Herbivores | Tissue loss | Wounding, HAMPs, electrical signals | Jasmonate, induced defense, indirect defense | Induction cascade Eq. (26.4) | [7.13.26](/7.13.26) |

The primary effects of different stresses differ, but the secondary effects converge: increased reactive oxygen species, higher ABA, accumulation of compatible solutes, lower activity of synthetic enzymes and higher activity of hydrolytic enzymes ([7.13.27](/7.13.27)). Shared protective compounds and signals explain **cross-tolerance**: plants that have experienced one stress often tolerate another better. The effects of combined stresses, however, are not simply additive: in the United States in 1980–2004, agricultural losses under drought plus heat were about six times those under drought alone, because drought closes the stomata and reduces transpirational cooling.

### 30.7.2. Trade-offs

Many plant traits have no "best" value, only a compromise among costs and benefits. The most important trade-offs of the course are:

| Trade-off | One side | The other side | Quantity or mechanism | Chapter |
|---|---|---|---|---|
| Carbon and water | Wider stomatal opening, more carbon | Narrower opening, less water lost | Cowan–Farquhar condition Eq. (10.6); Figure 2 | [7.13.10](/7.13.10) |
| Hydraulic efficiency and safety | Wide conduits, conductance $\propto r^4$ | Narrow conduits and small pits, resistance to cavitation | $P_{50}$ and safety margin, Eq. (3.3) | [7.13.3](/7.13.3) |
| Isohydric and anisohydric | Protect leaf water potential and xylem | Keep photosynthesizing | Eq. (27.3) | [7.13.27](/7.13.27) |
| Light capture and photoprotection | Large antenna, little heat dissipation | Strong NPQ | Slow NPQ relaxation costs the canopy carbon | [7.13.7](/7.13.7) |
| Cost of $\ce{CO2}$ concentration | Low energy cost of C3 | Low photorespiration and high WUE of C4 | Eqs. (8.4), (8.5) | [7.13.8](/7.13.8) |
| Growth and defense | Growth | Defense compounds | JAZ–DELLA; optimal defense allocation Eqs. (26.5), (26.6) | [7.13.26](/7.13.26) |
| Root and shoot | Organs acquiring light and $\ce{CO2}$ | Organs acquiring water and nutrients | Functional balance Eq. (17.13) | [7.13.17](/7.13.17) |
| Dormancy and germination | Deep dormancy: avoids the unfavorable season | Shallow dormancy: uniform emergence but prone to preharvest sprouting | ABA/GA balance; domestication selected shallow dormancy | [7.13.20](/7.13.20), [7.13.28](/7.13.28) |
| Early senescence and grain quality | Early senescence: high grain protein | Late senescence: long grain-filling period | *NAM-B1* | [7.13.24](/7.13.24) |
| Yield and stress resistance | High harvest index of domesticated crops | Resistance and adaptability of wild species | Domestication bottleneck Eq. (28.3); de novo domestication | [7.13.28](/7.13.28) |

These trade-offs explain the relation between plant physiology and agriculture: breeding and cultivation can rarely improve both sides of a trade-off at once, and most progress comes from reselecting the compromise point for a particular environment (for example, selecting semidwarf, fertilizer-responsive, lodging-resistant varieties for well-irrigated, heavily fertilized fields), or from finding new mechanisms that bypass the trade-off (for example the C4 pathway, induced defense, or stress-induced rather than constitutive expression of stress-tolerance genes).

## 30.8. The Main Equations of the Course

The table below collects the main equations of the course by chapter. Typical values are taken from the chapters; an equation used in several chapters is listed under the chapter where it first appears.

| Equation | Chapter and equation number | Physical or biological meaning | Typical values |
|---|---|---|---|
| $Y = \mathrm{HI}\times B$, $B = \varepsilon_{\mathrm{c}}\int f_{\mathrm{int}}S\,\mathrm{d}t$ | 1, Eq. (1.1); 9, Eq. (9.11) | Yield = harvest index × biomass = partitioning × conversion × interception × radiation | $\varepsilon_{\mathrm{c}}$ 2.5–3 for C3, 3.3–4 $\mathrm{g\,MJ^{-1}}$ for C4; HI 0.3–0.5 |
| $J = g\,\Delta X = \Delta X/r$ | 1, Eq. (1.2) | Flux = conductance × driving force | Section 30.2 |
| $\Psi_{\mathrm{w}} = \Psi_{\mathrm{s}} + \Psi_{\mathrm{p}} + \Psi_{\mathrm{g}} + \Psi_{\mathrm{m}}$ | 2, Eq. (2.1) | Components of water potential | Leaf $-0.2$ to $-2.5\,\mathrm{MPa}$; gravitational potential $0.01\,\mathrm{MPa\,m^{-1}}$ |
| $\Psi_{\mathrm{s}} = -c_{\mathrm{s}}RT$ | 2, Eq. (2.2); 27, Eq. (27.1) | Solute potential depends only on the osmolarity of solute particles | $1\,\mathrm{osmol\,L^{-1}} \approx -2.44\,\mathrm{MPa}$ (20 °C) |
| $J_V = L_p(\Delta\Psi_{\mathrm{p}} + \sigma\Delta\Psi_{\mathrm{s}})$ | 2, Eqs. (2.3), (2.7) | Water flow across membranes; $\sigma$ is the reflection coefficient | $L_p \sim 10^{-7}$–$10^{-6}\,\mathrm{m\,s^{-1}\,MPa^{-1}}$ |
| $\varepsilon = \Delta\Psi_{\mathrm{p}}/(\Delta V/V)$ | 2, Eq. (2.4) | Volumetric elastic modulus: wall stiffness | 1–50 MPa |
| $t_{1/2} = 0.693V/[AL_p(\varepsilon - \Psi_{\mathrm{s}})]$ | 2, Eq. (2.8) | Speed of cellular water equilibration | 1–10 s |
| $\Psi_{\mathrm{p}} = -2T/r$ | 3, Eq. (3.1) | Negative pressure under a meniscus | Surface tension $0.0728\,\mathrm{N\,m^{-1}}$ |
| $Q = \frac{\pi r^4}{8\eta}\frac{\Delta\Psi_{\mathrm{p}}}{\Delta x}$ | 3, Eq. (3.2) | Hagen–Poiseuille: xylem bulk flow | About $0.02\,\mathrm{MPa\,m^{-1}}$; a 100 m tree needs about 2 MPa at the top |
| $\mathrm{PLC} = 100[1 - \mathrm{e}^{-(-\Psi_{\mathrm{x}}/b)^c}]$ | 3, Eq. (3.3) | Vulnerability curve | $P_{50}$ about $-1$ to $< -8\,\mathrm{MPa}$ |
| $E = g_{\mathrm{tw}}\Delta w$, $1/g_{\mathrm{tw}} = 1/g_{\mathrm{s}} + 1/g_{\mathrm{b}}$ | 3, Eqs. (3.4), (3.5) | Transpiration = conductance × vapor concentration difference | $E \sim 1$–$10\,\mathrm{mmol\,m^{-2}\,s^{-1}}$ |
| $A/E = c_{\mathrm{a}}(1 - c_{\mathrm{i}}/c_{\mathrm{a}})/(1.6\,\Delta w)$ | 3, Eq. (3.6) | Water-use efficiency | Transpiration ratio about 400 for C3, 150 for C4, 50 for CAM |
| $E = K_{\mathrm{plant}}(\Psi_{\mathrm{soil}} - \Psi_{\mathrm{leaf}} - \rho_{\mathrm{w}}gh)$ | 3, Eq. (3.7); 27, Eq. (27.3) | Liquid-phase Ohm's law of the SPAC | Predawn leaf water potential ≈ soil water potential |
| $y = A(1 - \mathrm{e}^{-c(x+b)})$ | 4, Eq. (4.1) | Mitscherlich fertilizer response | $x_{90} = \ln 10/c - b$ |
| $\tilde\mu_j = \mu_j^\circ + RT\ln c_j + z_jF\varphi$ | 5, Eq. (5.1) | Electrochemical potential | — |
| $E_j = (59.2\,\mathrm{mV}/z_j)\lg(c^{\mathrm{o}}/c^{\mathrm{i}})$ | 5, Eq. (5.2) | Nernst equation; $V_{\mathrm{m}} - E_j$ distinguishes active from passive transport | 59.2 mV per tenfold concentration at 25 °C |
| $\Delta p = V_{\mathrm{m}} - 59.2\,\mathrm{mV}\,\Delta\mathrm{pH}$ | 5, Eq. (5.3) | Proton motive force | Plasma membrane about $-250\,\mathrm{mV}$ |
| $v = V_1S/(K_1+S) + V_2S/(K_2+S)$ | 5, Eq. (5.5) | Biphasic uptake (HATS + LATS) | $\ce{K+}$ HATS 5–30 µM |
| $\ce{N2 + 8e- + 8H+ + 16ATP -> 2NH3 + H2 + 16ADP + 16P_i}$ | 6, Eq. (6.8) | Stoichiometry of nitrogen fixation | More than 4 g carbon per gram of nitrogen |
| $\Phi_{\mathrm{PSII}} + \Phi_{\mathrm{NPQ}} + \Phi_{\mathrm{NO}} = 1$; $F_{\mathrm{v}}/F_{\mathrm{m}}$ | 7, Eqs. (7.4)–(7.8) | Partitioning of absorbed light energy; chlorophyll fluorescence | Healthy leaf $F_{\mathrm{v}}/F_{\mathrm{m}} \approx 0.83$ |
| $\mathrm{d}x/\mathrm{d}t = -k_{\mathrm{d}}Ix + k_{\mathrm{r}}(1 - x)$ | 7, Eq. (7.9) | Photoinhibition: D1 damage and repair | Steady state $x^* = k_{\mathrm{r}}/(k_{\mathrm{r}} + k_{\mathrm{d}}I)$ |
| $\phi = 2\Gamma^*/c_{\mathrm{c}}$; $\Gamma^*(T)$ | 8, Eqs. (8.1), (8.2) | Ratio of oxygenation to carboxylation; $\ce{CO2}$ compensation point | $\Gamma^* = 42.75\,\mu\mathrm{mol\,mol^{-1}}$ (25 °C) |
| $3 + 2/(1 - \varphi)$ ATP | 8, Eq. (8.5) | Energy cost of C4 ($\varphi$ is leakiness) | Leakiness 20%–30% |
| $\Delta = a + (b - a)c_{\mathrm{i}}/c_{\mathrm{a}}$ | 8, Eqs. (8.8), (8.10) | Carbon isotope discrimination records $c_{\mathrm{i}}/c_{\mathrm{a}}$ and WUE | About 20‰ for C3, 3–5‰ for C4 |
| $A = \min(A_{\mathrm{c}}, A_{\mathrm{j}}, A_{\mathrm{p}})$ | 9, Eqs. (9.3)–(9.6) | Farquhar model: Rubisco, RuBP regeneration, triose phosphate utilization | $K_{\mathrm{c}} = 404.9$, $K_{\mathrm{o}} = 278.4$ (25 °C) |
| $A = g_{\mathrm{c}}(c_{\mathrm{a}} - c_{\mathrm{i}}) = g_{\mathrm{m}}(c_{\mathrm{i}} - c_{\mathrm{c}})$ | 9, Eqs. (9.7), (9.8) | Supply of $\ce{CO2}$ | $c_{\mathrm{i}}/c_{\mathrm{a}}$ about 0.7 for C3 |
| $k(T) = k_{25}\exp[E_{\mathrm{a}}(T - 298.15)/(298.15RT)]$ | 9, Eq. (9.9) | Arrhenius temperature response | C3 optimum 20–30 °C |
| $I = I_0\mathrm{e}^{-kL}$ | 9, Eq. (9.10) | Beer's law: light in the canopy | Optimal LAI 4–6 |
| $J \approx 2rD\Delta c$; $g_{\max}$ | 10, Eqs. (10.1), (10.2) | Small-pore diffusion law; anatomical maximum stomatal conductance | — |
| $g_{\mathrm{s}} = g_0 + 1.6(1 + g_1/\sqrt{D})A/c_{\mathrm{a}}$ | 10, Eqs. (10.4), (10.5) | Medlyn stomatal model | $g_1 \approx 4$ for C3, about 1.6 $\mathrm{kPa^{0.5}}$ for C4 |
| $\partial E/\partial A = \lambda$ | 10, Eq. (10.6) | Cowan–Farquhar optimality condition | — |
| $u = -\frac{a^2}{8\eta f}\frac{\mathrm{d}P}{\mathrm{d}x}$ | 11, Eqs. (11.1)–(11.3) | Sieve-tube bulk flow and Münch pressure flow | About $1\,\mathrm{m\,h^{-1}}$; sucrose 0.3–0.9 M |
| Sink strength = sink size × sink activity | 11, Eq. (11.4) | Ability of a sink to compete for assimilates | — |
| P/O = $\ce{H+}$ pumped/4 | 12, Eq. (12.1) | ATP yield of respiration | NADH 2.5, succinate 1.5, via AOX 1.0 or 0 |
| $R = \frac{1 - Y_{\mathrm{G}}}{Y_{\mathrm{G}}}\frac{\mathrm{d}W}{\mathrm{d}t} + mW$ | 12, Eqs. (12.2), (12.3) | Growth and maintenance respiration | White clover $k \approx 0.25$, $c \approx 0.015\,\mathrm{d^{-1}}$ |
| $R(T) = R_{\mathrm{ref}}Q_{10}^{(T - T_{\mathrm{ref}})/10}$ | 12, Eq. (12.4) | Temperature response of respiration | $Q_{10} \approx 2$ |
| $\mathrm{d}c/\mathrm{d}t = s + J_{\mathrm{in}} + r - (k_{\mathrm{deg}} + k_{\mathrm{conj}})c - J_{\mathrm{out}}$ | 13, Eq. (13.1) | Steady state of hormone concentration | $t_{1/2} = \ln 2/k$ |
| Ion trapping | 13, Eqs. (13.4), (13.5) | Accumulation of weak acids in alkaline compartments | IAA: about 43-fold at cytosolic pH 7.2 |
| $\partial_t c = D\partial_x^2 c - v\partial_x c - kc$ | 13, Eq. (13.6) | Advection–diffusion of polar auxin transport | 5–20 mm/h |
| $D^* = s/(k_0 + k_1\theta)$ | 14, Eqs. (14.2), (14.3) | Steady state of DELLA and growth restraint | *gai*/*Rht* type: $k_1 = 0$ |
| $g_{\mathrm{s}} = g_{\min} + (g_{\max} - g_{\min})\exp(-\beta[\mathrm{ABA}]\mathrm{e}^{-\delta\Psi})$ | 15, Eq. (15.1) | Tardieu–Davies: chemical and hydraulic signals amplify each other | — |
| $\varphi = k_1/(k_1+k_2)$ | 16, Eqs. (16.3), (16.7) | Photostationary state of phytochrome | Red light 0.85–0.88, daylight about 0.6, about 0.29 under a canopy with $\zeta = 0.2$ |
| $\frac{1}{V}\frac{\mathrm{d}V}{\mathrm{d}t} = \phi(P - Y)$ | 17, Eq. (17.2) | Lockhart equation | $Y$ about 0.1–0.5 MPa |
| $\mathrm{RGR} = \mathrm{NAR}\times\mathrm{LAR}$ | 17, Eqs. (17.7), (17.8) | Growth analysis | Seedling RGR 0.1–0.4 $\mathrm{d^{-1}}$ |
| $W = K/(1 + \mathrm{e}^{-r(t - t_{\mathrm{m}})})$ | 17, Eq. (17.9); 23, Eq. (23.3) | Grand period of growth, grain filling | Maximum rate $rK/4$; effective filling period $4/k$ |
| $\mathrm{GDD} = \sum\max(0, \bar T - T_{\mathrm{b}})$ | 17, Eq. (17.12) | Growing degree days | — |
| $v_{\max} = F\,l_{\mathrm{mat}}$; $\lambda = vT$ | 18, Eq. (18.2) | Root elongation; root clock | Root clock period about 6 h |
| $\tan(\theta/2) = \tan(\theta_0/2)\,\mathrm{e}^{-kt}$ | 19, Eq. (19.3) | Sine law of gravitropic bending | — |
| $\theta_{\mathrm{HT}} = [\Psi - \Psi_{\mathrm{b}}(g)](T - T_{\mathrm{b}})t_g$ | 20, Eqs. (20.1)–(20.3) | Hydrotime and hydrothermal time | Three parameters describe the whole germination curve |
| $v = K_i - p/\sigma$ | [7.12.19](/7.12.19#eq-19.1), Eq. (19.1) | Ellis–Roberts seed longevity equation | Moisture content and temperature act multiplicatively |
| $\cos H_0 = -\tan\phi\tan\delta$, $N = 2H_0/15^\circ$ | 21, Eqs. (21.1), (21.2) | Day length | Critical day length: henbane 11.5 h, cocklebur 15.5 h |
| $\dot F = vP^n/(K^n + P^n) - \gamma F$ | 21, Eq. (21.3) | External coincidence: *CO* transcription × stabilization in light → *FT* | Critical day length is an emergent property |
| $D = D_{\min} + (D_0 - D_{\min})\mathrm{e}^{-V/V_{\mathrm{s}}}$ | 22, Eq. (22.1) | Vernalization dose–response | Effective temperature 0–10 °C |
| $\dot E = k_0 + k_1E^n/(K^n + E^n) - k_2E$ | 23, Eq. (23.5) | Autocatalytic switch of ethylene system 2 | Saddle-node bifurcation |
| $\mathrm{RE} = (N_{\mathrm{green}} - N_{\mathrm{senesced}})/N_{\mathrm{green}}$ | 24, Eq. (24.2) | Nutrient remobilization efficiency | About 50% |
| $L(T) = L_0Q_{10}^{-(T - T_0)/10}$ | 24, Eqs. (24.5), (24.6) | Postharvest storage life | — |
| $\mathrm{d}x/\mathrm{d}t = rx(1 - x)$ | 25, Eqs. (25.1)–(25.5) | van der Plank disease epidemic | $r \approx 0.4\,\mathrm{d^{-1}}$, doubling in about 1.7 d |
| $f^* = a^{-1}\ln(ah_0/r_0)$ | 26, Eqs. (26.5), (26.6) | Optimal defense allocation | — |
| $L_{\max} = \sqrt{2D\varphi(C_0 - C_{\mathrm{c}})/Q}$ | 27, Eq. (27.4) | Maximum root length supplied with oxygen by aerenchyma | — |
| $Y_{\mathrm{r}} = 100 - b(\mathrm{EC_e} - a)$ | 27, Eq. (27.6) | Maas–Hoffman salt tolerance model | — |
| $\Psi_{\mathrm{ice}} \approx -(\Delta_{\mathrm{fus}}H/\bar V_{\mathrm{w}})(T_0 - T)/T_0$ | 27, Eqs. (27.7), (27.8) | Water potential of ice and freezing dehydration | About $-1.2\,\mathrm{MPa}$ per °C; about 90% water loss at −10 °C |
| $R = h^2S$ | 28, Eq. (28.1) | Breeder's equation | — |
| $H_d/H_0 \approx \mathrm{e}^{-d/2N_{\mathrm{b}}}$ | 28, Eq. (28.3) | Retention of heterozygosity through a domestication bottleneck | — |
| $M = Wh\sin\theta$ | 28, Eq. (28.4) | Bending moment of lodging | Semidwarfing lowers $h$ |

## 30.9. Links to Other Courses

| Course | What this course uses | What this course provides for it |
|---|---|---|
| Biochemistry ([7.1](/7.1)) | Light reactions and the Calvin cycle ([7.1.24](/7.1.24)), biochemistry of C4 and CAM ([7.1.25](/7.1.25)), respiration ([7.1.18](/7.1.18), [7.1.20](/7.1.20), [7.1.23](/7.1.23)), nitrogen metabolism ([7.1.27](/7.1.27)), hormone receptors and signaling ([7.1.15](/7.1.15)) | The physiological consequences and quantification of these pathways in the leaf, the whole plant and the field |
| Cell Biology ([7.3](/7.3)) | Membrane transport ([7.3.5](/7.3.5)), the cell wall ([7.3.23](/7.3.23)), autophagy and cell death ([7.3.11](/7.3.11), [7.3.25](/7.3.25)) | Turgor, proton pumps and the vacuole of the plant cell |
| Genetics and Molecular Biology ([7.4](/7.4), [7.2](/7.2)) | Breeder's equation and heterosis ([7.4.24](/7.4.24)), cytoplasmic male sterility ([7.4.11](/7.4.11)), epigenetic memory ([7.2.15](/7.2.15)) | The physiological basis of vernalization and hybrid rice |
| Developmental Biology ([7.5](/7.5)) | Morphogens and self-organized patterns ([7.5.11](/7.5.11), [7.5.12](/7.5.12)), evolutionary theories of aging ([7.5.37](/7.5.37)) | Auxin maxima, meristems and the decision to flower |
| Biophysics ([7.6](/7.6)) | Water potential and chemical potential ([7.6.3](/7.6.3)), photochemistry of photoreceptors ([7.6.18](/7.6.18)), switches and oscillators ([7.6.33](/7.6.33)) | The numerical values of these physical principles in plants |
| Evolutionary Biology ([7.10](/7.10)) | Host–pathogen and plant–herbivore coevolution ([7.10.17](/7.10.17)), domestication ([7.10.9](/7.10.9), [7.10.33](/7.10.33)) | The physiology of domestication traits and of the evolution of C4 |
| Microbiology ([7.11](/7.11)) | Nodule and mycorrhizal symbioses ([7.11.31](/7.11.31)), growth curves in batch culture ([7.11.8](/7.11.8)) | The host side of the physiology |
| Botany ([7.12](/7.12)) | Morphology and anatomy, seeds and life histories, phylogeny ([7.12.19](/7.12.19), [7.12.20](/7.12.20), [7.12.23](/7.12.23), [7.12.27](/7.12.27), [7.12.32](/7.12.32)) | The mechanisms behind the morphological structures of 7.12 |
| Mathematics and Statistics ([2.4](/2.4), [2.5](/2.5), [7.7](/7.7)) | Ordinary differential equations, the diffusion equation, probit and threshold models | Worked applications in biology |
| Ecology ([7.19](/7.19)) | — | Primary production, water-use and light-use efficiency, relations of plants to other organisms, effects of climate change |

## Summary

| Thread | Core relations | Main values | Chapter |
|---|---|---|---|
| Unified framework | Flux = conductance × driving force, Eq. (1.2); series resistance is controlled by the largest; long distances by bulk flow, short distances by diffusion | Glucose diffusion over 1 m about 32 years; xylem $Q \propto r^4$ | 1–5, 11, 13, 17, 27 |
| Recurring mathematics | Saturation, Hill, first-order kinetics, logistic, switch, oscillator, threshold accumulation, optimization | Section 30.2.2 | Whole course |
| Water–carbon coupling | $A/E = c_{\mathrm{a}}(1 - c_{\mathrm{i}}/c_{\mathrm{a}})/(1.6\Delta w)$, Eq. (3.6); the stoma is the largest adjustable resistance; Cowan–Farquhar optimum, Eq. (10.6) | Transpiration ratio about 400 for C3, 150 for C4, 50 for CAM; $c_{\mathrm{i}}/c_{\mathrm{a}}$ about 0.7 for C3 | 3, 8–10 |
| Carbon budget | Radiation × interception × conversion × partitioning, Eqs. (1.1), (9.11); source–sink and pressure flow | Theoretical limit C3 4.6%, C4 6.0%, field about 1%; respiration 30%–60%; HI 0.3 → 0.5 | 7–12 |
| Water budget | About 97% lost, 2% retained, 1% in metabolism; transpiration doubles as nutrient conveyor, cooling and signal channel | 5–11 mm for a wheat field on a sunny day (Example 30.4.1) | 2, 3 |
| Nitrogen budget | Mass flow and diffusion → proton-coupled uptake → GS–GOGAT → remobilization | About 12 ATP per nitrate; fixation 16 ATP/$\ce{N2}$; remobilization about 50% | 4–6, 24 |
| Hormones | Steady state Eq. (13.1); Hill dose–response; receptors mostly act by derepression | Nine classes; ABA rises about 50-fold in drought | 13–15 |
| Environmental sensing | Phytochrome photostationary state, blue-light receptors, temperature and gravity sensing, circadian clock | Daylight $\varphi \approx 0.6$; period about 24.7 h | 16, 19 |
| Long-distance signals | Fast alarms (hydraulic, electrical, reactive oxygen waves), slow instructions (hormones, FT, RNA) | Electrical signal ≤ 9 cm/min; phloem about 1 m/h | 11, 13–16, 21, 25–27 |
| Developmental program | Threshold accumulation makes decisions robust, positive feedback makes them irreversible | Hydrotime, thermal time, vernalization dose; LFY–AP1, ethylene system 2, *FLC* memory | 17–24 |
| Stress | Primary effects differ, secondary effects converge (reactive oxygen species, ABA, compatible solutes); cross-tolerance | Osmotic adjustment 0.2–0.8 MPa; water potential of ice about $-1.2\,\mathrm{MPa}$ per °C | 7, 25–27 |
| Trade-offs | Carbon and water, efficiency and safety, growth and defense, root and shoot, dormancy and germination, yield and resistance | Section 30.7.2 | Whole course |
| Agriculture | Harvest index, semidwarfing, heterosis and the physiological basis of domestication | World rice yield 1.9 → 4.8 t/ha (1961–2024) | 28 |

The main equations of the course, with chapters and equation numbers, meanings and typical values, are collected in the table of Section 30.8.

## Questions

1. A 30 m tall tree transpires at noon on a sunny day. The soil water potential is $-0.3\,\mathrm{MPa}$, the water potential of the canopy leaves is $-1.8\,\mathrm{MPa}$, and the air is at 20 °C and 50% relative humidity. (a) How much of the water potential difference between the canopy leaves and the soil is due to gravity? (b) What is the water potential difference between leaf and air? Why is this difference enormous, yet this segment from leaf to air is not where most of the resistance to flow in the whole plant lies?

   **Answer** (a) The gravitational potential gradient is about $0.01\,\mathrm{MPa\,m^{-1}}$, so 30 m corresponds to $0.29\,\mathrm{MPa}$ ($\rho_{\mathrm{w}}gh = 1000 \times 9.8 \times 30\,\mathrm{Pa}$). The total water potential difference is $1.5\,\mathrm{MPa}$, of which about 0.29 MPa is used to lift the water column and the remaining 1.2 MPa to overcome frictional resistance in the liquid phase (Eq. (3.7)).

   (b) The water potential of the air is $\Psi = (RT/\bar V_{\mathrm{w}})\ln\mathrm{RH} = (8.314 \times 293/18.0\times10^{-6})\ln 0.5 \approx -94\,\mathrm{MPa}$, about 92 MPa below that of the leaf. In the liquid phase flux is proportional to the water potential difference, whereas in the gas phase the driving force for transpiration is the water vapor mole fraction difference $\Delta w$ and the corresponding resistance is that of the stomata and boundary layer (Eq. (3.5)). That the water potential drops so far in the gas phase means that the "resistance" of the gas-phase segment (in terms of water potential) is far larger than that of the liquid phase; this is why the transpiration rate is determined mainly by stomatal conductance and $\Delta w$, and why the plant regulates water loss through the stomata rather than through the liquid phase. The water potential difference in the liquid phase only determines how high or low leaf water potential is at a given transpiration rate (Eq. (27.3)), and hence whether the xylem is close to its cavitation threshold.

2. A C3 leaf has $c_{\mathrm{a}} = 420\,\mu\mathrm{mol\,mol^{-1}}$ and $c_{\mathrm{i}}/c_{\mathrm{a}} = 0.7$. (a) What is its transpiration ratio at a leaf-to-air vapor pressure deficit $D = 1\,\mathrm{kPa}$ and at $3\,\mathrm{kPa}$ (atmospheric pressure 101.3 kPa)? (b) A C4 leaf at $D = 3\,\mathrm{kPa}$ has $c_{\mathrm{i}}/c_{\mathrm{a}} = 0.35$; what is its transpiration ratio? (c) What does this show about the environments in which C4 plants dominate?

   **Answer** By Eq. (3.6), the transpiration ratio is $\mathrm{TR} = E/A = 1.6\,\Delta w/[c_{\mathrm{a}}(1 - c_{\mathrm{i}}/c_{\mathrm{a}})]$.

   (a) $D = 1\,\mathrm{kPa}$: $\Delta w = 0.00987$, $\mathrm{TR} = 1.6 \times 0.00987/(420\times10^{-6} \times 0.3) = 0.0158/1.26\times10^{-4} \approx 125$. $D = 3\,\mathrm{kPa}$: $\Delta w = 0.0296$, $\mathrm{TR} \approx 376$.

   (b) $\mathrm{TR} = 1.6 \times 0.0296/(420\times10^{-6} \times 0.65) = 0.0474/2.73\times10^{-4} \approx 173$, about 46% of that of a C3 leaf under the same conditions.

   (c) The $\ce{CO2}$-concentrating mechanism of the C4 leaf keeps Rubisco close to saturation at low $c_{\mathrm{i}}$, so photosynthesis can be maintained with a smaller stomatal conductance, and each unit of water lost yields about twice as much carbon. This advantage is most pronounced in dry air (large $D$), at high temperature (strong photorespiration, high $\Gamma^*$) and in strong light; in cool, humid, low-light environments, the extra 2 ATP or so that C4 pays for each $\ce{CO2}$ fixed (Eq. (8.5)) removes its advantage (Section 30.3.2).

3. On a maize field at peak growth, one day's intercepted PAR is $8\,\mathrm{MJ\,m^{-2}}$, the radiation-use efficiency is $3.5\,\mathrm{g\,MJ^{-1}}$, dry matter contains 45% carbon and 1.2% nitrogen, the transpiration ratio (molar) is 150, and respiration is assumed to consume 40% of the carbon fixed. Estimate the dry matter increment per square meter that day, the total $\ce{CO2}$ assimilated by the canopy, the amount of water transpired and the nitrogen that must be taken up. Compare with the wheat of Example 30.4.1: what do the water and nitrogen consumption each show?

   **Answer** Dry matter $8 \times 3.5 = 28\,\mathrm{g\,m^{-2}}$, containing $12.6\,\mathrm{g} = 1.05\,\mathrm{mol}$ of carbon; total canopy assimilation $1.05/0.6 = 1.75\,\mathrm{mol\,CO_2}$. Transpiration is $1.75 \times 150 = 263\,\mathrm{mol}$ of water, about $4.7\,\mathrm{kg\,m^{-2}}$ (4.7 mm). The nitrogen requirement is $28 \times 0.012 = 0.34\,\mathrm{g}$, about 24 mmol.

   Compared with wheat (about 25 g of dry matter, 5–11 mm of transpiration), maize gains slightly more dry matter while transpiring only about as much as the lower wheat estimate and less than half of the upper one, which is the water-use efficiency advantage of the C4 pathway (Section 30.3.2). The nitrogen requirement is similar to wheat's while the tissue nitrogen concentration is lower, reflecting less Rubisco and a higher photosynthetic efficiency per unit nitrogen in C4 leaves. On the other hand, less transpiration also means less nitrate delivered by mass flow (4.7 L × 2 mM ≈ 9 mmol, less than 40% of the requirement), so maize depends more on diffusion and root growth to acquire nitrogen.

4. Use the two mechanisms of Section 30.6 (threshold accumulation and positive feedback) to explain: (a) why winter wheat that meets a few cold days in autumn does not flower in winter; (b) why a climacteric fruit that has begun to ripen continues to ripen even when exogenous ethylene is removed; (c) why a seed does not germinate after a single light shower.

   **Answer** (a) Vernalization requires the accumulation of enough effective cold (Eq. (22.1)); a few cold days only shorten slightly the number of days needed for flowering. Moreover, even after vernalization is complete, most winter wheats still need long days (the photoperiod pathway) to flower, and the short days of autumn and winter do not meet this condition. The integration of the two pathways (*VRN1* ⊣ *VRN2* ⊣ *FT*) allows flowering to occur only in spring.

   (b) Synthesis of system 2 ethylene is promoted by ethylene itself (*ACS* and *ACO* are induced by ethylene), and Eq. (23.5) has two stable states when $k_1$ is large enough; once the ethylene concentration passes the unstable point, the system jumps to the high-ethylene stable state and sustains itself (irreversibility after a saddle-node bifurcation), and exogenous ethylene is merely the trigger that pushes the system over the threshold.

   (c) Germination requires the accumulation of enough hydrotime (Eq. (20.1)): only when the water potential stays above the base water potential $\Psi_{\mathrm{b}}$ for long enough does the seed complete the repair and metabolic preparation of phase II. After a light shower the soil dries quickly, accumulation is insufficient, and the imbibed seed remains in a reversible phase. A dormant seed must first have its dormancy released by a change in the ABA/GA balance. Everything before radicle emergence is reversible; only emergence is the irreversible "decision."

5. (Open question) From the whole course choose one example each to show the following three cases of "the same molecule having different meanings at different scales": (a) ABA; (b) ethylene; (c) sucrose.

   **Answer** Points for reference:

   (a) ABA: at the molecular scale it is a signal in which PYR/PYL receptors inhibit PP2C and release SnRK2 ([7.1.15](/7.1.15)); at the cellular scale it opens anion channels in guard cells and lowers turgor ([7.13.10](/7.13.10)); at the whole-plant scale it is a signal that reports soil drought from the roots through the xylem, with its distribution regulated by xylem pH ([7.13.15](/7.13.15)); at the life-history scale it establishes seed dormancy and desiccation tolerance ([7.13.20](/7.13.20), [7.13.23](/7.13.23)).

   (b) Ethylene: at the molecular scale it acts by derepression through ETR–CTR1–EIN2; in seedlings it causes the triple response, which helps to push through the soil ([7.13.20](/7.13.20)); in flooding it induces aerenchyma and the internode elongation of deepwater rice ([7.13.27](/7.13.27)); in fruit it is an autocatalytic switch that makes ripening irreversible ([7.13.23](/7.13.23)); in abscission zones it determines the timing of organ shedding ([7.13.24](/7.13.24)).

   (c) Sucrose: it is the transport form of photosynthetic products and a respiratory substrate ([7.13.11](/7.13.11), [7.13.12](/7.13.12)); it is the osmotic driving substance of pressure flow (Eqs. (11.1)–(11.3)); it is an osmoticum in guard cells in the afternoon ([7.13.10](/7.13.10)); it is a signal that starts the outgrowth of axillary buds after apical dominance is released ([7.13.18](/7.13.18)) and takes part, via trehalose 6-phosphate, in the nutritional pathway to flowering ([7.13.22](/7.13.22)). That the same molecule means different things at different scales is exactly why the plant must be understood as a system.
