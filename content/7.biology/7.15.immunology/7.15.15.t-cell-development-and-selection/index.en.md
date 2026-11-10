---
title: T-Cell Development and Selection
source_hash: 5f706876e1a2
---

The first question on the knowledge path is "who is recognizing?" Chapter [7.15.12](/7.15.12) explained how random rearrangement generates an almost unlimited number of TCRs, and chapters [7.15.13](/7.15.13) and [7.15.14](/7.15.14) described what the TCR is to recognize, the pMHC. Randomly generated TCRs have two problems: most cannot bind the individual's own MHC molecules at all and are therefore useless, and a few bind self pMHC too strongly and would attack the body's own tissues once in the periphery. The task of the **thymus** is to pick out of the random repertoire the small fraction that both "recognizes self MHC" and "does not react strongly to self," and this is positive and negative selection. This chapter follows the process in the order of thymocyte development and uses a simple Monte Carlo model to show how an "affinity window" produces both MHC restriction and self-tolerance. How peripheral T cells are activated is covered in [7.15.16](/7.15.16); the place of central tolerance among all tolerance mechanisms is covered in [7.15.24](/7.15.24).

## 15.1. The Thymus and Thymocytes

The precursors of T cells come from hematopoietic stem cells of the bone marrow ([7.15.2](/7.15.2)). Multipotent lymphoid precursors travel through the blood and enter the thymus near vessels at the corticomedullary junction (dependent on CCR7, CCR9 and the P-selectin ligand PSGL-1). The precursors themselves are not yet committed to the T-cell fate: what determines it is the activation of Notch1 by the Notch ligand DLL4 expressed on thymic epithelial cells, and precursors without Notch1 signaling develop into B cells in the thymus. IL-7 and stem cell factor maintain the survival and proliferation of early thymocytes.

**Definition 15.1.1 (Thymocyte)** Cells of the T-cell lineage that develop in the thymus and have not yet left it are called **thymocytes**.

**Definition 15.1.2 (Thymic Epithelial Cell)** The epithelial cells that make up the stromal scaffold of the thymus, express MHC molecules and present self peptides to thymocytes are called **thymic epithelial cells** (TECs), divided into cortical thymic epithelial cells (cTECs) and medullary thymic epithelial cells (mTECs). Both depend on the transcription factor FOXN1; FOXN1 deficiency prevents the thymus from forming (nude mice; in humans, T-cell deficiency with congenital alopecia).

Besides epithelial cells, the thymus contains dendritic cells, macrophages and a few B cells, located mainly in the medulla and at the corticomedullary junction. A major job of the macrophages is to clear the large numbers of apoptotic thymocytes: about 98% of double-positive thymocytes die in the thymus, and only about 2%–5% are exported as mature T cells (mouse data).

## 15.2. Stages of Thymocyte Development

The development of αβ T cells is divided into three major stages by the expression of CD4 and CD8: double negative (DN, CD4⁻CD8⁻), double positive (DP, CD4⁺CD8⁺) and single positive (SP, CD4⁺CD8⁻ or CD4⁻CD8⁺). Mouse DN cells are further divided into four substages by CD44 and CD25; human thymocytes are staged with CD34, CD7 and CD1a, but the order of events is the same.

| Stage | Mouse phenotype | Location | Main events |
|---|---|---|---|
| DN1 | CD44⁺CD25⁻ (c-Kit⁺) | Corticomedullary junction → cortex | Newly entered precursors, still multipotent |
| DN2 | CD44⁺CD25⁺ | Deep cortex | Commitment to the T-cell fate under Notch signaling; RAG expressed, rearrangement of TCRβ, γ, δ begins |
| DN3 | CD44⁻CD25⁺ | Subcapsular zone | Bifurcation of the αβ and γδ lineages; β selection: a functional β chain and pTα form the pre-TCR |
| DN4 | CD44⁻CD25⁻ | Subcapsular zone → cortex | Pre-TCR signaling drives extensive proliferation, RAG temporarily shut off |
| DP | CD4⁺CD8⁺ | Cortex | RAG expressed again, TCRα rearranged, αβTCR expressed at the surface; positive selection |
| SP | CD4⁺ or CD8⁺ | Medulla | Negative selection (tissue-restricted antigens), maturation, export |

![Developmental stages of αβ T cells in the mouse thymus. Precursors enter the thymus at the corticomedullary junction, migrate toward the subcapsular zone through the DN1–DN4 stages, return to the cortex at the DP stage, where they undergo positive selection on cTECs, and enter the medulla at the SP stage, where they undergo negative selection before export. The table below lists the surface molecules and the state of gene rearrangement at each stage: CD44 and CD25 define DN1–DN4; TCRβ rearranges at DN2–DN3, and the pre-TCR of DN3 (β chain + pTα) emits the β-selection signal; TCRα rearranges at the DP stage, when the αβTCR first appears at the surface; RAG is expressed twice, at DN2–DN3 and at the DP stage](./plots/thymocyte-stages.py)

### 15.2.1. β Selection and the Pre-TCR

The TCR β-chain locus rearranges first (at the DN2–DN3 stages, D–J first and then V–DJ). Whether a usable β chain has been obtained is tested by a checkpoint:

**Definition 15.2.1 (Pre-TCR)** The receptor composed of a functional TCRβ chain, the invariant pre-Tα chain (pTα) and CD3 is called the **pre-TCR**. It does not need to recognize a ligand; by oligomerizing on its own it signals constitutively.

Signaling from the pre-TCR (through Lck and ZAP-70, the same pathway as the mature TCR) causes DN3 cells to:

1. survive and proliferate extensively (several divisions), expanding the cells that carry a functional β chain;
2. stop rearrangement of the β chain on the other allele, achieving **allelic exclusion** of the β chain ([7.15.12](/7.15.12));
3. express CD4 and CD8 and enter the DP stage;
4. re-express RAG afterward and begin α-chain rearrangement.

DN3 cells that cannot produce an in-frame β chain undergo apoptosis. Each β-chain rearrangement has only about a one-in-three chance of the correct reading frame, and the probability that both alleles fail is not small, which is why β selection eliminates a large number of cells. The γδ and αβ lineages diverge at the DN2–DN3 stages: strong, sustained γδTCR signaling favors the γδ lineage and weaker pre-TCR signaling favors the αβ lineage (the signal-strength model).

### 15.2.2. α-Chain Rearrangement

The TCRα locus has about 70 Vα and about 61 Jα segments. α-chain rearrangement can proceed repeatedly: when the first V–J joining cannot produce a TCR that can be selected, an upstream Vα and a downstream Jα rearrange again, deleting the segment in between, and several attempts can be made within the roughly 3–4-day life span of a DP cell; this is a kind of receptor editing in the thymus. Allelic exclusion of the α chain is incomplete, and a few mature T cells express two α chains. The δ-chain locus is embedded within the α locus and is deleted during α-chain rearrangement, so a cell that has completed α rearrangement can no longer become a γδ T cell.

## 15.3. Positive Selection

DP thymocytes expressing αβTCR at the surface contact cTECs in the cortex and "browse" the self pMHC on the cTECs.

**Definition 15.3.1 (Positive Selection)** When the TCR of a DP thymocyte recognizes, with low affinity, a self peptide–MHC complex presented by a thymic cortical epithelial cell, the thymocyte receives signals for survival and continued differentiation; this process is called **positive selection**. Positive selection gives mature T cells their self **MHC restriction** (Definition 13.6.1).

**Definition 15.3.2 (Death by Neglect)** DP thymocytes whose TCR cannot bind any self pMHC effectively receive no survival signal and undergo apoptosis within 3–4 days; this is called **death by neglect**. It is the main cause of thymocyte death, accounting for more than 90% of DP thymocytes.

The survival signal induces the antiapoptotic proteins Bcl-2 and Bcl-xL through the ERK pathway downstream of the TCR and at the same time inhibits the proapoptotic protein Bim, which is highly expressed in DP cells. Evidence for positive selection comes from bone marrow chimeric mice: when bone marrow from $H\text{-}2^{a\times b}$ hybrid mice is transplanted into a recipient whose thymus is only $H\text{-}2^a$, the T cells that develop recognize only antigen presented by $H\text{-}2^a$; that is, T cells are restricted by the MHC of the thymic epithelium and not by the T cells' own MHC.

cTECs have special processing machinery for positive selection: the thymoproteasome (β5t, [7.15.14](/7.15.14)), cathepsin L and the serine protease PRSS16 generate a "private" set of self peptides different from that of other cells. One explanation is that if positive selection and the subsequent negative selection used exactly the same peptides, the cells that were positively selected would be exactly those reacting most strongly to these peptides and would easily be deleted in negative selection; the unique peptide repertoire of cTECs reduces this overlap and increases the diversity of the repertoire. β5t-deficient mice have markedly fewer CD8⁺ T cells.

## 15.4. CD4/CD8 Lineage Commitment

A positively selected DP cell eventually keeps only one coreceptor, and which one it keeps matches the MHC class of its TCR: cells recognizing MHC class II molecules become CD4⁺, and those recognizing MHC class I molecules become CD8⁺. Mice and patients lacking MHC class II molecules (or CIITA) have almost no CD4⁺ T cells, and mice lacking β2m (and therefore class I molecules) have almost no CD8⁺ T cells.

The lineages are executed by two mutually antagonistic transcription factors: ThPOK (*Zbtb7b*) determines the CD4 lineage, and RUNX3 determines the CD8 lineage. The better-supported account is the kinetic signaling model (Singer):

1. At the start of positive selection, a DP cell first downregulates CD8 and becomes an intermediate CD4⁺CD8^lo cell, regardless of which class its TCR is restricted to;
2. If the TCR is MHC II-restricted, CD4 is still present, signaling continues, ThPOK is induced, and the cell becomes a CD4⁺ SP cell;
3. If the TCR is MHC I-restricted, the downregulation of CD8 interrupts the signal; the interruption makes the cell sensitive to IL-7, and IL-7 signaling induces RUNX3, which silences *Cd4* and re-expresses *Cd8* ("coreceptor reversal"), and the cell becomes a CD8⁺ SP cell.

What determines the lineage is therefore not which class of MHC the TCR recognizes in itself, but the duration of TCR signaling. Cells of the CD4⁺ lineage can be further divided into conventional helper T-cell precursors and regulatory T cells (§15.7).

## 15.5. Negative Selection

**Definition 15.5.1 (Negative Selection)** When the TCR of a thymocyte recognizes, with high affinity, a self peptide–MHC complex presented in the thymus, the thymocyte is induced to undergo apoptosis (**clonal deletion**) or is diverted to another fate (regulatory T cell, anergy); this process is called **negative selection**. Negative selection is the main mechanism of **central tolerance**.

Negative selection takes place in two places:

- Cortex: DP cells can be deleted when they meet widely expressed self antigens (presented by cTECs, cortical DCs and macrophages); this part is often underestimated;
- Medulla: SP cells stay in the medulla for about 4–5 days and are tested repeatedly on mTECs and DCs, which deletes the cells that react to tissue-restricted antigens.

High-affinity signals induce apoptosis through the mitochondrial pathway by way of Nur77 and Bim (the **intrinsic pathway** of apoptosis, [7.3.25](/7.3.25)).

A key question is how the thymus presents proteins expressed only in peripheral tissues such as the pancreatic islets, the thyroid and the retina. The answer is the "promiscuous gene expression" of mTECs:

**Definition 15.5.2 (Autoimmune Regulator)** The **autoimmune regulator** (AIRE) is a transcriptional regulatory protein expressed mainly in medullary thymic epithelial cells. It binds poorly active chromatin (histone H3 unmethylated at K4) and releases stalled RNA polymerase II, causing mTECs to express, at a low level, thousands of genes normally expressed only in peripheral tissues (tissue-restricted antigens, such as insulin).

Each mTEC expresses only a portion of the tissue-restricted antigens, and all mTECs together cover most of the peripheral self proteome. The transcription factor FEZF2 controls another set of tissue-restricted antigens independently of AIRE. mTECs can present these antigens directly or transfer them to medullary DCs for presentation; peripheral DCs that migrate into the thymus can also bring peripheral self antigens.

People with AIRE mutations develop autoimmune polyendocrinopathy–candidiasis–ectodermal dystrophy (APECED, also called autoimmune polyendocrine syndrome type 1), in which multiple endocrine glands come under autoimmune attack; patients also often have neutralizing autoantibodies against IL-17 and IL-22, which explains the chronic mucocutaneous candidiasis ([7.15.28](/7.15.28)). In mice, the expression level of insulin in the thymus is correlated with susceptibility to type 1 diabetes.

Negative selection is not perfect: some self antigens are not expressed in the thymus or are expressed too weakly, and some self-reactive T cells have an affinity just below the deletion threshold. Cells that escape negative selection are controlled by peripheral tolerance mechanisms (**peripheral tolerance**, [7.15.24](/7.15.24)).

## 15.6. The Affinity Window Model

Positive and negative selection use the same receptor and the same kind of ligand (self pMHC) yet produce opposite outcomes. The unifying explanation is the affinity window (more precisely, a window of signal strength):

| Thymocyte signal from self pMHC | Outcome |
|---|---|
| None or very weak | Death by neglect (Definition 15.3.2) |
| Weak (low affinity) | Positive selection (Definition 15.3.1), becoming a conventional T cell |
| Stronger (near the threshold) | Partly diverted to "agonist selection" lineages such as regulatory T cells and iNKT cells |
| Strong (high affinity) | Negative selection (Definition 15.5.1), clonal deletion |

The difference between thresholds is steep: in fetal thymic organ culture, a difference of only a few-fold in the affinity of the ligand met by the same TCR changes the outcome from positive to negative selection; the kinetics of ERK activation (slow and sustained for weak ligands, fast and strong for strong ligands) and the **kinetic proofreading** of TCR signaling ([7.15.16](/7.15.16)) both take part in this steep discrimination.

**Example 15.6.1 (Monte Carlo Model of the Affinity Window)** Suppose each DP thymocyte randomly receives one TCR, and the logarithm $x$ of the strongest self pMHC signal it meets in the thymus follows the standard normal distribution $\mathcal{N}(0,1)$ (arbitrary units). Take the thresholds $\theta_{+} = 1.405$, $\theta_{\mathrm{T}} = 1.74$, $\theta_{-} = 1.79$: for $x < \theta_+$ death by neglect, for $\theta_+ \le x < \theta_{\mathrm{T}}$ positive selection, for $\theta_{\mathrm{T}} \le x < \theta_-$ entry into the Treg lineage, and for $x \ge \theta_-$ negative selection. The thresholds are illustrative values, chosen so that the proportions of the outcomes agree in order of magnitude with those of the mouse thymus:

$$
\mathbb{P}(\text{neglect}) = \Phi(\theta_+) \approx 0.92,\quad
\mathbb{P}(\text{positive}) \approx 0.039,\quad
\mathbb{P}(\text{Treg}) \approx 0.004,\quad
\mathbb{P}(\text{negative}) = 1 - \Phi(\theta_-) \approx 0.037,
$$

where $\Phi$ is the standard normal distribution function ([3.1.5](/3.1.5)). About 4% of cells are exported, of which about 10% are Tregs. The model gives three qualitative conclusions:

1. The reactivity of the surviving repertoire to self pMHC is "truncated" to a narrow band: every mature T cell reacts weakly to self MHC (MHC restriction) and none reacts strongly (self-tolerance);
2. Because of the tail of the normal distribution, the number of cells in the positive selection window depends on the distance between the window and the negative threshold; when the window is narrow, a slight change in the threshold or in ligand density changes the output markedly;
3. When all signals are multiplied by the ligand density $d$ ($x \mapsto x + \log_{10} d$), nearly all cells die by neglect if $d$ is very small (low MHC expression) and negative selection increases sharply if $d$ is very large. This agrees with the loss of the corresponding T-cell subsets in MHC-deficient mice, and with experiments in which overexpressing a self antigen in the thymus deletes the T cells specific for it.

:::

![The affinity window of thymic selection (Monte Carlo model, illustrative thresholds). A: Maximum signal strength against self pMHC (logarithmic, standard normal distribution) for 400,000 DP thymocytes and their outcomes: gray death by neglect (about 92%), green positive selection (about 3.9%), blue entry into the Treg lineage (about 0.4%), red negative selection (about 3.7%); the vertical axis is logarithmic. B: Proportions of the outcomes when all signals are multiplied by the relative density $d$ of self pMHC; for $d < 1$ (reduced MHC expression) the selected cells fall rapidly, for $d > 1$ negative selection rises rapidly, and the dashed line is the total fraction of exported cells](./plots/affinity-window.py)

## 15.7. Development of Other T-Cell Lineages

**Regulatory T cells**: some CD4-lineage thymocytes, under a stronger (but below deletion) signal from self pMHC together with CD28 costimulation and IL-2, induce **FOXP3** and become thymus-derived regulatory T cells (tTregs). Their TCRs are biased toward recognition of self antigens, which is just what is needed to suppress responses against the same self antigens in the periphery ([7.15.17](/7.15.17), [7.15.24](/7.15.24)). By contrast, peripherally induced Tregs (pTregs) are generated from naive CD4⁺ T cells under the action of TGF-β and IL-2, mainly in the intestinal mucosa.

**γδ T cells** branch off at the DN2–DN3 stages (§15.2.1). The mouse fetal thymus produces successive "waves" using different Vγ segments, which settle in the epidermis (dendritic epidermal T cells), the reproductive tract, the lung and other sites, and many have already acquired the ability to secrete IFN-γ or IL-17 before leaving the thymus. Among human γδ T cells, Vγ9Vδ2 predominates in the blood (recognizing phosphoantigens, [7.15.14](/7.15.14)) and Vδ1 predominates in the tissues.

**NKT cells** (iNKT) are selected from DP thymocytes, but what selects them is not cTECs but CD1d with self glycolipids on the surface of other DP thymocytes; they express the transcription factor PLZF and are already effector-memory-like cells when they leave the thymus. **MAIT cells** are selected in a similar way by MR1 on DP thymocytes.

The precursors of CD8αα intraepithelial lymphocytes undergo "agonist selection" (high-affinity signals) in the thymus instead of being deleted, and then settle in the intestinal epithelium (**intraepithelial lymphocytes**, [7.15.23](/7.15.23)). What these lineages have in common is that a stronger self-reactive signal does not lead to death but is directed toward an innate-like fate in which effector functions are already in place.

## 15.8. Thymic Output and Peripheral Maturation

Mature SP thymocytes upregulate the S1P receptor S1PR1 (induced by the transcription factor KLF2) and leave the thymus along the high concentration of sphingosine-1-phosphate in blood and lymph; S1PR1 antagonists (such as fingolimod) retain lymphocytes in the lymphoid organs and are used to treat multiple sclerosis. Recent thymic emigrants still go through several weeks of functional maturation in the periphery.

T-cell receptor excision circles (TRECs) are circular DNA excised during TCR rearrangement that do not replicate with cell division, so their abundance in the T-cell pool reflects recent thymic output. Quantification of TRECs in newborn blood spots is used to screen for **severe combined immunodeficiency** ([7.15.31](/7.15.31)).

The survival of peripheral naive T cells depends on two signals: IL-7 and low-intensity self pMHC signals received through the TCR ("tonic" signals). These are the same kind of weak signals as those used in positive selection, showing that weak recognition of self MHC accompanies a T cell throughout its life.

The thymus is largest around birth and begins to involute after puberty: the epithelial spaces are replaced by adipose tissue, and output declines year by year. The adult pool of naive T cells is maintained mainly by slow proliferation of existing peripheral cells; the diversity of the TCR repertoire declines in older people, which is one of the causes of immunosenescence ([7.15.18](/7.15.18)). Adults who had the thymus removed in childhood (common in cardiac surgery) have fewer naive T cells and a narrower repertoire than their peers.

## Summary

- The thymus screens the random TCR repertoire into one that "recognizes self MHC and does not attack self." Notch1–DLL4 determines the T-cell fate, and FOXN1-dependent **thymic epithelial cells** (Definition 15.1.2) provide the ligands for selection.
- Order of development: DN1 → DN2 (TCRβ rearrangement) → DN3 (**pre-TCR**, Definition 15.2.1; β selection, allelic exclusion) → DN4 (proliferation) → DP (repeated TCRα rearrangement, surface αβTCR) → SP → export.
- Selection and outcomes:

| Process | Site | Ligand-presenting cell | Signal | Result |
|---|---|---|---|---|
| Death by neglect (Definition 15.3.2) | Cortex | — | None | More than about 90% of DP cells die by apoptosis |
| Positive selection (Definition 15.3.1) | Cortex | cTEC (private peptides from the thymoproteasome) | Weak | MHC restriction; CD4/CD8 lineage commitment |
| Negative selection (Definition 15.5.1) | Cortex and medulla | DCs, mTECs (AIRE, Definition 15.5.2) | Strong | Clonal deletion, central tolerance |
| Agonist selection | Medulla and elsewhere | mTECs, DCs; CD1d (DP cells) | Stronger | tTreg, iNKT, CD8αα IEL |

- Lineage commitment is determined by the duration of TCR signaling: sustained → ThPOK → CD4; interrupted + IL-7 → RUNX3 → CD8.
- Affinity window (Example 15.6.1): a normally distributed self-reactivity and two thresholds suffice to reproduce the proportions "about 92% neglect, about 4% positive, about 4% deleted" and to explain the experiments in which changing the MHC expression level changes the outcome of selection.
- Export depends on S1PR1; TRECs measure thymic output; the thymus involutes after puberty and repertoire diversity declines with age.

## Questions

1. Why does positive selection use peptides produced by processing machinery different from that of negative selection (the thymoproteasome and cathepsin L)?

   **Answer** Positive selection picks out cells that react weakly to certain self pMHC. If negative selection used exactly the same peptides, the selected cells would be exactly those that react to these peptides, and those with higher affinity would be deleted in the medulla, narrowing the repertoire. The private peptide repertoire of cTECs makes the ligands of positive selection overlap less with the self peptides presented in the periphery and the medulla, so that most positively selected cells react only more weakly to peripheral self peptides, which both preserves them and makes them less likely to cause autoimmunity; the marked reduction of CD8⁺ T cells in β5t-deficient mice supports this.

2. A mouse lacks β2m. What happens to its T-cell composition? What happens to NK-cell function?

   **Answer** Loss of β2m means that MHC class I molecules (as well as CD1d, MR1 and other molecules that need β2m) can hardly reach the cell surface, CD8⁺ T cells cannot be positively selected, and the periphery has almost no CD8⁺ T cells; iNKT and MAIT cells are also absent; CD4⁺ T cells are normal. NK cells depend during development on inhibitory signals from self class I molecules to be "licensed," and NK cells that develop in an environment without class I molecules have low reactivity, so they do not attack self cells that likewise lack class I molecules, but their killing function is weaker overall.

3. In the model of Example 15.6.1, suppose the threshold for negative selection is raised by some mutation to $\theta_- = 2.3$ (assume the Treg window moves with it to $[2.25, 2.3)$). How do the fraction of exported cells and the "potential self-reactivity" change?

   **Answer** The positively selected cells are $\Phi(2.25) - \Phi(1.405) \approx 0.9878 - 0.920 = 0.068$, negative selection falls to $1 - \Phi(2.3) \approx 0.011$, and the output increases to about 7%; but the extra cells have $x$ in $[1.79, 2.25)$, that is, they react strongly to self pMHC and would originally have been deleted. These cells enter the periphery and increase the risk of autoimmunity. AIRE deficiency is the disappearance of the signal for certain self antigens rather than a raised threshold, but the effect is similar: high-affinity cells reacting to those antigens are no longer deleted.

4. (Open question) After thymic involution, how do adults maintain the number and diversity of naive T cells? What does this imply for vaccinating older people with a new vaccine?

   **Answer** Key points: the adult naive T-cell pool is maintained mainly by peripheral proliferation (tonic signals from IL-7 and self pMHC), and thymic output continues but is small; proliferation maintains cell numbers without generating new TCRs, some clones expand and some disappear, and repertoire diversity gradually declines. The response to a new antigen (such as a never-encountered pathogen or a new vaccine) depends on whether precursors exist in the naive T-cell pool, and reduced diversity makes older people respond to new vaccines more weakly and more slowly, requiring stronger adjuvants or higher doses; booster responses to antigens already vaccinated against depend on memory cells and are less affected ([7.15.18](/7.15.18), [7.15.33](/7.15.33)).
