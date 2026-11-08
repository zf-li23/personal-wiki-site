---
title: Environmental Effects on Growth
description: "How the physical and chemical environment limits microbial growth: cardinal temperatures and the asymmetry of the growth–temperature curve; psychrophiles, mesophiles, thermophiles and hyperthermophiles; molecular adaptations to cold (flexible enzymes, fluid membranes, cold shock and antifreeze proteins) and to heat (stable proteins, saturated and ether lipids, reverse gyrase, DNA-binding proteins, compatible solutes) and the upper temperature limit of life; acidophiles, neutrophiles and alkaliphiles and the maintenance of internal pH; water activity, halophiles, osmophiles and xerophiles, compatible solutes and the salt-in strategy; the oxygen classes, thioglycolate tubes and anaerobic culture, reactive oxygen species and superoxide dismutase, catalase, peroxidase and superoxide reductase; pressure and piezophiles; radiation."
---

Even in a medium that supplies every nutrient, a microorganism grows only if the physical and chemical state of its surroundings lies within limits it can tolerate. Four factors dominate: temperature, pH, the availability of water and oxygen; pressure and radiation matter in particular habitats. For each factor every organism has a range in which it can grow and an optimum within that range, and organisms are classified by where their optimum lies. The ranges are narrow for any one species, often less than $40$ degrees of temperature or three pH units, but taken together microorganisms grow from below $-10\,^\circ\mathrm{C}$ to above $120\,^\circ\mathrm{C}$, from pH $0$ to pH $11$, in saturated brine and without any oxygen. Organisms that grow optimally at the extremes, the **extremophiles**, are the subject of much of this chapter, both because they show how far the chemistry of life can be pushed and because their enzymes are useful.

The growth rate whose dependence on the environment is described here is the exponential growth rate of [7.11.8](/7.11.8). The physical chemistry behind the adaptations, such as membrane fluidity, protein stability and osmotic pressure, is treated in [7.1.12](/7.1.12), [7.6.16](/7.6.16) and [7.6.24](/7.6.24); the DNA damage caused by radiation and its repair in [7.2.8](/7.2.8). The archaea that hold most of the records are described in [7.11.19](/7.11.19), the killing of microorganisms by heat, radiation and chemicals in [7.11.10](/7.11.10), and the deep sea and other extreme habitats in [7.11.29](/7.11.29).

## 9.1. Temperature

### 9.1.1. Cardinal Temperatures

Temperature acts on growth in two opposite ways. As it rises, chemical and enzymatic reactions become faster and growth accelerates; above some temperature, however, proteins, nucleic acids or the membrane are damaged irreversibly and growth stops. Every organism therefore has three *cardinal temperatures*: a minimum below which it cannot grow, an optimum at which it grows fastest, and a maximum above which it cannot grow. The maximum reflects the denaturation of one or more essential components. The minimum is usually set by the membrane, which must remain fluid enough for transport and for generating a **proton-motive force**; below it the membrane gels. The optimum lies closer to the maximum than to the minimum, so the growth rate rises gradually with temperature and falls steeply just above the optimum (figure below). For *Escherichia coli* the cardinal temperatures are about $8$, $39$ and $48\,^\circ\mathrm{C}$; the range of about $40$ degrees is typical, and no organism grows over a much wider one. The cardinal temperatures of a strain are not fixed: *E. coli* grows at a somewhat higher temperature in a rich medium than in a minimal one, because at high temperature some biosynthetic enzymes become limiting first.

The asymmetry has a simple explanation. The rates of the cell's reactions increase roughly exponentially with temperature (the Arrhenius law, with activation energies of typically $50$–$80\,\mathrm{kJ\,mol^{-1}}$), whereas the unfolding of a protein is highly cooperative, with an enthalpy of unfolding of hundreds of kilojoules per mole, so that the fraction of folded protein falls from nearly one to nearly zero within a few degrees of its melting temperature ([7.6.16](/7.6.16)). The product of a slowly rising and a sharply falling factor has its maximum close to the point where the second begins to fall (panel B).

**Definition 9.1.1 (Temperature Classes)** By their optimum growth temperature, microorganisms are classified as

- **psychrophiles**, with an optimum of $15\,^\circ\mathrm{C}$ or lower, a maximum below about $20\,^\circ\mathrm{C}$ and a minimum of $0\,^\circ\mathrm{C}$ or lower;
- *mesophiles*, with optima in the middle range, about $20$–$45\,^\circ\mathrm{C}$;
- **thermophiles**, with optima between $45$ and $80\,^\circ\mathrm{C}$;
- **hyperthermophiles**, with optima above $80\,^\circ\mathrm{C}$.

Organisms that can grow at $0\,^\circ\mathrm{C}$ but have optima of $20$–$40\,^\circ\mathrm{C}$ are called *psychrotolerant*.

Mesophiles are the commonest and best-studied microorganisms: they live in warm-blooded animals and in soil and water of temperate and tropical regions, and most pathogens of humans are mesophiles. The class boundaries are conventions; growth temperatures form a continuum.

![Temperature and growth. A: growth rate against temperature for the four temperature classes (cardinal temperature model with inflection; curves scaled to 1 at the optimum): a psychrophile (minimum, optimum and maximum −5, 10 and 18 °C, illustrative), the mesophile *Escherichia coli* (8, 39 and 48 °C), a thermophile (40, 63 and 75 °C, illustrative) and the hyperthermophile *Pyrolobus fumarii* (90, 106 and 113 °C). Each curve rises gradually and falls steeply above the optimum. B: a toy model of the asymmetry: reaction rates rise with temperature (Arrhenius, activation energy 60 kJ/mol, dashed) while the fraction of an essential protein that is folded collapses near its melting temperature (two-state unfolding, dotted); their product, the growth rate, peaks a few degrees below the maximum](./plots/cardinal-temperatures.py)

### 9.1.2. Life in the Cold

Most of the Earth is cold. The oceans, which cover more than two-thirds of its surface, have an average temperature of about $5\,^\circ\mathrm{C}$, and the deep ocean is at $1$–$3\,^\circ\mathrm{C}$ throughout the year; polar regions, glaciers, permafrost and the high mountains add to the cold biosphere. Constantly cold habitats, such as sea ice, Antarctic lakes under permanent ice cover and glacier channels, harbor psychrophiles; seasonally cold ones, which warm up in summer, are dominated by psychrotolerant organisms. Psychrophilic algae and bacteria grow in dense layers in and under sea ice, and snow algae color the surface of snowfields red, green or orange with carotenoids; the classic red snow alga, named *Chlamydomonas nivalis*, accumulates the red carotenoid astaxanthin in its resting cells. The gas-vesiculate bacterium *Polaromonas vacuolata* from Antarctic sea ice grows optimally at $4\,^\circ\mathrm{C}$. The lowest temperature at which growth of a bacterium has been documented is $-15\,^\circ\mathrm{C}$, for *Planococcus halocryophilus* from Arctic permafrost (Mykytczuk et al. 2013), and metabolic activity has been measured at still lower temperatures in thin films of liquid water within frozen material. Strict psychrophiles can be killed by warming to room temperature, so they must be kept cold from sampling to the laboratory.

Psychrotolerant bacteria, by contrast, are found in temperate soils and water and in refrigerated food: they grow slowly at $4\,^\circ\mathrm{C}$ but much faster at $30\,^\circ\mathrm{C}$. They are the main agents of spoilage of chilled meat, milk and vegetables, and the pathogen *Listeria monocytogenes*, which can multiply in a refrigerator, makes refrigeration alone an insufficient safeguard for ready-to-eat foods.

Psychrophiles have adapted the same components that limit the minimum growth temperature:

- Enzymes. Cold-active enzymes are more flexible, which keeps them catalytically active at temperatures where the enzymes of mesophiles are too rigid. Compared with their mesophilic counterparts they tend to have more α-helix and less β-sheet, more polar and fewer hydrophobic residues, fewer salt bridges and hydrogen bonds, and more glycine; as a consequence many are denatured at moderate temperatures.
- Membranes. Psychrophiles keep their membranes fluid with more unsaturated, shorter-chain and branched **fatty acids**, and some contain polyunsaturated fatty acids. Mesophiles make the same kind of change when grown at lower temperature, a response called homeoviscous adaptation (Sinensky 1974).
- Protecting RNA, proteins and membranes. Cold shock proteins, small nucleic-acid-binding proteins such as CspA of *E. coli*, act as RNA chaperones that melt secondary structures in mRNA which would otherwise block translation in the cold. Cryoprotectants prevent damage by ice: antifreeze (ice-binding) proteins, solutes such as glycerol and sugars made in large amounts in the cold, and thick layers of exopolysaccharide.

Freezing does not necessarily kill cells. Bacteria suspended in medium with $10\,\%$ dimethyl sulfoxide or glycerol and frozen at $-80\,^\circ\mathrm{C}$ or in liquid nitrogen ($-196\,^\circ\mathrm{C}$) remain viable for years, which is how culture collections store them; slow freezing without such protectants kills many cells by ice crystals and by the concentration of solutes.

### 9.1.3. Life at High Temperatures

Thermophiles live in sun-heated soil, compost piles and silage (which can reach $70\,^\circ\mathrm{C}$), hot water heaters and the effluents of power plants. Hyperthermophiles live in hot springs at or near boiling and in deep-sea hydrothermal vents, whose fluids may emerge at $350\,^\circ\mathrm{C}$ and stay liquid under the pressure of the water column. As the water flowing out of a boiling spring cools, it sets up a thermal gradient along which different organisms establish themselves at different temperatures, and such gradients revealed the upper limits of the major groups (figure below, panel A). Hyperthermophiles grow surprisingly fast in their springs, with generation times of about an hour, as shown by immersing microscope slides in the spring and following the microcolonies that form on them.

![Temperature limits and the osmotic response. A: upper temperature limits for growth of groups of organisms (data from Madigan et al. 2019; where a range is given, the thick bar marks it): eukaryotes stop at about 60 °C, oxygenic and anoxygenic phototrophs at 70–73 °C, chemotrophic Bacteria at 95 °C and Archaea at 122 °C. B: the two-stage response of *Escherichia coli* to a sudden rise of external osmolarity (model curves, arbitrary units): K⁺ is taken up within minutes with glutamate as its counterion, then glycine betaine taken up from the medium replaces much of the K⁺ glutamate over the following hour, and growth resumes (Section 9.3.3)](./plots/limits-osmotic-response.py)

Above about $65\,^\circ\mathrm{C}$ only prokaryotes thrive, and above about $95\,^\circ\mathrm{C}$ only archaea; some hyperthermophilic archaea have optima above $100\,^\circ\mathrm{C}$ and must be cultured in pressurized vessels. The current record is held by the methanogen *Methanopyrus kandleri*, strain 116 of which grew at $122\,^\circ\mathrm{C}$ under high pressure (Takai et al. 2008). The ultimate limit is probably set by the stability of small molecules: ATP and NAD hydrolyze within minutes at $150\,^\circ\mathrm{C}$, and many expect the upper limit of life to lie somewhere between $122$ and $150\,^\circ\mathrm{C}$.

Thermophiles and hyperthermophiles stabilize the same components that fail at high temperature (the archaeal cases are treated in [7.11.19](/7.11.19)):

- Proteins. Their enzymes are intrinsically more stable and often work best near the organism's growth temperature, through small changes of amino acid sequence: more ionic bonds (salt bridges) between basic and acidic residues on the surface, more tightly packed hydrophobic cores, shorter loops, and fewer residues that are chemically labile at high temperature (asparagine, glutamine, cysteine). Chaperonins refold proteins damaged by heat. Some hyperthermophiles accumulate solutes that stabilize proteins, such as di-*myo*-inositol phosphate, diglycerol phosphate, mannosylglycerate or, in *Methanopyrus*, more than $1\,\mathrm{M}$ potassium cyclic 2,3-diphosphoglycerate.
- Membranes. Thermophilic bacteria have more saturated, longer-chain fatty acids, which form a more stable hydrophobic core. Most hyperthermophiles are archaea, whose ether-linked isoprenoid lipids resist hydrolysis, and many of which have tetraether lipids spanning the whole membrane as a monolayer that cannot peel apart ([7.11.2](/7.11.2)).
- DNA. At $100\,^\circ\mathrm{C}$ an unprotected double helix of moderate GC content would melt. Hyperthermophiles have an enzyme found in no mesophile, *reverse gyrase*, a type I topoisomerase that introduces positive supercoils and thereby stabilizes the duplex; they have small DNA-binding proteins (Sac7d and Sso7d in *Sulfolobus*) or archaeal **histones** that compact and protect the DNA, and high intracellular concentrations of K⁺ and of the solutes listed above. The GC content of the genome does not correlate with growth temperature, but that of the stems of ribosomal RNAs does: more GC pairs, with three hydrogen bonds, stabilize the RNA structures.

Heat-stable enzymes have many commercial uses, because they work at high temperatures and keep longer. The classic example is the DNA polymerase of *Thermus aquaticus*, a thermophile isolated from a hot spring in Yellowstone National Park by Brock and Freeze (1969): Taq polymerase survives the denaturation steps of the **polymerase chain reaction**, which made the automation of PCR possible ([7.2.5](/7.2.5#sec-5.6.1)). Others are proteases, amylases and pullulanases from thermophiles used in detergents and in starch processing, and proofreading polymerases from hyperthermophilic archaea such as *Pyrococcus* used for high-fidelity PCR.

## 9.2. pH

### 9.2.1. Acidophiles, Neutrophiles and Alkaliphiles

pH is the negative logarithm of the hydrogen-ion activity; a change of one unit is a tenfold change in $\mathrm{H^+}$. As with temperature, each organism grows over a range, typically two to three pH units, and has an optimum. Most natural environments have a pH between $3$ and $9$.

**Definition 9.2.1 (pH Classes)** Organisms that grow best at pH $5.5$ to $7.9$ (circumneutral pH) are *neutrophiles*; those that grow best below pH $5.5$ are **acidophiles**, and those with optima of pH $8$ or higher are **alkaliphiles**.

*E. coli* is a neutrophile. Many fungi grow best at pH $5$ or below, fewer organisms below pH $3$, and very few below pH $2$ (figure below, panel A). In strong acidophiles high proton concentrations are required for the stability of the membrane, and the cells lyse at neutral pH. The most acidophilic organism known, the archaeon *Picrophilus oshimae* from acidic volcanic soils, grows optimally at pH $0.7$ and $60\,^\circ\mathrm{C}$ and lyses spontaneously above pH $4$. Acidophilic chemolithotrophs such as *Acidithiobacillus ferrooxidans*, which oxidize iron and sulfur compounds and produce sulfuric acid themselves, create the acidic, metal-rich waters of mine drainage and are used to leach copper and other metals from low-grade ores ([7.11.7](/7.11.7)). Alkaliphiles live in soda lakes and carbonate-rich soils, at pH up to $10$–$11$; some, mostly archaea, are also extreme halophiles. Alkaliphilic *Bacillus* species excrete proteases and lipases that remain active at high pH and are added to laundry detergents.

### 9.2.2. Internal pH

The pH optimum refers to the outside of the cell. The cytoplasm must be kept close to neutrality, because the macromolecules inside are stable only over a limited range, roughly pH $5$ to $9$ and for most cells $6.5$ to $8$. Acidophiles and alkaliphiles therefore maintain a large pH difference across their membranes, by opposite means:

- Acidophiles have membranes of low proton permeability, pump protons out, and reverse the membrane potential (inside positive, largely by taking up K⁺), which slows the entry of protons. The resulting large $\Delta\mathrm{pH}$ is itself the main component of their proton-motive force.
- Alkaliphiles face the opposite problem: protons are scarce outside, and the pH gradient across the membrane points the wrong way for a proton-motive force. They import protons by Na⁺/H⁺ antiporters, which keeps the cytoplasm about two units below the outside, and use a sodium-motive force to drive transport and to rotate their flagella. Many nevertheless make ATP with a proton-driven ATP synthase, which is still not fully understood; protons appear to be kept close to the outer surface of the membrane.

Microbial growth itself changes the pH, because fermentation acids accumulate and ammonia is released from amino acids. Culture media are therefore buffered, for neutrophiles commonly with phosphate or bicarbonate; organic buffers such as HEPES, MES and Tris cover other ranges. The response of enteric bacteria to acid in the stomach, by acid-induced amino acid decarboxylases that consume protons, is part of their pathogenesis ([7.11.33](/7.11.33)).

![pH, salt and water activity. A: pH optima of example organisms on the pH scale, with the classes acidophile (optimum below pH 5.5), neutrophile and alkaliphile (optimum pH 8 or higher); the cytoplasm is kept near neutrality whatever the external pH (box, schematic). Data from Madigan et al. (2019): *Picrophilus oshimae* 0.7, *Acidithiobacillus ferrooxidans* 3, *Rhodopila globiformis* 5, *Escherichia coli* 7, *Chloroflexus aurantiacus* 8, *Natronobacterium gregoryi* 10. B: growth rate against NaCl concentration for the four salt classes (illustrative curves): a nonhalophile such as *E. coli*, a halotolerant organism such as *Staphylococcus aureus*, a halophile such as the marine *Aliivibrio fischeri* (optimum near 3 %) and an extreme halophile such as *Halobacterium* (optimum 15–30 %). C: water activity of common materials and the lowest water activity known to allow growth (data from Madigan et al. 2019); right: water activity of NaCl solutions computed from their osmotic coefficients, which reaches about 0.75 at saturation, the value of salt lakes and salted fish](./plots/ph-salt-water.py)

## 9.3. Water Activity and Osmotic Stress

### 9.3.1. Water Activity

Water is the solvent of life, and its availability depends not only on whether an environment is wet or dry but also on the solutes dissolved in the water. Solutes bind water and lower its chemical potential, so that water tends to move from a dilute to a concentrated solution, the process of **osmosis**.

**Definition 9.3.1 (Water Activity)** The **water activity** $a_{\mathrm{w}}$ of a solution or material is the ratio of the vapor pressure of water in equilibrium with it to the vapor pressure of pure water at the same temperature, $a_{\mathrm{w}} = p/p^*$. It ranges from $0$ (no free water) to $1$ (pure water).

Water activity is the thermodynamic activity of water: its chemical potential is $\mu_{\mathrm{w}} = \mu_{\mathrm{w}}^* + RT\ln a_{\mathrm{w}}$, and a solution of water activity $a_{\mathrm{w}}$ has the **osmotic pressure** $\Pi = -(RT/V_{\mathrm{m,w}})\ln a_{\mathrm{w}}$, with $V_{\mathrm{m,w}}$ the molar volume of water. For dilute solutions $a_{\mathrm{w}}$ is close to the mole fraction of water (Raoult's law); for electrolytes it is computed from the osmotic coefficient $\phi$ as $\ln a_{\mathrm{w}} = -\nu m \phi M_{\mathrm{w}}$, where $m$ is the molality, $\nu$ the number of ions per formula unit and $M_{\mathrm{w}}$ the molar mass of water ([6.3](/6.3)).

**Example 9.3.1** Seawater contains about $3\,\%$ NaCl, about $0.5\,\mathrm{mol\,kg^{-1}}$; with $\nu = 2$ and $\phi \approx 0.92$, $\ln a_{\mathrm{w}} = -2 \times 0.5 \times 0.92 \times 0.018 = -0.017$, so $a_{\mathrm{w}} \approx 0.98$. A saturated NaCl solution ($6.1\,\mathrm{mol\,kg^{-1}}$, $\phi \approx 1.27$) has $a_{\mathrm{w}} \approx 0.75$. The osmotic pressure of seawater is $\Pi = (8.314 \times 298/1.8\times10^{-5}) \times 0.017 \approx 2.4\,\mathrm{MPa}$, about $24$ times atmospheric pressure.

:::

Because the cytoplasm normally contains more solutes than the surroundings, water tends to flow into the cell, which is said to be in positive water balance; the wall bears the resulting turgor pressure. If the outside becomes more concentrated than the inside, water flows out, the cytoplasm shrinks away from the wall (plasmolysis), and the cell cannot grow. The water activities of some materials are shown in the figure above (panel C): seawater $0.98$, bread $0.95$, salami $0.85$, jams $0.80$, salt lakes and salted fish $0.75$, cereals and dried fruit $0.70$. The lowest water activity at which growth has been observed, about $0.61$, belongs to xerophilic fungi such as *Xeromyces bisporus* growing on sugary substrates; it seems to be a physicochemical limit common to all three domains. This is the basis of the oldest methods of food preservation, salting, sugaring and drying.

### 9.3.2. Salt and Sugar Classes

**Definition 9.3.2 (Halophiles and Related Classes)** Microorganisms that require NaCl for growth and grow best at elevated NaCl concentrations are **halophiles**; marine organisms typically need $1$–$4\,\%$ NaCl, and those that need $15$–$30\,\%$ NaCl for optimal growth are **extreme halophiles**. *Halotolerant* organisms tolerate reduced water activity but grow best without added solute. Organisms that grow in high concentrations of sugar are *osmophiles*, and those that grow in very dry environments are *xerophiles*.

The NaCl requirement of halophiles is specific and cannot be met by KCl or other salts (panel B). Seawater organisms such as *Vibrio* and *Aliivibrio fischeri* grow best near $3\,\%$; organisms from hypersaline lagoons and salterns grow best at $3$–$12\,\%$; extreme halophiles, among them the haloarchaea (*Halobacterium*, *Halococcus*) and the bacterium *Salinibacter ruber*, grow in salt lakes, salterns and salted fish up to saturation and are often unable to grow below $15\,\%$ ([7.11.19](/7.11.19)). *Staphylococcus aureus*, which is halotolerant, grows well at $7.5$–$10\,\%$ NaCl, which is used in media that select it from skin samples ([7.11.8](/7.11.8)). Osmophilic yeasts such as *Zygosaccharomyces* spoil jams, syrups and honey, and xerophilic molds grow on dried foods.

### 9.3.3. Compatible Solutes and the Salt-In Strategy

To keep positive water balance in a medium of low water activity, a cell must raise the concentration of solutes in its cytoplasm. Inorganic salts are not suitable for most cells, because high concentrations of ions disturb the structure and interactions of proteins and nucleic acids.

**Definition 9.3.3 (Compatible Solute)** A **compatible solute** is a highly soluble, usually uncharged or zwitterionic, low-molecular-weight compound that a cell accumulates to high concentration in its cytoplasm, by synthesis or uptake, to balance external osmotic pressure without inhibiting its biochemical processes.

| Organism | Main compatible solutes | Lowest $a_{\mathrm{w}}$ for growth |
|---|---|---|
| Most nonphototrophic bacteria (*Escherichia*), freshwater cyanobacteria | amino acids (glutamate, proline); sucrose, trehalose | 0.98 |
| Marine cyanobacteria (*Synechococcus*) | α-glucosylglycerol | 0.92 |
| Marine algae | mannitol, glycosides, proline, dimethylsulfoniopropionate | 0.92 |
| Halotolerant bacteria (*Staphylococcus*) | amino acids, glycine betaine | 0.90 |
| Salt-lake cyanobacteria (*Aphanothece*) | glycine betaine | 0.75 |
| Halophilic phototrophic purple bacteria | glycine betaine, ectoine, trehalose | 0.75 |
| Extremely halophilic archaea (*Halobacterium*) | KCl | 0.75 |
| Halophilic green alga *Dunaliella* | glycerol | 0.75 |
| Xerophilic fungi (*Xeromyces*) | glycerol | 0.61 |

The table summarizes data from Madigan et al. (2019). Compatible solutes include amino acids and their derivatives (glycine betaine, an *N*-trimethylated glycine; ectoine, a cyclic amino acid; proline), sugars (sucrose, trehalose), polyols (glycerol, mannitol) and sulfonium compounds such as dimethylsulfoniopropionate, made in large amounts by marine algae, whose breakdown releases dimethyl sulfide to the atmosphere ([7.11.30](/7.11.30)). They are excluded from the surfaces of proteins, which favors the compact native state, so that many of them also stabilize enzymes against heat, freezing and drying; ectoine and trehalose are used for this reason in cosmetics and to preserve biological materials. The maximal amount of compatible solute that an organism can make or accumulate is genetically determined, and this is what places it in one of the salt classes.

The response of *E. coli* to a sudden rise in osmolarity has two stages. Within minutes the cell takes up K⁺ (by the Trk and Kdp systems) and makes glutamate as its counterion; then, over the next hour, it replaces this ionic solution with compatible solutes (figure in Section 9.1.3, panel B), by importing glycine betaine or proline from the medium (by ProP and ProU) or by synthesizing trehalose. When the outside becomes suddenly dilute, as when a soil bacterium is caught in rain, water rushes in, and mechanosensitive channels in the membrane (MscS and MscL) open under tension and release solutes before the cell bursts ([7.6.25](/7.6.25)).

The extremely halophilic archaea and a few bacteria (*Salinibacter*, the Halanaerobiales) use another strategy, called salt-in: they accumulate KCl in the cytoplasm to concentrations that match the external NaCl, with K⁺ often above $4\,\mathrm{M}$. This saves the energy cost of making organic solutes, but it requires that the whole proteome be adapted to high salt: their proteins are rich in acidic amino acids (glutamate and aspartate) on the surface, which keep them hydrated and soluble at high ionic strength, and many of them denature in dilute solution. These organisms are therefore obligately halophilic.

## 9.4. Oxygen

### 9.4.1. The Oxygen Classes

Oxygen is required by some microorganisms, used by others when available, and lethal to still others. Air contains $21\,\%$ $\mathrm{O_2}$, but $\mathrm{O_2}$ is poorly soluble in water (about $0.25\,\mathrm{mM}$ at $25\,^\circ\mathrm{C}$) and diffuses slowly, so that wherever respiration consumes it faster than it is supplied, anoxic conditions arise: in muds, sediments, bogs, waterlogged soils, the intestines of animals, sewage sludge, the interior of biofilms, and even within soil aggregates a few millimeters across.

**Definition 9.4.1 (Oxygen Classes)** According to their relationship to $\mathrm{O_2}$, microorganisms are classified as

- *obligate aerobes*, which require $\mathrm{O_2}$ and grow at full oxygen tension, respiring it;
- **microaerophiles**, aerobes that require $\mathrm{O_2}$ but grow only at concentrations lower than in air;
- **facultative anaerobes**, which grow without $\mathrm{O_2}$ (by fermentation or anaerobic respiration) but grow better with it, because they can respire it;
- **aerotolerant anaerobes**, which cannot use $\mathrm{O_2}$ but grow in its presence, equally well with or without it;
- **obligate anaerobes**, which are inhibited or killed by $\mathrm{O_2}$.

| Class | Relationship to $\mathrm{O_2}$ | Metabolism | Example | Habitat |
|---|---|---|---|---|
| Obligate aerobe | required | aerobic respiration | *Micrococcus luteus* | skin, dust |
| Facultative anaerobe | not required, growth better with $\mathrm{O_2}$ | aerobic or anaerobic respiration, fermentation | *Escherichia coli* | mammalian large intestine |
| Microaerophile | required, at levels below air | aerobic respiration | *Spirillum volutans*, *Campylobacter* | lake water; animal intestines |
| Aerotolerant anaerobe | not required, growth not better with $\mathrm{O_2}$ | fermentation | *Streptococcus pyogenes*, lactobacilli | upper respiratory tract; milk, plants |
| Obligate anaerobe | harmful or lethal | fermentation or anaerobic respiration | *Methanobacterium*, *Clostridium* | sewage sludge, anoxic sediments |

Microaerophily has several causes: some organisms have only a limited capacity to remove the toxic products of oxygen, and others contain $\mathrm{O_2}$-sensitive enzymes, such as the nitrogenase of nitrogen-fixing *Azospirillum*. Among obligate anaerobes the sensitivity to oxygen varies widely. Many clostridia tolerate traces or even brief exposure to air (and their spores are not harmed), whereas methanogens are killed rapidly. Most eukaryotes are obligate aerobes, but facultative ones (yeasts) and obligate anaerobes (rumen ciliates and fungi, *Giardia* and *Trichomonas*, [7.11.20](/7.11.20)) are known.

A simple test shows an organism's class. Thioglycolate broth contains sodium thioglycolate, a **reducing agent** that reacts with $\mathrm{O_2}$, and a little agar that prevents convection; after thioglycolate has consumed the dissolved oxygen, $\mathrm{O_2}$ enters again only by diffusion from the surface, so a gradient forms from oxic at the top to anoxic below. The redox dye resazurin, pink when oxidized and colorless when reduced, shows how far oxygen penetrates. Each class grows in a characteristic zone (figure below, panel A).

Aerobes need aeration, because they consume $\mathrm{O_2}$ faster than it diffuses into a liquid culture: flasks are shaken, or sterile air is bubbled through fermenters. For anaerobes the task is to exclude $\mathrm{O_2}$: vessels filled to the top and tightly closed, with a reducing agent, suffice for moderately sensitive organisms; plates are incubated in anoxic jars, in which a chemical sachet generates $\mathrm{H_2}$ and $\mathrm{CO_2}$ and a palladium catalyst combines the $\mathrm{H_2}$ with the remaining $\mathrm{O_2}$ to water; and strict anaerobes are handled in glove boxes filled with an oxygen-free gas mixture, or in tubes and bottles prepared under oxygen-free gas by the Hungate technique ([7.11.4](/7.11.4)).

### 9.4.2. Why Oxygen Is Toxic

Molecular oxygen itself is a rather unreactive molecule; what harms cells are its partially reduced forms. The complete reduction of $\mathrm{O_2}$ to water needs four electrons, and when electrons are added one at a time the intermediates are the **superoxide** anion $\mathrm{O_2^{\bullet-}}$, hydrogen peroxide $\mathrm{H_2O_2}$ and the hydroxyl radical $\mathrm{OH^\bullet}$ (figure below, panel B):

$$
\mathrm{O_2} \xrightarrow{\ \mathrm{e^-}\ } \mathrm{O_2^{\bullet-}} \xrightarrow{\ \mathrm{e^-} + 2\mathrm{H^+}\ } \mathrm{H_2O_2} \xrightarrow{\ \mathrm{e^-} + \mathrm{H^+}\ } \mathrm{H_2O} + \mathrm{OH^\bullet} \xrightarrow{\ \mathrm{e^-} + \mathrm{H^+}\ } \mathrm{H_2O}.
$$

These **reactive oxygen species** form inevitably in any cell exposed to oxygen, mostly when reduced flavoproteins, quinones and iron–sulfur proteins of metabolism and respiration transfer single electrons to $\mathrm{O_2}$ by accident; light adds singlet oxygen when photosensitizing pigments are excited. Superoxide inactivates enzymes with exposed iron–sulfur clusters, such as dehydratases of central metabolism, and releases their iron. Hydrogen peroxide reacts with free ferrous iron in the Fenton reaction, $\mathrm{Fe}^{2+} + \mathrm{H_2O_2} \to \mathrm{Fe}^{3+} + \mathrm{OH^-} + \mathrm{OH^\bullet}$, and the hydroxyl radical oxidizes whatever it meets, including DNA bases ([7.2.8](/7.2.8)). Because both superoxide and peroxide feed the Fenton reaction, they act together.

### 9.4.3. Enzymes That Remove Reactive Oxygen

All organisms that live in contact with oxygen have enzymes that destroy superoxide and hydrogen peroxide (panel B):

- *Superoxide dismutase* (SOD) converts two superoxide anions into hydrogen peroxide and oxygen, $2\,\mathrm{O_2^{\bullet-}} + 2\,\mathrm{H^+} \to \mathrm{H_2O_2} + \mathrm{O_2}$. SODs contain manganese, iron, copper and zinc, or nickel. SOD is essential for aerobes.
- *Catalase* decomposes hydrogen peroxide, $2\,\mathrm{H_2O_2} \to 2\,\mathrm{H_2O} + \mathrm{O_2}$, and peroxidases reduce it with an organic reductant, for example NADH peroxidase, $\mathrm{H_2O_2} + \mathrm{NADH} + \mathrm{H^+} \to 2\,\mathrm{H_2O} + \mathrm{NAD^+}$. In *E. coli* the low levels of peroxide produced in normal aerobic growth are removed mainly by the peroxiredoxin alkyl hydroperoxide reductase, and catalase takes over at high levels.
- *Superoxide reductase* (SOR), found instead of SOD in some strictly anaerobic bacteria and archaea, reduces superoxide to hydrogen peroxide with electrons from reduced rubredoxin, $\mathrm{O_2^{\bullet-}} + 2\,\mathrm{H^+} + \mathrm{e^-} \to \mathrm{H_2O_2}$, without releasing oxygen.

SOD and catalase work in series, converting superoxide via hydrogen peroxide to oxygen and water; aerobes and facultative anaerobes usually have both. Some aerotolerant lactic acid bacteria lack SOD and instead accumulate millimolar concentrations of manganese, whose complexes dismutate superoxide nonenzymatically, less efficiently but sufficiently. Obligate anaerobes are killed by $\mathrm{O_2}$ because they have few such defenses and because their metabolism relies on enzymes that oxygen or its products destroy, such as the oxygen-sensitive iron–sulfur enzymes and the glycyl-radical enzymes of fermentation. The expression of the defenses is regulated: in *E. coli* the transcription factor OxyR senses hydrogen peroxide and SoxR senses superoxide-generating compounds ([7.11.11](/7.11.11)), and similar regulons protect pathogens against the oxidative burst of phagocytes ([7.11.34](/7.11.34)).

![Oxygen classes and reactive oxygen species (schematic). A: growth in tubes of thioglycolate broth, in which oxygen enters only by diffusion from the surface (pink: oxidized resazurin). Obligate aerobes grow only at the surface; obligate anaerobes only in the depth; facultative anaerobes throughout, but best near the top; microaerophiles in a band just below the surface; aerotolerant anaerobes evenly throughout. B: the stepwise one-electron reduction of oxygen to water through superoxide, hydrogen peroxide and the hydroxyl radical (formed from hydrogen peroxide and Fe²⁺), and the enzymes that remove superoxide (superoxide dismutase; superoxide reductase in some strict anaerobes, without releasing oxygen) and hydrogen peroxide (catalase, peroxidase)](./plots/oxygen.py)

The *catalase test* exploits the second reaction: a loopful of cells from a colony is mixed with a drop of $3\,\%$ hydrogen peroxide, and catalase-positive organisms release a stream of oxygen bubbles. The test separates, for example, catalase-positive staphylococci from catalase-negative streptococci and is one of the first steps of bacterial identification ([7.11.16](/7.11.16)).

## 9.5. Pressure

Pressure increases by about $0.1\,\mathrm{MPa}$ ($1$ atmosphere) for every $10\,\mathrm{m}$ of water depth, so that the average ocean floor at about $4000\,\mathrm{m}$ is at $40\,\mathrm{MPa}$ and the deepest trenches at more than $100\,\mathrm{MPa}$. Most bacteria from the surface are inhibited at such pressures. Barotolerant organisms grow at high pressure but best at atmospheric pressure; *piezophiles* (barophiles) grow best at high pressure, and the most extreme of them, isolated from the deepest trenches, cannot grow at atmospheric pressure at all. Since the deep sea is also cold, most piezophiles are psychrophiles as well. High pressure favors processes that decrease volume and opposes those that increase it, so it affects the packing of membrane lipids (like cold, it makes membranes more ordered), the assembly of multimeric proteins such as ribosomes and the binding of substrates; piezophiles respond, among other ways, with more unsaturated fatty acids in their membranes. Deep-sea microbial life is described in [7.11.29](/7.11.29).

## 9.6. Radiation

Electromagnetic radiation affects microorganisms according to its energy. Visible light drives phototrophy but can also kill, when it excites photosensitizing pigments that transfer energy to oxygen and form singlet oxygen; carotenoids, which quench singlet oxygen, protect many phototrophs and nonphototrophic bacteria exposed to light, which is one reason why colonies of airborne bacteria are often pigmented. Ultraviolet radiation, especially at wavelengths near $260\,\mathrm{nm}$ where DNA absorbs, forms pyrimidine dimers and other lesions that block replication, and ionizing radiation breaks DNA strands, mostly through hydroxyl radicals from the radiolysis of water ([7.2.8](/7.2.8#sec-8.1.2)); both are used to kill microorganisms ([7.11.10](/7.11.10)). Natural resistance varies enormously. Bacterial spores are far more resistant than growing cells, and *Deinococcus radiodurans* survives doses of ionizing radiation thousands of times higher than those lethal to humans, by efficient repair of its fragmented chromosomes and by manganese complexes that protect its proteins from oxidation ([7.11.18](/7.11.18)).

## Summary

| Factor | Classes (by optimum) | Key adaptations |
|---|---|---|
| Temperature | **psychrophile** (≤ 15 °C), mesophile, **thermophile** (45–80 °C), **hyperthermophile** (> 80 °C); psychrotolerant (Definition 9.1.1) | cold: flexible enzymes, unsaturated and short-chain fatty acids, cold shock and antifreeze proteins; heat: ionic bonds and hydrophobic cores in proteins, saturated or ether lipids and monolayers, reverse gyrase, DNA-binding proteins, solutes |
| pH | **acidophile** (< 5.5), neutrophile, **alkaliphile** (≥ 8) (Definition 9.2.1) | cytoplasm kept near neutral: proton-tight membranes and reversed membrane potential (acidophiles), Na⁺/H⁺ antiport and sodium-motive force (alkaliphiles) |
| Water activity | nonhalophile, halotolerant, **halophile**, **extreme halophile**; osmophile, xerophile (Definition 9.3.2) | **compatible solutes** (Definition 9.3.3) or salt-in with acidic proteins; lower limit $a_{\mathrm{w}} \approx 0.61$ |
| Oxygen | obligate aerobe, **microaerophile**, **facultative anaerobe**, **aerotolerant anaerobe**, **obligate anaerobe** (Definition 9.4.1) | **superoxide dismutase**, **catalase**, peroxidases, superoxide reductase |
| Pressure | barotolerant, piezophile | membrane lipids, protein assembly |

- Every organism has minimum, optimum and maximum temperatures; the optimum lies near the maximum because reaction rates rise slowly while proteins unfold cooperatively. Growth ranges from $-15$ to $122\,^\circ\mathrm{C}$; above $95\,^\circ\mathrm{C}$ only archaea grow. Taq polymerase from *Thermus aquaticus* made PCR practical.
- **Water activity** (Definition 9.3.1) measures the availability of water and is related to osmotic pressure by $\Pi = -(RT/V_{\mathrm{m,w}})\ln a_{\mathrm{w}}$; seawater has $a_{\mathrm{w}} = 0.98$, saturated NaCl $0.75$ (Example 9.3.1).
- Reactive oxygen species arise from one-electron reductions of $\mathrm{O_2}$; their removal decides which organisms can live with oxygen. Thioglycolate tubes reveal the oxygen class, and the catalase test is used in identification.

## Questions

1. Why is the optimum growth temperature of a microorganism usually much closer to its maximum than to its minimum? What sets the minimum?

   **Answer** Below the optimum, the growth rate is limited by the rates of chemical reactions, which increase gradually (roughly exponentially, by a factor of about two per $10$ degrees). Above it, essential proteins unfold; unfolding is highly cooperative, so it goes from negligible to complete within a few degrees. The product peaks just below the temperature where unfolding begins. The minimum is usually set by the membrane, which becomes too rigid for transport and energy conservation, so psychrophiles make membranes with more unsaturated and short-chain fatty acids.

2. A hyperthermophilic archaeon grows at $105\,^\circ\mathrm{C}$. List four features that would allow its DNA, proteins and membranes to remain functional, and explain why the GC content of its genome is not one of them.

   **Answer** Positive supercoiling by reverse gyrase and DNA-binding proteins or archaeal histones that stabilize the duplex; high intracellular K⁺ and solutes such as cyclic 2,3-diphosphoglycerate or di-*myo*-inositol phosphate; proteins with more salt bridges and tightly packed hydrophobic cores, plus chaperonins; tetraether lipid monolayers that cannot separate into two leaflets and ether bonds that resist hydrolysis. Genomic GC content does not correlate with growth temperature, because the double helix is stabilized by the other means and because GC content is shaped mainly by mutational biases; only structured RNAs such as rRNA are GC-rich in hyperthermophiles.

3. Calculate the water activity and osmotic pressure of a $2\,\mathrm{mol\,kg^{-1}}$ NaCl solution ($\phi = 0.98$) at $25\,^\circ\mathrm{C}$. How can a halophile growing in it keep positive water balance, and why does the salt-in strategy require a special proteome?

   **Answer** $\ln a_{\mathrm{w}} = -2 \times 2 \times 0.98 \times 0.018 = -0.071$, so $a_{\mathrm{w}} = 0.93$; $\Pi = (8.314 \times 298/1.8\times10^{-5}) \times 0.071 = 9.7\,\mathrm{MPa}$. The cell must raise its internal solute concentration above the external osmolality, either by accumulating compatible solutes such as glycine betaine or ectoine, which do not disturb enzymes, or by accumulating KCl (salt-in). At molar KCl, ordinary proteins aggregate and lose their hydration shell; salt-in organisms have proteins with many surface acidic residues, which bind water and cations and stay soluble at high salt but unfold in dilute solution.

4. Predict the growth pattern in thioglycolate broth of (a) a mutant of a facultative anaerobe that lacks superoxide dismutase but still has catalase, and (b) an obligate anaerobe that expresses superoxide reductase. Explain your reasoning.

   **Answer** (a) Superoxide accumulates in the oxic zone, inactivates iron–sulfur enzymes and feeds the Fenton reaction, so the mutant grows poorly or not at all near the surface but normally in the anoxic depth: it behaves like an anaerobe (*E. coli* *sodA sodB* mutants indeed need special supplements to grow aerobically). (b) It still grows only in the anoxic part, because its oxygen-sensitive enzymes and lack of respiration remain, but superoxide reductase lets it survive brief exposure to oxygen; since SOR does not release $\mathrm{O_2}$, it detoxifies superoxide without regenerating oxygen in the cell.

5. Why are psychrotolerant bacteria rather than psychrophiles the main cause of spoilage of refrigerated food, and why is *Listeria monocytogenes* a concern for ready-to-eat foods?

   **Answer** Food is stored at about $4\,^\circ\mathrm{C}$ but is handled, transported and sometimes held at higher temperatures; psychrotolerant organisms grow (slowly) at $4\,^\circ\mathrm{C}$ and survive warming, whereas strict psychrophiles are rare in temperate environments and are killed by warming. In a week in the refrigerator, slow exponential growth multiplies their numbers many times. *L. monocytogenes* is psychrotolerant, so it multiplies during refrigerated storage of foods that are eaten without further heating; refrigeration slows but does not stop it.
