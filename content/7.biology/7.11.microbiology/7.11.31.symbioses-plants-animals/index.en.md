---
title: Microbial Symbioses with Plants and Animals
description: "Kinds of symbiosis and how symbionts are transmitted; the legume–rhizobium symbiosis (flavonoids and Nod factors, the infection thread, bacteroids, leghemoglobin and the cost of nitrogen fixation), actinorhizal and cyanobacterial nitrogen-fixing symbioses, mycorrhizae, lichens, endophytes and the root microbiome; Agrobacterium, the Ti plasmid and crown gall; insect endosymbionts (Buchnera, termites, Wolbachia), the squid–Aliivibrio light organ, entomopathogenic nematodes, chemosynthetic symbioses of vent animals, corals and coral bleaching; the rumen and hindgut fermentation; and the evolution of symbiont genomes."
---

Most plants and animals do not live alone. Their roots, leaves, guts and even their cells are inhabited by microorganisms, and many of their characteristic abilities are really abilities of those partners: legumes fix nitrogen through bacteria in their root nodules, cattle live on grass because their rumen is a fermenter full of anaerobes, aphids survive on phloem sap because bacteria inside their cells make the amino acids the sap lacks, and coral reefs exist because dinoflagellates photosynthesize inside the coral's cells. This chapter describes these associations from the microbial side: how partners recognize each other, what they exchange, how the association is passed on, and what living inside a host does to a microbial genome. It builds on the metabolism of nitrogen fixation, chemolithotrophy and fermentation ([7.11.6](/7.11.6#sec-6.6), [7.11.7](/7.11.7), [7.11.5](/7.11.5)), on the bacteria and fungi described in [7.11.17](/7.11.17), [7.11.18](/7.11.18) and [7.11.21](/7.11.21), and on the soil and marine habitats of [7.11.29](/7.11.29). The evolutionary theory of mutualism and coevolution is in [7.10.17](/7.10.17), the role of symbionts in animal development in [7.5.38](/7.5.38#sec-38.9), and the human microbiota, the most studied symbiosis of all, is the subject of [7.11.32](/7.11.32).

## 31.1. Kinds of Symbiosis

### 31.1.1. A Continuum of Outcomes

**Definition 31.1.1 (Symbiosis)** A **symbiosis** is a close and persistent association between organisms of different species. By its effect on the host, the microbial partner (the symbiont) is a **mutualist** when both partners gain in fitness, a *commensal* when it benefits without measurably affecting the host, and a *parasite* when it benefits at the host's expense; a parasite that causes disease is a pathogen.

The word was introduced by de Bary (1879) for "the living together of unlike organisms", without any judgment of benefit, and that broad sense is used here; in some textbooks "symbiosis" means mutualism only. The three outcomes are a continuum rather than fixed categories. The same microbe can be a mutualist in one host and a parasite in another, or change with conditions: rhizobia that stop fixing nitrogen become a cost to the plant (the sanctions of **mutualism**, [7.10.17](/7.10.17#sec-17.3)), mycorrhizal fungi are beneficial in poor soils but can depress growth in fertilized ones, and members of the normal human microbiota cause disease when they reach the wrong site ([7.11.32](/7.11.32)). Two further outcomes complete the classification of pairwise interactions used in older microbiology texts: *amensalism*, in which one partner is harmed and the other unaffected (as when an antibiotic producer inhibits its neighbors), and competition, in which both lose. Interactions between free-living microbes that cooperate through metabolism, such as syntrophic partners exchanging $\ce{H2}$ (**syntrophy**, [7.11.7](/7.11.7)), are treated with microbial ecology ([7.11.29](/7.11.29)).

| Effect on microbe / host | Name | Examples in this chapter |
|---|---|---|
| + / + | mutualism | rhizobia in legume nodules; *Buchnera* in aphids; rumen microbiota; *Symbiodinium* in corals |
| + / 0 | commensalism | many skin and gut bacteria; rhizosphere saprotrophs |
| + / − | parasitism, pathogenesis | *Agrobacterium* (crown gall); *Wolbachia* in many insects |
| − / 0 or 0 / − | amensalism | antibiotic production, acidification by lactic acid bacteria |

Symbioses also differ in intimacy and dependence. *Ectosymbionts* live on the surface of the host or in its gut lumen; endosymbionts live inside its tissues or cells. An *obligate* symbiont cannot live without its host; a *facultative* one can. A host can be obligately dependent on its symbiont too: aphids freed of *Buchnera* by antibiotics grow poorly and do not reproduce. The host together with its persistent symbionts forms a **holobiont** ([Definition 38.9.1](/7.5.38#def-38.9.1)).

### 31.1.2. How Symbionts Are Passed On

**Definition 31.1.2 (Vertical and Horizontal Transmission)** A symbiont is transmitted *vertically* when it passes from parent to offspring, usually through the egg, and *horizontally* when each new host acquires it from the environment or from unrelated hosts.

The mode of transmission shapes the whole relationship.

- Vertical transmission ties the symbiont's reproduction to the host's: a symbiont that harms its host reduces its own transmission, so selection favors benefit to the host, or, in maternally transmitted symbionts, manipulation of host reproduction towards infected daughters (Section 31.4.3). Vertically transmitted symbionts live in small, bottlenecked populations, lose their free-living stage and their genomes shrink (Section 31.7).
- Horizontal transmission requires that the host select the right partner out of a diverse environment in every generation, and that the symbiont survive outside the host. Legumes, the bobtail squid and most corals acquire their symbionts in this way, and each has evolved a sequence of molecular checkpoints that excludes the wrong partners (Sections 31.2.2 and 31.5.1). Horizontally acquired symbionts keep larger genomes.

## 31.2. The Legume–Rhizobium Symbiosis

### 31.2.1. Root Nodules

The **rhizobia** ([7.11.17](/7.11.17#sec-17.3.2)) are soil bacteria that can live freely in the soil and the **rhizosphere** ([7.11.29](/7.11.29#sec-29.7.2)) or, in the roots of legumes, induce and inhabit a new organ.

**Definition 31.2.1 (Root Nodule)** A **root nodule** is an organ formed on the root of a legume (or of an actinorhizal plant, Section 31.2.5) in response to a nitrogen-fixing bacterium, whose central tissue consists of plant cells filled with the differentiated bacteria, which fix $\ce{N2}$ and supply the plant with ammonium in exchange for organic carbon.

The legumes (Fabaceae), with about 20 000 species, include soybean, pea, bean, clover, alfalfa and many tropical trees. Nodulated legumes grow on nitrogen-poor soils without fertilizer, and legume–rhizobium symbioses fix an estimated several tens of millions of tonnes of nitrogen per year in agriculture, a large part of biological nitrogen fixation on land (the nitrogen cycle: [7.11.30](/7.11.30)). Associations are specific: each rhizobial species or biovar nodulates a particular group of legumes, its *cross-inoculation group* (pea and vetch with *Rhizobium leguminosarum* bv. *viciae*, clover with bv. *trifolii*, alfalfa with *Sinorhizobium meliloti*, soybean with *Bradyrhizobium japonicum*), although some strains, such as *Sinorhizobium fredii* NGR234, have a host range of more than a hundred legume genera. Nodules are either *indeterminate*, with a persistent meristem at the tip that keeps adding cells (pea, alfalfa, clover; cylindrical nodules with zones of infection, fixation and senescence), or *determinate*, spherical and without a persistent meristem (soybean, bean, *Lotus*).

### 31.2.2. Signal Exchange and Infection

Nodulation is a dialogue of signals in both directions (Figure 1).

1. Root exudates contain flavonoids (luteolin from alfalfa, genistein and daidzein from soybean), which diffuse to rhizobia in the rhizosphere. They bind NodD, a LysR-type transcriptional activator, which then activates the *nod* genes. Different legumes release different flavonoids, and NodD proteins of different rhizobia respond to different ones: the first step of host specificity.
2. The *nod* genes direct the synthesis of the bacterial signal.

**Definition 31.2.2 (Nod Factor)** A **Nod factor** is a lipochitooligosaccharide secreted by rhizobia that induces nodule development in a compatible legume: a backbone of three to five β-1,4-linked *N*-acetylglucosamine residues, synthesized by the products of the common genes *nodABC*, whose terminal residue carries a fatty acyl chain, with species-specific substitutions (acetyl, sulfate, fucose, methyl groups, and the length and unsaturation of the acyl chain) added by host-specific *nod* genes.

3. Nod factors are recognized at nanomolar concentrations by LysM-domain receptor kinases of the root hair (NFR1 and NFR5 in *Lotus japonicus*, a model legume); the substitutions decide which legumes respond, the second step of specificity (*S. meliloti* Nod factor without its sulfate no longer nodulates alfalfa). Receptor signalling, through a further receptor kinase (SYMRK), leads to oscillations of calcium in and around the nucleus (calcium spiking), decoded by a calcium- and calmodulin-dependent kinase that activates transcription factors for nodulation.
4. The root hair curls around attached bacteria and traps them in a pocket. The plant cell wall there is remodeled and the plasma membrane invaginates to form the *infection thread*, a tube of plant wall material, filled with dividing bacteria embedded in a matrix, that grows down through the root hair and into the cortex. Bacterial exopolysaccharides are needed for normal progression; mutants without them are blocked or trigger defense responses.
5. Meanwhile, Nod factor signalling has reactivated cell division in the inner (indeterminate) or outer (determinate) cortex, producing a nodule primordium, and plant cytokinin signalling is needed for this.
6. Where the infection thread reaches the primordium, bacteria are released into the cytoplasm of plant cells by a form of endocytosis, each enclosed in a plant-derived membrane.

Some tropical legumes use other routes. In "crack entry", rhizobia enter at the gaps where lateral roots emerge, and *Azorhizobium caulinodans* forms nodules on the stems of the aquatic legume *Sesbania rostrata*. Certain photosynthetic *Bradyrhizobium* strains nodulate *Aeschynomene* species without any Nod factor, by a mechanism that is still being worked out.

The receptors, the calcium spiking and the decoding kinase belong to a *common symbiosis signalling pathway* that legumes share with the much older **arbuscular mycorrhiza** (Section 31.3.1): arbuscular mycorrhizal fungi secrete chemically related lipochitooligosaccharides and short chitin oligomers (Myc factors), and mutants of the common pathway lose both symbioses. The rhizobial symbiosis, which arose roughly 100 million years ago in one clade of flowering plants (the nitrogen-fixing clade, which also includes the actinorhizal plants), evidently recruited a signalling system that had served arbuscular mycorrhizae for more than 400 million years.

![A: the signal exchange that initiates a legume root nodule. Flavonoids released by the root activate the rhizobial regulator NodD, which switches on the *nod* genes; their products synthesize the Nod factor, which is perceived by LysM receptor kinases (NFR1 and NFR5 in *Lotus*) and triggers nuclear calcium spiking, root-hair curling, the infection thread and cortical cell division. Specificity is checked twice, at the flavonoid–NodD and at the Nod factor–receptor step. B: exchange in an infected nodule cell (schematic). The plant supplies C4-dicarboxylates (malate, succinate) through the symbiosome membrane and the bacteroid transporter DctA; their oxidation provides electrons and ATP for nitrogenase, and the ammonium formed is assimilated by the plant and exported as amides or ureides. Leghemoglobin keeps free O2 at nanomolar levels while delivering bound O2 to the bacteroids' respiration.](./plots/nodule-exchange.py)

### 31.2.3. Bacteroids and the Nitrogen-Fixing Nodule

**Definition 31.2.3 (Bacteroid)** A **bacteroid** is the differentiated, nitrogen-fixing form of a rhizobium inside a nodule cell. One or a few bacteroids, enclosed in a membrane of plant origin (the *peribacteroid* or *symbiosome membrane*), form a *symbiosome*, a compartment that functions as a nitrogen-fixing organelle of the plant cell.

In the infected cells of a mature nodule, thousands of symbiosomes fill the cytoplasm. Bacteroid differentiation is controlled by the plant. In legumes of the clade that includes pea and alfalfa (the inverted-repeat-lacking clade), the plant produces hundreds of nodule-specific cysteine-rich (NCR) peptides, related to antimicrobial defensins, that are delivered to the bacteroids, increase membrane permeability and block cell division: the bacteroids become elongated or branched, endoreduplicate their genome to 8–24 copies and can no longer divide, a terminal differentiation. Soybean bacteroids, by contrast, keep a normal size and ploidy and can regrow when released. In both, a few undifferentiated bacteria in the infection threads survive the senescence of the nodule and return to the soil.

The exchange across the symbiosome membrane is the core of the mutualism (Figure 1):

- The plant supplies C4-dicarboxylic acids, mainly malate and succinate, which bacteroids take up through the dicarboxylate transporter DctA. Bacteroid mutants without DctA form nodules but cannot fix nitrogen: sugars are not the carbon source. Malate is oxidized in the TCA cycle to supply electrons, through ferredoxin or flavodoxin, to nitrogenase, and NADH for respiration and ATP synthesis.
- Nitrogenase reduces $\ce{N2}$ to ammonia ([7.11.6](/7.11.6#sec-6.6.2); the enzyme: **nitrogenase**, [7.1.27](/7.1.27)), which diffuses or is transported as $\ce{NH4+}$ into the plant cytoplasm. Bacteroids repress their own ammonium assimilation (glutamine synthetase), so that the fixed nitrogen goes to the plant, where glutamine synthetase and glutamate synthase assimilate it. Temperate legumes export the nitrogen from the nodule as amides (asparagine, glutamine), tropical legumes such as soybean as ureides (allantoin, allantoic acid). In pea, amino acids are also cycled between plant and bacteroid: bacteroids depend on the plant for branched-chain amino acids, which ties them metabolically to their host.

Nitrogenase is irreversibly destroyed by $\ce{O2}$, but bacteroids need $\ce{O2}$ for the respiration that powers it. The nodule solves this in two ways ([7.11.6](/7.11.6#sec-6.6.3)): a diffusion barrier of tightly packed cells in the nodule cortex limits the entry of $\ce{O2}$, and the infected cells are filled with an oxygen-binding protein.

**Definition 31.2.4 (Leghemoglobin)** **Leghemoglobin** is a monomeric plant hemoglobin, present at millimolar concentration in the cytoplasm of infected nodule cells, whose very high affinity for $\ce{O2}$ keeps the concentration of free $\ce{O2}$ in the nanomolar range while its large pool of bound $\ce{O2}$ diffuses rapidly to the symbiosomes and supplies the bacteroids' respiration.

The globin is encoded by the plant and the heme is made largely by the plant too; leghemoglobin gives active nodules their pink-red color, and nodules of plants in which leghemoglobin synthesis is silenced turn white, contain more free $\ce{O2}$ and do not fix nitrogen. The bacteroids, for their part, use a terminal oxidase of very high affinity (the *cbb*$_3$ oxidase, encoded by *fixNOQP*), and the expression of the *nif* and *fix* genes is switched on by low $\ce{O2}$ through the two-component system FixL–FixJ, whose sensor kinase FixL is a heme protein.

### 31.2.4. The Cost of Nitrogen Fixation and Its Control

Nitrogen fixation is expensive. By [Eq. (27.1)](/7.1.27#eq-27.1), nitrogenase consumes at least 16 ATP and 8 electrons per $\ce{N2}$, and the respiration that supplies them, together with the growth and maintenance of the nodule, costs the plant several grams of carbon for every gram of nitrogen fixed (estimates range from about 4 to over 10 g C per g N, depending on species and conditions; a comparison of costs is in Question 2). The plant therefore regulates the symbiosis tightly:

- Nitrate in the soil inhibits nodulation and nitrogen fixation: when combined nitrogen is available, assimilating it is cheaper.
- Autoregulation of nodulation limits nodule number: signal peptides (CLE peptides) made in newly infected roots travel in the xylem to the shoot, where a receptor kinase (HAR1 in *Lotus*, NARK in soybean) triggers a signal that returns to the root and suppresses further nodulation. Mutants without the receptor form hundreds of nodules (supernodulation) and grow poorly.
- Sanctions: nodules that fix little nitrogen receive less $\ce{O2}$ and carbon and their bacteria multiply less (Kiers et al. 2003, [7.10.17](/7.10.17#sec-17.3)), which limits the spread of ineffective "cheater" strains.

Because nodules release nitrogen into the soil when they decay, and because the plant residues are rich in nitrogen, legumes enrich soils for the following crops; this is the basis of rotations with clover or beans and of green manures. Seeds of legumes are routinely coated with inocula of effective rhizobial strains (inoculants) where the right rhizobia are absent from the soil, for example when soybean was introduced to Brazil.

### 31.2.5. Other Nitrogen-Fixing Plant Symbioses

- Actinorhizal symbioses: the filamentous actinomycete *Frankia* ([7.11.18](/7.11.18#sec-18.4)) forms root nodules on about 200 species of woody plants in eight families, among them alder (*Alnus*), *Casuarina*, bayberry (*Myrica*) and sea buckthorn (*Hippophae*). *Frankia* protects its nitrogenase in vesicles at the tips of its hyphae, whose multilayered envelope of hopanoid lipids slows the entry of $\ce{O2}$, so that it fixes nitrogen even in air. Alders and *Casuarina* are pioneers of nitrogen-poor soils, river gravels and dunes.
- *Parasponia*, an elm relative, is the only nonlegume nodulated by rhizobia.
- Cyanobacterial symbioses: heterocystous cyanobacteria ([7.11.18](/7.11.18#sec-18.5)) live in the leaf cavities of the water fern *Azolla* (*Nostoc azollae*, traditionally *Anabaena azollae*), in the coralloid roots of cycads, in the stem glands of *Gunnera* and in liverworts and hornworts; within the plant the frequency of **heterocysts** rises to 20–30 % of the cells, compared with 5–10 % in free-living filaments. The *Azolla* symbiont is transmitted vertically with the fern's spores and has a partly degenerated genome. *Azolla* has long been grown in Asian rice paddies as a green manure, and cyanobacteria are also the nitrogen-fixing partners of many lichens (Section 31.3.2).
- Associative nitrogen fixation: bacteria such as *Azospirillum* and endophytic *Gluconacetobacter diazotrophicus* in sugarcane fix nitrogen on or in roots and stems without forming a specialized organ; their contribution to the plant is much smaller and variable.

## 31.3. Fungal Symbioses: Mycorrhizae and Lichens

### 31.3.1. Mycorrhizae

The fungi that form a **mycorrhiza** with plant roots, and the structures they form, are described in [7.11.21](/7.11.21#sec-21.6.2). The main types differ in the fungi, the hosts and the structures of exchange:

| Type | Fungi | Hosts | Structure | Main exchange |
|---|---|---|---|---|
| arbuscular | Glomeromycotina (about 300 described species) | about 70–80 % of land plant species, most crops and grasses | intracellular arbuscules in cortical cells, surrounded by the periarbuscular membrane of the plant; vesicles; extraradical hyphae | phosphate (and some N, water) to plant; sugars and fatty acids to fungus |
| ectomycorrhizal | basidiomycetes and ascomycetes (thousands of species: boletes, amanitas, truffles) | about 2 % of species but dominant trees of temperate and boreal forests (pines, oaks, beeches, dipterocarps) | mantle around short roots, intercellular Hartig net, rhizomorphs into soil | N and P from organic matter to plant; sugars to fungus |
| ericoid | ascomycetes | heaths (Ericaceae) on acid, organic soils | hyphal coils in epidermal cells | N from organic matter |
| orchid | basidiomycetes | orchids | coils (pelotons) in cortical cells | carbon from fungus to seedling (orchid seeds have almost no reserves) |

The arbuscular symbiosis begins with an exchange of signals. Under phosphate limitation, roots release strigolactones, carotenoid-derived hormones, which stimulate the germination and branching of fungal hyphae; the fungi answer with lipochitooligosaccharides and chitin oligomers that activate the common symbiosis pathway (Section 31.2.2). A hyphopodium on the root surface gives rise to hyphae that cross the epidermis through a prepenetration apparatus assembled by the plant cell, spread in the cortex and form arbuscules in inner cortical cells. Exchange takes place across the periarbuscular membrane: plant phosphate transporters located only there (PT4 in *Medicago truncatula*) take up phosphate released by the fungus, which had absorbed it in the soil and moved it along the hyphae as polyphosphate; in return the plant supplies sugars and, remarkably, fatty acids (as monoacylglycerols), because arbuscular mycorrhizal fungi lack the genes for cytosolic fatty acid synthase (Jiang et al. 2017; Luginbuehl et al. 2017). They cannot complete their life cycle without a host and are obligate symbionts, which is why they cannot be grown in pure culture. Each arbuscule lives only a few days before it collapses and is replaced.

The benefit to the plant comes from the hyphae, which are much thinner than roots and extend centimeters beyond the zone depleted of phosphate around them (phosphate, which binds to soil particles, diffuses very slowly). Mycorrhizal plants can also be better protected against drought and root pathogens. Hyphae of one fungus can connect the roots of several plants into common mycorrhizal networks; that carbon and signals pass between trees through them is shown by isotope labeling in some experiments, but how much carbon is transferred in natural forests, and whether this benefits seedlings, is contested (Karst et al. 2023).

### 31.3.2. Lichens

A **lichen** ([Definition 21.6.2](/7.11.21#def-21.6.2)) is a mycobiont, usually an ascomycete, with a photobiont, a green alga (often *Trebouxia*) or a cyanobacterium (often *Nostoc*); about 20 000 species are known, named after their fungus. The fungus builds the thallus: a dense cortex, a layer of photobiont cells held among hyphae, and a loose medulla. The photobiont supplies the fungus with carbohydrates, green algae as sugar alcohols (ribitol, sorbitol, erythritol), cyanobacteria as glucose, and cyanobacterial photobionts fix nitrogen as well. The fungus provides a protected, light-exposed habitat, water uptake and storage, and lichen acids that dissolve and chelate minerals from rock and that deter herbivores and absorb ultraviolet light.

Lichens tolerate complete desiccation: they lose water within hours, become metabolically inactive, and resume photosynthesis within minutes of wetting. This is what allows them to colonize bare rock, tree bark and polar and desert soils, and to begin the weathering and soil formation on which later colonists depend. They grow slowly, from less than a millimeter to a few centimeters per year, so the size of the largest thalli on a dated surface is used to date moraines and rockfalls (lichenometry). Because they absorb water and nutrients from the air over their whole surface and have no means of excluding pollutants, many lichens are killed by sulfur dioxide and by nitrogen deposition, and the composition of lichen communities is used to monitor air quality.

The two-partner view of lichens has been revised. Spribille et al. (2016) found that the cortex of many lichens of the large family Parmeliaceae contains basidiomycete yeasts of the Cyphobasidiales, whose abundance correlated with the thallus chemistry; lichen thalli also carry a characteristic bacterial community. Which of these additional partners are needed for a normal thallus is not yet known, but they may explain why lichens are difficult to resynthesize from the fungus and alga alone.

### 31.3.3. Endophytes and the Root Microbiome

Beyond these specialized organs, every healthy plant hosts bacteria and fungi on its leaves (the phyllosphere), on and around its roots, and inside its tissues.

**Definition 31.3.1 (Endophyte)** An **endophyte** is a bacterium or fungus that lives inside the tissues of a healthy plant, for at least part of its life, without causing disease.

The root microbiota is assembled in two steps: the plant enriches a subset of the soil community in the rhizosphere, and a still narrower subset enters the root, so that root communities of plants on different soils are more similar than the soils themselves; Actinomycetota, Pseudomonadota and Bacteroidota are enriched. Some of these microbes are beneficial:

- Plant growth promotion: rhizobacteria (for example *Pseudomonas* and *Bacillus* strains) solubilize phosphate, release siderophores that capture iron, produce or degrade plant hormones (auxins; the enzyme ACC deaminase lowers the level of the ethylene precursor ACC in roots and so the inhibition of root growth by ethylene), and fix nitrogen.
- Protection: some strains suppress soil-borne pathogens by producing antibiotics (2,4-diacetylphloroglucinol of *Pseudomonas* in soils suppressive to take-all disease of wheat) or by competing with them, and some prime the plant's own defenses throughout the shoot (*induced systemic resistance*, mediated by jasmonate and ethylene signalling).
- Fungal endophytes of grasses, *Epichloë* species, live in the intercellular spaces of leaves, are transmitted through the seed and produce alkaloids that protect their host against insects and grazing animals.

The plant side of these interactions, including plant immunity and the defense hormones, is treated in plant physiology ([7.13](/7.13)).

### 31.3.4. A Plant Pathogen Among the Root Bacteria

The crown gall bacterium *Agrobacterium tumefaciens*, its **Ti plasmid** and its use as the standard vector for transgenic plants are described in [7.11.17](/7.11.17#sec-17.3.2) and [7.4.19](/7.4.19#sec-19.1.2).

## 31.4. Insects and Their Endosymbionts

### 31.4.1. Nutritional Endosymbionts: *Buchnera* and Aphids

Insects that live on unbalanced diets — phloem or xylem sap, blood, wood — almost always carry bacterial symbionts that make up for what the diet lacks. Phloem sap is rich in sucrose but poor in nitrogen and almost devoid of the **essential amino acids**; aphids, whiteflies, psyllids, cicadas and leafhoppers feed on it throughout their lives.

**Definition 31.4.1 (Bacteriocyte)** A **bacteriocyte** is a specialized insect cell whose cytoplasm is packed with endosymbiotic bacteria; bacteriocytes are often grouped into an organ, the *bacteriome*.

Nearly all aphids harbor *Buchnera aphidicola*, a gammaproteobacterium related to the enterics, in bacteriocytes of the abdomen: a pea aphid contains several million cells. Experiments in which aphids were freed of *Buchnera* with antibiotics showed that they then require all the essential amino acids in an artificial diet; the genome of *Buchnera* (about 640 kb in the pea-aphid symbiont, Shigenobu et al. 2000) retains nearly complete pathways for the essential amino acids and riboflavin, while it has lost most genes for nonessential amino acids, cell-surface components, regulation and DNA repair. The synthesis is a joint venture: some steps of the pathways are encoded in the aphid genome and carried out by the bacteriocyte (for example, the transaminations at the ends of the pathways for branched-chain amino acids and phenylalanine), and the aphid supplies nonessential amino acids such as glutamine and aspartate as nitrogen sources. *Buchnera* is transmitted vertically: bacteria are transferred from maternal bacteriocytes into the developing embryos inside the mother (aphids reproduce parthenogenetically for most of the year). The cophylogenies of *Buchnera* and aphids match, the signature of strict **cospeciation** over the about 160–280 million years since the association began.

Many sap feeders carry two or more obligate symbionts that divide the work. In sharpshooters (leafhoppers of the Cicadellinae), *Sulcia muelleri* (Bacteroidota) makes eight essential amino acids and *Baumannia cicadellinicola* (a gammaproteobacterium) makes the remaining two and many vitamins; in citrus mealybugs, *Moranella endobia* lives inside the cytoplasm of *Tremblaya princeps*, itself inside the bacteriocytes, a bacterium within a bacterium. Besides such *primary* (obligate) symbionts, many insects carry facultative *secondary* symbionts that are not required for reproduction but can confer heat tolerance or protection against parasitoid wasps and fungi, and that can be gained, lost and occasionally transferred between host species.

Other examples: tsetse flies, which feed only on blood, depend on *Wigglesworthia* for B vitamins; carpenter ants on *Blochmannia* for nitrogen recycling; and the bean bug *Riptortus pedestris* acquires its *Caballeronia* (formerly *Burkholderia*) symbionts from the soil in every generation and filters them through a constricted region of the midgut that admits only the symbiont, a horizontal counterpart.

### 31.4.2. Termites and Lignocellulose

Wood is mostly cellulose, hemicellulose and lignin and contains little nitrogen. Termites, with their gut symbionts, digest 74–99 % of the cellulose they eat (Madigan et al. 2019), and in tropical savannas they rival grazing mammals in biomass. The hindgut, about a microliter in volume, is a microbial fermenter:

- In the "lower" termites, flagellated protists of the parabasalids and oxymonads ([7.11.20](/7.11.20)) phagocytose wood particles and ferment cellulose to acetate, $\ce{H2}$ and $\ce{CO2}$ in their hydrogenosomes (**hydrogenosome**, [7.11.3](/7.11.3)). The protists themselves carry ecto- and endosymbiotic bacteria, some of which fix nitrogen or make amino acids for them. In the "higher" termites (Termitidae, about three quarters of the species) the protists have been lost, and bacteria of the Spirochaetota and Fibrobacterota, among others, digest the fiber.
- The $\ce{H2}$ produced is used mainly by spirochetes that are **acetogens**, reducing $\ce{CO2}$ to acetate by the Wood–Ljungdahl pathway ([7.11.7](/7.11.7)), rather than by **methanogens**; acetate is absorbed by the termite and supplies most of its energy. Termites nevertheless emit methane, contributing a few percent of global emissions.
- The gut is not uniformly anoxic: oxygen diffuses from the gut wall into the outer 100–200 µm, where it is consumed by bacteria, giving radial gradients of $\ce{O2}$ and $\ce{H2}$ and distinct microhabitats.
- Nitrogen is supplied by nitrogen fixation by gut bacteria and by the recycling of uric acid.

Termites lose their gut symbionts at each molt and reacquire them from nestmates by proctodeal feeding, so that sociality is also a means of symbiont transmission. Fungus-growing termites (Macrotermitinae) and leaf-cutter ants have moved part of the digestion outside the body, into gardens of cultivated fungi ([7.11.21](/7.11.21)).

### 31.4.3. Reproductive Manipulators: *Wolbachia*

Maternally transmitted symbionts are passed on only by females, so any trait that increases the number or the success of infected daughters spreads, whether or not it benefits the host. *Wolbachia* ([7.11.17](/7.11.17#sec-17.3.3)), an alphaproteobacterium that lives in the cytoplasm of the germ line of perhaps half of all insect species and of many other arthropods and filarial nematodes, does this in four ways: it kills male embryos (male killing), converts genetic males into functional females (feminization, in woodlice), makes unfertilized eggs develop into females (induction of parthenogenesis, in haplodiploid wasps), and, most commonly, causes **cytoplasmic incompatibility**, in which embryos die when an infected male fertilizes an uninfected female. The genetics of incompatibility (the *cifA* and *cifB* genes, [Definition 11.6.3](/7.4.11#def-11.6.3)) and a model of its spread with an invasion threshold are given in [7.4.11](/7.4.11#sec-11.6.3).

The same biology is used against mosquito-borne viruses. *Wolbachia* strains from *Drosophila* transferred into *Aedes aegypti*, which is not naturally infected, both spread through populations by cytoplasmic incompatibility and inhibit the replication of dengue, Zika and chikungunya viruses in the mosquito; a cluster-randomized trial in Yogyakarta, Indonesia, found a 77 % reduction in dengue incidence in release areas (Utarini et al. 2021). Releasing only infected males, which sterilize the wild females they mate with, is a complementary strategy for suppressing mosquito populations. In filarial nematodes, *Wolbachia* is a mutualist on which the worms depend, so the antibiotic doxycycline, which kills the bacteria, is used to treat filariasis.

## 31.5. Symbioses of Marine Invertebrates

### 31.5.1. The Squid–*Aliivibrio* Light Organ

The Hawaiian bobtail squid *Euprymna scolopes* hunts at night in shallow water and hides its silhouette from predators below by emitting downward light that matches moonlight (counterillumination). The light is made by *Aliivibrio fischeri* (*Vibrio fischeri*, [7.11.17](/7.11.17#sec-17.5.3)) in a bilobed light organ in the mantle cavity. The association is a model of horizontal acquisition, because the squid hatches symbiont-free and can be raised either way, and only one bacterial species is involved (Figure 2):

1. Within an hour of hatching, cilia on the surface of the juvenile light organ sweep bacteria from seawater, and the squid secretes mucus in response to bacterial peptidoglycan. Gram-negative bacteria aggregate in the mucus, and *A. fischeri*, less than 0.1 % of the bacterioplankton, comes to dominate the aggregates within a few hours.
2. The bacteria migrate through pores and ducts into the crypts of the organ, a path guarded by nitric oxide and other antimicrobials that *A. fischeri* tolerates better than its competitors; chemotaxis towards chitin oligosaccharides released by the host guides them.
3. Each crypt is colonized by one or a few cells, which lose their flagella and grow to about $10^{9}$ cells per organ. The bacterial signals peptidoglycan monomer (tracheal cytotoxin) and lipopolysaccharide then induce the regression of the ciliated surface, so that the organ closes to further colonization ([7.5.38](/7.5.38#sec-38.9)).
4. At high density the bacteria switch on the *lux* operon by **quorum sensing** through LuxI–LuxR ([7.11.11](/7.11.11#sec-11.7.2)). Mutants without luciferase colonize but fail to persist: the host appears to sanction dark symbionts, probably through the oxygen they would otherwise consume.
5. Every dawn the squid expels about 90 % of its symbionts into the water and the rest regrow during the day, a daily cycle that renews the population and seeds the environment with symbionts for the next generation of hatchlings.

![A model of the daily cycle of the light organ (illustrative parameters). A: after the dawn expulsion of 90 % of the *Aliivibrio fischeri* cells, the remainder regrow logistically (r = 0.45 per hour); because the autoinducer concentration follows cell density, luminescence stays off while the population is small and is switched on only when density passes the quorum, here a few hours after dawn, so that the organ is fully bright by nightfall, when the squid hunts. B: light per cell as a Hill function of the autoinducer concentration (threshold 0.5, Hill coefficient 4), the switch-like response of the LuxI–LuxR circuit.](./plots/squid-light-organ.py)

### 31.5.2. Insect-Killing Nematodes and Their Bacteria

Nematodes of the families Steinernematidae and Heterorhabditidae carry gammaproteobacterial symbionts, *Xenorhabdus* and *Photorhabdus* respectively, in their intestine. Only one stage, a nonfeeding infective juvenile, lives in the soil; it enters an insect and releases its bacteria, which kill the insect and convert its tissues into food for the developing nematodes, while their antibiotics keep out competing microbes. *Photorhabdus* is also bioluminescent, so infected insect cadavers glow. When the cadaver is exhausted, new infective juveniles take up the symbionts and leave. The bacterial–nematode pairs show cospeciation, and the nematodes are sold for the biological control of soil-dwelling insect pests.

### 31.5.3. Chemosynthetic Symbioses

At hydrothermal vents and cold seeps ([7.11.29](/7.11.29)), where reduced compounds meet oxygenated seawater in darkness, many invertebrates are nourished by chemolithoautotrophic symbionts (**chemolithotroph**, [7.11.7](/7.11.7)).

- The giant tube worm *Riftia pachyptila*, up to 2 m long, has no mouth or gut as an adult. Its trunk is filled by the trophosome, a tissue of bacteriocytes with sulfur-oxidizing gammaproteobacteria (*Candidatus* Endoriftia persephone) at about $10^{9}$ cells per gram. The worm's red plume absorbs $\ce{O2}$, $\ce{H2S}$ and $\ce{CO2}$; its hemoglobin binds $\ce{O2}$ and sulfide at separate sites, delivering both to the symbionts while protecting the worm's own cytochrome oxidase from sulfide. The symbionts fix $\ce{CO2}$ with the Calvin cycle and the reverse TCA cycle, and the worm digests part of them. Each juvenile is infected anew through the skin from free-living symbionts in the water, and the symbiont, which has a free-living stage, has a large genome of a few megabases.
- Vesicomyid clams (*Calyptogena*) and lucinid clams carry sulfur oxidizers in their gills; the *Calyptogena* symbionts are transmitted vertically through the egg and have reduced genomes of about 1 Mb.
- *Bathymodiolus* mussels host sulfur-oxidizing and methanotrophic bacteria (**methanotroph**) in their gills, and at some vents the sulfur oxidizers also oxidize $\ce{H2}$.

Similar symbioses occur in shallow sediments (gutless oligochaete worms with several symbionts each), in sponges and in shipworms, whose symbionts digest wood and fix nitrogen.

### 31.5.4. Corals and Their Dinoflagellates

Reef-building corals live in clear, nutrient-poor tropical waters. They owe their productivity to photosynthetic dinoflagellates of the family Symbiodiniaceae ([7.11.20](/7.11.20#sec-20.4)) in their gastrodermal cells.

**Definition 31.5.1 (Zooxanthellae)** **Zooxanthellae** are the golden-brown photosynthetic symbionts of corals, sea anemones, giant clams and other marine invertebrates; in reef corals they are dinoflagellates of the family Symbiodiniaceae (formerly the single genus *Symbiodinium*, now divided into several genera such as *Breviolum*, *Cladocopium* and *Durusdinium*), living in symbiosomes within host cells at about $10^{6}$ cells per square centimeter of coral surface.

The symbionts transfer most of the carbon they fix, as glycerol, glucose, amino acids and lipids, to the host, covering much of a coral's energy needs in shallow water; the coral supplies $\ce{CO2}$, ammonium and phosphate from its metabolism and a sunlit, protected habitat, whose calcium carbonate skeleton scatters light and increases the light available to the symbionts. Photosynthesis also raises the pH and carbonate saturation at the site of calcification, so that symbiotic corals build their skeletons several times faster in the light. Most corals acquire their symbionts horizontally from seawater as larvae or juveniles; some transmit them in the egg.

**Definition 31.5.2 (Coral Bleaching)** **Coral bleaching** is the loss of zooxanthellae, or of their pigments, from the tissue of a coral, which turns the colony white as its skeleton shows through the transparent tissue; it is caused chiefly by temperatures above the local summer maximum, especially in combination with high irradiance.

Under heat stress the photosynthetic apparatus of the symbionts is damaged, reactive oxygen species accumulate, and the host expels or digests its symbionts; the symbionts may also retain more of their carbon and become less beneficial before bleaching. A sustained rise of about $1\,^\circ\mathrm{C}$ above the usual summer maximum for several weeks is sufficient, and the accumulated thermal stress is expressed in degree heating weeks. Bleached corals can recover their symbionts if conditions return to normal, but they are starving and die if bleaching is prolonged. Mass bleaching events have become frequent with ocean warming (1998, 2010, 2014–2017 and 2023–2024 were global events), and large parts of the Great Barrier Reef have bleached repeatedly since 2016. Tolerance depends partly on the symbiont: corals with heat-tolerant *Durusdinium* bleach at higher temperatures, at a cost in growth, and some corals shift their dominant symbiont after bleaching, but whether such shifts can keep pace with warming is doubtful.

## 31.6. Fermentation in the Guts of Mammals

### 31.6.1. Foregut and Hindgut Fermenters

Vertebrates do not make cellulases. Herbivorous mammals therefore house microbial fermenters in an enlarged section of the gut, either before the acid stomach (foregut fermenters: ruminants, camels, kangaroos, colobine monkeys, sloths, and among birds the hoatzin) or after the small intestine, in the cecum and colon (hindgut fermenters: horses, rabbits, rodents, elephants, many primates including humans). The position matters. In a foregut fermenter, the microbial cells themselves, with their protein and vitamins, pass on into the acid stomach and small intestine and are digested, and toxins in the food can be detoxified before absorption; but readily digestible sugars and protein of the food are fermented by the microbes before the host can use them. Hindgut fermenters absorb the food's easily digestible nutrients first, but most of the microbial protein is lost in the feces, unless it is recovered by eating feces (caecotrophy in rabbits and many rodents, which re-ingest special soft pellets from the cecum).

### 31.6.2. The Rumen

**Definition 31.6.1 (Rumen)** The **rumen** is the largest chamber of the four-part stomach of ruminants (cattle, sheep, goats, deer and their relatives), a continuously fed anaerobic fermentation vessel in which bacteria, archaea, protists and fungi digest plant polysaccharides to short-chain fatty acids, $\ce{CO2}$ and $\ce{CH4}$.

Food passes into the reticulum and rumen (together the reticulorumen), which in a cow hold 100–150 L at $39\,^\circ\mathrm{C}$ and pH 5.5–7; large particles are regurgitated, chewed again with bicarbonate-rich saliva (rumination; a cow secretes well over 100 L of saliva a day) and swallowed, and small particles pass through the omasum into the abomasum, the acidic true stomach, where the microbes are killed and digested (Figure 3). Food stays in the rumen for 20–50 h, long enough for cellulose to be degraded, which takes much longer than starch digestion.

The rumen contains $10^{10}$–$10^{11}$ bacteria and about $10^{6}$ ciliates per milliliter, together with anaerobic fungi and methanogenic archaea, and works as a food web of guilds:

- Fibrolytic bacteria attach to plant particles and degrade cellulose and hemicellulose: *Fibrobacter succinogenes* (Fibrobacterota) with enzymes on its outer membrane, and *Ruminococcus albus* and *R. flavefaciens* (Bacillota) with cellulosomes, multienzyme complexes on the cell surface (**cellulose**, [7.1.10](/7.1.10)). Anaerobic fungi of the Neocallimastigomycota, which have hydrogenosomes, penetrate the tough plant tissues with rhizoids and loosen them.
- Amylolytic and saccharolytic bacteria (*Prevotella*, *Ruminobacter*, *Selenomonas*, *Streptococcus bovis*) ferment starch and sugars; secondary fermenters convert succinate to propionate (*Schwartzia*) and lactate to propionate and acetate (*Megasphaera elsdenii*).
- Methanogens (*Methanobrevibacter ruminantium* and relatives), partly attached to the surface of ciliates, consume $\ce{H2}$ and reduce $\ce{CO2}$ to $\ce{CH4}$. Keeping the $\ce{H2}$ partial pressure low allows the fermenters to reoxidize their NADH by making $\ce{H2}$ rather than reduced products, which yields more acetate and ATP — the interspecies hydrogen transfer of **syntrophy**.

**Definition 31.6.2 (Short-Chain Fatty Acid)** A **short-chain fatty acid** (SCFA; *volatile fatty acid* in animal nutrition) is a monocarboxylic acid with one to six carbon atoms, chiefly acetate ($\ce{C2}$), propionate ($\ce{C3}$) and butyrate ($\ce{C4}$), formed by the microbial fermentation of carbohydrates in the gut and absorbed by the host as a source of energy and carbon.

The products of rumen fermentation can be summarized by an overall stoichiometry for a forage diet (Madigan et al. 2019):

**Formula 31.6.1 (Rumen Fermentation)**

$$
\begin{aligned}
57.5\,\ce{C6H12O6} \longrightarrow\ & 65\,\text{acetate} + 20\,\text{propionate} + 15\,\text{butyrate} \\
&+ 60\,\ce{CO2} + 35\,\ce{CH4} + 25\,\ce{H2O},
\end{aligned} \tag{31.1}
$$
with the acids written as their free forms $\ce{C2H4O2}$, $\ce{C3H6O2}$ and $\ce{C4H8O2}$; carbon, hydrogen and oxygen balance. At steady state the rumen fluid contains about 60 mM acetate, 20 mM propionate and 10 mM butyrate.

The fatty acids are absorbed through the rumen wall and meet 60–80 % of a ruminant's energy needs: acetate and butyrate are oxidized and used for fat synthesis (milk fat comes largely from acetate), and propionate is the main substrate of gluconeogenesis in the liver, from which a ruminant, which absorbs almost no glucose from its gut, makes the glucose it needs (including the lactose of milk). Comparing the heats of combustion of the products with that of glucose shows where the energy of the food goes (Figure 3B; Question 4): about three quarters is retained in the fatty acids, a little is released as heat in the fermentation and used by the microbes for growth, and almost a fifth of the energy of the fermented sugar is lost as methane, belched out by eructation. The microbial cells that grow on this energy, washed into the abomasum, supply the ruminant with most of its protein: rumen bacteria make amino acids from ammonia, which ruminants can be fed as urea, and the B vitamins and vitamin K.

![A: the path of food through the ruminant stomach and the guilds of the rumen food web (schematic). Feed enters the reticulorumen, coarse particles are regurgitated and chewed again with bicarbonate-rich saliva, and small particles pass through the omasum to the acidic abomasum, where the microbial cells are digested. In the rumen, fibrolytic and amylolytic bacteria, anaerobic fungi and ciliates hydrolyze and ferment plant polysaccharides; secondary fermenters convert succinate and lactate; methanogens remove H2 as CH4, which is belched out; the short-chain fatty acids are absorbed through the rumen wall. B: where the energy of the fermented glucose goes, computed from the overall stoichiometry (Eq. (31.1)) and the heats of combustion of glucose, the three acids and methane. Data from Madigan et al. (2019).](./plots/rumen-fermentation.py)

Changes in the diet change the community. When a cow is switched abruptly from forage to grain, *S. bovis* grows rapidly on the starch and its lactic acid, a stronger acid than the SCFAs, lowers the pH below 5.5; the fibrolytic bacteria and ciliates are inhibited, and severe **acidosis** can kill the animal. Feedlot cattle are therefore adapted to grain gradually. A single species can also add a capability: the rumen bacterium *Synergistes jonesii* degrades the toxic pyridine diols formed from mimosine in the tropical legume *Leucaena*; ruminants in Hawaii carried it and those in Australia did not, until Australian cattle were inoculated with it, after which they could feed on *Leucaena* without poisoning.

Ruminant methane is about a third of the methane emitted by human activities, and a cow emits a few hundred grams a day; reducing it would both limit warming and save feed energy (2–12 % of the gross energy intake is lost as methane, depending on diet). Measures that lower emissions include diets richer in concentrates or lipids, the inhibitor 3-nitrooxypropanol, which blocks methyl-coenzyme M reductase, the last enzyme of methanogenesis ([7.11.7](/7.11.7)), and reduces emissions by about a quarter to a third in feeding trials, and supplements of the red alga *Asparagopsis*, whose bromoform inhibits the same step; breeding for low-emission animals and the persistence and safety of these additives are under study.

### 31.6.3. Hindgut Fermentation

Horses ferment fiber in an enlarged cecum and colon with a microbiota similar in its guilds to that of the rumen; they digest fiber less completely than ruminants but process larger amounts of low-quality forage faster, because food passes through more quickly. In rabbits the cecum separates small particles and microbes from coarse fiber, and the soft cecal pellets eaten directly from the anus return microbial protein and vitamins to the stomach. The giant panda, a carnivore by descent eating almost only bamboo, has a short gut and a microbiota of the carnivore type, and digests only a small fraction of the cellulose it eats; it compensates by eating large amounts. The human colon is a hindgut fermenter of moderate capacity, in which SCFAs supply a few percent to about a tenth of the energy ([7.11.32](/7.11.32)).

## 31.7. Living Inside a Host: The Evolution of Symbiont Genomes

The genomes of obligate symbionts show a consistent set of changes (Figure 4), whose population-genetic causes are discussed in [7.10.18](/7.10.18#sec-18.8.3):

- Size: obligate intracellular symbionts of insects have genomes of 0.1–0.8 Mb, compared with 2–8 Mb in free-living relatives; the smallest bacterial genomes known (about 110–150 kb, in *Nasuia*, *Tremblaya*, *Hodgkinia* and *Carsonella*) belong to sap-feeder symbionts and encode fewer genes than some giant viruses. Genes for functions the host provides (cell-wall synthesis, regulation, many transporters, DNA repair and recombination) are lost first; genes for the nutrients that the symbiont supplies are kept.
- Base composition: most such genomes are strongly AT-rich (often 20–30 % GC). Mutation in bacteria is biased towards GC→AT changes (deamination of cytosine, oxidation of guanine), and the loss of repair genes and the weakness of selection let the genome drift towards the mutational equilibrium; exceptions such as *Tremblaya* (59 % GC) show that the bias is not universal.
- Rates: symbiont genes evolve faster than those of free-living relatives, and their proteins accumulate slightly deleterious substitutions; many symbionts overproduce the chaperonin GroEL, which may help misfolded proteins fold.

![A: genome size and GC content of obligate endosymbionts of animals (red; segments show the range among *Buchnera* and *Blochmannia* strains) and of some free-living bacteria (blue). The symbionts of aphids (*Buchnera*), tsetse flies (*Wigglesworthia*), carpenter ants (*Blochmannia*), sharpshooters (*Sulcia*) and mealybugs (*Moranella*, *Tremblaya*) and the gill symbiont of the clam *Calyptogena magnifica* (*Ruthia*) have genomes of 0.14–1.2 Mb, most of them AT-rich; *Tremblaya* is a GC-rich exception. Symbiont data from Madigan et al. (2019). B: without selection on base composition, GC content approaches the mutational equilibrium GC* = u/(u + v), where u and v are the rates of AT→GC and GC→AT mutation; the GC→AT bias of bacterial mutation, unopposed after the loss of repair genes, drives genomes towards low GC (illustrative ratios v/u).](./plots/symbiont-genomes.py)

The cause is chiefly drift. A symbiont that is transmitted vertically passes through a severe bottleneck in every host generation and lives as many small, asexual, non-recombining populations. In such populations selection against slightly deleterious mutations is ineffective, gene losses that are only slightly harmful are fixed, and the loss of the least-mutated class repeats irreversibly by **Muller's ratchet** ([Definition 14.2.4](/7.10.14#def-14.2.4)). Because lost genes cannot be regained without recombination or gene transfer, genome reduction is one-way, and the host becomes dependent on a partner that is slowly degenerating. Hosts respond by adding new partners that take over failing functions, by importing proteins into the symbionts (aphids target host-encoded proteins to *Buchnera*; the amoeba *Paulinella* imports nucleus-encoded proteins into its photosynthetic cyanobacterial organelle), and occasionally by replacing an old symbiont with a new one. The endpoint of such dependency, with genes transferred to the host nucleus and proteins imported back, is an organelle: mitochondria and plastids ([7.10.28](/7.10.28)). Horizontally transmitted symbionts, such as rhizobia, *Aliivibrio* and the *Riftia* symbiont, which must survive in the environment and compete there, keep large genomes.

## Summary

- Symbioses (Definition 31.1.1) range from mutualism through commensalism to parasitism, and outcomes depend on the partners and conditions. Transmission (Definition 31.1.2) is vertical (aligning symbiont and host interests, genome reduction) or horizontal (selection of partners by the host in each generation, large symbiont genomes).
- Legume nodules (Definition 31.2.1, Figure 1): flavonoids → NodD → *nod* genes → **Nod factors** (Definition 31.2.2) → LysM receptors, calcium spiking → root-hair curling, infection thread, cortical cell division → **bacteroids** in symbiosomes (Definition 31.2.3) that receive malate and return ammonium. **Leghemoglobin** (Definition 31.2.4) and a diffusion barrier keep free $\ce{O2}$ low; the plant controls the costly symbiosis by nitrate inhibition, autoregulation and sanctions. *Frankia*, *Nostoc*–*Azolla* and cycads are other nitrogen-fixing symbioses.
- Mycorrhizae trade phosphate and nitrogen for sugars and (arbuscular fungi) fatty acids, through a signalling pathway shared with nodulation. Lichens are desiccation-tolerant pioneers and pollution indicators with additional yeast and bacterial partners. Endophytes (Definition 31.3.1) and rhizobacteria promote growth and induce systemic resistance.
- Insects: *Buchnera* and other bacteriocyte symbionts (Definition 31.4.1) supply essential amino acids and vitamins; termite hindgut protists and bacteria ferment wood to acetate, with $\ce{H2}$ consumed by acetogens; *Wolbachia* manipulates host reproduction and is used to block dengue transmission.
- Marine invertebrates: the squid light organ selects *Aliivibrio fischeri* in steps and depends on quorum-sensed luminescence (Figure 2); vent tube worms, clams and mussels live on chemolithoautotrophic symbionts; corals depend on **zooxanthellae** (Definition 31.5.1), and **coral bleaching** (Definition 31.5.2) under heat stress threatens reefs.
- The **rumen** (Definition 31.6.1) ferments fiber to **short-chain fatty acids** (Definition 31.6.2), $\ce{CO2}$ and $\ce{CH4}$ (Formula 31.6.1, Figure 3); the ruminant lives on the acids and on the digested microbes. Hindgut fermenters ferment after the small intestine.
- Obligate, vertically transmitted symbionts evolve small, AT-rich, fast-evolving genomes through drift and Muller's ratchet (Figure 4); the extreme is the organelle.

## Questions

1. A rhizobium mutant forms normal-looking but white nodules on its host and the plants are nitrogen-starved. Give three different defects, in bacterium or plant, that could produce this phenotype, and how you would distinguish them.

   **Answer** White nodules lack functional leghemoglobin or fixation. (a) A bacterial *nif* or *fix* mutant (nitrogenase, its cofactor, the *cbb*$_3$ oxidase or FixL–FixJ): nodules form but no acetylene reduction is detected; complementation with the cloned gene restores fixation. (b) A *dctA* mutant: bacteroids cannot take up malate and succinate and so cannot power nitrogenase; the mutant fails to grow on succinate in culture. (c) A plant defect, such as silenced leghemoglobin synthesis: the same wild-type bacterium fixes nitrogen on normal plants, and nodules of the mutant plant contain more free $\ce{O2}$. Swapping bacterial and plant partners distinguishes bacterial from plant causes.

2. Nitrogenase needs 16 ATP and 8 electrons per $\ce{N2}$. Assuming respiration of sugar yields about 30 ATP and 24 electrons per glucose (6 C), estimate the minimum carbon cost per gram of nitrogen fixed, and explain why measured costs are higher.

   **Answer** Per $\ce{N2}$ (28 g N) about 16 ATP plus 8 electrons are needed; 16 ATP require about $16/30$ glucose and 8 electrons $8/24$ glucose, together about 0.87 glucose, 5.2 C atoms, or 62 g C — about 2.2 g C per g N as a theoretical minimum. Measured costs (about 4–10 g C per g N) are higher because the electrons also reduce protons to $\ce{H2}$ (at least a quarter of them), part of the respiration is uncoupled from fixation, ammonium must be assimilated and exported, and the plant builds and maintains the nodule and feeds bacteroid growth.

3. Explain why genomes of *Buchnera* are small and AT-rich while that of the *Riftia* symbiont is large, although both are obligately dependent on their animal host.

   **Answer** *Buchnera* is transmitted vertically, through a bottleneck of a few cells in every generation, and lives in small, asexual, non-recombining populations in which drift dominates selection: slightly harmful gene losses and GC→AT mutations are fixed, and Muller's ratchet makes the loss irreversible. The *Riftia* symbiont is acquired horizontally from a free-living population, so it must survive, compete and colonize outside the host, retains the genes needed for that, and its large free-living population allows selection to remove deleterious mutations.

4. Using the heats of combustion of glucose (2803 kJ/mol), acetic acid (874), propionic acid (1527), butyric acid (2183) and methane (890 kJ/mol), compute from Eq. (31.1) the fractions of the energy of fermented glucose that end in the fatty acids and in methane. What becomes of the rest?

   **Answer** Glucose: $57.5 \times 2803 = 161\,200$ kJ. Fatty acids: $65 \times 874 + 20 \times 1527 + 15 \times 2183 = 56\,810 + 30\,540 + 32\,745 = 120\,100$ kJ, 74.5 %. Methane: $35 \times 890 = 31\,150$ kJ, 19.3 %. The remaining about 6 % is released in the fermentation; part of it is conserved as ATP and used for microbial growth (the microbes are then digested by the host), the rest is heat. A ruminant thus loses nearly a fifth of the energy of the fermented carbohydrate as methane.

5. Why can a coral recover from a brief bleaching event but die after a long one, and why does a coral that hosts *Durusdinium* grow more slowly?

   **Answer** A bleached coral has lost most of the photosynthate that covers its energy budget; it survives briefly on reserves and heterotrophic feeding, and can repopulate from the few remaining symbionts or from seawater when temperatures fall. If stress persists, its reserves are exhausted and it starves and becomes susceptible to disease. Heat-tolerant *Durusdinium* symbionts transfer less carbon to their host than the usual *Cladocopium*, so the coral gains thermal tolerance at the cost of a smaller energy supply and slower growth.
