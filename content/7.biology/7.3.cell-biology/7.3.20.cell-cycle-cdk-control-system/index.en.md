---
title: The Cell Cycle and the Cdk Control System
description: The eukaryotic cell cycle as a sequence of events driven by an autonomous control system; phases, G0 and special cycles; measuring and synchronizing the cycle (flow cytometry, labeled mitoses); the classic experiments (MPF, premature chromosome condensation, cdc genes, cyclin); cyclins, Cdks, CAK, Wee1, Cdc25, CKIs, phosphatases, SCF and APC/C; once-per-cycle replication; the switch into and out of M phase; and a model of the embryonic oscillator with bistability and hysteresis.
---

A cell reproduces by duplicating its contents and dividing in two, and every cell alive today descends through an unbroken series of such divisions from the first cells. The cell cycle has two jobs that must never fail: to copy each **chromosome** exactly once, and to separate the copies precisely into two daughters. This chapter is about the control system that orders these events, a network of **protein kinases**, **protein phosphatases** and **ubiquitin** ligases that is distinct from the machines it controls: the **replisome** ([7.2.7](/7.2.7)), the spindle and the **contractile ring** ([7.3.21](/7.3.21)). Its core, the **cyclin-dependent kinases** and their **cyclins**, was introduced in biochemistry ([7.1.15](/7.1.15#sec-15.6.1)); here we follow how they were discovered, how each component is regulated, how S phase is limited to one round of replication, and how positive and negative feedback turn the network into a set of irreversible switches and, in early embryos, a free-running oscillator. The next chapter describes the mechanics of division that M-Cdk sets in motion, and [7.3.22](/7.3.22) the signals and checkpoints that decide whether a cell in a tissue should divide at all. The models here use the dynamical systems of [2.4](/2.4) and anticipate the systems biology of [7.9](/7.9).

## 20.1. Cell Proliferation

### 20.1.1. The Cell Cycle and Its Phases

Single cells proliferate to make more organisms; multicellular organisms proliferate to grow, to make gametes and to replace cells that die. An adult human replaces some $3\times10^{11}$ cells a day, about four million every second, most of them blood cells and cells of the gut epithelium. Cell proliferation combines two processes that are often confused: **cell growth**, the increase of cell mass, and cell division, the splitting of one cell into two. Most proliferating cells coordinate the two so that their size stays constant ([7.3.22](/7.3.22)).

**Definition 20.1.1 (Cell Cycle and Its Phases)** The **cell cycle** is the ordered series of events by which a cell duplicates its contents and divides into two daughter cells, from the end of one division to the end of the next. In eukaryotes it is divided into four phases: **G1 phase** (gap 1), between the end of mitosis and the start of DNA replication; **S phase** (synthesis), in which the nuclear DNA is replicated; **G2 phase** (gap 2), between replication and mitosis; and **M phase**, which comprises mitosis (nuclear division) and cytokinesis (division of the cytoplasm). G1, S and G2 together form **interphase**.

M phase is short, about an hour in a mammalian cell; interphase occupies the rest. Growth continues throughout interphase, and the gap phases are more than delays: they give the cell time to grow and to check its internal state and its environment before it commits to the two irreversible events, replication and segregation. The biochemical work of the phases is distinct:

| Phase | Main events |
|---|---|
| G1 | **chromatin** decondensed; growth, synthesis of RNA and proteins; decision to enter a new cycle (Start, 20.3.7); licensing of **replication origins** |
| S | replication of the nuclear DNA; synthesis of **histones** and assembly of new **nucleosomes**; establishment of sister-chromatid cohesion; duplication of the **centrosome** begins |
| G2 | continued growth; repair of replication errors; accumulation of mitotic **cyclins**; synthesis of **tubulin** and other proteins needed for **mitosis** |
| M | chromosome condensation, spindle assembly, **nuclear envelope** breakdown (in animals), segregation, re-formation of nuclei, **cytokinesis** |

![The cell cycle and its control system. A: the four phases of a proliferating human cell with a cycle of about 24 hours (G1 about 11 h, S about 8 h, G2 about 4 h, M about 1 h), drawn clockwise from the end of mitosis. Red bars mark the three regulatory transitions of the control system: Start (the restriction point) in late G1, the G2/M transition and the metaphase-to-anaphase transition, each with the questions the cell must answer before it proceeds; cells can leave G1 for the nondividing state G0 and, if quiescent, return. B: relative activities of the cyclin–Cdk complexes and of the two forms of APC/C over one cycle, with the phases stretched to show M phase (schematic shapes, not measurements). G1-Cdk follows mitogenic signals; G1/S-Cdk peaks at Start; S-Cdk rises in S and falls in early mitosis; M-Cdk accumulates in G2 as an inactive stockpile (dotted) and is switched on abruptly at G2/M; APC/C–Cdc20, active from mitosis, destroys M-cyclin at the metaphase-to-anaphase transition, after which APC/C–Cdh1 keeps cyclins low until late G1](./plots/cycle-overview.py)

### 20.1.2. Three Kinds of Cells in the Body

Cells in an adult tissue fall into three groups with respect to the cycle:

1. Cycling cells divide continuously: stem and **progenitor cells** of the skin, gut and bone marrow ([7.3.24](/7.3.24)).
2. Quiescent cells have left the cycle but return to it when stimulated: hepatocytes after partial hepatectomy, lymphocytes after **antigen** stimulation, fibroblasts after wounding.
3. Terminally differentiated cells have lost the ability to divide permanently: most neurons, skeletal and cardiac muscle cells, red blood cells, the keratinocytes of the outer epidermis.

**Definition 20.1.2 (G0 Phase)** **G0 phase** is a nondividing state that cells enter from G1 when they withdraw from the cell cycle, in which the cell-cycle control system is partly dismantled. Quiescent cells can leave G0 and re-enter the cycle in response to signals; in terminally differentiated cells the genes for many Cdks and cyclins are permanently silenced and G0 is irreversible.

Most cells of the body are in G0. Almost all the variation in the length of the cell cycle in an adult lies in G1 and G0: the time from the start of S phase to the end of mitosis is comparatively constant, typically 12–24 hours in mammals.

### 20.1.3. How Long the Phases Last

The durations vary widely between organisms and cell types, and G1 varies most:

| Cell | Cycle time | Remarks |
|---|---|---|
| Early *Xenopus* embryo (cleavage cycles 2–12) | about 30 min | alternating S and M, no G1 or G2, no growth; 12 synchronous divisions give about 4000 cells in about 7 h |
| *Drosophila* syncytial embryo (nuclear cycles 1–13) | 8–20 min | nuclear divisions without cytokinesis ([7.3.21](/7.3.21)) |
| Budding yeast (rich medium) | about 90 min | G1 short, S about 20 min |
| Fission yeast | 2–3 h | G1 very short, G2 about 70% of the cycle |
| Human **cell line** in culture | about 24 h | G1 about 10–12 h, S about 6–10 h, G2 3–4 h, M under 1 h |
| Intestinal crypt **transit-amplifying cell** | about 12–16 h | |
| Human hepatocyte | about a year or more | mostly in G0 |

Two kinds of specialized cycle show which parts of the standard cycle are dispensable. The cleavage cycles of animal embryos lack gap phases and growth: the egg is already enormous, and the divisions only partition it, so the cells shrink with every cycle. In *Xenopus* the cycle lengthens and gap phases appear at the midblastula transition, after the twelfth cleavage, when the ratio of DNA to cytoplasm reaches a threshold (compare the **nuclear-to-cytoplasmic ratio** of [7.3.16](/7.3.16#sec-16.7.1)). In the **endocycle** (endoreplication, Definition 17.5.2), by contrast, rounds of S phase alternate with gap phases without mitosis, so the cell becomes polyploid: the salivary-gland cells of *Drosophila* larvae, with **polytene chromosomes** of about 1000 parallel copies ([7.3.17](/7.3.17)), the trophoblast giant cells of the mouse placenta, the leaf hairs (trichomes) of *Arabidopsis* (up to 32C), and many plant cells that grow large this way. Megakaryocytes and some hepatocytes become polyploid by endomitosis, an M phase without completed nuclear division or cytokinesis.

### 20.1.4. Measuring the Cycle

Cell-cycle position can be read from morphology, DNA content or phase-specific markers:

- Microscopy. Mitotic cells round up and condense their chromosomes; the fraction of cells in mitosis is the mitotic index. Antibodies against histone H3 phosphorylated on Ser10 (pH3), a mitotic mark, and against tubulin (the spindle) identify the stages by **immunofluorescence**.
- Incorporation of thymidine analogs. A brief pulse of $[^3\mathrm{H}]$thymidine (detected by **autoradiography**), bromodeoxyuridine (BrdU, detected with antibodies) or 5-ethynyl-2′-deoxyuridine (EdU, detected by click chemistry) labels the cells that are in S phase; the fraction labeled is the labeling index.
- DNA content. Cells stained with a DNA dye such as propidium iodide or Hoechst 33342 are measured one by one by **flow cytometry** ([7.3.3](/7.3.3)): G1 cells have the diploid content 2C, G2 and M cells 4C, and S-phase cells lie in between. Combined with an EdU or BrdU pulse, a two-dimensional plot separates S cells unambiguously.
- Live reporters. The Fucci system (fluorescent ubiquitination-based cell-cycle indicator) expresses fragments of two proteins destroyed at opposite times: a red-tagged fragment of Cdt1, destroyed by SCF and CRL4 ubiquitin ligases from S phase onward, and a green-tagged fragment of geminin, destroyed by APC/C from late mitosis through G1 (20.3.6). Nuclei are red in G1, yellow at G1/S and green in S, G2 and M, so the phases of single cells can be followed in a living tissue.

A proliferating population is not a uniform sample of the cycle. In a population growing exponentially with cycle time $T$, a cell that divides produces two newborn cells, so young cells outnumber old ones. If every cell had the same $T$, the density of cells of age $a$ would be

$$
n(a) = \frac{2\ln 2}{T}\,2^{-a/T}, \qquad 0 \le a < T,
$$
and the fraction of cells in a phase occupying ages $a_0$ to $a_1$ would be $2\left(2^{-a_0/T} - 2^{-a_1/T}\right)$. The mitotic index $I_{\mathrm{M}}$ and the labeling index $I_{\mathrm{S}}$ are therefore not simply $T_{\mathrm{M}}/T$ and $T_{\mathrm{S}}/T$, although for short phases at the end of the cycle the correction is small: $I_{\mathrm{M}} = 2^{T_{\mathrm{M}}/T} - 1 \approx (\ln 2)\,T_{\mathrm{M}}/T$.

**Definition 20.1.3 (Labeled Mitoses Method)** The **labeled mitoses method** (percent-labeled-mitoses method) measures the durations of the cell-cycle phases from a single pulse of a labeled DNA precursor: the fraction of mitotic cells that carry the label is followed over time. Labeled mitoses first appear after the shortest G2; the fraction rises to 50% at about $T_{\mathrm{G2}} + T_{\mathrm{M}}/2$, stays high for about $T_{\mathrm{S}}$, falls, and rises again one cycle time $T$ after the first rise, when the cells labeled in S reach their second mitosis.

![Measuring the cell cycle in a simulated asynchronous population (mean G1 = 11 h, S = 8 h, G2 = 4 h, M = 1 h; each phase of each cycle drawn from a gamma distribution with a coefficient of variation of 0.15; the population is grown for five generations before measurement). A: DNA content per cell as measured by flow cytometry, with the contributions of G1 (2C), S (between 2C and 4C, rising linearly) and G2 + M (4C) shaded and their fractions given; 4% measurement noise widens the peaks. Because young cells outnumber old ones, G1 is over-represented relative to its share of the cycle time. B: the labeled mitoses method. After a pulse of labeled thymidine at time 0, the percentage of labeled mitotic figures rises to 50% at about TG2 + TM/2, stays near 100% for about the length of S phase (TS), falls, and rises again one cycle time (TC) later; variability between cells blurs the edges and damps the second wave](./plots/cycle-measurement.py)

### 20.1.5. Synchronizing Cells

Biochemical analysis of a phase needs many cells in that phase at once.

**Definition 20.1.4 (Cell Synchronization)** **Cell synchronization** is the production of a population of cells that are at the same stage of the cell cycle, either by selecting cells of one stage or by arresting all cells at one point and then releasing them together.

Natural synchrony is found in early embryos (the first dozen cleavages of frog and sea urchin eggs), in the nuclei of syncytia (insect embryos, the plasmodium of the slime mold *Physarum*), in the blood-stage schizonts of malaria parasites, which divide in step and cause the periodic fevers of the disease, and in dormant fungal spores that germinate together when their arrest is lifted. Artificial methods either select cells of one stage or induce an arrest and release it:

| Method | Principle | Arrest point | Advantages and limitations |
|---|---|---|---|
| Mitotic shake-off | rounded mitotic cells adhere weakly and are detached by shaking | M (selection, no drug) | high synchrony, cells undamaged; low yield, since only 1–2% of an exponential culture is in mitosis at a time, so harvests must be repeated |
| Double thymidine block | excess thymidine raises dTTP, which inhibits **ribonucleotide reductase** and depletes dCTP; two blocks separated by a release longer than S collect all cells at the G1/S boundary | G1/S | high synchrony; unbalanced growth (cells keep growing during the block and become large) |
| Hydroxyurea, aphidicolin | inhibit ribonucleotide reductase or **DNA polymerase** α | early S | simple; replication stress and DNA damage |
| Colchicine, nocodazole, colcemid | depolymerize **microtubules**; the **spindle assembly checkpoint** holds the cells in mitosis ([7.3.21](/7.3.21)) | **prometaphase** | many mitotic cells, good for chromosome preparations; colchicine is poorly reversible, and long arrests damage cells |
| Cdk inhibitors | RO-3306 inhibits Cdk1 (reversible arrest in late G2); palbociclib inhibits Cdk4/6 | G2, G1 | specific and reversible |
| Serum starvation, **contact inhibition** | withdrawal of **mitogens** ([7.3.22](/7.3.22)) | G0 | no drug; not all cell types arrest, and re-entry is slow and spread out |
| Centrifugal elutriation | separates cells by size, which increases through the cycle: in a centrifugal field the sedimentation velocity of a sphere is proportional to the square of its radius (Stokes' law), balanced against a counterflow of medium | selection by size | works for any cell in suspension, without drugs; lower synchrony |

Arrest perturbs the cells (they keep growing during a block, and drugs cause DNA damage), and synchrony decays within one or two cycles because of cell-to-cell variation; live-cell reporters such as Fucci now often replace synchronization.

## 20.2. Model Systems and Classic Experiments

### 20.2.1. Yeasts, Frog Eggs and Cultured Cells

The control system was discovered by combining three experimental systems with complementary strengths:

- Yeasts for genetics. The budding yeast *Saccharomyces cerevisiae* and the fission yeast *Schizosaccharomyces pombe* can be grown as haploids, so recessive mutations show their phenotype at once. Mutations in essential cell-cycle genes are isolated as temperature-sensitive alleles: the cells grow at the permissive temperature (about 25 °C) and arrest at the restrictive temperature (about 36 °C) at the point where the gene product is needed, with a uniform terminal morphology (the bud size of budding yeast and the length of fission yeast mark the cycle stage).
- Frog eggs and their extracts for biochemistry. A *Xenopus* egg is about $1.2\,\mathrm{mm}$ across and contains the stockpiled proteins for 12 rapid cleavage cycles. Extracts made by crushing eggs in a centrifuge carry out replication, spindle assembly and cycles of Cdk activity in a test tube, and can be depleted of a protein or supplemented with a purified one; they even organize themselves into cell-like compartments that divide (Cheng and Ferrell 2019).
- *Drosophila* embryos and cultured mammalian cells for the control of division in a multicellular context, genetic screens in a metazoan and the microscopy of mitosis.

### 20.2.2. Maturation-Promoting Factor

A frog oocyte grows for months arrested in **prophase** of **meiosis** I, a G2-like state, with a huge nucleus called the germinal vesicle. The **hormone** progesterone triggers maturation: the germinal vesicle breaks down, the chromosomes condense, the oocyte completes meiosis I and arrests again in **metaphase** of meiosis II, now an egg ready for fertilization.

**Definition 20.2.1 (Maturation-Promoting Factor)** **Maturation-promoting factor** (MPF; later read as M-phase-promoting factor) is the activity in the cytoplasm of M-phase cells that induces entry into M phase when transferred to a cell in interphase or G2. Biochemically, MPF is the complex of the cyclin-dependent kinase Cdk1 with a B-type cyclin.

Masui and Markert (1971), and independently Smith and Ecker, injected cytoplasm from mature eggs into immature oocytes and found that it induced maturation without progesterone and even when protein synthesis in the recipient was blocked. Cytoplasm from the recipient could then mature a second oocyte, and so on through serial transfers, so the activity amplified itself in each recipient: a first sign of the positive feedback of 20.5.2. The same experiments revealed a second activity, cytostatic factor (CSF), that holds the mature egg in metaphase II; it is now known to be the Mos–MAP kinase pathway acting through Emi2, an inhibitor of APC/C, and it is destroyed at fertilization by a $\ce{Ca^2+}$ wave. MPF activity was later found in M-phase cells of every eukaryote tested, from yeast to mammals. Lohka, Hayes and Maller purified it from *Xenopus* eggs in 1988 as two proteins of about 32 and 45 kDa: Cdc2 (Cdk1) and cyclin B.

![Three classic experiments on the control of the cell cycle. A: maturation-promoting factor. Cytoplasm from a mature *Xenopus* egg arrested in metaphase of meiosis II, injected into an immature oocyte arrested in G2 of meiosis I with an intact germinal vesicle, causes germinal vesicle breakdown, chromosome condensation and spindle assembly without progesterone; cytoplasm from the newly matured oocyte matures a further oocyte (serial transfer), so the activity amplifies itself. B: premature chromosome condensation. When a mitotic HeLa cell is fused with an interphase cell, the interphase nucleus condenses its chromatin at once: a G1 nucleus forms long single chromatids, an S-phase nucleus fragmented, "pulverized" chromatin, and a G2 nucleus double chromatids. C: fission yeast cell-division-cycle mutants drawn to scale (scale bar 10 µm). Wild-type cells divide at about 14 µm; temperature-sensitive cdc2 or cdc25 mutants at the restrictive temperature arrest in G2 and keep growing into long cells; wee1 mutants divide at about half the normal length; cells lacking both wee1 and cdc25 are viable and divide at a nearly normal size](./plots/classic-experiments.py)

### 20.2.3. Premature Chromosome Condensation

Cell fusion gave the same answer in mammalian cells. Johnson and Rao (1970) fused HeLa cells synchronized at different stages with inactivated Sendai **virus**, which merges the plasma membranes of adjacent cells into a binucleate **heterokaryon**.

**Definition 20.2.2 (Premature Chromosome Condensation)** **Premature chromosome condensation** (PCC) is the condensation of the chromatin of an interphase nucleus into chromosome-like structures, induced by fusing the interphase cell with a cell in M phase. The morphology of the prematurely condensed chromosomes reveals the stage of the interphase nucleus: single chromatids in G1, fragmented chromatin in S and pairs of chromatids in G2.

A mitotic cell is therefore dominant over an interphase cell: its cytoplasm contains a diffusible factor that forces any nucleus into mitosis, whatever its state. The related fusions of interphase cells (Rao and Johnson 1970) showed that the cytoplasm of an S-phase cell drives a G1 nucleus into replication, but not a G2 nucleus, which has already replicated: the first evidence of the once-per-cycle rule of 20.4. PCC is still used to visualize chromosome damage in interphase cells after irradiation.

### 20.2.4. Cell-Division-Cycle Genes

**Definition 20.2.3 (Cell-Division-Cycle Gene)** A **cell-division-cycle gene** (*cdc* gene; *CDC* in budding yeast) is a gene required for a specific step of the cell cycle, identified originally by conditional mutations that arrest yeast cells at that step with a uniform terminal phenotype.

From 1970 Leland Hartwell isolated dozens of temperature-sensitive *cdc* mutants of budding yeast. By placing their arrest points in order (a double mutant arrests at the earlier of the two points), he showed that the cell cycle is a dependent pathway of events, and found that *CDC28* is required at a point in late G1 that he called Start, after which a cell is committed to the cycle. From the sensitivity of mutants to radiation he also proposed (with Weinert, 1989) the idea of checkpoints: controls that make the start of an event depend on the completion of an earlier one, such as the *RAD9*-dependent arrest of cells with damaged DNA in G2.

In fission yeast Paul Nurse and colleagues found *cdc2*, required both for Start and for entry into mitosis, and two genes that set the size at which cells divide (Figure in 20.2.2):

- loss-of-function mutations in *cdc2* or *cdc25* arrest cells in G2; they keep growing into elongated cells;
- loss of *wee1* (and the dominant *cdc2-1w* allele) makes cells enter mitosis early, at about half the normal size ("wee" is Scots for small);
- the double mutant *wee1 cdc25* is viable and divides at a nearly normal size.

These phenotypes place Wee1 as an inhibitor and Cdc25 as an activator of Cdc2, acting in opposite directions on the same target (20.3.3). Fission yeast *cdc2* and budding yeast *CDC28* encode the same 34 kDa **protein kinase**; in 1987 Lee and Nurse cloned the human homolog by its ability to rescue a fission yeast *cdc2* mutant, which showed that the control system is conserved across a billion years of evolution.

### 20.2.5. Cyclins and the Unification

In 1982 Tim Hunt, studying protein synthesis in fertilized sea urchin eggs, noticed a protein that accumulated during each interphase and was abruptly destroyed at each division (Evans et al. 1983). He named it cyclin; similar proteins were found in clams, frogs and yeast, and cyclin **mRNA** alone induced maturation when injected into frog oocytes. By 1988–1990 the three lines converged: MPF contains Cdc2 and cyclin B, so the factor of the frog eggs, the gene of the yeasts and the oscillating protein of the sea urchins are parts of one enzyme. Murray and Kirschner (1989) showed that cyclin synthesis is the only protein synthesis required to drive cycles in egg extracts, and that a cyclin lacking its destruction signal arrests extracts in mitosis. Hartwell, Hunt and Nurse shared the 2001 Nobel Prize in Physiology or Medicine.

## 20.3. The Components of the Control System

### 20.3.1. What the Control System Must Do

**Definition 20.3.1 (Cell-Cycle Control System)** The **cell-cycle control system** is the network of regulatory proteins, centered on cyclin–Cdk complexes, their regulators and ubiquitin ligases, that triggers the events of the cell cycle in the correct order and at the correct time, and that halts the cycle at defined transitions when conditions inside or outside the cell are not suitable.

A useful view is a timer with a set of switches. The control system must (i) start each event at the right time and give it enough time to finish; (ii) start the events in the right order; (iii) start each event only once per cycle; (iv) switch each transition on completely and irreversibly, since a half-condensed chromosome or a half-broken nuclear envelope would be a disaster; (v) be robust, with backup mechanisms; and (vi) be adaptable to different cell types and conditions. It acts at three transitions (figure in 20.1.1): Start (late G1), where the cell commits to replication; the G2/M transition, where it triggers the early events of mitosis; and the metaphase-to-anaphase transition, where it triggers sister-chromatid separation and the completion of division. Each transition is blocked if a problem is detected: the environment is unfavorable or the cell too small (Start), DNA is unreplicated or damaged (G2/M), or a chromosome is not attached to the spindle (metaphase to **anaphase**). In the early embryonic cycles the control system runs without these brakes, so it is an autonomous device distinct from the processes it controls: an egg extract keeps cycling when replication is blocked.

### 20.3.2. Cyclins and Cdks

The **cyclin-dependent kinases** ([Definition 15.6.1](/7.1.15#def-15.6.1)) are Ser/Thr kinases that are inactive without a cyclin partner. Cdk levels are constant and exceed those of the cyclins; cyclin levels rise and fall, so cyclin–Cdk complexes form and act at specific stages. Cyclins are classified by the stage at which they act:

| Complex | Function | Vertebrates: cyclin, Cdk | Budding yeast | Fission yeast |
|---|---|---|---|---|
| G1-Cdk | responds to growth signals, prepares Start | cyclins D1, D2, D3 with Cdk4, Cdk6 | Cln3 with Cdk1 (Cdc28) | Puc1 (minor) with Cdk1 (Cdc2) |
| G1/S-Cdk | triggers Start, centrosome duplication; falls in S | cyclin E with Cdk2 | Cln1, Cln2 with Cdk1 | Cig2 with Cdk1 |
| S-Cdk | fires replication origins, prevents re-replication; persists to early M | cyclin A with Cdk2 and Cdk1 | Clb5, Clb6 with Cdk1 | Cig2, Cig1 with Cdk1 |
| M-Cdk | triggers mitosis; destroyed at anaphase | cyclin B with Cdk1 | Clb1–4 with Cdk1 | Cdc13 with Cdk1 |

Cdks share a conserved fold with the other protein kinases and carry, in their αC helix, the PSTAIRE motif (**residues** 45–51 of Cdk1) that contacts the cyclin; binding of the cyclin swings this helix into the active position. Cyclins are defined by the cyclin box, a domain of about 100 residues that binds the Cdk, present twice in tandem as two five-helix cyclin folds. The human genome encodes about 20 Cdks and about 30 cyclins, but only the four classes in the table drive the cycle. Yeasts use a single Cdk that changes partners; vertebrates have several, and further Cdks (Cdk7 in CAK and in TFIIH, Cdk8 and Cdk9 in transcription, [7.2.13](/7.2.13)) do not drive the cycle. Mouse genetics showed how redundant the vertebrate set is: embryos lacking all the interphase Cdks (Cdk2, Cdk3, Cdk4 and Cdk6) develop to mid-gestation with Cdk1 binding all cyclins, whereas embryos lacking Cdk1 arrest at the earliest cleavage divisions (Santamaría et al. 2007).

How can a single kinase, Cdk1, trigger S-phase events first and mitotic events later? Two mechanisms work together. First, cyclins direct the kinase to substrates: cyclins A and E bind RxL motifs in substrates through a hydrophobic patch, and cyclins of different stages prefer different docking motifs, so each complex phosphorylates its own targets well and others poorly. Second, substrates differ in the level of Cdk activity they require.

**Remark 20.3.1** Coudreuse and Nurse (2010) replaced all the cyclins and Cdks of fission yeast that drive the cycle with a single fusion protein of Cdc13 (cyclin B) and Cdc2. The cells cycled almost normally: a low level of the activity triggered S phase and a high level triggered mitosis. This supports the quantitative model of Cdk control (Stern and Nurse 1996), in which the order of events follows from rising thresholds of a single activity, with the multiplicity of cyclins adding specificity and robustness rather than being logically required.

### 20.3.3. Phosphorylation of the Cdk Subunit

Cyclin binding alone only partly activates the kinase (the T loop moves out of the substrate site). Full activity needs a phosphate on the T loop, and inhibitory phosphates near the ATP site override it.

**Definition 20.3.2 (Cdk-Activating Kinase)** **Cdk-activating kinase** (CAK) is the protein kinase that phosphorylates the threonine in the T loop of Cdks (Thr161 of human Cdk1, Thr160 of Cdk2), which is required for full activity of cyclin–Cdk complexes. In animals CAK is itself a cyclin–Cdk complex, cyclin H–Cdk7 with the assembly factor MAT1; in budding yeast it is the monomeric kinase Cak1. Its activity is constant through the cycle.

**Definition 20.3.3 (Wee1 and Cdc25)** **Wee1** is a nuclear protein kinase that phosphorylates Cdk1 (and Cdk2) on Tyr15 in the glycine-rich loop of the ATP-binding site, which inhibits the kinase even when it is bound to cyclin and phosphorylated by CAK; the related membrane-associated kinase Myt1 phosphorylates Thr14 and Tyr15. **Cdc25** is a dual-specificity protein phosphatase that removes these inhibitory phosphates and activates the Cdk; mammals have three, Cdc25A (mainly G1/S and S), Cdc25B and Cdc25C (G2/M).

Inhibitory phosphorylation is the main control of Cdk1 at the G2/M transition: cyclin B–Cdk1 complexes accumulate in G2 in the Thr14/Tyr15-phosphorylated form and are activated all at once by Cdc25 (20.5). A Cdk1 mutant that cannot be phosphorylated (T14A Y15F, "Cdk1AF") drives premature mitosis.

### 20.3.4. Cdk Inhibitor Proteins

**Definition 20.3.4 (Cdk Inhibitor Protein)** A **Cdk inhibitor protein** (CKI) is a small protein that binds cyclin–Cdk complexes or Cdk subunits and inhibits their kinase activity. Animal CKIs form two families: the INK4 proteins (p16INK4a, p15INK4b, p18 and p19), which bind Cdk4 and Cdk6 and prevent their association with D cyclins; and the Cip/Kip proteins (p21Cip1, p27Kip1 and p57Kip2), which bind cyclin E–Cdk2 and cyclin A–Cdk2, insert into the ATP site and block it. Budding yeast has Sic1 and fission yeast Rum1, which inhibit the B-type cyclin–Cdk complexes in G1.

CKIs carry information into the control system. p27 accumulates when mitogens are absent or cells touch each other and holds cells in G1; p21 is induced by p53 after DNA damage; p16 accumulates in senescent cells and is inactivated in many cancers ([7.3.22](/7.3.22), [7.3.26](/7.3.26)). p21 also binds PCNA, the sliding clamp of DNA polymerase δ, through a C-terminal PCNA-interacting motif, and so blocks DNA synthesis at replication forks directly while still allowing repair synthesis. The Cip/Kip proteins also have a paradoxical role: they promote the assembly of cyclin D–Cdk4 complexes and, when tyrosine-phosphorylated, can remain bound without inhibiting them. CKIs are removed by ubiquitin-mediated destruction: p27 and Sic1 are phosphorylated by Cdks and then recognized by SCF.

![How Cdk activity is controlled. A: states of a Cdk subunit. Free Cdk is inactive because its T loop (red) blocks the substrate site. Cyclin binding moves the T loop and gives partial activity; phosphorylation of the T-loop threonine (Thr161 in Cdk1) by CAK gives full activity. Phosphorylation of Thr14 and Tyr15 by Wee1 and Myt1 inactivates the complex even with the activating phosphate present, and Cdc25 removes these phosphates. A CKI such as p27 wraps around the cyclin–Cdk complex and blocks its active site; after phosphorylation the CKI is destroyed by SCF. B: the circuit that controls entry into and exit from M phase, in SBGN activity-flow notation (open arrows activate, bars inhibit). M-Cdk activates its activator Cdc25 (directly and through Plk1) and inhibits its inhibitors Wee1 and Myt1; through Greatwall and its substrates ENSA and ARPP19 it inhibits PP2A-B55, the phosphatase that opposes Cdk on its substrates and on Cdc25 and Wee1, and PP2A-B55 in turn inhibits Greatwall. With a delay M-Cdk activates APC/C–Cdc20, which destroys cyclin B; checkpoints inhibit Cdc25 (Chk1, Chk2 after DNA damage) or APC/C–Cdc20 (the spindle assembly checkpoint)](./plots/cdk-control.py)

### 20.3.5. Phosphatases Oppose the Cdks

The phosphorylation state of a Cdk substrate is set by a balance, like the level of water in a sink fed by a tap (the kinase) and drained by a plug hole (the phosphatase); the fastest way to fill the sink is to turn on the tap and plug the drain at the same time. Phosphatases that dephosphorylate Cdk substrates therefore belong to the control system:

- PP2A-B55, a trimer of the catalytic C subunit, the scaffold A subunit and the regulatory B55 subunit, is the main antagonist of Cdk1 in animal cells. It is high in interphase, inhibited in mitosis by the Greatwall pathway (20.5.2) and reactivated at mitotic exit.
- PP2A-B56 acts locally at centromeres and kinetochores, where shugoshin recruits it to protect cohesin ([7.3.21](/7.3.21)).
- PP1 is inhibited by Cdk1 phosphorylation in mitosis and reactivates after cyclin destruction; at kinetochores it opposes Aurora B.
- In budding yeast the phosphatase Cdc14, sequestered in the nucleolus for most of the cycle and released in anaphase, dephosphorylates Cdk substrates, activates Cdh1 and induces Sic1, driving mitotic exit.

### 20.3.6. Ubiquitin Ligases: SCF and APC/C

Cdk activity rises by synthesis and activation of cyclins, but falls mainly by their destruction through the **ubiquitin–proteasome system** ([Definition 20.7.1](/7.2.20#def-20.7.1)). Two ubiquitin ligases of the cullin–RING class control the cycle.

**Definition 20.3.5 (SCF Complex)** The **SCF complex** is a ubiquitin ligase made of Skp1, the cullin Cul1, the RING protein Rbx1 and one of many interchangeable F-box proteins that bind the substrates. Its activity is constant through the cell cycle; it ubiquitylates proteins only after they have been phosphorylated, because F-box proteins recognize phosphorylated degrons.

SCF couples destruction to the kinase activity that marks the substrate. SCF with the F-box protein Skp2 destroys p27 (phosphorylated by cyclin E–Cdk2) in late G1 and S; SCF–Fbw7 destroys cyclin E after its autophosphorylation, ending G1/S-Cdk activity; SCF–βTrCP destroys Wee1, Emi1 and Cdc25A after their phosphorylation by Plk1 or checkpoint kinases.

**Definition 20.3.6 (Anaphase-Promoting Complex)** The **anaphase-promoting complex** or cyclosome (APC/C) is a ubiquitin ligase of about $1.2\,\mathrm{MDa}$, built from 14 different proteins including a cullin-like subunit (Apc2) and a RING subunit (Apc11), that ubiquitylates securin and the S- and M-phase cyclins, triggering sister-chromatid separation and exit from mitosis. It is active only when bound to one of two coactivators: Cdc20, which acts from mitosis to the end of anaphase, and Cdh1 (Fzr1), which acts from late anaphase to late G1. The coactivators recognize degrons in the substrates, the destruction box (D box, RxxL) and the KEN box; in mitotic cyclins the D box lies near the N terminus, and a sea urchin cyclin B lacking its N-terminal 90 residues is stable and arrests egg extracts in mitosis (Murray, Solomon and Kirschner 1989); the nine-residue motif itself was identified by Glotzer, Murray and Kirschner (1991).

The two coactivators are regulated in opposite ways by Cdk1. Phosphorylation of APC/C subunits by Cdk1 promotes the binding of Cdc20, so APC/C–Cdc20 is switched on in mitosis (and held in check by the spindle assembly checkpoint until all chromosomes are attached). Phosphorylation of Cdh1 by Cdks prevents its binding, so APC/C–Cdh1 can act only after cyclins have been destroyed and Cdk activity has fallen. Cdh1 then keeps cyclins low throughout G1, destroying the remaining mitotic cyclins, Cdc20 itself, Plk1, Aurora kinases, geminin and Skp2, until it is phosphorylated at the next Start by G1/S-Cdk, whose cyclin E is not an APC/C substrate; from S phase to early mitosis the inhibitor Emi1 also blocks it. Substrates are destroyed in a defined order even by one ligase: cyclin A and Nek2A are degraded in prometaphase, because they bind Cdc20 in a way that escapes the checkpoint; securin and cyclin B are degraded at metaphase.

### 20.3.7. A Linked Series of Switches

The components form a chain (figure in 20.1.1). When conditions are right, G1-Cdk accumulates in response to mitogens and induces the genes for G1/S- and S-cyclins. G1/S-Cdk triggers Start, partly by releasing the brakes that keep Cdk activity low in G1: it phosphorylates Cdh1 and CKIs, marking the CKIs for SCF. S-Cdk then fires replication origins and, together with G1/S-Cdk, starts centrosome duplication. M-Cdk triggers the events of early mitosis and activates APC/C–Cdc20, which destroys securin and cyclins; the fall of Cdk activity activates APC/C–Cdh1, and Cdh1, CKIs (Sic1 in yeast, p27 in animals) and the low transcription of cyclin genes together make G1 a stable state of low Cdk activity. The cell leaves it only when the next G1/S-Cdk wave overcomes all three brakes at once, at Start. Each step creates the conditions for the next and removes those of the previous one, so the cycle moves in one direction. The decision at Start in animal cells, controlled by mitogens and the retinoblastoma protein, is the subject of [7.3.22](/7.3.22).

## 20.4. The Control of S Phase

### 20.4.1. Licensing and Firing

Every base pair of the genome must be copied once and only once: re-replication of even part of a chromosome amplifies genes and creates DNA damage. Replication starts at tens of thousands of origins in a human cell, and the solution, introduced in [7.2.7](/7.2.7#sec-7.6.1), is to split initiation into two steps that need opposite states of the control system:

1. **Origin licensing** ([Definition 7.6.1](/7.2.7#def-7.6.1)): in late mitosis and G1, when Cdk activity is low, the origin recognition complex (ORC) with Cdc6 and Cdt1 loads the MCM2–7 helicase core onto origins as an inactive double hexamer, the **prereplicative complex**.
2. Firing: in S phase, the Dbf4-dependent kinase DDK (Cdc7–Dbf4) phosphorylates MCM, and S-Cdk phosphorylates the initiation factors Sld2 and Sld3 (in vertebrates RecQL4 and Treslin), which with Dpb11 (TopBP1) recruit Cdc45 and the GINS complex. Two CMG helicases (Cdc45–MCM–GINS) form, separate and move away from the origin with the replisomes.

**Proposition 20.4.1 (Once-per-Cycle Replication)** Suppose that MCM loading can occur only when Cdk activity is low, that origin firing requires high Cdk activity, that firing removes the MCM double hexamer from the origin, and that Cdk activity rises once and falls once in each cycle. Then each origin fires at most once per cycle.

**Proof** Within one cycle, the interval of low Cdk activity (late M and G1) precedes the interval of high activity (S, G2 and early M). An origin can only fire in the high interval and only if it carries a loaded double hexamer. Firing converts that double hexamer into two moving CMG helicases, which leave the origin, so after firing the origin is unlicensed. It cannot be relicensed until Cdk activity falls again, which by assumption happens only once, at the end of the cycle; so no second firing is possible in the same cycle. $\square$

The proposition also explains why licensing and firing must be separated in time rather than merely in amount: if the two steps could overlap, an origin licensed and fired early in S could be reloaded and refired. The control system makes the two windows mutually exclusive by the same oscillation of Cdk activity that drives the rest of the cycle.

![Two windows for DNA replication. A: over one cycle (phases not to scale), the activity of S- and M-Cdks is low from late mitosis to late G1 and high from the G1/S transition until anaphase, while APC/C–Cdh1, active in the low window, destroys geminin. Origins can be licensed only in the low window and fired only in the high window. B: the steps at one origin. ORC, bound throughout the cycle, recruits Cdc6 and Cdt1, which load two MCM2–7 hexamers as an inactive head-to-head double hexamer around duplex DNA (the prereplicative complex); in S phase S-Cdk and DDK recruit Cdc45 and GINS, and two CMG helicases move apart, opening a replication bubble; while Cdk activity stays high, phosphorylated ORC and Cdc6 and geminin-bound Cdt1 cannot load new MCM, so a fired origin cannot fire again in the same cycle](./plots/licensing-window.py)

### 20.4.2. Preventing Re-replication

Cells use several overlapping mechanisms to block relicensing from S phase to the end of mitosis, so that the failure of one is tolerated:

- Cdk phosphorylation of ORC subunits reduces their activity; phosphorylated Cdc6 is exported from the nucleus (in yeast it is destroyed by SCF).
- Cdt1 is destroyed in S phase by two ubiquitin ligases: CRL4–Cdt2, which recognizes Cdt1 only when it is bound to PCNA at active replication forks, so destruction is coupled to replication itself, and SCF–Skp2 after Cdk phosphorylation.
- Geminin, a metazoan protein that accumulates from S phase and is destroyed by APC/C at the end of mitosis, binds the remaining Cdt1 and blocks MCM loading.
- In yeast, Cdk phosphorylation also exports the MCM proteins from the nucleus.

The first evidence came from *Xenopus* extracts: Blow and Laskey (1988) found that nuclei that had replicated in an extract could not replicate again unless their nuclear envelope was permeabilized, which let in a licensing factor (now known to be Cdt1 and MCM). Overexpression of Cdt1 or depletion of geminin in human cells causes re-replication, DNA damage and checkpoint arrest, and partial deregulation leads to localized amplification of chromosome segments.

### 20.4.3. Duplicating the Rest of the Chromosome

Chromosome duplication is more than DNA replication. G1/S-Cdk, by phosphorylating the coactivator NPAT at the histone gene clusters, induces a burst of histone synthesis (the replication-dependent histone mRNAs lack poly(A) and are degraded when replication stops), and nucleosomes are assembled behind the fork from old and new **histones** ([7.2.4](/7.2.4)), so the chromatin state of the parent is approximately reproduced in the daughters ([7.2.15](/7.2.15)). Sister-chromatid cohesion is established as the fork passes: cohesin rings loaded in G1 are converted to cohesive rings by acetylation of their Smc3 subunit (by Eco1/Esco), so the two sisters remain linked until anaphase ([7.3.21](/7.3.21)). The centrosome is duplicated in parallel, under a licensing logic of its own: at the G1/S transition G1/S-Cdk and the kinase Plk4 start one new centriole beside each old one, and the two centrioles of a pair cannot duplicate again until they have been disengaged in the following mitosis ([7.3.14](/7.3.14#sec-14.3.2), [7.3.21](/7.3.21)).

## 20.5. Entry into and Exit from M Phase

### 20.5.1. A Stockpile of Inactive M-Cdk

Cyclin B is synthesized from S phase onward and binds Cdk1, which is phosphorylated at once by CAK on Thr161 and by Wee1 and Myt1 on Thr14 and Tyr15. By late G2 the cell therefore contains a large stockpile of cyclin B–Cdk1 that is primed but held inactive, mostly in the cytoplasm. The trigger that starts its activation is not one molecule but a combination of S-phase and early mitotic kinases: cyclin A–Cdk, which is not inhibited as strongly, begins the process; Aurora A with its cofactor Bora activates the Polo-like kinase Plk1 in late G2, and Plk1 phosphorylates Cdc25 (activating it) and Wee1 (marking it for SCF–βTrCP). The first active cyclin B–Cdk1 appears at the centrosomes, and the complex is then rapidly imported into the nucleus at the end of prophase.

### 20.5.2. Positive Feedback Switches M-Cdk On

The activation, once begun, completes itself through three positive loops (figure in 20.3.4):

1. Active M-Cdk phosphorylates and activates its activator Cdc25.
2. Active M-Cdk phosphorylates and inhibits its inhibitors Wee1 and Myt1.
3. Active M-Cdk phosphorylates the kinase Greatwall (MASTL), which phosphorylates the small proteins ENSA and ARPP19; these become tight-binding inhibitors (and slowly dephosphorylated substrates) of PP2A-B55. Since PP2A-B55 dephosphorylates Cdc25, Wee1, Greatwall and Cdk1 substrates, its inhibition removes the drain while the tap is opened. PP2A-B55 also inactivates Greatwall, so the two are mutual antagonists, a double-negative and hence positive loop of its own.

The loops are linked to each other by positive feedback, which makes the switch robust and very steep: mitotic substrates go from mostly unphosphorylated to mostly phosphorylated within minutes. In large cells such as frog eggs the switch even spreads through space as a trigger wave, a self-propagating front of Cdk1 activation that crosses the egg at about $60\,\mu\mathrm{m\,min^{-1}}$, far faster than diffusion alone over that distance (Chang and Ferrell 2013). Active M-Cdk with Plk1 and Aurora A then triggers the events of early mitosis by phosphorylating hundreds of proteins: condensin and histone H1 (chromosome condensation), nuclear lamins and nucleoporins (nuclear envelope breakdown, [7.3.16](/7.3.16#sec-16.6.2)), microtubule regulators (spindle assembly), Golgi matrix proteins (Golgi fragmentation) and regulators of the actin cortex (mitotic rounding).

### 20.5.3. The Metaphase-to-Anaphase Transition

Entry into mitosis is triggered by phosphorylation; progression into anaphase is triggered by proteolysis. M-Cdk sets the stage by promoting the binding of Cdc20 to APC/C, so M-Cdk activates the machinery that will destroy it, a negative feedback with a built-in delay: APC/C–Cdc20 does not destroy cyclin B and securin until the spindle assembly checkpoint is satisfied, typically about 20 minutes after the last chromosome attaches ([7.3.21](/7.3.21)).

**Definition 20.5.1 (Securin and Separase)** **Separase** is a cysteine protease that cleaves the kleisin subunit of cohesin (Scc1, called Rad21 in vertebrates), opening the cohesin rings that hold sister chromatids together and allowing anaphase. **Securin** is an inhibitory chaperone of separase that binds it and blocks its active site until securin is ubiquitylated by APC/C–Cdc20 and destroyed by the proteasome at the metaphase-to-anaphase transition.

The names come from yeast genetics (separase is Esp1 in budding yeast and Cut1 in fission yeast; securin is Pds1 and Cut2). In vertebrates cyclin B–Cdk1 itself binds and inhibits separase, so cyclin B destruction releases separase in a second way; mice lacking securin are viable. Destroying securin and cyclin B at the same moment is what makes the transition abrupt and irreversible: the cleaved cohesin cannot be rebuilt until the next S phase, and the fall of Cdk activity flips the positive loops of 20.5.2 into the dephosphorylation state.

### 20.5.4. Exit from Mitosis

Exit requires the dephosphorylation of the many proteins phosphorylated in early mitosis, in a defined order: substrates phosphorylated weakly or dephosphorylated quickly by PP2A-B55 and PP1 lose their phosphates first (anaphase spindle changes), others later (nuclear envelope reassembly, cytokinesis). When cyclin B destruction is prevented by a nondegradable cyclin B lacking its destruction box, sister chromatids still separate, because securin is destroyed, but the cell stalls in an anaphase-like or telophase-like state with condensed chromosomes, a persistent spindle and no cytokinesis. Exit thus needs both proteolysis (to remove the kinase) and phosphatases (to remove its marks). In budding yeast a signaling network, the mitotic exit network, releases Cdc14 from the nucleolus in late anaphase only when the spindle has delivered a nucleus into the bud, which couples exit to correct segregation. As Cdk activity falls, APC/C–Cdh1 takes over from APC/C–Cdc20 (which is itself a Cdh1 substrate), CKIs accumulate, and the cell enters the stable G1 state of 20.3.7.

## 20.6. The Cell Cycle as an Oscillator

### 20.6.1. Embryonic Cycles Without Checkpoints

In a frog egg extract, cyclin B is synthesized, Cdk1 activity rises, falls and rises again with a period of 30–60 minutes for many cycles, with or without nuclei, and even when DNA replication is blocked: the embryonic control system is a clock rather than a sequence of dominoes. Murray and Kirschner (1989) showed that an extract whose own mRNA had been destroyed cycled when supplied with cyclin B mRNA alone, so the synthesis of a single protein drives the oscillation, and the cycle is closed by the destruction of that protein by APC/C. A negative feedback loop is not by itself enough for sustained oscillation; the loop must contain a delay or a switch. Here, the positive feedback of 20.5.2 supplies the switch.

**Definition 20.6.1 (Cell-Cycle Oscillator)** The **cell-cycle oscillator** is the autonomous biochemical oscillation of Cdk1 activity generated by the continuous synthesis of cyclin, the switchlike activation of cyclin–Cdk1 through positive feedback, and the delayed negative feedback by which active Cdk1 activates APC/C–Cdc20 and so destroys its own cyclin. Mathematically it is a stable **limit cycle** of a relaxation oscillator.

### 20.6.2. A Minimal Model

The essentials can be written as three ordinary differential equations, simplified from the model of Novák and Tyson (1993). Let $C$ be the total concentration of cyclin B–Cdk1 (Cdk1 is in excess, so every cyclin is bound), $u$ the concentration of active, dephosphorylated cyclin B–Cdk1, and $A$ the active fraction of APC/C–Cdc20:

$$
\begin{aligned}
\frac{\mathrm{d}C}{\mathrm{d}t} &= k_{\mathrm{s}} - k_{\mathrm{d}}(A)\,C, \\
\frac{\mathrm{d}u}{\mathrm{d}t} &= k_{25}(u)\,(C - u) - k_{\mathrm{wee}}(u)\,u - k_{\mathrm{d}}(A)\,u, \\
\frac{\mathrm{d}A}{\mathrm{d}t} &= k_{\mathrm{a}}\,\frac{u^m}{K_{\mathrm{a}}^m + u^m}\,(1 - A) - k_{\mathrm{i}}A,
\end{aligned}
\tag{20.1}
$$
with $k_{\mathrm{d}}(A) = k_{\mathrm{d}0} + k_{\mathrm{d}1}A$, $k_{25}(u) = k_{25}' + k_{25}''H(u)$, $k_{\mathrm{wee}}(u) = k_{\mathrm{w}}' + k_{\mathrm{w}}''\,(1 - H(u))$ and $H(u) = u^4/(K^4 + u^4)$.

| Parameter | Value | Meaning |
|---|---|---|
| $k_{\mathrm{s}}$ | $2\,\mathrm{nM\,min^{-1}}$ | cyclin B synthesis (new complexes join the inactive pool) |
| $k_{\mathrm{d}0}$, $k_{\mathrm{d}1}$ | $0.01$, $0.4\,\mathrm{min^{-1}}$ | basal and APC/C-dependent cyclin destruction |
| $k_{25}'$, $k_{25}''$ | $0.03$, $1\,\mathrm{min^{-1}}$ | Cdc25 activity: basal, and the part activated by Cdk1 |
| $k_{\mathrm{w}}'$, $k_{\mathrm{w}}''$ | $0.02$, $0.2\,\mathrm{min^{-1}}$ | Wee1 activity: basal, and the part inhibited by Cdk1 |
| $K$, $K_{\mathrm{a}}$ | $20\,\mathrm{nM}$ | Cdk1 levels for half-maximal feedback and APC/C activation |
| $m$ | 4 | steepness of APC/C activation (**Hill coefficient**) |
| $k_{\mathrm{a}}$, $k_{\mathrm{i}}$ | $0.3$, $0.08\,\mathrm{min^{-1}}$ | APC/C activation and inactivation; their slowness is the delay |

The two feedback terms in the $u$ equation are the positive loops: Cdc25 activity rises and Wee1 activity falls as $u$ rises. The $A$ equation is the delayed negative loop. With these parameters the system has a single unstable steady state surrounded by a stable limit cycle with a period of about 65 minutes (figure below, panel A): cyclin accumulates slowly while Cdk1 stays off, Cdk1 switches on abruptly, APC/C follows a few minutes later, and cyclin is destroyed.

### 20.6.3. Bistability and Hysteresis of the Cdk1 Switch

The behavior is easiest to understand in the $(C, u)$ **phase plane**. If cyclin cannot be degraded ($A = 0$, as with a nondegradable cyclin B), the steady states of $u$ for a fixed $C$ satisfy $\mathrm{d}u/\mathrm{d}t = 0$, which can be solved for $C$:

$$
C = u\left(1 + \frac{k_{\mathrm{wee}}(u) + k_{\mathrm{d}0}}{k_{25}(u)}\right).
\tag{20.2}
$$
Because the ratio of Wee1 to Cdc25 activity falls steeply as $u$ rises, $C(u)$ is not monotonic: for intermediate $C$, three values of $u$ satisfy (20.2), the outer two stable and the middle one unstable. Cdk1 activity is bistable, and the response to cyclin shows hysteresis (Definitions 18.4.2 and 18.4.3): Cdk1 switches on only when cyclin exceeds the right fold (about $43\,\mathrm{nM}$ in the model), but once on it stays on until cyclin falls below the left fold (about $24\,\mathrm{nM}$). The limit cycle of the full model runs along the lower branch as cyclin accumulates, jumps to the upper branch after passing the right fold, and travels back along it as APC/C destroys cyclin, until it falls off the left fold: a relaxation oscillation whose amplitude is set by the width of the hysteresis loop.

**Example 20.6.1** The prediction was tested in *Xenopus* egg extracts arrested in interphase by blocking protein synthesis, to which a nondegradable cyclin B was added at various concentrations (Sha et al. 2003; Pomerening, Sontag and Ferrell 2003). Extracts starting from interphase activated Cdk1 only above about 32–40 nM cyclin, whereas extracts starting from mitosis remained mitotic down to about 16–24 nM: the thresholds for entering and leaving M phase differ by a factor of about two. In the cell, this hysteresis means that a transient dip in cyclin level during mitosis does not cause a premature exit, and that the transition, once made, is not undone by small fluctuations.

Pomerening, Kim and Ferrell (2005) then removed the positive feedback in extracts by replacing Cdk1 with Cdk1AF, which cannot be inhibited by Wee1 or Myt1. Cdk1 activity still oscillated, but the oscillations were damped after a few cycles, had lower amplitude and lost their abrupt rise, as in the model when $k_{25}''$ and $k_{\mathrm{w}}''$ are set to zero (panel C). Negative feedback alone produces a damped oscillation; the positive loops turn it into a robust, large-amplitude, relaxation-type oscillation whose period can be tuned by the rate of cyclin synthesis without losing amplitude. In the language of [2.4](/2.4), the steady state of the model loses stability through a **Hopf bifurcation** as the strength of the positive feedback increases (between $k_{25}'' = 0.4$ and $0.6\,\mathrm{min^{-1}}$ with the other parameters as in the table).

![A minimal model of the embryonic cell-cycle oscillator, Eq. (20.1). A: time courses of total cyclin B–Cdk1 (C), active Cdk1 (u) and APC/C activity (dashed, scaled by 60 nM): cyclin accumulates for most of the cycle while Cdk1 stays off; Cdk1 then switches on abruptly, activates APC/C after a delay, and cyclin is destroyed (period about 65 min). B: the (C, u) phase plane. The grey S-shaped curve is the set of steady states of u for nondegradable cyclin, Eq. (20.2); the solid parts are stable, the dashed part unstable, and the folds at about 43 nM and 24 nM are the thresholds for switching Cdk1 on and off (hysteresis). The limit cycle (red, with arrows showing its direction) follows the lower branch as cyclin rises, jumps up after passing the right fold, and returns along the upper branch as cyclin is destroyed. C: with the positive feedback removed (Cdc25 and Wee1 rates fixed at 0.1 per min), the oscillation is damped and the system settles to a steady state with intermediate Cdk1 activity](./plots/cdk-oscillator.py)

### 20.6.4. Oscillator Plus Checkpoints

The somatic cell cycle keeps the oscillator but adds brakes. Each of the three transitions is a bistable switch built from positive feedback (at Start, the Rb–E2F loop of [7.3.22](/7.3.22); at G2/M, the loops of 20.5.2; at the metaphase-to-anaphase transition, the mutual inhibition of Cdk1 and Cdh1 and the irreversible cleavage of cohesin). A checkpoint holds the system on one side of a switch by inhibiting a component that the switch needs (Cdc25 after DNA damage, Cdc20 when chromosomes are unattached), and when the brake is released the switch flips completely and the system does not slide back: the irreversibility of cell-cycle transitions is a property of the feedback in the network, not of any single reaction (Novák et al. 2007). An embryonic cycle is thus a clock with the brakes taken off, and a somatic cycle is a sequence of switches that the clock can throw only when the checkpoints allow it. The brakes that decide whether to divide at all, and their failure in cancer, are the subject of [7.3.22](/7.3.22); the general theory of such networks belongs to [7.9](/7.9).

## Summary

| Topic | Key points |
|---|---|
| Cell cycle (Definition 20.1.1) | G1, S, G2, M; interphase = G1 + S + G2; G0 (Definition 20.1.2); G1 most variable; embryonic cycles lack gap phases, endocycles lack mitosis |
| Measurement | mitotic and labeling indices, flow cytometry of DNA content, labeled mitoses method (Definition 20.1.3), Fucci; exponential age distribution $n(a) \propto 2^{-a/T}$ |
| Synchronization (Definition 20.1.4) | shake-off, double thymidine block, nocodazole, Cdk inhibitors, serum starvation |
| Classic experiments | MPF = Cdk1–cyclin B (Definition 20.2.1); PCC shows dominance of M phase (Definition 20.2.2); *cdc* genes, Start and checkpoints (Definition 20.2.3); *wee1* and *cdc25*; cyclin destruction; Nobel Prize 2001 |
| Components (Definition 20.3.1) | G1-, G1/S-, S-, M-Cdk; CAK activates (Definition 20.3.2); Wee1/Myt1 inhibit, Cdc25 reverses (Definition 20.3.3); CKIs: INK4, Cip/Kip, Sic1 (Definition 20.3.4); PP2A-B55, PP1; SCF (Definition 20.3.5) and APC/C–Cdc20/Cdh1 (Definition 20.3.6); a single Cdk–cyclin can order the cycle by thresholds (Remark 20.3.1) |
| S phase | licensing at low Cdk, firing at high Cdk: once per cycle (Proposition 20.4.1); geminin, CRL4–Cdt2, ORC and Cdc6 phosphorylation; cohesion and centrosome duplication |
| M phase | stockpile of inactive M-Cdk; Plk1 trigger; positive loops through Cdc25, Wee1 and Greatwall–ENSA–PP2A-B55; APC/C–Cdc20 destroys securin and cyclin B; separase opens cohesin (Definition 20.5.1); exit needs proteolysis and phosphatases |
| Oscillator (Definition 20.6.1) | cyclin synthesis + bistable Cdk1 switch + delayed APC/C feedback, Eq. (20.1); hysteresis of Cdk1 activation, Eq. (20.2) and Example 20.6.1; positive feedback makes oscillations robust; somatic cycle = oscillator + checkpoints |

## Questions

1. In an exponentially growing culture with a cycle time of 24 h, a 20-minute EdU pulse labels 30% of the cells, and G2 + M together last 5 h. Estimate the length of S phase, first naively and then taking the age distribution into account.

   **Answer** Naively, $T_{\mathrm{S}} \approx 0.30 \times 24 = 7.2\,\mathrm{h}$. With the age density of 20.1.4, S spans ages $T_{\mathrm{G1}}$ to $T - 5\,\mathrm{h}$, so $0.30 = 2\left(2^{-T_{\mathrm{G1}}/24} - 2^{-19/24}\right)$. Since $2^{-19/24} = 0.577$, $2^{-T_{\mathrm{G1}}/24} = 0.727$, so $T_{\mathrm{G1}} = -24\log_2 0.727 \approx 11.0\,\mathrm{h}$ and $T_{\mathrm{S}} = 24 - 11.0 - 5 \approx 8.0\,\mathrm{h}$. The naive estimate is too short because cells late in the cycle are under-represented in an exponential population.

2. Explain why a fission yeast *wee1* mutant divides small, a *cdc25* temperature-sensitive mutant at the restrictive temperature becomes very long, and the double mutant *wee1 cdc25* divides at a nearly normal size. What does the double mutant tell us about the role of Tyr15 phosphorylation?

   **Answer** Wee1 phosphorylates Cdc2 on Tyr15 and delays mitosis until the cell has grown enough to accumulate sufficient Cdc25 and cyclin to overcome it; without Wee1, Cdc2 is activated early, at a smaller size. Without Cdc25, the inhibitory phosphate cannot be removed, Cdc2 is never activated and the cells grow without dividing. In the double mutant, Tyr15 is not phosphorylated, so Cdc25 is not needed; division is then controlled by other inputs (cyclin accumulation and other phosphatases and kinases), which give a roughly normal size. The inhibitory phosphorylation is therefore a regulatory layer superimposed on cyclin–Cdk activation, used to set the timing of mitosis and to respond to checkpoints, rather than an essential part of the engine.

3. When a G2 cell is fused with an S-phase cell, the G2 nucleus does not replicate its DNA, whereas a G1 nucleus fused with an S-phase cell does. Explain this result in modern molecular terms.

   **Answer** The S-phase cytoplasm contains active S-Cdk and DDK, which fire licensed origins. A G1 nucleus has licensed origins carrying MCM double hexamers and therefore replicates. A G2 nucleus has already fired its origins, which are now empty, and it cannot load new MCM because Cdk activity is high in the fused cell (ORC and Cdc6 phosphorylated, Cdt1 inhibited by geminin or destroyed). Replication requires a licensed origin and an S-phase environment; only the latter is supplied by the fusion (Proposition 20.4.1).

4. A nondegradable form of cyclin B is added to a cycling *Xenopus* egg extract. Predict the behavior of the extract and of sperm nuclei in it. Why do sister chromatids still separate in cells expressing nondegradable cyclin B?

   **Answer** The extract enters mitosis and stays there: Cdk1 activity remains high, nuclei break down, chromosomes condense and spindles form, but there is no exit, no nuclear reassembly and no further cycle. In cells, APC/C–Cdc20 is still activated and destroys securin, so separase is freed and cleaves cohesin; sister chromatids separate, but because Cdk1 stays active the spindle is not disassembled properly, nuclei do not re-form and cytokinesis fails. Exit from mitosis requires the fall of Cdk activity, not just the destruction of securin.

5. Using Eq. (20.2), explain why the response of Cdk1 to cyclin would be graded (not bistable) if Wee1 and Cdc25 were not regulated by Cdk1. What would happen to the thresholds if Wee1 activity were reduced?

   **Answer** If $k_{25}$ and $k_{\mathrm{wee}}$ are constants, Eq. (20.2) becomes $C = u\,(1 + (k_{\mathrm{wee}} + k_{\mathrm{d}0})/k_{25})$, a straight line: $u$ is proportional to $C$, a graded response with one steady state for each $C$. Bistability requires the ratio $k_{\mathrm{wee}}(u)/k_{25}(u)$ to fall steeply with $u$, which makes $C(u)$ fold back. Reducing Wee1 activity (smaller $k_{\mathrm{w}}'$ and $k_{\mathrm{w}}''$) lowers $C(u)$ for every $u$, so both folds move to lower cyclin concentrations and the hysteresis loop narrows: Cdk1 is activated at a lower cyclin level, earlier in G2, the counterpart of the small size of *wee1* mutants.

6. Why is it important that APC/C–Cdc20 is activated by M-Cdk with a delay, rather than instantly? What would a cell lose if APC/C were activated at the same time as Cdk1?

   **Answer** If APC/C were activated as soon as Cdk1 became active, cyclin B would be destroyed before the events of early mitosis (condensation, spindle assembly, attachment) were complete, and the oscillation would collapse to a small-amplitude or steady state: in the model, a fast negative loop damps the relaxation oscillation. The delay (slow APC/C activation and, in somatic cells, the spindle assembly checkpoint) gives M phase a minimum duration and ensures that segregation happens only after all chromosomes are attached.

7. In a Fucci experiment, a cell that has just divided is red; some hours later it is yellow, then green, and green persists until the next mitosis. Which proteins are being destroyed at each stage, and by which ubiquitin ligase?

   **Answer** In G1 the geminin reporter is destroyed by APC/C–Cdh1, so only the red Cdt1 reporter is seen. At the G1/S transition Cdh1 is inactivated by G1/S-Cdk and geminin begins to accumulate while Cdt1 has not yet been destroyed: both colors, yellow. From S phase, Cdt1 is destroyed by CRL4–Cdt2 (coupled to replication) and SCF–Skp2, so the nucleus is green through S, G2 and early M, until APC/C destroys the geminin reporter in late mitosis.

8. Proposition 20.4.1 assumes that firing removes the MCM double hexamer from the origin. Suppose instead that an origin is passively replicated by a fork coming from a neighboring origin before it has fired. Does the conclusion still hold?

   **Answer** Yes. The passing replisome displaces the inactive MCM double hexamer (and ORC) from the unfired origin, so the replicated origin is unlicensed just as if it had fired; it cannot be relicensed while Cdk activity is high. Passive replication therefore also counts as the single use of that stretch of DNA in the cycle. Dormant licensed origins that are not used in this way serve as backups when forks stall.
