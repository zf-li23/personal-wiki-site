---
title: "Transcriptional Regulation in Bacteria: Operons and Phage"
description: Operons and polycistronic mRNA; cis- and trans-acting mutations and the partial-diploid test; negative control of the lac operon (lacI⁻, lacIˢ and lacOᶜ mutants, filter binding and footprinting, the repressor tetramer and DNA looping among O1, O2 and O3); positive control by cAMP–CAP (contacts with the α-CTD, DNA bending, class I and II promoters), catabolite repression and inducer exclusion; the trp repressor and attenuation; phage λ (three phases of transcription, N and Q antitermination, establishment and maintenance of lysogeny, the operator O_R, CI and Cro, induction); the thermodynamic model of promoter occupancy (simple repression, activation, induction by an MWC repressor, DNA looping and its 10.5 bp periodicity, the Shea–Ackers model of O_R).
---

A bacterium cannot afford to make every protein all the time: synthesizing a protein of average length costs on the order of a thousand ATP equivalents, and an *E. coli* cell growing on glucose has no use for the enzymes that break down lactose, arabinose or maltose. Most such decisions are taken at the first step of gene expression, the initiation of **transcription** described in [7.2.10](/7.2.10), where stopping wastes the least. This chapter is about the logic of that control, worked out in three systems that became the paradigms of molecular biology: the *lac* operon, which showed that genes are switched by proteins binding DNA near **promoters** (Jacob and Monod, 1961) and that one promoter can integrate two signals; the *trp* operon, which added a second, purely transcriptional mechanism, attenuation; and phage λ, whose choice between killing and lying dormant in its host was the first genetic switch understood in molecular detail. The chapter proceeds from the genetic logic of operons (11.1) to negative (11.2) and positive (11.3) control of *lac*, attenuation (11.4) and the λ switch (11.5), and ends with the thermodynamic model (11.6), which turns the cartoons into equations and predicts how much a gene is expressed from the numbers of regulator molecules and their binding energies. The model uses the **Boltzmann distribution** and the binding analysis of [7.1.7](/7.1.7); its kinetic counterpart and the search of regulators for their sites follow in [7.2.22](/7.2.22), and the network-level consequences of these circuits (bistability, feedback, noise) in [7.9](/7.9).

## 11.1. Operons

### 11.1.1. One Promoter, Several Genes

In bacteria, genes whose products work together are often adjacent and transcribed from a single promoter into one mRNA, which ribosomes translate from several start codons.

**Definition 11.1.1 (Operon)** An **operon** is a group of adjacent genes transcribed from one promoter into a single mRNA, together with the control sites that regulate this transcription. An mRNA that carries the coding sequences of several genes is a **polycistronic mRNA**.

The *lac* operon contains three genes: *lacZ*, encoding β-galactosidase, which hydrolyzes lactose to galactose and glucose; *lacY*, encoding lactose permease, which imports lactose with a proton; and *lacA*, encoding galactoside transacetylase, which acetylates nonmetabolizable galactosides and may help detoxify them. A single promoter and one polycistronic mRNA ensure that the products are made in fixed proportions and under one control. When *E. coli* grows on a mixture of glucose and lactose, it first uses glucose; then growth pauses while the *lac* enzymes are made, and resumes on lactose. Monod called this two-phase growth *diauxie*. It contains both kinds of control described in this chapter: the operon is switched on only when lactose is present (negative control, by a repressor) and only when glucose is absent (positive control, by an activator).

**Definition 11.1.2** A **repressor** is a protein that prevents transcription of a gene by binding a DNA site near its promoter; the site it binds in an operon is the **operator**. An **activator** is a protein that stimulates transcription by binding a DNA site near a promoter and helping RNA polymerase initiate. A small molecule that inactivates a repressor, and so turns on transcription, is an **inducer**; one that activates a repressor, and so turns transcription off, is a **corepressor**.

The terms refer to the direction of control: in negative control the regulator stops a gene that would otherwise be expressed (a brake), and in positive control the regulator is required to start a gene that would otherwise be silent (an accelerator). In both, the regulator acts only when bound to DNA, and its ability to bind is changed by a small-molecule **ligand**: regulators are **allosteric proteins** ([7.1.7](/7.1.7)).

### 11.1.2. Cis and Trans

Two kinds of regulatory mutations can be distinguished by genetics alone, without knowing anything about molecules.

**Definition 11.1.3** A **cis-acting element** is a DNA sequence that affects only the expression of genes on the same DNA molecule (operators, promoters, terminators); it acts as DNA and is not expressed as RNA or protein. A **trans-acting factor** is a diffusible product, RNA or protein, that can act on target genes on any DNA molecule in the cell.

The test is the *partial diploid* (merodiploid): a cell carrying two copies of the region, one on the chromosome and one on an F′ **plasmid**, with different mutations. A mutation in a trans-acting factor is complemented by a wild-type copy on the other molecule, because the wild-type product diffuses to both; a mutation in a cis-acting element affects only the genes physically linked to it, whatever is on the other molecule. The argument also runs in reverse: if a mutation acts only in cis, it must work through the DNA itself; if it acts in trans, it must work through a diffusible product.

## 11.2. Negative Control of the lac Operon

### 11.2.1. The Genetic Evidence

The natural inducer is not lactose but *allolactose* (galactose β1→6 glucose), made from lactose by a side reaction of β-galactosidase, which occasionally transfers the galactose to the 6-hydroxyl of glucose instead of to water. In the laboratory the operon is induced with isopropyl β-D-thiogalactoside (IPTG), which binds the repressor but is not a **substrate** of β-galactosidase: it is a *gratuitous inducer*, whose concentration stays constant. A trace of the *lac* products is always present, which is how lactose can enter and be converted to allolactose before the operon is induced.

Jacob and Monod found three classes of regulatory mutants and analyzed them in partial diploids.

| Genotype (chromosome / F′) | β-galactosidase − inducer | + inducer | Conclusion |
|---|---|---|---|
| $I^+ O^+ Z^+$ | low | high | Wild type: inducible |
| $I^- O^+ Z^+$ | high | high | Constitutive: *lacI* encodes a negative regulator |
| $I^- O^+ Z^+ \,/\, I^+ O^+ Z^-$ | low | high | $I^+$ is dominant and acts in trans: a diffusible repressor |
| $I^{\mathrm{s}} O^+ Z^+$ | low | low | Super-repressor: cannot bind inducer, never induced |
| $I^{\mathrm{s}} O^+ Z^+ \,/\, I^+ O^+ Z^+$ | low | low | $I^{\mathrm{s}}$ is dominant in trans: it binds both operators |
| $I^+ O^{\mathrm{c}} Z^+$ | high | high | Operator-constitutive: the repressor cannot bind |
| $I^+ O^{\mathrm{c}} Z^- \,/\, I^+ O^+ Z^+$ | low | high | Constitutive expression appears only from the $Z$ linked to $O^{\mathrm{c}}$: |
| $I^+ O^{\mathrm{c}} Z^+ \,/\, I^+ O^+ Z^-$ | high | high | the operator acts in cis |

The constitutive $O^{\mathrm{c}}$ mutations mapped next to *lacZ*, and an operator that acts only in cis had to be a DNA site, not a gene product. A further class, $I^{-\mathrm{d}}$, is dominant negative: these repressors cannot bind DNA but still form tetramers, and mixed tetramers with wild-type **subunits** are inactive, so they override a wild-type *lacI* in trans. Jacob and Monod concluded that *lacI* encodes a repressor that binds the operator and prevents transcription of *lacZYA*, and that the inducer binds the repressor and releases it; this was a prediction about molecules made from genetics, and it was confirmed when the repressor was isolated.

### 11.2.2. The Biochemical Evidence

Gilbert and Müller-Hill (1966) purified the lac repressor by its ability to bind radioactive IPTG in equilibrium dialysis, from a strain that overproduced it (a wild-type cell contains only about ten tetramers).

**Example 11.2.1 (The repressor binds the operator)** Riggs, Cohn and colleagues (1970) mixed ${}^{32}\mathrm{P}$-labeled DNA containing the *lac* operator with increasing amounts of repressor and measured the complex by nitrocellulose filter binding ([7.2.6](/7.2.6)). Binding increased with repressor and reached half saturation at about $10^{-13}\,\mathrm{M}$ in the low-salt buffer used; with IPTG the curve shifted to far higher repressor concentrations. In a second design, three labeled DNAs were compared: DNA with the wild-type operator bound repressor tightly, DNA with an $O^{\mathrm{c}}$ operator required much more repressor, and DNA without an operator bound only at very high concentration. The **biochemistry** thus reproduced the genetics: the repressor binds the operator, the inducer releases it, and $O^{\mathrm{c}}$ mutations weaken binding. The same experiments gave an association rate constant of about $7\times10^9\,\mathrm{M^{-1}\,s^{-1}}$, higher than the limit for a **diffusion-controlled reaction** between the repressor and a $20\,\mathrm{bp}$ target, which led to the idea of **facilitated diffusion** along DNA ([7.2.22](/7.2.22)).

Gilbert and Maxam (1973) located the operator by **DNase I footprinting** and by sequencing the protected fragment: the repressor covers about $26\,\mathrm{bp}$ around $+11$, overlapping the start site. The operator is nearly palindromic, as expected for a site bound by two symmetrically arranged subunits.

**Definition 11.2.1** The lac repressor (LacI) is a tetramer of identical $360$-residue subunits. Each subunit has an N-terminal *headpiece* with a **helix–turn–helix** DNA-binding motif, a hinge helix that inserts into the minor groove at the center of the operator, a core domain that binds the inducer, and a C-terminal helix; the C-terminal helices of four subunits form a bundle that holds two dimers together, each dimer binding one operator.

Inducer binding changes the relative orientation of the two core subdomains and, through the hinge, of the two headpieces of a dimer, so that they no longer fit the two half-sites; affinity for the operator falls about a thousandfold, while nonspecific DNA binding is barely affected. This is the allosteric transition of an **MWC model** with two states, a DNA-binding and a non-binding conformation (11.6.3).

### 11.2.3. Three Operators and DNA Looping

Why is the repressor a tetramer, when one dimer covers an operator? The *lac* region has two auxiliary operators that resemble the main one: $O_2$ centered at $+412$ within *lacZ*, and $O_3$ centered at $-82$, just upstream of the CAP site. The classical operator is called $O_1$.

**Example 11.2.2 (The auxiliary operators cooperate in repression)** Oehler, Müller-Hill and colleagues (1990) placed *lac* regions with all combinations of wild-type and deleted operators into the *E. coli* chromosome (by λ lysogenization) in a strain with a wild-type *lacI* and measured repression, the ratio of β-galactosidase with and without IPTG. With all three operators repression was $1300$-fold; with $O_1$ and $O_2$ it was $700$-fold, with $O_1$ and $O_3$ $440$-fold; with $O_1$ alone only $18$-fold; with $O_2$ and $O_3$ but no $O_1$, $1.9$-fold, and with $O_2$ or $O_3$ alone none. Removing either auxiliary operator decreased repression only slightly, but removing both decreased it about $50$-fold.

$O_1$ is the operator that blocks transcription, but the auxiliary operators raise its occupancy: a tetramer bound at $O_2$ or $O_3$ holds its second dimer near $O_1$, and when both dimers are bound the DNA between them forms a loop ($93\,\mathrm{bp}$ from $O_3$ to $O_1$, $401\,\mathrm{bp}$ from $O_1$ to $O_2$). The crystal structure of the repressor with two operator fragments (Lewis and colleagues, 1996) showed the tetramer as a V whose two dimers bind separate operators independently, as looping requires. *DNA looping* is the general principle: a protein or complex bound at two sites on the same DNA brings them together, and the second site sees an effective concentration of the first set by the flexibility of the intervening DNA (11.6.4).

How does the repressor stop transcription? In the simplest view, repressor and polymerase compete for overlapping sites ($O_1$ overlaps the start site and the downstream part of the promoter). Experiments at high concentrations in vitro suggested instead that polymerase could bind in the presence of repressor and be locked into **abortive initiation** (Lee and Goldfarb, 1991); kinetic experiments under conditions closer to those in vivo (Schlax, Record and colleagues, 1995) showed that repressor prevents the polymerase from rebinding after it dissociates, as expected for competition, and in vivo measurements agree. The competition (steric occlusion) model is now the accepted one for *lac*.

![The lac control region and repression by looping. A: map of the lac operon drawn with SBOL Visual glyphs: lacI with its own promoter, the auxiliary operator O3 (centered at −82), the CAP site (−61.5), the lac promoter, the main operator O1 (+11) overlapping the start site, and lacZ with the second auxiliary operator O2 (+412) inside it, followed by lacY and lacA; the polycistronic mRNA is shown below. B: the repressor tetramer bound to O1 with one dimer and to O3 (or O2) with the other, the 93 bp of DNA between them, which contain the CAP site and the promoter, forming a loop](./plots/lac-control-region.py)

## 11.3. Positive Control of the lac Operon

### 11.3.1. Catabolite Repression and cAMP

**Definition 11.3.1** **Catabolite repression** is the reduced expression of operons for the use of alternative carbon sources when a preferred carbon source, glucose in *E. coli*, is available.

In 1965 Makman and Sutherland found that **cyclic AMP** (cAMP) is abundant in *E. coli* starved of glucose and scarce in cells growing on it, and Perlman and Pastan (1968) showed that adding cAMP to the medium overcame catabolite repression of the *lac*, galactose and *ara* operons. Mutants defective in adenylate cyclase (*cya*) could not induce these operons unless cAMP was added, and a second class of mutants (*crp*) could not induce them even with cAMP; the *crp* gene encodes the protein through which cAMP acts.

**Definition 11.3.2** The **catabolite activator protein** (CAP), also called cAMP receptor protein (CRP), is a dimeric activator of *E. coli* that binds cAMP and, as the CAP–cAMP complex, binds specific DNA sites and stimulates transcription from more than a hundred promoters.

**Example 11.3.1 (CAP and cAMP are both required)** Zubay and colleagues (1970) synthesized β-galactosidase in cell-free extracts from *lac* DNA (on a transducing phage) with increasing cAMP. With an extract from wild-type cells, β-galactosidase synthesis increased steeply with cAMP; with an extract from a *crp* mutant it stayed at the basal level at all cAMP concentrations, and adding purified CAP restored the response. The activator is the CAP–cAMP complex, not cAMP itself. (The current name corrects the historical "catabolite gene activator protein"; the protein activates genes for **catabolism** of other sugars, and the name has nothing to do with "catabolic activator".)

### 11.3.2. How CAP Activates

CAP–cAMP binds a $22\,\mathrm{bp}$ site centered at $-61.5$ of the *lac* promoter (between two **base pairs**), and mutations in this site that prevent CAP binding prevent activation. Two features explain activation.

First, CAP contacts the polymerase. CAP and polymerase cosediment in the presence of cAMP, their footprints are adjacent, CAP mutations in a surface patch called activating region 1 (AR1) abolish activation without affecting DNA binding, and polymerase lacking the α-CTD (Example 10.3.1) is not activated. A crystal structure of CAP–cAMP, α-CTD and DNA (Benoff, Ebright and colleagues, 2002) shows AR1 of the downstream CAP subunit touching one α-CTD, which is also bound to DNA next to the CAP site, while the other α-CTD binds DNA alone. CAP thus recruits the polymerase by providing an additional binding surface for the α-CTD, the same **domain** that binds **UP elements**: in the language of Formula 10.4.1, CAP at *lac* lowers $K_{\mathrm{c}}$, with the interaction worth a few **thermal energy** units ($k_{\mathrm{B}}T$).

Second, CAP bends the DNA by about $90^\circ$ (Schultz, Shields and Steitz, 1991), which wraps the upstream DNA toward the polymerase and helps the proteins and DNA in the complex make their contacts.

CAP-dependent promoters fall into two classes. At *class I* promoters (*lac*), the CAP site is upstream of the −35 element, at $-61.5$ or one or more helical turns further ($-71.5$, $-82.5$, $-92.5$), always on the same face of the helix, and activation is through the α-CTD alone. At *class II* promoters (such as P1 of the galactose operon), the CAP site at $-41.5$ overlaps the −35 element; CAP contacts the α-CTD through AR1, the α-NTD through AR2 and σ region 4 through AR3, and accelerates isomerization (raises $k_2$) as well as binding. Many bacterial activators use one of these two architectures, and the α-CTD is their common target.

**Remark 11.3.1 (The ara operon)** The *ara* operon, controlled by AraC, shows the same parts used differently. In the absence of arabinose an AraC dimer binds the site $O_2$, about $270\,\mathrm{bp}$ upstream of the $P_{\mathrm{BAD}}$ promoter, and the half-site $I_1$, looping about $210\,\mathrm{bp}$ of DNA and repressing; arabinose changes the conformation of AraC so that it binds $I_1$ and $I_2$ next to the promoter and activates $P_{\mathrm{BAD}}$, together with CAP–cAMP. Inserting half a helical turn ($5\,\mathrm{bp}$) between $O_2$ and $I_1$ abolished repression, and a full turn ($11\,\mathrm{bp}$) restored it (Lee and Schleif, 1989): looping requires both sites on the same face of the helix, a dependence on phase that the model of 11.6.4 explains. The $P_{\mathrm{BAD}}$ promoter with AraC is widely used for tunable expression.

### 11.3.3. Two Signals, One Promoter

The *lac* promoter is weak by itself (its −35 and −10 elements match the consensus poorly) and needs CAP; it is also blocked by the repressor. It is therefore strongly expressed only when lactose is present AND glucose is absent:

| Glucose | Lactose | Repressor | CAP–cAMP | Expression |
|---|---|---|---|---|
| + | − | Bound | Low | Off (basal) |
| − | − | Bound | High | Off (basal) |
| + | + | Released, but little inducer enters | Low | Low |
| − | + | Released | High | High (about $1000$ times basal) |

The textbook account explains the third row by low cAMP in glucose-grown cells. Measurements since the 1990s showed that cAMP levels differ less between glucose and lactose growth than this implies, and that the main mechanism of the glucose effect on *lac* is *inducer exclusion*.

**Definition 11.3.3 (Inducer Exclusion)** **Inducer exclusion** is the inhibition of the uptake of an inducer, and so of induction, by a preferred carbon source; in *E. coli* the unphosphorylated glucose-specific enzyme IIA of the phosphotransferase system (EIIA$^{\mathrm{Glc}}$), which accumulates while glucose is transported, binds and inhibits lactose permease and other sugar permeases.

The same protein links both mechanisms: phosphorylated EIIA$^{\mathrm{Glc}}$, which predominates when glucose is absent, activates adenylate cyclase, so that glucose transport both lowers cAMP and excludes the inducer. The *lac* system also contains positive feedback, because the permease that the operon encodes imports its own inducer; at low inducer concentration this makes the response of single cells all-or-none, a bistability first seen by Novick and Weiner (1957) and analyzed in [7.9](/7.9). The diagram below collects the interactions as an SBGN activity-flow map, together with those of the *trp* operon and phage λ.

![Regulatory logic of the three systems of this chapter as SBGN Activity Flow maps (arrows with open heads: positive influence; bars: negative influence; AND, NOT: logical operators; hexagons: phenotypes). A: the lac operon: lactose enters through LacY and is converted by LacZ into allolactose, which inactivates LacI; transcription of lacZYA requires CAP–cAMP AND NOT LacI; glucose transport inhibits adenylate cyclase (CyaA) and, by inducer exclusion, LacY; the products LacY and LacZ feed back positively on induction. B: the trp operon: tryptophan activates the TrpR repressor (corepressor) and, through charged tRNA$^{\mathrm{Trp}}$, promotes termination at the attenuator; both inhibit trpEDCBA, whose enzymes make tryptophan (a double negative feedback). C: phage λ: CII activates PRE and so cI; CI represses PR and PL (cro, N and the early genes), activates its own PRM at low concentration and represses it at high concentration; Cro represses PRM; CIII protects CII from the protease FtsH; DNA damage activates RecA, which induces cleavage of CI; N and Q are antiterminators for the delayed-early and late genes; the mutual repression of cI and cro selects lysogeny or lysis](./plots/regulation-maps.py)

## 11.4. The trp Operon and Attenuation

### 11.4.1. Repression

The *trp* operon (*trpEDCBA*) encodes the five enzymes of tryptophan synthesis from chorismate. Its control is the mirror image of *lac*: the gene product is the corepressor. The *trpR* gene, elsewhere on the chromosome, encodes an *aporepressor*, a dimer that binds the *trp* operator only when it has bound tryptophan, whose binding rotates the two **helix–turn–helix** **motifs** of the dimer into the spacing of the **major grooves** of the operator. When tryptophan is abundant, the repressor binds the operator, which overlaps the promoter, and reduces transcription about $70$-fold. TrpR also represses *aroH* and its own gene.

### 11.4.2. Attenuation

Yanofsky found that *trpR* mutants still regulate the operon about tenfold in response to tryptophan, and that the control acts after initiation: most transcripts started in tryptophan-rich cells end in a $162$-nt leader region before *trpE*.

**Definition 11.4.1 (Attenuation)** **Attenuation** is the regulation of transcription by premature termination at a terminator (the *attenuator*) in the leader region of an operon, where the decision to terminate or to read through depends on the alternative secondary structures of the nascent leader RNA.

The *trp* leader RNA contains four segments that can pair in two ways: 1 with 2 and 3 with 4, or 2 with 3. The 3:4 **hairpin**, followed by a run of U, is an **intrinsic terminator** ([7.2.10](/7.2.10)); the 2:3 hairpin (the *antiterminator*) prevents it from forming. The leader also encodes a $14$-residue leader **peptide** (MKAIFVLKGWWRTS) with two adjacent tryptophan codons in segment 1. Because bacterial translation starts while the RNA is being made, a ribosome follows the polymerase on the leader, and its position decides which hairpin forms.

- Tryptophan abundant: the ribosome translates through the Trp codons and stops at the leader stop codon, between segments 1 and 2, covering segment 2; segments 3 and 4 then pair as soon as 4 is made, and the polymerase terminates at the attenuator.
- Tryptophan scarce: the ribosome stalls at the two Trp codons waiting for charged tRNA$^{\mathrm{Trp}}$, covering segment 1; segment 2 pairs with 3 when 3 is made, the terminator cannot form, and the polymerase transcribes into *trpE*.
- No translation (e.g., no ribosome loads): segments 1:2 and 3:4 pair, and transcription terminates.

![Attenuation in the trp leader. The leader RNA (drawn 5′ to 3′ behind the polymerase) has four segments: 1 (containing the two Trp codons of the leader peptide), 2, 3 and 4 (followed by U8). A: with abundant tryptophan, the ribosome reaches the leader stop codon and covers segment 2; the 3:4 hairpin forms and terminates transcription at the attenuator. B: with scarce tryptophan, the ribosome stalls at the Trp codons in segment 1; segment 2 pairs with 3 (antiterminator), the 3:4 terminator cannot form, and the polymerase continues into trpE. C: without a translating ribosome, 1:2 (a pause hairpin) and 3:4 form and transcription terminates](./plots/trp-attenuation.py)

The timing works because the polymerase pauses after making the 1:2 hairpin, about $90$ nt into the leader, a NusA-stimulated pause that waits until a ribosome has initiated on the leader peptide and released it; from then on the ribosome follows closely enough to control the folding of segments 2–4. Repression and attenuation multiply: about $70$-fold by the repressor times about $10$-fold by attenuation gives a range of about $700$-fold. Attenuation senses charged tRNA$^{\mathrm{Trp}}$ rather than tryptophan itself, and so responds to the supply of tryptophan for protein synthesis. The *his* operon has seven His codons in a row in its leader and relies on attenuation alone; leaders of other amino-acid operons work the same way. In *Bacillus subtilis*, the trp leader is controlled differently, by an RNA-binding protein, TRAP, which binds tryptophan and then the leader, favoring the terminator, and many genes in bacteria are attenuated by riboswitches, leader RNAs that change structure on binding a metabolite directly ([7.2.18](/7.2.18)).

## 11.5. Phage λ: A Genetic Switch

### 11.5.1. Lysis or Lysogeny

**Definition 11.5.1** A **temperate phage** can follow either of two pathways after infecting a bacterium: the *lytic* pathway, in which it replicates, produces progeny and lyses the host, or **lysogeny**, in which its genome is maintained in the host, usually integrated into the chromosome as a **prophage**, with the lytic genes repressed; a bacterium carrying a prophage is a *lysogen*.

Phage λ of *E. coli* has a linear genome of $48.5\,\mathrm{kb}$ with **cohesive ends** that circularizes on entry. In a lysogen, the λ repressor CI, the product of *cI*, keeps nearly all other phage genes silent; the prophage is replicated passively with the chromosome. The lysogen is immune to superinfection by λ, because the repressor present in the cell binds the operators of the incoming genome; virulent mutants (λvir) with mutations in the operators escape this immunity. When the host DNA is damaged, the prophage is induced: it excises and enters the lytic pathway, abandoning a host that may not survive.

### 11.5.2. Lytic Development: Three Phases of Transcription

Lytic infection proceeds in three phases, each turned on by a product of the previous one.

- Immediate early: host polymerase transcribes from the leftward and rightward promoters $P_{\mathrm{L}}$ and $P_{\mathrm{R}}$ until the first terminators, $t_{\mathrm{L1}}$ and $t_{\mathrm{R1}}$. The products are N (leftward) and Cro (rightward).
- Delayed early: N is an antiterminator; with it, transcription from $P_{\mathrm{L}}$ and $P_{\mathrm{R}}$ continues through the terminators into the delayed-early genes: *cII* and *O*, *P* (replication), *Q* to the right; *cIII*, *gam*, *red* (recombination), *xis* and *int* (excision and integration) to the left.
- Late: Q is a second antiterminator acting on transcripts from the late promoter $P_{\mathrm{R}'}$, which reads through a terminator into the head, tail and lysis genes (about $26\,\mathrm{kb}$ transcribed as one unit).

Regulating by **antitermination** rather than by new promoters has an advantage: the same promoters serve each phase, and the genes of a phase are expressed together as soon as their antiterminator appears.

**Example 11.5.1 (N acts on RNA, at nut)** N works only on polymerases that have transcribed a *nut* site (N utilization) located downstream of $P_{\mathrm{L}}$ and $P_{\mathrm{R}}$; the antitermination is thus specific for λ transcripts. *nut* is recognized as RNA: it consists of *boxA*, a short sequence also present in rRNA leaders, and *boxB*, a hairpin bound by the arginine-rich motif of N. N assembles with host factors NusA, NusB, NusG and NusE (ribosomal protein S10) on the polymerase, which then reads through intrinsic and ρ-dependent terminators for thousands of base pairs. Cross-linking showed how: a photoreactive nucleotide placed at different positions of a terminator RNA cross-linked to both NusA and N when it lay between $18$ and $24$ nt from the $3'$ end, the region of the upstream half of the terminator hairpin, and with two mutations that prevent the hairpin from forming, the downstream half was not cross-linked (Gusarov and Nudler, 2001). Without N, the upstream half of a nascent terminator hairpin binds an upstream **binding site** of the polymerase, and NusA helps release it so that the hairpin forms (NusA stimulates termination); N bound to the same RNA, together with NusA, holds it and slows hairpin formation, so the polymerase escapes the terminator. **Cryo-electron microscopy** of the complete N–Nus–polymerase complex (2017) showed N threading along the polymerase to the RNA exit channel, where it blocks hairpin invasion and suppresses pausing.

Q acts differently: it binds a DNA site (*qut*) within $P_{\mathrm{R}'}$ and is loaded onto a polymerase paused at $+16$/$+17$ by σ region 2 binding a −10-like sequence in the transcribed DNA, the σ-dependent pause of [7.2.10](/7.2.10); once loaded, Q travels with the polymerase and makes it resistant to termination.

### 11.5.3. Establishing Lysogeny

After infection both the lytic and the lysogenic program begin, because the immediate- and delayed-early genes are needed for both. The decision rests on CII, an activator made from the $P_{\mathrm{R}}$ transcript. CII activates three promoters: $P_{\mathrm{RE}}$ (repressor establishment), from which *cI* is transcribed leftward; $P_{\mathrm{I}}$, for *int*; and $P_{\mathrm{aQ}}$, which makes an antisense RNA against *Q*. The $P_{\mathrm{RE}}$ transcript is also antisense to *cro*, interfering with its translation. A burst of CII thus makes CI, integrase and less Q and Cro: everything needed for lysogeny.

CII is unstable: it is degraded by the host protease FtsH (HflB), and CIII, a delayed-early product from the left, inhibits FtsH. The amount of CII therefore integrates information about the infection: many phages infecting one cell (high multiplicity of infection) give more CII, which favors lysogeny when hosts are scarce relative to phages; poor nutrition lowers FtsH activity and also favors lysogeny, when a lytic burst would be small. Integration by Int, a **site-specific recombination** between *attP* of the phage and *attB* of the chromosome, completes the establishment ([7.2.9](/7.2.9)).

### 11.5.4. Maintaining Lysogeny: The Operator $O_{\mathrm{R}}$

Once made, CI controls itself. Each of the operators $O_{\mathrm{L}}$ and $O_{\mathrm{R}}$ has three subsites, $O_{\mathrm{R}1}$, $O_{\mathrm{R}2}$ and $O_{\mathrm{R}3}$, each $17\,\mathrm{bp}$, bound by CI dimers. $O_{\mathrm{R}}$ lies between two divergent promoters: $P_{\mathrm{R}}$ (rightward, *cro*), which overlaps $O_{\mathrm{R}1}$ and $O_{\mathrm{R}2}$, and $P_{\mathrm{RM}}$ (repressor maintenance, leftward, *cI*), which overlaps $O_{\mathrm{R}3}$.

- CI binds $O_{\mathrm{R}1}$ most tightly; a dimer at $O_{\mathrm{R}1}$ helps a second dimer bind $O_{\mathrm{R}2}$ through contacts between their C-terminal domains (**cooperative binding**).
- CI at $O_{\mathrm{R}1}$ and $O_{\mathrm{R}2}$ represses $P_{\mathrm{R}}$ (and, at $O_{\mathrm{L}}$, $P_{\mathrm{L}}$).
- CI at $O_{\mathrm{R}2}$ activates $P_{\mathrm{RM}}$: its N-terminal domain touches σ region 4 of a polymerase at $P_{\mathrm{RM}}$ and accelerates open-complex formation (a $k_2$ effect, Formula 10.4.1). CI is thus a positive autoregulator.
- At higher concentration CI also occupies $O_{\mathrm{R}3}$ and represses $P_{\mathrm{RM}}$: negative autoregulation, which caps the CI level.

The $O_{\mathrm{R}3}$ occupancy is made efficient by a loop. CI dimers at $O_{\mathrm{R}1}$–$O_{\mathrm{R}2}$ and $O_{\mathrm{L}1}$–$O_{\mathrm{L}2}$ associate into an octamer, looping the $2.4\,\mathrm{kb}$ of DNA between the operators, and two more dimers then bind cooperatively at $O_{\mathrm{R}3}$ and $O_{\mathrm{L}3}$ (Dodd, Egan and colleagues, 2004). Without the loop, repression of $P_{\mathrm{RM}}$ is weak, and the CI level of a lysogen would drift higher.

Cro binds the same six subsites with the opposite order of affinity: $O_{\mathrm{R}3}$ first, then $O_{\mathrm{R}2}$ and $O_{\mathrm{R}1}$. At low concentration Cro represses $P_{\mathrm{RM}}$, and at higher concentration also $P_{\mathrm{R}}$ and $P_{\mathrm{L}}$, its own promoters, which reduces early gene expression late in lytic infection.

### 11.5.5. The Switch and Its Induction

CI and Cro repress each other's promoters, and each acts on its own: CI activates its own promoter, Cro represses the promoter of CI. Such a pair of mutual repressors has two stable states, one with CI high and Cro low (lysogeny) and one with Cro high and CI low (lysis), and the initial burst of CII decides which state an infected cell enters. Once in the lysogenic state, the cell stays there for many generations: in cells lacking RecA the spontaneous rate of switching to lysis is below about $10^{-7}$ per generation, a stability that requires the cooperativity and the octameric loop described above. The analysis of this bistability as a property of a dynamical system, in the phase plane of CI and Cro concentrations, belongs to systems biology ([7.9](/7.9)); here the point is that bistability needs a nonlinear (cooperative) response and positive feedback, both of which the molecular mechanism supplies.

Induction connects the switch to the **SOS response** ([7.2.8](/7.2.8)). DNA damage generates single-stranded DNA, on which RecA forms an activated filament (RecA*). RecA* stimulates a latent self-cleavage of CI between its N-terminal DNA-binding domain and its C-terminal dimerization domain (between Ala111 and Gly112), the same reaction that RecA* induces in LexA. The cleaved N-terminal domains cannot dimerize or bind cooperatively, they fall off the operators, $P_{\mathrm{L}}$ and $P_{\mathrm{R}}$ fire, Cro is made, and the phage enters the lytic program, excises and lyses the cell about an hour later. The temperature-sensitive repressor CI857, inactivated at $42\,^\circ\mathrm{C}$, allows synchronous induction and is used in expression systems.

## 11.6. The Thermodynamic Model of Transcriptional Regulation

### 11.6.1. Promoter Occupancy

The cartoons of this chapter say which molecules bind where; a quantitative account must say how much a gene is expressed for given numbers of polymerases and regulators. The thermodynamic model (Ackers, Johnson and Shea, 1982; Buchler, Gerland and Hwa, 2003; Bintu, Phillips and colleagues, 2005) assumes that the binding and unbinding of regulators and polymerase are fast compared with initiation, so that the occupancy of the promoter region is at equilibrium, and that the rate of transcription is proportional to the probability of the states in which polymerase is bound and able to initiate.

**Definition 11.6.1 (Thermodynamic Model)** The **thermodynamic model** of transcriptional regulation describes the promoter region as a system in equilibrium among a set of states of occupancy by RNA polymerase and regulators, each with a statistical weight given by the **Boltzmann factor** of its free energy and the numbers of the bound molecules, and takes the transcription rate to be proportional to the probability $p_{\mathrm{bound}}$ of the states in which polymerase is bound at the promoter.

The probability of a state is its weight divided by the sum of all weights, the **partition function** ([6.3.10](/6.3.10)), exactly as for ligand binding to a protein in [7.1.7](/7.1.7). In a cell the specific sites compete with the rest of the genome: a polymerase or repressor that is not at its site is not free in solution but bound nonspecifically somewhere else on the DNA. This sets the reference state.

**Formula 11.6.1 (Polymerase occupancy)** Suppose that $P$ polymerase molecules are distributed between one promoter and $N_{\mathrm{NS}}$ nonspecific sites, with **binding energy** $\varepsilon_{\mathrm{S}}$ at the promoter and $\varepsilon_{\mathrm{NS}}$ at a nonspecific site, and let $\Delta\varepsilon_{\mathrm{pd}} = \varepsilon_{\mathrm{S}} - \varepsilon_{\mathrm{NS}} < 0$. If $N_{\mathrm{NS}} \gg P$, the probability that the promoter is occupied is
$$
p_{\mathrm{bound}} = \frac{\dfrac{P}{N_{\mathrm{NS}}}\,\mathrm{e}^{-\beta\Delta\varepsilon_{\mathrm{pd}}}}{1 + \dfrac{P}{N_{\mathrm{NS}}}\,\mathrm{e}^{-\beta\Delta\varepsilon_{\mathrm{pd}}}}, \qquad \beta = \frac{1}{k_{\mathrm{B}}T}. \tag{11.1}
$$

**Proof** With the promoter empty, all $P$ polymerases are on nonspecific sites, which can be chosen in $\binom{N_{\mathrm{NS}}}{P} \approx N_{\mathrm{NS}}^P/P!$ ways, each of energy $P\varepsilon_{\mathrm{NS}}$; with the promoter occupied, $P - 1$ are on nonspecific sites, in $\binom{N_{\mathrm{NS}}}{P-1} \approx N_{\mathrm{NS}}^{P-1}/(P-1)!$ ways, with energy $\varepsilon_{\mathrm{S}} + (P-1)\varepsilon_{\mathrm{NS}}$. The ratio of the total weights of the two states is
$$
\frac{Z_{\mathrm{bound}}}{Z_{\mathrm{empty}}} = \frac{N_{\mathrm{NS}}^{P-1}/(P-1)!}{N_{\mathrm{NS}}^{P}/P!}\,\mathrm{e}^{-\beta(\varepsilon_{\mathrm{S}} - \varepsilon_{\mathrm{NS}})} = \frac{P}{N_{\mathrm{NS}}}\,\mathrm{e}^{-\beta\Delta\varepsilon_{\mathrm{pd}}},
$$
and $p_{\mathrm{bound}} = Z_{\mathrm{bound}}/(Z_{\mathrm{empty}} + Z_{\mathrm{bound}})$. $\square$

Equation (11.1) has the form of a binding curve, $p_{\mathrm{bound}} = [\mathrm{P}]/([\mathrm{P}] + K_{\mathrm{d}})$, with the number of polymerases per nonspecific site in place of the concentration and $\mathrm{e}^{\beta\Delta\varepsilon_{\mathrm{pd}}}$ in place of the **dissociation constant**. For *E. coli*, $N_{\mathrm{NS}} \approx 4.6\times10^6$ (the genome length in base pairs) and the number of polymerases available for a promoter is of the order of $10^3$; a promoter is half occupied when $\mathrm{e}^{-\beta\Delta\varepsilon_{\mathrm{pd}}} = N_{\mathrm{NS}}/P \approx 5\times10^3$, that is, $\Delta\varepsilon_{\mathrm{pd}} \approx -8.5\,k_{\mathrm{B}}T$. Most regulated promoters are weaker than this; for a *weak promoter*, $(P/N_{\mathrm{NS}})\mathrm{e}^{-\beta\Delta\varepsilon_{\mathrm{pd}}} \ll 1$, and $p_{\mathrm{bound}}$ is proportional to that quantity, which simplifies everything that follows.

### 11.6.2. Repression and Activation

Add $R$ repressors that bind an operator overlapping the promoter with energy difference $\Delta\varepsilon_{\mathrm{rd}}$, and exclude the polymerase when bound. Writing $p = (P/N_{\mathrm{NS}})\mathrm{e}^{-\beta\Delta\varepsilon_{\mathrm{pd}}}$ and $r = (R/N_{\mathrm{NS}})\mathrm{e}^{-\beta\Delta\varepsilon_{\mathrm{rd}}}$ for the weights of the occupied states relative to the empty promoter, the three states (empty, polymerase, repressor) have weights $1$, $p$ and $r$.

**Formula 11.6.2 (Simple repression)** The ratio of expression with and without repressor, the *fold change*, is
$$
\text{fold change} = \frac{p_{\mathrm{bound}}(R)}{p_{\mathrm{bound}}(0)} = \frac{1 + p}{1 + p + r} \approx \left(1 + \frac{R}{N_{\mathrm{NS}}}\,\mathrm{e}^{-\beta\Delta\varepsilon_{\mathrm{rd}}}\right)^{-1} \tag{11.2}
$$
for a weak promoter ($p \ll 1$).

The approximation is the important step: for a weak promoter the fold change does not depend on the polymerase at all, only on the repressor number and its binding energy, two quantities that can be measured or varied independently. Garcia and Phillips (2011) did both: they built *E. coli* strains with a single operator (an ideal symmetric operator $O_{\mathrm{id}}$, $O_1$, $O_2$ or $O_3$) in front of a reporter and with the repressor gene expressed at levels from about $10$ to $1000$ per cell, counted the repressors, and fitted Eq. (11.2). The binding energies obtained, $\Delta\varepsilon_{\mathrm{rd}} \approx -17.0$, $-15.3$, $-13.9$ and $-9.7\,k_{\mathrm{B}}T$ for $O_{\mathrm{id}}$, $O_1$, $O_2$ and $O_3$, predicted the fold change of all strains with no further parameters.

**Example 11.6.1 (Repression by O1 alone)** With wild-type repressor numbers, $R \approx 10$ tetramers per cell, and $O_1$ alone, Eq. (11.2) gives
$$
r = \frac{10}{4.6\times10^6}\,\mathrm{e}^{15.3} \approx \frac{10 \times 4.4\times10^6}{4.6\times10^6} \approx 9.5, \qquad \text{fold change} \approx \frac{1}{10.5},
$$
a repression of about $10$-fold, the order of magnitude of the $18$-fold measured by Oehler and colleagues for $O_1$ alone (Example 11.2.2). The model also explains why a single weak operator such as $O_3$ represses not at all at these numbers ($r \approx 3.5\times10^{-2}$), and why a tenfold overexpression of repressor increases repression roughly tenfold once $r \gg 1$: on the log–log plot, fold change falls with slope $-1$ against $R$.

**Formula 11.6.3 (Activation)** If $A$ activators bind a site next to the promoter with energy difference $\Delta\varepsilon_{\mathrm{ad}}$, and an activator and polymerase bound together interact with energy $\varepsilon_{\mathrm{ap}} < 0$, then with $a = (A/N_{\mathrm{NS}})\mathrm{e}^{-\beta\Delta\varepsilon_{\mathrm{ad}}}$ the weights are $1$, $p$, $a$ and $pa\,\mathrm{e}^{-\beta\varepsilon_{\mathrm{ap}}}$, and for a weak promoter the fold change in expression is
$$
\text{fold change} = \frac{1 + a\,\mathrm{e}^{-\beta\varepsilon_{\mathrm{ap}}}}{1 + a}. \tag{11.3}
$$
It rises from $1$ when the activator is absent to the maximum $\mathrm{e}^{-\beta\varepsilon_{\mathrm{ap}}}$ when its site is saturated.

An activation of $50$-fold, typical of CAP at *lac*, needs only $\varepsilon_{\mathrm{ap}} = -\ln 50\,k_{\mathrm{B}}T \approx -3.9\,k_{\mathrm{B}}T$, the energy of a few hydrogen bonds or salt bridges between AR1 and the α-CTD. This is the quantitative content of the *recruitment* model: an activator need not change the polymerase, only add a small favorable contact; the weak promoter is weak because it binds polymerase poorly, and the contact makes up the difference. If the activator itself needs a ligand, as CAP needs cAMP, $A$ in Eq. (11.3) is replaced by the number of liganded activators, $A\,[\mathrm{cAMP}]^n/([\mathrm{cAMP}]^n + K^n)$, which gives the dose–response of Example 11.3.1.

### 11.6.3. Induction

Inducers enter the model through the allosteric state of the repressor. If each repressor dimer is either active (binding the operator) or inactive, with free-energy difference $\Delta\varepsilon_{\mathrm{AI}} = \varepsilon_{\mathrm{I}} - \varepsilon_{\mathrm{A}}$, and has two inducer-binding sites with **dissociation constants** $K_{\mathrm{A}}$ in the active and $K_{\mathrm{I}}$ in the inactive state, then the **MWC model** of [7.1.7](/7.1.7) gives the active fraction at inducer concentration $c$:
$$
p_{\mathrm{act}}(c) = \frac{(1 + c/K_{\mathrm{A}})^2}{(1 + c/K_{\mathrm{A}})^2 + \mathrm{e}^{-\beta\Delta\varepsilon_{\mathrm{AI}}}(1 + c/K_{\mathrm{I}})^2}, \tag{11.4}
$$
and $R$ in Eq. (11.2) is replaced by $p_{\mathrm{act}}(c)\,R$. With the parameters fitted for IPTG by Razo-Mejia, Phillips and colleagues (2018), $K_{\mathrm{A}} \approx 140\,\mu\mathrm{M}$, $K_{\mathrm{I}} \approx 0.5\,\mu\mathrm{M}$ and $\Delta\varepsilon_{\mathrm{AI}} \approx 4.5\,k_{\mathrm{B}}T$, one set of three numbers describes induction curves for all operators and repressor numbers. The curves have a characteristic shape: their midpoint shifts to higher inducer concentration as repressors or operator strength increase, and the expression at saturating inducer (the *leakiness* of repression) stays below $1$, because even with both sites occupied a small fraction $1/[1 + \mathrm{e}^{-\beta\Delta\varepsilon_{\mathrm{AI}}}(K_{\mathrm{A}}/K_{\mathrm{I}})^2] \approx 10^{-3}$ of repressors remains active.

### 11.6.4. DNA Looping and Its Periodicity

Looping adds a state in which one tetramer occupies two operators. Let $r_i = (R/N_{\mathrm{NS}})\mathrm{e}^{-\beta\Delta\varepsilon_i}$ be the weights for binding of a tetramer to operator $O_1$ (which blocks the promoter) or to an auxiliary operator $O_{\mathrm{aux}}$, and let a tetramer bound at $O_1$ close a loop to $O_{\mathrm{aux}}$ with additional weight $K_{\mathrm{loop}}$. For a weak promoter,
$$
\text{fold change} = \frac{1 + r_{\mathrm{aux}}}{1 + r_1 + r_{\mathrm{aux}} + r_1 r_{\mathrm{aux}} + r_1 K_{\mathrm{loop}}}, \qquad K_{\mathrm{loop}} = \mathrm{e}^{-\beta(\Delta\varepsilon_{\mathrm{aux}}' + \Delta F_{\mathrm{loop}})}, \tag{11.5}
$$
where $\Delta\varepsilon'_{\mathrm{aux}}$ is the binding energy of the second dimer at $O_{\mathrm{aux}}$ and $\Delta F_{\mathrm{loop}}$ is the free energy of forming the DNA loop. The loop competes with the free state only through the factor $K_{\mathrm{loop}}$, which can be large even when $O_{\mathrm{aux}}$ alone is weakly occupied: this is how $O_2$ and $O_3$, which by themselves repress little, multiply the repression by $O_1$ (Example 11.2.2).

The loop free energy depends on the length $L$ of DNA between the operators in three ways, which follow from the elasticity of DNA (a semiflexible polymer with bending persistence length $\ell_{\mathrm{p}} \approx 50\,\mathrm{nm} \approx 150\,\mathrm{bp}$, [7.6](/7.6)):

- Bending: a loop shorter than about $\ell_{\mathrm{p}}$ must be bent sharply, at an energy cost growing roughly as $\ell_{\mathrm{p}}/L$;
- Entropy: a long loop is easy to bend, but the probability that its ends meet falls as $L^{-3/2}$, as for the ends of a random walk;
- Twist: the two operators must face the repressor from the same side of the helix. If $L$ is not a whole number of helical repeats ($10.5\,\mathrm{bp}$), the DNA must be twisted by the fractional excess $\delta = L/10.5 - \operatorname{round}(L/10.5)$ of a turn, at an energy cost proportional to $\delta^2/L$.

The first two terms give an optimum loop length of the order of $\ell_{\mathrm{p}}/2$ and a slow decline at greater lengths; the third superimposes a modulation with a period of $10.5\,\mathrm{bp}$ that fades as $L$ grows, because long loops absorb a fractional turn more easily. This is what Müller, Oehler and Müller-Hill (1996) measured when they moved an auxiliary operator in steps of single base pairs: repression oscillated with a $10$–$11\,\mathrm{bp}$ period, was strongest at about $70$–$80\,\mathrm{bp}$, and decreased slowly up to more than $1\,\mathrm{kb}$; the same phase dependence underlies the half-turn experiment with *ara* (Remark 11.3.1). Systematic measurements of this kind (Boedicker, Garcia and Phillips, 2013) showed that loops in vivo are easier to form than naked-DNA elasticity predicts, owing to DNA-bending proteins such as HU and to the flexibility of the repressor.

![The thermodynamic model of lac regulation. A: fold change against the number of repressors per cell for a single operator (Eq. (11.2), N_NS = 4.6 × 10⁶), with binding energies −17.0 (Oid), −15.3 (O1), −13.9 (O2) and −9.7 kBT (O3); stronger operators repress at lower repressor numbers, and the curves fall with slope −1 once repression is strong; the dotted line marks about ten repressors per cell (wild type). B: induction curves from the MWC repressor of Eq. (11.4) (KA = 140 µM, KI = 0.5 µM, ΔεAI = 4.5 kBT) for O1 with 10, 100 and 1000 repressors per cell; the midpoint shifts to higher IPTG with more repressor, and expression at saturating IPTG stays slightly below 1. C: activation by CAP–cAMP (Eq. (11.3) with εap = −3.9 kBT, about 50-fold maximal activation, and a liganded fraction of CAP rising with cAMP with half-saturation at 50 µM and Hill coefficient 2) compared with a CAP-deficient strain, which stays at basal expression. D: repression (the inverse of the fold change) by O1 with an auxiliary operator O2 at distance L, using Eq. (11.5) and a minimal loop free energy βΔF = F0 + (3/2) ln L + aℓp/L + 2π²(Ceff/L)δ² with ℓp = 150 bp, a = 0.75 (bending optimum near 75 bp), an effective twist stiffness Ceff = 35 bp and F0 calibrated so that the best loop represses about 1000-fold; repression oscillates with the 10.5 bp helical repeat, is maximal near 70–80 bp and decays slowly for longer loops (an illustrative model, not a fit)](./plots/thermodynamic-model.py)

### 11.6.5. The Shea–Ackers Model of $O_{\mathrm{R}}$

The first thermodynamic model of a promoter was made for λ $O_{\mathrm{R}}$ (Shea and Ackers, 1985), from binding free energies measured by footprint titrations in vitro. Each of the $2^3 = 8$ states of $O_{\mathrm{R}}$ (each subsite empty or occupied by a CI dimer) has a weight
$$
w_s = [\mathrm{D}]^{n_s}\,\mathrm{e}^{-\Delta G_s/RT},
$$
where $[\mathrm{D}]$ is the concentration of free CI dimers (related to the total CI by the dimerization equilibrium), $n_s$ the number of dimers bound and $\Delta G_s$ the sum of the intrinsic free energies of the occupied subsites plus a cooperative term for adjacent occupied pairs, only one pair being cooperative at a time ($O_{\mathrm{R}1}$–$O_{\mathrm{R}2}$, or $O_{\mathrm{R}2}$–$O_{\mathrm{R}3}$ when $O_{\mathrm{R}1}$ is empty). $P_{\mathrm{R}}$ is active in the states with $O_{\mathrm{R}1}$ and $O_{\mathrm{R}2}$ empty; $P_{\mathrm{RM}}$ is active at a basal rate when $O_{\mathrm{R}2}$ and $O_{\mathrm{R}3}$ are empty, activated about tenfold when $O_{\mathrm{R}2}$ is occupied and $O_{\mathrm{R}3}$ empty, and off when $O_{\mathrm{R}3}$ is occupied.

With the measured values (intrinsic free energies about $-12.5$, $-10.5$ and $-9.5\,\mathrm{kcal\,mol^{-1}}$ for $O_{\mathrm{R}1}$, $O_{\mathrm{R}2}$, $O_{\mathrm{R}3}$, cooperativity about $-2.7\,\mathrm{kcal\,mol^{-1}}$, dimerization about $-11\,\mathrm{kcal\,mol^{-1}}$), the model reproduces the qualitative behavior of 11.5.4: as CI rises, $O_{\mathrm{R}1}$ and $O_{\mathrm{R}2}$ fill together (cooperativity makes their occupancy curves nearly coincide and steepens them), $P_{\mathrm{R}}$ switches off and $P_{\mathrm{RM}}$ switches on over less than a tenfold range of CI, and only at about a hundred times higher CI does $O_{\mathrm{R}3}$ fill and $P_{\mathrm{RM}}$ decline. With the in vitro free energies these transitions lie at nanomolar CI; in the cell, competition from nonspecific DNA and different ionic conditions weaken the effective affinities and shift them to the concentrations found in a lysogen (a few hundred nanomolar), but the order of events is the same. The sharpness of these switches is a **cooperativity** effect with an effective **Hill coefficient** near $2$; it supplies the nonlinearity that the bistable switch of 11.5.5 needs. Measured in vivo, $P_{\mathrm{RM}}$ repression is stronger than this in vitro model predicts, the difference being the $O_{\mathrm{L}}$–$O_{\mathrm{R}}$ loop.

![The Shea–Ackers model of the λ right operator. A: occupancy of OR1, OR2 and OR3 by CI dimers against the total CI concentration (monomers), computed from the eight states of OR with intrinsic free energies −12.5, −10.5 and −9.5 kcal mol⁻¹, a cooperativity of −2.7 kcal mol⁻¹ between adjacent dimers (OR1–OR2, or OR2–OR3 when OR1 is empty) and a dimerization free energy of −11.1 kcal mol⁻¹ at 25 °C; OR1 and OR2 fill together, OR3 only at much higher CI. B: the resulting relative activities of PR (active when OR1 and OR2 are empty) and PRM (basal with OR2 and OR3 empty, tenfold activated with OR2 occupied and OR3 empty, off with OR3 occupied); PR switches off and PRM on over a narrow range, and PRM is repressed only at about a hundredfold higher CI. With these in vitro free energies the transitions lie at nanomolar CI; in vivo they are shifted to higher concentrations (see text)](./plots/lambda-or.py)

## Summary

| Topic | Key points |
|---|---|
| Operons (Definitions 11.1.1–11.1.3) | Genes co-transcribed into a polycistronic mRNA; repressors bind operators (negative control), activators help polymerase (positive control); inducers inactivate repressors, corepressors activate them; cis-acting elements act on linked DNA, trans-acting factors diffuse; partial-diploid test |
| *lac* negative control | Allolactose (IPTG) inducer; $I^-$ constitutive, recessive, trans; $I^{\mathrm{s}}$ uninducible, dominant; $O^{\mathrm{c}}$ constitutive, cis-dominant; filter binding (Example 11.2.1), footprint at $+11$; tetramer with HTH headpieces (Definition 11.2.1); $O_1$, $O_2$ ($+412$), $O_3$ ($-82$): $1300$-fold with all three, $18$-fold with $O_1$ alone (Example 11.2.2); DNA looping; competition with polymerase |
| *lac* positive control (Definitions 11.3.1–11.3.3) | Catabolite repression; CAP–cAMP (Example 11.3.1) at $-61.5$, AR1 contacts α-CTD, bends DNA $90^\circ$; class I and II promoters; AND logic; inducer exclusion by EIIA$^{\mathrm{Glc}}$ is the main glucose effect; *ara* looping and phase (Remark 11.3.1) |
| *trp* | TrpR + Trp corepressor ($70$-fold); attenuation (Definition 11.4.1) by the leader peptide's Trp codons and alternative hairpins 1:2/3:4 versus 2:3 ($10$-fold); $700$-fold in total; TRAP and riboswitches elsewhere |
| λ (Definition 11.5.1) | Lytic: immediate early (N, Cro), delayed early (via N antitermination at *nut*, Example 11.5.1), late (Q at *qut* and the σ-dependent pause); lysogeny: CII (protected by CIII from FtsH) activates $P_{\mathrm{RE}}$, $P_{\mathrm{I}}$, $P_{\mathrm{aQ}}$; maintenance: CI at $O_{\mathrm{R}1}$, $O_{\mathrm{R}2}$ (cooperative) represses $P_{\mathrm{R}}$, activates $P_{\mathrm{RM}}$, at $O_{\mathrm{R}3}$ represses it; octamer loop to $O_{\mathrm{L}}$; Cro prefers $O_{\mathrm{R}3}$; induction by RecA*-stimulated CI cleavage |
| Thermodynamic model (Definition 11.6.1) | $p_{\mathrm{bound}}$ from Boltzmann weights relative to nonspecific DNA (Formula 11.6.1); simple repression $(1 + (R/N_{\mathrm{NS}})\mathrm{e}^{-\beta\Delta\varepsilon_{\mathrm{rd}}})^{-1}$ (Formula 11.6.2, Example 11.6.1); activation up to $\mathrm{e}^{-\beta\varepsilon_{\mathrm{ap}}}$ (Formula 11.6.3); induction by an MWC repressor, Eq. (11.4); looping Eq. (11.5) with bending, entropy and twist giving an optimum near $70$–$80\,\mathrm{bp}$ and a $10.5\,\mathrm{bp}$ period; Shea–Ackers model of $O_{\mathrm{R}}$ |

## Questions

1. Predict the β-galactosidase and permease levels, without and with inducer, of the partial diploids (a) $I^+ O^{\mathrm{c}} Z^- Y^+ \,/\, I^- O^+ Z^+ Y^-$ and (b) $I^{\mathrm{s}} O^+ Z^+ Y^+ \,/\, I^+ O^{\mathrm{c}} Z^+ Y^+$.

   **Answer** (a) The $I^+$ repressor acts in trans on both copies. The first copy has $O^{\mathrm{c}}$ and therefore expresses its genes constitutively: no β-galactosidase ($Z^-$) but permease ($Y^+$) with and without inducer. The second copy has a normal operator controlled by the $I^+$ repressor: β-galactosidase only with inducer, and no permease ($Y^-$). Result: permease constitutive, β-galactosidase inducible. (b) The super-repressor binds every normal operator and cannot be removed by inducer, so the $O^+$ copy is never expressed; but the $O^{\mathrm{c}}$ copy cannot be bound by any repressor and is expressed constitutively. Both enzymes are made constitutively, from the second copy only (at about half the level of a fully induced diploid).

2. Explain why the inducer of the *lac* operon must be allolactose rather than lactose itself, and why the cell needs a basal level of the *lac* proteins.

   **Answer** Allolactose is made from lactose by β-galactosidase, so its formation requires both lactose inside the cell and active β-galactosidase; a repressor that responded directly to external lactose would need a sensor at the surface. The basal (leaky) expression provides a few molecules of permease, which let a little lactose in, and of β-galactosidase, which converts some of it to allolactose; without them the operon could never be induced by lactose (it would remain inducible by IPTG, which enters without permease at high concentration). Leakiness and the positive feedback through permease make induction an autocatalytic, potentially all-or-none process.

3. Using Eq. (11.2), how many repressors per cell would be needed for $O_2$ alone to repress $100$-fold? For $O_3$?

   **Answer** Fold change $= 1/100$ requires $r = 99$: $R = 99\,N_{\mathrm{NS}}\mathrm{e}^{\beta\Delta\varepsilon}$. For $O_2$, $\mathrm{e}^{-13.9} \approx 9.2\times10^{-7}$, so $R \approx 99 \times 4.6\times10^6 \times 9.2\times10^{-7} \approx 420$. For $O_3$, $\mathrm{e}^{-9.7} \approx 6.1\times10^{-5}$, so $R \approx 99 \times 4.6\times10^6 \times 6.1\times10^{-5} \approx 2.8\times10^4$, more than the total of some abundant proteins: $O_3$ alone cannot work as a strong operator, and its role is to help $O_1$ by looping.

4. In the model of Eq. (11.5), what is the repression when the auxiliary operator is deleted? Use the result to explain how a $50$-fold contribution of the auxiliary operators can arise from operators that by themselves repress less than twofold.

   **Answer** With no auxiliary operator, $r_{\mathrm{aux}} = 0$ and $K_{\mathrm{loop}} = 0$, and Eq. (11.5) reduces to $1/(1 + r_1)$, the repression by $O_1$ alone (about $10$–$20$-fold). With the auxiliary operator, the term $r_1 K_{\mathrm{loop}}$ appears in the denominator, multiplied by $r_1$: the loop is an alternative way of occupying $O_1$ that is available only to a repressor already bound there, so its weight relative to the free state is $r_1 K_{\mathrm{loop}}$, not $r_{\mathrm{aux}}$. If $K_{\mathrm{loop}} \approx 50$ the repression increases about $50$-fold, although $r_{\mathrm{aux}}$ alone (the effect of the auxiliary operator without $O_1$) is small. The large effective concentration of the tethered second dimer near the auxiliary operator, far above the free repressor concentration, makes $K_{\mathrm{loop}} \gg r_{\mathrm{aux}}$.

5. A CAP site is moved from $-61.5$ to $-66.5$ upstream of a class I promoter. Predict the effect on activation and explain. What happens when it is moved to $-72$?

   **Answer** Moving the site by $5\,\mathrm{bp}$, half a helical turn, places CAP on the opposite face of the DNA, so its AR1 can no longer reach the α-CTD at the right position; activation is lost or strongly reduced, although CAP still binds. Moving it by about one full turn ($-72$, about $10.5\,\mathrm{bp}$ further) restores the face of the helix and largely restores activation, because the flexible α-CTD linker can span the extra distance. Class I activation therefore works at $-61.5$, $-71.5$, $-82.5$, $-92.5$ but not at intermediate positions.

6. Predict the effect on *trp* operon expression of (a) a mutation in segment 3 that prevents its pairing with segment 4 but not with 2; (b) mutation of the two Trp codons of the leader to Ala codons; (c) a mutation in the AUG of the leader peptide.

   **Answer** (a) The terminator cannot form, so transcription reads through regardless of tryptophan: attenuation is lost, and the operon is controlled by the repressor only (about $10$-fold higher expression when tryptophan is abundant). (b) The ribosome no longer stalls when tryptophan is scarce, so it reaches the stop codon and covers segment 2; the terminator forms under all conditions, and the operon no longer responds to tryptophan through attenuation (it would now respond, weakly, to alanine starvation). (c) No ribosome translates the leader: segments 1:2 and 3:4 pair, and transcription terminates under all conditions; expression is low even in starvation. This experiment showed that translation of the leader peptide is required for the response.

7. Why does a lysogen of λ resist superinfection by λ, but not by a phage with different operators (e.g., phage 434)? Predict what happens when a lysogen is infected by λvir with mutations in $O_{\mathrm{L}}$ and $O_{\mathrm{R}}$.

   **Answer** The lysogen contains free CI, which binds the operators of an incoming λ genome before $P_{\mathrm{L}}$ and $P_{\mathrm{R}}$ can be transcribed, so the infecting genome is silenced (immunity). Phage 434 has different operators and its own repressor, so λ CI cannot bind its operators, and 434 grows lytically on a λ lysogen; the specificity of immunity maps to the operators and the repressor recognition helix, as hybrid phages showed. λvir operators bind CI poorly, so its $P_{\mathrm{L}}$ and $P_{\mathrm{R}}$ remain active in the lysogen, and it grows lytically. Its products (N, Cro) also act in trans on the resident prophage, which can be induced as well.

8. Using Formula 10.4.1, explain why an activator acting on $k_2$ (like λ CI at $P_{\mathrm{RM}}$) and one acting on $K_{\mathrm{c}}$ (like CAP at *lac*) respond differently to the polymerase concentration. Which activation is captured by the thermodynamic model?

   **Answer** At low polymerase concentration ($[\mathrm{R}] \ll K_{\mathrm{c}}$), the rate of open-complex formation is $k_2[\mathrm{R}]/K_{\mathrm{c}}$, proportional to both $k_2$ and $1/K_{\mathrm{c}}$; both activators help. At high polymerase ($[\mathrm{R}] \gg K_{\mathrm{c}}$) the promoter is saturated with closed complexes, the rate approaches $k_2$, and lowering $K_{\mathrm{c}}$ no longer helps, while raising $k_2$ still does. The equilibrium thermodynamic model represents activation as an increase in the occupancy of the promoter by polymerase, which corresponds to the $K_{\mathrm{c}}$ mechanism (recruitment); activation of a step after binding is outside its equilibrium assumption and must be added as a state-dependent rate, as in the activated $P_{\mathrm{RM}}$ rate of the Shea–Ackers model.

9. (Open question) Phage λ chooses lysogeny more often when several phages infect the same cell. Propose a molecular explanation in terms of CII and discuss what it suggests about the "decision" as a computation.

   **Answer** Each infecting genome contributes copies of *cII* and *cIII*; with more genomes, CII is made faster than FtsH can degrade it, especially with CIII inhibiting FtsH, and crosses the threshold for activating $P_{\mathrm{RE}}$ sooner; the cooperative and positive-feedback action of CI then locks the cell into lysogeny. A high multiplicity of infection signals that phages outnumber hosts, so a lytic burst would find few new hosts, and dormancy is the better strategy; poor host nutrition, which lowers FtsH activity, likewise favors lysogeny when a lytic burst would be small. The decision thus computes a ratio of phage to host resources through protein dosage and degradation, and single-cell experiments (Zeng, Golding and colleagues, 2010) suggest that each infecting phage "votes", the outcome depending on whether all genomes in a cell commit to lysis. A quantitative treatment requires stochastic models of CII, CI and Cro with feedback, the subject of [7.9](/7.9).
