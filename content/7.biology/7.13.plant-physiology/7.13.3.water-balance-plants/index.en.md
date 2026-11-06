---
title: Water Balance of Plants
description: Soil water types and soil water potential, field capacity and the permanent wilting percentage; sites, pathways and driving forces of water uptake by roots, root pressure, bleeding and guttation; Hagen–Poiseuille flow in the xylem, the pressure needed to lift water to the top of a 100-m tree, and the cohesion–tension theory; cavitation, embolism and vulnerability curves; modes, indices and driving forces of transpiration, and stomatal and boundary-layer conductance; transpiration ratio and water-use efficiency; the series-resistance model of the soil–plant–atmosphere continuum; rational irrigation.
source_hash: 2e574676f6dc
---

Terrestrial plants face an unavoidable dilemma: photosynthesis requires taking up $\ce{CO2}$ from the atmosphere, but the passages through which $\ce{CO2}$ enters the leaf also let water vapor escape, and the water vapor concentration difference that drives water loss is much larger than the concentration difference that drives $\ce{CO2}$ uptake. The plant's solution is a physical system that consumes almost no metabolic energy and continually replenishes from the soil the water lost in transpiration: water in the soil is absorbed by roots, rises through the xylem by bulk flow for several meters to over a hundred meters, evaporates from the surfaces of mesophyll cell walls, and diffuses out through the stomata as vapor. The energy that drives all of this ultimately comes from the sun.

This chapter follows the path of water: water in the soil (3.1), water uptake by roots (3.2), transport in the xylem and the cohesion–tension theory (3.3), transpiration (3.4), and finally connects the segments into the **soil–plant–atmosphere continuum** and quantifies it with a series-resistance model (3.5), and discusses the physiological basis of rational irrigation (3.6). The water potential concept at the cellular scale was presented in the previous chapter, [7.13.2](/7.13.2); the anatomy of roots, stems and leaves, including the endodermis and **Casparian strip** and the structure and evolution of vessels and tracheids, was covered in botany ([7.12.20](/7.12.20), [7.12.5](/7.12.5), [7.12.23](/7.12.23)), and only their physiological function and quantitative relations are given here; the mechanism of stomatal movement is discussed separately in [7.13.10](/7.13.10).

## 3.1. Water in the Soil

### 3.1.1. Types of Soil Water

Soil is a mixture of three phases: the solid phase is mineral particles and organic matter, the liquid phase is the soil solution containing dissolved minerals, and the gas phase is the air in the pores. The water content of soil and the rate at which water moves in it depend mainly on soil texture and structure. Sand particles can exceed 1 mm in diameter, have a small specific surface area and large channels between particles; clay particles are smaller than $2\,\mu\mathrm{m}$, with a large specific surface area and fine channels; humus can aggregate clay particles into crumbs, forming larger channels and improving aeration and drainage.

After heavy rain or irrigation, water percolates under gravity along the pores between particles, partly draining or trapping the air in the pores; because of capillary action the finer channels fill with water first. According to how water is held by the soil, soil water can be divided into three types:

| Type | How it is held | Available to plants? |
|---|---|---|
| Bound water (hygroscopic water) | Very thin films strongly adsorbed on soil particle surfaces; the water remaining in air-dried soil | Water potential extremely low; unavailable |
| Capillary water | Held by capillary action in the pores between soil particles | The main source of water for plants |
| Gravitational water | Water in excess of what capillary action can hold, percolating down through large pores | Drains quickly, available only briefly; prolonged retention makes the soil anoxic |

### 3.1.2. Soil Water Potential

Soil water potential can likewise be decomposed into solute, pressure (matric) and gravitational potentials. Except in saline soils the soil solution is very dilute, and the solute potential is generally only about $-0.02\,\mathrm{MPa}$ and can be neglected; in saline soils it can reach $-0.2\,\mathrm{MPa}$ or lower. The pressure potential of moist soil is close to zero; as the soil dries, water retreats into ever finer pores between soil particles, forming curved air–water interfaces (menisci), and the water beneath the interface is under negative pressure:

$$
\Psi_{\mathrm{p}} = -\frac{2T}{r}, \tag{3.1}
$$

where $T = 0.0728\,\mathrm{N\,m^{-1}} = 7.28\times10^{-8}\,\mathrm{MPa\,m}$ is the **surface tension** of water and $r$ is the radius of curvature of the meniscus (the contact angle has been taken as zero in the equation). For $r = 1\,\mu\mathrm{m}$ (about the size of the largest clay particles), $\Psi_{\mathrm{p}} = -0.15\,\mathrm{MPa}$; once the water has retreated into finer gaps between clay particles, $\Psi_{\mathrm{p}}$ easily reaches $-1$ to $-2\,\mathrm{MPa}$. This negative pressure is the **matric potential** of the soil: the term matric potential commonly used in soil science describes the same thing as Eq. (3.1). Eq. (3.1) will recur throughout this chapter: from soil pores and mesophyll cell walls to the pit membranes of the xylem, the radius of the meniscus determines the tension on the water.

![Negative pressure beneath a curved air–water interface, $-\Psi_{\mathrm{p}} = 2T/r$ (Eq. (3.1), log–log axes; 20 °C, contact angle zero). In a vessel lumen of radius $20\,\mu\mathrm{m}$, the tension produced by capillary action is only $0.007\,\mathrm{MPa}$, sufficient to lift water only $0.74\,\mathrm{m}$; the green horizontal band is the range of soil water potential corresponding to field capacity (about $-0.01$ to $-0.033\,\mathrm{MPa}$), and the dashed line is the permanent wilting point ($-1.5\,\mathrm{MPa}$); a gap of $1\,\mu\mathrm{m}$ between clay particles corresponds to $-0.15\,\mathrm{MPa}$; when the radius of the menisci between microfibrils of mesophyll cell walls shrinks from $0.5\,\mu\mathrm{m}$ to $0.01\,\mu\mathrm{m}$, the tension rises from $0.3\,\mathrm{MPa}$ to $15\,\mathrm{MPa}$, enough to pull water up the tallest trees; the gray region is the size scale of pit membrane pores (about 10–100 nm), which determines the threshold for cavitation caused by air passing through pit membranes (3.3.5)](./plots/capillary.py)

**Definition 3.1.1 (Field Capacity)** The water content of a soil after it has been saturated with water, the gravitational water has drained away, and all the capillary and bound water still remain in the soil is called the **field capacity**. The soil water potential is then about $-0.01$ to $-0.033\,\mathrm{MPa}$ (in soil science $-0.033\,\mathrm{MPa}$ is often used). Field capacity is highest in clay, next in loam and lowest in sand.

Water uptake by plants gradually dries the soil. The drooping of leaves and young stems because of the decline in cell turgor is called *wilting*: if the plant recovers when transpiration is reduced (as at night or in shade), the wilting is called temporary; if it fails to recover even when transpiration is reduced, it is called permanent wilting, and the roots can then no longer obtain enough water from the soil.

**Definition 3.1.2 (Permanent Wilting Percentage)** The percentage of the soil dry weight made up by the water still remaining in the soil when a plant has just undergone permanent wilting is called the **permanent wilting percentage**; the soil water potential at that point is called the *permanent wilting point* and is about $-1.5\,\mathrm{MPa}$.

The difference between field capacity and permanent wilting percentage is the water available to plants. The permanent wilting point is not a universal constant: $-1.5\,\mathrm{MPa}$ is a conventional value measured on mesophytic crops such as sunflower, and drought-tolerant plants can take up water from drier soil; but because the soil water content changes little with water potential around this value, the error in estimating available water with it is small.

| Soil (typical range of volumetric water content) | Field capacity | Permanent wilting percentage | Available water |
|---|---|---|---|
| Sand | 8%–12% | 3%–5% | about 5%–8% |
| Loam | 25%–30% | 10%–14% | about 15% |
| Clay | 35%–45% | 20%–28% | about 15% |

Clay holds the most water but also binds it most tightly, so its permanent wilting percentage is high; loam has the most available water. Conversely, at the same water content, sand holds more available water than clay: sand with 20% water is wet, whereas clay with the same 20% is already close to the wilting point.

### 3.1.3. Movement of Water in the Soil

Water in the soil moves mainly by bulk flow: since the negative pressure of the water arises from menisci, water flows from regions with more water and larger water-filled pores (higher $\Psi_{\mathrm{p}}$) toward regions with less water. After roots take up water, the soil near the root surface dries and its $\Psi_{\mathrm{p}}$ falls, creating a pressure gradient with the wetter surrounding soil, and water flows along connected pores toward the root surface. The flow rate depends on the pressure gradient and on the soil hydraulic conductivity, and their product is Darcy's law $J = -K\,\mathrm{d}\Psi/\mathrm{d}x$. Hydraulic conductivity falls sharply as the soil dries, often by several orders of magnitude: air occupies the formerly water-filled channels, and water can move only along fewer and finer channels and the water films on particle surfaces. When the soil is drying, therefore, it is often not the water potential of the soil but the rate at which water flows toward the root that limits water uptake; in dry soil, diffusion of water vapor also contributes to some extent.

In arid regions, water in the soil layers near the surface continually evaporates, salts remain in the surface layer and are continually replenished by solution from below, resulting in soil salinization; long-term irrigation with saline river water without adequate drainage accelerates this process ([7.13.27](/7.13.27)).

## 3.2. Water Uptake by Roots

### 3.2.1. Sites of Uptake

Water uptake by roots takes place mainly near the root tip, with the root hair zone (maturation zone) having the greatest capacity, the elongation zone next, and the meristematic zone and root cap very little. The root hair zone absorbs most strongly for three reasons: root hairs multiply the absorbing surface (in three-month-old wheat, root hairs account for more than 60% of the root surface area); the cell walls of root hairs are rich in hydrophilic pectin and are in intimate contact with soil particles; and the conducting tissues of the root hair zone have already differentiated and matured, so the resistance to water flow is low.

Older root segments have low uptake capacity because hydrophobic suberin is deposited in the walls of their epidermis and exodermis. This looks unfavorable but is in fact necessary: if the entire root system surface were equally permeable, most of the water would enter through the root segments near the stem base, the tension in the xylem would be dissipated by the inflow of this water, and the distal parts of the root system would not obtain water; lowering the permeability of old root segments allows the xylem tension to extend to the distal parts of the root system and lets the root tips that are exploring new soil take up water.

Contact between root and soil is easily broken by disturbance. Transplanted seedlings need protection from water loss for the first few days until new roots have re-established contact with the soil; transplanting with soil, avoiding damage to young roots and firming the soil around the roots are all intended to protect the sites of uptake and the root–soil contact.

### 3.2.2. Pathways of Uptake

There are three pathways for water from the epidermis to the endodermis (the figure in [7.12.20](/7.12.20) shows their anatomical positions):

- Apoplast pathway: water moves in the **apoplast**, that is, along cell walls, intercellular spaces and the lumina of dead cells, without crossing any membrane;
- Symplast pathway: water moves through connected protoplasts (the **symplast**) via **plasmodesmata**;
- Transmembrane pathway: water enters a cell on one side and leaves on the other, crossing the plasma membrane twice (and possibly the tonoplast) for each cell traversed.

The last two are together called the cell-to-cell pathway. At the endodermis, the **Casparian strip** on the radial and transverse walls is impregnated with hydrophobic lignin and suberin and blocks the apoplast pathway, so water and solutes must cross the plasma membranes of endodermal cells to enter the stele. The endodermis thus becomes in effect a selectively permeable barrier in the root, which also explains why root hydraulic conductivity depends so strongly on **aquaporins**: downregulating the expression of aquaporin genes markedly lowers root hydraulic conductivity.

These three pathways are not three unrelated pipes: a water molecule can travel for a stretch in the symplast, cross the plasma membrane into the apoplast and return to the symplast, water always moving in the direction of least resistance and greatest gradient. Which pathway dominates depends on the nature of the driving force. When transpiration is vigorous, the tension in the xylem creates a hydrostatic pressure gradient, the resistance of the cell wall is small, and the apoplast pathway can carry most of the flow in the cortex; at night, when transpiration stops and only the osmotic driving force remains, water moves mainly by the cell-to-cell pathway. This "composite transport model" (Steudle and Peterson, 1998) explains why root hydraulic conductivity varies with transpiration rate. Frequently stated claims such as "the apoplast pathway accounts for only about 1%" or "the symplast pathway is of no real significance" are too absolute.

The resistance in the root is mainly radial: the resistance to water crossing living cells is far greater than that to longitudinal flow along the xylem. When the soil dries, gaps appear at the root–soil interface and the walls near the endodermis become further suberized, so that the radial resistance of the root increases still more.

Water uptake by roots is reduced under hypoxia or low temperature, which was for a long time hard to explain, in particular why flooded plants wilt. It is now known that hypoxia impairs respiration in root cells and acidifies the cytosol, the plasma membrane aquaporins close because of histidine protonation, and the hydraulic conductivity of the root falls sharply ([7.13.2](/7.13.2)). Maintaining a high membrane hydraulic conductivity requires energy supplied by respiration.

![Radial water uptake by roots (schematic). A: cross section through the maturation zone of a young dicot root (drawn cell by cell; the Casparian strip on the radial walls of the endodermis is red); arrows show the radial path of water from the soil through epidermis, cortex, endodermis and pericycle into the xylem. B: the hydraulic circuit of the same path: resistances of the soil and the root–soil interface; in the cortex the apoplast pathway (cell walls, green) and the cell-to-cell pathway (plasmodesmata and aquaporins in the plasma membrane, blue) are in parallel; at the endodermis the Casparian strip blocks the apoplast pathway, and all water must cross a membrane (yellow); after entering the xylem the longitudinal resistance is very small. During transpiration the tension in the xylem pulls the water (hydrostatic pressure gradient, apoplast pathway important); when transpiration stops, ions loaded into the xylem lower its solute potential, and the root takes up water like an osmometer, generating root pressure](./plots/root-pathways.py)

### 3.2.3. Driving Forces of Uptake: Root Pressure and Transpirational Pull

There are two driving forces for water uptake by roots. Chinese textbooks call water uptake caused by the physiological activity of the root system itself and independent of shoot transpiration "active absorption", and water uptake driven by transpirational pull "passive absorption". It should be noted that "active absorption" does not mean that water is pumped actively: what consumes energy is the active uptake of ions, and water still enters passively down the water potential gradient.

**Definition 3.2.1 (Root Pressure)** The pressure produced by the physiological activity of the root system that makes liquid rise from the root through the xylem is called **root pressure**.

The generation of root pressure: root cells actively take up ions from the soil solution and release them into the xylem vessels of the stele; the Casparian strip prevents these ions from leaking back into the cortex along the apoplast, so the solute potential of the xylem sap falls and its water potential becomes lower than that of the soil solution outside the root; water enters the xylem across the endodermis by osmosis and builds up a positive hydrostatic pressure in the xylem. The multicellular tissue of the whole root system behaves like an osmometer. This gives an upper limit for root pressure: if the solute potential of the xylem sap is $0.1\,\mathrm{MPa}$ lower than that of the soil solution, the root pressure is at most about $0.1\,\mathrm{MPa}$, which can support a water column only about $0.1/0.0098 \approx 10\,\mathrm{m}$ high. Measured root pressures are generally less than $0.1\,\mathrm{MPa}$ and sometimes reach $0.2\,\mathrm{MPa}$ or more. Root pressure appears only when soil water is ample and transpiration is very weak; once transpiration increases, water is carried away quickly and no positive pressure can be built up in the xylem.

The existence of root pressure is demonstrated by bleeding and guttation.

**Definition 3.2.2 (Bleeding)** The exudation of liquid from wounded or broken plant tissue is called **bleeding**, and the exuded sap is called bleeding sap. When soil water is ample and a seedling of an annual plant is cut off near the ground, drops of liquid flow from the cut xylem and can continue for several hours or longer; a manometer attached to the cut surface can measure the root pressure.

When grapevines and birches are pruned in spring, copious bleeding can be seen; the bleeding sap contains mineral ions, amino acids, organic acids and hormones synthesized in the root (such as cytokinins) and is often used to analyze the metabolic activity of roots; the amount and composition of bleeding sap can also serve as an index of the physiological activity of the root system. The sap flow of sugar maple (*Acer saccharum*) in early spring is different: it arises from positive pressure generated in the stem by alternating freezing and thawing and is not root pressure.

**Guttation** is the exudation of drops of liquid from the tips or margins of unwounded leaves, the drops being discharged through **hydathodes** connected to the leaf margins, tips and vein endings. It is most common on warm, humid evenings and mornings, when transpiration is suppressed and root pressure is present; the "dew" at the leaf tips of grasses (such as rice and wheat) in the early morning is in fact mostly guttation fluid. Salts in guttation fluid are deposited at the leaf tip and sometimes cause local injury. Root pressure may be merely an unavoidable by-product of rapid ion uptake; but one of its functions is that the positive pressure in the xylem at night can dissolve gas bubbles and repair embolism caused by cavitation (3.3.5).

The driving force of passive absorption is the *transpiration pull*: water loss by transpiration from the leaf lowers the water potential of mesophyll cells and the xylem, and this lowering is transmitted through the continuous water column all the way to the root, causing the root to take up water from the soil. Under normal transpiration, passive absorption dominates over the life of the plant; root pressure is the main factor only at night or in the early morning when soil water is ample, or in early spring before trees have leafed out (the figure often cited in Chinese textbooks is that root pressure accounts for less than 5% of uptake).

### 3.2.4. Factors Affecting Water Uptake by Roots

| Factor | Effect | Physiological mechanism and examples |
|---|---|---|
| Available soil water | Only capillary and gravitational water can be used | No uptake below the permanent wilting percentage; hydraulic conductivity falls sharply as the soil dries |
| Soil aeration | Hypoxia and high $\ce{CO2}$ reduce uptake | Root respiration is impaired and aquaporins close; with long-term flooding, ethanol accumulating from **alcoholic fermentation** injures root cells |
| Soil temperature | Both low and excessively high temperatures reduce uptake | At low temperature the viscosity of water rises (about 50% higher at 5 °C than at 20 °C), cytoplasmic viscosity increases and respiration weakens; thermophilic plants (such as cucumber) wilt easily in cold soil. High temperature increases respiratory oxygen consumption while the solubility of oxygen falls, accelerates root aging and inactivates enzymes |
| Soil solution concentration | High concentration lowers the soil water potential | Plants have difficulty taking up water on saline-alkali soils, a condition called physiological drought; excessive fertilization causes "burning" of seedlings |
| The root system itself | Root density, total surface area, root permeability | Permeability changes with root age and developmental stage and is affected by suberization of the endodermis |

## 3.3. Water Transport in the Xylem

### 3.3.1. Pathway of Transport and the Conducting Elements

The path of water in the plant can be summarized as: soil → root hair → root cortex and endodermis → pericycle and stelar parenchyma cells → root vessels → stem vessels → vessels of petiole and leaf veins → mesophyll cells → intercellular spaces of the mesophyll → substomatal cavity → stoma → atmosphere. In most plants the **xylem** is the longest segment of this path: in a plant 1 m tall, more than 99.5% of the path length is in the xylem, and the proportion is higher in tall trees.

Two kinds of dead cells conduct water in the xylem: tracheids and vessel elements ([7.12.5](/7.12.5)). At maturity they lose their protoplasts and leave only lignified thick walls, forming hollow tubes of very low resistance. Tracheids are individual spindle-shaped cells, and water flows from one tracheid into the adjacent one through paired **pits** in the side walls; they occur in all vascular plants. Vessel elements are shorter and wider with **perforation plates** in the end walls, and many vessel elements joined end to end form a **vessel**, ranging in length from a few centimeters to several meters, found in angiosperms, gnetophytes and a few ferns. The pit membrane between a pit pair consists of two primary walls and the middle lamella and lets water pass but not easily gas bubbles; the **bordered pits** of conifer tracheids have a **torus**, thickened at the center, and a porous margin around it, and under a large pressure difference the torus is pushed to one side and seals the pit, acting like a valve.

### 3.3.2. Hagen–Poiseuille Flow

Long-distance transport in the xylem is pressure-driven bulk flow. The volume flow rate of laminar flow in a circular tube is given by the **Hagen–Poiseuille law**:

$$
Q = \frac{\pi r^4}{8\eta}\,\frac{\Delta\Psi_{\mathrm{p}}}{\Delta x}, \qquad \bar v = \frac{Q}{\pi r^2} = \frac{r^2}{8\eta}\,\frac{\Delta\Psi_{\mathrm{p}}}{\Delta x}, \tag{3.2}
$$

where $r$ is the tube radius, $\eta$ is the **viscosity** of water ($1.0\times10^{-3}\,\mathrm{Pa\,s}$ at 20 °C) and $\Delta\Psi_{\mathrm{p}}/\Delta x$ is the pressure gradient. The flow rate is extremely sensitive to the radius: doubling the radius increases the flow 16-fold. A single vessel $100\,\mu\mathrm{m}$ in diameter carries $10^4$ times the flow of a tracheid $10\,\mu\mathrm{m}$ in diameter, and 100 times as much per unit cross-sectional area; the stems of climbing plants contain vessels up to $500\,\mu\mathrm{m}$ in diameter, enabling them to transport large amounts of water through slender stems. The rate of water transport also differs among woods accordingly: ring-porous woods have wide, long vessels and the fastest flow; diffuse-porous woods have narrower, shorter vessels and slower flow; gymnosperms with only tracheids are slowest.

The efficiency of the xylem can be illustrated with numbers. Take a flow velocity of $4\,\mathrm{mm\,s^{-1}}$ in the xylem (already high for narrow vessels) and a vessel radius of $40\,\mu\mathrm{m}$; from Eq. (3.2) the pressure gradient required is $8\eta\bar v/r^2 = 8 \times 10^{-3} \times 4\times10^{-3}/(1.6\times10^{-9}) = 2\times10^4\,\mathrm{Pa\,m^{-1}} = 0.02\,\mathrm{MPa\,m^{-1}}$. The inner walls of real vessels are irregular and water must also cross perforation plates and pits, so the measured resistance is about twice that of an ideal tube. By contrast, for water to cross layer after layer of living cells at the same velocity, with each cell crossed by two membranes, the driving force required is about $2\times10^8\,\mathrm{MPa\,m^{-1}}$, ten orders of magnitude greater. Another comparison: if 10 vessel elements joined end to end (each $200\,\mu\mathrm{m}$ long and $50\,\mu\mathrm{m}$ in inner diameter) each retained two plasma membranes, then even with a membrane hydraulic conductivity as high as $3\times10^{-6}\,\mathrm{m\,s^{-1}\,MPa^{-1}}$ (many aquaporins), the resistance of these 20 membrane layers would be about 260 million times that of the membrane-free tube. The conducting elements die and lose their protoplasts precisely in order to eliminate membrane resistance.

Even so, the xylem still contributes appreciably to the total resistance of the whole plant; the paths in root and leaf, though short, pass through living tissue and have a large resistance: the leaf accounts on average for about 30% of the total liquid-phase resistance (3.5).

### 3.3.3. The Pressure Difference Needed to Lift Water to the Top of a 100-m Tree

The tallest trees in the world are the coast redwood (*Sequoia sempervirens*) of North America and the mountain ash (*Eucalyptus regnans*) of Australia, both of which can exceed 100 m. Treating the trunk as a long tube, the pressure gradient needed to maintain the transpiration stream in the xylem of tall trees is about $0.01\,\mathrm{MPa\,m^{-1}}$, so over a height of 100 m about $1\,\mathrm{MPa}$ is needed to overcome frictional resistance. Gravity must also be overcome: from $\Psi_{\mathrm{g}} = \rho_{\mathrm{w}}gh$, a height difference of 100 m corresponds to $1\,\mathrm{MPa}$. Adding the two, a pressure difference of about $2\,\mathrm{MPa}$ is needed from the base of the tree to the top of the crown. Root pressure is generally less than $0.1\,\mathrm{MPa}$ and disappears during transpiration, so it obviously cannot supply such a pressure difference; moreover, transporting water by root pressure would mean that the leaves must continually deal with the large amounts of solutes carried along with the water. Water must be "pulled" up.

### 3.3.4. The Cohesion–Tension Theory

**Definition 3.3.1 (Cohesion–Tension Theory)** Transpiration from the leaf lowers the water potential in the mesophyll cell walls and creates a large negative hydrostatic pressure (tension) in the xylem; this tension is transmitted down along the continuous water column in the xylem and pulls water from the root toward the leaf; the cohesion among water molecules allows the water column to withstand such tension without breaking, and the adhesion of water to the vessel walls attaches the column to the walls. This theory of the ascent of water through the xylem is called the **cohesion–tension theory**.

The theory was proposed by Dixon and Joly in 1894. The source of the tension is in the leaf. When the stomata are open, water vapor diffuses out of the leaf and water on the surfaces of mesophyll cell walls evaporates; the remaining water retreats into the fine gaps between the cell wall microfibrils, forming curved air–water interfaces. Cellulose is hydrophilic (contact angle about zero), and by Eq. (3.1) the smaller the radius of curvature of the meniscus, the greater the negative pressure of the water: $-0.3\,\mathrm{MPa}$ at a radius of $0.5\,\mu\mathrm{m}$, $-3\,\mathrm{MPa}$ at $0.05\,\mu\mathrm{m}$ and $-15\,\mathrm{MPa}$ at $0.01\,\mu\mathrm{m}$. The more evaporation, the deeper the interface retreats, the greater the curvature and the greater the tension. This is completely analogous to the situation in the soil: the plant holds on to water by capillary forces at both ends, and the leaf end pulls tighter, like a tug of war with water as the rope.

Water flows from the leaf cell walls toward the sites of evaporation; part of it comes from the protoplasts of neighboring cells, but because the leaf is connected to the soil through the low-resistance xylem, most of the water that replaces the water lost in transpiration comes from the soil. This requires a continuous liquid path from the site of evaporation through the plant all the way to the soil. The whole process consumes no metabolic energy directly: the energy driving the movement of water comes from the sun, which heats the leaf and the surrounding air and makes water evaporate. But water transport is not free: the plant must build vessels that can withstand great tension without collapsing (thickened and lignified secondary walls; plants with high xylem tension have high wood density), and must accumulate enough solutes in living cells for them to maintain turgor as water potential falls.

The main evidence supporting the cohesion–tension theory:

1. Tension does exist in the xylem. Measured with the pressure chamber, the xylem water potential of branches of transpiring trees is $-1.2$ to $-3.5\,\mathrm{MPa}$, and lower still in plants of arid regions (Scholander et al., 1965); if the xylem of a transpiring plant is pierced through a drop of ink on the stem, the ink is drawn in immediately and forms visible streaks along the stem.
2. Water can withstand very large tensions. Because of hydrogen bonding, water has a high tensile strength: in careful experiments water columns can withstand tensions exceeding $20\,\mathrm{MPa}$ (often quoted as $30\,\mathrm{MPa}$), far greater than the negative pressures that can occur in the xylem.
3. Water flows stably under negative pressure. Xylem pressures measured by applying known tensions to branches in a centrifuge agree with the results of the pressure chamber (Holbrook et al., 1995; Pockman et al., 1995); in "artificial trees" made with microfluidic chips, liquid water was stably pulled by evaporation at pressures below $-7\,\mathrm{MPa}$ (Wheeler and Stroock, 2008).
4. Gas bubbles in the xylem can be confined and removed (3.3.5).

The theory has been controversial for over a century: in the early 1990s the xylem negative pressures measured directly with a pressure probe were far smaller than the results of the pressure chamber, which for a time cast doubt on it; the centrifuge experiments above showed that the problem lay in the cavitation triggered when the pressure probe was inserted into a vessel, not in the theory itself. The cohesion–tension theory is now the accepted explanation of water transport in the xylem.

### 3.3.5. Cavitation and Embolism

Water in the xylem is in a metastable state. Liquid water is stable only when its hydrostatic pressure is higher than its **saturated vapor pressure**; at 20 °C the saturated vapor pressure of water is about $0.0023\,\mathrm{MPa}$ (absolute pressure), whereas the pressure in the xylem at the top of a tree is $-2\,\mathrm{MPa}$, far below it. Water does not vaporize because (1) cohesion and adhesion make the free-energy barrier to the liquid–vapor phase change very high, and (2) the structure of the xylem provides few nucleation sites that could lower this barrier. The most important nucleation sites are gas bubbles: water in the root must cross the endodermis to enter the xylem, and the endodermis acts like a filter that prevents bubbles from entering; pit membranes also act as filters.

**Definition 3.3.2 (Cavitation and Embolism)** The rapid expansion of a gas bubble in a water column under tension, breaking the column, is called **cavitation**; after cavitation the conducting element is filled with gas and loses its water-conducting function, which is called **embolism**.

Once a bubble is large enough that the inward pressure produced by surface tension ($2T/r$) is smaller than the outward pull produced by the negative pressure of the liquid, it expands, and as it expands its curvature decreases and the inward pressure decreases further, until it fills the entire conducting element. Cavitation occurs mainly in two ways:

- *Air seeding*: when a conducting element is already gas-filled (wounded, after leaf abscission or because an adjacent vessel is already embolized) and one side of a pit membrane is in contact with air, if the pressure difference across the pit membrane exceeds the pressure $2T/r_{\mathrm{pore}}$ that the meniscus in a pit membrane pore can withstand, air is pulled through the pit membrane (in conifers, the torus is pushed off its seat), causing cavitation of the adjacent conducting element. A pore radius of 50 nm corresponds to a threshold of about $2.9\,\mathrm{MPa}$ and 10 nm to about $15\,\mathrm{MPa}$, so the pore size of pit membranes largely determines the resistance of wood to cavitation.
- Freeze–thaw: gases are dissolved in water and are almost insoluble in ice, and the bubbles released when xylem freezes may expand into emboli on thawing. Bubbles released in wide vessels are larger and more likely to cause embolism on thawing, so wide, long vessels are more at risk in cold regions ([7.12.5](/7.12.5)).

In drought, acoustic emissions can be detected from plants: the sudden formation and expansion of bubbles raises the local water pressure momentarily by about $1\,\mathrm{MPa}$ or more and produces high-frequency sound waves. If not limited, cavitation would be catastrophic: emboli block the main pathways for water, increase resistance, and eventually cause leaves and other organs to dehydrate and die.

The sensitivity of species to cavitation is expressed by the *vulnerability curve*: the percentage loss of hydraulic conductivity (PLC) of a branch, stem segment or root segment is plotted against the applied xylem water potential. It is commonly described in Weibull form:

$$
\mathrm{PLC} = 100\left[1 - \exp\!\left(-\left(\frac{-\Psi_{\mathrm{x}}}{b}\right)^{c}\right)\right], \qquad P_{50} = -b\,(\ln 2)^{1/c}, \tag{3.3}
$$

where $\Psi_{\mathrm{x}}$ is the xylem water potential, $b$ and $c$ are shape parameters, and $P_{50}$ is the xylem water potential at which half of the hydraulic conductivity is lost, the standard index for comparing the resistance of different species to cavitation. Species of moist habitats (such as riparian poplars and birches) have $P_{50}$ of only about $-1$ to $-2\,\mathrm{MPa}$, and shrubs of arid regions (such as *Artemisia*) can be below $-8\,\mathrm{MPa}$. The difference between the lowest xylem water potential actually reached in the field, $\Psi_{\min}$, and $P_{50}$ is called the *hydraulic safety margin*. An analysis of more than 200 forest tree species worldwide found that about 70% of species have a safety margin of less than $1\,\mathrm{MPa}$; that is, trees of both wet and dry habitats operate close to their hydraulic limits (Choat et al., 2012), which explains why severe drought causes widespread tree mortality in all kinds of forests.

![Xylem vulnerability curves (Eq. (3.3), schematic parameters for three representative woody plants). The ordinate is the percentage loss of hydraulic conductivity and the abscissa is the xylem water potential (increasingly negative to the right). A riparian tree has $P_{50} = -1.5\,\mathrm{MPa}$ (blue), a mesic tree $-3.5\,\mathrm{MPa}$ (green) and a desert shrub $-8\,\mathrm{MPa}$ (red); dots mark the 50% loss points; the arrows above are the lowest xylem water potentials $\Psi_{\min}$ each reaches in the field, and the double arrows and numbers at the bottom are the hydraulic safety margins $\Psi_{\min} - P_{50}$ ($0.3$, $0.9$ and $2.5\,\mathrm{MPa}$): drought-tolerant species are not farther from danger, but their curves as a whole are shifted toward more negative water potentials](./plots/vulnerability.py)

Plants limit the consequences of cavitation in several ways:

1. Confinement: conducting elements have limited length and are connected to one another through pits, and gas bubbles do not easily pass through the fine pores of pit membranes, so an embolus is usually confined to a single tracheid or vessel; water can bypass it and continue to flow through adjacent water-filled elements. Conducting elements of limited length increase the resistance but also limit the effect of cavitation.
2. Repair: root pressure at night can compress bubbles and make the gas redissolve (lianas such as grape repair winter freeze–thaw emboli with root pressure in spring); some studies suggest that the xylem can also repair emboli under tension, but the mechanism is unclear and remains controversial.
3. Renewal: plants with **secondary growth** form new xylem every year to compensate for the loss of conducting capacity caused by embolism.

## 3.4. Transpiration

### 3.4.1. Concept, Modes and Significance of Transpiration

**Definition 3.4.1 (Transpiration)** The process by which water is lost from the aerial parts of a plant to the atmosphere in the form of water vapor is called **transpiration**.

Only a small part (1%–3%) of the water absorbed by the plant is used for growth and metabolism, and the great majority (about 97%) is lost by transpiration. Transpiration differs from evaporation: it is regulated by plant structure (stomata, cuticle) and physiology (stomatal opening and closing).

The mode of transpiration varies with the age and organ of the plant. In young plants the whole surface of the shoot can transpire; in mature plants, the stems and branches of woody plants can transpire through **lenticels**, but the proportion is very small (about 0.1%), and transpiration occurs mainly through the leaves. Leaf transpiration is of two kinds: cuticular transpiration through the **cuticle** and stomatal transpiration through the **stomata**. The wax in the cuticle is almost impermeable to water, which passes slightly only because of hydrophilic pectin and fine cracks, and the water lost through the cuticle of a mature leaf is usually only about 5%; young leaves and shade plants have thin cuticles and a higher proportion of cuticular transpiration, and in the submerged leaves of aquatic plants cuticular transpiration predominates. In mature leaves of sun plants more than 80%–90% of transpiration is through the stomata, so the stomata are the main pathway for the escape of water vapor and the entry of $\ce{CO2}$; the number, distribution and opening mechanism of stomata are treated in [7.13.10](/7.13.10).

The physiological significance of transpiration:

1. Driving force: transpiration establishes a water potential gradient between soil, plant and atmosphere and is the main driving force for water uptake and water transport by plants, especially tall trees.
2. Transport: mineral salts absorbed by the root and substances such as hormones synthesized in the root are carried in the transpiration stream. Minerals reach the leaves mainly by bulk flow and transpiration promotes this, but it is not a prerequisite for mineral transport: at night, without transpiration, root pressure can also drive xylem sap upward.
3. Cooling: the heat of vaporization of water is high, and transpiration carries away large amounts of heat so that leaves exposed to strong light do not overheat. For example, at a transpiration rate $E = 3.6\,\mathrm{mmol\,m^{-2}\,s^{-1}}$ the latent heat flux is $\lambda E = 3.6\times10^{-3} \times 44\times10^3 = 160\,\mathrm{W\,m^{-2}}$, equivalent to about a quarter to a third of the radiant energy absorbed by a leaf at noon on a sunny day.
4. Gas exchange: transpiration accompanies the opening of stomata, which lets the $\ce{CO2}$ needed for photosynthesis enter the leaf.

### 3.4.2. Indices of Transpiration

- *Transpiration rate*: the amount of water lost by transpiration per unit time per unit leaf area, usually expressed in $\mathrm{mmol\,m^{-2}\,s^{-1}}$ in physiological ecology and often in $\mathrm{g\,m^{-2}\,h^{-1}}$ in agronomy ($1\,\mathrm{mmol\,m^{-2}\,s^{-1}} = 64.8\,\mathrm{g\,m^{-2}\,h^{-1}}$). Typical plants transpire about $15$–$250\,\mathrm{g\,m^{-2}\,h^{-1}}$ in the daytime and about $1$–$20\,\mathrm{g\,m^{-2}\,h^{-1}}$ at night. The transpiration rate has already been normalized by leaf area, so it does not itself vary with leaf area, whereas the water loss of the whole plant is proportional to leaf area. The common statement that "transpiration rate is independent of leaf area" holds only in this sense.
- Transpiration ratio and water-use efficiency: see 3.4.5.

Methods of measurement: gravimetric methods (rapid weighing of detached organs, or weight changes of potted plants and weighing lysimeters); stomatal porometers or open gas-exchange systems that measure the change in air humidity in the leaf chamber, the latter using an infrared gas analyzer to measure $\ce{CO2}$ and water vapor simultaneously; stem sap flow (heat pulse, thermal dissipation probes); and indirect estimation from leaf and canopy temperatures obtained by infrared thermometry.

### 3.4.3. The Driving Force of Transpiration

Liquid water within the leaf is driven by water potential gradients, but the last segment from leaf to atmosphere is diffusion of water vapor, controlled by the water vapor concentration gradient. The transpiration rate depends on two factors: the water vapor concentration difference between the internal air spaces of the leaf and the external atmosphere, $\Delta c_{\mathrm{wv}} = c_{\mathrm{wv(leaf)}} - c_{\mathrm{wv(air)}}$, and the resistance of this diffusion path.

The volume of the internal air spaces of the leaf is not large (about 5% of leaf volume in pine needles, 10% in maize leaves, 30% in barley, 40% in tobacco), but the surface area of the evaporating cell walls is 7 to 30 times the external surface area of the leaf, so the air in the leaf is nearly in water potential equilibrium with the cell wall surfaces. From the relation $\Psi = (RT/\bar V_{\mathrm{w}})\ln\mathrm{RH}$ of [7.6.3](/7.6.3#eq-3.7), even when the leaf water potential is as low as $-2\,\mathrm{MPa}$ the relative humidity of the air in the leaf remains above 98%: for example, at 25 °C the relative humidity of the internal air space is 0.99, with a water potential of $-1.38\,\mathrm{MPa}$; the relative humidity of air just outside the stoma drops to about 0.47, with a water potential of $-104\,\mathrm{MPa}$. The water vapor concentration in the leaf can therefore be estimated from the saturation water vapor concentration at leaf temperature, and leaf temperature is easy to measure.

The saturated vapor pressure rises nearly exponentially with temperature (the **Clausius–Clapeyron equation**), commonly approximated by the empirical Tetens formula:

$$
e_{\mathrm{s}}(T) = 0.6108\,\exp\!\left(\frac{17.27\,t}{t + 237.3}\right)\ \mathrm{kPa}, \tag{3.4}
$$

where $t$ is the temperature in degrees Celsius: $2.34\,\mathrm{kPa}$ at 20 °C, $3.17\,\mathrm{kPa}$ at 25 °C and $4.24\,\mathrm{kPa}$ at 30 °C. The leaf-to-air vapor pressure difference $D = e_{\mathrm{s}}(T_{\mathrm{leaf}}) - e_{\mathrm{air}}$ is the driving force of transpiration; expressed as a mole fraction, $\Delta w = D/p$, where $p$ is atmospheric pressure. Leaf temperature has a large effect on transpiration: with air at 25 °C and relative humidity 50%, if the leaf temperature is also 25 °C, $\Delta w = (3.17 - 1.58)/101.3 = 0.0156$; if the leaf temperature rises to 30 °C, $\Delta w = (4.24 - 1.58)/101.3 = 0.0263$, an increase of the driving force of about 70%.

### 3.4.4. Resistances to Transpiration: Stomatal and Boundary-Layer Conductance

Water vapor passes two resistances from the leaf interior to the atmosphere: the resistance of the stomata, $r_{\mathrm{s}}$, and the resistance of the layer of unstirred air adjacent to the leaf surface, the leaf *boundary layer* resistance $r_{\mathrm{b}}$. Expressed in terms of the reciprocal of resistance, the conductance ($\mathrm{mol\,m^{-2}\,s^{-1}}$), the two are in series:

$$
E = g_{\mathrm{tw}}\,\Delta w, \qquad \frac{1}{g_{\mathrm{tw}}} = \frac{1}{g_{\mathrm{s}}} + \frac{1}{g_{\mathrm{b}}}, \tag{3.5}
$$

where $g_{\mathrm{s}}$ is the **stomatal conductance**, $g_{\mathrm{b}}$ is the boundary-layer conductance and $E$ is the transpiration rate. The thickness of the boundary layer is determined mainly by wind speed and leaf size. For a flat leaf the boundary-layer conductance to water vapor can be approximated by $g_{\mathrm{b}} \approx 0.147\sqrt{u/d}\,\mathrm{mol\,m^{-2}\,s^{-1}}$ ($u$ is wind speed in $\mathrm{m\,s^{-1}}$; $d$ is the characteristic dimension of the leaf in the downwind direction in m): for a leaf width of 5 cm, $g_{\mathrm{b}} \approx 0.29$ in a light breeze ($0.2\,\mathrm{m\,s^{-1}}$) and about $1.1\,\mathrm{mol\,m^{-2}\,s^{-1}}$ in a wind of $3\,\mathrm{m\,s^{-1}}$.

**Example 3.4.1 (Transpiration rate of a leaf)** Leaf and air temperatures are both 25 °C, air relative humidity is 50% and atmospheric pressure 101.3 kPa; $g_{\mathrm{s}} = 0.3$ and $g_{\mathrm{b}} = 1.0\,\mathrm{mol\,m^{-2}\,s^{-1}}$. Find the transpiration rate.

$g_{\mathrm{tw}} = 1/(1/0.3 + 1/1.0) = 0.231\,\mathrm{mol\,m^{-2}\,s^{-1}}$ and $\Delta w = 0.0156$, so $E = 0.231 \times 0.0156 = 3.6\times10^{-3}\,\mathrm{mol\,m^{-2}\,s^{-1}} = 3.6\,\mathrm{mmol\,m^{-2}\,s^{-1}}$, that is, $3.6 \times 64.8 \approx 234\,\mathrm{g\,m^{-2}\,h^{-1}}$. If the wind stops and $g_{\mathrm{b}}$ drops to 0.29, then $g_{\mathrm{tw}} = 0.147$ and transpiration falls to $2.3\,\mathrm{mmol\,m^{-2}\,s^{-1}}$ (assuming unchanged leaf temperature).

At high wind speed the boundary layer is thin and its resistance small, the stomatal resistance dominates, and transpiration is controlled mainly by the stomata; in still air the boundary layer is very thick and becomes the main obstacle to water vapor loss, so opening the stomata wider has little effect on transpiration, although closing them completely still reduces it. The degree of this "stomatal control" can be compared quantitatively with $\mathrm{d}\ln E/\mathrm{d}\ln g_{\mathrm{s}} = g_{\mathrm{b}}/(g_{\mathrm{s}} + g_{\mathrm{b}})$. The actual situation is more complicated: wind also couples leaf temperature to air temperature through the boundary layer, and a rise in leaf temperature in still air increases the driving force.

![Dependence of transpiration rate on stomatal and boundary-layer conductance (Eq. (3.5); leaf and air temperature 25 °C, relative humidity 50%, characteristic leaf dimension 5 cm, leaf temperature taken as constant). A: transpiration rate as a function of stomatal conductance: in wind ($u = 3\,\mathrm{m\,s^{-1}}$, $g_{\mathrm{b}} = 1.14$, blue) transpiration increases almost in proportion to stomatal conductance; in still air ($u = 0.2\,\mathrm{m\,s^{-1}}$, $g_{\mathrm{b}} = 0.29\,\mathrm{mol\,m^{-2}\,s^{-1}}$, red) transpiration quickly approaches an upper limit set by the boundary layer (dashed line). B: the degree of stomatal control of transpiration, $\mathrm{d}\ln E/\mathrm{d}\ln g_{\mathrm{s}}$: near 1 transpiration is controlled by the stomata, near 0 by the boundary layer](./plots/boundary-layer.py)

Many morphological features of leaves influence the thickness of the boundary layer: hairs on the leaf surface act like miniature windbreaks; sunken stomata (such as the stomatal crypts of oleander) create a protected space outside the stomata; the size and shape of the leaf and its angle to the wind direction all affect how wind sweeps over the leaf surface. Most of these features cannot be changed within hours or days; short-term regulation of transpiration depends on the control of stomatal aperture by the guard cells. Some plants can also change leaf orientation: aligning the leaf parallel to the sun's rays lowers leaf temperature and hence $\Delta w$; many grasses roll their leaves under water shortage, increasing the boundary layer resistance; even wilting reduces the radiation intercepted and lowers leaf temperature.

### 3.4.5. Transpiration Ratio and Water-Use Efficiency

**Definition 3.4.2 (Transpiration Ratio and Water-Use Efficiency)** The ratio of the amount of water lost by plant transpiration to the amount of $\ce{CO2}$ assimilated by photosynthesis over the same period is called the **transpiration ratio**; its reciprocal, the amount of carbon assimilated per unit amount of water transpired, is called the **water-use efficiency** (WUE). On a molar basis, $\mathrm{WUE} = 1/\mathrm{TR}$.

A C3 plant loses as many as about 400 water molecules for each $\ce{CO2}$ molecule fixed, a transpiration ratio of about 400 and a water-use efficiency of about $1/400 = 0.0025$; for C4 plants the ratio is about 150, and for CAM plants about 50. Agronomy often uses another expression, the grams of water consumed per gram of dry matter accumulated by the plant (also called the transpiration coefficient), which is a few hundred for common crops: about 300 for C4 crops such as sorghum and maize and about 500–800 for C3 crops such as wheat, rice, soybean and alfalfa; for a given crop it varies greatly with climate and cultivation conditions.

The exchange ratio between water and $\ce{CO2}$ is so lopsided for three reasons:

1. The concentration gradient driving water loss is about 50 times that driving $\ce{CO2}$ uptake: $\ce{CO2}$ makes up only about 0.04% of the atmosphere, whereas the water vapor concentration inside the leaf is relatively very high.
2. $\ce{CO2}$ diffuses in air about 1.6 times more slowly than water vapor ($\ce{CO2}$ molecules are larger and have a smaller diffusion coefficient).
3. Before entering the chloroplast, $\ce{CO2}$ must also cross the plasma membrane, cytoplasm and chloroplast envelope, all of which add resistance to the $\ce{CO2}$ diffusion path.

These three points can be combined in one equation. The photosynthetic rate is $A = g_{\mathrm{s,c}}(c_{\mathrm{a}} - c_{\mathrm{i}})$, where $c_{\mathrm{a}}$ and $c_{\mathrm{i}}$ are the mole fractions of $\ce{CO2}$ in the atmosphere and the intercellular spaces and the stomatal conductance for $\ce{CO2}$ is $g_{\mathrm{s,c}} = g_{\mathrm{s}}/1.6$; dividing by Eq. (3.5) (neglecting the boundary layer), the instantaneous water-use efficiency is

$$
\frac{A}{E} = \frac{c_{\mathrm{a}}\,(1 - c_{\mathrm{i}}/c_{\mathrm{a}})}{1.6\,\Delta w}. \tag{3.6}
$$

**Example 3.4.2 (Water-use efficiency of C3 and C4 leaves)** Take $c_{\mathrm{a}} = 420\,\mu\mathrm{mol\,mol^{-1}}$ and $\Delta w = 0.0156$ (25 °C, relative humidity 50%). For a C3 leaf $c_{\mathrm{i}}/c_{\mathrm{a}} \approx 0.7$, and $A/E = 420\times10^{-6} \times 0.3/(1.6 \times 0.0156) = 5.0\times10^{-3}$, that is, about 200 water molecules lost for each $\ce{CO2}$ assimilated. In a C4 leaf, because PEP carboxylase draws the intercellular $\ce{CO2}$ concentration down to a very low level ($c_{\mathrm{i}}/c_{\mathrm{a}} \approx 0.4$), $A/E = 1.0\times10^{-2}$, about 100 water molecules, twice the efficiency of C3. The transpiration ratio of whole plants over a whole season is higher (about 400 for C3) because carbon lost in respiration, water loss at night and drier air must also be counted. Eq. (3.6) also explains why CAM plants have the lowest transpiration ratio: their stomata open at night and close during the day, and at night leaf temperature is low and $\Delta w$ is very small ([7.13.8](/7.13.8)).

Eq. (3.6) shows that water-use efficiency is determined by two kinds of factors: the evaporative demand of the environment $\Delta w$ (the same plant is more efficient under moist, cool conditions than under hot, dry ones), and the plant's ability to keep $c_{\mathrm{i}}$ low (C4 photosynthesis, low stomatal conductance). Lowering stomatal conductance can raise water-use efficiency but also lowers the photosynthetic rate, a long-standing trade-off in breeding drought-resistant crops ([7.13.9](/7.13.9)).

### 3.4.6. Factors Affecting Transpiration

| Category | Factor | Effect on transpiration and reason |
|---|---|---|
| Leaf structure | Stomatal frequency, stomatal size, volume of the substomatal cavity | Transpiration increases as these increase |
| | Stomatal position, surface appendages, cuticle, stomatal crypts | Sunken stomata, many epidermal hairs and a thick, intact cuticle increase the boundary-layer or epidermal resistance and reduce transpiration |
| Physiology | Photosynthetic type | Water lost per unit $\ce{CO2}$ fixed: CAM < C4 < C3 |
| | Stomatal aperture, leaf water status, **abscisic acid** | Water deficit and abscisic acid close the stomata and reduce transpiration |
| Environment | Light | Opens the stomata and at the same time raises leaf temperature, increasing the vapor pressure difference between leaf and air, so transpiration speeds up |
| | Air humidity | The higher the humidity, the smaller the vapor pressure difference between leaf and air and the slower the transpiration |
| | Temperature | When temperature rises, the saturated vapor pressure in the leaf increases more than the actual vapor pressure of the atmosphere, so the vapor pressure difference increases and transpiration is enhanced; excessively high temperature closes the stomata |
| | Wind | A light breeze thins the boundary layer and speeds transpiration; dry wind promotes and humid wind reduces transpiration; strong wind causes the guard cells to lose water and the stomata to close, so transpiration decreases instead |
| | Soil | Affects transpiration indirectly by affecting water uptake by roots |

## 3.5. The Soil–Plant–Atmosphere Continuum

### 3.5.1. The Series-Resistance Model

**Definition 3.5.1 (Soil–Plant–Atmosphere Continuum)** The physically continuous system formed by water from the soil through root, stem and leaf to the atmosphere, in which water moves in the direction of decreasing water potential from segment to segment, is called the **soil–plant–atmosphere continuum** (SPAC).

Along this path, the mode of water movement and the driving force differ from segment to segment: in the soil and xylem, liquid water moves by bulk flow under pressure gradients ($\Delta\Psi_{\mathrm{p}}$); when liquid water crosses membranes (water uptake by cells, water crossing the endodermis in the root), the driving force is the transmembrane water potential difference and the flow is osmotic; in the gas phase water moves mainly by diffusion, and once it reaches the air outside the leaf, convection (a form of bulk flow) predominates.

van den Honert (1948) likened this process to an electrical circuit: at steady state the water flow through each segment is equal, and the water potential drop across each segment equals the flow times the resistance of that segment, as in **Ohm's law**.

$$
E = \frac{\Psi_{\mathrm{soil}} - \Psi_{\mathrm{leaf}} - \rho_{\mathrm{w}}gh}{R_{\mathrm{soil}} + R_{\mathrm{root}} + R_{\mathrm{stem}} + R_{\mathrm{leaf}}}
= K_{\mathrm{plant}}\,(\Psi_{\mathrm{soil}} - \Psi_{\mathrm{leaf}} - \rho_{\mathrm{w}}gh), \tag{3.7}
$$

where $E$ is expressed per unit leaf area and $K_{\mathrm{plant}}$ is the conductance of the whole liquid-phase pathway (per unit leaf area, in $\mathrm{mmol\,m^{-2}\,s^{-1}\,MPa^{-1}}$). The total water potential drop in the liquid phase is only a few MPa, whereas in the gas phase from the leaf interior to the atmosphere the water potential falls abruptly from about $-1.4\,\mathrm{MPa}$ to about $-100\,\mathrm{MPa}$ (the water potential drop in air is far greater than in the liquid phase, so the segment of water vapor diffusion cannot be written as a resistor in the same circuit and must be treated separately with Eq. (3.5)). The leaf, although short in the liquid-phase path, accounts on average for about 30% of the total liquid-phase resistance; leaf hydraulic resistance increases with decreasing vein density, with shading, with leaf age and with falling leaf water potential, and can differ 40-fold between leaves of different venation.

### 3.5.2. Diurnal Course and Drought

The diurnal course of leaf water potential can be deduced from Eq. (3.7). At night transpiration stops, $E \approx 0$, and the leaf and soil approach equilibrium, so that the predawn leaf water potential equals the soil water potential minus the gravitational term; the predawn water potential is therefore a good indicator of the soil water status in the root zone of the plant. In the daytime transpiration increases and leaf water potential falls with $E$, reaching a minimum at midday and recovering in the afternoon as transpiration weakens. When the soil dries, the predawn water potential is already low; the decline in soil hydraulic conductivity reduces $K_{\mathrm{plant}}$, and even if partial stomatal closure reduces $E$, the midday leaf water potential is still lower.

**Example 3.5.1 (Midday leaf water potential)** A tree 10 m tall has a soil water potential of $-0.1\,\mathrm{MPa}$, a whole-pathway conductance $K_{\mathrm{plant}} = 6\,\mathrm{mmol\,m^{-2}\,s^{-1}\,MPa^{-1}}$ and a midday transpiration rate of $5\,\mathrm{mmol\,m^{-2}\,s^{-1}}$. From Eq. (3.7), $\Psi_{\mathrm{leaf}} = -0.1 - 0.1 - 5/6 = -1.03\,\mathrm{MPa}$. When the soil has dried to $-0.8\,\mathrm{MPa}$, the conductance has halved and transpiration has also halved because of partial stomatal closure, $\Psi_{\mathrm{leaf}} = -0.8 - 0.1 - 2.5/3 = -1.73\,\mathrm{MPa}$. If the turgor loss point of this plant is $-1.5\,\mathrm{MPa}$ ([7.13.2](/7.13.2#sec-2.5.2)), its leaves lose turgor at midday in drought; to avoid this, the stomata must close further, at the cost of reduced photosynthesis.

![Series-resistance model of the soil–plant–atmosphere continuum (Eq. (3.7); a tree 10 m tall, schematic values per unit leaf area). A: top: diurnal course of transpiration rate for moist soil (blue, peak $5\,\mathrm{mmol\,m^{-2}\,s^{-1}}$) and dry soil (red, stomata partly closed, peak halved); bottom: leaf water potential, which at night differs from soil water potential (dotted line) only by the gravitational term $0.1\,\mathrm{MPa}$ and falls to a minimum at midday: $-1.03\,\mathrm{MPa}$ when moist and $-1.73\,\mathrm{MPa}$ in drought. B: water potential profile along the path: the dashed line is predawn (gravitational term only) and the solid line is midday; in moist soil the water potential drop is mainly in the root and leaf, whereas in drought the hydraulic conductivity of the soil falls greatly and the largest drop shifts to between the soil and the root surface](./plots/spac.py)

In arid habitats, SPAC can also show reversed water flow. When transpiration stops at night, water absorbed by roots in deep moist soil can flow through the root system to roots in shallow dry soil and be released from there into the shallow soil; this phenomenon is called hydraulic lift, or more generally *hydraulic redistribution*, and was first demonstrated in big sagebrush (*Artemisia tridentata*) of the western United States (Richards and Caldwell, 1987). It alleviates drought in the shallow soil, allows nutrient uptake in shallow roots and decomposition of organic matter to continue, and also benefits neighboring shallow-rooted plants.

## 3.6. Rational Irrigation

### 3.6.1. Water Requirements of Crops

The goal of rational irrigation is to obtain the greatest economic return with the least water, which requires irrigating at the right time and in the right amount according to the water requirements of the crop. Different crops need different amounts of water: soybean and rice need more, wheat and sugarcane less, and sorghum and maize least (C4 crops have lower transpiration ratios, 3.4.5). The same crop also needs different amounts of water at different developmental stages; taking wheat as an example:

| Period | Growth characteristics | Water requirement |
|---|---|---|
| Germination to early tillering | Mainly vegetative growth, rapid root development, small leaf area | Water consumption not great |
| Late tillering to heading | Rapid development of stems, leaves and ears, vigorous metabolism | Greatest water consumption; the booting stage (tetrad formation to pollen grain formation) is the first critical period for water |
| Heading to start of grain filling | Leaf area essentially fixed; flowering, fertilization and embryo development | Under water shortage the upper leaves draw water from the floral organs below and yield falls; vulnerable to damage by hot dry winds |
| Start of grain filling to end of milk stage | Photosynthate transported to the grain | Second critical period for water: water shortage makes grain filling difficult and also inhibits photosynthesis in the flag leaf |
| End of milk stage to full ripeness | Grain ripening | No water supply needed; irrigation is in fact harmful, causing unproductive tillers at the stem base, excess grain water content, lower quality and lower protein content |

The *critical period for water* is the period when the crop is most sensitive to water shortage and when water shortage affects yield most; it is generally the stretch from meiosis of the pollen mother cells to flowering and fertilization ([7.13.23](/7.13.23)).

### 3.6.2. Indicators for Irrigation

- Soil indicators: soil water content (a certain fraction of field capacity, for example 60%–70%, depending on crop and developmental stage, is often used as the lower limit for irrigation) or soil water potential.
- Morphological indicators: under water shortage young stems and leaves wilt; leaf color is dark green (cell growth slows while chlorophyll accumulates relatively) or turns red (in drought the breakdown of carbohydrates exceeds synthesis and more anthocyanins form); growth rate declines. By the time morphological indicators appear, the plant has often already been injured.
- Physiological indicators: leaf water potential (especially predawn water potential), cell sap concentration or osmotic potential, stomatal aperture or stomatal conductance; an increase in canopy temperature also reflects weakened transpiration. Physiological indicators are earlier and more sensitive than morphological ones.

### 3.6.3. Methods of Irrigation and Water-Saving Irrigation

Traditional flood irrigation (furrow and border irrigation) uses a large amount of water, part of which is lost by deep percolation and surface evaporation, and may also lead to secondary salinization. Water-saving irrigation methods include:

- Sprinkler irrigation: irrigation equipment sprays water as a mist above the crop, from which it falls onto the crop and soil; it saves water and can modify the microclimate of the field.
- Drip irrigation: a network of pipes is laid on or under the ground so that water drips into the root zone at set times and amounts; it has the highest water-use efficiency.

Further water-saving strategies exploit the crop's own physiological regulation:

- *Deficit irrigation*: the crop is deliberately subjected to water deficit during certain periods. Regulated deficit irrigation reduces watering in non-critical periods and concentrates the limited water in the critical periods, raising water-use efficiency without appreciable yield loss; sustained deficit irrigation stops watering after early irrigation and lets the soil dry gradually, so that the plant gradually adapts, reducing canopy area and biomass but not markedly lowering the harvest index. Wine grapes need a certain water stress to improve fruit quality, a typical application of deficit irrigation.
- *Partial root-zone drying*: only part of the root zone is irrigated, alternating between sides. Signals such as **abscisic acid** produced by roots on the dry side are carried to the leaves and reduce stomatal aperture and transpiration, while roots on the wet side continue to meet the water needs of the plant.
- Alternate wetting and drying irrigation: an important measure for water-saving, high-yield rice cultivation, in which a layer of water is maintained on the field for a period and then allowed to drain naturally, and water is applied again before the soil cracks severely. It makes full use of rainfall and reduces irrigation water, reduces unproductive tillers, raises the percentage of productive panicles, improves canopy structure, improves the physical and chemical properties of the soil, and promotes the transport of assimilates to the grain and grain filling, especially in the weaker grains.

Besides meeting the physiological water needs of crops, irrigation also has an ecological function of improving the growing environment: early rice is irrigated deeply before a cold wave to protect against cold; saline-alkali soils are irrigated to leach salts and to suppress the rise of salts with capillary water; fields of dryland crops are irrigated after fertilization to dissolve the fertilizer.

## Summary

| Link | Driving force and mechanism | Main resistance or limitation | Typical values |
|---|---|---|---|
| Soil water (3.1) | Meniscus negative pressure $\Psi_{\mathrm{p}} = -2T/r$; bulk flow | Soil hydraulic conductivity falls sharply on drying | Field capacity $-0.01$ to $-0.033\,\mathrm{MPa}$; permanent wilting point about $-1.5\,\mathrm{MPa}$ |
| Site of root uptake (3.2.1) | Root hair zone strongest | Suberization of old root segments | Root hairs of wheat over 60% of root surface area |
| Pathways of root uptake (3.2.2) | Apoplast, symplast and transmembrane pathways; composite transport | The Casparian strip of the endodermis forces water across membranes; aquaporins determine root hydraulic conductivity | Hypoxia closes aquaporins |
| Root pressure (Definition 3.2.1) | Ion loading lowers xylem $\Psi_{\mathrm{s}}$, osmotic water uptake | Appears only when transpiration is weak | Generally $< 0.1\,\mathrm{MPa}$, up to $0.2\,\mathrm{MPa}$ |
| Bleeding, guttation | Evidence for root pressure; guttation through hydathodes | — | Bleeding of grape and birch in spring; sugar maple sap flow from stem pressure |
| Xylem transport (3.3.2) | Pressure-driven bulk flow, Hagen–Poiseuille | Flow $\propto r^4$; pits and perforation plates about double the resistance | $0.02\,\mathrm{MPa\,m^{-1}}$ ($r = 40\,\mu\mathrm{m}$, $4\,\mathrm{mm\,s^{-1}}$); living-cell path $10^{10}$ times greater |
| The 100-m tree | Friction about $1\,\mathrm{MPa}$ + gravity about $1\,\mathrm{MPa}$ | Root pressure falls far short | About $2\,\mathrm{MPa}$ |
| Cohesion–tension theory (Definition 3.3.1) | Tension generated by menisci in mesophyll cell walls, transmitted by cohesion of water | The water column is metastable | Xylem $-1.2$ to $-3.5\,\mathrm{MPa}$; tensile strength of water $> 20\,\mathrm{MPa}$ |
| Cavitation and embolism (Definition 3.3.2) | Air seeding (pit membranes), freeze–thaw | Vulnerability curve, $P_{50}$; safety margin | $P_{50}$ from about $-1$ to $< -8\,\mathrm{MPa}$; 70% of tree species have a safety margin $< 1\,\mathrm{MPa}$ |
| Transpiration (Definition 3.4.1) | Water vapor concentration difference $\Delta w$ (increases exponentially with leaf temperature) | Stomatal and boundary-layer conductances in series | $E \sim 1$–$10\,\mathrm{mmol\,m^{-2}\,s^{-1}}$; cuticular transpiration about 5% |
| Transpiration ratio and WUE (Definition 3.4.2) | $A/E = c_{\mathrm{a}}(1 - c_{\mathrm{i}}/c_{\mathrm{a}})/(1.6\,\Delta w)$ | 50-fold concentration gradient, 1.6-fold slower diffusion, mesophyll resistance | TR: C3 about 400, C4 about 150, CAM about 50 |
| SPAC (Definition 3.5.1) | Ohm's law in the liquid phase; diffusion in the gas phase | Leaf about 30% of liquid-phase resistance; soil resistance dominates in drought | Predawn leaf water potential ≈ soil water potential |
| Rational irrigation (3.6) | Water requirement pattern and critical periods; soil, morphological and physiological indicators | — | Two critical periods in wheat: booting, and grain filling to milk stage |

The main equations of this chapter:

| No. | Equation | Use |
|---|---|---|
| (3.1) | $\Psi_{\mathrm{p}} = -2T/r$ | Negative pressure of menisci in soil, cell walls and pit membranes |
| (3.2) | $Q = \dfrac{\pi r^4}{8\eta}\dfrac{\Delta\Psi_{\mathrm{p}}}{\Delta x}$ | Bulk flow in the xylem |
| (3.3) | $\mathrm{PLC} = 100[1 - \mathrm{e}^{-(-\Psi_{\mathrm{x}}/b)^c}]$, $P_{50} = -b(\ln 2)^{1/c}$ | Vulnerability curve |
| (3.4) | $e_{\mathrm{s}} = 0.6108\,\mathrm{e}^{17.27t/(t + 237.3)}\,\mathrm{kPa}$ | Saturated vapor pressure |
| (3.5) | $E = g_{\mathrm{tw}}\Delta w$, $1/g_{\mathrm{tw}} = 1/g_{\mathrm{s}} + 1/g_{\mathrm{b}}$ | Transpiration rate |
| (3.6) | $A/E = c_{\mathrm{a}}(1 - c_{\mathrm{i}}/c_{\mathrm{a}})/(1.6\,\Delta w)$ | Water-use efficiency |
| (3.7) | $E = K_{\mathrm{plant}}(\Psi_{\mathrm{soil}} - \Psi_{\mathrm{leaf}} - \rho_{\mathrm{w}}gh)$ | Soil–plant–atmosphere continuum |

## Questions

1. A vessel has a radius of $25\,\mu\mathrm{m}$. (a) Find the pressure gradient required for water to flow in it at $1\,\mathrm{mm\,s^{-1}}$ (ideal tube, 20 °C); (b) if it is replaced by a tracheid of radius $10\,\mu\mathrm{m}$, by what factors do the mean flow velocity and the volume flow rate of a single element change under the same pressure gradient?

   **Answer** (a) From Eq. (3.2), $\Delta\Psi_{\mathrm{p}}/\Delta x = 8\eta\bar v/r^2 = 8 \times 10^{-3} \times 10^{-3}/(25\times10^{-6})^2 = 1.28\times10^4\,\mathrm{Pa\,m^{-1}} \approx 0.013\,\mathrm{MPa\,m^{-1}}$. (b) The mean velocity is proportional to $r^2$ and becomes $(10/25)^2 = 0.16$ times, that is, $0.16\,\mathrm{mm\,s^{-1}}$; the volume flow rate is proportional to $r^4$ and becomes $(0.4)^4 = 0.026$ times, about 1/39. In reality water in a tracheid must also flow through pits from one cell into the next, so the resistance is still greater.

2. On a summer noon, leaf temperature is 32 °C, air temperature 28 °C, relative humidity 40%, atmospheric pressure 100 kPa, $g_{\mathrm{s}} = 0.25$ and $g_{\mathrm{b}} = 0.8\,\mathrm{mol\,m^{-2}\,s^{-1}}$. Use Eqs. (3.4) and (3.5) to find the transpiration rate and the corresponding latent heat flux.

   **Answer** $e_{\mathrm{s}}(32\,^\circ\mathrm{C}) = 0.6108\exp(17.27 \times 32/269.3) = 0.6108 \times \mathrm{e}^{2.052} = 4.75\,\mathrm{kPa}$; $e_{\mathrm{s}}(28\,^\circ\mathrm{C}) = 0.6108\exp(17.27 \times 28/265.3) = 3.78\,\mathrm{kPa}$, and the actual water vapor pressure of the air is $0.4 \times 3.78 = 1.51\,\mathrm{kPa}$. $\Delta w = (4.75 - 1.51)/100 = 0.0324$. $g_{\mathrm{tw}} = 1/(4 + 1.25) = 0.190\,\mathrm{mol\,m^{-2}\,s^{-1}}$ and $E = 0.190 \times 0.0324 = 6.2\,\mathrm{mmol\,m^{-2}\,s^{-1}}$ (about $400\,\mathrm{g\,m^{-2}\,h^{-1}}$). $\lambda E = 6.2\times10^{-3} \times 43.5\times10^3 \approx 270\,\mathrm{W\,m^{-2}}$ (the heat of vaporization near 30 °C is about $43.5\,\mathrm{kJ\,mol^{-1}}$). The leaf being 4 °C warmer than the air makes the driving force about 40% larger than when leaf temperature equals air temperature ($\Delta w = 0.0227$).

3. The vulnerability curve of a shrub can be described by Eq. (3.3) with $b = 4.0\,\mathrm{MPa}$ and $c = 3$. (a) Find $P_{50}$; (b) if the xylem water potential falls to $-4.5\,\mathrm{MPa}$ in drought, how much conductivity is lost? (c) If the lowest xylem water potential in the field is $-2.8\,\mathrm{MPa}$, what is the hydraulic safety margin?

   **Answer** (a) $P_{50} = -4.0 \times (\ln 2)^{1/3} = -4.0 \times 0.885 = -3.54\,\mathrm{MPa}$. (b) $(4.5/4.0)^3 = 1.424$ and $\mathrm{PLC} = 100(1 - \mathrm{e}^{-1.424}) = 76\%$. (c) $\Psi_{\min} - P_{50} = -2.8 - (-3.54) = 0.74\,\mathrm{MPa}$, within the "narrow safety margin" range in which most tree species lie.

4. Use Eq. (3.6) to explain: (a) why the water-use efficiency of the same C3 plant is lower in dry air; (b) how water-use efficiency changes when atmospheric $\ce{CO2}$ concentration rises while $c_{\mathrm{i}}/c_{\mathrm{a}}$ remains roughly unchanged; (c) why closing some of the stomata can raise water-use efficiency yet often lowers yield.

   **Answer** (a) Dry air increases the water vapor mole fraction difference $\Delta w$ between inside and outside the leaf, the denominator becomes larger and $A/E$ falls: more water must be paid for each $\ce{CO2}$ assimilated. (b) When $c_{\mathrm{i}}/c_{\mathrm{a}}$ is constant, $A/E$ is proportional to $c_{\mathrm{a}}$, so elevated $\ce{CO2}$ raises water-use efficiency, as confirmed in the carbon isotope record of tree rings over past decades; in addition stomatal conductance often decreases as $\ce{CO2}$ rises. (c) Closing some stomata lowers $c_{\mathrm{i}}$ and increases $(1 - c_{\mathrm{i}}/c_{\mathrm{a}})$, so $A/E$ rises; but $A$ itself falls as $c_{\mathrm{i}}$ decreases, reducing carbon gain when water is ample, so there is a trade-off between high water-use efficiency and high yield, which is advantageous only in water-limited environments.

5. A student argues: "Root pressure can push water up, so water transport in tall trees depends mainly on root pressure." Refute this statement using the data in this chapter, and explain the actual role of root pressure in plants.

   **Answer** Root pressure is generally less than $0.1\,\mathrm{MPa}$ and at most about $0.2\,\mathrm{MPa}$, which can support a static water column of only about 10–20 m, whereas lifting water to the top of a 100-m tree and maintaining the transpiration stream requires about $2\,\mathrm{MPa}$ (about $1\,\mathrm{MPa}$ each for friction and gravity); moreover, root pressure appears only when transpiration is very weak, and when transpiration is vigorous the xylem is under tension and no positive pressure can be measured. Water transport in trees depends mainly on transpirational pull (the cohesion–tension mechanism). The actual roles of root pressure are: at night and in early spring (before trees leaf out) it causes water and solutes to rise, giving rise to guttation and bleeding; and positive pressure in the xylem can compress and dissolve gas bubbles and repair embolism caused by cavitation, which is exactly how lianas such as grape recover their conducting capacity in spring.
