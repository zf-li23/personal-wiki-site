---
title: "B-Cell Responses: Germinal Centers, Affinity Maturation and Class Switching"
description: Two-signal activation of B cells by thymus-dependent antigens and T–B cell interaction; the fate bifurcation between the extrafollicular response and the germinal center; affinity maturation by the mutation–selection cycle between the dark zone and the light zone; class switching determined by cytokines; the generation of long-lived plasma cells and memory B cells; responses to thymus-independent antigens; and the general rules of primary and secondary humoral responses.
source_hash: 4abba643d8b9
---

On the knowledge path, this chapter answers two questions on the humoral side: "what is decided after recognition?" and "how is it remembered?" Once a mature B cell has bound antigen, it must decide whether to become activated; once activated, it must decide whether to secrete low-affinity antibody immediately or to enter a germinal center and spend several weeks "polishing" the antibody; finally, it must decide which class of antibody to make and how many long-lived plasma cells and memory cells to leave behind. The previous chapter ([7.15.19](/7.15.19)) described how B cells acquire their receptors; the help from the T-cell side, that is, the differentiation of **Th cells** and **follicular helper T cells**, is covered in [7.15.17](/7.15.17); the overall timeline of the immune response and T-cell memory are covered in [7.15.18](/7.15.18). How the antibodies produced here exert their effects is the subject of the next chapter ([7.15.21](/7.15.21)).

## 20.1. Responses to Thymus-Dependent Antigens: Two Signals

Antigens are divided according to whether B-cell activation requires T-cell help into **thymus-dependent antigens** (TD antigens, the vast majority of proteins) and **thymus-independent antigens** (TI antigens, §20.7). For TD antigens, full activation of the B cell requires two signals:

| Signal | Provided by | Content |
|---|---|---|
| Signal 1 | Antigen | Antigen cross-links the BCR; the **BCR complex** transmits the signal through Igα/Igβ and the **B-cell coreceptor** (C3d–CD21–CD19) amplifies it ([7.15.19](/7.15.19)) |
| Signal 2 | An activated Th cell specific for the same antigen | CD40L (CD154) on the Th cell binds CD40 on the B cell, the most important costimulation; ICOS–ICOSL, CD28–CD80/CD86 and other interactions occur at the same time |
| Cytokines | Th / Tfh cells | IL-21 (proliferation, plasma cell differentiation, maintenance of the germinal center), IL-4 (proliferation, switching to IgG1/IgE) and others, acting on the B cell in contact by directed secretion |

A B cell that receives signal 1 without T-cell help becomes anergic or undergoes apoptosis within a few days, which is one form of peripheral B-cell tolerance ([7.15.24](/7.15.24)).

How does a T cell find "its" B cell? The B cell binds a conformational epitope of the intact antigen with its BCR, internalizes and processes the antigen, and presents linear peptides from the same antigen to CD4⁺ T cells as peptide–MHC class II complexes. The epitope recognized by the B cell and the peptide recognized by the T cell can be completely different as long as they belong to the same molecule; this is called "linked recognition". The classical evidence is the **hapten–carrier effect** ([7.15.8](/7.15.8)): a strong secondary anti-hapten response is obtained only when the animal is reimmunized with the same carrier protein, because T-cell help is directed at carrier peptides. The same principle underlies the **conjugate vaccine**: when a bacterial polysaccharide is covalently attached to a protein carrier, B cells that recognize the polysaccharide receive help from T cells that recognize the carrier peptides ([7.15.33](/7.15.33)).

Where and when do they meet? T cells and B cells that recognize the same antigen are both very rare (each about $10^{-5}$–$10^{-6}$), and their meeting is arranged by a sequential switching of chemokine receptors:

| Time (after antigen contact) | Chemokine receptors of the B cell | Destination |
|---|---|---|
| Naive B cell | CXCR5 (ligand CXCL13, follicular stromal cells) | Patrols the FDC network within the follicle at about $6\,\mu\mathrm{m\,min^{-1}}$ |
| A few hours | Upregulates CCR7 (ligands CCL19/CCL21, T-cell zone) and EBI2 | Moves to the border between the B-cell zone and the T-cell zone and meets activated Th cells, which have upregulated CXCR5 |
| 1–3 days | Mainly EBI2 (ligand 7α,25-dihydroxycholesterol) | Outer edge of the follicle and interfollicular region; T–B pairs stay in contact for minutes to hours |
| About day 4 | Bifurcation: downregulates EBI2 and keeps CXCR5 → follicle center; or downregulates CXCR5 and upregulates CXCR4 → medullary cords (lymph node) or red pulp junction (spleen) | Germinal center, or extrafollicular plasmablast foci |

## 20.2. Fate Bifurcation: Extrafollicular Response and Germinal Center

The clone of B cells activated at the T–B border divides into three branches, and the progeny of a single B cell can appear in all three:

1. Extrafollicular response: some cells migrate to the medullary cords of the lymph node or the red pulp–white pulp junction of the spleen, form primary foci and rapidly differentiate into plasmablasts. A plasmablast is a cell that has begun to secrete antibody, can still proliferate and still carries a small amount of BCR; plasmablasts appear at about day 3, peak on days 7–8, essentially disappear within two weeks and mostly undergo apoptosis. They secrete low-affinity antibody without somatic mutation, at first IgM and on days 5–6 also IgG, which shows that class switching does not require entry into a germinal center. These antibodies provide protection in the first week of the response and form immune complexes that FDCs can trap.
2. Early memory B cells: memory cells produced before the germinal center forms, mostly IgM⁺ and unmutated.
3. **Germinal center**: the remaining cells enter the center of the follicle and proliferate, forming a **germinal center** (§20.3).

This bifurcation is decided by a pair of mutually inhibitory transcription factors:

- BCL6 is the master regulator of germinal center B cells (and also of Tfh cells), and mice lacking BCL6 have no germinal centers at all. It reduces expression of EBI2, induces AID and suppresses the DNA damage response, enabling cells to tolerate hypermutation;
- BLIMP-1 is the master regulator of plasma cells; it promotes splicing of secretory Ig mRNA and shuts off expression of MHC class II molecules and PAX5;
- BCL6 represses BLIMP-1 and BLIMP-1 also represses BCL6; the action of IRF4 depends on its concentration: a low level of IRF4 induces AID and supports the germinal center fate, whereas a high level of IRF4 activates BLIMP-1 and pushes the cell toward the plasma cell.

Mutual repression forms a bistable switch ([7.9.16](/7.9.16)), so a B cell is either a germinal center cell or a plasma cell and intermediate states are unstable; the stronger the BCR signal (the higher the affinity and the more T-cell help received), the higher the IRF4 and the more the cell tends toward the plasma cell.

## 20.3. Structure of the Germinal Center

**Definition 20.3.1 (Germinal Center Reaction)** The process in which activated B cells form a germinal center in the center of a secondary lymphoid follicle and undergo there rapid proliferation, somatic hypermutation, affinity-dependent selection and class switching, and finally produce high-affinity plasma cells and memory B cells is called the **germinal center reaction**.

The germinal center begins to form at about day 4 after antigen contact, shows mature zonation on day 7, is largest on days 7–12 (up to about $10^4$ cells) and usually regresses within 3–4 weeks; persistent antigen (for example in a chronic infection or after some vaccines) can sustain it for months. The proliferating B cells push the original naive B cells of the follicle to the periphery, where they form the mantle zone, rich in IgD⁺ cells. The interior of the germinal center is divided into two zones:

**Definition 20.3.2 (Dark Zone)** The region of the germinal center near the T-cell zone, densely packed with rapidly proliferating centroblasts, is called the **dark zone**. Stromal cells of the dark zone secrete CXCL12, which attracts centroblasts that express high levels of CXCR4; centroblasts express high levels of AID and of the error-prone DNA polymerase η, and the dark zone is where somatic hypermutation takes place.

**Definition 20.3.3 (Light Zone)** The region of the germinal center away from the T-cell zone, with sparser cells and containing a follicular dendritic cell network and Tfh cells, is called the **light zone**. B cells in the light zone are called centrocytes; they re-express MHC class II molecules and CD86 on their surface and here the mutated BCR is tested.

**Definition 20.3.4 (Follicular Dendritic Cell)** A cell that is located in lymphoid follicles, differentiates from stromal (mesenchymal) precursors rather than from hematopoietic cells, expresses high levels of complement receptors (CR1, CR2) and Fc receptors, and keeps intact antigen on its surface for a long time, in the form of immune complexes or coated with complement, for recognition by B cells is called a **follicular dendritic cell** (FDC).

The FDC resembles the ordinary **dendritic cell** in name but is different in nature: it does not express MHC class II molecules and does not process or present peptides; what it displays is unprocessed intact antigen, which can be retained on its surface for weeks to months. It also secretes CXCL13 and organizes the structure of the follicle. Thus "displaying antigen to B cells" by FDCs is not **antigen presentation** in the classical sense.

![Structure of the germinal center. In a secondary lymphoid follicle, the germinal center is surrounded by the mantle zone of naive IgM⁺IgD⁺ B cells. In the dark zone near the T-cell zone, centroblasts proliferate rapidly and undergo somatic hypermutation (AID; CXCR4 and CXCL12 from stromal cells keep them in the dark zone). In the light zone, follicular dendritic cells (pink) keep antigen (green) on their surface, centrocytes compete for antigen with their mutated BCRs and process it into peptides presented to Tfh cells (red) in exchange for help in the form of CD40L and IL-21. Cells of the dark zone enter the light zone at a rate of about 15% per hour; in the light zone only about 10%–30% of the cells are selected and return to the dark zone for the next round of proliferation and mutation, while most of the rest undergo apoptosis and are cleared by tingible body macrophages, or leave the germinal center and differentiate into plasmablasts (later long-lived plasma cells in the bone marrow) and memory B cells](./plots/germinal-center.py)

## 20.4. Somatic Hypermutation and Affinity Maturation

**Somatic hypermutation** (mechanism in [7.15.12](/7.15.12)) begins with cytidine deamination in the V region by AID; error-prone repair then introduces point mutations in the V regions of the heavy and light chains, at a rate of about $10^{-3}$ per base pair per division, about $10^5$–$10^6$ times above the genomic background. A V region of about 300 bp therefore acquires an average of about 0.3 mutations per division, concentrated in AID-preferred hotspot sequences in the CDRs. It occurs only in germinal centers, requires help through CD40–CD40L, and acts on the V region but not on the C region.

**Definition 20.4.1 (Affinity Maturation)** The phenomenon in which, during the immune response to a thymus-dependent antigen, the mean affinity of the antibodies produced for the antigen rises gradually with time and repeated immunization, because somatic hypermutation and affinity-dependent selection are repeated in the germinal center, is called **affinity maturation**.

The mutations themselves are random, and most of them lower affinity or even destroy BCR expression; the improvement in affinity comes entirely from selection. The current understanding of the selection mechanism is as follows:

1. After a dark zone cell enters the light zone, it must "capture" antigen from the surface of the FDC with its new BCR. The higher the affinity, the more antigen it captures;
2. The B cell processes the captured antigen and presents it to Tfh cells. Tfh cells are limited in number and preferentially form long-lasting contacts with the B cells that have the highest peptide–MHC density on their surface;
3. B cells that receive more help divide more often after returning to the dark zone, have a shorter S phase, and their progeny increase in proportion; cells that lose the BCR or receive no help undergo apoptosis within hours (germinal center B cells express high levels of Fas and low levels of Bcl-2, and their default fate is death).

The stringency of selection also increases with time: antibody secreted by early plasmablasts binds antigen on the FDC and competes with the BCR, so antigen becomes ever harder to obtain and low-affinity cells gradually lose their chance. In the mouse, photoactivation tracing has shown that about 15% of dark zone cells enter the light zone per hour and about 3% of light zone cells return to the dark zone per hour, which translates into about 10%–30% of the light zone cells being selected to continue cycling in each round.

**Example 20.4.1 (Stochastic Simulation of Affinity Maturation)** A germinal center can be written as a stochastic "mutation–selection" process (a selection and drift model from population genetics, [7.10](/7.10); for the language of random sampling see [3.1](/3.1)). Each B cell has an affinity $a = \log_{10}(K_{\mathrm{A}}/\mathrm{M^{-1}})$, and one cycle (about 12 hours) consists of:

1. Selection: the antigen captured by a cell is proportional to the occupancy of its BCR,

   $$
   w_i = \frac{K_{\mathrm{A},i}\,c}{1 + K_{\mathrm{A},i}\,c},
   $$
   where $c$ is the concentration of free antigen available on FDCs, which falls from $10^{-6}\,\mathrm{M}$ to $10^{-9}\,\mathrm{M}$ over time; Tfh help is limited, so in each round only $N_{\mathrm{sel}} = 500$ cells are drawn with weights $w_i$;
2. Proliferation and mutation: selected cells divide twice, and each daughter cell acquires $\mathrm{Poi}(0.3)$ mutations; each mutation destroys the BCR with probability 0.3 (the cell dies), and otherwise changes $a$ by a normal random amount with a mean slightly below 0 and a standard deviation of 0.25, the effect of favorable mutations becoming smaller as $a$ approaches the upper limit $a_{\max} = 10$.

All parameters are illustrative values that give only the order of magnitude. The control experiment keeps the same mutation process but makes selection independent of affinity.

![Stochastic simulation of affinity maturation in the germinal center (parameters are illustrative, see Example 20.4.1). A: the distribution of BCR affinity $\log_{10} K_{\mathrm{A}}$ over time (the brighter the color, the higher the fraction of cells; the white dashed line is the mean): the whole distribution shifts upward, and the mean affinity rises by about two and a half orders of magnitude within three weeks. B: mean affinity. With selection (blue line) the mean affinity roughly follows the inverse of the available antigen concentration (gray dotted line, $-\log_{10} c$), because only cells with $K_{\mathrm{A}} c \gtrsim 1$ can capture enough antigen; with mutation only and no affinity-dependent selection (red dashed line) the mean affinity actually falls, because most mutations are harmful. C: clonal diversity. With selection, the 40 starting clones are rapidly replaced by a few high-affinity clones and the effective number of clones $1/\sum f_i^2$ ($f_i$ is the fraction of clone $i$) falls to about 2; without selection the number of clones also declines through random drift, but much more slowly](./plots/affinity-maturation.py)

The simulation gives three conclusions that agree with experiments:

- Affinity maturation requires selection; mutation alone only lowers affinity.
- The less antigen, the more stringent the selection and the higher the affinity. This explains why booster immunizations with a low dose and a long interval often yield antibodies of higher affinity.
- Selection reduces clonal diversity, and in responses to simple haptens one clone often "wins"; in real responses to complex antigens, clones against different epitopes can coexist for a long time within one germinal center, and diversity is higher than in the model.

The measured magnitude of affinity maturation is usually 10- to 1000-fold. Self-reactive BCRs that newly arise in germinal centers are mostly eliminated because they receive no Tfh help (the corresponding T cells have been made tolerant), or undergo apoptosis within hours after meeting soluble self antigen; but this test is not perfect, and low-affinity autoantibodies can often be detected after severe infections.

:::

## 20.5. Class Switching

**Class switch recombination** (mechanism in [7.15.12](/7.15.12)) replaces the $C_\mu$ downstream of the heavy-chain V region with $C_\gamma$, $C_\alpha$ or $C_\varepsilon$ and deletes the intervening DNA; the variable region is unchanged, so the specificity of the antibody is unchanged, and what changes is the **isotype** of the antibody and the effector functions and distribution associated with it ([7.15.21](/7.15.21)). Switching requires two kinds of signals:

- CD40 signaling (or TLR signaling) induces AID. The serum of patients with X-linked hyper-IgM syndrome, who lack CD40L, contains almost only IgM; they have no germinal centers and no memory B cells, and their antibodies carry no somatic mutations ([7.15.31](/7.15.31));
- Cytokines determine which isotype is switched to: a cytokine first induces germline transcription of the corresponding switch region, making the DNA of that switch region accessible, and AID can act only on a switch region that is being transcribed.

| Cytokine | Human | Mouse | Corresponding effector module |
|---|---|---|---|
| IL-4, IL-13 | IgE, IgG4 | IgE, IgG1 | Type 2 immunity: parasites and allergy |
| IFN-γ | IgG1, IgG3 (weaker) | IgG2a (IgG2c), IgG3 | Type 1 immunity: opsonization, complement, activation of phagocytes |
| IL-21, IL-10 | IgG1, IgG3 | — | Strong opsonization and complement activation |
| TGF-β (together with BAFF, APRIL, retinoic acid) | IgA | IgA, IgG2b | Mucosal barrier ([7.15.23](/7.15.23)) |

The choice among **type 1 immunity**, **type 2 immunity** and **type 3 immunity** ([7.15.1](/7.15.1)) is thus expressed on the humoral side as the choice of antibody isotype. Class switching can proceed only downstream along the order of the C genes on the chromosome (in humans: μ, δ, γ3, γ1, α1, γ2, γ4, ε, α2), because the DNA in between is deleted; a cell can switch from IgM to IgG1 and then to IgE or IgA, but cannot return to IgM. Class switching begins early in the response, before the germinal center forms, and can also occur in TI responses; somatic hypermutation occurs only in germinal centers and, in mice and humans, only in TD responses.

## 20.6. Plasma Cells and Memory B Cells

B cells that leave the germinal center differentiate into two kinds of cells that maintain humoral immunity for the long term, and they are produced at different times: cells that leave early (around days 6–8) are mainly memory B cells with fewer mutations and a higher proportion of IgM⁺ cells; from about day 10 onward, more and more cells upregulate plasma cell transcription factors and become plasmablasts with more mutations and higher affinity.

**Definition 20.6.1 (Long-Lived Plasma Cell)** A terminally differentiated plasma cell that resides in specific niches such as the bone marrow, no longer proliferates, secretes antibody at a very high rate without further antigenic stimulation and can live for years or even a lifetime is called a **long-lived plasma cell** (LLPC).

A plasma cell can secrete thousands of antibody molecules per second, its cytoplasm is filled with rough endoplasmic reticulum, and it essentially no longer expresses the BCR or MHC class II molecules on its surface, so it is no longer regulated by antigen and can no longer interact with Th cells. The survival of long-lived plasma cells depends on the bone marrow niche: CXCL12 from mesenchymal stromal cells (binding CXCR4), APRIL (binding BCMA) from eosinophils and megakaryocytes, IL-6, and the antiapoptotic protein Mcl-1 maintained by these signals. The number of niches is limited, and newly produced plasmablasts must compete with existing plasma cells. Specific antibodies can still be detected 75 years after smallpox vaccination, which shows that the life span of some long-lived plasma cells approaches that of a human.

| | Naive B cell | Plasmablast | Long-lived plasma cell |
|---|---|---|---|
| Membrane BCR | High | Intermediate | Low or none |
| Proliferation | Not proliferating (resting) | Proliferating | Not proliferating |
| Life span | Weeks to months | Days | Years to lifetime |
| CD19, CD20, MHC II | High | Intermediate | Low or none |
| CD38, CD138, CXCR4 | Low | Intermediate | High |
| Location | Lymphoid organs | Lymphoid organs and blood | Bone marrow, mucosa |
| Transcription factors | PAX5; BCL6 low | BLIMP-1, IRF4 | BLIMP-1 high, XBP1 |

**Definition 20.6.2 (Memory B Cell)** A B cell that is generated in the primary response, is resting, long-lived and able to recirculate, expresses a BCR that has undergone class switching or somatic mutation (or both), and on meeting the same antigen again proliferates and differentiates into plasma cells faster and more strongly than a naive B cell is called a **memory B cell**.

Memory B cells outnumber their naive precursors, express more CD40, CD80/CD86 and antiapoptotic proteins, signal more strongly through the BCR and enter the cell cycle faster; in humans they are mostly CD27⁺. They fall into two classes with different roles:

- Class-switched (IgG⁺ and so on) high-affinity memory cells: they can capture antigen even while antibody is still present in the serum, differentiate rapidly into plasma cells in the secondary response, and generally no longer enter germinal centers;
- IgM⁺ low-affinity memory cells: they are easily inhibited by existing antibody, respond only after antibody levels have fallen, and reenter germinal centers to continue mutating. They keep a reserve that "can still be optimized" for coping with variants of the antigen (for example viral surface proteins that undergo **antigenic drift**).

At the end of the primary response (days 14–18), the great majority of the expanded B cells undergo apoptosis, leaving only memory cells and long-lived plasma cells; Fas–FasL takes part in this contraction. The long-term titer of protective antibody is maintained by long-lived plasma cells, and the rapid response at reinfection is supplied by memory B cells; together these two mechanisms constitute the **immunological memory** of humoral immunity.

## 20.7. Responses to Thymus-Independent Antigens

TI antigens can induce antibody without T-cell help and fall into two classes:

| | TD antigens | TI-1 antigens | TI-2 antigens |
|---|---|---|---|
| Examples | Most proteins | Bacterial components such as LPS (mostly TLR ligands) | Highly repetitive molecules such as capsular polysaccharides and polymeric flagellin |
| Mode of activation | BCR + T-cell help | BCR + mitogen receptors such as TLRs; at high concentrations, polyclonal activation without the BCR | Extensive cross-linking of BCRs by multivalent antigen |
| Antibody produced in animals without T cells | No | Yes | Yes |
| Responding cells | Follicular B cells | Both mature and immature B cells | Mature B cells, mainly marginal zone B and B-1 cells |
| Antibody | All classes, affinity maturation | Mainly IgM, low affinity | Mainly IgM, some IgG (BAFF and APRIL secreted by DCs can induce switching) |
| Germinal center and memory | Yes | Essentially none | Very weak |

At low concentrations of a TI-1 antigen, only the B cells whose BCR can bind the antigen and concentrate it at the cell surface are activated and produce specific antibody; at high concentrations, the TLR signal alone is sufficient to activate large numbers of B cells of different specificities, that is, the antigen acts as a **mitogen** and causes polyclonal activation. TI-2 antigens rely on multivalent repetitive epitopes to cross-link many BCRs at the same time, and the signal strength depends on epitope density; excessive cross-linking leads instead to anergy.

The significance of TI responses lies in speed: the capsular polysaccharides of extracellular bacteria cannot be presented by MHC and T cells cannot help, and the IgM produced within days by marginal zone B and B-1 cells can activate **complement** and cause **opsonization**, controlling infection before the TD response takes shape. The human marginal zone does not mature until about 2 years of age, so infants respond poorly to pure polysaccharide antigens, which is exactly why polysaccharide vaccines are made into **conjugate vaccines** ([7.15.33](/7.15.33)).

## 20.8. General Rules of the Humoral Response

The differences between the **primary immune response** and the **secondary immune response** ([7.15.18](/7.15.18)) are most obvious on the antibody side:

| | Primary response (naive B cells) | Secondary response (memory B cells) |
|---|---|---|
| Amount of antigen required | Large | Small |
| Lag period | 4–7 days | 1–3 days |
| Time to peak | 7–10 days | 3–5 days |
| Amount of antibody | Smaller | Usually 10–1000 times higher and long-lasting |
| Main classes | IgM predominant early, IgG later | IgG predominant (IgA in mucosa) |
| Affinity | Low | High (result of affinity maturation) |
| Antigens that can induce it | TD and TI | Mainly TD |

![Clonal selection and the primary and secondary antibody responses. A: each naive B cell has only one specificity; antigen selects the cells whose receptors match it, and with T-cell help this clone expands and differentiates into antibody-secreting plasma cells (secreting IgM first and then IgG) and long-lived memory B cells. B: a minimal kinetic model including antigen, IgM-secreting and IgG-secreting B cells, memory cells and serum antibody (serum half-life 5 days for IgM and 21 days for IgG; the other parameters are illustrative). Antibody appears only about a week after the first contact, with IgM preceding IgG; when the same antigen is given again on day 60, memory cells make the response almost free of lag, with a peak more than about one order of magnitude higher and dominated by IgG](./plots/antibody-response.py)

These differences are a summary of the sections of this chapter: memory B cells are numerous and have a low activation threshold (short lag period, little antigen needed), have already completed class switching (IgG predominant) and affinity maturation (high affinity), and the secondary response produces a new batch of long-lived plasma cells (long duration). The timing of booster immunization is determined by this too: enough time must be left between two vaccinations for the germinal center reaction and the formation of memory; if the interval is too short, antibody left over from the first response binds the antigen and weakens the stimulation of memory cells.

## Summary

- Two signals: antigen cross-links the BCR (signal 1); a Th cell specific for the same antigen provides signal 2 through CD40L–CD40 together with IL-21 and IL-4. The B cell presents peptides of the antigen to the T cell, so T and B cells recognize different parts of the same molecule (linked recognition, the **hapten–carrier effect**, the **conjugate vaccine**).
- Three fates: extrafollicular plasmablasts (fast, low affinity, unmutated), early memory cells, and the germinal center; decided by a bistable switch between BCL6 and BLIMP-1/IRF4.
- **Germinal center reaction** (Definition 20.3.1): proliferation and mutation in the **dark zone**, selection in the **light zone** through antigen on **FDCs** and Tfh help; selection determines the direction and mutation only supplies variation (Example 20.4.1).
- **Affinity maturation** (Definition 20.4.1): affinity rises 10- to 1000-fold with time and repeated immunization; the less antigen, the more stringent the selection.
- **Class switching**: CD40 signaling induces AID and cytokines determine the isotype: IL-4 → IgE (IgG4 in humans, IgG1 in the mouse), IFN-γ → human IgG1/IgG3 (mouse IgG2a), TGF-β → IgA; type 1/2/3 immunity on the humoral side.
- Long-term maintenance: **long-lived plasma cells** (Definition 20.6.1) maintain the antibody titer in bone marrow niches; **memory B cells** (Definition 20.6.2) supply the rapid secondary response.
- TI antigens: TI-1 (TLRs and so on, polyclonal at high concentration) and TI-2 (repetitive epitopes cross-link the BCR; marginal zone B and B-1 cells), fast but without affinity maturation or significant memory.

## Questions

1. Use the model of Example 20.4.1 to explain why plasma cells produced later in a response secrete antibody of higher affinity. If a large dose of the same antigen is given on day 7, how does the model predict that affinity maturation will change?

   **Answer** Later plasma cells come from germinal center cells that have gone through more rounds of the mutation–selection cycle, when the antigen concentration is lower and selection is more stringent, so the surviving cells have a higher mean affinity. If a large dose of antigen is given on day 7, $c$ rises abruptly, the occupancy $K_{\mathrm{A}}c/(1 + K_{\mathrm{A}}c)$ of almost all cells approaches 1, the weights $w_i$ hardly differ, and selection becomes independent of affinity; during this period the rise in mean affinity stops or even reverses because of harmful mutations, until the antigen has been consumed and its concentration has fallen again. This agrees with the experience that antibody obtained by high-dose immunization has lower affinity.

2. Why do patients deficient in CD40L lack IgG, IgA and IgE, lack somatic mutations in their antibodies and lack memory B cells, while IgM is normal or even elevated?

   **Answer** CD40–CD40L signaling is the key signal in TD responses for inducing AID, forming and maintaining the germinal center and keeping germinal center B cells alive. Without it, AID induction is insufficient, and neither class switching nor somatic hypermutation can proceed efficiently, so switched isotypes and mutations are lacking; germinal centers cannot form, so the memory B cells that depend on them are also few. IgM can still be produced by extrafollicular responses and TI responses that need no class switching, and with no exit through switching, IgM accumulates instead.

3. The FDC and the classical dendritic cell are both called "dendritic cells". Compare them in origin, surface molecules and function, and explain why it is essential for affinity maturation that FDCs display intact antigen and not peptides.

   **Answer** Origin: FDCs come from stromal (mesenchymal) precursors and classical DCs from hematopoietic myeloid precursors. Surface molecules: FDCs express high levels of CR1, CR2 and Fc receptors and do not express MHC class II molecules; classical DCs express high levels of MHC class II molecules and costimulatory molecules. Function: FDCs keep unprocessed intact antigen on the surface for a long time for binding by the BCRs of B cells; classical DCs process antigen into peptides and present them to T cells as peptide–MHC complexes. The BCR recognizes conformational epitopes of intact antigen, and affinity maturation tests the ability of the mutated BCR to bind these epitopes, so intact antigen in its native conformation is needed; peptide–MHC complexes cannot be used for this test.

4. Why does the primary response begin with IgM? Explain from the gene structure and the molecular structure.

   **Answer** Gene structure: the constant region gene nearest downstream of the rearranged VDJ is $C_\mu$ (followed by $C_\delta$); switching to other isotypes needs AID and T-cell signals and takes several days, so the earliest plasmablasts secrete IgM. Molecular structure: secreted IgM is a pentamer with 10 antigen-binding sites, so even if the affinity of each site is low, multivalent binding gives a high **avidity**, and a single IgM molecule can activate the classical pathway of complement, which suits it to act before affinity maturation.

5. (Open question) Memory B cells include IgM⁺ cells that are easily inhibited by existing antibody and class-switched cells that are not. From the standpoint of coping with pathogen variation, discuss the benefits and costs of this division of labor.

   **Answer** Key points: class-switched high-affinity memory cells can respond while antibody is still present, rapidly producing large amounts of high-affinity antibody against the original epitope, which suits an antigen that reappears unchanged; but they generally no longer enter germinal centers and can hardly be optimized again. IgM⁺ memory cells have lower affinity and a broader cross-reactivity, respond after antibody levels have fallen and reenter germinal centers; starting from a point that is "not yet overspecialized", they can mutate and be selected again against variant epitopes, which leaves room for variation such as antigenic drift. The costs are that the secondary response is dominated first by existing memory cells against the original epitope ("original antigenic sin"), so the response to a new epitope may be weak; and that maintaining two kinds of memory cells occupies limited survival niches.
