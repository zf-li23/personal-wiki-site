---
title: "Microbial Eukaryotes II: Fungi"
description: "What a fungus is: absorptive nutrition, chitin and glucan walls, ergosterol, hyphae and yeasts, and the place of fungi among the opisthokonts; tip growth, the Spitzenkörper, septa and the specialized hyphae, with a model of mycelial growth; the yeast cell, budding and fission, three yeast life cycles, mating types and yeast as a model and industrial organism; dimorphism; asexual and sexual spores, the dikaryon and the parasexual cycle; the phylogeny of fungi from Cryptomycota and Microsporidia to the Dikarya; fungi as decomposers, symbionts and pathogens of plants and insects; fungal metabolites and mycotoxins; and the mycoses of humans and antifungal resistance."
---

Fungi are the decomposers of the land. They digest wood, leaves and dung, form the mycorrhizae through which most plants take up phosphate, and partner algae and cyanobacteria in lichens; they are the most damaging pathogens of crops, and a few dozen species cause human disease, mostly in people whose immunity is impaired. Fungi also gave us bread, beer and wine, penicillin, statins and cyclosporin, and two of the most important model organisms of eukaryotic biology, the budding and fission yeasts. This chapter describes how fungi are built and grow, how they reproduce, how their main lineages are related, and what they do in nature and to us. Fungi are opisthokonts, closer to animals than to plants or to the protists of [7.11.20](/7.11.20); their origin is discussed in [7.10.28](/7.10.28#sec-28.4), the genetics of yeast and *Neurospora* in [7.4.9](/7.4.9), and the antifungal drugs in [7.11.14](/7.11.14#sec-14.10.1). Mycorrhizae and lichens are treated as symbioses in [7.11.31](/7.11.31).

## 21.1. What Is a Fungus?

**Definition 21.1.1 (Fungus)** A **fungus** is a member of the kingdom Fungi, the clade of opisthokont eukaryotes that feed by absorption — secreting digestive enzymes into their surroundings and taking up the products — and that grow as filaments (hyphae) or as single cells (yeasts), with walls of chitin and β-glucans and with ergosterol as the main sterol of their membranes.

Each feature of the definition has consequences.

- Nutrition: fungi are chemoorganotrophs that cannot engulf food. A hypha grows into its substrate, secretes cellulases, ligninolytic enzymes, proteases and lipases, and absorbs sugars, amino acids and other small molecules across its plasma membrane. Fungi live as saprotrophs on dead material, as symbionts of plants and animals, or as parasites, and many switch between these ways of life.
- Walls: the fungal wall is built of **chitin** (β-1,4-linked *N*-acetylglucosamine, [7.1.10](/7.1.10#sec-10.3)) and β-1,3- and β-1,6-glucans, covered by mannoproteins in yeasts; it is made at the growing tip by enzymes in the plasma membrane. Neither chitin nor β-glucans occur in human cells, which makes the synthesis of the wall a target of antifungal drugs (echinocandins inhibit β-1,3-glucan synthase).
- Membranes: ergosterol replaces the cholesterol of animals. The polyenes bind it and the azoles inhibit its synthesis ([7.11.14](/7.11.14#sec-14.10.1)).
- Other markers: fungi synthesize lysine by the α-aminoadipate pathway, unlike plants, bacteria and oomycetes; they store glycogen and trehalose, not starch; most undergo a **closed mitosis**, in which the nuclear envelope does not break down.

Fungi and animals are sister groups within the opisthokonts, named for the single posterior flagellum of their motile cells — the sperm of animals and the zoospores of chytrids. Most fungi have lost the flagellum. About 150,000 species of fungi have been described, but surveys of environmental DNA suggest that the true number lies in the millions, most of them never cultured.

## 21.2. Hyphae and Mycelium

### 21.2.1. Tip Growth

**Definition 21.2.1 (Hypha and Mycelium)** A **hypha** is a tubular filament of a fungus, bounded by a wall and growing only at its tip; a **mycelium** is the network of branching hyphae that makes up the body of a filamentous fungus.

A hypha extends only at its apex, which may advance at a micrometer per second in fast-growing species, while the wall behind it rigidifies. Vesicles made by the Golgi apparatus, carrying chitin synthases, glucan synthases and wall material, travel along microtubules toward the tip and accumulate just behind it in the *Spitzenkörper* ("apical body"), a dense cluster of vesicles with actin filaments that acts as a vesicle supply center: it releases vesicles to fuse with the plasma membrane at the very tip, and its position determines the direction of growth, so that if the Spitzenkörper moves to one side, the hypha turns (panel A of the figure below). Turgor pressure drives the extension of the plastic apical wall. Branches arise behind the tip, so that the number of tips, and hence the total rate of extension, grows with the length of the mycelium.

In most fungi the hyphae are divided by cross-walls, *septa*, into compartments that usually contain one or two nuclei; a central pore in each septum allows cytoplasm, organelles and even nuclei to move between compartments. In ascomycetes the pore is simple and can be plugged within seconds by a *Woronin body*, a dense organelle derived from peroxisomes, when a hypha is damaged, so that the rest of the mycelium does not bleed out; in mushroom-forming basidiomycetes the pore is surrounded by a barrel-shaped swelling (the dolipore) capped by membrane (the parenthesome). The hyphae of the Mucoromycota have no regular septa: they are *coenocytic*, a continuous tube of cytoplasm with many nuclei, and septa form only to seal off reproductive structures or injured parts.

![A: the tip of a septate hypha (ascomycete, schematic). Secretory vesicles move toward the tip along microtubules and collect in the Spitzenkörper, which supplies them to the apical membrane; behind the tip, septa with central pores and Woronin bodies divide the hypha into compartments with nuclei and mitochondria. B, C: a simple model of mycelial growth. Each tip extends at a constant rate ($v = 100\,\mu\mathrm{m\,h^{-1}}$) with a small random change of direction, and a hypha branches at 45° when the length it has grown since its last branch exceeds a threshold drawn around the hyphal growth unit $G = 150\,\mu\mathrm{m}$. B shows the mycelium after 13 h; C, on a logarithmic scale, the total length $L$ and the number of tips $N$, which grow exponentially at the same rate with $L/N \approx G$, while the radius of the colony grows linearly.](./plots/hyphal-growth.py)

**Formula 21.2.1 (Hyphal Growth Unit)** If every tip of a mycelium extends at rate $v$ and branching keeps the mean length of hypha per tip at a constant value $G$, the *hyphal growth unit*, then the total length $L$ and the number of tips $N = L/G$ satisfy

$$
\frac{\mathrm{d}L}{\mathrm{d}t} = vN = \frac{v}{G}L, \qquad L(t) = L_0\,\mathrm{e}^{vt/G},
$$
so that a mycelium grows exponentially at the specific rate $\mu = v/G$, like a population of cells, although each hypha extends at a constant speed.

Measured growth units are of the order of a hundred micrometers, and the formula links the two descriptions of fungal growth: the biomass of a young mycelium in liquid culture increases exponentially, while the radius of a colony on a plate increases linearly, because only the tips near the margin advance into new medium (panel C of the figure above). Older parts of a colony stop growing as the substrate under them is exhausted, and nutrients are moved through the mycelium to the growing front.

### 21.2.2. Specialized Hyphae

Hyphae differentiate into structures that anchor, spread, invade, survive or capture.

| Structure | Form and function | Examples |
|---|---|---|
| Rhizoids | short, branched hyphae that anchor the mycelium and absorb nutrients | *Rhizopus*, chytrids |
| Stolons | aerial hyphae arching over the substrate and rooting with rhizoids, spreading the colony | *Rhizopus* |
| Haustoria | branches that penetrate the wall of a living plant cell and invaginate its membrane, taking up nutrients without killing it | rusts, powdery mildews (and the oomycete downy mildews) |
| Appressoria | swollen cells at the tip of a germ tube that attach to a leaf and force a peg through the cuticle by turgor | rice blast fungus *Magnaporthe oryzae* |
| Sclerotia | hard, compact resting bodies of hyphae with a melanized rind | *Sclerotinia*, ergot of *Claviceps* |
| Rhizomorphs | root-like cords of parallel hyphae that conduct water and nutrients over long distances | honey fungi (*Armillaria*) |
| Stromata | compact masses of hyphae on or in which fruiting bodies are formed | many ascomycetes |
| Traps | adhesive networks, knobs or constricting rings that catch nematodes | *Arthrobotrys* |

The appressorium of *Magnaporthe* is the clearest example of the mechanics of fungal invasion: its wall is impregnated with melanin, which makes it impermeable to glycerol; the cell accumulates glycerol to a high concentration, and the resulting turgor, several megapascals, is focused on a narrow penetration peg that punctures the leaf. In the constricting rings of nematode-trapping fungi, three cells swell within a fraction of a second when a nematode enters the ring and hold it fast.

In submerged culture, mycelia either grow as dispersed filaments or form compact pellets, depending on the density of spores in the inoculum, the shear and the medium; the morphology changes the viscosity of the broth, the transfer of oxygen and the yield of products such as penicillin and citric acid, and is controlled in industrial fermentations.

### 21.2.3. Molds and Colonies

**Definition 21.2.2 (Mold)** A **mold** is a filamentous fungus that grows as a mycelium and forms asexual spores on aerial hyphae, without large fruiting bodies; the word describes a growth form, not a taxonomic group.

The colonies of microorganisms on agar reflect the organization of their cells, and microbiologists recognize the main groups by eye.

| Feature | Bacteria | Yeasts | Actinomycetes | Molds |
|---|---|---|---|---|
| Surface | moist, smooth or wrinkled | moist, smooth, glossy | dry, powdery, compact | dry, velvety, cottony or powdery |
| Size and growth | small to large; fast | larger and thicker than bacteria; fast | small; slow | large, spreading; fast |
| Attachment to the agar | lifted easily | lifted easily | firmly embedded | firmly embedded |
| Color | various; same on both sides | mostly cream or white (some red, black) | often different above and below | pigmented spores; different above and below |
| Smell | various | often fruity or alcoholic | earthy (geosmin) | musty |

The difference between moist and dry colonies follows from the cells: the single cells of bacteria and yeasts lie in a film of water held between them by capillarity, whereas the aerial hyphae and spores of actinomycetes and molds rise into the air, and the substrate hyphae grow into the agar and anchor the colony.

## 21.3. Yeasts and Dimorphism

### 21.3.1. The Yeast Cell

**Definition 21.3.1 (Yeast)** A **yeast** is a fungus that grows predominantly as single cells, which divide by budding or fission; like "mold", the word names a growth form that has evolved independently in ascomycetes and basidiomycetes.

The budding yeast *Saccharomyces cerevisiae* has oval cells about 5–10 µm long, with a wall of an inner layer of β-glucans and a little chitin and an outer layer of mannoproteins; enzymes from the gut of snails or from bacteria digest the wall to give protoplasts. Inside are a nucleus, mitochondria, a large vacuole that stores amino acids, phosphate and ions and acts as a lysosome, and in most strains a 2-µm plasmid, a 6.3-kb circle with no known function for the cell that is maintained at about 50 copies in the nucleus and has served as a basis for yeast vectors. *S. cerevisiae* is a **facultative anaerobe**, and even in the presence of oxygen it ferments glucose to ethanol when sugar is abundant (the Crabtree effect), the basis of brewing, winemaking and the rising of bread ([7.11.5](/7.11.5)).

In budding, a small outgrowth of the mother cell enlarges, receives a nucleus by mitosis through the neck, and separates; a ring of chitin remains on the mother as a *bud scar* and on the daughter as a birth scar. Because a new bud never forms at an old scar, the number of scars counts the divisions of a cell, and a mother cell produces a limited number of daughters, typically 20–30, before it stops dividing — the replicative lifespan used as a model of aging. When daughter cells stay attached after budding, they form chains of elongated cells, *pseudohyphae*, which differ from true hyphae in being constricted at every septum. The fission yeast *Schizosaccharomyces pombe* grows at its ends and divides by a medial septum, like a bacterium, so that its cells have constant width and a length that measures their position in the cell cycle — the property that made it the organism in which the genetic control of the cell cycle was discovered ([7.3.20](/7.3.20)).

### 21.3.2. Yeast Life Cycles and Mating Types

Yeasts reproduce sexually by forming asci with ascospores (in ascomycete yeasts) or basidiospores (in basidiomycete yeasts). Their life cycles differ in which ploidy grows vegetatively (see the figure below).

![Three life cycles of ascomycete yeasts (shaded: haploid and diploid phases). A: in *Saccharomyces cerevisiae* both haploid and diploid cells bud indefinitely; haploids of mating types a and α fuse to give diploids, which form asci with four ascospores when starved of nitrogen on a poor carbon source. B: in *Schizosaccharomyces pombe* the vegetative cells are haploid and divide by fission; two cells of opposite mating type conjugate, and the zygote undergoes meiosis at once to form an ascus of four spores (eight in *S. octosporus*, after a postmeiotic mitosis). C: in *Saccharomycodes ludwigii* the vegetative cells are diploid; meiosis gives four ascospores, which fuse in pairs inside the ascus, so that the haploid phase is confined to the ascus.](./plots/yeast-life-cycles.py)

In *S. cerevisiae* the mating type is set by the allele at the *MAT* locus: *MATa* cells secrete the peptide pheromone a-factor and *MAT*α cells α-factor, each arresting the cell cycle of the other type and inducing the projections ("shmoos") through which the cells fuse. Wild strains are often *homothallic*: a haploid cell switches its mating type after a division by cutting the *MAT* locus with the HO endonuclease and replacing its allele, by **gene conversion**, with a copy of the opposite allele from one of two silent loci, *HML* and *HMR*, kept transcriptionally silent by heterochromatin ([7.4.17](/7.4.17#sec-17.8)). Only the mother cell switches, so that a single spore soon gives cells of both mating types, which mate to form diploids. Laboratory strains carry mutant *ho* alleles and are *heterothallic*, with stable mating types, so that haploids and diploids can be maintained and crossed at will, and the ascospores of a diploid can be dissected for **tetrad analysis** ([7.4.9](/7.4.9)).

### 21.3.3. Yeast as a Model and as an Industrial Organism

*S. cerevisiae* was the first eukaryote whose genome was sequenced (1996): about 12 Mbp in 16 chromosomes, with some 6,000 genes, few introns and efficient homologous recombination, which allows any gene to be replaced precisely. It combines the genetics of a microbe — haploid growth, mutants selected on plates, crosses analyzed by tetrads — with the cell biology of a eukaryote, and was the organism in which the secretory pathway, the cell-division-cycle genes, autophagy, prions as heritable protein conformations, the **yeast two-hybrid system** and the systematic deletion of every gene were developed. It remains the main production organism of fermented beverages, baker's yeast, bioethanol and many recombinant proteins and metabolites, such as vaccine antigens and the antimalarial precursor artemisinic acid. Other industrial yeasts include *Komagataella* (formerly *Pichia*) *pastoris* for proteins, *Yarrowia lipolytica* for lipids and *Kluyveromyces lactis* for lactose.

### 21.3.4. Dimorphism

**Definition 21.3.2 (Dimorphism)** **Dimorphism** in fungi is the ability of one species to grow either as a yeast or as a mycelium, switching between the two forms in response to temperature, nutrients, carbon dioxide or contact with a host.

Many of the fungi that cause systemic infections in humans are *thermally dimorphic*: they grow as molds in soil at environmental temperatures and produce airborne spores, and convert after inhalation, at 37 °C, to a yeast (*Histoplasma capsulatum*, *Blastomyces dermatitidis*, *Paracoccidioides*, *Talaromyces marneffei*, *Sporothrix*) or to large spherules filled with endospores (*Coccidioides*). The tissue form evades phagocytes better, and the switch is required for virulence. *Candida albicans* shows the reverse pattern: it grows as budding yeast in culture and as a commensal, and forms germ tubes, true hyphae and pseudohyphae in response to body temperature with serum, neutral pH and $\ce{CO2}$; the hyphae invade tissue and secrete a peptide toxin, candidalysin, that damages epithelial cells, while the yeast form disseminates in the blood.

## 21.4. Spores and Reproduction

### 21.4.1. Asexual Spores

Fungi reproduce asexually by fragments of mycelium, by budding or fission and above all by spores, which are small, numerous, often pigmented and dispersed by air, water or animals. Their form and the structures that bear them are the main characters of fungal identification (see the spore figure below).

**Definition 21.4.1 (Sporangiospore and Conidium)** A **sporangiospore** is an asexual spore formed by cleavage of the cytoplasm inside a sac, the sporangium, at the tip of a sporangiophore; a **conidium** is an asexual spore formed outside any sac, by budding or by the separation of a cell from the tip or side of a hypha or of a specialized conidiophore.

| Spore | Formation | Examples |
|---|---|---|
| Zoospore | flagellated, formed in a sporangium; swims | chytrids, *Allomyces* |
| Sporangiospore | nonmotile, formed in a sporangium | *Rhizopus*, *Mucor* |
| Conidium | budded from phialides or other conidiogenous cells, often in chains | *Aspergillus*, *Penicillium* |
| Arthroconidium (arthrospore) | from the fragmentation of a hypha at its septa | *Geotrichum*, *Coccidioides* |
| Blastoconidium | budded from a yeast cell or hypha | *Candida*, *Cryptococcus* |
| Chlamydospore | a thick-walled resting cell within or at the end of a hypha | *Candida albicans*, many molds |
| Ballistospore | shot from a sterigma by the sudden fusion of a water drop | the yeast *Sporobolomyces* |

The conidiophores of *Aspergillus* carry a swollen vesicle covered with phialides, each extruding a chain of conidia, while those of *Penicillium* branch like a brush (from the Latin *penicillus*). Spores of molds are produced in astronomical numbers and are everywhere in the air: a person inhales hundreds to thousands of *Aspergillus fumigatus* conidia a day.

![Spores of fungi (schematic, not to a common scale). Top row, asexual: sporangiospores in a sporangium with a central columella (*Rhizopus*); conidia in chains on the phialides of an *Aspergillus* conidiophore; arthroconidia formed by fragmentation of a hypha (*Geotrichum*); a thick-walled chlamydospore (*Candida albicans*). Bottom row, sexual: a zygospore between two suspensors (*Rhizopus*); eight ascospores in the ascus of *Neurospora*, in an ordered octad; four basidiospores on the sterigmata of a basidium (*Agaricus*); and, for comparison, blastoconidia budding from a yeast cell, with bud scars.](./plots/spore-types.py)

### 21.4.2. Sexual Reproduction and the Dikaryon

Sexual reproduction in fungi has three steps that can be separated in time: *plasmogamy*, the fusion of cytoplasm of two cells; *karyogamy*, the fusion of their nuclei; and meiosis. In most fungi the diploid phase is brief, and meiosis follows karyogamy at once. In the Dikarya (ascomycetes and basidiomycetes) plasmogamy and karyogamy are separated by a phase in which the two parental nuclei coexist, unfused, in each cell.

**Definition 21.4.2 (Dikaryon)** A **dikaryon** is a fungal hypha or cell containing two genetically different haploid nuclei, one from each parent, that divide in step without fusing; it is written $n + n$. A mycelium with more than one kind of nucleus in any arrangement is a **heterokaryon** ([7.3.3](/7.3.3)).

Mating is controlled by mating-type loci. In heterothallic species, only cells of different mating type can fuse; homothallic species are self-fertile. Ascomycetes and many fungi have two mating types, but the mushroom-forming basidiomycetes have two unlinked mating-type loci, one encoding homeodomain transcription factors and the other pheromones and their receptors, each with many alleles; a split-gill fungus, *Schizophyllum commune*, has more than 20,000 mating types, so that almost any two individuals are compatible while sibling spores mate with only a quarter of their siblings.

The sexual spores define the main groups of fungi.

**Definition 21.4.3 (Zygospore and Basidiospore)** A **zygospore** is a thick-walled resting spore formed by the fusion of two gametangia of compatible hyphae, in which karyogamy and later meiosis take place (Mucoromycota and Zoopagomycota). A **basidiospore** is a haploid sexual spore formed outside a basidium, a cell in which karyogamy and meiosis take place, usually four on short stalks (sterigmata) at its apex (Basidiomycota).

The **ascospores** of ascomycetes are formed inside an **ascus** ([7.4.9](/7.4.9), Definition 9.1.1), usually four or, after a postmeiotic mitosis, eight; asci are borne free in yeasts and in fruiting bodies (ascocarps) in most filamentous ascomycetes. The oospores of oomycetes are not fungal spores at all ([7.11.20](/7.11.20#sec-20.5.3)). Many fungi, including many important pathogens and industrial strains, reproduce sexually rarely or have never been seen to do so; they were once classified in an artificial group, the "Deuteromycota" or fungi imperfecti. Molecular phylogenies place them among the ascomycetes and basidiomycetes, and sexual cycles, or at least intact mating-type genes, have since been found in many of them, including *Aspergillus fumigatus* and *Penicillium chrysogenum*; since 2013 a fungus has one name, rather than separate names for its asexual and sexual stages.

### 21.4.3. The Parasexual Cycle

In fungi without a sexual cycle, recombination can still occur through the **parasexual cycle**, discovered by Guido Pontecorvo in *Aspergillus nidulans* in the 1950s. Hyphae of two strains fuse into a heterokaryon; rarely, two different nuclei fuse into a diploid nucleus, which divides by mitosis and can be selected when the haploid strains carry complementary nutritional markers; in the diploid, **mitotic recombination** produces homozygous segments, and nondisjunction leads to the loss of chromosomes and back to haploids that carry whole chromosomes of either parent in new combinations (haploidization). The cycle was used to map genes to chromosomes in *Aspergillus* and other fungi that lack sexual crosses, and the pathogen *Candida albicans*, a diploid that has no meiosis, uses a related cycle of mating, tetraploidy and chromosome loss.

## 21.5. The Phylogeny and Diversity of Fungi

### 21.5.1. The Main Lineages

Fungi were long classified by their sexual spores into four phyla — chytrids, zygomycetes, ascomycetes and basidiomycetes. Molecular phylogenies kept the last two as the Dikarya, split the chytrids into several lineages and dissolved the zygomycetes, which are paraphyletic, while adding parasitic groups that are related to fungi but were never thought to be fungi at all (see the phylogeny below).

![The main lineages of fungi, with one representative genus each and animals as the outgroup (after the classifications of Spatafora and colleagues, 2016, and James and colleagues, 2020; the relationships of Cryptomycota, Microsporidia and Aphelida, here grouped as Opisthosporidia, are debated). Columns: a flagellated stage (filled), the vegetative body and the sexual spore. The flagellum was lost several times; the dikaryon and regularly septate hyphae unite the Dikarya.](./plots/fungal-tree.py)

**Definition 21.5.1 (Chytrid)** A **chytrid** is a member of the Chytridiomycota, aquatic and soil fungi that reproduce by zoospores with a single posterior flagellum and grow as a single cell (thallus) with branching rhizoids or as a chain of thalli, without true hyphae.

**Definition 21.5.2 (Microsporidia)** The **microsporidia** are obligate intracellular parasites of animals and protists, related to fungi, that infect host cells as small spores which evert a coiled *polar tube* and inject their contents (the sporoplasm) through it into the host cell.

- Opisthosporidia: the Cryptomycota (*Rozella*, parasites of chytrids and oomycetes, which have a flagellated zoospore but a wall only in resting stages), the Aphelida, parasites of algae, and the Microsporidia. Microsporidia were once thought to be primitive eukaryotes without mitochondria; they have mitosomes ([7.11.3](/7.11.3#sec-3.6)), and genomes reduced to as little as about 2–3 Mbp, smaller than that of *Escherichia coli*, in *Encephalitozoon*. They import ATP from their host through transporters acquired from bacteria. Microsporidia infect insects (the pébrine disease of silkworms studied by Pasteur), fish and crustaceans, and opportunistically humans with AIDS.
- Chytridiomycota: the chytrids decompose pollen, chitin and plant remains in water and soil, and parasitize algae, which makes them important in freshwater food webs. *Batrachochytrium dendrobatidis* infects the keratinized skin of amphibians and disrupts its exchange of electrolytes; spread from East Asia through the global trade in amphibians, it and its relative *B. salamandrivorans* have contributed to the decline of hundreds of amphibian species and the extinction of dozens, the greatest loss of biodiversity attributed to a single pathogen. Anaerobic chytrids of the Neocallimastigomycota live in the rumen and digest plant fiber with hydrogenosomes.
- Blastocladiomycota: *Allomyces*, a water mold with an alternation of haploid and diploid generations and sporic meiosis, unusual among fungi.
- Zoopagomycota: parasites and pathogens of animals and other fungi, among them the insect-killing *Entomophthora*, whose infected flies climb to high places before they die and shower spores on the flies below.
- Mucoromycota: the bread molds *Rhizopus* and *Mucor*, with coenocytic hyphae, sporangiospores and zygospores; the Mortierellomycotina of soil; and the Glomeromycotina (treated by some authors as the phylum Glomeromycota), the fungi of arbuscular mycorrhizae (Section 21.6.2), which have no known sexual stage and multinucleate spores.
- Dikarya: Ascomycota and Basidiomycota, together more than 95% of described fungal species.

### 21.5.2. Ascomycota

**Definition 21.5.3 (Ascomycota)** **Ascomycota** is the phylum of fungi that form their meiotic spores, the ascospores, inside an ascus. It is the largest phylum of fungi, with yeasts and filamentous species whose hyphae have simple septal pores and Woronin bodies, and most of its members also reproduce asexually by conidia.

The Ascomycota have three subphyla. The Taphrinomycotina include the fission yeast *Schizosaccharomyces*, the plant pathogen *Taphrina* (peach leaf curl) and *Pneumocystis*, a parasite of the lungs of mammals that has no ergosterol in its membrane. The Saccharomycotina are the budding yeasts — *Saccharomyces*, *Candida*, *Komagataella*. The Pezizomycotina are filamentous ascomycetes, nearly all of which form asci in fruiting bodies (ascocarps) of three main kinds: closed spherical cleistothecia, from which the spores escape when the wall breaks (*Aspergillus*, *Penicillium*, the powdery mildews); flask-shaped perithecia with an opening (*Neurospora*, *Magnaporthe*, *Claviceps*); and open, cup-shaped apothecia lining a surface with asci (cup fungi, most lichens). Morels (*Morchella*) and truffles (*Tuber*), the largest ascocarps, are modified apothecia; truffles, which fruit underground, attract animals with their smell to dig them up and disperse the spores. The Pezizomycotina include the main plant pathogens among ascomycetes, the molds of food and the producers of most fungal antibiotics and mycotoxins (Section 21.7), and most of the fungi of lichens.

### 21.5.3. Basidiomycota

**Definition 21.5.4 (Basidiomycota)** **Basidiomycota** is the phylum of fungi that form their meiotic spores, the basidiospores, outside a basidium; their mycelia spend most of their life as dikaryons, kept in order in the mushroom-forming species by clamp connections.

The Basidiomycota have three subphyla: the Pucciniomycotina, which include the rusts; the Ustilaginomycotina, which include the smuts; and the Agaricomycotina, which include the mushrooms, bracket fungi, puffballs, jelly fungi and the yeast *Cryptococcus*.

In a mushroom-forming species the spore germinates into a short-lived monokaryotic mycelium; when two compatible monokaryons meet, their hyphae fuse and the nuclei of each migrate through the other's mycelium, establishing a dikaryon that can grow for years (panel A of the figure below). At each division of a dikaryotic tip cell, a hook-like *clamp connection* ensures that the two daughter cells each receive one nucleus of each kind. When conditions are favorable, usually after rain, the mycelium builds a fruiting body, the basidiocarp; in mushrooms, the basidia line the gills or pores under the cap in a fertile layer, the hymenium, and each produces four basidiospores, which are shot from their sterigmata one by one and fall between the gills to be carried away by the air. Mushrooms of the genera *Agaricus*, *Lentinula* (shiitake), *Pleurotus* (oyster mushrooms) and others are cultivated on composted or lignocellulosic substrates; some of the most poisonous species belong to *Amanita*, whose amatoxins, especially α-amanitin, inhibit RNA polymerase II ([7.2.12](/7.2.12)) and destroy the liver.

![A: the life cycle of a mushroom-forming basidiomycete. Haploid basidiospores germinate into monokaryotic mycelia; plasmogamy between compatible mycelia gives a dikaryotic mycelium ($n + n$), which forms the basidiocarp; karyogamy in the young basidium gives the only diploid nucleus, which undergoes meiosis at once to give four basidiospores. B: a clamp connection. The two nuclei (orange and blue) of the apical cell divide at the same time, one of them inside a backward-growing hook; septa separate the products and the hook fuses with the cell behind, so that both the new apical cell and the cell behind it again contain one nucleus of each mating type.](./plots/mushroom-cycle.py)

The rusts and smuts are plant pathogens without large fruiting bodies. Rusts are obligate biotrophs with the most complex life cycles of any fungi: *Puccinia graminis*, the wheat stem rust, produces five kinds of spores and alternates between wheat and barberry, so that the eradication of barberry in North America in the twentieth century helped to control it; a virulent lineage, Ug99, detected in Uganda in 1998 and named in 1999, overcame resistance genes used in most of the world's wheat. Smuts, such as *Ustilago maydis* on maize, replace the grain with masses of black spores; *U. maydis* is a model for the genetics of fungal pathogenesis and of mating, and its galls are eaten in Mexico as huitlacoche. *Cryptococcus neoformans* and *C. gattii* are basidiomycete yeasts with a thick polysaccharide capsule, from soil and bird droppings, that cause meningitis in people with AIDS (Section 21.8).

## 21.6. Fungi in Ecology

### 21.6.1. Decomposers

Fungi decompose most of the plant material on land, because they can penetrate solid substrates with hyphae and translocate nitrogen and phosphorus from elsewhere to the cellulose- and lignin-rich, nutrient-poor materials they digest. Lignin, an irregular aromatic polymer that encases the cellulose of wood, cannot be broken down by hydrolysis; it is oxidized by radicals produced by extracellular peroxidases (lignin, manganese and versatile peroxidases) and laccases, and the process yields the fungus little energy but gives access to the cellulose. Two types of wood decay are distinguished by what is left behind.

| | White rot | Brown rot |
|---|---|---|
| Agents | many Agaricomycetes (e.g., *Phanerochaete*, *Trametes*) | some Agaricomycetes (e.g., *Fomitopsis*, the dry rot fungus *Serpula lacrymans*) |
| Lignin | degraded by peroxidases and laccases | modified but largely left |
| Cellulose | degraded | degraded, partly by Fenton chemistry (hydroxyl radicals from $\ce{H2O2}$ and $\ce{Fe^2+}$) |
| Residue | pale, fibrous | brown, crumbling into cubes |

The ligninolytic peroxidases of white-rot fungi evolved, according to molecular clock estimates, around the end of the Carboniferous, and it has been proposed that their origin slowed the burial of wood as coal; other studies attribute the abundance of Carboniferous coal mainly to geology and climate, and the question is open. White-rot fungi and their enzymes are studied for the bleaching of pulp and the degradation of aromatic pollutants ([7.11.30](/7.11.30)).

### 21.6.2. Mycorrhizae, Lichens and Other Symbioses

**Definition 21.6.1 (Mycorrhiza)** A **mycorrhiza** is a symbiotic association between a fungus and the roots of a plant, in which the fungal mycelium in the soil supplies the plant with phosphate, nitrogen and water and receives sugars and lipids from it. In an **arbuscular mycorrhiza** the fungus (Glomeromycotina) grows inside the cells of the root cortex and forms finely branched exchange structures, arbuscules; in an *ectomycorrhiza* the fungus (mostly basidiomycetes and ascomycetes) forms a sheath around short roots and a network between the cortical cells without entering them.

About 70–80% of land plant species form arbuscular mycorrhizae, an association that is more than 400 million years old and probably helped plants to colonize land; ectomycorrhizae, formed by forest trees such as pines, oaks and beeches, evolved repeatedly in many lineages of fungi. The fungus of an arbuscular mycorrhiza depends on its host for fatty acids, which it cannot synthesize itself, as well as sugars. Mycorrhizal networks link plants of the same and different species, though how much carbon they transfer between plants in the field is debated.

**Definition 21.6.2 (Lichen)** A **lichen** is a stable symbiotic association of a fungus (the mycobiont, usually an ascomycete) with a population of green algae or cyanobacteria (the photobiont), forming a body, the thallus, whose form is distinct from that of either partner grown alone.

Lichens grow on rock, bark and soil where neither partner could live alone, tolerate desiccation and extreme temperatures, and are among the first colonists of bare rock; they are sensitive to sulfur dioxide and are used to monitor air pollution. Many lichen thalli contain further fungi, basidiomycete yeasts in the cortex. Fungi also live inside the leaves and stems of almost all plants as endophytes, some of which protect their hosts against herbivores with alkaloids; they are cultivated as food by leaf-cutter ants, termites and ambrosia beetles; and they live in the guts of herbivores. These symbioses are the subject of [7.11.31](/7.11.31).

### 21.6.3. Pathogens of Plants and Insects

Fungi cause most of the infectious diseases of plants. The rice blast fungus *Magnaporthe oryzae* (also named *Pyricularia oryzae*) destroys enough rice each year to feed tens of millions of people, and a lineage that jumped to wheat in Brazil in 1985 spread to Bangladesh in 2016; the rusts, smuts and powdery mildews are obligate biotrophs; *Fusarium* species cause wilts and head blights, among them the Tropical Race 4 of *F. oxysporum* f. sp. *cubense* that threatens the Cavendish banana; *Botrytis cinerea* rots fruit; and introduced fungi destroyed the American chestnut (*Cryphonectria parasitica*) and most of the elms of Europe and North America (*Ophiostoma*, Dutch elm disease). Plant pathogens are biotrophic, feeding on living cells through haustoria, or necrotrophic, killing tissues with toxins and enzymes, or hemibiotrophic, switching from the first to the second; they deliver effector proteins that suppress plant immunity, and plants recognize them with resistance proteins ([7.12](/7.12)).

Entomopathogenic fungi infect insects through the cuticle, with appressoria and chitinases, rather than through the gut. *Beauveria bassiana*, the agent of the white muscardine disease of silkworms in which Agostino Bassi showed in 1835 that a microorganism causes an infectious disease, and *Metarhizium* are used as biological insecticides. *Ophiocordyceps unilateralis* makes infected carpenter ants climb vegetation and bite into a leaf vein before they die, so that the fruiting body that grows from the ant's head sheds spores on the trails below.

## 21.7. Fungal Metabolites and Mycotoxins

Filamentous fungi, especially ascomycetes, produce a great variety of **secondary metabolites**, encoded by clusters of genes for polyketide synthases, nonribosomal peptide synthetases and terpene synthases, which are often silent in the laboratory and are activated by stress, competition or epigenetic manipulation.

| Product | Fungus | Use or effect |
|---|---|---|
| Penicillins | *Penicillium chrysogenum* (*P. rubens*) | β-lactam antibiotics ([7.11.14](/7.11.14#sec-14.4.1)) |
| Cephalosporins | *Acremonium chrysogenum* | β-lactam antibiotics |
| Griseofulvin | *Penicillium griseofulvum* | antifungal for dermatophyte infections |
| Lovastatin, compactin | *Aspergillus terreus*, *Penicillium citrinum* | inhibitors of HMG-CoA reductase, the first **statins** ([7.1.26](/7.1.26)) |
| Cyclosporin A | *Tolypocladium inflatum* | immunosuppressant (calcineurin inhibitor) for transplantation |
| Ergot alkaloids | *Claviceps purpurea* | ergotism; drugs for migraine and hemorrhage; precursor of LSD |
| Citric acid | *Aspergillus niger* | food acidulant (bulk chemical) |
| Gibberellins | *Fusarium fujikuroi* | plant hormones, discovered from the "foolish seedling" disease of rice |
| Aflatoxins | *Aspergillus flavus*, *A. parasiticus* | liver toxins and carcinogens in stored crops |
| Fumonisins, trichothecenes | *Fusarium* spp. | contaminants of maize and wheat |
| Ochratoxin A | *Aspergillus*, *Penicillium* spp. | kidney toxin in cereals, coffee and wine |

**Definition 21.7.1 (Mycotoxin)** A **mycotoxin** is a secondary metabolite of a fungus that is toxic to animals or humans when eaten, inhaled or absorbed, usually as a contaminant of crops or stored food.

Aflatoxin B1 is the most potent natural liver carcinogen known. It is activated in the liver by cytochrome P450 to an epoxide that alkylates guanine in DNA and characteristically causes a G to T transversion at codon 249 of the tumor suppressor gene *TP53*; together with chronic hepatitis B, dietary aflatoxin from groundnuts and maize stored in warm, humid conditions is a major cause of liver cancer in parts of Africa and Asia, and acute aflatoxicosis has killed people in famines. Ergotism, caused by eating rye contaminated with the sclerotia of *Claviceps purpurea*, caused epidemics in medieval Europe, with gangrene of the limbs (from the vasoconstricting alkaloids) or convulsions and hallucinations. Mushroom poisoning is a separate matter: the toxins of *Amanita* and other mushrooms are eaten deliberately in the fruiting body, not as contaminants.

## 21.8. Fungal Diseases of Humans

**Definition 21.8.1 (Mycosis)** A **mycosis** is an infection of an animal by a fungus. Mycoses are classified by depth as superficial or cutaneous (skin, hair, nails), subcutaneous (entering through wounds) and systemic (in internal organs, usually from the lungs); a systemic mycosis is *primary* when it occurs in healthy people and *opportunistic* when it requires an impaired defense.

Fungi cause disease in three ways: by allergy (the spores of *Aspergillus*, *Alternaria* and other molds are major triggers of asthma), by toxins (Section 21.7) and by infection. Few fungi grow at 37 °C, and fewer can withstand the defenses of healthy people, so serious mycoses are concentrated in people with neutropenia, transplants, HIV infection, cancer chemotherapy or long stays in intensive care. They are nonetheless estimated to kill more than a million people a year, a burden that is often overlooked.

| Class | Disease | Agent | Route and features |
|---|---|---|---|
| Superficial | tinea pedis (athlete's foot), tinea corporis (ringworm), onychomycosis | dermatophytes: *Trichophyton*, *Microsporum*, *Epidermophyton* | contact; digest keratin |
| Superficial | pityriasis versicolor; dandruff | *Malassezia* (basidiomycete yeast) | skin microbiota, lipid-dependent |
| Subcutaneous | sporotrichosis | *Sporothrix schenckii*, *S. brasiliensis* | thorns and soil; cats in Brazil |
| Subcutaneous | chromoblastomycosis, mycetoma | pigmented molds | traumatic implantation in the tropics |
| Systemic, endemic | histoplasmosis, blastomycosis, coccidioidomycosis, paracoccidioidomycosis, talaromycosis | thermally dimorphic fungi (Section 21.3.4) | inhaled spores; each has its own geographic range |
| Opportunistic | candidiasis (thrush, vaginitis, candidemia) | *Candida albicans*, *C. glabrata* (*Nakaseomyces glabratus*), *Candidozyma auris* (*Candida auris*) | endogenous microbiota; catheters |
| Opportunistic | invasive aspergillosis | *Aspergillus fumigatus* | inhaled conidia; neutropenia, transplants |
| Opportunistic | cryptococcal meningitis | *Cryptococcus neoformans*, *C. gattii* | inhaled; capsule; leading fungal killer in advanced HIV infection |
| Opportunistic | *Pneumocystis* pneumonia | *Pneumocystis jirovecii* | person to person; defining illness of AIDS |
| Opportunistic | mucormycosis | *Rhizopus*, *Mucor* and relatives | diabetic ketoacidosis, corticosteroids; invades blood vessels |

*Candida albicans* is a commensal of the gut, mouth and vagina of most people; broad-spectrum antibiotics, which remove competing bacteria, and impaired immunity let it overgrow, and catheters let it into the blood. *Aspergillus fumigatus* is a thermotolerant saprotroph of compost whose small conidia reach the alveoli; in a person without neutrophils they germinate and the hyphae invade blood vessels. *Pneumocystis jirovecii*, which cannot be cultured, lacks ergosterol and is therefore insensitive to amphotericin B and the azoles; it is treated and prevented with trimethoprim–sulfamethoxazole. During the COVID-19 pandemic, mucormycosis rose sharply in India among patients with diabetes treated with corticosteroids.

Antifungal therapy relies on four classes — polyenes, azoles, echinocandins and flucytosine — whose targets and limits are discussed in [7.11.14](/7.11.14#sec-14.10.1). Resistance is increasing. *Candida auris*, first described in 2009 from an ear infection in Japan, emerged at about the same time in several continents as distinct clades, spreads between patients in hospitals, persists on surfaces and is often resistant to azoles and sometimes to all classes. Azole-resistant *A. fumigatus*, with mutations in the promoter and coding sequence of *cyp51A* (the target of azoles), such as TR34/L98H, arises in the environment, where azole fungicides are sprayed on crops, and is then inhaled by patients who have never received azoles: an example of resistance selected by agriculture, as in [7.11.15](/7.11.15). In 2022 the World Health Organization published its first list of fungal priority pathogens, with *Cryptococcus neoformans*, *Candida auris*, *Aspergillus fumigatus* and *Candida albicans* in the critical group.

## Summary

- A fungus (Definition 21.1.1) is an absorptive opisthokont with walls of chitin and β-glucans and membranes with ergosterol; fungi are the sister group of animals, and most have lost the flagellum.
- Hyphae and mycelia (Definition 21.2.1) grow at the tip, where the Spitzenkörper delivers secretory vesicles; septa with pores and Woronin bodies or dolipores divide the hyphae of the Dikarya, while those of the Mucoromycota are coenocytic. Branching keeps the length per tip near the hyphal growth unit, so that a mycelium grows exponentially at rate $v/G$ (Formula 21.2.1) while a colony expands linearly. Hyphae differentiate into rhizoids, stolons, haustoria, appressoria, sclerotia, rhizomorphs and traps; molds (Definition 21.2.2) and yeasts form characteristic colonies.
- Yeasts (Definition 21.3.1) bud or divide by fission; their life cycles differ in the vegetative ploidy (see the yeast life-cycle figure in Section 21.3.2); *S. cerevisiae* switches mating type by gene conversion from silent cassettes and is a premier model and industrial organism. Dimorphic pathogens (Definition 21.3.2) switch between mold and yeast or spherule forms with temperature, *Candida albicans* between yeast and hyphae.
- Asexual spores include sporangiospores and conidia (Definition 21.4.1), arthroconidia, blastoconidia and chlamydospores; sexual spores — zygospores, ascospores and basidiospores (Definition 21.4.3) — define the main groups. In the Dikarya plasmogamy and karyogamy are separated by a dikaryon (Definition 21.4.2); the parasexual cycle gives recombination without meiosis.
- Phylogeny (see the figure of fungal lineages in Section 21.5.1): Opisthosporidia (Cryptomycota, Microsporidia, Definition 21.5.2), chytrids (Definition 21.5.1) with flagellated zoospores, Blastocladiomycota, Zoopagomycota, Mucoromycota (including the arbuscular mycorrhizal fungi), and the Dikarya: Ascomycota (Definition 21.5.3; yeasts, molds, ascocarps) and Basidiomycota (Definition 21.5.4; mushrooms with clamp connections, rusts, smuts, *Cryptococcus*).
- Fungi decompose lignocellulose (white and brown rot), form mycorrhizae (Definition 21.6.1) and lichens (Definition 21.6.2), and are the chief pathogens of plants (rice blast, rusts, *Fusarium*) and important pathogens of insects and amphibians (chytridiomycosis).
- Fungal secondary metabolites include antibiotics, statins, cyclosporin and mycotoxins (Definition 21.7.1) such as aflatoxins and ergot alkaloids.
- Mycoses (Definition 21.8.1) are superficial, subcutaneous or systemic; serious ones are mostly opportunistic (*Candida*, *Aspergillus*, *Cryptococcus*, *Pneumocystis*, Mucorales), and resistance (*Candida auris*, azole-resistant *A. fumigatus*) is a growing problem.

## Questions

1. Oomycetes and fungi both grow as absorptive hyphae. List four characters that show that they are not related, and explain why the distinction matters for the control of potato late blight.

   **Answer** Oomycete walls contain cellulose and β-glucans rather than chitin; their hyphae are diploid, whereas fungal hyphae are haploid or dikaryotic; their zoospores have two flagella of the stramenopile type, one with tubular hairs, while fungal zoospores have a single posterior flagellum; and they make lysine by the diaminopimelate pathway rather than the α-aminoadipate pathway (they also lack ergosterol synthesis). Phylogenetically they are stramenopiles. Because many fungicides target fungus-specific processes such as ergosterol synthesis, they are ineffective against *Phytophthora*, which needs different compounds (such as phenylamides or copper).

2. A mycelium in a fresh medium has a hyphal growth unit of 200 µm and tips that extend at 2 µm min⁻¹. What is its specific growth rate and doubling time, and why does a colony of the same fungus on a plate widen by a constant amount per hour?

   **Answer** By Formula 21.2.1, $\mu = v/G = 2/200 = 0.01\,\mathrm{min^{-1}}$, so the doubling time is $\ln 2/\mu \approx 69$ min. On a plate, the tips at the margin advance at 2 µm min⁻¹, about 0.12 mm h⁻¹, into fresh medium; branches inside the colony grow into space that is already occupied and soon exhausted, so the radius, which is set by the leading tips, increases linearly while the total biomass of the young colony increases faster.

3. Haploid cells of a wild homothallic strain of *S. cerevisiae* are placed singly in wells. After a few divisions, diploids appear in each well. Explain, and say why geneticists use *ho* mutants.

   **Answer** After its first division, a mother cell expresses the HO endonuclease, which cuts the *MAT* locus; the break is repaired by gene conversion from the silent cassette of the opposite mating type (*HML*α or *HMRa*), so the mother switches mating type while its daughter keeps the old one. The two cells now have opposite mating types, secrete pheromones that arrest each other, fuse and form a diploid. Without HO, haploid strains keep a stable mating type, so haploid lines with defined genotypes can be maintained, mated deliberately and their diploids sporulated for tetrad analysis.

4. Why are most serious fungal infections opportunistic, and why are antifungal drugs fewer and more toxic than antibacterial drugs?

   **Answer** Few fungi grow at body temperature, and those that do are usually controlled by neutrophils, macrophages and T-cell responses; serious infection therefore requires neutropenia, impaired cell-mediated immunity (HIV, transplants, corticosteroids), breaches of barriers (catheters, surgery) or the removal of competing bacteria by antibiotics. Fungi are eukaryotes, so their ribosomes, polymerases and most enzymes resemble human ones; selective targets are limited to the cell wall (β-glucans), ergosterol and its synthesis and a few enzymes such as fungal cytosine deaminase. Drugs aimed at ergosterol also bind cholesterol or human P450 enzymes to some extent, which accounts for the nephrotoxicity of amphotericin B and the drug interactions of azoles.

5. Azole-resistant *Aspergillus fumigatus* is isolated from patients who have never taken azoles. How can this be, and what does it imply for the control of resistance?

   **Answer** *A. fumigatus* lives in compost and soil, where azole fungicides used in agriculture and horticulture select for mutations such as TR34/L98H in *cyp51A* (a promoter duplication that raises expression and a substitution that lowers binding). Resistant conidia are produced in enormous numbers and inhaled by everyone; a susceptible patient can therefore be infected with a strain that is already resistant. Control of resistance must include the use of azoles outside medicine, a "One Health" problem, in addition to the stewardship of antifungal drugs in hospitals.
