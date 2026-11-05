---
title: Viral Diversity, Ecology and Subviral Agents
description: The diversity of viruses across the hosts of all three domains; archaeal virus morphologies, giant viruses and virophages; ICTV classification and the origin of viruses; marine viral ecology, the viral shunt, kill-the-winner and piggyback-the-winner, auxiliary metabolic genes and viromics; plant and insect viruses; and the subviral agents — viroids, satellites, hepatitis delta and prions.
---

The three preceding chapters followed single viruses through single cells. This one steps back twice. First to the whole of the virosphere: the viruses of bacteria and archaea, of animals, plants, fungi and protists, the giant viruses that blur the line between a virus and a cell, and the question of how classification and phylogeny can be done at all for a group with no gene shared by all its members. Then to ecology: viruses are the most abundant biological entities on Earth, they kill a large fraction of the ocean's microorganisms every day, and in doing so they move carbon, limit blooms and maintain diversity. The chapter ends below the level of viruses, with agents that have only a genome and no protein (viroids and satellites) or only a protein and no genome (prions).

Two threads from earlier chapters run through it. The Baltimore classes of [7.11.22](/7.11.22) organize the diversity; the arms race of [7.11.23](/7.11.23) and the error-prone replication of [7.11.25](/7.11.25) explain much of the evolution. The origin of viruses was introduced from the side of the tree of life in [7.10.27](/7.10.27#sec-27.7) and is taken up here from the side of the viruses themselves.

## 26.1. The Shape of the Virosphere

Every cellular organism that has been looked at carefully has viruses. Their distribution over the Baltimore classes, however, is strikingly uneven, and the unevenness is informative.

- Bacteria and archaea are infected overwhelmingly by double-stranded DNA viruses (class I). Single-stranded DNA phages (class II, ϕX174 and M13) and RNA phages (classes III and IV, ϕ6 and MS2) exist but are a small minority of isolates, and no class V or VI virus of a prokaryote is known.
- Animals are the only hosts in which all seven classes occur. Negative-strand RNA viruses (class V) and retroviruses (class VI) are essentially confined to them.
- Plants are dominated by positive-strand RNA viruses, have many more single-stranded DNA viruses than animals do, and host most known class VII (reverse-transcribing DNA) viruses, the caulimoviruses.
- Fungi are infected almost exclusively by RNA viruses of classes III and IV. Most are transmitted only by hyphal fusion and cell division — they have no extracellular phase at all, which makes the boundary between a virus and a cytoplasmic genetic element thin.
- Protists host the largest known viruses, including the giant viruses of amoebae (§26.3), together with a wide range of RNA viruses.

![Scale and distribution of the virosphere. A: genome sizes, from the 246-nucleotide coconut cadang-cadang viroid and the 1.75 kb circovirus to the 2.5 Mb pandoravirus, which exceeds the genomes of several bacteria and archaea; RNA genomes (orange) occupy a narrow band around 10 kb, DNA genomes (blue) four orders of magnitude. B: the number of described virus species by Baltimore class for each host group, showing the dominance of class I in prokaryotes, of class IV in plants and of the full spectrum in animals. Data from Madigan et al. (2019) after Nasir and Caetano-Anollés (2015)](./plots/virosphere.py)

Genome size spans almost four orders of magnitude (Figure A above). The upper end belongs to double-stranded DNA: phage G of *Bacillus* at about 500 kb, mimivirus at 1.2 Mb, pandoravirus at 2.5 Mb, larger than the genome of a mycoplasma and encoded in a particle larger than some bacterial cells. The lower end belongs to RNA, for the reason given in [7.11.25](/7.11.25#sec-25.2): an unproofread polymerase sets an error threshold, and a genome longer than about $\mu^{-1}$ cannot be maintained. The only RNA viruses that exceed 15 kb are the coronaviruses, which proofread.

**Remark 26.1.1** Classification by host and classification by genome strategy answer different questions. Host range tells us where a virus lives and how it is transmitted; the Baltimore class tells us what problem its genome must solve in order to be expressed and copied, and therefore what its molecular biology looks like. The older textbook division into bacterial, plant, vertebrate and insect viruses survives in applied contexts (plant pathology, medical virology) but groups viruses that have nothing molecular in common.

## 26.2. Viruses of Archaea

Archaeal viruses were long a curiosity and are now one of the most distinctive parts of the virosphere. Almost all characterized isolates have double-stranded DNA genomes, usually circular; RNA viruses of archaea have not been propagated in the laboratory, although metagenomes from acidic hot springs contain positive-strand RNA sequences, complete with a replicase gene, that cannot come from the bacteria or eukaryotes present and are almost certainly archaeal.

What is unusual is the morphology. Viruses of halophilic and methanogenic *Euryarchaeota* are often head-and-tail particles resembling the phages of enteric bacteria, but the viruses of hyperthermophilic *Crenarchaeota* include shapes seen nowhere else:

| Morphotype | Example | Host | Particle |
|---|---|---|---|
| Spindle (lemon-shaped) | SSV1 | *Sulfolobus solfataricus* | $40 \times 80\,\mathrm{nm}$, circular genome about 15 kb, often in rosettes |
| Filamentous, rigid | SIFV | *S. solfataricus* | $50 \times 900$–$1500\,\mathrm{nm}$, linear genome |
| Two-tailed spindle | ATV | *Acidianus convivator* | lemon-shaped on release, then grows a tubular tail at each end |
| Spindle with short tail | PAV1 | *Pyrococcus abyssi* | $80 \times 120\,\mathrm{nm}$, released without lysis |
| Bottle-shaped, droplet, coil | ABV, SNDV, AFV | thermoacidophiles | no counterpart among bacterial or eukaryotic viruses |

![Morphotypes of archaeal viruses, drawn to scale against a head-and-tail bacteriophage. From left: the spindle-shaped SSV1 of *Sulfolobus solfataricus*, often released in rosettes; the rigid filamentous SIFV; the bottle-shaped ABV; and ATV of *Acidianus convivator*, which leaves the cell as a lemon and extends a hollow tail at each end over the following hours, outside any cell. Dimensions as in the table of §26.2](./plots/archaeal-viruses.py)

**Example 26.2.1** ATV is the only known case of virion development in the complete absence of a host cell. Virions released by lysis are lemon-shaped; over the next hours, at $85\,^\circ\mathrm{C}$ and $\mathrm{pH}\ 1.5$, each extends a hollow tube from both ends while the body becomes thinner, with no input of energy or material from outside. The tails are thought to help the particle find or attach to a cell in an environment where diffusion is the only transport. ATV is also lysogenic, which is rare among archaeal viruses.

PAV1 and SSV1 look alike but share almost no sequence, so similar morphology here does not imply common ancestry — one reason morphology was abandoned as a basis for classification (§26.4). Many archaeal viruses leave the cell without lysing it, by budding or through a dedicated pyramidal structure that pushes through the S-layer, and lysogeny and chronic release are more common than the lytic cycle. The hosts are the organisms of [7.11.19](/7.11.19).

## 26.3. Giant Viruses and Virophages

**Definition 26.3.1 (Giant Virus)** A **giant virus** is a double-stranded DNA virus of a eukaryote whose particle (0.2–1.5 μm) and genome (0.3–2.5 Mb) are in the size range of cellular microorganisms, and which encodes functions — translation factors, aminoacyl-tRNA synthetases, tRNAs, DNA repair and metabolic enzymes — otherwise thought to be the property of cells. Giant viruses belong to the phylum *Nucleocytoviricota*, the group earlier called the nucleocytoplasmic large DNA viruses (NCLDV), which also contains the poxviruses, iridoviruses and algal phycodnaviruses.

Mimivirus was isolated from *Acanthamoeba* in a cooling tower and was first taken for a bacterium: it is 0.75 μm across, its capsid is covered with fibrils, and it stains Gram-positive. Its 1.2 Mb genome encodes about a thousand proteins, among them four aminoacyl-tRNA synthetases and several translation factors. Pandoraviruses, from marine amoebae, have ovoid particles about 1 μm long and genomes to 2.5 Mb, of which only some 7 % of genes have recognizable homologs in the databases. Pithovirus, recovered from 30 000-year-old Siberian permafrost, has the largest particle known, about 1.5 μm.

These discoveries revived two old ideas. The first, that giant viruses are reduced cells and should be a fourth domain of life, was based on their translation-related genes. It is not supported: phylogenies of the conserved core genes place *Nucleocytoviricota* as a monophyletic viral group whose translation genes were acquired piecemeal from hosts at different times, and no giant virus has a ribosome or makes ATP. The second idea, that the boundary between viruses and cells is a continuum rather than a line, remains useful; the operational criterion stays the one of [7.11.22](/7.11.22) — a virus has no ribosomes and no energy metabolism, and reproduces by assembly from separately synthesized parts rather than by growth and division.

**Definition 26.3.2 (Virophage)** A **virophage** is a small double-stranded DNA virus that reproduces only in a cell coinfected by a giant virus, using the giant virus's transcription machinery and its cytoplasmic viral factory, and reduces the yield of that helper. Sputnik, the first example, has an 18 kb genome encoding 21 proteins in a 75 nm icosahedral capsid and replicates only in mimivirus-infected *Acanthamoeba*.

Whether these are satellites (§26.9) or a distinct category is partly a question of definition: like a satellite virus, a virophage depends on a helper, is not derived from it and depresses its replication; unlike one, it has a substantial genome of its own and encodes its own capsid and replication proteins (a primase-helicase in Sputnik, a protein-primed DNA polymerase in mavirus). The ecologically interesting consequence is that a virophage behaves as a defence of the cellular host. A population of the marine flagellate *Cafeteria roenbergensis* carrying the integrated virophage mavirus survives a giant-virus epidemic that would otherwise destroy it, because the virophage lowers the burst size of the helper — one of the few known cases of a virus acting as an inducible immune system for a eukaryote.

## 26.4. Classification and Nomenclature

The International Committee on Taxonomy of Viruses (ICTV) maintains the formal classification. Its present framework differs in two ways from the one in most textbooks.

First, the hierarchy is complete. Fifteen ranks run from realm through kingdom, phylum, class, order and family to genus and species, with suffixes that identify the rank (*-viria* for realms, *-virae* kingdoms, *-viricota* phyla, *-viricetes* classes, *-virales* orders, *-viridae* families, *-virus* genera). Six realms are recognized, each defined by a hallmark gene rather than by a host or a shape:

| Realm | Hallmark | Contents |
|---|---|---|
| *Riboviria* | RdRp, or reverse transcriptase | all RNA viruses, retroviruses, hepadnaviruses |
| *Duplodnaviria* | HK97-fold major capsid protein | tailed bacterial and archaeal viruses, herpesviruses |
| *Varidnaviria* | double jelly-roll capsid protein | *Nucleocytoviricota*, adenoviruses, PRD1-like phages |
| *Monodnaviria* | HUH endonuclease (rolling-circle initiator) | CRESS-DNA viruses, microviruses, parvoviruses, papilloma- and polyomaviruses |
| *Adnaviria* | A-form DNA in a filamentous capsid | filamentous viruses of hyperthermophilic archaea |
| *Ribozyviria* | self-cleaving ribozyme, circular RNA | hepatitis delta virus and its relatives |

Second, groupings based on morphology have been abolished. The families *Myoviridae*, *Siphoviridae* and *Podoviridae*, defined by contractile, long non-contractile and short tails, were dissolved in 2022: tail morphology is homoplastic, and genome comparisons show that it says little about relatedness. All tailed phages now belong to the class *Caudoviricetes*, subdivided by sequence. Tail morphology survives as a description — one may still call T4 myovirus-like — but not as a taxon. The spindle-shaped archaeal viruses of §26.2 have no counterpart elsewhere and their place in the hierarchy is still unsettled.

Species names are now binomial, in the form *Genus species*: dengue virus, for example, is the species *Orthoflavivirus denguei*. Taxon names are italic and capitalized; the name of the physical agent ("dengue virus", "phage T4") is not a taxon, is written in roman type and is what one normally uses in text.

**Remark 26.4.1** A classification of viruses cannot be a single phylogeny. No gene is present in all viruses, so there is no equivalent of the ribosomal RNA tree of [7.11.16](/7.11.16); the realms are therefore several separate trees, each rooted in its own hallmark gene, and lateral exchange between them is common. Where a group does share a set of genes — the *Nucleocytoviricota*, the retroviruses, the tailed phages — ordinary phylogenetic methods ([7.8.6](/7.8.6)) work well within it.

## 26.5. The Origin of Viruses

The three hypotheses for the origin of viruses are set out in [7.10.27](/7.10.27#sec-27.7): regression of parasitic cells, escape of cellular genetic elements, and descent from replicators that preceded cells. The evidence from virology itself favours no single answer, and increasingly favours all three at once for different lineages.

- The capsid folds argue for deep ancestry and for polyphyly. Only a handful of major capsid protein folds exist — the HK97 fold, the single and double jelly roll, the filamentous archaeal fold — and each is shared across viruses of all three domains while having no cellular homolog. That pattern is what one expects if a few ancient lineages of capsid-forming elements diversified with their hosts, and it is why the realms are defined this way.
- The polymerases argue for repeated escape. Viral polymerases, helicases and ligases are frequently more closely related to cellular or plasmid enzymes than to those of other viruses, and giant-virus genomes are visibly patchworks of host-derived genes.
- The reduction hypothesis has no clear case. Giant viruses were its best candidate and no longer support it (§26.3).

A fourth consideration cuts across these. Viruses are plausibly older than the last universal common ancestor: reverse transcription has been proposed as the route by which an RNA world acquired DNA, with DNA appearing first in viral genomes as a way of escaping cellular ribonucleases and only later being adopted by cells. The argument is speculative, but it illustrates why "viruses are escaped host genes" cannot be the whole story — the host would have to have had the genes first.

What is certain is coevolution. Every defence described in [7.11.23](/7.11.23) and [7.11.27](/7.11.27) has a viral counter, every counter a new defence, and the genes involved are among the fastest-evolving in both partners. A large part of the gene content of bacterial, archaeal and animal genomes — restriction systems, CRISPR arrays, prophages, endogenous retroviruses, the recombination machinery of adaptive immunity — exists because of viruses.

## 26.6. The Ecology of Viruses

Numbers first. Seawater contains about $10^6$ prokaryotic cells and $10^7$ virus particles per millilitre; over the whole biosphere the standing stock is of order $10^{31}$ particles, the most abundant biological entity on the planet, although their small size makes them only some 5 % of microbial biomass. Between 5 % and 50 % of the bacteria in surface seawater are killed by viruses each day, a mortality comparable to that from grazing by protists.

**Definition 26.6.1 (Viral Shunt)** The **viral shunt** is the diversion of carbon and nutrients from higher trophic levels back into the dissolved organic matter pool by viral lysis. Cell contents released by lysis are taken up by the surviving heterotrophic bacteria and respired, rather than being transferred to grazers; the consequence is to retain nitrogen, phosphorus and iron in the surface layer, to stimulate bacterial production, and to reduce the fraction of primary production that reaches larger organisms or sinks to the deep ocean.

![The viral shunt in the marine microbial loop. Primary production by phytoplankton and cyanobacteria is grazed by protists and passed up the food web (grey arrows), or lysed by viruses (red). Lysis returns the cell contents to the dissolved organic matter pool, from which heterotrophic bacteria take them up and respire them, short-circuiting the transfer to higher trophic levels and retaining nutrients in the surface layer. Typical standing stocks are given per millilitre of surface seawater; 5–50 % of the bacterial standing stock is lysed each day. The export of particulate carbon to depth is reduced correspondingly](./plots/viral-shunt.py)

The global flux is large: lysis is estimated to release $10^8$ to $10^9$ tonnes of carbon per day from marine microorganisms, and the biogeochemical consequences are taken up with the element cycles in [7.11.29](/7.11.29) and [7.11.30](/7.11.30).

Viral predation also structures communities, and two complementary models describe how.

**Definition 26.6.2 (Kill the Winner)** In the *kill-the-winner* model, lytic viruses are host-specific and their reproduction is proportional to the abundance of their host. The competitively superior bacterial population grows fastest, is therefore cropped hardest, and never excludes its competitors. Viral predation thus converts competition for a limiting nutrient — which by itself would lead to competitive exclusion ([7.11.4](/7.11.4)) — into a community in which many slow-growing populations coexist with a few fast-growing ones held down by their viruses.

**Remark 26.6.1** The counterpart at high host density is *piggyback-the-winner*: in habitats where hosts are abundant and growing fast — coral reefs, the gut, dense blooms — the measured ratio of viruses to cells falls and the proportion of lysogens rises, the reverse of what kill-the-winner predicts. The explanation offered is that a temperate virus in a rapidly growing host does better by replicating with it, and by excluding related viruses through superinfection immunity, than by lysing it. The classical view that lysogeny is the strategy of starvation (§[7.11.23](/7.11.23#sec-23.7)) and this one both have support; which prevails appears to depend on host growth rate as well as host density.

![Viral control of a microbial community, simulated in a chemostat. A: kill the winner. Two bacterial populations compete for one nutrient; population 1 is the better competitor and excludes population 2 when viruses are absent (dotted). With a host-specific lytic virus on each, both persist, because each host is pinned near $(D+m)/[(\beta-1)\varphi]$ — a density set by its virus, not by its competitive ability. B: the same model run to steady state over a range of nutrient supply. Host density hardly changes while virion density rises, so a purely lytic model predicts a virus-to-cell ratio that increases with productivity; the decline measured in highly productive habitats is the piggyback-the-winner pattern and requires lysogeny. Parameters in the script](./plots/kill-the-winner.py)

Finally, viruses are a reservoir and a conveyor of genes. Marine cyanophages carry *auxiliary metabolic genes*, host-derived genes that are expressed during infection and support the metabolism the virus depends on: the clearest case is the *psbA* gene for the D1 protein of photosystem II in phages of *Prochlorococcus* and *Synechococcus*. D1 turns over rapidly under illumination, and host protein synthesis is shut off during infection; a phage-encoded copy keeps photosynthesis — and therefore the ATP and NADPH the phage needs — running to the end of the latent period. Phage-borne *psbA* alleles also circulate among host strains, so the phage population is a shared gene pool for photosynthesis. Transduction, the other route ([7.11.13](/7.11.13)), moves host genes between cells on a similar scale.

## 26.7. Viromics and the Human Virome

**Definition 26.7.1 (Virome)** The **virome** is the whole set of viral genomes in a defined sample — a habitat, a community, an organism or an organ. Because viruses have no universal marker gene, a virome is characterized by shotgun sequencing of the viral size fraction and assembly, not by amplicon surveys; the analysis is that of [7.8.14](/7.8.14#sec-14.6.2).

Every such study returns the same result: most of what is there is unknown. Typically about three quarters of the sequences in a viral metagenome match nothing in the databases, against roughly a tenth for bacterial metagenomes. Most viral diversity is therefore undescribed, and the pace of description now depends on computation rather than on isolation. A virus can be assembled, classified by its hallmark gene, assigned a host by matching CRISPR spacers in the bacterial genomes of the same sample, and placed in a family before anyone has grown it. crAssphage, the most abundant virus of the human gut and present in a large fraction of people worldwide, was discovered this way in 2014, by cross-assembly of human faecal metagenomes, several years before its *Bacteroides* host was cultivated.

The human virome has three components:

- Bacteriophages, by far the most numerous. The large intestine contains roughly equal numbers of prokaryotic cells and virus particles, about $10^9$ of each per gram of faeces, predominantly DNA phages and predominantly temperate. They act on the human host indirectly, by moving genes — including antibiotic resistance and virulence genes — among the bacteria of the microbiota ([7.11.32](/7.11.32)), and in mucus they adhere to mucin glycans and kill incoming bacteria, a non-host-encoded layer of defence.
- Viruses of human cells, mostly persistent and mostly without symptoms: anelloviruses, acquired early in life and never associated with a disease; circoviruses; adenoviruses, polyomaviruses and papillomaviruses in the nose, mouth, skin and gut; herpesviruses, latent for life in most adults. Endogenous retroviruses, remnants of past germline infections, make up 5–8 % of the human genome and are not usually counted as part of the virome.
- Plant viruses from food, of which pepper mild mottle virus is the most consistently detected. They do not replicate in humans.

**Remark 26.7.1** The virome of a healthy person is individual and stable over years, like the bacterial microbiome, and the same caution applies to inferences from it: an association between a virus and a disease state in a cross-sectional survey is correlational. Causal claims about the virome require the evidence hierarchy applied in [7.11.32](/7.11.32).

## 26.8. Viruses of Plants and of Insects

Plant viruses matter economically — they cause losses of tens of billions of dollars a year — and are biologically distinctive because of the cell wall.

- *Entry* cannot be receptor-mediated: nothing can cross an intact wall. A plant virus enters through a wound, which is why transmission depends on a vector or on mechanical damage. Aphids, leafhoppers, whiteflies, thrips and nematodes are the common vectors; transmission is *non-persistent* (the virion is carried on the stylet and lost within minutes, as for many potyviruses), *persistent–circulative* (the virion crosses the gut to the salivary glands) or *persistent–propagative* (the virus also multiplies in the insect, so that the vector is a second host).
- *Movement* within the plant uses the plasmodesmata ([7.3.23](/7.3.23#sec-23.5)): all plant viruses encode a *movement protein* that binds the genome and modifies the plasmodesmata, raising their size exclusion limit so that a ribonucleoprotein or a whole virion can pass to the next cell. The 30 kDa movement protein of tobacco mosaic virus was the first identified. Long-distance spread follows the phloem.
- Genomes are mostly positive-strand RNA, often divided among several particles (*multipartite* genomes, for example the three RNAs of brome mosaic virus, each separately encapsidated), an arrangement almost unknown among animal viruses and tolerable only because transmission delivers many particles at once.

Insect viruses include the baculoviruses, large circular double-stranded DNA viruses of lepidopteran larvae. They are traditionally divided by the protein inclusion body that occludes the virions: in the nucleopolyhedroviruses many virions lie in one large polyhedron made in the nucleus, in the granuloviruses a single virion lies in a small granule. A third group of occluded insect viruses, the cypoviruses (family *Reoviridae*, ten segments of double-stranded RNA), multiplies in the cytoplasm of midgut cells and also forms polyhedra. In baculoviruses the virions are embedded in a crystalline matrix of the protein polyhedrin, which protects them in the environment and dissolves in the alkaline midgut of a larva that eats contaminated foliage. Polyhedrin is made in enormous amounts late in infection, and its very strong promoter, driving a foreign gene in a virus from which polyhedrin has been deleted, is the basis of the baculovirus expression system used to make recombinant proteins and virus-like particles. Baculoviruses are also used directly as biological insecticides. Some insect viruses, finally, are vectored in the opposite direction: the arboviruses of [7.11.27](/7.11.27) multiply in both an arthropod and a vertebrate.

## 26.9. Subviral Agents: Viroids and Satellites

A **viroid** ([7.3.1](/7.3.1)) is a circular single-stranded RNA of 246 to about 400 nucleotides, with no capsid and no protein-coding capacity, that replicates autonomously in plant cells. Some thirty are known, all of plants; potato spindle tuber viroid (PSTVd, 359 nt), found by Diener in 1971, is the prototype, and coconut cadang-cadang viroid (246 nt) the smallest known pathogen of any kind.

Their biology follows from what they lack. Extensive intramolecular base pairing folds the circle into a rod or a branched structure stable enough to survive outside a cell; with no capsid there is no receptor, so entry is through wounds, by contaminated machinery or by pollen and seed, and spread within the plant is through plasmodesmata and the phloem. With no protein, replication must be done entirely by host enzymes, which is possible only because plant DNA-dependent RNA polymerases will accept an RNA template. Two families differ in where and how:

| | *Pospiviroidae* (PSTVd) | *Avsunviroidae* (avocado sunblotch viroid) |
|---|---|---|
| Secondary structure | rod, with a central conserved region | rod and branched, no conserved region |
| Site of replication | nucleus | chloroplast |
| Polymerase | host RNA polymerase II | nuclear-encoded chloroplast polymerase |
| Cleavage of multimers | host RNase III | self-cleavage by a hammerhead ribozyme |
| Ligation | host DNA ligase I | chloroplast tRNA ligase |
| Sequence diversity | low | high |

![Replication and pathogenesis of a viroid. A: the rod-like secondary structure of potato spindle tuber viroid (359 nt), with the central conserved region. B: rolling-circle replication — the circular (+) RNA is copied by host RNA polymerase into a concatemeric (−) strand, which is copied again into (+) concatemers, cleaved to unit length (by host RNase III in the *Pospiviroidae*, by the viroid's own hammerhead ribozyme in the *Avsunviroidae*) and circularized by ligation. C: pathogenesis — double-stranded replication intermediates are processed by the plant RNA-silencing machinery into small interfering RNAs, which direct cleavage of host mRNAs with partial complementarity; silencing of a chloroplast chaperone mRNA by siRNAs from peach latent mosaic viroid produces the chlorotic symptoms](./plots/viroid.py)

Both families replicate by a rolling circle. How they cause disease was long obscure, since they make no protein; the answer, in the cases now understood, is RNA silencing ([7.2.18](/7.2.18)). Viroid replication intermediates are double-stranded, the plant processes them into small interfering RNAs, and those siRNAs silence host mRNAs with which they happen to be partially complementary. Small RNAs from peach latent mosaic viroid target the mRNA for a chloroplast heat-shock protein and produce the characteristic chlorosis; the Y-satellite RNA of cucumber mosaic virus silences a gene of chlorophyll biosynthesis and turns tobacco leaves bright yellow. Viroid disease is, on this view, an accident of sequence — a parasite that is nothing but a nucleic acid is recognized by the machinery that evolved to destroy parasitic nucleic acids, and the collateral damage is the symptom.

**Definition 26.9.1 (Satellite Virus)** A **satellite virus** is a subviral agent that depends on a coinfecting *helper virus* for its reproduction and whose genome has no sequence relationship to the helper's. Satellite viruses encode their own capsid protein; *satellite nucleic acids*, which do not, are packaged by a protein of the helper. Satellites typically depress the yield of the helper and may either worsen or attenuate the disease it causes.

Satellite tobacco necrosis virus, a 1260-nucleotide RNA in a $T=1$ capsid of its own making, is the classical example; its helper, tobacco necrosis virus, supplies the polymerase, and its presence reduces the helper's yield to near zero. Satellite RNAs are subviral agents of the same kind that encode no capsid protein and are packaged by the helper's coat protein. *Virusoids* are circular satellite RNAs of roughly $220$–$390$ nucleotides that are encapsidated together with the helper's own genome, as in the plant sobemoviruses; they replicate by a rolling circle and cut themselves to unit length with hammerhead ribozymes, as the viroids of the *Avsunviroidae* do. Older texts, and Chinese textbooks in particular, list satellite viruses, satellite RNAs and virusoids as three categories, which differ only in whether the satellite makes its own capsid and whether it is packaged inside the capsid of its helper.

Adeno-associated virus, a parvovirus that requires adenovirus or a herpesvirus as helper, is both a family member and a satellite in ICTV's scheme, and is the vector most used in human gene therapy.

**Example 26.9.1 (Hepatitis delta)** Hepatitis delta is a satellite of hepatitis B virus and a hybrid of the two categories above. Its genome is a 1.7 kb circular RNA — the smallest of any animal virus — that is 70 % base-paired into a viroid-like rod, is copied by host RNA polymerase II, and is cut to unit length by its own ribozyme. Unlike a viroid it encodes a protein, the delta antigen, in two forms produced by ADAR-mediated editing of the stop codon: the small form is required for RNA synthesis, the large form for assembly. It cannot make an envelope, and uses the surface protein of hepatitis B virus instead, so that infection occurs only in people infected with HBV — roughly 5 % of them — and coinfection accelerates progression to cirrhosis. ICTV places it and its newly discovered relatives in the realm *Ribozyviria*.

## 26.10. Prions

A **prion** ([7.1.6](/7.1.6#def-6.5.2)) is the opposite extreme: an infectious agent that is protein and nothing else. The diseases it causes, the *transmissible spongiform encephalopathies* (TSEs), are rare, invariably fatal neurodegenerative diseases with long incubation periods, spongiform vacuolation and neuronal loss in the brain, and — the first clue that they were not ordinary infections — no inflammatory or antibody response at all.

| Disease | Host | Route |
|---|---|---|
| Scrapie | sheep, goats | natural transmission within flocks; known for over 250 years |
| Bovine spongiform encephalopathy (BSE) | cattle | meat-and-bone meal in feed |
| Chronic wasting disease | deer, elk, moose | the only TSE in free-ranging animals; saliva and faeces |
| Kuru | humans | ritual consumption of brain tissue |
| Creutzfeldt–Jakob disease (CJD) | humans | sporadic (1–2 per million per year), familial, or iatrogenic |
| Variant CJD | humans | consumption of BSE-infected beef |
| Fatal familial insomnia, Gerstmann–Sträussler–Scheinker | humans | inherited, dominant mutations of *PRNP* |

The protein-only hypothesis, formulated by Prusiner in 1982 after the infectious fraction had been purified and found to be protein, resolves an apparent paradox: an agent with no nucleic acid can nevertheless be inherited, because the host encodes it. The gene *PRNP* encodes a glycosylphosphatidylinositol-anchored neuronal glycoprotein, $\mathrm{PrP^C}$, which is largely α-helical, soluble and completely digested by proteinase K. The pathogenic conformer $\mathrm{PrP^{Sc}}$ has the same sequence but is rich in β-sheet, insoluble, and digested only to a protease-resistant core of 27–30 kDa. $\mathrm{PrP^{Sc}}$ templates the conversion of $\mathrm{PrP^C}$ into more of itself; the converted molecules aggregate into amyloid fibrils and the neurons die.

![The prion cycle and its kinetics. A: conformational conversion — the α-helical, protease-sensitive PrP^C made by the neuron is templated by PrP^Sc into the β-sheet-rich conformer, which polymerizes into amyloid fibrils; proteinase K digests PrP^C completely but leaves the 27–30 kDa core PrP 27–30, the diagnostic signature. B: nucleated polymerization — a simulation of the same model shows the long lag before aggregate mass becomes detectable, the acceleration once fibrils fragment and seed further growth, and the abolition of the lag by adding preformed seed, which is both the mechanism of infection and the basis of the RT-QuIC and PMCA amplification assays. C: three ways to acquire a TSE — sporadic (spontaneous conversion), inherited (a destabilizing *PRNP* mutation) and acquired — converge on the same self-propagating conformer](./plots/prion.py)

Several features of the diseases follow from this mechanism.

- *Mice lacking the gene.* Mice without *Prnp* develop normally and cannot be infected: without the substrate there is no propagation. This is the decisive genetic evidence for the hypothesis.
- *A species barrier* exists because conversion is most efficient when the sequences of $\mathrm{PrP^{Sc}}$ and $\mathrm{PrP^C}$ match. Hamster prions do not propagate in mice but do in mice transgenic for the hamster gene, and the prions they produce are hamster prions. A single substitution can remove the barrier. BSE prions have an unusually broad host range, which is why they reached humans; prions of chronic wasting disease, in contrast, do not infect mice transgenic for human *PRNP*, and no human case has been attributed to them.
- *Prion strains* exist without any sequence difference. Serially passaged isolates differ reproducibly in incubation period, in the brain regions affected and in the glycosylation and electrophoretic pattern of the protease-resistant core, and they keep these properties in one inbred line of mice. The information distinguishing strains is carried by conformation — the clearest demonstration that a protein can hold heritable information.
- *Three origins.* Inherited disease arises from over 40 known dominant mutations of *PRNP*; sporadic disease, which is 85–90 % of human cases, from rare spontaneous conversion; acquired disease from ingestion or from medicine. Over 400 iatrogenic cases of CJD have been recorded, from corneal grafts, dura mater, depth electrodes and cadaveric growth hormone, and the extreme resistance of prions to the usual sterilization ([7.11.10](/7.11.10)) is the reason.
- *No treatment* is available. Quinacrine blocked prion accumulation in culture but failed in trials; antibodies and small molecules that bind PrP are in development. Diagnosis, by contrast, has improved greatly: RT-QuIC and protein misfolding cyclic amplification use the templating reaction itself, with cycles of shaking or sonication to fragment fibrils and multiply the number of seeds, and detect femtogram amounts of $\mathrm{PrP^{Sc}}$ in cerebrospinal fluid or nasal brushings.

**Example 26.10.1 (BSE and variant CJD)** The British BSE epidemic was created by recycling: ruminant carcasses were processed into meat-and-bone meal and fed back to cattle, so that a single infected animal could infect many. Cases peaked in 1992 at about 37 000 a year and collapsed after the 1988 ban on ruminant feed and the 1989 ban on specified bovine offal in human food. Variant CJD in humans followed with a lag of about seven years, peaked in 1999 and has remained rare: 229 cases worldwide as of 2011, against the hundreds of thousands of infected cattle that entered the food chain. The episode is the standard example of a feeding practice converting a sporadic animal disease into an epidemic, and of how long the latency of such an epidemic can be.

Not all prions are pathogenic. Several fungal proteins propagate as self-templating conformers without causing disease: in *Saccharomyces cerevisiae*, the nitrogen catabolite repressor Ure2p in its aggregated state [URE3] releases the genes it normally represses, so that the cell can use poor nitrogen sources, and the prion state is inherited cytoplasmically. Such prions behave as epigenetic switches that let a clone explore an alternative phenotype ([7.11.12](/7.11.12)). In mammals, the innate immune adaptor MAVS polymerizes into a prion-like filament when a cell detects viral RNA, and the polymer is the signalling-competent form — the subject of the next chapter. The conformational self-templating that makes prions infectious is, in other words, an ordinary property of some proteins ([7.1.6](/7.1.6), [7.6.16](/7.6.16)); what is unusual about $\mathrm{PrP^{Sc}}$ is that it is transmissible between organisms.

## Summary

- Viruses of all seven Baltimore classes exist, but their distribution over hosts is uneven: class I in prokaryotes, class IV in plants, all seven only in animals, and classes V and VI essentially only in animals. Genome size spans $10^2$ to $10^{6.4}$ bases, with RNA confined to the small end by the error threshold.
- Archaeal viruses are almost all dsDNA and include morphotypes — spindle, two-tailed, bottle, filamentous — found nowhere else; ATV completes its development outside any cell (Example 26.2.1).
- **Giant viruses** (Definition 26.3.1) of amoebae reach 2.5 Mb and 1.5 μm and encode translation-related genes, but are not a fourth domain; **virophages** (Definition 26.3.2) parasitize them and can protect the cellular host population.
- ICTV classification uses fifteen ranks and six realms defined by hallmark genes; morphology-based families of tailed phages were abolished in 2022 and species names are now binomial. No single phylogeny of all viruses is possible (Remark 26.4.1).
- The origins of viruses are probably multiple: conserved capsid folds argue for ancient lineages, polymerases for repeated escape from cells, and nothing now supports reduction from cells.
- Viruses are the most abundant biological entities on Earth ($\sim10^{31}$ particles), kill 5–50 % of marine bacteria a day, and drive the **viral shunt** (Definition 26.6.1); *kill the winner* (Definition 26.6.2) maintains diversity, *piggyback the winner* describes the rise of lysogeny at high host density, and auxiliary metabolic genes such as phage *psbA* support host metabolism during infection.
- The **virome** (Definition 26.7.1) is characterized by shotgun metagenomics; about three quarters of viral sequences are unknown. The human virome is dominated by temperate gut phages, with persistent anello-, papilloma-, polyoma- and herpesviruses of human cells.
- Plant viruses enter through wounds, move through plasmodesmata using a movement protein, and are mostly +ssRNA, often multipartite; baculoviruses of insects supply the polyhedrin promoter of the baculovirus expression system.
- Viroids are protein-free circular RNAs replicated by host polymerases, in the nucleus (*Pospiviroidae*) or the chloroplast with ribozyme self-cleavage (*Avsunviroidae*); they cause disease by RNA silencing of host genes. **Satellite viruses** (Definition 26.9.1) depend on an unrelated helper; hepatitis delta is a viroid–satellite hybrid that uses the HBV envelope (Example 26.9.1).
- Prions are infectious conformations of the host protein $\mathrm{PrP^C}$. The protein-only hypothesis explains the species barrier, the existence of strains without sequence differences, and the three origins — sporadic, inherited and acquired — of human TSEs (Example 26.10.1). Non-pathogenic prions act as epigenetic switches in fungi and as signalling polymers in innate immunity.

## Questions

1. Why are there no known negative-strand RNA viruses of bacteria, and no RNA virus of any host with a genome of 100 kb?

   **Answer** A negative-strand genome cannot be translated, so the particle must deliver a polymerase with the genome, and in bacteria the phage genome usually enters without its capsid proteins — the injection mechanism that works for dsDNA phages cannot deliver a nucleoprotein complex. The 100 kb limit is the error threshold of [7.11.25](/7.11.25#sec-25.2): with an unproofread RdRp at $\mu \approx 10^{-4}$ per base, $\mu L \gg 1$ and no sequence is maintained. The exception proves the rule — coronaviruses reach 30 kb only because nsp14 proofreads.

2. A seawater sample contains $10^6$ bacteria and $10^7$ virus particles per ml, and 20 % of the bacteria are lysed per day with a burst size of 50. Estimate the daily production of virus particles and the mean lifetime of a particle in the water.

   **Answer** Production is $0.2 \times 10^6 \times 50 = 10^7$ particles per ml per day. At steady state production equals loss, so the standing stock of $10^7$ particles turns over once per day: the mean lifetime of a particle is of order one day. Losses are to decay, UV damage, adsorption to particles and grazing — which is why the virosphere, though enormous, is also extremely dynamic.

3. Why did the discovery of giant viruses not establish a fourth domain of life, although their genomes are larger than those of some bacteria?

   **Answer** Genome size is not a criterion of cellularity. Giant viruses have no ribosomes, no energy metabolism and no division; they are assembled from separately synthesized parts in a viral factory. Their translation-related genes, which prompted the proposal, are a minority, are not a complete set, and phylogenies place them as host-derived acquisitions by a monophyletic viral group (*Nucleocytoviricota*) rather than as relics of a reduced cell.

4. Viroids and prions both propagate without the usual genetic machinery. Compare how each stores and copies its information, and what limits the host range of each.

   **Answer** A viroid stores information in an RNA sequence and copies it by base pairing, but borrows all the enzymes — host RNA polymerase, nuclease, ligase, or its own ribozyme for cleavage. Its host range is limited by the plant enzymes and trafficking proteins it must recruit, and by the requirement for wound entry and plasmodesmatal movement, which is why no viroid infects animals. A prion stores information in a protein conformation and copies it by templated misfolding of a protein the host already makes; its host range is limited by sequence matching between $\mathrm{PrP^{Sc}}$ and the host's $\mathrm{PrP^C}$ — the species barrier — and by the need for the host to express *PRNP* at all.

5. Kill-the-winner and piggyback-the-winner make opposite predictions for the virus-to-cell ratio as host abundance rises. How could the two be reconciled, and what measurement would distinguish them in a given habitat?

   **Answer** They describe different viral strategies rather than contradictory facts: kill the winner concerns lytic viruses, whose production tracks host abundance, while piggyback the winner concerns temperate viruses, whose decision shifts towards lysogeny when hosts are abundant and growing. In a habitat where most viruses are temperate the second dominates. The distinguishing measurements are the fraction of cells carrying inducible prophages (by mitomycin C induction or by prophage detection in single-cell genomes) and the direct estimate of lytic infection frequency (by transmission electron microscopy or by viral production assays) as functions of host density and growth rate, rather than the virus-to-cell ratio alone, which confounds production with decay.
