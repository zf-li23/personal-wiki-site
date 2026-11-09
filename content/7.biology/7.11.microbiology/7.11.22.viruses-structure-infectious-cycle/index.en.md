---
title: "Viruses: Nature, Structure and the Infectious Cycle"
description: "What a virus is: the extracellular virion and the intracellular replicating state, the range of sizes and genomes, and how viruses differ from cells. The experiments that identified viral genetic material (Hershey–Chase; the reconstitution of tobacco mosaic virus). The Baltimore classification of the seven routes to mRNA and the current ICTV taxonomy. Virion architecture: capsids and capsomeres, helical and icosahedral symmetry, the triangulation number, complex and enveloped particles, and the enzymes carried in virions. The infectious cycle: attachment, entry and uncoating, genome replication and expression, assembly, release and maturation, and the outcomes of infection. Methods: host cells, tissue culture and organoids, cytopathic effect, the plaque assay and titers, TCID50 by Reed–Muench and Spearman–Kärber, particle counts and genome copies, the particle-to-PFU ratio, multiplicity of infection and the Poisson distribution, and the one-step growth curve."
---

Every chapter so far has described organisms that grow: they take up nutrients, make more of their own substance and divide. This chapter turns to entities that do none of these things. A virus has no metabolism, no ribosomes and no means of increasing in size; outside a cell it is an inert particle that can be crystallized like a protein. Inside a suitable cell it is something else entirely — a set of instructions that redirects the cell's biosynthesis to make more copies of itself. Viruses are nevertheless the most numerous biological entities on the planet, they infect members of all three domains, they kill a large fraction of the microbial biomass of the ocean every day, and they have supplied molecular biology with most of its early tools and concepts.

This chapter establishes the general principles: what a virus is and what it is made of, how virus genomes are classified by the way they reach mRNA, the architecture of the particle, the steps of the infectious cycle common to all viruses, and — because virology is above all a quantitative science — how viruses are grown, detected and counted. Bacteriophages, which supply most of the quantitative methods, follow in [7.11.23](/7.11.23); the molecular detail of genome replication and expression in [7.11.24](/7.11.24) and [7.11.25](/7.11.25); the diversity of viruses and the subviral agents in [7.11.26](/7.11.26); the host side of the interaction in [7.11.27](/7.11.27); drugs and vaccines in [7.11.28](/7.11.28). The definition of a **virus** and its place among the forms of life were given in [7.3.1](/7.3.1#sec-1.5), and the competing hypotheses for the origin of viruses in [7.10.27](/7.10.27#sec-27.7); neither is repeated here. The physics of capsid symmetry and assembly belongs to [7.6.7](/7.6.7#sec-7.5) and [7.6.29](/7.6.29#sec-29.1), and is used rather than derived.

## 22.1. What a Virus Is

### 22.1.1. Two States

A virus exists in two states, and most confusion about what viruses "are" comes from failing to distinguish them.

The extracellular state is the **virion**: a nucleic acid genome packaged in a protein shell, with or without a membrane, metabolically inert, structurally stable and incapable of change. Its functions are to protect the genome outside the cell, to recognize the next host cell and to deliver the genome into it. The intracellular state is not a particle at all. After entry, the capsid is shed, and what exists in the cell is a replicating nucleic acid together with the viral proteins it directs the cell to make; at this stage nothing recognizable as a virus can be recovered. The virus is, in Luria's phrase, a genetic element that alternates between an inert vehicle and an intracellular genetic program.

**Definition 22.1.1 (Capsid)** The **capsid** is the protein shell that encloses a viral genome. It is built from many copies of one or a few polypeptides, assembled into morphological units, the **capsomeres**, arranged with helical or icosahedral symmetry. The capsid together with the genome it contains is the **nucleocapsid**.

This two-state life gives the formal definition its two halves: viruses are *obligate intracellular parasites*, dependent on the host for energy, precursors, ribosomes and most enzymes, and they are *genetic elements*, with their own genome and their own evolutionary history.

### 22.1.2. Sizes and Genomes

Most virions are between $20$ and $300\,\mathrm{nm}$ across, below the resolution of the light microscope. Poliovirus, at $30\,\mathrm{nm}$, is the size of a ribosome; the vaccinia virion, about $350 \times 270\,\mathrm{nm}$, is the size of the smallest bacterial cells and was visible to nineteenth-century microscopists as "elementary bodies". The record holders dissolve the size criterion altogether: *Mimivirus* has an icosahedral capsid of $500\,\mathrm{nm}$ with fibers that bring the particle to $750\,\mathrm{nm}$, and the ovoid *Pandoravirus* particle is $1\,\mu\mathrm{m}$ long, larger than the cells of *Mycoplasma genitalium* ([7.11.26](/7.11.26)).

Genomes span an even wider range, from about $1.7\,\mathrm{kb}$ (circoviruses, two genes) and $3.6\,\mathrm{kb}$ for the RNA phage MS2 to $1.2\,\mathrm{Mb}$ in *Megavirus* and $2.5\,\mathrm{Mb}$ in *Pandoravirus salinus* — more than ten times the genome of the smallest cellular endosymbionts ([7.11.13](/7.11.13#sec-13.1.2)). RNA genomes are confined to the lower end, the largest being those of the nidoviruses, which encode a proofreading exonuclease ($32\,\mathrm{kb}$ in the coronaviruses, $41\,\mathrm{kb}$ in a nidovirus of planarians), because replication without proofreading cannot maintain a longer sequence ([7.6.41](/7.6.41), [7.11.25](/7.11.25)). Within these ranges the genome may be DNA or RNA, single- or double-stranded, linear or circular, one molecule or several (a *segmented* genome, as in influenza virus with eight segments or the reoviruses with ten to twelve).

The small genome is the central constraint on viral design. A particle must be built from a protein that the genome can afford to encode, which forces the repeated use of identical subunits and hence symmetry ([7.6.7](/7.6.7#sec-7.4)); a genome of a few kilobases cannot encode a replication apparatus and must borrow the cell's; and the same sequence is often read in more than one frame or processed into several products to squeeze more protein out of less nucleic acid.

### 22.1.3. How a Virus Differs from a Cell

Four differences are decisive, and each is more informative than the question of whether viruses are alive.

1. *One kind of nucleic acid.* A cell contains both DNA and RNA; a virion contains one genome of one chemical type. (Retroviruses and hepadnaviruses use both DNA and RNA, but at different stages, never in the same particle.)
2. *No ribosomes and no energy metabolism.* No virus encodes a complete ribosome; all viral proteins are made by host ribosomes, with host tRNAs and host ATP. Giant viruses encode translation factors and aminoacyl-tRNA synthetases, but still no ribosome.
3. *No growth and no binary fission.* A virion does not enlarge and does not divide. The genome is replicated and the components are synthesized separately, and particles are then assembled from a pool — a mode of multiplication by assembly rather than by division.
4. *Dependence that is absolute.* A cell deprived of a nutrient can often make it; a virus deprived of its host does nothing at all.

The practical consequences dominate the rest of this chapter: a virus can only be grown in cells, and it can only be counted by what it does to cells.

## 22.2. The Genetic Material of Viruses

### 22.2.1. DNA: the Hershey–Chase Experiment

By 1950 the transforming principle of pneumococcus had been shown to be DNA ([7.2.1](/7.2.1), [7.4.10](/7.4.10#sec-10.3)), but many still held that protein carried genetic information. Alfred Hershey and Martha Chase settled the question in 1952 with phage T2, using the natural separation of a phage infection: the particle attaches outside the cell and sends only part of itself in.

They grew phage separately in medium containing $^{35}\mathrm{S}$, which labels protein but not nucleic acid, and in $^{32}\mathrm{P}$, which labels nucleic acid but not protein. Labeled phage was adsorbed to *Escherichia coli*, and the empty particles were sheared from the cell surface in a kitchen blender and separated by centrifugation. Most of the $^{32}\mathrm{P}$ was found with the cells and passed to the progeny phage; most of the $^{35}\mathrm{S}$ stayed in the supernatant with the empty coats and did not. The genetic material that enters the cell and directs the production of several hundred complete new particles is DNA.

The experiment is also the model for a style of argument used throughout virology: separate the components of the particle, follow each one, and ask which is sufficient to produce progeny.

### 22.2.2. RNA: the Reconstitution of Tobacco Mosaic Virus

That genetic information can be carried by RNA was established at almost the same time with the first virus ever described. Tobacco mosaic virus (TMV) can be dissociated into its RNA and its single species of coat protein, and the two will reassemble spontaneously into rods indistinguishable from the original. Heinz Fraenkel-Conrat and Robley Williams (1955) reassembled infectious particles from the separated components, and Fraenkel-Conrat and Beatrice Singer (1957) reconstituted particles from the protein of one TMV strain and the RNA of another and showed that the progeny — their symptoms, and the coat protein of the new virions — followed the strain that donated the RNA. Gierer and Schramm, in the following year, showed that the naked RNA is itself infectious.

The reconstitution experiment made a second point that mattered for structural biology: all the information needed to build the particle is contained in the sequences of its components, so assembly is spontaneous **self-assembly** ([7.6.29](/7.6.29#sec-29.1)) and needs no template and no external energy input.

### 22.2.3. The Central Dogma, and Where Viruses Extend It

Crick's statement of information flow, $\text{DNA} \to \text{RNA} \to \text{protein}$, describes cells completely. Viruses use every transfer the chemistry allows: RNA replicated from RNA by a virus-encoded **RNA-dependent RNA polymerase**, an enzyme no cell possesses for this purpose; DNA synthesized from RNA by **reverse transcriptase** (Temin and Baltimore, 1970), which overturned the belief that the DNA → RNA step is irreversible ([7.2.1](/7.2.1#sec-1.1)); and in the hepadnaviruses, a DNA genome that is transcribed into an RNA intermediate and then copied back into DNA. What no virus does is the transfer that is chemically impossible: protein back to nucleic acid.

Because the genome is the complete specification, cloned viral DNA can be used to recover infectious virus. The cloned cDNA of poliovirus is infectious when introduced into cells (Racaniello and Baltimore, 1981), and the same principle, generalized as **reverse genetics**, allows influenza virus to be rebuilt from eight plasmids and the 1918 pandemic strain to be reconstructed from sequences recovered from preserved tissue. Infectious clones are the standard tool of molecular virology ([7.11.24](/7.11.24), [7.11.25](/7.11.25)) and the reason that virology is also a biosafety discipline ([7.11.35](/7.11.35)).

## 22.3. Classification

### 22.3.1. The Baltimore System

Every virus faces one invariable requirement: at some point its genome must be converted into mRNA that host ribosomes can translate, and mRNA is by convention the plus $(+)$ strand. The steps needed to get there depend only on the chemistry and polarity of the genome, so grouping genomes by their route to mRNA groups viruses by their replication strategy. David Baltimore proposed this scheme in 1971.

**Definition 22.3.1 (Baltimore Classification)** The **Baltimore classification** assigns a virus to one of seven classes according to the nature of its genome (DNA or RNA, double- or single-stranded) and the pathway by which that genome gives rise to mRNA. A single-stranded genome with the sequence of mRNA defines a **positive-strand RNA virus** (class IV); one complementary to mRNA defines a **negative-strand RNA virus** (class V).

![The Baltimore classification: the seven routes from a viral genome to mRNA. One row per class. On the left is the genome carried in the virion, drawn as one line for a single strand and two for a duplex, in blue for DNA and orange for RNA, with the polarity marked (+ is the sense of mRNA); arrows give the syntheses required, with the enzyme responsible named above each — host RNA polymerase, host DNA polymerase, a virus-encoded RNA-dependent RNA polymerase (RdRp) or reverse transcriptase — and any intermediate drawn where it is made. Every route ends at the mRNA column. The next column says whether the virion must carry its own polymerase, which it must whenever no host enzyme can copy the genome (classes III, V, VI and VII); class IV needs none, because its genome is itself mRNA. The examples name a bacterial, a plant and an animal virus for each class where one exists, and the last column states the point of the strategy. In class VII the mRNA also serves as the pregenome that is reverse-transcribed back into the DNA genome.](./plots/baltimore.py)

The seven classes, with the point of each strategy:

| Class | Genome | Route to mRNA | Enzyme in the virion | Examples |
|---|---|---|---|---|
| I | dsDNA | Transcription of the minus strand | No | Phage T4 and λ, herpesviruses, adenoviruses, poxviruses (which do carry a polymerase, being cytoplasmic) |
| II | ssDNA | Synthesis of the complementary strand, then transcription | No | Phage φX174 and M13, parvoviruses, circoviruses |
| III | dsRNA | Transcription inside the particle | Yes (RdRp) | Reoviruses, rotaviruses, phage φ6 |
| IV | $(+)$ssRNA | The genome is mRNA | No | Phage MS2 and Qβ, poliovirus, coronaviruses, TMV |
| V | $(-)$ssRNA | Transcription by the packaged polymerase | Yes (RdRp) | Influenza, measles, rabies, Ebola viruses |
| VI | $(+)$ssRNA with a DNA intermediate | Reverse transcription, integration, transcription | Yes (RT) | HIV and other retroviruses |
| VII | dsDNA with an RNA intermediate | Transcription, then reverse transcription | Yes (RT) | Hepatitis B virus, cauliflower mosaic virus |

Three consequences follow immediately and are worth stating before any detail.

- *A genome that is not mRNA must be copied before anything can happen.* Classes III, V and VI therefore cannot start an infection with naked nucleic acid: the virion must deliver its polymerase along with the genome, and their purified genomes are not infectious. Class IV genomes are infectious on their own, which is why poliovirus RNA transfected into cells yields virus.
- *The place of replication follows from the enzyme required.* Viruses that use host RNA polymerase II or host DNA polymerase must replicate in the nucleus (classes I, II, VI, VII, with the poxviruses as the famous cytoplasmic exception, carrying their own transcription machinery); viruses with their own RdRp are free to stay in the cytoplasm (classes III, IV, V, with influenza virus as the counter-exception, transcribing in the nucleus because it steals capped primers from host transcripts).
- *The classes predict the drug targets.* An enzyme the host does not possess — RdRp, reverse transcriptase, integrase, viral protease — is a selective target, which is why antiviral chemotherapy is organized along the same lines ([7.11.28](/7.11.28)).

### 22.3.2. Taxonomy

The Baltimore classes are a functional grouping, not a taxonomy: they say nothing about ancestry, and viruses in one class can be unrelated. Formal classification is the business of the International Committee on Taxonomy of Viruses (ICTV), which maintains a fifteen-rank hierarchy from realm down to species. The six realms recognized at present are defined by deep structural and enzymatic homologies that survive where sequence similarity has long since decayed: *Riboviria* (all RNA viruses and the reverse-transcribing viruses, united by the RdRp or RT fold), *Duplodnaviria* (tailed phages and herpesviruses, united by the HK97 capsid fold and a terminase), *Varidnaviria* (the double-jelly-roll capsid lineage, including adenoviruses and the giant viruses), *Monodnaviria* (the rolling-circle replication-initiator lineage of small DNA viruses), *Adnaviria* (filamentous archaeal viruses with A-form DNA) and *Ribozyviria* (hepatitis delta-like agents). Species have binomial names (genus plus epithet), a rule adopted in 2021 and applied throughout the taxonomy from 2023; the species containing the virus SARS-CoV-2, long called *Severe acute respiratory syndrome-related coronavirus*, is now *Betacoronavirus pandemicum*.

Two older schemes still appear in the literature and should not be carried forward.

- *Classification by host.* Calling viruses "bacterial", "plant" or "animal" viruses describes their ecology, not their relationships: the tailed phages are the closest relatives of the herpesviruses, not of the plant viruses. The terms remain useful informally, and the word *bacteriophage* is irreplaceable.
- *Classification by morphology.* The tailed-phage families *Myoviridae*, *Siphoviridae* and *Podoviridae*, defined by contractile, long non-contractile and short tails, were abolished in 2022 because genome sequences showed each to be polyphyletic; tail morphology evolves repeatedly. The tailed phages are now the class *Caudoviricetes*, and the words *myovirus*, *siphovirus* and *podovirus* survive only as morphological descriptions, which is how they are used here and in [7.11.23](/7.11.23).

## 22.4. The Architecture of the Virion

![Virion architecture. A: helical symmetry, tobacco mosaic virus — 2130 identical subunits wound in a helix of 16⅓ subunits per turn around a single (+) RNA of 6395 nucleotides, three nucleotides per subunit, giving a rigid rod 300 nm long, 18 nm wide, with a hollow 4 nm core; the length of the rod is set by the length of the RNA. B: icosahedral symmetry — a shell of 20 triangular faces and 12 fivefold vertices; the subunits cluster into capsomeres, 12 pentamers and 10(T − 1) hexamers for triangulation number T, with 60T subunits in all (Caspar and Klug; the geometry is derived in [7.6.7](/7.6.7#sec-7.5)). Shells are drawn for T = 1 (φX174-like, 60 subunits), T = 3 (poliovirus-like, 180), T = 4 (hepatitis B-like, 240) and T = 7 (phage HK97, 420); pentamers are marked in a darker tone. C: a complex virion, phage T4 — a prolate icosahedral head (T = 13 laevo in the cap, elongated by an extra equatorial band), a contractile tail with a sheath around a central tube, a baseplate, six long and six short tail fibers. D: an enveloped virion, influenza A — a host-derived lipid bilayer carrying the trimeric hemagglutinin and the tetrameric neuraminidase, the M2 ion channel and a layer of M1 beneath it, enclosing eight helical ribonucleoprotein segments, each with its own polymerase. All four are drawn to the same scale except C and D, which are enlarged as marked.](./plots/virion-architecture.py)

### 22.4.1. Symmetry and Self-Assembly

Crick and Watson pointed out in 1956 that a small genome cannot encode a large shell protein, so a capsid must be built from many copies of a small one; and identical subunits bonding identically to their neighbors necessarily produce a symmetric structure ([7.6.7](/7.6.7#sec-7.4.2)). Two symmetries close a shell around a genome.

In **helical symmetry** the subunits are arranged in a helix around the nucleic acid, which runs in a groove between successive subunits. The diameter is set by the subunit, the length by the genome — the defining property of a helical nucleocapsid, demonstrated by TMV, whose rods are uniformly $300\,\mathrm{nm}$ long because its RNA is 6395 nucleotides long. Rigid helical rods occur among plant viruses; in animal viruses (rabies, measles, Ebola, influenza) the helical nucleocapsid is flexible and is coiled inside an envelope.

**Definition 22.4.1 (Icosahedral Symmetry)** A capsid has **icosahedral symmetry** when its subunits are arranged with the rotational symmetry of an icosahedron: twenty triangular faces, twelve vertices, and axes of five-, three- and twofold rotation, giving 60 equivalent positions. It is the arrangement that encloses the largest volume with the smallest number of subunit types, and it gives the virion its roughly spherical appearance.

Sixty subunits enclose too little space for most genomes. Caspar and Klug (1962) showed that larger shells keep icosahedral symmetry if subunits occupy *quasi-equivalent* environments, grouped into twelve pentamers at the vertices and $10(T-1)$ hexamers elsewhere, where the **triangulation number** $T = h^2 + hk + k^2$ counts the lattice triangles per face; the shell then contains $60T$ subunits ([Theorem 7.5.2](/7.6.7#thm-7.5.2)). Poliovirus is a pseudo-$T{=}3$ particle with 60 copies each of VP1, VP2 and VP3; hepatitis B capsids are $T{=}4$; phage HK97 is $T{=}7$ and the herpesvirus capsid $T{=}16$; the adenovirus capsid is $T{=}25$; the capsid of *Mimivirus* has an estimated $T$ of about a thousand. Large capsids are not simply bigger: they need scaffolding proteins, a unique portal vertex for DNA entry, and often a maturation protease, and they assemble through a metastable procapsid that expands when filled ([7.6.29](/7.6.29#sec-29.1.3), and phage T4 in [7.11.23](/7.11.23#sec-23.4.5)).

Not all particles are purely helical or icosahedral. *Complex* virions combine both, the head-and-tail phages being the standard example: an icosahedral head joined through a portal to a helical tail. The poxviruses are brick-shaped with an internal biconcave core, and the pandoraviruses are ovoid with no symmetry at all.

### 22.4.2. The Envelope

**Definition 22.4.2 (Viral Envelope)** The **viral envelope** is a lipid bilayer, acquired from a host membrane when the virion buds, in which virus-encoded glycoproteins are embedded. A virion that has one is *enveloped*; one that has none is *naked* or *non-enveloped*.

The lipids come from the host (the plasma membrane for influenza and HIV, the ER or Golgi for coronaviruses and flaviviruses, the inner nuclear membrane for herpesviruses) but the proteins are viral. Envelope glycoproteins perform the two most specific steps of infection: attachment to the receptor and fusion of the two membranes. Many are made as a precursor that must be cleaved by a host protease to become fusion-competent — influenza hemagglutinin by tryptase or, in highly pathogenic avian strains with a polybasic cleavage site, by the ubiquitous furin, a difference that broadens tissue tropism and underlies much of their virulence.

The envelope dictates the stability of the particle outside the host. Enveloped viruses are inactivated by drying, detergents, alcohols and lipid solvents and generally require close contact or droplets for transmission; naked viruses (enteroviruses, noroviruses, adenoviruses) survive on surfaces, in water and in the gut, resist bile salts and detergents, and transmit by the fecal–oral route ([7.11.35](/7.11.35)). Hand disinfection with alcohol works far better against influenza virus than against norovirus for this reason ([7.11.10](/7.11.10)).

### 22.4.3. Enzymes and Other Cargo

A virion is not only a container. It carries whatever the first minutes of infection require and the cell cannot supply.

- *Polymerases.* Classes III, V, VI and VII package the enzyme that copies their genome, as explained above.
- *Enzymes that open the way in.* Many tailed phages carry a lysozyme-like peptidoglycan hydrolase at the tail tip to make a local hole in the wall.
- *Enzymes that open the way out.* The neuraminidase of influenza virus cleaves sialic acid from host glycoproteins so that new virions do not stick to the cell they just left, and to the mucus that covers the airway.
- *Proteins that disarm the host.* Phage P1 carries the Dar proteins in its head and co-injects them with its DNA, where they mask the sites of host restriction enzymes ([7.11.23](/7.11.23#sec-23.8.3)); herpesviruses deliver VP16 and vhs in the tegument, which activate viral transcription and destroy host mRNA within minutes.
- *Host components.* Retroviral particles package host tRNA as the primer for reverse transcription, and enveloped virions often carry host membrane proteins picked up during budding.

## 22.5. The Infectious Cycle

![The infectious cycle. Left: a bacteriophage on a Gram-negative cell. 1, attachment of the tail fibers to a receptor in the outer membrane or lipopolysaccharide; 2, penetration — the tail tube crosses the envelope and the genome alone is injected, the capsid staying outside; 3, synthesis — the host's program is shut off and phage nucleic acid and protein are made in a timed sequence; 4, assembly of heads, tails and fibers and packaging of the genome; 5, release by lysis of the cell. Right: an enveloped animal virus. 1, attachment to a receptor, and in many cases to a second co-receptor; 2, entry, either by fusion of the envelope with the plasma membrane at neutral pH or by endocytosis followed by acid-triggered fusion with the endosomal membrane ([7.3.10](/7.3.10)); 3, uncoating and transport of the genome to its site of replication; 4, replication and expression, often in a membrane-bound replication compartment; 5, assembly, in which the nucleocapsid meets the viral glycoproteins at a membrane; 6, release by budding, which may leave the cell intact, and 7, maturation, in which a viral protease cleaves the precursor proteins of the released particle to give the infectious form. The eclipse period is marked on both: the interval during which no infectious particle exists, because the entering genome has left its capsid and new particles have not yet been assembled.](./plots/infectious-cycle.py)

The cycle has five steps in every virus and in every host. The differences between a phage, a plant virus and an animal virus lie in how each step is accomplished, not in whether it occurs.

### 22.5.1. Attachment

Infection begins with a collision, which is a matter of diffusion and concentration, followed by specific binding between a protein on the particle surface and a **receptor** on the cell. Receptors are normal cell components with normal jobs: the maltose porin LamB for phage λ, the vitamin $\mathrm{B}_{12}$ transporter BtuB for phage BF23, sialylated glycans for influenza virus, the complement regulator CD46 or the signaling molecule SLAM for measles virus, CD4 together with the chemokine receptor CCR5 or CXCR4 for HIV. Many animal viruses need an *attachment factor* first (heparan sulfate, lectins) and then a receptor that triggers entry; others need a co-receptor in sequence.

**Definition 22.5.1 (Host Range and Tropism)** The **host range** of a virus is the set of host species and strains it can productively infect; its **tissue tropism** is the set of cell types it infects within a host. Both are determined in the first instance by the distribution of the receptor, and beyond that by every later step: whether the cell provides the factors the genome needs, and whether its innate defenses allow replication.

A cell that supports the complete cycle is *permissive*; one that has the receptor but blocks a later step is *susceptible but non-permissive*. The distinction matters in practice: making a mouse cell express the human receptor often allows entry but not replication, and the search for what else is missing is a standard route to discovering host factors ([7.11.27](/7.11.27)).

Because attachment is the step most exposed to the outside, it is also the step at which resistance appears first. A bacterium that loses or alters a surface receptor becomes phage-resistant in a single mutation, at whatever cost the lost function entails ([7.11.23](/7.11.23#sec-23.8.1)).

### 22.5.2. Entry and Uncoating

Here the three kinds of host differ most, because their surfaces differ.

*Bacteria and archaea* are enclosed in a wall, so the particle stays outside and only the genome (with a few proteins) is delivered through it. Tailed phages have evolved elaborate injection machines for this ([7.11.23](/7.11.23#sec-23.4.2)).

*Plants* have a wall and no endocytosis, so plant viruses cannot enter on their own at all. They depend on mechanical wounding, on vectors that pierce the wall — aphids, leafhoppers, nematodes, fungi — or on inheritance through seed, and they then move from cell to cell through plasmodesmata with the help of virus-encoded movement proteins ([7.11.26](/7.11.26)).

*Animal cells* take in the whole particle. Enveloped viruses fuse their envelope with a cell membrane: either at the plasma membrane at neutral pH (HIV, paramyxoviruses) or after endocytosis, when the acidification of the endosome to $\mathrm{pH}\,5$–$6$ triggers an irreversible conformational change in the fusion protein (influenza virus, and many others; [7.3.10](/7.3.10)). Naked viruses have no membrane to fuse and instead breach one: poliovirus, on binding its receptor, externalizes the myristoylated VP4 and the amino terminus of VP1, which form a pore through which the RNA passes; adenovirus lyses the endosome outright. Low pH, receptor binding and proteolysis are the three common triggers, and all three ensure that the particle opens where it should and not before.

Uncoating delivers the genome to the compartment where it will be replicated, and for nuclear viruses it is a transport problem as well: the herpesvirus capsid travels along microtubules to the nuclear pore and injects its DNA through it, while the HIV capsid is now known to enter the nuclear pore nearly intact and uncoat inside the nucleus.

### 22.5.3. Replication and Expression

Once inside, the virus must do three things in the right order: make the proteins that create an environment for replication, replicate the genome, and make the structural proteins in the large amounts a particle requires. Nearly all viruses therefore express their genes in temporal classes — early genes for enzymes and host-shutoff functions, late genes for structural proteins — and the switch between them is a favorite subject of molecular biology ([7.11.23](/7.11.23#sec-23.4.3), [7.11.24](/7.11.24)).

Host shutoff is a common early function: T4 modifies the host RNA polymerase, poliovirus cleaves the translation initiation factor eIF4G so that only its own cap-independent IRES-driven translation continues, influenza virus steals the caps of host transcripts, and herpesvirus vhs degrades host mRNA. Replication is often localized in a visible structure — the viral factories of poxviruses and giant viruses, the double-membrane vesicles of coronaviruses — which concentrates the components and hides double-stranded RNA from the sensors of innate immunity ([7.11.27](/7.11.27)).

### 22.5.4. Assembly, Release and Maturation

Assembly is largely spontaneous, driven by the shape complementarity of the subunits; where it is not, the virus encodes scaffolding proteins or recruits host chaperones (the λ capsid protein requires the *E. coli* chaperonin GroEL/GroES). Simple RNA viruses co-assemble capsid and genome around a packaging signal. Large DNA viruses build an empty procapsid and pump the genome in with an ATP-driven motor against the pressure of the DNA already inside, one of the strongest molecular motors known ([7.6.28](/7.6.28#sec-28.5.4)).

Release takes three forms. *Lysis* kills the cell and liberates everything at once: phages do it with a timed enzymatic program ([7.11.23](/7.11.23#sec-23.6)), naked animal viruses by the accumulated damage of infection. *Budding* through a membrane wraps the nucleocapsid in an envelope as it leaves and need not kill the cell, so a budding virus can produce particles for hours or days — the basis of persistent infection. Exocytosis carries enveloped particles that bud into an internal compartment (coronaviruses, which leave through the lysosomal pathway) out in vesicles.

Many viruses are released in a non-infectious form and *mature* afterward, by proteolysis of the proteins of the particle: HIV protease cleaves the Gag polyprotein after budding, condensing the particle into the mature conical core, and picornaviruses cleave VP0 into VP2 and VP4 during encapsidation. Maturation is a one-way switch that prevents the particle from being infectious while it is still inside the cell that made it; it is also a drug target ([7.11.28](/7.11.28)).

### 22.5.5. The Outcomes of Infection

| Outcome | What happens | Examples |
|---|---|---|
| Lytic (acute, productive) | Rapid production of progeny; the cell dies | Phage T4; poliovirus; influenza virus |
| Persistent (chronic) | Continuous or episodic production, the cell survives | Hepatitis B and C viruses; arenaviruses; filamentous phage M13, which is extruded without lysis |
| Latent | The genome persists with little or no gene expression and can reactivate | Herpes simplex virus in sensory neurons; phage λ as a **prophage** ([7.2.11](/7.2.11#sec-11.5)) |
| Transforming | The cell survives, loses growth control and may become tumorigenic | HPV, Epstein–Barr virus, hepatitis B virus ([7.3.26](/7.3.26)) |
| Abortive | Entry and partial expression without progeny | Any virus in a non-permissive cell |

**Definition 22.5.2 (Cytopathic Effect)** The **cytopathic effect** (CPE) is the set of visible changes an infection produces in cultured cells: rounding and detachment, shrinkage or swelling, fusion into multinucleate syncytia, and inclusion bodies. Its pattern is characteristic of the virus and is the usual way an infection is recognized in culture.

Inclusion bodies are accumulations of viral components or of the structures where replication occurs: the cytoplasmic Negri bodies of rabies virus in neurons, long used as a diagnostic criterion, the intranuclear Cowdry bodies of herpesviruses, the polyhedral protein crystals in which baculoviruses embed their virions. On a plant leaf, the equivalent of CPE is the local lesion — a necrotic spot where the virus has killed a patch of cells, used by Holmes from 1929 as the first quantitative assay for a virus and still the standard for plant viruses, since the number of lesions is proportional to the inoculum.

## 22.6. Growing, Detecting and Counting Viruses

Virology became quantitative when it learned to count. Everything in the rest of the virology chapters — burst sizes, growth curves, mutation rates, drug efficacy, vaccine titers — rests on the assays of this section.

### 22.6.1. Host Systems

Bacterial and archaeal viruses are the easiest: a pure culture in broth, or a lawn on an agar plate, is all that is needed.

Animal viruses were for decades grown in whole animals or in embryonated hen's eggs, which are still used for influenza vaccine production. The decisive advance came in 1949, when John Enders, Thomas Weller and Frederick Robbins grew poliovirus in cultures of human embryonic skin, muscle and intestine — non-neural tissue, which showed that the virus was not strictly neurotropic and made it possible to produce it in quantity. Their method opened the way to the Salk and Sabin vaccines and to the isolation of most of the viruses known today, and brought them the 1954 Nobel Prize. Cell culture today uses primary cells, diploid cell strains with a finite lifespan and immortal **cell line**s, each with its own permissiveness; a virus that grows in no available line is, for most practical purposes, unstudiable, which is why hepatitis C virus had to be discovered by molecular cloning and why human noroviruses resisted culture for forty years.

Two recent systems narrow the gap between a cell line and a tissue. **Organoid**s ([7.3.3](/7.3.3)) — self-organizing three-dimensional cultures from stem cells — reproduce the differentiated cell types and the polarity of an epithelium, and have made it possible to grow noroviruses in intestinal organoids, to study hepatitis B virus in liver organoids and to show that SARS-CoV-2 and Zika virus infect specific cell types of airway and brain organoids. Air–liquid interface cultures of airway epithelium serve the same purpose for respiratory viruses.

### 22.6.2. Plaques and Titers

![Quantifying a virus. A: the plaque assay. A tenfold dilution series of the stock is plated, each dilution on a lawn of host cells (for a phage, in a thin top agar; for an animal virus, a confluent monolayer under an agar or methylcellulose overlay that keeps progeny local); each infectious particle starts a focus of infection that spreads to its neighbors and leaves a clear plaque. Only plates with 10–100 plaques are counted. With 17 plaques from 0.1 ml of the 10⁻⁶ dilution, the titer is 17 × 10 × 10⁶ = 1.7 × 10⁸ PFU/ml. B: the dose–response curve. One-hit kinetics (one particle suffices) give a straight line through the origin, so plaque number is proportional to dose; a virus whose infectivity requires two different particles (some bipartite plant viruses) gives a parabola. C: the end-point dilution assay and the 50 % end point. Ten wells per dilution are scored for cytopathic effect; the fraction positive falls from 1 to 0 over two or three dilutions. The Reed–Muench interpolation and the Spearman–Kärber estimator applied to the same data give log TCID50 = −4.84 and −4.90, that is about 10⁴.⁹ TCID50 per 0.1 ml. D: the particle-to-PFU ratio for representative viruses (data from Flint et al., 2015), on a logarithmic scale: close to 1 for many phages, 10–100 for many animal viruses, 10⁴ for papillomavirus. The excess is not mostly defective particles but failure to complete a cycle that has many steps.](./plots/quantification.py)

**Definition 22.6.1 (Plaque)** A **plaque** is a visible clearing in a layer of host cells, produced when one infectious particle infects one cell and its progeny spread to the neighboring cells while diffusion is restricted by an overlay. The number of infectious units in a sample, measured by counting plaques, is its titer, expressed in **plaque-forming unit**s per milliliter (PFU/ml).

$$
\text{titer (PFU/ml)} = \frac{\text{number of plaques}}{\text{volume plated (ml)}} \times \frac{1}{\text{dilution}} . \tag{22.1}
$$

The plaque assay was devised for phages by d'Hérelle in 1917 and transferred to animal viruses by Dulbecco in 1952, and it did for virology what colony counting did for bacteriology: it made a virus suspension a countable population and allowed clonal stocks to be prepared by picking a plaque. A plaque is a clone, since it descends from a single particle; "plaque purification", repeated two or three times, is how pure virus stocks are made.

Three properties of the assay must be kept in mind.

- *The dose–response curve is linear.* Doubling the inoculum doubles the plaques, which shows that one particle is enough to start an infection (*one-hit kinetics*). A quadratic curve means that two complementing particles are required, as for the bipartite genomes of some plant viruses.
- *Plating efficiency is below one, often far below.* The titer is reported in plaque-forming units, not in particles, because the fraction of particles that succeed depends on the host cell, the medium and the handling. Plating efficiencies above $50\,\%$ are common for phages, $0.1$–$1\,\%$ is not unusual for animal viruses.
- *Plaque morphology is a phenotype.* Plaque size and turbidity report on burst size, lysis timing and the lytic–lysogenic decision, and mutants were historically isolated by their plaques — the *rII* mutants of T4 that founded fine-structure genetics are named after their plaque type ([7.4.10](/7.4.10#sec-10.6)).

Variants extend the method to viruses that do not lyse: the *fluorescent focus assay* stains infected cells with an antibody or detects a fluorescent reporter and counts foci; the *infectious center assay* plates infected cells rather than free virus and measures what fraction of a population is infected; the *transformation assay* counts foci of transformed cells for retroviruses such as Rous sarcoma virus.

### 22.6.3. End-Point Dilution: the TCID50

Some viruses kill cells without producing discrete plaques, or are assayed in eggs or animals. The end-point dilution assay replaces counting by a yes/no score on replicate test units.

**Definition 22.6.2 (TCID50)** The **TCID50** (median tissue culture infectious dose) is the amount of virus that infects $50\,\%$ of inoculated replicate cultures. The corresponding end points in animals are the $\mathrm{LD}_{50}$ (median lethal dose) and in general the $\mathrm{ID}_{50}$ (median infectious dose).

The $50\,\%$ point is used because it is the steepest and therefore best-determined part of the dose–response curve; it rarely falls on a dilution actually tested, so it is interpolated. Two estimators are standard. The Reed–Muench method pools the results cumulatively and interpolates linearly in the logarithm of the dilution,

$$
\text{proportionate distance} = \frac{(\%\ \text{positive above } 50) - 50}{(\%\ \text{positive above } 50) - (\%\ \text{positive below } 50)} , \tag{22.2}
$$

the logarithm of the end point being that of the dilution above $50\,\%$ minus the proportionate distance times the log dilution step. The Spearman–Kärber estimator uses all the dilutions instead of two and is the better statistical procedure (it is the mean of the tolerance distribution, with a known variance):

$$
\log_{10} \text{TCID}_{50} = x_0 + \frac{d}{2} - d\sum_i p_i , \tag{22.3}
$$

where $x_0$ is the logarithm of the highest concentration tested (the lowest dilution), $d$ the logarithm of the dilution step and $p_i$ the fraction of positive wells at dilution $i$, summed from $x_0$ downward, with $p = 1$ at the top and $p = 0$ at the bottom of the series. The two methods normally agree to within a few hundredths of a logarithm, as in panel C of the figure.

Because a well is scored positive if it receives at least one infectious unit, the two scales are related through the Poisson distribution of Section 22.6.5: $50\,\%$ of wells are negative when the mean dose is $m = -\ln 0.5 = 0.69$ infectious units, so one TCID50 corresponds to about $0.7\,\mathrm{PFU}$, and

$$
\text{PFU/ml} \approx 0.7 \times \text{TCID}_{50}/\mathrm{ml} . \tag{22.4}
$$

### 22.6.4. Counting Particles and Genomes

Infectivity assays measure what the virus can do; physical assays measure how much of it there is, and the two are not the same number.

Particle numbers are measured in the electron microscope against a known concentration of latex beads, by nanoparticle tracking, or by flow cytometry of stained particles in environmental samples. *Hemagglutination* exploits the ability of influenza, adenoviruses and paramyxoviruses to cross-link red blood cells into a lattice: the highest dilution that still prevents the cells from settling into a button gives the titer in hemagglutination units, a crude but fast measure of particle number, and in the hemagglutination inhibition test it is the standard serological assay for influenza. Viral proteins can be quantified immunologically, as in the p24 ELISA for HIV. Genome copies are counted by quantitative PCR or RT-PCR against a standard curve, now the commonest measurement of all.

**Formula 22.6.1 (Particle-to-PFU Ratio)** The ratio of the number of physical particles to the number of plaque-forming units measures the inefficiency of infection. It is near 1 for many bacteriophages but ranges from about 10 to $10^4$ for animal viruses: $20$–$50$ for influenza virus, $50$–$200$ for herpes simplex virus, $30$–$1000$ for poliovirus, about $10^4$ for papillomavirus.

A high ratio does not mean that most particles are defective, although some are (damaged, empty, or carrying lethal mutations). Mainly it means that the cycle has many steps and that failure at any one of them aborts the infection; since the dose–response curve is nevertheless linear, each particle that does succeed acted alone.

The practical consequence is the most important sentence of this section: *a genome copy is not an infectious virus*. RNA of SARS-CoV-2, measles virus or poliovirus is routinely detected by PCR for days or weeks after infectious virus has disappeared, because naked or encapsidated nucleic acid persists in tissue and in secretions. Diagnosis, infection control and the end of isolation cannot be decided on a PCR cycle threshold alone ([7.11.35](/7.11.35)); the question "how much virus is in this sample?" always requires the counter-question "measured how?".

### 22.6.5. Multiplicity of Infection

![Multiplicity of infection and the one-step growth curve. A: the distribution of virus particles among cells at a given multiplicity is Poisson. Bars give P(k) for MOI m = 0.1, 1 and 5; at m = 1, 37 % of cells receive nothing and 26 % receive two or more, so "one particle per cell" never means one particle in every cell. B: the fractions of cells receiving none, exactly one and more than one particle as functions of m; the fraction infected is 1 − e^(−m), which reaches 99 % only at m = 4.6. Low MOI (≪ 1) gives single infections and allows several cycles of spread; high MOI (≫ 1) infects every cell synchronously, which is what a one-step experiment requires. C: the one-step growth curve. All cells are infected at once at t = 0 and the culture is diluted so that released virus cannot start a second cycle. Infectious particles assayed in the whole culture (solid) stay at the input level while the entering genomes are uncoated and copied — the eclipse period — then rise as particles are assembled inside the cells; free virus in the medium (dashed) rises only after lysis, at the end of the latent period, and reaches a plateau. The ratio of the plateau to the input number of infected cells is the burst size, here 100. The dotted curve is what an experiment on an enveloped virus released by budding would show: no intracellular pool accumulates, and the curve rises gradually with no sharp step.](./plots/moi-growth.py)

**Definition 22.6.3 (Multiplicity of Infection)** The **multiplicity of infection** (MOI) is the ratio of infectious particles added to cells present in a culture. Since particles and cells meet by random collision, the number $k$ of particles entering a given cell follows the Poisson distribution with mean $m$ equal to the MOI:

$$
\mathbb{P}(k) = \frac{m^k \mathrm{e}^{-m}}{k!} . \tag{22.5}
$$

Three consequences are used constantly. The fraction of cells that escape infection is $\mathbb{P}(0) = \mathrm{e}^{-m}$, so the fraction infected is $1 - \mathrm{e}^{-m}$; infecting $99\,\%$ of the cells requires $m = -\ln 0.01 = 4.6$, not $m = 1$. Conversely, $m$ can be measured from the observed fraction of uninfected cells, $m = -\ln \mathbb{P}(0)$ — the basis of the infectious center assay. And at low multiplicity, $\mathbb{P}(\ge 2) \approx m^2/2$ is negligible, which is what makes single-burst experiments and genetic analyses of single infections possible ([7.11.23](/7.11.23#sec-23.5.2)).

The choice of MOI is a design decision. High multiplicity synchronizes the infection and is required for one-step growth, for biochemistry and for studying a single cycle; it also allows complementation between defective genomes, which can mask a mutant phenotype. Low multiplicity allows multiple cycles, amplifies small defects in replication or spread, and is the condition of natural infection.

### 22.6.6. The One-Step Growth Curve

**Definition 22.6.4 (One-Step Growth Curve)** A **one-step growth curve** is the time course of virus production in a culture in which all cells are infected simultaneously at high multiplicity and the inoculum is then removed or diluted, so that only one cycle of infection takes place. It resolves the cycle into:

- the **eclipse period**, from infection until the first infectious particle has been assembled inside a cell — during which the virus cannot be recovered from the culture at all, even by breaking the cells open, because the genome has left its capsid;
- the **latent period**, from infection until the first particles appear outside the cell, which includes the eclipse period plus the time needed to assemble and release;
- the rise period, during which the individual cells release their contents asynchronously; and
- the plateau, whose height divided by the number of infected cells gives the **burst size**, the mean yield per cell.

Burst sizes range from tens to thousands of particles: about 100 for phage T4 and λ, several thousand for poliovirus. Latent periods range from twenty minutes for a fast phage to hours for an animal virus and days for some herpesviruses. The experiment was designed by Ellis and Delbrück in 1939 for phages, where its logic is clearest and where it is described in detail ([7.11.23](/7.11.23#sec-23.5.2)); it is the standard way to characterize any virus–cell pair, and the difference between the intracellular and extracellular curves is the first thing it tells us about how the virus leaves the cell.

## Summary

- A virus alternates between an inert extracellular **virion** — a genome in a **capsid** (Definition 22.1.1), sometimes within a **viral envelope** (Definition 22.4.2) — and an intracellular state that is not a particle at all but a replicating genome plus the proteins it directs the cell to make. Virions are $20$–$1000\,\mathrm{nm}$ and genomes $1.7\,\mathrm{kb}$–$2.5\,\mathrm{Mb}$; the small genome forces symmetry, economy of coding and dependence on host machinery.
- The genetic material was identified as DNA by the Hershey–Chase experiment and as RNA by the reconstitution of tobacco mosaic virus; both experiments also showed that the particle self-assembles from information in its components. Viruses realize every information transfer the chemistry allows, including RNA → RNA and RNA → DNA.
- Every virus must make mRNA, and the route it takes defines its **Baltimore classification** (Definition 22.3.1). Classes III, V and VI must package their own polymerase; class IV genomes are infectious alone. Formal taxonomy is the ICTV hierarchy of six realms built on deep structural homology; the morphology-based tailed-phage families were abolished in 2022, and *myovirus*, *siphovirus* and *podovirus* now denote shapes only.
- Capsids are helical (length set by the genome, as in TMV) or icosahedral (**icosahedral symmetry**, Definition 22.4.1, with $60T$ subunits for triangulation number $T$); complex virions combine the two. Envelopes are host lipid plus viral glycoproteins and determine both the entry mechanism and the stability of the particle outside the host. Virions carry the enzymes the first minutes require.
- The infectious cycle is attachment, entry and uncoating, replication and expression, assembly, and release, with maturation after release in some viruses. The **host range** and **tissue tropism** (Definition 22.5.1) are set first by the receptor and then by every later step. Infection ends in lysis, persistence, latency, transformation or abortion, and leaves a characteristic **cytopathic effect** (Definition 22.5.2).
- Viruses are grown in cultures, eggs, animals and now organoids, and are counted by what they do: the **plaque** assay in PFU/ml (Definition 22.6.1, Eq. (22.1)), the **TCID50** by Reed–Muench or Spearman–Kärber (Definition 22.6.2, Eqs. (22.2)–(22.4)), and physical assays for particles and genomes. The particle-to-PFU ratio (Formula 22.6.1) is 1 for many phages and up to $10^4$ for animal viruses; a genome copy detected by PCR is not an infectious particle.
- Particles distribute among cells by Poisson statistics, so the **multiplicity of infection** (Definition 22.6.3) determines the fraction infected, $1 - \mathrm{e}^{-m}$, and whether cells are singly or multiply infected. A **one-step growth curve** (Definition 22.6.4) at high multiplicity resolves the **eclipse period**, the **latent period** and the **burst size**.

## Questions

1. A stock of an animal virus has a genome titer of $10^{11}$ copies/ml by RT-qPCR and an infectivity titer of $10^{7}\,\mathrm{PFU/ml}$. A colleague concludes that $99.99\,\%$ of the particles are defective. What else could explain the ratio, and what experiment would distinguish the explanations?

   **Answer** The particle-to-PFU ratio of $10^4$ (if every genome copy is in a particle) has at least three sources: genuinely defective particles; intact particles that fail at one of the many steps of a cycle in these cells, under these conditions; and free, non-encapsidated nucleic acid counted by PCR but incapable of infection. Nuclease treatment of the stock before extraction removes the third contribution. Counting particles directly in the electron microscope gives the true physical number. Whether the remainder are defective or merely unlucky can be tested by raising the multiplicity: if the particles are defective in different functions they will complement one another and the yield per cell will rise faster than the input; and single-particle imaging shows what fraction attach, enter and uncoat. Historically, the linearity of the dose–response curve shows that the successful particles act singly, so a high ratio reflects inefficiency rather than cooperation.

2. Classes III, V and VI of the Baltimore scheme package a polymerase in the virion, class IV does not. Explain why, and predict in each case what happens when purified genomic nucleic acid is transfected into a permissive cell.

   **Answer** A cell has no enzyme that can copy RNA into RNA or RNA into DNA, so a genome that is not itself translatable mRNA can do nothing until a viral polymerase is present — and that polymerase can only be made from mRNA, which does not yet exist. The only way out of the circle is to bring the enzyme in the particle. Class IV genomes are mRNA: ribosomes translate them on arrival, making the RdRp, so no packaged enzyme is needed. On transfection, class IV RNA (poliovirus) yields infectious virus; dsRNA (III), $(-)$RNA (V) and retroviral RNA (VI) do not, unless the polymerase subunits are supplied from expression plasmids — which is exactly how reverse-genetics systems for influenza virus and other negative-strand viruses are built. Class I, II and VII DNA is generally infectious, since host polymerases can transcribe it (poxvirus DNA is the exception, being cytoplasmic and dependent on packaged enzymes).

3. In an end-point dilution assay, ten wells per dilution gave the following fractions with cytopathic effect: $10^{-2}$, 1.0; $10^{-3}$, 1.0; $10^{-4}$, 0.9; $10^{-5}$, 0.4; $10^{-6}$, 0.1; $10^{-7}$, 0. Calculate the TCID50 by the Spearman–Kärber estimator and convert it to an approximate PFU titer. Why should wells be scored over the whole series rather than at the two dilutions nearest $50\,\%$?

   **Answer** With $x_0 = -2$, $d = 1$ and $\sum p_i = 1.0 + 1.0 + 0.9 + 0.4 + 0.1 + 0 = 3.4$, Eq. (22.3) gives $\log_{10}\text{TCID}_{50} = -2 + 0.5 - 3.4 = -4.9$: the $50\,\%$ end point is at the $10^{-4.9}$ dilution, so the undiluted stock contains $10^{4.9} \approx 7.9 \times 10^{4}$ TCID50 per inoculated volume. By Eq. (22.4) this is about $0.7 \times 7.9\times10^4 \approx 5.5\times10^4\,\mathrm{PFU}$ per the same volume. Using the whole series averages out the binomial scatter of the individual wells instead of resting the estimate on the two dilutions that happen to straddle $50\,\%$; the Spearman–Kärber estimator is the mean of the tolerance distribution and has the smaller variance, and its standard error can be computed from the $p_i$.

4. You wish to measure the burst size of a newly isolated phage. Design the experiment, state the multiplicity you would use and why, and say how the result would differ if the phage were released continuously rather than by lysis.

   **Answer** Mix phage with an exponentially growing culture at a multiplicity of about $0.05$–$0.1$ so that almost all infected cells receive exactly one particle (at $m = 0.1$, $\mathbb{P}(\ge 2)/\mathbb{P}(\ge 1) \approx 5\,\%$) and no cell is infected twice; allow a few minutes for adsorption; remove unadsorbed phage with antiserum or by centrifugation; dilute the culture by $10^4$ so that released particles cannot find a new host; and sample at intervals, plating each sample for plaques both directly (free virus plus infected cells, each infected cell giving one infectious center) and after artificial lysis (total intracellular plus free virus). The plateau divided by the number of infectious centers measured during the latent period is the burst size. Dilution and low multiplicity are what make the experiment "one-step". For a phage released continuously, such as the filamentous M13, there is no sharp step: free phage rises steadily from early times, no intracellular pool of complete particles accumulates, the cells keep growing, and "burst size" has to be replaced by a rate of release per cell per hour.

5. Why does attachment determine host range, and why is it nevertheless wrong to say that host range is determined by the receptor?

   **Answer** Attachment is the only step that happens outside the cell, and specific binding to a surface molecule is both necessary for entry and the first point of discrimination; a cell lacking the receptor cannot be infected at all, and a single mutation in a receptor confers resistance, which is why receptor identity sets the outer limit of the host range. But the receptor only makes a cell *susceptible*. The cell must also be *permissive*: provide the transcription factors, the translation apparatus, the membranes and the nucleotide pools the genome needs, allow the virus to counter the intrinsic and innate defenses, and permit assembly and release. Cells that are made to express a receptor often support entry but no replication; conversely, a virus can sometimes enter by an unintended route and still replicate. Host range is therefore the product of all the steps, and it can be changed by mutations affecting any of them ([7.11.27](/7.11.27)).
