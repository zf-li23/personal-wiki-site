---
title: DNA Replication
description: Semiconservative replication and the Meselson–Stahl experiment; origins, bidirectional forks, Okazaki fragments and RNA primers; the chemistry of DNA polymerization (template, primer, two-metal-ion catalysis, base selection and proofreading); the five DNA polymerases of E. coli, the Pol III holoenzyme and the sliding clamp; initiation at oriC, the replisome, termination at Ter–Tus and once-per-cycle control; eukaryotic licensing, the CMG helicase, the division of labor among Pol α, δ and ε, chromatin replication, telomerase; replication time, multifork replication, stochastic origin firing and the fidelity budget.
---

**Replication** is the transfer of the **central dogma** that every cell must perform completely, exactly once per division and with an error rate far below that of any other biosynthetic process: an *E. coli* cell copies $4.6\times10^6$ **base pairs** in about forty minutes and makes about one error in $10^{10}$ nucleotides, and a human cell copies $6\times10^9$ base pairs in an S phase of about eight hours. The **double helix** suggested the principle at once (each strand is a template for the other), but the machinery that implements it had to be discovered step by step, and almost every step answered one of a short list of questions: is the copy semiconservative; where does replication start and in which directions does it proceed; how can two antiparallel strands be copied by enzymes that work in one direction only; how are a high speed and a low error rate achieved together; how is initiation limited to once per cell cycle; and how are the ends of linear chromosomes copied. This chapter follows those questions: the mode of replication (7.1), the geometry of the fork (7.2), the chemistry of polymerization and its fidelity (7.3), the bacterial replisome (7.4), termination and control (7.5), replication in **eukaryotes** and at **telomeres** (7.6), and the arithmetic of time, origins and errors (7.7). The topological problem created by unwinding is treated in [7.2.3](/7.2.3); the repair of the errors and lesions that escape replication follows in [7.2.8](/7.2.8), and the use of replication enzymes as laboratory tools in [7.2.5](/7.2.5).

## 7.1. Semiconservative Replication

### 7.1.1. Three Models

Watson and Crick noted in 1953 that the complementarity of the two strands "immediately suggests a possible copying mechanism": the strands separate and each directs the synthesis of a new partner. Three outcomes were conceivable for the distribution of parental material among the products.

**Definition 7.1.1 (Semiconservative Replication)** In **semiconservative replication** each daughter duplex consists of one parental strand and one newly synthesized strand. In **conservative replication** the parental duplex would remain intact and the copy would consist of two new strands; in **dispersive replication** each strand of both daughters would be a patchwork of old and new segments.

### 7.1.2. The Meselson–Stahl Experiment

In 1957 Matthew Meselson and Franklin Stahl grew *E. coli* for many generations in a medium whose only nitrogen source was $\ce{^{15}NH4Cl}$, so that all DNA was "heavy", then transferred the cells to $\ce{^{14}NH4Cl}$ and took samples after each doubling. DNA extracted from the samples was centrifuged to equilibrium in a cesium chloride gradient, in which each molecule comes to rest where the density of the solution equals its own buoyant density: $1.724\,\mathrm{g\,mL^{-1}}$ for fully heavy DNA, $1.710\,\mathrm{g\,mL^{-1}}$ for fully light DNA. The bands were located by their ultraviolet absorption.

![The Meselson–Stahl experiment computed for the three models. Each row is a CsCl equilibrium gradient after the given number of generations in light medium, shown as the absorbance profile of the DNA bands (Gaussian bands of equal width at the buoyant densities of fully heavy, 1.724, hybrid, 1.717, and fully light DNA, 1.710 g/mL; areas proportional to the amount of DNA). Conservative replication would keep a heavy band while adding a light one; semiconservative replication gives a single hybrid band after one generation and then hybrid and light bands in the ratios 1:1, 1:3 and 1:7; dispersive replication gives a single band that moves step by step toward the light density. The observed pattern is the middle column.](./plots/meselson-stahl.py)

After one generation all DNA formed a single band of intermediate density, which excludes the conservative model. After two generations there were two bands of equal intensity, hybrid and light, which excludes the dispersive model; after three generations the ratio was 1:3. When the hybrid DNA was denatured by heat, it separated into single strands of heavy and of light density, so the hybrid band was made of one entirely old and one entirely new strand, as the semiconservative model predicts. The experiment is the model of a decisive measurement in molecular biology: a physical property (density) is made to report a molecular history (which atoms were incorporated when), and the three hypotheses make quantitatively different predictions.

**Example 7.1.1** After $g \geq 1$ generations of semiconservative replication, the $2^g$ duplexes descended from one heavy duplex contain the two original heavy strands in exactly two hybrid molecules, so the fraction of hybrid DNA is $2/2^g = 2^{1-g}$ and the ratio of hybrid to light DNA is $2 : (2^g - 2)$. After three generations (an eightfold increase in DNA) the ratio is $2 : 6 = 1 : 3$; under the dispersive model every duplex would instead have a heavy fraction of $2^{-3}$ and a density of $1.710 + 0.014/8 \approx 1.712\,\mathrm{g\,mL^{-1}}$.

## 7.2. Origins, Forks and Okazaki Fragments

### 7.2.1. Bidirectional Replication from an Origin

John Cairns (1963) labeled replicating *E. coli* with $[^3\mathrm{H}]$thymidine, spread the gently lysed DNA on a slide and exposed it to a photographic emulsion. The autoradiographs showed the chromosome as a single circle, about $1.7\,\mathrm{mm}$ long, with an internal loop: a replicating circle looks like the Greek letter $\theta$. Both strands were being copied at the same time, and no long single-stranded regions were seen, so the parental strands are not separated completely before copying begins.

**Definition 7.2.1** A **replication fork** is the Y-shaped region in which the parental duplex is being unwound and both separated strands are being copied. An **origin of replication** is the DNA site at which replication of a chromosome or plasmid begins; a segment replicated from one origin is a **replicon**.

That replication starts at fixed origins and usually proceeds in both directions was shown by marking positions along the DNA. In **denaturation** mapping (Ross Inman), partially melted molecules of phage λ show reproducible single-stranded bubbles at AT-rich sequences; on replicating molecules these landmarks showed that every replication loop started at the same point and grew at both ends. In *E. coli*, a short pulse of radioactive thymidine labeled both ends of the loop, so both ends are active forks moving away from the origin. Bidirectional replication is the rule for bacterial and eukaryotic chromosomes; some **plasmids** (ColE1) replicate unidirectionally, and some phages and plasmids use a rolling circle, in which one strand is nicked and its $3'$ end is extended around the circle while the old strand is displaced.

### 7.2.2. Semidiscontinuous Synthesis

All DNA polymerases synthesize DNA in the $5' \to 3'$ direction (7.3.1). Because the two strands of a duplex are antiparallel, one daughter strand at a fork can grow in the direction of fork movement while the other would have to grow $3' \to 5'$ overall. Reiji and Tsuneko Okazaki resolved the paradox in 1968: when *E. coli* was labeled with $[^3\mathrm{H}]$thymidine for only a few seconds, much of the label was found in short pieces of DNA, which became incorporated into long DNA during a subsequent chase with unlabeled thymidine; in cells with a defective **DNA ligase** the short pieces accumulated.

**Definition 7.2.2** At a replication fork, the **leading strand** is the daughter strand that is synthesized continuously in the direction of fork movement; the **lagging strand** is synthesized discontinuously, in the direction opposite to fork movement, as a series of short **Okazaki fragments** that are later joined. Okazaki fragments are about $1000$–$2000$ nucleotides long in bacteria and $150$–$200$ nucleotides in eukaryotes.

The fragments are joined by DNA ligase (Definition 5.3.1). Replication is therefore semiconservative, bidirectional and semidiscontinuous; these three words summarize the first two sections.

### 7.2.3. RNA Primers

No DNA polymerase can start a chain: each can only extend a primer with a free $3'$-OH (7.3.1). Kornberg's group found that nascent Okazaki fragments of phages and of *E. coli* carry a few ribonucleotides at their $5'$ ends, and that in *E. coli* their synthesis is resistant to rifampicin, an inhibitor of RNA polymerase, so the **primers** are made by a separate enzyme.

**Definition 7.2.3 (Primase)** A **primase** is a DNA-dependent RNA polymerase that synthesizes the short RNA primers on which DNA polymerases start new DNA chains at replication origins and on the lagging strand. In *E. coli* the primase is DnaG, which makes primers of about $10$–$12$ nucleotides; in eukaryotes it is part of the DNA polymerase α–primase complex.

Every Okazaki fragment begins with its own primer, and the leading strand needs one primer at the origin. Because RNA primers would leave ribonucleotides in the genome, they are removed after synthesis and replaced with DNA (7.4.4). Starting chains with RNA has a plausible logic: the first few nucleotides of a new chain cannot be proofread (7.3.3), so they are made in a material that is marked for replacement.

## 7.3. The Chemistry of DNA Polymerization

### 7.3.1. Template, Primer and Direction

Arthur Kornberg purified the first DNA-synthesizing enzyme from *E. coli* in 1955–1957, now called DNA polymerase I, and used it to establish the requirements of DNA synthesis.

**Definition 7.3.1 (DNA Polymerase)** A **DNA polymerase** is an enzyme that adds deoxynucleotides to the $3'$-OH end of a primer strand annealed to a template, choosing each incoming deoxynucleoside triphosphate (dNTP) by complementarity to the template base. The reaction is

$$
(\mathrm{dNMP})_n + \mathrm{dNTP} \longrightarrow (\mathrm{dNMP})_{n+1} + \mathrm{PP_i}, \tag{7.1}
$$
in which the $3'$-OH of the primer terminus attacks the α-phosphorus of the dNTP and pyrophosphate is released. All known DNA polymerases require a template and a primer and synthesize DNA only in the $5' \to 3'$ direction.

The new **phosphodiester bond** is formed at the expense of a phosphoanhydride bond, so reaction (7.1) alone has a small free-energy change; base stacking and pairing in the product stabilize it, and hydrolysis of the pyrophosphate by pyrophosphatase ($\Delta_{\mathrm{r}}G'^{\circ} \approx -19\,\mathrm{kJ\,mol^{-1}}$) makes polymerization effectively irreversible. Each added nucleotide thus costs two phosphoanhydride bonds. The $5' \to 3'$ rule follows from this chemistry: the energy for adding a nucleotide is carried by the incoming nucleotide itself. A hypothetical $3' \to 5'$ polymerase would have to carry the activating triphosphate on the end of the growing chain; removing a wrong nucleotide from that end in proofreading would also remove the activation, and the chain could not be extended again without a separate reactivation step.

### 7.3.2. Two Metal Ions in a Hand-Shaped Active Site

The catalytic cores of DNA polymerases resemble a right hand gripping the primer–template: the palm carries the catalytic **residues**, the fingers bind the incoming dNTP and the template base, and the thumb holds the duplex product and contributes to processivity. Catalysis uses two $\ce{Mg^2+}$ ions held by two conserved aspartate residues of the palm. Metal ion A lowers the $\mathrm{p}K_{\mathrm{a}}$ of the primer $3'$-OH and positions the resulting alkoxide for in-line attack on the α-phosphate; metal ion B binds the β- and γ-phosphates of the dNTP, neutralizes the negative charge that develops in the pentacovalent transition state and assists the departure of pyrophosphate. The same two-metal-ion mechanism is used by RNA polymerases ([7.2.10](/7.2.10)), reverse transcriptases and many nucleases, a reflection of the common chemistry of nucleotidyl transfer.

Binding of the correct dNTP closes the fingers onto the nascent base pair (an induced-fit conformational change), and only the closed complex is catalytically competent. After bond formation the enzyme translocates by one base pair, moving the new pair from the insertion site to the postinsertion site.

### 7.3.3. Fidelity: Base Selection and Proofreading

Watson–Crick pairs A·T and G·C have nearly identical geometry: the distance between the C1′ atoms of the two sugars is about $1.05\,\mathrm{nm}$ in both, and the glycosidic bonds make the same angles with the pair. The closed **active site** is shaped to accommodate this geometry; a mismatched pair, even one that forms hydrogen bonds (such as a G·T wobble pair or a pair with a rare tautomer), distorts it and is rejected before or after the fingers close. Base selection by replicative polymerases gives about one error in $10^4$–$10^5$ insertions, much better than the free-energy difference between correct and incorrect pairs in solution would allow, because the enzyme tests geometry and not only hydrogen bonding.

**Definition 7.3.2 (Proofreading)** **Proofreading** by a DNA polymerase is the removal, by a $3' \to 5'$ exonuclease activity of the same enzyme or complex, of a misincorporated nucleotide from the primer terminus before synthesis continues.

A mismatched terminus is extended slowly and melts more easily; it frays into the exonuclease site, which in DNA polymerase I lies about $3\,\mathrm{nm}$ from the polymerase site, and the wrong nucleotide is hydrolyzed off. Removal and replacement of one nucleotide costs two further phosphoanhydride bonds, so proofreading trades energy for accuracy. It improves fidelity by a factor of $10^2$–$10^3$. The kinetic logic, in which a branch that removes errors is placed after an irreversible step, is that of **kinetic proofreading** ([6.3.18](/6.3.18)); the same logic recurs in tRNA charging and decoding ([7.2.19](/7.2.19)).

**Definition 7.3.3** An **exonuclease** hydrolyzes nucleotides one at a time from an end of a nucleic acid strand, in the $5' \to 3'$ or the $3' \to 5'$ direction; an **endonuclease** cleaves phosphodiester bonds within a strand.

DNA polymerase I is a single polypeptide of $103\,\mathrm{kDa}$ with three activities. Mild proteolysis splits it into a small fragment carrying the $5' \to 3'$ exonuclease and a large fragment of $68\,\mathrm{kDa}$, the Klenow fragment, which retains the polymerase and the $3' \to 5'$ proofreading exonuclease. The $5' \to 3'$ exonuclease degrades a strand paired to the template ahead of the polymerase, which can therefore move a nick along the DNA (**nick translation**, Definition 5.7.1). Most other DNA polymerases lack this activity; Pol I uses it to remove RNA primers.

**Definition 7.3.4 (Processivity)** The **processivity** of a polymerase is the average number of nucleotides it adds in one binding event, before it dissociates from the primer–template.

## 7.4. The Bacterial Replisome

### 7.4.1. Five DNA Polymerases

Pol I accounts for more than 90 % of the DNA polymerase activity in *E. coli* extracts, but it is not the replicative enzyme: it is too slow and too distributive for the observed fork rate, and in 1969 Paula DeLucia and John Cairns isolated a *polA* mutant that was viable, though sensitive to ultraviolet light and alkylating agents. The search for other polymerases in this mutant found Pol II and Pol III (1970–1971); Pol IV and Pol V were identified in 1999 as members of the translesion family ([7.2.8](/7.2.8)).

| Property | Pol I | Pol II | Pol III | Pol IV | Pol V |
|---|---|---|---|---|---|
| Gene (polymerase **subunit**) | *polA* | *polB* | *polC* (*dnaE*) | *dinB* | *umuC* |
| Family | A | B | C | Y | Y |
| $3' \to 5'$ exonuclease (proofreading) | yes | yes | yes (ε subunit) | no | no |
| $5' \to 3'$ exonuclease | yes | no | no | no | no |
| Rate / ($\mathrm{nt\,s^{-1}}$) | $10$–$20$ | $40$ | $250$–$1000$ | $2$–$3$ | $1$ |
| Processivity / nt | $3$–$200$ | $1500$ | $\geq 500{,}000$ (**holoenzyme**) | $1$ (more with β clamp) | $6$–$8$ |
| Role | primer removal, gap filling in repair | restart and repair | chromosome replication | translesion synthesis | translesion synthesis (SOS) |

### 7.4.2. The Pol III Holoenzyme and the Sliding Clamp

Pol III is a complex of nine kinds of subunits (ten if the γ variant of τ is counted). The core is αεθ: α (*dnaE*) is the polymerase, ε (*dnaQ*, also called *mutD* because its mutations raise the mutation rate a thousandfold) the proofreading exonuclease, and θ stabilizes ε. The core alone has a processivity of only $10$–$20$ nucleotides. Processivity comes from a separate ring:

**Definition 7.4.1 (Sliding Clamp)** A **sliding clamp** is a ring-shaped protein that encircles duplex DNA, slides along it, and binds a polymerase, keeping it on the template; a **clamp loader** is an AAA+ ATPase complex that opens the ring with energy from ATP binding, places it around a primer–template junction and releases it closed after ATP hydrolysis. The bacterial clamp is the β dimer (*dnaN*), and the eukaryotic clamp is the trimer PCNA (proliferating cell nuclear antigen), loaded by RFC (replication factor C).

The β ring has an inner diameter of about $3.5\,\mathrm{nm}$, wide enough for **B-DNA** with a layer of water, and its six similar **domains** (three per subunit) give it a pseudo-sixfold symmetry; PCNA forms the same kind of ring from three subunits of two domains each, although the two proteins have no detectable sequence similarity. The clamp loader of Pol III (the γ or τ complex, $\tau_3\delta\delta'$, plus χψ) also links up to three cores through the τ subunits and binds the helicase; the assembly of cores and clamp loader is Pol III*, and with β clamps it is the Pol III holoenzyme, which adds about $1000$ nucleotides per second with a processivity of more than $5\times10^5$.

The clamp is a general platform: Pol I, Pol II, Pol IV, Pol V, DNA ligase and mismatch-repair proteins all bind β through a short **motif**, and in eukaryotes more than a hundred proteins bind PCNA. Clamps left behind on Okazaki fragments mark newly synthesized DNA, which eukaryotic mismatch repair uses to identify the new strand ([7.2.8](/7.2.8)).

### 7.4.3. Initiation at *oriC*

The *E. coli* origin, *oriC*, is a region of about $245\,\mathrm{bp}$. It contains **binding sites** for the initiator DnaA (five high-affinity $9\,\mathrm{bp}$ DnaA boxes, R1–R5, and several lower-affinity sites that bind only DnaA·ATP), sites for the DNA-bending proteins IHF and FIS, and an AT-rich DNA unwinding element (DUE) of three tandem $13\,\mathrm{bp}$ repeats. It also contains eleven GATC sites, which Dam methylase methylates on adenine (7.5.2).

| Protein | Subunits | Function at the origin |
|---|---|---|
| DnaA | about 8–20 per origin | AAA+ ATPase; DnaA·ATP binds the DnaA boxes and forms a right-handed filament that melts the DUE |
| DnaB | hexamer | replicative helicase; encircles the lagging-strand template and moves $5' \to 3'$ |
| DnaC | hexamer | helicase loader; opens the DnaB ring and places it on single-stranded DNA |
| HU, IHF, FIS | dimers | bend DNA and modulate initiation |
| DnaG (primase) | monomer | synthesizes RNA primers; binds DnaB |
| SSB | tetramer | coats single-stranded DNA |
| **DNA gyrase** | $\mathrm{A_2B_2}$ | removes positive supercoils ahead of the forks |
| Dam methylase | monomer | methylates GATC; controls the timing of reinitiation |

**Definition 7.4.2 (Helicase)** A **helicase** is a motor protein that uses the energy of nucleoside triphosphate hydrolysis to move along a nucleic acid strand with a defined polarity and separate the strands of a duplex ahead of it. Replicative helicases are hexameric rings that encircle one strand.

**Definition 7.4.3** **Single-stranded DNA-binding proteins** (SSB in bacteria, RPA in eukaryotes) bind single-stranded DNA cooperatively and without sequence specificity, keeping it extended, preventing hairpins and protecting it from nucleases.

Initiation proceeds in three steps. DnaA·ATP assembles on the DnaA boxes into a helical filament around which the DNA is wrapped; the strain this imposes, aided by the negative **supercoiling** of the chromosome ([7.2.3](/7.2.3)), melts the DUE, and DnaA binds the single strands. DnaC then loads one DnaB hexamer on each separated strand, in opposite orientations; loading of the helicases is the **committed step**. Finally DnaG binds DnaB and lays down the first primers, Pol III is loaded, and two forks move away from the origin. DnaB translocates $5' \to 3'$ along the strand it encircles, so at each fork it runs on the lagging-strand template; the first primer made by the DnaG at one fork's helicase primes the leading strand of the opposite fork.

### 7.4.4. Elongation: The Replisome

**Definition 7.4.4 (Replisome)** The **replisome** is the multiprotein complex that replicates DNA at a fork: helicase, primase, the polymerase holoenzyme with its clamps and clamp loader, single-stranded DNA-binding protein, and the enzymes that complete the lagging strand.

The leading-strand polymerase follows the helicase continuously. On the lagging strand the helicase recruits primase every one to two kilobases; the clamp loader places a new β clamp on the fresh primer; the lagging-strand core finishes the previous Okazaki fragment, releases its clamp and jumps to the new one. To let one replisome copy both strands while it moves in one direction, the lagging-strand template is looped out: the loop grows as an Okazaki fragment is made and collapses when the core moves to the next primer, which gave the arrangement the name trombone model. Primers are removed by the $5' \to 3'$ exonuclease of Pol I (and by RNase H), Pol I fills the gap from the $3'$ end of the preceding fragment, and DNA ligase seals the remaining nick using AMP from $\mathrm{NAD^+}$.

![The *E. coli* replication fork moving to the right. DnaB helicase encircles the lagging-strand template and unwinds the parental duplex; DNA gyrase ahead of the fork removes the positive supercoils. DNA polymerase III cores held by β sliding clamps extend the leading strand continuously toward the fork and the lagging strand discontinuously away from it, in Okazaki fragments started from RNA primers laid down by primase (DnaG); SSB coats the exposed single strand. Behind, DNA polymerase I removes each primer by nick translation and DNA ligase seals the nick. Parental strands dark blue, new DNA light blue, RNA primers orange. The loop of the lagging-strand template (trombone) is drawn flat.](./plots/replication-fork.py)

The picture of a rigid, coordinated machine has been revised by single-molecule experiments. Leading- and lagging-strand polymerases in reconstituted *E. coli* replisomes work independently: each can pause or stall while the other continues, and the leading strand advances by bursts and pauses rather than at a constant rate. Polymerase cores also exchange with cores in solution on a time scale of seconds, and in living cells the replisome is a dynamic assembly in which only the helicase stays bound throughout. The physical coupling of the strands through the τ subunits limits how far one strand can run ahead of the other, rather than forcing them to move in lockstep.

## 7.5. Termination and Once-per-Cycle Control

### 7.5.1. Termination

The two forks from *oriC* meet in a terminus region opposite the origin. Ten Ter sites of about $20\,\mathrm{bp}$ (TerA–TerJ), in two oppositely oriented groups, bind the protein Tus. A Tus–Ter complex is polar: it stops a fork arriving from one side, because the helicase moving in that direction strips a strand from the Tus-bound DNA and locks Tus in place, but lets a fork from the other side displace Tus. The groups therefore form a trap that forks can enter but not leave. Deletion of Tus or of the Ter sites is not lethal, since forks usually meet and fuse wherever they collide; the trap limits over-replication when one fork is delayed.

Replication of a circle leaves the daughter chromosomes linked as catenanes, the result of positive supercoils that were converted into intertwinings of the daughters behind the fork ([7.2.3](/7.2.3)). **Topoisomerase** IV, a type II enzyme, unlinks them. If an odd number of crossovers has occurred during recombinational repair ([7.2.9](/7.2.9)), the daughters form one dimeric circle, which the site-specific recombinases XerC and XerD resolve at the *dif* site in the terminus.

### 7.5.2. Initiation Once per Cell Cycle

Initiation is the only step at which bacterial replication is regulated; once forks are established they proceed at nearly constant speed. Three mechanisms keep *oriC* from firing again too soon.

- Sequestration. Immediately after replication, the GATC sites of *oriC* are hemimethylated: the parental strand is methylated, the new strand not yet. The protein SeqA binds hemimethylated GATC clusters and keeps the origin inaccessible to DnaA and to Dam methylase for about a third of the cell cycle (about $10\,\mathrm{min}$ in fast growth). Fully methylated *oriC* can fire; hemimethylated *oriC* introduced into cells cannot.
- Regulatory inactivation of DnaA (RIDA). The protein Hda, bound to β clamps on newly replicated DNA, stimulates hydrolysis of ATP by DnaA, converting the initiator into the inactive DnaA·ADP. Initiation itself thus switches off the initiator.
- Titration and reactivation. The *datA* locus near the origin binds many DnaA molecules and promotes their ATP hydrolysis, and the *dnaA* promoter is itself sequestered and repressed by DnaA; conversely, the DARS sites regenerate DnaA·ATP from DnaA·ADP. The ratio of DnaA·ATP to origins, which rises with cell growth, sets the time of the next initiation.

## 7.6. Replication in Eukaryotes

### 7.6.1. Many Origins, Licensed Once

Eukaryotic chromosomes are linear, large and packaged in **chromatin**, and eukaryotic forks are slow, about $20$–$50\,\mathrm{nt\,s^{-1}}$. Replication therefore starts from many origins: about 400 in budding yeast, where origins are $100$–$200\,\mathrm{bp}$ autonomously replicating sequences (ARS) with an $11\,\mathrm{bp}$ consensus, and $3$–$5\times10^4$ in a human cell, where origins have no **consensus sequence** and are chosen from a larger set of potential sites ([7.2.2](/7.2.2)). Using many origins creates a new problem: each must fire at most once per cell cycle, or parts of the genome would be over-replicated.

**Definition 7.6.1 (Origin Licensing)** **Origin licensing** is the loading, in late mitosis and G1, of the replicative helicase core MCM2–7 onto origins as an inactive head-to-head double hexamer encircling duplex DNA, by the origin recognition complex (ORC), CDC6 and CDT1. The loaded double hexamer is the main part of the **prereplicative complex** (pre-RC). Licensed origins are activated (fired) in S phase; no new licensing is possible until the next G1.

The two steps are separated by the activity of **cyclin-dependent kinases** (CDKs; [7.1.15](/7.1.15)). Licensing can occur only when CDK activity is low (late M and G1). Firing requires high activity of S-phase CDK and of the Dbf4-dependent kinase DDK (CDC7–DBF4): DDK phosphorylates MCM, and CDK phosphorylates the yeast proteins Sld2 and Sld3, which together with Dpb11 recruit CDC45 and the GINS complex to MCM2–7. The result is the active helicase CMG (CDC45–MCM2–7–GINS); the double hexamer separates into two CMGs that each encircle one strand and move in opposite directions. High CDK activity during S, G2 and M also prevents relicensing, by inactivating ORC and CDC6 and, in metazoans, by the protein geminin, which binds CDT1. The cell cycle is thus divided into a window in which origins can be licensed but not fired and a window in which they can be fired but not licensed, so that each origin fires at most once.

### 7.6.2. The Eukaryotic Replisome

CMG translocates $3' \to 5'$ on the leading-strand template, the opposite polarity to DnaB, but the logic of the fork is the same. Three B-family DNA polymerases share the work.

| Enzyme | Subunits | Role | Proofreading |
|---|---|---|---|
| Pol α–primase | 4 (primase PRIM1/PRIM2, polymerase POLA1) | makes an RNA primer of about $10\,\mathrm{nt}$ and extends it with about $20\,\mathrm{nt}$ of DNA, at the origin and for every Okazaki fragment | no |
| Pol ε | 4 | leading-strand synthesis; bound to CMG | yes |
| Pol δ | 3–4 | lagging-strand synthesis; also removes Pol α's DNA and displaces primers | yes |
| PCNA, RFC | trimer, pentamer | sliding clamp and clamp loader | |
| RPA | trimer | single-stranded DNA binding | |
| FEN1, DNA2, ligase I | | cleave the displaced primer flap and seal the nick | |

The division of labor between Pol ε and Pol δ was established in yeast by polymerase mutants with a distinctive error signature, whose mutations appeared on the leading or the lagging strand according to their orientation relative to nearby origins, and by mapping where ribonucleotides incorporated by mutant polymerases end up. In reconstituted yeast replisomes, CMG binds Pol ε and actively excludes Pol δ from the leading strand. Pol δ completes each Okazaki fragment by running into the $5'$ end of the previous one and displacing its primer as a flap, which FEN1 (or, for long flaps, DNA2) removes before ligase I seals the nick. This strand-displacement pathway replaces the nick translation of Pol I.

Eukaryotic replication duplicates chromatin as well as DNA. **Nucleosomes** ahead of the fork are disassembled, helped by the histone **chaperone** FACT that travels with the replisome; the parental H3–H4 tetramers are passed to the two daughter duplexes, in roughly equal numbers, by CMG and Pol α (lagging) and Pol ε (leading), while H2A–H2B dimers are released. New H3–H4 is deposited by the chaperone CAF-1, which binds PCNA, and the spaces are filled with old and new H2A–H2B. The length of eukaryotic Okazaki fragments, close to the nucleosome repeat of about $165$–$200\,\mathrm{bp}$, reflects this coupling: Pol δ stops where it meets a newly assembled nucleosome. Recycling of modified parental **histones** is the starting point for the inheritance of chromatin states ([7.2.15](/7.2.15)).

When converging forks meet, the two CMG complexes pass each other, the remaining gap is filled and the CMGs, now encircling duplex DNA, are removed: their MCM7 subunit is polyubiquitylated (by SCF$^{\mathrm{Dia2}}$ in yeast and CUL2$^{\mathrm{LRR1}}$ in metazoans) and extracted by the ATPase p97 (CDC48). **Topoisomerase** II resolves the intertwined sister chromatids.

### 7.6.3. Telomeres and Telomerase

The lagging strand cannot be completed at the very end of a linear template: removal of the last RNA primer leaves a gap that no polymerase can fill, and even without a primer the lagging-strand machinery needs template beyond the final Okazaki fragment. Each daughter molecule would therefore lose some sequence from one end in every round, the end-replication problem. In addition, the ends are processed by nucleases to leave a single-stranded $3'$ overhang on the G-rich strand. Bacteria avoid the problem with circular chromosomes; eukaryotes cap their linear chromosomes with **telomeres** ([7.2.2](/7.2.2)) and lengthen them with a special reverse transcriptase.

**Definition 7.6.2 (Telomerase)** **Telomerase** is a ribonucleoprotein reverse transcriptase that extends the $3'$ end of the G-rich strand of a telomere by repeatedly copying a short template within its own RNA subunit. Human telomerase consists of the protein TERT and the $451$-nucleotide RNA TR (TERC), whose template region $3'$-CAAUCCCAAUC-$5'$ directs the addition of TTAGGG repeats.

![The end-replication problem and telomerase. A: when the final Okazaki fragment at the end of a linear chromosome is primed and its RNA primer is removed, the lagging-strand daughter is left shorter than its template, with a 3′ overhang of parental DNA; the leading-strand end is later resected to give a G-rich 3′ overhang as well. B: one cycle of telomerase. The 3′ end of the G-rich strand (…GGTTAG-3′) pairs with the 3′ end of the RNA template (3′-CAAUC…); reverse transcription copies the rest of the template, adding GGTTAG; the enzyme then translocates, re-pairing the new 3′ end with the start of the template, and the cycle repeats. The complementary C-rich strand is filled in afterwards by Pol α–primase. Telomerase RNA orange, telomeric DNA blue, newly added DNA light blue.](./plots/telomerase.py)

Elizabeth Blackburn and Carol Greider identified telomerase in extracts of the ciliate *Tetrahymena* (1985), which has tens of thousands of minichromosomes and therefore much telomerase. The enzyme adds repeats processively: after each copy of the template it translocates and re-pairs, so one binding event can add many repeats. The complementary C-rich strand is synthesized by Pol α–primase recruited by the CST complex. In humans telomerase is active in germ cells, stem cells and most cancers (about 85–90 %), but is repressed in most somatic cells, whose telomeres shorten by about $50$–$100\,\mathrm{bp}$ per division (blood-cell telomeres decline from about $11\,\mathrm{kb}$ at birth to about $4\,\mathrm{kb}$ in old age). When some telomeres become critically short they are recognized as DNA damage, and the cell stops dividing (replicative senescence, the Hayflick limit of about 40–60 divisions of cultured human fibroblasts). About 10–15 % of cancers maintain their telomeres without telomerase, by recombination between telomeres (alternative lengthening of telomeres, ALT; [7.2.9](/7.2.9)).

## 7.7. Time, Origins and Errors

### 7.7.1. Replication Time and Multifork Replication

With one origin and two forks at $v \approx 1000\,\mathrm{nt\,s^{-1}}$, the *E. coli* chromosome takes

$$
C = \frac{L}{2v} = \frac{4.64\times10^6}{2\times1000\,\mathrm{s^{-1}}} \approx 2300\,\mathrm{s} \approx 40\,\mathrm{min}, \tag{7.2}
$$
in agreement with the measured C period of about $40\,\mathrm{min}$ at $37^\circ\mathrm{C}$. After replication ends, a further D period of about $20\,\mathrm{min}$ elapses before division. Yet *E. coli* can divide every $20\,\mathrm{min}$. Helmstetter and Cooper (1968) explained the paradox: a cell initiates replication a time $C + D$ before the division that it serves, so when the doubling time $\tau$ is shorter than $C + D$, new rounds start at the origins before earlier rounds have finished. Chromosomes then carry nested forks (multifork replication), and the number of copies of a locus decreases from origin to terminus.

**Proposition 7.7.1 (Cooper–Helmstetter Gene Dosage)** In a steadily growing population with doubling time $\tau$, replication period $C$ and forks moving at constant speed, the average number of copies of a locus at relative position $m$ between the origin ($m = 0$) and the terminus ($m = 1$) is proportional to $2^{C(1-m)/\tau}$. In particular the ratio of origin to terminus copies is

$$
\frac{n_{\mathrm{ori}}}{n_{\mathrm{ter}}} = 2^{C/\tau}. \tag{7.3}
$$

**Proof** A locus at position $m$ is replicated a time $mC$ after the initiation that copies it, and the terminus a time $C$ after initiation. In a population growing exponentially with doubling time $\tau$, the number of copies of a DNA element is proportional to the number of cells that existed when it was copied, so loci copied a time $\Delta t$ earlier are more numerous by $2^{\Delta t/\tau}$. The locus at $m$ is copied a time $(1 - m)C$ before the terminus of the same round, hence its copy number exceeds that of the terminus by $2^{(1-m)C/\tau}$. $\square$

At $\tau = 20\,\mathrm{min}$ the origin is present in four times as many copies as the terminus, so genes near the origin have a higher dosage in fast growth; *E. coli* places its ribosomal RNA operons near *oriC*, and their transcription benefits from this dosage. Sequencing the DNA of a growing culture and plotting read coverage along the chromosome (marker frequency analysis) gives the profile of Proposition 7.7.1 directly, and its slope measures $C/\tau$ (panel A of the next figure).

For a human chromosome of $150\,\mathrm{Mb}$ replicated by a single fork at $50\,\mathrm{nt\,s^{-1}}$, the time would be $3\times10^6\,\mathrm{s}$, about 35 days; with two forks from a central origin, 17 days. An S phase of about $8\,\mathrm{h}$ requires origins every $100\,\mathrm{kb}$ or so if all fired at once. In fact origins fire throughout S phase, in a reproducible but probabilistic temporal program (early-replicating, gene-rich euchromatin and late-replicating **heterochromatin**), and the time to complete replication is a property of the stochastic firing process.

### 7.7.2. Stochastic Origin Firing

A simple model treats initiation as a random process. Origins fire at random positions and times with a rate $I$ per unit length of unreplicated DNA per unit time, and each initiation sends out two forks at speed $v$. The model is a one-dimensional version of the Kolmogorov–Johnson–Mehl–Avrami theory of crystallization (replicated domains play the role of growing crystals).

**Proposition 7.7.2** In this model the fraction of the genome replicated at time $t$ is

$$
f(t) = 1 - \exp\!\left(-I v t^2\right), \tag{7.4}
$$
and the time at which a fraction $1 - \varepsilon$ is replicated is $t_{1-\varepsilon} = \sqrt{\ln(1/\varepsilon)/(Iv)}$.

**Proof** A point $x$ is still unreplicated at time $t$ if and only if no origin has fired at a position $x'$ and time $t' < t$ with $\lvert x - x' \rvert < v(t - t')$: such an origin would have sent a fork past $x$. Initiations in already replicated DNA are impossible, but adding "phantom" initiations there does not change whether $x$ is replicated, because the region of the $(x', t')$ plane that matters lies entirely in unreplicated DNA as long as $x$ itself is unreplicated. The initiations then form a Poisson process in the plane with intensity $I$, and the number falling in the triangle $\{(x', t')\colon 0 < t' < t,\ \lvert x - x'\rvert < v(t - t')\}$, of area $vt^2$, is Poisson with mean $Ivt^2$. The probability that it is zero is $\exp(-Ivt^2)$. $\square$

![Two quantitative views of replication timing. A: gene dosage along the *E. coli* chromosome (Proposition 7.7.1) for doubling times of 20, 40 and 100 minutes with C = 40 min, as the copy number of each locus relative to the terminus, plotted from the origin (oriC, position 0) to the terminus (ter, position 1) on both replichores; at a 20-minute doubling time the origin is present in four copies per terminus. B: a simulated human-like chromosome segment of 10 Mb in which origins fire at random positions and times at a constant rate per unreplicated kilobase (I = 1.5 × 10⁻⁵ kb⁻¹ min⁻¹) and forks move at 1.5 kb/min; each initiation is a dot and its two forks the edges of a growing replicated domain (shaded). C: the replicated fraction of the simulated segment (points) and the Kolmogorov–Johnson–Mehl–Avrami prediction of Eq. (7.4) (line); 99 % of the DNA is replicated after about 7.5 hours, but the last unreplicated gap in this run closes only after almost 9 hours, the random-completion problem.](./plots/replication-kinetics.py)

The model reproduces two features of real S phases. With constant $I$, the last gaps are filled slowly: the unreplicated fraction falls as a Gaussian in $t$, and a large gap far from any fired origin can persist. Cells reduce this random-completion problem by increasing the initiation rate during S phase, so that late gaps are rapidly filled by newly fired origins; measured $I(t)$ in *Xenopus* egg extracts and in human cells rises through most of S phase. A complementary safeguard is that many more origins are licensed than fire: dormant origins near a stalled fork fire and rescue replication of the region.

**Example 7.7.1** For a fork speed of $v = 1.5\,\mathrm{kb\,min^{-1}}$ (about $25\,\mathrm{nt\,s^{-1}}$) and an S phase in which 99 % of the DNA should be replicated in $t = 8\,\mathrm{h} = 480\,\mathrm{min}$, Eq. (7.4) requires $I = \ln 100/(v t^2) = 4.6/(1.5\times480^2) \approx 1.3\times10^{-5}\,\mathrm{kb^{-1}\,min^{-1}}$. The expected number of initiations per kilobase is $\int_0^t I\,[1 - f(t')]\,\mathrm{d}t' \approx \tfrac12\sqrt{\pi I/v} \approx 2.6\times10^{-3}$, one origin per $400\,\mathrm{kb}$, which is four to eight times sparser than the measured density of fired origins in human cells (one per $50$–$100\,\mathrm{kb}$). The discrepancy shows that real cells fire many more origins than a constant-rate process would need, at the cost of more forks but with a far shorter tail of late gaps.

### 7.7.3. The Fidelity Budget

The error rate of replication is the product of the three successive filters ([7.2.1](/7.2.1#sec-1.5)):

$$
\varepsilon \approx \underbrace{10^{-5}}_{\text{base selection}}\times\underbrace{10^{-2}}_{\text{proofreading}}\times\underbrace{10^{-3}}_{\text{mismatch repair}} = 10^{-10}\ \text{per nucleotide}. \tag{7.5}
$$
For *E. coli* this gives $4.6\times10^6\times10^{-10} \approx 5\times10^{-4}$ errors per genome per replication, close to the measured mutation rate of about $1\times10^{-3}$ per genome per generation (about $2\times10^{-10}$ per base pair). Remarkably, the mutation rate per genome is nearly the same, about $0.003$, across DNA-based microbes whose genomes differ a hundredfold in size (Drake's rule), which suggests that the rate per base pair is tuned to the size of the genome rather than pushed to a physical minimum. In human cells, with $6.2\times10^9\,\mathrm{bp}$ per diploid genome, a rate of $10^{-10}$ gives about one replication error per cell division; the germline mutation rate of about $1.2\times10^{-8}$ per base pair per generation corresponds to 60–70 new mutations per child, accumulated over the 20 to 30 germ-cell divisions in each mother and the hundreds of divisions in a father, together with mutations from unrepaired damage ([7.2.8](/7.2.8)).

**Example 7.7.2** A mutation in *dnaQ* that inactivates the ε subunit removes the proofreading factor of $10^{-2}$ to $10^{-3}$, and *dnaQ* (*mutD*) mutants are indeed among the strongest mutator strains known, with mutation rates raised $10^3$–$10^4$-fold. The rise is larger than the loss of proofreading alone because the flood of errors saturates mismatch repair. Mutator alleles of human Pol ε with defective proofreading (for example POLE P286R) cause "ultramutated" colorectal and endometrial tumors with more than $100$ mutations per megabase.

## Summary

| Topic | Key points |
|---|---|
| Mode (Definition 7.1.1) | Semiconservative: Meselson–Stahl CsCl gradients after one generation give one hybrid band, after two hybrid and light in 1:1 (Example 7.1.1); denatured hybrid gives heavy and light strands |
| Geometry (Definitions 7.2.1, 7.2.2) | Fixed origins, usually two forks ($\theta$ structures); leading strand continuous, lagging strand as Okazaki fragments of $1$–$2\,\mathrm{kb}$ (bacteria) or $150$–$200\,\mathrm{nt}$ (eukaryotes); RNA primers by primase (Definition 7.2.3) |
| Chemistry (Definition 7.3.1) | Template + primer, $5' \to 3'$, Eq. (7.1); $3'$-OH attacks the α-phosphate; two $\ce{Mg^2+}$; palm, fingers, thumb; $\mathrm{PP_i}$ hydrolysis drives synthesis |
| Fidelity | Base selection by geometry ($10^{-4}$–$10^{-5}$), proofreading by $3' \to 5'$ exonuclease (Definition 7.3.2, $10^{-2}$–$10^{-3}$), mismatch repair ($10^{-2}$–$10^{-3}$); overall about $10^{-10}$, Eq. (7.5) |
| *E. coli* polymerases | Pol I (Klenow fragment + $5' \to 3'$ exo; primer removal), Pol II, Pol III (αεθ core, $\tau_3\delta\delta'\chi\psi$ clamp loader, β clamp, Definition 7.4.1; $1000\,\mathrm{nt\,s^{-1}}$, processivity $> 5\times10^5$, Definition 7.3.4), Pol IV and V (translesion) |
| Initiation | *oriC* $245\,\mathrm{bp}$: DnaA boxes, DUE, 11 GATC; DnaA·ATP melts DUE, DnaC loads DnaB helicase (Definition 7.4.2) on each strand, DnaG primes; SSB (Definition 7.4.3), gyrase |
| Replisome (Definition 7.4.4) | Trombone loop of lagging-strand template; primers removed by Pol I and RNase H, nicks sealed by ligase; polymerases act independently and exchange |
| Termination and control | Ter–Tus polar traps; catenanes unlinked by topo IV; dimers resolved by XerCD at *dif*; reinitiation blocked by SeqA sequestration of hemimethylated *oriC*, RIDA (Hda), *datA*, and regenerated by DARS |
| Eukaryotes | Licensing of MCM2–7 double hexamers by ORC, CDC6, CDT1 in G1 (Definition 7.6.1); firing by DDK and S-CDK forms CMG; Pol α–primase primes, Pol ε leading, Pol δ lagging; PCNA, RFC, RPA, FEN1, ligase I; histone recycling, CAF-1, FACT; CMG unloading by ubiquitylation and p97 |
| Telomeres | End-replication problem; telomerase (Definition 7.6.2) copies $3'$-CAAUCCCAAUC-$5'$ into TTAGGG repeats; somatic shortening, senescence; telomerase in 85–90 % of cancers, ALT in the rest |
| Quantitative | $C = L/2v \approx 40\,\mathrm{min}$ (Eq. (7.2)); multifork replication and dosage $2^{C(1-m)/\tau}$ (Proposition 7.7.1); stochastic firing $f = 1 - \mathrm{e}^{-Ivt^2}$ (Proposition 7.7.2, Example 7.7.1); about $10^{-3}$ errors per *E. coli* genome per replication, Drake's rule |

## Questions

1. Meselson and Stahl's cells grew asynchronously. If heavy-labeled cells are transferred to light medium and DNA is analyzed after $1.5$ generations, what bands are expected under the semiconservative model, and in what proportions?

   **Answer** Count in units of the initial amount of DNA. After $1.5$ generations there are $2^{1.5} \approx 2.83$ units of duplex DNA, which contain the original heavy strands, equivalent to $1$ unit of duplex. In an exponentially growing culture practically every original molecule has been replicated once by this time, so every heavy strand is paired with a new light strand: the hybrid DNA amounts to $2$ units ($2/2.83 \approx 71\,\%$) and light DNA to the remaining $0.83$ units ($29\,\%$). No heavy band remains. Meselson and Stahl's photographs indeed show a dominant hybrid band with a growing light band between one and two generations.

2. Why can't a polymerase synthesize DNA $3' \to 5'$ by using nucleoside $5'$-monophosphates and a triphosphate on the $3'$ end of the growing chain? What would happen to proofreading?

   **Answer** Such an enzyme is chemically conceivable: the $5'$-OH or $5'$-phosphate of an incoming nucleotide could attack a $3'$-triphosphate at the chain end, releasing pyrophosphate. But the activating group would then sit on the chain. When a wrong nucleotide had to be removed by an exonuclease, its removal would leave an end without a triphosphate, and synthesis could not continue without a separate enzyme to reactivate the end. In $5' \to 3'$ synthesis each incoming dNTP brings its own activation, so the chain end is always an unactivated $3'$-OH that can be trimmed and extended indefinitely. The fact that all polymerases work $5' \to 3'$ is thus a consequence of the need for proofreading.

3. In a strain with a temperature-sensitive DNA ligase, cells are pulse-labeled with $[^3\mathrm{H}]$thymidine at the restrictive temperature and the DNA is analyzed on alkaline sucrose gradients. What is observed, and what does it show?

   **Answer** Alkali denatures DNA, so the gradient separates single strands by length. Without ligase, Okazaki fragments are not joined, and the label appears in a slowly sedimenting peak of short strands of $1$–$2\,\mathrm{kb}$ in addition to the long strands of the leading strand. The short pieces persist during a chase. This shows that discontinuous synthesis occurs and that ligase joins the fragments; with wild-type ligase the short pieces are seen only after very short pulses.

4. Using the data for the *E. coli* replisome, estimate (a) the number of Okazaki fragments made per chromosome, (b) the number of primers per second at one fork, and (c) the number of helical turns that must be removed per chromosome.

   **Answer** (a) Each fork's lagging strand covers half of one strand of the chromosome on each replichore; together the two lagging strands cover $4.64\times10^6\,\mathrm{nt}$. With fragments of $1$–$2\,\mathrm{kb}$ this is $2300$–$4600$ fragments. (b) At $1000\,\mathrm{nt\,s^{-1}}$ a new primer is needed every $1$–$2\,\mathrm{s}$ at each fork. (c) $4.64\times10^6/10.5 \approx 4.4\times10^5$ turns, removed by gyrase and topoisomerase IV ([7.2.3](/7.2.3)).

5. Explain why hemimethylated *oriC* cannot initiate replication, and predict the phenotype of a *dam* mutant and of a *seqA* mutant.

   **Answer** After a round of replication the GATC sites of *oriC* are methylated only on the parental strand. SeqA binds hemimethylated GATC clusters with high affinity and covers *oriC* and the *dnaA* promoter, preventing DnaA binding and Dam methylation for about a third of the cell cycle; this enforces a refractory period. In a *seqA* mutant the origin is not sequestered, and cells reinitiate too soon and asynchronously, so their origin number is irregular. In a *dam* mutant no GATC is methylated, so there is no hemimethylated state to sequester: initiation is also asynchronous. Both mutants are viable, showing that sequestration is one of several layers of control (with RIDA and *datA*). A *dam* mutant also loses strand discrimination in mismatch repair and is a mutator ([7.2.8](/7.2.8)).

6. A human cell line has a deletion that removes half of its potential origins but leaves the licensing machinery intact. Using the model of 7.7.2, how would the length of S phase change if cells compensated by firing the remaining origins at twice the rate? What would happen if they could not compensate?

   **Answer** In Eq. (7.4) only the product $Iv$ matters. If the remaining origins fire at twice the rate per origin, the initiation rate per unit length $I$ is unchanged, and S phase is unaffected. If they cannot compensate, $I$ halves and the time to reach any fixed replicated fraction grows by a factor $\sqrt2$, from about $8$ to about $11\,\mathrm{h}$. Large gaps between active origins would take especially long, and stalled forks in them could not be rescued by dormant origins, increasing the risk of under-replicated DNA entering mitosis, a source of chromosome breaks.

7. (Open question) Telomerase-negative mice (lacking the RNA subunit) are viable for several generations, and only later generations show defects. Explain this observation and what it implies for the use of telomerase inhibitors in cancer therapy.

   **Answer** Laboratory mice have very long telomeres ($20$–$50\,\mathrm{kb}$). Without telomerase they lose sequence each division, but it takes several generations before telomeres become critically short in proliferating tissues; then germ cells, blood and gut fail and fertility drops. The lag shows that telomerase acts on telomere length, not on immediate survival. For cancer therapy this implies that a telomerase inhibitor would kill tumor cells only after many divisions, when their (often already short) telomeres become critical, that normal stem cells would also be affected, and that tumors could escape by switching to ALT; inhibitors are therefore studied mainly in combination with other treatments.
