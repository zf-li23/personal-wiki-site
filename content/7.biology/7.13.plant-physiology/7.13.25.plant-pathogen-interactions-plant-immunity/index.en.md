---
title: Plant–Pathogen Interactions and Plant Immunity
description: Plant diseases, pathogen types, trophic strategies and the disease triangle; pathogen virulence strategies and effector proteins; pattern-triggered immunity (PRRs, FLS2–BAK1–BIK1, the ROS burst, calcium channels, stomatal immunity); the gene-for-gene hypothesis, NLR structure and recognition modes, resistosomes and TIR enzymatic activity, the hypersensitive response and the zigzag model; mutual potentiation of PTI and ETI; systemic acquired resistance (SA, NHP, NPR1), induced systemic resistance and systemic stomatal immunity; SA–JA antagonism; antiviral RNA silencing and closure of plasmodesmata; the van der Plank epidemic model, vertical and horizontal resistance, durable resistance and resistance breeding.
source_hash: 58f0b95ef31c
---

Plants live among microbes throughout their lives. Enormous numbers of bacteria, fungi and oomycetes inhabit leaf surfaces, the rhizosphere and the interior of tissues, yet only a very few of them can make a given plant sick. A pathogen can usually infect only a few plant species, and a plant is resistant to the vast majority of potential pathogens. Even so, disease reduces crop yields worldwide by roughly 10%–30% each year. Plants have no circulating immune cells, no antibodies and no adaptive immunity; instead each cell has autonomous innate immunity. Receptors on the cell surface recognize molecular patterns shared by microbes, intracellular receptors recognize effector proteins that pathogens inject into the cell, and the signals from both layers of immunity spread through the whole plant by hormones and mobile signals. This chapter begins with the history of plant disease and the lifestyles of pathogens, then discusses the receptors and signaling of the two layers of immunity, the counter-measures of pathogens and systemic resistance, and finally uses simple epidemic models to explain the field significance of resistance and the strategies of resistance breeding. The biology of pathogenic microbes themselves and symbioses of plants with beneficial microbes are in [7.11.31](/7.11.31); the genetics of host–pathogen coevolution (the gene-for-gene model and the matching-alleles model) is in [7.10.17](/7.10.17#sec-17.2.4); innate immunity in animals is in 7.15; the synthesis and signaling of the hormones involved are in [7.13.15](/7.13.15); interactions between herbivores and plants are in the next chapter, [7.13.26](/7.13.26).

## 25.1. Plant Diseases and Pathogens

### 25.1.1. The Birth of Plant Pathology

The potato was introduced into Europe from South America in the sixteenth century and by the early nineteenth century had become the staple food of Irish farmers. From 1845 a previously unknown disease blackened and rotted the foliage of whole potato fields within weeks, and tubers continued to rot in storage. In the Great Famine of 1845–1849 about 1–1.5 million people in Ireland died of starvation and disease and about 2 million emigrated to North America and elsewhere; the population fell from more than 8 million to a little over 6 million and did not recover for a long time.

This catastrophe spurred the founding of plant pathology. The prevailing view was that the mold on diseased leaves grew only after the plant had become "sick"; in 1846 the Englishman M. J. Berkeley proposed the opposite: the plant is sick because the mold is growing on it. In 1861 the German Anton de Bary inoculated spores from diseased plants onto healthy plants and observed that the spores germinated, penetrated the leaves and caused the same disease, proving that the causal agent of late blight is an organism, later named *Phytophthora infestans*. *P. infestans* is an **oomycete**; phylogenetically it belongs to the stramenopiles, close to brown algae and diatoms, and is not a fungus. Whether it originated in central Mexico or in the Andean region of South America is still debated in molecular phylogeographic studies.

Over the following decades the etiology of plant disease developed rapidly. In the 1870s Pasteur and Koch established the germ theory of animal infectious disease, and Koch's postulates apply equally to plant disease. In 1878 T. J. Burrill showed that fire blight of pear and apple is caused by a bacterium (now called *Erwinia amylovora*). In 1892 D. Ivanovsky and in 1898 M. Beijerinck found that the agent of tobacco mosaic disease passes through fine porcelain filters that retain bacteria; Beijerinck called it a "contagious living fluid" (*contagium vivum fluidum*). This was the first **virus** to be discovered, tobacco mosaic virus (TMV). Nematodes were recorded as plant pathogens even earlier: in 1743 J. T. Needham described the wheat seed gall nematode (*Anguina tritici*), and in the 1850s Berkeley studied root-knot nematodes of cucumber.

### 25.1.2. Types of Pathogens

The organisms that cause plant disease belong to several distantly related groups (Table 25.1). Measured by the losses they cause, fungi and oomycetes are the most important, followed by viruses and bacteria; parasitic plants ([7.13.26](/7.13.26)) are also a kind of pathogen.

| Group | Characteristics | Routes of entry | Examples |
|---|---|---|---|
| Fungi | Eukaryotic, chitinous cell walls; ascomycetes form meiospores in asci, basidiomycetes on basidia | Direct penetration of cuticle and cell wall by appressoria using turgor and hydrolytic enzymes; stomata; wounds | Rice blast fungus (*Magnaporthe oryzae*), wheat stem rust fungus (*Puccinia graminis*), gray mold (*Botrytis cinerea*), powdery mildew fungi |
| Oomycetes | Eukaryotic, cell walls mainly of cellulose and β-glucan; zoospores | Direct penetration; stomata | *P. infestans*, *Phytophthora sojae*, downy mildews |
| Bacteria | Prokaryotic; mostly Gram-negative | Stomata, hydathodes, lenticels, wounds; insect vectors | *Pseudomonas syringae*, *Xanthomonas*, *Ralstonia solanacearum* |
| Viruses | Cannot actively penetrate the cell wall | Wounds; vectors such as aphids, whiteflies and leafhoppers deliver virus directly into the vascular system; seeds and pollen | TMV, cucumber mosaic virus, tomato yellow leaf curl virus |
| Nematodes | Multicellular animals that pierce cell walls with a stylet | Root epidermis (most); a few infect stems and leaves | Root-knot nematodes (*Meloidogyne*), cyst nematodes (*Heterodera*, *Globodera*) |

### 25.1.3. Trophic Strategies of Pathogens

How a pathogen obtains nutrients from its host determines how the host should resist it, and this is one of the main threads for understanding plant immunity.

**Definition 25.1.1 (Biotrophic, Necrotrophic and Hemibiotrophic Pathogens)** A pathogen that grows in living host tissue and obtains nutrients from living cells without killing them is called a **biotroph**; a pathogen that first kills host cells with toxins or cell wall-degrading enzymes and then uses the nutrients in the dead tissue is called a **necrotroph**; a pathogen that lives biotrophically early in infection and later switches to killing host cells is called a **hemibiotroph**.

Biotrophic pathogens maintain a "feigned harmony" with the host: they secrete few cell wall-degrading enzymes, try to avoid triggering host defenses, and often take up nutrients through **haustoria**, which extend into the cell but remain outside the host plasma membrane. Many are obligate parasites that cannot be cultured away from a living host, such as rust fungi, powdery mildews and downy mildews. Necrotrophic pathogens "grab and run": they secrete toxins and large amounts of hydrolytic enzymes that macerate and rot tissue (as in gray mold caused by *B. cinerea*), and often have a wide host range. *P. infestans* is a typical hemibiotroph: in the first day or two of infection it secretes effector proteins that suppress host defenses and cell death, and the leaf shows no symptoms; it then secretes necrosis-inducing proteins, the tissue dies rapidly, and the lesion expands and produces large numbers of spores.

This distinction has direct physiological consequences: killing infected cells starves a biotroph but plays into the hands of a necrotroph. Section 25.4.5 shows that the typical response of plants to the former is local cell death, and Section 25.5.5 explains how the two kinds of response are dominated by two different hormones.

### 25.1.4. The Disease Triangle

Plants are constantly exposed to large numbers of microbes, but only very few encounters lead to disease, which requires three conditions to be met at once.

**Definition 25.1.2 (Disease Triangle)** Disease occurs only when a susceptible host, a pathogen with sufficient virulence and an environment favorable to the pathogen are all present; the relationship among the three is called the **disease triangle**.

Environmental factors include temperature, rainfall and the duration of leaf wetness, wind, soil water and nutrients, planting density, pollution and other organisms. For example, potato late blight is epidemic in cool, rainy weather with dew on the leaves at night, and in the field forecasts commonly use combinations of temperature and relative humidity. Human activity adds a fourth dimension to the triangle (sometimes called the disease tetrahedron or pyramid): the movement of people and plants carries pathogens and vectors to new regions, large monocultures that are genetically uniform allow a pathogen that has overcome resistance to spread rapidly (the 1970 southern corn leaf blight epidemic in the United States, [7.10.17](/7.10.17#sec-17.2.4)), and tillage and irrigation change the field microclimate.

The disease triangle also explains where a plant's resistance to most pathogens comes from. For the vast majority of microbes a plant is a "nonhost": they either cannot adapt to its physical and chemical barriers or are completely suppressed by its basal immunity. This resistance, effective against all strains of a species, is called *nonhost resistance*; it is the most widespread and most durable form of resistance and is carried mainly by the first layer of immunity discussed below.

### 25.1.5. Pathogen Virulence Strategies

A successful pathogen must find the host and attach to its surface, cross the host's barriers into the tissue, evade or suppress host defenses, grow and multiply there, and then spread to other plants.

- Entry: many fungi form appressoria on the leaf surface and penetrate the epidermis directly, using turgor pressures of up to several megapascals together with cutinases and cell wall-degrading enzymes; bacteria and many fungi enter through natural openings such as stomata, hydathodes and lenticels, or through wounds; wounds made by herbivorous insects and piercing–sucking mouthparts are entrances for viruses and some bacteria, and aphids and whiteflies inject viruses directly into sieve tubes.
- Enzymes: cutinases, cellulases, xylanases, pectinases and polygalacturonases break down the cuticle and cell walls; the cell wall fragments they produce are also signals by which the host recognizes damage (Section 25.2.1).
- Toxins: host-specific toxins act only on hosts of particular genotypes, such as HC-toxin of *Cochliobolus carbonum*, which inhibits histone deacetylases of maize; nonspecific toxins act on many plants, such as fusicoccin of *Fusicoccum amygdali*, which irreversibly activates the plasma membrane $\ce{H+}$-ATPase through 14-3-3 proteins, so that guard cells take up large amounts of $\ce{K+}$, the stomata stay open and the plant wilts and dies ([7.13.10](/7.13.10)).
- Hormones and hormone mimics: *Gibberella fujikuroi* secretes **gibberellin**, which makes infected rice overgrow (bakanae, "foolish seedling" disease), and gibberellin was in fact discovered through this disease ([7.13.14](/7.13.14)); coronatine of *P. syringae* is a structural analog of the active jasmonate JA-Ile (Section 25.5.5); *Agrobacterium tumefaciens* transfers genes for the synthesis of auxin and cytokinin into the host genome ([7.11.17](/7.11.17)).

The effects of disease on host physiology also follow regular patterns. In vascular diseases (such as Fusarium wilt and bacterial wilt) the pathogen or the gums it secretes plug the vessels, and host callose and tyloses also occlude them, so the leaves wilt. The respiration rate of infected tissue often rises several-fold, owing to the respiration of the pathogen itself, loss of compartmentation in host cells that lets enzymes meet substrates, concentration of sugars at the infection site, and the energy cost of the defense response itself. Chloroplasts are damaged and photosynthesis declines. The hormone balance is disturbed: rust raises auxin content at the infection site, rice bakanae involves excess gibberellin, and wheat dwarf (a viral disease) lowers gibberellin levels and stunts the plant.

## 25.2. Pattern-Triggered Immunity

### 25.2.1. Molecular Patterns and Pattern Recognition Receptors

The first layer of plant immunity recognizes molecules that microbes cannot do without and that are therefore hard to alter. A **pathogen-associated molecular pattern**, abbreviated PAMP (also called a microbe-associated molecular pattern, MAMP, because it is also present in nonpathogenic microbes), is conserved in a large group of microbes and absent from the host: examples are bacterial flagellin, elongation factor EF-Tu, **lipopolysaccharide** and **peptidoglycan**, fungal **chitin**, and the 13-residue peptide Pep13 from the cell wall transglutaminase of oomycetes. Plants also recognize signals of their own damage, **damage-associated molecular patterns** (DAMPs): oligogalacturonides from the degradation of cell wall pectin, extracellular ATP, and the peptide hormones released after wounding, **systemin** (tomato) and Pep peptides.

They are recognized by **pattern recognition receptors** (PRRs) in the plasma membrane. Plant PRRs are of two kinds: receptor-like kinases (RLKs) have an extracellular domain, a single transmembrane segment and an intracellular serine/threonine kinase domain; receptor-like proteins (RLPs) lack an intracellular kinase domain and must associate with an RLK to transmit signals. There are two main types of extracellular domain: leucine-rich repeats (LRRs) recognize peptides, and LysM domains recognize *N*-acetylglucosamine-containing glycans such as chitin and peptidoglycan.

| Molecular pattern | Source | Receptor (*Arabidopsis* unless noted) | Extracellular domain |
|---|---|---|---|
| flg22 (conserved N-terminal 22-residue peptide of flagellin) | Bacteria | FLS2 | LRR |
| elf18 (N-terminal 18-residue peptide of EF-Tu) | Bacteria | EFR (Brassicaceae only) | LRR |
| Chitin oligosaccharides | Fungi | CERK1 and LYK5; in rice CEBiP (RLP) and OsCERK1 | LysM |
| Peptidoglycan | Bacteria | LYM1, LYM3 (RLPs) and CERK1 | LysM |
| Oligogalacturonides | Own cell wall (DAMP) | WAK1 | EGF-like |
| Extracellular ATP | Own damaged cells (DAMP) | DORN1 (P2K1) | Lectin |
| Pep1 | Own precursor PROPEP1 (DAMP) | PEPR1, PEPR2 | LRR |

**Definition 25.2.1 (Pattern-Triggered Immunity)** The defense response triggered when a **pattern recognition receptor** in the plasma membrane recognizes a pathogen-associated molecular pattern or damage-associated molecular pattern is called **pattern-triggered immunity** (PTI).

PTI blocks the great majority of microbes not adapted to the host; it is the main source of nonhost resistance and also of basal resistance to adapted pathogens. Because it recognizes conserved molecules, PTI cannot distinguish pathogens from beneficial microbes: the Nod factors of rhizobia and the Myc factors of mycorrhizal fungi are structurally similar to chitin, and their LysM receptors evolved from defense receptors ([7.11.31](/7.11.31)); symbiotic microbes must suppress PTI with dedicated effector proteins and signals in order to colonize.

### 25.2.2. From Receptor to Defense: FLS2 Signaling

FLS2 is the best-studied PRR. At rest FLS2 is bound to the cytoplasmic receptor-like cytoplasmic kinase (RLCK) BIK1. When flg22 binds the LRR of FLS2, within seconds the coreceptor BAK1 (a member of the SERK family, also involved in signaling by the brassinosteroid receptor BRI1) is recruited; flg22 acts as a molecular glue that holds the extracellular domains of the two together, the intracellular kinase domains phosphorylate each other, and BIK1 is then phosphorylated. The released BIK1 phosphorylates a series of downstream proteins:

1. The NADPH oxidase RBOHD: BIK1 phosphorylates its N terminus, and RBOHD passes electrons to $\ce{O2}$ on the outer side of the plasma membrane, producing superoxide, which dismutates to $\ce{H2O2}$. This **reactive oxygen species** burst begins about 2–5 min after recognition and peaks at 10–15 min. Apoplastic $\ce{H2O2}$ can kill microbes directly, cross-links and thereby strengthens cell wall proteins, and also spreads as a signal to neighboring cells.
2. Calcium channels: BIK1 phosphorylates and activates the cyclic nucleotide-gated channel complex CNGC2/CNGC4, causing $\ce{Ca^2+}$ influx; in guard cells BIK1 phosphorylates the osmosensitive calcium channel OSCA1.3, causing stomatal closure (Section 25.2.3). Cytosolic $\ce{Ca^2+}$ activates calcium-dependent protein kinases (CPKs), which in turn phosphorylate RBOHD, forming a positive feedback in which $\ce{Ca^2+}$ and ROS amplify each other.
3. MAPK cascades: within minutes two modules, MPK3/MPK6 and MPK4, are activated and phosphorylate transcription factors such as WRKYs. About 30 min after recognition the transcription of thousands of genes changes, including enzymes for the synthesis of **ethylene**, **salicylic acid** and phytoalexins, and pathogenesis-related proteins.

Slower responses appear within hours: **callose** papillae are deposited on the inner side of the cell wall, plasmodesmata at the infection site are sealed with callose (Section 25.6.2), and lignin and phenolics accumulate in the cell wall.

![The two layers of plant innate immunity (schematic). Left, pattern-triggered immunity: the bacterial molecular pattern flg22 binds the LRR receptor kinase FLS2, which recruits the coreceptor BAK1; the released receptor-like cytoplasmic kinase BIK1 phosphorylates the NADPH oxidase RBOHD (ROS burst in the apoplast: O₂ → O₂•⁻ → H₂O₂) and the calcium channel CNGC2/4 (Ca²⁺ influx); Ca²⁺ activates CPKs, and the MAPK cascade (MPK3/6) activates WRKY transcription factors and defense genes, followed by callose deposition, stomatal closure, and synthesis of pathogenesis-related proteins and phytoalexins. Right, effector-triggered immunity: the pathogen injects effector proteins into the cell through the type III secretion system; some effectors suppress components of PTI (such as BIK1), causing effector-triggered susceptibility; an intracellular NLR (N-terminal CC or TIR domain, central NB-ARC domain, C-terminal LRR) recognizes one of the effectors directly or indirectly and oligomerizes into a resistosome, causing Ca²⁺ influx and transcriptional reprogramming, often accompanied by the hypersensitive response](./plots/immunity-layers.py)

### 25.2.3. Stomatal Immunity

Bacteria enter leaves through stomata, so stomatal opening and closing is the sentinel of PTI. After the leaf surface contacts bacteria or flg22, guard cells partly close the stomata within 1–2 h, delaying bacterial entry (Melotto et al. 2006). This response requires FLS2 and BIK1–OSCA1.3 calcium signaling in guard cells, and shares the downstream OST1 kinase and SLAC1 anion channel with the pathway by which **abscisic acid** induces stomatal closure ([7.13.10](/7.13.10)). *P. syringae* counters by secreting coronatine: it mimics JA-Ile, activates jasmonate signaling through COI1, inhibits stomatal closure and reopens the stomata after 1–3 h; mutant strains unable to synthesize coronatine are greatly reduced in their ability to invade through the leaf surface.

### 25.2.4. The Cost of Immunity

A stronger immune response is not always better. Continuously activated defense consumes large amounts of carbon and nitrogen and suppresses photosynthesis, and activated defense hormones directly inhibit growth. In *Arabidopsis*, mutants with constitutively active PRRs or NLRs (such as *snc1*, a gain-of-function mutant of the NLR gene *SNC1*) and mutants that over-accumulate salicylic acid are generally dwarfed with curled leaves, often with spontaneous cell death; when two accessions of the same species are crossed, incompatible combinations of immune genes from the two parents sometimes cause *hybrid necrosis*. This trade-off between resistance and yield is also common in breeding: cultivars carrying strong resistance genes sometimes yield less. Therefore the number and activity of immune receptors and the downstream signaling are all under strict negative regulation: PRR complexes are kept inactive by phosphatases at rest and degraded by ubiquitination after activation, and the transcripts of many NLR genes are regulated by miRNAs (Section 25.4.2). The allocation of resources between plant growth and defense is discussed with a simple model in the next chapter ([7.13.26](/7.13.26#sec-26.3.6)).

## 25.3. Effector Proteins and Effector-Triggered Susceptibility

Pathogens adapted to a host can suppress its PTI. Their weapons are **effectors**: molecules, mostly proteins, that the pathogen secretes into the host apoplast or injects into host cells and that alter the host's structure, metabolism or hormone balance to the pathogen's advantage.

Gram-negative bacterial pathogens use the **type III secretion system** to inject effector proteins directly into host cells: it is a syringe-like structure with a hollow needle that spans the inner and outer bacterial membranes ([7.11.31](/7.11.31)); a *P. syringae* strain has about 30 effector proteins and a *Xanthomonas* strain a similar number. Effectors of fungi and oomycetes are secreted through haustoria or invasive hyphae, and many oomycete effectors have an N-terminal RXLR motif associated with entry into host cells. Bacteria with the type III secretion system deleted can hardly multiply in the host, showing that effector proteins are central to pathogenicity.

Effector proteins act on every compartment of the host cell (Table 25.2).

| Effector (pathogen) | Site of action | Action |
|---|---|---|
| AvrPto, AvrPtoB (*P. syringae*) | Plasma membrane | Bind receptor kinases such as FLS2 and BAK1 and inhibit their kinase activity; AvrPtoB is also an E3 ubiquitin ligase that causes receptor degradation |
| AvrAC (*Xanthomonas campestris*) | Cytosol | Uridylylates BIK1 and its homologous kinases, blocking PTI signaling |
| Avr2 (*Cladosporium fulvum*) | Apoplast | Inhibits cysteine proteases of tomato |
| AvrE, HopM1 (*P. syringae*) | Plasma membrane, endomembranes | AvrE forms water-permeable channels in the host plasma membrane (2023); both promote "water-soaking" of the apoplast in the mesophyll, providing the bacteria with an aqueous habitat |
| TAL effectors, such as AvrBs3 (*Xanthomonas*) and PthXo1 (*Xanthomonas oryzae*) | Nucleus | Bind host promoters and activate susceptibility genes: AvrBs3 activates pepper *UPA20*, causing hypertrophy of mesophyll cells; PthXo1 activates the rice sugar transporter gene *SWEET11*, so that sucrose flows into the apoplast where the bacteria live |
| Coronatine (small molecule, *P. syringae*) | Cytosol and nucleus | Mimics JA-Ile, activates jasmonate signaling and suppresses salicylic acid-dependent defense and stomatal closure |

TAL (transcription activator-like) effectors have a special structure: the central region is a series of nearly identical repeats of 34 amino acids, and the amino acids at positions 12 and 13 of each repeat (the repeat-variable diresidue, RVD) determine the single base that repeat binds, for example HD for C, NG for T, NI for A, and NN for G or A. This protein–DNA code made it possible to design proteins that bind any sequence; fused to a nuclease domain they give the genome-editing tool **TALEN** ([7.2.24](/7.2.24)).

The result of an effector successfully suppressing PTI is called *effector-triggered susceptibility* (ETS): the pathogen multiplies extensively in the host and the host becomes diseased. To counter this, plants have evolved a second layer of immunity.

## 25.4. Effector-Triggered Immunity

### 25.4.1. The Gene-for-Gene Hypothesis

In the 1940s and 1950s H. H. Flor studied the genetics of flax and the flax rust fungus (*Melampsora lini*) and found that each resistance gene of flax is effective only against rust races carrying the corresponding avirulence gene, and so proposed the **gene-for-gene model** ([Definition 17.2.5 in 7.10.17](/7.10.17#def-17.2.5)): the host resistance gene (*R*) and the pathogen avirulence gene (*Avr*) correspond one to one, and the host is resistant only when both are present. For one locus, only one of the four combinations is incompatible (Table 25.3).

| | Pathogen *Avr* (avirulent) | Pathogen *avr* (virulent) |
|---|---|---|
| Host *R* (resistant) | Incompatible: resistant | Compatible: susceptible |
| Host *r* (susceptible) | Compatible: susceptible | Compatible: susceptible |

With several loci, the host is resistant as long as any one *R* gene recognizes any one *Avr* product of the pathogen. The name "avirulence gene" is given from the host's point of view: it makes the pathogen avirulent on a host carrying the corresponding *R* gene. Molecular studies showed that *Avr* genes encode precisely the effector proteins, whose original function is to promote pathogenicity, and that host *R* genes encode the receptors that recognize them. In 1984 B. Staskawicz and colleagues cloned the first avirulence gene from the soybean bacterial blight pathogen: introduced into a virulent race, it changed the race from compatible to incompatible on the corresponding soybean cultivar, the first molecular evidence for the gene-for-gene hypothesis. The first *R* gene was cloned in 1993 (tomato *Pto*, encoding a kinase), and in 1994 *Arabidopsis* *RPS2* (map-based cloning) and the tobacco *N* gene for resistance to TMV (transposon tagging) were cloned; they encode the same class of intracellular receptors.

### 25.4.2. NLRs

**Definition 25.4.1 (NLR)** An immune receptor that recognizes pathogen effector proteins inside the cell and consists of an N-terminal domain, a central nucleotide-binding domain (NB-ARC) and a C-terminal leucine-rich repeat domain (LRR) is called an **NLR** (nucleotide-binding leucine-rich repeat receptor), also called an NB-LRR protein; the resistance proteins encoded by most resistance genes (*R* genes) belong to this class.

**Definition 25.4.2 (Effector-Triggered Immunity)** The defense response caused when an **NLR** recognizes a pathogen effector protein, directly or indirectly, is called **effector-triggered immunity** (ETI).

By N-terminal domain, NLRs fall into three classes: CNLs with an N-terminal coiled coil (CC; for example RPS2 and ZAR1); TNLs with an N-terminal Toll/interleukin-1 receptor-like domain (TIR; for example tobacco N, RPP1 and Roq1); and RNLs with an N-terminal coiled coil resembling that of the powdery mildew resistance protein RPW8 (CC<sub>R</sub>; ADR1 and NRG1), which are the "helpers" of many NLRs (Section 25.4.3). TNLs occur only in eudicots, gymnosperms and a few other groups; grasses have no TNLs and no NRG1, which they require.

The NB-ARC domain is a molecular switch, homologous to animal NOD-like receptors and the apoptotic protein APAF-1. Several conserved motifs each have a role: the P-loop (GxxxxGKS/T) binds the phosphate groups of the nucleotide, and mutations reduce binding and inactivate the receptor; the Walker B motif (hhhhDD, h a hydrophobic residue) coordinates $\ce{Mg^2+}$; the MHD motif participates in nucleotide binding, and mutations often make the NLR self-activating. A resting NLR binds ADP, and the LRR domain locks it in the closed conformation; after recognition of the effector, ADP is exchanged for ATP (or dATP), the conformation opens, and several NLR molecules oligomerize (Section 25.4.4).

Plants have many more NLRs than animals: about 150 in *Arabidopsis*, about 190 in tomato, about 500 in rice, and more than 1000 in some wheat varieties. Unlike human and mouse NLRs, which retain clear orthologous relationships, plant NLRs have expanded independently in different species and orthologs are hard to find; many NLR genes are arranged in clusters, within which gene duplication, unequal crossing over and gene conversion continually generate new recognition specificities, and the LRR sites in contact with effectors are under diversifying selection. These are the molecular traces of the host–pathogen **evolutionary arms race**. Excess NLRs harm the plant, and many NLR transcripts are cleaved by miRNAs: the miR482 family of tomato targets the conserved sequence encoding the P-loop, so that a single miRNA can down-regulate many NLRs at once (of the 186 annotated NLRs in tomato, 58 are targets of miR482), and the cleavage products also generate secondary siRNAs that amplify the silencing. During pathogen infection miR482 levels fall and NLR expression can rise.

### 25.4.3. How NLRs Recognize Effector Proteins

NLRs recognize effector proteins in two ways.

Direct recognition: the LRR or another domain of the NLR binds the effector directly, as in flax L protein with the rust fungus AvrL567, *Nicotiana benthamiana* Roq1 with *Xanthomonas* XopQ, and *Arabidopsis* RPP1 with the downy mildew ATR1. Direct recognition puts receptor and effector into a "one-to-one" arms race: the pathogen escapes recognition simply by changing the contact surface of the effector, and the host must produce new LRR variants, which is exactly the situation described by the gene-for-gene model.

Indirect recognition: more NLRs do not bind the effector but monitor the host targets of effectors.

**Definition 25.4.3 (Guard Hypothesis)** The recognition mode in which an NLR binds and monitors a host protein (the guardee) and is activated when an effector modifies this protein is called the **guard hypothesis**; a monitored protein that no longer has a physiological function of its own and serves only as bait is called a *decoy*.

*Arabidopsis* RIN4 is the classic guardee: the *P. syringae* effectors AvrRpm1 and AvrB phosphorylate RIN4 and are sensed by the CNL protein RPM1 that binds it; the effector AvrRpt2 is a cysteine protease that cleaves RIN4 and is sensed by RPS2. The advantage of indirect recognition is that one receptor can recognize several structurally unrelated effectors that act on the same target, and a pathogen that wishes to escape recognition must give up modifying this target, that is, give up part of its virulence.

An example of a decoy is ZAR1: it binds the pseudokinase RKS1; the *Xanthomonas* effector AvrAC is meant to uridylylate BIK1 to block PTI, but it also uridylylates the decoy kinase PBL2, which resembles BIK1, and uridylylated PBL2 binds RKS1 and thereby activates ZAR1. Some NLRs have integrated the decoy directly into their own sequence: in rice the paired CNL proteins RGA4 and RGA5 together recognize the rice blast effector AVR-Pia; the C terminus of RGA5 has a heavy metal-associated (HMA) domain that mimics the true target of the effector, and binding of AVR-Pia relieves the inhibition of RGA4 by RGA5, whereupon RGA4 causes cell death.

Paired and networked NLRs separate recognition from execution: "sensor" NLRs responsible for recognition activate "helper" NLRs responsible for signal output. In Solanaceae, dozens of sensor NLRs depend on a few NRC helpers (NRC2, NRC3, NRC4), forming a hierarchical immune receptor network; signaling by TNLs requires the RNL-type helpers ADR1 and NRG1.

### 25.4.4. Resistosomes

Cryo-electron microscopy structures in recent years have revealed the form of NLRs after activation.

**Definition 25.4.4 (Resistosome)** The macromolecular complex formed by oligomerization of an NLR after activation by an effector protein is called a **resistosome**; the resistosomes of CNLs and RNLs are cation channels in the plasma membrane, and the resistosomes of TNLs generate signaling molecules through the enzymatic activity of their TIR domains.

- ZAR1 (2019, *Science*): after uridylylated PBL2 binds RKS1, ZAR1 releases ADP and binds dATP, and five ZAR1–RKS1–PBL2<sup>UMP</sup> units assemble into a wheel-shaped pentamer; the α1 helices at the N termini of the five CC domains protrude and form a funnel that inserts into the plasma membrane. A 2021 study (*Cell*) showed that the ZAR1 resistosome is a calcium channel: it mediates $\ce{Ca^2+}$ influx at the plasma membrane, causing ROS accumulation and cell death. The resistosome of the Solanaceae helper NRC4, solved in 2024, is also a pore-forming oligomer.
- RNLs: NRG1 and ADR1 likewise oligomerize when activated and form $\ce{Ca^2+}$-permeable channels in the plasma membrane (2021, *Science*); they are the executors of TNL signaling.
- TNLs: the complexes of Roq1 with XopQ and of RPP1 with ATR1 (2020, *Science*) are both tetramers in which four TIR domains face each other in pairs to form an enzymatic active center. The TIR domain is an $\ce{NAD+}$ hydrolase (2019), and activated TIR converts $\ce{NAD+}$, ATP and other substrates into several small nucleotide-derived molecules: 2'-(5''-phosphoribosyl)-5'-adenosine monophosphate (pRib-AMP) and pRib-ADP bind the heterodimer of the lipase-like proteins EDS1 and PAD4 and activate ADR1; ADP-ribosylated ATP (ADPr-ATP) and di-ADP-ribose bind EDS1–SAG101 and activate NRG1 (2022, *Science*).

Thus the intracellular immune receptors of plants all converge on the same exit: opening a calcium channel in the plasma membrane.

![Activation of the ZAR1 resistosome (schematic, based on structures published in 2019 and 2021). A: At rest ZAR1 (CC, NB-ARC and LRR domains) binds ADP and associates with the pseudokinase RKS1; the *Xanthomonas* effector AvrAC uridylylates the decoy kinase PBL2, PBL2ᵁᴹᴾ binds RKS1, ZAR1 exchanges ADP for dATP, and five ZAR1–RKS1–PBL2ᵁᴹᴾ units assemble into a pentamer (top view). B: The α1 helices of the five CC domains form a funnel that inserts into the plasma membrane, and the resistosome becomes a Ca²⁺-permeable channel; the rise in cytosolic Ca²⁺ causes ROS, transcriptional reprogramming and hypersensitive cell death](./plots/zar1-resistosome.py)

### 25.4.5. The Hypersensitive Response and Local Defense

A common phenotype of ETI is the rapid death of cells around the infection site.

**Definition 25.4.5 (Hypersensitive Response)** The rapid programmed death of host cells, within hours, at and around the site of pathogen infection, forming a restricted necrotic lesion that deprives the pathogen of nutrients and prevents its spread, is called the **hypersensitive response** (HR).

The hypersensitive response is a form of plant **programmed cell death** ([7.3.25](/7.3.25), [7.13.24](/7.13.24)). It is often preceded by rapid accumulation of reactive oxygen species and nitric oxide (NO), and both are required: raising only one of them induces cell death very little. Experimentally, the hypersensitive response appears as a local necrotic lesion at the inoculation site (for example, on tobacco leaves, cultivars carrying the *N* gene form only local lesions in response to TMV and do not become systemically diseased, which is the principle of the local-lesion assay for virus concentration); trypan blue staining shows that dead cells are confined to the infection site, and the hyphae and haustoria of the pathogen no longer expand. The hypersensitive response is particularly effective against biotrophic pathogens; ETI resistance, however, does not always require cell death, and in many cases multiplication of the pathogen is already suppressed before cell death occurs.

Accompanying PTI and ETI, a series of local defense responses also occurs at the infection site:

- Reinforcement of the cell wall: lignin and callose are deposited; structural cell wall proteins such as hydroxyproline-rich glycoproteins are oxidatively cross-linked by $\ce{H2O2}$, making the wall harder to digest. Phenylalanine ammonia-lyase (PAL) is the first enzyme in the synthesis of lignin and many phenolic defense compounds, and its activity is closely related to resistance ([7.13.26](/7.13.26)).
- *Phytoalexins*: low-molecular-weight secondary metabolites that are synthesized at the infection site only after infection and are strongly toxic to microbes. Plants do not store the enzymes that make them in advance but transcribe them after infection. Different families use different compounds: legumes mostly use isoflavonoids (medicarpin in alfalfa, glyceollin in soybean), Solanaceae mostly sesquiterpenoids (rishitin in potato and tomato, capsidiol in pepper and tobacco), and *Arabidopsis* uses camalexin, derived from tryptophan. Tobacco transformed with a stilbene synthase gene that makes resveratrol shows markedly increased resistance to a fungus; conversely, pathogens carrying genes for enzymes that degrade phytoalexins can infect plants that are otherwise resistant.
- *Pathogenesis-related proteins* (PR proteins): a group of low-molecular-weight proteins (6–43 kDa) whose expression is induced after infection, located in the vacuole or apoplast, including chitinases and β-1,3-glucanases that hydrolyze fungal cell walls (the two are often induced together), thaumatin-like proteins, antimicrobial peptides such as defensins, and protease inhibitors; the function of PR1 is still not completely understood, but it is a marker gene of salicylic acid signaling. Plant **lectins** bind polysaccharides of the fungal cell wall and inhibit hyphal growth and spore germination.

### 25.4.6. The Zigzag Model

Putting the two layers of immunity and the pathogen's counter-measures together, Jones and Dangl (2006) proposed an overarching model.

**Definition 25.4.6 (Zigzag Model)** The model that summarizes the two layers of plant immunity by the rise and fall of defense strength during the host–pathogen interaction is called the **zigzag model**: in the first phase, PRRs recognize PAMPs, causing PTI; in the second phase, adapted pathogens secrete effector proteins that suppress PTI, causing effector-triggered susceptibility; in the third phase, an NLR recognizes one of the effectors, causing strong ETI that often exceeds the threshold of the hypersensitive response; in the fourth phase, natural selection makes the pathogen lose or alter the recognized effector, or acquire new effectors that suppress ETI, so that the host becomes susceptible again, and NLR alleles that recognize the new effectors are then selected.

![The zigzag model of plant immunity (schematic, after Jones and Dangl 2006). The vertical axis is the strength of the defense response, and the two dashed lines are the threshold for effective resistance and the threshold for the hypersensitive response (HR). PRR recognition of a PAMP causes pattern-triggered immunity (PTI); effector A suppresses PTI, causing effector-triggered susceptibility (ETS); NLR-1 recognizes effector A, causing effector-triggered immunity (ETI) whose strength exceeds the HR threshold; the pathogen loses A and acquires effector B, so the plant is susceptible again; NLR-2 recognizes B, causing another round of ETI; effector C escapes recognition, and so on. The horizontal axis represents both the course of a single infection and many rounds of host–pathogen coevolution](./plots/zigzag.py)

The zigzag model describes ETI as an "amplified version" of PTI after it has been suppressed: the two use many of the same downstream components (calcium signaling, ROS, MAPKs, salicylic acid), while ETI is stronger and more lasting and often accompanied by the hypersensitive response. It is also a picture of coevolution: each "zig" corresponds to one adaptation and counter-adaptation between host and pathogen.

### 25.4.7. Mutual Potentiation of PTI and ETI

The zigzag model draws the two layers of immunity as two successive and independent phases. Several studies published together in 2021 (*Nature*) revised this: in *Arabidopsis* lacking PRRs (such as the *fls2 efr cerk1* triple mutant), activating ETI alone can hardly restrict bacterial growth or cause a full hypersensitive response; conversely, ETI makes the PTI ROS burst stronger and longer-lasting by raising the transcript and protein levels of PTI components such as RBOHD, BIK1 and the PRRs. That is, the two layers of immunity are not two parallel pathways but one system that amplifies itself: ETI restores and strengthens PTI that has been weakened by effectors, and PTI in turn is a prerequisite for ETI to exert its full effect. The EDS1–PAD4–ADR1 module downstream of TNLs also takes part in PTI and stomatal immunity and is a node at which the two layers of immunity meet at the molecular level.

## 25.5. Systemic Defense

### 25.5.1. Systemic Acquired Resistance

**Definition 25.5.1 (Systemic Acquired Resistance)** The phenomenon in which, after a plant is locally infected by a pathogen (especially an infection that causes the hypersensitive response), uninfected distant tissues develop lasting, broad-spectrum resistance to many later pathogens is called **systemic acquired resistance** (SAR).

SAR is established 1–2 days after the primary infection and can last 2–3 weeks or longer; it is effective against viruses, bacteria, fungi and oomycetes regardless of the type of the primary pathogen. Leaves in the SAR state express PR genes (*PR1*, *PR2*, *PR5*) at high levels even before they are reinfected, and are in a "primed" state: on reinfection the defense response is faster and stronger.

The establishment of SAR requires **salicylic acid**. In infected leaves salicylic acid is synthesized mainly by the isochorismate synthase ICS1 pathway in plastids, and its content rises several tens of times within a day, later also in distant leaves; transgenic plants expressing the bacterial salicylate hydroxylase (NahG, which degrades salicylic acid to catechol) cannot establish SAR. However, salicylic acid itself is not the signal that travels long distances in the phloem: in grafting experiments, an infected salicylic acid-deficient (*NahG*) rootstock can still make wild-type scions develop SAR. The salicylic acid in distant leaves is newly synthesized there.

What, then, is the mobile signal? Several candidates have been proposed, and they may act together:

- Methyl salicylate (MeSA): in tobacco, blocking the methylation of salicylic acid in infected leaves, or blocking the demethylation of MeSA in distant leaves, abolishes SAR (2007).
- *N*-Hydroxypipecolic acid (NHP) and its precursor pipecolic acid (Pip): synthesized from lysine by ALD1, SARD4 and the flavin monooxygenase FMO1 (2018); the *fmo1* mutant cannot establish SAR at all, and exogenous NHP can induce SAR. In distant leaves NHP and salicylic acid promote each other's synthesis, forming a positive feedback.
- Azelaic acid (AzA), glycerol-3-phosphate (G3P) and the diterpenoid dehydroabietinal (DA); the lipid transfer protein DIR1, expressed in the phloem, is required for long-distance movement of the signal.

The measured speed of SAR signal transmission is about $3\,\mathrm{cm\,h^{-1}}$, much faster than diffusion alone, and most evidence points to the phloem.

![Systemic acquired resistance (schematic). A: Infection of a local leaf (red dots) causes ETI and the hypersensitive response, and salicylic acid (SA) and pipecolic acid/N-hydroxypipecolic acid (Pip/NHP) accumulate; mobile signals (NHP/Pip, methyl salicylate MeSA, azelaic acid AzA, glycerol-3-phosphate G3P and dehydroabietinal DA, requiring the lipid transfer protein DIR1) reach distant leaves through the phloem. In distant leaves NHP (synthesized via ALD1, SARD4 and FMO1) and SA (synthesized via ICS1) promote each other; NPR1 bound to SA enters the nucleus as a monomer and, together with TGA transcription factors, activates genes such as PR1, PR2 and PR5, and the leaf is primed. B: Schematic time course of the quantities after one local inoculation: SA in the local leaf peaks within about a day, and SA and resistance in distant leaves are established within 1–2 days, with resistance lasting for weeks](./plots/sar-signals.py)

### 25.5.2. NPR1 and the Perception of Salicylic Acid

The core regulator of SAR is NPR1 (nonexpressor of PR genes 1): screens for mutants insensitive to salicylic acid and unable to induce PR genes repeatedly yielded this one locus. NPR1 and its homologs NPR3 and NPR4 all contain a BTB domain and ankyrin repeats, and all are now known to bind salicylic acid and to be salicylic acid receptors, but with opposite actions: NPR1 is a transcriptional coactivator, and NPR3 and NPR4 are transcriptional corepressors (2018).

In the absence of infection, NPR1 stays in the cytosol as disulfide-linked oligomers. Accumulation of salicylic acid changes the cellular redox state, thioredoxins reduce NPR1 to monomers, and the monomers enter the nucleus, bind TGA-type bZIP transcription factors and activate defense genes such as *PR1*; binding of salicylic acid to NPR1 enhances its coactivator activity. At the infection site, high concentrations of salicylic acid cause NPR1 to form condensates in the cytosol, which promote the degradation of cell death-promoting proteins and keep the surrounding cells alive (2020). An alternative model was proposed earlier: at different salicylic acid concentrations NPR3 and NPR4 act as adaptors of an E3 ligase that promotes NPR1 degradation, so that NPR1 is degraded at the infection site, allowing cell death, while NPR1 accumulates in distant tissue and establishes SAR; parts of this model conflict with later structural and genetic evidence and it is no longer generally adopted.

The "memory" of SAR is also related to epigenetics: in the SAR state histone modifications on the promoters of some defense genes change, making them easier to transcribe; in some plants the primed state can even be passed to the next generation.

### 25.5.3. Induced Systemic Resistance

**Definition 25.5.2 (Induced Systemic Resistance)** The phenomenon in which certain nonpathogenic rhizosphere microbes (plant growth-promoting rhizobacteria or fungi), after colonizing the roots, increase the resistance of the whole plant to many pathogens is called **induced systemic resistance** (ISR).

Compared with SAR, ISR is caused by beneficial microbes rather than pathogens, usually depends on **jasmonic acid** and ethylene signaling and not on salicylic acid (but requires the cytosolic function of NPR1), and generally does not directly cause PR gene expression; it mainly appears as priming: when attacked by a pathogen, the ROS burst, cell wall reinforcement and accumulation of defense enzymes and secondary metabolites are faster and stronger than in uninduced plants. The earliest evidence came from carnation: after the roots were colonized by nonpathogenic *Pseudomonas fluorescens*, the resistance of the plants to Fusarium wilt increased; before inoculation there was no difference in phytoalexin levels between the two groups of plants, and after inoculation accumulation in induced plants was much faster. *Bacillus pumilus* on pea roots acts similarly: only when *Fusarium* tries to penetrate do the root cell walls rapidly deposit large amounts of callose and phenolics at the point of entry. These actions of **rhizosphere** microbes are discussed in [7.13.26](/7.13.26#sec-26.4.4).

### 25.5.4. Systemic Stomatal Immunity

SAR takes a day or two to establish, while bacteria need only a few hours to enter through the leaf surface. A study published in 2026 (*Cell*) described a faster systemic defense: after one leaf of *Arabidopsis* is infected or treated with a PAMP, the stomata of distant uninfected leaves close within a short time, which is called systemic stomatal immunity. The signal is a small peptide, USIC, encoded by a uORF (**upstream open reading frame**) of an mRNA: it is synthesized upon PAMP induction, secreted into the apoplast in vesicles, moves over long distances and is enriched in distant leaves; the *usic* mutant retains stomatal immunity in the local leaf but loses systemic stomatal closure. In distant leaves USIC binds the receptor-like kinases SIRK1 and KIN7 directly; KIN7 moves from the plasma membrane to the tonoplast and is cleaved by a caspase-like protease (metacaspase MC4), and the cleaved KIN7 interacts with the plasma membrane $\ce{H+}$-ATPase AHA1 and the aquaporin PIP2;1, promoting stomatal closure. This pathway does not depend on salicylic acid and requires no new transcription, so it is much faster than SAR; USIC and SIRK1–KIN7 are conserved in Brassicaceae crops (rapeseed, Chinese cabbage, radish), and corresponding receptor complexes exist in tomato and tobacco.

### 25.5.5. Antagonism between Salicylic Acid and Jasmonic Acid

Two kinds of pathogens need two defense strategies, and plants dominate them with two hormones:

| | Salicylic acid pathway | Jasmonate/ethylene pathway |
|---|---|---|
| Mainly against | Biotrophic and hemibiotrophic pathogens (downy mildews, powdery mildews, *P. syringae*); phloem-feeding insects also induce it | Necrotrophic pathogens (*B. cinerea*, *Alternaria*); chewing herbivorous insects ([7.13.26](/7.13.26)) |
| Typical responses | Hypersensitive response, PR1/PR2/PR5, SAR | Plant defensin PDF1.2, protease inhibitors, secondary metabolites, ISR |
| Cell death | Promoted | Not promoted; cell death in fact benefits necrotrophs |

The two pathways inhibit each other: salicylic acid suppresses the expression of jasmonate-responsive genes through NPR1, and jasmonic acid also suppresses salicylic acid accumulation. The significance of this antagonism may be that the hypersensitive response benefits necrotrophs and so should be suppressed when they are present; concentrating resources on one effective defense also reduces the cost. Pathogens exploit this: coronatine of *P. syringae* activates the jasmonate pathway and thereby suppresses the salicylic acid pathway that is effective against it, and coronatine-producing strains are markedly more virulent.

Defense hormones are also integrated with other signals. Drought and **abscisic acid** generally suppress defense against pathogens; defense reduces the growth rate (Section 25.2.4). Defense is also regulated by the circadian clock: in *Arabidopsis* the jasmonate response peaks during the day, synchronized with the feeding rhythm of herbivorous insects ([7.13.26](/7.13.26#sec-26.3.4)), while salicylic acid accumulates at night, which may be one reason why *Arabidopsis* is more resistant to bacteria when inoculated in the morning than in the evening.

## 25.6. Viruses, Plasmodesmata and RNA Silencing

### 25.6.1. Viral Infection and Movement

Plant viruses cannot penetrate the cell wall and enter cells through wounds and vectors. Once inside, their spread from cell to cell depends on **plasmodesmata** ([7.3.23](/7.3.23)), and long-distance spread depends on the phloem. Plasmodesmata normally allow only molecules below about 1 kDa to pass freely; virus-encoded movement proteins (such as the 30 kDa movement protein of TMV) bind the viral genomic RNA and enlarge the effective pore size of plasmodesmata, delivering nucleic acid–protein complexes into neighboring cells; some viruses move through modified plasmodesmatal channels with the cooperation of several proteins, or even as whole virions.

### 25.6.2. Closing Plasmodesmata

Closing plasmodesmata is a defense: it blocks the cell-to-cell spread of viruses and also the flow at the infection site of molecules other than effector proteins and defense signals. Pathogen infection, PAMPs and salicylic acid can all induce callose deposition at the neck of plasmodesmata, narrowing their pore; the plasmodesmata-localized protein PDLP5 is required for closure induced by salicylic acid. A 2019 study (*PNAS*) revealed another layer of mechanism: high concentrations of salicylic acid cause the plant-specific plasma membrane protein remorin to oligomerize with the help of 14-3-3 proteins, membrane lipids are more often in the ordered state (sterol-enriched nanodomains), the extensibility of the plasmodesmatal plasma membrane decreases, and the pore narrows or closes accordingly; at low salicylic acid levels ordered and disordered phases are evenly distributed and plasmodesmata keep a wider aperture.

### 25.6.3. RNA Silencing

The main means of plant antiviral defense is RNA silencing (**RNA interference**, [7.2.18](/7.2.18)). The genomes of most plant viruses are RNA, and replication produces double-stranded RNA intermediates, or the genomic RNA itself folds into double-stranded regions. Host Dicer-like proteins (DCL4, DCL2) cut this double-stranded RNA into virus-derived 21–22 nt **small interfering RNAs**, which are loaded onto Argonaute proteins (AGO1, AGO2) to form silencing complexes that cleave homologous viral RNA; RNA-dependent RNA polymerase (RDR6) uses the cleaved viral RNA as a template to synthesize new double-stranded RNA, amplifying the silencing signal. siRNAs can move through plasmodesmata and the phloem, spreading silencing into tissues the virus has not yet reached, a form of systemic antiviral immunity.

The counter-measure of viruses is to encode silencing suppressors: the P19 dimer of tomato bushy stunt virus acts like a caliper, binding 21 nt siRNA duplexes by length so that they cannot be loaded onto AGO; HC-Pro of potyviruses and the 2b protein of cucumber mosaic virus also inhibit different steps of silencing. The tug-of-war between silencing and anti-silencing is the version of the zigzag model at the level of nucleic acids. Viral proteins can also be recognized by NLRs: the tobacco TNL protein N recognizes p50, the helicase domain of the TMV replicase, and its resistance requires NRG1, causing the hypersensitive response and local lesions. In agriculture, preinoculation with a mild strain can protect plants from a severe strain of the same virus (cross-protection), and one of its mechanisms is the sequence-specific RNA silencing triggered in advance by the mild strain.

## 25.7. Disease Epidemics and Resistance Breeding

### 25.7.1. The van der Plank Model

Disease in the field is a population process. For a polycyclic disease such as potato late blight or rust, which can produce many generations in one growing season, the Dutch plant pathologist J. E. van der Plank (1963) described the growth of disease with the logistic equation: let $x$ be the proportion diseased (disease severity, 0 to 1); the rate of new infection is proportional to the amount of spores produced by diseased tissue (proportional to $x$) and to the healthy tissue not yet diseased (proportional to $1 - x$),

$$
\frac{\mathrm{d}x}{\mathrm{d}t} = r\,x\,(1 - x), \tag{25.1}
$$

where the proportionality constant $r$ is called the *apparent infection rate*, with unit $\mathrm{d^{-1}}$; it is "apparent" because it lumps together infection efficiency, latent period, sporulation and many other processes without distinguishing them. Equation (25.1) is the same as logistic growth of populations ([7.11.8](/7.11.8)), and its solution is

$$
x(t) = \frac{x_0\,\mathrm{e}^{rt}}{1 - x_0 + x_0\,\mathrm{e}^{rt}}, \tag{25.2}
$$

where $x_0$ is the initial disease severity (the effective initial inoculum). When disease severity is very low, $1 - x \approx 1$ and the disease grows exponentially with doubling time $\ln 2/r$; when severity approaches 1 growth stops, because the infectable tissue is exhausted.

Equation (25.2) can be linearized: taking the logit transform of both sides,

$$
\operatorname{logit} x = \ln\frac{x}{1 - x} = \ln\frac{x_0}{1 - x_0} + r\,t, \tag{25.3}
$$

$\operatorname{logit} x$ is a linear function of time, with slope $r$. From the disease severities $x_1$ and $x_2$ of two surveys (at times $t_1$ and $t_2$) one can estimate

$$
r = \frac{\operatorname{logit} x_2 - \operatorname{logit} x_1}{t_2 - t_1}; \tag{25.4}
$$

with several surveys, a least-squares regression of the logit values on time gives the slope as the estimate of $r$ (see panel B of the epidemic curve figure below). The time at which severity reaches 50% is $t_{50} = \ln[(1 - x_0)/x_0]/r$.

**Example 25.7.1** In a susceptible potato field, disease severity is 1% on day 10 and 20% on day 18. (a) Estimate $r$. (b) If there is no control, how much longer until severity reaches 50%? (c) What is the doubling time of early disease?

**Solution** (a) $\operatorname{logit}(0.01) = \ln(0.01/0.99) = -4.595$ and $\operatorname{logit}(0.20) = \ln(0.25) = -1.386$; by Eq. (25.4), $r = (-1.386 + 4.595)/8 = 0.401\,\mathrm{d^{-1}}$. (b) At 50% severity the logit is 0, so the time required is $1.386/0.401 = 3.5\,\mathrm{d}$, that is, around day 21.5. (c) The doubling time is $\ln 2/0.401 = 1.7\,\mathrm{d}$. It takes only about 11 days to go from 1% to 50%, while at severity below 1% symptoms are almost invisible in the field: this explains why late blight often destroys a whole field "overnight", and also why control must begin before the disease is visible.

:::

For a monocyclic disease that infects only once per growing season (such as many soilborne root diseases, where the inoculum is a fixed amount in the soil), the rate of new infection is proportional only to healthy tissue, $\mathrm{d}x/\mathrm{d}t = r_{\mathrm{M}}(1 - x)$, and disease severity grows as $1 - \mathrm{e}^{-r_{\mathrm{M}}t}$; van der Plank called these "simple interest" diseases, and polycyclic diseases "compound interest" diseases.

### 25.7.2. Vertical and Horizontal Resistance

van der Plank used Eq. (25.1) to distinguish two kinds of resistance.

**Definition 25.7.1 (Vertical and Horizontal Resistance)** Resistance that is effective against some races of a pathogen but not against others is called **vertical resistance**, also called race-specific resistance; resistance that is equally effective against all races of the pathogen is called **horizontal resistance**, also called non-race-specific resistance.

Vertical resistance is mostly controlled by a single *R* gene (NLR) and appears as immunity or the hypersensitive response; genetically it is a qualitative trait. Horizontal resistance is mostly controlled by many minor-effect genes and appears as partial resistance (fewer and smaller lesions, longer latent period, less sporulation); it is a quantitative trait, and the loci controlling it are called quantitative resistance loci. In Eq. (25.2) the two act differently:

- Vertical resistance allows only a few virulent races in the field pathogen population to infect, which is equivalent to lowering the effective initial inoculum $x_0$; once a virulent race is established, its growth rate $r$ is the same as on a susceptible cultivar. If $x_0$ is reduced to $1/k$ of its original value, the disease curve is shifted later by

$$
\Delta t = \frac{1}{r}\ln\frac{x_0(1 - x_0')}{x_0'(1 - x_0)} \approx \frac{\ln k}{r}. \tag{25.5}
$$

- Horizontal resistance lowers the efficiency of infection in each generation, making $r$ smaller and the curve flatter.

Panel A of the epidemic curve figure below compares the two: at $r = 0.40\,\mathrm{d^{-1}}$, vertical resistance reduces the effective inoculum by 99% ($k = 100$) and delays $t_{50}$ by $\ln 100/0.40 = 11.5\,\mathrm{d}$; horizontal resistance halves $r$ and delays $t_{50}$ from 23 d to 46 d. The days of delay matter greatly for production: if potatoes can complete tuber bulking before the disease breaks out, the loss is much smaller. The two kinds of resistance can also be stacked: in a region with very little initial inoculum, a cultivar that lowers both $x_0$ and $r$ may suffer no epidemic during the entire growing season.

![Epidemic curves of the van der Plank model (Eq. 25.1). A: A susceptible cultivar (x₀ = 10⁻⁴, r = 0.40 d⁻¹, red line); vertical resistance reduces the effective initial inoculum by 99% (x₀ = 10⁻⁶, r unchanged, blue dashed line), shifting the whole curve later by about 11.5 days; horizontal resistance halves the apparent infection rate (r = 0.20 d⁻¹, x₀ unchanged, green line), flattening the curve; dots mark the time t₅₀ at which severity reaches 50%, and the horizontal dashed line is about 5% severity, visible to the naked eye. B: After the logit transformation all three curves are straight lines whose slope is r; squares are simulated field survey data (susceptible cultivar, with random error added), and the slope of the least-squares line gives the estimate of r. The parameter values are illustrative and comparable in order of magnitude to potato late blight on a susceptible cultivar](./plots/epidemic-curves.py)

### 25.7.3. Durable Resistance

**Definition 25.7.2 (Durable Resistance)** Resistance that remains effective when grown over large areas for a long time in environments favorable to disease is called **durable resistance**.

Vertical resistance controlled by a single *R* gene is often not durable, because it exerts strong selection on the pathogen: a mutation or loss of a single effector gene lets the pathogen escape recognition, and growing the same resistance gene over large areas causes virulent races to expand rapidly, producing a "boom-and-bust cycle": a few years after a resistant cultivar is released its resistance is "lost," and a new resistant cultivar takes its place. Wheat stem rust is a famous example: from the 1970s, wheat carrying the stem rust resistance gene *Sr31* (a translocation from rye), bred by CIMMYT (the International Maize and Wheat Improvement Center) and others, was released around the world and remained effective for decades; the stem rust race Ug99, found in Uganda in 1998–1999, overcame *Sr31* and has spread to eastern and southern Africa and the Middle East.

On the other hand, some *R* genes and resistance loci have remained effective for a long time: the tomato NLR gene *Mi-1.2* was introgressed into cultivated tomato in the 1940s from the wild species *Solanum peruvianum* and is still the main source of resistance to root-knot nematodes, and it also gives resistance to aphids and whiteflies; wheat *Lr34* encodes an ABC transporter that provides partial resistance to leaf rust, stripe rust and powdery mildew and has been used for about a hundred years without being overcome; the resistance of barley *mlo* mutants (lacking a membrane protein needed for entry of the powdery mildew fungus) to powdery mildew has remained effective since its release in Europe in 1979.

The current strategy of resistance breeding is to stack several kinds of resistance acting at different stages of infection:

- Pyramiding several *R* genes (gene stacking), especially NLRs that recognize the pathogen's core effector proteins (effectors that the pathogen can hardly lose); the probability that the pathogen overcomes several genes at once is very low; in potato, introduction of late blight-resistance NLRs from wild species (such as *Rpi-vnt1*) has markedly reduced fungicide use.
- Transfer of PRRs across species: tomato naturally lacks EFR, which recognizes EF-Tu, and after *Arabidopsis* *EFR* was introduced, tomato resistance to several bacterial diseases increased (2010). PRRs recognize conserved molecules, which pathogens can hardly escape by mutation.
- Breeding for quantitative resistance (horizontal resistance): using quantitative resistance loci and genomic selection ([7.4.24](/7.4.24)).
- Disrupting susceptibility genes: host genes needed by effectors or pathogens are called susceptibility genes, such as *MLO* and the *SWEET* genes activated by TAL effectors; editing the effector-binding site in the *SWEET* promoter gives rice broad-spectrum resistance to bacterial blight.
- In cultivar deployment, rotating and mixing cultivars carrying different resistance genes (multilines, cultivar mixtures) to avoid large-scale genetic uniformity.

Combined with the disease triangle (Definition 25.1.2), the overall measures of disease control can be classed into three kinds: weakening the pathogen (quarantine, biological control, chemical control), separating host from pathogen (crop rotation, field sanitation, control of virus vectors) and strengthening the host (proper nutrition and drainage, genetic diversity, resistance genes, quantitative resistance, and using chemical or biological means to place plants in a primed state). Methods of improving resistance by transgenesis and gene editing and their safety assessment are in [7.13.29](/7.13.29).

## Summary

| Topic | Key points | Quantitative relations and data |
|---|---|---|
| Disease and pathogens (25.1) | Late blight and the Great Famine (1845–1849), de Bary (1861), TMV (1892/1898); fungi, oomycetes, bacteria, viruses, nematodes, parasitic plants | Disease reduces crop yields by 10%–30% each year |
| Trophic strategies (Definition 25.1.1) | Biotrophs (haustoria, "feigned harmony"), necrotrophs (toxins and hydrolases), hemibiotrophs (*P. infestans*) | — |
| Disease triangle (Definition 25.1.2) | Susceptible host + virulent pathogen + favorable environment; human activity is a fourth dimension; nonhost resistance is the most widespread | — |
| Virulence strategies (25.1.5) | Appressoria, natural openings, wounds and vectors; enzymes, toxins (HC-toxin, fusicoccin), hormones (gibberellin, coronatine) | Respiration of diseased tissue often rises several-fold |
| PTI (Definition 25.2.1) | PRRs (RLKs, RLPs; LRR, LysM) recognize PAMPs/DAMPs; FLS2–BAK1–BIK1 → RBOHD, CNGC2/4, OSCA1.3, CPK, MAPK, WRKY | ROS burst from 2–5 min, peak at 10–15 min; transcriptional changes about 30 min; callose within hours |
| Stomatal immunity (25.2.3) | flg22 closes stomata; coronatine reopens them | Closure in 1–2 h, reopening after 1–3 h |
| Effectors (25.3) | Type III secretion system; target receptors, kinases, proteases, transcription; TAL RVD code; ETS | About 30 effectors per bacterial strain; 34-amino-acid repeats |
| Gene-for-gene (25.4.1) | One-to-one *R*–*Avr*; of the four cells only *R* × *Avr* is incompatible; *Avr* encodes effectors | First *Avr* 1984, *Pto* 1993, *RPS2* and *N* 1994 |
| NLRs (Definition 25.4.1) | CNL, TNL, RNL; NB-ARC switch (P-loop, Walker B, MHD); gene clusters and diversifying selection; miR482 | About 150 in *Arabidopsis*, about 500 in rice |
| Recognition modes (Definition 25.4.3) | Direct recognition; guard (RIN4–RPM1/RPS2), decoy (PBL2–RKS1–ZAR1), integrated decoy (HMA of RGA5); sensor–helper networks (NRC, ADR1, NRG1) | — |
| Resistosomes (Definition 25.4.4) | ZAR1 pentamer is a calcium channel; NRG1 and ADR1 channels; TNL tetramer TIR is an $\ce{NAD+}$ hydrolase whose products activate EDS1–PAD4/SAG101 | Structures from 2019–2024 |
| Hypersensitive response (Definition 25.4.5) | Local programmed cell death; requires ROS and NO; cell wall reinforcement, phytoalexins, PR proteins | PR proteins 6–43 kDa |
| Zigzag model (Definition 25.4.6) | PTI → ETS → ETI → ETS…; PTI and ETI potentiate each other (2021) | — |
| SAR (Definition 25.5.1) | SA required but not the mobile signal; NHP, MeSA, AzA, G3P, DA, DIR1; NPR1 and TGA; NPR3/4 are corepressors; priming and epigenetic memory | Established in 1–2 d, lasts 2–3 weeks; signal about $3\,\mathrm{cm\,h^{-1}}$ |
| ISR (Definition 25.5.2) and systemic stomatal immunity | Beneficial rhizosphere microbes, JA/ET-dependent, priming; USIC peptide–SIRK1/KIN7–MC4, SA-independent | — |
| SA–JA antagonism (25.5.5) | SA against biotrophs, JA/ET against necrotrophs and chewing insects; coronatine exploits the antagonism | — |
| Viruses (25.6) | Movement proteins enlarge plasmodesmata; callose and remorin close plasmodesmata; DCL–AGO–RDR6 RNA silencing; suppressors such as P19 | Plasmodesmal size exclusion limit about 1 kDa; siRNA 21–22 nt |
| Epidemics and breeding (25.7) | Simple and compound interest diseases; vertical resistance lowers $x_0$, horizontal resistance lowers $r$; durable resistance (*Sr31* and Ug99; *Mi-1.2*, *Lr34*, *mlo*); stacking, PRR transfer, editing of susceptibility genes | Example 25.7.1: $r \approx 0.4\,\mathrm{d^{-1}}$, doubling about 1.7 d |

Main equations:

- van der Plank model $\mathrm{d}x/\mathrm{d}t = r x(1 - x)$, Eq. (25.1); solution $x(t) = x_0\mathrm{e}^{rt}/(1 - x_0 + x_0\mathrm{e}^{rt})$, Eq. (25.2).
- Logit linearization $\operatorname{logit} x = \operatorname{logit} x_0 + rt$, Eq. (25.3); $r = (\operatorname{logit} x_2 - \operatorname{logit} x_1)/(t_2 - t_1)$, Eq. (25.4); $t_{50} = \ln[(1 - x_0)/x_0]/r$.
- Delay due to vertical resistance $\Delta t \approx \ln k/r$, Eq. (25.5); monocyclic disease $x = 1 - \mathrm{e}^{-r_{\mathrm{M}}t}$.

## Questions

1. Why can PTI explain the resistance of most plants to most microbes, while ETI mainly explains the resistance of cultivars to pathogen races? What would happen to a plant with PTI but no NLRs at all?

   **Answer** PRRs recognize molecules (flagellin, chitin and so on) that are shared by a large group of microbes and hard to change, so they act against all microbes that have not adapted to the host, constituting nonhost resistance and basal resistance; only the few pathogens that have evolved a full set of effector proteins suppressing PTI can cause disease on that host. NLRs recognize specific effector proteins, which are present or absent, or altered, between pathogen races, so NLR-mediated resistance appears as specificity between cultivars and races, that is, the gene-for-gene relationship. A plant with only PTI would remain resistant to nonadapted microbes but completely susceptible to pathogens adapted to it (which can suppress PTI with effectors), being in the ETS phase of the zigzag model; and because ETI can also potentiate PTI (Section 25.4.7), its basal resistance would also be weaker than that of a normal plant.

2. (Calculation) On a susceptible wheat cultivar, the severity of stripe rust is 0.5% on May 1 and 30% on May 15. (a) Estimate the apparent infection rate $r$. (b) A cultivar carrying a new *R* gene leaves only 1/1000 of the effective initial inoculum in the field (assume a small number of virulent races able to overcome it already exist, and $r$ is unchanged); by how many days is the time to reach 30% severity delayed? (c) A horizontally resistant cultivar lowers $r$ by 40%; with the same initial severity, how many days does it take to increase from 0.5% to 30%?

   **Answer** (a) $\operatorname{logit}(0.005) = \ln(0.005/0.995) = -5.293$ and $\operatorname{logit}(0.30) = \ln(0.3/0.7) = -0.847$, so $r = (5.293 - 0.847)/14 = 0.318\,\mathrm{d^{-1}}$. (b) The initial severity is very low, so by Eq. (25.5), $\Delta t \approx \ln 1000/0.318 = 6.908/0.318 = 21.7\,\mathrm{d}$, a delay of about three weeks. (Exact calculation: the severity of the new cultivar on May 1 is $x_0' \approx 5\times10^{-6}$, $\operatorname{logit} x_0' = -12.206$, and reaching a logit of −0.847 takes $11.36/0.318 = 35.7\,\mathrm{d}$, which is 21.7 d later than the original 14 d.) (c) $r = 0.6 \times 0.318 = 0.191\,\mathrm{d^{-1}}$, and the time required is $4.446/0.191 = 23.3\,\mathrm{d}$, about 9 days more than for the susceptible cultivar. Both kinds of resistance delay the epidemic; the effect of vertical resistance is larger when virulent races are rare but is quickly lost once virulent races increase, whereas the effect of horizontal resistance is independent of race composition.

3. Explain with the gene-for-gene model why, a few years after a wheat cultivar carrying *R1* is released, the frequency of *avr1* (not recognized by *R1*) in the field rust population rises rapidly. Why are NLRs that recognize "core effector proteins," or that use indirect recognition, often more durable?

   **Answer** In fields where the *R1* cultivar is grown over large areas, strains carrying *Avr1* cannot infect, while strains that have mutated or lost *Avr1* can multiply; selection is very strong, the frequency of *avr1* rises in a logistic fashion, and resistance is "lost" accordingly. If the recognized effector is a core effector required for pathogenicity, losing or greatly changing it markedly reduces the virulence of the pathogen, the cost of escaping recognition is high, and selection is much weaker. Indirect recognition monitors the modification of host targets by effectors (such as phosphorylation or cleavage of RIN4); to escape, the pathogen must give up its action on this target, that is, this part of its virulence, and cannot simply change the surface of the effector; moreover, a guardee may be modified by several effectors, so the pathogen would need to change several genes at once. Both kinds of recognition therefore make "escape" harder and resistance more durable.

4. A hemibiotrophic pathogen induces the salicylic acid pathway early in infection and later secretes large amounts of necrosis-inducing toxins. Based on SA–JA antagonism, predict: (a) what effects does exogenous methyl jasmonate have on this disease in the early and late phases? (b) How would the pathogen's secretion of coronatine change the course of early infection?

   **Answer** (a) Early in infection the pathogen lives biotrophically, and salicylic acid-dependent defenses (the hypersensitive response, PR proteins) are the effective ones; exogenous methyl jasmonate would suppress the salicylic acid pathway through antagonism and might make early infection easier to establish. Later the pathogen becomes necrotrophic, and jasmonate/ethylene-dependent defenses (defensins, secondary metabolites) are more effective against it, whereas salicylic acid-induced cell death in fact benefits it; raising jasmonate at this stage might reduce disease. The same treatment may therefore have opposite effects at different stages. (b) Coronatine mimics JA-Ile, activates jasmonate signaling, suppresses the salicylic acid defense that should be acting early, and also reopens stomata closed by flg22, so that the pathogen enters in greater numbers through the leaf surface and multiplies faster early; the biotrophic phase is prolonged, and the later necrosis comes earlier and is more severe.

5. How would a tobacco plant transformed with the *P19* gene (a silencing suppressor of tomato bushy stunt virus) respond, respectively, to TMV and to a mild strain of an RNA virus? Why is P19 often coexpressed in transient expression experiments in *N. benthamiana*?

   **Answer** P19 binds 21 nt siRNA duplexes so that they cannot be loaded onto AGO proteins, thereby suppressing RNA silencing. In plants transformed with P19, antiviral RNA silencing is weakened, RNA viruses (including mild strains) replicate and spread faster and cause more severe symptoms, and the cross-protection provided by mild strains (partly dependent on sequence-specific silencing) would also weaken. For tobacco carrying the *N* gene, resistance to TMV is determined mainly by ETI and the hypersensitive response caused by N (a TNL) recognizing the viral helicase and signaling through NRG1; P19 generally does not abolish this resistance but may let the virus spread somewhat farther before the hypersensitive response occurs. In transient expression experiments, the transcript of the introduced foreign gene accumulates in large amounts and triggers post-transcriptional gene silencing in the host, so that expression falls rapidly; coexpressing P19 suppresses this silencing, so that the target protein is expressed at higher levels for longer.
