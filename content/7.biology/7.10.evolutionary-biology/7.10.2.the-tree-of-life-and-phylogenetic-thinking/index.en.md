---
title: The Tree of Life and Phylogenetic Thinking
description: "Phylogeny as history and the tree as its picture; Darwin's tree and today's tree of life; reading trees (nodes, branches, roots, rotation, relationship versus similarity); taxa, monophyletic, paraphyletic and polyphyletic groups, crown and stem groups; characters, homology and homoplasy (convergence, parallelism, reversal), plesiomorphy, apomorphy and synapomorphy; a first look at parsimony; reticulation, gene trees and species trees, orthology and paralogy, phylogenies of genes, cells and languages; ancestral states, the molecular clock, mosaic evolution and adaptive radiation; classification and nomenclature, from two kingdoms to three domains."
---

When a normal copy of the *Drosophila* gene *eyeless* is expressed in the wrong place in a fly larva, an almost perfect extra compound eye grows on a wing or a leg; the same happens when the corresponding mouse gene, *Pax6*, is expressed instead, and the eye that forms is a fly's eye, not a mouse's. Almost half of 414 essential genes of yeast can be replaced by their human counterparts. Insects and mammals, yeast and humans share such machinery because they descend from common ancestors. Descent from common ancestors, the first of Darwin's two great ideas ([7.10.1](/7.10.1#sec-1.3.2)), means that all organisms are related by one genealogy, and much of evolutionary biology consists of reconstructing that genealogy and reading evolutionary history from it.

This chapter is the introduction to phylogenetic thinking for the whole course. It defines a phylogeny and the trees that depict it, explains how to read trees and which groups of organisms they define, introduces the characters and the kinds of similarity on which phylogenetic inference rests, gives a first example of inference by parsimony, discusses why the history of genes and the history of species may differ, shows what phylogenies reveal about evolutionary history, and ends with biological classification. The mathematical objects (trees as graphs, Newick notation, the number of trees) and the algorithms of inference (distance methods, Fitch parsimony, maximum likelihood, the bootstrap) were treated in bioinformatics ([7.8.6](/7.8.6)); their statistical properties are the subject of [7.10.20](/7.10.20)–[7.10.22](/7.10.22), and dating with the molecular clock of [7.10.24](/7.10.24). Here the emphasis is on the biological concepts.

## 2.1. The Tree of Life

### 2.1.1. From Darwin to Today

On the Galápagos, Darwin suspected that the different finches, mockingbirds and tortoises of the islands descended from single ancestral species. Extended logically, the idea implies that those ancestors descended from older ancestors, and so on: in 1837 Darwin sketched in a notebook a branching diagram of descent headed "I think", and in the *Origin* (1859) he inferred that "probably all the organic beings which have ever lived on this earth have descended from some one primordial form". He compared the affinities of all beings to a great tree, the twigs being living species, the dead branches extinct groups. Today the *tree of life* is the genealogy of all organisms, living and extinct, and it is inferred mostly from DNA sequences.

**Definition 2.1.1 (Phylogeny)** A **phylogeny** is the history of the events by which species or other taxa have successively arisen from common ancestors: the order and times of branching, and the changes of characters along the lineages. A phylogenetic tree is a branching diagram that depicts a phylogeny, or a hypothesis about it.

The distinction matters because the history is single and real, whereas a tree is an estimate that may be wrong and may be revised. The **phylogenetic tree** as a mathematical object, a tree in the sense of graph theory with labeled leaves and, if rooted, a direction in time, was defined in [7.8.6](/7.8.6#def-6.1.1).

### 2.1.2. Highlights of the History of Life

All known organisms descend from a single ancestral form of life, the **last universal common ancestor** (LUCA), which lived probably between about 4 and 3.7 billion years ago. The earliest cellular organisms that we know of were prokaryotes, which diverged into two great groups, the Bacteria and the Archaea. Eukaryotes arose from a symbiosis: an archaeon, related to the Asgard archaea discovered by metagenomics, and a bacterium (an alphaproteobacterium) that became the mitochondrion. The mitochondria in each human cell are therefore more closely related to free-living bacteria such as *Escherichia coli* than to the nuclei of the same cells. A lineage of eukaryotes later engulfed a cyanobacterium that became the chloroplast, and this lineage gave rise to the green algae and land plants. The once standard **three-domain system** (Bacteria, Archaea, Eukarya as three primary branches) is therefore being replaced by a tree with two primary domains, in which eukaryotes are nested within the archaea ([7.8.6](/7.8.6#sec-6.8.1), [7.10.27](/7.10.27)).

![Some major groups of organisms and their relationships (a cladogram: branch lengths are not to scale). Eukaryotes arose from a partnership between an archaeon related to the Asgard archaea and an alphaproteobacterium that became the mitochondrion (star), so the archaea are a grade (red branches) from which eukaryotes emerged. A green-algal ancestor of plants acquired a cyanobacterium that became the chloroplast (bar). Fungi and animals share an ancestor (opisthokonts), and choanoflagellates are the sister group of animals; within the vertebrates, birds are the sister group of crocodiles, primates are closest to rodents among the mammals shown, and whales to hippopotamuses](./plots/tree-of-life.py)

Phylogenies have revealed relationships that are far from obvious from appearance. Complex multicellularity evolved several times independently: in plants, brown algae, some fungi and animals. Fungi and animals stem from a common ancestor, so we are more closely related to mushrooms than to plants; the closest living relatives of animals are the single-celled choanoflagellates, which resemble the feeding cells of sponges. Some animals never had a head (jellyfishes), while echinoderms such as sea stars lost theirs when they evolved radial symmetry from bilaterally symmetrical ancestors, and are the closest relatives of the chordates among the groups shown. Birds are more closely related to crocodiles than to any other living animals; primates are more closely related to rodents than to most other mammals; and whales, which are mammals, are closest to hippopotamuses. Diversity is distributed very unevenly over the tree: there are about 33,000 species of bony fishes, about as many as all other vertebrates together, and about 350,000 described species of beetles, whereas the earliest-diverging lineage of flowering plants is a single species, *Amborella trichopoda*, which survives only in New Caledonia.

## 2.2. Reading Trees

### 2.2.1. The Parts of a Tree

The tips of a tree (terminal nodes) are the sampled taxa, usually living species; each segment is a branch or lineage; an internal node represents the splitting of an ancestral lineage into two, usually by speciation, and stands for the common ancestor of everything above it. The node at the base, the **most recent common ancestor** of all the taxa, is the root, and a rooted tree has an implicit time axis from the root to the tips. The time scale is often only relative (the order of branching); in a chronogram branch points are placed at their estimated dates, and in a phylogram branch lengths are proportional to the amount of change, such as substitutions per site ([7.8.6](/7.8.6#sec-6.1.1)).

**Definition 2.2.1 (Anagenesis and Cladogenesis)** **Anagenesis** is evolutionary change of features within a single lineage. **Cladogenesis** is the branching of a lineage into two or more descendant lineages. After cladogenesis, anagenesis in the descendant lineages makes them diverge.

A tree shows the cladogenesis as nodes and may show anagenesis as character changes mapped on branches. All the descendants of one ancestor form a **clade** (monophyletic group), so a rooted tree is a set of nested clades; two clades that are each other's closest relatives, descended from one ancestor with no other descendants, are **sister groups** ([7.8.6](/7.8.6#def-6.1.3)).

![How to read a phylogenetic tree. A: the parts of a rooted tree of human, chimpanzee and bonobo, with an extinct lineage F (x). The chimpanzee and bonobo are sister species; node D is their most recent common ancestor, node E that of the three living species, and the lineage below E leads down to the root. B: four drawings of the same tree. Rotating the branches about a node, changing the direction in which time runs or drawing the branches slanted changes nothing, because relationships are given by the order of branching, not by the left-to-right order of the tips. C: a different tree, in which 1 and 2 are sister taxa. D: relationship is not similarity. Crocodiles resemble lizards, but they share a more recent common ancestor with birds; the bird lineage has simply changed more (bars: character changes)](./plots/reading-trees.py)

### 2.2.2. Relationship Is Order of Branching

Two taxa are more closely related to each other than to a third if they share a more recent common ancestor, as two siblings are more closely related to each other than to a cousin. Two rules follow.

1. *Branches can be rotated about any node without changing the tree.* The left-to-right order of the tips carries no information; only the pattern of nesting does. A tree in which the human is drawn next to the chimpanzee does not mean that humans are closer to chimpanzees than bonobos are.
2. *Relationship is not similarity.* Crocodiles and lizards look more alike than either looks like a bird, but crocodiles share a more recent ancestor with birds: the common ancestor of all three was lizard-like, and the bird lineage underwent more change. Dolphins resemble sharks, but are mammals related to hippopotamuses; the fins are a convergent adaptation to swimming. Similarity can be used as evidence of relationship only after the right kind of similarity has been identified (Section 2.3).

A common misreading treats a tree as a ladder of progress, with "lower" organisms at the base and humans at the top. Every living species is at a tip, equally far in time from the root; a lineage that branched early, such as *Amborella*, is not an ancestor and has been evolving as long as every other.

### 2.2.3. Taxa and Groups

**Definition 2.2.2 (Taxon)** A **taxon** (plural taxa) is a named group of organisms at any level of a classification, such as the species *Macaca mulatta*, the genus *Macaca* or the family Cercopithecidae. Taxa above the species level are higher taxa.

Groups of taxa are classified by their relationship to the tree. A clade is monophyletic. A **paraphyletic group** contains a common ancestor and some, but not all, of its descendants: the traditional class Reptilia, which excludes birds although birds descend from the common ancestor of crocodiles, lizards and turtles, or "fishes", which exclude the tetrapods. A **polyphyletic group** contains taxa without their common ancestor, so that its defining feature evolved more than once: "warm-blooded animals" (birds and mammals), or the former order Falconiformes, which united falcons with hawks and eagles until DNA showed falcons to be closer to parrots and songbirds ([7.8.6](/7.8.6#def-6.1.3)).

When fossils are included, a further distinction is needed, because extinct taxa branch off below the common ancestor of the living members of a group.

**Definition 2.2.3 (Crown Group and Stem Group)** The **crown group** of a set of living taxa is their most recent common ancestor and all of its descendants, living and extinct. The **stem group** comprises the extinct taxa that are more closely related to the crown group than to its living sister group but lie outside the crown. Crown and stem together form the total group.

The crown group Aves is the last common ancestor of all living birds and its descendants; *Archaeopteryx* and the non-avian dinosaurs such as *Tyrannosaurus*, more closely related to birds than to crocodiles, are stem-group birds. A stem group is paraphyletic by construction; the distinction matters for dating, because a fossil of the stem group dates the split from the sister group, not the origin of the crown ([7.10.24](/7.10.24)), and for the origin of body plans, which were assembled piecemeal along the stem ([7.10.1](/7.10.1#sec-1.7.6), [7.10.32](/7.10.32)).

![Groups on a tree. A: on a tree of amniotes, Archosauria (crocodiles and birds, green) is monophyletic, an ancestor and all its descendants. The traditional class Reptilia (lizards and snakes, turtles, crocodiles, without birds) is paraphyletic: it omits some descendants of its common ancestor. "Warm-blooded animals" (birds and mammals) is polyphyletic: endothermy evolved twice, and the group excludes other descendants of its members' common ancestor. B: the crown group Aves (blue) is the most recent common ancestor of living birds and all its descendants; extinct relatives that branched off the lineage below it (*Archaeopteryx* and non-avian dinosaurs such as *Tyrannosaurus*) form the stem group; crown plus stem is the total group](./plots/groups.py)

### 2.2.4. Rooting

Most methods of inference give unrooted trees, which specify relationships without the direction of time ([7.8.6](/7.8.6#sec-6.1.1)). The usual way to root a tree is to include an **outgroup**, a taxon known from other evidence to lie outside the group of interest, the **ingroup**: the root is placed on the branch that joins the outgroup to the ingroup. An outgroup also tells us which character states are ancestral (Section 2.3.4). In the example of Section 2.4 the ground squirrel, a different genus, is the outgroup for three species of tree squirrels; the Galápagos finches are rooted with finches of the South American mainland.

## 2.3. Characters and Homology

### 2.3.1. Characters

**Definition 2.3.1 (Character and Character State)** A **character** is a feature of organisms that varies among taxa and can be compared among them, such as the number of toes on the hind foot; its alternative forms (five toes, three, one) are its **character states**. In a DNA alignment each aligned site is a character and the base at the site (A, C, G or T) is its state.

Before DNA sequencing, phylogenies were based on morphology, which is still the only source of data for most fossils. Sequencing provides thousands to millions of characters per genome. Whatever the data, phylogenetic inference requires that the states being compared are comparable, inherited from a common source.

### 2.3.2. Homology

**Definition 2.3.2 (Homology)** Features of different organisms are homologous, and the relation between them is **homology**, if they have been inherited, with or without modification, from a feature of their common ancestor. The definition applies to anatomical structures, developmental processes, genes and individual sites of DNA.

The forelimb bones of tetrapods are homologous ([7.10.1](/7.10.1#sec-1.7.2)); so are the middle-ear bones of mammals and certain jaw bones of their reptile-like ancestors ([7.10.32](/7.10.32)), and the wings of birds, bats and pterosaurs as forelimbs, although not as wings. A character may be homologous while a particular state is not: the toes of guinea pigs and rhinoceroses are homologous with ours, and the five-toed (pentadactyl) state of humans and crocodiles is homologous, inherited unbroken from their common ancestor; but the three-toed state of guinea pigs and rhinoceroses evolved independently from five-toed ancestors and is not.

Homology is a hypothesis, judged by several criteria. The strongest for anatomy are correspondence of position relative to other parts of the body and correspondence of structure (the same components in the same arrangement); similarity of shape or function is not a criterion (the forelimbs of a horse and an eagle). Embryology often helps: the correspondence between the hind limbs of birds and of crocodiles is clearer in embryos, before the bird's bones fuse. For sequences, homology of sites is established by an alignment that maximizes the match between sequences, with gaps for insertions and deletions ([7.8.3](/7.8.3), [7.8.5](/7.8.5)). Homologous structures usually have similar genetic and developmental bases, but sometimes the developmental basis has diverged more than the structure; conversely, structures that are not homologous as structures can be built by homologous genes (**deep homology**, [7.5.39](/7.5.39#def-39.3.1)).

### 2.3.3. Homoplasy

Similar character states in different taxa that were not inherited from a common ancestor with that state are **homoplasy**, the source of error in phylogenetic inference and also one of the most informative patterns in evolution ([7.8.6](/7.8.6#def-6.4.1)).

**Definition 2.3.3 (Convergent Evolution, Parallel Evolution, Evolutionary Reversal)** **Convergent evolution** (convergence) is the independent evolution of similar features in different lineages, usually from different ancestral structures or by different developmental routes. **Parallel evolution** (parallelism) is the independent evolution of the same character state, especially in closely related lineages, on the same genetic and developmental basis. An **evolutionary reversal** is the return of a lineage from a derived character state to an ancestral one.

The camera eyes of vertebrates and of cephalopods (squids, octopuses) are the classic case of convergence: both have a lens and a retina, but they evolved independently from eyeless ancestors, and differ in detail, the vertebrate photoreceptors pointing away from the light, with the nerve fibers crossing the retina and leaving it through a blind spot, whereas cephalopod photoreceptors point toward the light. The repeated loss of the pelvic girdle in freshwater populations of the threespine stickleback, by changes at the same gene *Pitx1* ([7.5.39](/7.5.39)), is parallel evolution. The distinction is not sharp, because the same genes often underlie similar changes even in distantly related organisms. Molecular convergence is common: cardiac glycosides, toxins made by milkweeds and by toads, inhibit the sodium–potassium pump, and resistance has evolved independently in insects that feed on milkweeds, in toads themselves, and in rodents, hedgehogs and several lineages of snakes and lizards that eat toads, by replacement of the same few amino acids of the pump, in four lineages the same glutamine-to-arginine substitution. In the Australasian monitor lizards, including the Komodo dragon, resistance was lost again and two of these positions reverted exactly to their ancestral amino acids.

Reversals include the many losses of wings in insect lineages. It was long believed that a complex character, once lost, is not regained (Dollo's law), but there are exceptions: the aquatic larval stage, ancestral in salamanders, was lost in the terrestrial plethodontid salamanders and regained in one nested lineage, the dusky salamanders *Desmognathus*; the direct-developing species still form parts of the larval skeleton inside the egg, so the developmental potential persisted.

Convergent features are often adaptations to similar ways of life, and a correlation between a convergent feature and an environmental factor across many lineages is often the first evidence of its function: long, slender bills have evolved in at least six lineages of nectar-feeding birds (hummingbirds, sunbirds and others), and long, tubular, often red flowers in many lineages of bird-pollinated plants (the **comparative method**, [7.10.3](/7.10.3)).

### 2.3.4. Ancestral and Derived States

**Definition 2.3.4 (Plesiomorphy, Apomorphy, Synapomorphy)** Relative to a given group, a **plesiomorphy** (ancestral character state) is a state inherited from the group's ancestor, and an **apomorphy** (derived character state) is a state that evolved within the group. An apomorphy shared by two or more taxa because it evolved in their common ancestor is a **synapomorphy**; a shared ancestral state is a *symplesiomorphy*, and an apomorphy found in a single taxon an *autapomorphy*.

The principle formulated by Willi Hennig is that only synapomorphies are evidence that taxa form a clade. Shared ancestral states group taxa that kept them, which can be a paraphyletic group: lizards, turtles and crocodiles share scales without feathers, but this is the ancestral amniote condition and does not make them a clade. Whether a state is ancestral or derived is decided by outgroup comparison: a state that occurs within the ingroup but not in its outgroups is probably derived. The terms are relative: hair is an apomorphy of mammals but a plesiomorphy within mammals.

## 2.4. Inferring Phylogenies: A First Look

Phylogenetic inference seeks the tree that best explains the distribution of character states among taxa. If characters change rarely, a shared derived state is probably inherited from a common ancestor, and the tree that requires the fewest changes is the best estimate. This is the logic of **maximum parsimony**, whose algorithms (Fitch, Sankoff) are given in [7.8.6](/7.8.6#sec-6.4).

**Example 2.4.1** The figure shows a short, hypothetical stretch of a hemoglobin gene in four squirrels: the ground squirrel *Spermophilus citellus*, an outgroup, and three species of *Sciurus*: the fox squirrel *S. niger*, the eastern gray squirrel *S. carolinensis* and the western gray squirrel *S. griseus*. Only sites 3 and 9 vary. With the outgroup fixed, three rooted trees of the ingroup are possible. On tree 1, which groups the two gray squirrels, the change T→A at site 3 happens once, in their common ancestor, and the change A→T at site 9 once, in the fox squirrel lineage: two changes. Trees 2 and 3 need the change at site 3 twice and the change at site 9 once: three changes. Tree 1 is the most parsimonious. The site-3 A is a synapomorphy of the gray squirrels; the site-9 T is an autapomorphy of the fox squirrel and, like every site with a single deviant taxon, says nothing about the tree.

![Inferring a phylogeny by parsimony (Example 2.4.1). A: a hypothetical stretch of a hemoglobin gene in four squirrels: the ground squirrel (outgroup) and three species of *Sciurus*; only sites 3 and 9 vary (bold; derived states colored). B: the three possible rooted trees of the ingroup. Red bars: the change T to A at site 3; blue bars: the change A to T at site 9. Tree 1 needs 2 changes, trees 2 and 3 need 3, so parsimony chooses tree 1](./plots/squirrel-parsimony.py)

The example shows both the logic and its limits. Parsimony assumes that changes are rare; when the same change is likely to happen more than once, because mutation rates are high, times are long or many lineages are sampled, the fewest-change tree can be wrong, and on trees with long branches parsimony is even statistically inconsistent (**long-branch attraction**, [7.8.6](/7.8.6#def-6.4.2)). Model-based methods, maximum likelihood and Bayesian inference, use explicit models of character change and are the standard for molecular data ([7.10.20](/7.10.20)–[7.10.22](/7.10.22)). The example also assumes that the gene's history is the species' history, which need not be true (Section 2.5). When successive branchings were so rapid that few changes accumulated between them, the data may be unable to resolve the order, and the tree is drawn with a polytomy, a node with three or more descendant branches; such a polytomy expresses ignorance (soft polytomy) rather than a real simultaneous split (hard polytomy).

## 2.5. Variations on the Phylogenetic Theme

### 2.5.1. Branches That Rejoin

The history of life is not entirely a branching tree. Some species arise from hybrids between two others (**hybrid speciation**, [7.10.12](/7.10.12)), a pattern especially common in plants: three diploid species of sunflowers, *Helianthus anomalus*, *H. paradoxus* and *H. deserticola*, each adapted to an extreme habitat (sand dunes, salt marshes, desert floor), descend from hybrids between *H. annuus* and *H. petiolaris*, and markers throughout their genomes trace back to both parents. More often, single genes cross species boundaries. **Horizontal gene transfer**, the transmission of genes between organisms other than from parent to offspring, places a few genes of an aphid among those of fungi: some aphids, almost alone among animals, synthesize carotenoid pigments, and the phylogeny of the genes for this pathway shows that their ancestor acquired them from a fungus. Among prokaryotes, transfer by plasmids and other mobile elements, transduction and uptake of free DNA is so frequent that the relationships of some bacteria look more like a network than a tree; it has spread antibiotic resistance among pathogens such as methicillin-resistant *Staphylococcus aureus* (MRSA), *Clostridioides difficile* and *E. coli* ([7.4.10](/7.4.10), [7.8.6](/7.8.6#sec-6.8.2)). When lineages merge or exchange genes, the phylogeny has a reticulate, netlike structure ([7.10.25](/7.10.25)).

### 2.5.2. Gene Trees and Species Trees

Phylogenetic methods apply to any objects that arise by descent with modification from common ancestors. Copies of a gene, within a species or across species, have a genealogy, a **gene tree**; the tree of the species from which they are sampled is the **species tree** ([7.8.6](/7.8.6#def-6.1.5)). A gene tree can differ from the species tree for three reasons: horizontal transfer or introgression, gene duplication and loss, and **incomplete lineage sorting**, the retention of ancestral polymorphism through successive speciation events, which is the subject of the coalescent theory of [7.10.7](/7.10.7) and [7.10.25](/7.10.25). The MacGillivray's warbler shows a gene tree within one species: mitochondrial haplotypes from Mexican populations are more closely related to one another than to those from the United States, indicating little exchange between the regions.

Gene duplication is one of the main ways genomes grow ([7.10.18](/7.10.18)). If a gene is duplicated into copies α and β in an ancestral species that then splits into species 1 and 2, the four genes stand in two kinds of homology. Genes whose last common ancestor is a speciation event (α1 and α2) are **orthologs**; genes whose last common ancestor is a duplication (α1 and β2, or α1 and β1) are **paralogs** ([7.1.4](/7.1.4)). Orthologs in different species are more closely related than paralogs in the same species, so the gene tree groups the genes by copy, not by species. Repeated duplication creates gene families. The human globin family includes myoglobin and the α- and β-globin subfamilies: myoglobin and hemoglobin diverged by duplication in an ancestor of the vertebrates, the α and β subfamilies by a later duplication in an ancestor of the jawed vertebrates (jawless lampreys have only a single type of hemoglobin chain), and some duplicates became nonfunctional **pseudogenes**.

![Gene trees, duplication and the molecular clock. A: a gene is duplicated (square) into copies α and β in an ancestral species; the species then splits (circles) into species 1 and 2. Genes whose last common ancestor is a speciation node are orthologs (α1 and α2; β1 and β2); genes whose last common ancestor is the duplication node are paralogs. The gene tree groups the genes by copy, not by species. B: reading a molecular clock (Formula 2.6.1). A calibration line D = 2rt, fitted to pairs of species whose divergence times are known from fossils, converts a number of differences into a time: a pair of mammals with 45 differences diverged about 74 million years ago (numbers from Futuyma and Kirkpatrick (2017), Fig. 2.17)](./plots/gene-duplication.py)

### 2.5.3. Phylogenies beyond Organisms

Cells form lineages by division, and somatic mutations inherited by daughter cells allow their phylogeny to be reconstructed: cell phylogenies trace the developmental history of organs such as the brain, and phylogenies of tumor cells show where metastases came from ([7.3.26](/7.3.26)). Viruses have phylogenies that trace the origins and spread of epidemics, as for HIV and Ebola ([7.10.1](/7.10.1), [7.8.6](/7.8.6#sec-6.8.3)). Outside biology, French, Spanish and the other Romance languages descend from Latin, an example of cultural evolution with its own descent with modification, and linguists now use phylogenetic methods borrowed from biology to reconstruct the history of language families and other cultural traits ([7.10.33](/7.10.33)).

## 2.6. What Phylogenies Tell Us

### 2.6.1. The History of Characters

Mapping character states on a phylogeny inferred from other data, and inferring the state of each ancestor, reconstructs when and on which branch characters changed. In the simplest method, the ancestors are assigned the states that require the fewest changes; model-based reconstruction is treated in [7.10.21](/7.10.21) and [7.10.26](/7.10.26).

**Example 2.6.1** Humans have a nonopposable great toe; orangutans, gorillas and chimpanzees have opposable ones. On the tree (orangutan, (gorilla, (chimpanzee, human))), with ancestors A1, A2, A3 from older to younger, assigning a nonopposable toe to A3, the common ancestor of chimpanzees and humans, requires two changes (to nonopposable in A3, back to opposable in the chimpanzee); assigning it an opposable toe requires one (to nonopposable in the human lineage). If changes are rare, the common ancestor of humans and chimpanzees had opposable great toes.

### 2.6.2. Divergence Times and the Molecular Clock

In the 1970s, comparisons of protein sequences between pairs of mammals whose divergence times were known from fossils showed that the number of differences increases roughly linearly with time. Pigs and cows, for example, belong to groups first recorded in the Eocene, about 50 Myr ago, so they diverged at least that long ago.

**Formula 2.6.1 (Molecular Clock)** If a sequence evolves at a roughly constant rate $r$ (substitutions per site per unit time) along every lineage of a clade, the expected difference between two species that diverged a time $t$ ago is
$$
D = 2rt, \qquad \hat t = \frac{D}{2r},
$$
the factor 2 because change accumulates along both lineages from the common ancestor. The rate is calibrated with fossils that date some of the splits.

With the calibration of the figure above, a pair of mammals whose genes differ at 45 sites is estimated to have diverged about 74 Myr ago, even if neither lineage has a fossil record, provided that the rate in their lineages is the same as in the calibrating ones. That proviso is the weakness: rates differ among sites and genes and among lineages, those of hominoid primates being slower than those of other mammals, partly because of differences in generation time and mutation rate, so there is no universal clock. The theory of the clock (the neutral theory: [7.4.23](/7.4.23#thm-23.7.1)) and its statistical extension to relaxed clocks and fossil calibrations are treated in [7.10.6](/7.10.6) and [7.10.24](/7.10.24).

### 2.6.3. Patterns of Evolution

Phylogenetic analyses of many groups document regularities in how characters evolve, and these patterns are themselves strong evidence for evolution ([7.10.1](/7.10.1#sec-1.7)).

*New features are modified old features.* Features almost always evolve from pre-existing features of the ancestors, not from nothing. The wings of birds, bats and pterosaurs are modified forelimbs; no vertebrate has wings sprouting from the shoulders, as angels and dragons do, because no ancestor had shoulder structures that could be modified for flight. The same holds for proteins, which acquire new functions by modification of old ones ([7.10.18](/7.10.18)).

*Characters evolve at different rates.* Some characters are conservative, retained almost unchanged in all descendants of an ancestor: humans keep the pentadactyl limb of early tetrapods, and all mammals have only the left systemic aortic arch, all amphibians and reptiles a pair. Others, such as body size, which varies at least a hundredfold within some mammalian orders, change rapidly.

**Definition 2.6.1 (Mosaic Evolution)** **Mosaic evolution** is the evolution of different characters at different rates within a lineage, so that every species is a mixture of ancestral and derived character states.

Frogs belong to a lineage that branched off before the mammalian orders diversified, but they are not "ancestral" animals: they keep five toes on the hind foot and several bones in the lower jaw, ancestral states, but have lost the teeth of the lower jaw and fused the tibia and fibula, states more derived than ours. Humans have five fingers and teeth in both jaws (ancestral) and a single bone in the lower jaw and a large brain (derived). Because of mosaic evolution, it is misleading to call one living species more "advanced" or "primitive" than another; the terms apply to character states, not to organisms.

*Evolution is often gradual.* Many differences between species are bridged by intermediate states among living relatives: the bills of sandpipers and curlews range from short to very long through intermediate forms. Many higher taxa that diverged long ago are not connected by living intermediates, but fossils document intermediates for some ([7.10.1](/7.10.1#sec-1.7.6)).

*Homoplasy is common* (Section 2.3.3), and often reflects similar adaptations in different lineages.

*Radiations are the common pattern of long-term evolution.* When branch points are dated, a phylogeny shows whether lineages arose steadily or in bursts.

**Definition 2.6.2 (Adaptive Radiation)** An *evolutionary radiation* is the divergence of many related lineages within a relatively short time. When the lineages become adapted to different ways of life, it is an **adaptive radiation**.

The Galápagos finches descend from a single ancestor that colonized the archipelago from South America and differ in bill form according to diet; the vangas of Madagascar, a single family of birds, differ even more in bill, foraging behavior, diet and habitat; the Hawaiian silversword alliance, close relatives in the sunflower family, ranges from rosette plants of bare lava to shrubs, trees, vines and mats of wet forest. The members of a radiation usually do not show a trend in any one direction; radiation rather than sustained directional trends is probably the most common pattern of long-term evolution ([7.10.31](/7.10.31), [7.10.32](/7.10.32)).

## 2.7. Classification and Nomenclature

### 2.7.1. The Linnaean System

The system of classification in use today goes back to Linnaeus, who introduced binomial nomenclature, a two-part name of genus and specific epithet (*Homo sapiens*), and a hierarchy of categories, kingdom, phylum (division in botany), class, order, family, genus and species, with intermediate categories such as superfamily and subspecies. The categories are ranks; a taxon is a particular group assigned to a rank: the rhesus macaque *Macaca mulatta* belongs to the genus *Macaca* and the family Cercopithecidae. Names are governed by codes of nomenclature (for animals, plants, prokaryotes and viruses) with rules such as these:

- The valid name of a taxon is the oldest available name (priority); no two animals, or two plants, may bear the same name.
- Each species name is tied to a type specimen (holotype), deposited in a museum or herbarium, which decides to which species the name applies when a species is later found to comprise several.
- Names of genera and species are italicized; names above the genus are capitalized but not italicized. Family names of animals end in -idae and subfamily names in -inae, formed from a type genus (Columbidae and Columbinae from *Columba*, the pigeon); family names of plants end in -aceae (Rosaceae from *Rosa*).

### 2.7.2. Phylogenetic Classification

Linnaeus intended his groups to reveal the plan of creation; since Darwin they are expected to reflect genealogy, and most systematists now hold that classifications should contain only monophyletic taxa. This has consequences for familiar groups. The traditional class Reptilia is paraphyletic; it becomes monophyletic if the birds are included in it, and modern classifications treat birds as a subgroup of reptiles and of dinosaurs. "Fishes", "invertebrates" and "protists" remain useful descriptive words but are not taxa. Polyphyletic groups such as the old Falconiformes are split once they are recognized. A rank-free system of names defined directly by clades (phylogenetic nomenclature, the PhyloCode) exists alongside the Linnaean codes; in either system, ranks have no biological meaning beyond the nesting of groups, and a family of beetles is not comparable to a family of mammals in age or diversity.

### 2.7.3. From Two Kingdoms to Three Domains

The highest level of classification has changed with knowledge of the deepest branches of the tree:

| System | Groups | Basis |
|---|---|---|
| Linnaeus (18th century) | Plantae, Animalia | mobility, nutrition |
| Haeckel (1866) | adds Protista for unicellular organisms | |
| Chatton (1920s–1930s) | prokaryotes and eukaryotes as two types of cells | presence of a nucleus |
| Whittaker (1969), five kingdoms | Monera (prokaryotes), Protista, Fungi, Plantae, Animalia | cell type, organization, mode of nutrition |
| Woese and colleagues (1977, 1990), three domains | Bacteria, Archaea, Eukarya | phylogeny of small-subunit ribosomal RNA |
| Phylogenomic trees (2010s–) | Bacteria and Archaea as primary domains; Eukarya within Archaea | phylogenies of many conserved proteins |

The five-kingdom scheme was a classification by grade: Monera and Protista are not clades. The three-domain system was the first to be based explicitly on phylogeny, and it revealed that the prokaryotes comprise two groups as distinct from each other as from eukaryotes; its replacement by a two-domain tree ([7.10.27](/7.10.27)) shows that classification follows the inferred phylogeny and changes with it.

## Summary

- A **phylogeny** is the history of descent; a phylogenetic tree is a diagram of, or hypothesis about, it (Definition 2.1.1). All known life descends from one ancestor; eukaryotes arose by symbiosis of an archaeon and an alphaproteobacterium.
- Trees are read by the order of branching (anagenesis and cladogenesis, Definition 2.2.1): branches can be rotated, relationship is recency of common ancestry, not similarity, and no living taxon is ancestral to another.

| Group | Contains | Example |
|---|---|---|
| Clade (monophyletic) | an ancestor and all its descendants | Archosauria; Reptilia including birds |
| Paraphyletic | an ancestor and some of its descendants | traditional Reptilia; "fishes" |
| Polyphyletic | taxa without their common ancestor | "warm-blooded animals" |
| Crown group (Definition 2.2.3) | the last common ancestor of living members and all descendants | crown birds |
| Stem group | extinct taxa on the lineage below the crown | *Archaeopteryx*, *Tyrannosaurus* |

- Phylogenetic evidence comes from characters and their states (Definition 2.3.1) that are homologous (Definition 2.3.2); homoplasy (convergence, parallelism and reversal, Definition 2.3.3) misleads inference but reveals adaptation. Only synapomorphies (Definition 2.3.4) are evidence of clades; polarity is set by outgroup comparison.
- Parsimony chooses the tree with fewest changes (Example 2.4.1); it fails when changes are frequent, and model-based methods are the standard.
- Trees can be reticulate (hybrid speciation, horizontal gene transfer); gene trees can differ from species trees; duplication creates paralogs, speciation orthologs. Genes, cells, viruses and languages have phylogenies.
- Phylogenies reconstruct the history of characters (Example 2.6.1) and, with a calibrated molecular clock, divergence times ($D = 2rt$, Formula 2.6.1). They document that new features are modified old ones, mosaic evolution (Definition 2.6.1), gradual change, frequent homoplasy and adaptive radiation (Definition 2.6.2).
- Classification uses Linnaean ranks and codes of nomenclature; modern classifications recognize only clades. The highest level has gone from two kingdoms to five kingdoms to three domains and, now, to a tree with eukaryotes within the archaea.

## Questions

1. Four species have the following bases at ten variable sites (among many invariant ones): species 1 `GCTGATGAGT`, species 2 `ATCAATGAGT`, species 3 `GTTGCAACGT`, species 4 `GTCAATGACA`. Which of the three unrooted trees requires the fewest changes?

   **Answer** For each tree the minimum number of changes is computed site by site (Fitch, [7.8.6](/7.8.6#sec-6.4.1)). The tree that splits $\{1,3\}$ from $\{2,4\}$ needs one change at every site, 10 in all; the trees $\{1,2\}|\{3,4\}$ and $\{1,4\}|\{2,3\}$ each need 12, because sites 3 and 4 (T/C and G/A, shared by 1 and 3 versus 2 and 4) each require two changes on them. The most parsimonious tree is $\{1,3\}|\{2,4\}$. Every site except 3 and 4 has a single deviant species and is uninformative.

2. Classify the following as monophyletic, paraphyletic or polyphyletic: (a) birds together with crocodiles; (b) all primates except humans ("apes and monkeys" in everyday usage); (c) the old grouping of vultures of the Old and New World, which were found to have acquired their similarities independently.

   **Answer** (a) Monophyletic (Archosauria among the living taxa). (b) Paraphyletic: it contains the common ancestor of primates and all its descendants except one. (c) Polyphyletic: the defining features evolved convergently, and the common ancestor of the two kinds of vultures had many other descendants not included.

3. Explain why a fossil of a stem-group bird cannot be used as a minimum age for the origin of the crown group Aves, and what it does date.

   **Answer** A stem-group fossil lies on the lineage below the most recent common ancestor of living birds (Definition 2.2.3), so the crown group may have originated after it. What the fossil shows is that the bird lineage had already separated from the crocodile lineage, its living sister group: it gives a minimum age for the split between the total groups of birds and crocodiles. Only a fossil with a synapomorphy of a subgroup of the crown (for example of the lineage of ducks and chickens) gives a minimum age for the crown.

4. Two species differ at 9% of neutral sites in a gene whose rate, calibrated with fossils in related lineages, is $r = 1.5 \times 10^{-3}$ substitutions per site per Myr. Estimate the time of divergence, and name two reasons the estimate might be wrong.

   **Answer** By Formula 2.6.1, $\hat t = D/2r = 0.09/(2 \times 1.5 \times 10^{-3}) = 30$ Myr. (a) The rate in these lineages may differ from that in the calibrating lineages, for example because of different generation times or mutation rates. (b) An observed difference of 9% underestimates the number of substitutions, because some sites changed more than once (multiple hits); a correction with a substitution model ([7.8.6](/7.8.6#sec-6.2.2)) gives a larger distance and an older date. In addition, fossil calibrations give only minimum ages, and the divergence of the genes precedes the split of the species by the time to coalescence of ancestral polymorphism ([7.10.7](/7.10.7)).

5. Why are the terms "primitive" and "advanced" applied correctly to character states but not to living species?

   **Answer** A character state is ancestral or derived relative to a particular group, by comparison with outgroups (Definition 2.3.4). A living species is a mixture of ancestral and derived states (mosaic evolution, Definition 2.6.1), and every living lineage has evolved for the same time since the root of the tree. A species that branched off early, such as *Amborella* or a frog relative to mammals, is not an ancestor and need not be less modified in all characters, so "primitive species" confuses the order of branching with the amount of change.
