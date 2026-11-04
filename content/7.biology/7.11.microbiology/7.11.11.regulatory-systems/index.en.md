---
title: Microbial Regulatory Systems
description: "How prokaryotes decide what to make: the levels and costs of regulation; DNA-binding proteins and negative and positive control (arginine, lactose and maltose operons); regulons, stimulons, catabolite repression and diauxie; alternative sigma factors, anti-sigma factors and partner switching; transcriptional regulation in archaea (NrpR, TrmBL1); two-component systems and phosphorelays (EnvZ-OmpR, the Che pathway); quorum sensing in Gram-negative and Gram-positive bacteria and its inhibition; the stringent response and (p)ppGpp; the Pho regulon and the heat shock response; small RNAs, Hfq, riboswitches and attenuation; and the regulation of enzyme activity by feedback inhibition and covalent modification."
---

A bacterium carries genes for far more proteins than it needs at any moment. *Escherichia coli* can transport and catabolize dozens of sugars, make all twenty amino acids, respire with half a dozen electron acceptors and build a flagellum, but a cell growing in glucose-salts medium makes almost none of these systems. Making an unused protein costs amino acids, ATP and ribosome time, and ribosome time is the scarcest resource of a fast-growing cell ([7.6.39](/7.6.39)): a protein that occupies one per cent of the proteome for nothing slows growth by roughly one per cent. Regulation is therefore not a refinement but a central part of microbial physiology, and the speed at which it works — a response in minutes, a complete change of program in an hour — is what allows a population with a generation time of half an hour to track a changing environment.

This chapter is about the regulatory devices that microorganisms use and about the logic that links them. The mechanics of bacterial transcription and the classical analyses of the *lac* and *trp* operons are not repeated here ([7.2.10](/7.2.10), [7.2.11](/7.2.11)), nor are the molecular details of riboswitches and small RNAs ([7.2.18](/7.2.18)) or the general theory of transcription networks, their motifs and their noise ([7.9.15](/7.9.15), [7.9.17](/7.9.17)). What this chapter adds is the microbiologist's view: the whole repertoire from promoter to enzyme, the global networks that act on hundreds of genes at once, the sensory systems with which a cell reads its surroundings and its neighbours, and the archaeal versions of the same problems. The developmental programs that these devices build — sporulation, biofilms, cell cycles — follow in [7.11.12](/7.11.12).

## 11.1. The Levels and the Costs of Regulation

A cell can control a protein's contribution to metabolism at three levels, which differ in speed and in cost.

| Level | Mechanism | Time scale | What it costs |
|---|---|---|---|
| Transcription | Repressors, activators, **σ factors**, termination and antitermination | Minutes (set by mRNA decay and dilution by growth) | Cheapest: nothing is synthesized in vain |
| Translation | Ribosome-binding site occlusion by **small RNAs** or **riboswitches**, translational coupling | Seconds to minutes | mRNA already made |
| Protein activity | Allosteric **feedback inhibition**, covalent modification, proteolysis, sequestration by an inhibitor | Seconds | The protein is already made and paid for |

Prokaryotes regulate mainly at transcription, for two reasons. Their mRNAs are short-lived (half-lives of a few minutes in *E. coli*), so stopping transcription empties the pool of a message quickly; and transcription and translation are coupled, so there is little room for the elaborate post-transcriptional control of eukaryotes. Control of enzyme activity is kept for cases where speed matters more than economy — the first enzyme of a biosynthetic pathway responds to its end product within seconds, long before the change in transcription is felt.

Regulation itself has a cost: the regulator must be made, and a mistake in either direction is expensive. A simple accounting ([when regulation pays](/7.9.17#fml-17.4.1)) shows when it pays to regulate a gene rather than express it constitutively: roughly, when the condition in which the product is useful occupies less than about half the time. Genes needed under all conditions — those for ribosomes, for the core of central metabolism, for the envelope — are constitutive, varying only with growth rate; genes for a particular sugar, a particular stress or a particular host are tightly regulated.

**Remark 11.1.1** Regulation is never complete. A "fully repressed" promoter still fires occasionally, and this basal expression is essential: it provides the few molecules of permease and β-galactosidase that let a *lac*-repressed cell notice lactose at all. Switches in biology are leaky by design.

## 11.2. DNA-Binding Proteins and Transcriptional Control

### 11.2.1. How Regulatory Proteins Read DNA

Regulatory proteins recognize base pairs through the major groove, where the pattern of hydrogen-bond donors, acceptors and methyl groups differs among the four base pairs. A single contact is not specific enough, so a protein must touch several successive base pairs; and because the groove on one face of the helix can only reach so far, most bacterial regulators are homodimers that bind a site made of two inverted repeats, one half-site per subunit. The commonest recognition module is the **helix–turn–helix**: two α-helices joined by a three-residue turn, the first (the recognition helix) lying in the major groove, the second packing against it. LacI, the arginine repressor, the λ repressor and more than two hundred other *E. coli* proteins use it; other families use zinc fingers or leucine zippers, both commoner in eukaryotes.

The binding is a matter of degree, not of switching. Affinities and concentrations set an occupancy, and expression follows it continuously; the thermodynamic treatment of this in [7.2.11](/7.2.11#sec-11.6) gives the fold-change of a promoter from the binding energies of its sites.

### 11.2.2. Negative Control: Repression and Induction

In negative control a **repressor** bound near the promoter prevents transcription, and a small molecule (an **effector**) decides whether it binds.

- *Repression.* The enzymes of a biosynthetic pathway are made unless the product is already available. Adding arginine to a culture of *E. coli* stops the synthesis of the arginine biosynthetic enzymes within minutes while total protein synthesis continues unchanged. Arginine is a **corepressor**: bound to the inactive repressor ArgR it converts it into a form that binds the operators of the *arg* operons.
- *Induction.* The enzymes of a catabolic pathway are made only when the substrate is there. Lactose induces β-galactosidase because its isomer allolactose, the **inducer**, binds LacI and lowers its affinity for the operator.

Biosynthetic operons are usually repressible, catabolic operons inducible — the sign of the effector follows from what the pathway is for. Not every effector is a substrate or a product: isopropyl β-D-thiogalactoside (IPTG) induces the *lac* operon although β-galactosidase cannot cleave it, which is why it is the standard laboratory inducer.

![Three modes of transcriptional control in *E. coli*. A: negative control of a biosynthetic operon (*argCBH*): without arginine the repressor ArgR cannot bind the operator (O) and the genes are transcribed; with arginine as corepressor (purple dot) ArgR binds and blocks RNA polymerase. B: negative control of a catabolic operon (*lacZYA*): LacI occupies the operator until allolactose binds it. C: positive control of *malEFG*: the promoter is weak and RNA polymerase binds it only when the activator MalT, with maltose bound, occupies the activator-binding site (AB) next to it. P promoter](./plots/control-modes.py)

### 11.2.3. Positive Control: Activation

In positive control the promoter is a poor match to the consensus and polymerase binds it weakly; an **activator** bound nearby recruits the enzyme. The maltose system of *E. coli* is the classical example: MalT binds its activator-binding sites only with maltose bound, and then contacts polymerase directly. Activators work in two geometries. When the site abuts the promoter, the activator touches the α subunit or σ of polymerase already in place. When it lies hundreds of base pairs away, as at promoters served by σ⁵⁴, the DNA must loop so that the activator — an ATPase that opens the closed complex — can reach the enzyme. Some activators bend the DNA sharply instead, as CRP does by about 90°, which by itself can improve the contacts polymerase makes with the promoter.

Positive and negative control are not alternatives: many operons have both, and many promoters carry several sites for different regulators, so that expression is a function of several signals at once.

## 11.3. Global Control

### 11.3.1. Regulons and Stimulons

A single regulator often serves genes scattered over the chromosome. The maltose genes of *E. coli* lie in several operons at three positions, all with MalT sites: together they form the maltose **regulon**. The scale above the regulon is the set of genes that respond to one stimulus, whatever regulator does the work.

**Definition 11.3.1 (Stimulon)** A **stimulon** is the set of all genes whose expression changes in response to one environmental stimulus, regardless of how many regulators mediate the response; it therefore usually comprises several regulons.

The heat shock stimulon of *E. coli*, for example, contains the σ³² and σᴱ regulons and more. Stimulons are an experimental category — they are what a transcriptome experiment measures ([7.9.2](/7.9.2)) — while regulons are a mechanistic one.

### 11.3.2. Catabolite Repression and Diauxie

When several carbon sources are available, *E. coli* uses the best one first. **Catabolite repression** keeps the catabolic operons for the others off while glucose is present; dozens of operons are affected, and so are the flagellar genes, since a cell with a good carbon source has no reason to swim. Two mechanisms act together, both running through the phosphotransferase system ([7.11.4](/7.11.4#sec-4.3.4)): unphosphorylated EIIAᴳˡᶜ, abundant while glucose is being transported, inhibits the uptake of other sugars (**inducer exclusion**), while phosphorylated EIIAᴳˡᶜ, abundant when glucose runs out, activates adenylate cyclase, so that cAMP rises and the **catabolite activator protein** can activate the *lac*, *mal* and other promoters.

The visible consequence is **diauxic growth**: two exponential phases separated by a lag.

**Definition 11.3.2 (Diauxic Growth)** **Diauxic growth** (diauxie) is growth of a culture in two successive exponential phases on a mixture of two usable substrates, with an intervening lag during which the enzymes for the second substrate are induced after the preferred one is exhausted.

Monod's diauxie experiments of the 1940s, in which *E. coli* grew first on glucose and then, after a lag, more slowly on lactose, were the observation from which the whole study of bacterial gene regulation began.

## 11.4. Sigma Factors, Alternative Sigmas and Anti-Sigma Factors

Bacteria change whole programs by changing the promoter specificity of RNA polymerase. The core enzyme is unspecific; a **σ factor** directs it to one class of promoters, and a cell that carries several σ factors can switch hundreds of genes at once by changing which σ competes successfully for a limited pool of core enzyme.

| σ of *E. coli* | Gene | Regulon |
|---|---|---|
| σ⁷⁰ | *rpoD* | Housekeeping genes; the great majority of promoters |
| σ³² | *rpoH* | Heat shock: chaperones and proteases of the cytoplasm |
| σᴱ (σ²⁴) | *rpoE* | Envelope stress: periplasmic chaperones and proteases, and *rpoH* |
| σˢ (σ³⁸) | *rpoS* | General stress and stationary phase; over 400 genes |
| σ⁵⁴ (σᴺ) | *rpoN* | Nitrogen assimilation, and other systems needing an activator ATPase |
| σ²⁸ | *fliA* | Late flagellar genes |
| σ¹⁹ | *fecI* | Ferric citrate transport (an extracytoplasmic function σ) |

σ⁵⁴ is the exception in the family: it binds a $-24/-12$ promoter instead of $-35/-10$ and forms a closed complex that cannot isomerize without an activator hydrolysing ATP nearby, which makes its promoters strictly dependent on positive control. *Bacillus subtilis* carries more than fifteen σ factors, including the four that drive sporulation ([7.11.12](/7.11.12)), and the soil bacterium *Streptomyces coelicolor* more than sixty.

A σ factor is itself regulated, most often by a dedicated inhibitor.

**Definition 11.4.1 (Anti-σ Factor)** An **anti-σ factor** is a protein that binds a σ factor and prevents it from forming a holoenzyme with core RNA polymerase; its release, by proteolysis, by a conformational signal or by an **anti-anti-σ factor** that titrates it away (*partner switching*), activates the σ regulon.

Partner switching is a general device: a phosphorylatable anti-anti-σ factor binds the anti-σ factor only in one phosphorylation state, so a phosphatase that senses the signal controls the switch. The SpoIIAB–SpoIIAA–σᶠ module of sporulation is the best-known example ([7.11.12](/7.11.12)); the σᴮ general stress response of *B. subtilis* works the same way.

![Two ways of controlling an alternative σ factor in *E. coli*. A: the envelope stress response. The anti-σ factor RseA, a membrane protein, holds σᴱ inactive; unfolded outer-membrane proteins activate the periplasmic protease DegS, which makes the first cut in RseA, after which the intramembrane protease RseP cuts again and the cytoplasmic fragment is degraded, releasing σᴱ to transcribe envelope-repair genes and *rpoH*. B: the heat shock response read as a titration feedback (simulation of the model in the text, arbitrary units). Free DnaK promotes the degradation of σ³²; a temperature step at $t = 10$ fills the cell with unfolded proteins, which sequester DnaK, so σ³² is stabilized and heat shock proteins are made at several times the previous rate; as chaperone accumulates and the unfolded proteins are refolded, free DnaK rises again and the synthesis rate settles at a moderately raised level](./plots/sigma-stress.py)

## 11.5. Transcriptional Regulation in Archaea

The archaeal transcription apparatus is of the eukaryotic type: a multisubunit RNA polymerase that needs TBP and TFB to recognize a TATA box and a B recognition element ([7.2.12](/7.2.12)). Its regulators, however, are of the bacterial type — small helix–turn–helix proteins responding to metabolites. Archaeal gene regulation is therefore a chimera, and the two halves meet at the promoter in ways that have no counterpart in either domain.

- *Repression by occluding the general factors.* NrpR of the methanogen *Methanococcus maripaludis* represses the genes of nitrogen assimilation, including those for nitrogen fixation and glutamine synthetase. It binds operators that overlap the BRE and TATA box and so blocks TFB and TBP rather than the polymerase itself. When fixed nitrogen runs short, α-ketoglutarate accumulates — the acceptor of ammonia is not being used — binds NrpR and releases it. The signal is thus the same metabolite that reports nitrogen status in bacteria ([7.1.27](/7.1.27#sec-27.1.4)), read by a different protein.
- *Dual-acting regulators.* TrmBL1 of the hyperthermophile *Pyrococcus furiosus* (growth optimum $100\,^\circ\mathrm{C}$) represses the genes for sugar uptake by binding downstream of the TATA box, and activates the genes of gluconeogenesis by binding upstream of the promoter and recruiting the initiation complex. Maltose and other sugars release it from both sites, so one protein and one effector switch the cell between taking up sugar and making it. The TrmB family has more than 250 members across the archaea.
- *Redox sensing.* SurR of *P. furiosus* senses elemental sulfur through a pair of cysteines in its DNA-binding motif: with sulfur present it is oxidized, leaves its sites, and the cell switches from hydrogen production to sulfur reduction ([7.11.7](/7.11.7)).

Two-component systems, by contrast, are rarer in archaea than in bacteria and absent from several lineages, while protein phosphorylation on serine, threonine and tyrosine is widespread.

## 11.6. Sensing and Signal Transduction

### 11.6.1. Two-Component Systems

The standard way for a prokaryote to convert an external signal into a change in transcription is the **two-component system** ([Definition 15.5.1](/7.1.15#def-15.5.1)): a sensor histidine kinase, usually in the cytoplasmic membrane, and a cytoplasmic response regulator. The kinase autophosphorylates on a histidine using ATP when its periplasmic or membrane domain is stimulated, and the phosphoryl group is transferred to an aspartate of the response regulator, most of which are DNA-binding proteins. *E. coli* has about fifty such systems; some bacteria with complex lifestyles have far more (*Myxococcus xanthus* over two hundred).

Three features make the design robust and modular.

1. *Specificity by interface.* Each kinase phosphorylates its own regulator, although the chemistry is identical in all of them; the specificity resides in a small set of contact residues, which is why the pairs can be duplicated and diverge without crosstalk.
2. *Resetting.* The phosphoaspartate is intrinsically labile (seconds to hours), and most sensor kinases are bifunctional: the same protein dephosphorylates the regulator when unstimulated. The output then depends on the ratio of the two activities rather than on the amount of either protein, which makes the response insensitive to the concentrations of the components ([7.9.17](/7.9.17#sec-17.2.2)).
3. *Extension to relays.* Inserting further His and Asp domains gives a phosphorelay, His → Asp → His → Asp, with more steps at which other signals can feed in or phosphate can be drained off. Sporulation in *B. subtilis* uses one ([7.11.12](/7.11.12)).

EnvZ and OmpR adjust the porins of *E. coli* to the osmolarity of the medium. At low osmolarity the cell makes OmpF, whose pore is wide and lets nutrients in quickly; at high osmolarity — in the intestine, where bile salts and other toxic molecules are also present — it switches to the narrower OmpC. One phosphorylated regulator does both, because the *ompF* promoter has high-affinity sites that activate it at low OmpR-P and low-affinity sites that repress it at high OmpR-P, while *ompC* needs high OmpR-P throughout. A small RNA adds a second layer: *micF*, transcribed divergently from *ompC*, blocks translation of *ompF* mRNA.

![The EnvZ–OmpR two-component system of *E. coli*. A: the dimeric sensor kinase EnvZ autophosphorylates on a histidine with ATP and transfers the phosphoryl group to an aspartate of OmpR; the same protein dephosphorylates OmpR-P, so the level of OmpR-P reports the balance of the two activities. OmpR-P activates *ompF* at low concentration and represses it at high concentration, while activating *ompC*; the MicF small RNA, made from the *ompC* region, blocks translation of *ompF* mRNA. B: the resulting porin switch (model): as osmolarity rises, the cell exchanges the wide pore for the narrow one](./plots/two-component.py)

### 11.6.2. The Chemotaxis Pathway

Chemotaxis uses a modified two-component system in which the output is behaviour rather than transcription, and in which the system must respond to *changes* in concentration rather than to concentration itself. The behaviour — runs interrupted by tumbles, biased into a random walk up the gradient — and the capillary assay that measures it are described in [7.11.3](/7.11.3#sec-3.5); the physical limits of the measurement, the amplification by receptor clusters and the theory of adaptation are the subject of [7.6.35](/7.6.35#sec-35.5).

The components are six Che proteins and the receptors. Methyl-accepting chemotaxis proteins (MCPs: Tar for aspartate and maltose, Tsr for serine, plus minor ones) form ternary complexes with the adaptor CheW and the histidine kinase CheA, arranged in a hexagonal array at the cell pole. Attractant binding *inhibits* CheA autophosphorylation. CheA-P phosphorylates two response regulators: CheY, which diffuses to the flagellar motor and binds the switch protein FliM to favour clockwise rotation and so tumbling, and CheB. The phosphatase CheZ dephosphorylates CheY-P in a fraction of a second, so that CheY-P tracks the current kinase activity. Adaptation is the job of the methylation system: CheR methylates four glutamates on each receptor, which raises its activity, and CheB-P removes the methyl groups. Because CheB is activated by the kinase it regulates, methylation closes a slow negative feedback loop around the fast signalling path, and the kinase activity returns to its pre-stimulus value whatever the background concentration. The cell therefore measures the *logarithmic derivative* of the concentration along its path — the behavioural analogue of the Weber–Fechner law ([Definition 35.6.3](/7.6.35#def-35.6.3)).

The same CheY output serves phototaxis and aerotaxis: the Aer receptor senses the redox state of the electron transport chain rather than a molecule, and feeds into the same kinase, so that one motor control system is shared by several senses.

## 11.7. Quorum Sensing

### 11.7.1. The Principle

Some activities are useless to a single cell. A toxin secreted by one bacterium in a host is diluted to nothing; a biofilm matrix needs many producers; a light organ must contain billions of cells before it glows. A cell can find out whether it is alone by making a diffusible signal and sensing it.

**Definition 11.7.1 (Quorum Sensing)** **Quorum sensing** is the regulation of gene expression in response to the concentration of a self-produced, diffusible signal molecule, which reports the local density of cells producing it, so that a response is made only when a sufficient population (a *quorum*) is present.

**Definition 11.7.2 (Autoinducer)** An **autoinducer** is the diffusible signal of a quorum-sensing system: a small molecule made at a low basal rate by every cell of the population, which accumulates with cell density and, above a threshold concentration, activates its own synthesis and the quorum-regulated genes.

Three properties follow from the definition. The signal reports density only when diffusion and flow are slow, so what a cell actually measures is a combination of density and confinement — a single cell in a droplet can induce itself, which is why the phenomenon is also called *diffusion sensing*. The positive feedback (the autoinducer induces its own synthase) makes the response sharp. And the response is collective, which creates a public good and therefore the possibility of cheating ([7.10.16](/7.10.16)).

### 11.7.2. Signals and Circuits

| Group | Signal | Receptor | Example |
|---|---|---|---|
| Gram-negative, species-specific | Acyl homoserine lactones (AHLs): a lactone ring with an acyl chain of 4–18 carbons, often 3-oxo-substituted | Cytoplasmic LuxR-type activators (membrane-permeant signals) or membrane kinases | *Vibrio fischeri* (3-oxo-C6-HSL), *Pseudomonas aeruginosa* (3-oxo-C12-HSL, C4-HSL) |
| Gram-negative, interspecies | AI-2, a family of furanones derived from 4,5-dihydroxy-2,3-pentanedione, made by LuxS | Periplasmic binding protein LuxP with the kinase LuxQ | *Vibrio harveyi*, and the many bacteria that carry *luxS* |
| Gram-negative, other | CAI-1 (an α-hydroxyketone), PQS (a quinolone), DSF (a fatty acid), 3-OH PAME | Membrane kinases or cytoplasmic regulators | *Vibrio cholerae*, *P. aeruginosa*, *Xanthomonas*, *Ralstonia* |
| Gram-positive | Autoinducing peptides (AIPs), processed and exported, often cyclic | Membrane histidine kinases of two-component systems | *Staphylococcus aureus* (agr), *Streptococcus pneumoniae* (competence), *Bacillus subtilis* (ComX, PhrA) |

The division is not absolute — some Gram-negative bacteria use peptides and some Gram-positive ones respond to AHLs made by others — but it reflects a real constraint: a lactone crosses the cytoplasmic membrane freely and can be sensed inside, whereas a peptide cannot and must be sensed at the surface.

The *Vibrio fischeri* light organ of the Hawaiian bobtail squid *Euprymna scolopes* is the system in which quorum sensing was discovered ([7.11.31](/7.11.31)). LuxI makes 3-oxo-C6-HSL; bound to LuxR it activates the divergently transcribed *luxICDABEG* operon, which encodes luciferase and the enzymes that supply its aldehyde substrate — and more LuxI. Free-living cells at $10^2$–$10^3$ per millilitre are dark; in the crypts of the light organ, at $10^{10}$–$10^{11}$ per millilitre, they glow, and the squid uses the light to erase its silhouette against the moonlit surface.

![Quorum sensing in *Vibrio fischeri* and the switch it makes. A: the *lux* circuit. LuxI synthesizes the autoinducer 3-oxo-C6-HSL (dots), which crosses the membrane freely; bound to LuxR it activates the *lux* operon, hence luciferase and more LuxI — a positive feedback loop. B: steady states of the scaled model $\dot a = \rho\,(1 + \beta h(a)) - a$ with $h(a) = a^2/(1 + a^2)$ and $\beta = 20$, plotted against the scaled cell density $\rho$ (logarithmic axes). Solid curves are stable states, the dashed curve unstable; between the two folds the system is bistable, and the arrows mark the jumps on and off, which occur at different densities (hysteresis). C: a culture growing logistically switches abruptly when $\rho$ crosses the upper fold; without the feedback ($\beta = 0$) the same signal rises gradually and the output never reaches saturation](./plots/quorum-switch.py)

**Formula 11.7.1 (A Minimal Quorum-Sensing Switch)** Let $a$ be the intracellular autoinducer concentration in units of the receptor's dissociation constant, let the fraction of activated receptor be $h(a) = a^2/(1 + a^2)$, and let synthesis be the sum of a basal rate and an induced rate $\beta$ times larger, while the signal is lost by export, dilution and degradation at rate $1$ in scaled time. With a population at scaled density $\rho$ sharing one extracellular pool,

$$
\frac{\mathrm{d}a}{\mathrm{d}t} = \rho\left[1 + \beta\,h(a)\right] - a. \tag{11.1}
$$

For $\beta > 8$ the steady-state curve $\rho(a) = a/[1 + \beta h(a)]$ is non-monotonic, so there is a range of densities with three steady states, two stable and one unstable, and the culture switches on and off at different densities.

**Proof** Steady states satisfy $\rho = a/[1 + \beta h(a)]$. With $h(a) = a^2/(1+a^2)$, $\mathrm{d}\rho/\mathrm{d}a = 0$ gives $(1+\beta)a^4 + (2-\beta)a^2 + 1 = 0$, a quadratic in $a^2$ with two positive roots exactly when $\beta > 8$. Between the corresponding densities the curve has three branches; the middle one, where $\mathrm{d}\rho/\mathrm{d}a < 0$, is unstable. $\square$

The two folds are saddle-node bifurcations ([Definition 33.2.2](/7.6.33#def-33.2.2)), and the resulting **bistability** and hysteresis are what make the decision collective and hard to reverse: a transient dip in density does not switch the population off. The same two ingredients, cooperative activation and positive feedback, recur in every quorum circuit; the analysis of such switches, including the effect of noise on single cells, belongs to [7.6.33](/7.6.33) and [7.9.17](/7.9.17).

### 11.7.3. Layered Circuits and Virulence

In *Vibrio harveyi* and *V. cholerae* three receptors — for a species-specific AHL or CAI-1 and for AI-2 — feed into one phosphorelay. At low density they act as kinases, phosphate flows through LuxU to LuxO, and LuxO-P with σ⁵⁴ makes the Qrr small RNAs, which with Hfq destroy the mRNA of the master regulator LuxR (HapR in *V. cholerae*). At high density the ligand-bound receptors become phosphatases, the Qrr RNAs vanish and the master regulator appears. In *V. cholerae* the logic is inverted relative to what one might expect: high density *represses* the virulence genes and the biofilm matrix and promotes dispersal, which fits a pathogen that must leave the intestine to infect a new host.

*Pseudomonas aeruginosa* illustrates hierarchy. LasR with 3-oxo-C12-HSL stands at the top and activates its own synthase, the Rhl system (RhlI/RhlR with C4-HSL) and the PQS quinolone system; the three together control elastase, pyocyanin, rhamnolipids, hydrogen cyanide and the biofilm matrix — the arsenal responsible for chronic lung infection in cystic fibrosis. In *Staphylococcus aureus*, the *agr* system raises secreted toxins and lowers surface adhesins at high density: the bacterium first attaches and then, when crowded, switches to an invasive, tissue-destroying program.

![Three quorum-sensing architectures (activity flow; arrows activate, bars inhibit). A: *Vibrio harveyi* and *V. cholerae*. Receptors for the species-specific autoinducer and for AI-2 are kinases when empty; the phosphate they feed through LuxU to LuxO drives the Qrr small RNAs, which block the master regulator LuxR/HapR. Ligand binding turns the receptors into phosphatases and the master regulator appears. B: *P. aeruginosa*. LasR with 3-oxo-C12-HSL activates its own synthase and the Rhl and PQS systems, which together switch on the virulence factors. C: the *agr* system of *S. aureus*. AgrB processes and exports the autoinducing peptide AgrD; AgrC senses it and phosphorylates AgrA, which induces the *agr* operon itself and RNAIII, raising secreted toxins and lowering surface adhesins](./plots/qs-circuits.py)

### 11.7.4. Interfering with the Quorum

Because quorum sensing controls virulence but not growth, blocking it should disarm a pathogen without selecting as strongly for resistance as an antibiotic does — the idea behind anti-virulence therapy. Three routes have been explored: degrading the signal (lactonases and acylases, which many bacteria and some eukaryotes make naturally), blocking the receptor (the halogenated furanones of the red alga *Delisea pulchra*, which accelerate LuxR turnover, and synthetic AHL analogues), and inhibiting the synthase. Several compounds reduce virulence in animal models. The expectation of resistance-free treatment is, however, too optimistic: cheaters that do not respond to the signal are at an advantage in a treated population only if the blocked product is costly, and resistance to quorum-sensing inhibitors has been selected in the laboratory.

## 11.8. The Stringent Response and Other Global Networks

### 11.8.1. (p)ppGpp

When a culture is shifted from a rich medium to a poor one, synthesis of rRNA and tRNA stops within seconds, long before the pools of any precursor could run out, and resumes later at a rate appropriate to the new medium. This is the **stringent response**, and its mediator is a pair of guanosine polyphosphates.

**Definition 11.8.1 (Stringent Response and (p)ppGpp)** The **stringent response** is the global reprogramming of a bacterium on nutrient starvation, mediated by the alarmones **guanosine tetraphosphate** (ppGpp) and guanosine pentaphosphate (pppGpp), together written (p)ppGpp: synthesis of stable RNA, ribosomal proteins, DNA replication and envelope components is shut down, while amino-acid biosynthesis, stress genes and the σˢ regulon are turned up.

An uncharged tRNA entering the A site of a translating ribosome stalls it and activates the ribosome-associated synthase RelA, which transfers a pyrophosphate from ATP to GDP or GTP. A second, bifunctional enzyme, SpoT, degrades (p)ppGpp under most conditions but synthesizes it in response to carbon, phosphate, iron or fatty-acid limitation; many Gram-positive bacteria have a single bifunctional Rel protein instead. In *E. coli*, (p)ppGpp acts on RNA polymerase itself, binding at two sites with the cofactor DksA: promoters with a short-lived open complex, which includes the rRNA promoters, are inhibited, while promoters for amino-acid biosynthesis, whose open complexes are limiting in a different step, are stimulated. The free RNA polymerase released from the rRNA operons — which in fast growth carry most of the transcribing enzyme — becomes available to everything else, so inhibition and activation are two sides of the same redistribution. The quantitative consequence is the first growth law: the ribosomal fraction of the proteome is proportional to the growth rate ([Formula 39.2.1](/7.6.39#fml-39.2.1)).

Microbiologically, the same alarmone means different things in different organisms because the starvation they meet differs. *E. coli* voided in the faeces meets a dilute water body, and (p)ppGpp slows its division; *Caulobacter crescentus* in oligotrophic water responds to carbon and nitrogen limitation by making more swarmer cells, which can swim away ([7.11.12](/7.11.12)); in *Mycobacterium tuberculosis* inside a granuloma, hypoxia and phosphate limitation raise (p)ppGpp and convert part of the population into dormant **persister** cells, which survive antibiotics and are one reason that tuberculosis must be treated for months ([7.11.15](/7.11.15)).

### 11.8.2. Phosphate, Heat and General Stress

- *The Pho regulon.* Inorganic phosphate is often the limiting nutrient in soil and fresh water. The two-component system PhoR–PhoB (PhoR–PhoP in *Streptomyces* and many Gram-positive bacteria) senses low $P_{\mathrm{i}}$ and the phosphorylated regulator acts as an activator at some promoters and a repressor at others: in *Streptomyces* it turns up high-affinity phosphate uptake and the alkaline phosphatases, and turns down nitrogen metabolism (*glnA*, *amtB*) and antibiotic production. It represses, in fact, more genes than it activates — a reminder that "activator" and "repressor" are properties of a protein at a particular promoter, not of the protein.
- *Heat shock.* Raised temperature unfolds proteins; the cell answers with chaperones (DnaK/Hsp70, GroEL/Hsp60, GroES/Hsp10) and proteases ([7.1.6](/7.1.6#sec-6.4)). In *E. coli* the regulon belongs to σ³² (RpoH), which is normally destroyed within a minute by the membrane protease FtsH. Free DnaK binds σ³² and hands it to the protease; when unfolded proteins appear, they compete for DnaK, σ³² is spared, and the heat shock genes are transcribed until enough chaperone has accumulated to capture both the unfolded proteins and σ³² again. The regulator is thus titrated by the very problem it solves, which gives a response proportional to the damage and a built-in shut-off. Archaea have heat shock responses too, built on different regulators — the repressor Phr in *Pyrococcus*, with Hsp20 and the thermosome, a group II chaperonin.
- *The general stress response.* σˢ (RpoS) governs over four hundred genes in *E. coli*: catalase and other defences against oxidation, acid and osmotic resistance, morphological changes and the DNA polymerase IV of the SOS system. It is controlled at every level — transcription of *rpoS* is raised by (p)ppGpp, translation of its mRNA is promoted by small RNAs with Hfq, and the protein is degraded by ClpXP unless the adaptor is sequestered — which makes it the hub where starvation, stress and stationary phase converge ([7.11.8](/7.11.8#sec-8.3), [7.11.9](/7.11.9)).

## 11.9. RNA-Based Regulation

RNA regulates by base pairing and by folding, and prokaryotes exploit both. The mechanisms themselves are treated in [7.2.18](/7.2.18#sec-18.9) and [7.2.11](/7.2.11#sec-11.4); the table collects the microbiological examples and the comparison.

| Device | How it works | Signal | Examples |
|---|---|---|---|
| *trans*-acting **small RNAs** | A $50$–$300\,\mathrm{nt}$ RNA pairs imperfectly with a target mRNA; pairing at the ribosome-binding site blocks or (by opening a hairpin) permits translation, and pairing can expose or hide a ribonuclease site | Whatever induces the sRNA promoter | RyhB (iron starvation: shuts down non-essential iron proteins), SgrS (glucose-phosphate stress: blocks *ptsG*), MicF (osmolarity: blocks *ompF*), DsrA and RprA (promote *rpoS* translation), OxyS (oxidative stress) |
| The chaperone Hfq | A hexameric Sm-like protein that holds an sRNA and its target together and protects unpaired sRNA from degradation | — | Required by most *E. coli* sRNAs; ProQ is a second, distinct chaperone |
| **Riboswitches** | A metabolite binds an aptamer in the $5'$ untranslated region; the conformational change makes or breaks a terminator or sequesters the ribosome-binding site. No protein is involved | The metabolite itself | Thiamine pyrophosphate (the one riboswitch class also found in eukaryotes), flavin mononucleotide, S-adenosylmethionine, lysine, glycine, guanine, cobalamin, cyclic di-GMP, fluoride; the *glmS* ribozyme-riboswitch cleaves its own mRNA on binding glucosamine 6-phosphate |
| RNA thermometers | A hairpin over the ribosome-binding site melts above a threshold temperature | Temperature | *rpoH* mRNA of *E. coli*; the ROSE elements of *Rhizobium*; *prfA* of *Listeria monocytogenes*, which switches on virulence at $37\,^\circ\mathrm{C}$ |
| **Attenuation** | Translation of a short leader peptide containing codons for the regulated amino acid decides which of two alternative hairpins forms, and therefore whether transcription terminates before the structural genes | Charging of one tRNA, read by the speed of a ribosome | *trp*, *his*, *leu* operons of enteric bacteria; the T-box mechanism of Gram-positive bacteria does the same without translation, by pairing the uncharged tRNA directly with the leader |

Two general points are worth drawing out. First, RNA devices are fast and cheap: a riboswitch needs no protein at all, and an sRNA is transcribed in seconds. Second, pairing is stoichiometric, not catalytic: an sRNA is consumed with its target, so the response is threshold-linear — below a critical target synthesis rate the message is silenced almost completely, above it the excess escapes ([Formula 18.9.1](/7.2.18#fml-18.9.1)). This is a sharper switch than a repressor gives, which is one reason that sRNAs are so common in stress responses.

## 11.10. Regulation of Enzymes and Other Proteins

The fastest control acts on proteins that already exist.

**Feedback inhibition** ([Definition 9.5.2](/7.1.9#def-9.5.2)) is the standard device of biosynthesis: the end product binds an allosteric site on the first committed enzyme of its own pathway. Branched pathways need more care, and bacteria have three solutions, all visible in the aromatic amino acid pathway of *E. coli*: **isozymes** (three DAHP synthases, each inhibited by one of phenylalanine, tyrosine and tryptophan, so that an excess of one shuts off only its share of the flux), sequential feedback (each branch is inhibited at its own first step, and the intermediate that accumulates inhibits the common step) and concerted inhibition (the common enzyme is inhibited only by several end products together). The same end products usually also repress the genes, a slower and more thorough version of the same decision ([7.1.27](/7.1.27#sec-27.2.7)).

Covalent modification allows a signal to be integrated and amplified. The classical prokaryotic example is glutamine synthetase, the enzyme of ammonia assimilation at low ammonia concentrations ([7.1.27](/7.1.27#sec-27.1.3)). Its twelve subunits are adenylylated one by one by adenylyltransferase, and an adenylylated subunit is inactive, so activity falls in twelve steps as nitrogen becomes plentiful. What decides the direction is the signal protein PII: when glutamine is scarce, the uridylyltransferase GlnD adds UMP to PII, and PII–UMP directs adenylyltransferase to *remove* AMP and activate the enzyme; when glutamine is plentiful, the same bifunctional GlnD removes UMP, and PII directs adenylylation and inactivation. The cascade of two covalent-modification cycles amplifies a modest change in the glutamine pool into a large change in activity, and the same PII protein also controls the transcription of the nitrogen regulon through the NtrB–NtrC two-component system — one metabolite, read once, acting on both the enzyme and its gene. The steady state of such a cycle and its ultrasensitivity are treated quantitatively in [Formula 27.1.1](/7.1.27#fml-27.1.1) and [7.1.9](/7.1.9#sec-9.6).

Other post-translational devices complete the repertoire: regulated proteolysis (σ³², σˢ, RseA, all above), sequestration by an inhibitor (anti-σ factors; the many toxin–antitoxin pairs of [7.11.15](/7.11.15)), and second messengers that bind proteins and RNA directly — cAMP, (p)ppGpp and cyclic di-GMP, the last of which controls the switch from swimming to attached growth ([7.11.12](/7.11.12)).

## Summary

- Regulation adjusts the proteome to the environment, and its economics decide where it acts: transcription for economy, RNA devices for speed and cheapness, protein modification for the fastest responses. Constitutive expression pays only for products needed most of the time (Remark 11.1.1).
- Transcriptional regulators are mostly dimeric helix–turn–helix proteins that bind inverted repeats. Negative control uses a repressor released by an inducer (catabolic operons) or activated by a corepressor (biosynthetic operons); positive control uses an activator that recruits polymerase to a weak promoter.
- Global systems act above the operon: a **regulon** is the set of operons served by one regulator, a stimulon (Definition 11.3.1) the set of genes responding to one stimulus. **Catabolite repression**, through inducer exclusion and cAMP–CRP, orders the use of carbon sources and produces **diauxic growth** (Definition 11.3.2).
- Alternative **σ factors** switch whole programs; anti-σ factors (Definition 11.4.1) and partner switching keep them in reserve until a signal — unfolded envelope proteins for σᴱ, free chaperone for σ³² — releases them.
- Archaea combine a eukaryote-like transcription apparatus with bacteria-like regulators, which block or recruit TBP and TFB (NrpR, TrmBL1, SurR).
- **Two-component systems** convert a signal into His → Asp phosphotransfer; bifunctional kinases make the output robust, phosphorelays allow more inputs, and the chemotaxis version (Che proteins with methylation feedback) converts concentration changes into motor bias with perfect adaptation.
- **Quorum sensing** (Definition 11.7.1) lets a population act only when numerous, through **autoinducers** (Definition 11.7.2): AHLs and other small molecules in Gram-negative bacteria, peptides in Gram-positive ones, AI-2 between species. Cooperative sensing plus autoinduction makes the switch bistable (Formula 11.7.1); layered circuits (Las/Rhl/PQS, *agr*, LuxO–Qrr–HapR) tie it to virulence, and interfering with it is an anti-virulence strategy.
- The **stringent response** (Definition 11.8.1) redistributes RNA polymerase away from rRNA genes through (p)ppGpp made by RelA and SpoT, setting ribosome content to nutrient supply and, in different organisms, triggering dispersal, differentiation or dormancy. Pho, heat shock and σˢ are the other large global networks.
- RNA regulates through *trans*-acting **small RNAs** with Hfq, **riboswitches**, thermometers and **attenuation**; pairing-based control is fast, cheap and threshold-linear.
- Enzyme activity is controlled by **feedback inhibition** (with isozymes, sequential and concerted variants in branched pathways), by covalent modification cascades such as PII and glutamine synthetase adenylylation, by proteolysis and by second messengers.

## Questions

1. *E. coli* grown in a medium containing both glucose and lactose shows diauxie, but a mutant lacking adenylate cyclase grows only on glucose and never resumes growth on lactose, while a mutant with a *lac* promoter altered to a strong consensus sequence shows a single exponential phase. Explain both results.

   **Answer** Induction of the *lac* operon needs two things: relief of LacI repression and activation by cAMP–CRP. Without adenylate cyclase there is no cAMP, so CRP never activates the weak *lac* promoter and lactose cannot be used, whatever LacI does. A promoter strong enough to be read without CRP removes the second requirement, so the operon is induced as soon as lactose is present and glucose no longer delays it; the two sugars are then used together and the lag disappears.

2. A sensor histidine kinase is bifunctional (kinase and phosphatase on the same regulator). Show qualitatively why the steady-state fraction of phosphorylated regulator is then almost independent of the total amount of the two proteins, and why this would not hold if a separate phosphatase did the dephosphorylation.

   **Answer** With one bifunctional enzyme, both the forward and the reverse reaction are catalysed by the same molecules, so at steady state the ratio of phosphorylated to unphosphorylated regulator is set by the ratio of the kinase and phosphatase rate constants of that enzyme — the enzyme concentration cancels. If the regulator is in excess over the kinase, the output also becomes independent of the regulator concentration. With a separate phosphatase, the balance is the ratio of two different protein concentrations, which fluctuate independently with expression noise, so the output tracks that ratio instead of the signal ([7.9.17](/7.9.17#sec-17.2.2)).

3. Why is cooperative binding of the autoinducer–receptor complex, together with autoinduction of the synthase, enough to make a quorum response bistable? Use Eq. (11.1) and state what bistability buys the population.

   **Answer** Autoinduction makes synthesis an increasing function of the signal, and cooperativity makes it S-shaped; the steady-state condition $\rho = a/[1 + \beta h(a)]$ then has a non-monotonic right-hand side for $\beta > 8$, so three steady states coexist over a range of $\rho$ (Formula 11.7.1). The outer two are stable. The population therefore commits sharply at a threshold density, and because the off-switch occurs at a lower density than the on-switch, a transient dilution does not abort a response already under way; the group behaviour is all-or-none rather than graded.

4. On a shift from a rich medium to one lacking amino acids, rRNA synthesis stops within seconds. Trace the chain of events, and explain why inhibiting rRNA synthesis should also raise the transcription of amino-acid biosynthesis genes.

   **Answer** Amino acid starvation leaves tRNAs uncharged; an uncharged tRNA in the A site stalls the ribosome and activates RelA, which makes (p)ppGpp from GTP (or GDP) and ATP. With DksA, (p)ppGpp binds RNA polymerase and destabilizes open complexes; the rRNA promoters, whose open complexes are intrinsically short-lived, are the first to fail. Because the rRNA operons occupy a large share of the polymerase in a fast-growing cell, shutting them down releases free enzyme, which — together with the direct stimulation of promoters limited at a different step — raises transcription of the biosynthetic operons. The cell thus trades ribosome production for the capacity to make the missing amino acids.

5. A clinical isolate of *Pseudomonas aeruginosa* from a chronically infected lung carries a loss-of-function mutation in *lasR*. Such mutants are common late in infection. Suggest why they arise, and what this implies for anti-virulence drugs aimed at LasR.

   **Answer** The LasR regulon is a set of secreted public goods — elastase, rhamnolipids, siderophores — that benefit all cells nearby. A mutant that does not make them saves the cost but still enjoys the products of its neighbours, so it increases in frequency within the population: a social cheater ([7.10.16](/7.10.16)). (Other contributions have been proposed, such as better growth on particular nitrogen sources and reduced recognition by the immune system.) For therapy this cuts both ways: the spread of such mutants shows that losing LasR signalling is tolerated in the lung, so the Rhl and PQS systems and LasR-independent virulence must still operate, and a LasR inhibitor alone would not disarm a late-stage infection. It also shows that the common claim that anti-virulence drugs impose no selection is too simple — selection acts, but on the social structure of the population rather than on growth of single cells.
