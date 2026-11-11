---
title: Immunological Tolerance
description: "How the immune system avoids attacking itself: the concept and antigen specificity of immunological tolerance; central and peripheral tolerance (anergy, ignorance, activation-induced death, regulatory T cells and tolerogenic DCs); the antigens, routes and host conditions that induce tolerance; oral tolerance; immune privilege and fetal–maternal tolerance; monogenic diseases of failed tolerance; a first-order kinetic model illustrating the two layers of defense; and clinical approaches to inducing and breaking tolerance."
source_hash: 98264a9bc80c
---

The preceding chapters answered how the immune system recognizes (receptors and MHC), how it decides (activation and polarization) and how it clears (antibodies and effector cells). This chapter answers half of the fifth question on the path: how it avoids attacking itself. Antigen receptors are produced by random rearrangement ([7.15.12](/7.15.12)), so receptors that recognize self molecules are not an exception but a certainty; if nothing were done about them, a considerable fraction of lymphocytes would be self-reactive. The solution of the immune system is not a single gate but defense in layers: self-reactive cells are deleted or reshaped during development ([7.15.15](/7.15.15), [7.15.19](/7.15.19)); cells that escape are rendered unresponsive, deleted or suppressed by regulatory cells in the periphery; and at some sites antigen is simply kept apart from lymphocytes. This chapter first gives the concepts and the layers, then goes through the peripheral mechanisms and the conditions for inducing tolerance one layer at a time, then discusses sites of immune privilege and fetal–maternal tolerance, uses a small model to show how the two layers of defense divide the work, and finally looks at what happens when tolerance fails ([7.15.28](/7.15.28)) and at how tolerance is exploited or reversed therapeutically. The molecular mechanisms of inhibitory receptors, checkpoints and Tregs are developed in [7.15.25](/7.15.25).

## 24.1. Concept and Features of Immunological Tolerance

**Definition 24.1.1 (Immunological Tolerance)** The state in which the immune system does not respond to a particular antigen is called **immunological tolerance**. An antigen that induces tolerance is called a tolerogen, and an antigen that induces a response is called an immunogen; the same molecule can be either a tolerogen or an immunogen, depending on the dose, form and route of entry of the antigen and on the state of the host.

The core feature of immunological tolerance is antigen specificity: there is no response to the tolerogen, and the response to other antigens is entirely normal. This distinguishes it from two other kinds of "unresponsiveness".

| | Immunological tolerance | Immunosuppression | Immunodeficiency |
|---|---|---|---|
| Antigen specificity | Yes | No | No |
| Mechanism | Clonal deletion, anergy, regulatory cells | Drugs, radiation, some infections | Gene mutations, viral infections |
| Consequence | Protection from autoimmune disease; may also leave chronic infections and tumors uncleared | Recurrent infections, tumors | Recurrent infections, tumors |

Tolerance can be induced: it is both natural (self-tolerance) and can be acquired later. Three historical threads established the concept. In 1945 Owen found that fraternal twin cattle that shared a placental circulation were red blood cell chimeras of each other and made no antibody against each other's red cells as adults; Burnet and Fenner inferred from this that antigens met during embryonic life are treated as "self". In 1953 Billingham, Brent and Medawar injected cells of another strain into newborn mice; as adults these mice accepted skin grafts of that strain without rejection yet still rejected skin of a third strain, which proved directly that tolerance can be induced artificially and is specific; Burnet and Medawar shared the 1960 Nobel Prize for this. The clonal selection theory ([7.15.1](/7.15.1)) requires that self-reactive clones be removed early in development, and later experiments (Goodnow's lysozyme double-transgenic mice, Nemazee's H-2K transgenic mice, [7.15.19](/7.15.19)) confirmed this. Later still, the discovery of peripheral tolerance and regulatory T cells extended tolerance from "deletion" to "active regulation", and the work on FOXP3 and Tregs received the 2025 Nobel Prize in Physiology or Medicine.

According to where it acts, self-tolerance is divided into four layers; they are not alternatives but are superimposed:

| Layer | Site | What it does | Main mechanisms |
|---|---|---|---|
| Antigen sequestration | Tissues with barriers | Keeps antigen from contacting lymphocytes | Blood–tissue barriers, lack of lymphatic drainage, local inhibitory factors |
| Central tolerance | Thymus (T), bone marrow (B) | Deletes or reshapes self-reactive cells during development | **Negative selection**, **receptor editing**, thymic Tregs |
| Peripheral tolerance | Secondary lymphoid organs and tissues | Prevents cells that escaped from being activated, or eliminates them | Ignorance, anergy, peripheral clonal deletion |
| Active regulation | Secondary lymphoid organs and sites of inflammation | Suppression of self-reactivity by regulatory cells | Tregs, tolerogenic DCs, regulatory B cells |

![Where self-tolerance is enforced. A: Central tolerance. Immature lymphocytes in the thymus and bone marrow that recognize self antigen strongly are deleted (apoptosis), B cells change the light chain by receptor editing, T cells become thymic Tregs, or B cells enter an anergic state; cells that recognize self not at all or only weakly leave after positive selection. B: Peripheral tolerance. A naive cell that has escaped and meets self antigen presented by an immature dendritic cell without costimulatory signals ends in ignorance, anergy, apoptosis (Fas, Bim) or suppression by Tregs; if the antigen appears together with danger signals, the same cell may be activated. C: Antigen sequestration. Barriers keep lymphocytes from contacting antigen, and privileged sites also have active suppressive mechanisms; this sequestration is relative, not absolute](./plots/tolerance-overview.py)

## 24.2. Central Tolerance

**Central tolerance** occurs in the primary lymphoid organs: in the thymus for T cells and in the bone marrow for B cells. Some of the antigen receptors produced by random rearrangement always bind self antigens; if these cells matured, autoimmune disease would be very common. Developing lymphocytes therefore undergo a "self test", whose outcome is determined by the strength of binding between receptor and self antigen (the affinity window, [7.15.15](/7.15.15)): cells that do not recognize self receive no survival signal and undergo apoptosis (**death by neglect**), cells with moderate recognition survive (positive selection), and cells with strong recognition are deleted or reshaped.

Central tolerance of T cells relies mainly on negative selection in the thymus. Thymocytes that strongly recognize self peptide–MHC initiate apoptosis through Nur77 and Bim (**clonal deletion**); some of the strongly recognizing cells instead become thymic Tregs that express **FOXP3**, which after leaving the thymus suppress responses to the same self antigen in the periphery. Why high-affinity recognition leads in some cells to deletion and in others to Tregs is currently understood in an integrated way: brief, high-affinity contact together with costimulation by CD28 and CD40 and local cytokines (IL-2 and others) favors Tregs, while sustained strong contact favors deletion. How the thymus presents antigens that are expressed only in peripheral tissues is the key to central tolerance: medullary cells among the **thymic epithelial cells**, under the control of **AIRE**, express thousands of tissue-restricted antigens at low levels, and these antigens are presented to thymocytes directly or by dendritic cells through **cross-presentation** ([7.15.15](/7.15.15)).

Central tolerance of B cells takes place in the bone marrow, and the outcome depends on the form of the self antigen ([7.15.19](/7.15.19)): multivalent, membrane-bound self antigen causes strong BCR cross-linking, which makes the cell re-express RAG and undergo receptor editing, and if editing fails the cell undergoes apoptosis; soluble, monovalent self antigen causes only a weak, persistent signal, which makes the cell downregulate surface IgM and enter an anergic state. When these cells are released into the periphery, they cannot compete for BAFF and have a very short life span.

Central tolerance is not perfect, for two reasons: not all self antigens are expressed in the thymus or bone marrow (even when AIRE is normal), and deletion has an affinity threshold, so self-reactive clones with affinity slightly below the threshold can escape. Studies show that about 20% of the mature naive B cells in the peripheral blood of healthy people carry self-reactive or polyreactive receptors (this proportion is as high as 55%–75% among the newly generated immature B cells of the bone marrow and falls after testing), which shows that escape of self-reactive cells is the norm. Peripheral tolerance exists for these cells.

## 24.3. Peripheral Tolerance

**Definition 24.3.1 (Peripheral Tolerance)** The mechanisms in secondary lymphoid organs and tissues that keep mature self-reactive lymphocytes from being activated, eliminate them, or have them suppressed by regulatory cells are called **peripheral tolerance**.

The starting point of peripheral tolerance is that when a mature naive lymphocyte meets antigen, the outcome depends on the "context". If the same antigen is accompanied by danger signals of pathogen origin and by costimulation, the cell is activated; without these signals, the cell goes toward tolerance. Self antigens are usually in the second context. There are five kinds of peripheral mechanisms.

### 24.3.1. Immunological Ignorance

**Definition 24.3.2 (Immunological Ignorance)** The state in which a self-reactive lymphocyte is neither activated nor eliminated, because the concentration of the antigen it recognizes is too low, its affinity too weak, or the antigen is located where it cannot reach the cell, is called **immunological ignorance**.

Ignorant cells still exist but "do not know" that the self antigen exists, so this is not true tolerance: such latent cells may switch to a responsive state if they meet higher levels of antigen, stronger costimulation (such as inflammation caused by infection) or released antigen. For example, inflammation appearing in one eye after trauma to the other (sympathetic ophthalmia, §24.5) shows that cells reactive to antigens inside the eye have been present all along, merely in a state of being "ignored".

### 24.3.2. Clonal Anergy

**Definition 24.3.3 (Clonal Anergy)** The state in which a lymphocyte that receives an antigen signal without a costimulatory signal enters a long-term inability to be activated is called **clonal anergy**.

For T cells this is the consequence of "signal 1 without signal 2" ([7.15.16](/7.15.16)): the TCR is stimulated by self peptide–MHC, but the antigen-presenting cell does not express sufficient **costimulatory molecules** (such as CD80/CD86), and the T cell neither produces IL-2 nor proliferates. The molecular basis is roughly this: the calcium–NFAT pathway of TCR signaling is activated, whereas Ras–ERK and AP-1 are insufficient for lack of CD28 signaling, and NFAT without its AP-1 partner induces a set of anergy-associated genes; E3 ubiquitin ligases (Cbl-b, Itch, GRAIL) degrade signaling molecules and TCR signaling weakens further; inhibitory receptors such as **CTLA-4** and **PD-1** reinforce this state ([7.15.25](/7.15.25)). Anergy is not death and under some conditions is reversible: adding **interleukin-2** or strong inflammatory signals can restore the response of anergic T cells.

Anergy of B cells was already met above (§24.2): soluble monovalent self antigen occupies the BCR for a long time without cross-linking it, and the cell downregulates mIgM, no longer responds to antigen and is at a disadvantage in competition for BAFF.

### 24.3.3. Peripheral Clonal Deletion

Self-reactive mature cells can also be deleted in the periphery. Under high-level, persistent stimulation by self antigen T cells are activated repeatedly and upregulate Fas and its ligand FasL; Fas initiates apoptosis through the **death receptor** pathway, which is called **activation-induced cell death** (discussed in [7.15.25](/7.15.25)); another route is the "passive" death mediated by the proapoptotic protein Bim: when antigen disappears and cytokines (such as IL-2 and IL-7) are withdrawn, activated cells undergo apoptosis, which is also why most effector cells disappear at the end of a response ([7.15.18](/7.15.18)). B cells are also induced to undergo apoptosis when self antigen cross-links the BCR extensively and no T-cell help is available. Peripheral tolerance of B cells has a further "safeguard": activation of a self-reactive B cell usually requires help from a Th cell specific for the same antigen ([7.15.20](/7.15.20)), but the corresponding self-reactive CD4⁺ T cells have been deleted in the thymus or controlled in the periphery, so self-reactive B cells lack help and can hardly enter germinal centers.

### 24.3.4. Dendritic Cells and Regulatory Cells

Dendritic cells at rest (steady state) continuously take up apoptotic cells and self proteins from the tissue and present them to T cells, but do not express high levels of costimulatory molecules or secrete inflammatory cytokines; such DCs are called tolerogenic DCs. **Cross-presentation** of self antigen by steady-state DCs to CD8⁺ T cells leads to anergy or deletion of the latter, which is called cross-tolerance; DCs also produce retinoic acid, TGF-β and IDO, which promote Treg differentiation. The state of maturation of the DC thus becomes the switch between tolerance and response: inflammatory signals make DCs upregulate MHC II, CD80/CD86, IL-12 and so on, turning a "tolerance signal" into an "activation signal" ([7.15.14](/7.15.14), [7.15.16](/7.15.16)).

**Regulatory T cells** are the protagonists of active tolerance. Tregs produced in the thymus and Tregs induced in the periphery from naive CD4⁺ T cells by TGF-β, IL-2 and low-intensity costimulation both express FOXP3 and high levels of CD25; they suppress neighboring self-reactive cells by competing for IL-2, lowering the costimulatory molecules of DCs through CTLA-4, secreting IL-10 and TGF-β, and by direct killing ([7.15.17](/7.15.17), [7.15.25](/7.15.25)). Regulatory B cells (secreting IL-10), myeloid-derived suppressor cells and tolerogenic macrophages have similar effects. The regulatory mechanisms of the periphery are antigen-specific: the TCR of a Treg recognizes self antigen, so suppression is confined to where the antigen is and does not cause systemic immunosuppression.

A summary of the peripheral mechanisms:

| Mechanism | Condition | Fate of the cell | Reversibility | When defective |
|---|---|---|---|---|
| Ignorance | Low antigen concentration or affinity, sequestration | Present but not activated | Can be activated when antigen increases or with inflammation | Autoimmunity after infection or trauma |
| Anergy | Signal 1 without signal 2 | No IL-2, no proliferation | Partly reversible (IL-2, strong inflammation) | Autoimmunity with abnormal costimulation |
| Peripheral clonal deletion | Persistent strong stimulation (Fas), cytokine withdrawal (Bim) | Apoptosis | Irreversible | Fas, FasL mutations: lymphoproliferation and autoimmunity |
| Tregs and tolerogenic DCs | Self antigen + TGF-β, IL-2 | Suppression of other cells | Depends on the number and function of Tregs | *FOXP3* mutation: multiorgan autoimmunity |

## 24.4. Conditions for Inducing Tolerance

The choice between tolerance and response is determined jointly by factors of the antigen and of the host, and the same antigen can become a tolerogen because of these factors.

| Factor | Favors tolerance | Favors response |
|---|---|---|
| Antigen dose | Too low or too high | Intermediate |
| Antigen form | Soluble monomer; not efficiently taken up by APCs | Aggregated polymers, particles, taken up and presented by APCs |
| Persistence of antigen | Persistent, repeated stimulation | Brief presence |
| Route of entry | Oral, intravenous; subcutaneous and intradermal are the hardest | Subcutaneous, intradermal (with adjuvant) |
| Adjuvant and state of APCs | No adjuvant; immature or unactivated APCs; weak costimulation | Adjuvant, mature APCs |
| Age and development | Embryonic and neonatal periods are easiest; adulthood is harder and not durable | Adulthood |
| Physiological state | Easily induced under immunosuppression | |
| Antigen epitope | Some epitopes tend to induce Tregs (tolerogenic epitopes) | |

The relation between antigen dose and outcome is nonmonotonic: with too low a dose, T and B cells are not sufficiently activated and the result is low-zone tolerance; with too high a dose, apoptosis or differentiation to Tregs is induced and the result is high-zone tolerance; intermediate doses produce a response. The dose requirements for tolerance of T cells and B cells differ:

| | T-cell tolerance | B-cell tolerance |
|---|---|---|
| Amount of antigen required | Small (low zone) | Large (high zone) |
| Time of onset | Fast, peaking within 24 h | Slow, 1–2 weeks |
| Duration | Long, months to years | Short, weeks |

This explains an important experimental observation: with a small dose of antigen that induces tolerance only in T cells, B cells may still be activated, but because T-cell help is lacking the B-cell response cannot be sustained. The key to inducing complete tolerance is therefore often the T-cell link.

**Definition 24.4.1 (Oral Tolerance)** The systemic, specific unresponsiveness to a protein antigen induced by its ingestion by mouth is called **oral tolerance**; the phenomenon that the same antigen can still induce a secretory IgA response locally in the gut, so that a local response coexists with systemic tolerance, is called split tolerance.

Oral tolerance is the default response of the gut to food antigens ([7.15.23](/7.15.23)): antigen in the gut is taken up by CD103⁺ DCs, which produce retinoic acid and TGF-β, induce pTregs and make T cells home to the gut; high doses of oral antigen also induce anergy and deletion of T cells. Oral antigen can therefore produce local IgA while maintaining tolerance in the whole body. Conversely, oral administration does not necessarily induce tolerance: antigens that carry pathogen signals, such as live attenuated vaccines, can activate immunity (this depends on whether the antigen is accompanied by danger signals and adjuvant and not simply on the route). Oral tolerance has been tried for the treatment of autoimmune diseases such as multiple sclerosis and rheumatoid arthritis, but the results of large trials were mostly negative, mainly because dose and duration are hard to optimize in humans.

## 24.5. Immune Privilege and Fetal–Maternal Tolerance

**Definition 24.5.1 (Immune Privilege)** Sites such as the anterior chamber of the eye, the testis and the brain, where immune rejection of grafts and antigens is weak and foreign antigens introduced do not provoke the usual inflammatory response, are called sites of **immune privilege**.

There are three kinds of mechanisms at privileged sites: physical barriers make it hard for antigen and lymphocytes to meet (blood–eye, blood–testis and blood–brain barriers, little lymphatic drainage); inhibitory factors secreted locally (TGF-β, α-MSH and others) and regulatory cells suppress inflammation; and tissue cells express FasL, which causes infiltrating activated T cells to undergo apoptosis (the level of expression and the size of the effect are still debated). The "anterior chamber-associated immune deviation" (ACAID) that follows antigen introduction into the anterior chamber of the eye is a typical example: antigen injected into the anterior chamber induces systemic antigen-specific tolerance and suppresses delayed-type hypersensitivity while preserving antibody responses.

This privilege is relative, not absolute. A penetrating injury of the eye exposes previously sequestered antigens, and inflammation of the injured eye causes inflammation in the contralateral eye (sympathetic ophthalmia), because antigens inside the eye never took part in establishing peripheral tolerance and the reactive clones are in a state of immunological ignorance. The brain is also not completely isolated: the blood–brain barrier can open and close, the meninges contain lymphatic vessels, circulating lymphocytes patrol regularly, and healthy people have self-reactive cells that recognize components of the nervous system, which shows that active suppression is present in the brain too; once tolerance to myelin antigens is broken, **autoimmune disease** results, such as multiple sclerosis (whose animal model is experimental autoimmune encephalomyelitis). "Privilege" therefore does not mean absence of immunity but that at these sites, where the consequences are serious, the balance of immunity is tilted toward tolerance.

Fetal–maternal tolerance is the most closely studied "privilege". The fetus expresses paternal antigens and is half foreign to the mother, yet is not rejected during pregnancy (the physiology of pregnancy is in [7.14.38](/7.14.38)). The mechanisms currently thought to operate are multilayered: the syncytiotrophoblast in direct contact with maternal blood does not express classical MHC molecules; the extravillous trophoblast does not express HLA-A, HLA-B or MHC class II molecules but expresses HLA-C and the **nonclassical MHC molecules** HLA-E and HLA-G, which suppress killing by uterine NK cells through inhibitory receptors, while uterine NK cells also help to remodel blood vessels; Tregs increase in the decidua, and inhibitory molecules such as IDO (tryptophan catabolism) and PD-L1 are present locally; hormones such as progesterone also play a role. The mother's tolerance to fetal antigens is actively induced and not merely a "barrier", and its disturbance is associated with complications such as recurrent miscarriage and preeclampsia (correlative studies; the mechanisms are still under study). Maternal IgG can cross the placenta through FcRn ([7.15.21](/7.15.21)), which is the basis of passive immunity, but also the route by which anti-red-cell antibodies injure the fetus in blood group incompatibility between mother and fetus.

## 24.6. A First-Order Model of Two Layers of Defense

How do the several layers of tolerance divide the work quantitatively? A linear model with only two variables gives an intuition. The model is schematic: the parameters are chosen to give reasonable time scales and are not measured values, and the model is used to compare the relative consequences of "which layer is missing".

**Example 24.6.1 (Division of Labor Between Central Tolerance and Peripheral Regulation)** Let the number of naive self-reactive cells be $S$ and the number of self-reactive effector cells be $E$ (both in relative units). The thymus exports self-reactive clones at rate $\theta$, of which a fraction $\delta$ is deleted by negative selection; naive cells die at rate $\mu$ and are activated by self antigen at rate $\alpha$; effector cells expand at rate $\rho$, the expansion being suppressed by Tregs (the number of Tregs is $R$, the suppression factor is $g = 1/(1 + R/K)$), and disappear at rate $d$:

$$
\begin{aligned}
\frac{\mathrm{d}S}{\mathrm{d}t} &= \theta(1-\delta) - (\mu+\alpha)S, \\
\frac{\mathrm{d}E}{\mathrm{d}t} &= \alpha S + (\rho g - d)E .
\end{aligned}
$$

Take $\theta = 1$, $\mu = 0.02\,\mathrm{d^{-1}}$, $\alpha = 0.002\,\mathrm{d^{-1}}$, $\rho = 0.05\,\mathrm{d^{-1}}$, $d = 0.03\,\mathrm{d^{-1}}$, $K = 1$. The steady state of the first equation is $S^* = \theta(1-\delta)/(\mu+\alpha)$, determined by central tolerance alone. The second equation depends on the sign of the effective growth rate $\rho g - d$. If $\rho g < d$, $E$ tends to a finite steady state

$$
E^* = \frac{\alpha S^*}{d - \rho g},
$$
otherwise $E$ grows exponentially. $\rho g < d$ is equivalent to $R > R_{\mathrm{c}} = K(\rho/d - 1)$, and with these parameters $R_{\mathrm{c}} \approx 0.67K$.

In the numerical solution (integrating 720 d, with $\delta = 0.95$ or 0 and $R = 4$ or 0):

- Both layers intact ($\delta = 0.95$, $R = 4$): $E^* = 0.23$.
- No negative selection ($\delta = 0$, $R = 4$, corresponding to the extreme case of AIRE deficiency): $S^*$ increases 20-fold and $E^* = 4.5$; the effector cells also increase 20-fold but remain bounded.
- No Tregs ($\delta = 0.95$, $R = 0$, corresponding to FOXP3 deficiency): $\rho g - d = 0.02\,\mathrm{d^{-1}}$ is positive, $E$ grows exponentially with a doubling time of about 35 d, crosses the illustrative threshold of "tissue damage" (taken as $E = 100$) at about 340 d, and has reached $2 \times 10^5$ at 720 d.
- Both layers missing: the threshold is crossed at about 190 d.

:::

The results have two implications. First, central tolerance changes the "level": it shrinks the pool of self-reactive cells proportionally (here by $1/(1-\delta)$) and so shrinks the size of any single peripheral event. Second, peripheral regulation changes the "stability": as long as suppression is strong enough ($R > R_{\mathrm{c}}$), the number of self-reactive cells has an upper limit; once suppression falls below the threshold, the number is no longer bounded, and central tolerance alone only postpones the appearance of the consequences. This agrees with the monogenic diseases of humans: AIRE deficiency and FOXP3 deficiency damage the central and peripheral layers respectively (§24.7) and present differently. The model does not take into account the dependence of the number of Tregs itself on IL-2 and the changes of self antigen, which would change the threshold but not the division of labor between "level and stability".

![A first-order kinetic model of two-layer self-tolerance (schematic). A: the number of self-reactive effector cells under four combinations (relative units, logarithmic axis, 720 d); the dashed line is the schematic threshold of tissue damage. With both layers intact (solid line) effector cells settle at a very low level; without negative selection but with Tregs retained (dashed line) the level rises about 20-fold but remains bounded; without Tregs (dashed line) the growth rate is positive and the number grows without bound; with both missing, growth is faster still. B: schematic of the nonmonotonic relation between antigen dose and response (no data): too low or too high a dose both produce tolerance (low-zone and high-zone tolerance), and an intermediate dose produces the strongest response](./plots/tolerance-layers.py)

## 24.7. Failure of Tolerance

When tolerance is broken, self-reactive cells are activated and **autoimmune disease** follows ([7.15.28](/7.15.28)). Common triggers and mechanisms include:

- Infection: inflammation caused by infection matures APCs, upregulates costimulatory molecules and induces secretion of inflammatory cytokines, so that self-reactive cells that were ignored or anergic are activated as bystanders;
- **Molecular mimicry**: an antigen of a pathogen is structurally similar to a self antigen, and the response against the pathogen cross-recognizes self tissue, as in rheumatic fever after group A streptococcal infection and Guillain–Barré syndrome after *Campylobacter jejuni* infection;
- Release of sequestered antigen: trauma, infection or inflammation exposes sequestered antigens (as in sympathetic ophthalmia);
- **Epitope spreading**: tissue damage releases new self antigens, and the response spreads from the initial target antigen to other epitopes of the same tissue;
- Genetic background: the accumulation of small variants in several genes, such as certain HLA alleles ([7.15.13](/7.15.13)).

The most convincing genetic evidence comes from monogenic diseases, each corresponding to a defect in one layer of defense:

| Gene | Layer of tolerance defective | Disease (human) | Main features |
|---|---|---|---|
| *AIRE* | Central tolerance: mTECs do not express tissue-restricted antigens | Autoimmune polyendocrinopathy–candidiasis–ectodermal dystrophy (APECED) | Autoimmunity of endocrine glands such as the parathyroid and adrenal glands, chronic mucocutaneous candidiasis |
| *FOXP3* | Active regulation: loss of Tregs | IPEX (immune dysregulation, polyendocrinopathy, enteropathy, X-linked) | Enteropathy beginning in the neonatal period, type 1 diabetes, dermatitis, multiorgan autoimmunity (corresponding to scurfy in the mouse) |
| *IL2RA* (CD25) | Active regulation: impaired survival and function of Tregs | CD25 deficiency | Autoimmunity and lymphocytic infiltration similar to IPEX |
| CTLA4 | Peripheral anergy and Treg function | CTLA-4 haploinsufficiency | Multiorgan lymphocytic infiltration, autoimmunity, hypogammaglobulinemia |
| FAS, FASLG | Peripheral clonal deletion: defective activation-induced cell death | Autoimmune lymphoproliferative syndrome (ALPS) | Enlarged lymph nodes and spleen, autoimmune cytopenias, increased double-negative T cells (corresponding to lpr and gld in the mouse) |

This table puts the mechanisms of the chapter onto diseases one by one and is the best way to understand the "layers": in people lacking the central layer, autoimmunity is concentrated in the tissues whose antigens AIRE presents; in people lacking Tregs, autoimmunity is systemic and begins earlier; in people lacking Fas, the main feature is accumulation of lymphocytes.

## 24.8. Exploiting and Breaking Tolerance

Knowledge of tolerance has two applications in opposite directions: inducing tolerance in autoimmune disease, transplantation and allergy, and breaking tolerance in tumors and chronic infections.

| Direction | Strategy | Principle | Examples and references |
|---|---|---|---|
| Inducing | Blocking costimulation | Signal 1 without signal 2, inducing anergy | CTLA-4–Ig fusion protein (blocks the binding of CD80/CD86 to CD28) used in rheumatoid arthritis and kidney transplantation; anti-CD40L antibodies |
| Inducing | Antigen-specific therapy | Altered or antagonist peptides compete for TCR and MHC; antigen given orally or intravenously induces tolerance | Glatiramer acetate in multiple sclerosis (mechanism still debated); tolerance mechanisms in allergen immunotherapy ([7.15.26](/7.15.26)) |
| Inducing | Regulatory cells | Expansion or infusion of Tregs; low-dose IL-2 expands Tregs selectively; induction of immune deviation | At the clinical trial stage, with large individual variation |
| Inducing | Deletion or reconstitution | Bone marrow and thymus transplantation, mixed chimerism, to rebuild central tolerance | Transplantation tolerance ([7.15.29](/7.15.29)) |
| Breaking | Blocking inhibitory receptors | Removing the inhibition of T cells by CTLA-4 and PD-1 | Immune checkpoint blockade antibodies ([7.15.25](/7.15.25), [7.15.30](/7.15.30)) |
| Breaking | Enhancing costimulation | Agonistic antibodies enhance T-cell activation | Anti-CD40, anti-4-1BB, anti-OX40, anti-GITR |
| Breaking | Weakening Tregs | Removal of suppressor cells | Anti-CD25 or depleting anti-CTLA-4 antibodies |
| Breaking | Maturing DCs | Turning tolerance signals into activation signals | Adjuvants and some cytokines (GM-CSF, IFN-γ); vaccine design ([7.15.33](/7.15.33)) |

The two directions share the same logic: central and peripheral tolerance are not static. Patients treated with checkpoint blockade for tumors often show adverse reactions resembling autoimmune disease (colitis, thyroiditis, hypophysitis and so on), which shows that what is released is not only the antitumor response but also self-reactivity that had been suppressed by tolerance; and since most tumor antigens come from self proteins, the difference between tumor immunity and autoimmunity is often only which tissue the response is directed at. This is the connection of this chapter with [7.15.30](/7.15.30) and [7.15.28](/7.15.28).

## Summary

- Immunological tolerance is an antigen-specific state of unresponsiveness (Definition 24.1.1), distinct from global immunosuppression and immunodeficiency; it is implemented in superimposed layers of antigen sequestration, central tolerance, peripheral tolerance and active regulation (§24.1).
- Central tolerance deals with developing self-reactive cells by negative selection, receptor editing and thymic Tregs, but escape is the norm, so peripheral mechanisms are needed (§24.2).
- Peripheral tolerance (Definition 24.3.1) includes ignorance (Definition 24.3.2), anergy (Definition 24.3.3), peripheral clonal deletion (Fas, Bim) and active regulation by Tregs and tolerogenic DCs; whether there is tolerance depends on the signal context accompanying the antigen (§24.3).
- Conditions for inducing tolerance: antigen dose (low and high zones), form, route, adjuvant and state of APCs, and the age and physiological state of the host; T-cell tolerance is fast, durable and needs little antigen, and B-cell tolerance is slow, transient and needs much antigen. Oral tolerance (Definition 24.4.1) is the default state of the gut (§24.4).
- Immune privilege (Definition 24.5.1) is relative and is maintained jointly by barriers, inhibitory factors and regulatory cells; fetal–maternal tolerance is active and multilayered (§24.5).
- In the first-order model, central tolerance shrinks the pool of self-reactive cells proportionally (level), and peripheral regulation decides whether it is bounded (stability) (Example 24.6.1).
- Failure of tolerance corresponds to monogenic diseases of different layers (*AIRE*, *FOXP3*, *CTLA4*, *FAS*) and also occurs after infection, molecular mimicry and release of antigen (§24.7).
- Therapeutically, tolerance is induced by blocking costimulation, antigen-specific therapy and regulatory cells, and broken by checkpoint blockade, agonistic costimulation and weakening of Tregs (§24.8).

## Questions

1. Why can the same antigen be either an immunogen or a tolerogen? Give at least three determining factors.

   **Answer** Immunogen and tolerogen are not inherent classes of antigen but outcomes of the interaction of antigen and host, depending on the signal context. (1) Dose: intermediate doses produce a response, and doses that are too low (low zone) or too high (high zone) produce tolerance. (2) Form and route: soluble monomers are not efficiently taken up by APCs, and entry by the oral or intravenous route readily induces tolerance, whereas aggregated polymers, particles, and subcutaneous antigen with adjuvant readily induce a response. (3) Costimulation and state of the APC: without adjuvant and when presented by immature DCs, T cells receive signal 1 without signal 2 and go toward anergy or Treg differentiation; mature DCs that provide costimulation induce a response. In addition, the age and developmental stage of the host (tolerance is easily induced in the embryonic and neonatal periods) and whether the host is immunosuppressed also have an influence.

2. Why do patients with *AIRE* mutations have mainly autoimmunity of endocrine glands? Does this defect affect central tolerance of B cells?

   **Answer** AIRE controls the expression by medullary thymic epithelial cells of large numbers of proteins that are normally expressed only in peripheral tissues (such as pancreatic islets, parathyroid and adrenal glands), so that the corresponding T-cell clones are deleted in the thymus or turned into Tregs; when AIRE is deficient, these clones escape to the periphery and attack tissues expressing the corresponding antigens, with the endocrine glands as the main target organs. Central tolerance of B cells takes place in the bone marrow and depends on self antigens on bone marrow stromal and hematopoietic cells, independent of AIRE; but production of autoantibodies usually needs Th-cell help, and AIRE deficiency lets self-reactive Th cells survive, so patients still develop autoantibodies.

3. In the model of Example 24.6.1, what happens to the number of self-reactive effector cells if the Treg level falls to $R = 0.5K$? Why does the model emphasize "stability" and not only level?

   **Answer** $g = 1/(1+0.5) = 2/3$ and $\rho g = 0.05 \times 2/3 \approx 0.033 > d = 0.03\,\mathrm{d^{-1}}$, so the effective growth rate is positive (about $0.0033\,\mathrm{d^{-1}}$); below the critical value $R_{\mathrm{c}} \approx 0.67K$ suppression is insufficient, $E$ no longer tends to a steady state but grows slowly and exponentially (doubling time about 200 d). This shows that when Tregs fall only slightly below the threshold, the consequence is unbounded accumulation and not a small rise in the number of effector cells; central tolerance, by contrast, only shrinks the input proportionally and cannot change the sign. It also suggests that a mild decline in the number or function of Tregs can cause chronic, progressive autoimmunity clinically.

4. (Open question) Why do tumor patients treated with anti-PD-1 or anti-CTLA-4 antibodies develop adverse reactions resembling autoimmune disease? What does this show about the nature of tolerance?

   **Answer** Key points: PD-1 and CTLA-4 are inhibitory receptors of peripheral tolerance that continuously restrict activation of self-reactive T cells; blocking them removes this brake, the antitumor response is enhanced and at the same time ignored or anergic self-reactive cells are released and attack tissues such as colon, thyroid, pituitary and skin. Depleting anti-CTLA-4 antibodies may also weaken Tregs and make the adverse reactions more severe. This shows that peripheral tolerance is a dynamic state that must be actively maintained continuously; tumor antigens mostly come from self proteins, and antitumor immunity and autoimmunity share the same pool of cells that tolerance suppresses; the therapeutic window depends on how the response can be biased toward the tumor.

5. (Open question) The fetus carries paternal antigens yet is not rejected in the mother. Discuss, in terms of the four layers of antigen sequestration, central tolerance, peripheral tolerance and active regulation, which mechanisms the mother may use.

   **Answer** Antigen sequestration: the syncytiotrophoblast covers the maternal–fetal interface and does not express classical MHC molecules, which limits presentation of paternal MHC. Peripheral tolerance: the extravillous trophoblast expresses HLA-G, HLA-E and HLA-C and suppresses uterine NK cells through inhibitory receptors; local IDO and PD-L1 and others suppress activated T cells. Active regulation: Tregs in the decidua and peripheral blood increase during pregnancy and suppress responses to paternal antigens. Central tolerance: a small number of fetal cells entering the mother (microchimerism) may induce tolerance to fetal antigens in the maternal thymus and periphery, but the evidence for this mechanism is weak. The point is that maternal tolerance is maintained by superimposed layers of mechanisms and not by a single one; defects are associated with complications such as recurrent miscarriage.
