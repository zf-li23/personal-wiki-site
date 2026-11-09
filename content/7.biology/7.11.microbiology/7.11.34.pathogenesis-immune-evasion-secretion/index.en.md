---
title: "Bacterial Pathogenesis II: Immune Evasion, Intracellular Life and Secretion Systems"
description: "The defensive side of pathogenesis: what a bacterium must survive, how capsules, surface proteins and lipid A modification defeat phagocytes, complement and antimicrobial peptides, how antigenic and phase variation outrun antibodies, how intracellular pathogens live in or out of the phagosome, the Sec, Tat and type I–VII secretion systems that deliver every one of these factors, and how pathogens arise by gene gain and gene loss."
---

A pathogen that could only attack would not last an hour. The factors of [7.11.33](/7.11.33) operate inside a host that is simultaneously trying to engulf, lyse, starve and neutralize the organism, and most of what distinguishes a successful pathogen from a harmless relative is defensive. This chapter follows that defense through three scales: molecules that disable individual host mechanisms, the intracellular lifestyle that places the bacterium beyond most of them, and the secretion machinery that puts all these proteins where they must act. It closes with the genomics of how a pathogen comes into existence, by gain of genes and equally by their loss.

Only as much immunology is given as the pathogen must deal with; the cells, receptors and development of the immune system are [7.15](/7.15). Protein targeting in eukaryotes, which the Sec system resembles, is [7.3.6](/7.3.6); the mobile elements that carry these genes are [7.11.13](/7.11.13).

## 34.1. What the Pathogen Must Survive

Four layers of defense meet a bacterium that has reached host tissue.

- *Barriers and chemistry*: intact epithelium, mucus and its flow, acid, bile, lysozyme, lactoferrin, and the cationic *antimicrobial peptides* (defensins, cathelicidins) that insert into the negatively charged bacterial surface.
- The complement system: a cascade of serum proteins activated by bacterial surfaces directly, by bound antibody, or by mannose-binding lectin. Its three products matter to a bacterium: C3b deposited on the surface *opsonizes* it for phagocytes, C5a recruits and activates them, and C5b–C9 assembles the membrane attack complex, which lyses Gram-negative cells whose outer membrane it can reach.
- *Phagocytes*: neutrophils and macrophages, which bind the organism (directly, or through receptors for C3b and for the Fc region of antibody), engulf it into a phagosome, fuse that with lysosomes, and attack it with acid, hydrolases, antimicrobial peptides, metal starvation, and the *oxidative burst* — a dedicated NADPH oxidase that consumes oxygen to make superoxide, from which hydrogen peroxide, hypochlorite and hydroxyl radical follow, together with nitric oxide from inducible nitric oxide synthase ([7.1.26](/7.1.26)).
- *Adaptive immunity*: antibody, which neutralizes toxins and adhesins, opsonizes, and activates complement; and T cells, which activate macrophages and kill infected cells.

Each of these has a counter, and the counters are the subject of the next three sections.

![What a pathogen must survive, and where each evasion strategy acts. From the left: antimicrobial peptides attack the surface, and are repelled by modification of lipid A with aminoarabinose or phosphoethanolamine. Complement deposits C3b and assembles the membrane attack complex, and is blocked by capsules that bind factor H, by proteases that cut C3b, and by long O-antigen that holds the complex away from the outer membrane. Phagocytes engulf and attack, and are defeated by capsules that prevent binding, by leukocidins that kill the cell, and by catalase, superoxide dismutase and peroxiredoxins that detoxify the oxidative burst. Antibody opsonizes and neutralizes, and is defeated by IgA proteases, by protein A binding IgG the wrong way round, and by antigenic and phase variation of the surface. The strategies are not alternatives: a pathogen such as *Streptococcus pneumoniae* uses several at once](./plots/host-defences-and-evasion.py)

## 34.2. Defeating Innate Immunity

### 34.2.1. Resisting Phagocytosis

The **capsule** ([7.11.3](/7.11.3)) is the commonest antiphagocytic factor. Being hydrophilic and often negatively charged, it prevents the phagocyte from making contact, and it hides surface-bound C3b from the phagocyte's receptors. Its importance is historical as well as biological: the smooth encapsulated and rough unencapsulated forms of *Streptococcus pneumoniae* differ by a factor of $10^5$ or more in virulence, and the transformation experiment that identified DNA as the genetic material was performed on that difference ([7.2.1](/7.2.1)). The M protein of *Streptococcus pyogenes* works similarly, as a fibrillar surface protein that both resists phagocytosis and recruits a host complement regulator.

Some organisms attack the phagocyte itself. The leukocidins of *Staphylococcus aureus* are pore-forming toxins directed at leukocytes by their chemokine receptors ([7.11.33](/7.11.33#sec-33.7)); *Yersinia* and *Pseudomonas* inject effectors that paralyze the actin cytoskeleton of the phagocyte so that engulfment fails altogether (§34.6).

### 34.2.2. Resisting Complement

*Serum resistance* is achieved in several ways. Surface proteins recruit the host's own complement regulators — factor H and C4b-binding protein — so that C3b deposited on the bacterium is inactivated as if it had landed on a host cell; the sialic acid of the *Neisseria meningitidis* capsule promotes the same factor H binding, which is also why that capsule is poorly immunogenic (§34.3). Long O-antigen chains hold the membrane attack complex at a distance from the outer membrane, so that smooth strains survive serum and rough derivatives of the same strain are lysed. Secreted proteases cleave C3b and C5a directly.

### 34.2.3. Resisting Antimicrobial Peptides

Cationic peptides are attracted by the negative charge of the envelope, so pathogens reduce it. The PhoP–PhoQ two-component system ([7.11.11](/7.11.11)) senses low magnesium and the peptides themselves and induces modification of lipid A: aminoarabinose and phosphoethanolamine are added to its phosphates, lowering the net negative charge, and the acyl chains are remodeled, which incidentally weakens TLR4 signaling ([7.11.33](/7.11.33#sec-33.9)). The same chemistry is what the plasmid-borne *mcr-1* gene performs constitutively, and it is the basis of transferable colistin resistance ([7.11.15](/7.11.15)).

### 34.2.4. Coagulase and the Fibrin Coat

*S. aureus* secretes coagulase, which converts host fibrinogen to fibrin without the normal clotting cascade; the organism coats itself and walls off the lesion. This localization is why staphylococcal infections tend to be abscesses, and the test for coagulase separates *S. aureus* from the less virulent coagulase-negative staphylococci ([7.11.16](/7.11.16)).

### 34.2.5. Surviving the Oxidative Burst

Catalase disposes of hydrogen peroxide, superoxide dismutases of superoxide, and peroxiredoxins and alkyl hydroperoxide reductases of the remaining peroxides; *Salmonella enterica* serovar Typhimurium carries four superoxide dismutases, two cytoplasmic and two periplasmic, the periplasmic ones protecting specifically against the burst delivered from outside. Mycobacteria add a thick, waxy, mycolic acid envelope that is simply hard to damage, and *Mycobacterium tuberculosis* uses its catalase-peroxidase KatG for the same purpose — the enzyme that also activates isoniazid, which is why resistance to that drug usually comes from *katG* mutations that cost the organism some of this protection ([7.11.15](/7.11.15)).

## 34.3. Defeating Adaptive Immunity

Antibody is the host's most specific weapon against an extracellular bacterium, so the strategies here are about making antibody useless.

### 34.3.1. Destroying or Misusing Antibody

Secretory IgA, the antibody of mucosal surfaces, is cut in its hinge region by IgA1 proteases secreted by *Neisseria gonorrhoeae*, *N. meningitidis*, *Haemophilus influenzae* and *S. pneumoniae* — all of them mucosal colonizers, a striking convergence. Protein A of *S. aureus* and protein G of some streptococci bind the Fc region of IgG, so that the antibody coats the bacterium upside down, its antigen-binding arms pointing outward and its Fc hidden, exactly the orientation that phagocyte Fc receptors cannot use. (The same binding makes protein A the standard reagent for purifying antibody.)

### 34.3.2. Looking like the Host

The capsule of *N. meningitidis* serogroup B is a polymer of sialic acid identical to a carbohydrate of human neural cell adhesion molecule; the capsule of *S. pyogenes* is hyaluronan, a normal matrix polysaccharide. Neither provokes a useful antibody response, because such a response would be autoimmune — which is also why there has never been a conventional polysaccharide vaccine against serogroup B, and why that vaccine was eventually made from surface proteins found by *reverse vaccinology*, a genome-wide search for surface-exposed antigens. Coating with host proteins — fibronectin, fibrinogen, transferrin — achieves the same concealment with less genetic investment.

### 34.3.3. Changing the Surface

Where concealment is impossible, variation works.

![Two mechanisms that change the bacterial surface. A: antigenic variation by gene conversion in *Neisseria gonorrhoeae*. One expressed pilin locus *pilE* has a promoter; 10–20 silent *pilS* cassettes do not. Recombination between the conserved regions copies a silent variable segment into *pilE*, producing a new pilin without changing the locus structure; with many cassettes and several variable regions per cassette, the number of possible surface variants is astronomical. B: phase variation by DNA inversion in *Salmonella*. An invertible segment carrying a promoter is flipped by the Hin recombinase: in one orientation the *fljB* flagellin and a repressor of *fliC* are transcribed; in the other, neither is, and the cell makes the *fliC* flagellin instead. The switch is reversible and occurs about once in $10^4$ cells per generation, far above the mutation rate, so the population always contains both phases. C: why this matters. In a simple model, antibody clears the current variant while a rare new variant escapes and grows, giving the waves of bacteremia characteristic of relapsing fever and of trypanosome infections](./plots/surface-variation.py)

**Antigenic variation** changes which version of a surface protein is made, while **phase variation** switches its expression on and off. Both are programmed: the variability is encoded, and the rate greatly exceeds the mutation rate.

- *Gene conversion.* In *N. gonorrhoeae*, the expressed pilin gene *pilE* is overwritten by segments copied from an array of promoterless *pilS* cassettes, generating new pilin sequences continuously within a single infection. Because the repertoire is combinatorial, no antibody response catches up, and infection confers no lasting immunity — one reason gonorrhea is reacquired repeatedly. *Borrelia burgdorferi* varies its VlsE lipoprotein the same way, and the relapsing-fever borreliae switch whole surface lipoproteins to produce successive waves of bacteremia.
- *DNA inversion.* The Hin recombinase of *Salmonella* inverts a segment carrying a promoter, switching between two flagellin genes; *Bacteroides* species in the gut invert promoters in front of capsular polysaccharide loci in the same way. The mechanism is the site-specific recombination of [7.11.13](/7.11.13).
- *Slipped-strand mispairing.* Short tandem repeats inside a coding sequence or promoter gain or lose a unit during replication, shifting the reading frame or changing promoter spacing, so the gene switches off and on stochastically. *H. influenzae* and *Neisseria* carry dozens of such *contingency loci*, mostly in surface structures — a genomic strategy of bet-hedging ([7.9.17](/7.9.17)).

The eukaryotic version of the same logic is the variant surface glycoprotein of African trypanosomes ([7.11.20](/7.11.20)), where a single VSG is expressed from a telomeric site out of a repertoire of over a thousand; the waves of parasitemia that result are the classical picture of antigenic variation, and the simple model in the figure reproduces them.

## 34.4. Life Inside Host Cells

**Definition 34.4.1 (Intracellular Pathogen)** An **intracellular pathogen** replicates inside host cells. *Facultative* intracellular pathogens (*Salmonella*, *Listeria*, *Legionella*, *M. tuberculosis*, *Brucella*) can also grow in culture; obligate intracellular pathogens — the **chlamydiae**, the **rickettsias** and *Coxiella burnetii* — cannot, having lost biosynthetic capacity in the course of adapting to a cytoplasm that supplies it.

The advantages are plain: a rich and constant supply of nutrients, shelter from antibody, complement and most antibiotics, and, if the host cell migrates, free transport. The price is that the cell must first be entered and then kept habitable, and that the host can kill the cell to deny the niche.

![Three fates of a bacterium inside a macrophage. Left: the normal course — the phagosome matures, acquires the vacuolar ATPase and acidifies, fuses with lysosomes, and the bacterium is destroyed by hydrolases, peptides and the oxidative burst. Center: arrest of maturation. *Mycobacterium tuberculosis* retains coronin 1 on the vacuole, excludes the proton pump and secretes the phosphatase SapM, so the compartment never becomes a phagolysosome; *Legionella pneumophila* goes further and converts its vacuole into a compartment derived from the endoplasmic reticulum, using about three hundred effectors injected by its Dot/Icm type IV secretion system; *Salmonella* remodels its vacuole with effectors of SPI-2. Right: escape into the cytosol. *Listeria monocytogenes* perforates the vacuole with listeriolysin O and phospholipases, replicates in the cytosol and moves by polymerizing actin into a comet tail, pushing into the neighboring cell; *Shigella* does the same with its own effectors](./plots/intracellular-fates.py)

### 34.4.1. Arresting the Phagosome

*M. tuberculosis* prevents the recruitment of the vacuolar proton ATPase and the fusion with lysosomes, retaining host coronin 1 on the vacuolar membrane and secreting a phosphatase that destroys the phosphatidylinositol 3-phosphate required for maturation; the compartment stays at an early endosomal stage and near-neutral pH. The bacterium then persists, often for the host's lifetime, inside the organized macrophage aggregate called a granuloma — a structure that is as much a bacterial habitat as a host containment device, since reactivation years later begins there, and since the caseous center of a granuloma eroding into an airway is how the organism is transmitted.

### 34.4.2. Rebuilding the Vacuole

*L. pneumophila*, whose natural hosts are freshwater amoebae, injects effectors through the Dot/Icm type IV system that intercept vesicles from the endoplasmic reticulum; within an hour the vacuole is studded with ER-derived vesicles and ribosomes and is invisible to the endocytic pathway. That human disease is an accident of this adaptation is clear from the ecology: Legionnaires' disease appeared with cooling towers, showers and air-conditioning systems — devices that aerosolize amoeba-laden water into human lungs, where alveolar macrophages behave enough like amoebae to be exploited.

### 34.4.3. Escaping to the Cytosol

*L. monocytogenes* lyses the vacuolar membrane with listeriolysin O, whose acid optimum confines its activity to the vacuole ([7.11.33](/7.11.33#sec-33.7)), and enters the cytosol, where it grows rapidly and spreads by actin-based motility ([7.3.13](/7.3.13)). The cytosol is not an empty refuge — it contains its own sensors, and bacteria that enter it are targeted by autophagy ([7.3.11](/7.3.11)) — so cytosolic pathogens also carry proteins that prevent their recognition and ubiquitination.

## 34.5. Getting Proteins Out: Sec, Tat and the Gram-Positive Surface

Every factor described so far has to be exported. Two general systems move proteins across the cytoplasmic membrane of bacteria and archaea, and both are ancient enough to be homologous to the eukaryotic machinery ([7.3.6](/7.3.6)).

**Definition 34.5.1 (Sec Pathway)** The **Sec pathway** translocates *unfolded* polypeptides through the SecYEG channel in the cytoplasmic membrane. Substrates carry an N-terminal signal peptide — a few positive residues, a hydrophobic core and a cleavage site — that is removed by signal peptidase during export.

Sec operates in two modes. In *post-translational* export, which carries most secreted proteins, the chaperone SecB binds the newly made protein and keeps it unfolded, and the ATPase motor SecA threads it through SecYEG, powered by cycles of ATP binding and hydrolysis together with the proton motive force. In *co-translational* insertion, which builds membrane proteins, the signal recognition particle binds a hydrophobic segment as it leaves the ribosome, docks at the membrane receptor FtsY, and translation itself pushes the chain into SecYEG, from which transmembrane helices partition laterally into the lipid. The insertase YidC assists this, and inserts some small membrane proteins by itself.

**Definition 34.5.2 (Tat Pathway)** The **twin-arginine translocation pathway** exports proteins that are already *folded*, recognizing a signal peptide containing an S-R-R-x-F-L-K motif. TatBC binds the signal, TatA assembles into a transient pore of a size matched to the substrate, and the proton motive force drives the transport.

Transporting a folded protein looks wasteful until one asks what cannot be done otherwise. Proteins that bind a cofactor — a molybdopterin, an iron–sulfur cluster — must acquire it in the cytoplasm where it is made; proteins that must bind the correct metal in competition with others do better in the controlled cytoplasmic environment; and a hetero-oligomer can be assembled inside and exported as a unit, with a signal peptide on only one subunit. Many respiratory enzymes of the periplasm therefore travel by Tat, and so do a few virulence factors, including the phospholipase C of *P. aeruginosa*.

### 34.5.1. The Gram-Positive Problem

With no outer membrane, a protein that crosses the cytoplasmic membrane of a Gram-positive cell is already outside, and will diffuse away unless it is retained. Three solutions are used: lipoprotein anchors, non-covalent binding domains that grip peptidoglycan or teichoic acid, and covalent attachment.

**Definition 34.5.3 (Sortase)** A **sortase** is a membrane-anchored transpeptidase of Gram-positive bacteria that recognizes a C-terminal sorting signal, usually LPXTG, cleaves it, and joins the protein covalently to the cross-bridge of peptidoglycan. Housekeeping sortases anchor surface adhesins and enzymes; specialized sortases polymerize pilin subunits into covalent pili ([7.11.33](/7.11.33#sec-33.4)).

Because one enzyme anchors many substrates, sortase mutants lose a whole class of surface proteins and are strongly attenuated, which makes sortase a target for anti-virulence compounds. The reaction is also a convenient laboratory tool — *sortagging* attaches almost any peptide to a protein bearing the motif.

Mycobacteria, whose mycolic acid outer layer is a barrier of its own, add the *type VII secretion system* (ESX): ESX-1 exports the small proteins ESAT-6 and CFP-10, which permeabilize host membranes and are required for virulence, and the region of the genome encoding it, RD1, is deleted in the BCG vaccine strain — which is precisely why BCG is attenuated.

## 34.6. The Secretion Systems of Gram-Negative Bacteria

**Definition 34.6.1 (Secretion System)** A **secretion system** is a machine that transports proteins across the bacterial envelope, to the surface, to the medium, or directly into another cell. In Gram-negative bacteria they are numbered T1SS to T6SS and divide into those that work in one step from the cytoplasm and those that take up substrates already delivered to the periplasm by Sec or Tat.

![The secretion systems of a Gram-negative bacterium, drawn against the envelope. Sec and Tat cross the inner membrane only. Sec-dependent systems take over in the periplasm: the T2SS pushes folded substrates through an outer-membrane secretin with a periplasmic pseudopilus (cholera toxin leaves this way); the T5SS autotransporter inserts its own β-barrel and threads its passenger domain through it (IgA proteases); the chaperone–usher pathway assembles pili. One-step systems span both membranes: the T1SS is an ABC transporter joined to an outer-membrane channel by an adaptor (α-hemolysin); the T3SS is a needle that injects effectors into a eukaryotic cell on contact, evolutionarily related to the flagellar export apparatus; the T4SS transfers both proteins and DNA, and is the machine of conjugation; the T6SS is an inverted contractile phage tail that fires a spike into a neighboring cell, bacterial or eukaryotic. Gram-positive bacteria use sortases, and mycobacteria the T7SS](./plots/secretion-systems.py)

| System | Steps | Energy and core parts | Typical cargo |
|---|---|---|---|
| T1SS | one step, cytoplasm to medium | ABC transporter, membrane fusion protein, TolC | α-hemolysin of *Escherichia coli*, RTX toxins, proteases |
| T2SS | two steps, Sec or Tat then out | secretin, periplasmic pseudopilus extended by an ATPase | cholera toxin, exotoxin A, hydrolytic enzymes |
| T3SS | one step, into a eukaryotic cell | basal body plus needle with a tip translocon; proton motive force and an ATPase; homologous to the flagellar export apparatus | effectors of *Salmonella*, *Shigella*, *Yersinia*, enteropathogenic *E. coli* |
| T4SS | one step, into a cell or into the medium | coupling protein, inner- and outer-membrane complexes, pilus | conjugative DNA; T-DNA of *Agrobacterium*; the effectors of *Legionella* and *Coxiella*; CagA of *Helicobacter pylori* |
| T5SS | two steps, Sec then self-export | autotransporter: a β-barrel domain carrying its own passenger | IgA proteases, pertactin, the vacuolating cytotoxin VacA |
| T6SS | one step, into a neighboring cell | an inverted, contractile phage-tail-like sheath with an Hcp tube and a VgrG–PAAR spike, recycled by ClpV | antibacterial effectors (and some anti-eukaryotic ones) |

Three of these deserve more than a table entry.

### 34.6.1. The Type III Secretion System

The *type III secretion system* is a syringe: a basal body spanning both membranes, a hollow needle of a length set by a molecular ruler, and a tip complex that, on contact with a target membrane, forms a pore through which effectors pass directly into the host cytosol. Chaperones hold the effectors unfolded and deliver them in order to an ATPase at the base. Delivering a toxin this way avoids neutralizing antibody entirely, which no secreted toxin can do. The homology to the flagellum — shared components, the same export chemistry, the same ruler-controlled assembly — is one of the clearest cases of a complex machine being recruited for a new function ([7.11.3](/7.11.3)).

The injected proteins — the *effector proteins* — then rewrite the host cell. The repertoires are large (tens for *Salmonella*, hundreds for *Legionella*) and the targets are the hubs of cell biology: Rho-family GTPases, whose activation and subsequent inactivation produce the membrane ruffle of trigger-mechanism entry ([7.11.33](/7.11.33#sec-33.5)); phosphoinositides and the vesicle-trafficking machinery, remodeled to build a replicative vacuole; NF-κB signaling, suppressed to delay inflammation; and cell death pathways, blocked or triggered as the infection requires. Enteropathogenic *E. coli* even injects the receptor for its own adhesin — Tir is translocated into the host membrane, where intimin on the bacterium binds it and the underlying actin is reorganized into the pedestal on which the bacterium sits.

### 34.6.2. The Type IV Secretion System

The *type IV secretion system* is the one machine that moves both DNA and protein, and the relationship is historical: conjugation systems ([7.11.13](/7.11.13)) and effector translocators are variants of the same apparatus. *Agrobacterium tumefaciens* transfers T-DNA and proteins into plant cells with its VirB/VirD4 system, which is how plants are transformed in the laboratory ([7.12](/7.12)); *H. pylori* injects CagA, which perturbs epithelial polarity and signaling and is associated with gastric cancer; *Legionella* and *Coxiella* use Dot/Icm to build their vacuoles.

### 34.6.3. The Type VI Secretion System

The *type VI secretion system* is an inverted bacteriophage tail. A baseplate anchored to the inner membrane assembles an Hcp tube tipped with a VgrG–PAAR spike inside a contractile sheath; when the sheath contracts, the spike with its attached effectors is driven out of the cell and into whatever is adjacent — no receptor is needed, only proximity. Most of its effectors are antibacterial: peptidoglycan hydrolases, phospholipases, nucleases, NAD⁺ glycohydrolases. Each is paired with an immunity protein that neutralizes it in sister cells, so a T6SS is a kin-discriminating weapon, and the arms race of toxin and immunity pair is one of the fastest-evolving parts of these genomes. The system is therefore as much an ecological instrument as a virulence factor: *Vibrio cholerae* uses it to clear competitors from the gut, *Pseudomonas aeruginosa* to counterattack precisely at the point where it was struck, and gut *Bacteroides* to structure their communities ([7.11.29](/7.11.29), [7.11.32](/7.11.32)).

## 34.7. How Pathogens Evolve: Gene Gain and Gene Loss

Comparative genomics gives a consistent picture of how a pathogen arises from a non-pathogen.

### 34.7.1. Gain

Pathogenicity islands, virulence plasmids and prophages deliver whole machines at once — a complete type III secretion system with its effectors, a capsule locus, a toxin ([7.11.33](/7.11.33#sec-33.10)). The islands are recognizable by their deviant GC content and codon usage, their insertion next to tRNA genes, their flanking repeats and their integrase genes. The result is punctuated: a single conjugation or transduction event can create a pathogenic lineage.

![Gene gain and gene loss. A: a pathogenicity island in a genome browser view. The GC content over the island departs from that of the rest of the chromosome, betraying a different ancestry; the island is inserted next to a tRNA gene, carries an integrase at one end and is flanked by direct repeats; the genes inside encode a secretion apparatus, its effectors and a regulator, and the whole block is absent from closely related non-pathogenic strains. B: the complementary process. Host-restricted lineages lose what the host supplies: *Shigella flexneri* is *Escherichia coli* that gained an invasion plasmid and inactivated its flagellar genes and *cadA*; *Mycobacterium leprae* carries about 1600 pseudogenes in a genome a megabase smaller than that of *M. tuberculosis*; *Rickettsia prowazekii* has shed most biosynthesis. Gain and loss are independent, and a pathogen is usually the product of both](./plots/pathogenicity-island.py)

### 34.7.2. Loss

Equally characteristic, and less intuitive, is decay. *Shigella* is not a separate genus in any phylogenetic sense — it is *E. coli* that has acquired an invasion plasmid and then lost function in genes incompatible with its lifestyle: *cadA*, whose lysine decarboxylase product would interfere with the enterotoxin, and the flagellar genes, which make an expensive and highly antigenic structure that an intracellular organism does not need. Pseudogenes accumulate wherever selection is relaxed: *Mycobacterium leprae* has about 1600 pseudogenes and a genome of 3.3 Mb against 4.4 Mb for *M. tuberculosis*, and the **rickettsias** and **chlamydiae** have gone further, shedding biosynthetic pathways that their host cytoplasm supplies. The process is the genome reduction of host-restricted lineages generally ([7.10.18](/7.10.18#sec-18.8)), and it is the reason obligate intracellular pathogens are hard to culture.

### 34.7.3. No Sharp Line between Pathogen and Commensal

Pathogen and commensal are ends of a continuum. *E. coli* spans it entirely: the core genome is shared, and the accessory genome decides whether a strain is a harmless colonist of the gut, a cause of cystitis, or a cause of hemolytic uremic syndrome ([7.11.13](/7.11.13)). *S. aureus* and *S. pneumoniae* are carried asymptomatically by a large fraction of healthy people and cause disease only occasionally. The same genes may be virulence factors in one context and colonization factors in another — adhesins, iron uptake, biofilm formation are all needed to live peacefully on a mucosal surface. Pathogenesis, in short, is a relation between an organism and a host, not a category of organism, and this is the microbiological content of the evolutionary argument in [7.10.17](/7.10.17#sec-17.2).

## Summary

- A pathogen must survive barriers and antimicrobial peptides, complement, phagocytes with their oxidative burst, and adaptive immunity; every one of these has well-characterized bacterial counters.
- Innate evasion: capsules and M protein prevent phagocytosis; recruitment of factor H, long O-antigen and proteases confer serum resistance; lipid A modification by PhoP–PhoQ (and by *mcr-1*) repels cationic peptides; catalase, superoxide dismutase and peroxiredoxins neutralize the oxidative burst; coagulase walls off the lesion.
- Adaptive evasion: IgA proteases; protein A binding IgG by its Fc; molecular mimicry by sialic acid and hyaluronan capsules; and programmed variation — gene conversion of *pilE* from *pilS* cassettes (**antigenic variation**), DNA inversion by Hin (**phase variation**), and slipped-strand mispairing at contingency loci.
- **Intracellular pathogens** (Definition 34.4.1) either arrest phagosome maturation (*M. tuberculosis*), rebuild the vacuole from the ER (*L. pneumophila*) or escape into the cytosol and move on actin tails (*L. monocytogenes*).
- The **Sec pathway** (Definition 34.5.1) exports unfolded proteins through SecYEG, post-translationally with SecB and SecA or co-translationally with the signal recognition particle; the **Tat pathway** (Definition 34.5.2) exports folded, cofactor-loaded proteins; Gram-positive bacteria retain surface proteins with **sortases** (Definition 34.5.3), and mycobacteria add the type VII system.
- **Secretion systems** T1SS–T6SS (Definition 34.6.1) differ in whether they cross one membrane or two and whether they deliver into a target cell: the **type III secretion system** injects **effector proteins** that rewrite host signaling and the cytoskeleton; the **type IV secretion system** transfers protein and DNA and is the conjugation machine; the **type VI secretion system** is an inverted phage tail used mainly against other bacteria, with cognate immunity proteins.
- Pathogens arise by gain of islands, plasmids and prophages and by loss of genes that no longer pay (*Shigella*, *M. leprae*, the **rickettsias**); commensal and pathogen are ends of a continuum rather than categories.

## Questions

1. A mutant of *Salmonella* lacking the PhoP–PhoQ system is avirulent in mice. Name two defenses it has become vulnerable to, and say why one of them would also change the host's inflammatory response to the organism.

   **Answer** PhoP–PhoQ induces lipid A modification (aminoarabinose, phosphoethanolamine) and other genes for survival inside the macrophage vacuole, so the mutant is killed by cationic antimicrobial peptides and fails to persist in macrophages. The lipid A changes also alter TLR4–MD-2 recognition: unmodified, hexa-acylated lipid A is a stronger agonist, so the mutant provokes a stronger early inflammatory response, which contributes further to its clearance.

2. Why can the type III secretion system deliver a toxin that no secreted toxin could deliver as effectively, and what evolutionary relationship does its structure reveal?

   **Answer** It injects effectors directly from the bacterial cytoplasm into the host cytosol on contact, so the proteins never appear in the extracellular fluid where neutralizing antibody could bind them; delivery is also targeted to the cell being manipulated. Structurally and genetically it is homologous to the flagellar export apparatus — same basal body architecture, same ruler-controlled length, shared components — so the injectisome is a flagellar machine recruited for protein injection.

3. Explain why the Tat pathway must exist when the Sec pathway already exports proteins, and give the property of a substrate that predicts Tat use.

   **Answer** Sec exports only unfolded chains, so a protein that must bind a cofactor made in the cytoplasm (molybdopterin, an iron–sulfur cluster), must select the right metal under controlled cytoplasmic conditions, or must be assembled as a hetero-oligomer before export cannot use it. Tat exports already-folded proteins, at the cost of a larger, transient pore and proton motive force. The predictor is the twin-arginine motif (S-R-R-x-F-L-K) in the signal peptide, and biochemically the need for a cytoplasmically acquired cofactor.

4. Antibody responses to *Neisseria gonorrhoeae* are vigorous but confer no lasting protection. Explain in terms of two distinct mechanisms, and state what this implies for vaccine design.

   **Answer** First, antigenic variation: *pilE* is continually overwritten by gene conversion from silent *pilS* cassettes, and several other surface antigens vary, so the population always contains variants not covered by existing antibody. Second, the organism secretes an IgA1 protease that destroys mucosal antibody, and surface sialylation recruits complement regulators, so even matched antibody works poorly. A vaccine must therefore be directed at conserved, functionally constrained surface molecules rather than at the immunodominant variable ones — the reverse-vaccinology approach taken against meningococcus B.

5. *Shigella* has a smaller genome than *Escherichia coli* and carries many pseudogenes, yet it is more virulent. How is this consistent, and what does it say about the relationship between the two organisms?

   **Answer** *Shigella* lineages are *E. coli* that acquired a large invasion plasmid (a gain of a complete type III secretion system and its effectors) and then lost functions that conflict with an intracellular, intracellularly spreading lifestyle — flagella, which are costly and highly antigenic, and *cadA*, whose product antagonizes the enterotoxin. Virulence came from gene gain, genome reduction from relaxed or antagonistic selection on the rest; the two processes are independent. Taxonomically, *Shigella* is not distinct from *E. coli*: the separate genus name is historical and clinical, not phylogenetic.
