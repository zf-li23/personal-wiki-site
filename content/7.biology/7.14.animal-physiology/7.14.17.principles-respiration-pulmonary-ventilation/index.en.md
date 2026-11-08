---
title: Principles of Respiration and Pulmonary Ventilation
description: Why aerobic respiration is needed; the relay of bulk flow and diffusion; partial pressure, Henry's law and Fick's law; water and air as respiratory media (human versus tuna); the maximum radius of a diffusion-limited organism; tidal and unidirectional ventilation, and the efficiency of concurrent, countercurrent, crosscurrent and pool exchangers (analytical solutions); respiratory muscles, alveolar pressure, intrapleural pressure and transpulmonary pressure; lung compliance, airway resistance and the work of breathing; lung volumes and capacities, forced expiration; anatomical and physiological dead space, alveolar ventilation; renewal of alveolar gas and the alveolar gas equation; evolution and comparison of skin, gills, lungs and tracheae, ram ventilation, the buccal pump, avian air sacs and parabronchi, the insect tracheal system and Paleozoic giant insects.
source_hash: 4050b61b9299
---

Every cell of an animal must continuously receive $\ce{O2}$ and discharge $\ce{CO2}$. At the micrometer scale diffusion is sufficient for this; at the centimeter scale it falls far short: a large animal must use a respiratory organ to bring the external medium (water or air) to a thin, extensive exchange membrane, and a circulatory system to bring blood to the other side of the membrane. This chapter is the general introduction to the respiratory system. We first explain why respiration is needed, what physical laws govern gas exchange (Sections 17.1 and 17.2), how the two media, water and air, impose different constraints on the design of an exchanger, and how the efficiencies of countercurrent, crosscurrent and other modes of exchange compare (Section 17.3); then we describe how the human lung draws air in and out: the respiratory muscles and the pleural cavity, the elasticity of the lung and airway resistance (Section 17.4), how ventilation is measured by lung volumes and ventilatory flows (Section 17.5), and how ventilation determines the composition of alveolar gas (Section 17.6). Finally we compare the respiratory organs and modes of ventilation of fishes, amphibians, birds and insects (Section 17.7). The structure of the **alveolus**, surface tension and the **pulmonary circulation** are the subject of Chapter 18, gas exchange in lung and tissue and gas transport in blood are Chapter 19, and neural control of breathing is Chapter 20. Lung development is in [7.5.30](/7.5.30), and the general account of the circulatory system is in Chapter 12.

## 17.1. Why a Respiratory System Is Needed

### 17.1.1. The Demand of Aerobic Metabolism

The basic way animals obtain energy is to oxidize organic compounds and store the released free energy in ATP ([7.1.16](/7.1.16)). Aerobic oxidation with $\ce{O2}$ as the final electron acceptor (**oxidative phosphorylation**, [7.1.23](/7.1.23)) yields about 30 ATP per glucose molecule, whereas anaerobic **glycolysis** yields only 2 ([7.1.18](/7.1.18)). A high metabolic rate, many systems working at once, continuous growth and repair, and sophisticated neural activity all rest on the high yield of aerobic metabolism; in hypoxia cells can only fall back on inefficient anaerobic metabolism, barely enough to sustain basic survival. The human brain makes up 2% of body weight and consumes about 20% of resting oxygen uptake; consciousness is lost within seconds of interruption of cerebral blood flow, and irreversible damage begins within minutes.

Neither $\ce{O2}$ nor $\ce{CO2}$ can be stored in large amounts in the body: the human $\ce{O2}$ reserve (gas in the lungs, oxygen bound to hemoglobin and myoglobin, dissolved oxygen) totals about $1.5\,\mathrm{L}$, enough for only about 6 minutes at a resting oxygen uptake of $250\,\mathrm{mL\,min^{-1}}$. Gas exchange must therefore proceed without interruption throughout life.

**Definition 17.1.1 (Respiration)** The process of gas exchange between the organism and the external environment is called **respiration**. Human respiration comprises four linked steps: pulmonary ventilation (gas exchange between the outside air and the alveoli) and pulmonary gas exchange (exchange between the alveoli and the blood of the pulmonary capillaries), together called external respiration; transport of gases in the blood; gas exchange between the blood of the tissue capillaries and the tissue cells (tissue gas exchange, or internal respiration); and the regulation that matches these steps to metabolic needs.

The consumption of $\ce{O2}$ by mitochondria within cells is called **cellular respiration** in biochemistry, and is the other end of the same chain as the "respiration" discussed here.

### 17.1.2. The Relay of Bulk Flow and Diffusion

$\ce{O2}$ travels from the air to the **mitochondria** in four steps, alternating two modes of transport:

| Step | Mode of transport | Driving force | Structure in the human body |
|---|---|---|---|
| 1. Ventilation | Bulk flow (convection) | Pressure difference produced by respiratory muscles | Airways, alveoli |
| 2. Pulmonary gas exchange | Diffusion | Partial pressure difference of $\ce{O2}$ | **Respiratory membrane** (about $0.6\,\mathrm{\mu m}$ thick) |
| 3. Transport in blood | Bulk flow | Pressure difference produced by the heart | Circulatory system, hemoglobin |
| 4. Tissue gas exchange | Diffusion | Partial pressure difference | Capillary wall, interstitium (a few to tens of micrometers) |

Bulk flow covers long distances quickly, and diffusion is responsible only for the last short distance (Chapter 12, Section 12.1.1: diffusion time $\propto$ distance squared). $\ce{CO2}$ travels the same path in the opposite direction. The transport capacity of every link in the chain must match the metabolic rate: in exercise oxygen consumption can increase more than tenfold, and ventilation, **cardiac output** and tissue $\ce{O2}$ extraction must all increase accordingly.

## 17.2. The Physics of Gas Exchange

### 17.2.1. Partial Pressure and Dissolution

Each gas in a gas mixture exerts a pressure as though it alone occupied the whole container; this is its **partial pressure**, and the total pressure is the sum of the partial pressures (**Dalton's law of partial pressures**, [6.1.1](/6.1.1)). The net direction of flow of gas molecules across a cross-section is determined by partial pressure, not total pressure: when the total pressures on the two sides are equal, $\ce{O2}$ still flows from the side of higher $\ce{O2}$ partial pressure to that of lower.

Atmospheric pressure at sea level is $760\,\mathrm{mmHg}$ ($101.3\,\mathrm{kPa}$; $1\,\mathrm{mmHg} = 0.1333\,\mathrm{kPa}$; in physiology gas partial pressures and blood pressures are customarily given in mmHg). In dry air $\ce{O2}$ is 20.93%, $\ce{N2}$ (together with a little Ar) about 79% and $\ce{CO2}$ only 0.04%, so

$$
P_{\ce{O2}} = 0.2093 \times 760\,\mathrm{mmHg} \approx 159\,\mathrm{mmHg}\ (21.2\,\mathrm{kPa}),\qquad P_{\ce{N2}} \approx 600\,\mathrm{mmHg}.
$$

Inspired air is warmed to $37\,^\circ\mathrm{C}$ in the airways and saturated with water vapor; the saturated vapor pressure of water at $37\,^\circ\mathrm{C}$ is $47\,\mathrm{mmHg}$ ($6.3\,\mathrm{kPa}$), which depends on body temperature and not on atmospheric pressure. The remaining gases are diluted, and in the humidified air entering the airways

$$
P_{\mathrm{IO_2}} = 0.2093 \times (760 - 47)\,\mathrm{mmHg} \approx 149\,\mathrm{mmHg}.
$$

At altitude atmospheric pressure falls while the 47 mmHg stays constant, so the proportion diluted by water vapor is larger: at $8848\,\mathrm{m}$ atmospheric pressure is about $253\,\mathrm{mmHg}$ and $P_{\mathrm{IO_2}} = 0.2093 \times 206 \approx 43\,\mathrm{mmHg}$.

When a gas is in contact with a liquid, molecules are exchanged back and forth between the two phases, and at equilibrium the concentration of dissolved gas in the liquid is proportional to the partial pressure of that gas in the gas phase (**Henry's law**, [6.3.5](/6.3.5)):

$$
c = \alpha P,
\tag{17.1}
$$

where $\alpha$ is the solubility (dependent on gas, solvent and temperature). At equilibrium the gas in the liquid also has a "partial pressure", namely the partial pressure of the gas phase in equilibrium with it; when physiologists say that the $P_{\ce{O2}}$ of blood is $40\,\mathrm{mmHg}$, this is the quantity they mean. Between two liquids, or between a liquid and a gas, gas always diffuses from the place of higher partial pressure to that of lower, even if the concentration is higher on the low-pressure side (for example between two liquids of different solubility).

| Gas | Solubility in plasma ($37\,^\circ\mathrm{C}$) | Relative to $\ce{O2}$ |
|---|---|---|
| $\ce{O2}$ | $0.003\,\mathrm{mL}/(100\,\mathrm{mL} \cdot \mathrm{mmHg})$ | 1 |
| $\ce{CO2}$ | $0.067\,\mathrm{mL}/(100\,\mathrm{mL} \cdot \mathrm{mmHg})$ | about 22–24 |
| $\ce{N2}$ | $0.0015\,\mathrm{mL}/(100\,\mathrm{mL} \cdot \mathrm{mmHg})$ | about 0.5 |

### 17.2.2. Fick's Law of Diffusion

For diffusion through a barrier of thickness $\Delta x$ and area $A$, the amount of gas passing per unit time obeys **Fick's law** ([2.5.1](/2.5.1)):

**Formula 17.2.1 (Diffusion of a Gas across a Membrane)**

$$
\dot V = \frac{A}{\Delta x}\, D\, \alpha\, (P_1 - P_2) = \frac{A}{\Delta x}\, K\, \Delta P,
\tag{17.2}
$$

where $D$ is the **diffusion coefficient** of the gas in the barrier, $\alpha$ is the solubility, and $K = D\alpha$ is called the Krogh diffusion constant.

Equation (17.2) lists all the factors an exchanger can adjust: the properties of the medium ($D$, $\alpha$), the exchange area $A$ (large), the diffusion distance $\Delta x$ (short) and the partial pressure difference $\Delta P$ (large). The evolution of the respiratory system can be seen as optimization of these four terms: the total alveolar area is about $70\,\mathrm{m^2}$, the thickness of the respiratory membrane is less than $1\,\mathrm{\mu m}$, and ventilation and blood flow maintain the partial pressure difference.

$D$ is inversely proportional to the square root of molecular weight (Graham's law); $\ce{CO2}$ is heavier than $\ce{O2}$ and its $D$ is slightly smaller ($\sqrt{32/44} \approx 0.85$), but its solubility is 24 times greater, so $K_{\ce{CO2}} \approx 20\,K_{\ce{O2}}$. Across the same barrier, $\ce{CO2}$ needs only about 1/20 of the partial pressure difference of $\ce{O2}$ to diffuse at the same rate. This is why the $P_{\ce{CO2}}$ difference between venous blood and alveolar gas is only about 6 mmHg while the $P_{\ce{O2}}$ difference is about 60 mmHg (Chapter 19).

### 17.2.3. Water and Air as Respiratory Media

At the same partial pressure, the $\ce{O2}$ concentration in air is far higher than in water, because the solubility of $\ce{O2}$ in water is very low. The physical properties of the two media differ by several orders of magnitude ($20\,^\circ\mathrm{C}$, in equilibrium with air):

| Property | Air | Water | Air/water |
|---|---|---|---|
| $\ce{O2}$ content | $\approx 280\,\mathrm{mg\,L^{-1}}$ ($210\,\mathrm{mL\,L^{-1}}$) | $\approx 9\,\mathrm{mg\,L^{-1}}$ (fresh water); $5$–$7\,\mathrm{mg\,L^{-1}}$ (warm seawater) | 30–56 |
| Diffusion coefficient of $\ce{O2}$ | $0.2\,\mathrm{cm^2\,s^{-1}}$ | $2 \times 10^{-5}\,\mathrm{cm^2\,s^{-1}}$ | about $10^4$ |
| Density | $1.2\,\mathrm{kg\,m^{-3}}$ | $1000\,\mathrm{kg\,m^{-3}}$ | about 1/800 |
| Viscosity | $1.8 \times 10^{-5}\,\mathrm{Pa\,s}$ | $1.0 \times 10^{-3}\,\mathrm{Pa\,s}$ | about 1/55 |
| Ratio of capacities for $\ce{CO2}$ and $\ce{O2}$ | about 1 | about 28 | — |

There are three consequences for animals. First, obtaining the same amount of $\ce{O2}$ from water requires processing a medium volume tens of times larger, and water is heavy and viscous, so pumping it is costly: respiration costs fishes about 10% of total metabolism (5%–15% in different species), but only 1%–2% in resting humans. Second, diffusion in water is ten thousand times slower, so the water layer on the gill must be very thin and constantly renewed, with spacing between gill lamellae of only tens of micrometers. Third, $\ce{CO2}$ is highly soluble in water, so water breathers excrete $\ce{CO2}$ easily and blood $P_{\ce{CO2}}$ is only 2–5 mmHg, which affects the signals on which respiratory control relies (Chapter 20, Section 20.7) and acid–base regulation (Chapter 25).

**Example 17.2.1 (Human and tuna)** The table below compares an adult human with a rapidly swimming tuna of similar body weight (values are rough orders of magnitude; tuna data vary greatly with species and size):

| Parameter | Human (air breathing) | Tuna (seawater breathing) | Remark |
|---|---|---|---|
| Medium processed at rest | $6$–$7.5\,\mathrm{L\,min^{-1}}$ | of the order of $10^2\,\mathrm{L\,min^{-1}}$ | Water breathing requires processing tens of times the volume |
| Medium processed during activity | $20$–$200\,\mathrm{L\,min^{-1}}$ | Several hundred $\mathrm{L\,min^{-1}}$ | |
| $\ce{O2}$ in medium | $\approx 280\,\mathrm{mg\,L^{-1}}$ | $5$–$7\,\mathrm{mg\,L^{-1}}$ | 40–56-fold difference |
| Fraction extracted from medium | about 20% | 30%–50% (countercurrent exchange, Section 17.3.3) | Efficient exchanger, but it cannot make up the difference in the medium |
| Respiratory cost as fraction of total metabolism | 1%–2% | about 10% | Density and viscosity of water |
| Exchange area | Alveoli $70$–$100\,\mathrm{m^2}$ | Gill area the largest among fishes, per body weight several times that of typical fishes | |

The strategy of the tuna is ram ventilation (Section 17.7.2): it swims with the mouth open, letting its forward speed force water over the gills, so that the cost of pumping water is absorbed into the cost of swimming.

### 17.2.4. Body Size and the Limit of Diffusion

How large can an organism be if it relies on diffusion alone for oxygen? Consider a spherical organism of radius $R$ whose tissue consumes oxygen uniformly at a rate $M$ per unit volume, with surface $\ce{O2}$ concentration kept at $c_0$, in equilibrium with the environment. In the steady state the $\ce{O2}$ concentration satisfies $D\nabla^2 c = M$ (the steady-state form of the diffusion equation, [2.5.1](/2.5.1)), and the spherically symmetric solution is

$$
c(r) = c_0 - \frac{M}{6D}\left(R^2 - r^2\right).
$$

The radius at which the central concentration falls to 0 is the maximum radius.

**Formula 17.2.2 (Maximum Size for Diffusive Oxygen Supply)**

$$
R_{\max} = \sqrt{\frac{6Dc_0}{M}}\ (\text{sphere}),\qquad R_{\max} = \sqrt{\frac{4Dc_0}{M}}\ (\text{long cylinder}),\qquad L_{\max} = \sqrt{\frac{2Dc_0}{M}}\ (\text{half-thickness of a slab}).
\tag{17.3}
$$

This estimate was given by Harvey (1928) and Krogh, and shows that the scale of diffusion limitation shrinks as the square root of the metabolic rate.

**Example 17.2.2 (The 1 mm limit)** In animal tissue $D \approx 2 \times 10^{-9}\,\mathrm{m^2\,s^{-1}}$; water in equilibrium with air at $25\,^\circ\mathrm{C}$ has $c_0 \approx 0.25\,\mathrm{mol\,m^{-3}}$. A resting human consumes $250\,\mathrm{mL\,min^{-1}}$ of oxygen (about $11\,\mathrm{mmol\,min^{-1}}$); averaged over $70\,\mathrm{kg}$ (about $0.07\,\mathrm{m^3}$) of tissue, $M \approx 2.6 \times 10^{-3}\,\mathrm{mol\,m^{-3}\,s^{-1}}$. Substituting in Eq. (17.3), a spherical organism has $R_{\max} = \sqrt{6 \times 2 \times 10^{-9} \times 0.25 / 2.6 \times 10^{-3}} \approx 1.1\,\mathrm{mm}$. For an organism with a ten-fold lower metabolic rate (such as a jellyfish or flatworm), $R_{\max}$ increases only to about $3.4\,\mathrm{mm}$; a flat body shape is not limited by radius but only by half-thickness, so a planarian can grow to several centimeters in length while only a few tenths of a millimeter thick.

:::

As body size increases, oxygen consumption $\propto R^3$ and body surface area $\propto R^2$, so the exchange area per unit volume falls as $1/R$, while the diffusion time from surface to center $\propto R^2$ increases. Besides transporting material by bulk flow (Chapter 12), organisms can make their body surface convoluted, make the body slender or flat, or develop specialized exchange membranes of enormous area.

## 17.3. The Design of Ventilation and Perfusion

### 17.3.1. Three Strategies of Larger Organisms

- Letting external water flow through the body: sponges use the flagella of choanocytes to drive water through a system of channels inside the body, so that each cell obtains $\ce{O2}$ directly from the passing water.
- Using the whole body surface as the exchange surface and the circulatory system for transport: earthworms and many amphibians (cutaneous respiration). Salamanders of the family Plethodontidae have neither lungs nor gills and exchange gases only through the skin and the oral mucosa; they are small, have a low metabolic rate, and live in cool, moist environments.
- Developing specialized respiratory membranes (gills, lungs, tracheae), using ventilation to maintain the partial pressure on the outside of the membrane and perfusion (blood flow) to maintain the partial pressure on the inside. This is the solution of large animals.

A specialized respiratory membrane requires two flows: ventilation of the medium and perfusion of the blood. The efficiency of exchange depends on the relative direction of the two flows and the mode of ventilation.

### 17.3.2. Tidal Ventilation and Unidirectional Flow

The lung is a blind sac and can be ventilated only in a tidal manner: the same passage serves inspiration and expiration, and the direction of flow of the medium periodically reverses. Tidal ventilation has two inherent drawbacks: each breath of fresh air mixes with the old gas remaining in the lung (a human renews only about 1/7 with each breath, Section 17.6.1), so the alveolar $P_{\ce{O2}}$ is always lower than that of the environment; and there is a segment of the passage, the dead space, that takes no part in exchange (Section 17.5.2). The alveoli of mammals are equivalent to a ventilated "pool": the gas in the pool is thoroughly mixed, and the blood faces a uniform partial pressure.

Fish gills and bird lungs have unidirectional (flow-through) ventilation: the medium enters at one end and leaves at the other, with no dead space or mixing, and the relative direction of medium and blood can be arranged. Heavy, viscous water is unsuited to tidal movement in and out (each reversal requires accelerating a large mass of water), and all vertebrates that breathe water with gills use unidirectional flow.

### 17.3.3. Concurrent, Countercurrent and Crosscurrent Flow

**Definition 17.3.1 (Concurrent, Countercurrent and Crosscurrent Exchange)** When two fluids flow on either side of a membrane across which material (or heat) can be exchanged, the arrangement in which they flow in the same direction is called **concurrent exchange**; the arrangement in which they flow in opposite directions is called **countercurrent exchange**; and the arrangement in which one fluid flows in one direction while the other is divided into many parallel streams that flow across it perpendicularly and join downstream is called **crosscurrent exchange**.

Countercurrent exchange recurs again and again in physiology: fish gills, the **rete mirabile** of the swim bladder (Chapter 19), the vasa recta of the renal medulla (Chapter 24), **countercurrent heat exchange** in the limbs (Chapter 31). Its efficiency can be compared with a linear model.

**Formula 17.3.1 (Efficiency of Exchangers)** Let the medium enter at partial pressure $P_I$ and the blood at venous partial pressure $P_v$; the capacity of each fluid for the gas (the amount of gas per unit change of partial pressure) is constant, and flow times capacity is written as the "capacity rates" $C_{\mathrm{blood}}$ and $C_{\mathrm{medium}}$; the total diffusive conductance of the exchanger is $G$. Write

$$
D^* = \frac{G}{C_{\mathrm{blood}}},\qquad r = \frac{C_{\mathrm{blood}}}{C_{\mathrm{medium}}},\qquad E = \frac{P_a - P_v}{P_I - P_v},
$$

where $E$ is the relative partial pressure reached by arterial (outflowing) blood. For the four designs,

$$
\begin{aligned}
\text{concurrent:}\quad & E = \frac{1 - \mathrm{e}^{-D^*(1+r)}}{1 + r}, \\
\text{ventilated pool (alveolus):}\quad & E = \frac{1 - \mathrm{e}^{-D^*}}{1 + r\left(1 - \mathrm{e}^{-D^*}\right)}, \\
\text{crosscurrent (avian parabronchus):}\quad & E = \left(1 - \mathrm{e}^{-D^*}\right)\frac{1 - \mathrm{e}^{-\lambda}}{\lambda},\quad \lambda = r\left(1 - \mathrm{e}^{-D^*}\right), \\
\text{countercurrent (fish gill):}\quad & E = \frac{1 - \mathrm{e}^{-D^*(1-r)}}{1 - r\,\mathrm{e}^{-D^*(1-r)}}\quad \left(\text{for } r = 1,\ E = \frac{D^*}{1 + D^*}\right).
\end{aligned}
\tag{17.4}
$$

These expressions are obtained by integrating mass conservation along the exchanger (Piiper and Scheid, 1970s) and are the same as the "effectiveness–number of transfer units" relations of heat exchangers in engineering.

![Efficiency of the four exchange designs (Formula 17.3.1, linear model). A: relative partial pressure $E$ reached by arterial blood as a function of the relative diffusive conductance $D^*$ for equal capacity rates ($r = 1$). Countercurrent (red) tends to 1 for large enough $D^*$, i.e., the blood can nearly reach the partial pressure of the inflowing medium; crosscurrent (green) tends to $1 - \mathrm{e}^{-1} \approx 0.63$; the ventilated pool (blue, mammalian alveolus) and concurrent flow (gray dashed) both tend only to 0.5, and at finite $D^*$ the pool is slightly lower than concurrent flow because the blood faces alveolar gas that has already been "used" and is identical to the expired gas. B: partial pressure profiles along the exchanger for $D^* = 3$ and $r = 1$, with the abscissa measured from the blood inlet. In concurrent flow (gray dashed) the two fluids quickly approach a common intermediate value and no further exchange occurs; in countercurrent flow they keep a constant partial pressure difference along the whole length, and the blood outlet (right end of the red line) is above the medium outlet (left end of the blue line). C: the upper limit as $D^* \to \infty$ as a function of $r$: only countercurrent flow can give $E = 1$ (when the capacity rate of the blood does not exceed that of the medium, $r \le 1$).](./plots/exchanger-designs.py)

The conclusions of the model agree with measurements:

- Countercurrent flow is the only design in which the partial pressure of outflowing blood can exceed that of the outflowing medium. In fish gills the $P_{\ce{O2}}$ of water leaving the lamellae can be lower than that of the outflowing arterial blood, and the fish can extract 50%–80% of the $\ce{O2}$ from the water. When the direction of water flow in an experimental fish is reversed (making the exchange concurrent), the extraction falls to about 10%.
- The efficiency of crosscurrent exchange lies between the two, and it can also make arterial $P_{\ce{O2}}$ higher than that of expired gas; this is part of the reason birds can maintain a relatively high arterial $P_{\ce{O2}}$ at high altitude (Section 17.7.4).
- The mammalian alveolus is the least efficient ventilated pool: arterial blood can at best equilibrate with alveolar gas, and alveolar gas is itself lower than inspired gas because of the mixing of tidal ventilation. Mammals compensate with an enormous diffusive conductance ($D^*$ very large) and a large ventilation.
- Real blood contains hemoglobin, and its capacity varies with partial pressure (the S-shaped curve of Chapter 19); Eq. (17.4) is only a linearized comparison, and uneven ventilation and blood flow (Chapter 18, Section 18.6) lower the efficiency further.

## 17.4. Mechanics of Pulmonary Ventilation

### 17.4.1. The Airways and the Lung

Air enters the trachea through the nose (or mouth), pharynx and larynx. The trachea bifurcates repeatedly within the thorax: the trachea is generation 0 and the main bronchi are generation 1, followed successively by lobar bronchi, segmental bronchi, bronchioles and terminal bronchioles (about generation 16), then respiratory bronchioles and alveolar ducts, ending in the alveolar sacs of generation 23. The first 16 generations only conduct gas and are called the conducting zone, whose volume is the anatomical dead space; from generation 17 on, the walls bear alveoli, and this is called the respiratory zone. With each bifurcation the diameter of a single tube becomes smaller but the number of tubes doubles, and the total cross-sectional area increases rapidly: in the respiratory zone the total cross-sectional area reaches hundreds of square centimeters, the forward velocity of the airflow falls to a very low value, and in the last stretch gas mixes mainly by diffusion.

The conducting zone is more than a set of pipes. The nasal cavity and airways warm the inspired air to body temperature and saturate it with water vapor; mucus and cilia work together to move trapped particles toward the pharynx, to be cleared by coughing or swallowing (**mucociliary clearance**, Chapter 2); particles larger than about $10\,\mathrm{\mu m}$ are mostly filtered out in the nasal cavity, smaller particles enter the lower airways, and those reaching the alveoli are phagocytosed by alveolar macrophages. The walls from the trachea to the terminal bronchioles contain smooth muscle under dual autonomic innervation: the parasympathetic (vagus nerve, ACh acting on $\mathrm{M_3}$ receptors) constricts it, and circulating **epinephrine** relaxes it through $\beta_2$ receptors (Chapter 7); inflammatory mediators such as histamine and leukotrienes constrict it (asthma).

### 17.4.2. Respiratory Muscles and Respiratory Movement

The lung itself has no muscle and can only expand and recoil passively with the enlargement and reduction of the thorax. The thorax is driven by the respiratory muscles, enlarging and shrinking rhythmically, which is called respiratory movement.

| Respiratory muscle | Action | When involved |
|---|---|---|
| Diaphragm (phrenic nerve, $\mathrm{C_3}$–$\mathrm{C_5}$) | On contraction the dome descends 1–2 cm (up to 10 cm in deep inspiration), increasing the vertical dimension of the thorax | The main muscle of quiet inspiration, about 2/3–3/4 of the tidal volume |
| External intercostals | Raise the ribs and sternum, increasing the anteroposterior and transverse dimensions of the thorax | Quiet inspiration |
| Accessory inspiratory muscles such as the scalenes and sternocleidomastoid | Raise the upper ribs and sternum | Forced inspiration |
| Internal intercostals | Pull the ribs down | Forced expiration |
| Abdominal muscles | Raise intra-abdominal pressure, pushing the diaphragm up into the thorax | Forced expiration, coughing |

In quiet breathing, inspiration is active and expiration is passive: after the inspiratory muscles relax, the elastic recoil of the stretched lung and thorax shrinks the thorax and expels gas. In forced breathing expiration also becomes active. Breathing mainly by movement of the diaphragm is called abdominal breathing, and breathing mainly by the intercostal muscles is called thoracic breathing; normally both are present together, thoracic breathing predominating in late pregnancy or with ascites, and abdominal breathing in pleurisy or rib fracture. The phrenic nerve arises from the cervical spinal cord, so injury of the high cervical cord (above $\mathrm{C_3}$) stops spontaneous breathing, whereas injury of the lower cervical cord spares diaphragmatic breathing.

### 17.4.3. Alveolar Pressure and Intrapleural Pressure

Between the visceral pleura on the surface of the lung and the parietal pleura on the inner surface of the chest wall lies a closed potential space holding only a few milliliters of serous fluid. The liquid film lets the two pleurae slide on each other but not separate, like two wet panes of glass. This fluid is continuously exchanged with lymph, and continuous lymphatic drainage keeps the pleural cavity at negative pressure.

**Definition 17.4.1 (Alveolar Pressure, Intrapleural Pressure and Transpulmonary Pressure)** The pressure of the gas in the alveoli is called the **alveolar pressure** $P_{\mathrm{alv}}$. The pressure within the pleural cavity is called the **intrapleural pressure** $P_{\mathrm{pl}}$. The difference between the two

$$
P_{\mathrm{L}} = P_{\mathrm{alv}} - P_{\mathrm{pl}}
$$
is called the **transpulmonary pressure**; it is the pressure that keeps the lung expanded and balances the elastic recoil of the lung. All pressures here are measured with atmospheric pressure as zero.

The lung in the thorax is always under tension: after birth the thorax grows faster than the lung, and the natural volume of the thorax is greater than that of the lung. The lung tends to recoil and the thorax to spring outward, and the two pull on each other through the liquid film of the pleural cavity, making intrapleural pressure lower than atmospheric. At the end of inspiration or expiration, when flow stops and $P_{\mathrm{alv}} = 0$,

$$
P_{\mathrm{pl}} = -(\text{elastic recoil pressure of the lung}).
$$

At the end of quiet expiration $P_{\mathrm{pl}}$ is about $-5\,\mathrm{cmH_2O}$ (about $-0.5\,\mathrm{kPa}$, $-4\,\mathrm{mmHg}$), and at the end of quiet inspiration about $-7.5\,\mathrm{cmH_2O}$. In quiet breathing intrapleural pressure is always negative; it becomes positive only in forced expiration (Section 17.4.5), and straining against a closed glottis (as in coughing or defecation) can raise it greatly.

The pressure changes during one quiet breath:

1. Before inspiration begins, the glottis is open, flow has stopped and $P_{\mathrm{alv}} = 0$.
2. The inspiratory muscles contract and the thorax enlarges; $P_{\mathrm{pl}}$ becomes more negative, the transpulmonary pressure increases and the lung is pulled open; the increase in lung volume makes $P_{\mathrm{alv}}$ negative (about $-1\,\mathrm{cmH_2O}$) and air flows in. At the end of inspiration flow stops and $P_{\mathrm{alv}}$ returns to 0.
3. The inspiratory muscles relax, the lung and thorax recoil, $P_{\mathrm{alv}}$ becomes positive (about $+1\,\mathrm{cmH_2O}$) and air flows out.

The significance of the negative intrapleural pressure is to keep the lung expanded and to lower the pressure in the large intrathoracic veins and the right atrium, which favors **venous return** (Chapter 14). When the chest wall or the lung surface is ruptured and air enters the pleural cavity (pneumothorax), the negative pressure vanishes and the lung collapses by its own elastic recoil.

### 17.4.4. Lung Compliance and Elastic Resistance

Ventilation must overcome two kinds of resistance: elastic resistance (the elastic recoil of the lung and thorax when expanded, which persists when flow stops, about 70% of the total resistance of quiet breathing) and non-elastic resistance (airway resistance, viscous resistance of tissue and inertia, which appear only when there is flow, about 30%).

**Definition 17.4.2 (Lung Compliance)** The change in lung volume produced by a unit change in transpulmonary pressure is called **lung compliance**:

$$
C_{\mathrm{L}} = \frac{\Delta V}{\Delta P_{\mathrm{L}}}.
$$

The reciprocal of compliance is elastic resistance. The lung compliance of a normal adult is about $200\,\mathrm{mL/cmH_2O}$ ($2\,\mathrm{L\,kPa^{-1}}$), and the compliance of the thorax is also about $200\,\mathrm{mL/cmH_2O}$; lung and thorax are in series, and the total compliance is about $100\,\mathrm{mL/cmH_2O}$.

The pressure–volume curve of the lung (Chapter 18) is S-shaped: it is steepest in the middle section near the functional residual capacity, where compliance is greatest, so quiet breathing takes the least effort; near total lung capacity the curve flattens and the lung is stretched to its limit. The size of the lung affects compliance (a large lung changes volume more at the same pressure), so when comparing individuals one uses specific compliance (compliance divided by functional residual capacity).

The elastic recoil of the lung has two sources: about 1/3 comes from the elastic and collagen fibers in the lung tissue, and about 2/3 from the **surface tension** of the liquid film lining the alveoli. The evidence is the comparison of inflation with air and with saline: saline eliminates the air–liquid interface, and the pressure needed to reach the same volume is only about 1/3 of that for air inflation. The **pulmonary surfactant** in the alveolar liquid film greatly lowers this surface tension; surface tension, the stability of alveoli and the hysteresis of the pressure–volume curve are the subject of Chapter 18.

Compliance changes in disease: pulmonary fibrosis, **pulmonary edema** and surfactant deficiency (neonatal respiratory distress syndrome) lower compliance and make breathing laborious; in emphysema the elastic fibers are destroyed and compliance rises, but the recoil of the lung is insufficient and expiration is difficult.

### 17.4.5. Airway Resistance

For airflow through the airways, the ratio of driving pressure to flow is the airway resistance:

$$
R_{\mathrm{aw}} = \frac{P_{\mathrm{mouth}} - P_{\mathrm{alv}}}{\dot V}.
$$

The airway resistance of a normal adult is about $1.5$–$2\,\mathrm{cmH_2O\,s\,L^{-1}}$, so in quiet breathing a flow of $0.5\,\mathrm{L\,s^{-1}}$ needs a pressure difference of only about $1\,\mathrm{cmH_2O}$. In **laminar flow** the resistance of a single tube follows the **Hagen–Poiseuille law** ([7.6.22](/7.6.22)), inversely proportional to the fourth power of the radius; in the trachea and large bronchi the flow is fast and the **Reynolds number** is high, so the flow shows **turbulence** or is transitional, and the resistance also increases with flow.

A counterintuitive fact is that the main part of the resistance is not in the finest airways but in the medium-sized bronchi (about generations 4–8). Each bronchiole is narrow, but they are so numerous and in parallel that their total resistance is small, less than 20% of the total. This makes early lesions of the small airways hard to detect in routine measurements.

Factors affecting airway resistance:

- Lung volume: the airways are pulled outward by the surrounding lung tissue (radial traction), so the larger the lung volume, the wider the airways and the smaller the resistance.
- Smooth muscle tone: the vagus nerve and inflammatory mediators constrict the bronchi, and $\beta_2$-receptor agonists dilate them, the latter being the basis of asthma treatment.
- Dynamic compression: in forced expiration intrapleural pressure becomes positive and compresses the intrathoracic airways; downstream of the "equal pressure point", where the pressure within the airway has fallen to equal the intrapleural pressure, the airway is narrowed and flow no longer increases with effort. Maximal expiratory flow is therefore determined mainly by the elastic recoil of the lung and the properties of the airways and is independent of effort; in emphysema the recoil is insufficient and the airways lose traction, the equal pressure point moves toward the alveolar side, and the airways collapse earlier.

### 17.4.6. The Work of Breathing

The work done by the respiratory muscles in one breath equals the integral of pressure over volume:

$$
W = \int P\,\mathrm{d}V,
$$

where $P$ is the pressure needed to drive gas into the lung (the sum of the pressures to overcome elastic and non-elastic resistance). On the pressure–volume diagram, the work against elastic resistance in inspiration is the area of the triangle under the compliance curve, about $V_{\mathrm{T}}^2/(2C)$; the work against airway resistance depends on flow rate. In quiet breathing the oxygen consumption of the respiratory muscles is only about 1%–3% of the total, and can rise above 10% in strenuous exercise; in obstructive or restrictive lung disease it can be as high as 30%, and breathing itself becomes a limiting factor for exercise.

**Example 17.4.1 (Why there is a most economical breathing frequency)** Let the required alveolar ventilation $\dot V_{\mathrm{A}} = f(V_{\mathrm{T}} - V_{\mathrm{D}})$ be fixed. At a low frequency $f$ and large tidal volume, the work against elastic resistance ($\propto f V_{\mathrm{T}}^2$) is large; at a high frequency and small tidal volume, the total ventilation $f V_{\mathrm{T}}$ must increase to compensate for the dead space and the flow is faster, so the work against airway resistance increases. The sum of the two is smallest at some intermediate frequency (Otis and colleagues, 1950). For normal people this frequency is about 10–15 breaths per minute, close to the actual resting respiratory frequency. In patients with low compliance (such as pulmonary fibrosis) the most economical frequency is higher, appearing as rapid shallow breathing; in patients with high airway resistance (such as asthma) it is lower, appearing as deep slow breathing.

## 17.5. Lung Volumes and Pulmonary Ventilation

### 17.5.1. Lung Volumes and Capacities

Recording changes in lung volume during breathing with a spirometer allows the gas in the lung to be divided into four non-overlapping "volumes"; combinations of two or more volumes are called "capacities".

**Definition 17.5.1 (Lung Volumes)** The amount of gas inspired or expired in each quiet breath is called the **tidal volume** ($V_{\mathrm{T}}$); the amount that can still be inspired with effort after a quiet inspiration is called the inspiratory reserve volume; the amount that can still be expired with effort after a quiet expiration is called the expiratory reserve volume; the amount of gas remaining in the lung after a maximal expiration, which cannot be expelled, is called the **residual volume**. The sum of the four is the **total lung capacity**.

**Definition 17.5.2 (Lung Capacities)** The sum of tidal volume and inspiratory reserve volume is called the inspiratory capacity; the sum of expiratory reserve volume and residual volume, i.e., the amount of gas left in the lung at the end of quiet expiration, is called the **functional residual capacity** (FRC); the sum of tidal volume, inspiratory reserve volume and expiratory reserve volume, i.e., the maximal amount that can be expired after a maximal inspiration, is called the **vital capacity** (VC).

| Name | Composition | Typical value for an adult male |
|---|---|---|
| Tidal volume | — | $500\,\mathrm{mL}$ |
| Inspiratory reserve volume | — | $3000\,\mathrm{mL}$ |
| Expiratory reserve volume | — | $1100\,\mathrm{mL}$ |
| Residual volume | — | $1200\,\mathrm{mL}$ |
| Inspiratory capacity | Tidal volume + inspiratory reserve volume | $3500\,\mathrm{mL}$ |
| Functional residual capacity | Expiratory reserve volume + residual volume | $2300\,\mathrm{mL}$ |
| Vital capacity | Tidal volume + inspiratory reserve volume + expiratory reserve volume | $4600\,\mathrm{mL}$ |
| Total lung capacity | Vital capacity + residual volume | $5800\,\mathrm{mL}$ |

Values for women are about 20%–25% smaller. These quantities vary considerably among individuals with height, age and fitness, so clinically they are judged as a percentage of the predicted value.

![Lung volumes and capacities (typical values for an adult male, in mL). The left section is quiet breathing (tidal volume 500 mL, 12 breaths per minute); in the middle a maximal inspiration is followed by a maximal expiration, and then quiet breathing resumes. Arrows on the right mark the four capacities composed of the volumes: inspiratory capacity IC, functional residual capacity FRC, vital capacity VC and total lung capacity TLC. The residual volume never leaves the lung and cannot be measured by spirometry, so every quantity that includes the residual volume (FRC, TLC) must be measured by gas dilution (helium dilution, nitrogen washout) or plethysmography.](./plots/spirogram.py)

The physiological significance of the functional residual capacity is buffering: it keeps the composition of alveolar gas from fluctuating widely with each breath (Section 17.6.1). The functional residual capacity is determined by the balance between the recoil of the lung and the outward elastic force of the thorax: in emphysema recoil falls and FRC increases; in pulmonary fibrosis it decreases.

Vital capacity reflects the maximal capacity of a single ventilation but not its speed: patients with airway obstruction can still expel a normal vital capacity if the expiration time is unlimited. Clinically one therefore measures the forced vital capacity (FVC, the maximal amount expired as hard and fast as possible after a maximal inspiration, slightly smaller than the vital capacity) and the forced expiratory volume in the first second (FEV₁).

**Definition 17.5.3 (Forced Expiratory Volume)** The amount of gas that can be expired within a given time in forced expiration as hard and fast as possible after a maximal inspiration is called the **forced expiratory volume**, usually expressed as the volume in the first second (FEV₁) and its percentage of the forced vital capacity (FEV₁/FVC). In normal people FEV₁/FVC is about 80%.

| Type | Examples | FVC | FEV₁ | FEV₁/FVC |
|---|---|---|---|---|
| Obstructive | Asthma, chronic obstructive pulmonary disease | Normal or reduced | Markedly reduced | Reduced (< 70%) |
| Restrictive | Pulmonary fibrosis, chest wall deformity, neuromuscular disease | Reduced | Reduced proportionally | Normal or raised |

### 17.5.2. Pulmonary Ventilation, Dead Space and Alveolar Ventilation

Pulmonary ventilation (minute ventilation) is the amount of gas inspired or expired per minute, $\dot V_{\mathrm{E}} = f V_{\mathrm{T}}$. At rest it is $12 \times 500 = 6\,\mathrm{L\,min^{-1}}$; in maximal deep, rapid breathing it can reach $150$–$200\,\mathrm{L\,min^{-1}}$ (maximal voluntary ventilation), about 25 times the resting value, showing the large reserve of ventilation.

**Definition 17.5.4 (Dead Space and Alveolar Ventilation)** The volume of each inspired breath that remains in the conducting airways and takes no part in gas exchange is called the **anatomical dead space**, about $150\,\mathrm{mL}$ in adults (roughly equal in milliliters to body weight in pounds). The volume of gas that enters alveoli but is not exchanged because there is no or inadequate blood flow is called alveolar dead space. The sum of the two is called the **physiological dead space** $V_{\mathrm{D}}$. The amount of fresh air entering the alveoli per minute that can exchange with blood is called the **alveolar ventilation**:

$$
\dot V_{\mathrm{A}} = f\,(V_{\mathrm{T}} - V_{\mathrm{D}}).
\tag{17.5}
$$

In healthy people alveolar dead space is close to 0, and physiological dead space equals anatomical dead space. At rest $\dot V_{\mathrm{A}} = 12 \times (500 - 150) = 4.2\,\mathrm{L\,min^{-1}}$.

The dead space is fixed, so depth of breathing is more effective than frequency:

| Mode of breathing | Frequency $f$ / min⁻¹ | Tidal volume / mL | Pulmonary ventilation / (L min⁻¹) | Alveolar ventilation / (L min⁻¹) |
|---|---|---|---|---|
| Quiet breathing | 12 | 500 | 6.0 | 4.2 |
| Rapid shallow breathing | 24 | 250 | 6.0 | 2.4 |
| Deep slow breathing | 6 | 1000 | 6.0 | 5.1 |

Physiological dead space can be measured with the Bohr equation: the $\ce{CO2}$ in expired gas comes entirely from the alveoli, and gas in the dead space contains no $\ce{CO2}$, so the $P_{\ce{CO2}}$ of mixed expired gas is diluted:

$$
\frac{V_{\mathrm{D}}}{V_{\mathrm{T}}} = \frac{P_{\mathrm{aCO_2}} - P_{\mathrm{ECO_2}}}{P_{\mathrm{aCO_2}}},
\tag{17.6}
$$

with arterial $P_{\ce{CO2}}$ substituted for alveolar $P_{\ce{CO2}}$ (Enghoff's modification). Normally $V_{\mathrm{D}}/V_{\mathrm{T}} \approx 0.3$; pulmonary embolism deprives some alveoli of blood flow, alveolar dead space increases, and $V_{\mathrm{D}}/V_{\mathrm{T}}$ rises.

The trachea of the giraffe is long and narrow, and its dead space is far larger in absolute terms than that of humans, but its tidal volume also increases in proportion and its respiratory frequency is lower, so $V_{\mathrm{D}}/V_{\mathrm{T}}$ is similar to that of other mammals. In mammals both tidal volume and dead space are about fixed proportions of body weight (about $6$–$7$ and $2\,\mathrm{mL\,kg^{-1}}$ respectively).

## 17.6. Alveolar Gas

### 17.6.1. Renewal of Alveolar Gas

At the end of quiet expiration the lung contains a functional residual capacity of about $2300\,\mathrm{mL}$ of gas. Of a $500\,\mathrm{mL}$ inspiration, what first enters the alveoli is the $150\,\mathrm{mL}$ of old alveolar gas left in the dead space by the previous expiration, and only then the $350\,\mathrm{mL}$ of fresh air. Each breath therefore renews only about

$$
\frac{350}{2300} \approx \frac{1}{7}
$$
of the alveolar gas.

Alveolar gas can be regarded as a mixing pool of volume FRC flushed at $\dot V_{\mathrm{A}}$; a change in the concentration of any gas approaches its new steady state exponentially with time constant $\tau = \mathrm{FRC}/\dot V_{\mathrm{A}} \approx 2.3/4.2\,\mathrm{min} \approx 33\,\mathrm{s}$; when ventilation doubles, $\tau$ halves. The significance of this slow renewal is stability: the $P_{\ce{O2}}$ and $P_{\ce{CO2}}$ of alveolar gas and arterial blood do not rise and fall sharply with each inspiration and expiration, nor change abruptly in a brief breath-hold.

### 17.6.2. The Alveolar Gas Equation

The composition of alveolar gas is determined by the balance of two processes: ventilation brings in $\ce{O2}$ and removes $\ce{CO2}$, while blood removes $\ce{O2}$ and brings in $\ce{CO2}$. For $\ce{CO2}$, which is almost absent from inspired gas, the steady-state rate of elimination equals alveolar ventilation times the fraction of $\ce{CO2}$ in alveolar gas:

$$
P_{\mathrm{ACO_2}} = \frac{\dot V_{\ce{CO2}}}{\dot V_{\mathrm{A}}} \times 863\,\mathrm{mmHg},
\tag{17.7}
$$

where $\dot V_{\ce{CO2}}$ is expressed at standard conditions (STPD) and $\dot V_{\mathrm{A}}$ at body temperature and saturated with water vapor (BTPS); the constant $863 = 760 \times 310/273$ comes from converting between the two states. This is one of the most important relations in respiratory physiology: at a given metabolic rate the $P_{\ce{CO2}}$ of the alveoli (and of arterial blood) is inversely proportional to alveolar ventilation. If ventilation doubles, $P_{\ce{CO2}}$ is halved.

**Definition 17.6.1 (Respiratory Exchange Ratio)** The ratio of the rate of $\ce{CO2}$ output to the rate of $\ce{O2}$ uptake, $R = \dot V_{\ce{CO2}}/\dot V_{\ce{O2}}$, is called the **respiratory exchange ratio**. In the steady state it equals the respiratory quotient of tissue metabolism (Chapter 30): $R = 1.0$ for complete oxidation of carbohydrate, about 0.7 for fat, about 0.8 for protein, and about 0.8 for a usual mixed diet.

**Formula 17.6.1 (Alveolar Gas Equation)** In the steady state, with $\ce{CO2}$-free inspired gas, the alveolar $P_{\ce{O2}}$ is

$$
P_{\mathrm{AO_2}} = P_{\mathrm{IO_2}} - P_{\mathrm{ACO_2}}\left[F_{\mathrm{IO_2}} + \frac{1 - F_{\mathrm{IO_2}}}{R}\right] \approx P_{\mathrm{IO_2}} - \frac{P_{\mathrm{ACO_2}}}{R},
\tag{17.8}
$$

where $F_{\mathrm{IO_2}}$ is the fraction of $\ce{O2}$ in inspired gas (0.21 for air), and the correction term in brackets arises because the volumes of inspired and expired gas differ when $R < 1$.

Substituting $P_{\mathrm{IO_2}} = 149\,\mathrm{mmHg}$, $P_{\mathrm{ACO_2}} = 40\,\mathrm{mmHg}$ and $R = 0.8$ gives $P_{\mathrm{AO_2}} \approx 149 - 40 \times 1.2 \approx 100\,\mathrm{mmHg}$ ($13.3\,\mathrm{kPa}$); the $104\,\mathrm{mmHg}$ often used in textbooks comes from slightly different values. Uses of the alveolar gas equation:

- Identifying the cause of hypoxemia: in hypoventilation $P_{\mathrm{ACO_2}}$ rises and $P_{\mathrm{AO_2}}$ falls correspondingly according to Eq. (17.8), and the alveolar–arterial $P_{\ce{O2}}$ difference ($A$–$a$ difference, normally 5–15 mmHg) is unchanged; whereas diffusion impairment, mismatch of the **ventilation–perfusion ratio** or shunt increase the $A$–$a$ difference (Chapters 18 and 19).
- Calculating the effect of oxygen administration and of altitude: breathing 30% $\ce{O2}$ raises $P_{\mathrm{IO_2}}$ to $214\,\mathrm{mmHg}$ and $P_{\mathrm{AO_2}}$ by about $65\,\mathrm{mmHg}$.
- Showing that hyperventilation has a limited effect: as ventilation increases to infinity, $P_{\mathrm{ACO_2}} \to 0$, and $P_{\mathrm{AO_2}}$ can rise at most to $P_{\mathrm{IO_2}}$.

![Alveolar $P_{\ce{O2}}$ (A) and $P_{\ce{CO2}}$ (B) as functions of alveolar ventilation (Eq. (17.7) and Formula 17.6.1, sea level, $R = 0.8$). Solid lines are at rest (oxygen uptake 250 mL/min, $\ce{CO2}$ output 200 mL/min), dashed lines are moderate exercise (oxygen uptake 1000 mL/min). Dots are the normal resting operating point (alveolar ventilation 4.2 L/min: $P_{\mathrm{AO_2}} \approx 100$ mmHg, $P_{\mathrm{ACO_2}} \approx 40$ mmHg) and the ventilation needed in exercise to keep the same alveolar gas (4 times, 16.8 L/min). $P_{\mathrm{ACO_2}}$ is a hyperbola: it rises steeply in hypoventilation; $P_{\mathrm{AO_2}}$ approaches the inspired value of 149 mmHg (dotted line) only slowly as ventilation increases. The right axis is in kPa.](./plots/alveolar-gas.py)

In exercise, as long as ventilation increases in proportion to metabolic rate, the composition of alveolar gas stays constant; in fact in moderate exercise $P_{\mathrm{ACO_2}}$ stays almost at 40 mmHg, a result of this matching (Chapter 20, Section 20.6).

Composition of gas at the various stages (sea level, in mmHg):

| Gas | Atmosphere | Humidified inspired gas | Alveolar gas | Mixed expired gas |
|---|---|---|---|---|
| $\ce{N2}$ | 597 | 563 | 569 | 566 |
| $\ce{O2}$ | 159 | 149 | 100–104 | 120 |
| $\ce{CO2}$ | 0.3 | 0.3 | 40 | 27 |
| $\ce{H2O}$ | 3.7 (depending on humidity) | 47 | 47 | 47 |

Expired gas is a mixture of alveolar gas and fresh air from the dead space, so its $P_{\ce{O2}}$ is higher and its $P_{\ce{CO2}}$ lower than those of alveolar gas; only the last portion of expiration (end-tidal gas) approaches alveolar gas, and clinically end-tidal $P_{\ce{CO2}}$ is used to monitor ventilation.

## 17.7. Evolution and Comparison

### 17.7.1. Diversity of Respiratory Organs

Respiratory organs of animals can be classified by medium and position of the exchange surface:

| Organ | Structural features | Medium | Examples |
|---|---|---|---|
| Body surface | The whole body surface; often with well-developed subcutaneous capillaries | Water or moist air | Flatworms, earthworms, frogs (skin accounts for most of their $\ce{CO2}$ output), plethodontid salamanders |
| Gills | Outward projections of the body surface, richly vascularized, supported by the buoyancy of water | Water | Mollusks, crustaceans, fishes, amphibian larvae |
| Lungs | Inward sacs of the body wall, avoiding water loss | Air | Pulmonate snails, spider book lungs, tetrapods; lungfishes |
| Tracheae | An inward branching tube system of the body wall that carries air directly to the cells | Air | Insects, myriapods, some arachnids |

Gills are evaginated and lungs and tracheae are invaginated, which is related to the medium: in water, gill lamellae are supported by the buoyancy of water and kept moist; in air, thin evaginated structures would collapse and lose water, so the exchange surface must be withdrawn into the body and air delivered to it by a ventilation pump (Chapter 18, Section 18.7). The lungs of vertebrates and the swim bladder of teleosts are homologous, both formed as outpocketings of the ventral or dorsal foregut; the earliest bony fishes already had lungs, and the swim bladder is a buoyancy organ derived from the lung in ray-finned fishes.

### 17.7.2. Fishes: Countercurrent Gills and Ram Ventilation

Teleosts have four gill arches on each side, each with two rows of filaments, and the upper and lower surfaces of the filaments are densely covered with flat secondary lamellae, on which gas exchange takes place. Water flows between the lamellae in the direction opposite to that of blood flow in the lamellae, constituting countercurrent exchange (Section 17.3.3). Ventilation is driven alternately by two pumps: the buccal pump (the mouth cavity enlarges to draw in water, then closes and pressurizes) and the opercular pump (enlargement of the opercular cavity creates negative pressure), so that water flows almost continuously and unidirectionally over the gills.

Fast-swimming fishes (tunas, mackerels, many sharks) stop pumping water actively while swimming and open the mouth to let the forward speed force water over the gills, called *ram ventilation*. The cost of ram ventilation is absorbed into swimming; tunas and some species of the mackerel family depend on it entirely and must swim continuously, and suffocate if they stop. Sharks vary: pelagic mako and requiem sharks depend on ram ventilation, whereas many benthic sharks and rays ventilate actively with spiracles and the buccal pump and can rest motionless on the bottom.

### 17.7.3. Amphibians and Reptiles: From Buccal Pump to Aspiration Pump

Amphibians have no intercostal muscles or diaphragm and "force" air into the lungs with a *buccal pump*: the floor of the mouth is lowered and air enters the buccopharyngeal cavity through the nostrils; the nostrils close and the floor of the mouth rises, pushing the air into the lungs under positive pressure; the elastic recoil of the lungs and the body-wall muscles expel the gas. This is a positive-pressure mode of ventilation, the opposite of the negative-pressure aspiration of mammals. The skin of the frog is the main route of $\ce{CO2}$ elimination (about 3/4), and the lungs are mainly responsible for $\ce{O2}$ uptake; tadpoles first breathe with gills and skin and switch to lungs and skin at **metamorphosis** ([7.5.33](/7.5.33)).

In amniotes the skin is keratinized and can no longer exchange gases, and they have changed to an aspiration pump in which trunk muscles create negative pressure in the thoracic cavity: lizards and snakes enlarge the thorax with the intercostal muscles (costal aspiration); in turtles the ribs are fused with the carapace, and muscles around the limbs and the shoulder and pelvic girdles change the volume of the body cavity; crocodilians have a "hepatic piston" made of the liver and diaphragm-like muscle, which pulls the liver backward to enlarge the thorax; mammals developed a muscular diaphragm. The intercostal muscles of lizards serve both breathing and locomotion; in fast running the trunk bends from side to side and the two lungs are compressed alternately, so that they cannot breathe at the same time (Carrier's "axial constraint"), which is thought to limit their sustained locomotor capacity; monitor lizards use a buccal pump to assist inspiration and partly overcome this constraint.

### 17.7.4. Birds: Air Sacs and Parabronchi

The avian lung is a rigid structure of almost constant volume, and ventilation is accomplished by the 9 (in most species) thin-walled air sacs connected to it. The air sacs themselves have almost no gas exchange and serve only as bellows; gas exchange takes place in the many parallel parabronchi within the lung.

**Definition 17.7.1 (Parabronchus)** The fine tubes in the avian lung that are arranged in parallel and connected at their two ends to the dorsobronchi and ventrobronchi are called **parabronchi**. Their walls project many anastomosing air capillaries ($3$–$10\,\mathrm{\mu m}$ in diameter) that interlace with blood capillaries, and gas exchange takes place here; gas flows unidirectionally along the parabronchus, and blood flows from the periphery of the parabronchus toward its lumen, perpendicular to the direction of airflow.

During one inspiration and one expiration, gas flows through the lung in a fixed direction: in inspiration, most of the fresh air passes through the main bronchus into the posterior air sacs, while the gas left in the lung by the previous breath enters the anterior air sacs; in expiration, fresh air in the posterior air sacs is driven into the parabronchi and the gas in the anterior air sacs is expelled through the trachea. Fresh air therefore flows unidirectionally (from posterior to anterior) through the parabronchi in both inspiration and expiration. This unidirectional flow does not depend on valves but on aerodynamic "valves" at the branch points of the bronchi, and has been observed in the lungs of birds, crocodilians and monitor lizards (Farmer, 2010s), suggesting that unidirectional flow may have originated in the common ancestor of archosaurs or even earlier.

Gas exchange in the avian lung is crosscurrent (Section 17.3.3), with an efficiency higher than that of the mammalian alveolus; the **blood–gas barrier** of birds is also thinner (Chapter 18, Section 18.7). These features allow birds to fly at high altitude: the bar-headed goose crosses the Himalayas every year, and satellite tracking has recorded sustained flapping flight at altitudes of $5000$–$6000\,\mathrm{m}$ (up to about $7300\,\mathrm{m}$), whereas a human at the same altitude can barely function.

### 17.7.5. Insects: The Tracheal System

**Definition 17.7.2 (Tracheal System)** Paired **spiracles** on the insect body surface open into a branching network of tubes within the body; the tube walls are lined with cuticle and have spiral thickenings (taenidia) to prevent collapse, and the ends become tracheoles less than $1\,\mathrm{\mu m}$ in diameter that reach into or lie against every cell; air is delivered to the tissue in the gas phase along this network. Such a respiratory system is called a **tracheal system**.

The tracheal system makes insect gas exchange independent of the circulatory system: their hemolymph (**open circulatory system**, Chapter 12) carries almost no $\ce{O2}$. $\ce{O2}$ diffuses in air about ten thousand times faster than in water, so in small insects diffusion alone suffices; the ends of the tracheoles are filled with liquid, and when oxygen demand increases, as in flight, the raised osmotic pressure of the tissue draws the liquid away and the gas phase comes closer to the cells. Large or active insects use abdominal pumping movements, compression of the thorax by the flight muscles and collapsible air sacs to produce convective ventilation in the main tracheal trunks.

Many insects show discontinuous gas exchange at rest: the spiracles stay closed for long periods, $\ce{O2}$ is consumed, and $\ce{CO2}$ is stored in the hemolymph as bicarbonate; then the spiracles enter a "flutter" phase of rapid opening and closing in which small amounts of air are drawn in; finally the spiracles open completely and the $\ce{CO2}$ is released in a burst. The significance of this pattern is still debated; the main hypotheses are reducing respiratory water loss, improving gas exchange in underground environments, and limiting exposure of the tissues to excessive $\ce{O2}$ (oxidative damage).

Diffusion limits the body size of insects: the longer the trachea, the greater the diffusion distance, and the fraction of volume occupied by tracheae increases with body size and finally crowds out other tissues (studies of beetles show that the fraction occupied by tracheae in the legs increases disproportionately in large species). From the late Carboniferous to the early Permian (about 300 million years ago), atmospheric $\ce{O2}$ reached about 30% (21% today; [7.10.29](/7.10.29)), and griffinflies (*Meganeura*) with a wingspan of about $70\,\mathrm{cm}$ and the arthropod *Arthropleura* more than $2\,\mathrm{m}$ long appeared. "Hyperoxia made giant insects possible" is a strong but still debated hypothesis: fruit flies and dragonflies reared in high $\ce{O2}$ grow larger after several generations and smaller in low $\ce{O2}$, which is consistent with it; but giant insects persisted for a time after $\ce{O2}$ fell, and the appearance of flying predators such as birds and pterosaurs may also have limited insect size.

## Summary

| Topic | Core content |
|---|---|
| Steps of respiration | Ventilation (bulk flow) → pulmonary gas exchange (diffusion) → transport in blood (bulk flow) → tissue gas exchange (diffusion) (Definition 17.1.1) |
| Partial pressure | $P_{\ce{O2}}$: dry air 159, humidified inspired gas 149, alveolar gas about 100 mmHg; water vapor 47 mmHg depends only on body temperature |
| Diffusion | Formula 17.2.1: $\dot V = (A/\Delta x)\,D\alpha\,\Delta P$; $K$ of $\ce{CO2}$ is about 20 times that of $\ce{O2}$ |
| Medium | Water has 30–56 times less $\ce{O2}$, diffusion $10^4$ times slower, 800 times heavier: fish respiration costs about 10%, human 1%–2% |
| Size limit | Formula 17.2.2: $R_{\max} = \sqrt{6Dc_0/M} \approx 1\,\mathrm{mm}$ |
| Exchange design | Formula 17.3.1: countercurrent (gill) > crosscurrent (bird lung) > ventilated pool (alveolus) ≈ concurrent; only countercurrent can give $E \to 1$ |
| Pleural cavity | Definition 17.4.1: $P_{\mathrm{L}} = P_{\mathrm{alv}} - P_{\mathrm{pl}}$; $P_{\mathrm{pl}}$ is about $-5$ to $-7.5\,\mathrm{cmH_2O}$ in quiet breathing |
| Elastic resistance | Definition 17.4.2: $C_{\mathrm{L}} \approx 200\,\mathrm{mL/cmH_2O}$; recoil is 1/3 from tissue, 2/3 from surface tension |
| Airway resistance | Mainly in medium-sized bronchi; lung volume, smooth muscle tone, dynamic compression |
| Lung volumes | Definitions 17.5.1, 17.5.2: TV 500, IRV 3000, ERV 1100, RV 1200; FRC 2300, VC 4600, TLC 5800 mL; FEV₁/FVC distinguishes obstructive from restrictive disease (Definition 17.5.3) |
| Ventilation | Eq. (17.5): $\dot V_{\mathrm{A}} = f(V_{\mathrm{T}} - V_{\mathrm{D}})$, 4.2 L/min at rest; deep slow breathing is more effective |
| Alveolar gas | About 1/7 renewed per breath; Eq. (17.7): $P_{\mathrm{ACO_2}} \propto \dot V_{\ce{CO2}}/\dot V_{\mathrm{A}}$; Formula 17.6.1: $P_{\mathrm{AO_2}} \approx P_{\mathrm{IO_2}} - P_{\mathrm{ACO_2}}/R$ |
| Evolution | Gills evaginated (buoyancy of water), lungs and tracheae invaginated (against water loss and collapse); ram ventilation; positive-pressure ventilation by the buccal pump; avian air sacs and parabronchi (Definition 17.7.1) with unidirectional crosscurrent flow; the insect tracheal system (Definition 17.7.2) independent of the circulation |

## Questions

1. Why is the $P_{\ce{CO2}}$ difference between venous blood and alveolar gas (about 6 mmHg) only 1/10 of the $P_{\ce{O2}}$ difference (about 60 mmHg), while the amounts of the two gases exchanged are similar (200 and 250 mL/min)?

   **Answer** By Formula 17.2.1 the diffusion rate is proportional to $K\Delta P$. The solubility of $\ce{CO2}$ is about 24 times that of $\ce{O2}$ and its diffusion coefficient about 0.85 times, so $K_{\ce{CO2}} \approx 20K_{\ce{O2}}$. Across the same barrier, a $\ce{CO2}$ partial pressure difference of 6 mmHg is equivalent to an $\ce{O2}$ partial pressure difference of 120 mmHg, enough to eliminate an amount of $\ce{CO2}$ similar to the amount of $\ce{O2}$ taken up. In addition, actual exchange is also affected by chemical reactions in the blood and by binding curves (Chapter 19).

2. One person breathes at 30 breaths/min with a tidal volume of 200 mL, and another at 10 breaths/min with a tidal volume of 600 mL. The dead space is 150 mL in both. Compare the pulmonary ventilation and alveolar ventilation of the two, and estimate their alveolar $P_{\ce{CO2}}$ ($\dot V_{\ce{CO2}} = 200\,\mathrm{mL\,min^{-1}}$).

   **Answer** Pulmonary ventilation is 6 L/min in both. Alveolar ventilation: $30 \times 50 = 1.5\,\mathrm{L\,min^{-1}}$ for the first and $10 \times 450 = 4.5\,\mathrm{L\,min^{-1}}$ for the second. By Eq. (17.7), $P_{\mathrm{ACO_2}} = 863 \times 0.2/\dot V_{\mathrm{A}}$: about 115 mmHg for the first (severe hypercapnia, with severe hypoxia) and about 38 mmHg for the second (normal). Most of the ventilation of rapid shallow breathing is wasted in the dead space.

3. Use Eq. (17.4) to explain why reversing the direction of water flow over the gills of a fish greatly reduces its $\ce{O2}$ extraction. If the diffusive conductance of the gill were infinite, what is the highest partial pressure blood could reach in concurrent flow?

   **Answer** Reversal makes the exchange concurrent. In concurrent flow the two fluids approach a common intermediate partial pressure along the exchanger and no further exchange occurs; as $D^* \to \infty$, $E \to 1/(1+r)$, which for $r = 1$ is only 0.5, i.e., blood can reach at most the midpoint between the partial pressures of the inflowing water and of venous blood. In countercurrent flow the two fluids keep a partial pressure difference along the whole length, and for $r \le 1$, $E \to 1$, so the blood can approach the partial pressure of the inflowing water. Real gills have a finite $D^*$, but the advantage of countercurrent flow is still large, and in experiments reversing the water flow reduces extraction from about 50%–80% to about 10%.

4. The atmospheric pressure at the summit of Mount Everest is about 253 mmHg. If a climber lowers $P_{\mathrm{ACO_2}}$ by hyperventilation to 7.5 mmHg (the measured value) and $R = 0.85$, estimate his $P_{\mathrm{AO_2}}$; what is the result if he does not hyperventilate and $P_{\mathrm{ACO_2}}$ stays at 40 mmHg?

   **Answer** $P_{\mathrm{IO_2}} = 0.2093 \times (253 - 47) \approx 43\,\mathrm{mmHg}$. From the simplified form of Formula 17.6.1, $P_{\mathrm{AO_2}} \approx 43 - 7.5/0.85 \approx 34\,\mathrm{mmHg}$ (about 35 mmHg from the exact form, in agreement with the measured value of about 35 mmHg of the 1981 American Medical Research Expedition to Everest). If $P_{\mathrm{ACO_2}} = 40\,\mathrm{mmHg}$, $P_{\mathrm{AO_2}} \approx 43 - 47 < 0$, and life cannot be sustained. Extreme hyperventilation is a necessary condition for survival at the summit, at the price of severe **respiratory alkalosis** (Chapter 20, Section 20.6.3, and Chapter 25).

5. Use Formula 17.2.2 to explain why most multicellular animals without a circulatory system that rely on diffusion for oxygen are flat or slender, or have internal channels flushed by water.

   **Answer** For a sphere, $R_{\max} = \sqrt{6Dc_0/M}$, about 1 mm at typical metabolic rates, a tiny volume. A slab is limited only in half-thickness $L_{\max} = \sqrt{2Dc_0/M}$ (about 0.6 mm), and its length and width are unlimited, so flatworms can grow to several centimeters or longer; a slender cylinder is limited only in radius. The other route is to bring water from the environment into the body (the channel system of sponges, the gastrovascular cavity of cnidarians), so that no cell is far from oxygen-rich water. The lower the metabolic rate, the larger the permitted size ($\propto M^{-1/2}$), so animals such as jellyfish, which are rich in water and have an extremely low metabolic rate per unit volume, can grow very large.

6. Why does the lung collapse when the pleural cavity is punctured while the thorax expands outward? Why might the function of the other lung also be affected in a patient with pneumothorax on one side?

   **Answer** Normally the recoil of the lung and the outward spring of the thorax balance each other through the liquid film of the pleural cavity, and intrapleural pressure is negative. After air enters, the two are no longer linked and each returns to its natural volume: the lung recoils to a very small size, and the thorax expands to a volume greater than at the functional residual capacity. In open pneumothorax on one side, negative intrathoracic pressure draws air in through the wound during inspiration, and the mediastinum is pushed toward the healthy side; in tension pneumothorax (the wound forms a one-way valve) the pressure in the affected hemithorax keeps rising, and the shifted mediastinum compresses the healthy lung and kinks the great veins, reducing **venous return**, which is life-threatening and requires emergency decompression.
