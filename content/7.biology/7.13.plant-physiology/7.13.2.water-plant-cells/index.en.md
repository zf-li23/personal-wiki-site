---
title: Water and Plant Cells
description: The structure and properties of water; water potential and its solute, pressure, gravitational and matric components, the van 't Hoff relation and the osmotic coefficient; diffusion, bulk flow and osmosis; imbibition, pressure-driven and osmotic water uptake, and plasmolysis; Höfler diagrams, the volumetric elastic modulus and pressure–volume curves; membrane hydraulic conductivity and the half-time of cell water exchange; aquaporins and their gating; water flow between cells; methods for measuring water potential.
source_hash: 815735af95d5
---

Plants use far more water than animals do: about 97% of the water absorbed by roots is lost by evaporation from the leaves, only about 2% remains in the plant for growth, and about 1% takes part in photosynthesis and other metabolic reactions; for every $\ce{CO2}$ molecule it absorbs, a leaf loses several hundred water molecules. On the other hand, plant cells have a **cell wall** that allows a hydrostatic pressure of several atmospheres to build up inside, which makes the water relations of plant cells quite different from those of wall-less animal cells: growth, stomatal movement, phloem transport and the upright posture of non-woody tissues all depend on **turgor pressure**. This chapter answers, at the cellular scale, the question "why and how does water enter and leave plant cells?" We begin with the properties of water (2.1), then use **water potential** to describe the free energy of water in a unified way (2.2), followed by the three modes of water movement (2.3), water uptake and plasmolysis of cells (2.4), how the properties of the wall and membrane determine cell volume and the rate of water exchange (2.5), aquaporins (2.6), water flow between cells (2.7) and the measurement of water potential (2.8).

The thermodynamic definition of water potential and its typical values in the soil–plant–atmosphere continuum were given in biophysics ([7.6.3](/7.6.3#sec-3.1.4), [Definition 3.1.1](/7.6.3#def-3.1.1)), osmotic pressure arises from the mixing entropy of dilute solutions ([7.6.2](/7.6.2#sec-2.3.3)), and the behavior of animal cells as osmometers is described in [7.3.5](/7.3.5#sec-5.3); this chapter builds on these to present the quantitative relations specific to plant cells. Water uptake, transport and transpiration of whole plants are the subject of the next chapter, [7.13.3](/7.13.3), and the water relations of guard cells are treated in [7.13.10](/7.13.10).

## 2.1. Properties of Water and Water in the Plant

### 2.1.1. Water Content of Plants and the States of Water

The water content of plants is usually 70%–90% of fresh weight: it can exceed 90% in aquatic plants, is generally 70%–85% in herbaceous plants and somewhat lower in woody plants; rapidly growing young organs have more than senescent ones, air-dried seeds only about 10%, and lichens, mosses and resurrection plants living in alternately wet and dry environments can fall to 6% or even lower when dry.

According to how strongly it is associated with other substances, water in cells can be divided into two classes. Water that is tightly adsorbed on the hydrophilic surfaces of cell walls, protoplasmic colloids and biological macromolecules and cannot move freely is called *bound water*; water that lies farther from colloidal particles, can move freely and serves as solvent and reactant is called *free water*. Bound water has a low chemical potential, hardly takes part in metabolism, and does not readily freeze or evaporate. The ratio of free to bound water is therefore an indicator of the physiological state of the cell: when the ratio is high, metabolism is vigorous and growth is fast; when it is low, metabolism is weak but resistance to drought and cold is strong, as in overwintering plants and dormant seeds. This division is qualitative, and there is no sharp boundary between the two kinds of water; to describe the state of water quantitatively one uses the water potential of 2.2.

### 2.1.2. Structure and Properties of Water

In a water molecule oxygen is more electronegative than hydrogen, so the electrons of the two O–H bonds are displaced toward oxygen, giving the oxygen end a partial negative charge and the two hydrogens partial positive charges; the molecule is tetrahedral, with two corners occupied by hydrogens and the other two by the lone pairs of oxygen. Each water molecule can therefore form up to four **hydrogen bonds** with neighboring water molecules, which is the origin of the special properties of water ([7.1.2](/7.1.2)). The table lists those most relevant to plant physiology.

| Property | Value (20–25 °C) | Physiological significance |
|---|---|---|
| Polarity and dielectric constant | Relative permittivity $\varepsilon_{\mathrm{r}} \approx 78$ | A good solvent: dissolves ions, sugars, amino acids and proteins, and is the medium of metabolism and transport |
| Specific heat capacity | $4.18\,\mathrm{J\,g^{-1}\,K^{-1}}$ ($75.3\,\mathrm{J\,mol^{-1}\,K^{-1}}$) | Buffers fluctuations in tissue temperature |
| Heat of vaporization | $44\,\mathrm{kJ\,mol^{-1}}$ ($2.44\,\mathrm{kJ\,g^{-1}}$, 25 °C) | Carries away large amounts of heat in transpiration, cooling sunlit leaves ([7.13.3](/7.13.3)) |
| Surface tension | $0.0728\,\mathrm{N\,m^{-1}}$ | Menisci in cell walls and soil pores generate negative pressure, the source of the transpirational pull |
| Cohesion and adhesion | Contact angle: clean glass, primary wall about $0^\circ$ | **Capillarity**; keeps the water column continuous in the xylem |
| Tensile strength | Can withstand tensions exceeding $20\,\mathrm{MPa}$ in careful experiments | Water in the xylem can be transported under negative pressure |
| Viscosity | $1.0\,\mathrm{mPa\,s}$ (20 °C), about $1.5\,\mathrm{mPa\,s}$ at 5 °C | Determines the resistance to bulk flow; low temperature slows water uptake by roots |

**Surface tension** describes the energy required to increase the area of a gas–liquid interface (unit $\mathrm{J\,m^{-2} = N\,m^{-1}}$). A curved interface exerts a net force on the liquid perpendicular to the interface: a bubble of radius $r$ experiences an inward pressure $2T/r$, where $T$ is the surface tension; the same relation will give the negative pressure of water in soil and cell walls in [7.13.3](/7.13.3). Cohesion is the mutual attraction among water molecules and adhesion is the attraction between water and solid surfaces (cell walls, glass); both arise mainly from hydrogen bonds, and together with surface tension they produce capillary rise. In a wettable capillary of radius $r$, the water column rises to $h = 2T\cos\theta/(\rho_{\mathrm{w}} g r)$: a vessel with $r = 20\,\mu\mathrm{m}$ can lift water only about $0.74\,\mathrm{m}$, so capillary rise cannot explain water transport in trees; what actually operates are the much smaller menisci in the walls of mesophyll cells ([7.13.3](/7.13.3)).

### 2.1.3. The Roles of Water in Plant Life

1. Main component of protoplasm: water keeps protoplasm in the sol state and maintains the structure of membrane lipid bilayers and proteins; when the water content falls, protoplasm turns into a gel and metabolism weakens accordingly.
2. Reactant in metabolism: water is the electron donor in photosynthesis and takes part in hydrolysis reactions and in respiration.
3. Medium for uptake and transport of substances: minerals and organic compounds are dissolved in water and are transported through the xylem, the phloem and between cells.
4. Maintenance of cell turgor and of the natural posture of the plant: turgor spreads the leaves, holds up young stems, opens flowers and provides the driving force for cell expansion ([7.13.17](/7.13.17)).
5. Temperature regulation: the large specific heat and high heat of vaporization prevent plants from overheating in strong light.
6. Ecological role: the amount of water determines vegetation type and productivity, and a single species may form different ecotypes in dry and moist habitats.

## 2.2. Water Potential

### 2.2.1. The Concept of Water Potential

The movement of water in the plant is a free-energy problem. The **chemical potential** of a substance is the change in Gibbs free energy of a system per mole of that substance added at constant temperature, pressure and amounts of other components; its absolute value cannot be measured and can only be given relative to a standard state. The **water potential** customarily used in plant physiology is the difference between the chemical potential of water in the system and that of pure water at the same temperature, atmospheric pressure and height, divided by the **partial molar volume** of water $\bar V_{\mathrm{w}} = 18.0\times10^{-6}\,\mathrm{m^3\,mol^{-1}}$ ([Definition 3.1.1](/7.6.3#def-3.1.1)):

$$
\Psi_{\mathrm{w}} = \frac{\mu_{\mathrm{w}} - \mu_{\mathrm{w}}^\circ}{\bar V_{\mathrm{w}}}.
$$

The dimension of water potential is energy divided by volume, that is, pressure ($1\,\mathrm{J\,m^{-3}} = 1\,\mathrm{Pa}$), and it is usually expressed in MPa; the older literature often uses bar ($1\,\mathrm{bar} = 0.1\,\mathrm{MPa}$) and atmosphere ($1\,\mathrm{atm} = 0.1013\,\mathrm{MPa}$, so $1\,\mathrm{MPa} \approx 9.87\,\mathrm{atm}$). For comparison, the pressure in a car tire is about $0.2\,\mathrm{MPa}$, and the hydrostatic pressure $10\,\mathrm{m}$ under water is about $0.1\,\mathrm{MPa}$. The water potential of pure water is defined as zero; that of ordinary solutions and plant cells is negative. Water always moves spontaneously from higher to lower water potential, and at equilibrium the water potential is the same everywhere in the system.

### 2.2.2. Components of Water Potential

The free energy of water is affected by four factors, namely solutes, pressure, gravity and adsorption on solid surfaces, and the water potential is correspondingly decomposed into four components:

$$
\Psi_{\mathrm{w}} = \Psi_{\mathrm{s}} + \Psi_{\mathrm{p}} + \Psi_{\mathrm{g}} + \Psi_{\mathrm{m}}. \tag{2.1}
$$

**Definition 2.2.1 (Solute Potential)** The amount by which the water potential is lowered by the presence of solute particles is called the **solute potential**, also called the **osmotic potential**, denoted $\Psi_{\mathrm{s}}$. Solutes dilute the water and increase the mixing entropy of the system, thereby lowering the free energy of water; in dilute solutions this effect depends only on the number of solute particles and not on their kind. The solute potential is always negative, and that of pure water is zero.

For an ideal dilute solution, the solute potential is the negative of the **osmotic pressure** $\varPi$, given by the van 't Hoff relation:

$$
\Psi_{\mathrm{s}} = -\varPi = -c_{\mathrm{s}}RT, \qquad c_{\mathrm{s}} = i\,c, \tag{2.2}
$$

where $R = 8.314\,\mathrm{J\,mol^{-1}\,K^{-1}}$, $T$ is the thermodynamic temperature, $c_{\mathrm{s}}$ is the **osmolarity**, that is, the amount of all solute particles per unit volume of solution; $c$ is the solute concentration, and $i$ is the number of particles into which one solute molecule dissociates (the van 't Hoff factor: sucrose and glucose $i = 1$, $\ce{NaCl}$ $i = 2$, $\ce{CaCl2}$ $i = 3$). At 20 °C $RT = 2.437\,\mathrm{L\,MPa\,mol^{-1}}$, so each $1\,\mathrm{osmol\,L^{-1}}$ of osmolarity corresponds to $-2.44\,\mathrm{MPa}$. Eq. (2.2) is one of the **colligative properties** ([6.3.5](/6.3.5)); Chinese textbooks often call $c$ the "molality" while writing its unit as $\mathrm{mol\,L^{-1}}$, but strictly the quantity in the equation is the osmolarity; in dilute solutions the values per kilogram of water (osmol/kg) and per liter of solution (osmol/L) are almost the same, whereas in concentrated solutions the former should be used.

Real solutions deviate from ideality: electrostatic interactions among the ions of electrolytes and the specific binding of macromolecular solutes to water make the effective number of particles smaller or larger than $ic$. This deviation is corrected by the *osmotic coefficient* $\phi$, $\Psi_{\mathrm{s}} = -\phi\,i\,cRT$; for a $0.1\,\mathrm{mol\,L^{-1}}$ $\ce{NaCl}$ solution $\phi \approx 0.93$, equivalent to about 1.86 effective particles per $\ce{NaCl}$ (Chinese textbooks often write this as a "dissociation coefficient $i = 1.8$"); the number of effective particles for $\ce{CaCl2}$ is about 2.6, whereas $\phi > 1$ for $1\,\mathrm{mol\,L^{-1}}$ sucrose.

**Example 2.2.1 (Glucose and NaCl solutions)** At 20 °C, which has the lower solute potential, a $0.1\,\mathrm{mol\,L^{-1}}$ glucose solution or a $0.1\,\mathrm{mol\,L^{-1}}$ $\ce{NaCl}$ solution?

Glucose does not dissociate, so $c_{\mathrm{s}} = 0.1\,\mathrm{osmol\,L^{-1}}$ and $\Psi_{\mathrm{s}} = -0.1 \times 2.437 = -0.244\,\mathrm{MPa}$. $\ce{NaCl}$ dissociates into $\ce{Na+}$ and $\ce{Cl-}$; ideally $c_{\mathrm{s}} = 0.2\,\mathrm{osmol\,L^{-1}}$ and $\Psi_{\mathrm{s}} = -0.488\,\mathrm{MPa}$; allowing for $\phi = 0.93$ the actual value is about $-0.45\,\mathrm{MPa}$. The $\ce{NaCl}$ solution therefore has the lower solute potential, about 1.9 times that of a glucose solution of the same concentration.

**Definition 2.2.2 (Pressure Potential)** The amount by which the water potential is changed by the presence of hydrostatic pressure is called the **pressure potential**, denoted $\Psi_{\mathrm{p}}$. Its zero is atmospheric pressure: positive pressure raises the water potential and negative pressure (tension) lowers it.

When a vacuolated cell takes up water and swells, the protoplast presses against the cell wall, and the reaction of the wall generates a positive hydrostatic pressure inside the cell, the **turgor pressure**, so that $\Psi_{\mathrm{p}} > 0$; in well-watered plants the $\Psi_{\mathrm{p}}$ of cells lies between $0.1$ and $3\,\mathrm{MPa}$, depending on the solute potential of the cell. At incipient plasmolysis $\Psi_{\mathrm{p}} = 0$. In the xylem vessels of a transpiring plant the water is under tension and $\Psi_{\mathrm{p}}$ is negative; at night, when root pressure is pronounced, the $\Psi_{\mathrm{p}}$ of the xylem can also be positive ([7.13.3](/7.13.3)). When discussing the water potential difference between two open systems at the same atmospheric pressure, $\Psi_{\mathrm{p}}$ is zero for both and can be omitted.

The gravitational potential $\Psi_{\mathrm{g}} = \rho_{\mathrm{w}}gh$ depends on the height $h$ of the water above a reference level, with $\rho_{\mathrm{w}}g \approx 0.0098\,\mathrm{MPa\,m^{-1}}$: for every $10\,\mathrm{m}$ of rise the water potential increases by about $0.1\,\mathrm{MPa}$. At the cellular scale the height difference between neighboring cells is negligible; but in tall trees gravitational potential is one of the main obstacles that water transport must overcome ([7.13.3](/7.13.3)).

**Definition 2.2.3 (Matric Potential)** The amount by which the water potential is lowered by the adsorption of water on hydrophilic solid surfaces and fine pores (cellulose and pectin of the cell wall, proteins and starch grains in protoplasm, soil particles) and by capillary action is called the **matric potential**, denoted $\Psi_{\mathrm{m}}$. It is always negative or zero.

Adsorbed water is only one or two molecules thick, and adsorption is not easily separated into contributions to the solute and pressure potentials, so it is lumped into a single term. In cells that have formed a central vacuole the matric potential is close to zero and is usually neglected; in air-dried seeds, wood and meristematic cells that have not yet formed vacuoles, however, the water potential is determined mainly by the matric potential, and the $\Psi_{\mathrm{m}}$ of air-dried seeds can be as low as $-100\,\mathrm{MPa}$ or even lower, which is why their water-absorbing ability is so strong. In dry soil, too, the soil water potential is determined mainly by the matric potential ([7.13.3](/7.13.3)).

### 2.2.3. Water Potential of Different Systems

| System | Water potential | Remarks |
|---|---|---|
| Pure water (open container) | $\Psi_{\mathrm{w}} = 0$ | Reference state |
| Solution in an open container | $\Psi_{\mathrm{w}} = \Psi_{\mathrm{s}} < 0$ | $\Psi_{\mathrm{p}} = 0$; for $\Psi_{\mathrm{g}}$ the height of the solution is taken as the reference level |
| Mature vacuolated cell | $\Psi_{\mathrm{w}} = \Psi_{\mathrm{s}} + \Psi_{\mathrm{p}}$ | Cytoplasm and vacuole have the same water potential; matric potential negligible |
| Cell without vacuole, dry seed | $\Psi_{\mathrm{w}} \approx \Psi_{\mathrm{m}}$ | Imbibition (2.4.1) |
| Cell at incipient plasmolysis | $\Psi_{\mathrm{p}} = 0$, $\Psi_{\mathrm{w}} = \Psi_{\mathrm{s}}$ | Plasmolytic method for measuring $\Psi_{\mathrm{s}}$ (2.8) |
| Fully saturated cell | $\Psi_{\mathrm{w}} = 0$, $\Psi_{\mathrm{p}} = -\Psi_{\mathrm{s}}$ | Takes up no more water |
| Apoplast (cell walls, xylem sap) | $\Psi_{\mathrm{s}} \approx -0.1$–$0\,\mathrm{MPa}$ | Very dilute solution; can be more concentrated in developing fruits and saline habitats |
| Air | $\Psi = (RT/\bar V_{\mathrm{w}})\ln\mathrm{RH}$ | About $-94\,\mathrm{MPa}$ at 50% relative humidity ([7.6.3](/7.6.3#eq-3.7), [7.13.3](/7.13.3)) |

Typical values of the components: the leaf $\Psi_{\mathrm{w}}$ of well-watered herbaceous plants is $-0.2$ to $-1.0\,\mathrm{MPa}$, that of trees and shrubs can reach $-2.5\,\mathrm{MPa}$, and that of plants of extremely arid regions can be below $-10\,\mathrm{MPa}$. The $\Psi_{\mathrm{s}}$ of cells of well-watered horticultural plants such as lettuce, cucumber seedlings and bean leaves can be as high as $-0.5\,\mathrm{MPa}$, with $-0.8$ to $-1.2\,\mathrm{MPa}$ more common; woody plants have lower $\Psi_{\mathrm{s}}$, which lets them maintain turgor even at very low midday water potentials. The cells of **halophytes** have very low $\Psi_{\mathrm{s}}$ and can take up water from saline water; in drought many plants accumulate solutes in their cells and lower $\Psi_{\mathrm{s}}$ to maintain turgor, which is **osmotic adjustment** ([7.13.27](/7.13.27)).

Water deficit first inhibits cell expansion: as soon as the water potential falls to $-0.2$ to $-0.4\,\mathrm{MPa}$, leaf expansion slows markedly, followed in turn by cell wall and protein synthesis, stomatal conductance and photosynthesis, while **abscisic acid** and compatible solutes begin to accumulate. In many plants water shortage inhibits shoot growth but promotes root elongation; this is an adaptation rather than mere injury: the root-to-shoot ratio increases and the water-absorbing capacity is relatively enhanced.

## 2.3. Modes of Water Movement

Water moves in the plant in three ways, which differ in driving force and in the scale to which they apply.

*Diffusion* is the net movement of a substance from a region of high concentration to one of low concentration resulting from the random thermal motion of molecules, and it obeys **Fick's law** ([2.5.1](/2.5.1)): the flux density is $J_{\mathrm{s}} = -D_{\mathrm{s}}\,\mathrm{d}c_{\mathrm{s}}/\mathrm{d}x$, where $D_{\mathrm{s}}$ is the **diffusion coefficient**. The time required for diffusion grows with the square of the distance, $t \sim L^2/D_{\mathrm{s}}$: for glucose in water $D \approx 10^{-9}\,\mathrm{m^2\,s^{-1}}$, so diffusing across a cell $50\,\mu\mathrm{m}$ in diameter takes about $2.5\,\mathrm{s}$, whereas diffusing $1\,\mathrm{m}$ takes about 32 years. Diffusion is therefore effective only at the cellular scale; the diffusion coefficient in the gas phase is about ten thousand times that in the liquid phase, and the exchange of water vapor and $\ce{CO2}$ between the inside and outside of the leaf is accomplished by diffusion ([7.13.3](/7.13.3)).

*Bulk flow* is the collective directional flow of groups of molecules in a liquid driven by a pressure gradient (also called mass flow), independent of the solute concentration gradient (as long as changes in viscosity can be neglected). The ascent of water in vessels, its transport in sieve tubes, and its flow in soil and cell walls are all bulk flow. Laminar flow in a tube obeys the **Hagen–Poiseuille law**, in which the flow rate is proportional to the fourth power of the tube radius ([7.12.5](/7.12.5), [7.13.3](/7.13.3)), so bulk flow suits long-distance transport.

**Osmosis** is the diffusion of water through a selectively permeable membrane. The membrane lets water and some small uncharged molecules pass but blocks solutes, so the difference in the chemical potential of water on the two sides of the membrane drives water toward the side of higher solute concentration (lower water potential). An ideal **semipermeable membrane** lets only the solvent through; biological membranes have different permeabilities for different solutes, described by the **reflection coefficient** $\sigma$ ($\sigma = 1$ for complete exclusion, $\sigma = 0$ for passage as freely as water; for small solutes the cell wall has $\sigma \approx 0$). According to the **Kedem–Katchalsky equations** of nonequilibrium thermodynamics ([6.3.18](/6.3.18)), the volume flux across a membrane is

$$
J_V = L_p\,(\Delta\Psi_{\mathrm{p}} + \sigma\,\Delta\Psi_{\mathrm{s}}), \tag{2.3}
$$

where $\Delta$ denotes outside minus inside and $L_p$ is the hydraulic conductivity of the membrane (2.5.3). For a solute with $\sigma = 1$ the bracket is just the water potential difference $\Delta\Psi_{\mathrm{w}}$; for a solute that can partly cross the membrane only $\sigma$ times its solute potential is effective, so in measuring the solute potential of cells by osmosis one should choose solutes that can hardly cross the membrane (sucrose, mannitol, polyethylene glycol).

| Mode | Driving force | Medium and scale | Examples in plants |
|---|---|---|---|
| Diffusion | Concentration (chemical potential) gradient | Short distances; much faster in the gas phase | Exchange of water vapor and $\ce{CO2}$ within the leaf, movement of substances within cells |
| Bulk flow | Pressure gradient $\Delta\Psi_{\mathrm{p}}$ | Long distances; resistance inversely proportional to the fourth power of tube diameter | Water flow in xylem, phloem, soil and cell walls |
| Osmosis | Transmembrane water potential difference $\Delta\Psi_{\mathrm{w}}$ | Across selectively permeable membranes | Water uptake and loss of cells, water crossing the endodermis in roots |

## 2.4. Water Uptake by Cells

### 2.4.1. Three Modes of Water Uptake

The driving force of water uptake by cells is always a water potential difference, and according to the water potential component that plays the dominant role three modes can be distinguished.

| Mode | Component involved | Conditions | Examples |
|---|---|---|---|
| Imbibition | Matric potential $\Psi_{\mathrm{m}}$ | Hydrophilic colloids present, no central vacuole yet | Water uptake of air-dried seeds before germination, meristematic cells |
| Osmotic uptake | Solute potential $\Psi_{\mathrm{s}}$ | Central vacuole present, the protoplasmic layer acts as a selectively permeable membrane | The main mode of water uptake and loss of mature cells |
| Pressure-driven uptake | Pressure potential $\Psi_{\mathrm{p}}$ | Pressure in the cell or vessel is reduced | Water uptake caused by negative pressure in vessels during transpiration; water uptake by growing cells when wall loosening lowers turgor |

The swelling of hydrophilic colloids upon taking up water is called *imbibition*. Among substances, proteins have the greatest capacity for imbibition, starch next, cellulose less, and lipids hardly swell at all, so protein-rich legume seeds swell more than starch-rich cereal grains. At the beginning of imbibition many water molecules are adsorbed on hydrophilic surfaces and heat is released (heat of wetting); as water is taken up the matric potential rises rapidly, from below $-100\,\mathrm{MPa}$ in the dry seed to near zero, and the membrane lipid bilayers return from the gel state of the dry condition to the liquid-crystalline state. This is the first phase of **seed germination** ([7.13.20](/7.13.20)).

### 2.4.2. Osmotic Uptake and Plasmolysis

A cell with a central vacuole and its environment form an osmotic system: the plasma membrane, cytoplasm and tonoplast together are called the protoplasmic layer and act as a selectively permeable membrane, the cell sap in the vacuole is a solution of relatively high concentration, and the cell wall is almost completely permeable to water and solutes. The cell takes up water when its water potential is lower than that of the environment and loses water when it is higher.

**Definition 2.4.1 (Plasmolysis)** When a vacuolated plant cell is placed in a solution whose water potential is lower than that of its cell sap (a hypertonic solution), the vacuole loses water and shrinks, and because the cell wall is hardly extensible the protoplast shrinks away from the wall; this phenomenon is called **plasmolysis**. The stage at which the protoplast has just begun to separate from the cell wall is called incipient plasmolysis, when $\Psi_{\mathrm{p}} = 0$ and $\Psi_{\mathrm{w}} = \Psi_{\mathrm{s}}$. When a plasmolyzed cell is returned to a solution of higher water potential or to pure water, the vacuole takes up water and swells, and the protoplast gradually regains its original form; this is called deplasmolysis.

Plasmolysis can occur because solutes can enter the space between wall and protoplast through the large pores of the wall, so that the whole water potential difference falls across the plasma membrane and the protoplast shrinks independently of the wall. When a cell loses water in air the situation is different: there is no solution between wall and protoplast to fill the gap, the wall collapses inward and deforms together with the protoplast, so no plasmolysis occurs and $\Psi_{\mathrm{p}}$ can be negative. Under field conditions the soil solution is very dilute and the osmotic adjustment of plant cells also prevents plasmolysis; plasmolysis is mainly an experimental phenomenon. Its significance is that (1) it shows that the protoplasmic layer is a selectively permeable membrane; (2) it can be used to judge whether a cell is alive (dead cells with damaged membranes do not plasmolyze); (3) it allows the solute potential of cells to be measured (2.8); and (4) the speed of deplasmolysis allows the ease with which substances cross the protoplasmic layer to be compared.

**Example 2.4.1 (Equilibrium of a cell in solution)** At 20 °C, a cell without turgor ($\Psi_{\mathrm{p}} = 0$) with an osmolarity of $0.3\,\mathrm{osmol\,L^{-1}}$ is placed in a large volume of $0.1\,\mathrm{mol\,L^{-1}}$ sucrose solution, and at equilibrium the cell volume has increased by 15%. Find the water potential components of the cell at equilibrium; then transfer the cell to a $0.3\,\mathrm{mol\,L^{-1}}$ sucrose solution and find the result.

Initially the cell has $\Psi_{\mathrm{w}} = \Psi_{\mathrm{s}} = -0.3 \times 2.437 = -0.732\,\mathrm{MPa}$, lower than the $-0.244\,\mathrm{MPa}$ of the solution, so water enters the cell. The amount of solution is large and its water potential does not change, so at equilibrium the cell has $\Psi_{\mathrm{w}} = -0.244\,\mathrm{MPa}$. The amount of solute is unchanged and the volume has increased by 15%, so $\Psi_{\mathrm{s}} = -0.732/1.15 = -0.636\,\mathrm{MPa}$, and therefore $\Psi_{\mathrm{p}} = \Psi_{\mathrm{w}} - \Psi_{\mathrm{s}} = 0.392\,\mathrm{MPa}$. After transfer to $0.3\,\mathrm{mol\,L^{-1}}$ sucrose ($-0.732\,\mathrm{MPa}$), water flows out of the cell and the volume shrinks to the original turgor-free volume, with $\Psi_{\mathrm{s}} = -0.636 \times 1.15 = -0.732\,\mathrm{MPa}$ and $\Psi_{\mathrm{p}} = 0$, so the cell is exactly at incipient plasmolysis; in a somewhat more concentrated solution plasmolysis would occur. If instead of changing the solution one slowly squeezes the cell between two plates and expels half of its water, at equilibrium $\Psi_{\mathrm{w}}$ is still $-0.244\,\mathrm{MPa}$, but $\Psi_{\mathrm{s}}$ doubles to $-1.272\,\mathrm{MPa}$ and $\Psi_{\mathrm{p}}$ rises to $1.028\,\mathrm{MPa}$: the same water potential can be composed of completely different components.

### 2.4.3. Water Cannot Be Pumped Actively

The examples above all show that the movement of water across membranes is passive: water moves only down a water potential gradient, and there is no known "water pump" that directly consumes ATP to pump water across a membrane against a water potential gradient. The only exception is the coupled transport of water and solutes: **symporters** for some sugars and amino acids can carry along up to about 260 water molecules for each solute molecule transported, the decrease in the free energy of the solute compensating for the increase in that of water so that the overall free energy change is still negative; but the amount of water transported in this way is small compared with the passive water flow down the water potential gradient. Plants control water not by pumping it but by changing the solute concentration (and hence $\Psi_{\mathrm{s}}$), the properties of the cell wall ($\Psi_{\mathrm{p}}$) and the hydraulic conductivity of membranes.

## 2.5. Cell Wall, Membrane and Cell Volume

### 2.5.1. The Höfler Diagram and the Volumetric Elastic Modulus

When a cell takes up or loses water, the three water potential components change together with the cell volume. Because the amount of solute is constant, the solute potential is inversely proportional to the volume (the **Boyle–van 't Hoff relation**, [7.3.5](/7.3.5#sec-5.3.1)); the turgor pressure is determined by the elasticity of the cell wall.

**Definition 2.5.1 (Volumetric Elastic Modulus)** The ratio of the change in cell turgor to the relative volume change that causes it is called the **volumetric elastic modulus** of the cell:

$$
\varepsilon = \frac{\mathrm{d}\Psi_{\mathrm{p}}}{\mathrm{d}V/V} \approx \frac{\Delta\Psi_{\mathrm{p}}}{\Delta V/V}. \tag{2.4}
$$

A cell wall with a large $\varepsilon$ is rigid, and the same volume change causes a large change in turgor; a wall with a small $\varepsilon$ is elastic.

The $\varepsilon$ of plant cells is usually between $1$ and $50\,\mathrm{MPa}$ and increases with turgor (the wall stiffens as it is stretched). Taking the protoplast volume at incipient plasmolysis $V_{\mathrm{ip}}$ as the reference, using the relative volume $v = V/V_{\mathrm{ip}}$ and treating $\varepsilon$ as constant, we obtain a two-parameter model:

$$
\Psi_{\mathrm{s}} = \frac{\Psi_{\mathrm{s,ip}}}{v}, \qquad
\Psi_{\mathrm{p}} = \begin{cases} \varepsilon\,(v - 1), & v \ge 1, \\ 0, & v < 1\ \text{(plasmolyzed in solution)}, \end{cases} \qquad
\Psi_{\mathrm{w}} = \Psi_{\mathrm{s}} + \Psi_{\mathrm{p}}. \tag{2.5}
$$

Plotting the three components on one graph with volume as abscissa gives the Höfler diagram (Höfler, 1920):

![Höfler diagram (numerical model, Eq. (2.5)). The abscissa is the ratio of protoplast volume to the volume at incipient plasmolysis. A: the solute potential at incipient plasmolysis is taken as $-1.0\,\mathrm{MPa}$ and $\varepsilon = 7\,\mathrm{MPa}$. The gray region on the left is the plasmolyzed state of a cell in a hypertonic solution, in which the pressure potential is zero and the water potential equals the solute potential; as the volume increases the solute is diluted and the solute potential rises slowly (purple), while the pressure potential increases linearly with volume (green), their sum being the water potential (blue). With a volume increase of only about 13%, the water potential rises from the point of incipient plasmolysis ($\Psi_{\mathrm{w}} = \Psi_{\mathrm{s}}$) to the point of full turgor ($\Psi_{\mathrm{w}} = 0$, $\Psi_{\mathrm{p}} = -\Psi_{\mathrm{s}}$). B: change of water potential with volume for three wall stiffnesses: a rigid wall with $\varepsilon = 20\,\mathrm{MPa}$ traverses the same range of water potential with a volume change of only about 5%, whereas an elastic wall with $\varepsilon = 3\,\mathrm{MPa}$ requires about 26%](./plots/hofler.py)

The Höfler diagram summarizes five states of a mature cell: (a) at incipient plasmolysis $\Psi_{\mathrm{p}} = 0$ and $\Psi_{\mathrm{w}} = \Psi_{\mathrm{s}}$; (b) placed in a solution of higher water potential or in pure water, the cell takes up water and its volume increases, and $\Psi_{\mathrm{w}}$, $\Psi_{\mathrm{s}}$ and $\Psi_{\mathrm{p}}$ all rise; (c) placed in a solution of lower water potential, all three fall; (d) at full turgor $\Psi_{\mathrm{p}} = -\Psi_{\mathrm{s}}$ and $\Psi_{\mathrm{w}} = 0$, and the cell takes up no more water; (e) when a cell loses too much water in air, the wall collapses inward and $\Psi_{\mathrm{p}} < 0$, so that $\Psi_{\mathrm{w}} < \Psi_{\mathrm{s}}$.

Because the cell wall is rigid, as long as $\Psi_{\mathrm{p}} > 0$ large changes in water potential are accompanied by only small changes in volume: in most cells turgor falls to zero when the relative volume has decreased by 10%–15%, and the change in water potential is carried mainly by turgor. This keeps the volume of plant cells relatively stable during daily transpirational water loss. The stem of a cactus is a counterexample: the outer layer is photosynthetic parenchyma and the interior is water-storage tissue; the storage cells are larger and thinner-walled (smaller $\varepsilon$), and in drought their solute concentration also falls as soluble sugars are polymerized to starch, so that although the water potentials of the two cell types remain in equilibrium, the water lost comes mainly from the storage cells and the water status of the photosynthetic tissue is maintained.

### 2.5.2. Pressure–Volume Curves

At the tissue level the counterpart of the Höfler diagram is the *pressure–volume curve*, which is measured with a pressure chamber (2.8): a detached leaf is allowed to lose water gradually in air, and is repeatedly weighed and its water potential measured. Let the relative water content of the leaf be $R$ ($R = 1$ at full turgor), of which a fraction $a$ is apoplastic water that does not take part in osmosis, so that the relative water content of the symplast is $R_{\mathrm{s}} = (R - a)/(1 - a)$; let the solute potential at full turgor be $\pi_0$; below the turgor loss point $\Psi_{\mathrm{p}} = 0$, and therefore

$$
\frac{1}{-\Psi_{\mathrm{w}}} = \frac{R_{\mathrm{s}}}{-\pi_0} = \frac{1}{-\pi_0}\Bigl(1 - \frac{1 - R}{1 - a}\Bigr). \tag{2.6}
$$

Plotting $1/(-\Psi_{\mathrm{w}})$ against the water loss $1 - R$ (the Tyree–Hammel plot), the points below the turgor loss point fall on a straight line: the intercept of the line extrapolated to $1 - R = 0$ gives $-1/\pi_0$, and its intersection with the abscissa gives the fraction of symplastic water $1 - a$; the point where the curve departs from the line is the *turgor loss point*, and the volumetric elastic modulus of the tissue can also be obtained from the curve above the turgor loss point.

![Pressure–volume curve (numerical model; $\pi_0 = -1.2\,\mathrm{MPa}$, apoplastic water fraction $a = 0.15$, symplast volumetric elastic modulus $12\,\mathrm{MPa}$). A: change of the water potential components with relative water content as the leaf loses water (the abscissa runs from right to left with water loss): at the start of water loss the water potential falls steeply, almost entirely because of the decline in turgor (green), while the solute potential (purple) changes little; turgor is lost (dashed line) when the relative water content has fallen to about 0.91, after which the entire decline in water potential comes from the concentration of solutes. B: Tyree–Hammel plot: simulated measurements (blue points) fall on a straight line below the turgor loss point (triangle, $\Psi = -1.33\,\mathrm{MPa}$), whose extrapolation to the ordinate gives $-1/\pi_0$ (square) and which meets the abscissa at $1 - a = 0.85$](./plots/pressure-volume.py)

The water potential at the turgor loss point, $\Psi_{\mathrm{tlp}}$, is a composite index of leaf drought tolerance: the lower $\Psi_{\mathrm{tlp}}$, the drier the conditions under which the leaf can still maintain turgor, stomatal opening and growth. A synthesis across several hundred species worldwide showed that plants of arid habitats have lower $\Psi_{\mathrm{tlp}}$, and that $\Psi_{\mathrm{tlp}}$ is lowered mainly by lowering the solute potential at full turgor $\pi_0$ (that is, by accumulating solutes) rather than by changing the elasticity of the cell wall (Bartlett et al., 2012).

### 2.5.3. Membrane Hydraulic Conductivity and the Half-Time of Water Exchange

When the water potentials inside and outside a cell are unequal, the rate at which water flows across the membrane is proportional to the driving force:

$$
J_V = L_p\,\Delta\Psi_{\mathrm{w}}, \tag{2.7}
$$

where $J_V$ is the volume flux density ($\mathrm{m^3\,m^{-2}\,s^{-1} = m\,s^{-1}}$) and the proportionality coefficient is the *hydraulic conductivity* $L_p$ of the membrane, with unit $\mathrm{m\,s^{-1}\,MPa^{-1}}$, which describes how easily water crosses the membrane. For example, with $L_p = 10^{-6}\,\mathrm{m\,s^{-1}\,MPa^{-1}}$ and $\Delta\Psi_{\mathrm{w}} = 0.2\,\mathrm{MPa}$ the initial $J_V = 0.2\,\mu\mathrm{m\,s^{-1}}$. The literature also often uses the osmotic water permeability coefficient $P_{\mathrm{f}}$ ($\mathrm{m\,s^{-1}}$), related to $L_p$ by $L_p = P_{\mathrm{f}}\bar V_{\mathrm{w}}/(RT)$: at 20 °C, $P_{\mathrm{f}} = 100\,\mu\mathrm{m\,s^{-1}}$ corresponds to $L_p \approx 7\times10^{-7}\,\mathrm{m\,s^{-1}\,MPa^{-1}}$.

As water enters the cell, the water potential difference between inside and outside shrinks and the flow slows. Let the cell volume be $V$ and the surface area $A$, and let the water potential of the external solution $\Psi_{\mathrm{o}}$ remain constant; then $\mathrm{d}V/\mathrm{d}t = A\,L_p(\Psi_{\mathrm{o}} - \Psi_{\mathrm{w}})$. From Eq. (2.4) and the Boyle–van 't Hoff relation, the change in water potential caused by a small change in volume is $\mathrm{d}\Psi_{\mathrm{w}} = \mathrm{d}\Psi_{\mathrm{p}} + \mathrm{d}\Psi_{\mathrm{s}} = (\varepsilon - \Psi_{\mathrm{s}})\,\mathrm{d}V/V$; substituting gives a first-order linear equation whose solution is an exponential relaxation:

$$
\Psi_{\mathrm{w}}(t) = \Psi_{\mathrm{o}} + (\Psi_{\mathrm{w}}(0) - \Psi_{\mathrm{o}})\,\mathrm{e}^{-t/\tau}, \qquad
t_{1/2} = 0.693\,\tau = \frac{0.693\,V}{A\,L_p\,(\varepsilon - \Psi_{\mathrm{s}})}. \tag{2.8}
$$

A short half-time means rapid equilibration: cells with a large surface-to-volume ratio, a membrane of high hydraulic conductivity and a rigid wall (large $\varepsilon$) quickly reach water potential equilibrium with the environment. The half-time of a single cell is usually 1–10 s, and some are shorter, so a single cell equilibrates with its surroundings in less than 1 min; in multicellular tissue water must cross many cells in succession and the half-time can be much longer.

![Water potential relaxation of a single cell (Eq. (2.8)). Cylindrical cell of radius $20\,\mu\mathrm{m}$ and length $100\,\mu\mathrm{m}$ ($V/A = 8.3\,\mu\mathrm{m}$), $\varepsilon = 10\,\mathrm{MPa}$, $\Psi_{\mathrm{s}} = -0.8\,\mathrm{MPa}$; a cell with water potential $-0.2\,\mathrm{MPa}$ is transferred to pure water at $t = 0$. A: the cell water potential approaches zero exponentially: with open aquaporins ($L_p = 2\times10^{-6}\,\mathrm{m\,s^{-1}\,MPa^{-1}}$, blue) the half-time is about $0.27\,\mathrm{s}$, and with closed aquaporins ($L_p$ ten times smaller, red) about $2.7\,\mathrm{s}$. B: the volume flux into the cell $J_V = L_p\,\Delta\Psi$ is greatest at the start and decays as the water potential difference shrinks; the areas under the two curves (the total water entering the cell) are equal: aquaporins change only the rate, not the final state](./plots/water-relaxation.py)

## 2.6. Aquaporins

For a long time it was unclear whether water crosses the lipid bilayer of membranes solely by diffusion or also through channels made of protein; some experiments showed that the lipid bilayer alone could not account for the observed flow rates, but the evidence for channels was not conclusive. In 1991–1992 Peter Agre and colleagues discovered the first **aquaporin**, CHIP28 (AQP1), in the erythrocyte membrane and showed in *Xenopus* oocytes that it is a water channel ([7.1.13](/7.1.13#sec-13.6.1)); the first plant aquaporin (the tonoplast γ-TIP) was identified in 1993. Aquaporins are integral membrane proteins of 25–30 kDa; each monomer has six transmembrane helices, and two conserved NPA (Asn–Pro–Ala) motifs meet in the middle of the membrane to form a narrow pore through which water molecules pass in single file; four monomers form a tetramer, each monomer having its own pore.

Aquaporins increase the rate of water transport across membranes, but they do not change its direction, which is determined by the water potential difference, and they do not supply the driving force.

Plants have many more kinds of aquaporins than animals: *Arabidopsis* has 35 aquaporin genes, belonging to four subfamilies.

| Subfamily | Number of *Arabidopsis* genes | Main location | Substances permeated (besides water; some members) |
|---|---|---|---|
| PIP (plasma membrane intrinsic proteins), divided into PIP1 and PIP2 | 13 | Plasma membrane | $\ce{CO2}$, $\ce{H2O2}$ |
| TIP (tonoplast intrinsic proteins) | 10 | Tonoplast | $\ce{NH3}$, urea, $\ce{H2O2}$ |
| NIP (nodulin-26-like intrinsic proteins) | 9 | Plasma membrane, peribacteroid membrane | Glycerol, boric acid, silicic acid, arsenite |
| SIP (small basic intrinsic proteins) | 3 | Endoplasmic reticulum | — |

NIP members are of special significance for mineral nutrition: the silicon uptake transporter Lsi1 of rice and the boron uptake transporter NIP5;1 of *Arabidopsis* both belong to this subfamily ([7.13.4](/7.13.4)); arsenite also enters rice roots through the silicon channel, which is one reason why rice grain accumulates arsenic.

The activity of aquaporins is regulated at several levels, allowing plants to adjust the hydraulic conductivity of membranes:

- Gating: the pore of PIPs can switch between open and closed. Phosphorylation of serines on the cytosolic loop favors the open state; dephosphorylation, protonation of a conserved histidine on loop D caused by lowering of the cytosolic pH, and the binding of $\ce{Ca^2+}$ all cause loop D to fold over the pore mouth and close it. Under waterlogging and hypoxia the cytosol of root cells acidifies, PIPs close, and the hydraulic conductivity of the root falls sharply, which explains a long-puzzling phenomenon: flooded plants wilt.
- Expression: expression is high in growing organs, root tips, and the endodermis and exodermis of the root where water flow is concentrated; expression has a diurnal rhythm, being high during the day when transpiration is vigorous and low at night; drought, salt, temperature, nutrients and hormones (such as **abscisic acid**) all alter it.
- Trafficking: recycling of membrane proteins between the plasma membrane and endomembranes changes their abundance in the plasma membrane.

Functional evidence comes from mutants and transgenic plants: *Arabidopsis* loss-of-function mutants such as *pip2;2* and *pip1;2* have reduced root hydraulic conductivity; downregulating aquaporin expression markedly lowers root hydraulic conductivity, so that plants wilt easily or compensate with a larger root system. Cells that must change volume rapidly are rich in aquaporins, for example the motor cells of the pulvinus of *Mimosa* ([7.13.19](/7.13.19)).

![Two pathways for water across the plant plasma membrane and gating of aquaporins (schematic; the apoplast, of higher water potential, is at the top and the cytoplasm at the bottom). Left: a few water molecules diffuse directly across the lipid bilayer, slowly. Middle: an open plasma membrane aquaporin (PIP; two subunits of the tetramer are drawn), in which water molecules pass rapidly in single file through the pore of each subunit, the NPA selectivity filter in the middle of the pore excluding ions and protons; phosphorylation (P) of a serine on the cytosolic side favors opening. Right: a closed aquaporin: dephosphorylation, protonation of a histidine on loop D ($\mathrm{H}^+$) upon cytosolic acidification, and binding of $\ce{Ca^2+}$ cause loop D (red) to cover the pore mouth, so that water can hardly pass. Whether open or closed, the direction of water flow is determined by the water potential difference across the membrane](./plots/aquaporin.py)

## 2.7. Water Movement Between Cells

The direction of water movement between two adjacent cells depends on the difference in their water potentials: water always flows from the cell of higher water potential to that of lower water potential until the difference is zero. To judge the direction one must compare total water potentials, not just solute potentials or turgor pressures.

**Example 2.7.1 (Two adjacent cells)** Cell A has $\Psi_{\mathrm{s}} = -1.5\,\mathrm{MPa}$ and $\Psi_{\mathrm{p}} = 0.7\,\mathrm{MPa}$; the adjacent cell B has $\Psi_{\mathrm{s}} = -1.2\,\mathrm{MPa}$ and $\Psi_{\mathrm{p}} = 0.6\,\mathrm{MPa}$. In which direction does water flow?

$\Psi_{\mathrm{w,A}} = -1.5 + 0.7 = -0.8\,\mathrm{MPa}$ and $\Psi_{\mathrm{w,B}} = -1.2 + 0.6 = -0.6\,\mathrm{MPa}$. B has the higher water potential, so water flows from B to A; after A takes up water its $\Psi_{\mathrm{p}}$ rises and $\Psi_{\mathrm{s}}$ rises slightly, and the opposite happens in B, until $\Delta\Psi_{\mathrm{w}} = 0$. Note that A has higher turgor than B, yet water flows to A: high turgor does not mean high water potential.

:::

The same holds for several cells in a row. If the water potential in a xylem vessel is $-0.1\,\mathrm{MPa}$ (for example $\Psi_{\mathrm{s}} = -0.05$ and $\Psi_{\mathrm{p}} = -0.05\,\mathrm{MPa}$), and three mesophyll cells lined up beside it have $\Psi_{\mathrm{s}}$ of $-0.5$, $-0.4$ and $-0.5\,\mathrm{MPa}$ and $\Psi_{\mathrm{p}}$ of $0.3$, $0.1$ and $0.1\,\mathrm{MPa}$, their water potentials are in turn $-0.2$, $-0.3$ and $-0.4\,\mathrm{MPa}$, and water flows along this declining gradient from the vessel to the farthest cell. The same principle extends between organs and to the whole plant: from the soil through root, stem and leaf to the atmosphere the water potential declines step by step, and water moves along this continuous gradient ([7.13.3](/7.13.3)).

In tissues, water has three parallel pathways between cells: the **apoplast** pathway through cell walls and intercellular spaces, the **symplast** pathway through **plasmodesmata**, and the transmembrane pathway, in which water crosses the plasma membrane twice (and possibly the tonoplast) for every cell traversed. The last two are together called the cell-to-cell pathway, and pressure probes can hardly separate them. Which pathway dominates depends on their respective resistances, as will be discussed under water uptake by roots ([7.13.3](/7.13.3)).

## 2.8. Measuring Water Potential

The concept of water potential has two uses: to judge the direction of water movement and to gauge the water status of plants. Methods of measurement can be divided into several classes according to the quantity measured, and all of their principles derive from the definitions of 2.2.

| Method | Quantity measured | Principle | Characteristics |
|---|---|---|---|
| Chardakov (dye-drop) method | $\Psi_{\mathrm{w}}$ of tissue | The tissue exchanges water with a series of sucrose solutions, and the concentration at which the solution density is unchanged by the exchange is found | Simple, suited to teaching; measures the original water potential of the tissue |
| Plasmolytic method | $\Psi_{\mathrm{s}}$ of cells | The solution that just causes incipient plasmolysis has a water potential equal to the solute potential of the cell at incipient plasmolysis | Gives $\Psi_{\mathrm{s}}$ at $\Psi_{\mathrm{p}} = 0$, which is lower than the original water potential of the tissue |
| Dew-point and psychrometric methods | $\Psi_{\mathrm{w}}$ of tissue or solution | The sample equilibrates with the air in a small closed chamber, and the relative humidity of the air is measured | Accurate but slow; requires extremely high temperature resolution |
| Pressure chamber | $\Psi_{\mathrm{w}}$ of leaves and twigs | Pressure is applied to a detached leaf, and the pressure required to just return xylem sap to the cut surface is measured | Fast, usable in the field |
| Freezing-point depression | $\Psi_{\mathrm{s}}$ of sap | Solutes lower the freezing point in proportion to the osmolarity | Requires extraction of cell sap |
| Pressure probe | $\Psi_{\mathrm{p}}$, $\varepsilon$ and $L_p$ of single cells | A capillary is inserted into the cell, and the pressure needed to balance the cell sap is measured | The only method that measures the turgor of a single cell directly |

In the Chardakov method, leaf discs are cut with a cork borer and placed in a series of sucrose solutions of increasing concentration; after about 30 min a little methylene blue is added to each tube to color the solution, a fine pipette is used to take up some colored solution and release a small drop gently into the middle of the sucrose solution of the corresponding original concentration, and the movement of the blue drop is observed. When the tissue has a lower water potential than the solution, the tissue takes up water, the solution becomes more concentrated, and the blue drop, being denser, sinks; when the tissue has a higher water potential than the solution, the tissue loses water, the solution becomes more dilute, and the drop rises; at the concentration at which the drop stays motionless, the water potential of the solution equals that of the tissue. Because the amount of solution is far greater than that of the tissue, the water potential of the tissue is measured near its original state, so the value from the Chardakov method is higher than that from the plasmolytic method.

The dew-point and psychrometric methods seal the sample in a small thermostatted chamber in which the water of the sample equilibrates with the chamber air; the water potential of the air then equals that of the sample, and the water potential of air is determined by the relative humidity, $\Psi = (RT/\bar V_{\mathrm{w}})\ln\mathrm{RH}$ ([7.6.3](/7.6.3#eq-3.7)). The difficulty is that the relative humidity corresponding to the water potential of plant tissue is extremely close to 1: at 25 °C $RT/\bar V_{\mathrm{w}} = 137\,\mathrm{MPa}$, $-1\,\mathrm{MPa}$ corresponds to $\mathrm{RH} = 0.9927$, and the **dew point** is only about $0.12\,\mathrm{K}$ below room temperature, so the instrument must resolve temperature differences of a thousandth of a kelvin. A thermocouple psychrometer uses the **Peltier effect** to cool the measuring junction of a thermocouple below the dew point so that a small drop of water condenses, and then measures the temperature at which the drop evaporates. Another approach is to suspend in the chamber a drop of a calibration solution of known solute potential: when the water potential of the calibration solution is higher than that of the tissue, it keeps evaporating and cools; when it is lower, water from the tissue evaporates and condenses on the calibration solution, warming it; when the two are equal the temperature does not change. By measuring a series of solutions of known concentration, the one with the same water potential as the tissue can be found.

The pressure chamber method (Scholander et al., 1965) seals a leaf with its petiole, or a small twig, in a steel pressure chamber with the cut end protruding. The xylem sap of a transpiring plant is under tension, and on cutting the sap retracts into the vessels; compressed gas is slowly admitted to the chamber until sap just reappears at the cut surface, and the pressure at that point, $P_{\mathrm{b}}$, is called the balancing pressure. The solute potential of xylem sap is small, and before excision the water potentials of the cells and the xylem are nearly in equilibrium, so $\Psi_{\mathrm{leaf}} \approx -P_{\mathrm{b}} + \Psi_{\mathrm{s,xylem}} \approx -P_{\mathrm{b}}$: for example, with $P_{\mathrm{b}} = 1.2\,\mathrm{MPa}$ and a sap solute potential of $-0.05\,\mathrm{MPa}$ the leaf water potential is about $-1.25\,\mathrm{MPa}$. The pressure chamber is fast and portable and is the standard method for measuring plant water status in the field; the pressure–volume curves of 2.5.2 are also measured with it; its accuracy is lower than that of psychrometric methods.

The freezing-point method uses the lowering of the freezing point of a solution by solutes, that is, **freezing-point depression**: when $1\,\mathrm{osmol}$ of solute is dissolved per kilogram of water the freezing point falls by $1.86\,\mathrm{K}$. A freezing-point osmometer rapidly cools the sample to freezing and then warms it slowly, recording the temperature at which the ice crystals have completely melted. From Eq. (2.2), at 20 °C $\Psi_{\mathrm{s}} \approx -2.437 \times \Delta T_{\mathrm{f}}/1.86 \approx -1.31\,\Delta T_{\mathrm{f}}\,\mathrm{MPa}$ ($\Delta T_{\mathrm{f}}$ in K). For example, if the freezing point of cell sap is $-0.62\,^\circ\mathrm{C}$, its osmolarity is about $0.33\,\mathrm{osmol\,kg^{-1}}$ and its solute potential about $-0.81\,\mathrm{MPa}$.

In the pressure probe method, a glass capillary filled with silicone oil and connected to a pressure transducer is inserted into the cell; under the turgor pressure, cell sap enters the tip of the capillary, and a piston is used to push the interface between oil and cell sap back to its original position, at which point the pressure read by the transducer is the turgor pressure of the cell. By changing the cell volume abruptly with the piston and recording the change in pressure and the subsequent relaxation, $\varepsilon$ (Eq. (2.4)) and $L_p$ (Eq. (2.8)) can also be obtained. This technique was developed in the 1970s and is the main experimental basis for the water relations of single cells.

## Summary

| Concept and relation | Key points | Typical values |
|---|---|---|
| Properties of water | Polar, tetrahedral, hydrogen bonds; solvent, high specific heat, high heat of vaporization, high surface tension, high tensile strength | $44\,\mathrm{kJ\,mol^{-1}}$; $0.0728\,\mathrm{N\,m^{-1}}$; tensile strength $> 20\,\mathrm{MPa}$ |
| States of water | Free and bound water; a high ratio means vigorous metabolism, a low one stress resistance | Water content 70%–90% of fresh weight, about 10% in dry seeds |
| Water potential ([7.6.3](/7.6.3#def-3.1.1)) | Chemical potential difference of water per partial molar volume; zero for pure water; water flows from high to low | Leaves $-0.2$ to $-2.5\,\mathrm{MPa}$ |
| Solute potential (Definition 2.2.1) | Solutes lower the water potential, depending only on particle number; $-\phi icRT$ | $1\,\mathrm{osmol\,L^{-1}} \approx -2.44\,\mathrm{MPa}$ (20 °C) |
| Pressure potential (Definition 2.2.2) | Hydrostatic pressure; turgor (positive) in cells, tension (negative) in vessels | Turgor $0.1$–$3\,\mathrm{MPa}$ |
| Gravitational potential | $\rho_{\mathrm{w}}gh$ | $0.01\,\mathrm{MPa\,m^{-1}}$ |
| Matric potential (Definition 2.2.3) | Adsorption on hydrophilic surfaces and fine pores; dominant in dry seeds and dry soil | Air-dried seeds $< -100\,\mathrm{MPa}$ |
| Diffusion, bulk flow, osmosis | Concentration gradient, pressure gradient, transmembrane water potential difference; $t \sim L^2/D$ | Glucose diffusing $50\,\mu\mathrm{m}$ takes about 2.5 s, $1\,\mathrm{m}$ about 32 years |
| Imbibition, osmotic and pressure-driven uptake | Depend on $\Psi_{\mathrm{m}}$, $\Psi_{\mathrm{s}}$ and $\Psi_{\mathrm{p}}$ respectively; the driving force is always the water potential difference | Protein > starch > cellulose |
| Plasmolysis (Definition 2.4.1) | Protoplast separates from the wall in a hypertonic solution; at incipient plasmolysis $\Psi_{\mathrm{p}} = 0$ | Example 2.4.1 |
| Volumetric elastic modulus (Definition 2.5.1) | Ratio of turgor change to relative volume change; a rigid wall stabilizes volume | $1$–$50\,\mathrm{MPa}$; turgor lost at a 10%–15% volume decrease |
| Pressure–volume curve | $1/(-\Psi)$ linear in water loss; yields $\pi_0$, $a$, $\Psi_{\mathrm{tlp}}$, $\varepsilon$ | Low $\Psi_{\mathrm{tlp}}$ means drought tolerance |
| Membrane hydraulic conductivity | $J_V = L_p\Delta\Psi$; half-time proportional to $V/A$ and inversely proportional to $L_p$ and $\varepsilon - \Psi_{\mathrm{s}}$ | $L_p \sim 10^{-7}$–$10^{-6}\,\mathrm{m\,s^{-1}\,MPa^{-1}}$; $t_{1/2}$ 1–10 s |
| Aquaporins | Change the rate, not the direction; PIP, TIP, NIP, SIP; gated by phosphorylation, pH and $\ce{Ca^2+}$ | 35 genes in *Arabidopsis* |
| Water flow between cells | Compare total water potentials, not turgor or solute potential | Example 2.7.1 |
| Measuring water potential | Chardakov, plasmolytic, psychrometer, pressure chamber, freezing point, pressure probe | $-1\,\mathrm{MPa} \leftrightarrow \mathrm{RH} = 0.993$; $\Psi_{\mathrm{s}} \approx -1.31\Delta T_{\mathrm{f}}$ |

The main equations of this chapter:

| No. | Equation | Use |
|---|---|---|
| (2.1) | $\Psi_{\mathrm{w}} = \Psi_{\mathrm{s}} + \Psi_{\mathrm{p}} + \Psi_{\mathrm{g}} + \Psi_{\mathrm{m}}$ | Decomposition of water potential |
| (2.2) | $\Psi_{\mathrm{s}} = -c_{\mathrm{s}}RT$, $c_{\mathrm{s}} = ic$ (multiply by $\phi$ for real solutions) | Solute potential from osmolarity |
| (2.3) | $J_V = L_p(\Delta\Psi_{\mathrm{p}} + \sigma\Delta\Psi_{\mathrm{s}})$ | Osmotic flow when the solute partly crosses the membrane |
| (2.4) | $\varepsilon = \Delta\Psi_{\mathrm{p}}/(\Delta V/V)$ | Stiffness of the cell wall |
| (2.5) | $\Psi_{\mathrm{s}} = \Psi_{\mathrm{s,ip}}/v$, $\Psi_{\mathrm{p}} = \varepsilon(v - 1)$ | Höfler diagram |
| (2.6) | $1/(-\Psi_{\mathrm{w}}) = R_{\mathrm{s}}/(-\pi_0)$ | Pressure–volume curve |
| (2.7) | $J_V = L_p\Delta\Psi_{\mathrm{w}}$ | Transmembrane water flow |
| (2.8) | $t_{1/2} = 0.693V/[AL_p(\varepsilon - \Psi_{\mathrm{s}})]$ | How fast the cell reaches water potential equilibrium with its environment |

## Questions

1. At 25 °C, slices of a tissue are placed in sucrose solutions of different concentrations, and incipient plasmolysis is found to begin at exactly $0.35\,\mathrm{mol\,L^{-1}}$; the water potential of the tissue measured by the Chardakov method corresponds to a $0.25\,\mathrm{mol\,L^{-1}}$ sucrose solution. Find the original $\Psi_{\mathrm{w}}$ of the tissue cells and the $\Psi_{\mathrm{s}}$ at incipient plasmolysis, and estimate the original $\Psi_{\mathrm{s}}$ and $\Psi_{\mathrm{p}}$ (assume that the cell volume shrank by 8% on losing turgor).

   **Answer** At 25 °C $RT = 8.314 \times 298.15\,\mathrm{J\,mol^{-1}} = 2.479\,\mathrm{L\,MPa\,mol^{-1}}$. The original $\Psi_{\mathrm{w}}$ of the tissue is $-0.25 \times 2.479 = -0.62\,\mathrm{MPa}$. At incipient plasmolysis $\Psi_{\mathrm{p}} = 0$ and $\Psi_{\mathrm{s,ip}} = -0.35 \times 2.479 = -0.87\,\mathrm{MPa}$. The original volume is $1/0.92 = 1.087$ times that at incipient plasmolysis, and the solute is diluted, so the original $\Psi_{\mathrm{s}} = -0.87 \times 0.92 = -0.80\,\mathrm{MPa}$, and therefore $\Psi_{\mathrm{p}} = -0.62 - (-0.80) = 0.18\,\mathrm{MPa}$. The plasmolytic method gives the solute potential at $\Psi_{\mathrm{p}} = 0$, which is lower than the original water potential of the tissue; the difference between the two methods reflects precisely the existence of turgor.

2. A cell has $\Psi_{\mathrm{s}} = -1.0\,\mathrm{MPa}$, $\Psi_{\mathrm{p}} = 0.4\,\mathrm{MPa}$ and $\varepsilon = 8\,\mathrm{MPa}$. It is placed in pure water. Using the model of Eq. (2.5), estimate the percentage increase in cell volume at equilibrium and the turgor at equilibrium ($\varepsilon$ taken as constant).

   **Answer** First find the reference at incipient plasmolysis: the relative volume $v_0$ at the current state satisfies $\varepsilon(v_0 - 1) = 0.4$, so $v_0 = 1.05$, and therefore $\Psi_{\mathrm{s,ip}} = -1.0 \times 1.05 = -1.05\,\mathrm{MPa}$. At equilibrium in pure water $\Psi_{\mathrm{w}} = 0$: $8(v - 1) = 1.05/v$, that is, $8v^2 - 8v - 1.05 = 0$ and $v = [8 + \sqrt{64 + 33.6}]/16 = 1.117$. The volume increases relative to the original by $1.117/1.05 - 1 \approx 6.4\%$, and the turgor at equilibrium is $\Psi_{\mathrm{p}} = 8 \times 0.117 = 0.94\,\mathrm{MPa}$, exactly equal to $-\Psi_{\mathrm{s}} = 1.05/1.117 = 0.94\,\mathrm{MPa}$ at that point.

3. Using Eq. (2.8), compare the half-times for two cells to reach water potential equilibrium with the environment: (a) a root cortical cell, approximated as a sphere of radius $25\,\mu\mathrm{m}$, with $L_p = 5\times10^{-7}\,\mathrm{m\,s^{-1}\,MPa^{-1}}$, $\varepsilon = 15\,\mathrm{MPa}$ and $\Psi_{\mathrm{s}} = -0.7\,\mathrm{MPa}$; (b) an internodal cell of a giant alga (such as *Chara*), approximated as a long cylinder of radius $0.4\,\mathrm{mm}$, with $L_p = 1\times10^{-6}\,\mathrm{m\,s^{-1}\,MPa^{-1}}$, $\varepsilon = 40\,\mathrm{MPa}$ and $\Psi_{\mathrm{s}} = -0.6\,\mathrm{MPa}$.

   **Answer** (a) For a sphere $V/A = r/3 = 8.3\,\mu\mathrm{m}$, and $t_{1/2} = 0.693 \times 8.3\times10^{-6}/(5\times10^{-7} \times 15.7) = 0.73\,\mathrm{s}$. (b) For a long cylinder $V/A \approx r/2 = 200\,\mu\mathrm{m}$, and $t_{1/2} = 0.693 \times 2\times10^{-4}/(10^{-6} \times 40.6) = 3.4\,\mathrm{s}$. Although the giant algal cell has both a higher membrane hydraulic conductivity and a stiffer wall, its volume-to-surface ratio is about 24 times greater and equilibration is still slower; this shows that cell size ($V/A$) is as important as the properties of membrane and wall.

4. Why can we say that "a cell with high turgor cannot necessarily take up water from a cell with low turgor"? Use the Höfler diagram to explain the relation between solute potential and pressure potential in a fully turgid cell.

   **Answer** Water flow between cells is determined by the total water potential, $\Psi_{\mathrm{w}} = \Psi_{\mathrm{s}} + \Psi_{\mathrm{p}}$; high turgor raises the water potential, and it can accompany a low water potential only if the solute potential is also sufficiently low (in Example 2.7.1 the turgor of A exceeds that of B, but its solute potential is lower by more, so it still takes up water from B). On the Höfler diagram the point of full turgor is the intersection of the water potential curve with the zero line, where $\Psi_{\mathrm{w}} = 0$ and $\Psi_{\mathrm{p}} = -\Psi_{\mathrm{s}}$, the two being equal in magnitude and opposite in sign; the cell takes up no more water because its water potential is already equal to that of pure water.

5. Why do flooded plants wilt? Explain in terms of root hydraulic conductivity and the gating of aquaporins, and show that this is not in conflict with the conclusion that "water moves passively".

   **Answer** Flooding makes the roots hypoxic, impairing respiration and ATP production, and the cytosol acidifies; the histidine on loop D of the plasma membrane aquaporins (PIPs) is protonated, the pore is closed, and the hydraulic conductivity of the root falls sharply. Transpiration continues while the resistance to water flow through the root has increased, so the leaves do not receive enough supply, lose turgor and wilt. Here water still moves passively down the water potential gradient; metabolic energy is not used to push water but to maintain the high hydraulic conductivity of the membrane (keeping the aquaporins open); when the energy supply is interrupted, the water potential gradient is still there but the water flow becomes smaller.
