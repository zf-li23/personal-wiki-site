---
title: "Introduction: Questions, History and Principles of Development"
description: "What developmental biology asks and how its answers were found: the questions of differentiation, morphogenesis, growth, reproduction, renewal, regeneration, evolution and environment; the frog life cycle; preformation and epigenesis, cell theory, germ plasm, Roux and Driesch, induction, the union with genetics, developmental biology in China; seven developmental processes; fate, specification and determination with the tests that tell them apart; autonomous, conditional and syncytial specification and the mosaic–regulative debate; transdifferentiation and dedifferentiation; the four ways of making cells different; the reliability of development (redundancy, negative feedback with a dosage model, genetic compensation, canalization); birth defects; and the place of mathematical models."
---

A human being begins as one cell about a tenth of a millimetre across and ends, two decades later, as some $3.7 \times 10^{13}$ cells of several hundred kinds, arranged in organs of exact shape and size, the left leg the same length as the right. The embryo has to build itself: it must respire before it has lungs and circulate blood before its heart has chambers, and nothing outside it holds a blueprint. This chapter introduces the questions that developmental biology asks about this process, the history of how those questions were sharpened into experiments, and the vocabulary used for the rest of the course: fate, specification, determination, induction, and the reliability of development. The cell-level machinery of differentiation is in [7.3.24](/7.3.24) and the genetic method in [7.4.20](/7.4.20); here we take the view of the whole embryo. The chapter ends with the role of mathematical models, which in this course stand beside the classical experiments of mutation, grafting and removal as a second way of reasoning about development.

## 1.1. What Developmental Biology Studies

**Definition 1.1.1 (Developmental Biology)** **Developmental biology** is the science of the processes by which an organism forms and changes over its life: the formation of gametes, fertilization, embryonic development, growth, the maintenance of the adult by renewal and repair, regeneration, and aging.

The field grew out of embryology, the study of the embryo between fertilization and birth or hatching, and its foundations are genetics ([7.4](/7.4)) and cell biology ([7.3](/7.3)). Its explanations have moved from the level of organs to that of cells and molecules, but its questions remain those of the embryo. Four features distinguish an embryo from any machine and from any non-living pattern:

- it arises from a single cell that multiplies, so that every structure is built by cells that were not there before;
- it functions while it builds: a chick embryo's heart beats from the second day of incubation, while the heart is still a tube;
- it organizes itself: no external template places the organs, and the order emerges from interactions among the cells;
- what it builds becomes fixed: the adult can repair and renew, but most of its structure cannot be rebuilt.

Developmental biology has to explain how a single genotype is turned into a phenotype, and it asks a family of questions:

| Question | What has to be explained | Where in this course |
|---|---|---|
| Differentiation | why cells with the same DNA have different properties, and how this is controlled | 7.5.1–7.5.3; [7.3.24](/7.3.24) |
| Morphogenesis | how cells build structures of particular shape | 7.5.7–7.5.9 and the organ chapters |
| Growth | how the number and timing of cell divisions are controlled and coordinated, so that parts have the right proportions and the two sides match | 7.5.34 |
| Reproduction | how germ cells are set apart from the soma, how the two influence each other, and how the germ cells make the next generation | 7.5.4, 7.5.26–7.5.27 |
| Renewal | where the cells that renew adult tissues come from, and how the rate and number are controlled | 7.5.36; [7.3.24](/7.3.24) |
| Regeneration | why some organs and some animals regenerate and others do not | 7.5.35 |
| Evolution | which changes in development produce new structures and body forms, and which heritable changes are possible at all | 7.5.39 |
| Environmental integration | how development uses and withstands its surroundings (colour, sex and even form can be set by the environment) | 7.5.38 |

Two questions underlie the others: how the fertilized egg gives rise to the adult body, and how that body produces another one. Development is therefore a cycle. Every animal passes through the same stages, which the frog shows in their most accessible form: fertilization, the fusion of sperm and egg; **cleavage**, rapid divisions without growth that turn the zygote into many smaller cells (blastomeres) forming a hollow ball, the **blastula**; **gastrulation**, movements that bring cells inside and form the **germ layers**, **ectoderm** outside, **endoderm** inside and **mesoderm** between them; organogenesis, in which the germ layers interact to form organs; a larval phase and **metamorphosis** in many species; and gametogenesis, which completes the cycle. The stages from fertilization to hatching or birth together form embryogenesis. Early in development a few cells, the germ cells, are set aside to form gametes; all the others are somatic cells.

![The life cycle of a frog as the generic animal life cycle. Clockwise from the top: gametes; the zygote; an 8-cell embryo after unequal cleavage (smaller cells in the pigmented animal half, larger yolky cells in the vegetal half); the blastula in section, with the blastocoel in the animal half; the gastrula in section, with ectoderm (blue), mesoderm (red) and endoderm (yellow) and the blastopore through which cells moved in; a neurula in cross-section, with the neural tube above the notochord and the somites on either side; the swimming tadpole; and the adult after metamorphosis. The arrows name the processes between the stages](./plots/frog-life-cycle.py)

In the leopard frog *Rana pipiens*, photoperiod and temperature tell the pituitary of the female that it is spring, and its hormones mature the gametes. Fertilization is external, and the entry of the sperm sets off a rotation of the egg cortex that will fix the dorsal side of the embryo (7.5.16). During cleavage the volume of the embryo stays constant while it divides into tens of thousands of cells; gastrulation begins about $180^\circ$ from the sperm entry point at a dimple, the blastopore; the notochord then instructs the ectoderm above it to form the neural plate, which rolls into the neural tube, and the mesoderm beside it segments into somites. The tadpole that hatches feeds for itself once its yolk is used up, and months later thyroid hormone drives metamorphosis: limbs grow, the tail is resorbed, the gut shortens and the gills give way to lungs. Gametogenesis then begins again; in *Rana pipiens* the eggs take three years to mature.

## 1.2. A Short History

![Milestones in the history of developmental biology, on a time axis broken into four segments with different scales (antiquity, 1640–1800, 1800–1900, 1900–2025). Orange: the debate between preformation and epigenesis; green: cells, nuclei and inheritance; pink: experimental embryology; blue: genetics and molecular biology](./plots/history-timeline.py)

### 1.2.1. Epigenesis and Preformation

**Definition 1.2.1 (Epigenesis and Preformationism)** **Epigenesis** is the view that the structures of the embryo arise anew in each generation from relatively unstructured material. **Preformationism** (preformation) is the view that all parts of the organism exist in miniature in the egg or the sperm and only grow during development.

Aristotle, who studied chick and invertebrate embryos in the fourth century BCE, already posed the two alternatives and favoured epigenesis. He also distinguished embryos that cleave completely (holoblastic, as in frogs and mammals) from those in which only part of the egg cleaves and the rest is yolk (meroblastic, as in birds). Little changed for two thousand years. William Harvey (1651) concluded that all animals, mammals included, come from eggs (*ex ovo omnia*). The microscope revived preformation: Marcello Malpighi (1672) found that an "unincubated" chick egg already contained much structure (the eggs had in fact lain in the August sun of Bologna), and some microscopists believed they saw a preformed little human in the sperm; Nicolaas Hartsoeker's famous drawing (1694) of such a homunculus was offered as a hypothesis, not an observation. Ovists placed the miniature in the egg, spermists in the sperm. Charles Bonnet, after discovering parthenogenesis in aphids, gave the theory its strongest form: each female contains in her eggs an infinite series of preformed individuals nested one inside the other (emboîtement), which made species immutable and every generation present since creation. In this period the word "evolution" meant exactly this unrolling of preformed germs.

Preformation failed for two reasons. It could not explain why the children of two parents resemble both (hybrid tobacco plants made by Joseph Kölreuter in 1766 were intermediate between their parents), and the nesting required ever smaller individuals without limit, a problem that became fatal once the cell theory gave living things a smallest unit. Caspar Friedrich Wolff (1767) watched the chick intestine form by the folding of a flat sheet that has no counterpart in the adult, which no preformed miniature could explain. To account for how organization arises anew, Wolff had to invoke a *vis essentialis*, and Johann Blumenbach a goal-directed "formative force". The modern view combines the two old positions: the egg contains the instructions (the genome and a few localized molecules), but the structures themselves are built afresh by interactions among cells.

### 1.2.2. Cells, Nuclei and the Germ Plasm

Karl Ernst von Baer discovered the mammalian egg (1827), extended Christian Pander's three germ layers of the chick to other vertebrates, and stated in 1828 that general features of a large group appear in the embryo before special ones, and that the embryo of a higher animal resembles the embryo, not the adult, of a lower one (von Baer's laws, 7.5.39). The **cell theory** of Matthias Schleiden (1838) and Theodor Schwann (1839), completed by Rudolf Virchow's principle that every cell arises from a cell ([7.3.1](/7.3.1)), made the egg a cell and development a history of cell divisions. Oscar Hertwig (1876) saw in sea urchin eggs that fertilization is the union of one sperm nucleus with the egg nucleus, which suggested that the nucleus carries inheritance; the behaviour of chromosomes in meiosis and the rediscovery of Mendel's laws in 1900 then gave the factors of heredity a physical home ([7.4.5](/7.4.5)).

August Weismann (1883, 1892) argued that the body (soma) is built by a germ plasm transmitted through the germ line, which is set apart early and is not changed by what happens to the soma. This separation of germ line and soma, and the inference that characters acquired by the body are not inherited, is the lasting part of his theory. His mechanism of development was wrong: he proposed that the determinants of the germ plasm are divided unequally among the daughter nuclei, so that each cell receives only those for its own fate. (The word germ plasm is now used for a different thing, the specialized cytoplasm that specifies germ cells, 7.5.27.)

### 1.2.3. Mosaic and Regulative Development

**Definition 1.2.2 (Mosaic and Regulative Development)** Development is **mosaic development** when the parts of an early embryo develop according to the fates they would have had in the whole embryo, so that removing a part removes the structures it would have formed. It is **regulative development** when the embryo can compensate for the removal, addition or rearrangement of parts, so that a part forms structures it would not normally have formed and the result is a complete, often smaller, embryo.

Wilhelm Roux, the founder of experimental embryology (*Entwicklungsmechanik*), tested Weismann's hypothesis in 1888. He killed one blastomere of a 2-cell frog embryo with a hot needle and left it in place; the surviving blastomere formed a half-embryo, as if each blastomere had received determinants for one half of the body. Hans Driesch (1892) separated the two blastomeres of a sea urchin embryo by shaking them apart and obtained two complete, small pluteus larvae; isolated blastomeres of the 4-cell stage did the same. On Weismann's view this was impossible: each sea urchin blastomere must still contain everything needed for a whole embryo, and its fate must depend on its position in the whole. Driesch drew a vitalist conclusion from this "harmonious equipotential system", but the experiment itself, an isolation of parts, became the basic test of how fates are assigned.

![Two classic experiments and a reinterpretation. A: Roux (1888) killed one blastomere of a 2-cell frog embryo and left it attached; the other formed a half-embryo. B: Driesch (1892) separated the blastomeres of a 2-cell sea urchin embryo; each formed a complete, smaller larva. C: when frog blastomeres are separated rather than one being killed in place, each can form a whole small embryo, provided that the first cleavage divided the grey crescent (the future dorsal side) between them](./plots/roux-driesch.py)

Roux's result turned out to depend on his method. The dead blastomere, left in contact, acted as a barrier and probably as an abnormal neighbour; when frog blastomeres are separated completely, each can form a whole tadpole. Hans Spemann's constriction experiments on newt eggs (1901–1903) showed the condition: a hair loop tied between the first two blastomeres gave two complete embryos when the plane of constriction divided the grey crescent, but when it separated the grey crescent to one side, only that side formed a normal embryo and the other formed an unstructured "belly piece". The frog embryo is therefore not mosaic at the 2-cell stage; it contains one localized region, the future dorsal side, whose presence is needed for a whole embryo (7.5.16).

### 1.2.4. Induction

Spemann's school then showed that tissues instruct one another. In 1924 Hilde Mangold, his doctoral student, grafted the dorsal lip of the blastopore from an early gastrula of the unpigmented newt *Triturus cristatus* into the ventral side of a gastrula of the pigmented *Triturus taeniatus*. The host formed a second body axis, with a neural tube, notochord and somites; the pigment difference showed that the notochord came mostly from the graft, but most of the neural tube and somites came from host cells that would otherwise have formed belly tissue. The graft had not just developed according to its own fate: it had changed the fate of its neighbours. This is **induction**, and the dorsal lip became the **Spemann organizer** (7.5.16). Spemann received the Nobel Prize in Physiology or Medicine in 1935; Mangold had died in 1924. The design of the experiment, a graft between species that differ in a visible marker, became a model for all later work: one needs to know which cells come from the graft and which from the host before one can say which tissue instructed which. The molecular nature of the inducers took another sixty years to find, and inducers proved to be secreted proteins of a few families (7.5.3).

### 1.2.5. The Union with Genetics and Molecular Biology

Embryology and genetics separated soon after 1900: Thomas Hunt Morgan, trained as an embryologist, turned to the fly *Drosophila* to study transmission, partly because embryological questions seemed out of reach. Wilhelm Johannsen's distinction between genotype and phenotype (1909) had already put the question that connects them: how does a genotype make a phenotype? Conrad Waddington and Richard Goldschmidt asked it explicitly, but the answer needed the tools of molecular biology. The main steps were:

| Period | Advance | Consequence for development |
|---|---|---|
| 1900–1910s | Mendel's laws rediscovered; chromosome theory; genotype and phenotype | developmental genes become mappable units |
| 1940s–1960s | DNA as genetic material; the double helix; the genetic code; Briggs and King, Gurdon: nuclear transfer | differentiated nuclei keep the whole genome ([7.3.24](/7.3.24#sec-24.2)) |
| 1970s–1980s | recombinant DNA; Lewis's bithorax genes; Nüsslein-Volhard and Wieschaus's screen for embryonic patterning mutants (1980); the homeobox (1984); Sulston's complete cell lineage of *C. elegans* | genes for the body plan identified and found to be shared by flies and vertebrates |
| 1980s–1990s | transgenic and knockout mice; mouse embryonic stem cells (1981); cloning of Dolly from an adult cell (1996) | gene function testable in mammals |
| 2000s | genome sequences of many species; induced pluripotent stem cells (2006) | the differentiated state is reversible by a few transcription factors |
| 2010s | genome editing (CRISPR–Cas9, 2012); single-cell transcriptomics; lineage barcoding | any species can be manipulated; every cell type can be profiled |
| 2020s | stem-cell-based embryo models; long-term culture of mammalian embryos | development studied in synthetic systems |

Nobel Prizes mark several of these steps: 1995 (Lewis, Nüsslein-Volhard, Wieschaus) for the genetic control of early embryonic development, 2002 (Brenner, Horvitz, Sulston) for organ development and programmed cell death in *C. elegans*, 2007 (Capecchi, Evans, Smithies) for gene targeting in mice, and 2012 (Gurdon, Yamanaka) for the discovery that mature cells can be reprogrammed to pluripotency.

### 1.2.6. Developmental Biology in China

Tong Dizhou (1902–1979) founded experimental embryology in China. After a doctorate at the Free University of Brussels (1934) he set up a laboratory of experimental embryology at Shandong University, and his first paper in China (1936) described frogs with two heads obtained by experimental manipulation. From the late 1950s he and his colleagues carried out nuclear transfer in amphibians and in fish, including transfers between species, to study how nucleus and cytoplasm interact in determining the characters of the embryo. Since about 2000 the field in China has grown rapidly, supported by national programmes on development and reproduction, stem cells and birth defects, and Chinese laboratories now publish a large share of the world's papers on development. Recent contributions include work on the epigenetic reprogramming of the zygotic genome after fertilization, the derivation of haploid embryonic stem cells and their use in place of gametes, interspecies chimeric embryos, the cloning of macaques by somatic cell nuclear transfer (2018), the extended culture of monkey embryos through gastrulation, and the developmental genetics of crop traits in rice.

## 1.3. Seven Developmental Processes

Development can be decomposed into processes that occur, in different combinations, in every organ:

| Process | What happens | Example |
|---|---|---|
| Cell proliferation | early on as **cleavage**: rapid divisions without growth, so the blastomeres get smaller | the *Xenopus* egg makes about 4000 cells in its first 12 divisions without growing |
| Pattern formation | cell identities become ordered in space and time: the body axes (anterior–posterior, dorsal–ventral, left–right) are set up, and the germ layers become separate regions of the late blastula and gastrula | the vertebrate limb: humerus, then radius and ulna, then digits |
| Morphogenesis | the embryo changes shape in three dimensions, most dramatically from gastrulation on: spherical (sea urchin, frog), hemispherical (fish) or disc-shaped (bird, human) embryos become elongated bodies | folding of the neural plate into a tube |
| Cell differentiation | cells of common origin become structurally and functionally different cell types; under normal conditions this is usually irreversible | myoblasts become muscle fibres |
| Growth | after the body plan is laid down the embryo enlarges by cell division, cell enlargement, deposition of extracellular material and the formation of cavities; different parts grow at different rates, which changes proportions | the human head is half the body length at 2 months of gestation and an eighth in the adult |
| Homeostasis of tissues | adult organs are maintained by repair (wound healing), replacement (intestinal epithelium), restoration (bone remodelling) and regeneration (skin, nails, hair) | the gut lining is replaced every few days |
| Aging | function declines; different organs begin to age at different times, and different cell types have different lifespans | 7.5.37 |

## 1.4. Cell Behaviour and the Genes That Control It

Between a gene and an embryo lies the behaviour of cells. Six behaviours do the work:

- Gene activity: which genes a cell expresses, which defines its state.
- Cell signalling: the sending, receiving and interpretation of signals.
- Movement and change of shape: cells reach their positions by moving and by changing shape, and the forces they generate and their uneven distribution can themselves create structures (7.5.7–7.5.9).
- Proliferation: different rates of division in different regions change the overall form.
- Differentiation: the acquisition of a specialized function.
- Cell death: the death of particular cells at particular times shapes structures (the spaces between the digits, [7.3.25](/7.3.25)) and removes abnormal cells.

Genes control these behaviours by controlling which proteins and RNAs a cell makes. Proteins used by nearly all cells, such as histones, ribosomal proteins and the enzymes of energy metabolism, are encoded by **housekeeping genes**; tissue-specific proteins give a cell its particular activities (hemoglobin in erythrocytes, myosin, actin and tropomyosin in muscle) and include enzymes, growth factors, receptors and structural molecules; noncoding RNAs such as **microRNAs** regulate the others. A cell can control the production and activity of these products at many steps from transcription to protein modification ([7.2](/7.2)), and the next two chapters take up how differential gene expression is set up and how cells signal to each other.

## 1.5. The Progressive Restriction of Fate

### 1.5.1. Fate, Specification and Determination

Development is progressive: cells become committed to their fates step by step, long before they look different. A **fate map** (7.5.2) records what the cells of each region of an embryo at a given stage will normally become. The fate of a cell is a statement about normal development only: it can change if the conditions change. To find out how firmly a cell is committed, one has to alter its environment, and two tests distinguish two stages of commitment.

**Definition 1.5.1 (Specification)** A cell or tissue is **specified** to a fate if, isolated in a neutral environment such as a culture dish, it develops according to that fate. Its specification is still reversible: in a different environment in the embryo it can adopt another fate.

A specified cell has undergone **determination** when it develops according to its fate even after it is placed in a different region of the embryo, among cells of other fates: its developmental potential has narrowed irreversibly to one fate ([7.3.24](/7.3.24#sec-24.1)). Determination usually precedes any visible difference by a long time, so both tests measure commitment, not differentiation.

**Example 1.5.1 (The Presumptive Eye of an Amphibian Embryo)** The region of an early amphibian gastrula that will form the eye forms eye tissue when explanted into a neutral medium: it is specified. Grafted into the trunk of a neurula next to the somitic mesoderm, the same tissue forms somite tissue like its neighbours: it is not yet determined. Taken from a neurula and grafted into the same place, the eye region forms an eye-like structure: by the neurula stage it is determined.

![Testing commitment in the presumptive eye of an amphibian embryo. Top: the eye region of an early gastrula (yellow) forms eye tissue when cultured in a neutral medium (it is specified), but grafted into the trunk of a neurula it forms somite tissue like its neighbours (it is not determined). Bottom: the eye region of a neurula forms eye-like tissue even in the trunk (it is determined). The isolation test asks whether a tissue has a fate of its own; the heterotopic graft asks whether that fate can still be changed](./plots/specification-tests.py)

The potential of embryonic cells follows a few general rules:

- it narrows as development proceeds;
- at a given stage, cells in different positions have different potentials;
- within one organ primordium, different cells can have different potentials;
- small populations of multipotent cells persist from the embryo into adult organs, where they renew and repair tissues (**stem cells**, [7.3.24](/7.3.24#sec-24.6)).

### 1.5.2. Three Modes of Specification

**Definition 1.5.2 (Autonomous, Conditional and Syncytial Specification)** In **autonomous specification** a cell's fate is set by molecules it inherits from the egg cytoplasm (cytoplasmic determinants), independently of its neighbours. In **conditional specification** a cell's fate is set by its interactions with other cells, that is, by its position in the embryo. In **syncytial specification** nuclei that share one cytoplasm acquire their fates from their positions in gradients of determinants spread through that cytoplasm, before cell membranes separate them.

![The three modes of specification. A, autonomous: a cytoplasmic determinant (red dots) in one region of the egg is inherited by one blastomere, which forms muscle even when isolated, while its sister does not. B, conditional: fates depend on the distance from a signalling source; a cell grafted from the far end to a position next to the source adopts the fate of its new position. C, syncytial: in an insect blastoderm, nuclei in a common cytoplasm read their position from opposing gradients of anterior and posterior determinants; cell membranes form only later](./plots/specification-modes.py)

| | Autonomous | Conditional | Syncytial |
|---|---|---|---|
| Source of the fate | cytoplasmic determinants inherited at cleavage | signals from neighbours, position | gradients of determinants in a common cytoplasm |
| Isolated blastomere | forms the structures it would have formed in the embryo | forms more, or other, structures | (cells form only after specification) |
| Removal of cells | the embryo lacks the corresponding structures | neighbours change fate and compensate | — |
| Lineage | invariant: the same divisions give the same fates in every embryo | variable | — |
| Typical embryos | tunicates, nematodes, molluscs and annelids (spiralians) | sea urchins, vertebrates | insects (*Drosophila*) |
| Developmental pattern | mosaic | regulative | — |

Autonomous specification was first described in the tunicate *Styela partita*, whose egg contains a yellow-pigmented crescent of cytoplasm that is inherited by the blastomeres that form the tail muscle; isolated, those blastomeres still make muscle, and a protein encoded by a maternal mRNA in the crescent (Macho-1) is needed for it (7.5.6). The sea urchin is the classical regulative embryo: the fates of its early blastomeres depend on where they are, and a 4-cell blastomere can still make a whole larva. In *Drosophila*, the first thirteen nuclear divisions occur without cell division, and the nuclei, spread in a common cytoplasm, read their positions in opposing gradients of transcription factors made from localized maternal mRNAs (7.5.14). Real embryos combine these modes: even the most mosaic embryos use induction for some tissues (the tunicate notochord and nervous system, the endoderm of the nematode, 7.5.6), and the regulative vertebrate embryo has a localized dorsal determinant.

### 1.5.3. Is Development Mosaic or Regulative?

The relation between the two modes is still debated. One view, which emphasizes that every cell eventually becomes determined and that localized maternal determinants act in many embryos, holds that mosaic development is the general rule and that regulation is a capacity acquired under particular conditions, an adaptation. The evidence supports a more mixed picture:

- Mosaic and regulative describe what happens when an embryo is perturbed at a given stage, not two kinds of animal. Every embryo becomes mosaic as its cells become determined; the difference between species is how early this happens. In the sea urchin it happens at about the 16-cell stage for the micromeres; in the mouse, blastomeres can still be rearranged freely at the 8-cell stage, and a single blastomere of a 2-cell embryo can form a complete mouse.
- Strongly mosaic embryos occur in groups with small embryos of few cells and rapid, stereotyped development (nematodes, tunicates, many spiralians); in such embryos there is little room for regulation, because each cell is a large fraction of a tissue. Regulative embryos, by contrast, are found in groups as distant as cnidarians (whose dissociated embryonic cells can reaggregate and form polyps), echinoderms and vertebrates. Comparison across the animal tree therefore does not show that mosaicism is ancestral; if anything, conditional specification is the more widespread mode and extreme mosaicism a specialization of fast-developing embryos.
- The two modes are used together within one embryo, and the same molecular mechanism (a localized maternal determinant, such as the β-catenin that becomes nuclear on the vegetal or dorsal side) can act autonomously in one cell and as the source of an inductive signal for its neighbours.

What can be said is that regulation is indeed adaptive: an embryo that can repair the loss of cells survives accidents of early development, and the mammalian embryo, whose cells must first decide between embryo and placenta according to their position, depends on it.

## 1.6. Transdifferentiation, Dedifferentiation and Redifferentiation

Under normal conditions differentiation is stable, but the state of a differentiated cell can change in three ways ([7.3.24](/7.3.24#sec-24.7)):

- In **transdifferentiation** a differentiated cell becomes a cell of another type. In newts, a lens removed from the eye is regenerated from pigmented cells of the dorsal iris, which lose their pigment, divide and become lens cells (Wolffian lens regeneration); in mice, pancreatic α cells can become insulin-producing β cells after the near-total loss of β cells. The formation of blood stem cells from a specialized hemogenic endothelium in the embryo (7.5.29) is a programmed change of the same kind.
- In **dedifferentiation** a differentiated cell loses its specialized features and returns to a less specialized, proliferating state; when it then differentiates again, into its former type or another, it redifferentiates. When the heart of a zebrafish regenerates after part of the ventricle is removed, cardiomyocytes near the wound partly disassemble their contractile apparatus, re-enter the cell cycle and divide, and the new cells redifferentiate into cardiomyocytes (7.5.35).

## 1.7. How Cells Become Different: An Overview

Four mechanisms make cells different from their neighbours, and later chapters treat each in detail:

1. Asymmetric division with **cytoplasmic determinants**: a determinant localized in a mother cell is inherited by one daughter only, so the two daughters differ from birth (**asymmetric cell division**, [7.3.21](/7.3.21#sec-21.6)); the unequal early divisions of the *C. elegans* zygote, controlled by the PAR proteins, are the best-studied case (7.5.6). This mechanism underlies autonomous specification.
2. **Induction**: a cell or tissue changes the fate of another by a signal, which can be secreted (paracrine) or presented on the cell surface (juxtacrine); the responding cells must be competent (7.5.3). A fate that depends on signals from other cells is called non-autonomous, one that depends only on the cell's own constituents autonomous.
3. **Morphogen** gradients: a substance spreading from a source forms a concentration gradient, and cells adopt different fates at different concentrations, so that one signal patterns a whole field by **positional information** (7.5.11). Several morphogens acting together give neighbouring cells distinct combinations of positional values.
4. **Lateral inhibition**: within a group of equivalent cells, a cell that begins to adopt a fate inhibits its neighbours from adopting the same fate; this generates spacing patterns, such as the regular array of feather buds in the skin of a 9-day chick embryo or the selection of neural precursors (7.5.12, 7.5.19; [7.3.24](/7.3.24#sec-24.3.3)).

The environment outside the embryo can also set fates. The map butterfly *Araschnia levana* has an orange spring form and a dark summer form, depending on the day length experienced by the larva; nutrition decides whether a honeybee larva becomes a queen or a worker; and in many turtles and in crocodilians the incubation temperature of the egg decides the sex (**temperature-dependent sex determination**, 7.5.26, 7.5.38).

## 1.8. The Reliability of Development

Development is remarkably reproducible: the two wings of a bird, which develop independently, end up the same size, and a given genotype produces nearly the same organism at different temperatures and with the small fluctuations in molecule numbers that every cell experiences. A developmental program is reliable if it is not changed in essence by such fluctuations of the environment or of the concentrations of individual molecules. Several kinds of mechanism contribute.

- Redundancy: two or more routes lead to the same result, so that the loss of one is tolerated. True duplicates are rare outside multicopy genes such as those for ribosomal RNA, but apparent redundancy, in which related genes or different mechanisms can each do the job, is common (**genetic redundancy**, [7.4.20](/7.4.20)). Mice lacking the myogenic transcription factor MyoD have normal skeletal muscle and raised levels of Myf5; mice lacking Myf5 also form muscle; mice lacking both have no skeletal myoblasts at all (Rudnicki and colleagues, 1992–1993).
- Negative feedback: an end product inhibits an earlier step, so that its level returns to a set point after a disturbance.
- Insensitivity of networks: some gene networks produce the same pattern over wide ranges of their parameters. In a computer model of the *Drosophila* segment polarity network, about one in two hundred random sets of rate constants, spanning orders of magnitude, still produced the correct pattern (von Dassow and colleagues, 2000).

### 1.8.1. Negative Feedback Buffers Gene Dosage

A heterozygote for a null allele has half the gene dosage, and most genes are nevertheless haplosufficient. Negative autoregulation, in which a protein represses its own gene ([7.2.22](/7.2.22#sec-22.6)), is one way of making the steady-state level insensitive to dosage.

**Formula 1.8.1 (Dosage Sensitivity of a Negatively Autoregulated Gene)** Let a gene present in $g$ copies make a protein $X$ that represses its own promoter with Hill coefficient $n$ (**Hill equation**, [7.1.7](/7.1.7)). With $u = X/K$, where $K$ is the repression threshold, and time in units of the lifetime of $X$,

$$
\frac{\mathrm{d}u}{\mathrm{d}t} = \frac{g a}{1+u^n} - u, \qquad a = \frac{\beta}{\gamma K},
\tag{1.1}
$$
where $\beta$ is the maximal synthesis rate per gene copy and $\gamma$ the decay rate. The steady state satisfies $u^*(1+u^{*n}) = ga$, and its logarithmic sensitivity to the dosage is

$$
S = \frac{\mathrm{d}\ln u^*}{\mathrm{d}\ln g} = \frac{1}{1 + n\,\phi}, \qquad \phi = \frac{u^{*n}}{1+u^{*n}} .
\tag{1.2}
$$

**Proof** Differentiate $\ln u^* + \ln(1+u^{*n}) = \ln g + \ln a$ with respect to $\ln g$: $S\,[1 + n u^{*n}/(1+u^{*n})] = 1$. $\square$

Without feedback ($n=0$) the level is proportional to the dosage ($S=1$). With strong repression ($u^* \gg 1$, $\phi \to 1$) the sensitivity falls to $1/(1+n)$: halving the dosage then lowers the level by a factor $2^{-1/(1+n)}$ only, $0.79$ for $n=3$. The same factor reduces the spread of the protein level caused by cell-to-cell variation in synthesis rates.

**Example 1.8.1** With $a = 20$ the wild-type steady state is $u^* = 4.0$ for $n=1$, $2.6$ for $n=2$ and $1.79$ for $n=4$, with sensitivities $S = 0.56$, $0.37$ and $0.22$. In a heterozygote ($g = 1/2$) the level falls to $68\,\%$, $77\,\%$ and $86\,\%$ of the wild type, compared with $50\,\%$ without feedback. If the synthesis rate varies between cells by a log-normal factor with standard deviation $0.3$ in $\ln g$, the standard deviation of $\ln u^*$ is $0.3$ without feedback and about $0.06$ with $n = 4$.

![Negative autoregulation buffers gene dosage. A: the circuit: a protein X represses its own promoter; synthesis is proportional to the gene dosage g. B: steady-state level against dosage, both relative to the wild type, on logarithmic scales, from Eq. (1.1) with a = 20: without feedback the line has slope 1 (a heterozygote has half the protein, red dot), with feedback the slope is the sensitivity S of Eq. (1.2), 0.22 for n = 4 (blue dot: 86 % of the wild-type level). C: steady-state levels in 4000 simulated cells whose synthesis rates vary with a standard deviation of 0.3 in ln g: the distribution with feedback (n = 4, blue) is five times narrower than without (red)](./plots/feedback-dosage.py)

The price of this buffering is that the level is less responsive to deliberate regulation as well; developmental genes that must respond to graded signals often combine negative feedback on some time scales with positive feedback that locks in a decision (**bistability**, [7.3.18](/7.3.18)).

### 1.8.2. Genetic Compensation

**Definition 1.8.1 (Genetic Compensation)** *Genetic compensation* is the upregulation of other genes, often paralogues of the mutated gene, in response to a deleterious mutation, which partly or fully replaces the lost function so that the mutant phenotype is milder than the loss of the gene product itself would cause.

Genetic compensation differs from redundancy: a redundant gene works in parallel all the time, whereas a compensating gene is induced by the mutation. It came to light through a discrepancy. In zebrafish, knocking down a gene with an antisense morpholino often gives a strong phenotype that a mutant in the same gene lacks; in one survey most such phenotypes were not reproduced by mutants (Kok and colleagues, 2015). Some of the discrepancies are artefacts of morpholinos (toxicity, off-target effects; 7.5.2), but others reflect compensation. For the zebrafish *egfl7* gene, mutants had no vascular defects and upregulated related genes, whereas morphants had defects; injecting the morpholino into mutants had no further effect, which showed that the morphant phenotype was specific (Rossi and colleagues, 2015). Knockdown of *capn3a* gives a small liver, whereas mutants have a normal liver.

Two studies published in 2019 found the trigger. Mutant alleles with a premature termination codon (PTC), whose mRNAs are degraded by **nonsense-mediated decay**, induced compensation; alleles that produce no mRNA, because the promoter was deleted, did not, and the mutants showed the morphant phenotype. The degradation of the mutant mRNA is required (El-Brolosy and colleagues), and the NMD factor Upf3a together with components of COMPASS, a complex that trimethylates histone H3 on lysine 4 at active promoters, increases the transcription of related genes, favouring those with sequence similarity to the mutated gene (Ma and colleagues). The same response occurs in mouse cells.

![Genetic compensation. Top: an allele with a premature termination codon (PTC) makes an mRNA that is degraded by nonsense-mediated decay; through the NMD factor Upf3a and the COMPASS complex, histone H3K4 trimethylation and transcription of related genes increase, and a paralogue compensates. Middle: a translation-blocking morpholino removes the protein but not the mRNA, so there is no compensation and the phenotype is strong. Bottom: an allele that makes no mRNA (promoter deleted) does not trigger compensation either](./plots/genetic-compensation.py)

Genetic compensation has two consequences for experimental design (7.5.2): a normal-looking mutant does not prove that a gene is dispensable, and the absence of a morphant phenotype in mutants does not prove that the morphant phenotype is an artefact; alleles that remove the whole gene or its promoter, conditional mutants, and acute degradation of the protein can distinguish the cases.

### 1.8.3. Canalization

**Definition 1.8.2 (Canalization)** **Canalization** is the property of a developmental system to produce the same phenotype despite variation in genotype or environment, so that development follows a few well-defined paths and small perturbations are corrected.

Conrad Waddington introduced the term in 1942 and pictured development as a ball rolling down a landscape of branching valleys (**Waddington landscape**, [7.3.24](/7.3.24#sec-24.7.4)): the depth of a valley is its canalization. Canalization hides genetic variation, which can be revealed when the buffering fails. Waddington exposed *Drosophila* pupae to heat shock, which produced a few flies lacking wing crossveins; by selecting such flies for several generations he obtained a line that formed crossveinless wings without heat shock, a process he called **genetic assimilation** (7.5.39). The chaperone Hsp90, which helps many signalling proteins fold, is one molecular buffer: when its activity is reduced, *Drosophila* show a range of heritable morphological abnormalities that were present but hidden in the population (Rutherford and Lindquist, 1998).

## 1.9. Birth Defects

Abnormal development causes birth defects, which affect about $3\,\%$ of newborns as major malformations. Their causes fall into two broad classes (7.5.38):

- Genetic malformations and syndromes. Piebaldism, an autosomal dominant condition, is caused by mutations in the receptor tyrosine kinase gene *KIT* (or, more rarely, in *SNAI2*); because KIT signalling is needed for the migration and survival of melanocyte precursors from the neural crest, affected children have a white forelock and unpigmented patches of skin from birth. (Mice with severe *Kit* mutations, the *Dominant white spotting* alleles, are also anemic and sterile, because the same receptor is needed by blood stem cells and germ cells; human piebaldism is usually confined to pigmentation, and deafness with patchy depigmentation points instead to Waardenburg syndrome.)
- Disruptions caused by **teratogens**, exogenous agents such as radiation, drugs, chemicals and infections. Thalidomide, sold as a sedative in the late 1950s and early 1960s, caused about ten thousand children to be born with phocomelia (shortened or absent limbs) when their mothers took it in the fifth to eighth week of pregnancy. Alcohol causes fetal alcohol spectrum disorder, recognizable by short palpebral fissures, a smooth philtrum, a thin upper lip, a flat midface, a short upturned nose, a low nasal bridge and epicanthal folds, with damage to the brain that impairs cognition and behaviour; because the nervous system keeps developing through childhood and adolescence, young people should not drink. The Lüliang mountains of Shanxi have had one of the highest rates of **neural tube defects** in the world; the causes are multifactorial, and low maternal folate and exposure to pollutants from household coal burning have both been associated with the risk (7.5.18).

## 1.10. Mathematical Models in Developmental Biology

A mathematical model in natural science systematizes data so that a change in the experimental conditions corresponds, ideally, to a change in a few parameters of the model. In practice models are seldom built that way: they are constructed by simplifying a hypothetical mechanism, and their main use is to suggest physical, chemical and mechanical mechanisms that can then be tested by experiment. A model can borrow concepts and techniques from other disciplines (statistical mechanics, fluid dynamics, the theory of dynamical systems), which is its advantage, and its danger is that what is special about biology may be lost in a description that aims to be too universal.

The central problem for models of development is epigenesis in the sense of Definition 1.2.1: the information that the egg carries is largely present in a spatially unstructured form, in the genome, and the complex, highly reproducible spatial structure of the animal has to be generated from it. The egg is not completely unstructured (it has an animal–vegetal axis and, in many species, localized determinants), but the information in these structures is small compared with that needed to specify the adult. Choosing the level of a model is the crucial decision:

| Choice | Alternatives | Where in this course |
|---|---|---|
| Generality | one model for many species, the species entering as parameters (reasonable for early stages, which are similar across animals), or a model of one organism | blastocoel formation (7.5.5), gastrulation (7.5.9) |
| Description of form | a classification of all possible changes of form, independent of mechanism (catastrophe theory), or a mechanism | 7.5.10 |
| Determinism | a deterministic model of one embryo, or a stochastic model of an ensemble of similar embryos | stem-cell lineages (7.5.36), cell proliferation (7.5.34) |
| What is modelled | differentiation and pattern (biochemical markers of cell type), or morphogenesis (the spatial arrangement of tissues), and whether both can be treated together | 7.5.11–7.5.13 versus 7.5.7–7.5.8 |
| Unit | cells as units with properties of their own, the underlying biochemistry inside them, or a continuum description of cell populations as a quasi-fluid, with mechanical properties of cells as an intermediate link | 7.5.7–7.5.8 |

This course follows the traditional sequence of developmental stages and organizes at each stage as much of the phenomenology as a model can capture, without forcing a model where the special features of one group of organisms dominate. The resulting models fall into a few families: energy and mechanical models of cell sorting and tissue flow (7.5.5, 7.5.7–7.5.9, 7.5.33), the geometry of stability and bifurcation (7.5.10), reaction–diffusion and gradient models of pattern (7.5.11, 7.5.12, 7.5.32, 7.5.33), chemotaxis (7.5.13), oscillators and waves (7.5.23), and stochastic models of growth and lineages (7.5.31, 7.5.34, 7.5.36). Formula 1.8.1 is a first example of the reasoning: a hypothesis about a mechanism (negative feedback) is turned into an equation, and the equation makes a quantitative prediction (the sensitivity $S$) that an experiment can test by changing one parameter (the gene dosage).

Today the two styles of research are not alternatives. The classical approach, which observes what goes wrong in a mutant or after a graft, a removal or a recombination of tissues, identifies the components and the causal links; quantitative imaging of living embryos measures concentrations, forces and timing; and models ask whether the identified components, with measured parameters, are sufficient to produce the observed pattern, and which properties make it reliable. A model that reproduces a pattern only shows that a mechanism could work; the experiment it suggests decides whether it does.

## Summary

- Developmental biology (Definition 1.1.1) studies the whole life cycle, from gametes and fertilization through embryonic development, growth and renewal to regeneration and aging; its questions are differentiation, morphogenesis, growth, reproduction, renewal, regeneration, evolution and environmental integration.
- The animal life cycle: fertilization, cleavage to a blastula, gastrulation forming three germ layers, organogenesis, larva and metamorphosis, gametogenesis; germ cells are set apart from somatic cells early.
- History: preformation gave way to epigenesis (Definition 1.2.1); the cell theory made development a history of cells; Weismann separated germ line and soma; Roux's half-embryos and Driesch's whole larvae defined mosaic and regulative development (Definition 1.2.2), and Spemann's constrictions showed that frog blastomeres regulate if they share the grey crescent; Spemann and Mangold discovered induction (1924); genetics and molecular biology identified the genes (1980s on).
- Seven processes: proliferation, pattern formation, morphogenesis, differentiation, growth, homeostasis (repair, replacement, restoration, regeneration), aging. Six cell behaviours connect genes and embryo.
- Commitment is progressive: specified cells keep their fate in a neutral environment (Definition 1.5.1), determined cells keep it anywhere (Example 1.5.1). Specification is autonomous, conditional or syncytial (Definition 1.5.2); mosaic and regulative describe the stage at which determination occurs, and most embryos use both modes.

| Mechanism of difference | Signal | Typical result |
|---|---|---|
| asymmetric division | inherited cytoplasmic determinant | sister cells differ from birth |
| induction | paracrine or juxtacrine signal to competent cells | a tissue changes the fate of its neighbour |
| morphogen gradient | concentration read at thresholds | several fates in order across a field |
| lateral inhibition | mutual inhibition among equivalent cells | spaced pattern of two fates |

- Differentiated cells can transdifferentiate or dedifferentiate and redifferentiate, especially in regeneration.
- Reliability comes from redundancy, negative feedback (Formula 1.8.1: sensitivity to dosage $S = 1/(1+n\phi)$, Example 1.8.1), insensitive networks, genetic compensation triggered by mRNA decay (Definition 1.8.1) and canalization (Definition 1.8.2).
- Birth defects (about $3\,\%$ of births) have genetic causes and teratogenic causes (thalidomide, alcohol).
- Models systematize data with few parameters and suggest mechanisms; the level of the model (general or specific, form or mechanism, deterministic or stochastic, pattern or shape, cells or continuum) is the crucial choice.

## Questions

1. Why could preformationism not explain the inheritance of characters from both parents, and why did the cell theory make the doctrine of nested germs untenable?

   **Answer** If the miniature organism were contained in the egg (or the sperm) alone, offspring would resemble only the mother (or the father); but hybrids, such as Kölreuter's tobacco hybrids or children of parents of different skin colour, are intermediate, so both gametes contribute to the form. Nested germs require that each preformed individual contain the next generation in still smaller form, without limit; once the cell theory showed that organisms are made of cells of finite size, a preformed individual many generations down would have to be smaller than a single cell, which is impossible.

2. Roux obtained half-embryos, Driesch whole larvae. List the differences between the two experiments that could explain the opposite results, and describe an experiment on frog embryos that decides between "frog embryos are mosaic" and "Roux's method caused the result".

   **Answer** The species differed (frog versus sea urchin); Roux killed one blastomere and left it attached, whereas Driesch separated them, so in Roux's experiment the surviving cell was still in contact with a dead cell that could act as an abnormal neighbour or barrier, and it might "behave as if" it were part of a whole embryo. The deciding experiment separates the two blastomeres of a frog embryo completely (or removes one), and also controls the orientation of the first cleavage relative to the grey crescent. Separated blastomeres form whole small tadpoles when each received part of the grey crescent, which shows that the frog embryo regulates; that a blastomere without grey crescent forms only a belly piece shows one localized determinant (Spemann's constriction experiments gave the same result).

3. In the Spemann–Mangold experiment, why was it essential that donor and host differed in pigmentation? What would one have concluded, wrongly, if they had not?

   **Answer** The pigment difference showed which cells of the secondary axis came from the graft and which from the host. The notochord was mostly graft, but most of the neural tube and somites were host tissue that would otherwise have formed ventral tissue. Without a marker, one could have concluded that the graft simply developed according to its own fate (self-differentiation) and formed a whole second axis by itself, which would be evidence for mosaic development rather than for induction.

4. Design experiments to decide whether the cells that will form the heart in an early vertebrate embryo are (a) specified and (b) determined at a given stage. What controls are needed?

   **Answer** (a) Explant the presumptive heart region at that stage into a neutral medium that supports differentiation (a defined culture medium without inducing tissues) and test for heart markers or beating. If the explant forms heart tissue, it is specified. Controls: explants of a region not fated to form heart (which should not form heart, showing the medium is neutral) and confirmation that the explant contains no contaminating inducing tissue (endoderm is a heart inducer). (b) Graft the same region, marked (by a dye, a transgenic marker or a species difference), heterotopically into a region with a different fate, at a stage when that region can still impose its fate, and see whether the graft forms heart tissue. If it does, the region is determined; if it adopts the host fate, it is specified but not determined. Controls: homotopic grafts (to show that grafting itself does not disturb development) and grafts of non-heart tissue into the same site.

5. A blastomere of an embryo is isolated and forms only epidermis, while in the embryo it would have contributed to epidermis and neural tissue. What can you conclude about the specification of neural tissue? What further experiment would distinguish between a missing inducer and missing competence?

   **Answer** The neural part of its fate is not specified autonomously at that stage: it needs a signal from other cells (conditional specification), whereas epidermis is either autonomous or the default fate in isolation. To distinguish a missing inducer from missing competence, recombine the isolated blastomere (or its descendants) with the tissue that normally neighbours it (or expose it to a candidate inducing molecule): if it now forms neural tissue, the blastomere was competent and lacked only the inducer; if it still forms only epidermis, it either lost competence after isolation or needs other conditions. Doing the recombination at different times measures the window of competence.

6. Using Eq. (1.2), how strong must negative autoregulation be (what Hill coefficient, in the limit of strong repression) for a heterozygote to have at least 90 % of the wild-type protein level? What is the cost of such buffering?

   **Answer** In the limit $\phi \to 1$ the level in a heterozygote is $2^{-S}$ with $S = 1/(1+n)$. We need $2^{-1/(1+n)} \ge 0.9$, that is $1/(1+n) \le \ln(1/0.9)/\ln 2 = 0.152$, so $n \ge 5.6$: a Hill coefficient of about 6. For finite repression ($\phi < 1$) $n$ must be even larger. Such strong feedback requires highly cooperative repression and a promoter far stronger than needed ($a \gg 1$, most of the synthesis capacity suppressed at steady state, which costs energy), and it makes the level insensitive to other regulatory inputs as well.

7. A zebrafish morpholino against gene *X* causes heart oedema, but a mutant with a premature stop codon in the third exon develops normally. List three hypotheses, and an experiment for each.

   **Answer** (i) The morphant phenotype is an off-target or toxic effect: inject the morpholino into homozygous mutants; if the oedema still appears, it does not depend on *X*. Use a second, non-overlapping morpholino and rescue with an mRNA that the morpholino does not bind. (ii) The mutant is compensated (genetic compensation triggered by mRNA decay): measure the expression of paralogues in mutants and morphants; make an allele that produces no mRNA (promoter or whole-gene deletion) and see whether it shows the phenotype; inhibit NMD (or Upf3a) in the PTC mutant. (iii) The PTC allele is not null (it escapes NMD and makes a truncated, functional protein, or alternative splicing skips the exon): examine the mRNA and protein in the mutant, and test another allele. Maternal mRNA could also mask a zygotic mutant phenotype: make maternal–zygotic mutants.

8. Why does a heterozygote for a null allele usually have a normal phenotype, while a few genes (such as *KIT* in piebaldism) cause a dominant phenotype when one copy is lost or mutated?

   **Answer** Most genes are haplosufficient: half the gene product is enough, because the process saturates (enzymes in excess) or because feedback restores the level (Formula 1.8.1). A dominant phenotype arises when the process is sensitive to the amount of product (haploinsufficiency, for example when a signal must cross a threshold in enough cells, as for the survival and migration of melanocyte precursors that depend on KIT signalling), or when the mutant protein interferes with the normal one (a dominant-negative effect: many piebaldism mutations in the kinase domain produce KIT proteins that dimerize with and inactivate the normal receptor, which gives a more severe phenotype than deletions).

9. Give an example in which an environmental signal, not a genetic difference, determines a developmental fate, and explain how one would show that the difference is not genetic.

   **Answer** Examples: the spring and summer forms of the map butterfly *Araschnia levana*, set by day length during larval life; temperature-dependent sex determination in turtles; caste in honeybees. To show that the difference is environmental, split a clutch of genetically related individuals (siblings, or a clone) between two environments and observe that the phenotype follows the environment (summer day length gives the dark form, short days the orange form), and that offspring of the two forms, reared under the same conditions, have the same phenotype.

10. (Open question.) A model reproduces a developmental pattern exactly. What does it show, and what does it not? How would you test it?

    **Answer** It shows that the mechanism in the model is sufficient in principle to produce the pattern with those parameters, and it may show which properties of the mechanism matter (for instance that two diffusion constants must differ). It does not show that the embryo uses that mechanism: other mechanisms can produce the same pattern, and the parameters may be unrealistic. To test it, derive predictions that distinguish it from alternatives, especially responses to perturbations (changing the size of the field, the dosage of a component, the temperature, or transplanting a source), measure the parameters independently (diffusion and degradation rates, binding constants), and check that the measured values put the system in the regime where the model gives the pattern.
