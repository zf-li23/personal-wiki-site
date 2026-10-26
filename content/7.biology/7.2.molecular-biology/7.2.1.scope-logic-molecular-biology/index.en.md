---
title: Scope and Logic of Molecular Biology
description: The central dogma as a statement about transfers of sequence information; DNA, RNA and protein as archive, working copy and machine; how the concept of the gene became biochemical; the experimental logic of the discipline; the plan of the course; and the numbers of molecular biology (energies in kBT, forces in pN, lengths in nm, masses, copy numbers, rates and error frequencies).
---

Molecular biology studies how genetic information is stored, copied, read out and regulated, and it explains these processes in terms of the structures and interactions of molecules. It was born with the **double helix** in 1953: the structure immediately suggested how DNA could be copied and that the order of its bases could be a code, and the following decades turned those two suggestions into a detailed account of replication, transcription and translation. This chapter sets out the frame of the whole course. It states the central dogma precisely (1.1), follows the concept of the gene from Mendel's factor to a segment of DNA (1.2), describes the experimental logic by which every conclusion of the field was reached (1.3), places the course among its neighbors and gives its plan (1.4), and collects the physical numbers that the later chapters use to ask "how fast, how accurate, how many" (1.5). The chemistry of nucleotides and of the double helix belongs to **biochemistry** ([7.1.11](/7.1.11)); the transmission of genes between generations belongs to genetics ([7.4](/7.4)).

## 1.1. The Central Dogma and the Three Carriers of Information

### 1.1.1. Transfers of Sequence Information

In 1958 Francis Crick formulated two principles that organized the young field. The sequence hypothesis says that the specificity of a nucleic acid lies in its base sequence and that this sequence encodes the amino-acid sequence of a protein. The central dogma says in which directions such sequence information can flow. Crick restated it in 1970, after the discovery of **reverse transcriptase** had led some to announce that the dogma was overthrown; the restatement shows that it had never claimed that information flows only from DNA to RNA to protein.

**Definition 1.1.1 (Central Dogma)** The **central dogma** of molecular biology states that sequence information, once it has passed into protein, cannot get out again: it can be transferred from nucleic acid to nucleic acid and from nucleic acid to protein, but not from protein to protein or from protein to nucleic acid.

The three transfers that occur in every cell are named as follows.

**Definition 1.1.2** **Replication** is the copying of a DNA sequence into a new DNA molecule (DNA → DNA, by DNA polymerases). **Transcription** is the synthesis of an RNA molecule complementary to a DNA template (DNA → RNA, by RNA polymerases). **Translation** is the synthesis of a polypeptide whose amino-acid sequence is specified by the codons of an mRNA (RNA → protein, on the ribosome). **Reverse transcription** is the synthesis of DNA on an RNA template (RNA → DNA, by reverse transcriptases).

Crick classified all nine conceivable transfers among the three polymers into three groups:

| Class | Transfers | Where they occur |
|---|---|---|
| General (in all cells) | DNA → DNA, DNA → RNA, RNA → protein | Replication, transcription, translation |
| Special (in particular systems) | RNA → DNA | Retroviruses, **retrotransposons** (LINE-1 and its relatives make up about a fifth of the human genome, [7.2.2](/7.2.2)), **telomerase** ([7.2.7](/7.2.7)) |
| | RNA → RNA | RNA viruses (RNA-dependent **RNA polymerases**), RNA-templated amplification of **small RNAs** in plants and worms ([7.2.18](/7.2.18)) |
| | DNA → protein | Only in vitro (single-stranded DNA read directly by **ribosomes** in the presence of antibiotics) |
| Never observed | Protein → protein, protein → RNA, protein → DNA | — |

![The central dogma as a diagram of possible transfers of sequence information. Solid arrows are the general transfers found in all cells: replication by DNA polymerase, transcription by RNA polymerase and translation on the ribosome. Dashed arrows are special transfers: reverse transcription (retroviruses, retrotransposons, telomerase), RNA replication (RNA viruses) and direct translation of DNA, seen only in vitro. No arrow leaves protein. The notes beside each box give its role: DNA is a stable archive with one or two copies per cell, RNA a short-lived working copy present in many copies and sometimes catalytic, protein the machine that catalyzes, builds and regulates.](./plots/central-dogma.py)

Two clarifications prevent common misreadings. First, reverse transcription is not limited to viruses: it is how the most abundant mobile elements of our genome copy themselves and how telomerase maintains chromosome ends, so a large part of our DNA was at some point written from RNA. Second, **prions** do not violate the dogma. A prion transmits a protein conformation, not a sequence; the misfolded protein converts copies of the same polypeptide that are still encoded by the host gene. Likewise chemical modifications of DNA and **histones** (methylation, acetylation, [7.2.15](/7.2.15)) are written by proteins, but they add information alongside the sequence rather than writing a sequence. What the dogma excludes is a mechanism by which an amino-acid sequence could be used as a template, and none has been found.

### 1.1.2. Archive, Working Copy and Machine

The three carriers divide the labor of information handling in a way that resembles a computer: DNA is the disk on which the program is stored, RNA the working memory that holds the part of the program in current use, and protein the processor that carries out the work. The analogy is imperfect (RNA also catalyzes and regulates, and proteins also store information in their modifications), but it captures why each molecule has the chemistry it has.

| | DNA | RNA | Protein |
|---|---|---|---|
| Chemistry | Deoxyribose, T; double-stranded | Ribose (2′-OH), U; mostly single-stranded, folds | 20 amino acids; folds into specific structures |
| Stability | Very stable (no 2′-OH to attack the backbone); damage is repaired | Labile; bacterial **mRNA half-life** minutes, mammalian hours | Mammalian proteins about two days on average; bacterial proteins mostly diluted by growth |
| Copies | One or two per gene per cell (plus organelle genomes) | 0.1–1000 per gene | 10–10⁷ per gene |
| Main role | Archive: inheritance, template | Working copy (**mRNA**), adaptor (**tRNA**), catalyst (rRNA, **ribozymes**), regulator | Catalysis, structure, transport, signalling, regulation |
| Chapters | 7.2.2–7.2.9 | 7.2.10–7.2.18, 7.2.23 | 7.2.19–7.2.20 |

The chemical differences are not accidents. The 2′-hydroxyl that makes RNA a better catalyst also makes its backbone susceptible to cleavage, and replacing uracil by thymine lets the cell recognize uracil arising from cytosine **deamination** as damage ([7.2.8](/7.2.8)). Because RNA can both carry a sequence and catalyze reactions, it is the leading candidate for the first genetic molecule ([7.2.23](/7.2.23)).

## 1.2. What Is a Gene?

### 1.2.1. From a Unit of Heredity to One Gene, One Polypeptide

For Mendel (1865) and the classical geneticists a gene was an abstract unit that determines a character and is transmitted according to definite rules; its chemical nature was unknown, and the study of its transmission is transmission genetics ([7.4](/7.4)). The first link between genes and molecules came from **metabolism**. Archibald Garrod (1902–1909) interpreted **alkaptonuria** as an "**inborn error of metabolism**", a hereditary lack of one enzyme. George Beadle and Edward Tatum (1941) made the link experimental: they irradiated the mold *Neurospora crassa*, isolated mutants that could grow only when a particular nutrient was supplied, and found that each mutation blocked one step of a biosynthetic pathway. Their conclusion, one gene, one enzyme, was later broadened to one gene, one protein (many proteins are not enzymes) and then to one gene, one polypeptide (hemoglobin contains two different polypeptides encoded by two genes).

The colinearity of gene and protein was demonstrated by Charles Yanofsky (1964): the order of mutations along the *trpA* gene of *E. coli*, mapped by recombination, matched the order of the amino-acid changes they caused in tryptophan synthase. Colinearity holds in bacteria almost without exception; in **eukaryotes** it is broken by **introns** ([7.2.2](/7.2.2), [7.2.16](/7.2.16)).

### 1.2.2. The Biochemical Definition

Not every gene encodes a polypeptide: genes for rRNA, tRNA and many other RNAs have RNA as their final product. A definition that covers all cases must therefore be stated in terms of products.

**Definition 1.2.1 (Gene)** A **gene** is a segment of DNA (in RNA viruses, of RNA) that contains the information required to produce a functional product, a polypeptide or an RNA with a structural, catalytic or regulatory function, together with the regulatory sequences that control when and how much of it is made.

**Definition 1.2.2** The **genome** of an organism is its complete set of genetic material: the entire DNA sequence of one set of chromosomes (and, separately counted, of its organelles). The **transcriptome** is the set of all RNA molecules present in a cell, tissue or organism under given conditions. The **proteome** is the set of all proteins encoded by the genome or present in a given cell or tissue.

The definition is a working one, and four complications show where it strains. **Alternative splicing** produces several proteins from one gene, and most human multi-exon genes are alternatively spliced ([7.2.16](/7.2.16)). Genes overlap, nest inside each other's introns and are transcribed from both strands ([7.2.2](/7.2.2)). Much of the genome is transcribed into RNAs of uncertain function ([7.2.18](/7.2.18)). Regulatory sequences such as **enhancers** can lie tens of kilobases from the genes they control and serve several genes ([7.2.14](/7.2.14)). Post-genome definitions therefore define a gene by its products, for example as the union of genomic sequences that encode a coherent set of possibly overlapping functional products (Gerstein et al., 2007). In practice, genome annotations count protein-coding genes and noncoding-RNA genes separately: a human genome has about 20,000 of the former and a comparable, less certain number of the latter ([7.2.2](/7.2.2)).

## 1.3. The Method: An Experiment Behind Every Conclusion

### 1.3.1. Necessity, Sufficiency and Mechanism

Almost every statement in this course can be traced to an experiment whose design and logic can be retold. Three kinds of argument recur:

| Kind of argument | What it shows | Typical experiment |
|---|---|---|
| Genetic | A component is necessary for a process; which components act on the same molecule (cis) or through a diffusible product (trans) | Isolate mutants with a phenotype; map them; test complementation in partial diploids |
| Biochemical | A set of components is sufficient | Fractionate an extract, purify the components, reconstitute the process in vitro |
| Structural and physical | How the components work | Determine structures (X-ray, **cryo-EM**); measure rates, affinities and forces; observe single molecules |

A mechanism is established when these lines converge: the mutant lacks an activity, the purified protein restores it, and the structure explains why.

**Example 1.3.1 (DNA is the transforming principle)** Frederick Griffith (1928) found that heat-killed virulent (S) pneumococci could convert live harmless (R) cells into the virulent form. Oswald Avery, Colin MacLeod and Maclyn McCarty (1944) purified the transforming principle from S cells and used the logic of elimination: its activity survived treatment with proteases and ribonuclease but was destroyed by deoxyribonuclease, and the purified material had the elemental composition of DNA. Alfred Hershey and Martha Chase (1952) reached the same conclusion for bacteriophage T2 with radioactive labels: ³²P (in DNA) entered the infected bacteria and appeared in progeny phage, whereas most ³⁵S (in protein) stayed outside with the empty coats.

**Example 1.3.2 (A plan for the rest of the course)** The experiments retold in later chapters follow the same pattern: density-gradient centrifugation shows that replication is semiconservative ([7.2.7](/7.2.7)); partial diploids separate cis-acting **operators** from trans-acting **repressors** ([7.2.11](/7.2.11)); frameshift mutations and synthetic messengers decipher the code ([7.2.19](/7.2.19)); **R-loop** electron microscopy reveals introns ([7.2.16](/7.2.16)); injected double-stranded RNA silences genes ([7.2.18](/7.2.18)).

### 1.3.2. Discoveries Become Tools

The enzymes that cells use to handle nucleic acids became the instruments of the field. **Restriction enzymes**, found as a bacterial defence against phages, cut DNA at defined sequences; DNA ligase joins fragments; DNA polymerases copy them and, as thermostable enzymes, power PCR; reverse transcriptase converts RNA into DNA; and the CRISPR–Cas systems of bacterial immunity have become programmable genome editors. The course therefore introduces the tools early ([7.2.5](/7.2.5), [7.2.6](/7.2.6)): every later chapter uses them to read the molecular state of a cell, and the last chapters use them to rewrite it ([7.2.24](/7.2.24)). Reading (sequencing), writing (synthesis and cloning) and editing are three uses of the same enzymology.

A second principle of method is the use of model systems. The remark attributed to Jacques Monod that what is true of *E. coli* is true of the elephant expresses the bet that the core mechanisms are shared, and the bet has largely paid off: polymerases, ribosomes and the genetic code are conserved across all life. Where bacteria and eukaryotes differ (chromatin, splicing, the organization of promoters), the differences are themselves informative, and the course treats the two in parallel.

## 1.4. The Course and Its Neighbors

### 1.4.1. Division of Labor Among the Disciplines

The boundaries between molecular biology and its neighbors are matters of emphasis, not of principle:

| Discipline | What it contributes | Where |
|---|---|---|
| Biochemistry | Chemistry of nucleotides and amino acids, the double helix and its melting, enzymes and their kinetics, metabolism of nucleotides | [7.1](/7.1), especially [7.1.11](/7.1.11) |
| Genetics | Transmission of genes, mutation as a cause of phenotypes, mapping, population consequences of mutation and recombination | [7.4](/7.4) |
| Cell biology | Compartments, membranes, protein sorting, the cell cycle | [7.3](/7.3) |
| Biophysics | DNA elasticity, diffusion and single-molecule mechanics, imaging | [7.6](/7.6) |
| Bioinformatics, systems biology | Sequence and omics analysis; networks, noise and synthetic circuits | [7.8](/7.8), [7.9](/7.9) |

Molecular biology takes the molecules from biochemistry and the genes from genetics and asks how the information in the one is carried by the other.

### 1.4.2. The Plan of the Course

The chapters follow the life of genetic information, in five parts:

| Part | Chapters | Question |
|---|---|---|
| I. The carrier | 7.2.2–7.2.4: genome content, DNA topology, chromatin | What holds the information, and how is it packaged? |
| II. The tools | 7.2.5–7.2.6: cloning, measurement and sequencing | How do we see and manipulate the molecules? |
| III. Maintenance | 7.2.7–7.2.9: replication, repair, recombination | How is the information copied and kept intact? |
| IV. Read-out and its control | 7.2.10–7.2.20: transcription and its regulation in bacteria and eukaryotes, chromatin regulation, RNA processing, RNA stability and regulatory RNA, translation and its control | How is the information read, and how is the reading controlled? |
| V. Integration | 7.2.21–7.2.25: condensates, a quantitative view of gene expression, the RNA world, gene editing, summary | How do the parts combine, how did the system arise, and how can it be rewritten? |

Each chapter ends its main line with a quantitative question (how fast, how accurate, how many molecules), using the numbers of the next section.

## 1.5. The Numbers of Molecular Biology

Molecular processes happen at a characteristic scale: lengths of nanometers, forces of piconewtons, energies of a few times the thermal energy, times from microseconds to hours. Knowing these numbers turns qualitative statements into checks: whether a bond can be broken by thermal motion, whether a cell can contain enough copies of a molecule for a reaction to be fast, whether a process can be finished within a cell cycle.

### 1.5.1. Energy: The Thermal Energy as the Unit

**Definition 1.5.1 (Thermal Energy)** The **thermal energy** $k_{\mathrm{B}}T$, the product of the Boltzmann constant and the absolute temperature, is the natural unit of energy for molecular processes. At $T = 310\,\mathrm{K}$,

$$
k_{\mathrm{B}}T = 4.28\times10^{-21}\,\mathrm{J} = 4.28\,\mathrm{pN\,nm}, \qquad N_{\mathrm{A}}k_{\mathrm{B}}T = RT = 2.58\,\mathrm{kJ\,mol^{-1}}
$$
(at $298\,\mathrm{K}$: $4.11\,\mathrm{pN\,nm}$ and $2.48\,\mathrm{kJ\,mol^{-1}}$; in the older unit, $RT \approx 0.6\,\mathrm{kcal\,mol^{-1}}$).

The reason for this unit is the **Boltzmann distribution** ([6.3.10](/6.3.10)): at equilibrium the probability of a state of energy $E$ relative to a state of energy 0 is $\mathrm{e}^{-E/k_{\mathrm{B}}T}$. An energy difference of $1\,k_{\mathrm{B}}T$ is overcome constantly by thermal motion; $5\,k_{\mathrm{B}}T$ gives a ratio of $0.007$; $20\,k_{\mathrm{B}}T$ gives $2\times10^{-9}$ and is, for a single event, practically irreversible.

![Energies of molecular biology in units of the thermal energy. A: typical ranges, with the scale in kilojoules per mole on top; noncovalent interactions in water (a van der Waals contact, a hydrogen bond or salt bridge) are comparable to the thermal energy, a base pair or the folding of a small protein is worth a few to a few tens of kBT, ATP hydrolysis under cellular conditions and the specific binding of a transcription factor about 20 kBT, a visible photon and a covalent C–C bond about 100 kBT. B: the Boltzmann factor, the relative probability of a state lying E above another, falls by a factor of ten for every 2.3 kBT.](./plots/energy-scale.py)

The scale explains a central feature of molecular biology: the interactions that carry information (base pairing, protein–DNA recognition, protein–protein contacts) are built from many weak bonds of $1$–$3\,k_{\mathrm{B}}T$ each, so they are specific in sum but individually reversible, whereas covalent bonds ($\sim 140\,k_{\mathrm{B}}T$) are stable on biological time scales and are made and broken only by enzymes. The hydrolysis of one ATP, about $20\,k_{\mathrm{B}}T$ under cellular conditions ([7.1.16](/7.1.16)), is enough to make one step of a motor or one cycle of an enzyme effectively one-way.

### 1.5.2. Length, Force and Mass

Since $1\,k_{\mathrm{B}}T \approx 4\,\mathrm{pN\,nm}$, a force of a few piconewtons acting over a nanometer does work comparable to the thermal energy: this is why molecular motors and single-molecule experiments work in piconewtons. The table collects the numbers used most often in this course; values are typical, rounded to the precision that matters.

| Quantity | Value | Remark |
|---|---|---|
| Rise per base pair (B-DNA) | $0.34\,\mathrm{nm}$ | $1\,\mathrm{Mb}$ of DNA is $0.34\,\mathrm{mm}$ long |
| Helical repeat (B-DNA in solution) | $10.5\,\mathrm{bp}$ per turn, $3.6\,\mathrm{nm}$ per turn | Measured topologically ([7.2.3](/7.2.3)) |
| Diameter of the double helix | $2.0\,\mathrm{nm}$ | Major groove about $2.2\,\mathrm{nm}$ wide, minor groove $1.2\,\mathrm{nm}$ |
| Persistence length of dsDNA | $50\,\mathrm{nm}$ ($\approx 150\,\mathrm{bp}$) | DNA is stiff below this length ([7.6](/7.6)) |
| Nucleosome core particle | $147\,\mathrm{bp}$ in $1.65$ turns around an $11\,\mathrm{nm}$ disc | Repeat about $200\,\mathrm{bp}$ ([7.2.4](/7.2.4)) |
| α helix | $3.6$ residues per turn, $0.15\,\mathrm{nm}$ rise per residue, pitch $0.54\,\mathrm{nm}$ | [7.1.5](/7.1.5) |
| β strand | about $0.33\,\mathrm{nm}$ per residue | |
| Lipid bilayer | $4$–$5\,\mathrm{nm}$ thick | |
| Mass of an amino-acid residue | $110\,\mathrm{Da}$ on average | A $300$-residue protein is about $33\,\mathrm{kDa}$ |
| Mass of a nucleotide residue; of a base pair | $330\,\mathrm{Da}$; $650\,\mathrm{Da}$ | The *E. coli* genome is about $5\,\mathrm{fg}$, a diploid human genome $6.6\,\mathrm{pg}$ |
| Forces | Kinesin stalls at $6\,\mathrm{pN}$, RNA polymerase at about $25\,\mathrm{pN}$, phage packaging motors above $50\,\mathrm{pN}$; B-DNA overstretches at $65\,\mathrm{pN}$; covalent bonds break at nanonewtons | |

### 1.5.3. Copy Numbers and Concentrations

A cell contains a definite number of each molecule, and many molecules are present in small numbers. The conversion between copy number and concentration follows from the volume.

**Example 1.5.1 (One molecule per bacterium)** An *E. coli* cell has a volume of about $1\,\mu\mathrm{m}^3 = 10^{-15}\,\mathrm{L}$. One molecule in this volume has the concentration

$$
c = \frac{1}{N_{\mathrm{A}}V} = \frac{1}{6.02\times10^{23}\,\mathrm{mol^{-1}}\times10^{-15}\,\mathrm{L}} \approx 1.7\,\mathrm{nM}.
$$
A protein present at 100 copies is therefore at about $0.17\,\mu\mathrm{M}$, and the 10 or so lac repressor tetramers of a cell are at about $17\,\mathrm{nM}$: far above their dissociation constant for the operator, so the operator is almost always occupied in the absence of inducer ([7.2.11](/7.2.11)). In a mammalian cell of about $3000\,\mu\mathrm{m}^3$, one molecule corresponds to about $0.5\,\mathrm{pM}$.

| Per cell | *E. coli* (about $1\,\mu\mathrm{m}^3$) | Human cell (about $2000$–$4000\,\mu\mathrm{m}^3$) |
|---|---|---|
| Genome | $4.6\,\mathrm{Mb}$, 1–8 copies depending on growth rate | $6.2\,\mathrm{Gb}$ (diploid), about $3\times10^7$ nucleosomes |
| Protein-coding genes | about 4300 | about 20,000 |
| mRNA molecules | $10^3$–$10^4$ (less than one per gene on average) | $10^5$–$10^6$ |
| Protein molecules | about $3\times10^6$ | $10^9$–$10^{10}$ |
| Ribosomes | $10^4$–$7\times10^4$ (rising with growth rate) | $10^6$–$10^7$ |
| RNA polymerases | $10^3$–$10^4$ | about $10^5$ (Pol II) |
| A typical transcription factor | $10$–$10^3$ | $10^3$–$10^5$ |

The small numbers have two consequences that recur in the course: reactions involving one gene and a few regulatory molecules are noisy ([7.2.22](/7.2.22)), and the time a regulator needs to find its site is limited by diffusion ([7.2.22](/7.2.22)).

### 1.5.4. Rates and Error Frequencies

| Process | Typical rate | Typical time |
|---|---|---|
| Diffusion of a protein in cytoplasm | $D \approx 10\,\mu\mathrm{m^2\,s^{-1}}$ (GFP in *E. coli*; about $25$ in mammalian cytoplasm) | Crossing a bacterium ($1\,\mu\mathrm{m}$): about $0.05\,\mathrm{s}$ |
| Replication fork | *E. coli* $\approx 1000\,\mathrm{nt\,s^{-1}}$; human $\approx 15$–$50\,\mathrm{nt\,s^{-1}}$ | *E. coli* chromosome: about $40\,\mathrm{min}$ |
| Transcription elongation | $20$–$80\,\mathrm{nt\,s^{-1}}$ | A $1\,\mathrm{kb}$ gene: about $20\,\mathrm{s}$ |
| Translation elongation | *E. coli* $10$–$20\,\mathrm{aa\,s^{-1}}$; eukaryotes $3$–$8\,\mathrm{aa\,s^{-1}}$ | A $300$-residue protein: $15\,\mathrm{s}$ to $1\,\mathrm{min}$ |
| mRNA half-life | *E. coli* minutes; mammals median about $9\,\mathrm{h}$ | |
| Protein half-life | Mammals median about $2\,\mathrm{d}$; most bacterial proteins are diluted by growth before they are degraded | |
| Cell cycle | *E. coli* $20\,\mathrm{min}$ at fastest; human cells about $24\,\mathrm{h}$ | |

**Example 1.5.2 (How long does it take to transcribe a gene?)** The human dystrophin gene spans about $2.2\,\mathrm{Mb}$. At an elongation rate of about $2.4\,\mathrm{kb\,min^{-1}}$ ($40\,\mathrm{nt\,s^{-1}}$), one transcript takes

$$
\frac{2.2\times10^6\,\mathrm{nt}}{2.4\times10^3\,\mathrm{nt\,min^{-1}}} \approx 920\,\mathrm{min} \approx 15\,\mathrm{h},
$$
close to the 16 hours measured in muscle cells. A long gene thus cannot respond to a signal faster than its transcription time, a constraint that matters in development, where some long genes are not transcribed to completion within a short cell cycle.

The accuracy of the three general transfers differs by six orders of magnitude, and so does what an error costs: a replication error is inherited by every descendant cell, whereas a transcription or translation error affects one short-lived molecule.

![Speed and accuracy of the general transfers, as order-of-magnitude ranges on logarithmic axes. A: elongation rates; bacterial replication is the fastest polymerization in the cell, eukaryotic replication is about twenty times slower and is compensated by many origins, transcription runs at tens of nucleotides per second and translation at a few to twenty amino acids per second. B: error frequencies per nucleotide or residue. For replication the fidelity cascade is shown step by step: base selection by the polymerase, then exonucleolytic proofreading, then mismatch repair, which together give about one error in 10⁹–10¹⁰ base pairs. Transcription errs about once in 10⁵–10⁶ nucleotides, aminoacylation of tRNA about once in 10⁴–10⁵ and decoding on the ribosome about once in 10³–10⁴ codons.](./plots/rates-fidelity.py)

The low error of replication cannot be explained by the free-energy difference between a correct and an incorrect base pair alone, which gives a discrimination of only about $10^{-2}$ to $10^{-4}$ per step. It is achieved by repeated checking at the cost of energy and time: proofreading, mismatch repair, and, in translation, **kinetic proofreading** ([6.3.18](/6.3.18), [7.2.19](/7.2.19)). Where each of the three transfers sits on the trade-off between speed, accuracy and energy is one of the quantitative themes of the course ([7.2.22](/7.2.22)).

## Summary

| Topic | Key points |
|---|---|
| Central dogma (Definition 1.1.1) | No transfer of sequence information out of protein; general transfers DNA → DNA, DNA → RNA, RNA → protein (Definition 1.1.2); special transfers RNA → DNA (retroviruses, retrotransposons, telomerase), RNA → RNA (RNA viruses), DNA → protein (in vitro only) |
| Three carriers | DNA archive (stable, 1–2 copies), RNA working copy (labile, many copies, also catalytic), protein machine |
| Gene (Definition 1.2.1) | Garrod → Beadle–Tatum (one gene, one enzyme) → one polypeptide → DNA segment encoding a functional product plus its regulatory sequences; complications: splicing, overlapping genes, noncoding RNA, distant enhancers |
| Genome, transcriptome, proteome (Definition 1.2.2) | All the DNA; all the RNA in given conditions; all the proteins |
| Method | Genetic (necessity), biochemical (sufficiency), structural and physical (mechanism); DNA as transforming principle (Example 1.3.1); enzymes of nucleic-acid metabolism become tools |
| Course plan | Carrier (2–4), tools (5–6), maintenance (7–9), read-out and control (10–20), integration (21–25) |
| Energy (Definition 1.5.1) | $k_{\mathrm{B}}T = 4.28\,\mathrm{pN\,nm} = 2.58\,\mathrm{kJ\,mol^{-1}}$ at $310\,\mathrm{K}$; weak bonds $1$–$3\,k_{\mathrm{B}}T$, ATP $\approx 20\,k_{\mathrm{B}}T$, covalent bond $\approx 140\,k_{\mathrm{B}}T$ |
| Lengths and masses | $0.34\,\mathrm{nm}$ per bp, $10.5\,\mathrm{bp}$ per turn, $2\,\mathrm{nm}$ diameter, $50\,\mathrm{nm}$ persistence length; $110\,\mathrm{Da}$ per residue, $650\,\mathrm{Da}$ per bp |
| Copy numbers | One molecule per *E. coli* $\approx 1.7\,\mathrm{nM}$ (Example 1.5.1); mRNA $10^3$–$10^4$ and protein $3\times10^6$ per bacterium |
| Rates and errors | Replication $1000$ (*E. coli*) and $15$–$50$ (human) $\mathrm{nt\,s^{-1}}$, error $10^{-10}$–$10^{-9}$; transcription $20$–$80\,\mathrm{nt\,s^{-1}}$, error $10^{-6}$–$10^{-5}$; translation $3$–$20\,\mathrm{aa\,s^{-1}}$, error $10^{-4}$–$10^{-3}$; a $2.2\,\mathrm{Mb}$ gene takes about $15\,\mathrm{h}$ to transcribe (Example 1.5.2) |

## Questions

1. Does the existence of reverse transcriptase contradict the central dogma? Does the inheritance of a prion phenotype?

   **Answer** Neither does. The dogma (Definition 1.1.1) forbids only transfers of sequence information out of protein. Reverse transcription is a transfer from nucleic acid to nucleic acid, one of the special transfers in Crick's classification. A prion propagates a conformation: the misfolded protein converts other molecules of the same polypeptide, whose sequence is still encoded by the host gene, so no amino-acid sequence is used as a template.

2. A protein is present at 50 copies in an *E. coli* cell. What is its concentration? If its dissociation constant for a DNA site is $10\,\mathrm{nM}$ and only the free protein binds, what fraction of the time is a single site occupied (ignore nonspecific binding)?

   **Answer** By Example 1.5.1, $c \approx 50\times1.7\,\mathrm{nM} = 85\,\mathrm{nM}$. The occupancy is $\theta = c/(c + K_D) = 85/95 \approx 0.89$. In reality most of the protein is bound nonspecifically to the millions of other sites on the chromosome, which lowers the free concentration; this correction is the subject of [7.2.11](/7.2.11).

3. Estimate the mass of DNA and the number of nucleosomes in a diploid human cell, and the length of its DNA if stretched out.

   **Answer** $6.2\times10^9\,\mathrm{bp}\times650\,\mathrm{g\,mol^{-1}}/(6.02\times10^{23}\,\mathrm{mol^{-1}}) \approx 6.7\times10^{-12}\,\mathrm{g} = 6.7\,\mathrm{pg}$. With one nucleosome per about $200\,\mathrm{bp}$: $6.2\times10^9/200 \approx 3\times10^7$ nucleosomes. Length: $6.2\times10^9\times0.34\,\mathrm{nm} \approx 2.1\,\mathrm{m}$, packed into a nucleus about $10\,\mu\mathrm{m}$ across.

4. Translation in *E. coli* makes about one error per $10^4$ codons. What fraction of molecules of a $1000$-residue protein are free of errors? What would the fraction be with the error frequency of transcription, $10^{-5}$?

   **Answer** With independent errors at frequency $\varepsilon$ per residue, the error-free fraction is $(1-\varepsilon)^{L} \approx \mathrm{e}^{-\varepsilon L}$. For $\varepsilon = 10^{-4}$, $L = 1000$: $\mathrm{e}^{-0.1} \approx 0.90$. For $\varepsilon = 10^{-5}$: $\mathrm{e}^{-0.01} \approx 0.99$. Translation accuracy is thus just good enough for proteins of typical length; very long proteins (titin has about 34,000 residues) are made with a substantial fraction of errors, which cells tolerate because most substitutions are mild.

5. Using the energy scale, explain why the two strands of DNA can be separated by a helicase consuming one ATP per base pair or so, while a covalent bond in the backbone is never broken by thermal motion during the life of a cell.

   **Answer** Separating one base pair costs a few $k_{\mathrm{B}}T$ (stacking and pairing, about $1$–$5\,k_{\mathrm{B}}T$), less than the roughly $20\,k_{\mathrm{B}}T$ released by one ATP, so a helicase can couple hydrolysis to unwinding. The Boltzmann factor for breaking a covalent bond of about $140\,k_{\mathrm{B}}T$ is $\mathrm{e}^{-140} \approx 10^{-61}$: even with molecular attempt frequencies of $10^{13}\,\mathrm{s^{-1}}$, spontaneous homolysis would take far longer than the age of the universe. Backbone bonds are instead broken by hydrolysis, which has a lower barrier and is catalyzed by nucleases, and spontaneous chemical damage (depurination, deamination) proceeds through such lower-barrier reactions ([7.2.8](/7.2.8)).
