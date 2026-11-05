---
title: "Bacterial Pathogenesis I: Infection and Toxins"
description: "What makes a bacterium a pathogen: the vocabulary of infection, the quantitative measures ID50 and LD50, the steps from a portal of entry to transmission, adhesins and colonization, invasion and spread through tissue, the competition for iron, the three classes of exotoxin with their molecular targets, endotoxin and the inflammatory cascade, and where virulence genes come from."
---

Most bacteria never cause disease, and the ones that do spend most of their existence not causing it. Pathogenesis is therefore not a property of a species but an outcome of a particular encounter: a sufficient number of cells of a particular strain, delivered to a particular tissue of a particular host. This chapter treats the offensive side of that encounter — how a bacterium reaches a surface, holds on to it, feeds, multiplies, damages the tissue and leaves for the next host — and ends with the toxins, which are the best-understood virulence factors and the ones whose biochemistry is most instructive. The defensive side, by which a pathogen survives the host response, together with the secretion machinery that delivers most of these factors, is [7.11.34](/7.11.34).

The structures used here were introduced earlier: the cell envelope and lipopolysaccharide in [7.11.2](/7.11.2), pili and capsules in [7.11.3](/7.11.3), biofilms in [7.11.12](/7.11.12), mobile elements and **pathogenicity islands** in [7.11.13](/7.11.13). The host's immune system is described only as far as a pathogen must deal with it; its cells, organs and receptors belong to [7.15](/7.15). The epidemiology of the resulting diseases is [7.11.35](/7.11.35).

## 33.1. The Language of Pathogenesis

**Definition 33.1.1 (Pathogen)** A **pathogen** is an organism capable of causing disease in a host. **Pathogenicity** is the ability to cause disease — a qualitative, species- or strain-level property — while **virulence** is the degree of damage inflicted, a quantitative property of a particular strain measured in a particular host.

The distinction matters because virulence is not an intrinsic constant. It depends on the strain (*Escherichia coli* ranges from a harmless gut commensal to the cause of haemolytic uraemic syndrome), on the route of delivery, and on the host's age, nutrition, genetics and existing microbiota ([7.11.32](/7.11.32)). An *opportunistic pathogen* causes disease only when these conditions favour it: *Pseudomonas aeruginosa* is harmless on intact skin and lethal in a burn patient.

Several further terms are used throughout.

- *Infection* is the establishment and multiplication of an organism in or on a host; *disease* is damage to the host that impairs its function. Infection without disease is the normal case: most people who acquire *Neisseria meningitidis* carry it in the nasopharynx and never become ill.
- A *carrier* harbours and sheds a pathogen without symptoms, and is epidemiologically important precisely because nothing marks them out ([7.11.35](/7.11.35)).
- The *incubation period* is the interval from infection to the first symptoms; the illness then passes through prodromal, acute and convalescent phases. Incubation periods range from hours (staphylococcal food poisoning, where a preformed toxin is ingested) to years (tuberculosis reactivating from a latent focus), and the distribution of this interval shapes the epidemic curve ([7.11.35](/7.11.35)).
- *Bacteraemia* is the presence of bacteria in the blood; *septicaemia* is their multiplication there, which if it provokes a systemic inflammatory response leads to sepsis and septic shock.

**Definition 33.1.2 (Virulence Factor)** A **virulence factor** is a bacterial molecule or structure that contributes to the establishment, maintenance or damage of an infection but is not required for growth outside the host. The main functional classes are adhesins, invasins and tissue-degrading enzymes, nutrient-acquisition systems, factors that defeat host defences, and toxins.

This operational definition is what makes virulence genetically tractable. A gene is called a virulence gene if deleting it reduces the severity of infection in an animal model while leaving growth in culture unaffected — the criterion behind *molecular Koch's postulates*: the gene is present in virulent strains, its inactivation reduces virulence, and restoring it restores virulence.

## 33.2. Measuring Virulence: ID50 and LD50

Virulence becomes quantitative as soon as one asks how many cells are needed.

**Definition 33.2.1 (ID50 and LD50)** The **infectious dose 50** (ID₅₀) is the number of organisms that establishes infection in 50 % of inoculated hosts; the **median lethal dose** (LD₅₀) is the number that kills 50 % within a stated period. Both are properties of a strain–host–route combination, not of the organism alone.

These numbers span an extraordinary range. *Shigella* and enterohaemorrhagic *E. coli* infect with tens to hundreds of ingested cells, because they survive gastric acid well and need only reach the colonic epithelium; *Vibrio cholerae* taken in water requires something closer to $10^8$ cells, most of which are killed by stomach acid, which is why neutralizing the acid (with a bicarbonate drink, or in people on acid-suppressing drugs) lowers the dose needed by orders of magnitude.

![Dose–response in infection. A: the independent-action model. Each ingested cell independently establishes infection with probability $r$, so the number of successful cells is Poisson with mean $rd$ and the probability of infection is $1 - \mathrm{e}^{-rd}$ (Eq. 33.1); the curve is plotted for three values of $r$, and the dose at which it crosses 0.5 is the ID₅₀. Because the model has a single parameter, ID₅₀ $= \ln 2 / r$: a hundredfold difference in ID₅₀ is a hundredfold difference in the per-cell probability of success. B: the same curve plotted against $\log_{10} d$ beside an empirical four-parameter logistic fit to simulated challenge data (ten hosts per dose); the logistic has a free slope and so can accommodate the shallower responses seen in practice, but near the midpoint the two are hard to distinguish — which is why ID₅₀ is estimated far more reliably than the shape of the curve. The fitting of such curves is treated in [7.7.11](/7.7.11#sec-11.5). C: ID₅₀ estimates differ by seven orders of magnitude between enteric pathogens, a difference produced mostly at the stomach](./plots/dose-response.py)

The simplest mechanistic model assumes *independent action*: each organism acts alone, with probability $r$ of surviving and establishing a focus of infection, independently of the others. The number of successes among a dose $d$ is then Poisson with mean $rd$, and the probability of at least one is

$$
P(\text{infection}) = 1 - \mathrm{e}^{-rd}. \tag{33.1}
$$

Two consequences are worth stating. First, there is no threshold: a single cell can in principle infect, with probability $r$, and the "minimum infectious dose" quoted in textbooks is a statistical statement about a population of hosts, not a biological barrier. Second, Eq. (33.1) gives $\mathrm{ID}_{50} = \ln 2 / r \approx 0.69/r$, so the enormous spread of ID₅₀ values is a spread in the single-cell success probability — in *Shigella* about $10^{-2}$, in *V. cholerae* about $10^{-8}$.

**Remark 33.2.1** Real challenge data often show a shallower slope than Eq. (33.1), for two reasons: hosts differ in susceptibility, and organisms sometimes cooperate (quorum-regulated virulence, [7.11.11](/7.11.11), makes a large inoculum more than the sum of its cells). A four-parameter logistic with a free Hill slope is then fitted empirically. Both models are fitted to the same kind of dose–response data as drug potency curves, and the statistical machinery is shared with them.

## 33.3. The Steps of an Infection

Every infection passes through the same sequence, and each step is a target for prevention.

![The course of an infection. The pathogen reaches a portal of entry — skin breached by a wound, a bite or a catheter; the respiratory, gastrointestinal or urogenital mucosa — and must survive the local defences (mechanical washing, mucus and secretory IgA, acid, lysozyme, antimicrobial peptides, the resident microbiota). It then adheres by adhesins to specific host receptors, multiplies to form a colonizing population, and in many diseases invades across the epithelium, spreading locally through tissue or systemically by blood or lymph. Damage follows, from toxins, from degradative enzymes or from the inflammatory response itself. Finally the pathogen is shed into secretions, faeces, skin lesions or blood taken up by an arthropod, which closes the cycle to the next host. The steps correspond to the sections of this chapter and the next; interventions act at each of them](./plots/infection-steps.py)

### 33.3.1. Portals of Entry

Intact skin is almost impenetrable: essentially no bacterium crosses it unaided, so skin infections begin at wounds, burns, surgical incisions, intravascular catheters, or bites. Arthropods create their own breach — *Yersinia pestis* enters by a flea bite, *Borrelia burgdorferi* by a tick bite — and so dispense with the problem entirely.

Mucous membranes, which line the respiratory, gastrointestinal and urogenital tracts, present an area of hundreds of square metres and are the usual route. They are defended by a layer of *mucin* glycoproteins that binds bacterial surface molecules and is continuously swept away: roughly a litre of mucus a day in the airway, moved by the ciliary escalator, and more in the gut. Secretory IgA embedded in the mucus crosslinks organisms and increases their entrapment. Pathogens answer with mucinases that digest the gel, or with shape and motility that penetrate it — *Helicobacter pylori* corkscrews through gastric mucus with a polar bundle of flagella, which is why it is one of the few organisms able to colonize the stomach.

Specialized structures are specific weak points. The M cells overlying the gut-associated lymphoid tissue sample luminal antigen and carry only a thin mucus layer; *Salmonella*, *Shigella* and *Yersinia* all use them as the way across the epithelium, exploiting the very cells that exist to detect them.

### 33.3.2. Localized and Systemic Courses

Some pathogens multiply only at the point of entry (*Corynebacterium diphtheriae* in the pharynx, *V. cholerae* in the small intestine) and cause disease at a distance through a toxin. Others breach the basement membrane and spread, through tissue, through the lymphatics to the nodes, or through the bloodstream to a target organ.

## 33.4. Adhesion and Colonization

**Definition 33.4.1 (Adhesin)** An **adhesin** is a bacterial surface molecule that binds a specific host molecule, anchoring the cell to a tissue. The complementary host molecule — usually a carbohydrate on a glycoprotein or glycolipid, or a protein of the junctional or extracellular-matrix machinery — is its receptor.

Adhesion is the first committed step, because a surface that is washed or swept clears any organism that merely arrives. It is also the main determinant of tissue tropism: an adhesin binds where its receptor is, and nowhere else. The specificity is fine-grained enough that single amino-acid differences in an adhesin change which organ is colonized.

### 33.4.1. Fimbrial Adhesins

Most adhesins sit at the tip of a pilus (fimbria), a filament of thousands of identical subunits capped by the binding protein. In Gram-negative bacteria the common ones are built by the *chaperone–usher pathway*: pilin subunits cross the inner membrane through the Sec machinery ([7.11.34](/7.11.34#sec-34.5)), a periplasmic chaperone holds each subunit in an incomplete fold, and an outer-membrane usher assembles and extrudes the fibre tip first, each subunit completing its neighbour's fold by *donor strand exchange*.

| Pilus | Example | Tip adhesin and receptor |
|---|---|---|
| Type 1 | *E. coli* | FimH binds terminal D-mannose on uroplakin and other glycoproteins; cystitis |
| P pilus | uropathogenic *E. coli* | PapG binds the Galα1-4Gal of the P blood group antigen on kidney epithelium; pyelonephritis |
| Type IV | *P. aeruginosa*, *Neisseria* | polar, retractile; adhesion plus twitching motility and DNA uptake ([7.11.3](/7.11.3), [7.11.13](/7.11.13)) |
| Curli (type V) | *E. coli*, *Salmonella* | amyloid fibres nucleated by CsgB from secreted CsgA; aggregation and biofilm formation |

The mannose binding of type 1 pili is the basis of a classical assay: piliated *E. coli* agglutinate erythrocytes, and the agglutination is abolished by free mannose, which was how the receptor was identified. It also suggests a therapy — *mannosides* that occupy FimH competitively reduce bladder colonization in animal models without killing the organism, and so impose less selection for resistance than an antibiotic ([7.11.15](/7.11.15)).

Gram-positive pili are built differently. Having no outer membrane to push a fibre through, *Corynebacterium*, *Actinomyces* and streptococci polymerize their pilin subunits by covalent isopeptide bonds, formed by **sortase** transpeptidases that recognize a C-terminal LPXTG motif and finally anchor the fibre to the peptidoglycan ([7.11.34](/7.11.34#sec-34.5)). The same enzymes attach dozens of other surface proteins, which is why a sortase mutant of *Staphylococcus aureus* loses many virulence factors at once.

### 33.4.2. Afimbrial Adhesins and Capsules

Surface proteins that are not assembled into filaments mediate the tighter, closer binding that follows the initial pilus-mediated contact; they commonly recognize host proteins rather than sugars — integrins, cadherins, fibronectin. Internalin A of *Listeria monocytogenes*, binding E-cadherin, is both an adhesin and an invasin (§33.5). Capsules and the exopolysaccharide of **biofilms** ([7.11.12](/7.11.12)) contribute as well: they are sticky, they protect against phagocytosis ([7.11.34](/7.11.34#sec-34.2)), and on implanted devices the biofilm is usually the infection.

**Remark 33.4.1** Binding is rarely passive. Contact with the host receptor is a signal: in enteropathogenic *E. coli*, in *Salmonella* and in *P. aeruginosa*, attachment induces the expression of secretion systems and effector proteins, so that the machinery of invasion is built only where it is needed. A two-step course — loose capture by a long, flexible pilus that overcomes electrostatic repulsion, then retraction or depolymerization and tight binding by surface proteins — is common.

## 33.5. Invasion, Spread and the Acquisition of Nutrients

### 33.5.1. Degradative Enzymes

Spreading through tissue means dismantling the matrix that holds it together. *Streptococcus pyogenes* secretes *hyaluronidase*, which depolymerizes the hyaluronan of the extracellular matrix; clostridia secrete *collagenase*, opening the way into deeper, less oxic tissue that suits an anaerobe. *S. pyogenes* also secretes *streptokinase*, which activates host plasminogen to plasmin and so dissolves the fibrin that the host deposits to wall the infection off — the opposite strategy to the coagulase of *S. aureus* ([7.11.34](/7.11.34#sec-34.2)), and an illustration that there is no single right answer: localizing the infection and escaping the localization are both viable. Streptokinase's fibrinolytic activity has been used clinically as a thrombolytic drug. Phospholipases (lecithinases), proteases, nucleases and glycosidases serve both to destroy tissue and to release nutrients; nucleases additionally dissolve the DNA meshwork of neutrophil extracellular traps.

### 33.5.2. Induced Uptake: Zipper and Trigger

Non-phagocytic epithelial cells can be made to internalize a bacterium, by two mechanisms distinguished by their morphology.

- The *zipper mechanism*: a bacterial surface protein binds a host adhesion receptor with high affinity, and the host membrane follows the bacterial surface around the cell, as a zip closes. *L. monocytogenes* uses internalin A (binding E-cadherin) and internalin B (binding the receptor tyrosine kinase Met); engaging these receptors triggers the normal endocytic and cytoskeletal responses ([7.3.10](/7.3.10), [7.3.18](/7.3.18)). The use of E-cadherin, a junctional protein, also explains how the organism crosses the intestinal, placental and blood–brain barriers.
- The *trigger mechanism*: the bacterium injects effector proteins through a type III secretion system ([7.11.34](/7.11.34#sec-34.6)) that activate host Rho-family GTPases directly, producing a dramatic ruffle of actin that engulfs the organism and then subsides as other injected effectors switch the GTPases off again. *Salmonella* and *Shigella* enter this way.

### 33.5.3. Spread between Cells

*L. monocytogenes*, *Shigella*, *Rickettsia rickettsii* and *Burkholderia* escape the vacuole into the cytosol and polymerize host actin at one pole, forming a comet tail that drives the cell forward and into a protrusion that the neighbouring cell engulfs. The bacterium therefore passes from cytoplasm to cytoplasm without entering the extracellular space, where antibody and complement would find it. The mechanism is the host's own machinery: ActA of *Listeria* mimics the nucleation-promoting factors that activate the Arp2/3 complex ([7.3.13](/7.3.13)), and the resulting branched network pushes exactly as it does at the leading edge of a motile cell.

### 33.5.4. Iron and Nutritional Immunity

Free iron in human tissue is of the order of $10^{-18}$ to $10^{-9}\,\mathrm{mol\,L^{-1}}$, far below what growth requires, because essentially all of it is bound — in haem, in ferritin inside cells, by transferrin in serum and lactoferrin at mucosal surfaces. Withholding metals in this way is a defence in its own right, called *nutritional immunity*, and it is reinforced during inflammation: the neutrophil protein calprotectin chelates manganese and zinc in the infected tissue, and hepcidin lowers serum iron.

Pathogens answer in three ways. They secrete **siderophores** ([7.11.4](/7.11.4)) — small chelators of extremely high affinity, taken back up with their bound ferric ion through dedicated outer-membrane receptors energized by the proton motive force through TonB, then through an ABC transporter at the inner membrane. They take iron directly from host proteins, with surface receptors that strip it from transferrin and lactoferrin or that extract haem (the Isd system of *S. aureus* passes haem from one cell-wall-anchored protein to the next and into the cytoplasm, where a haem oxygenase releases the iron). And they lyse host cells with toxins, releasing the large intracellular stores — which is one reason many toxins are expressed only when iron is scarce. Diphtheria toxin is the classic case: its gene is repressed by the iron-loaded DtxR regulator, so the toxin appears exactly when the organism is starved of iron, that is, in the host.

**Remark 33.5.1** Because siderophore uptake systems are specific, they are also a route in: some antibiotics are smuggled through them as *sideromycins*, and the cephalosporin cefiderocol is a siderophore conjugate designed on this principle ([7.11.14](/7.11.14)).

## 33.6. Exotoxins: AB Toxins

**Definition 33.6.1 (Exotoxin)** An **exotoxin** is a protein secreted by a living bacterium (or released on lysis) that damages the host at sites often distant from the infection. Exotoxins are heat-labile proteins of defined sequence, effective at very low concentration, strongly antigenic, and convertible into *toxoids* — chemically or genetically inactivated forms that retain antigenicity and are the basis of the diphtheria and tetanus vaccines.

Three structural classes cover almost all of them: AB toxins, which deliver an enzyme into the host cytoplasm; pore-forming toxins, which perforate the membrane; and superantigens, which subvert the immune system itself.

![The three classes of exotoxin. A: an AB toxin. The B moiety binds a surface receptor; the holotoxin is endocytosed; a conformational change (acidification in the endosome, or retrograde transport to the endoplasmic reticulum) translocates the A subunit across a membrane; in the cytosol the A subunit, an enzyme, modifies its target catalytically, so that a few molecules suffice. B: a pore-forming toxin. Soluble monomers bind the membrane (often through a lipid such as cholesterol or sphingomyelin), oligomerize into a ring, and insert a β-barrel that opens a pore; the cell loses its ionic gradients and lyses. C: a superantigen. Instead of being processed into a peptide, the toxin crosslinks the MHC class II molecule of an antigen-presenting cell to the variable β region of the T-cell receptor outside the peptide groove, activating a large fraction of T cells irrespective of their specificity and provoking a massive release of cytokines](./plots/toxin-classes.py)

**Definition 33.6.2 (AB Toxin)** An **AB toxin** consists of an enzymatically active A moiety and a binding B moiety (often a pentamer of identical subunits). The B part determines which cells are intoxicated, by its receptor; the A part determines what happens to them, by its catalytic activity. Because the A subunit is an enzyme acting on an intracellular substrate, a single molecule reaching the cytosol can kill a cell.

![Two AB toxins and their intracellular routes. Left: diphtheria toxin binds the precursor of heparin-binding EGF, enters by clathrin-mediated endocytosis, and uses the acidification of the endosome to insert its translocation domain and thread the A chain into the cytosol, where it ADP-ribosylates the diphthamide residue of elongation factor 2, arresting protein synthesis. Right: cholera toxin binds the ganglioside GM1, travels backwards through the Golgi to the endoplasmic reticulum, and exploits the ER-associated degradation machinery to deliver A1 to the cytosol, where it ADP-ribosylates the α subunit of $G_{\mathrm{s}}$; this blocks the GTPase activity of $G_{\mathrm{s}}\alpha$, leaving adenylate cyclase permanently on. The resulting high cAMP opens the CFTR chloride channel and blocks sodium absorption, so chloride, bicarbonate and water pour into the lumen. The diagram also shows why oral rehydration works: glucose-coupled sodium uptake through SGLT1 is untouched by the toxin](./plots/ab-toxin-routes.py)

The examples below are chosen because each illustrates a different enzymatic chemistry.

- *Diphtheria toxin* (*C. diphtheriae*) ADP-ribosylates elongation factor 2 on a modified histidine residue (diphthamide), inactivating it and stopping translation ([7.2.20](/7.2.20)). Death of pharyngeal epithelium produces the characteristic pseudomembrane, and the circulating toxin damages heart and nerves. The toxin gene is carried not by the bacterium but by a lysogenic bacteriophage (corynephage β) — **lysogenic conversion**, §33.10.
- *Cholera toxin* (*V. cholerae*) ADP-ribosylates the α subunit of the stimulatory G protein $G_{\mathrm{s}}$, abolishing its GTPase activity so that adenylate cyclase runs continuously ([7.3.18](/7.3.18)). The intestinal epithelium secretes chloride and water; the resulting watery diarrhoea can exceed a litre an hour and kills by hypovolaemia, not by tissue damage. The epithelium is intact throughout, which is why oral rehydration with a glucose–salt solution is curative: the sodium–glucose cotransporter still works. The heat-labile enterotoxin LT of enterotoxigenic *E. coli* is a close homologue, and *pertussis toxin* performs the opposite modification, ADP-ribosylating the inhibitory $G_{\mathrm{i}}\alpha$ so that it can no longer be activated — again raising cAMP.
- *Botulinum and tetanus toxins* (*Clostridium botulinum*, *C. tetani*) are zinc endopeptidases that cleave the SNARE proteins of neuronal vesicle fusion ([7.3.8](/7.3.8), [7.16](/7.16)); without SNARE function no neurotransmitter is released. The two toxins are homologous and differ in where they go. Botulinum toxin stays in the periphery and silences the motor neuron at the neuromuscular junction, giving flaccid paralysis; tetanus toxin is transported retrogradely to the spinal cord and acts on the inhibitory interneurons that restrain motor neurons, so the motor neurons fire unopposed and the paralysis is spastic. Both can kill by paralysing the respiratory muscles. The same mechanism, applied locally in minute amounts, is used therapeutically for dystonia, spasticity and strabismus, and cosmetically for wrinkles.
- *Shiga toxin* (*Shigella dysenteriae*, and Shiga-toxin-producing *E. coli* such as O157:H7, again phage-encoded) is an N-glycosidase that removes a single adenine from the 28S rRNA of the large ribosomal subunit, preventing elongation-factor binding and stopping translation. Its B pentamer binds the glycolipid Gb3, which is abundant on renal endothelium — hence haemolytic uraemic syndrome. Ricin, from the castor bean, has the same enzymatic activity, an example of convergence between a bacterial and a plant toxin.

**Remark 33.6.1** ADP-ribosylation — transfer of the ADP-ribose of NAD⁺ to a protein side chain — recurs across unrelated toxins (diphtheria, cholera, pertussis, *P. aeruginosa* exotoxin A, several injected effectors). It is a convenient chemistry for a toxin: the donor NAD⁺ is abundant in every cell, the modification is essentially irreversible on the timescale of the infection, and the target is a protein that the cell cannot do without.

## 33.7. Pore-Forming Toxins

**Definition 33.7.1 (Pore-Forming Toxin)** A **pore-forming toxin** is secreted as a soluble monomer, binds a lipid or protein receptor in the target membrane, oligomerizes, and refolds into a transmembrane channel. Because the activity is destroyed by a membrane, not by an intracellular target, these toxins act on whatever cells they reach.

**Definition 33.7.2 (Hemolysin)** A **hemolysin** is a toxin that lyses erythrocytes. The name reflects the assay rather than the target — the zone of clearing around a colony on blood agar is easy to read, and is used for identification ([7.11.16](/7.11.16)) — and most hemolysins lyse many other cell types, often more importantly.

- The *α-hemolysin* of *S. aureus* is the structural paradigm. Seven monomers assemble on the membrane into a pre-pore, then each contributes a β-hairpin to a 14-stranded β-barrel that spans the bilayer. The pore is small (about 1.4 nm), so the cell dies by osmotic imbalance and loss of potassium rather than by escape of macromolecules. The same protein, engineered, is the sensing pore of some nanopore sequencers ([7.8.1](/7.8.1)).
- *Cholesterol-dependent cytolysins* — listeriolysin O, streptolysin O, pneumolysin, perfringolysin O — bind membrane cholesterol, oligomerize into rings of 30 to 50 subunits and open pores tens of nanometres across, large enough for proteins to pass. Listeriolysin O is remarkable for its regulation: it is maximally active near pH 5.5 and nearly inactive at neutral pH, so it perforates the acidified phagosome and lets the bacterium escape, but does not lyse the host cell from within the cytosol, where the bacterium needs its host alive ([7.11.34](/7.11.34#sec-34.4)).
- *Phospholipases* destroy the membrane enzymatically rather than by insertion. The α-toxin of *C. perfringens* is a phospholipase C (a lecithinase) that hydrolyses phosphatidylcholine and sphingomyelin; in a deep wound with poor blood supply it produces the spreading tissue necrosis of gas gangrene.
- *Leukocidins* such as the Panton–Valentine leukocidin of *S. aureus* are bicomponent β-barrel pores targeted to leukocytes by binding chemokine receptors, and so are both cytolysins and immune-evasion factors ([7.11.34](/7.11.34#sec-34.2)).

## 33.8. Superantigens

**Definition 33.8.1 (Superantigen)** A **superantigen** is a protein that binds outside the antigen-binding groove, crosslinking MHC class II on an antigen-presenting cell to a particular variable β region of the T-cell receptor. Because specificity for a peptide is bypassed, every T cell carrying that Vβ segment is activated — of the order of 5–30 % of the T-cell population, against the 0.01–0.1 % activated by a conventional antigen.

The consequence is not immunity but a massive, synchronous release of inflammatory cytokines — a *cytokine storm* — producing fever, capillary leak, hypotension, shock and multi-organ failure. Toxic shock syndrome toxin 1 and several staphylococcal enterotoxins, and the streptococcal pyrogenic exotoxins, act this way; the staphylococcal enterotoxins additionally cause vomiting when ingested, and because they are preformed in the food and heat-stable, the illness begins within a few hours and cooking does not prevent it.

The clonal expansion is followed by deletion and anergy of the responding T cells, which leaves a hole in the repertoire; the host is therefore damaged twice. Why superantigen activity is selected for is not settled: suppressing an effective specific response, and the tissue damage and fluid loss that aid transmission, are both plausible contributions.

## 33.9. Endotoxin and the Inflammatory Cascade

**Endotoxin** is not secreted and is not a protein. It is the lipopolysaccharide of the Gram-negative outer membrane ([7.11.2](/7.11.2)) — lipid A anchoring a core oligosaccharide and a repeating O-antigen — and its toxicity resides in lipid A. LPS is released when cells divide, lyse, or are killed by an antibiotic or by complement.

![From lipopolysaccharide to inflammation. Lipid A is extracted from a bacterial surface by LPS-binding protein, handed to CD14 and delivered to the TLR4–MD-2 complex; MD-2 holds the acyl chains, and binding dimerizes the receptor. Signalling through MyD88 and TRIF activates NF-κB and IRF3, and the cell transcribes TNF-α, IL-1β, IL-6 and type I interferons; cytosolic LPS is sensed separately by caspase-11/4/5, which triggers pyroptosis. Locally these cytokines produce the useful response — vasodilation, recruitment of neutrophils, fever; systemically they produce the damaging one — widespread vasodilation and capillary leak, coagulation, falling blood pressure, septic shock. The number of acyl chains on lipid A sets the potency: the hexa-acylated lipid A of *Escherichia coli* is a strong agonist, the tetra-acylated lipid A made by *Yersinia pestis* at 37 °C is nearly silent, and modifications that add aminoarabinose also reduce binding of cationic antimicrobial peptides ([7.11.34](/7.11.34#sec-34.2)). The immunology beyond cytokine release belongs to [7.15](/7.15)](./plots/lps-inflammation.py)

The signalling is the best-characterized example of innate recognition of a **pathogen-associated molecular pattern**. LPS-binding protein and CD14 deliver lipid A to the TLR4–MD-2 complex at the cell surface; MD-2 accommodates the acyl chains in a hydrophobic pocket, and the ligand bridges two receptor complexes into a dimer, which recruits adaptors and activates NF-κB and the interferon regulatory factors. The result is transcription of TNF-α, IL-1β, IL-6 and other mediators. A second, cytosolic route — caspase-11 in mice, caspases 4 and 5 in humans, binding lipid A directly — triggers the inflammatory cell death called pyroptosis.

At a local focus this cascade is protective. Systemically it is the disease: fever, tachycardia, falling lymphocyte and platelet counts, activation of complement and of the coagulation cascade, disseminated intravascular coagulation, vasodilation and shock. Nothing in this sequence requires living bacteria, which has two practical consequences. Killing a heavy Gram-negative infection with a bactericidal antibiotic transiently worsens the inflammatory state as LPS is released from lysed cells. And injectable pharmaceuticals must be free of LPS, not merely sterile, since autoclaving destroys the organisms but not the heat-stable lipid A; the standard test exploits the clotting of amoebocyte lysate from the horseshoe crab *Limulus polyphemus* by picogram quantities of endotoxin, now increasingly replaced by recombinant factor C assays that spare the animals.

| | Exotoxin | Endotoxin |
|---|---|---|
| Chemistry | protein | lipopolysaccharide (lipid A) |
| Source | secreted by living Gram-positive and Gram-negative bacteria | outer membrane of Gram-negative bacteria, released on lysis |
| Heat stability | usually destroyed above 60 °C (staphylococcal enterotoxins excepted) | stable to autoclaving |
| Potency | very high; nanogram quantities | comparatively low; microgram quantities |
| Specificity | one molecular target per toxin; distinct syndromes | one general syndrome: fever, inflammation, shock |
| Immunology | strongly antigenic; neutralized by antitoxin; convertible to toxoid | poor antigen; no useful toxoid |
| Genetics | often phage-, plasmid- or island-encoded | chromosomal, part of envelope synthesis |

## 33.10. Where Virulence Genes Come From

Virulence genes are conspicuously mobile. They cluster in **pathogenicity islands** — chromosomal regions of tens to hundreds of kilobases whose GC content and codon usage differ from the rest of the genome, flanked by direct repeats and often inserted at a tRNA gene, frequently carrying an integrase ([7.11.13](/7.11.13)). Everything about them says recent horizontal acquisition. The *Salmonella* pathogenicity islands SPI-1 and SPI-2, each encoding a complete type III secretion system with its effectors, are the standard example; the locus of enterocyte effacement of enteropathogenic *E. coli* is another.

Other virulence determinants ride on plasmids (the invasion plasmid of *Shigella*, the toxin and capsule plasmids of *Bacillus anthracis*, the heat-labile and heat-stable enterotoxins of enterotoxigenic *E. coli*) or on prophages. Conversion of a harmless strain into a pathogen by lysogeny — **lysogenic conversion** ([7.11.23](/7.11.23)) — accounts for an impressive list: diphtheria toxin, cholera toxin (on the filamentous phage CTXφ, whose receptor is the toxin-coregulated pilus, so the two main virulence factors of *V. cholerae* are acquired together), Shiga toxin, botulinum toxin, the streptococcal pyrogenic exotoxins, and the Panton–Valentine leukocidin.

Two general points follow. First, virulence can appear suddenly in a lineage, by a single transfer event, rather than evolving gradually — and the same mobility carries resistance genes, which is why resistance and virulence often travel together ([7.11.15](/7.11.15)). Second, a toxin whose gene is carried by a phage is, from the phage's point of view, a phage gene; selection on it includes selection acting on the phage, which may favour properties that do the bacterium no good at all.

Why virulence persists at all is an evolutionary question, treated with the transmission–virulence trade-off in [7.10.17](/7.10.17#sec-17.2). The microbiological complement to that argument is that much virulence is *coincidental*: the factors that make *Listeria* a dangerous pathogen are those that let it survive in soil amoebae, and the toxins of *C. tetani* and *C. botulinum* bring the organism no transmission benefit whatever, since the intoxicated host is a dead end. Pathogenesis is in large part a by-product of adaptation to other environments.

## Summary

- **Pathogenicity** is the ability to cause disease, **virulence** its degree (Definition 33.1.1); both depend on the strain, the route and the host, and **opportunistic pathogens** cause disease only when host defences fail.
- Virulence is quantified by ID₅₀ and LD₅₀ (Definition 33.2.1). Under independent action, $P(\text{infection}) = 1 - \mathrm{e}^{-rd}$ (Eq. 33.1), so there is no threshold dose and $\mathrm{ID}_{50} = \ln 2/r$; observed values range over seven orders of magnitude.
- An infection proceeds through entry at a portal, adhesion, colonization, invasion and spread, damage, and shedding. Mucosal surfaces are the usual entry, and M cells a standard weak point.
- **Adhesins** (Definition 33.4.1) at pilus tips or on the cell surface bind specific host receptors and set tissue tropism; Gram-negative pili are assembled by the chaperone–usher pathway, Gram-positive pili covalently by **sortases**.
- Invasion uses degradative enzymes, induced uptake by the zipper (internalin–E-cadherin) or trigger (injected effectors) mechanism, and cytosolic spread on actin comet tails. Iron is withheld by nutritional immunity and won back by **siderophores**, by receptors for host iron proteins, and by lysing host cells.
- **Exotoxins** (Definition 33.6.1) fall into three classes: **AB toxins** (Definition 33.6.2) deliver an enzyme into the cytosol (diphtheria and cholera toxins ADP-ribosylate EF-2 and $G_{\mathrm{s}}\alpha$; botulinum and tetanus toxins cleave SNAREs; Shiga toxin depurinates 28S rRNA); **pore-forming toxins** (Definition 33.7.1) perforate membranes; **superantigens** (Definition 33.8.1) crosslink MHC II to TCR Vβ and cause a cytokine storm.
- **Endotoxin** is lipid A, recognized by TLR4–MD-2 and by cytosolic caspases; it provokes a single inflammatory syndrome ending in septic shock, is heat-stable, and is the reason injectables must be endotoxin-free.
- Virulence genes cluster in **pathogenicity islands** and on plasmids and prophages, so virulence can be acquired in one horizontal transfer; much of it is a by-product of adaptation to environments other than the host.

## Questions

1. A strain has ID₅₀ = $10^3$ cells in a given host and route. Under independent action, what is the probability that a dose of 10 cells establishes infection, and what does the answer say about "minimum infectious dose"?

   **Answer** From $\mathrm{ID}_{50} = \ln 2/r$, $r = 0.693/10^3 = 6.93\times10^{-4}$. For $d = 10$, $P = 1 - \mathrm{e}^{-6.93\times10^{-3}} \approx 0.0069$, about 0.7 %. The model has no threshold: small doses infect rarely but not never, so a quoted minimum infectious dose describes the dose at which infections become common in a group of hosts, not a barrier below which infection is impossible.

2. Cholera toxin and Shiga toxin are both AB toxins delivered to the cytosol, but cholera causes massive watery diarrhoea with an intact epithelium while Shiga toxin causes bloody diarrhoea and kidney damage. Explain both differences from the molecular targets.

   **Answer** Cholera toxin ADP-ribosylates $G_{\mathrm{s}}\alpha$, locking adenylate cyclase on; the enterocyte stays alive but secretes chloride and water, so the fluid loss is enormous and the mucosa is undamaged — hence the effectiveness of oral rehydration, since glucose-coupled sodium uptake is unaffected. Shiga toxin depurinates the 28S rRNA and kills the cell outright, so the colonic mucosa is destroyed (blood in the stool); its B subunit binds Gb3, which is abundant on renal endothelium, so toxin entering the circulation damages the kidney and produces haemolytic uraemic syndrome.

3. Why does listeriolysin O have a sharp pH optimum near 5.5, and what would you expect of a mutant whose toxin were equally active at pH 7?

   **Answer** The toxin must perforate the acidified phagosome to let the bacterium reach the cytosol, but must not damage the membranes of the host cell once there, because *L. monocytogenes* replicates in a living cytoplasm and spreads directly into neighbours. A mutant active at neutral pH would lyse the host cell from within, killing its own niche, exposing the bacteria to antibody, complement and phagocytes, and preventing cell-to-cell spread; such mutants are attenuated.

4. Both a superantigen and endotoxin can cause shock with fever and hypotension. Compare the two routes, and say why neither requires living bacteria at the site of damage.

   **Answer** A superantigen crosslinks MHC II to TCR Vβ, activating up to a third of T cells regardless of specificity and provoking a cytokine storm. Endotoxin acts on innate cells: lipid A binds TLR4–MD-2 (and cytosolic caspases), inducing TNF-α, IL-1β and IL-6. Both converge on the same mediators, hence the similar picture. Neither needs a living organism: the superantigen is a preformed, secreted protein that can act after being absorbed from food or from a localized focus, and endotoxin is a heat-stable cell-wall component that acts after the cells have been killed — which is why antibiotic therapy of a heavy Gram-negative infection can transiently worsen the shock.

5. A clinical isolate of *E. coli* produces Shiga toxin. What do you predict about the location of the toxin gene, and what practical consequence does the prediction have for the hospital laboratory and for treatment?

   **Answer** Shiga toxin in *E. coli* is carried by a lambdoid prophage, so the gene is expected in a prophage region rather than in the core genome, and it can spread to other strains by transduction. Induction of the prophage — for instance by the SOS response ([7.2.8](/7.2.8)) — both increases toxin production and lyses the cells, releasing it. Hence the laboratory should detect the toxin or its gene rather than rely on serotype alone, and antibiotics that induce the SOS response are generally avoided in this infection, since they can increase toxin release and the risk of haemolytic uraemic syndrome.
