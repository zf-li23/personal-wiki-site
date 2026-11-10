---
title: B-Cell Development, Receptors and Subsets
description: B cells develop in the bone marrow in stages that follow the order of heavy-chain and light-chain gene rearrangement, pass two checkpoints (pre-BCR and complete BCR) and a test for self-reactivity, and mature in the spleen; how the BCR complex and coreceptor recognize antigen and transmit signals; the division of labor among follicular, marginal zone and B-1 subsets; and the three functions of B cells.
source_hash: 008ec0ca4bde
---

This chapter answers the question "who is recognizing?" on the B-cell side: how a **B cell** acquires a single unique antigen receptor, how that receptor is tested, and how binding of antigen is turned into an intracellular signal. The structure of the antigen-receptor genes and the mechanism of rearrangement were described in [7.15.12](/7.15.12); here rearrangement is placed on the timeline of development to show how it decides the fate of the cell. T-cell development in the thymus ([7.15.15](/7.15.15)) follows the same logic, and the two chapters can be read side by side. The next chapter ([7.15.20](/7.15.20)) describes the response of a mature B cell after it meets antigen, and [7.15.24](/7.15.24) puts the test for self-reactivity introduced here into the overall framework of immunological tolerance.

## 19.1. Sites and Microenvironments of Development

In mammals, B cells first arise in the fetal liver; after birth they are produced throughout life in the bone marrow from **hematopoietic stem cells** by way of **common lymphoid progenitors**. In birds, B cells develop in the bursa of Fabricius, which gave the "B" its name. Mature B cells leave the bone marrow and settle in the lymphoid follicles of the **lymph nodes**, the **spleen** and mucosal lymphoid tissues ([7.15.3](/7.15.3)).

Development depends on several kinds of signals from bone marrow stromal cells, which act at different stages:

| Signal | Source and receptor | Function |
|---|---|---|
| CXCL12 | Stromal cell → CXCR4 | Retains the earliest progenitors in the bone marrow niche |
| SCF (stem cell factor) | Stromal cell membrane → c-Kit (CD117) | Proliferation of early progenitors |
| IL-7 | Stromal cell → IL-7R (contains the **common γ chain**) | Survival and proliferation of pro-B and large pre-B cells (essential in the mouse, dispensable in humans) |
| VCAM-1 | Stromal cell → VLA-4 (integrin α4β1) | Adhesion to the stroma, which allows the cell to receive the signals above |

Inside the cell, a series of transcription factors commits it to the B lineage in turn. E2A and EBF1 switch on B-cell genes and make the D and $J_{\mathrm{H}}$ segments of the heavy-chain locus accessible. PAX5 is the master switch of the B lineage: it activates B-cell genes such as CD19 and Igα and at the same time shuts off genes of the T lineage and other lineages, such as Notch1. PAX5 and EBF1 promote each other's expression in a positive feedback loop, so once the lineage is determined it is not reversed (the logic of this bistability is discussed in [7.9.16](/7.9.16)). PAX5 stays expressed until the B cell differentiates into a plasma cell.

## 19.2. Stages of Development in the Bone Marrow and the Two Checkpoints

The stages of B-cell development are defined by two things: how far rearrangement of the antigen-receptor genes has proceeded, and whether the cell has a receptor on its surface. The heavy chain is rearranged before the light chain, and after each chain is completed the cell must assemble a receptor with it and receive its signal before it can enter the next stage.

![Stages of B-cell development. From left to right: common lymphoid progenitor (CLP), pre-pro-B, pro-B, large pre-B, small pre-B, immature B, transitional B (T1 → T2) and mature naive B cells; the first six stages occur in the bone marrow and the last two in the spleen. The rows give the state of the heavy-chain and light-chain genes (yellow: being rearranged; green: rearrangement complete), the surface receptor and the main markers. The two red dashed lines are the two checkpoints: a large pre-B cell must express a functional pre-BCR, and an immature B cell must express a complete IgM BCR and pass the test for self-reactivity; self-reactive immature B cells are dealt with by receptor editing, clonal deletion or anergy](./plots/b-cell-stages.py)

1. Pre-pro-B and pro-B cells: a cell enters the B lineage once it expresses B220 (CD45R). Early in the pro-B stage the cell completes D–$J_{\mathrm{H}}$ joining of the heavy chain; late in this stage, under the action of PAX5, it completes $V_{\mathrm{H}}$–$DJ_{\mathrm{H}}$ joining (**V(D)J recombination**; RAG1/RAG2 and TdT are expressed at this stage). The cell already expresses Igα, Igβ and CD19 but has no receptor yet.
2. Large pre-B cells: a cell whose heavy-chain rearrangement has succeeded synthesizes the μ chain.

**Definition 19.2.1 (Pre-B Cell)** A cell of the B lineage that has completed VDJ rearrangement of the heavy chain, expresses the μ heavy chain in the cytoplasm and on the surface, and has not yet rearranged its light-chain genes is called a **pre-B cell**. Its surface μ chain pairs with the surrogate light chain (composed of the two polypeptides VpreB and λ5) and, together with Igα/Igβ, forms the **pre-BCR** (pre-B-cell receptor).

The pre-BCR needs no ligand: VpreB and λ5 each carry an additional peptide segment, and the opposite charges of these segments make the pre-BCR aggregate spontaneously in the membrane and signal. This signal is the first checkpoint, and it has three consequences:

- The cell survives and proliferates for 2–7 rounds (large pre-B cells). All the daughter cells share the same heavy chain and then each rearranges a light chain on its own, so that one successful heavy-chain rearrangement can be combined with many different light chains, which enlarges the repertoire;
- RAG is transiently downregulated, TdT disappears and the chromatin of the other heavy-chain allele is closed, which ensures **allelic exclusion**: a B cell expresses only one heavy-chain allele;
- When proliferation ends the cell becomes smaller (small pre-B cell), expresses RAG again and begins V–J rearrangement of the light chain.

A cell whose heavy-chain rearrangement fails cannot assemble a pre-BCR and undergoes apoptosis at this stage. Deficiency of the human surrogate light chain (λ5) arrests B-cell development at the pro-B stage and causes an antibody deficiency with almost no B cells ([7.15.31](/7.15.31)).

3. Small pre-B cells: the light chains are rearranged in order. In the mouse the κ chain is rearranged first; if one κ allele fails the other is tried, and λ is rearranged only if both fail. In humans the initiation of κ and λ is more random, but κ still predominates (about 2:1 in humans and about 20:1 in the mouse). The light-chain loci permit "secondary rearrangement": a V segment upstream of the rearranged VJ joins a J segment downstream, deleting the original junction, so each locus can make more than one attempt. TdT is scarcely present at the small pre-B stage, so light-chain junctions rarely contain N nucleotides.

**Definition 19.2.2 (Immature B Cell)** A B cell that has successfully rearranged a light chain and expresses a complete mIgM on its surface (but not yet mIgD) is called an **immature B cell**. The tonic signal of the complete BCR shuts off RAG and stops light-chain rearrangement; this is the **second checkpoint**. A cell that fails to produce a functional light chain from any of the four light-chain loci undergoes apoptosis.

**Example 19.2.1 (Success Rate of Rearrangement)** The junctions of rearrangement are imprecise ([7.15.12](/7.15.12)), and the probability that the downstream J segment stays in the original reading frame after joining is about $p = 1/3$. Ignoring stop codons and pseudogenes, treat each rearrangement as an independent trial with success probability $p$:

- Heavy chain: allele 1 is tried first and, if it fails, allele 2. The probability that the cell passes the first checkpoint is

  $$
  p + (1 - p)p = \frac{5}{9} \approx 0.56;
  $$
  the other $4/9$ of pro-B cells die. Among the survivors, the fraction in which allele 1 failed and allele 2 succeeded is

  $$
  \frac{(1-p)p}{p + (1-p)p} = \frac{2}{5} = 0.4,
  $$
  that is, about 40% of mature B cells have VDJ rearrangements on both heavy-chain alleles (one of them nonproductive), while in the rest the other allele remains in the DJ configuration. This prediction is close to the proportions measured in single cells, which supports the model of allelic exclusion in which alleles are tried in turn and trying stops at the first success.
- Light chain: there are two κ loci and two λ loci, and each locus can be tried $m$ times, so the probability of obtaining a functional light chain is $1 - (1-p)^{4m}$; it is 0.80 for $m = 1$ and already 0.96 for $m = 2$. Secondary rearrangement therefore allows the vast majority of cells that passed the first checkpoint to pass the second as well.

![A discrete probability model of the success rate of heavy-chain and light-chain rearrangement (probability $p = 1/3$ that each joint preserves the reading frame). A: proportions of the three outcomes when the two heavy-chain alleles are tried in turn: allele 1 succeeds (1/3), allele 1 fails and allele 2 succeeds (2/9), both fail and the cell dies (4/9); bars are exact values, circles are the results for 200,000 simulated cells. B: probability of obtaining a light chain when each of the four light-chain loci is tried $m$ times (solid line); the probability with only the two κ loci (dashed line); and the overall output of bone marrow development after multiplying by the heavy-chain survival rate 5/9 (dotted line)](./plots/rearrangement-odds.py)

This calculation is a direct application of the binomial and geometric distributions in biology ([3.1](/3.1)). It also shows how wasteful B-cell development in the bone marrow is: the mouse bone marrow produces about $2 \times 10^7$ immature B cells per day, of which only about 10% enter the peripheral mature pool. Part of the loss comes from nonproductive rearrangements, and a larger part from the selection described in the next section and from competition in the periphery.

:::

## 19.3. Testing for Self-Reactivity and Peripheral Maturation

Rearrangement is random, and a considerable fraction of the BCRs it produces can bind **autoantigens**. Immature B cells respond to BCR signals in the opposite way to mature cells: the same cross-linking that activates a mature B cell causes arrest or apoptosis in an immature one (which expresses little of the antiapoptotic proteins Bcl-2 and Bcl-xL). This makes the bone marrow the place where self-reactivity is tested. Depending on the form of the self antigen and the strength of the BCR signal, there are four outcomes:

| Self antigen encountered | BCR signal | Outcome |
|---|---|---|
| Multivalent, membrane-bound (such as molecules on the surface of stromal cells) | Strong cross-linking | RAG is expressed again and the light chain undergoes **receptor editing**; if editing still fails, the cell undergoes apoptosis (**clonal deletion**) |
| Soluble, monovalent | Weak but persistent | **Clonal anergy**: mIgM is downregulated, and in the periphery the cell has a short life span and does not respond to antigen |
| Very low concentration, or absent from the bone marrow | None | The cell matures as usual and is left to peripheral mechanisms |
| None | Normal tonic signal | Normal maturation |

Nemazee and Bürki (1989) provided direct evidence for this mechanism with transgenic mice: all B cells expressed a transgenic BCR recognizing the MHC class I molecule $\mathrm{H\text{-}2K^k}$. In mice that did not express $\mathrm{K^k}$, these B cells appeared normally in the periphery and the serum contained about $93\,\mu\mathrm{g\,mL^{-1}}$ of the transgenic antibody; in mice that expressed $\mathrm{K^k}$, there were almost no such B cells in the periphery and the serum antibody was below the detection limit ($< 0.3\,\mu\mathrm{g\,mL^{-1}}$). Further analysis showed that the residual B cells had kept the transgenic heavy chain but had exchanged the light chain for a new endogenous one, that is, receptor editing had occurred. It is now believed that elimination of self-reactivity in the bone marrow relies mainly on receptor editing, with apoptosis as a backup when editing fails. This test is part of **central tolerance**, discussed in detail in [7.15.24](/7.15.24).

Immature B cells that pass the test leave the bone marrow by responding to sphingosine-1-phosphate in the blood through S1P receptors, and complete their final maturation in the spleen:

1. Transitional B cells (T1 → T2): T1 cells are still sensitive to BCR cross-linking, and self-reactive T1 cells are eliminated further in the spleen; T2 cells begin to express IgD, CD21, CD23 and the BAFF receptor (BAFF-R).
2. Mature naive B cells: through alternative splicing they express mIgM and mIgD simultaneously (the two have the same variable region and differ only in the constant region), lose transitional markers such as CD24 and CD93, and become recirculating follicular B cells.

Survival of peripheral B cells depends on binding of BAFF (B-cell activating factor, a member of the TNF family) to BAFF-R and on the tonic signal of the BCR. The amount of BAFF is limited and transitional cells compete for it; self-reactive cells, whose BCR signals are abnormal, compete poorly and are eliminated. Conversely, when BAFF is in excess, self-reactive B cells can also survive: BAFF-transgenic mice develop autoimmunity resembling **systemic lupus erythematosus**, and anti-BAFF antibody is therefore used to treat this disease ([7.15.28](/7.15.28)).

## 19.4. The BCR Complex and Coreceptor

**Definition 19.4.1 (BCR Complex)** The multisubunit complex on the surface of a B cell that recognizes antigen and transmits signals is called the **BCR complex**. It consists of membrane immunoglobulin (mIg), which recognizes antigen, and the Igα/Igβ heterodimer (CD79a/CD79b), which transmits the signal; the two are associated noncovalently.

The two parts of the **B-cell receptor** have a clear division of labor. The cytoplasmic tail of mIg has only three amino acids (KVK) and cannot transmit a signal by itself. Igα and Igβ belong to the **immunoglobulin superfamily**; each has one extracellular Ig-like domain, a transmembrane region and a cytoplasmic region containing an **immunoreceptor tyrosine-based activation motif** (ITAM). After antigen cross-links several BCRs, the signal is transmitted in the following order:

1. The Src-family kinase Lyn phosphorylates the ITAM tyrosines of Igα/Igβ;
2. The doubly phosphorylated ITAM recruits and activates Syk;
3. Syk phosphorylates the adaptor protein BLNK, which brings BTK and PLCγ2 together;
4. PLCγ2 hydrolyzes $\mathrm{PIP_2}$ to produce $\mathrm{IP_3}$ (which raises calcium and activates NFAT) and DAG (which activates PKC and, through it, **NF-κB**), and the Ras–ERK pathway is activated at the same time.

BTK deficiency arrests B-cell development at the pre-B stage (the pre-BCR uses the same pathway) and causes **X-linked agammaglobulinemia**; BTK inhibitors are also targeted drugs for B-cell malignancies. The overall structure of this pathway is homologous to that of T-cell receptor signaling ([7.15.16](/7.15.16)): the recognition chains and the ITAM chains are separate, and the signal passes in turn through a Src-family kinase, a Syk-family kinase, an adaptor protein and PLCγ.

**Definition 19.4.2 (B-Cell Coreceptor)** The complex that consists of CD21 (complement receptor 2, CR2), CD19 and CD81 (a tetraspanin), is engaged together with the BCR when it recognizes antigen, and enhances BCR signaling is called the **B-cell coreceptor**.

The coreceptor links the "tag" of the **complement** system to recognition by the B cell. The surface of an antigen tagged by complement activation carries covalently bound C3d ([7.15.10](/7.15.10)); when one epitope of the antigen binds the BCR and C3d binds CD21, the coreceptor is brought next to the BCR. After phosphorylation, the long cytoplasmic tail of CD19 recruits PI3K, which produces $\mathrm{PIP_3}$ and activates Akt, and also helps to recruit BTK. Co-ligation can lower the amount of antigen needed to activate a B cell by more than 100-fold; in the mouse, an antigen linked to two or three copies of C3d is three to four orders of magnitude more immunogenic than the same antigen without C3d, and C3d is therefore called a "natural molecular **adjuvant**". CD21 is also the receptor through which Epstein–Barr virus enters B cells.

![The BCR complex and coreceptor. Membrane IgM recognizes antigen with its two antigen-binding sites; Igα (CD79a) and Igβ (CD79b), associated with it noncovalently, each carry one ITAM (short red bars). The surface of a complement-tagged antigen carries C3d, which binds CD21 (complement receptor 2, made up of a chain of short consensus repeats) and so links the CD21–CD19–CD81 coreceptor and the BCR through the same antigen. Below the membrane: Lyn phosphorylates the ITAMs, Syk is recruited and activated, BTK and PLCγ2 are activated through the adaptor BLNK, producing $\mathrm{IP_3}$ (calcium signal, NFAT) and DAG (PKC, NF-κB), and Ras–ERK is activated; CD19 recruits PI3K, which produces $\mathrm{PIP_3}$ and activates Akt, and $\mathrm{PIP_3}$ also recruits BTK to the membrane. The result is proliferation, survival and antigen uptake](./plots/bcr-complex.py)

BCR signaling is also negatively regulated: the cytoplasmic regions of CD22 (a sialic acid-binding lectin) and of the inhibitory Fc receptor FcγRIIB contain an immunoreceptor tyrosine-based inhibitory motif (ITIM), which recruits the phosphatases SHP-1 and SHIP and counteracts the kinases. When FcγRIIB is co-engaged with the BCR by an antigen–IgG complex, it tells the B cell that "enough specific antibody has been made", a negative feedback of antibody on its own production ([7.15.21](/7.15.21), [7.15.25](/7.15.25)).

## 19.5. Surface Molecules of B Cells

The surface molecules of B cells fall into five functional groups. The molecules in the table below are the ones most commonly used in immunophenotyping and as pathological markers (a systematic summary of markers is given in [7.15.35](/7.15.35)).

| Function | Molecules | Key points |
|---|---|---|
| Antigen recognition and signaling | mIgM, mIgD; CD79a/CD79b | Mature naive B cells are IgM⁺IgD⁺; memory B cells after class switching express IgG, IgA or IgE; plasma cells essentially no longer express membrane Ig |
| Coreceptors | CD19, CD21, CD81 | CD19 is expressed from the pro-B cell to the plasmablast and is the most reliable B-lineage marker in flow cytometry; CD21 binds C3d and is highly expressed on FDCs |
| Interaction with T cells | CD40; CD80/CD86 (B7); MHC class II molecules; ICAM-1 | CD40 is constitutively expressed and binds CD40L on activated T cells, the most important second signal for B-cell activation; B7 is upregulated after B-cell activation |
| Negative regulation | CD22, FcγRIIB (CD32B), CD72 | The cytoplasmic regions contain ITIMs |
| Survival and localization | BAFF-R, TACI, BCMA; CXCR5, CCR7, S1PR1 | BAFF-R maintains the survival of naive B cells and BCMA that of plasma cells; CXCR5 guides B cells to the follicles |
| Stage and subset | CD20, CD5, CD23, CD27, CD38, CD138 | CD20 is expressed from the pre-B to the memory B cell but not on plasma cells (anti-CD20 antibody therefore depletes B cells while sparing existing long-lived plasma cells); human CD27 marks memory B cells; CD38 and CD138 are highly expressed on plasma cells |

The general nomenclature and functional families of CD molecules are described in [7.15.4](/7.15.4).

## 19.6. B-Cell Subsets

Peripheral B cells are not a homogeneous population; according to origin, site of residence and mode of response they fall into three major subsets.

**Definition 19.6.1 (Follicular B Cell)** A B cell that is produced throughout life from hematopoietic stem cells in the bone marrow, matures through the transitional stage, recirculates between the blood and the lymphoid follicles of secondary lymphoid organs, and mainly mounts T-cell-dependent responses to thymus-dependent antigens is called a **follicular B cell**, also known as a B-2 cell.

**Definition 19.6.2 (Marginal Zone B Cell)** A B cell that resides in the marginal zone at the outer edge of the splenic white pulp, expresses high levels of IgM and CD21 and low levels of IgD and CD23, and responds rapidly to antigens arriving through the blood is called a **marginal zone B cell**.

**Definition 19.6.3 (B-1 Cell)** A B cell that arises early in ontogeny from embryonic progenitors, is found mainly in the peritoneal and pleural cavities, renews itself in the periphery, and has a restricted receptor repertoire biased toward conserved polysaccharide and lipid antigens is called a **B-1 cell**; in the mouse it is divided by the presence or absence of CD5 into B-1a (CD5⁺) and B-1b (CD5⁻).

| | Follicular B (B-2) | Marginal zone B | B-1 |
|---|---|---|---|
| Origin | Bone marrow hematopoietic stem cells, produced throughout life | Bone marrow hematopoietic stem cells, differentiating from T2 cells (requires Notch2 signaling and a stronger BCR signal) | B-1a arise from embryonic progenitors (earlier than hematopoietic stem cells) and then renew themselves in the periphery |
| Location | Lymphoid follicles, recirculating | Splenic marginal zone, essentially nonrecirculating | Peritoneal and pleural cavities; also in the spleen and intestinal lamina propria |
| Repertoire | Diverse, many N nucleotides | Biased toward specificities cross-reactive with self and microbes | Restricted, oligoclonal, few N nucleotides |
| Main antigens | Protein (TD antigens) | Blood-borne polysaccharides and proteins | Polysaccharides, phospholipids (such as phosphatidylcholine), bacterial cell wall components |
| T-cell help | Required | Partly not required | Essentially not required |
| Products | High-affinity antibody after affinity maturation and class switching; memory cells | Early IgM and some IgG, appearing within days | **Natural antibody** (present without immunization, mainly IgM) |
| Position | Mainstay of adaptive immunity | Between innate and adaptive immunity | Between innate and adaptive immunity |

"Natural antibody" means antibody that is secreted continuously without obvious immunization and binds conserved epitopes broadly with low affinity (mainly IgM). The natural antibodies produced by B-1 cells bind "altered self" such as apoptotic cells and oxidized lipids, help to clear cell debris, and also form the first line of humoral defense against some bacteria. B-1 cells are well characterized in the mouse; the phenotype of human B-1-like cells and whether they form a separate lineage remain controversial.

B cells can also be classified from other angles, which cut across the table above:

- By stage of activation: **naive lymphocytes** (naive B cells that have not met antigen), the effector B cell or **plasma cell**, and the **memory B cell** ([7.15.20](/7.15.20));
- By BCR isotype: mIgM⁺ B cells (immature and naive B cells) and B cells that have class-switched to mIgG⁺, mIgA⁺ and mIgE⁺;
- By function: regulatory B cells (Bregs) are not a separate lineage but a state of B cells that secrete IL-10, IL-35 or TGF-β and suppress inflammation (enriched among B10 cells, which are CD1d-high and CD5⁺ in the mouse, and among transitional B cells that are CD24-high and CD38-high in humans).

## 19.7. Functions of B Cells and B-Cell Malignancies

B cells have three functions:

1. Production of antibody, which mediates **humoral immunity**. This is the most important function of B cells and is carried out by the plasma cells they differentiate into ([7.15.20](/7.15.20), [7.15.21](/7.15.21)).
2. Presentation of antigen. B cells capture antigen specifically with the BCR, internalize and process it, and present it as peptide–MHC class II complexes to CD4⁺ T cells. Because the BCR concentrates antigen inside the cell, at low antigen concentrations B cells present specific antigen several orders of magnitude more efficiently than by nonspecific uptake; this is the molecular basis on which T cells can "help the B cell that recognizes the same antigen" (**antigen presentation**, [7.15.14](/7.15.14)).
3. Secretion of cytokines and regulation of immunity. Activated B cells secrete IL-6, TNF-α, lymphotoxin and other cytokines, which take part in maintaining the structure of lymphoid follicles and in regulating other immune cells; Bregs secrete IL-10 to suppress inflammation.

Malignant transformation can occur at every stage of B-cell development and response, so **leukemias** and **lymphomas** derived from B cells often retain features of the stage at which they arose: the state of rearrangement and mutation, surface molecules and localization (for the general biology of tumors see [7.3.26](/7.3.26)).

| Stage of origin | Example of tumor | Features retained |
|---|---|---|
| Pro-B, pre-B cells | B-lymphoblastic leukemia (B-ALL) | Bone marrow localization, TdT⁺, CD19⁺, often no surface Ig |
| Naive B cell | Mantle cell lymphoma | CD5⁺, V regions mostly unmutated |
| Germinal center B cell | Follicular lymphoma, Burkitt lymphoma, most diffuse large B-cell lymphomas | BCL6⁺, somatic mutations in V regions; off-target action of AID and the breaks of class switching allow oncogenes to be translocated to Ig loci (for example t(14;18) places *BCL2*, and t(8;14) places *MYC*, under the IgH enhancer) |
| Memory-like or B-1-like cell | Chronic lymphocytic leukemia | CD5⁺CD23⁺ |
| Plasma cell | Multiple myeloma | CD138⁺, CD20⁻, secretion of monoclonal immunoglobulin, bone marrow localization |

Each tumor clone derives from a single B cell and therefore carries the same V(D)J rearrangement; measuring the clonality of rearrangement (all cells share one rearrangement) is a common way to distinguish a tumor from reactive hyperplasia.

## Summary

- The main line of development: in the bone marrow the genes are rearranged in the order heavy chain first, light chain second, and after each chain is completed a receptor must be assembled and its signal received.

  | Stage | Heavy chain | Light chain | Surface receptor | Key events |
  |---|---|---|---|---|
  | Pro-B | D–J → V–DJ | Germline | None | PAX5 commits the lineage; RAG, TdT |
  | Large pre-B | VDJ | Germline | Pre-BCR (μ + VpreB/λ5) | Checkpoint 1: survival, proliferation, heavy-chain allelic exclusion |
  | Small pre-B | VDJ | V–J | None | Light chains rearranged in turn; secondary rearrangement possible |
  | Immature B | VDJ | VJ | IgM | Checkpoint 2; test for self-reactivity (editing, deletion, anergy) |
  | Transitional B (spleen) | VDJ | VJ | IgM, IgD begins | BAFF competition, further elimination of self-reactivity |
  | Mature naive B | VDJ | VJ | IgM + IgD | Recirculation |

- Probability: the probability that each joint preserves the reading frame is about 1/3, the survival rate when the two heavy-chain alleles are tried in turn is 5/9, and about 40% of the survivors have rearranged both alleles (Example 19.2.1); the four light-chain loci and secondary rearrangement push the pass rate of the second checkpoint above 90%.
- **BCR complex** (Definition 19.4.1): mIg recognizes, the ITAMs of Igα/Igβ transmit the signal, Lyn → Syk → BLNK/BTK → PLCγ2; the **B-cell coreceptor** (Definition 19.4.2) links the complement tag to the BCR through C3d–CD21 and lowers the activation threshold; CD22 and FcγRIIB regulate negatively through ITIMs.
- Subsets (Definitions 19.6.1–19.6.3): follicular B cells produce T-cell-dependent antibody that undergoes affinity maturation; marginal zone B and B-1 cells have restricted repertoires, respond quickly, are mostly T-cell independent and produce natural antibody.
- Functions: production of antibody, presentation of antigen, secretion of cytokines; B-cell tumors retain the rearrangement, mutation and phenotype of the stage of origin.

## Questions

1. If every V(D)J joint were precise, with no addition or deletion of nucleotides, how would the conclusions of Example 19.2.1 change? Why does the immune system accept the death of 4/9 of pro-B cells rather than give up imprecise joining?

   **Answer** With precise joining, the reading frame would be determined by the sequence of the segments, each joint could be designed to be in frame, and the survival rate would be close to 1. But then the junctions would have no N or P nucleotides and no nucleotides would be trimmed, so **junctional diversity** would vanish, and CDR3 (the heavy-chain CDR3 spans exactly the V–D–J junction) is the most variable part of the antigen-binding site and contributes most to specificity. The size of the repertoire would shrink by several orders of magnitude. The loss from nonproductive rearrangements is the price paid for junctional diversity; the first checkpoint lets the cell confirm that the heavy chain is usable before investing in light-chain rearrangement, so the price does not spread downstream.

2. Why can the pre-BCR signal without binding a ligand? What problem would arise if it needed a ligand?

   **Answer** The role of the pre-BCR is to test whether this μ chain can fold, pair with a light-chain-like molecule and reach the cell surface, not to test specificity. The additional peptides of VpreB and λ5 cover the heavy-chain CDR3 and carry opposite charges, so the pre-BCR aggregates spontaneously and signals; every structurally competent heavy chain can therefore pass the checkpoint, regardless of its specificity. If a ligand were required, only heavy chains that happened to bind some ligand in the bone marrow could pass, and the repertoire would be severely narrowed, before the light chain is even added, by a ligand unrelated to future antigens.

3. Anti-CD20 monoclonal antibody can deplete almost all B cells from the blood, yet the titers of a patient's existing protective antibodies often change little over several months. Use the table of surface molecules in this chapter to explain this, and say what it means for vaccinating a person receiving this treatment with a new vaccine.

   **Answer** CD20 is expressed from the pre-B to the memory B cell, whereas plasma cells (especially **long-lived plasma cells** in the bone marrow) do not express CD20, so what is depleted are B cells and not the cells that are secreting antibody; existing antibody is maintained by long-lived plasma cells, so titers do not change in the short term. By contrast, a response to a new antigen requires naive B cells to be activated and to differentiate into new plasma cells; during treatment these precursors have been depleted, so the antibody response to a new vaccine will be weak, and vaccination should be given before treatment or after B cells have recovered.

4. In Nemazee's transgenic experiment, suppose the BCR recognizing $\mathrm{K^k}$ were replaced by one recognizing a protein expressed only in hepatocytes and not entering the blood. What would you expect to happen to these B cells in the bone marrow? And in the periphery?

   **Answer** This self antigen is absent from the bone marrow, so the BCR provides only the tonic signal; the immature B cells are not edited or deleted and mature as usual into the periphery, which is the situation of **immunological ignorance**. In the periphery, as long as the antigen remains sequestered at low concentration and there is no T-cell help (the corresponding self-reactive T cells have usually been deleted in the thymus), these B cells remain inactive; if tissue damage releases the antigen in large amounts and there are inflammation and T-cell help at the same time, they may be activated, which is the problem the peripheral tolerance mechanisms must deal with ([7.15.24](/7.15.24)).

5. Why might the "restricted" repertoire of B-1 cells be an advantage?

   **Answer** B-1a cells are produced in the embryo, when TdT expression is very low and few N nucleotides are added at the junctions, so the repertoire is biased toward a few V segment combinations conserved in evolution; these combinations recognize conserved structures, such as phosphatidylcholine and bacterial polysaccharides, that are shared by many microbes and also appear on apoptotic cells. The result is a "prefabricated" repertoire that needs no prior immunization and can supply large amounts of IgM in the first days of an infection, functionally close to pattern recognition. The cost is that these cells can hardly make high-affinity antibody against new epitopes, which is made up for by the diverse repertoire of follicular B cells.
