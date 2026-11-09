---
title: "Controlling Microbial Growth: Sterilization and Disinfection"
description: "The vocabulary of microbial control (sterilization, disinfection, antisepsis, sanitization; static, cidal and lytic agents); heat killing as a first-order process, the decimal reduction time D, the z value, lethality F0 and the 12D standard; the autoclave and what limits it, dry heat, tyndallization, pasteurization and canning; ultraviolet and ionizing radiation, D10 and survival curves with a shoulder, food irradiation; depth, membrane and nucleopore filters and HEPA; measuring antimicrobial activity; disinfectants, antiseptics and sterilants by chemical class and mechanism; the Chick–Watson law and Ct values; factors that affect efficacy and the resistance hierarchy; the inactivation of prions."
---

The control of microbial growth is as old as cooking, salting and smoking food, but its systematic form dates from the nineteenth century, when Pasteur showed that heating destroys the organisms that spoil wine and beer, Tyndall that boiling must be repeated to kill heat-resistant forms, Lister that carbolic acid (phenol) on wounds and instruments prevents surgical infection, and Koch that steam is a more reliable killer than dry heat. Today the same principles keep media and instruments sterile in the laboratory, make canned food safe, provide clean drinking water and prevent infections in hospitals.

This chapter treats the physical and chemical agents used outside the body. Their effect is the reverse of growth: just as a growing population increases exponentially ([7.11.8](/7.11.8)), a population exposed to a lethal agent usually dies exponentially, and the same arithmetic of logarithms describes both. The resistance of different organisms to these agents, in particular of the **endospores** of *Bacillus* and *Clostridium* ([7.11.3](/7.11.3)), sets the conditions that must be used. Antimicrobial drugs, which act inside the body and must be selectively toxic, are the subject of [7.11.14](/7.11.14) and [7.11.15](/7.11.15); the DNA damage on which ultraviolet and ionizing radiation act is described in [7.2.8](/7.2.8).

## 10.1. Terms and Principles

### 10.1.1. Degrees of Control

The words used for microbial control have precise meanings, which matter in practice: a procedure that disinfects an instrument may leave it far from sterile.

**Definition 10.1.1 (Sterilization, Disinfection and Antisepsis)** **Sterilization** is the killing or removal of all microorganisms, including endospores and viruses, from an object or material. **Disinfection** is the killing or removal of pathogens and most other microorganisms, though not necessarily of endospores, from inanimate objects and surfaces. **Antisepsis** is the reduction of microorganisms on living tissue, such as skin or wounds, by agents mild enough not to harm it.

Related terms are *sanitization*, the reduction of microbial numbers on surfaces such as food-processing equipment to levels judged safe by public health standards, and *decontamination*, the treatment of an object to make it safe to handle, which can be as simple as washing. Sterility is absolute in principle, but because killing is exponential (Section 10.2), it is defined in practice as a probability: a sterilization process for medical devices must achieve a sterility assurance level of $10^{-6}$, that is, at most one item in a million may carry a surviving organism.

**Definition 10.1.2 (Static and Cidal Agents)** An agent that kills microorganisms is called *-cidal* (**bactericidal**, fungicidal, virucidal, sporicidal for bacteria, fungi, viruses and spores); an agent that only inhibits their growth, so that growth resumes when it is removed, is called *-static* (**bacteriostatic**, fungistatic). A bactericidal agent that kills by lysing cells is *bacteriolytic*.

The three kinds of effect are distinguished by following a culture after the agent is added with both a viable count and a total count or turbidity (figure in Section 10.4.1): a static agent stops the increase of both; a cidal agent makes the viable count fall while the cells, though dead, remain intact and the turbidity constant; a lytic agent makes both fall. Static agents are typically inhibitors of an essential process, such as protein synthesis, that bind reversibly; cidal ones bind tightly or damage the cell irreversibly, as formaldehyde does; lytic ones, such as detergents that dissolve the membrane, destroy its integrity. Whether an agent is static or cidal often depends on its concentration and on the organism.

### 10.1.2. An Overview of Methods

| Method | Examples | Main use |
|---|---|---|
| Moist heat | autoclaving, boiling, tyndallization, pasteurization | sterilization of media, glassware, instruments, waste; food |
| Dry heat | hot-air oven, flaming, incineration | glassware, metal instruments, oils and powders; disposal |
| Low temperature, drying | refrigeration, freezing, freeze-drying, dehydration | preservation (mostly static) |
| Radiation | ultraviolet; gamma rays, electron beams, X-rays | surfaces and air; sterilization of disposables, food irradiation |
| Filtration | membrane filters, depth filters, HEPA | heat-sensitive liquids; air |
| Chemicals | alcohols, aldehydes, phenolics, halogens, peroxygens, quaternary ammonium compounds, ethylene oxide | disinfection, antisepsis, chemical sterilization |

## 10.2. Heat

### 10.2.1. The Kinetics of Heat Killing

Heat is the most widely used agent of sterilization, because it is effective, cheap and leaves no residue. Heat kills by denaturing proteins and nucleic acids and by disrupting membranes; in moist heat, water takes part in the unfolding and coagulation of proteins, so that moist heat kills at lower temperatures and in shorter times than dry heat, which kills mainly by oxidation. Steam also transfers heat efficiently, since it releases its latent heat of vaporization where it condenses on a cooler surface.

When a suspension of microorganisms is held at a lethal temperature, the number of survivors usually falls by the same fraction in each interval of time: death is a first-order process, like radioactive decay, and the logarithm of the number of survivors falls linearly (figure below, panel A). The reason is that each cell is killed by a random event, such as the inactivation of one essential molecule, whose probability per unit time is constant.

**Definition 10.2.1 (Decimal Reduction Time)** The **decimal reduction time** $D$ (D value) of an organism at a given temperature is the time required at that temperature to reduce the number of viable cells or spores tenfold, that is, to kill $90\,\%$ of the population.

**Formula 10.2.1 (First-Order Death)** If death is first order with rate constant $k_{\mathrm{d}}$, the number of survivors after heating for time $t$ is

$$
N(t) = N_0\,\mathrm{e}^{-k_{\mathrm{d}} t} = N_0\,10^{-t/D}, \qquad D = \frac{\ln 10}{k_{\mathrm{d}}}, \tag{10.1}
$$
so a treatment of duration $t$ achieves $t/D$ decimal (log) reductions, independently of the initial number $N_0$.

For a mesophilic bacterium, $D$ is about $42$ minutes at $50\,^\circ\mathrm{C}$, $12$ minutes at $60\,^\circ\mathrm{C}$ and $3$ minutes at $70\,^\circ\mathrm{C}$ (data from Madigan et al. 2019). Because the reduction is a fixed number of logarithms, the time needed to sterilize depends on how many organisms there are at the start: to bring $10^6$ spores to a probability of survival of $10^{-6}$ requires $12$ decimal reductions, whereas $10^2$ spores require only $8$. The older notion of a *thermal death time*, the time needed to kill all cells at a given temperature, therefore depends on the size of the population and is less useful than $D$.

How strongly $D$ depends on temperature is expressed by a second parameter. When $\log_{10} D$ is plotted against temperature, the points fall approximately on a straight line (panel B).

**Formula 10.2.2 (The z Value)** The *z value* is the rise in temperature that reduces $D$ tenfold:

$$
D(T) = D(T_{\mathrm{ref}})\,10^{(T_{\mathrm{ref}} - T)/z}. \tag{10.2}
$$

Spores of *Clostridium botulinum*, the organism that determines the heat treatment of low-acid canned food, have $D_{121.1} \approx 0.21\,\mathrm{min}$ and $z \approx 10\,^\circ\mathrm{C}$; for vegetative cells $z$ is typically $4$–$7\,^\circ\mathrm{C}$, and the mesophile above, with $D$ falling fourfold per $10$ degrees, has $z \approx 17\,^\circ\mathrm{C}$. The linear relation is an empirical approximation; it corresponds to an Arrhenius dependence of $k_{\mathrm{d}}$ with a very large activation energy ($z = 10\,^\circ\mathrm{C}$ near $121\,^\circ\mathrm{C}$ corresponds to roughly $300\,\mathrm{kJ\,mol^{-1}}$), as expected for the cooperative unfolding of proteins ([7.11.9](/7.11.9#sec-9.1.1)). Not every survival curve is a straight line: clumps, a mixture of populations with different resistance, or the need for spores to be activated by heat before they germinate produce shoulders and tails, and the D value then describes only the linear part.

### 10.2.2. Lethality and the 12D Standard

In a real process the temperature is not constant: a can, a flask of medium or a load in an autoclave heats up and cools down slowly. The killing achieved at each moment can be converted, with Eq. (10.2), into an equivalent time at a reference temperature, and added up.

**Formula 10.2.3 (Lethality)** The lethality of a heat process with temperature history $T(t)$ is the equivalent time at the reference temperature,

$$
F = \int 10^{(T(t) - T_{\mathrm{ref}})/z}\,\mathrm{d}t. \tag{10.3}
$$
For sterilization the reference is $121.1\,^\circ\mathrm{C}$ ($250\,^\circ\mathrm{F}$) and $z = 10\,^\circ\mathrm{C}$, and $F$ is then written $F_0$. A process with lethality $F$ achieves $F/D_{\mathrm{ref}}$ decimal reductions of an organism with that $z$.

The integrand, the *lethal rate*, falls tenfold for each $10$ degrees below the reference, so that the time a can spends below about $100\,^\circ\mathrm{C}$ contributes almost nothing to its sterility (panel C). The canning industry requires that low-acid foods (pH above $4.6$) receive at least a "botulinum cook" of $12$ decimal reductions of *C. botulinum* spores, the 12D concept: $12 \times 0.21 = 2.5\,\mathrm{min}$ at $121.1\,^\circ\mathrm{C}$, and in practice $F_0$ values of $3$ minutes or more at the slowest-heating point of the can. The reasoning is that even a can containing $10^{12}$ spores, an absurdly high number, would be left with one expected survivor; with realistic numbers of less than one spore per can, the probability that a can contains a survivor is about $10^{-12}$ or less. Acid foods (pH $4.6$ or below) such as fruits, tomatoes and pickles need much milder treatments, because *C. botulinum* does not grow or make toxin below pH $4.6$, and heat killing is faster in acid. Since spores of some spoilage thermophiles are far more resistant than those of *C. botulinum*, commercial processes are often designed for still higher $F_0$ to prevent spoilage, a different goal from safety.

**Example 10.2.1** A sterilization process must reduce a population of $10^4$ spores of an indicator organism with $D_{121.1} = 1.5\,\mathrm{min}$ to a survival probability of $10^{-6}$. It needs $\log_{10}(10^4/10^{-6}) = 10$ decimal reductions, that is, $F_0 = 10 \times 1.5 = 15\,\mathrm{min}$. At $115\,^\circ\mathrm{C}$, where $D = 1.5 \times 10^{0.61} = 6.1\,\mathrm{min}$, the same effect would take $61$ minutes.

:::

![Kinetics of heat killing. A: survival curves of a mesophilic bacterium at 50, 60 and 70 °C, with decimal reduction times of 42, 12 and 3 min (data from Madigan et al. 2019); on a logarithmic axis first-order death gives straight lines, and D is the time for one tenfold fall (arrow, at 60 °C). B: D against temperature on a logarithmic axis: the mesophile of A (z about 17 °C) and spores of *Clostridium botulinum* (D at 121.1 °C = 0.21 min, z = 10 °C); a rise of z degrees reduces D tenfold. C: a canning process: the temperature at the center of a can in a retort at 121 °C (red; heating and cooling modeled as first-order lags, illustrative) and the accumulated lethality F0 (dashed), which exceeds the 12D value for *C. botulinum* spores (2.5 min, dotted) only after the center has been close to the retort temperature for some minutes](./plots/heat-kill.py)

### 10.2.3. The Autoclave and Dry Heat

Endospores survive boiling for hours, so sterilization by moist heat needs temperatures above $100\,^\circ\mathrm{C}$, which water reaches only under pressure. The *autoclave* is a pressure chamber in which steam at about $100\,\mathrm{kPa}$ above atmospheric pressure ($1.1\,\mathrm{kg\,cm^{-2}}$, $15\,\mathrm{lb\,in^{-2}}$) reaches $121\,^\circ\mathrm{C}$; at this temperature small amounts of spore-containing material are sterilized in about $15$ minutes. It is the temperature that kills, not the pressure. Its effectiveness depends on several conditions:

- Air must be removed. A mixture of air and steam at the same pressure is cooler than pure steam, and air trapped in a container or a dense load prevents steam from reaching the material. Autoclaves expel air by gravity, as steam enters from the top and pushes the heavier air out at the bottom, or by evacuating the chamber before admitting steam (prevacuum cycles, which also allow $134\,^\circ\mathrm{C}$ cycles of a few minutes).
- The material itself must reach the temperature. Large volumes of liquid and bulky loads heat slowly, so the holding time is counted from the moment the slowest point reaches $121\,^\circ\mathrm{C}$; a $1\,\mathrm{L}$ bottle of medium needs considerably longer than a test tube.
- The initial number of organisms and the medium matter: more organisms need more decimal reductions; proteins, fats and sugars protect cells, and organisms die faster at acidic pH.

The success of a cycle is checked with chemical indicators (tape or strips that change color at the right temperature) and with biological indicators, strips carrying about $10^6$ spores of the highly heat-resistant *Geobacillus stearothermophilus*, which are incubated afterward to test whether any survived.

Dry heat is used for materials that steam would damage or cannot penetrate: glassware, metal instruments, powders and oils. Because it is less efficient, it needs $160$–$170\,^\circ\mathrm{C}$ for one to two hours in a hot-air oven. Flaming of inoculating loops and incineration of waste are dry-heat methods too.

### 10.2.4. Boiling, Tyndallization and Pasteurization

Boiling at $100\,^\circ\mathrm{C}$ for $10$–$30$ minutes kills vegetative cells and most viruses, but not all spores, so it disinfects rather than sterilizes. Before autoclaves were common, heat-sensitive media were sterilized by *tyndallization* (intermittent or fractional sterilization), named after Tyndall: the material is heated to about $100\,^\circ\mathrm{C}$ for $30$ minutes on three successive days and incubated in between, so that spores surviving one heating germinate and are killed as vegetative cells at the next. It fails for spores that do not germinate in the material.

**Definition 10.2.2 (Pasteurization)** **Pasteurization** is a mild heat treatment of a liquid food that kills pathogens and reduces the number of spoilage organisms, without sterilizing it or significantly changing its flavor and nutritional value.

Pasteur developed the procedure in the 1860s to prevent the souring of wine; its main use today is for milk, juices and beer. Milk was originally pasteurized at $63\,^\circ\mathrm{C}$ for $30$ minutes (low-temperature, long-time); today most milk is passed through a heat exchanger and held at $71$–$72\,^\circ\mathrm{C}$ for $15$ seconds (high-temperature, short-time, or flash pasteurization). The conditions were set to kill the most heat-resistant of the pathogens once transmitted by raw milk, *Mycobacterium bovis* (tuberculosis) and *Coxiella burnetii* (Q fever), and by reducing the total load they extend the shelf life of refrigerated milk. Ultrahigh-temperature (UHT) treatment at $135$–$140\,^\circ\mathrm{C}$ for one to a few seconds, followed by aseptic packaging, is a true sterilization, so that UHT milk keeps for months at room temperature. Because high temperatures kill microorganisms far faster than they degrade flavor and vitamins (the $z$ value for spores is about $10\,^\circ\mathrm{C}$, that for most quality changes $25$–$40\,^\circ\mathrm{C}$), high-temperature, short-time processes preserve quality better.

## 10.3. Radiation and Filtration

### 10.3.1. Ultraviolet Radiation

Ultraviolet radiation between about $220$ and $300\,\mathrm{nm}$ is absorbed by DNA and forms pyrimidine dimers and other photoproducts that block replication and transcription ([7.2.8](/7.2.8#sec-8.1.2)); the low-pressure mercury lamps used as "germicidal" lamps emit mostly at $254\,\mathrm{nm}$, close to the absorption maximum of DNA. UV is used to disinfect the work surfaces of biological safety cabinets and laminar-flow hoods when they are not in use, air in operating theaters and food-preparation rooms, and water and wastewater, in which it kills the chlorine-resistant protozoan oocysts of *Cryptosporidium*. Its weakness is poor penetration: it is absorbed by glass, plastics, dust, turbid water and the outer layers of cells, so it acts only on exposed surfaces and thin layers. Treated bacteria can also recover: those with photolyase repair dimers when exposed to visible light afterward (photoreactivation), and others survive by dark repair, so UV-treated water is not stored in the light. Spores are more UV-resistant than vegetative cells, because their DNA is bound to small acid-soluble spore proteins, which change the photochemistry, and because they have a dedicated repair enzyme.

### 10.3.2. Ionizing Radiation

Ionizing radiation, from the radionuclides $^{60}\mathrm{Co}$ and $^{137}\mathrm{Cs}$ (gamma rays), from electron accelerators (electron beams) or from X-ray sources, carries enough energy to ionize molecules, mostly water, whose radiolysis produces hydroxyl radicals that break DNA strands. It penetrates solid objects and packaging, so it can sterilize items in their final, sealed packaging. Its dose is measured as absorbed energy per mass, in grays ($1\,\mathrm{Gy} = 1\,\mathrm{J\,kg^{-1}} = 100\,\mathrm{rad}$). The analog of the decimal reduction time is the decimal reduction dose $D_{10}$, the dose that kills $90\,\%$ of a population.

| Organism | $D_{10}$ / Gy |
|---|---|
| *Salmonella enterica* (serovar Typhimurium) | 200 |
| *Escherichia coli* | 300 |
| *Saccharomyces cerevisiae*, *Aspergillus niger* | 500 |
| *Bacillus subtilis* | 600 |
| *Lactobacillus brevis* | 1200 |
| *Deinococcus radiodurans* | 2200 |
| *Clostridium botulinum* (spores) | 3300 |
| Coxsackie virus | 4500 |
| Foot-and-mouth disease virus | 13 000 |

These values (data from Madigan et al. 2019) show the general order: endospores and viruses are more resistant than vegetative cells, small viruses being among the most resistant, and microorganisms are far more resistant than animals, for which a dose of about $10\,\mathrm{Gy}$ delivered over a short time can be lethal. Survival curves of many organisms have a shoulder at low doses before the exponential decline, because damage must accumulate (or exceed the capacity for repair) before it kills. A simple description is the multitarget model, in which a cell dies only when all of $n$ sensitive targets have been hit:

**Formula 10.3.1 (Multitarget Survival)** If a cell has $n$ independent targets, each inactivated by a Poisson number of hits with mean $d/d_0$ at dose $d$, the surviving fraction is

$$
S(d) = 1 - \left(1 - \mathrm{e}^{-d/d_0}\right)^n. \tag{10.4}
$$
For $n = 1$ the curve is a single exponential with $D_{10} = d_0 \ln 10$; for $n > 1$ it has a shoulder and then becomes exponential with the same slope, extrapolating back to $S = n$ at zero dose.

*Deinococcus radiodurans* survives doses of several kilograys with little loss of viability (a pronounced shoulder) because it reassembles its shattered chromosomes efficiently ([7.11.18](/7.11.18)). Medical disposables (syringes, catheters, sutures), plastic labware, drugs and tissue grafts are sterilized by ionizing radiation, commonly with doses around $25\,\mathrm{kGy}$, validated against the resistance of the actual bioburden. Foods such as spices, dried vegetables, poultry and meat are irradiated in many countries at lower doses to kill pathogens and insects or to delay spoilage; irradiated foods do not become radioactive.

![Ionizing radiation and filtration. A: survival curves from the decimal reduction doses of several organisms (data from Madigan et al. 2019; straight lines on the logarithmic axis for single-hit kinetics); *Deinococcus radiodurans* is drawn with the multitarget model (Formula 10.3.1) with a terminal D10 of 2200 Gy and an illustrative shoulder of about 5 kGy, over which survival hardly falls. B: sizes of viruses and cells compared with the pores of membrane filters (0.2 and 0.45 µm) and the particle size used to test HEPA filters (about 0.3 µm), on a logarithmic scale: bacteria and larger cells are retained by a 0.2-µm filter, but viruses, and some very small or thin cells such as mycoplasmas and *Leptospira*, can pass](./plots/radiation-filtration.py)

### 10.3.3. Filtration

Liquids that heat would damage, such as solutions of vitamins, antibiotics, serum and some culture media, and air are sterilized by passing them through filters that hold back microorganisms (panel B). Three types of filter are in use:

- Depth filters are fibrous sheets of paper, glass or other fibers that trap particles throughout their thickness. The most important are *HEPA* (high-efficiency particulate air) filters, which by the usual standard remove at least $99.97\,\%$ of particles of $0.3\,\mu\mathrm{m}$, the size that penetrates fibrous filters most easily (smaller particles are caught by diffusion, larger ones by inertia). HEPA filters clean the air of biological safety cabinets, operating theaters and clean rooms; they reduce but do not guarantee sterility.
- Membrane filters are thin films of polymers such as cellulose esters, nylon or polyethersulfone with pores of defined size. Filters with pores of $0.2$ or $0.22\,\mu\mathrm{m}$ are used for sterilization (they are validated by their ability to retain the small bacterium *Brevundimonas diminuta*), and $0.45\,\mu\mathrm{m}$ filters for clarification and for collecting bacteria from water for counting.
- Nucleopore (track-etched) filters are thin polycarbonate films in which radiation tracks are etched into uniform cylindrical holes. They are used to collect cells for microscopy, on a flat surface where they can be counted ([7.11.8](/7.11.8#sec-8.6.1)).

Filtration does not remove viruses, which are smaller than $0.2\,\mu\mathrm{m}$ except for the largest, and some bacteria pass $0.2\,\mu\mathrm{m}$ filters: mycoplasmas, which are small and lack a wall so that they deform, the very thin spirochete *Leptospira*, and the "ultramicrobacteria" of nutrient-poor waters. Cell-culture media are therefore often filtered through $0.1\,\mu\mathrm{m}$ membranes to exclude mycoplasmas, and viruses are removed by special nanofilters only where required, as for biological drugs.

### 10.3.4. Low Temperature and Drying

Refrigeration ($4\,^\circ\mathrm{C}$) and freezing preserve food mainly by slowing or stopping growth, not by killing; psychrotolerant organisms still grow slowly in the refrigerator ([7.11.9](/7.11.9#sec-9.1.2)), and many organisms survive freezing. Drying, salting and sugaring lower the water activity below the limits of most organisms ([7.11.9](/7.11.9#sec-9.3.1)); they too are mainly static. Freeze-drying (lyophilization), the removal of water by sublimation from a frozen sample under vacuum, is used to preserve microbial cultures, vaccines and foods for long periods.

## 10.4. Chemical Control

### 10.4.1. Measuring Antimicrobial Activity

The activity of a chemical against an organism is measured by finding the lowest concentration that inhibits growth, the **minimum inhibitory concentration** (MIC). In the dilution method, a series of tubes or wells of liquid medium containing twofold dilutions of the agent is inoculated with a standard number of cells and incubated; the MIC is the lowest concentration in which no growth is visible (figure below, panel D). In the disc diffusion method, paper discs containing the agent are placed on an agar plate seeded with the organism; the agent diffuses into the agar and forms a concentration gradient, and the diameter of the zone without growth around each disc depends on the activity of the agent, its diffusion and the amount in the disc. These methods are used above all for antibiotics, and their standardized clinical forms are described in [7.11.14](/7.11.14). For disinfectants, which act briefly on surfaces, suspension and carrier tests measure the decimal reductions achieved within a given contact time instead (the historical measure, the phenol coefficient, compared an agent with phenol).

![Static, cidal and lytic agents and the MIC. A–C: an exponentially growing culture (doubling time 40 min) receives an inhibitory concentration of an agent at 2 h (arrow); total cells (dashed, measured by turbidity) and viable cells (green) on a logarithmic axis (model curves). A bacteriostatic agent stops the increase of both (the two curves coincide), and growth resumes when it is removed (dotted); a bactericidal agent makes the viable count fall while dead cells remain and the turbidity stays constant; a bacteriolytic agent makes both fall. D: the broth dilution test: twofold dilutions of the agent are inoculated with the same number of cells, and after incubation the tubes below the MIC (here 4 µg per milliliter) are turbid](./plots/agent-effects.py)

### 10.4.2. Disinfectants, Antiseptics and Sterilants

Chemicals for use outside the body are grouped by where they are used and how strongly they act.

**Definition 10.4.1 (Disinfectant and Antiseptic)** A **disinfectant** is a chemical agent that kills microorganisms, but not necessarily endospores, on inanimate objects and surfaces. An **antiseptic** (germicide) is a chemical agent that kills or inhibits microorganisms and is sufficiently nontoxic to be applied to living tissues.

Chemical *sterilants* (sterilizing agents) destroy all microorganisms including endospores, given enough time; they are used for "cold sterilization" of heat-sensitive devices such as endoscopes, catheters and plastic tubing. *Sanitizers* are milder and are used on food-contact surfaces. The same substance can belong to several groups depending on concentration and contact time: hydrogen peroxide is an antiseptic at $3\,\%$ and a sterilant as a vapor; glutaraldehyde disinfects in $20$ minutes and sterilizes in about $10$ hours. In hospitals the level of treatment is chosen by the risk of the item (the Spaulding classification): items that enter sterile tissue must be sterile, items that contact mucous membranes need high-level disinfection, and items that touch only intact skin need low-level disinfection.

| Class | Examples | Mechanism | Uses and limits |
|---|---|---|---|
| Alcohols | ethanol, isopropanol, $60$–$90\,\%$ in water | denature proteins, dissolve membrane lipids | skin antisepsis, hand rubs, surfaces; rapid; not sporicidal; water is needed (absolute alcohol is less effective) |
| Aldehydes | glutaraldehyde ($2\,\%$), *ortho*-phthalaldehyde, formaldehyde | alkylate amino and thiol groups of proteins and nucleic acids | high-level disinfection and chemical sterilization of instruments; toxic, irritant |
| Phenolics and bisphenols | phenol, cresols, chloroxylenol, triclosan, hexachlorophene | disrupt membranes, denature proteins (triclosan at low concentration also inhibits fatty acid synthesis) | surfaces, soaps, antiseptics; phenol historically (Lister) |
| Biguanides | chlorhexidine | binds and disrupts membranes | skin and mouth antisepsis; persists on skin |
| Halogens | chlorine, hypochlorite, chloramines, chlorine dioxide; iodine, iodophors (povidone-iodine) | oxidize thiols and other groups; iodinate proteins | drinking water, bleach for surfaces; iodophors for skin; inactivated by organic matter |
| Peroxygens | hydrogen peroxide, peracetic acid, ozone | oxidize, through hydroxyl radicals | surfaces, sterilization (vapor, plasma), water; residues harmless |
| Quaternary ammonium compounds | benzalkonium chloride, cetylpyridinium | cationic detergents that disrupt membranes | surfaces, food equipment, mild antiseptics; weak against spores, mycobacteria and nonenveloped viruses; neutralized by soaps and organic matter |
| Heavy metals | silver, copper; mercury compounds (historical) | bind thiol groups of proteins | silver in wound dressings, copper sulfate as algicide; mostly static |
| Gases | ethylene oxide, β-propiolactone; formaldehyde vapor | alkylate proteins and nucleic acids | sterilization of heat-sensitive plastics and devices; ethylene oxide is explosive and carcinogenic, items must be aerated |

Water disinfection relies mostly on chlorine, which reacts with water to form hypochlorous acid; this uncharged acid ($\mathrm{p}K_{\mathrm{a}} \approx 7.5$) penetrates cells and is a far stronger germicide than the hypochlorite ion, so chlorination is more effective at slightly acidic than at alkaline pH. Chlorine is harmless to humans at the concentrations used (below a few milligrams per liter) and leaves a residual that protects the distribution system, but it reacts with organic matter to form disinfection by-products, and the oocysts of *Cryptosporidium* resist it, which is why many plants add ultraviolet treatment or ozone.

### 10.4.3. The Kinetics of Disinfection

Chemical killing, like heat killing, is often approximately first order, with a rate that increases with the concentration of the agent. Chick (1908) found the first-order form, and Watson (1908) the dependence on concentration.

**Formula 10.4.1 (Chick–Watson Law)** For a disinfectant at constant concentration $C$, the survivors after contact time $t$ obey

$$
\ln\frac{N}{N_0} = -k\,C^n t, \tag{10.5}
$$
where $k$ is a rate constant characteristic of the agent and the organism and $n$ the dilution coefficient. A given kill is therefore achieved when $C^n t$ reaches a fixed value; for $n = 1$, when the product $Ct$ does.

The *Ct value*, the product of concentration (in $\mathrm{mg\,L^{-1}}$) and contact time (in minutes) needed for a given log reduction, is used to design the disinfection of drinking water. The coefficient $n$ shows how much the efficacy of an agent depends on dilution (figure below, panel B): for chlorine $n$ is close to $1$, so halving the concentration doubles the time needed; for phenol and alcohols $n$ is large (about $6$ for phenol and about $9$ for ethanol), so even modest dilution makes them almost ineffective, which is why alcohol solutions must not be weakened and why disinfectant solutions must be prepared at the stated concentration.

### 10.4.4. What Determines Efficacy

The effect of a chemical agent depends on

- the concentration and the contact time (Formula 10.4.1), and the temperature, since the rate increases with temperature;
- the pH, which changes the charge of the agent or of the cell surface (hypochlorous acid against hypochlorite; quaternary ammonium compounds are more active at alkaline pH);
- organic matter, such as blood, pus, soil or food residues, which reacts with or adsorbs many agents, especially chlorine and quaternary ammonium compounds, so that surfaces must be cleaned before they are disinfected;
- the state of the organisms: the number present, whether they are dried onto a surface or embedded in a **biofilm**, whose matrix slows penetration and whose cells may be in a tolerant physiological state, often making them hundreds of times harder to kill than suspended cells ([7.11.12](/7.11.12));
- and above all the kind of organism.

Microorganisms and other infectious agents differ in their resistance to chemicals in a fairly consistent order (panel C). Enveloped viruses, whose lipid envelope is easily disrupted, and vegetative bacteria are the most sensitive; fungi, small nonenveloped viruses such as poliovirus and norovirus, the mycobacteria, whose waxy outer layer of mycolic acids ([7.11.18](/7.11.18)) excludes aqueous agents, and the oocysts of protozoa such as *Cryptosporidium* are progressively more resistant; bacterial endospores, dehydrated, encased in their coats and with protected DNA, are the most resistant cells. Only sterilants such as aldehydes, peroxygens and ethylene oxide kill spores reliably.

![Chemical disinfection. A: the Chick–Watson law for a disinfectant at three concentrations (dilution coefficient n = 1, illustrative rate constant): survival falls exponentially at a rate proportional to the concentration. B: the time needed for a 99 % kill against concentration on log–log axes has slope −n: for n = 1 the product Ct is constant, for n = 2 a twofold dilution makes the agent four times slower. C: the approximate order of resistance of microorganisms and infectious agents to chemical disinfectants; the order of neighboring groups varies with the agent](./plots/disinfection.py)

### 10.4.5. Prions

At the top of the resistance order are not organisms but **prions**, the infectious misfolded proteins that cause transmissible spongiform encephalopathies such as Creutzfeldt–Jakob disease in humans, scrapie in sheep and bovine spongiform encephalopathy in cattle ([7.11.26](/7.11.26)). Their aggregated, β-sheet-rich protein resists the standard autoclave cycle, ionizing and ultraviolet radiation and the aldehydes, which even stabilize it. Iatrogenic transmission of Creutzfeldt–Jakob disease by neurosurgical instruments, electrodes and grafts led to special procedures for instruments that may have been in contact with high-risk tissue: prolonged autoclaving at $134\,^\circ\mathrm{C}$ (for example $18$ minutes), immersion in $1\,\mathrm{M}$ sodium hydroxide or in concentrated sodium hypochlorite (about $20\,000$ ppm available chlorine), often combined, or disposal of single-use instruments by incineration.

## Summary

- **Sterilization** removes all microorganisms, **disinfection** pathogens on objects, **antisepsis** microorganisms on living tissue (Definition 10.1.1). Static agents inhibit, cidal agents kill, lytic agents kill by lysis (Definition 10.1.2); they are distinguished by viable and total counts.
- Heat kills exponentially: $N = N_0 10^{-t/D}$ (Formula 10.2.1), with the **decimal reduction time** $D$ (Definition 10.2.1). $D$ falls tenfold per $z$ degrees (Formula 10.2.2); the lethality $F_0$ of a process is the equivalent time at $121.1\,^\circ\mathrm{C}$ (Formula 10.2.3). Low-acid canned food receives a 12D botulinum cook ($F_0 \ge 3\,\mathrm{min}$); sterility is a probability.
- The autoclave sterilizes with steam at $121\,^\circ\mathrm{C}$ for about $15$ minutes once the load is hot, provided air is removed; dry heat needs $160$–$170\,^\circ\mathrm{C}$ for one to two hours; tyndallization sterilizes by repeated heating; **pasteurization** (Definition 10.2.2: $63\,^\circ\mathrm{C}$ for $30$ min, $72\,^\circ\mathrm{C}$ for $15$ s; UHT $135$–$140\,^\circ\mathrm{C}$) kills pathogens without sterilizing.
- Ultraviolet light forms pyrimidine dimers and acts only on surfaces, air and clear water; ionizing radiation penetrates and sterilizes packaged items; survival curves may have a shoulder (Formula 10.3.1), and $D_{10}$ values show spores and viruses to be more resistant than vegetative cells.
- Membrane filters with $0.2\,\mu\mathrm{m}$ pores sterilize heat-sensitive liquids but do not remove viruses and some mycoplasmas; HEPA filters clean air.
- **Disinfectants** and **antiseptics** (Definition 10.4.1) and sterilants act by denaturation, alkylation, oxidation or membrane disruption. Killing follows the Chick–Watson law $\ln(N/N_0) = -kC^nt$ (Formula 10.4.1); efficacy depends on concentration, time, temperature, pH, organic matter, biofilms and the organism, with resistance increasing from enveloped viruses and vegetative bacteria to mycobacteria, oocysts, endospores and **prions**.

## Questions

1. A suspension contains $10^8$ spores per milliliter with $D_{121} = 1.5\,\mathrm{min}$. How long must it be held at $121\,^\circ\mathrm{C}$ to reach $10^{-6}$ surviving spores per milliliter? How long at $111\,^\circ\mathrm{C}$ if $z = 10\,^\circ\mathrm{C}$? Why is it misleading to speak of "the time that kills all spores"?

   **Answer** $\log_{10}(10^8/10^{-6}) = 14$ decimal reductions: $14 \times 1.5 = 21\,\mathrm{min}$ at $121\,^\circ\mathrm{C}$. At $111\,^\circ\mathrm{C}$, $D = 15\,\mathrm{min}$, so $210\,\mathrm{min}$. Because killing is exponential, the number of survivors never becomes exactly zero; it only becomes a small expected number, so sterility must be stated as a probability of survival, and the time needed depends on the initial number.

2. Explain why a $2\,\mathrm{L}$ flask of medium autoclaved for $15$ minutes may not be sterile, and why an autoclave with trapped air may fail even when its gauge shows $121\,^\circ\mathrm{C}$.

   **Answer** The $15$ minutes refer to the time at $121\,^\circ\mathrm{C}$ of the material itself; a large volume of liquid takes a long time to heat, so its center may spend only a few minutes near $121\,^\circ\mathrm{C}$, giving too little lethality ($F_0$) for its spores. An air–steam mixture at a given pressure has a lower temperature than saturated steam, and air pockets prevent steam from contacting surfaces and condensing on them, so parts of the load stay cooler than the chamber sensor; air removal is therefore essential.

3. Compare low-temperature long-time pasteurization, high-temperature short-time pasteurization and UHT treatment of milk. Why can higher temperatures for shorter times give a safer and better-tasting product?

   **Answer** LTLT ($63\,^\circ\mathrm{C}$, $30\,\mathrm{min}$) and HTST ($72\,^\circ\mathrm{C}$, $15\,\mathrm{s}$) kill vegetative pathogens such as *Mycobacterium bovis* and *Coxiella burnetii* but not spores, so the milk must be refrigerated; UHT ($135$–$140\,^\circ\mathrm{C}$, a few seconds) kills spores and, with aseptic packaging, gives a shelf-stable product. Microbial killing has a small $z$ value (about $10\,^\circ\mathrm{C}$ for spores, less for vegetative cells), whereas the chemical reactions that degrade flavor and vitamins have larger $z$ values ($25$–$40\,^\circ\mathrm{C}$): raising the temperature accelerates killing much more than damage, so the same kill is reached with less damage.

4. A hospital disinfectant with a dilution coefficient $n = 4$ kills a test organism by $5$ log units in $10$ minutes at its recommended concentration. A worker dilutes it twofold to save money. What contact time is now needed? For hypochlorite ($n \approx 1$)?

   **Answer** By the Chick–Watson law the required time scales as $C^{-n}$: halving $C$ multiplies it by $2^4 = 16$, to $160$ minutes, so the diluted disinfectant is practically useless in normal contact times. For hypochlorite, $2^1 = 2$: $20$ minutes. Agents with large $n$ (phenolics, alcohols) must be used at the stated concentration.

5. Rank the following by resistance to a quaternary ammonium disinfectant and explain the two extremes: influenza virus, *Staphylococcus aureus*, poliovirus, *Mycobacterium tuberculosis*, spores of *Bacillus subtilis*. Which agent would you use for an endoscope that has been used on a patient with tuberculosis?

   **Answer** From most sensitive to most resistant: influenza virus (enveloped) < *S. aureus* (vegetative bacterium) < poliovirus (small, nonenveloped) < *M. tuberculosis* < *B. subtilis* spores. Quaternary ammonium compounds are cationic detergents that disrupt lipid membranes, so the lipid envelope of influenza is destroyed easily; spores are dehydrated, have impermeable coats and protected DNA and are barely affected (quaternary ammonium compounds are at most sporostatic). An endoscope (a semicritical item) needs high-level disinfection with an agent active against mycobacteria, such as glutaraldehyde, *ortho*-phthalaldehyde or peracetic acid, after thorough cleaning.
