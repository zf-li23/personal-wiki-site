---
title: "Course Summary: The Threads of Microbiology"
description: "A synthesis of the microbiology course: eight threads (the small cell, metabolism, growth and its control, regulation and the fluid genome, diversity and the tree of life, viruses, ecology, microbes and humans) that run through its chapters, a table of the quantitative models, the time scales of microbial life, how methods changed the field, open problems and the connections to other courses."
---

Microbiology is defined by a size and a set of methods rather than by a branch of the tree of life ([7.11.1](/7.11.1)): it studies Bacteria, Archaea, microbial eukaryotes and viruses, organisms that are too small to be seen individually and that are therefore known through what they do in cultures, in communities and in hosts. The thirty-five chapters before this one have followed the usual order of the subject, from the cell to its metabolism and growth, its regulation and genetics, the diversity of microorganisms, the viruses, their ecology and their relations with people. This chapter adds no new material. It follows eight threads that cross that order and lays the main results of each side by side; the references (Formula 8.3.1, Definition 22.3.1, Eq. (35.1)) lead to the chapters where they are derived. The molecular background — the chemistry of the envelope, bioenergetics, transcription, bacterial genetics, the growth laws and the origin of the prokaryotes — is in the courses listed in §36.12.

## 36.1. The Shape of the Course

The course falls into ten blocks.

| Block | Chapters | Central question | Main tools |
|---|---|---|---|
| Introduction | 7.11.1 | What is a microorganism, and how did we learn about them? | microscopy, pure culture, Koch's postulates, rRNA phylogeny |
| The cell | 7.11.2–7.11.3 | How is a prokaryotic cell built, and how does it move? | staining, electron microscopy, envelope chemistry |
| Nutrition and metabolism | 7.11.4–7.11.7 | What does a cell need, and how does it gain energy and carbon? | media, transport, redox potentials, $\Delta_{\mathrm{r}}G$ |
| Growth and its control | 7.11.8–7.11.10 | How fast do populations grow, what limits them, how are they killed? | exponential growth, the chemostat, survival curves |
| Regulation and genetics | 7.11.11–7.11.13 | How do cells sense, decide, differentiate and exchange genes? | regulons, two-component systems, mobile elements |
| Drugs and resistance | 7.11.14–7.11.15 | How do antimicrobial drugs work, and how do bacteria escape them? | MIC, pharmacodynamics, resistance genetics |
| Diversity | 7.11.16–7.11.21 | How are microorganisms classified, and what lineages are there? | 16S rRNA and genome phylogeny, ANI, polyphasic taxonomy |
| Viruses | 7.11.22–7.11.28 | What is a virus, how does it replicate, interact with hosts and get controlled? | Baltimore classes, plaque and growth curves, reverse genetics |
| Ecology | 7.11.29–7.11.31 | Who lives where, what do they do, and how do they drive the cycles of elements? | FISH, metagenomics, isotopes, microsensors |
| Microbes and humans | 7.11.32–7.11.35 | How do microbes live with us, make us ill, and spread? | germ-free animals, virulence factors, epidemic models |

![The threads of the course. Rows: eight threads; columns: the chapters 7.11.1–7.11.35; large dots mark a chapter of which the thread is a main subject, small dots a chapter that uses or extends it. Bands at the top mark the blocks. Each thread is concentrated in one block and recurs in later ones: metabolism returns in the diversity and ecology chapters, regulation and genetics in the chapters on resistance, phages and pathogenesis.](./plots/threads.py)

## 36.2. The Small Cell

The first thread is size. Microorganisms span more than five orders of magnitude in length, from viruses of $20\,\mathrm{nm}$ to bacterial cells a centimeter long (§1.9.1), but most prokaryotic cells are about a micrometer across. At that size the ratio of surface to volume is large ($S/V = 3/r$ for a sphere, Formula 1.9.1), diffusion distances inside the cell are short, and uptake through the surface can support a high specific metabolic rate; this is the root of the short doubling times, the large population sizes and the large supply of mutations that characterize microbial life (§1.2.4). The giant bacteria confirm the rule by evading it: they fill their volume with a vacuole or distribute their genome copies to the periphery (§1.9.2).

A small cell without internal compartments places most of its functions in its envelope.

- The cytoplasmic membrane is the permeability barrier, the site of energy conservation by the **proton-motive force** and the anchor of transporters and sensors. Bacterial and archaeal membranes solve the same problem with opposite chemistry, ester-linked fatty acids on glycerol 3-phosphate against ether-linked isoprenoids on glycerol 1-phosphate (§2.2).
- The **peptidoglycan** sacculus sets shape and resists turgor; its thickness and the presence of an **outer membrane** underlie the Gram stain (Definition 2.5.1), the different permeability of Gram-positive and Gram-negative bacteria to drugs (§14.2.4) and the endotoxin of the latter (§33.9). Its synthesis in three compartments (§8.2) is the most exploited antibiotic target (§14.4).
- Surface structures attach cells and move them: capsules, fimbriae and pili, flagella driven by an ion-powered rotary motor, archaella (§3.1, §3.4). Chemotaxis turns a random walk into directed movement by modulating the length of runs (§3.5.1), with an adaptive signaling network (§11.6.2).
- **Endospores** (Definition 3.3.1) are the extreme of dormancy, and their resistance sets the standards of sterilization (§10.2).

Microbial eukaryotes have the compartments that prokaryotes lack, but in anaerobic lineages the mitochondrion is reduced to a hydrogenosome or mitosome (§3.6, §20.1.2). Viruses are not cells at all: the virion is a genome in a self-assembling protein shell (§22.4), and the cell it infects supplies everything else.

## 36.3. Metabolism: Using Every Redox Gradient

The second thread is the diversity of energy metabolism, which is the reason microorganisms run the chemistry of the planet. Every way of conserving energy is a transfer of electrons from a donor to an acceptor, and its yield follows from the difference of their reduction potentials, $\Delta_{\mathrm{r}}G^{\circ\prime} = -zF\Delta E^{\circ\prime}$ (Formula 5.1.2). Microorganisms use practically every pair on the redox tower (Definition 5.1.1) whose difference exceeds the minimum of about $-20\,\mathrm{kJ}$ per reaction that a cell can conserve (§7.1.1).

| Strategy | Electron donor | Electron acceptor | Chapters |
|---|---|---|---|
| Fermentation | organic | an internal organic product | §5.3 |
| Aerobic and anaerobic respiration | organic | $\ce{O2}$, nitrate, Fe(III), Mn(IV), sulfate, $\ce{CO2}$, organic and halogenated compounds | §5.4, §7.3 |
| Chemolithotrophy | $\ce{H2}$, $\ce{H2S}$ and $\ce{S^0}$, $\ce{Fe^2+}$, $\ce{NH3}$, $\ce{NO2-}$ | usually $\ce{O2}$ or nitrate | §7.2 |
| Methanogenesis and acetogenesis | $\ce{H2}$, formate, acetate, methyl compounds | $\ce{CO2}$ or a methyl group | §7.4 |
| Phototrophy | light-driven: water (oxygenic), sulfide, $\ce{H2}$, $\ce{Fe^2+}$ or organic donors (anoxygenic) | — | §6.1–§6.4 |

Three consequences recur in the rest of the course. First, the same few machines — the proton-motive force, ATP synthase, quinone pools, ferredoxin and electron bifurcation — are combined in modular, branched chains (§5.4.1), so that one organism can switch acceptors as conditions change. Second, carbon and energy are separate choices (Definition 4.2.1–Definition 4.2.3): six pathways of autotrophic $\ce{CO2}$ fixation differ in their ATP cost and oxygen tolerance (§6.5.6), and **nitrogen fixation** is confined to prokaryotes (§6.6). Third, reactions that are endergonic for one organism become possible in partnership: in **syntrophy** (§7.5) a hydrogen consumer keeps $\ce{H2}$ low enough for a fermenter to gain energy, which links the anaerobic food chain to **methanogenesis**. The Winogradsky column (Definition 7.6.1) shows the whole sequence of metabolisms ordered along one redox gradient, and the global cycles of §36.8 are the same sequence on the scale of the planet.

## 36.4. Growth and Its Control

The third thread is quantitative. A bacterial population grows exponentially, $N = N_0 2^n$ with growth rate constant $k = \ln 2/g$ (Formula 8.3.1); a batch culture runs through lag, exponential, stationary and death phases (§8.4.1); a **chemostat** (Definition 8.5.1) fixes the growth rate through the dilution rate, and of competitors limited by the same nutrient the one with the lowest break-even concentration $R^*$ wins (Formula 4.5.1, Formula 8.5.1). The environment sets the range in which growth is possible — temperature from $-15$ to $122\,^\circ\mathrm{C}$, pH, water activity, oxygen and pressure (§9.1–§9.5) — and each class of extremophile has its molecular adaptations.

Killing is the same mathematics run backwards. Heat, radiation and disinfectants kill exponentially, with a **decimal reduction time** $D$ (Formula 10.2.1) and the Chick–Watson law for chemical agents (Formula 10.4.1); sterility is therefore a probability, not a state (§10.2.2). Antimicrobial drugs are assessed by the MIC and by pharmacodynamic functions that relate net growth rate to concentration (Formula 14.3.2), and the biphasic killing of a population that contains **persisters** (Formula 15.5.1) explains why a culture can survive a drug to which every survivor is still susceptible.

| Model | Result | Where |
|---|---|---|
| Surface-to-volume ratio | $S/V = 3/r$ (sphere), Eq. (1.1) for a rod | Formula 1.9.1 |
| Competition in a chemostat | the lowest $R^* = K_{\mathrm{s}}D/(\mu_{\max} - D)$ wins | Formula 4.5.1 |
| Exponential growth | $N = N_0 2^n$, $g = t/n$, $k = \ln 2/g$ | Formula 8.3.1 |
| Heat killing | $N = N_0 10^{-t/D}$; $D$ falls tenfold per $z$ degrees | Formula 10.2.1, Formula 10.2.2 |
| Disinfection | $\ln(N/N_0) = -kC^n t$ | Formula 10.4.1 |
| Quorum switch | bistability from cooperative, autoinduced signal production | Formula 11.7.1 |
| Bet hedging | long-run growth is the mean of the logarithm of growth factors | Formula 12.4.1 |
| Diffusion into a biofilm | full penetration needs a Thiele modulus $\varphi \le 1$ | Formula 12.9.1 |
| Plasmid persistence | a costly plasmid persists if transfer outweighs loss and cost | Formula 13.2.1 |
| Disk diffusion | the squared zone diameter falls linearly with $\ln \mathrm{MIC}$ | Formula 14.3.1 |
| Persistence | biphasic killing curve | Formula 15.5.1 |
| Multiplicity of infection | fraction of cells infected $1 - \mathrm{e}^{-m}$ | Definition 22.6.3 |
| One-step growth of a phage | eclipse, latent period and burst size from one model | Eq. (23.1) |
| Phage and host in a chemostat | damped oscillations, coexistence with resistant mutants | Eq. (23.2) |
| Error threshold | the mutation rate per genome limits genome length | Definition 25.2.1 |
| Within-host dynamics | $R_0 = \beta pT_0/(\delta c)$ | Formula 27.6.1 |
| Herd immunity | immune fraction above $1 - 1/R_0$ | Eq. (28.2) |
| Infection by independent action | $\mathbb{P}(\text{infection}) = 1 - \mathrm{e}^{-rd}$, $\mathrm{ID}_{50} = \ln 2/r$ | Eq. (33.1) |
| Final size of an epidemic | $1 - r_\infty = \mathrm{e}^{-R_0 r_\infty}$ | Eq. (35.1) |
| Predictive value of a test | depends on the pre-test probability | Eq. (35.2) |

Two mathematical motifs dominate the table. Exponential processes with constant rates — growth, killing, the decay of susceptibles — are read on logarithmic axes; and Poisson statistics, from colony counts (Definition 8.6.1) and the most probable number to the multiplicity of infection and the dose–response of infection, convert the discreteness of cells and particles into probabilities. The theory of balanced growth and the bacterial growth laws behind these phenomenological models are in [7.6.39](/7.6.39).

## 36.5. Regulation, Development and the Fluid Genome

The fourth thread is how microorganisms adapt: mostly by changing what they express, not what they look like. Regulation acts where its cost is lowest for the speed required, transcription for economy, RNA for speed, protein modification for the fastest responses (Remark 11.1.1). Over these sit global networks that reallocate the whole proteome: catabolite repression and **diauxic growth** (Definition 11.3.2), alternative σ factors (§11.4), two-component systems (§11.6.1), the **stringent response** (Definition 11.8.1) and **quorum sensing** (Definition 11.7.1), which lets a population act only when it is numerous. Differentiation in prokaryotes is built from the same parts (§12.1): sporulation by a cascade of compartment-specific σ factors (§12.3), the asymmetric cell cycle of *Caulobacter crescentus* (§12.5), heterocysts spaced by an activator and a diffusible inhibitor (§12.8), and the **biofilm** (Definition 12.9.1), the usual way bacteria live in nature. Phenotypic heterogeneity in one genotype — competence, persistence, partial germination — is adaptive when the environment fluctuates (§12.4).

The second half of the thread is the fluidity of the genome. A prokaryotic genome consists of a core shared by a species and an accessory part of islands, plasmids, transposons, integrons, prophages and integrative conjugative elements (§13.1.4, §13.3); together these make an open **pangenome**. **Horizontal gene transfer** by transformation, transduction and conjugation (§13.5–§13.7) moves genes between lineages, within limits set by ecology, restriction, CRISPR and the requirement for homology (§13.9). The consequences run through the later chapters:

- antimicrobial resistance spreads as genes on mobile elements as well as by clonal expansion (§15.6.2);
- virulence is often acquired in one step, as a **pathogenicity island**, a plasmid or a toxin-carrying prophage (§33.10, §34.7.1; **lysogenic conversion**, Definition 23.3.2);
- the defense systems against phages cluster in islands and move between genomes, so that immunity is a property of the pangenome (§23.8.6);
- physiological groups such as nitrogen fixers and sulfate reducers are polyphyletic, because their key genes move (§17.1.1), and the history of prokaryotes is not a simple tree ([7.10.27](/7.10.27#sec-27.6)).

Mutation remains the ultimate source of variation and is random with respect to its use (§13.4.4), but in microorganisms recombination with foreign DNA is so frequent that species are held together, if at all, by periodic selection within ecotypes or by recombination among relatives (§16.4.5).

## 36.6. Diversity and the Tree of Life

The fifth thread is the one that makes microbiology a starting point for the study of biological diversity. Classification by phenotype gave way to phylogeny when the **16S rRNA gene** (Definition 16.3.1) showed that prokaryotes form two domains and that the eukaryotes are related to the Archaea (§1.7); genome phylogenies and the Genome Taxonomy Database (Definition 16.6.1) now place every sequenced genome on one tree. On that tree almost every branch is microbial.

![The tree of life in outline (cladogram; branch lengths have no meaning). The root is placed between Bacteria and Archaea, and the eukaryotes branch from within the Archaea as the sister group of the **Asgard archaea** (§19.8), so that in this two-domain view the Archaea in the wide sense include the eukaryotes. The bacterial lineages are those of 7.11.17–7.11.18, the archaeal ones those of 7.11.19, the eukaryotic supergroups those of 7.11.20–7.11.21. Stars mark the lineages that contain macroscopic multicellular organisms (animals, fungi with fruiting bodies, brown algae, red algae and land plants); all other lineages, and most members of the starred ones, are microbial.](./plots/tree-of-life.py)

| Domain | What unites it | Chapters | Highlights |
|---|---|---|---|
| Bacteria | ester lipids, peptidoglycan walls, bacterial transcription machinery | 7.11.17–7.11.18 | Pseudomonadota (formerly Proteobacteria) with a third of the described species; Gram-positive Bacillota and Actinomycetota; the cyanobacteria, the only oxygenic phototrophic bacteria; the **candidate phyla radiation** (Definition 16.3.2), known mainly from genomes |
| Archaea | ether lipids on glycerol 1-phosphate, no peptidoglycan, eukaryote-like information processing | 7.11.19 | halophiles, methanogens, hyperthermophiles up to $122\,^\circ\mathrm{C}$, ammonia oxidizers of the ocean and soil; DPANN symbionts; Asgard archaea as the closest relatives of eukaryotes; no known pathogens |
| Eukaryotes | nucleus, endomembranes, mitochondria or their remnants | 7.11.20–7.11.21 | protists in every supergroup (Definition 20.1.1), plastids spread by secondary endosymbiosis; fungi as absorptive relatives of animals (Definition 21.1.1) |

Several conclusions of this block cut across the classification. Function and phylogeny are separate axes: photosynthesis, nitrogen fixation, methanotrophy and parasitism are scattered over the tree. Morphological categories — "protist", "alga", "Gram-positive" — are grades rather than clades, and the Gram reaction only roughly follows phylogeny (§2.5.4). The species is an operational category defined by thresholds of genome similarity (§16.4.4), and most organisms known from sequences have no cultured representative; the SeqCode now allows them to be named from genomes (§16.7.2). The origin of the eukaryotic cell and the endosymbiotic origin of organelles are treated in [7.10.28](/7.10.28), and the deeper history of the tree in [7.10.2](/7.10.2) and [7.10.27](/7.10.27).

## 36.7. Viruses

The sixth thread treats viruses as a separate kind of biological entity. A virus alternates between an inert **virion** and an intracellular state that is a replicating genome (§22.1.1); it has no metabolism, and its small genome forces symmetry, economy of coding and dependence on the host (§22.4.1, §24.1). Every virus must make mRNA, and the route it takes defines its class in the **Baltimore classification** (Definition 22.3.1), which in turn decides what enzymes the virion must carry: an RNA-dependent RNA polymerase for negative-strand and double-stranded RNA genomes, reverse transcriptase for retroviruses (§25.1, §25.6).

The chapters followed a virus through four levels.

- *The particle and its cycle*: attachment, entry, replication, assembly and release; plaque assays, the TCID50 and the one-step growth curve (§22.5, §22.6), worked out first for phages (§23.4, §23.5).
- *The genome*: DNA viruses solve priming and the end problem in several ways and push the cell into S phase (§24.3, §24.4); RNA viruses replicate without proofreading, form a **quasispecies** (Definition 25.2.1) and are limited in genome length by the **error threshold** (§25.2).
- *The host*: restriction factors, pattern recognition and interferon (§27.3, §27.4), adaptive immunity as a selective force producing antigenic drift and shift (§27.5); in bacteria, the layered defenses from restriction–modification to CRISPR–Cas and abortive infection (§23.8).
- *The population and the biosphere*: phages are the most abundant biological entities, kill a large fraction of marine bacteria every day and drive the **viral shunt** (Definition 26.6.1); viruses have probably arisen several times (§26.5); prions and viroids extend the notion of an infectious agent below the virus (§26.9, §26.10).

Antiviral drugs and vaccines (7.11.28) are the practical side of this thread. Selective targets are few, resistance is certain in large populations with error-prone polymerases, and combination therapy works because multiple specific mutations rarely coexist in one genome (§28.4); vaccination protects the unvaccinated once the immune fraction exceeds $1 - 1/R_0$ (Eq. (28.2)).

## 36.8. Microbes in Ecosystems

The seventh thread puts the metabolisms of §36.3 back into their environments. Microbial ecology asks who is present, what they do and how fast (Definition 29.1.1), and each question has its methods (§29.4–§29.6): cell counts and FISH, metagenomes and single-cell genomes, rates measured with microsensors and isotopes, and the identification of active cells by stable isotope probing and NanoSIMS. The **great plate count anomaly** (Definition 8.6.2) — that only a small fraction of cells in most samples forms colonies — is the reason these culture-independent methods dominate the field.

Microbial habitats are structured at the scale of the cell: gradients of oxygen and sulfide over millimeters separate aerobes from anaerobes in mats, sediments, soil aggregates and biofilms (§29.2). On the global scale the processes link into **biogeochemical cycles** (Definition 30.1.1): fixation and decomposition of carbon with methane as a microbial product and sink, the nitrogen cycle with its fixation, nitrification, denitrification and anammox, the sulfur, iron and phosphorus cycles (§30.2–§30.6). The same processes are engineered in wastewater treatment, where the solids retention time decides which slow-growing guilds remain (Formula 30.9.1), in bioremediation and in bioleaching (§30.9–§30.12), and they respond to and amplify global change (§30.8).

Symbiosis (Definition 31.1.1) is the closest of these relations: legumes and rhizobia exchange carbon for fixed nitrogen in a controlled organ (§31.2), mycorrhizal fungi supply most land plants with phosphate (§31.3.1), insects and marine invertebrates depend on endosymbionts for nutrients or energy (§31.4, §31.5), and ruminants live on the products of microbial fermentation (§31.6). Vertically transmitted symbionts lose genes by drift until, at the extreme, they become organelles (§31.7).

## 36.9. Microbes and Humans

The last thread is the relation of microorganisms to people, and its first lesson is that commensalism and pathogenicity are ends of a continuum (§34.7.3). The human body carries about as many bacterial cells as human cells, almost all in the colon (§32.1.1). The gut **microbiome** ferments fiber to short-chain fatty acids, transforms bile acids and drugs, trains the immune system and protects against pathogens by **colonization resistance** (Definition 32.4.1). Most claims about its role in disease rest on association or animal experiments; the clearest causal case is *Clostridioides difficile* infection after antibiotics, which is cured by restoring the community (§32.5.2), and the chapter labels every claim by its level of evidence (§32.1.3).

Pathogenicity is the ability to cause disease and **virulence** its degree (Definition 33.1.1); both depend on the host as well as on the microbe. The steps of an infection — entry, adhesion, invasion, damage and transmission — each have their bacterial tools: adhesins, invasins, siderophores, toxins (§33.4–§33.8), and the means to survive phagocytes, complement and antibodies, to live inside host cells and to inject effectors with secretion systems (§34.2–§34.6). In populations, the reproduction number governs growth and decline of an epidemic (§35.3), the route of transmission dictates the control measure (§35.2), and diagnosis depends on the quality of the specimen and on the pre-test probability as much as on the test (§35.6).

The control of microorganisms is the other side of this relation. Sterilization and disinfection (7.11.10), antimicrobial drugs (7.11.14), vaccines and antivirals (7.11.28) have reduced infectious disease more than any other medical intervention, and each meets an evolutionary response: antimicrobial resistance caused an estimated 1.27 million deaths directly in 2019 (§15.1.1), and resistance genes are ancient, mobile and co-selected (§15.6). Microorganisms are also producers of foods, chemicals, drugs and enzymes, but the industrial and applied uses of these capacities are beyond the scope of this course.

## 36.10. Time Scales

The threads also differ in their time scales. A swimming cell changes direction about once a second, regulation reshapes expression within minutes, populations double in minutes to weeks, resistance to a new drug appears within years, and the divergence of species is measured in tens of millions of years. Because so many generations fit into a human lifetime, microbial evolution can be watched in the laboratory (§16.2.1), and because microbes were the only life for most of Earth's history (§1.2.3), their metabolism shaped the atmosphere in which all later life evolved.

![Microbial processes on one logarithmic time axis, with values from the chapters: a run of a swimming *Escherichia coli* cell (about 1 s, §3.5.1); a transcriptional response (minutes) and a complete change of expression program (about an hour, §11.1); the doubling of *Vibrio natriegens* (about 10 min), the latent period of phage T4 (about 25 min, §23.5), the generation time of *Mycobacterium tuberculosis* (about 20 h, §18.3.2), the doubling of an Asgard archaeon in co-culture (two to three weeks, §19.8) and generation times in the deep biosphere (years to millennia, §29.7.3); resistance reported within a few years of a new antibiotic (§15.6), citrate use in the long-term evolution experiment after about 31 500 generations (§16.2.1), and the divergence of 16S rRNA genes by about 1 % in 50 million years (§16.2.3); the Great Oxidation Event (about 2.4 Ga) and the oldest stromatolites (about 3.43 Ga, §1.2.3).](./plots/timescales.py)

## 36.11. How Methods Changed the Field

Microbiology advanced by its methods more visibly than most of biology, and each new method changed what counted as knowing a microorganism.

| Period | Method | What it made possible |
|---|---|---|
| 1670s | the simple microscope (Leeuwenhoek) | seeing bacteria and protists (§1.3.1) |
| 1860s–1880s | sterilization, solid media and pure culture (Pasteur, Koch) | the end of spontaneous generation, the germ theory, **Koch's postulates** (§1.3.2, §1.4) |
| 1880s–1900s | **enrichment culture** (Beijerinck, Winogradsky) | chemolithotrophy, nitrogen fixation, the discovery of viruses (§1.5) |
| 1940s–1970s | bacterial and phage genetics, molecular biology | the gene, the operon, recombinant DNA (§1.6.2, §23.1.2) |
| 1977 onward | rRNA sequencing (Woese) | the Archaea and a phylogenetic classification (§1.7, §16.3) |
| 1995 onward | genome sequencing | genome-based taxonomy, pangenomes, reverse genetics of viruses (§13.1, §16.6, §24.2) |
| 2000s onward | metagenomics, single-cell genomics, isotope and single-cell activity methods, cryo-electron microscopy | the uncultured majority, new phyla and superphyla, activities of single cells in situ (§29.5, §29.6) |

The pattern is that culture-dependent and culture-independent methods complement each other rather than one replacing the other. Sequences reveal organisms and their potential, but physiology, genetics and the testing of causal hypotheses still need cultures or gnotobiotic hosts, which is why new cultivation methods (§4.5.4, §29.3.2) remain as important as new sequencing methods.

## 36.12. Open Problems and Connections

The chapters end with questions that are not settled.

- *The uncultured majority.* Most lineages are known only from genomes; what most of them do, and why they resist cultivation, is largely unknown (§29.3.2, §18.1.2).
- *The prokaryotic species.* Whether species are real units held together by recombination or ecotypes kept apart by selection, and how to name organisms without cultures, are still debated (§16.4.5, §16.7.2).
- *Causality in the microbiome.* Except in a few cases, it is unknown whether shifts of the human microbiota cause disease or follow it (§32.5).
- *New antimicrobials.* Few new classes have been found since the 1960s; genome mining, new cultivation methods and phage therapy are the main hopes (§15.7.2).
- *Viruses in the history of life.* The origins of viruses, their role in the origin of cellular functions and in the evolution of immunity are open (§26.5, §23.8.6).
- *The limits of life.* The upper temperature limit and the biosignatures by which life could be recognized elsewhere are unresolved ([7.10.27](/7.10.27#sec-27.8), §19.9).

| Course | What it provides or receives | Pages |
|---|---|---|
| Biochemistry (7.1) | chemistry of peptidoglycan and LPS; bioenergetics, oxidative phosphorylation, photosynthesis, nitrogenase | [7.1.10](/7.1.10), [7.1.23](/7.1.23), [7.1.24](/7.1.24), [7.1.27](/7.1.27) |
| Molecular biology (7.2) | bacterial transcription and its regulation, the *lac* and *trp* operons, CRISPR as a tool | [7.2.10](/7.2.10), [7.2.11](/7.2.11), [7.2.24](/7.2.24) |
| Cell biology (7.3) | prokaryotic and eukaryotic cells, microscopy | [7.3.1](/7.3.1), [7.3.2](/7.3.2) |
| Genetics (7.4) | transformation, conjugation and transduction as genetic tools; the pangenome | [7.4.10](/7.4.10), [7.4.14](/7.4.14) |
| Biophysics (7.6) | physics of chemotaxis, growth laws and resource allocation | [7.6.35](/7.6.35), [7.6.39](/7.6.39) |
| Bioinformatics (7.8) | phylogenetic algorithms; analysis of amplicon and metagenome data | [7.8.6](/7.8.6), [7.8.14](/7.8.14) |
| Systems biology (7.9) | noise, bet hedging and synthetic biology | [7.9.17](/7.9.17) |
| Evolutionary biology (7.10) | the tree of life, the origin of prokaryotes and lateral transfer, the origin of eukaryotes | [7.10.2](/7.10.2), [7.10.27](/7.10.27), [7.10.28](/7.10.28) |
| Immunology (7.15) | receives the strategies of pathogens (7.11.33–7.11.34), the innate response to viruses (7.11.27) and vaccines (7.11.28) | [7.15](/7.15) |

Microbiology is in turn a prerequisite for the later courses: plant biology for the rhizosphere, nodules and plant pathogens, immunology for the pathogens it is directed against, and ecology for the cycles of elements and the microbial communities of every habitat.

## Summary

- The course moved from the microbial cell (7.11.2–7.11.3) through its metabolism, growth and control (7.11.4–7.11.10), regulation and genetics (7.11.11–7.11.15) and diversity (7.11.16–7.11.21) to viruses (7.11.22–7.11.28), ecology (7.11.29–7.11.31) and the relations of microbes with people (7.11.32–7.11.35).
- Small size gives a high surface-to-volume ratio (Formula 1.9.1), fast growth and large populations; the envelope carries most cellular functions and is the main target of drugs.
- Energy metabolism uses almost every redox couple whose yield exceeds the biological minimum ($\Delta_{\mathrm{r}}G^{\circ\prime} = -zF\Delta E^{\circ\prime}$, Formula 5.1.2), which makes microorganisms the engines of the biogeochemical cycles.
- Growth and killing are exponential processes, and Poisson statistics links cells and particles to counts, infections and doses (§36.4).
- Microorganisms adapt mainly by regulation and by horizontal transfer; their genomes are a core plus a mobile accessory part, which spreads resistance, virulence and defense.
- Almost every branch of the tree of life is microbial; the eukaryotes branch from within the Archaea, and function is distributed over the tree independently of phylogeny.
- Viruses are defined by their route to mRNA (Definition 22.3.1), are the most abundant biological entities and are controlled by host restriction, immunity, drugs and vaccines.
- Commensal and pathogen, mutualist and parasite are ends of continua that depend on the host and the environment.

## Questions

1. Explain, with numbers from the course, why the open ocean is dominated by very small cells such as *Prochlorococcus* and *Pelagibacter*, and why this is consistent with the competition rule of the chemostat.

   **Answer** At low nutrient concentrations uptake per unit volume limits growth, and $S/V = 3/r$ (Formula 1.9.1) rises as cells shrink, so small cells take up more per unit of biomass. In competition for a limiting nutrient the species with the lowest break-even concentration $R^*$ wins (Formula 4.5.1); a low $R^*$ requires a high affinity (low $K_{\mathrm{s}}$), which small cells with many high-affinity transporters achieve, so oligotrophic water selects small, high-affinity oligotrophs rather than fast growers (§4.5.3, §29.9.1).

2. Using the redox tower, explain why sulfate reduction and methanogenesis occur below nitrate and iron reduction in a sediment, and why syntrophy is needed for the complete degradation of fatty acids under anoxia.

   **Answer** Organisms that use the acceptor with the more positive potential gain more energy per electron and lower the donor concentration below what the others need, so the acceptors are used in the order $\ce{O2}$, nitrate, Mn(IV), Fe(III), sulfate, $\ce{CO2}$ with depth (§7.3.1). The oxidation of propionate or butyrate to acetate and $\ce{H2}$ is endergonic at standard conditions; it becomes exergonic only when a methanogen or sulfate reducer keeps $\ce{H2}$ at very low partial pressure, and both partners then share the small available free energy (§7.5.1, Example 7.5.1).

3. Give three examples from different chapters in which a single horizontal transfer changed a bacterium's medical significance, and name the mobile element involved.

   **Answer** Lysogenic conversion: the cholera toxin genes are carried by the phage CTXφ, and diphtheria toxin by a prophage (Definition 23.3.2). Pathogenicity islands: the type III secretion system of *Salmonella* is encoded on islands acquired by transfer (§33.10, §34.6.1). Resistance: *mecA* on the SCC*mec* element makes *Staphylococcus aureus* MRSA, and carbapenemase genes on plasmids and transposons spread among Enterobacterales (§15.3.2, §15.6.2).

4. The same mathematics of a reproduction number appears for a phage in a culture, a virus within a host and an infection in a human population. State the threshold in each case and what lowers it below 1.

   **Answer** Within a host, $R_0 = \beta pT_0/(\delta c)$ (Formula 27.6.1): the infection spreads if each infected cell produces more than one newly infected cell; drugs that reduce $\beta$ or $p$ push it below 1. In a population, $R_t = R_0 s_t$ (§35.3.1): an epidemic grows while $R_t > 1$ and declines when susceptibles fall below $1/R_0$, which vaccination achieves above the herd-immunity threshold $1 - 1/R_0$ (Eq. (28.2)). For a phage in a chemostat, each adsorbed particle must yield more than one new successful infection before it is washed out; this holds only if the host density exceeds $N^* \approx D/[\delta(\beta\mathrm{e}^{-D\tau} - 1)]$ (from Eq. (23.2)), so a small burst, slow adsorption or a long latent period raises the threshold. Predation holds the host near $N^*$, far below its resource-limited density, and the cost of resistance lets sensitive hosts, resistant hosts and phage coexist (§23.9).

5. Why can a culture survive an antibiotic although every colony recovered from it is still fully susceptible, and why is a biofilm infection hard to cure for the same reason?

   **Answer** A population contains a small fraction of dormant persisters that pre-exist the drug and are killed slowly, so the killing curve is biphasic (Formula 15.5.1); survivors that regrow produce a population with the same MIC (Definition 15.5.1). In a biofilm, consumption against diffusion produces starved, slowly growing layers when the Thiele modulus exceeds 1 (Formula 12.9.1); these cells are tolerant like persisters, and the matrix and the protection from phagocytes add to the effect (§12.9.3).
