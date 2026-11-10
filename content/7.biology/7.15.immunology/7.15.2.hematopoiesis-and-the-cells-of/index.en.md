---
title: Hematopoiesis and the Cells of the Immune System
source_hash: a9af758d759f
---

The previous chapter posed the five questions of an immune response; this chapter answers the most basic prerequisite among them: who the participating cells are, where they come from, and how many there are of each. All immune cells are blood cells and derive from **hematopoietic stem cells** in the bone marrow. The hematopoietic stem cell itself and the general principles of the hematopoietic hierarchy were covered in [7.3.24](/7.3.24), and the physiology of blood leukocytes (counts, extravasation, phagocytosis, and the vascular reaction of inflammation) is in [7.14.11](/7.14.11). Here these cells are reorganized from the immunological point of view: they are grouped by lineage (myeloid and lymphoid), for each cell type we remember only "what it recognizes, what it does, and where it is", and morphology, numbers, and surface markers are collected in a single summary table (§2.2). The places where cells act, the immune organs, are the subject of the next chapter; the effector mechanisms of the various cell types are developed in Chapters 5, 7, and 17; and the systematic method of identifying cells by surface markers is in [7.15.35](/7.15.35).

## 2.1. Hematopoiesis and the Lineages of Immune Cells

### 2.1.1. Hematopoietic Stem Cells and the Two Major Progenitors

In adults hematopoiesis takes place in the bone marrow (in the fetus it occurs successively in the yolk sac, liver, and spleen, [7.3.24](/7.3.24)). Self-renewing **hematopoietic stem cells** give rise to multipotent progenitors, whose potential becomes progressively restricted and which divide into two major branches.

**Definition 2.1.1** Progenitors derived from multipotent progenitors that can differentiate only into myeloid blood cells (granulocytes, monocytes and macrophages, some dendritic cells, mast cells, and also erythrocytes and megakaryocytes) are called **common myeloid progenitors** (often called "myeloid stem cells" in Chinese textbooks); progenitors that can differentiate only into lymphocytes (T cells, B cells, NK cells, and other innate lymphoid cells) are called **common lymphoid progenitors** ("lymphoid stem cells").

The common myeloid progenitor divides further into the granulocyte–monocyte progenitor (GMP) and the megakaryocyte–erythroid progenitor (MEP). The GMP gives rise to neutrophils, eosinophils, basophils, and monocytes; the macrophage–dendritic cell progenitor (MDP) gives rise to monocytes and the common dendritic cell progenitor (CDP), which produces conventional dendritic cells. Among the progeny of the common lymphoid progenitor, B cells and NK cells mature in the bone marrow, whereas the precursors of T cells leave the bone marrow and develop in the thymus ([7.15.15](/7.15.15)).

![Hematopoietic lineages of immune cells (simplified). The self-renewing hematopoietic stem cell (HSC) divides via multipotent progenitors (MPP) into the common myeloid progenitor (CMP, warm-colored branch) and the common lymphoid progenitor (CLP, cool-colored branch). The CMP divides into the megakaryocyte–erythroid progenitor (MEP: erythrocytes, megakaryocytes, and platelets) and the granulocyte–monocyte progenitor (GMP: neutrophils, eosinophils, basophils, and mast cells, as well as monocytes via the MDP and conventional dendritic cells via the CDP); after entering tissues, monocytes become macrophages and can also differentiate into monocyte-derived dendritic cells. The CLP gives rise to B cells, NK cells and other innate lymphoid cells, and T cells that migrate to the thymus to develop; plasmacytoid dendritic cells can arise from either branch (dashed lines). The small boxes beside the branches show the main transcription factors that drive each branch. Real hematopoiesis is a more continuous process, and many progenitors are already biased toward one fate at the single-cell level; the tree is a summary of the population](./plots/hematopoiesis-lineages.py)

### 2.1.2. Lineage Commitment: Transcription Factors and Cytokines

Which branch a progenitor takes is decided by a few mutually antagonistic transcription factors, while cytokines maintain its survival and proliferation. The general principles of **master regulators** (mutual repression forms an either-or switch, and self-activation maintains the chosen fate) are in [7.3.24](/7.3.24); the table below lists only those most often mentioned in immune cell lineages, which are also often used as lineage markers in flow cytometry and tissue staining ([7.15.35](/7.15.35)).

| Branch | Key transcription factors | Main cytokines | Notes |
|---|---|---|---|
| Myeloid vs lymphoid | PU.1 (high: myeloid; low: lymphoid), Ikaros (lymphoid) | SCF, FLT3L, IL-3 | The dose of PU.1 determines the branch |
| Granulocyte vs monocyte | C/EBPα, C/EBPε (granulocyte); IRF8, KLF4 (monocyte) | G-CSF (granulocyte), M-CSF (monocyte), GM-CSF | C/EBPα and IRF8 antagonize each other |
| Eosinophil | GATA1, C/EBPα | IL-5 | |
| Basophil, mast cell | GATA2, MITF (mast cell) | IL-3, SCF (KIT ligand) | |
| Conventional dendritic cell | cDC1: IRF8, BATF3; cDC2: IRF4 | FLT3L | |
| Plasmacytoid dendritic cell | E2-2 (TCF4), IRF8 | FLT3L | |
| Erythroid, megakaryocytic | GATA1, KLF1 (erythroid), FLI1 (megakaryocytic) | EPO, TPO | Less related to immunity |
| B cell | E2A, EBF1, PAX5 | IL-7 (essential in mice) | PAX5 locks in the B-cell fate |
| T cell | Notch1 signaling, TCF-1, GATA3, BCL11B | IL-7 | Thymic epithelium provides Notch ligands |
| NK cell and ILC | Id2, NFIL3 (E4BP4), T-bet, EOMES (NK) | IL-15 (NK), IL-7 (ILC) | Id2 inhibits E proteins so the cell does not take the T or B path |

Most of these cytokines belong to the families of **colony-stimulating factors** and hematopoietic factors; their receptors and signaling are in [7.15.11](/7.15.11). Clinically, G-CSF is used after chemotherapy to promote neutrophil recovery and to mobilize hematopoietic stem cells into the peripheral blood for collection; after bone marrow transplantation all immune cells of the recipient derive from the donor, a unique problem of transplantation immunology ([7.15.29](/7.15.29)).

### 2.1.3. Homeostasis of Hematopoiesis: Production Rate = Pool Size / Lifespan

The numbers of blood cells remain stable for years, so the daily production of each cell type must equal its daily loss. If the pool size of a cell type is $N$ and its mean lifespan (mean residence time) is $\tau$, and death is assumed to be random (each cell dies with probability $1/\tau$ per unit time), then

$$
\frac{\mathrm{d}N}{\mathrm{d}t} = P - \frac{N}{\tau}, \qquad N^* = P\tau,
$$

and at steady state the production rate is $P = N^*/\tau$. This is a first-order linear equation ([2.4](/2.4)); after a departure from steady state, $N$ approaches the new steady state exponentially with time constant $\tau$.

**Example 2.1.1** An adult has about $5\,\mathrm{L}$ of blood with neutrophils at about $4 \times 10^{9}\,\mathrm{L^{-1}}$, so the circulating pool is about $2 \times 10^{10}$ cells; the "marginal pool" attached to vessel walls is of comparable size, giving about $4$–$5 \times 10^{10}$ cells in the blood in all. Radioactive labeling gives a half-life of neutrophils in blood of about $7\,\mathrm{h}$, so the mean residence time is $\tau = t_{1/2}/\ln 2 \approx 10\,\mathrm{h}$ and

$$
P \approx \frac{4.5 \times 10^{10}}{10\,\mathrm{h}} \approx 1 \times 10^{11}\ \text{cells per day},
$$

that is, about one million per second. This output is of the same order as that of erythrocytes (about $2 \times 10^{11}$ per day), even though there are a thousand times more erythrocytes than neutrophils in blood: neutrophils live far shorter lives. The bone marrow also stores about 10–20 times the blood pool of mature neutrophils, which are released within hours during infection, whereas increased production ("emergency granulopoiesis", driven by G-CSF) takes effect only after a day or two.

:::

The situation for lymphocytes is the opposite. The human body has about $4 \times 10^{11}$ T cells, the great majority in lymphoid organs rather than in the blood; the mean lifespan of naive T cells is measured in years, the number of new T cells exported by the adult thymus each day is small relative to this pool, and the T-cell pool is maintained mainly by slow self-renewal of peripheral cells ("homeostatic proliferation", sustained by IL-7 and IL-15). The number of lymphocytes therefore cannot be adjusted rapidly by "speeding up production" but only by expansion of selected clones ([7.15.1](/7.15.1)) and redistribution of cells among organs ([7.15.3](/7.15.3)).

![Homeostasis of hematopoiesis (illustrative calculation, values of the order found in the literature). A: pool size $N$ (light bars) and daily production calculated from $P = N/\tau$ (dark bars), on a logarithmic scale. The neutrophil pool is three orders of magnitude smaller than the erythrocyte pool, yet the production is of the same order because of the short lifespan (about 10 h vs 120 days); the T-cell pool is large and the lifespan is measured in years, so daily turnover is small. B: in the first-order model $\mathrm{d}N/\mathrm{d}t = P - N/\tau$, the change in blood neutrophil count after the production rate rises to 4 times its original value at $t = 0$ (emergency granulopoiesis): with $\tau = 10\,\mathrm{h}$ the count approaches the new steady state in a little over a day (solid line); release of the marrow reserve makes the count rise first within a few hours (dashed line). If $\tau$ were one year, the same change in production rate would be barely visible within weeks (dotted line), showing that the lymphocyte pool cannot be adjusted rapidly through production](./plots/leukocyte-turnover.py)

## 2.2. Overview of Leukocytes

**Definition 2.2.1 (Leukocyte)** **Leukocytes** are the nucleated blood cells of the blood, including granulocytes, monocytes, and lymphocytes; besides blood, they are abundant in lymph, lymphoid organs, and nearly all tissues.

"White blood cell" is a hematological category (the thin white layer above the erythrocyte layer after centrifugation), not a functional one: mast cells, macrophages, and dendritic cells all derive from hematopoietic stem cells but, once mature, are found almost exclusively in tissues. The table below is the first "master table of names" of this course and will be used in all later chapters.

| Cell | Share of blood leukocytes | Morphology | Main surface markers (human) | Main location | Lifespan | Main functions |
|---|---|---|---|---|---|---|
| Neutrophil | 40%–75% | Nucleus with 3–5 lobes, fine cytoplasmic granules | CD15, CD16, CD66b, CD11b | Blood; enters tissues during inflammation | About 10 h in blood, 1–2 days in tissues | Phagocytosis and killing of bacteria, NETs; effector cell of type 3 immunity |
| Eosinophil | 0.5%–5% | Bilobed nucleus, coarse orange-red granules | Siglec-8, CCR3, CD193 | Blood, mucosa (especially intestine) | Several days in tissues | Killing of helminths; type 2 immunity, allergy |
| Basophil | 0–1% | Lobed nucleus obscured by dark purple granules | FcεRI, CD123, CD203c | Blood; can enter inflamed tissue | Several days | Histamine release; IL-4 production; type 2 immunity |
| Mast cell | Not in blood | Cytoplasm full of metachromatic granules | KIT (CD117), FcεRI | Skin, mucosa, perivascular connective tissue | Weeks to months | Degranulation (histamine, tryptase); allergy, antiparasitic defense |
| Monocyte | 3%–10% | Largest cell, kidney- or horseshoe-shaped nucleus | CD14, CD16 (subset), CD11b, HLA-DR | Blood | About 1 day in blood | Enters tissues and differentiates into macrophages or dendritic cells |
| Macrophage | Not in blood | Irregular shape, abundant cytoplasm, phagocytic vacuoles | CD68, CD163, CD64, CD206 (some) | All tissues (each with its own name, [7.15.5](/7.15.5)) | Months to years (some self-renewing) | Phagocytic clearance, antigen presentation, cytokine secretion, tissue repair |
| Dendritic cell | <1% | Many long processes | HLA-DR high, CD11c; cDC1: CD141; cDC2: CD1c; pDC: CD123, CD303 | Subepithelium, tissue interstitium, T-cell zones of lymphoid organs | Several days | Uptake and presentation of antigen, priming of naive T cells |
| T cell | About 70% of lymphocytes | Small lymphocyte, large nucleus, scant cytoplasm | CD3; CD4 or CD8 | Blood, lymph, T-cell zones of lymphoid organs, tissues | Years for naive cells | Cell-mediated immunity; help and regulation |
| B cell | 10%–15% of lymphocytes | Small lymphocyte | CD19, CD20, surface Ig | Lymphoid follicles, splenic marginal zone, blood | Weeks to years | Antibody production; antigen presentation |
| Plasma cell | Very few in normal blood | Eccentric nucleus, "cartwheel" chromatin, well-developed rough endoplasmic reticulum | CD138, CD38 high, CD20 negative | Bone marrow, medullary cords of lymph nodes, lamina propria of mucosa | Days to decades | Massive antibody secretion |
| NK cell | 10%–15% of lymphocytes | Large granular lymphocyte | CD56, CD16; CD3 negative | Blood, liver, spleen, uterus | Weeks | Killing of virus-infected cells and tumor cells; IFN-γ secretion |

The normal adult blood leukocyte count is about $(4$–$10) \times 10^{9}\,\mathrm{L^{-1}}$. Changes in the differential leukocyte count are among the most commonly used immunological readouts in the clinic:

| Change | Common causes | Immunological meaning |
|---|---|---|
| Neutrophilia with immature band cells ("left shift") | Acute bacterial infection, tissue injury | Release of marrow reserves and emergency granulopoiesis |
| Neutropenia | Chemotherapy, some viral infections, autoimmunity | The risk of bacterial and fungal infection rises steeply as the absolute count falls |
| Relative lymphocytosis | Viral infection (for example atypical lymphocytes in infectious mononucleosis) | Expansion of virus-specific T cells |
| Lymphopenia | Glucocorticoids, acute stress, HIV infection | Redistribution or destruction of lymphocytes |
| Eosinophilia | Helminth infection, allergic disease, some drug reactions | Type 2 immunity (IL-5) |
| Monocytosis | Chronic infection (for example tuberculosis), convalescence | |

## 2.3. Myeloid Cells

### 2.3.1. Monocytes and Macrophages

**Definition 2.3.1** Mononuclear phagocytes in the blood are called **monocytes**; long-lived phagocytes that arise from the differentiation of monocytes after they enter tissues, or that settle in tissues during embryonic life and renew themselves, are called **macrophages**.

Monocytes and macrophages together are called the mononuclear phagocyte system. Human blood monocytes are divided by CD14 and CD16 into three subsets: classical monocytes (CD14⁺⁺CD16⁻, about 85%, rapidly recruited to sites of inflammation), intermediate monocytes (CD14⁺⁺CD16⁺), and nonclassical monocytes (CD14⁺CD16⁺⁺, "patrolling" along the vascular endothelium). Macrophages are long-lived "tissue housekeepers": at steady state they clear apoptotic cells, senescent erythrocytes, and debris; during infection they phagocytose pathogens, secrete inflammatory cytokines such as TNF, IL-1, and IL-6, and present antigen to T cells; and in the late phase of inflammation they take part in tissue repair. Macrophages in many tissues settle during embryonic life and are thereafter maintained by self-renewal without depending on replenishment by blood monocytes; their tissue-specific names, the classification of "activation states", and its limitations are in [7.15.5](/7.15.5).

### 2.3.2. Granulocytes and Mast Cells

**Definition 2.3.2 (Granulocyte)** Myeloid leukocytes whose cytoplasm contains abundant specific granules and whose nuclei are lobed are called **granulocytes** (also polymorphonuclear leukocytes). According to the affinity of the granules for dyes, there are three kinds: **neutrophils**, whose granules are neutral and which are the most numerous; **eosinophils**, whose granules are stained orange-red by the acidic dye eosin; and **basophils**, whose granules are stained dark purple by basic dyes.

The granule contents of the three granulocytes determine their functions. The azurophilic granules of neutrophils contain myeloperoxidase, elastase, and defensins, and the specific granules contain lactoferrin and the membrane proteins that make up NADPH oxidase; neutrophils are the first cells to reach a site of infection, are short-lived and abundant, and kill bacteria by phagocytosis, the respiratory burst, and neutrophil extracellular traps ([7.15.7](/7.15.7)). The granules of eosinophils contain major basic protein, eosinophil cationic protein, and peroxidase; these toxic proteins are effective against helminths that are too large to be phagocytosed and are released onto the surface of the worm. The granules of basophils contain histamine and heparin, and basophils are an important early source of IL-4 in blood.

**Definition 2.3.3 (Mast Cell)** **Mast cells** are granulated cells derived from bone marrow progenitors that enter tissues in an immature form and mature only there; they are found mainly in the skin, mucosa, and perivascular connective tissue, express the high-affinity IgE receptor (FcεRI) on their surface, and upon stimulation rapidly release histamine, proteases, and heparin from their granules and synthesize prostaglandins, leukotrienes, and cytokines.

Mast cells and basophils have similar granule contents and FcεRI, but they are different lineages: basophils mature in the bone marrow and circulate in the blood, whereas mast cells reside in tissues for years. Both are core effector cells of type 2 immunity and type I hypersensitivity ([7.15.26](/7.15.26)), and mast cells are also among the earliest "sentinels" at a site of infection ([7.15.5](/7.15.5)).

### 2.3.3. Dendritic Cells

**Definition 2.3.4 (Dendritic Cell)** **Dendritic cells** are hematopoietic-derived cells with long processes that efficiently take up and process antigen, migrate to lymphoid organs, present antigen to naive T cells, and provide costimulatory signals.

Dendritic cells are named for their morphology (discovered in mouse spleen by Steinman and Cohn in 1973), and their core function is to link innate and adaptive immunity: they are the only cells that can effectively initiate naive T-cell responses. There are three main kinds of dendritic cells in humans: two kinds of **conventional dendritic cells** (cDC1 excels at cross-presenting extracellular antigen to CD8⁺ T cells, and cDC2 mainly activates CD4⁺ T cells) and the **plasmacytoid dendritic cell** (pDC, which secretes large amounts of type I interferon after sensing viral nucleic acid); during inflammation, monocytes can also differentiate into monocyte-derived dendritic cells. Langerhans cells in the epidermis resemble dendritic cells in morphology and function but derive from progenitors that settle during embryonic life and are closer to macrophages in lineage. The division of labor, maturation, and migration of the subsets are in [7.15.14](/7.15.14).

Note that the **follicular dendritic cell** in lymphoid follicles, although similar in name, is not a hematopoietic-derived cell but a stromal cell; it does not process antigen but retains intact antigen (in the form of immune complexes) on its surface for long periods for B cells to recognize ([7.15.20](/7.15.20)).

## 2.4. Lymphocytes

### 2.4.1. Common Features

**Definition 2.4.1 (Lymphocyte)** **Lymphocytes** are leukocytes derived from the common lymphoid progenitor that are morphologically small round cells with a large nucleus and scant cytoplasm; they include T cells and B cells, which express clonally specific antigen receptors, and NK cells and other innate lymphoid cells, which do not express such receptors.

Resting lymphocytes are only $7$–$10\,\mathrm{\mu m}$ in diameter, have almost no cytoplasm, and are metabolically very inactive; under the microscope T cells, B cells, and NK cells are hard to tell apart and can be distinguished only by surface markers. After stimulation by antigen they become lymphoblasts more than $15\,\mathrm{\mu m}$ in diameter with abundant cytoplasm and begin to divide. An adult has about $10^{12}$ lymphocytes, with a total mass comparable to that of the liver, but only about 2% are in the blood, and the rest are distributed in lymphoid organs and tissues.

### 2.4.2. T Cells

**Definition 2.4.2 (T Cell)** **T cells** are lymphocytes that mature in the thymus and use the T-cell receptor (TCR) to recognize antigenic peptides presented by MHC molecules; their common lineage marker is CD3, which forms a complex with the TCR.

"T" stands for the *thymus*. In 1961 Miller found that mice thymectomized in the neonatal period have very few lymphocytes and cannot reject skin grafts, establishing the immunological function of the thymus. T cells can be classified along several dimensions, which later chapters develop in turn:

| Dimension | Categories | Chapter |
|---|---|---|
| TCR chains | αβ T cells (90%–95% of blood T cells); γδ T cells (more abundant in mucosa and skin) | [7.15.5](/7.15.5), [7.15.15](/7.15.15) |
| Coreceptor and MHC restriction | CD4⁺ T cells recognize peptides presented by MHC class II molecules; CD8⁺ T cells recognize peptides presented by MHC class I molecules; the CD4:CD8 ratio in blood is about 2:1 | [7.15.13](/7.15.13), [7.15.16](/7.15.16) |
| Function | Helper T cells (Th1, Th2, Th17, Tfh), cytotoxic T lymphocytes (CTL), *regulatory T cells* (Treg) | [7.15.17](/7.15.17) |
| State | Naive, effector, memory (§2.4.5) | [7.15.18](/7.15.18) |

### 2.4.3. B Cells and Plasma Cells

**Definition 2.4.3 (B Cell)** **B cells** are lymphocytes that mature in the bone marrow (in birds, the bursa of Fabricius) and use membrane-bound immunoglobulin as the antigen receptor (B-cell receptor, BCR) to recognize the native conformation of antigen directly; when activated they can differentiate into antibody-secreting plasma cells.

"B" originally referred to the bursa of Fabricius of birds: in 1956 Glick found that chickens whose bursa had been removed could not produce antibodies. Mammals have no bursa, and B cells develop in the bone marrow, which also happens to begin with B. Unlike T cells, B cells can recognize almost any kind of molecule, including proteins, polysaccharides, lipids, and nucleic acids, and do not require the antigen to be processed or presented.

**Definition 2.4.4 (Plasma Cell)** **Plasma cells** are antibody-secreting cells formed by the terminal differentiation of B cells: they no longer express (or express little) membrane BCR, no longer divide, and secrete one specific antibody at a rate of thousands of molecules per second.

The rough endoplasmic reticulum of plasma cells is extremely well developed, the nucleus is eccentric, and the chromatin has a "cartwheel" appearance. Short-lived plasma cells survive for days in the medullary cords of lymph nodes and the red pulp of the spleen and produce the early antibodies of the primary response; long-lived plasma cells that have passed through a germinal center migrate to the bone marrow and can survive for decades, and they are the main source of long-term maintenance of serum antibody ([7.15.20](/7.15.20)).

### 2.4.4. NK Cells and Innate Lymphoid Cells

**Definition 2.4.5 (Natural Killer Cell)** **Natural killer cells** (NK cells) are large granular lymphocytes that express neither TCR nor BCR and can kill certain virus-infected cells and tumor cells without prior sensitization; the typical phenotype of human NK cells is CD3⁻CD56⁺, and most express CD16.

NK cells are the "innate" members among lymphocytes: they use germline-encoded activating and inhibitory receptors to judge whether a target cell is abnormal, in particular whether the target has lost MHC class I molecules ("missing self"), and kill by the same perforin–granzyme mechanism as CTLs ([7.15.5](/7.15.5)). NK cells were discovered in the 1970s as "background killing" in the study of tumor immunity, and it was later recognized that they are members of a large class of **innate lymphoid cells**; the other innate lymphoid cells (ILC1, ILC2, ILC3) do not kill but rapidly secrete in tissues the same cytokines as Th1, Th2, and Th17 and are the innate versions of type 1, 2, and 3 immunity ([7.15.1](/7.15.1), [7.15.5](/7.15.5)).

### 2.4.5. Naive, Effector, and Memory

T cells and B cells go through three states during life, which is important for understanding the dynamics of the response and for reading surface markers.

**Definition 2.4.6** Mature T or B cells that have completed development and left the central immune organs but have not yet met their specific antigen are called **naive lymphocytes**; cells that arise from the activation and proliferation of naive lymphocytes by antigen and then differentiate to carry out clearance functions directly (such as CTLs, effector Th cells, and plasma cells) are called **effector cells**; long-lived cells that survive after the response ends and can respond rapidly on re-encountering the same antigen are called **memory cells**.

| | Naive | Effector | Memory |
|---|---|---|---|
| Has met antigen | No | Yes (responding) | Yes (response has ended) |
| Number (per specificity) | Very few ($10^{-6}$–$10^{-5}$) | Very many at the peak | $10^{2}$–$10^{3}$ times more than naive |
| Lifespan | Years, maintained by IL-7 and weak signals from self pMHC | Most die by apoptosis within days to weeks | Years to decades, maintained by IL-7 and IL-15 |
| Migration | Recirculate between blood and peripheral lymphoid organs | Migrate to infected tissue | Some recirculate, some reside in tissues |
| Activation requirement | Require professional antigen-presenting cells (dendritic cells) and strong costimulation | — | Lower activation threshold, faster |
| Typical surface markers (human T cells) | CD45RA⁺, CCR7⁺, CD62L⁺ | CD45RO⁺, activation markers CD69, CD25, HLA-DR | CD45RO⁺; central memory CCR7⁺, effector memory CCR7⁻ |

The detailed subdivision of memory subsets and the mechanisms of their maintenance are in [7.15.18](/7.15.18). The two splice isoforms of CD45 (CD45RA and CD45RO) distinguish naive from memory cells and are one of the most commonly used examples of alternative RNA splicing in immunology.

![Morphology of the major immune cells (schematic, sizes approximately to scale; cell names below the figure). Myeloid: neutrophil (lobed nucleus, fine granules), eosinophil (bilobed nucleus, coarse granules), basophil (granules obscuring the nucleus), mast cell (in tissue, full of granules), monocyte (kidney-shaped nucleus), macrophage (irregular, with phagocytic vacuoles), dendritic cell (long processes). Lymphoid: small lymphocyte (nucleus occupying most of the cell; T, B, and NK cells are morphologically indistinguishable), plasma cell (eccentric nucleus, well-developed rough endoplasmic reticulum), memory cell and NK cell (large granular lymphocytes)](./plots/immune-cell-gallery.py)

## Summary

- Immune cells all derive from **hematopoietic stem cells** in the bone marrow and differentiate along two branches, the **common myeloid progenitor** (granulocytes, monocytes and macrophages, conventional dendritic cells, mast cells) and the **common lymphoid progenitor** (T, B, and NK cells and other innate lymphoid cells) (Definition 2.1.1); the branches are determined by mutually antagonistic transcription factors (PU.1, C/EBPα, IRF8, GATA, E2A–EBF1–PAX5, Notch–TCF-1, Id2) and maintained by SCF, FLT3L, CSFs, and IL-7 and IL-15.
- At steady state the production rate $=$ pool size / lifespan (Example 2.1.1): neutrophils with a lifespan of about 10 h are produced at about $10^{11}$ per day and can be greatly increased within hours to a day or two by marrow reserves and emergency production; the T-cell pool, with lifespans of years, can be adjusted only by clonal expansion and redistribution.
- The morphology, proportion, surface markers, location, lifespan, and function of each kind of **leukocyte** (Definition 2.2.1) are in the master table of §2.2; they are best remembered by "what is recognized, what is done":

  | Cell | Recognizes | Main role | Effector module |
  |---|---|---|---|
  | **Neutrophils** | PRRs, Fc and complement receptors | Phagocytosis and killing | Type 3 |
  | **Eosinophils**, **basophils**, **mast cells** | IgE (FcεRI), IgG | Granule release | Type 2 |
  | **Monocytes** and **macrophages** | PRRs, Fc and complement receptors | Phagocytosis, inflammation, repair, presentation | All three types; activated in type 1 |
  | **Dendritic cells** | PRRs | Priming of naive T cells | Determine the type of response |
  | **NK cells** | Activating and inhibitory receptors | Killing, IFN-γ | Type 1 |
  | **T cells** | TCR: peptides presented by MHC | Cell-mediated immunity, help, regulation | All three types |
  | **B cells** and **plasma cells** | BCR: native conformation of antigen | Antibodies | All three types |

- Lymphocytes exist in three states, **naive lymphocytes**, **effector cells**, and **memory cells** (Definition 2.4.6), which can be distinguished by CD45RA/RO, CCR7, and CD62L.

## Questions

1. Conditioning before bone marrow transplantation eliminates the recipient's hematopoietic stem cells. Which leukocytes recover first in the recipient's blood after transplantation? Why is full recovery of T cells much slower?

   **Answer** Neutrophils recover first (usually in 2–3 weeks), because their lifespan is short and their pool is small, so the progeny of donor hematopoietic stem cells quickly reach the steady-state number (the logic of Example 2.1.1: the smaller $\tau$ is, the faster the approach to steady state). T-cell recovery is much slower (months to years): new naive T cells must develop in the thymus, and the adult thymus has involuted and exports little; the T cells that recover early are mainly peripheral expansion of mature T cells in the graft, with a narrow repertoire diversity.

2. Use the model of §2.1.3 to explain why the blood neutrophil count can rise within a few hours of infection, and why this early rise cannot be explained by "increased bone marrow production".

   **Answer** Increased production requires proliferation and maturation of progenitors and takes days to deliver new cells into the blood; even if new cells entered the blood immediately, the count would approach the new steady state slowly with time constant $\tau \approx 10\,\mathrm{h}$. The rise within a few hours comes from redistribution of existing cells: mature neutrophils stored in the bone marrow (about 10–20 times the blood pool) are released, and cells in the marginal pool detach from vessel walls and enter the circulating pool.

3. Why is it said that "dendritic cell" and "follicular dendritic cell" are confused only in name? What is the essential difference in function?

   **Answer** Dendritic cells are hematopoietic-derived leukocytes that take up antigen, degrade it intracellularly into peptides, and load them on MHC molecules to present to T cells; follicular dendritic cells are stromal cells (not hematopoietic in origin) in lymphoid follicles that do not process antigen but retain intact antigen (immune complexes) on their surface for a long time through complement receptors and Fc receptors, for recognition by the BCR of B cells. The former serves T cells and the latter serves B cells; they merely both have processes in morphology.

4. A complete blood count shows leukocytes at $12 \times 10^{9}\,\mathrm{L^{-1}}$, of which 18% are eosinophils. Which effector module does this suggest is activated? What are possible causes?

   **Answer** The absolute eosinophil count is about $2.2 \times 10^{9}\,\mathrm{L^{-1}}$, clearly elevated, suggesting type 2 immunity (IL-5 drives the production and survival of eosinophils). Common causes are helminth infection and allergic disease (asthma, atopic dermatitis); eosinophilia is also seen in drug reactions and a few hematologic malignancies, and these must be distinguished using the history and other tests.

5. (Open question) The lifespan of naive T cells is measured in years, whereas most effector cells of the same clone die within weeks. Explain the significance of this arrangement from the standpoint of the immune system's limited "resources".

   **Answer** Key points: the total number of lymphocytes is held by homeostasis (the amount of survival factors such as IL-7 and IL-15 is limited), while the repertoire must cover as many specificities as possible, so each specificity can retain only very few long-lived naive cells; once a response occurs, the selected clone temporarily expands to a huge number and must contract after antigen clearance, otherwise a single clone would crowd out the space of other specificities and cause persistent inflammatory damage. The memory cells left after contraction, more than the naive precursors but far fewer than at the peak of the effector response, are a compromise between "preparing for threats already encountered" and "preserving coverage of unknown threats" ([7.15.18](/7.15.18)).
