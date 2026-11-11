---
title: Dynamics of T-Cell Responses and Immunological Memory
source_hash: 2d104d7dce42
---

The last question on the knowledge path is "how is it remembered and switched off after clearance?" The previous two chapters described how T cells are activated ([7.15.16](/7.15.16)) and which effector cells they differentiate into ([7.15.17](/7.15.17)); this chapter looks back at the process in terms of time: in an infection, a naive T-cell clone first proliferates by several orders of magnitude, then contracts by more than 90% after the antigen is cleared, leaving a small number of memory cells, which on the next encounter with the same antigen respond faster and more strongly. This is the cellular basis of the fourth property of adaptive immunity, memory, and it is also the principle by which vaccines work ([7.15.33](/7.15.33)). The chapter first gives the three phases of the response and its quantitative picture, then covers the fate decisions of effector cells and the subsets and maintenance of memory cells, and finally uses a kinetic model to place expansion, contraction and the recall response in one framework, and discusses exhaustion caused by chronic stimulation and the immunosenescence that appears with age. The time course of the antibody response (affinity maturation and memory B cells) is covered in [7.15.20](/7.15.20), the integration of the immune response in space and time in [7.15.22](/7.15.22), and the molecular mechanisms of exhaustion and checkpoints in [7.15.25](/7.15.25).

## 18.1. The Three Phases of the Response

**Definition 18.1.1 (Primary Immune Response)** The adaptive immune response elicited by the first exposure of the body to an antigen is called the **primary immune response**: it starts slowly and is weak, and effector molecules (effector T cells, antibodies) peak only days to two weeks later.

**Definition 18.1.2 (Clonal Expansion)** The process in which antigen-specific lymphocytes, once activated, increase the number of cells of that specificity by several orders of magnitude through repeated division is called **clonal expansion**.

Clonal expansion is the cellular content of the clonal selection theory ([7.15.1](/7.15.1)): the antigen does not create new specificities but selects existing clones and lets them proliferate massively. The primary response of a T cell has three phases:

| Phase | Time (mouse CD8⁺ T cells, acute viral infection) | What happens |
|---|---|---|
| Expansion | Days 1–8 after infection | Division begins about 1 day after activation, with a division every 6–8 h, and one cell can produce more than $10^4$ descendants; differentiation into effector cells and exit from the lymph node |
| Contraction | 1–2 weeks after day 8 | Antigen is cleared and 90%–95% of effector cells undergo apoptosis |
| Memory | Months to lifelong thereafter | The remaining cells become memory T cells, stable in number and ready to respond again |

In order of magnitude, naive precursor T cells for a particular pMHC are rare: about 1 in every $10^5$–$10^6$ naive T cells, only about $10^2$–$10^3$ in the whole mouse. Expansion brings them to $10^6$–$10^7$ at the peak of the response, a considerable fraction of CD8⁺ T cells. CD4⁺ T cells expand less (about $10^2$–$10^3$-fold) and contract less. The estimates of precursor frequency and expansion in chapter 1 ([7.15.1](/7.15.1)) find real data here: to produce enough effector cells, 4 orders of magnitude of expansion are needed first, and this expansion takes several days, which explains why the primary response is slower than innate immunity, and why in the first days of an infection defense relies mainly on innate immunity ([7.15.7](/7.15.7)).

## 18.2. Expansion: Programmed Division and Limits

Expansion has several notable features. First, the response is programmed: experiments show that after brief exposure to antigen and costimulation, CD8⁺ T cells can complete a predetermined round of division (about 7–10 or more divisions) without further antigen and acquire effector functions; strong and sustained stimulation can increase the number of divisions and the degree of effector differentiation. Second, division is limited: the proliferation of effector T cells is limited by the amount of antigen, growth factors such as IL-2, and the number of APCs and competition for them, so T cells of different precursor frequencies reach similar total numbers at the peak, and the more precursors there are, the smaller the expansion of each cell (see the model in §18.8). Third, effector cells leave the lymph node by downregulating CD69, CD62L and CCR7, re-expressing S1PR1, and turning to chemokines of the inflamed site ([7.15.4](/7.15.4), [7.15.22](/7.15.22)).

The cost of expansion is metabolic: activated T cells switch to aerobic glycolysis and glutamine metabolism to meet the biosynthetic needs of a division every 6–8 h (promoted by CD28 through PI3K–Akt–mTOR, [7.15.16](/7.15.16)), so T-cell responses are limited in tissues where nutrients or oxygen are restricted (such as the tumor microenvironment).

## 18.3. Fate Decisions of Effector Cells

The daughter cells of activation are not all alike: most differentiate into short-lived terminal effector cells, and a few retain differentiation potential and become precursors of memory cells.

| Type | Surface markers (mouse) | Transcription factors | Fate |
|---|---|---|---|
| Short-lived effector cell (SLEC) | KLRG1 high, IL-7 receptor α chain (CD127) low | T-bet high, Blimp-1 high | Strong killing function, die in the contraction phase |
| Memory precursor effector cell (MPEC) | KLRG1 low, CD127 high | EOMES, TCF-1, BCL6 | Survive and become memory cells |

What determines the fate is the total amount and quality of signals: the strength and duration of the antigen, costimulation, inflammatory cytokines (IL-12 and type I interferon raise T-bet and bias toward terminal effectors), competition for IL-2 and IL-7, and CD4 help (without CD4 help, CD8⁺ T cells complete the primary response but the memory formed performs poorly in the recall response, [7.15.16](/7.15.16)). One explanation is asymmetric division: at the first division, the daughter cell on the side in contact with the APC inherits more TCR signal and T-bet, while the cell on the other side retains potential; another explanation is that the strength of signals gradually accumulated within a population of cells determines the destination. All studies agree that the more divisions in the course of the response, the larger the memory pool formed.

## 18.4. Contraction

After the antigen is cleared, more than 90% of effector cells die, which is very important for "switching off" the response and for keeping the capacity of the T-cell pool stable:

- Withdrawal of growth factors: survival signals such as IL-2 decrease, the proapoptotic protein BIM rises, the antiapoptotic protein BCL-2 falls, and the cells go through the mitochondrial apoptotic pathway;
- Activation-induced cell death: repeated strong stimulation upregulates Fas and FasL, and cells undergo apoptosis through the death receptor pathway and are cleared by macrophages ([7.15.25](/7.15.25), [7.3.25](/7.3.25));
- Competitive suppression by Tregs and inhibitory receptors (CTLA-4, PD-1) also promote contraction ([7.15.17](/7.15.17)).

Defects in contraction (such as *FAS* mutations and BIM deficiency) cause lymphocytes to accumulate and produce autoimmunity ([7.15.24](/7.15.24), [7.15.31](/7.15.31)).

## 18.5. Memory T Cells

**Definition 18.5.1 (Memory T Cell)** T cells that survive after antigen activation, live long, and respond faster and more strongly than naive T cells on re-encountering the same antigen are called **memory T cells**.

Memory T cells differ from naive T cells in four ways:

- Higher precursor frequency: after the response, cells of the same specificity outnumber the naive precursors by 10–1000-fold;
- Lower activation threshold: a lower antigen concentration is needed, there is less dependence on costimulation, and they can be activated by macrophages and B cells (not only DCs);
- Faster effector function: in some cells the effector cytokine genes are in an epigenetically "poised" state and can be transcribed within hours of antigen contact;
- Different location: different subsets are distributed in lymphoid organs, blood and peripheral tissues.

Resting memory cells, like naive cells, have a quiescent metabolism, with the cell cycle arrested in G0 and energy derived mainly from oxidative phosphorylation of fatty acids, but with larger mitochondrial reserves so that glycolysis can be upregulated rapidly on activation. In the peripheral blood of healthy young adults, memory T cells make up about 35% of T cells, rising to about 60% after the age of 70, a result of accumulated antigen exposure and a reduction of naive T cells.

By location, phenotype and function, memory T cells fall into four subsets:

**Definition 18.5.2 (Central Memory T Cell)** A **central memory T cell** (TCM) is a memory T cell that expresses the lymph node homing molecules CCR7 and CD62L, is distributed mainly in secondary lymphoid organs and recirculates among them, has high proliferative potential, and on renewed antigen contact can expand rapidly and differentiate into the various effector cells.

**Definition 18.5.3 (Effector Memory T Cell)** An **effector memory T cell** (TEM) is a memory T cell that does not express CCR7 and patrols between peripheral tissues and blood; it displays effector functions (IFN-γ and others) almost immediately, but has lower proliferative potential and a shorter lifespan than TCM.

**Definition 18.5.4 (Tissue-Resident Memory T Cell)** A **tissue-resident memory T cell** (TRM) is a memory T cell that settles for a long time in peripheral tissues (skin, mucosa, lung, brain and others) and no longer recirculates; it expresses high CD69 and expresses the **integrin** CD103 (on CD8⁺ T cells), by which it is retained in the epithelium, and it is the earliest responder in situ on reinfection.

There are also stem-cell-like memory T cells (TSCM), very few in number and the least differentiated, which express CCR7 and CD62L like naive cells but also carry memory markers (Fas, the IL-2 receptor β chain CD122), have the capacity for self-renewal, and can generate all the other memory subsets.

| Subset | CCR7 | CD62L | CD45RA (human) | CD45RO (human) | CD69 | Main location | Functional features |
|---|---|---|---|---|---|---|---|
| Naive T cell | + | + | + | − | − | Lymphoid organs, blood | Can be activated only by DCs |
| TSCM | + | + | + | − | − | Secondary lymphoid organs | Self-renewal, generate other subsets |
| TCM | + | + | − | + | − | Secondary lymphoid organs | Produce IL-2, strong expansion capacity |
| TEM | − | Variable | − | + | Variable | Blood and peripheral tissues | Rapid production of effector cytokines |
| TRM | − | − | − | + | + | Skin, mucosa, lung, brain and others | Defense in situ |
| Effector T cell | − | − | + | − | − | Sites of inflammation | Killing and cytokines, short-lived |

CD45RA and CD45RO are two splice isoforms of CD45 and are the old markers distinguishing naive from memory cells in humans; effector cells can re-express CD45RA (TEMRA), so they must be used together with CCR7 (the combination of CD45RA, CD45RO, CCR7 and CD62L is summarized in the marker atlas of [7.15.35](/7.15.35)).

The relationship of the subsets is currently seen as a linear model: naive T cell → TSCM → TCM → TEM → terminal effector cell, with the degree of differentiation increasing and self-renewal and lifespan decreasing along the way; TRM come from precursors of TCM or TEM and complete their differentiation in the tissues. There is also evidence that effector cells can form TEM directly, and the two models are not mutually exclusive.

## 18.6. Maintenance of Memory

The number of memory T cells remains stable for years after antigen clearance, requiring neither antigen nor MHC:

| Signal | Role |
|---|---|
| IL-7 (IL-7Rα, CD127) | Survival signal: upregulates BCL-2; both CD4⁺ and CD8⁺ memory cells depend on it |
| IL-15 (IL-15Rβ, CD122, by trans-presentation) | Homeostatic proliferation of CD8⁺ memory cells; their slow homeostatic division lets the pool persist far longer than any single cell lives |
| TGF-β, local tissue signals | Maintain residence and survival of TRM in tissues |

Under the action of IL-7 and IL-15, memory cells divide slowly (each cell once every few weeks to months), and division balances death, keeping the pool stable over the long term; this is also called homeostatic proliferation. The receptors for these cytokines share the γc chain and the JAK–STAT pathway ([7.15.11](/7.15.11), [7.15.16](/7.15.16)), so patients with IL-7 receptor deficiency or γc deficiency lack T cells ([7.15.31](/7.15.31)).

## 18.7. Why the Recall Response Is Faster and Stronger

**Definition 18.7.1 (Secondary Immune Response)** The adaptive immune response mediated by memory cells when the body encounters the same antigen again is called the **secondary immune response** (also called the recall response): it has a short latent period and a high intensity, effector molecules peak within days, and the quality is also higher.

The secondary response is faster and stronger than the primary response because of the following factors acting together:

1. Number: cells of the same specificity are 10–1000-fold more numerous, so the starting point is higher, the probability of finding antigen is higher, and less expansion is needed ([7.15.3](/7.15.3));
2. Threshold: memory cells can respond to low antigen concentrations and weaker costimulation, and need not wait for DCs;
3. Speed: effector genes are poised, and the lag before proliferation is shortened (from about 1 day to about 0.5 day);
4. Location: TRM and TEM are already in peripheral tissues and can act immediately at the site of infection; TCM proliferate rapidly and differentiate into the various effector cells;
5. Cooperation: the cooperation of memory B cells and memory Tfh makes the antibody response faster and stronger ([7.15.20](/7.15.20)).

For T cells, the quality of the secondary response is not simply more but an earlier arrival at effective killing capacity: in viral reinfection, memory CD8⁺ T cells begin to produce IFN-γ and kill target cells 1–2 days after infection, and the virus may be cleared before the infected individual shows symptoms. The goal of a vaccine is to establish such a memory pool without causing disease ([7.15.33](/7.15.33)).

## 18.8. A Kinetic Model

Putting the points above into a single mathematical framework allows a check of quantitative consistency.

**Example 18.8.1 (Programmed Expansion, Contraction and Memory of the CD8⁺ T-Cell Response)** Suppose activated cells undergo $G$ divisions, the number of cells of generation $g$ is $A_g$ ($g = 0, \dots, G-1$), the number of effector cells is $E$ and the number of memory cells is $M$. The division rate is $r$ (mean division interval $1/r$), limited by a competition ceiling $K$ related to the total number of cells $N = \sum_g A_g + E + M$:

$$
\begin{aligned}
\frac{\mathrm{d}A_0}{\mathrm{d}t} &= -r s A_0, \qquad
\frac{\mathrm{d}A_g}{\mathrm{d}t} = 2 r s A_{g-1} - r s A_g \quad (g \ge 1), \\
\frac{\mathrm{d}E}{\mathrm{d}t} &= (1 - \varphi)\,2 r s A_{G-1} - \delta_E E, \qquad
\frac{\mathrm{d}M}{\mathrm{d}t} = \varphi\,2 r s A_{G-1} - \delta_M M,
\end{aligned}
$$

where $s = \max(0, 1 - N/K)$ acts while antigen is present (after the lag and before antigen clearance) and is 0 otherwise; cells that complete the division program become memory cells with probability $\varphi$ and the rest become effector cells; effector cells die at rate $\delta_E$ after antigen clearance, and memory cells decline slowly with a very small net death rate $\delta_M$. Take the illustrative parameters $G = 14$ ($2^{14} \approx 1.6 \times 10^4$-fold), $1/r = 7\,\mathrm{h}$, lag 1 d, antigen cleared on day 9, $K = 10^7$, $\varphi = 0.08$, $\delta_E = 0.5\,\mathrm{d^{-1}}$ (after clearance) and $\delta_M = 0.01\,\mathrm{d^{-1}}$.

The numerical solution gives the following. A clone with $10^2$ precursors reaches $1.5 \times 10^6$ cells on day 8 (an expansion of about $1.5 \times 10^4$-fold), then contracts by 95%, and on day 60 still has about $7.5 \times 10^4$ memory cells, about 750 times the starting number of precursors. With $10^3$ precursors the peak is reached on day 9 at about $9 \times 10^6$, contraction is about 96%, and the memory pool is about $3.9 \times 10^5$ (about 390 times the precursors). A clone with $10^4$ precursors is already limited by competition before reaching the ceiling $K$, the peak is about $10^7$, expansion is only about 1000-fold, and the memory pool is only about 17 times the precursors.

:::

This simple model reproduces several qualitative and quantitative facts: the number of cells at the peak is determined mainly by the ceiling $K$ and not by the number of precursors, and the more precursors there are, the less each cell expands, which is a competitive "immunodominance"; the 90%–95% contraction and the roughly $10^2$–$10^3$-fold increase over precursors (the memory pool) agree in order of magnitude with the data. A secondary response starting from the memory pool (taking a lag of 0.4 d, 6 divisions, and antigen cleared on day 5 because the response is faster) brings the cell number to $10^6$ in only about 0.7 day, whereas the primary response needs about 3.2 days, and it also reaches the $10^7$ range much faster: this is what "faster" means. What the model lacks is the diversity of cell fates (the four memory subsets), the dynamics of the pathogen (antigen clearance actually depends on the immune response itself) and transport between tissues, and the real response is far more complex; a more complete model would couple the antigen load to the killing by effector cells (the race model in [7.15.7](/7.15.7); methods for differential equations in [2.4](/2.4)), while the randomness of precursor numbers requires a stochastic model ([3.1](/3.1)).

![Programmed expansion, contraction and memory of the CD8⁺ T-cell response (illustrative parameters, see Example 18.8.1). A: Total number of antigen-specific cells (solid lines) and the number of memory cells among them (dashed lines) over time for three precursor numbers ($10^2$, $10^3$, $10^4$) (logarithmic axis); the peak is limited by the ceiling $K$, contraction after the peak is about 95%, and the memory pool remains stable over the long term. B: Comparison of the primary response started from $10^3$ naive precursors with the secondary response started from the roughly $3.9 \times 10^5$ memory cells it leaves behind: the secondary response has a higher starting point and shorter lag and reaches the ceiling faster](./plots/cd8-clonal-dynamics.py)

## 18.9. Exhaustion, Immunosenescence and Clinical Significance

The formation of memory depends on antigen being cleared. When antigen persists (chronic viral infections such as HIV, HBV and HCV, and tumors), T cells are stimulated continually and gradually lose function: first IL-2 and proliferative capacity, then TNF-α, and finally even IFN-γ and killing function are lost, with persistently high expression of inhibitory receptors such as PD-1, TIM-3 and LAG-3. This state is called T-cell exhaustion, distinct from anergy and regulation: it is a partially reversible differentiated state, and the progenitor exhausted cells that retain TCF-1 expression respond to checkpoint blockade and can generate new effector cells. The mechanisms of exhaustion and checkpoint therapy are covered in [7.15.25](/7.15.25) and [7.15.30](/7.15.30).

The problem at the other end is immunosenescence. The thymus involutes after puberty and the output of naive T cells decreases ([7.15.15](/7.15.15)); the adult naive T-cell pool is maintained by peripheral proliferation and repertoire diversity declines year by year, while repeated antigen exposure through life raises the proportion of memory cells, and chronic viruses (such as cytomegalovirus) also cause some of their clones to expand excessively and occupy immunological "space." The result is that older people respond more weakly to new antigens (new pathogens and new vaccines), responses to antigens already encountered are relatively preserved, and the level of chronic inflammation rises. In vaccination, adjuvants, high doses or multiple doses are used to compensate ([7.15.33](/7.15.33)), and vaccines that need to maintain baseline memory (such as influenza vaccines, updated every year) face the challenge of "original antigenic sin" (prior memory limiting the response to new variants) ([7.15.32](/7.15.32)).

## Summary

- The primary response of T cells (Definition 18.1.1) has three phases: clonal expansion (Definition 18.1.2, of the order of $10^4$-fold), contraction (90%–95% apoptosis) and memory. Precursors are rare ($10^{-5}$–$10^{-6}$), and several days of expansion are needed to have enough effector cells, so the primary response is slow.
- Expansion is programmed and limited by antigen, IL-2 and competition; the number of cells at the peak is determined mainly by the ceiling and not by the number of precursors.
- The daughters of activation divide into short-lived effector cells (KLRG1 high, CD127 low, T-bet high) and memory precursors (KLRG1 low, CD127 high, EOMES and TCF-1); the total amount and quality of signals, inflammation and CD4 help determine the destination.
- Contraction is carried out by withdrawal of growth factors (BIM) and activation-induced cell death.
- Memory T cells (Definition 18.5.1) fall into TSCM, TCM (Definition 18.5.2), TEM (Definition 18.5.3) and TRM (Definition 18.5.4), differing in surface markers (CCR7, CD62L, CD45RA/RO, CD69, CD103), location and function; along TSCM → TCM → TEM → effector cell, proliferative potential declines. The memory pool is maintained by IL-7 and IL-15 in the absence of antigen, and TRM are retained by tissue signals.
- Reasons the secondary response (Definition 18.7.1) is faster and stronger: more precursors, lower threshold, poised effector genes, closer location, and cooperation with memory B cells.
- Example 18.8.1: a model of programmed division + competition ceiling + fate probability reproduces expansion, contraction, memory and the speeding up of the secondary response.
- Chronic stimulation causes exhaustion, and thymic involution and accumulation of memory cause immunosenescence; both are relevant to vaccines and therapy.

## Questions

1. A mouse has $10^7$ naive CD8⁺ T cells, and the precursor frequency for a certain viral epitope is $10^{-5}$. If the number of cells of the clone at the peak of the response is $10^7$, by how many fold has it expanded? About how many divisions are needed? If each division takes 7 h on average, how long does this take?

   **Answer** The number of precursors is $10^7 \times 10^{-5} = 100$; $10^7/10^2 = 10^5$-fold. $\log_2 10^5 \approx 16.6$, that is, about 17 divisions (more if cells die). At 7 h each, this takes about $17 \times 7 \approx 120\,\mathrm{h}$, that is, 5 days; adding the lag of 1 day, about 6 days, consistent with the peak occurring 6–8 days after infection.

2. A patient lacks CD4⁺ T cells (as in advanced HIV infection). How do the primary response and memory of his CD8⁺ T cells change?

   **Answer** Without CD4 help, DCs cannot be fully "licensed" by CD40L and IL-2 is scarce, so the primary response of CD8⁺ T cells can occur but is weaker; the memory cells formed are few, the recall response is poor, and they are more susceptible to activation-induced death. In addition, lack of CD4⁺ T cells also impairs class switching and memory formation in B cells. In fact, HIV-infected people gradually lose CD8⁺ T-cell control of viruses such as CMV and EBV, and the response turns to an exhausted type ([7.15.16](/7.15.16), [7.15.31](/7.15.31)).

3. Why is it said that TRM are better suited than TCM to defend against pathogens invading through the skin or mucosa, whereas TCM are better suited to systemic infections?

   **Answer** TRM reside in the epithelial tissue that was previously infected and no longer recirculate; they display effector function directly in situ and respond first at the site of infection, without waiting for cells in the blood to arrive, but they are limited in number and have low proliferative potential. TCM are in secondary lymphoid organs and have strong proliferative capacity; after receiving antigen presented by DCs they expand rapidly and can differentiate into the various effector cells that reach the whole body through the blood, so they are suited to systemic infections requiring extensive expansion. The two form an "in situ plus reserve" cooperation.

4. According to Example 18.8.1, if the competition ceiling $K$ is raised to $10^8$, how does the peak of the clone with $10^4$ precursors change? If the time of antigen clearance is advanced to day 4, what is the effect on the size of the memory pool?

   **Answer** After $K$ is raised, the clone is no longer limited by competition, and the clone with $10^4$ precursors expands by programmed division to the order of $2^{14} \times 10^4 \approx 1.6 \times 10^8$ (approaching this limit under $K = 10^8$); the peak rises about 10-fold and the memory pool grows correspondingly ($\varphi \times$ peak). If antigen clearance is advanced to day 4, division stops, many cells do not complete 14 divisions, the total expansion is smaller, and the number of cells entering memory is correspondingly lower; this corresponds to "a weak, short stimulus produces less memory," consistent with the observation that the more divisions in the response, the larger the memory.

5. (Open question) The goal of vaccination is to establish memory. If rapid local protection in the intestinal mucosa is desired, how should the memory T-cell subsets and the route of vaccination be considered?

   **Answer** Ideas: TRM must be established in order to respond immediately in the mucosa, and the formation of TRM requires antigen and DCs in the local tissue (or draining lymph node) together with induction by local signals (TGF-β, IL-15), so mucosal vaccination (oral, intranasal) is more likely than intramuscular injection to induce mucosal TRM and IgA; injection mainly produces TCM, TEM and serum IgG. A strategy of systemic immunization first followed by mucosal boosting ("prime-pull" or "prime-boost") can be used, so that systemic memory cells are recruited to the mucosa and become TRM; the lifespan and turnover of TRM in tissue must also be considered ([7.15.23](/7.15.23), [7.15.33](/7.15.33)).
