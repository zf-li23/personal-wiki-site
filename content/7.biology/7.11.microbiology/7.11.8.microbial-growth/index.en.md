---
title: "Microbial Growth: Cell Division and Population Growth"
description: "Binary fission and the bacterial cell cycle: replication, segregation, the divisome with FtsZ, the Min system and nucleoid occlusion, MreB and crescentin, budding; peptidoglycan biosynthesis in three compartments (Park nucleotide, bactoprenol and lipid II, transglycosylation and transpeptidation by penicillin-binding proteins, autolysins); the mathematics of exponential growth; the growth cycle of a batch culture and its four phases; synchronous cultures; continuous culture in the chemostat and turbidostat, washout and competition for a limiting nutrient; fed-batch and high-density culture; measuring growth by direct and viable counts, the most probable number, turbidity and biomass."
---

In microbiology, growth means an increase in the number of cells, not in the size of one cell. A bacterium doubles its contents and divides, its two daughters do the same, and within a day a single cell can give rise to more cells than there are people on Earth. This chapter follows growth on two scales. At the scale of the cell, it describes how a rod-shaped bacterium replicates and segregates its chromosome, finds its middle and builds a new wall between the daughters, and how the wall itself is made, a pathway that is the target of the most important antibiotics. At the scale of the population, it gives the arithmetic of exponential growth, the phases of a culture in a closed flask, the continuous cultures that hold a population in steady state, and the methods by which cells are counted.

Several pieces are treated elsewhere and only linked here: the molecular machinery of replication and its once-per-cycle control in [7.2.7](/7.2.7), the cytoskeletal proteins FtsZ and MreB in [7.3.15](/7.3.15#sec-15.2), the physics of the Min oscillation in [7.6.36](/7.6.36#sec-36.3), cell-size control by the adder in [7.3.22](/7.3.22#sec-22.4.2), and the quantitative laws of balanced growth, Monod's law and the steady state of the chemostat in [7.6.39](/7.6.39). The nutrients and media on which cells grow are in [7.11.4](/7.11.4), the effect of the physical environment on growth rate in [7.11.9](/7.11.9), and the killing of cells, which uses the same kinetics in reverse, in [7.11.10](/7.11.10).

## 8.1. Binary Fission and the Bacterial Cell Cycle

### 8.1.1. One Cell Becomes Two

**Definition 8.1.1 (Binary Fission)** **Binary fission** is cell division in which a cell, after doubling all its components, forms a septum at its middle and divides into two equivalent daughter cells.

A rod such as *Escherichia coli* elongates to about twice its length, then the cytoplasmic membrane and the wall grow inwards from all sides at midcell until the two daughters are pinched off. The interval between successive divisions is one generation, and the time it takes is the **generation time** (doubling time). During one generation every component of the cell, from the chromosome to the ribosomes and ions, increases in proportion, so that each daughter starts with a complete set. In the best laboratory media *E. coli* divides about every $20$ minutes; most bacteria need hours, and in nutrient-poor natural habitats, such as the deep subsurface, generation times of months or longer are inferred.

There are variations within binary fission. In *Bacillus subtilis* a septum of membrane and wall forms across the cell before the cell constricts, so that the daughters can stay attached in chains. In *Caulobacter crescentus* the cell constricts gradually without a distinct septum, and the two daughters differ (a stalked cell and a swimming swarmer cell, [7.11.12](/7.11.12)).

### 8.1.2. Replication and Segregation

Before dividing, the cell must have two complete chromosomes and must have moved them apart. Replication of the single circular chromosome of *E. coli* starts at one **origin of replication**, *oriC*, and proceeds in both directions to the terminus; its initiation is triggered by the ATP-bound form of DnaA and blocked, for some time after each initiation, by sequestration of the newly replicated, hemimethylated origin by SeqA ([7.2.7](/7.2.7#sec-7.5.2)). At $37\,^\circ\mathrm{C}$ the two forks take about $40$ minutes to copy the $4.6\,\mathrm{Mb}$ chromosome, and another $20$ minutes pass between the end of replication and division. A cell that divides every $20$ minutes therefore starts new rounds before the previous ones finish, so that its chromosomes carry several pairs of forks (multifork replication). The timing is described quantitatively by the **Cooper–Helmstetter model** ([7.6.39](/7.6.39#fml-39.2.3)), and cell size is held constant because each cell adds a roughly constant volume between birth and division, the **adder** ([7.3.22](/7.3.22#sec-22.4.2)).

Segregation of the daughter chromosomes is not done by a spindle. In many bacteria, including *Caulobacter*, a partitioning (Par) system acts on a centromere-like site *parS* near the origin: ParB binds *parS*, and the ATPase ParA, distributed over the **nucleoid**, moves the new ParB–*parS* complex to the opposite pole, where it is captured by the polar protein PopZ. *E. coli* lacks ParAB for its chromosome; its sister chromosomes are decatenated by topoisomerase IV, organized by the condensin MukBEF, and appear to separate largely through the physical action of replication and the entropy of two confined polymers ([7.6.21](/7.6.21)). The DNA translocase FtsK in the septum pumps the last chromosomal DNA out of the closing division plane.

### 8.1.3. The Divisome

**Definition 8.1.2 (Divisome)** The **divisome** is the complex of cell-division proteins assembled on a ring of FtsZ at the future division site, which constricts the cell and synthesizes the septal cell wall.

Division begins when **FtsZ**, the bacterial tubulin homolog, polymerizes with GTP into short protofilaments that are tethered to the membrane by FtsA and (in *E. coli*) ZipA, forming the Z ring at midcell. Several thousand FtsZ molecules take part. The ring recruits, in a roughly ordered sequence, proteins that link it to the rest of the division machinery: FtsK, the septal peptidoglycan synthase pair FtsW–FtsI (FtsI is the penicillin-binding protein PBP3, Section 8.2), FtsN, which triggers septal wall synthesis, and amidases that split the shared septal wall so that the daughters can separate. FtsZ filaments treadmill around the ring, growing at one end and shrinking at the other, and carry the wall-synthesizing enzymes with them; the rate of treadmilling sets the rate of septal wall synthesis (Bisson-Filho et al. 2017; Yang et al. 2017). In *E. coli* the ring assembles when the cell cycle is about three-quarters complete and disassembles as the septum closes. FtsZ is present in almost all bacteria and in many archaea; the other Fts proteins are bacterial.

Two systems place the ring at the middle (figure below, panel B):

- Nucleoid occlusion: proteins bound to the chromosome inhibit FtsZ assembly over the nucleoid: SlmA in *E. coli*, Noc in *B. subtilis*. The ring can form only in the DNA-free gap that opens at midcell when the two daughter nucleoids have separated, which also prevents the septum from guillotining a chromosome.
- The Min system: MinC inhibits FtsZ polymerization and rides on the membrane-bound ATPase MinD, which MinE releases from the membrane. In *E. coli* the three proteins oscillate from pole to pole about once a minute, the **Min oscillation**; averaged over time, the inhibitor is lowest at midcell ([7.6.36](/7.6.36#sec-36.3), where the reaction–diffusion model is analyzed). Mutants lacking the Min proteins often divide near a pole and produce small anucleate minicells. *B. subtilis* has no oscillation; its MinCD is held at the poles and at new septa by DivIVA.

![Binary fission of a rod-shaped bacterium (schematic). A: one cell cycle. (1) A newborn cell with one nucleoid (blue) and one origin of replication (yellow). (2) The cell elongates and replicates its chromosome; the two new origins move apart. (3) Replication is complete, the nucleoids have separated, and FtsZ forms the Z ring (red) in the gap at midcell. (4) The divisome constricts the envelope and synthesizes the septum. (5) Two equivalent daughter cells separate. B: why the ring forms at midcell (model curves): the time-averaged MinC from the pole-to-pole Min oscillation is highest at the poles, and nucleoid occlusion inhibits ring assembly over the two segregated nucleoids; only in the middle (shaded) are both inhibitors low](./plots/binary-fission.py)

### 8.1.4. Cell Shape: MreB and Crescentin

The shape of a bacterium is the shape of its peptidoglycan sac, and the shape of the sac is set by where new wall material is inserted. In rods, the actin homolog **MreB** forms short filaments bound to the inner face of the cytoplasmic membrane that move around the cell circumference, roughly perpendicular to the long axis, together with the wall-synthesizing complex of RodA and PBP2 (the "Rod complex"). Their motion is driven by wall synthesis itself, and it spreads insertion over the cylinder, so that the cell lengthens without becoming wider. Earlier fluorescence images were read as a continuous MreB helix; with better microscopy the filaments turned out to be short, discrete patches that move circumferentially (Domínguez-Escobar et al. 2011; Garner et al. 2011). Deleting or inhibiting MreB turns rods into spheres, and most cocci lack *mreB* altogether, which suggests that a sphere is the default form and a rod requires dispersed, oriented insertion. Cocci such as *Staphylococcus aureus* make new wall almost only at the septum.

The vibrio-shaped *Caulobacter crescentus* has, in addition, crescentin, a coiled-coil protein related to eukaryotic intermediate filaments, which forms a filament along the inner (concave) side of the cell and slows wall growth there, so the cell curves. The three main elements of the eukaryotic cytoskeleton thus all have bacterial relatives: tubulin in FtsZ, actin in MreB (and in the plasmid-segregating ParM), and intermediate filaments in crescentin ([7.3.15](/7.3.15#def-15.2.1)).

### 8.1.5. Budding and Other Modes of Division

Binary fission is not universal. Budding bacteria divide by unequal growth: a new cell grows out from one point of the mother cell, which keeps its identity, as in *Pirellula* or *Blastobacter*; in *Hyphomicrobium* and *Rhodomicrobium* the bud forms at the tip of a hypha (a thin cytoplasmic extension). Polar growth, the insertion of new wall at one pole only, is common in the Alphaproteobacteria and in the Actinomycetota, among them *Mycobacterium* and *Streptomyces*. Because a bud is built anew rather than divided, internal membrane systems need not be partitioned, which may explain why many budding bacteria, such as the phototrophic and nitrifying ones, have elaborate intracytoplasmic membranes. Other modes include fragmentation of filaments into short pieces, the formation of spores at hyphal tips in *Streptomyces*, multiple fission into many daughter cells (baeocytes) in some cyanobacteria and in the predatory *Bdellovibrio*, which grows as a filament inside the periplasm of its prey and then fragments into several progeny, and the formation of daughter cells inside the mother in a few giant bacteria. Most archaea of the Thermoproteota (formerly Crenarchaeota) lack FtsZ and divide with homologs of the eukaryotic ESCRT-III proteins ([7.11.19](/7.11.19)).

## 8.2. Peptidoglycan Biosynthesis

### 8.2.1. A Pathway in Three Compartments

The **peptidoglycan** sac is one huge, cross-linked molecule ([7.1.10](/7.1.10#sec-10.3.5); its structure in Gram-positive and Gram-negative cells is in [7.11.2](/7.11.2)). Growing it raises a logistic problem: the building blocks are made in the cytoplasm from nucleotide-activated sugars, but they are assembled outside the cytoplasmic membrane, where there is no ATP. The cell solves it by attaching each subunit to a lipid carrier that crosses the membrane, and by building in, as a stored bond, the energy that the final cross-linking step needs. The pathway (figure below) has three stages.

1. Cytoplasm. UDP-*N*-acetylglucosamine (UDP-GlcNAc) is converted to UDP-*N*-acetylmuramic acid (UDP-MurNAc) by MurA, which adds an enolpyruvyl group from phosphoenolpyruvate, and MurB, which reduces it to the lactyl ether. The ligases MurC, MurD, MurE and MurF then add, one at a time, L-alanine, D-glutamate, *meso*-diaminopimelic acid (L-lysine in most Gram-positive bacteria) and the dipeptide D-alanyl-D-alanine. The D-alanine is made from L-alanine by alanine racemase and joined by D-Ala–D-Ala ligase. The product, UDP-MurNAc-pentapeptide, is the *Park nucleotide*, which J. T. Park found accumulating in penicillin-treated *S. aureus* in the 1950s.
2. Membrane. The carrier is undecaprenyl phosphate (bactoprenol phosphate), a $\mathrm{C_{55}}$ isoprenoid alcohol phosphate embedded in the membrane. MraY transfers phospho-MurNAc-pentapeptide from the Park nucleotide to it, giving lipid I, and MurG adds GlcNAc from UDP-GlcNAc, giving lipid II, the complete disaccharide–pentapeptide unit on its carrier. A flippase (MurJ is the leading candidate in *E. coli*) moves lipid II to the outer face of the membrane.
3. Outside the membrane. Glycosyltransferases join the disaccharide of lipid II to the end of a growing glycan strand, releasing undecaprenyl pyrophosphate, which is dephosphorylated and flipped back to carry the next unit. Transpeptidases then cross-link the peptides of neighboring strands (Section 8.2.2).

![Peptidoglycan biosynthesis (schematic, *E. coli*-type peptides with meso-diaminopimelic acid). In the cytoplasm, UDP-GlcNAc is converted to UDP-MurNAc (MurA, MurB) and the pentapeptide is added (MurC–F, the last step adding D-Ala-D-Ala), giving the Park nucleotide. In the membrane, MraY transfers it to the lipid carrier bactoprenol phosphate (undecaprenyl phosphate), giving lipid I; MurG adds GlcNAc to make lipid II, which is flipped to the outer face. Outside the membrane, transglycosylation (class A penicillin-binding proteins, and the SEDS proteins RodA and FtsW) adds the disaccharide-pentapeptide to a growing strand and releases the carrier as undecaprenyl pyrophosphate, which is dephosphorylated and returned; transpeptidation by penicillin-binding proteins cross-links the strands and releases the terminal D-Ala; autolysins open the existing wall where new strands are inserted. Red bars mark the steps blocked by fosfomycin, D-cycloserine, bacitracin, vancomycin and the β-lactams](./plots/peptidoglycan-synthesis.py)

### 8.2.2. Transglycosylation, Transpeptidation and Penicillin-Binding Proteins

The enzymes of the last stage were identified by their ability to bind radioactive penicillin covalently, which is how they got their name: *penicillin-binding proteins* (PBPs). Class A PBPs are bifunctional, with a glycosyltransferase and a transpeptidase domain; class B PBPs, such as PBP2 and PBP3 (FtsI) of *E. coli*, are transpeptidases that work with the glycosyltransferases RodA and FtsW, members of the SEDS (shape, elongation, division and sporulation) family discovered as wall synthases only in 2016 (Meeske et al. 2016). RodA–PBP2 builds the lateral wall with MreB, and FtsW–FtsI the septum with FtsZ.

In transpeptidation, the enzyme attacks the peptide bond between the two terminal D-alanines of a donor pentapeptide with an active-site serine, releasing the last D-alanine and forming an acyl-enzyme; the amino group of a neighboring peptide (the diaminopimelate of *E. coli*, or the pentaglycine bridge of *S. aureus*) then attacks the acyl-enzyme, forming the cross-link. The reaction needs no ATP: the energy comes from the peptide bond made in the cytoplasm by D-Ala–D-Ala ligase. **β-Lactam antibiotics** resemble the D-Ala–D-Ala end of the donor and acylate the active-site serine, but the acyl-enzyme hydrolyzes extremely slowly, so the enzyme is inactivated. In *E. coli* most cross-links are of this 4→3 type (D-Ala of one peptide to DAP of another); a minority, 3→3 links between two DAPs, are made by L,D-transpeptidases that β-lactams other than carbapenems do not inhibit.

### 8.2.3. Autolysins and the Growth of the Wall

A closed sac can grow only if bonds are cut where new material is inserted. *Autolysins*, hydrolases that cleave the glycan backbone (lytic transglycosylases, glucosaminidases), the peptide (endopeptidases) or the bond between the two (amidases), open the existing wall, and new strands are spliced in. The two activities must be balanced: if synthesis stops while autolysins keep working, the wall develops holes and the cell bursts under its turgor pressure. This is why β-lactams kill growing bacteria by lysis but hardly affect nongrowing ones. In Gram-negative rods new strands are inserted under tension into a single-layered sac, the "make-before-break" model; in Gram-positive bacteria new wall is added at the inner face of the thick wall, which moves outwards and is shed from the surface ("inside-to-outside" growth).

Every stage of the pathway has its drug, which makes it the classic case of a selective target, since animals have no peptidoglycan. Fosfomycin inhibits MurA; D-cycloserine, an alanine analog, inhibits alanine racemase and D-Ala–D-Ala ligase; bacitracin binds undecaprenyl pyrophosphate and prevents recycling of the carrier; vancomycin binds the D-Ala–D-Ala end of lipid II and nascent wall and blocks both transglycosylation and transpeptidation; the β-lactams inactivate the PBPs; and lysozyme, an enzyme of tears and egg white, hydrolyzes the glycan backbone of the finished wall. Their mechanisms, spectra and resistance are the subject of [7.11.14](/7.11.14) and [7.11.15](/7.11.15).

## 8.3. Exponential Growth

### 8.3.1. Generations, Generation Time and the Growth Rate Constant

If every cell divides once per generation time $g$, the number of cells doubles in each interval $g$: from one cell to $2, 4, 8, \dots$ This is exponential growth. On an arithmetic axis the curve becomes ever steeper; on a semilogarithmic plot, with the logarithm of cell number against time, it is a straight line whose slope is proportional to the growth rate (figure below, panel A). Semilogarithmic plots are therefore the standard way to display growth data, and the generation time can be read from them as the time in which the line rises by $\log_{10} 2 = 0.301$.

**Formula 8.3.1 (Exponential Growth)** A population that starts with $N_0$ cells and passes through $n$ generations in time $t$ has

$$
N = N_0\,2^n, \qquad n = \frac{\log_{10} N - \log_{10} N_0}{\log_{10} 2} \approx 3.3\,(\log_{10} N - \log_{10} N_0), \qquad g = \frac{t}{n}.
$$
Writing the same growth as a continuous process, $\mathrm{d}N/\mathrm{d}t = kN$, gives $N = N_0\,\mathrm{e}^{kt}$ with the instantaneous (specific) growth rate constant

$$
k = \frac{\ln 2}{g} = \frac{0.693}{g}, \tag{8.1}
$$
in units of reciprocal time. The slope of $\log_{10} N$ against $t$ is $k/\ln 10 = 0.301/g$.

The two descriptions are equivalent for a population that grows steadily: $g$ is the mean time for the population to double, and $k$ the fractional rate of increase at any instant. Biochemical engineers and physiologists usually write the specific growth rate as $\mu$, and 7.6 writes it as $\lambda$ ([7.6.39](/7.6.39#def-39.1.1)); the generation time is then the **doubling time** $\tau = \ln 2/\lambda$. The exponential law holds exactly in **balanced growth**, when every component of the culture increases by the same factor, which is reached after several generations in a constant environment.

**Example 8.3.1** A culture grows exponentially from $5 \times 10^6$ to $5 \times 10^8$ cells per milliliter in $8\,\mathrm{h}$. Then $n = 3.3\,(8.70 - 6.70) = 6.6$ generations, $g = 8/6.6 = 1.2\,\mathrm{h} = 72\,\mathrm{min}$, and $k = 0.693/1.2 = 0.58\,\mathrm{h^{-1}}$.

### 8.3.2. Consequences of Exponential Growth

Exponential growth starts slowly and ends explosively. A single cell doubling every $30$ minutes makes one new cell in the first half hour and $2048$ new cells between $5.5$ and $6$ hours. A single cell of $10^{-12}\,\mathrm{g}$ dividing every $20$ minutes would weigh $2^{144} \times 10^{-12}\,\mathrm{g} \approx 2 \times 10^{31}\,\mathrm{g}$ after $48$ hours, more than a thousand times the mass of the Earth ($6 \times 10^{27}\,\mathrm{g}$). No population can sustain this for long; growth must stop when a nutrient runs out or waste accumulates, which is what Section 8.4 describes. The same arithmetic explains everyday experiences such as the spoilage of milk: lactic acid bacteria that grow slowly in the refrigerator reach, after a week, a population large enough that one night at room temperature is enough to sour the milk.

## 8.4. The Growth Cycle of a Batch Culture

### 8.4.1. Four Phases

**Definition 8.4.1 (Batch Culture and Growth Curve)** A **batch culture** is a culture grown in a closed vessel, to which no nutrients are added and from which nothing is removed during growth. A plot of the logarithm of cell number against time for such a culture is its **growth curve**.

A batch culture is the commonest way to grow microorganisms, and its growth curve has four phases (figure below, panel B). They are properties of the population, not of individual cells: a cell does not "enter stationary phase" by itself, but the culture does as nutrients run out.

**Definition 8.4.2 (Phases of Growth)** After inoculation into fresh medium, a batch culture passes through:

- the **lag phase**, an interval before growth begins, in which the cells adjust to the new medium;
- the **exponential phase** (log phase), in which the cells divide at a constant rate, the maximal rate for the conditions;
- the **stationary phase**, in which there is no net increase in cell number because an essential nutrient is exhausted or inhibitory products have accumulated;
- the **death phase**, in which the number of viable cells declines, usually exponentially.

The length of the lag phase depends on the history of the inoculum and on the medium. If exponentially growing cells are transferred into the same medium under the same conditions, there is essentially no lag. Cells from an old (stationary) culture are depleted of ribosomes, enzymes and metabolite pools and must rebuild them; cells transferred from a rich to a poorer medium must induce the enzymes for the biosynthesis of everything the new medium lacks; and cells damaged by heat, radiation or chemicals must first repair the damage. Lag is therefore not a phase of inactivity but of intense synthesis without division: RNA and protein increase, and in *Salmonella* hundreds of genes, including those for iron and manganese uptake, are induced within minutes of transfer (Rolfe et al. 2012). A simple quantitative description (Baranyi and Roberts 1994) gives the cells a "physiological state" that must grow to a threshold before division at full speed can start; it is used in the figure.

In the exponential phase, cells are in balanced growth, at their largest size and highest content of ribosomes for the conditions, and are the most uniform; they are used for most physiological and biochemical experiments. The growth rate depends on the medium, the temperature and the organism ([7.11.9](/7.11.9)), and in general prokaryotes grow faster than eukaryotes and small eukaryotes faster than large ones.

In the stationary phase growth stops, but the cells are not inert. They switch to a starvation program: in *E. coli* the stationary-phase sigma factor $\sigma^{\mathrm{S}}$ (RpoS) takes over transcription of hundreds of genes, the alarmone ppGpp of the **stringent response** shuts down ribosome synthesis, and the cells become smaller and rounder, condense their nucleoid with the protein Dps, and become more resistant to heat, oxidation, osmotic stress and antibiotics ([7.11.11](/7.11.11)). Spore formers begin to sporulate ([7.11.12](/7.11.12)). There can be slow growth balanced by death, with nutrients released by dead cells feeding survivors, called *cryptic growth*. Whether the population stops because of a limiting nutrient or because of toxic products (such as acids from fermentation) can be tested by adding the nutrient or by neutralizing the products.

If incubation continues, viable cells die, typically exponentially but much more slowly than they grew, so that viable cells may persist for months or years. Two complications matter. First, the viable count may fall while the total count does not, because dead cells remain intact for some time (panel B), and some cells that no longer form colonies are alive and metabolically active, a state called viable but nonculturable. Second, after most cells have died the population often does not die out but enters a long-term stationary phase, in which cell numbers stay roughly constant for months, with death balanced by growth on the remains of others. Such cultures are taken over in waves by mutants that grow better under starvation (growth advantage in stationary phase, GASP; Zambrano et al. 1993), an evolution experiment in a single flask.

![The growth of a bacterial population in batch culture. A: the same exponential growth (generation time 30 min, starting from 1000 cells per milliliter) on an arithmetic and on a semilogarithmic axis; only the semilogarithmic plot shows the constant rate as a straight line. B: the four phases of the growth cycle (model: Monod growth on one limiting nutrient, a Baranyi–Roberts lag of 3 h and first-order death after starvation). The viable count (green) falls in the death phase while the total count (dashed), measured by microscopy or turbidity, falls only as dead cells lyse. C: the lag depends on the inoculum: exponential-phase cells transferred into the same medium grow at once; stationary-phase cells first rebuild their machinery; damaged cells, or cells moved to a poorer medium, have a longer lag](./plots/growth-curve.py)

The curve of panel B can be read in terms of the two quantities that a nutrient controls in a batch culture (Monod 1949). Below a certain concentration both the growth rate and the final yield increase with the concentration of the limiting nutrient; above it, only the yield increases, because the growth rate is already maximal (**Monod's law**, [7.6.39](/7.6.39#fml-39.1.1)). The yield, the mass of cells formed per mass of nutrient consumed, is used to design media and to compare the efficiency of metabolic pathways. When two sugars are present, *E. coli* uses the preferred one first, pauses, and then grows on the second, a two-step growth curve called **diauxic growth** ([7.2.11](/7.2.11)).

### 8.4.2. Synchronous Cultures

In an exponential culture cells are at all stages of the cell cycle, and their ages are distributed so that young cells are twice as frequent as dividing ones. To study events tied to the cell cycle, one needs a synchronous culture, in which most cells divide at the same time. There are two kinds of methods:

- Selection of cells at one stage from an asynchronous culture: collecting newborn cells released from cells bound to a membrane (the "baby machine" of Helmstetter and Cummings, 1963), separating small, young cells by size through filtration or density-gradient centrifugation, or, in *Caulobacter*, isolating swarmer cells, which are denser than stalked cells.
- Induction of synchrony by a block that is then released: a temperature shift of a mutant whose initiation of replication is temperature-sensitive (*dnaA*(Ts)), starvation for a required nutrient, or an inhibitor of DNA synthesis.

Induction methods disturb the physiology of the cells, and in all methods synchrony decays within a few generations because individual generation times vary (their coefficient of variation is typically $10$–$20\,\%$). Today, many cell-cycle questions are answered instead by following single cells under the microscope, in microfluidic devices that keep each cell in a constant environment for many generations.

## 8.5. Continuous Culture

### 8.5.1. The Chemostat

**Definition 8.5.1 (Continuous Culture)** A **continuous culture** is an open culture system to which fresh medium is added continuously and from which an equal volume of culture is removed, so that the population can be kept growing at a steady state for long periods.

In a batch culture the environment changes all the time, and exponential growth lasts only a few generations. The **chemostat** (Monod 1950; Novick and Szilard 1950) is the most common continuous culture device (figure below, panel A). Sterile medium containing one growth-limiting nutrient, often the carbon or nitrogen source, at concentration $s_0$ is pumped at flow rate $F$ into a stirred, aerated vessel of volume $V$, and culture leaves through an overflow at the same rate. Two variables set by the experimenter control two properties of the culture:

- the dilution rate $D = F/V$ sets the growth rate: at steady state the specific growth rate equals $D$;
- the concentration $s_0$ of the limiting nutrient in the feed sets the cell density: at steady state the biomass is $Y(s_0 - s^*)$, where $Y$ is the yield.

The approach to the steady state is self-regulating. After inoculation the cells grow faster than they are washed out and use up the limiting nutrient; as its concentration falls, their growth rate falls (Monod's law), until it exactly balances dilution. If cells are added, they consume more nutrient and their growth rate drops below $D$; if cells are removed, the nutrient rises and they grow faster. The equations and the steady state ($s^* = K_sD/(\lambda_{\max} - D)$, independent of $s_0$) are derived in [7.6.39](/7.6.39#fml-39.1.2), where their linear stability is also discussed; here we use them to look at what the experimenter sees. The steady state holds only between limits. At very low $D$ the cells spend much of their energy on maintenance and many die. At high $D$ the residual nutrient rises steeply, and if $D$ exceeds the critical dilution rate $D_{\mathrm{c}} = \lambda_{\max}s_0/(K_s + s_0)$, which is just below the maximal growth rate, the cells cannot keep up with dilution and are washed out (panel B). Dense ($10^9\,\mathrm{mL^{-1}}$), moderate ($10^7$) or dilute ($10^5$) populations can be maintained at any growth rate below washout by choosing $s_0$.

Chemostat cultures provide exponentially growing cells at a known, adjustable growth rate for weeks, from which one can sample repeatedly. Much of what is known about bacterial physiology at submaximal growth rates, such as the increase in ribosome content with growth rate (the first growth law, [7.6.39](/7.6.39#sec-39.2.2)), came from chemostats. The low, steady nutrient concentrations also resemble many natural habitats, so chemostats are used in ecology and evolution: they select spontaneous mutants that scavenge the limiting nutrient better, and they can be used for enrichment, by raising $D$ until only the fastest-growing organism in a natural sample remains.

### 8.5.2. Competition for a Limiting Nutrient

When two species share the chemostat and are limited by the same nutrient, the outcome follows from the steady-state condition. Each species can persist only if the nutrient is at least the concentration at which its growth rate equals $D$.

**Formula 8.5.1 (Break-Even Concentration)** For a species with Monod parameters $\lambda_{\max}$ and $K_s$ in a chemostat at dilution rate $D < \lambda_{\max}$, the nutrient concentration at which its growth exactly balances dilution is

$$
R^* = \frac{K_s D}{\lambda_{\max} - D}.
$$
Of several species limited by the same nutrient, the one with the lowest $R^*$ draws the nutrient down to its own $R^*$, where the others grow slower than they are diluted, and excludes them.

This is the simplest form of the **competitive exclusion principle**, and $R^*$ is the quantity that Tilman (1982) used for resource competition in plants and algae ([7.19](/7.19)). Because $R^*$ depends on $D$, the winner can change with the dilution rate (figure below, panels C and D): a scavenger with a low $K_s$ but a modest $\lambda_{\max}$ wins at low $D$, an organism that grows fast only at high concentration wins at high $D$, and the two can coexist only at the single dilution rate where their $R^*$ values are equal. Coexistence of many species on few resources in nature therefore needs something more, such as fluctuations, spatial structure, cross-feeding or several limiting resources.

![The chemostat in practice. A: the apparatus (schematic): fresh medium with the limiting nutrient at concentration s0 is pumped at flow F into a stirred, aerated vessel of volume V, and culture leaves through an overflow; the dilution rate D = F/V sets the growth rate. B: a culture at steady state at D = 0.4 per hour after a step change of the pump at time 0 (model: Monod kinetics, maximal growth rate 1.0 per hour, Ks = 0.1 mM, s0 = 5 mM): at D = 0.8 per hour it settles at a new steady state; at D = 1.05 per hour, above the critical dilution rate of 0.98 per hour, the cells wash out. C: Monod curves of two species limited by the same nutrient, a scavenger (blue: maximal rate 0.6 per hour, Ks = 0.02 mM) and an organism that grows fast only at high concentration (orange: 1.2 per hour, 0.5 mM); dots mark the break-even concentrations R* at D = 0.3 and 0.65 per hour (the scavenger cannot grow at 0.65 per hour at all). D: competition from equal inocula: at D = 0.3 per hour (solid) the scavenger wins, at 0.65 per hour (dashed) the fast grower wins](./plots/chemostat.py)

### 8.5.3. The Turbidostat, Fed-Batch and High-Density Culture

**Definition 8.5.2 (Turbidostat)** A **turbidostat** is a continuous culture in which the turbidity of the culture is monitored and the flow of fresh medium is adjusted to keep it constant; all nutrients are in excess, and the cells grow at their maximal rate for the conditions.

The two devices are complementary. A chemostat works best at low dilution rates, where the limiting nutrient controls growth tightly; a turbidostat works best near the maximal growth rate, where a chemostat would be close to washout. Turbidostats are used to keep cells in exponential growth at a defined density and, in experimental evolution, to select for faster growth or for tolerance of a drug whose concentration is raised automatically (the "morbidostat").

Industrial production rarely uses true continuous culture, because contamination and the selection of nonproducing mutants are hard to avoid over long runs. The usual compromise is *fed-batch culture*: a batch culture to which a concentrated nutrient, usually the carbon source, is fed over time at a rate that keeps it limiting. Feeding at a rate that grows exponentially keeps the cells growing at a chosen rate below their maximum, which avoids overflow metabolism (the excretion of acetate by *E. coli* at high glucose uptake, [7.6.39](/7.6.39#sec-39.4)) and oxygen limitation, and allows cell densities of more than $100\,\mathrm{g}$ of dry mass per liter, a high-density culture.

## 8.6. Measuring Growth

### 8.6.1. Direct Counts

The total number of cells, living and dead, can be counted in a microscope. In a counting chamber such as the Petroff–Hausser chamber, a grid of known area is etched on a slide and a coverslip held at a known height above it, so that each square holds a known volume.

**Example 8.6.1** A Petroff–Hausser chamber has a grid of $1\,\mathrm{mm^2}$ divided into $25$ large squares, and a depth of $0.02\,\mathrm{mm}$. If a large square contains on average $12$ cells, the grid contains $12 \times 25 = 300$ cells in $0.02\,\mathrm{mm^3}$, that is $1.5 \times 10^4$ cells per $\mathrm{mm^3}$ and $1.5 \times 10^7$ cells per milliliter.

Microscopic counts are fast but imprecise; they need at least about $10^6$ cells per milliliter, they cannot tell live cells from dead ones without special stains, and small cells and debris are easily confused. For natural samples, cells are collected on a filter and stained with a DNA dye such as DAPI or SYBR Green, or with fluorescent probes for particular groups (fluorescence in situ hybridization, [7.11.29](/7.11.29)); stains that enter only cells with damaged membranes distinguish live from dead cells. **Flow cytometry** counts cells in a stream one at a time by their light scattering and fluorescence, thousands per second, and can sort them; it is the standard method for counting marine picoplankton. Electronic particle counters (Coulter counters) count and size cells by the change in electrical resistance as each passes through an aperture.

### 8.6.2. Viable Counts

**Definition 8.6.1 (Viable Count and Colony-Forming Unit)** A **viable count** (plate count) is the number of cells able to divide and form a colony, measured by spreading a known volume of a suitably diluted sample on, or mixing it into, a solid medium and counting the colonies after incubation. Because a colony may arise from a single cell or from a clump, the result is expressed in **colony-forming units** (CFU) per unit volume or mass.

In the spread-plate method, $0.1\,\mathrm{mL}$ or less of a dilution is spread over the surface of an agar plate; in the pour-plate method, $0.1$–$1.0\,\mathrm{mL}$ is mixed with molten agar cooled to about $45$–$50\,^\circ\mathrm{C}$, so colonies grow both on and in the agar (which some heat-sensitive cells do not survive). A dense culture must be diluted, usually in a series of tenfold steps, until the plates carry a countable number of colonies, conventionally between $30$ and $300$ (figure below, panel A). The concentration is the colony count divided by the volume plated and by the dilution; for example, $159$ colonies from $1\,\mathrm{mL}$ of a $10^{-3}$ dilution correspond to $1.59 \times 10^5\,\mathrm{CFU\,mL^{-1}}$.

The countable range has a statistical basis. If cells are randomly distributed in the sample, the number deposited on a plate follows a Poisson distribution, whose standard deviation is the square root of its mean ([3.1](/3.1)), so the relative error of a count of $c$ colonies is about $1/\sqrt{c}$: $18\,\%$ for $30$ colonies and $6\,\%$ for $300$. Plates with fewer colonies are imprecise; on plates with many more, colonies merge or inhibit one another and the count falls below the true number (panel B). Further errors come from pipetting, clumping, incomplete mixing and the choice of medium and incubation time. Replicate plates of the key dilutions are therefore used.

Viable counts are very sensitive, since a single viable cell in the sample plated can be detected, and with selective media they can target one group in a mixture: a medium with $7.5$–$10\,\%$ NaCl selects staphylococci from skin, and media selective for coliform bacteria are used to detect fecal contamination of water and food. Used to count all organisms in a natural sample, however, plate counts fail badly.

**Definition 8.6.2 (Great Plate Count Anomaly)** The **great plate count anomaly** is the observation that viable counts of natural samples, such as soil and seawater, are smaller by one to several orders of magnitude than direct microscopic counts of the same samples (Staley and Konopka 1985).

Part of the difference is due to dead cells, which microscopic counts include. Most of it, however, reflects the fact that no single medium and set of conditions suits more than a small fraction of the organisms in a natural community, many of which grow slowly, depend on other organisms or have not been cultured at all. This is one of the reasons for culture-independent methods based on DNA sequences ([7.8.14](/7.8.14), [7.11.29](/7.11.29)).

### 8.6.3. The Most Probable Number

When cells cannot be counted as colonies, for example because they grow only in liquid or are rare in a large sample, their concentration can be estimated statistically from the presence or absence of growth in replicate tubes.

**Definition 8.6.3 (Most Probable Number)** The **most probable number** (MPN) method estimates the concentration of viable cells from the pattern of positive tubes (showing growth or a specific reaction) in several replicate tubes inoculated with each of a series of dilutions: the MPN is the concentration under which the observed pattern is most probable.

If the cells are randomly distributed, a tube inoculated with volume $v$ of a sample containing $c$ cells per unit volume receives a Poisson number of cells with mean $cv$, and is positive with probability $1 - \mathrm{e}^{-cv}$. With $n_i$ tubes at volume $v_i$, of which $p_i$ are positive, the likelihood is

$$
L(c) = \prod_i \left(1 - \mathrm{e}^{-cv_i}\right)^{p_i}\,\mathrm{e}^{-cv_i(n_i - p_i)},
$$
and the MPN is its maximum ([3.3](/3.3)). Tables give the MPN and its confidence limits for the common designs with three or five tubes per dilution. For three tubes each of $0.1$, $0.01$ and $0.001\,\mathrm{g}$ of sample and the result $3$, $2$, $0$ positive tubes, the MPN is $93$ cells per gram (figure below, panel C). The method is imprecise (the $95\,\%$ interval spans roughly a factor of ten) but sensitive and simple, and it is still used to count coliforms in water and food and functional groups such as nitrifying or sulfate-reducing bacteria in soil and sediment.

### 8.6.4. Turbidity and Biomass

A suspension of cells looks cloudy because cells scatter light, and the amount of light scattered increases with the cell mass. A spectrophotometer measures the light that passes through a sample unscattered, as optical density (OD) at a stated wavelength, commonly $600\,\mathrm{nm}$ for bacteria (also $540$ or $660\,\mathrm{nm}$). For unicellular organisms the OD is proportional to cell mass and, at a given cell size, to cell number, but only at low density: at high density, light scattered by one cell can be scattered back into the detector by another, and the reading saturates (panel D). Before OD can stand in for counts, a standard curve against direct or viable counts must be made, and dense cultures are diluted into the linear range. The conversion is specific to the organism, its size and the instrument; for *E. coli* one OD unit at $600\,\mathrm{nm}$ corresponds roughly to $10^9$ cells per milliliter. Turbidity is quick, nondestructive and can be measured repeatedly on the same culture, which makes it the method of choice for following the growth of pure cultures, but it is misleading for organisms that clump, form filaments or grow as **biofilms** on the vessel walls.

![Measuring growth. A: serial tenfold dilution and spread plating of 0.1 mL from three of the dilutions of a sample with 1.6 × 10⁸ CFU per milliliter: only the plate with about 160 colonies is in the countable range; the concentration is the colony count divided by the volume plated and the dilution. B: the relative error of a plate count: the Poisson error 1/√c falls with the number of colonies c, while on crowded plates colonies merge and the count falls short (model with a plate that holds about 3000 colony areas); the total error is smallest between about 30 and 300 colonies. C: the most probable number for three tubes each of 0.1, 0.01 and 0.001 g of sample with 3, 2 and 0 positive tubes: the log-likelihood of the concentration peaks at 93 per gram; the shaded range is an approximate 95 % interval. D: optical density is proportional to cell density only at low density, so turbidity is calibrated with a standard curve (points) and dense cultures are diluted (rule-of-thumb calibration for *E. coli*, 1 OD unit = 8 × 10⁸ cells per milliliter)](./plots/counting.py)

Other measures of growth follow the mass of cells rather than their number: dry weight (cells are collected by centrifugation or filtration, washed and dried; about a quarter of the wet weight), total protein or DNA, the amount of a component proportional to living biomass such as ATP (measured by luciferase light) or a cell-wall constituent, and metabolic activity, such as the consumption of oxygen or substrate or the production of $\mathrm{CO_2}$ or acid. For filamentous fungi and actinomycetes, which do not consist of countable single cells, mass measures are the only practical ones.

| Method | Measures | Advantages | Limitations |
|---|---|---|---|
| Counting chamber | total cells | fast, cheap | imprecise, needs ≥ 10⁶ mL⁻¹, live and dead not distinguished |
| Epifluorescence counts on filters | total cells (or groups, with probes) | works on dilute natural samples, can identify groups | laborious; stains vary in specificity |
| Flow cytometry | total cells, size and fluorescence | very fast, thousands of cells, sorting | expensive instrument; clumps and debris |
| Plate count | viable cells (CFU) | very sensitive, selective media for target groups | slow (one to several days), only cells that grow on the medium, many sources of error |
| Most probable number | viable cells | for organisms that grow only in liquid or are rare; functional groups | imprecise (factor of about ten) |
| Turbidity (OD) | cell mass | fast, nondestructive, repeatable | needs a standard curve; nonlinear at high density; clumps and biofilms |
| Dry weight, protein, ATP | biomass | applies to filamentous organisms | insensitive, destructive (dry weight); ATP varies with physiology |

## Summary

- Most bacteria divide by **binary fission** (Definition 8.1.1): after replication and segregation of the chromosome, the **divisome** (Definition 8.1.2), assembled on the FtsZ ring, builds a septum at midcell. Nucleoid occlusion and the Min system place the ring; MreB directs dispersed wall growth in rods, crescentin curves *Caulobacter*. Some bacteria bud or grow from one pole.
- Peptidoglycan is made in three compartments: the Park nucleotide in the cytoplasm, lipid I and lipid II on the bactoprenol carrier in the membrane, and transglycosylation and transpeptidation outside by *penicillin-binding proteins* and SEDS proteins, balanced by autolysins. Each stage is the target of an antibiotic.
- Exponential growth (Formula 8.3.1): $N = N_0 2^n$, $g = t/n$, $k = \ln 2/g$; plotted on a semilogarithmic scale it is a straight line.
- A **batch culture** has a **growth curve** with a **lag phase**, an **exponential phase**, a **stationary phase** and a **death phase** (Definitions 8.4.1–8.4.2). Lag reflects the state of the inoculum and the medium; stationary cells are reprogrammed for survival; the death phase leads to long-term stationary cultures; total and viable counts diverge after growth.
- Synchronous cultures are made by selection or induction and lose synchrony within a few generations.
- In a **continuous culture** (Definition 8.5.1) such as the **chemostat**, the dilution rate sets the growth rate and the feed concentration the density; above the critical dilution rate the culture washes out. Of species limited by the same nutrient, the one with the lowest break-even concentration $R^*$ wins (Formula 8.5.1). The **turbidostat** (Definition 8.5.2) holds the density constant at maximal growth; **fed-batch culture** reaches high densities.
- Growth is measured by direct counts, **viable counts** in **CFU** (Definition 8.6.1, countable range 30–300 by Poisson statistics), the **most probable number** (Definition 8.6.3), turbidity with a standard curve, and biomass. Plate counts of natural samples show the **great plate count anomaly** (Definition 8.6.2).

## Questions

1. A culture is inoculated with $2 \times 10^4$ cells per milliliter and after a lag of $1\,\mathrm{h}$ grows exponentially with a generation time of $25\,\mathrm{min}$. How many cells per milliliter are there after $5\,\mathrm{h}$, and what is $k$?

   **Answer** Exponential growth lasts $4\,\mathrm{h} = 240\,\mathrm{min}$, that is $n = 240/25 = 9.6$ generations, so $N = 2 \times 10^4 \times 2^{9.6} = 2 \times 10^4 \times 776 = 1.6 \times 10^7\,\mathrm{mL^{-1}}$. The growth rate constant is $k = 0.693/(25/60\,\mathrm{h}) = 1.66\,\mathrm{h^{-1}}$.

2. Why do β-lactam antibiotics kill growing bacteria by lysis, but have little effect on cells in stationary phase? What would you expect if an autolysin-deficient mutant were treated with penicillin?

   **Answer** β-Lactams inactivate the transpeptidases (PBPs) that cross-link new strands. In growing cells, autolysins keep opening the existing wall for insertion; without cross-linking the new material is weak, holes appear and the cell bursts under its turgor. Nongrowing cells make little new wall, so blocking its synthesis has little consequence. An autolysin-deficient mutant stops growing in penicillin but lyses much less: it is inhibited rather than killed (penicillin tolerance), which shows that killing requires the cell's own hydrolases.

3. A chemostat with a vessel of $1\,\mathrm{L}$ is fed at $0.3\,\mathrm{L\,h^{-1}}$ with medium containing $2\,\mathrm{g\,L^{-1}}$ glucose. The organism has $\lambda_{\max} = 0.8\,\mathrm{h^{-1}}$, $K_s = 0.01\,\mathrm{g\,L^{-1}}$ and a yield of $0.5\,\mathrm{g}$ of cells per gram of glucose. Find the doubling time, the residual glucose and the biomass at steady state. What happens if the pump is set to $0.85\,\mathrm{L\,h^{-1}}$? If the feed glucose is doubled?

   **Answer** $D = 0.3\,\mathrm{h^{-1}}$, so the cells grow at $0.3\,\mathrm{h^{-1}}$: doubling time $\ln 2/0.3 = 2.3\,\mathrm{h}$. Residual glucose $s^* = 0.01 \times 0.3/(0.8 - 0.3) = 0.006\,\mathrm{g\,L^{-1}}$; biomass $0.5\,(2 - 0.006) \approx 1.0\,\mathrm{g\,L^{-1}}$. At $D = 0.85\,\mathrm{h^{-1}}$, above $D_{\mathrm{c}} = 0.8 \times 2/2.01 = 0.796\,\mathrm{h^{-1}}$, the culture washes out. Doubling the feed glucose doubles the biomass (to about $2.0\,\mathrm{g\,L^{-1}}$) but leaves the growth rate and the residual glucose unchanged.

4. From a sample, $0.1\,\mathrm{mL}$ of the $10^{-4}$, $10^{-5}$ and $10^{-6}$ dilutions are spread on plates, giving more than $1000$, $212$ and $19$ colonies. Calculate the viable count, and explain why the other two plates are not used. A direct count of the same sample gives $8 \times 10^8$ cells per milliliter; give two possible reasons for the difference.

   **Answer** The $10^{-5}$ plate is in the countable range: $212/(0.1 \times 10^{-5}) = 2.1 \times 10^8\,\mathrm{CFU\,mL^{-1}}$. The first plate is too crowded (colonies merge, so it underestimates), and the last has too few colonies for precision (relative error about $1/\sqrt{19} = 23\,\%$). The direct count is higher because it includes dead (and viable but nonculturable) cells and because clumps or chains give one colony from several cells; for a natural sample the main reason would be that most organisms do not grow on the medium used (the great plate count anomaly).

5. Two bacteria are limited by the same amino acid in a chemostat: A has $\lambda_{\max} = 1.0\,\mathrm{h^{-1}}$, $K_s = 10\,\mu\mathrm{M}$; B has $\lambda_{\max} = 0.5\,\mathrm{h^{-1}}$, $K_s = 1\,\mu\mathrm{M}$. Which wins at $D = 0.2$ and at $D = 0.45\,\mathrm{h^{-1}}$? At which dilution rate are they equal?

   **Answer** $R^*_A = 10D/(1 - D)$, $R^*_B = D/(0.5 - D)$ in micromolar. At $D = 0.2$: $R^*_A = 2.5$, $R^*_B = 0.67$, so B wins. At $D = 0.45$: $R^*_A = 8.2$, $R^*_B = 9.0$, so A wins. They are equal when $10(0.5 - D) = 1 - D$, that is $D = 4/9 = 0.44\,\mathrm{h^{-1}}$; only at this dilution rate can they coexist.
