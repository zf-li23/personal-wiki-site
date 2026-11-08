---
title: "Differentiation, Development and Biofilms in Bacteria"
description: "Development in prokaryotes: coexisting cell fates in Bacillus subtilis (motile, matrix-producing, competent, cannibal and sporulating cells) and the Spo0A phosphorelay; the morphological stages of sporulation and its compartmentalized sigma-factor cascade; germination; bet hedging in a fluctuating environment and Cohen's model; the asymmetric cell cycle of Caulobacter crescentus; the life cycle of Streptomyces; the social cycle of the myxobacteria; heterocysts and akinetes in cyanobacteria; and biofilms: the stages of formation, the matrix and extracellular DNA, c-di-GMP, division of labor, the gradients and the Thiele modulus, tolerance to antimicrobials, and where biofilms matter in nature and medicine."
---

Most prokaryotes divide into two cells like themselves, and the textbook picture of a bacterium is a single cell in a liquid. Both are poor descriptions of how bacteria usually live. In the field, cells are attached to surfaces in mixed communities; in a culture of one species, genetically identical cells adopt different states at the same time; and a few lineages build structures — stalks, spores, aerial hyphae, fruiting bodies — through programs that deserve the name development, with irreversible commitment, asymmetric division, intercellular signals and distinct cell fates.

This chapter collects those programs. It begins with the best-studied case of several fates coexisting in one population, *Bacillus subtilis*, and with the most elaborate prokaryotic developmental program, sporulation; it then asks why a population should split into states at all, which leads to the theory of **bet hedging**; and it goes on to the asymmetric cell cycle of *Caulobacter*, the mycelial life cycle of *Streptomyces*, the social cycle of the myxobacteria and the spaced differentiation of **heterocysts** in filamentous cyanobacteria. It ends with the commonest multicellular state of all, the biofilm. The regulatory devices used throughout — σ factors, two-component systems, quorum sensing, second messengers — are those of [7.11.11](/7.11.11); the structure and resistance of the mature **endospore** are in [7.11.3](/7.11.3#sec-3.3), the gene-expression waves of sporulation as a network motif in [7.9.15](/7.9.15#sec-15.5.5), the theory of noise and fate decisions in [7.9.17](/7.9.17#sec-17.1.4), and the patterning mathematics in [7.5.12](/7.5.12) and [7.6.36](/7.6.36#sec-36.6).

## 12.1. What "Development" Means in a Prokaryote

Four features distinguish a developmental program from ordinary regulation.

1. *Several fates in one genotype.* A starving culture of *B. subtilis* contains motile cells, matrix producers, competent cells, cannibals and sporulating cells at the same time, in proportions that depend on conditions but never reach 100 %.
2. *Asymmetric division.* The two products of a division differ: the small forespore and the large mother cell, the swarmer and the stalked cell of *Caulobacter*. Asymmetry requires that the division site be placed off-center, or that the two poles differ in age and composition ([7.3.21](/7.3.21), [Definition 21.5.1](/7.3.21#def-21.5.1) for the eukaryotic case).
3. *Commitment.* Beyond a certain point the program runs to completion even if the inducing conditions disappear. A *B. subtilis* cell that has engulfed its forespore cannot return to growth.
4. *Intercellular signaling.* Development is coordinated across a population (quorum sensing, the peptides of sporulation) or across a filament (the PatS peptide of *Anabaena*), and it often involves the sacrifice of some cells for others.

What prokaryotic development does not involve is a new mechanism: everything is built from the regulators of [7.11.11](/7.11.11). What is new is the architecture — feedback loops that make states mutually exclusive, cascades that keep two compartments in step, and signals that space differentiated cells apart.

## 12.2. Coexisting Cell Fates in *Bacillus subtilis*

As a culture of *B. subtilis* exhausts its nutrients, it does not take one decision but several, and different cells take different ones.

- *Motility.* σᴰ-controlled genes make flagella and the chemotaxis apparatus; motile cells are the "escape" option.
- *Matrix production.* The *epsA–O* and *tapA–sipW–tasA* operons make exopolysaccharide and the amyloid-like fiber protein TasA, the two components of the biofilm matrix. The repressor SinR keeps them off in growing cells; the antagonist SinI, induced by Spo0A, sequesters SinR and switches the fate on. Motility and matrix production are mutually exclusive, so a biofilm contains two visibly different subpopulations.
- *Competence.* About 10–20 % of cells in stationary phase take up DNA from the medium ([7.11.13](/7.11.13)). The master regulator ComK activates its own gene, and the positive loop combined with a slower negative one makes the circuit *excitable*: noise occasionally pushes a cell over the threshold, it becomes competent for a few hours, and then returns ([7.9.17](/7.9.17#sec-17.1.4)). The fraction, not the identity, of competent cells is determined.
- *Cannibalism.* Cells with intermediate Spo0A activity export the toxins SdpC and SkfA, which lyse their siblings that have not yet activated Spo0A, and protect themselves with the matching immunity proteins. The nutrients released delay the lysing cells' own commitment to sporulation — an expensive and irreversible step — so cannibalism buys time.
- *Sporulation.* The last resort, taken by cells in which Spo0A activity is highest.

The common hub is the master regulator Spo0A, which is phosphorylated not by a single kinase but by a phosphorelay: five sensor kinases (KinA–KinE), responding to starvation, redox state, DNA damage and the peptide signals of quorum sensing, phosphorylate Spo0F; Spo0B transfers the phosphate to Spo0A; and several phosphatases (RapA, RapB, Spo0E) drain the relay at different points. The relay thus integrates many inputs and many veto signals, and it converts them into a graded level of Spo0A-P: low activity switches on matrix production, intermediate activity cannibalism, high activity sporulation. One regulator with graded thresholds produces an ordered series of fates.

## 12.3. Sporulation

### 12.3.1. The Morphological Program

Sporulation in *B. subtilis* takes about eight hours and passes through stages that were numbered by electron microscopy in the 1960s. The chromosome is replicated and stretched into an axial filament (stage I); a septum forms near one pole, dividing the cell into a small forespore and a large mother cell, with about a third of one chromosome trapped in the forespore and the rest pumped in by the DNA translocase SpoIIIE (stage II); the mother cell membrane migrates around the forespore and fuses behind it, so that the forespore lies free in the mother cell cytoplasm, surrounded by two membranes (engulfment, stage III); the cortex, a modified peptidoglycan, is laid down between the two membranes and the coat proteins assemble outside (stages IV and V); the core is dehydrated to $10$–$25\,\%$ water, against $80$–$90\,\%$ in a vegetative cell, filled with calcium dipicolinate and its DNA saturated with small acid-soluble spore proteins (maturation, stage VI); and the mother cell lyses, releasing the spore (stage VII).

**Definition 12.3.1 (Sporulation)** **Sporulation** is the developmental program by which a vegetative cell is converted into a dormant spore. In endospore-forming bacteria it proceeds through an asymmetric division, engulfment of the forespore by the mother cell, synthesis of cortex and coat, maturation, and lysis of the mother cell, and it is irreversible after engulfment.

### 12.3.2. Two Compartments, Four σ Factors

What makes sporulation a model of development is that the two compartments express different genes in the right order, each checking the other's progress. Four alternative σ factors act in turn, two in each compartment, and each is activated only by a signal from the other side.

σᶠ is made before the septum forms but is held inactive by the anti-σ factor SpoIIAB ([Definition 11.4.1](/7.11.11#def-11.4.1)). The phosphatase SpoIIE accumulates at the septum and, acting only in the small compartment, dephosphorylates the anti-anti-σ factor SpoIIAA, which then takes SpoIIAB away from σᶠ: a partner switch that works in the forespore alone. Active σᶠ directs the transcription of SpoIIR, which crosses to the septal membrane and activates the protease SpoIIGA, which cuts pro-σᴱ to active σᴱ in the mother cell. σᴱ drives engulfment and cortex synthesis; when engulfment is complete, the SpoIIIA–SpoIIQ channel assembled across the two membranes feeds the forespore and allows σᴳ to become active there. σᴳ makes the small acid-soluble spore proteins and the machinery of germination, and also SpoIVB, which triggers the intramembrane protease SpoIVFB to process pro-σᴷ in the mother cell. σᴷ then directs coat synthesis and the lysis that releases the spore.

![Sporulation in *Bacillus subtilis*. A: the morphological stages, from the vegetative cell through the asymmetric septum, engulfment and the synthesis of cortex and coat to the lysis of the mother cell. B: the compartmentalized σ-factor cascade. The Spo0A phosphorelay commits the cell; σᶠ is released in the forespore by the SpoIIE–SpoIIAA–SpoIIAB partner switch, and each compartment then activates the next factor in the other one (diagonal arrows), so that gene expression and morphology stay in step](./plots/sporulation.py)

Within each compartment the σ factors drive waves of genes, shaped by linked feed-forward loops: σᴱ turns on early mother-cell genes and the repressor SpoIIID that turns them off again, and σᴱ with SpoIIID is needed for σᴷ, which with GerE produces two further waves ([Example 15.5.1](/7.9.15#ex-15.5.1)). The *B. subtilis* genome devotes several hundred genes to this program.

### 12.3.3. Germination

A spore is not inert but dormant, and its return to growth has three steps ([7.11.3](/7.11.3#sec-3.3.2)): activation, often by sublethal heat; germination proper, triggered within minutes when germinant receptors in the inner membrane bind specific nutrients (L-alanine, a mixture of asparagine, glucose, fructose and potassium, or muropeptides from growing neighbors), after which calcium dipicolinate is released, the cortex is hydrolyzed and the core rehydrates; and outgrowth, in which the cell resumes metabolism and emerges from the coat. Germination is not a regulated transcriptional program — it begins in a cell with no ATP and no transcription — but a cascade of pre-formed proteins, which is why it is so fast.

Individual spores in one preparation germinate over a wide range of times, from minutes to days, and the distribution is not explained by any measurable difference between them. This heterogeneity is the subject of the next section.

## 12.4. Bet Hedging in a Fluctuating Environment

Why should a clone produce different phenotypes rather than the single best one? Because in a varying environment the quantity that selection maximizes is not the mean growth rate but its long-run average per period, which is the mean of the logarithm: a strategy that is excellent in most periods but lethal in a rare one has a long-run rate of $-\infty$. This is **bet hedging** ([Definition 17.1.2](/7.9.17#def-17.1.2)).

The classical model is Cohen's (1966) analysis of germination in annual plants, which applies without change to bacterial spores. Let a fraction $G$ of the dormant propagules germinate each season. A germinated propagule yields $Y$ new ones in a good season (probability $p$) and none in a bad one; a propagule that stays dormant survives the season with probability $S$.

**Formula 12.4.1 (Cohen's Germination Model)** The population multiplies by $S(1 - G) + YG$ in a good season and by $S(1 - G)$ in a bad one, so the long-run growth rate per season is

$$
\Lambda(G) = p\ln\left[S(1 - G) + YG\right] + (1 - p)\ln\left[S(1 - G)\right], \tag{12.1}
$$

which is maximal at an interior $G^* < 1$ whenever $p < 1$, and tends to $G^* = p$ as $S \to 1$ and $Y \to \infty$.

**Proof** Differentiating, $\Lambda'(G) = p(Y - S)/[S + (Y - S)G] - (1 - p)/(1 - G)$. As $G \to 1^-$ the second term diverges, so $\Lambda' \to -\infty$ and $G = 1$ is never optimal for $p < 1$; $\Lambda$ is concave, so the root of $\Lambda' = 0$ is the maximum. With $S = 1$ and $Y \gg 1$ the condition becomes $p/G = (1 - p)/(1 - G)$, that is $G^* = p$. $\square$

![Cohen's model of germination in a randomly varying environment, applied to spores. A: the long-run growth rate $\Lambda(G)$ of Eq. (12.1) against the germinating fraction $G$ for three probabilities of a good year ($S = 0.9$, $Y = 10$); the dots mark the optima, and $G = 1$ is lethal whenever a bad year is possible. B: the optimal fraction $G^*$ against $p$ for three yields; the dotted line is the rule $G^* = p$. C: two hundred years of one simulated environment with $p = 0.6$: the optimal hedger grows steadily, a genotype that germinates everything dies in the first bad year, and one that germinates far too rarely grows slowly](./plots/bet-hedging.py)

The prediction — germinate a fraction of the spores, not all — is what is observed. Spores of *Bacillus cereus* and *B. subtilis* germinate heterogeneously even in rich medium, and the fraction depends on the history of the spore; the "superdormant" minority requires much stronger germinants. The same logic covers persister cells under antibiotics ([7.11.15](/7.11.15)), phase variation of surface structures ([7.11.34](/7.11.34)) and the stochastic competence of *B. subtilis*: when the environment cannot be predicted, the population buys insurance with a minority of cells in the wrong state.

## 12.5. The Asymmetric Cell Cycle of *Caulobacter crescentus*

*Caulobacter* lives in nutrient-poor fresh water and divides into two cells that differ in structure and in fate. The swarmer cell has a single polar flagellum and pili and cannot replicate its chromosome; it disperses, and then differentiates, shedding the flagellum and building at the same pole a stalk tipped with an adhesive holdfast. The stalked cell is sessile and reproductive: it replicates its chromosome, builds a new flagellum at the opposite pole and divides asymmetrically, producing a stalked cell that starts again at once and a swarmer that must differentiate first. Because the cycle has a phase in which no replication occurs, the eukaryotic names G1, S and G2 are used for it.

Three regulators whose levels oscillate in succession run the cycle. CtrA, a response regulator, is active (phosphorylated) in the swarmer: it binds the origin of replication and blocks initiation, and it transcribes the flagellar and pilus genes. At the G1-to-S transition CtrA is degraded by the ClpXP protease at the stalked pole, DnaA rises, binds the origin and fires replication. GcrA follows and drives replication elongation, division and stalk synthesis; CtrA reappears late and is confined to the swarmer compartment of the predivisional cell, where the kinase–phosphatase pair DivJ, PleC and the regulator DivK set its activity differently at the two poles. The whole program is spatially organized: the two poles carry different protein complexes, and the asymmetry of the predivisional cell is what makes the daughters different.

![The asymmetric cell cycle of *Caulobacter crescentus*. A: the life cycle. The flagellated swarmer cannot replicate; it sheds the flagellum, builds a stalk and holdfast at that pole, replicates and divides asymmetrically into a stalked cell, which divides again at once, and a new swarmer. B: the three master regulators over one cycle. CtrA-P in the swarmer blocks the origin and the stalked-cell program; its proteolysis lets DnaA rise and fire the origin; GcrA drives replication and division; CtrA returns late and is inherited by the swarmer](./plots/caulobacter.py)

*Caulobacter* also senses surfaces. Contact blocks the rotation of the flagellum, and the resulting signal triggers the immediate synthesis of holdfast — within seconds, far faster than the developmental program — so a swarmer that touches a good surface attaches at once. The second messenger that connects surface sensing to the switch from motility to attachment is cyclic di-GMP, which also governs biofilm formation (§12.9).

## 12.6. The Life Cycle of *Streptomyces*

The streptomycetes are Gram-positive soil bacteria that grow as filaments, not as single cells, and their life cycle resembles that of a mold. A spore germinates into a hypha that extends at its tip and branches, producing a *substrate mycelium* that penetrates the soil and secretes hydrolytic enzymes for cellulose, chitin, lignin fragments and proteins — the reason streptomycetes dominate the degradation of recalcitrant organic matter in soil, and the source of the earthy smell of damp ground, the terpene geosmin.

When nutrients run out, the colony raises *aerial hyphae*, covered by a hydrophobic sheath of chaplin and rodlin proteins that allows them to break the surface tension of the water film. They are nourished by the controlled lysis of the substrate mycelium — the colony cannibalizes its own older parts — and it is at this moment that the colony makes *secondary metabolites*, compounds not required for growth itself, among them most of the antibiotics in clinical use ([7.11.14](/7.11.14)). The aerial hyphae then septate at regular intervals into chains of uninucleoid spores, which disperse. Development is controlled by the *bld* genes (mutants are "bald": no aerial hyphae) and the *whi* genes (mutants make aerial hyphae but no spores, so the colony stays white); the extracellular signal γ-butyrolactone (A-factor in *Streptomyces griseus*) couples the timing of morphological differentiation to that of antibiotic production, which is why the two are so often regulated together.

![Two multicellular life cycles of soil bacteria. A: *Streptomyces*. A spore germinates into branching substrate hyphae; on starvation aerial hyphae rise, fed by lysis of the substrate mycelium — the stage at which antibiotics are made — and septate into chains of spores. B: *Myxococcus xanthus*. Cells glide in swarms and lyse their prey with secreted enzymes; on starvation about $10^5$ cells aggregate into a fruiting body in which a minority becomes myxospores, while most of the population lyses](./plots/lifecycles.py)

## 12.7. The Social Life of the Myxobacteria

*Myxococcus xanthus* is a predator. Its cells glide over surfaces in swarms, secreting hydrolytic enzymes and antibiotics that lyse other bacteria, and absorbing the products; a group can reach a far higher local concentration of enzyme than a single cell, so predation is a cooperative act. Two motility systems are used: *adventurous* (A) motility, by which single cells at the edge of the swarm move by a motor complex in the cell envelope that pushes against the substratum, and *social* (S) motility, which is twitching driven by retractile type IV pili and works only when cells are close enough to touch ([7.11.3](/7.11.3#sec-3.4.3)).

When the prey is exhausted, about $10^5$ cells aggregate — first into traveling waves (ripples), then into streams converging on an aggregation center — and build a **fruiting body**.

**Definition 12.7.1 (Fruiting Body)** A **fruiting body** is a macroscopic, often stalked or branched multicellular structure formed by the aggregation of starving cells, inside which a subpopulation differentiates into resistant dormant cells (myxospores in the myxobacteria); the remaining cells lyse or form the supporting structure.

In *M. xanthus* the fruiting body is a simple mound; in *Stigmatella* and *Chondromyces* it is a branched, pigmented tree up to half a millimeter high. Only about 10 % of the cells become myxospores — spherical, desiccation-resistant resting cells that survive for years, though not nearly as long as endospores; another fraction remains as peripheral rods, and the majority lyses, feeding the rest.

A population in which most cells die for the benefit of a few invites cheating, and cheaters are easy to find: developmental mutants that contribute few cells to the swarm but a disproportionate share of the spores in a mixed fruiting body. Several mechanisms limit them. Kin discrimination by polymorphic outer-membrane proteins (TraA/TraB) restricts the exchange of membrane material and the formation of chimeric groups to close relatives; some cheaters are obligate and collapse the population when alone; and in laboratory evolution, a cheater lineage has been observed to acquire a mutation that restored cooperation and dominated the ancestor in turn. The theory — relatedness, Hamilton's rule and the policing of public goods — belongs to [7.10.16](/7.10.16).

## 12.8. Heterocysts and Akinetes in Cyanobacteria

Filamentous cyanobacteria of the order Nostocales solve an incompatibility of metabolism by differentiating cells in space. Nitrogen fixation requires nitrogenase, which is destroyed by oxygen, while oxygenic photosynthesis produces oxygen; *Anabaena* and *Nostoc* therefore confine nitrogen fixation to **heterocysts** ([Definition 36.6.1](/7.6.36#def-36.6.1)), terminally differentiated cells that make up about one cell in ten along the filament. A heterocyst degrades photosystem II and the phycobilisomes, retains photosystem I for ATP, builds an extra envelope of glycolipid and polysaccharide that slows the entry of oxygen, raises respiration to consume what enters, and expresses the *nif* genes. The exchange with its neighbors runs through septal junctions: glutamine out, sucrose in.

The decision is made and spaced by two coupled feedbacks. Nitrogen starvation raises 2-oxoglutarate, which activates the global nitrogen regulator NtcA; NtcA and the transcription factor HetR activate each other, and HetR activates its own gene — local self-activation. HetR also induces the small peptides PatS and HetN, whose processed product, the pentapeptide RGSGR, moves through the septal junctions into the neighboring cells and promotes the degradation of HetR there — lateral inhibition with a diffusible inhibitor. Local activation with lateral inhibition is the recipe for a spaced pattern; since the filament grows, new heterocysts appear in the middle of intervals that have become too long, keeping the spacing nearly constant. The patterning is modeled in [7.6.36](/7.6.36#sec-36.6.1), and the general theory of such mechanisms in [7.5.12](/7.5.12).

Heterocysts are terminal: they neither divide nor revert. The same filaments can also form a second differentiated cell type under different stress.

**Definition 12.8.1 (Akinete)** An **akinete** is a thick-walled, nutrient-filled resting cell of a filamentous cyanobacterium that forms from a vegetative cell under nutrient limitation, cold or desiccation, resists drying and cold but not high temperature, and germinates into a new filament.

Akinetes often form next to heterocysts, and they are the stage in which populations of bloom-forming cyanobacteria overwinter in lake sediments ([7.11.30](/7.11.30)).

![Heterocyst differentiation in *Anabaena*. A: the filament. About one cell in ten becomes a heterocyst, which loses photosystem II, builds a thick envelope and fixes nitrogen; glutamine moves to the vegetative cells and sucrose the other way through the septal junctions. B: the circuit. Nitrogen starvation raises 2-oxoglutarate and activates NtcA, which with HetR forms a mutual activation loop; HetR also activates its own gene and induces PatS and HetN, whose pentapeptide product moves into the neighbors and promotes the degradation of HetR there. Local self-activation plus lateral inhibition gives the regular spacing](./plots/heterocyst.py)

## 12.9. Biofilms

### 12.9.1. What a Biofilm Is, and Why Cells Build One

Most microbial biomass on Earth is not planktonic.

**Definition 12.9.1 (Biofilm)** A **biofilm** is a community of microbial cells attached to a surface or to each other and embedded in a self-produced matrix of extracellular polymeric substances (polysaccharides, proteins and extracellular DNA), within which the cells are physiologically differentiated from planktonic cells and from one another.

Surfaces are where nutrients accumulate: organic molecules adsorb to a solid, so the layer next to it is richer than the bulk. A matrix retains extracellular enzymes and their products near the cells that made them, protects against desiccation, phagocytosis, protists and antimicrobials, and keeps a cell among its relatives, which makes cooperation pay. The cost is diffusion: the cells inside a biofilm compete for substrate and oxygen with those above them (§12.9.3).

### 12.9.2. Formation, Matrix and the c-di-GMP Switch

Biofilm development is conventionally divided into reversible attachment, irreversible attachment, microcolony formation, maturation into a structured film with water channels, and dispersal. The cell changes as it goes: flagellar motility is switched off, adhesins and pili are made, and the matrix genes are turned on.

The matrix is typically 90 % of the dry mass of a biofilm. It contains exopolysaccharides (alginate, Pel and Psl in *Pseudomonas aeruginosa*; VPS in *Vibrio cholerae*; cellulose and PNAG in enterobacteria), structural proteins (the amyloid curli of *E. coli*, TasA of *B. subtilis*, the lectins that cross-link the polysaccharides) and extracellular DNA, which binds cations and cross-links the matrix. The eDNA comes in part from a programmed event: in *P. aeruginosa*, a subpopulation of cells is lysed by the endolysin of a prophage whose lytic gene fires at random in a few cells, and the DNA and membrane vesicles they release nucleate the matrix. Antibiotic treatment, by inducing prophages, can therefore *promote* biofilm formation.

The switch between the motile and the attached lifestyle is governed by the second messenger cyclic di-GMP.

**Definition 12.9.2 (Cyclic di-GMP)** **Cyclic di-GMP** (c-di-GMP) is a bacterial second messenger made from two GTP by diguanylate cyclases (GGDEF domains) and degraded by phosphodiesterases (EAL and HD-GYP domains). A high concentration promotes attachment, matrix synthesis and the sessile lifestyle; a low concentration promotes flagellar motility, dispersal and, in several pathogens, acute virulence.

c-di-GMP binds protein effectors (motor-brake proteins that slow the flagellum, glycosyltransferases of matrix synthesis, transcription factors) and riboswitches. A single genome may encode dozens of cyclases and phosphodiesterases, each with its own input domain, and many act locally rather than on the whole cytoplasmic pool, so the one messenger can serve many decisions. Quorum sensing ([7.11.11](/7.11.11#sec-11.7)) acts on the same programs: in *P. aeruginosa*, AHL signaling is required for a normally structured biofilm, while in *V. cholerae* high cell density represses the matrix and promotes dispersal.

### 12.9.3. Gradients, Division of Labor and Tolerance

A biofilm a few hundred micrometers thick is chemically stratified, because consumption at the top prevents substrate and oxygen from reaching the bottom. A simple reaction–diffusion model gives the scale.

**Formula 12.9.1 (Penetration and the Thiele Modulus)** In a flat biofilm of thickness $L$ with diffusion coefficient $D$ and zero-order consumption at rate $q$ per unit volume, the steady state of $D\,\mathrm{d}^2c/\mathrm{d}x^2 = q$ with $c(L) = c_0$ at the surface and no flux at the base ($x = 0$) is

$$
c(x) = c_0\left[1 - \varphi^2\left(1 - \frac{x^2}{L^2}\right)\right], \qquad \varphi = L\sqrt{\frac{q}{2Dc_0}}. \tag{12.2}
$$

The substrate reaches the base only if the Thiele modulus $\varphi \le 1$; for $\varphi > 1$ it runs out at the depth $x_{\mathrm{c}} = L(1 - 1/\varphi)$, and the cells below are starved.

**Proof** Integrating twice gives $c(x) = qx^2/(2D) + Ax + B$; no flux at $x = 0$ gives $A = 0$, and $c(L) = c_0$ gives $B = c_0 - qL^2/(2D)$, which is Eq. (12.2). The minimum is at $x = 0$, where $c = c_0(1 - \varphi^2)$, so penetration requires $\varphi \le 1$. When $\varphi > 1$, consumption stops where the substrate does, and the solution of the same equation on $[x_{\mathrm{c}}, L]$ with $c(x_{\mathrm{c}}) = c'(x_{\mathrm{c}}) = 0$ fixes $x_{\mathrm{c}} = L(1 - 1/\varphi)$. $\square$

Put in numbers for oxygen: $D \approx 2 \times 10^{-9}\,\mathrm{m^2\,s^{-1}}$, $c_0 \approx 0.25\,\mathrm{mol\,m^{-3}}$ in air-saturated water, and a respiration rate of order $q \approx 10^{-1}\,\mathrm{mol\,m^{-3}\,s^{-1}}$ for a dense film give $\varphi = 1$ at $L \approx 100\,\mu\mathrm{m}$. Oxygen microelectrodes find exactly this: anoxic zones a few tens to a few hundreds of micrometers below the surface of active biofilms and microbial mats ([7.11.29](/7.11.29)).

Two consequences follow. The first is a division of labor that need not be genetic: cells at the top grow fast and aerobically, cells in the middle ferment or respire anaerobically, cells at the base are dormant, and in *B. subtilis* biofilms the matrix producers, the sporulating cells and the motile cells occupy different positions. The second is tolerance. A biofilm survives antimicrobial concentrations that kill the same strain in suspension, for several reasons that act together: slow penetration of the agent (charged antibiotics bind the matrix; reactive species such as hypochlorite are consumed by it), slow growth or dormancy of the cells inside, since most antibiotics need an active target ([7.11.14](/7.11.14)), a high local density that favors **persister** formation and horizontal transfer of resistance genes, and protection from phagocytes and antibodies. This is tolerance rather than resistance: cells dispersed from a biofilm are as susceptible as any others, which is why the killing curve of a biofilm has a resistant tail rather than a shifted MIC ([7.11.15](/7.11.15)).

![Biofilms. A: the stages, from reversible attachment through irreversible attachment and matrix synthesis, microcolonies and a mature film with water channels, to dispersal by matrix-degrading enzymes when c-di-GMP falls. B: substrate penetration from Eq. (12.2) for several values of the Thiele modulus $\varphi$; for $\varphi > 1$ the substrate is exhausted before the base and the cells there are starved. C: the consequence for treatment — exponential killing of a planktonic culture, against the resistant tail produced by a dormant subpopulation in a biofilm](./plots/biofilm.py)

### 12.9.4. Biofilms in Nature and Medicine

Dental plaque is the best-studied natural biofilm: an ordered succession in which *Streptococcus* species attach to the salivary pellicle, *Fusobacterium nucleatum* coaggregates with almost everything and bridges early and late colonizers, and anaerobes establish themselves in the resulting micro-anoxic environment; acid produced at the enamel surface demineralizes it. In fresh water and in the sea, biofilms coat every stone and every particle, and microbial mats are biofilms thick enough to be laminated by their own gradients ([7.11.29](/7.11.29)). In industry they foul heat exchangers, membranes and pipelines and cause microbially influenced corrosion, and in wastewater treatment they are deliberately cultivated on supports.

In medicine, biofilms account for a large share of chronic and device-related infection: *P. aeruginosa* in the airways in cystic fibrosis, *Staphylococcus epidermidis* and *S. aureus* on catheters, prosthetic joints and heart valves, *E. coli* in recurrent urinary tract infection, *Streptococcus mutans* in caries. The clinical signature is a persistent infection that responds to antibiotics while they are given and relapses when they stop. Control therefore attacks the biofilm rather than the cell: physical removal (brushing, débridement, replacing the device), surfaces and coatings that resist attachment or release antimicrobials, matrix-degrading enzymes (DNase I, dispersin B, alginate lyase), agents that lower c-di-GMP and so trigger dispersal — with the caveat that dispersal releases virulent planktonic cells and must be combined with an antibiotic — quorum-sensing inhibitors ([7.11.11](/7.11.11#sec-11.7.4)), and bacteriophages, whose depolymerases digest the matrix ([7.11.23](/7.11.23)).

## Summary

- Prokaryotic development is built from ordinary regulators, but it has the features of development: coexisting fates in one genotype, asymmetric division, commitment and intercellular signaling.
- In *B. subtilis* the phosphorelay to Spo0A integrates many signals into a graded output: low Spo0A-P gives matrix production (through SinI against SinR), intermediate gives cannibalism, high gives **sporulation** (Definition 12.3.1), while an excitable ComK loop makes a minority of cells competent.
- Sporulation runs through asymmetric division, engulfment, cortex and coat synthesis, maturation and mother-cell lysis, driven by four compartment-specific σ factors (σᶠ, σᴱ, σᴳ, σᴷ) activated in turn by signals crossing between the two compartments. Germination is a fast, pre-formed cascade, not a transcriptional program.
- Heterogeneity is adaptive when the environment fluctuates: the long-run growth rate is the mean of the logarithm, so the optimum is to germinate (or to grow) with a fraction less than one — Cohen's model, Formula 12.4.1, the microbial form of **bet hedging**.
- *Caulobacter* divides asymmetrically into a dispersing swarmer and a reproducing stalked cell; CtrA, DnaA and GcrA oscillate in succession, and polar complexes make the two daughters different. Surface contact, sensed through the flagellum, triggers holdfast synthesis.
- *Streptomyces* grows as a substrate mycelium, raises aerial hyphae at the expense of its own older parts, makes antibiotics at that moment, and septates the aerial hyphae into spore chains. The myxobacteria glide in predatory swarms and, when starved, build **fruiting bodies** (Definition 12.7.1) in which about a tenth of the cells become myxospores while most lyse — a public good open to cheating and policed by kin discrimination.
- Filamentous cyanobacteria separate nitrogen fixation from photosynthesis in **heterocysts**, spaced by HetR self-activation and the diffusible inhibitor PatS; **akinetes** (Definition 12.8.1) are their resting cells.
- A **biofilm** (Definition 12.9.1) is cells in a self-made matrix of polysaccharide, protein and eDNA on a surface. The switch to it is governed by **cyclic di-GMP** (Definition 12.9.2) and by quorum sensing. Consumption against diffusion stratifies the film: full penetration requires a Thiele modulus $\varphi \le 1$ (Formula 12.9.1), and the starved, dormant cells below give biofilms their tolerance to antimicrobials. Biofilms dominate natural habitats, foul industrial systems and cause chronic and device-related infections; control aims at the matrix, at attachment and at dispersal rather than at the single cell.

## Questions

1. A mutant of *B. subtilis* lacking the phosphatase RapA sporulates earlier and at a lower cell density than the wild type, while a mutant lacking the peptide signal PhrA, which inhibits RapA, sporulates later. Explain both, and say what this pair of genes contributes to the decision.

   **Answer** RapA drains phosphate from Spo0F in the relay, so it lowers Spo0A-P and delays sporulation; without it, the relay runs unchecked and the threshold for sporulation is reached sooner. PhrA is an exported, re-imported peptide that inhibits RapA, so it reports cell density; without PhrA, RapA stays active and sporulation is delayed. The pair therefore makes the commitment conditional on the population being dense — a quorum requirement on an expensive and irreversible decision — and provides a point at which other signals can veto the relay.

2. σᶠ protein is present in the cell before the asymmetric septum forms, yet it becomes active only in the forespore. How is this achieved, and why must the mechanism be insensitive to the amounts of the proteins involved?

   **Answer** σᶠ is held by the anti-σ factor SpoIIAB. The anti-anti-σ factor SpoIIAA can take SpoIIAB away, but only when dephosphorylated, and the phosphatase SpoIIE is localized at the septum. The forespore is a far smaller compartment than the mother cell, so the same number of SpoIIE molecules at the septum produces a much higher concentration in it, and SpoIIAA is dephosphorylated there alone. The mechanism must work on a ratio rather than on absolute numbers because the two compartments differ several-fold in volume and in protein content; a scheme depending on absolute amounts would release σᶠ in both.

3. Using Eq. (12.1), explain why a strategy that germinates every spore can never be optimal if a bad year is possible, however rare. Would the conclusion change if a bad year merely reduced the yield to a small positive value instead of zero?

   **Answer** With $G = 1$ the growth factor in a bad year is $S(1 - G) = 0$, so $\ln$ of it is $-\infty$ and $\Lambda = -\infty$: a single bad year eliminates the lineage. Mathematically, $\Lambda'(G) \to -\infty$ as $G \to 1$, so the optimum is interior. If a bad year gave yield $\varepsilon > 0$, the logarithm would remain finite and $G = 1$ could be optimal when $\varepsilon$ is not too small or bad years are rare; hedging is then a quantitative trade-off rather than an absolute requirement. The sharp result depends on the possibility of total failure.

4. A dense biofilm consumes oxygen at $q = 0.05\,\mathrm{mol\,m^{-3}\,s^{-1}}$, with $D = 2 \times 10^{-9}\,\mathrm{m^2\,s^{-1}}$ and $c_0 = 0.25\,\mathrm{mol\,m^{-3}}$ at the surface. How thick can the film be and remain fully oxic? If it is $400\,\mu\mathrm{m}$ thick, how deep is the oxic layer, and what metabolism would you expect below it?

   **Answer** Full penetration needs $\varphi = L\sqrt{q/(2Dc_0)} \le 1$, that is $L \le \sqrt{2Dc_0/q} = \sqrt{2 \times 2\times10^{-9} \times 0.25/0.05} = \sqrt{2\times10^{-8}} = 1.4\times10^{-4}\,\mathrm{m}$, about $140\,\mu\mathrm{m}$. At $L = 400\,\mu\mathrm{m}$, $\varphi = 400/141 = 2.8$, so oxygen is exhausted at $x_{\mathrm{c}} = L(1 - 1/\varphi) = 400 \times 0.65 = 259\,\mu\mathrm{m}$ from the base: the oxic layer is the top $\approx 141\,\mu\mathrm{m}$. Below it one expects, in order of decreasing yield, denitrification, then fermentation, sulfate reduction and methanogenesis where those substrates are available — the stratification of a microbial mat in miniature.

5. A catheter infection by *S. aureus* is treated with an antibiotic at ten times the MIC measured on a planktonic culture. The infection improves and then relapses after treatment ends, and the organism recovered from the catheter has the same MIC as the original isolate. Interpret the result, and say what it implies for treatment.

   **Answer** The unchanged MIC rules out genetic resistance: what the biofilm provides is tolerance. The agent penetrates the matrix slowly and is partly bound or consumed by it, and the cells deep in the film are starved and dormant, so the targets of most antibiotics (wall synthesis, translation at a high rate) are not active. The killing curve therefore has a surviving tail that regrows once the drug is withdrawn (panel C of the figure). Treatment must remove or replace the device where possible, use agents active against non-growing cells, combine them with measures aimed at the matrix or at dispersal, and continue long enough to catch cells that resume growth — and dispersal agents should not be used alone, since they release virulent planktonic cells.
