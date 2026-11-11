---
title: Transplantation Immunology
description: Types of transplants and the immunological basis of rejection; the direct, indirect and semi-direct pathways of allorecognition; the mechanisms of hyperacute, acute and chronic rejection and of graft-versus-host disease; the principles of HLA matching and cross-matching and matching probabilities; the mode of action at each target of immunosuppressive therapy; transplantation tolerance and immune-privileged sites; and the barriers to xenotransplantation.
source_hash: ad9cf887a2b6
---

Transplantation immunology is the medical setting in which the ability of adaptive immunity to recognize "non-self" creates a problem: this time the "non-self" that is recognized is an organ from another individual of the same species. It is closely linked to earlier chapters: the core of rejection is recognition of **MHC** molecules by T cells ([7.15.13](/7.15.13), [7.15.14](/7.15.14)); rejection mediated by preformed antibody is Type II hypersensitivity ([7.15.27](/7.15.27)); drugs that suppress rejection act on every signal of T-cell activation ([7.15.16](/7.15.16)); and successful tolerance is an application of the chapters on tolerance ([7.15.24](/7.15.24)) and on the brakes ([7.15.25](/7.15.25)).

We first treat the classification of transplants and the basis of rejection, then the three pathways of allorecognition and the types of rejection and of graft-versus-host disease, then matching probabilities, the targets of immunosuppression, and finally tolerance and xenotransplantation. Transplant technique, organ allocation and the like are unrelated to immunology and are not covered here.

## 29.1. Types of Transplants and the Basis of Rejection

By the relation between donor and recipient, grafts fall into four classes:

| Type | Donor and recipient | Outcome |
|---|---|---|
| Autograft | The same individual | Accepted |
| Syngeneic graft | Genetically identical individuals (monozygotic twins, inbred mice) | Accepted |
| Allograft | Genetically different individuals of the same species | Rejected unless suppressed |
| Xenograft | Different species | Rejected rapidly and violently |

**Definition 29.1.1 (Allograft)** A transplant between genetically different individuals of the same species is called an **allograft**, and the transplanted tissue or organ is called an allogeneic graft.

The antigens that cause rejection are polymorphic molecules of the same species, collectively called alloantigens. The strongest are the **MHC** molecules, called **HLA** in humans, because of their extremely high polymorphism: the HLA of each individual differs from that of everyone else (monozygotic twins excepted) ([7.15.13](/7.15.13)). The others, which are weaker, are called minor histocompatibility antigens; they are peptides derived from the degradation of other polymorphic proteins (including products of genes on the Y chromosome) and presented to T cells by MHC molecules; the ABO blood group antigens are also an important class of alloantigens ([7.15.27](/7.15.27)). When donor and recipient MHC are fully matched, differences in minor antigens can still cause slower and weaker rejection or the graft-versus-host disease of 29.4.

The classical skin-graft experiments revealed the immunological character of rejection: with a first allogeneic skin graft, rejection appears at 7–10 days and is complete by 10–14 days (primary response); a second graft of skin from the same donor begins to be rejected at 3–4 days and is completed at 5–6 days (secondary response, with memory); skin from an unrelated third party is rejected as a primary rejection (specificity). These properties show that rejection is adaptive immunity, mediated by T cells; transferring T cells from the recipient to a syngeneic animal that has not been grafted makes it reject a graft from the same donor rapidly.

Alloreactivity has a peculiar quantitative feature: for the peptide of a given pathogen, only about $10^{-5}$–$10^{-4}$ of T cells in the naive repertoire can recognize it, but for an allogeneic cell, $1\%$–$10\%$ of recipient T cells react (about three orders of magnitude more than for a pathogen). The reason is that the TCRs of T cells are selected against a background of self MHC plus a variety of self peptides ([7.15.15](/7.15.15)); for an allogeneic MHC that resembles self MHC, together with the thousands of different peptides it presents, each allogeneic cell surface carries countless complexes that "look like self MHC plus some foreign peptide", so a large proportion of clones recognize it by cross-reaction; this is also why rejection is a stronger response than any infection elicits.

## 29.2. Three Pathways of Allorecognition

**Definition 29.2.1 (Allorecognition)** The process in which recipient T cells recognize donor-derived MHC molecules (and the peptides they present) is called **allorecognition**; it proceeds by direct and indirect pathways.

![Two main pathways of allorecognition. A, direct pathway: recipient T cells use the TCR to recognize intact donor MHC with peptide (red) on the surface of a donor **antigen-presenting cell**, which enters the recipient with the graft and supplies costimulation; many T cells are activated through cross-reaction. B, indirect pathway: recipient antigen-presenting cells take up shed donor proteins (including donor MHC molecules) and, after processing, present donor-derived peptides on recipient (self) MHC molecules (purple).](./plots/allorecognition.py)

- Direct pathway: recipient T cells directly recognize intact MHC molecules on the surface of donor cells. Donor antigen-presenting cells (dendritic cells, called "passenger leukocytes") enter with the graft and meet recipient T cells in the draining lymph node with costimulatory molecules present, so activation is strong and fast and many T cells (CD4⁺ and CD8⁺) take part; this is the main cause of acute rejection. As the donor passenger leukocytes are cleared, the role of the direct pathway gradually declines.
- Indirect pathway: recipient antigen-presenting cells take up fragments of donor cells (including peptides of donor MHC molecules), process them in the manner of an ordinary exogenous antigen and present them on recipient MHC to CD4⁺ T cells. This pathway is the same as the response to any foreign protein; the clones are fewer but persistent, and can provide help to B cells, which produce antibody against donor HLA, related to chronic rejection.
- Semi-direct pathway: recipient antigen-presenting cells acquire intact donor MHC molecules (by exosomes or by transfer on cell contact) and present them in a "mixed" form of donor MHC plus recipient MHC, so that the same antigen-presenting cell can be recognized by T cells of both the direct and the indirect pathways, and CD4⁺ T cells can also provide help to CD8⁺ T cells that recognize donor MHC class I molecules.

## 29.3. Types of Rejection

**Definition 29.3.1 (Graft Rejection)** The phenomenon in which the immune response of the recipient's immune system to an allogeneic graft results in destruction of the graft and loss of its function is called **graft rejection**.

| Type | Time | Mechanism | Lesion | Response to immunosuppression |
|---|---|---|---|---|
| Hyperacute | Minutes to hours | **Preformed** antibody in the recipient (anti-ABO, anti-HLA, for example from sensitization by pregnancy, transfusion or earlier transplants) activates complement | Injury of graft vascular endothelium, thrombosis, ischemic necrosis | Cannot be treated, only prevented (matching and cross-matching) |
| Acute cellular | Days to weeks (mostly within months) | T cells acting mainly through the direct pathway: CD8⁺ CTLs kill graft cells, CD4⁺ T cells activate macrophages and recruit cells, lymphocytic infiltration of the endothelium | Infiltration of mononuclear cells, injury of parenchyma and vascular endothelium | Usually effective |
| Acute antibody-mediated | Days to weeks | Newly produced (or preformed low-level) anti-donor HLA antibody; injury by complement and Fc receptor cells | Microvascular inflammation, C4d deposition | Requires treatment aimed at B cells and antibody |
| Chronic | Months to years | CD4⁺ T cells of the indirect pathway, persistent anti-donor antibody, chronic inflammation and growth factors | Intimal thickening and occlusion of graft vessels, parenchymal fibrosis | Insensitive to current drugs; the main cause of long-term graft failure |

The difference among the mechanisms can also be read by "pathway": hyperacute rejection is humoral and "preformed", acute rejection is cellular and "direct", and chronic rejection is "indirect" plus antibody. The main limit on long-term survival is chronic rejection, and the balance between drug toxicity (nephrotoxicity, infection, cancer) and rejection.

## 29.4. Graft-versus-Host Disease

**Definition 29.4.1 (Graft-versus-Host Disease)** A disease in which immunocompetent cells carried in the graft (mainly donor T cells) recognize the alloantigens of the recipient and attack recipient tissue, causing damage to skin, liver, intestine and other organs, is called **graft-versus-host disease** (GVHD).

Three conditions are required: the graft contains immunocompetent cells, the recipient carries histocompatibility antigens that the donor lacks, and the recipient cannot effectively reject the donor cells (being immunosuppressed because of immunodeficiency or conditioning). It is therefore typically seen in hematopoietic stem cell transplantation: tissue damage caused by conditioning releases danger signals and cytokines, which activate recipient antigen-presenting cells, which in turn activate donor T cells that differentiate into effector cells and attack skin, hepatobiliary tract and digestive tract (acute) or cause chronic manifestations resembling autoimmune disease (chronic). Even with fully HLA-matched donors, differences in minor histocompatibility antigens can cause GVHD.

The same immunological mechanism is also beneficial: donor T cells and NK cells also attack residual recipient leukemia cells (the graft-versus-leukemia effect), so removing donor T cells reduces GVHD but increases relapse of leukemia. The aim of treatment is to separate GVHD from the antileukemic effect, which is where tumor immunology and transplantation immunology meet ([7.15.30](/7.15.30)).

## 29.5. HLA Matching and Cross-Matching

Three levels are considered in choosing a donor: (1) ABO blood group compatibility, because blood group antigens are expressed on endothelial cells and incompatibility causes hyperacute rejection; (2) HLA matching, comparing the alleles of HLA-A, -B, -C and -DRB1, -DQB1, -DPB1 of donor and recipient, the better the match the lower the risk of acute rejection and GVHD (the requirement for hematopoietic stem cell transplantation is much higher than for solid organs); (3) cross-matching, testing the recipient's serum against the donor's cells to see whether the recipient already has antibody against donor HLA (panel reactive antibody, PRA, expresses the degree of sensitization of the recipient to the HLA of the population, and donor-specific antibody, DSA, antibody against the particular donor). Recipients sensitized by pregnancy, transfusion or earlier transplantation find it harder to obtain a suitable donor.

**Definition 29.5.1 (Mixed Lymphocyte Reaction)** The reaction in which lymphocytes of two individuals are cultured together in vitro, the cells of one being treated so that they cannot proliferate (as stimulator cells), and the T cells of the other (responder cells) proliferate because they recognize alloantigenic MHC on the stimulator cells, is called the **mixed lymphocyte reaction** (MLR).

The MLR is a miniature of alloreactivity in vitro: the degree of T-cell proliferation reflects the degree of difference between the MHC of the two (especially MHC class II molecules). It was used historically to judge HLA compatibility and has now been largely replaced by molecular HLA typing, but it remains a method for studying alloreactivity and a tool for evaluating immunosuppression and the function of regulatory cells.

### 29.5.1. Matching Probabilities

The mode of inheritance of HLA makes matching probabilities computable: HLA genes are tightly linked and inherited as a unit, the **haplotype** ([7.4.8](/7.4.8)). Each child receives one haplotype from each parent, so:

- Between siblings: the probability of sharing both haplotypes with a given sibling is $1/4$, of sharing one (haploidentical) is $1/2$, and of sharing neither is $1/4$; the probability that among $n$ siblings at least one is a full match is $1 - (3/4)^n$.
- Between parent and child: one haplotype is always shared (haploidentical).

**Example 29.5.1 (Probability of Donor Matching)** For an unrelated donor, let the population frequencies of the recipient's two haplotypes be $h_1$ and $h_2$; under Hardy–Weinberg proportions ([7.4.22](/7.4.22)) the probability that a random donor's genotype is exactly the recipient's genotype (a full match at haplotype level) is

$$
P = 2h_1h_2\quad(h_1 \ne h_2).
$$

In a registry of $N$ registered donors, the probability of at least one full match is $1 - (1 - P)^N$, and the $N$ needed to reach $90\%$ is $N \approx \ln 10/P$. Taking illustrative haplotype frequencies:

![Probability of donor matching (illustrative haplotype frequencies, Hardy–Weinberg proportions). A: probability that at least one of $n$ siblings is a full HLA match, $1 - (3/4)^n$. B: probability that an unrelated-donor registry contains at least one haplotype-level full match as a function of registry size $N$, for two haplotypes each at frequency 3%, 0.3% and 0.03% (single-donor match probability $P = 2h^2$ of $1.8 \times 10^{-3}$, $1.8 \times 10^{-5}$ and $1.8 \times 10^{-7}$, respectively).](./plots/hla-matching.py)

A recipient with common haplotypes ($P = 1.8 \times 10^{-3}$) needs only about $1.3 \times 10^3$ registrants to reach 90%; at $h = 0.3\%$ about $1.3 \times 10^5$ are needed; at $h = 0.03\%$ about $1.3 \times 10^7$. The high polymorphism of HLA means that a recipient with rare haplotypes can hardly find a fully matched unrelated donor, and also explains the size of registries, the haplotype frequencies of different populations and the practical value of haploidentical donors. (Real haplotype frequency distributions have far more than three values, and there is population-specific linkage disequilibrium among haplotypes; only orders of magnitude are given here.)

## 29.6. Targets of Immunosuppressive Therapy

**Definition 29.6.1 (Immunosuppressant)** A drug that suppresses the immune response is called an **immunosuppressant**, and is used to prevent and treat transplant rejection, GVHD and autoimmune disease.

They can be arranged along the steps of T-cell activation in [7.15.16](/7.15.16), each class corresponding to a target:

| Stage | Drug class (examples) | Molecular target and principle |
|---|---|---|
| Signal 1 (TCR) | Calcineurin inhibitors (cyclosporine, tacrolimus); anti-CD3 antibody | Cyclosporine with cyclophilin and tacrolimus with FKBP12 inhibit calcineurin, so that NFAT cannot be dephosphorylated and enter the nucleus, and transcription of **IL-2** is blocked (for calcium signaling see [7.3.19](/7.3.19)); anti-CD3 binds the TCR complex and depletes or modulates T cells |
| Signal 2 (costimulation) | Fusion protein of the extracellular domain of CTLA-4 with the Fc of IgG (belatacept) | Binds B7 and blocks CD28 costimulation (25.8) |
| Signal 3 (IL-2 receptor and growth) | Anti-CD25 antibody; mTOR inhibitors (sirolimus) | Block the α chain of the IL-2 receptor; sirolimus with FKBP12 inhibits mTOR and blocks the proliferation signal downstream of the IL-2 receptor |
| Proliferation (DNA synthesis) | Mycophenolic acid, azathioprine | Inhibit de novo purine synthesis (IMPDH); T and B lymphocytes depend more on de novo synthesis, so selectivity for lymphocytes is higher |
| Cell depletion | Antithymocyte globulin, anti-CD52, anti-CD20 | Deplete T cells or B cells (anti-CD20 is used for antibody-mediated rejection and the management of sensitization) |
| Broad anti-inflammatory | Glucocorticoids | Suppress inflammatory genes and lymphocyte proliferation through the glucocorticoid receptor (25.7) |

Clinically, several drugs are always combined, each acting at a different step, so that the dose and toxicity of each are reduced. The common problem of all these drugs is nonspecificity: they suppress all T-cell responses, so the risk of infection (including opportunistic infection) and of cancer (weakened immune surveillance, see [7.15.30](/7.15.30)) rises, and each has its own organ toxicity (the nephrotoxicity of calcineurin inhibitors is one example).

## 29.7. Transplantation Tolerance and Immune-Privileged Sites

Transplantation tolerance means that the recipient does not reject the graft of a particular donor while the responses to other antigens remain normal, without long-term immunosuppression. It is the ideal state but difficult to achieve; existing principles are:

- Mixed chimerism: the recipient receives donor hematopoietic stem cells, so that donor-derived antigen-presenting cells enter the recipient's thymus and clones against the donor are eliminated by negative selection (central tolerance, [7.15.15](/7.15.15)).
- Costimulation blockade and regulatory T cells: blocking the second signal while T cells are being activated causes T cells to become anergic or to become Tregs ([7.15.24](/7.15.24)); infusion of expanded **regulatory T cells** is a method under investigation.
- Spontaneous tolerance: some liver transplant recipients retain graft function after withdrawal of drugs, partly because of the special immunological environment of the liver (the tolerogenic antigen presentation by liver sinusoidal endothelium and Kupffer cells, and the oral-tolerance-like effect of the portal vein).

Grafts at some sites are more readily accepted, the sites of **immune privilege**: the anterior chamber of the eye, the cornea, the brain, the testis, and the placenta and fetal–maternal interface ([7.15.24](/7.15.24), [7.14.38](/7.14.38)). These sites are characterized by lack of lymphatic drainage, blood–tissue barriers, low expression of MHC molecules on cell surfaces and local immunosuppressive factors (TGF-β, FasL, PD-L1). Corneal transplantation therefore does not require matching in most cases and has a high success rate; but after inflammation or neovascularization occurs at these sites, privilege is lost.

## 29.8. Barriers to Xenotransplantation

The shortage of organs has drawn attention to xenotransplantation (the pig being the main candidate donor), but there are multiple immunological barriers, which are also a collection of principles from earlier chapters:

- Preformed natural antibodies: most mammals (except Old World primates) express the $\alpha$-Gal antigen (galactose-α-1,3-galactose); humans lack the corresponding glycosyltransferase yet, through exposure to intestinal bacteria, produce large amounts of anti-α-Gal antibody, causing hyperacute rejection of pig organs.
- Incompatibility of **complement regulatory proteins**: the complement regulatory proteins on pig cell surfaces (such as DAF and MCP) cannot effectively inhibit human complement, so human complement attacks without restraint ([7.15.10](/7.15.10)).
- Incompatibility of the coagulation system: coagulation-regulating molecules of pig and human (such as thrombomodulin) do not interact well, and thrombosis easily occurs.
- **Cellular immunity**: the MHC differences are larger across species, and T-cell responses are stronger than to allografts.
- Infection: the risk of cross-species infection by porcine endogenous retroviruses and other pathogens.

The countermeasure is to engineer the donor: knock out the gene that synthesizes α-Gal, introduce genes for human complement regulatory proteins and coagulation-regulating molecules, and combine this with immunosuppression. This proceeds by "removing the above barriers one by one", and the principle is the immunological mechanism of each of the barriers listed.

## Summary

- Allografts (Definition 29.1.1) are rejected because a high proportion ($1\%$–$10\%$) of clones in the recipient T-cell repertoire cross-recognize allogeneic MHC; rejection has memory and specificity.
- Allorecognition (Definition 29.2.1) has direct, indirect and semi-direct pathways, which dominate acute rejection, chronic rejection and the link between the two, respectively (figure).
- Graft rejection (Definition 29.3.1) is divided into hyperacute (preformed antibody), acute cellular (direct pathway), acute antibody-mediated and chronic (indirect pathway plus antibody).
- Graft-versus-host disease (Definition 29.4.1) arises from immunocompetent cells in the graft and shares its mechanism with the graft-versus-leukemia effect.
- Matching comprises ABO, HLA and cross-matching; HLA is inherited as haplotypes (probability of a full match between siblings 1/4), the probability of a full match for an unrelated donor is $2h_1h_2$, and rare haplotypes need very large registries (Example 29.5.1); the mixed lymphocyte reaction (Definition 29.5.1) is the in vitro readout of alloreactivity.
- Immunosuppressants (Definition 29.6.1) are layered by the signals of T-cell activation: TCR signal, costimulation, IL-2 receptor and proliferation, plus cell depletion and glucocorticoids; the common cost is nonspecificity.
- Tolerance depends on central deletion, costimulation blockade and Tregs, and immune-privileged sites on barriers and inhibitory factors; the barriers to xenotransplantation are the incompatibilities of preformed antibody, complement regulation, coagulation and cellular immunity.

## Questions

1. Why is rejection faster on a second graft of skin from the same donor? What does this mean for judging whether a recipient has been sensitized?

   **Answer** The first graft activated and expanded T cells specific for donor MHC and formed memory cells; on renewed contact the memory cells are activated faster and in greater numbers, so rejection begins at 3–4 days, and antibody against donor HLA may also already be present. The significance is that previous transplantation, transfusion or pregnancy sensitizes the recipient to HLA, and sensitized recipients are more prone to hyperacute and accelerated rejection with a new graft, so cross-matching and testing for panel reactive antibody are done.

2. Explain why transplantation between monozygotic twins needs no immunosuppression whereas haploidentical transplantation between parent and child does.

   **Answer** The MHC and minor antigens of monozygotic twins are identical, there are no alloantigens and hence no allorecognition. Between parent and child only one HLA haplotype is identical, and the haplotype from the other parent is "non-self" to the recipient; together with differences in minor antigens, the direct and indirect pathways are still activated and immunosuppression is needed.

3. A patient with a very rare HLA haplotype needs an unrelated donor. What does the model of Example 29.5.1 suggest? What methods can circumvent this limitation?

   **Answer** The probability of a match for a single donor, $2h_1h_2$, is very small, and the required registry size is proportional to $1/P$, so rare haplotypes require registries orders of magnitude larger. In principle the limitation can be circumvented by using a haploidentical related donor with stronger immunological measures (T-cell depletion, regulatory cells) to reduce GVHD; by accepting a lower level of matching (requiring a match only at key loci); or by using cord blood (whose T cells are naive and whose matching requirements are lower). All these methods trade a change in the strength of the immune response for matching.
