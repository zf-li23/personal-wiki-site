---
title: "The Immune Response in Space and Time: From Infection to Memory"
description: "Putting the molecules and cells of the preceding chapters back into the body: the distribution of immune cells at steady state; the timeline of a primary response from the local innate response through activation in the lymph node, homing of effector cells, clearance, contraction and memory; the two forms in which antigen reaches the lymph node; the search problem of rare lymphocytes; a three-layer kinetic model; tertiary lymphoid structures; and the connection to spatial omics."
source_hash: 2861f773020f
---

The preceding chapters answered, one by one, the five questions on the knowledge path: who recognizes, what is recognized, how the decision is made, with which effectors, and how the response is remembered and shut off ([7.15.1](/7.15.1)). But each question is answered at a particular place and a particular moment: innate cells at the site of infection, T cells in the paracortex of the lymph node, B cells in the follicles and germinal centers, plasma cells in the bone marrow, tissue-resident memory cells on barrier surfaces. This chapter arranges these fragments in a single spatiotemporal map and shows how a primary response unfolds across several organs within two or three weeks. The anatomy of the organs and of lymphocyte recirculation is described in [7.15.3](/7.15.3), adhesion molecules and chemokines in [7.15.4](/7.15.4), the dynamics of T-cell responses and memory in [7.15.18](/7.15.18), and the B-cell side in [7.15.20](/7.15.20); the particularities of barrier tissues are the subject of the next chapter ([7.15.23](/7.15.23)).

## 22.1. Distribution at Steady State

Immune cells do not simply "float" uniformly in the blood. An adult has about $5 \times 10^{11}$ lymphocytes, of which only about 2% are in the blood at any moment; the rest are distributed in lymphoid organs and nonlymphoid tissues:

| Site | Main cells | State |
|---|---|---|
| Blood | Neutrophils, monocytes; naive and central memory lymphocytes | In transit; lymphocytes stay in the blood for only about half an hour |
| Lymph nodes, spleen | Naive T and B cells, **central memory T cells**; DCs; stromal cells such as **follicular dendritic cells** and fibroblastic reticular cells | Brief stay during recirculation (6–24 h per lymph node) |
| Bone marrow | Hematopoietic progenitors, B-cell precursors, **long-lived plasma cells**, some memory T cells | Production and long-term maintenance |
| Barrier tissues such as skin, gut and lung | **Tissue-resident macrophages**, DCs, **innate lymphoid cells**, **tissue-resident memory T cells**, IgA plasma cells, **intraepithelial lymphocytes** | Long-term residence, no recirculation; human skin contains about $2 \times 10^{10}$ T cells, about twice as many as the blood |
| Other parenchymal organs (liver, brain, kidney and so on) | Tissue-specific resident macrophages (Kupffer cells, microglia and so on), a few resident lymphocytes | Steady-state surveillance |

Two rules run through the chapter:

1. Sentinels are in the periphery, decisions are made in lymphoid organs. The first to meet a pathogen are the innate cells and memory cells resident in tissues; activation of naive lymphocytes occurs almost only in secondary lymphoid organs, because only there can the rare antigen-specific lymphocytes, the antigen-bearing DCs and the helper cells be brought together.
2. Position is state. The same cell type executes different programs at different positions: macrophages of the splenic red pulp clear aged red blood cells, macrophages of the subcapsular sinus of the lymph node capture particulate antigen in the lymph, and alveolar macrophages clear surfactant; CD8⁺ T cells in lymph nodes are mostly naive or central memory cells, whereas CD8⁺ T cells in the epidermis of the skin are mostly CD69⁺CD103⁺ resident memory cells. When reading immune cells in a tissue section, position is as important as phenotype (§22.9).

## 22.2. Timeline of a Primary Response

![Space and time of a primary response. Top: resident cells (sentinels) in the infected tissue sense the pathogen and recruit neutrophils and monocytes within hours; dendritic cells (DCs) take up antigen and migrate through afferent lymphatics to the draining lymph node (1–2 days), whereas free antigen arrives with the lymph within minutes. In the lymph node, naive T cells scan DCs in the T-cell zone, and activated B cells receive help at the T–B border and later form germinal centers in the follicles. Effector T cells and antibody secreted by plasma cells enter the blood through the efferent lymphatics and the thoracic duct and return to the inflamed tissue (dashed lines). Bottom: the timeline of the same process: innate response and inflammation (days 0–1), DC migration (days 0.5–2), T-cell activation and expansion (days 1–5), B-cell activation and extrafollicular plasmablasts (days 2–8), germinal center (days 5–21), effector T cells clearing the pathogen in the tissue (days 5–12), contraction and memory (after day 12)](./plots/space-time.py)

| Time | Place | Event | Chapter |
|---|---|---|---|
| 0–4 h | Site of infection | Epithelium, resident macrophages and mast cells sense PAMPs and DAMPs through **pattern recognition receptors** and release IL-1, TNF, IL-6 and chemokines; complement is activated | [7.15.6](/7.15.6), [7.15.7](/7.15.7) |
| Hours–1 day | Site of infection | **Neutrophils** arrive first through the **leukocyte adhesion cascade**, followed by monocytes; NK cells and ILCs secrete early cytokines (such as IFN-γ) | [7.15.4](/7.15.4), [7.15.5](/7.15.5) |
| Minutes–hours | Draining lymph node | Soluble small antigens and particulate antigens arrive with the lymph and are captured by DCs and subcapsular sinus macrophages in the lymph node | §22.3 |
| 12 h–2 days | Afferent lymph → lymph node | Activated tissue DCs upregulate CCR7, migrate into the T-cell zone and present antigen with peptide–MHC and costimulatory molecules; the lymph node "shuts" its exit and increases blood flow through HEVs | [7.15.14](/7.15.14) |
| 1–5 days | T-cell zone of the lymph node | Rare naive T cells find their cognate DCs, are activated and undergo **clonal expansion** (dividing once every 6–8 h), and differentiate into effector subsets | [7.15.16](/7.15.16), [7.15.17](/7.15.17) |
| 2–8 days | T–B border, medullary cords | B cells receive T-cell help, and some form extrafollicular plasmablasts that secrete early IgM and IgG | [7.15.20](/7.15.20) |
| 4–21 days | Follicles | **Germinal center reaction**, affinity maturation and class switching | [7.15.20](/7.15.20) |
| From day 4–7 | Blood → site of infection | Effector T cells regain S1PR1, leave the lymph node and enter inflamed tissue according to the homing receptors they have acquired; antibody arrives with the blood | §22.5 |
| 6–12 days | Site of infection | The pathogen is cleared (most acute infections) | [7.15.32](/7.15.32) |
| 10–30 days | Whole body | After the antigen has disappeared, 90%–95% of effector cells undergo apoptosis (contraction), leaving memory T and B cells and long-lived plasma cells | §22.6 |

The longest segment of the timeline is the 4–7 days from infection to the appearance of adaptive effector cells. During this time only innate immunity controls the pathogen, so the ratio of the length of this "delay" to the growth rate of the pathogen determines the severity of an infection (the model of §22.5).

## 22.3. How Antigen Reaches the Lymph Node

Naive lymphocytes do not enter nonlymphoid tissues, so antigen must be brought to them. The lymphatic system (**lymph**, **lymphatic system**, [7.14.31](/7.14.31)) connects each piece of tissue with one or several draining lymph nodes, and antigen arrives in two forms:

| | Unprocessed antigen | Antigen processed by DCs |
|---|---|---|
| Form | Soluble protein, particles, viruses, or complexes with complement or antibody | Peptide–MHC complexes on the surface of migratory DCs |
| Time of arrival | Minutes to hours | 12 h to several days |
| Route of entry | Enters the subcapsular sinus with the afferent lymph; molecules smaller than about 70 kDa enter the T-cell zone along conduits sheathed by fibroblastic reticular cells and are taken up by resident DCs there; larger particles are retained by subcapsular sinus macrophages and handed over to B cells in the follicles | DCs upregulate CCR7, enter afferent lymphatics along a CCL21 gradient and then enter the T-cell zone |
| Recognized by | B cells (which recognize intact conformational epitopes); nonspecific B cells can also use the complement receptor CR2 to "carry" complement-coated antigen to FDCs | T cells |

B cells and T cells therefore recognize two forms of the same antigen in different regions of the same lymph node and then meet at the T–B border ([7.15.20](/7.15.20)). The spleen has no afferent lymphatics and captures antigen from the blood: after blood flows into the marginal sinus its velocity falls sharply, and macrophages, DCs and **marginal zone B cells** of the marginal zone come into direct contact with blood-borne antigen; processed antigen is carried by DCs into the T-cell zone of the white pulp ([7.15.3](/7.15.3)).

## 22.4. The Search Problem

Naive T cells that recognize a given peptide–MHC are very few: in the mouse there are only about 20–200 naive CD4⁺ T cells specific for one epitope, of the order of $10^{-6}$ of all T cells; the frequency in humans is comparable. They must find, among hundreds of lymph nodes in the body, the few dozen DCs that are presenting this peptide in the draining lymph node. The part of this "needle in a haystack" problem that takes place within a single lymph node was estimated with a random walk in [7.15.3](/7.15.3): when a few dozen cognate DCs are present, a T cell entering the lymph node is likely to find them during one stay. The remaining question is how long it takes before the precursor cells reach the right lymph node.

**Example 22.4.1 (Time to Recruitment to the Draining Lymph Node)** Suppose there are $n$ naive T cells specific for an epitope, each cell enters a lymph node on average once per day (each stay lasting about 12–24 h), the probability that the node entered is the draining lymph node is $q$ (the fraction of the whole-body lymphocyte flow that this node receives), and the probability of finding a cognate DC after entry is $s$. Treating recruitment of each cell per day as an independent event, the number of cells recruited within $t$ days is approximately Poisson distributed with mean

$$
\lambda(t) = n\,q\,s\,t ,
$$
and the probability that at least one precursor has been recruited is $1 - \mathrm{e}^{-\lambda(t)}$ ([3.1](/3.1)). Take $n = 100$, $q = 0.01$, $s = 0.8$: then only 0.8 cells are recruited per day on average, and the probability of recruiting at least one on the first day is about 55%.

This estimate illustrates three points:

- A primary response takes several days to form, partly because time is spent "looking for the right cell";
- Several changes in the draining lymph node after infection serve to raise the recruitment rate: inflammation increases blood flow to the lymph node and the permeability of HEVs several-fold ($q$ increases); activated cells downregulate S1PR1 through CD69, so all lymphocytes stay longer in the lymph node (the lymph node "shuts", $s$ increases); and the lymph node itself enlarges several-fold within days. Raising $q$ only threefold already brings the probability of recruiting a precursor on the first day above 90%;
- Once a few precursors have been recruited, their **clonal expansion** (dividing once every 6–8 h, increasing $10^3$–$10^4$-fold within a week) makes up for the scarcity of the starting numbers; and memory cells are 10 to 1000 times more numerous than naive precursors, with some of them resident in barrier tissues, so the secondary response hardly needs this search phase (§22.6).

:::

## 22.5. The Effector Phase: Homing and Clearance

After proliferation ends, activated lymphocytes re-express S1PR1 and leave the lymph node. Where the effector cells go is determined by the homing molecules they acquire at activation: DCs in the lymph node draining a tissue "stamp" the T cells with the address of that tissue.

| Site of activation | Signal from the DC | Homing molecules acquired by the T cell | Destination |
|---|---|---|---|
| Mesenteric lymph nodes, Peyer's patches | Retinoic acid (a vitamin A metabolite) | Integrin α4β7, CCR9 | Small intestinal lamina propria (MAdCAM-1 and CCL25 on endothelium) |
| Skin-draining lymph nodes | Vitamin D metabolites and others | Cutaneous lymphocyte antigen (CLA, a P/E-selectin ligand), CCR4, CCR10 | Skin (E-selectin, CCL17, CCL27) |
| Lung-draining lymph nodes | — | CCR4, CCR8 and others | Lung |

At sites of inflammation the endothelium upregulates E-selectin, P-selectin, ICAM-1 and VCAM-1, tissues secrete chemokines, and effector cells enter the tissue through the **leukocyte adhesion cascade**; different effector subsets respond to different chemokines (Th1 cells and CTLs respond through CXCR3 to CXCL9/10 induced by IFN-γ, Th2 cells through CCR4 and CCR8, Th17 cells through CCR6), so the type of inflammation itself determines the type of effector cells recruited. Some plasma cells remain in the medullary cords of the lymph node and some enter the bone marrow or mucosa, while antibody is distributed throughout the body with blood and tissue fluid.

**Example 22.5.1 (A Three-Layer Race Between Innate and Adaptive Immunity)** An infection can be compressed into four variables (all relative quantities, with illustrative parameters): pathogen $P$ ($P = 1$ is the maximum load), innate effectors $I$, adaptive effectors $E$ and memory $M$:

$$
\begin{aligned}
\frac{\mathrm{d}P}{\mathrm{d}t} &= rP(1-P) - k_I I P - k_E E P, \\
\frac{\mathrm{d}I}{\mathrm{d}t} &= s_I \frac{P}{P+h} - d_I I, \\
\frac{\mathrm{d}E}{\mathrm{d}t} &= \rho\, a(t)\,(E + M)(1 - E) - d_E \bigl(1 - a(t)\bigr)(E - E_0), \\
\frac{\mathrm{d}M}{\mathrm{d}t} &= \phi\, d_E \bigl(1 - a(t)\bigr)(E - E_0) - d_M M,
\end{aligned}
$$
where

$$
a(t) = \frac{P(t-\tau)}{P(t-\tau) + h_A}
$$
is the antigen signal "seen" by the adaptive cells, and the delay $\tau$ represents the time needed for antigen to be carried to the lymph node, for activation, and for the effector cells to return to the tissue. $r$ is the growth rate of the pathogen, $k_I, k_E$ are the killing efficiencies of the two kinds of effector, $\rho$ is the rate of clonal expansion, $E_0$ is the number of naive precursors and $\phi$ is the fraction converted to memory after contraction. This adds a layer of delayed adaptive response on top of the innate race of [7.15.7](/7.15.7); delay differential equations and stability are discussed in [2.4](/2.4), and a similar race structure appears in the signaling decisions of [7.9.16](/7.9.16).

![The three-layer race model between innate and adaptive immunity (Example 22.5.1, illustrative parameters). A: a primary infection ($r = 2\,\mathrm{d^{-1}}$, $\tau = 4\,\mathrm{d}$). Innate effectors (green) rise within hours and can only slow the growth of the pathogen (red); adaptive effector cells (blue), after the delay, expand exponentially from very few precursors, clear the pathogen at about day 10, then contract, leaving a fraction as memory cells (green dashed line). The yellow band is the delay period. B: peak pathogen load ($\log_{10}$) as a function of the adaptive delay $\tau$ and the pathogen growth rate $r$; the white lines are the contours of peak $10^{-2}$ and $10^{-1}$. Slowly growing pathogens ($r$ below the maximum killing rate of innate immunity $k_I I_{\max} = 1.5\,\mathrm{d^{-1}}$) are controlled mainly by innate immunity and the peak is almost independent of $\tau$; fast-growing pathogens reach a high load before the adaptive response arrives, and each additional day of delay raises the peak markedly. C: reinfection with the same pathogen: memory cells raise the starting point of the adaptive effectors several thousand-fold and shorten the delay to 1.5 days, and the pathogen is cleared at a peak two orders of magnitude lower](./plots/three-layer-race.py)

The point of the model is that innate immunity determines "how fast the pathogen can grow" and adaptive immunity determines "when it stops". For a fast-growing pathogen, the delay of the adaptive response is a fatal weakness; this explains why the immune system places resident memory cells in advance in barrier tissues, and also why the value of vaccines lies mainly in shortening the delay and raising the starting point (panel C, [7.15.33](/7.15.33)).

:::

## 22.6. Contraction and the Location of Memory

After the antigen has been cleared, antigen signals and survival signals such as IL-2 disappear, and 90%–95% of the expanded effector cells undergo apoptosis within one to two weeks (mainly through the Bim-mediated intrinsic pathway, with participation of the Fas pathway). The memory cells that remain are not concentrated in one place but are distributed according to "where antigen may be met again":

| Memory population | Location | Features |
|---|---|---|
| **Central memory T cells** | Lymph nodes, spleen (CCR7⁺CD62L⁺) | High proliferative potential; expand rapidly in lymphoid organs on meeting antigen again |
| **Effector memory T cells** | Recirculate between blood and nonlymphoid tissues | Rapidly produce effector molecules |
| **Tissue-resident memory T cells** | Barrier tissue of the original infection (CD69⁺, mostly CD103⁺ in epithelium) | Do not recirculate; can respond in situ within hours and recruit other cells |
| **Memory B cells** | Recirculate, and stay near the site of the original infection (such as the lung) | Differentiate rapidly into plasma cells |
| **Long-lived plasma cells** | Bone marrow, mucosal lamina propria | Secrete antibody continuously and maintain the protective titer in the serum |

Immunological memory thus also has a spatial structure: serum antibody is the first adaptive line of defense in the whole body, tissue-resident memory cells are the "outposts" at the site of the original infection, and central memory cells are the "reserves" in lymphoid organs ([7.15.18](/7.15.18)).

## 22.7. Tertiary Lymphoid Structures

**Definition 22.7.1 (Tertiary Lymphoid Structure)** An ordered aggregate of lymphocytes that forms de novo in nonlymphoid tissue, such as sites of chronic inflammation, autoimmunity, grafts and tumors, and has a tissue organization resembling that of secondary lymphoid organs is called a **tertiary lymphoid structure** (TLS): it contains B-cell follicles (with an FDC network and germinal centers when mature), adjacent T-cell zones, DCs, and high endothelial-like venules that express peripheral lymph node addressin.

"Tertiary" is relative to the **primary lymphoid organs** (first order) and the **secondary lymphoid organs** (second order). The development of secondary lymphoid organs is programmed and is established already in the embryo through interactions of lymphoid tissue inducer cells with stromal cells; TLSs, by contrast, are induced in adult tissue by persistent inflammation: activated lymphocytes and ILCs express lymphotoxin LTα1β2, which acts on LTβR on fibroblasts and endothelium in the tissue and induces CXCL13, CCL19, CCL21 and the differentiation of HEVs, and these signals in turn recruit more lymphocytes, forming a positive feedback; when inflammation resolves, the TLS usually disappears with it.

TLSs are divided by maturity into three stages: scattered lymphocyte aggregates, primary follicle-like structures without FDCs, and secondary follicle-like structures containing a CD21⁺/CD23⁺ FDC network and BCL6⁺ germinal centers. A mature TLS can carry out antigen presentation, B-cell affinity maturation and plasma cell production in situ in the tissue, without waiting for cells to travel to distant lymph nodes. Its significance varies with the context:

- In many solid tumors, the presence of a mature TLS is associated with a better prognosis and a better response to **immune checkpoint blockade**, possibly because TLSs support local antitumor T-cell and B-cell responses ([7.15.30](/7.15.30));
- In the synovium in rheumatoid arthritis, in the salivary glands in Sjögren syndrome and elsewhere, TLSs sustain local autoantibody production and are associated with persistence of the disease ([7.15.28](/7.15.28));
- In grafts undergoing chronic rejection, TLSs support local responses to alloantigens ([7.15.29](/7.15.29)).

In tissue sections, identification of a TLS relies on a spatial combination and not on a single marker: clusters of CD20⁺ B cells, an adjacent CD3⁺ T-cell zone, a CD21⁺ or CD23⁺ FDC network, PNAd⁺ HEVs (recognized by the MECA-79 antibody), BCL6⁺ or Ki-67⁺ germinal center B cells, and DC-LAMP⁺ mature DCs. The key to judging maturity is whether an FDC network and germinal centers are present (a systematic summary of markers is in [7.15.35](/7.15.35)).

## 22.8. Two Typical Response Pathways

The same set of mechanisms unfolds along different pathways depending on the route of infection. Only the immunological processes are described below.

A local barrier infection (skin as an example). At the first infection, keratinocytes and resident macrophages and mast cells sense the pathogen, and local inflammation recruits neutrophils; dermal DCs and epidermal Langerhans cells carry antigen to the draining lymph node, where they start T-cell and B-cell responses; about a week later effector T cells carrying skin homing molecules return to the site of infection and clear infected cells; afterward tissue-resident memory T cells remain in the skin. At reinfection of the same site, these resident memory cells recognize infected cells within hours and secrete IFN-γ, which puts the surrounding tissue into an antipathogen state and recruits circulating cells; many reinfections are controlled before symptoms appear.

An infection disseminated through the blood. Blood-borne antigen is first captured in the marginal zone of the spleen: marginal zone macrophages phagocytose particles, and **marginal zone B cells** produce IgM within days against TI antigens such as polysaccharides, activating complement and causing opsonization; at the same time splenic DCs carry antigen into the white pulp and start a T-cell-dependent response, and Kupffer cells in the liver also clear large numbers of particles from the blood. This pathway explains a clinical fact: people who have undergone splenectomy or have functional asplenia are particularly susceptible to bloodstream infections with encapsulated bacteria, because they have lost the marginal zone as a rapid, T-cell-independent humoral line of defense, and this is also why these people need to be vaccinated with the corresponding **conjugate vaccines** ([7.15.33](/7.15.33)).

## 22.9. Connection to Spatial Omics

**Spatial omics** ([7.9.6](/7.9.6)) turns "position is state" into a measurable quantity: by measuring dozens of proteins or thousands of genes simultaneously on sections that preserve tissue structure, each cell can be put back into its microenvironment. The content of this chapter supplies the questions that should be asked when interpreting such data:

- In which compartment is the cell (follicle, T-cell zone, dark zone or light zone of a germinal center, intraepithelial, perivascular)? The same cell type often has different programs in different compartments, for example B cells in the light zone of a germinal center and B cells in the mantle zone;
- Who is its neighbor? T–B pairs, three-cell clusters formed by CD8⁺ T cells with DCs and CD4⁺ T cells, and contacts between Tfh cells and germinal center B cells are all spatial evidence of a response in progress; the statistical analysis of **cellular neighborhoods** ([7.9.6](/7.9.6)) searches for such recurring combinations;
- At which point of the timeline are these structures? Early inflammatory infiltrates, mature TLSs and fibrotic scars can consist of the same cell types yet have completely different spatial organization.

Conversely, spatial data also have limits: a section is only one instant of the timeline, whereas most of the processes in this chapter are dynamic, and the movement of cells, the duration of contacts and the routes of homing can be obtained only from intravital imaging and tracing experiments.

## Summary

- Distribution: at any moment only about 2% of lymphocytes are in the blood; sentinels (resident innate cells and memory cells) are in peripheral tissues, and decisions about naive lymphocytes are made in secondary lymphoid organs; position determines state.
- Timeline: innate response (hours) → antigen reaches the lymph node (free antigen in minutes, DCs in 1–2 days) → T-cell activation and expansion (1–5 days) → B-cell activation and germinal center (2–21 days) → homing of effector cells and clearance (4–12 days) → contraction and memory (10–30 days).
- Two forms of antigen: unprocessed antigen goes to B cells (through lymphatic conduits, subcapsular sinus macrophages, FDCs), and processed peptide–MHC goes to T cells (through migratory DCs); the spleen captures blood-borne antigen.
- Search and recruitment: specific precursors are of the order of $10^{-6}$, and the lymph node raises its recruitment rate during inflammation by increasing blood flow and shutting its exit (Example 22.4.1); clonal expansion and the number of memory cells make up for the scarcity.
- The three-layer race (Example 22.5.1): innate immunity determines how fast the pathogen grows and adaptive immunity determines when it is cleared; the delay $\tau$ and growth rate $r$ together determine the peak load, and the value of memory and vaccines lies in shortening the delay and raising the starting point.
- Spatial structure of homing and memory: DCs at the site of activation imprint homing molecules; central memory is in lymphoid organs, effector memory in the circulation, tissue-resident memory in barriers and long-lived plasma cells in the bone marrow.
- **Tertiary lymphoid structure** (Definition 22.7.1): a lymphoid-organ-like structure that arises de novo in chronic inflammation, with maturity judged by the FDC and germinal center, and associated with tumor prognosis, autoimmunity and chronic rejection.

## Questions

1. In the model of Example 22.5.1, under what condition can the pathogen be controlled without any dependence on adaptive immunity? What situation does this correspond to biologically?

   **Answer** When the growth rate of the pathogen is smaller than the maximum killing rate of innate immunity, that is, $r < k_I I_{\max}$ (with $I_{\max} = s_I/d_I$), then once the innate effectors have risen $\mathrm{d}P/\mathrm{d}t < 0$, and the pathogen begins to decline before the adaptive response arrives. The corresponding situation is most low-virulence microbes encountered every day and small invading inocula: they are cleared within hours to days by barriers, complement, phagocytes and antimicrobial peptides and usually cause no obvious adaptive response. The model also illustrates the consequences of innate immunodeficiency: when $k_I$ or $I_{\max}$ falls, even a slowly growing pathogen that would have been controlled by innate immunity comes to depend on adaptive immunity, causing severe infection.

2. Use the estimate of Example 22.4.1 to explain why the secondary response mediated by memory T cells is much faster than the primary response. Give at least two different reasons.

   **Answer** (1) Memory cells are 10 to 1000 times more numerous than naive precursors, so $n$ is larger and the time to recruitment to the draining lymph node shortens in proportion; (2) tissue-resident memory cells are already at the site of infection and skip the step of "going to the lymph node to look for antigen" altogether, and effector memory cells can also enter inflamed tissue directly; (3) memory cells have a low activation threshold and depend little on costimulation, so after entering the lymph node the probability $s$ of being activated by a DC is higher, and they can produce effector molecules faster.

3. In one lymph node section, B cells are densely clustered, with a Ki-67⁺ population in the center and a ring of IgD⁺ cells around it; in another, tumor section, CD20⁺ B cells and CD3⁺ T cells are mixed together with no CD21⁺ network. Judge what state each is in and give your reasons.

   **Answer** The first is a secondary lymphoid follicle containing a germinal center: the Ki-67⁺ proliferating population is the germinal center (mainly centroblasts of the dark zone), and the outer ring of IgD⁺ cells is the mantle zone made up of naive B cells pushed to the periphery, which shows that a TD response is in progress. The second is a lymphocyte aggregate of B and T cells with no FDC network and no separate B-cell and T-cell zones; at most it is an immature tertiary lymphoid structure (the aggregate stage) that cannot yet support a local germinal center reaction; to judge whether it matures further, one should also look at PNAd⁺ HEVs and BCL6⁺ germinal center B cells.

4. Why do T cells induced by orally or intestinally administered antigen tend to return to the gut, whereas this is not the case after subcutaneous administration? What does this imply for the design of mucosal vaccines?

   **Answer** DCs in the Peyer's patches and mesenteric lymph nodes that drain the gut produce retinoic acid, which makes the T and B cells they activate express integrin α4β7 and CCR9; these cells bind MAdCAM-1 on gut endothelium and CCL25 secreted by the epithelium and therefore return to the small intestine. Antigen given subcutaneously is presented in lymph nodes draining skin or muscle, where DCs do not provide this signal, and the effector cells acquire skin or systemic homing molecules. The implication is that to establish resident memory and secretory IgA at a mucosa, antigen should preferably be presented at an inductive site of the mucosa (vaccination by a mucosal route), or other means should be used to guide effector cells to the mucosa ([7.15.23](/7.15.23), [7.15.33](/7.15.33)).
